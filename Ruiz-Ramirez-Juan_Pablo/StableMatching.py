def gale_shapley(hombres, mujeres, preferencias_m, preferencias_w):
   pareja_de_w = {}

   siguiente_propuesta = {hombre: 0 for hombre in hombres}
   while True:
      m = None
      for m in hombres: 
         if m not in pareja_de_w.values() and siguiente_propuesta[m] < len(preferencias_m[m]): 
            break
      else:
            m = None
      if m is None:
          break
      # resto del algoritmo
      w = preferencias_m[m][siguiente_propuesta[m]]
      siguiente_propuesta[m] += 1
      if w not in pareja_de_w:
         pareja_de_w[w] = m
      else:
         m_actual = pareja_de_w[w]
         if (preferencias_w[w].index(m) < preferencias_w[w].index(m_actual)):
            pareja_de_w[w] = m
   pareja_invertida = {hombre: mujer for mujer, hombre in pareja_de_w.items()}
   return pareja_invertida

"""preferencias_m = {
   "Xavier": ["Amy", "Bertha", "Clare"],
   "Yancey": ["Bertha", "Amy", "Clare"],
   "Zeus": ["Amy", "Bertha", "Clare"],
   }

preferencias_w = {
   "Amy": ["Yancey", "Xavier", "Zeus"],
   "Bertha": ["Xavier", "Yancey", "Zeus"],
   "Clare": ["Xavier", "Yancey", "Zeus"],
   }
Hombres = ["Xavier", "Yancey", "Zeus"]
Mujeres= ["Amy", "Bertha", "Clare"]"""

hombres = [] 
mujeres = [] 
preferencias_m = {} 
preferencias_w = {}
N, quien_propone = input().split()
N = int(N)
for _ in range(N):
    partes = input().split()
    hombre = partes[0]
    preferencias = partes[1:]
    preferencias_m[hombre] = preferencias
    hombres.append(hombre)

for _ in range(N):
   partes2 = input().split()
   mujer= partes2[0]
   preferencias = partes2[1:]
   preferencias_w[mujer] = preferencias
   mujeres.append(mujer)

if quien_propone == 'w': 
   resultado = gale_shapley(mujeres, hombres, preferencias_w, preferencias_m) 
   resultado = {hombre: mujer for mujer, hombre in resultado.items()}
else: 
   resultado = gale_shapley(hombres, mujeres, preferencias_m, preferencias_w)

for hombre in hombres:
    print(f"{hombre} {resultado[hombre]}")

#Ordenar la salida de forma alfabetica 
