from game_message import Tick, Action, Spawn, Sail, Dock, Anchor, directions

import math

class Bot:
    
    ports_plan = []
    
    i = 0

    return_plan = []

    def __init__(self):
        print("Initializing your super mega duper bot")

    def check_obstacle(list_topology, direction, max):
        new_direction = direction
        if direction == "SE":
            if list_topology[2][2] < max:
                new_direction = direction
            else:
                if list_topology[1][2] < max:
                    new_direction = "E"
                elif list_topology[2][1] < max:
                    new_direction = "S"
                elif list_topology[0][2] < max:
                    new_direction = "NE"
                elif list_topology[2][0] < max:
                    new_direction = "SW"
                elif list_topology[0][1] < max:
                    new_direction = "N"
                elif list_topology[1][0] < max:
                    new_direction = "W"
        elif direction == "SW":
            if list_topology[2][0] < max:
                new_direction = direction
            else:
                if list_topology[1][0] < max:
                    new_direction = "W"
                elif list_topology[2][1] < max:
                    new_direction = "S"
                elif list_topology[2][2] < max:
                    new_direction = "SE"
                elif list_topology[1][2] < max:
                    new_direction = "NW"
                elif list_topology[0][1] < max:
                    new_direction = "N"
                elif list_topology[0][1] < max:
                    new_direction = "E"
        elif direction == "S":
            if list_topology[2][1] < max:
                new_direction = direction
            else:
                if list_topology[2][2] < max:
                    new_direction = "SE"
                elif list_topology[2][0] < max:
                    new_direction = "SW"
                elif list_topology[1][2] < max:
                    new_direction = "E"
                elif list_topology[1][0] < max:
                    new_direction = "W"
                elif list_topology[0][2] < max:
                    new_direction = "NE"
                elif list_topology[0][0] < max:
                    new_direction = "NW"
        elif direction == "NE":
            if list_topology[0][2] < max:
                new_direction = direction
            else:
                if list_topology[0][1] < max:
                    new_direction = "N"
                elif list_topology[1][2] < max:
                    new_direction = "E"
                elif list_topology[2][2] < max:
                    new_direction = "SE"
                elif list_topology[0][0] < max:
                    new_direction = "NW"
                elif list_topology[2][1] < max:
                    new_direction = "S"
                elif list_topology[1][0] < max:
                    new_direction = "W"
        elif direction == "NW":
            if list_topology[0][0] < max:
                new_direction = direction
            else:
                if list_topology[0][1] < max:
                    new_direction = "N"
                elif list_topology[1][0] < max:
                    new_direction = "W"
                elif list_topology[0][2] < max:
                    new_direction = "NE"
                elif list_topology[2][0] < max:
                    new_direction = "SW"
                elif list_topology[1][2] < max:
                    new_direction = "E"
                elif list_topology[2][1] < max:
                    new_direction = "S"
        elif direction == "N":
            if list_topology[0][1] < max:
                new_direction = direction
            else:
                if list_topology[0][0] < max:
                    new_direction = "NW"
                elif list_topology[0][2] < max:
                    new_direction = "NE"
                elif list_topology[1][0] < max:
                    new_direction = "W"
                elif list_topology[1][2] < max:
                    new_direction = "E"
                elif list_topology[2][0] < max:
                    new_direction = "SW"
                elif list_topology[2][2] < max:
                    new_direction = "SE"

        return new_direction

        
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
        if len(Bot.ports_plan) == 1:
            current = 0
            while current < len(Bot.ports_plan):
                distance = []
                for poss_next_port in range(len(tick.map.ports)):
                    if poss_next_port in Bot.ports_plan:
                        continue
                    
                    # Use .row instead of [0]
                    coord = [tick.map.ports[Bot.ports_plan[current]].row - tick.map.ports[poss_next_port].row,
                            tick.map.ports[Bot.ports_plan[current]].column - tick.map.ports[poss_next_port].column]

                    distance_current_port = math.sqrt(coord[0]**2 + coord[1]**2)

                    distance.append([distance_current_port, poss_next_port])
                    
                    distance = sorted(distance)
                
                current += 1

                if current == len(tick.map.ports)-1:
                    Bot.ports_plan.append(current)
                    Bot.ports_plan.append(Bot.ports_plan[0])
                    break
                else:
                    #print(distance)
                    Bot.ports_plan.append(distance[0][1])
            
   
        
        
        #return Sail(directions[tick.currentTick % len(directions)])
        #for i in range(1,len(ports_plan)):
        
        col = tick.map.ports[Bot.ports_plan[Bot.i]].column - tick.currentLocation.column
        row = tick.map.ports[Bot.ports_plan[Bot.i]].row - tick.currentLocation.row
        
        topology_around =  [[tick.map.topology[tick.currentLocation.row-1][tick.currentLocation.column-1],tick.map.topology[tick.currentLocation.row-1][tick.currentLocation.column],tick.map.topology[tick.currentLocation.row-1][tick.currentLocation.column+1]],
                            [tick.map.topology[tick.currentLocation.row][tick.currentLocation.column-1],tick.map.topology[tick.currentLocation.row][tick.currentLocation.column],tick.map.topology[tick.currentLocation.row][tick.currentLocation.column+1]],
                            [tick.map.topology[tick.currentLocation.row+1][tick.currentLocation.column-1],tick.map.topology[tick.currentLocation.row+1][tick.currentLocation.column],tick.map.topology[tick.currentLocation.row+1][tick.currentLocation.column+1]]]
        
        max_tide = tick.map.tideLevels.max


        if row > 0:
            if col > 0:
                return Sail(Bot.check_obstacle(topology_around, "SE", max_tide))
            elif col < 0:
                return Sail(Bot.check_obstacle(topology_around, "SW", max_tide))
            else:
                return Sail(Bot.check_obstacle(topology_around, "S", max_tide))
        elif row < 0: 
            if col > 0: 
                return Sail(Bot.check_obstacle(topology_around, "NE", max_tide))
            elif col < 0:
                return Sail(Bot.check_obstacle(topology_around, "NW", max_tide))
            else:
                return Sail(Bot.check_obstacle(topology_around, "N", max_tide))
        else:
            if col > 0 :
                return Sail(Bot.check_obstacle(topology_around, "E", max_tide))
            elif col < 0:
                return Sail(Bot.check_obstacle(topology_around, "W", max_tide))
            else:
                if Bot.i != len(Bot.ports_plan)-1:
                    Bot.i += 1
                print(tick.map.ports[Bot.ports_plan[Bot.i]].column )
                print(tick.map.ports[Bot.ports_plan[Bot.i]].row) 
                return Dock()
