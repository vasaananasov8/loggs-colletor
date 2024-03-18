from aiokafka import AIOKafkaConsumer  # type: ignore

import src.utils.config as cfg


def create_kafka_consumer() -> AIOKafkaConsumer:
    return AIOKafkaConsumer(
        cfg.KAFKA_TOPIC_NAME,
        bootstrap_servers=f"{cfg.KAFKA_HOST}:{cfg.KAFKA_PORT}",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
    )


async def kafka_consumer_worker(consumer: AIOKafkaConsumer) -> None:
    """
    Start consumer and loop to listen kafka
    :param consumer:
    :return:
    """
    await consumer.start()
    try:
        async for msg in consumer:
            #  Some logic with messages from kafka
            print(f"Process msg from kafka: {msg}")
    finally:
        await consumer.stop()
