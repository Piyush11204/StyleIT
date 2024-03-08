class Cart():
    def  __init__(self,request):
        self.session = request.session

        cart=self.session.get('session_key',{}) 
        if 'session_key'  not in self.session:
            #if no session cart then create a new one
            self.cart={}
            for i in range(0,5):
                self.cart[str(i)]='Item Not Found!'
        else:
            self.cart=cart
            
    def add(self,ShopIT):
        ShopIT_id= str(ShopIT.id)
        
        if ShopIT_id in self.cart :
            #item is already added to the cart so we just increment the quantity by one
            self.cart[ShopIT_id]['quantity']+=1  
        else:
            #add item into the cart dictionary with its default values
            self.cart[ShopIT_id]={'quantity':1,'price':float(ShopIT.price),'product':ShopIT }
        self.session.modified=True    
    
  













        # item_dict=self.cart.setdefault(str(ShopIT_id),{'price':None,'quantity':0})
        # if update==True:
        #     #when updating the quantity of an existing item
        #     if item_dict['price']!=None:
        #         #checking whether it is already present or not
        #         item_dict['quantity']+=int(quantity)    
        # else:
        #     #when adding a new item to the cart
        #     item_dict['price']=float(quantity)*39.98   #assuming price as 39.98*quantity
        #     item_dict['quantity']=int (quantity)       #making sure that the quantity entered
