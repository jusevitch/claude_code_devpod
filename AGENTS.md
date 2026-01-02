# AI Coding Agents DevPod Template

This is a template repository for running AI coding agents in DevPod containers.

## Project Structure

- `.devcontainer/devcontainer.json` - Container configuration
- `.devcontainer/setup.sh` - Post-creation setup script (installs Claude Code, Codex CLI, and uv)
- `.claude/settings.json` - Claude Code settings (bypasses permissions in container)

## Development

To test changes to the devcontainer configuration:

```bash
devpod up . --ide vscode
```

## Included Tools

### AI Coding Agents
- Claude Code (Anthropic)
- Codex CLI (OpenAI)

### Development Tools
- Node.js (for Claude Code and Codex CLI)
- Python + uv
- Rust + rust-analyzer
- Git + GitHub CLI