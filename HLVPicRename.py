# -*- coding:UTF-8 -*-
import os 
import shutil



def create_path(path):
	"""判斷資料夾路徑不存在就建立"""
	if not os.path.isdir(path):
		os.makedirs(path)


def get_file_name_type(fileName):
    """取得檔名與副檔名"""
    eles = fileName.split('.')
    if len(eles) > 1:
        fName = '.'.join(eles[0:-1])
        fType = eles[-1]        
    else:
        fName = eles[0]
        fType = ''        
    return fName, fType
	
	
def get_qualify_files(readPath, fileTypes):
	"""取得符合副檔名的檔案,"""
	qualifyFiles = []
	files = os.listdir(readPath)
	for f in files:
		fPath = os.path.join(readPath, f)
		if os.path.isfile(fPath):
			try:
				fName, fType = get_file_name_type(f)
				if fType.lower() in fileTypes:
					qualifyFiles.append(f)
			except ValueError:
				if get_file_name_type(f)[-1] not in fileTypes:
					return None
				else:	
					print(f+"請檢視檔案名稱")
	return 	qualifyFiles


def bubbleSort(x):
	"""泡沫排序法, 由小到大排序"""
	matrix = []
	i = len(x)-1
	while (i > 0):
		j = 0
		while (j < i):
			if (x[j] > x[j+1]):
				matrix = x[j+1]
				x[j+1] = x[j]
				x[j] = matrix
			j += 1
		i -= 1
	return x


def exam_length(column, length, message, equal=False):
	"""	判斷資料長度 
		column 是要判斷的變數 
		length 是要求的長度 
		message 是錯誤時顯示訊息
	"""
	if equal:
		if len(column) != length:
			print(message)
			return False
	else:
		if len(column) > length:
			print(message)
			return False		
	
	return True




if __name__ == '__main__':
	while 1:
		attention = """=== 注意事項： ===\n1、僅能讀取JPG、JPEG檔案\n2、請將圖檔與執行檔放於同一資料夾內
3、稅號須連續,掃描時先掃同一圖資別, 且須為同一頁次（如稅號01010101000~01010101500,皆為總表,且頁次0）
4、程式會對圖檔原檔名排序進行重新命名, 因此掃描時請按照稅號順序由小到大掃描, 且掃描圖檔檔名需有規則性,如有流水號或時間戳記
5、資料夾內請勿放不相干的圖檔,避免順序混亂"""
		input(attention+"\n=== Press Enter to Continue... ===\n")
		
		picTypes = ["00", "01", "02", "03", "04", "05", "99"]
		picTypesCh = ["總表", "稅籍資料卡", "平面圖", "附件", "公設分攤表", "公設建物測量成果圖", "稅籍資料卡+平面圖"]
		
		# 讀取圖檔
		while 1:
			readPath = r"./"		# 讀取的資料夾為程式所在資料夾
			movePath = r"./OriginalFiles\\"	
			destPath = r"./RenameFiles\\"
			create_path(movePath)
			create_path(destPath)
			fileTypes = ['jpg', 'jpeg']		# 副檔名限定jpg或jpeg
			
			qualifyFiles = get_qualify_files(readPath, fileTypes)
			picQuantity = len(qualifyFiles)
			
			if not picQuantity:
				input("=== 圖檔不存在, 請將圖檔與執行檔放置於同一資料夾, 完成後請按Enter ===")
				continue
			else:	
				qualifyFiles = bubbleSort(qualifyFiles)
				zeroMK = False
				break
		
		# 輸入房屋稅號
		while 1:
			hou_losnStart = input("請輸入房屋稅號起號(11位)：")
			if hou_losnStart[0] == "0":		# 判斷房屋稅號開頭是否為0
				zeroMK = True
			
			if not exam_length(hou_losnStart, 11, "房屋稅號長度不正確!", equal=True):
				continue
			
			try:
				ihou_losnStart = int(hou_losnStart)
			except:
				print("房屋稅號格式不正確!")
				continue

			break
		
		
		# 選擇圖資別
		for i, picTypeCh in enumerate(picTypesCh):
			print("({}){}".format(i+1, picTypeCh))
		
		while 1:	
			choosePicType = input("請選擇圖資別：")
			try:
				ichoosePicType = int(choosePicType)
			except:
				print("無此選項, 請重新輸入!")
				continue			
				
			if not 1 <= ichoosePicType <= len(picTypes):
				print("圖資別錯誤, 請重新輸入!")
				continue
			else:
				picType = picTypes[ichoosePicType-1]
			break

		
		# 輸入版次
		while 1:
			version = input("請輸入版次：")
			if not exam_length(version, 3, "版次僅可輸入0~999", equal=False):
				continue

			try :
				iversion = int(version)
			except:
				print("版次輸入格式錯誤, 請重新輸入!")
				continue
			
			if not 0 <= iversion <= 999:			
				print("版次輸入錯誤, 請重新輸入!")
				continue
			else:
				CLenVesrsion = 3-len(version)	# C是補集
				version = "0"*CLenVesrsion + version
			break	


		# 輸入頁次
		while 1:
			page = input("請輸入頁次：")
			if not exam_length(page, 3, "頁次僅可輸入1~999", equal=False):
				continue
				
			try :
				ipage = int(page)
			except:
				print("頁次輸入格式錯誤, 請重新輸入!")
				continue

			if not 0 < ipage <= 999:			
				print("頁次輸入錯誤, 請重新輸入!")
				continue
			else:
				CLenPage = 3-len(page)	# C是補集
				page = "0"*CLenPage + page
			break

		
		# 輸入房屋稅號間隔
		while 1:
			interval = int(input("請輸入房屋稅號間隔："))
			try:
				int(interval)
			except:
				print("房屋稅號間隔格式不正確!")
				continue
			break
		
		
		# 房屋稅號開頭為0須補0
		if zeroMK:
			hou_losnEnd = "0"+str(ihou_losnStart+interval*(picQuantity-1))
		else:
			hou_losnEnd = str(ihou_losnStart+interval*(picQuantity-1))
		
		# 列出圖檔數、預計房屋稅號起訖及圖資別等供使用者參考
		print("【圖檔數】：{} 【房屋稅號起號】：{} 【預計終號】：{}".format(picQuantity, hou_losnStart, hou_losnEnd))
		print("【圖資別】：{} 【版次】：{} 【頁次】：{}".format(picTypesCh[ichoosePicType-1], version, page))

		if input("錯誤請輸入N,並檢查原檔名 (N)離開/(其他)繼續：").upper() == "N":
			os._exit(0)

		print("\n")
		
		
		# 決定新檔名
		i = 0
		duplicate = []	# 紀錄無法重新命名的檔案
		for pic in qualifyFiles:
			fName, fType = get_file_name_type(pic)
			if zeroMK:
				newFileName = "0" + str(ihou_losnStart+i) + picType + version + page + "." + fType
			else:
				newFileName = str(ihou_losnStart+i) + picType + version + page + "." + fType
				
			source = os.path.join(readPath, pic)
			dest = os.path.join(destPath, newFileName)
			moveDest = os.path.join(movePath, pic)		
			
			if not os.path.exists(dest):
				# 複製檔案並以新檔名命名
				shutil.copy2(source, dest)
				print("原始檔名：{} 新檔名：{}".format(pic, newFileName))
				shutil.move(f"{source}", moveDest)
			else:
				duplicate.append(pic)
			i += interval
		
		
		print("\n【檔案重新命名完成, 請查看{}】".format(str(os.getcwd()+destPath)))
		print("\n【原檔案移動至{}】".format(str(os.getcwd()+movePath)))
		if len(duplicate) > 0:
			print("=== 以下無法重新命名,新檔名已存在: ====")
			print("{} ".format(str("\n".join(duplicate))))
			
		input("=== Press Enter to Continue... ===\n")
