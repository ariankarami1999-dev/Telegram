<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/jigrrrwDjZa9CCsY8INFgSsd5VoVCqY0KWW-oI_N6bEfPoq1u178EHh1KQzwgjjh6G5qnJ-jfkUGG69mYopfagP6MXMlA_t7mrwS7AwiGFQSEwHzElO6SLvsHnSo9PMhntKUnpOXMlnPVa57uyTkg9InQLrvZalk1zfTT5TKhnpqBWv_XkIxbOUwdnwhYfE_tOkd3i5zWm8IOG0yv27pjbxGcn4djfRa1IRSSp-_VEl1h1dGfq0mXOXFuhymLlwlMuo8BR35XY-akRL9sBVm9w2-156ynKID0HXCyxfY72fMmOb_WNxPkBzqgwXwX-tXuOxz5DbFb1db8S7j8b1C-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 928K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 21:40:27</div>
<hr>

<div class="tg-post" id="msg-132106">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نیویورک تایمز: طبق داده‌های شرکت «کپلر»، در سه روز گذشته ۱۰۸ کشتی از  تنگه هرمز عبور کرده‌اند
🔴
با وجود بهبود نسبی تردد، مقامات دریایی گزارش می‌دهند همچنان حدود ۳۰۰ تا ۴۰۰ شناور با ۶ هزار خدمه در خلیج فارس سرگردان‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/132106" target="_blank">📅 21:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132105">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a913fff9.mp4?token=P_V-gyu8ROwlib9Dhxy1XHy-5xuys3Hi9YrsEgBmDjUQ2nelEqV-X4V1iWZqiBFEQ9zkT4-cugfQjHTe2R4F2vOvjo5wpHYjTgkLC9NYELSxjLVqbCqHuZChZgRifeN_6WHt4cHAhVkkzdnwVrPWREG4c87FTv7oVNkVD6nf8bT0nswATN3m8q3Z-I_WSKbWWdZ2WCcowmEmxZmRW1rytHe7nkGKJuRpMKtAHGIrtH5qtKlH1bYbvbJVzA3R95in_eiIy8YvkYF8B_Iv1_TPYxu6824UlHCEVothqVAb7GrEiB8-ThdQUqgcaKlMwGc37W0UPvTStSf27R4GVMaczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a913fff9.mp4?token=P_V-gyu8ROwlib9Dhxy1XHy-5xuys3Hi9YrsEgBmDjUQ2nelEqV-X4V1iWZqiBFEQ9zkT4-cugfQjHTe2R4F2vOvjo5wpHYjTgkLC9NYELSxjLVqbCqHuZChZgRifeN_6WHt4cHAhVkkzdnwVrPWREG4c87FTv7oVNkVD6nf8bT0nswATN3m8q3Z-I_WSKbWWdZ2WCcowmEmxZmRW1rytHe7nkGKJuRpMKtAHGIrtH5qtKlH1bYbvbJVzA3R95in_eiIy8YvkYF8B_Iv1_TPYxu6824UlHCEVothqVAb7GrEiB8-ThdQUqgcaKlMwGc37W0UPvTStSf27R4GVMaczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مکرون با عینک آفتابی خود وارد دمشق شد و توسط وزیر خارجه سوریه استقبال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132105" target="_blank">📅 21:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132104">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
شبکه ملی برق کوبا دچار فروپاشی شده است و یک قطعی کامل برق در سراسر جزیره گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/132104" target="_blank">📅 21:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132103">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ادارات برخی استان‌ها سه‌شنبه و چهارشنبه ۱۶ و ۱۷ تیرماه تعطیل شد
🔴
روزهای تعطیل:
🔴
سمنان: سه‌شنبه و چهارشنبه
🔴
مازندران: سه‌شنبه
🔴
هرمزگان: سه‌شنبه
🔴
کاشان و آران و بیدگل: سه‌شنبه
🔴
مرکزی: سه‌شنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/132103" target="_blank">📅 20:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132102">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01f989eae.mp4?token=SPG-q95njn365MW0Gflarg9cSF4ba_mDrTOCL0Me0iwc9fRZ93iNKIsn58PiuGiKwuc3Sp1y-aPF9FNgMLZST7mN66G45dREjNGxIhyVxgohBcq6IUM2wbRMD2WJpJPWyk8E6kHWKM6f9jm02fFaJRvMTFsRxpcOSHpLge-or8WGm9M1X3oRbj-RmGzaAVog_52KyGdid4pTjZwVayBxRTSIy9itgvIa48qgx3dgibs-VtpO8856T4pbWxlBsWcP-a_y4gRS6edd7XofMTAJmUUCkj1QY7SQsfXJiuEdiOqvHgF4uFKLoySTWDhgQY_zCBehx-2sbAyVvviCDIQryTg9Q_i3e4xUscH-E4KyjzHMKUNKIUQXfMku4mHIkIe0WIX-IA4vQZ5xV0bEzcxZrqDLl1q_N6NXovI1Mo9cvZbla3NtaysJoVrlMUGLQEyN4Ny7aK85l-iCB4qZRFGJLwiGC3KYjmsxfXXcf83Qs-Q78zK9-Hha8NNW7ijI4Boz6OLc8jlGe8FFZQ3MizXv1Qn0vldNLdXkL46AIBtmNabRZZclUhoIjdJAYcFtzTJlo4nd2CsMcFhYsY2lZlQ4yFRbKixtljA4SOk02m4g8JXNAbki1aJmD5ZJVZ2LVVTh-434j_LEI3XOyVBnnQlKuIHlQUzZ8PwZ2EZ9DpQ_i3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01f989eae.mp4?token=SPG-q95njn365MW0Gflarg9cSF4ba_mDrTOCL0Me0iwc9fRZ93iNKIsn58PiuGiKwuc3Sp1y-aPF9FNgMLZST7mN66G45dREjNGxIhyVxgohBcq6IUM2wbRMD2WJpJPWyk8E6kHWKM6f9jm02fFaJRvMTFsRxpcOSHpLge-or8WGm9M1X3oRbj-RmGzaAVog_52KyGdid4pTjZwVayBxRTSIy9itgvIa48qgx3dgibs-VtpO8856T4pbWxlBsWcP-a_y4gRS6edd7XofMTAJmUUCkj1QY7SQsfXJiuEdiOqvHgF4uFKLoySTWDhgQY_zCBehx-2sbAyVvviCDIQryTg9Q_i3e4xUscH-E4KyjzHMKUNKIUQXfMku4mHIkIe0WIX-IA4vQZ5xV0bEzcxZrqDLl1q_N6NXovI1Mo9cvZbla3NtaysJoVrlMUGLQEyN4Ny7aK85l-iCB4qZRFGJLwiGC3KYjmsxfXXcf83Qs-Q78zK9-Hha8NNW7ijI4Boz6OLc8jlGe8FFZQ3MizXv1Qn0vldNLdXkL46AIBtmNabRZZclUhoIjdJAYcFtzTJlo4nd2CsMcFhYsY2lZlQ4yFRbKixtljA4SOk02m4g8JXNAbki1aJmD5ZJVZ2LVVTh-434j_LEI3XOyVBnnQlKuIHlQUzZ8PwZ2EZ9DpQ_i3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقام از ترامپ با دمپایی و کمربند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/132102" target="_blank">📅 20:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132101">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ:اگه بازیکنمون بخشیده نمیشد و مقابل بلژیک حذف میشدیم، من میگفتم مثل انتخابات ۲۰۲۰ اینجا هم تقلب شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/132101" target="_blank">📅 20:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132100">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilxyP6aGgqwZKAEaDmwWk_8DFEIvAaCtBcGLX068_BOjlLq_-rG4VwWkXIY1EfN8i4miTWJj7C_PhQzF-ZaMzT3yIjIT9bf-xw6m-_AR-wgd-HUPTEgIWNB1bD1o2lELZUKfzACarzagryhavEN6__gsAier9K1QYK0jKB5GuASgjWTXjSpI_r1crVcMw5OzkFsPsl4hypzqZo3Oerm8dEW3qRrJdJo509Bd5HyDkViKOr4C-pWXtQVQleiND515WqLCt8uUjGGq9LrAAiYklVEXdhjBJQXqUC4H5mXXhgGepGwcktpGbQeW-EKBNJGBkwSuam0QFsZntcEA_HIogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط شریعتمداری، مدیر هولدینگ خلیج فارس هم کلی پول رپورتاژ داده تا کانالا بزنن که اومده به مراسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/132100" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132099">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سفیر اسرائیل در ایالات متحده:
ما معتقد نیستیم که ترکیه باید هواپیماهای جنگنده F-35 را در اختیار داشته باشد.
🔴
با این حال، اسرائیل درک می‌کند که دولت ایالات متحده مجموعه‌ای گسترده‌تر از ملاحظات استراتژیک را باید در نظر بگیرد، زمانی که در حال اتخاذ تصمیم است.
🔴
ما مخالف فروش هواپیماهای جنگنده پنهان‌کار F-35 به ترکیه هستیم، اما به هر تصمیمی که آمریکا بگیرد، احترام خواهیم گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/132099" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132098">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFHzuVCmK9h5kduRkXQzWrc4nLGytDO5jIcfI3eaZlCvJrgF1IgTB1i59IbyEdmtAK3YwCSfNvomodbFsHu-lczI1aSkURm1CYWvPAC9DX-Q7ldP-kdmcWDMl-AxWM4NpR_AydFTftinjHGLHczcs5Fg5WD869_ywA7Alh7u-kqTMVeqsPdiIkJEZ-Q9hFAWJSImB5uf3Om1DR4C9Xo4DMuawQaFn7aw-UHDB897_xFJSRpfOy-MmFY6LQCTeBm-93F5CUljsMagKAf_tz0nj5A4TuHFjU8W3Ri16vhNZby1iLYjwTKgImk3r3BmcMfxv80lgDEL8B_2PrBV8NjOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ حسام الدین آشنا به عدم حضور حسن روحانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/132098" target="_blank">📅 20:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132097">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b484bee13d.mp4?token=H7yAzKM-PWzLfa0Z7wiw-b6lr7slb5iUV8aLm7JUEWpXQuI2l4wCV43HbviObl8jeETY2iME6xsIzEZGZl6QZMWUoWZgfjLiwDwjNAhGUsoFoZngPJszTN5WNcMUpCjyLpLvMIG79Pp6uevi9sIMNNBUh-lPgkoBCINPWSjHONffFQg6lDVNnf6_aSCVTHIAwlVWbZbq_gRz15hfrkHU3hN91ofIMbhdSwCi1x7tj5pOV-Z4j_Jmp9xca8NcsCLJkgNpZenJpVuNnOkCakhbgcUqh4qczwQj55nPuMwc0WZJZ_5Vd36kKPCauQIGa2uqBLClGePZN6ZeGGI0JRg3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b484bee13d.mp4?token=H7yAzKM-PWzLfa0Z7wiw-b6lr7slb5iUV8aLm7JUEWpXQuI2l4wCV43HbviObl8jeETY2iME6xsIzEZGZl6QZMWUoWZgfjLiwDwjNAhGUsoFoZngPJszTN5WNcMUpCjyLpLvMIG79Pp6uevi9sIMNNBUh-lPgkoBCINPWSjHONffFQg6lDVNnf6_aSCVTHIAwlVWbZbq_gRz15hfrkHU3hN91ofIMbhdSwCi1x7tj5pOV-Z4j_Jmp9xca8NcsCLJkgNpZenJpVuNnOkCakhbgcUqh4qczwQj55nPuMwc0WZJZ_5Vd36kKPCauQIGa2uqBLClGePZN6ZeGGI0JRg3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: یک سوشیال دموکرات، یک کمونیست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/132097" target="_blank">📅 20:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132096">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ : خیلی از اینایی که اینجان
🔴
حتی درست‌وحسابی نمی‌تونن راه برن، ولی خرپولن
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/132096" target="_blank">📅 20:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132095">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: من لری [فینک] و برخی از بزرگترین افراد وال‌استریت را می‌بینم: گلدمن ساکس، بلک‌استون، بلک‌راک. همه آن‌ها اینجا هستند.
🔴
به آن فکر کنید. من همه آن‌ها را نابغه می‌دانم. هر یک از آن‌ها نابغه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/132095" target="_blank">📅 19:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132094">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ: به پادشاه چارلز گفتم شاید بهتر باشد یک لقب خوب مثل «چارلز فاتح» داشته باشد.
🔴
او گفت: «نه، نه، نه، لطفاً.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/132094" target="_blank">📅 19:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132093">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
حالا که حماس تسلیم شده بهتره اونایی که تو ایران عشق جنگ دارن رو با کامیون اعزام کنیم غزه تا به آرزوشون برسن، البته اگه
تخم
داشته باشن چون همیشه عادت دارن جاهایی شعار بدن که امنیت کامله و خوراکی و عشق و حال به راهه</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/132093" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132092">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4810d9bf95.mp4?token=FQ-mF2A5IOtEiGabyOoQ4_ZXOYkVCBVwyQq0rDk4rGE8D0qQk0w1eFzxuz7DBkXj6qTNS82m-Ph909SXNbpU8cZ1GAo4XmQpjz7WC_1puOAbHpV4og8fmKEA1CcDEIOZUw0toiK7BGDPzQyth3dD41ffHz5mi_QT9MDvrHyaZliSyToPDh4pwp8NTQSY7Oo3dPxfaF5293r_u2NZmkPP262v4Yf0roDuxICTX18LF_ApALvGS5p2rqYy4L7-fyphQuEI1ZPW_02YsqZIVYhlSRl42eKUuVMoISwTdcvu_rqjk7XcfsvATLBHPjgtvmaGlGmFEj41yNxxuLHuEEnlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4810d9bf95.mp4?token=FQ-mF2A5IOtEiGabyOoQ4_ZXOYkVCBVwyQq0rDk4rGE8D0qQk0w1eFzxuz7DBkXj6qTNS82m-Ph909SXNbpU8cZ1GAo4XmQpjz7WC_1puOAbHpV4og8fmKEA1CcDEIOZUw0toiK7BGDPzQyth3dD41ffHz5mi_QT9MDvrHyaZliSyToPDh4pwp8NTQSY7Oo3dPxfaF5293r_u2NZmkPP262v4Yf0roDuxICTX18LF_ApALvGS5p2rqYy4L7-fyphQuEI1ZPW_02YsqZIVYhlSRl42eKUuVMoISwTdcvu_rqjk7XcfsvATLBHPjgtvmaGlGmFEj41yNxxuLHuEEnlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاجعه مراسم امروز
‼️
🔴
حمله جماعت تندرو به پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/132092" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132091">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ--dFLo3a1Ig1CGYj6Oj2MXsqTVTNZsUcy-fX-D7swQNCWT9-65YaSMD5-mpCQHJOqbV4vChEtsjmrUu6FQkkB15rmqsLoJk6yC9-1NRyrV0yO9Ok8M1V6Pr6qbuTuJe2lEnCYxvAmIsrwaJXZlra7InNVrRCWkKZZM3rDA3S398NxrApk0gVJW78Cf5YspEKKGrqOfEma9H8MSaVCurqbEgQ_54gO29de7CMpZKxPVeMxBypy_M0xHdoQASm-J60BhzmGDiKbfrNqAdIxI7Rryck9lBWQnRhYvdZhiDk6Ht11czOwDDzV_4w_rpYQ3nyvULJmhfZw2ombv6YIbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی عبدی، تحلیلگر: امام خامنه‌ای بزرگترین شخصیت تاریخ ایران هست
‼️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/132091" target="_blank">📅 19:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132090">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHx7ujAucCEK74i5etLJAWbz76iz_OlWnZkYJDRiGS2pm0F9XnbJH_YL3Nd3t4XcgIW_g0m8HQibtfVTUhqMmK7r7PaaYLA9kHgAMsKUe9b7QYXXgNa1Sh0Wzg3UrEwfNDyzTLwpaFKWXpv4rNLEviSDRpkThhGwYQ6tkxP0nxJEY1PBWtT7qUIZqImqcoYa_1y_S28ZF_DxSRiW9sSPqanCEAl0g0276rqePnZ0F2YcEbvMjk7OO4lxTgdhXkXunWFRaZtDb4l-6eWCroFOtlFn5UJGz5tzNBQeVwvmPLSV1FUONMJZOgKdfic-vA5FUalaUAYqKPPddwoAfnzJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/132090" target="_blank">📅 19:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132089">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
🔴
می‌شنوم «آن‌ها بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
🔴
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
🔴
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
🔴
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/132089" target="_blank">📅 19:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132088">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / الحدث: ساعاتی پیش حماس تسلیم شد نخست وزیر خود خوانده او طی یک کنفراس خبری استعفا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/132088" target="_blank">📅 19:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132087">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فیدان: روابط رجب طیب اردوغان، رئیس‌جمهور ترکیه با دونالد ترامپ، رئیس‌جمهوری آمریکا می‌تواند به کاهش تنش‌ها در ناتو کمک کند، زیرا رهبران کشورهای عضو این ائتلاف خود را برای دیدار در آنکارا آماده می‌کنند.
🔴
برای ترامپ، این موضوع صرفا به اعتماد و دوستی مربوط می‌شود. ترکیه قصد دارد به سود کل خانواده ناتو رفتار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132087" target="_blank">📅 19:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132085">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlhK03z6XEsatVmH5aevMl2TAIOBLm2adRpFNwotp5IeQ2Hpmtcu_NzXwEKA6bRSLh_THNV3xvBUILuGOwb908ZrzmnKDv_FKb3wM4SMZ57Snfum0UbjcRmrxrhr1830sS6ZsJXJPPtnSl0BpkZYAjc6K7gH86glWsM0ZbjOq7fNbX-Wbsd6mtU8hHE9TFGRd91LMuWfn283zKsTerplLJgBdOO6DZ7UMzqcSnGA2iu25XDrLKiXw5scKkaPzHmxx4dw7ptmgFiOXB1HOVtizD4b_pFjW3cMf0tPWPNSyqJH509COkoM8GiRT2mOn__8UpDOgAlhEZHvgFcQWSrQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtrGLbMcoUjvANrIFkDWyceKUaHj0Ru5uP4LAIIxo07PYcrX87gIyUG5JX-n6I9kQEeJfyGFusUuAmopzUyS4Xgaxlh90OMhAmh1NpchU49jUQF2c041Pt_rQ2j1pM_7cxCCmxewZjaz76avLBLXpNMNcOmm0lJiAnl5BHw8FPLJLtE0jaSrw9igIPGh4jCCOfkEuQZ75fhz66g00zPIoe3XIvPMiEEDXCqvQd434mkrCV7Y8I6zoBNh7Vs1Ei6oZF-uWwiK-dCnt9aSYlZw8uKvRfm-W6UtBI2JXVMk2r7p_p74ML_nNaWRAIo_fKUeDABI7uzd-I_6WXM6bUbiLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال با انتشار این پست ها از مرزهای کشور در دوره بایدن و مدارس دخترانه تمام محجبه در مینه‌سوتا انتقاد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132085" target="_blank">📅 19:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132084">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285e95c239.mp4?token=P_XF_v48dF8yyH3_WEUANZje1_8kkxj6580jmjC2_lw68JP7yzxlvzf0hUErkUjxgGnd6OZp8sJwyTezUxABz38b81kQJR5PvQYzt_WwLcbDldLve_jjW7hNRmUALj6A-X9l5S0SUoHbFXw2paaBWTNpZCISmnjK8e1PkmnK-p_8GPjqTOVDAiyG_vUQHkNfOWT2MHBSazGfO1W_IC_Bk7Yp6dtG9hU0X_sj3COF5atvrbinroPPsu0KW_7UqDPps19qu8cMsKJCvMRQKYGuWQa8swkp_ZLThmMPjieShpEZ_OywZrLjhUyiPPhvYmWDS2Lzl3kOKJgFC4Ir40bnCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285e95c239.mp4?token=P_XF_v48dF8yyH3_WEUANZje1_8kkxj6580jmjC2_lw68JP7yzxlvzf0hUErkUjxgGnd6OZp8sJwyTezUxABz38b81kQJR5PvQYzt_WwLcbDldLve_jjW7hNRmUALj6A-X9l5S0SUoHbFXw2paaBWTNpZCISmnjK8e1PkmnK-p_8GPjqTOVDAiyG_vUQHkNfOWT2MHBSazGfO1W_IC_Bk7Yp6dtG9hU0X_sj3COF5atvrbinroPPsu0KW_7UqDPps19qu8cMsKJCvMRQKYGuWQa8swkp_ZLThmMPjieShpEZ_OywZrLjhUyiPPhvYmWDS2Lzl3kOKJgFC4Ir40bnCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در حاشیه مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132084" target="_blank">📅 19:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132083">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
اکونومیست: بسیاری از کشورهای اروپا از هدف دفاعی ناتو عقب می‌مانند
🔴
بسیاری از کشورهای اروپایی تا سال ۲۰۳۵ به هدف ناتو برای اختصاص ۵ درصد از تولید ناخالص داخلی به بودجه دفاعی نخواهند رسید.
🔴
این گزارش می‌گوید با افزایش نگرانی‌ها از تهدید روسیه و احتمال کاهش حمایت نظامی آمریکا، کشورهای اروپایی باید توان دفاعی خود را تقویت کنند.
🔴
همچنین بررسی‌ها نشان می‌دهد کشورهایی که به روسیه نزدیک‌تر هستند، در سال‌های اخیر بودجه دفاعی خود را بیشتر از سایر کشورها افزایش داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/132083" target="_blank">📅 19:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132082">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/132082" target="_blank">📅 19:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132081">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کاتز، وزیر دفاع اسرائیل : وقتی برای هر شرایطی آماده باشی، دیگه هیچ محدودیتی برات وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132081" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132080">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ درباره دیدار آمریکا-بلژیگ:
باید اجازه دهید از بهترین بازیکنان خود استفاده کنند و بازی امشب شگفت‌انگیز خواهد بود.
🔴
ما یک تیم کامل خواهیم داشت و بلژیک نیز یک تیم کامل خواهد داشت و می‌دانید چه؟ اگر ما را شکست دهند، می‌توانند واقعاً به خود افتخار کنند.
🔴
اما اگر راه دیگر را در نظر بگیریم و ما را شکست دهند (اگر کارت قرمز تعلیق نشده بود)، می‌گفتم که بازی تقلبی بوده، درست همان‌طور که انتخابات در سال ۲۰۲۰ تقلبی بود، اما من وارد آن موضوع نمی‌شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132080" target="_blank">📅 18:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132079">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
خبرنگار: آیا در حال ساخت فرودگاه هلیکوپتر هستید؟
🔴
ترامپ: بله. در طول ۵۰ سال، هلیکوپترها روی چمن فرود می‌آمدند. چمن خیس و گِلی است. شرکت سیکورسکی بابت آن پرداخت می‌کند.
🔴
ما تعدادی هلیکوپتر سیکورسکی سفارش دادیم. خوب، آن‌ها حدود دو و نیم برابر قدرتمندتر از مدل‌های قدیمی هستند. وقتی روی چمن فرود می‌آیید، مشکل این نیست که چمن تغییر رنگ می‌دهد. چمن کنده می‌شود. کنده می‌شود.
🔴
یک بار هلیکوپتر فرود آمد و نیمی از چمن جلوی در ورودی دفتر بیضی نشسته بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132079" target="_blank">📅 18:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132078">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: من فقط به یک دلیل به یک طرفدار بزرگ کریپتو تبدیل شده‌ام: اگر ما آن را نداشته باشیم، چین آن را خواهد داشت و آن‌ها دوست دارند آن را داشته باشند.
🔴
اما اکنون آن‌ها حتی تلاش زیادی هم نمی‌کنند زیرا ما بر کریپتو مسلط شده‌ایم.
🔴
من طرفدار آن هستم. در ابتدا نبودم. خیلی درگیر نبودم، اما تماشا می‌کردم. می‌دیدم که پول زیادی شروع به ورود با بیت‌کوین و، می‌دانید، اشکال مختلف آن می‌کند. و گفتم: «این چیز زندگی زیادی دارد.»
🔴
ما در هوش مصنوعی به‌طور قابل‌توجهی جلوتر از چین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/132078" target="_blank">📅 18:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132077">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رییس جمهور دولت مستعفی یمن: گزارش‌ها حاکی از آن است که پرواز انجام‌شده از سوی ایران به مقصد صنعا، حامل پرسنل نظامی و کارشناسان موشکی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132077" target="_blank">📅 18:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132076">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9701b8ad3d.mp4?token=dxl20h7c5ELlN3pH3-42ELLbd2vlc5dVdLIe29Zu-3GRmZ3mYhNPvqtfPlAW6MYUKte7oEQRHsvoPkjhPfo2ptdo5pORDjnfXmH7wl7ZHCvk8iGEbhTllFtIWNyXoMfdhHJfW5fonTWZ96TYAOnV-WSYT1kuQ2WybqTQDMzqVLSu5-nqmjHuZ0axLWIJxKTEZ3PBNpigBJ1VZ38tOCYsLqTtrlkuyiDNJC5ebdr86fsdvhoe9wtT0RTvPZG9MRQ85g2GNqNRuYCOO77Ftcxc_UQD3T3pW60N5dO4kr1ArSroyNzCi8osQrqMTqkpy38Ih_Q_GYV_vuWmSOM31XzGDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9701b8ad3d.mp4?token=dxl20h7c5ELlN3pH3-42ELLbd2vlc5dVdLIe29Zu-3GRmZ3mYhNPvqtfPlAW6MYUKte7oEQRHsvoPkjhPfo2ptdo5pORDjnfXmH7wl7ZHCvk8iGEbhTllFtIWNyXoMfdhHJfW5fonTWZ96TYAOnV-WSYT1kuQ2WybqTQDMzqVLSu5-nqmjHuZ0axLWIJxKTEZ3PBNpigBJ1VZ38tOCYsLqTtrlkuyiDNJC5ebdr86fsdvhoe9wtT0RTvPZG9MRQ85g2GNqNRuYCOO77Ftcxc_UQD3T3pW60N5dO4kr1ArSroyNzCi8osQrqMTqkpy38Ih_Q_GYV_vuWmSOM31XzGDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: هر بار که مردی را در حوزه ارزهای دیجیتال می‌بینم که تحقیقی را منتشر کرده، می‌گویم: «تو خوش‌شانسی که من رئیس‌جمهور هستم.»
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/132076" target="_blank">📅 18:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132075">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49e2cfdc7.mp4?token=gu4J24kh-dzQdBWiWwIOa8-eN_YiNPkqh73empSHP5maHwiO6eZtJ5VypZBHdna--yrJHijmPurKQYyxU4yTSjizmpOJKFD6xn0danVr6roKaLNujIFQH6rR9lyDCEbmH4JheXSwJtZHAdxQbLlxY-g9vhq1c6S2fWkrc9QzlMooRExrXmWXtFsljHrcyyiTkgpoNcVfES0eRvsMRcM2kkFDH0GIFPArBAZNshCw95z-fD792HUVX9KFoJhNJVliP2wE7SFImp7Vhg7RT8G-2dZkCczLDyoIIikhKjkLxyV4AoyuJLM3mPMaQllqfk_gvZrtiE9aMR9yQLBxgTq9vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49e2cfdc7.mp4?token=gu4J24kh-dzQdBWiWwIOa8-eN_YiNPkqh73empSHP5maHwiO6eZtJ5VypZBHdna--yrJHijmPurKQYyxU4yTSjizmpOJKFD6xn0danVr6roKaLNujIFQH6rR9lyDCEbmH4JheXSwJtZHAdxQbLlxY-g9vhq1c6S2fWkrc9QzlMooRExrXmWXtFsljHrcyyiTkgpoNcVfES0eRvsMRcM2kkFDH0GIFPArBAZNshCw95z-fD792HUVX9KFoJhNJVliP2wE7SFImp7Vhg7RT8G-2dZkCczLDyoIIikhKjkLxyV4AoyuJLM3mPMaQllqfk_gvZrtiE9aMR9yQLBxgTq9vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
ادعا می‌کند که انرژی بادی برای محیط زیست مضر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132075" target="_blank">📅 18:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132074">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
روس اتم: ما مذاکرات ایران و آمریکا را بسیار به دقت دنبال می‌کنیم، به همه جزئیات واقفیم
🔴
به احتمال زیاد به مشارکت ما در حل‌وفصل موضوع برنامه هسته‌ای ایران نیاز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132074" target="_blank">📅 18:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132073">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ: یک برنامه‌ای وجود دارد به نام تیک‌تاک. آیا اسمش را شنیده‌اید؟
🔴
حدود دو روز پیش اعلام شد. آیا می‌دانید که محبوب‌ترین فرد در تیک‌تاک کیست؟ ترامپ.
🔴
تایلور سویفت در رتبه یازدهم قرار داشت. من به طور قاطع در رتبه اول تیک‌تاک قرار دارم.
🔴
آن‌ها در مورد خطرات بسیار زیاد ناشی از نفوذ تیک‌تاک صحبت می‌کنند.
🔴
شاید این برنامه بد باشد. شاید هم نباشد. اما یک چیز را می‌دانم. مردم بزرگ آمریکا، افراد برجسته تجاری و شرکت‌های بزرگی آن را خریداری کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132073" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132072">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b9f4c114.mp4?token=f-o2e1mymhtEwm67SHzJ8mQTdgIEhrF0IrqhrpmhWaKlPXLLBIcibnvqns2e-Rru7o1W50pDtH3RCf3EFQDo4VV9uIAJhNYFpNFEz6VgZWhImSGwCsLR0jek8C8gmwxZBcSnT0z8QITqajqIwn8oOmDt291TdgMYvoWvLwFZ8Ul2mjawLaOBUNpV6TNH3-qMCBrKATRAscygpKiL442DtjYCkIBWBYEosW-OtYiP1uiNeWV2DRGpgPZ-42G5KOxugaEJEkQDJMkGGdKuf0VkOcTHKPoWzQIDzNwBZNEutwQUNj5QnHM2EnNkwZPIWBH8w0qQ3gPCS4R4YTF7A6i9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b9f4c114.mp4?token=f-o2e1mymhtEwm67SHzJ8mQTdgIEhrF0IrqhrpmhWaKlPXLLBIcibnvqns2e-Rru7o1W50pDtH3RCf3EFQDo4VV9uIAJhNYFpNFEz6VgZWhImSGwCsLR0jek8C8gmwxZBcSnT0z8QITqajqIwn8oOmDt291TdgMYvoWvLwFZ8Ul2mjawLaOBUNpV6TNH3-qMCBrKATRAscygpKiL442DtjYCkIBWBYEosW-OtYiP1uiNeWV2DRGpgPZ-42G5KOxugaEJEkQDJMkGGdKuf0VkOcTHKPoWzQIDzNwBZNEutwQUNj5QnHM2EnNkwZPIWBH8w0qQ3gPCS4R4YTF7A6i9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
🔴
من به دنبال تغییر رژیم نیستم، هرچند که این همان تغییر رژیم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/132072" target="_blank">📅 18:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132071">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/740daf8e44.mp4?token=mujC8LWOg6md93EOjW3CpeLIKf1GMVPZB8nUZfBNCV1-c0_2yE3ChciArV1ilD9VUuKLP0uqa_PEQNYTnez_S4Un_rc6eEf1O6QMLEG1Foz-f3nT_5oFXqpg4zfyXGEIaT9Ln2h1pAivajoyE_PkiAeADFTzNw5d4s7JyvVfIc6DPQY1KF2BMiS2-nk4vW2lmn609i4wAZvIfh_8zC1YGpVg1pXSnI0roVkSq0cP0cWcDFn-KiCch17c_ZBngKJ1s_kYZUDYep63hOKqy9LtsTN-pMRL5UsKTyFE32CmPc8olp0nwEhaTKYETyVc5XnP-Oh34YdJLFo4WVtBbN-ZPYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/740daf8e44.mp4?token=mujC8LWOg6md93EOjW3CpeLIKf1GMVPZB8nUZfBNCV1-c0_2yE3ChciArV1ilD9VUuKLP0uqa_PEQNYTnez_S4Un_rc6eEf1O6QMLEG1Foz-f3nT_5oFXqpg4zfyXGEIaT9Ln2h1pAivajoyE_PkiAeADFTzNw5d4s7JyvVfIc6DPQY1KF2BMiS2-nk4vW2lmn609i4wAZvIfh_8zC1YGpVg1pXSnI0roVkSq0cP0cWcDFn-KiCch17c_ZBngKJ1s_kYZUDYep63hOKqy9LtsTN-pMRL5UsKTyFE32CmPc8olp0nwEhaTKYETyVc5XnP-Oh34YdJLFo4WVtBbN-ZPYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد جنگ پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
🔴
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
🔴
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132071" target="_blank">📅 18:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132070">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfaf82d48a.mp4?token=vR9Nuz4Lv4TxsynrxkkGt2Qe5nbsmjWazsGPpnMz0_oR-2k3yo7OxYB-acVNLixItWdHVsLxdHBWppR_lPEpWN38gFIWc2tHCDDPGtkKffFGAw09Y9G5cCr7qJFZFvDCW0BEllvYS99Nr28l-OCgDSss_ip8sEJhdufcJeVROyUUUGQYMZmWv60WceIqWqT7DQtIVS_oobliJ2Eyt86G50KqhkheSaUrFU41FRDYNqBus_kxTFDnomTLVCFhV-DK-l0TRAUPd-I0Jbu-5CmGg9N5U701DImzNczFPU4XG-2PVseKZpKIW_5qnyD6EgOvVLWzB41H7huAo-z1TUpo-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfaf82d48a.mp4?token=vR9Nuz4Lv4TxsynrxkkGt2Qe5nbsmjWazsGPpnMz0_oR-2k3yo7OxYB-acVNLixItWdHVsLxdHBWppR_lPEpWN38gFIWc2tHCDDPGtkKffFGAw09Y9G5cCr7qJFZFvDCW0BEllvYS99Nr28l-OCgDSss_ip8sEJhdufcJeVROyUUUGQYMZmWv60WceIqWqT7DQtIVS_oobliJ2Eyt86G50KqhkheSaUrFU41FRDYNqBus_kxTFDnomTLVCFhV-DK-l0TRAUPd-I0Jbu-5CmGg9N5U701DImzNczFPU4XG-2PVseKZpKIW_5qnyD6EgOvVLWzB41H7huAo-z1TUpo-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته دبیرکل ناتو در آنکارا: اگر شما یک جوان در روسیه زندگی می‌کنید و به پیوستن به تلاش‌های جنگی فکر می‌کنید، دوباره فکر کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132070" target="_blank">📅 18:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132069">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b1f31782.mp4?token=Ulplcr02h4X4CnHFzyC0aIOoa5zFsU4OY6QitGRFMiayfGUGhJNgvaBX4mG3a3ohWYDkeL8C60vwqcD6Rs8DTpsJIxuwW3urqu0kOy3jJUC8TYMCitZWiChdMGmUo6BuTQv6HKJVToCpqs5hOwu_zflZ4WZ09gFXcaO46xw4gesDd1axBcUuhCCXI1wYXIKeUTJnFMnR21okBpQ9cRP8fYuEBeOCcVAyVYveQnDxSQYHLv1FWJ-BgflotNv1MB5O9hWnlFufDujx5_QY0_xyJPMPcEsav8z7WXtlE3dAiUdcUkhzMuDYBsdhwLSztpKow56dsZn_7XUbRAXUJ6VS2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b1f31782.mp4?token=Ulplcr02h4X4CnHFzyC0aIOoa5zFsU4OY6QitGRFMiayfGUGhJNgvaBX4mG3a3ohWYDkeL8C60vwqcD6Rs8DTpsJIxuwW3urqu0kOy3jJUC8TYMCitZWiChdMGmUo6BuTQv6HKJVToCpqs5hOwu_zflZ4WZ09gFXcaO46xw4gesDd1axBcUuhCCXI1wYXIKeUTJnFMnR21okBpQ9cRP8fYuEBeOCcVAyVYveQnDxSQYHLv1FWJ-BgflotNv1MB5O9hWnlFufDujx5_QY0_xyJPMPcEsav8z7WXtlE3dAiUdcUkhzMuDYBsdhwLSztpKow56dsZn_7XUbRAXUJ6VS2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تنگه معروف هرمز؛ ماشین پول ساز بزرگی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132069" target="_blank">📅 18:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132068">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0da10c12.mp4?token=IdiTUWNsswBulP4Ix8E_GheIPutl5nRxRWPcNUDWwukLiDtDl6xBhmX1cRNL0--IwbMy3b2p6oZ5yS5yfhjK_6JioTLGlEOKluPZzbcV3VByD4K_FIbDGpY0XVYhutvuwOrXMulgXg-G7GFHH2uUULdgaDDDFI4ceipUzktigZdXEJ5qqIMyOrAxxOwlv_i4Mhn27LqMZRx_RW_xe5SyIzi9cO96fvNRgJsbhetFplRU6HqfXkB0eMbjyby08D3DTYJJ3U3lqdJdd9LK2zM__SBPmlhwXEH9DV_k5AsovS0E7o-vrpVI-uWC7RNxXMXc-nefQQN8Ye7B7Ae8HbQmLiM3D4uvVZqf9m3NPI7c_c2Ipouq2Vd2Tmig0RkzEyDJeRTkDaWS0VtWrSCpF9YUeR0BGik_8BwVg9dlNHHNMqMHT1tNTKyxnAv8o4A3slcSErMI74ADnLTgIcVK9QPEzWNSKXzb58eONRupbabl-ET3_zZ4VTjXTuhsBxIlFlgy7vyhoXvJcowovZkGSaAk5obncsacAyqQutqU9m24seMD_nG_6EJOzYrvCoomtKiwKWuqvaYzUrClfZ82TXfg1q7-HmonO8kYQIeOnPB8_l1iQjvRiisv1diQHKx2yLVvy5LyhBIB8P2G2p3caBqUIiL86vqs-cmPvUi0QLL5XIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0da10c12.mp4?token=IdiTUWNsswBulP4Ix8E_GheIPutl5nRxRWPcNUDWwukLiDtDl6xBhmX1cRNL0--IwbMy3b2p6oZ5yS5yfhjK_6JioTLGlEOKluPZzbcV3VByD4K_FIbDGpY0XVYhutvuwOrXMulgXg-G7GFHH2uUULdgaDDDFI4ceipUzktigZdXEJ5qqIMyOrAxxOwlv_i4Mhn27LqMZRx_RW_xe5SyIzi9cO96fvNRgJsbhetFplRU6HqfXkB0eMbjyby08D3DTYJJ3U3lqdJdd9LK2zM__SBPmlhwXEH9DV_k5AsovS0E7o-vrpVI-uWC7RNxXMXc-nefQQN8Ye7B7Ae8HbQmLiM3D4uvVZqf9m3NPI7c_c2Ipouq2Vd2Tmig0RkzEyDJeRTkDaWS0VtWrSCpF9YUeR0BGik_8BwVg9dlNHHNMqMHT1tNTKyxnAv8o4A3slcSErMI74ADnLTgIcVK9QPEzWNSKXzb58eONRupbabl-ET3_zZ4VTjXTuhsBxIlFlgy7vyhoXvJcowovZkGSaAk5obncsacAyqQutqU9m24seMD_nG_6EJOzYrvCoomtKiwKWuqvaYzUrClfZ82TXfg1q7-HmonO8kYQIeOnPB8_l1iQjvRiisv1diQHKx2yLVvy5LyhBIB8P2G2p3caBqUIiL86vqs-cmPvUi0QLL5XIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کارت قرمز بالوگان:
من [به کارت قرمز اعتراض کردم].
🔴
من با جیانی [اینفانتینو] صحبت کردم، که بسیار محترم است و به گفته آن‌ها، او موفق‌ترین جام جهانی های تاریخ را چهار بار برگزار کرده است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132068" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132067">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ راجب هری کین : فکر می‌کنم کین بازیکن فوق‌العاده‌ای است. با او گلف بازی کردم و خیلی دوستش دارم.
🔴
گلف‌باز خوبی است. واقعاً عالی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132067" target="_blank">📅 18:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132066">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ:
نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
🔴
ما می‌توانیم تامین انرژی ایران را مختل کنیم و تمام نیروگاه‌های بزرگی را که ساخته‌اند، نابود کنیم.
🔴
هیچ پولی به ایران نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132066" target="_blank">📅 17:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132065">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af6138603.mp4?token=gthX2TyY3GkhnSr4GaK96WARHM-l2aATuTQni-9aEwatdppaYsCtWDAp-hWwelpd8p5_QI_BRt6CMjjkhOwt6B2FZcIR9j3WHTYvjJy-IQ7tYM8I_6kLD2L7ukWW5ShZykVUsrYbE6vJ2asC3y2zjq1Byw-gQZw4LTWhitT9kPbbRNMwD4LkurtHvjpCIqwQs0p73OSoNwSQCMDT-Io-S1L6ljCAp7xE7BKIbGTq3Os69UmDHzncvSgrGgeyxwJTGNQ5fMuQuY9g6NGFIowx-vA0Z-7Jq78k7i96B_OKpdOI2W4o4soMG95A1VoaxNEgaVye42R9c9xPHbsCcmoJskuX9gsoWLY5LSvrvQy7pSMhve0yYjVcFQ76w28XRsu12ndkhvln6sCXLWswPf7W49XQAU7I3Ehn59kXYiIlsCM7s91JNlHl0Dfv9L-Kknfz3fwXteZKD9HQf2_U_uOw0theHNwPpF8gF9K_JngAqz8dXafFNPtXdK2BMAQ8UkkdRo82yENOEwbmuH1fYYds79vy5VVwTuSjHJh6rQ9CK4tSuWg2TTopM4ADkusABjl61F_1RMJmmJ0O43kJa8JIAZ4GyKSJabAR2jqPXecAE8YpQ2YLmTn4eRf8naeWYmyQNZSsXQwBKyA2JN4pcUsmFVn1N5WrTVl6WGJJKf9LNcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af6138603.mp4?token=gthX2TyY3GkhnSr4GaK96WARHM-l2aATuTQni-9aEwatdppaYsCtWDAp-hWwelpd8p5_QI_BRt6CMjjkhOwt6B2FZcIR9j3WHTYvjJy-IQ7tYM8I_6kLD2L7ukWW5ShZykVUsrYbE6vJ2asC3y2zjq1Byw-gQZw4LTWhitT9kPbbRNMwD4LkurtHvjpCIqwQs0p73OSoNwSQCMDT-Io-S1L6ljCAp7xE7BKIbGTq3Os69UmDHzncvSgrGgeyxwJTGNQ5fMuQuY9g6NGFIowx-vA0Z-7Jq78k7i96B_OKpdOI2W4o4soMG95A1VoaxNEgaVye42R9c9xPHbsCcmoJskuX9gsoWLY5LSvrvQy7pSMhve0yYjVcFQ76w28XRsu12ndkhvln6sCXLWswPf7W49XQAU7I3Ehn59kXYiIlsCM7s91JNlHl0Dfv9L-Kknfz3fwXteZKD9HQf2_U_uOw0theHNwPpF8gF9K_JngAqz8dXafFNPtXdK2BMAQ8UkkdRo82yENOEwbmuH1fYYds79vy5VVwTuSjHJh6rQ9CK4tSuWg2TTopM4ADkusABjl61F_1RMJmmJ0O43kJa8JIAZ4GyKSJabAR2jqPXecAE8YpQ2YLmTn4eRf8naeWYmyQNZSsXQwBKyA2JN4pcUsmFVn1N5WrTVl6WGJJKf9LNcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ خطاب به مقامات تهران:
یا قرار می‌بندیم یا کار را تمام می‌کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم قرار ببندیم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم.
می‌توانیم تأمین انرژی‌شان را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی ندارند. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این را می‌دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132065" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132064">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری/ترامپ:
یا ایران توافق را امضا می‌کند یا ما ماموریت نظامی‌خود را کامل خواهیم کرد!
🔴
در عرض یک ساعت می‌توانیم پل‌ها و تاسیسات تولید انرژی و برق آنها را نابود کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132064" target="_blank">📅 17:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132063">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db3ddc151.mp4?token=N45-eU5l6W8hOwR0MU-CXUsjQElGdtKAMLtoOuH8VGlXWsr2vQdUJoG294BJgtQP_2gJbPOYk6BRP8J_thkHSUr-fWUd-X3ue2GD-KI2sZathdDY7Q5bV7NL9ukb77FYnSyatUJdaILJUfYzFffIXDzsdahYsLe8pHDHJgMpP-QwoTksLRaiPL0e3nzDRDXEiwwFfI73w40cInxO03XCAMKzhWb8QGsTixz9gfn5cp356MW837ZeFyyKO35FUWCFhslOplp0gEs_9FqAu1K0vui134l3eRv1ZR15KxdMfBCGQ25LEjJNdPKqnaQTbVlAZtkeCsTmgl4qFW80Z3xXGxswfhztQ5gBn9sR2i8LbwKDaGHGFC2j7svB2Lplft2Xjc4wrosIqLmD6ihboXXJhsvCMrhqSRY535D3f5KTZzB8K783d1arvExMQTtG41XBb5RN6GcrkJZymJA6Rh045Jqvhu4F-2Seau4GUTLEjGqJ4PRvrp_AJzvHJWL6RSqpbAvDuu__dcMXWHeRUEvGTCXzhWGdWXdBc1jQlGjlxkM-5LIB7EknMWBbVHaPeufqkXQhbTtyg6V7hnyC1Vc7EfLlUo7J6uv8OKhzs4JkhFg-RCS-SCkK5_weLxAM42B8K8qpACSsqISp1r6m2RL8o7jauk_hSjxvPMGqlPP9bE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db3ddc151.mp4?token=N45-eU5l6W8hOwR0MU-CXUsjQElGdtKAMLtoOuH8VGlXWsr2vQdUJoG294BJgtQP_2gJbPOYk6BRP8J_thkHSUr-fWUd-X3ue2GD-KI2sZathdDY7Q5bV7NL9ukb77FYnSyatUJdaILJUfYzFffIXDzsdahYsLe8pHDHJgMpP-QwoTksLRaiPL0e3nzDRDXEiwwFfI73w40cInxO03XCAMKzhWb8QGsTixz9gfn5cp356MW837ZeFyyKO35FUWCFhslOplp0gEs_9FqAu1K0vui134l3eRv1ZR15KxdMfBCGQ25LEjJNdPKqnaQTbVlAZtkeCsTmgl4qFW80Z3xXGxswfhztQ5gBn9sR2i8LbwKDaGHGFC2j7svB2Lplft2Xjc4wrosIqLmD6ihboXXJhsvCMrhqSRY535D3f5KTZzB8K783d1arvExMQTtG41XBb5RN6GcrkJZymJA6Rh045Jqvhu4F-2Seau4GUTLEjGqJ4PRvrp_AJzvHJWL6RSqpbAvDuu__dcMXWHeRUEvGTCXzhWGdWXdBc1jQlGjlxkM-5LIB7EknMWBbVHaPeufqkXQhbTtyg6V7hnyC1Vc7EfLlUo7J6uv8OKhzs4JkhFg-RCS-SCkK5_weLxAM42B8K8qpACSsqISp1r6m2RL8o7jauk_hSjxvPMGqlPP9bE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132063" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132062">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
مراسم تشییع در تهران تمام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/132062" target="_blank">📅 17:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132061">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7WQapwXgmQ98ZWj-t-peg7Fp3k6AiwA3AfI6JKpL6p6bpvoXvWkT9gKy2NkWA-p2di3XYDbGF4lSnR-6ARcH1EQzlk3933krCzy9VxsR3EVNtu04XuBupDyhttS9KcsSjGqWwn_kyL3QzhSiGOmwC3tNgcAhiuqBNX_GBGCQ-u1GPBzpUSTVDjPk4xnWx26YHxnTjZM0ieRXMiDheTejl_OJj0GW51flC2MSu3EH33qMi1gMsfHWKFzMnqlcLwqCWAHyn1nTeXeiGnRA7MATCBYOLU2PiF1S8-rFcbW_RBwcejNpiSKtnJkINCChUkxXqh609mCt0eqsR87tyMs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخلاف گفته‌ها، آیت الله سیستانی مرجع اعظم و اعلم شیعیان جهان نماز میت در کربلا بر پیکر آیت الله خامنه‌ای را نخواهد خواند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132061" target="_blank">📅 17:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132060">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/132060" target="_blank">📅 17:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132059">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBV3QIEtSN28twlOssCBtfnETqvoBJHaN0m4IutQi-SaCA_bKwbyYT6FqhWV6_HTmQJrgCvygcLuzkraGE3X2YyYk2XeocEDH3Qm26eU4EanCrfswKPIIUgMxvSTRL8sRapyejKhN8VudKGzA7KcT14Zi8CG9-DaemYD7G9gzCduwUN0KPItISeln5i4mNNeH38pzMfjU5ndO-KXu6tzL20vZl4QOxhfgL6Phgw0zu5Qq0pqs8oN9Znih-UINtr7zcsU6s0oLTgHLvmQXx3OZF5RsZ2KMawOJk55QSIQrqdE0Zn5ENLb4T6Sr_0sJIZnMxAyxV54ntB2xvgo6IdZng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132059" target="_blank">📅 17:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132058">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7Foo6uIiyM9SzmmvTXgC3xqSds9OxgVcrbAkmij9MOgQmd8L6jr0xSx4bTys5cYXK1Ox8FgqCJ67gq3vSKzvnZpCquRQgcCNQU6NROYbrVnOH2yUIhuGacmYyBvqFx2o3MBpRO0cAWacmFgzar1NE80Qwi_D6hufXN6kS6SCtmmNZSnx5NroPCkRvMo6sIkHhH54MXl-tmKt4Vg8NZTYmyUDasy1hcmzJDE2b1SBLUbbJdcB5d2_oxMFXcF8eJsdmID58QFVCWlOyMOfKUZqAwk7PKg7cglegPD5dD4R9OEB8ryLrQDrIz3j5yRetbuys39u5M8t6Dk5df5UNHqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تو مراسم امروز 30میلیون نفر اومدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/132058" target="_blank">📅 17:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132057">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رییس کمیسیون انرژی مجلس: در تابستان قطعا قطعی برق نخواهیم داشت و در زمستان هم احتمالا قطعی گاز و برق نداری
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132057" target="_blank">📅 16:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132056">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اکسیوس: ونس را باید جانشین نهایی ترامپ دانست
🔴
اکسیوس در گزارشی نوشت: ونس در این تابستان کتابی پر فروش منتشر کرده، همچنین به پیش‌برد یک توافق صلح موقت با ایران کمک کرده، بعلاوه یک تور رسانه‌ای گسترده به راه انداخته و توانسته نظر مردی را که در دفتر بیضی نشسته، جلب کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132056" target="_blank">📅 16:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7468_AOa1jQfEAUd4h2t858prGVmYst0QxrK5hVwiNT_ZaVxU5B7KGP6m9uiK7x-dwhgaYYIRFoJxTgNn4mes2yoWW8vitMmIY3WuONs6AWsZK7AqvXLNSd8bt57r10QjC0IH93P_7t-ui0DVkO9U1bNzNFTJ8oZgfknjlx5ubJy1YAj8pz-F60Zore3B7Wqv17SErplHymnMY1HyNTCkXBbS-umQn9vqcRaVZxHj37UzOMZucckePaDOLZvDHPBhu1g_niX3O1BBsnhOrnJJyYOdNEiGGK_KLPlarJEI-Kl1aPHxIy3O3zut26uGGxfLFnHRhC_u1j3QqjcHCA8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZilkJDJHkGWegQ1gj9kTFVjn-ckfZfdwv7DpDkoi4RmF8tT1cH8EHABZUAzEYEV7EZ1jYtbqp-12iM8R1BWIKzMI4s--BR1qK2y8deHZYq9WhAq7JQfjmMnuQzbS6b21rJrRnBOJKkxkKxOyXBDvVZx9RyMpsYV9CFiFSjcT8SZ4J3Vs5LieT7nHLvHlumujtDfh1-hn92Aq5DzMI8WL34HSYxGrrOzng42rGC_z_Ewm84Y7lLnUqh-Pyd5dbLYXGXwwIl0XeeR8mLKflnuphDY9K4JS01yTt-DyMOJmphJ2BIx96wZoc9umHg41ZFwYtxCnBW6etyeITT7kK20NxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
طی اتفاقی جالب تاکنون دو مرجع عالیقدر شیعه یعنی آیت الله العظیمی شیرازی و خراسانی تسلیتی نگفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132054" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwaPI0Le4zCavYA2XVQ_Y23DtlsO2GGYnx5-xaDXQojSUaMI-oXzQs9GyN8FUoUR5-OyXwNl1jxdQo_mqykQPMLdxHYGydO-xxapLC5nias7jB-x0ezPxQqleplUvutvIsKZ0A1lKrxRlAAxaUiIak22RhpQxibKVj2x55nA28SBO3E42_r1QGa3MsGZQ-Ofjue7RbccOTzjm7B73HwruoO73EoL7CllrXRL94ReqEPlISOK8UmdJwXeVMtrvPYWJvvjIbQ7oszGa03ckaa6Hp41K17_sIlAwPU21uAMUcTawgjimL1ngP468VjCsZ8XN9H0KlSVLFUMOK-nsXVK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از صبح امروز یک تصویر از راه دور منتشر شده بود و صفحات حکومتی میگفتن آقا مجتبی نامحسوس اومده، الله اکبر
🔴
درحالی که این شخص واعظ موسوی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132053" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نتانیاهو :
آمریکا نباید به ترکیه اف‌۳۵ یا موتور جنگنده بده
- چون اون‌وقت برتری هوایی اسرائیل از بین میره و توازن قدرت منطقه به ضرر ما عوض میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132052" target="_blank">📅 16:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
مجری :
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره
- که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/132051" target="_blank">📅 16:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a8198c42e.mp4?token=tjde4M8hk3BxNAVA9ijIym5TtfGSvESB9iTAofV9tDmIjyBP81wXsEPvTb5HkusTUd0zcnTlezJ3MyTB6fOa1IqKQOuxvwK2bPOp2Uix3GsIfLm6V5lyTaY2TcEo7W6VkZ_r54eZS-Lo4zNncjM-tAipLDp0gHQeDnK5dJqDbbrWGgMr85NtwTuqIfbuKeXhyG1FjzbXxpOje0PGm5OW6FLF6M6B7v7iStbtpPNiEgCxGstcMfXVL24OgRoHfPzTwsrdyIhhd9S9XnsbMuSGWVP9n4qTLbenLEJw1vgJMd9IlzV_DDB9s1ZzkqM7qUltT7NMj2JHC5Ndpp9yW_Z1jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a8198c42e.mp4?token=tjde4M8hk3BxNAVA9ijIym5TtfGSvESB9iTAofV9tDmIjyBP81wXsEPvTb5HkusTUd0zcnTlezJ3MyTB6fOa1IqKQOuxvwK2bPOp2Uix3GsIfLm6V5lyTaY2TcEo7W6VkZ_r54eZS-Lo4zNncjM-tAipLDp0gHQeDnK5dJqDbbrWGgMr85NtwTuqIfbuKeXhyG1FjzbXxpOje0PGm5OW6FLF6M6B7v7iStbtpPNiEgCxGstcMfXVL24OgRoHfPzTwsrdyIhhd9S9XnsbMuSGWVP9n4qTLbenLEJw1vgJMd9IlzV_DDB9s1ZzkqM7qUltT7NMj2JHC5Ndpp9yW_Z1jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/132050" target="_blank">📅 16:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
طبق گزارش‌ها تاکنون یک مورد هم حمله تروریست‌ها در مراسم امروز رخ نداده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132049" target="_blank">📅 16:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132048">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلومبرگ: دو نفتکش سعودی برای نخستین بار از ماه فوریه، در مسیر آمریکا قرار دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132048" target="_blank">📅 16:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132047">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2tRWCIyDXY02nsUmsRD_5hOG09PUf7rcrmWWietuB6LKpa0rpJh2TLNtgSS8-qzRb4c7CsAdAiYPIGXnvntjusMjRvYp0IGymh-1_wkGljqdH8G98lTS6Awl_76GNlQ02snOVDblTwhT_sC3PW1JXHd4vVWbnVfoFG2OT_r_edr7twLGnFNLCJ8IPnqax2ZosoOHMAT_HGiTCpSSIl73lxVh-0jwdyVUzqIUhj_0A5rxEbHRmabSc5vJ7hGVRt9YhNvfVPRb7RJsJnk009RKXyl3tP4OmiV3BiW4U7WfhXABa3HanIwW2xFSwsuM-4oZP1CqA94JXahYHC188HSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو شروع فصل جدید سریال silo ، همون قسمت اول آمریکا با تاماهاوک و f35 به ایران حمله میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132047" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132046">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXqbyHGTS5YiggzFXl3BuxO6-4Oo8D5P9a1gx_6d9ZkWXQ-EDGyY2R_bFO36r21FM_SO3cw--JfVgIKKCUpQ-cBSB4Q0rgkQUc7h-BxrwEA1F65OBtSn2TAVV9Pf6Y6hqavB2sc6myuoa9c_T6UYHN132zR4V1OUlOeRDJv6rxKhYGOY27i9h0S4Ao7-6ATEC5N92XJU2r71EF6toIEoFXaq4ERKaEocyIG9lPhUobMidcVRHkQoUDaIsT7qpKiO3F-RNEhFpmDvhwAmFD1OCP7YPxgEsXXIVEhyL5KXFwLLC3hqjCzYtHJin4f68iQ11xb2mutZOb5xHgX4UXv1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنجال مجدد در استادیوم‌ها
‼️
🚨
ویدیو دیگری از هواداران زن آرژانتینی منتشر شده که مجدد لخت شدن
فیفا هنوز واکنشی نداشته!
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132046" target="_blank">📅 15:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/wBnld2Vq2ITDCAURniDe0cTyPYplQeb0l09VZ8oDkJC2O6VavtAn5JT4SOGI2Ii6KFsMi0jFtbSC1iR4S4MJxo4Yj6_0wO4lGhKGoR8W96QbkmJUcO_iUrS5rLIhsA60USISMc6dZKSWk0bVHnWvAzXBpVKGsFtWOzw-Vyeq7J3mppjgTqpRXxxtwpj3_Ojf7hiPhcjqprm3s1nH3LEmw05fLDF6hCL2jY0BYoEi8loQ3sjOiiZyP7FjpyaKoCT9mXM9rGaXAv2p04UMejwpb-zIac6o5CIMp6htNH3TJCDg58eimNWD-TjoGD_MaTI1GlDi5bylQwF-KwwN6A1BNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dyg7wt2cBZSEH_4oNrNazZvnkEB9WMoid2bUL4_pg8RujjNsddTYIrTGaGqWq8lisqgM9TQbYhDqOJoouIWh8FaOCOLAWwkiyLiq_ttUCzRLWNWjQDZNqBtPTfhj13KKSODqiZ0R4K-5jfOLNly_W2JlyyW12pLpDslwMEPY3DHtz4pMccj9zFwoZwrOayitXuAAOB2HPfwh-VXEYfQ3lTaYkFc0iRGnIy4W5oN3l_FSwWyes2yI5pndMRgQg5LPdJ1GyPOaPQgP8wvsEetJvmermy3Haduy28EQB58vY3OGHTqWTOfpMeog9XXIUE5AFQG8_e86_7zV0mX2uLO6QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله پهپادی اوکراین به پالایشگاه اومسک روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132044" target="_blank">📅 15:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سازمان پخش اسرائیل: استعفای ظاهری دولت حماس چیزی جز یک فریب نیست
🔴
مقام ارشد اسرائیلی: حماس بیم آن دارد که اعلام شود این خود است که توافق را نقض می‌کند، به همین دلیل وقت‌کشی می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132043" target="_blank">📅 15:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نتانیاهو: آمریکا نباید به ترکیه اف-۳۵ بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132042" target="_blank">📅 15:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نتانیاهو : از آمریکا تشکر میکنم
🔴
نیرو‌های قویِ داره اگه آمریکا نبود دموکراسی وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132041" target="_blank">📅 15:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تایمز آو ایندیا: آمریکا مانع از حضور ۱۳ کشور در مراسم تشییع پیکر رهبر شهید ایران شد. حداقل ۱۳ کشور از جمله سه کشور از اروپای شرقی، پنج کشور از آفریقا، دو کشور عربی حوزه خلیج فارس و دو کشور بزرگ شرق آسیا یا از این مراسم انصراف یا سطح نمایندگی خود را در پی فشار ایالات متحده کاهش داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132040" target="_blank">📅 15:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
به گزارش اکونومیست، شارلوت هاوارد، سردبیر بخش آمریکا، نوشت میراث دونالد ترامپ هنوز در حال آشکار شدن است و شاید در نهایت او بیش از هر چیز به‌خاطر کسب ثروت از جایگاه ریاست‌جمهوری شناخته شود؛ منصبی که تنها ۴۵ نفر در تاریخ آمریکا آن را در اختیار داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132039" target="_blank">📅 15:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فردا سه‌شنبه شهرستان‌های کاشان و آران و بیدگل تعطیل رسمی اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132038" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132037">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQsdEhbOQQZapaJIZZqbNBcfwjQm_9YczP-8LVdtQm4FmTe803eHmh0VIM6Vuth3Kh4oJbI0aJ-eYuIo9eiWA-kGFlGpA8IJW5vMQHyDvzCcbKM5DZCLZIMHUnAekZbhpYy6R0n2_UHJkLpx5cDq8P0_rUZkEBwxxPPUE1P8G7bS9P9KG0F4k98Ovdk0bcYq7OMsoeUA3s-Emf26lhBdddv9QJH0RT4-c8bWrPAXd9wFCmZeWfIw3a5_gBCJxrk3nunCoN41zuXqGTeDVSzhxCKy_jat3pxUW5jWBks9fO1d1Des0Ctb3c0XSUObBZvGvFDPHPR5rzl3kwuEHDyJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی واسه نتانیاهو و ترامپ ترامپ ۱۰۰ قطعه زمین ۲ هزار متری جایزه گذاشته،آیدیشم گذاشته کارو انجام دادید پیام بدید !
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132037" target="_blank">📅 15:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VXHo61t5sra0xJxGl8pGGpJtaei3K3fFpkW_Z2m7L-UE9GEeGPABMlMC6zajVckuVaVGom9XwEXcK84octUsn-a40RbFVRjomesLUMccYEnHDKeRminNO-_b8YUpe8uzijZNoUB-FNL1k3e8x34CbbYrjrM_go3BBCKD7LRTogZ-vx0jtJXp-2684rGu-mRi_IyKn5MubqY_SNiHmlvMCyvfrlncTnum_9HIMJJA8YEDKdNnuZ6O_c1HuMUUeQFHLYJDgiBiRcXrnea2RDZGPDxZSSn47kExLl1n8AU25EGGSsS8kVQqTgW1_AFakc98GsllXpexNaTI6ZpF7ibPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵۰۰ کیلو طلا، جایزه برای کشتن ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132036" target="_blank">📅 15:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132035">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
بریتانیا تحریم‌های جدیدی را در ارتباط با روسیه اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132035" target="_blank">📅 15:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132034">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
به گزارش کلش‌ریپورت، معاون رئیس مجلس لهستان گفته است این کشور به‌طور محرمانه موشک‌های رهگیر پاتریوت ساخت آمریکا را به اوکراین منتقل کرده، در حالی که همزمان به‌صورت علنی درخواست‌های واشنگتن برای ارسال دوباره این موشک‌ها در جریان جنگ ایران را رد کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132034" target="_blank">📅 15:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132033">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ادعای عبدالرضا داوری: ۲۴ میلیون نفر در مراسم وداع و تشییع رهبر شرکت کردن و رکورد تمام تاریخ رو شکست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/132033" target="_blank">📅 14:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132032">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
استانداری هرمزگان: تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی استان هرمزگان در روز سه‌شنبه تعطیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132032" target="_blank">📅 14:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132031">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132031" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132030">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بلومبرگ: اتحادیه اروپا در پی ایجاد ابرنهاد سیاست خارجی است
🔴
خبرگزاری بلومبرگ گزارش داد که اتحادیه اروپا در حال بررسی طرحی برای ادغام چندین واحد و اداره در قالب یک بخش متمرکز امور خارجی است؛ اقدامی که در صورت اجرا، می‌تواند توازن قدرت در سیاست خارجی اتحادیه اروپا را دستخوش تغییر کند.
🔴
به گزارش بلومبرگ به نقل از یک منبع آگاه در بروکسل، «ابرنهاد» جدید امور خارجی ممکن است به‌طور کامل یا جزئی وظایف اداره تجارت اتحادیه اروپا و همچنین اداره خاورمیانه، شمال آفریقا و خلیج فارس را که مسئول سیاست‌گذاری در این مناطق است، در خود ادغام کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132030" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132029">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
قوه قضائیه عراق: 25 میلیارد دینار دیگر در پرونده پالایشگاه‌های نفت کشف و ضبط شد. همچنین یک میلیون دلار و 5 کیلوگرم طلا در پرونده عدنان الجمیلی از منزل وی در تکریت کشف شد. مجموع اموال کشف‌شده تاکنون به 127 میلیارد دینار و 24 میلیون دلار رسیده و تحقیقات و پیگرد متهمان این پرونده همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132029" target="_blank">📅 14:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132028">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2684c5fbb4.mp4?token=gQrq_mzAmJ6uC6obakLFMPkuA7QDG5VDtjm3Cj8lNIcQiw9AIyHe8gBSe7iBrt1GCeP3or23kAbpHxCCu36u4w1jC-Jyaya9wEriCaiMRpT6eUi6C2r6qDAveohSTj4J1ePv-RD7_QrO5hTXFZ77jugbJ1jURrMFvqy-DKsvK1JJQiOv_mJB0aXOajvBmM-uSgN6n9vkukcTIsqhmZLry3p6JsIeasUL0MweMbIfCeJontmrHU8da753gtUW6rJi42gHTda8UOZhgqN3RUSdtkm3784AR_S4r3bQ-vIzC0RDCa9cFC_NrfFunY7J6_FKIQZ9qAk2uLXL0g90RDWUck0OnZNLg3q5rTzhMVGGpSF7fpQ2-LfEgAzKs0Hnreecy78Y5FT65RPmGIZHD7KMNeOfuQmXs5JozROAe32xnEGK6cAEU4I8CJ9egZ5P9iq15hkuoPAJV-huTq5bvxRmQwlNRhmy85OqhBoHsZ52O91hDBsE8ZIIfxz7Rkf6-QxALfG-NoAqO0kyEcKiMjBF6MEfXTx_lgKgf_aDlzrkzVHhpX9C2mT8lBmQBv9UyL3zHS_os4ve5cZ4gKK_fk0iEBdxaMt1vOkXQUuiJMTDfLuzmCid5BrZAxzoHWoK3KDhf4DQJxgCUfH9IPvEMsa8BddmuJlF8ke9uInDHN39mro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2684c5fbb4.mp4?token=gQrq_mzAmJ6uC6obakLFMPkuA7QDG5VDtjm3Cj8lNIcQiw9AIyHe8gBSe7iBrt1GCeP3or23kAbpHxCCu36u4w1jC-Jyaya9wEriCaiMRpT6eUi6C2r6qDAveohSTj4J1ePv-RD7_QrO5hTXFZ77jugbJ1jURrMFvqy-DKsvK1JJQiOv_mJB0aXOajvBmM-uSgN6n9vkukcTIsqhmZLry3p6JsIeasUL0MweMbIfCeJontmrHU8da753gtUW6rJi42gHTda8UOZhgqN3RUSdtkm3784AR_S4r3bQ-vIzC0RDCa9cFC_NrfFunY7J6_FKIQZ9qAk2uLXL0g90RDWUck0OnZNLg3q5rTzhMVGGpSF7fpQ2-LfEgAzKs0Hnreecy78Y5FT65RPmGIZHD7KMNeOfuQmXs5JozROAe32xnEGK6cAEU4I8CJ9egZ5P9iq15hkuoPAJV-huTq5bvxRmQwlNRhmy85OqhBoHsZ52O91hDBsE8ZIIfxz7Rkf6-QxALfG-NoAqO0kyEcKiMjBF6MEfXTx_lgKgf_aDlzrkzVHhpX9C2mT8lBmQBv9UyL3zHS_os4ve5cZ4gKK_fk0iEBdxaMt1vOkXQUuiJMTDfLuzmCid5BrZAxzoHWoK3KDhf4DQJxgCUfH9IPvEMsa8BddmuJlF8ke9uInDHN39mro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری وایرال شده از برخورد موشک های هایپرسونیک روسیه به کی‌یف در حملات دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132028" target="_blank">📅 14:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132027">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
روزنامهٔ «پاکستان آبزرور» از احتمال برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132027" target="_blank">📅 14:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132026">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ویدیو هوایی از جمِعیتی که برای مراسم تشییع علی خامنه‌ای اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/132026" target="_blank">📅 14:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بانک مرکزی: اختلال جدیدی در خدمات بانکی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132025" target="_blank">📅 14:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فرمانده سنتکام، کوپر، این هفته به "بیروت" سفر میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132024" target="_blank">📅 13:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132023">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwU9hHpL_BxklPsTWWayvPvPQZ0Pb_FZ--AdU93zw_RvXGtxhniWai4LN8N0lL2NmqueUYadnvRBVHsFXj67_tg067CeV2fJFqR3qLEBgPsP9EBnkd6i_dCd-zJJSs3zy1XX3B6WZAo7meym7ZZEAd9QNmpfFo5ITh5y8V9sRXf1HZBJnYjzNxrojREHxuRm67o8S__ckTVf56ZWKw1Ukfz11qxN-hngSGqLQQmqR27LN8aovIR3OHVdZMwKR-PWGT4lFjrdcAS21h-n8uwyk0JXLIhExDV_byFTFRwGOvBQTtEBtcxNlVmGxFQUUEJRnM7wlb1KORmdVl6GybvhkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
🔴
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
🔴
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
🔴
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132023" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132022">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کرملین : قراره پوتین با ترامپ تماس بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132022" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132021">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjReynawZ7m3N7PaOy2voH3s4tyHVsf3RJVhvauErhHbwlHdQudFJf3MVPRWLdCzL3bQLakrYzllCQALMeNnEBRzcNrFt2kzDvUNiyLUlPQKhfedB5gQfdpgBhRcGbbvKtUvCuuw_jGGea8nILghH_ZBf1MJ75ZH5FlPnhCi5DGThJaSQuBt5SyZbR34na4k3EVa3PZsvFgKJxtYkMp4RtddCyTzbdBdadOZ_vh_P981WMIMnXcVXDw-gfCuhsjU3az46HRFmRzAybYosZ2h8s9JzGNaSnNtKS4jPGFflq-MX_PBkIbEduzolV4iUoWz_0tbfhqdQgH7Fh75u412hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور سید عباس عراقچی وزیر امور خارجه در مراسم تشییع
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/132021" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132020">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiTVYTGx4fYrWE-sEk7QmkFpms3bciBrBRf6pCshR_QhC6NqhuqLZWnt3XaA5WjiEz6JrkCwd6JIrSrQ4uEmsAzS-G4EnbYsJ9fo1Wmn2Z16GLSAqOOIUQftlA12b-8O8Vc8cX_ZCTpIS6ValO8zmne6pv3ko76Vwmnii-V3XW6OEkznzGwkFZxCeVuTFAg492ChVLQY-6g8D2WEetw6e3pttuY61_Xp9tHgeYvNKXQRoDfJjDKEH1pDsNcqeQ_g4g9XhL_onD-gMrhrDlr2StZq5HpR4iWdoPrkakj96rGTsJTUGYmQ8OHCgDk6FEvxyRhxXlNXl_Z4Hg188zSGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک بنر در مراسم : دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/132020" target="_blank">📅 13:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132019">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نتانیاهو : اورشلیم پایتخت متحد ماست
🔴
هیچ‌وقتم قرار نیست دوباره بین کسی تقسیم بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132019" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132018">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کره‌جنوبی: ایران در مراسم وداع رهبرش از ما دعوت کرد اما بعدا دعوتش را پس گرفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132018" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132017">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgczHDnIIL-hoPZC0q5vibpSxFe0vG5YAP2Z8DmAIdnPOaMSvIll43q2duK16MaXo1tpCLyanoJrriHqjN-AvjJSG3SPQ1MY7AeQ4y2cmSGXKkGFrIKJCtgiS-EDTH2Uxvff7KfnXXkuC5_HXqID7gWHo9DTM6ctuZVAG1VsOoKWyoc8Merz7xqQu-yDFuv3tX0RAmPwKPUJsAVVL3KgPTY-M_MqQIGDky1OCEAWQTG_EotyeSfjtRw-8aGr00bwkZkN3eBkiT2F_TguLeIPLtdFyKj88PjofFnz9kdL71Q3sFvlrcijTb5Y1qx2gZeWuyp9SEx-gNOgyY3qcDZO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان، نبطیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132017" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132016">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر  فردا در مراسم تشییع عراق شرکت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132016" target="_blank">📅 13:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132015">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc3c73d84.mp4?token=HQqsXCbERtilbICzEBBnEJt9R3BArqKWpnUin-xvKgQNgHLS3h6lQ2UFjTS5lkz02bD6YeUPAOM2vAabm3-dvtB0BKAK5an1zRjdikinYEKZYVRrYuQYVvRsTeFZ7u6J_9XGkwcoqYoyuXrvRDJjUzAixQi-J_ocOTThvyZo1V1Bp9-jJB62ZxBSL_zuVFhTAgfEtZ8fFxd2TfCKAmghC8tmeQ26VszmfvoUKjhoieVbSE6Ut9oHbLvGnjFsLgKioU9DtNG9dLLWZX0Df927NawlO-iULWe-9EKSO_NXVpQ6zMB2NvuLpEtP7HeO9MSfPwu2bdspn6lDC8QW0uH7Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc3c73d84.mp4?token=HQqsXCbERtilbICzEBBnEJt9R3BArqKWpnUin-xvKgQNgHLS3h6lQ2UFjTS5lkz02bD6YeUPAOM2vAabm3-dvtB0BKAK5an1zRjdikinYEKZYVRrYuQYVvRsTeFZ7u6J_9XGkwcoqYoyuXrvRDJjUzAixQi-J_ocOTThvyZo1V1Bp9-jJB62ZxBSL_zuVFhTAgfEtZ8fFxd2TfCKAmghC8tmeQ26VszmfvoUKjhoieVbSE6Ut9oHbLvGnjFsLgKioU9DtNG9dLLWZX0Df927NawlO-iULWe-9EKSO_NXVpQ6zMB2NvuLpEtP7HeO9MSfPwu2bdspn6lDC8QW0uH7Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132015" target="_blank">📅 13:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132014">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCKwoVMqKLv7VNL21124y-h-DvML64VNBaF4IjaeSw31YPkul68JEHeDCVYu30nXLOcl7J76EmgNQuU51IvXB7QL-nrequxJOaLfAt6kBDNxLZSu3sjDhnWKp3t6vyOvu2MGeIgApEyAMd5__GofcCvH0kqoiFaBIK9Hr2P7gc8V6dcTbusuomSdl4NQ-VweMS6_FA-FvGH8MYjLTd7okiRK5sKCJaTCEHg2vsJzszbIy6zVVgnUu6tD79_3olQMYdhcW8GKcBWtjOxrzGRQTvTK8oiUXydH7Ezb39Ul7taO6A-uX6KvePKbOvi8JXxAvFIDF4eBXN5bCZMbjsgxhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در شهر بنت‌جبیل جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132014" target="_blank">📅 13:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132013">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات زیر :
🤖
@Team_express_bot</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132013" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132012">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
سرویس های V2ray  Team Express
✔️
اتصال پایدار و پرسرعت
✔️
دارای ساب برای اطلاع لحظه ای از باقیمانده
✔️
متصل در تمامی دستگاه ها و اینترنت ها
✔️
مناسب استریم، بازی و استفاده روزمره
✔️
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
🤖
ربات خرید
@Team_express_bot
✅️
📞
پشتیبانی
@Expressuport
✅️
📢
کانال اطلاع‌رسانی
@Vpn_express_sup
✅️
😍
رضایت مشتریان
@vpn_express_supp
✅️
🌱
سپاس از اعتماد شما</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132012" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132011">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مترو تهران: به‌ اطلاع شهروندان و مسافران گرامی می‌رساند، تمامی ایستگاه‌های مترو تهران و حومه در حال حاضر فعال و پذیرای مسافران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132011" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132010">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWpAMVFxcDr1FBhndy_8EuBt_Vdq8GXttewUX7OGZYU6NYCMT_3-wwP0W3Pj_eHuHwRquv1gq40hT8I5DQ6eFsnPMpBtXgfKvtoOsJSKCyW2lj8bP_Twp3XkonnhSJphEO_XXB74h65-R_VQ_fU4n7u7RTeqkl_YQpuaIkkiVboNTlGLfJ8fNRw8dHiJ5rVkxSi7LGC5jPYOGvUvAwr5UtHx3cDgCTtnEWuFBR2Zajljijvbh8N37IycKNj0Y1X8luPXRZrYWJ-BgWLCOYijHrkrlyelU55CTh8cNzaEfu2UrRAvg0hLmarRDsCUUBlJTASn2XhjSaJGsNa2gEGQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای تأییدنشده نجاح محمدعلی، خبرنگار : امروز  سید مجتبی خامنه‌ای نیز در میان تشییع‌کنندگان حضور داشته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/132010" target="_blank">📅 12:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132009">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده/اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/132009" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132008">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مجری فاکس: جناب رئیس جمهور به نظرتون کی قهرمان میشه؟
🔴
ترامپ: ایران نباید سلاح هسته‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132008" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132007">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWvx1ztnUbfTgg98j_d53DnuTroRHKdL2tP-CmDosM14o1w5zTAnPc306CZWwE2wWeqXVAmWQsbxwFc2OWmt_TDpX_3gm37NLii1yVzJzG9js0eRNFWmzL_i8jzP3wtJu95AspAgykPEBkuV3VSuUi4M51gwykJRQdmZHQT6I_cdNsLM5AcAFa7_Wt2QeoC7KWBXVxpM8D-fLaq2mj03cjzvGRmeiOMxMfFPS_HZYtg6pS-dxeaG5O2rqzJ8AEup3bT6QZ3N5Q9zvi6QrjtAWLy_N67b_3BGL47lX9Yni4P2GWNCV29skV1iyVY5scKkuNx3C3tjeotuefibi5UH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : هری کین یک بازیکن عالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132007" target="_blank">📅 12:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132006">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd089597a.mp4?token=THL62kH_KoLduHghfBkPK6Zi_jw2p9b0Unit8T5t80ycjgTekb8qc2wA-DHsYEx7qc_p0uk6NxIijHIzysAhqtJ8aTY8uPzQlEt9_p5V8bvKIUS26cQpYti5w_RiW8toiHlR4b-FctDNSWHShw3LZGHy8-FGq7TseQdNYcIZ_ka30PB9blBLpdL2eaIaCcn3mVWJ1ayL6Tgks5c6MTg_3A_zi0S0HiaPwSXCk1zO_RejizV2ArQSSVSPtxj9cKXGzl-sr2f6mdyvHiXOjcJd2xIVfTAxYoUaSPWZlsIvXcHJRTsqtC29ZNB02prkYFvkTyfEm7eCnLV9Wdrwl_beMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd089597a.mp4?token=THL62kH_KoLduHghfBkPK6Zi_jw2p9b0Unit8T5t80ycjgTekb8qc2wA-DHsYEx7qc_p0uk6NxIijHIzysAhqtJ8aTY8uPzQlEt9_p5V8bvKIUS26cQpYti5w_RiW8toiHlR4b-FctDNSWHShw3LZGHy8-FGq7TseQdNYcIZ_ka30PB9blBLpdL2eaIaCcn3mVWJ1ayL6Tgks5c6MTg_3A_zi0S0HiaPwSXCk1zO_RejizV2ArQSSVSPtxj9cKXGzl-sr2f6mdyvHiXOjcJd2xIVfTAxYoUaSPWZlsIvXcHJRTsqtC29ZNB02prkYFvkTyfEm7eCnLV9Wdrwl_beMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک ترور هدفمند در غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/132006" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132005">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ارتش اسرائیل: طی ماه گذشته 20 فرد مسلح را در جنوب لبنان کشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/132005" target="_blank">📅 12:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132004">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/شرق‌الاوسط: حماس قصد دارد طی روزهای آینده انحلال دولت خود را اعلام کند و حکومت غزه را به شورای صلح ترامپ بسپارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132004" target="_blank">📅 12:08 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
