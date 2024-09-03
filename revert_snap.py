'''
███    ███  ██████  ██   ██ ███    ███ ███████ 
████  ████ ██    ██  ██ ██  ████  ████ ██      
██ ████ ██ ██    ██   ███   ██ ████ ██ █████   
██  ██  ██ ██    ██  ██ ██  ██  ██  ██ ██      
██      ██  ██████  ██   ██ ██      ██ ███████

Example Script for reverting a virtual machine
'''
import requests
import sys
import urllib3
from utility.moxme import get_ticket
from utility.moxme import revert_snapshot
from utility.moxme import moxme
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

   
def main():
    # Get authentication ticket and CSRF token
    ticket, csrf_token = get_ticket(info['base_url'],info['proxmox_user'],info['proxmox_password'])

    # Revet the VM to the specified snapshot
    response = revert_snapshot(ticket,
                               csrf_token,
                               info['base_url'],
                               info['node'],
                               info['vm_id'],
                               info['snapshot_name'])

if __name__ == "__main__":
    # Get program variables
    info = moxme()

    main()
