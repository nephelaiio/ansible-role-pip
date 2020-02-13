# nephelaiio.pip

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-pip.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-pip)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-systemd--service-blue.svg)](https://galaxy.ansible.com/nephelaiio/pip/)

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
  * Ubuntu Xenial
  * Ubuntu Bionic
  * CentOS 7
  * CentOS 8
  * Debian Stretch
  * Debian Buster

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
