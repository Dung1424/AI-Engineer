import argparse
import json
from pathlib import Path

import numpy as np
from datasets import load_dataset
from sklearn.metrics import accuracy_score, f1_score
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
)

MODEL = "distilbert-base-multilingual-cased"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=3)
    args = parser.parse_args()
    dataset = load_dataset("json", data_files="data/intents.jsonl", split="train")
    labels = sorted(set(dataset["label"]))
    label2id = {label: index for index, label in enumerate(labels)}
    dataset = dataset.map(lambda row: {"labels": label2id[row["label"]]})
    split = dataset.train_test_split(test_size=0.25, seed=42)
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    tokenized = split.map(lambda batch: tokenizer(batch["text"], truncation=True), batched=True)
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL, num_labels=len(labels), id2label=dict(enumerate(labels)), label2id=label2id
    )

    def metrics(output):
        prediction = np.argmax(output.predictions, axis=1)
        return {
            "accuracy": accuracy_score(output.label_ids, prediction),
            "macro_f1": f1_score(output.label_ids, prediction, average="macro"),
        }

    trainer = Trainer(
        model=model,
        args=TrainingArguments(
            output_dir="artifacts/checkpoints",
            num_train_epochs=args.epochs,
            per_device_train_batch_size=8,
            per_device_eval_batch_size=8,
            eval_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
            metric_for_best_model="macro_f1",
            seed=42,
            report_to="none",
        ),
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["test"],
        processing_class=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer),
        compute_metrics=metrics,
    )
    trainer.train()
    result = trainer.evaluate()
    trainer.save_model("artifacts/model")
    tokenizer.save_pretrained("artifacts/model")
    Path("artifacts/labels.json").write_text(json.dumps(labels, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
