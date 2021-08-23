from blueqat import Circuit

# I gate
Circuit().i[0].m[:].run(shots=100)
# >> Counter({'0': 100})
# X gate
Circuit().x[0].m[:].run(shots=100)
# >> Counter({'1': 100})
# Y gate
Circuit().y[0].m[:].run(shots=100)
# >> Counter({'1': 100})
# Z gate
Circuit().z[0].m[:].run(shots=100)
# >> Counter({'0': 100})
# H gate
Circuit().h[0].m[:].run(shots=100)
# >> Counter({'1': 55, '0': 45})
# S gate
Circuit().s[0].m[:].run(shots=100)
# >> Counter({'0': 100})
# S† gate
Circuit().s[0].m[:].run(shots=100)
# >> Circuit().sdg[0].m[:].run(shots=100)

# 量子ビット0と量子ビット1にHゲートを適用
Circuit().h[0, 1].m[:].run(shots=1000)
# >> Counter({'01': 257, '11': 257, '00': 249, '10': 237})

# 量子もつれ
# # cnotゲート
Circuit().h[0].cx[0, 1].m[:].run(shots=1000)
# >> Counter({'00': 516, '11': 484})

# 足し算
Circuit().h[0, 1].cx[0, 2].cx[1, 2].ccx[0, 1, 3].m[:].run(shots=1000)
# >> Counter({'1010': 263, '0000': 259, '0110': 241, '1101': 237})