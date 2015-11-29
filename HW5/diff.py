def main():
    file1=str(input("Enter the name of the first file: "))
    file2=str(input("Enter the name of the second file: "))
    file_one=open(file1)
    file_two=open(file2)
    a=file_one.read()
    b=file_two.read()
    
    for i in range(0,min(len(a),len(b))):
        if not a[i]==b[i]:
            print("Mismatch at character ",i,a[i],"!=",b[i])
            
    if len(a)>len(b):
        for i in range(len(b),len(a)):
            print("No matching character for character %d (%s) found in %s."%(i,a[i],file1))
         
    if len(a)<len(b):
        for i in range(len(a),len(b)):
            print("No matching character for character %d (%s) found in %s."%(i,b[i],file2))
    file_one.close()
    file_two.close()
    
    
main()
