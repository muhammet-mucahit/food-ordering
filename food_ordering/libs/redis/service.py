from abc import ABC

import redis


class AbstractRedisPubSub(ABC):
    def __init__(self, channel):
        self._redis_client = redis.Redis(host="redis", port=6379, db=0)
        self._channel = channel


class Subscriber(AbstractRedisPubSub):
    def __init__(self, channel: str, callback):
        super(Subscriber, self).__init__(channel)
        self._pubsub = self._redis_client.pubsub(ignore_subscribe_messages=True)
        self.callback = callback

    def subscribe(self):
        self._pubsub.subscribe(self._channel)

    def get_value(self):
        message = self._pubsub.get_message(ignore_subscribe_messages=True)
        if message:
            return message["data"]
        message = self._pubsub.get_message(ignore_subscribe_messages=True)
        if message:
            return message["data"]

    def process(self):
        value = self.get_value()
        while value:
            decoded = value.decode("utf-8")
            self.callback(decoded)
            value = self.get_value()


class Publisher(AbstractRedisPubSub):
    def __init__(self, channel: str):
        super(Publisher, self).__init__(channel)

    def publish(self, value: str):
        self._redis_client.publish(self._channel, value)


class PubSubService:
    def __init__(self, publisher: Publisher, subscribers: [Subscriber]):
        self._publisher = publisher
        self._subscribers = subscribers

        # Start the subscription, be ready when orders published
        self._subscribe_all_subscribers_to_publisher()

    def _subscribe_all_subscribers_to_publisher(self):
        for subscriber in self._subscribers:
            subscriber.subscribe()

    def publish(self, value: str):
        self._publisher.publish(value)

    def process_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.process()
