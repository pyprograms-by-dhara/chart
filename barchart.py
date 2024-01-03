import matplotlib.pyplot as plt
import numpy as np

x=np.array(['C','C++','Java','Python','PHP'])
y=np.array([23,18,35,28,11])

plt.bar(x,y,color='purple',width=0.5)
plt.show()
