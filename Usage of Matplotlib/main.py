import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mu=100
sigma=15
x=mu+sigma*np.random.randn(10000)
y=mu+30*np.random.randn(10000)
plt.hist([x,y], bins=100, histtype='barstacked')
plt.show()