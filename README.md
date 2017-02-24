# wqcms6.0-getshell
批量检测wqcms6.0配合iis6.0解析漏洞getshell，根据网上的poc用burpsuit抓包，再用python重构了包，然后批量利用getshell，先用wqCms 6.0.py，检测网上批量抓的url.txt,之后会导出一个文本jieguo.txt,因为这个需要iis6.0的解析漏洞配合，所以就算上传成功了，也不一定可以利用，之后我们再来用结果检测.py来检测一下，jieguo.txt,中的连接，因为可以使用的shell一句话，会返回500错误，我们就把这些返回500的url写入shell.txt.就得到最后的答案了。
