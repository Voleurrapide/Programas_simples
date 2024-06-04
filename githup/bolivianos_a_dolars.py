print("1)comprar dolars")
print("2)vender dolars")
r=int(input("-->"))
di=int(input("dame el monto que quieres cambiar --> "))
if r == 1:
    dso=di*6.96
    dsp=di*9.40
    dsod=di/6.96
    dspd=di/9.40
    print("nesesitas ",dso," Bs. en el tipo de cambio official para obtener",dsod," y en el paralelo ",dsp,"Bs. para obtener ",dspd,"la diferensia entre paralelo y official es",dsp-dso,"Bs.")
elif r == 2:
    dso=di/6.86
    dsp=di/8.72
    dsod=di*6.96
    dspd=di*9.40
    print("los dolares offisiales estan a ",dsod," Bs. para offreser ",dso," dolars y el paralelo a ",dspd," Bs. para offreser ",dsp," Bs. con una diferensia de ",dsp-dso," entre el paralelo y el official en el benefisios")