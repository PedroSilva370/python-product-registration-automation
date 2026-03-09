import pyautogui
import time

pyautogui.PAUSE = 0.3

# open the browser (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# enter the link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Step 2: Login
# select the email field
pyautogui.click(x=685, y=451)
# write your email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # moving on to the next field
pyautogui.write("LOGIN_PASSWORD")
pyautogui.click(x=955, y=638) # Click the login button.
time.sleep(3)

# Step 3: Import the product database for registration.
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Step 4: Register a product
for linha in tabela.index:
    # click on the code field
    pyautogui.click(x=653, y=294)
    # retrieve the value from the table for the field we want to fill.
    codigo = tabela.loc[linha, "codigo"]
    # fill in the field
    pyautogui.write(str(codigo))
    # move to the next field
    pyautogui.press("tab")
    # fill in the field
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter") # Register the product (submit button)
    # scroll everything up
    pyautogui.scroll(10000)
    # Step 5: Repeat the registration process until the end.