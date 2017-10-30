from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

 	url(r'^$', 'mooc.accounts.views.dashboard', 
         name='dashboard'),

    url(r'^entrar/$', 'django.contrib.auth.views.login', 
        {'template_name': 'accounts/login.html'}, name='login'),

    url(r'^sair/$', 'django.contrib.auth.views.logout', 
        {'next_page': 'core:home'}, name='logout'),


	url(r'^cadastre-se/$', 'mooc.accounts.views.register', 
         name='register'),

	url(r'^editar/$', 'mooc.accounts.views.edit', 
         name='edit'),

	url(r'^editar-senha/$', 'mooc.accounts.views.edit_password', 
         name='edit_password'),
)
