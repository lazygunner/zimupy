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

    def info(self,
             resource_id,
             prevue=None,
             share=None):
        """
        影视资源详情
        :param resource_id: 资源ID
        :param prevue: 是否获取播放档期(只有电视剧才有效) 1-获取
        :param share: 是否获取分享信息 1-获取
        :return:
        """
        url = 'resource/getinfo'
        params = {'id': resource_id}
        if prevue:
            params.update({'prevue': prevue})
        if share:
            params.update({'share': share})

        ret = self._get(
            url,
            params=params
        )

        return ret

    def season_info(self, resource_id):
        """
        影视资源季度信息
        :param resource_id: 资源ID
        :return:
        [
            {u'episode': u'17', u'season': u'1'},
            {u'episode': u'23', u'season': u'2'},
            {u'episode': u'23', u'season': u'3'},
            {u'episode': u'24', u'season': u'4'},
            {u'episode': u'24', u'season': u'5'},
            {u'episode': u'24', u'season': u'6'},
            {u'episode': u'24', u'season': u'7'},
            {u'episode': u'24', u'season': u'8'},
            {u'episode': u'24', u'season': u'9'},
            {u'episode': u'10', u'season': u'10'},
            {u'episode': u'3', u'season': u'103'}
        ]
        """
        url = 'resource/season_episode'
        params = {'id': resource_id}

        ret = self._get(
            url,
            params=params
        )

        return ret

    def item_list(self,
                  resource_id,
                  client,
                  uid,
                  token,
                  need_link=1,
                  click=1):
        """
        影视下载资源列表
        :param resource_id: 资源ID
        :param client: 客户端类型: 1-IOS, 2-安卓, 3-WP
        :param uid: 用户UID
        :param token: 用户token
        :param need_link: 是否同时获取下载链接 1-获取,0-不获取
        :param click: 部分app客户端默认只输出固定的中文字幕,\
                      更多的需要再次点击获得,click为1则表示获取更多的数据
        :return:
        """

        url = 'resource/itemlist'
        params = {
            'id': resource_id,
            'client': client,
            'uid': uid,
            'token': token
        }

        if need_link:
            params.update({'file': need_link})
        if click:
            params.update({'click': click})

        ret = self._get(
            url,
            params=params
        )

        return ret

    def item_list_web(self,
                      resource_id,
                      season,
                      episode,
                      need_link=1):
        """
        影视下载资源列表-不验证用户权限
        :param resource_id: 资源ID
        :param season: 季度
        :param episode: 集数
        :param need_link: 是否同时获取下载链接 1-获取,0-不获取
        :return:
        [
            {
                u'episode': u'1',
                u'format': u'1080P',
                u'id': u'201118',
                u'link': [
                    {
                        u'address': u'ed2k://|file|The.Big.Bang.Theory.S01E01.\
                        Pilot.1080p.WEB-DL.AAC2.0.H.264-SA89.mkv|922437684|\
                        30D4B09A8CA938195E75BC4A4CA584A8|\
                        h=VOAHWVN4PSZ5JA5YMMNLHBK7HRXECLXR|/',
                        u'way': u'1'
                    }
                ],
                u'name': u'The.Big.Bang.Theory.S01E01.Pilot.1080p.WEB-DL.AAC2.0.H.264-SA89.mkv',
                u'season': u'1',
                u'size': u'879.71MB'
            },
            {
                u'episode': u'1',
                u'format': u'720P',
                u'id': u'9441',
                u'link': [
                    {
                        u'address': u'ed2k://|file|The.Big.Bang.Theory.S01E01.\
                        Pilot.720p.WEB-DL.AAC2.0.H264-PhoenixRG.mkv|\
                        713270287|B084CB735DE3EDFBC18B127B622BE9A1|\
                        h=7B4YZLAKFDRM5PN5QLLZHIRL7G6TKMPR|/',
                        u'way': u'1'
                    }
                ],
                u'name': u'The.Big.Bang.Theory.S01E01.Pilot.720p.WEB-DL.AAC2.0.H264-PhoenixRG.mkv',
                u'season': u'1',
                u'size': u'680.23MB'
            },
            {
                u'episode': u'1',
                u'format': u'BD-720P',
                u'id': u'224099',
                u'link': [
                    {
                        u'address': u'ed2k://|file|The.Big.Bang.Theory.\
                        S01E01.720p.BluRay.x264.DTS-WiKi.mkv|1674042352|\
                        2B7E7586E90E9241FE512E70FC8F86D5|\
                        h=YWPE2DA6S2S4EDT2MTHBCWWBK7Q3JQTW|/',
                        u'way': u'1'
                    }
                ],
                u'name': u'\u751f\u6d3b\u5927\u7206\u70b8.\
                    \u5185\u5c01\u4e2d\u82f1\u53cc\u8bed\u7279\u6548\u5b57\u5e55.\
                    The.Big.Bang.Theory.S01E01.720p.BluRay.x264.DTS-WiKi.mkv',
                u'season': u'1',
                u'size': u'1.56GB'
            },
            {
                u'episode': u'1',
                u'format': u'DVD',
                u'id': u'9726',
                u'link': [
                    {
                        u'address': u'ed2k://|file|big_bang_theory.1x01.pilot.\
                            dvdrip_xvid-fov.avi|183793664|CCA06BAB966FA0AAA7DF1BAA353D84FA|\
                            h=IXBTSJOAAATJHKSXR3WBRJNVQURF3H4Z|/',
                        u'way': u'1'
                    }
                ],
                u'name': u'big_bang_theory.1x01.pilot.dvdrip_xvid-fov.avi',
                u'season': u'1',
                u'size': u'175.28MB'
            },
        ]
        """

        url = 'resource/itemlist_web'
        params = {
            'id': resource_id,
            'season': season,
            'episode': episode,
            'file': need_link,
        }

        ret = self._get(
            url,
            params=params
        )

        return ret

    def item_link(self, item_id):
        """
        获取影视资源下载地址
        :param item_id: 单个资源ID
        :return:
        [
            {
                u'address': u'ed2k://|file|flhd-supernaturals06e04-720p.mkv|\
                2336369843|6DFF105567BDB21E3400A9C81DEDBBC9|\
                h=M7BAAQPGTMGKRBX6FC2KHWHIVE6PM36A|/',
                u'way': u'1'
            }
        ]
        """

        url = 'resource/itemlink'
        params = {
            'id': item_id,
        }

        ret = self._get(
            url,
            params=params
        )

        return ret
