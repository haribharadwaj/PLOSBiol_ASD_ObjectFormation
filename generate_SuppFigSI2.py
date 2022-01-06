# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy import io
import numpy as np
import pylab as pl


fname = 'ERPsummary_zscore_left.mat'
dat = io.loadmat(fname)
t = dat['t'].flatten()
c6 = dat['c6']
c12 = dat['c12']
c18 = dat['c18']

peak = 'combined'
start, stop = (0.05, 0.44)
pl.subplot(1, 2, 1)
s6 = c6[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s12 = c12[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s18 = c18[:, np.logical_and(t > start, t < stop)].mean(axis=1)

# TD-left
x = np.asarray([5.75, 11.75, 17.75])
y = np.asarray([s6[:26].mean(), s12[:26].mean(), s18[:26].mean()])
yerr = np.asarray([s6[:26].std() / (26 ** 0.5), s12[:26].std() / (26 ** 0.5),
                   s18[:26].std() / (26 ** 0.5)])
pl.errorbar(x, y, yerr,
            fmt='ob-', elinewidth=2)


fname = 'ERPsummary_zscore_right.mat'
dat = io.loadmat(fname)
t = dat['t'].flatten()
c6 = dat['c6']
c12 = dat['c12']
c18 = dat['c18']

peak = 'combined'
start, stop = (0.05, 0.44)
# TD-right
s6 = c6[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s12 = c12[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s18 = c18[:, np.logical_and(t > start, t < stop)].mean(axis=1)

x = np.asarray([5.75, 11.75, 17.75])
x = x + 0.5
y = np.asarray([s6[:26].mean(), s12[:26].mean(), s18[:26].mean()])
yerr = np.asarray([s6[:26].std() / (26 ** 0.5), s12[:26].std() / (26 ** 0.5),
                   s18[:26].std() / (26 ** 0.5)])
pl.errorbar(x, y, yerr,
            fmt='ob--', elinewidth=2)

pl.xlabel('Number of Coherent Tones', fontsize=16)
pl.ylabel('Evoked Response (normalized)', fontsize=16)
pl.xticks((6, 12, 18))
pl.ylim((1.0, 4.25))
ax = pl.gca()
ax.tick_params(labelsize=14)
pl.legend(('Left', 'Right'), loc='upper left')


## LOAD DATA AGAIN FOR ASD
fname = 'ERPsummary_zscore_left.mat'
dat = io.loadmat(fname)
t = dat['t'].flatten()
c6 = dat['c6']
c12 = dat['c12']
c18 = dat['c18']

peak = 'combined'
start, stop = (0.05, 0.44)
pl.subplot(1, 2, 2)
s6 = c6[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s12 = c12[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s18 = c18[:, np.logical_and(t > start, t < stop)].mean(axis=1)

# ASD-left
y = np.asarray([s6[26:].mean(), s12[26:].mean(), s18[26:].mean()])
yerr = np.asarray([s6[26:].std() / (21 ** 0.5), s12[26:].std() / (21 ** 0.5),
                   s18[26:].std() / (21 ** 0.5)])
pl.errorbar(x, y, yerr,
            fmt='sr-', elinewidth=2)
pl.xlabel('Number of Coherent Tones', fontsize=16)
pl.xticks((6, 12, 18))
ax = pl.gca()
ax.tick_params(labelsize=14)
pl.legend(('Left', 'Right'), loc='upper left')




# ASD-right
fname = 'ERPsummary_zscore_right.mat'
dat = io.loadmat(fname)
t = dat['t'].flatten()
c6 = dat['c6']
c12 = dat['c12']
c18 = dat['c18']

peak = 'combined'
start, stop = (0.05, 0.44)
s6 = c6[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s12 = c12[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s18 = c18[:, np.logical_and(t > start, t < stop)].mean(axis=1)
x = x + 0.5
y = np.asarray([s6[26:].mean(), s12[26:].mean(), s18[26:].mean()])
yerr = np.asarray([s6[26:].std() / (21 ** 0.5), s12[26:].std() / (21 ** 0.5),
                   s18[26:].std() / (21 ** 0.5)])
pl.errorbar(x, y, yerr,
            fmt='sr--', elinewidth=2)
pl.xlabel('Number of Coherent Tones', fontsize=16)
pl.xticks((6, 12, 18))
pl.ylim((1.0, 4.25))
ax = pl.gca()
ax.tick_params(labelsize=14)
pl.legend(('Left', 'Right'), loc='upper left')