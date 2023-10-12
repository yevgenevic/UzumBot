import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def google_sheets_ostatki(csv_url: str):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('botproject-400713-67dc83c63c0d.json', scope)
    gc = gspread.authorize(credentials)

    sheet_key = '1H_Z_TBysCo5kMwaftrEZ26T65_1PxT51E1MZMzlRxm8'
    sheet = gc.open_by_key(sheet_key)

    worksheet = sheet.get_worksheet(5)

    worksheet.clear()

    df = pd.read_csv(csv_url, decimal=',')

    df = df.where(pd.notna(df), None)

    data = df.values.tolist()

    first_row_data = ["ID", "Наименование", "Штрихкод", "SKU", "ID товара", "К отправке", "В продаже", "Возврат",
                      "Брак", "Себест. (сумы)", "Стоимость продажи (сумы)", "Общий остаток",
                      "Общая сумма остатков (сумы)", "Себест. (сумма) (сумы)", "Стоимость продажи (сумма) (сумы)",
                      "Остаток на СДХ", "Остаток на фотостудии", "Остаток на СДХ (сумма) (сумы)", "Доступно к отправке",
                      "Статус"]

    worksheet.append_rows([first_row_data])

    worksheet.append_rows(data)

    return worksheet.url

# if __name__ == "__main__":
#     google_sheets_ostatki()
