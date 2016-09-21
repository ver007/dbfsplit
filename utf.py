import codecs
f = codecs.open('config.txt','w','utf-8')
txt = '''<?xml version="1.0" encoding="utf-8"?>
    <!-- 支持的 CompType: COMP_EQUAL/COMP_NOTEQUAL/COMP_LESS/COMP_NOTLESS/COMP_GREAT/COMP_NOTGREAT, 即 = != < >= > <= -->
    <!-- 支持的 LinkType: AND/OR -->
    <!-- 日期通配符示例: 日期为2012年10月06日时, @Y@M@D = 20121006, @XM = A06; 日期为2012年3月10日时, @Y@M@D = 20120310, @XM = 310 -->
    <!-- 字段类型Type均填string, 程序内部所有类型转化为string后进行匹配 -->
    <!-- 同一<Filter>节点下的<Field>子节点以FieldID属性作为唯一主键 -->
    


  <!-- 中融-华林-光大-融华一号 需要的深交所数据
   深圳数据：Sjshb.dbf（回报库），Sjshq.dbf（行情库），Sjsgf.dbf（深交所股份库），Sjsdz.dbf（深交所对账库），LOFJS.dbf（LOF结算库）
       Sjsxx.dbf（深交所信息），Sjsfx.dbf（深交所发行），Sjsjg.dbf（深交所结果），Sjsmx1.dbf（深交所明细1），Sjsmx2.dbf（深交所明细2）。-->
  <sysconfig sysdate="20160818" copyresult="yes" okfile="yes" autorun="yes" loglevel="DEBUG"/>
  <DBFFile FileID="SJSHB_ZR" Description="深交所回报库">
      <Source      Description="源文件信息"      FileName="e:\onedrive\python\project\sjsfw.dbf"/>
      <Destination Description="中融信托"    SaveName="\\192.101.1.227\e$\huangming\@Y@M@D\@XM\sjsfw1.DBF"/>
      <Destination Description="中融信托"    SaveName="e:\onedrive\python\project\sjsfw2.dbf"/>
      <!-- <Destination Description="光大银行"    SaveName="\\192.101.1.227\e$\huangming\sjsfw4.DBF"/> -->
      <Filter Description="分拆条件">
          <Field FieldID="FWXWDM" FieldName="证券账户" FieldValue="000700" Type="string" CompType="COMP_EQUAL" LinkType="AND"/>
      </Filter>
  </DBFFile>
  <DBFFile FileID="SJSHQ_ZR" Description="深交所行情库">
      <Source      Description="源文件信息"      FileName="\\192.101.1.227\e$\huangming\sjsfw1.DBF"/>
      <Destination Description="中融信托"    SaveName="H:\onedrive\python\project\SJSHQ.DBF"/>
      <Destination Description="光大银行"    SaveName="H:\onedrive\python\project\SJSHQ2.DBF"/>
      <Filter Description="分拆条件">
          <!--Field FieldID="HQGDDM" FieldName="证券账户" FieldValue="0899044298" Type="string" CompType="COMP_EQUAL" LinkType="AND"/-->
      </Filter>
  </DBFFile>
 
</DBFSplitter>
'''
f.write(txt)
f.close()
