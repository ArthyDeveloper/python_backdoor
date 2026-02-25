import keyboard # Ações do teclado;
import pyautogui # Ações do mouse;
import pymongo # MongoDB;
import wmi # Task Manager;
from pywinauto import Application # Alternar janelas;
import time, subprocess # Tempo, delays e CMD;

#from pynput.mouse import Button, Controller # Ações do mouse;
#mouse = Controller()

# Congela script por um dado tempo.
def esperar(tempo:int):
  try:
    time.sleep(tempo)
  except TypeError: pass

# Clica quantas vezes quiser e é configurável para clicar com o botão direito.
# Exemplo: Esquerdo: click(1) | Direito: click(1, False)
def click(numClicks=1, leftClick=True):
  try:
    if leftClick: # Click Esquerdo;
      pyautogui.click(clicks=numClicks, button="primary")
    else: # Click Direito;
      pyautogui.click(clicks=numClicks, button="secondary")
  except TypeError: pass

# Move o mouse para uma coordenada x e y com uma velocidade padrão de 0.1.
# Valores podem ser ajustados como exemplo: mover(123, 123, 1)
# Segundo parâmetro (Y) não é obrigatório, pois o Primeiro parâmetro por ser uma tuple com x e y.
# Exemplo: mover((123, 123), speed=1).
def mover(x, y=False, speed=0.1):
  try:
    if not y and type(x) == tuple:
      c_x, c_y = x
      pyautogui.moveTo(c_x, c_y, duration=speed)
    else:
      pyautogui.moveTo(x, y, duration=speed)
  except TypeError: pass

# Escreve algo com o teclado.
def escrever(texto:str):
  try:
    keyboard.write(texto)
  except TypeError: pass

# Aperta e solta um tecla específico do tecaldo com dicionário do módulo keyboard.
# Possui opção de repetição de pressionamentos e tempo entre teclagens.
def botaoTeclado(tecla:str, repetitions=1):
  try:
    for _ in range(repetitions):
      keyboard.press_and_release(tecla)
  except TypeError: pass

# Usa hotkey de 2 ou 3 teclas usando dicionário de teclas do pyautogui.
# Exemplo: hotkey("win", "shift", "s") | hotkey("ctrl", "v").
def hotkey(tecla1:str, tecla2:str, tecla3:str=""):
  try:
    pyautogui.hotkey(tecla1, tecla2, tecla3)
  except TypeError: pass

# Como se desse um Alt+Tab para uma janela específica através do PID do processo.
def alternarJanela(PID:int):
  try:
    app = Application().connect(process=PID)
    app.top_window().set_focus()
  except TypeError: pass

# Usa a janela Win+R com pyautogui para execução de comandos.
# Muito primitivo. Use runCMD(comando).
def winR(action):
  try:
    hotkey("win", "r")
    escrever(action)
    botaoTeclado("enter")
  except TypeError: pass

# -----------------------------------
# Comandos baseados em CMD / Terminal
# -----------------------------------

# Escreve uma mensagem na tela com Powershell.
# Somente a mensagem (str) é obrigatório, mas é possível adicionar título à janela.
def interceptar(mensagem, title="", assincrono=True):
  try:
    if assincrono:
      subprocess.Popen(f"PowerShell -Command Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{mensagem}', '{title}')")
    else:
      subprocess.run(f"PowerShell -Command Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('{mensagem}', '{title}')")
  except TypeError: pass

# Executa qualquer comando no CMD sem abri-lo.
# Retorna stdout como mensagem debug de ação ou stderr para erros.
# Uso para múltiplos comandos: runCMD("comando1 && comando2...").
def runCMD(comandosCMD, assincrono=True):
  try:
    if assincrono:
      return subprocess.Popen(f"cmd /c {comandosCMD}", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
      return subprocess.run(f"cmd /c {comandosCMD}", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  except TypeError: pass

# Lista todos os processos da máquina, mas só exibe Nome do .EXE, Nome do Programa, PID e Caminho do Programa.
# TODO: Enviar informações formatadas para Webhook do DB como TXT.
def get_processes_list():
  try:
    f = wmi.WMI()
    processes = f.Win32_Process()
    for process in processes:
      #print(process)
      print(
        process.Caption,
        process.Name,
        process.ProcessId,
        process.ExecutablePath
      )
  except Exception: pass

# Usa da função runCMD para encerrar um processo forçadamente usando PID do processo.
# Para obter o PID, use getProcessesList()
def taskkill(PID:int):
  result = runCMD(f"taskkill /f /pid {PID}")
  stdout, stderr = result.communicate()
  if stdout:
    print(f"{stdout.decode("utf-8")}")
  if stderr:
    print(f"{stderr.decode("utf-8")}")