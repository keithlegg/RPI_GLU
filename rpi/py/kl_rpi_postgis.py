import psycopg2
import kl_rpi_base
import os



###############################


"""
class pg_dataloader:

    def __init__(self): 
       self.SYS_BIN = 'C:/Program Files/PostgreSQL/9.2/bin'

    def load_shapefile(self):
       pass

"""
   
###############################


class pg_datalink:
    def __init__(self):
       self.CONFIG       = kl_rpi_base.kl_rpi_config()
       self.CONFIG.read_cfg()
       ###
       self.TABNAME = self.CONFIG.ATTR_PGDB_TBNAME  #database table name 
       self.DBNAME  = self.CONFIG.ATTR_PGDB_DBNAME  #'robot'
       self.USER    = self.CONFIG.ATTR_PGDB_USER    #'postgres'
       self.PASSWD  = self.CONFIG.ATTR_PGDB_PASSWD  #'password'
       ###
       #self.SCHEMA
       #self.SRID
       #self.GEOM
       #self.GID
   
   
    ##############################
    def show_env(self):
       print ('#DB   '+ self.DBNAME)
       print ('#TAB  '+ self.TABNAME)
       print ('#USR  ' +self.USER)
       print ('#PASS '+self.PASSWD)
	   
    ##############################
    #MAKE A TABLE
    #DELETE A TABLE?
    #MAKE A COLUMN
    #RUN A QUERY
    #                          # 


    #                          # 
    #     #HIGHER LEVEL#       # 
    #CREATE_GEOM (PT,LINE,POLY)
    #BUFFER 
    #SAVE TO SHAPEFILE
    #RENDER TO "ROBO_META_TXT" ->MAPSERVER/OPENLAYERS
    """
    # MAKE A POINT
    INSERT INTO bot_test(p_id, geom)
      VALUES(2, ST_GeomFromText('POINT(-71.060316 48.432044)', 4326));
    ######################
    #	MAKE A LINE
     INSERT INTO bot_test(p_id, geom)
      VALUES(3, ST_GeomFromText('LINESTRING (30 10, 10 30, 40 40)', 4326 ) );
 
    #####################
     INSERT INTO bot_test(p_id, geom)
      VALUES(2, ST_GeomFromText(ST_MakeLine(ST_MakePoint(1,2), ST_MakePoint(3,4)), 4326));
 
    """
    ##############################
     #MACRO TO BUILD A QUERY
    def writeback_query(self,type): 
        output = ''       
        if (type=='pg_line'): 
            output  =  'SELECT ST_AsText(ST_MakeLine(ST_MakePoint(1,2), ST_MakePoint(3,4)));'


        return output
 
    ##############################
      #MACRO TO BUILD A QUERY
    def standard_query(self,type): 
         output = ''
         #####
         if(type=='testgid'):
            output= "SELECT * FROM "+self.ACTIVE_TABLE+" WHERE gid<100"
         #####

         ##### 
         return output

 
    ##############################
    def test_conn(self):  
        #conn = "host='localhost' dbname='moose' user='postgres' password='password'"
        con_str = ('host=localhost dbname='+self.DBNAME+' user='+self.USER+' password='+self.PASSWD)
        conn = psycopg2.connect(con_str)
        cursor = conn.cursor()
        print "Connected!\n"
        cursor.close()
        conn.close()


  
    ##############################
    #cursor.execute("SELECT * FROM parcels WHERE gid<100")
    #records = cursor.fetchall()

    def test_read(self):  
        con_str = ('host=localhost dbname='+self.DBNAME+' user='+self.USER+' password='+self.PASSWD)
        conn = psycopg2.connect(con_str)
        cursor = conn.cursor()
        cursor.execute(self.standard_query('testgid') )
        records = cursor.fetchall()
        print(records[0][1])

        cursor.close()
        conn.close()

    ##############################
    def test_write(self):
        con_str = ('host=localhost dbname='+self.DBNAME+' user='+self.USER+' password='+self.PASSWD)
        conn = psycopg2.connect(con_str)
        cursor = conn.cursor()
        cursor.execute(self.writeback_query('pg_line') )

        #Data = name, url, id, point, polygon
        #print Data
        #cur.execute(SQL, Data)
        #conn.commit()
        cursor.close()
        conn.close()
    ##############################
    """
    def test(self):
            conn = psycopg2.connect('dbname='+self.DBNAME+' user='+self.USER+' password='+self.PASSWD)
	    cur = conn.cursor()
	    #SQL = 'INSERT INTO my_table (name, url, id, point_geom, poly_geom) VALUES (%s,%s,%s,%s,%s);'
	    #Data = name, url, id, point, polygon
	    #print Data
	    #cur.execute(SQL, Data)
	    #conn.commit()
	    cur.close()
	    conn.close()
    """

#########################


#foo = pg_datalink()
#foo.connect()

