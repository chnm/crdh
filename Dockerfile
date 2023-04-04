FROM ruby:3.1.2 as build-stage

WORKDIR /app
ADD . .

RUN gem install bundler
RUN bundle install
