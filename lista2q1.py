# -*- uft-8 -*-

from numpy import random, exp, sqrt, pi, ln
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

Y1_ksi = sqrt(ln(1+(Y1_dev/Y1_med)**2))
Y1_lambda = ln(Y1_med) - 1/2*Y1_ksi**2

Y2_ksi = sqrt(ln(1+(Y2_dev/Y2_med)**2))
Y2_lambda = ln(Y2_med) - 1/2*Y2_ksi**2

C1_ksi = sqrt(ln(1+(Y1_dev/C1_med)**2))
C1_lambda = ln(C1_med) - 1/2*C1_ksi**2

Y1 = random.lognormal(Y1_ksi, Y1_lambda, n)
Y2 = random.lognormal(Y2_ksi, Y2_lambda, n)
C1 = random.lognormal(C1_ksi, C1_lambda, n)
