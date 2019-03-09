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

To finish up the correct font usage, execute these manual steps:

- iTerm
  - In `Preferences`, go to `Profiles`
  - Per profile you want to use, go to `Text`
  - Set the font to the Powerline font installed via this Ansible config.
- Visual Studio Code
  - Follow [this StackOverflow answer](https://stackoverflow.com/a/48038543/7269988)
