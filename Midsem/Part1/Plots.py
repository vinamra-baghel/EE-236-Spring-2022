from matplotlib import pyplot as plt

main = []
for line in open("Values.txt", 'r'):
    if line == '\n':
        continue
    nline = line.split()
    main.append(float(nline[0]))

temp = [20, 30, 40, 50, 60, 70, 80]

tcoeff1 = (main[4]-main[3])/(temp[4]-temp[3])
tcoeff2 = (main[11]-main[10])/(temp[4]-temp[3])
print("PN-Diode: " + str(tcoeff1) + "; Zener Diode: " + str(tcoeff2))

plt.figure()
plt.plot(temp, main[:7], '*-')
plt.xlabel("Temperature")
plt.ylabel("Voltage for 2mA Current")
plt.title("Q1 Voltage vs Temperature for PN-Diode")
plt.show()

plt.figure()
plt.plot(temp, main[7:], '*-')
plt.xlabel("Temperature")
plt.ylabel("Voltage for -0.5mA Current")
plt.title("Q1 Voltage vs Temperature for Zener Diode")
plt.show()