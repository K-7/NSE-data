# NSE-data
Scrapped NSE-50 data and displayed as cards of scrips. 

Used CherryPy, Redis and Celery for the entire flow.
> Celery tasks scraps the data and puts them in Redis.
> CherryPy server sends the data from Redis to the client side
