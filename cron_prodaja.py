from postcsv import prodaja_db
from db import select_prodaja_vse

url = select_prodaja_vse()[0]
prodaja_db(url)
