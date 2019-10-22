import re
import os
from datetime import datetime
from stanfordcorenlp import StanfordCoreNLP

file_path = r"C:\Users\i847808\Desktop"
new_file_path = r"C:\Users\i847808\Desktop\newLogs"
filename = r"Fieldglasslogs.txt"
timestamp = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day) + str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second)
new_file_name = timestamp + "_" + filename
regex_email = r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+'
regex_name = r'([A-Z][a-z]+(?: [A-Z][a-z]\.)? [A-Z][a-z]+)'
regex_ssn = r'(\d{3}-\d{2}-\d{4})'
regex_address = r'\d{1,4}( \w+){1,5}, (.*), ( \w+){1,5}, (AZ|CA|CO|NH|IL), [0-9]{5}(-[0-9]{4})?'


class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000 )# , quiet =False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'dict'
        }

    def ner(self, sentence):
        return self.nlp.ner(sentence)

def process_file():

 with open(file_path + "\\" + filename, 'r') as f_in:
  lines = f_in.readlines()
  if lines != "\n":
   if os.path.exists(new_file_path):
    f = open(new_file_path + "\\" + new_file_name,'w+')

    for item in lines:
      if bool(re.search(regex_ssn,item)) == True:   ## SSN
        new_line = item.replace(item,"  SSN removed  ")
        print("SSN no " + item + " at line number " + str(lines.index(item)) + " at position " + str(item.index(item) ) )
        f.write(new_line + " ")

      if bool(re.search(regex_email,item)) == True:   ## SSN
        new_line = item.replace(item,"  Email removed  ")
        print("Email address " + item + " at line number " + str(lines.index(item)) + " at position " + str(item.index(item) ) )
        f.write(new_line + " ")

      if bool(re.search(regex_address,item)) == True: ## Address
        new_line = item.replace(item,"  Address removed  ")
        print("Address " + item + " at line number " + str(lines.index(item)) + " at position " + str(item.index(item) ) )
        f.write(new_line + " ")

      else: f.write(item + " ")
    f.close()

def main():
 try:
   os.stat(new_file_path)
 except:
   os.mkdir(new_file_path)

 process_file()

if __name__ == "__main__":
 main()