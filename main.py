import random
import time as t
import matplotlib.pyplot as plt
import numpy as np

def gen_signal(n, W_max, N, struct):
    if struct == 'ARRAY': signals = np.zeros(N)
    elif struct == 'LIST': signals = [0] * N
    step = W_max/n
    
    for i in range(n):
        A = random.random()
        fi = random.random()
        w = i * step
        for t in range(N):
            signals[t] += A * np.sin(w * t + fi)
    return signals

def gen_time(n, W_max, I, struct):
    time = []
    for i in range(I):
        start_time = t.time()
        gen_signal(n, W_max, i, struct)
        end_time = t.time()
        time.append(end_time - start_time)
    return time

def math_expectation(data):
    return np.mean(data)

def dispertion(data):
    return np.var(data)

def crosscorrelation(data1, data2):
    result = np.correlate(data1, data2, mode='same')
    return result

def autocorrelation(data):
    result = np.correlate(data, data, mode='full')
    return result[result.size // 2:]

n = int(input("Harmonics = "))
W_max = int(input("Frequency = "))
N = int(input("Number of points = "))
I = int(input("Iterations(for time) = "))

signal1 = gen_signal(n, W_max, N, 'LIST')
signal2 = gen_signal(n, W_max, N, 'LIST')
time = gen_time(n, W_max, I, 'LIST')

plt.figure(1)
plt.plot(signal1)
plt.title('Generate random signals')
plt.figure(2)
plt.plot(time)
plt.title('Dependence of time on N')
plt.figure(3)
plt.plot(crosscorrelation(signal1, signal2))
plt.title('Crosscorrelation')
plt.figure(4)
plt.plot(autocorrelation(signal1))
plt.title('Autocorrelation')
plt.show()

print("############################")

print("Math expectation = " + str(math_expectation(signal1)))
print("Dispertion = " + str(dispertion(signal1)))

print("############################")

yellow = "\033[93m {}\033[00m"
print(yellow.format("Time of generate for LIST = " + str(gen_time(n, W_max, 1, 'LIST')[0]))) 
print(yellow.format("Time of generate for ARRAY = " + str(gen_time(n, W_max, 1, 'ARRAY')[0]))) 
