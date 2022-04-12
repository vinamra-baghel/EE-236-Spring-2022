from matplotlib import pyplot as plt

main = []
for line in open("Values.txt", 'r'):
    if line == '\n' or line[0] == '-':
        continue
    nline = line.split()
    main.append(float(nline[2]))

def fill_factor(vmp, imp, voc, isc):
    return (vmp*imp)/(voc*isc)

part2_ff = []
for i in range(25, 45, 4):
    part2_ff.append(fill_factor(main[i], main[i+1], main[i+3], main[i+2]))

part3_ff = []
for i in range(45, 65, 4):
    part3_ff.append(fill_factor(main[i], main[i+1], main[i+3], main[i+2]))

temp = [35, 45, 55, 65, 75]
rs = [0, 10, 30]
rsh = [100, 500, 5000]

plt.figure()
plt.plot(temp, part2_ff, '*-')
plt.xlabel("Temperature")
plt.ylabel("Fill Factors")
plt.title("Part 2 Fill Factors")
plt.show()

plt.figure()
plt.plot(temp, main[0:25:5], '*-')
plt.plot(temp, main[1:25:5], '*-')
plt.plot(temp, main[2:25:5], '*-')
plt.xlabel("Temperature")
plt.ylabel("V_D")
plt.legend(["For 1mA", "For 2mA", "For 5mA"])
plt.title("Part 2 V_D")
plt.show()

plt.figure()
plt.plot(temp, main[28:45:4], '*-')
plt.xlabel("Temperature")
plt.ylabel("V_OC")
plt.title("Part 2 V_OC")
plt.show()

plt.figure()
plt.plot(rs, main[48:57:4], '*-')
plt.xlabel("Series Resistance")
plt.ylabel("V_OC")
plt.title("Part 3 V_OC")
plt.show()
plt.figure()
plt.plot(rsh, [main[60], main[52], main[64]], '*-')
plt.xlabel("Shunt Resistance")
plt.ylabel("V_OC")
plt.title("Part 3 V_OC")
plt.show()

plt.figure()
plt.plot(rs, main[47:57:4], '*-')
plt.xlabel("Series Resistance")
plt.ylabel("I_SC")
plt.title("Part 3 I_SC")
plt.show()
plt.figure()
plt.plot(rsh, [main[59], main[51], main[63]], '*-')
plt.xlabel("Shunt Resistance")
plt.ylabel("I_SC")
plt.title("Part 3 I_SC")
plt.show()

plt.figure()
plt.plot(rs, part3_ff[:3], '*-')
plt.xlabel("Series Resistance")
plt.ylabel("Fill Factors")
plt.title("Part 3 Fill Factors")
plt.show()
plt.figure()
plt.plot(rsh, [part3_ff[-2], part3_ff[1], part3_ff[-1]], '*-')
plt.xlabel("Shunt Resistance")
plt.ylabel("Fill Factors")
plt.title("Part 3 Fill Factors")
plt.show()