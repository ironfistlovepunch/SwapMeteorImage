import importlib
import unicodedata
import appex

#unicode正規化対策
name = "メテオ並び替えzip"
try:
		name_nfc = unicodedata.normalize("NFC",name)
		メテオ並び替えzip = importlib.import_module(name_nfc)
except ModuleNotFoundError as e:
		#NFC正規化でダメならNFD正規化を試みる
		name_nfd = unicodedata.normalize("NFD",name)
		メテオ並び替えzip = importlib.import_module(name_nfd)

#print(appex.is_running_extension())
#print(appex.get_text())

file_path = appex.get_file_path()
#print(file_path)
メテオ並び替えzip.main(file_path)
