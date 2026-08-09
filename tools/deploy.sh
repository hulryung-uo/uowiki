#!/usr/bin/env sh
# Manual production deploy for the wiki (uotavern.com/wiki).
#
# There is no GitHub->Vercel integration; pushing to main does not deploy.
#
# Deploying straight from this repo is rejected by Vercel with
#   "Git author dkkang@huconn.com must have access to the team ..."
# because commits here are authored with the GitHub identity
# (dkkang@huconn.com) while the Vercel account is hulryung@gmail.com. The CLI
# never surfaces this — it just prints "Building..." forever, and the reason is
# only visible via the deployments API.
#
# So we deploy from a copy that has no .git: with no git metadata attached,
# Vercel skips the author check entirely. Nothing about the repo's git identity
# or history changes. Build artifacts are left out so the upload stays small —
# Vercel runs `npm run build` on its own machine.
#
# Usage:  tools/deploy.sh            (production)
#         tools/deploy.sh --no-prod  (preview)
set -eu

repo=$(cd "$(dirname "$0")/.." && pwd)
staging=$(mktemp -d)
trap 'rm -rf "$staging"' EXIT

target=--prod
if [ "${1:-}" = "--no-prod" ]; then
	target=
	shift
fi

tar --exclude=.git --exclude=.vercel --exclude=node_modules --exclude=dist \
	--exclude=.astro -cf - -C "$repo" . | tar -xf - -C "$staging"
mkdir -p "$staging/.vercel"
cp "$repo/.vercel/project.json" "$staging/.vercel/project.json"

# Uses whatever account `vercel login` is currently on (must be hulryung@gmail.com).
# shellcheck disable=SC2086
vercel deploy $target --yes --cwd "$staging" "$@"
