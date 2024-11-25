# achmad_rizki_fauzi-web-scraping-assignment

Tujuan Web Scraping :
Mendapatkan data cuaca di kota Jakarta Pusat dalam bentuk json atau csv.

Langkah-langkah :
1. Lakukan Instalasi package scrapy. Direkomendasikan untuk menggunakan virtual environment (https://docs.scrapy.org/en/2.11/intro/install.html#using-a-virtual-environment-recommended)
2. Buatlah project scrapy dengan perintah **scrapy startproject _project_name_** (https://docs.scrapy.org/en/2.11/intro/tutorial.html#creating-a-project)
3. Buatlah kelas spider pada folder /project_name/_spiders_ (https://docs.scrapy.org/en/2.11/intro/tutorial.html#our-first-spider)
   ![image](https://github.com/user-attachments/assets/fba6e234-d45f-4be7-9627-07727abe6816)
4. Bukalah terminal dan masuk ke root folder project kemudian jalankan perintah **scrapy crawl _bmkg_jakpus_ -O cuaca.json** atau **scrapy crawl _bmkg_jakpus_ -O cuaca.csv**. Sesuailkan _bmkg_jakpus_ dengan nilai dari variabel nama kelas spider. (https://docs.scrapy.org/en/2.11/intro/tutorial.html#storing-the-scraped-data)
5. Setelah perintah (langkah 5) dijalankan maka akan muncul log seperti gambar di bawah :
   ![image](https://github.com/user-attachments/assets/e803c43b-093c-4768-8399-333f6ec059d4)
6. File output akan muncul pada root folder project.
   ![image](https://github.com/user-attachments/assets/ee4b479f-9c7a-4ede-8c4a-2baadc7f1169)




 
