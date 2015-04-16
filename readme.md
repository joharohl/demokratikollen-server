# Demokratikollen Server deploy scripts.

# Use Ansible to config a remote server.

1. Create provision/users/files/authorized_keys containing the ssh keys needed to access the server.
2. Create an Ansible inventory file containing a remote machine in the group "remote".
3. Run: 