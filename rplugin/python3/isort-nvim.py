from subprocess import PIPE, Popen

import neovim

ISORT_COMMAND = 'isort'


@neovim.plugin
class IsortNvim:

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('Isort', nargs='*', range='%', complete='file')
    def isort_command(self, args, range):
        current_file = self.nvim.call('expand', '%')
        if not current_file:
            self.error('The current buffer is not saved')
            return
        output = self._isort(current_file)
        lines = output.split('\n')[:-1]
        self.nvim.current.buffer[:] = lines

    def error(self, msg):
        self.nvim.err_write('[isort] {}\n'.format(msg))

    def _isort(self, file):
        isort_command = self.nvim.vars.get('isort_command', ISORT_COMMAND)
        args = [isort_command, '--stdout', file]
        with Popen(args, stdout=PIPE) as proc:
            return proc.stdout.read().decode()
