from matplotlib import pyplot as plt
import math

main3 = []
for line in open("outN3.txt", 'r'):
    if line[0:2] == 'vt':
        main3.append(float(line.split()[2]))

Vsb = [0, 1, 2, 3, 4]
print(main3)
gamma = (main3[-1] - main3[0])/(math.sqrt(Vsb[-1] + 0.6) - math.sqrt(0.6))
print(gamma)

plt.figure()
plt.plot(Vsb, main3, '*-')
plt.xlabel("V_SB")
plt.ylabel("V_T")
plt.title("Threshold Voltage vs V_SB")
plt.show()

main4 = []
for line in open("outC4.txt", 'r'):
    if line[0:2] == 'tp':
        main4.append(float(line.split()[2]))

Vdd = [2, 2.2, 2.4, 2.6, 2.8, 3, 3.3]
print(main4)

plt.figure()
plt.plot(Vdd, main4, '*-')
plt.xlabel("V_DD")
plt.ylabel("T_P")
plt.title("Propogation Delay vs Supply Voltage")
plt.show()