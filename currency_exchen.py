# import requests
# from tkinter import *
# from tkinter import ttk, messagebox as mb
#
# currencies = {
#     "CNY": "Китайский юань",
#     "USD": "Американский доллар",
#     "EUR": "Евро",
#     "RUB": "Российский рубль",
#     "JPY": "Японская йена",
#     "GBP": "Британский фунт стерлингов",
#     "AUD": "Австралийский доллар",
#     "CAD": "Канадский доллар",
#     "CHF": "Швейцарский франк",
#     "KZT": "Казахстанский тенге",
#     "UZS": "Узбекский сум"
# }
#
# def update_currency_label(event, label_widget, combobox_widget):
#     code = combobox_widget.get().strip().upper()
#     name = currencies.get(code, "Выберите валюту")
#     label_widget.config(text=name)
#
# def exchange():
#     target_code = target_combobox.get().strip().upper()
#     base1_code = base1_combobox.get().strip().upper()
#     base2_code = base2_combobox.get().strip().upper()
#
#     if not target_code:
#         mb.showwarning("Внимание", "Выберите целевую валюту")
#         return
#     if not base1_code and not base2_code:
#         mb.showwarning("Внимание", "Выберите хотя бы одну базовую валюту")
#         return
#
#     results_lines = []
#
#     for base_code, label_name in [(base1_code, "Базовая 1"), (base2_code, "Базовая 2")]:
#         if not base_code:
#             results_lines.append(f"{label_name}: не выбрана")
#             continue
#
#         try:
#             response = requests.get(f"https://open.er-api.com/v6/latest/{base_code}", timeout=10)
#             response.raise_for_status()
#             data = response.json()
#
#             rates = data.get('rates', {})
#             if target_code in rates:
#                 rate = rates[target_code]
#                 base_name = currencies.get(base_code, base_code)
#                 target_name = currencies.get(target_code, target_code)
#                 results_lines.append(f"{label_name} ({base_name}): {rate:.2f} {target_name} за 1 {base_name}")
#             else:
#                 results_lines.append(f"{label_name}: курс к {target_code} не найден")
#         except Exception as e:
#             results_lines.append(f"{label_name}: ошибка — {e}")
#
#
#     result_text = "\n".join(results_lines)
#     result_label.config(text=result_text, justify=LEFT)
#
# root = Tk()
# root.title("Курс валют")
# root.geometry("400x500")
#
# Label(text="Базовая валюта 1").pack(pady=5, padx=10, anchor=W)
# base1_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
# base1_combobox.pack(pady=2, padx=10, fill=X)
# base1_name_label = ttk.Label()
# base1_name_label.pack(pady=2, padx=10, anchor=W)
# base1_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, base1_name_label, base1_combobox))
#
# Label(text="Базовая валюта 2").pack(pady=5, padx=10, anchor=W)
# base2_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
# base2_combobox.pack(pady=2, padx=10, fill=X)
# base2_name_label = ttk.Label()
# base2_name_label.pack(pady=2, padx=10, anchor=W)
# base2_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, base2_name_label, base2_combobox))
#
# Label(text="Целевая валюта").pack(pady=5, padx=10, anchor=W)
# target_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
# target_combobox.pack(pady=2, padx=10, fill=X)
# target_name_label = ttk.Label()
# target_name_label.pack(pady=2, padx=10, anchor=W)
# target_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, target_name_label, target_combobox))
#
# button = Button(text="Получить курсы", command=exchange)
# button.pack(pady=15)
#
# result_label = ttk.Label(wraplength=360, justify=LEFT, font=("Arial", 10))
# result_label.pack(padx=10, pady=5, anchor=W, fill=BOTH, expand=True)
#
# root.mainloop()



import requests
from tkinter import *
from tkinter import ttk, messagebox as mb

currencies = {
    "CNY": "Китайский юань",
    "USD": "Американский доллар",
    "EUR": "Евро",
    "RUB": "Российский рубль",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

def update_currency_label(event, label_widget, combobox_widget):
    code = combobox_widget.get().strip().upper()
    name = currencies.get(code, "Выберите валюту")
    label_widget.config(text=name)

def exchange():
    target_code = target_combobox.get().strip().upper()
    base1_code = base1_combobox.get().strip().upper()
    base2_code = base2_combobox.get().strip().upper()

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
                results_lines.append(f"{label_name} ({base_name}): {rate:.2f} {target_name} за 1 {base_name}")
            else:
                results_lines.append(f"{label_name}: курс к {target_code} не найден")
        except Exception as e:
            results_lines.append(f"{label_name}: ошибка — {e}")

    result_text = "\n".join(results_lines)
    result_label.config(text=result_text, justify=LEFT)

def clear_all():
    base1_combobox.set('')
    base2_combobox.set('')
    target_combobox.set('')

    base1_name_label.config(text="")
    base2_name_label.config(text="")
    target_name_label.config(text="")

    result_label.config(text="", justify=LEFT)

root = Tk()
root.title("Курс валют")
root.geometry("400x500")

Label(text="Базовая валюта 1").pack(pady=5, padx=10, anchor=W)
base1_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
base1_combobox.pack(pady=2, padx=10, fill=X)
base1_name_label = ttk.Label()
base1_name_label.pack(pady=2, padx=10, anchor=W)
base1_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, base1_name_label, base1_combobox))

Label(text="Базовая валюта 2").pack(pady=5, padx=10, anchor=W)
base2_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
base2_combobox.pack(pady=2, padx=10, fill=X)
base2_name_label = ttk.Label()
base2_name_label.pack(pady=2, padx=10, anchor=W)
base2_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, base2_name_label, base2_combobox))

Label(text="Целевая валюта").pack(pady=5, padx=10, anchor=W)
target_combobox = ttk.Combobox(values=list(currencies.keys()), state="readonly")
target_combobox.pack(pady=2, padx=10, fill=X)
target_name_label = ttk.Label()
target_name_label.pack(pady=2, padx=10, anchor=W)
target_combobox.bind("<<ComboboxSelected>>", lambda e: update_currency_label(e, target_name_label, target_combobox))

btn_frame = Frame(root)
btn_frame.pack(pady=15)

button_calc = Button(btn_frame, text="Получить курсы обмена", command=exchange, bg="#85bb65")
button_calc.pack(side=LEFT, padx=15)

button_clear = Button(btn_frame, text="Очистить", command=clear_all, bg="#ff0000")
button_clear.pack(side=LEFT, padx=15)

result_label = ttk.Label(wraplength=360, justify=LEFT, font=("Arial", 10))
result_label.pack(padx=10, pady=5, anchor=W, fill=BOTH, expand=True)

root.mainloop()