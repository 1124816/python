import numpy as np
import matplotlib.text as text
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

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.plot(t, f(t), label='Monthly Earnings')
axes.plot(t, [p(i) for i in t], label='All Earnings')
axes.plot(t, [5.233]*len(t), label='Monthly Break even point')
axes.axis([0, 20, 0, 80])
legend = axes.legend(loc='upper left', fontsize='x-large')
axes.set_facecolor('#795548')
fig.set_facecolor('#795548')
plt.xlabel('Months')
plt.ylabel('Dollars (in thousands)')
axes.set_title('Income', color='#FFFFFF')
axes.grid(True)
plt.setp(legend.get_texts(), color='#FFFFFF')
axes.spines['bottom'].set_color('#FFFFFF')
axes.spines['top'].set_color('#FFFFFF')
axes.spines['left'].set_color('#FFFFFF')
axes.spines['right'].set_color('#FFFFFF')
axes.xaxis.label.set_color('#FFFFFF')
axes.tick_params(axis='x', colors='#FFFFFF')
axes.yaxis.label.set_color('#FFFFFF')
axes.tick_params(axis='y', colors='#FFFFFF')
# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#695548')
#print([p(i) for i in t])
fig.tight_layout()
#plt.show()
fig.savefig('foo.png', facecolor=fig.get_facecolor(), edgecolor=fig.get_facecolor())
