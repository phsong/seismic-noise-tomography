"""
Performing raw-clean FTAN analysis to extract dispersion
curves (Rayleigh group velocity vs period) across pairs
of station.
"""

from pysismo import pscrosscorr
import glob
import os

# loading cross-correlations
flist = sorted(glob.glob(pathname='../Cross-correlation/xcorr*.pickle*'))
print 'Select file containing cross-correlations:'
print '\n'.join('{} - {}'.format(i, os.path.basename(f)) for i, f in enumerate(flist))
pickle_file = flist[int(raw_input('\n'))]
xc = pscrosscorr.load_pickled_xcorr(pickle_file)

# performing raw-clean FTAN, exporting FTANs to pdf and
# dispersion curves to pickle file
suffix = os.path.basename(pickle_file).split('_')[-1].split('.')[0]
xc.FTANs(suffix=suffix, whiten=True)