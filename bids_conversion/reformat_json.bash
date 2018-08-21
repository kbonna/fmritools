#!/bin/bash
# This script is formatting all .json files in /. and all subfolders
#
# Author: Kamil Bonna
# ICNT, 18/03/2018
shopt -s globstar
for f in **/*.json; do
	python -mjson.tool $f >> temp
	rm $f
	mv temp $f
done
