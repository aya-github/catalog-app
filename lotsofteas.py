from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Item


engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create a dummy user
User1 = User(name="tea drinker 1", email="teadrinker1@example.com")
session.add(User1)
session.commit()

# teas for white tea
category1 = Category(name="White Tea")

session.add(category1)
session.commit()

item1 = Item(name="Silver Needle (Baihao Yinzhen)",
             description="Silver Needle is a white tea produced in Fujian Province in China. It is considered the most expensive variety and most prized white teas. Only top buds (leaf shoots) of the camellia sinensis plant are used to produce the tea. (https://en.wikipedia.org/wiki/Baihao_Yinzhen)",
             category=category1)

session.add(item1)
session.commit()

item2 = Item(name="White Peony (Bai Mudan)",
             description="White Peony is a type of white tea made from both young tea buds and leaves of camellia sinensis plant. It has stronger flavor and greater potency than Silver Needle. (https://en.wikipedia.org/wiki/White_Peony_Tea)",
             category=category1)

session.add(item2)
session.commit()

category2 = Category(name="Green Tea")

session.add(category2)
session.commit()

item3 = Item(name="Sencha",
             description="Sencha is a type of green tea made from whole leaves that are steamed and rolled. It is a most common green tea in Japan and produced throught the season. (https://en.wikipedia.org/wiki/Sencha)",
             category=category2)

session.add(item3)
session.commit()

item4 = Item(name="Gyokuro",
             description="Gyokuro is a type of Sencha according to production methods; however, cultivation method is different. Gyokuro tea leaves are shaded from the sun for at least 20 days prior to harvesting. (https://en.wikipedia.org/wiki/Gyokuro)",
             category=category2)

session.add(item4)
session.commit()

item5 = Item(name="Matcha",
             description="Matcha is finely ground powder of Tencha, the green tea plants that are shade-grown for 3 to 4 weeks prior to harvest. Stems and veins are removed during processing. (https://en.wikipedia.org/wiki/Matcha)",
             category=category2)

session.add(item5)
session.commit()

category3 = Category(name="Oolong Tea")

session.add(category3)
session.commit()

item6 = Item(name="Iron Goddess of Mercy (Tieguanyin)",
             description="Iron Goddess of Mercy is a premium variety of Chinese oolong tea, and the top varieties of the tea are one of the most expensive teas in the world. Iron Goddess of Mercy is originated in Anxi in Fujian province in China. (https://en.wikipedia.org/wiki/Tieguanyin)",
             category=category3)

session.add(item6)
session.commit()

item7 = Item(name="Da Hong Pao (Big Red Robe)",
             description="Da hong Pao is a Wuyi rock tea grown in Wuyi mountains in Fujian Province in China. It is a heavily oxidized, dark oolong tea. It is the most expensive tea in the world. (https://en.wikipedia.org/wiki/Da_Hong_Pao)",
             category=category3)

session.add(item7)
session.commit()

item8 = Item(name="Dong Ding (Frozen Summit)",
             description="Dong Ding is the mountain in the Lugu region of Nantou County in central Taiwan where the tea is cultivated. The tea plants were brought to Taiwan from the Wuyi Mountains in Fujian Province in China about 150 years ago. (https://en.wikipedia.org/wiki/Dong_Ding_tea)",
             category=category3)

session.add(item8)
session.commit()

item9 = Item(name="Jin Xuan (Milk Ooolong)",
             description="Jin Xuan is a variety of oolong tea originated in Taiwan. The tea has light, smooth, creamy, and mily taste. (https://en.wikipedia.org/wiki/Jin_Xuan_tea)",
             category=category3)

session.add(item9)
session.commit()

category4 = Category(name="Black Tea")

session.add(category4)
session.commit()

item10 = Item(name="Assam",
              description="Assam is a black tea named after the region Assam in India. It is mostly grown at or near sea level. The tea has brisk and malty flavor, and it has a strong and bright color. (https://en.wikipedia.org/wiki/Assam_tea)",
              category=category4)

session.add(item10)
session.commit()

item11 = Item(name="English Breakfast Tea",
              description="English breakfast tea is a blend of teas originating from Assam, Ceylon, and Kenya. Interestingly, english breakfas tea appears to have originated in what is now the United States from Colonial times. (https://en.wikipedia.org/wiki/English_breakfast_tea)",
              category=category4)

session.add(item11)
session.commit()

item12 = Item(name="Earl Grey Tea",
              description="Earl Grey tea is traditionaly a black tea blend flavored with bergamot oil. Tea companies have begun producing Earl Grey in other varieties of teas, such as green teas or oolong teas. (https://en.wikipedia.org/wiki/Earl_Grey_tea)",
              category=category4)

session.add(item11)
session.commit()


print("added categories and items!")
