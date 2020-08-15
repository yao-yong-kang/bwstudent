HOSTNAME='127.0.0.1'
POST=3306
USERNAME='root'
PASSWORD=''
DATABASE='student'

url_db="mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8mb4"\
    .format(USERNAME,PASSWORD,HOSTNAME,POST,DATABASE)

SQLALCHEMY_DATABASE_URI=url_db
SQLALCHEMY_TRACK_MODIFICATIONS=False
debug=True