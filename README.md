# HSPICE Utilities
## Overview
Package for extracting data from HSPICE simulation runs.

## Supported Data Types
This package supports the following data types:
- `.mt.csv`: CSV files containing measurement data from HSPICE simulations.
- `.printtr`: Files containing transient analysis data prints from HSPICE simulations.

## Functionalities
### Single File Functionalities
- **parse_mt_csv**: Parses `.mt.csv` files to extract measurement data.
- **parse_printtr**: Parses `.printtr` files to extract transient analysis data.

Returned as `pandas.Dataframe`

### Folder Functionalities
- **batch_parse_mt_csv**: Parses all `.mt.csv` files in a folder including subfolders.
- **batch_parse_printtr**: Parses all `.printtr` files in a folder including subfolders.

Returned as a `dict` with:
 - `key` = `filename`
 - `value` = `pandas.Dataframe`

## Installation
To install the necessary dependencies, run:
```bash
git clone https://github.com/loncsemi/hspice_utils.git
```