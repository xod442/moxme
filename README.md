# moxme
Yet another python bininding for proxmox server automation

## Access Program variables

Reverts one VM at a time, call with these variables

- promox_host - the IP address of the proxmox server or cluster
- proxmox_user - user ID should be something that was created to support API's make sure you have one
- Proxmox_password - password for the API user
- base_url - EX: https://192.168.1.1:8006/api2/json
- node - the name of the Proxmox host EX: r4025-lg4-esx-02
- vm_id - a number that represents the vm to be reverted
- snapshot_name - the name of the snapshot to revert to
