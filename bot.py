import tkinter as tk
from tkinter import messagebox
from botcity.core import DesktopBot
import pyautogui
import time

# Disable errors if we are not connected to Maestro

def execute_bot(descricao_produto, descricao_produto_detalhada, unidade, especie, classe, subClasse, atividade):
    bot = DesktopBot()
    bot.browse("http://3305prd.cloudmv.com.br/mvautenticador-cas/login?service=http%3A%2F%2F3305prd.cloudmv.com.br%3A80%2Fsoul-mv%2Fcas")
    time.sleep(30)
    
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\user.png', confidence=0.8), duration=0.5)
    bot.type_keys("FUNEV")
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\pass.png', confidence=0.8), duration=0.5)
    bot.type_keys("Murl0c!@#24")
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\select.png', confidence=0.8), duration=0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\funev.png', confidence=0.8), duration=0.5)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\login.png', confidence=0.8), duration=0.5)
    time.sleep(8)
    
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\caminhao.png', confidence=0.8), duration=0.6)
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\almoxarifado.png', confidence=0.8), duration=0.52)
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\tabelas.png', confidence=0.8), duration=0.2)
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\produtos.png', confidence=0.8), duration=0.2)
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\cadastro.png', confidence=0.8), duration=0.2)
    time.sleep(20)

    cadastrar_produto(bot, descricao_produto, descricao_produto_detalhada, unidade, especie, classe, subClasse, atividade)

def cadastrar_produto(bot, descricao_produto, descricao_produto_detalhada, unidade, especie, classe, subClasse, atividade):
    if not bot.find_text("descricao", threshold=230, waiting_time=10000):
        not_found("descricao")
    bot.double_click_relative(54, 27)
    time.sleep(1)
    bot.type_keys(descricao_produto)
    time.sleep(1)

    if not bot.find_text("descricaoDetalhada", threshold=230, waiting_time=10000):
        not_found("descricaoDetalhada")
    bot.click_relative(53, 26)
    bot.enter()
    time.sleep(1)
    bot.type_keys(descricao_produto_detalhada)
    time.sleep(1)

    if not bot.find_text("unidade", threshold=230, waiting_time=10000):
        not_found("unidade")
    bot.click_relative(38, 29)
    time.sleep(1)
    bot.type_keys(unidade)
    time.sleep(1)

    if not bot.find_text("especie", threshold=230, waiting_time=10000):
        not_found("especie")
    bot.click_relative(32, 29)
    time.sleep(1)
    bot.type_keys(especie)
    time.sleep(1)

    if not bot.find_text("classe", threshold=230, waiting_time=10000):
        not_found("classe")
    bot.click_relative(26, 32)
    time.sleep(1)
    bot.type_keys(classe)
    time.sleep(1)

    if not bot.find_text("subClasse", threshold=230, waiting_time=10000):
        not_found("subClasse")
    bot.click_relative(42, 30)
    time.sleep(1)
    bot.type_keys(subClasse)
    time.sleep(1)

    if not bot.find_text("atividade", threshold=230, waiting_time=10000):
        not_found("atividade")
    bot.click_relative(37, 29)
    time.sleep(1)
    bot.type_keys(atividade)
    time.sleep(1)

    pyautogui.click(pyautogui.locateCenterOnScreen('img\\empresas.png', confidence=0.8), duration=0.2)
    bot.scroll_down(5)
    time.sleep(1)
    for i in range(1, 17):
        bot.type_keys(str(i))
        if i != 16:
            bot.type_down()
        time.sleep(1)

    pyautogui.click(pyautogui.locateCenterOnScreen('img\\save.png', confidence=0.8), duration=0.2)
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen('img\\not.png', confidence=0.8), duration=0.2)
    time.sleep(2)
    
    codigo_produto = bot.control_c()
    return codigo_produto

def not_found(label):
    print(f"Element not found: {label}")

def nova_funcao(descricao_produto, descricao_produto_detalhada, unidade, especie, classe, subClasse, atividade):
    bot = DesktopBot()
    cadastrar_produto(bot, descricao_produto, descricao_produto_detalhada, unidade, especie, classe, subClasse, atividade)

def perguntar_novo_cadastro():
    resposta = messagebox.askyesno("Novo Cadastro", "Deseja fazer outro cadastro?")
    if resposta:
        nova_funcao(entry_descricao_produto.get(), entry_descricao_produto_detalhada.get(), entry_unidade.get(), entry_especie.get(), entry_classe.get(), entry_subClasse.get(), entry_atividade.get())
        pyautogui.click(pyautogui.locateCenterOnScreen('img\\adicionar.png', confidence=0.8), duration=0.6)
        limpar_campos()
        root.deiconify()
    else:
        root.quit()

def limpar_campos():
    entry_descricao_produto.delete(0, tk.END)
    entry_descricao_produto_detalhada.delete(0, tk.END)
    entry_unidade.delete(0, tk.END)
    entry_especie.delete(0, tk.END)
    entry_classe.delete(0, tk.END)
    entry_subClasse.delete(0, tk.END)
    entry_atividade.delete(0, tk.END)

def on_submit():
    root.withdraw()  # Esconde a janela principal
    descricao_produto = entry_descricao_produto.get()
    descricao_produto_detalhada = entry_descricao_produto_detalhada.get()
    unidade = entry_unidade.get()
    especie = entry_especie.get()
    classe = entry_classe.get()
    subClasse = entry_subClasse.get()
    atividade = entry_atividade.get()

    try:
        codigo_produto = execute_bot(descricao_produto, descricao_produto_detalhada, unidade, especie, classe, subClasse, atividade)
        messagebox.showinfo("Success", f"Cadastro realizado com sucesso!\nCódigo do produto é: {codigo_produto}")
        perguntar_novo_cadastro()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        root.deiconify()  # Mostra a janela principal em caso de erro

# Configuração da interface gráfica
root = tk.Tk()
root.title("Cadastro de Produtos")

tk.Label(root, text="Descrição do Produto:").pack()
entry_descricao_produto = tk.Entry(root)
entry_descricao_produto.pack()

tk.Label(root, text="Descrição Detalhada:").pack()
entry_descricao_produto_detalhada = tk.Entry(root)
entry_descricao_produto_detalhada.pack()

tk.Label(root, text="Unidade:").pack()
entry_unidade = tk.Entry(root)
entry_unidade.pack()

tk.Label(root, text="Espécie:").pack()
entry_especie = tk.Entry(root)
entry_especie.pack()

tk.Label(root, text="Classe:").pack()
entry_classe = tk.Entry(root)
entry_classe.pack()

tk.Label(root, text="Subclasse:").pack()
entry_subClasse = tk.Entry(root)
entry_subClasse.pack()

tk.Label(root, text="Atividade:").pack()
entry_atividade = tk.Entry(root)
entry_atividade.pack()

tk.Button(root, text="Cadastrar", command=on_submit).pack()

root.mainloop()
