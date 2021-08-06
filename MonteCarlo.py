from scipy import stats
import numpy as np

varx, vary = 1, 1
x, y = [], []
#k = 0


###criar uma lista para que o erro seja menor que 0.05%
while abs(varx) > 0.025/150 and abs(vary)>0.025/150: #o intervalo de testes foi baseado em tentativa e erro

    x1,y1 = np.random.uniform(-1,1,2000000), np.random.uniform(-1,1,2000000)#cria os pontos nos eixos x e y
    x1, y1 = x1.tolist(), y1.tolist()                                   
    x, y = x + x1, y +y1
    varx, vary = stats.sem(x), stats.sem(y)


#como o loop sempre irá criar um x1 e y1, não corre o risco de len(x) != len(y)
#agora que o erro está ajustado, vamos calcular quantos% dos pontos estão dentro do círculo
dentro, fora, total = 0, 0, 0
for i in range(len(x)):
    if x[i]**2 + y[i]**2 >  1**2: fora = fora+1
    if x[i]**2 + y[i]**2 <  1**2: dentro = dentro+1
    total = total + 1


#agora, sabendo que a área do quadrado é 4, multiplicarei por ((dentro)/(total))
area_circulo = 4*(dentro/total)
valor_pi = (area_circulo)
print('o valor de pi é :', valor_pi)
