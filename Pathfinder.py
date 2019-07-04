"""Vehicles Routing Problem (VRP)."""

from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from random_matrice import MatRoad
from matrice_file_generator import create_csv
import matplotlib.pyplot as plt

import random
import time
import Stat
import csv

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
    route_list = []
    max_route_distance = 0
    iteration = 0
    list_distance = []
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id+1)
        while not routing.IsEnd(index):
            iteration += 1
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
        route_list.append(route_distance)
        max_route_distance = max(route_distance, max_route_distance)
    print('Minimum of the route distances: {}km'.format(min_route_distance))
    print("\n"+"General informations for the vehicles")
    print("Number of iterations : "+str(iteration))
    print("Number of vehicles :",data['num_vehicles'])
    print("Number of cities",MatRoad.citiesR)
    print("Execution time : %s secondes" % (total_time),"\n")
    
    
    """ create the histogram and call the creation of the csv file """
    vehicles_time_list = []
    vehicles_list = []
    for i in range(data['num_vehicles']) :
        vehicles_list.append(i+1)
        vehicles_time_list.append(total_time)
    plt.bar(vehicles_list,route_list,align='center')
    plt.xlabel('Vehicle id')
    plt.ylabel('Minimum of the route distances')
    for i in range(len(route_list)):
        plt.hlines(route_list[i],0,vehicles_list[i]) 
    plt.show()

    csv_list = [data['num_vehicles'],total_time,min_route_distance,max_route_distance]
    create_csv(csv_list)



def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.    
    "data = create_data_model()"
    with open('DataPathfinder.csv', 'w') as csvFileData :
        writer = csv.writer(csvFileData, delimiter=';')
        column_list = ['Number of vehicles','Execution time', 
                       'Minimum distance', 
                       'Maximum distance']
        writer.writerow(column_list)
        csvFileData.close()
    data = {}
    data['distance_matrix'] = MatRoad.matrice_symm
    data['depot'] = random.randint(0, MatRoad.citiesR-1)
    
    i = 1
    while i < 100 :
        data['num_vehicles'] = i
        i += 1
        start_time = time.time()
    
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
                routing_enums_pb2.FirstSolutionStrategy.SAVINGS)

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        # Print solution on console.
        if solution:
            total_time = round(time.time() - start_time,2)
            print_solution(data, manager, routing, solution, total_time)
    Stat.StatistiqueMatRoad()

if __name__ == '__main__':
    main()