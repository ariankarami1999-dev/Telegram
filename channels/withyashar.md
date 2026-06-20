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
<img src="https://cdn4.telesco.pe/file/R-2G-6ZRbML_SHh4yUJa_DcAibIynRy-jfbi9pWdgUti9xO885JSKZNFcbxjePOD4SmTdipJ-34Cjf-0aXPCEqEUb-a8hjWRkK5MfrMxpn1n-hdWXKqGL2bB0zBGEUwdloRuPk9w_dL_IyQq8htZvMPfqJJGDJU4OctcDVIcE14F1RoEMYsxUd-zmkgmMl92G4Iobn9R-FOsknfZGp5DU5Wuhx0pTiP-c3jLCGToe1SJY9tClxz7XWoXqhiOs7oF4u1UZDIQokcKdJ_SpkMpu5eXcXIw2Uv0xb1DreSBkLgaCoc17XsfFGCNmLgv_Da0NF6gK63ie_O8YIGqM0woSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 03:31:43</div>
<hr>

<div class="tg-post" id="msg-15375">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آکسیوس: ویتکاف برای اولین دور مذاکرات داره میره سوئیس.
البته
فعلا تاریخ جدیدی برای مذاکرات تایید نشده؛ نخست وزیر قطر هم به عنوان میانجی اصلی الان تو سوئیسه.
@withyashar</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/withyashar/15375" target="_blank">📅 03:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15374">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بابک زنجانی : ‏به نظر می‌رسد یک موضوع نفوذ و خرابکاری امنیتی در کشور در حال وقوع است.
@withyashar</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/withyashar/15374" target="_blank">📅 02:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15373">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عفو بین‌الملل هشدار داد مقام‌های جمهوری اسلامی از پوشش شرایط جنگی برای تشدید سرکوب استفاده کرده‌اند. همزمان برخی خانواده کشته‌شدگان‌ دی هم از حذف نام آنها در سامانه «بهشت زهرا»ا خبر دادند.
@withyashar</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/withyashar/15373" target="_blank">📅 02:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15372">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ارتش اسرائیل (IDF) در حال پیشروی به سمت تپه علی الطاهر است.
بعد از بمباران سنگین تپه الطاهر در هفت روز گذشته، حال نیروهای اسرائیلی در حال فتح این تپه هستند.
تپه الطاهر از لحاظ استراتژیک آخرین سد دفاعی شهر نبطیه است‌.
@withyashar</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/withyashar/15372" target="_blank">📅 02:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15371">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V92Od8pMOTQf7hEZ5b3JEXSsvK95Bo8F7bSs5RtQlvRg2rpMPimEZDxcOeMg9vDkeHFOnwgD7903HdJl_eBIPIL6u0Xhz7DkR4XWl0N97SyyZDj_4ZIbCE3-O6mVaGF184uySYdgGy_SEetRHjuPhqRft7J64v9hrACkxpzOWR2kWFq6Vea4UphO7l_BRaGpuipHCD3-F5MbPqqT_3Nsl3BO6F8vtIyKJ5Ozu-PniiD56hjuKQhqaPpXaKdVlnAJy1RXqTM3FBzL30HHODRzgXNb1inpvLteuN5jIcNAJr6tX7rC72bHdjQRqPUuv0GSQFkDvQAr-ibJ_CSqEYP6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت ۱۰ نفتکش ایرانی به نام های؛ دیونا، قهرمان، سونیا، دورنا، آمبر، خندان، برف، هدی، استارلا و دریا عمیق به طرف چین
@withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/15371" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15370">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تیم ملی آمریکا با برد ۲ هیچ برابر استرالیا به عنوان دومین تیم پر قدرت به مرحله حذفی جام جهانی ۲۰۲۶ صعود کرد!
@withyashar</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/15370" target="_blank">📅 01:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15369">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746536a751.mp4?token=WRl24cR1hckpMLauOEzOBbvokw4Zjcnaj1VCgdLYlCr0241gWeSR1UjXMotvL4Ki5tUAD_ZC9Wdyvu1LfdRZ3lsLdCmh12EnSzCyzpq6_3MCMh9eHXe2pY57EqSq1WK7GUAbMkq4pD14V334p-Miq42EeOBg6pK667StXvDlpu4WcTlgkcPJ552FTxjkaIjD4k52OfTUb5HoCfHn-z87uLke4bEQPcCLSRkGQZyCGUmWZ56yVmQnmQ44Vrq7jfBep-0nwLXdSFOYKuwGX5ocHIwM4ozj6h-Pbk9nQPSLA0GNTOf9SMm2_SQaXcN8zk4R1vHy8nY12eUj3GWp8r6H6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746536a751.mp4?token=WRl24cR1hckpMLauOEzOBbvokw4Zjcnaj1VCgdLYlCr0241gWeSR1UjXMotvL4Ki5tUAD_ZC9Wdyvu1LfdRZ3lsLdCmh12EnSzCyzpq6_3MCMh9eHXe2pY57EqSq1WK7GUAbMkq4pD14V334p-Miq42EeOBg6pK667StXvDlpu4WcTlgkcPJ552FTxjkaIjD4k52OfTUb5HoCfHn-z87uLke4bEQPcCLSRkGQZyCGUmWZ56yVmQnmQ44Vrq7jfBep-0nwLXdSFOYKuwGX5ocHIwM4ozj6h-Pbk9nQPSLA0GNTOf9SMm2_SQaXcN8zk4R1vHy8nY12eUj3GWp8r6H6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان درگیری‌های سنگین بین نیروهای اسرائیل و حزب‌الله تو لُبنان
@withyashar</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/15369" target="_blank">📅 01:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15368">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNHJEOKrgnWEq9lyBd2MfXP7Su4W8_aR5pdm3T9fRNcVvBMiev4D0fyIzfAzYSweHz0t1E19-OmzNK7uTBlwagk1mMrzLnxQI1y1vik6UCDIxgJDRi33TjYl-NMgrOGdAkRPgMfPZXfYLHXMsib2d7KBkO4nMrPl7tomyU8XfIH8KSPu6RTNkvKZoCsK0MxfJj6zdHckcEzST5tEqHwxcrwGkDp02uYLyuuffqK-bV83YKUzU3iJdhHp5lopKWtN3rEO8rizK4oeTDNE4aAfwVu-Lrk3Qj6ImoVtewK410u2WLoyytlfeQRsMAhW30ONil8qp0mk1nfNK9BQA6qgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور لایو
@withyashar</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/15368" target="_blank">📅 01:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15367">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">https://www.instagram.com/reel/DZyFKZXCHfl/?igsh=anMxYmI2ZnUzdHpy
لایو سیو شد</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/15367" target="_blank">📅 00:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">میرم لایو اینستاگرام
💥
🚨
۵ دقیقه دیگه نتیف های اینستاگرام رو روشن کنید و اگه ندارید فالو کنید instagram.com/yashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/15366" target="_blank">📅 00:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">میرم لایو اینستاگرام
💥
🚨
۵ دقیقه دیگه نتیف های اینستاگرام رو روشن کنید و اگه ندارید فالو کنید
instagram.com/yashar</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/15365" target="_blank">📅 00:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95575b9e53.mp4?token=HD5GxvXz6lhjr3A71jO82kRnc_SBRsSIb1Uf43-oRdNxpef2mDIAZZmaTG7t15kZuh-D1ObNxBDlW5s_TRBUA_Ikt9muQuLajWx_8CDxIag0txFaC3rj0wGjXv4oASjzjQzLGDqm1iAU5RuXQ2Z-yQgMtp8XInhNHuuk3phVtEiv_qikVQidVZ5G1WffdZlbrgxMbEvkI4OkjSnRV-H6IaLHkW-obfusUCZN64IYAlv7x2roxq9tACPKL-Cgchfo3OnGWPSdngj5vWlniK5cNd5AMMXB5nrqSbTTlJi81xjlBMzXAONeJYvOpxcab2Gys2ba2lB9vf3V2g-IzTa-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95575b9e53.mp4?token=HD5GxvXz6lhjr3A71jO82kRnc_SBRsSIb1Uf43-oRdNxpef2mDIAZZmaTG7t15kZuh-D1ObNxBDlW5s_TRBUA_Ikt9muQuLajWx_8CDxIag0txFaC3rj0wGjXv4oASjzjQzLGDqm1iAU5RuXQ2Z-yQgMtp8XInhNHuuk3phVtEiv_qikVQidVZ5G1WffdZlbrgxMbEvkI4OkjSnRV-H6IaLHkW-obfusUCZN64IYAlv7x2roxq9tACPKL-Cgchfo3OnGWPSdngj5vWlniK5cNd5AMMXB5nrqSbTTlJi81xjlBMzXAONeJYvOpxcab2Gys2ba2lB9vf3V2g-IzTa-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «ما رابطه خوبی با اسرائیل داریم  بی بی نتانیاهو یک نخست‌وزیر جنگجو است.
باید به همین عنوان از او قدردانی شود. باید به او اعتبار بدهند.»
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/15364" target="_blank">📅 00:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ درباره حمله دوباره به ایران:
به یاد داشته باشید، اگر این کار را انجام دهیم، ناگهان نفت به سرعت از تنگه خارج نخواهد شد.
افرادی که مالک کشتی‌های میلیارد دلاری هستند، دوست ندارند موشک‌ها بالای سرشان پرواز کنند
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/15363" target="_blank">📅 00:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15362">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قفلی جدید ترامپ برای هزارمین بار : ایران ۶۰ روز فرصت داره توافق کنه.
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/15362" target="_blank">📅 23:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15361">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صدای چندین انفجار در استان ادلب سوریه شنیده شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/15361" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15360">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ اعلام کرد: جنگنده فوق پیشرفته F47 برای ارتش آمریکا در حال ساخت است، پیشرفته ترین هواپیمای جنگی در تاریخ بشر
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/15360" target="_blank">📅 23:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b86630f610.mp4?token=EQA_sdlO5nfoZckunnJmAmJmY1jRbhKD0c7OKHc2HcQGgtgBPJw3ahWZOuXz9RMW67jW1e2NJdj2WShP6_8T_R756KipYmMVew-LobqIFGL0CiYYxj9bqwGD5w1WldurkppJs1Y1UnQxEGyWyTvzajZAU54IKQgOJjW0aSRaZYrWQiDKMb-FiYNf7jZQBY0ZIVMpY-v5dfcmTif9hJu0KT2XprZUkLpBCFWMPuiM3GwpmRcm9V6Q2K8KXcgTweeD7VXJV9pK3MMHjus3R4ImAm2KdRY46vM9xSZCyDHs1C-56zbt9XL0Wrx5OOxanWTdtktHCv3593ShIFqSCYf85A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b86630f610.mp4?token=EQA_sdlO5nfoZckunnJmAmJmY1jRbhKD0c7OKHc2HcQGgtgBPJw3ahWZOuXz9RMW67jW1e2NJdj2WShP6_8T_R756KipYmMVew-LobqIFGL0CiYYxj9bqwGD5w1WldurkppJs1Y1UnQxEGyWyTvzajZAU54IKQgOJjW0aSRaZYrWQiDKMb-FiYNf7jZQBY0ZIVMpY-v5dfcmTif9hJu0KT2XprZUkLpBCFWMPuiM3GwpmRcm9V6Q2K8KXcgTweeD7VXJV9pK3MMHjus3R4ImAm2KdRY46vM9xSZCyDHs1C-56zbt9XL0Wrx5OOxanWTdtktHCv3593ShIFqSCYf85A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما سفرهای زیادی انجام می‌دهیم. به ترکیه خواهیم رفت.
در مقطعی، برای یک کنفرانس بزرگ به چین باز خواهیم گشت
اگر با ایران به توافق نرسیم، کارهایی خواهیم کرد که آنها را خوشحال نکند، اما فکر نمی‌کنم این کار را بکنیم.
توافق هسته‌ای ۲۰۱۵ با ایران یک فاجعه بود
من با رهبر جدید ایران صحبت نکرده‌ام، اما او شجاعت خاصی دارد.
من از موضع قدرت مذاکره کردم چون نیروی دریایی و هوایی ایران نابود شده است.
کشتی‌ها به طور بی‌سابقه‌ای در حال عبور از تنگه هرمز هستند
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/15359" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db2a296ef.mp4?token=FtEIpTkUCmx8fngVYd82QdRqYqlkfmygqXj_-a1VTrRttSQLHZU5CBa_6yKj9XPlfToCuV3gXeullFERhvvbnneHYKhO5eoipJm9LN_S1p9Z6uN8ymBs2_J4A-OeSINeUK1kdJujI_68bxTOYvCTbZwjsGEsgCAzC2pRdTY1YtlLmIDb8jjFr0M-s9XJwANCMSdJbluGy8k2PXilq3jRtlPNFGky6mP745xn79XndzyNpeVPRIlbA9dTZh9sSmuyqnjNROz7GPXeUmmEJ7yYd14HsJ6E4yc6VkOiK8OtHe0XXalveBqX65aLv-0fUGspLS7BV36l94TcY1UwhdIz7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db2a296ef.mp4?token=FtEIpTkUCmx8fngVYd82QdRqYqlkfmygqXj_-a1VTrRttSQLHZU5CBa_6yKj9XPlfToCuV3gXeullFERhvvbnneHYKhO5eoipJm9LN_S1p9Z6uN8ymBs2_J4A-OeSINeUK1kdJujI_68bxTOYvCTbZwjsGEsgCAzC2pRdTY1YtlLmIDb8jjFr0M-s9XJwANCMSdJbluGy8k2PXilq3jRtlPNFGky6mP745xn79XndzyNpeVPRIlbA9dTZh9sSmuyqnjNROz7GPXeUmmEJ7yYd14HsJ6E4yc6VkOiK8OtHe0XXalveBqX65aLv-0fUGspLS7BV36l94TcY1UwhdIz7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ خبرنگاران را به پایگاه مشترک اندروز دعوت کرد تا هواپیمای جدید ریاست‌جمهوری ایالات متحده را ببینند.
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/15358" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJv1dFBnKRR4Z7Ky7RFNMukTk_7-WKySXLWPyPS47oAT4a86_D3wV7Aroy7qrMSWELAfr9APrBIspos0RPyucuTp4JLFcwWOOiVxre9JvXoxF0PltRAtOnK9bVEsNuevZRZSNogiaPc8jNTR-dbuXKFT_6-1TF_AjT46FrgsTTWga8ygoGJa3ei87vzirySd9OLiNnV9xfWXwW5mHoqN9obENyHmMtKsxT12KJdEU7b_WJMd-L6KoFR8-GhUTcpPYORPrjpnwbE7uukxakwvM3zCdmOmSHuArel1HujlkQTi8lF57x3lWR7OT7JC2z1vXNSMpzKEpEClfI0GlDocSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در پایگاه نیروی هوایی اندروز از یک هواپیمای موقت جدید ریاست‌جمهوری رونمایی کرد؛ یک جت لوکس که توسط قطر اهدا و عبارت «ایالات متحده آمریکا» بر روی آن درج شده است.
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/15357" target="_blank">📅 23:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: حدود ۷۰۰ کشتی از تنگه هرمز عبور می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/15356" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15355">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ:
کسانی که مردم ایران رو سرکوب کردن، دیگه در قدرت نیستن!
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/15355" target="_blank">📅 23:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15354">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزارت امور خارجه آمریکا:  روبیو به جوزف عون‌ رئیس جمهور لبنان تأکید کرد که ضروری است حزب‌الله خلع سلاح شود و دولت کنترل خود را گسترش دهد
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/15354" target="_blank">📅 23:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15353">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سناتور آمریکایی تد کروز: دادن میلیاردها دلار به حکومت ایران که شعار مرگ بر آمریکا سر می‌دهد، ایده بدی است
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/15353" target="_blank">📅 23:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15352">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/824375196b.mp4?token=UB2Nfpb3s8zUccd58Nqh-uOcwbmMZgKWocJZnznC3vz-mKvCRN9WnlDNZgAAlNa1C4Rl2z99fTMIKEmDvaUAdi9J3-mVwAlV30XwE2BtbJH3ZpEh5t9HCjfXEJ487T4w_QtGk7Wc439dWhLYXFFQSHyKVWAX8HBpDostOMMhBs7AyK0ufdl9JevKa3uMnfhCusJ9-7s2-XIGv9Kk2LmjBKI1UhYcpcYK0JcFflTPsFoPCRWU7est96fBzD78ZNUQqNC4HqaRsLBaFDaOS3N1k8gAc9S4VL8Wvtf_gDFScjtr-T_8iY5szFBD78cH2I4LZ9Cr2W3VCWVkIwztMLt12qxQJw_mLiUa51MNA9gIbCYKbd5X872V-JvQ13lwjBmR87Yy9YfEI6RvZNYIngudRj3j1yj8i_DaPz9dkGjJZPMnNUkMxIzxJIQLujyzlLz6lPalSzvNKDEAdZnSqHNbg1apZyhmWZAYFAQkNJO-0xUUTb0SbtlQOOvGxVxd4DMeEIzBybgEKKiHFc2r0brkxM6MRay-IiQytal6yajKDG8O6A2AvHJVJKW1kSyh2i0RirxqVx_TIemzGSAzVSPRCVVYpAbTDLET_8n0HEwuOvHPPamHAgKKJX42WESpBVbadccrswiLC8bsNKdY_2E1egtUHxsEnXVSisD8HNY34_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/824375196b.mp4?token=UB2Nfpb3s8zUccd58Nqh-uOcwbmMZgKWocJZnznC3vz-mKvCRN9WnlDNZgAAlNa1C4Rl2z99fTMIKEmDvaUAdi9J3-mVwAlV30XwE2BtbJH3ZpEh5t9HCjfXEJ487T4w_QtGk7Wc439dWhLYXFFQSHyKVWAX8HBpDostOMMhBs7AyK0ufdl9JevKa3uMnfhCusJ9-7s2-XIGv9Kk2LmjBKI1UhYcpcYK0JcFflTPsFoPCRWU7est96fBzD78ZNUQqNC4HqaRsLBaFDaOS3N1k8gAc9S4VL8Wvtf_gDFScjtr-T_8iY5szFBD78cH2I4LZ9Cr2W3VCWVkIwztMLt12qxQJw_mLiUa51MNA9gIbCYKbd5X872V-JvQ13lwjBmR87Yy9YfEI6RvZNYIngudRj3j1yj8i_DaPz9dkGjJZPMnNUkMxIzxJIQLujyzlLz6lPalSzvNKDEAdZnSqHNbg1apZyhmWZAYFAQkNJO-0xUUTb0SbtlQOOvGxVxd4DMeEIzBybgEKKiHFc2r0brkxM6MRay-IiQytal6yajKDG8O6A2AvHJVJKW1kSyh2i0RirxqVx_TIemzGSAzVSPRCVVYpAbTDLET_8n0HEwuOvHPPamHAgKKJX42WESpBVbadccrswiLC8bsNKdY_2E1egtUHxsEnXVSisD8HNY34_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : هیچکس نمی‌خواست به ایران زمینی حمله کنیم، نه؟!
حتی اگر همین الان هم بهشون حمله میکردیم، رهبران و فرمانده هاشون فرار میکردن به غار هاشون که زیر کوه های گرانیتی ساختند.
این کوه ها خیلی محکم اند و نابود کردن شون سخته.
الان از غار اومدن بیرون ولی اگه بازم حمله کنیم سریع فرار میکنن اون زیر؛
• تنها راه گرفتنشون فرستادن سرباز هامون به اونجا بود.
اگه صلح نمی‌کردیم الان تنگه بسته بود و نفت نداشتیم.
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/15352" target="_blank">📅 23:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15351">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e83d087d.mp4?token=VC97z-eQQTai1W49shkWI7MUcfIQ9ljHLfvgo44oOYuY8rNClfeqnDnn-QGeh6JqMSjzKSkAIvH35SVrFTZn_-EwQsPBsbIAmi_P5dO6XjttBz2gM71jkpjjdsyF3nxavjbN0Lw6qQV2VEsb3JoFrIgSslDjkwgjqM4gJdPn1IWLOSJK3HKWqCtFC_O8t78F5pZDeZlfiOcgKcJKP78x6EaUuHfoLn04ESWCIKmhZTTDeYs5RK2Ekn_8mV9SRAcQuwqlEGDJSYqwm3DFMBgRxdx60Ylj5BaxRuw0_1G2zIlglwufzTMCJrkx6f64cx1Tv_qrJaUmE4JJC2FLPWHBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e83d087d.mp4?token=VC97z-eQQTai1W49shkWI7MUcfIQ9ljHLfvgo44oOYuY8rNClfeqnDnn-QGeh6JqMSjzKSkAIvH35SVrFTZn_-EwQsPBsbIAmi_P5dO6XjttBz2gM71jkpjjdsyF3nxavjbN0Lw6qQV2VEsb3JoFrIgSslDjkwgjqM4gJdPn1IWLOSJK3HKWqCtFC_O8t78F5pZDeZlfiOcgKcJKP78x6EaUuHfoLn04ESWCIKmhZTTDeYs5RK2Ekn_8mV9SRAcQuwqlEGDJSYqwm3DFMBgRxdx60Ylj5BaxRuw0_1G2zIlglwufzTMCJrkx6f64cx1Tv_qrJaUmE4JJC2FLPWHBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در اونجا رژیم چینج انجام دادیم. همشون از بین رفتن.
مارک کاپوتو، اکسیوس:  این چه تغییر رژیمیه که‌ انجام دادید؟ شما خامنه‌ای جونیور رو همچنان در ایران دارید و مقامات بسیاری از سپاهیا زنده‌ن.
ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/15351" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15350">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">همکنون حمله اسرائیل به جنوب لبنان با بمب‌های فسفری
🚨
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/15350" target="_blank">📅 23:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15349">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هم اکنون هشدار بالگرد آمریکایی  به نیروی دریایی سپاه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/15349" target="_blank">📅 23:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15348">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhZjVZNf_jDzFebfijbHgc7t6ZBDIOszeVPRC63JtFiVn7LlaDMfQY4vBoJ6tHKqqsHMXXxrVrJXQkue9yqOge-xKw2aRn-oj7hlcU7jVDckQTFd4gCI8TP7GnLXZgwawmGsnO3FywZcxt1icOZ6zv1EsKiIrHLrA-orr3Ru3WMy3pI9MHt-1T6gkqyEoHzA5XCDwZdRYKSk7WCOg0Y_UkW_SPm0LU0IUzZh3r6FWhfSShFb0FTbPn81NOyN8B1SI-1RoClSugS-WX9_OX7DaPXaVPR4ZbC1wEVhOCOskKNFJuO5Xe5mdh_n7dEAI36ePQLuBP_YOAjUbUiBFmd4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ با انتشار نظرسنجی ای نوشت: توافقی بسیار محبوب، به جز برایِ فیک نیوز ها و شریک آنها، دوموکرات ها!
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/15348" target="_blank">📅 23:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15347">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر خارجه انگلیس: درخواست "به آتش کشیدن تمام لبنان" یک بیانیه وحشتناک و نفرت‌انگیز از یک وزیر اسرائیلی (بن‌گویر) است که به درستی توسط دولت بریتانیا تحریم شده
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/15347" target="_blank">📅 23:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15346">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">روزنامه اسرائیل هیوم به ترامپ: می‌توانستی بزرگترین رئیس جمهور تاریخ آمریکا باشی اما رفوزه شدی
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/15346" target="_blank">📅 23:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15345">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رهبر حزب الله، نعیم قاسم با آتش بس با اسرائیل مخالفت کرد
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/15345" target="_blank">📅 22:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15344">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">واشنگتن پست: سازمان اطلاعات آمریکا اعلام کرده که اسرائیل به طور فعال در تلاش است تا یادداشت تفاهم ایران و آمریکا را بر هم بزند.
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/15344" target="_blank">📅 22:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15343">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آسوشیتدپرس: ایران به امریکا اطلاع داده است اگر اسرائیل ادامه دهد. همه چیز متوقف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/15343" target="_blank">📅 18:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15342">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محمدمنان رییسی، نماینده مجلس:
خوش‌انصاف‌ها(منظورش قالیباف) مجلس رو باز کنید، رهبرم تنها مونده.
@withyashar
قالیبافم باز نمیکنه تا جا پاش محکم بشه</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/15342" target="_blank">📅 18:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15341">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال 12 اسرائیل: نتانیاهو با مسئله لبنان سعی در خراب کردن تفاهم نامه بین آمریکا و ایران داره.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/15341" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15340">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری تسنیم:
هر دقیقه باز بودن تنگه هرمز خسارت مهمیه؛ اگر آمریکا فشار انرژی رو از روی خودش تخلیه کنه، وقیح‌تر و تهاجمی‌تر هم خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/15340" target="_blank">📅 18:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15339">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حمزه صفوی، فرزند مشاور عالی رهبری افشا کرد:
یک روز در چهل سال گذشته نبوده که ایران سودای ساخت بمب اتم نداشته باشد
تمام اسناد IAEA، تورقوزآباد و آماد نشان می‌دهد که حکومت تمام تلاش خود را کرده اما همهٔ اینها در بزنگاه‌های تاریخی لو رفته‌ است.
کرهٔ شمالی وقتی در دههٔ ۱۹۹۰ با آمریکا مذاکره هسته‌ای داشت، در دو سایت دیگر خود پروژهٔ پیش‌برندهٔ بمب اتمی را داشته و لو نرفته اما دو سایت فوردو و نطنز را ما اعلام نکردیم بلکه لو رفتند.
برنامه هسته‌ای ایران، گران‌ترین برنامه هسته‌ای جهان، نه برق آورد، نه بمب، نه امنیت
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/15339" target="_blank">📅 18:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15338">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سخنگوی وزارت خارجه: برگزاری نشست سوئیس فوریت ندارد
یکی از اهداف اصلی نشست سوئیس در روز جمعه، امضای متن تفاهم خاتمه جنگ تحمیلی بود و قرار بود در حاشیه مراسم امضا راجع به ترتیبات مربوط به مذاکرات توافق نهایی هم تبادل نظر شود.
با توجه به اینکه امضای متن یادداشت تفاهم، در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد اما درحال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15338" target="_blank">📅 17:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15337">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">از زمان آغاز آتش‌بس، نیروی هوایی اسرائیل بیش از ۱۱ حمله هوایی در سراسر جنوب لبنان انجام داده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15337" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15336">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک مقام ارشد در کاخ سفید به آکسیوس:
«نتانیاهو با تمدید آتش‌بس در لبنان صد درصد موافقت کرده است.»
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/15336" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15335">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حزب‌الله: هنوز هیچ اطلاعیه‌ای درباره زمان آتش‌بس دریافت نشده است
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15335" target="_blank">📅 17:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15334">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانال ۱۲ به نقل از یک مقام ارشد اسرائیلی: آتش‌بس به ما این امکان را می‌دهد که به تخریب زیرساخت‌ها و اقدام علیه تهدیدها ادامه دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15334" target="_blank">📅 16:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15333">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار المیادین در جنوب لبنان: همزمان با اجرایی شدن آتش‌بس ، حملهٔ هوایی اسرائیل به النبطیه صورت گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/15333" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15332">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">باراک راوید از آکسیوس: یک مقام ارشد آمریکایی به من می‌گوید
اسرائیل و حزب‌الله بر سر آتش‌بس مجدد در لبنان از ساعت ۴ بعد از ظهر امروز به وقت محلی توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر و پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15332" target="_blank">📅 16:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15331">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش ها مبنی بر آتش‌بس بین اسرائیل و حزب‌الله هم اکنون به اجرا درآمده است
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/15331" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15330">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWI3_URizy64ZVI07XpvWliKxLR0Ggto-kzwQIFy5nKPit9RnuwtGIxnF_DJXy8HunEnMt89UyDpo4N_JCwp6uV8L013XssZB6kvfgRWHssN51WWjyhJx6eHfC9jpMqvvoXegmbj4dZ-PGV6Gu9r50I-xUyZbvXfqBnWOqSE6BjJvVwBsFdk93WualJ9AkFkl88z4pvOsXjA0_Z7r2Mte6_CGTtuOiwjVbj5O2tZD7Os2cQQRYXEulLtNpBxhuMmITfyL8ncfpVncA5YpzE6gEM5WzSyLfHbrSddEpJV2PbLeyL1RIfiQt8R4JPlnEdsO_QrPuG3naSHro92XLWUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از یک مقام آمریکایی ادعا کرد:
«حزب‌الله و اسرائیل با آتش‌بس موافقت کرده‌اند» و افزود که مذاکره‌کنندگان از آمریکا و قطر با حمایت ایران به توافق کمک کردند.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15330" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15329">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7oEgEysSkE-oNE6DDCHFL5oYHtIwuXoboMVWBjTSUxxpcrk9Rs9GgRBRXUgNEWWdq70_Gdn4WsdDJn0roa5LERsqhJIzN47HEvUfgcs2_rN4Jh9QJOK79bSyPAwMVFBvgELkFQSonPj3q_i7grY9A1SLLTVASRDNoN5CpXdQNCZ60x21hnBSuLD1Xau0kzstDKXwLYDufaQWVmlymZGJHUvzpv8aqaKaqCWBY60_Bnf-gVBGwisEq11DGxWnaBiN_Tx0SlMuPg6TsRj588qvPvncb47bt-5oTk1cOS5vCAMOGkYNPacIHh0MqUVWeQ7yEr6V_MBsf_WKlA95k4KcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : ما از روی استیصال نرفتیم سراغ مذاکره
این ایران بود که بهش نیاز داشت، کارشون تمومه!
همون ۶۰ روزی که گفته بودیم رو جلو می‌بریم، هیچ پولی هم گیرشون نمیاد
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15329" target="_blank">📅 16:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15328">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5PInIuhAf-ppET1BAybZ9ML0ZXdmfmzI0g8uqT68cPjPSyJOnU1KNTZkGak7rqe52gmq-w3U9WkCSxbwhSdPWIog_smXa5tKhfXmiSJEpiY57jWQPQy7DrrA0_k-OrqW6knFtc4H2iX24IaXeU5wx1Ph7z-hsUUn3aLmSOfERJBbifHkOaAhg4XUPW6kjCoaFFQLqItujSWLPvFM9sirI8jnxkTPxO16Dzr8IYh14N6apmFiiEHlFOYi8VyjrmHglwIfCgyWuy0ooofqKsKZ1CL_z_rlexSlRH5HaGknn6n4NH0vlsEwHW7zIoVVVD9UyUPXqvhtP7M_YW7q_VGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ در‌تروث : جنگ ایران را تضعیف کرده و دیگر نیروی هوایی، نیروی دریایی، پدافند هوایی، رادار یا تقریبا هیچ‌چیز دیگری ندارد؛ با این حال دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش در وضعیت بهتری قرار دارد. باور می‌کنید بتوان چنین حرفی زد؟ بعضی افراد چقدر می‌توانند احمق باشند؟
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/15328" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15327">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سنتكام: جنگنده‌های اف-۱۶ به گشت‌زنی‌های خود در خاورمیانه ادامه می‌دهند و آماده مداخله هستند.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15327" target="_blank">📅 16:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15326">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">طالبان استفاده از گوشی‌های هوشمند رو برای تمامی کارکنان نظامی و غیرنظامی خودشون ممنوع کرد!
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/15326" target="_blank">📅 15:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15325">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f67ff589.mp4?token=aV01hN8PpIKjr9Ai6IB-xYvpANd4Q3XdolJfB73Bn405dkGoIl1mXbJCMIVq39vtwxDuWpnneh3Hvsjt0FxCPvOI5Vi3bj334-vehRGpIB7GsQ-LgVP8cet0eteohv0MZcZdm4d75aPL__uIwIIyk9TIEp_CWij7d-_F7yhcH1Opx3E9s1623v3wx89Uf0TFA14ylyIxDHSzRqqGc9AnNsq5Rmts5Aw_8YoFdmBNyhc2lJOBDSt9vDqFsMFK6QwBwwdQ4_rLittI-LXFES4KzvWhOAct9xAQ969KnRE8F-6SWJPO-OrIyH8OKP96fT2hJRiJ2qENc80s5vZVIND1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f67ff589.mp4?token=aV01hN8PpIKjr9Ai6IB-xYvpANd4Q3XdolJfB73Bn405dkGoIl1mXbJCMIVq39vtwxDuWpnneh3Hvsjt0FxCPvOI5Vi3bj334-vehRGpIB7GsQ-LgVP8cet0eteohv0MZcZdm4d75aPL__uIwIIyk9TIEp_CWij7d-_F7yhcH1Opx3E9s1623v3wx89Uf0TFA14ylyIxDHSzRqqGc9AnNsq5Rmts5Aw_8YoFdmBNyhc2lJOBDSt9vDqFsMFK6QwBwwdQ4_rLittI-LXFES4KzvWhOAct9xAQ969KnRE8F-6SWJPO-OrIyH8OKP96fT2hJRiJ2qENc80s5vZVIND1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاهره و بیروت ما داریم میایییییم
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15325" target="_blank">📅 15:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15324">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تحلیلگر ارشد و رئیس کل ستاد مشترک ارتش اتاق جنگ ، سر ادمیرال یاشار : مسیر قاهره از بیروت میگذرد @withyashar
🎖️</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/15324" target="_blank">📅 14:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15323">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرنگار العربیه در سوئیس: مذاکرات بین آمریکا و ایران ظرف چند روز آینده آغاز می شود
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/15323" target="_blank">📅 14:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15322">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ به طور هیستریک عصبی به ثانیه در تروث در حال پست گذاشتن است. خواهیم دید چه خواهد گفت.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15322" target="_blank">📅 14:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تحلیلگر ارشد و رئیس کل ستاد مشترک ارتش اتاق جنگ ، سر ادمیرال یاشار : مسیر قاهره از بیروت میگذرد
@withyashar
🎖️</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/15321" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الجزیره : نتانیاهو: حزب‌الله بهای بسیار سنگینی خواهد پرداخت
نتانیاهو افزود به ارتش دستور داده است در واکنش به «نقض آتش‌بس» ضربات شدیدی به حزب‌الله وارد کند.
همچنین ، ارتش اسرائیل حدود ۸۰ هدف متعلق به حزب‌الله را هدف قرار داده و «ده‌ها عضو» این گروه را به هااکت رسانده است. همچنین امروز یک مقر فرماندهی حزب‌الله در منطقه بقاع هدف حمله قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15320" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مشاور هیئت مذاکره‌کننده ایرانی، مرندی: نظام ترامپ به توافق پایبند نیست. و ایران در این شرایط یادداشت تفاهم را اجرا نخواهد کرد. اقتصاد آمریکا در معرض فروپاشی است و اسرائیل مجازات خواهد شد. @withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/15319" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروی دریای سپاه در بیسیم کانال ۱۶ دریایی: “از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/15318" target="_blank">📅 14:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش‌ها از شلیک مدام قایق‌های سپاه در تنگه هرمز حکایت دارد.
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/15317" target="_blank">📅 13:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">باز‌ تنگه دعوا شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15316" target="_blank">📅 13:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دقایقی پیش براساس گزارش مستقیم از چند کشتی در خلیج فارس، سپاه پاسداران حرکت تمام کشتی‌ها رو متوقف کرد و عملاً تنگه هرمز رو بست.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15315" target="_blank">📅 13:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر امور خارجه پاکستان: علت آغاز نشدن مذاکرات سوئیس به دغدغه مقامات ایرانی به مراسم ماه محرم مربوط میشه.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15314" target="_blank">📅 13:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15313">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مشاور هیئت مذاکره‌کننده ایرانی، مرندی:
نظام ترامپ به توافق پایبند نیست. و ایران در این شرایط یادداشت تفاهم را اجرا نخواهد کرد. اقتصاد آمریکا در معرض فروپاشی است و اسرائیل مجازات خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/15313" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15312">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شبکه CNN به نقل از منابع آگاه اعلام کرد که پیش شرط ایران برای شروع مذاکرات در سوئیس توقف درگیری‌ها در لبنان است
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15312" target="_blank">📅 13:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15311">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3d24142f.mp4?token=HpzeMUFvKgmCZC5mYz8vS3MxXoZ5zagqlXLyExxOUHoUdEcT_yjssvCN_RuqdoDUKnuAVHGLVF-HIEtNiSvK89h1W55QswrVGqM8KW_ejWNuO7nfvkTxixn8hMo-afAimh5QtS10FWrWZj_zs4-ms9h3NfencqXaYVkQ1B_lwNzWhM8E8y-FVIAlHHlks6xJS-VlXl9hED3efY20mBu2BLDurdazSoBM-p3hfq0qm5Q_OygiSt6lbj6jxKXh8VxlTY0pVxwMWr-J5aWsda12rtBq66bkEv9ZSuVOsH1i4ZvBVGXLxEvT-C-OXNzr3O2i7sYdhuLvXkLakcSnhv0YMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3d24142f.mp4?token=HpzeMUFvKgmCZC5mYz8vS3MxXoZ5zagqlXLyExxOUHoUdEcT_yjssvCN_RuqdoDUKnuAVHGLVF-HIEtNiSvK89h1W55QswrVGqM8KW_ejWNuO7nfvkTxixn8hMo-afAimh5QtS10FWrWZj_zs4-ms9h3NfencqXaYVkQ1B_lwNzWhM8E8y-FVIAlHHlks6xJS-VlXl9hED3efY20mBu2BLDurdazSoBM-p3hfq0qm5Q_OygiSt6lbj6jxKXh8VxlTY0pVxwMWr-J5aWsda12rtBq66bkEv9ZSuVOsH1i4ZvBVGXLxEvT-C-OXNzr3O2i7sYdhuLvXkLakcSnhv0YMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توقیف یک دستگاه نیسان گاوی عجیب برای اهداف خاص توسط پلیس
@withyashar
🤯</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15311" target="_blank">📅 13:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bffa7007.mp4?token=bqI7-R2sEvzDtz4BZcvDQdBeOQFikrg88ad1gwUnuO4sijRc_3cu6zWD9H4bKKmCAZFwUMj9q3sbO237MW3A7RXsSl4tRjxoMxjzXBqUqz0N8nNa5ypCKzm1DPIrbOLezqMBuy-B8f98sQq5RFn69D4XhRMO-krlclfAv5ZWWvTxZ7V1W0-SOLzya_DxD7N5K310KUHQY71k-nlIeoQcPIrx5nc9Iiw9IM9PsGS04ka3minzP80RaX2890KKPkFKrVPZvS8o0uQvKWtAzLPlyWSjTVTBgj8IKzUUmGp5vWMpr0D6yDJvcqMGiNenJHIgyTmDl1HnwL3ju1W6TAS7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bffa7007.mp4?token=bqI7-R2sEvzDtz4BZcvDQdBeOQFikrg88ad1gwUnuO4sijRc_3cu6zWD9H4bKKmCAZFwUMj9q3sbO237MW3A7RXsSl4tRjxoMxjzXBqUqz0N8nNa5ypCKzm1DPIrbOLezqMBuy-B8f98sQq5RFn69D4XhRMO-krlclfAv5ZWWvTxZ7V1W0-SOLzya_DxD7N5K310KUHQY71k-nlIeoQcPIrx5nc9Iiw9IM9PsGS04ka3minzP80RaX2890KKPkFKrVPZvS8o0uQvKWtAzLPlyWSjTVTBgj8IKzUUmGp5vWMpr0D6yDJvcqMGiNenJHIgyTmDl1HnwL3ju1W6TAS7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب رسمی‌کاخ سفید: دیروز ترامپ تو نشست سران جی7 وقتی وارد شد بلند گفت رئیس منم
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15310" target="_blank">📅 12:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15309">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B07PdT2OvqF0WW-Xs1lXpcwWwpoPmNlj4flyF4G8BfuJsgIRmH3grW9dzbnOCJkcmA7sMnXfXS3XCdk6Qw2wp7h4SaMt1lmG5goY21mbbyFFDA5YlJ_jRDZaFZ_l-xS25WZ6ZpbVdtdrRP9neWLpaAFMAsGWZ8nl92KKImnxdlivRJTVmXVl6yGTsR7WINVRGm2F0AoGmvnouRzaFJoX_U5yIOf9tj0eFg7bzdWLEXc4vX0LSn2RkXNDp9mktCYox6v_d170HAom8qoDG1x6FL7heRIFmn9ELwRyFWbEFg210zaPLcpIiRMyuhm4PNI_MSQ7-M4cmw1IkNGo_X5-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: ۳پا چندین سلول مخفی در عراق ایجاد کرده است تا حملاتی علیه کشورهای خلیج فارس که میزبان نیروهای آمریکایی هستند انجام دهد، که خارج از ساختارهای فرماندهی سنتی شبه‌نظامیان عمل می‌کنند تا خطر شناسایی کاهش یابد
سه تا چهار سلول، هر کدام متشکل از حدود ده مبارز شیعه عراقی نخبه، حداقل هفت حمله پهپادی بین ۲۰ آوریل تا ۱۷ مه علیه اهدافی در کویت، عربستان سعودی و… از محل‌های پرتاب نزدیک بصره و سماوه انجام دادند.
برخی اعضا از مقاومت اسلامی در عراق جذب شده‌اند، اما سلول‌های جدید مستقیماً به سپاه پاسداران گزارش می‌دهند نه به رهبری شبه‌نظامیان مستقر.
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15309" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c913f668.mp4?token=nLArA8TCaSwXElcGcBUWVaY6xtGjGtPPcslM2geE3yN0ioFLg77o67_ypnn-a1yF1U5obe09VklIhpuUVzg7W-eJr5cypbYK2oNctofK7BlMT9qagEwHA6SWyQQJVBpItYJmea2hw7h8xOhpWfc7JBZclGQFtMzLIVHVrT_7K0m2Yr8GvNvITeu_luspiTNQP_9i-p_osxRXXptMYlYdGPkCfDfeGXVmMolLL8yCNZTj4P1u9zJa9Bgxe7me36s1sFtU9ymD16D7k-l8FZVMRrDWr-LTGsdofEXNi0jTlqEwL4uaTBNsbcGYjHsjXKUtRqOU0WXfiVnXyVl0TKJSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c913f668.mp4?token=nLArA8TCaSwXElcGcBUWVaY6xtGjGtPPcslM2geE3yN0ioFLg77o67_ypnn-a1yF1U5obe09VklIhpuUVzg7W-eJr5cypbYK2oNctofK7BlMT9qagEwHA6SWyQQJVBpItYJmea2hw7h8xOhpWfc7JBZclGQFtMzLIVHVrT_7K0m2Yr8GvNvITeu_luspiTNQP_9i-p_osxRXXptMYlYdGPkCfDfeGXVmMolLL8yCNZTj4P1u9zJa9Bgxe7me36s1sFtU9ymD16D7k-l8FZVMRrDWr-LTGsdofEXNi0jTlqEwL4uaTBNsbcGYjHsjXKUtRqOU0WXfiVnXyVl0TKJSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:حملات را یادتان هست؟ آنها وارد می‌شدند و بیرون می‌آمدند.ما وارد می‌شویم، نابود می‌کنیم و آنجا را ترک نمی‌کنیم. این کاری است که ما اکنون در لبنان انجام می‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15308" target="_blank">📅 12:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15307">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuAfDZcMQKHGxbYegFrW7lk_ibgpxXKeglN4RY2ooklsOtOA7A07007paPIZPjDkvTE5Beo_J2w1-suq3_AC_kW1erTq4_1-KGXOZxscxffZMgHGjd6-7dKjV-VJUWhlEgnbO3q_IFNzDtbjAM1THeZSLXRvzrVSoXb07v48-Z5y7gfIDzQGasTFtugYyCrdf3GGDiMjGaOKq7QHfjwy-RGOlKQ3vHW11GtRglNSLzaarPBBxrbOhCHtDuOLpj3TkfzZftS_C64GGvDpVHsaYOXOzFQXLvvd34ICKGs2I4I4VwqCdD1rqrEnmipgLCnKantY_gr1ZBGibog2uPeJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ارتش اسرائیل ساعاتی پیش در بعلبک، در عمق حدود ۸۵ کیلومتری در عمق لبنان. حمله‌ای غیرمعمول در عمق آن - ارتش اسرائیل در ماه‌های اخیر تقریباً در دره لبنان و منطقه بعلبک حمله نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/15307" target="_blank">📅 12:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15306">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd1e599ede.mp4?token=UUC9s-ussMWLqEPE-SIr3iu5fg9kUvN6bMu9Blx2i4i9kFpTc-fETFjJ6ojVLpmy6SAQ-oLWfRWnD5Io2j6qaIbHvv9vqNUHMlDP3QgS7mTi3738RxMGF9uSGtg91ce0vCARePs0K9V0xjcPifPYGziijVQ9Peoa6xKvR8P8wTdBL8DKy4ld-euKPexDKHJG50tBFUM3XCbXHG-I9TqRasG8Us5wsH_XamXnvWWXcWlYQKM3snniD8FUlItKPDYXuQr80VxpwDc837VUGtc0KH5feXxbp5nkseJpPbw_RrJZCXAT7NE9WeXaCgyw8Ry1UOVqT-XHkucHG7HSuEFvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd1e599ede.mp4?token=UUC9s-ussMWLqEPE-SIr3iu5fg9kUvN6bMu9Blx2i4i9kFpTc-fETFjJ6ojVLpmy6SAQ-oLWfRWnD5Io2j6qaIbHvv9vqNUHMlDP3QgS7mTi3738RxMGF9uSGtg91ce0vCARePs0K9V0xjcPifPYGziijVQ9Peoa6xKvR8P8wTdBL8DKy4ld-euKPexDKHJG50tBFUM3XCbXHG-I9TqRasG8Us5wsH_XamXnvWWXcWlYQKM3snniD8FUlItKPDYXuQr80VxpwDc837VUGtc0KH5feXxbp5nkseJpPbw_RrJZCXAT7NE9WeXaCgyw8Ry1UOVqT-XHkucHG7HSuEFvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:تمام خط اول روستاهای لبنان ویران شده است.ما در حال ویران کردن تمام خانه‌ها هستیم. ساکنان دیگر هرگز آنها را در مقابل چشمان خود نخواهند دید.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15306" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15305">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم. @withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15305" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15304">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هم اکنون منابع لبنانی می‌گویند:
ستون‌های زرهی اسرائیلی در حال پیشروی به سمت نبطیه، پایتخت حزب‌الله در جنوب لبنان هستند و درگیری‌ها سنگینی گزارش می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15304" target="_blank">📅 12:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15303">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575f785e69.mp4?token=oBy5CPXBpKcNXT-Y_444FTsoS22m9XkV84aIsTJZjoNjRTpwJBC79SxMfCKdWkpw7__Py6p2ChR9Mgg1_q6SuOA9S8SYpWhqJyJxU4_zt06rBe618gZ3rkevHG_mnpNz4ctY6BbUj0NZHiPkxzQjAE0cN1s22cV7ZbSPZZZuMYQ7tembS0CU7aW3hGCGMZayRzKstr53UGuVqxj05shWmhxSX-IoK72g30XwV7d5_gU7jLaBKlQjzVYkSRXOhiFIX38K_SynJqZQGE8T9vQQmjs7cNETs4psRWHgpippLonPjpQ35Yv6PYfpsz6PfKPECQWrC6vwa9PgyIPOfRfK9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575f785e69.mp4?token=oBy5CPXBpKcNXT-Y_444FTsoS22m9XkV84aIsTJZjoNjRTpwJBC79SxMfCKdWkpw7__Py6p2ChR9Mgg1_q6SuOA9S8SYpWhqJyJxU4_zt06rBe618gZ3rkevHG_mnpNz4ctY6BbUj0NZHiPkxzQjAE0cN1s22cV7ZbSPZZZuMYQ7tembS0CU7aW3hGCGMZayRzKstr53UGuVqxj05shWmhxSX-IoK72g30XwV7d5_gU7jLaBKlQjzVYkSRXOhiFIX38K_SynJqZQGE8T9vQQmjs7cNETs4psRWHgpippLonPjpQ35Yv6PYfpsz6PfKPECQWrC6vwa9PgyIPOfRfK9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/15303" target="_blank">📅 11:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15302">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد @withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15302" target="_blank">📅 11:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15301">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دو حمله هوایی به لبنان
الجزیره از دو حمله هوایی اسرائیل به شهرک عین بورضای و حومه شهر بعلبک در منطقه البقاع در شرق لبنان خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15301" target="_blank">📅 11:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15300">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq0EUxBcwUzXMaBg1WjnnZeAUVNTXsDwArLWNT_S6-UmeT1K_kZwN7aKyeKC6b9vOGs0zfs6QR1bwru6yLNH88QUhSQ82liuYcZ6oOnZxiTvcQrhB5ZGFDD_yKPXcW6_TCT5RUzuKkD0HQGzt8qE-w3nq-GRh0sh14vHeuNZAhniJDe1O-7qLIb3uCbXNS4Kd413plwyIjvuDgwAXvcY62p7h61XnpN21Oe_ucnN29gdI9j6M5NMOw15hGSfn40bOj8Tacj4I9PBKYEa7nprhiv-J8G87L3QdbZdiToPR6Ns7yrUUSVZ_bJCFbvqX8OfKhuercxeNd70Id_-goz3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : یک ایده جدید:
دست از قلدربازی برای متحدانمان و چاپلوسی برای دشمنمان بردارید.
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/15300" target="_blank">📅 11:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15299">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/15299" target="_blank">📅 11:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15298">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بن گویر وزیر امنیت اسراییل:به ازای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید گریه کنند. کل لبنان باید بسوزد
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15298" target="_blank">📅 10:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15297">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyfFGSCb5hkYp_MJ8wrh1Ys60C0Lvvmw5Gx3JTmpvdyCz24VdR38Eop5AYCZrLyiEb6Ws0V0YLZxEwDEQMw8DmEdDfXmQe96zt3bl5HzoZY_v11sf7O35F9aA7BZW2ioBKOdmk1ZB5LisuSSy8qHexe1hlSELKhMnNdbXvNdyZ8JfN9RR56dsFBWMZBa4r-CSo4DGUDursbV2ZGfYkOoKph0FobQuJo4-qVkoiV5V99MYVr0O8XybPXxaZq1FymrLf-_D0QZ9WcJ6rq_cY9E3L6fBd-VMKn0OIyPktWYSRhX8kWmB1nW6zKq3xHGcORL514Wva0NRm-vsz6200b8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لورا لومر خبرنگار نزدیک به ترامپ جاویدنام های دی ماه رو حدود ۱۰۰ هزار نفر اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15297" target="_blank">📅 10:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15296">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602da85ed4.mp4?token=K9Xufp7XJiOlVoqEiRyCsBFPz0uZA0bcjtUhb-1c4y8xXblKJ899udNWxRcKodcWen0Yz5gE-ge7kPRiHTljIrsD_OtRhKaZcHrCzgc83sl7qWpJ0gqOQdAhD72qvrfdaCnDjG7aNSrnIc4CU-ErYnOdA8U7vqQrLFPvfMKj3mTeqP3aDRX0hRSkaRQb9B_-hhXhcy-pq148M_PlJ97AZ_DsLjOvBxtYgkCcmu582xd714QZA7GA680v8AW-eyxXw7l8DWVvsR3k_xOn5pZ_EiMbhJKiNzzrrS2zD6eVc_gUEgc6_JdPmW18Ef0-6_Af6Dws71LqgYPp7d1r0WhbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602da85ed4.mp4?token=K9Xufp7XJiOlVoqEiRyCsBFPz0uZA0bcjtUhb-1c4y8xXblKJ899udNWxRcKodcWen0Yz5gE-ge7kPRiHTljIrsD_OtRhKaZcHrCzgc83sl7qWpJ0gqOQdAhD72qvrfdaCnDjG7aNSrnIc4CU-ErYnOdA8U7vqQrLFPvfMKj3mTeqP3aDRX0hRSkaRQb9B_-hhXhcy-pq148M_PlJ97AZ_DsLjOvBxtYgkCcmu582xd714QZA7GA680v8AW-eyxXw7l8DWVvsR3k_xOn5pZ_EiMbhJKiNzzrrS2zD6eVc_gUEgc6_JdPmW18Ef0-6_Af6Dws71LqgYPp7d1r0WhbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری اکسیوس: در مورد نه تنها اعمال قدرت، بلکه محدودیت‌های قدرت خود به عنوان نتیجه از درگیری ایران چه آموخته‌اید؟
ترامپ: هیچ محدودیتی وجود ندارد. من هنوز آن درس را نیاموخته‌ام. می‌دانم که وجود دارند، اما می‌دانید، هیچ محدودیتی وجود ندارد. ما آن‌ها را کاملاً از نظر نظامی شکست دادیم
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/15296" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15294">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb0c5fe35.mp4?token=Np1eHHzDKGHZJqvoa617pnn1qzi0CwDQEt5KHV3zP9TdJcNDtXerJjWJrz1OOIrXwB2P_UC5Vu1FN2ncJ_6_0q2SAB0K1S5m_QjPu-Bosokj6unRHmLwtMyWWcYOU8fHBzrJ1wMWgLxDSYhd7yc4Lm2W9XwMHAqV4xodstWgcW9qGvHeRS6RyPpAeqOXuzUaoBVbzQRWXrtm0foYxAdViEB739buq4b41RdGQWwV89l49RGud12lAdHT5k_lheZE5Oy7Q5Vv9m9kEP7JtU77lv84lJDnuy04mU-yEysn4lryLuDYM2x66IYehGFbPa7juaEP7rFbS_IWaO9iKPtIew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb0c5fe35.mp4?token=Np1eHHzDKGHZJqvoa617pnn1qzi0CwDQEt5KHV3zP9TdJcNDtXerJjWJrz1OOIrXwB2P_UC5Vu1FN2ncJ_6_0q2SAB0K1S5m_QjPu-Bosokj6unRHmLwtMyWWcYOU8fHBzrJ1wMWgLxDSYhd7yc4Lm2W9XwMHAqV4xodstWgcW9qGvHeRS6RyPpAeqOXuzUaoBVbzQRWXrtm0foYxAdViEB739buq4b41RdGQWwV89l49RGud12lAdHT5k_lheZE5Oy7Q5Vv9m9kEP7JtU77lv84lJDnuy04mU-yEysn4lryLuDYM2x66IYehGFbPa7juaEP7rFbS_IWaO9iKPtIew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در آغاز درگیری ایران، شما صحبت کردید که فقط تسلیم بی‌قید و شرط را می‌خواهید. تفاهم‌نامه شبیه تسلیم بی‌قید و شرط به نظر نمی‌رسد.
ترامپ : واقعاً احتمالاً تسلیم بی‌قید و شرط است. من اینطور فکر می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/15294" target="_blank">📅 10:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15293">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزارت خارجه آمریکا: حزب‌الله باید خلع سلاح شود
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/15293" target="_blank">📅 10:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15292">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه  رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:  https://t.me/+hLt81qXCGTQzOWQ0 https://t.me/+hLt81qXCGTQzOWQ0  لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/15292" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15291">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دلار داره آرامش قبل طوفان رو تجربه میکنه و ممکنه بزودی حرکت بزرگش رو آغاز کنه
رفقایی که نمیدونن دلار میریزه یا رشد میکنه عضو این کانال تحلیل بشن بهتون میگه:
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0
لامصب اطلاعات رانتی داره</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/15291" target="_blank">📅 02:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15290">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش های محلی در جنوب لبنان،
از حملات هوایی سنگین جنگنده های اسرائیلی خبر می‌دهند،آسمان جنوب شرقی لبنان به دلیل شلیک گسترده منور های روشنایی ارتش اسرائیل روشن شده است.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/15290" target="_blank">📅 01:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15289">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.  https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433  ترجمه :    ببین ترامپ،  می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این…</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/15289" target="_blank">📅 01:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15288">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کامنت جدیدم زیر پست ترامپ، لاتیش کردم
😂
فقط همین کامنت رو لایک کنید . ترجمه در کانال تلگرام.
https://www.instagram.com/reel/DZvkK0jpILu/?comment_id=18367681780225433
ترجمه :    ببین ترامپ،
می‌دونم دیر یا زود این کار رو به سرانجام می‌رسونی، ولی رفیق، این دیگه درست نیست. مردم ایران از این همه انتظار و بلاتکلیفی به مرز دیوانگی رسیده‌اند.
این داستان را تمام کن و کار را یکسره کن.
خیلی از ما در این ماجرا کنار تو هستیم، اما باور کن این آخرین تغییر رژیمی است که حاضر به حمایت از آن هستیم. بعد از این دیگر چنین چیزی تکرار نخواهد شد.
عشقی.</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/15288" target="_blank">📅 01:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15287">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر دفاع اسرائیل:اسرائیل توانایی انجام عملیات مستقل علیه ایران را دارد و در هر لحظه برای اجرای یک عملیات آبی و سفید در ایران آماده است.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/15287" target="_blank">📅 01:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15286">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل سموتریچ:
غزه در ویرانه باقی خواهد ماند. در نهایت، مهاجرت رخ خواهد داد، زیرا در دهه‌های آینده چیزی برای جستجو در آنجا وجود نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/15286" target="_blank">📅 01:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15285">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: پیت هگست قراره خیلی پیروزی های دیگه بدست بیاره پسر خوبیه
من فقط مردمی رو دوس دارم که طرفدار من باشن
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/15285" target="_blank">📅 01:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15284">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.  https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==  اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15284" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15283">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">subseven</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/15283" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15282">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/15282" target="_blank">📅 00:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15281">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این پست جنجالی را از دست ندید، کلیک کنید و کارهای اداریش را انجام بدهید. حتماً تا انتها ببینید.
https://www.instagram.com/reel/DZvdCMHxeYT/?igsh=MW50eDUzOWQ0MnFzYw==
اتاق جنگ با یاشار : Bagher.exe</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/15281" target="_blank">📅 00:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arGZpyDeD7yXxKb45zdSMzpL9WoTjPRY1l6nrtxP4ye3jdAVEeE1lDI-RVb5Gvt2cJ1Jd2NOcHgrzILFnKykvqvDigvGBuzkQpDmUcK2P7SJAVyEn4Z4xJArE7YpUezWx5UxGZGMzFKZX3-MrcTJzVgvuNqNsYDnEx_Zsm5ekpEu7xg04ll78ntMdTFnmiIyKTPUXRJtZubTH9__WD7tk2QmlWPpV66I3dgGh1joGJg8l3zTsfunHFS2k4mCA_vWRmJC8x47GGJmgvPebTqYtsXyaw-mzm7h8AEoNZNZQ99ygKe0WDEUTRvfQDkUktRaTs-1nNuZsRD6eONquGe0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/15280" target="_blank">📅 00:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزیر جنگ اسرائیل: قدرت ایران را درهم شکستیم، رهبران، دانشمندان هسته‌ای و زیرساخت‌ها را هدف قرار دادیم و برنامه هسته‌ای ایران را از بین بردیم؛ اکنون باید اطمینان حاصل کنیم که این برنامه دوباره احیا نشود
اسرائیل در هر لحظه برای عملیات مستقل در ایران آماده است
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/15279" target="_blank">📅 23:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">المیادین به نقل از منبع آگاه: هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15278" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRHv8WKeaaVEuyzNi5lN1YpoRt_D2UQqNQ-64hY_vdY7PgxJK6poEMHjg8qFHS8akPlWfz1aIKNywS9YmOO2gyf2XTC5glagbGvg90kB0w6qgNlgiIrUWC7TPIVn1uW85ekoEzLy7UBHdM3-lMzXCqodVBmaNWxzzpcwYIvfIyz9fac4-TXAM31jnjelRJGWewb6Nu17MITFihtBU25dGfWteDUvlZbFSWwWZT_vh14-vo0xc4j0iuUMqx-O3sOtOg2SflccKpzfov_ieXK8kXyKp2Kq8oK0P4dVoxbfrXmscHPgtR2kv04mtkN7o7DgtjLx6LTwjYhlDKDhqlJ07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: ایالات متحده به صلح متعهد است و ما از همه در خاورمیانه می‌خواهیم که به تعهد خود برای پیشرفت عالی مذاکرات ما پایبند بمانند.
بازارها از آنچه اتفاق می‌افتد هیجان‌زده‌اند:قیمت نفت به شدت کاهش یافته و سهام به سرعت افزایش یافته است.
ما انتظار داریم آتش‌بس کامل در تمام جبهه‌ها، از جمله لبنان، «حزب‌الله» و اسرائیل برقرار شود. از توجه شما به این موضوع سپاسگزاریم!
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/15277" target="_blank">📅 23:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شورای عالی امنیت ملی:
بر اساس تفاهم‌نامه منعقد شده، تا ۶۰ روز هیچ‌گونه عوارضی از کشتی‌های عبوری از تنگه هرمز دریافت نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/15276" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromyegi❤️</strong></div>
<div class="tg-text">به یزدان قسم فقط کانال خودتو میبینم و طبق تحلیل هات روانمو سالم نگهداشتم وگرنه با این توافق الکی که پیش اومده خودکشی میکردم
😮‍💨
دمت گرم
🤍
من به تغییر رژیم ایمان دارم و میدونم طبق گفته شما زمان بر هست پس صبر میکنم
پاینده ایران و جاویدشاه
👑
✌🏻
❤️</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/15275" target="_blank">📅 22:18 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
