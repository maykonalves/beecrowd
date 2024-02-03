x = input().split()
item, quantity = map(int, x)

prices = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

# verificar qual o valor de A para encontrar o valor de B

if item in prices:
    unity_price = prices[item]
    total = unity_price * quantity
    print(f"Total: R$ {total:.2f}")