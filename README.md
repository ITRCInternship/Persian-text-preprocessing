# Persian-text-preprocessing
docker build -t nlp-fa:3.8 .
docker run --rm -v "${PWD}:/app" -w /app nlp-fa:3.8 pytest -q
