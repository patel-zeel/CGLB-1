import os

dataset = 'Wilson_pol'
seeds = [1001, 1002, 1003]

main = 'python plotcli.py metrics '
parts = []
for seed in seeds:
    parts.append(f'./logs/keops/Wilson_pol/cglb-Matern32-1024-fp64/{seed}/logs.json')

print(main + ' '.join(parts))
os.system(main + ' '.join(parts))