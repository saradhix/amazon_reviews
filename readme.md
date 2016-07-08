You need to download the reviews file with this command and unzip

wget http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Cell_Phones_and_Accessories_5.json.gz
gunzip reviews_Cell_Phones_and_Accessories_5.json.gz
python reviews_Cell_Phones_and_Accessories_5.json

This will print the ngram and the rating one per line.
