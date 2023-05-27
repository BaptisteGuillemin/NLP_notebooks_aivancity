import re

text = "Hey Amazon - my packaaaaage never Arriiiiiiiived !!!!!    https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first PLEASE FIX ASAP! @AmazonHelp  #Amazon.”"
    
text = re.sub('http\S+', '', text)
text = re.sub("[^a-zA-Z0-9\s]","", text)
text = re.sub(r'([a-z])\1+', r'\1', text)
    



print(text)






































##
##import re
##
##def clean_tweet(tweet):
##    
##    temp = re.sub("@+","", temp)
##    temp = re.sub("#+","", temp)
##    temp = re.sub(r'http\S+', '', temp)
##    temp = re.sub('[()!?\.*?\]', ' ', temp)
##    temp = re.sub('\[.*?\]',' ', temp)
##    temp = re.sub("[^a-z0-9]"," ", temp)
##    temp = re.sub(r'([a-z])\1+', r'\1', temp)
##    temp = temp.split()
##    #temp = [w for w in temp if not w in stopwords]
##    temp = " ".join(word for word in temp)
##    return temp
##
##tweets = ["Hey Amazon - my packaaaaage never Arriiiiiiiived !!!!!    https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first PLEASE FIX ASAP! @AmazonHelp  #Amazon.”"]
##
##results = [clean_tweet(tw) for tw in tweets]
##print(results)
