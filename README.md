# Solar Data PDF Table Extraction

This project extracts tables from the `SolarData.pdf` file and converts them into structured CSV files using Python and tabula-py.

## Overview

The script reads tables from specified pages of a PDF document, standardizes column counts across tables, and exports each table as a separate CSV file.

## Requirements

- Python 3.7+
- pandas
- tabula-py
- jpype1

## Installation

Install required dependencies:

```bash
pip install tabula-py pandas jpype1
```

## Usage

1. Place `SolarData.pdf` in the `/Users/avinashladdha/___PERSONAL/text_extraction/` directory

2. Run the extraction script:

```bash
python extract_data.py
```

3. Output CSV files will be generated as `table_1.csv`, `table_2.csv`, etc.

## File Structure

```
/Users/avinashladdha/___PERSONAL/text_extraction/
├── extract_data.py          # Main extraction script
├── SolarData.pdf            # Source PDF file
├── table_1.csv              # Extracted table 1
├── table_2.csv              # Extracted table 2
├── combined_tables.csv      # All tables combined
└── README.md                # This file
```

## Features

- Extracts tables from specified PDF pages
- Handles hierarchical table structures
- Standardizes column counts across tables
- Forward fills missing values in key columns
- Exports to CSV format
- Combines all tables into a single file

## Parameters

Edit the `pages` variable in `extract_data.py` to extract from different pages:

```python
pages = [i for i in range(3, 13)]  # Extracts pages 3-12
```

## Extraction Methods

The script uses `lattice=True` for better detection of table borders and gridlines.

## Notes

- Table 2 has hierarchical data with sub-rows for "Enlisted Models"
- Empty cells are forward-filled to maintain data integrity
- Completely empty rows are removed during processing

## Troubleshooting

If you encounter a jpype error:
```bash
pip install jpype1 --upgrade
```

For better extraction quality on complex tables, consider using Camelot:
```bash
pip install camelot-py[cv]
```