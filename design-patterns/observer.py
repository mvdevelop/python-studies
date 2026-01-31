
class Observer:
    def update(self, message):
        pass


class Subscriber(Observer):
    def update(self, message):
        print(f"Received message: {message}")


class Publisher:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Usage
publisher = Publisher()
subscriber1 = Subscriber()
subscriber2 = Subscriber()

publisher.subscribe(subscriber1)
publisher.subscribe(subscriber2)

publisher.notify("New content available!")
