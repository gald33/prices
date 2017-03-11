import os
path = "./scrapedfiles/xml/"
renamed_path = "./scrapedfiles/xml_renamed/"
for filename in os.listdir(path):
    print path + filename
    import xml.etree.ElementTree as ET
    tree = ET.parse(path + filename)
    root = tree.getroot()
    print root
    if root.find('ChainId')==None:
		    print "not shupersal"
		    chain_id=root.find('ChainID').text 
		    sub_chain=root.find('SubChainID').text
		    store_id=root.find('StoreID').text 
    else:
		chain_id=root.find('ChainId').text  
		sub_chain=root.find('SubChainId').text
		store_id=root.find('StoreId').text
    print "chain_id" + str(chain_id)
