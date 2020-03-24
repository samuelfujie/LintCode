import heapq
class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        results = []
        if not buildings:
            return results
            
        events = collections.defaultdict(list)
        for id, building in enumerate(buildings):
            enter, leave, height = building
            # 1 for enter, 0 for leave
            events[enter].append([1, height, id])
            events[leave].append([0, height, id])
        
        # (floor_height=0, id=-1)
        hp = [(0, -1)]
        heapq.heapify(hp)
        
        on_floor = True
        exited = set([])
        for x in sorted(events.keys()):
            for event in events[x]:
                # if entering
                if event[0]:
                    heapq.heappush(hp, (-event[1], event[2]))
                # if leaving
                else:
                    exited.add(event[2])

            while hp[0][1] in exited:
                heapq.heappop(hp)
            kp_height = -hp[0][0]
            
            if on_floor:
                results.append([x, x, kp_height])
                on_floor = False
            else:
                results[-1][1] = x
                if kp_height == 0:
                    on_floor = True
                    continue
                if results[-1][2] != kp_height:
                    results.append([x, x, kp_height])
                    
        return results