FROM ruby:3.1.2 as build-stage

ARG configfile
ENV CONFIG_FILE $configfile

WORKDIR /app
ADD . .

RUN gem install bundler
RUN bundle install
RUN bundle exec jekyll build --config _config.yml,${CONFIG_FILE}
