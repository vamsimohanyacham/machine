#!/bin/bash

VERSION_FILE="version.txt"
if [ -f "$VERSION_FILE" ]; then
    CURRENT_VERSION=$(cat $VERSION_FILE)
    echo "Current version: $CURRENT_VERSION"
else
    CURRENT_VERSION="1.0.0"
    echo "No version file found. Using default version: $CURRENT_VERSION"
fi

IFS='.' read -r -a VERSION_PARTS <<< "$CURRENT_VERSION"
MAJOR=${VERSION_PARTS[0]}
MINOR=${VERSION_PARTS[1]}
PATCH=${VERSION_PARTS[2]}

PATCH=$((PATCH + 1))

NEW_VERSION="${MAJOR}.${MINOR}.${PATCH}"

echo $NEW_VERSION > $VERSION_FILE
echo "New version: $NEW_VERSION"
