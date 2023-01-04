word=$1

reversed=$(echo $word | rev)

if [ $word == $reversed ]; then
    echo "$word is palindrome"
else
    echo "$word is not a palindrome"
fi