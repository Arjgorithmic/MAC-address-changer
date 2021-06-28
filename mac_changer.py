#!/usr/bin/env python

import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface who's mac address needed to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="Custom MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("\n[-] Please specify an interface ,\n use --help for more info")
    elif not options.new_mac:
        parser.error("\n[-] Please specify an MAC Address ,\n use --help for more info")
    return options


def change_mac(interface, new_mac):
    print(" [+] Changing MAC address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# interface = input("Select Interface >>> ")
# new_mac = input("NEW MAC Address >>> ")

options = get_args()
# change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
mac_regex_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if mac_regex_result:
    print(mac_regex_result.group(0))
else:
    print("Cannot find MAC ADDRESS")
