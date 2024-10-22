import tkinter
import os
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename (initialdir="/", title="Bыберите þайл",
                                           filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))

    text['text'] = text['text'] + "" + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('400x350')
window.configure(bg='#FFDAB9')
window.resizable(False, False)
text = tkinter.Label(window, text='Фaйл:', height=5, width=20, background='#FFC0CB')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать Файл',
                               background='#F08080', command = file_select)
button_select.grid(column=3, row=1)
window.mainloop()
