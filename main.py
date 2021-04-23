#Strings(Text) ausgeben
print("Hey du bist super!")                 #In "" stehen Strings

#Variablen Integers (Zahlen) und Strings(Text) zuweisen und ausgeben
a = 2**85                                   # Mit ** rechnet man hoch 2^85
print (a)                                   # Zahlen brauchen keine "" man nennt sie Integers oder Float

v = "deine mutter stinkt nicht"
print (v)

#Verschiedene Dinge ausgeben wie Variablen mit verschiedenem Inhalt und Strings
print (a , "lol" , v)

#Listen (Arrays) anlegen und ausgeben
liste1 = []                                 #Eine leere Listenvariable kann auch angelegt werden
liste1 = [1,2,3,4]                          #Eine Variable der eine Liste(Array) zugewiesen wird mit []  
                                            #,(komma) trennen die "Elemente" voneinander             
print (liste1)                              #Ausgabe einer ganzen Liste

print (liste1[0])                           #Ausgabe einer bestimmten Stelle des Arrays hier 0 also wird "1" ausgeg.
print (liste1 + [5,6,7,8])                  #Ausgabe des Arrays, gleichzeitig gibt man ein undefiniertes Array aus

#Elemente in Arrays austauschen/hinzufügen - Merke Strings lassen sich nicht einfach austauschen
liste1[1] = liste1[2] + liste1[3]           #Setzt an Stelle 1 des Arrays das Element aus Stelle 2 + Stelle 3
print (liste1)                              #Aus 1,2,3,4 wird so 1,7,3,4
liste1 = liste1 + [5,6,7,8]                 #Hinzufügen von Elementen zum Array
print (liste1)

#Mit der Append Funktion Elemente anfügen
liste1.append(42)                           #Hängt eine 42 an die 9te Stelle
print (liste1)
liste1.append("deine mutter")               #Hängt einen String "deine mutter" an das Array an
print (liste1)

#Verschiedene EINZELNE Stellen des Arrays ausgeben, Negative Zahlen zählen von hinten
print (liste1[1] , liste1[-1])              #In den Klammern steht die Stelle des Arrays her 1 und die 1ste von hinten

#Arrays in Arrays gehen auch
liste2 = ["a" , "b"]
liste3 = [liste1,liste2]                    #Dem Array liste3 werden die Elemente von Liste1 und Liste2 zugewiesen
print (liste3)                              #[[1, 7, 3, 4, 5, 6, 7, 8, 42, 'deine mutter'], ['a', 'b']]
                                            #Man sieht es sind 2 Arrays in einem Array [[][]]

#Strings über mehrere Zeilen schreiben mit 3 Anführungszeichen"
print ("""1 Zeile
2 Zeile
3 Zeile""")

#Man kann auch Strings mit Operatoren (*/+-) bearbeiten
stringsmalzahl = 3 * "hi" + " 4 mal OMFG = " + 4 * "OMFG "
print (stringsmalzahl)
#Oder wie hier wenn wir zwei Strings addieren und "hihoooooooooooooooo" ausgeben
t = "hi"
z = "hooooooooooooooooooooooo"
print (t + z)

#Verschiede Stellen eines Arrays VON-BIS ausgeben #Zeilensprünge in der Ausgabe Funktion gehen mit "\n"
print ("\n" + stringsmalzahl[0:3])          #Stelle 0-3
print ("\n" + stringsmalzahl[:3])           #Anfang-3
print ("\n" + stringsmalzahl[3:])           #Stelle 3-Ende
print ("\n" + stringsmalzahl[-3:])          #3t letzte Stelle bis Ende
print ("\n" + stringsmalzahl[-8:])          #8t letzte Stelle bis Ende
print ("\n" + stringsmalzahl[:-4])          #Anfang bis 4t letzte  Stelle

#Dinge ersetzen kann man bei Strings indem man den neuen Teil als String + den restlichen Teil des Arrays addiert
stringsmalzahl = "TEST" + stringsmalzahl[4:-1]# "hihihi" wird hier zu "TESThi"
print ("\n" + stringsmalzahl)               
stringsmalzahl = stringsmalzahl[0:8] + " MITTE " + stringsmalzahl[13:] 
                                            #Sowas geht natürlich auch um in der mitte etwas austauschen



#Die Lenge eines Arrays rausfinden/Ausgeben mit der len() Funktion
text1 = "Der String stringsmalzahl ist"
text2 = "Elemente lang, bzw. er hat als Array so viele Stellen"
print ("\n" + text1, len(stringsmalzahl) , text2)  #In der Mitte die Len-Funktion

print ("\n" + stringsmalzahl + "\n" + text1 , len(stringsmalzahl) , text2)


#Die if Abfrage mit "if Bedingung:"
x = 40
if x < 50:                                  #Führt den Code aus wenn x kleiner ist als 50
    print("x ist kleiner als 50")           #eingerückt der Code in der Abfrage/Schleife (in Python nutzt man deswegen keine {})
    x = 0                                   #Setzt den Wert von x danach auf 0
print("jetzt ist x =" , x)                  #Dieser Code wird IMMMER ausgeführt, er ist nicht mehr in der if Abfrage

#Wahrheitswerte True und False (Bolean-Wert)
y = True                                    #Der Variablen wird der Bolean-Wert True zugewiesen
if y:                                       #Wenn etwas True ist wird es ausgeführt, deswegen braucht es hier kein "if y = True" es reicht "if y"
    print("y ist True")
    y = False
print("Jetzt ist y =",y)

#Wahrheitswerte werden auch gebildet wenn man Vergleiche anstellt
x = 44
Bedingung = x <= 50                         #In die Variable Bedingung wird das Ergebnis des Vergleiches "x ist kleiner gleich 50" geschrieben

#Code ausführen falls die Bedingung False ist geht mit "else:"
if Bedingung:                               #Wenn Bedingung(True) führe den eingerückten Code aus
    print("IF:Die Bedingung x <= 50 ist", Bedingung, "weil x = ", x)
else:                                       #Ansonsten führe den anderen angerückten Code aus:
    print("ELSE:Die Bedingung x <= 50 ist", Bedingung, "weil x = ", x)

#Mehrere Bedingungen checken mit "elif" "Wenn das dann das(if), Wenn das obere nicht dann das(elif), Ansonsten(else)"
Bedingung ="ich bin kein bolean mehr"
print(Bedingung)
if Bedingung == True:                               #Wenn in der Variablen Bedingung True steht führe den eingerückten Code aus
    print("IF:Die Bedingung x <= 50 ist", Bedingung, "weil x = ", x)
elif Bedingung == "ich bin kein bolean mehr":       #Wenn in der Variablen Bedingung == ... steht führe den eingerü
    print("ELIF:Die Bedingung ist kein Bolean mehr, wir haben ihr einen String zugewiesen und diesen verglichen")
else:                                               #Ansonsten führe den anderen angerückten Code aus:
    print("ELSE:Die Bedingung x <= 50 ist", Bedingung, "weil x = ", x)

#Die Schleifen - While Schleifen - Wichtig ist das man die Bedinung irgendwann erreicht - sonst Endlosschleife(oft bei Spielen benutzt)
x = 0
while x <=15:                                       #Solange x kleiner gleich 15 ist
    if x < 5:
        print("X ist kleiner als 5:", x)
    elif x == 5:
        print("X ist gleich 5:",x)
    elif x < 10:
        print("X ist kleiner als 10:",x)
    else:
        print("X ist weder kleiner,gleich 5 noch kleiner als 10:",x)
    #x = x + 1                                       #x wird  ein neuer Wert hinzugefügt x += 1 entspricht x = x + 1
    x += 1                                           #TIPP: Die Stelle an den man die Bedingung aufrechnet ist wichtig
print("fertig" + "\n")

#Die Schleifen - For Schleifen - Machen fast das gleiche wie While, aber effizienter
                                                    #Ist sehr viel anders als in z.B. Java wo wir uns eine Zählvariable definieren und dadurch zählen                    
for x in range(15):                                 #Weist der Variablen x 15 mal einen neuen Wert zu von 0 aus mit der range-Funktion
    if x < 5:
        print("X ist kleiner als 5:", x)
    elif x == 5:
        print("X ist gleich 5:",x)
    elif x < 10:
        print("X ist kleiner als 10:",x)
    else:
        print("X ist weder kleiner,gleich 5 noch kleiner als 10:",x)
    #es muss nicht hochgezählt werden
print("finish" + "\n" )

#Listen durchgehen mit der For-Schleife
x = ["Python", "Java", "C++"]   

for w in x:                                      #Wir definieren ein Wort/Element "W", dieses liegt in der Liste x 
    print(w)                                     #Für jedes Element W in der Liste x
print("finished Wort" + "\n")

#Listen können also auch gemischt sein
x = x + [3,2,1]                                  #Erweitere die Liste um ein paar Integers 
for w in x:                                      #Wir definieren ein Wort/Element "W", dieses liegt in der Liste x 
    print(w)                                     #Für jedes Element W in der Liste x
print("finished Wort +  Zahlen hinzugefügt" + "\n")

#Es können auch Schleifen in schleifen sein
x = [1,2]
for w in x:                                      #Wir definieren ein Wort/Element "W", dieses liegt in der Liste x 
    for y in x:                                  #Wir definieren ein Wort "y", dieses liegt in  der Liste x
        print(w)                                 #Die innere Schleife läuft solange bis sie fertig ist, danach geht es mit der äußeren weiter
        print(y)                                 #Die wieder die inner von vorne anfangen lässt
#Zur Erklärung: w = 1, y = 1, danach ist w = 1 weil man immer noch in der inneren Schleife ist, y = 2 - die innere Schleife endet, w wird zu 2, y = 1 weil die innere von vorne
#beginnt, w = 2, y = 2 - ENDE   
#Das Beispiel ist natürlich wenig nützlich aber es gibt Anwendungsfälle dafür, die if Schleife ist etwas praktikabler
print("finished Schleife in Schleife" + "\n")

#Die if Abfrage in der For Schleife - Wir fragen ab ob die Elemente in dem Array einer Bedingung entsprechen und führen je nachdem etwas aus
x = [234,3,54,65,646,23,646,324,3,4,656,435,4,32,5345435]
for w in x:
    if w <= 400:
        print("w ist kleiner gleich 400:",w)
    else:
        print("w ist größer als 400:",w)
print("If Abfrage in for Schleife fertig" + "\n")    

#Die For Schleife mit der range-Funktion - For Schleifen die x-mal durchlaufen - wie in Java 
for i in range(5):                                  #Zählt im Grunde die Stellen eines Arrays(Liste) hoch wie bei "for w in x" aber in x steht 0,1,2,3,4
    print(i)
print("Finished - Einfache For-Schleife mit 'bis' range(5)")
for i in range(5,10):                               #Man kann auch festlegen das man die Stellen 5 bis 10 nutzt wie hier(gezählt wird 5,6,7,8,9)
    print(i)                                        #Denn Übersetzt ist die 10 gleichbedeutend mit "solange die Stelle kleiner als 10 ist"
print("finished - For Schleife mit 'von bis' range(x,x)")
for i in range(5,20,2):                             #Hier gibt man die Schrittweite an mit der hochgegangen werden solll
    print(i)                                        #Möglich sind natürlich auch negative Angaben in allen Stellen der Funktion
print("Finished - For Schleife mit 'von bis und Step' range(x,x,x)" + "\n")

#Beispiel für den praktischen Nutzen einer Range Funktion - Um z.B. alle Elemente aus einem Array auszugeben
x = ["Rene", "Pinky", "Kotek"]                      #Definiert das Array und dessen Stellen
for i in range(0,len(x),2):                             #Für das Element i in der Range von der Länge des x-Arrays (das Array x hat 3 Elemente)            
    print(x[i])                                     #Er setzt in i also 0,1,2 ein und wir können mit print(x[i]) die jeweilige Stelle ausgeben(x an der Stelle i)
print("Finished - For Schleife mit range und der len-Funktion" + "\n")

#Break und Continue in der For- und While-Schleifen - Um die Schleife an einer bestimmten Vorraussetzung abbrechen
print("----Break und Continue in der For- und While-Schleifen - Um die Schleife an einer bestimmten Vorraussetzung abbrechen---")
#Break - Bricht die Schleife ganz ab
print("--Break--")
for i in range(0,20,2):
    if i%2 == 0:                                    #"i%2 == 0" %=modulo -> Rest einer Rechnung- Hat eine Zahl durch 2 einen Rest von 0 ist die Zahl grade
        print(f"{i} ist eine grade Zahl....breche ab")#mit f"" erstellen wir hier einen Funktions-String"
        break                                       #Wenn i durch 2 einen Rest von 0 hat(grade ist) bricht die for-Schleife ab (was direkt passiert)
    print(i)                                        #Wird in diesem Fall gar nicht mehr ausgeführt

for i in range(5,20):
    max = 13                                        
    if i > max:                                     #Wenn i größer ist als der in "max" definierte integer-Wert
        print(f"Oh, {i} ist Größer als {max}...breche ab!")
        break
    print(i)                                        #Dieser Code wird ausgeführt bis die if Bedingung darüber zum break führt
#Continue - Bricht die Schleife nur für den aktuellen Durchlauf ab
print("--Continue--")
for i in range(0,20):
    if i%2 == 1:                                    #Wenn die Zahl ungrade ist führt er die if Abfrage aus
        print(f"{i} ist ungrade")
        continue                                    #Und unterbricht mit der Continue Funktion den Rest der Schleife
    print(f"{i} ist grade")                         #Wenn die If Abfrage False ist wird dieser Teil ausgegeben

print("Finished - Break und Continue in einer Schleife" + "\n")

#Funktionen - Man definiert eine Funktion um diese immer wieder aufzurufen mit unterschiedlichen Parametern
print("---Funktionen---")
def Funktion(von, bis, step):                       #Definiert eine Funktion namens Funktions mit den Parametern von, bis und step
    for i in range(von,bis,step):                   #hier verwenden wir die Parameter um die range der for-Schleife zu bestimmen
        print(i+1)

Funktion(0,52,2)                                    #Um die Funktion abzurufen müssen wir diese nur noch in den Code schreiben und die Parameter übergeben
print("Finished Funktionen mit Parametern" + "\n")

#Funktionen - Rückgaben aus Funktionen(returns), Fibonati-Zahlen und Rekursionen(Unendlicher Vorgang der mit Hilfe von sich selbst definierbar ist)
print("Eine Fibonati Zahl errechnet sich aus den beiden vorheringen Werten addiert 0,1,1,2,3,5,8")
def fib(n):                                         #Definiert die Funktion fib mit dem Parameter n      
    if n < 2:
        return "kapier ich nicht "
    else:    
        return fib(n-1)+fib(n-2)                    #Return gibt einen Wert zurück der danach angegeben wird hier fib(n-1)+fib(n-2)
                                                    #Hier muss beachtet werden das wir direkt wieder die Funktion abrufen
var = fib(10)
print(var)