import numpy as np

class Importable:
    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def event():
        pass

    @staticmethod
    def render(wf_module, table):
        sortby = wf_module.get_param_column('sortby')
        order = wf_module.get_param_menu_string('order')

        if sortby == '':
            wf_module.set_ready(notify=False)
            return table
        elif sortby not in table.columns:
            wf_module.set_error('Invalid column.')
            return table
        else:
            if table[sortby].dtype != np.float64 and table[sortby].dtype != np.int64:
                table[sortby] = table[sortby].str.replace(',', '')
                table[sortby] = table[sortby].astype(float)
            if order == 'Ascending':
                newtab = table.sort_values(sortby)
            else:
                newtab = table.sort_values(sortby, ascending = False)
            wf_module.set_ready(notify=False)
            return newtab