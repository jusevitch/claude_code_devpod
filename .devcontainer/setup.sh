#!/bin/bash
# Post-create setup script for DevPod container
# This script runs after the container is created and installs required tools

set -e

echo "=== DevPod Container Setup ==="

# Source nvm environment (required because postCreateCommand runs before shell init)
export NVM_DIR="/usr/local/share/nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
    . "$NVM_DIR/nvm.sh"
fi

# Install uv (fast Python package manager)
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    echo "uv installed successfully"
else
    echo "uv is already installed"
fi

# Install Claude Code
# Using --loglevel=error to reduce output and avoid TTY issues
if ! command -v claude &> /dev/null; then
    echo "Installing Claude Code..."
    npm install -g @anthropic-ai/claude-code --loglevel=error --no-fund --no-audit
    echo "Claude Code installed successfully"
else
    echo "Claude Code is already installed"
fi

# Install OpenAI Codex CLI
if ! command -v codex &> /dev/null; then
    echo "Installing OpenAI Codex CLI..."
    npm install -g @openai/codex --loglevel=error --no-fund --no-audit
    echo "OpenAI Codex CLI installed successfully"
else
    echo "OpenAI Codex CLI is already installed"
fi

# Install shell aliases
if [ -f .devcontainer/.bash_aliases ]; then
    cp .devcontainer/.bash_aliases ~/.bash_aliases
    echo "Shell aliases installed"
fi

echo "=== Setup Complete ==="
echo ""
echo "AI Coding Assistants:"
echo "  Claude Code: claude --dangerously-skip-permissions"
echo "  Codex CLI:   codex --yolo"
