# graph.rb
# adapted from http://snippets.dzone.com/posts/show/7331

require 'thread'
require 'set'

# directed, weighted graph
class Graph

  # is this the best way?
  INFINITY = 1 << 64

  def initialize
    # adjacency matrix
    # {<node> => {target => weight}, <node> => {...}}
    @graph = {}
    @nodes = Set.new
  end

  # s= source, t= target, w= weight
  def add_edge(s, t, w)
    if (not @graph.has_key? s)
      @graph[s] = {t => w}
    else
      @graph[s][t] = w
    end

    @nodes.merge [s,t]

  end
 
def BFS(graph, vertex, mark_method)
q = Queue.new
q << vertex
#mark v
while not q.empty? do
  t = q.pop
  #if t == goal return t
end
end
=begin
 procedure BFS(G,v)
   create a queue Q
3      enqueue v onto Q
4      mark v
5      while Q is not empty:
6          t < Q.dequeue()
7          if t is what we are looking for:
8              return t
9          for all edges e in G.incidentEdges(t) do
10             o < G.opposite(t,e)
11             if o is not marked:
12                  mark o
13                  enqueue o onto Q
=end
  # uses Dijkstra's to find shortest paths from source
  # takes a source node and returns a map of destinations and their shortest
  # distances
  def shortest_distances( src )
    
    raise ArgumentError if (not @graph.has_key? src)

    # keep a priority queue of nodes, ordered by known distances
    distances = Queue.new
	marked = []
    

    # results accumulator
    results = {}
    results[src] = 0
	distances << src

    while (not distances.empty?) do   
      # get the shortest known
      current_node = distances.pop
	  k = @graph[current_node].keys
	  new_keys =  k.keep_if{|node| not marked.include?(node)}
      new_keys.each do |key|
	    distances << key
		new_dist = results[current_node] + @graph[current_node][key]
		if (not results.include?(key))  #if @graph[current_node][key]
		  results[key] = new_dist
		else
		  if (results[key] > new_dist)
		     results[key] = new_dist
		  end			 
		end
		marked << key
		end
    end
    return results
  end

  
end