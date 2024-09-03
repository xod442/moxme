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
__name__ = moxme_auth.py

A python script to get the ticket and csrf_token

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

