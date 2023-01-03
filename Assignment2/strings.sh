string1="Hello I'm harshita"

length=`expr length "$string1"`
echo "The length of the string is $length"

string1="Hello"

# Concatenate

string1="Hello"
string2="World"

result="$string1 $string2"
echo "$result"



# Convert the string to lowercase
lowercase=$(echo "$string1" | tr '[:upper:]' '[:lower:]')
echo "$lowercase"

# Uppercase
uppercase=$(echo "$string1" | tr '[:lower:]' '[:upper:]')
echo "$uppercase"

#Slicing

length=${#string1}

# Set the start index and length of the slice
start=2
length=4

sliced=${string1:start:length}
echo "$sliced"


