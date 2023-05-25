def addtoinventory(Item):
   inventory.append(Item)
currency = 0

inventory = ['Basic_Gloves']
if location_choice == glove_shop:
   if location_choice == input ('Hello welcome to my shop. We can sell you any gloves or something a little special if you catch my drift...  Choices: Buy Gloves/Buy Steroids '):
    if purchase == input('Buy Gloves'):
        glove_choices == input('Here are the glove options: Light Gloves, Heavy Gloves, Fiery Gloves, Fingerless Gloves, Bell Gloves, Latex Gloves, Holy Gloves, Police Gloves, Only Finger Gloves ')
        if glove_choice == 'Light GLoves':
            glovepurchase == input ('The light gloves will increase your dexterity and decrease stamina use and they cost 50. Would you like to purchase it? Choices: Y/N ')
            if glovepurchase == 'Y':
                addtoinventory('Light Gloves')
                currency = float(currency) - 50
            if glovepurchase == "N":
               return_to_shop = input('Ok is there anything you would like? ')
        if glove_choice == 'Heavy Gloves':
            glovepurchase == input('The Heavy Gloves Will do more damage and give you more defense but will use more stamina. and cost 50 Would you like to purchase it? Choices: Y/N ')
            if glovepurchase == 'Y':
               addtoinventory('Heavy Gloves')
               currency = float(currency) - 50
            if glovepurchase == "N":
               return_to_shop = input('Ok is there anything you would like? ')
        if glove_choice == 'Fiery Gloves':
            glovepurchase == input ('The Fiery Gloves will greatly increase your speed and attack but they will greatly drain stamina cost 100. Would you like to purchase it? Choices: Y/N ')
            if glovepurchase == 'Y':
               addtoinventory('Fiery Gloves')
               currency = float(currency) - 50
            if glovepurchase == "N":
               return_to_shop = input('Ok is there anything you would like? Y/N ')

            
                
           
           


"""currency = 0
currency = float(currency) + 100
currency = float(currency) + 200
currency = float(currency) - 50
print (currency)"""

