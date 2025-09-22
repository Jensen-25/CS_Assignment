import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("istherecorrelation.csv")

plt.figure(dpi=300)
plt.plot(df["X"], df["Y"], "o-")
plt.xlabel("X variable")
plt.ylabel("Y variable")
plt.title("Correlation Plot")
plt.savefig("correlation_plot.png", dpi=300)
plt.show()
