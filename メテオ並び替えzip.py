import importlib
import sys
import os

import unicodedata
import datetime
import zipfile
import shutil

#unicode正規化対策
name = "メテオ並び替え"
try:
		name_nfc = unicodedata.normalize("NFC",name)
		メテオ並び替え = importlib.import_module(name_nfc)
except ModuleNotFoundError as e:
		#NFC正規化でダメならNFD正規化を試みる
		name_nfd = unicodedata.normalize("NFD",name)
		メテオ並び替え = importlib.import_module(name_nfd)

#？？？
def 確認(zip_name):
	print(zip_name)

#メイン処理
def main(zip_name):
	#処理日時
	now = datetime.datetime.now()
	now_str = now.strftime("%Y%m%d%H%M%S")
	
	#作業フォルダ関連
	zip_dir = os.path.dirname(zip_name)
	temp = os.path.join(zip_dir,"files_" + now_str)
	source = os.path.join(temp,"source")
	#出力フォルダ
	out_dir = os.path.join(temp,"c")
	#出力ファイルの圧縮名
	out_zip = os.path.join(zip_dir,"c")

	#フォルダ作成
	os.makedirs(out_dir)

	#解凍、リスト作成
	with zipfile.ZipFile(zip_name) as z:
		#リスト作成
		name_list = sorted(z.namelist())
		jpg_list = [s for s in name_list if 'jpg' in s]
		json_list = [s for s in name_list if "json" in s]
		#解凍
		z.extractall(source)

	#呼び出し
	for i,jpg in enumerate(jpg_list):
		jpg_name = os.path.join(source,jpg)
		json_name = os.path.join(source,json_list[i])
		メテオ並び替え.main(jpg_name,json_name,out_dir)
	
	#圧縮
	shutil.make_archive(out_zip,"zip",out_dir)

#プログラム実行
if __name__ == "__main__":
	#ファイル入力
	if len(sys.argv) == 1:
		originalfiles = os.path.abspath("originalfiles.zip")
	else:
		originalfiles = sys.argv[1]

	main(originalfiles)
