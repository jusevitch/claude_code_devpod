# Claude Code DevPod Template

This file is a template for creating containers using DevPod to run Claude Code inside.

Claude Code is powerful. Running it unconstrained in your computer is probably a bad idea. A better idea is to use it within Docker or Podman containers to mitigate the risk of it hallucinating and causing data loss or corruption.

[DevPod](https://devpod.sh/) is an open source alternative to Codespaces. It allows you to specify a Docker (or Podman) container in a `.devcontainer.json` file, save it within a repository, then activate that repository locally within a Docker container. You can then run `claude --dangerously-skip-permissions` to your heart's content.

The key advantage of DevPod is its simplicity:

* `git clone` a repository with a `.devcontainer.json` file
* Create a new workspace using the DevPod GUI (or `devpod up . --ide vscode` using the CLI)
* Use VSCode to watch Claude happily create either works of genius or horrifying chaos within a Docker container
* Push changes up to Github.

## Instructions for use

This repository contains enough to run a fully functional (albeit minimal) DevPod Ubuntu environment with Rust, Python, uv, Git, the Github CLI, and Node.js (for Claude Code) preinstalled.

To use this for your own environments:

* Clone the repository
* Edit the `.devcontainer.json` file to fit your specifications. For example,
  * You can change the base image (e.g. Debian, Fedora, etc.). The `mcr.microsoft.com` images seem to work best with fewest errors.
  * You can change the features. Add Julia, remove Python, etc.
* Create a new Workspace using DevPod
* Launch and install Claude Code by running `npm install -g @anthropic-ai/claude-code` (this will persist in future sessions).
* Add your code.
* Push code to Github.

Anyone in the future who wants to reproduce your environment can simply clone it and use it to create a new DevPod workspace.


## Additional Resources

* Microsoft Docker devcontainers: https://hub.docker.com/r/microsoft/devcontainers
* Devcontainer Features: https://containers.dev/features (e.g. Rust, Python, CUDA, etc.)


## Known Issues

* It should be possible to install Claude Code automatically. I have not figured out how to do this without crashing the DevPod build process.