import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(host):
    if host.exists('pip3'):
        assert host.command('pip3 --version').rc == 0
    else:
        assert host.command('pip --version').rc == 0


def test_pip(host):
    if host.exists('pip3'):
        assert 'setuptools' in host.pip_package.get_packages(pip_path='pip3')
    else:
        assert 'setuptools' in host.pip_package.get_packages(pip_path='pip')
