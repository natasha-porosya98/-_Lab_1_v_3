print("Завдання 1")
S = int(input("Введіть початкову суму: "))
while not S or S<0:
    S = int(input("Початкова сума має бути більше 0: "))
p = float(input("Введіть процентову ставку: "))
while not p or p <= 0 or p >= 100:
    p = int(input("Процентова ставка має бути більше за 0 і менше за 100: "))
n = int(input("Введіть термін вкладення: "))
while not n or n<0 :
    n = int(input("Термін вкладення має бути більше 0: "))
A = S * (1 + p / 100) ** n
print("Нарахований депозитний вклад:", A)

print("Завдання 2")
while True:
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вийти")
    operation = input("Введіть номер операції (1/2/3/4/5): ")
    if operation == '5':
        break
    if operation in ('1', '2', '3', '4'):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if operation == '1':
            print(f"Результат: {num1} + {num2} = {num1 + num2}")
        elif operation == '2':
            print(f"Результат: {num1} - {num2} = {num1 - num2}")
        elif operation == '3':
            print(f"Результат: {num1} * {num2} = {num1 * num2}")
        elif operation == '4':
            if num2 != 0:
                print(f"Результат: {num1} / {num2} = {num1 / num2}")
            else:
                print("Помилка: Ділення на нуль неможливе.")
    else:
        print("Неправильний вибір. Спробуйте знову.")

print("Завдання 3")
mood = input("Який у вас настрій: ")
if not mood or mood=='-':
    print("Today, I am feeling neutral")
else:
    print(f"Today, I am feeling {mood}")