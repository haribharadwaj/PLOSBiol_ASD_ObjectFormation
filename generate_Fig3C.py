# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy import io
import numpy as np
import pylab as pl

fname = 'ERPsummary_zscore.mat'
dat = io.loadmat(fname)
t = dat['t'].flatten()
c6 = dat['c6']
c12 = dat['c12']
c18 = dat['c18']

start, stop = 0.05, 0.44
pl.figure()
s7 = c6[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s14 = c12[:, np.logical_and(t > start, t < stop)].mean(axis=1)
s20 = c18[:, np.logical_and(t > start, t < stop)].mean(axis=1)

x = np.asarray([5.75, 11.75, 17.75])
y = np.asarray([s7[:26].mean(), s14[:26].mean(), s20[:26].mean()])
yerr = np.asarray([s7[:26].std() / (26 ** 0.5), s14[:26].std() / (26 ** 0.5),
                   s20[:26].std() / (26 ** 0.5)])
pl.errorbar(x, y, yerr,
            fmt='ob-', elinewidth=2)

x = x + 0.5
y = np.asarray([s7[26:].mean(), s14[26:].mean(), s20[26:].mean()])
yerr = np.asarray([s7[26:].std() / (21 ** 0.5), s14[26:].std() / (21 ** 0.5),
                   s20[26:].std() / (21 ** 0.5)])
pl.errorbar(x, y, yerr,
            fmt='sr--', elinewidth=2)
pl.xlabel('Number of Coherent Tones', fontsize=16)
pl.ylabel('Evoked Response (normalized)', fontsize=16)
pl.xticks((6, 12, 18))
ax = pl.gca()
ax.tick_params(labelsize=14)
pl.legend(('TD', 'ASD'), loc='upper left')
