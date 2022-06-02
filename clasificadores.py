# Inteligencia Artificial para la Ciencia de los Datos
# Implementación de clasificadores 
# Dpto. de C. de la Computación e I.A. (Univ. de Sevilla)
# ===================================================================

# --------------------------------------------------------------------------
# Autor(a) del trabajo:
#
# APELLIDOS: OUAHMED
# NOMBRE: Bilel
#
# Segundo componente (si se trata de un grupo):
#
# APELLIDOS: VARNEROT
# NOMBRE: Antoine
# ----------------------------------------------------------------------------

import numpy as np
import sys
sys.path.append("/jugar_tenis.py")
from jugar_tenis import X_tenis, y_tenis

# ====================================================
# PARTE I: IMPLEMENTACIÓN DEL CLASIFICADOR NAIVE BAYES
# ====================================================

# I.1) Implementación de Naive Bayes

class NaiveBayes():
    def __init__(self,k=1):
        self.k=k

#On choisit une structure dictionnaire pour pouvoir retrouver les probabilités par la suite
    def entrena(self,X,y):
        probas = {}
        for i in range(len(X)):
            if not (y[i] in probas):
                probas[y[i]] = 1
                probas["cond " + y[i]] = [{} for t in range(np.shape(X)[1])]
            else:
                probas[y[i]] += 1
            for j in range(np.shape(X)[1]):
                if not (X[i][j] in probas["cond " + y[i]][j]):
                    probas["cond " + y[i]][j][X[i][j]] = 1
                else:
                    probas["cond " + y[i]][j][X[i][j]] += 1
                print(probas)
        return probas


a = NaiveBayes()
b = a.entrena(X_tenis, y_tenis)
print(b)


#     def clasifica_prob(self,ejemplo):

#         ......

#     def clasifica(self,ejemplo):

#         ......
