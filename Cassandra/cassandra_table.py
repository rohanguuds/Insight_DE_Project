#######################################################
# This script is for creating a table in cassandra    #
#######################################################

from cassandra.cluster import Cluster


cassandra_cluster = Cluster(['54.71.115.97','35.166.209.97','35.166.89.248','34.218.167.77'])
cassandra_session = cassandra_cluster.connect('oilwell')
cassandra_session.execute('DROP TABLE IF EXISTS oil_production;')
CREATE TABLE oil_production (dt date, well_name text, oil_bbl float, water_bbl float, gas_mscf float, pressure float, PRIMARY KEY (well_name,dt)) WITH CLUSTERING ORDER BY (dt ASC);
