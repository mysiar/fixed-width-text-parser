# Vibrator's files

### APS

```
H26 APS Vibrator Attributes
H26
H26 Item	Definition of field  		Cols  	Format	Min to Max      		Default	Units
H26 ----	---------------------		------	------	----------------		-------	-----
H26 1   	Record identification		1-1   	%1s   	A               		None   	-
H26 2   	Line name            		2-17  	%16.1f	Free            		None   	-
H26 3   	Point number         		18-25 	%8.1f 	Free            		None   	-
H26 4   	Point index          		26-26 	%1d   	1 to 9          		1      	-
H26 5   	Vibrator fleet number		27-27 	%1d   	Free            		None   	-
H26 6   	Vibrator number      		28-29 	%2d   	Free            		None   	-
H26 7   	Vibrator drive level 		30-32 	%3d   	0 to 100        		None   	%
H26 8   	Average phase        		33-36 	%4d   	-180 to 180     		None   	deg
H26 9   	Peak phase           		37-40 	%4d   	-180 to 180     		None   	deg
H26 10  	Average distortion   		41-42 	%2d   	0 to 99         		None   	%
H26 11  	Peak distortion      		43-44 	%2d   	0 to 99         		None   	%
H26 12  	Average force        		45-46 	%2d   	0 to 99         		None   	%
H26 13  	Peak force           		47-49 	%3d   	Free            		None   	%
H26 14  	Average ground stiffness		50-52 	%3d   	Free            		None   	-
H26 15  	Average ground viscosity		53-55 	%3d   	Free            		None   	-
H26 16  	Vib. position easting		56-64 	%9.1f 	Free            		None   	metre
H26 17  	Vib. position northing		65-74 	%10.1f	Free            		None   	metre
H26 18  	Vib. position elevation		75-80 	%6.1f 	-999.9 to 9999.9		None   	metre
H26
H26      1         2         3         4         5         6         7         8
H26 5678901234567890123456789012345678901234567890123456789012345678901234567890
H26

A         19064.0 25360.01222 70   1   2101863 71 56 72 725883.0 2531118.2 121.6
```

### VAPS
```
H26 APS Vibrator Attributes 
H26 
H26 Item	Definition of field  		Cols  	Format	Min to Max      		Default	Units
H26 ----	---------------------		------	------	----------------		-------	-----
H26 1   	Record identification		1-1   	%1s   	A               		None   	-   	
H26 2   	Line name            		2-17  	%16.1f	Free            		None   	-   	
H26 3   	Point number         		18-25 	%8.1f 	Free            		None   	-   	
H26 4   	Point index          		26-26 	%1d   	1 to 9          		1      	-   	
H26 5   	Vibrator fleet number		27-27 	%1d   	Free            		None   	-   	
H26 6   	Vibrator number      		28-29 	%2d   	Free            		None   	-   	
H26 7   	Vibrator drive level 		30-32 	%3d   	0 to 100        		None   	%   	
H26 8   	Average phase        		33-36 	%4d   	-180 to 180     		None   	deg 	
H26 9   	Peak phase           		37-40 	%4d   	-180 to 180     		None   	deg 	
H26 10  	Average distortion   		41-42 	%2d   	0 to 99         		None   	%   	
H26 11  	Peak distortion      		43-44 	%2d   	0 to 99         		None   	%   	
H26 12  	Average force        		45-46 	%2d   	0 to 99         		None   	%   	
H26 13  	Peak force           		47-49 	%3d   	Free            		None   	%   	
H26 14  	Average ground stiffness		50-52 	%3d   	Free            		None   	-   	
H26 15  	Average ground viscosity		53-55 	%3d   	Free            		None   	-   	
H26 16  	Vib. position easting		56-64 	%9.1f 	Free            		None   	metre	
H26 17  	Vib. position northing		65-74 	%10.1f	Free            		None   	metre	
H26 18  	Vib. position elevation		75-80 	%6.1f 	-999.9 to 9999.9		None   	metre	
H26 19  	Shot number          		82-86 	%5d   	1 or 99999      		None   	-   	
H26 20  	Acquisition number   		87-88 	%2d   	1 to 32         		None   	-   	
H26 21  	2-digit vibrator fleet number89-90 	%2d   	1 to 32         		None   	-   	
H26 22  	Vib status code      		91-92 	%2d   	1 to 98         		None   	-   	
H26 23  	Mass 1 Warning       		94-94 	%1s   	  or W          		None   	-   	
H26 24  	Mass 2 Warning       		95-95 	%1s   	  or W          		None   	-   	
H26 25  	Mass 3 Warning       		96-96 	%1s   	  or W          		None   	-   	
H26 26  	Plate 1 Warning      		100-100	%1s   	  or W          		None   	-   	
H26 27  	Plate 2 Warning      		101-101	%1s   	  or W          		None   	-   	
H26 28  	Plate 3 Warning      		102-102	%1s   	  or W          		None   	-   	
H26 29  	Plate 4 Warning      		103-103	%1s   	  or W          		None   	-   	
H26 30  	Plate 5 Warning      		104-104	%1s   	  or W          		None   	-   	
H26 31  	Plate 6 Warning      		105-105	%1s   	  or W          		None   	-   	
H26 32  	Force Overload       		106-106	%1s   	  or F          		None   	-   	
H26 33  	Pressure Overload    		107-107	%1s   	  or P          		None   	-   	
H26 34  	Mass Overload        		108-108	%1s   	  or M          		None   	-   	
H26 35  	Valve Overload       		109-109	%1s   	  or V          		None   	-   	
H26 36  	Excitation Overload  		110-110	%1s   	  or E          		None   	-   	
H26 37  	Stacking folder      		111-112	%2d   	1 to 32         		None   	-   	
H26 38  	Computation domain   		113-113	%1s   	T or F          		None   	-   	
H26 39  	Ve version           		114-117	%4s   	Free            		None   	-   	
H26 40  	Day of year          		118-120	%3d   	1 to 999        		None   	-   	
H26 41  	Time hhmmss          		121-126	%6s   	000000 or 235959		None   	-   	
H26 42  	HDOP                 		127-130	%4.1f 	1.0 or 99.9     		None   	-   	
H26 43  	Tb Date              		131-150	%20d  	0 to 1.8446744073709552E19None   	-   	
H26 44  	GPGGA Message        		151-239	%89s  	Free            		None   	-   	
H26                                                                        
H26      1         2         3         4         5         6         7         8
H26 5678901234567890123456789012345678901234567890123456789012345678901234567890
H26                                                                        

A         19080.0 25206.01222 70   1  -3111864 73 55 73 723954.7 2531266.3 124.4     1 122 1                   1T 4.1294035708 1.1    1287187046624000GPGGA,235726.00,2252.45969167,N,05310.97627209,E,4,10,1.1,127.602,M,-33.537,M,9.0,0002*67
```


### COG
```
H26 C.O.G Attributes Record Specification 							 	 
H26 
H26 Item	Definition of field  		Cols  	Format	Min to Max      		Default	Units
H26 ----	---------------------		------	------	----------------		-------	-----
H26 1   	Record identification		1-1   	%1s   	A               		None   	-   	
H26 2   	Line name            		2-17  	%16.1f	Free            		None   	-   	
H26 3   	Point number         		18-25 	%8.1f 	Free            		None   	-   	
H26 4   	Point index          		26-26 	%1d   	1 to 9          		1      	-   	
H26 5   	COG state            		28-28 	%1d   	0 to 7          		None   	-   	
H26 6   	COG position easting 		30-38 	%9.1f 	Free            		None   	metre	
H26 7   	COG position northing		40-49 	%10.1f	Free            		None   	metre	
H26 8   	COG position elevation		51-56 	%6.1f 	Free            		None   	metre	
H26 9   	Deviation COG - Source		60-69 	%10.1f	Free            		None   	metre	
H26                                                                        
H26       items  5 : 0= No Cog                                             
H26                  1= Estimated Cog                                      
H26                  2= Est. Radial Err.                                   
H26                  3= Actual Cog                                         
H26                  4= Radial Err.                                        
H26                  5= Missing Position                                   
H26                  6= Inaccurate Cog                                     
H26                  7= Natural Cog                                        
H26                                                                        
H26                                                                        
H26      1         2         3         4         5         6         7         8
H26 5678901234567890123456789012345678901234567890123456789012345678901234567890
H26                                                                        

C         19064.0 25360.01 3  725883.0  2531118.2  121.6          2.5
```