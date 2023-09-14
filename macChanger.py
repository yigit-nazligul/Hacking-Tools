import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest = "interface",help= "Interface to you want to change.")
parse_object.add_option("-m","--mac",dest = "mac_adress",help = "Please type your new MAC adress.")

print ("Mac Changer Started !")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_adress])
subprocess.call(["ifconfig",interface,"up"])




