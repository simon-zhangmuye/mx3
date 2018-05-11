# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2018/4/29 23:25'
from .models import Course, Lesson, Video, CourseResource
import xadmin


# Course的admin管理器
class LessonInline(object):
    model = Lesson
    extra = 0

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students', 'get_zj_nums']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name','desc','detail','degree','learn_times','students']
    readonly_fields = ['click_nums','fav_nums']
    ordering = ['-click_nums']
    inlines = [LessonInline]
    model_icon = 'fa fa-etsy'
    list_editable = ['desc','detail']
    refresh_times = [3,5]
    style_fields = {"detail":"ueditor"}
    import_excel =True

    #这段代码是导入excel的，版本冲突结果导致失败
    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']

    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    exclude = ['add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'download', 'add_time']
    exclude = ['add_time']

# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
