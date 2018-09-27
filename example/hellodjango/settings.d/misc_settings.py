# some sample
APPLICATION_SENTENCE="Hello Django"

# add apps into project read after settings.py
# append application into lists
#INSTALLED_APPS.append('my_application')
#MIDDLEWARE.append('my_application.middleware.MyApplucationMiddleware')

# add an application
INSTALLED_APPS.append("myapplication.apps.MyapplicationConfig")
