from libs_web_scraping import request_url
from libs_web_scraping import search_iphone_url
from libs_web_scraping import generate_sheet_output


PATH_OUTPUT_SHEET = r"C:\Users\rafae\OneDrive\Documentos\codingBob\newVersionTestBPA\output\saida.xlsx"


if __name__ == "__main__":
    retorno_body_request = request_url()
    retorno_descricoes, retorno_valores = search_iphone_url(body_response=retorno_body_request)
    generate_sheet_output(descricoes=retorno_descricoes, valores=retorno_valores, path_output=PATH_OUTPUT_SHEET)