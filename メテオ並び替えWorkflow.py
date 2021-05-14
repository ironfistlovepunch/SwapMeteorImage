import sys
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

print(sys.argv[1],sys.argv[2])
#呼ぶ
メテオ並び替え.main(sys.argv[1],sys.argv[2])

#戻る
webbrowser.open("workflow://")
