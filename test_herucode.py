from random import choice

from unittest import TestCase
from herucode import HeruLang


def make_random_verb():
    b = HeruLang.BAR_LETTERS
    x = HeruLang.ALPHABET
    li = [choice(x), choice(x), choice(x), choice(x), choice(x), choice(b)]

    return " ".join(li)


def make_random_subjunctive_verb():
    b = HeruLang.BAR_LETTERS
    x = HeruLang.ALPHABET
    li = [choice(b), choice(x), choice(x), choice(x), choice(x), choice(b)]

    return " ".join(li)


class TestHeruLangInner(TestCase):

    def setUp(self) -> None:
        self.HL = HeruLang

    def test_is_verb(self):
        self.assertTrue(self.HL.is_verb("iygsee"))

    def test_are_verbz(self):
        for i in range(100):
            self.assertTrue(self.HL.is_verb(make_random_verb()))

    def test_are_subjunctive_verbs(self):
        for i in range(100):
            self.assertTrue(self.HL.is_subjunctive_verb(make_random_subjunctive_verb()))

    def test_as_number(self):
        self.assertEqual(self.HL.as_number(word="gxjrc"), 605637)

    def test_is_pretty(self):
        self.assertTrue(self.HL.is_pretty(self.HL.as_number(word="gxjrc")))


class TestHeruLangBehaviour(TestCase):

    def test_analyze_1(self):
        test_string = """shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx
py en yco ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi
yrx qinexwo qx rqw wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn
cwj hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr
fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm ocxfsjdng sfoqmd
pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry
ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd
oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql
"""
        hl = HeruLang()
        result = hl.analyze(test_string)
        ### 'verbs': 36, 'pretty_numbers': 22, 'subjunctive_verbs': 25, 'prepositions': 3
        self.assertEqual(result["verbs"], 36)
        self.assertEqual(result["pretty_numbers"], 22)
        self.assertEqual(result["subjunctive_verbs"], 25)
        self.assertEqual(result["prepositions"], 3)

    def test_analyze_2(self):
        test_string = """dufqwh ndis eqclrnguo ceqrugs meod eofxlrd uqpwmni xrhm qgro hlwgimn fjnomcledi silruxh
efwh uxfrpsnqd fyejhi fxdn swfruc eopq hcgeox lhimoynsr rwjxecpmfl gimqxwuyr eujh rfs
qncuyiel hwuiqlne umyldn uwflpqc gywlc oxmegsdi sqemywlg cnfimrgows hnxyfd exmdnos
djpsogiy xyp myngercj yeujqcoih sgljco xy lruneodc frqog hqsgcy wmi hyfgqj iecusqjp
ugnmqfypsd yp rxoew lqeshijndg umynehjsci rnc xhrjyocde mnefpj rcyihwxq oihjwrup
gquscxhw ucrfdsoeq drg nqhodjsm snp cwoen ehyldsnmf pmrs cghuwpfxly ifwpnx wqdgrl
xocpjedsfm oegli url rylnsph ijucmxw jwispgefdo heixgmcy gm sdhfnoxg hc jqwpdo eo
hmypjfu xuedl nqpge cnyosu dniefl lf xcdupho wixmhcuynj poy ous jwroheqm xchm
jnufdshiqe liyrexhmu cjlxoiquef fwqrijemcd csxpy eqxghfry fhnwomgyuq yj euhxmosc
    """
        hl = HeruLang()
        result = hl.analyze(test_string)
        ### #
        #1) There are 3 prepositions in the text
        #2) There are 46 verbs in the text
        #3) There are 26 subjunctive verbs in the text
        ##

        self.assertEqual(result["verbs"], 46)
        self.assertEqual(result["pretty_numbers"], 21)
        self.assertEqual(result["subjunctive_verbs"], 26)
        self.assertEqual(result["prepositions"], 3)