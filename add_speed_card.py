# coding=UTF-8
import xlrd
import sys
import helian_common as helian_common

reload(sys)
sys.setdefaultencoding('utf-8')

con = helian_common.getMysqlConnect()
global cursor
cursor = con.cursor()
def addSpeedCard():
    print('start')
    url = 'addSpeed.xlsx'
    data = xlrd.open_workbook(url)
    table = data.sheets()[0]
    #行数
    nrows = table.nrows
    #列数
    ncols = table.ncols
    #从第二行开始读取，第一行是标题
    for rownum in range(1,nrows):
            row_data = table.row_values(rownum)
            phone = row_data[0]
            #加速卡类型
            category = row_data[1]
            # sql = ""
            if(category=='日卡'):
               sql = """ INSERT INTO score_store_my_goods(order_id,user_id,score_goods_id,score_goods_score,score_goods_price,score_goods_name,score_goods_img,score_goods_desc,
		is_used,pro_type,goods_score,tx,rx,total_time,create_time,modify_time,pay_type,is_old) VALUES(
		 '',(SELECT user_id FROM lianlian_box.app_reguser_info WHERE msisdn='"""+str(phone)[:11]+"""'),'25',0,3,'【加速卡】禾连Wi-Fi加速日卡','/homepage_category/2016/07/12/d4921a1a56c84c1685c950a1f9a8a535.png',
		 '客服电话：4001011130
使用范围:
加速卡仅在“禾连健康项目所及医院”网点使用具有提速效果
使用及有效期:
兑换/购买后即可享受加速权益24小时
',0,'01',0,500,500,24,NOW(),NOW(),2,0
		);"""
               cursor.execute(sql)
               con.commit()
            elif(category=='周卡'):
                sql = """ INSERT INTO score_store_my_goods(order_id,user_id,score_goods_id,score_goods_score,score_goods_price,score_goods_name,score_goods_img,score_goods_desc,
		is_used,pro_type,goods_score,tx,rx,total_time,create_time,modify_time,pay_type,is_old) VALUES(
		 '',(SELECT user_id FROM lianlian_box.app_reguser_info WHERE msisdn='"""+str(phone)[:11]+"""'),'30',0,18,'【加速卡】禾连Wi-Fi加速周卡','/homepage_category/2016/07/12/13d27a20b98247c5a5f27e93b7386eca.png',
		 '客服电话：4001011130

使用范围:
加速卡仅在“禾连健康项目所及医院”网点使用具有提速效果

使用及有效期:
兑换/购买后即可享受加速权益168小时
',0,'01',0,500,500,168,NOW(),NOW(),2,0
		);"""
                cursor.execute(sql)
                con.commit()
            print('success')
if __name__ == '__main__':
    addSpeedCard()