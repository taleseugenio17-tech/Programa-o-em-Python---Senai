import tkinter as tk
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk

def soma():
   try:
        n1  =  float(numero_1.get())
        n2  =  float(numero_1.get())
        resultado  = n1  +  n2
        r.config (text = resultado)
        messagebox.showinfo('','Obrigada por usar a aplicação')
   except:
        messagebox.showerror('', 'digite um número para fazer o calculo')


def sub():
    n1  =  float(numero_1.get())
    n2  =  float(numero_1.get())
    resultado  = n1  -  n2
    r.config (text = resultado)


def mult():
    n1  =  float(numero_1.get())
    n2  =  float(numero_1.get())
    resultado  = n1  * n2
    r.config (text = resultado)


def div():
    n1  =  float(numero_1.get())
    n2  =  float(numero_1.get())
    resultado  = n1  / n2
    r.config (text = resultado)


janela =  tk.Tk()

janela.iconbitmap('x.ico')

janela.geometry('700x600')


secao = tk.Frame(janela)
secao.grid(pady=20, row=1, column= 0)


t  = tk.Label(secao, text = 'Faça o calculo', font=('Gill Sans MT', 15))
t.grid(padx=10, pady=10, row = 1 , column= 0)




secao2_inputs = tk.Frame(janela)
secao2_inputs.grid(row=2,  column= 0)

numero_1 = tk.Entry(secao, width = 20, font=('Gill Sans MT', 15))
numero_1.grid(column = 0, row = 3)

numero_1 = tk.Entry(secao, width = 20, font=('Gill Sans MT', 15))
numero_1.grid(column = 1, row  = 3)




# seção para os botões

secao3_botoes = tk.Frame(janela)
secao3_botoes.grid(pady=10, row=3, column= 0)


button_mais = tk.Button(secao3_botoes, text="+", command=soma)
button_mais.grid(padx=20, pady=20, row=3, column= 0)


button_menos = tk.Button(secao3_botoes, text="-", command=sub)
button_menos.grid(padx=20, pady=20, row=3, column= 1)

button_mult = tk.Button(secao3_botoes, text="x", command= mult)
button_mult.grid(padx=20, pady=20, row=3, column= 2)


button_div = tk.Button(secao3_botoes, text=":", command=div )
button_div.grid(padx=20, pady=20, row=3, column= 3)







# resultado


secao4_r = tk.Frame(janela)
secao4_r.grid(pady=10, row=5, column= 0)



r  = tk.Label(secao4_r, text = '=', font=('arial', 15))
r.grid(padx=20, pady=10, row = 5 , column= 0)



# Substitua 'seu_arquivo.jpg' pelo nome e caminho corretos do seu
img_pil = Image.open('teste.png')
img_pil = img_pil.resize((200, 200), Image.LANCZOS)
img_tk = ImageTk.PhotoImage(img_pil)

label_imagem = tk.Label(janela, image=img_tk)
label_imagem.image = img_tk
label_imagem.grid(pady=10, padx=10)

janela.mainloop()