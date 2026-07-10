import tkinter as tk


janela  = tk.Tk()

janela.geometry('300x300')

# texto formulario

tk.Label(janela, text= 'FOMULARIO').pack()


tk.Label(janela, text='nome').pack()
tk.Label(janela, text= 'email').pack()
tk.Label(janela, text='usuário').pack()

#seção de botoes
secao3_botoes= tk.Frame(janela)
secao3_botoes.grid(pady=10, row=3)
button_mais = tk.Button(secao3)
# input(nome)

nome  = tk.Entry(janela)
nome.pack()




janela.mainloop()