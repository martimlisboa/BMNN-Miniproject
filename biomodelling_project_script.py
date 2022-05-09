#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:14:33 2022

@author: matthewleonsinis
"""

# Importing essential packages

import numpy as np


#%% Getting Started Q1

# Binary nodes initialisation

def nodes(no_of_neurons):
    S = np.random.choice((1., -1.), size=(no_of_neurons,1))
    return S.flatten()

# Sets weights of elements

def weight_matrix(no_of_neurons, patterns):
    weights = np.zeros((no_of_neurons, no_of_neurons))
    # Formula for weights
    for elem in patterns:
        elem_flattened = elem.flatten()
        for i in range(N):
            for j in range(N):
                weights[i, j] += elem_flattened[i] * elem_flattened[j]
    weights /= no_of_neurons
    # Diagonal elements zero
    np.fill_diagonal(weights, 0)
    return weights


#%% Define initial state

def flip_nodes(pattern, c):
    flipped_pattern = pattern.copy()
    for i in range(len(flipped_pattern)):
        r = np.random.rand()
        if r <= c:
            flipped_pattern[i] = -flipped_pattern[i]
    return flipped_pattern


#%% Update initial state

def update_state(weight_matrix, pattern, steps):
    for i in range(steps):
        pattern = np.sign(weight_matrix @ pattern)
    return pattern


#%% Hamming distance

def hamming_distance(pattern1, pattern2, no_of_neurons):
    return (no_of_neurons - np.dot(pattern1, pattern2)) / (2*no_of_neurons)


#%% Q2 Test Run

M = 10
N = 1000

pattern_list = []
for i in range(M):
    pattern = nodes(N)
    pattern_list.append(pattern)

weights = weight_matrix(N, pattern_list)

initial_pattern = flip_nodes(pattern_list[0], 0.05)

# After 10 time steps

updated_pattern = update_state(weights, initial_pattern, 10)

# Hamming distance

hamming_dist = hamming_distance(updated_pattern, initial_pattern, N)

print(hamming_dist)


#%% Q1: Implementation of Hopfield network and computing capacity


          