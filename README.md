# ansible-atriso-config

Ansible driven configuration automation for:

* macOS
* [PiKVM](https://pikvm.org/)

Initial inspiration for the macOS setup from [Superlumic](https://github.com/superlumic)
but went with a more purer Ansible driven setup similar to [geerlingguy/mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook).

## Inspiration

* [superlumic](https://github.com/superlumic/superlumic-config)
* [osxc](https://github.com/osxc/starter)
* [mac-dev-playbook](https://github.com/geerlingguy/mac-dev-playbook)
* [macos-virtualbox-vm](https://github.com/geerlingguy/macos-virtualbox-vm)

## Preparation

* Install Ansible
* clone this repo
* run `ansible-galaxy install -r requirements.yml`

## Usage

For the MacBook Pro laptops, use one of the following commands:

* run `ansible-playbook playbooks/mac/main.yml -i inventories/atrisobook2020 -K`
* run `ansible-playbook playbooks/mac/main.yml -i inventories/atrisobook2022 -K`

For the PiKVM, use the following command:

* run `ansible-playbook playbooks/pikvm/main.yml -i inventories/pikvm --extra-vars @secrets.yml`

The `secrets.yml` file contains a DNSimple API token created on the [DNSimple portal](https://dnsimple.com/dashboard).

The ssh keys can be found in 1Password.
