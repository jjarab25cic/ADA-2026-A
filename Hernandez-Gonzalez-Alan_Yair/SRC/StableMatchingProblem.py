#-------------- Modificación para lectura de tiempo y guardao en archivo --------------
import time 
from pathlib import Path
base_dir = Path(__file__).parent
folder = base_dir / "execution_times.txt"
output_file = Path(folder)
start_time = time.perf_counter()
#-------------- Lectura de número de parejas y orden --------------
ng = input().split()
n = int(ng[0])
g = ng[1]
menOrder = []
womenOrder = []
menPreferences = {}
womenPreferences = {}
#-------------- Lectura de preferencias --------------
for i in range(n):
  line = input().split()
  menPreferences[line[0]] = line[1:] 
  menOrder.append(line[0])

for i in range(n):
  line = input().split()
  womenPreferences[line[0]] = line[1:]
  womenOrder.append(line[0])
#------- Función principal -------
def getStableMatching(group1, group2):
  freePerson = list(group1.keys())
  nextPerson = {}
  nextPerson = {p:0 for p in freePerson}

  engagedPerson1 = {}
  engagedPerson2 = {}

  while(freePerson):
    person1 = freePerson[0]    

    if nextPerson[person1] >= n:
      freePerson.pop(0)
      continue

    person2 = group1[person1][nextPerson[person1]]
    nextPerson[person1] += 1

    #Caso 1: persona libre
    if person2 not in engagedPerson2:
      engagedPerson1[person1] = person2
      engagedPerson2[person2] = person1
      freePerson.pop(0)
    else:
      #Caso 2: persona con compromiso
      currentPerson = engagedPerson2[person2]
      if group2[person2].index(person1) < group2[person2].index(currentPerson):
        engagedPerson1.pop(currentPerson, None)
        freePerson.append(currentPerson)
        engagedPerson1[person1] = person2
        engagedPerson2[person2] = person1 
        freePerson.pop(0)  
  #Salida del algorimo
  if g == 'm':
    for man in menOrder:
        print(man, engagedPerson1[man])
  else:
      for woman in womenOrder:
        print(woman, engagedPerson1[woman])
#Invocación a la función principal
if g == 'm':
  getStableMatching(menPreferences, womenPreferences)
else:
  getStableMatching(womenPreferences, menPreferences)

#-------------- Modificación para la escritura del tiempo --------------
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
file_exists = output_file.exists()
with open(output_file, "a") as f:
    if not file_exists:
        f.write("Numero de parejas, Tiempo de ejecución\n")
    f.write(f"{n}, {elapsed_time:.8f} \n")
