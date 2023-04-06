import climage

  
# converts the image to print in terminal 
# inform of ANSI Escape codes 

output = climage.convert("sprites/Ting-Lu.png",is_unicode=True) 

  
# prints output on console. 

print(output)