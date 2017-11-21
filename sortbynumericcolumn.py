def render(table, params):
    sortby = params['sortby']
    order = params['order']

    if sortby is None:
        return table
    else:
        if table[sortby].dtype != np.float64 and table[sortby].dtype != np.int64:
            table[sortby] = table[sortby].str.replace(',', '')
            table[sortby] = table[sortby].astype(float)
        if order == 'Ascending':
            newtab = table.sort_values(sortby)
        else:
            newtab = table.sort_values(sortby, ascending = False)
        return newtab
