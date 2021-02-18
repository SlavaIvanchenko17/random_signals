import random
import time as t
import matplotlib.pyplot as plt
import numpy as np

def gen_signal(n, W_max, N):
    A = random.random()
    fi = random.random()
    signals = np.zeros(N)
    step = W_max/n
    w = step
    
    for t in range(N):
        for _ in range(n):
            signals[t] += A * np.sin(t * w + fi)
            w += step
        w = step
    return signals

def gen_time(n, W_max, N):
    time = []
    for i in range(N):
        start_time = t.time()
        gen_signal(n, W_max, i)
        end_time = t.time()
        time.append(end_time - start_time)
    return time

def math_expectation(data):
    return np.mean(data)

def dispertion(data):
    return np.var(data)


n = int(input("Harmonics = "))
W_max = int(input("Frequency = "))
N = int(input("Number of points = "))
I = int(input("Iterations(for time) = "))
signal1 = gen_signal(n, W_max, N)
signal2 = gen_signal(n, W_max, N)
time = gen_time(n, W_max, I)
plt.figure(1)
plt.plot(signal1)
plt.title('Generate random signals')
plt.figure(2)
plt.plot(time)
plt.title('Dependence of time on N')
plt.figure(3)
plt.xcorr(signal1, signal2, usevlines=True, normed=True, maxlags=200, lw=3)
plt.title('Crosscorrelation')
plt.figure(4)
plt.acorr(signal1, usevlines=True, normed=True, maxlags=200, lw=3)
plt.title('Autocorrelation')
plt.show()
print("Math expectation = " + str(math_expectation(signal1)))
print("Dispertion = " + str(dispertion(signal1)))

