import pandas as pd
from sqlalchemy import create_engine
hostname="127.0.0.1"
dbname="Ishu_exceller"
uname="dell"
pwd="incorrect"
data={ "food_item":["Barley","Bran flakes","Quinoa","oat bran muffin","Oatmeal","Popcorn","Brown rice","Bread","Split peas","Lentils","white kidney beans","Chia seeds","Almonds","Pistachios","Sunflower kernels","raw Carrot","raw Cauliflower","boiled Sweet corn","baked Potato","sprouts","Turnip greens","Broccoli","Green peas","Strawberries","Orange","Banana","Apple","Pear","Raspberries"],
       "gm of fibre/gm": [0.038,0.183,0.027,0.044,0.017,0.146,0.018,0.062,0.082,0.078,0.072,0.353,0.123,0.106,0.094,0.025,0.019,0.025,0.023,0.029,0.035,0.032,0.056,0.021,0.021,0.025,0.025,0.031,0.065]}
fibre_df=pd.DataFrame(data)
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))
fibre_df.to_sql('fibre_in_food', engine, index=False)