#######################################################
# This script is for creating a table in cassandra    #
#######################################################

from cassandra.cluster import Cluster


cassandra_cluster = Cluster(['54.71.115.97','35.166.209.97','35.166.89.248','34.218.167.77'])
cassandra_session = cassandra_cluster.connect('oilwell')
cassandra_session.execute('DROP TABLE IF EXISTS oil_production;')
cassandra_session.execute('CREATE TABLE oil_production (dt date, well_name text, oil_bbl float, water_bbl float, gas_mscf float, pressure float, PRIMARY KEY (well_name,dt)) WITH CLUSTERING ORDER BY (dt ASC);')
cassandra_session.execute('DROP TABLE IF EXISTS monthly_oil;')
cassandra_session.execute('CREATE TABLE monthly_oil (well_name text, month text, oil_avg float, PRIMARY KEY (well_name, month)) WITH CLUSTERING ORDER BY (month DESC);')
cassandra_session.execute('DROP TABLE IF EXISTS well_pressure;')
cassandra_session.execute(' CREATE table well_pressure (id int, well_name text, dt text, pressure_1 int, pressure_2 int, pressure_3 int, pressure_4 int, PRIMARY KEY(dt, id))WITH CLUSTERING ORDER BY (id ASC);')
