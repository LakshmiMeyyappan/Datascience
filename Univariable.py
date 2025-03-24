class Univariate():

        def qualQuan(dataset):
            quan=[]
            qual=[]
            for columnName in dataset.columns:
        #print(columnName)
                if(dataset[columnName].dtypes=='O'):
                    #print("qual")
                    qual.append(columnName)
                else:
                    #print("quan")
                    quan.append(columnName)
            return qual,quan