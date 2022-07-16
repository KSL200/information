import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.youtube.com/channel/UCNoYIJQMYLkT3HtdT5Ixe9Q" # https:// 꼭 붙여야 연결됩니다!
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
colors = ["red", "pink"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "강성록")
write("description", "원화중학교 3학년 공식 쪼꼬미 성록이")
write("button", "유튭(아직 서툼)")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "좋아하는거": "사람,동물,게임,핑크핑크,",
  "생일": "2007.9.28",
  "MBTI": "ESFJ",
  "하는 게임": "몬스터 헌터 시리즈(캡콤 짱짱)"
}
information(informations)
