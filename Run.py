from matplotlib import pyplot as plt
import math

# Approximates an ODE using Euler's method
# f: A lambda in terms of (t, y)
# num_steps: The amount of points that will be approximated
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# return: An array of 2 arrays: time and output
def Euler(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1):
    # The amount to step in the t direction for every next approximation
    step = (t_end - t_init) / float(num_steps)

    # Arrays for the output: [time, output]
    output = [[], []]

    # Initial values for t and each different y
    t = t_init
    y = y_init

    # Calculate each step of the approximation
    for i in range(num_steps):
        # Populate arrays with next t value and each next y value
        output[0].append(t)
        output[1].append(y)

        # Calculate each new y, then increment t
        y += step * f(t, y)
        t += step
        return output

# Approximates a system of two ODEs using Euler's method
# f: A lambda in terms of (t, y)
# num_steps: The amount of points that will be approximated
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# return: An array of 2 arrays: time and output
def EulerSystem(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1, v_init = 1):
    # The amount to step in the t direction for every next approximation
    step = (t_end - t_init) / float(num_steps)

    # Arrays for the output: [time, output]
    output = [[], [], []]

    # Initial values for t and each different y
    t = t_init
    y = y_init
    v = v_init

    # Calculate each step of the approximation
    for i in range(num_steps):
        # Populate arrays with next t value and each next y value
        output[0].append(t)
        output[1].append(y)
        output[2].append(v)

        # Calculate each new y, then increment t
        y += step * f[0](t, y, v)
        v += step * f[1](t, y, v)
        t += step

    return output

# Approximates an ODE using the Midpoint method
# f: A lambda in terms of (t, y)
# num_steps: The amount of points that will be approximated
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# return: An array of 2 arrays: time and output
def Midpoint(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1):
    # The amount to step in the t direction for every next approximation
    step = (t_end - t_init) / float(num_steps)

    # Midpoint of each step
    half_step = float(step) / 2

    # Arrays for the output: [time, Euler, Midpoint, Trapezoid, RK]
    output = [[], []]

    # Initial values for t and each different y
    t = t_init
    y = y_init

    # Calculate each step of the approximation
    for i in range(num_steps):
        # Populate arrays with next t value and each next y value
        output[0].append(t)
        output[1].append(y)

        # Partial calculations
        k1 = f(t, y)

        # Calculate each new y, then increment t
        y = y + (step * f(t + half_step, y + (half_step * k1)))
        t += step

    return output

# Approximates a system of two ODEs using the Midpoint method
# f: A lambda in terms of (t, y)
# num_steps: The amount of points that will be approximated
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# return: An array of 2 arrays: time and output
def MidpointSystem(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1, v_init = 1):
    # The amount to step in the t direction for every next approximation
    step = (t_end - t_init) / float(num_steps)

    # Midpoint of each step
    half_step = float(step) / 2

    # Arrays for the output: [time, output]
    output = [[], [], []]

    # Initial values for t and each different y
    t = t_init
    y = y_init
    v = v_init

    # Calculate each step of the approximation
    for i in range(num_steps):
        # Populate arrays with next t value and each next y value
        output[0].append(t)
        output[1].append(y)
        output[2].append(v)

        # Partial calculations
        k1a = f[0](t, y, v)
        k1b = f[1](t, y, v)

        # Calculate each new y, then increment t
        y += step * f[0](t + half_step, y + (half_step * k1a), v + (half_step * k1a))
        v += step * f[1](t + half_step, y + (half_step * k1b), v + (half_step * k1b))
        t += step

    return output

# Approximates an ODE using the Trapezoid method
# f: A lambda in terms of (t, y)
# num_steps: The amount of points that will be approximated
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# return: An array of 2 arrays: time and output
def Trapezoid(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1):
    # The amount to step in the t direction for every next approximation
    step = (t_end - t_init) / float(num_steps)

    # Midpoint of each step
    half_step = float(step) / 2

    # Arrays for the output: [time, Euler, Midpoint, Trapezoid, RK]
    output = [[], []]

    # Initial values for t and each different y
    t = t_init
    y = y_init

    # Calculate each step of the approximation
    for i in range(num_steps):
        # Populate arrays with next t value and each next y value
        output[0].append(t)
        output[1].append(y)

        # Partial calculations
        k1 = f(t, y)
        k2 = f(t + step, y + (step * k1))

        # Calculate each new y, then increment t
        y = y + (half_step * (k1 + k2))
        t += step

    return output

# Approximates a system of two ODEs using the Trapezoid method
# f: A lambda in terms of (t, y)
# num_steps: The amount of points that will be approximated
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# return: An array of 2 arrays: time and output
def TrapezoidSystem(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1, v_init = 1):
    # The amount to step in the t direction for every next approximation
    step = (t_end - t_init) / float(num_steps)

    # Midpoint of each step
    half_step = float(step) / 2

    # Arrays for the output: [time, output]
    output = [[], [], []]

    # Initial values for t and each different y
    t = t_init
    y = y_init
    v = v_init

    # Calculate each step of the approximation
    for i in range(num_steps):
        # Populate arrays with next t value and each next y value
        output[0].append(t)
        output[1].append(y)
        output[2].append(v)

        # Partial calculations
        k1a = f[0](t, y, v)
        k1b = f[1](t, y, v)
        k2a = f[0](t + step, y + (step * k1a), v + (step * k1a))
        k2b = f[1](t + step, y + (step * k1b), v + (step * k1b))


        # Calculate each new y, then increment t
        y = y + (half_step * (k1a + k2a))
        v = v + (half_step * (k1b + k2b))
        t += step

    return output

# Approximates an ODE using the Runge-Kuta method
# f: A lambda in terms of (t, y)
# num_steps: The amount of points that will be approximated
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# return: An array of 2 arrays: time and output
def RungeKuta(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1):
    # The amount to step in the t direction for every next approximation
    step = (t_end - t_init) / float(num_steps)

    # Partial step precalculations
    half_step = float(step) / 2
    sixth_step = float(step) / 6

    # Arrays for the output: [time, Euler, Midpoint, Trapezoid, RK]
    output = [[], []]

    # Initial values for t and each different y
    t = t_init
    y = y_init

    # Calculate each step of the approximation
    for i in range(num_steps):
        # Populate arrays with next t value and each next y value
        output[0].append(t)
        output[1].append(y)

        # Partial calculations
        k1 = f(t, y)
        k2 = f(t + half_step, y + (half_step * k1))
        k3 = f(t + half_step, y + (half_step * k2))
        k4 = f(t + step, y + (step * k3))


        # Calculate each new y, then increment t
        y = y + (sixth_step * (k1 + (2 * k2) + (2 * k3) + k4))
        t += step

    return output

# Approximates a system of two ODEs using the Runge-Kuta method
# f: A lambda in terms of (t, y)
# num_steps: The amount of points that will be approximated
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# return: An array of 2 arrays: time and output
def RungeKutaSystem(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1, v_init = 1):
    # The amount to step in the t direction for every next approximation
    step = (t_end - t_init) / float(num_steps)

    # Partial step precalculations
    half_step = float(step) / 2
    sixth_step = float(step) / 6

    # Arrays for the output: [time, output]
    output = [[], [], []]

    # Initial values for t and each different y
    t = t_init
    y = y_init
    v = v_init

    # Calculate each step of the approximation
    for i in range(num_steps):
        # Populate arrays with next t value and each next y value
        output[0].append(t)
        output[1].append(y)
        output[2].append(v)

        # Partial calculations
        k1a = f[0](t, y, v)
        k1b = f[1](t, y, v)
        k2a = f[0](t + half_step, y + (half_step * k1a), v + (half_step * k1a))
        k2b = f[1](t + half_step, y + (half_step * k1b), v + (half_step * k1b))
        k3a = f[0](t + half_step, y + (half_step * k2a), v + (half_step * k2a))
        k3b = f[1](t + half_step, y + (half_step * k2b), v + (half_step * k2b))
        k4a = f[0](t + step, y + (step * k3a), v + (step * k3a))
        k4b = f[1](t + step, y + (step * k3b), v + (step * k3b))


        # Calculate each new y, then increment t
        y = y + (sixth_step * (k1a + (2 * k2a) + (2 * k3a) + k4a))
        v = v + (sixth_step * (k1b + (2 * k2b) + (2 * k3b) + k4b))
        t += step

    return output

# Plots a 1st order ODE using four different approximation methods
# function: A lambda in terms of (t, y)
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
def Plot1stOrder(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1):
    # Populate arrays of points with approximations of the 1st order ODE
    euler = Euler(f, num_steps, t_init, t_end, y_init)
    midpt = Midpoint(f, num_steps, t_init, t_end, y_init)
    trap  = Trapezoid(f, num_steps, t_init, t_end, y_init)
    rk    = RungeKuta(f, num_steps, t_init, t_end, y_init)

    # Plot the 1st order ODE against time
    plt.plot(euler[0], euler[1])
    plt.plot(midpt[0], midpt[1])
    plt.plot(trap[0], trap[1])
    plt.plot(rk[0], rk[1])

    # Labels
    plt.legend(["Euler", "Midpoint", "Trapezoid", "Runge-Kuta"])
    plt.xlabel("Independent Variable: t")
    plt.ylabel("Dependent Variable: y")

    # Display the plot
    plt.show()

# Plots a 2st order ODE using four different approximation methods
# function: A lambda in terms of (t, y)
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# v_init: The initial value of y'
def Plot2ndOrder(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1, v_init = 1):
    # Populate arrays of points with approximations of the 2nd order ODE
    euler = EulerSystem(f, num_steps, t_init, t_end, y_init, v_init)
    midpt = MidpointSystem(f, num_steps, t_init, t_end, y_init)
    trap  = TrapezoidSystem(f, num_steps, t_init, t_end, y_init)
    rk    = RungeKutaSystem(f, num_steps, t_init, t_end, y_init)

    # Plot the approximations of the 2nd order ODE
    plt.plot(euler[0], euler[1])
    plt.plot(midpt[0], midpt[1])
    plt.plot(trap[0], trap[1])
    plt.plot(rk[0], rk[1])

    # Labels
    plt.legend(["Euler", "Midpoint", "Trapezoid", "Runge-Kuta"])
    plt.xlabel("Independent Variable: t")
    plt.ylabel("Dependent Variable: y")

    # Display the plot
    plt.show()

# Plots a system of 2 ODEs' phase plane using four different approximation methods
# function: A lambda in terms of (t, y)
# t_init: Initial value of the time variable
# t_end: The final value of the time variable
# y_init: The initial value of the dependent variable
# v_init: The initial value of y'
def PlotSystem(f, num_steps = 10000, t_init = 0, t_end = 100, y_init = 1, v_init = 1):
    # Populate arrays of points with approximations of the system of ODEs
    euler = EulerSystem(f, num_steps, t_init, t_end, y_init, v_init)
    midpt = MidpointSystem(f, num_steps, t_init, t_end, y_init)
    trap  = TrapezoidSystem(f, num_steps, t_init, t_end, y_init)
    rk    = RungeKutaSystem(f, num_steps, t_init, t_end, y_init)

    # Plot the approximations of the phase space of the system of ODEs
    plt.plot(euler[1], euler[2])
    plt.plot(midpt[1], midpt[2])
    plt.plot(trap[1], trap[2])
    plt.plot(rk[1], rk[2])

    # Labels
    plt.legend(["Euler", "Midpoint", "Trapezoid", "Runge-Kuta"])
    plt.xlabel("Independent Variable: y")
    plt.ylabel("Dependent Variable: y'")

    # Display the plot
    plt.show()

# Run the program
Plot1stOrder(lambda x, y: math.cos(x) + math.sin(y))
Plot2ndOrder([lambda t, y, v : math.sin(t) + math.cos(y) + v, lambda t, y, v: math.cos(v)])
PlotSystem([lambda t, y, v : math.sin(t) + math.cos(y), lambda t, y, v: math.sin(v)], 100, 0, 10)