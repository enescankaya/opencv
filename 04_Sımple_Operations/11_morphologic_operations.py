"""Morfolojik işlemler, görüntü işleme ve bilgisayarla görme alanında kullanılan bir teknikler setidir. Bu işlemler, bir görüntünün şekil özelliklerinianaliz etmek ve 
değiştirmek için matematiksel morfoloji kurallarını kullanır. Morfolojik işlemler genellikle ikili (binarize) görüntülerle çalışır ve temel olarak görüntüdeki nesnelerin 
şekil ve yapısını analiz etmeye yöneliktir."""
"""Temel Morfolojik İşlemler:
Erozyon (Erosion): Görüntüdeki nesnelerin sınırlarını daraltır. Bu işlem, nesnelerin iç kısmını küçültür ve gürültüleri (küçük beyaz noktaları) temizleyebilir.

Genişletme (Dilation): Görüntüdeki nesnelerin sınırlarını genişletir. Bu işlem, nesnelerin iç kısmını büyütür ve küçük boşlukları doldurabilir.

Açma (Opening): Erozyon ve ardından genişletme işlemlerini uygular. Genellikle küçük gürültüleri ve ayrık nesneleri temizlemek için kullanılır.

Kapama (Closing): Genişletme ve ardından erozyon işlemlerini uygular. Genellikle küçük boşlukları ve delikleri doldurmak için kullanılır.

Küçültme (Hit-or-Miss Transform): Belirli bir yapı elemanını kullanarak bir desenin görüntüdeki konumunu bulur."""
import cv2,numpy as np
img =cv2.imread("word.png",0)
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)#beyazlıkları azaltıyor gibi, yani siyah kısımlar daha belirgin oluyor kalınlaşıyor
dilation=cv2.dilate(img,kernel,iterations=5)#tam tersi beyazlıkları kalınlaştırıyor
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)#resmin üzerindeki gürültüyü kaldırır. bulanıklaştırıyor biraz(beyazlıkları kalınlaştırıyor)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)#opening tam tersi siyahlıkları kalınlaştırıyor
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)#gradient beyaz çizgiler içinde siyah ile geçer. harflerin belirginliği için iyi bir yol
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)#dış çizgileri sadece belirginleştirir 
images=[img,erosion,dilation,opening,closing,gradient,tophat]
resized_images=[]
# for i in images:
#   resized_image=  cv2.resize(i,(300,300),interpolation=cv2.INTER_LINEAR)
#   resized_images.append(resized_image)

resized_images = [cv2.resize(i, (300,300), interpolation=cv2.INTER_LINEAR) for i in images]  #çok daha basit bir yöntem

# Resimleri göster
cv2.imshow("original", resized_images[0])
cv2.imshow("erosion", resized_images[1])
cv2.imshow("dilation", resized_images[2])
cv2.imshow("opening", resized_images[3])
cv2.imshow("closing", resized_images[4])
cv2.imshow("gradient", resized_images[5])
cv2.imshow("tophat", resized_images[6])




"""cv2.imshow("original",img)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)"""
cv2.waitKey(0)
cv2.destroyAllWindows()
