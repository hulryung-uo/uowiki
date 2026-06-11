#!/bin/sh
# Install the optional git hooks in tools/hooks/ into .git/hooks/.
# Currently: pre-commit, which regenerates src/content/docs/changelog.md and
# stages it with every commit (fully automatic changelog). Skip this if you
# prefer to refresh the changelog only at ship time (LIBRARIAN.md step 7).
set -e
ROOT="$(git rev-parse --show-toplevel)"
for hook in "$ROOT"/tools/hooks/*; do
  name="$(basename "$hook")"
  cp "$hook" "$ROOT/.git/hooks/$name"
  chmod +x "$ROOT/.git/hooks/$name"
  echo "installed $name"
done
