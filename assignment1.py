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
        prices = map(float,input("Enter price of Each Book seperated by space : ").split()) # Taking the input from user in a single line.
        gst = float(input("Enter GST if you want to : ")) # If the user gives strings then it will give us an error.
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
    alpha = [0]*26  # I am taking a list of size 26 initialized with all 0's
    s = s.lower()   # converting the string into lowercase
    for char in s:
        alpha[ord(char)-97]+=1     # The ascii value of 'a' = 97. Here what I am doing is the index 0 is equal to 'a' how? 
                                   # ord functiion will give the ascii value of a character. ord('b')-97 = 98-97 = 1. The index 1='b'
        if alpha[ord(char)-97]==1: # So i am subtracting 97 from the ascii value of each character of string which give the index.
            print(char,end=",")    # By using that i am storing the count of each character.
    print()                        # If the count is 1 i am printing otherwise i am not doing anything.
if __name__ == '__main__':
    try:
        printUniqueLetters(input("Enter a string contains alphabet only : "))  # Taking the input string from user.
    except IndexError as e:                  
        print("You should enter the alphabet letters only!")   # If the user gives the input as special characters we will get an error.
        print(e)   # The error is IndexError.
        
 # I hope the code is now understandable.

