import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext

knowledge_base = {
    "HTML": "HTML (HyperText Markup Language) - это язык разметки, используемый для создания структуры веб-страниц. "
            "Он позволяет определять заголовки, абзацы, изображения, ссылки и другие элементы.",
    "CSS": "CSS (Cascading Style Sheets) - это язык стилей, который управляет внешним видом веб-страницы: цветами, шрифтами, "
           "размерами и позиционированием элементов.",
    "JavaScript": "JavaScript - это язык программирования, который позволяет создавать интерактивные элементы на веб-страницах, "
                  "такие как анимации, обработка событий и динамическое обновление контента.",
    "Python": "Python - это мощный язык программирования, который используется как для серверной части веб-приложений, так и для "
              "разработки скриптов. Популярные фреймворки для веба включают Django и Flask.",
    "Django": "Django - это высокоуровневый фреймворк на Python для быстрой разработки веб-приложений. Он предоставляет готовую систему "
              "аутентификации, админ-панель и ORM для работы с базами данных.",
    "Flask": "Flask - это легковесный веб-фреймворк на Python, который позволяет создавать веб-приложения с минимальной архитектурой.",
    "API": "API (Application Programming Interface) - это интерфейс для взаимодействия между различными приложениями. REST и GraphQL "
           "являются популярными подходами для создания API.",
    "SQL": "SQL (Structured Query Language) - это язык запросов для работы с базами данных. Он используется для создания, изменения, "
           "чтения и удаления данных в базах данных.",
    "Git": "Git - это система контроля версий, которая помогает отслеживать изменения в коде. Git позволяет работать в командах и управлять "
           "разработкой с помощью репозиториев.",
}

example_website = """
<!DOCTYPE html>
<html>
<head>
    <title>Пример сайта</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #fff3e0; }
        header { background-color: #ff9800; padding: 20px; text-align: center; color: black; }
        section { margin: 20px; padding: 20px; background-color: white; border-radius: 5px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
        footer { background-color: #ffcc80; text-align: center; padding: 10px; margin-top: 20px; }
    </style>
</head>
<body>
    <header>
        <h1>Добро пожаловать на мой сайт</h1>
    </header>
    <section>
        <h2>Обо мне</h2>
        <p>Привет! Я начинающий веб-разработчик, изучающий HTML, CSS и JavaScript.</p>
    </section>
    <footer>
        <p>Контакты: email@example.com</p>
    </footer>
</body>
</html>
"""


learning_material = [
    ("Шаг 1. Основы HTML", """
HTML (HyperText Markup Language) – это язык разметки, который используется для создания структуры веб-страниц. 
Каждая веб-страница начинается с тега <html>, который содержит блоки <head> и <body>. 
Тег <head> содержит метаданные страницы, а <body> включает видимый контент, такой как текст, изображения, ссылки и т. д.
Пример HTML:
<!DOCTYPE html>
<html>
<head>
    <title>Пример сайта</title>
</head>
<body>
    <h1>Заголовок страницы</h1>
    <p>Это абзац текста.</p>
</body>
</html>
    """),
    ("Шаг 2. Основы CSS", """
CSS (Cascading Style Sheets) – это язык, который описывает внешний вид HTML-элементов на веб-странице. 
CSS позволяет задавать стили, такие как цвет текста, размеры шрифтов, отступы, границы и фон. 
Внешние стили подключаются через тег <link> в разделе <head> HTML-документа.
Пример CSS:
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}
h1 {
    color: #ff9800;
}
    """),
    ("Шаг 3. Основы JavaScript", """
JavaScript – это язык программирования, который добавляет интерактивность веб-страницам. 
Он может изменять содержимое страницы в реальном времени, реагировать на действия пользователя, такие как клики или ввод данных.
Пример JavaScript:
<script>
    document.getElementById('demo').innerHTML = 'Привет, мир!';
</script>
    """),
    ("Шаг 4. Основы серверного программирования с Python", """
Python широко используется для серверной части веб-приложений. Django и Flask – это два популярных фреймворка для создания сайтов на Python.
Django предлагает полную инфраструктуру для разработки, а Flask является легковесным решением, которое позволяет разрабатывать гибкие и простые приложения.
Пример сервера на Flask:
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Привет, мир!'
if __name__ == '__main__':
    app.run()
    """)
]


quiz_data = [
    {"question": "Что такое HTML?", "options": ["Язык программирования", "Язык разметки", "База данных"],
     "answer": "Язык разметки"},
    {"question": "Для чего используется CSS?",
     "options": ["Создание логики сайта", "Оформление стилей", "Работа с сервером"], "answer": "Оформление стилей"},
    {"question": "Какой язык программирования используется для создания интерактивности на веб-странице?",
     "options": ["Python", "JavaScript", "HTML"], "answer": "JavaScript"},
    {"question": "Какой фреймворк на Python популярен для создания серверных приложений?",
     "options": ["Django", "Flask", "React"], "answer": "Django"},
    {"question": "Что такое API?", "options": ["Программное обеспечение", "Интерфейс для взаимодействия", "Приложение"],
     "answer": "Интерфейс для взаимодействия"},
]


class WebDevApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Учебное приложение по веб-разработке")
        self.geometry("1000x800")
        self.configure(bg='#fff3e0')

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self, bg='#fff3e0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        title_label = tk.Label(main_frame, text="Изучайте веб-разработку", font=("Arial", 28, "bold"), bg='#fff3e0',
                               fg='black')
        title_label.pack(pady=20)

        button_frame = tk.Frame(main_frame, bg='#fff3e0')
        button_frame.pack(pady=10)

        btn_knowledge = tk.Button(button_frame, text="База знаний", width=20, height=2,
                                  command=self.show_knowledge_slides, bg='#ff9800', fg='black',
                                  font=("Arial", 14, "bold"))
        btn_knowledge.grid(row=0, column=0, padx=20, pady=10)

        btn_learning = tk.Button(button_frame, text="Учебный материал", width=20, height=2,
                                 command=self.show_learning_slides, bg='#ff9800', fg='black',
                                 font=("Arial", 14, "bold"))
        btn_learning.grid(row=0, column=1, padx=20, pady=10)

        btn_example = tk.Button(button_frame, text="Пример сайта", width=20, height=2,
                                command=self.show_website_example, bg='#ff9800', fg='black', font=("Arial", 14, "bold"))
        btn_example.grid(row=0, column=2, padx=20, pady=10)

        btn_quiz = tk.Button(button_frame, text="Пройти тест", width=20, height=2, command=self.start_quiz,
                             bg='#ff9800', fg='black', font=("Arial", 14, "bold"))
        btn_quiz.grid(row=1, column=0, columnspan=3, pady=20)

    def show_knowledge_slides(self):
        self.knowledge_index = 0
        self.knowledge_window = tk.Toplevel(self)
        self.knowledge_window.title("База знаний")
        self.knowledge_window.geometry("800x600")

        self.knowledge_label = tk.Label(self.knowledge_window, text=list(knowledge_base.keys())[self.knowledge_index],
                                        font=("Arial", 20, "bold"), bg='#fff3e0', fg='black')
        self.knowledge_label.pack(pady=10)

        self.knowledge_text = scrolledtext.ScrolledText(self.knowledge_window, wrap="word", font=("Arial", 14),
                                                        height=15, bg='#fff', fg='black')
        self.knowledge_text.pack(fill="both", expand=True)
        self.show_knowledge_content()

        
        button_frame = tk.Frame(self.knowledge_window, bg='#fff3e0')
        button_frame.pack(pady=10)

        self.prev_button = tk.Button(button_frame, text="Назад", command=self.show_prev_knowledge_slide,
                                     state="disabled", bg='#ff9800', fg='black', font=("Arial", 14))
        self.prev_button.grid(row=0, column=0, padx=20)

        self.next_button = tk.Button(button_frame, text="Вперед", command=self.show_next_knowledge_slide, bg='#ff9800',
                                     fg='black', font=("Arial", 14))
        self.next_button.grid(row=0, column=1, padx=20)

    def show_knowledge_content(self):
        term = list(knowledge_base.keys())[self.knowledge_index]
        self.knowledge_text.config(state='normal')
        self.knowledge_text.delete(1.0, tk.END)
        self.knowledge_text.insert(tk.END, knowledge_base[term])
        self.knowledge_text.config(state='disabled')

    def show_prev_knowledge_slide(self):
        if self.knowledge_index > 0:
            self.knowledge_index -= 1
            self.knowledge_label.config(text=list(knowledge_base.keys())[self.knowledge_index])
            self.show_knowledge_content()
            if self.knowledge_index == 0:
                self.prev_button.config(state="disabled")
            if self.knowledge_index < len(knowledge_base) - 1:
                self.next_button.config(state="normal")

    def show_next_knowledge_slide(self):
        if self.knowledge_index < len(knowledge_base) - 1:
            self.knowledge_index += 1
            self.knowledge_label.config(text=list(knowledge_base.keys())[self.knowledge_index])
            self.show_knowledge_content()
            if self.knowledge_index == len(knowledge_base) - 1:
                self.next_button.config(state="disabled")
            if self.knowledge_index > 0:
                self.prev_button.config(state="normal")

    def show_learning_slides(self):
        self.slide_index = 0
        self.slide_window = tk.Toplevel(self)
        self.slide_window.title("Учебный материал")
        self.slide_window.geometry("800x600")

        self.slide_label = tk.Label(self.slide_window, text=learning_material[self.slide_index][0],
                                    font=("Arial", 20, "bold"), bg='#fff3e0', fg='black')
        self.slide_label.pack(pady=10)

        self.slide_text = scrolledtext.ScrolledText(self.slide_window, wrap="word", font=("Arial", 14), height=15,
                                                    bg='#fff', fg='black')
        self.slide_text.pack(fill="both", expand=True)
        self.show_slide_content()

        button_frame = tk.Frame(self.slide_window, bg='#fff3e0')
        button_frame.pack(pady=10)

        self.prev_button = tk.Button(button_frame, text="Назад", command=self.show_prev_slide, state="disabled",
                                     bg='#ff9800', fg='black', font=("Arial", 14))
        self.prev_button.grid(row=0, column=0, padx=20)

        self.next_button = tk.Button(button_frame, text="Вперед", command=self.show_next_slide, bg='#ff9800',
                                     fg='black', font=("Arial", 14))
        self.next_button.grid(row=0, column=1, padx=20)

    def show_slide_content(self):
        self.slide_text.config(state='normal')
        self.slide_text.delete(1.0, tk.END)
        self.slide_text.insert(tk.END, learning_material[self.slide_index][1])
        self.slide_text.config(state='disabled')

    def show_prev_slide(self):
        if self.slide_index > 0:
            self.slide_index -= 1
            self.slide_label.config(text=learning_material[self.slide_index][0])
            self.show_slide_content()
            if self.slide_index == 0:
                self.prev_button.config(state="disabled")
            if self.slide_index < len(learning_material) - 1:
                self.next_button.config(state="normal")

    def show_next_slide(self):
        if self.slide_index < len(learning_material) - 1:
            self.slide_index += 1
            self.slide_label.config(text=learning_material[self.slide_index][0])
            self.show_slide_content()
            if self.slide_index == len(learning_material) - 1:
                self.next_button.config(state="disabled")
            if self.slide_index > 0:
                self.prev_button.config(state="normal")

    def show_website_example(self):
        window = tk.Toplevel(self)
        window.title("Пример сайта")
        window.geometry("800x600")

        text = scrolledtext.ScrolledText(window, wrap="word", font=("Arial", 14), bg='#fff', fg='black')
        text.insert(tk.END, example_website)
        text.configure(state='disabled')
        text.pack(fill="both", expand=True)


    def start_quiz(self):
        self.quiz_window = tk.Toplevel(self)
        self.quiz_window.title("Тест")
        self.quiz_window.geometry("800x600")
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self.quiz_window, text="", font=("Arial", 18), bg='#fff3e0', fg='black')
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()
        self.options_frame = tk.Frame(self.quiz_window, bg='#fff3e0')
        self.options_frame.pack(pady=20)

        self.radio_buttons = []
        for i in range(3):
            radio = tk.Radiobutton(self.options_frame, text="", variable=self.option_var, value="", indicatoron=0,
                                   font=("Arial", 14), width=30, bg='#fff3e0', fg='black')
            radio.pack(anchor="w", pady=5)
            self.radio_buttons.append(radio)

        self.next_button = tk.Button(self.quiz_window, text="Следующий вопрос", command=self.next_question,
                                     bg='#ff9800', fg='black', font=("Arial", 14))
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        question_data = quiz_data[self.current_question]
        self.question_label.config(text=question_data["question"])
        self.option_var.set(None)

        for i, option in enumerate(question_data["options"]):
            self.radio_buttons[i].config(text=option, value=option)

    def next_question(self):
        question_data = quiz_data[self.current_question]
        if self.option_var.get() == question_data["answer"]:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(quiz_data):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Результат", f"Ваш результат: {self.score}/{len(quiz_data)}")
        self.quiz_window.destroy()


if __name__ == "__main__":
    app = WebDevApp()
    app.mainloop()