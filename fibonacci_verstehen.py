functionCallCount = 0

def fib( n ):
  
  # das sagt der function "fib" das "functionCallCount" eine variable
  # von außerhalb ist. Wenn du dann was mit ihr veränderst, verändert
  # sich auch die variable außen 
  global functionCallCount

  # erhöht bei jedem function aufruf die variable "functionCallCount" um 1
  functionCallCount = functionCallCount + 1
  
  # Für n=0 und n=1 brauchen wir spezielles verhalten,
  # da wir ja sonst in den negativen bereich kommen 
  # (würde zb so aussehen für n=1 --> fib( 1 - 2) + fib(1 - 1) )
  if( n == 0 ):
    print("0")
    return 0
  if( n == 1 ):
    print("1")
    return 1
  # Das ist das normale muster der fibonacci zahlen
  return fib(n - 2) + fib(n - 1)


# berechnet die fibonacci zahl für die 10te stelle
# 1 1 2 3 5 8 13 21 34 --> 55 <--
result = fib( 10 )

print( "Fibonacci beträgt", result)
print( "'fib' wurde", functionCallCount, "mal aufgerufen" )



#####################################################################
functionCallCount = 0

def fib( n ):
  
  # das sagt der function "fib" das "functionCallCount" eine variable
  # von außerhalb ist. Wenn du dann was mit ihr veränderst, verändert
  # sich auch die variable außen 
  global functionCallCount

  # erhöht bei jedem function aufruf die variable "functionCallCount" um 1
  functionCallCount = functionCallCount + 1
  
  # Für n=0 und n=1 brauchen wir spezielles verhalten,
  # da wir ja sonst in den negativen bereich kommen 
  # (würde zb so aussehen für n=1 --> fib( 1 - 2) + fib(1 - 1) )
  if( n == 0 ):
    return 0
  if( n == 1 ):
    return 1

  # Das ist das normale muster der fibonacci zahlen
  return fib(n - 2) + fib(n - 1)


# Fordert den user zu einem input auf.
# Dieser input wird dann in eine ganze zahl 
# umgewandelt (integer auf english kurz "int")
# und in die variable n gespeichert.
n = int( input("Enter a number: ") )

# berechnet die fibonacci zahl für die nte stelle
result = fib( n )

print( "Fibonacci für n =", n, "ist", result )
print( "'fib' wurde", functionCallCount, "mal aufgerufen" )