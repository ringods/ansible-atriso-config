from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: 
    short_description: kvmd-pstrun allows writable persistent storage on a PiKVM
    description:
        - This become plugin allows files and folders to be created on the special PiKVM Persistent Storage.
    author: Ringo De Smet
    options:
        become_exe:
            description: kvmd-pstrun executable
            default: kvmd-pstrun
            ini:
              - section: privilege_escalation
                key: become_exe
              - section: kvmd_become_plugin
                key: executable
            vars:
              - name: ansible_become_exe
              - name: ansible_kvmd_exe
            env:
              - name: ANSIBLE_BECOME_EXE
              - name: ANSIBLE_KVMD_EXE
    notes:
      - This plugin ignores the become_user, become_flags & become_pass supplied.
'''

from ansible.plugins.become import BecomeBase
from ansible.module_utils.six.moves import shlex_quote
from ansible.utils.display import Display

display = Display()

class BecomeModule(BecomeBase):

    name = 'community.pikvm.kvmd-pst'
    prompt = 'PST write is allowed: /var/lib/kvmd/pst/data'

    def build_become_command(self, cmd, shell):
        super(BecomeModule, self).build_become_command(cmd, shell)

        if not cmd:
            return cmd

        become = self.get_option('become_exe')

        full_cmd = '%s -- %s' % (become, cmd)
        display.v(u"Full command: %s" % full_cmd)
        return full_cmd
