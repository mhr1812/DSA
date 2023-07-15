from typing import List
import heapq

class Schedule:

    def __init__(self, value=0, events=None):
        self.value = value
        self.events = [] if events is None else events

    def __repr__(self):
        return f"Schedule(value={self.value}, events={self.events})"
    
    def __lt__(self, other):
        # less-than: smaller value, or more events to achieve the same value
        return self.value < other.value or self.value == other.value and len(self.events) > len(other.events)

    def add_event(self, value, k):

        assert 1 <= k and len(self.events) <= k
        
        new_events = self.events.copy()
        new_value = self.value

        if k > len(new_events):
            new_events.append(value)
            new_value += value
            if k == len(new_events):
                heapq.heapify(new_events)
        elif value > new_events[0]:
            new_value += value - new_events[0]
            heapq.heapreplace(new_events, value)

        return Schedule(new_value, new_events)

class Solution:
    def __init__(self, debug=False):
        self.debug = debug
        
    def maxValue(self, events: List[List[int]], k: int) -> int:

        if k == 1:
            return max(e[2] for e in events)
                
        events = sorted(tuple(event) for event in events)
        
        best = Schedule()

        schedules = []
        for start, end, value in events:

            okay = False
            while schedules and schedules[0][0] < start:
                e, s = heapq.heappop(schedules)
                if self.debug:
                    print(f"finish event at t={e:3d}, schedule={s}")
                heapq.heappush(schedules, (end, s.add_event(value, k)))
                if best < s:
                    best = s
                    okay = True

            if self.debug:
                print(f"start  event at t={start:3d}, {value=:3d}")

            if not okay:
                heapq.heappush(schedules, (end, best.add_event(value, k)))

        for e, s in schedules:
            if self.debug:
                print(f"finish event at t={e:3d}, schedule={s}")
            if best < s:
                best = s

        if self.debug:
            print(f"best schedule overall: {best}")

        return best.value