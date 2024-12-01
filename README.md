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
* run `ansible-galaxy install -r requirements.yml --force`

## Usage

For the MacBook Pro laptops, use one of the following commands:

* run `ansible-playbook playbooks/mac-personal/main.yml -K`
* run `ansible-playbook playbooks/mac-work/main.yml -K`

For the PiKVM, use the following command:

* run `ansible-playbook playbooks/pikvm/main.yml --extra-vars @secrets.yml`

The `secrets.yml` file contains a DNSimple API token created on the [DNSimple portal](https://dnsimple.com/dashboard).

The ssh keys can be found in 1Password.

## Needs automation

The following parts need conversion into Ansible roles & tasks, but are documented here in the meantime.

### PiKVM

After the Ansible setup, the PiKVM has the Certbot DNSimple plugin installed, together with the config file containing a DNSimple API token. The following commands are a one time setup required to get the certificate generated and renewed automatically:

```bash
$ rw
$ kvmd-certbot certonly --dns-dnsimple --dns-dnsimple-credentials /var/lib/kvmd/pst/data/certbot/runroot/certbot-dnsimple.conf -d kvm.home.atriso.be --email ringo@de-smet.name -n --agree-tos
$ kvmd-certbot install_nginx kvm.home.atriso.be
$ kvmd-certbot install_vnc kvm.home.atriso.be
$ systemctl enable --now kvmd-certbot.timer
$ ro
```
