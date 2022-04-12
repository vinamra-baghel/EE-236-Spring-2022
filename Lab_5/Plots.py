from matplotlib import pyplot as plt
import math

main = []
for line in open("Values.txt", 'r'):
    main.append(float(line))

Vsb = [0, -1, -2, -3, -4]
gamma = (main[-1] - main[0])/(math.sqrt(-Vsb[-1] + 0.8) - math.sqrt(0.8))
print(gamma)

plt.figure()
plt.plot(Vsb, main, '*-')
plt.xlabel("V_SB")
plt.ylabel("V_T")
plt.title("Threshold Voltage vs V_SB")
plt.show()