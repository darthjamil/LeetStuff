# Requirements
## Functional Requirements
- I can press the Up button, and the closest elevator already going up will stop to pick me up.
  - No other elevator will stop to pick me up.
- I can press the Down button, and the closest elevator already going down will stop to pick me up.
  - No other elevator will stop to pick me up.
- If there is no such elevator in either case, the closest free elevator will pick me up.
- When I get into an elevator and press a floor, that floor is added to the elevators list of floors to stop at.
- If I press a lower floor for an elevator going up, it prevents me from pressing the lower floor. Same vice versa.
- If no elevators are available to pick me up, the first one that becomes available will be scheduled to pick me up.
- An elevator request can never be starved.

## Non-Functional Requirements
- We will not fix the numnber of elevators. Call it K.
- Some elevators may go only to floors N through M.
- The system should read the current state/location of elevators on boot.

# Application Design
## Layers
Onion architecture, but infrastructure service layer is collapsed into the API layer, and 
there is no repository layer needed because no durable storage is needed.
- API Layer: contains interface with mechanical components and coordination logic
- Domain Layer: Contains domain objects and business logic

## API
- void boot(int numElevators, int numFloors)

From a floor
- void RequestUp(int fromFloor)
- void RequestDown(int fromFloor)
- void UpElevatorArrived()
- void DownElevatorArrived()

Inside an elevator
- bool AddFloor(int floor)

## Design
```
class System // singleton
    Elevators[]
    Floors[]

    static System(int numElevators, int numFloors)
        - TODO accept allowedFloors for each elevator

    void RequestUp(int floor)
        - Sort elevators by difference between currentFloor and floor; return smallest one that returns true for AddFloor(int)

    void RequestDown(int floor)
        - Same as Above

class Elevator
    int currentFloor
    Direction direction // Direction.Up, Direction.Down, Direction.Stationary
    int[] allowedFloors // always includes Lobby
    Queue<int> floorsToStopAt

    bool AddFloor(int floor)
        - return false if floor is not in allowedFloors
        - if direction is Up and floor > currentFloor, add to queue and return true else false
        - if direction is Down and floor < currentFloor, add to queue and return true else false
        - if direction is stationary, add to queue, set direction, and return true

    void Tick(int currentFloor) // called by hardware as elevator moves
        - tick currentFloor and deque if currentFloor is in queue
        - if currentFloor is last element in queue, set direction to Stationary

class Floor
    bool upRequested
    bool downRequested
```
