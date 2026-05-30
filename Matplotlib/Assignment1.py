import numpy as np
import matplotlib.pyplot as plt
# Rows: Kohli, Rohit, Sehwag
# Columns: Year 1 to Year 10

runs = np.array([
    [890, 1020, 950, 1100, 980, 1200, 1150, 1080, 1250, 1190],  # Kohli
    [760, 850, 920, 880, 970, 1050, 990, 1120, 1080, 1150],      # Rohit
    [980, 1040, 910, 860, 990, 870, 920, 800, 950, 890]          # Sehwag
])

players = ["Kohli", "Rohit", "Sehwag"]
virat = np.array([890, 1020, 950, 1100, 980, 1200, 1150, 1080, 1250, 1190])
rohit = np.array([760, 850, 920, 880, 970, 1050, 990, 1120, 1080, 1150])
sehwag = np.array([980, 1040, 910, 860, 990, 870, 920, 800, 950, 890])

years = np.linspace(1990,2010,10)

plt.style.use("ggplot")
plt.plot(years, virat, color="blue", linestyle='--', marker='o', label="Virat")
plt.plot(years, rohit, color="red", linestyle='-', marker="*", label="Rohit")
plt.plot(years, sehwag, color="orange", linestyle=':', marker="x", label="Rohit")
plt.grid()
plt.legend()
plt.title("Epic Battle of the Batsmen")
plt.show()




