from datetime import datetime, timedelta

data_new = datetime.now()
ten_minutes_later = data_new + timedelta(minutes=10)

print(data_new, ten_minutes_later)