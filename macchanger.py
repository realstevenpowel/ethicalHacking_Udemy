#!/usr/bin/env python

import subprocess
import optparse

#trying out a function
def change_MAC(interface, new_mac)
    print("changing mac address for " + options.interface + " to this mac " + options.new_mac)
    subprocess.call(["ifconfig " + interface + " down",])
    subprocess.call(["ifconfig " + interface + " hw ether " + new_mac])
    subprocess.call(["ifconfig " + new_mac + " up"])

parser  = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change the mac")
parser.add_option("-m", "--macaddress", dest="new_mac", help="new mac ad")

(options, arguments) = parser.parse_args()

#interface = "wlan0"
#new_mac = "88:66:77:55:33:00"
#interface = input("enter the interface to alter. Ex: wlan0")
#new_mac = input("enter the chosen mac address")

#oldcode
#interface = options.interface
#new_mac = options.new_mac

change_MAC(options.interface, options.new_mac)

#old code
#print("changing mac address for " + options.interface + " to this mac " + options.new_mac)
#
#
#
#subprocess.call(["ifconfig " + interface + " down",])
#subprocess.call(["ifconfig " + interface + " hw ether " + new_mac])
#subprocess.call(["ifconfig " + new_mac + " up"])
