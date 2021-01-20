import time
import win32com.client as win32

class Save_Excel():

    def __init__(self):
        self.xls_path       = 'C:/Python/Descargas_tes/test_results.xlsx'
        self.gen_img_path   = 'C:/Python/Descargas_test/Test_Rsafe/gscreen'
        self.location       = {'x': 465, 'y': 385}
        self.size_img       = {'height': 95, 'width': 180}

    def general_screenshot(self):
        driver.save_screenshot(self.gen_img_path)

    def cut_image(self):
        x = location['x']
        y = location['y']
        width = location['x'] + size['width']
        height = location['y'] + size['height']

        im = Image.open(self.gen_img_path)
        im = im.crop((int(x), int(y), int(width), int(height)))  # here we made the cut of the image
        im.save(self.gen_img_path)

    def save_image_xls(self,celda):
        wb_obj = openpyxl.load_workbook(path)
        sheet_obj = wb_obj.worksheets[0]
        img = openpyxl.drawing.image.Image(self.gen_img_path)

        cells = "D" + str(celda)
        img.anchor = cells
        sheet_obj.add_image(img)
        wb_obj.save(self.xls_path)
        time.sleep(3)

    def test_fails(self,test):
        Excl = win32.Dispatch("Excel.Application")
        Excl.Visible = True
        Excl.Workbooks.Open(self.xls_path)
        wb = Excl.ActiveWorkbook
        sheet_obj = wb.Worksheets('Hoja1')
        sheet_obj.Cells(4, test).Value = "The test fails"
        save_file(wb)
        time.sleep(3)