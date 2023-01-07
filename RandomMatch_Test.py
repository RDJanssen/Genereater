Ingredient = ['kimchi','coffee', 'wine', 'egg', 'corn', 'potato', 'onion', 'apple', 'lentil', 'steak', 'pork', 'leek', 'mustard greens', 'herbs', 'yogurt', 'rice','chikpea', 'tofu', 'seitan', 'berbere', 'tempeh', 'ice cream', 'pepper','peanut butter','peperjack','pickle','oat', 'fish', 'strawberry', 'squash','chocolate', 'coconut','couscous','crab','cinnamon,','giardineira','ham','hot sauce','hummus','macncheese','beer','pasta','potato chips','preserves','relish', 'salsa', 'sausage', 'salmon', 'stock', 'tea', 'tomato','tortilla','tuna','turkey','vanilla','vinegar', 'cornbread','cheeto', 'almond', 'anchovy','asparagus','arugula','avocado','bacon','bagel','basil','nanna', 'bbq', 'beans', 'boeuf', 'beets', 'carnitas', 'berries', 'olives', 'muffin', 'pudding','mushroom', 'pancake', 'cookies', 'cauliflower', 'buttermilk','cabbage','cake','cashews']

Format = ['steak', 'burrito', 'gallette', 'soup', 'puree', 'tartare', 'donut', 'mash', 'hash', 'coulis', 'sauce', 'carpaccio', 'ice cream' ,'charcuterie', 'parfait', 'pie', 'sandwoch', 'pizza' , 'casserole', 'plate', 'bowl', 'suchi', 'aioli','smoothie', 'balls', 'foam','salad','curry', 'cake', 'reduction', 'glaze', 'gravu', 'bread', 'empanada','soup','stew','gazpacho','pancake','filling','cookie','crust','paste','cracker','mousse', 'ganache', 'fries','cocktail','syrup','dip','gremolata', 'dust', 'ash', 'bars', 'burger','tapenade', 'hummus', 'cheese', 'broth', 'cider', 'wine', 'rub', 'oil', 'wrap', 'frosting', 'truffle', 'topping', 'marinade', 'chutney', 'ceviche', 'dressing', 'vinaigrette', 'crudite', 'cruton','pasta','jam','slaw','melt','roast','biscuit', "&eggs", 'in aspic', 'butter', 'bagna cauda',]
Style = ['pan fried', 'microwaved', 'dressed','wilted', 'keto', 'salted', 'cured', 'morrocan', 'scrambled', 'teriyaki','sorbet','general zhao', 'al pastor', 'chicken fried', 'spicy', 'szechuan', 'berbere', 'blackened', 'classic holiday', 'sour','margerhita', 'raw', 'steamed', 'boiled', 'dehydrated', 'diced', 'stir fried', 'instant','crispy' , 'shredded', 'deep dish', 'charred' , 'drunken', 'grilled', 'egyptian', 'family style', 'farmhouse','skewered', 'chilled', 'sabzhi', 'mediterranean', 'breaded', 'poached','artisanal', 'brewed', 'trash', 'gratin','fresh', 'frosted', 'faux',   'brined', 'smoked', 'vegan', 'fermented', 'baked', 'macerated', 'french', 'indian', 'mexican', 'carmelized', 'bbq', 'brulee', 'thai', 'chiffonade', 'beerbattered','deepfroe', 'gastro', 'emulsion', 'pureed', 'dry aged', 'infused', 'jerk', 'southwest', 'glutenfree','curried', 'dried','dry rubbed', 'curdled', 'candied', 'preserved','boiled','steamed', 'spiced', 'pumpkin spice', 'thick cut', 'stuffed', 'etouffee', 'reduction', ]

numbers = []
seed()

items = []
elements = [Ingredient, Format, Style]
for element in elements:
    value = randint(0, len(element))
    items.append(element[value])

print()
print(" ".join(items))


### OLD CODE FOR REFERENCE 
### numbers = []
### from random import seed
### from random import randint
### seed()
### print(len(Ingredient))
### print(len(Format))
### print(len(Style))
### for i in range(3):
###    value = randint(0, len(Format)-1)
###    numbers.append(value)
### print(numbers)

### print(Style[numbers[0]] + " " + Ingredient[numbers[1]] + " " + Format[numbers[2]])
