


dbname=mydatabase
uname=myuser
pgsversion=1.5

#########################

###load shapefile 
shapefilename=WTR_Valves_sm #leave off .shp 
SRID=900913


###########################################


#LOAD SOME DATA

shp2pgsql -s $SRID -g "the_geom" -W UTF-8 $shapefilename.shp  > $shapefilename.sql

psql -d $dbname -U postgres -f $shapefilename.sql
psql -d $dbname -U postgres -c "GRANT ALL ON $shapefilename TO $uname;"


###########################################









