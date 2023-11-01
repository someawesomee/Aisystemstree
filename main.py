import tkinter as tk
from tkinter import *
from tkinter import messagebox
from decision import DecisionQuery
from decisionResult import DecisionResult

#Создаём окно
window = Tk()
window.title('Desicion Tree for Heart Attack')
window.geometry('800x700')

frame = Frame (
    window,
    padx = 10,
    pady = 10
)
frame.pack(expand = True)

age_tf = Label(
    frame,
    text = "Введите свой возраст\n 1 - >65, 0 - <65"

)
age_tf.grid(row = 1, column=1)

ecg_results_tf = Label(
    frame,
    text = "Результаты ЭКГ\n(0 - аномалий не найдено, 1 - проблемы с сердцем)"
)
ecg_results_tf.grid(row = 2, column=1)



heart_pain_tf = Label(
    frame,
    text = "Боль в груди\n(0 - нету, 1 -есть"
)
heart_pain_tf.grid(row = 3, column=1)

pressure_tf = Label(
    frame,
    text = "Проблемы с давлением\n(0 - нет, 1 - есть)"
)
pressure_tf.grid(row = 4, column=1)

#Добавляем поля для ввода данных

age_tf = Entry(
    frame,

)
age_tf.grid(row = 1, column=2)

ecg_results_tf = Entry(
    frame,
)
ecg_results_tf.grid(row = 2, column=2)

sex_tf = Entry(
    frame,

)
sex_tf.grid(row = 3, column=2)

heart_pain_tf = Entry(
    frame,
)
heart_pain_tf.grid(row = 4, column=2)

pressure_tf = Entry(
    frame,

)
pressure_tf.grid(row = 5, column=2)


def data():
    age = int(age_tf.get())
    ecg_results = int(ecg_results_tf.get())
    sex = int(sex_tf.get())
    heart_pain = int(heart_pain_tf.get())
    pressure = int(pressure_tf.get())

    #Создаем дерево решений
    decision_tree = DecisionQuery()

    # Добавляем узлы дерева
    decision_tree.Title = "License"
    decision_tree.Test = (lambda x: x.License)
    decision_tree.Positive = DecisionResult()
    decision_tree.Negative = DecisionResult()

    # Оцениваем дерево решений
    # decision_tree.Evaluate(user)

    # Получаем результат
    result = decision_tree.Positive.Result

    # Обрабатываем результат
    if result:
        print("Вы прошли")
    else:
        print("Вы не прошли")



class DecisionResult():
    pass


# # Вызываем функцию при нажатии кнопки
# button = Button(
#     frame,
#     text="Применить",
#     command=data
# )
# button.pack(expand=True)
cal_btn = Button(
   frame,
   text='Рассчитать',
   command=data
)
cal_btn.grid(row=6, column=2)




window.mainloop()
