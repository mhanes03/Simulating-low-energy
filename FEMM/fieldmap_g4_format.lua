--bf_output.lua--
r1=0
r2=30
dr=10
 
z1=100
z2=200
dz=10
 
ni = (r2-r1)/dr+2
nj = (z2-z1)/dz+2
 
handle=openfile("B_g4format_2.dat","w")

write(handle,"# Fieldmap from Femm\n")
write(handle,"param current=5.0\n")
write(handle,"cylinder Z0=100 nR=5 dR=10 nZ=12 dZ=10\n")
write(handle,"extendZ flip=Br\n")
write(handle,"data\n")
 
for j=0,nj-1,1 do
  for i=0,ni-1,1 do
  r=r1+i*dr
  z=z1+j*dz
  A,B1,B2=mo_getpointvalues(r,z)
  write(handle,r,",",z,",",B1,",",B2,"\n")
 end
end
 
closefile(handle)

