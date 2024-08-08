from audioset_download import Downloader

d = Downloader(root_path='dataset', 
               labels=['Water'], 
               n_jobs=1, 
               download_type='unbalanced_train', 
               copy_and_replicate=False)
d.download(format = 'wav')