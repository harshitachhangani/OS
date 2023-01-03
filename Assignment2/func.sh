a=0

add(){
sum=0
i=1
len=$#
x=$((len + 1))
while [ $i -lt $x ]
do
    arg=${!i}
    sum=$((sum + arg))
    i=$((i + 1 ))
done
a=$sum
}

add 5 4 9 1
echo $a