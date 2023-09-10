#!/bin/bash

repoRoot="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"

streamlit run "$repoRoot"/src/app.py