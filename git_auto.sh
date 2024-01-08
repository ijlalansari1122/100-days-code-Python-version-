#!/bin/bash

# Navigate to your project directory
cd /path/to/your/project

# Get the current branch name
branch=$(git rev-parse --abbrev-ref HEAD)

# Check for changes
changes=$(git status --porcelain)

if [ -n "$changes" ]; then
    # Add all changes
    git add .

    # Generate a commit message with a timestamp
    commit_message="Auto commit: $(date +"%Y-%m-%d %H:%M:%S")"

    # Commit changes
    git commit -m "$commit_message"

    # Push to the current branch
    git push origin "$branch"

    echo "Changes committed and pushed successfully."
else
    echo "No changes detected. Nothing to commit or push."
fi
