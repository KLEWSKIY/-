import threading
import queue
import time
import random
class RailwaySection:
    def __init__(self):
        self.occupied = False
        self.lock = threading.Lock()

    def occupy(self):
        with self.lock:
            self.occupied = True

    def release(self):
        with self.lock:
            self.occupied = False


def train_generator(direction, railway_section, train_queue):
    while True:
        arrival_time = random.uniform(1, 5)
        time.sleep(arrival_time)

        print(f"Потяг {direction} наближається до залізничної ділянки.")
        with railway_section.lock:
            if railway_section.occupied:
                print(f"Потяг {direction} чекає на відкриття залізничної ділянки.")
                railway_section.lock.release()
                railway_section.lock.acquire()

        print(f"Потяг {direction} в'їжджає на ділянку залізниці.")
        railway_section.occupy()

        travel_time = random.uniform(3, 10)
        time.sleep(travel_time)

        print(f"Потяг {direction} виїжджає із залізничної ділянки.")
        railway_section.release()
        train_queue.put(1)


def main():
    railway_section = RailwaySection()
    train_queue = queue.Queue()

    westbound_train_thread = threading.Thread(target=train_generator, args=('На захід', railway_section, train_queue))
    eastbound_train_thread = threading.Thread(target=train_generator, args=('На схід', railway_section, train_queue))

    westbound_train_thread.start()
    eastbound_train_thread.start()

    while True:
        train_queue.get()
        print("Поїзд проїхав ділянку.")
        time.sleep(1)


if __name__ == "__main__":
    main()
