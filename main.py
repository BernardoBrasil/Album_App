from tkinter import *
from PIL import ImageTk, Image

#Instanciando
root= Tk()
root.title('Out of the Box')

pasta = "/Users/silasbernardo/Documents/programasGit/album_App/Images/"
#criando um icone para ir no topo do programa
root.iconbitmap(pasta + 'Icone-Preto.ico')

#Funções
def back():
    number -= number

def next():
    number += number


#Adicionar imagens sao tres passos, criar imagem, selecionar objeto que vai a imagem, printar o objeto
my_img1 = ImageTk.PhotoImage(Image.open(pasta +'img1.png'))
my_img2 = ImageTk.PhotoImage(Image.open(pasta +'img2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open(pasta +'img3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open(pasta +'img4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open(pasta +'img5.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open(pasta +'img6.jpg'))

 global number= 1

my_img = [my_img6,my_img5,my_img4,my_img3,my_img2,my_img1]

my_Label = Label(image= my_img[number])
my_Label.pack()

button_Next = Button(root, text='>>',command=next)
button_Back = Button(root, text= '<<', command= back)
button_quit= Button(root,text='Sair do Programa', command= root.quit)
'''
button_Next.grid(row = 0, column= 0)
button_Back.grid(row = 0, column= 1, columnspan=2)
button_quit.grid(row = 0, column= 2,)
'''

button_quit.pack()
button_Back.pack()
button_Next.pack()



root.mainloop()