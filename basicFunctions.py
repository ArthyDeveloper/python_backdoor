import keyboard # Ações do teclado;
import pyautogui # Mover mouse;
from pywinauto import Application # Alternar janelas;
from pynput.mouse import Button, Controller # Ações do mouse;
import time, subprocess # Tempo, delays e CMD;

mouse = Controller()

def esperar(tempo):
  try:
    time.sleep(tempo)
  except TypeError: pass

def click(numClicks=1, esquerdoOuDireito=True):
  try:
    for x in range(0, numClicks):
      match esquerdoOuDireito:
        case 1: # Click Esquerdo;
          mouse.press(Button.left)
          mouse.release(Button.left)
        case 2: # Click Direito;
          mouse.press(Button.right)
          mouse.release(Button.right)
  except TypeError: pass

def mover(x, y, duração=0.1):
  try:
    pyautogui.moveTo(x, y, duration=duração)
  except TypeError: pass

def escrever(texto):
  try:
    keyboard.write(texto)
  except TypeError: pass

def botaoTeclado(botão):
  try:
    keyboard.press_and_release(botão)
  except TypeError: pass

# TODO: Adaptar para funcionar com hotkeys de 3 teclas ou mais;
def hotkey(tecla1, tecla2):
  try:
    pyautogui.hotkey(tecla1, tecla2)
  except TypeError: pass

# TODO: Precisa funcionar com aplicativos com sub processos;
def alternarJanela(nomeJanela):
  try:
    app = Application().connect(title_re=nomeJanela)
    app.top_window().set_focus()
  except TypeError: pass

# TODO: Encontrar jeito de deixar stealth ou de limpar histórico do Windows + R;
def winR(action):
  try:
    hotkey("win", "r")
    escrever(action)
    botaoTeclado("enter")
  except TypeError: pass

def interceptar(mensagem, title="", assincrono=True):
  try:
    if assincrono:
      subprocess.Popen(f"PowerShell -Command Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{mensagem}', '{title}')")
    else:
      subprocess.run(f"PowerShell -Command Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{mensagem}', '{title}')")
  except TypeError: pass

def runCMD(comandosCMD, assincrono=True):
  # Uso: runCMD("comando1 && comando2...")
  try:
    if assincrono:
      subprocess.Popen(f"cmd /c {comandosCMD}")
    else:
      subprocess.run(f"cmd /c {comandosCMD}")
  except TypeError: pass