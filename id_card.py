import os
import json
import random
import datetime


class IdCard:

    def __init__(self):
        self.__area = self.__getArea()
        self.sex = random.choice(['男', '女'])
        self.name = self.__getName()
        self.birthday = self.__getBirthday()
        self.ethnic = self.__getEthnic()
        self.address = self.__getAddress()
        self.idNum = self.__getIdNum()
        self.visaOffice = self.__getVisaOffice()
        self.validPeriod = self.__getValidPeriod()

    def __getName(self):
        # 删减部分，比较大众化姓氏
        firstName = (
            "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平"
            "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉"
            "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
        )
        # 百家姓中双姓氏
        firstName2 = "万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
        # 女孩名字
        girl = "秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽"
        # 男孩名字
        boy = "伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘"
        # 名
        name = "中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝"
        # 10%的机遇生成双数姓氏
        if random.choice(range(100)) > 10:
            first_name = firstName[random.choice(range(len(firstName)))]
        else:
            i = random.choice(range(len(firstName2)))
            first_name = firstName2[i: i + 2]

        name_1 = ""
        # 生成并返回一个名字
        if '女' in self.sex:
            girl_name = girl[random.choice(range(len(girl)))]
            if random.choice(range(2)) > 0:
                name_1 = name[random.choice(range(len(name)))]
            return first_name + name_1 + girl_name
        else:
            boy_name = boy[random.choice(range(len(boy)))]
            if random.choice(range(2)) > 0:
                name_1 = name[random.choice(range(len(name)))]
            return first_name + name_1 + boy_name

    def __getBirthday(self):
        # 随机生成年月日
        year = random.randint(1960, 2000)
        month = random.randint(1, 12)
        # 判断每个月有多少天随机生成日
        if year % 4 == 0:
            if month in (1, 3, 5, 7, 8, 10, 12):
                day = random.randint(1, 31)
            elif month in (4, 6, 9, 11):
                day = random.randint(1, 30)
            else:
                day = random.randint(1, 29)
        else:
            if month in (1, 3, 5, 7, 8, 10, 12):
                day = random.randint(1, 31)
            elif month in (4, 6, 9, 11):
                day = random.randint(1, 30)
            else:
                day = random.randint(1, 28)
        # 小于10的月份前面加0
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        return [year, month, day]

    def __getEthnic(self):
        ethnics = (
            '蒙古', '回', '藏', '苗', '维吾尔', '彝', '壮', '布依', '白', '朝鲜', '侗', '哈尼', '哈萨克', '满', '土家', '瑶', '达斡尔', '东乡', '高山',
            '景颇',
            '柯尔克孜', '拉祜', '纳西', '畲', '傣', '黎', '傈僳', '仫佬', '羌', '水', '土', '佤', '阿昌', '布朗', '毛南', '普米', '撒拉', '塔吉克',
            '锡伯', '仡佬',
            '保安', '德昂', '俄罗斯', '鄂温克', '京', '怒', '乌孜别克', '裕固', '独龙', '鄂伦春', '赫哲', '基诺', '珞巴', '门巴', '塔塔尔', '汉')
        return ethnics[random.randint(0, len(ethnics) - 1)]

    def __getAddress(self):
        area = self.__area
        address = str(area['province'])
        city = area['city']
        county = area['county']
        town = area['town']
        if '市' not in county:
            address = address + city
        return address + county + town + str(random.randint(0, 9999)) + '号'

    def __getIdNum(self):
        area_code = self.__area['code']
        birthday = [str(i) for i in self.birthday]
        # 生成15、16位顺序号
        num = ''
        for i in range(2):
            num += str(random.randint(0, 9))

        if self.sex == '男':
            # 生成奇数
            seventeen_num = random.randrange(1, 9, 2)
        else:
            seventeen_num = random.randrange(2, 9, 2)
        eighteen_num = str(random.randint(1, 10))
        if eighteen_num == '10':
            eighteen_num = 'X'
        return str(area_code) + ''.join(birthday) + num + str(seventeen_num) + eighteen_num

    def __getVisaOffice(self):
        county = self.__area['county']
        return county + '公安局'

    def __getValidPeriod(self):
        begin = datetime.date.today()
        decade = datetime.timedelta(days=3652)
        end = begin + decade
        return begin.strftime("%Y.%m.%d") + '-' + end.strftime("%Y.%m.%d")

    def __getArea(self):
        """
        {'province': '山东省', 'city': '菏泽市', 'county': '菏泽高新技术开发区', 'code': '371772', 'town': '马岭岗镇'}
        """
        with open('resource/area.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)
            area = data[random.randint(0, len(data) - 1)]
        return area
