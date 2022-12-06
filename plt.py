import matplotlib.pyplot as plt

ps = [16,
      64,
      128,
      256,
      384,
      512,
      768,
      1024,
      1280,
      1536,
      2048,
      2560,
      3072,
      3584,
      3968
      ]

# for basic
memory = [0,
          48,
          176,
          736,
          528,
          704,
          1456,
          2512,
          3824,
          5408,
          9184,
          14016,
          11744,
          18624,
          32480,
          ]
time = [0.06008148193359375,
        0.6148815155029297,
        2.312898635864258,
        8.862972259521484,
        19.86980438232422,
        35.89320182800293,
        83.7256908416748,
        149.68609809875488,
        239.12501335144043,
        344.56896781921387,
        608.0398559570312,
        976.733922958374,
        1415.229082107544,
        1913.0868911743164,
        2358.213186264038
        ]

# for dc
memory_dc = [16,
             32,
             32,
             48,
             80,
             80,
             80,
             144,
             176,
             336,
             240,
             320,
             384,
             464,
             352
             ]
time_dc = [0.1888275146484375,
           1.5921592712402344,
           5.544900894165039,
           19.616127014160156,
           43.82514953613281,
           79.33306694030762,
           177.1676540374756,
           313.8539791107178,
           495.5577850341797,
           719.1481590270996,
           1282.9740047454834,
           2019.3829536437988,
           2855.311870574951,
           3935.6307983398438,
           4829.51807975769
           ]

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
