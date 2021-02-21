#!/bin/sh
set -x
TRAVIS_REPO_SLUG="jira_travis"
TRAVIS_BRANCH="master"
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t "cryofracture/$TRAVIS_REPO_SLUG:$TAG" .
docker push "cryofracture/$TRAVIS_REPO_SLUG:$TAG"