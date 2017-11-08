#!/usr/bin/env bash
set -e

git clone "https://github.com/${TRAVIS_REPO_SLUG}.git" json
npm run build
git add plugins.min.json
git commit -m "Update from travis $TRAVIS_COMMIT"
git push -f --quiet "https://${GITHUB_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git" json 2> /dev/null