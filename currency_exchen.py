# import requests
# from tkinter import *
# from tkinter import ttk, messagebox as mb
#
# currencies = {
#     "USD": "Американский доллар",
#     "EUR": "Евро",
#     "JPY": "Японская йена",
#     "GBP": "Британский фунт стерлингов",
#     "AUD": "Австралийский доллар",
#     "CAD": "Канадский доллар",
#     "CHF": "Швейцарский франк",
#     "RUB": "Российский рубль",
#     "CNY": "Китайский юань",
#     "KZT": "Казахстанский тенге",
#     "UZS": "Узбекский сум"
# }
#
# def update_currency_label(event):
#     code = target_combobox.get().strip().upper()
#     name = currencies.get(code, "Выберите валюту")
#     currency_label.config(text=name)
#
# def exchange():
#     target_code = target_combobox.get().strip().upper()
#     base_code = base_combobox.get().strip().upper()
#
#     if not target_code or not base_code:
#         mb.showwarning("Внимание", "Выберите обе валюты")
#         return
#
#     try:
#         response = requests.get(f"https://open.er-api.com/v6/latest/{base_code}")
#         response.raise_for_status()
#         data = response.json()
#
#         if target_code in data.get('rates', {}):
#             exchange_rate = data['rates'][target_code]
#             base_name = currencies.get(base_code, base_code)
#             target_name = currencies.get(target_code, target_code)
#
#             mb.showinfo(
#                 "Курс обмена",
#                 f"Курс {exchange_rate:.1f} {target_name} за 1 {base_name}"
#             )
#         else:
#             mb.showerror("Ошибка", f"Валюта {target_code} не найдена в курсе {base_code}")
#     except Exception as e:
#         mb.showerror("Ошибка", f"Произошла ошибка при запросе: {e}")
#
# root = Tk()
# root.title("Курс валют")
# root.geometry("300x260")  # ширина высота
#
# Label(text="Базовая валюта").pack(pady=10, padx=10)
# base_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
# base_combobox.pack()
#
# Label(text="Целевая валюта").pack(pady=10, padx=10)
# target_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
# target_combobox.pack()
#
# currency_label = ttk.Label()
# currency_label.pack(pady=10, padx=10)
#
# button = Button(text="Получить курс", command=exchange)
# button.pack()
#
# target_combobox.bind("<<ComboboxSelected>>", update_currency_label)
#
# root.mainloop()


import requests
from tkinter import *
from tkinter import ttk, messagebox as mb

currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

def update_currency_label(event, label_widget, combobox_widget):
    """Обновляет название валюты рядом с выбранным комбобоксом"""
    code = combobox_widget.get().strip().upper()
    name = currencies.get(code, "Выберите валюту")
    label_widget.config(text=name)

def exchange():
    target_code = target_combobox.get().strip().upper()
    base1_code = base1_combobox.get().strip().upper()
    base2_code = base2_combobox.get().strip().upper()

    # Проверка: хотя бы одна базовая и целевая должны быть выбраны
    if not target_code:
        mb.showwarning("Внимание", "Выберите целевую валюту")
        return
    if not base1_code and not base2_code:
        mb.showwarning("Внимание", "Выберите хотя бы одну базовую валюту")
        return

    results_lines = []

    for base_code, label_name in [(base1_code, "Базовая 1"), (base2_code, "Базовая 2")]:
        if not base_code:
            results_lines.append(f"{label_name}: не выбрана")
            continue

        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{base_code}", timeout=10)
            response.raise_for_status()
            data = response.json()

            rates = data.get('rates', {})
            if target_code in rates:
                rate = rates[target_code]
                base_name = currencies.get(base_code, base_code)
                target_name = currencies.get(target_code, target_code)
                results_lines.append(
                    f"{label_name} ({base_name}): {rate:.2f} {target_name} за 1 {base_name}"
                )
            else:
                results_lines.append(f"{label_name}: курс к {target_code} не найден")
        except Exception as e:
            results_lines.append(f"{label_name}: ошибка — {e}")

    # Выводим все результаты в один лейбл (вместо кучи popup)
    result_text = "\n".join(results_lines)
    result_label.config(text=result_text, justify=LEFT)

root = Tk()
root.title("Курс валют: две базовые")
root.geometry("400x500")

# --- Базовая 1 ---
Label(text="Базовая валюта 1").pack(pady=5, padx=10, anchor=W)
base1_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
base1_combobox.pack(pady=2, padx=10, fill=X)
base1_name_label = ttk.Label()
base1_name_label.pack(pady=2, padx=10, anchor=W)
base1_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, base1_name_label, base1_combobox))

# --- Базовая 2 ---
Label(text="Базовая валюта 2").pack(pady=5, padx=10, anchor=W)
base2_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
base2_combobox.pack(pady=2, padx=10, fill=X)
base2_name_label = ttk.Label()
base2_name_label.pack(pady=2, padx=10, anchor=W)
base2_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, base2_name_label, base2_combobox))

# --- Целевая валюта ---
Label(text="Целевая валюта").pack(pady=5, padx=10, anchor=W)
target_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
target_combobox.pack(pady=2, padx=10, fill=X)
target_name_label = ttk.Label()
target_name_label.pack(pady=2, padx=10, anchor=W)
target_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, target_name_label, target_combobox))

# Кнопка
button = Button(text="Получить курсы", command=exchange)
button.pack(pady=15)

# Лейбл для вывода результатов
result_label = ttk.Label(wraplength=360, justify=LEFT, font=("Arial", 10))
result_label.pack(padx=10, pady=5, anchor=W, fill=BOTH, expand=True)

root.mainloop()
