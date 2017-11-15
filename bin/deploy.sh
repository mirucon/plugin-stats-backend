#!/usr/bin/env bash
set -e

openssl version

echo -e "Host github.com\n\tStrictHostKeyChecking no\nIdentityFile ~/.ssh/deploy.key\n" >> ~/.ssh/config
openssl aes-256-cbc -k "$SERVER_KEY" -in .travis/deploy_key.enc -d -a -out deploy.key
cp deploy.key ~/.ssh/
chmod 600 ~/.ssh/deploy.key

git clone -b json --quiet "https://github.com/${TRAVIS_REPO_SLUG}.git"
npm run build
git add plugins.min.json
git commit -m "Update from travis $TRAVIS_COMMIT"
git push origin json