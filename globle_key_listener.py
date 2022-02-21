from tkinter import EXCEPTION
from tracemalloc import stop
from pynput.keyboard import Key, Listener
import pynput
import audio
import voice_mode_ui
import re
import struct
import binascii
import threading
from PyQt5.QtCore import QSettings

global modifirekeys
modifirekeys = ["Key.alt_l","Key.alt_gr"]
currentkey = []
currentkey1 = []
currentreleaskey = []
global calledtimes
calledtimes = [0]
global workdone
workdone = [True]
global alphabet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
global keyboardnumbers
keyboardnumbers = ['0','1','2','3','4','5','6','7','8','9']
on_releasetimes = [0]

def itwasdone(doneornot):
    calledtimes[0] = 0
    currentkey.clear()
    workdone[0] = doneornot 

def starlistener_old(hotkeydict,selecteddiviceinderx,volume=1):
    def callplayaudio(pressedkey):
        print(pressedkey)
        calledtimes[0] +=1
        if calledtimes[0] < 2:
            afilename = hotkeydict[pressedkey]
            print(volume)
            audio.playaudio_class().playaudio(filename=afilename,deviceindex=selecteddiviceinderx,chunksize=1024,volume=volume)
        else:
            print("done")
            calledtimes[0] = 0
            currentkey.clear()



    def on_press(key):
        strkey = str(key)
        try:
            if not(re.search("Key.",str(key))):
                print(keyboardnumbers)
                if not(str(key).replace("'","") in keyboardnumbers):
                    print(str(key))
                    formatedkeyhex = str(key).replace("'\\x","")
                    formatedkeyhex = formatedkeyhex.replace("'","")
                    print(formatedkeyhex)
                    print(int(formatedkeyhex, 16))
                    keyindex = int(formatedkeyhex, 16)
                    if keyindex < 27:
                        print('{0} pressed'.format(
                        alphabet[keyindex-1]))
                        strkey = str(alphabet[keyindex-1])
        except Exception as e:
            print(e)
            print('{0} pressed'.format(
            key))    
            strkey = str(key) 
        
        currentkey.append(strkey)   
        print(str(key))
        
        if currentkey[0] in modifirekeys:
            print("must be have second or more keys") 
            if strkey != currentkey[0] and len(currentkey) <2:
                currentkey.append(strkey)
        else:
            currentkey.clear()
            currentkey.append(strkey)        
        print(currentkey)    
    def on_release(key):
        print('{0} release'.format(
            key))
        if len(currentkey) >1:
            try:
                print(currentkey[0]+"+"+str(currentkey[1]).replace("'","") +" "+str(hotkeydict.keys()))
                for i in hotkeydict.keys():
                    if currentkey[0]+"+"+str(currentkey[1]).replace("'","") == i:
                        print("play audio of key "+str(i))
                        callplayaudio(str(i))    
                currentkey.clear()
            except:
                pass
        """if key == Key.esc:
            # Stop listener
            return False"""

    # Collect events until released
    print(str(hotkeydict))
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
  
def starcapture_hk_old():

    def setstophk(hkey):
        settingval = QSettings("Dragon Voide Mode","settings vals")
        captrdkey = hkey[0]+"+"+hkey[1]
        settingval.setValue("stophotkey",captrdkey)
        print(captrdkey)

    def on_press(key):
        strkey = str(key)
        try:
            if not(re.search("Key.",str(key))):
                print(keyboardnumbers)
                if not(str(key).replace("'","") in keyboardnumbers):
                    print(str(key))
                    formatedkeyhex = str(key).replace("'\\x","")
                    formatedkeyhex = formatedkeyhex.replace("'","")
                    print(formatedkeyhex)
                    print(int(formatedkeyhex, 16))
                    keyindex = int(formatedkeyhex, 16)
                    if keyindex < 27:
                        print('{0} pressed'.format(
                        alphabet[keyindex-1]))
                        strkey = str(alphabet[keyindex-1])
        except Exception as e:
            print(e)
            print('{0} pressed'.format(
            key))    
            strkey = str(key)
        
        currentkey1.append(strkey)   
        print(currentkey1)
        
        if currentkey1[0] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l"]:
            print("must be have second or more keys") 
            if strkey != currentkey1[0] and len(currentkey1) <2:
                currentkey1.append(strkey)
        else:
            currentkey1.clear()
            currentkey1.append(strkey)        
        print(str(currentkey1)+"on press")    
    def on_release(key):
        print('{0} release'.format(
            key))
        if len(currentkey1) >1:
            try:
                print(currentkey1[0]+"+"+str(currentkey1[1]).replace("'",""))
                setstophk(currentkey1)
                print(str(currentkey1)+"on releas")
                #return currentkey    
                currentkey.clear()
            except:
                pass
        """if key == Key.esc:
            # Stop listener
            return False"""

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def starlistener(hotkeydict,selecteddiviceinderx,volume=1):

    def callplayaudio(pressedkey):
        print(pressedkey)
        calledtimes[0] +=1
        if calledtimes[0] < 2:
            afilename = hotkeydict[pressedkey]
            print(volume)
            audio.playaudio_class().playaudio(filename=afilename,deviceindex=selecteddiviceinderx,chunksize=1024,volume=volume)
        else:
            print("done")
            calledtimes[0] = 0
            currentkey.clear()



    def on_press(key):
        strkey = str(key)
        print(strkey)
        if str(key) in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]:
            currentkey.append(str(key))
            if len(currentkey)>1:
                if str(key)!=currentkey[0] and str(key) in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"] and len(currentkey)<2:
                    currentkey.append(str(key))
                    print(currentkey)

                '''else:
                    print(currentkey)
                    currentkey.clear()'''    
            else:
                print(currentkey)

    def on_release(key):
        print('{0} release'.format(
            key))
        settingval = QSettings("Dragon Voide Mode","settings vals")
        on_releasetimes[0] += 1
        print(str(currentkey)+"onreleasss")
        currentreleaskey.append(str(key))
        try:
            if len(currentreleaskey)>0:
                if not(currentreleaskey[len(currentreleaskey)-1] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]):

                    if len(currentkey) > 0:
                        print('ok')
                        if currentkey[0] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"] and len(currentkey)<2:
                            currentkey.append(str(key))
                            print(currentkey)
                            print('1')
                            for i in hotkeydict.keys():
                                if currentkey[0]+"+"+str(currentkey[1]).replace("'","") == i:
                                    print("play audio of key "+str(i))
                                    callplayaudio(str(i))    
                            if currentkey[0]+"+"+str(currentkey[1]).replace("'","") == settingval.value("stophotkey"):
                                print("stop")
                                currentkey.clear()
                            else:
                                currentkey.clear()     
                            currentkey.clear()

                            currentkey.clear()
                            currentreleaskey.clear()
                        elif currentkey[1] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"] and len(currentkey)<3:
                            currentkey.append(str(key))
                            print(currentkey)
                            print('2')
                            print(len(currentkey))
                            currentkeystr = currentkey[0]+"+"+str(currentkey[1])+"+"+currentkey[2].replace("'","")
                            print(currentkeystr+" curenkeystr")
                            
                            for i in hotkeydict.keys():
                                print(currentkeystr+" curenkeystronloop")
                                if currentkeystr == i:
                                    print("play audio of key "+str(i))
                                    callplayaudio(str(i))
                                if currentkeystr == settingval.value("stophotkey"):
                                    print("stop")
                                    currentkey.clear()
                                else:
                                    currentkey.clear() 
                            currentkey.clear()
                            currentreleaskey.clear()
                    if len(currentkey)!=0:        
                        if not(currentkey[len(currentkey)-1] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]):
                            print(currentkey)
                            print('3')
                        else:
                            currentkey.clear()
                            currentreleaskey.clear() 
        except Exception as e:
            print(e)                            
        '''try:
            if currentkey[0] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]:
                print("must be have second or more keys")
                if len(currentkey)>1:
                    if currentkey[1] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]:
                        print("must be have another key1")
                        if currentkey[1] == currentkey[0]:
                            print(currentkey)
                            currentkey.clear()
                        if len(currentkey)>2:
                            if currentkey[2] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]:
                                print("must be have another key2")
                                if currentkey[2] == currentkey[0] or currentkey[2] == currentkey[1] :
                                    print(currentkey)
                                    currentkey.clear()
                            else:
                                print(str(currentkey)+" is valid n ready to use")
                                for i in hotkeydict.keys():
                                    if currentkey[0]+"+"+str(currentkey[1])+"+"+currentkey[2].replace("'","") == i:
                                        print("play audio of key "+str(i))
                                        callplayaudio(str(i))
                                if currentkey[0]+"+"+str(currentkey[1])+"+"+currentkey[2].replace("'","") == settingval.value("stophotkey"):
                                    print("stop")
                                    currentkey.clear()
                                else:
                                    currentkey.clear()              
                                currentkey.clear()
                                #currentkey.clear()

                    else:
                        print(str(currentkey)+" is valid n ready to use")
                        for i in hotkeydict.keys():
                            if currentkey[0]+"+"+str(currentkey[1]).replace("'","") == i:
                                print("play audio of key "+str(i))
                                callplayaudio(str(i))    
                        if currentkey[0]+"+"+str(currentkey[1]).replace("'","") == settingval.value("stophotkey"):
                            print("stop")
                            currentkey.clear()
                        else:
                            currentkey.clear()     
                        currentkey.clear()

                               
            else:
                currentkey.clear()
        except Exception as e:
            print(e)
            currentkey.clear() '''       
    # Collect events until released
    print(str(hotkeydict))
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def starcapture_hk():
    
    def setstophk(hkey):
        settingval = QSettings("Dragon Voide Mode","settings vals")
        if len(hkey)>2:
            captrdkey = hkey[0]+"+"+hkey[1]+"+"+hkey[2]
        elif len(hkey)>1:
            captrdkey = hkey[0]+"+"+hkey[1]
        elif len(hkey) == 1:
            captrdkey = hkey[0]        
        settingval.setValue("stophotkey",captrdkey.replace("'",""))
        print(captrdkey)

    def on_press(key):
        strkey = str(key)
        '''try:
            if not(re.search("Key.",str(key))):
                print(keyboardnumbers)
                if not(str(key).replace("'","") in keyboardnumbers):
                    print(str(key))
                    formatedkeyhex = str(key).replace("'\\x","")
                    formatedkeyhex = formatedkeyhex.replace("'","")
                    print(formatedkeyhex)
                    print(int(formatedkeyhex, 16))
                    keyindex = int(formatedkeyhex, 16)
                    if keyindex < 27:
                        print('{0} pressed'.format(
                        alphabet[keyindex-1]))
                        strkey = str(alphabet[keyindex-1])
        except Exception as e:
            print(e)
            print('{0} pressed'.format(
            key))    
            strkey = str(key)
        
        currentkey1.append(strkey)   
        print(currentkey1)
        
        if currentkey1[0] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l"]:
            print("must be have second or more keys") 
            if strkey != currentkey1[0] and len(currentkey1) <2:
                currentkey1.append(strkey)
        else:
            currentkey1.clear()
            currentkey1.append(strkey)        
        print(str(currentkey1)+"on press") '''   
    def on_release(key):
        print('{0} release'.format(
            key))
        on_releasetimes[0] += 1
        currentkey1.append(str(key))
        if currentkey1[0] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]:
            print("must be have second or more keys")
            if len(currentkey1)>1:
                if currentkey1[1] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]:
                    print("must be have anothre key")
                    if len(currentkey1)>2:
                        if currentkey1[2] in ["Key.alt_l","Key.alt_gr","Key.ctrl_l","Key.shift"]:
                            print("must be have anothre key")
                        else:
                            print(str(currentkey1)+" is valid n ready to use")
                            setstophk(currentkey1)
                            currentkey1.clear()

                else:
                    print(str(currentkey1)+" is valid n ready to use")
                    setstophk(currentkey1)
                    currentkey1.clear()        


    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def startcapture_hk_call():
    t1 = threading.Thread(target=starcapture_hk)
    t1.start()
