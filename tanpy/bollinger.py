import pandas as pd

def bollinger_bands(x, lookback=20, band_sep=2.0, percent_b=True, pb_scale=100, col_prefix="bb_"):
    """ Creates Bollinger Bands® given a pandas Series `x` of price data
        (usually applied to close data).
    Args:
        x:         (DataFrame)
        lookback:  (int)   number of timesteps to use for moving average
                   (default=20)
        band_sep:  (float or list of 2 floats)
                   How much separation (in standard deviations) to use
                   placing the lower and upper bands.
                   (default=2.0)
                   If a single number is provided, then it symetrically places
                   the upper and lower bands.
                   If a list of two numbers is provided, the it interprets it as
                   [lower_separation, upper_separation]
        percent_b: (bool) Should it also return a column with %b? (default=True)
        pb_scale:  (float) Sets the scale of the percent_b metric. What value
                    to use when price touches the upper band? (default=100.0).
                    Eg, set to `pb_scale=1` for machine learning applications.
        col_prefix: (str) Column Name Prefix. When naming the columns for the
                    returned dataframe, what prefix should it use?
                    (default= "bb_")
    Returns:
        out: (DataFrame) Dataframe with the following columns:
             - `bb_mid`   the middle bollinger band (moving average)
             - `bb_lower` the lower bollinger band
             - `bb_upper` the upper bollinger band
             - `bb_percent_b` the %b metric
             Note, that the prefix of the column names will be different if you
             manually set the `col_prefix` to something else.
    Credits:
        Bollinger Bands® were developed by John Bollinger
    """
    # PARSE `band_sep`
    try:
        band_sep = float(band_sep)
        band_sep = [band_sep, band_sep]
    except:
        assert len(band_sep) > 1, "`band_sep`, must be a number, or a list of two numbers"

    # CALCULATE BANDS
    rolling = x.rolling(lookback)
    mid = rolling.mean()
    std = rolling.std()
    lower = mid - (band_sep[0]*std)
    upper = mid + (band_sep[1]*std)
    out = pd.DataFrame({f"{col_prefix}mid":   mid,
                        f"{col_prefix}upper": upper,
                        f"{col_prefix}lower": lower})

    # PERCENT B
    if percent_b:
        out[f"{col_prefix}percent_b"] = pb_scale * (x - lower) / (upper - lower)

    return out
