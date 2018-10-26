# -*- uft-8 -*-

from numpy import random, exp, sqrt, pi
from scipy import integrate

#Média e desvio padrão das variabeis aleatórios
S_med, S_dev= 60., 10.
Y1_med, Y1_dev = 1., 0.2
Y2_med, Y2_dev = 2.0, 0.1
a0_med = 1.0
C1_med, C1_dev = 5.203e-15, 2.587e-15
m_med, m_dev = 3.5, 0.3
ac = 50

#Núnemro de iterações para Monte Carlo
n = 10
#Variáveis aleatórias do tipo Lognormal

a = random.exponential(1.0, n)

#Variável aleatória do tipo normal(Gaussiana)

S = random.normal(S_med, S_dev, n)
m = random.normal(m_med, m_dev, n)

#Variáveis aleatórias do tipo Lognormal


Y1 = random.lognormal(Y1_med, Y1_dev, n)
Y2 = random.lognormal(Y2_med, Y2_dev, n)
C1 = random.lognormal(C1_med, C1_dev, n)

f = []
for i in range(n):
    ff = integrate.fixed_quad(a, a[i], ac, 1/(exp(Y1[i]*(a[i]/50)**Y2[i])*sqrt(2*pi))**m[i], )

    f.append(ff)
