a=$(shuf -i 0-50 -n1)
echo $a
n=1
while [ $n -le 5 ]
do 
	echo "Guess The No.:"
	read ans
		if [ $ans = $a ]
		then
			GUESS=$n
			case $GUESS in
				'1') echo "You won 1st prize"
				;;
				'2') echo "You won 2nd prize"
				;;
				'3') echo "You won 3rd prize"
				;;
				'4') echo "You won 4th prize"
				;;
				'5') echo "You won 5th prize"
				;;
			esac
			break
		else
			echo "Try Again..."
		fi
	((n=n+1))
	if [ $n = 6 ]
	then
		echo "Better Luck Next Time :( "
	fi
done