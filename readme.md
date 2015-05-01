# Demokratikollen Server deploy scripts.

# Use Ansible to config a remote server.

1. Create provision/users/files/authorized_keys containing the ssh keys needed to access the server.
2. Create an Ansible inventory file containing a remote machine in the group "remote".
3. Export a variable NEW_RELIC_LICENCE_KEY set to the new relic licene key.
4. Run this ansible onto the machine.

# After server is provisioned.
1. Clone demokratikollen into /home/deploy/demokratikollen_old
2. Copy over a backup of an old /home/deploy/data dir with database_dumps containing _latest versions.

3. Clone demokratikollen to your own pc. 
4. Modify the deploy ansible to use the deployment_first.py instead of deployment.py
5. Set the SECRET envs for cookie and CSRF.
6. Set DEPLOY env to all
5. Run the ansible, keep fingers crossed.
6. Monitor on the server or tunnel port 8080 to get to the deploy log.
