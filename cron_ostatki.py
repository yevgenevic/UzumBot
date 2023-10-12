from postcsv import ostatki_db
from db import select_ostatki_vse

url = select_ostatki_vse()[0]
ostatki_db(url)
