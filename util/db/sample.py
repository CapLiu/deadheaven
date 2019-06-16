from util.db.database import Base,create_all_table,addRecord,get,deleteRecord
from sqlalchemy import Column,Integer,String,TEXT
class sampleTable(Base): # 使用sqlalchemy建立表类，必须继承Base类
    __tablename__ = 'sampleTable' #表名
    id = Column(Integer,primary_key=True) #id为主键，数据类型为Integer
    name = Column(String(10)) #创建大小为10，类型为String的name列
    fullname = Column(String(10))

#class otherTable(Base): # 如法炮制建立其他表
#    pass

# 测试部分
create_all_table() #将基于Base的所有表在数据库中建立

def sample_add():
# 建立一个sampleTable的对象，并调用addRecord函数向表中插入数据
    sampledata1 = sampleTable(id=1,name='Sample',fullname='S.Example')
    result = addRecord(sampledata1)
    print(result)

def sample_get():
# 根据指定id查找,使用get(tableClass,<idvalue>)
    print('Name is %s,fullname is %s' % (get(sampleTable,1).name,get(sampleTable,1).fullname))

def sample_delete():
# 使用deleteRecord删除sampledata
    sampledata = get(sampleTable,1)
    deleteRecord(sampledata)

def sample_update():
# update数据
    sampledata = get(sampleTable,1)
    sampledata.name='Sample1'
    result = addRecord(sampledata)
    print(result)

