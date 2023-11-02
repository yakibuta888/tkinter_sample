import tkinter
from tkinter import ttk
from tkinter import filedialog

from googletrans import Translator


root = tkinter.Tk()
root.title('translator')
icon = tkinter.PhotoImage(file='src/sample/translate.png')
root.iconphoto(False, icon)
root.geometry('655x480')
root.resizable(False, False)


normal_font = ('Arial', 10)
bold_font = ('Arial', 10, 'bold')
bg_color = '#87CEFA'
button_color = '#4682B4'
root.config(bg=bg_color)

language_list = ['Japanese', 'English', 'Chinese', 'French', 'German', 'Hindi']

translator = Translator()


def convert():
    languages = {
        'Japanese': 'ja',
        'English': 'en',
        'Chinese': 'zh-ch',
        'French': 'fr',
        'German': 'de',
        'Hindi': 'hi'
    }

    before_text = input_box.get('1.0', 'end-1c')
    before_language = input_pulldown.get()
    after_language = output_pulldown.get()

    after_text = translator.translate(
        before_text,
        src=languages[before_language],
        dest=languages[after_language]
    )
    if output_box.get('1.0'):
        output_box.delete('1.0', 'end')
    output_box.insert('1.0', after_text.text)


def save():
    file_name = filedialog.asksaveasfilename(
        title='名前を付けて保存',
        filetypes=[('Text', '.txt'), ('PNG', '.png')],
        initialdir='./',
        defaultextension='.txt'
    )
    with open(file_name, 'w') as f:
        f.write(output_box.get('1.0', 'end-1c'))


input_pulldown = ttk.Combobox(root, values=language_list, font=normal_font, justify='center')
output_pulldown = ttk.Combobox(root, values=language_list, font=normal_font, justify='center')
to_label = tkinter.Label(root, text='to', font=normal_font, bg=bg_color)

input_pulldown.grid(row=0, column=0, padx=10, pady=10)
to_label.grid(row=0, column=1, padx=10, pady=10)
output_pulldown.grid(row=0, column=2, padx=10, pady=10)

input_pulldown.set('Japanese')
output_pulldown.set('English')

input_box = tkinter.Text(root, font=normal_font, width=35, height=20, borderwidth=3)
output_box = tkinter.Text(root, font=normal_font, width=35, height=20, borderwidth=3)
equal_sigh = tkinter.Label(root, text='=', font=normal_font, bg=bg_color)

input_box.grid(row=1, column=0, padx=10, pady=10)
equal_sigh.grid(row=1, column=1)
output_box.grid(row=1, column=2, padx=10, pady=10)

input_box.insert('1.0', '翻訳したい文章を入力')

convert_button = tkinter.Button(root, text='翻訳', font=bold_font, fg='white', bg=button_color, command=convert)
save_button = tkinter.Button(root, text='保存', font=bold_font, fg='white', bg=button_color, command=save)

convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)
save_button.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 10), ipadx=50)


root.mainloop()
