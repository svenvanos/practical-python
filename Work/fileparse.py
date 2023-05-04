# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv (filename, has_headers=True, select=None, types=None, delimiter=",", silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        
        # read the file headers if they do
        if has_headers:
            headers = next(f).strip().split(delimiter)
        else:
            headers = []
        
        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        
        records = []
        for rowno, row in enumerate(rows):
            if not row: # skip rows with no data
                continue
            
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
                
            # apply type conversion if given
            
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue
                
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    
    return records

