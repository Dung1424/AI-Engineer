# Hàm

def greet(name):
    return "Hello " + name

message = greet("Dung")
print(message)

def calculate_average(scores):
    total = sum(scores)
    return total / len(scores)

result = calculate_average([8, 9, 10])
print(result)