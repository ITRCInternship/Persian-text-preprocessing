# build image
docker build -t nlp-fa:3.8 .

# run any script; here we run the shipped example:
docker run --rm -v "${PWD}:/app" -w /app nlp-fa:3.8 \
           python usage_example.py