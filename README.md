# build image
docker build -t nlp-fa:3.8 .

# run any script; here we run the shipped example:

## normalizer

docker run --rm -e PYTHONPATH=/app nlp-fa:3.8 usage_examples/normalization_example.py

## spell checker

docker run --rm -e PYTHONPATH=/app nlp-fa:3.8 usage_examples/spell_example.py

## informal to formal convertor

docker run --rm -e PYTHONPATH=/app nlp-fa:3.8 usage_examples/formal_example.py