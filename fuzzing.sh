#!/bin/bash

array=($(ls /root/fuzzing/seedFiles/audio))

for input in ${array[@]}; do
	inputArr=($(echo $input | tr "." "\n"))
	filename=${inputArr[0]}
	ext=${inputArr[1]}
	
	outputFN="/root/fuzzing/seedFiles/output/audioFuzz/sample_%n.${ext}"
	inputFN="/root/fuzzing/seedFiles/audio/${filename}.${ext}"
	radamsa -o ${outputFN} -n 100 -r ${inputFN} -m ft=2
done
