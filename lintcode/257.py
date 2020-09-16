"""
257. Longest String Chain
https://www.lintcode.com/problem/longest-string-chain/description?_from=contest&&fromId=93

dp[i] longest string chian ending in i
dp[i] = max(dp[i], dp[j] + 1) if distance between words[j] and word[i] is 1 for j in range [0, i)

max(dp[i])

dp[i] = 1

longest increasing subsequence变形

"""
class Solution:
    """
    @param words: the list of word.
    @return: the length of the longest string chain.
    """
    def longestStrChain(self, words):
        if not words:
            return 0

        words = sorted(words, key=lambda x: len(x))
        n = len(words)
        dp = [1] * n

        for i in range(n):
            for j in range(i - 1, -1 ,-1):
                if len(words[j]) == len(words[i]):
                    continue
                if len(words[i]) - len(words[j]) > 1:
                    break
                if self.is_valid(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def is_valid(self, word1, word2):
        i = 0
        j = 0
        diffed_by_one = False
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                if diffed_by_one:
                    return False
                if j + 1 < len(word2) and word1[i] == word2[j + 1]:
                    j += 1
                else:
                    return False
                diffed_by_one = True

        return True


s = Solution()
words=["uiykgmcc","jrgbss","mhkqodcpy","lkj","bwqktun","s","nrctyzifwytjblwy","wrp","scqlcwmxw","irqvnxdcxoejuu","gmlckvofwyifmrw","wbzbyrcppaljigvo","lk","kfeouqyyrer","efzzpvi","ubkcitcmwxk","txihn","mdwdmbtx","vuzvcoaif","jwmboqvhpqodsj","wscfvrfl","pzye","waxyoxftvrgqmkg","wwdidopozinxxn","dclpg","xjsvlxktxs","ajj","pvsdastm","tatjxhygidhn","feafycxdxagn","irqvnxxoeuu","kwjo","tztoovsyfwz","prllrw","sclmx","bbmjnwaxcwaml","gl","wiax","uzvcoaif","ztovyfwz","qxy","zuexoxyp","qxyyrl","pvsdasvtm","femafycxdxaagn","rspvccjcm","wvyiax","vst","efzi","fjmdcc","icsinrbpql","ctybiizlcr","ntyzfwytjblw","tatjxhygidhpn","e","kykizdandafusu","pnepuwcsxl","kfeuqyyrer","afplzhbqguu","hvajtj","prll","ildzdimea","zueoxp","ezi","lqr","jkaagljikwamaqvf","mlzwhkxsn","rspvccbcjjtcm","wscfvrl","m","msygukwlkrqboc","pifojogoveub","bkcmwx","jercgybhss","wrpi","aicsinkgrbpqli","aplzbuu","sclcmxw","atpepgsz","govrcuuglaer","bdxjpsvlxkytxs","uikgm","bm","wvyhiqax","znvaasgfvqi","hatpepgsz","hrzebpa","bnfz","lybtqrfzw","taxhygihn","bjnfzk","mhqp","ide","znvcaasgfvqi","ftv","afplzhbqsguuu","thn","pdbccbe","mxevopfoimgjww","fjmdrcce","rspvccjjcm","jv","motnfwohwule","xjsvlxtxs","bqeb","eug","jftavwgl","rzebpa","lybtqrfazw","zuexoxp","jercgybhsys","hajtj","bkcitcmwxk","mbpvxsdastvtm","mowlznwhkxsn","dvenn","rsacxe","tatjxhygihn","cotybiizlcr","bbmnaxaml","pkwrpsi","nqpdbccbkxens","mbpbovxsdastvtm","mj","pxpsvikwekuq","qeug","dmelddga","aicsinkgrbpxqli","bdxjpsvlxktytxs","pkrllrxw","jkgljikwmaqf","iddie","ctybiizcr","nyzfwytjblw","yvuhmiuehspi","keuqre","wzbypaigvo","sck","uzcoaf","dlpg","ubkcpitlscmwxk","molzwhkxsn","pepuwcsxl","laplm","dclpgc","mahkxqodcpy","sclcmx","hvrzebpaz","bgovrcuuglaer","clazpulmw","yvuyhmiuehspiq","wzbycpaljigvo","sceqalciwmxw","hjytflmvsgv","u","hjyvxytfflhmvsgv","jkgjikwmaqf","fefycxdxagn","ftvw","ofncgxrkqvcr","spvcjc","pvsdastvtm","kykzdandaus","wbzbycppaljigvo","haytpepgsz","jmowlznwhkxsn","aplzhbguu","zvyz","nfvqi","jfvtavwsgl","xejnllhfulns","zhhvbiqiw","jkgljikwmaqvf","tyizc","irqvnxcxoejuu","clvazzpulmw","oncgxrqvcr","qlupvpdkhrm","mtnfwohwule","wwdidopzozinxxn","auiykgmcc","wscfvrfyl","pfksmrullrxw","jwmoqvhpqods","ftavwg","iddiea","kcmw","ykkwjwo","pe","aplzbguu","eu","bbmnaxal","ntyswtnlab","zhhhvbhbiqiw","jwmoqvpqods","kykzdndaus","bbmjnaxcwaml","zunvcaasgfvqi","icsingrbpql","sceqalciwmsxyw","yvuhmiuehsp","bxjsvlxktxs","waxoxftvrgqmkg","cogxxpaknks","scllvazzpulmw","tatjxhygeidhpn","ftvwg","tyz","nafvqi","oby","pgzpkhqog","irqvnxxoejuu","oxwpkxlakcp","bnf","oxwnpkxlakcp","bwqktu","ufybbaozoqk","ntydswtnlab","zvyfz","znaafvqi","npdbccbke","mhkqocpy","kuq","bjnfz","taxhyihn","kwrpsi","qifepmcatbdjlf","lzwhks","kfeuqre","mxevopfoimgww","spvcjcm","oncgxrkqvcr","jftavwsgl","soifcbya","jpzyeg","jwmboqvhpqods","lapulm","jrgbhss","xejfnllhfulns","zhhhvbbiqiw","km","kuqre","scxlzlvazzpulmw","ztvyfwz","wbzbycpaljigvo","rzbpa","vsastm","uybaooqk","dn","ykwjwo","ufybmvbaozoqk","nknm","mbpvsdastvtm","dpgzpxykhqog","wzbypajigvo","bnjnfzk","eollbigtftpdrd","zhbiqiw","yvuhiuehp","zhhhvbhbiqiwg","pfksrullrxw","pzyeg","aplzhbqguu","z","hvrzecbpazw","clvazpulmw","tajxhygihn","pgzpxykhqog","fefyxdxagn","wimomuvhn","lqrzw","xejnlhfulns","jhrc","xsxxs","slmx","jrgss","uikgmc","ncgqvcr","womuhn","aryouvtnmme","uzco","zhhhvbiqiw","hjytflhmvsgv","znvaasfvqi","kuqr","ojrpp","ztoovyfwz","zvz","pxpsviweuq","ufybaooqk","xy","jfvvtavwksvgl","raiachv","bmnaxl","rspvccjjtcm","pgzpxkhqog","xhbtfnqebaj","sceqalciwmsxw","jssctk","uzvcoaf","fefydxagn","jhrvc","mbj","raiahv","nrtyzifwytjblwy","mhqcp","jkgjkwmaqf","wscfvrfylhi","lqrz","ahabucermswyrvl","wxoxftvrgqmkg","ku","uyaoq","mhqocp","ykwjo","vstm","ofncgxrkqvcwr","dqvh","taxyihn","idie","bwqtu","tztoovyfwz","rspvcccjjtcm","uojrpp","wmomuhn","cotycbiizlxcr","nrtyzfwytjblw","ocbya","sceqlciwmxw","ajtj","rspvccbcjjthcm","kfeuqyyre","dmelddg","txyihn","ubkcitlscmwxk","ntyswtnla","bdxjpstvlxktytxs","odqdvbh","pxpsvikeewekuq","mdwdmbdtux","vs","bma","wzbypigvo","qxyy","vsstm","hbtnqeba","hrzebpaz","xhbtfnjsqebbaj","ahaucermswyrv","ddmbtx","zhhbiqiw","pxpsvikewekuq","odqdvgbh","bxjpsvlxktxs","jsck","fjmdc","mdwdmbdtx","jqxyyrl","pxpsvikweuq","ctybizcr","dqvbh","lpl","lqrfzw","ufybaozoqk","znvaafvqi","yvuhmiuehp","hvrzebpazw","pfksrllrxw","alzuu","xjsvxtxs","afplzhbqguuu","icsingrbpqli","hjxytflhmvsgv","femafycxdxagn","uyaoqk","gmlckvofwyifrw","cinrbpql","jrcgbhss","oxwpkxlkcp","jkagljikwamaqvf","eollbigtftpdrdy","rspvcjcm","socbya","clapulm","qeb","kwrpi","efzpi","hbtfnqebaj","kykizdnandafusu","sclvazzpulmw","efzzpvvi","jfvvtavwsvgl","mhqocpy","v","mbpbvxsdastvtm","irqvnxouu","hvaajtj","ofnlcgxrkqvcwr","hbtqeba","hbtqeb","jwmqpds","ntrnlhujdslco","zv","npdbccbken","mhp","ddb","prllw","mddmbtx","clazpulm","cogxxpaknkse","bkitcmwxk","oxwpklkcp","tyiz","jwmqvpqods","waxyoxftvrgqmkgb","afplzhbbqsgujuu","bwtu","jercgbhss","rsacx","mahkqodcpy","cotycbiizlcr","ahabucermswyrv","lupvpkhr","dvnn","b","atpepsz","ncgxqvcr","qe","ubkcitlcmwxk","lyqrfzw","wimomuhn","bbmnaxl","motnfwohrwule","yvuyhmiuehspi","jfvvtavwsgl","rac","fefdxagn","bwqkctun","uotjrpp","ddbtx","afplzhbbqsguuu","xss","xsxs","wvyiqax","kykizdandaus","npdbccbkens","r","oxwnpkxjlakcp","tzmteoovsyfwz","kykizdnandafuspu","ahabulcermswyrvl","xjsxxs","qxyyr","ck","xhbtfnqebbaj","nqpdbccbkens","mpvsdastvtm","zuexqoxyp","gmlkvofwyifrw","kmw","txhn","kykizdandausu","molznwhkxsn","lupvpdkhr","jwmqvpds","bktcmwx","wyiax","hzvaajtj","ddbx","pifojogveub","naafvqi","motnfwjohrwule","odqvbh","aicsingrbpqli","jopzyeg","lybtqrfazrw","pijogveub","xzejfnllhfulns","scxllvazzpulmw","irqyvnxdcxfoejuu","cogxpaknks","pdkwrpsi","wzbycpajigvo","xjsxtxs","irqvnxdcxfoejuu","xhbtfnjqebbaj","uybaoqk","oncgxqvcr","aj","pepuwsxl","lytqrfzw","nkm","jrgs","pkrllrw","wscfvrfyli","bbmjnaxcaml","jftavwg","vuzvcozaif","pifjogveub","cmogxxpaknkse","cinrbql","scqlciwmxw","ztvyfz","mxyevopfoimgjpww","soicbya","lupvpdkhrm","ahaucermsyrv","ufybmvbaouzoqk","bdxjpsvlxktxs","hjxytfflhmvsgv","hjvxytfflhmvsgv","nqpdbccbzkxens","wr","kykzdndus","iddimea","fjmdrcc","efzzpi","vsdastm","btqeb","pfkrllrxw","ocby","irqvnxxouu","ildzpdimea","lzwhkxsn","ilddimea","ufybvbaozoqk","mxyevopfoimgjww","jhr","kcmwx","dvn","uzcof","glw","hbtnqebaj","riahv","w","qeugv","kfeuqyre","ilrdzpdimea","lplm","icinrbpql","scqlcmxw","bbmjnaxaml","e","rsac","bf","jwmqvpqds","tzteoovsyfwz","rc","lzwhkxs","jkgljikwamaqvf","tybizc","aplzuu","nrtyzifwytjblw","pze","bktcmwxk","uiykgmc","jsctk","npdbccbe","tybizcr"]
print(s.longestStrChain(words))