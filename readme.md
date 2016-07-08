You need to download the reviews file with this command and unzip

wget http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Cell_Phones_and_Accessories_5.json.gz


gunzip reviews_Cell_Phones_and_Accessories_5.json.gz


python create_ngram_data.py

This will print the ngram and the rating one per line.
