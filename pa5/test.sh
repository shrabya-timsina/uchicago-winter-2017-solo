#!/bin/sh



#  python3 Markov.py speeches/bush-kerry3/BUSH.txt speeches/bush-kerry3/KERRY.txt speeches/bush-kerry3/KERRY-30.txt 3

#for filename in speeches/obama-mccain3/*.txt; do
#   for file in speeches/obama-mccain3/*.txt; do

for last in speeches/obama-mccain3/OBAMA-*.txt; do
echo
#echo "filename: " $filename
#echo "file: " $file
echo "last: " $last
echo
python3 Markov.py speeches/mccain1+2.txt speeches/obama1+2.txt $last 3
echo "------------------------------"
#sleep 3
done
#    done
#done
#python3 Markov.py speeches/mccain1+2.txt speeches/obama1+2.txt speeches/obama-mccain3/OBAMA-47.txt 3