# Claude Code DevPod Template

Run Claude Code safely inside Docker containers using DevPod.

Claude Code is powerful. Running it unconstrained on your computer is risky. This template runs it within Docker containers to mitigate the risk of data loss or corruption from hallucinations.

[DevPod](https://devpod.sh/) is an open source alternative to GitHub Codespaces. It lets you spin up development containers from a `.devcontainer` configuration with a single command.

## Prerequisites

(Skip if you've done this before)

1. [Install Docker](https://docs.docker.com/engine/install/)
2. [Install DevPod CLI](https://devpod.sh/docs/getting-started/install#install-devpod-cli)
3. Add Docker to DevPod as the default provider:
```bash
devpod provider add docker
devpod provider use docker
```

## Quick Start

1. Clone this repository and `cd` into it
2. Run `devpod up . --ide vscode`

That's it! Claude Code is automatically installed and ready to use.

## What's Included

- **Claude Code** - Anthropic's AI coding assistant (auto-installed)
- **Python** + **uv** - Python with fast package management
- **Rust** - Full Rust toolchain with rust-analyzer
- **Node.js** - JavaScript runtime
- **Git** + **GitHub CLI** - Version control

## Using Claude Code

Once the container opens in VS Code:

```bash
# Start Claude Code (recommended for containers)
claude --dangerously-skip-permissions

# Or start with normal permissions
claude
```

## Customization

Edit `.devcontainer/devcontainer.json` to customize your environment:

- Change the base image (Debian, Fedora, etc.)
- Add/remove language features (Julia, Go, etc.)
- Add VS Code extensions
- Modify the setup script in `.devcontainer/setup.sh`

See [devcontainer features](https://containers.dev/features) for available options.

## How It Works

The `.devcontainer/` folder contains:
- `devcontainer.json` - Container configuration
- `setup.sh` - Post-creation script that installs Claude Code and uv

The `.claude/settings.json` file pre-configures Claude Code to bypass permission prompts (safe within containers).

## See Also

* [Claude Code DevPod template for Python only](https://github.com/jusevitch/claude_code_python)
* [Claude Code DevPod template for Rust only](https://github.com/jusevitch/claude_code_rust)

## Resources

- [DevPod Documentation](https://devpod.sh/docs)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Devcontainer Features](https://containers.dev/features)
- [Microsoft Devcontainer Images](https://hub.docker.com/r/microsoft/devcontainers)
