from django.contrib import admin

from .models import User, Chat, Review, Opening, Watchlist, PartnerUniversity, Shortlist, Forum, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Review)
admin.site.register(Opening)
admin.site.register(Watchlist)
admin.site.register(PartnerUniversity)
admin.site.register(Shortlist)
admin.site.register(Forum)
admin.site.register(Comment)