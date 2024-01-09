#pip install pyautogui
import pyautogui 
import time
import pandas

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
# scroll -> pyautogui.scroll

pyautogui.PAUSE = 1

# aperta a tecla do windows (command + barra de espaço)
pyautogui.press("win")
# digita o nome do programa (chrome)
pyautogui.write("chrome")
# aperta enter
pyautogui.press("enter")

# digitar o link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

#apertar enter
pyautogui.press("enter")

#espera 5 segundos
time.sleep(5)

# Passo 2 - Fazer login 
pyautogui.click(x=549, y=380)

# digitar o email 
pyautogui.write("pythonimpressionador@gmail.com")

# digitar a senha
pyautogui.press("tab")
pyautogui.write("minha senha")

pyautogui.press("tab")

# posicionar cursor
pyautogui.click(x=694, y=531)
time.sleep(3)

# guarda base de dados
tabela = pandas.read_csv("produtos.csv")

# cadastra produtos
for linha in tabela.index:
    pyautogui.click(x=570, y=255)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")

    # enviar o produto
    pyautogui.press("enter")

    # scroll 
    pyautogui.scroll(5000)
