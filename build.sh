#!/bin/sh
# Local build + link check. Run this when you've added/changed content (or any
# time you want a full check). This is NOT the production build: CI (.github/
# workflows/hugo.yml) deploys with the real baseURL. Here we build with
# baseURL "/" so htmltest can resolve root-relative internal links against public/.
#
# The link check catches files that were referenced but never published — e.g. a
# raw Markdown [text](./file) link to a bundle file, which publishResources=false
# does not publish (see the cascade note in hugo.toml). It also flags broken
# internal links and dead #anchors. Config lives in .htmltest.yml.
# Install the checker once with: brew install htmltest
#
# For live editing/preview, keep using `hugo serve`.

set -e
rm -rf public
hugo --baseURL /
htmltest

# Old local-preview invocation, kept for reference:
# hugo --baseURL https://localhost:8080/public/
# Production deploy URL (handled by CI, not here):
# hugo --baseURL https://pages.graphics.cs.wisc.edu/VisSnacks/
