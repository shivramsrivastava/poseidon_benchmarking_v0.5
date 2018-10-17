#! /usr/bin/python

import commands, os

f = open("ip_addresses")

all_data = f.read()

ips = all_data.split("\n")

# skip last empty entry
ips = ips[:(len(ips) - 1)]

print ips

for ip in ips:
   cmd_part1 = "ssh -i ~/.ssh/kubemarkkey.pem -t ubuntu@%s " % ip
   #paste your join command as cmd_part2
   cmd_part2 = "sudo kubeadm reset"
   cmd = cmd_part1 + cmd_part2
   os.system(cmd)
   print "Done resetting on %s" % ip
