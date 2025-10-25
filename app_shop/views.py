from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from datetime import datetime
from app_shop.models import Category,Product,Contact

# Create your views here.

def trang_chu(request):
    danh_sach_danh_muc = Category.objects.all()
    return render(request,'index.html',{
        'danh_sach_danh_muc': danh_sach_danh_muc,
    })

def gioi_thieu(request):
    danh_sach_danh_muc = Category.objects.all()
    #return HttpResponse('<h1> Đây là Giới thiệu của CoffeeShop</h1>')
    return render(request, 'about.html',{
        'danh_sach_danh_muc': danh_sach_danh_muc,
    })

def lien_he(request):
    danh_sach_danh_muc = Category.objects.all()
    #return HttpResponse('<h1> Đây là Liên hệ CoffeeShop</h1>')

    #Thực hiện form
    form_lien_he = ContactForm()
    thong_bao = ''
    #Khi người dùng click nút Gửi thông tin
    if request.POST.get('name'):
        #Gán biến
        ho_ten = request.POST.get('name')
        email = request.POST.get('email')
        tieu_de = request.POST.get('subject')
        noi_dung = request.POST.get('message')
    
        #Lưu vào CSDL
        # cách 1
        # lh1 = Contact(name=ho_ten, email=email, subject=tieu_de, message=noi_dung)
        # lh1.save()

        #Cách 2
        Contact.objects.create(name=ho_ten, email=email, subject=tieu_de, message=noi_dung)

        #Gửi email cơ bản
        # nguoi_gui = settings.EMAIL_HOST_USER
        # ds_nguoi_nhan = [email]
        # send_mail(tieu_de, noi_dung, nguoi_gui, ds_nguoi_nhan, fail_silently=True)

        #Gửi mail với Django Template
        noi_dung_mail = render_to_string('contact_sendmail.html',{
            'ho_ten': ho_ten,
            'tieu_de': tieu_de,
            'noi_dung': noi_dung,
        })
        nguoi_gui = settings.EMAIL_HOST_USER
        ds_nguoi_nhan = [email]
        email = EmailMessage(tieu_de,noi_dung_mail,nguoi_gui,ds_nguoi_nhan)
        email.content_subtype='html'
        email.send()

        #Thông báo kết quả
        thong_bao='''
            <div class="alert alert-success" role="alert">
                Gửi thông tin thành công!
            </div>
        '''
    return render(request, 'contact.html',{
        'danh_sach_danh_muc': danh_sach_danh_muc,
        'form_lien_he' : form_lien_he,
        'thong_bao': thong_bao,
    })

def danh_muc(request, danh_muc_id):
    danh_muc_san_pham=Category.objects.get(id=danh_muc_id)
    danh_sach_san_pham = Product.objects.filter(category_id=danh_muc_id)
    danh_sach_danh_muc=Category.objects.all()
    #ket_qua = f'<h1>Bạn đang truy cập Danh mục: {danh_muc_san_pham}</h1>'
    return render(request, 'menu.html',{
        'danh_sach_danh_muc': danh_sach_danh_muc,
        'danh_muc_san_pham':danh_muc_san_pham,
        'danh_sach_san_pham':danh_sach_san_pham,
    })

def dang_ky(request):
    form_dang_ky = UserProfileForm()
    thong_bao = ''

    #Khi người dùng click nút "Đăng ký"
    if request.method == 'POST':
        form_dang_ky = UserProfileForm(request.POST, request.FILES)
        if form_dang_ky.is_valid():
            #Kiểm tra upload hình ảnh
            if 'avatar' in request.FILES:
                form_dang_ky.avatar = request.FILES['avatar']


            #Ghi thông tin vào CSDL
            form_dang_ky.save()

            #Thông báo thành công
            thong_bao = '''
                <div class="alert alert-success" role="alert">
                    Đăng ký thành công!
                </div>
            '''
        else:
            #Thông báo thất bại
            thong_bao = '''
                <div class="alert alert-danger" role="alert">
                    Đăng ký thất bại!
                </div>
            '''


    return render(request, 'register.html',{
        'form_dang_ky': form_dang_ky,
        'thong_bao': thong_bao,
    }) 


def demo_dtl(request):
    dtb=8
    
    ds_sinh_vien =[
        'Sinh viên A',
        'Sinh viên B',
        'Sinh viên C',
        'Sinh viên D'
    ]

    ds_sinh_vien_2 = [
        {'ma_sv':'SV001','ho_ten':'Sinh viên 1','dia_chi':'TPHCM'},
        {'ma_sv':'SV002','ho_ten':'Sinh viên 2','dia_chi':'Hà Nội'},
        {'ma_sv':'SV003','ho_ten':'Sinh viên 3','dia_chi':'Đồng Tháp'},
        {'ma_sv':'SV004','ho_ten':'Sinh viên 4','dia_chi':'Bình Thuận'},
    ]    
    
    return render(request,'demo_dtl.html',{
        'diem_tb': dtb,
        'dssv': ds_sinh_vien,
        'dssv2': ds_sinh_vien_2,

    })