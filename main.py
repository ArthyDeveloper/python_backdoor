import requests, asyncio
from basicFunctions import *
import warnings, sys

async def main():
  warnings.filterwarnings("ignore", category=UserWarning)
  sys.coinit_flags = 0
  
  # Verificando conexão estável antes de prosseguir.
  await check_internet_connection()

  # Resgatando valores do DB.
  configs = await startup()
  mac_address = configs["mac_address"]
  await api_request("POST", {"route":"webhook", "data":{"mac_address":mac_address, "webhook_message":f"Máquina ligada `{mac_address}`", "webhook_image":""}})

if __name__ == "__main__":
  asyncio.run(main())