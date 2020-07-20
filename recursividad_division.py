
def div( n, m ):

    if m > n :
        return 0
    else:
        return div( ( n - m ), m ) + 1

n = int( input( "Ingrese el divedendo: " ) )
m = int( input( "Ingrese el divisor: " ) )

numero_div = div( n, m )
print( "El cociente entre " + repr( n ) + " y " + repr( m ) + " es " + repr( numero_div ) )