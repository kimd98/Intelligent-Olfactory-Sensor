import time
import board
import busio
import adafruit_sgp30
import datetime as dt
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

matplotlib.use('tkagg')

# Create library object on I2C port
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
print("SGP30 serial #", [hex(i) for i in sgp30.serial])

# Initialize communication with SGP30
sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

# Count time for test function
elapsed_sec = 0

# Parameters
x_len = 300         # Number of points to display
y1_range = [0, 60000]  # Range of possible Y values to display
y2_range = [400, 60000]
y3_range = [0, 20000]
y4_range = [0, 20000]

# Create figure for plotting
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
xs = list(range(0, 300))

y1s = [0] * x_len
y2s = [400] * x_len
y3s = [0] * x_len
y4s = [0] * x_len

ax1.set_ylim(y1_range)
ax2.set_ylim(y2_range)
ax3.set_ylim(y3_range)
ax4.set_ylim(y4_range)

# Create a blank line. We will update the line in animate
line1, = ax1.plot(xs, y1s)
line2, = ax2.plot(xs, y2s)
line3, = ax3.plot(xs, y3s)
line4, = ax4.plot(xs, y4s)

# Add labels
ax1.set_title('SGP30 TVOC over Time')
ax1.set_ylabel('TVOC (ppb)')
ax1.set_xlabel('Sample')
ax2.set_title('SGP30 eCO2 over Time')
ax2.set_ylabel('eCO2 (ppm)')
ax2.set_xlabel('Sample')
ax3.set_title('SGP30 Ethanol over Time')
ax3.set_ylabel('Ethanol (ppm)')
ax3.set_xlabel('Sample')
ax4.set_title('SGP30 H2 over Time')
ax4.set_ylabel('H2 (ppm)')
ax4.set_xlabel('Sample')

def test():
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    print("H2 = %d \t Ethanol = %d" % (sgp30.H2, sgp30.Ethanol))
    time.sleep(1)
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print(
            "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
            % (sgp30.baseline_eCO2, sgp30.baseline_TVOC)
        )

# This function is called periodically from FuncAnimation
def animate(i, y1s, y2s, y3s, y4s):

    # Read data from SGP30
    tvoc = sgp30.TVOC
    eco2 = sgp30.eCO2
    h2 = sgp30.H2
    ethanol = sgp30.Ethanol

    # Add y to list
    y1s.append(tvoc)
    y2s.append(eco2)
    y3s.append(ethanol)
    y4s.append(h2)

    # Limit y list to set number of items
    y1s = y1s[-x_len:]
    y2s = y2s[-x_len:]
    y3s = y3s[-x_len:]
    y4s = y4s[-x_len:]

    # Update line with new Y values
    line1.set_ydata(y1s)
    line2.set_ydata(y2s)
    line3.set_ydata(y3s)
    line4.set_ydata(y4s)

   # Show the latest data
   # text_TVOC = ax1.text(0.1, 0.9, 'TVOC: ' + str(sgp30.TVOC) + ' ppm', horizontalalignment='center',
   #     verticalalignment='center', transform=ax1.transAxes)
   # text_eCO2 = ax2.text(0.1, 0.9, 'eCO2: ' + str(sgp30.eCO2) + ' ppb', horizontalalignment='center',
   #     verticalalignment='center', transform=ax2.transAxes)

    return line1,line2,line3,line4,


while True:
    # test()
    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig,
        animate,
        fargs=(y1s, y2s, y3s, y4s),
        interval=50,
        blit=True)

    plt.subplots_adjust(hspace=0.6)
    plt.show()
