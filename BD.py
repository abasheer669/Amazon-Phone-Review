import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://Ram:9drgskms@cluster0.iqujs.mongodb.net/Filter?retryWrites=true&w=majority")

db=client["Filter"]
p=db["Last"]

"""Ratings greater than 4"""


q1={'rating':{'$gt':3.8}}

rating_count=p.count_documents(q1)

"""Total reviews"""

q2={'total_review':{'$gt':1000}}

total_review_count=p.count_documents(q2)

"""Answer asked"""

q3={'ans_ask':{'$gt':250}}

ans_asked_count=p.count_documents(q3)

"""Customer_review"""

q4={'cust_review_pol':{'$gt':0.0}}

cust_review_count=p.count_documents(q4)

"""Customer_Sub"""

q5={'cust_review_sub':{'$gt':0.5}}

cust_review_sub_count=p.count_documents(q5)

"""Aggregate

p.aggregate([{$group: {id:"$by_info"},Maxrate:{$max:"$rating"}}])"""

q6={'rating':{'$gt':4.0},'cust_review_pol':{'$gt':0.0},'cust_review_sub':{'$gt':0.5},'total_review':{'$gt':1000},'ans_ask':{'$gt':250}}

a1_count=p.count_documents(q6)

"""Out of"""

q7={'by_info':'Samsung','rating':{'$gt':4.0},'cust_review_pol':{'$gt':0.0},'cust_review_sub':{'$gt':0.5},'total_review':{'$gt':1000},'ans_ask':{'$gt':250}}

samsung=p.count_documents(q7)

q8={'by_info':'Apple','rating':{'$gt':4.0},'cust_review_pol':{'$gt':0.0},'cust_review_sub':{'$gt':0.5},'total_review':{'$gt':1000},'ans_ask':{'$gt':250}}

apple=p.count_documents(q8)

"""Analystics"""

print("The follwing  are some mean analytics:\n\n\n")

print("The Number of mobile phones available under criteria \n")

print("1.Rating :" + str(rating_count) +"(>3.8)")

print("2.Total review :"+ str(total_review_count)+"(>1000)")

print("3.Answers :" + str(ans_asked_count) +"(>250)")

print("4.Customer reviewed :" + str(cust_review_count) +"(positive)")

print("5.Customer sub reviewed :" + str(cust_review_sub_count) +"(>0.5)")

print("CONCLUSION")

print("\n\nTotal no of avaliable phones satisfying the given constrain is :"+str(a1_count))

print("\n\nOut of:")

print("\n\t1.Samsung :"+str(samsung))

print("\n\t2.Apple :"+str(apple))

test1=p.find(q7,{'_id':0,'feature':0,'cust_review_pol':0,'cust_review_sub':0,'ans_ask':0,'total_review':0})

print("\n\n\nRecommended Samsung Mobiles:")

j=0

for i1 in test1:
    print(j+1)
    print(i1)
    print("\n")
    j+=1
    
test2=p.find(q8,{'_id':0,'feature':0,'cust_review_pol':0,'cust_review_sub':0,'ans_ask':0,'total_review':0})

print("\nRecommended Apple Mobiles :")
j=0    
for i2 in test2:
    print(j+1)
    print(i2)
    print("\n")
    j+=1












