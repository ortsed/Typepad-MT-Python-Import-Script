import os
import sys
import site
import timelib
import settings

# Set this to the path to your python library
sys.path.append('/path/to/django/lib')

import connection, transaction
cursor = connection.cursor()

def convert_chars(text):

	conv_table = [
		["\xc3\x84\xc3\xba", "&ldquo;"],
		["\xc3\x84\xc3\xb9", "&rdquo;"],
		["\xc3\x84\xc3\xae", "&mdash;"],
		["\xe2\x80\x9a\xc3\x84\xc3\xb4", "&rsquo;"],
		["\xe2\x88\x9a\xc2\xba", "&uuml;"],
		["\xe2\x80\x9a\xc3\x84\xc2\xa2", "&bull;"],
		["\xe2\x80\x9a\xc3\x84\xc2\xb6", "&hellip;"],
		["\xe2\x80\x9a\xc3\x84\xe2\x89\xa4","&prime;"],
		["\xe2\x88\x9a\xc2\xa9","&eacute;"],
		["\xe2\x88\x9a\xc2\xb0","&aacute;"],
		["\xe2\x80\x9a\xc3\x84\xc3\xb2","&lsquo;"],
		["\xe2\x80\x9a\xc3\x84\xe2\x89\xa5","&Prime;"],
		["\xe2\x88\x9a\xe2\x89\xa0","&iacute;"],
		["\xe2\x80\x9a\xc3\x84\xc3\xb2","&lsquo;"],
		["\xe2\x88\x9a\xc3\x9f","&ccedil;"],
		["\xe2\x88\x9a\xe2\x89\xa5","&oacute;"],
		["\xe2\x88\x9a\xc2\xae","&egrave;"],
		["\xe2\x88\x9a\xe2\x88\x82","&ouml;"],
		["\xe2\x88\x9a\xc3\x98", "&iuml;"],
		["\xe2\x88\x9a\xe2\x88\xab", "&uacute;"],
		["\xe2\x88\x9a\xe2\x89\xa0","&iacute;"],
		["\xe2\x88\x9a\xc2\xb1","&ntilde;"],
		["\xe2\x88\x9a\xe2\x88\x8f","&oslash;"],
		
		["\xe2\x89\x88\xc2\xb0","&scaron;"],
		["\xe2\x88\x9a\xc2\xb4","&euml;"],
		
		["\xe2\x88\x9a\xe2\x89\xa0","&iacute;"],
		["\xc2\xb7\xe2\x88\xab\xc2\xa3", "&#7843;"],
		["\xc6\x92\xc3\xaa\xc2","&#272;"],
		["\xb7\xc2\xaa\xc2\xa9", "&#7913;"],
		["\xe2\x88\x9a\xc2\xa5","&ocirc;"],
		["\xe2\x88\x9a\xc2\xa8", "&igrave;"],
		["\xc2\xb7\xc2\xaa\xc3\xa1","&#7879;"],
		["\xe2\x88\x9a\xc3\x98","&iuml;"],
		["\xe2\x88\x9a\xe2\x84\xa2","&ecirc;"],
		["\xe2\x88\x9a\xe2\x80\xa2","&aring;"],
		["\xe2\x88\x9a\xc2\xa9","&eacute;"],
		["\xe2\x88\x9a\xe2\x80\xa0","&agrave;"],
		["\xe2\x88\x9a\xc3\xba", "&Uuml;"],
		["\xe2\x88\x9a\xc2\xa2","&acirc;"],
		["\xc2\xac\xce\xa9","&frac12;"],
		["\xc2\xac\xc3\xa6","&frac34;"], 
		["\xc2\xac\xe2\x89\xa4","&sup2;"],
		
		["\xe2\x89\x88\xc3\xbc","&#351;"],
		["\xe2\x89\x88\xc3\xbb","&#350;"],
		["\xc6\x92\xe2\x88\x9e","&#304;"],
		["\xe2\x88\x9a\xc2\xaa","&ucirc;"],
		["\xe2\x88\x9a\xc3\x91","&Auml;"],
		
		["\xe2\x89\x88\xc3\xb6","&#346;"],
		["\xc6\x92\xc3\xb4","&#281;"],
		["\xe2\x89\x88\xc3\x91","&#324;"],
		["\xe2\x88\x9a\xc2\xa7","&auml;"],
		["\xe2\x88\x9a\xc3\x86","&icirc;"],
		["\xe2\x88\x9a\xc2\xa7","&auml;"],
		["\xe2\x89\x88\xc3\xab","&#337;"],
		["\xc2\xac\xe2\x88\x9e","&deg;"],
		["\xe2\x88\x9a\xc2\xb4","&euml;"],
		["\xe2\x88\x9a\xe2\x89\xa4","&ograve;"],
		["\xe2\x89\x88\xce\xa9","&#381;"],
		["\xe2\x89\x88\xc3\xa6","&#382;"],
		["\xe2\x88\x9a\xcf\x80","&ugrave;"],
		["\xe2\x88\x9a\xc2\xa3","&atilde;"],
		["\xe2\x88\x9a\xc3\xa2","&Eacute;"],
		["\xe2\x88\x86\xe2\x88\x9e","&#432;"],
		["\xc2\xb7\xc2\xaa\xc3\xb4","&#7897;"],
		["\xe2\x88\x9a\xe2\x88\x9e","&eth;"],
		["\xc3\xbf\xc2\xae\xc5\xb8\xc3\xa4","&#1610;"],
		["\xe2\x88\x9a\xc3\xb34","&times;"],
		["\xe2\x88\x9a\xc3\x85","&Aacute;"],
		["\xc2\xac\xe2\x88\x91","&middot;"],
		
		["\xe2\x80\x9a\xc3\x84\xc3\xac",""],
		["\xc2\xac\xe2\x89\xa0",""],
		["\xe2\x80\x9a&","&"]
	]
	#text = text.encode()
	for row in conv_table:
		text = text.replace(row[0], row[1])
	return text

file = raw_input('MT/Typepad export file to be imported: ')
g = open(file, 'r', 0)

line_number = 0
author =''
title =''
basename = ''
date = ''
body = ''
extended = ''
keywords =''
excerpt = ''
section = 0

total_errors = 0

while True:

	
	line = g.readline()
	
	line_number = line_number + 1
	status = 'publish'

	
	
	if line =='--------\n':
		if status != 'draft':
			
			try:
				cursor.execute("INSERT INTO mt_entry (entry_title, entry_basename, entry_blog_id, entry_created_on, entry_authored_on, entry_status, entry_author_id, entry_text, entry_text_more, entry_keywords, entry_excerpt) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [convert_chars(title), convert_chars(basename), 1, date, date, 2,  4750, convert_chars(body), convert_chars(extended), convert_chars(keywords), convert_chars(excerpt)])
				transaction.commit_unless_managed()
			except Warning as war:
				total_errors = total_errors + 1
				print(war)
				#pdb.set_trace()
				#print("\r\r")
				print ('INSERT INTO mt_entry (entry_title, entry_basename, entry_blog_id, entry_created_on, entry_authored_on, entry_status, entry_author_id, entry_text, entry_text_more, entry_keywords, entry_excerpt) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' %
				(
					convert_chars(title), 
					convert_chars(basename), 
					1, 
					date, 
					date, 
					2, 
					4750, 
					convert_chars(body), 
					convert_chars(extended), 
					convert_chars(keywords), 
					convert_chars(excerpt)
				))


			
		line_number=0
		section = 0
		author =''
		title =''
		status = 'publish'
		basename = ''
		date = ''
		body = ''
		extended = ''
		keywords =''
		excerpt = ''
		
	elif line_number in [1,4,5,6]:
		pass
	elif line_number == 2:
		#title
		title = line[7:-1]
	elif line_number == 3 and line[8:] == 'Draft':
		status = 'draft'
	elif line_number == 7:
		basename = line[10:-1]
	elif line_number == 9:
		try:
			date = timelib.strtodatetime(line[6:]).strftime("%Y-%m-%d %I:%M:%S")
		except:
			date = '0000-00-00 00:00:00'
	elif line_number > 11:

		if line == '-----\n' :
			section = section + 1
		elif section == 0:
			if line != 'BODY:\n':
				body = body + '\n' + line
		elif section == 1:
			if line != 'EXTENDED BODY:\n':
				extended = extended + '\n' + line
		elif section == 2:
			if line != 'EXCERPT:\n':
				excerpt = excerpt + '\n' + line
		elif section == 3:
			if line != 'KEYWORDS:\n':
				keywords = keywords + '\n' + line
	
	
	
	if not line:
		break
	

print "Total errors: " + total_errors

