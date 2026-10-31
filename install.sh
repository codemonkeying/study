#!/bin/sh
# Link `study` into ~/.local/bin. Then: study init [URL-of-your-data-repo]
set -e
here=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$HOME/.local/bin"
ln -sf "$here/study.py" "$HOME/.local/bin/study"
chmod +x "$here/study.py"
echo "installed: $HOME/.local/bin/study"
echo "next: study init            (new local data repo)"
echo "  or: study init <git-url>  (clone your existing data repo)"
case ":$PATH:" in *":$HOME/.local/bin:"*) ;; *) echo "add to your shell rc: export PATH=\"\$HOME/.local/bin:\$PATH\"";; esac
