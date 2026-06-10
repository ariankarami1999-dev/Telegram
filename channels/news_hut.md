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
<img src="https://cdn4.telesco.pe/file/P2NsLXyJldXP7L6X52q6203ws2NgDAtTjUlDZDOvhVZp4P3jEiL8s9UoU4BgGCS9lJfUSqwQkmu99bIWLtFUHQlmj2KM0gDYQkRB5lO-_5RkoRy9piwaHHVtlInmpyi1c-1Dnzt8I62vuWlffNZve1VvuNgkOpViivJ_ooHG4fR_gq1eZbNH2Yveu6CReD2BE0U-ZpTYnsMC6ViX9EhM1qexogITrJirG1qssbu7B1A7Q8yCjrMfkXbpFUxPU6g4-9WvJPvmIsIYm63HHeUwS70W0stb9qP9Iwx5YydTnj0YrBGJRMUK0SJcMo-G2rOIgu8DYvhVEFFCvm_pxKvoQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 226K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-65676">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65676" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !
https://play.google.com/store/apps/details?id=com.barkovpn.app</div>
<div class="tg-footer">👁️ 315 · <a href="https://t.me/news_hut/65676" target="_blank">📅 18:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65675">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ اعلام کرد امروز ساعت ۵:۳۰ عصر به وقت شرق آمریکا در یک سخنرانی اضطراری با رسانه ها و مردم صحبت خواهد کرد.
جزئیات و محور های این سخنرانی هنوز اعلام نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/news_hut/65675" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65674">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC6ObM7Z8jbMWh8SF-GemDCve8OYD3rBohgBHdSZr6qhSEKpwXDi9y7K8AAyQ3ozDRfVv5g0gR_1fh_ZN0Mt-AHtlVg_Xa0o_SWP78YYo4i6tc8d5G-j75ecg6ApwUYfxeDj0lWsBY-_R5zfP_LTktpKs2fkfPmsf1E33C5eSW289_i625RaLewMJW0DxsTKgOi2XhgIm8_9cHbgqgO-h6_YOi0vdl4NoJet1aGpAT0VK3pXqo6HWSnaGtWHu-NlXf20u_JrHIBQnMzFclNjJF2ex6A8qc-3T-j3CtxuoUNbBRfRCyvOzvQmfbPupaM2s_Mm4WuVdkkYJucjgz4rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو:
به اقدامات قاطع خود علیه جمهوری اسلامی و نیابتی های آن در منطقه ادامه خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/news_hut/65674" target="_blank">📅 17:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65673">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwlUIOCQdrE-LcXRuhJhqQ46lFG1rogpBsKrnYXybwHdCV7SRp524zmHyuguVnU98BXdhua4Wgm09MSjwgMPIZpJCgfM-yun0TCThTWCy6fFn6FzZVrnrVrgKhdIls-Ox3z15eDGozi8-MGl7RDz29zpI36LNOVeCnSwO2FMZ1rPI84CywXejKPpj5mQeriS5sro8SUXswOkFL-ahOGXIazUHmj0XkPTeuu8fGo64TN2Ek4Xy4Rb2BhkVtffTACH499Bn_p8VCJF1ZCGVVj5nlQbGm7Fe8m5BVatz61cNrhRdNh9kgTsrsMnQJ8CDKUnmhUXXDyjs1fOCKCBGy4hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب گذشته یک فروند بمب‌افکن B_52 نیروی هوایی ایالات متحده در پایگاه هوایی فیرفورد بریتانیا فرود آمد.
با احتساب این بمب‌افکن مجموعا سه فروند B_52 در ۲۴ ساعت گذشته در پایگاه‌های نیروی هوایی سلطنتی بریتانیا فرود آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/news_hut/65673" target="_blank">📅 17:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65672">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/j9c32D7vm2iEKbphB2vsY4yTMnVwO_d__GEh5U3Mj2YNkUvC5bEMOCpTLGTBbfUx_HKZUVN11Xqyp8xXo49EaCsvJ1riWkeg7HJ71XZXdGPCR2Rb8h-B695JoMe5h5r5_LhC2Mgq3AmaLP2d_auMjCp23naX5cSrVt80GJ89TBfTiBieSZi43MdSJQLrVOZiQJMK9Qpj8UwyG_tKuDkRGyT3dkXL1lM7O5XPMZ9KPRxRuWdYC9agnZj9km1Y2D1iljfByTnRsUR0ZfJoYzX3gYCbN5UqgieEHS2kpgp98tnUIdnyhwAFqc-C4tAdQkE0PWsjIPv9Rk4pimR5RmtQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۶ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🎁
| کد تخفیف : 40
▫️
5 گیگ 30 هزار تومان
▫️
10 گیگ 60 هزار تومان
▫️
15 گیگ 90 هزار تومان
▫️
20 گیگ 120 هزار تومان
▫️
30 گیگ 180 هزار تومان
▫️
40 گیگ 240 هزار تومان
▫️
50 گیگ 300 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🗣
| ربات :
@OPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/news_hut/65672" target="_blank">📅 17:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65671">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79a9aadfeb.mp4?token=Fu_v7F_cME23fyfkQaXnMl7yy33US6RrKuq0GtIcXuqF89Pfys2JkcUJqs1Jf_2lleEfZwfLvmv7eDGvm0DS5cdSTwFtGlhelb41dRhK6PB57_zMvnceFxjITNePPa43gi93nczDD4t742zwgFhTH42U61k3AkziVka73SwDjgZE0kPpejN3MAw5pGDK-H-l3fQmptOTzLEKyhnkxrwYrGjcppSvfOHH3SJieaBpPBbz6ZsWAfEDBL_kfXwIy_QU2TZ063xGXEqyWhnZ5XRqPZ4fFgbOPsbupt_2D_8ywQkdIzWORzF8pCxCi_iaUmMP87JzoY5X0KavOR6dHeM9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79a9aadfeb.mp4?token=Fu_v7F_cME23fyfkQaXnMl7yy33US6RrKuq0GtIcXuqF89Pfys2JkcUJqs1Jf_2lleEfZwfLvmv7eDGvm0DS5cdSTwFtGlhelb41dRhK6PB57_zMvnceFxjITNePPa43gi93nczDD4t742zwgFhTH42U61k3AkziVka73SwDjgZE0kPpejN3MAw5pGDK-H-l3fQmptOTzLEKyhnkxrwYrGjcppSvfOHH3SJieaBpPBbz6ZsWAfEDBL_kfXwIy_QU2TZ063xGXEqyWhnZ5XRqPZ4fFgbOPsbupt_2D_8ywQkdIzWORzF8pCxCi_iaUmMP87JzoY5X0KavOR6dHeM9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🚬
تو مکزیکوسیتی شورش و اعتراض شده و در فاصله یک روز تا افتتاحیه جام جهانی، معلمای مکزیکی به خاطر دستمزد پایین ، حمله کردن به محل استادیوم افتتاحیه و ارتش وارد عمل شده تا جلوشونو بگیره
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65671" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65670">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام. ما کارمان با ایران را ادامه میدهیم و به جلو میرویم.  @News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/65670" target="_blank">📅 16:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65669">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef101c520e.mp4?token=emIwQvQNyCMLynPSyKtZoHCP-GNjLYIIT8rsu25ihzq2utKO7tNkAox5Dl40bvB1MKRns4cxj-sNDVl4HI5wrmFipQWFMn7FC7liAw6GLFr8UxN9QIpMvWPSYLobISeUI6zsQaHkF5Rf7bo3EpkpqJZFxgPTiQbYxzzX7ZJuNXjKnYhEcFvqiK-6KdciT-jp9hrdesQjnQOcK33cKhFx6TcAA_izfxAkO3snSGovnT4QWwpcaCz-xoRBqcElH_XduULRhp6j7BDj2ybNbUjTcO9UqVMzyW2ReGMURypKzR_UFTuIKjlm8gd_SidPicenqFsAi5TBIcjgDFxn9xGI0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef101c520e.mp4?token=emIwQvQNyCMLynPSyKtZoHCP-GNjLYIIT8rsu25ihzq2utKO7tNkAox5Dl40bvB1MKRns4cxj-sNDVl4HI5wrmFipQWFMn7FC7liAw6GLFr8UxN9QIpMvWPSYLobISeUI6zsQaHkF5Rf7bo3EpkpqJZFxgPTiQbYxzzX7ZJuNXjKnYhEcFvqiK-6KdciT-jp9hrdesQjnQOcK33cKhFx6TcAA_izfxAkO3snSGovnT4QWwpcaCz-xoRBqcElH_XduULRhp6j7BDj2ybNbUjTcO9UqVMzyW2ReGMURypKzR_UFTuIKjlm8gd_SidPicenqFsAi5TBIcjgDFxn9xGI0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جزئیات عملیات نجات دو خدمه هلیکوپتر ارتش آمریکا؛
جنیفر گریفین، مجری فاکس‌نیوز:
مقامات آمریکایی مطمئن نیستند که ایرانی‌ها قصد هدف قرار دادن بالگرد آمریکایی را داشته‌اند، اما گفته‌اند ایران در آن زمان چندین پهپاد بر فراز تنگه پرتاب کرده بود.
دو خلبان توسط یک «کورسیر» نجات یافتند؛ یک شناور سطحی خودران ۲۴ فوتی با برد ۱۰۰۰ مایل دریایی و ظرفیت حمل محموله ۱۰۰۰ پوندی که توسط شرکت «سرونیک تکنالوجیز» ساخته شده و در زمان وزارت دفاع لوید آستین، تحت مسئولیت دولت بایدن به کار گرفته شده است.
این اولین باری است که ارتش آمریکا یا هر ارتش دیگری از یک شناور دریایی هدایت شونده برای یافتن و نجات خلبانان سرگردان در دریا استفاده میکند.
«ناوتیپ ۵۹» اولین ناوگروه عملیاتی مجهز به هوش مصنوعی و پهپاد نیروی دریایی آمریکا است که توسط دریادار برد کوپر در سال ۲۰۲۱، زمانی که فرمانده ناوگان پنجم بود، تأسیس شد. خدمه سرنگون‌ شده پس از دو ساعت شناور بودن در آب، سوار بر این شناور خودران شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/65669" target="_blank">📅 16:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65668">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
صادق زیباکلام از اصلاح‌طلبان حکومتی بدلیل اظهارات اخیرش بار دیگر بازداشت شد
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65668" target="_blank">📅 16:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65667">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
ترامپ:
آنها فرصتی برای امضای توافق و زنده ماندن داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65667" target="_blank">📅 15:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65666">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۳ اسرائیل :
احتمال واقعی و جدی وجود داره جنگ علیه ایران رو از سر بگیرم
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65666" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65665">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
اسرائیل هیوم:
وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده. ترامپ بعد از حادثه بالگرد و حملات دیشب بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65665" target="_blank">📅 15:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65664">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZtnSaUZYqlL3eR8Dr9PzLkiW-DZ1swURc4Hs3MkItWBfInoNtea8TKmMUdvJZngR4pk_EGysu_DcBDDD2nzjdzp7N2gkVPh_3JeDP8cgOQ0iGnB558E8m6nKr5seh_mbMo5bSYnXzOyxq3clE_5RQglbvL75nSnaARbiMPdHS4zaVMa8VwyMbah8M5DqNkI_BqCW417B1NzUB1DRlEHBzHzPczhNMpK52uSg9qceYlPTyPPXVHb94opDn_sgAwZkdlouFvpeORvDK26Yl4alhIhvIDtRNFxW-bCVfLPkemfTLdvny2KGVQmqpoLHhQICOFQB0zQJ_B10BiciSqcHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید رو بیدار کنید این کاکولدزاده دوباره شاخ شد #hjAly‌</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65664" target="_blank">📅 15:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65663">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHeuWMsUXHwFbFz2K4epwx3gTEr3_UVoiGLRguZzsldK0I4Ebc3vs0gYOi7K_KIwRpkFolEixeeJRwNhKYKJvMEfL_r5NJGWddadUmQGDh6QqUmxNQnjPA8g0hO0IovqwGeu2IOVRRAKke4xjltJzmoEPrkXYU6pWVMeJVeGsJyC-pXBw4ujoXEvdxffLj2_4ajl3XRUvkOof_OLsuhuBQ__3Q2ka4bOpu6XPVHOvBV-n7dQ39txTbCj_piRB_heiWLeqi44TZqahIVUr-9wfMnRhCEq6-pmQtfFE03jUeLSKFiMUzwtyn5hZtRqtlCrx2IV7SrMKAh1-E93aKetHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
رسانه‌های خبری جعلی از گزارش دادن درباره میزان اثربخشی ایالات متحده خودداری می‌کنند. محاصره دریایی موفق‌ترین محاصره در تاریخ جنگ‌های دریایی است. هیچ چیزی عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است! ایران تجارت نمی‌کند، ارتش خود را تأمین مالی نمی‌کند و هیچ یک از صورتحساب‌هایش را پرداخت نمی‌کند، و به زودی به یک کشور شکست‌خورده تبدیل می‌شود! نفت زیادی خارج می‌شود. الحمدلله!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65663" target="_blank">📅 15:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65662">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:  به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام. ما کارمان با ایران را ادامه میدهیم و به جلو میرویم.  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65662" target="_blank">📅 15:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
ترامپ به فاکس نیوز:
به صدور دستور برای حمله های جدید به نیروگاه ها و پل های ایران نزدیک شده ام.
ما کارمان با ایران را ادامه میدهیم و به جلو میرویم
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65661" target="_blank">📅 15:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ:  ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65660" target="_blank">📅 14:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM8zCOxESNv0fzfhsH-g9SQVdYfxYP7jtdFU53-G6y3aI3gsRESykzWc_8lqGjFlLaMVhpI8zNkrtH7i8birWwbIraUAegBE0hOE9QNY5_JijiP40lkiaEEcy2KNG11dQp8jHbLzzNbLvtpb-Lus_dsaDa-CVxKdsFmMt1e0WPhrx56YkgGxHMaWxjv6lSmH_H7jZoRkOlpXHsoIf9HFjh_4SMwdIel5m7EvgGaO-Fl1mq66y3roOyHHTYY5ITW8Rf-CtDTMfBQ8lpbfkHbGM6pwrlxQCCmsIozyC0lO7GL2dJSlhlM9o8eBHmrvZiJCOyyHfzPjNdRu2L4gdBxx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ:
ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. قلدر خاورمیانه مُرد آنها خیلی طول کشیدند تا برای توافقی که برایشان عالی بود مذاکره کنند، حالا باید هزینه‌اش را بپردازند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65659" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88679deb0f.mp4?token=d1XRe_MBiLx8FHaNfcSMrI2qyJopjNf1hE6e-VIMzSbdcBHPb9eb0IMvyMTHZS8937ZaQuA0IBZnM4vbxehcjwFbhhPmXU92QScuA41OwSbJq_osOGNYix5aoqxf4h3KemwNnGjiNX1890f216qCvOeNSvAj98sIa16I2KXcKpxrMkZAxHSiID85Xclnhz9cXJgWA-AbrAGbpOoHW3aw3PY-_5H_FIa155HheqFU-jQ0wshGijrGywFxs1bGWGfla_BUVGw30SVibRbI6VBWTZNkklYCB0Qg8ccjfQVb6-DhxbrEiGO9q2LDbeOOXf852R6CE79pCluRuaP99Y4jRYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88679deb0f.mp4?token=d1XRe_MBiLx8FHaNfcSMrI2qyJopjNf1hE6e-VIMzSbdcBHPb9eb0IMvyMTHZS8937ZaQuA0IBZnM4vbxehcjwFbhhPmXU92QScuA41OwSbJq_osOGNYix5aoqxf4h3KemwNnGjiNX1890f216qCvOeNSvAj98sIa16I2KXcKpxrMkZAxHSiID85Xclnhz9cXJgWA-AbrAGbpOoHW3aw3PY-_5H_FIa155HheqFU-jQ0wshGijrGywFxs1bGWGfla_BUVGw30SVibRbI6VBWTZNkklYCB0Qg8ccjfQVb6-DhxbrEiGO9q2LDbeOOXf852R6CE79pCluRuaP99Y4jRYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگ جدید تتلو بنام "رفتم که رفتم" از تلفن زندان که آخرش می‌زنه زیر گریه....
⬇️
دانلود ورژن کامل و MP3 آهنگ
⬇️
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65658" target="_blank">📅 14:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b931b462.mp4?token=N0FLrDiL9GHH08Kffik7dHlE8GXk6w4BBup-dK_chA9NZ3MDAS9fF06UtwJLG4NN_Das3Dafcy_hhiW2sOCVUG_kJz5mBvgLMTVTuSfqKQ79hckHEsz5JB_fOirtTptSpIcDqCRigt2ri7glcdwdbnQ_Uecno3H6PV49faIwAb6YgJxRK8fGDRupAwI_kpenxyx-O2Atmeq_RwLOhcnIG8C7dzDxVtAjsWoIpgq87AMV4oDh0Fw6zONs6cApqqLyQGHm8G_RhH6tmruQJRBt3CLdel94q43Ru4fvRH43a4FKX9TSF_a6nD6ePfNRjqAU0Myu5XExdmOQGr7U8zeGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b931b462.mp4?token=N0FLrDiL9GHH08Kffik7dHlE8GXk6w4BBup-dK_chA9NZ3MDAS9fF06UtwJLG4NN_Das3Dafcy_hhiW2sOCVUG_kJz5mBvgLMTVTuSfqKQ79hckHEsz5JB_fOirtTptSpIcDqCRigt2ri7glcdwdbnQ_Uecno3H6PV49faIwAb6YgJxRK8fGDRupAwI_kpenxyx-O2Atmeq_RwLOhcnIG8C7dzDxVtAjsWoIpgq87AMV4oDh0Fw6zONs6cApqqLyQGHm8G_RhH6tmruQJRBt3CLdel94q43Ru4fvRH43a4FKX9TSF_a6nD6ePfNRjqAU0Myu5XExdmOQGr7U8zeGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که این خانم از خودش منتشر کرده و گفته؛
«دختری که مدنظر پسراست واسه ازدواج»
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65657" target="_blank">📅 14:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99e4a5f08.mp4?token=L4OuYFsXom7CHwJ8AcnOnD5iO_aujADNGGpj6A7E94G4vMV0pZheHqsbYe8T25Ji8u14kaV_d5sBNbFzUL2oDeWDmGLs60VYfnufEACclFEjAW7y59D6LXjJIRPIJ_6bC86WyT-3rZsvA2XN92EHqhsL2a3kB4t4WPq9hsSi79Bd5X8VZ8It1wDhLJ-cKC3vFf-0bVBL3d_L9S03bNhsH4P1AgwSy-YqxuJbq-k-oCGhzatcUzBPnKeWRhCRJTIZ6Fur53rKQyqNL7ILT7aFFX_zrFVSGB9i_TpzCHnYmwcLA6-IAnmOLr9_zbYC1O0vjbwRdWImMBdRxPQp9nwZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99e4a5f08.mp4?token=L4OuYFsXom7CHwJ8AcnOnD5iO_aujADNGGpj6A7E94G4vMV0pZheHqsbYe8T25Ji8u14kaV_d5sBNbFzUL2oDeWDmGLs60VYfnufEACclFEjAW7y59D6LXjJIRPIJ_6bC86WyT-3rZsvA2XN92EHqhsL2a3kB4t4WPq9hsSi79Bd5X8VZ8It1wDhLJ-cKC3vFf-0bVBL3d_L9S03bNhsH4P1AgwSy-YqxuJbq-k-oCGhzatcUzBPnKeWRhCRJTIZ6Fur53rKQyqNL7ILT7aFFX_zrFVSGB9i_TpzCHnYmwcLA6-IAnmOLr9_zbYC1O0vjbwRdWImMBdRxPQp9nwZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران شهرک حومین‌الفوقا در شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65656" target="_blank">📅 13:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65654">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqzKX6PiJd39QXZd01yy3v5CobqSgQ542MtOydlgXWWviBwF2vbPS1j1QzLwmh6dQrJxhjabm8OJUk0Y7mBmbcnp0_G3YO-sr8TUaliFUvGCzd4vd0TdKNnC7cSdexSKO33JIPnPl_y0kOkOFFosC5vOa-f6h9Ru0O-t8twS792I8NNApUfMeeKaK0XeJCfWlYdqf7aIY71Wb5Bg6GcZeBLt3oVXA_8a2RF8c3Mw1_CUKubxGUAUbldeUtMMWH6ITNOXgvzO2j3g51YzjIH_wHTu-vlDhAMcgu7PFzROiliruFOsK7qTRWaNyA-CKvPnFe-c2LwMcMO3rlVd2FkdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان تجارت دریایی انگلیس:
یک نفتکش در نزدیکی ساحل عمان از ناحیه موتورخانه هدف قرار گرفته است و ۱ خدمه کشته و ۲ تن مفقود شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65654" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65653">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65653" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/65653" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65652">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2qpmb7NrM1r2uoEO-zBtQ5UKCLNk69KeUJR9HhR07oMySu5Yyw1-IiTAD_KuFHb3oCZQwaU0nBcXlH9FpBuIsCZ79_DhR0fH4_RGe5pZnkAO6GaycSeKADjbsMsnX47r8VYpDyn307hrQsT9FMaHqznfrFTKXeAOpa-numP3z3NrpybUdvZFkAgzyIrtNbPph6cM4RVUu37fQu5RVk4-YUYMKIyrnCdTjF13YPLmIzVBAzbCdWzxZgWdZMG8Jj511F13NIsKdQoYDBTkEnjtEJZL5wMwm9WmiF5p0M75cLF8ivUbOKwOlnJoOJyVOq3vV3cY8m7SIgiQM62EzhtRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65652" target="_blank">📅 13:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65651">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaXmpoX7TeW0cUTDLSA35rABosPDOIJEOF69PBcW1QpGwCAn3JwA60WG565KgeZjedfaZBZnxuFPMQbAUpL2DF3h6xR1Hkf8I0vW-2ZUSh5Sl0N2bNK0F7PrLRyvFh3k09COgRYN5ApVKVtQWoEK3dnBR2vDt4RWytkaSBHMAgtsGLd5w3QeD5HOkerjPnqGLhM-7G_jvS8h5gbhdsOs3WkxiHRClYT2Z-YmaH8UqUxVDi9CkrUwKVius-vEBLLk46kZspFxE2dHbbU3F_ko8CLRHffg42sbEsuNzZCjyusVY2a9nuHy7iLIMRN76ZDVipdAWgcffMryKBh8TptyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاتو پاک کن عزیزم
#hjAly‌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65651" target="_blank">📅 13:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65650">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
ویدیویی که ترامپ پست کرده: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم  این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65650" target="_blank">📅 13:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65649">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9276ffa5c.mp4?token=gdeCtsxPzzGwWpqnz3AYAu4Vc2vM6d_Ka6X-RsyQPTvR67yzfTkuXAY4WCnMsKuZhpNmOpbdDFr-YJDYeGNiIaIX1NNwm4z5YEEpbfZ6Qguh5bCxINRCw-aTT5-20-y2YgI8BslKRFj7z2FB6NAVg_F-OmHyFqKatHcERRlEhJaNJnhXsNSTVlkZg-gUdCQKh3m2tiI1PWAk8YQgaBKsEWOkpI6kKKgRctZ3oOc5XiM6XfKCGLB_NXT7qfKjqJ2ui1jnIIm6qb2_O56AqiQPyv7qPP5rmPZdrAaI7Pea3WhGE7bvIIRb4Al_NxtOKFz0thVgUQ9CEUl8suPJxY-0nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9276ffa5c.mp4?token=gdeCtsxPzzGwWpqnz3AYAu4Vc2vM6d_Ka6X-RsyQPTvR67yzfTkuXAY4WCnMsKuZhpNmOpbdDFr-YJDYeGNiIaIX1NNwm4z5YEEpbfZ6Qguh5bCxINRCw-aTT5-20-y2YgI8BslKRFj7z2FB6NAVg_F-OmHyFqKatHcERRlEhJaNJnhXsNSTVlkZg-gUdCQKh3m2tiI1PWAk8YQgaBKsEWOkpI6kKKgRctZ3oOc5XiM6XfKCGLB_NXT7qfKjqJ2ui1jnIIm6qb2_O56AqiQPyv7qPP5rmPZdrAaI7Pea3WhGE7bvIIRb4Al_NxtOKFz0thVgUQ9CEUl8suPJxY-0nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که ترامپ پست کرده:
اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
اهمیت انتخاب این سکانس در این است که ترامپ پس از حمله‌ای که رسماً «متناسب» توصیف شده، پیامی دوگانه می‌فرستد: از یک طرف می‌گوید پاسخ فعلی کنترل‌شده و محدود بوده؛ از طرف دیگر هشدار می‌دهد که محدود بودن این پاسخ نباید به‌عنوان ضعف تعبیر شود. پایان سکانس با تهدیدی روشن همراه است: اگر آمریکایی کشته شود، پاسخ بعدی می‌تواند از چارچوب «متناسب» خارج شود و به «فاجعه کامل» تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65649" target="_blank">📅 13:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSmJK5qcOWT5pqFOa_haESPbSNq3lgQ-VatUln00Rx_4nAXBZNxgHiDpkIrbKbn0rS1sfKQMAvNvHJVJSqty8-b0-22GMH9x8GDSWdKF2x5swEInsVHY0G6ufnXDsUus1RZJaV9lxXNe_6dZJc9UmjrU70d7RyfTCzVpZEPSfTyBwsDk4BTSDc5wtF--gyDKM1YYAjmjp0KBJhrKCK2OB11l7B3JYMK8boyBl__OaQDvUijQTDYUyI4uVT-M0IW4oSojrgMShDP1XnbJsLST9PlG9M-hXbokdno7AZu3jLNsu6WDvG6qyFzHOcHqms2KxJKwxejRT3J6vVao13Aaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kI7tSIhsPSbEnG0GMUlPXoGYokcDnnEF4zLeaYVEhRtnnZAY5Qcm24uHCnQvK-iBG03ehjUWTpc-EVHSaiflWEhQ6IYwRIwKFqERyaMcpQKeaPCX-EJBKzXNtkgfyBmcdU6hh6mvZt_EYs1KeXDx6LvluX_YS_B1XLCCGeYwvLh6il-oEAkCnb0rOv9VmSOeSCETz4MAVqvAcqg4fNSqPrRfkasOgvRAZCeWfE1udb9auxbtM-UaHQwbuqU8d0pifNIjCWxXwVF0v4vUSgjoJaSnPdNm-WHUh8AB9IQz0JwT6uZqUpFsYL__cSEq5yRB6RldIZn9pT1R4KkZED4U2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKWF0Jcx5mBAx-praFamabCwespJopNE89WIxmCxL_v9Ky7DICpJc00En0taP7bjkPk9ZkH6d-1VqIc8HvlczjGITcBmMZkCKV0olyNJV6W86M69WEZF1lB5dM0NoPHTntETE9bUQ-UzZefUMxf8CRoZq2syl1henx5vWxACWmZibwgxjGmBVRR4jh5uemJr2DvUKqBYb7__TlRMmHCnCwPoDJsVMXMds6gVbW8lhcHOuqw0GoXPsYja3maoWTsv2vNMfHpPTZzrZ022-Hs5G0Ck46bXP0zD_kCsBQhugQc6ihgo1_TB_EeROXRxqTK1nUhH-Wsvi-V31l8DGJDtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7thS9_Xp3OtpMPnGunUpuuDEmiUwVtxkuZmJk3-x04I5StpdM6LDyLWlnIcXGH47D-KFM3L3FWDMY7gyBPUJup2hv5FV2thWXNP5EgJPD759PrvYLNR68PhHtGVoTDBUt4_h7myB0yN4ay2Y2AGfNOmawD1BZ5md3NAD8eJil_W7G6LJasT9QdZuxU3oByjDfw-I1zWWkJPPyKwUcnx6Is4McR_wpw7MB9aDAzcCpRrRoAy_3kNqEA_XBjyEejThvCkyBNjp52TUkko7-U7MXUoMg6EyPi7rNXR700-J3BjSyPNMbvJ5t9c2C7IhxLmhU2wPkSfJ97RdEnJwfWNRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
حمله به منطقه طیر دبا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65645" target="_blank">📅 12:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef8e24b58.mp4?token=kvomGkYencikX1s_BhZO0ps27VBXarxg9l3K7_QXY_F4Hvl5ciUOLNZor8m0qxYvKzBORC5ejtGDbz0l8RqHYq3Mg_Ox-PNeJtX_ZYG5K0op8j7nz6XHP7dLYhB5XkumgXvcpvGsIZ7FfdLFSM5Lfb-qAFj5rtStz46P0ohZbGLH6PqoITUUmbwMEJRE8GhspEcXajGAzQKWF1YPy8ghghhJ56yIKI8Uhot6nss3GxCuDju_D8v6AZGYqyoch-R2YOgkJfKWbC9ffSaH3LPu54YRmXRyIL-F0E1W06CZjhHu8dygQJwl70Bglle2HpHHK1_WYxXinVHj5fkygCeF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef8e24b58.mp4?token=kvomGkYencikX1s_BhZO0ps27VBXarxg9l3K7_QXY_F4Hvl5ciUOLNZor8m0qxYvKzBORC5ejtGDbz0l8RqHYq3Mg_Ox-PNeJtX_ZYG5K0op8j7nz6XHP7dLYhB5XkumgXvcpvGsIZ7FfdLFSM5Lfb-qAFj5rtStz46P0ohZbGLH6PqoITUUmbwMEJRE8GhspEcXajGAzQKWF1YPy8ghghhJ56yIKI8Uhot6nss3GxCuDju_D8v6AZGYqyoch-R2YOgkJfKWbC9ffSaH3LPu54YRmXRyIL-F0E1W06CZjhHu8dygQJwl70Bglle2HpHHK1_WYxXinVHj5fkygCeF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
با توجه به اتفاقاتی که دیشب افتاد باید وضعیت مذاکرات رو دوباره بررسی کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65644" target="_blank">📅 12:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf0916f5e.mp4?token=WRXMcQfyBsis4mMfkb3qZQ1QMXHDyaGCpwM0MLVNPdHMdDHdcKPAqwuVbfsw6wUK_qVAEJ1gfcZefEv6IxZVgVlBtwB6qdYoUEIfyflh-9rcsdyLI7XLsx-DMJmxNJJipErWr9MFaIfxdwxCteix1jq39cUM7C_JNwjahaPO8CmFUYUTjzAI_gVI6-Z1cYEWYkgI83x7l_cJonwTYJfDVGzo4zQGG1TYg7um0K4Hq4z3z2OwvfJM-USsH_AHRJ38pwa_e6dfSAQyPdQsmaEbUicEwbJsvRBVPDZcHYqMGQdPL4-CsmpiEwF9Izq3R4j4fDH5PQATMs_zaMTMBfLfCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf0916f5e.mp4?token=WRXMcQfyBsis4mMfkb3qZQ1QMXHDyaGCpwM0MLVNPdHMdDHdcKPAqwuVbfsw6wUK_qVAEJ1gfcZefEv6IxZVgVlBtwB6qdYoUEIfyflh-9rcsdyLI7XLsx-DMJmxNJJipErWr9MFaIfxdwxCteix1jq39cUM7C_JNwjahaPO8CmFUYUTjzAI_gVI6-Z1cYEWYkgI83x7l_cJonwTYJfDVGzo4zQGG1TYg7um0K4Hq4z3z2OwvfJM-USsH_AHRJ38pwa_e6dfSAQyPdQsmaEbUicEwbJsvRBVPDZcHYqMGQdPL4-CsmpiEwF9Izq3R4j4fDH5PQATMs_zaMTMBfLfCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای از صبح امروز که حداقل ۱۱ موشک سوخت جامد دوربرد به سمت اهدافی تو خاورمیانه شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65643" target="_blank">📅 12:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65639">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGs7-_vb_pO15R2KMiUrY62SB0gJWQnJLBldSkPqyrKu6YArEAkdPUJ9lW0tWAlIRI1M7HcbSKOD30m9fM9-1I-tGPB_wrcfSzOY2zSzrj8KDipSm9cGno0kS6sBmyk85BYENDgs9tenrXEqYfICQMrcpbJkb9q1JdRYZxR8K4FBmdrGssBycvIa14zNsNl-pz7Za5rrcezzzb9HrnRHnPYtlRcWcnFDpTbJZE8IzYvMOKf41GOXbCmF1eoIDkhkjxm3fPDJgcjH_kLTFo6nnn42A7DxlsYImlmiRcuSV8AO1vP0aAVs5H8HX9olU76qsAZrtfFXgCpv0bQ7GDcjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONlQf_8bxVyUEbobcH6gnPHeNLPrq9E2V-yZcQQd1ZnPA4PgXFMckbkVE9PdzJHm-qcEtbydmfdjsAU_bStrRO59D2Eqog1bCAaabKKLc_x_iwx7uHcfavPwke3g-a4Tfl001DMaDI6l1NheN3Co_JfANtTe-lVa92IaQOIwz-xRWv9mr4w1HoIa8Rt2-EcqM02YHa7Q5GIJqALjEPN3oEKDPp9y7M6LYQ38s1qA4GOGlD3psqU3dTRs_n7Jmfgj70XF1zgb1cWlE6B7e8Bl9zSNtBFcEf_GBMMLBfoIC7Gk5gVWJBjikMPeqXhWdNHNKAdvtgKbTgAONU-HgP0tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_Pojb931FbqkXplbNNKMMYdxq7teArtAPzqMfuq-Ff9dm1EcnO8uiFSRRj1nHYlFH7htIs2uWSFxgHn4Em2Wledgn0JxKgA57jJFzF0rQdcCMGWiv9BvsYooaLypDeSLE_AOp6YgDLOO1MDLxxdnPpkvCRCCEgxallm_Dog2L-iITW_sRNHqWSgtGtpC4KAKHjqQLjx9-QSiHKsGE4WbOGfpr-33lejQeynZ3HxHxBh4V6hmgsAMczcysvApKeEMhAKpi9jY3rmWD8yUaIeOy3EVZOxkmCuUGsUiOptcx1PI9r3fxRSvVt4xhvO1mHwHSLjG_wFjDByhEMSsq4Zrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqP01Smcl_lKIlKGpkUJcmEpShkfiFfLJiYWddOsyq27757rhL5HZMASx2iDwVcZnaIWr0OTDygJWSm_OcYoHM5pAdRqI2gAv83h_iykV_VHTBLDQSENLZgai04YgQskbTWaltzubMBWeCQj11njmOEHMXqcddOew7HFe9fB6Gsh5dhvDvmS8PnH6QGxOLzOqSMBiVDwWRsLxjp3sGuxeQnS0G61zmQJVlvDcz8xVQP1NYQlcv1TAZIgc-kUhXJDZtbVlpPbVdS45ymRKEGmZFJ7wvDTwh5mgVvh7nNroBtfsBYVSBJsvFxfHZGo_4AifxSyazXZAO3Dn-Mhsw2Amg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
حملات صبح امروزاسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65639" target="_blank">📅 10:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65638">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دعوای ۴ دختر تو بابل
😐
@sammfoott</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65638" target="_blank">📅 10:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65637">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7m4Vl89uS_GkE3jAluG-7cRbvoT2xcMqZWlPYP8VK-sNAzvNM0cciABCr3xVdKI3P1ET7OB5KQpGlDzTDfVzqSoJjRjFQAGpz-c-pPraWvOTSjKx_vtS6q-hoAQuwEAf0JNSLLb0Q_FUIRodkZfs-hNqeuJMna4tdhkRQisAgkvAmtWLuWi4_8O-PcNlqUo_xU-x59jdn6nSbNdmijdVbaBw1jMAdMnWDFtb_fLK70MMPwvR7lq5N-pPt_Kzy9pRuia82Y3pE_1eXaeyMJmYnDPkJf5E8i2chhHc4tbzHHafEO3x4-Jlebc9mkjfUa0pyeyrkhNKc_Z911XlHHezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری که فاکس نیوز از آرایش سنگین ناوگان دریایی آمریکا در منطقه برای «اجرای محاصره دریایی»منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65637" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65636">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">😁
برا رفتن به باشگاه بهونه نیارید. از بی‌بی یاد بگیرید با چنتا کشور میجنگه ولی ورزشش ترک نمیکنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65636" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWo3UuwhMdbbbyzFPkCXQbmE5G-lHzI4w2q9IPwFy-TmP74g0Oy--q2I2aE5K-lEHrC1TDvUXkQ6x_GGE1WyLRM0F3kgjhbv_D-E940c-AipohnqLyCKZHkjTzcEkvDNhh4vk7ZH5A_s8BferVzKiOx5Gg-frLWWgDRkYAWAFol0q84vJWU-45jVmYQLLUHKnlGggxgwBOVQxnMpAm9QU2wH3BEESWx9cKANnxRirnCeCe7Q1-mAcKpH-NUUV5HcGrzwYKc1owNAofip6ghpspGh-pITUEeFGCT9zkUE6VqhSoAgQ-Q1aTw-WvRfBloN1wBnHu49YFsk5ftJ0R8cww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
رضا دالمن، دانشجوی کارشناسی ارشد مهندسی کامپیوتر دانشگاه صنعتی شریف‌بدلیل آویزان کردن موش روی تنه درخت‌ در ایام اعتراضات، با حکم شورای انضباطی این دانشگاه به اخراج و محرومیت چهار ساله از تحصیل در تمامی دانشگاه‌های کشور محکوم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65635" target="_blank">📅 09:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwoYlKNrdXpz-CjO7uyr5I6qMrEcW1yPLd3alr4tVM965e5Pj-egdMGngikwVXy68yQ97fN29KTGr9-062ibUxyQ2r9tD0QuhiHuxq6usSOK1ckRcixPBOlEDq4XYaK3hGSRJuQGd4bcA260eyaM7aqUl6F2-BWRps9usimMiUTT8Yfk5EbsB6PVLexGgO3I5T4G0tPyXL45YMqOp0Aq8ayg-Cg5TA41KxSuGBesS7XhQ0cROlQi61wiERIdsucJrQzwGF5o4Ik3p63dVRlb8g7fmSw27z-Jvx7cJoP4CgCLqeqy2SFDNgoBmNiTEHEnIEXE9WwuaNu7LYF3E0e1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تصویر منتشر شده از شهر قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65634" target="_blank">📅 03:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=I8WRoiNZMeLpT4zzqO_HoG_7wbdHqS2uKJaVxJItIpGbkn_lJ_4sFng8bvVd846QM6SqIrRQMAtEYXe4BPsUVP-pTBkC3K2WGzF9B9MgYHk59AQyYxsKBgtHjGH0kuIefP60MeOi0sYWcX-v4mEVVCD4Ryjd9HNDL8nCqwDAFWKsmRwwNwr9s4ybxNfamF05bOp4ZmfGZQ1IRw4y5v32Ekkvq7S4pfOuewaybt86dGDtG3hNjN1zlamRdKLPeYWXmEghoRBSYe_hq86RAUhewhfCX06tuoZ_rPsceoMMuPKoHM9Pmem8gZOaRCkmbrlZlT73LEgBHU-7erPpSHVfnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=I8WRoiNZMeLpT4zzqO_HoG_7wbdHqS2uKJaVxJItIpGbkn_lJ_4sFng8bvVd846QM6SqIrRQMAtEYXe4BPsUVP-pTBkC3K2WGzF9B9MgYHk59AQyYxsKBgtHjGH0kuIefP60MeOi0sYWcX-v4mEVVCD4Ryjd9HNDL8nCqwDAFWKsmRwwNwr9s4ybxNfamF05bOp4ZmfGZQ1IRw4y5v32Ekkvq7S4pfOuewaybt86dGDtG3hNjN1zlamRdKLPeYWXmEghoRBSYe_hq86RAUhewhfCX06tuoZ_rPsceoMMuPKoHM9Pmem8gZOaRCkmbrlZlT73LEgBHU-7erPpSHVfnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک‌های پدافندی سپاه از جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65633" target="_blank">📅 03:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام ارشد آمریکایی به کانال 12 اسرائیل گفته؛ هم‌اکنون موج دوم حملات آمریکا به ایران همین الان در حال انجامه
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65632" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBt6y4iuOuLWgqDKxgdLjnT0KKNxhgQGTevGAG2UtjN3jOisgvS2pT9o1Op_bhDgJ3jcTJC7tOkbqWLNTZAqEoM61tsEIZjUNnnjKssVSySv9CPlf2VzcLZ7DPL2WagXvtluERdgjCSOrvdDMbw68e6V40ryrEk3cTCYfV4ubehqjORPdg_yYhwBV4at0AT0Darcl8nYElHEebuDhzYjCZuoOATJayFbWNW5TxPn5wVHbEUHzZv7qTfkGg1p8nwTKhjB6eXTiFjP6Nmx11Oqb0FiZMx7m30sQkOatZMD0f33Zuyaen3Ssiaopamp7u6jrU5mDdt86ULaunrXx4XnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🗳
کانال رضایت ها :
@AtlasSmartTrust
🌐
وب سایت رسمی ایران :
AtlasArbitrage.ir
🔥
ربات رسمی  :
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65631" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65630">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65630" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65629">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_0ley2EFEL1D4-Vs10zuTv3xSZUYGx_AKEZLODHdTT1aR4KYUEyVJ_cv9QuXCA6PDKn-Ez7SPaddFBZF62yaqnXdZM2ufY5Cg4LW4pGVyewwV_2zDnbwG-LpGQ-31zCr0l8G3NGtkK0BBcNrhJV1S09EsTazn_AIaZ9eEHEc-HjZWiWZoBy7KYRXa48jviywVK8879m80XNWk4UCsRexVuXDJ52IOYiv9i-rvJPgu3oVYoSEl-7z73EMCAN2dG4-dKU6LrvBlPoW_XtB6r0tu3DYbbJQo_frIz2cjMdQMZRKgUC99H5x1KSUwqaR6TtqKH4rmFe2q0YsxNXrBGjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65629" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65628">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
گزارش ها از حملات ترکیه به شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65628" target="_blank">📅 01:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65627">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65627" target="_blank">📅 01:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65626">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=uDYSgXr3bstyaTBXt77jfOWSVifpGSacry33iyGYzPHGzZyq6VS1uJG7RIV75MOvavb37QemxmOesV841llvC2TdBe1JlujxbkJUlipUkgI63YaFlFQEpwYtmNXIb_DHVjq1ykaQuhKHInrmrrEemTUVAHmbskXqlbWTah3oy1hYXRfkbniT7Y7pknYzkz7QosJ-xU1_PeESvsTt6L46cdw6P1mg9u94fLgDl4pX9UX7sTtXKYsrCZKucMqQ0gsG-zQweq-LvgwgavjivIzVr-9CRLW4xieu9bsZJRxf3GCWEwvjX0QU3e2vCBxP35rm4Nip2iUOsawgJIYo0xlB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d15a212.mp4?token=uDYSgXr3bstyaTBXt77jfOWSVifpGSacry33iyGYzPHGzZyq6VS1uJG7RIV75MOvavb37QemxmOesV841llvC2TdBe1JlujxbkJUlipUkgI63YaFlFQEpwYtmNXIb_DHVjq1ykaQuhKHInrmrrEemTUVAHmbskXqlbWTah3oy1hYXRfkbniT7Y7pknYzkz7QosJ-xU1_PeESvsTt6L46cdw6P1mg9u94fLgDl4pX9UX7sTtXKYsrCZKucMqQ0gsG-zQweq-LvgwgavjivIzVr-9CRLW4xieu9bsZJRxf3GCWEwvjX0QU3e2vCBxP35rm4Nip2iUOsawgJIYo0xlB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پهپادهای سپاه در آسمون عراق
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65626" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65625">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlFX_gKMLkhbh5-QlAb3F3s1yBWs8kQqetTxFqb1mlbBR9aQijAyF3z6RkpdTHq0GTicShRIEXAqg9wpQVV7U9zOow9JDpofHDS39f99eOVKzYGgyVnAgX_ph-60eXbkMBURo5CizoN2RaNb9s8Prz3LixFT3BlJS8CvjSnUoAI3kJiKHghPcvSDCdcwz9i6AZNpouTZNtvjdvrblJu8EGcwIWKT0626TUT0DRIfMv2AT-PWEg7KH-XzrCM7nnBnM-H13MzgyedYKv-iBL5G2oH8mpA78CWoXVDdka_6N-t2e4zeU26sWpvrghxm-HCXLXj0lUt7z1vFkG7qN8QVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار تخلیه سپاه برای بیکینی باتم
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65625" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65624">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2yplze-8QHgZqgrmlJurDcadxdiJbtb1gQ2JvZv9HmvRUSUJ2B_xi-wrg4HH0Izm-RAozOnzpJqgqrg3aZg24zbf_bgXcDJnq4AnuTrZFl2CbhloHGSwOatHFgTH3fGZuL6lJNqs6ihQQAP5Ssc83v40DPCEeqdezhZ_VW7mzO0dI03mcQ_lAuA4O_qSHucDNrf2edUJ4sMSSK5tWFkbtvTj3juTLoNa1S0Q66pRSozw2lVRQLpD6CuhmMrUHZte-Nwisoyh3Qsghd4Yodz4-GOSrblHTogNDnyAg_aigu3J3ctcxl8iyY44CcbCQQtiHDo56-6OksLkEtTYd2NjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
علی قلهکی: برآوردم این است که سنگین‌ترین پاسخِ ایران پس از آتش بسِ اخیر به آمریکا داده خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65624" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65623">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehgwRf13GqShuuUKcBBQciL4f7RL0X8orOi-a9mqRaHUij4qv1FX1ZCXz5ID_XyRx5GZF7JCWQIBru4Io1FtruikCKthdoVSdqkx3TGpZBNlKIAK5kT2zO159Nr0t195zUEXjl6_YiO9IkPxjJl8xjGE92zcnfuzI96FjHdWqbA2H0bnnNQa4hG4hR9q2vTDxbyUJvq4zRS4s0BAD_PlYTHmmv50Z1OtDeIRQpmZdtHXVzfQJ4yNPR5W7vK3lfA3ZbNmyOvJTfkcDMaKxBeDmyTIqJurSZccdQaYoCbpxagk3EqAXrBv2U5M0Igp6OzVvy0GfPOIliUm6ZFZ0sYokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلند شید برید سر درستون کنکور به تعویق نمی‌افته
✍️
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65623" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65622">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65622" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65621">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
کویت و بحرین هم حریم هواییشون رو بستن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65621" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65620">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
حملات پاکستان به افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65620" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65619">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHNpQ-aeIM-AjC0nYGibYMkT9o6ajeSBSbJuLjbZI_dIH0U9hrCRLqzczT418T_RZpLHZ3NmfJ8jv8fJmeDTTGl-whPxTdnD0oWUhFKwk61vr9bi4yR8cNmkWB-UbA8hAJ1wdyfYOzEPEDSk838p-ydwIxj0SPlOz3OBCoQZTilS1AktDPVoj8SZJTy3hNhIHuuOByfDevrEF-Nab6UYAG0YHWz4UkKxOFUELZp8qK-xDLAV1QNIn0b7M0uSNniwX8ocTkL1PleOLbrB5L5Notubrqn2zvGgjQWzj8nd-SCOzymttDeBG0_KGps_IvV_Lqs6776vT8zHX8L7NbyIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
توئیت جدید سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65619" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65617">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی قطر بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65617" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65616">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇱
گزارش‌ها از حملات اسرائیل به لبنان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65616" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
سنتکام:
حملات نظامی علیه ایران با دستور مستقیم ترامپ انجام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65615" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65614">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود! #hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65614" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65613">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛روابط عمومی سپاه پاسداران:
ارتش متجاوز آمریکا به ۵ نقطه نظامی در خاک ایران حمله کرده است و باید هزینه سنگینی بابت این گستاخی خود پرداخت کند
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65613" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ناو آبراهام نه تنها نرفت قعر دریا بلکه با موشکاش قعر مارو داره میدره
🙁
🙁
🙁
#E</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65612" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
صدا و سیمای جمهوری اسلامی گزارش می‌دهد که در چند دقیقه گذشته یک مکان در جزیره قشم هدف شش حمله هوایی قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65611" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65610">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از هدف قرار گرفتن پایگاه دریایی ولایت در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65610" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65609">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
ترامپ :
فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65609" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65608">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
گزارشات رسیده از حملات به مراکز دفاعی میناب
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65608" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65607">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65607" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
آمریکا گفته حملات با موشک های کروز و تاماهاوک انجام شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65606" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5jJLiWINeX0TwS98Gi09aPS69PUdUwSiBT8Cbv0DV2AxJVNB1TjsUUJbLhEcPAV9Ftfonb0Fme4pjV9Il-W7R6M1t6RY3SGj6IRyhDckzPBFVegcpb1MTHYbla4KJnN1G1wtW54KC_B-q18TP2of0YsCIeOKv5aNAUfXckqfqgcnYH3S0N-iT-S-SY1q0tq0A2kAWFUvW5CrczgnQ0DYiVCPy9FGcJzLI33hys7kQZAtZl5W3LydlPI24F1k_epcD4rhViB2dbF62xaidwgBD21R4ltRv6GuI7x3tiEpk04jnPxRm71lBkV4x2bRZKfM3Ut3SHC6CoGAwkrjxxlKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65605" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65604">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">احتمالا هدف حملات پایگاه های موشکی در بندرعباس و قشم بودن؛ و پاسخ جمهوری اسلامی به کشور های حاشیه خلیج فارس خواهد بود!
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65604" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaleh</strong></div>
<div class="tg-text">حاج علی از پارمیدا خجالت بکش
اون ایموجی گریه چیه مشتی قبل جنگ ابهتی داشتی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65603" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65602">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtX3HM4iGvFKWjs8Bu2frbB0hiGyXpc3xXL0D7oW3EQbPeUtaQ6Dj-JYnw5le1QxD6YdFaDhPxWwW04-riTjJ50gJU58r9fOjBhWE2tlzAAHRUta_22spyJ-qFnKsUY1qaRU_nkvdeoGBWLIJ8Hb1ZxT8vQR3QMSqyNmScWuksogY5k3Qtvxw1_NqSow-x4daOyKkS6TBI6RgU63REedSs6Fme4oX5snDQHG0GOX6ajQTzOm2tnxa0KxNxOfOSBquvT_L9tFbd1UnuYZ4U363mUSIF-gErnFMHNkNN-1ObIPS4rgXXc_bg-eiPekJRRSSIT_ZVWt3UiPpIdgDmEWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اصلا حرفی نزدم که؛ حرفام هشتگ داره پایینش
😭
فقط اومدم به ترامپ گفتم کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65602" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65601">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
گزارش ها از انفجار در پایگاه نیروی دریایی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65601" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65600">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvou9rc1Y6pDnhiIuch5zW4YoF94VQ_kxIZiwlm0gKd-jMCeClUqGf3iOT4cdYiCSpQPDiSc0pQNLJOWaaeG-QVuvlZ1B6rykBn9zSFQyF6NIc1cTt2YCVbusESRkrMY6PRaHKhzQkv5Xrf5aSUml30YGnRuJcOI6oaMCI66PcMjw9hDExVFEZ-2AdrzA4J-7dEwCMQi41N9SJ1mt2F8R48PRxeppdK8HeiX3g_jIgDrOvWx5pajLEB_FWHIU5MD1CDy4NSJkCcYJ25LNLmH_i8RhzztHDtnode9POBv-oU_yBW2rc4SNZ79DaUHUjnUbEYhIjtikRC5OLKsMIcqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اصلا حرفی نزدم که؛ حرفام هشتگ داره پایینش
😭
فقط اومدم به ترامپ گفتم کاکولدزاده
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65600" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65599">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران جمهوری اسلامی: عملیات شرورانه آمریکا را با شدت پاسخ می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65599" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قشنگ نمی‌زنن بیناموسا، ارضا نمی‌شم دیگه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65597" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-pJcWHdLkQ_uDnkHQA9qYqILELPyjMmyRBfGnx3NjqJukjoEBBGkqRRRBaDtD42HRs73gjeJgMo3wRrlmP5M66iJB9Yf8Az6wGuNI4RGN9f_rrl1V4F3xaFzSg6VAHW1ShEjqnoaeWtFTHdwTWe1D6QQlFHZL51cC9NCNQC1liKwM2VYrRH4rMAVaYhsTcPjs9UN3Os_yG-97K0OsoNuRbrl4wTc2qgBCoWhEFAKEgtThP5umWMV_wAvduLMehKsHPw-acy-3GFEM3n-Z5bBhBNH4w3SBWJexKD1KElwI_VCw5KJvDloKe_yxC7OR6XxFJ82jW2I0Ardu1JDiuFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده سنتکام، رسما آغاز عملیات در جنوب ایران رو تایید کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65596" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65595" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
انفجارهای شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65594" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از هدف قرار گرفتن پایگاه شهید راهبر در بندرعباس حکایت دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65593" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65592" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
دقایقی پیش حزب‌الله به شمال اسرائیل حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65591" target="_blank">📅 00:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
‼️
سخنگوی کمیسیون امنیت ملی: دست آن رزمنده ای که در تنگه هرمز هلیکوپتر آمریکایی را سرنگون کرد میبوسیم.  «هنوز هیچکدوم از منابع داخلی رسما سرنگونی بالگرد آمریکایی رو گردن نگرفتن»  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65590" target="_blank">📅 00:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ما که از بیکاری و بی پولی رو آوردیم به مجازی وگرنه که تخمی تر از خودش نیست
🚬
#E</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65589" target="_blank">📅 00:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شما هم مث من حالتون تخمی تر شده و قید مجازیو زدین؟
😂
دلم برا قدیم‌تر ها تنگ شده #hjAly</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65588" target="_blank">📅 00:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شما هم مث من حالتون تخمی تر شده و قید مجازیو زدین؟
😂
دلم برا قدیم‌تر ها تنگ شده
#hjAly</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65587" target="_blank">📅 00:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
ترامپ به واشنگتن پست:  محاصره باعث شده ایران «بسیار فقیر» شود و آن را تا زمانی که لازم باشد در جای خود نگه خواهم داشت.  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65586" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ کاکولدزاده حاضره برای رسیدن به توافق، ملانیا رو با عقدِ یک صیغه‌ی یک‌ماهه، در اختیار کینگ‌وحیدی قرار بده #hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65585" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAWqAo6-lPo4NJn8FK2skd40hKGr6IGeBwhETFJ7f9IhUD9HnWZUK0z1GvxR96KpyBwOyNDiMAyn7BOxp7I1BCnobIjCzXbjt8xquHb0FEFYZkvIorPlwWBFyWDqcC46dRx2uEQkKLU7dGdeSj83Rb6vkjJ4l9XIBNNC6-mR9UzpY0kFuWIOR0RlFxRGLAR8sVJ8Ou0wunMDROBkoluQ6-phwAO2Kc14CHsUDy-Vf_cFyAUh1BdhXM0vElJLLfFoIxsRBjHLG2JZ-DCP9g_ZlfCZ8uTo2lDOHt-LA7iLghanS5ncb2NxrFyxWYxCPYvh2JfTlDgqlVRmW1ZReBuyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
سخنگوی کمیسیون امنیت ملی:
دست آن رزمنده ای که در تنگه هرمز هلیکوپتر آمریکایی را سرنگون کرد میبوسیم.
«
هنوز هیچکدوم از منابع داخلی رسما سرنگونی بالگرد آمریکایی رو گردن نگرفتن
»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65584" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه پاسداران: هیچ حمله‌ای دیشب از سوی ایران شکل نگرفته و اخبار مطرح شده کذبه و ترامپ داره دروغ میگه
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65583" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
ترامپ به واشنگتن پست:
محاصره باعث شده ایران «بسیار فقیر» شود و آن را تا زمانی که لازم باشد در جای خود نگه خواهم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65582" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65579">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
شلیک موشک از خاک یمن به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65579" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65578">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📌
۱۰۰ میلیون تومان جایزه نقدی - بدون قرعه‌کشی!
📌
​
​
✅
قهرمان جام و آقای‌گل رو دقیق پیش‌بینی کن و کل جایزه رو برنده شو.
​
⚠️
ظرفیت محدود:
فقط برای ۱۰۰ نفر اول.
به دلیل حجم بالای درخواست‌ها، اولویت با کسانی است که زودتر پیش‌بینی‌شون رو ثبت کنن.
​
🔸
برای مشاهده شرایط و ثبت پیش‌بینی، همین الان وارد کانال زیر شو:
💵
​
https://t.me/+5uTOXJ02mftjNzQ0</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65578" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65577">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
♨️
شورای امنیت سازمان ملل رأی‌گیری درباره قطعنامه ۱۷۳۷ را پیش برد و با ۱۱ رأی موافق، بررسی بازگشت تحریم‌ ها علیه جمهوری اسلامی ایران را تصویب کرد. بریتانیا از فعال شدن تمام تحریم علیه ایران استقبال کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65577" target="_blank">📅 23:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65576">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار یدیعوت آحارونوت: حملات آمریکا جوری خواهد بود که هیچکس حتی فکرشو نمیکنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65576" target="_blank">📅 23:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65575">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZNiEKBRxiUNesgqUUnPCN0I2El-hg5BRXramii9Ek6zKOnRIw7tj0Mq5siwMoONPfPak1nbtMJ4xrgVwfusOH-kUS6OT48gML7_fwEN0iu29DkZG0t8cf6bs_oZ5XAPL3PyeN7LXzbpuoQcY9uEzccfMgVmyApjTbP3LqemAkosPDaxHQyjB6LNI1M-jfRu8w8CpAvcIxfkBtQL45Xu8WYYof_FNYQbbQQSTKPn5jvlFFVODVFNNBMZFNzl5Gw4xXyXkVlvxRq2-QYzjoLF-MXQ6lDWMAI4PuOl5l3Ewik_y2ZTCdZzCh_uNdba4XtmLPNlF5_NiFTNDrQqJ-caxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
لیست ترور منتشر شده منتسب به سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65575" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65574">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4SCmWwUzGZvSAnvWXS9q3-VfLJTINM1ftGDxqrp9KAMAchMoZuMTN6Fjoww6sdNRTuzFg2sgGx9McmrzYuqJlw82_tXXu_j01QOd-RI-rXs-Ww174OW5JyYBx9Xtiq_Vot2Hook7a0AJyMXYjxY234JEH4jJyC_PDIBg0xesiUr0FQz3YAAxeY-k5um0Fn41e7A57aTSppCzHzjg3st6XAxgIB-2ddGjr-9sg89DB-mmhnBjc55ZZrFi_i53ZwUdD-YwJTrCSyAPSWZZv0vjDczHGBpyjQjJSwjppvBChPswkMGw3sCrvz8KkehIWZ_Pr6tl1O2NG-4Mv4BAg_rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فضای پروازی ایران کلیر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65574" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65573">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
العربیه به نقل از یه مقام آمریکایی؛ شواهد و نشونه‌ها نشون میده که جمهوری اسلامی بالگرد آپاچی آمریکا رو عمداً مورد هدف قرار داده بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65573" target="_blank">📅 22:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65572">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
♨️
حمله موشکی سپاه به مقر کردها در عراق
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65572" target="_blank">📅 22:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65571">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39f367b1d.mp4?token=i98ONSvek92qRRZ6MCTkqOoutCvOFr4DxXsxf78UUpMlM2mbzcekieVSoQAmHz1gf0BWGBnuVrOLBcXx6rztKz_pf4AEcZJ_4JsuJ8mGreN_4nlVRBU9nSytf_sIPKt0rdSKEuBUsXDhP-68LWvulmrYtw--BD6gXOjsIIZiyHqWnjTxvctkI2XU_U5LMWXXBPl_kPIx2btcnovRJGGHLuk90T3x5fytvcBpX3qgL4nv4jhUrvSTmQQ9ZFr_JIYDiOvjABo8BnI9iHWpBs9-jHIhUp8PSVpX-qKSD2mC-j_UtBadMotx84VI-TvnllN4iPwuY_JaTEUKYteiLC3Qcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39f367b1d.mp4?token=i98ONSvek92qRRZ6MCTkqOoutCvOFr4DxXsxf78UUpMlM2mbzcekieVSoQAmHz1gf0BWGBnuVrOLBcXx6rztKz_pf4AEcZJ_4JsuJ8mGreN_4nlVRBU9nSytf_sIPKt0rdSKEuBUsXDhP-68LWvulmrYtw--BD6gXOjsIIZiyHqWnjTxvctkI2XU_U5LMWXXBPl_kPIx2btcnovRJGGHLuk90T3x5fytvcBpX3qgL4nv4jhUrvSTmQQ9ZFr_JIYDiOvjABo8BnI9iHWpBs9-jHIhUp8PSVpX-qKSD2mC-j_UtBadMotx84VI-TvnllN4iPwuY_JaTEUKYteiLC3Qcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
متکی، نماینده تهران: قوه قضاییه حکم اعدام ترامپ و نتانیاهو رو صادر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65571" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65570">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_gCb0UdFqsYTmJ-K4uONR7PYbSSUtfydWldpK308eafIki3aqZdc8JrKxzqvnZstuVpHAiqpg-VJ26f-Bvk8S3JjVXoyTWPh3j5umjUTEItekQ8NAfATpjw8-VQ9cIeizwB5qHQhrWjmsq-eZRZBVlZfKaJjc2D2eu3NdFgsTm3Y_Vek9z3QvNyvyn22xj13qNTgf01Lz1pyvNSIfQ9kYGiRLS6AUoWhtzCIplOORvrGuiLvKYnQCVKsQr6GUQ2oGPLbybjsJT4abEV4xx8uBdpj0-KFkURBOJRA9tPShbWRjuBP-aFf67hBAC8Iesrd72lgzvvaAK8_5Vc1b0pTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65570" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65569">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
♨️
قالیباف: در صورت نقض آتش بس توسط آمریکا، ایران دیپلماسی را کنار خواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65569" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65568">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a7445c3.mp4?token=pXlyut5ktQGqJn5SzP2tjGB1caQ_iznavWKLwkemQSxVdVUSx-oi4lQ6ZaH9QzJ-9eadAmdGSs17VsuywNclY9zZwc05v6RwGrlG2Vv8mZo8emMLCnLnHyb0Nv7MjrwjGs1WRiYDA6qMSJ4Z9WVaDCWn9zAuwRN4px9kSFmyPmNPD-liJRAlW8CraZ0an7PAlcFwzfmxZ0p01_XzSEVY7NtZqv5AghSb1frJ7uBS8bsY6ttri0iFFgBcsHhlSiuTe8iVYdih8j7qVWAdfOm4SH2SR5MMcC7I9l-cTgpZf-Rb_KZ-9KZLWgHhv36qWPYHpift1eJDosf7fo966cDZhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a7445c3.mp4?token=pXlyut5ktQGqJn5SzP2tjGB1caQ_iznavWKLwkemQSxVdVUSx-oi4lQ6ZaH9QzJ-9eadAmdGSs17VsuywNclY9zZwc05v6RwGrlG2Vv8mZo8emMLCnLnHyb0Nv7MjrwjGs1WRiYDA6qMSJ4Z9WVaDCWn9zAuwRN4px9kSFmyPmNPD-liJRAlW8CraZ0an7PAlcFwzfmxZ0p01_XzSEVY7NtZqv5AghSb1frJ7uBS8bsY6ttri0iFFgBcsHhlSiuTe8iVYdih8j7qVWAdfOm4SH2SR5MMcC7I9l-cTgpZf-Rb_KZ-9KZLWgHhv36qWPYHpift1eJDosf7fo966cDZhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت گسترده جت‌های جنگنده بر فراز بصره، کردستان عراق و مناطق متعددی از جنوب و شمال عراق گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65568" target="_blank">📅 22:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65567">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcI0B1W2neB12Gub_9ESP9q2qQTyUGHaFXs9T6PfOL96eQkJ91RflcJu59-hfNgIJUDcGgUuQMUYgbk54aCcDSm45LXA5PS4aOSi5m17nTXWZSmrNJxNeSsR0epM8myMePUfxp0jos_9UJYyaudeYdv-EjRNe-Y88umtnjdn_PzhOSAVE9XQaNjhIzIauzkuTZeU7IYoOutEsAcuTBXVm64Oyt-95koOEOuPv1sRNmui7K5WjiODfDI5D-ksZM_RCaozaXFfTX-ngj2NCZgZ-92kMsw74JA8CI9kXjWsVu2E_jo_crHfWh6xT0qxS5Ae1jpdqBRqI_uFC12A5ufifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فعالیت حداقل ۹ سوخت رسان ایالات متحده در خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65567" target="_blank">📅 22:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65566">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
صابرین نیوز رسانه سپاه: امریکا به اسرائیل اطلاع داده در ساعات آینده حمله را شروع خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65566" target="_blank">📅 22:28 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
