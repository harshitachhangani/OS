# Write script which will print greetings based on time

hour=$(date +%H)

if [ $hour -ge 0 -a $hour -lt 12 ]; then
    greeting="Good
