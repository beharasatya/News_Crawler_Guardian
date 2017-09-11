import unittest
from guardian.spiders import guardian_home
from scrapy.http import TextResponse, Request


class GuardianSpiderTest(unittest.TestCase):

    def setUp(self):
        url = 'https://www.theguardian.com/au'
        with open('sample.html', mode='rb') as f:
            file_content = f.read()
        self.spider = guardian_home.GuardianHomeSpider()
        self.dummy_response = TextResponse(url=url,
        request=Request(url),
        body=file_content,
        encoding='utf-8')

    def test_parse(self):
        parse_item = list(self.spider.parse_news(self.dummy_response))
        for item in parse_item:
            self.ass
            self.assertEqual(item['author'], 'Helen Davidson')
            self.assertEqual(item['title'], 'More states could help asylum seekers denied welfare by Coalition')
            self.assertEqual(item['article'],
                                   '''Australian state governments are not ruling out following Victoria’s lead in offering assistance to asylum seekers who have had their support cut off by the federal government.  Documents leaked in August revealed a federal government plan to cut income and accommodation support for a number of single asylum seekers in Australia by placing them on a bridging visa in an attempt to encourage them to return to Manus Island and Nauru. At least 63 have been since transferred to the “final departure bridging E visa” and had their $200-per-week welfare assistance cut from the 28 August. They were given three weeks to move from government assisted housing.  “If you cannot find work to support yourself in Australia you will need to return to a regional processing country or any country where you have a right of residence,” an information document said. In response the Daniel Andrews-led Labor government last week announced a $600,000 package to assist affected asylum seekers residing in Victoria. The package covered housing, basic food, medical, clothing and transport expenses, as well as funding for caseworkers, and was praised by refugee organisations. The federal government, which has defended its decision, refused to respond to Andrews’ announcement. Guardian Australia has since contacted the relevant state governments, and only New South Wales appeared to rule out providing the same assistance. “The determination of support payments to asylum seekers on bridging visas is a matter entirely for the commonwealth,” said a spokesperson for the NSW multicultural department, which already provides a range of services for NSW-based asylum seekers. The Queensland government also already provides state-funded assistance to asylum seekers, but said it would “continue to monitor the situation” and work with partner organisations. A spokesman for the WA premier, Mark McGowan, said their understanding was that most of the impact would be on families in Victoria and NSW. However, he added: “We need to assess the matter further and we’re currently looking to see what avenues are available.” The South Australian government also refused to rule out providing assistance if it was needed, however a spokesman for the minister for communities and social inclusion, Zoe Bettison, said they believed there were only two men currently affected by the cut and both had found assistance from community organisations and gained employment. While it appeared only single individuals were targeted initially, government fact sheets indicate the move is expected to affect about 400 people who are in Australia after being transferred from Manus Island or Nauru for medical treatment, of which 367 are being assisted by the Human Rights Law Centre. The majority of people are in Victoria, with large portions in New South Wales and Queensland. It’s not thought there are any members of the group in the ACT, Tasmania or the Northern Territory. In making last week’s announcement Andrews accused the federal government of forcing people on to the streets to “freeze, languish and starve”. “They deserve our respect and our compassion. And if our country can’t provide it, then our state will,” he said. The Human Rights Law Centre welcomed the Victorian government’s announcement and said the other states’ responses were promising. “When Peter Dutton threatened to rip these people from the community and deport them back to harm in February last year we saw churches, state premiers and the Australian community all take a stand and force him to back down,” said the centre’s director of legal advocacy, Daniel Webb. “We’re seeing a similar response again.” Webb said the Andrews government move would ensure asylum seekers would not be destitute in Victoria, but hundreds of others remained in “an incredibly precarious situation”. “They’ve been getting on with rebuilding their lives in the community – some for several years – but they’re now terrified that one day soon the immigration minister will force them to choose between destitution here or danger and abuse elsewhere,” he said. “Really, the sensible and compassionate thing to do is to let them stay and get on with rebuilding their lives in freedom and safety.”''')

if __name__ == '__main__':
    unittest.main()