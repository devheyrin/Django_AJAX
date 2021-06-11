import csv

from config.settings import DATA_DIRS


class MyAnalysis:
    def wm(self, year, month):
        f = open(DATA_DIRS[0]+'\\ta.csv');
        # f = open('../data/age.csv')
        data = csv.reader(f);
        next(data);
        htemp = [];
        ltemp = [];
        for row in data:
            if year == int(row[0].split('-')[0]) and month == int(row[0].split('-')[1]):
                ltemp.append(float(row[3]));
                htemp.append(float(row[4]));
        data = [{
            'name':'일별 최저 기온',
            'data':ltemp
        },{
            'name':'일별 최저 기온',
            'data':htemp
        }];
        return data;

    def localage(self, target):
        f = open(DATA_DIRS[0]+'\\age.csv', encoding='UTF8');
        #f = open('../data/age.csv', encoding='UTF8')
        data = csv.reader(f);
        next(data);
        mcnt = [];
        fcnt = [];
        print(''+target)
        for row in data:
            if target in row[0]:
                for i in row[3:104]:
                    try:
                        mcnt.append(int(i));
                    except:
                        mcnt.append(int(i.replace(',','')));
        print();
        data = [{
            'name':'Total Age',
            'data':mcnt
        }];
        return data;

    def genderage(self, target):
        f = open(DATA_DIRS[0]+'\\age.csv', encoding='UTF8');
        #f = open('../data/age.csv', encoding='UTF8')
        data = csv.reader(f);
        next(data);
        m = [];
        f = [];

        for row in data:
            if target in row[0]:
                for i in row[106:207]:
                    m.append(-int(i.replace(',','')));
                for i in row[209:310]:
                    f.append(int(i.replace(',','')));
        data = [{
            'name':'Male Age',
            'data':m
        },{
            'name':'Female Age',
            'data':f
        }];
        return data;

    def genderage2(self, target):
        f = open(DATA_DIRS[0]+'\\age.csv', encoding='UTF8');
        data = csv.reader(f);
        next(data);
        m = 0;
        f = 0;

        for row in data:
            if target in row[0]:
                m = int(row[105].replace(',',''));
                f = int(row[208].replace(',',''));
                # for i in row[106:207]:
                #     m.append(-int(i.replace(',','')));
                # for i in row[209:310]:
                #     f.append(int(i.replace(',','')));
        data = [{
            'name':'Male Age',
            'y':(m/(m+f))*100

        },{
            'name':'Female Age',
            'y':(f/(m+f))*100
        }];
        return data;


    def traffics(self, station, line):
        f = open(DATA_DIRS[0]+'\\card.csv', encoding='UTF8');
        data = csv.reader(f);
        next(data);
        freeride = []; #무임승차
        freeoff = []; #무임하차
        paidride = []; #유임승차
        paidoff = []; #유임하차

        for row in data:
            #print(row);
            if station in row[3] and line in row[1]:
                paidride = int(row[4].replace(',',''));
                paidoff = int(row[5].replace(',',''));
                freeride = int(row[6].replace(',', ''));
                freeoff = int(row[7].replace(',', ''));
        data = [{
            'name':'유임승차',
            'y':paidride
        },{
            'name':'유임하차',
            'y':paidoff
        },{
            'name':'무임승차',
            'y':freeride
        },{
            'name':'무임하차',
            'y':freeoff
        }];
        return data;

    def subway(self):
        f = open(DATA_DIRS[0] + '\\card.csv', encoding='UTF8');
        data = csv.reader(f);
        next(data);
        rate = 0;
        mx = 0;
        # for row in data:
        #     for i in range(4, 8):
        #         row[i] = int(row[i].replace(',',''));
        #         print('------',i,'----------');
        #         print('row[i]',type(row[i]));
        #         print('row[6]',type(row[6]));
        #         print('row[5]',type(row[5]));
        #         print('row[4]',type(row[4]));
        #         if int(row[6].replace(',','')) != 0:
        #             rate = (row[4] / int(row[6].replace(',','')));
        #             if rate > mx:
        #                 mx = rate
        #                 print(row, round(rate, 2));
        for row in data:
            for i in range(4, 8):
                row[i] = int(row[i].replace(',',''));

            if row[6] != 0:
                rate = (row[4] / row[6]);
                if rate > mx:
                    mx = rate
                    print(row, round(rate, 2));


if __name__ == '__main__':
    result = MyAnalysis().subway();
    print(result);