""" Book - Introduction to Python Programming : Rs 499.00

Book - Python Libraries Cookbook : Rs. 855.00

Book - Data Science in Python : Rs. 645.00


Taxes and additional charges are described as details - 

GST : 12%

Delivery Charges : Rs. 250.00 """

def totalInvocie(prices,gst=12):
    delivery_charges = 250.00
    sub_total = sum(prices)+delivery_charges
    total_invoice = (sub_total*gst)/100
    print("Total Invoice is : %.2f" %(total_invoice+sub_total))

if __name__== '__main__':
    print("""
             _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
            |                                                                                       |
            |                            Total Invoice Calculator                                   |
            |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

        ----------------------------------------------------------------------------------------------------
             _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
            |                                                                                          |
            |    This is command line based Total invoice calculator application.                       |
            |    In this application you can find the total invoice of your purchased Goods.           |
            |    By default the GST percentage is 12 if you wish you can enter your own.               |
            |    And there is also a sample list of prices to calculate the Total Invoice.             |
            |    In this application you can enter the prices of Goods the Delivery Charges and GST %. |
            |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
            
            Default Price List = [499.00,855.00,645.00]
            Default GST(%) = 12%
            Defult Delivery Charges = 250.00""")
    gst = 12
    try :
        prices = map(float,input("Enter price of Each Book seperated by space : ").split())
        gst = float(input("Enter GST if you want to : "))
    except ValueError as e:
        prices=[499.00,855.00,645.00]
    totalInvocie(prices,gst)



"""Question 2 - 

Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.

                                  

Input : string1 = "India"

Output : uniqueLetters = i,n,d,a


Input : string1 = "Dedication"

Output : uniqueLetters = d,e,i,c,a,t,o,n"""


def printUniqueLetters(s):
    alpha = [0]*26
    s = s.lower()
    for char in s:
        alpha[ord(char)-97]+=1
        if alpha[ord(char)-97]==1:
            print(char,end=",")
    print()
if __name__ == '__main__':
    try:
        printUniqueLetters(input("Enter a string contains alphabet only : "))
    except IndexError as e:
        print("You should enter the alphabet letters only!")
        print(e)

