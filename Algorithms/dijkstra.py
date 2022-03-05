import json

# setup the data structures
graph1 = {}
graph1['start'] = {}
graph1['start']['a'] = 6
graph1['start']['b'] = 2
graph1['a'] = {}
graph1['a']['fin'] = 1
graph1['b'] = {}
graph1['b']['a'] = 3
graph1['b']['fin'] = 5
graph1['fin'] = {}

graph2 = {}
graph2['start'] = {}
graph2['start']['a'] = 5
graph2['start']['b'] = 2
graph2['a'] = {}
graph2['a']['c'] = 4
graph2['a']['d'] = 2
graph2['b'] = {}
graph2['b']['a'] = 8
graph2['b']['d'] = 7
graph2['c'] = {}
graph2['c']['fin'] = 3
graph2['c']['d'] = 6
graph2['d'] = {}
graph2['d']['fin'] = 1
graph2['fin'] = {}

graph3 = {}
graph3['start'] = {}
graph3['start']['a'] = 10
graph3['a'] = {}
graph3['a']['b'] = 20
graph3['b'] = {}
graph3['b']['c'] = 1
graph3['b']['fin'] = 30
graph3['c'] = {}
graph3['c']['a'] = 1
graph3['fin'] = {}

graph4 = {}
graph4['start'] = {}
graph4['start']['a'] = 2
graph4['start']['b'] = 2
graph4['a'] = {}
graph4['a']['fin'] = 2
graph4['a']['c'] = 2
graph4['b'] = {}
graph4['b']['a'] = 2
graph4['c'] = {}
graph4['c']['fin'] = 2
graph4['c']['b'] = -1
graph4['fin'] = {}

costs = {}
parents = {}
processed = []

infinity = float('inf')

def get_cheapest_node():
	cheapest_cost = infinity
	cheapest_node = None

	for node in costs:
		if costs[node] < cheapest_cost and node not in processed:
			cheapest_cost = costs[node]
			cheapest_node = node

	return cheapest_node

def initialize(graph):
	global costs, parents
	costs = {}
	parents = {}

	first_neighbours = graph['start']
	for n in first_neighbours.keys():
		costs[n] = first_neighbours[n]
		parents[n] = "start"
	costs['fin'] = infinity
	parents['fin'] = None

	processed = []

def dijkstra(graph):
	initialize(graph)

	global costs, parents

	# TODO: get cheapest  node
	node = get_cheapest_node()

	# #TODO: for each neighbor update its cost if smaller
	while node is not None:
		neighbors = graph[node]
		for n in neighbors.keys():
			new_cost = costs[node] + neighbors[n]
			if n not in costs or new_cost < costs[n]:
				costs[n] = new_cost
				parents[n] = node

		# TODO: mark node as processed
		processed.append(node)
		# TODO: loop until no more unprocessed nodes
		node = get_cheapest_node()

def main():
	dijkstra(graph2)

	shortest_path = []
	shortest_path.append("fin")

	node = parents['fin']
	while node != "start" :
		shortest_path.append(node)
		node = parents[node]
	shortest_path.append("start")

	shortest_path.reverse()

	print("Shortest path = {}".format(shortest_path))
	print(json.dumps(parents, indent=4))
	print("Total Cost = ", costs['fin'])

if __name__ == '__main__':
	main()
