gulp = ./node_modules/gulp/bin/gulp.js
# Creating the CSS needs to be run through Gulp

preview : clean
	bundle exec jekyll serve --watch --drafts --config _config.yml,_config-preview.yml

clean :
	rm -rf _site/*

.PHONY: preview clean 
