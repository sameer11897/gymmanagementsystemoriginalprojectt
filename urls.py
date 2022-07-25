"""gymanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as uviews
from gymmanager import views as gviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',uviews.home,name='home'),
    path('register/', uviews.register, name="register"),
    path('checkregister/', uviews.checkregister, name="checkregister"),
    path('userlogin/',uviews.userlogin,name='userlogin'),
    path('checklogin/', uviews.checklogin, name="checklogin"),
    path('fgpassword/',uviews.fgpassword,name='fgpassword'),
    path('adminlogin/',gviews.adminlogin,name='adminlogin'),
    path('usernvbar/',uviews.usernvbar,name="usernvbar"),
    path('viewGymUserDetails/',gviews.viewGymUserDetails,name="viewGymUserDetails"),
    path('addgym/',gviews.addgym,name="addgym"),
    path('checkregistergym/',gviews.checkregistergym,name="checkregistergym"),
    path('checkadmin/',gviews.checkadmin,name='checkadmin'),
    path('adminnavbar/',gviews.adminnvbar,name="adminnavbar"),
    path('showgym/',uviews.showgym,name="showgym"),
    path('addtrainer/',gviews.addtrainer,name="addtrainer"),
    path('savetrainerdetailes/',gviews.savetrainerdetailes,name="savetrainerdetailes"),
    path('showtrainer/',uviews.showtrainer,name="showtrainer"),
    path('anyquery/',uviews.anyquery,name="anyquery"),
    path('savequery/',uviews.savequery,name="savequery"),
    path('showquery/',gviews.showquery,name="showquery"),
    path('showpassword/',uviews.showpassword,name="showpassword"),
    path('showtraineradmin/',gviews.showtraineradmin,name="showtraineradmin"),
    path('deletetraineradmin/',gviews.deletetraineradmin,name="deletetraineradmin"),
    path('userequest/',uviews.userrequest,name="userrequest"),
    path('requeststatus/',uviews.requeststatus,name="requeststatus"),
    path('userrequestgym/',gviews.userrequestgym,name="userrequestgym"),
    path('accept/',gviews.accept,name="accept"),
    path('reject/',gviews.reject,name="reject"),
    path('requestdeleteobj/',gviews.requestdeleteobj,name="requestdeleteobj"),
    path('deletequery/',gviews.deletequery,name="deletequery"),
    path('showgymadmin/',gviews.showgymadmin,name="showgymadmin"),
    path('deletegymdetailsadmin/',gviews.deletegymdetailsadmin,name="deletegymdetailsadmin"),
    path('updatetrainerdetailes/',gviews.updatetrainerdetailes,name="updatetrainerdetailes"),
    path('updatetrainer/',gviews.updatetrainer,name="updatetrainer"),
    path('updatefinaltrainer/',gviews.updatefinaltrainer,name="updatefinaltrainer"),
    path('updategym/',gviews.updategym,name="updategym"),
    path('updategymm/',gviews.updategymm,name="updategymm"),
    path('updatefinalgym/',gviews.updatefinalgym,name="updatefinalgym")
]
