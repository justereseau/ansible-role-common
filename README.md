# Ansible Role: Common [![Build Status](https://travis-ci.org/lucasmaurice/ansible-role-common.svg?branch=master)](https://travis-ci.org/lucasmaurice/ansible-role-common)

This role deploy bases packages and shits on a **Debian** or a **RedHat** host.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
---
# DNS Related vars
RESOLV_NAMESERVERS:
  - 1.1.1.1
  - 1.0.0.1
RESOLV_SEARCH: []
RESOLV_SORTLIST: []
RESOLV_OPTIONS: []
RESOLV_DOMAIN: ''

# Define if need vm guest tools.
# Can be `ESXi` ; `Proxmox` ; or `none`
COMMON_VM_HOST: none

```

- `RESOLV_NAMESERVERS`: The list of nameserver to install.

- `RESOLV_SEARCH`:

- `RESOLV_SORTLIST`:

- `RESOLV_OPTIONS`:

- `RESOLV_DOMAIN`:

- `COMMON_VM_HOST`: Define if this is a and need vm guest tools. Can be `ESXi` ; `Proxmox` ; or `none`

## License

[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png)](https://http://www.wtfpl.net)
