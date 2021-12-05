import pandas as pd
from pandas.core.reshape.merge import merge

customer_info = {'id': [8, 7, 4, 5, 13, 14, 15, 1], 'first_name': ['John', 'Jill', 'William', 'Henry', 'Emma', 'Liam', 'Mia', 'Mark'], 'last_name': ['Joseph', 'Michael', 'Daniel', 'Jackson', 'Isaac', 'Samuel', 'Owen', 'Thomas'], 'city': ['San Francisco', 'Austin', 'Denver', 'Miami', 'Miami', 'Los Angeles', 'New York', 'Pittsburgh'], 'address': ['4476 Parkway Drive', '4379 Skips Lane', '4833 Coplin Avenue', '1985 Peck Court', '3832 Euclid Avenue', '3153 Rhapsody Street', '4470 McKinley Avenue', '1299 Randall Drive'], 'phone_number': ['928-386-8164', '813-297-0692', '813-368-1200', '808-601-7513', '808-690-5201', '808-555-5201', '808-640-5916', '602-993-5916']}
order_info = {'id': [1, 2, 3, 4, 5, 6, 7, 8], 'cust_id': [4, 4, 5, 7, 7, 15, 15, 15], 'order_details': ['Coat', 'Shoes', 'Skirt', 'Coat', 'Shoes', 'Boats', 'Shirts', 'Slipper'], 'total_order_cost': [100, 80, 30, 25, 80, 100, 60, 20]}

customers = pd.DataFrame(data=customer_info)
orders = pd.DataFrame(data=order_info)

merged_dfs = pd.merge(customers, orders, how='left', left_on='id', right_on='cust_id')

print(merged_dfs)

final_list = merged_dfs[['first_name', 'last_name', 'city', 'order_details']].sort_values('first_name', 'order_details')