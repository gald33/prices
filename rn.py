from datetime import datetime
import pytz
import os
import xml.etree.ElementTree as ET

def rename_xml():
    time = datetime.now(tz=pytz.timezone('Asia/Jerusalem')).strftime("%Y%m%d")

    path = "./scrapedfiles/xml/"
    renamed_path = "./scrapedfiles/xml_renamed/"
    for filename in os.listdir(path):
        et = ET.parse(path + filename)
        root = et.getroot()
        if root.find('ChainId')==None:
            #print "not shupersal"
            chain_id=root.find('ChainID').text 
            sub_chain=root.find('SubChainID').text
            store_id=root.find('StoreID').text 
        else:
		    chain_id=root.find('ChainId').text  
		    sub_chain=root.find('SubChainId').text
		    store_id=root.find('StoreId').text
        #print "Time: " +str(time)
        #print "chain_id",chain_id
        #print "store_id",store_id
        #print "sub_chain", sub_chain
	
        os.rename(path + filename, renamed_path + "prices-"+chain_id+"-"+sub_chain+"-"+store_id+"-"+ time)
