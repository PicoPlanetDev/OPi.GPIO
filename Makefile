# build
build:
	echo "Building..."
	rm -rf ./dist
	python3 -m build

# upload
upload:
	echo "Uploading..."
	python3 -m twine upload dist/*

# upload test
upload-test:
	echo "Uploading to test..."
	python3 -m twine upload --repository testpypi dist/*