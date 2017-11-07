#!/usr/bin/env bash

set -e

npm run build
git add plugins.min.json
git commit -m "Update from travis $TRAVIS_COMMIT"
git push --quiet "https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG}.git" json 2> /dev/null