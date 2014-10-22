import urllib2
from multiprocessing.dummy import Pool
urls = ['http://www.stuzone.com','http://www.python.org']
pool = Pool()
result = pool.map(urllib2.urlopen,urls)
print result
pool.close()
pool.join()
