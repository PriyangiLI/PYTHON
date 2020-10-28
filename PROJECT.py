
import sqlite3
import time

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('Charac.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from CHARACTERS"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Name: ", row[0])
            print("AGE: ", row[1])
            print("NATIONALITY: ", row[2])
            print("GENDER: ", row[3])
            print("PROFESSION: ", row[4])
            print("REAL OR NOT: ", row[5])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()
#DISPLAYING CHRACTERS
from Tkinter import *

def onclick():
   pass

root = Tk()
text = Text(root)
time.sleep(3)
text.insert(INSERT, "The list of characters:\n")
text.insert(INSERT, "Virat Kohli\n")
text.insert(INSERT, "Hannah Montana\n")
text.insert(INSERT, "Narendra Modi\n")
text.insert(INSERT, "Avatar Aang\n")
text.insert(INSERT, "Thor Odinson\n")
text.insert(INSERT, "Woody from Toy Story\n")
text.insert(INSERT, "Cinderella\n")
text.insert(INSERT, "Dorothy Gale\n")
text.insert(INSERT, "Harry Potter\n")
text.insert(INSERT, "Sherlock Holmes\n")
text.insert(INSERT, "Justin Beiber\n")
text.insert(INSERT, "Chhota Bheem\n")
text.insert(INSERT, "Donald Trump\n")
text.insert(INSERT, "P V Sindhu\n")
text.pack()
root.mainloop()

class Person():
    def __init__(self,fname,age,nationality,gender,profession):
        self.fname=fname
        self.age=age
        self.nationality=nationality
        self.gender=gender
        self.profession=profession
    def nat(self):
      ln=[]
      if self.nationality=='Indian':
        ln.append(self.fname)

vk=Person('Virat Kohli',31,'Indian','Male','Cricketer')
hm=Person('Hannah Montana',14,'American','Female','Singer')
nm=Person('Narendra Modi',70,'Indian','Male','Prime Minister')
av=Person('Avatar Aang',13,'Japanese','Male','Fictional Character')
th=Person('Thor Odinson',1500,'American','Male','Fictional Character')
w=Person('Woody from Toy Story',17,'American','Male','Fictional Character')
pc=Person('Cinderella',19,'American','Female','Fictional Character')
dg=Person('Dorothy Gale',12,'American','Female','Fictional Character')
hp=Person('Harry Potter',17,'British','Male','Fictional Character')
sh=Person('Sherlock Holmes',60,'British','Male','Fictional Character')
jb=Person('Justin Beiber',26,'Canadian','Male','Singer')
cb=Person('Chhota Bheem',13,'Indian','Male','Fictional Character')
dt=Person('Donald Trump',74,'American','Male','President')
pv=Person('P V Sindhu',25,'Indian','Female','Badminton Player')



Person.nat(vk)
l=[]

l.append(hm.fname)
l.append(vk.fname)
l.append(nm.fname)
l.append(av.fname)
l.append(th.fname)
l.append(w.fname)
l.append(pc.fname)
l.append(dg.fname)
l.append(hp.fname)
l.append(sh.fname)
l.append(jb.fname)
l.append(cb.fname)
l.append(dt.fname)
l.append(pv.fname)
print(len(l))
print(l)
start=input("Do you want to start the game??? ")
if start=='yes':
 while len(l)!=1:
  nat=input("Is your character Indian?")
  if nat=='yes':
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Donald Trump' in l: l.remove('Donald Trump')
    
  else:
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Narindra Modi' in l: l.remove('Narendra Modi')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  age=input("Is your character above 50 years of age? ")
  if age=='yes':
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  else:
    if 'Narendra Modi' in l: l.remove('Narendra Modi')
    if 'Thor Odison' in l: l.remove('Thor Odison')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Donald Trump' in l: l.remove('Donald Trump')
  gene=input('Is your character a female? ')
  if gene=='yes':
    if 'Thor Odison' in l: l.remove('Thor Odison')
    if 'Narendra Modi' in l: l.remove('Narendra Modi')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'Donald Trump' in l: l.remove('Donald Trump')
  else:
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  pro=input("Is your character real? ")
  if pro=='yes':
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
  else:
    if 'Narendra Modi' in l: l.remove('Narendra Modi')
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Donald Trump' in l: l.remove('Donald Trump')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  gen=input('Is your character a male? ')
  if gen=='yes':
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  else:
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Narendra Modi' in l: l.remove('Narendra Modi')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'Donald Trump' in l: l.remove('Donald Trump')
  age1=input("Is your character under the age of 45? ")
  if age1=='yes':
    if 'Narendra Modi' in l: l.remove('Narendra Modi')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Donald Trump' in l: l.remove('Donald Trump')
  else:
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  fic=input("Is your character a fictional character? ")
  if fic=='yes':
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Narendra Modi' in l: l.remove('Narendra Modi') 
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Donald Trump' in l: l.remove('Donald Trump')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  else:
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
  bal=input("Is your character bald? ")
  if bal=='yes':
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Narendra Modi' in l: l.remove('Narendra Modi')
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'Donald Trump' in l: l.remove('Donald Trump')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  else:
     if 'Avatar Aang' in l: l.remove('Avatar Aang')
  pr=input("Is your character a disney princess? ")
  if pr=='yes':
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Narendra Modi' in l: l.remove('Narendra Modi')
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'Donald Trump' in l: l.remove('Donald Trump')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  else:
    if 'Cinderella' in l: l.remove('Cinderella')
  bk=input("Is your character from a famous book? ")
  if bk=='yes':
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Narendra Modi' in l: l.remove('Narendra Modi')
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Cinderella' in l: l.remove('Cinderella')
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'Donald Trump' in l: l.remove('Donald Trump')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  else:
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Sherlock Holmes' in l: l.remove('Sherlock Holmes')
    print(l)
  si=input("Is your character a singer? ")
  if si=='yes':
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Narendra Modi' in l: l.remove('Narendra Modi')    
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Cinderella' in l: l.remove('Cinderella')    
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Donald Trump' in l: l.remove('Donald Trump')
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  else:
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
  si=input("Is your character an American? ")
  if si=='yes':
    if 'Justin Beiber' in l: l.remove('Justin Beiber')
    if 'Virat Kohli' in l: l.remove('Virat Kohli')
    if 'Chhota Bheem' in l: l.remove('Chhota Bheem')
    if 'Harry Potter' in l: l.remove('Harry Potter')
    if 'Avatar Aang' in l: l.remove('Avatar Aang')
    if 'Narendra Modi' in l: l.remove('Narendra Modi')        
    if 'P V Sindhu' in l: l.remove('P V Sindhu')
  else:
    if 'Woody from Toy Story' in l: l.remove('Woody from Toy Story')
    if 'Thor Odinson' in l: l.remove('Thor Odinson')
    if 'Cinderella' in l: l.remove('Cinderella')      
    if 'Dorothy Gale' in l: l.remove('Dorothy Gale')    
    if 'Donald Trump' in l: l.remove('Donald Trump')
    if 'Hannah Montana' in l: l.remove('Hannah Montana')
    
print(l)
import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END,l)
tk.mainloop()
print(*l, sep = ", ")
