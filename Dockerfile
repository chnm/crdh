FROM ruby:3.1.2 as build-stage

ARG configfile
ENV CONFIG_FILE $configfile

WORKDIR /app
ADD . .

RUN gem install bundler
RUN bundle install
RUN bundle exec jekyll build --destination ./_site --config _config.yml,${CONFIG_FILE}

FROM nginx:1.23-alpine

COPY --from=build-stage /app/_site/ /usr/share/nginx/html
