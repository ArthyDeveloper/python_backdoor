import asyncio
from basicFunctions import *
import warnings, sys

async def main():
  warnings.filterwarnings("ignore", category=UserWarning)
  sys.coinit_flags = 0
  
  # Verificando conexão estável antes de prosseguir.
  await check_internet_connection()

  # Resgatando valores do DB.
  mac_address = get_mac()
  await check_registration(mac_address)

if __name__ == "__main__":
  asyncio.run(main())