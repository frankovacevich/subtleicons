import os
import os.path
import json
from shutil import copyfile

otp = []
names = []
for dirpath, dirnames, filenames in os.walk("../icons"):
	for filename in [f for f in filenames if f.endswith(".svg")]:
		if dirpath.replace(".\\","") == "all":
			continue

		if filename in names:
			print("Found duplicate names:",filename)
		names.append(filename)

		file_path = os.path.join(dirpath, filename)

		otp.append({"name":filename.replace(".svg",""),"path":file_path.replace("\\","/").replace("./",""),"category":dirpath.split("\\")[-1].capitalize()})
		copyfile(file_path, ".\\all\\" + filename)

output = open("website/icons.js","w+")
output.write("ICONS=" + json.dumps(otp))
output.close(
