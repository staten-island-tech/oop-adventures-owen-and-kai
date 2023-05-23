def addtoinventory(Item):
   inventory.append(Item)

inventory = ['Basic_Gloves']
if location_choice == glove_shop:
   if location_choice == input ('Hello welcome to my shop. We can sell you any gloves or something a little special if you catch my drift...  Choices: Buy Gloves/Buy Steroids' ):
    if purchase == input('Buy Gloves'):
        glove_choices ==input('Here are the glove options: Light Gloves, Heavy Gloves, Fiery Gloves, Fingerless Gloves, Bell Gloves, Latex Gloves, Holy Gloves, Police Gloves, Only Finger Gloves')
        if input == 'Light GLoves':
            glove_purchase == input ('The light gloves will increase your dexterity and decrease stamina use. Would you like to purchase it? Choices: Y/N')
            if input == 'Y':
                addtoinventory('Light Gloves')
            if input == "N":
               print
        if input == 'Heavy Gloves':
            glove_purchase == input('The Heavy Gloves Will do more damage and give you more defense but will use more stamina. Would you like to purchase it? Choices: Y/N')
           
           


currency = 0
currency = float(currency) + 100
currency = float(currency) + 200
currency = float(currency) - 50
print (currency)

