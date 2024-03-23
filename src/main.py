import asyncio
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

import src.utils.config as cfg
from services.kafka_concumer.KafkaConcumer import create_kafka_consumer, kafka_consumer_worker


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """
    Startup and shutdown events is deprecated now in FastAPI lib
    Code before "yield" - startup event
    Code after "yield" - shutdown event
    https://fastapi.tiangolo.com/advanced/events/
    :param app: arg for FastAPI
    """

    # Create async task to consume kafka
    kafka_consumer_task = asyncio.create_task(
        kafka_consumer_worker(create_kafka_consumer())
    )
    yield
    kafka_consumer_task.cancel()
    await kafka_consumer_task


def get_app() -> FastAPI:
    app = FastAPI(
        title="logg-collector",
        lifespan=lifespan
    )
    return app


if __name__ == '__main__':
    uvicorn.run(get_app(), host=cfg.APP_HOST, port=cfg.APP_PORT)
