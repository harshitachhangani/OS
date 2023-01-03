# Read the lower and upper limits from the user
echo -n "Enter lower limit: "
read lower
echo -n "Enter upper limit: "
read upper

# Print all the prime numbers between the lower and upper limits
for i in $(seq $lower $upper); do
  # Check if the number is prime
  is_prime=1
  for j in $(seq 2 $((i-1))); do
    if [ $((i%j)) -eq 0 ]; then
      is_prime=0
      break
    fi
  done
  if [ $is_prime -eq 1 ]; then
    echo "$i"
  fi
done
