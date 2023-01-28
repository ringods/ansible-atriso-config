# macos-config

[![Continuous Integration](https://github.com/ringods/macos-config/actions/workflows/ci.yml/badge.svg)](https://github.com/ringods/macos-config/actions/workflows/ci.yml)

Ansible driven MacOS configuration automation. Initial inspiration from [Superlumic](https://github.com/superlumic)
but went with a more purer Ansible driven setup similar to [geerlingguy/mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook).

## Inspiration

* [superlumic](https://github.com/superlumic/superlumic-config)
* [osxc](https://github.com/osxc/starter)
* [mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook)
* [macos-virtualbox-vm](https://github.com/geerlingguy/macos-virtualbox-vm)

## Usage

- Install Ansible
- clone this repo
- run `ansible-galaxy install -r requirements.yml`
- run `ansible-playbook ringods.yml -i inventory.ini -K`

To test against a macOS VM running via CirrusLabs Tart:

- run `ansible-playbook ringods.yml -i inventory-tart.ini -K`
