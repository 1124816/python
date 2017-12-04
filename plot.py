import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Make some fake data.
#a = b = np.arange(0, 3, .02)
#c = np.exp(a)
#d = c[::-1]

def f(x):
    return((100.*1.2**x)*7.)/1000

def p(x):
    return integrate.quad(f, 0, x)[0]

t = np.arange(0., 20.5, 0.5)
# Create plots with pre-defined labels.
#fig, ax = plt.subplots()
plt.plot(t, f(t), label='Monthly Earnings')
plt.plot(t, [p(i) for i in t], label='All Earnings')
plt.plot(t, [62.796]*len(t), t, [5.233]*len(t), label='Break even point')
#ax.plot(a, d, 'k:', label='Data length')
#ax.plot(a, c + d, 'k', label='Total message length')
plt.axis([0, 20, 0, 100])
legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')

plt.xlabel('Months')
plt.ylabel('Thousands of Dollars')
plt.title('How we be rich')
plt.grid(True)

# Put a nicer background color on the legend.
#legend.get_frame().set_facecolor('#00FFCC')
#print([p(i) for i in t])
plt.show()
