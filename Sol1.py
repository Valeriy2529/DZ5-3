
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, \
    QMainWindow, QFormLayout
from PyQt6.QtGui import QIcon, QPixmap, QFont

#Класс LoginPage представляет собой окно для авторизации пользователей.
class LoginPage(QWidget):

    def center_window(window):
        qr = window.frameGeometry()
        cp = window.screen().availableGeometry().center()
        qr.moveCenter(cp)
        window.move(qr.topLeft())

    def __init__(self):
        super().__init__()
        self.setFixedSize(250, 230) # Позиция и размеры окна
        self.setWindowTitle("Авторизация")  # Заголовок окна
        self.show()
        self.setWindowIcon(QIcon("../Images/cooking.png"))  # Иконка приложения


        # Установка цвета фона
        self.setStyleSheet("background-image: url(../Images/natural.jpg);")  # Цвет фона

        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(3600,3600)

        # Создаем вертикальный layout (компоновщик)
        self.form_layout = QFormLayout()

        self.label_welcome = QLabel("АВТОРИЗАЦИЯ")
        self.label_welcome.setStyleSheet("font: bold; font-size: 16pt")
        self.label_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_welcome.setFixedSize(250, 35)

        self.label_welcome.setMinimumSize(2, 15)

        # Создание меток и полей ввода
        self.username_label = QLabel("Логин:")
        self.username_label.setStyleSheet("font: bold; font-size: 10pt")
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("font: bold; font-size: 10pt")
        self.username_input.setFixedSize(150, 35)

        self.password_label = QLabel("Пароль:")
        self.password_label.setStyleSheet("font: bold; font-size: 10pt")
        self.password_input = QLineEdit()
        self.password_input.setFixedSize(150, 35)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Скрыть ввод пароля

        # Создание кнопки для авторизации
        self.login_button = QPushButton("Войти")
        self.login_button.setStyleSheet("font: bold; font-size: 10pt")
        self.login_button.clicked.connect(self.handle_login)
        self.login_button.setFixedSize(100, 35)

        # Добавление элементов в компоновщик формы
        self.form_layout.addRow(self.label_welcome)
        self.form_layout.addRow(self.username_label, self.username_input)
        self.form_layout.addRow(self.password_label, self.password_input)
        self.form_layout.addRow(self.login_button)

        # Основной компоновщик, чтобы собрать элементы вместе
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.form_layout)
        main_layout.addWidget(self.login_button)

        # Установка главного компоновщика для виджета
        self.setLayout(main_layout)

    # Обработка входа
    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Простейшая проверка для демонстрации
        if username == "admin" and password == "1357":
            self.show_profile_page()
        else:
            QMessageBox.warning(self, "Ошибка!", "Неправильное имя пользователя или пароль.")

    def show_profile_page(self):
        self.profile_window = ProfilePage()
        self.profile_window.show()
        self.close()  # Закрываем окно авторизации

# Класс ProfilePage представляет собой окно личного профиля пользователя.
class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Личная страничка")
        self.setWindowIcon(QIcon("../Images/cooking.png"))
        self.setFixedSize(350, 350)

        # Установка цвета фона
        self.setStyleSheet("background-color: #fffafa;")

        layout = QVBoxLayout()

        self.label_welcome = QLabel("Добро пожаловать в личный профиль!")
        layout.addWidget(self.label_welcome)

        # Добавление изображения
        self.image = QLabel()
        self.pixmap = QPixmap("../Images/panda.jpg")  # путь к изображению
        self.image.setPixmap(self.pixmap)
        layout.addWidget(self.image)

        self.setLayout(layout)

# Создается экземпляр приложения и отображается экран авторизации.
# Используется sys.exit(app.exec()) для корректного завершения приложения.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec())
