from db_past_winning_numbers import *


file_name = 'past_winning_number.db'
(conn, cursor) = db_open(file_name)

records = db_load(cursor)
