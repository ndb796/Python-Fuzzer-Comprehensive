import requests
from lxml import html
from urllib.parse import urljoin

class BFSCrawler:
    def __init__(self, root):
        # visited: 이미 방문한 URL
        self.visited = {}
        # queue: 방문해야 할 URL 정보가 담겨 있는 큐(방문 큐)
        self.queue = [root]

    def get_url_list(self, url):
        # 현재 URL 방문 처리
        self.visited[url] = 1
        # 해당 URL에서 HTML 문서 파싱
        # JavaScript 관련 코드로 파싱이 불가능한 경우 제외
        try:
            response = requests.get(url, timeout=1.0)
            parsed_html = html.fromstring(response.text)
        except:
            return
        # XPath를 이용해 파싱하는 경우 문자열 깨짐 현상을 방지
        for a_tag in parsed_html.xpath('//a'):
            # href 속성이 없는 태그는 제외
            if a_tag.get('href') is None:
                continue
            # target: 결과적으로 찾은 링크 URL
            target = urljoin(url, a_tag.get('href'))
            # 이미 방문한 URL인 경우 제외
            if target in list(self.visited.keys()):
                continue
            # 방문 큐에 이미 있는 URL인 경우 제외
            if target in self.queue:
                continue
            self.queue.append(target)
    
    def crawl(self, threshold=-1):
        count = 0
        while count is not threshold:
            # 현재 URL 대상으로 파싱 수행
            now = self.queue[0]
            self.get_url_list(now)
            # 가장 앞에 있는 현재 URL(이미 방문한) 삭제
            self.queue = self.queue[1:]
            # 더 이상 방문할 URL이 없는 경우
            if len(self.queue) == 0:
                break
            count += 1
            # 크롤링 진행 상황 출력
            if count % 10 == 0:
                print("processing... [{0}/{1}]".format(count, threshold))

    def print_output(self):
        result_list = list(self.visited.keys())
        for i in result_list:
            print(i)

crawler = BFSCrawler('http://www.dowellcomputer.com/main.jsp')
crawler.crawl(threshold=100)
crawler.print_output()