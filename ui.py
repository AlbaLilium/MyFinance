from __future__ import annotations
import pygame
import pygame_menu


class Page:
    def draw(self):
        pass


class EnterPage(Page):
    is_first_enter: bool = True

    def draw_first_enter_windows(self):
        self.menu.clear()
        self.menu.add.button('Create database', self.draw_registration_windows)
        self.menu.add.button('Open database', self.draw_authorization_windows)
    def draw_registration_windows(self):
        self.menu.clear()
        self.menu.add.text_input('Registration')
        self.menu.add.text_input('Login: ', default='login')
        self.menu.add.text_input('Password: ', default='password')
        self.menu.add.button('Ok', BudgetPage().draw)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)
    def draw_authorization_windows(self):
        self.menu.clear()
        self.menu.add.text_input('Authorisation')
        self.menu.add.text_input('Login: ', default='login')
        self.menu.add.text_input('Password: ', default='password')
        self.menu.add.button('Ok', BudgetPage().draw)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)
    def draw(self):
        pygame.init()
        self.menu = pygame_menu.Menu('Finance manager', 1000, 800, theme=pygame_menu.themes.THEME_DARK)
        self.menu.clear()
        self.draw_first_enter_windows()


class BudgetPage(Page):
    def pressed_add_button(self):
        pass
    def pressed_delete_button(self):
        pass
    def pressed_change_button(self):
        pass
    def draw(self):
        pygame.init()
        surface = pygame.display.set_mode((1000, 800))
        self.menu = pygame_menu.Menu('Finance manager', 1000, 800, theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.text_input('Budget')
        self.menu.add.button('Category', CategoryPage().draw)
        self.menu.add.button('Debts', DebtsPage().draw)
        self.menu.add.button('Transaction', TransactionPage().draw)
        self.menu.add.button('Piggy Bank', PiggyBankPage().draw)
        self.menu.add.button('Settings', SettingsPage().draw)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)
        while True: self.menu.mainloop(surface)

class CategoryPage(Page):
        def pressed_add_button(self):
            pass
        def pressed_delete_button(self):
            pass
        def pressed_change_button(self):
            pass
        def draw(self):
            pygame.init()
            surface = pygame.display.set_mode((1000, 800))
            self.menu = pygame_menu.Menu('Finance manager', 1000, 800, theme=pygame_menu.themes.THEME_DARK)
            self.menu.add.text_input('Category')
            self.menu.add.button('Budget', BudgetPage().draw)
            self.menu.add.button('Debts', DebtsPage().draw)
            self.menu.add.button('Transaction', TransactionPage().draw)
            self.menu.add.button('Piggy Bank', PiggyBankPage().draw)
            self.menu.add.button('Settings', SettingsPage().draw)
            self.menu.add.button('Exit', pygame_menu.events.EXIT)
            while True: self.menu.mainloop(surface)

class DebtsPage(Page):
        def pressed_add_button(self):
            pass
        def pressed_delete_button(self):
            pass
        def pressed_change_button(self):
            pass
        def draw(self):
            pygame.init()
            surface = pygame.display.set_mode((1000, 800))
            self.menu = pygame_menu.Menu('Finance manager', 1000, 800, theme=pygame_menu.themes.THEME_DARK)
            self.menu.add.text_input('Debts')
            self.menu.add.button('Budget', BudgetPage().draw)
            self.menu.add.button('Category', CategoryPage().draw)
            self.menu.add.button('Transaction', TransactionPage().draw)
            self.menu.add.button('Piggy Bank', PiggyBankPage().draw)
            self.menu.add.button('Settings', SettingsPage().draw)
            self.menu.add.button('Exit', pygame_menu.events.EXIT)
            while True: self.menu.mainloop(surface)

class PiggyBankPage(Page):
        def pressed_add_button(self):
            pass
        def pressed_delete_button(self):
            pass
        def pressed_change_button(self):
            pass
        def draw(self):
            pygame.init()
            surface = pygame.display.set_mode((1000, 800))
            self.menu = pygame_menu.Menu('Finance manager', 1000, 800, theme=pygame_menu.themes.THEME_DARK)
            self.menu.add.text_input('Piggy Bank')
            self.menu.add.button('Budget', BudgetPage().draw)
            self.menu.add.button('Category', CategoryPage().draw)
            self.menu.add.button('Debts', DebtsPage().draw)
            self.menu.add.button('Transaction', TransactionPage().draw)
            self.menu.add.button('Settings', SettingsPage().draw)
            self.menu.add.button('Exit', pygame_menu.events.EXIT)
            while True: self.menu.mainloop(surface)

class TransactionPage(Page):
        def pressed_add_button(self):
            pass
        def pressed_delete_button(self):
            pass
        def pressed_change_button(self):
            pass
        def draw(self):
            pygame.init()
            surface = pygame.display.set_mode((1000, 800))
            self.menu = pygame_menu.Menu('Finance manager', 1000, 800, theme=pygame_menu.themes.THEME_DARK)
            self.menu.add.text_input('Transaction')
            self.menu.add.button('Budget', BudgetPage().draw)
            self.menu.add.button('Category', CategoryPage().draw)
            self.menu.add.button('Debts', DebtsPage().draw)
            self.menu.add.button('Piggy Bank', PiggyBankPage().draw)
            self.menu.add.button('Settings', SettingsPage().draw)
            self.menu.add.button('Exit', pygame_menu.events.EXIT)
            while True: self.menu.mainloop(surface)

class SettingsPage(Page):
        def pressed_button(self):
            pass
        def draw(self):
            pygame.init()
            surface = pygame.display.set_mode((1000, 800))
            self.menu = pygame_menu.Menu('Finance manager', 1000, 800, theme=pygame_menu.themes.THEME_DARK)
            self.menu.add.text_input('Settings')
            self.menu.add.button('Budget', BudgetPage().draw)
            self.menu.add.button('Category', CategoryPage().draw)
            self.menu.add.button('Debts', DebtsPage().draw)
            self.menu.add.button('Transaction', TransactionPage().draw)
            self.menu.add.button('Piggy Bank', PiggyBankPage().draw)
            self.menu.add.button('Exit', pygame_menu.events.EXIT)
            while True: self.menu.mainloop(surface)

