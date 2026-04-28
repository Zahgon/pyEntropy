import math
from collections import Counter

import numpy as np


def time_delay_embedding(time_series, embedding_dimension, delay):
    """Calculate time-delayed embedding.

    Parameters
    ----------
    time_series : np.ndarray
        The input time series, shape (n_times)
    embedding_dimension : int
        The embedding dimension (order).
    delay : int
        The delay between embedded points.

    Returns
    -------
    embedded : ndarray
        The embedded time series with shape (n_times - (order - 1) * delay, order).

    """
    pass


def util_pattern_space(time_series, lag, dim):
    """Create a set of sequences with a given lag and dimension.

    Parameters
    ----------
    time_series : np.ndarray
        Vector or string of the sample data
    lag : int
        Lag between the beginning of sequences
    dim : int
        Dimension (number of patterns)

    Returns
    -------
    pattern_space: np.ndarray
        2D array of vectors

    Raises
    ------
    ValueError: If the lag is less than 1 or the result matrix exceeds the size limit.

    """
    pass


def util_granulate_time_series(time_series, scale):
    """Extract coarse-grained time series.

    Parameters
    ----------
    time_series : np.ndarray
        Time series
    scale : int
        Scale factor

    Returns
    -------
    cts : np.ndarray
        Array of coarse-grained time series with a given scale factor

    """
    pass


def shannon_entropy(time_series):
    """Calculate Shannon Entropy of the sample data.

    Parameters
    ----------
    time_series: np.ndarray | list[str]
        Vector or string of the sample data

    Returns
    -------
    ent: float
        The Shannon Entropy as float value

    """
    pass


def sample_entropy(time_series, sample_length, tolerance=None):
    """Calculate the sample entropy of degree m of a time_series.

    This method uses Chebyshev norm.
    It is quite fast for random data but can be slower is there is
    structure in the input time series.

    Parameters
    ----------
    time_series : np.ndarray
        Time series, 1-d vector
    sample_length : int
        length of longest template vector
    tolerance : float
        tolerance (defaults to 0.1 * std(time_series)))

    Returns
    -------
    sampen: np.ndarray
        Array of Sample Entropies SE.
        SE[k] is the ratio `#templates of length k+1` / `#templates of length k`
        where `#templates of length 0` = n*(n - 1) / 2, by definition

    Notes
    -----
    The parameter 'sample_length' is equal to m + 1 in Ref[1].

    References
    ----------
    .. [1] http://en.wikipedia.org/wiki/Sample_Entropy
    .. [2] http://physionet.incor.usp.br/physiotools/sampen/
    .. [3] Madalena Costa, Ary Goldberger, CK Peng. Multiscale entropy analysis of biological signals

    """
    pass


def multiscale_entropy(time_series, sample_length, tolerance=None, maxscale=None):
    """Calculate Multiscale Entropy considering different time-scales of the time series.

    Parameters
    ----------
    time_series : np.ndarray
        Input time series for analysis.
    sample_length : int
        Bandwidth or group of points
    tolerance : float
        Tolerance value (default is 0.1 times the standard deviation of the `time_series`)
    maxscale : int
        Maximum timescale (default is the length of the `time_series`)

    Returns
    -------
    mse : np.ndarray
        Array of Multiscale Entropies

    References
    ----------
    .. [1] http://en.pudn.com/downloads149/sourcecode/math/detail646216_en.html
            Can be viewed at https://web.archive.org/web/20170207221539/http://en.pudn.com/downloads149/sourcecode/math/detail646216_en.html

    """
    pass


def permutation_entropy(time_series, order=3, delay=1, normalize=False):
    """Calculate Permutation Entropy.

    Parameters
    ----------
    time_series : list | np.ndarray
        Time series
    order : int
        Order of permutation entropy
    delay : int
        Time delay
    normalize : bool
        If True, divide by log2(factorial(m)) to normalize the entropy
        between 0 and 1. Otherwise, return the permutation entropy in bit.

    Returns
    -------
    pe : float
        Permutation Entropy

    References
    ----------
    .. [1] Massimiliano Zanin et al. Permutation Entropy and Its Main
        Biomedical and Econophysics Applications: A Review.
        http://www.mdpi.com/1099-4300/14/8/1553/pdf

    .. [2] Christoph Bandt and Bernd Pompe. Permutation entropy â€” a natural
        complexity measure for time series.
        http://stubber.math-inf.uni-greifswald.de/pub/full/prep/2001/11.pdf

    Notes
    -----
    Last updated (Oct 2018) by Raphael Vallat (raphaelvallat9@gmail.com):
    - Major speed improvements
    - Use of base 2 instead of base e
    - Added normalization

    Examples
    --------
    1. Permutation entropy with order 2

        >>> x = [4, 7, 9, 10, 6, 11, 3]
        >>> # Return a value between 0 and log2(factorial(order))
        >>> print(permutation_entropy(x, order=2))
            0.918

    2. Normalized permutation entropy with order 3

        >>> x = [4, 7, 9, 10, 6, 11, 3]
        >>> # Return a value comprised between 0 and 1.
        >>> print(permutation_entropy(x, order=3, normalize=True))
            0.589

    """
    pass


def multiscale_permutation_entropy(time_series, m, delay, scale):
    """Calculate the Multiscale Permutation Entropy.

    Parameters
    ----------
    time_series : np.ndarray
        Time series for analysis
    m : int
        Order of permutation entropy
    delay : int
        Time delay
    scale : int
        Scale factor

    Returns
    -------
    mspe : np.ndarray
        Array of Multiscale Permutation Entropies

    References
    ----------
    .. [1] Francesco Carlo Morabito et al. Multivariate Multi-Scale Permutation Entropy for
            Complexity Analysis of Alzheimer`s Disease EEG. www.mdpi.com/1099-4300/14/7/1186
    .. [2] http://www.mathworks.com/matlabcentral/fileexchange/37288-multiscale-permutation-entropy-mpe/content/MPerm.m

    """
    pass


def weighted_permutation_entropy(time_series, order=2, delay=1, normalize=False):
    """Calculate the weighted permutation entropy.

    Weighted permutation entropy captures the information in the amplitude of a signal where
    standard permutation entropy only measures the information in the ordinal pattern, "motif".

    Parameters
    ----------
    time_series : list | np.ndarray
        Time series
    order : int
        Order of permutation entropy
    delay : int
        Time delay
    normalize : bool
        If True, divide by log2(factorial(m)) to normalize the entropy
        between 0 and 1. Otherwise, return the permutation entropy in bit.

    Returns
    -------
    wpe : float
        Weighted Permutation Entropy

    References
    ----------
    .. [1] Bilal Fadlallah, Badong Chen, Andreas Keil, and JosÃ© PrÃ­ncipe
           Phys. Rev. E 87, 022911 - Published 20 February 2013

    Notes
    -----
    - Updated in Jun 2023 by Nikolay Donets
    - Updated in March 2021 by Samuel Dotson (samgdotson@gmail.com)

    Examples
    --------
    1. Weighted permutation entropy with order 2

        >>> x = [4, 7, 9, 10, 6, 11, 3]
        >>> # Return a value between 0 and log2(factorial(order))
        >>> print(permutation_entropy(x, order=2))
            0.912

    2. Normalized weighted permutation entropy with order 3

        >>> x = [4, 7, 9, 10, 6, 11, 3]
        >>> # Return a value comprised between 0 and 1.
        >>> print(permutation_entropy(x, order=3, normalize=True))
            0.547

    """
    pass


def composite_multiscale_entropy(time_series, sample_length, scale, tolerance=None):
    """Calculate Composite Multiscale Entropy.

    Parameters
    ----------
    time_series : np.ndarray
        Time series for analysis
    sample_length : int
        Number of sequential points of the time series
    scale : int
        Scale factor
    tolerance : float
        Tolerance (default = 0.1 * std(time_series))

    Returns
    -------
    cmse : np.ndarray
        Array of Composite Multiscale Entropies

    References
    ----------
    .. [1] Wu, Shuen-De, et al. "Time series analysis using
        composite multiscale entropy." Entropy 15.3 (2013): 1069-1084.

    """
    pass
