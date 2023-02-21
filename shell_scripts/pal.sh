#!/bin/bash

echo "Enter a number:"
read num

reverse=$(echo $num | rev)

if [ $num -eq $reverse ]; then
  echo "$num is a palindrome."
else
  echo "$num is not a palindrome."
fi

echo "The reverse of $num is: $reverse"