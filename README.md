
# UDOps APIs

Purpose
Django API’s are one of the most important aspects while we are developing UI for our UDops package. There are several APIs which are supposed to be used in the first phase of API development which are as follows:
1.Count
2.Summary
3.List
4.Search
5.Update


Steps We performed to host above APIs are:

1.As Udops utility is python based we are using django APIs.
  For initiating Django project run command as: python3 manage.py runserver IP_Address:8000
2.You will get ip address from EC2 instance console as Public IPv4 DNS
  Current Public DNS =ec2-3-134-192-71.us-east-2.compute.amazonaws.com
Note: If you restart or reboot your instance then Public IPv4 DNS ID will get change and you have to add that id in “ALLOWED_HOSTS” of setting.py file of django project as below,

To see output in postman install “POSTMAN” in your local machine and run all APIs as per below instructions.
1. Count : To get count of all corpuses.
Argument: None
Request method : ‘GET’
URL is in format = Public_DNS:port_number/APIName/
Enter the above URL only in postman and click on send button.
NOTE : Public DNS will change according to the EC2 instance.

2. Summary: To get Summary of all corpuses by passing argument as any of the column names of corpus_metadata table.
Argument: “Column” Eg.  {“column”:”language”}
Request method = ‘GET’
URL is in format = Public_DNS:port_number/APIName/
Here pass the argument in postman in the json format and it will give you the following output.
NOTE : Public DNS will change according to the EC2 instance.

3. List: To get List of all corpuses by passing substring of “language or source type”	
Argument : “search_string” Eg.  {“search_string”:”eng”}
Request method = ‘POST’
URL is in format = Public_DNS:port_number/APIName/
Here pass the argument in postman as json format.             
Enter a “search_string” related to either language column or source_type column and it will give the following output.
NOTE : public dns will change according to instance

4. Search: To Search corpuses by passing substring of "corpus_name”	
Argument : “search_string”  Eg.  {“search_string”:”ing ”} substring of corpus_name.
Request method = ‘POST’
URL is in format = Public_DNS:port_number/APIName/
Here pass the argument in postman as json format. 
This “search_string” will be related to the corpus_name column and it will give the following output.
NOTE : public dns will change according to instance

5. Update: To upsert corpus which exists in metadata table
Attribute:corpus_name,corpus_type,language,source_type,Customer_name,data_domain_name 
Eg.     {"corpus_id":"1","corpus_name":"hinglish","corpus_type":"nlp","language":"marathi","source_type":"AAA","customer_name":"dataeaze","data_domain_name":"CCCCC"} 
Request method = ‘PUT’
URL is in format = Public_DNS:port_number/APIName/
Here pass the argument in postman as json format
Here it will update : corpus_type, language, source_type, customer_name, data_domain_name             
NOTE : public dns will change according to instance

6. donut:  This api will give distinct counts of language, corpus_type, source_type , vendor, domain_name  .    
Argument: “Column” Eg.  {“column”:”source_type”}
Request method = ‘GET’
URL is in format = Public_DNS:port_number/APIName/
Here pass the argument in postman in the json format and it will give you the following output.
NOTE : Public DNS will change according to the EC2 instance.
