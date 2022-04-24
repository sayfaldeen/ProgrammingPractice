#!/usr/local/bin/julia-1.7

# Script to implement DP for finding fibonacci sequences in Julia

memo = Dict(0=>0, 1=>1, 2=>1)

function DPFib(n::Int)
	if n in keys(memo)
		return memo[n]
	elseif n-2 in keys(memo) && n-1 in keys(memo)
		memo[n] = memo[n-1] + memo[n-2]
	elseif n-2 in keys(memo)
		memo[n-1] = DPFib(n-1)
		memo[n] = memo[n-1] + memo[n-2]
	else
		memo[n] = DPFib(n)
	end

	return memo[n]
end

println([DPFib(n) for n in 0:50])
