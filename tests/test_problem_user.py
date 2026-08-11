import pytest
from pages.login_page import LoginPage


@pytest.mark.xfail(reason="Known bug: problem_user sees identical broken images for all products")
def test_problem_user_images(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("problem_user", "secret_sauce")
    
    image = page.locator("img.inventory_item_img").all()
    
    source = []
    for img in image:
        src = img.get_attribute("src")
        source.append(src)
        
    print(source)
    assert len(set(source)) > 1