#DictionaryEx

menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3', '4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;

print('학생관리시스템v01')
print("="*70, end = '\n\n')

for i in menu:
	print(i, end = '')
print('\n')

print("="*70, end = '\n\n')

while True:
	num = input("메뉴의 번호를 선택하세요:  ")

	if num == "":
		print("Chk", end = '')
	else:
		num = int(num)

	if num == 1:
		print("\t",menu[0], "Algorithm Chk", end = '\n\n')
	elif num == 2:
		print("\t",menu[1], "Algorithm Chk", end = '\n\n')
	elif num == 3:
		print("\t",menu[2], "Algorithm Chk", end = '\n\n')
	elif num == 4:
		print("\t",menu[3], "Algorithm Chk", end = '\n\n')
	elif num == 9:
		print('\t',menu[4], end = '\n')
		print('\t\t\t', "종료합니다.")
		break
	else:
		print("\t","메뉴 번호를 확인하세요", end = '\n\n')

