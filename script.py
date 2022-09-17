import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.leagueoflegends.com/ko-kr/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["#E0FFF", "#00FF00"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "최장우")
write("description", "안녕하세요 대곡중학교 15살 입니다")
write("button", "instagram")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "제목1": "롤",
  "제목2": "플스",
  "제목3": "유튜브",
  "제목4": "웹툰"
}
information(informations)
