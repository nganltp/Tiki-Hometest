import json

def save_by_asin():
    for review in reviewsList:
        mydict = {}
        asin = review['asin']
        print('asin: ', asin)
        file_name ='Reviews/' + asin + '.json'
        f = open(file_name, 'a+')
        
        mydict['reviewID'] = review['reviewerID']
        mydict['helpful'] = review['helpful']
        f.write(str(mydict)+ '\n')
        f.close()

reviewsList= []
with open('reviews_Office_Products.json') as f:
    for jsonObj in f:
        reviewDict = json.loads(jsonObj)
        reviewsList.append(reviewDict)

print(reviewsList[0]['reviewerID'])



# with open('reviews_Office_Products.json', 'r') as review_file:
#     reviews=review_file.read()

# obj_reviews = json.load(reviews)

# print(obj_reviews[0])
# # for review in reviews:
# #     print(review['reviewerID'])