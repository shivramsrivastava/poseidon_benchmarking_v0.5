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
   cmd_part2 = "sudo kubeadm join 11.12.14.30:6443 --token fpm7kp.6vh12qpccupspjde --discovery-token-ca-cert-hash sha256:5deb1412a4652acfc342434a3987ff12a26e0cf888d0434e5316ee5b3d2adb7e"
   cmd = cmd_part1 + cmd_part2
   os.system(cmd)
   print "Joined %s to master...." % ip
