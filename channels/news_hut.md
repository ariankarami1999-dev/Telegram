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
<img src="https://cdn4.telesco.pe/file/qj2z_LIJ9KATlMPj7pry0Pnn1SfbZ2jHkyQxAypfrH6NzFRfQZ4_Jjc2h0AZl9ijfheSneknI7j_VT5lA4lxvzVta0vnSycXceblP6G60uAgKd21SzZpn9k08clo2VqOhfsjQrVLbnstYa4mshxcpwYdfemONtY_t-Txyog0LfRHvUSrJ2p79QUo7TeTEP_IGg1E1Iv4uv-LuS5tX38sv3VDCqoxVSKBpZYLSY2qpnbXslDN_vzVCS5gbH6tSwmoymxInYUdPE7JCutYaqjihcXP_jm51LZOsG06YiiXkYW4F9KjVUTbA5DhgBbLwqvjiOjdHFXLzh7ZHlBRrg1asA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-65524">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=rzrZ44NUsa55ziP7hUbDTmqgtlLo7dBvgyJm4D47uiPJLZjcGFRB97chKu4ee8iftBfzv8uCSoPDr32SJMzLZ3I4H_cLL9hgyVbyRNR916WTDd5eik94D2-1_T59D4g5Dxz3dLoXIUPFtUwjW1T2fiVJlth0piB2VvsM5Nee25rOeS1F-jsYVmzDON_d0anToM7KDGmjW9iLo5xYx_jnLOoEoFkpoNm-3M0o57S0m5sRODS_CSJjb2Dkh_QpNSjq9hGrb55sX6CDaql2uvHzqchHijLveylzxAS9OEzPhcrs9EGYTE9peOdVQRLgT8c2Z_DaRHfA7BZaqN2GN2DWO0ejYw8LgAE-_J8-uj9n7RfJW_pebnyZbr5-vMkWsQGiahcPKFLzLzqobWTdn_KVtzykusuGsznfOMP0YREkb0AnG3KpbhZbQYyIHbEyob8_yd-eLvThTbtBPgkYccj4t3k12QDWjFAanMaFXjLehl617ju4PZtIHllKL7ISwgl9NJhtvuKpCjaFdZ9lW6GBdjr9g8r2LIKUMtTIXdkeNvy4p1iSUp51NQ-hriaW2Op7n5tV4Bw5-zlgljc5NQyJnFEqSm5YfTch0qbdZviTl3-RxPXH_D5Z0tkmIeMdYVYOgqFCPznyKM-4ZuQIiBX_SZZsoI-KcsH6sATu0knP-j0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=rzrZ44NUsa55ziP7hUbDTmqgtlLo7dBvgyJm4D47uiPJLZjcGFRB97chKu4ee8iftBfzv8uCSoPDr32SJMzLZ3I4H_cLL9hgyVbyRNR916WTDd5eik94D2-1_T59D4g5Dxz3dLoXIUPFtUwjW1T2fiVJlth0piB2VvsM5Nee25rOeS1F-jsYVmzDON_d0anToM7KDGmjW9iLo5xYx_jnLOoEoFkpoNm-3M0o57S0m5sRODS_CSJjb2Dkh_QpNSjq9hGrb55sX6CDaql2uvHzqchHijLveylzxAS9OEzPhcrs9EGYTE9peOdVQRLgT8c2Z_DaRHfA7BZaqN2GN2DWO0ejYw8LgAE-_J8-uj9n7RfJW_pebnyZbr5-vMkWsQGiahcPKFLzLzqobWTdn_KVtzykusuGsznfOMP0YREkb0AnG3KpbhZbQYyIHbEyob8_yd-eLvThTbtBPgkYccj4t3k12QDWjFAanMaFXjLehl617ju4PZtIHllKL7ISwgl9NJhtvuKpCjaFdZ9lW6GBdjr9g8r2LIKUMtTIXdkeNvy4p1iSUp51NQ-hriaW2Op7n5tV4Bw5-zlgljc5NQyJnFEqSm5YfTch0qbdZviTl3-RxPXH_D5Z0tkmIeMdYVYOgqFCPznyKM-4ZuQIiBX_SZZsoI-KcsH6sATu0knP-j0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/news_hut/65524" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65523">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
‼️
مصطفی پور دهقان نماینده مجلس:
وزیر ارتباطات دستور داده یوتیوب بزودی رفع فیلتر بشه.
«در صورت رفع فیلتر شدن به دلیل تحریم بودن ایران درآمد یوتیوبر های ایرانی قطع خواهد شد»
@News_Hut</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/news_hut/65523" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65522">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=vEoLhJe8LJWHiIM1ELQO-f5-KDkjCSVhzLWC4FAAQ5G_Cxna6zXfRTaAMGMWwPGoddPsw2yApm7cHRGQ8DjS6ssa6nwXcP7SXEvPqS8cDwDrFqmBPnIhFx2UkvIw-MUqMVsTcCRpW50A1nFPKuoMyWlB-FNy7qgvYIaaPT-Ti7_-QYkhdfqw7yd0eJ966GCXqRkhR9Jv7E2IXeYGjr9gdxQEDPM0Biv9ErJZ1ktzREr45j1Bk0X-kbWRHwYcaxafvP-WoNpUfk_tzDAo_iIZYWv8hD39uZZaglFuaCLbs6ptN2xIYcLnCQjl0c_JjzxOQabF231ewazABYllCo3k5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=vEoLhJe8LJWHiIM1ELQO-f5-KDkjCSVhzLWC4FAAQ5G_Cxna6zXfRTaAMGMWwPGoddPsw2yApm7cHRGQ8DjS6ssa6nwXcP7SXEvPqS8cDwDrFqmBPnIhFx2UkvIw-MUqMVsTcCRpW50A1nFPKuoMyWlB-FNy7qgvYIaaPT-Ti7_-QYkhdfqw7yd0eJ966GCXqRkhR9Jv7E2IXeYGjr9gdxQEDPM0Biv9ErJZ1ktzREr45j1Bk0X-kbWRHwYcaxafvP-WoNpUfk_tzDAo_iIZYWv8hD39uZZaglFuaCLbs6ptN2xIYcLnCQjl0c_JjzxOQabF231ewazABYllCo3k5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون با کفن رفته تو زاینده رود و از پزشکیان میخواد وارد دولتش کنه تا مشکلات کشور رو حل کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/news_hut/65522" target="_blank">📅 13:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65521">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=b6Xeur1mtlxP1BbzxiG-RpvQp0XOZ9HdBJNzTtq-PysJEo3zrWyc9himyb4XtUYHOmdPV1zXQ7A0bEzYWfBrww1f12785BKlKJf8lihOwMxLCvrfo1Bm5K8iM2swONn0Rd7fRM6uQZmW23j0efO_p7WSWFbSPAe7Z3_FhyMo3GyZQqsBqKHVLu6quemv0MZGIPVBGw_u4w9WtiT59pDShvA5Otu3rL68vUckLPZu2fxXZvssQfRjjGc0Of5H_0nV5yIXQPChRWAKlwgd-NUfs9A5TtjJjNPrIWcirz9FG67_v9mdoZeyq3MhCBRzjfAGCcaKVffQsG4xNCtLOVLj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=b6Xeur1mtlxP1BbzxiG-RpvQp0XOZ9HdBJNzTtq-PysJEo3zrWyc9himyb4XtUYHOmdPV1zXQ7A0bEzYWfBrww1f12785BKlKJf8lihOwMxLCvrfo1Bm5K8iM2swONn0Rd7fRM6uQZmW23j0efO_p7WSWFbSPAe7Z3_FhyMo3GyZQqsBqKHVLu6quemv0MZGIPVBGw_u4w9WtiT59pDShvA5Otu3rL68vUckLPZu2fxXZvssQfRjjGc0Of5H_0nV5yIXQPChRWAKlwgd-NUfs9A5TtjJjNPrIWcirz9FG67_v9mdoZeyq3MhCBRzjfAGCcaKVffQsG4xNCtLOVLj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آذری‌جهرمی وزیر ارتباطات دولت روحانی و از بنیانگذاران فیلترینگ در ایران: اقدام به قطع اینترنت و فیلتر کردن جوابگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/news_hut/65521" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65520">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65520" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/news_hut/65520" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65519">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBaYm8qrsGgQr4YaVwUWw1pcmmhHcMUqdWHYVvX4t_MPW8ycwgCrTpqqM99YOjXrY1IbyTNZPFHctga1drP60cAmLLrVavRmvDLqO1uV49tj7ZefnCfA3AJ6HnPAfxlfOSGae9D_zSY7uVHuTY6Mv5_tZzIq5OUhTT1aoO5BpKLXp0t0YvHH2Zt4gOJQq-VkGoUmEnM9I41Y5csBCs0pX3saWVVIt5-PhXfcfKm-tQRnVY1m2MXm0hYrf73_Cth6PkE1iWR1_77pQfJ0Gs1F_dd-xrd7YwTncnza1QwFAmiUmReVH1_pzZyrrMg073XkbJcypcyuwfaCLQdKPIquEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/news_hut/65519" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65518">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=BbgB484KfhmoFwCTwMC-f8sjNlEygN9MnlxURApQlvHXUGld7uAOofCPp_QWQCJl4fBY6dHX7i1I3zugTyCurd1YwpUfkP1OwnhHYtEXq6tWOMmIHq4k9cSiPAObc8vT35aFUDGa7o073i4agwWKrtyqyJQcerfu_0khU_20OOM5mD6a4v172dOH-kiWAmJk--4aSXbtamLtZIkt2XHDny5cJlEr51BwmYZkNOwNwt35LFoz1BUol0UOhHNGSTZmTpnuC21ThDORO2BaoftFRS7SJpbrPDJ6gbnPeGyW_3vRL7eHIBDCdaMghJkFpyzi8llqVtC_Tb6yJdWIhmNF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=BbgB484KfhmoFwCTwMC-f8sjNlEygN9MnlxURApQlvHXUGld7uAOofCPp_QWQCJl4fBY6dHX7i1I3zugTyCurd1YwpUfkP1OwnhHYtEXq6tWOMmIHq4k9cSiPAObc8vT35aFUDGa7o073i4agwWKrtyqyJQcerfu_0khU_20OOM5mD6a4v172dOH-kiWAmJk--4aSXbtamLtZIkt2XHDny5cJlEr51BwmYZkNOwNwt35LFoz1BUol0UOhHNGSTZmTpnuC21ThDORO2BaoftFRS7SJpbrPDJ6gbnPeGyW_3vRL7eHIBDCdaMghJkFpyzi8llqVtC_Tb6yJdWIhmNF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مقاومت فوق‌العاده یه برج ۳۶ طبقه فیلیپینی در مواجهه با زلزله دیروز ۸ ریشتری در این کشور
@News_Hut</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/news_hut/65518" target="_blank">📅 12:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65517">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش باحال حمید معصومی‌نژاد تو ایتالیا از آخرین روز مدرسه تو این کشور که دانش‌آموزا اینجوری همو با آرد و‌ تخم مرغ و ... به کثافت کشیدن و جشن گرفتن
😂
اینجا هم بچه‌های بیچاره هرروز بخاطر تاثیر معدل کنکور تجمع میکنن که به هیچ‌جای هیچ مسئولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/65517" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65516">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTwiLoIr7DO4cuszYNQUaNj4jMB3Polp0FcwBopFg0q_AWZPphyUKYGSmvqypcwdrZi1-rBg1lXg4_m8xsqNuS6wBKgUMBlO-6XhfbD6IZssXl8HwnbIUDd_St1IFTLU2PjDi42AO2shrhWWtBntPm5MbdHgLDtp2Tn7Gt4ueDjOGuOq5hH4XLW5JAr12bRd23vf07pzmGzfFsPcHn2U7cpgz6WEjGMZw7B8hSZiICy8wuCynu_gSyalHQGnZJUMHBZzTpep_BTyg4lJdef2Dnv-aAP0ivR9UN-99oZhdhgXDqFiZx7S_ezn3Qes3LjSa5AoyfWX56peDx8w4QPPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
سفارت جمهوری اسلامی در بیروت بجای مردم ایران اومده گفته که لبنان قلب ایرانه و خب گوه خورده
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/65516" target="_blank">📅 11:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65515">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇷
ستاد دفن و خاکسپاری علی‌خامنه‌ای اعلام کرد که مراسم خاکسپاری رهبر دوم ترور شده حکومت حداقل تا بعد از دهه اول محرم برگزار نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65515" target="_blank">📅 11:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65514">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
جی دی ونس معاون ترامپ:
مواردی وجود داره که منافع اسرائیل و ایالات متحده متفاوته.
هدف اصلی ایالات متحده در مورد ایران اینه که اطمینان حاصل کنه تهران سلاح هسته‌ای نداره.
ما می‌تونیم به توافق هسته‌ای بلندمدتی با ایران دست یابیم. ممکنه اسرائیل این موضوع را نپسنده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/65514" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65513">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد ایران:
اگر حالا ما برویم و بمباران کنیم «که اگر بخواهیم می‌توانیم خیلی راحت این کار را انجام دهیم» و دو سه هفته دیگر آنهارا بمباران کنیم، آنها دیگر هیچ چیزی نخواهند داشت.
اما شما تنگه را برای ماه‌ها «باز» نخواهید دید. اگر ما بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نمی‌خواهم.
ما یک سند امضا شده خواهیم داشت که در واقع از انجام بمباران قوی‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65513" target="_blank">📅 10:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65512">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا از نتانیاهو خواستید که حمله را تلافی نکند؟
ترامپ: نه، من گفتم کاری را که درست است انجام بده، اما می‌خواهم هر چه سریع‌تر متوقف بشی چون آنها باید متوقف شوند.
این مربوط به لبنان بود و باید متوقف شود. ما می‌خواهیم کار تمام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65512" target="_blank">📅 10:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65511">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
ترامپ درباره نتانیاهو:
به نتانیاهو حمله شد و او هم متقابلاً پاسخ داد و من نمی‌توانم او را به خاطر این موضوع سرزنش کنم، آنها را هدف قرار دادند. آنهاهم متقابلاً پاسخ دادن و حالا درگیری را تمام کرده‌اند.
بنابراین، آنها قرار است فقط برای یک هفته دیگر یا چیزی حدود آن، یکدیگر را به حال خود رها کنند.
این وضعیت خاورمیانه مدت زیادی است که ادامه دارد. اگر واقعاً بخواهید بگویید حدود ۳۰۰۰ سال اما مطمئناً ۴۷ سال است که اینگونه ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65511" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65510">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
ما اکنون در حال مذاکره هستیم و آنها می خواهند معامله بسیار خوبی انجام دهند. آنها حاضرند همه چیز را به ما بدهند. آنها حاضرند به ما "هیچ سلاح هسته ای" بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65510" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
🇺🇸
🚨
🚨
ترامپ اعلام کرد در دو هفته آینده "پیروزی کامل" را بر ایران اعلام خواهد کرد!
ترامپ: من فکر می‌کنم که ما در آن نبرد پیروز می‌شویم، اما شما واقعاً در دو هفته آینده که پیروزی کامل را اعلام می‌کنیم، پیروز خواهید شد.
این یک پیروزی کامل خواهد بود. خیلی زود این اتفاق می افتد و قیمت نفت پایین می آید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65509" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
🚨
🚨
ترامپ درباره ایران: ما هر چیزی را که برای تخریب وجود داشت، نابود کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65508" target="_blank">📅 09:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65507">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65507" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
🚨
🚨
مقام ایرانی به الجزیره:
واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65506" target="_blank">📅 09:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65505">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
طبق گزارش
نیویورک تایمز
، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65505" target="_blank">📅 09:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65504">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=Pu_FcKCoMln7WykV5NehLYQZgjslVLaGMgIEtKTjmu6GSme19WYv06pnnoD5DidILAQDEOLV3ojE0CoUWclT0JDX6T8D0QxePbqlVdeZbN8-xbjAJtwbEb67AV9sdwDGYFMDHrf97XgmLTYJyJSA-524CclstgUIcQ-jrwve676zZIH01ZcIXDXufkmpy12s47OnBxY9OlCCYtA6w8NFztu9Sho72Tr4cvONBkq5PsjZyw5y6qGfDZRac0VsRhAA-qcFQWiVDuKRwEOqrarvliEJht8l4D9ry7d9bRYjX1bj1HxiHUrCex19_HjsYDsvcW4FqRdYdaIJlNiuP9GQwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=Pu_FcKCoMln7WykV5NehLYQZgjslVLaGMgIEtKTjmu6GSme19WYv06pnnoD5DidILAQDEOLV3ojE0CoUWclT0JDX6T8D0QxePbqlVdeZbN8-xbjAJtwbEb67AV9sdwDGYFMDHrf97XgmLTYJyJSA-524CclstgUIcQ-jrwve676zZIH01ZcIXDXufkmpy12s47OnBxY9OlCCYtA6w8NFztu9Sho72Tr4cvONBkq5PsjZyw5y6qGfDZRac0VsRhAA-qcFQWiVDuKRwEOqrarvliEJht8l4D9ry7d9bRYjX1bj1HxiHUrCex19_HjsYDsvcW4FqRdYdaIJlNiuP9GQwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یک کارشناس حکومتی در صداوسیمای جمهوری اسلامی: آمریکا در جنگ ۴۰ روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته! کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها برای جمهوری اسلامی کار سختی نیست و ما به درخواست کشورهای منطقه خویشتنداری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65504" target="_blank">📅 09:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65503" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl_w1VD1DaW77JMNunrqIT0K9vP82awwDEe8hgGP7aSgju4vJQyVuHxL3BGZlC4tYaN1kZb5YCCA-G0Vo9x8utxWYFT4_GuNTts8lr3kAA2yB70qp5U4TG6AbtPtPC302HL1oss0sqsfNdkGY7l225HzAQ3lNNtNt2Y8RSmD8MZqCECDmYZqO87mOFMR76inVf9cORi2edxmTHcOpQ6tmj0VIojIZDtiZvF-AUX0lE5oQqfz6QhxQpwiaUdbcccz6MyowljgvRvHutzzxbyUpBOHwX6l7ox0D-nLULKIRb5RZL27dUCPhpq22s6jmy9PuLKguziVbmqRUszW83iyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65502" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65501">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru9iLZ7mnVtuOVJwvfQ293FIWv8CZ6uv_Vsr-8Wnd7eKyBIPWQhnN-X27fq1WZGscrPZUwLT5-_xuGSkWaHeQePG0KOgKfUUXowr4wumil_SoWcAVaFMcUI1582F7WBWkuOd72LzO0zsYZc6NKQhnUqgi2kbEBSfiGbHwboptGnzUlUgeBcHLZ5aBdSCJP2sti-fHf-6g0_cEmBu-U4jHXuG4aekFPef77OzQAv4vFF9GMFz8QsyBCUo1wuocHcEINA0AG1l2Pkeg2NEA04j5Cd-OjhYUDmtMXkR5hvyXlx978Y40KAUv3Qp6oCf13TtH-E46MkJ_s1gDuUAPcXHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
اونایی که
۵ ماه
پیش وارد شدن الان
۲.۵ برابر پولشون سود
دریافت کردن
دو فرصت
ویژه
در
سرآوا
برای شما فراهم شده که با بازدهی فوق‌العاده می‌تونه مسیر جدیدی به سوی
ثروت
براتون باز کنه
✅
اگه توام‌ دنبال یه‌راه میگردی تا بتونی درامد خودتو داشته باشی به خانواده سرآوا ملحق شو:
@Sarava_Finance</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65501" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65498">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
مهدی خراتیان تحلیلگر اصولگرا: در ۱۸ و ۱۹ دی ۱۰۰ شهر یا سقوط کردند یا در آستانه سقوط بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65498" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65497">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
♨️
🚀
خبرگزاری فارس: انصارالله یمن با پهپاد به سرزمین‌های اسرائیل حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65497" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65496">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65496" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7093313be4.mp4?token=Bic9MZSzWRs9BDkiX_VpCNLTzDr5QIsk-x2g5a8_0S17YJ09HoK3xOtzLzPqTQuoWMUoypOQROq40I56HAPVJ0-iUkQDIQPF6LlVs_LlpoBKRrrMAigcGV-uz1JVwTyvUBeKSVX2kmG4lUMjocCg6-5DBwQQpW65Fo1Vw7N9qgtWvEKppsYZ-fa6ZFk2K3k_rMTyonkRKZTmiGLwlbf3x6YcisTSmCqB5LsHJlUBAdj-hCKISlpPJ8kA6pzU25YW80CRJGE2zsoTGdw-YY9WitA_KsPX4RzONIX7KDd90H16-PRZUIXgCuCgK7GMDpU4mXv-tOUQMUVrOyv1roA96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7093313be4.mp4?token=Bic9MZSzWRs9BDkiX_VpCNLTzDr5QIsk-x2g5a8_0S17YJ09HoK3xOtzLzPqTQuoWMUoypOQROq40I56HAPVJ0-iUkQDIQPF6LlVs_LlpoBKRrrMAigcGV-uz1JVwTyvUBeKSVX2kmG4lUMjocCg6-5DBwQQpW65Fo1Vw7N9qgtWvEKppsYZ-fa6ZFk2K3k_rMTyonkRKZTmiGLwlbf3x6YcisTSmCqB5LsHJlUBAdj-hCKISlpPJ8kA6pzU25YW80CRJGE2zsoTGdw-YY9WitA_KsPX4RzONIX7KDd90H16-PRZUIXgCuCgK7GMDpU4mXv-tOUQMUVrOyv1roA96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سپاه پاسداران حملات موشکی و پهپادی به پایگاه‌های آمریکایی و گروه‌ های کرد در نزدیکی سوران، استان اربیل، کردستان عراق انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65495" target="_blank">📅 23:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=XPbIR_zUVc_AWe2Hxjt2N3Jh-R8vmaAl5rFvORXtLyYxDivONJ_09UFUa4jwZWHIfaMECYwD7uYnEAnKP8l6ao6NS3_HFrJCXKxB9q7sPJml4n2X4CrvTnLj7nUfV37172YRLNE26PS4A02pZ25-1kusnY4dGhJpL1OIB7nKCvO195ob97cV8mtKAtCtGTjXv3JpVL5SFvdEEoACH4Ja_q1KHyAP6C5OieskSoLpgABb8WhgSvM8jFbfVavxfUeiG9LLG42wrVpRzX4FXzyr2vjTsDQ9vi3nhCDRNjgazpWCQYoE9_SxKykzTUMURywxRuq-iWcyHgguyPWTH8HbOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=XPbIR_zUVc_AWe2Hxjt2N3Jh-R8vmaAl5rFvORXtLyYxDivONJ_09UFUa4jwZWHIfaMECYwD7uYnEAnKP8l6ao6NS3_HFrJCXKxB9q7sPJml4n2X4CrvTnLj7nUfV37172YRLNE26PS4A02pZ25-1kusnY4dGhJpL1OIB7nKCvO195ob97cV8mtKAtCtGTjXv3JpVL5SFvdEEoACH4Ja_q1KHyAP6C5OieskSoLpgABb8WhgSvM8jFbfVavxfUeiG9LLG42wrVpRzX4FXzyr2vjTsDQ9vi3nhCDRNjgazpWCQYoE9_SxKykzTUMURywxRuq-iWcyHgguyPWTH8HbOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
رژیم جمهوری اسلامی با موشک به کردستان عراق حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65494" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
رئیس جمهور لبنان:
اگر حزب الله از تحویل سلاح خودداری کند، مردم از آن روی برمی گردانند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65493" target="_blank">📅 22:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
قالیباف:
هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی روابط با آمریکا. ما نمی‌خواهیم از طریق تسلیم یا شعار پیشرفت کنیم؛ بلکه باید به دنبال پیروزی مهندسی‌شده با قدرت و عقلانیت ایرانی باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65492" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65491">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
نتانیاهو به وزرای دولت خود:
ممکن است به چند دور (جنگ) دیگر با ایران بازگردیم، این پایان کار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65491" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnriTGykiDe0B7te9kmZl4FGkMnpoWRRvDHsETggA1AukC4lJR_B2x6sSF0zyWMARy3EdTzxqf014_Ro_ZlHCOQre5-LIE_Do-EBofq8j7oAoAc2iiMIAj_xedu1pVp9SSLFBW3BPjSojr-AasSetxyzU00qbo-86JXtw8rpka7nTow-n5azuU0GuS7mVpbA-ySIWm1YBLdMUIp7c7tZcRKQXnUnmdpOq13vv6F3X80E9YCF2dC5f0hUS4HbCkminqobZCczigLeR7nS6zMRYsZzvpd4JGm11DTIB8RIIxTnFV1d3n3udu7BRT2NOCGm-UQf4rYu8TN8ykgBE9buzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65490" target="_blank">📅 22:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNuSTVIh0pmAhVzvP4zKzP5-xSw5fAC4_X5fYEygP-UdJ9EVMO4dsaEdtplJsvXzpRhYIDvJuLAyUzmp3wmNygQlgEpo_-cQoQhQfVn3aGIHpAEiwaWDvJx32zMEWju7PQT2ZZzVY8X1kQlk9YDDx6ENJO0a3stMbIXK24_4vuDy7UuVEOFXfv1bE9X92lKrJyTUiSS3AYEvO89XxROH2NyUOv3k_16oPQnZM3xhGBNJt4HA9ahQ5ze_8fI2OspsEJwr2PvjUhovCyRjroYlIGaa3R8fjDz5Ool0b-BzKV6oGM7N6NAEpeq_yQD0yg_Rz9nl8yLUPHW17GIFOkoloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
صابرین نیوز با انتشار ویدیویی از شاهنشاه آریامهر محمدرضا پهلوی سعی در مشروعیت بخشیدن به موضوع کمک به لبنان دارد
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65489" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
مردم ایران بهتر از هر کسی می‌دونن که تا وقتی جمهوری اسلامی سر کاره، نه ایران روی آرامش می‌بینه و نه منطقه. صلح، امنیت و پیشرفت واقعی فقط زمانی به دست میاد که این حکومت دیگه بر سر کار نباشه.
راه‌حل، مذاکره با سپاه و مسئولان جمهوری اسلامی نیست، راه‌حل اینه که دنیا کنار مردم ایران بایسته و از تلاششون برای رسیدن به آزادی و پایان دادن به جمهوری اسلامی حمایت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65488" target="_blank">📅 21:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
این حکومت سال‌هاست مردم ایران رو گروگان خودش کرده و از جون و مالشون برای پیش بردن جنگ، ترور و بی‌ثباتی تو منطقه استفاده می‌کنه. توی این درگیری هم مثل همیشه، هر آسیبی که به زیرساخت‌های ایران یا مردم بی‌گناه وارد بشه، مسئولیتش با جمهوری اسلامیه. این رژیمه که کشور رو به این شرایط کشونده و هزینه تصمیماتش رو مردم عادی میدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65487" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
جمهوری اسلامی باز هم برای حمایت از حزب‌الله ، کشور رو وارد یه درگیری نظامی دیگه کرده و بار دیگه نشون داده که منافع مردم ایران براش هیچ اهمیتی نداره
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65486" target="_blank">📅 21:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۲ اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت!
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65485" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
ترامپ :
اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن.من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه!
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65484" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشور: حوزه هوایی کشور به وضعیت عادی خود بازگشته است و عملیات پروازی طبق اطلاعیه‌های پروازی صادر شده (NOTAM) از سر گرفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65483" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=COsN9W14QP7UaIJy8DiSBBN-1BvrTLyfDn8zn74m94TSDZD8LfwSD6WMNWAu0_TpjfgzaUvMxzuVIAGZ5zAkZpCyQOzGx5CSsbZkny41KISwuK1bfR7q78erL4iu8Mvq243tEJHIohnEc3z5IuPgaiBLa7asDcidRPPu2vpRrlnmuTuLos0_raEXBN5q6qDF9_XyRFXo8xksjnZOCxeW3V7KBu9BbRb3WE4P_KN7BWdGNmDLcYJvw0W6_ZOznoy0EWEo5ucb6ZU6mD28jHET8J2gb4vf3AVlXXBT4fcsiOrBBhWnBbIYDO8xvGNGaukbVLV-ixxml4P8TKbnRCeTvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=COsN9W14QP7UaIJy8DiSBBN-1BvrTLyfDn8zn74m94TSDZD8LfwSD6WMNWAu0_TpjfgzaUvMxzuVIAGZ5zAkZpCyQOzGx5CSsbZkny41KISwuK1bfR7q78erL4iu8Mvq243tEJHIohnEc3z5IuPgaiBLa7asDcidRPPu2vpRrlnmuTuLos0_raEXBN5q6qDF9_XyRFXo8xksjnZOCxeW3V7KBu9BbRb3WE4P_KN7BWdGNmDLcYJvw0W6_ZOznoy0EWEo5ucb6ZU6mD28jHET8J2gb4vf3AVlXXBT4fcsiOrBBhWnBbIYDO8xvGNGaukbVLV-ixxml4P8TKbnRCeTvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فیلمی از کشتی M/T Marivex که امروز صبح گرفته شده، پس از آنکه توسط نیروهای آمریکایی به دلیل ادعای تلاش برای شکستن محاصره دریایی ایالات متحده علیه ایران، از کار افتاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65482" target="_blank">📅 20:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siRTzi9QhaKPhnknUxg1hWAcBHMwbmSHlZGNiSrZSA1LvklX7SEM0atrovw7tJHQU20tuGLs4Q5zlW8YyYS8B34ALOgf8nP1gExn7AP-zCMjE4HKLsrm4YSK83EAWyREzmAlP5YMpFsPIuVg6JfJuZ2QCkWCHlImzyQCLyJ9U1nITzkcB98S4UHU_6NKdeZkQVI8IHdQNqzQqwOkhWJEzMmiJDu7Zrsisg7yTFUPB4tPVbX9TXCiNr_uU-FZ_AjHOUXxMPelTqVDeFyM_h9Mb-sPdrXaYA8aCqhVx_SKjU6Wmpp58RYVkUsen3ncQkmmDWi9tcYQnxH6bNiIp3gdgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده یک نفتکش بدون بار را در خلیج عمان، در 8 ژوئن، پس از اینکه کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، تحریم‌های جاری علیه ایران را نقض کرد، از کار انداختند.
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچو پالائو را زمانی که در حال عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران بود، از کار انداخت.
یک جنگنده F/A-18 سوپر هورنت از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از اینکه خدمه از دستورات نیروهای ایالات متحده اطاعت نکردند، یک مهمات دقیق را به بخش‌های مهندسی و فرماندهی کشتی شلیک کرد.
ماری‌وکس دیگر به سمت ایران حرکت نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65481" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65480" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONvhrWNAk8sa-RB2kEclmNyU2gE6IX5E6BviLPbz2-gHTOWam6QM_F72_ONcJ8fT5Bueu3NAvJ60wGtjpHsiMAvi6La-luuXEPwNwX8dPLCO2prtYNz43QrEFdwm3GIAbIwu0wmCULU_qlwjQ_kw5iDoZlFq_UsrSY7K0CVIxrgvrWrW5vuDcA-R0Tn4vPZkeK7b5cN5kKdCOnARU3qnIC03k5qUgJhy0W8HdNx60uqajxWwy_hm5OvNegA1xDiBecZq05fwqcc1vJfj0E4CybFF5q0ZgSgn80JxgiWVbOLATjvntznr8jsiMm1fWKbmyQcwrlZlRZEDx9AivzPXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65479" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل: ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
«این حمله گسترده انجام نشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65477" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
فیلد مارشال ، محسن رضایی:
ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه. اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65476" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل تعدادی از فرماندهان ارشد حماس را ترور کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65475" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران فکر می‌کرد می‌تواند به خاک ما حمله کند و ما واکنش نشان ندهیم، این اتفاق نه رخ داده نه رخ خواهد داد، دست کم تا زمانی که من مسئول باشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65474" target="_blank">📅 19:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9oPGGo_HD1aR6AdlSFNA5C-GlgLmQ7hgs3LpAPBenYtlrn1xfnRbM4OOwcCLh1sCq3WuKE4zQdlxXZTwBvZ4KiKOoSHndDLsXe1HIYcGdZvFNC4ZwHtWivyDeso-Q6YEK8kAzQEnWuAT6NDgzKgxvtiuG5NjE_hPSfb0DjsNwfXtg2jNcp6x1DcS6BMB0A_o8-ULzFL6uPxAnWgTXXLRCyeEtYAoHx71hVnXG_z53px-YuWppvhBnYDjP3Q2XClHajsxtLtkeTsHZNDdarRwuA21pI6zesBMFVpHYLHlYKrUnGDh8p1n5VCA_CTERqE2HV4ausEheRJsYHw-enQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروی دفاعی اسرائیل (IDF) دستور تخلیه محله زقاق المفدی در صور در جنوب لبنان را صادر کرده و به ساکنان هشدار داده است که فوراً خانه‌های خود را ترک کرده و به شمال رودخانه زهرانی نقل مکان کنند، به دلیل حملات قریب‌الوقوع علیه حزب‌الله.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65473" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65472" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65471">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
نتانیاهو در واکنش به اظهارات ترامپ: اسرائیل حق دفاع از خود را دارد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65471" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65470">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اسرائیل فعلا از حمله به ایران خودداری می‌کند ولی ماموریت ما با حزب الله هنوز تموم نشده
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65470" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65469">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=b3ZeopbN__gZ-42GQUt2kVczL-Sc8aO5QgQllHA5sGSH-7V_dImTxDgbagHTGPFQkMEanusj-25aEzkfB_7s7KqVs5KFNMHERj-so-zPy8WkKibVe7Ws2jbK059N3wj1jb7fBlrtSmB49O_tSTJHxSw3J24e35arv1BCYkX0jg_VxZ6Fc-bQGBtDxCZyVLUKpOlDKx5kGSqceXEZPHJ_G1Sr5tsRWFzCQ6SGXno76RUDANIrMp27IvYjIW4TcywY-FARcjOZHvg6qo8zvXM72lF-b3oW-nYh-g9p4yac47P2zN92oRw4h3jVpBjxgHzP27sws8xAwcMPVKldCnIepA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=b3ZeopbN__gZ-42GQUt2kVczL-Sc8aO5QgQllHA5sGSH-7V_dImTxDgbagHTGPFQkMEanusj-25aEzkfB_7s7KqVs5KFNMHERj-so-zPy8WkKibVe7Ws2jbK059N3wj1jb7fBlrtSmB49O_tSTJHxSw3J24e35arv1BCYkX0jg_VxZ6Fc-bQGBtDxCZyVLUKpOlDKx5kGSqceXEZPHJ_G1Sr5tsRWFzCQ6SGXno76RUDANIrMp27IvYjIW4TcywY-FARcjOZHvg6qo8zvXM72lF-b3oW-nYh-g9p4yac47P2zN92oRw4h3jVpBjxgHzP27sws8xAwcMPVKldCnIepA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65469" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65468">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران معادلات را بر ما تحمیل نمی‌کند؛ پس از شلیک حزب‌الله به اسرائیل، به بیروت حمله کردیم؛ پس از حمله ایران به اسرائیل، به مناطق مختلف ایران حمله کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65468" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65467">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
نتانیاهو:نظام ایران پس از پاسخ ما عقب‌نشینی کرد و اگر اشتباهش را تکرار کند با شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65467" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65466">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو: تسویه حساب اسرائیل با حزب‌الله با قدرت ادامه پیدا خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65466" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65465">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=G8KiogrlgsTRiwzwkE4_jADmxzUXcbyacfGBne7FPcbTUM8hCIxV6-R3Q62eBJBPGcfmabvvA-PQnKQP2VTioONSBOT4DWb-gQOs4Rcw-_nWWV4pIIqVGfJ_IxDG84SbUo1vNqYwe2_mi4o_ms1lLWC_OwgCmb2bJd5fZZSVOxZ2rksZ1dff5wLhlKhxicjivj7JF9DOuDVULJAEKrVLvnk3j9H3XaaK4w4BEuysgv6-zbvh8M9rty8HQKSOMJJrz5VJFMVSBuy1WbaO48GH2JLIUJ9_qjyNBaTx4yT95SUezv7wWQc_m9JPKGr2Lg52s53DSTB69owtx5KG5jM-og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=G8KiogrlgsTRiwzwkE4_jADmxzUXcbyacfGBne7FPcbTUM8hCIxV6-R3Q62eBJBPGcfmabvvA-PQnKQP2VTioONSBOT4DWb-gQOs4Rcw-_nWWV4pIIqVGfJ_IxDG84SbUo1vNqYwe2_mi4o_ms1lLWC_OwgCmb2bJd5fZZSVOxZ2rksZ1dff5wLhlKhxicjivj7JF9DOuDVULJAEKrVLvnk3j9H3XaaK4w4BEuysgv6-zbvh8M9rty8HQKSOMJJrz5VJFMVSBuy1WbaO48GH2JLIUJ9_qjyNBaTx4yT95SUezv7wWQc_m9JPKGr2Lg52s53DSTB69owtx5KG5jM-og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سوخت رسان های آمریکا در فرودگاه بن گوریون اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65465" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65464">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
بنیامین نتانیاهو تا دقایقی دیگر سخنرانی بسیار مهمی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65464" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65463">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل، ایسرائیل کاتز:
وضعیت در ضاحیه بیروت همانند شهرک‌های شمالی است. هر حمله‌ای به شهرک‌های شمالی منجر به حمله‌ای در ضاحیه خواهد شد. ارتش اسرائیل به عملیات خود در لبنان علیه سازمان تروریستی حزب‌الله ادامه خواهد داد. ما تهدیدات ایران را به‌طور کامل رد می‌کنیم. هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همان‌طور که دیروز اتفاق افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65463" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3210944dde.mp4?token=Pi5V-_wkAC9MN8Uf7q4SbnYZW6-gY0NB2nncnidUDalMaM7ZxV3syW5Tu6OewWClPiONTVHvO3sOIDg7YlbitlrfFzvzS9B3L9y4e30SbuUityGw4F4DZ3ZwexTvC8ck_fGR__8eKhz-GPhZ6Qas2KyLx8FqMC-1gl6Ue2mCAtnDXufUcEufqb-T-EzCEvBGeP_OQ1m6uY6ebxCHS6zM2JGyTP12hctixvBJH2R5ARdhoEjMt4_72vFWphM1_F2Qh_erej1c2mdL5axCiA7SOMiYxU8UjAfWqR0YXr5J--USoGRnXT8YbC6PxRCUbhLczqsebFgZLPvo8BU1HjtfGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3210944dde.mp4?token=Pi5V-_wkAC9MN8Uf7q4SbnYZW6-gY0NB2nncnidUDalMaM7ZxV3syW5Tu6OewWClPiONTVHvO3sOIDg7YlbitlrfFzvzS9B3L9y4e30SbuUityGw4F4DZ3ZwexTvC8ck_fGR__8eKhz-GPhZ6Qas2KyLx8FqMC-1gl6Ue2mCAtnDXufUcEufqb-T-EzCEvBGeP_OQ1m6uY6ebxCHS6zM2JGyTP12hctixvBJH2R5ARdhoEjMt4_72vFWphM1_F2Qh_erej1c2mdL5axCiA7SOMiYxU8UjAfWqR0YXr5J--USoGRnXT8YbC6PxRCUbhLczqsebFgZLPvo8BU1HjtfGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای از اصابت پهباد به مواضع گروه های کرد در شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65462" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
اسرائیل هیوم از منابع: هنوز هیچ محدودیتی برای فعالیت ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65461" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=HGNaLrWp2NgwV02F3f2xjZU_X8AZgxhSSXKVm1m44YKz871mcs9adVF9l7Rkv-dNbIKxodv5ZLlAtHmmDfycDZMwdrQxQuN5fLSFAfnPkKfAquj6ALhK8-wiTGaCAM7lUA-mStEkCYTCQOnbwudQ6Srqcw-S0mZzwQTQMpXhl1tns_1rDDZ35KqlbYixs1SIE5t1n6zsofbCf0te4fvbhzPGwPQvKVXgd2Fdf9vgIkK-87HwBhMgFzOtv_A4rgu177sRMhn9ITLDLKdqAbJCjPmLr9MFc7zMuY201yOfrd5VqUBXeOOQ9s0iNQO3mGKj67xWVKf-PbHFZy-P7Ehtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=HGNaLrWp2NgwV02F3f2xjZU_X8AZgxhSSXKVm1m44YKz871mcs9adVF9l7Rkv-dNbIKxodv5ZLlAtHmmDfycDZMwdrQxQuN5fLSFAfnPkKfAquj6ALhK8-wiTGaCAM7lUA-mStEkCYTCQOnbwudQ6Srqcw-S0mZzwQTQMpXhl1tns_1rDDZ35KqlbYixs1SIE5t1n6zsofbCf0te4fvbhzPGwPQvKVXgd2Fdf9vgIkK-87HwBhMgFzOtv_A4rgu177sRMhn9ITLDLKdqAbJCjPmLr9MFc7zMuY201yOfrd5VqUBXeOOQ9s0iNQO3mGKj67xWVKf-PbHFZy-P7Ehtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیویی کوتاه از حملات امروز اسرائیل به اهدافی مشخص شده در ایران
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65460" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsZqiKPF0DOvf6i4oM1dDcPM_p5_o_0pJR3_89uVlgg7-x3nIvFcbo1oYVCDVvYTulAnjr17796eRRh9I6mqGQm8yXDbWUE-K02KBSg36E3EjxF_qNdQLWCigJWULGUKxTIhDkFM-Q86lyQxT6B_f1qbpu9oA_wBomjzx2JZTXXJ3oJr-UtRZVZNBomGJci3q75FLKaI3ri77jG_pXhAZ0lOR7_X2TypjB8tS_bd5a-OWlPTX2KMhZEQRdl33EcJE8n3Pm9_7zYo0sVDtHfgI9qaHXUEq8uHUmh1OY49A3UCpOF0sxglvdte6fLG7Gv0vUQRTlei5cXvxtxYJphBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65459" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwK4PPPnzWICVTSG4WTFcP-UTG2okg0hcV03nxEZKh5iJlPptp657eqPROdXKJhcaBak4x8rZyHZS8Jq7p8K6JljapieLrNSln2ZvigkJGdq7Nrw8G449C0TErOJi2ihBMhoiANsPG7En1Mym4uWK3AJJ3mvxvL74t-oXshRxplk5D1A3Va3R5T4_DAWhYTu_oEebNFXOPPUbbRiZlDxndySPlx2xs-YRYvxe2zn6DZBNdGC_2I4ykRclAYwZaUjsP_At1HuHKK4U3w15l2u8rNE4yUm5BBA9G0mvhI9qqejG-1cngKIiu3yS3s6XaFDSsDCJE5PXPm0I4HgAZoBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها حاکی از حملات مجدد اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65458" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cenbWtWUppsL71xKjjp215xWXIZvjFjGYZY_crKX4ZDczn3jAUgW-qtA_52VXSwYrvYKZOuNjFtJWrLsynC_mMlgCBQckpCdruF1SAb6KL9ZYjx-QzojoJlB7VeOfxO2jT0f42571HzvRRaiuRnxMMImZxyThuQOelGaeAfw9SLHorEmIJKo_CAS2IqTdxCHqJi2-k036fF418ObOK0rtT_Zd1MM3IvsIXXH_WbtM5YKV5hY61MbaYdB5DyA9aEEb6VbnNiv5afNL0qduCFSBxEhZLf9xDAbBBj775ENxXm-YOQC6JLo2-V0TXxPfTSu7CpU5LWrJDT-ipjeUICkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما پایان درگیری‌های دیشب و صبح امروز رو رسما اعلام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65457" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇷
فرماندهی قرارگاه خاتم الانبیا:توقف عملیات نیروهای مسلح را اعلام می کند. با تاکید بر اینکه در صورت ادامه حملات و اقدامات تجاوزکارانه از جمله در جنوب لبنان، اقدامات قوی‌تر، خشن‌تر و قاطع‌تر از گذشته در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65456" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ViBrMPzS6bkUJn4CcbJPcWNpNkiI6ZMkq1hvn_OrWYPhFTTcVH3n4Og5asA7HJXAZ8nJIxWxDfkh4NJviA-seWzoRzMlT8HiQ0fysWPclE-_vDN2PblEM-5AhajUawrQsY7raH0zM4lja6L6SvLhseqoV3pivaGfEspGcAovkIDNYakURpEsRvC7JvBTzRi37hc5sqc3W4e-3wFVfQF7El63eiypVZiy5-5UgLH2eMi6xX6MT-oS2ijYSI4fB-dtAfgmdVo6gUM3sok8mNCFVNYkfI87jgnH1LF8h5AwMEbujTZwpFR27ie3RV50zPhnMEAaJ-bnnOtnMbRVhlyMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaC9_nEIpSW7UR4p1mcETP88-nbaoiCVtqHqzSI2Hn29HajK9e-bguPbWsaxui_QUIiE4ULT0dZAXy_QOsDFbVTn9i6gx6zgpOKnR3Td-j1bcrFy_al3NE_8m9oZYqz4tneK8LuwhtJw9cL8ndjyZ8okvmB286TMOvGUpcmSTrnxHKPm0u2AGYt5hABen1hQS_v6Cuwv4XrahXO_fHEFqPjbCBZ248wRs2vh-cKJR37tOVC-d5LGV_sT_ugzdYeFC6UpOXOpevSe2UT5lHYqQ3WlaUqDJ6tSUGQHq4WUonqjiPyKHbl3BNt4S_HgkPqshauNlLNIl9EvOCicC7qQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uupi2RNeVVf9Y7OHoJiALSQ__6vDnJLKv96_xLqO2Fygc1LqMUWmJL-kqc4ian118BmmFIfp3nfvgNPCY_UdsMN3NL22rdcON3ppG4YeE8p_8cai_O6MeeCoG4qdC-ubbejnuUtZqcC4_bOmor13y243gXtgoofugYaIh-wO5_Q5BNRq5p8xscp2xLehYwPFtDQ8VjAxefNPhL8BTLXkPA3OY3mjUBKt6URx1bH8ZSET67gkjE0idnExBVCmDcrQQfrfxkGNzqaFPM3fNSQJ7Ig9kHJe3kOjt_AOAGU4g1ZtyaMzmp1K-M8uFQ_hVYtnxDqZn6grLzMw-itGe0dijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IanHFHOeCnCudxqOjFzm7VqGKackkRANv-y3PDtgwl9R5qfXa5P9ml0OKr4O9Ryi5blEGh87cyuWztFsfCvaXVKAAYjE5RHIrFBVS6HaSaLXv7Q7WAITuKBlt2bSiwfYKdpsUpayoW7KJQmiWemwgBpiD2F3SzFj2i2hdI19WtnDqiaK-cAnIR6UXC6tVdsjUI3DgRD0JYPPI-62R5l2Qc4d62hE-hY7gx66IfFHz2rreXMKdsT441CTjnnEQCE4nSK5Lkk1kWQHCU81KqJmA5nWTE18FDfU5eEhRosIsLrUo2Em3CMu8weFPAdWl8_gTwk_Ad2YyeO1aWcLKXxZ8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65452" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگاعشون
⚡
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65451" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-PAbNnmEhTCHLUDwwADN8bxlYLitcpnnmSaPyBKc2u3GH2MkaWrMGG-v7Uw0sm1TbzWNs7vLTa6_SopS-y-u5ieh7cQu-3rxPislxS0BFti6-l7cRliIXNu_vFRb_BmFRXEVJuUfU4bgmbNEKlMRyElFQ0p77KJDQcY5E-Rtbz7ft22WN0oAJ-oW7alQVHGz6MQY07uRLGuw6fK3zD9vqPX5sWtqSl8z5ii-xP8uL6Hjkdf1DWZbNwkbT0UydK341JLytl9nnmxx8N6Flao4TGS_4xYXwmylSfS4Fy1jkxTvjvlekoqr00nRznAcpunMw-vsU6t29hhxYAvacJjwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبانی
🆘
کامل در لینک زیر باز شده است، برای دریافت آن کلیک کنید و عضو شوید
👇
👇
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک را لغو می کنم
❌
❌
❌
سریع بپیوندید
🖱
سریع بپیوندید
🎧
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65450" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD6gs71XjimJ31pIIMYmBw0QUv5PwkbtfDgbIwqq_T6zxvDuVymMMvKRuEBYWyZZUS9WxWTelbTCu0JdeLo8r_Ouv-B1VdqOVtNyzz9QVkCJkcKoZBtypSp0eBdmASn-9G7MjAzAgNk4XzHfGnPZqE27b1u3BziRg_95erf5W9s58y7CwGCpeyt-KiTgH4QiRT8Mft0Au6NcknVz23ZFfHMlTmdZCtqvBjAnI3W6dsZX9geKoHCeIfQZy6pIfsSwocGNM-PHOM6YJrNtV9UwdEY0FdS3Zi7k8dsiS44GYPbscZKzqECHGGrMR4DXs8Yz3dFGdkd9u6zJJQ_spcg0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره با قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65449" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65448" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOhGeP6EzhSBdLwKBzp808pIBXRDovnlIlUIgkG_d5wD_kk8f2yTG1kO_UNAjY_dAnrGvD4qiJWuD8NtJjdMcSMazbO9HU1Wazuuvxty8dQiJKN6D2b9P4U6bzFCjAgG4ZlBGZj3GmEbGIgrXSnuCzmxximAH5HcJF7LSIAS5lbcz46cyhlgvl-F4qnUOBn0UfV0sVjXL4hO1lw4iGsWgjSd7t6iZEL6cuJZGKTEAT3IMgnqg3xU25-75uadulDcuD2yQ8lZSD7lKZuQmgfYWGKaOi-znTF1vieOtncBMyWG414fI2snjuHXODA6sqghDpVxCjhVuXIPeHKMnYIPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
دیلی میل| یک فوتبالیست بین‌المللی متهم شده که در یک هتل پنج‌ستاره در ترکیه تلاش کرده یک دختر ۱۴ ساله بریتانیایی را برای «بغل کردن» به پشت یک پرچین ببرد. پدر این دختر در گفت‌وگو با دیلی‌میل گفت که دخترش پس از این اتفاق دچار وحشت شده و در حالی که اشک می‌ریخته با خانواده تماس گرفته است. این حادثه زمانی رخ داد که او همراه خواهر ۱۰ ساله‌اش کنار استخر بود و والدینش حضور نداشتند. دختر ۱۴ ساله که از دیدن یک چهره مشهور هیجان‌زده شده بود، از بازیکن درخواست عکس کرد. پس از گرفتن عکس، بازیکن تلفن او را گرفت، اطلاعات اینستاگرام خود را وارد کرد و از طریق حساب دختر برای خودش پیام فرستاد تا ارتباط برقرار شود. به گفته دختر، پس از آنکه او سن خود را اعلام کرد، فوتبالیست او را هات خطاب کرد و درخواست بغل کردن داد. وقتی دختر مخالفت کرد، بازیکن اصرار کرد و از او خواست به پشت یک پرچین برود؛ جایی که به گفته او هیچ‌کس نمی‌توانست آن‌ها را ببیند. دختر که ترسیده بود، به او گفت پدرش در راه است. به گفته خانواده، بازیکن پس از شنیدن این موضوع به سمت دیگر استخر رفت و خود را پنهان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65447" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
اخبار جنگو تو چنل دوممون پوشش میدیم عضو باشید
😉
✌🏼
@Futball
@Futball
@Futball
@Futball</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65446" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-W_dhK3OvK90NH437ea0oZd16BIXkqYGwopoYHoNv0OCsdR4Y-BRyew3Bi9dgXEXDwtcM3_fUnL9DQgWYrChbB-RyM4w5u4BFqea0DLdFg366Ze48mzIiWqI1FG6aa5pMe7UJcPP4lNoUlQhUvpRLZxDkd-bT_lPfEfsOSMD0go0VpxYaNb3_ea6PCgbfZqT-LioDL5cdNUjmq6ej5qzw7UzK9srON-264ppPtLfQuAZBqfST0TksZH_CC2QwPV0jRyhD25F9zjVYR7OUGBiqG0wjoKsHRMXxWLZ41eZhYLTmP3YGFb982Euv3GTiusvvxhCJvVPcK8IofCEAzSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65445" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
مارکو روبیو:فقط کشورهای احمق وقتی به آنها شلیک می‌شود پاسخ نمی‌دهند
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65444" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇱
منابع اسرائیلی: حملات دیشب و امروز کاملا با اختیار و بدون دخالت نظر آمریکا بوده اما سنتکام در رهگیری موشک‌های ایرانی کمک داده
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65443" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=sjDXIZQhnkp-Qvc6osYXNgWB072lLmNRc5aqjOSIdr1ekAAOXNfoaeZxMEQ7ETbh9aThIOJbeCBejYKTJnnInwCsI3UnEXGwyloRVXm0GtBdZMYhur3JXzQcfbYUHHDpPxagH7HBX23YWRAJGqRhuqBAHRp7-_fscCnQ1wneosMBUT85uHv5Ln1AxNXXJlqBhBr9Y_rFxUCU-g4mYteV5MQr6j11v7hMzgHyDnMHFSGcOHsiBe640NREQNDA0mskbp5tg2wKWZv7Ng9woxkpeWlH5FQN0KqXpfXR-2afCmqMS8eoFn7RRX04TBmRae7fMw9xLadxRVIfu-Jb1v2-Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c5e38e196.mp4?token=sjDXIZQhnkp-Qvc6osYXNgWB072lLmNRc5aqjOSIdr1ekAAOXNfoaeZxMEQ7ETbh9aThIOJbeCBejYKTJnnInwCsI3UnEXGwyloRVXm0GtBdZMYhur3JXzQcfbYUHHDpPxagH7HBX23YWRAJGqRhuqBAHRp7-_fscCnQ1wneosMBUT85uHv5Ln1AxNXXJlqBhBr9Y_rFxUCU-g4mYteV5MQr6j11v7hMzgHyDnMHFSGcOHsiBe640NREQNDA0mskbp5tg2wKWZv7Ng9woxkpeWlH5FQN0KqXpfXR-2afCmqMS8eoFn7RRX04TBmRae7fMw9xLadxRVIfu-Jb1v2-Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
‼️
‼️
بدون شرح:
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65442" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDwxXE5mgxFeorMDQRRSp0ofAbSLZt72M-t1ma7sU6bv-ezhl4zOic5iMIziMlVGfz_dAwa4X2J2Tz8tiSTJQZbmPGlXClFtRoRd344iULmsOQe6rpy6FyNUM7YWtT3CiWahhpCDpr_3g0WSNcn0dkg2YULiZFyxIqA0lKvHNvjOmWAl3q-haseB82L3XcrTFn85uEFSM5vGMEXS0qMPOvqxE5to_PxhXlFaw3MwqcIbyduQWmBdIJOo3sbs0VlofRHmizLqB9t3SdTaY1vqom9K7aHxb-q0qUR0tJ3qItrPmSBepn3hWvvzRCfF8Tcur4Co_2IR8di8EO7LAJz0uPfYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb70e7631.mp4?token=rHoGH6F9KI7mPsjkWaMvjbX10xQBNOGY0nQ6QkfjtqCfValhLVqry_dCGaZpix9sml5byiFKxc0K4jeDO02OgSqUa51Frc_FH0nDsD_VtS-be6vPS-QOuw8dEcHDf4RDXTqTXrNPYtagHxO61qefE-s1GKuzJQhJbqJv6947JgRMGLSVJfJovzkSMdMpjYJ4NwxFdurzUd77G0XITJG8k8Bz3mpvIy2GtBSdUcbI4EIgJ5KlpaXtz2fV3eqU1bJ-gyPvw4KT0stZIKt0UHXn1snXwRhziXsp85DZqiYK9s7riVpNFzNje0aitFCSczmUO5Z656FaoKDxlJngXjbDwxXE5mgxFeorMDQRRSp0ofAbSLZt72M-t1ma7sU6bv-ezhl4zOic5iMIziMlVGfz_dAwa4X2J2Tz8tiSTJQZbmPGlXClFtRoRd344iULmsOQe6rpy6FyNUM7YWtT3CiWahhpCDpr_3g0WSNcn0dkg2YULiZFyxIqA0lKvHNvjOmWAl3q-haseB82L3XcrTFn85uEFSM5vGMEXS0qMPOvqxE5to_PxhXlFaw3MwqcIbyduQWmBdIJOo3sbs0VlofRHmizLqB9t3SdTaY1vqom9K7aHxb-q0qUR0tJ3qItrPmSBepn3hWvvzRCfF8Tcur4Co_2IR8di8EO7LAJz0uPfYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
حمله شدید پزشکیان به رسانه دیکتاتوری جبلی
: صداوسیما هر روز شعار می‌دهد اما باید واقعیت را هم بگوید
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65441" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65440" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65440" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smf4VSJmd7Cwg19LzmflL7ArPpW704zBTbNQCdgVjNbmGg1VKI3kSWEys5Uasly9QxvMIcIkUWJk2II9KLMP6_cyYHbRxztre8BMJOSreBaOaRB-fY_V9OhTl35kjPyAFomNRxUOY8OdAYZNg3sCxjEW-9dv-Ni3XBh30hUh6eyplkih-KlRcHiBdVs4LCR3sg3TRKbRl0hTdffvJLkXFcTz7O-LBCgDoDlBz_F6JOX0cLUlVP4-y1N4E_aR6TPcZ2AqA41mvsAoxUuGKayf9c_QLBYyZxouotd6lmq3v1wkqzX1rJUwYxU_dphlutsF0L7sil3kfy7oM8fMKDOl9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65439" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری‌فارس: سپاه دیشب در حملات خودش از آخرین نسل موشک‌های خیبرشکن استفاده کرده و تونسته تلفات خیلی خوبی از دشمن بگیره!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65438" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8792984a2f.mov?token=LkrC2xfxuJlgtRuECZ1qoVAfoMHHnBBAjoGlZp4bCMfSuuprp213KL7_FEy-y9tBBH-iZrdwYhBJ121Q3WQb_JkZ-tU9SxaJDZ_OtxNEp46zoUbY28vBc7NIdbRMDprJxs4a1vIRcWTj0EvMEwwUmZSRN8yEkzisRm8geJvJxPITnvzELNl5Tj91bxxdKNpC4pjqttsDkoBQB1LMTBNcoMc4gqbzdTauFbUCmULv_E2PpyvlmAW62WdE416BoJBgQDJf-hkUGUOxKayuwCOnjHPhuBVMSo-aKF4yBKJQdBkav36gvDGAoXgIsBpKczVinNzu2kWX4YCrlFoZ3Jmt3iDUCjhMplmSs3wKQurhjqN2VvManZy-t6Pq9tAQPf2lP3hNdYxdti7LKoBvD3hk4wo8HIXnW53N8__JmneKvXaR2JT8DdPVQh3txS09ZJgxszhGSHPwKGEl5ZUg76B7Um2-3G6tJETwpS2bBTzhC0Z8kpVYzz1OBr77HOUgw33WI6rA6vWF77cOJZr9l3mX_mKqrQB_lwKwJs1B7ENtoADYt3DAWFH_cy-j4cI5RT0xf7CdL5O8dgC4kv_egOIKGwsa7BgyIEK-mcOX__McLRGrx3vflVeXaknOn41nWk4Vzp92t8Arz1XwUPHZ2IiVpxvFep8oJVOUMetz04aXmcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8792984a2f.mov?token=LkrC2xfxuJlgtRuECZ1qoVAfoMHHnBBAjoGlZp4bCMfSuuprp213KL7_FEy-y9tBBH-iZrdwYhBJ121Q3WQb_JkZ-tU9SxaJDZ_OtxNEp46zoUbY28vBc7NIdbRMDprJxs4a1vIRcWTj0EvMEwwUmZSRN8yEkzisRm8geJvJxPITnvzELNl5Tj91bxxdKNpC4pjqttsDkoBQB1LMTBNcoMc4gqbzdTauFbUCmULv_E2PpyvlmAW62WdE416BoJBgQDJf-hkUGUOxKayuwCOnjHPhuBVMSo-aKF4yBKJQdBkav36gvDGAoXgIsBpKczVinNzu2kWX4YCrlFoZ3Jmt3iDUCjhMplmSs3wKQurhjqN2VvManZy-t6Pq9tAQPf2lP3hNdYxdti7LKoBvD3hk4wo8HIXnW53N8__JmneKvXaR2JT8DdPVQh3txS09ZJgxszhGSHPwKGEl5ZUg76B7Um2-3G6tJETwpS2bBTzhC0Z8kpVYzz1OBr77HOUgw33WI6rA6vWF77cOJZr9l3mX_mKqrQB_lwKwJs1B7ENtoADYt3DAWFH_cy-j4cI5RT0xf7CdL5O8dgC4kv_egOIKGwsa7BgyIEK-mcOX__McLRGrx3vflVeXaknOn41nWk4Vzp92t8Arz1XwUPHZ2IiVpxvFep8oJVOUMetz04aXmcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فیلم دوربین مداربسته از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به حوزه ریاست فدراسیون ووشو و شکستن دوربین مداربسته و درب اتاق رئیس برای ورود به اتاق ریاست
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65437" target="_blank">📅 12:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=Q7wrsc2E_smDFx4OSgVo5sNp1d8GJWKKZzOqb0FF-AQj4fXYUGQa0SlVMfPw3trisx7TF75842SMl_1f_QUk3d4NmTCOaKFPHR9abFNntnASf7YNqPgWIUuaIdbbmZ7hU7arj-Z-s8bjs1wrF5Cop_KCQxKQUatAWXXtA1s_qHw-SXFAe9zFmSnyz91B_FYAa3a8meb8emJfjdl7UziLw40KmC8tTcnOlLEwRRazbqfOBSjoundOgleVQ2DCLeu_mE6fwQ1fHadbBpYmL7ZBxShwWE24nKRV7wq156n7Iki7e40kumyX_5Bam9Y3fORqzaJIkONvDolzrzkZRhrqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b744fd7fb3.mp4?token=Q7wrsc2E_smDFx4OSgVo5sNp1d8GJWKKZzOqb0FF-AQj4fXYUGQa0SlVMfPw3trisx7TF75842SMl_1f_QUk3d4NmTCOaKFPHR9abFNntnASf7YNqPgWIUuaIdbbmZ7hU7arj-Z-s8bjs1wrF5Cop_KCQxKQUatAWXXtA1s_qHw-SXFAe9zFmSnyz91B_FYAa3a8meb8emJfjdl7UziLw40KmC8tTcnOlLEwRRazbqfOBSjoundOgleVQ2DCLeu_mE6fwQ1fHadbBpYmL7ZBxShwWE24nKRV7wq156n7Iki7e40kumyX_5Bam9Y3fORqzaJIkONvDolzrzkZRhrqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتشر شده منتسب به آسمان یزد
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65436" target="_blank">📅 12:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsZ3UUNvhB8_7WUC_iondNIV2zxXeBrVkZvGJkEG3y_DMvRaq-EcEmtgzXB2OCr3ey2dWMYIBsWqEsSy-nP9QxyjdL6JrxmTSM0LswdUyASC7iLnoFDNa5iUiZM1KrEdA8hUpqhNh8q9A5wd4gd-ptn1WcoQkhTY6THWjmByFgY8g-jqNgvmuSgWXR0LxlvXQ_Lv-4042ml6XhL59LAQuqol-0HoIfvZsDSPosojnyu16cqcpPLOOltQFn5ee14q5fzW1unoRDBwQplIeD7nEHQ3H3lITgwv2guI1V1JQ3vsF8C-kA5zqbZDOS0trb8NO5x3GAbEzJdSJMzy9T_G5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مشاهده ستون‌های دود از شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65435" target="_blank">📅 12:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
گزارش رسانه های اسرائیلی از هدف قرار گرفتن فرودگاه شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65434" target="_blank">📅 12:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ اسرائیل: حمله به‌ نقاط مختلف ایران را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65433" target="_blank">📅 11:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
صدای انفجار در اصفهان و همدان
@News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65432" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گزارش ها از حمله به دانشگاه هوا فضای عاشورا
@News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/65431" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
غرب تهران و کرج گزارش انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65430" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
صدای انفجار های شدید در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65429" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=PzArtbGTwzdmbjAbSM-Q5TPMA-y9mYJRuS6DU0yqhdKHYqnPgm4BCQS8Dm4o4QrYU0Mtm-1yChZSdYrXD3CHCVMTBaziobxw26nrpdxXTMz8lFEotFyfiGQPrnJV_23Ta10DIsbjIVx_GSTWs98nIe2bA_eMRyu18dj80Y0toXFbwC98S1Omj-F66UV9R6ulJMcQJyO3XpyPuBKfueF7Ss50zVSLMG5uTypMUACoyszN8Qoo1FFqkZRU_i4VUEW4zZ_b0NInj7eSN6aFydeLc-TrziOYN3PX0Hy0ut7uKU4om99Z75SgnDwRGZHDDFZ-ItPQodx6GIi98uV71CJiuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8514d8db20.mp4?token=PzArtbGTwzdmbjAbSM-Q5TPMA-y9mYJRuS6DU0yqhdKHYqnPgm4BCQS8Dm4o4QrYU0Mtm-1yChZSdYrXD3CHCVMTBaziobxw26nrpdxXTMz8lFEotFyfiGQPrnJV_23Ta10DIsbjIVx_GSTWs98nIe2bA_eMRyu18dj80Y0toXFbwC98S1Omj-F66UV9R6ulJMcQJyO3XpyPuBKfueF7Ss50zVSLMG5uTypMUACoyszN8Qoo1FFqkZRU_i4VUEW4zZ_b0NInj7eSN6aFydeLc-TrziOYN3PX0Hy0ut7uKU4om99Z75SgnDwRGZHDDFZ-ItPQodx6GIi98uV71CJiuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
در ادامه اوضاع بگایی آسیا، تو فیلیپین زلزله 8.2 ریشتری اومده و تلفات نسبتا زیادی تا الان داده!!
@News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65428" target="_blank">📅 10:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=dJb8a83AV37VFNSiV__1SRsmoTG9v_sHEZV53w0bTWIOKk-Jzutyl1rO-GUPHFgDUJKABwebb-rN3id-atvoIejerzlhxtmm2uLPOA8bfQySV0JLai4yo5EJfk5_Z_WqcqARgd6kwbDspHeqVtXG39hCasYPv1-nJ7of2Ux35rWwxaAANhjyzDIIiosXI3Ia4tJL-K9pAzNcgkYD_FENwmKSWMGBPsZJMl05UjUlQiAn5IROGgnJZEgJ7LtebT0I36rrThWgUR85UGj5fvu1ZjkOe6lFUtBFSD7yeNYMCVlYwqRMaPo8SOp7DwcnzVfp0duoDdxfjBOJv2FcQ4mLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b691d50ba0.mp4?token=dJb8a83AV37VFNSiV__1SRsmoTG9v_sHEZV53w0bTWIOKk-Jzutyl1rO-GUPHFgDUJKABwebb-rN3id-atvoIejerzlhxtmm2uLPOA8bfQySV0JLai4yo5EJfk5_Z_WqcqARgd6kwbDspHeqVtXG39hCasYPv1-nJ7of2Ux35rWwxaAANhjyzDIIiosXI3Ia4tJL-K9pAzNcgkYD_FENwmKSWMGBPsZJMl05UjUlQiAn5IROGgnJZEgJ7LtebT0I36rrThWgUR85UGj5fvu1ZjkOe6lFUtBFSD7yeNYMCVlYwqRMaPo8SOp7DwcnzVfp0duoDdxfjBOJv2FcQ4mLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
لحظه اعلام خبر حمله موشکی به اسرائیل و واکنش هواداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/news_hut/65427" target="_blank">📅 10:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
فرودگاه‌های غرب ایران کامل تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65426" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEXlmPSYZOkg57jP39mReeMUUI2iH2QX0FiGRpdORIiR9zaGwjAFTUNfAJuhxKjvhzq7e5WC0KbP6EgpeQWEW6c2nX4FjH_wUgNjwNeAA5jxTn3O8M92gTFu6BTZFRdc0S_xxoQSgM9HkvvGO9oPCOiqpH0LNJ7AfLuEa-Hrta7wtjwHsxlZfYTIgDgxER_eOsvJj65_LeVz3lyjhYUwSpopgdE4SJyiCbM94CVBcn-WE89XiGOL785fZOuKq4TuRDf7dMufMB2sVpOEGX_R6zaDd_bU3mYb4GtTHkYOI0qerJkHyFMoXB6yN5M6wQgsK94cqkaZOFXrB8YnLAh3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت ایلان ماسک درمورد ایران: « تنگه هرمز به نام اهورا مزدا از زرتشتیان نام گذاری شده »
@News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65425" target="_blank">📅 10:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aazTk1G5-qZJlPBexpLP9jL2EwbQQqD5hU3v0YzaoxMxwdnmHdOBRJPSoRqYhMNLGSgpCGBlMmEZHQxGi8cSyTAKOLCKsU2o3jrA4lUM9ASo6bN46H_MDip234jdlrNkvcHgrZLaC4TxnEbSghFHG4pmleKcTZvR4YSwrKWW-zpHu1V_ynDufRI1ysK8dS9_sY0xL_n_fzKgYsUZbXpbeDr3zBISA36jqWwRyMdFLWN6NHXlHeGLHVf5yS0OqnYIOYYZhWW6v5-fq-Rnc4JqsShJ2pVIL9LrI02A1MFuuVQpfjEIIX7KVHvfgw2X3lZI6tnYmFKgjoDLEdt6H6Qsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
حمله موشکی سپاه به مرکز انرژی اسرائیل در حیفا و ناصره
@News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65424" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=SYb-KhPDlHEmD9Z3bfdcZ4WCHQwRptO8SX3ytjQyMcIkfBDwnBO2n6h73LbeyPyv-pwSJi925j2q90yjduA4rLvFnHqTWyAK7-AAmhUoJbveijXdvIa2fOboG72KxmigyTygJICdqZREBA7Rh10THA7gmqsTSLcxTQHqtVJiHAfAUInHyXiAkFGHfrw3GpRda93j3U8mwyzI24KoEq9o3WHT7-ADFN2PZRwOR8EOri1cFLs2GtihF-2jus7VhXKDq5nKzek2tMs_cKXQdpuNhW0Nv4dOrdptl2bUTxo5VeMmZ59UHouFv8Vk38o9TAK6Qkvc_M113_i-Y0rTGrjYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56aa95f90.mp4?token=SYb-KhPDlHEmD9Z3bfdcZ4WCHQwRptO8SX3ytjQyMcIkfBDwnBO2n6h73LbeyPyv-pwSJi925j2q90yjduA4rLvFnHqTWyAK7-AAmhUoJbveijXdvIa2fOboG72KxmigyTygJICdqZREBA7Rh10THA7gmqsTSLcxTQHqtVJiHAfAUInHyXiAkFGHfrw3GpRda93j3U8mwyzI24KoEq9o3WHT7-ADFN2PZRwOR8EOri1cFLs2GtihF-2jus7VhXKDq5nKzek2tMs_cKXQdpuNhW0Nv4dOrdptl2bUTxo5VeMmZ59UHouFv8Vk38o9TAK6Qkvc_M113_i-Y0rTGrjYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
تصاویری از پرتاب موشک از ایران لحظاتی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65423" target="_blank">📅 10:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام انصارالله یمن تنگه باب‌المندب بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65422" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
یک پایگاه آمریکایی در عربستان سعودی هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/65421" target="_blank">📅 10:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=Vx9BnlTpTRqZzR44Ns87XkYTH50EMFfroOlQgfJ0c3ZGAJotYO8CCYlVf2f71EE9ymvfci7ML1ibtCrpJzecFb0xnghYpA3jMXaN2iHYAc4K5SjBp0Na5E_tHCDiC9rHnEOhP0kuZZjsI_vrLkMJQdKAUVy9aISR6vOS0nBQyjgfJ8rcFLNyhzgYDxMklM8CQprmxpM6kDuOnXHRhCKa9BtGqxCawAR8nYCXsdcHi3cIHgRHhRvp47b5oDNzzvZNNzoJRKSwCAkvx0gX2-c-t05rqFxdzeiPIHvYkjuH32PKm7wM_HEI0yD3Oe5M8E-3fdpY0MCsc8SZqxVvSHdhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9d994e5a.mp4?token=Vx9BnlTpTRqZzR44Ns87XkYTH50EMFfroOlQgfJ0c3ZGAJotYO8CCYlVf2f71EE9ymvfci7ML1ibtCrpJzecFb0xnghYpA3jMXaN2iHYAc4K5SjBp0Na5E_tHCDiC9rHnEOhP0kuZZjsI_vrLkMJQdKAUVy9aISR6vOS0nBQyjgfJ8rcFLNyhzgYDxMklM8CQprmxpM6kDuOnXHRhCKa9BtGqxCawAR8nYCXsdcHi3cIHgRHhRvp47b5oDNzzvZNNzoJRKSwCAkvx0gX2-c-t05rqFxdzeiPIHvYkjuH32PKm7wM_HEI0yD3Oe5M8E-3fdpY0MCsc8SZqxVvSHdhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
با تایید اسرائیل، پتروشیمی ماهشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/news_hut/65420" target="_blank">📅 08:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب موشک از ارومیه ، لرستان و اصفهان به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/news_hut/65419" target="_blank">📅 07:39 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
