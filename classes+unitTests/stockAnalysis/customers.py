#class for registering and tracking a customer's portfolio.
class customer():
    number_of_customers = 0
    customers =[]

    def __init__(self, name):
        self.id = id
        self.name = name
        self.portolio = []
        customer.number_of_customers = customer.number_of_customers +1
        self.customer_register()
    
    def customer_register(self):
        self.id = customer.number_of_customers
        customer.customers.append((self.id, self.name))
    
    def customer_investment(self, stock, price, count):
        self.portolio.append((stock, price, count))

'calculate profit'
'taxes'
'rebalancing'
'risk profile'        





customer1 = customer("jens")
customer2 = customer("mary")
'buying stocks'
print('******************customer buys******************')
customer1.customer_investment("google", 20, 4)
print(customer1.name,customer1.portolio)
'our customers'
print('****************Customers********************')
for customer in customer.customers:
    print(customer)
'customer holdings'
print('**********************Customer value********************')
print(f'{customer1.name} has {customer1.portolio[0][1] * customer1.portolio[0][2]} dkk of {customer1.portolio[0][0]}')