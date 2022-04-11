import base64
import sqlalchemy
from sqlalchemy import create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import BLOB, TIMESTAMP
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:Chopras1!@localhost/studentdb', echo=True)
Base = declarative_base()

q = "CREATE TABLE IF NOT EXISTS camera(image_id int primary key, camera_id int, images blob, time_stamp timestamp)"


class CameraQuery(Base):
    __tablename__ = 'CameraQuery'
    image_id = Column(Integer, primary_key=True)
    camera_id = Column(Integer)
    images = Column(BLOB)
    time_stamp = Column(TIMESTAMP)

    def __repr__(self):
        return "<Camera(image_id='%s', camera_id='%s', images='%s', time_stamp='%s')>" % (
            self.image_id, self.camera_id, self.images, self.time_stamp)


def insertQuery(*id, cameraName, image, date):
    fetchedImg = base64.b64encode(image)
    ed_user = CameraQuery(camera_id=cameraName, images=fetchedImg, time_stamp=date)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    session.execute(q)
    session.add(ed_user)
    session.commit()

# Open a file in binary mode
# file = open('C:/Users/Harman/OneDrive/Pictures/App/1.jpg', 'rb').read()

# We must encode the file to get base64 string
# file = base64.b64encode(file)


# ed_user = Camera(image_id=1, camera_id=2, images=file, time_stamp='1999-01-15 8:00:00')
# Session = sessionmaker(bind=engine)
# Session.configure(bind=engine)
# session = Session()

# session.execute(q)
# session.add(ed_user)
# session.commit()
