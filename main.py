from db_manager import DatabaseManager

def main():
    # 初始化資料庫管理器
    db_manager = DatabaseManager()

    # 建立資料庫連接
    db_manager.create_connection()

    # 創建資料表
    db_manager.create_table()

    # 插入五筆產品資料
    products = [
        (1, 'Smart Watch', 'Wearables', 199.99, 500, '2023-02-10', 'A smart watch with health monitoring features.'),
        (2, 'Smart Speaker', 'Home Devices', 99.99, 300, '2023-01-15', 'A smart speaker with voice control and music playback.'),
        (3, 'Smart Lightbulb', 'Home Devices', 19.99, 1000, '2022-12-05', 'A smart lightbulb that can be controlled via smartphone.'),
        (4, 'Smart Thermostat', 'Home Devices', 149.99, 150, '2023-03-22', 'A smart thermostat for temperature control.'),
        (5, 'Smart Glasses', 'Wearables', 299.99, 250, '2023-05-01', 'Smart glasses with AR features.')
    ]
    db_manager.insert_products(products)

    # 查詢所有產品
    db_manager.read_products()

    # 更新某個產品的價格和庫存
    db_manager.update_product('Smart Watch', 179.99, 450)

    # 刪除某個產品
    db_manager.delete_product('Smart Glasses')

    # 將查詢結果匯出成 CSV 檔案
    db_manager.export_to_csv('products_data.csv')

    # 關閉資料庫連接
    db_manager.close_connection()

if __name__ == "__main__":
    main()
