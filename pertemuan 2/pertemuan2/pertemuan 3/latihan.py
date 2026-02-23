class Person:
  def __init__(self,nama,jeniskelamin,umur):
    self.nama = nama
    self.jeniskelamin = jeniskelamin
    self.umur = umur

class karyawan(Person):
   def __init__(self,nama,jeniskelamin,umur,gaji):
     super().__init__(nama,jeniskelamin,umur)   
     self.__gaji =gaji #protected

   def get_gaji(self):
    return self.__gaji
     
class rekening:
    def __init__(self,Norekening,Pin):
     self.Norekening = Norekening
     self.__Pin = Pin 

    def get_pin(self):
      return self.__Pin
    
    def set_pin(self,pinbaru):
      self.__Pin = pinbaru
p1 = karyawan("alsa","perempuan",18,10000)
print(p1.nama)
print(p1.jeniskelamin)
print(p1.umur)
print(p1.get_gaji())
p2 = rekening("1234567891","123456")
print(p2.get_pin())











 







