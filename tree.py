#CMPT 120L 200
#Veronica Stureborg

#Program to display a tree on screen using text characters
#i is equal to the row
#h is the height of the tree

def main():
    h=int(input("How high would you like the tree to be?"))
    for i in range (h):
        print(((h-i-1))* ' '+(i*2+1)* '#')
    print((h-1)* ' '+'#')                        
    
main()


