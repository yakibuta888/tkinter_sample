import tkinter
import tkinter.ttk as ttk
import csv
from typing import Any, Generator, Literal


DATABASE_FILE = 'src/sample/money_database.csv'

root = tkinter.Tk()
root.title('家計簿アプリ')
icon = tkinter.PhotoImage(file='src/sample/money_diary.png')
root.iconphoto(False, icon)
root.geometry('500x350')
root.resizable(False, False)


def insert_data(row_data: list[str]):
    tree.insert('', 'end', values=(row_data[0], row_data[1], row_data[2]))


def delete():
    selected_ids = tree.selection()
    for item_id in selected_ids:
        tree.delete(item_id)

    update_csv()


def read_csv(file_path: str) -> Generator[list[str], None, None]:
    with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        reader = csv.reader(f)

        yield from reader


def reflect_database():
    for data in read_csv(DATABASE_FILE):
        insert_data(data)


def update_csv():
    all_ids = tree.get_children()

    with open(DATABASE_FILE, 'w', encoding='utf-8-sig', errors='ignore') as f:
        writer = csv.writer(f, lineterminator='\n')
        for item_id in all_ids:
            content = list(tree.item(item_id, 'values'))
            writer.writerow(content)


def add():
    add_window()
    add_button.config(state='disabled')
    edit_button.config(state='disabled')
    delete_button.config(state='disabled')


def add_window():
    global date_entry, category_entry, money_entry, _add_window
    _add_window = tkinter.Toplevel()
    _add_window.geometry("250x200")
    _add_window.title('データ追加')

    date_label = tkinter.Label(_add_window, text='日付')
    date_entry = tkinter.Entry(_add_window, width=20)
    date_label.grid(row=0, column=0, padx=10, pady=20)
    date_entry.grid(row=0, column=1, padx=10, pady=20)

    category_label = tkinter.Label(_add_window, text='内訳')
    category_entry = tkinter.Entry(_add_window, width=20)
    category_label.grid(row=1, column=0, padx=10, pady=(0, 20))
    category_entry.grid(row=1, column=1, padx=10, pady=(0, 20))

    money_label = tkinter.Label(_add_window, text='金額')
    money_entry = tkinter.Entry(_add_window, width=20)
    money_label.grid(row=2, column=0, padx=10, pady=(0, 20))
    money_entry.grid(row=2, column=1, padx=10, pady=(0, 20))

    save_button = tkinter.Button(_add_window, text='保存', command=add_row)
    save_button.grid(row=3, column=0, columnspan=2)


def add_row():
    new_data = [date_entry.get(), category_entry.get(), money_entry.get()]
    insert_data(new_data)
    update_csv()
    _add_window.destroy()

    add_button.config(state='normal')
    edit_button.config(state='normal')
    delete_button.config(state='normal')


def edit():
    if tree.selection():
        global selected_id
        selected_id = tree.selection()[0]
        selected_data = tree.item(selected_id, 'values')
        edit_window(selected_data)

        add_button.config(state='disabled')
        edit_button.config(state='disabled')
        delete_button.config(state='disabled')


def edit_window(selected_data: tuple[Any, ...] | Literal['']):
    global date_entry, category_entry, money_entry, _edit_window
    _edit_window = tkinter.Toplevel()
    _edit_window.geometry("250x200")
    _edit_window.title('データ編集')

    date_label = tkinter.Label(_edit_window, text='日付')
    date_entry = tkinter.Entry(_edit_window, width=20)
    date_label.grid(row=0, column=0, padx=10, pady=20)
    date_entry.grid(row=0, column=1, padx=10, pady=20)

    date_entry.insert(0, selected_data[0])

    category_label = tkinter.Label(_edit_window, text='内訳')
    category_entry = tkinter.Entry(_edit_window, width=20)
    category_label.grid(row=1, column=0, padx=10, pady=(0, 20))
    category_entry.grid(row=1, column=1, padx=10, pady=(0, 20))

    category_entry.insert(0, selected_data[1])

    money_label = tkinter.Label(_edit_window, text='金額')
    money_entry = tkinter.Entry(_edit_window, width=20)
    money_label.grid(row=2, column=0, padx=10, pady=(0, 20))
    money_entry.grid(row=2, column=1, padx=10, pady=(0, 20))

    money_entry.insert(0, selected_data[2])

    save_button = tkinter.Button(_edit_window, text='保存', command=edit_row)
    save_button.grid(row=3, column=0, columnspan=2)


def edit_row():
    tree.delete(selected_id)

    new_data = [date_entry.get(), category_entry.get(), money_entry.get()]
    insert_data(new_data)
    update_csv()
    _edit_window.destroy()

    add_button.config(state='normal')
    edit_button.config(state='normal')
    delete_button.config(state='normal')


output_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
output_frame.pack()
button_frame.pack()

tree = ttk.Treeview(output_frame)
tree['columns'] = (1, 2, 3)
tree['show'] = 'headings'

tree.column(1, width=130)
tree.column(2, width=130)
tree.column(3, width=130)

tree.heading(1, text='日付')
tree.heading(2, text='内訳')
tree.heading(3, text='金額')

reflect_database()

tree.pack(pady=20)

add_button = tkinter.Button(button_frame, text='追加', borderwidth=2, command=add)
edit_button = tkinter.Button(button_frame, text='編集', borderwidth=2, command=edit)
delete_button = tkinter.Button(button_frame, text='削除', borderwidth=2, command=delete)
add_button.grid(row=0, column=0, padx=5, pady=15, ipadx=5)
edit_button.grid(row=0, column=1, padx=5, pady=15, ipadx=5)
delete_button.grid(row=0, column=2, padx=5, pady=15, ipadx=5)


root.mainloop()
