#EΡΓΑΣΙΑ 9: ΥΠΟΛΙΣΤA
while True:
        print("EISAGWGH DEDOMENWN:")

        temp=int(input("Dwste ton prwto akeraio arithmo sthn lista: "))

        list=[temp]

        while True:

                temp=int(input("Dwste ena akeraio arithmo sthn lista: "))

                if temp==0 :

                        if (len(list)<2):

                                print("H lista prepei na periexei toulaxiston duo stoixeia")
                        else:

                                break
                else:

                        list.append(temp)

                        if len(list)>=2:

                                print("Gia diakoph ths eisagwghs dedomenwn eisagete to '0'")



        telos=len(list)//2

        max = sum(list[:telos])

#arxeiothetw tis metavlhtes "max_arxh" kai "max_telos" me skopo na vrw thn arxh kai to telos ths upolistas me to megalutero athroisma  

        max_arxh=0

        max_telos=telos

        arxh=0

        for i in range(telos,len(list)+1):

   
            if max<sum(list[arxh:i]):

                max=sum(list[arxh:i])

                max_arxh=arxh

                max_telos=i

            arxh+=1
    
        print("H upolista me to megalutero athroisma einai: " ,max,":",list[max_arxh:max_telos])
        print("Pieste 'ENTER' gia na ksanadwsete lista.")
        answer=input()
        if answer!="":
                break
    
