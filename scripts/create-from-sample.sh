#!/bin/bash
# create ./config/.env file from .env.SAMPLE if not exists
# create ./.vscode/settings.json file from settings.json.SAMPLE if not exists
#
set -e

repoRoot="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"

envFilePath="$repoRoot/.env"
envFileSamplePath="$repoRoot/.env.SAMPLE"

if [ ! -e $envFilePath ];then
  cp $envFileSamplePath $envFilePath
fi

settingsFilePath="$repoRoot/.vscode/settings.json"
settingsFileSamplePath="$repoRoot/.vscode/settings.json.SAMPLE"

if [ ! -e $settingsFilePath ];then
  cp $settingsFileSamplePath $settingsFilePath
fi
