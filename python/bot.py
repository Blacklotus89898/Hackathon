from game_message import Tick, Action, Spawn, Sail, Dock, Anchor, directions

class Bot:
    def __init__(self):
        print("Initializing your super mega duper bot")
        
    def get_next_move(self, tick: Tick) -> Action:
        """
        Here is where the magic happens, for now the move is random. I bet you can do better ;)
        """
        if tick.currentLocation is None:
            return Spawn(tick.map.ports[0])
        
        #return Sail(directions[tick.currentTick % len(directions)])
        for i in range(len(ports_plan)):
            row = tick.map.ports[ports_plan[i]].column - tick.currentLocation.column
            col = tick.map.ports[ports_plan[i]].row - tick.currentLocation.row
        
        
            if row > 0:
                if col > 0:
                    return Sail("NE")
                elif col < 0:
                    return Sail("NW")
                else:
                    return Sail("N")
            elif row <0: 
                if col > 0: 
                    return Sail("SE")
                elif col < 0:
                    return Sail("SW")
                else:
                    return Sail("S")
            else:
                if col > 0 :
                    return Sail("E")
                elif col < 0:
                    return Sail("W")
                else:
                    return Dock()

        
        """

        while Tick.currentLocation != Tick.map.Position 
        if desired.Position.row == 1:  
            return Sail(directions[0])
        if desired.Position.row == -1:  
            return Sail(directions[4])
        if desired.Position.col == 1:  
            return Sail(directions[2])
        if desired.Position.col == -1:  
            return Sail(directions[6])
    """

    """if Sail.direction == "N":
        Tick.currentLocation.column += 1 
    if Sail.direction == "S":
        Tick.currentLocation.column -= 1 
    if Sail.direction == "W":
        Tick.currentLocation.row -= 1 
    if Sail.direction == "E":
        Tick.currentLocation.row += 1
    if Sail.direction == "NE":
        Tick.currentLocation.row += 1"""
       

