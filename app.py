"""
Menu:
- user management
    - list users
    - select user
    - create user
    - delete user
- account management
    - finances overview
    - list accounts
    - select account
        - print balance
        - print operation history
            - time constrained
                - month
                - year
            - category constrained
        - add transaction
        - modify transaction
        - remove transaction
    - create account
    - delete account
    - rename account
- category management
    - list categories
    - create category
    - delete category
    - rename category
- add transaction
"""


def main_menu():
    print("""
    Main Menu

    't' - Add transaction
    'u' - User management
    'a' - Account management
    'c' - Category management
    'Q' - Close application

    Select action above
    """)
    user_selection = input()
    if user_selection == 'Q':
        pass
    elif user_selection == 'c':
        category_submenu()
    elif user_selection == 'a':
        account_submenu()
    elif user_selection == 'u':
        user_submenu()
    elif user_selection == 't':
        pass
    else:
        print("Incorrect command, please try again.")
        main_menu()

def user_submenu():
    print("""
    User Management
    
    'l' - List users
    'r' - Rename user
    's' - Select user
    'n' - Create new user
    'D' - Delete user
    'B' - Go back to Main Menu
    'Q' - Close application
    
    Select action above
    """)
    user_selection = input()
    if user_selection == 'Q':
        pass
    elif user_selection == 'B':
        main_menu()
    elif user_selection == 'D':
        pass
    elif user_selection == 'n':
        pass
    elif user_selection == 's':
        pass
    elif user_selection == 'r':
        pass
    elif user_selection == 'l':
        pass
    else:
        print("Incorrect command, please try again.")
        user_submenu()

def account_submenu():
    print("""
    Account Management

    'f' - Finances overview
    'l' - List account
    'r' - Rename account
    's' - Select account
    'n' - Create new account
    'D' - Delete account
    'B' - Go back to Main Menu
    'Q' - Close application
    
    Select action above
    """)
    user_selection = input()
    if user_selection == 'Q':
        pass
    elif user_selection == 'B':
        main_menu()
    elif user_selection == 'D':
        pass
    elif user_selection == 'n':
        pass
    elif user_selection == 's':
        select_account()
    elif user_selection == 'r':
        pass
    elif user_selection == 'l':
        pass
    elif user_selection == 'f':
        pass
    else:
        print("Incorrect command, please try again.")
        account_submenu()


def selected_account_submenu(account_name):
    print(f"""
    Account {account_name}

    'b' - Show balance
    'l' - List account transactions
            - time constrained
                - month
                - year
            - category constrained
    't' - Add transaction
    'm' - Modify transaction
    'D' - Delete transaction
    'B' - Go back to Accounts Submenu
    'M' - Go back to Main Menu
    'Q' - Close application

    Select action above
    """)
    user_selection = input()
    if user_selection == 'Q':
        pass
    elif user_selection == 'M':
        main_menu()
    elif user_selection == 'B':
        account_submenu()
    elif user_selection == 'b':
        pass
    elif user_selection == 'l':
        pass
    elif user_selection == 't':
        pass
    elif user_selection == 'm':
        pass
    elif user_selection == 'D':
        pass
    else:
        print("Incorrect command, please try again.")
        selected_account_submenu(account_name)

def select_account() -> None:
    print("Select which account?: ")
    user_selection = input()
    selected_account_submenu(user_selection)
    return None


def category_submenu():
    print("""
    Category Management

    'l' - List categories
    'r' - Rename category
    'n' - Create new category
    'D' - Delete category
    'B' - Go back to Main Menu
    'Q' - Close application
    
    Select action above
    """)
    user_selection = input()
    if user_selection == 'Q':
        pass
    elif user_selection == 'B':
        main_menu()
    elif user_selection == 'D':
        pass
    elif user_selection == 'n':
        pass
    elif user_selection == 'r':
        pass
    elif user_selection == 'l':
        pass
    else:
        print("Incorrect command, please try again.")
        category_submenu()


if __name__ == "__main__":
    main_menu()
    