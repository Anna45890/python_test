import random

print("Привет! Я загадала число от 1 до 100.")
print("Попробуй угадать! У тебя 10 попыток.")

secret_number = random.randint(1, 100)

attempts = 0

while attempts < 10:
    your_number = int(input("Введи число: "))
    attempts += 1
    if your_number > secret_number:
        print("Число слишком большое.")
    elif your_number < secret_number:
        print("Число слишком маленькое.")
    else:
        print("Поздравляю! Вы угадали число!")
        print(f"Количество попыток: {attempts}")
        break
else:
    print(f"Вы не угадали число. Это было {secret_number}")