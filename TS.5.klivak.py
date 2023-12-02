import threading
import time
import random
from queue import Queue
class PriorityMessageQueue:
    def __init__(self):
        self.normal_queue = Queue()
        self.priority_queue = Queue()

    def put_message(self, message, priority=False):
        if priority:
            self.priority_queue.put(message)
        else:
            self.normal_queue.put(message)

    def get_message(self):
        if not self.priority_queue.empty():
            return self.priority_queue.get()
        elif not self.normal_queue.empty():
            return self.normal_queue.get()
        else:
            return None

def message_producer(queue, t1):
    for i in range(1, 11):
        time.sleep(random.uniform(0, t1))
        queue.put_message(f"Повідомлення {i}", priority=(i % 3 == 0))

def message_consumer(queue, t2):
    while True:
        message = queue.get_message()
        if message:
            time.sleep(random.uniform(0, t2))
            print(f"Оброблено: {message}")

if __name__ == "__main__":
    random.seed(42)  

    priority_message_queue = PriorityMessageQueue()

    producer_thread = threading.Thread(target=message_producer, args=(priority_message_queue, 5))
    consumer_thread = threading.Thread(target=message_consumer, args=(priority_message_queue, 3))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
