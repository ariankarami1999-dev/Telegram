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
<img src="https://cdn4.telesco.pe/file/HWf9qKvYnNC_OHaG7dY5BvQ_b2k6wA9cfQEaCO2jyRkkushrJquGtOyEeDBtYAdimyFZo8DGzN370gufoM97Ovc9YHwvXOOaQ9IiDsFEaUPkH_0PkhSJWNFbJTU0dgSLn5krsPlcdALBEqR_v0Yei8HoY3RVXqzWgve_cJlX6NcdTHzF67qXBPeC1YPkh6uI7aQsHFGTumb5ORPujpt_wugrqfiYoHWXqk-SSgJPjdL_NlYB5SZ3XS7PhObvoM1gphs66Wvt7mgLg047k_AiffslHOpdbh6mckfOTV3-tQzgT0yLbLXm3xMQuhud5loUoJezhRbEqCKS8K23mMiD7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 137K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 15:03:20</div>
<hr>

<div class="tg-post" id="msg-65051">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/news_hut/65051" target="_blank">📅 14:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65050">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ-ZAVlXoKO7TQVaQ6v2inZivZCrOpn_im9UcvLB0usvp1LuNazYGFXiaXl1kz91rLfuZkdmooh92KC3Y6DosUHzTmF5q3yirpIh87W1OkS8WsjbPzZKf1MRxwtWoFiukylcBhGi-lqXDSL9xn2O3JkEEXme2gR3kkbntPcqc4zg8tXEksy4aGk0ZB3KqU-eJkdbqKghgeaH7eRNNsU4p27mf-75OYcCt2yac4f8mO02b3u9-F34MQccqd9qEHRiLvUzZUXUuAmFWQZ_72yICqNEFKzeHAT8j6Y1rrm60_iGaM83aFwhFDBYSxaz-mHu70hvs8Ed_UtUCDr8duL5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/news_hut/65050" target="_blank">📅 14:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65049">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=n0tumdSiTBnReTq9rZdT1ohVZ1tKsYXHwU5b78ThQtBi0PpjnDloEqtPuaaQPlkP2b41GLi3wQ1TYboUrbj7P_zlwTi8oJcc6Oy_cYyzKA6rIhNNnOYGTgb0tr6UxQLw3rz22htN24upCuyg3TRoqyp7lRSmGIZrkkHJQxtCO1uPPlukw0qn02AL4MMrnRlf8ut0dk5zj7I2_AyDNcckb_diSMa5c4DrN1s4Uhli82X3-3-ZvQiD3R0maYqLefJ14EfoBJ4IOt8A9w8S7eItBLP9LsldVbeeFx6v338pHTpni4Gvb4PdK5__Xw-Rz2rRgp-wQpGipCtNxT5TQ-Zwqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=n0tumdSiTBnReTq9rZdT1ohVZ1tKsYXHwU5b78ThQtBi0PpjnDloEqtPuaaQPlkP2b41GLi3wQ1TYboUrbj7P_zlwTi8oJcc6Oy_cYyzKA6rIhNNnOYGTgb0tr6UxQLw3rz22htN24upCuyg3TRoqyp7lRSmGIZrkkHJQxtCO1uPPlukw0qn02AL4MMrnRlf8ut0dk5zj7I2_AyDNcckb_diSMa5c4DrN1s4Uhli82X3-3-ZvQiD3R0maYqLefJ14EfoBJ4IOt8A9w8S7eItBLP9LsldVbeeFx6v338pHTpni4Gvb4PdK5__Xw-Rz2rRgp-wQpGipCtNxT5TQ-Zwqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد نگینی‌پور، مستندساز حکومتی مستندی ۴ دقیقه‌ای از حضورش تو پزشکی قانونی کهریزک منتشر کرده از اعتراضات ۱۸ و ۱۹ دیماه‌،
تو خود مستند حکومتی که منتشر شده تعداد بالای کشته‌شده‌ها و کانتینتر های حمل جسد دیده میشه که جنایت خودشون رو به کار دشمن ربط میدن و ابعاد بزرگ این جنایت مشخصه!!
@News_Hut</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/news_hut/65049" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65048">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/news_hut/65048" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65047">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=s3IG9X_NqzYUCCPHDKmfT6gifTMrfY8ln5xBnM2s0YsHBSLrhM0Po2z5jgxQhjb4b38k80yvugYf1uqN75X6wtvcscHOAzU_sfydop19zgI1f3b4jtTpvZ4nOY5hf5wF5R8K0sOBI-SGTS7mLszjHqtpIvVqHLkBq9qg5rqhpFJUcBrDs4RJlEkjceRd7MWfRbiCAC1due_MTLZ1K-I0vpu2z_V-CySsQOqs0HuqsVcWANKxCg3sqSs_7b1892LsHh1kmSqydx_8hR4EIyTEMNk5xKoNz9lBINCW3O77iePMRsTI5CrNHdehYnt1ngzjYzKOrfwfv12l6obyZSKagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=s3IG9X_NqzYUCCPHDKmfT6gifTMrfY8ln5xBnM2s0YsHBSLrhM0Po2z5jgxQhjb4b38k80yvugYf1uqN75X6wtvcscHOAzU_sfydop19zgI1f3b4jtTpvZ4nOY5hf5wF5R8K0sOBI-SGTS7mLszjHqtpIvVqHLkBq9qg5rqhpFJUcBrDs4RJlEkjceRd7MWfRbiCAC1due_MTLZ1K-I0vpu2z_V-CySsQOqs0HuqsVcWANKxCg3sqSs_7b1892LsHh1kmSqydx_8hR4EIyTEMNk5xKoNz9lBINCW3O77iePMRsTI5CrNHdehYnt1ngzjYzKOrfwfv12l6obyZSKagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم.
ولی ترجیح ما توافق خوبه.
@News_Hut</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/news_hut/65047" target="_blank">📅 13:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65046">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قالیباف دوباره به عنوان رئیس مجلس انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/news_hut/65046" target="_blank">📅 11:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65045">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZc4cMZjNE-_5oT8xWpVl1-ACXcAo0MNfKc74eQQM3cXVMYEKcNoXYn0bqITGczC6O-kkff2klgm6L2bDnSPK59ey-GvRfznam0wQ2tYieYWg5gtMoSEVtT4RwsW5fkNxZQfkZFBH3VksojdCtmebBHD7e11XST78Auhl05ezo3Ppv8YvvV2ba_qixIHSXPm23PDMX3U2IVl_4B25ix-DPX49PUlNLeBG5DFTHFEfdMNow3tVEY9l4vzm6PtzkixPgKFuzCjM2M9TLVXyl9xvF9oofGWraaKOBTxGoZlHuYQ0Q4Bq56iAbIKN9SkE5rYj9QA93Ut0ssHe-4cZ4qHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج حقارت ارتش
ایران
به روایت تصویر:
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/65045" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65044">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: توافقی برای پایان دادن به جنگ علیه جمهوری اسلامی ممکن است «امروز» حاصل شود
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/65044" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65043">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام: اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.  پیوستن…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65043" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65042">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYN9DhGqDp3KTSf_o4xql317-FUDOVC7ADiEb7BxVJkRew7snLEoqP3Lr93KBwpMzNtMIlU6S9t9PgiQwU653ayc0VxMRwd7Fcd_DNRvlKUxJYb1Tg9qktSCgetxmrCnAkLN0uxlTpJqrFr9IzjCNkCQQ5T5HKYplKW7AxaNV9pH-gcffZFR2UaOLM6Qc37wtmYLnjuA7UpO15PWSK7BquZ0GGEeJaeKZumsWZQPp7ud-WUw086Cp_MlWt136AI7eD9ckaDXLrtgqHduRcYF2wUfx53wdU9FHxXKltLFq27Pn9LeeY0rE5ocA3Ddok4tVESevPS7ws7P1B4VyOT_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.
پیوستن عربستان سعودی، قطر و پاکستان به توافق‌نامه‌های ابراهیم فراتر از تحول‌آفرین برای منطقه و جهان خواهد بود. این یک حرکت درخشان از سوی رئیس‌جمهور ترامپ است.
به عربستان سعودی و دیگران: اکنون زمان جسارت برای آینده‌ای جدید در خاورمیانه است. من انتظار دارم، همان‌طور که رئیس‌جمهور ترامپ پیشنهاد کرده است، شما در واقع به توافق‌نامه‌های ابراهیم بپیوندید و به طور موثر درگیری عرب-اسرائیلی را پایان دهید. اگر از رفتن به این مسیر که توسط رئیس‌جمهور ترامپ پیشنهاد شده است خودداری کنید، این موضوع عواقب شدیدی برای روابط آینده ما خواهد داشت و این پیشنهاد صلح را غیرقابل قبول می‌کند. علاوه بر این، این موضوع توسط تاریخ به عنوان یک محاسبه‌گری بزرگ دیده خواهد شد.
رئیس‌جمهور ترامپ: در گرفتن یک معامله خوب با ایران بر موضع خود بایستید. به همان اندازه مهم است که بر موضع خود در اصرار بر پیوستن عربستان سعودی و دیگران به توافق‌نامه‌های ابراهیم به عنوان بخشی از این مذاکرات بایستید.
دوباره، این یک پیشنهاد درخشان از سوی رئیس‌جمهور ترامپ است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/65042" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65041">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آیا دونالد ترامپ، باراک حسین اوبامای دوم خواهد شد و دستور آزادسازی ۲۵میلیارد دلارِ جمهوری اسلامی را می‌دهد یا خیر؟!  بزودی خواهیم دید! @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65041" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65040">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZVyw5EuBQusKO2msMviZSGdic-vHPmWKO1TcE1uQlgy7mQKAHWDBezY464IIQ_iJcOsNG4-K5XbO5rzAhvWSOwg6I9_3zGJ5Q1JPt23oNn6EZEaeEATPv0DM8cCk0Pv6tQLbiEAsv9_8evXtIIhkDV-FUYG9dDxvxGGJzReTHWUsOLCC5Muvyde2xK5Oz9iGrCLv9inlyCdTr0WQo1JzU7k-frC-nhsuyelcafADQ1V1HVc4GskSIKJa_J_tgtgXgLhhGNrQuRq4DyYLKSMaYZYGTr31ocyBmDtXK6k-YrEr6U4DuOws3d0jtSb-zKH8lu-wO8ORVNUOIf-NRT6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65040" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65039">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Heywa8ruf2NY8QQ_JoGX6V1W87-71tBh01Ig2YDGGSBbe3Pbi8I4hJx30CtTn9n60thAn1UiSubaoUCW4nqT9Ojr-cCdemmZSWRqEOA04y9NASWVY7ClUDoQVokcz-0hZoKSdbiEKCp2OTmIJdFSX91-D_3ZIe7llDr7xsZ6w4EBTakZjL2IYy6gsXSnooFoMBIFYOsP1vzdwZTSrUrAIwM1jRy8_RxKjoTOHiQmckdR6haU5hEdID-WRUqe1M86m2F3WDbumCI3-0EKD9Ldk4MR7UUbrmOipTHaoJD9uye1FKGoDIbsipt3L4SfPR35Tfu-rBEC-OZfCxOOMwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز حتی به طور کامل مذاکره نشده است.
بنابراین به بازندگان گوش ندهید که از چیزی که هیچ چیز در مورد آن نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بدی انجام نمی‌دهم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65039" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65038">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است. من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد. این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65038" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65037">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من معامله بد انجام نمی‌دهم؛ در مورد جزئیات توافق فعلا حرف نمی‌زنم، صحبت های خوبی در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65037" target="_blank">📅 17:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65036">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تنها چیزی که ترامپ تغییر داد رژیم غذایی مردم ایران بود
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65036" target="_blank">📅 15:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=BGX7lmupHBdLVMqT1KyZdsaRMjbFJwqhfwpxk38KYaKzxyk_Ndo23p4VHsv-XUbtJEk8A1OFBHZJL7wNvkE_GJK8mbo5KwzlZIDWGkBJuCXNrLQSA18RwP7GLYeySabY5UFvi-nNbm2GaIqPJpFY9D2WxiZ8gCELMetj5xKnjUB3brIbrQK-nJLSmEszdnYUq6oeWCd7JibH0e84PGNp5flS-OFFF5f-wEJ9EdT_ylsN7md9oM9hNSsspfX6ErYPMmpxKJB3LdcgHTxo6IvGm46WOXMJT-cydsDyiVsxeKWSmVvbzOE-yCSViOp-eavfhYsSgfo8cM0__Y3bQSgI8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=BGX7lmupHBdLVMqT1KyZdsaRMjbFJwqhfwpxk38KYaKzxyk_Ndo23p4VHsv-XUbtJEk8A1OFBHZJL7wNvkE_GJK8mbo5KwzlZIDWGkBJuCXNrLQSA18RwP7GLYeySabY5UFvi-nNbm2GaIqPJpFY9D2WxiZ8gCELMetj5xKnjUB3brIbrQK-nJLSmEszdnYUq6oeWCd7JibH0e84PGNp5flS-OFFF5f-wEJ9EdT_ylsN7md9oM9hNSsspfX6ErYPMmpxKJB3LdcgHTxo6IvGm46WOXMJT-cydsDyiVsxeKWSmVvbzOE-yCSViOp-eavfhYsSgfo8cM0__Y3bQSgI8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIWk9CfEqvOzRx2Nfc_n9S3Q_PClUHUlWhjw32rZgopwa7MFo7xiimyzvhYq85rleYSSabQdPqBxqk05Z-f1U83CCHIwSsm3walu7LM5CrjZG7a_xwzeXhVQmT5L_FiErmh5YqmCAOvR5TJcg4JJfcTpuM2VloWae-lbZ3jgh9r27pL-TD_tJkgHmGVUGZC7AcqvpY5YW0Erlbt1c4Ba4vSwOUqQi2Z_TWiWEL5cd9oFoTqppU_KIfCn8nmdiDSz3NF59j6z7HC7rjN1qexeYgJVUuz33lOgdjIFCVrBCKssw1m-oL0Ai-JzCaz0_0PfWjRIGJmRhJLwaPH475OEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BVF5ponrdWOcY52KyfA1oDKpcnKPmPXdsBDu5g-TjRkhPFPKkX_7Eon_IoTyin5bD9s3qM3NJxh9my7f-63s3VTIA8Jw2ZffYoJqqsoaE5NSmNx9zerUzPD7qVaphm9nuDqndySRK-mB_ox8sZI3tUMGmx3f7neQxSACR-WuR6LFuYU7A4Zbu-gSbKyEKc6CYqDeVcYQIb7YhUFHVWhba0clfh3Iw6_uZ_Tg0M-7AC7lW1zduKLlNafFaPd3XMXWLK9RL4onwrb5AVXEr3LUHvAQEUb_m-FSr8NH0Z0XpaWZbCIxmAx5OVwUcgKx4tOzF4mMNcBAelkpByW0RJ6fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=RdLn_iWLNfe7AHt1imxsaTcS0bx0D3F8mHfMIUKgm2CZJlBhv6jSSd6iXlGo-ClTn4GxF_7i5as1fEQNr9h3yRTfMv-fBySNxTGsAM3FQTMAcq1Pw0WDTqVBBpUFSGpXGYwMHDWcVFD8XXDCR-NLd5OXlWh2tMfXN8YZAwptJYLunPp4fbwsYVYHRHLoMvYbxGMfAgNz5HIdrhHJoTpCtLD6wwWOaIonetcIpY4-rnIHvPAnYHqoYDGvgc8Sb1_vAGJTmCDquQuYNgOGs0WpG5gK9OLetL1J2AZj_7GIGw7Y8ZpB8XzHkplW1dVV5iUONIlRKNhEnrLqy4Ywb1_91g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=RdLn_iWLNfe7AHt1imxsaTcS0bx0D3F8mHfMIUKgm2CZJlBhv6jSSd6iXlGo-ClTn4GxF_7i5as1fEQNr9h3yRTfMv-fBySNxTGsAM3FQTMAcq1Pw0WDTqVBBpUFSGpXGYwMHDWcVFD8XXDCR-NLd5OXlWh2tMfXN8YZAwptJYLunPp4fbwsYVYHRHLoMvYbxGMfAgNz5HIdrhHJoTpCtLD6wwWOaIonetcIpY4-rnIHvPAnYHqoYDGvgc8Sb1_vAGJTmCDquQuYNgOGs0WpG5gK9OLetL1J2AZj_7GIGw7Y8ZpB8XzHkplW1dVV5iUONIlRKNhEnrLqy4Ywb1_91g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=lzcDqUhWTRfbV7DWK-zyLkszOYiG-FtCabuOhIzeaOgY0hmVmyP7k2g0xEoX6XZhTIliW7cauymZONFouJqcUF_rNj7vCROWvU4UMk3Df05EtWNuedT_eLZsZIZmybtCJts0jEiwaNrFqO90V_JDVUsXf3GdQi-6eH__H180k86EFV6lks9sBVCziVnWk7jyyTgwfq2zHFtpDQMdmeNYMYZW3ooIyflCj18w4igM0WFzVu6ORoM0cHC_UFfKDvvZGdo2sz4se3tONKG8et-78qYkToncyjgC8AkYjE7EN984fiwdiOOc99ab7N2AGUD22oIwFn8Tbt3lFPVrdcDVTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=lzcDqUhWTRfbV7DWK-zyLkszOYiG-FtCabuOhIzeaOgY0hmVmyP7k2g0xEoX6XZhTIliW7cauymZONFouJqcUF_rNj7vCROWvU4UMk3Df05EtWNuedT_eLZsZIZmybtCJts0jEiwaNrFqO90V_JDVUsXf3GdQi-6eH__H180k86EFV6lks9sBVCziVnWk7jyyTgwfq2zHFtpDQMdmeNYMYZW3ooIyflCj18w4igM0WFzVu6ORoM0cHC_UFfKDvvZGdo2sz4se3tONKG8et-78qYkToncyjgC8AkYjE7EN984fiwdiOOc99ab7N2AGUD22oIwFn8Tbt3lFPVrdcDVTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hZqLGbFilJehLgGvprBdu_JdN7l4Y1EvJXiiO1EZvRlqvSGmpNygwirApKhlJ6F0lUnfqkrvpNsVLexdGpoaRQaP0pX0k00YzJcw10mhDHwR_JGDXj0SxeVOF5HekeR_QPxP2UDz1S8v_p5L0GIiOyulwfArKeGNEiuWAvPQgM_dhKwv1YYptAm1Gojy02eEP3uCh6UgymPvASU1Jj18tpKld8EEofFwZvBCjYwhdJg14OerPedF-yhuLYADuR4f0skygw5FnRL5US3hNJTJ1CLpcoB6tQ2VQ28WbUfszYDcz3YWuJdhPvARh-oHEjcRHA8uZzPrPvdzbAOnHFDQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65016">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5PnT3lTENA-Dyzum8-Th3M1QnhKIZ0CqECKa3qdszlwxspGMiZnNTD1yfWkp4XjIiy5G8u_2k7SVMeoaz_7A8ylubUt9KRlGzv3kxLSAeBbOzuOLNlxuXo4tq3eSeXCDRyaG2YbUerAFjSh1vP04UkhADRQyfAz3cmvGgxfPjHnH82VZTeWSMh3c9EwSfar5k_adeBWXIWmbwOVCCQ4I4AyNaJknKcI20wZy2nUZJYmc8IwK64-F15BQOeJuQ3olNfdkH4ZHZxL0H78qupGBXMWW8EHxdz_wOa7-LBIr_4ScxTqCUx3Z_DrUYgXwxyWK2gk7k-d6Hn0LSvAbUp8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ تو تروث‌سوشال: ایالات متحده خاورمیانه!! با پرچم امریکا روی نقشه ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65016" target="_blank">📅 18:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65015">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ مارکو روبیو: ممکنه امریکا به زودی خبری در مورد ایران منتشر کنه شاید هم نکنه امیدوارم این اتفاق بیفته
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65015" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65014">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=lxxAn_TZOg8Gb-B7gLYpY3XMaGkSUyePSjpCtzSeHd167RxXD9XXgd7b4V7iCZ8fzUMRwZPZwp9vPkAZ1uVzlTzeRb3-e1jXf1nq4sv-mOSxEefK9ZT8T4la70PEj9m4710phZm8-GE8O-2gnx085TchvV0xaAvlwNX1jWuxmmxQ-VmbEc8YFSdoH9HVESl3CdCiI7CjTv5RXJcHyFxuQlXug3o9igLFrd29Vk_CUJ_7Jz0aAvQJmBrjCXecYLjJMp4Gag5r0IcrrxjDA7ZRgty2Sl869NO1jH4tzx2DPS9vndPXHzsmjDYKjRLoVKWfaFf2NvK8I9qKo7-fqIkbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=lxxAn_TZOg8Gb-B7gLYpY3XMaGkSUyePSjpCtzSeHd167RxXD9XXgd7b4V7iCZ8fzUMRwZPZwp9vPkAZ1uVzlTzeRb3-e1jXf1nq4sv-mOSxEefK9ZT8T4la70PEj9m4710phZm8-GE8O-2gnx085TchvV0xaAvlwNX1jWuxmmxQ-VmbEc8YFSdoH9HVESl3CdCiI7CjTv5RXJcHyFxuQlXug3o9igLFrd29Vk_CUJ_7Jz0aAvQJmBrjCXecYLjJMp4Gag5r0IcrrxjDA7ZRgty2Sl869NO1jH4tzx2DPS9vndPXHzsmjDYKjRLoVKWfaFf2NvK8I9qKo7-fqIkbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقائی، سخنگو وزارت خارجه:
ما هم بسیار دور و هم بسیار نزدیک به یک توافق هستیم.
دیدگاه‌ها به هم نزدیک‌تر شده‌اند، اما نه به حد یک توافق — بلکه به حدی که ممکن است بتوانیم به راه‌حلی برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65014" target="_blank">📅 17:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65013">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73653df566.mp4?token=ILqThMvPnxIM_AF9CFTw3Ai953SZL43UN49mM4H06UEPjHz352co4A6JneX_epXIUAs7CV_77NZpWojNCRh55BdW7bxzayRPUXZZzRFz_eMTPtdqBtycB4X_DlM9526vqfzFmnoD-WXBFVlS4Z2_BF4iHvb0nLgrXcYh31i8Uev1Z2qDuvgsOH50LrZrU8bbyvkxpqhK3cSpPBxYFKQJIDAErP87aSZJA-A5he2EtRHhH8_SjftPp0z2BIbBhxXPrG0OcPdkPmDrrmw7mwDKG-WsWmak_AHMITpiLYA1ns4kt4M3ka_SuyZw2sV8lMDApHw_qe5roNkwcvY9p6K8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73653df566.mp4?token=ILqThMvPnxIM_AF9CFTw3Ai953SZL43UN49mM4H06UEPjHz352co4A6JneX_epXIUAs7CV_77NZpWojNCRh55BdW7bxzayRPUXZZzRFz_eMTPtdqBtycB4X_DlM9526vqfzFmnoD-WXBFVlS4Z2_BF4iHvb0nLgrXcYh31i8Uev1Z2qDuvgsOH50LrZrU8bbyvkxpqhK3cSpPBxYFKQJIDAErP87aSZJA-A5he2EtRHhH8_SjftPp0z2BIbBhxXPrG0OcPdkPmDrrmw7mwDKG-WsWmak_AHMITpiLYA1ns4kt4M3ka_SuyZw2sV8lMDApHw_qe5roNkwcvY9p6K8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توئیتر اکانت ترامپ که با هوش مصنوعی به ویدئو درست کرده از مجری سی‌بی‌اس که مخالف خودشه و ترامپ میندازدش تو سطل زباله :/
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65013" target="_blank">📅 15:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65012">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YMRf6SBD_U2CK50dWZnFY_kNZgQv8u9m55rAqSL_pwNSaQCJBRy0EuUSaGGz3uJe7OousvBJ0eheim-wL9UutWIoKmb3oDnWhWH4s6QlJ5of7SnZWtuBjNfdVErWqucSR6FevhWpYivAz1lAboBXhSMpIiGsgvK-wR7AJ7uiFKUHaPu3Uf6ltHtWBuaEl30k8IwXlbJ6H1f4etKyeylQE5SXovLzycwwcggufVDXLKIZlqX-_pm52HkBADJvQJ4HndIuvUo-ztXSRMlhFfsQ7dJrNcBUeE4ML4gTp5kKPAjmfksPMKckXibsLpsgYIsrfmWgMsHdABOomH3eiAc9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عروسی پسرش بود نرفته، آخر هفته برنامه گلف داشت که کنسل کرده و تو کاخ سفید مونده حالا خبرگزاری‌ها شدن دو دسته یه دسته میگن توافق نزدیکه حتی متن توافق منتشر میکنن یه دسته متن توافق بقیه رو تکذیب می‌کنن و میگن کلا حتی نزدیک توافق هم نیستن دو طرف.  این وضعیت…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65012" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65010">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t60CXE0CEgU3HtUEUVtxq1ZC4pJbMDK7wswXDa1DFABHSuU_a1dWZSujU3NhvEX53I4EgnvJ9cACehYCgUsWQCI9glP9h4Xjt2jWqmS-EUSN03miKwWwypc-HuW2qpJTu2KKzfDX4YPOcOecTJ25cuSeaq5wZgsN628klJeoXZwUUIb6wqm4npUzdxU_125WzYx00-OTDKtQx_UQJPjs_HMkCK_rI_dQPlXIGIeeuDamOapalKGGwhlfaQzcm9DCJ8jyYmj1AvBWbY7Iqvp-kbFjbf4kj6xSfxFvr-_J5lCrZjFva3ihVj5ekq7OWnyupIRk0WPHF9RSyLfmSDKTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=k-4IaPTzX5RySVXPo3xtpN7-0P6mPcMSqeCpBAD3HPqJE2XKWMYMcPoAKT-JuWJseUp3eSvJpJNIA5sKn03NgoIX8Fb8BcVPFvEjp2_1uKr9NE80-D-FNGnsUpq9vAgEt06sE70Z_i8-NpLFysMuRTQXnR_wR2iXoO6r6P0zC2c5rg7pMxoUxg77N7brQqBLDx8tO7FZfPYlmerqqGjhRpATRtfR4b7Te7hSBwwSTI5KigHYCKR48nCUd8P3MHWJfbu-XiTJq-vBe0N43mHDI3cQvDkbvodeOayoS0E3oy-huDmxDFUQ9jel0Q4Bn8Nnpcbfr7yNlb-lgA6u4cyogA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=k-4IaPTzX5RySVXPo3xtpN7-0P6mPcMSqeCpBAD3HPqJE2XKWMYMcPoAKT-JuWJseUp3eSvJpJNIA5sKn03NgoIX8Fb8BcVPFvEjp2_1uKr9NE80-D-FNGnsUpq9vAgEt06sE70Z_i8-NpLFysMuRTQXnR_wR2iXoO6r6P0zC2c5rg7pMxoUxg77N7brQqBLDx8tO7FZfPYlmerqqGjhRpATRtfR4b7Te7hSBwwSTI5KigHYCKR48nCUd8P3MHWJfbu-XiTJq-vBe0N43mHDI3cQvDkbvodeOayoS0E3oy-huDmxDFUQ9jel0Q4Bn8Nnpcbfr7yNlb-lgA6u4cyogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی از برنامه جدیدش به نام مای دات رو نمایی کرد و برای تبلیغات نوشت:
اینستاگرام پولی میشه ولی برنامه ما رایگانه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65010" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65009">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65009" target="_blank">📅 03:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65008">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65008" target="_blank">📅 01:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65007">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">واقعاً خوشبحال جمهوری اسلامی که با چنین اپوزیسیون احمقی طرفه، نه تنها پادشاهی خواهان با [به اصطلاح] دموکراسی خواهان دائما درگیر هستند، حالا خبر رسیده که علی کریمی و شاهین نجفی از داخل گروه پادشاهی‌خواهان هم باهم بشدت درگیر شدند
!
شما با این وضعین می‌خواین در مقابل آخوند بجنگید؟ جای تاسف داره واقعاً، حیف مردمی که گوش به پست و توییت های شما بودند و هستند!
#hjAly</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65007" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65006">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=L_OL7jHzOqqzHvXTkyvuRtmu3LxM0Na-ktRkJusPU0bJ_Rb5dcHsLePziIazuBzgVO5IU9YMzJp7KPGE3Vs_ZVGfsudfAY-CGhwOu7tGq6iO4iERA73nZxturpZz51-VSGKBRRLyyOCkh-73KMk4a1HqFOvRQ1nVeXYKGlTrg8TpdtBCoPtskFJzuAyXMNl6ZYksVc3lUkudjtON1q9x-KAP-SPV2-wNzyAHdhx_TbGH-7zAx7DO6fODom3yotVRWwlANmjUzzrAleXJh0hC4JOHpV6jePZN_K8o4rXer-HeNN3rRHdGQzLrLH6tVOTUdgLhJ0q3FdZNOkI9lkKbEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=L_OL7jHzOqqzHvXTkyvuRtmu3LxM0Na-ktRkJusPU0bJ_Rb5dcHsLePziIazuBzgVO5IU9YMzJp7KPGE3Vs_ZVGfsudfAY-CGhwOu7tGq6iO4iERA73nZxturpZz51-VSGKBRRLyyOCkh-73KMk4a1HqFOvRQ1nVeXYKGlTrg8TpdtBCoPtskFJzuAyXMNl6ZYksVc3lUkudjtON1q9x-KAP-SPV2-wNzyAHdhx_TbGH-7zAx7DO6fODom3yotVRWwlANmjUzzrAleXJh0hC4JOHpV6jePZN_K8o4rXer-HeNN3rRHdGQzLrLH6tVOTUdgLhJ0q3FdZNOkI9lkKbEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امتحانات نهایی پایه یازدهم و دوازدهم تو بازه ۱۵ تا ۲۰ تیر به‌صورت حضوری برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65006" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65005">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65005" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65004">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
العربی‌الجدید: سفر عاصم منیر به تهران دلیلی بر توافق نیست و پیام جدیدی منتقل نکرده است، گزارش‌ها درمورد مفاد توافق گمانه‌زنی است و اختلاف بین طرفین هنوز زیاد است.  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65004" target="_blank">📅 21:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65003">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
📰
العربی‌الجدید به نقل از یک منبع نزدیک به مذاکرات:  سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به معنای این نیست که توافق در دسترس است. گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و صرفاً گمانه‌زنی‌های رسانه‌ای است. وزیر کشور پاکستان پیام جدیدی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65003" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65002">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
📰
العربیه: طبق منابع العربیه، انتظار می‌رود پیش‌نویس نهایی یک توافق احتمالی میان ایالات متحده و ایران که توسط پاکستان میانجی‌گری شده است. که ممکن است ظرف چند ساعت اعلام شود.  شرایط کلیدی آن عبارتند از: آتش‌بس فوری، جامع و بدون قید و شرط در تمام جبهه‌ها، از…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65002" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65001">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبرگزاری های حکومتی: عاصم منیر وارد تهران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65001" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65000">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=H92RiV0T1WLTlgchMXBdMMlbJCZR0n2BWSXwJkmZmcwiMeshOXsVyq86amT0DGTipmWvsJWp2qTe1yvw8UbVxfosBvqvD-122AjRaLDMVJ94TTIayfNxt33CIBkMSu88rIojnytwQuT7UHu1IgXTCjFB9E5gF9DWbfDN8UQucUQxqrdj2m4jV_aOmaTCRwKlFIOLVcNR8zzjyc-9-qrf45J1yRbpkBU3gW7EW_5-DIZRmdFGk0Hq8McBmKdwXnbFUUQiWDLFHP5rrapoywITpduGhOp4johVJHDl36iz9HmQqB8K06JH507Euw9faz6zpGvXDrmJywfaRLTHXRNbGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=H92RiV0T1WLTlgchMXBdMMlbJCZR0n2BWSXwJkmZmcwiMeshOXsVyq86amT0DGTipmWvsJWp2qTe1yvw8UbVxfosBvqvD-122AjRaLDMVJ94TTIayfNxt33CIBkMSu88rIojnytwQuT7UHu1IgXTCjFB9E5gF9DWbfDN8UQucUQxqrdj2m4jV_aOmaTCRwKlFIOLVcNR8zzjyc-9-qrf45J1yRbpkBU3gW7EW_5-DIZRmdFGk0Hq8McBmKdwXnbFUUQiWDLFHP5rrapoywITpduGhOp4johVJHDl36iz9HmQqB8K06JH507Euw9faz6zpGvXDrmJywfaRLTHXRNbGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ما باید شروع کنیم به فکر کردن درباره کاری که اگر چند هفته دیگر ایران تصمیم بگیرد، «ما اهمیتی نمی‌دهیم؛ ما تنگه‌ها را بسته نگه می‌داریم؛ هر کشتی که به ما گوش ندهد یا به ما پول ندهد را غرق می‌کنیم» چه باید بکنیم — آن وقت کسی باید کاری در این باره انجام دهد.
امروز این نکته را مطرح کردم؛ خیلی‌ها سر تکان دادند؛ خیلی‌ها بعد از آن نزد من آمدند و آن را تأیید کردند، اما امروز خبری برای شما نداریم که چیزی در حال وقوع باشد.
باید پلن B داشته باشیم برای اینکه اگر کسی شروع به تیراندازی کرد و چطور تنگه‌ها را باز کنیم، و من امروز این نکته را مطرح کردم. نمی‌دانم که آیا این لزوماً مأموریت ناتو خواهد بود، اما قطعاً کشورهایی از ناتو می‌توانند در آن مشارکت کنند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65000" target="_blank">📅 18:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64999">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/news_hut/64999" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64998">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZtDb9FOx0PWm220qWbU8XSMQ7aGV2VvzJUOhs-frUAdOTlfR46KqRn0fL96zgUvBgDhLyE-K80u-pIjugg2LnFS1HbbGmQDuUte6SY0TEsblyBF5jmOrrJzJuTbv4fmNlZyTlpwasgrx4Yuo8rmu0AO6zwXrbYFJ-FnB98mdgM95ifT24Yc5ZjkFHGj9SDA0YnfUhy97bOOK6BrKp2TJIXQKJNtqoMT8ZoqPYtkUfeCJAuXerm2KYU7tyh2O2CQHP6VW5-Cj5jl72gbRZumYX9JZJT5YwJRYYNfyHkonmWGcNcsTChdi1FFCgsG2jASzXqdsCcS0xWyCSMu0UwZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
لارنس نورمن، خبرنگار وال استریت ژورنال: یه منبع میگه هر چیزی درباره پیش‌نویس توافقی که داره می‌چرخه، دروغه و صحت نداره!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64998" target="_blank">📅 18:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64997">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
📰
رویترز: یک تیم مذاکره‌کننده قطری امروز به تهران آمده است با هماهنگی ایالات متحده برای کمک به پیشبرد تلاش‌ها به سوی توافقی برای پایان دادن به جنگ با ایران و حل مسائل باقی‌مانده.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64997" target="_blank">📅 17:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64996">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKUjAiRuVpyxAH18_OBiM6pDOdioQvhJ9w3pDGCEtHydxwoSC8atiWuAQjAhsn_uc7gczH65Bb-o5RtE6cflcXEjVApS8VmvCfAJmI6xMwImnLzJ3e8dU1rPmj3sxFn_jD2fvaq3LOqnKrq6asH4daCnaq2E217rCYeFCmKblP0oPaWoQd6UCtreUkL_ulJ_EE1vzvTDHDJLXHNeQX4KhjphH1DVKx_C1ch2m5YDY8yP4wb-cPiTASDpjnFKfAA1wurgztTj9TPfqsSFjPMowvuhtpLwVnSelanfxgSDwnpw1st1gavjvKlTsR0clwEjrSp8pD8eLWEpPaXENDj1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو هواپیما دولتی پاکستان راهی ایران شدند؛
احتمالا عاصم منیر در راه تهرانه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64996" target="_blank">📅 16:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64995">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t67EzfYoHunbeR-g2uwqtMG7x_L7LBG92JlNCjwhISnPCkctq_ulC5NACe32KBMUqIyWP2xLk1TCLL3Sc36BmJ2r9Ce5VmqH4XrUNtydN8Y2qZ3DALMoHDoX1L6CTh16WqJ5mfmk-cPUFGJGcsDfb1w-J1EKfVxP34paQKGfGaFzC6itqLQOCPSwOC17hGbxhj366cl_DvXXrpuOqAqASXTqfjoixp2UQjTsZ81DZHrmMWSSZpl0YXl0DnF2ND5zDURgUDzeVd5uhbkM4MtwheDAUYqVACH6mA5SwbSbGg9n28x2OSzt_2qtk7DJxAjiVxFXKUi-0hy-1Lu15Dh0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس: نهادهای بالادستی به این نتیجه رسیدن که بازگشایی اینترنت به صلاح همه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64995" target="_blank">📅 14:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64994">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سپاه: تو ۲۴ ساعت گذشته به ۳۵ کشتی اجازه ورود و خروج از تنگه هرمز رو دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64994" target="_blank">📅 14:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64993">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
سفرِ «عاصم منیر»، فرمانده ارتش پاکستان به تعویق افتاد، این یعنی هنوز اختلافات ایران و آمریکا حل نشده
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64993" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890f54566.mp4?token=rMjY3n9WSKSJTIdCdM_kCgtcRj94YhI8QjjeLZ0PbvW9DOhNS5yhErDPui3NppVyqpt3Z_KTT7psUFC56M6oQuMqBQ3MQy4CQFlsqfAlp_hniOcc4sjRZnaCIjWNwyRaX3Xowkz6ibDNtOEWAzAwCR5KPIf1msje-XI1eePCtsmT03fKtujp8xS73BpzYZbi3OQf6e5AWsNnQSbzVTsyDiRZh_SBUY4jazAgF56uSjRPjQj231_blw05Tpa77i1nvlX8VdSOenQTjGG1M-xSgzw5CCextRq4LsDuWjZcGZVwqM6rU2M-e5seDRsXzNkIraeJbujMOTbsimDHeyyBfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890f54566.mp4?token=rMjY3n9WSKSJTIdCdM_kCgtcRj94YhI8QjjeLZ0PbvW9DOhNS5yhErDPui3NppVyqpt3Z_KTT7psUFC56M6oQuMqBQ3MQy4CQFlsqfAlp_hniOcc4sjRZnaCIjWNwyRaX3Xowkz6ibDNtOEWAzAwCR5KPIf1msje-XI1eePCtsmT03fKtujp8xS73BpzYZbi3OQf6e5AWsNnQSbzVTsyDiRZh_SBUY4jazAgF56uSjRPjQj231_blw05Tpa77i1nvlX8VdSOenQTjGG1M-xSgzw5CCextRq4LsDuWjZcGZVwqM6rU2M-e5seDRsXzNkIraeJbujMOTbsimDHeyyBfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64992" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43db173db6.mp4?token=a6UCXWt9bAd4Snuf2w34MOeg6c3HSeurZ2be8Dmp2JG3XgV5beoOnOtwFo_vohoOB2Z2Gz03GL7Eo0FjiAgz0KRR6v0u94ywJWZeYE-SqFm4OesV0xmWcqvIJ32-KsgLg4EpKStL0UCT3GiqjJgdkuGE02EIaPIEkWbhfoJNXGD1g9PI0SMN_I8vFESHH06RxC4X0Emm2u0FlS1IFZc47IvhDJmxKhzGbXUVbg99xS8ICOKWdebgI551v6t_irlFs5Cu-umw08o8fU6ff6HGMHNFKeo1L76FvYLJ2p1PbZpmhYQHvWMIcK4jx8FvGIpWu9Wu8dS2Rq1inwSqyTYwOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43db173db6.mp4?token=a6UCXWt9bAd4Snuf2w34MOeg6c3HSeurZ2be8Dmp2JG3XgV5beoOnOtwFo_vohoOB2Z2Gz03GL7Eo0FjiAgz0KRR6v0u94ywJWZeYE-SqFm4OesV0xmWcqvIJ32-KsgLg4EpKStL0UCT3GiqjJgdkuGE02EIaPIEkWbhfoJNXGD1g9PI0SMN_I8vFESHH06RxC4X0Emm2u0FlS1IFZc47IvhDJmxKhzGbXUVbg99xS8ICOKWdebgI551v6t_irlFs5Cu-umw08o8fU6ff6HGMHNFKeo1L76FvYLJ2p1PbZpmhYQHvWMIcK4jx8FvGIpWu9Wu8dS2Rq1inwSqyTYwOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🚨
ترامپ:
ایران نمی‌تواند اورانیوم غنی‌شده خود را نگه دارد. به محض اینکه آن را به دست آوریم، احتمالاً آن را نابود خواهیم کرد. ما آن را نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64991" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64990">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPf5cbLEGRqelOxJdb-RGHVxXoF7d1nT1CM22Z6zRfwMQknQCPEHGmgRIBn4hWvah0tvqVntBvqLnlQZCN7iNKNSSEAk9b0cHELSJOGSmmIdRhE99Li1AKNDeVd5GlFq-StCsPRz7NMpeyJxU09YTULRx8V5ArAAPKz4OPXiLmO9TSIT6EF4bL_k1mvkx1JOWe-9kFM6XMtujHHyBJE0LMxPxZvlL6BdCPpNqP-iJkE207pb4AKdpqpDhDvSpHvEyFfPx9yON7GbyBaZkmLQA0Si6mw2O0jLnw3KPZsX4NzTwM56WbZf9OWt0nhkpOZxTLTY2zeyOcZ8Tjic9FPOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یه پست از نشریه نیویورک پست بازنشر کرد که تیتر خبری‌ش هست؛«چطور میشه تهرانو تو سه حرکت نابود کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64990" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64989">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJwSlCIfCJyZi180xn9rkLDVj3n0Gj0mLNjFmKKq486F_gUkEU6nMzKj0HtzDDQ-mYo1vIyyneUw6v3uBrEmSxRVtPkayY_3DQUxXAxbOO4X8xFGe-1Ko9OVa5tmz_c9Rfkn8n8ZLMNDdudHhcNo65gVYCd7m1kKqwD5kEmUU566lAoz1aIk0cXeLsuP4-UhUty5WkTv_1ljF6GFnrS-0QIeSduLvkGloWw19ulA8deqfofMXulqWPNOXv1NMFrcdeeUeG0s-h64JJl1iSfC6YB1Q1JkT_lZFwRyy1L3IhMmzQAmmY4l1tZEAtHNvYk3mCIHyf9WEiQuFx8f22s8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید هزینه‌ ریجستری گوشی‌های آیفون
ریجستری آیفون ۱۷پرومکس، ۱۰۴ میلیون تومان!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64989" target="_blank">📅 15:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64988">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMGmoyazecQ3uODahhyuIh-ut79S8YZSPL9aTNrIb020BiTnzSOl5q_g4_jXpjwWaY51WB1SProfy1aREMEeBGgq3e4-6_XlNkcSs_ltSSpp84dgxbGiBJ6Pwq22iM9pMf8W6_nKYv_LCWCilpAev2P6TF7DxU9vVZ-2aRUtHhxf2b13lgDVLjDeKwTSaqdPq6_0eb8QTxspL-5-oJJyotnI0xhROR9s2d_HGYAHrcd5WP8YkiKMkrOvY3-Vw5IZSS2qQQvrNP7748lXm8qrIvLzLgjTel6LL3AJGlFoRMI70O2ng49o4zBTjZ1QVypWPSSTgsxWFKMl3n0kNl3hHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست کاخ سفید از مهم‌ترین دشمنان امریکا که در دوره فعلی ترامپ حذف یا دستگیر شدند:
رئیس‌جمهور ونزوئلا - مادورو
رهبر رژیم جمهوری اسلامی- خامنه‌ای
معاون رهبر داعش - ابو بلال المنوکی
و برای رائول کاسترو رئیس‌جمهور سابق کوبا (و برادر فیدل کاسترو) کیفرخواست صادر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64988" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64987">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
📰
رویترز: منابع ایرانی می‌گویند رهبر معظم(مجتبی)اعلام کرده است که اورانیوم غنی‌شده باید در ایران بماند.  آمریکا می‌خواهد اورانیوم بسیار غنی‌شده ایران به خارج فرستاده شود مقامات اسرائیلی می‌گویند ترامپ به اسرائیل گفته است که این اتفاق خواهد افتاد دستور رهبر…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64987" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64986">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
بندرعباس ۴.۶ ریشتر زلزله شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64986" target="_blank">📅 13:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64985">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAMAfWLd0sgPeDC4PMteK_nyFAUfTDZyWc8zwUWul1U75LoQgQEzpCCRFZVqb-5m4ylECGKFZpZHrVqSeyB07Cq7tkOY_C8Fe7UfHeUSFTJEzDvEK-mnmupKqQZ9_jA6j-jX29j6oDuHFjHWMILPHJJH9NkXm6Q145Ym9WnaRR4UaLVGUAyw8bOriLRvrB8b_ZyE67Dc5W8IrFREZPRRH5qmt9wjSn1lk9fjs6_jKy04crKRpflxTPQ4XDqSy7ycx1bwlzTfrWzUz53nZONjPtXG_gukXOvAEeCGZjPWFmBgi7rYwgKasA5MgOcaaD39bKqGy3wV-1aDS44Za7_9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: تا زمان شکست امریکا و کشتن ترامپ تنگه رو باید ببندیم
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64985" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: اگر فرمانده ارتش پاکستان به ایران سفر نکند، توافق نهایی ممکن است ظرف چند ساعت اعلام شود  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64984" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور خیلی از خانواده ها در آمریکا نگران گسترش هوش مصنوعی هستند، نظرتون چیه؟
ترامپ: هوش مصنوعی عالیه، ایران نباید سلاح هسته‌ای داشته باشه :)))))
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64983" target="_blank">📅 04:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JEtGIn6vfqjUbPVfrzgTHV5B5jO1H5Ejx18-NIo4859LH5Xj2RQYBd_eHYrNHef2r8LsvQXR9_8IVTYRjY-LuCXYDQ7zlsdEUU4OiSmbS1mntmyLNc975AlXbko3cnB_Q-jborLhWBSsKaN8zCaJZiEiZZj_rtvaFuQ8Uj4yhcsIv5olanECpEjIcI7HfRtUhrounROgGDxBDzLaFyJRCyjSB6kYbgz9XDnGUzI5ixO-bqz9Zy7-spX4_rJjJjaZ8XI4Ls4yiuEeqpCQHKm6EMfbqD5wNDDSsfvR8i1pPuVyfeornp2pxuWK-iPeQN6LuoGOh4sAhyO5ShBvUUwL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHlgvn-rAkaOqMGaf41lI4BxfaBYU8pi9Qpb8RxO9zFhnbg0E6sZsill21SsMYq5u_FeNVsMmBteMnvQ-_ZSQKpU6Ry5AVbJ-o8mhFbjADM3NGY4NfvNie7CaTB2sRy9nTxgtMEc5X4N27D15jHgeE6wq3CudkwhMPBUcgyz-EctUqmLAmjHqXmTsN3j7JaNrxQqvD3qfVZQydVKBvEkrnXZYKP_-H5N32R7nDUEQ4xcQ9_SD0SW1F4NYPUdBneqM2Oimo11yyC1Ync2k_4GNDYPcgeRzTrWV5LlrEwXQTBDRvQIxLDj64HH8lnMzkPxHeltw8gczxzOilXCoEndCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEyaZFDXqjxVTolJmsu2UK5cRqycqfa8LZ-CbuqnFBXbtPaCQAu3pWv2_WIEF1zSMDIRylEXH3KYWzgV018IFZP8h_E2HItbLb76JB2soc2ze7aVMZun3qifp13T7aZzlJhhbvpkeuxyicgI-Pqw2ujyXM00Q0OWiSkcN5utul5LZwkXfVL0mRS_mTD8aop1naa5sfTKNoESIoz1sl9Hh-us7wbMAtHDqAw6Fub15vyM-b4S14cFsmnf8KoKcl00GCn57Ivo1umEeeKzesUmIGh6FAMebJ5rIX60ADTc6OGj9VcN23NYXh-jeLqHWBdLS6Tqcy639_-pSHdwdDAJDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=OXXz66NYaH93r6m59-NZMp1VCsMtUcWMSOFKoBspSUBvWsTDZdid0wIUs-Ef4XLGZTqM6HmkTQEByLyPlbcCG6K7lnJjVsMNdWr6v61Pasat9XQpWvgJQsIuBuqn3iM8HMpRl3_nDXg4F7OloyxHjx5apiZa42elIkFdq82ydJ1y3FMqrEfrRoYbTT6gJbblWZc1ewvj1z10Wpgsu_1alUTOW2C_TEEbNUnzEU-rjoZmmrqDPwfEkBZtw0d5IPP-DmoEea05c9BtD-gUNERv1XmH5vhB3TrCvZon3AffZ75YPGgAvQ1-9FnFA5UQIFa0KhZ2RXFoPmLLcHoYIGhpzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=OXXz66NYaH93r6m59-NZMp1VCsMtUcWMSOFKoBspSUBvWsTDZdid0wIUs-Ef4XLGZTqM6HmkTQEByLyPlbcCG6K7lnJjVsMNdWr6v61Pasat9XQpWvgJQsIuBuqn3iM8HMpRl3_nDXg4F7OloyxHjx5apiZa42elIkFdq82ydJ1y3FMqrEfrRoYbTT6gJbblWZc1ewvj1z10Wpgsu_1alUTOW2C_TEEbNUnzEU-rjoZmmrqDPwfEkBZtw0d5IPP-DmoEea05c9BtD-gUNERv1XmH5vhB3TrCvZon3AffZ75YPGgAvQ1-9FnFA5UQIFa0KhZ2RXFoPmLLcHoYIGhpzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان،عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3woqKYT8HW0au6N_sP3m1J6t7E4hlqedj-tqSHFX_etAJPNBTfth262Cn_7dwiMeU909WqaY8Kkz5pwB-EErK31-ygxMTE0YL383CqTT-ZU0KSQGzfF8l9Vkzft0OH3nARRBpTxLKHZgfHMaIg6XSYiyH04x2Nna1J2aJurc_NJPwEwZpQeKUUEubwPUaOfoztAItSfE5x7xCGnVIvRbMf8npBnumOfUlR2MVuth0ASveF6ZPMJrvSCBCDVukdAHimPtG7tH34bmnpmYDct2nQuiNfqaJ-u3QNjIkiAISvec9Y-c-JzUICoVc0pLAwXfBgaZ_UuoQdqS40jZ_da4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDXSbQla_KvAoRkG5bCxpsVZBDV7E3F2FV7hme-dILX6xELuyPk6qk87Ea10rFqeyi8ZEJsGTAi2uYOuyvgN4drG4w_D3SbT13HPCvtQ796XiDrDUhQuUuD8fNYNy1imF4j1YY3nKOevuk0DXQKYMWTQbWybdwdSsGqHsVH54L1UEViksTTcnX2zQ5ew9ePrC-jpf5lD1GS7tW_gKuwGy92u58OnwArTxj1T_YtDGkD7ySuII_828JHv2sfEOUwQ_xU6srTK__MCx6Ma-scR0L0Zy1O1FIi3Ri_rZk0QEIMXg_xKD7zZndcZ2YX2EPmFTaKUEdWso_Az2sJsoPiwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=qoRdI2Y096qS3GvOq0xrxEh-y56-VmFliQudrwIA0sCXIopmjUBYA6aan4qpjAgkfsqmS2yAVWUzcXepuLlDbSfhkuQVCz0N34gQP2WhIuVXH1EiQ7lNDvxnlMLX4kxb4bFSuP3h9xsWV9_mIiDenc1kWzhQhfFpfNwlHrCZFtHnYmPaPJBW6mCgbQWDu-b5dwEtTKvIqXSHpWEI-zJEynEb0mlc9BVnVi77K1ywD8NSg6OPBlGej8MCA1Un5J9btbouUkkIhb-bsYO-URgMsuy7sNGxX57PhE5GMwkZdPRA3k_mDyeOo3ZwjxFDN13WwSaG-VTgSXt6jEXFTdJxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=qoRdI2Y096qS3GvOq0xrxEh-y56-VmFliQudrwIA0sCXIopmjUBYA6aan4qpjAgkfsqmS2yAVWUzcXepuLlDbSfhkuQVCz0N34gQP2WhIuVXH1EiQ7lNDvxnlMLX4kxb4bFSuP3h9xsWV9_mIiDenc1kWzhQhfFpfNwlHrCZFtHnYmPaPJBW6mCgbQWDu-b5dwEtTKvIqXSHpWEI-zJEynEb0mlc9BVnVi77K1ywD8NSg6OPBlGej8MCA1Un5J9btbouUkkIhb-bsYO-URgMsuy7sNGxX57PhE5GMwkZdPRA3k_mDyeOo3ZwjxFDN13WwSaG-VTgSXt6jEXFTdJxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=dhyG-x4j98hphpKFhHZhDBG0sdLM5hsG7EdBDAFefzbP1TZNSnxb7omBfIfde171ua8LbRNNfPwyAXYg0-ND0-arIaX4sr3mp3niPW75Muw148U0M38fG0DvKof2KSZXxCaO_guM65lNOuySzPQOGJ-mhpB9fYnhiisbQItneZtBcFl6fYjyxG0Wn9HSm2fYQmCtDPSinfjlCxv8v_Q8qa_tPzCkDVp19UWEvARekHC7IZlaf60oXeBdcvFULrlMzQSQpEcQikacWChU6vk2V4JrcK5kbg7xSbtUKpGV6_rOCDqiRK57bHDoiXGVHXTP8PGv6ccaq4pH06FJ9ivmvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=dhyG-x4j98hphpKFhHZhDBG0sdLM5hsG7EdBDAFefzbP1TZNSnxb7omBfIfde171ua8LbRNNfPwyAXYg0-ND0-arIaX4sr3mp3niPW75Muw148U0M38fG0DvKof2KSZXxCaO_guM65lNOuySzPQOGJ-mhpB9fYnhiisbQItneZtBcFl6fYjyxG0Wn9HSm2fYQmCtDPSinfjlCxv8v_Q8qa_tPzCkDVp19UWEvARekHC7IZlaf60oXeBdcvFULrlMzQSQpEcQikacWChU6vk2V4JrcK5kbg7xSbtUKpGV6_rOCDqiRK57bHDoiXGVHXTP8PGv6ccaq4pH06FJ9ivmvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=RoGIG-uxuCzefQxRd1I9imJvPk8RNUh140STIttl8-0XN0jFnKqyw0kjHBZ5ivLIzWwMXAkj_ki1DEQFDbIaJUxj-7ZWvV_FIF0FZorq51XeDX_zCN_fYZhvOJVVekmClpBHczxbZt7_0Q8jgPhQQKIE7r44xj9eO40t-eVmJ1iTnJ2rfPOOWEnNZBOPfGANmNceVlEhJ8v-8vNk0XWpR90rjRG2e5g-33gr0oeYt7Pua7_L8veLEQorIn3D4KQVjgCYO231h-y5izau_KB_QbyK72urH-_u3flJ9iV-3SNqv5VkPiAoGk3vQdE0ruDJR0w_zbBCjhllLCahnT8xyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=RoGIG-uxuCzefQxRd1I9imJvPk8RNUh140STIttl8-0XN0jFnKqyw0kjHBZ5ivLIzWwMXAkj_ki1DEQFDbIaJUxj-7ZWvV_FIF0FZorq51XeDX_zCN_fYZhvOJVVekmClpBHczxbZt7_0Q8jgPhQQKIE7r44xj9eO40t-eVmJ1iTnJ2rfPOOWEnNZBOPfGANmNceVlEhJ8v-8vNk0XWpR90rjRG2e5g-33gr0oeYt7Pua7_L8veLEQorIn3D4KQVjgCYO231h-y5izau_KB_QbyK72urH-_u3flJ9iV-3SNqv5VkPiAoGk3vQdE0ruDJR0w_zbBCjhllLCahnT8xyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=hkeiAQ7Vxo753U9aHQVk-ukxyb5fGa0iY1s3wsHRLHfKxA1zQ3LgfDmHEwxUiW8gejWouTZhMJkFQEsxwmriGTgoZB-8vTHc76vkc6Pajrzuzp8UPzRfTt_cvStT4Xm-ja5tprGJhK9jYuQdoDvfKGZynJOfCMa1dkP2i7pAYdUz9VxEY01HQWnvtUuFvM5HTMwHtMFTZsCfybtCPXIz22o22JvBymgeSzPeo7EZ55h6GKKGxnZEk69jBRMC2riWwaXLALZiBr1W8B6GKNnDBY1rmpQ2fD3EoeViMuOIxYnVn7NhmrhxHbr2j-dzfWniNISJk-iwp-vNgRclQqYk_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=hkeiAQ7Vxo753U9aHQVk-ukxyb5fGa0iY1s3wsHRLHfKxA1zQ3LgfDmHEwxUiW8gejWouTZhMJkFQEsxwmriGTgoZB-8vTHc76vkc6Pajrzuzp8UPzRfTt_cvStT4Xm-ja5tprGJhK9jYuQdoDvfKGZynJOfCMa1dkP2i7pAYdUz9VxEY01HQWnvtUuFvM5HTMwHtMFTZsCfybtCPXIz22o22JvBymgeSzPeo7EZ55h6GKKGxnZEk69jBRMC2riWwaXLALZiBr1W8B6GKNnDBY1rmpQ2fD3EoeViMuOIxYnVn7NhmrhxHbr2j-dzfWniNISJk-iwp-vNgRclQqYk_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=kAJxfXGF0L-Ep_i5VNbyKMBdPxR1ArcLXb56GQLKsUn1naDQLy2vhj1Z-v5IfyA06gDQiGtr6X0RsTVIOzqMSzO2dPypu_6bEg5XoSov5xDAxTmvQDjDofa0G8VJZKQFDidMdEfoLQN75yTnAiFwSDrBZnitANis2jGUFMQWyg6WNl2YfVy9pIC47rvZ0vB_lFYQmzWd7ajILskwinYKEbsqb_LDDK9Ll2ZKEAR7XTWnCWeJRHXsoDBvv5sU40Efbg_AJIg4cTtVsIqPzDEdHQtgtxRSJPQoEkduuJl683pqhRehbpwn0XCHm-u0LNkzSyVdDKmxJh1xEd4bPc9tlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=kAJxfXGF0L-Ep_i5VNbyKMBdPxR1ArcLXb56GQLKsUn1naDQLy2vhj1Z-v5IfyA06gDQiGtr6X0RsTVIOzqMSzO2dPypu_6bEg5XoSov5xDAxTmvQDjDofa0G8VJZKQFDidMdEfoLQN75yTnAiFwSDrBZnitANis2jGUFMQWyg6WNl2YfVy9pIC47rvZ0vB_lFYQmzWd7ajILskwinYKEbsqb_LDDK9Ll2ZKEAR7XTWnCWeJRHXsoDBvv5sU40Efbg_AJIg4cTtVsIqPzDEdHQtgtxRSJPQoEkduuJl683pqhRehbpwn0XCHm-u0LNkzSyVdDKmxJh1xEd4bPc9tlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXYARTZo4Q5i2ihmsV9Qrw2FrirAYwRdGofq26gC0633GKOuqJGM23qn9hwYXG8iuhu9cIuQGEYW_FFIhioRxXftazvvqLGmSAmldBH0HbJUWkXpqsJP4dpS-sE3VY_6t67ea4k1A3V3mE-9oASx-Ttkn_UXXZhCb9H3YRvToZN5XDTHR4ujfgzlYKaRXaMzGVtgwpjBLbm6oQhS8PGfb8-2y_7xOWUPRjrg-KVkgfosM9GbT5Pu1MuVV06pIvF770WIZhcBFGGByaK-wuJeqCIlmMWPr_At_sPlhMSen9ThBEDPQW4MyrtDJ67iSZOxFxLv6r7RCz7iX4wdukqtiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLQ7Zk8f1e7eyk5xRVT0KroNVzTAcxjZxWwxPOG_BGXAlCyo14bn3fqEFV4y8Si0fojnXo5o1ACZ0UVWKpky8DA3tZkP5tINGxdqWOpGAsFcnQJleSkdJ84bkJ7GA5GVPYJ28T37GCL5I0ym361fYBAtCpWbSLPQGeQRLliaU7edqqZvtcV1St-VdD4qHa97-fsfYttl0gE6F7bMCl11QIQChYSnn6bMzbNeRo8Iq32zQm5kBTCAbsHq9NDAbY-FG0pDdTbx1NaEnacwz0meCarvlHDEWGu5QwSzX4008Etxft6__qJPG42Yexl_wIhp6rnh9ilamq9wlL0HcUXq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksvXO57nCXK5Eq26Q2kDsAkm9u4N34gNeWHIwROW3QvzEFg7WyqQYl2zxYTbCcvnB1eYY880euRaBg_hYNR61jq3e_m0GpuQKRqodnqrnsLE1LqmmWOCddebDntheNGwVRGVfFl1ntw6iM9rtzHTHD5crntWo6bjBGUX4EUmpoKyPbeusC7NKxwLJNyYlbCnHZ44u5ysdrgKvw2Tw1KaaLK1CB5PpU5SaTcJHVz9gPxd8RhBF4vyOo_shVvT5-f6ApXihhYITRQgL3CKAgiAlEcwYXPOOL4c5JXgOBjE0NFCHnbBBTu1yUKBHs3fqBx-IJfvitKtyq6ekvdpKNj0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdgPUT_L5UyFE7zgMYokHiko32lqORie5QDTTdnvUUzQY2DuS4jz9xSbZIqjO2ykFj7JpQfV9UNWXGvrH8Pie0TxlDzL0NvHaKwBzhCbYIT4eH2p5B366qTfQwP6_4EcE0Mf-wAZl2jHAWU8CqXD_sIYXB_qIflsyOTJgvP_0uVkxTZwMF5CzCt0913WTjDpwHk20qGZm5AD1ZnX2qykYfQp0biFUA32cjEl7UiO7Gd_7GUdnL-ccMv8kyvRpzQTdGPySQA_sjtiycuGsugUiCZNiDyHbJ438Hd_ur9xM6PPwejOkTFv-fm0apsY5ybRFXn_iXAR2TaNwVmYYh4M0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiSXRn4HuTcf4Uw6fZc8-dwb60UNvs07i7_mfELeztM40xWwcz6EWzm5IN6RQkPULMj4ctvcheCRAj_Mv-X1NXP_Cn8j0lXqXlkXe1Iiwh8N1Fqc5YHEB9eLLYfLHshN54oDYPUoou1HYN9HL8kjmj75Z9-HlZ9M7TjFIy6a8cwljp8V-r8g-S1C2QezCzEJPbRu88Y4qIrqmBg1G0ODd_SxE0fB4FIQkJWdRj0NsERmPlwGPx3VGJTNN_TyqwoavJPD3tKBbXBN-u7pXdNzalPgobhBS0cQ7GtuKvg_faVDXv5lNCMkVWFczb__M693xpGUDCuUv9ofc6jW_OJMgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SaOijHBA16BSqqU_eb9D6tLftNSJj0qws5Qb1aUFq6qGrd4VxZq3APV1xhFSyhNpRWEzrC9UoJp8Jk1r5_pGLSPFp1-9n-fvStfU9nm_E0lMSWML63KfPLHUkPRz3IAuTwnwd_pywoXR587mUtNVmAJuznc1jQQBeWx8m8vHWrfOpFcjcACJH9ualQcEA2R2vO_QLhAVx8lyOc9u_RGefpr6qKyJW8oY_ayIXGaSdOd-_suTkzG_rnvs9qaJmyU3CyoX3bw8ATQLwrUh6FlIFQpRvrHAjyoDeQTdpXb4m5urfvmKOPWLtaHrlWsVrR-MWpxDptzgp3P1qjNdu4WZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a4eBKxSARdrQfzL-TRO3YldICElgLV5yTFfqHCsqgctB5ZlRI4f13bCi6bKKaCCWUY358nm8JlP7WkP32hWeMV7MTRihbqJlGfYC0u2MoGh7rxX7KH04FTWwOrlWAVx39PNAm7YXgv1UUP4g1kDtr3ZH5aelDQRKCVVXuih21l1AwjRAQtKECoJrQ3O-YdDhJm4nU6W3Sa9xr18hXLUBh6xPsq8ql0ECvorAjKAvckkRhr3ArJUzWdYe2UpB5ADaesdm6EWzsjFkOLaXI-SgiUSg8G8yDnnTAT0f8E39sg3zkXdtWDjIXZUQbAGSjOVT-VuXn6esPyPZEAH13e5lug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ubig83BYjGmUIMOw-5tImnTMfEky45nLEJEJ5ZzX55o5CyJSXmxjJss3EQrjRAhm6t0Bgy37oGOEqS5ir5J0VaNf2eFTs64Aib6Ef6stY4cuia2G2w7dza5mWH77GKfxQzcnCBxWZDI_vZtYOJHaYH83CLdCohR53WKBkOqZhY93nWvCuvMohbkQW6oNkSNoLDVTAIISNtRzvtPojgjfVim2P6GHa87Cg8iokshhA7VCgl-s0phAoPM56akQ1Qk_uE0HeWITDAqd-fvYz3LvNvGu2ts5O3b38K318dPh2Ky_V5XsUfAMJropzxReyfe9CaC2HjjFrF1YzS7QBxNj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tNAy3-EthBKrMjcDk0iODId-4NiMx70GMzGg1BHSmilPrBAaymjMOLO1d1xdWY4h0PXD9uqxi6RNV2nfazFAgHNM7tu4JeSmjVt-CZbzZZ2bVyC8T3gvmZp2G_W9WITYlbRFFCPy6G-i8qOUb1V_3eJFvxfjMOJ4wU_njhhXs_Y-yrvLWRK8nriWCLpSkxw2sGwWwxN2YuZnnloJWKnvu9CXjvAcMHq7V3Mb9rYRk-wzr3nOTqSqTw5lC8WYg3kWxqGXQQ1hwI01AiqiphUHZdBvyAkiXsX6sgCRiG6k7lcd-v5wVRtk1bTECaMbreaQb6aBTSZX-X_PQ_4GFz9VuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iZxC3z75bxsuuRVoCZ9AFb9HPrhswX3xCsVvclWsPxHrRWe9FCjiP2bMT0-O7kJl0i7v1k0ptCef7XJXtlBYsN8myletuv1fNRfOJCJimag9z3AKL3KSdjFX2pF6Tjlwo-xfC6xfSvaiVztUrkA0PHDpnJoXpBMMd5cMPA8rbHf0VKCrSZN5y3j_C1mU3gZT-8eWVtrsVRagcby8mZ5yyZuTY6BrIVZCaDjOJboQvdNl2g7czS9u71KUeMCLIpEdvGKexA6z5D7vYLC4PtJMvsVp6DnCUbIsxJU9lVAwwC2ORuioEr8tqFprCw3aaP68VGImHJwv7qTnp4J5Y7nBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vTtXGkp3DdWqBC8jMtuejA1s6EKd4bQsuzL2Z7iobIzmU3hetkGlfB2n2ltLPYbKssmTsYefOoUsbntKwdlggj28YYpFSIl0757nDkqihDoCiuB9FzK5q5A-GCyzbbVzsSPfCL0quG7ntrISTIlHsV6_qRzETQEmCGa3I_O6KqTg_DOn_mgnrmtLf7copJKR440WNX_iF1fUEdaUbISkEO3GbLIgU4xA8rMRP21tyUahWhON6s8hLv9yva_2C2qFbjJvsiznYTNL7I1FQ0nRnK3fFUF5foEmNC5nHAu86kFnvX8pscNjo58nC_gNhueXl6DfG1PxCSwO-gYlMnvgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CrpkXOvcBXZxyBV2O34_ystNWrX3ICjiZeRo5WRKSlKlefIsP8YQ9EdMlzV42ORzaYNhYjh5pXsPfNlsjsLwIAZatICUIAJYz0aMDRWGG6nw-pUkSpjMo7AEa-RCnJzKK0k2g_3KZJoq0x-Y5PKDYGjSgXwfG-hVNlJ7k2PJvGCEtzmbrPf0rcLmq1LHVG0siHxcp64FVxFUE0FV1f2boJIpy4WA7T3LNVN5PUMM4idUsA0aORCNA-HQVvOy8ea_WRJS14QOz0fO7BHBMnlBY2DjabUS0fg80MVloJF7a0NHDrolPhUnmP2Llti6C-rzqZ3RufDMqhc5y7FBNfKcZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWM0ivjRYZzVFhCeX0t9HJU6D2KRbQQ0ybbzW1agYws0SLslfl6GQYUUMF1V-57jm0tUp3Rz6dBLAF6iIgi9FkdbbpatxNcFbvQA21kjuFvuvsSGZyUhF68PVNNuKcdNXm2elshZDbBMCLg39u0XRXg042ur1HhFyN_9B-aD9lQ4nnJ4VS4cnnrXxS5oGcTMhy3e2RQ4OCCWu1VY5-VkEx38qVR6-8n5cxJ-wt0GKvBAgK3y7Ljh4UfpFRIo49SAUsY2yYCLbxtSwyiHaYnIv6yua1HjMmbhUxUZqYrJgIKW1cXtgxMT6wCpyi2HPKSbe_4bPUo-2Lz1MLvvZadyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dtNYTMYXwV5ou_X-XZ9LqGwP2n-LDi3HBh8TTksFJQ3QdOnvnpPRtscmbCSKJzdrPOomdsFmSvwepCqCItsSq0JGhkOlg5zD0dfwv1SwfNLoFvp-mJsMbZIgM_eqe67k_u2jxJ2EiBfHAvXPKk1mQhrD3T9pJcr5X0SST9-WMntLgT-HhUH-ZWQxct8G4KlR1Pe-E33NuZA2E0VmganE2X-r2_ZgG4kyCl1LzoOvfI3RWH12dKedf1ZGCGIQfwr8N3AYeXcnmv2qPxvjGAD6E3ecgCOrpPRJxf3Z6Dq2Ndvl_mkOf1WM3oO7h5wU5vQuPXz8DCMVVBcty7snQKOBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhLzSeOlfzfXC6ujUdMnVKaQCL8pPmMoZlpwX34C2iJ6pya08lcWN5w6-QUxY8U73slXgyIAJu7YRcV3CUX4ui1md5xwRLeDXZxxTsP2nkGXE_S6QYTYCiPlB-QLl0uD73DCssypjFKyQwIpQORVoH2I0ZYvHpdsJbJmD6PTqZWW4wiOyF1flg-PDzq5Gk1CEt-aW6qQmLjSxWzWyCyxObDQjhTmv3oPtba9do7G-z0-NvhAbZHxoLjcYB7i8-plwaFLAHtyT67eVc9pX2-lpAMqy3ZEHWyJOeelOXbPGh8Ynqor-ioNBbBU8phPgtNTz544SXaENtM0d5XtkMWH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=fz0xwkFPiPzAeeG3HusU0Cq0KwKchL4Qx8VrwzU5qkSTDqrpK3d9MMZb07CYdUwykHVS6RlrzPpPj9W9okC5byJ7cSmXVxSYgsVNBRH6I0X9ppRG49y7NB9v_8ZwYs_h8nCYOnjETuZ-K7VSV-VZODxHBfaeGYV5xqj_dRAkd-RxjS9IiysH5-Tljxfy_ui5b7sU4xFz3EIAkPcYhWGQxviUXcYA-eM2czcRqaRPLD5vjX0GJQTYfyjAIPlb40IOCr4LBLYDfT_gtHUhCUpPNl24CdzoPmgu4vuTddtal9-1CNvJIkfgL2Flqkgro9ixREuNogcrBPOX8khBkv5jKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=fz0xwkFPiPzAeeG3HusU0Cq0KwKchL4Qx8VrwzU5qkSTDqrpK3d9MMZb07CYdUwykHVS6RlrzPpPj9W9okC5byJ7cSmXVxSYgsVNBRH6I0X9ppRG49y7NB9v_8ZwYs_h8nCYOnjETuZ-K7VSV-VZODxHBfaeGYV5xqj_dRAkd-RxjS9IiysH5-Tljxfy_ui5b7sU4xFz3EIAkPcYhWGQxviUXcYA-eM2czcRqaRPLD5vjX0GJQTYfyjAIPlb40IOCr4LBLYDfT_gtHUhCUpPNl24CdzoPmgu4vuTddtal9-1CNvJIkfgL2Flqkgro9ixREuNogcrBPOX8khBkv5jKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=inIZQR42a0mw0YqSJcwEGtzo4MCGcVem1Fz4ZCDOANNhGH9PJzXmvyCuniPuvP6WxidX9amwRpOPBtL4_-uqWIlsXHmTeeZSl8f-WvwWa7O6pFLVZg-2jtlLsak_jar1C-H5EuvGSl0V3inrpVcphzZuoQ7Mg1--bb5vc6ahcQYvrCS2VYneSEQCS2alElRvDw-nhwYIuuFmmyQ-tTeO7v78L57w4AYuGg04L0tmU7CsJljlrV76yZZwBCzjcVTGeCcb_PhzpjLMA26ktp8BoP2eZELJfO8g8nT4mviTkZYsdfk85TtfTSTV-drTltDhm019PqmSfDpYrHJweDE2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=inIZQR42a0mw0YqSJcwEGtzo4MCGcVem1Fz4ZCDOANNhGH9PJzXmvyCuniPuvP6WxidX9amwRpOPBtL4_-uqWIlsXHmTeeZSl8f-WvwWa7O6pFLVZg-2jtlLsak_jar1C-H5EuvGSl0V3inrpVcphzZuoQ7Mg1--bb5vc6ahcQYvrCS2VYneSEQCS2alElRvDw-nhwYIuuFmmyQ-tTeO7v78L57w4AYuGg04L0tmU7CsJljlrV76yZZwBCzjcVTGeCcb_PhzpjLMA26ktp8BoP2eZELJfO8g8nT4mviTkZYsdfk85TtfTSTV-drTltDhm019PqmSfDpYrHJweDE2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nVfu3BkZHmlStowY2lPTucr2p5h9EzUw6zwaKOAjjumBVGHdFojjb2IbSycU-i-E_986Bn1VxNwV_gLBdJFD8kh7Ldu9oMLbdWI5l0QTKGkj-scW94RI8g1n0_9WrGaV71zuXfTblr6TZrLphD47pz0jh3KgPVyef8n1gpYXgLYDKIxW5j0GEhKN-ni8fXyAjz6yXZq4J7oPYrfsNOkwqkW_gXgtZDp5xeOyfc54AO2yRiar6XNVNeFyd_q7oSeeD15DeR6Jq_lKAJel62R8_txxMJ5Ign0ldbX0zZUHUdyc46n7dzFH1Xwum2geUGMt5SLMOM30--vLHp6aKvB8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVZSe8M6maCnS9ilE1tFNtuRIOzCal8X04eSt5rE4Hq_fVy9mR-d5OTxJ5JWbhVrWFuNe-CoYIARMo6e_Am6jKVSroSqgaL57zPjn1c5dWfO1IvURhWolN0YMpYIsdtZkLN4sNlo5X3pmDzT1HkWG0hwucHdSuauCkVk48HLJkqen6aIILS6nqf6wTbDecLp6Ml_tv_6p6j1Aw_fBjHdce7jzUndUoVbgkFdIgSDHB2nEAXQXFeJ1aVNgwSWuOUlZRotrUh0JeIkiXlElXCDjL1bZwHc-YeJ6NUXCUE4-Id_TKfhoZL1er7ki5L66WBcmQzoQiN6SX2hAN1NOjsGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
