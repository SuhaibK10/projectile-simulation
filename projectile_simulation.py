import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


g = 9.8  


st.title("Projectile Motion Simulation")


v0 = st.slider("Initial Velocity (m/s)", 0, 100, 30)  # Initial velocity slider
angle = st.slider("Launch Angle (degrees)", 0, 90, 45)  # Launch angle slider


theta = np.radians(angle)


t_flight = 2 * v0 * np.sin(theta) / g


t_values = np.linspace(0, t_flight, num=500)


x_values = v0 * np.cos(theta) * t_values
y_values = v0 * np.sin(theta) * t_values - 0.5 * g * t_values**2

fig, ax = plt.subplots()
ax.plot(x_values, y_values)


ax.set_xlabel("Distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title(f"Projectile Motion (v0={v0} m/s, angle={angle}°)")

# Display the plot
st.pyplot(fig)

# Display additional information
st.write(f"Time of flight: {t_flight:.2f} seconds")
st.write(f"Maximum height: {max(y_values):.2f} meters")
st.write(f"Maximum range: {x_values[-1]:.2f} meters")
