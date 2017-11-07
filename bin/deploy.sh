#!/usr/bin/env bash

set -e

git clone git@github.com:${TRAVIS_REPO_SLUG}.git
npm run build
git add plugins.min.json
git commit -m "Update from travis $TRAVIS_COMMIT"
git push origin json