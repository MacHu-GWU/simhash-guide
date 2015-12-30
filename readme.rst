simhash算法是Google在网页爬虫系统中用来快速检测一个网页的内容是否和数据库中已爬的网页重复或者近似。 相似哈希算法的本质是将两个网页哈希之后, 按位比较两个simhash值, 相同的位越多, 表明两个很相似。 完全一样的网页simhash值一定相同, 不完全一样的网页simhash值可能相同, 但是概率很小。

一共中国学生在读完原始论文之后, 在PyPI社区发布了其Python实现, 链接在这里: https://pypi.python.org/pypi/simhash

原始论文请参考原始论文: Detecting Near-Duplicates for Web Crawling.pdf

本代码库保存了simhash这个库的一些用法例子, 和对其进行了一些性能测试。 测试表明simhash的确在相似性检测上有非常大的优势。但在生产系统中使用simhash, 还有许多数据储存, 查询等工程问题有待解决。鉴于Google未公布其细节, 这一问题还有待研究。