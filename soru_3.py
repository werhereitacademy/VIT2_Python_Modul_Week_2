#Müşteri Yönetim Sistemi

#Proje Açıklaması: Bu proje, müşterilerinizi yönetmek ve temel işlemleri gerçekleştirmek için kullanabileceğiniz bir müşteri yönetim sistemi oluşturmanızı içerir. Bu sistem, müşteri bilgilerini saklama, yeni müşteri ekleyebilme, müşteri bilgilerini güncelleyebilme, müşteri silme ve müşteri listesini görüntüleme gibi temel işlevlere sahip olacaktır. İşte projenin temel adımları:'''


#1-Müşteri bilgilerini saklamak için bir sözlük yapısı kullanın. Her müşteri için bir benzersiz müşteri kimliği (ID) atayın ve müşteri bilgilerini bu kimlikle ilişkilendirin. Her müşteri için ad, soyad, e-posta, telefon gibi bilgileri içeren bir sözlük kullanabilirsiniz.

# 2-Kullanıcıya aşağıdaki işlemleri seçebileceği bir menü sunun:

# Yeni müşteri eklemek
# Müşteri bilgilerini güncellemek
# Müşteri silmek
# Tüm müşterileri listelemek
# Çıkış yapmak

# 3-Kullanıcının seçimine göre ilgili işlemi gerçekleştirin. Örneğin, yeni müşteri eklerken kullanıcıdan gerekli bilgileri alın ve sözlüğe yeni bir müşteri ekleyin.

# 4-Müşteri bilgilerini güncellerken, müşteri kimliğini kullanarak mevcut bilgileri görüntüleyin ve güncellenmiş bilgileri kaydedin.

# 5-Müşteri silme işleminde kullanıcıdan müşteri kimliğini alın ve bu müşteriyi sözlükten silin.

# 6-Tüm müşterileri listeleme işleminde, mevcut müşterilerin listesini görüntüleyin.

# 7-Kullanıcı çıkış yapana kadar işlemleri tekrarlayın.

# Müşteri bilgilerini saklamak için bir sözlük oluşturun (müşteri kimliği anahtar olarak kullanılır)



# Customer Management System

# Project Description: This project involves creating a customer management system that you can use to manage your customers and perform basic operations. This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers, and listing customers. Here are the basic steps of the project:

customer_info = {}
customer_id = 1

while True:
    print("\n1. Add a new customer\n2. Update customer information\n3. Delete a customer\n4. List all customers\n5. Exit")
    
    choice = input("Please select an operation (1-5): ")
    if choice == "1":
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Email: ")
        phone = input("Phone: ")
        
        customer_info[customer_id] = {
            'name': name,
            'surname': surname,
            'email': email,
            'phone': phone
        }
        customer_id += 1
        print(customer_info)
        
    elif choice == "2":
        print(customer_info)
        updated_customer_id = int(input("Customer ID to update: "))
        name = input("Name: ")
        surname = input("Surname: ")
        email = input("Email: ")
        phone = input("Phone: ")
        
        customer_info[updated_customer_id] = {
            'name': name,
            'surname': surname,
            'email': email,
            'phone': phone
        }
    
        print ("Customer information updated!")
        print (customer_info)
        
    elif choice =="3":
        print(customer_info)
        deleted_customer_id = int(input("Customer ID to delete: "))
        del customer_info[deleted_customer_id]
        print("Your operation has been successfully completed.")
        print(customer_info)
        
    elif choice == "4":
        print(customer_info)
        
    elif choice == "5":
        print("Exiting . . .")
        print("GOODBYE")
        break
        
    else:
        print("Invalid choice! Please make a selection between 1-5.")