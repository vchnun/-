n, cap, time = [3, 100, 20]
skills = [[10,8,5],[5,2,1],[20,25,8]]
val = [s[0] for s in skills]
com = [s[1] for s in skills]
# nums = [time//s[2] for s in skills]
# 初始cd为0?
time -= 1
nums = [time//s[2]+1 for s in skills]
del skills
vals = []
csms = []
'''
# 直接转化为01
for i in range(n):
    # k = 0
    # while((2**k-1) <= nums[i]):
    for _ in range(nums[i]):
        vals.append(val[i])
        csms.append(com[i])'''
# 二进制分解
for i in range(n):
    x = nums[i]
    k = 1
    while(x > k):
        vals.append(val[i]*k)
        csms.append(com[i]*k)
        x -= k
        k *= 2
    else:
        vals.append(val[i]*x)
        csms.append(com[i]*x)
# 

del val
del com
dp = [0]*(cap+1)
for i in range(len(vals)):
    for j in range(cap, csms[i]-1,-1):
        dp[j] = max(dp[j-csms[i]] + vals[i], dp[j])
print(dp[cap])