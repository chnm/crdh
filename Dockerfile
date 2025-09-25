FROM ruby:3.1.2 AS build-stage

ARG environment
ARG configfile
ENV ENVIRONMENT=$environment
ENV CONFIG_FILE=$configfile

WORKDIR /app
ADD . .

RUN gem install bundler
RUN bundle install
RUN JEKYLL_ENV=${ENVIRONMENT} bundle exec jekyll build --destination ./_site --config _config.yml,${CONFIG_FILE}

FROM nginx:1.23-alpine

COPY --from=build-stage /app/_site/ /usr/share/nginx/html
