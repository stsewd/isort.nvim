# Isort.nvim

Neovim plugin to sort python imports using [isort](https://github.com/timothycrosley/isort).

Inspired by [vim-isort](https://github.com/fisadev/vim-isort).

## Requirements

- [Isort](https://github.com/timothycrosley/isort) (`pip install isort`).
- The `isort` command must be on your `PATH`.
- Make sure that you install the latest version of isort (or at least >=5.7.0)

## Install

Install using [vim-plug](https://github.com/junegunn/vim-plug).
Put this on your `init.vim`.

```vim
Plug 'stsewd/isort.nvim', { 'do': ':UpdateRemotePlugins' }
```

## Usage

Call `:Isort` and it will sort the imports of the current buffer.
You can also pass a range via the visual mode.

_All arguments of the command will be passed to isort_.

Alternatively, use `:IsortSync` if you need the operation to complete
synchronously (e.g. in a BufWritePre autocmd).

## Configuration

Isort command.

```vim
g:isort_command = 'isort'
```

## Differences with vim-isort

- No need to install isort on the same python environment.
- Pure python implementation.
- Neovim only.
