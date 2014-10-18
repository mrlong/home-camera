import Kuaipan
import time
from config import *



#a = Kuaipan.KuaipanOAuth(consumer_key, consumer_secret);
#print a.GetRequestToken();

#print a.GetAccessToken('585060741');


kuaipan_file = Kuaipan.KuaipanFile(consumer_key, consumer_secret, oauth_token, oauth_token_secret)

#print kuaipan_file.account_info();

 
#print kuaipan_file.upload_file('a.jpg',kuaipan_dir);

#myfile_kuaipan = ;

myfilename = time.strftime("%Y-%m-%d_%H%M%S")  + '.jpg';

print kuaipan_file.upload_file('a.jpg', kuaipan_path='/pi-img/'+myfilename, ForceOverwrite=True);


