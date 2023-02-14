#install pycirclize
import matplotlib.pyplot as plt
from stackedwaterfalls import StackedWaterfalls as sw

aircomp  =  [[0.74] , [0.16], [0.05, 0.05]]
names = [['N$_2$'], ['O$_2$'], ['AR','H$_2$O']] # Labels of input values

air = sw(aircomp, names)
air.plot()
plt.show()


names = [['A'], ['B', 'C', 'D'], ['E', 'F']]  # Labels of input values
data_set1 = [[0.3], [0.2, 0.0, 0.0], [0.0, 0.030]]
data_set2 = [[0.3], [0.3, 0.0, 0.0], [0.0, 0.030]]
data_set3 = [[0.6], [1e-16, 0.8, 0.1],
             [0.01, 1e-16]]  # need to set 0's here to very small num that is not zero to force legend elements
colors = [['deepskyblue'], ['royalblue', 'silver', 'darkorange'], ['brown', 'grey']]

d1 = sw(data_set1, names, colors)
d2 = sw(data_set2, names, colors)
d3 = sw(data_set3, names, colors)

ax, xst2 = d1.plot(shadecolor='cornflowerblue',
                   legend=False, linkskw={'lw': '2', 'color': 'red', 'alpha': 0.1}, total=True,
                   grouplabel="Set 1", barnames=["One", "Two", "Three"], grouplabelstyle=']')

ax, xst3 = d2.plot(shadecolor='yellow', ax=ax, xstart=xst2 + 0.4, total=True, grouplabel="Set 2",
                   grouplabelstyle="|-",
                   legend=False)
ax, xst4 = d3.plot(shadecolor='red', ax=ax, xstart=xst3 + 0.4, total=True, grouplabel="Set 3",
                   grouplabelstyle="|",
                   legend=True, legkw={'ncol': 3, 'framealpha': 1.0, 'loc': 'best', 'fontsize': 15})

ax.grid()
ax.set_ylim(0, 1.8)
plt.tight_layout()

plt.show()
