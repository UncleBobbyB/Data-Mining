#Data Cleaning
##Unreal Point
Remove points without the range of maximum longitude and latitude.
##Duplicate timing points
If several points are in the same track within the same time, keep the first
point and remove the rest.
##High speed points
Remove points having speed larger than 90km/h.
##Long distance points
Remove points whose distance between adjacent points are larger than 2km.
##Laggy points
Remove points whose time spans with adjacent points are longer than 10min.
##Stationary points
Remove tracks whose point moves less than 50m within 30min.
##Waiting points
Remove points who appears to be waiting for passengers (according to passenger
status).
