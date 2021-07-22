import os
import sys
import glob
import importlib
import unicodedata
import webbrowser

#unicode正規化対策
name = "メテオ並び替えzip"
try:
		name_nfc = unicodedata.normalize("NFC",name)
		メテオ並び替えzip = importlib.import_module(name_nfc)
except ModuleNotFoundError as e:
		#NFC正規化でダメならNFD正規化を試みる
		name_nfd = unicodedata.normalize("NFD",name)
		メテオ並び替えzip = importlib.import_module(name_nfd)

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

if len(sys.argv) == 2:
	zip = sys.argv[1]
	
else:
	#テスト用
	zip_file = "0003.zip"
	work_path = "/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/作業用/メテオ画像合成/20210514195727/"
	zip = work_path + zip_file

#ファイル所在関連
zip_path = get_file_path(zip,"zip")
print(zip_path)
file_dir = os.path.dirname(zip)
print(file_dir)

#呼ぶ
メテオ並び替えzip.main(zip_path)

#戻る
webbrowser.open("workflow://")

