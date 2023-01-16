import time
from pages.elements_page import TextBoxPage

class TestElement:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_name, input_email, input_curr_adrr, input_per_addr = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_adrr, output_per_addr = text_box_page.check_filled_form()
            assert input_name == output_name, f"{input_name} does not equal to {output_name}"
            assert input_email == output_email, f"{input_email} does not equal to {output_email}"
            assert input_curr_adrr == output_curr_adrr, f"{input_curr_adrr} does not equal to {input_curr_adrr}"
            assert input_per_addr == output_per_addr, f"{input_per_addr} does not equal to {input_per_addr}"

