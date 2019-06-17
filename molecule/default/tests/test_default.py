import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(Command):
    assert Command('pip --version').rc == 0


def test_pip(PipPackage):
    assert 'docker' in PipPackage.get_packages()
