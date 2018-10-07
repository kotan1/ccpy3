"""
Calculate and print area of the selected shape.
"""

print "Area calculator is running."

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius ** 2
  print "Area is %f" % (area)
elif option == 'T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print "Area is %f" % (area)
else:
  print("Invalid shape.")
 
print("Exiting calculator.")