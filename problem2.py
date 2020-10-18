import json
def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z
     

def cal_helpful(helpFul):
    try:
        return float(helpFul[0]/helpFul[1])
    except:
        return 0.0
import csv
def write_csv(asin, reviewArr, helpful):
    rows = []
    for i in range(len(reviewArr)):
        rows.append([asin, helpful[i],reviewArr[i]])
    with open('result.csv', 'a+') as csvfile: 
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)   
        # csvwriter.writerow(fields)
        csvwriter.writerows(rows)
def write_txt(asin, reviewArr, helpful):
    with open('result.txt', 'a+') as f:
        f.write('asin: ' + asin+'\n')
        f.write('descent helpful: '+ str(helpful)+'\n')
        for data in reviewArr:
            f.write(str(data) +'\n')

def write_json(asin,reviewArr):
    data = {}
    data[asin] = reviewArr
    with open('result.json', 'a+') as f:
        json.dump(data, f)

reviewsList= []
with open('ReviewsList.json') as f:
    for jsonObj in f:
        reviewDict = json.loads(jsonObj)
        reviewsList.append(reviewDict)
asin_pre = ''
reviewArr = []
helpful = []
fields = ['asin', 'helpful', 'review_infor']
with open('result.csv', 'a+') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
for review in reviewsList:
    asin_curr = review['asin']
    if (asin_curr != asin_pre):
        sort_list(reviewArr, helpful)
        # write_csv(asin_curr, reviewArr, helpful)
        # write_txt(asin_curr, reviewArr, helpful)
        # write_json(asin_curr, reviewArr)
        reviewArr = []
        helpful = []
    reviewArr.append(str(review))
    cHelpFul = cal_helpful(review['helpful'])
    helpful.append(cHelpFul)
    asin_pre = asin_curr
    #write vào json