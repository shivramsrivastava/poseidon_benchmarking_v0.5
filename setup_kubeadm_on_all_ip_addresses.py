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
   cmd_part2 = "\"rm -rf delete_if_needed* && git clone https://github.com/shivramsrivastava/kubernetes-1.10.4-kubemark.git -b scripts_v_1_11 delete_if_needed4 && printf 'y\\ny\\ny\\n' | /home/ubuntu/delete_if_needed4/setup_docker_17.03_kubeadm_v1.11.1.sh\""
   cmd = cmd_part1 + cmd_part2
   os.system(cmd)
   print "DONE INSTALLING on %s" % ip
