
#lets send ourselves to rpi 
tar -zcvf ../../../rpi_api.tar.gz ../../../rpi_api
scp ../../../rpi_api.tar.gz pi@YOUR.RPI.IP.ADDRESS:

#now extract it on remote machine 
#ssh pi@YOUR.RPI.IP.ADDRESS  tar -xfv rpi_api.tar




