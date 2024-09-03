'''
███    ███  ██████  ██   ██ ███    ███ ███████ 
████  ████ ██    ██  ██ ██  ████  ████ ██      
██ ████ ██ ██    ██   ███   ██ ████ ██ █████   
██  ██  ██ ██    ██  ██ ██  ██  ██  ██ ██      
██      ██  ██████  ██   ██ ██      ██ ███████

Example Script for reverting a virtual machine

Reverts one VM at a time, call with these variables

promox_host - the IP address of the proxmox server or cluster
proxmox_user - user ID should be something that was created to support API's make sure you have one
Proxmox_password - password for the API user
base_url - EX: https://192.168.1.1:8006/api2/json
node - the name of the Proxmox host EX: r4025-lg4-esx-02
vm_id - a number that represents the vm to be reverted
snapshot_name - the name of the snapshot to revert to


'''
import requests
import sys
import urllib3
from proxmox.moxme_auth import get_ticket
from proxmox.moxme_vms import revert_snapshot
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

   
def main():
    # Get authentication ticket and CSRF token
    ticket, csrf_token = get_ticket(base_url,proxmox_user,proxmox_password)
    
    # Revet the VM to the specified snapshot
    response = revert_snapshot(ticket,csrf_token,base_url,node,vm_id,snapshot_name)
    

if __name__ == "__main__":

    # TODO: Get these vars from user args
    proxmox_host = "10.250.0.14"
    proxmox_user = "api"
    proxmox_password = 'Aruba123!@#'
    base_url = f"https://{proxmox_host}:8006/api2/json"
    node = "r4025-lg4-esx-02"
    vm_id = "101"
    snapshot_name = "no-folder"

    main()
