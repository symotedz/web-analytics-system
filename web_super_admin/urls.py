from django.urls import path
from . import views , teacher_views, staff_views, student_views, subject_views, fee_views
from . import library_views, exam_views, assignment_views, grade_views, TransportationRequest_views
from . import TransportationStopOrder_views, TransportationStop_views, TransportationRoute_views
from . import Notice_views, Event_views, Plan_views, School_blocks_views, class_block_views
from . import ELearning_views, Message_views, TimeTable_views, ExamResult_views

app_name = 'web_super_admin'

urlpatterns = [
    path('', views.index, name='index'),
    
    # urls for teacher view
    path('teacher_create/', teacher_views.teacher_create, name='teacher_create'),
    path('teachers_detail/', teacher_views.teachers_detail, name='teachers_detail'),
    path('teacher_detail/<int:pk>/', teacher_views.teacher_detail, name='teacher_detail'),
    path('teacher_update/<int:pk>/', teacher_views.teacher_update, name='teacher_update'),
    path('teacher_delete/<int:pk>/', teacher_views.teacher_delete, name='teacher_delete'),
    path('teachers_delete/', teacher_views.teachers_delete, name='teachers_delete'),
    
    # urls for staffs view
    path('staff_create/', staff_views.staff_create, name='staff_create'),
    path('staffs_detail/', staff_views.staffs_detail, name='staffs_detail'),
    path('staff_detail/<int:pk>/', staff_views.staff_detail, name='staff_detail'),
    path('staff_update/<int:pk>/', staff_views.staff_update, name='staff_update'),
    path('staff_delete/<int:pk>/', staff_views.staff_delete, name='staff_delete'),
    path('staffs_delete/', staff_views.staffs_delete, name='staffs_delete'),
    
    # urls for students view
    path('student_create/', student_views.student_create, name='student_create'),
    path('students_detail/', student_views.students_detail, name='students_detail'),
    path('student_detail/<int:pk>/', student_views.student_detail, name='student_detail'),
    path('student_update/<int:pk>/', student_views.student_update, name='student_update'),
    path('student_delete/<int:pk>/', student_views.student_delete, name='student_delete'),
    path('students_delete/', student_views.students_delete, name='students_delete'),
    
    # urls for subjects view
    path('subject_create/', subject_views.subject_create, name='subject_create'),
    path('subjects_detail/', subject_views.subjects_detail, name='subjects_detail'),
    path('subject_detail/<int:pk>/', subject_views.subject_detail, name='subject_detail'),
    path('subject_update/<int:pk>/', subject_views.subject_update, name='subject_update'),
    path('subject_delete/<int:pk>/', subject_views.subject_delete, name='subject_delete'),
    path('subjects_delete/', subject_views.subjects_delete, name='subjects_delete'),
    
    # urls for fees view
    path('fee_create/', fee_views.fee_create, name='fee_create'),
    path('fees_detail/', fee_views.fees_detail, name='fees_detail'),
    path('fee_detail/<int:pk>/', fee_views.fee_detail, name='fee_detail'),
    path('fee_update/<int:pk>/', fee_views.fee_update, name='fee_update'),
    path('fee_delete/<int:pk>/', fee_views.fee_delete, name='fee_delete'),
    path('fees_delete/', fee_views.fees_delete, name='fees_delete'),
    
    # urls for librarys view
    path('library_create/', library_views.library_create, name='library_create'),
    path('librarys_detail/', library_views.librarys_detail, name='librarys_detail'),
    path('library_detail/<int:pk>/', library_views.library_detail, name='library_detail'),
    path('library_update/<int:pk>/', library_views.library_update, name='library_update'),
    path('library_delete/<int:pk>/', library_views.library_delete, name='library_delete'),
    path('librarys_delete/', library_views.librarys_delete, name='librarys_delete'),
    
    # urls for exams view
    path('exam_create/', exam_views.exam_create, name='exam_create'),
    path('exams_detail/', exam_views.exams_detail, name='exams_detail'),
    path('exam_detail/<int:pk>/', exam_views.exam_detail, name='exam_detail'),
    path('exam_update/<int:pk>/', exam_views.exam_update, name='exam_update'),
    path('exam_delete/<int:pk>/', exam_views.exam_delete, name='exam_delete'),
    path('exams_delete/', exam_views.exams_delete, name='exams_delete'),
    
    # urls for assignments view
    path('assignment_create/', assignment_views.assignment_create, name='assignment_create'),
    path('assignments_detail/', assignment_views.assignments_detail, name='assignments_detail'),
    path('assignment_detail/<int:pk>/', assignment_views.assignment_detail, name='assignment_detail'),
    path('assignment_update/<int:pk>/', assignment_views.assignment_update, name='assignment_update'),
    path('assignment_delete/<int:pk>/', assignment_views.assignment_delete, name='assignment_delete'),
    path('assignments_delete/', assignment_views.assignments_delete, name='assignments_delete'),
    
    # urls for grades view
    path('grade_create/', grade_views.grade_create, name='grade_create'),
    path('grades_detail/', grade_views.grades_detail, name='grades_detail'),
    path('grade_detail/<int:pk>/', grade_views.grade_detail, name='grade_detail'),
    path('grade_update/<int:pk>/', grade_views.grade_update, name='grade_update'),
    path('grade_delete/<int:pk>/', grade_views.grade_delete, name='grade_delete'),
    path('grades_delete/', grade_views.grades_delete, name='grades_delete'),
    
     # urls for TransportationRequests view
    path('TransportationRequest_create/', TransportationRequest_views.TransportationRequest_create, name='TransportationRequest_create'),
    path('TransportationRequests_detail/', TransportationRequest_views.TransportationRequests_detail, name='TransportationRequests_detail'),
    path('TransportationRequest_detail/<int:pk>/', TransportationRequest_views.TransportationRequest_detail, name='TransportationRequest_detail'),
    path('TransportationRequest_update/<int:pk>/', TransportationRequest_views.TransportationRequest_update, name='TransportationRequest_update'),
    path('TransportationRequest_delete/<int:pk>/', TransportationRequest_views.TransportationRequest_delete, name='TransportationRequest_delete'),
    path('TransportationRequests_delete/', TransportationRequest_views.TransportationRequests_delete, name='TransportationRequests_delete'),
    
    # urls for TransportationStopOrder_viewss view
    path('TransportationStopOrder_create/', TransportationStopOrder_views.TransportationStopOrder_create, name='TransportationStopOrder_create'),
    path('TransportationStopOrders_detail/', TransportationStopOrder_views.TransportationStopOrders_detail, name='TransportationStopOrders_detail'),
    path('TransportationStopOrder_detail/<int:pk>/', TransportationStopOrder_views.TransportationStopOrder_detail, name='TransportationStopOrder_detail'),
    path('TransportationStopOrder_update/<int:pk>/', TransportationStopOrder_views.TransportationStopOrder_update, name='TransportationStopOrder_update'),
    path('TransportationStopOrder_delete/<int:pk>/', TransportationStopOrder_views.TransportationStopOrder_delete, name='TransportationStopOrder_delete'),
    path('TransportationStopOrders_delete/', TransportationStopOrder_views.TransportationStopOrder_delete, name='TransportationStopOrders_delete'),
    
    # urls for TransportationStop_viewss view
    path('TransportationStop_create/', TransportationStop_views.TransportationStop_create, name='TransportationStop_create'),
    path('TransportationStops_detail/', TransportationStop_views.TransportationStops_detail, name='TransportationStops_detail'),
    path('TransportationStop_detail/<int:pk>/', TransportationStop_views.TransportationStop_detail, name='TransportationStop_detail'),
    path('TransportationStop_update/<int:pk>/', TransportationStop_views.TransportationStop_update, name='TransportationStop_update'),
    path('TransportationStop_delete/<int:pk>/', TransportationStop_views.TransportationStop_delete, name='TransportationStop_delete'),
    path('TransportationStops_delete/', TransportationStop_views.TransportationStop_delete, name='TransportationStops_delete'),
    
    # urls for TransportationRoutes view
    path('TransportationRoute_create/', TransportationRoute_views.TransportationRoute_create, name='TransportationRoute_create'),
    path('TransportationRoutes_detail/', TransportationRoute_views.TransportationRoutes_detail, name='TransportationRoutes_detail'),
    path('TransportationRoute_detail/<int:pk>/', TransportationRoute_views.TransportationRoute_detail, name='TransportationRoute_detail'),
    path('TransportationRoute_update/<int:pk>/', TransportationRoute_views.TransportationRoute_update, name='TransportationRoute_update'),
    path('TransportationRoute_delete/<int:pk>/', TransportationRoute_views.TransportationRoute_delete, name='TransportationRoute_delete'),
    path('TransportationRoutes_delete/', TransportationRoute_views.TransportationRoutes_delete, name='TransportationRoutes_delete'),
    
    # urls for notice view
    path('notice_create/', Notice_views.notice_create, name='notice_create'),
    path('notices_detail/', Notice_views.notices_detail, name='notices_detail'),
    path('notice_detail/<int:pk>/', Notice_views.notice_detail, name='notice_detail'),
    path('notice_update/<int:pk>/', Notice_views.notice_update, name='notice_update'),
    path('notice_delete/<int:pk>/', Notice_views.notice_delete, name='notice_delete'),
    path('notices_delete/', Notice_views.notices_delete, name='notices_delete'),
    
    # urls for Event view
    path('Event_create/', Event_views.Event_create, name='Event_create'),
    path('Events_detail/', Event_views.Events_detail, name='Events_detail'),
    path('Event_detail/<int:pk>/', Event_views.Event_detail, name='Event_detail'),
    path('Event_update/<int:pk>/', Event_views.Event_update, name='Event_update'),
    path('Event_delete/<int:pk>/', Event_views.Event_delete, name='Event_delete'),
    path('Events_delete/', Event_views.Events_delete, name='Events_delete'),
    
    # urls for Event view
    path('Plan_create/', Plan_views.Plan_create, name='Plan_create'),
    path('Plans_detail/', Plan_views.Plans_detail, name='Plans_detail'),
    path('Plan_detail/<int:pk>/', Plan_views.Plan_detail, name='Plan_detail'),
    path('Plan_update/<int:pk>/', Plan_views.Plan_update, name='Plan_update'),
    path('Plan_delete/<int:pk>/', Plan_views.Plan_delete, name='Plan_delete'),
    path('Plans_delete/', Plan_views.Plans_delete, name='Plans_delete'),
    
    # urls for Event view
    path('School_blocks_create/', School_blocks_views.School_blocks_create, name='School_blocks_create'),
    path('School_blockss_detail/', School_blocks_views.School_blockss_detail, name='School_blockss_detail'),
    path('School_blocks_detail/<int:pk>/', School_blocks_views.School_blocks_detail, name='School_blocks_detail'),
    path('School_blocks_update/<int:pk>/', School_blocks_views.School_blocks_update, name='School_blocks_update'),
    path('School_blocks_delete/<int:pk>/', School_blocks_views.School_blocks_delete, name='School_blocks_delete'),
    path('School_blockss_delete/', School_blocks_views.School_blockss_delete, name='School_blockss_delete'),
    
    # urls for Event view
    path('class_block_create/', class_block_views.class_block_create, name='class_block_create'),
    path('class_blocks_detail/', class_block_views.class_blocks_detail, name='class_blocks_detail'),
    path('class_block_detail/<int:pk>/', class_block_views.class_block_detail, name='class_block_detail'),
    path('class_block_update/<int:pk>/', class_block_views.class_block_update, name='class_block_update'),
    path('class_block_delete/<int:pk>/', class_block_views.class_block_delete, name='class_block_delete'),
    path('class_blocks_delete/', class_block_views.class_blocks_delete, name='class_blocks_delete'),
    
    # urls for Elearning view
    path(' ELearning_create/',  ELearning_views.ELearning_create, name='ELearning_create'),
    path(' ELearnings_detail/',  ELearning_views.ELearnings_detail, name='ELearnings_detail'),
    path(' ELearning_detail/<int:pk>/',  ELearning_views.ELearning_detail, name='ELearning_detail'),
    path(' ELearning_update/<int:pk>/',  ELearning_views.ELearning_update, name='ELearning_update'),
    path(' ELearning_delete/<int:pk>/',  ELearning_views.ELearning_delete, name='ELearning_delete'),
    path(' ELearnings_delete/',  ELearning_views.ELearnings_delete, name='ELearnings_delete'),
    
    # urls for Message view
    path(' Message_create/',  Message_views.Message_create, name='Message_create'),
    path(' Messages_detail/',  Message_views.Messages_detail, name='Messages_detail'),
    path(' Message_detail/<int:pk>/',  Message_views.Message_detail, name='Message_detail'),
    path(' Message_update/<int:pk>/',  Message_views.Message_update, name='Message_update'),
    path(' Message_delete/<int:pk>/',  Message_views.Message_delete, name='Message_delete'),
    path(' Messages_delete/',  Message_views.Messages_delete, name='Messages_delete'),
    
    # urls for TimeTable view
    path(' TimeTable_create/',  TimeTable_views.TimeTable_create, name='TimeTable_create'),
    path(' TimeTables_detail/',  TimeTable_views.TimeTables_detail, name='TimeTables_detail'),
    path(' TimeTable_detail/<int:pk>/',  TimeTable_views.TimeTable_detail, name='TimeTable_detail'),
    path(' TimeTable_update/<int:pk>/',  TimeTable_views.TimeTable_update, name='TimeTable_update'),
    path(' TimeTable_delete/<int:pk>/',  TimeTable_views.TimeTable_delete, name='TimeTable_delete'),
    path(' TimeTables_delete/',  TimeTable_views.TimeTables_delete, name='TimeTables_delete'),
    
    # urls for ExamResult view
    path('ExamResult_create/', ExamResult_views.ExamResult_create, name='ExamResult_create'),
    path('ExamResults_detail/', ExamResult_views.ExamResults_detail, name='ExamResults_detail'),
    path('ExamResult_detail/<int:pk>/', ExamResult_views.ExamResult_detail, name='ExamResult_detail'),
    path('ExamResult_update/<int:pk>/', ExamResult_views.ExamResult_update, name='ExamResult_update'),
    path('ExamResult_delete/<int:pk>/', ExamResult_views.ExamResult_delete, name='ExamResult_delete'),
    path('ExamResults_delete/', ExamResult_views.ExamResults_delete, name='ExamResults_delete'),
]
