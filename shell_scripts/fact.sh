#!/bin/bash

# function to find factorial using recursive method
function factorial_recursive {
    if [ $1 -eq 0 ]
    then
        echo 1
    else
        local result=$(($1 * $(factorial_recursive $(($1 - 1)))))
        echo $result
    fi
}

# function to find factorial using non-recursive method
function factorial_non_recursive {
    local result=1
    for (( i=1; i<=$1; i++ ))
    do
        result=$(($result * $i))
    done
    echo $result
}

# take input from user
echo "Enter a number: "
read num

# find factorial using recursive method
result_recursive=$(factorial_recursive $num)
echo "Factorial of $num using recursive method: $result_recursive"

# find factorial using non-recursive method
result_non_recursive=$(factorial_non_recursive $num)
echo "Factorial of $num using non-recursive method: $result_non_recursive"
