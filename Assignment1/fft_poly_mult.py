import numpy as np # importing numpy for matrix operations
from math import floor, ceil

def FFT(x):
    N = len(x)
    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = \
          np.exp(-2j*np.pi*np.arange(N)/ N)
        
        X = np.concatenate(\
            [X_even+factor[:int(N/2)]*X_odd,
             X_even+factor[int(N/2):]*X_odd])
        return X

def IFFT(x):
    N = len(x)
    if N == 1:
        return x
    else:
        X_even = IFFT(x[::2])
        X_odd = IFFT(x[1::2])
        factor = np.exp(2j*np.pi*np.arange(N)/ N)
        
        X = np.concatenate(\
            [X_even+factor[:int(N/2)]*X_odd,
             X_even+factor[int(N/2):]*X_odd])
        return X

def IFFT2(x):
    n = len(x)
    return IFFT(x)/n

def pad_arrays(A,B):
    n1 = len(A)
    n2 = len(B)
    A = A + [0 for _ in range(n2-1)]
    B = B + [0 for _ in range(n1-1)]
    pad_size_A = 2**ceil(np.log2(len(A))) - len(A)
    pad_size_B = 2**ceil(np.log2(len(B))) - len(B)
    A += [0 for _ in range(pad_size_A)]
    B += [0 for _ in range(pad_size_B)]
    return A,B




def fft_poly_mult(A,B):
    A,B = pad_arrays(A,B)
    A = np.array(A)
    B = np.array(B)
    C = np.real(IFFT2(FFT(A)*FFT(B)))
    return list(map(round,C.tolist()))

def inbuilt_fft_poly_mult(A,B):
    A,B = pad_arrays(A,B)
    A = np.array(A)
    B = np.array(B)
    C = np.real(np.fft.ifft(np.fft.fft(A)*np.fft.fft(B)))
    return list(map(round,C.tolist()))