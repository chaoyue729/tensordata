import os
import time
import json
import requests
import pandas as pd
import tensorflow as tf

def ctrip_hotel_reviews(root):
    """Ctrip hotel reviews datasets.
    
    datasets url:`https://github.com/SophonPlus/ChineseNlpCorpus/blob/
    master/datasets/ChnSentiCorp_htl_all/ChnSentiCorp_htl_all.csv`
    
    Ctrip's review data set contains 7000+ samples, 
    including more than 5,000 positive reviews 
    and more than 2,000 negative reviews
    
    Data storage directory:
    root = `/user/.../mydata`
    mnist data: 
    `root/ctrip_hotel_reviews/ctrip_hotel_reviews.txt`
    Args:
        root: str, Store the absolute path of the data directory.
              example:if you want data path is `/user/.../mydata/ctrip_hotel_reviews`,
              root should be `/user/.../mydata`.
    Returns:
        Store the absolute path of the data directory, is `root/ctrip_hotel_reviews`.
    """
    start = time.time()
    assert tf.gfile.IsDirectory(root), '`root` should be directory.'
    task_path = os.path.join(root, 'ctrip_hotel_reviews')
    if tf.gfile.Exists(task_path):
        tf.gfile.DeleteRecursively(task_path)
    tf.gfile.MakeDirs(task_path)
    url_json = 'https://raw.githubusercontent.com/Hourout/datasets/master/nlp/ctrip_hotel_reviews/ctrip_hotel_reviews.json'
    url_txt = 'https://raw.githubusercontent.com/SophonPlus/ChineseNlpCorpus/master/datasets/ChnSentiCorp_htl_all/ChnSentiCorp_htl_all.csv'
    s = requests.get(url_json)
    with open(os.path.join(task_path, 'ctrip_hotel_reviews.json'), 'w') as outfile:
        json.dump(s.json(), outfile, ensure_ascii=False)
        outfile.write('\n')
    s = requests.get(url_txt).content
    data = pd.read_csv(io.StringIO(s.decode('utf-8')))
    data.to_csv(os.path.join(task_path, 'ctrip_hotel_reviews.txt'), index=False)
    print('ctrip_hotel_reviews dataset download completed, run time %d min %.2f sec' %divmod((time.time()-start), 60))
    return task_path
