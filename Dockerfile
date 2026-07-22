# syntax=docker/dockerfile:1.7

FROM stagex/pallet-nodejs AS build-stage

COPY --from=stagex/user-hugo-extended:0.161.1 /usr/bin/hugo /usr/local/bin/hugo

COPY --from=stagex/core-go /usr/lib/go/lib/time/zoneinfo.zip /zoneinfo.zip
ENV ZONEINFO=/zoneinfo.zip

ARG hugobuildargs
ENV HUGO_BUILD_ARGS=$hugobuildargs

WORKDIR /app

COPY package.json package-lock.json ./
# The legacy Gulp dependencies are not used by the Hugo build. In particular,
# gulp-sass pulls in deprecated node-sass, whose install script requires a
# native build toolchain that is intentionally absent from this image.
RUN npm ci --ignore-scripts

COPY . .

# Hugo's Dart Sass doesn't resolve node_modules imports, so stage
# Foundation SCSS sources where Hugo's asset pipeline can find them.
RUN mkdir -p assets/vendor && \
    cp -r node_modules/foundation-sites assets/vendor/ && \
    cp -r node_modules/motion-ui assets/vendor/

RUN hugo ${HUGO_BUILD_ARGS}

FROM stagex/user-caddy

COPY --from=stagex/core-musl / /
COPY --from=build-stage /app/public /srv

COPY <<'EOF' /etc/caddy/Caddyfile
{
	auto_https off
	admin off
}

:80 {
	root * /srv
	encode gzip zstd

	# Backward compatibility: /img/* serves from /assets/img/*
	rewrite /img/* /assets{uri}

	file_server
}
EOF

ENV XDG_CONFIG_HOME=/tmp/caddy-config \
    XDG_DATA_HOME=/tmp/caddy-data

EXPOSE 80
ENTRYPOINT ["/usr/bin/caddy"]
CMD ["run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
