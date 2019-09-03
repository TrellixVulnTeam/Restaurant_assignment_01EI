from app import app,db
from tables import Item,Booking,Transaction,Restaurant,User
from flask import request       

@app.route('/api/GetBill',methods=['POST'])
def generateBill():
    restaurant_name=request.json.get('restaurant_name')
    username=request.json.get('username')
    items=request.json.get('items')
    restaurant = Restaurant.query.filter_by(Restaurant_Name=restaurant_name).first()
    user = User.query.filter_by(username=username).first()
    Total_amount=restaurant.Base_Table_Charges
    for item in items:
        item_data=Item.query.filter(Item.Item_Name==item,Item.Restaurant_Id==restaurant.Restaurant_Id).first()
        Total_amount=Total_amount + item_data.Price
    
    transaction=Transaction(User_Id=user.User_Id,Restaurant_Id=restaurant.Restaurant_Id,Total=Total_amount)
    db.session.add(transaction)
    db.session.commit()
    return "Bill is Generated "+"and amount to be paid is " + str(Total_amount)


if __name__ == "__main__":
    app.run(port=5004, debug=True)