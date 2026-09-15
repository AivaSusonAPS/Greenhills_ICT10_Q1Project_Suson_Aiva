from pyscript import document, display


def create_order(e):
    document.getElementById('output').innerHTML = ' '

    drink1 = document.getElementById("item1")
    drink2 = document.getElementById("item2")
    drink3 = document.getElementById("item3")
    drink4 = document.getElementById("item4")

    subtotal = float(drink1.value) * drink1.checked + float(drink2.value) * drink2.checked + float(drink3.value) * drink3.checked + float(drink4.value) * drink4.checked

    vat = subtotal * 0.12
    total = vat + subtotal

    display(f'Subtotal: {subtotal}', target='output')
    display(f'VAT: {vat}', target='output')
    display(f'Total AMount: {total}', target='output')
    
def getting_sku(e):

    categ_name = document.getElementById('categoryName').value
    prod_name = document.getElementById('productName').value
    stock_name = document.getElementById('stockName').value

    display(f'SKU: {categ_name}/{prod_name}/{stock_name}', target='result')

