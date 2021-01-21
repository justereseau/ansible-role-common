# Ansible Role: Common [![Build Status](https://travis-ci.com/justereseau/ansible-role-common.svg?branch=master)](https://travis-ci.com/justereseau/ansible-role-common)

This role deploy bases packages and shits on a **Debian** or a **RedHat** host.

## Shits intalled

- [DNS and Resolve config](tasks/set-dns.yml) (If COMMON_DEPLOY_RESOLVE = true, default: true)

- [Base packages](tasks/base-packages.yml) (If COMMON_DEPLOY_BASE_PACKAGES = true, default: true)

- [NTP Provider](tasks/ntp.yml) (If COMMON_DEPLOY_NTP = true, default: true)

- [Hostname and domain name](tasks/hostname.yml) (If COMMON_DEPLOY_HOSTNAME = true, default: true)

## Role Variables

See [defaults/main.yml](defaults/main.yml):

## License

[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png)](https://http://www.wtfpl.net)
