####CODE FOR OXY gAS TURBINE STATGE1 THERMAL HTC LOAD APPLICATION
model=ExtAPI.DataModel.Project.Model
geom=model.Geometry
mesh=model.Mesh
materials = model.Materials
#analysis = model.Analyses[0]
#as we have two analysis 1. static structural and another Thermal analysis we have used Analyses[1] else we can use Analyses[0]
analysis = model.Analyses[1]
solution = analysis.Solution
connnections=model.Connections
conn1=model.Connections

#stage3 htc details

datalist= ['D_01','D_02','D_03','D_04','D_05','D_06','D_06 bis','D_07','D_08','D_09','D_10','D_11','D_11 bis','D_12','D_13','D_13 bis','D_14','D_15','D_16','F_06','F_07','F_08','LS_1','LS_2','LS_3','C_22','C_23','C_24','C_25','C_16','D_28','Tip_01','Tip_02']
HTC=[1912,291,634,18387,17665,13147,53056,739,62928,16606,1721,13592,26971,362,10021,39294,2352,256,1338,17528,29308,37167,13840,13107,11795,900,1620,367,18075,442,4135,30014,24094]
Tbulk=[404.4,404.4,404.4,404.4,404.4,577.6,577.6,582.2,582.2,582.2,582.2,582.2,582.2,582.2,582.2,582.2,582.2,498.4,498.4,859.5,859.5,859.5,815.1,814.9,788.8,584.9,733.4,577.6,404.4,404.4,404.4,815.1,788.8]
Pressure=[21.36,19.8,18.23,17.29,17.34,20.48,20.48,19.5,19.5,18.16,18.16,18.16,18.16,17.96,17.96,17.96,17.69,16.85,16.85,20.67,20.49,19.55,18.14,17.41,16.61,21.5,20.67,20.48,21.36,21.36,19.8,18.14,16.61]



gp=model.NamedSelections.Children
gplist=[]
for i in gp:
    gplist.append(i.Name)


# to get the index value from the datalist using the contact naming list -gplist  , the output of this code is idx list shown above.   
indices_dict = {}
for i, num in enumerate(datalist):
    if num in indices_dict:
        indices_dict[num].append(i)
    else:
        indices_dict[num] = [i]
ids = [indices_dict[num][0] for num in gplist if num in indices_dict]


    
for idx in ids:    

    convection1=analysis.AddConvection()
    cv=DataModel.GetObjectsByName(datalist[idx])[0]
    convection1.Location= cv
    convection1.FilmCoefficient.Output.SetDiscreteValue(0, Quantity(HTC[idx], "W m^-1 m^-1 C^-1"))
    convection1.AmbientTemperature.Output.SetDiscreteValue(0, Quantity(Tbulk[idx], "C"))
    convection1.Name=str('HTC_'+cv.Name)


for idx in ids:    

    pressure=analysis.AddPressure()
    cv=DataModel.GetObjectsByName(datalist[idx])[0]
    pressure.Location= cv
    pressure.Magnitude.Output.SetDiscreteValue(0, Quantity(Pressure[idx], "MPa"))

    pressure.Name=str('Pr_'+cv.Name)

###!!!

##
##/prep7
##csys,6
##NSEL,S,NODE,,    84240
##NSEL,A,NODE,,    59564
##nrotat,all


##cp,1,uy,84240,59564
##csys,0
##ALLSEL
##/SOLU
