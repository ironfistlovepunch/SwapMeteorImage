import os
import sys
import glob
import importlib
import unicodedata
import webbrowser

#unicode正規化対策
name = "メテオ並び替え"
try:
		name_nfc = unicodedata.normalize("NFC",name)
		メテオ並び替え = importlib.import_module(name_nfc)
except ModuleNotFoundError as e:
		#NFC正規化でダメならNFD正規化を試みる
		name_nfd = unicodedata.normalize("NFD",name)
		メテオ並び替え = importlib.import_module(name_nfd)

#ファイルの所在を返す
def get_file_path(path,extension):
	file_name = os.path.basename(path)
	split_name = os.path.splitext(file_name)[0]
	file_dir = os.path.dirname(path)
	
	file_path = os.path.join(file_dir,split_name)
	l = glob.glob(file_path + "*." + extension)
	return l[0]

#入力ファイル関係
print(len(sys.argv))

if len(sys.argv) == 3:
	image = sys.argv[1]
	json = sys.argv[2]
	#work_path = 
else:
	#テスト用
	image = "0003.jpg"
	json = "0003.ptimg.json"
	work_path = "/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/作業用/メテオ画像合成/20210514195727/"
	image = work_path + image
	json = work_path + json

#ファイル所在関連
image_path = get_file_path(image,"jpg")
print(image_path)
json_path = get_file_path(json,"json")
print(json_path)
file_dir = os.path.dirname(image)
print(file_dir)

#呼ぶ
メテオ並び替え.main(image_path,json_path,file_dir)

#戻る
webbrowser.open("workflow://")

