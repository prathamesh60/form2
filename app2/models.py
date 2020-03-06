from django.db import models

class MainDept(models.Model):
    DEPT_NO = models.IntegerField(default=None,null=True, blank=True)
    DEPT_NAME = models.CharField(max_length=20,null=True, blank=True)
    SDEPT = models.CharField(max_length=10,null=True, blank=True)
    class Meta:
        db_table = "DEPARTMENT"

class SubDept(models.Model):
    SUBDEPT_NO = models.IntegerField(default=None,null=True, blank=True)
    SUBDEPT_NAME = models.CharField(max_length=20,null=True, blank=True)
    SUBDEPT = models.CharField(max_length=10,null=True, blank=True)
    DEPT_NO = models.IntegerField(default=None,null=True, blank=True)
    class Meta:
        db_table = "SUBDEPT"

class MainDesignation(models.Model):
    DESIG_NO = models.IntegerField(default=None,null=True, blank=True)
    DESIG_NAME = models.CharField(max_length=50,null=True, blank=True)
    SDESIG = models.CharField(max_length=10,null=True, blank=True)
    class Meta:
        db_table = "DESIGNATION"

class SubDesignation(models.Model):
    SUBDESIG_NO = models.IntegerField(default=None,null=True, blank=True)
    SUBDESIG_NAME = models.CharField(max_length=50,null=True, blank=True)
    SUBDESIG = models.CharField(max_length=8,null=True, blank=True)
    DESIG_NO = models.IntegerField(default=None,null=True, blank=True)
    class Meta:
        db_table = "SUBDESIG"

class Scale:
    SCALE_NO = models.IntegerField(default=None,null=True, blank=True
    B1 = models.IntegerField(default=None,null=True, blank=True)
    l1= models.IntegerField(default=None,null=True, blank=True)
    B2 = models.IntegerField(default=None,null=True, blank=True)
    l2 = models.IntegerField(default=None,null=True, blank=True)
    B3 = models.IntegerField(default=None,null=True, blank=True)
    l3 = models.IntegerField(default=None,null=True, blank=True)
    B4 = models.IntegerField(default=None,null=True, blank=True)
    l4 = models.IntegerField(default=None,null=True, blank=True)
    SCALE_NAME = models.CharField(max_length=100,,null=True, blank=True)
    l5 = models.IntegerField(default=None,null=True, blank=True)
    DETAIL = models.CharrField(max_length=200,null=True, blank=True)
    GRDPAY = models.IntegerField(default=None,null=True, blank=True)
    PAYBAND = models.CharField(max_length=60,null=True, blank=True)
    TA = models.IntegerField(default=None,null=True, blank=True)
    class Meta:
        db_table = "SCALE"

class Staff(models.Model):
    STAFF_NO = models.IntegerField(default=None,null=True, blank=True)
    STAFF_NAME = models.CharField(max_length=40,null=True, blank=True)
    class Meta:
        db_table = "STAFF"


class Caste(models.Model):
    CASTE_NO = models.IntegerField(default=None,null=True, blank=True)
    CASTE_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "CASTE"

class Category(models.Model):
    CATEGORY_NO = models.IntegerField(default=None,null=True, blank=True)
    CATEGORY_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "CATEGORY"
        
class Religion(models.Model):
    RELIGION_NO = models.IntegerField(default=None,null=True, blank=True)
    RELIGION_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "RELIGION"


class Appointment(models.Model):
    APPOINT_NO = models.IntegerField(default=None,null=True, blank=True)
    APPOINT_NAME = models.CharField(max_length=25,null=True, blank=True)
    l1 = models.IntegerField(default=None,null=True, blank=True)
    l2 = models.IntegerField(default=None,null=True, blank=True)
    l3 = models.IntegerField(default=None,null=True, blank=True)
    l4 = models.IntegerField(default=None,null=True, blank=True)
    l5 = models.IntegerField(default=None,null=True, blank=True)
    l6 = models.IntegerField(default=None,null=True, blank=True)
    l7 = models.IntegerField(default=None,null=True, blank=True)
    l8 = models.IntegerField(default=None,null=True, blank=True)
    l9 = models.IntegerField(default=None,null=True, blank=True)
    l10 = models.IntegerField(default=None,null=True, blank=True)
    l11 = models.IntegerField(default=None,null=True, blank=True)
    l12 = models.IntegerField(default=None,null=True, blank=True)
    l13 = models.IntegerField(default=None,null=True, blank=True)
    l14 = models.IntegerField(default=None,null=True, blank=True)
    l15 = models.IntegerField(default=None,null=True, blank=True)
    D1 = models.IntegerField(default=None,null=True, blank=True)
    D2 = models.IntegerField(default=None,null=True, blank=True)
    D3 = models.IntegerField(default=None,null=True, blank=True)
    D4 = models.IntegerField(default=None,null=True, blank=True)
    D5 = models.IntegerField(default=None,null=True, blank=True)
    D6 = models.IntegerField(default=None,null=True, blank=True)
    D7 = models.IntegerField(default=None,null=True, blank=True)
    D8 = models.IntegerField(default=None,null=True, blank=True)
    D9 = models.IntegerField(default=None,null=True, blank=True)
    D10 = models.IntegerField(default=None,null=True, blank=True)
    D11 = models.IntegerField(default=None,null=True, blank=True)
    D12 = models.IntegerField(default=None,null=True, blank=True)
    D13 = models.IntegerField(default=None,null=True, blank=True)
    D14 = models.IntegerField(default=None,null=True, blank=True)
    D15 = models.IntegerField(default=None,null=True, blank=True)
    D16 = models.IntegerField(default=None,null=True, blank=True)
    D17 = models.IntegerField(default=None,null=True, blank=True)
    D18 = models.IntegerField(default=None,null=True, blank=True)
    D19 = models.IntegerField(default=None,null=True, blank=True)
    D20 = models.IntegerField(default=None,null=True, blank=True)
    D21 = models.IntegerField(default=None,null=True, blank=True)
    D22 = models.IntegerField(default=None,null=True, blank=True)
    D23 = models.IntegerField(default=None,null=True, blank=True)
    D24 = models.IntegerField(default=None,null=True, blank=True)
    D25 = models.IntegerField(default=None,null=True, blank=True)
    D26 = models.IntegerField(default=None,null=True, blank=True)
    D27 = models.IntegerField(default=None,null=True, blank=True)
    D28 = models.IntegerField(default=None,null=True, blank=True)
    D29 = models.IntegerField(default=None,null=True, blank=True)
    D30 = models.IntegerField(default=None,null=True, blank=True)

    class Meta:
        db_table = "APPOINT"


class SuplHead(models.Model):
    SUPLNO = models.IntegerField(default=None,null=True, blank=True)
    SUPLHEAD_NAME = models.CharField(max_length=30,null=True, blank=True)
    class Meta:
        db_table = "SUPLHEAD"

class Bank:
    BNO = models.IntegerField(default=None,null=True, blank=True)
    BSNAME = models.CharField(max_length=10,null=True, blank=True)
    BNAME = models.CharField(max_length=50,null=True, blank=True)
    LOCATION = models.CharField(max_length=35,null=True, blank=True)
    BANKNO = models.IntegerField(default=None,null=True, blank=True)
    
    class Meta:
        db_table = "BANK"

class City:
    CITY_NO = models.IntegerField(default=None,null=True, blank=True)
    CITY_NAME = models.CharField(max_length=25,null=True, blank=True)
    class Meta:
        db_table = "CITY"

class Title(models.Model):
    TITLE_NO = models.IntegerField(default=None,null=True, blank=True)
    TITLE_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "TITLE"

class TypeTran(models.Model):
    TYPETRAN_NO = models.IntegerField(default=None,null=True, blank=True)
    TYPETRAN_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "TYPETRAN"

class NatureDesignation(models.Model):
    #CREATE NEW TABLE
    
class UnderCollege(models.Model):
    UNO = models.IntegerField(default=None,null=True, blank=True)
    UGPG_NAME = models.CharField(max_length=20,null=True, blank=True)
    LUGPG = models.CharField(max_length=50,null=True, blank=True)

    class Meta:
        db_table = "UGPG"


class Loan(models.Model):
    #CREATE NEW TABLE 
    
class StaffType(models.Model):
    STNO = models.IntegerField(default=None,null=True, blank=True)
    STAFF_TYPE = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "STAFFTYPE"

class InstallmentType(models.Model):
    INO = models.IntegerField(default=None,null=True, blank=True)
    IDNO = models.IntegerField(default=None,null=True, blank=True)
    PAYHEAD = models.CharField(max_length=3,null=True, blank=True)
    MONAMT = models.IntegerField(default=None,null=True, blank=True)
    INSTALNO = models.IntegerField(default=None,null=True, blank=True)
    TOTAMT = models.IntegerField(default=None,null=True, blank=True)
    REM = models.CharField(max_length=200,null=True, blank=True)
    STOP = models.IntegerField(default=None,null=True, blank=True)
    EXPDT = #Date
    PAIDNO = models.IntegerField(default=None,null=True, blank=True)
    MON = models.CharField(max_length=7,null=True, blank=True)
    NEW = models.IntegerField(default=None,null=True, blank=True)
    REF_NO = models.CharField(max_length=35,null=True, blank=True)
    DESP_NO = models.CharField(max_length=35,null=True, blank=True)
    DESP_DT = #Date
    START_DT = #Date
    DEFA_AMT = models.IntegerField(default=None,null=True, blank=True)
    PRO_AMT = models.IntegerField(default=None,null=True, blank=True)
    CODE = models.CharField(max_length=20,null=True, blank=True)
    IBNO = models.IntegerField(default=None,null=True, blank=True)
    MONYEAR = models.CharField(max_length=30,null=True, blank=True)
    STOP1 = models.IntegerField(default=None,null=True, blank=True)
    BAL_AMT = models.IntegerField(default=None,null=True, blank=True)
    REGULAR = models.IntegerField(default=None,null=True, blank=True)
    LTNO = models.IntegerField(default=None,null=True, blank=True)
    
    class Meta:
        db_table = "INSTALLMENT"
    
    # PER = models.IntegerField(default=None,null=True, blank=True)
    # FIXAMT = models.IntegerField(default=None,null=True, blank=True)
    # T_RANGE = models.IntegerField(default=None,null=True, blank=True)
    # F_RANGE = models.IntegerField(default=None,null=True, blank=True)
    # ITNO = models.IntegerField(default=None,null=True, blank=True)
    # LTNO = models.IntegerField(default=None,null=True, blank=True)
    # REGULAR = models.IntegerField(default=None,null=True, blank=True)
    # BAL_AMT = models.IntegerField(default=None,null=True, blank=True)
    # STOP1 = models.IntegerField(default=None,null=True, blank=True)
    # IBNO = models.IntegerField(default=None,null=True, blank=True)
    # PRO_AMT = models.IntegerField(default=None,null=True, blank=True)
    # PRO_AMT = models.IntegerField(default=None,null=True, blank=True)
    # DEFA_AMT = models.IntegerField(default=None,null=True, blank=True)
    # NEW = models.IntegerField(default=None,null=True, blank=True)
    # PAID_NO = models.IntegerField(default=None,null=True, blank=True)
    # STOP = models.IntegerField(default=None,null=True, blank=True)
    # NEW = models.IntegerField(default=None,null=True, blank=True)
    # TOTALAMT = models.IntegerField(default=None,null=True, blank=True)
    # INSTAL_NO = models.IntegerField(default=None,null=True, blank=True)
    # MONAMT = models.IntegerField(default=None,null=True, blank=True)
    
    # USER_PASS = models.CharField(max_length=3,null=True, blank=True)
    # USER_NAME = models.CharField(max_length=3,null=True, blank=True)
    # IPADDRESS = models.CharField(max_length=3,null=True, blank=True)
    # MONYEAR = models.CharField(max_length=3,null=True, blank=True)
    # CODE = models.CharField(max_length=3,null=True, blank=True)
    # DESP_NO = models.CharField(max_length=3,null=True, blank=True)
    
    # PAYHEAD = models.CharField(max_length=3,null=True, blank=True)
    
