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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 10:49:23</div>
<hr>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXEYplLELLwQq-E9ukrEhqDtGDS9X24CEXFLsSGTMMfmGplnWjLRGAJ4sCS0zh8aNYtiew0XM75Bnq29otbpKr9kWcX8UUuT8OHCxkvC8dhD-J4yfB6DNpXPK6dZgEEoSsj7DmG_cjEzBoIfX7vPDNGys75ALXow9kY61a22TS1sKHTyIg7RvxF96yR_d-MnqbmuySQmi-8B00jx4AelmQOhQ5jjybBLAYRdAdqUaFXsY_twHEmdBKDqS-35X34pbkEl1yJJjVzfe9L_d82s7u5X-vcsNMfQq2WkmvlFNWAErK3KQ56jbtayo7XN513Z7aC2jkh4LMGHjAYS8FAZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=NUHOS09AvBlAGispoen6jiG5oyo-_vMxz6amTjCzvYEQJEAXl76mEQjutVuP9--VoDyZRnwEbpkDIqBsAbxCgU8eOPJIPVJ-HxCbLoI8DCssxfVaLVcBkrodPUSZPZ-TkJIYyXNZdGO_N005RvCMjMAQPQbNWjf8Z-ovTdr4QvqtHXWIJiPwcaUaGUbutePprYbShMFK9LyXjeeDpwKx_mus8UzmOvCylGsJ4vClbFZmTW0tRAqMSG_wkGJ7nRyBT7OW5ilJVb2MYRSc1Qp5L3XqcFDU6PcKUDY4PvRbDS_tSAKLq1weyiKeTOjFjLNPRFtu_0pob4hESQHUTusfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=NUHOS09AvBlAGispoen6jiG5oyo-_vMxz6amTjCzvYEQJEAXl76mEQjutVuP9--VoDyZRnwEbpkDIqBsAbxCgU8eOPJIPVJ-HxCbLoI8DCssxfVaLVcBkrodPUSZPZ-TkJIYyXNZdGO_N005RvCMjMAQPQbNWjf8Z-ovTdr4QvqtHXWIJiPwcaUaGUbutePprYbShMFK9LyXjeeDpwKx_mus8UzmOvCylGsJ4vClbFZmTW0tRAqMSG_wkGJ7nRyBT7OW5ilJVb2MYRSc1Qp5L3XqcFDU6PcKUDY4PvRbDS_tSAKLq1weyiKeTOjFjLNPRFtu_0pob4hESQHUTusfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=uhppZHsKlj6yoLSHOLVOpveSirXVgJc2AIK6IYdyRxFTaecwZyCOeHs7zgA1I_V28khg1Ye9mLwilmjwWu5Tvt_1W_S-AIWuf3pDwdg5puP9JWApXWQvgGryAzIKoZTkb3599PqcSnJxtQfoshAiXGfUVC6hLUOudZ5G3risjkx6lupqIDRPawFlUNSjI11xV9LKYxwZ-N-YWYSfB8J4NU_VW8REuuiXHnEvQUC6GpwY_uQqvBpUi3zH90XaZ7jKVduc0P_ZgS-uUp-5rxJ2p6iXL90HAiUVGaIZLM7UKn7fjUPdIQ_NifbCLYGUmGxB8z_Y5wmo1Q1U0vi_0m3IpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=uhppZHsKlj6yoLSHOLVOpveSirXVgJc2AIK6IYdyRxFTaecwZyCOeHs7zgA1I_V28khg1Ye9mLwilmjwWu5Tvt_1W_S-AIWuf3pDwdg5puP9JWApXWQvgGryAzIKoZTkb3599PqcSnJxtQfoshAiXGfUVC6hLUOudZ5G3risjkx6lupqIDRPawFlUNSjI11xV9LKYxwZ-N-YWYSfB8J4NU_VW8REuuiXHnEvQUC6GpwY_uQqvBpUi3zH90XaZ7jKVduc0P_ZgS-uUp-5rxJ2p6iXL90HAiUVGaIZLM7UKn7fjUPdIQ_NifbCLYGUmGxB8z_Y5wmo1Q1U0vi_0m3IpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rjByUsw67RfMsN3LvOUQHt00mVKiLy5KvbNz-jgqbV5-fUJRd6UXp4os45E84CwG_1nNvA2dARd0D9MvmrWJsn03UYlb2_0p89U4B_CeUQRvTXHOBQBPi5myK5UmKa2O41X0K-f1a9rDHyjZ0qPK2Jm3YlkAepQM29wAe0hFZhIQu1fCLgZ59r49Z_FiAtAVOQoQz5L959JhVgsQ5LSAROlR0mmDOcC_tdfw_QiZgYQBSgyu960HwIGSSNfIsuM6ZzHuTz_eJoqa70t_WjhSE6UqX2TihsWmm4ptmOR3-0sIKxwfCE8_whpggN-95DMMsEEAnwh99QB3QG1yqKEqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=rjByUsw67RfMsN3LvOUQHt00mVKiLy5KvbNz-jgqbV5-fUJRd6UXp4os45E84CwG_1nNvA2dARd0D9MvmrWJsn03UYlb2_0p89U4B_CeUQRvTXHOBQBPi5myK5UmKa2O41X0K-f1a9rDHyjZ0qPK2Jm3YlkAepQM29wAe0hFZhIQu1fCLgZ59r49Z_FiAtAVOQoQz5L959JhVgsQ5LSAROlR0mmDOcC_tdfw_QiZgYQBSgyu960HwIGSSNfIsuM6ZzHuTz_eJoqa70t_WjhSE6UqX2TihsWmm4ptmOR3-0sIKxwfCE8_whpggN-95DMMsEEAnwh99QB3QG1yqKEqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzvzQg1_t2hbOwZ8E7EaiomDRkRaPDZ04KwNq2whN0IfWA6xUzamD5XD3IGXfPuyfr6mQhy70-gAWJarEskaUpdlLr6Ch5v6aMKgIfFGCMj42oJIjp0N188y9jWuKPYor10CH0hTlXCWBhm38VxIKBqR8m3hyE4BOaJlnysMZPflzSSlmkYeAO7gYPkPwSguimGimPq7NST-GuIs-ZSf__xlgd2KrZVAu-vRnOhc4TYwbSXveBV0-jbppuA-m4I8BqunM89c6n9seNerh_cNL2FDDJQSAC7ccRu0-L5XJPx679vYWRWp7BbNEfw-a7do-ui4xtY7YAcTBlGy4Y3w-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa1SUO_3erGCcGeODvn4X6O6Nn81h2Q_rsCh_Jvw7YwQ0ashMqAkztc1xj72AxFq4KbJlYzaOiRSj79amKdKk8Cj_iX2SmsY9x8H0QBXbb3b7q4qf4jTU23k31cDJy5W0a9vrV2yNSCWzwYWEki3DMMpOJqdqzgAKdWfCWO5Mn0b0ODDKc0e9qPfgdYw0Hy5WXUUggDFqOLB79KQONtiU7G-drjgqamt-KVKLzKv13H74vnaHeFvKHL90CKxf7PFdfg9g6xFynD96ZLchL_CaDOlnkEHtpiaE5kxixjHoSp8KkdoBD16GTE5vPMCECdaODE2SMYH1NW8v_IoTh_2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMnYjAbZkrGp-TrgLiwlDY-CbGWWyS5WFwlZ4R8gg8wHbrfaWsYX_-t8O9OPCjzrXdZpXOS9lWqSsMikab3wQgKp08A4l6U6qfytA8btttAjNS1Xd6p9bswkvRtRKFHzVQWagBeE9b-e9M2YWhmUdq_zka6Tpcu4FfBy2SIhGK2wkqFNvJX1969Ztois6w029udJk0DBctmVRQhB5ZRy7rRldSjywfFLtJyuL2qkwFltUtgvNnNj4ELUDRmOCdPNPcSQnEIu_oR9Xkgj8z6WlRH8TWPNS84QfRUW_aiDzySuP2PnvAxASJrM2xknKzaQ8aycaHfiMmRPJizW08NUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfLI1913RMseNmjYIpHruWIM0t78rygM5WPCjYAPuQQs48N9dzZnzp0BfgTulp4WDLOGe8LV1ZTbutRQh6BhM7OpiXRcP_Kd-HHD0-21OUPFmjGPytH3h6YLo6KQaXPNQ2t1Wtb_Z0-ABFE9EOkhzoxnOGL3MVBMlp5TQtnHY0TvJ2ibVNRoQzdR9lc20CXyN5xdcmk6QjBmctVpREVtddJjjxTDlmqU9laJH2OqYBlplekGmMaYUNg3srXFQrgQeNVyKCGKqqLSylYv0MKlpeyTEwT8rdBIjsdC-QenQc3U7ScjvHLi9__PTBQZb0hxEKPURRnNyxv5laqpZwnvRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgRPrat8799uTSjzEeMDcn7S9TJp5XBZpY0VkusVQBX9HvPxAjklO-7YcGZSea5MT8BttWgXQD7QnVCgYdpSAXpvhdeqdcW22jrIdQ8zDYX10er0ulSbL3l5mYSnGVVf6E50Yh0FyNKwP-pICc3SOY7KqtzjH9I6EKIjTeVOS81eo98tIrJnOMlvS6xLGeBX1DIZo1XF6bbytWQ34IPBRUOTkTqFmp34Ye6qE9txMGosSofc-vycdBM6wy2jWZfGftyQvvRWk_hmmCDBNgxwxk_Mk_9GEhF637BrmJN0hgvcCnxvd6NIHihUO05nq6uzt9rLzm-UShMEumBfQGAxEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv-KVjYs1-hKHLmn2zqGTcNxNe333n1jN0ZVLxVbcE0tdxW8_oxZp1wIUV-NUshP9ukAUQLe4VeMfeGN30DPyec3yyJ7kkBHv6GTBro7Trnjod8it-kSER0uLHbj0FWykPEQTUm5jl_K7yOUn0yH7iDZccy77hsM40fiQxllSJnoFBddKxV-3kAywGNq4NzfNedbPMEVpALxeDz6eq4UiM_JQiL_oYisB4UAeWyQjjD_4SbnKy0uPQddVUidXM5uvIwpX-n2pboKuJe3fL6B0aslwk5zseZlkl8sZRl_aM970FgRO3IHrCj-ihaN_M9vXwqOjPSANRv9wS-ktJyNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=SpIa2avzNgiBuklilMpJH7iyTuKD5GR79hR5npSHMVTYCtvrVfFV7NlOCIIGb5ARR9oFtu-VeY0ec0NXgYmOQDzzCVQ3CZjmQZSEtXVoEpCIxY1S5gsn2qA2EqyC5SYFTT5jt49wQmTavbTpbjKRsxBaRwrQpMti726YREdUe4ab9UBkWNisrmLp-BUKjF7CAuWVapbZZLYxa84awJNX-82e6yYuVUWldKLzU7VJ-UdWz8jz0fdjeBjg0p8QBFh8QxOJW1oQoz9G-zyoK5sGiCde7cYDogyihRuiIPX40wgZuqSI_KeGE-H1b7X5zNM7fnKq5ENCJHZPx3XeGIP-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=SpIa2avzNgiBuklilMpJH7iyTuKD5GR79hR5npSHMVTYCtvrVfFV7NlOCIIGb5ARR9oFtu-VeY0ec0NXgYmOQDzzCVQ3CZjmQZSEtXVoEpCIxY1S5gsn2qA2EqyC5SYFTT5jt49wQmTavbTpbjKRsxBaRwrQpMti726YREdUe4ab9UBkWNisrmLp-BUKjF7CAuWVapbZZLYxa84awJNX-82e6yYuVUWldKLzU7VJ-UdWz8jz0fdjeBjg0p8QBFh8QxOJW1oQoz9G-zyoK5sGiCde7cYDogyihRuiIPX40wgZuqSI_KeGE-H1b7X5zNM7fnKq5ENCJHZPx3XeGIP-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5mSTAiHyMaE1tPBs1YQq3Bb9i9HqpRUS9WrC-DXUyBy8dAYmVw1z5hWcZvrel0TiUKf65b-CZemdVdg8mnDPk4YJfV8mamxaZFhKdMlZLbxhulyOdTB-RrTuB0zfhuUc7bDKtqd3JO6eU6cq3zeWpocFUhFV1VaaV7WHgciRoYp9uEDqaiMMuGciOl00WbeE64v3EOzB3aJAV4phy2nm0LV44hHwKEaVmXalXvJ033GWcMXAIAcZrds8BsMOVayrcX1xVfDcIWDwM27J4ItzjFzbR85bhIVt0pNSncZ8mdaRnYCGAo_oPB2dZoI0jCNVXuTp3q46dCeX1Se_Ow2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GAoOy9bKsfAtFhyUXWyOr5z9FbWI64rY_bX7Ce0UxY6dW2oF6LSqmqQZEuNkpinrMpDw7IVOmedMBfDF2qDzQRlIOWunCU84nOj3Znsk0bi6aoKvtWPUThJoZyAosQq13EDxOpVXx9Zv-Txkk8Jw6KnXJG87VVAugPvXKUAcMFaxuhCiPgDCuEvOnlaCPv7wC0lflSpIrySBEhkqvU9BDlnr7WsouSbOpsxJLdk40nPVEDz9PKqSmOsbxy7BLH0aDXtfsBXU6wmuvXm68IKBAQh4kkpJbVUj7pZQVu660v9U_BlRJzqbcFjisqwIvIz-6vcLKE18-B018BAsg5O-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCMETejeLOxDYs0iJEw-ir3HhGQuqlPsLyDdaT_TpvuHbLZ7UMZpdJIuk6m77rp0NzpQanADHL7IY8Lnk61L-7UzFi2SECXS88qf8E1i3CFEgM4kL5kaoeThyv10d_LxG_zg46Ei_CGRwXBhj9MEn6nSCRyEXtvzIO4n4TbvOYu3elAdJ3DdiJxxr5WRj6Wvxfd973NImrLiFtc0CFv7mHZ9WICCcpEwmktWG93mppguCR2Q93PiGwZyO1sEjYQRV-EThLwbUz4jbl2wAFqIu-wyQI_Zad9ryNb903oM5PQTaz0rCG7OX7Sh5QT6RWzwwYNT_0iakWvdctbXvNiqhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO5EklmPYXk6HmyqSdYSf9NHuNYRq62ZLJMcxLSi3CCIJEWEi7dIHqGGbengjibokA6IHBuutfyAZ57lT-ode6Wct-LBTMQYo6_jiZf9MuhPPI82eQ1f4Nt_f8vHCJpjfGVqxNPGAvKyfwYtbQVWczBNOsyXaqpw82JjTeDAdG_26q6Nvk7ef_D1b-Wa1XYFhZ4ANhBiJF8CtMgzqF1apRLWw9ctt5U5cX9pZlF4zKTCyUQ1lmha5o5UVrkucu9jwUBxxXF0wA1RgWfMbEM6YiVeAXmP3ojz2hcAEOMCksfxHTgDxxTH_UjusNBgZLe_57GOFCT9wsizxOb3aanvgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Axe7ziebzBCwzrDVoYhcDNK83bJDL8B8T-izD9B_BZ4D-7PzHmj46mqST1onQXMhU8FMP7X6owVj1ICklq_kNsKrt7g04ERXpqwlRZN1ei6cYBxD2izePn7CIjXLOay1MfKZ9wT-KiKEs4BPPw4UfzTUAVZQrFQMtgYu-Zqd4kPDf1P81VIhqpl3jM2vifuLBRrAjQ0VOU9cR21LprQnHnXhx8zW0nrY03XSVIpb9ST_5qKuCiy-4YFRUwCzy1ZVrHtCfI7saEqAJ17p8doWRHknKIBR6Rpd5Uax36JF6WoT6yiOY-2qFWYAgh5-x1SIY6-raJBf6-Li9P_8BUnEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DobapqB5dSNJiwgJGnPDCzd4aVKH7LSgcHAWRmydfQBkIUJpWbQTautmvPBv-YiTE8H0iD3I1nVEwRVF76Com-JEJZ1c4xSWucYQGEOult9NZrpTlUYLUCrzrCBLPzj2tX9nMvYWS-63nr6B3VqGnkx2p23bOILvxy1LgHZnG5Mqe0H27xfP-iicbyrzA3DRisGrnFfBLPdQIB1Cd1R7PhbX9SCAPmDksn2-nd4_UQuGA_F1V3BXVrAIUcDrmOUvhWaOfJH1UWtkrfm7H2Os4cAeMlhasEOvLtip8wTjt5ZbpBKK5kSS_gw7XuTHaySqOz-TEFQTcn6ulBMpuIWO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpmU21DfX6gkPO8YBMqGp8uzDbzEkVmgNqA1xJDGmyXYCjzJJntr3ElFDCvIJEVJcA7wI5OMF8g7IvCyDhNxl26U4SpMNDbMmHJ-L9DH7alY64ST1RfqUIUclQXi4GzPa3LGGSlNupImEeBTbnAiYtq7JYg3VX4hwwxHrnhNlqY1P9zetPUT25Zm73o4oJJCGI_cUH5PrVgmMD4bXIFOGVRXkK1leUeUfOjKKOHdL-_s3avs1JiJrlpfKUhg99JJPJqqLFJaW2kn2DuT0ogRyBCQrx6M9q6ODpVIyIUPwGg523ExzXNAIp1E1oImUAi7giZpKtYpRoUyYM22azLIPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGNTKygJS67iQVkyR-XXRoqpjDyXa24_3qmb4xrtywB8PXNgalblg6I0z7_qLoUwNLOdhmcyomK8xnyzLH5faAHDAhDd8eVk3i-FOzzq0Jp4hEEdQSD8Y36r5U2h2E907jtz1QlW97SvkOx_pmCerAMZ_ezDaHBBkLdYiYmNsosAmiMfrZWp0NpNHTHHJDzAnk95wgv9GDEZdGAgHByMiGrHvhM3Ehs6ZC1Do0vdNXG5WA5yrBeq2KxZEt1B9tGaJO6EA-qT1hAlKnlAwAeMtLkMtg_jr7A5MIsu30awATq9iDj_PRGPNlfsmT1OcMjoizOWzWtG9Dm-izBS_Jc36A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=G7EdCAypqMoqC0JO4uj6KDPIaAo28dLzBJ8A_VImKF1rNqrB-vkkXKIPUsUgjw5xiyV-6Mh29xGcP1rBPTX6radqLk2SSopqH5ZVWvHlJ-jeTtjCmgfzP9SOxh-Seaa_b9TJlrGEU8x_-rpnu4iDYbt2gx9EFj84gBCY-CIRA_Ru7WYyO30_rorai1XjrDW4WXC9EF4exUvAoYb9XfRStaoQRZRBNUsXM_2CxdHoN2yQR13mEswGiGjQHPw90c7DK0bu1NON-nssJA-S0mHGBCGHmLPdgCtJBNpvsdFqzXU22rHrQPZblX6PApcS_jHWeQgOE2wyn6BczPFZl2iQFG406KDDVtPkTzkHR51pv77vX570rgw7rNS56dy4yCwkKNbbBkStQoc2MRGS0Y8m_pw7r2-zEXXyO6iiFjHrwlYB9jYDolGRmUMhQko8RqU_W6LxgI_BY_qKtsePzPFMSDxYAb_jJqwxeKhdv_n975-Jm1LgS5B4-RLL0hIEj0RzeM9QT-2QbpkQkYoGXBQUqNsK0L5OFbV5LtXmCPnZ8y1bR2xrZr-MJjNBvOSEhMiwoc6hIr-gDN7obYenBf9rRT52CklB0pMobe8rAq2pduTreGfSthmgNbnfRZkahjvxFHlzH9AWNhu52h8w_ZLG6Sfj-3u1URLmITWNMRk9BVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=G7EdCAypqMoqC0JO4uj6KDPIaAo28dLzBJ8A_VImKF1rNqrB-vkkXKIPUsUgjw5xiyV-6Mh29xGcP1rBPTX6radqLk2SSopqH5ZVWvHlJ-jeTtjCmgfzP9SOxh-Seaa_b9TJlrGEU8x_-rpnu4iDYbt2gx9EFj84gBCY-CIRA_Ru7WYyO30_rorai1XjrDW4WXC9EF4exUvAoYb9XfRStaoQRZRBNUsXM_2CxdHoN2yQR13mEswGiGjQHPw90c7DK0bu1NON-nssJA-S0mHGBCGHmLPdgCtJBNpvsdFqzXU22rHrQPZblX6PApcS_jHWeQgOE2wyn6BczPFZl2iQFG406KDDVtPkTzkHR51pv77vX570rgw7rNS56dy4yCwkKNbbBkStQoc2MRGS0Y8m_pw7r2-zEXXyO6iiFjHrwlYB9jYDolGRmUMhQko8RqU_W6LxgI_BY_qKtsePzPFMSDxYAb_jJqwxeKhdv_n975-Jm1LgS5B4-RLL0hIEj0RzeM9QT-2QbpkQkYoGXBQUqNsK0L5OFbV5LtXmCPnZ8y1bR2xrZr-MJjNBvOSEhMiwoc6hIr-gDN7obYenBf9rRT52CklB0pMobe8rAq2pduTreGfSthmgNbnfRZkahjvxFHlzH9AWNhu52h8w_ZLG6Sfj-3u1URLmITWNMRk9BVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=BaMF99XH3P8acqBlS-gYSmlyEgcdBpLewJNc2tkbUEtablJcn0W6cPiBHvMLzNZX41xIDbgHhTn1MrwxznfRoiH2m1AXIVbxoH_rCrre1EVPMJ0rWS3-XJgRrN6gD7XyVV1WnwRf5Iydb996nTaJKUsydmMx2IoMetWLFLbipwD_kLXVLKZfRnMF-DKdto8uzYPwy-SYNftnVn5zRmAlZzv242dJagYDkGaOrecysu6Olfwcc7XMGSKiK2ASBV1aTtZNKuFTVyIos7z5fnr4-ke0btQkRZNkGLkO6zWEqajbjTvRC_WO7Mll2PL-Vb9Av9eQfoYuJ3opyXV6GCFH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=BaMF99XH3P8acqBlS-gYSmlyEgcdBpLewJNc2tkbUEtablJcn0W6cPiBHvMLzNZX41xIDbgHhTn1MrwxznfRoiH2m1AXIVbxoH_rCrre1EVPMJ0rWS3-XJgRrN6gD7XyVV1WnwRf5Iydb996nTaJKUsydmMx2IoMetWLFLbipwD_kLXVLKZfRnMF-DKdto8uzYPwy-SYNftnVn5zRmAlZzv242dJagYDkGaOrecysu6Olfwcc7XMGSKiK2ASBV1aTtZNKuFTVyIos7z5fnr4-ke0btQkRZNkGLkO6zWEqajbjTvRC_WO7Mll2PL-Vb9Av9eQfoYuJ3opyXV6GCFH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ockgFA-pbzGk05SNlCGrwiK_TIWPUAJJJa4eBOeIu09VgrPkVkz4oopcnW3B7c-h-lkrrFsBiEchMzexS0s6SUhbFGqEsLRMCC-wDrDxtgfZaPrKoeum8B9TISQ_Ba1QuTfyNaA2MIMTt7ZddWq76TPzrVq_4CKKJGLR13mIDcQFCvNtsOb0WdlTJdUOc8fstpeeOho8Rq6idhfAxASVCpdX2-EuA27GC7lM2lAeqF-ecfaGeZ2Liqlb8nAcnuYzKI9BvAF-oL4nx3P85026PG-d_I9HUU3-p6vWaXiujVzNqANl7_v1JrG9v7_OSeHS6ZMQKEPTCWRUfTcq7do6xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lewDHmw-ZVNrhKUdvqwslNReF8UG5VwE1x0c6zO5Om682wL2wIE77C_Sqs38P5SjB0IJyQstlfMn6ymH0t-mDNOe3ebM3Oo6e7fxct1IO-8Bg2ebhu3Qie0oy9geTolwJDW24svYg7kxxthK6OVAh1mWkbv-qjOLlK5tYsJSLu_Tnm1NiB7TowN8-sfcLYwXQhzBV493Su8PF4pE5_Zo-1BXnqaXPZAM2NeXH7cagg2D6gfRT7NrF6i4xv4bPc9NqW92UNHV1B1YeobeAkzdM3zjTrd_0VlCxbdoAkxexJFrntNH2XuNUW954czIoScPch92ijrIZXbgp6rCbWoMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axdrWRdXhWwX25gXPqTZEmZnqVm9T4iIpPsE7yCd07byD8E59XjU4oj65ocPjID_XYwawBci8uJcMsvazduoyTva3QuJsKBWUL2jhc25lE5n_MJldG8KBdgtzlp6OUsSsgZ-rFj-1T34cIc2naXEiKNcmDrfkQ8WPmdsdvFljUiv6VQG7Ae7JYI73vi73u8vyTEzCrTZXB2w3h6kCBdpnlJ5wjNPBpSXOm8mqg7p6fDkDQtJNkGLLejgjQaL7Z3mVHJKtcTad83lFCYP1OUMOZNGUj6R4AFfXvWED15gtYUIj0QJYVkxGX5_lkvjrhm6Ry-jrpT7U7J_eN9uEflwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze-HAOZqdlTVNmkgPm5XY4fzSHKIWq7DD3oElWNzotxTcLEnUNlQ5U-Me_VTD63bQH0R_SXPMUWKFvB8nW9FQIbsq5Q3aBPqBP_1MOnxIB1Gqd3Jg8yUO276ijYA06vDqLQEihn79lwy2hbNQL4bzANjUB04486YM32IRvYkbiiuBkQLmaHAAqBBocguxJYsh4K7zFgOorgs6Jajp9g_O444RVEFAzUYd0e-vmpTIs1h7nmyKV97rW0g0OD7AvxP3z6QPzFIeB3BBa02KRoxf24K-bSwmRpoXd4qNdP5vYw_nNSYA0AsoGKuzaF39Ad4w8eZmkxI9JbIHQEWboSiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwDI_us_cw8YwCB--i2CFNHGSgG1-LSHVc8BeW3BIrbudnTv0pUn_Ic4vwbnGj2dHXKQzFBi1jsKhBIOfgzZST_1mPy3aZIzupJ-tsFiXQseNXgnwBnmGp1nHfBD7VF2EeH_WcLs0NKq0S2W31hBT0hg7eV4nQDxmweFk44n8aYjWQJTCFv29bhzwOEar6Hx6jHg0Y1GogWysR8Lpa6z6CSg2znWiOlphu9TlPMpZlidknkYOApr2CwsVnwJex6-GLwXpmoHipda5PXUKYBI4KHsX0F4A6AEwtk5iGZu7nMAIbTAKHBFX90eB_kvNnN0bUfxA75P1uoDRB4JeLqxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZx2tuwU7JRsQv3YdNlvHdsuXA76SXsAPllasKPdvYsEV3-ZHEXDiT_AUQAsVvlZFm0fDVio9CfsItC9hwNVUTiO-HdzMmxzc-UYDqNllV9H3nS__DbYgRY_yuG-38h-MkHnntEyrcWEk0dXc_XMllscfJGEhPVPoMjp_M0d8tNjn5faHgB-gdTsQscTX4r6eJtCntIiULl1NhIfSI04qPN2FiNYLLtQ-LJowPxHSpC44IpToEDRO-fi-nQn0yuHplloUkNZjT8BbERqpgmpkQasn2fF0vai4M9-m9NQD_FW1j7l_jcoAlyVQsnjin8uXGvgPFclWTVaY64R_ucctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZs-OvwDbDMkNqQq6MvbN33_00Y6PeNF53lUYCsaqI_FI586nVLCCtS2dNDRqweb6aZ_ncvN-UktMg4jEccDLL6FUuikEGHrF3d16YH8ifQzIOp2eRLK_QSgMpl51-eVcpQZgzt61_GCj4pSyHSonYRTh1GwJoAmZEHuPD0xSYhW1hAxH-0zzjUDMjnieBpXKwKAnn3OVvBklHJuTmoHIdY-wzgA0zhsIs7-mPBHfcPDRvTtaEMWfe-mjCu7YQa1k2jYL0SJjsp4aaHzuRwUne6luGkhsdniH401SCJKtsUFQzISFvMA2OHkmkj5FUC8EQ5MXbtguaT9QlbqW162xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_-6A_iYBE-RJI3bjqfHeX16A4VxoT7GctJf0O4iZqCjsYe-tVx_2iNb_UuQIHZb7sTS9QpCJKjBXtDYNDoWMbvtiZN041w7yIeurf2NffNSSQjYRvCop39cQAvLcRiSMWBOXQ6whTpjBld8aGCbWqHfsaLrgyoIe1IafgyQkavhMdMy8zwacTUY9DhqCz02uTRyt1PazvzRt45RsT0ZXtWat-9EpYQ768BziBQM0RQRbpzgwNN-_q-j3vAohf6GJnofDFv7p1Dtotfw9fzldltln-fZ7j4n7B4OxAYEY7CPLuAtOrMPMfsWSDnxvJKkFBX-oTZJpM-BNHYaGLbhyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzm8LwugjQozUxVUxucgCiZWf6mVDZYHsB_L7KP1GRjsPtqoOlO6DZuZGCfJPOUl-jRVt684v81xunBNl3Wj7yYJbgzzslSL95xK6OCG3cWFmL5dUs9V7In8YY0SrYnMaaKyBuI5xvvUkfADRkMp74xOhLyj5uV7klSBjvJbeOIdbDDOEGBDnjqZAm1f5wTAwi5HgI2FQZLo6BdpgMZyKpMb1c9t5ynkKEQnzLsLObU6sgppSttWrVYf7ZvmbwUSm8OjTlCsADFb2tvfOSSbVCo1KkKmMkd64MsLA39m4Aq_1ozdOOYZohCCsig9DulOO_GqB1jYzVlOMhGyTPyv8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=QkXPJQU4bSMk2F10qGPdgP3i6U3koMP0NsSdIBcPnORHpBemu6kgLKdlqW_nwnE8ALOjamo5-O4VfF1uhxYsz7RyBddhmyCWUDijT-HWA-KitVgIpPzhbzkYJV6Y0aTbpZVioPn4InhuJtJtaeIDOdMOb4Xmv2papBD4HJDeAqZ2ULqHpFUUs0A43O62FDUeBBux4v8smI73FIl3XxofYEe_iuRvktRiTkZ5Auujv7iC6OiypRCTgel1zF9TDMOAbdoR7jb5AODnaf0zqiiWbqjkw5ZsEpxuFreKQlemToQh7UPk5hDcmAlwD2veQZjMGBecCyLKQqnnlMsVKH033Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=QkXPJQU4bSMk2F10qGPdgP3i6U3koMP0NsSdIBcPnORHpBemu6kgLKdlqW_nwnE8ALOjamo5-O4VfF1uhxYsz7RyBddhmyCWUDijT-HWA-KitVgIpPzhbzkYJV6Y0aTbpZVioPn4InhuJtJtaeIDOdMOb4Xmv2papBD4HJDeAqZ2ULqHpFUUs0A43O62FDUeBBux4v8smI73FIl3XxofYEe_iuRvktRiTkZ5Auujv7iC6OiypRCTgel1zF9TDMOAbdoR7jb5AODnaf0zqiiWbqjkw5ZsEpxuFreKQlemToQh7UPk5hDcmAlwD2veQZjMGBecCyLKQqnnlMsVKH033Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5MAUfJxET0qzIJFglexrqECRqTgdlPbVh2kr95pwMuBS-d-SCEPH-wdgylgMTz1hp2B-oyjk6LflEyV9Zs03HcdkrIeFRfjwZygq-DKXQ0tZk-6W6dLaJKFWlkvfQOaiTNhmmLlP9wO8OChiJd5b7H2gSgIxuex_FhASCPPwc6Z1cyS8aa3ZeYLDiMK0y6Acvbuv5PE4msH5Ns907_sElZ0xW7fChOsUYipTQnyqQCP_1hrGnpaukpxgXQcQjVvLWz3jxRJ39PzGYelcwwkd_rhDxSm0PAiAOJJoWD2m1fb3uCSY6nYuzhCddTu_XGWIXoeuwSqPMiqZ-bbHu3xsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=PjMAimvhyQJnNjwuC1quxPPNURhJoUnf1-DBMq5mE4Xpq__OwhDwOXGakfpUf6GGmRtXCfHHjVnKd5xbaQ6PdsZBKxwO8SrOqKMhH2o17279FVuYr08hY7L01T8RbUr-r-t5TQPgATGrGMnzHbJEsyl7uiEZOnzEcLfsRKAPwPdPbrG5hlj95En7Pu0KsqZJCM-AHZlaHeldIMMbWSnLx6EbOWv8Mlg9ADcZDStqLdzIX_M-myXFSW73jDD7rF3ooMwRwjxhPJTBTiRh1LYwU_DKr2tEgCa1DvpoJ84Y4XmaLTHX1_GIIQdVh_46Q2WwiWkvmRk-6gYU-Cq3zqnSAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=PjMAimvhyQJnNjwuC1quxPPNURhJoUnf1-DBMq5mE4Xpq__OwhDwOXGakfpUf6GGmRtXCfHHjVnKd5xbaQ6PdsZBKxwO8SrOqKMhH2o17279FVuYr08hY7L01T8RbUr-r-t5TQPgATGrGMnzHbJEsyl7uiEZOnzEcLfsRKAPwPdPbrG5hlj95En7Pu0KsqZJCM-AHZlaHeldIMMbWSnLx6EbOWv8Mlg9ADcZDStqLdzIX_M-myXFSW73jDD7rF3ooMwRwjxhPJTBTiRh1LYwU_DKr2tEgCa1DvpoJ84Y4XmaLTHX1_GIIQdVh_46Q2WwiWkvmRk-6gYU-Cq3zqnSAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=Z4NPnT1jeMcrKm3CTJb1KUfyifi1-qynqJj6wZ-y35flE6OOESQlSMetS7slcEEcY4XalDy9esoC_jIRf40m1RoByLLGYzFCTYu7OyXp9yFYVnHhuhaKIs26_S4DwkrYL_Li3_iYxQOjBjH7jUCtzHohGDJUCLcx8NcC9Q_-DUfyfIhOMYiOS88ECeUicWpBhEWvCP9DijrTGtFwpHmKwZlBzS4ydm5KAbrNqHx-06t2hIXE_FrdWr5KGMxenyZMZoahCbmNqPgAY_wa262AR6eUjZeS49ALdYavPeSQXUj_p3ml9RNjFII9YAeaf-Llfxx9mJindjf0W9ja8HHWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=Z4NPnT1jeMcrKm3CTJb1KUfyifi1-qynqJj6wZ-y35flE6OOESQlSMetS7slcEEcY4XalDy9esoC_jIRf40m1RoByLLGYzFCTYu7OyXp9yFYVnHhuhaKIs26_S4DwkrYL_Li3_iYxQOjBjH7jUCtzHohGDJUCLcx8NcC9Q_-DUfyfIhOMYiOS88ECeUicWpBhEWvCP9DijrTGtFwpHmKwZlBzS4ydm5KAbrNqHx-06t2hIXE_FrdWr5KGMxenyZMZoahCbmNqPgAY_wa262AR6eUjZeS49ALdYavPeSQXUj_p3ml9RNjFII9YAeaf-Llfxx9mJindjf0W9ja8HHWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm2o_rAjjVsd_6gp0ZqmVmR3F4Fie2RfQymeI9bX02oBA6EukoLez5KubuDpG8ubr_9-sdEqQQSMdcwartvxE9njHYx8KrJb3gKgjYQdbe1n4FBoLU5JlM3tPABQx7ZqXxUAjlvTvTWN-QTqcZPnQ5xsxoIpHP15j2x-vAvr1gJf39rRqWx7gTN0vNZ1V-D_q0kJSCl1eAyvzTdV1-P0S1Vty9dPg0zuNoE4jZsI26eEdIGetXmZs7w0UYW1EwtClAkRPf8c1WB2Exo4An7ou0i8lxaPLL_pFt3reEh3XLWGQ_TZL0IOWhJY4hnu-sRzn7AKwS9teH-oQEkt-co3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=TxSriBT1Y31WMelizZpVBonbCDnvulGNoIjpVeXl46pcyc-sK47G15fTBNWt-Xo014ybQLDYWTmialex7_eDX3ROVu7Ds-EfsjYb8Vv1O8NsxI9zZaRABLu3DuKWmUcjht4834CJB3wwW3Fd9-cs8jb-VVGJ89E3y8h7Y2AydIdk1RqmozOLKcbMMNRafk5oFsYEBLNMMfTfup6doUA5v2l_Mp2Fb_s_tes2hLkfbci_CwIPbQkTbGvUzXSBk-K3sCNCr-PEOJ7QNUxIimIV1cFEly212IyQGNhA6JAzJ-aQbM0ocSBQ6s9yoc8Qjtvpc3mB6iHtJ41AzI7Hu73DIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=TxSriBT1Y31WMelizZpVBonbCDnvulGNoIjpVeXl46pcyc-sK47G15fTBNWt-Xo014ybQLDYWTmialex7_eDX3ROVu7Ds-EfsjYb8Vv1O8NsxI9zZaRABLu3DuKWmUcjht4834CJB3wwW3Fd9-cs8jb-VVGJ89E3y8h7Y2AydIdk1RqmozOLKcbMMNRafk5oFsYEBLNMMfTfup6doUA5v2l_Mp2Fb_s_tes2hLkfbci_CwIPbQkTbGvUzXSBk-K3sCNCr-PEOJ7QNUxIimIV1cFEly212IyQGNhA6JAzJ-aQbM0ocSBQ6s9yoc8Qjtvpc3mB6iHtJ41AzI7Hu73DIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGpPy-u6T6uwFpHqoLnVS5ySpkHzhyAbB3lNYwt31POCdHtId0XKDMe2g7_-aQDQ8BrQ4eFGb8rkjnTdnVwUQvnPk-G8fB4zvMTXxGPKZVk6PXu4rKIHm1ACTwGuKnnbyK7zIJQWX_1eyTaLg-i4_ZCu1TFb4ZyAyYcJK4OH8yO4rVzkibr7QdQW09wjiTEjoQ5BF3FkcQUPba2f6ybDzsxVettBh06KtBkegPUNpHD6Ffk_-z_pc8z2twpa1knu0VJo0cXtAiQ9ZuFan1sv7if4uFaUsoO2fMKffuYmvkdoFFIKIrRLMGPZDM-yLBvKFjiDO_dJ3nKep9Hu0LgJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rznPZtZ7YM16gl0Odwjw4JaQY8tsNHXBleRZXZgNTXhWXNrnymcoXhKj-0zz2DWF7IKb3ObdOZroh59TnoQcNUiLqgvJc0Xl0RFeHzx7vjcnArqXKdPKzqaY2Gd1OevVCpFI6ZuH0TL5UHU8CdbS3PFzSCTQyOIsX_7UIano7l1s71yZFn0CuqNVfeGUWrYZC-SxrOKz6h64ShEBluJbnLPPHeAeJYV2_QL4XPc9xD4XmAh-8uK5Nao39mu3mwrgBvTEagpRL0wHVGcRQGA7NE7N61m9BgIkblL4wBRe5LhuzvSxonyWAWU7NFuCTIrPo-BTMCHnkV7U_6tL0I5R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌های ضد و‌ نقیض از استعفای پزشکیان از ریاست جمهوری</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5222" target="_blank">📅 00:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-cJI5HsC9xT2m19UIVxn1asFtlJ8n2ANJyjhn1Qdbo1odU2qtpz1Jj_MhGlzYX7LfvrUwup8a_Ei6fdShVm3EjlnS3hf1u6GsfJka-xFA3HJM_lx1VZumfO0sVLw21IT31ij7zVIK2KRx2Pw1FG0__Ot-SZOwkmgVhKmq8iSRfiVEL0gVzs8XI-Xw8nYGKH1I9bZ8VyymmzrMNRpQgmVrEYlXoL7vYx3S760Cl4Fw8Ef4FFKRV2QQhvJQS5Gt8NYznVieNlgHPQajgJ0pJtFAoxz55SajYbPay9zTRAXeG_61FA3u04ooXZekQoHvABZxG5MCy_JnNIRGV3G6ZpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m51UaWq_dB5R8KzV1S3rNiv5h4sjIjTU1gOkKkfHszsuLRJ53Mj5sYGrhhAuigbZ8_V7uR691YTzOhJe8_yTltNS1NF67_8s_rMHkVbVRs3h0Jj0SLQBIIOYSvfq5nRhayG2yK_GPEFDtbWmz2pgv1QLsrwVnFMZUqlmIToMXwO48KaohzflMKoKXgw_YCqtc3jkNqcJFYIVOgTBaX61iyulNdIHJm1isrRgetYIp3llFIiM1BcQsTQQt4T4rjbhbC6QR3NvdBtgBp9Bj1UEjrOilYCrcG_uCkqsccLozyyIVX3YOtrDIYDupXTm75pWFkjG67auvQVrhoTXC5Z6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOK7bt2Bu3_j_fT0tUVwM71K23xN-4hl3R25bqN9wTsdUSw-2-ty1iTEi9_ejllAM24zuhbyoj69sN-ezB4y08hWWoSdZaCwnsNY30Ws4l0CgidCarvpj11F2gyOFp0qf8ZHKdJOcQZ2u65Zwq4Mem5e4aXxtxp4YYtvJ0etU3RME-fuy4TAzhB-GCEdMlTttlvPO7XGyCEiaYC_W8DE3kjpfVMYU1oOUFPxUcSDr7n08fkAPS-Jm-YxF-Q0wTcN19-Yorm6JOTdJ7a5WFiNvX3vFPA4vCMgmJ7EjYlxQJub5ncAAjW1fHV9r5CxrFveIUgvBT6ZeD58hZQz5DV-6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGGI1Ih127Mciz8I_kV6Sr2Kp1UXFsm0ISFy-5ZsuAp0WG1kbLModzCjv7-eWWH6zIHY0MnSh8XnDwyahQ6SaANMkXGgCLjzL9pTsurnTWAZK8IqyFhnCwCQhOfvtUcBrXfJgqXHCk8kq_UYc6UFmuW2CiQ5aj0zOjP6T24GhlSMXbJqzVUjti7kwDjmVQAGqmdG0T_uBEvRbd7U8ky3woEOb1pKnQZTVBFfp-nucHqZaKuiDGGOPzy0sattXAvxjPuDlmxLxiwA9d1_VoF73UhrThIDnmvHrdJfoqT89VFThJwW4MaFIpqO5EqL-Nqo0FbudTj3hSqPVMb3evT8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDQcK3h8lr_hnPAKP9ZopqSzhjOMMA85dKt6VheV8DYWbhvlNhC3KJ_3-0Y8HFxyzXu8RgKuNJ1SWMN6bvW-J1WLm0C_gvvjfuR32vD7qmeWIP8sw-smceP_aRM8bWyualup8GMheCZznNrNcaAK0t9Ky4PfyNiY8rRfwTGQogompVIbvLFTU3-FdEM4olJyxeg8YjP-BX8p7b3KMM8rr3_fyQpvZrKO7HDDDU5tJi6XzsPY4313JfYET_tZbdZ3oWcqscZFY4J2gjkj_sKpLQCxwU3ukoRlsTpERnw5gWxO2ApS1DZSPMLGAYjwRBAA1dO39ciZt0HbYasQW8i4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJdmP6RTwOZzl9n1OzF1OtP36zuvlzZn5fIc-cjPgsiux2dP2nSdP1Auw2jpHg47RjqYcSdiuU9j7KLrurQAvlG4G5weDcKSZteCek0It9FafsTkySy9rBmSMncdcA11rHzJxbd9cMFaocSc_LbdsbqYCpllCluoA2ru68Fz1rnbjl6ump7P9fJG9wD4Fba_YHSzJwCBqaFKqeUWiYVIKLocdsATUQytqhC2B8daxlI6hVpkdlXOrvES8fWQlpptN23RM3PBTBIIHsvBWB2_fFf1JM7_jQS1tJfMOGBdg6QcsQe4n7IsrvQgZAsAr-_NCGTdhVHi0--OuSLiqgqcbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رفسنجانی سالها پیش گفت من به خامنه‌ای گفتم پاسخ این همه ضررها در دشمنی با آمریکا رو شما به عهده میگیرید ؟؟ خامنه‌ای گفت بله! جواب خدا با من!!!  و خب این جنگ‌ها و تحریم‌ها و آسیب‌ها و کودکان میناب و... همه همون مسائلی است که خامنه‌ای گفته جواب خدا با من! یعنی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5216" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db68225cef.mp4?token=U4gdIw_TMPX1I-L78qGRytbyQ0OkRza12SJVHNz7tgQNtkUAO6wSlz0ocVX0VZjEWZWNSaBPvs17DEw2JZZsclAQF2HZHYwAUCYFLcx6mucQIhBxICzvkM8un-cabIZIT_2gBJISVeSyiqkufB1m6Jr-uFZp7c4ty2HS-dUjHFS-Qf9fiEMW7cO90GRbARZNXHwUn1wijTxDVmNwAUfZTVQS0n-pXsO4G2Bh-Crcd5Ka4g3HeqkS2uNgPUq24wSZAi0yrB3Q1v5rZVdDPsp78GwoYZM4FDixZFsp3U3zdU6ciSNE2N9ACFmyjgpSjmWwSUkK-P61wR3GEm9fhvwnOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db68225cef.mp4?token=U4gdIw_TMPX1I-L78qGRytbyQ0OkRza12SJVHNz7tgQNtkUAO6wSlz0ocVX0VZjEWZWNSaBPvs17DEw2JZZsclAQF2HZHYwAUCYFLcx6mucQIhBxICzvkM8un-cabIZIT_2gBJISVeSyiqkufB1m6Jr-uFZp7c4ty2HS-dUjHFS-Qf9fiEMW7cO90GRbARZNXHwUn1wijTxDVmNwAUfZTVQS0n-pXsO4G2Bh-Crcd5Ka4g3HeqkS2uNgPUq24wSZAi0yrB3Q1v5rZVdDPsp78GwoYZM4FDixZFsp3U3zdU6ciSNE2N9ACFmyjgpSjmWwSUkK-P61wR3GEm9fhvwnOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴ در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته «دو گزینه بیشتر نیست» یا جنگ و خونریزی یا مذاکره مستقیم «برای از بین بردن غنی‌سازی و موشکی»  این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5215" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=jFYFCodzOXWSCC8PB1qnZcoXxoL1TsoWKKAi_E6P1yl7kyBwrYxSgi5RMCIYEzZ4g-e3DKqS3JIUmF1YUp6w1cng2OGoQYNftriR36zLrO2q7UAkj-o8ERvfE_szUwXfSBvY9zO-1v01Cfd5QOygbDPeXOcpfd2kKfk_trPZhqAaWpZpnfdGsUjeOagH_HsiWrj_7fc0s_jzlJ9ExqMBJfiEbrBGuYJdtP_YTZi0Cd-7yHIJCDMC042QO47EnDshv0Wo4ZjHyR9JuXJQ56tKhK6vfxdZj8KFV1coCVv2KU_aFmGuwMUji4OfKySbT1rJ4a4cnDpMsy2YLL3xfsaQgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=jFYFCodzOXWSCC8PB1qnZcoXxoL1TsoWKKAi_E6P1yl7kyBwrYxSgi5RMCIYEzZ4g-e3DKqS3JIUmF1YUp6w1cng2OGoQYNftriR36zLrO2q7UAkj-o8ERvfE_szUwXfSBvY9zO-1v01Cfd5QOygbDPeXOcpfd2kKfk_trPZhqAaWpZpnfdGsUjeOagH_HsiWrj_7fc0s_jzlJ9ExqMBJfiEbrBGuYJdtP_YTZi0Cd-7yHIJCDMC042QO47EnDshv0Wo4ZjHyR9JuXJQ56tKhK6vfxdZj8KFV1coCVv2KU_aFmGuwMUji4OfKySbT1rJ4a4cnDpMsy2YLL3xfsaQgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌نشستن و  با نخوت وعده «دردسرها»  میدادن برای آمریکا و دنیا!  «حالا حالا دردسرها» خواهیم داشت!  بعد که جنگ شد تقصیر مردم ایرانه که تاریخ نخوندن!!!  تقصیر تلویزیون اینترنشناله!</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/farahmand_alipour/5214" target="_blank">📅 17:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=Dx_6rJbnUmQ-P9lar7LhChCuciGoG30VlM3eiqv_A6Rd__6BzituH4o8d5Wk_LzlIObZyzv6-OddMu8N8CurGlUH3idAKlPqwHi9pX26WiFPKal-B8McKyKFt9rIgEOd0Z-fqWsGZlSGYLzAVbmh062PvZYyfMylBabAJqeE7zb5VVsiJss4OIqSf2lFlpuv-ENtB8D1pUJrBemDKNiYT6xtBxPG7FR5KR2RBJfVXNeqVZE1vgko7lqpeItduhMm4XJ2B3N-w84mnWim9Sq3TRhFiT5xr_gfyj9hrx3_Ncoa3aCO3RokuQ4Sz33Qncd9OCwYoM88hicmhLC2zMP1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab893ceeae.mp4?token=Dx_6rJbnUmQ-P9lar7LhChCuciGoG30VlM3eiqv_A6Rd__6BzituH4o8d5Wk_LzlIObZyzv6-OddMu8N8CurGlUH3idAKlPqwHi9pX26WiFPKal-B8McKyKFt9rIgEOd0Z-fqWsGZlSGYLzAVbmh062PvZYyfMylBabAJqeE7zb5VVsiJss4OIqSf2lFlpuv-ENtB8D1pUJrBemDKNiYT6xtBxPG7FR5KR2RBJfVXNeqVZE1vgko7lqpeItduhMm4XJ2B3N-w84mnWim9Sq3TRhFiT5xr_gfyj9hrx3_Ncoa3aCO3RokuQ4Sz33Qncd9OCwYoM88hicmhLC2zMP1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی! جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!  فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ، بی ایراد هستن…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5213" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLAOYEELGs5BIKn1Q8Ctg4ni1RwO5RlmuofYVpbykHqUVt4WaAYUNqv9YzthlsfNkahSnvHUS4JECCyh24jSSHvk2DmfyGdQ8sUi6joaQ-dPrMnIQZACssNHbpAVY8C8y8D8fFhlCZx2JoWfnEx9B2nxrgBJaluk3eMjQUHWhdkNtZixz3KKP21prGQ417fD5OKX0ozDCKRh0jfsQFa2snfNYddO0AYE3pRFtFY-7j0KHWojYRSDbiWQjyby1EVDBW23A2gjVT3rIb0AQc1eZFD3iBQzCxTfWmZhOlcbl3AeAGq-wub5FmVFyYxHjxM-vaSFyzBrbDTN4s3xRFo1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله جنگ ۴۰ روزه به خاطر ایران اینترنشنال بود و دیاسپورای ایرانی!
جنگ ۱۲ روزه هم تقصیر افغانستانی‌های ساکن ایران بود!!! یادمون هست!
فقط فعالیت هسته‌ای و موشکی و نیابتی‌های جمهوری اسلامی و ۴۷ سال سیاست آمریکا ستیزی و دنبال نابودی اسرائیل بودن ،
بی ایراد هستن و مشکلی ندارن!
و همونطور که می‌بینید روی میز مذاکرات هم بحث ایران اینترنشناله و افغانستانی‌های ساکن ایران و دیاسپورا! مشکلات و دعوا سر اینهاست!
خوش به حال آخوند که چون شمایانی رو داره! هر بلایی که سرتون ببره، آغوش گرم آخوند رو رها نمی‌کنید!
شما اگه تاریخ خونده بودید راه شوروی و کره‌شمالی رو نمی‌رفتید! راه
صدام و بشار اسد رو نمی‌رفتید و چندین هزار نفر رو دو شب قتل عام نمی‌کردید! بی‌آبروهای تاریخ!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5212" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfMltwoQfwxxDw8AJdQQIezcF0jiR1qIg2-CHDW-DSQE-u7NDOVLJ-R7y36GeuCs4S2GGWMYietUEiAX1tIpW-MXeG-4tgkmXKwD_M_VzRsfkhq2HD7Lnde4_gnQi_k44ISaU63aMuFan6I3eHNw_qwt-zKTCpGAw4F0g1RG1oDk-NJcO40HtWiPtVEX0krPYoxoepRHA0GUlyTsRF1wFnPg0Lx_lq73V0pMhvPzY_COUMdlN5GThOhhRxW_zkolB_BwZn4peuaCLw-f7TJBZpFiEtKGwKKA_11x14sNPrN32F2yy0RQJF-kpLQGwFg_Im1IksxGPXvbB_GBfFD1_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5211" target="_blank">📅 17:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caLuxa_Simk3Cw4csOecgcSHsimLdE4toyHszxBRFTMJWzDvCIZgxrzYmJPOx7tn-h10ORnp5_fC3XUkl-3gD9jX4zfx4PRRxkECXrZ3wgfSW6tzxsOT2iW7g1gK-nfIxt6GHI3I-eBabbDPIVknASBz0-Ev8etuaPN1I6E2QyYS_vvjqL_g308cErW51zt4ZPwVjz0FOpDSvMS-60HZAfMMwawRlv9AsQNtuiIIpjCUKsKsNy2_ddS1KGqfvILEL2wDX4e22XUJX5l5NLcuNMGRFKA7S_wJrpaSO7JjrljiMm7tXWVz_Vm5GgZ_A0IDJUlq-BHNe936qBRYr5gAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5210" target="_blank">📅 15:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2V64NJhiyZCzuwSxHbVRLARvIUcIE5Fn4aT3cE0PaB3F6YGf2m7OGkO714NatOsxPYo5Xp8jIUOgLiPvk1-WoYInqf3Cmfceyf_M8gzrAUocg5Q9Gevbz4V4c8DMplJH7SDsJ-WnHSQvlqCmeBwzlV4HU9PkeFKi2wo2UhltOmbHqZ7IOJSQk2Ua2O23W7fbFSDtVnLSgHHoeerux9inxwcs0VNWRoV9Ot9wBhYvLMmJEOB0qvh9gFgegbPjwdHSpHarPN8ReOhS8A1qc6kclW2g5gei5FJ0DQ7Ic2-B7t3DD4Ch0Ko2cEdrK97fY7fKf7qXTywJ3-nB1jJDnuMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل قلعه شقیق در جنوب لبنان
را تصرف کرد، این مهم‌ترین پیشروی ارتش اسرائیل در جنوب لبنان از سال ۲۰۰۰ میلادی است!
گروه تروریستی حزب‌الله لبنان،
بدون اجازه گرفتن از دولت و مجلس و ارتش لبنان و در خونخواهی خامنه‌ای،
به اسرائیل حمله کردند، اسرائیل نیز در پاسخ دست به حمله گسترده به مناطق شیعه‌نشین لبنان زد، بیش از دو ماه است که حدود یک میلیون شیعه لبنانی آواره شده‌اند! بیش از سه هزار تن کشته شدند!
چند هفته پیش دولت لبنان قصد مداخله داشت و تلاش برای «آتش‌بس» اما این گروه تروریستی و حامیانش مخالفت کردند و گفتند که جمهوری اسلامی باید این آتش‌بس را برای ما بیاورد!
(که بعد تبلیغ کنن قدرت ج‌ا بود)
جمهوری اسلامی نیز توقف در جنگ لبنان را در صدر خواسته‌های خود از دولت ترامپ قرار داده ولی هنوز به تفاهم با آمریکا نرسیده و اسرائیل هم داره کار رو ادامه میده!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5209" target="_blank">📅 12:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=V9ICB2BGoJTVFg6AVe-sFzjo_PXlMW9iYDa726mI0aa8aqcXtxHBn6bo_4Aqi_YGyowAtW8Y0cr-VBs4PTl3BzZ3GP6CSos4p-JLS8YDrF5Vy61GhwgbtsPeRrTEIOZUPHJS2qtAArrm9Gq-A6yBoL5Vyu5jp2pWAxd0_QS-Qk4j_vMwWwjSjRjcxkQOqjTdbXlgrJbNecBCUFejjjrDOjX1kkNGhXSm2ZopPLhxlKLhhMUtH7BZYvaC_SC-pjvl6di24E_hoO7ovhdSGogh9H-8dTIekMOr4ipwou8aBb4-11V69E_VhctS8TXXGGzpm_ay9y-ftgeoDcjW5ofwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c1b13d62.mp4?token=V9ICB2BGoJTVFg6AVe-sFzjo_PXlMW9iYDa726mI0aa8aqcXtxHBn6bo_4Aqi_YGyowAtW8Y0cr-VBs4PTl3BzZ3GP6CSos4p-JLS8YDrF5Vy61GhwgbtsPeRrTEIOZUPHJS2qtAArrm9Gq-A6yBoL5Vyu5jp2pWAxd0_QS-Qk4j_vMwWwjSjRjcxkQOqjTdbXlgrJbNecBCUFejjjrDOjX1kkNGhXSm2ZopPLhxlKLhhMUtH7BZYvaC_SC-pjvl6di24E_hoO7ovhdSGogh9H-8dTIekMOr4ipwou8aBb4-11V69E_VhctS8TXXGGzpm_ay9y-ftgeoDcjW5ofwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، ۱۸ دی در جریان اعتراضات شهر قدس بازداشت و پس از ۶۰ روز پیکرش تحویل خانواده داده شد.
امیرمحمد ۱۸ دی‌ در اعتراضات ناپدید شد. خانواده‌اش به بیمارستان‌ها، سردخانه‌ها و پزشکی قانونی مراجعه کردند، اما هیچ اثری از او نیافتنند.
پس از دو روز و در ۲۰ دی، تلفن همراهش روشن شد و ماموران حکومتی از این طریق به خانواده اعلام کردند که امیرمحمد زنده است.
خانواده پس از این خبر، پیگیری‌های بیشتری در دادگستری انجام دادند و آنجا نیز به آنها اطمینان داده شد که پسرشان زنده است و حتی برایش حکم صادر شده است.
امیرمحمد دانش‌آموز مقطع هشتم بود و خانواده تلاش کرد از طریق آموزش و پرورش نیز این موضوع را پیگیری کند، اما در آنجا نیز با پاسخ‌هایی مبهم و با برچسب «پرونده محرمانه» روبه‌رو شد.
این بلاتکلیفی و بی‌خبری تا ۶۰ روز ادامه داشت؛ تا اینکه در نهایت پزشکی قانونی با خانواده تماس گرفت و اعلام کرد پیکر امیرمحمد شناسایی شده است.
پیکر این نوجوان با کد «ناشناس ۱۱۷۵۴» به خانواده تحویل داده شد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5208" target="_blank">📅 10:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=jfDAgtGSkD2tpCfyyBq5PUC-hZ8ROM8_qNdFiTPPf8AEI-xSeAVt2oNNvxQTulWRTuf_lgtAW4K2D2lNebFlgPgw3qvLIvEglwmQPJpqEPUQC90-TZ5AKV7Qq5tp7ANgHTBtK5XMT3ue9fY9ev5M0DjvVK7lkSPTnyE57v5wAsARym5hbC2deUp9Hqai27HmIb1-FL0A4oSGafVxD4tYb8A2jN1Xcu3w5txSem5LPffahHU2r93e1oPfTq8Mf2GDuMxzhZWXyUAGghUkAu8SSu2Yp6eaLpwsGg95IfyyetLJAembxxD_DHMgM4RxsCpJyFpF34Nkrn-4c9yndGfjTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afd0458a0.mp4?token=jfDAgtGSkD2tpCfyyBq5PUC-hZ8ROM8_qNdFiTPPf8AEI-xSeAVt2oNNvxQTulWRTuf_lgtAW4K2D2lNebFlgPgw3qvLIvEglwmQPJpqEPUQC90-TZ5AKV7Qq5tp7ANgHTBtK5XMT3ue9fY9ev5M0DjvVK7lkSPTnyE57v5wAsARym5hbC2deUp9Hqai27HmIb1-FL0A4oSGafVxD4tYb8A2jN1Xcu3w5txSem5LPffahHU2r93e1oPfTq8Mf2GDuMxzhZWXyUAGghUkAu8SSu2Yp6eaLpwsGg95IfyyetLJAembxxD_DHMgM4RxsCpJyFpF34Nkrn-4c9yndGfjTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5207" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkvqmzgylmQruPdxzVq2Ekq0YANI4gn_3Wyq6EDotQClk3KSKNU7sbQOS1oj2zUYGuG5NTlik2GnsGk1zn85qidfgYhlwnGY5-FeR3pIyuswnS9pQXpu0INBSe_RdAktKe2QQAVNeTtaXSJiLa6cPSeooiYvHXkTrVLU8ei-KfM-55RZVTU32Qkrb_kpQw8dJUajCnXz3EFPAnuKUYAB7xkLtqW5TYr7Y_WCjsrET6V1uam-7eUz87spgPU24Nt1FiR5RQ3ypHxYKDx-mMDBA5c4wWz4_2ozl1_0fQa-Spcqg_nAlKUxCXCJHgzqOCilFGYEaRZgFsZZ6rHZU-CudA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doi5aYCENnHiiDOFmisYwTOkehDAR0wi51NCqrSrRZAyBXt7KRhyb4ccR2S9gBoZdgobTO_yFJc6GV2v6blSYprCVyhLMoViqT5-cUOygdEZcH7r04ajqEnLtrzJTJnGMW9ClMF-Ts3SM8VhIgBMI5R6R90Y8ksl-kq0QBoVFaAEHSTgqR5Q1G3W_Jg-iLrWgthCbIHnXK0k2N0aXXRboprnATl-ubegcZyW3IVkKjFYblWnwZJBFcP2AqW0yPOB6D8vv8FShx4gHLKjH0Jv0g2nUHc9si8IUCLzxSeS5BeRbZBr5thzO48HQiW0CYh789e4Be0O-JKCp7-85Nm48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmTNLVo4GZGJgp1rHXjVCa4jGVuBgpNcauGz4SXRD9Sw_L4-RIfV5IatWiPj4hQb2jUT6PH9rukjlxSbZ8X6t8Hfv1620QRk1xXS31Z7hN8q-GnxRRfVl-CC8rHTEHPJoZHBcVgRNu3v0B3Wr17d-ah8vwTj_XaoEwgQYqsu_XhfFwTiIyQJYIKePvat_URu8i3qz101WpBTtSB2y2GRHWE6PMH7ZSWZ4QBVqOTI5CCcrSehTaM7PRJpYNXAfRKAS-lnJvezGLB9KWrKb6HTlUJ3aWEekhHyBuaQSG1TeBLnOSXfJ3O5E_NBz2iT3FKRhdvAgzC4re-Z_Cdn7mukTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0Vq0yQgCdszZNKArtUA3xovFGyACLVv1CEN1sQdnimtcpQX1k4aBVDQVB40wvlGw_dUseViUWPsl5I5qVfkaxHIzbrkaxvu3fJkBEG2ZAGMt8xs9mef28x8cKzhQfarIRE9NmC3sxgLlL7BlQ_XdQZrTMPeSQEGko2VwrjSf9MPVkzSD9RarP6uBqIdWcpEX_CLzySrsP43UDGgUlQkqFPsAWuqXcGFhymHhU3XIw3V9X_td0yzLM2nUpWb7uEsa-5p-egRNApBWCGW0mIxqR1wzji_Y0g7XItBzEKi-GXh2pSk3wjbnVoUeqxt_A6Lms2JE_FgGEtxv3WARm_UkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voeBIYt1HT6n791M6MzQYGJh2zw9vX-wEOxDyWXSTFSvw-5VEPAZG_rsFNGs5_Ao2VmNmTiEuYg2ZTo5KOOJwXq6X9jZ7WubVkWLq6R1IRL2vUjhDVO4WOt5zFhkpBohkOYdZVp7JFQiEW7b9tTehoqDOxM4Hjwj8digO7g28NS8ykR5HJvvBmj8BcqC6hCKllSMO-zMIptJi2ixuw-KMWSfkLMz7AFtsc5B3BAHa1Lto80WzJVbWt3B-_N3iZ9XNMRGWEjYQy9PZyx4aV2PQVvptB6XKAeUtkUjhzYRYDD1BYnFcxIjvwrq8So7YwJKMx-l0wWqY-CGaKQM_tZ7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1fofCxpA55Pma15re7RGYtvANF8-sR7Nv4fptG8EX83D4PuYmhJnDDXicegH4bawxkmV02rYiT5hKwqByteM6W6A7LuJ5fLXxSNl5ZQDgpZf0kyHEdYu5ydZXhZg3ZD7VWmBcFNKTNl3pnojbzr3tZdPsY743DGjJGQeUMuUC9Y3TAgw-3Luw5-vnEC4klHdTWRNcUWravIeEJLzos0-yJsxknLv7KpAFFaPTY3qZrlLqngbZezlUmeVpmwBEa3gt9sYmgXjCiH3b_pRhqocbkuF_m0LMCaU21ufelwG-KgsX90PaSAIxfFRPkrkL6N8w0Ji4WQWDiJBvsKOwLNrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cN4BsJPmd7MfsCkxp7GearMqV4B-8zEfWYuGdMbzdhwuYh4_38Yg27NI2iKsBEqjzJgeIetuVqe_haOjUZpxpU455XrtF9gCNM2ahJmvTuP6OtkeMAWJUv8oyB6XppbYd_mRhCtShIdXF4sAqcFzCoBDx5He1YYN7Lz6ujlRdY6IhXOaN3sOg3NPexu9D_UxCl85LkJC_1sVHd7Y7K01qrFD4WJmP_UdngeH8OEBsyrf5P3fmCAr3ZChQTRAx1zBITj_BFfqjZUT621Ze3DCHifL8z5lXg7j0UkECrSe5bk6bAZu7uxGDR049DOz-cIFXGNQFwHg6MAkZAhIdOLewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYSw-59rh5XkCrtqXsHyHHOswS5mI_oWo1CZz47G4NGwxwDVVgh1p8a2feyRMcXOWAxLjT9rW3oFe7l8xprWzOrjPgtl17StU6wkKiQtTTaOFU0LI0bqj2W59OQghrJW1ix7gmI0QiXtw88R9y0CcjsUASfz0xcfUtiCA5c_PCc0BEOOra_OSwrMTZdoRCCzgxovllL2Y_y3B-BwcIhtzHcv_xZdtfO5K-VvxzJ3enoyAYYxCL5_aHPee2ZWVWEjf4RzBmpNafeq6NZJSBnIYljOd30CDsH4HlozfhNkc6YEiGsb-_uqNGmvMOJoO6OrqlUwd3Mc_EMy22XSAcWRKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=XE-WMXtSATg14VawAhLMEcSI8kzpu_CKYVzpI94ePQBgg1rnQSQkL8a19atTfO1263QPjwOfyYxZeKTXZNi5QtxuDbqWeCmTqD7PxRRHq_DlfQM5LdIwW0tnq0IzVbNTTvwttGBzjNDDFdz6_kXasEsw2rJhEZmwpSEOOhYqo8l6O0ksj7AOd7flRy9mTjVEAmOtP5AlPV9WtCJNkBqqoGFonQkCEbHWk02W7VG5awy26gIizC8BgPbHaPDL_oWzJw00LRHHcuMYo28rVo1FeOKxRaCeXY_jBbA9GJ5SVcUh1nCTYxqpkvtw2XWe52yRDAt1hSTPNpxwru5_gv5Zcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=XE-WMXtSATg14VawAhLMEcSI8kzpu_CKYVzpI94ePQBgg1rnQSQkL8a19atTfO1263QPjwOfyYxZeKTXZNi5QtxuDbqWeCmTqD7PxRRHq_DlfQM5LdIwW0tnq0IzVbNTTvwttGBzjNDDFdz6_kXasEsw2rJhEZmwpSEOOhYqo8l6O0ksj7AOd7flRy9mTjVEAmOtP5AlPV9WtCJNkBqqoGFonQkCEbHWk02W7VG5awy26gIizC8BgPbHaPDL_oWzJw00LRHHcuMYo28rVo1FeOKxRaCeXY_jBbA9GJ5SVcUh1nCTYxqpkvtw2XWe52yRDAt1hSTPNpxwru5_gv5Zcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=CTQ3IhhWzvVznVTsWpEeYUhDKIWe8ZADEOp5P9gW4GtAh4Q3s-9sU4A5wBvGv-RmL0qmblIpgPf95EHVB5KTx-t6FjWmWjf4sbMfwaBT3IZiXQ-0qILn-l94LBO_1vKzhMo35xQz6n3_QbxqU-9V-tQ0ycst1tKvPNYpqvNB3QkYoO8yx4DhRaJN2kPr7MAwk_urpUTDhxasQUdS5aobP9K6NqVynhoU8nI01oEfw4ZuRXZ0npbQh7fV6-Xs4UZR9DRVLt12Rv5jfvWdRmqcwpDlnu7qAvItZ7eG8urs1KrfNgXzc83ylYbeNn97FeJ9Zv1dykAiPEhFWZOUXmCEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=CTQ3IhhWzvVznVTsWpEeYUhDKIWe8ZADEOp5P9gW4GtAh4Q3s-9sU4A5wBvGv-RmL0qmblIpgPf95EHVB5KTx-t6FjWmWjf4sbMfwaBT3IZiXQ-0qILn-l94LBO_1vKzhMo35xQz6n3_QbxqU-9V-tQ0ycst1tKvPNYpqvNB3QkYoO8yx4DhRaJN2kPr7MAwk_urpUTDhxasQUdS5aobP9K6NqVynhoU8nI01oEfw4ZuRXZ0npbQh7fV6-Xs4UZR9DRVLt12Rv5jfvWdRmqcwpDlnu7qAvItZ7eG8urs1KrfNgXzc83ylYbeNn97FeJ9Zv1dykAiPEhFWZOUXmCEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDEVISout7HgOUuycIar-pUSsebHvJ_5Fp8FgxUJBwGsYa5y9gA7QJwt0PqACZw86eOS5Br7eAkhZSGG2S_jthqBjvLGqWBsfaX2VhHMGQBM-fvjgzJSLjP2wRvqzKHFbwX8QmVhhBTFRw3M6cd7L2tZ9Df1E8BOAv7Z4P49k2ogPbXtnOK5rNTSFBcGjIU4rVxQYYwQLOHUghgwAlRcp3Eo6i2ngpEDqLR0WmZ4yrkEikOg8TBJvFfEJyK9iP8kTBS1uD-QeTxKk2Shp3FRC8101kPFvhxEmUZGioQeOXT4QNIVb_APTyvVCjCxwqwn42esvGGe1wEaaUPV8U-FZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG5mGDgFuL98RQPHEd7ZrqVtsTTbqoGWbQqBaE45WLQ433r4Fapwzw2JOfYX6RMmL7ivpJZ97kUZT0_UNcjTQS0tv7YElFWnMTxG2z1GxfzZn_1cxP-74H3p3WWUh6tXhdOGQb9lcXW21uY2g4yjkKr5hHpnZI-jYWCJwGaGtwXUOYM1lWvDNmPg4_TUUoub9eNMysah9S_0UD2fa3D_REBBVk4JcN2K-AEDmJ6mCYsjQyza_Jz8g42XjTi8MT6-WMdypTNUUzZX3ig9-WQWDK3XnZbAkkfqwCdL4Q3SIi6wRwELQKlJg_5ujeFicC9GtSgQ5ixrrSn9nqEdHHl37w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=iH04F8KjpnCCpbVqhRCgDOMXb5LggD-er2X99sgOZgW2IKjb7uMHmi60YdC7NqpkL7mAKbJ6qGZW3_ZWE5XnhKbRyZzcjSdxpqDa-62UqbuicL-UzqqABjM_wCaJM9s0_bCnlcTAY7gFBOqOmYIye_h_QUSDJkP0dEqj0BLdd1Ls_5OT1R3bK9VKtqbCgPAOla4YHYzrar8nHOIKQeKxdL7iDraNtSe2GO_GQf82SJ_v2BnugOw0osLhVeOVpGTE4JaD_yp_meVjBn5cntaGZOwFc7pnDHT6n_pzi-Ny7QwQRXRLlc6ajBzwF7BmYQ6g--cwPL9ANre1nnjvaNUsUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=iH04F8KjpnCCpbVqhRCgDOMXb5LggD-er2X99sgOZgW2IKjb7uMHmi60YdC7NqpkL7mAKbJ6qGZW3_ZWE5XnhKbRyZzcjSdxpqDa-62UqbuicL-UzqqABjM_wCaJM9s0_bCnlcTAY7gFBOqOmYIye_h_QUSDJkP0dEqj0BLdd1Ls_5OT1R3bK9VKtqbCgPAOla4YHYzrar8nHOIKQeKxdL7iDraNtSe2GO_GQf82SJ_v2BnugOw0osLhVeOVpGTE4JaD_yp_meVjBn5cntaGZOwFc7pnDHT6n_pzi-Ny7QwQRXRLlc6ajBzwF7BmYQ6g--cwPL9ANre1nnjvaNUsUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjtRPFaQsoskPZcVaFX0rfrTdGUzlgXwVWgzA2Bf43rMja9LwAG7MVeS-bTy5zUjOcIdMjeF0wXJRn8h-17fdRRWMTF3qt2wvvCeF4Bf4481GS5rSJbragtUxFN3CiH9kgqVgNnjNH_nzVldsBmckc2Uhcx-1F4AHumNolESzC5ANwOKy8YIarVezSAiN7cI5VEu0hS4qwcjEMe048dP7SgSvy6lFw7xQbiu5I0s4fKb4yneUzO2_svfqs3bwieR6zci_YD_MC2FoqqzNOdre4h9K6cHVIxF35p7gKpW5ZPNPZ8_oALOeJhIrOxvuwlLLAc5_4eTFyx7bqWCeKdFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=JqUokZJMReWhq2u5cv84pfZ5LubRvhhcTut3b21dyzG_mUbP0rS_lTZONC5JQV2Avm9bUTj-r0jIi5NmSEILRh4uYxpCec3wQ5H4Lm4urd48joNuYb72zMyGzuVHd_a0a8Vj6TenOGFZeP-hYzV2l-Jq2qk15cn1hgZv7mMNuuA69kEEmYbdMkZhmNy9SxCmEM4t2SDAhf-Q7_pbCkzWUAL7_XWSxdRTzUUspaTh6olslAkaykqFgnQ2ZcLH6sORgITJez4W0T4d7FuXfUTicyMfKoesI5YFFQpkXvR445ZNMwgGwdvvrNzuvjy0TdRxYa3GK5OxE-v5yfEXeBZCtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=JqUokZJMReWhq2u5cv84pfZ5LubRvhhcTut3b21dyzG_mUbP0rS_lTZONC5JQV2Avm9bUTj-r0jIi5NmSEILRh4uYxpCec3wQ5H4Lm4urd48joNuYb72zMyGzuVHd_a0a8Vj6TenOGFZeP-hYzV2l-Jq2qk15cn1hgZv7mMNuuA69kEEmYbdMkZhmNy9SxCmEM4t2SDAhf-Q7_pbCkzWUAL7_XWSxdRTzUUspaTh6olslAkaykqFgnQ2ZcLH6sORgITJez4W0T4d7FuXfUTicyMfKoesI5YFFQpkXvR445ZNMwgGwdvvrNzuvjy0TdRxYa3GK5OxE-v5yfEXeBZCtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=U8v_85n7ST75JlZO9gTSisqWfJpCPS0hwMqoGMwVMYWCB2Lws-kvl9TTq_QPXfhdrVFP7_ljOj7o-5bGUzZE0AL05ksvmVYf8qFo8yWnxzSPwRUCVGVKaCJSRrWMU2YuWvTZlSTxEa73VfkZfPuvS_Kv2FcOvj6DoTnam-NAFFbyjxW5QlsU9jmEOXT4ECkLClL8FD5vng85HSE3YpLXY_1V995GoaO-I_HfSlJAWoxAzu-cxqAgLSIap-YLgXOigR9FWUa8ZQCYkP_MTo1mYd2fFk8KCP7svo5zqVwIRIriu0xpHeIchnJRjVNAOwtU3pE0CwMPEyNDyTJBQ-zn-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=U8v_85n7ST75JlZO9gTSisqWfJpCPS0hwMqoGMwVMYWCB2Lws-kvl9TTq_QPXfhdrVFP7_ljOj7o-5bGUzZE0AL05ksvmVYf8qFo8yWnxzSPwRUCVGVKaCJSRrWMU2YuWvTZlSTxEa73VfkZfPuvS_Kv2FcOvj6DoTnam-NAFFbyjxW5QlsU9jmEOXT4ECkLClL8FD5vng85HSE3YpLXY_1V995GoaO-I_HfSlJAWoxAzu-cxqAgLSIap-YLgXOigR9FWUa8ZQCYkP_MTo1mYd2fFk8KCP7svo5zqVwIRIriu0xpHeIchnJRjVNAOwtU3pE0CwMPEyNDyTJBQ-zn-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=FLFDgkz_MN63GhNP1JMvqasnSHEDZSIsYCobxIyKWzxsd2u-gXlxifIiW_lSG5wPYGP5TA3jLmrc-Dx_TkCxQO79kr6G54JHA7BCaSzeSpyfq1g7SGutojdlntPeN-XrkXKLTkbgMY6BmE3ucwHFGYLgT_7Lqcvzpxkw2rz7aFN8Xo6EZfNabyRY1ax751Xbc8xu3lLnOEqRVfNSaqNfpdnrfRNIVG8eURgewbXGhVBuPUKYgUQUuqH8TE67PT39Num2Ev-0Z0l9njbt00iA7qywE7iQZOjLfcPI7VilsXCQy7MBwZHh8FEPAvD2rlzWjuDn7qpWISPjzZkdFEZxIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=FLFDgkz_MN63GhNP1JMvqasnSHEDZSIsYCobxIyKWzxsd2u-gXlxifIiW_lSG5wPYGP5TA3jLmrc-Dx_TkCxQO79kr6G54JHA7BCaSzeSpyfq1g7SGutojdlntPeN-XrkXKLTkbgMY6BmE3ucwHFGYLgT_7Lqcvzpxkw2rz7aFN8Xo6EZfNabyRY1ax751Xbc8xu3lLnOEqRVfNSaqNfpdnrfRNIVG8eURgewbXGhVBuPUKYgUQUuqH8TE67PT39Num2Ev-0Z0l9njbt00iA7qywE7iQZOjLfcPI7VilsXCQy7MBwZHh8FEPAvD2rlzWjuDn7qpWISPjzZkdFEZxIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=G-VZiYjJtfN9LMM1y9LoRXM2IHhpCaZo92XszCqIYcCZ6O9r5AmNAxJMtGSjcSZgbSBASLFKuT-_R32QzYlNYpxpmq6gDH9xZg0Yep-78kFkUgoskUM4c17_sLDB7gKYH-k1AGkMvi3MgJQ7f1eB7XF3Q6he9G_sgrxtpjh6Hwbayr6_S53sKlfscYBjKCOZy8z3-o4ZMmhLtSd68hpyiSgddw08ZlMAyHkTM00EKdLwvUvUa0qlxiH-pmh0Z8NAdwVFAlRH2u6CghDfo9q68K7DwbqL-ZEI71KWIS6jdBl51hFJ2HCrNgqj0t-xtYdClbPMKG38Wb4lTs8OIMz4tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=G-VZiYjJtfN9LMM1y9LoRXM2IHhpCaZo92XszCqIYcCZ6O9r5AmNAxJMtGSjcSZgbSBASLFKuT-_R32QzYlNYpxpmq6gDH9xZg0Yep-78kFkUgoskUM4c17_sLDB7gKYH-k1AGkMvi3MgJQ7f1eB7XF3Q6he9G_sgrxtpjh6Hwbayr6_S53sKlfscYBjKCOZy8z3-o4ZMmhLtSd68hpyiSgddw08ZlMAyHkTM00EKdLwvUvUa0qlxiH-pmh0Z8NAdwVFAlRH2u6CghDfo9q68K7DwbqL-ZEI71KWIS6jdBl51hFJ2HCrNgqj0t-xtYdClbPMKG38Wb4lTs8OIMz4tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=cS2_28iSaEKPhJzaaCZEbEQL-osj-hN6AklabWTZfWwi9Ram1A1ZQYUpzV74QVklsPP6JCQxLz-Uh059xPfXWYeM6ArOKamYwWF1ggk8pfcdh1aD5_ys3UwJiMb6JwMWVyhQ_xQ4m27ToCquV1v2KLuPA818qZCX29-ak9KFhCJNSma3BmwGGzq7HswmbVyDu1Bt2bX-nNroiyVBzUKRdytRwD595LkQdbXJ-CMkGU4M9ugvwjEkbOAT2Hk-JsDAxV3299dtyaqQ2cYZjQQzvrT5qEE0fFYLvgBkuMOEvkxmON5F3xWzyGqOh6aNi-VIOv-GbOEbweXkbSHWC8nx3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=cS2_28iSaEKPhJzaaCZEbEQL-osj-hN6AklabWTZfWwi9Ram1A1ZQYUpzV74QVklsPP6JCQxLz-Uh059xPfXWYeM6ArOKamYwWF1ggk8pfcdh1aD5_ys3UwJiMb6JwMWVyhQ_xQ4m27ToCquV1v2KLuPA818qZCX29-ak9KFhCJNSma3BmwGGzq7HswmbVyDu1Bt2bX-nNroiyVBzUKRdytRwD595LkQdbXJ-CMkGU4M9ugvwjEkbOAT2Hk-JsDAxV3299dtyaqQ2cYZjQQzvrT5qEE0fFYLvgBkuMOEvkxmON5F3xWzyGqOh6aNi-VIOv-GbOEbweXkbSHWC8nx3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=o9hLuuWdmRk3oEJmDqZW3H4N3zelsZ8BHDF_MTRF_9bEBFVpnainQkUY-r-bDmsJpd8mev4KwyCW6WalIBt6ySkytyggOfGwHShtCBxS5Llo8593RiOEzJnTCzZn4J_gFSXDOg9wc09EhkZ9eg776D_nrd6QTJgp5n2tDMguT1fzo_h2q4Qxx61ywhCgpIT3a7FcgaqRiDoL15A1ZjVtxhoDnvwfCyFhDW_qIXE7m_qjNI9iUrlDQPeaNcFZsdy-34oX51s8sAQGLLXbnfRZoNOLOLzThCKW9ZaeZR99MdZf8r_pVu-T7STvap4KAVAuFHQ0HDPu2QfHXxAsh-nqcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=o9hLuuWdmRk3oEJmDqZW3H4N3zelsZ8BHDF_MTRF_9bEBFVpnainQkUY-r-bDmsJpd8mev4KwyCW6WalIBt6ySkytyggOfGwHShtCBxS5Llo8593RiOEzJnTCzZn4J_gFSXDOg9wc09EhkZ9eg776D_nrd6QTJgp5n2tDMguT1fzo_h2q4Qxx61ywhCgpIT3a7FcgaqRiDoL15A1ZjVtxhoDnvwfCyFhDW_qIXE7m_qjNI9iUrlDQPeaNcFZsdy-34oX51s8sAQGLLXbnfRZoNOLOLzThCKW9ZaeZR99MdZf8r_pVu-T7STvap4KAVAuFHQ0HDPu2QfHXxAsh-nqcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
