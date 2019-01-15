# macos-config

[![Travis CI - `master`](https://travis-ci.org/ringods/macos-config.svg?branch=master)](https://travis-ci.org/ringods/macos-config)

Ansible driven MacOS configuration automation. Initial inspiration from [Superlumic](https://github.com/superlumic)
but went with a more purer Ansible driven setup similar to [geerlingguy/mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook).

## Inspiration

* [superlumic](https://github.com/superlumic/superlumic-config)
* [osxc](https://github.com/osxc/starter)
* [mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook)

## Usage

- Install Ansible
- clone this repo
- run `ansible-galaxy install -r requirements.yml`
- run `ansible-playbook ringods.yml -i inventory.yml -K`
