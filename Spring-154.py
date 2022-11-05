from time import time
import os
import binascii
import math
import os.path

lenf=0
name=""
add_bits=""
Make_togher=""

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":

                        i=1

                    if namez=="e":
                        i=2
                 
                    Number_add_plus_one=""
                    Prime_Not=""
                    Times_6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    compress_or_not_compress=1
                    Circle_times3=0

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    	
                    nac=len(nameas)
                    
                   
                    s=""

                    Equal_info_between_of_the_cirlce_of_the_file=""
                    Equal_info_between_of_the_cirlce_of_the_file_2=""

                    Prime_Not=""
                    Times_6=""

                    Translate_info_Decimal=""

                    D=0

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()
                    

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7==0:
                        	 raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                                   
                        Equal_info_between_of_the_cirlce_of_the_file_23=""
 
                        sda18=""
                        Equal_info_between_of_the_cirlce_of_the_file_29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    

                                    if Circle_times3==1:
                                        Equal_info_between_of_the_cirlce_of_the_file_2=sda
                            
                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_2, 2)
                                
                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                             
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    
                                    data=width_bits3
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1

                                    Equal_info_between_of_the_cirlce_of_the_file_2=sda
                                    Extact=Equal_info_between_of_the_cirlce_of_the_file_2

                                    lenf3=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                lenf2=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**40)-1:
                                        raise SystemExit

                                #########################################################################################################################################################
                                
                                
                                if i==1:

                                    
                                    Extract1=0
                                    Times_10=0
                                    Times_7=0
                                    between_of_the_cirlce_of_the_file5=26
                                    

                                    while Extract1!=1:
                                        
                                        


                                         
                                            
                                            Circle_times2=0
                                            between_of_the_cirlce_of_the_file5+=1

                                            if between_of_the_cirlce_of_the_file5==(2**16)-1:
                                                Times_10+=1
                                                between_of_the_cirlce_of_the_file5=26
                                            if Times_10==(2**48)-1:
                                                Times_7+=1
                                                Times_10=0
                                                between_of_the_cirlce_of_the_file5=26
                                            
                                                
                                            
                                            
                                            
                                           
                            
                                            Times_8=Times_7
                                            Times_9=bin(Times_7)[2:]
                                            long_T=len(Times_9)
                                            long_T=(long_T//8)+1
                                            Combinate=""
                                            Combinate="0"+str(long_T*8)+"b"
 
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file2=""
                                            Equal_info_between_of_the_cirlce_of_the_file3=""
                                            Equal_info_between_of_the_cirlce_of_the_file4=""
    
                                           
                                            Equal_info_between_of_the_cirlce_of_the_file2=format(between_of_the_cirlce_of_the_file5,'016b')
                                            Equal_info_between_of_the_cirlce_of_the_file3=format(Times_10,'048b')
                                            Equal_info_between_of_the_cirlce_of_the_file4=format(Times_8,Combinate)
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file4
    
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=""
                                      
                                            
                                            
                                            lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
    
    
                                            add_bits=""
    
                                            Times_6=""
    
                                            #Extract
    
                                            sda10=""
                                            Translate_info_Decimal=""
                                          
                                            Number_add_plus_one=""
                                            Prime_Not=""
                                            Times_6=""
                                        
                                            Number_of_the_file=0
                                            Prime_Not=0
    
                                            C=1
                                         
                                            if C==1:
                                                if   Circle_times2==0:
    
                                                         
    
                                                        
    
                                                        
                                                        
                                                        
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
    
                                                        sda10=Equal_info_between_of_the_cirlce_of_the_file2[0:16]
                                                        Deep5 = int(sda10, 2)
                                                        Deep5=Deep5+2
                                                        Deep4=Deep5-1
                                                        
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                        Equal_info_between_of_the_cirlce_of_the_file4=Equal_info_between_of_the_cirlce_of_the_file_2
                                                        
                                                        Deep7=Deep5-2
                                                        
                                                        Times_6=Equal_info_between_of_the_cirlce_of_the_file3[0:48]
                                                        
                                                        T = int(Times_6, 2)
                                                        
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                        #print("Deep: ")
                                                        #print(Deep7-25)
                                                        
                                                if   Circle_times2>0:
                                                        Translate_info_Decimal_2=0
                                                
                                                        
            
                                                if C==1 and T!=0:
                                                        Equal_info_between_of_the_cirlce_of_the_file4=Equal_info_between_of_the_cirlce_of_the_file4
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                        Number_add_plus_one=Equal_info_between_of_the_cirlce_of_the_file4[lenf6-Deep4:lenf6]
                                                        Prime_Not=Equal_info_between_of_the_cirlce_of_the_file4[lenf6:lenf6]
                                                        Equal_info_between_of_the_cirlce_of_the_file4=Equal_info_between_of_the_cirlce_of_the_file4[0:lenf6-Deep4]
                                                if len (Equal_info_between_of_the_cirlce_of_the_file)!=0:
                        
                                                                                                    
                                                    Number_of_the_file=int(Equal_info_between_of_the_cirlce_of_the_file4, 2)

                                                else:
                                                    Number_of_the_file=0
                                                
                                                Hole_Number_information=(2**Deep5)-1
                                                add_ones_together=Hole_Number_information
                                                Number_of_the_file=Number_of_the_file*add_ones_together
                                                Number_of_the_file=Number_of_the_file
                                                #print(Number_of_the_file)
                                                        
                                               
                                            Times_6=Number_add_plus_one
                                            Number_add_plus_one=""
                                              
                                            #####################################################################################################################################################
                                           
                                            Prime_Not=""
                                            
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                             
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                            #print(Equal_info_between_of_the_cirlce_of_the_file_17)
                                           
    
                                            if i==1:
                                                Make_togher=""
                                                Make_togher=Times_6
                                                Number_add_plus_one=""
                                                add_bits=""
                                                if C==1 and T!=0:
                                                        Circle_times2=Circle_times2+1
    
                                                lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                #print(Circle_times2)
                                                
                                                
                                                if  Circle_times2==T:
                                                           
                                                    if C==1 and T==0:
                                                        Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file4
                                                        lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                        add_bits=""
                                                        count_bits=8-lenf%8
                                                        z=0
                                                        if count_bits!=0:
                                                                if count_bits!=8:
                                                                    while z<count_bits:
                                                                        add_bits="0"+add_bits
                                                                        z=z+1
                                                        Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                                
                                                    if C==1 and T!=0:
         
                                                        Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                                        lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                        
                                                        
                                                        
                                                        lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                        add_bits=""
                                                        count_bits=8-lenf%8
                                                        z=0
                                                        if count_bits!=0:
                                                                if count_bits!=8:
                                                                    while z<count_bits:
                                                                        add_bits="0"+add_bits
                                                                        z=z+1
                                                        Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                                                                         
                                                    if Extact==Equal_info_between_of_the_cirlce_of_the_file_17:
                                                           Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file2+Equal_info_between_of_the_cirlce_of_the_file3+Equal_info_between_of_the_cirlce_of_the_file4
      
                                                           Extract1=1
                                                        
                                    if Extract1==1:                
                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)
                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                                            
                                            with open(nameas, "wb") as f2:
                                                f2.write(width_bits3)
                                                    
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
                                    		
                                if i==2:
                                    Circle_times2=0

                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                              
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    sda10=""
                                    Translate_info_Decimal=""
                                  
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                
                                    Number_of_the_file=0
                                    Prime_Not=0

                                    
                                 
                                    if C==1:
                                        if   Circle_times2==0:

                                                
                                                
                                                
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                                sda10=Equal_info_between_of_the_cirlce_of_the_file[0:16]
                                                Deep5 = int(sda10, 2)
                                                Deep5=Deep5+2
                                                Deep4=Deep5-1
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[16:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                Deep7=Deep5-2
                                                
                                                Times_6=Equal_info_between_of_the_cirlce_of_the_file[0:48]
                                                T = int(Times_6, 2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[48:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                print("Deep: ")
                                                print(Deep7-25)
                                                
                                        if   Circle_times2>0:
                                        	Translate_info_Decimal_2=0
                                        
                                        	
    
                                        if C==1 and T!=0:
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                Number_add_plus_one=Equal_info_between_of_the_cirlce_of_the_file[lenf6-Deep4:lenf6]
                                                Prime_Not=Equal_info_between_of_the_cirlce_of_the_file[lenf6:lenf6]
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[0:lenf6-Deep4]
                                                if len (Equal_info_between_of_the_cirlce_of_the_file)!=0:
                        
                                                                                                    
                                                    Number_of_the_file=int(Equal_info_between_of_the_cirlce_of_the_file, 2)

                                                else:
                                                    Number_of_the_file=0
                                                                                                    
                                                Hole_Number_information=(2**Deep5)-1

                                                add_ones_together=Hole_Number_information
                                                Number_of_the_file=Number_of_the_file*add_ones_together
                                                Number_of_the_file=Number_of_the_file
                                                
                                       
                                    
                                      
                                    #####################################################################################################################################################
                                   
                                    
                                    
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                     
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                   

                                    if i==2:
                                        Make_togher=""
                                        Make_togher=Times_6
                                        Number_add_plus_one=""
                                        add_bits=""
                                        if C==1 and T!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==T:
                                        	   
                                            if C==1 and T==0:
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                        
                                            if C==1 and T!=0:
 
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                            	lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	#print(lenf14)

                                            		
                                            	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                         
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)

                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(width_bits3)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
