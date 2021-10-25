# items have their own separate class
# items name as well as the price

class ShoppingCart:
    init
    # dict = {}
    # correct price based on location
    # self.subtotal = 0
    # self.taxtotal = 0
    # self.grandtotal = 0
    add(object, howmany)
    # append to dictionary the number of items for the object such as the banana
    # += homwmany
    # if not in dict:
    # create a new key value pair
    # do not let self.grandtotal >= 50,000
    # return "Sorry price is too high."
    remove
    # in the dictionary we can look up in constant time the object key and we can
    # -= 1
    # floor cap at 0
    # isEmpty()

    # if item not in dict.keys():
    # return "Item does not exist in cart!"

    clear
    # clear dictionary
    # isEmpty()

    isEmpty
    # if dict is None:
    # print("Shopping cart is empty")

    look
    # return dict.items()
    calculate_price
    #
    # store object that has access to the tax
    # for i, k in dict.items():
    #    self.subtotal  += k * k.getPrice()
    #    self.taxtotal += subtotal * store.getTax()

    # self.subtotal = 1000
    # self.taxtotal = 100
    # self.grandtotal = subtotal + taxtotal
    # return self. grand_total
    checkout
    # dont let user be able to checkout when dict is None
    # we will just have grand total

# the store page

# create object of type shopping cart
# sc.add(Banana)
# sc.add(Banana)
# sc.remove(Banana)
# sc.remove(Banana)
# sc.remove(Banana)
# sc.remove(Banana)
# sc.add(Television, 1000)
