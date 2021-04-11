from django.shortcuts import render

# Create your views here.

def wish_shakti(request):
  template = 'shakti/wish_shakti.html'
  # image_urls = [ 
  #   'https://drive.google.com/thumbnail?id=0B3lrnSe6BdE4UlZfOGNqYmotZFk',
  #   'https://drive.google.com/thumbnail?id=0B3lrnSe6BdE4bklLcEg3cW5KQmc',
  #   'https://drive.google.com/thumbnail?id=0B3lrnSe6BdE4M216WVh0WUlxRDg',
  #   'https://drive.google.com/thumbnail?id=1yhvBSKSIt7KsUw0vcvb1lQv2wY1ZFvAP',
  #   'https://drive.google.com/thumbnail?id=0B3lrnSe6BdE4ZUlUTnI2M25KTGc',
  #   'https://drive.google.com/thumbnail?id=0B3lrnSe6BdE4ZUlUTnI2M25KTGc',
  #   'https://drive.google.com/thumbnail?id=0B3lrnSe6BdE4ZUlUTnI2M25KTGc',
  # ]
  image_paths = [
    'shakti/img/bridge_1.jpeg',
    'shakti/img/2ndsem_1.jpeg',
    'shakti/img/bridge_2.jpeg',
    'shakti/img/act_1.jpeg',
    'shakti/img/2ndsem_2.jpeg',
    'shakti/img/convo_1.jpeg',
    'shakti/img/cooking_1.jpeg',
    'shakti/img/2ndsem_3.jpeg',
    'shakti/img/cooking_2.jpeg',
    'shakti/img/guard_1.jpeg',
    'shakti/img/2ndsem_4.jpeg',
    'shakti/img/mess_1.jpeg',
    'shakti/img/milan_1.jpeg',
    'shakti/img/2ndsem_5.jpeg',
    'shakti/img/milan_2.jpeg',
    'shakti/img/nanka_1.jpeg',
    'shakti/img/stairs_1.jpeg',
  ]
  video_urls = [
    'https://drive.google.com/file/d/133kNLh1BT0-gugs3_oKHotr7HG6_I-bd/preview',
    'https://drive.google.com/file/d/12zWDiBeRlardbjtr1IWj5b_jxv9NAYN5/preview',
    'https://drive.google.com/file/d/1CGqMN4uktfpSa7rxQ3bYxM5nMbwxW6bA/preview',
    'https://drive.google.com/file/d/11eLnMAyFQC_gCaVVorROIsk3rlELvxlp/preview',
    'https://drive.google.com/file/d/1M6cD2G9ZxtbFH_JDj5bSkZQXatHUSYsY/preview',
    'https://drive.google.com/file/d/1xwha96a9lj_CN7MY000R85TX_SpLaSnV/preview',
  ]
  context = {
    'image_paths': image_paths,
    'video_urls': video_urls
  }
  return render(request, template, context)