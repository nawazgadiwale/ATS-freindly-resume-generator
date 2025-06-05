import re
import string

#function to clean and normalize text 
def clean_text(text):
    text = text.lower() #converts to lower case 
    text = re.sub(rf"[{string.punctuation}]","",text)
    #remove puncuation
    return text

#function to extract keywords from job description
def extract_keywords(text, top_n=30):
    text = clean_text(text)
    words = list(set(text.split())) #unique words
    return [word for word in words if len(word)>3][:top_n]

#function to compare keywords from JD and user Input 
def match_keywords(jd_keywords,user_keywords):
    user_keywords = [k.strip().lower() for k in user_keywords]
    return list(set(jd_keywords) & set(user_keywords))
#this returns macthed keywords