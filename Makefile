# File:  setup/Makefile (from github.com/txt/evil)
# # Usage: make
typo:   ready
	@- git status
	@- git commit -am "saving"
	@- git push origin master # insert your branch names here

commit: ready
	@- git status
	@- git commit -a
	@- git push origin master

update: ready
	@- git pull origin master

status: ready
	@- git status

ready:
	@git config --global credential.helper osxkeychain
	#@git config credential.helper 'cache --timeout=3600'

kelei:  
	@git config --global user.name "Kelei Gong" #<== your name
	@git config --global user.email kgong@ncsu.edu #<== your email
