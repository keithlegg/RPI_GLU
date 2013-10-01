import kl_rpi_base



class rpi_terminal:
   def __init__(self):
      pass

   def update(self):
      foo = kl_rpi_base.kl_rpi_api()
      foo.write_gps_file('./gps_latlon.txt') #write to web directory 
      #foo.dump_postgis('./gps_latlon.txt') #


##############################
foo = rpi_terminal()
foo.update()



