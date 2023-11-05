import math
import numpy as np

# Define the time-domain signal x(n)
x_n = [1,3,5,7,9,11,13,15]
A = np.array([64.0, 20.9050074380220, 11.3137084989848, 8.65913760233915, 8, 8.65913760233915, 11.3137084989848, 20.9050074380220])
Phase = np.array([0.0, 1.96349540849362, 2.35619449019235, 2.74889357189107, -3.14159265358979, -2.74889357189107, -2.35619449019235, -1.96349540849362])
N = 8
varia = input("Enter type of operation: ")


def dft(x_n, N):
    x_k = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        x_k[k] = np.sum(x_n * np.exp(-1j * 2 * np.pi * k * np.arange(N) / N))
    # Calculate amplitude and phase
    amplitude = np.abs(x_k)
    phase = np.angle(x_k)

    return amplitude, phase

# Function to calculate IDFT
def idft(amplitudes, phases, N):
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(1j * 2 * np.pi * k * n / N)
    X_n = np.dot(e, amplitudes * np.exp(1j * phases))
    return X_n / N

if(varia == "DFT"):
    x, y = dft(x_n=x_n,N=N)
    # Format the numbers
    x = [f'{i:.13f}f' for i in x]
    y = [f'{i:.13f}f' for i in y]
    # Print the results
    print("(A) = ", x)
    print("Phase = ", y)
else:
    X_n = idft(amplitudes=A,phases=Phase,N=N)
    x = np.array(range(N))
    # Extract the real parts and store them in a list
    y = [round(xn.real) for xn in X_n]
    print("x = ",x)
    print("y = ",y)

