from user import User
class Controller:
    userList: list

    def _run(self):
        pass

    def create_user(self, login: string, password: string):
        pass
    def checkAuthorization(self, login: string, password: string):
        pass
    def add_spending(self, user: User):
        pass
    def delete_spenging(self, id: int):
        pass
    def change_spending(self, id: int):
        pass

    def add_income(self, user: User):
        pass
    def delete_income(self, id: int):
        pass
    def change_income(self, id: int):
        pass

    def create_category(self, user: User):
        pass
    def delete_category(self, id: int):
        pass
    def change_category(self, id: int):
        pass

    def add_debt(self,user: User):
        pass
    def delete_debt(self,id: int):
        pass
    def change_debt(self, id: int):
        pass

    def add_transaction(self, user: User):
        pass
    def change_transaction(self, id: int):
        pass
    def add_piggy_bank(self, user: User):
        pass
    def change_piggy_bank(self, id: int):
        pass
    def delete_piggy_bank(self, id: int):
        pass
    def create_file(self, user: User):
        pass
    def open_file(self, user: User):
        pass
