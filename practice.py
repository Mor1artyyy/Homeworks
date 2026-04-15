class Database:
    """
    База данных для хранения данных пользователя
    """
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == "__main__":
    db = Database()
    while True:
        choice = int(input("Здравствуйте! Выберите действие: \n1 - Вход:\n2 - Регистрация:\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in db.data:
                if password == db.data[login]:
                    print(f'Добро пожаловать, {login}!')
                    break
                else:
                    print("Неверный пароль!")
            else:
                print("Пользователь не найден!")
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте еще раз!")
                continue
            db.add_user(user.username, user.password)