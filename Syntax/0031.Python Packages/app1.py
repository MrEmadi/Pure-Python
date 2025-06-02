# The reference of all Python packages: https://pypi.org
# -> Install the PIP: python -m pip install pip
# -> Upgrade the PIP: python -m pip install --upgrade pip

# Install a package -> pip install <Package-Name>
# Uninstall a package -> pip uninstall <Package-Name>

# For example: install the prettytable's package
# -> 'pip install prettytable'
from prettytable import PrettyTable

table = PrettyTable()
table.add_column(fieldname='Name', column='')
table.add_column(fieldname='Age', column='')
table.add_column(fieldname='City', column='')
table.add_column(fieldname='Sex', column='')
table.add_row(row=['Amirhossein Emadi', '25', 'Gorgan', 'Male'])
table.add_row(row=['Zahra Emadi', '23', 'Gorgan', 'Female'])
table.add_row(row=['Reza Jahangiry', '26', 'Boshruyeh', 'Male'])
table.add_row(row=['Narjes Emadi', '24', 'Tabas', 'Female'])
print(table.get_string())
