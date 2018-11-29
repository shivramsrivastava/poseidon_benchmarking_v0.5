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
   cmd_part2 = "sudo kubeadm join 11.12.14.30:6443 --token sxe17x.0jdecw6964019zuk --discovery-token-ca-cert-hash sha256:d44fc09fcee64c88cf558a15dedd07f01a5f6ea3d335d50ccd5eba7c861b7a95"
   cmd = cmd_part1 + cmd_part2
   os.system(cmd)
   print "Joined %s to master...." % ip
