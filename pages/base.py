from playwright.sync_api import Page, TimeoutError, Response, expect
from data.environment import host


class Base:
    def __init__(self, page: Page):
        self.page = page

    def open(self, uri) -> Response | None:
        return self.page.goto(f"{host.get_base_url()}{uri}", wait_until='domcontentloaded')

    def click(self, locator: str) -> None:
        self.page.click(locator)

    def input(self, locator: str, data: str) -> None:
        self.page.locator(locator).fill(data)

    def get_text(self, locator: str, index: int) -> str:
        return self.page.locator(locator).nth(index).text_content()

    def click_element_by_index(self, locator: str, index: int) -> None:
        self.page.locator(locator).nth(index).click()

    def input_value_by_index(self, locator: str, index: int, data: str) -> None:
        self.page.locator(locator).nth(index).fill(data)

    def wait_for_element(self, locator, timeout=12000) -> None:
        self.page.wait_for_selector(locator, timeout=timeout)

    def wait_for_all_elements(self, locator, timeout=5000):
        elements = self.page.query_selector_all(locator)

        for element in elements:
            self.page.wait_for_selector(locator, timeout=timeout)

        return elements

    def current_url(self) -> str:
        return self.page.url

    def checkbox_by_index(self, locator: str, index: int):
        elements = self.page.query_selector_all(locator)
        if 0 <= index < len(elements):
            elements[index].check()
        else:
            print(f"Element with index {index} not found.")

    def click_first_element(self, locator: str):
        self.page.locator(locator).first.click()

    def click_by_text(self, text: str):
        self.page.get_by_text(text).click()

    def input_in_shadow_root(self, shadow_locator: str, shadow_input_locator: str, data: str):
        shadow_root = self.page.evaluate_handle(f'document.querySelector("{shadow_locator}").shadowRoot')
        input_element = shadow_root.evaluate_handle(f'document.querySelector("{shadow_input_locator}")')
        input_element.as_element().fill(data)

    def checkbox(self, locator: str) -> None:
        self.page.locator(locator).check()

    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, timeout=10000)
        except TimeoutError:
            return False
        return True

    def is_element_NOT_presence(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, timeout=5000)
        except TimeoutError:
            return True
        return False

    def selector(self, locator: str, value: str):
        self.page.select_option(locator, value)

    def drag_and_drop(self, source, target):
        self.page.drag_and_drop(source, target)

    def alert_accept(self, locator: str):
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.click(locator)

    def open_new_tab_and_check_presence(self, locclick,
                                        locpresence):
        with self.page.expect_popup() as page1_info:
            self.page.click(locclick)
        page1 = page1_info.value
        page1.bring_to_front()
        loc = page1.locator(locpresence)
        expect(loc).to_be_visible(visible=True, timeout=12000)

    def close_tab(self, number):
        all_tabs = self.page.context.pages
        all_tabs[number].close()

    def switch_to_previous_tab(self,
                               number):
        all_tabs = self.page.context.pages
        new_tab = all_tabs[number]
        self.page.bring_to_front()
        self.page.wait_for_load_state()
        return new_tab

    def close_all_tabs_except_first(self):
        all_tabs = self.page.context.pages
        for p in range(1, len(all_tabs)):
            all_tabs[p].close()

    def refresh(self) -> Response | None:
        return self.page.reload(wait_until='domcontentloaded')

    def alert_with_double_input(self, key1, value1, key2, value2):
        dialog = self.page.wait_for_event('dialog')
        inputs = {key1: value1, key2: value2}
        dialog.fill(inputs)
        dialog.accept()

    def switch_to_iframe_and_click(self, iframe_locator,
                                   locator_for_click):
        frame = self.page.frame_locator(iframe_locator)
        if frame is not None:
            frame.locator(locator_for_click).click()
        else:
            print("Iframe not found with the specified locator:", iframe_locator)

    def switch_to_iframe_and_input(self, iframe_locator, locator_for_input, data: str):
        frame = self.page.frame_locator(iframe_locator)
        if frame is not None:
            frame.locator(locator_for_input).fill(data)
        else:
            print("Iframe not found with the specified locator:", iframe_locator)

    def get_iframe_by_index(self, index):
        return self.page.main_frame.child_frames[index]

    def switch_to_main_frame(self):
        return self.page.main_frame
