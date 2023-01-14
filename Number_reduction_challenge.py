
//Created by AnietieLEssien

/*

Creating pattern (Numbered Reduction)


    1 2 3 4 5
    2 3 4 5
    3 4 5
    4 5
    5
    
    
    
*/


for i in range(5):
  for j in range(5-i):
    print(str(j+i+1),end=" ")
  print()