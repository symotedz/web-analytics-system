from easy_pdf.views import PDFTemplateView

class exam_result_pdf(PDFTemplateView):
    template_name = 'exam_result_pdf.html'


