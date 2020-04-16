#!/usr/bin/env python
## EstimatingExponentFromExecutionTime.py
## Avi Kak (kak@purdue.edu)
## March 31, 2015
## This script demonstrates the basic idea of how it is possible to infer
## the bit field of an exponent by measuring the time it takes to carry
## out the one of the key steps in the modular exponentiation algorithm.

import time

## This is our basic script for modular exponentiation. See Section 12.5.1 of
## Lecture 12:

def modular_exponentiate(A, B, modulus): #(1)
  time_trace = [] #(2)
  result = 1 #(3)
  while B > 0: #(4)
     start = time.time() #(5)
     if B & 1: #(6)
       result = ( result * A ) % modulus #(7)
     elapsed = time.time() - start #(8)
     time_trace.append(elapsed) #(9)
     B = B >> 1 #(10)
     A = ( A * A ) % modulus #(11)
  return result, time_trace #(12)

## Since a single experiment does not yield reliable measurements of the time
## taken by a computational step, this function helps us carry out repeated
## experiments:

def repeated_time_measurements(A, B, modulus, how_many_times): #(13)
  list_of_time_traces = [] #(14)
  results = [] #(15)
  for i in range(how_many_times): #(16)
    result, timetrace = modular_exponentiate(A, B, modulus) #(17)
    list_of_time_traces.append(timetrace) #(18)
    results.append(result) #(19)
  # Also return results for debugging, etc.
  return list_of_time_traces, results #(20)

A = 12345678901234567890123456789012345678901234567890123456789012345657889

B = 0b1111110101001001

modulus = 987654321 #(23)

num_iterations = 1000 #(24)

list_of_time_traces, results = repeated_time_measurements(A, B, modulus, num_iterations) #(25)

sums = [sum(e) for e in zip(*list_of_time_traces)] #(26)

averages = [x/num_iterations for x in sums] #(27)

averages = list(reversed(averages)) #(28)

print "\ntimings: ", averages #(29)

minval, maxval = min(averages), max(averages) 
print "maxval ", maxval
print "minval", minval
threshold = (maxval + minval) / 2 
bitstring = ''  #(32)
print "thredhold:", threshold

for item in averages: #(33)
  if item > threshold: #(34)
    bitstring += '1' #(35)
  else: #(36)
    bitstring += '0' #(37)

print "\nbitstring for B constructed from timings: ", bitstring #(38)

