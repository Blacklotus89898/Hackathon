from game_message import Tick, Action, Spawn, Sail, Dock, Anchor, directions

import math

class Bot:
    
    ports_plan = []

    def __init__(self):
        print("Initializing your super mega duper bot")

        
    def get_next_move(self, tick: Tick) -> Action:
        """
        Here is where the magic happens, for now the move is random. I bet you can do better ;)
        """
        
        # Spawn at the closest dock
        if tick.currentLocation is None:
            closest_ports = []
            for i_ports in range(len(tick.map.ports)):
                distance = math.sqrt(tick.map.ports[i_ports].row**2 + tick.map.ports[i_ports].column**2)
                port_distance = [distance, i_ports]
                closest_ports.append(port_distance)

                closest_ports = sorted(closest_ports)

            Bot.ports_plan += [closest_ports[0][1]]
            return Spawn(tick.map.ports[closest_ports[0][1]])
        
        # Plan the next ports
        if len(Bot.ports_plan) == 0:
            
            current = 0
            while current < len(Bot.ports_plan):
                distance = []
                for poss_next_port in range(len(tick.map.ports)):
                    if current == poss_next_port:
                        continue
                    
                    coord = [tick.map.ports[Bot.ports_plan[poss_next_port]].row-tick.map.ports[current].row,
                            tick.map.ports[Bot.ports_plan[poss_next_port]].column-tick.map.ports[Bot.ports_plan[current]].column]
                    distance_current_port = math.sqrt(coord[0]**2 + coord[1]**2)

                    if len(distance) == 0:
                        distance.append([distance_current_port, poss_next_port])
                    elif distance_current_port < distance:
                        distance[0] = [distance_current_port, poss_next_port]
                Bot.ports_plan.append(distance[0][1])

                current += 1
            
        if tick.currentLocation == tick.map.ports[Bot.ports_plan[0]] and len(tick.visitedPortIndices) == 0:
            return Dock()
        
        return Sail(directions[tick.currentTick % len(directions)])
