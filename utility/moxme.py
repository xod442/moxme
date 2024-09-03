'''
███    ███  ██████  ██   ██ ███    ███ ███████ 
████  ████ ██    ██  ██ ██  ████  ████ ██      
██ ████ ██ ██    ██   ███   ██ ████ ██ █████   
██  ██  ██ ██    ██  ██ ██  ██  ██  ██ ██      
██      ██  ██████  ██   ██ ██      ██ ███████

A set of functions for interacting with proxmox


   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__status__ = "Alpha"

'''
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_ticket(api_url, proxmox_user, proxmox_password):
    # Authenticate and retrieve the API ticket and CSRF token
    url = f"{api_url}/access/ticket"
    data = {
        'username': proxmox_user,
        'password': proxmox_password,
        'realm': 'pve'
    }
    try:
        # response = requests.post(url, data=data, allow_redirects=False, verify=False)
        response = requests.post(url, data=data, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to authenticate: {e}")
        sys.exit(1)
    
    ticket = response.json()['data']['ticket']
    csrf_token = response.json()['data']['CSRFPreventionToken']
    return ticket, csrf_token

def revert_snapshot(ticket,csrf_token,base_url,node,vm_id,snapshot_name):
    # Revert the VM to the specified snapshot
    url = f"{base_url}/nodes/{node}/qemu/{vm_id}/snapshot/{snapshot_name}/rollback"
    headers = {
        'CSRFPreventionToken': csrf_token,
        'Cookie': f'PVEAuthCookie={ticket}'
    }
    
    try:
        response = requests.post(url, headers=headers, verify=False)
        response.raise_for_status()
        print(f"Successfully reverted VM {vm_id} to snapshot '{snapshot_name}'.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to revert snapshot: {e}")
        sys.exit(1)

    
def moxme():

    proxmox_host = "10.250.0.14"

    # Get parameters for function
    moxme = {
         "vm_id": "101",
         "node": "r4025-lg4-esx-02",
         "proxmox_user": "api",
         "proxmox_password": "Aruba123!@#",
         "vm_id": "101",
         "snapshot_name": "no-folder",
         "base_url": f"https://{proxmox_host}:8006/api2/json"

     } 
    
    return moxme