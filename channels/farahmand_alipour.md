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
<img src="https://cdn4.telesco.pe/file/G1yguFHtk8vNXSAuAdBmBbfuaN7jTXYnxN1lwvANXL-S5CNCbPqvZOTisKlYgZ393raMwPFicou7xXIsj7CvFI6mDm2hhTAoUZ1A6uC_5IDl1cO-OfMkvKbkXo8Ztm8ei9WZEx39iAbfeVcNDXfKZGEVAk_SwfMSrz207YXNxbo7h91B3xAvxds7owsYdg2xU1cpFUIYyqVSmRrXyvAbKcmuA3d_CsgnoeS0LA5003FDDCevjRR3zu_t4wWWYTnkPpNV1oGaqjF1VI2qDv3XBDtHxJ3UeJLOX8ztiWaN06fK97qruLTjSty2Ku0Q3HISLEyNbh7Y_xD-9q6vJ11b5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 05:34:28</div>
<hr>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=NUHOS09AvBlAGispoen6jiG5oyo-_vMxz6amTjCzvYEQJEAXl76mEQjutVuP9--VoDyZRnwEbpkDIqBsAbxCgU8eOPJIPVJ-HxCbLoI8DCssxfVaLVcBkrodPUSZPZ-TkJIYyXNZdGO_N005RvCMjMAQPQbNWjf8Z-ovTdr4QvqtHXWIJiPwcaUaGUbutePprYbShMFK9LyXjeeDpwKx_mus8UzmOvCylGsJ4vClbFZmTW0tRAqMSG_wkGJ7nRyBT7OW5ilJVb2MYRSc1Qp5L3XqcFDU6PcKUDY4PvRbDS_tSAKLq1weyiKeTOjFjLNPRFtu_0pob4hESQHUTusfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=NUHOS09AvBlAGispoen6jiG5oyo-_vMxz6amTjCzvYEQJEAXl76mEQjutVuP9--VoDyZRnwEbpkDIqBsAbxCgU8eOPJIPVJ-HxCbLoI8DCssxfVaLVcBkrodPUSZPZ-TkJIYyXNZdGO_N005RvCMjMAQPQbNWjf8Z-ovTdr4QvqtHXWIJiPwcaUaGUbutePprYbShMFK9LyXjeeDpwKx_mus8UzmOvCylGsJ4vClbFZmTW0tRAqMSG_wkGJ7nRyBT7OW5ilJVb2MYRSc1Qp5L3XqcFDU6PcKUDY4PvRbDS_tSAKLq1weyiKeTOjFjLNPRFtu_0pob4hESQHUTusfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=uhppZHsKlj6yoLSHOLVOpveSirXVgJc2AIK6IYdyRxFTaecwZyCOeHs7zgA1I_V28khg1Ye9mLwilmjwWu5Tvt_1W_S-AIWuf3pDwdg5puP9JWApXWQvgGryAzIKoZTkb3599PqcSnJxtQfoshAiXGfUVC6hLUOudZ5G3risjkx6lupqIDRPawFlUNSjI11xV9LKYxwZ-N-YWYSfB8J4NU_VW8REuuiXHnEvQUC6GpwY_uQqvBpUi3zH90XaZ7jKVduc0P_ZgS-uUp-5rxJ2p6iXL90HAiUVGaIZLM7UKn7fjUPdIQ_NifbCLYGUmGxB8z_Y5wmo1Q1U0vi_0m3IpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=uhppZHsKlj6yoLSHOLVOpveSirXVgJc2AIK6IYdyRxFTaecwZyCOeHs7zgA1I_V28khg1Ye9mLwilmjwWu5Tvt_1W_S-AIWuf3pDwdg5puP9JWApXWQvgGryAzIKoZTkb3599PqcSnJxtQfoshAiXGfUVC6hLUOudZ5G3risjkx6lupqIDRPawFlUNSjI11xV9LKYxwZ-N-YWYSfB8J4NU_VW8REuuiXHnEvQUC6GpwY_uQqvBpUi3zH90XaZ7jKVduc0P_ZgS-uUp-5rxJ2p6iXL90HAiUVGaIZLM7UKn7fjUPdIQ_NifbCLYGUmGxB8z_Y5wmo1Q1U0vi_0m3IpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rjByUsw67RfMsN3LvOUQHt00mVKiLy5KvbNz-jgqbV5-fUJRd6UXp4os45E84CwG_1nNvA2dARd0D9MvmrWJsn03UYlb2_0p89U4B_CeUQRvTXHOBQBPi5myK5UmKa2O41X0K-f1a9rDHyjZ0qPK2Jm3YlkAepQM29wAe0hFZhIQu1fCLgZ59r49Z_FiAtAVOQoQz5L959JhVgsQ5LSAROlR0mmDOcC_tdfw_QiZgYQBSgyu960HwIGSSNfIsuM6ZzHuTz_eJoqa70t_WjhSE6UqX2TihsWmm4ptmOR3-0sIKxwfCE8_whpggN-95DMMsEEAnwh99QB3QG1yqKEqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rjByUsw67RfMsN3LvOUQHt00mVKiLy5KvbNz-jgqbV5-fUJRd6UXp4os45E84CwG_1nNvA2dARd0D9MvmrWJsn03UYlb2_0p89U4B_CeUQRvTXHOBQBPi5myK5UmKa2O41X0K-f1a9rDHyjZ0qPK2Jm3YlkAepQM29wAe0hFZhIQu1fCLgZ59r49Z_FiAtAVOQoQz5L959JhVgsQ5LSAROlR0mmDOcC_tdfw_QiZgYQBSgyu960HwIGSSNfIsuM6ZzHuTz_eJoqa70t_WjhSE6UqX2TihsWmm4ptmOR3-0sIKxwfCE8_whpggN-95DMMsEEAnwh99QB3QG1yqKEqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=NVTrVgvvOV3gyxNs7L_Cd6ybazM2sKzDHseO1GAyvbLxD96FhcXXZMUT31UXDucsY9yXRg9LseLy6L8MhY5s4ou2zzQETm-5stPla-uUzeePsLA7H9zl7D3yoWF4x-mUvPf0Lv9ze_5kTKuWRVnef-Om5rW1BvsmSvIedhPOh5yUiKOsUZl15Jw9mhCpl7gyDhoNOGUVWfa9Vrp6SeKXIPsNQU5uSh-ln16jP-KtNogz2GH7wyI8WTMZVrigYCiJeptTO6IwHYq7NB1cGw7fGuh2Lxd3benwamOBX8woVJxqAGJpgr8AeL57qrFDGTBeNem1qJYo9Pb6aMw6DuR7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=NVTrVgvvOV3gyxNs7L_Cd6ybazM2sKzDHseO1GAyvbLxD96FhcXXZMUT31UXDucsY9yXRg9LseLy6L8MhY5s4ou2zzQETm-5stPla-uUzeePsLA7H9zl7D3yoWF4x-mUvPf0Lv9ze_5kTKuWRVnef-Om5rW1BvsmSvIedhPOh5yUiKOsUZl15Jw9mhCpl7gyDhoNOGUVWfa9Vrp6SeKXIPsNQU5uSh-ln16jP-KtNogz2GH7wyI8WTMZVrigYCiJeptTO6IwHYq7NB1cGw7fGuh2Lxd3benwamOBX8woVJxqAGJpgr8AeL57qrFDGTBeNem1qJYo9Pb6aMw6DuR7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzvzQg1_t2hbOwZ8E7EaiomDRkRaPDZ04KwNq2whN0IfWA6xUzamD5XD3IGXfPuyfr6mQhy70-gAWJarEskaUpdlLr6Ch5v6aMKgIfFGCMj42oJIjp0N188y9jWuKPYor10CH0hTlXCWBhm38VxIKBqR8m3hyE4BOaJlnysMZPflzSSlmkYeAO7gYPkPwSguimGimPq7NST-GuIs-ZSf__xlgd2KrZVAu-vRnOhc4TYwbSXveBV0-jbppuA-m4I8BqunM89c6n9seNerh_cNL2FDDJQSAC7ccRu0-L5XJPx679vYWRWp7BbNEfw-a7do-ui4xtY7YAcTBlGy4Y3w-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa1SUO_3erGCcGeODvn4X6O6Nn81h2Q_rsCh_Jvw7YwQ0ashMqAkztc1xj72AxFq4KbJlYzaOiRSj79amKdKk8Cj_iX2SmsY9x8H0QBXbb3b7q4qf4jTU23k31cDJy5W0a9vrV2yNSCWzwYWEki3DMMpOJqdqzgAKdWfCWO5Mn0b0ODDKc0e9qPfgdYw0Hy5WXUUggDFqOLB79KQONtiU7G-drjgqamt-KVKLzKv13H74vnaHeFvKHL90CKxf7PFdfg9g6xFynD96ZLchL_CaDOlnkEHtpiaE5kxixjHoSp8KkdoBD16GTE5vPMCECdaODE2SMYH1NW8v_IoTh_2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etJkcshiWs8rQ-v4V7DNLi15Au2s8gRTO0H8RhSch2JcFzBr0II7u0qw71xaAPTVChTndRR_ueX0zLdLYMso3l9T8nEdB9RiIMj4ekH0PurtxCSJBD5uprqfAUX3xZoJmG1Xx9vGfXoP1CBxCHoy8kfUWKhuK7ns8ccKvtRNYNsjN6Cha1kUuWqvSFatUo1shFBnxk7Vu8uH4GXKnpzTWR_tpqfADg1E4nFiqWUg_z9VHIQq0LL_OiUiSFtIAGFQr2O58rOQrdQMtg42ke7sxbXLrO_v1zxr1cN5Si4n-xX4hxOosQ5WvTp1lQn9P2wmkPOEnMOn347e8ppFoMP0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWelbRb8XSFqxIrc_vTotVmbN2n4QPda70hcD3dfSHGMOYGKrSyYEzk_9Jws-Hz3Z8dTyNXMJZ0epkxcGZ2BUl5M7uoqV-faeL_O-7wh2WMxFP-dTIl9YGv-qE6BnqsaG4iIFsmxMMjAYTVzWAF07GsxNwiC30S1DzvF37kI2eDW6mS9ZHxErCltbSfdmQFlATje3UiNZQvuYDkPIKQYLWq25A4Zv2q0THv5Bq28Kng9z3KoXg1W_1NJC_oKPu_x2jjjPqAhbA3IHol0N6Was_JzGOIgPQgEvoGtvBmTR4PkZhdVzJUG-N1W0neNf1z2-LA_d13f6gTUVxkxUrD0fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH68NWPUAfl87xVgUdOTn0HP4e7NotuhIylwY8d1A0BbSa0IHY_Nsuj-vgKIQsq9Gsuqrqt03zGKG-58XMXXePWVLuyRLpLH_K4Sv_WTZF40nRDOOMyf5YENUjmUXLw06f0XQo4yBz3xAseLiZtvhQcEhPjxmp4H0tNMTztUrwMLmO97_N4fj6kLAeD88A46uup82Cx_kXA_V7JulJg5MdOp9YRhsbMkVQ3gZF5tRdwCgq08oUqhB5vApteuwHLiNooIxCQ_AdFk4r9bxaZMW0F54bL31nfttuCg73K1kqy6vBk8TbJjb_KqK8eR951DLfGyLe6CJAOI3pn0qzLGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJNChKs8UX-xwTz_nykgmipLJes__i3DWZqKtPaGjHicjYxD8SGlHekrG4AOHGSDZw2dwu6jkUBfTpaEzWRQ3goSKY0xQrAkSR5E77xtC-eLnkJlM85mLNYwsHIKh5Anab6mhU3L9OR4XO4C72HIrV3ZLFUgqw0WLc3kYVkCdQU9tL650gY4bepLFtMjmIiDpv81aKhozdAnT6-vWyvBAYKl7sMS1Aknub75YCHAW79ThPE7K-847a1Ut68QcJKFG0lfR3HMUQWfwHp1m5KqGqFrhM4xae5Kew_vttmavqZCLNbgkr6LgoCdyS-XldqrWrgvKxkXuhwy1c3v1-HZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITXA13_oTN4uV2FBVjfUB70-sG8QzriTPbq9LCSgZLFwYU0CfOZSuO99RiCi-KuFbITSgDKcgebqHaR8Ll8wrxloaZTQtvfAewGEQ6yLn5cz1O5Q_uZ_Ol2SBhyRN98JcSR1wttc01Q5LRWB9c2pDmx2nzWcHRO_PlE0GPBUis8rRi3f-CP2Xe6lzw0lx6og8TWqOE7d1HJTWP-dvEhJqa7iT3X_1wnIBAS8lXJx89v6I4W_PKA_hQZnrQSJDDMwRd8mL9SO4sHhFluTFBkDUNjveoFwDTfIAYBLHZ0fKUZQTYX5N5ISAsEAmmM6HuMInR_aTPXdwrzMVyjjLgNNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ui1YE3hFK3ltp9ixQdKAkoqUoAUGBFhIwe4hlAi9EK0mhQ6Ri0g-u5k2rP-FNmS2jVZRW2PjZe-icKoT5cxH-bI0cgaZoLflMAM0uH3n0kDyCl6EMdbMYdTWtusO_ONReYI_w08-7omhC_OVdLZfIRS0ehXJ4CbzcNmm3gQCdK5FIfbo3AzdLjAjzXx50w4USEbYkitR0K1F5vCyw1n-pcuVa5S5JS3BqrMra_5khTfNP3CqPlt4RD8RJ6OjNV_t5SV3WR7x-2Go3ZuslPgfnvd72e0LTpHd5YVzcTFEcU4TNZpeGiVCZSChtuaHgWj7T0Xb9G4tl75TYVlq90M0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ui1YE3hFK3ltp9ixQdKAkoqUoAUGBFhIwe4hlAi9EK0mhQ6Ri0g-u5k2rP-FNmS2jVZRW2PjZe-icKoT5cxH-bI0cgaZoLflMAM0uH3n0kDyCl6EMdbMYdTWtusO_ONReYI_w08-7omhC_OVdLZfIRS0ehXJ4CbzcNmm3gQCdK5FIfbo3AzdLjAjzXx50w4USEbYkitR0K1F5vCyw1n-pcuVa5S5JS3BqrMra_5khTfNP3CqPlt4RD8RJ6OjNV_t5SV3WR7x-2Go3ZuslPgfnvd72e0LTpHd5YVzcTFEcU4TNZpeGiVCZSChtuaHgWj7T0Xb9G4tl75TYVlq90M0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5mSTAiHyMaE1tPBs1YQq3Bb9i9HqpRUS9WrC-DXUyBy8dAYmVw1z5hWcZvrel0TiUKf65b-CZemdVdg8mnDPk4YJfV8mamxaZFhKdMlZLbxhulyOdTB-RrTuB0zfhuUc7bDKtqd3JO6eU6cq3zeWpocFUhFV1VaaV7WHgciRoYp9uEDqaiMMuGciOl00WbeE64v3EOzB3aJAV4phy2nm0LV44hHwKEaVmXalXvJ033GWcMXAIAcZrds8BsMOVayrcX1xVfDcIWDwM27J4ItzjFzbR85bhIVt0pNSncZ8mdaRnYCGAo_oPB2dZoI0jCNVXuTp3q46dCeX1Se_Ow2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpDXtwlerrqaTW6TweJou17vaR-Y7JbhhRBc52SQKt6ja-BnRMNTYgq-GH0f77ICLA-gtxQNfTqHbRAZMoII25okY-gyMc0omQaJecdRNgc57hwCSUS1oFOl3CxitUQtHy4gN98jMBg31TnU51UzYD860PNJHOEwMCyiCV1bB2BSdG1GVIYyK8BgbmX_CA5g9H_TmLEZpZ8NrL7eYJsrkpBlR_EEFITSIvHEKcx0xE1Wa0NYx3HdRAWKYZCYyFUNangkeomruDGCjLbk1uSsX3mdINFynHZVOW_epm860ROxjcrE7GkxDt06PKYWXQ-aXinTjeKluA5SqGVaBvvi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlSCLkafqLOGjA90ur_0xp8S3dpMoUlGeehJgAy-FlRStnfGTxXQ000D_G5zbkUePKkjY51TH7WEpMtGFP7XYOwpZBIPWkz6ifcST1FRnCUG9WAWrCVa7BQKHphzLdSVLX7SQLi7EEhbt6l4TPrrkr4AIxR849keuaAxc4Z8025K2eMQbNTUswxBEJD80cVhQOXfgv9D7HulQ-Aqy3D38c4h98wlIb9eyRZU7hUnS86l_IOu6a4GVyuI4iyxTA5gd_dy95xqM1JumqUWPYCydNLDYBmCOmIB0iEPwP-1BtCK2H4eMM3lGXTQqXxVbUJSiP5Vqv0F169LT421NV9kKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flmsoJJ9lkcp98hsmgYyz1Cq4iH-1gUuYD5eC1-GUdE7_3SvX9P6uLsK5SduEske3uPgzk0fK9Mj6WFhMABIjSiku098T8aKjQColm16Y7UyYwpOS0vwrb9wmgEpxFaECHGS_CfjdOZJyP5uyLPHjzybu9JbU4WRQ6lC2_2PMn1OG0ORP3AhJEVwpKlL35Kza0jMipXb2RddSbbMLpIVw5HS4o0792UhitYBHrgtBLbQU1jqOQtUOJSNLNuRO7GZAfUtFfs7vf_S65OKBLQpcDNqviu2MKRTrp1zGt6qio-MgzZ_a-lgpdKzZHFi1iNWFZdB-3JsNOaOjLPzd_OJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1nyaWc_y_tHnytXZe9Xzxfneo6UDlI_VeZBZj42wnDYoVz4UpiPDLXwDqwickG9TfjpYR5vjfgMuSiMUuQBHcekoP41dW59-PnD4nEtaj6Mq4VQF6iOdW7T9785EyODkXtA4Xg7rFVaOLoYXEd8HU3a0F3Pm-X1fbp6ISjKobmZENjTT440azKiL2Hq5j6DOVHabI76HGWSyE7xlura2sU6SkVgb8jK7Ef8rMeW0KssSrI2T2ta3rsihD7SzH4gKrvXxkoy2NPxHq5h8MoFFaejWJRX8javc-mMpxniCl1DAmfI9fjniwY1b1fBCd8w-5WPUtJy1jyssom9NxIvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeXxdLrRNMz1usORlDK1iffYbnOKusK1UdrKaKSSacPSKONLcPP676WMgEG8feTQBh3FTTIab4vwfyeBeo4QBwnYlid9-ZrtSKPnIAaCBNd6cYLruyQ3TjvXrK_GE0j1Czdb03xhESpT22Covzbi3CQB1Y47o1jhP8TONk5-gXyB92E7GhqmVJqzpeB4e0wc5QaqYcYeJOl4s97nNZ_lYT8Cq3EKBg7pIfToAnb4-32o7-d4oV-ku1-PQM99_3xWdBHenbKQmsVgqVpPPbrROWxraP64sLY99yiQDEcwproE6AsQqrcLfVIkEgnV7qz-5yOr6lCrfGMg7PRtN9ZDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9D9-zk10jooaKEivcIdLn5DDrmezeu-WEbh9kJBV1rGXeQ0AByoTzUMDOi6OuklVzH5Xnt4Pf4DifPLh_pLA4NeXhG2-SabX3BNKtkeDW0DPR4UNEJfwkl2Mw6cejkS-4VpNCsSrz005t94iXfxVy0_lM3e1298WUdc4Lhrt6mrOkpgErCc9XOo83wWtcj7IvlNsrm_TXoJF0fBQw3WeMeNpzhLfIOtvAZNJLBtvWfAaVnG5Xo0F2JTe1E02ajUMwuu_wf9e5fYiAEBYzBA8KmVbbrOW8O8d2Z_njdRj5d96gKjRZusOQ2-ICvUgR9Pz4vxJP4mIbzhai3rBdzEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5ctTG4wQkKzMfWcMvAx5Alf5vkLuGNPFDf-UNYAnDrm_hRTBH1ftSdkah_-c_meAdamc59n96rd9qfu7r4_D06EFI7Gw_EBZkjOkugkdsx3ItsX0f4j51taWlj3uOuk4hrP9WeLXH9wZUObXy0mi6DpbYXp6S57LAcIMyCGmlL04CX-DtyJzUMiqHV7ASI31A3HHfVp4L7UM-KeMN2tK-_dEOwBwM8jnBuj7EJ-rw89e3J6vh95m-gZmnh9nGzfvAgiejmW_EFUDb29BK5sqQpfMvTTtQPdfQj_pubXnx06puYNQ8fqDPq1agzZnMHIbozTG4qnKhIfC1RaFHBnEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=LsgsCC2QMzvNAhHuZl407JbO3Gk4Xl9PMuh0KeJ-3D_lhhaUwa2crYzlk_gX-qFz7szYd6Zqexm9fbSD42OAIsqCdRg_lSvOLyoBrvmOrL4rSSiSJPvd93W2GZJfVX-8tzOi5SR_kJWBtPwm9rZ9eHFBNoP8I3bGSfy4YBr4aEgrn7--TTmWE9ABUfkougcdYJblcB1YtJRcVINQULk7MZ5IwQvE8Hw4m8OA7hpsc84RHHt9sbC_-IMprGPEGnfX3BN3hKHWfElqX4nWcicSJacxw38Thv2RMwdqquqMbdl-34OxAWMpYCD4-XyC1zgc2wtN_FUPkZsjgYD3rXlVQHGIOYMTlxJCR0bwAcjUc2slneqm4PIogG3N5_abQ4ylZ-bgkoSD7-9tQyf1gETDxwt3bT1ufOxAREbPmIfr7OxdjXmEjj9zrmiCmwZP1HBrICrAPjVtL8sz7QNBPGeWt38IF4BKMVuTDImXFzAV7KzFpRbnrRFEGjTTmOdZ_P3rpV5Va2HICKKJCmcyiPNMJItv_OLLRgYIZxo98PR7RaYDCy764vWWAOtjQgoLgsN5X9VxGP_at-07CP2Su57nCOCBwjTvjV8FKLYXJSFDse8ipuzMcKQlqe-VUYZuEYTiCMFGALxZjmZJxbYHuoJisRn0K-tsCn7BatKjm4PKe8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=LsgsCC2QMzvNAhHuZl407JbO3Gk4Xl9PMuh0KeJ-3D_lhhaUwa2crYzlk_gX-qFz7szYd6Zqexm9fbSD42OAIsqCdRg_lSvOLyoBrvmOrL4rSSiSJPvd93W2GZJfVX-8tzOi5SR_kJWBtPwm9rZ9eHFBNoP8I3bGSfy4YBr4aEgrn7--TTmWE9ABUfkougcdYJblcB1YtJRcVINQULk7MZ5IwQvE8Hw4m8OA7hpsc84RHHt9sbC_-IMprGPEGnfX3BN3hKHWfElqX4nWcicSJacxw38Thv2RMwdqquqMbdl-34OxAWMpYCD4-XyC1zgc2wtN_FUPkZsjgYD3rXlVQHGIOYMTlxJCR0bwAcjUc2slneqm4PIogG3N5_abQ4ylZ-bgkoSD7-9tQyf1gETDxwt3bT1ufOxAREbPmIfr7OxdjXmEjj9zrmiCmwZP1HBrICrAPjVtL8sz7QNBPGeWt38IF4BKMVuTDImXFzAV7KzFpRbnrRFEGjTTmOdZ_P3rpV5Va2HICKKJCmcyiPNMJItv_OLLRgYIZxo98PR7RaYDCy764vWWAOtjQgoLgsN5X9VxGP_at-07CP2Su57nCOCBwjTvjV8FKLYXJSFDse8ipuzMcKQlqe-VUYZuEYTiCMFGALxZjmZJxbYHuoJisRn0K-tsCn7BatKjm4PKe8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=vaRDK2YxmwtAzvdQISyNk_fbW-A5OnMsmmoYrSWyk4RKt0-ZzhFeM1by1zMfdT7gp--JjRNGNir0LRVEkafO_WfFprnh5sMLYusXyFIY728SmKdBSjZQmePWfKhXvscd64WxDpJZDlh1XHqOgsDdSaYb3F0uLcWT_nFVmLD-R-6Z9QnwH--092gfCXwIc4U59wgUjdk1Ud2bLDcE6Digt0bmlL_Q9SgqBSUKj1tRVOR7YwrKRB2vvHvClUTj430tJIk9jiMTkI6XXKnLRPikF3HjGoGdtX0P4uQSZYFWT54gkktvIkG5tA1Ic7LZ_CAAduvjAr9BUXR5qeZAKiIqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=vaRDK2YxmwtAzvdQISyNk_fbW-A5OnMsmmoYrSWyk4RKt0-ZzhFeM1by1zMfdT7gp--JjRNGNir0LRVEkafO_WfFprnh5sMLYusXyFIY728SmKdBSjZQmePWfKhXvscd64WxDpJZDlh1XHqOgsDdSaYb3F0uLcWT_nFVmLD-R-6Z9QnwH--092gfCXwIc4U59wgUjdk1Ud2bLDcE6Digt0bmlL_Q9SgqBSUKj1tRVOR7YwrKRB2vvHvClUTj430tJIk9jiMTkI6XXKnLRPikF3HjGoGdtX0P4uQSZYFWT54gkktvIkG5tA1Ic7LZ_CAAduvjAr9BUXR5qeZAKiIqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZUxryTQ_jeIbKDqHWVT_kGRl9ttlMInvtkZ_48Wp5rqpgUJOsfmW5nH8vPtcnOqhqN-Myt79hOCFf4TpGVkjXSsDN1gdUUdgT7AGSF8rkSiGur17-qWU5rMnPm7MMsvpxYJXgn4DWAbmhOoBH4mloWkauZi-1FANLqI-Dmr9llCCjj0EdlbQ-k0e3EPSxV_gCRVaA5Mo47A4PTjqouREmnNl3nW38ZEXynLhobQs04UqEnrntdVfW4C_E8ycGUTGV1DyLVCBFU0a0mlnQZei9CMb2b9mGmwXPy5U4G44SnJCWurvYd0a2FGotblGHx70n5lIztZS6ZguvmwE949PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNgVzMLe8Lihq_VEYmUcNBtIBqrJZQ5pPlUlE5uEGPzpSJavK3HgswIRYtMZoqW906Xnh7Q4zBxh5sLPrOZQB5sg3F6u8OwHZFcEmNH3g7lFaFntHu_N-7aWxDH6KNn875X5b8K3iPAC5o9bygC0-LYeuehHmnvma4hbYaMaerlE4grla25jHMf7gi7vkNGm2cPQ9DPFYSh83_6sKkRSVxYTi0FY9ShsSZO3iOZOMzxQ0ppB3b_esrlHj-UUDKyNm-FrVCdKDBZkGGMbzCepDTZUYf8xqJqtE7h18HovUUcAAndTm_ybnHrSW4XqlQHLM0dXk3cBR9M2DPNwvct5ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdLhsHIhWrm3MLaCR2dKf7-Z0kXni7v8DOCypO8SWRgwNzRJKbB0sraWvgkLxWxtcyU0qHT4J_fbb2GcdJ9zgvEoDXQ2mHkXTUw9eJRA-tX365WoCfZZO3RDopfjK3uUMWew7Qd9k_jx7KH9jKzcuPB5_TLHGELhec3VafsMfY06szteN3X9QsFtw8c-MDB2aoo4lJ-TeICKpWglrw7htUlOOwMkBEX8RcS9J81fmExHTu_QJWCBhxa8eiQl3il4y8dHaKqdhksB8GeqSWBG9ZgpZUzcIgAS9V8wamZFuZwj_g4FDjYgcpjcyYeLDeozw7eVdWPID2lnpS_3IlWz9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfAwbFKUmfHLA-UnpNGVIG31AchleBKZ_DBqKouMxWjJG-kvuCFZLXQJw0oPkjh5jHNuh9YZDfh1QodhlDOePHJePcu13bQujXQO1PzaQDGjt6sQnWzDUkPMiYR9zlCjjkAi36d9HG3bnzj8JOci8g_sLvFvq50w32IXjhezevjhYJ2dmB7iFrg4kdJHqHNc58T5Lw8vbMmQgGFyCFogCjF0aC1y5D5eGkscU3HPLujRyze1QVFhA7BI1BqvcLgLUVGGIiT-QR_xmkCdkFQ32tTBylVjA10pcJF3iwmWw8-qn4EIU47dLyMDC7K9vGR0_59lEktdJP3Oy7GZhDOZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnqSUSmkAxd4lZyufD7AHZ0oJMWwWSOkve3MhxOiliZJiXLRUwW3kJPVqZ77xLKFMyQ3cZVJcRR4eBDRMn5AfvMLsWvvkkK9YhiIG1cFuWwcLEHgKHN0krdrRy14LWXFXB_7hoaEP2KJmQhwfPo2zhKxxhGIQC_9H3J3gt6J_FSxNJuzBulmG190FHu9_SeBt7rHyI0yrROvrT4cVQOTe0GPgdzRnMnM3qRZXy-83n1IfZU2Gl5Etxw75G-_MiWEeXspAJ_n9yyx3GTJXo7pwvL0zeV17fE57rkl55ekHRZY0tzTmjZJPL1nM_SaQtEvANkDaQp2_4uFwE9I94vPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zlf4cqaP4Jjlo8C6OYAr7wIJZRe3pAnY1yufdPqqjBQ18oYRzoQcfZNsLKZeunfpXQ4p8_JEUEEK8erMqxhgvU9mpd-x_CAYYi0Nc5QmFyDWD1U39vu9yTPYiXXb51OCR2GPMWhl6OxybzeRRMsuJQKsJzmyFN4uKzmIkLJmB-_vDdXlzki0rkupo47GQtMSu71hOwo5-8zoIA_7XQcujFMFF2JlYBU5Xy9VI83FD6RmotCIaW5IFU7O5cy3ekHeynbMAPQiR6fhXj37tvNSmfrP5EHDsCY1sUbWuz3wzrVBIELqonR28WP_61rq41yYymO63UCmyWZyXHhSygyFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOTlpiwQqSrIZWGCVzdur0fk32XpF6VXYDiVz7TotzESC-LPGLnmWpd9AqiJRGxKTly-dtHPQcXWxy0ojCvzt9tKgu54daUOYLborXT_wP_YjnLIjpviEh6NEFfYN_kmo_rWxZhTCxKuRhOcYoR0a5rssch5SIrjYyt1Jqds6VjmlO9QeZGEM-Nc_PJ0XvTvtMmNvuTyoPSFxT4IEQYoXoj6v7TGL6VbaXpwXl9n9ouHPiL_DixFfgW6YcC5lGrwN88qPx60fFx1Koyn5-N2xmsEQzqzXjH8ZhvvczBdoIUG4mtc1FJHAmwHN532Ckp_x3nAotxy87nZzeZaLjjubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHYLO78C7BeeeKfznij01fL-l8O5mvUchMU-UHrt3JJpS1iBvYe1e8UHmRFvjcDQXPVzWVeYtlbvjwzCK0K6H3lMi4MkIWxiyb_cYyBuAAbFuMksSL_KIpP7xal69ZKxOPi5VmIpdv7n-dtKkWkZd3ZVkWfmmiengNdgyRkmXBntyCLEJQkfKCIhFlC3eZTJESfaYUylsUBZUr_-B7uVfw8wbvPUzh9Xep4XmC1ZmgFvURT3w-x4usSxkY8wUo2Y9coG6eiLL0o4LOkpij6SdRlF9CzMtkCZIHrv3s32wLP5ZbT8shMm10HkZEpvMIzfhpSrfjIl2VVFGofgZfouBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRbzIdZPDg24ZgOqMOfKO3GjsiLMMXyXXJ85aQziBeEdIi4ycBzBfdCGQgmDmmQaiwqX-kv3E1HgVlevV6nC6wp3LQldgEKvLOU3d_WJ3TewzBcdeajqKvaBEWkEa5KYVhT69YGyR3oweFcFtnI_Ug-V3LlNsNQUoj0wepO-oXS9D5FvflsXqFgmAz8_alEVBnwE1KUB3P0D66WybuN-KLbWxm9XzymA1LbGP8gNpjeLCe2X8CoosE8Ijm7JYH-NzHr7Rlwr5Dzkw_vZlrKFYCKuOjoIDaPCs1zr9LuJX_rgyhjUGq0F564ye5X3SZPC6ppBNyxo_7tu-tobnER-qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=M-GUVE5dObaio_9wKuhjbronMGbJA6xQZZr1bE5yyKKN9-pkLtxCqTLowdny39ebQhn5LFgDDqxd4yBIqlBkMrebvhRMlg-RM3gnzDWBwidVnT01iXlu7NOUz7wneXAEwP7rQQSpyxN7y9gexpwvYbJDzKqXahyomjmlIoRDPb4jDrunFACF3-4aOwPmCFjVN_uNZJKZua4nLdTDRNGv5EZUeCJjTEPvli3g-yCIQbG6pRsaiNlf5yJabA-Wzu7tMd7-gO8FZ7TWlnFt1wZiOpUjZL-DKQpylbIZKx14D_33cpOB-wJGcDGffzvkrCAFZnElGHs_kf9EOeFzlm4Zaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=M-GUVE5dObaio_9wKuhjbronMGbJA6xQZZr1bE5yyKKN9-pkLtxCqTLowdny39ebQhn5LFgDDqxd4yBIqlBkMrebvhRMlg-RM3gnzDWBwidVnT01iXlu7NOUz7wneXAEwP7rQQSpyxN7y9gexpwvYbJDzKqXahyomjmlIoRDPb4jDrunFACF3-4aOwPmCFjVN_uNZJKZua4nLdTDRNGv5EZUeCJjTEPvli3g-yCIQbG6pRsaiNlf5yJabA-Wzu7tMd7-gO8FZ7TWlnFt1wZiOpUjZL-DKQpylbIZKx14D_33cpOB-wJGcDGffzvkrCAFZnElGHs_kf9EOeFzlm4Zaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIlC-DtSuMsxyFyRqi0n7opJieSn8pWWZXLil4GCy46BOLWszdFyakA8dAYbP-FeBgm6EBl2pwZSmhYbmYksIPinGKVxUxbz0cqjyvZRsdBYBvVmdxhe_JC1AmktAbXRP52Haznb4pHpG1biLdP9U6UlNqgtGP5WuOhYQLepuCPiG5z8vYrFCloYmY2AttyYSJuqWIKnYhl-eHWS5_W02L7tuPCLAgZlJcDZSae2bBVtvAiQ4hmONohO6PebDYNSNbV3u3eaeBZQAgC15WK6pmXCBzlLQru-Dr3a60s9qpy7cVJ82IpdE7JYsj3-yFogrYDuWWLM3QuPAohtI-BUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=pCcWuybDih-Kv57T3tIYbk7D_NCbUzAsWW2NmAu6wRXhjkrZDcrVgmUZzs_9sywvkE0URMNUapWWYvBjCVoES1i6OGlXuPfWau5CkoxFBXnNtc9jlFsHzr6WQXLHYRszD1VjVjj-bg_aMIMcQbsDMYfHfQQRiV3oz5iICpjTv6Tztr4AKeqL1eOmD0loAjzthtlJSBV6p6x6eMiO6rHmRRmoaauVRMkrV6aWMcJiUF2ZM_JuKjl5UkED6kspJ95gQqJOAChHy9fIiESFf6hGFlNQccXlilJYdjk7qh3bD1KUsqQIvyJAnZ_Y_2F0nmxz4aucLKUfJsnoiMFeIw-R_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=pCcWuybDih-Kv57T3tIYbk7D_NCbUzAsWW2NmAu6wRXhjkrZDcrVgmUZzs_9sywvkE0URMNUapWWYvBjCVoES1i6OGlXuPfWau5CkoxFBXnNtc9jlFsHzr6WQXLHYRszD1VjVjj-bg_aMIMcQbsDMYfHfQQRiV3oz5iICpjTv6Tztr4AKeqL1eOmD0loAjzthtlJSBV6p6x6eMiO6rHmRRmoaauVRMkrV6aWMcJiUF2ZM_JuKjl5UkED6kspJ95gQqJOAChHy9fIiESFf6hGFlNQccXlilJYdjk7qh3bD1KUsqQIvyJAnZ_Y_2F0nmxz4aucLKUfJsnoiMFeIw-R_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=Bir1RF_F0er2ABTbHWll0Y1vh9L1-AwBhZ-pH4o02bbUIf4EOTq8ZAjuO4oAcUHZwBj92xGdkT-TScPg5mmS9FJNJiGg5ldbvtmHAuutFXqNyFKI4fSkkpzBEIzBbWvh2glHUJsJQpdAtErZpZfIMU69mk4v-Wpb8yV658pQGyw4KzLwQDN3IYCo3rV-Rnz-zp2V5alGebXEKDxVAukhfCOKL3qFZQ58uhsMv_GrhS1WgcpCj_yBOaXguypO-uaXIG7jGGK_eOAmZzTuZb7cC8D-QKAB7va-QwpFXV96zZvJTWFFpXhKKeC8T6lepVrB-w-wm8v2QUzwQ759inLBVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=Bir1RF_F0er2ABTbHWll0Y1vh9L1-AwBhZ-pH4o02bbUIf4EOTq8ZAjuO4oAcUHZwBj92xGdkT-TScPg5mmS9FJNJiGg5ldbvtmHAuutFXqNyFKI4fSkkpzBEIzBbWvh2glHUJsJQpdAtErZpZfIMU69mk4v-Wpb8yV658pQGyw4KzLwQDN3IYCo3rV-Rnz-zp2V5alGebXEKDxVAukhfCOKL3qFZQ58uhsMv_GrhS1WgcpCj_yBOaXguypO-uaXIG7jGGK_eOAmZzTuZb7cC8D-QKAB7va-QwpFXV96zZvJTWFFpXhKKeC8T6lepVrB-w-wm8v2QUzwQ759inLBVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Seoz-zagGysXCRX6_6PsE8Eq7F5lsEW8T4K5FrpCkHd0YI8BKJBdJ6n5mtVrgsPBtiPNYHoKYJylGk18b_jSVUULONb7sRW2415L6-iheBm0ijRrhjXAYBjnXShZMHDzyGh0crF7yoMI271WLbjJx73jbjw1tay3CM1-sxJEcRut5rtpDfsDpaQk1MPGJ3Hs3ipkS8jcxXvdRDqV9XV0Zq7zoIv4Q-J_kNZzdlsvPxtWvSVx7vGsB3l3bdOJ7slVe-4Gh1MIfAQEKPvgcfl1apTyHtQcOlmpxqsG58hCeP4BFjrHhszmjCfw9Ng_q1d1cS971MYUsDEircyM_jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=HHnW2GnMdFFKADNT37nwCAh_v_whj26qDw0yZkJQKxDRxSMFACwmAnRgssSKoncT82-0N3PPaGpNs8kQgjml9NGTTftSLWuxIEUki9JTdIJri6piomQLmo0URpQzVjoZ6P7GlnRRLkpthS6tGNmvx4mIgzpVGdvJEH4F7lYVii0zVfMGFYRbOn1u3AS-Vf_GO0WvFR2ZtldK1jyYdZ4kx7DDXU4ido9ZpqOM0zzGaZw9b8C3MLDWxtO1TUsyEq9bJG7jAxKv-TreIrk_uNEgEoZLo8VP68NqmqwSt62BD20rAwzd85ZY0cZ_kmFRC2_CSEJkIQD1voPOPDsF-F7UQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=HHnW2GnMdFFKADNT37nwCAh_v_whj26qDw0yZkJQKxDRxSMFACwmAnRgssSKoncT82-0N3PPaGpNs8kQgjml9NGTTftSLWuxIEUki9JTdIJri6piomQLmo0URpQzVjoZ6P7GlnRRLkpthS6tGNmvx4mIgzpVGdvJEH4F7lYVii0zVfMGFYRbOn1u3AS-Vf_GO0WvFR2ZtldK1jyYdZ4kx7DDXU4ido9ZpqOM0zzGaZw9b8C3MLDWxtO1TUsyEq9bJG7jAxKv-TreIrk_uNEgEoZLo8VP68NqmqwSt62BD20rAwzd85ZY0cZ_kmFRC2_CSEJkIQD1voPOPDsF-F7UQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsWZS2ATn4DaM96D8-Uo8THn6gER31bhFjIUA0k3CjpohxWKpGpWtHWfbv6JvbkhI9Q47va0h6VU0280XAaIhia9gU0WPj6SuKw2Uz0whchu5AksUi17F5zOOqJESRZ6DR7qcfIEZxwa_M6O_ifVetBAHOwMlAh17XYq4MkiNbBHKnVP2QXYgEU6dWuYk3CbJnfImCgbR_rudIEXaf1vxE8AIt01W0xwgT01_tgeeSX36UQHnl0VoJKaicaf9Lgqsg4L58cZi4QcV2dTplL5SWGClEJJCgQGT3ez5had6Y3h5Gd0jK5v5RASiUS6aaUFQ2UN81nJd9CS3fcj4QfRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXi_K6Et9Fc_0whXPquocVAhVgvQRL8RBR9g_01vhk-0ATbMiiJQpA8Cuu8GAINSy4mT414moStFPfGLiQdfEEN_mQdBZyOCL4s1dxep1DbTrEk1UgTViAFD4PRgLbVlymx1rrh5FEueckTzGDyobukqyV_qyyirkk4SxaxEJ1TjJZfJwltxeR3aN4Vp-7jdMqy5mSl5mpcYV-niRaY1_Hb1ck5IkhKM32pUXU9NK0Y27-Ffy4EVWjiLT0V5VGrF-mLgqWtwP0l28AFMWW8PY9gMN2WL1OhbqvkJM9uvjsdpkZt0QJv_hwjuhJ1b0RVmd0Y9-YD7-Ex1w2H0uvUyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QhyVZcA-SDgPka02oeSYhkh65as0wzXhcjStBt679gqorpCxX5VdK1Xm-olqgtMUDG8xPQrUVeSjo9aGhstcpxs9U3Rt6NybruJ0KO6h2jRzUu3Lc1AvC6kTsYVR4zOfq85iDc3AJ-dp_LI6v8SAod-CEuqfguBf2c176P1eyIjmYGSSBvJSP-iQuRaMmBd-9iGUkOTfzAxhPLbbUv-Q37lX05b1-a-TI0RVri8K6zTzEEKCsRhr1UB7KJjoxlg90wDz-htKMsKbYjksjGKw_edqVR017MfE0bCxWPMU5qmYlePWrJRokxVurLwbD5vbOvlD6IChRZOGDhFAsx36dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXtVFXfUbHoLgX8_g-63jgRqbBCD_VrlV3bI65P97yC_ARk2vL4KLFgyrYt4zsr8Z3WTpCOVpfPcx5bdW5Geh5BeNvpxyu7K7ujNUbC4iet2eHy4QvdJBbFbiBBPH-42zinC0tDsjI4EfK9EBFU2uKdrb026GAHtrt5olQb7rfD0Ec9VVzNUZu6J5m7AyOVYNfhE3i9ffdciCh2F7Te9G8Tz1Q6DEQbYWSr-VcfiYn8d-OpA0P6a_7ZUqWp33f73f1vQPvvtZcRWgfaDsMdWCfkiRDYAuHhMaFi_AwLhFKF6Dg6FqIVJoiYpFcacatuSlfNGdgOiAZYr0Ypbgq3Kgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nj29HYYTGy1_8ylT0kTMJCuo0bNS12YiJ0cM5hQ0wE_-JKiR97ld3I7It09h5dBR_XJzeBOos5yeS3oYV1rxuLtfCPXNp1XLvTy-lJcC_eSTtdCyYYMmnP1txhZztBfdMe8tMiqCBt7MJhiZqMM1O_mq-jcS-IeA9rZeJwez1Mrg4Z2tq-P7WYlZXocv9LH0wTBdjYgBvgOTC6gKlA5zW6sF7IHEUSlkQUxpqU21EyTc5nd1wMBIagxkhZJJyyD-nylhAkeWQy2tFLShSpmPX8hbuFmw1xYAcg1Ls5WqAWUqhzV3XfO7N641MNxn3r5Ul5WKUEIuyhKYIzQmtJz_DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتون رفته میخواستید برید
پشت سر خامنه‌ای در قدس نماز بخونید؟
که شما تاریخ خوندید نه؟
تاریخ جمال عبدالناصر و صدام و قذافی و بشار اسد رو لابد خونده بودید
که همین هوس‌ها رو داشتن!!!
و به همین نتایج هم رسیدن!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5219" target="_blank">📅 18:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5216">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKodEUC8H3XCuAXumRJ9DbkygwaAM9Ez59ax34Y2WK-9FtPaE6Y8EDnBZj8J4sDgX_iqxlIO56mVTZXSNBZbmdu_cTGnm7Rqlkt5_nn9ZB4HjZxLpuA2Bgnz8S3BWqjJushpKoeNjZ0p2Gz_gB_KvdxCPaQDAJctRQezFPAxRjzzLJhIrLUuursHrpgGxWL1CpfUm5MNqtw3nRrC52htlOjkhdkuP3nxdGVKMjDxDkqF4qfGlLozpgWaiWtGChcj6Uek0nb_73qXXpN50sa8wPhxB9kA8W4XC-5y84mIX_Tto-sIuxM3yESJW3FWTttoi4ND0lV51VO_U2YP0MkuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uCXzcL6o5pzv_vttpzN7XNyrRBVaaHdRzZq_43XdUzJ7xA0-I8vA7yGTvlIDQ_vuDBSi7lzuw7x1gtcN-NLPS5ScigAhrrMHzqWv5dGwyRU5uMToYDRNPUAcnyP0pRKgByA83px5QK7h2LPBCaROXtP9CUM1JTH_6dlf1f12_FjebyyGT0b5EimasqlZN8hElghm8ZNRiU-lx9weLPblkLL2ksQWUEQ8VsvQORmGEL6V1Oqi0YnJrx2-LMJtHsGgybYncrNEnTTOl6JazcWsM3hiweRAyLrrDPwJXU-EfbrY5weMEeu5ne7QzYRsqGkV-R8gmB1jmsE1uAd2i105pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZLQuBH09Ek6lRRymdDrhmTHRWJVknY156JDyA_VLOmMSrcwUgcIoXSPLjCZUbIKH4yfU3k_1ZMUNtKklrscn_PA66ZFci2je6_pHzg3L1jT0BXWrOqJ6SmXoKp2-oL4k-Y-fUkkxFW1ukWlcnzcK9f3Q07ecFtAsDPo4mymS-JO2wUCh2OhJRI4rwd7SqDgOpgpyqrh20zVu0DTGlylmyhxsorwbza-5Dc4ope1RnMt9WRiKS51cBxenoIe8GX71rCvmgDK74fFuUgwB6GyJ_TTcvCu2q1UNHa5UhwlPW2OgYsrrLsaXse6x6DkdWKL1N3eo4DQfS-RQqOZEJpiNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=IdIj42tx5-6CONk_b4iuJCX0elSXTk7_sA0unyqjd7Rv9TJ2YJWYeYuCCiGB-dzXwmg4E4kftAK5Q-IG6UrXtZ1FCTIlIf9fqWqVaqiDTXpiN0Z67xFoEfcm-Usf1hSLLepwXPyzXjUa68ArATWnJujfgBPnM95Mpm43x2LyxRfqdOZNMpWUaE7wRUWTNVEoAZXXuUFsoXpBFS7pWJ1jQsjjrk4pVBVZ8fOV7Zk0uNLk4R5crxEObpoVIIUruWiD1Ra2IVOMl5L_1rl0-L-3WkKfzWXo_gREaDo0KSxa-MBYk2o7G5vx7Kf7Rj0PIojAX38au3V13LHpD0KP06QZkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=IdIj42tx5-6CONk_b4iuJCX0elSXTk7_sA0unyqjd7Rv9TJ2YJWYeYuCCiGB-dzXwmg4E4kftAK5Q-IG6UrXtZ1FCTIlIf9fqWqVaqiDTXpiN0Z67xFoEfcm-Usf1hSLLepwXPyzXjUa68ArATWnJujfgBPnM95Mpm43x2LyxRfqdOZNMpWUaE7wRUWTNVEoAZXXuUFsoXpBFS7pWJ1jQsjjrk4pVBVZ8fOV7Zk0uNLk4R5crxEObpoVIIUruWiD1Ra2IVOMl5L_1rl0-L-3WkKfzWXo_gREaDo0KSxa-MBYk2o7G5vx7Kf7Rj0PIojAX38au3V13LHpD0KP06QZkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=GIKky68rpyv5QMJmjU8HY9uy2TrksyCYLXSwE1RkBnICKZcvh0TdYK5pnAJi_7sANriClHxPRDmlzdrrsSEV5wQwqEy0J4EATifvhzei6xp0ZJap5R_HgXJ_YtIw7JSxgqByIJlNJbZOtPC8XRJ3Y8gHdNDe613AAAJm4F8z6JplMclFwMbNBfeibCtXMvr5pNB2AA3ecIkJKqIupJoOcBwDBZ1MQ4QDXeE9aT64WleyRrfDUWh9Jj4tp9xQg6S90I2TZXBES80miO5UVDnjHd08lu4XHSrBLEEjCMi7IooDdTwXxGHJFQbU0FG2pVuos1FZX-5re3PxH8IV-8g3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=GIKky68rpyv5QMJmjU8HY9uy2TrksyCYLXSwE1RkBnICKZcvh0TdYK5pnAJi_7sANriClHxPRDmlzdrrsSEV5wQwqEy0J4EATifvhzei6xp0ZJap5R_HgXJ_YtIw7JSxgqByIJlNJbZOtPC8XRJ3Y8gHdNDe613AAAJm4F8z6JplMclFwMbNBfeibCtXMvr5pNB2AA3ecIkJKqIupJoOcBwDBZ1MQ4QDXeE9aT64WleyRrfDUWh9Jj4tp9xQg6S90I2TZXBES80miO5UVDnjHd08lu4XHSrBLEEjCMi7IooDdTwXxGHJFQbU0FG2pVuos1FZX-5re3PxH8IV-8g3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=UjCelDoCf1xAQu2A9Zk8kJZKUpaYRwGSEOa4oKG_BahiU9I1T0I4pF-3vbTROkFDEw7Mb_UwG09JJwQ_VoowIwP1SW2_Znb242L6xfRw6s6_nrRMp0e0xgDaiTiJ0uRfEZuiPRub35EBij0pSK2cj2U5SvIaUrCfMYZR8yKiAUfCW4nXokiJ4EBd3NQJGXelkEyrNZqBPhimk1drrk83Wj1eAepP72dGaiCcjfpKEVfu9ptpt2k5Gh9ZjVXT5AlXLJn0MNDD1oiVYGLhLXEhphBpEN506-scUgp5YMQu9js1XJlFLoFk53j9Z9Pd2RyS8hLfXHd9_lauGFSmsGzLAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=UjCelDoCf1xAQu2A9Zk8kJZKUpaYRwGSEOa4oKG_BahiU9I1T0I4pF-3vbTROkFDEw7Mb_UwG09JJwQ_VoowIwP1SW2_Znb242L6xfRw6s6_nrRMp0e0xgDaiTiJ0uRfEZuiPRub35EBij0pSK2cj2U5SvIaUrCfMYZR8yKiAUfCW4nXokiJ4EBd3NQJGXelkEyrNZqBPhimk1drrk83Wj1eAepP72dGaiCcjfpKEVfu9ptpt2k5Gh9ZjVXT5AlXLJn0MNDD1oiVYGLhLXEhphBpEN506-scUgp5YMQu9js1XJlFLoFk53j9Z9Pd2RyS8hLfXHd9_lauGFSmsGzLAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdEytbGViOnRPfYESnWLrguOQl_1JM7sH0k5sEGHF_-GQVvKBQ8UmcDY2RBU7kJTvyN1nVdDalxyEJLSgx9h6KShqj_9ocdR2UZk9UloNEzHMzZRD78hwhUbXWTK43dV7S37c1mOe1DaceScAWajXA7cFEnLtWhLBj8r_SMIGZy18X4R2f0wrmoL9_1a3uLaKP2dCukNmF4h88ERYVMHtFDauaSJ0mxtHrGzPjEHytljWh8cJ3puTcMzDyFnoiV23uvu7yNcxU7obIThvlbdZGbBWP6diCYt3pMQceUP2glN1LXxczDzLX_WRyBvob3ICkiExm3NE7K4IRBPcpvVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXYXuifR1FExUTQwghoBDmt7EgXRzrSG_gz-gHtf810FwU_oSXSY1M-fLXeeAuPLLkOhM84MNQ9zcIilg95NHGY9W02Z35an7BrxPbTS7tj8kLpa_xQzIZGb4u0QA16rcHrTKgicaEv8APTfijsET32sC5LHp7rNoIQHFFZzPLHsQkVHFFWxv7QhdraC_67mUfl0MXxtDGxxfr_JuKlKKoFqGptC15ONYTlE0fpmhqqey398vdhfF1KZjJAivzMfF4m9dS5uyku6qkLNZTJ4wIvgDdzqrjRyszFQtjhK72BT2VXa_fNwwaUNyOdjVabF7qF-Oh0vF8wfGnmIh6eCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ  ۴۰ روزه به خاطر ایران اینترنشال بود و‌ دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های
ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های
جمهوری اسلامی  و ۴۷ سال آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات
هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات سر اینهاست!
خوش به حال  آخوند که چون شمایانی رو داره!
هر بلایی که سرتون ببره،
آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی
و کره شمالی رو نمی‌رفتید! راه صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAIPUGH0-TGYhlumuVKSzqCfevgP_h5SEtRyQyOgAIU3irtAHw8ms9ehm0PLqXYycCwA3RJUXyLFhpROVhEgYaq0CFj-AXVGUU_pgpFCJAtMciXE5waRQE5Kq1yDgx8oNATBivC3wgkA2LJYOF_QbxrPewHFTCiEGNcxAWsO2XCe8eDf06I04B84CU9EPPLM6yh05bDS-6dv89ifxtdpvTJJSAsY1lIpBTFPY4w1yjRlhBXCzNmhuvte6bYWzwoIM2wD-YBB11EPtoPCAA5kuzcSYWzxRkA_v3NzyxLIHILrBDoDKVWDvzKQB9w6kDPCiidCVnLIa2i3NN1MrqZ7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyyF9_nGv6iKbIFvyWkzB0OZVL6bypL4m6jRHs_HzBDsJlgLqsn5CQLp7MLzEXsCru4CalSpMH4Iu4QFlKlSuTy6YwhHIFYRExZt2dPGFAjeskD6FNPMW2i9yWSs9VQ403WcYWbmYx7ycXRtu42GTQNh73MvOlL_4uMRsGdw7icd1pXk68AzM6I28xXjwclAY2FGKBvXS2wryD0qL3tB286w-CVwULNAe9fo2ek4nInrDQf6xxdfCywAvadSP_N9ToMXWhAhAtTfoW-ekjc8-J4F5b7j6EQW4cXzGmQSaxGyCsgcDiOkZh95nVarmZFLQ4qJ-O9mVx0jrXeZH1DUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=J_KHQFJnehzKBsQseB_RRyLSzdkJHMFeV6ud7wa2-ycFfIwxk5gkg2raSjtLZOY71F36Prx_MAh83Xp64gY8lLfJU_XNFEPEdBMmIa7fkgh96NHXa935rDa6XgvtxCye9eVexQXzf8NjP7Gg_SFOVj52FpJ10aIs-jSWC8lyE-o6LaM1NUamMZfer-B7ZX61Ut9wdrTAXv_tJAduZ8tpt3kifynhu_dpGpqvYzXLhHcTBx56vazj7IY3qx9nDY6Jnq_DWGaAehLhBoYFzwt8R8xMCj0PeCebIp_dSP1ALqjDizV79LB4QfFZFUykZOyBSKd2uZ8oadEQA652_F9_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=J_KHQFJnehzKBsQseB_RRyLSzdkJHMFeV6ud7wa2-ycFfIwxk5gkg2raSjtLZOY71F36Prx_MAh83Xp64gY8lLfJU_XNFEPEdBMmIa7fkgh96NHXa935rDa6XgvtxCye9eVexQXzf8NjP7Gg_SFOVj52FpJ10aIs-jSWC8lyE-o6LaM1NUamMZfer-B7ZX61Ut9wdrTAXv_tJAduZ8tpt3kifynhu_dpGpqvYzXLhHcTBx56vazj7IY3qx9nDY6Jnq_DWGaAehLhBoYFzwt8R8xMCj0PeCebIp_dSP1ALqjDizV79LB4QfFZFUykZOyBSKd2uZ8oadEQA652_F9_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=jv_vrgoBj6SxKzEuepAMCNMNJHBgAsGTneWBOCInk-aardlJJVwhJwLbFsEkDKgR6foLo8-88EjPujg5qvE63YQr1gDMeoj_TBEBNzwEX_UB1PTHJfKU78O5jRX0xhaN-yUhRbJAzdcK10nIIWBFuHqcjkKKKdSFdbJHvn5am2jtNc08anUy0NzZICxDqCHTp1B2DbccTQtF4jTvJjWOljj4Dy8Ce5mDwnWt_aylkv0C9R3t0bsaYf8xfcQQrsEM14nl89-xrBglbCl_RYJiZ4s6h5b0drpKnCS_Lr5Ux7kBgwA6iKaptdDXZbhFJX5r3XDiIACqkSXjbJ8sZphNIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=jv_vrgoBj6SxKzEuepAMCNMNJHBgAsGTneWBOCInk-aardlJJVwhJwLbFsEkDKgR6foLo8-88EjPujg5qvE63YQr1gDMeoj_TBEBNzwEX_UB1PTHJfKU78O5jRX0xhaN-yUhRbJAzdcK10nIIWBFuHqcjkKKKdSFdbJHvn5am2jtNc08anUy0NzZICxDqCHTp1B2DbccTQtF4jTvJjWOljj4Dy8Ce5mDwnWt_aylkv0C9R3t0bsaYf8xfcQQrsEM14nl89-xrBglbCl_RYJiZ4s6h5b0drpKnCS_Lr5Ux7kBgwA6iKaptdDXZbhFJX5r3XDiIACqkSXjbJ8sZphNIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xxxr5cBw6oRLamZ_vBnFVZw1BIzcWgm4SPMR1vo0kh58cX8m_vIvQ-DKg-Pa4HNaZCzBQnCkdkFs9chxhfEM9Z0naGtM1VwHwLgj09xVgX7b8Af_FzS1eAp8wSSYBEro5ZjBkMLYlBfWgSLscIRnYYDnkds4BtWbcVntqiqDCzYy-ieJdkGvYGXqJvEakOt8DSPxLbMdyfZwqQGStb7_Uz1cz5kIpmH0n0ftPod9Zw38dROgT_pCO9oe3uO_UQMHld69gVlfDUlrYGAzHgN9CT_hzzfkPRJT-CcIA-r7lRDGqL0lI0KOvQJLxGHtEYQ0g4vevrSCfQL7KYRsNTkCvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brl1RGTwry0x-90AdhcZ1G8kh4Xz47t_OhoImKqkm7cHHtQF6cg3UTeJnXkB98_dM5I8OFvnakXIDsiTvbfhQXRo8tJ7CI81S1fGK564ra0e1A75mfsm8Uj45l41XCtgbp02mBN0wMog5MsTScTQZpEYXNaOQqzhQs84ZwqizofTt5Moijv3wUOjnJ8N0YVm0hVUVndPymVW4V0u0oL_o1ODGoToZwao1_XPU0Noko4iGljekXlLHKINdYlIKK6Mc1SpkmIq_YOBrUpiUCfe_CWqUEcVIhV29M5egFu6KE3i51jWOj62RMsrul4x0DBfpBdYzXM2k9_LNVaHqwrc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgrlZhs41mgusPlVB-UdRo-OGa69Yyuf12StfzsQs5hXiHKAr9G0nI1tiFJWlNBZTYbnJ_u-hDxb5--8cMOljcDu0d5Iwhv38WGowW6MSiwxPY5g3AXDA9ysbEBMIkGD9qvItHbPT6W6eNBA74GqhkwdXomm8LFr5Mq1KT05AAn7IY2stR4lQmgyTDSpSooSrzf4W4xqTX88ezHHV4Xqv-DvjeHa52Lvpx5fykbnwvP2ADA9Zo3VCWtslJbQBcnxoteb3woDm7GNxtfa5rX47slzbh8GCKVnnrEORyAON-qh8hvNYCVbw078GHCs4ZyZnWXL7aAw0gDuaVA_VRMtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eISvFjR3HlSVlPjN0kU1aOw9B8lT865HvRfdJs8WQGyvVGNDQKfmxxfia4Ie0RylwwSpxIukQ4jTF3H66Eg_yNoahHRayEccNBJqHhvCnmp1tulvYU_iPq96IHypuEBIgg7w1QP9Q6Xj29tjq2-zqeD94DqeH71t8PiqUCiPBnf8fKaCAD6nhnYs8s5AX7B6DumPa46EUEv7cmvxGcYpBig7hp5Fk35yCCI4FwQOKOMhk7b1RNzoJH7xW4sCoGy9G5Pf-nbvhEsuy7aFdROJeMlfdr_Th027pymdKxZR1zy4AFcpIadKObVNFapjHFrCtJ8djNZacFJ2mRwEkU1mfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXBvZ8nRfU06eFpSekoYq2jNVfjusN6URgJFjJD6NdRogbxVRcSeHwWzBdqh8mZDGQRl4xWsouayg4ytvE0PZkd0apQPCHRrWCWpPbtcv70ttJP9cAVXtt9BKMoU2C6MPIE7QQFV_3xzMmW2KsyBt-pjv201_SW2ib6YwrsyAv8UFGnvpsxM2sksDB8PTxEvRPuzqW2fo0Kd9Tf_pnQ0XRgTj7cbNmmQZGKriy5_6qJfm9m4rtHajzjUxriEgnCAgY9i7PtgcnLrWR6nZrltW8BX9IG3aPbn9o4VYHjBt-S1SYGP3HZqfKgpMNGHtOZ0YdYg7MP_a3WrSMZpHJOp9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIgyPoHrp9tbXr3Qhzs_JUdWazwL803pXI6rzPiZwBiulHRQ-INShe8MmUxRWxvTqWYkORDfIOqTh2ybFTDKrFtxypqODhuhQfvy_whoA83I0AFyGYJEEosATBpYVf2R29qwCB1VYlpXiuT2Ct52Yicsn0UU_PMZl04ZrasD3Uy6GWmIWnOhUrpabRsQkicOpyY6gANN_mHvo2bkxGA7LMitrGgI2bmhuMefpHQ-FPEG0FOl-aFbgpa1nrh8A68t2vGRi40NDxlhtimmyRhcaK4qV965by938exP9H_FTvaXX0AUgzJWLZAosxLQgcLznQE-9nik7VhAS3VlLbWXEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egDgncMbVbfgEmuemBz_t4N2o52zY28bJ-2HWv3mQq3LWAY4a16oUSk-2Zh958FxZG5HKy9or5kQ9bBuzexjjwfx1p6soR3yStR1A8cb2DR-2APuk5TH7Hup0HwEJ-DrwV8xL5pOCH-5AkJGaq4fJMKjkEtQoSX_OKdp90EZeiKt4YNIh_s4HltlOomwCPCXcoW1N0wP1685lRL26ESq-lnQ8eLvWrhNipDUGn1c4W3JBQ89DJyL8d7TOsoEeyxKy7YEuklfu7cUMD3MtuukdQ3MxFB3CT-WEKsg7WYCNeL4sjJG2_J0el00ser0RulwYUPxU9WR__rBuIm6XRCdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2smPZJ8kmBS3HDmg1q9712SMPElZhNyicoEhE04MQS5CX-cqAKFkeo2jcICLBpgETJ06tx5FSO9kKsBo3NlsCzp5HYCaWSRVWVZ2oTOCRD3PfQt64-VfwB2qJ5285DI7B-asnYhQhPsoc4SJSAvjNWOam0j3coy3ZyzawQBAikiwpXfCYgD_kagM3Ohkkogs09fVE4U4auOlSH5sKB3eepq_qnZK-yg338ykY3cYLSYuLFcADOj16udGLleaX6hH5nu0XXmEjlDN-bja2ccb5Vt7n2pvuj3OL6NVwxOg2TuJjw6VVCLTluboewuyS2mxn4bYaO5GPA9ilFOqF8O7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=jiChoSwUjUu1M79cIMT8DiwJkUr8vyYjsEHZxFIKN7lckAq7NCpeUnQz70SAW9svAhPuCGxIuHHJ9fzTsF8KGPo4DN29BQRSCS83KjrTs7_cv9pw7u9PCN59P63OHiIKMoX4BNTuZbEwDDRlf8y_XXE9rDWnLF1gpSMZRC1JRl7d40clWZBxpNsGENdj5OCl6zUQFqjPM9B5x2jqer_xBDhpfo790xz5vEbuh6MldFwWtt2hmsVNxvc-kyJzXjONL77TxW8sdJIvln0tF1C-CCTUpWy4McazUjLoBytMuOUd2b4fw729BITlCXxYzk1mwXUuN9PEpot6_8IHNmHEDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=jiChoSwUjUu1M79cIMT8DiwJkUr8vyYjsEHZxFIKN7lckAq7NCpeUnQz70SAW9svAhPuCGxIuHHJ9fzTsF8KGPo4DN29BQRSCS83KjrTs7_cv9pw7u9PCN59P63OHiIKMoX4BNTuZbEwDDRlf8y_XXE9rDWnLF1gpSMZRC1JRl7d40clWZBxpNsGENdj5OCl6zUQFqjPM9B5x2jqer_xBDhpfo790xz5vEbuh6MldFwWtt2hmsVNxvc-kyJzXjONL77TxW8sdJIvln0tF1C-CCTUpWy4McazUjLoBytMuOUd2b4fw729BITlCXxYzk1mwXUuN9PEpot6_8IHNmHEDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=IGyPQJieT2EfJspVK8KFTQdcOtRvGdzPNTzUB2Av-8qxJ0aNtxWU5CaIFJpa6Xwj6UcWVoSg6wJKKnX7fm1nsv41xpdYpQHIt84cxGv2n0Y_WbHMwX1TMvIMI-bU0rH1XEFNrAzlxphlFx-cOE_6R1Vk1bHIy9xjrBHZzmUoZKOr1rvxG8MG3qmy-f3kHBpATl29bD5biRhlVlyAMQRUvj-QZV_oAduCfr1dISeHGWT0naRZtZK6k7m0hbPJkfwXVLxv2tQBZaVPfxR_gNYpiJ0KXyk0N2kXh_Qll0Br7Fp7acOp_CFgS3cXO-PnRvJkYLSFVA67i8ynfNJ7vd4EeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=IGyPQJieT2EfJspVK8KFTQdcOtRvGdzPNTzUB2Av-8qxJ0aNtxWU5CaIFJpa6Xwj6UcWVoSg6wJKKnX7fm1nsv41xpdYpQHIt84cxGv2n0Y_WbHMwX1TMvIMI-bU0rH1XEFNrAzlxphlFx-cOE_6R1Vk1bHIy9xjrBHZzmUoZKOr1rvxG8MG3qmy-f3kHBpATl29bD5biRhlVlyAMQRUvj-QZV_oAduCfr1dISeHGWT0naRZtZK6k7m0hbPJkfwXVLxv2tQBZaVPfxR_gNYpiJ0KXyk0N2kXh_Qll0Br7Fp7acOp_CFgS3cXO-PnRvJkYLSFVA67i8ynfNJ7vd4EeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ttdy-zIxvdAZZsPQ28W5ZYc8-AGSCUffkS7OjzfJfxfQLoo5FpSiZIbwJjNYIB_7ruAFURfogpFXgnLiRCjnELtPMy-BWJgxyifg1Gm5qyBSVLkTKBBsm3JGakX-iZc3AuHiVGWoGcS44-7UcUBmrVsMYHnOUsv-Ln4kayaqh3DHNKTb785y27IKDVBPinF8Z4E1y6s_rvaoxwRabNDwNCvxzZ6W1P1PDdKZ2mgHjUX7-hClZgrUKK7BSmEdhHGLi8jqqpSmvTkabyfW2wJnreg0xQOaXzFBJ1PKznVSZPtw3i3UopgtFz0u8rYgVsL1PS5ojlfWuH7NheZu4PskeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWro0d0t8AuG6Um_kmRtsW_wETD1JwtQM_JLorSYcSxRar3std_W45DyAJmHFkSrvKQQl8QbWGCqIbYZmG6u3Qa47zBmRLLD8Tpjte5o4UeQIof-WUZV2oGs2VlxnTPJhelg0uNzvdAAEb5c5QeTUvhr7zaBVEWCSeMHL00G7jKz_rjq2ieycIUivESDdjvTI-6L5kmOUolBI-IqS4JpTueDJW3QiJ7zDieK8kx-ijid7hHpXAyhOryyOmUQ0y4nPccyrpieraHqEI4OC5tqRqK3t9Oq8YpdL-SpzxStnPagcvupZm_Xw6-4pJN-3Qu0amLNhAP5kH9Yk9fYHZ6fpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=hg5oMMD3MnoS72wsCJ7LlgY9wh8_RMRdLsuullkySHeNlYroX2AD_bjAbDl7JsCO7oOPzcJdqZ_OiilXLgI_B-ufP1K32zzFoyjLcmsZiWMwxBrn7XL3uZw7yfWHDvY0iAmGpDeyvBWYyGRGjDTaujLQqPN0egzj9mYQj6G_MKsSGrwxgClinKx5HPusbCQDtjqqMM_pu7pVAeJT93_g1SwJLpCfivw3t82nYxOVcQflYmGsZrTyT9PBdUQ_211NqtV1FseHdbIdV7ud1ZkvyX5pQapuJZCKZkB4BykNBHOZ1CF5GmfBnQ8ti3hQ_Ji-iKJ75EE8VnJFAAssTCy-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=hg5oMMD3MnoS72wsCJ7LlgY9wh8_RMRdLsuullkySHeNlYroX2AD_bjAbDl7JsCO7oOPzcJdqZ_OiilXLgI_B-ufP1K32zzFoyjLcmsZiWMwxBrn7XL3uZw7yfWHDvY0iAmGpDeyvBWYyGRGjDTaujLQqPN0egzj9mYQj6G_MKsSGrwxgClinKx5HPusbCQDtjqqMM_pu7pVAeJT93_g1SwJLpCfivw3t82nYxOVcQflYmGsZrTyT9PBdUQ_211NqtV1FseHdbIdV7ud1ZkvyX5pQapuJZCKZkB4BykNBHOZ1CF5GmfBnQ8ti3hQ_Ji-iKJ75EE8VnJFAAssTCy-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbqmKRHQhYjGr0S6BhyXW8lCnHcy0q1f1-zJnI0WClNaNI2KANt-vxG0n7s4jwqihE0Hi0qUzDMYUX-WPIGEljz_cNIZcwcnRtYohyaKTV7hVMTH9MwOSplOT_eucAKEBISDlVQEGMAzl-7iUvvceHoxHAeC8PxKQYYRD6VH2x1MyINvky9cE-x796itF0oAnCPli7tvHkCSWc-ZkNUOUVMf0C5YpMJeoNu6e1GrQ9KzneZkpiTAqpxBjQ4abkn-TGZ4vKAtpy3Kxfokf_KfHe67UxsSIGsIM8rVshlQk0bZjTSx7d9AT8DjXI_wlUndBUWPzNStD7VuaNZj5VBL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=TczgkRtGyER2ucaGGOByglWNO--CdHDULFZbtMFxv6cGX_tTR-cyPLKyPfCScbFY7vCP9_JWHEwtmWe8UniicaiZU8WjyKcTobGJJWgbW0jQD9_tz_-0d_kQFmDnI6eLb8oJ2M1Iu1WqTGRbCzxHOQt8Bj91mk1BoKHv4iMtlFG4OgHPqwqaQwMRneiWgMgltJ_fMG00Shb8Tqi-oFV_l8L9iAanaKHJkRPe78y1vKIDdv8__H67Pz0XhXext57TWU2h5k_Nf9JH850VOBU3NZlMS4JoNF2i2UpqndH1vU_MxeVWKkujGL_Hg2ZoVtVN6sAzGKtZoOGXJbFwtNm3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=TczgkRtGyER2ucaGGOByglWNO--CdHDULFZbtMFxv6cGX_tTR-cyPLKyPfCScbFY7vCP9_JWHEwtmWe8UniicaiZU8WjyKcTobGJJWgbW0jQD9_tz_-0d_kQFmDnI6eLb8oJ2M1Iu1WqTGRbCzxHOQt8Bj91mk1BoKHv4iMtlFG4OgHPqwqaQwMRneiWgMgltJ_fMG00Shb8Tqi-oFV_l8L9iAanaKHJkRPe78y1vKIDdv8__H67Pz0XhXext57TWU2h5k_Nf9JH850VOBU3NZlMS4JoNF2i2UpqndH1vU_MxeVWKkujGL_Hg2ZoVtVN6sAzGKtZoOGXJbFwtNm3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=FGcXuf00DnjHrCMj9I_81r74SnhaB80IuhsgYdfxySjwgZaXD8mbcQC7hWF2MPlI-LHUFQf0OPpks1Iiof8HM0JR7n7dyNvZFFSdcH3xMWawlO4Jn9bLZvrwr6PfcxhJ_K-NiPNyEIen3jhS5E0TdcGTXRkRAuKfK_rmPV6LDbsFxd89yC7bsyTjCgaNrnk973xXkUzMo104IHYTAHhN5NLwwzdukqtN2YkYgb-hipXdRiDdogc5PfbZEDCAODuj5VbAXQHD1ydsbZLswjORTq1uRMVlKrUYgiE_t6WSxKERQLKkiJC0SoqTATbt9stG6TYFcCTDM8UACUcaVDesCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=FGcXuf00DnjHrCMj9I_81r74SnhaB80IuhsgYdfxySjwgZaXD8mbcQC7hWF2MPlI-LHUFQf0OPpks1Iiof8HM0JR7n7dyNvZFFSdcH3xMWawlO4Jn9bLZvrwr6PfcxhJ_K-NiPNyEIen3jhS5E0TdcGTXRkRAuKfK_rmPV6LDbsFxd89yC7bsyTjCgaNrnk973xXkUzMo104IHYTAHhN5NLwwzdukqtN2YkYgb-hipXdRiDdogc5PfbZEDCAODuj5VbAXQHD1ydsbZLswjORTq1uRMVlKrUYgiE_t6WSxKERQLKkiJC0SoqTATbt9stG6TYFcCTDM8UACUcaVDesCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=uvQ7jD8sWCRH50Uo8l7r9hpw_qrU-B58mJDZAVzc2aObw5XsnWWXG5IRzypH9N-ImrK-am4m1BmfYCYkOJqqoJAj6S46-IEMTg7bY0Vj9YoM9JM-SJx-Ogbxn47r-Qdn00ImuEJU-lW5d_UW355j1_HvB7qSQDSHcVlihC_cXXAeY8UBtdhBIeT3l-oZTUvzOFmRbLFk2NUA2kYHOUjN3WtCbqTFdzltgeWyScTzM-c6cyMbULWDWUKUAp4s4Uc9-C7off2Qmo8uZ4yHtN8pLXOhY50ktvkEikJDKPMnDrY68zsWcW9v4IdrOR9PWJNtkZ4OFI_W9ey18ZaQIDyj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=uvQ7jD8sWCRH50Uo8l7r9hpw_qrU-B58mJDZAVzc2aObw5XsnWWXG5IRzypH9N-ImrK-am4m1BmfYCYkOJqqoJAj6S46-IEMTg7bY0Vj9YoM9JM-SJx-Ogbxn47r-Qdn00ImuEJU-lW5d_UW355j1_HvB7qSQDSHcVlihC_cXXAeY8UBtdhBIeT3l-oZTUvzOFmRbLFk2NUA2kYHOUjN3WtCbqTFdzltgeWyScTzM-c6cyMbULWDWUKUAp4s4Uc9-C7off2Qmo8uZ4yHtN8pLXOhY50ktvkEikJDKPMnDrY68zsWcW9v4IdrOR9PWJNtkZ4OFI_W9ey18ZaQIDyj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=XNc8BQYsddGTiqGKpGl0_GMIIK5F_qr_kBBWQznMGlf-MmT3iY2WNQqOXAa2ZM1fZlvDs8XGqpCPZ2hjoWzIWYUgHH4qiRenS-aCjm4ue6ieT08GboJxZ7pWFCR-uy6qWCyUzCfCtPy2Xn34CNVt8z7nLkxPhPADihkkIpxssBmbM9heoJlirCdkJz49m3DOkl7mLJcRktRNwM2ZAnocu7WZesGw12BFXYtRDFKcBhTONPBMlw-4v7WUyWJLt8t27JginUBH9SGsC1W8K-h1ZniojUoy7VPtiBBBUSVxpFln_PxgDwPzOvbFmeJOpPZlw1scIRhGhzJKtEnsSsfEVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=XNc8BQYsddGTiqGKpGl0_GMIIK5F_qr_kBBWQznMGlf-MmT3iY2WNQqOXAa2ZM1fZlvDs8XGqpCPZ2hjoWzIWYUgHH4qiRenS-aCjm4ue6ieT08GboJxZ7pWFCR-uy6qWCyUzCfCtPy2Xn34CNVt8z7nLkxPhPADihkkIpxssBmbM9heoJlirCdkJz49m3DOkl7mLJcRktRNwM2ZAnocu7WZesGw12BFXYtRDFKcBhTONPBMlw-4v7WUyWJLt8t27JginUBH9SGsC1W8K-h1ZniojUoy7VPtiBBBUSVxpFln_PxgDwPzOvbFmeJOpPZlw1scIRhGhzJKtEnsSsfEVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=sOj0WzWHhfBF8q-EFZIUgHvnuCKOYqyh4RoXBX9DKskzw4IzpI_XBkBWdUiK5YcioAf83Oo0lyXe6jF7RqILTGWBnExWFDvbil7woEPrXNfiqL3HWFT7LZNm_Nj1enC6m6XlEoTwDacGuuej3_nMN7giKE5Cqxe0kFhn8ckSd_dUIF6_6BqC99pssK59olk3m07qSDbbwieXvZwboHDnwW-Dm5K5GCey5XypNKKwmz42WS5GjmWeF2KyjJTs0j_1bu9F7IL3C6HRbYeGJk2gCII58JN1HlP2KyC6XWSN0hMQQiJkUXXAjp-7jRCkgsmsFcx_O5BHSsPgZTHvrKjdew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=sOj0WzWHhfBF8q-EFZIUgHvnuCKOYqyh4RoXBX9DKskzw4IzpI_XBkBWdUiK5YcioAf83Oo0lyXe6jF7RqILTGWBnExWFDvbil7woEPrXNfiqL3HWFT7LZNm_Nj1enC6m6XlEoTwDacGuuej3_nMN7giKE5Cqxe0kFhn8ckSd_dUIF6_6BqC99pssK59olk3m07qSDbbwieXvZwboHDnwW-Dm5K5GCey5XypNKKwmz42WS5GjmWeF2KyjJTs0j_1bu9F7IL3C6HRbYeGJk2gCII58JN1HlP2KyC6XWSN0hMQQiJkUXXAjp-7jRCkgsmsFcx_O5BHSsPgZTHvrKjdew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=E4bpC8ThqArHsiLPQbZhT1y2vrzvnBsoUOuL7vFegDOI9nZ9Egtz_OgqiamWXt9NqiIu9t8XVhZsXKdh1yXc-onN5xi1YpqY83QsF56DfYppSHsNJmR6z8Q33XY5XpSZjWv8378NRV-VMcmbOBN_xxvA_ZC356b-veQjvWTZXl2xhkW9V-GOSdzmmNeyysFi-FBVQ-wMZ7Ox0zpuT7uAmHjfjHtWse7Z5-zIynJSU6jstVVuQ4CdKo68w8Z1dSmqNHVUaeDpxrpbDafBKNr3q0Pd1C9YTHM6YWIxRUi7inLbCd5qX7LTcWWkzA07f5niKN538Nc4dSAqVUJ6LfNRAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=E4bpC8ThqArHsiLPQbZhT1y2vrzvnBsoUOuL7vFegDOI9nZ9Egtz_OgqiamWXt9NqiIu9t8XVhZsXKdh1yXc-onN5xi1YpqY83QsF56DfYppSHsNJmR6z8Q33XY5XpSZjWv8378NRV-VMcmbOBN_xxvA_ZC356b-veQjvWTZXl2xhkW9V-GOSdzmmNeyysFi-FBVQ-wMZ7Ox0zpuT7uAmHjfjHtWse7Z5-zIynJSU6jstVVuQ4CdKo68w8Z1dSmqNHVUaeDpxrpbDafBKNr3q0Pd1C9YTHM6YWIxRUi7inLbCd5qX7LTcWWkzA07f5niKN538Nc4dSAqVUJ6LfNRAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO53_d7vjsNwp0TIpVmCVsyQ-Hhg4IpWDeC02ap7xI97SYQkG0F_Skeubg2rLZ6eKJD3yW3DJGjs472UKTjrHHYEydlPLh8734GnbHu71bD6alywmznDMzF6zilbDYaEBaArOA3Hcgb4CoMb1twvH_dXlUfN5-kOUmMSKb7mAUYsoG2bea0JwDvuFyiJViWlfeWqqM3p9_OZjyrcklRxsJD3UlsfOCz4b7FM4u7kN5qNcytWxI-Ccwd7Pw4Cj4OYIwmRt2W5ThiW-lcjPRAP6mbI_mKCMYLTz3Q2bN8pPlzdcGXkbIK8UaJ9kSWSX1ipiINtRDkGwp0ZZZXCWLAFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=r5WcoOrTovw9li2jXDI6A18DOm4p-R4OKzp-2rLNro4aifnLMcRvX7Jd27ERZrjdPdj7fxSiVzVmim-L0yOArjLUjt2lAQywuoMZNCSO0w3T18lGEr9IjXVJ5F4FFOHLyHAwzUyjle7saafi_UDIKFVs9J3mSFRRmD1Y-2UZh-1WwiEcgPTvfrx78h8qq5iuzSGjc8Tz3eIoFLpshLF1lmnqXYnoksM-OUnFWg1fsIp70g_oe_V1oqBXmndMjErtivQQl1bsk-it6X29xTmZxXwcmb9QCI8sTlXn4bJBXygx4n_Lv-jUqhWNka3FEzi-C9Tr0SsFPbjBhfARz7f1YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=r5WcoOrTovw9li2jXDI6A18DOm4p-R4OKzp-2rLNro4aifnLMcRvX7Jd27ERZrjdPdj7fxSiVzVmim-L0yOArjLUjt2lAQywuoMZNCSO0w3T18lGEr9IjXVJ5F4FFOHLyHAwzUyjle7saafi_UDIKFVs9J3mSFRRmD1Y-2UZh-1WwiEcgPTvfrx78h8qq5iuzSGjc8Tz3eIoFLpshLF1lmnqXYnoksM-OUnFWg1fsIp70g_oe_V1oqBXmndMjErtivQQl1bsk-it6X29xTmZxXwcmb9QCI8sTlXn4bJBXygx4n_Lv-jUqhWNka3FEzi-C9Tr0SsFPbjBhfARz7f1YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaoZFhP-c78ZATQVbCFHYgWrEc4jKr9ZDnUdA7Aaq3fSvXA77LpzMdhvOaTFzJn__GfrjVyB6pvmt2f6Kk7NSXR8g80BEHUCwrDYtCcWfrlQlDUwF9cdhWbFwj45g454sCWzvLxlf4u17gAvpsELjHz-DmDEsstz7kKVpxvZ3WiWlzOoGvfnH4_w-dXO_TUoZO1IC6q9h4VtbmCdS8WZFdqfuRfzmTBTOVfNKM8zdQcO-O4Gewy2SxpjDDWgHVvqo-NU5GLCDerm6mtxZVZZ53CH6ChQdscJ1VH_ZT-xznkiVWn6gSZo1nKFK2u__MNmAqOUbwGVafKhy7QHbuh0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=vTYWwiuCjhPSpG38NE8J9_AO9Nq-x5XVRvXAXNXEC76xhvOuT2ByfQK_cg9cfO2aVfdpjqAnT-nmWBhRKFsjRQ1HdNldMCKs2yY2_4x5oYt9ifJPYrBC_ufCjxkI-kbAvJ_bQyGH4t-WHpt1UecCSjmHDMb7IQmFjegudunXq1UD9OoQ1toMskW3R2dUArN_1hmaHZ_QTfqbZsSH54kgC85ONx9yCJocK2j5Bh3-3L8AmsQUSO1YbEuLgoPEjmbfAb2nqOZRBNhPWjvEa05gImgV_Fkhk9o0ZqKRT4ZA0MVOnMPmKla4CvUFcQPGFvSnFT6InoNoLMHAummARfz7yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=vTYWwiuCjhPSpG38NE8J9_AO9Nq-x5XVRvXAXNXEC76xhvOuT2ByfQK_cg9cfO2aVfdpjqAnT-nmWBhRKFsjRQ1HdNldMCKs2yY2_4x5oYt9ifJPYrBC_ufCjxkI-kbAvJ_bQyGH4t-WHpt1UecCSjmHDMb7IQmFjegudunXq1UD9OoQ1toMskW3R2dUArN_1hmaHZ_QTfqbZsSH54kgC85ONx9yCJocK2j5Bh3-3L8AmsQUSO1YbEuLgoPEjmbfAb2nqOZRBNhPWjvEa05gImgV_Fkhk9o0ZqKRT4ZA0MVOnMPmKla4CvUFcQPGFvSnFT6InoNoLMHAummARfz7yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
