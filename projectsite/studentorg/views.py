from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, Student, OrgMember, College, Program
from studentorg.forms import OrganizationForm, StudentForm, OrgMemberForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy

class HomePageView(ListView):   
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

########################## ORGANIZATION ##########################
########################## ORGANIZATION ##########################
########################## ORGANIZATION ##########################

class OrganizationList(ListView) :
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView) :
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView) :
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView) :
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

########################## ORG MEMBER ##########################
########################## ORG MEMBER ##########################
########################## ORG MEMBER ##########################

class OrgMemberList(ListView) :
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmem_list.html'
    paginate_by = 5

class OrgMemberCreateView(CreateView) :
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmem_form.html'
    success_url = reverse_lazy('orgmem-list')

class OrgMemberUpdateView(UpdateView) :
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmem_form.html'
    success_url = reverse_lazy('orgmem-list')

class OrgMemberDeleteView(DeleteView) :
    model = OrgMember
    template_name = 'orgmem_del.html'
    success_url = reverse_lazy('orgmem-list')

########################## STUDENT ##########################
########################## STUDENT ##########################
########################## STUDENT ##########################

class StudentList(ListView) :
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5

class StudentCreateView(CreateView) :
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView) :
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView) :
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

########################## COLLEGE ##########################
########################## COLLEGE ##########################
########################## COLLEGE ##########################

class CollegeList(ListView) :
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

class CollegeCreateView(CreateView) :
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView) :
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView) :
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

########################## PROGRAM ##########################
########################## PROGRAM ##########################
########################## PROGRAM ##########################

class ProgramList(ListView) :
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5

class ProgramCreateView(CreateView) :
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView) :
    model = Program
    form_class = ProgramForm
    template_name = "program_form.html"
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView) :
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')


# Create your views here.s
