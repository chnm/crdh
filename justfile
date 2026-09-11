# List available recipes
default:
    @just --list

# Install npm dependencies (PostCSS/Tailwind, needed by hugo)
setup:
    npm ci

# Serve the site locally with drafts and live reload
preview:
    hugo server --buildDrafts --navigateToChanged

# Build the production site into public/
build:
    hugo --minify

# Build with the same flags as the Docker/CI image
build-ci:
    hugo --buildDrafts --buildFuture

# Remove generated output and Hugo caches
clean:
    rm -rf public resources/_gen .hugo_build.lock
