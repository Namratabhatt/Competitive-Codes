#!bin/bash

folder=$1
number=$2
file="Problem"
pwdc=$(pwd)

mkdir $folder
cd $folder

for (( i=1; i<=$number ;i++))
do
	mkdir $file$i
	cp "$pwdc"/pythonTemplate.py "$file$i"/Solution.py 
done

