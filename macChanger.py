import subprocess
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest = "interface",help= "Interface to you want to change.")
    parse_object.add_option("-m","--mac",dest = "mac_address",help = "Please type your new MAC adress.")
    return parse_object.parse_args


def change_mac_address(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_adress])
    subprocess.call(["ifconfig",interface,"up"])

print ("MAC Address Changer Started!")
get_user_input() = (user_input,arguments)
change_mac_address = (user_input.interface,user_input.mac_address)

def check_new_mac():
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)
