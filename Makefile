prepare:
	mkvirtualenv jirate

build: 
	workon jirate
	python setup.py build
	python setup.py sdist bdist_wheel

clean:
	rm -rf build dist *.egg-info .eggs