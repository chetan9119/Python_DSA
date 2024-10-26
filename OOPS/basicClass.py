# class StarCookie: 
#     milk = 0.2
#     def __init__(self, weight, color):
#         self.weight = weight
#         self.color = color
        
#     def __str__(self):
#         return f"Hello {self.color} is ready"
        
# star_cookie1 = StarCookie(2, "Red")
# star_cookie2 = StarCookie(16, "Black")
# print(star_cookie2.milk)
# print(star_cookie2.milk)
# print(StarCookie.milk)

# print(star_cookie2.__dict__)
# print(StarCookie.__dict__)

class YoutubeChannel:    
    def __init__(self, username, subscriber=0, subscriptions=0):
        self.username = username
        self.subscriber = subscriber
        self.subscriptions = subscriptions
        
    def subscribe(self, user):
        user.subscriber += 1
        self.subscriptions += 1
        
    def unsubscribe(self, user):
        user.subscriber -= 1
        self.subscriptions -= 1
  
chetan = YoutubeChannel("Chetan")
mummy = YoutubeChannel("Mummy")

# print(chetan.subscriber)
# print(chetan.subscriptions)
# print(mummy.subscriber)
# print(mummy.subscriptions)


chetan.subscribe(mummy)

# # print(chetan.subscriber)
# # print(chetan.subscriptions)
# print(mummy.subscriber)
# print(mummy.subscriptions)

mummy.subscribe(chetan)  


# print("Mummy Subs details")
# print(mummy.subscriber)
# print(mummy.subscriptions)


# print("Chetan Subs details")
# print(chetan.subscriber)
# print(chetan.subscriptions)


mummy.unsubscribe(chetan)
chetan.unsubscribe(mummy)

print("Mummy Subs details")
print(mummy.subscriber)
print(mummy.subscriptions)


print("Chetan Subs details")
print(chetan.subscriber)
print(chetan.subscriptions)