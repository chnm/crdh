FROM ruby:3.1.2 as build-stage

ARG baseurl
ENV BASE_URL $baseurl
ARG addargs
ENV ADD_ARGS $addargs

WORKDIR /app
ADD . .

RUN gem install bundler
RUN bundle install
RUN bundle exec jekyll build --baseurl "${BASE_URL}" ${ADD_ARGS} --config _config.yml
