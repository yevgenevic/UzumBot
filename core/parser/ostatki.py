import sys
sys.path.append('/home/ubuntu/wisell_bot/UzumBot')

from playwright.sync_api import Playwright, sync_playwright
import redis
import time
from db import cursor, connection, create_ostatik

def run(playwright: Playwright) -> None:
    # redis_db.flushdb()
    browser = playwright.firefox.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://seller.uzum.uz/seller/signin")
    page.get_by_placeholder("example@mail.com").click()
    page.get_by_placeholder("example@mail.com").fill("+998900667171")
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("half65life90")
    page.locator("[data-test-id=\"button__next\"]").click()
    page.get_by_role("link", name="Отчеты Отчеты").click()
    page.get_by_role("button", name="Формирование отчета").click()
    page.locator("#suggest-11").get_by_role("img").click()
    page.locator("#suggest-11 div").filter(has_text="Продажи").nth(2).click()
    page.locator("#suggest-11").get_by_role("img").click()
    page.locator("#suggest-11 div").filter(has_text="Остатки").nth(2).click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="Выбрать все").nth(1).click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(80)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download_info:
        with page.expect_popup() as page1_info:
            page.locator(".actions > .link-component").first.click()
        page1 = page1_info.value
    download = download_info.value.url
    create_ostatik("vse", download)
    page1.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.locator("#suggest-31").get_by_role("img").click()
    page.locator("#suggest-31 div").filter(has_text="Остатки").nth(2).click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.get_by_title("Beauty4you").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(80)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download1_info:
        with page.expect_popup() as page2_info:
            page.locator(".actions > .link-component").first.click()
        page2 = page2_info.value
    download1 = download1_info.value.url
    create_ostatik("beauty4you", download1)
    page2.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.locator("#suggest-51").get_by_role("img").click()
    page.locator("#suggest-51 div").filter(has_text="Остатки").nth(2).click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.get_by_title("Lucky kids").locator("label").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(80)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download2_info:
        with page.expect_popup() as page3_info:
            page.locator(".actions > .link-component").first.click()
        page3 = page3_info.value
    download2 = download2_info.value.url
    create_ostatik("luckykids", download2)
    page3.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.locator("#suggest-71").get_by_role("img").click()
    page.locator("#suggest-71 div").filter(has_text="Остатки").nth(2).click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.get_by_title("Lucky kids").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(80)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download3_info:
        with page.expect_popup() as page4_info:
            page.locator(".actions > .link-component").first.click()
        page4 = page4_info.value
    download3 = download3_info.value.url
    page4.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.locator("#suggest-91").get_by_role("img").click()
    page.locator("#suggest-91 div").filter(has_text="Остатки").nth(2).click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.get_by_title("Top Price").locator("label").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(80)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download4_info:
        with page.expect_popup() as page5_info:
            page.locator(".actions > .link-component").first.click()
        page5 = page5_info.value
    download4 = download4_info.value.url
    create_ostatik("topprice", download4)
    page5.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.locator("#suggest-111").get_by_role("img").click()
    page.locator("#suggest-111 div").filter(has_text="Остатки").nth(2).click()
    page.get_by_placeholder("Выберите магазин").click()
    page.get_by_title("to.Be").locator("label").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(80)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download5_info:
        with page.expect_popup() as page6_info:
            page.locator(".actions > .link-component").first.click()
        page6 = page6_info.value
    download5 = download5_info.value.url
    create_ostatik("tobe", download5)
    page6.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.locator("#suggest-131").get_by_role("img").click()
    page.locator("#suggest-131 div").filter(has_text="Остатки").nth(2).click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.get_by_title("Smoke Cases").locator("label").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(80)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download6_info:
        with page.expect_popup() as page7_info:
            page.locator(".actions > .link-component").first.click()
        page7 = page7_info.value
    download6 = download6_info.value.url
    create_ostatik("smokecases", download6)
    print(download6)
    page7.close()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
