import itertools
import math

# 演示 itertools.permutations (排列)
print("=== 排列 (Permutations) ===")
data = ['A', 'B', 'C']
print(f"数据: {data}")

# 所有元素的排列
perms = list(itertools.permutations(data))
print(f"所有元素的排列: {perms}")
print(f"排列数: {len(perms)}")

# 部分元素的排列
perms_2 = list(itertools.permutations(data, 2))
print(f"选取2个元素的排列: {perms_2}")
print(f"选取2个元素的排列数: {len(perms_2)}")

print("\n=== 组合 (Combinations) ===")
# 演示 itertools.combinations (组合)
combs = list(itertools.combinations(data, 2))
print(f"选取2个元素的组合: {combs}")
print(f"组合数: {len(combs)}")

# 演示 itertools.combinations_with_replacement (可重复组合)
combs_rep = list(itertools.combinations_with_replacement(data, 2))
print(f"选取2个元素的可重复组合: {combs_rep}")
print(f"可重复组合数: {len(combs_rep)}")

print("\n=== 使用 math.factorial 计算排列组合数 ===")
# 使用数学公式计算
n = len(data)
r = 2

# 排列数公式: P(n,r) = n! / (n-r)!
perm_count = math.factorial(n) // math.factorial(n-r)
print(f"使用公式计算排列数 P({n},{r}) = {perm_count}")

# 组合数公式: C(n,r) = n! / (r! * (n-r)!)
comb_count = math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
print(f"使用公式计算组合数 C({n},{r}) = {comb_count}")