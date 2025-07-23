import hashlib
import wmi
import uuid
import socket
import platform
import subprocess

def get_cpu_id():
  try:
    c = wmi.WMI()
    for cpu in c.Win32_Processor():
      return cpu.ProcessorId.strip()
  except:
    return "unknown_cpu"

def get_bios_serial():
  try:
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
      return bios.SerialNumber.strip()
  except:
    return "unknown_bios"

def get_baseboard_serial():
  try:
    c = wmi.WMI()
    for board in c.Win32_BaseBoard():
      return board.SerialNumber.strip()
  except:
    return "unknown_board"

def get_disk_serial():
  try:
    output = subprocess.check_output("vol C:", shell=True)
    serial = output.decode(errors="ignore").split("Serial Number is")[-1].strip()
    return serial
  except:
    return "unknown_disk"

def get_mac_address():
  try:
    mac = uuid.getnode()
    if (mac >> 40) % 2:
      return "unknown_mac"  # Random MAC
    return ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))
  except:
    return "unknown_mac"

def generate_machine_id():
  elements = [
    get_cpu_id(),
    get_bios_serial(),
    get_baseboard_serial(),
    get_disk_serial(),
    get_mac_address(),
    socket.gethostname(),
    platform.system(),
    platform.version(),
  ]
  raw = '|'.join(elements)
  return hashlib.sha256(raw.encode()).hexdigest(), elements

if __name__ == "__main__":
  print("Machine ID:", generate_machine_id())