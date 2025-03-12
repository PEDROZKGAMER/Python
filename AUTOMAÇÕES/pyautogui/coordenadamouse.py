import pyautogui
import time

# Parte 1: Obtém a posição do mouse
print("Mova o mouse para o ícone desejado dentro de 5 segundos...")
time.sleep(5)
posicao_mouse = pyautogui.position()
print(f"A posição atual do mouse é: {posicao_mouse}")