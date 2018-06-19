# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import CourseOrg, CityDesc
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserAskForm
from courses.models import Course
from operation.models import UserFavorite
# Create your views here.


class OrgView(View):
    """课程机构"""
    def get(self, request):
        #所有的课程机构
        all_org = CourseOrg.objects.all()
        #课程机构所在地
        all_city = CityDesc.objects.all()

        #筛选city_id
        city_id = request.GET.get('city', "")

        #热度排序
        hot_order = all_org.order_by("-click_numbers")[:3]

        # 筛选机构
        category = request.GET.get('ct', "")

        # 热度排序
        sorts = request.GET.get('sort', "")

        if city_id:
            all_org = all_org.filter(city_id=int(city_id))

        if category:
            all_org = all_org.filter(category=category)

        if sorts:
            if sorts == "student":
                all_org = all_org.order_by("-students")
            elif sorts == "courses":
                all_org = all_org.order_by("-courses_nums")
        # 统计
        org_count = all_org.count()
        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_org, 3, request=request)
        org = p.page(page)
        return render(request, "org-list.html", {
            "all_org": org,
            "all_city": all_city,
            "org_count": org_count,
            "city_id": city_id,
            "category": category,
            "hot_order": hot_order,
            "sorts": sorts,
        })


class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status";"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        current_page = "home"
        '''
        在Course表中，有一个course_org(课程机构)的外键，在这里通过课程机构（course_org）这个外键进行反向获取课程(course)信息
    class Course(models.Model):
        course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)

        同理，在teacher表中有课程机构的外键，也能通过课程机构这个外键进行反向获取教
    class Teacher(models.Model):
        org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")

        '''
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html',  {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        '''
        在Course表中，有一个course_org(课程机构)的外键，在这里通过课程机构（course_org）这个外键进行反向获取课程(course)信息
    class Course(models.Model):
        course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)

        同理，在teacher表中有课程机构的外键，也能通过课程机构这个外键进行反向获取教
    class Teacher(models.Model):
        org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")

        '''
        current_page = 'course'
        all_courses = course_org.course_set.all()[:3]
        return render(request, 'org-detail-course.html',  {
            'all_courses': all_courses,
            'course_org': course_org,
            'current_page': current_page,
            'has_fav': has_fav
        })


class OrgDescView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        current_page = "desc"
        '''
        在Course表中，有一个course_org(课程机构)的外键，在这里通过课程机构（course_org）这个外键进行反向获取课程(course)信息
    class Course(models.Model):
        course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)

        同理，在teacher表中有课程机构的外键，也能通过课程机构这个外键进行反向获取教
    class Teacher(models.Model):
        org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")

        '''
        return render(request, 'org-detail-desc.html',  {
            'current_page': current_page,
            'course_org': course_org,
            'has_fav': has_fav
        })


class OrgTeacherView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()[:3]
        current_page = "teacher"
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        '''
        在Course表中，有一个course_org(课程机构)的外键，在这里通过课程机构（course_org）这个外键进行反向获取课程(course)信息
    class Course(models.Model):
        course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)

        同理，在teacher表中有课程机构的外键，也能通过课程机构这个外键进行反向获取教
    class Teacher(models.Model):
        org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")

        '''
        return render(request, 'org-detail-teachers.html',  {
            'all_teachers': all_teachers,
            'current_page': current_page,
            'has_fav': has_fav,
            'course_org': course_org,
        })


class AddFavView(View):
    """
    用户收藏,取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get("fav_id", 0)
        fav_type = request.POST.get("fav_type", 0)

        ##request.user这是一个匿名的内置类
        if not request.user.is_authenticated():
            #判断用户是否登录状态
            return HttpResponse('{"status";"fail","msg": "用户未登录"}', content_type='application/json')

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            #如果纪录存在，则表示进行删除收藏
            exist_records.delete()
            return HttpResponse('{"status";"fail","msg": "收藏"}', content_type='application/json')

        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status";"success","msg": "已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status";"fail","msg": "未收藏"}', content_type='application/json')