## Librerías
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('font',family='Times New Roman')
from matplotlib.font_manager import FontProperties

### Parámetros para serie trigonométrica de Fourier
w0 = np.pi/2.0                # W0
N  = 1000                     # Número de elementos para sumatoria
l  = 1000                     # Elementos máximo para vector de tiempo
t  = np.linspace(0,12,l)      # Vector de tiempo
f  = np.zeros(l)

### Coeficientes de serie trigonométrica de Fourier

for i in range(0,l,1):
    a0 = 7/2
    suma = 0.0
    for n in range(1,N+1,1):
        an = (1.0/(n*w0)**2.0)*(np.cos(n*w0)-1)
        bn = (np.sin(n*w0)/(n*w0)**2.0)-(1.0/(n*w0))
        suma = suma + (an*np.cos(n*w0*t[i]) + bn*np.sin(n*w0*t[i]))
    #End for
    f[i] = a0/2 + suma
#End for

## Graficando la solución
font = FontProperties()
font.set_style('italic')

plt.plot(t,f,'-',color='red',lw = 1.5,label='Solución')
plt.legend(frameon=True,fontsize=14,loc=0,ncol=1)
plt.yticks(fontsize=16,fontproperties=font)
plt.xlabel("t [s]",fontsize = 18, color = 'black',fontproperties=font)
plt.ylabel("f(t)",fontsize = 18, color = 'black',fontproperties=font)
plt.ylim(0,2*f.max())
titulog = 'Serie_trigonometrica_Fourier.png'
plt.grid(True)
plt.grid(color = '0.5', linestyle = '--',linewidth = 1)
plt.xticks(fontsize=16,rotation=0,fontweight='bold',fontproperties=font)
plt.yticks(fontweight='bold',fontproperties=font)
plt.savefig(titulog, dpi = 600)
plt.show()