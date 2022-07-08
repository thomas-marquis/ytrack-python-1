#!/bin/bash

set -e

cd /jail

mkdir run
mkdir run/tests

cp -rf ./student/* ./run
rm -rf ./run/tests

cd run
cp -rf "/app/tests/${EXERCISE}" ./tests

if [ -d ./tests/features ]; then
    echo "Launching functional tests"
    cp -rf ./tests/features ./features
    rm -rf ./tests/features
    {
        behave -s
    } || {
        echo "Functional tests ending with code $?"
    }
    echo "Functional tests ending"
fi

echo "Launching unit tests"
pytest --tb=short -v -s
echo "Unit tests ending"
