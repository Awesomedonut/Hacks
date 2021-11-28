
import os 
import sys
from flask import Flask, render_template, url_for, redirect

sys.path.insert(1, './src/')
from cli import *
import time
import webbrowser
import threading
app = Flask(__name__)


emotion_str=['Happy','sad','Surprise','Anger','Confusion']






# return the max emotion 
def getMaxEmotion(lst):

  max = lst[0]
  maxIndex=0
  lenght = len(lst)

  for i in range(0,lenght):
    if lst[i] >= max:
      maxIndex=i
      max=lst[i]
      
  return emotion_str[maxIndex]

# emotionVAl=val()
emotionVAl=[1,0.5,0.9,0.8,0]

Maxemotion = getMaxEmotion(emotionVAl)



class Person:
  def __init__(self, title, desc):
    self.title = title
    self.desc = desc



# represents the movie class

array=[]

path = './static/csvFiles/'+Maxemotion+'.csv'

print(path)

file = open(path)
first_line = file.readline()
data_list = first_line.strip().split(',')

p1=Person( data_list[0],data_list[1])
array.append(p1)



first_line = file.readline()
data_list = first_line.strip().split(',')

p2=Person( data_list[0],data_list[1])
array.append(p2)


first_line = file.readline()
data_list = first_line.strip().split(',')

p3=Person( data_list[0],data_list[1])
array.append(p3)


for i in array:
  print(i.title)
  print(i.desc)










@app.route("/")
def index():
    return render_template('landing.html')

@app.route('/home')
def upload_file():
    return render_template('emotion.html', log=emotionVAl, array=array)

@app.route("/contrib")
def con():
    return render_template("contributors.html")
    
app.run(debug=True)









# -----------------------------------------------------------------------------

# progressMeter = "[#######"
# completionMeter = "[###################################################"  # 51

# for i in range(100):
#     if (i == 1 or i == 10 or i == 30):
#         time.sleep(0.6)
#     print('\r'+progressMeter, end='')
#     time.sleep(0.15)
#     if(i == 25):
#         time.sleep(1.5)

#     progressMeter += '#'
#     if progressMeter == completionMeter:
#         break

# print(']')

# def appRUN():
#     print("opening server .....")
#     progressMeter = "[#######"
#     completionMeter = "[#####################"  # 51

#     for i in range(100):


#         print('\r'+progressMeter, end='')
#         time.sleep(0.2)
       
#         progressMeter += '#'
#         if progressMeter == completionMeter:
#             break
#     app.run()

# def openWindow():
#     time.sleep(5)
#     webbrowser.open_new('http://127.0.0.1:5000/')
 
# t1 = threading.Thread(target=appRUN)
# # t2 = threading.Thread(target=openWindow)
# t1.start()
# # t2.start()
# t1.join()
# # t2.join()




