# Demokratikollen Server deploy scripts.

# Use Ansible to config a remote server.

1. Create provision/users/files/authorized_keys containing the ssh keys needed to access the server.
2. Create an Ansible inventory file containing a remote machine in the group "remote".
3. Export a variable NEW_RELIC_LICENCE_KEY set to the new relic licene key.
3. Run: 