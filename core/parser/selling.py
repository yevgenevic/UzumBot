import sys
sys.path.append('/home/ubuntu/wisell_bot/UzumBot')

from playwright.sync_api import Playwright, sync_playwright
import time
import redis

from db import create_prodaja

redis_db = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


def run(playwright: Playwright) -> None:
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
    page.get_by_placeholder("Выберите магазин").click()
    page.locator("label").filter(has_text="Выбрать все").nth(1).click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("label").filter(has_text="1 месяц").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(60)
    page.locator("[data-test-id=\"button__close-modal\"] path").click()
    with page.expect_download() as download_info:
        with page.expect_popup() as page1_info:
            page.locator(".actions > .link-component").first.click()
        page1 = page1_info.value
    download = download_info.value.url
    create_prodaja("vse", download)
    page1.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.get_by_placeholder("Выберите магазин").click()
    page.get_by_title("Beauty4you").locator("label").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("label").filter(has_text="1 месяц").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(60)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download1_info:
        with page.expect_popup() as page2_info:
            page.locator(".actions > .link-component").first.click()
        page2 = page2_info.value
    download1 = download1_info.value.url
    create_prodaja("beauty4you", download1)
    page2.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.get_by_placeholder("Выберите магазин").click()
    page.locator("[data-test-id=\"multi-select-list__multi-select\"]").get_by_text("Lucky kids").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("label").filter(has_text="1 месяц").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(60)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download2_info:
        with page.expect_popup() as page3_info:
            page.locator(".actions > .link-component").first.click()
        page3 = page3_info.value
    download2 = download2_info.value.url
    create_prodaja("luckykids", download2)

    page3.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.get_by_placeholder("Выберите магазин").click()
    page.get_by_title("Top Price").locator("label").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("label").filter(has_text="1 месяц").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(60)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download3_info:
        with page.expect_popup() as page4_info:
            page.locator(".actions > .link-component").first.click()
        page4 = page4_info.value
    download3 = download3_info.value.url
    create_prodaja("topprice", download3)

    page4.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.get_by_placeholder("Выберите магазин").click()
    page.get_by_title("to.Be").locator("label").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("label").filter(has_text="1 месяц").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(60)
    page.locator("[data-test-id=\"button__close-modal\"] path").click()
    with page.expect_download() as download4_info:
        with page.expect_popup() as page5_info:
            page.locator(".actions > .link-component").first.click()
        page5 = page5_info.value
    download4 = download4_info.value.url
    create_prodaja("tobe", download4)

    page5.close()
    page.get_by_role("button", name="Формирование отчета").click()
    page.get_by_placeholder("Выберите магазин").click()
    page.locator("[data-test-id=\"multi-select-list__multi-select\"]").get_by_text("Smoke Cases").click()
    page.locator("[data-test-id=\"multi-select__multi-select\"]").get_by_role("img").click()
    page.locator("label").filter(has_text="CSV").click()
    page.locator("label").filter(has_text="1 месяц").click()
    page.locator("[data-test-id=\"form-report\"]").click()
    time.sleep(60)
    page.locator("[data-test-id=\"button__close-modal\"]").get_by_role("img").click()
    with page.expect_download() as download5_info:
        with page.expect_popup() as page6_info:
            page.locator(".actions > .link-component").first.click()
        page6 = page6_info.value
    download5 = download5_info.value.url
    create_prodaja("smokecases", download5)

    page6.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
