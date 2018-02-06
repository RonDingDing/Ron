import random
import collections
import queue


DEFAULT_NUMBER_OF_TAXIS = 19
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 33
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple("Event", ["time", "proc", "action"])


def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'Leave garage')
    for i in range(trips):
        time = yield Event(time, ident, "Pick up passenger")
        time = yield Event(time, ident, "Drop off passenger")

    yield Event(time, ident, "Going home")


class Simulator(object):
    def __init__(self, proc_map):
        self.events = queue.PriorityQueue()
        self.all_taxis = dict(proc_map)

    def run(self, end_time):
        for _, proc in sorted(self.all_taxis.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** End of events ***')
                break

            current_event = self.events.get()
            sim_time, taxi_id, previous_action = current_event
            print('Taxi ', taxi_id, ":" , current_event)
            active_proc = self.all_taxis[taxi_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.all_taxis[taxi_id]
            else:
                self.events.put(next_event)
        else:
            msg = "*** End of simulation time: {} events pending ***"
            print(msg.format(self.events.qsize()))


def compute_duration(previous_action):
    if previous_action in ["Leave garage", "Drop off passenger"]:
        interval = SEARCH_DURATION
    elif previous_action == "Pick up passenger":
        interval = TRIP_DURATION
    elif previous_action == "Going home":
        interval = 1
    else:
        raise ValueError("Unknown previous action : %s" % previous_action)
    return int(random.expovariate(1 / interval)) + 1


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS, seed=None):
    if seed is not None:
        random.seed(seed)
    taxis = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL) for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == "__main__":
    pass
     #main()
