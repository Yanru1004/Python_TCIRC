#b015 數字的顏色

while True:

    
    try:
        
        #讀取數字

        num = int(input())
        color = 'White'



        if num % 2 == 0:
            color = 'Red'

        if num % 3 == 0:
            if color == 'White':
                color = 'Yellow'

            elif color == 'Red':
                color = 'Orange'

        if num % 5 == 0:
            color = 'Black'
            

        if num % 7 == 0:
            if color == 'White':
                color = 'Blue'
            
            elif color == 'Red':
                color = 'Purple'
            
            elif color == 'Yellow':
                color = 'Green'
            
            elif color == 'Orange' or color == 'Black':
                color = 'Black'
        
        print(color)    
        

    except:
        break