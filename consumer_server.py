import time

from kafka import KafkaConsumer


class ConsumerServer(KafkaConsumer):

    def __init__(self, topic_name):

        self.consumer = KafkaConsumer(
            bootstrap_servers="localhost:9092",
            request_timeout_ms=1000,
            auto_offset_reset="earliest",
            max_poll_records=10
        )
        self.consumer.subscribe(topics=topic_name)

    def consume(self):
        while True:
            for metadata, consumer_record in self.consumer.poll().items():
                if consumer_record:
                    for record in consumer_record:
                        print(record.value)
                        time.sleep(0.2)

            time.sleep(0.5)


if __name__ == "__main__":
    consumer = ConsumerServer("sf.police.department.calls.data")
    consumer.consume()
