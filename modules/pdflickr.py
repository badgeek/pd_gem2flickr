# WEB -> PD
# PD -> WEB
# iyok@deadmediafm.org

print "\n\n--- FLICKR PY EXTERNAL"
print "--- by iyok@deadmediafm.org"

try:
	import flickrapi
	import urllib
	import pyext
	import string
	import os,sys
except:
	print "ERROR!! FCK!"

class pdflickteria(pyext._class):
	
	_inlets  = 2
	_outlets = 2
	
	token_path = './flickrtokens'
	
	flickr = flickrapi


	def init_1(self, *args):
		# // init flickr
		print "-- pdflickr init loading"
		
		self.api_key = str(args[0])
		self.api_secret = str(args[1])
		
		self.flickr = flickrapi.FlickrAPI(self.api_key,self.api_secret)
		
		self.flickr.token.path = self.token_path
		
		(token, frob) = self.flickr.get_token_part_one(perms='write')
		if not token: raw_input("Press ENTER after you authorized this program")
		self.flickr.get_token_part_two((token, frob))
		print "-- pdflickr init ok"
	
	def upload_2(self,*args):
		temp = list(args)
		arg_list = list()
		for item in temp:
			arg_list.append(str(item))
		value = string.join(arg_list,' ')
		print "-- pdflickr uploading..."
		self.flickr.upload(filename=value)
		print "-- pdflickr upload ok"