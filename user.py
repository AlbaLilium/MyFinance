from budget import Budget
from category import Category
from transaction import Transaction
from piggy_bank import PiggyBank
from debt import  Debt
from file import  File

class User:
    __login: string
    __password: string
    budget: Budget
    debts: list
    transaction: list
    piggy_banks: list
    file: File

    def change_passoword(self, new_password: string):
        pass
    def check_login_and_password(self, login: string, password: string):
        pass
    def create_budget(self):
        pass
    def create_debts(self):
        pass
    def create_transaction(self):
        pass
    def create_piggy_banks(self):
        pass
    def create_file(self):
        pass
    def open_file(self):
        pass