a=$(shuf -i 0-10 -n1)

n=1

while [ $n -le 5]
do 
	echo "Enter Your Guess"
	read guess

	if [$n == $guess ]
	then
		chance = $n

		case $chance in
			"1") echo "You Won"
				;;
			"2") echo "You Lare 2nd"
				;;
			"3") echo "You are 3rd"
				;;
			"4") echo "You are 4th"
				;;
			"5") echo "You are 5th"
				;;
			
		esac
	else
		echo "Try again"

	((n=n+1))

	if [ $n == 6 ]
	then 
		echo "Better Luck Next Time"
	fi 
done
