"""Vehicles Routing Problem (VRP)."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from random_matrice import MatRoad
from matrice_file_generator import create_csv

import random
import time


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = MatRoad.matrice_symm
    data['num_vehicles'] = random.randint(1, MatRoad.citiesR)
    data['depot'] = random.randint(0, MatRoad.citiesR-1)
    return data


def print_solution(data, manager, routing, solution, total_time):
    """Prints solution on console."""
    min_route_distance = 0
    list_distance = []
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        while not routing.IsEnd(index):
            plan_output += ' {} -> '.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += '{}\n'.format(manager.IndexToNode(index))
        plan_output += 'Distance of the route: {}km\n'.format(route_distance)
        print(plan_output)
        list_distance.append(route_distance)
        min_route_distance = [route_distance, min_route_distance]
        if min_route_distance != [0,0]:
            min_route_distance = min(i for i in min_route_distance if i != 0)
        else :
            min_route_distance = 0
    print('Minimum of the route distances: {}km'.format(min_route_distance))
    print("\n"+"Infos en plus")
    print(data['num_vehicles'])
    print(MatRoad.citiesR)
    print("Temps d execution : %s secondes" % (total_time))
    
    list_distance = [filter(lambda a: a != 0, list_distance)]
    total_time = [total_time]
    data['num_vehicles'] = [data['num_vehicles']]
    create_csv(total_time, data['num_vehicles'], list_distance)



def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    start_time = time.time()
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    distance_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        120,  # vehicle maximum travel distance
        True,  # start cumul to zero
        distance_name)
    distance_dimension = routing.GetDimensionOrDie(distance_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)
    
    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        total_time = int(time.time() - start_time)
        print_solution(data, manager, routing, solution, total_time)


if __name__ == '__main__':
    main()