from subprocess import PIPE, Popen

import neovim

ISORT_COMMAND = 'isort'


@neovim.plugin
class IsortNvim:

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command(
        'Isort', nargs='*', range='%',
        complete='customlist,IsortCompletions')
    def isort_command(self, args, range):
        text = self._get_lines(range)
        output = self._isort(text)
        lines = output.split('\n')[:-1]
        self.nvim.current.buffer[range[0] - 1:range[1]] = lines

    def error(self, msg):
        self.nvim.err_write('[isort] {}\n'.format(msg))

    def _get_lines(self, range):
        lines = self.nvim.current.buffer[range[0] - 1:range[1]]
        return '\n'.join(lines)

    def _isort(self, text, *args):
        isort_command = self.nvim.vars.get('isort_command', ISORT_COMMAND)
        isort_args = [isort_command] + list(args) + ['-']
        with Popen(isort_args, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            output, error = proc.communicate(input=text.encode())
            return output.decode()

    @neovim.function('IsortCompletions', sync=True)
    def isort_completions(self, args):
        arglead, cmdline, cursorpos, *_ = args
        return [
            '--line-width',
            '--top',
            '--future',
            '--builtin',
            '--thirdpaty',
            '--project',
            '--virtual-env',
            '--multi-line',
            '--indent',
            '--add-import',
            '--force-adds',
            '--remove-import',
        ]
