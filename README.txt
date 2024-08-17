*** The LEDS are commented till it will be tested with the Raspberry Pi till then use the (green,yellow,red) output as an indecation that the code works ***

DISCRIPTION:
A Python script that covers the following points:
- Reads total CPU usage.
- Appends the usage to a log file with a timestamp every 5 seconds.
- Lights a green LED when the percentage is less than 50%, lights a yellow LED when the percentage is less than 80%, and finally lights a red LED when the percentage is above or equal to 80%.

Deadline: (Saturday) by 11:59 PM

Note: When trying to run the code, comment out the LED code lines as the gpiozero library will only work on a Raspberry Pi. We will test the code on Sunday.
