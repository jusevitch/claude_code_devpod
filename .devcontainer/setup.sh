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

# Source uv environment
export PATH="$HOME/.local/bin:$PATH"

# Install Python 3.12 via uv (ensures it's available for uv projects)
echo "Installing Python 3.12 via uv..."
uv python install 3.12
echo "Python 3.12 installed"

# Install Claude Code
# Using --loglevel=error to reduce output and avoid TTY issues
if ! command -v claude &> /dev/null; then
    echo "Installing Claude Code..."
    npm install -g @anthropic-ai/claude-code --loglevel=error --no-fund --no-audit
    echo "Claude Code installed successfully"
else
    echo "Claude Code is already installed"
fi

echo "=== Setup Complete ==="
echo ""
echo "To start Claude Code, run: claude"
echo "To start with all permissions (recommended in containers): claude --dangerously-skip-permissions"
