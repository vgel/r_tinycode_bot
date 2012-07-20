#!/usr/bin/env python
import json, sys, os

rawlanguages = json.loads(open(sys.argv[1]).read())
classified = {}
if os.path.exists(sys.argv[2]):
	print "Loading previously classified"
	classified = json.loads(open(sys.argv[2]).read())
done = len(classified)

try:
	for language in rawlanguages:
		if language not in classified:
			print "Language name: " + language + ", URL: " + rawlanguages[language]
			print "File extensions used (comma seperated, \"\" for none: ex .py,.pyc)"
			extensions = filter(lambda x: x!='', raw_input().split(","))
			print "Shebang lines, ex #!/usr/bin/python2,#!/usr/bin/python3,#!/usr/bin/env python"
			shebangs = filter(lambda x: x!='', raw_input().split(","))
			print "Synonyms (case-insensitive), eg javascript,js,jscript,ecmascript. Don't include main name."
			names = filter(lambda x: x!='', raw_input().split(","))
			names.append(language)
			classified[language] = {
				"extensions": extensions,
				"shebangs": shebangs,
				"synonyms": names
			}
finally:
	f=open(sys.argv[2],'w')
	j=json.dumps(classified)
	f.write(j)
	print "Wrote %d bytes (%d languages, %d new)"%(len(j),len(classified),len(classified)-done)