# -*- coding: utf-8 -*-
"""recycle_guide.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zgaot9Yv0B4VfkDfd9fGg7fY6mwDKV3x
"""

flag = False
while(not flag):
  item=input("What are you getting rid of? \n A) Paper \n B) Plastic/Metal/Glass \n C) Flammable Items \n D) Clothing \n E) Electronics \nInput: " )
  item = item.upper()
  
#Paper ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  if item == "A" or item == "PAPER":
    flag = True
    itemA = input("\nIs it from a tree and is unsoiled? \n\n[Yes]  [No]  [Honestly, I don't know] \nInput: " ).upper()
    if itemA == "YES":
      print("Recycle your item in one of the green bins. They accept mixed paper and cardboard.")
    elif itemA == "NO":
      print("Just dump in it the black bin, aka your local trash can.")
    else:
      itemA1 = input("\n Is your item a... \n- newspaper \n- magazine \n- paperboard egg carton \n- mail envelope \n- paper bag \n- wrapping paper \n- receipt \n- paper cup with wax lining \n- food or shoe box \n- and/or an unsoiled part of a pizza box? \n\n[Yes]  [No] \nInput: ").upper()
      if itemA1 == "YES":
        print("Lucky for you, your item is recyclable! Please discard it in a green bin (for mixed paper and cardboard.")
      else:
        input("Is your item a soft paper like a paper towel, paper with heavy wax, or an hardcover book? \n\n[Yes]  \n[No] \nInput: ")
        print("If your item is a hardcover book and is in a decent condition then you can donate it to your local library or resell it online. Otherwise, your item belongs in a garbage can.")

#Plastic and Glass -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  elif item=="B" or item=="PLASTIC" or item== "GLASS" or item=="METAL":
    flag = True
    itemB = input("\nIs it a... \n- plastic bottle \n- rigid plastic food container and packaging \n- condiment containers \n- cleaning solution bottle \n- rigid plastic toys with batteries removed \n- empty aerosol can and lid \n- metal can or hanger \n- aluminum foil \n- glass bottle and jar? \n\n[Yes]  [No]  [Not Sure] \nInput: ")
    itemB = itemB.upper()

    if itemB == "YES":
      print("Put it in the blue bin and you're good to go!")
    else:
      itemB1 = input("\nThen is your item a plastic bag, food wrapper, or made out of styrofoam? \n- [Yes] \n- [No] \n- Input:")
      print("Off to the trash it goes!")

#Flammable Items ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  elif item == "C" or item == "FLAMMABLE ITEMS":
    flag = True
    itemC = input("Is the item  \n- A) motor oil \n- B) gasoline \n- C) heating oil \n- D) or harmful household chemicals (liking cooking oil)? \nInput: ")
    itemC = itemC.upper()
    if itemC == "A" or "B" or "C":
        print("You can bring your oil to a gas station. You may be charged a fee though.")
    else:
        print("You have to take the oil/chemicals to a SAFE Disposal Event.")
#Clothing ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
  elif item=="D" or item=="CLOTHING":
    flag = True

    itemD1=input('Does your clothing contain Spandex, Lycra, or elastane? \n [Yes] \n [No] \nInput: "')
    itemD1 = itemD1.upper()
    
    if itemD1 == "YES":
      print("Your only options are either donating, reselling, or throwing it away.")
    else:
      itemD2 = input("Is your clothing in good condition? \n [Yes] \n [No] \nInput: ")
      itemD2 = itemD2.upper()
      
      if itemD2 == "YES":
        print("You can donate your clothing at a thrift shop, community center, or to charity. Otherwise, you may also resell your items online on platforms such as Ebay or Depop.")
      
      else:
        print('You can either drop off your clothes at a textile recycling service or compost it.')
#Electronics ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  elif item=='E' or item=="ELECTRONICS":
    flag = True
    print("You can drop off old electronics at any NYC electronics drop off locations")
    
    import pandas as pd
    df = pd.read_csv("https://data.cityofnewyork.us/resource/wshr-5vic.csv")
    dfC = df[["dropoff_sitename","address","zipcode"]]
    zip = int(input("Enter Zip Code: "))
    for n in range(dfC["zipcode"].size):
      data = dfC[(dfC["zipcode"]+10000 >= zip-300) & (dfC["zipcode"]+10000 <= zip+300)]
    display(data)

  else: 
    print("That is not a vaild response, please try again")