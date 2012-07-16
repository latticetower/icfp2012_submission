require 'set'

class DStarLiteSolver
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
	@nodes_changes_detected = nil 
	## this thing must return true if our move subject to changes in world state, else otherwise
	@get_changed_nodes =  nil
	## ths thing return changed edges
	@costs = nil
	## this thing return cost matrix
	@pred = nil
	##this thing calls function with previous nodes
	@succ = nil
	## this thing calls function with next nodes
	@eql_function = nil
	@g = {}
	@rhs = {}
  end
  
  def set_heuristics(code)
    @heuristics = code[:h]
	@costs = code[:costs]
	@pred = code[:pred]
	@succ = code[:succ]
	@nodes_changes_detected = code[:change_function]
	@get_changed_nodes = code[:changed_nodes]
	@eql_function = code[:eql]
  end
  
  def eql?(u,v)
    return @eql_function.call(u,v) if not @eql_function.nil?
    false
  end
  
  def changes_detected?
    @nodes_changes_detected.call() if @nodes_changes_detected
	false
  end
  def changed_nodes
    @get_changed_nodes.call if @get_changed_nodes
	[]
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
    [minimal(g(s), @rhs[s]) + h(s_start, s), minimal(g(s), @rhs[s])] 
  end
  def minimal(x, y)
    return x if x < y
	y
  end  
  def min(x, &b)
  return nil if x.size<1
	s2 = x[0]
    x.each do |s1| 
	  if b.call(s1, s2)
	      s2 = s1
	  end 
	end
	s2
  end
  def g(s_dot)
    if not @visited_set.include?(s_dot)
	  @visited_set << s_dot
	  @g[s_dot] = INFINITY
	else
	  return @g[s_dot]
	end
	INFINITY
  end
  
  def update_state(s, s_start, s_goal)
	  if not @visited_set.include?(s)
		  @visited_set << s
		  @g[s] = INFINITY
	  end

	if (not eql?(s, s_goal))
	  s_current = min(succ(s)) { |s1, s2| c(s, s1) + g(s1) < c(s, s2) + g(s2)}
	  
	  @rhs[s] =  c(s, s_current) + g(s_current)
	# p "  changed rgs[#{s}]=#{@rhs[s]}"
#	  p " #{s} #{succ(s).collect{|x| {x => c(s,x)+ g(x)}}} s_current  = #{s_current}, rhs = #{@rhs[s]}"
	end
	if @opened_set.include? (s)
	   @opened_set.delete(s)
	end
	if (g(s) != @rhs[s]) and not @opened_set.include?(s)
		@opened_set[s] = key(s, s_start)
	end 

  end
  
  def compute_shortest_path(s_start, s_goal)
  
    s_current = min(@opened_set.keys){|s1, s2| less_keys(@opened_set[s1], @opened_set[s2])}
    while (less_keys(@opened_set[s_current], key(s_start, s_start)) or @rhs[s_start] != @g[s_start])
	  @opened_set.delete(s_current)
	  
	  if (g(s_current) > @rhs[s_current])
	    @g[s_current] = @rhs[s_current] 
		pred(s_current).each do |s_dot|
		   update_state(s_dot, s_start, s_goal)
	    end 
	  else
	    @g[s_current] = INFINITY
		pred(s_current).each do |s_dot|
		  update_state(s_dot,s_start,s_goal)
		end
		update_state(s_current,s_start,s_goal)
	  end
	  s_current = min(@opened_set.keys){|s1, s2| less_keys(@opened_set[s1], @opened_set[s2])}
	end
  end	

  def less_keys(pair1, pair2)
return false if (pair1 == nil)
return false if (pair2 == nil)
    return true if (pair1[0] < pair2[0]) 
	return false if (pair1[0] > pair2[0])
	return true if (pair1[1] < pair2[1]) 
	false
  end
  
  def mainfunc(s_start, s_goal)
	  @g[s_start] = INFINITY
	  @rhs[s_start] = INFINITY
	  @g[s_goal] = INFINITY
	  @rhs[s_goal] = 0

	 @visited_set = Set.new
	  @opened_set = {}



	  @opened_set[s_goal] = key(s_goal, s_start)

#while true do
  compute_shortest_path(s_start, s_goal)
  s1_length = @g[s_start]
s1 = s_start
  p s1
  if @g[s_start] < INFINITY
  while s1 != s_goal do
   s1 = @g.select{|k, v| v == s1_length - 1 and pred(k).include?(s1) }.keys.first
   s1_length = s1_length-1
   p s1
  end
  else 
  p "A"
  end
  if changes_detected?
    changed_nodes.each do |u|
      update_state(u, s_start, s_goal)
    end	  
	  #publish current e suboptimal solution
	  #update_state(u, s_start,s_goal)
 # else 
 # p 'return '
 # p @g
 # p @rhs
 # gets()
 #   return   
 # end
  

end
end

end