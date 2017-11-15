#!/usr/bin/env bash
set -e

git clone -b json --quiet "https://github.com/${TRAVIS_REPO_SLUG}.git"
npm run build
git add plugins.min.json
git commit -m "Update from travis $TRAVIS_COMMIT"
git push "https://${GITHUB_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git" json