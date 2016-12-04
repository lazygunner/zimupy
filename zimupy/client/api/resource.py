# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from zimupy.client.api.base import BaseZiMuZuAPI


class Resource(BaseZiMuZuAPI):

    def list(self,
             channel=None,
             area=None,
             sort=None,
             year=None,
             category=None,
             limit=None,
             page=None):

        """
        影视资源列表
        :param channel: 频道 电影:movie,电视剧:tv,公开课:openclass
        :param area: 国家,例如:”美国”,”日本”,”英国”
        :param sort: 排序 更新时间update,发布时间pubdate,上映时间premiere,名称name,排名rank,评分score,点击率views
        :param year: 年代 最小值为1990
        :param category: 影视类型 具体值请参看网站
        :param limit: 默认为10个,不能大于20
        :param page: 列表页码
        :return: {
            'count': '11365',
            'list': [{
                'score': '8.0',
                'rank': '1735',
                'views': '67056',
                'id': '34838',
                'area': '英国',
                'play_status': '第1季连载中',
                'cnname': '神秘校园',
                'enname': 'Class',
                'category': '/剧情/魔幻/科幻/冒险/',
                'lang': '/英语/',
                'channel': 'tv',
                'remark': 'ZiMuZu原创翻译/字幕更新S01E08',
                'itemupdate': '1480861101',
                'format': '',
                'poster': 'http://tu.rrsub.com/ftp/2016/1020/38baa41860f38c3541f80f73c609f0e6.jpg',
                'poster_b': 'http://tu.rrsub.com/ftp/2016/1020/b_38baa41860f38c3541f80f73c609f0e6.jpg',
                'poster_a': 'http://tu.rrsub.com/ftp/2016/1020/a_38baa41860f38c3541f80f73c609f0e6.jpg',
                'poster_m': 'http://tu.rrsub.com/ftp/2016/1020/m_38baa41860f38c3541f80f73c609f0e6.jpg',
                'poster_s': 'http://tu.rrsub.com/ftp/2016/1020/s_38baa41860f38c3541f80f73c609f0e6.jpg',
            }]
        }
        """

        url = 'resource/fetchlist'
        params = {}
        if channel:
            params.update({'channel': channel})
        if area:
            params.update({'area': area})
        if sort:
            params.update({'sort': sort})
        if year:
            params.update({'year': year})
        if category:
            params.update({'category': category})
        if limit:
            params.update({'limit': limit})
        if page:
            params.update({'page': page})
        ret = self._get(
            url,
            params=params
        )

        return ret
