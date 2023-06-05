translate chinese python:
    def GetTranslation(basestr, dict):
        """
        从指定字典里寻找替换字符串(不区分大小写)
        """
        try:
            return adict[astr.lower()]
        except:
            return astr
    r_RANDOM_TOPIC_FREQUENCY_DESC_MAP = {
        "never":"从不",
        "rarely":"很少",
        "sometimes":"偶尔",
        "frequent":"经常",
        "often":"频繁"
    }
