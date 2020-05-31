from collections import deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        #拓扑排序，但是要求序列里最多只能有1，不然不存在
        #build
        # graph = {x:[] for x in org} 不能用这个初始化graph,因为seqs不仅仅有对应关系还包括所有的可能出现的数。org里面的数可能存在seqs不存在的数
        # in_degrees = {x:0 for x in org}

        graph, in_degrees, is_valid = self.build_graph(seqs)
        queue = deque([x for x in in_degrees if in_degrees[x] == 0])
        order = []

        while (queue):
            if (len(queue) > 1): return False
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return order == org

    def is_valid(self, number):
        return 1 <= number <= 10**4

    def build_graph(self, seqs):
        graph = {}
        #initialize empty graph
        for item in seqs:
            for i in item:
                graph[i]=[]

        in_degrees = {x:0 for x in graph}

        for item in seqs:
            for index in range(len(item)-1):
                if not (self.is_valid(item[index]) and self.is_valid(item[index+1])):
                    return {}, {}, False
                graph[item[index]].append(item[index+1])
                in_degrees[item[index+1]] += 1

        return graph, in_degrees, True


def main():
    s = Solution()
    print(s.sequenceReconstruction([111,291,702,70,561,469,707,897,165,927,796,323,362,3,568,793,603,930,644,721,590,827,421,579,364,193,552,853,972,924,353,913,544,586,397,115,640,716,202,281,67,673,933,952,880,177,107,799,883,271,724,166,751,44,392,203,50,106,911,319,388,390,142,409,487,741,718,34,558,703,26,782,711,966,83,435,543,709,256,288,934,572,614,20,963,45,699,132,874,449,239,265,923,600,158,556,750,939,790,909,537,620,181,655,340,493,396,492,639,840,93,49,62,507,191,68,485,688,591,852,697,545,75,800,562,722,481,613,420,310,302,783,879,497,188,51,369,809,245,624,766,458,685,770,402,495,949,237,733,996,860,810,267,533,211,162,157,823,704,79,86,136,632,357,398,746,277,771,415,973,23,30,920,869,251,763,321,554,196,383,521,698,347,753,218,336,122,946,279,273,665,464,947,433,898,209,71,705,666,779,902,10,61,969,431,818,739,466,830,981,526,27,462,280,843,479,404,46,360,328,394,877,989,84,161,199,104,594,77,607,503,292,216,957,863,668,652,478,223,765,452,215,708,465,512,48,348,758,149,582,931,896,760,858,313,293,36,508,59,354,616,92,887,331,474,678,135,316,959,950,857,96,371,14,757,728,314,308,240,259,878,57,922,938,318,498,803,118,69,999,52,108,918,349,541,748,90,867,985,190,334,517,597,876,647,247,153,174,439,904,16,514,587,657,848,542,905,300,516,780,304,140,454,538,21,990,776,261,286,382,738,249,667,610,204,412,789,389,928,643,230,761,370,595,39,740,416,851,994,91,102,948,436,297,283,662,829,41,715,892,19,854,195,352,670,611,200,81,301,812,325,681,189,744,345,995,850,519,692,861,781,87,1000,109,872,311,496,172,381,250,581,17,471,604,889,891,253,906,802,378,60,47,56,893,475,737,992,881,238,900,641,865,589,987,726,337,344,413,518,555,58,686,706,828,483,426,257,97,901,749,163,536,295,178,553,535,791,194,484,584,745,65,491,502,423,808,836,326,622,967,510,625,43,815,377,910,980,712,725,522,767,463,669,663,207,806,217,147,143,73,811,473,306,272,299,233,243,650,845,747,661,72,984,275,264,312,429,332,633,346,186,339,252,743,13,598,205,940,419,315,225,156,168,656,797,78,998,307,566,912,317,263,31,391,651,785,942,890,227,565,442,844,120,350,6,262,993,417,470,627,859,961,826,505,864,975,266,710,784,677,833,82,424,274,160,224,159,254,395,534,958,28,213,866,461,437,962,672,116,695,792,884,368,399,38,822,131,637,842,74,489,814,456,819,80,183,629,451,134,660,617,309,76,125,187,289,285,411,727,144,831,450,885,563,379,154,549,94,573,219,675,320,401,730,270,101,570,242,605,729,945,167,335,490,119,453,936,375,837,476,100,2,577,171,365,459,871,235,42,520,403,550,557,580,4,674,447,15,988,530,813,296,965,596,226,777,609,795,915,899,935,198,717,971,488,393,361,682,626,32,509,64,124,787,862,585,756,457,608,255,548,422,228,8,769,303,690,723,759,269,540,875,578,380,182,689,978,440,169,846,925,511,330,117,601,546,941,236,121,551,569,855,926,222,991,642,888,113,825,631,197,206,528,960,232,414,201,9,486,438,694,752,571,687,366,974,894,943,63,278,886,425,241,386,123,821,322,358,130,506,929,653,914,907,88,683,155,89,529,794,164,659,477,646,742,363,184,112,99,567,482,173,37,110,175,615,298,432,786,731,916,244,527,873,868,500,427,895,979,679,448,719,126,547,574,691,654,696,445,444,525,210,839,645,671,559,146,214,774,338,128,145,982,407,234,441,372,192,977,762,684,141,98,735,40,129,805,816,133,701,882,755,953,944,359,33,693,248,53,460,356,713,832,180,231,583,768,921,282,114,649,870,246,138,856,287,376,807,342,5,467,964,560,384,12,139,385,714,955,817,539,208,523,513,221,680,367,305,499,773,849,835,1,333,468,268,374,406,408,260,531,29,329,152,185,480,700,18,22,410,373,937,430,664,986,606,294,532,593,443,838,501,515,25,66,732,387,103,954,658,150,736,428,418,932,956,11,524,798,35,54,229,455,919,276,734,351,917,355,847,341,638,804,24,772,434,676,968,720,258,504,635,137,648,619,95,151,983,621,618,564,575,179,834,472,623,220,602,824,324,588,636,127,903,343,634,576,599,176,170,446,105,778,630,494,754,820,592,7,976,290,908,970,212,764,841,327,788,775,55,85,400,284,405,997,148,612,801,628,951],[[706,828,483,426,257,97,901,749,163,536,295,178,553,535,791,194,484,584,745,65,491,502,423,808,836,326,622,967,510,625,43,815,377,910,980,712,725,522,767,463,669,663,207,806,217,147,143,73,811,473,306,272,299,233,243,650,845,747,661,72,984,275,264,312,429,332,633,346,186,339,252,743,13,598,205,940,419,315,225,156,168,656,797,78,998,307,566,912,317,263,31,391,651,785,942,890,227,565,442,844,120,350,6,262,993,417,470,627,859,961,826,505,864,975,266,710,784,677,833,82,424,274,160,224,159,254,395,534,958,28,213,866,461,437,962,672,116,695,792,884,368,399,38,822,131,637,842,74,489,814,456,819,80,183,629,451,134,660,617,309,76,125,187,289,285,411,727,144,831,450,885,563,379,154,549,94,573,219,675,320,401,730,270,101,570,242,605,729,945,167,335,490,119,453,936,375,837,476,100,2,577,171,365,459,871,235,42,520,403,550,557,580,4,674,447,15,988,530,813,296,965,596,226,777,609,795,915,899,935,198,717,971,488,393,361,682,626,32,509,64,124,787,862,585,756,457,608,255,548,422,228,8,769,303,690,723,759,269,540,875,578,380,182,689,978,440,169,846,925,511,330,117,601,546,941,236,121,551,569,855,926,222,991,642,888,113,825,631,197,206,528,960,232,414,201,9,486,438,694,752,571,687,366,974,894,943,63,278,886,425,241,386,123,821,322,358,130,506,929,653,914,907,88,683,155,89,529,794,164,659,477,646,742,363,184,112,99,567,482,173,37,110,175,615,298,432,786,731,916,244,527,873,868,500,427,895,979,679,448,719,126,547,574,691,654,696,445,444,525,210,839,645,671,559,146,214,774,338,128,145,982,407,234,441,372,192,977,762,684,141,98,735,40,129,805,816,133,701,882,755,953,944,359,33,693,248,53,460,356,713,832,180,231,583,768,921,282,114,649,870,246,138,856,287,376,807,342,5,467,964,560,384,12,139,385,714,955,817,539,208,523,513,221,680,367,305,499,773,849,835,1,333,468,268,374,406,408,260,531,29,329,152,185,480,700,18,22,410,373,937,430,664,986,606,294,532,593,443,838,501,515,25,66,732,387,103,954,658,150,736,428,418,932,956,11,524,798,35,54,229,455,919,276,734,351,917,355,847,341,638,804,24,772,434,676,968,720,258,504,635,137,648,619,95,151,983,621,618,564,575,179,834,472,623,220,602,824,324,588,636,127,903,343,634,576,599,176,170,446,105,778,630,494,754,820,592,7,976,290,908,970,212,764,841,327,788,775,55,85,400,284,405,997,148,612,801,628,951],[686,706],[111,291,702,70,561,469,707,897,165,927,796,323,362,3,568,793,603,930,644,721,590,827,421,579,364,193,552,853,972,924,353,913,544,586,397,115,640,716,202,281,67,673,933,952,880,177,107,799,883,271,724,166,751,44,392,203,50,106,911,319,388,390,142,409,487,741,718,34,558,703,26,782,711,966,83,435,543,709,256,288,934,572,614,20,963,45,699,132,874,449,239,265,923,600,158,556,750,939,790,909,537,620,181,655,340,493,396,492,639,840,93,49,62,507,191,68,485,688,591,852,697,545,75,800,562,722,481,613,420,310,302,783,879,497,188,51,369,809,245,624,766,458,685,770,402,495,949,237,733,996,860,810,267,533,211,162,157,823,704,79,86,136,632,357,398,746,277,771,415,973,23,30,920,869,251,763,321,554,196,383,521,698,347,753,218,336,122,946,279,273,665,464,947,433,898,209,71,705,666,779,902,10,61,969,431,818,739,466,830,981,526,27,462,280,843,479,404,46,360,328,394,877,989,84,161,199,104,594,77,607,503,292,216,957,863,668,652,478,223,765,452,215,708,465,512,48,348,758,149,582,931,896,760,858,313,293,36,508,59,354,616,92,887,331,474,678,135,316,959,950,857,96,371,14,757,728,314,308,240,259,878,57,922,938,318,498,803,118,69,999,52,108,918,349,541,748,90,867,985,190,334,517,597,876,647,247,153,174,439,904,16,514,587,657,848,542,905,300,516,780,304,140,454,538,21,990,776,261,286,382,738,249,667,610,204,412,789,389,928,643,230,761,370,595,39,740,416,851,994,91,102,948,436,297,283,662,829,41,715,892,19,854,195,352,670,611,200,81,301,812,325,681,189,744,345,995,850,519,692,861,781,87,1000,109,872,311,496,172,381,250,581,17,471,604,889,891,253,906,802,378,60,47,56,893,475,737,992,881,238,900,641,865,589,987,726,337,344,413,518,555,58,686]]))

if __name__ == "__main__":
    main()
