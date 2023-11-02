import tkinter
from tkinter import messagebox

# ウィンドウの作成
root = tkinter.Tk()
root.title('Entry limit Practice!')
root.geometry('320x200')
root.resizable(False, False)


# 関数の定義
def show_message():
    messagebox.showinfo('お知らせ', 'お知らせです')


def limit_character(string: str):
    boolean_limit = len(string) <= 5
    return boolean_limit


def least_character(string: str):
    if len(string) >= 5:
        button_1['state'] = 'normal'
    return True


# 文字数制限の検証関数
vc_1 = root.register(limit_character)
vc_2 = root.register(least_character)


# エントリーの作成
entry_1 = tkinter.Entry(root, width=30, validate='key', validatecommand=(vc_1, '%P'))
entry_2 = tkinter.Entry(root, width=30, validate='key', validatecommand=(vc_2, '%P'))

entry_1.grid(row=0, column=0, padx=35, pady=25)
entry_2.grid(row=1, column=0, padx=35, pady=(0, 25))

# ボタンの作成
button_1 = tkinter.Button(root, text='テスト', state='disabled', command=show_message)
button_1.grid(row=2, column=0, padx=35, ipadx=10)

# ループ処理
root.mainloop()
