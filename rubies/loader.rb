
infile = File.new("C-small-practice.in", "r")
outfile = File.new("C-out.txt", "w")

a1 = []
b1 = []
 b1h = Hash.new
  a1h = Hash.new
  
SubData = Hash.new

def maxSub(a, b, sA, sB)
 subKey = sA.to_s + '_'  + sB.to_s
 return SubData[subKey] if SubData.has_key?(subKey)
 
 if a.nil? or b.nil?
  SubData[subKey] = 0
  return 0
 end
 
 if a.size == 0 or b.size == 0
  SubData[subKey] = 0
  return 0
 end
  m1=0
 
 
 m2 = maxSub(a[1, a.size - 1], b[1, b.size - 1], sA+1,sB+1)
 m3 = maxSub(a, b[1, b.size - 1], sA,sB+1)
 m4 = maxSub(a[1,a.size-1], b, sA+1,sB)
 
 if a[0][0] == b[0][0]
   mAB = [a[0][1], b[0][1]].min
   a[0][1]  = a[0][1] - mAB
   b[0][1]  = b[0][1] - mAB
   akey = (a[0][1] == 0 ? 1 : 0)
   bkey = (b[0][1] == 0 ? 1 : 0)
   m1 = mAB + maxSub(a[akey, a.size - akey].clone, 
         b[bkey, b.size-bkey].clone, sA + akey, sB + bkey) 
   a[0][1]  = a[0][1] + mAB
   b[0][1]  = b[0][1] + mAB
 
 end
 
 m1234 = [m1,m2,m3,m4].max
 SubData[subKey] = m1234
return m1234
 end



T = infile.gets().to_i
T.times do |i|
#testcases

  SubData.clear
  str = infile.gets()
  arr = str.scan(/\d+/)
  n = arr.shift.to_i
  m = arr.shift.to_i
  
  a1.clear
  a1h.clear
  str = infile.gets() #next line 2n
  arr = str.scan(/\d+/)
  n.times do |j|
    a = arr.shift.to_i
	aKey = arr.shift
	if a1h.key?(aKey) 
	  a1h[aKey] = a1h[aKey] + a
	else
	  a1h[aKey] = a
	end
    a1 << [aKey, a]
  end
  
  b1.clear
  b1h.clear
  str = infile.gets() #next line 2n
  arr = str.scan(/\d+/)
  m.times do |j|
    b = arr.shift.to_i
	bKey = arr.shift
	if b1h.has_key?(bKey) 
	  b1h[bKey] = b1h[bKey] + b
	else
	   b1h[bKey] = b
	end
	b1 << [bKey, b]
  end
  
  sum = 0
  a1.delete_if{|a|  !( b1h.has_key?(a[0]))}
  b1.delete_if{|b|  !( a1h.has_key?(b[0]))}
  if a1.size >0 
  ##
  
     n = a1.size
	 m = b1.size
	 n.times do |i|
 	    m.times do |j|
		  maxSub( a1[n-i, i], b1[m-j, j], n-i, m-j)	
		end
	 end
  sum=maxSub( a1, b1, 0, 0)
  end
  #outfile.puts("Case ##{i+1}: "+ a1.map{ |i|  "#{i}" }.join(' '))
  # outfile.puts("Case ##{i+1}: "+ b1[1,b1.size-1].map{ |i|  "#{i}" }.join(' '))
 
  outfile.puts("Case ##{i+1}: #{sum}")
end
infile.close
outfile.close