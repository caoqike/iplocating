import csv
import os
import socket
import requests
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import  mark_safe
from myapp import models
# Create your views here

def index(request):
    # UserInfo.objects.create(name="cqk1", password="12345678")
    # user_list=models.UserInfo.objects.all()
    # return render(request,"myhtml.html",{"user_list":user_list})

    page=int(request.GET.get('page',1))
    #所显示的10条信息
    start=(page-1)*10
    end=page*10

    local_list=models.LocalInfo.objects.all()[start:end]
    cnt=models.LocalInfo.objects.all().count()

    print(cnt)
    total_page_cnt=int(cnt/10)+1

    plus=5
    start_page=page-plus
    end_page=page+plus+1

    if end_page>total_page_cnt:
        start_page=total_page_cnt-10
        end_page=total_page_cnt+1
    if start_page<=0:
        start_page=1
        end_page=start_page+10+1
    #页码
    page_str_list=[]

    page_str_list.append('<li><a href="/index/?page={}">首页</a></li>'.format(1))
    if page>1:
        prev ='<li><a href="/index/?page={}">上一页</a></li>'.format(page-1)
    else:
        prev='<li><a href="/index/?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev)

    if page<total_page_cnt:
        next ='<li><a href="/index/?page={}">下一页</a></li>'.format(page+1)
    else:
        next='<li><a href="/index/?page={}">下一页</a></li>'.format(total_page_cnt)

    for i in range(start_page,end_page):
        if i==page:
            elem='<li class="active"><a href="/index/?page={}">{}</a></li>'.format(i,i)
            page_str_list.append(elem)
        else:
            elem = '<li><a href="/index/?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(elem)
    page_str_list.append(next)
    page_str_list.append('<li><a href="/index/?page={}">尾页</a></li>'.format(total_page_cnt))
    page_string=mark_safe("".join(page_str_list))

    return render(request,"myhtml.html",{"local_list":local_list,"page_string":page_string})
def detect_list(request):
    detect_list = models.Detect.objects.all()
    return render(request, 'detect_list.html',{"detect_list":detect_list})


def home(request):
    if request.method=='GET':
        return render(request,'home.html')
def user_add(request):
    if request.method=='GET':
        return render(request,'user_add.html')
    #获取前端post返回的
    user=request.POST.get('name')
    pwd=request.POST.get('password')
    models.UserInfo.objects.create(name=user,password=pwd)
    return redirect("/user/list")

def detect_add(request):
    if request.method=='GET':
        return render(request,'detect_add.html')
    #获取前端post返回的
    ip=request.POST.get('ip')
    addr=request.POST.get('addr')
    models.Detect.objects.create(ip=ip,addr=addr)
    return redirect("/detect/list")


def process(ip):
    print('tracert loading %s' % ip)
    tracert = os.popen('tracert -d %s' % ip).read()  # 执行1次tracert命令
    with open('tmptracert.txt', 'w', newline='') as f:
        f.writelines(tracert)
    print(tracert)
    with open('tmptracert.txt', 'r', newline='') as f:
        tmp=f.readlines()
        end=len(tmp)-2
        lines=tmp[4:end]
        print(lines)
    routes=[]
    total_row=[]
    myip = socket.gethostbyname(socket.gethostname())
    total_row.append(myip)
    dst_addr = ip
    total_row.append(dst_addr)
    for line in lines:
        row=[]
        if '请求超时' in line:
            continue
        delays = []
        t1 = line[3:9].strip()
        print(t1.strip())
        t2 = line[12:18].strip()
        print(t2.strip())
        t3 = line[21:27].strip()
        print(t3.strip())
        router = line[32:]
        router=router.replace(' \n','')
        print(router)
        for si in delays:
            print(si)
        print(line.rstrip())
        #三个延迟
        delays.append(t1)
        delays.append(t2)
        delays.append(t3)
        #一个路由名
        row.append(router)
        row.append(delays)
        #每个路由及其对应的三个延迟加入到总的路由数组
        routes.append(row)

    total_row.append(routes)

    #将total_row保存到文件
    f = open('query.csv', 'a',newline='')  # open file
    print(f)
    # create the csv writer
    writer = csv.writer(f)
    # write a row to the csv file
    writer.writerow(total_row)
    f.close()

def locate(request):
    if request.method == 'GET':
            return render(request, 'locate.html',{'current_user':request.session["info"]['id'] })

    ip = request.POST.get("ip")
    print(ip)


    if request.session["info"]['id']=='xxxx':

        print('不好意思只能')
        #只提供精确到市级的


    #提供精确信息
    else:

        print('可精确')

        local_obj = models.LocalInfo.objects.filter(ip=ip).first()
        type=0
        if not local_obj:

            url = f'http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query&lang=zh-CN'
            # 其中fields字段为定义接受返回参数，可不传；lang为设置语言，zh-CN为中文，可以传
            res = requests.get(url)  # 发送请求

            data = json.loads(res.text)
            with open('json.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps(data, indent=2, ensure_ascii=False))

            dataJson = json.load(open('json.json', encoding='UTF-8'))  # 打开json文件，并将其中的数据全部读取
            jsondata = [dataJson["country"], dataJson["regionName"], dataJson["city"]]  # 读取json文件中我们需要的部分
            print(jsondata)
            print(dataJson)

            return render(request, 'locate.html', {'current_user': request.session["info"]['id'], 'query_result':dataJson,"type":1})

        else:
            #我们的数据库中有的
            print(local_obj.address)
            return render(request, 'locate.html', {'current_user': request.session["info"]['id'], 'query_result':local_obj,"type":0})



def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    #获取前端post返回的
    user=request.POST.get('name')
    pwd=request.POST.get('password')
    models.UserInfo.objects.create(name=user,password=pwd)
    return redirect("/load/")

def user_list(request):
    user_list=models.UserInfo.objects.all()
    print(user_list)
    return render(request,'user_list.html',{"user_list":user_list})
def tracert_list(request):
    tracert_list = models.TracertResult.objects.all()
    print(tracert_list)
    return render(request, 'tracert_list.html', {"tracert_list": tracert_list})
def  tracert_delete(request):
    nid = request.GET.get('nid')
    models.TracertResult.objects.filter(id=nid).delete()
    tracert_list = models.TracertResult.objects.all()
    return render(request, 'tracert_list.html', {"tracert_list": tracert_list})

class TracertInfo:
    def __init__(self,dist,lastroute,delays):
        self.dist=dist
        self.lastroute=lastroute
        self.delays=delays

#基于tracert最后一跳路由的聚类
def tracert_cluster_last(request):
    tracert_list = models.TracertResult.objects.all()
    cluster_list=[]
    info_list=[]
    for item in tracert_list.values():
        obj=[]
        #dist
        obj.append(item.get('dist'))
        #print(item.get('delays'))
        #解析，获得字符串的倒数第一条路由
        res=item.get('delays').replace("\n",",")
        #print(res)
        li=eval(res)
        print(type(li))
        #lastroute
        obj.append(li[(len(li))-2][0])
        #delays
        obj.append(item.get('delays'))
        info_list.append(obj)

    #遍历倒数第一跳路由
    for i in info_list:
        ti = TracertInfo(i[0], i[1],i[2])
        flag = 0
        #如果是初始为空，则加入该路由
        if len(cluster_list) == 0:
            newlist = []
            newlist.append(ti)
            cluster_list.append(newlist)
            continue
        for item in cluster_list:
            #存在与其路由相同的已加入，则不加入
            if item[0].lastroute == ti.lastroute:
                item.append(ti)
                flag = 1
                break
        #无相同的，加入
        if flag == 0:
            newlist = []
            newlist.append(ti)
            cluster_list.append(newlist)

    display_list = []
    for item in cluster_list:
        tmp=[]
        tmp.append(item[0].lastroute)
        #同一个最后一条路由对应的不同目标IP列表
        dists=[]
        for a in item:
            dists.append(a.dist)
        tmp.append(dists)
        display_list.append(tmp)
        print('---------------------------')
    return render(request,'cluster_last.html',{"display_list":display_list})

class TracertInfo2:
    def __init__(self,dist,lastroute,lastroute2,delays):
        self.dist=dist
        self.lastroute=lastroute
        self.lastroute2 = lastroute2
        self.delays=delays

#基于倒数第二跳以及倒数第一跳的路由聚类。
def tracert_cluster_last2(request):
    tracert_list = models.TracertResult.objects.all()
    cluster_list = []
    info_list = []
    for item in tracert_list.values():
        obj = []
        # dist
        obj.append(item.get('dist'))
        # print(item.get('delays'))
        # 解析，获得字符串的倒数第一条路由
        res = item.get('delays').replace("\n", ",")
        # print(res)
        li = eval(res)
        print(type(li))
        # lastroute
        obj.append(li[(len(li)) - 2][0])

        #lastsecroute

        obj.append(li[(len(li)) - 3][0])
        # delays
        obj.append(item.get('delays'))
        info_list.append(obj)

    # 遍历倒数第二跳路由
    for i in info_list:
        ti = TracertInfo2(i[0], i[1], i[2],i[3])
        flag = 0
        if len(cluster_list) == 0:
            newlist = []
            newlist.append(ti)
            cluster_list.append(newlist)
            continue
        for item in cluster_list:
            #倒数第二条和倒数第一条都一样的才放入相同列表
            if item[0].lastroute == ti.lastroute and  item[0].lastroute2 == ti.lastroute2:
                item.append(ti)
                flag = 1
                break
        if flag == 0:
            newlist = []
            newlist.append(ti)
            cluster_list.append(newlist)

    display_list = []
    for item in cluster_list:
        tmp = []
        tmp.append(item[0].lastroute)
        tmp.append(item[0].lastroute2)
        # 同一个最后一条路由对应的不同目标IP列表
        dists = []

        for a in item:
            dists.append(a.dist)

        tmp.append(dists)

        display_list.append(tmp)

        print('---------------------------')

    return render(request, 'cluster_last2.html', {"display_list": display_list})

def local_add(request):
    if request.method=='GET':
        return render(request,'local_add.html')
    #获取用户的post数据
    ip=request.POST.get("ip")
    print(ip)
    addr=request.POST.get("addr")
    name=request.POST.get("name")
    mail=request.POST.get("mail")

    longitude=request.POST.get("longitude")

    latitude=request.POST.get("latitude")

    models.LocalInfo.objects.create(ip=ip,address=addr,name=name,mail=mail,longitude=longitude,latitude=latitude)
    #保存到数据库
    return redirect("/index")
def user_delete(request):
    nid=request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    user_list = models.UserInfo.objects.all()

    return render(request, 'user_list.html', {"user_list": user_list})

def detect_delete(request):
    nid=request.GET.get('nid')
    models.Detect.objects.filter(id=nid).delete()
    detect_list = models.Detect.objects.all()
    return render(request, 'detect_list.html', {"detect_list": detect_list})

def local_delete(request):
    nid = request.GET.get('nid')
    models.LocalInfo.objects.filter(id=nid).delete()
    return redirect("/index")

def user_edit(request,nid):
    if  request.method=="GET":
        row_object=models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {"row_object": row_object});
    #获取用户提交的更新的信息
    # 获取用户的post数据
    user = request.POST.get('name')
    pwd = request.POST.get('password')
    models.UserInfo.objects.filter(id=nid).update(name=user,password=pwd)
    return redirect('/user/list/')

def detect_edit(request,nid):
    if  request.method=="GET":
        row_object=models.Detect.objects.filter(id=nid).first()
        return render(request, 'detect_edit.html', {"row_object": row_object});
    #获取用户提交的更新的信息
    # 获取用户的post数据
    ip = request.POST.get('ip')
    addr = request.POST.get('addr')
    models.Detect.objects.filter(id=nid).update(ip=ip,addr=addr)
    return redirect('/detect/list/')



def local_edit(request,nid):
    if  request.method=="GET":
        row_object=models.LocalInfo.objects.filter(id=nid).first()
        return render(request, 'local_edit.html', {"row_object": row_object});
    #获取用户提交的更新的信息
    # 获取用户的post数据
    ip = request.POST.get("ip")
    addr = request.POST.get("addr")
    name = request.POST.get("name")
    mail = request.POST.get("mail")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    models.LocalInfo.objects.filter(id=nid).update(ip=ip,address=addr,name=name,mail=mail,longitude=longitude,latitude=latitude)
    return redirect("/index")

