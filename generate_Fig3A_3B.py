# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:50:07 2018

@author: hari
"""

from scipy import io
import pylab as pl
import numpy as np

fname = 'ERPsummary_zscore.mat'
dat = io.loadmat(fname)
t = dat['t'].flatten()
c6 = dat['c6']
c12 = dat['c12']
c18 = dat['c18']

# Plot 2-panels (Fig 3A and 3B)
nasd = 21 
ntd = 23


ylims = (-1, 8.)
pl.figure()
pl.subplot(121)
pl.plot(t, np.mean(c6[:26, ], axis=0),
        'b-.', linewidth=1)
pl.plot(t, np.mean(c12[:26, ], axis=0),
        'b--', linewidth=2)
pl.plot(t, np.mean(c18[:26, ], axis=0),
        'b', linewidth=3)

pl.legend(('6', '12', '18'), loc='upper left')
pl.ylim(ylims)
pl.ylabel('MEG Response (Z-Score)', fontsize=16)
pl.xlabel('Time (s)', fontsize=16)
ax = pl.gca()
ax.tick_params(labelsize=14)
pl.subplot(122)

pl.plot(t, np.mean(c6[26:, ], axis=0),
        'r-.', linewidth=1)
pl.plot(t, np.mean(c12[26:, ], axis=0),
        'r--', linewidth=2)
pl.plot(t, np.mean(c18[26:, ], axis=0),
        'r', linewidth=3)
pl.ylim(ylims)
pl.legend(('6', '12', '18'), loc='upper left')
pl.xlabel('Time (s)', fontsize=16)
ax = pl.gca()
ax.tick_params(labelsize=14)
pl.show()