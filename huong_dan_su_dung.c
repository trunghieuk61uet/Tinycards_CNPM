Tai lieu huong dan su dung

Sản phẩm được xây dựng trên framework Django, để chạy trang web trên local của ubuntu thì ta thực hiện các bước sau:
Mở Terminal gõ theo các bước sau:

	git clone https://github.com/trunghieuk61uet/Tinycards_CNPM.git

	cd Tinycards_CNPM

Tạo môi trường ảo của python :
	virtualenv blog_venv

	source blog_venv/bin/activate

Install các thư viện cần thiết:
	pip install Django==1.11.7
	pip install Pillow
	pip install social-auth-app-django

Tạo database (ở đây ta dùng database mặc định của django là sqlite3)
	cd mysite
	python manage.py makemigrations
	python manage.py migrate

Tạo tài khoản admin:
	python manage.py createsuperuser
	Nhập tên tài khoản, mật khẩu admin muốn tạo (giả sử tài khoản, mật khẩu đều là :admin)

Run server:
	python manage.py runserver



