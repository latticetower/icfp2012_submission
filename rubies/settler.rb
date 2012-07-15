require 'c:/42/icfp2012/rubies/graph.rb'
require 'c:/42/icfp2012/rubies/d_lite.rb'
INFILE = "c:/42/icfp2012/rubies/levels/contest1.map" 
#, "r"
#outfile = File.new("c:/42/icfp2012/rubies/moves/result.txt", "w")
INFINITY = 1 << 64
@arr = Array.new
def reachable? (value)
  (value != '#' and value != '*')
end

def get_pred(vertex)
  preds = []
  x = vertex[0]
  y = vertex[1]
  if not reachable?(@arr[x][y])
    return []
  end
  if (x > 0) 
    if reachable?(@arr[x - 1][y])
	  preds.push([x-1, y])
	end
  end
  if (x < @arr.length - 1)
    if reachable?(@arr[x + 1][y])
	  preds.push([x + 1, y])
	end
  end
  if (y > 0) 
    if reachable?(@arr[x][y - 1])
	  preds.push([x, y - 1])
	end
  end
  if (y < @arr[x].length - 1)
    if reachable?(@arr[x][y + 1])
	  preds.push([x, y + 1])
	end
  end
  preds
end
def get_succ(vertex)
  succs = []
  x = vertex[0]
  y = vertex[1]
  if not reachable?(@arr[x][y])
    return []
  end
  if (x > 0) 
    if reachable?(@arr[x - 1][y])
	  succs.push([x-1, y])
	end
  end
  if (x < @arr.length - 1)
    if reachable?(@arr[x + 1][y])
	  succs.push([x + 1, y])
	end
  end
  if (y > 0) 
    if reachable?(@arr[x][y - 1])
	  succs.push([x, y - 1])
	end
  end
  if (y < @arr[x].length - 1)
    if reachable?(@arr[x][y + 1])
	  succs.push([x, y + 1])
	end
  end
  succs
end
def changes?
false
end
def changed_nodes
[]
end
def profit(v)
  if @arr[v[0]][v[1]] == '\\'
    return -25
  end
  0
end
def get_costs(u, v)
  if reachable?(@arr[v[0]][v[1]])
    return 1 + profit(v)
  end
  INFINITY
end

File.foreach(INFILE) do |line|
=begin
  case line
  when /\*/
    puts 'found rocks in line #{line}'
  when /\\/
    puts 'found lambdas in line #{line}'
  when /R/
    puts 'found robot in line'
  when /\#/
    puts 'found walls in line'
  when //
=end

a = line.gsub(/\n/, '').split(//)
@arr.push(a)
p a

end

g = DStarLiteSolver.new

g.set_heuristics({:h => lambda{|s1, s2| 3},
:pred => lambda{|vertex| get_pred(vertex)},
:succ => lambda{|vertex| get_succ(vertex)},
:costs => lambda{|u, v| get_costs(u, v)},
:change_function => lambda{changes? },
:changed_nodes => lambda{changed_nodes },
:eql => lambda{|u,v| u[0]==v[0] and u[1] ==v[1]}
})
p reachable? ([1,1])
p reachable? ([2,2])
g.mainfunc([1,1],[4,2])
#p g.shortest_distances('a')