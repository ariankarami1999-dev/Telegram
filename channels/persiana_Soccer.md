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
<img src="https://cdn4.telesco.pe/file/Gw25KyPZv88yv60EfisI_Cju4JAkyVEcxIG2jfX9ziq_Q0WxvUJhLUvuLt4de37kzDhK6hxSDnx67IurxE_rE-sGSRe6g4NoyQ9NiQrf-qtBxllpCWLCwcusaxKOkqkqjrdLqZC6VdS9hRcwWOLePGAoDLR9EEy487QA0BxoHhhJvUP6jpQMHWjEtvTeGGEkyWyXMpE9sy4SrVYml3D9YkGR-AQxIkTqcjtHp_H3aSbM4lQzmqerE4maELtamiCFR8LqbjX1uMoLgEwSjX-9Z5q_9Cx1LsPfkfOWBbM4y7hNfIualOh2rwBiMKjdopu3EA5FqLdN4atFelsb6XALLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 540K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-29460">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=Wv41oS7biCWKXVnwpBfS2tVEOZjHCFCUzIStzRiczseA9K-w9gpLzR2VG5LBnIaaDalUjJX70urQrOKZERJbaosqsH0sZUl49xLxOheVkJinSDAWQanSbgrej2uZqjq4npHp13bEU0Zz9JHwbEbECjWH7LypJJyGyIQz47JN3GP3xCgGfuQ9Y8WIM592T60Gu47Bs5uVccVb81uq8-OXZLgLobiFKZTMkxPi3pOvm21YPnlAw5oTrAhdc6VuwDJXmvP8tA6-z1TCfVuHDfsoxNRJKA_svhRGApNol0dOp31NN4rRPMPl0UYhwDrwPg_OWzAGhkjU8LXpch02KMPInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=Wv41oS7biCWKXVnwpBfS2tVEOZjHCFCUzIStzRiczseA9K-w9gpLzR2VG5LBnIaaDalUjJX70urQrOKZERJbaosqsH0sZUl49xLxOheVkJinSDAWQanSbgrej2uZqjq4npHp13bEU0Zz9JHwbEbECjWH7LypJJyGyIQz47JN3GP3xCgGfuQ9Y8WIM592T60Gu47Bs5uVccVb81uq8-OXZLgLobiFKZTMkxPi3pOvm21YPnlAw5oTrAhdc6VuwDJXmvP8tA6-z1TCfVuHDfsoxNRJKA_svhRGApNol0dOp31NN4rRPMPl0UYhwDrwPg_OWzAGhkjU8LXpch02KMPInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/29460" target="_blank">📅 18:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29459">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=Y9RFJU97XDfS5IF75ym474naB2delqGpP-wd-KsFHn0OVUGguJ8G9L1sNrQ2FsBRbe6nQnZFhegy0kGERXgTIXF37cHZ2PwGCqOywZiiuISqh6akyS-XqIlS3d0H6ONTngObc_Dl_BYDR8A6Q6g1LVAwNAwp--JJqV13oEwdMYjYd5pPHS6sSE9oVXf3jGJVbu6GtU9XdHLMLGmszna8vQ8nhkhBjEoJ-H-ODo9DZMjfGfmKUyUi6fTL1Icd0OPNrVMEKLg5dRkGzY-sIxXM3YRladsctlTNnp-y333GYBUP6DnT83kXEFH8SzCqJ1eM6E_OzVuVvHSKjk0y0uvUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=Y9RFJU97XDfS5IF75ym474naB2delqGpP-wd-KsFHn0OVUGguJ8G9L1sNrQ2FsBRbe6nQnZFhegy0kGERXgTIXF37cHZ2PwGCqOywZiiuISqh6akyS-XqIlS3d0H6ONTngObc_Dl_BYDR8A6Q6g1LVAwNAwp--JJqV13oEwdMYjYd5pPHS6sSE9oVXf3jGJVbu6GtU9XdHLMLGmszna8vQ8nhkhBjEoJ-H-ODo9DZMjfGfmKUyUi6fTL1Icd0OPNrVMEKLg5dRkGzY-sIxXM3YRladsctlTNnp-y333GYBUP6DnT83kXEFH8SzCqJ1eM6E_OzVuVvHSKjk0y0uvUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/29459" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29458">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyim_HRDvOwLK91CB96KFvgzFHycQGl_5qqFiUox540zhf_RgEzkNX2JDno4LAvAi_aCpREcDlPzzPJzvFybldXlWeo4d4WERcuBYWe6mO1N03FB8Nbqj1Nx0A-6wa0QdyomwyWFDOi_SSAjvyEwFQvSK-WDzhyaaHzP35UIvjGKXLvsFYbXPJ7lhcHGHzwkRuWvXKLOaixQbt8S5kMmkQ_nZhZk6dzh9i5c7crar-OA3yhPwckpZaL4cdedIe5TOF2ZK7KSEwcPr0cStSJ_vBU_RecoFWuVDnSCS5Sj8Uxa0JRvd4Y0lt-5xwKvIWAzpfOYNF-uAVrEcJtK1POvElSu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyim_HRDvOwLK91CB96KFvgzFHycQGl_5qqFiUox540zhf_RgEzkNX2JDno4LAvAi_aCpREcDlPzzPJzvFybldXlWeo4d4WERcuBYWe6mO1N03FB8Nbqj1Nx0A-6wa0QdyomwyWFDOi_SSAjvyEwFQvSK-WDzhyaaHzP35UIvjGKXLvsFYbXPJ7lhcHGHzwkRuWvXKLOaixQbt8S5kMmkQ_nZhZk6dzh9i5c7crar-OA3yhPwckpZaL4cdedIe5TOF2ZK7KSEwcPr0cStSJ_vBU_RecoFWuVDnSCS5Sj8Uxa0JRvd4Y0lt-5xwKvIWAzpfOYNF-uAVrEcJtK1POvElSu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
👤
ویدیویی‌از آنالیز عملکرد فوق العاده علی علیپور در فصل جدید رقابت‌ها زیر نظر مهدی تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/29458" target="_blank">📅 18:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29457">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD9hw-HKSqb9QV-rTNP2eq9GQ6oDSe40vga8NzKmAXMhxa-4eq7899QSDEpBPK9H374Jne_gBqGWvcWKBaGl4BsmgqxzAQec6TBlbsN7E4iSgWahXPKBkEV8dgTAZbFRdPu0FXzb7C9bV-b_eW__1PT1Js-FhvLDMR3Hf81WADm0TLHJKthUChvv23o4ohq95ajAlCeIO9-596ecibD3ascS2Q6KD0J8e1qbjaQzeZkqVgmDiwjwk3C7UadprIEaf8Eae9e2eIdBq37PVXSSvXQKngLa-7fnoZAM43eN_Z61UqjXH9IxFcf1LRL8uRWS_9_Zladyz6934VB-GM8FWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/29457" target="_blank">📅 18:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29456">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzyVwQfS15IzKMbDxK19FEamGDggbnOlM2b74NkdCQ7DaSq54q3CvjSO01bBugx0eziJnqMCtAG_w02aNlw4lNLbfLskkk54f-n6kaeznHicNhedHNKCLBl7Wxu01HLZ84z5gdrT1CTd1aOrEeeZjmT_Lgx8eQ1LPjJKyHSGDise_hBNaT__W0-qqgOLDyYwOI_LRuSx90iKYAQNqUuFwAAC2FZYWAST3V7y0MqL6v70H5ZQgiuppHiEc2UJt8v3v7JmGGt8L3yfV-dF_o3BAigHn0ICCAdWZMuGYG1rB4_4w8iZyOl1abFZ-dzcUv4075Qx-SSPXsm1uaL-gJWMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/29456" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29455">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f74RI1WL6YdX6PNLaVIHSeraa2-Uc3SMWlwBPI6WGpgVJZP0MCZAA5VThIuih3TAzbVAkD19fyuYjJ_CbJtEiqiVuxMuEnGOfKgqULMvlZXMY7MwDIczZOUdwQHtFPD5WWaZuaW22q1xTcaKQSCZr7f25psU7-EKLwu6W2JB7mf0WOjpRTmojF8OpUvn8CR3X4GJeZ44rHv2Dc2YwzkFO4A-C28VfLA7KrFF1y1Uj_ubgJTPZIHkQHh0Nz-yOGunyP7gUBxxOO9z0b_1zl5txGZXOJC6KoYBbDvsKwivMp_LEZlilWg2tGXAdZJEjqj1g1UcVZ2BRQf1rCaoOvZ8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/29455" target="_blank">📅 18:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29454">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYBgrq6G0rKxeCW6ABUaVDTwnTASaqJx3Lm1TMt_FNsLtuKff6RRKvHhgSYGXiOinBNR5hj8tsDGmFtyUPEzzbudMpXwIpPM-W1LfUtfhei4RkkAD2mgCQMngcyNc3EC74s0AgcqR_Ag5tgheiAG3PjD9k6BdUv0b6PaFmJd5m4j_RHB9mDl9QS_vAEibDvbIZciYSA1xG0_WK0YNAv5_zPF6n04blqW9oskTMC38K8ejPhyvbDPVlryUPZF3UlfVJy_C5TTRwzKCbzROt1LuD3ghn-Wk2FhBMfZzjVjzCtxXRsCPuCWx8lCbCvhW3dPZCwto6uz24L1ia6gol12ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/29454" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29453">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VThlg64qvBGu0zosifBGQkGMJtAwvFa_lanvsdC3B9vjXOAVaNdTKNEsdR8R2wk74OHtXYhDitghv3tFF3eI8Ja8LxOWqv-F0TW_eHmnJHIb_yg-oABzjcIOYHnna0IVaxIErTjCybA_hbsFZr12AawLVz82t-vzutEK-lRqPRJe-cj3MS4AwhuSnAEjccGuuVKerPEUT7qiTp7xDlHS4WmbsXuJrIzcgt3ItadD6B4iVfu2Hpk8chknjv8l-Z1bKpsq-lxMI9uSFzRUSjGzngXjH9jYKFhQnSaJSZWJQF2DJ8IcK2Vtk-hjL88f5F-4_KXfcmnU6f48DaUtY0VOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/29453" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29452">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2-VmLDSxOWyiXAsM7-8i8vucY5ybzaIr6MnkkdAozCiV8woxK2PwQGk9W7SSmWKElJvY9RttUFhjyHF9906KL91hLjcqzct9HS_yMFw54l5pPbD3217sJmMds7EKVpHwyN01pSRMiuRLjRm9kIHelmRywz9lcIEV-RKoHojS7Vld1PE9663CcoEiolRfHSNaEYGCZ15sPcdweq032qByjqnE09C-x8nhqKLB8ss2DHydkNBv452Tss7a54ShvJX4P8jg0Bwo671JMYQ3hDihccXZyO2HTxpto216e51pxb9xWR3J6JT2hihRhTpxZk-FwJt5g5CudT0rDzwck7tjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/29452" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29451">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX8hc2zlKkolUd5TmjYtVy0SdE3k0qnB7n_jR2GiVOivtoPg2BUmI3dkVmKzHzFLDPIDc9ovJSwq1Pe65DtKGybNsHMKciwzbiiX_4O5V6Z9exiSaUkbE-wH7G4GBwRGx03og-t2gpgpZNY7yz3fovBlNHQknwWb_yUrPUVUx9BH9uTJmg6nRevfhsOzEv3INkWNp_r78q-hrgixH9P3idqTyz6b89Urx_mqvZXWx_bpljwFBy0Z-BUyqE8kv-40dWDYt3T-NxiAWyK2sGpPg5PuhLMv4_GVxxx6wDgxD0jz2O9_CMfeUrYiCeDyllZNrn4ZdydFDIcUZTFiFrdaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/29451" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29450">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=doLqVnSDr0cccPbqBeN73XCXwplfjlcIAvfw2B3z66Fgw8US6_8uuAwWBnd6Gg4mBEEFqXd_-rfaXmHiK8CPm3ZtLj6IH1qz-kK1mfEMQ6597GHBeCdiTzY0Wt-bcQU0bVPXGj_5aCtWNYi265ih-qE_CNVlJWFLXS-jRz6b_h1mxVGb27EIBGPr2pii-9KuP-RUixsq62nsMzoVW9SX-L_ugUgQTrvj78pO_WeO_ClWDPJJjHhN2lQlv-zaZPZeuffIGEnGgd07VDJkudnJluKQt7DuCLsn5aDACVYEl3R-P1k94C553iI-ykheDvO6Rvf8nrasXo_SooBqhe6ahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=doLqVnSDr0cccPbqBeN73XCXwplfjlcIAvfw2B3z66Fgw8US6_8uuAwWBnd6Gg4mBEEFqXd_-rfaXmHiK8CPm3ZtLj6IH1qz-kK1mfEMQ6597GHBeCdiTzY0Wt-bcQU0bVPXGj_5aCtWNYi265ih-qE_CNVlJWFLXS-jRz6b_h1mxVGb27EIBGPr2pii-9KuP-RUixsq62nsMzoVW9SX-L_ugUgQTrvj78pO_WeO_ClWDPJJjHhN2lQlv-zaZPZeuffIGEnGgd07VDJkudnJluKQt7DuCLsn5aDACVYEl3R-P1k94C553iI-ykheDvO6Rvf8nrasXo_SooBqhe6ahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صفحه‌رسمی اینستاگرام AFC با انتشار این ویدیو و موزیک تولد 32 سالگی مهدی ترابی هافبک مصدوم‌تیم‌تراکتور روتبریک گفت؛ ببینید چه اهنگی براش انتخاب کردند. بیشر بخاطر آهنگه گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/29450" target="_blank">📅 17:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29449">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG72aKJ9Xhq8VQKMZNVY3YKWmdcIroI_Tcn8ovK4YqtMynhlaW1Pszwe3IisBfWG1qs57aPPdpvydontXWzpo6FlrPcdXCcQoo4y8lGIJpr08Bb39PNFxZk6rU9kGPjBKHGmmeV3Th-OGVMZV6BthUddRAsMnaZjUZelMG9A6tCJcopCjg_IMkwnmDGOsVRDrFsoSUeJSO35C16PrJVZMVKpvCY-I-l8Fg_I9luBEloWifkNEHHRYQzQd4wF3vjQodUfu1ya61P02IPYrkBVh9A7M8BEmq0krG4PwfKV7AN0DeUBa0IbNUXVzYntJ6rDAAogHBsjYWBQOgLZCqlulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
قیمت جهانی سری جدید آیفون 18 اعلام شد؛ آیفون 18 تاشو قیمتش حدود 600 میلیون تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/29449" target="_blank">📅 16:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29448">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKx1nXOrVt4tiHu8in_ef72Kc6xNfxZ6AyjTRp2Odj6oH3-CVGK-vuYYH8V0_m1cqoYOQ9QSPUQ503CNmBEr-aDjynQLrT5NQQmg0Eb7ujieDwwrwiWxre1yKMiq4vxOGKPRoLdOA0zEChYa5Mtqi9c2uS5sqE75YkKkPA5yoReu_nhUWHlQ9dd_KqSwhRBqPl5ngjJldDF4dpmU2QJMuCcPhhSHSG68DJBoo_7YDmbR0Y0edCPn_46lR-khiWGinBqiopyDAhm1m59xFIG2lIOMhL35RtwgqcocGJNTBElo5hst5B44lYCcAMx5e8AFcwNzi5N5IDZ9jUzDUcQ7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارت‌پروژه‌جدید؛آرام همسرسابق‌سپهر حیدری کاپیتان سابق‌پرسپولیس رامین رضاییان رو فالو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/29448" target="_blank">📅 16:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29447">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOqCHwPgFLKsqRogHApMOTYXz5dADR6dlQWlcK77OLhhpyS-0Xy6y2pKPn6EVc8Ac6d7Wf9Cse1i7BTvLs8u46okmKSF52niRBfCkEUtQkxBS3l-vx5NLBHT_3xYNqreHj2V1xmB2ITxnMBGY0SltL2sK8GhLIXgOddOPM6I2L-UKpaot9UQl_V2xNx8Y5BXOvU045KJ9L3Wq5JNzU3dVbzQ7DSdWMyZ0qwrvArlKcT1j-6j1ABfG08MxccJfLvcR-FjemAcTPrOpNrBhES1uh6PKzBSASFZG8yoYCgrMU5e0AsLD5hJaSFskFFvrWygYhtWFYBfgMKeXLjqRgjV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/29447" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29446">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9wxNfmmQ3kTzRwRdJTwg8PXZHH7GOVyg9H1OadW_0_LoobN5iw3g-Wauhe6f7meRcYl_oTfYTnnDXLtodriejCsqkeMrwRpHh_XTx8M5aGWV5Xo5MZ510LMJM-lk6yX4ZPlQwOVwjK0MNPjOh6qep42yFaCeWZmE_AQrknHYcihel9LRPd1RHMpP9JzKc4b3VrsxwjUq6w88xBJvdtw0LWxoff8DZH2oNgntbpvOze9jJx8PnZaWeypPoV3gUntbRKkXbKEWzAh9gJu6RrrA38MCTPQ77qRtQ2UEwTWy868DWZMEdrnMKn5ta0FiwZr3MLgVq6q4XGD5wFwl2kZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
خبرنگارباشگاه‌اینترمیامی هستن که اعتراف کرده بخاطر اخلاق تند رودریگو دی‌پائول جرات نداره در پایان مسابقات این تیم‌ باهاش مصاحبه کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/29446" target="_blank">📅 16:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29445">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSaDRkKtCnOcL60_runzo6N_S3VrARgMycaAcyWMyBkIITddURKEBUxBiKyUKpOUYNfbcfYNsxe_RIdlRQwtdxm1pH8sQQWCfO5goF9Lw2Em_3i48s5B6cW8PGP8cyeh16STsikKYyD4Zh-YV14W3dFNkuuVXumAdcZ8u_ZtQZlaWirTpfF7pRF8IwFKyVS1kvjwV0X5IqFlBt6EdFdGEG348_eBZiBUS3LknWQmdT9Fjm477i9oIvBU238jqgPfS1LzoGHQdm_noawwULRnp_nJ0_mMPYAPSdru49AUGAwaH_H8q5QTiKMUkGUZMBxz_p4KKwcmUfYp2wDfzAiX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/29445" target="_blank">📅 16:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29444">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9Sno5lw5UMm660rlKoYdCGnE5XzwQ75h9ckDhTK1V4yKxjoOKMWpfN8NSmwhM_jU8rziOkJXDYj0E0SzmATflOiW6V3uCoOTaHKlVS3NdHuXUl01Dk-RKPJMRl66yWg0ahxfnja2sctiSgeUF-VO3vcgbu51JBa83D_pxy_OL-QGxqExnI8vaAv7R453pom3W6GOx5o_ykxZUoaFc_IqMY2HIwpXCFQlDam6z3UCcvPgvP8Cq3XGv96QjoHkC6naizICjT6OVfBrYrVEtKntjpXKgOy8WPBWqI1pyTyw1JZt4LQyxcBwO6jeDYFBpJCQjtv4aKUlqJdfZUmYm8rSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ وکیل‌پایه‌یک‌دادگستری امید عالیشاه؛ با شکایت بازیکن کهنه کار تیم گل گهر از خداداد عزیزی ممکنه سرپرست باشگاه تراکتور 6 ماه‌به‌زندان برود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29444" target="_blank">📅 15:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29443">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=Igk89FLcYBIg2fF9NI6H2dDSGLJITrwdrxEpV4C9bBvJ48MHmREfUCBhxYRzytyfZRbW4XjyA1Z8kPCpHRJof3AvmZ7hRECf1Et2Y-6vjlEumZJehtBQMnbCxTxEm_FR-DO4SWfVRGbM65aSUvOol5Hernqut7AXBIRZThaqQlmvuzX4oHWwnLwLAGPxC3mh5bGpIZSRvZjaK8QGo1n5aK2itzUY0luQAtq3bNoR7gffqguwR62qtdPvBscDJ6H8C1Yp6qaQavmuhZnkCGG-1yp2z4d0p9ZpewxCypA0ZgjyTwWziEhOKw2Ql2W7xs6bnIMKcPMe3sFd0kTpWdGBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=Igk89FLcYBIg2fF9NI6H2dDSGLJITrwdrxEpV4C9bBvJ48MHmREfUCBhxYRzytyfZRbW4XjyA1Z8kPCpHRJof3AvmZ7hRECf1Et2Y-6vjlEumZJehtBQMnbCxTxEm_FR-DO4SWfVRGbM65aSUvOol5Hernqut7AXBIRZThaqQlmvuzX4oHWwnLwLAGPxC3mh5bGpIZSRvZjaK8QGo1n5aK2itzUY0luQAtq3bNoR7gffqguwR62qtdPvBscDJ6H8C1Yp6qaQavmuhZnkCGG-1yp2z4d0p9ZpewxCypA0ZgjyTwWziEhOKw2Ql2W7xs6bnIMKcPMe3sFd0kTpWdGBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلایه مهدی مهدوی‌ کیا اسطوره فوتبال ایران و باشگاه پرسپولیس از عادل؛ سرنوشت مسی اردبیلی که در ۹ سالگی وارد برنامه نود شد به کجا رسید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/29443" target="_blank">📅 15:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29442">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akViPJsGT9JKWAlndsWPYekXJQxWe5DeB85IaQCPcUuWeS08Ih5tRySBjvR0so1TQTeNYM1whde80LYnl3vw4nA76lOCpLaqiMCgRD-fPCfqNFKB-rnUbMUqXoii-Q0Rt4I28FMkjlZ6LDInaBR9JJnveTkQghitcisvWTUF8z_KfYFIS0A_UyrG3b6gm75_ys6RlvR_wigI-7xwcySLNCwVLrrFkHEhMxxEeXF7nlHzixohZUi0F2VSM2i9yS-jEOIzr2kxhlXSx1YXh7liieXOpNcgcP3Uhr5n_KngB9aLbwRHuAijVVWRqkeF_zuzysywvRyzizWEO1XmB54hZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/29442" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29441">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzXdtmSeimnP1sxXtuT6A6tiO6ndRRv-NzcMi--Df8X3slXp_IxRY6e4T2Sga84h9ZfkKHTX8648PraxOjyNL0YOqCR4i60q1qeIOrHZeuMKz0zDgaTcpKmBN1_TmbmIl1fJKxzaGOe4uekWh5keWsE8qtMFZQNiJtr49eKoZ-cKV_WCbuvmD9gdSIEjEw1m2y6JQdDKB_-nkeGT981TqvDGM4WSRErPQ2wVzHQVYGQiu-bl_q54eaZcZVB8LtaHSPEvhMjopiiy9h4Cmy7zkXNeqO2OkG57-2sNP7WwEB7bailLmsAcZLoWuXROPUOzDA6GzTYiTlghQnUO3b7vOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29441" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29440">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAzAq0rNUQqGEBeXHaPd-qr3naLVFz2mpKiWHrEsnTY2no-r7uqyhcG1wMBb9TKHSSR0_yUr7pQttGuqQCB-zgm8Vs9dhl_JLFFY9zhfKWoWwqCFuxaU8V_VKsr3a4mN12171PfLyfw2L0fm5PJlMF4DBtLDO8m5FfBivE8pAMFS0Pk8FllJCivwKwTCxS_yYCl90OCSMIMOcFrLzgJFHqw09bcJmYQZTcDY7bOIJrMUos_2KUJbLMdd3_57AQrAnRBz6vrcAXnxwKHg1YuB3dNoRJ8L0pGZqZ_cwnC7Qi0Yyu6xKi6begF09YFIEDYsKc_mSgG8hhe7HSK577Ishg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته هفتم لیگ برتر ایران
🇮🇷
استقلال
🆚
پیکان
🇮🇷
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/29440" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29439">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYMfRMUDst7tAj24tmJaRBNzgcW0QcRW7umnl8oBgic-2jFzDNBu0P6wjmySOQgucM2xNgMOAOdox9wmFI7e_UmhQtSJ190qijKxPfkSgAXBGzwP5qPp0IYYbu__c-He01NatGud6CxTeeaSuxKFaqNQK9Km2N0l7a9ONKb1yvYqajmToQyRCcGOO651EOt51elJh2xnYYVMVruaDVjlhkh82krhQSlqsVcAjEUJRSn7nBtEzSpyeZaPpRg67y4k5udKZugUZReiR9hx9ZW0eo34eJ36M_MApiH5lRyahthJrWMh0CoKEEHnBPAyCwIPd5Spor5e0YfshQbm0Gznhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/29439" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29438">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhwLBwyp3g-WZeOarBERAvK1FfiKXUzKWolhpmVtoXtGv9mbdHWzVTKMu6O_0wZxpERC06rh407xSkYn8jtNTE6eDwFSnfcktaVAS_D7E4vZQEIMY7FKCPfyydtjy0gIrihkHDDrrVg7GCFF6YNcMzH4_iRthTu36UkKX7CSQCymwFnflHCN_1r8ZZ8bThPabggMINBIUmO1h3kQYdltwDyiOcczoBFGwY3VHkKi8zFbetiAkQDYtOlKu3ESElYYtjDUuad8VHbR2I6g2Rd96ZgUsagHWFyaahMYjkwrv_C-sAXwDqh_QH61Otjqqm-r1WrWYxRM1zNMa9QQuO9Pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس:واقعا موندم چرا بازی برابر خیبر لغو شد. ما چند بار اعلام کردیم هیچ مشکلی برای این مسابقه نداریم اما سازمان لیگ به دلایل نامشخص تصمیم به لغو بازی ما گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/29438" target="_blank">📅 14:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29437">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY3nOYdD8elr5PtCnJmbUjJIcJi4OgfA2hJl_s5AhQ9SLXOjeO1qp2xBI5azvKG8JX8dFsBvJqlBZXjYv_SrFycw4e8qYDwxyqDxOAwcI-u8bzmdlZjsaoiI2Hbak5g6YO3efpE-Ertwequ4786D7X7c_pNqFV30xVzAPibp6Ek7O4VlIwDLUkYtEYCPTWK-IQQAQofJj3gdmcQbVVS_C4qqMGu6oUPr8M2hzr_SEAj9Hj39F1PsGcQLug2TgBUiMI1O2cuW-qi4_r3DJwqoKy11IsCHJzPVHv-jzE01jRowfwfTjJ3dOyI2Id_6X8iNKWH81tezG4KVAC3CJzjrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29437" target="_blank">📅 14:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29436">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBevE6cdLbUca4gOweEPBLqlhfJQuh15Oh8vQ9_JJtGwVkTWiSedLPJhXpTsikzC_qUXTnd70BjsfJnNyZtjumR3cqsmLTTpq514qsshEF5ykqBaD-A3hq7CBz7mOB7rnGZavFqxRbGor0cNgZfzN7C7LApRGdQwNxD7reV5ChE6m4ktuqKAwiMFNid1_Baz5FHqWFgwbhFABc0jVeTLSLCrdlranh2L5WSGGLYPrFc00dt1KlUbNxGjuIaEMoC1NE8GOYvJzeYCyfKR7WgkQvhTvX6g0Hnfhh6HiJDx6NtXDVDhHQOZxCTMxPWbgb0lMA1-1DmAGXLD3fhE5aYuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛علیرضامحمددستیار مهدی تارتار در پرسپولیس درروزهای‌گذشته‌با فرهان جعفری و محمد قربانی تماس‌های مفصلی داشته و از آن‌ها خواسته به تمام‌پیشنهادات خود پاسخ‌منفی بدهند تا بانک شهر در نیم فصل مقدمات جذب‌این دوبازیکن رو فراهم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/29436" target="_blank">📅 14:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29435">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-Mcx5qGz1JFwKN7SwEKtONWqlQfNzF6DdldH5mvDhIx-pI5BInypr6RzHOHdSAmUIsmEdj9ReeJjLu5o1mkzquSYrWntPC5XF3qMRf8DeT2NFFDIefGFVaBDVVmOZHwNgSEdJWSg-Fx2_sVK0yPnoYAiqZgASW8hInhSe5OPJBGb9hSgoK7NN-QUaZB3Ck64XJvMKcL3atFrUnSOHFGS8DR0eTqum6rqTsEtzz_MMFbUS60biIE6_tY9t5ieJUhI2BOsf2Wv6AMZ7Tsak6SRnIw5Jqou7ZDWxLCX2z1XZzcAbU1z-gDr7VbQrpUYfaQqFyDPB4n8MciqnUkn4stw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
بعداز حمله‌شدید هواداران کریس رونالدو؛ دوست‌دختر ژائونوس پیج کریس رونالدو و جورجینا رو در اینستاگرام فالو کرد و برای او کامنت قلب قرمز گذاشت. دوست دختر نوس بعد از اون مصاحبه علیه CR7 توسط فن‌های رونالدو به قتل تهدید شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29435" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T71Bu0uanTHnb6nUvlkoKpebzVzAlrxbmsCOrvH6VLUIdGvBlYmd123LZGIVYDtSexrHRQhYGGwRiMMVVr6v5hPUiiK3OErXlev7hn3UEK683gNO_bF7d54EUcGjlZWqXhdIy_5X1r1JXkjiKnqd3-GazgtixRXYmzSWABpTE9EKZfGn1SOKOtKQpiG-urEVSldtHA-qsPJ9-v_8sOUhEnfxYyd5_vEJ7SiudyHVfVcnPjP7ZAc5SEHId3Sm3XtyQH4ss2C6Y0w5BlwVDTa-IXHtwBP05Sw5n0hFToDFg0hxuwgQXRLnhz0llrLAXZV9gWEVDXo4_r0ZZkn1rp6NhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29434" target="_blank">📅 13:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29433">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCaIqCh48VHqWvUVvccl2vi8yBXwfMEcRiB-DBJ5s_Xo8jfPnCK2n_q7y7xpxa74qZoPWjkQ7mfyoZOnB1sE-jAOE-eQR1vO7sNgF2En7ccMghpMFzbtz9NW9NcNaTYwjWQpYHgU227BDIGNq_C_FBR9lzYMXd7yOqBtmYdyTO8TB_6xNF51g-UOwJ3M5dOczr9Xh1gHZCg2qHjIt-rrpSehkyNFQzLKAzEP1ou7FUqeFX-DkcXo-HAy3rV1ZHCxBFoAmb06UsqkJB7HLYB9ybqFXLRb7CjYGm46Hb3IwVUUXePuHP37qiCy70uAVJ4FvGsPij6_xEDHFZFzTU2OSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29433" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29432">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyvdxzAQsEHtKxWRctygaBScmDBY9DwQBn6tSw5d8gaw8eFrGleNePA3ELzj-8gt1L1ANxtzYTun7AQS7gpi--cpc22viJWqZ_YkypseUcuaN6DRWMBzdj6VO5qq8YyFJkg_FVXmefrAnoxN-G9t0O9EEXFNo1MADVcMICB2lGnm_aGR4RvC527hyDGhnWquxg9MNggPBBg1LJnXRdrJCN1ZAIseMaBpfKD6ekZ6EY-gLTKnLi1XmjIIGaGiDqd5agZHZdqjd3mW_Qy9THtOQbyiMZeW6mcR-8TSNPW0nrEmtmLz_oGMBtMHY4gBRAJzvIPwjZ_5dMnIR7_VYEY2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29432" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29431">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbStaM4I8DTk4R6NT2VapSQ3jXsL7m-_Ssp9RhyrQM_jP2cJ2qdOYoQTOEApH3w0BWKrOzq0O-DRHJIvFN_a53RSyojn4a8KFCpbPA5fiRKzok-o5JnXJ7sKTZlLl7YJKtN-X3XVwwsHVc5q-omJFX0c3pP4TZ44sChQki4UFf9xGu966ScLOgm-4uAwElPBo6vy8beASCa0Guxehjh6qRyCMKY2z0U8stepRC3FCQwzzV5Ky-SYOsZTeUuq8134rhrWn-8ho2_VSRFBywf3fvW-G_jFF5U3Ew1JeZ3QQlNvxQja7qlI0jqs1_gDRZQLkmI0O4pkeESYYlYE4Lv1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29431" target="_blank">📅 12:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2Wn8pAYVx5QMW0EhL0bAMaYp2JAEUPN760cfXXDP9gkCli7dI9rwd4l7CP0DyEXHlSZfXhoJAqdRTs3BGTVTM1gm_HDdZn74UeXBcUZyIuM62qyfrNgeyJOihjXmaI8eyWW6DwTqcYYA6hPALk-8JgobYAH-ELkGlukUE_TfMZoathw9I6rZiu3vKbSaIsCJyqv96v7Jt4BIKNorvnM_099L_5Q9M-n7cWkJ5n1TBGPFNYSqtgpBz77QSb2M4fhywQjiZmGzzO4avIcte-gZSXntOX7epOUevVCPWhXeTNXDGGwJVCp1WmtuA8aazlscrdkZw5Miq26pFJKhsAZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29430" target="_blank">📅 12:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=UXPFW6MkA24Mprn81alQ0Ny4fYHqtcpSMhPm3VbtnOIhj3dsu9KuciUjNgQTdwwTAWj27BA7Iqu43RLMCSYRR-HWciTJp0O4YLN3kEKuQm1rh3a3kM_fIq22_mcQHo_kTxovWXUfgmpp_kBwSiHJJfA0PqsyEpW3r_Q6UW6_0bc5L10qVTTdosu7IVNukoJsFWl2_ILLaImCr12N8QPSLfFDhVO8blaOggPCY2QGxdAbiU0lUYfl685J3LOEBfjE6P64_aqV124cG9vYr6s_ZDlbWXI89p7AoAUpicSIRNzbs98ZnY-T43z0zaUqOr7zGH7ywSm1my6hyJ1ah6vrPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=UXPFW6MkA24Mprn81alQ0Ny4fYHqtcpSMhPm3VbtnOIhj3dsu9KuciUjNgQTdwwTAWj27BA7Iqu43RLMCSYRR-HWciTJp0O4YLN3kEKuQm1rh3a3kM_fIq22_mcQHo_kTxovWXUfgmpp_kBwSiHJJfA0PqsyEpW3r_Q6UW6_0bc5L10qVTTdosu7IVNukoJsFWl2_ILLaImCr12N8QPSLfFDhVO8blaOggPCY2QGxdAbiU0lUYfl685J3LOEBfjE6P64_aqV124cG9vYr6s_ZDlbWXI89p7AoAUpicSIRNzbs98ZnY-T43z0zaUqOr7zGH7ywSm1my6hyJ1ah6vrPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های سه دیدار فوق‌ جذاب امشب رقابت‌های چمپیونز لیگ؛ لیورپول با شاگردان سیمئونه، تک گل دیدار آرسنال و ناپولی و آتش‌بازی شاگردان انریکه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29429" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29427">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGfDGLk9EyNN5lhi5ewgHYznNaNiyAH1uZuRaGENizdGNznygA8ymyGU-_caOSlz-i_VuObKN11r9rod674jJ7PB5XYVHXGCd8vkIaazJ-JJMi1GtSBR3kRkf0AICEA52PUglxiHVMEiTRz6u8sg13Jq9JKP7PSgFpbwmkxL-BN-tRs9xf9YnWbDbHwjXr23X99Pxr_UecYEBpWgSUWcqRXARP0c9TVp-M0dUfeZuN75LJZB0TECpQaV7k146msEAx0Ot6xZyvkgAAoIkmMBxDbR_ggLeWV3bh6lAEN1cc6nNZEUPmNZOmaTMvasXL7sHhcW14kK8DGPBHxs5n5SOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssphVKeoT8rLREx9kW72C6EUygBEE2cdTk_0UBQBtmji01FPIu2OE5Bz-uJTxj_UaZ31Ax3J8htWMRvXILjeltFsajRjllLe-URx1V2XSaobfzAt-y-SGtaKMmIp94kSPEEoOcIrLZjxC-1Xv9ydCXfl1Jtn1M1tAt3HNTrg_4UXwukVJ7DVNLdipCvwnwreWqK6jLGIMot35jnVL6Zaxg1z6RnC7PZQPCwhH0O1c1uT_hTpZNkHu7olkJFdBUjeWBHEpy8P9Vfwu6oQKZSJwbB_zZcX69M5C3-tYWEoig3tkrI8AUTX1NAiHdcRfbyAPKcH_TB6GThu30MbOn9ImQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
پاس گل دیدنی لیونل مسی به کاسمیرو در بازی بامداد امروز اینترمیامی‌مقابل‌شیکاگو فایر در لیگ MLS؛ بازی با نتیجه یک بر یک به پایان رسید. این423امین‌پاس‌گل دوران حرفه‌ای لئو مسی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29427" target="_blank">📅 12:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29426">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dWHAVYd8fVtz5grfJLNw7Him-YPC3Md5YRwla6g0zUrz7dfNdiaIfHKrYiqXJ3Z1NCf0XBzgGZQgXAKKjajjAsSYTRA7Mn2i7l7TZzXRDYr0tKuYoJjy_vhMS2A_ZjtnjY78DSHeF2IDsUwuF5D70Nlo9HU9hr1IcHDQrv-eMMu8j6kbB4hjt7jTfkG3foYn4sMhHtMqU-thmYgYeBaoYvh46apXQolnQDg36XWIFYUB9oxAKIlcUnJJolyCpZKBM6HelHpCptmCpN2h8hT3MEdDyb1XbtNBK0FFx88WrSklTXpzOBERLS6tQ8S7pMN-fX1wsfQufjzNFug7eP_mZYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dWHAVYd8fVtz5grfJLNw7Him-YPC3Md5YRwla6g0zUrz7dfNdiaIfHKrYiqXJ3Z1NCf0XBzgGZQgXAKKjajjAsSYTRA7Mn2i7l7TZzXRDYr0tKuYoJjy_vhMS2A_ZjtnjY78DSHeF2IDsUwuF5D70Nlo9HU9hr1IcHDQrv-eMMu8j6kbB4hjt7jTfkG3foYn4sMhHtMqU-thmYgYeBaoYvh46apXQolnQDg36XWIFYUB9oxAKIlcUnJJolyCpZKBM6HelHpCptmCpN2h8hT3MEdDyb1XbtNBK0FFx88WrSklTXpzOBERLS6tQ8S7pMN-fX1wsfQufjzNFug7eP_mZYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو جالب از حضور ریما رامین‌فر در جشنواره فیلم ونیز با تیپ و استایلی متفاوت و واکنش نقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/29426" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29425">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fi870Y9iB4nuIm_G1W6kodqfwPgzBFwH1JR6COMv-YMu5f9OnrQ75N8G1mbeoO8XWRuV8Ksv0Sz5f4_xaK2Wx566cZwRieTV29liLvNMkspWrhQT_IEYmEfGX1Ai7zJeML2N_RgGH1X9vGCsOIS6vW7uFAWmPbDF4qXA0ltKZU_tozw4As0Y_Xlw0iL5C8lIujbxZc9V5D2PTkdhXZOVBOG0hPfhfCwOTXtb2gFEF3TMGq8rgb1HXJ1x__MoWK3VGaCwRQcRLX8UEXE9mh2Swwk0Iq3jlJ8rfD0gnM4l3kYfcNkNsFDDxlorQWwUAVoZgQYQHQ8Icfr0h0QDgylGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی‌های‌جذاااااب
لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
🆕
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای،مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29425" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29424">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A74iCNTV-MAoh391GlnPrObsX4cFi-uy42hfprpbIXwfUYIB2lqOZs3Vv_J9nVMEWk1TBSirTNf81vs0xa43fDR49r_EvB2o72PyWcHoureKJFFK6c9gbRt825wIbw7eA8gEn3QQLjxmdPMxPE3UsRDc4_SA2pboukHtbSp_YfPhVGObnjnnXOtxCXFCEWGMzeHHYMdIHJZxUSliW11m3IlzCKxDSOjdCiZYg_wlTVgcpxqyuxGPZ2kShez6LJQnNOXsDBR3Ft_1VO4mU5g_9necNfj-aWzV762YBoYKZXk7MvnXrN_HUwZxnrZmnqAt0VnXhpe8rWT9vjftRtBVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29424" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p98d0E0GkTFWnh_NkiblGxMnDhCv50lLxmokBcDe2NgHwolHWmSJPjhz4dx2uHx1QfAz-6P5gX0fVJceEEWjpdTP9Sqzojm0h8xOKvH1m-zLLKw-hJ0fqIIl3E9gEsDYGobmJKvO_m1FgK6TXNVg1ankqUhSBjoBzyiCM8uQWW61_EGu_oMGj_tbP1ZRBA2cAWlz18WEjsz-fS0_0Zi2RxK1NrFPgJiWWRhXqxJM6kKWuTR-kqoX3PAcXwTNgEq5gvhGq6SYOM2ATkObJP0YR_0-yGwOh0ikWeU_aMF6H3IbIjyaPKqzOzCMNFOjE7favYK4uZR-O3bWrbNuPEGIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIEymmlid3Xb1ukcY_Neh3QLuQVwAlPlQS8cU1pQQ4mtU2TBrT4_w_2lL34cPjGs3LP3XT5vf-MZ_e3YOsZjvTjkyW-r2Zc_zGY2p1jWFsUFhTC40QdWAhnzB2YdSAFFRqxIPwt921nGIE1b_mQXqOusHaYmv8kb5HQqF_eDVInyTZSJkzKg8AzXsOoi8eCFKlqH8Oh06-okzvYflFhl2FXnYmu5MadvtYenfIBP-nNK3-fBF5RHIur-w2SWq6akDCDYdLXy2oSpkB83eaSO3OOdFoUHEcFt2UK8G26rrjEGqrHbWhT-8BtC3I-umu5BmXEUOMa6hDOQ-3-KNDbIxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
🇹🇷
روزی‌ روزگاری آردا گولر به‌ این شکل با رونالدو وارد زمین میشد الان دیگه شده فوق ستاره رئال مادرید. رونالدو در مصاحبه اخیر خود گفته آردا پتانسیل این رو داره یه روزی توپ طلای فوتبال جهان رو از آن خود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29422" target="_blank">📅 11:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1mh3nqaD_h2mRyyA_Puz7zmvBCKSkyL6j68WYYMXCdT4tf081lwgyWxee0WZLqswMeU5T4b6u-PeWarULbwMWcD3jscfgmv22FG4IPo0MLM-Zv0v9-_lTWyMslO23dj0RZmO6e47ItzzamyZe9Iw-vGnX0fwToxjuoOZGa5PiqZ8E47yF6rQZhwp7bbT0jI3_Xvpz0mvHiJu6sOKOZAvZ8bwN-dS0j8QmpRQSi8YH0p256UnpEYoIvyKT9ECYZzvVEUn8HSTQqlrhu3lgexlwl0sXGgBj4gcWkMletUafCTKi5mgnFcoVkB7hDfvlOsVz_NS_PZvHBO8JQh8mxGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان:
حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29421" target="_blank">📅 10:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29420">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=eQOrIzhnullDwrEXhrCOIE001Hpr6RH7ItS9ZLDA6XNECLT8KjaAvR-wxmBQGO0Qtq6BwoQ59xVlaCpxEN-dtjmbbKpf3wokACwhZRuTZIqQAD3WR7FRSmnhmTgnqgCDqqGdbEpRq3l5_8LW-GiVLkqeCkU3tXhYUHo0aodczuv37zKhOBzt2MT6OX3sA-9d5MohY5N4_bG9kZbaAsDF4IReLZYptXR66nUt-0eqMpwyKNaRrGVol_Pj4ZWu9TLJLAUf26-f8BbfT-5ZxQ-pyu8Mj6Q3o49zjZ7Ax-Mi23Pzt0zYZA5HbuE0uEUgUKmxnxN30pM4ryIKgmldMeopbTOpIKamrhBUzl3Y1pN15yo_auaNjk1xRjoH1DYyGQejl1EJiM4qt9a0EApmWK3SHVVU-nOWETwVQbTmD8z_ZIkPsYyfbhgIamgSVMrXvmOutUsTGnOFFUPF1dD9EbU0Ylz4bf4fGAaWUrOKkHjUjXYB3E_bUlidRazaWRblgp4QzDH_TWDRRVE24HtR8P6rJl9MRE7y652qZyh8CA6i6937nhdtuejGaUpxpA3RgNf9vBPS1SiB_bd48Q7UV6YN9gNW4J99UH7r1EljyK-GLf_R3qe0xJL1MFKeeJiKiwv1ZPqBhCAzP8QMGhU6KJ30Z8tERjzQ9b9Yjj86QPaHHKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=eQOrIzhnullDwrEXhrCOIE001Hpr6RH7ItS9ZLDA6XNECLT8KjaAvR-wxmBQGO0Qtq6BwoQ59xVlaCpxEN-dtjmbbKpf3wokACwhZRuTZIqQAD3WR7FRSmnhmTgnqgCDqqGdbEpRq3l5_8LW-GiVLkqeCkU3tXhYUHo0aodczuv37zKhOBzt2MT6OX3sA-9d5MohY5N4_bG9kZbaAsDF4IReLZYptXR66nUt-0eqMpwyKNaRrGVol_Pj4ZWu9TLJLAUf26-f8BbfT-5ZxQ-pyu8Mj6Q3o49zjZ7Ax-Mi23Pzt0zYZA5HbuE0uEUgUKmxnxN30pM4ryIKgmldMeopbTOpIKamrhBUzl3Y1pN15yo_auaNjk1xRjoH1DYyGQejl1EJiM4qt9a0EApmWK3SHVVU-nOWETwVQbTmD8z_ZIkPsYyfbhgIamgSVMrXvmOutUsTGnOFFUPF1dD9EbU0Ylz4bf4fGAaWUrOKkHjUjXYB3E_bUlidRazaWRblgp4QzDH_TWDRRVE24HtR8P6rJl9MRE7y652qZyh8CA6i6937nhdtuejGaUpxpA3RgNf9vBPS1SiB_bd48Q7UV6YN9gNW4J99UH7r1EljyK-GLf_R3qe0xJL1MFKeeJiKiwv1ZPqBhCAzP8QMGhU6KJ30Z8tERjzQ9b9Yjj86QPaHHKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29420" target="_blank">📅 10:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29419">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=dbjkSNAubcj4rLbnMCO5L8wptFyPdicr_4UE_4ng1_zukBfBKynKHZPqLrfKPLSMSzNzrwF58tyOd4yryALqop48EIRm9DYa1rloDOikXIHCkTuiwlXzvO0QvQYMsiQSF8Ls2UkdIHT71ZPsAMabFscZlBMnk_qdpni7TC1vFiFEuCK35EQFNLheD6h8sD8Ac0hSy9AM_OxHP1NrsmYrvmF4qMZoZz_rU41i9SQ_dl0MgdW-SMMpKj5nbKSvlmq_eH72hKUf-viBwIEQaNPs06UokTflCWzLhAl6UtLUlRocfZR46eExT9RLmhyMuh6mYzgYy96RoQOMLH5I3u3CCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=dbjkSNAubcj4rLbnMCO5L8wptFyPdicr_4UE_4ng1_zukBfBKynKHZPqLrfKPLSMSzNzrwF58tyOd4yryALqop48EIRm9DYa1rloDOikXIHCkTuiwlXzvO0QvQYMsiQSF8Ls2UkdIHT71ZPsAMabFscZlBMnk_qdpni7TC1vFiFEuCK35EQFNLheD6h8sD8Ac0hSy9AM_OxHP1NrsmYrvmF4qMZoZz_rU41i9SQ_dl0MgdW-SMMpKj5nbKSvlmq_eH72hKUf-viBwIEQaNPs06UokTflCWzLhAl6UtLUlRocfZR46eExT9RLmhyMuh6mYzgYy96RoQOMLH5I3u3CCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#فکت؛ برای اولین بار از فصل 2017/18 و بعد از 9 سال، ایران هیچ بازیکنی تو لیگ قهرمانان اروپا و پنج لیگ معتبر و جذاب فوتبال اروپا نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29419" target="_blank">📅 10:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29418">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Goc3Xxzymz5AeTHhn9uYbiPy4WmKsyIlKjhz-PjvNuLfQhLDhMox6_EO7-WkOYu1Mr1iXg0MtlZha_JMTPkDkJ5swOzj65mYlkveoTTNqrLmcowooVmupQ3NBhBjoyNPJftsGnxZhxJlXnro7BwTbb0LPklE1MSpZfnZZUL1O8t7DwrkQXb4QeS89aerBrKgXBnCsLGz2xMhxjuqp-gu4HjbvgSiWboBZ63zY7Mb5ItKpX4GUsH7JRq7ijD8BDmLf0LCgNgDIZXyXSoRAotTalNLzoO9s09Eg7_vPKnyBNRnVbT__F2lQOIk8p48rLFToQjmF25eUP9_m7qNZbQ8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29418" target="_blank">📅 10:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29417">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9326281.mp4?token=NLL5SCVvKUFw-_-76ddiWXcBOnBi5poLBx89IzrjRG-WFvT9hYJTjPl_Q2DUoT-wjkkOWbTiRVMgZu-FFK9MB03xoQqyN_Nlhnk7xZZVUND223JAxs8BfDZhtUws1yx-y25zjSkD3A-8CnMAar3mMFTKDqfwkAMnP5lsXrt9OniaXC0RAEO6kVwHayu5oeUTYYaG4NNNiaPWExFKsNyRM9FxV6R6VzGraradCN3JnOa9TZfoZ_mOrC4ohEEPqCuW-Ml0lzt0IOJ4qQlTHRKTpL-Wlmy-8gAO1b5gR8iVYE32qPVUOxTNu1Ln2aPOTzcFh2Kusdd1iH-YQJPj5HRGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9326281.mp4?token=NLL5SCVvKUFw-_-76ddiWXcBOnBi5poLBx89IzrjRG-WFvT9hYJTjPl_Q2DUoT-wjkkOWbTiRVMgZu-FFK9MB03xoQqyN_Nlhnk7xZZVUND223JAxs8BfDZhtUws1yx-y25zjSkD3A-8CnMAar3mMFTKDqfwkAMnP5lsXrt9OniaXC0RAEO6kVwHayu5oeUTYYaG4NNNiaPWExFKsNyRM9FxV6R6VzGraradCN3JnOa9TZfoZ_mOrC4ohEEPqCuW-Ml0lzt0IOJ4qQlTHRKTpL-Wlmy-8gAO1b5gR8iVYE32qPVUOxTNu1Ln2aPOTzcFh2Kusdd1iH-YQJPj5HRGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29417" target="_blank">📅 09:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29413">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhWWOEWUl0wFlU1cHJ33TRZB9tN8FeCFRuDVYvDUxZFz5VBuyXNr2hqFg1gMaJZD8X8JU9vBHIaOQTWuPE-UGlg-l1e2J5VIhHfEyqBymKOLeV52sWjqe1GntwXDoSjcc4SZgt-h4at8QJzGwklOIqJBmf3aAt8_Kl69dKu5g9nOAIf6a0Pqok19Ax1b3QqgwgbO-qfeCKTrUBHLfWduVnI8qf_wwqYqyj1feuRB0pqEI_vIEjDn1Z_w38h2jEjLCx1tW1RG41And_dp7_tGssabpj3-_MramvCxY4K9YwS_i2foLdKHS3XIMPWa2czoEStJGLgyY1KO3FsHZpvXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد…</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/29413" target="_blank">📅 01:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29411">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUu-SG__aIE-gZth5H5vhVU0TluQFP__O8qtmXKF9ujQSoSJOUF9XdjzkHdBw16FMZUtX6EVpDhpAjnSIAy5xbcrrHs3PQk9qPTxjaXKaH6B90wXPTlap6PfyaBp_yP4C8LX2xNhSixEDuiv6UeIKVTz91Ocng4flkyhv7a7kFaBhPHgT9VcKh0fve4VrGTJL5l5z3pck3l-s5M3JXCSoG-qZqT82ndM1oKUR2ao1wjW2jA2KoJqrvIBzQzRMyNzjK49xUScSuKBTuy5VfaFcGuxS-EKiA-LcCBYZht_nb4E2QB4iCpyP6IVyE-3x7ph-3NbG9s_ZQf8bwBVHdsp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ شهاب زاهدی مورد توجه چندباشگاه‌لیگ‌برتری قرار گرفته و احتمال اینکه در نیم فصل به لیگ برتر بازگردد وجود دارد. به زودی اطلاعات دقیق‌تری در این باره خواهیم گفت. حتی شنیدیم ممکنه زاهدی در نیم فصل یاغی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/29411" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29410">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=Iu0hNR6vg9kzMmEBcxfyln6nARfm92Y0pkiSUfn3iDcizoVrqiiL7y9n3rW5W4Kyw9VgFOfefsCpb8fTDDs3_vcDuCdQOdQDx7ZPBbUaCyJQqfFWObOqL9aK1QX8xDOwGshO82gMAKAKkMp9mljeQMa1QlQfVk2uZMrPyuh_krZd9T7kP7k4Rdtvf_UXTZD4xZX_dkhGi2pLOZDKcQO85X5gepuOPEuDccJZt2YfKt99AXQJ-kyMzDHjuz5ZurY9S_g02GuMC95n3yF9qXHv3CYgiubdvFPzwFPERiqBNz-pPRforO0Iu7tDQkFydrWXT15NHmeuNFdaS51plBU6MTaR4DZyawfDE_vUa55V3KCxBttCdCuJXP13in6tQsDv5oJU-198Dq_Lxxy2WSIMsp7nsuhePLAVRODLfU953ZeJHSIRNLQE8evT75azmMaEfcIo3RsV8Z4ofdCnlZQcuaAzFCwah-DvROfhogER3ulj5CYMR4Yt9griZcLJhKucnOYabht1O0yDm-QBAGGOOZOTWZs7wUtUe8U9ouOyOs1trOpR0-hJM1r-fayArrg8jczFd7zyNM_SDlkHcqcoHkp-I2zWUDF01vmcJFwHwheIo1wkhKURMpF9CgovP4VwQdCVUyG5fH8zzB1_xWeAI22UyzpQODuNf7eyPFKs0Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=Iu0hNR6vg9kzMmEBcxfyln6nARfm92Y0pkiSUfn3iDcizoVrqiiL7y9n3rW5W4Kyw9VgFOfefsCpb8fTDDs3_vcDuCdQOdQDx7ZPBbUaCyJQqfFWObOqL9aK1QX8xDOwGshO82gMAKAKkMp9mljeQMa1QlQfVk2uZMrPyuh_krZd9T7kP7k4Rdtvf_UXTZD4xZX_dkhGi2pLOZDKcQO85X5gepuOPEuDccJZt2YfKt99AXQJ-kyMzDHjuz5ZurY9S_g02GuMC95n3yF9qXHv3CYgiubdvFPzwFPERiqBNz-pPRforO0Iu7tDQkFydrWXT15NHmeuNFdaS51plBU6MTaR4DZyawfDE_vUa55V3KCxBttCdCuJXP13in6tQsDv5oJU-198Dq_Lxxy2WSIMsp7nsuhePLAVRODLfU953ZeJHSIRNLQE8evT75azmMaEfcIo3RsV8Z4ofdCnlZQcuaAzFCwah-DvROfhogER3ulj5CYMR4Yt9griZcLJhKucnOYabht1O0yDm-QBAGGOOZOTWZs7wUtUe8U9ouOyOs1trOpR0-hJM1r-fayArrg8jczFd7zyNM_SDlkHcqcoHkp-I2zWUDF01vmcJFwHwheIo1wkhKURMpF9CgovP4VwQdCVUyG5fH8zzB1_xWeAI22UyzpQODuNf7eyPFKs0Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/persiana_Soccer/29410" target="_blank">📅 01:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29409">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caQQLwbB8H_0OqSl2Nb64YsayJVSfLWNML9BdcMJjknhadJbMEFc5PgaZX7vXsN_KBfKwyzY_ErrSNzESblDbmU58qPtsypCiEJK9jM8RjlpJnQF3gvS6bEhzg5pLy-GHmXYFaFHvDZeb_mo5SibYq6gTzX23SLZuE73mLWFzhKBFqWJM1Picn4pFGWrNV_ToCQFr5JLOEgej_ioFlgFqO4dJeQ_5bsGmd3dyJdOuCqRFW62XAIg5PnQDoVjn3HheKdrgpUiQO0FHtQEAC7O5E3thKXyWakhS06ZUebGxW01sahHTjk3k0tJEK3EzVWE3SzT23RjqB9WikDGX_NePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛درباره محمد قربانی چون در لیست مهدی تارتار قرار داره باشگاه‌پرسپولیس در نیم فصل بار دیگر برای جذب او اقدام خواهد کرد. رقم تعیین شده برای‌ رضایت‌ نامه قربانی 1.2 میلیون دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/persiana_Soccer/29409" target="_blank">📅 01:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29407">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ZKIsbwe1XKsWFg7jzO_X0XbLRNPtIe3xIO69bMaWAMCSB8DR9QajUDy0IOFK4Yi7EJRdqbR1PCARYUnUPtUR3NV6zRCLyuHrEjzV2CejSRRa1q2koPjYh61MNSfduqD4UODwzQVscownnFdU21JktVpZ3LuNcOy1IXCc3vKMSUrMrJf-mcBfnUVeAnMtAwHLk5pG5LATVW4M9kCYaorN8L_Ah5AnXeUrNc1AR6FcLH9ry5Zn2algkSUegEE3ajnXpaUUlLjdW3reQgLebXaKdPfzUrisiPyO1muu1nvFAkjqL0zdgnW3aNf93_6vgIoAb77-7KZNz55o_4i0Fwmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/persiana_Soccer/29407" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgJMa_nXMuYw1vUDGPH6EK6qZZ3jl4Yu67QizZaZ3_DwhWUnxzu9rejkblV7yu3GRnWiuf8cbdELkb4r7WxZs3115awxkT1_7_XC1GCQlCX0FimMwwnHBM90NqGW2Ac79u4CFqJOepKR-z0DL9P9L0vV7cKB264r-CT2AT3AX9_2kRFX112G6NApVWdp00cIPI1WbPQnef7MGDvJ0LABbg06hAETnI9LcRKEjIHetvb-uvkAY5zpqkAo7PlnIrHxk-mPDov8XqEjbUsGA7AP1S3_NVvVxZl8MD4GYFOKjD975YbO5ZxK6oKSGl0GkBKuMsX1vkbW64wTj-fKhokaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردارزشمندلیورپولی‌ها در آنفیلد تا آتش‌بازی بارسلونا و پاری‌سن‌ژرمن مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/29406" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29405">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWPJMiQd8TszbfIPpxRtijPXHOcmvx3ABt2mmVH3Nt63eTd4juZBBCLxQzLH4rWF5kbmeuMTUHFRD_c174UNuxogUlaSXTLUR1AA-b-6dO5Sy4ViXxZkH1ysK6x1XC_z1VRNtkFhEjTZTBS3SACwB_txzR92jarMEdqdi6lfj8wP35lkNGrcqICueJfN8IupOKWg4rcAIOd8onvFLPINT8M8fMxRRmkC21asou3_u68E3d1cfTweQahYie1BbwjqsDsy5Kmb2Nis_z-0vobl_b7hjOlHawW5iyydmP9fi8ge6KaNMJujyZVd2AtpFTLXo2eZz7mcN8djM6id3DAbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛
شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29405" target="_blank">📅 00:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29404">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29404" target="_blank">📅 00:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29403">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdOzZ_tu4DrFt8nHj8-kxfNRh5qwajORmxfXIAIoDVkToiwP3SJGWeSOe_7nXVv_eARkTDtgl_SMSje6p_h74w99S_H2WV8m2oFGLC1Xk4tqdqw52SCUmsA-I9dKJsvO6CcH5L6ZIRmfDhJre43lQY2d0bL7V7PHmvHQlrHFDy6kFbRpPSACc859GRnmWkxRQrX3CMHprGFtb-G4_GrN3rzafvqgymF6peYHTdKb1gRcKh6dBAfjd7qNB6bVDNJ4T3x8OXg6tixFgrOX1KdSP6WaFZsPsqZ0Jo3hzZL0xqwF8IXVa670FVy3dvWdO4GWve5exaeucyPpneBNmxaKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29403" target="_blank">📅 00:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoQkCs6naySortUDCOUeJgSAaGCn9U-DP53m86nUr2SVoA5Hf4plJFxEB3C7I3bKkQr-RCdn7XDIynQRjj5nGuu0jhWdkRFiEHne0RTuDzXq2_uiu_ub8jQia47zVwywZzAwb0w6VmRTpeY7K0DJKjNKsZNTCJ7uRBi4RXMuPqcfS8WxWtXTgnwNl3-fouQzf31q1L39iEnhxCux05KjeTWCrRuLvw-nN3iH9HBcZswoVtlblfIGIP_VET_zK_UeYiLVHliZ0AJg_rr13pKbxH98DRstQVzACbYJUv1FX39no3Wiv31Ff8s2jsQ1d1YCUg3IsncmFTUaOaziT0UO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29402" target="_blank">📅 00:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29401">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ398qbo-C1PneaLxriVTRaICgBggE1het8uYgAlh7c-Y_zNqZj6aVDb8HeXnk_4M_kisUS4fLE3-sn9m_6ZTXHE8_rgRFIoVzNsI0G5klpxv7-6xEr8HKO8EF7ozVAT5SXd63MG_uOWIOjEMOAV3SA6GWVIPpSOYm3h6Nagjc2F9qi8DKURyYf-MrK-fkJuJBPwtDn8MW9blmN7k-wN72CZY4MfQY_J68zT7UguJxJVpsShxyhcfMWt7HrCFmVScH7me9JwDm3tuGIk7N7mzjU2zfNTZk1zoumgN9Xroyxfn--m-2SVHpg6P3c4yhmhTmAhJ-Dxi1epv3RLr6lRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
طبق گفته اکثر رسانه‌ ها؛ این آخرین فصل حضور ارلینگ هالند در باشگاه منچسترسیتی و لیگ جزیره خواهد بود و در پایان فصل راهی یکی از دو باشگاه رئال مادرید یا بارسلونا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29401" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29400">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a8082900.mp4?token=vOB7Z1uzXphqy3T5Hv4wHUorgVBjE0BVTUa0XoNhx-B_zHTOa8kXusXSIKRu6dDO8YdPQ_-5wwZ_4tCReGAxNS3nfGbT652ls8CpMFnqV6wn1d7TfgWPXNMhyVyfNEW9pENUkNGDlYTiJ_cupof_VehFCvBzDltn-84EkVoZudiLf6mIUN9mAo7q-k9Nj73uWr-YfKMrdzmbgrfrDq5LYF2bL7vx7ZnLViVnWRRZSpsONMgSNATlhjxek8Q-yAguMJkmhyfsMVdj8D_eWHqk10trLcjKhyStd-2MH95J2yqTeneZFgfRs2pD4ifmE3JZH-9Bdxw_Oi2Cq9Fdjw0gFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a8082900.mp4?token=vOB7Z1uzXphqy3T5Hv4wHUorgVBjE0BVTUa0XoNhx-B_zHTOa8kXusXSIKRu6dDO8YdPQ_-5wwZ_4tCReGAxNS3nfGbT652ls8CpMFnqV6wn1d7TfgWPXNMhyVyfNEW9pENUkNGDlYTiJ_cupof_VehFCvBzDltn-84EkVoZudiLf6mIUN9mAo7q-k9Nj73uWr-YfKMrdzmbgrfrDq5LYF2bL7vx7ZnLViVnWRRZSpsONMgSNATlhjxek8Q-yAguMJkmhyfsMVdj8D_eWHqk10trLcjKhyStd-2MH95J2yqTeneZFgfRs2pD4ifmE3JZH-9Bdxw_Oi2Cq9Fdjw0gFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌ازدواج‌محمدپروین‌باآناهیتا درگاهی عمه دنیس اکرت مهاجم ملی پوش استاندارد لیژ از زبان داماد سابق علی پروین: پروین بشدت مخالف بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/29400" target="_blank">📅 23:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29399">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3Pjup110JFz2oL1kQXjDl7s4vnJ67JSbsYqJqMQaNNuDhX0Itau_LRSQ-NuqesMBi97UUrlDoFH91tyiW3ke6Vf8Qp1JqTVSjCWhvZntYuukj1-V0VMuJGokVvuKfnbp0a01H3MlA1fNWRAkLcbuhuVlGpBuzxsaQPFqg08OP9PGGL_YNW2MJA5fa2ulDbuUwhC-Egx1L3PnbvOGkwAVC6bwaFUYxkPpsJib0KhBcv9rLHjNiF4_LcqXtPMAkYeKGwJLAZOD0xIbBHTRlHDfXwTQ7dryaZJ0jomN-43gZ0aulvtRWvO5kPotqUu8nyO9TodKNMFY0nUNZQNpmgwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29399" target="_blank">📅 23:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29398">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3iQ-7J2pu4YEEqh6GYJYJo9kfWjI_DWMWT-3QGxJpa17ml7Ek6zXp10MHT--cnhgC2ohMpbFNhJ6URcWyVmz9dXHh6eXBEG554rXLWV0zy6n420jYHkBPISeREdM7dNSoC77epaFWosg7WCuDVUWBHgZUzUa_Bh_pNgjMRIUop8g-sGAI8A5WZV-a-V2w9vwzO7kOYneieEHJ_AeeAD0kIQm6D2ZObeyzv1SFrd2sXAu_hr4AI1TXNUHDz-RJNX8ZZaAeVrEhD_nx07CnqNKG0aECQaUh5ou7KZAkUbuxW6ZmYBev6lJDWktqDec16B105FOhvZGyYRGB3Bwc08Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29398" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCZr6WL_gvBnH4OqNm7LPvixHJ1MZTSPkhftHp22HWLuOmmi7j6qcnbm1S1hPd1cu7j8ce1hQoN1mwNazH1rgfXmQxKQXF6_YwfdTWP9-f_qq0mzkeT7x-PURsG55CqQMZS6incP53moP7scVJ7R_spGlR0613-KIb78xnHmUA5TWcQxHa-1VzQtPZoKuLjhTAFhV9Hxx5AESwMhRHKrKqHnfhvu7oUCqqDx65m8QF1E-Mkv9zotNogfHMZRJN0JDT0le_hZ34nTZuyYQ69XTTiY1idj1YEn1esioxPIY4Fdfv0PRdQrx51xOSmJnSANDBoxOx42iTKYSTdzt5Psbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نتایج درخشان و خیره کننده بارسلونا مدل هانسی فلیک در این فصل: 5 مسابقه، 5 پیروزی، 22 گل زده، 5 گل خورده، میانگین نمره 9.3 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29397" target="_blank">📅 22:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29396">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEqd3sCGIngRKz8n8WXZonJL0meHp05cswT3v2kDMQGZ-2hxgyClLEVfLm_hiC0EzlcB8ANIimv4MpuWawSe7q0XYFF-KzJ2GXQZf2ldZ3Pf_xTpEFKRQNcvKxWpyJVV_NcwsykU4AVuoml3wGCMqPZbYS2lynbSX4d6f1sDNuy2nHcfX2a02f7diVlXaf4J0BiwNBcBB2IAYhG_ZlABhqYJ7cJ4cyAUjTDleEugyhqDHMUMzzM_CKn0dEQVDROCIISeGkAcNVvjWOHrXGX06sQXI8zbs6WJnKYGO6vf4yL2mWkYTagtcLe2Q6cjgOW92kyGve9a6fbszedD6Iz2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
در هفته اول چمپونزلیگ؛ شاگردان هانسی فلیک درنیوکمپ آتش‌بازی راه انداختن و با نتیجه پر گل 5 بر 1 نماینده هلند رو شکست داد. 22 گل زده در 5 مسابقه؛ عملکرد استثتایی بارسای فلیک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29396" target="_blank">📅 22:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29395">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqbP1qag-8_p3tjciNNBwoZIF8iriCfZmYzd9fymU_zCDQvEieTSY7z0A-_FCDw2Ajio7ac3RfQYjj4VCTX50QZ5vsnwPwrluGqOQYERuurqyLnuIm7C_IGIf2VaPNTtd9wnzHyo-6E9-saYN6yr3BVL3KohS2pOUe0enfhYX4SYui55thVI4LA4QB0uoBgG0-r0sg5xKjuRm0O-7A0Xh8hlebBOtSqE22rnoWrAtUi_hNnJp0nAXiyC1ttPtRuda9wdFEJsygu4PCH9P8EDJHw2lgoj8QZLD_WuI6qx1AsF6RBqkQ3JSnuv4hw5MvuVJHc-rgOLElFf4mRtJiFbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کاشته تماشایی لامین یامال ستاره 19 ساله بارسا در بازی امشب آبی اناری‌ها مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/29395" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=eqAEXLW0BErGv5lOEMaSbOPATxSH8YCS3d6-RN07Rl-03pYaPqTbubJwX-KFGpjQdWlZmsHue6FmS7jwXj9-jYrMCubEoWur-4thOB2Z9n1MrRuzn1LkEAOrmv3Sk43EaL0r0VHtLFyBUeewxQ9bM-usYxX5gHtqCjWEW6e5ORk8c3sErvrbBEsacSrhS55gSacvOh36Xn2aF_Ru7gVNGFtos46JbgFtfKlQqGCZQtUpdzjf_C0PmvGEjA-aVxg_q6_ZZFj56_dhvz-RBIaYETSSFd3WIWJM88Ik9VxwrWBFuK8DgWOmEYcn-ZlhzH9a8zmiAR0PDuRP0SwfJb1yNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=eqAEXLW0BErGv5lOEMaSbOPATxSH8YCS3d6-RN07Rl-03pYaPqTbubJwX-KFGpjQdWlZmsHue6FmS7jwXj9-jYrMCubEoWur-4thOB2Z9n1MrRuzn1LkEAOrmv3Sk43EaL0r0VHtLFyBUeewxQ9bM-usYxX5gHtqCjWEW6e5ORk8c3sErvrbBEsacSrhS55gSacvOh36Xn2aF_Ru7gVNGFtos46JbgFtfKlQqGCZQtUpdzjf_C0PmvGEjA-aVxg_q6_ZZFj56_dhvz-RBIaYETSSFd3WIWJM88Ik9VxwrWBFuK8DgWOmEYcn-ZlhzH9a8zmiAR0PDuRP0SwfJb1yNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
مقایسه‌عملکردکریس‌رونالدو
🆚
لیونل مسی به مناسبت قرارگرفتن لیونل مسی در لیست 30 نفر کاندیدای توپ طلا و غیبت عجیب کریس رونالدو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29394" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=fkDZ3p17jmBSMPE6-EKJ8PkQtVCl8dYNKK87XCIiXnEfUoOyRspnDuLv9IuFC3kiLDFQDfzLYb-aw-v5bfg-s1QaWhO1CrM8UJsIQN8NGbQQBKq56vsTXn40j8qLJ-DyvnpmKePOuq2tHF-JYVfLxLLUaMxvHb965Y-HCjja4lNCDlDMnsc-PlaNh7qQOfHF1NLyfl27_v-OdXIthGOKV_vxGkTSolVJqEVqrlFQhTX0frDnhCNUfsg6422xxGwafS1Bo4-Z0Vygbo3TBcpvhl9lTLTDUCbJpiF2VA8_ox_LToUMa1JrNa1oG_7hz3Lk6xtcF-BFcqflcmDvGqEKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=fkDZ3p17jmBSMPE6-EKJ8PkQtVCl8dYNKK87XCIiXnEfUoOyRspnDuLv9IuFC3kiLDFQDfzLYb-aw-v5bfg-s1QaWhO1CrM8UJsIQN8NGbQQBKq56vsTXn40j8qLJ-DyvnpmKePOuq2tHF-JYVfLxLLUaMxvHb965Y-HCjja4lNCDlDMnsc-PlaNh7qQOfHF1NLyfl27_v-OdXIthGOKV_vxGkTSolVJqEVqrlFQhTX0frDnhCNUfsg6422xxGwafS1Bo4-Z0Vygbo3TBcpvhl9lTLTDUCbJpiF2VA8_ox_LToUMa1JrNa1oG_7hz3Lk6xtcF-BFcqflcmDvGqEKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل‌استثنایی کریم‌آدیمی ستاره 23 ساله تازه وارد بارسلونا در بازی امشب این تیم مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29393" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp-EZwE5c4xOFpmlvSMZi8WyS0ERBzqCZnnTreFKWHZfTOymvigu-j8T3raRh_UEIogPkGd-8b8IlWwRm77SgsGIyYqoQTrlTz1h0Z6T92nDN0pLvt557xYOJphqqbSUqgd30onDLeIbgnN2UlomMsjLPEnZe98kG_6OO0uXaZeAeruIUjT1tJDYfm5HzJqGg1XNjHMkCLg0c8Iyakvp4NK0pNsYhrmZk_UEdvRwYnNJ2xLv2ZVA4G1NzsUWOVeS4jiAPWfF9hJLseIuEKo3ECSCRUZVPggFVhA5ag8Y1lRIUC_TnYS49sbXa8k4vim0-u6seksFdZRM2qlu2bXrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29392" target="_blank">📅 21:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29391">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=E9tri_9pyl2dYglDteHxEiQS8KtK1x4lqLk4qh4zmy9fXeCrDxHFcYlbLoGWg2dnrHtTpLihSBIgKsfWrOHBCP-AHFwH8dE33LFNse8PuMQQ_QWJh2iv8idp107SAjwr1QBe42uWlalQrgBjyCsud9HYqTwDzD9w2YcqpigsI92ISOGjbN1Ums9trV29D9YHhE2Vml0Q1WcB9SwJVINWrBTLuKtYLn8l3TgYssbsVYGM3TTbBDlGQoqaxllzCcu7Mzd94ZyXaGxHwgfedYFCpQmxFYwgzF3c6XKlIKgFP4gWItEP2L1dgazRoE56KMXEgYicMLlcRGqijKq9GHGgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=E9tri_9pyl2dYglDteHxEiQS8KtK1x4lqLk4qh4zmy9fXeCrDxHFcYlbLoGWg2dnrHtTpLihSBIgKsfWrOHBCP-AHFwH8dE33LFNse8PuMQQ_QWJh2iv8idp107SAjwr1QBe42uWlalQrgBjyCsud9HYqTwDzD9w2YcqpigsI92ISOGjbN1Ums9trV29D9YHhE2Vml0Q1WcB9SwJVINWrBTLuKtYLn8l3TgYssbsVYGM3TTbBDlGQoqaxllzCcu7Mzd94ZyXaGxHwgfedYFCpQmxFYwgzF3c6XKlIKgFP4gWItEP2L1dgazRoE56KMXEgYicMLlcRGqijKq9GHGgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آرش فرزین دامادسابق علی‌پروین:
بعد از شش سال جدایی هنوزم لادن پروین رو دوست دارم! بت زدن ‌هام رو بازی‌های فوتبال باعث طلاقم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29391" target="_blank">📅 21:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29390">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqKWIofGEOxn5DqNgtdwUatIScgrfk74Y4B4nMNojrmoomfrLY_1XybXDAdB60oy2wGR8GeRcS3LgAObZV1JplVUXbDBYo7dLhNGL-PC3Wn-eokHonBiuaxOBVgwkcujlLI9NYZ14EskcnH5sDD3f7eF2BRsQTWmSsQeaRI--LLUQh16HYypAuYk4CoCwgYht_VpE6kOp-6PB9614zTAMIeQRAZdfTP6TV6qE76jGRu89ZLJJgE_XZFCtd-4d1sJTGW1tAixcJi-NNO8rxOeSOgq7t1TyR_HDVrfn26GoLVLb19Ql5y3TIWXetK_S5E7PO8XTTv3nV1MQINhPYK-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29390" target="_blank">📅 20:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29389">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/448238a183.mp4?token=OK4wNB36M_Y26TvrcclAwmFEXvoi5hXndpdAVbVvBEj4Ev65GVsiNFL4uLYMIFgmbE5_Te48ikP_xRjq5r_k6_mTycAttXTPNRWRPlZ0qkWYR3Q8mSDNyCm9u8CDviqDTQAVgGiYAqj_c9wKmz4QJxRemLQ2WeIGyksz1uN1xR9SiN9eFYKSfKQXFm0YGZ1n4TMseemmakJ9ANLQf9HbmEaHel1iyA14Iqr6pC87s1wOJuDQ0EIWo8mRxBVICD3-XeizdgDZiMAm9DO03xt5cz41lpuX-J6lXdcCBpLcs2lHO9gpvhS6iYWW6wAdCedaqPPV2Zbc7KFpVp0FEqib8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/448238a183.mp4?token=OK4wNB36M_Y26TvrcclAwmFEXvoi5hXndpdAVbVvBEj4Ev65GVsiNFL4uLYMIFgmbE5_Te48ikP_xRjq5r_k6_mTycAttXTPNRWRPlZ0qkWYR3Q8mSDNyCm9u8CDviqDTQAVgGiYAqj_c9wKmz4QJxRemLQ2WeIGyksz1uN1xR9SiN9eFYKSfKQXFm0YGZ1n4TMseemmakJ9ANLQf9HbmEaHel1iyA14Iqr6pC87s1wOJuDQ0EIWo8mRxBVICD3-XeizdgDZiMAm9DO03xt5cz41lpuX-J6lXdcCBpLcs2lHO9gpvhS6iYWW6wAdCedaqPPV2Zbc7KFpVp0FEqib8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29389" target="_blank">📅 20:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29388">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
#تکمیلی؛ پیج معروف 433 سه پاس گل دیدنی نادر محمدی باپرتاب‌اوت دراین‌فصل رو پست‌کرده و میکل آرتتا روهم تگ خورده که این بازیکن رو بخر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29388" target="_blank">📅 20:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29387">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmBgb5cqfcxRmVD1GyQMdkSPOXiiVdI3Xg5YqyfMIiC4SCaD4YpdINsSb36I8_9tj3UqutXSRuS0tiXaTHa000DTeoXUrpyhk-dFSA7NmATHpdRyx2lWNeRdikfC3O4IUkQyh2oblm_cRIar_Lr0dVFLFH4vcTfupUf-i2PE57M9fDY4miuIrjOh1AmpmsPBK3lUSRsCj-Q_xb87ixuTKP7iJpBPxsAob0kMoF9lc8Ec4N7tKC0Cs4GK9seS8Vwx5wrqs_k4LPEdwj-0gSraEwfNeDTUrvvhk9q6QVincTCupYdCw3sGIoyZChDzdGbHr11y2_FzepHBVsPj2JojXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29387" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29386">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn26b5nCn5YfpH-3ht0rT_XfoSlvzjcnMkyxuWbLUig-WgnUh9otrUqSjbqoYa8p52ic94b2xApak407utl5ntl90E9e_GJIDj5Y_ihmTNE3gK9f37jcCi-pemrdthtRjye32GyBjZjUu4z529p9yhZh6Qg6Bp6Bkn6W3xnqwvWB_Xk1m7pVZyvg6xJDCkIMv7trKFg58chRnmrreCkRiMR8pyVlqrovrnDhoGbnAAs5_F7BGmbtypzY4uYqk5gJcA8wxfSpHQoVM_LudKwrGdP288lb-G8YLag4WZkvEOKV-nNXBh3E3x0HJJa37RtWNC8onqGt-NVCnBmAgXhtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اسماعیل کارتال سرمربی فنرباغچه در نشست خبری قبل از دیدار فردا با آاس رم: «آاس رم فعلی قدرتمند ترین و با کیفیت ترین ترکیب تاریخ این باشگاه است.»
حالا
ترکیب فصل ۲۰۱۵/۱۶
:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29386" target="_blank">📅 19:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29385">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUWvUABtfBpKrMBZ3FuSdnd5K7w4k1cbATIx1GyA3Rjg4enxhm0woPWVs7y7wdAE8hSmQ0ippzatyvifzsbjZzWxsA10HEb-S3dsG52BDQkfPzeUp0kCBKrXRxbW1kohw2PcOD6IrAgW9bAzsINQY8NyDEK9olyWS1HxEh7M0AKCTJZadsns0m4foC7ndfmgrZFYgyBrukGUhiGi4ItJ4D9gZjiVAx-JqIDuW2pAtALknhIKh5Jr9kwDIp1Gkv5k6kCy1SEjIS6na4QGgkzazDjgmLlNwCqPYOLXo1gAAak9Mgx6FSdbJkyz6wr0_oUw_Kh3YxBH1yFZdSMH1_evRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29385" target="_blank">📅 19:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf1gXr8qYZkzxWqwktRqfSA4AqYv22DlIsiqbSMRwdIgZoRfhvDLSe7EVEmZw0kASTkJyak6CIDOOmk2_jv-RExo4cOY7btBp8FXA2Xz0CW_OZlkTJep3Kajl-mI9PDXKvdlugHy91h89XgLkDpXqPuajuW6HZe67ATIY7mQ2EQQcJmEsO7jhlBICCBtWtMyE2yzfR_urorA6F5bWJLM1em_7OaSKB5bAoLVxRsVj95FKjmf-Kv47AA5cg2KUOT1DU79zLYSwb4J9CK1iOrKzr51wtj_IG2dsCb3USNVB_gik1Lr2jk_wn63t0qMsaLx5EJR2nHxajGvzcQU0wW3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29384" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29383">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpjlAofHY88CrTXcCVPfv-ez3zvZqln1qfvEwwMlX84esW3bPa3cJKBcalVo0tJrVPBLktjGWArFGRAzVXByacpq-Yt4kv5dUnvlECxXWSGvpGX2ogOkytWS6y5TjWMfu-ThKP-1_O_JAFO9tl4MGq9Kd_kYkoRiLlQ_uZozqKeqH4Q2JKqLaaDWHOmyMUh7WOIy_oBHisNy2o9HPdIILz6Qus-cMX_OIkGlnAEedeOzTDW-0uF2hn3zBh66exmHht06naPYdwUOedxH5q09OvhlhWWFSsDF7-4wuLzM9KLTC7jh4yyyNqK_uB9HZVPWbuEfwFsfsShgQxKDU0o_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29383" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29382">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6qlPVupJ2FaL-pc5guXXbyy9BJls1AVZ5aJQs_u8MpEUSY-YzMTz2pvyi5CDQ6amXPB0V-YaQM6LvIBbWBw-9Ef9GLxZYFegb8nVI7u90RiZcvowdAgIy8pq74Zei_nBajLejOoHp1huBtkBf25F07DVYPxqZNmClYgMuTQ-lasurRwUD0OjrFk5ZOtPIllF3vYnfi8N25qEiHVrm89JzA0bqrj8XvSDo-3x6yCZxEkSOTm7ZL2nbjWtF8NurKwvOPU4rSjdXPeRq3IwCqz-QHTAdS1CmAjVbLfxyYCvpCPHoEP_iy57Y_B3Fz6RxhV-ILueXs_ZQ5wZ90TI35ijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29382" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29381">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuqcWiICOtsxmR636IQtctkk9n5KL-LI0lyGJ_yqVJHwBtB2OiCgOFfk_kvbQSvAuyGSqlBRN20PauQb8WlJFDq7wRBp8UDyb-bw6yTb2hB6KKCvPTChUvCcq1qiS5DRxJWd7aL_pRUP_yTzDCzcDQDtXLbfU7CPVTJ23EmPK6rYZg2iZWlR3-raowoZMV3ENAeNDCQG0kqfRH9__hlNBx5NdSAV71X1rKJgHPgUn0p69qXpiUbx6RZIYE7F6pWLleJicc7wJ0Dix9V1L7vmijW8VLD7Flm0LZMHo_fM4zNJHyVKFKng_pozBeX3k4eqgQZj-eKrRkd5NcQnx3mEZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
لیونل مسی و کریس رونالدو آمادگی خود را برای حضور در مسابقه خدافظی کارلوس توز در تیم بوکاجونیورز اعلام‌کرده‌اند و بالاخره بعدِ سال‌ها این دو فوق ستاره در یک تیم همتیمی خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29381" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29380">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtgdGoMBbmWG8gaaspmHSo6QqdSXEY0L-p_7nqwm3RVuP-w6lGoEvNg7HLZuB_lQOTasByPEvoz0tWQGoJa8ZLnTu8zPNEzFIc2l1sC1H4z5pWYRKEogSzy5qqdyTDnAHejx_fKWs9MorQafhHTWQ3zGM6_M1QU3nFU6V4w71n7CmLr4s1HvyYqIwHTxsyWm5GoXxCHHPzXJHQqr76iZ5-fOEpOrdg2WJcGGySaalrNC_muFnFv7mjDyMf3w4GJkRm5KP5IM6pD3XEAGl_iqwx8ZeIFsZQ3-X7QGQGoH2v_H6aBvVJiznlmngyWZt3-vJTS_l1BD_LkZWVKLd5ZvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
اتلتیکو مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29380" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29379">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgCdaEDNaMwwbpOYImMWssxb1KjOWBTObqoqKrGaE7LbFLxEqlNQY21N3nSI2XnO2NZG1G-ssdMhy7ZGN9NTjUxreRdlvHfW06u3ck64mCA8rso7KA7U6NvTQIah-pgP-fwAHKEaWRUXnyjF2ZoL3JIbcGW7qWBFVONLeGYzOusooFBtZ2Zakol_0y-8IXbB5yNIfFjsQ4UH1HyaHZmznLGjeVr9bMcn9eQXAwcAHnmWFfCHEOA1UI6zNuZwY6hVd5Pdcwl2adc-FwjHOSQqRuTuDbS7KGIBC0_f4vzoVy_HeBwNiVDIlQHvtpqNO-S3_4gATF9S-7SkJUFo7YHI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛
مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29379" target="_blank">📅 17:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29378">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Md2oZ9p43tiId7u4Y6G45YirBBaFvLoO0sx5f81GjwhBaIxFI__T3K8wyOya6xQj_psdFSkBmFe6QE9ten0-bWv_IvIj8nwxjZCmRPgp0LXguxC-pT8OlgAEwkkZZKS4G9E5DIgkE-qPQjQ-Vuz_Q4o35XYtuHsedgNKciu4CRN3vJmbom1Y-17VAIAms98v_rVXy_7YLsidmrI9iL1eEeWFuZbXqooS18DlkyY2U3hRan8W29SKttdtP2Q5lygSOo9_-EEm-Ws35ubsX-_iiE1LM4lDABMQkfE2DsF2wvTFJo5tTeJXk54PX47FFVmaCt6Jd-folRzTBin5XHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
💵
قیمت‌های‌احتمالی‌آیفون 18 که قراره امشب حوالی ساعت20:30 بوقت‌ایران ازش رونمایی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29378" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnHylp8_Gj87ScY60G6ofq9YExmnPk4eAhIbmejw-RO4E9VnMFo8xxzrZuWhcHxmuouT9s6H0zYV6DiRTeT7wUYI85UJ21urPPi0ZohPQlsPgwPGqkFAjnw23Ck7BwsrhaTjoNvbzSp_KKggZeWi_qQXJ4Wm6HIGEXAxzf9dmXS8Z7adK2saHuNZr76Elk_8Vis6Kv4QS1lhyBATuWkbBogAYmClUWMbInqPZ0Zc5KhMOoV_NMDNnh6CkffVqeOT74qzaXCYCUFCt6AKNZj4-twx_Qq8KjQCdBOAe5Gb1l6f2-bQJzUf0PnrBM-2HLnAeiu1lVMthgedifF-sotFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی جالب پاریسی‌ها در تاریخ توپ طلا؛ نامزدهای نهایی کسب‌توپ‌طلای فصل گذشته فوتبال اعلام شدند و در اتفاقی جالب، پاری سن‌ ژرمن، فاتح لیگ قهرمانان با ده نامزد رکوردار شد. تا کنون هییچ باشگاهی در یک سال ده نامزد دراین‌مراسم نداشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29377" target="_blank">📅 17:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgH1-nLZjJwAHPZPpwOD-UnjcBMCWMwuUHctd_rbYncdWhSR19emj2ZTeFU3U37pzQBxMLbAONxW-iVX33qXcJCtJmEEHztelA6Yjhg0n2XVBaZ4RSevQkeMpL9QWxaDPJIz3cNi8FjiLLMzH3_8jBZ-oV80hqxOTftZQi989JEHJHEZnjBkdwiAoR8OtQ3P3UmShe8gXdzQCxZ6751z44UMqOBjsMsCH0YBZOjWFlPtdP2xrVvSU-iTVTfJTCoBmJ6cYdz_ar0xs6NM7ICno6GNhnxVjfCqtKwWSQn4xyQbD68lLIylpW2R2Sp1jq20cPZYHs6HyQk1y0lXyrcL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29376" target="_blank">📅 17:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUzoLwOqlbE7SqoLmlEczM0wVe71hAgktrEmiRxH4M5gOIZqxNW5AIqdu34aAhBFaTEVg5JSEbnlYUL4YmDtIqJeOIjxS2e8GkLgHJNUJzEoTXQDE5MtD9KaLtmU6vts5IIE6upDuHKurqf7aSomPNNqRh5fmGxlGr_PE3hGQB53xccQDZibZOp6tkuHthnSY5KP11Zb3vSRNsYSj1-W5RrWqznfm6vNnyrgkezzCKLn4b2xnns4kVUWF41Moty3e9417SmIsS0qExVTRM0l6Rewz82XaUrKM-e3z7xjMp_FeX-IAulIx6_icRxRNGCHNwjO5QiScM4VeLG0NAqtTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29375" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp1W281UNxaMZ7ELsK9EJ-nYQxnWWBZlVUcYse-0QhR4FWPHF-DPOFF621NIGaY3UlENUvYK4JqEEL9GhLaEtDuNRChyX1iAskdQQSrbG7fNriIdK25hPMcu6a7YV6xuo33Dk9EOyD6RF95h3E8NKtKllMLxMXojv8muQ0E5b6xUOiqT6LCBl56Nmy5RftSZwy9BeqdDlzeoJGHZgXsgp9yjeYNdEXkl1ymm7st-nbjVbM-Vya-o_eFsC-ccydCCxio5bcRwdJ42A_bbYnzh6Jtns4a3rr75BHh27irOMGu9Z3FyzemQ5nLNqgDo-NpD4HR93-UZlPW3UKHM6ocNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29374" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6wQtOGzrezlnOb-peA95qwkiCYRMCHG5qnfIZ7yEkjgykoanOYqzPCTZNi0pM5UcCkPQbyzLe65j-6DXZPrYAHQ5_43Q5ByghfBTrwEfTgXQjaf5VlRA_IVMFqgfYAdJkpyQY6AdWCqNwMI6386CI4x697vizA_UaYYP_wx7fK72chrQ6pKqRs57n-UanqXfPT2i8jOYKIOB14qxo1mw7A3cxc0nGe2tY1q1-QL3O52W4R_QWBkF83Ej6y3CZxDD-p_NDp2s0pLy-8jKQ2cO5SWtChEB2pYZBAJhcfsfAKb5XW3l1lDYJ3I93PZnPNjxXkdTlXEcqXui_NYpLZ7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگار معروف و محبوب شبکه DAZN ایتالیا که مسابقات جذاب سری‌آ پوشش میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29373" target="_blank">📅 15:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkN4V_hBCtiA5JmDNoIcP5_gwLiorn8_6oagC-cM3HyyLzngUq9GU5X8pCICGyoPBhyBwC2IABxhUk5t5gB38s7GIEfYIL6Kgt4KvSFW66zLhH8e2gQJPYZTDkN-4okAciDa33tYjJi90k9-24LryHxNb3bpS6MJ-t6qdQ9D5xbO9CXb5ZSSmCwwKT5TlAbUwDDwNSekCPNGId49IwQw-LDEsKaiSD6ZlJ5UqItVJu4H_1ibYgmfzEb2pGFFhGmGlttmOzNsebMdvHc7T2uskCnze-qxDY-KNOS8XJb5sE9Zdtjvlur6x7-BR2S7i3JU9QEdOgCnogScd3IQsN_ESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
داورهای هفته هفتم لیگ برتر مشخص شدند؛
وحید کاطمی مسابقه استقلال
🆚
پیکان رو قضاوت خواهد کرد و بیژن‌حیدری‌ مسابقه روزیکشنبه دوتیم پرسپولیس
🆚
خیبر در خرم آباد سوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29372" target="_blank">📅 15:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmmVhmOEIxJD4fb-FYSyNikTiKwAqlJ5OVlFD7QoGdw8MUozbP1rxwlA7EqXZ-QKdtrVS4EU2qFj2LltGMSrtnq7gsPZcLLBIGGW9ZWThuD4ILCzsVGRk7WuAo20gvJ46gEKmUSbTMFEcwrOf5MZZWauYAnKqJD224_X9ktYsicZUrpie4IoeMV_iWMjZBkjOq_sADLKtQTC1IZuJHUAwvFyK8n_GRy6XoqnnOPyo0kisKMrNhv1HOhSiXWz2EsJOCWfkiU9R8JLevsP4n_mrjhS7Fl2Cg8hc9fb3xxXgPQIhVpnndMU0Ml-IXhxtjcMVNo0dzVsCxDeXzbIQeYgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29371" target="_blank">📅 15:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sYGi0rb41xcf-lUr3I6-OXoOC8UMOpXA_yzSmnggHj2BZUmu9dw1pQYppxZo17XkxwJ4Zdtr-4paFVYWviY6WQ0xK1p87sHVDAyW0xIt_iKEIueL4BaVrmP8rHjD6jOaU_c_tsVls5YFFjoKieJZkaJbJu-EHIITEKj33dlwsK_e9O1Oy-4TudagHXteXYrKOTmZjALfwzxbUziBSRw-_tM8lbdW61_eGY7Uvs8GCC8fgyxAMkVnnysinsolfnFmbXQkzDJ7KmQt1ekDUyHQ1ysyH1jr93nziBVax93Jzscgj6JwSu9JACnTfOFFibAe27k4UVvOS_59rohPs3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29370" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29369">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqTttjTMdyqmheATdZjDHvByEcmQ_OjOQ79UsyhwpnS7wKR6AkGaq65jI8cDARh0cEyJdJ7bLQ65ralqKpoODBSfzsAlashu6AA4gwtKT_tP-DarJ4qdYpJ2sJ03_SxYvt-Ldw1ufN4o05246llNK5QB7xtDdkXC-6uWdQ31UiVc-puVhHfI9Pm5fq2W_TkqjA0zupSI7E9mG3FIHs1C3TrFj-Bc12gDYuLNoNmI2R1ch2ue4pHQWIRKYVZYKstiStQ6mkEA619CDkYw7ErItOYQwDlMwB_0iN71I7mljBcDHLmnclpeQ9qgpZ4Qw7cmQLxpTBlGrdrSTne5Ox_0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29369" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29368">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xkz5p1mxbggvXW1RMgzivXZTchIoobYMWmZ3QBhbx2dTEqVDh7FToGjcpT9uLeB2G1pF0NugB578Lj2IhjrGljhs2a93VumAWQgYpdobYh_Po6jsvHS4qnAI6AOPRbVVDtzVTtpIlkFKyc5V_WxZ-7DnL_g2A-8SUDUw7sreheqtvvEQm5tCihty9a922DuVAihz3NiM8QPNW7RKVAz2zCL5exOp2ruO-pLggS3sgmzh9_elmslpv9eVXEBTZlcUIHo3ubr2eM1EZlvFdUjAIqAZVCWzFNzQY6PzuBE2WsCveiE30O8flDCs0vuhwNswWZ7FVtZ-bUtRLTScMPerEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
لیونل مسی آرژانتینی ساعاتی قبل با خرید 100% سهام‌باشگاه‌الدنسه‌مالک این باشگاه اسپانیایی تو دسته‌دوم لالیگا شد. چقد لوگوشون‌شبیه بارسائه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29368" target="_blank">📅 14:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29367">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4A44-qUdOBgfqxzjV4AWn7fOS66u_XATEBoGj1gyJyKLmgn4p0leGQSj7L9IJROGN72AIPb4VV9hii5bMkbOm1bFi8AI9eOjXKMpn4r9nZNcOtl1nsCgwZY8mD-dQAeEOOAXf8yHfQhMPJFBJ8zgW6X9Ruix3WMUnKewVPFFQAiHrjzUtCvnbI1E2gT3WG9LQw7VeJbNyz0fGGVGhRZtE0aBEkxCD1Sz-h4OpNNcuJ_iJYetjjkhBR7F4eP5jhdtdSeoCUVI1RLVi8tdZgqupPgysW-A00BEUA-q_0llPZ_fY-ONYSD14hpUEamTBUTgIj8WhSCfUU3rta248z6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29367" target="_blank">📅 14:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29366">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG4EmmMUAYNgt2lC3BwzH_AVAiGAgash5iKknfBBi0TqqFt3mSfYD31KycdSG6JFFpUNDtyvlFaHKSB41IgmQ_tSi8nZkLlWkuY-K5yJWDoghY-I7GxVEUivgevN6odS60c3nSvLxtMUY7ky288DGK2PGu-M4Pn2MHeZDQLZI03IvEEUjiJjFB2IXJ0jwXvgcCZRSIVJ-7XcjcPm1MaC7xx3Dmfdt5b_E_z0yXSqEqTklcQhaJkqOQIpA8BPY_teHFmPD0kNyzuqTkUzGYH-BIpcm9G2OJp6qxaCcxF8ob5ESSv9_TJEoKox8i1ZEZT9VHBveJOubbemSojKJHlhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌‌ملت‌‌های‌والیبال‌آسیا؛
تیم ملی والیبال ایران درسومین‌مسابقه خود درقهرمانی مردان آسیا 2026 بانتیجه‌سه‌بریک موفق به شکست چین شد. شاگردان پیاتزا بااین‌ پیروزی درجدول کلی‌مسابقات در جایگاه دوم قرار گرفتند و در مرحله یک چهارم نهایی رقابت ها به مصاف تیم ملی چین تایپه خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29366" target="_blank">📅 13:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29365">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=Fvjxa76m1RhC2paxc6CVA9Ms4i5TgdOMmXhE8vEHJuuaxN9P4BEGUufvfEP9WFLSd4hZPKntq-u55thHIjiuok5IaI7tYhlREhAXMZ3BHKh6Hd-AjfMYR_Anz5qvuNFY071GsI1HzJbDqpwHGzM0Gp__RY39nJcyB4yekkERVg1CuMtiEYVPVUjZ-TUdVXDvedQU9KP9XmcHgAgswZT_n7DPm9okTa9sCUFhBAQg8nIxMtWjD8bIsmxuoMiri_vZp5QLxk2bgTgQ_QBWximlvZv9-P4wSzTxMipr90JhWz5I4nb3Vmlx12ik7u_ToPMDnwlSgSq23TlCPRa0Hv_yF2ZPEXowyZgPXR8c5bE0fgCaqs3cNQ30nmKhSneEuewX393BWlW1gqxM-QoMfp9v5GKm7oAE6n8M8cnexRpRdpIdNB-bOq6JUNWeC0Er1_-RB3c9aOV__cLuYIWebs-iahhvwu-FPjVsKNsSR8I4WgalE7cXOmcgrMh7d3rvl-EqGvLRhJPzlTQ1jrQUL02ee-ZTk4C2QvVuHFFVPA91x7BCb4evZpPpDVXJHWRtw8X7nzfmFTtt6Q02idv42t9Uyzep8f3HOnnSM8nkpc0lpB1oQZ95NETtlEwUYTuL2AXKUCnjOFqpkhOOdaXxXbs0hWJihwR0DvXEXkzbtFMKllk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=Fvjxa76m1RhC2paxc6CVA9Ms4i5TgdOMmXhE8vEHJuuaxN9P4BEGUufvfEP9WFLSd4hZPKntq-u55thHIjiuok5IaI7tYhlREhAXMZ3BHKh6Hd-AjfMYR_Anz5qvuNFY071GsI1HzJbDqpwHGzM0Gp__RY39nJcyB4yekkERVg1CuMtiEYVPVUjZ-TUdVXDvedQU9KP9XmcHgAgswZT_n7DPm9okTa9sCUFhBAQg8nIxMtWjD8bIsmxuoMiri_vZp5QLxk2bgTgQ_QBWximlvZv9-P4wSzTxMipr90JhWz5I4nb3Vmlx12ik7u_ToPMDnwlSgSq23TlCPRa0Hv_yF2ZPEXowyZgPXR8c5bE0fgCaqs3cNQ30nmKhSneEuewX393BWlW1gqxM-QoMfp9v5GKm7oAE6n8M8cnexRpRdpIdNB-bOq6JUNWeC0Er1_-RB3c9aOV__cLuYIWebs-iahhvwu-FPjVsKNsSR8I4WgalE7cXOmcgrMh7d3rvl-EqGvLRhJPzlTQ1jrQUL02ee-ZTk4C2QvVuHFFVPA91x7BCb4evZpPpDVXJHWRtw8X7nzfmFTtt6Q02idv42t9Uyzep8f3HOnnSM8nkpc0lpB1oQZ95NETtlEwUYTuL2AXKUCnjOFqpkhOOdaXxXbs0hWJihwR0DvXEXkzbtFMKllk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز جذاب و دیدنی دیدار هفته اخیر آرسنال و چلسی؛ میکل آرتتا به‌این شکل تونست ژابی رو ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29365" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29364">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=OcdvnJo4mIw07bEWqcxzXYy_vdE0EPhIF_X1yh0AMtg2e-IwoFgLhmGIX4jIUKB3s40qCjl94Jrac-qbXmoO6sZQZJ-KfK0QbZEdcnVnAczryY4_0GA_6V2qLkz3aE_B4uS9ra3ug2KYza_XMM1DdtOdtM_rJUQRCobNGe-8bPBkeXmQEIwuNVaIdrQcZE4d1TIMPklFZOdm2_iVWiLyCvYfCzg78H56b-8RfO2QalL0jUzjkBczXG5TvKGxsILC5w1tq_FDWGVa-IwU8qhzKA33IPKcKoCFfDSqIoZ4bUQbEU6otl47Hpn2TnudaE1nBJjWE3EMXX5dYMQHpBtCuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=OcdvnJo4mIw07bEWqcxzXYy_vdE0EPhIF_X1yh0AMtg2e-IwoFgLhmGIX4jIUKB3s40qCjl94Jrac-qbXmoO6sZQZJ-KfK0QbZEdcnVnAczryY4_0GA_6V2qLkz3aE_B4uS9ra3ug2KYza_XMM1DdtOdtM_rJUQRCobNGe-8bPBkeXmQEIwuNVaIdrQcZE4d1TIMPklFZOdm2_iVWiLyCvYfCzg78H56b-8RfO2QalL0jUzjkBczXG5TvKGxsILC5w1tq_FDWGVa-IwU8qhzKA33IPKcKoCFfDSqIoZ4bUQbEU6otl47Hpn2TnudaE1nBJjWE3EMXX5dYMQHpBtCuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
فاصله‌امتیازات دوتیم استقلال و پرسپولیس در تمام ادوار لیگ‌برتر به‌کمترین حالت خود در تاریخ 25 ساله برگزاری این مسابقات رسیده است؛ تا پایان هفته‌ششم لیگ بیست‌‌ششم استقلال تنهابایک امتیاز پیشه. نکته مهم این که در محاسبه امتیازات، کسر امتیازهای انضباطی اعمال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29364" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29362">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=f4q4c4E1fRuYYFiX0ibs0cMi5JZa2zV9LQg4kY0xroZf1wnc_C8yro8ICNZHJVGguQ6iaTbJaoGpN56eV-1N_bWb6qiKnMS_L-seLO5EmuZb2f6Obo5xJInkJ_uqNZsPJyA6F4YVSMQ0e2CvmeowDimHIvMX8RjJ8lUU9pLL7U-DoVKMHMQ6L9Zo5jZy-MKQP_CWyX5aROF1kej2586XtPzGgS4FDkTcba484YAfCbGmP92IYtl2cqN9zl12DVxU4v-WqF8Ec83mUn3LDcEMsbe_MnxAdlZcN3LCh6wpVEoY9GtJ-YG6W4nQi9Xg1YnSVqUELml9lzugyb_qJMH8Ex7qqK3TOsRG9gbkqGxszhdMAwvceKixfcyQCUIxYSpmNXp1MvUsm_A3XmMj7hh4y6keUxrc0Eji2ssvXyQqzyLUoMK4M8gNj7lGZj6gAdAB6bFDC6jd00fdPKyPCTE6el3iWwWNFJaH4pR8A-vw4BJDkfNnc6UIhiEU0t_9jB7aKqNl_FtW_MJpmRwV8O0MDsyRAkZ8OAaEoTGiWlmkT25hltmjcjxT0LRcA3iBkKN4m0b_V2YnFEhUrFRQwJjApRI_QQO62Yx-U0MfPozOPtlcWLlFlFgBnQYyD1JIDo3-TzefOFvp7kM8A2S_jZ2TR8sjZxfxU0v9a6YoozZv6ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=f4q4c4E1fRuYYFiX0ibs0cMi5JZa2zV9LQg4kY0xroZf1wnc_C8yro8ICNZHJVGguQ6iaTbJaoGpN56eV-1N_bWb6qiKnMS_L-seLO5EmuZb2f6Obo5xJInkJ_uqNZsPJyA6F4YVSMQ0e2CvmeowDimHIvMX8RjJ8lUU9pLL7U-DoVKMHMQ6L9Zo5jZy-MKQP_CWyX5aROF1kej2586XtPzGgS4FDkTcba484YAfCbGmP92IYtl2cqN9zl12DVxU4v-WqF8Ec83mUn3LDcEMsbe_MnxAdlZcN3LCh6wpVEoY9GtJ-YG6W4nQi9Xg1YnSVqUELml9lzugyb_qJMH8Ex7qqK3TOsRG9gbkqGxszhdMAwvceKixfcyQCUIxYSpmNXp1MvUsm_A3XmMj7hh4y6keUxrc0Eji2ssvXyQqzyLUoMK4M8gNj7lGZj6gAdAB6bFDC6jd00fdPKyPCTE6el3iWwWNFJaH4pR8A-vw4BJDkfNnc6UIhiEU0t_9jB7aKqNl_FtW_MJpmRwV8O0MDsyRAkZ8OAaEoTGiWlmkT25hltmjcjxT0LRcA3iBkKN4m0b_V2YnFEhUrFRQwJjApRI_QQO62Yx-U0MfPozOPtlcWLlFlFgBnQYyD1JIDo3-TzefOFvp7kM8A2S_jZ2TR8sjZxfxU0v9a6YoozZv6ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
عملکرد 9 فوق ستاره‌ درفصل‌گذشته رقابت‌ها که در لیست 30 نفره کاندیدای توپ طلا قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29362" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29361">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732028b756.mp4?token=kTxzZqIIrQJ7WQv-iurD_QyCiKBcfRbFOcUMh-mYc6Y4vUohPWwuWoeTpfJqWwnGuE-ZHwkHVPfLd7Y4JT0vGo_9RFXrFnXMc8HrCq2R7cLgMCNuaRSBXaYN7Zf6pDYnIMikwxS-OPZgBfhJxh17oBGgKdJBDI7Op08JFgVa8R0-v9qztWUtZWsBSkV30O89DqeN2XhttLFgOuOOcwzfmGl_B-aMzaUYQSWDVQHYQ8e0FN8pu9BB4XogRPob6aneHgl_ggcqihIq5_mjLCoC7dOpxQypbBPwHFQMDpEk2C_1hG9x9jGKPuDcKh_ZJ_076OwhHONU9TQRySZebqIvhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732028b756.mp4?token=kTxzZqIIrQJ7WQv-iurD_QyCiKBcfRbFOcUMh-mYc6Y4vUohPWwuWoeTpfJqWwnGuE-ZHwkHVPfLd7Y4JT0vGo_9RFXrFnXMc8HrCq2R7cLgMCNuaRSBXaYN7Zf6pDYnIMikwxS-OPZgBfhJxh17oBGgKdJBDI7Op08JFgVa8R0-v9qztWUtZWsBSkV30O89DqeN2XhttLFgOuOOcwzfmGl_B-aMzaUYQSWDVQHYQ8e0FN8pu9BB4XogRPob6aneHgl_ggcqihIq5_mjLCoC7dOpxQypbBPwHFQMDpEk2C_1hG9x9jGKPuDcKh_ZJ_076OwhHONU9TQRySZebqIvhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29361" target="_blank">📅 12:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29360">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7Q1volQFRNEa-GVqWDPNEiK-oOKVnw8bDKqoAM2Y4v3F1roNd7FyFkOxxyQUzTDGSwnJfZT-yu4KXEnvPwiqeL0HY0iY4TUQlAXuXy_QE2kX7WA2_wtXEfewCkcbxJMT9RK6pTlU-j_d8WEQnRgwQpEXeItp2dmywxwosRKKQcd-YhjsuDdgF_khWvgtAIjealGzuGT6L5jgtwG0hHH51SnSDRE7-988kc6vaivztnLRx82BlX4WNR4LRTBsJ66kDLPv9fo8GI-IsfPz9b0ET2OhkckwF9WSfCAG3_CY-arxQP7ZndPK1ZzZszNvwqBlmDWP1s_wAeV-xpNxKksbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برسی عملکرد خیره کننده رافینیا دیاز ستاره برزیلی بارسا درفصل‌گذشته‌رقابت‌ها که یکی از بزرگ ترین غایبان لیست نهایی 30 نفره کاندید های جایزه توپ طلا در سال 2026 به شمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29360" target="_blank">📅 12:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29359">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb5FKcK2pX0pV79US-XIX9pdWkEV6MO3rl2rItbhzVCmST5QkOCjca1WMsXLWn3mnVowV-lc-ZnwZW30fxjgnbimUXp7WX8BLijFNPYjToLOdBUNdfQVt6XtZ2UvO46jptbNfwVobvpVMk4k2pqgb8qoyc78CFpML1I_WJT8-ZUEnDxeyD0dHaX-rdUBYCPqD1jjTzBG9HaJ_4Ao36A4K-Bm2F-1T0FpG93j-Aq6DpsTNXEJaOBpaDA3Cf0YrxjZoMFcCq-dYfUEt-eB2NKoiPT2Q-N1InkOFaMnRasLkiYu2M9dl25PoVusQtOcIZf4E5YpBbBwo6xdkjTf1IXVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29359" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29358">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClvC6YXRNsh_VbzFtkZ3c9-K_waS4yMf9lCgwA2mZlW5GSGKV68RbSgYwFrE8QEvxm5KJqdEBqiYAZGDAtp4Q2kLzl9ssY2rfVDuxMF6UFwSl_1oaU2fWhNf8vaqEZLwkEYRuVn5x_bcXqEiNJeNahUf0SkXrGi4Zky5DF8UEcPypb3DYFb644FvgvO8q7t2S95TObROFMyJlEfrm6UHOAsZZ76J5y39HHMC6heZ1rfwvtDP3WOcMspCI6bcozTVzC7Z9mCxk0deoJfsrzA9QG4pzWt9DhjuTA3akWAcAoe_KvKYfGnF1XkdS5-OnjNs7S1DPsLd3n1rpbsbfL3tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29358" target="_blank">📅 11:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29357">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8fVQUj104LI6nrJyPTkW6QACh9v4L7a3YYzWJ36E68yTIS4uJiRb2VkzFyDssSXNFbPshGuvQw4tYSebZEskvHLJsb0z6IrRuKmSkNLV0eXuvL4seBGuEXEuXQu3vUjUi_o0nzFA67qAt9W-gO5ez67s3A4pzKug1y7s8ynrx-6VjqSZttqc1b_kiVciNm__f_vPSqsmf8zT8Q0g5IK1-RIie5HGUQkJL9Ki4xoxQ_Van-tl23FZcTzgW95sP2TAm6BTlZJzOWpZWH4doBTQ8Odw_0uaJW6_ER3sqC1EIUjSCtGYnZnrDLyDLQxIRX-HuW0Ji8Ay8PJoiiS42fzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29357" target="_blank">📅 11:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29356">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imo_9u-1HlZ-zpk4FyAoGrPTPjFSBTenf8C4xsbRsa4jwNFzo2EFQ04CCFlMxovZwmq9w2DMItRk3sGjh6D_vehRl4UA1Q8gUm70UKIEv6KCqbfcoxybPq7_k3_DOZgyqTgERiLf11V5wC5MzNyZ6gM9WQs8_Y-ggAf590Vt7FkBzT2WXmnMjsF4KRwLQDjjKd1fNUOejUypu3YGE2wFcmS3HdFx_4jWwnnGLk35auh53tUFzWrB3IkbEV_o_vfEP3VYLqC6SnuJrjmopsR3mdp3Ic9T-x98a-5B0u_bkmxm8HwfD1C2Cp1Dd4l7UcHMFlm6UvzTDSYKQV1KIreu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛
خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29356" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29355">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqzXl8ZxGs7hv1wovNxr4mRmC-j_Vmw0kHWWVDFQipTviVrksNDueATG4WLYABdkcaP5JvyIjAc339949jKH4ARqAEhC8ajbEGSOcWVnjUKXbRtbjxtk8ZQdXg3roDcB1FsalA-gT48-jBP_4RaBvgOqQQdgDH9iPQGRI2IfrLBgarfbNOVocO2Ny4f6M5YIySTI6X8I8u9xor7ptuzBYGXEegsFQvc_MbI5PxrVafug7E4tZ2MU2NgohpS_47XdGxzkIMy_S8pZm3X5Y8wFGi5yX4pvTabQTA-MyM6-hKmvJK-uH3q2E2IwvoOfzI5_LlNpMxs9UJD6Yu_bHyoxTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی مهاجم ۲۰ ساله پرسپولیس با دو گلی که این فصل به ثمر رساند به دومین گلزن جوان تاریخ این باشگاه با حداقل دو گل تبدیل شد. مهرداد اولادی با ۱۹ سال و ۶ ماه و یک روز، تنها بازیکنیه که پیش از ۲۰ سالگی به ۲ گل برای پرسپولیس رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29355" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29354">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=PuxthvLSDU7Ahh8dCUNL2SVRq5zIKwnkPyATgJnAX8pYJhoKofcp2KmC0GZ-WB43EDfdldGAywTWZjVLgd_40tDW7IRxzA3Eg0ORDvuzkv3xncO96cRHMPZy8UqJk14jaE0LfdGkAvVM6WKcP02P9QSu9cirTPj1dBgZuRJSM-v0eVJL06q6lSgkeocIUFt8J20yUZc8HyQH2e8zpsn5JyFU2L7-16O8mUFQLnTXo3MPrZwoFzYa3GsrgM93DtH5LlCAL0fjivSgW92_jvcj9hpuLz8Wz8qvSFGlZF8sgN8Rt3XfrkMopE-zoqcEfWuZ7JKxKNcdo17_01vlAOiecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=PuxthvLSDU7Ahh8dCUNL2SVRq5zIKwnkPyATgJnAX8pYJhoKofcp2KmC0GZ-WB43EDfdldGAywTWZjVLgd_40tDW7IRxzA3Eg0ORDvuzkv3xncO96cRHMPZy8UqJk14jaE0LfdGkAvVM6WKcP02P9QSu9cirTPj1dBgZuRJSM-v0eVJL06q6lSgkeocIUFt8J20yUZc8HyQH2e8zpsn5JyFU2L7-16O8mUFQLnTXo3MPrZwoFzYa3GsrgM93DtH5LlCAL0fjivSgW92_jvcj9hpuLz8Wz8qvSFGlZF8sgN8Rt3XfrkMopE-zoqcEfWuZ7JKxKNcdo17_01vlAOiecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت تمام قد خوزه مورینیو از فده والورده؛
جایزه‌بهترین‌بازیکن زمین باید به‌کورتوا میرسید فک کنم اهداکننده‌جایزه گل والورده رو دید و بقیه بازی رو خوابید با این حال فده هم خوب بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29354" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29353">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpMYyT-I0lVxZZIvT6R1DsDEqNA6ubfeeETRejL_8yesg4L5kK98fcDQz1tE-ykzcfrixd02k6FjzjUfCfnLqrO1kWVGeChSFtlrj4V0jbLRaAalhxv5A26c5I2RiEvdXwQ9DfNDONup0eKseOW3txSMsSBd9p9-jVh3Kop_bd8gO0J5BMBEwGhh2PZcfQjXFZsHVxBGg0Ua2jnyGkT-tvChVMQ9TqZ9el7y7x-B9Ih87ewEcn3sbbIjOGAiW-UqZ_g7zoLVzm85LPxhMAXE4VjJCEvQ7WKuZ1x0lkgP_XHkvbow2vW42jDvWu3nRSeiEQqwXs3olyowVsgckjx_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛بعداز درخشش ادامه‌دار نادر محمدی در لیگ‌یک‌روسیه و لینک‌کردن او به آرسنال توسط رسانه 433؛ این‌بار نشریه سان گفته میکل آرتتا اگه قهرمانی UCL رو میخواد باید نادر محمدی رو در ژانویه جذب کنه! قطعا درهر بازی 3 4 پاس گل ثبت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29353" target="_blank">📅 09:49 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
