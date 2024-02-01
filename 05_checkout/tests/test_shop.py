from lib.shop import Shop

def test_Shop_checkout_returns_minus1_when_skus_are_lowercase():
    shop = Shop()
    assert shop.checkout('aBc') == -1

def test_Shop_checkout_returns_minus1_when_skus_are_not_valid_characters():
    shop = Shop()
    assert shop.checkout('-B8x') == -1

def test_Shop_checkout_returns_minus1_when_skus_are_numbers():
    shop = Shop()
    assert shop.checkout('18') == -1

def test_Shop_checkout_returns_total_price_for_two_As():
    shop = Shop()
    assert shop.checkout('AA') == 100

def test_Shop_checkout_returns_total_price_for_ABCD():
    shop = Shop()
    assert shop.checkout('ABCD') == 115

def test_Shop_checkout_returns_total__discounted_price_for_AAA():
    shop = Shop()
    assert shop.checkout('AAA') == 130

def test_Shop_checkout_returns_total__discounted_price_for_AAAAAA():
    shop = Shop()
    assert shop.checkout('AAAAAA') == 260

def test_Shop_checkout_returns_total__discounted_price_for_AAAAAAA():
    shop = Shop()
    assert shop.checkout('AAAAAAA') == 310

def test_Shop_checkout_returns_total__discounted_price_for_AAABBCDAB():
    shop = Shop()
    assert shop.checkout('AAABBCDAB') == 290
