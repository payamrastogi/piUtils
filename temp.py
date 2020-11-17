#!/usr/bin/python
from subprocess import PIPE, Popen
from gpiozero import CPUTemperature
from time import sleep, strftime, time
#import matplotlib.pyplot as plt
#plt.switch_backend('TkAgg')
#plt.ion()
#x = []
#y = []

def get_cpu_temperature():
    """get cpu temperature using vcgencmd"""
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    output = output.decode("utf-8")
    return float(output[output.rindex('=') + 1:output.rindex("'")])

#print(get_cpu_temperature())
cpu = CPUTemperature()
# with open("/home/pi/workspace/piUtils/cpu_temp.csv", "a") as log:
#     while True:
#         temp = cpu.temperature
#         #y.append(temp)
#         #x.append(time())
#         #plt.clf()
#         #plt.scatter(x,y)
#         #plt.plot(x,y)
#         log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
#         sleep(1)
#         #plt.pause(1)
#         #plt.draw()
print(cpu.temperature)