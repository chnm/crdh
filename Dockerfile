# syntax=docker/dockerfile:1.7

FROM stagex/pallet-nodejs AS build-stage

COPY --from=stagex/user-hugo-extended /usr/bin/hugo /usr/local/bin/hugo

ARG hugobuildargs
ENV HUGO_BUILD_ARGS=$hugobuildargs

WORKDIR /app
COPY . .

# Legacy devDependencies (node-sass/gulp) aren't used for the Hugo build;
# --ignore-scripts skips their postinstall compilation.
RUN npm ci --ignore-scripts

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
