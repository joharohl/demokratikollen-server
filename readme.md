# Demokratikollen Server deploy scripts.

# Use Ansible to config a remote server.

1. Create provision/users/files/authorized_keys containing the ssh keys needed to access the server.
2. Create an Ansible inventory file containing a remote machine in the group "remote".
3. Export a variable NEW_RELIC_LICENCE_KEY set to the new relic licene key.
3. Run: 

# Create server from scratch.
0. Run this ansible onto the machine.
1. Clone the src into /home/deploy
2. Copy over a backup of an old /home/deploy/data dir
3. Ssh to the server and run the first_deployment.py