from modelos.contenedor import Contenedor
from modelos.caja import Caja
from packing.optimizador import Optimizador



contenedor = Contenedor(
    "40FT"
)


opt = Optimizador(
    contenedor
)



opt.agregar_caja(
    Caja(10,5,5)
)


opt.agregar_caja(
    Caja(15,6,5)
)


opt.agregar_caja(
    Caja(8,8,5)
)



opt.calcular()



for x in opt.reporte():

    print(x)