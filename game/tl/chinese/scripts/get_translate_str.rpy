init -999 python in tl_str:
    def GetTranslation(basestr, dict):
        """
        从指定字典里寻找替换字符串(不区分大小写)
        """
        try:
            return adict[astr.lower()]
        except:
            return astr
    r_RANDOM_TOPIC_FREQUENCY_DESC_MAP = {
        "Never":"",
        "Rarely","",
        "Sometimes","",
        "Frequent","",
        "Often",""
    }
