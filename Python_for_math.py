# Non-inverted Summing Amp 
V1 = 20
V2 = 10
V3 = 20
R1 = 1
R2 = 1
R3 = 1
Rf = 1
Rg = 1

denomenator = ((1/R1) + (1/R2) + (1/R3))
numerator = ((V1/R1) + (V2/R2) + (V3/R3))
Vout = (1 + (Rf/Rg))*(numerator/denomenator)
print(f"Vout: {Vout}")