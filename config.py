PG_USER = 'elenapalenova'
PG_PASSWORD = '123'
PG_HOST = '127.0.0.1'
PG_DB = 'swapi'
PG_DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:5432/{PG_DB}'
PG_DSN_ALC = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:5432/{PG_DB}'