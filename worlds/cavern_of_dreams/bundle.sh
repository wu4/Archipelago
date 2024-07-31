#!/bin/sh

cd "$(dirname "$0")/.."
zip -r cavern_of_dreams.apworld cavern_of_dreams -x cavern_of_dreams/bundle.sh
mv cavern_of_dreams.apworld ../..
