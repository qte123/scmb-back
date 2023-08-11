# 过滤器
from common.utils.handler import handle_filter


def page_filter(request):
    # 用户访问权限范围
    page_path = request.path[15:]
    student = ['grade.html']
    teacher = ['grade.html', 'index.html', 'CourseManagement.html', 'addCourse.html', 'modifyCourse.html',
               'deleteCourse.html', 'SCManagement.html', 'addSC.html', 'modifySC.html', 'deleteSC.html',
               'StuManagement.html', 'addStudent.html', 'modifyStudent.html', 'deleteStudent.html']
    admin = ['grade.html', 'index.html', 'CourseManagement.html', 'addCourse.html', 'modifyCourse.html',
             'deleteCourse.html', 'SCManagement.html', 'addSC.html', 'modifySC.html', 'deleteSC.html',
             'StuManagement.html', 'addStudent.html', 'modifyStudent.html', 'deleteStudent.html', 'user.html',
             'modifyUser.html', 'deleteUser.html']

    return handle_filter(request, student, teacher, admin, page_path, 1)
