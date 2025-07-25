
# there is no cache created for the main file as python always compiles the file which we directly load from the command line

# import sales
# when python sees this it will look for sales.py in the crrent directory
# if not found it will look for it in some pre defined directories which come with python installation
import sys
print(sys.path)

# from ecommerce.sales import calc_shipping,calc_tax
# or
from ecommerce import sales

sales.calc_shipping()
sales.calc_tax()

from ecommerce.ads import advertisements

advertisements.show_ads()

