#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Copyright (c) 2014 Feng Wang <wffrank1987@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

from crawler.core.base import *

from optparse import OptionParser

import time
import logging

logger = logging.getLogger('crawler.' + __name__)
logger.setLevel(logging.DEBUG)

def yelp_biz_ids(cate, loc, proxies=None):
    start = 0
    step = 10
    while True:
        url = "http://www.yelp.com/search?cflt=%s&start=%d&find_loc=%s" % (cate, start, loc)

        logger.info('fetching from %s' % url)

        html = get_response(url, proxies)

        soup = parse_soup(html)
        bussiness_divs = soup.findAll('div', {'class': "search-result natural-search-result biz-listing-large"})
        for div in bussiness_divs:
            bussiness_story = div.find('div', {'class': "media-story"})
            title_div = bussiness_story.find('h3', {"class": "search-result-title"}).find('a')
            url = 'http://www.yelp.com%s' % title_div['href']
            #title = title_div.text
            #print '%s -> %s' % (title, url)
            yield url
        start += step
        time.sleep(5)
