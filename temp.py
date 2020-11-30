#!/usr/bin/python3

from gpiozero import CPUTemperature
cpu_temp = CPUTemperature()
print (cpu_temp.temperature)

'''
#%%
from subprocess import PIPE, Popen
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from gpiozero import CPUTemperature

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
cpu = CPUTemperature()
# Initialize communication with TMP102
def get_cpu_temperature():
    """get cpu temperature using vcgencmd"""
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    output = output.decode("utf-8")
    return float(output[output.rindex('=') + 1:output.rindex("'")])

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    temp_c = cpu.temperature
    print (temp_c)
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('CPU Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
# %%
'''