import scipy.stats

T = int(input())

for t in range(1, T+1):
	W, H, L, U, R, D = [int(i) for i in input().split()]
	
	ans = 0.0
	if D != H:
		
		ans += scipy.stats.binom.cdf(L-2, D+L-2, 0.5)
	
	if R != W:
		
		ans += scipy.stats.binom.cdf(U-2, R+U-2, 0.5)
		
	print("Case #%d: %f" % (t, ans))