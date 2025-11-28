import os


class FinanceCalculator:

    def __init__(self):
        self.balance = 0
        self.list_of_transactions = []

    def add_transaction(self, type, amount, category):
        amount = float(amount)
        if type == "Доход":
            self.balance += amount
        elif type == "Расход":
            self.balance -= amount

        transaction = {
            'type': type,
            'amount': amount,
            'category': category,
        }
        self.list_of_transactions.append(transaction)

    def get_transactions(self):
        return self.list_of_transactions

    def get_balance(self):
        return self.balance

    def save_data(self):
        with open("data.txt", 'w', encoding='utf-8') as file:
            file.write(f"balance:{self.balance}\n")

            for transaction in self.list_of_transactions:
                file.write(f"{transaction['type']},{transaction['amount']},{transaction['category']}\n")

    def show_balance_and_transactions(self):
        print(f" Баланс: {self.balance} ")

        if not self.list_of_transactions:
            print("Транзакций нет.")
            return

    def load_data(self):
        if os.path.exists("data.txt"):
            with open("data.txt", 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    balance_line = lines[0]
                    if balance_line.startswith("balance:"):
                        self.balance = float(balance_line.split(":")[1])

    def run(self):
        self.load_data()
        while True:
            print(
                "\n1 - доход / расход \n2 - просмотр баланса и транзакций \n3 -завершение программы \nвыберите действие:")
            command = input()
            if command == "1":
                print("доход/расход")
                self.add_transaction(input("Введите тип: "), input("ВВедите сумму: "), input("Введите категорию: "))
            elif command == "2":
                print("просмотр баланса и транзакций")
                self.show_balance_and_transactions()

            elif command == "3":
                print("завершение программы")
                self.save_data()
                break


if __name__ == '__main__':
    x = FinanceCalculator()
    x.run()
