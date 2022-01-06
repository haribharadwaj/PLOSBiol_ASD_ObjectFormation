# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:50:07 2018

@author: hari
"""

from scipy import io
import pylab as pl


hemi = 'right'  # 'left' for Fig 2A, 'right' for fig 2B
fname = 'ERPsummary_zscore_' + hemi + '_OverallOnset.mat'
dat = io.loadmat(fname, squeeze_me=True)

t = dat['t']
ysummary = dat['ysummary']

# Plot individual groups
nasd = 21
ntd = 26

mtd = ysummary[:26, ].mean(axis=0)
etd = ysummary[:26, ].std(axis=0) / (ntd ** 0.5)
masd = ysummary[26:, ].mean(axis=0)
easd = ysummary[26:, ].std(axis=0) / (nasd ** 0.5)

alpha = 0.25

pl.plot(t,mtd, 'b')
pl.fill_between(t, mtd - etd, mtd + etd, alpha=alpha)
pl.plot(t, masd, 'r')
pl.fill_between(t, masd - easd, masd + easd, alpha=alpha)
pl.ylim([-2., 12.])
pl.legend(('TD', 'ASD'), loc='upper left')
pl.xlabel('Time (s)', fontsize=16)
ax = pl.gca()
ax.tick_params(labelsize=14)
pl.show()
