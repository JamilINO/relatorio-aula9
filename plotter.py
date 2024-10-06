import matplotlib.pyplot as plotlib
import numpy


figura, ax = plotlib.subplots()

ax.plot([1,2], [3,4])


ax.set_title("Meu Titulo legal")
plotlib.savefig("outputs/figura.png")
plotlib.show()
