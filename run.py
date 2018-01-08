import sys,time
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2, urllib
from json import *
from selenium import webdriver

username = ""
password = ""

def getPage(cateId):
    data = {
            'status': 1,
            'cateId':cateId
            }
    f = urllib2.Request(
        url     = 'https://try.taobao.com/api3/call?what=show&page=1&pageSize&api=x/search',
        data    = urllib.urlencode(data)
        )
    f.add_header('Host', "try.taobao.com");
    f.add_header('Referer', "https://try.taobao.com/?spm=a1…0799.a214d7j.2.388b746cxcxFEu");
    f.add_header('x-csrf-token', "1WP0qlcjhex9YVHqLaLD");
    f.add_header('Cookie', "thw=cn; isg=AurqQblTRO_D1suljbb2atedOFNM83FcOQAnuHSioD3sp4thXOlZxaKVQ-hF; cna=7ahhEOiw9n8CAXt2BbmlW3af; t=afbbfad84ee0bf5b65c30aa61c414c96; um=6AF5B463492A874D2F84588B3A609B1F36C0293A18C4379FF1E947EBF592DD1804C3F729C139E965CD43AD3E795C914C7A267BD14507698601124454A5056A05; l=AnV1JjvCuW-gvaRXoqt7OfhShfov8ikE; tracknick=jccg20033088999; _cc_=WqG3DMC9EA%3D%3D; _tb_token_=1WP0qlcjhex9YVHqLaLD");
    f.add_header('Accept', "application/json, text/javascript, */*; q=0.01");
    #f.add_header('Accept-Encoding', "gzip, deflate, br");
    f.add_header('Accept-Language', "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2");
    f.add_header('Cache-Control', "no-cache");
    f.add_header('Connection', "keep-alive");
    #f.add_header('Content-Length', "25");
    f.add_header('Content-Type', "application/x-www-form-urlencoded; charset=UTF-8");
    f.add_header('Pragma', "no-cache");
    f.add_header('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0");
    f.add_header('X-Requested-With', "XMLHttpRequest");

    response = urllib2.urlopen(f)
    g = response.read()
    d=JSONDecoder().decode(g)
    
    return d["result"]["paging"]["pages"]
    

def foo(page, cateId): 
    data = {
            'status': 1,
            'cateId':cateId
            }
    f = urllib2.Request(
        url     = 'https://try.taobao.com/api3/call?what=show&page='+str(page)+'&pageSize&api=x/search',
        data    = urllib.urlencode(data)
        )
    f.add_header('Host', "try.taobao.com");
    f.add_header('Referer', "https://try.taobao.com/?spm=a1…0799.a214d7j.2.388b746cxcxFEu");
    f.add_header('x-csrf-token', "1WP0qlcjhex9YVHqLaLD");
    f.add_header('Cookie', "thw=cn; isg=AurqQblTRO_D1suljbb2atedOFNM83FcOQAnuHSioD3sp4thXOlZxaKVQ-hF; cna=7ahhEOiw9n8CAXt2BbmlW3af; t=afbbfad84ee0bf5b65c30aa61c414c96; um=6AF5B463492A874D2F84588B3A609B1F36C0293A18C4379FF1E947EBF592DD1804C3F729C139E965CD43AD3E795C914C7A267BD14507698601124454A5056A05; l=AnV1JjvCuW-gvaRXoqt7OfhShfov8ikE; tracknick=jccg20033088999; _cc_=WqG3DMC9EA%3D%3D; _tb_token_=1WP0qlcjhex9YVHqLaLD");
    f.add_header('Accept', "application/json, text/javascript, */*; q=0.01");
    #f.add_header('Accept-Encoding', "gzip, deflate, br");
    f.add_header('Accept-Language', "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2");
    f.add_header('Cache-Control', "no-cache");
    f.add_header('Connection', "keep-alive");
    #f.add_header('Content-Length', "25");
    f.add_header('Content-Type', "application/x-www-form-urlencoded; charset=UTF-8");
    f.add_header('Pragma', "no-cache");
    f.add_header('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0");
    f.add_header('X-Requested-With', "XMLHttpRequest");
    response = urllib2.urlopen(f)
    g = response.read()
    d=JSONDecoder().decode(g)
    
    return d["result"]["items"]

tryList = []
nowTimeStamp = time.time()

for cateId in ['"1"', '"100"', '"58"','"40"','"21"','"82"','"110"']:
    page =  getPage(cateId)
    for i in xrange(page, 1, -1):
        tList = foo(i, cateId)

        breakFlag = False
        for item in tList:
            endTime = item["endTime"] / 1000
            if (endTime - nowTimeStamp) / 3600 > 24:
                breakFlag = True
                break
            tryList.append([1.0 * item["requestNum"] / item["totalNum"], item["title"], item["id"]])
        if breakFlag:
            break
    

tryList = sorted(tryList, key=lambda d:d[0])
for i in range(15):
    print tryList[i][1],tryList[i][2],tryList[i][0] 


browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://login.taobao.com/member/login.jhtml")
browser.find_element_by_xpath("//a[@class='forget-pwd J_Quick2Static']").click()
browser.find_element_by_xpath("//input[@class='login-text J_UserName']").send_keys(username)
browser.find_element_by_xpath("//input[@class='login-text']").send_keys(password)
time.sleep(3)
browser.find_element_by_id("J_SubmitStatic").click()
time.sleep(5)

for i in range(15):
    tid = tryList[i][2]
    browser.get("https://h5.m.taobao.com/try/detail.htm?tid="+str(tid))
    try:
       time.sleep(1)
       browser.find_element_by_xpath("//button[@class='h5try-ra-button special-none op']").click()
       time.sleep(1)
       browser.find_element_by_xpath("//button[@class='h5try-ra-button special-none btn-submit']").click()
    except:
        pass