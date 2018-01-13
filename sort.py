def render(table, params):
    col = params['sortby']
    order = params['order']
    sorttype = params['num-or-alpha']

    if col=='':
        return table
    
    if sorttype == 0: # numeric
        # if we don't have a numeric type, try deleting commas and coercing
        if table[col].dtype != np.float64 and table[col].dtype != np.int64:
            table[col] = table[col].str.replace(',', '')
            table[col] = table[col].astype(float)
    else:
        table[col] = table[col].astype(str)

    asc = order == 0
    table.sort_values(col, inplace=True, ascending = asc)
    return table
