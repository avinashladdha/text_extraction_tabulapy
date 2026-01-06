import tabula
import pandas as pd
import os

# Set working directory
os.chdir("/Users/avinashladdha/___PERSONAL/text_extraction")

# Specify the PDF file path
pdf_path = "/Users/avinashladdha/___PERSONAL/text_extraction/SolarData.pdf"

# Extract tables from specific pages
pages = [i for i in range(4,5)]

def standardize_columns(tables):
    """Standardize column count and alignment across all tables"""
    if not tables:
        return tables
    
    # Find the maximum column count
    max_cols = max(len(table.columns) for table in tables)
    
    standardized_tables = []
    for idx, table in enumerate(tables):
        current_cols = len(table.columns)
        
        if current_cols < max_cols:
            # Add missing columns with NaN values
            for i in range(max_cols - current_cols):
                table[f"Extra_Col_{i}"] = None
            print(f"Table {idx + 1}: Added {max_cols - current_cols} column(s)")
        
        elif current_cols > max_cols:
            # Keep only the first max_cols columns
            table = table.iloc[:, :max_cols]
            print(f"Table {idx + 1}: Trimmed to {max_cols} columns")
        
        standardized_tables.append(table)
    
    return standardized_tables

try:
    # Extract tables with different parameters
    tables = tabula.read_pdf(
        pdf_path, 
        pages=pages, 
        multiple_tables=False,
        lattice=True
    )
    
    # Print detailed info about Table 2 (index 1)
    if len(tables) > 1:
        print("\n=== TABLE 2 INSPECTION ===")
        print(f"Shape: {tables[1].shape}")
        print(f"Columns: {list(tables[1].columns)}")
        print(f"First few rows:\n{tables[1].head(10)}")
    
    # Standardize columns across all tables
    tables = standardize_columns(tables)
    
    # Display extracted tables
    for idx, table in enumerate(tables):
        print(f"\n--- Table {idx + 1} (Columns: {len(table.columns)}) ---")
        print(table.head())
        
        # Save each table to a CSV file
        table.to_csv(f"table_{idx + 1}.csv", index=False)
    
    print(f"\nSuccessfully extracted and standardized {len(tables)} table(s)")
    
except Exception as e:
    print(f"Error extracting tables: {e}")