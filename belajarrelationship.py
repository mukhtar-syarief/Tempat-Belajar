from tkinter.tix import INTEGER
from sqlalchemy import create_engine, Integer, Column, String, Text, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from flask import Flask

app = Flask(__name__)

Base = declarative_base()

engine = create_engine('postgresql+psycopg2://postgres:m03kht4r1999@127.0.0.1:5432/postgres')

####################################
#########----ONE TO MANY----########
####################################
class Writer(Base):
    __tablename__ = "writers"
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    email = Column(Text, unique = True)
    catalogs = relationship("Catalog", backref = "writer")

    def __repr__(self):
        return f"Writer(id = {self.id}, name = {self.name}, email = {self.email})"


class Catalog(Base):
    __tablename__ = "catalogs"
    id = Column(Integer, primary_key =True)
    writer_id = Column(Integer, ForeignKey("writers.id",ondelete="CASCADE"))
    headline = Column(Text)
    konten = Column(Text)


    def __repr__(self):
        return f"Catalog(id = {self.id}, writer = {self.writer.name}, headline = {self.headline}, konten = {self.konten})"


katalog2 = Catalog(headline = "Mbuh bingung", konten = "Oponeh kontene tambah bingung", writer = Writer(name = "suyono"))

writer3 = Writer(name = "Sasmidi", email = "sasmidi@gmail.com")
writer4 = Writer(name = "Sumaji", email = "sumaji@gmail.com")
writer5 = Writer(name = "Sugandi", email = "sugandi@gmail.com")



katalog3 = Catalog(headline = "One to Many", konten = "Coba cara lain", writer = writer3)
katalog5 = Catalog(headline = "One to Many", konten = "Sudah Berhasil..", writer = writer5)


print(writer3.catalogs)
print(katalog5.writer.name)
print(katalog2.writer.email)


####################################
####--ONE TO MANY & MANY TO ONE--###
####################################
class Penjahit(Base):
    __tablename__ = "penjahit"
    id = Column(Integer, primary_key = True)
    nama = Column(Text)
    alamat = Column(Text)
    pakaian = relationship("Pakaian", back_populates = "penjahit")

    def __repr__(self):
        return f"Penjahit(id = {self.id}, nama = {self.nama}, alamat = {self.alamat}"

class Pakaian(Base):
    __tablename__ = "pakaian"
    id = Column(Integer, primary_key =True)
    penjahit_id = Column(Integer, ForeignKey("penjahit.id"))
    jenis = Column(Text, unique = True)
    harga = Column(Integer)
    penjahit = relationship("Penjahit", back_populates = "pakaian")

    def __repr__(self):
        return f"Pakaian(id = {self.id}, jenis = {self.jenis}, harga ={self.harga})"

Session = sessionmaker(bind=engine)
s = Session()

Base.metadata.create_all(engine)

sulis = Penjahit(nama="Sulistyowati", alamat = "Jln. Tanjung 123")
gamis = Pakaian(jenis="Gamis", harga=100000, penjahit = sulis)

kemeja = Pakaian(jenis="Kemeja", harga=80000, penjahit = sulis)
kemeja2  = Pakaian(jenis="Kemeja", harga = 90000)
# satrio = Penjahit(nama = "Satrio", alamat = "Jln. Balitar 50", pakaian = kemeja2)

s.add_all([sulis,gamis,kemeja,kemeja2])
s.commit()

print(gamis.penjahit.nama)
print(gamis.penjahit.alamat)
print(kemeja.penjahit.nama)
print(sulis.pakaian)
print(satrio.pakaian.jenis)
# s.add(katalog5)
# s.commit()
