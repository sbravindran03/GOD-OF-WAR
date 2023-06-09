from django.urls import path
from .Routes import NoCodeViews, BlogViews, common, AI_Functions
from WebpageBuilderDjango import settings
from django.conf.urls.static import static

# Initilizes........................

urlpatterns = []


def Make_Join(Componets):
    OutComponets = []
    for i in Componets:
        for j in i:
            OutComponets.append(j)
    return OutComponets


# Paths.............................

NoCodeMaker = [
    path('view_pages', NoCodeViews.index, name='home'),
    path('', common.home, name='home'),
    path('home', common.home, name='home'),
    path('automation', common.automation, name='automation'),
    path('blog', common.blog, name='blog'),
    path('compiler', common.compiler, name='compiler'),
    path('add', NoCodeViews.addPage, name="addpage"),
    path('edit/<id>', NoCodeViews.editPage, name="editpage"),
    path('page/create', NoCodeViews.savePage, name="create_page"),
    path('editPage/<id>', NoCodeViews.editPageContent, name="editPageContent"),
    path('preview/<id>', NoCodeViews.previewPage, name='previewPage')
]

BlogBuilder = [
    path('list_blog', BlogViews.list_blog),
    path('list_edit_blog', BlogViews.list_edit_blog),
    path('view_blog/<str:pk>', BlogViews.view_blog),
    path('edit_blog/<str:pk>', BlogViews.edit_blog),
    path('blog_edit', BlogViews.blog_edit),
    path('save_blog', BlogViews.save_blog),
    path('delete_blog', BlogViews.delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>', BlogViews.save_edit_blog),
]

AI_functions = [
    path('Code_scriping', AI_Functions.Code_scriping),
    path('Error_Solver', AI_Functions.Error_Solver),
]

# Add Paths Together..............

urlpatterns.extend(Make_Join([NoCodeMaker, BlogBuilder, AI_functions]))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
