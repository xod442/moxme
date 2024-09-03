# moxie
Yet another python bininding for proxmox server automation

## Access Program variables

- from utility.moxme import moxme
- info = moxme()
- ticket, csrf_token = get_ticket(info['base_url'],info['proxmox_user'],info['proxmox_password'])

Prgram variables are kept in the info dictionary!

