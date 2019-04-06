# TANPY - Technical Analysis for Python

## Motivation

The motivation for this package is due to the following:

The [ta-lib](http://mrjbq7.github.io/ta-lib/index.html) python wrapper for the popular [TA-Lib](https://www.ta-lib.org) library has the following problems:

- It requires the user to compile additional non-python libraries
- The underlying  TA-Lib library has not received any development since 2007
- It does not handle missing values gracefully


The [finta](https://github.com/peerchemist/finta) library is at least a pandas native library, but it has the following issues:

- It rigidly expects you to use a dataframe formatted in a very specific way, eg, columns labelled `"open", "close"`


This library is created to offer greater flexibility on the data you apply the indicator algorithms on, and foster greater amount of experimenting by the user, eg, applying indicators in non-standard ways, such as to something other than  `close` prices.


## Technical Analysis Notes

[Click here](notes/index.md) for notes about different technical indicators, and how to use them using this package.


# Installing

TODO:
