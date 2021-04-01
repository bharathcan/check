print("Give Input")
Area=input("Enter Area in m^2:")
TubePressure=input("Enter TubePressure in kg/cm^2:")
ShellPressure=input("Enter ShellPressure in kg/cm^2:")



dif=0

dif=float(TubePressure)-float(ShellPressure)

if dif<0:
  dif=-dif
  print(dif)
  

  
 # C_B=(0.27015*dif+1.2214*Ps+0.56483*Pt+95.225)*A+15621

  #Base_Cost

  C_B=(0.27015*dif+1.2214*float(ShellPressure)+0.56483*float(TubePressure)+95.225)*float(Area)+15621
  print("Base_Cost =",C_B,"EUR")
  
  Type=str(input("Enter Type[BEM ,BKU,BEU]:"))
  Selected="BEM"
  Selected2="BEU"
  Selected3="BKU"
  
  if Type==Selected:
      F_m=0.00194*dif+0.00250*float(TubePressure)+0.00663*float(ShellPressure)+0.000478*float(Area)+2.04
      F_d=1
      F_t=1
      FOB_Cost=C_B*F_t*F_m*F_d
      print("FOB_COST of 1st Quarter(2011)=",FOB_Cost,"EUR")
      print("FOB_COST of 1st Quarter(2014)=93000 EUR")

  elif Type==Selected2:
      
      F_m=0.00194*dif+0.00250*float(TubePressure)+0.00663*float(ShellPressure)+0.000478*float(Area)+2.04
      F_d=1
      F_t=0.8373
      FOB_Cost=C_B*F_t*F_m*F_d
      print("FOB_COST of 1st Quarter(2011)=",FOB_Cost,"EUR")
      print("FOB_COST of 1st Quarter(2014)=93000 EUR")

  elif Type==Selected3:
       
       F_m=0.00194*dif+0.00250*float(TubePressure)+0.00663*float(ShellPressure)+0.000478*float(Area)+2.04
       F_d=1
       F_t=0.282*float(ShellPressure)/(float(TubePressure)+float(ShellPressure))+0.00226*float(ShellPressure)-0.000113*float(Area)+0.997
       print(F_t)
       FOB_Cost=C_B*F_t*F_m*F_d
       print("FOB_COST of 1st Quarter(2011)=",FOB_Cost,"EUR")
       print("FOB_COST of 1st Quarter(2014)=93000 EUR")

      
  else:
      print("You selected wrong type")
       
      
  
      
