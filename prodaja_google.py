import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def google_sheets_prodaja(csv_url: str):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('botproject-400713-67dc83c63c0d.json', scope)
    gc = gspread.authorize(credentials)

    sheet_key = '1H_Z_TBysCo5kMwaftrEZ26T65_1PxT51E1MZMzlRxm8'
    sheet = gc.open_by_key(sheet_key)

    worksheet = sheet.get_worksheet(4)

    worksheet.clear()

    df = pd.read_csv(csv_url, decimal=',')

    df = df.where(pd.notna(df), None)

    data = df.values.tolist()

    first_row_data = ["Статус", "Дата создания", "Дата получения", "№ заказа", "Штрихкод", "SKU", "Наименование",
                      "Категория", "Количество", "Возвраты", "Выручка (сумы)", "Выручка с вычетом комиссии (сумы)",
                      "Комиссия маркетплейса (сумы)", "Цена (сумы)", "Себестоимость (сумы)"]

    worksheet.append_rows([first_row_data])

    worksheet.append_rows(data)

    return worksheet.url
