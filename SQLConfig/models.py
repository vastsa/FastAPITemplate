from sqlalchemy import Column, String, DateTime, func, Integer, Text

from SQLConfig.database import Base


class Algj_peerkeyword(Base):
    """
    同行关键词任务表
    """
    __tablename__ = 'algj_peerkeyword'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    account = Column(String(50))
    url = Column(String(250))
    yearsOfGoldSupplier = Column(Integer)
    productCount = Column(Integer)
    status = Column(Integer)
    modifyTime = Column(DateTime, default=func.now())
    createTime = Column(DateTime)
    remark = Column(String(250))
    filedMsg = Column(String(500))

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


class Algj_peerkeywordlog(Base):
    """
    同行关键词任务日志表
    """
    __tablename__ = 'algj_peerkeywordlog'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    account = Column(String(50))
    url = Column(String(250))
    yearsOfGoldSupplier = Column(Integer)
    productCount = Column(Integer)
    status = Column(Integer)
    modifyTime = Column(DateTime, default=func.now())
    createTime = Column(DateTime)
    remark = Column(String(250))
    filedMsg = Column(String(500))


class Algj_peerkeywordproductinfo(Base):
    """
    同行关键词抓取结果表
    """
    __tablename__ = 'algj_peerkeywordproductinfo'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    account = Column(String(50))
    url = Column(String(250))
    keyWord = Column(String(250))
    productName = Column(String(250))
    productId = Column(String(20))
    isShowcase = Column(Integer)
    modifyTime = Column(DateTime, default=func.now())
    createTime = Column(DateTime)
    remark = Column(String(250))


class Algj_keyword(Base):
    """
    关键词表
    """
    __tablename__ = 'algj_keyword'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    account = Column(String(50))
    keywordId = Column(Integer)
    keyword = Column(String(250))
    problemKey = Column(String(50))
    chinese = Column(String(250))
    showcaseCount = Column(Integer)
    goldSupplierCount = Column(Integer)
    searchHeat = Column(Integer)
    source = Column(Integer)
    isP4P = Column(Integer)
    isCorekeyword = Column(Integer)
    setKeywordType = Column(Integer)
    promotionRatingStar = Column(String(50))
    bestRanking = Column(String(50))
    modifyTime = Column(DateTime)
    createTime = Column(DateTime)
    remark = Column(String(250))


class Base_userTask(Base):
    """
    基本用户任务表
    """
    __tablename__ = 'base_usertask'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account = Column(String(50))
    taobaoUserId = Column(Integer)
    taskFrom = Column(Integer)
    taskType = Column(Integer)
    status = Column(Integer)
    created = Column(DateTime)
    modifytime = Column(DateTime)
    remark = Column(String(200))

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


class Base_userTaskLog(Base):
    """
    任务日志表
    """
    __tablename__ = 'base_usertasklog'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account = Column(String(50))
    taobaoUserId = Column(Integer)
    taskFrom = Column(Integer)
    taskType = Column(Integer)
    failedMsg = Column(Text)
    status = Column(Integer)
    created = Column(DateTime)
    newCount = Column(Integer)
    delCount = Column(Integer)
    modifytime = Column(DateTime)
    modifyCount = Column(Integer)
    remark = Column(Text)


class Algj_ProductKeywordRanking(Base):
    __tablename__ = 'algj_productkeywordranking'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    account = Column(String(50))
    keyword = Column(String(500))
    goodsId = Column(Integer)
    productId = Column(String(50))
    productName = Column(String(250))
    categoryId = Column(Integer)
    categoryName = Column(String(50))
    groupId = Column(Integer)
    groupName = Column(String(50))
    showcaseId = Column(Integer)
    productType = Column(String(50))
    mainImage = Column(Text)
    status = Column(String(20))
    rankingPage = Column(Integer)
    rankingOrder = Column(Integer)
    display = Column(String(20))
    ownerMember = Column(Integer)
    ownerMemberDisplayName = Column(String(20))
    pcDetailUrl = Column(String(250))
    modifyTime = Column(DateTime)
    createTime = Column(DateTime)
    remark = Column(String(250))


class Algj_Product(Base):
    __tablename__ = 'algj_product'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userId = Column(Integer)
    account = Column(String(50))
    goodsId = Column(Integer)
    productId = Column(String(50))
    productName = Column(String(250))
    categoryId = Column(Integer)
    categoryName = Column(String(50))
    groupId = Column(Integer)
    groupName = Column(String(50))
    showcaseId = Column(Integer)
    productType = Column(String(50))
    keywords = Column(String(500))
    mainImage = Column(Text)
    description = Column(Text)
    language = Column(String(50))
    status = Column(String(20))
    gmtModified = Column(String(20))
    display = Column(String(20))
    ownerMember = Column(Integer)
    ownerMemberDisplayName = Column(String(20))
    IsSpecific = Column(Integer)
    IsRts = Column(Integer)
    isSmartEdit = Column(Integer)
    pcDetailUrl = Column(String(255))
    created = Column(DateTime)
    isFoucusOn = Column(Integer)
    productLayered = Column(String(20))
    ranking = Column(String(50))
    schemaInfo = Column(Text)
    modifyTime = Column(DateTime)
    createTime = Column(DateTime)
    remark = Column(Text)
