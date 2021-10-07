# CRDH

This repository contains the website for [*Current Research in Digital History*](http://crdh.rrchnm.org/), a publication of the [Roy Rosenzweig Center for History and New Media](http://rrchnm.org) at George Mason University.

## Building the site

This site is built using Jekyll (which has Ruby dependencies manged by bundler), and the site assets are built using Gulp (which has Node dependencies managed by npm).

Follow these steps to install the necessary software.

1. Install current version of Ruby for your platform. This repository is generally kept up to date with the version of Ruby provided by Homebrew. You can see the Ruby version in the `Gemfile`.
2. Install bundler with `gem install bundler`.
3. Install Jeykll and its dependencies with `bundle install`.
4. \[OPTIONAL\] Install the Node dependencies with `npm install`.

Once everything is installed, you should be able to preview the site locally by running `make preview`.

