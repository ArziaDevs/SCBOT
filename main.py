from scratchclient import ScratchSession
from time import sleep
from random import randint
session = ScratchSession("atom_x_10", "не дам пароль")
connection = session.create_cloud_connection(612229554)
while True:
    connection.set_cloud_variable("CLOUD1", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    connection.set_cloud_variable("CLOUD2", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    connection.set_cloud_variable("CLOUD3", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    connection.set_cloud_variable("CLOUD4", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    connection.set_cloud_variable("CLOUD5", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    connection.set_cloud_variable("CLOUD6", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    connection.set_cloud_variable("CLOUD7", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    connection.set_cloud_variable("CLOUD8", randint(0,9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    connection.set_cloud_variable("CLOUD9", randint(0,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
