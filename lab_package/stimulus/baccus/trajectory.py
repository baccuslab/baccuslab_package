import numpy as np
from scipy.interpolate import interp1d

from flystim import trajectory as ftrajectory

class TVPairsBounded(ftrajectory.Trajectory):
    """
    List of arbitrary time-value pairs. 
    Values are optionally bounded by a lower and upper bound, and wrap around if they exceed the bounds.

    :tv_pairs: list of time, value tuples. [(t0, v0), (t1, v1), ..., (tn, vn)]
    :kind: interpolation type. See scipy.interpolate.interp1d for options.
    :bounds: lower and upper bounds for the value. (lower, upper) or None for no bounds.
    """
    def __init__(self, tv_pairs, kind='linear', fill_value='extrapolate', bounds=None):
        times, values = zip(*tv_pairs)
        values_interpolated = interp1d(times, values, kind=kind, fill_value=fill_value, axis=0)
        
        if bounds is None:
            self.getValue = values_interpolated
        else:            
            lo = min(*bounds)
            hi = max(*bounds)
            bound_range = hi - lo
            self.getValue = lambda t: np.mod(values_interpolated(t) - lo, bound_range) + lo

