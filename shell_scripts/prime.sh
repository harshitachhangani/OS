#!/bin/bash

# Take input from user
echo "Enter a number: "
read num

# Check if number is prime
is_prime=1
for (( i=2; i<=$num/2; i++ ))
do
    if [ $(( $num % $i )) -eq 0 ]
    then
        is_prime=0
        break
    fi
done

if [ $num -eq 1 ]
then
    echo "1 is neither prime nor composite"
elif [ $is_prime -eq 1 ]
then
    echo "$num is a prime number"
else
    echo "$num is not a prime number"
fi

# Reverse the number
reverse=0
while [ $num -ne 0 ]
do
    remainder=$(( $num % 10 ))
    reverse=$(( $reverse * 10 + $remainder ))
    num=$(( $num / 10 ))
done
echo "Reverse of the number is $reverse"
