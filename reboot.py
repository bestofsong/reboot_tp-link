#!/usr/bin/python
'''
Reboot tp-link wifi router
Created on: Nov 8, 2015 by Tyler Chen
'''

import requests
import base64
import urllib
import sys

# Configuration parameters, change these to match with your tp-link wifi router.
ip = '192.168.0.100'
username = 'admin'
password = 'admin'

# Reboot old tp-link, tested with TL-WR941ND
#requests.get('http://%s/userRpm/SysRebootRpm.htm?Reboot=Reboot' %ip, auth=(username, password))

# Reboot new tp-link, tested with ArcherC9
def reboot_tplink(ip, username, password):
  full_string = username + ":" + password
  url = 'http://%s/userRpm/SysRebootRpm.htm?Reboot=Reboot' %ip
  auth_info = "Basic " + base64.b64encode(full_string)
  cookie = urllib.quote(auth_info)
  cookie = dict(Authorization=cookie)
  headers = {
  	"Host": ip,
  	"Referer": "http://%s/userRpm/SysRebootRpm.htm" %ip,
    "Authorization":auth_info
  }
  resp = requests.get(url, cookies=cookie, headers=headers )
  print ""+str(resp)

# Execute reboot
try:
	print "[+] Trying to reboot TP-Link router address: %s" %ip
	reboot_tplink(ip, username, password)
except Exception, e:
	print "[!] Error = " +str(e)
	print "[!] Cannot reboot your TP-Link router!"
	sys.exit()
print "-"*60
print "[+] Your TP-Link router: %s has just been rebooted!" %ip
print "[+] Exiting, have a nice day!"
print ""
