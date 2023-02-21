#!/bin/bash

# initialize array of numbers
numbers=(10 2 8 4 6 5)

# print original array
echo "Original array: ${numbers[@]}"

# get length of array
n=${#numbers[@]}

# perform bubble sort
for (( i=0; i<$n-1; i++ ))
do
    for (( j=0; j<$n-$i-1; j++ ))
    do
        if [ ${numbers[$j]} -gt ${numbers[$j+1]} ]
        then
            # swap numbers
            temp=${numbers[$j]}
            numbers[$j]=${numbers[$j+1]}
            numbers[$j+1]=$temp
        fi
    done
done

# print sorted array
echo "Sorted array: ${numbers[@]}"
