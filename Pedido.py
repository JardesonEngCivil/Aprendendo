import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

janela = tk.Tk()
janela.title('Pedido')
janela.geometry('600x600')
janela.configure(background= '#ffc8dd')


def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) <40:
        x = random.randint(0, janela.winfo_width() - button_1.winfo_width())
        y = random.randint(0, janela.winfo_height() - button_1.winfo_height())
        button_1.place(x =x , y = y)


def accepted():
    messagebox.showinfo('Deu certo', '19:30 hrs passo pra te buscar!!!')

def denied():
    button_1.destroy()


margin = Canvas(janela, width=00, bg= '#ffc8dd', height=100,
                bd = 0, highlightthickness=0, relief = 'ridge')
margin.pack()

text_id = Label(janela, bg= '#ffc8dd', text = ' quer sair para comer 20:00 hrs?',
                fg = '#590d22', font = ("Montserrat", 24, 'bold'))
text_id.pack()

button_1 = tk.Button(janela, bg= '#ffb3c1', text = 'Não',command = denied,
                     relief = RIDGE, bd=3, font = ("Montserrat", 8, 'bold'))
button_1.pack()
janela.bind('<Motion>', move_button_1)

button_2 = tk.Button(janela, bg= '#ffb3c1', text = 'Sim',command = accepted,
                     relief = RIDGE, bd=3, font = ("Montserrat", 14, 'bold'))
button_2.pack()




janela.mainloop()