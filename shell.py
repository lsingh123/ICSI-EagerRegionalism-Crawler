Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import twittersearch
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import twittersearch
ModuleNotFoundError: No module named 'twittersearch'
>>> import twittersearch
>>> object = twittersearch.TwitterSearch
>>> object.SearchTwitter(['geoblocking', 'not available in your country', 'ban users from', 'ban an entire country', 'no access in'], 100)
>>> 
