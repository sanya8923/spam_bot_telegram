import aioredis


db = await aioredis.from_url('redis://localhost')
