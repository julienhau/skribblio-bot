#! python3

from PIL import Image
import pyautogui, sys, requests,pprint,json, time
from io import BytesIO

YOUR_KEY = ''

data={
(255,255,255):(300,720),
(0,0,0):(300,745),
(193,193,193):(323,720),
(76,76,76):(323,745),
(239,19,11):(348,720),
(116,11,7):(348,745),
(255,113,0):(371,720),
(194,56,0):(371,745),
(255,228,0):(396,720),
(232,162,0):(396,745),
(0,204,0):(420,720),
(0,85,16):(420,745),
(0,178,255):(443,720),
(0,86,158):(443,745),
(35,31,211):(468,720),
(14,8,101):(468,745),
(163,0,186):(490,720),
(85,0,105):(490,745),
(211,124,170):(516,720),
(167,85,116):(516,745),
(160,82,45):(542,720),
(99,48,137):(542,745)
}



pyautogui.PAUSE = 0.008

word = sys.argv[1]
res = requests.get(f'https://app.zenserp.com/api/v2/search?apikey={YOUR_KEY}={word}&tbm=isch&device=desktop&location=Manhattan,New%20York,United%20States')
res1 = requests.get(json.loads(res.text)['image_results'][0]['sourceUrl'])
img = Image.open(BytesIO(res1.content))
img = img.convert('RGB')
baseheight = 45
hpercent = (baseheight/float(img.size[1]))
wsize = int((float(img.size[0])*float(hpercent)))
img = img.resize((wsize,baseheight), Image.ANTIALIAS)
for x in range(wsize):
	for y in range(45):
		r,g,b = img.getpixel((x,y))
		minValue = 1000000000
		color =()
		for r1,g1,b1 in data.keys():
			value = (r1-r)**2+(g1-g)**2+(b1-b)**2
			if value < minValue:
				minValue = value
				color = (r1,g1,b1)
		pyautogui.click(data[color][0],data[color][1])
		pyautogui.click(229+6*x,135+6*y)
sys.exit()
