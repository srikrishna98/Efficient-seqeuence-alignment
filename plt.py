import matplotlib.pyplot as plt

ps = [96, 128]

# for basic
memory = [79.999, 154.921]
time = [0.0, 0.0]

# for dc
memory_dc = [17.204, 24.254]
time_dc = [0.014, 0.028]

plt.title('Memory(KB) vs Problem Size')

plt.plot(ps, memory, label="basic", marker='o',
         markerfacecolor='blue', markersize=5)
plt.plot(ps, memory_dc, label="efficient", marker='o',
         markerfacecolor='orange', markersize=5)

plt.xlabel("Problem Size (m+n)")
plt.ylabel("Memory (KB)")
plt.legend()

plt.savefig('Memory-ProblemSize.png')
plt.show()

plt.title('Time(s) vs Problem Size')

plt.plot(ps, time, label="basic", marker='o',
         markerfacecolor='blue', markersize=5)
plt.plot(ps, time_dc, label="efficient", marker='o',
         markerfacecolor='orange', markersize=5)

plt.xlabel("Problem Size (m+n)")
plt.ylabel("Time (s)")
plt.legend()

plt.savefig('Time-ProblemSize.png')
plt.show()
