import pandas as pd
import matplotlib.pyplot as plt

# Given constants (configurable)
n = 20000  # Number of steps
epsilon = 0.001 # Time step (s)
v = 1  # m/s
F = 2  # N
m = 5  # kg
a = F / m  # Acceleration magnitude (a)
R = v**2 / a  # Radius is calculated based on v^2/a
x0 = R  # m
y0 = 0  # m

# Initial conditions
t = 0
x = x0
y = y0
vx = 0
vy = v
ax = -1*a
ay = 0

# Dictionary to store the initial values (at t=0)
current_state = {
    't': t,
    'x': x,
    'vx': vx,
    'ax': ax,
    'y': y,
    'vy': vy,
    'ay': ay,
    't+epsilon/2': t + epsilon / 2,
    'vx(t+epsilon/2)': vx + ax * epsilon / 2,
    'vy(t+epsilon/2)': vy + ay * epsilon / 2
}

# List to store each state
rows = [current_state]

# Iteration loop for n steps
for _ in range(1, n):
    # Update time
    t += epsilon

    # Update positions using half-step velocities from the previous state
    x += current_state['vx(t+epsilon/2)'] * epsilon
    y += current_state['vy(t+epsilon/2)'] * epsilon

    # Update velocities using half-step velocities from the previous state
    vx = current_state['vx(t+epsilon/2)']
    vy = current_state['vy(t+epsilon/2)']

    # Update accelerations based on new positions
    ax = -x * a / R
    ay = -y * a / R

    # Calculate half-step velocities for the next iteration
    vx_half_step = vx + ax * epsilon
    vy_half_step = vy + ay * epsilon

    # Update the current state
    current_state = {
        't': t,
        'x': x,
        'vx': vx,
        'ax': ax,
        'y': y,
        'vy': vy,
        'ay': ay,
        't+epsilon/2': t + epsilon / 2,
        'vx(t+epsilon/2)': vx_half_step,
        'vy(t+epsilon/2)': vy_half_step
    }

    # Add current state to the list
    rows.append(current_state)

# Convert list of dictionaries to DataFrame
df_updated = pd.DataFrame(rows)

# Print the first 5 rows of the updated DataFrame
print(df_updated.head())

# Create a scatter plot of x and y columns
plt.figure(figsize=(10, 10))
plt.scatter(df_updated['x'], df_updated['y'], s=1)  # s is the size of the points

# Set the range of x and y axes
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# Draw major axes through x=0 and y=0
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Add grid, labels and title
plt.grid(True)
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Scatter Plot of Object Position in Circular Motion')

# Show the plot
plt.show()