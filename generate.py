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

if len(titles) < 3:
    raise Exception("헤드라인이 3개 미만입니다.")

selected = random.sample(titles[:20], 3)

today = datetime.now().strftime("%Y년 %m월 %d일")
main_keyword = selected[0].split()[0]

blog_title = f"{today} 주요 뉴스 분석 | {main_keyword} 이슈 정리"

content = f"""
<h2>{today} 종합 뉴스 브리핑</h2>

<p>오늘 주요 이슈를 종합적으로 정리했습니다.
아래 내용은 공개된 뉴스 헤드라인을 기반으로 한 분석입니다.
기사 본문을 인용하지 않았습니다.</p>
"""

for headline in selected:
    content += f"""
<h3>{headline}</h3>

<p><strong>이슈 개요</strong><br>
최근 정책 및 시장 흐름과 연결된 사안으로 주목받고 있습니다.</p>

<p><strong>영향 분석</strong><br>
단기적으로는 심리적 변동성이 나타날 수 있으며,
중장기적으로는 정책 방향이 중요하게 작용할 수 있습니다.</p>

<p><strong>체크 포인트</strong><br>
공식 발표 일정과 추가 지표를 지속적으로 확인하는 것이 필요합니다.</p>
"""

content += """
<hr>
<p><em>※ 본 글은 공개된 뉴스 헤드라인을 참고한 개인 분석 콘텐츠입니다.
투자 판단의 책임은 본인에게 있습니다.</em></p>
"""

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(blog_title + "\n\n" + content)

print("완료")
