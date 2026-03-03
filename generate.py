import requests
import random
from datetime import datetime
import xml.etree.ElementTree as ET

RSS_URL = "https://www.yna.co.kr/rss/news.xml"

resp = requests.get(RSS_URL, timeout=10)
root = ET.fromstring(resp.content)

titles = []
for item in root.findall(".//item/title"):
    if item.text:
        titles.append(item.text.strip())

selected = random.sample(titles[:20], 3)

today = datetime.now().strftime("%m월 %d일")

content = f"""
{today} 종합 헤드라인 브리핑

"""

for headline in selected:
    content += f"""
“{headline}” (출처: 연합뉴스)

■ 이슈 배경
최근 정책 및 시장 흐름과 연결된 이슈로 보입니다.

■ 시장 영향
단기 변동성 확대 가능성이 있습니다.

■ 체크 포인트
추가 발표 일정과 시장 반응을 확인하세요.

"""

content += """
※ 본 글은 공개된 헤드라인을 참고한 개인 분석이며
기사 본문을 인용하지 않았습니다.
"""

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("완료")
