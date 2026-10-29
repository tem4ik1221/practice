def shop(*args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)
 
    discount = kwargs["discount"]
    delivery = kwargs["delivery"]

    apply_discount = lambda subtotal, discount: subtotal * (1 - discount / 100)
 
    subtotal = sum(args)
    after_discount = apply_discount(subtotal, discount)
    final_price = after_discount + delivery

    print("Цены:", *args)
    print(f"Сумма товаров: {subtotal} руб.")
    print(f"Скидка {discount}%: {subtotal - after_discount} руб.")
    print(f"Доставка: {delivery} руб.")
    print(f"ИТОГО: {final_price} руб.")
 
    return final_price

shop(120, 250, 80, discount=10, delivery=40)