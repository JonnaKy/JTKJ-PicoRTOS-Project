import matplotlib.pyplot as plt
import numpy as np

# Data
timestamps = np.arange(1, 11)  # Assuming each data point corresponds to a different timestamp

# Acceleration data (X, Y, Z)
acceleration_x = [-0.013062, -0.013184, -0.013184, -0.012817, -0.012207, -0.013428, -0.012695, -0.014038, -0.013184, -0.013184]
acceleration_y = [-0.066284, -0.066528, -0.066040, -0.066406, -0.065186, -0.065796, -0.066406, -0.066162, -0.065796, -0.065796]
acceleration_z = [1.014160, 1.013428, 1.011963, 1.012085, 1.012329, 1.011963, 1.012329, 1.012329, 1.013062, 1.012573]

# Angular velocity data (X, Y, Z)
angular_velocity_x = [-0.549618, -0.488550, -0.503817, -0.580153, -0.442748, -0.595420, -0.534351, -0.458015, -0.488550, -0.488550]
angular_velocity_y = [-0.076336, -0.061069, -0.152672, -0.137405, -0.167939, -0.061069, -0.152672, -0.091603, -0.030534, -0.030534]
angular_velocity_z = [-0.381679, -0.366412, -0.458015, -0.366412, -0.427481, -0.381679, -0.412214, -0.351145, -0.381679, -0.381679]

# Plotting
plt.figure(figsize=(12, 8))

# Plot Acceleration (X, Y, Z)
plt.subplot(2, 1, 1)
plt.plot(timestamps, acceleration_x, label='Accel X', color='r', marker='o')
plt.plot(timestamps, acceleration_y, label='Accel Y', color='g', marker='o')
plt.plot(timestamps, acceleration_z, label='Accel Z', color='b', marker='o')
plt.title("Acceleration (m/s²) vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.legend()

# Plot Angular Velocity (X, Y, Z)
plt.subplot(2, 1, 2)
plt.plot(timestamps, angular_velocity_x, label='Ang Vel X', color='r', marker='o')
plt.plot(timestamps, angular_velocity_y, label='Ang Vel Y', color='g', marker='o')
plt.plot(timestamps, angular_velocity_z, label='Ang Vel Z', color='b', marker='o')
plt.title("Angular Velocity (degrees/s) vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (degrees/s)")
plt.legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
