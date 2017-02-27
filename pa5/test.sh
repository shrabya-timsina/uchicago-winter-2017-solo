#!/bin/sh

for filename in speeches/bush-kerry3/*.txt; do
	for file in speeches/bush-kerry3/*.txt; do
		for last in speeches/bush-kerry3/*.txt; do
			echo
			echo "filename: " $filename
			echo "file: " $file
			echo "last: " $last
			echo
		    python3 Markov.py $filename $file $last 3
		    echo "------------------------------"
		    sleep 3
		done
	done
done