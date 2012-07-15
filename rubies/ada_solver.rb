require 'set'

class AdaStarSolver
  INFINITY = 1 << 64
  def initialize
    # adjacency matrix
    # {<node> => {target => weight}, <node> => {...}}
    @graph = {}
    @nodes = Set.new
	@opened_set = {}
	@closed_set = Set.new
	@icons_set = Set.new
	@epsilon = 1
	@heuristics = nil
	@edge_costs_detected = nil 
	## this thing must return true if our move subject to changes in world state, else otherwise
	@get_changed_edges =  nil
	## ths thing return changed edges
	@costs = nil
	## this thing return cost matrix
	@pred = nil
	##this thing calls function with previous nodes
	@succ = nil
	## this thing calls function with next nodes
	
	@g = {}
	@rhs = {}
  end
  def set_heuristics(code)
    @heuristics = code[:h]
	@costs = code[:costs]
  end
  
  
  # s= source, t= target, w= weight
  def add_vertex(s)
    if (not @graph.has_key? s)
      @graph[s] = {t => w}
    else
      @graph[s][t] = w
    end
    @nodes.merge [s,t]
  end
 
  def h(s1, s2)
    return @heuristics.call(s1, s2) if not @heuristics.nil?
	return INFINITY
  end

  def c(s1, s2)
    return @costs.call(s1, s2) if not @costs.nil?
	return INFINITY
  end
  
  def pred(s1)
    return @pred.call(s1) if not @pred.nil?
	[]
  end
  
  def succ(s1)
    return @succ.call(s1) if not @succ.nil?
	[]
  end
  
  
  

  
  def key(s, s_start)
    if (@g[s] > @rhs[s]) 
      [@rhs[s] + @epsilon * h(s_start, s), @rhs[s]] 
	else
	  [@g[s] + h(s_start,s), @g[s]]
	end
  end
  
  def min(x, &b)
    min_result = INFINITY
	s_dot = nil
    for s in x do
	  min_s = b.call(s)
	  if min_s < min_result
	    min_result = s
		s_dot = s
	  end
	end
	return s_dot
  end
  
  def update_state(s, s_start, s_goal)
    if not @g.has_key?(s)
	  @g[s] = INFINITY
	end
	if (s != s_goal)
	  s_current = min(succ(s)){|s_dot| c(s ,s_dot) + @g[s_dot] }
	  @rhs[s] = c(s, s_current) + @g[s_current]
	end
	if (@opened_set.include?(s))
	  @opened_set.remove(s)
	end
	if (@g[s] != @rhs[s])
	  if (not @closed_set.include?(s))
	    @opened_set[s] = key(s, s_start)
	  else 
	    @icons_set << s
	  end
	end
  end
  def compute_or_improve_path(s_start, s_goal)
    s_current = min(@opened_set.keys){|s| key(s, s_start)}
    while ( key(s_current, s_start) < key(start_s, s_start) or rhs[s_start] != g[s_start])
	  @opened_set.remove(s_current)
	  if (@g[s_current] > @rhs[s_current])
	    @g[s_current] = @rhs[s_current]
		@closed_set << s_current 
		pred(s_current).merge(s_current).each do |s_dot|
		   update_state(s_dot)
	    end 
	  else
	    @g[s_current] = INFINITY
		pred(s_current).merge(s_current).each do |s_dot|
		  update_state(s_dot)
		end
	  end
	  s_current = min(@opened_set.keys){|s| key(s, s_start)}
	end
  end	

  def mainfunc(s_start, s_goal)
	  @g[s_start] = INFINITY
	  @rhs[s_start] = INFINITY
	  @g[s_goal] = INFINITY
	  @rhs[s_goal] = 0
	  @epsilon = 1
	  @opened_set = {}
#	  @closed_set
#	  @icons_set
	  @opened_set[s_goal] = key(s_goal, s_start)
	  compute_or_improve_path(s_start, s_goal)
	  #publish current e suboptimal solution
	  
  end

end