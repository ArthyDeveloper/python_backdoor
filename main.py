import requests, asyncio
from basicFunctions import *
import warnings, sys

async def main():
  warnings.filterwarnings("ignore", category=UserWarning)
  sys.coinit_flags = 0
  internet = False
  while not internet:
    internet = await check_internet_connection()
    if not internet:
      print("erro, esperando 10 secs")
      esperar(10)
    else: pass
  
  print("passou")

if __name__ == "__main__":
  asyncio.run(main())