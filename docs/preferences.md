# Preferences

Skills here target my setup. Commands a skill shows follow these choices.

## Install commands

- Userland CLIs: `mise use -g <backend>:<tool>`. Prefer backends that fetch built releases (`github:`, `aqua:`) over ones that build from source (`cargo:`, `go:`).
- System-wide programs: `pacman -S`, or `yay -S` for AUR packages.

## Agent instructions file

- Refer to `AGENTS.md`, never `CLAUDE.md`. Claude Code reads `AGENTS.md` too.

## CLI output

- Commands output minified JSON with no color. Pass the flags only when the CLI doesn't already default to that.
- Exceptions are fine. A CLI's JSON is not always its plain output in another format: it can be a much larger dump or lack what the plain output shows. Keep plain output where it is the better read.
