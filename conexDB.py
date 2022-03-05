from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///./teste.db"
#SQLALCHEMY_DATABASE_URL ="postgres://gyxefczrdfplqw:065b83736788a744ea8bef5a4aa6898bff2041a1f86c0cb7cdc2dff6bc69e207@ec2-52-45-83-163.compute-1.amazonaws.com:5432/dcr5rnvabn8a53"
#SQLALCHEMY_DATABASE_URL = "mysql://root:''@localhost:3306/produto"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False, })



