# Vianney ANANI 
#Pour de Dé
result = 0

for h1 in range(1, 7):
  #######################################
    for h2 in range(1, 7):
      ##########################################
        for h3 in range(1, 7):  
          ####################################
            for h4 in range(1, 7):  
              #################################
                for h5 in range(1, 7):
                  ##############################
                    if h1 + h2 + h3 + h4 + h5 == 20:
                        result += 1 

print("Nombre de façons d'obtenir 20 :", result)
