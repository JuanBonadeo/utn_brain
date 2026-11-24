Ejemplos de Síndromes:

Hallar el código lineal que verifique la condición, si se desean transmitir 6 mensajes…

Si se quiere detectar y corregir errores simples en cada uno de los símbolos:



6 mensajes 2m>=6  m=3 

Cantidad de síndromes: se van probando los n que cumplan con la ecuación:
               n=6

Longitud del síndrome n-m = 6 – 3 = 3 (cantidad de columnas de HT) 

ei x HT =Si

(100000)  h11 h12 h13  = (001) = (h11 h12 h13)
	           h21 h22 h23
	           h31 h32 h33
	              h41 h42 h43 
                      h51 h52 h53
	           h61 h62 h63

(010000)  h11 h12 h13  = (010) = (h21 h22 h23)
	           h21 h22 h23
	           h31 h32 h33
	              h41 h42 h43 
                      h51 h52 h53
	           h61 h62 h63


(001000)  h11 h12 h13  = (011) = (h31 h32 h33)
	           h21 h22 h23
	           h31 h32 h33
	              h41 h42 h43 
                      h51 h52 h53
	           h61 h62 h63

(000100)  h11 h12 h13  = (100) = (h41 h42 h43)
	           h21 h22 h23
	           h31 h32 h33
	              h41 h42 h43 
                      h51 h52 h53
	           h61 h62 h63


(000010)  h11 h12 h13  = (101) = (h51 h52 h53)
	           h21 h22 h23
	           h31 h32 h33
	              h41 h42 h43 
                      h51 h52 h53
	           h61 h62 h63

(000001)  h11 h12 h13  = (110) = (h61 h62 h63)
	           h21 h22 h23
	           h31 h32 h33
	              h41 h42 h43 
                      h51 h52 h53
	           h61 h62 h63





Con HT  se plantea la Condición de Ortogonalidad vi x HT =0 con vi perteneciente al Código de Grupo V


Se plantean las ecuaciones, se obtiene V y se eligen 6 mensajes (cuales quieran)

Si se quiere corregir sólo en el primer dígito y sólo detectar en el resto:



6 mensajes  2m>=6 m=3 

Cantidad de síndromes: se van probando los n que cumplan con la ecuación:

 n=5

Longitud del síndrome n-m = 5 – 3 = 2 (cantidad de columnas de HT) 

ei x HT =Si

(10000)    h11 h12 	      = (01) = (h11 h12 )
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	           


(01000)    h11 h12        = (10) = (h21 h22)
	           h21 h22
	           h31 h32
	              h41 h42 
                      h51 h52
	          


(00100)    h11 h12	         = (10) = (h31 h32 )
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	           

(00010)    h11 h12        = (10) = (h41 h42 )
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	          

(00001)    h11 h12        = (10) = (h51 h52 )
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	          
01
10
10	= HT	
10
10



Con HT  se plantea la Condición de Ortogonalidad vi x HT =0 con vi perteneciente al Código de Grupo V




	  			   01
                                            10
	                                      10		
	                                      10
                                            10

              x1 x2 x3 x4 x5




Se plantean las ecuaciones, se obtiene V y se eligen 6 mensajes (cuales quieran).

Si se quieren corregir en el primer y tercer dígito y sólo detectar el resto:


6 mensajes  2m>=6  m=3 

Cantidad de síndromes: se van probando los n que cumplan con la ecuación:

      n=5

Longitud del síndrome n-m = 5 – 3 = 2 (cantidad de columnas de HT)

ei x HT =Si

(10000)    h11 h12        = (01) = (h11 h12 )
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	           


(01000)    h11 h12        = (10) = (h21 h22 )
	           h21 h22
	           h31 h32
	              h41 h42 
                      h51 h52
	          




(00100)    h11 h12        = (11) = (h31 h32 )
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	           

(00010)    h11 h12        = (10) = (h41 h42)
	           h21 h22  
	           h31 h32  
	              h41 h42   
                      h51 h52  
	          

(00001)    h11 h12        = (10) = (h51 h52 )
	           h21 h22  
	           h31 h32  
	              h41 h42  
                      h51 h52  
	          

01
10
11	= HT	
10
10

Con HT  se plantea la Condición de Ortogonalidad vi x HT =0 con vi perteneciente al Código de Grupo V


	  			   01
                                            10
	                                      11		
	                                      10
                                            10

              x1 x2 x3 x4 x5        00



Se plantean las ecuaciones, se obtiene V y se eligen 6 mensajes (cuales quieran).

Si se quiere corregir en el primer y segundo dígito, detectar el resto excepto el menos significativo:

Nota: el menos significativo es el último y su síndrome es 00.

6 mensajes 2m>=6  m=3 

Cantidad de síndromes: se van probando los n que cumplan con la ecuación:
  n=5       (se toma 3 porque el S4 es cero)      

Longitud del síndrome n-m = 5 – 3 = 2 (cantidad de columnas de HT)

ei x HT =Si

(10000)    h11 h12        = (01) = (h11 h12)
	           h21 h22  
	           h31 h32  
	              h41 h42   
                      h51 h52  
	           

(01000)    h11 h12       = (10) = (h21 h22)
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	          

(00100)    h11 h12       = (11) = (h31 h32)
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	           

(00010)    h11 h12       = (11) = (h41 h42)
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 
	          

(00001)    h11 h12       = (00) = (h51 h52 )
	           h21 h22 
	           h31 h32 
	              h41 h42 
                      h51 h52 


	          

01
10
11	= HT	
11
00

Con HT  se plantea la Condición de Ortogonalidad vi x HT =0 con vi perteneciente al Código de Grupo V



	  			   01
                                            10
	                                      11		
	                                      11
                                            00

              x1 x2 x3 x4 x5         00



Se plantean las ecuaciones, se obtiene V y se eligen 6 mensajes (cuales quieran).


