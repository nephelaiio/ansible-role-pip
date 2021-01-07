# nephelaiio.pip

[![Build Status](https://github.com/nephelaiio/ansible-role-pip/workflows/CI/badge.svg)](https://github.com/nephelaiio/ansible-role-pip/actions)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.pip-blue.svg)](https://galaxy.ansible.com/nephelaiio/pip/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/pip) to install and configure pip

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook

```
- hosts: servers
  roles:
     - role: pip
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Focal
  * Ubuntu Bionic
  * Ubuntu Xenial
  * CentOS 7
  * Debian Buster

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
