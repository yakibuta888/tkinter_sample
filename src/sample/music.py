import tkinter
import tkinter.filedialog
from tkinter import END, ANCHOR
import pygame.mixer as pymix


root = tkinter.Tk()
root.title('音楽再生アプリ')
icon = tkinter.PhotoImage(file='src/sample/music-96.png')
root.iconphoto(False, icon)
root.geometry('500x550')
root.resizable(False, False)

basic_font = ('Times New Roman', 12)
list_font = ('Times New Roman', 15)


def add_item():
    file_type = [('', '*')]
    file_name = tkinter.filedialog.askopenfilename(filetypes=file_type, initialdir='./')
    my_listbox.insert(END, file_name)


def remove_item():
    my_listbox.delete(ANCHOR)


def clear_list():
    my_listbox.delete(0, END)


def play():
    global music_player
    pymix.quit()

    n = my_listbox.curselection()
    sound_file = my_listbox.get(n)

    pymix.init()
    sounds = pymix.Sound(sound_file)
    music_player = sounds.play()
    music_player.set_volume(0.1)


def stop():
    pymix.pause()


def restart():
    pymix.unpause()


def adjust_volume(volume: str):
    music_player.set_volume(float(volume))


input_frame = tkinter.Frame(root)
output_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
vol_frame = tkinter.Frame(root)
input_frame.pack()
output_frame.pack()
button_frame.pack()
vol_frame.pack()

list_add_button = tkinter.Button(input_frame, text='追加', borderwidth=2, font=basic_font, command=add_item)
list_remove_button = tkinter.Button(input_frame, text='選択削除', borderwidth=2, font=basic_font, command=remove_item)
clear_button = tkinter.Button(input_frame, text='一括削除', borderwidth=2, font=basic_font, command=clear_list)
list_add_button.grid(row=0, column=0, padx=2, pady=15, ipadx=5)
list_remove_button.grid(row=0, column=1, padx=2, pady=15, ipadx=5)
clear_button.grid(row=0, column=2, padx=2, pady=15, ipadx=5)

my_scrollbar = tkinter.Scrollbar(output_frame)

my_listbox = tkinter.Listbox(output_frame, width=30, height=15, yscrollcommand=my_scrollbar.set, borderwidth=3, font=list_font)
my_listbox.grid(row=0, column=0)

my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.grid(row=0, column=1, sticky='NS')

play_button = tkinter.Button(button_frame, text='再生', borderwidth=2, font=basic_font, command=play)
stop_button = tkinter.Button(button_frame, text='一時停止', borderwidth=2, font=basic_font, command=stop)
restart_button = tkinter.Button(button_frame, text='再開', borderwidth=2, font=basic_font, command=restart)
play_button.grid(row=0, column=0, padx=5, pady=15, ipadx=5)
stop_button.grid(row=0, column=1, padx=5, pady=15, ipadx=5)
restart_button.grid(row=0, column=2, padx=5, pady=15, ipadx=5)

vol_label = tkinter.Label(vol_frame, text='音量')
vol_scale = tkinter.Scale(vol_frame, orient='horizontal', length=300, from_=0.0, to=1.0, resolution=0.01, showvalue=False, command=adjust_volume)
vol_scale.set(0.1)
vol_label.grid(row=0, column=0, padx=10)
vol_scale.grid(row=0, column=1, padx=10)

root.mainloop()
