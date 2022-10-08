import asyncio
from datetime import timedelta
from arq import create_pool
from arq.connections import RedisSettings


async def main():
    redis = await create_pool(RedisSettings)
    await redis.enqueue_job("say_hello", name="lalala")
    await redis.enqueue_job('say_hello', name="hahaha", _defer_by=timedelta(minutes=1))


if __name__ == '__main__':
    asyncio.run(main())
