
def method_help():
  # pass
  dic={"key1":100,"key2":200}
  a=dic.popitem()
  print(a)
########################################################################################################################
  # Methods, Help & Documentation Practice #1
  # Remove the characters to the left of our main text:
  
  # ,
  
  # :
  
  # %
  
  # _
  
  # #
  
  # Use the lstrip() method. Print the result to the screen:
  
  # ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
  
  # Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.
  word=",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"
  word.lstrip(",:%_#")
  print(word)


  




########################################################################################################################
  # Methods, Help & Documentation Practice #2
  # Add the element "orange" as the fourth element of the following list fruits, using the insert() method:
  
  fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
  fruits.insert(1,"orange")
  print(fruits)
  
  # Search the documentation for the requested method to know how it works.







########################################################################################################################
  #   Methods, Help & Documentation Practice #3
  # Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:
  
  phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
  tv_brands = {"Sony", "Philips", "Samsung", "LG"}
  isolated_sets= phone_brands.isdisjoint(tv_brands)
  print(isolated_sets)
  # Search the documentation for the requested method to know how it works.