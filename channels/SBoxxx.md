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
<img src="https://cdn4.telesco.pe/file/toS-3r9JULwgq0mtrAOqJDugmd8LDspRwUTrGOFLhzFGnCE05brP29GW9LCPYBlxBNXxTDqz7hdS63gLs25IpCjKSmGxKDPqhhW8mPKpHEbnWovwaGwpWs8vQ498xLKGTxNtDGgYXtvZQtFZOZgIscUirM4BF8h89bTz-8Pxk1z9xUZSULNgeGYXQ1mxI6UZIyVtD2IGNAFV0bfDahdQx39rKLvfqC9BslTffmP2X6XRDfH_hCdmI5fdiEiElX1_V3JdUfl63O7Zn17hGQntPwm3Zpn6HC2IM6FCknJACSSFAZ3L1NXeygKKHcCfcruec3b6bOH0fBNiBX8NC-xOVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.86K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 23:31:05</div>
<hr>

<div class="tg-post" id="msg-16812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGLzXYGGhoXFdnUEunpaHvw2gxW99AS3cBUHJXxYAigcWTo5Sj7l5MWexU-lMNl_2XD5Os1I55xOWBuKtFKeElEWdhQQEbqCl44YESM_MDBIP4UP9CYZYEI-5LQAB9pyniKKT1k0ouLh7RJv06lyUC5elfM74mwSMlfCFZsp0ZbUOAtwKiCJV0RKNUE8hmUCTX8YfII2QxV5KKZD9NiYbAQp5C1axtCHagiHvelfOuAFGsowtICYNFsUaAcmG5enx4izqLmem5JVpXzzYBKLzXfS8nYf9qMQopjWRwBMaZM7Q2SjwELlJ1ejrZpXPe29DDAU9K5VDU6IDDGZlHTWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جنگ در جنوب لبنان!
منطقه بنفش تصرفات اخیر ارتش اسرائیل
منطقه سرخ محدوده بمباران ها و تنشهای نظامی</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16812" target="_blank">📅 20:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16811">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بسیار کار خوبی است و باعث کاهش فشار روی سرورهای پورن هاب می شود.</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16811" target="_blank">📅 20:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16809">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLEPJ8oItoDifLP1v0YJ8zm72w6mPCotPuAY6VSBtvRqTLASlVnCbDchfZEKSIJ4FcGXHK-gAyakEjKbX74f8vIZpF5xISU_8dg6QQVIJCaEfzJr-FNqmHz5ieL0zWuKVW-x_kUWjkGGn_YibZwhhA-vtoW5CYnrLM9CMUKNR9oKTFZ91uIqU0GScgOg6EGR9tC1ubQnveprw69MT5wFcTF_BE9dIPsf3XTl1FntNzgiB_rT4qhI0rb7BLiRzFAIHLor-kUjfM1N7dbtoqmNOuuwLjuzNOnFZr-jikVg2Ds9USlzgG_T2OigCHYIHEbadno8QQ1TngMq-8S6P1V56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JObiMz8diaRbXxTsYRedEdY1kP-gxjtivcx8IfoUnAbJMiOcy6Ux9C3XuUI77yp7d9IkmcnQmHH5Ur69AZI6VgWNZKexbW2Y5V7huS73fvVwso3xu3wwI8fvLHJTc-5iWDJGl3Gu8OguE8SuYJII075InqFRNhMm7a4kQfUNQO4079TbGjTJtTwRqJDtvWZ_X_WtTkcsQdblnobeGzp7e8wqUpXhGdVyylwtIlbuvYeZp63q8w_dPfnDHw-hGWTNCgQsH1c9vsUIQIgnGSo0QTzOlJKACR6eX0He6P1BR-G4egMEv6Ci3d5oVrmtcxB7gnUMoTKdj4BaXPdzU0TDhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک کمپین عجیب در خبرگزاری فارس
گزینه «قطع داوطلبانه دسترسی به اینترنت بین‌الملل» را فعال کنید!
ایجاد کننده کمپین صالح اسکندری از موسسین حزب شریان است
@kakhresaneh</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16809" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16807">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16807" target="_blank">📅 18:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16806">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn5CUji7NbgCDh57xgyOhlUeOgKz9gpMqUaR-HgbmNw-Q1uONaDngtrqH3BcW6-QRwwWgCbDtB4KjuFKgtDXO066_r6qAxZCLAg8dRdyXdAVQuCkIHdOGudfDdDTOahT38nxv0X2bLuo9eUexufnw8XIjeD0x5OBZeOC129L7LraXSgifNSAAob8AFLJDzlrXdX0KXjFOU8MxJKSPHT7rB4LleP9gS2WXAUm88PPTVgLR7DOYIe1NfNBz7nCd6Wm3-L36IAbn_fKJQTa8gA_PBk9-c7FZOMtPx7p-uuhpaizOgmGBDy-tUEk3m_gC4ZIsKSL_DfQTxALMipCuAi_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ فراخوان داده به تماشای برنامه امشب مارک لوین که از محافظه کاران بسیار تندروی حامی ادامه جنگ با ایران است و اساساً توافق با ایران را بی معنی می داند.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16806" target="_blank">📅 18:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16805">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دقیقاً توصیف موج 4 به زبان ژئوپولیتیک.  بدترین سناریوی ممکن برای روح و روان ما و برای رشد طلا و دلار در داخل</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16805" target="_blank">📅 18:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16804">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzsKAHlylYgs20P0vovCGmoVtc4moGNkNU8cTNOZCPT9KW-ryuRoy_oSWD2tphW_QM5FN1ERrd3utdipwutHErof4JnvTvIR9yMZDY3gBd5dsliV9BXaoNTLyqFiIJKYaELVOkbrZM4CYX-H_1ZiX7UvRXt1oTMyNrjLMfOaqEXkJGh30fJiKSFh2xY30_FCAnU0kubn1p1af8oYEZ7g3cH-pzADK0wf6RQi924NrirxI-ioazwhbvG0Pom7huQ7sVFi8CP8qcV7IbBfShiHL0rLWp24i4yT7WQf3tftitEAwLUQ2ZJM0NgdWWq3ckR1mY_BkdvDr9EbKx2BdE8_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش گاردین، در انگلستان، سه نوجوان مهاجر که به یک دختر ۱۵ ساله و یک دختر ۱۴ ساله تجاوز کردند، جریمه ۲۶ پوند شدند و آزاد شدند.
فعالان حقوق بشر انگلیسی نمی‌فهمند که این چگونه ممکن است، زیرا حتی جریمه پارک غیرقانونی در بریتانیا ۱۳۰ پوند است که پنج برابر بیشتر از مبلغی است که نوجوانان مهاجر پرداخت کرده‌اند</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/16804" target="_blank">📅 18:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16803">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696ee3bdc6.mp4?token=OQZhI78zXdXpuDMHoa0UIDWEcxsvpscScE8KuTUyAKnj0afkAimw5bhW5rKzktY-2RJdk2TMmNCgEgctV_I_LRMebrQMbznY_zzkFiYYCXc4_-j8mg7EhgO2j-BOYgzaukkYVvGrOCvxdUGNeiEIPcC4F_R9rxzBvBTKEKPlJQHQZE3a9ruQwjbcjI9ZcwZYHJ_DwcV-sspcQ4M6fIFFiBazNmQBaJC34GkHk4ZxgwpHU2JujUsSyC45p8569UVvbjhgfzKrl6exh2emeAs73lyCGiIqmZgxmxcIomCDZpEEcjILGVtbVdFjQGO9-hp6CXfpPTiWuDz65ylnP0vtfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696ee3bdc6.mp4?token=OQZhI78zXdXpuDMHoa0UIDWEcxsvpscScE8KuTUyAKnj0afkAimw5bhW5rKzktY-2RJdk2TMmNCgEgctV_I_LRMebrQMbznY_zzkFiYYCXc4_-j8mg7EhgO2j-BOYgzaukkYVvGrOCvxdUGNeiEIPcC4F_R9rxzBvBTKEKPlJQHQZE3a9ruQwjbcjI9ZcwZYHJ_DwcV-sspcQ4M6fIFFiBazNmQBaJC34GkHk4ZxgwpHU2JujUsSyC45p8569UVvbjhgfzKrl6exh2emeAs73lyCGiIqmZgxmxcIomCDZpEEcjILGVtbVdFjQGO9-hp6CXfpPTiWuDz65ylnP0vtfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال طول می‌کشد تا به شرایط قبل جنگ برگردیم
💬
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی:
🗣️
آسیب‌های واقعی کمتر از برآوردهای اولیه بود، اما بازگشت به وضعیت پرچالش قبل از جنگ (با ناترازی عمیق‌تر انرژی) یک و نیم تا دو سال زمان می‌برد.
@kakhresaneh</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16803" target="_blank">📅 17:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16802">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیروهای سپاه پاسداران ایران به سایت‌های گروه‌های جدایی‌طلب در شمال عراق حمله کردند —رسانه‌های دولتی</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/16802" target="_blank">📅 17:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16801">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X31hIMnZykfPWG5Cs5ptDtCotKtbB9pmus71zY5thgt6c1W7O388upzjiQa1tgBXOu768S9YdNe9TZXCe5B0LUMF7hO-EBWcQx_e3Rt1rHU7EY9VT22vyymxwLqoYylC2qSY-kh8bM3iQY7zKPiuXn1WicBQqG50AkVW6yiZDFdKTYLBAQFo1hxSRvxd8aG6Rq2l13Ra3ri-We81I6m_O4Wk6jkLL6EX70zeuj3jeCL7_L2oLf3d3MyOg0E0AUo-eqQsRdXFuUyzn9QAwC68E1VpkSTUkNNkHo1OsMEhVVaHg2ujFGOrOpkjSi9TfFtIGMcmRAoPQ_6Ikk2eElkY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
«ما قوی‌تر از همیشه بازگشته‌ایم»
او تصرف قلعه بوفورت در لبنان را تبریک گفت و وعده «تغییر چشمگیر» در سیاست نسبت به حزب‌الله داد</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/16801" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به گفته یکی از افراد مطلع، اسرائیل در طول جنگ، سامانه‌های گنبد آهنین و نیروهای خود را برای دفاع از امارات متحده عربی اعزام کرد و ده‌ها تن از این نیروها همچنان در یک پایگاه نظامی در این کشور خلیج فارس مستقر هستند.   در اوایل آوریل، عربستان سعودی به آمریکا شکایت…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/16800" target="_blank">📅 14:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صداهای شنیده شده در قشم و بندرعباس ناشی از امحای مهمات عمل نکرده از جنگ رمضان است.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/16799" target="_blank">📅 14:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صداهای شنیده شده در قشم و بندرعباس ناشی از امحای مهمات عمل نکرده از جنگ رمضان است.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/16798" target="_blank">📅 14:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پاکستان به تازگی ۶ کریدور زمینی به ایران افتتاح کرده است.  ۶ مسیر زمینی از کراچی و گوادر مستقیماً به مرز ایران، گبد، تفتان، و چندین نوع دیگر.  کالاهای کشورهای ثالث اکنون می‌توانند تحت نظارت گمرکی از پاکستان به ایران با کامیون ترانزیت شوند.  بیش از ۳۰۰۰ کانتینر…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/16797" target="_blank">📅 14:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16796">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔵
اختلاف در سازمان کشورها ترک زبان: قزاقستان مخالف تبدیل سازمان کشورهای ترک زبان به یک اتحاد نظامی
⬅️
روزنامه برلینر زایتونگ آلمان می‌نویسد، مسائل ژئوپلیتیکی موجب بروز اختلافی کلیدی در میان کشورهای ترک زبان شده است: برخی از آنها طرفدار ایجاد اتحاد نظامی ترکی هستند، در حالی که برخی دیگر با آن مخالفند. توکایف اصرار دارد که سازمان کشورهای ترک زبان نباید به یک اتحاد نظامی تبدیل شود. در حالی که اردوغان و علی‌اف برای گسترش نفوذ ژئوپلیتیکی و ایجاد یک بلوک نظامی پافشاری می‌کنند.
🔹
قزاقستان از ایده تبدیل سازمان کشورهای ترک زبان به یک اتحاد نظامی تحت یک پروژه ژئوپلیتیکی حمایت نمی‌کند. قاسم جومارت توکایف رئیس جمهور قزاقستان، این موضع را در ۱۵ می در نشست غیررسمی سران کشورها و دولت‌های عضو این سازمان در ترکستان قزاقستان صراحتا اظهار نمود. این در حالی ست که در ماه آوریل، آندری بلوسوف وزیر دفاع روسیه اعلام کرد که مسکو حضور نیروهای خارجی در آسیای مرکزی را نخواهد پذیرفت.
🔹
رئیس جمهور قزاقستان در نشست مذکور گفت: «اخیراً، برخی ایده ایجاد یک اتحاد نظامی را مطرح کرده‌اند. نیات منفی آنها برای ما آشکار است. همچنین مشخص است که اهداف آنها هیچ ارتباطی با صلح ندارد. قزاقستان معتقد است که چنین موضعی باید قویاً رد شود. تقویت وحدت جهان ترک برای ما بسیار مهم و اولویت اصلی است».
🔹
وی اذعان نمود که سازمان کشورهای ترک زبان نه یک پروژه ژئوپلیتیکی است و نه یک سازمان نظامی، بلکه یک پلتفرم منحصر به فرد است که تقویت تجارت، اقتصاد، فناوری‌های پیشرفته، دیجیتالی شدن، فرهنگ و همکاری بین فردی بین کشورهای برادر را ترویج می‌دهد. وی افزود که کشورهای ترک زبان باید در هماهنگی زندگی کنند و با هم توسعه یابند، بدون اینکه از اهداف خود منحرف شوند.»  توکایف همچنین بر اهمیت وحدت کشورهای ترک زبان با توجه به وضعیت ژئوپلیتیکی بین‌المللی بسیار دشوار تأکید کرد.
🔹
پیش از این، آذربایجان پیشنهاد برگزاری رزمایش‌های نظامی مشترک را داده بود. اردوغان که دو روز قبل از اجلاس در یک سفر رسمی وارد قزاقستان شده بود، اغلب در سخنرانی خود به موضوعات ژئوپلیتیک اشاره می‌کرد و تاکید نمود که بحران‌های فلسطین، لبنان، ایران، اوکراین و سایر کشورها لزوم تقویت دفاع ما و گسترش همکاری در بخش صنعتی را نشان داده است. اردوغان همچنین گفت: «همانطور که بحران تنگه هرمز نشان می‌دهد، پروژه‌های حمل و نقلی که جهان ترک را به هم متصل می‌کند، به ویژه مسیر حمل و نقل ترانس-خزر، برای سال‌های آینده اولویت اصلی ما خواهد بود.
🔹
در این نشست علی‌اف نیز به جنبه های ژئوپلیتیکی فعالیت‌های این گروه اشاره می کرد و اظهار داشت: «جهان ترک باید به یکی از مهمترین مراکز ژئوپلیتیکی قرن بیست و یکم تبدیل شود. آذربایجان به تمام تلاش خود برای تقویت سازمان کشورهای ترک ادامه خواهد داد.»
🔹
این در حالی ست که این کشورها در حال تقویت روابط و همکاری های نظامی خود در قالب های دو جانبه و چند جانبه در داخل خود هستند.  در جریان همین اجلاس مشخص شد که آنکارا و آستانه برای ایجاد یک شرکت مشترک برای مونتاژ پهپادهای ANKA ترکیه در قزاقستان توافق کرده‌اند.
آمو | مطالعات تخصصی آسیای مرکزی
@C5Amu</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/16796" target="_blank">📅 13:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔸
سخنگوی کمیسیون امنیت ملی: برخی اخبار حاکی از موافقت آمریکا با شرایط ایران است</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/16795" target="_blank">📅 13:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFquxYpEiwQXtU0YX4MkFZyUad0LIkYzIQMymvcqBgL5BaiNlkfnFjG8cc7te2lz_IbiUpem1p4L8lm4FSfb2GwzXLXujPJ7UmcYssrc9fodgFo24kK1IGmg-s1omI4hXtlDiuWGHG0-Xad5OpVkuSDB3L1IZaUISkgS4VfGZJbMeeyBF6H9YEj-G6Ec8amXgVIYje6rw1_MUmepUwvzZw-czgvr3mtyoON1d2cnzanQ43wSdW5B8sQyRkIJcau5cBLMg3Zq-k1WfAY_c8kPWKHcdgG8bhpDuAkVHCh-C3nA27YghgWHyXcwHVm9AweIKXC5fd2Grkc4IpAWb0eudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش نیویورک تایمز با استناد به مقامات آمریکایی، ایران نتوانسته است تنگه هرمز را برای ترافیک دریایی بیشتر باز کند، زیرا قادر به یافتن تمام مین‌هایی که در این مسیر پخش کرده نیست و توانایی خنثی کردن آن‌ها را ندارد.  مقامات آمریکایی گفتند که «مسیرهای امن»…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/16794" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ابرت کیوساکی: خالی بودن ذخایر طلا فورت ناکس باعث فروپاشی اقتصاد آمریکا می‌شود!   رابرت کیوساکی (Robert Kiyosaki)، نویسنده کتاب پرفروش «پدر پولدار، پدر فقیر»، نگرانی خود را درباره اقتصاد آمریکا با طرح احتمال مفقود شدن ذخایر طلای فورت ناکس (Fort Knox) ابراز…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/16793" target="_blank">📅 08:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16792">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، یک پیشنهاد صلح تجدیدنظر شده با شرایط سخت‌تر به ایران ارسال کرده است - به نقل از چندین مقام آمریکایی در گفتگو با نیویورک تایمز.   این «پیشنهاد جدید و سخت‌تر» با هدف افزایش فشار بر ایران برای پذیرش توافق طراحی شده است</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/16792" target="_blank">📅 08:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16791">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بن‌گویر: حملات به ضاحیه کافی نبوده است
ایتامار بن‌گویر، وزیر امنیت داخلی اسرائیل، اعلام کرد صدها نیروی حزب‌الله در هفته‌های اخیر هدف قرار گرفته‌اند، اما این اقدامات را کافی ندانست.
او خواستار تشدید حملات به منطقه ضاحیه در جنوب بیروت شد و از دولت اسرائیل خواست عملیات گسترده‌تری را علیه این منطقه انجام دهد.
اظهارات بن‌گویر در ادامه مواضع تند او درباره جنگ لبنان مطرح شده و همزمان با افزایش حملات و تنش‌ها در جبهه شمالی اسرائیل بیان شده است.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/16791" target="_blank">📅 08:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، یک پیشنهاد صلح تجدیدنظر شده با شرایط سخت‌تر به ایران ارسال کرده است - به نقل از چندین مقام آمریکایی در گفتگو با نیویورک تایمز.
این «پیشنهاد جدید و سخت‌تر» با هدف افزایش فشار بر ایران برای پذیرش توافق طراحی شده است</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/16790" target="_blank">📅 08:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16789">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4vHIgYSzneAef8OwtOJFtrD9kuzjT-up5ETcdy_uiwOT2bu11321KoygRCoHufsqWXpdHZ1PnbWJbtRZlye1zaXPXLRjRTWxJp72JZW9VKU-xt8SBPzrV09wDL4-BV3tijf46129aU5o5KFUvOWyntH9_osNeAGMWG0rLuNH-WJGvK1deAUbvAQ8B17qEfz98WROpTOri61fLOYovP_xeoFFtBAwzCXHGtTVfasHdTOUR4Z0U52sopcT0xIaz65EQqkUdUkUPzvPOt1swrf_dZ7VsqAwj9vMkO8voXOd-JG-1Zc-jFM2__0Bgldh1Hlqq5BjbEhEdxapVFZJoZ0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:  مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند.…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16789" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16788">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بلومبرگ  گزارش داده که حمله موشکی منتسب به ایران در روز شنبه ۳۰ مه (نهم خرداد) به یک پایگاه هوایی در کویت، موجب زخمی شدن تعدادی از نیروهای آمریکایی و وارد آمدن خسارت جدی به دست‌کم دو فروند پهپاد تهاجمی «ام کیو -۹ ریپر» شده است.
بلومبرگ به نقل از فردی مطلع از جزئیات این حمله که به دلیل محرمانه بودن جزئیات نخواست نامی از او برده شود، گزارش داد که پدافند هوایی کویت توانسته است این موشک که از نوع «فاتح-۱۱۰» بوده را رهگیری کند، اما با این وجود، قطعات و آوار ناشی از آن به پایگاه هوایی «علی السالم» برخورد کرده است.
بر اساس این گزارش، حدود پنج نفر شامل نیروهای شرکت‌های پیمانکاری و همچنین نیروهای نظامی دچار جراحات سطحی شده‌اند. همچنین یک فروند پهپاد «ام کیو -۹ ریپر» به طور کامل منهدم شده و دست‌کم یک فروند دیگر به شدت آسیب دیده است. ارزش هر فروند از این پهپادها حدود ۳۰ میلیون دلار برآورد می‌شود.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/16788" target="_blank">📅 00:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16787">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پاریس قهرمان شد…
تبریک به گل شیفته عزیز</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16787" target="_blank">📅 22:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16786">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فوری | فرماندهی مرکزی ایالات متحده:   دیروز، ما یک کشتی با پرچم گامبیا را که سعی داشت با حرکت به سمت یک بندر ایرانی، محاصره را بشکند، از کار انداختیم.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16786" target="_blank">📅 22:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یک کشتی تجاری متعلق به دولت ایران توسط ارتش آمریکا با شلیک توقیف شد و نتوانست وارد بنادر ایران شود.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16785" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">با این وضعیت به نظرم دوشنبه نفت با گپ مثبت باز بشود</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16784" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:  محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16783" target="_blank">📅 21:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران   به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،  درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16782" target="_blank">📅 21:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تا الان فکر می کردم فقط صیغه ساعتی وجود دارد...
سبحان الله؛ ویزای ساعتی را هم دیدیدم در این زندگی اما قهرمانی توفان سرخ آسیا را در همین آسیا نه!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16781" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16780">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حالا خوب است به این ویزا ندهند
😂</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16780" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16779">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔵
بحران ذخایر استراتژیک در واشینگتن؛ تاجیکستان کلید حل بن‌بست تسلیحاتی آمریکا در برابر ایران
⬅️
گزارش‌های اخیر رسانه‌های آمریکایی، از جمله
ان‌بی‌سی
نیوز (NBC News)، از نگرانی عمیق مقامات دفاعی این کشور پرده برداشته است. بر اساس این تحلیل‌ها، واشینگتن در صورت تداوم یا تشدید درگیری‌های نظامی با ایران، با چالش جدی تخلیه زرادخانه‌ها روبرو خواهد شد؛ بحرانی که ریشه در کمبود شدید فلز راهبردی «تنگستن» دارد.
🔹
تنگستن که نقشی حیاتی در تولید مهمات سنگین و تجهیزات نفوذکننده نظامی ایفا می‌کند، از سال ۲۰۱۵ به این سو دیگر در داخل خاک آمریکا استخراج نمی‌شود. اکنون با جدی‌تر شدن سناریوهای تقابل نظامی با ایران، پنتاگون برای حفظ توان بازدارندگی و عملیاتی خود، ناچار به جست‌وجوی شتاب‌زده برای یافتن منابع جایگزین شده است.
🔹
در این میان، منطقه آسیای مرکزی به کانون توجه راهبردی واشینگتن تبدیل شده است. پیش از این، دونالد ترامپ شخصاً بر قرارداد تصاحب ۷۰ درصد از سهام میادین بزرگ تنگستن در قزاقستان نظارت داشت، اما به دلیل زمان‌بر بودن بهره‌برداری از این معادن، آمریکا اکنون به دنبال گزینه‌های در دسترس‌تر است.در همین راستا، نگاه‌ها به سمت تاجیکستان معطوف شده است.
🔹
همکاری‌های اخیر دوشنبه با کره جنوبی برای استخراج از معدن «میخورا» با ظرفیت سالانه ۴ هزار تن، به عنوان یک راه تنفس برای صنایع نظامی غرب نگریسته می‌شود. کارشناسان معتقدند تنگستن تاجیکستان می‌تواند به‌طور مستقیم یا با واسطه (از طریق کره جنوبی)، نیازهای مبرم ارتش آمریکا را پوشش دهد.
🔹
هدف نهایی این تحرکات، علاوه بر آمادگی برای سناریوهای جنگی در قبال ایران، قطع وابستگی کامل به چین در زنجیره تأمین مواد اولیه نظامی است. واشینگتن بر این باور است که بدون تأمین پایدار این فلز از منابعی غیر از چین، حفظ پتانسیل رزمی در برابر رقبای منطقه‌ای همچون ایران، در درازمدت غیرممکن خواهد بود.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16779" target="_blank">📅 18:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">- مشاور ارشد رهبر عالی ایران، محسن رضایی:
همان‌طور که پیش‌بینی شده بود، رئیس‌جمهور ایالات متحده برای سومین بار به دیپلماسی خیانت کرده است.
با ادامه محاصره دریایی و مطرح کردن مطالبات بیش از حد در مذاکرات، او یک‌بار دیگر ثابت کرده که تمایلی به مذاکره ندارد و اهداف دیگری را دنبال می‌کند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16778" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پییت هگست، وزیر دفاع ایالات متحده، هشدار جدی به چین صادر کرد
پییت هگست، وزیر دفاع آمریکا، در نشست امنیتی شانگری-لا در سنگاپور (۳۰ می ۲۰۲۶) سخنرانی کرد و نسبت به تغییر اساسی در رویکرد ایالات متحده به امنیت منطقه‌ای و همکاری با متحدان هشدار داد.
هگست تأکید کرد که امنیت منطقه آسیا-اقیانوس آرام برای مدت طولانی بیش از حد به قدرت نظامی آمریکا وابسته بوده، در حالی که بسیاری از متحدان هزینه‌های دفاعی خود را کاهش داده‌اند.
ایالات متحده از متحدان خود انتظار دارد حداقل
۳.۵ درصد از تولید ناخالص داخلی (GDP)
خود را به امور دفاعی اختصاص دهند.
کشورهایی که هزینه‌های دفاعی خود را افزایش دهند، از مزایایی همچون تسریع فروش تسلیحات، افزایش تبادل اطلاعات و گسترش همکاری‌های صنعتی-دفاعی بهره‌مند خواهند شد.
وی با لحنی قاطع اعلام کرد که متحدان و شرکایی که از پرداخت سهم خود در دفاع جمعی خودداری کنند، با
تغییر روشن و اساسی
در نحوه همکاری و تعامل ایالات متحده مواجه خواهند شد.
هگست چین را به‌عنوان چالش استراتژیک اصلی بلندمدت آمریکا معرفی کرد و بر لزوم ایجاد «تعادل قدرت پایدار» در منطقه تأکید ورزید تا هیچ کشوری نتواند بر همسایگان خود سلطه یابد.
وی از گسترش فعالیت‌های نظامی و رفتارهای تهاجمی چین در منطقه انتقاد کرد.
این سخنرانی نشان‌دهنده سیاست دولت ترامپ مبنی بر فشار بر متحدان برای تقبل بار بیشتر دفاعی و اتخاذ رویکردی قاطع‌تر در قبال جمهوری خلق چین است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/16777" target="_blank">📅 11:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">توهم خطرناک جنگ مدرن.pdf</div>
  <div class="tg-doc-extra">328.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/16776" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مقاله ای طولانی اما بسیار خواندنی از اکونومیست درباره تحولات جنگ مدرن و خصوصاً بحث استفاده روزافزون از پهپادها و ریزپهپادها.
اشارات گسترده ای به جنگ اخیر ایران شده که خواندنی است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16776" target="_blank">📅 10:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16775">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbGcImOX_BplEF5SRP16OpBu6G7wd2jrPciWzCCZKkkigg_1StXUCQVscrkk-dtXIYbKBzrMMJnjfLte30cKxwiax6qJBdi-u3hOFA1c9tR0JJdaJU0znhKFK-9EG7FND3Ef_qB0zrOkkrXacYwb1ULQQgVm8XxURRP3T7XFxEIKOyb80QxBkm1OsDDnVva7W0r4TjAzbE0Ns0HcrjLQKs5Czug16tp9Hi2zcXYxmSQb928cBautTF2tWC8eVlzZ7nL8CWFTYT54sKY8yGIgwtlrgBZnzrV16vkD1D_FqUYaPBaFO9hJg08ag9c8_AO3_GlsB8pe3RXq-Xp7mlSCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام هدفگیری شناورهای ایرانی در جنوب تنگه هرمز از سوی ارتش آمریکا</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16775" target="_blank">📅 09:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16774">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این فاکستانی ها هم فعلاً ظاهراً بلای خاصی بجز 100 مورد حادثه تروریستی که اصولاً در پاکستان از بارش باران فراوان تر است دامنگیرشان نشده اما فی الحال لیندسی گراهام گفته به آنها مشکوک است و الّا و بلّا باید به پیمان ابراهیم بپیوندند!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16774" target="_blank">📅 08:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16773">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پاکستان از 3 سمت تحت فشار است:  — هند ( که همین دیروز اعلام کرد عملیات سیندور را تمام شده نمی داند) — افغانستان (که هر روز شاهد برخوردهای مرزی در مناطق پشتون نشین پاکستان هستیم) — ایالت خودمختار بلوچستان که در آن نیروهای BLA با حمایت مستقیم هند ( و شاید ایران)…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16773" target="_blank">📅 08:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16772">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16772" target="_blank">📅 07:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16767">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیویورک تایمز:  بحث رئیس‌جمهور ترامپ در اتاق وضعیت نزدیک به دو ساعت طول کشید، اما او به توافق در مورد یک توافق جدید با ایران نرسید، طبق گفته یک مقام ارشد دولت که با شرط ناشناس بودن برای بحث در مورد مباحثات داخلی صحبت کرد.   دولت احساس می‌کند که به رسیدن به…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/16767" target="_blank">📅 22:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16766">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیویورک تایمز:
بحث رئیس‌جمهور ترامپ در اتاق وضعیت نزدیک به دو ساعت طول کشید، اما او به توافق در مورد یک توافق جدید با ایران نرسید، طبق گفته یک مقام ارشد دولت که با شرط ناشناس بودن برای بحث در مورد مباحثات داخلی صحبت کرد.
دولت احساس می‌کند که به رسیدن به یک توافق نزدیک است، اما سایر مسائل همچنان حل نشده باقی مانده‌اند، به ویژه آزادسازی وجوه مسدود شده ایران</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16766" target="_blank">📅 22:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16765">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تو شیر پیل افکنی !
بزن که خوب میزنی !</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16765" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16764">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تحلیل استاد خانعلی زاده از توافق ایران با آمریکا!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16764" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16763">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKByNA59ZzhE6nstFbHWheZkAGIQLwTn4dD9kUBerJ8fkzQATZWZX355dKPr7fyaBkarPiEq_kiygMIdTZ0KfX63PtopB2CmlNtZrcB3XFE7JP1M4d5v8otNusdQaiRwlQab5geVkph5NErKqa1eMcylUPxMjU_cwcpoXocMQYB7yQ2vxMdxTUjMIrF3lTldV0mbxzZJVArfhNkOH1ZLFvue_TDRF1cx9YgWFSjlLepOm0qMr4ikmf9WmnsdjILh15Pv1GgzSjschWh_aE3VbaWz7lnuLaGvoVeINmMQVxctTM1kc3K-WMsM0CvZ3p5xeYM2KEXn4TTFhRj2HTXQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل استاد خانعلی زاده از توافق ایران با آمریکا!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/16763" target="_blank">📅 22:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16762">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نقش پنهان امارات در جنگ شامل ده‌ها حمله به ایران
به گزارش وال استریت ژورنال، امارات متحده عربی ده‌ها حمله هوایی علیه ایران را از روزهای اولیه جنگ آغاز کرد و تا روز پس از اعلام آتش‌بس ادامه داد،
درگیری عمیق‌تری که تاکنون در کمپین هوایی تحت رهبری ایالات متحده و اسرائیل شناخته نشده بود.
محدوده این حملات شواهد بیشتری از تمایل فزاینده این کشور به محافظت از آنچه به عنوان منافع استراتژیک خود می‌بیند ارائه می‌دهد و آن را از برخی از همسایگان خود در منطقه خلیج فارس متمایز می‌کند که رویکرد بسیار محتاطانه‌تری نسبت به تهدید از سوی ایران اتخاذ کرده‌اند.
این حملات با هماهنگی ایالات متحده و اسرائیل انجام شد که هر دو اطلاعاتی را فراهم کردند، افراد گفتند.
اهداف شامل جزایر قشم و ابوموسی در تنگه هرمز؛ بندرعباس، پالایشگاه نفت در جزیره لاروان در خلیج فارس و مجتمع پتروشیمی عسلویه بود‌ه است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/16762" target="_blank">📅 22:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16761">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فعال شدن پدافند در قشم!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16761" target="_blank">📅 22:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16760">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:  محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/16760" target="_blank">📅 18:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16759">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ:
محاصره دریایی ایران برداشته شده و اورانیوم غنی شده آن را خارج کرده و نابود می کنیم</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/16759" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16758">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">کمیته امنیت ملی مجلس ایران:
قصد نداریم اورانیوم غنی‌شده را به کشور ثالث منتقل کنیم اما شاید آنرا به کشور رابع ارسال کنیم.
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16758" target="_blank">📅 15:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16757">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmvlxpcsVmkNLgERrgEolhB2WmJ6EKmQzs5oCPGqn428zIZDj4YPj83dDY9NxO7-NgJXap19NS3GJs-CJXnK9rcKxiyFgoX5U6ST-5gjd0dWUoWst2a9kl0l0915-c9WBW-cV6v3J7kzVfnKJC2A2a-5Ceacx2c1nLvjUV_Y5eNa3TdhDBceMSNICrb-W-njl3xvpudr8d7GXjuvvMTEEtA9vghj47QRwmMM5bMFYnh1PkwzJYbVEwkfkYvxov-d4n1yuOiLV1YVBA-MFBOgnygNgX6abnSxMOnUrIpohmK9MwDeASuuTlJ-M1V2vE5JbiAdBH259ixgrfUi30X-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره عملکرد پهپاد شاهد-136 در جنگ اخیر
جنگ اخیر نشان داد که پهپادهای خانواده شاهد همچنان یکی از مهم‌ترین ابزارهای تهاجمی ایران به شمار می‌روند، اما بسیاری از ادعاهای مطرح‌شده در فضای مجازی درباره عملکرد آن‌ها نیازمند تفکیک میان واقعیت‌های تأییدشده و ادعاهای اثبات‌نشده است.
پهپاد شاهد-۱۳۶ که در سال‌های اخیر به‌طور گسترده مورد استفاده قرار گرفته، از سامانه‌های ناوبری ماهواره‌ای و هدایت اینرسی برای رسیدن به اهداف خود بهره می‌برد. برخلاف برخی ادعاها، استفاده از ناوبری ماهواره‌ای در این پهپاد فناوری جدیدی محسوب نمی‌شود و از ابتدا بخشی از طراحی آن بوده است. آنچه می‌تواند یک تحول مهم تلقی شود، استفاده از ارتباطات داده‌ای پیشرفته، انتقال تصویر زنده و هدایت لحظه‌به‌لحظه تا زمان اصابت است؛ موضوعی که تاکنون شواهد مستقل و عمومی کافی برای تأیید گسترده آن منتشر نشده است.
در جریان درگیری‌های اخیر، گزارش‌هایی درباره استفاده از نسخه‌های پیشرفته‌تر پهپادهای شاهد منتشر شد. برخی منابع از نصب دوربین‌های اپتیکی بر روی این پهپادها و افزایش دقت آن‌ها سخن گفته‌اند. از نظر فنی، افزودن دوربین به چنین سامانه‌ای کاملاً امکان‌پذیر است، اما ادعاهایی نظیر «اصابت صددرصدی» یا «نابودی قطعی همه اهداف انتخاب‌شده» با واقعیت‌های شناخته‌شده جنگ مدرن سازگار نیست. هیچ سامانه تسلیحاتی در جهان، حتی پیشرفته‌ترین موشک‌ها و مهمات هدایت‌شونده غربی، دارای نرخ موفقیت صددرصدی نیستند.
یکی از مهم‌ترین ادعاهای مطرح‌شده مربوط به آسیب دیدن یا انهدام یک فروند هواپیمای هشدار زودهنگام آمریکایی (AWACS) در پایگاه پرنس سلطان در منطقه الخرج عربستان سعودی است. منابع ایرانی این حمله را موفقیت‌آمیز توصیف کرده‌اند و برخی تصاویر ماهواره‌ای نیز نشانه‌هایی از آسیب به یک هواپیما را نشان داده‌اند. با این حال، جزئیات کامل حادثه و نوع دقیق سلاح به‌کاررفته هنوز به‌طور مستقل و قطعی تأیید نشده است.
در خصوص سامانه دفاع موشکی THAAD نیز گزارش‌هایی از آسیب دیدن برخی تجهیزات و رادارهای مرتبط منتشر شده است. با این حال، ادعای نابودی کامل چندین آتشبار و خروج دائمی آن‌ها از خدمت هنوز از سوی منابع مستقل تأیید نشده و نیازمند شواهد بیشتری است.
در مجموع، داده‌های موجود نشان می‌دهد که پهپادهای شاهد همچنان توانایی ایجاد خسارت‌های قابل توجه و نفوذ به برخی لایه‌های دفاعی دشمن را دارند. با این حال، بسیاری از ادعاهای مطرح‌شده در شبکه‌های اجتماعی و کانال‌های خبری غیررسمی درباره عملکرد این پهپادها، فراتر از اطلاعاتی است که تاکنون به‌طور مستقل قابل راستی‌آزمایی بوده است. تحلیل دقیق تحولات نظامی مستلزم اتکا به شواهد مستند، تصاویر ماهواره‌ای معتبر و ارزیابی‌های مستقل است، نه صرفاً ادعاهای تبلیغاتی طرف‌های درگیر.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/16757" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:
مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند. در این چارچوب، علی‌اکبر ولایتی، مشاور رهبر جمهوری اسلامی، کنترل ایران بر تنگه هرمز را «اهرم نهایی» و «ضمانت واقعی» پایداری هرگونه توافق احتمالی میان ایران و آمریکا توصیف کرد. این موضع‌گیری نشان می‌دهد که تهران، پس از تضعیف بخشی از توان بازدارندگی متعارف خود، به‌ویژه در حوزه موشکی، بیش از گذشته بر موقعیت ژئوپلیتیکی تنگه هرمز به‌عنوان یک دارایی راهبردی تکیه می‌کند.
از نگاه ایران، ارزش تنگه هرمز صرفاً در موقعیت جغرافیایی آن خلاصه نمی‌شود، بلکه این گذرگاه یکی از حیاتی‌ترین شریان‌های انتقال انرژی جهان است و توانایی تأثیرگذاری بر امنیت انرژی بین‌المللی را در اختیار تهران قرار می‌دهد. کنترل یا اعمال نفوذ بر جریان کشتیرانی و صادرات نفت در این منطقه، برای ایران ابزاری جهت ایجاد بازدارندگی، افزایش قدرت چانه‌زنی و محدود کردن گزینه‌های نظامی آمریکا و متحدانش محسوب می‌شود. در واقع، تهران تلاش دارد کنترل بر تنگه را به‌عنوان بخشی از معادله امنیت منطقه‌ای و یکی از پایه‌های نظم مطلوب خود در خلیج فارس تثبیت کند.
در همین راستا، مقامات و رسانه‌های ایرانی بر لزوم مدیریت ترافیک دریایی در تنگه هرمز تحت «ترتیبات ایرانی» تأکید کرده‌اند. برخی گزارش‌ها حاکی از آن است که ایران در مذاکرات غیرمستقیم با آمریکا خواستار به‌رسمیت شناخته‌شدن نقش محوری خود در مدیریت امنیت و عبور و مرور دریایی در این آبراه بوده است. این دیدگاه در تعارض مستقیم با سیاست سنتی آمریکا مبنی بر تضمین آزادی کشتیرانی در آب‌های بین‌المللی قرار دارد.
هم‌زمان، اختلافات اساسی میان تهران و واشنگتن درباره موضوعاتی نظیر برنامه هسته‌ای، لغو تحریم‌ها، آزادسازی دارایی‌های بلوکه‌شده و آینده حضور نظامی آمریکا در منطقه همچنان پابرجاست. گزارش‌های منتشرشده نشان می‌دهد ایران تلاش می‌کند پیش از ورود به توافقات گسترده هسته‌ای، امتیازات اقتصادی و امنیتی مشخصی دریافت کند؛ موضوعی که از نگاه آمریکا می‌تواند بخشی از اهرم فشار واشنگتن را تضعیف کند.
در فضای داخلی ایران نیز برخی رسانه‌های نزدیک به ساختار امنیتی، بر ضرورت تبدیل دستاوردهای نظامی اخیر به دستاوردهای سیاسی و راهبردی پایدار تأکید کرده‌اند. در این چارچوب، تثبیت نفوذ ایران بر تنگه هرمز به‌عنوان یکی از مهم‌ترین ابزارهای قدرت ژئوپلیتیکی کشور، جایگاهی محوری در محاسبات راهبردی تهران یافته است.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16756" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسانه اسرائیلی یدیعوت آحارونوت گزارش داد که اسنادی که توسط سرویس اطلاعاتی موساد اسرائیل در ۱۳ ژوئن ۲۰۲۵، در مرحله افتتاحیه «عملیات شیر در حال صعود» منتشر شد، نشان می‌دهد که عوامل ایرانی آموزش دیده توسط اسرائیل و نه خود عوامل موساد اسرائیل در داخل ایران فعالیت می‌کرده اند.
طبق این گزارش، این عوامل در اسرائیل آموزش دیدند، به زندگی عادی در ایران بازگشتند و منتظر فعال شدن بودند. در بهار ۲۰۲۵، تیم برنامه‌ریزی مشترکی از موساد و نیروی هوایی اسرائیل به آنها مأموریتی برای از کار انداختن یک مرکز دفاع هوایی ایرانی دادند که به عنوان بخشی از تلاش‌ها برای تضمین برتری هوایی اسرائیل بر تهران تلقی می شود.
این عوامل از طریق مسیرهای مخفی قاچاق با پهپادها، موشک‌ها و تجهیزات مأموریت مجهز شدند. آنها مختصات نهایی و دستورالعمل‌های استقرار را درست قبل از عملیات دریافت کردند تا خطر نشت اطلاعات به حداقل برسد.
در آن شب، سلول‌های مرتبط با موساد دیگری نیز فعال شدند، از جمله عواملی که به هدایت حملات علیه مقامات ارشد نیروی هوا و فضای سپاه پاسداران و مختل کردن سیستم‌های دفاع هوایی و موشک‌های بالستیک در تهران و غرب ایران کمک کردند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/16755" target="_blank">📅 11:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16754">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شب گذشته شهر شیعه نشین مرجعیون در جنوب لبنان توسط ارتش اسرائیل تصرف شد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16754" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16753">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">CNN:
پس از حملات ایالات متحده و اسرائیل که در طول جنگ راه‌های دسترسی به «شهرهای موشکی» زیرزمینی ایران را مسدود کرده بودند، حداقل ۵۰ تونل دسترسی پاکسازی و تعمیر شده اند.
تصاویر ماهواره‌ای نشان می‌دهد  که ماشین‌آلات سنگین در حال برداشتن آوار و باز کردن ورودی‌ها در چندین سایت موشکی هستند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16753" target="_blank">📅 09:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16752">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو:
در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/16752" target="_blank">📅 09:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16750">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرهایی دال بر فعال شدن پدافند اصفهان!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/16750" target="_blank">📅 00:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16749">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQB8lm4OaKD1wkHIyLCEHcHjZJ8DhETZlbZ5vwPj-Ap3NMus95LIZlv-in9DLC8DNMhi74YWrsUCrAuJJD5FVUafu3pVDBXsGYqkOGmLJ4q1W4MsErdsjtamllPI9UzZ8kHqxx1cG3GPDk2wA9gO7d3Ys7TLEnb2bervyp6DyeSDHBXo7JrrKBVtCrDbnQcGWJA8lKkpZ7LdEFTv8XbZtHH0iu7w9TbomDjgkO1TOWZxppj_cqwFXQ6fXFb8xR-oje5MuEn_JYbZM1mw1UUQMfcXHmNZ4_wrmfXOQVLXwooEKRke6wlVQIOWqXSfMojP2pHZFcpmV9IZIgVmxrPfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/16749" target="_blank">📅 23:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16748">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تسنیم گزارش داده که مردم بندرعباس نگران نباشند، منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا مربوط است!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/16748" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16747">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تسنیم گزارش داده که مردم بندرعباس نگران نباشند، منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا مربوط است!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/16747" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16746">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/16746" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16745">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">باز گویا در هرمز تبادل آتش داریم!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/16745" target="_blank">📅 23:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16744">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">باز گویا در هرمز تبادل آتش داریم!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/16744" target="_blank">📅 23:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16743">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxDaMfs6_xtp_szofgQwfleEI__eFKUScQzhV-J-_Jst9zu1KyLmhExbxztAf2dfBw7xNBpBSF1JhIKu8AeGjWtMv0wjaEovbt2HxYIXI0A13DK-3R5W8O_cIsNTN9wwP4Tn0zBFblKNWZUoS6FSHh8i-6vM4s-mftqA5gtDjO5WFAQiqnI9Fsye6AGySbixBEsEgvwwPVnmHiNgey20j6McAb1TR5ovoGqPcK8IPgX64M9CxAOrJaWB52v_HRODB1_FR_C2Z0NjZpJCT169Tejm3U0eYZBIP5mpNZvVd7LeB4N_CMs2wEcYYkfbIXLjF5t8eMSNq20SR5BNBBOeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/16743" target="_blank">📅 20:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16742">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این عمانی ها هم بدبخت‌ها یک بار زمان شاه از شر کمونیسم نجاتشان دادیم ولی ۲۰ سال است که سر‌‌ پرونده هسته ای رنده شده اند!  اینقدر که اینها پیام آوردند و بردند، ۱۲۴ هزار پیامبر نکردند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/16742" target="_blank">📅 18:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16741">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:   «من این را به‌طور خاص به عمان می‌گویم؛ ایالات متحده با هر کشوری که به ایران در وضع عوارض در تنگه هرمز کمک کند، قاطعانه برخورد خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/16741" target="_blank">📅 18:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16740">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16740" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16739">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2kf4mLNYMAc70v-__lTj0uva1B2yPlI_r-mpjjvnlLCT28i9LAC54VdhogEU88IsIqhdf2YgQQ1Zxt2zJyXDaSxceY3TIAlR1tSX9OrE--E2iVfd-WFhhoxXAwe30qWfYfSHHwsdmzjUYwiELZa-6WvuF2p0qYVzgMqtNIl_cE_wNVFt4L4TnotGY7UYIr15pBpYIuhMgop_JZaPnHbjlbrl9vvBfimriZAR-s_9ZTJ09EmaRcatTE_0QJF6lSYA45hyKs97_yt7hty6AjE1byCgbOhfgGZL-ItovHeljTi7KtnDXTHadWJV8kSBFO2Bv_ZfL4juGxbdvOQO-Pcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#VIX
— H4
شاخص ویکس از محدوده ای که جنگ شروع شد پایینتر آمده و کانال را هم شکسته.
سوگمندانه بازارها ما را به یک ورشان هم حساب نمی کنند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/16739" target="_blank">📅 18:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16738">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/16738" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16737">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو:
باید مأموریت در ایران را کامل کنیم و تقریباً روزانه در این خصوص با ترامپ صحبت می‌کنم.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/16737" target="_blank">📅 17:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16736">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شرایط توافق شده :  هیچ گروه مسلحی در جنوب رودخانه لیتانی وجود نداشته باشد  کنترل ارتش لبنان بر جنوب  سلاح‌های حزب‌الله محدود شده یا ‌حذف بشود</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/16736" target="_blank">📅 16:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ریچارد فانتین تحلیلگر ارشد سیاست خارجی آمریکا :   محتمل‌ترین پایان این جنگ داغ، یک توافق محدود است. سپس مذاکراتی طولانی و شاید بی‌حاصل آغاز خواهد شد. جنگ سرد از سر گرفته می‌شود. و آمریکا و ایران در انتظار دور دیگری از درگیری در روزی دیگر خواهند ماند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/16735" target="_blank">📅 14:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/16734" target="_blank">📅 14:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ماکرون و احیای آرمان شارل دوگل  در تحولات اخیر، رئیس‌جمهور فرانسه، امانوئل ماکرون، اقداماتی قاطعانه انجام داده که یادآور میراث شارل دوگل است و خود را به عنوان یک رهبر کلیدی در دفاع و خودمختاری اروپا معرفی کرده است. پیشنهاد ماکرون برای گسترش بازدارندگی هسته‌ای…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16733" target="_blank">📅 14:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwa0eQT-5WX7K4DoQoo2jFf6iaQLP-xuX9hP-23WMpqPN44Ui5vm37sYleQ-0qtf0ypqYVhQMvfaOgx8r_j9PUx8hKQxIm5dvDG-slkld7NfvGYMSTnEI_l5KosOZgxDbF4TzbRqXbEGmXaYVVryr4RuVM04Nlx4t3Xq_ns6gRD8ltgx7gz8TL-yaJgWp-sm1lNsAyB2rIYQU6lmb5Dz8O0YsdDmZqZpcFlsh0Zm9oiBqtlabTJzoCo4tW3E2zcqYzoVq0yIH_TZCVaxhqklzViSKVVre9C9aMXzE9fcw2BVQzwsogk55Uo2VDXqW2eJ_DSvZ5USm16DTO3BB0wuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی خودارضایی مبارک!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/16732" target="_blank">📅 13:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16731">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگر دولت ما آن بالا Short کرده بود تا الان خسارتش جبران شده بود.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/16731" target="_blank">📅 11:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16730">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#TOTAL — H4  حدود 250 میلیارد دلار از ارزش بازار کریپتو پودر شد.  اکنون به کف کانال رسیده و اگر فروش هست باید تریل کرد یا کلاً تسویه.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/16730" target="_blank">📅 11:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16729">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of4osqdqWIswp483y90kCdd3_5cNZq8TxxKw2L6tLcpBsVfPhBgVUecMKbPuMvkTdDzM41nTEeuGBcEPnBtOoKP3RCSdK5bmZowPbDv904YQcm7hmfI0IxMOs3YbDCuXQib-cPAzOQ3vOdOm8QxajNfV3sikc-V2Vg-bwfFMr0qb4S9qBbPPEHfPN54oTDym9peek4IwbdQry6-sOTFFY0awf3N8QB-cAvrKb7e5qVuGpy5ZSK9p6EJxz5Y3XgM2Mgs_lGjrlwNM3cYim8PrIUGaEHohVa5OZhd3MLBRtBxRZiDzQ1ifViUDAdC0AaEJ4q8NWe1jBoLeP0uXgi-RkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TOTAL — H4  تایم پایین تر</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/16729" target="_blank">📅 11:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16728">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی از بازی است از دید من.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16728" target="_blank">📅 09:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16727">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cfb8e810.mp4?token=UXaQXRF--m5Ep0pl_dalCYBG2jBZauNKX5F4vEYOcQ7TksG55Fk_DAkdV-nylLU4NoFxGWJ065wXGFfhHD-yPTCjLhj98-2hCcjODQVh4ba3LxnfnWpVupoFs7w-RlJXVWILIlZp6Fwev5ZJLGjXQG3TQfSphvgdoh58vdNvpbnRNghP1YSOlUyzqmPAMGWrDomks1B5vEtALUftRMsWtvw03vQtg5if0R7VwhUGS_PNAz8YpmMjPm8H8yEBOzg0E5xUGnPKXnXi3I3d4zhKxkCOSrS24FcKFZGWLC_KKIv9_bbMZsyvwPWo90i09E1dLMGIkuShQu3tSa70ZWqn5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cfb8e810.mp4?token=UXaQXRF--m5Ep0pl_dalCYBG2jBZauNKX5F4vEYOcQ7TksG55Fk_DAkdV-nylLU4NoFxGWJ065wXGFfhHD-yPTCjLhj98-2hCcjODQVh4ba3LxnfnWpVupoFs7w-RlJXVWILIlZp6Fwev5ZJLGjXQG3TQfSphvgdoh58vdNvpbnRNghP1YSOlUyzqmPAMGWrDomks1B5vEtALUftRMsWtvw03vQtg5if0R7VwhUGS_PNAz8YpmMjPm8H8yEBOzg0E5xUGnPKXnXi3I3d4zhKxkCOSrS24FcKFZGWLC_KKIv9_bbMZsyvwPWo90i09E1dLMGIkuShQu3tSa70ZWqn5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب الله زندگی شیعیان لبنان را با پیوند زدن سرنوشت شان به حیوانات اخوانی حماس به گه کشید</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16727" target="_blank">📅 09:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16726">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این بازی ها فعلاً برای خالی نبودن عریضه است و اینکه فشار جمهوریخواهان تندرو از روی ترامپ برداشته بشود و این ور هم جانفدایان مقداری آرام گیرند و گرنه موج 3 جنگ تمام شده و این حمله اسرائیل به حزب الله هم بخشی
از بازی است
از دید من.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16726" target="_blank">📅 09:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16725">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وضعیت گروه هواداران پروفسور رائفی پور</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16725" target="_blank">📅 08:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16724">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiQH0JexlnIAcsSI2JTtlAcVlAfiaxmkIeDs8-HQSuL375rBBnzslspiWP_o3CCx9coGsavV6FdoWH5_u0indYBjdXva8_l6CwsneLrF5zuiHNkR0LO7ydMYrNulf7-4MYZfZPAPnSqd1Yeh5eiVQxthZfMGnVo6IsgN7pWSGCCx-dBLbAOI_O77dLYMNR11Fuv_3v-BeayT280CMYB4X2PhMavUXmICYCl09J2vWaP_gY5QM0KPwin3I_wlkLnbiKVd2E8CnXXoCKL9pi6Z2-kZ_rKdZNlCCN6bXqloNGZaxyc73sO1R12Fk7ufpKISm6EGH_mONsZbnVBRlF0KRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت گروه هواداران پروفسور رائفی پور</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16724" target="_blank">📅 08:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16723">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8g5z0cJ83BoHEo3I-29AoUhuHHTvcCZn55HkrQRKRaZFJ6Z8SIR9qOpa0BHlE6a16Xu9SwmzLycSDInPdsyCEylNEslO292UY5I4oiArPWDkLPbOtsedYXe9_F5RXaNmOiwHc12HR2nx8Uzljd9lKCqRFbMWdhhHvP2n0ZF1v9Q9OQtDorloZnAERA2cMrpsWRn_nXDSzoN46QRDtQRPkfpSMKzFX8O7FjVUnTpsRUX5iaqkU4N9r0_EDQxAkVyhUPwFMRoTlJN3Daal2PK4ngrC_Vb5R6PfEkS4GiC2j7uAm0hz2iPgJQnG6lp4dlWTcBU4spWOIj5jtlbgwpidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خیلی هم الکی نبود و سپاه یک پایگاه هوایی آمریکا را در کویت زد.  ولی هنوز موج 4 هستیم
😆</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/16723" target="_blank">📅 08:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16722">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک منبع آگاه نظامی به خبرگزاری تسنیم گفت: ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.   در مقابل، ارتش تروریستی آمریکا به زمین…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/16722" target="_blank">📅 08:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16721">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0ErjgUwCJrSW_2ZXgni2ep6UDttx0V0b7bZ5HPnXFmmh7Gb394ZeRnhSxliOCjHcnEEjVPEgUmOXkvPAaiKNVk5tWkr-SCGDw-vV3Mskrb55wVteY3QokOSiou7epgKWEReQiodYmSJLUdiiaW93Rl6oaDOzOzmUpP7VM-vaezx3dfABNDr5fez6apJucsU0im-tYb0wwz_DPtqYtV-loUo_npJsgPc7Mal_KcUsm9X3T88o4DSqlrKzn5h-901GJlMPWxyWsexiQOI0mOvxWNkI8pJtU-5J0g-UovImsXbnv1tplB0UaLH9fDtX9XG4bXIzLGJj5Nb22xxi5dgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران یک موشک بالستیک از خوزستان به سمت پایگاه هوایی علی السالم در کویت پرتاب کرد که توسط سامانه پاتریوت مستقر در پایگاه رهگیری شد.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16721" target="_blank">📅 08:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16720">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ایران یک موشک بالستیک از خوزستان به سمت پایگاه هوایی علی السالم در کویت پرتاب کرد که توسط سامانه پاتریوت مستقر در پایگاه رهگیری شد.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16720" target="_blank">📅 08:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16719">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این قسمت بیانیه عملاً یعنی خیلی دنبال تنش نیستیم ولی خب.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/16719" target="_blank">📅 08:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16718">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع‌تر خواهد بود و مسئولیت و عواقب آن با متجاوز است.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16718" target="_blank">📅 07:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16717">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سپاه پاسداران:
به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع‌تر خواهد بود و مسئولیت و عواقب آن با متجاوز است.
و ماالنصر الا من عندالله العزیز الحکیم.
روابط‌عمومی سپاه پاسداران انقلاب اسلامی</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/16717" target="_blank">📅 07:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16716">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الکی است و امروز یک توافق امضا می‌شود که البته در چهارچوب همان موج ۴ ارزیابی کنیدش</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16716" target="_blank">📅 07:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16715">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سبحان الله!
یک نفر که مشخص است از 28 فوریه تا امروز به نت جهانی دسترسی نداشته و صرفاً در بله و ایتا غسل می کرده در دایرکت پرسیده که استاد با این 300 میلیارد دلاری که از آمریکا میگیریم احتمال نمی دهید دلار تا 100 هزار تومن پایین بیاید؟!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16715" target="_blank">📅 01:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16714">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/16714" target="_blank">📅 00:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16713">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16713" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16712">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16712" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16711">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:  • آتش‌بس دائمی در همه جبهه‌ها • خروج آمریکا از منطقه • عدم دخالت در امور ایران • رفع کامل تحریم‌های اولیه و ثانویه  • آزادسازی وجوه مسدود شده • +۳۰۰ میلیارد دلار غرامت بازسازی • کنترل و مدیریت ترافیک دریایی…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16711" target="_blank">📅 23:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16710">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شروط کلی ایران به صورت رسمی در صداوسیما اعلام شد:
• آتش‌بس دائمی در همه جبهه‌ها
• خروج آمریکا از منطقه
• عدم دخالت در امور ایران
• رفع کامل تحریم‌های اولیه و ثانویه
• آزادسازی وجوه مسدود شده
• +۳۰۰ میلیارد دلار غرامت بازسازی
• کنترل و مدیریت ترافیک دریایی در تنگه هرمز</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/16710" target="_blank">📅 23:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16709">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترور جدید اسرائیل در غزه</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16709" target="_blank">📅 23:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16708">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhKbQrqmeBCavpZjiWn7BYAZ6VmNY3znhHCHPCuBr4fiNL-BFrBLGWA7f42HioUptge8nW216V2wiiTWu9ZwTO185iIAAO2dBVnpnE9KWF0a2kyK01hpYt8W8bkTEc_apos5fiOrPnAqNG3naB_CSto2tKFisgKRiREqDRulLzDcFVxN6Dzr-Wgh0KON7X-lv8_wqNp516ohUvF0gpWNnPoVt_-TzWWJsb02Bj-RDTnMfX_favKAjzXOR1lrOwDnJCYIQdZrK3ac9cxK4bMCi6qmjl31dJF8vO5Pox_VKoSTiUrJ3_9FU2aE_ZeC9Z76eY6I1OS3wTWtKLaKMMg3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16708" target="_blank">📅 22:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16707">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e42f7252.mp4?token=RSfhkwUVpPZczxwdK5r4dAqbw5YxwQxUHLwl-VH4mowG94vzvIIJWXXo5WT9wvIIpwMbqzd0QJLI9rnV1Vy8Z7zNJMgBzttMEPF-gCMU30scoXTZnirlpRvrTe2SgagzsOreQ7b2_YUVu4luwyY3OJTU22zKkPqEW1ymFL7QyE693n3FKqAcUxImWfn9Cphpt6cYF_ThDbq6qt6Gm9gWsw1yaXiXnHhDbrRu6tGA8Z4iZ4hoDEoMJF5l_lp9mwQxd_Q9fIfWmwBX5i5x-rVyWC_Gf8i66g_oeI3HDHFNu_JQUXMi4FaDY54YHwoB6RbFkrFmw5mlzHx2K7F0rAj9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e42f7252.mp4?token=RSfhkwUVpPZczxwdK5r4dAqbw5YxwQxUHLwl-VH4mowG94vzvIIJWXXo5WT9wvIIpwMbqzd0QJLI9rnV1Vy8Z7zNJMgBzttMEPF-gCMU30scoXTZnirlpRvrTe2SgagzsOreQ7b2_YUVu4luwyY3OJTU22zKkPqEW1ymFL7QyE693n3FKqAcUxImWfn9Cphpt6cYF_ThDbq6qt6Gm9gWsw1yaXiXnHhDbrRu6tGA8Z4iZ4hoDEoMJF5l_lp9mwQxd_Q9fIfWmwBX5i5x-rVyWC_Gf8i66g_oeI3HDHFNu_JQUXMi4FaDY54YHwoB6RbFkrFmw5mlzHx2K7F0rAj9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ تهدید به منفجر کردن عمان کرد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16707" target="_blank">📅 22:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16706">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16706" target="_blank">📅 21:35 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
