from pymongo import MongoClient
from neo4j import GraphDatabase
conn=MongoClient('mongodb://root:example@157.230.15.68:27017/?authMechanism=DEFAULT')


#driver=GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "admin"))


driver=GraphDatabase.driver("neo4j://157.230.15.68:7687", auth=("neo4j", "Admin12345"))