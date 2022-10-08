from datetime import datetime
from arq import cron, run_worker
from aiohttp import ClientSession
from arq.connections import RedisSettings


async def startup(ctx):
    ctx['session'] = ClientSession()
    print("starting...")


async def shutdown(ctx):
    await ctx['session'].close()
    print("ending...")


async def say_hello(ctx, name) -> None:
    print("say_hello: ", ctx)
    print(f"Hello {name}")


async def timed_schedule(ctx) -> None:
    print("timed: ", ctx)
    print(datetime.now())


class WorkerSettings:
    on_startup = startup
    on_shutdown = shutdown
    # This redis setting used for workers getting jobs
    redis_settings = RedisSettings()
    job_timeout = 1200

    functions = [
        say_hello
    ]

    cron_jobs = [
        cron(
            timed_schedule,
            second=0,
            unique=True,
        ),
    ]


if __name__ == '__main__':
    run_worker(WorkerSettings)
