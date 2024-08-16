from gpiozero import LED
from time import sleep
import psutil

# leds = {
#     "green" : LED(14),
#     "yellow" : LED(15),
#     "red" : LED(18)
# }

cpu_data_file = open("cpu_data_file.txt","a")

try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=5, percpu = True)
        cpu_usage_mean = round(sum(cpu_usage) / len(cpu_usage) ,3)
        print(f"cpu usage persenage: {cpu_usage_mean}%")
        if (80 > cpu_usage_mean >= 50):
            # leds["yellow"].on()
            # leds["green"].off()
            # leds["red"].off()
            print("yellow")
        elif (cpu_usage_mean >= 80):
            # leds["red"].on()
            # leds["green"].off()
            # leds["yellow"].off()
            print("red")
        else:
            # leds["green"].on()
            # leds["yellow"].off()
            # leds["red"].off()
            print("green")
        data = f"cpu usage persentage: {cpu_usage_mean}% \n"
        cpu_data_file.write(data)

except KeyboardInterrupt:
    print("\nScript interrupted. Exiting...")