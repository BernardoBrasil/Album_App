from tkinter import *
from PIL import ImageTk, Image

#Instanciando
root= Tk()
root.title('Out of the Box')

#criando um icone para ir no topo do programa
root.iconbitmap('/Users/silasbernardo/Documents/Projetos em Execução/OTB/Imagens/Icones/Icone-Preto.ico')

#Adicionar imagens sao tres passos, criar imagem, selecionar objeto que vai a imagem, printar o objeto
my_img = ImageTk.PhotoImage(Image.open('/Users/silasbernardo/Documents/Projetos em Execução/OTB/Imagens/Screenshot_20221226-230234~2.png'))
my_Label = Label(image= my_img)
my_Label.pack()



#Saindo do programa
button_quit= Button(root,text='Sair do Programa', command= root.quit)
button_quit.pack()

root.mainloop()