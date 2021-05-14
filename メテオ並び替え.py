import sys
import os
import re
import json
from PIL import Image

#画像並び替え
def swap_image(new_img,x,y,img,box):
	crop = img.crop(box)
	#crop.show()
	new_img.paste(crop,(x,y))
	return new_img

#メイン処理
def main(img_path,json_path):
	#ファイル名称設定
	file_name = os.path.basename(img_path)
	split_name = os.path.splitext(file_name)[0]
	file_dir = os.path.dirname(img_path)
	
	#画像準備
	img_org = Image.open(img_path)
	
	with open(json_path,mode="rt") as f:
		data = json.load(f)
		views = data["views"]
		src = data["resources"]["i"]["src"]
		width = views[0]["width"]
		height = views[0]["height"]
		coords = views[0]["coords"]
		
		#出力ファイル設定
		out_name = "c_" + src
		out_path = os.path.join(file_dir,out_name)
	
		#新規画像
		img_new = Image.new("RGB",(width,height),(0,0,255))
		
		#処理開始
		for i in coords:
			m_str = re.findall(r"\d+",i)
			#数値変換
			m = [int(item) for item in m_str]
			x = m[4]
			y = m[5]
			box = (m[0],m[1],m[0]+m[2],m[1]+m[3])
			print(x,y,box)
			img = swap_image(img_new,x,y,img_org,box)
	
		#保存
		img.show()
		img.save(out_path,quality=95)
		print(out_path)

	print(file_dir)

#プログラム実行
if __name__ == "__main__":
	#ファイル入力
	if len(sys.argv) == 1:
		img_path = os.path.abspath("0001.jpg")
		json_path = os.path.abspath("0001.ptimg.json")
		
		main(img_path,json_path)
	else:
		print("ないよ")
