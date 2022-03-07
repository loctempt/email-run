make_dir:=$(shell pwd)

install:
	chmod u+x mail-run.py
	echo $(make_dir)
	ln -s $(make_dir)/mail-run.py /usr/local/bin/mail-run

uninstall:
	rm /usr/local/bin/mail-run
