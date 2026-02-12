# Use Alpine Linux as base image for smaller size
FROM alpine:3.23 AS build-stage

ARG hugobuildargs
ENV HUGO_BUILD_ARGS=$hugobuildargs

# Set Hugo version - update this to the latest version
ENV HUGO_VERSION=0.154.5
ENV HUGO_BINARY=hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz

# Install Hugo and dependencies + Node.js for SCSS compilation
RUN apk add --no-cache \
    wget \
    ca-certificates \
    gcompat \
    libstdc++ \
    nodejs \
    npm && \
    ARCH=$(uname -m) && \
    case ${ARCH} in \
        x86_64) HUGO_ARCH="Linux-64bit" ;; \
        aarch64) HUGO_ARCH="Linux-ARM64" ;; \
        armv7l) HUGO_ARCH="Linux-ARM" ;; \
        *) echo "Unsupported architecture: ${ARCH}" && exit 1 ;; \
    esac && \
    HUGO_BINARY=hugo_extended_${HUGO_VERSION}_${HUGO_ARCH}.tar.gz && \
    wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY} && \
    tar xzf ${HUGO_BINARY} && \
    mv hugo /usr/local/bin/hugo && \
    rm ${HUGO_BINARY} && \
    apk del wget

RUN hugo version

# Set working directory
WORKDIR /app

# Copy all project files first
ADD . .

# Install npm dependencies AFTER copying all files
# We need foundation-sites (in devDeps) for SCSS source files
# Use --ignore-scripts to skip node-sass/gulp build steps (Hugo compiles SCSS)
# This ensures node_modules is in /app where Hugo's SCSS compiler can find it
RUN npm install --ignore-scripts

# Hugo's Dart Sass doesn't resolve node_modules imports like Node Sass does
# Copy Foundation SCSS from node_modules into assets where Hugo can find it
# Need to copy the entire scss directory including _vendor subdirectory
RUN mkdir -p assets/vendor && \
    cp -r node_modules/foundation-sites assets/vendor/ && \
    cp -r node_modules/motion-ui assets/vendor/

# Build the site with Hugo
RUN hugo ${HUGO_BUILD_ARGS}

FROM nginx:1.23-alpine

COPY --from=build-stage /app/public/ /usr/share/nginx/html

# Create symlink from /img to /assets/img for backward compatibility with markdown image paths
RUN ln -s /usr/share/nginx/html/assets/img /usr/share/nginx/html/img


