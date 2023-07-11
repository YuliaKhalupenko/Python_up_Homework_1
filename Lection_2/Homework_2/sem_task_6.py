# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю +
# ✔ Допустимые действия: пополнить, снять, выйти +
# ✔ Сумма пополнения и снятия кратны 50 у.е. +
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.+
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3% +
# ✔ Нельзя снять больше, чем на счёте +
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной +
# ✔ Любое действие выводит сумму денег +


def check_amount(amount):
    if amount % 50 == 0:
        return True
    else:
        print("Сумма должна быть кратной 50!")
        return False


def calculate_interest(balance, operations_count):
    if operations_count >= 3:
        balance *= 0.97  # Начисляем проценты в размере 3%
        balance = round(balance, 2)
        print("Начислены проценты 3%.")
        print("Общий счет после начисления процентов:", balance, "y.e.")
    return balance


def deduct_wealth_tax(balance):
    if balance > 5000000:
        wealth_tax = balance * 0.1  # Вычитаем налог на богатство 10%
        wealth_tax = round(wealth_tax, 2)
        balance -= wealth_tax
        print("Вычтен налог на богатство:", wealth_tax, "y.e.")
        print("Общий счет после вычета налога на богатство:",
              round(balance, 2), "y.e.")
    return balance


def calculate_withdrawal_fee(amount):
    withdrawal_fee = amount * 0.015  # 1.5% от суммы снятия
    withdrawal_fee = max(withdrawal_fee, 30)  # не менее 30 у.е.
    withdrawal_fee = min(withdrawal_fee, 600)  # не более 600 у.е.
    return withdrawal_fee


def deposit(balance, operations_count):
    amount = int(input("\nВведите сумму для пополнения (кратную 50): "))
    if check_amount(amount):
        balance += amount
        # Проверяем и вычитаем налог на богатство
        balance = round(deduct_wealth_tax(balance), 2)

        print("Счет пополнен на", amount, "у.е.")
        print("Общий счет:", balance, "y.e.")
        operations_count += 1
        balance = calculate_interest(balance, operations_count)
    return balance, operations_count


def withdraw(balance, operations_count):
    amount = int(input("\nВведите сумму для снятия (кратную 50): "))
    if check_amount(amount):
        if amount <= balance:
            balance = deduct_wealth_tax(balance)

            withdrawal_fee = round(calculate_withdrawal_fee(amount), 2)
            balance -= withdrawal_fee

            balance -= amount
            print("Вы сняли", amount, "у.е.")
            print("Процент за снятие:", withdrawal_fee, "у.е.")
            print("Общий счет:", round(balance, 2), "y.e.")
            operations_count += 1
            balance = calculate_interest(balance, operations_count)
        else:
            print("Недостаточно средств на счете!")
    return balance, operations_count


def atm():
    balance = 0
    operations_count = 0

    while True:
        print("\n1. Пополнить счет")
        print("2. Снять деньги")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ")

        match choice:
            case "1":
                balance, operations_count = deposit(balance, operations_count)
            case "2":
                balance, operations_count = withdraw(balance, operations_count)
            case "3":
                print("До свидания!")
                break
            case _:
                print("Некорректный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    atm()
