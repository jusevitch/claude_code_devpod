# Claude Code DevPod Template

This is a template repository for running Claude Code in DevPod containers.

## Project Structure

- `.devcontainer/devcontainer.json` - Container configuration
- `.devcontainer/setup.sh` - Post-creation setup script (installs Claude Code + uv)
- `.claude/settings.json` - Claude Code settings (bypasses permissions in container)

## Development

To test changes to the devcontainer configuration:

```bash
devpod up . --ide vscode
```

## Included Tools

- Node.js (for Claude Code)
- Python + uv
- Rust + rust-analyzer
- Git + GitHub CLI
