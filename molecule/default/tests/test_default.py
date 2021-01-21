import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hostname(host):
    needed_hostname = host.ansible.get_variables()['inventory_hostname']
    hostname = host.ansible("command", "hostname -f", check=False)['stdout']
    assert hostname == needed_hostname


def test_dns(host):
    f = host.file("/etc/resolv.conf")
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ntp(host):
    assert host.package("chrony").is_installed
    assert host.service("chrony").is_enabled \
        or host.service("chronyd").is_enabled
    assert host.service("chrony").is_running \
        or host.service("chronyd").is_running
    f = host.file("/etc/chrony.conf")
    assert f.exists
    assert f.contains('pool 0.debian.pool.ntp.org iburst')
    assert f.contains('pool 1.debian.pool.ntp.org iburst')
    assert f.contains('pool 2.debian.pool.ntp.org iburst')
    assert f.contains('pool 3.debian.pool.ntp.org iburst')
