#/bin/bash

## RUN MAIN PROGRAM ##

./bin/python3.9 ./src/main.py
OUTPUT_VARIABLE=$?

case $OUTPUT_VARIABLE in


## poweroff
23)
echo "powering down..."
for i in {0..3}
do
echo $i
sleep 1
done
;;

## reboot
24)
echo "rebooting..."
;;

## update
25)
echo "updating..."
;;

## program closed properly
0)
echo "Program closed properly"
for i in {5..1}
do
echo  -ne $i \\r
sleep 1

done



;;

esac
