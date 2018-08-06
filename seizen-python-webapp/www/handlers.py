#/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'songzhen'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
	users = await User.findAll()
	logging.info(' user: %s' % users)
	return {
		'__template__': 'test.html',
		'users': users
	}

@get('/blog')
async def blog(request):
	summary = 'Hello, this is a python web app demo.'
	blogs = [
		Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
		Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
		Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
	]
	return {
		'__template__': 'blogs.html',
		'blogs': blogs
	}
