# -*- coding: utf-8 -*-
import re
import json
import string

import re


def convert(name):
    return re.sub(r'([A-Z]*)([A-Z][a-z]+)', lambda x: (x.group(1) + '_' if x.group(1) else '') + x.group(2) + '_',
                  name).rstrip('_').lower()


def change_case(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)

    return ''.join(res)


if __name__ == '__main__':
    keys = ["MediaClassification", "Om_url", "Qualified_level", "Score_stretch", "Black_rate", "Copyright",
            "First_recommand", "Flag_ad", "Flag_minivideo", "Media_level_v2", "Pub_time", "Ws_info", "Minivideo_src",
            "Pic_minivideo", "Score_quality_id", "FrameLogo", "Have_coverQRCode", "Have_subtitle", "Is_normalized",
            "Is_qq_push", "Pic_scale", "U_cate2", "Hot_spot", "Pic_490_280", "U_cate1", "Cate1_embedding",
            "Content_level", "First_recommend_vid", "Media_id", "Qb_rec_level", "Targetid", "Cdn_info", "Ai_rec_status",
            "Media_icon", "Video_border_view", "Cmsid", "Duration", "Intercept_code", "Resolution",
            "Sec_recommand_name", "Have_water_mark", "Howto", "Is_stretch", "Is_subtitle_cut", "Minivideo_info",
            "Aspect", "Cate2_embedding", "Have_videoQRCode", "Minivideo_firstframe", "Pic_1280_720", "Utags",
            "Admin_qq", "Cover_border_view", "Eventid", "Pic_resolution", "TagInfos", "Title_scale", "Cmsid_state",
            "Feed_id", "UgcSource", "Content", "Expire_time", "First_recommand_name", "Media_name", "Score_classic_id",
            "UnionVid", "Vid", "Flag_newera", "Is_ori", "Premium", "Account_type", "Flag_neg_social", "Sec_recommand",
            "Video_source"]
    elems = []
    for key in keys:
        e = dict()
        e["name_qeh"] = key
        e["name_hbase"] = ["qeh_" + change_case(key)]
        e["type"] = "string"
        elems.append(e)
    print(json.dumps(elems))
