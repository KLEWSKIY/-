import threading
import queue
import time
import random
def generate_messages(queue, t1):
    while True:
        message = f"Повідомлення {random.randint(1, 100)}"
        queue.put(message)
        time.sleep(random.uniform(0, t1))

def process_messages(queue, t2):
    while True:
        message = queue.get()
        print(f"Обробка: {message}")
        time.sleep(random.uniform(0, t2))

if __name__ == "__main__":
    message_queue = queue.Queue()

    t1 = 5
    t2 = 3

    generator_thread = threading.Thread(target=generate_messages, args=(message_queue, t1))
    processor_thread = threading.Thread(target=process_messages, args=(message_queue, t2))

    generator_thread.start()
    processor_thread.start()

    generator_thread.join()
    processor_thread.join()
