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
<img src="https://cdn4.telesco.pe/file/ssDHd6s_djXWaajl1LAI4_MlYBwQRQj0VEKv7ISYDGdPUG6qgk9Lgai81jzGsn_Pb1R9Y5V1l9dcjbxKBOVkHd5XNfBA2vDtGD-hlYylTk42MVg529VS-JocyhaLU9j_0EHoIrYF1FIwJwuZC0JEKAeKI6G6UZ0zHGsK5532HrenFI8lvDgjR1sX8nYuRjvRjQU7BnpP5YY6uzNFcqY0oldsiJm1uSQp2X4ZGnCp3-nk7EVeHpRMkleqKvbr6p2S1xFTthq0X7pUeBQmNy5fnzlUpn2Ez5_ak_9SBPQLAndK0AcDOVYRD1p9XpIjLtwcvP-Yaz2uITSF4YrFftZlYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 246K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 02:31:12</div>
<hr>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=jDvKGaUDDRAMyT-i3bB0qiIFl48Pbofv2zDSD7ImuR420dH66qiVTIBPKljRuH039pp-_LJo7MOmzi4KAwffTcBzOpHy8v-x1XO_rtb7m4QVRLv8nnXZth4n6VVrDcWF05oqHu8xNvXQLuoJwZFjQx918nZ1ryx8nKsryyv9S3gsqUSythpTcdMFEXpBtHi-Axq6M6YjncYI9bujLNY0CbRHyMMFLm0mp83FgOwMW47viN9E3lfAGXDnm4SPQaQfEXxqjcKwgNykFQ6Es9Gvxs0Q7CzTEtb-rp4k-ExBBxF9xpAIku2gr54CngkQRCbYsO3vOIAykl5IJMWiZSsspA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=jDvKGaUDDRAMyT-i3bB0qiIFl48Pbofv2zDSD7ImuR420dH66qiVTIBPKljRuH039pp-_LJo7MOmzi4KAwffTcBzOpHy8v-x1XO_rtb7m4QVRLv8nnXZth4n6VVrDcWF05oqHu8xNvXQLuoJwZFjQx918nZ1ryx8nKsryyv9S3gsqUSythpTcdMFEXpBtHi-Axq6M6YjncYI9bujLNY0CbRHyMMFLm0mp83FgOwMW47viN9E3lfAGXDnm4SPQaQfEXxqjcKwgNykFQ6Es9Gvxs0Q7CzTEtb-rp4k-ExBBxF9xpAIku2gr54CngkQRCbYsO3vOIAykl5IJMWiZSsspA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAN7-mz-ZHNUhWPvizZBEJeYf1ieLq-atVzOfX4RHp2rPwTmIDSPPmbxSxDF3xlR9T68IcX79LEBXd2bOIOal8dYBLebitYUbEJHdxz_Vas89tgpd0Ck38OJTA6kjL2O51BrI6X6RSOnn-fe5G3IWRF10cRh3CmQKyDCRxKQFAaZMBBzcsVgcXlyeEAsUu7XzN1_ALojBTwNYQz73LCmNdVkYuFQ0wPQJxz1iKJmu-aH3LulgCYWxr3yPJPfpDAzhyjIi-YHkDYXUjmXwygSmRc0ZIsrzkiXtJ9_BMvXp__Z9I-gtfqt9n4rKH-lcXrTLmJeeDy-MPPG4qWcv58hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLfWNDOYzWu7ijCi6TyT2MIuNoGt5CkRMUVEfX_N0BfmOf4UiGnMk1WGwQ7vXy8uhmGtuVUD4aZQ3-OaA1OwcacrRaoIdwwy8VpGD2dXFue4mb4s_6QPgEZbFFvAqJ8AhgSagtWZORZz2Zr53hkfXZmcVX8PO_RJS_ye2-KSvp5jtNCgZsz86UaJgR-1GGA-Ub6IQ7yQ1qoHIqJQ1jsfd6YSrS5eIWuTP-pXfKysRuUC9vl12keVRGXL0OBOLrVBZvsMTrznW3PLw-MMznWZjvgARATnbLZoguQKfjpzcisTxdFprctISDQdir7JKyWdOcbKpivnn220jqY9XzaB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23404">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Vgr99u2E-t3Um9JP9H8w7qZBSIM-THWeP7B9GyMoZ4q89FO3gqCKKD_jnvOvGzjy5QTs0aHl00Ijv9Aw4YdR2mFcnFDQW0U4sQ7JqhHp4VAGEsmM5dSe8cjsn3qIIaNcj5X9JpzTiaiPDDr_-9wfUf-N2F2ue0wdr68LOM4XM-ebxrmf2CxcfLQkZOqwTNRb8Zlh3-Ke5ZQB6Q0C3IYPYn8BT4D7rMmXc96rblgOX1c7N45d0MZrmYUWCO5LrGyUfn5F12P-1ngjrLnlqL1kbCKteTFw6anUPrxbuSuBpi_DYK70VYzVcTum6uyurL1eo1T1PraPNqM0c57qhctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
توم‌میخوای‌ازمسابقات جام جهانی فوتبال پول دربیاری
؟
🥇
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام‌جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون e23:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/persiana_Soccer/23404" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-IDtR9uvLoeKJmJl8ME1k22-uatKM_kI5aNHCnzR9OexYkDwgUIAbr5eNdhNP84faB2AkSHaitwm46J6IalWN9z8ajaISNYChPqjGdbJenNUY5h7QW5wqlp__VTyuBlUKWVaj6WBT10KDBP4toxLzSNUgw4UD_zj3WL9IYRCTqt0JiLfPVtY24UNv9HW4vGVwiUp8U-ph5NgECicYhTT01RZqWq8TdEUOACXd-LQJvOQ5yxoRzg51fLGfGr60aRSu7cHipkBLqDpBmZNwi6bosZ0qRqBfVH6mwCFS04Bes-6-YcOi4LIIClRXol8KOmjkmkoS8WovfkdGeXjtd9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=W81eI3_ZThzgqDvlQRbfSrmsK1zTtk11weSwIxxQudwn2O0DgZorzn1XcM7tdO7phZJ_Bzfkdhlgaf8tJwdD7ulpqU0A218bK10CkJOD9UwalCiZADEwg8MiRmC6C4MQLZlkU_xhSDlrhB_NJ9EhkQVLQRQU3K3Sro_Sx-F6X5-KctHDeS9cyXLQwxeo44S1UoYyPmf8KbNoV42g4g6pN6Ku32beBPgNAS8hIbFF4Pl0M352c0vPzh_E-uAJtLXSuHxiCwtYYurjb4Fplww1ov3wbKr3YHbUFNUIx9izmb47WiDgFma1bb_BrB2nnnS3r5i5JP7mhN59zcHlGBm4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=W81eI3_ZThzgqDvlQRbfSrmsK1zTtk11weSwIxxQudwn2O0DgZorzn1XcM7tdO7phZJ_Bzfkdhlgaf8tJwdD7ulpqU0A218bK10CkJOD9UwalCiZADEwg8MiRmC6C4MQLZlkU_xhSDlrhB_NJ9EhkQVLQRQU3K3Sro_Sx-F6X5-KctHDeS9cyXLQwxeo44S1UoYyPmf8KbNoV42g4g6pN6Ku32beBPgNAS8hIbFF4Pl0M352c0vPzh_E-uAJtLXSuHxiCwtYYurjb4Fplww1ov3wbKr3YHbUFNUIx9izmb47WiDgFma1bb_BrB2nnnS3r5i5JP7mhN59zcHlGBm4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evfKd2dGfBMrmzK0ZXmLFFF6Wg5dVOvwbo4emuteJjdYb9y5EfBCOpq_9npxHZpPcDmmx17Q7R3Tp_PzDvaQtWnYxBVGEvdGcVcWL6ikqoANCNdS9XY6no7nJYRjR_d6C0Ts6YhWxit9B8GXWttlqtd1biXNmcjKnkgiQiPx3CLxJ8DtAnEGxxQN5pw2SUw4H4GG0c529LK8d4vmc9ZP3spTB9Qvx2rP0ZGKJqnmjcMigkxr0m06AYIDo08PfjnmGC2U49WnKcNNA69SegdVGImODzdR4gmoHD4faCils8xIttkJVW9SSUGtRPWwQMpsjrLDHbaVfb_hmPkq3VwvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=o-aAS8yLefRS0TTuoeqC6H1UCof5wO5Xr4fZMxIlzGzJK9xlIH1JLcjdzQuFs7_6jjnbAB6vHEnDbbHbOKFzKX724jyoZj5QC_Ad-34WmWxYaLAK6C6RP5x4CTf2ZWppcInvpf84wCsPVQutUen21K9knSiYbfTdCVwDllo_ScbS6Ow-oz1S7vUtSf2C9GNVQsrgboEwFSsYHZJnltbahqc0AJEHIZ7kwF1QYJSZz_fSwL7tMKf5UuIYUL7VxCz1VkA5M-bpMRRqUK0PKpqmeVhNkRvN9NBuZptAoPTMZw-JzcPNF-UaneBJxesloPAvl-3Org8FBtR5d6DZXm5u3Ch2r4C0QoSNzFzqGYwHXjcFETzsK_3ZwbGe4fmx8v-_uhmw5wQsvbfuTE5yTn4dxxLN1IG9oG9aS75HD-uh0bTx4dljMM3Il7ovMyzrFy9ow3Iql_9MPADX0p903wGTv7o_3Y5GvttKKJrYue6_rScdYbJoc_JN0FW3Y6_Zr4nPCZqvCLOMar6Vazu90ugD8DsYjOti38qA3EKLjJ-VFAGYmRrYXXtn6Mvz4PGPDNAMIzV1F3q4IavEZPm8BzRRasjnkJEDZSEBCXw783UMc3im1ntl4rAP2lUTFroUgsQ9ZIjioI_BGAfgpxhV9v7yEtGrfSD0AmD2XVBF_D2qNPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=o-aAS8yLefRS0TTuoeqC6H1UCof5wO5Xr4fZMxIlzGzJK9xlIH1JLcjdzQuFs7_6jjnbAB6vHEnDbbHbOKFzKX724jyoZj5QC_Ad-34WmWxYaLAK6C6RP5x4CTf2ZWppcInvpf84wCsPVQutUen21K9knSiYbfTdCVwDllo_ScbS6Ow-oz1S7vUtSf2C9GNVQsrgboEwFSsYHZJnltbahqc0AJEHIZ7kwF1QYJSZz_fSwL7tMKf5UuIYUL7VxCz1VkA5M-bpMRRqUK0PKpqmeVhNkRvN9NBuZptAoPTMZw-JzcPNF-UaneBJxesloPAvl-3Org8FBtR5d6DZXm5u3Ch2r4C0QoSNzFzqGYwHXjcFETzsK_3ZwbGe4fmx8v-_uhmw5wQsvbfuTE5yTn4dxxLN1IG9oG9aS75HD-uh0bTx4dljMM3Il7ovMyzrFy9ow3Iql_9MPADX0p903wGTv7o_3Y5GvttKKJrYue6_rScdYbJoc_JN0FW3Y6_Zr4nPCZqvCLOMar6Vazu90ugD8DsYjOti38qA3EKLjJ-VFAGYmRrYXXtn6Mvz4PGPDNAMIzV1F3q4IavEZPm8BzRRasjnkJEDZSEBCXw783UMc3im1ntl4rAP2lUTFroUgsQ9ZIjioI_BGAfgpxhV9v7yEtGrfSD0AmD2XVBF_D2qNPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tikkuf5VS0yMkKhlFI2fcRQldXIERGJxf529k0mv00Eui4YVLRpkfEQCrvRWmsgDzdvLXv1iLzYdRi1IrL2SauXqh9FE6dNV1_MM4sYDaEUPuMtzCu0oPY_1i9N9QyMN63Vdmmwf9ymPpBevAp5jNNvv3Ew2vQpUgTLNE4kST3vqoDugSW1rHoRIcKXMHZZtLhgGK-yTNujwRDaofw-Wt5q7sOgT1QCOKkOX9nskdGkBG3iU9hEVSZIizyXEBoQZPKt6hFGDV4eAxRL6T9O3m2K-nt8HjDwnaz3fGb0xLNdxB9KDg5Nd1iC274InTIrE8-zNt6jD7SQYudXi3MMxVbMCUQOg2x0ICZK_8ug55Z71V3w9dVMAgjRy-s3loEBy0QW3R-GuJi4APPuR6-2Ar543Vq5tAytWSF1b8gV-IFo1LQxkYSfAxGk5qsf4ZLNruXv2_fvz0HTy5LsMDaqt8IKvGHAG6j70-dQ746bQeIb9x8cFVUhVxhHeqwAoAZ6FOdzNlx20N34gWfj4HFCsbik5hKGlL0RBiNBAWrCk2iI8Wo_6AtjZT8HsLGt5nQHruaXLVROYI1xsGIdRVOQd0p-9_0lrBsus93FuKiiiJQCUJffl28c0L24nhStb-Mz3WXJolXoM9m1KSO4dqSBpyXcTcAdOYPRjzDOI2Cf_Aao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tikkuf5VS0yMkKhlFI2fcRQldXIERGJxf529k0mv00Eui4YVLRpkfEQCrvRWmsgDzdvLXv1iLzYdRi1IrL2SauXqh9FE6dNV1_MM4sYDaEUPuMtzCu0oPY_1i9N9QyMN63Vdmmwf9ymPpBevAp5jNNvv3Ew2vQpUgTLNE4kST3vqoDugSW1rHoRIcKXMHZZtLhgGK-yTNujwRDaofw-Wt5q7sOgT1QCOKkOX9nskdGkBG3iU9hEVSZIizyXEBoQZPKt6hFGDV4eAxRL6T9O3m2K-nt8HjDwnaz3fGb0xLNdxB9KDg5Nd1iC274InTIrE8-zNt6jD7SQYudXi3MMxVbMCUQOg2x0ICZK_8ug55Z71V3w9dVMAgjRy-s3loEBy0QW3R-GuJi4APPuR6-2Ar543Vq5tAytWSF1b8gV-IFo1LQxkYSfAxGk5qsf4ZLNruXv2_fvz0HTy5LsMDaqt8IKvGHAG6j70-dQ746bQeIb9x8cFVUhVxhHeqwAoAZ6FOdzNlx20N34gWfj4HFCsbik5hKGlL0RBiNBAWrCk2iI8Wo_6AtjZT8HsLGt5nQHruaXLVROYI1xsGIdRVOQd0p-9_0lrBsus93FuKiiiJQCUJffl28c0L24nhStb-Mz3WXJolXoM9m1KSO4dqSBpyXcTcAdOYPRjzDOI2Cf_Aao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF1x7gzpO4kemMvKDlpxpcNmP35E1UKJBoJmZCNM0oLSk6woB1URRW4l-p4UQ7GxaRQHvx_UrQu5Xh_1c-bMfTU3rzB2gCm37nWDCHTFhijM5HlBowPmVTey4SL12etWopVPkuSDuki3Nc2xY_bI1q6fUxulgt_Vrc34IWIXs65J-8G8EAw1mL_LgFU7vvJC5og2lmOd5tc93xhjg3kV2mOYS4SazHRKNndXw0fPg6IRoc2KN-mTK8EfO6yRANsTB5T1jSHDDCys2osPnPSd6jU1Bmls0-T9bH-qWC0wOGqtwJTUrdgiEb3fzWKORNCNEut8uuG8A1gmCsJhqoqWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpPzHsXvglIOsLO2a9WdVX-_MeRRr-i5ZaAZn-dU-jHKQP1T15mgbCSyPjP6SZy56KT4PrSMcxnp7OtBp-E_79KWci3ThM5Dy8NZZeaHmN0_hsXAU9I_0AeGQSE-dQK4JEmR-QgPcgl1rEbYP6XFLMpXgH3Qyy5FWh315GPqTVeKtuZ1_cbJo5d4p9vol2_AgIy4DW6SRsgSkKo4wDsQzZd-ug6p--GBlNWS7E6XnUX6oYlRbR6ewd6VKPO3ALl7puOi5nz4y0P8y0LYG90jW8LnzC09wGOhvNrShLf65QlxzNNzMuLlUIcRsqtqUdF9KfV6l1SgmOHNujmNJZiTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHq40FHuC-KuWeCKlO9t_oZ6bLoEpJVmNCM74Z5nAxToLh776RVQEmpiFupUcrugO2ppL7TQ9RCcQL3L1dIzaE7O2AMa3-NnC31vAlHI7pDxJNmKKZF8m3w755B4obyp3eAGWShIlSeRD4cqZadzVgobBj0V6ammy2Qs5LAxYgOwQ0hdEjAlV_lMkPizyiypz1F_HKOSN0iNjOCjLYE1UmTC_RWLdZv5_7xf9EbegvA4lrpvd6x5OSlF_KACWIEUUNVaHXiWQdUQe4wjRSMKn-eO9D8QhUiioqIG1CdfUg93mVp3caYI1RsUFuQn3y7yKEM1vRIGY5s5h_Ist6l8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CznaUJcx_ezXDLf_PhgDBJCZkyP_MmvYtFwR2HQDHBRX3zZ2n7lIlyvdEkqYYGncLCTwXn21bamEsn3-GaHtvkTun6Dl0L15QLjgkoCzgV8zGmIIFK2AgtKGi6ML9_4Kxsc-n9oCftE83UWldG60UL2jnxcFOsHechL-9QbU08cbfwalFM2AYzX-rHRToytw4hziAXVe38CvkE7Agek2Cb0C1bhFZZB2gwNDEM8Ia_S-RgeCGQSoJlqzTBB-o-jUqjWc5hP3Dt2DJOKU-LHDsm-V-yd1GWx7H9BA6TOLCFQyELMc7bHsWA1GDchYoXizrQYJlmhq0AQKMkKqqzwUtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=YHE-4ra-deD6mSHEJxqv5K6nvBfShQGgSSOdlkDg9gyoXSePTMZDQDnTzGPw77SPhvFcTMon8EnkNwdXsTLAe7tuyMFqKw7HD0cUp0J7u5wBIFrFi5OjnLg0NCyvciCcsnLSC4v-yr_Lk4BZD__HddTGkvdyCI7aFCvvCW2mO38TSqu2rG227CaYp4wVk0u8wwPit5nYtnrQHYYJFtdT14X7ymMqQaVsmHENdacmSUQ6o5mvQfJlGXOrj9Fir4EZVKRnMiicx6bxi7L4pj3aPf9UDf9iNuz2gYUeqVO7geZM7zL24R-hderOwzmiX5lJ0YvRxKhFUD_srKEIanGZ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=YHE-4ra-deD6mSHEJxqv5K6nvBfShQGgSSOdlkDg9gyoXSePTMZDQDnTzGPw77SPhvFcTMon8EnkNwdXsTLAe7tuyMFqKw7HD0cUp0J7u5wBIFrFi5OjnLg0NCyvciCcsnLSC4v-yr_Lk4BZD__HddTGkvdyCI7aFCvvCW2mO38TSqu2rG227CaYp4wVk0u8wwPit5nYtnrQHYYJFtdT14X7ymMqQaVsmHENdacmSUQ6o5mvQfJlGXOrj9Fir4EZVKRnMiicx6bxi7L4pj3aPf9UDf9iNuz2gYUeqVO7geZM7zL24R-hderOwzmiX5lJ0YvRxKhFUD_srKEIanGZ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roTi8GiT3mIWhCH2chGWiH9T8AHioj8nWKbYmy1TPybaxW-CdySNcDjw0gZa5-3JhEI7AdRgN6FuKnK2Ugjev3d4felVTrpATIH3XWrB2B6f6begyl7-6LN4ijxa9N2zETG8MxWliUerVgrzvixOFHMtMs5v7yjXirVo7Y0e3CtKVWS_ksZQfDCoF_HHHPWUwtbT8n_KrT9FWDUNzTLvm9HaJ39QwGjqA7CnzYiX23L3r48GmwgsZTRwc-c-3780XeKQdOUfpjPtJWewlgrtBp-mOFgEN87td-IRR4VogvWA3lwewQPjDt1pFJvY-IyOpO26ph4nuwguoRoOiQyraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAq3bdhOu_B4_gAzUeYqZdMUpH3zlZMNNCVocODozLxSf0OR7ruGRS4GDq9Bi9YW5BpMiXT9QF9UWIcSl_9-3ma8LDPHqJnQsNpirr4lXgutkOHrbnmc6MDWrT6Xqh4fKQukc0G24imh2OVsBeErxRIwvAnDhtyb1Gg7_YzFA3PEYk9zmsd6l07j-opTdFeiAgT05SESVZoQYmaIbFRWI9u8JGprwYdGxLdn86XVoFc0AnlC9H52oFqeekFd0PekWum_6gnkxH8yesBK-cQU2lDnA2YVZ7B3fZGw9y0RZG2-VUwlE00lcHykRid_nTpZY5IzzZ-DjPf8zVbCDRApdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIv_81HjvkvbA3otrm04MZ7C6DcgVqGeyHtw2UuLWvuH_Ra3N9erpOCq49cmrNla3m0Pj-yeC73RdpttK8QKoPIzwlrBpbzn8O01VLRTsFyI4y-tzxc5F-aM3eK9qqbQb3gLSTDq_tNlZuSuKYnf0BDKB2ehGBbW1rtOaRvQ8uPvyVHi9sGnl_StseyFgvNwd-Vo6i46VkANCvyzr2FO-JLxIQEOTPqJrxgVmThaRq_b_mDJ-WiiNbY5FprJKw-HhnK6XTmUc7wOKEcrXfvsqgXDoSAwPbku8AP2VaTk-0s5aPiJl2UKns-jFkSZhpGMKbf5i1diT3lKU96Gx7E-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=qk9i7kP49dnXsYqcfwY3xTcXpFiHfXCUUyK65B7TA2FWc68KihL_J_Fzvv5Q9olZjHWX7PqWbA21z9ZLsQc9ykKd7GUcvk14JOC2S7WI1TqvIxxZ3pDVZXI0cnk4N5qzYQDdG08dmY9nMlB3GJVkiV1RX_-Qvn7YuLQ7UV-MGhURS1H30QcdJaEUtyjFUXOB0vJIeF-k98CWoqZnMHtCV4zsTXEzOobtIeOKX_4kWUnju07VdETDtPywDQTen5iPT9LuCtrpOspEN8a7vjd-gkLjSUy3JKpEHhsv1VSZs8IdQODPjrhVA1N_umlkzLZrYkAL2sJWXq16zkeGXBtnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=qk9i7kP49dnXsYqcfwY3xTcXpFiHfXCUUyK65B7TA2FWc68KihL_J_Fzvv5Q9olZjHWX7PqWbA21z9ZLsQc9ykKd7GUcvk14JOC2S7WI1TqvIxxZ3pDVZXI0cnk4N5qzYQDdG08dmY9nMlB3GJVkiV1RX_-Qvn7YuLQ7UV-MGhURS1H30QcdJaEUtyjFUXOB0vJIeF-k98CWoqZnMHtCV4zsTXEzOobtIeOKX_4kWUnju07VdETDtPywDQTen5iPT9LuCtrpOspEN8a7vjd-gkLjSUy3JKpEHhsv1VSZs8IdQODPjrhVA1N_umlkzLZrYkAL2sJWXq16zkeGXBtnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3cqZLqwoD5rZjS3PVu1UF5h36KP1NK4szkIcNBhUJAX6W6Ld8p7tEGWjv9lQ-K5Id42T4ZIsuUnsLGPUPuAPS9BruYLis27yRZPNkjb6hN76XjwOqa6SJc6fbmZs--vx_j1zTetzGICXZuQYtQNMIsx6SrtDClMLe74c8bBTrClUpX99rR9Z02cZjXRwaLANHRuo2-AS-TSBbnPzZkkNSIXzBbnRn2EO0c1FlJG60ninj82JY9O0thlZheqxgk1D6aFOHKgWNpX8TuWfJxPUcaoV4UCHO5E3Vd34-ZAByK2_6wQkGssF2OkVMuLvjgjZazq2BiIfjW57jCbSivLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kdfDD41hKy93_I7Bz80I6zG8F3UohJVP2VwTrEbiCzfx8bL0J_YO07r31h0lhF8TqraCF3To8G5BIfCY9u7sG6owOg4x93DXmd8dxVeXPVXaDQnffyCR4HpQbG3PwnN6rhc4hRNafgLrC5wxlSkOQG3G_HnN92CVO6UAZqjf_Z7GXLbELZo8kJ_dPaukNFbpZGtM3ziIbKHZW4vpJpTN7bYe0YPr86xDeB2FwCe_cE-u5kT-Y4qaib4raF-jBWykvDgPiapBAw9cES9in0ahkjT0rk5IllxSaCb0WuBE3E-BHvsqzIBx6WZXXhS0p6lT25Aq3ddz-dC-zabByfKlvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kdfDD41hKy93_I7Bz80I6zG8F3UohJVP2VwTrEbiCzfx8bL0J_YO07r31h0lhF8TqraCF3To8G5BIfCY9u7sG6owOg4x93DXmd8dxVeXPVXaDQnffyCR4HpQbG3PwnN6rhc4hRNafgLrC5wxlSkOQG3G_HnN92CVO6UAZqjf_Z7GXLbELZo8kJ_dPaukNFbpZGtM3ziIbKHZW4vpJpTN7bYe0YPr86xDeB2FwCe_cE-u5kT-Y4qaib4raF-jBWykvDgPiapBAw9cES9in0ahkjT0rk5IllxSaCb0WuBE3E-BHvsqzIBx6WZXXhS0p6lT25Aq3ddz-dC-zabByfKlvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQXHo0Pe3EhCWzrVsJHe4tYdFLB4UYciiO4hvLctPfBejaIOzqI5Hsmq4wCxAE77mkeA7pIFztQzNCcKXbXVu87mGeIR1Myt9eSZC_Ew806WO3SXsLAWfAZyN4gnDaCr1YC383hvSamc28_QvHY5nGU3plJl0wP-kzWjWsvC444pg6G2zPbyGNrQNN-08MkXvJdyvwMFvySbAYCgmaaCxf3k2Sx80tSJyQtFoS_zFQfEWpWyyBnlj-e0HTW2oHZU5-BUITjX0-RQ6erZIBD8hFWHW1G-HAhae4apweaMU0vWVNu7sVI1zWb03n0wkwvaskV3jOQvCEwDDs6l5uYbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX97SgTpD34vqIb5nCn5w-QP5OQ4QwLet71K2PhzbldMkFICS_q8owtivc7CIFrADXZfXh0fWrFoi1DjprCsVHebKjLFPG9WVukwDJGaPekPE7YdQaQ9CefIw5spjK7yFdl1-JhLKLdB2EQ6WE0LbqKdTYLpktaCLNP3TPZjy04I-nLuTp6Tz4bRoJbyImQ9ZDDPDEHQkCQyc2wKNruRO07vjYD38Dx_sBKyYatjs9BXa0E1xFkJ2E809ltKlaLl6-Y-NDGlG9u58HaaULkJTqAMXCb06FFTCKz_5hi4g2HS9HxMRq7N61t9SEGW54wMfzx7pXvLOXjS6m42pIgJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=VlU0FkusqrCs7NB65lqNyxlNIJ3Nv00h0FZFYpzNZ_XE2DW2ArYjRbqpsFM0Gt9nwApae8fP1PYc7wm205cmAfZdHmxyaodAaaSHOfuZ0kIkp_XXf7gT2U7bbHdP8Mn6DiPjMo2wI-e0BNyt2uOhDivr-t9L2eOpkh7swydLYh_qMqCUSJGld0tObjv3GthnwyaMlCt6-CyVD5K6JtYo_T9s_OquX0kASfojC-4aIEjCI3ImI-HXNDGaaNurIzojuTbWkUdwnMhCwkNQ3dq0dXSFS2NGq_y2kF21VAvsXOvfk-pwEXWxZUPyGMKMvP-HeINmcOWM82vmf-h5m9ifRIohNVVAyGK_Zt8CK3oIzULfxNI7VVWVyNpmkBFVV1xRaYM17JSe7ODOxzmqIabVwoKk869Ng9sjEP1KOM8029DmBtyL0fqZZsc5-528fJS1wpp3krYSnMrK30Ypdn-hNP_GthwL1JYVmZAqpWoQZiSvz6E7wbzOGRYG4NxztZQ-u6e3UY6cV1BwtRF5ZSBJhQFw03wnP-dKiycHxse9m3TwQiEOzq6bqQLrBJFJYTM-EnVW2_P2UADDcS40KamC06D-YdxdtlZ2gsoCtyotjs09VmQTzNsucvAjWuUGBlCblS1cu5pmsU0MBCbXBTUxFZDPF9RNABsIjZI4lOOzAk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=VlU0FkusqrCs7NB65lqNyxlNIJ3Nv00h0FZFYpzNZ_XE2DW2ArYjRbqpsFM0Gt9nwApae8fP1PYc7wm205cmAfZdHmxyaodAaaSHOfuZ0kIkp_XXf7gT2U7bbHdP8Mn6DiPjMo2wI-e0BNyt2uOhDivr-t9L2eOpkh7swydLYh_qMqCUSJGld0tObjv3GthnwyaMlCt6-CyVD5K6JtYo_T9s_OquX0kASfojC-4aIEjCI3ImI-HXNDGaaNurIzojuTbWkUdwnMhCwkNQ3dq0dXSFS2NGq_y2kF21VAvsXOvfk-pwEXWxZUPyGMKMvP-HeINmcOWM82vmf-h5m9ifRIohNVVAyGK_Zt8CK3oIzULfxNI7VVWVyNpmkBFVV1xRaYM17JSe7ODOxzmqIabVwoKk869Ng9sjEP1KOM8029DmBtyL0fqZZsc5-528fJS1wpp3krYSnMrK30Ypdn-hNP_GthwL1JYVmZAqpWoQZiSvz6E7wbzOGRYG4NxztZQ-u6e3UY6cV1BwtRF5ZSBJhQFw03wnP-dKiycHxse9m3TwQiEOzq6bqQLrBJFJYTM-EnVW2_P2UADDcS40KamC06D-YdxdtlZ2gsoCtyotjs09VmQTzNsucvAjWuUGBlCblS1cu5pmsU0MBCbXBTUxFZDPF9RNABsIjZI4lOOzAk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23380">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiKgf0nbQpPIzz7m7TnO_zfhYiMCEmtNco9LWV10EK5bA99xmpC5rkTIib_pevGbhPPaFCZ0Y65taVSI0HUD23h_ophaZpj2qJ9_F1-hHSn5ATpJhCbIWXp5HqBtyJJyrf8xwl9FuKxjbDyeIkDDFe3dVfPQlKsgOlmAHaPwqT4sRWNwLr39Bi-DnDuAOoRWg0lUdvy8NvCvekaisS1EoUe4F1VHpl4zXe8qBTbknPmQfjyZWp2RDUBXABS7UFLoEuqpcGmDqhZXGmmS_n1_OXH-WUMnzsrzXfPU-LT-mVKULfl7jHXKt_c-lPkLt2dRLqNaiQcJNa0jEUcVMQnpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای سهمی از جایزه بزرگ ۲.۵ میلیارد تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود :
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23380" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9Ch3YjKdLM382XOzgWN5341kypVoBIGwrzHT0MOOu0DRPjdXxWd9LeQ1a5xQPBP7zEkYOp-tTIQnIBWTgR7O9T1ExMuq6NATRclgw44L3mP8szNzEAaZP5cLaz8WFO5c5mFx4fSwCswX5-VckYQXeBVickHir2WqQ8TKC9qhDtbpDF-hJjQ2Tf9AiU098JHj5A0jgQLqKSzm7AjUWaa6MXmxejJGHl1s6K23oCQ6_4bzrQWGRXzbx_3GgPV9992FT91rkBoaeXBtV3TnO5RqAv93fDFbM6eIl61AuPGOGKTke-ETyIONALS7tVQKFVouFHm2LUdSRViEhbRWvwoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUtfMzQN8hzCDafmceMnFYiOuOomtSBIBGh5865G8AL4dfI0r1LpA7xTjbEB1XuhQ5DwG-L0mVsDv-swRDM2KsanJmNzy-u8aHO_u3DjUt712u116ovuoOYCkEY7L7MRzXKP2pD9iODN3SDt7Y82dgQQB3TzqEtUXGPiMPbnRRuU7G80CnrUjMMIrUTuAjdjyL7gMMjJPP13lTvoWL2YCwcGVEjCJ_ea2srA4fBkdThfPF4ZErYW6NvXG8RF9NdkliB7Y2flaW-RIZEdr6GtudXxhSnubjfMBqCamek5vHuH65DfIMuVbzPFXWS-qAHIxn3Gs4szoPl9FlTX7-hPdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=mrnYkWm2fZFDqF2MbvKTcFsg6qJX3Akvxw5znWNvI9eZhHMU2WU9eYp0OnlC6t48oJZoPs_bl9aAMDfpwGQWWTKkAq06svR1c6VqFFy66Vp7vXJLV8SMa8oQsEpZOjVQYzgdGKcZThswjBILZdDfPcgr-x1avUTpJ-6dFI-P4XJ6zZa-8fVeIV4xE20noiEoayL-FEsUZSTrbjMPbnRbbcOkZwdelXliIKpmxwFFCbJJX0IngarfYf-3JTAYcBbvubH0cNIcX0daNusqYQ3ld1M7D0Th2srAK9U1vmV6nuZM2Hl1AK0KHeGl76wIU-WAp0xmbFIEzv5pT7TNrW4_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=mrnYkWm2fZFDqF2MbvKTcFsg6qJX3Akvxw5znWNvI9eZhHMU2WU9eYp0OnlC6t48oJZoPs_bl9aAMDfpwGQWWTKkAq06svR1c6VqFFy66Vp7vXJLV8SMa8oQsEpZOjVQYzgdGKcZThswjBILZdDfPcgr-x1avUTpJ-6dFI-P4XJ6zZa-8fVeIV4xE20noiEoayL-FEsUZSTrbjMPbnRbbcOkZwdelXliIKpmxwFFCbJJX0IngarfYf-3JTAYcBbvubH0cNIcX0daNusqYQ3ld1M7D0Th2srAK9U1vmV6nuZM2Hl1AK0KHeGl76wIU-WAp0xmbFIEzv5pT7TNrW4_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=Hvv52A-jjEw3BTKG-gKinmS39DVyqiGINDqm8_c0mX-zK_n5sFJ68Ogs6gkbGGjJnR5MMeO9SFs9ndLB8N38aNoNQLeLcwHaXbV_tVIdkhFIPTELuMW2AsKH8L-4emxUrUC2XYMrZu-xN5udiHm-FD-M4HtZgyjkxO35oMZUtUtqdaUI9I_IBCvg8CI4UJIGi6oyCwVAj86jHyEDB-BB6hJvgEWougrtVfb5Z83VIRRJsHJmOTOYAq3-ZaIVgywYoKeV1pURW23hPzZWGL4pjiG_Tt4MjEFV8ExkUP7_pKELR7t_2P5VyeRrUDI1LDhdeG0NUF53kNiqU8u68ihhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=Hvv52A-jjEw3BTKG-gKinmS39DVyqiGINDqm8_c0mX-zK_n5sFJ68Ogs6gkbGGjJnR5MMeO9SFs9ndLB8N38aNoNQLeLcwHaXbV_tVIdkhFIPTELuMW2AsKH8L-4emxUrUC2XYMrZu-xN5udiHm-FD-M4HtZgyjkxO35oMZUtUtqdaUI9I_IBCvg8CI4UJIGi6oyCwVAj86jHyEDB-BB6hJvgEWougrtVfb5Z83VIRRJsHJmOTOYAq3-ZaIVgywYoKeV1pURW23hPzZWGL4pjiG_Tt4MjEFV8ExkUP7_pKELR7t_2P5VyeRrUDI1LDhdeG0NUF53kNiqU8u68ihhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=jdYGr4xU_2oBYc0m2QI6fOdTOg7-5F8UrvAmsrFsd_uUzrXcm30h4ENX1cr7BZ9n1z9-X2aaHfN1ELAOglNj_x6sRub7AMd1UB6BHlWAQ8-3rn3MgcP7NJZfi8N5YmlIPge0RZKhglh9hwFezhJfC_pRY7Uu9RQoM9vQYMFGJ0pGng4VUXj5d6MgeRvlJlZDoc4Umlz3aIRpufb3rrQcd6wMa6XBve0Vd7YiPDvzcyelqVs0jyCGdPCwk0dH-mp8Jsf8qGArTgCGHqWLZ_k7imkv8dOrwnrIyj5kU8bBCRw9SlnPOiyiPeJn2mFw9NdDnxor51lPK4A5NLNw1rPj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=jdYGr4xU_2oBYc0m2QI6fOdTOg7-5F8UrvAmsrFsd_uUzrXcm30h4ENX1cr7BZ9n1z9-X2aaHfN1ELAOglNj_x6sRub7AMd1UB6BHlWAQ8-3rn3MgcP7NJZfi8N5YmlIPge0RZKhglh9hwFezhJfC_pRY7Uu9RQoM9vQYMFGJ0pGng4VUXj5d6MgeRvlJlZDoc4Umlz3aIRpufb3rrQcd6wMa6XBve0Vd7YiPDvzcyelqVs0jyCGdPCwk0dH-mp8Jsf8qGArTgCGHqWLZ_k7imkv8dOrwnrIyj5kU8bBCRw9SlnPOiyiPeJn2mFw9NdDnxor51lPK4A5NLNw1rPj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=oH04QkpUIccJn9f2Y3TitqTj-apYVz7TavjZIMWF4RbFXfRM-tyqRoC2bakj874t8FJEiLTsbTgBgpIRPI1X21yBFf8JUkV3sDEqgJ7Y6Ls4d_J9M8SYr5wTsb55Q5BkpDBlCWho-E_K3dBHcdFfeje-_WyjJfT3EA03G9ciJQLTFpv04w8tJ9pSTtFXz7fWXjoOg2lauHl5LK1NNZKkdSulTjrhlnT6tict9w5Hrk8XvpWLvKYleMK_C5GTiSNPbyAUMTrgmPwNzC2A611k7yykUlSzh31Vdla_H_0eFNjXq7tcPvfaX4npBFsg1iYS3WnQhg6TiFnYqygtw0aAfQNFMcPoqihMkoEZWlNxd4IuQa_UgRAGVwquSAVZo2TtrvO1Kr-3HIDMxr2ZR9CXVvwSFsJGwqMgURy_-lSUiJJfskZ4f13lm1sKSVy9AKqKqCotAkGP7Gs5kmG9moC_Bu_uFFaxlxfTQxxgaJbRnROoHRKgeT17q-OfDcP_KG0R5VPgtYoIlsI8E3hwf2RrAmuJUjfC12yzy7tnRyq8Unajl8nI3YiZ_Txzk3lZDMxogKID7fwNHfMsP6IsR-mzo7yQXo28xAtsbCDcfirnsioZYqRQpqMfndGpIWp0VlAEkg_0aWxsG1aH58bZD7OMX9qeXF3WHfyh06rf-H_Iz6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=oH04QkpUIccJn9f2Y3TitqTj-apYVz7TavjZIMWF4RbFXfRM-tyqRoC2bakj874t8FJEiLTsbTgBgpIRPI1X21yBFf8JUkV3sDEqgJ7Y6Ls4d_J9M8SYr5wTsb55Q5BkpDBlCWho-E_K3dBHcdFfeje-_WyjJfT3EA03G9ciJQLTFpv04w8tJ9pSTtFXz7fWXjoOg2lauHl5LK1NNZKkdSulTjrhlnT6tict9w5Hrk8XvpWLvKYleMK_C5GTiSNPbyAUMTrgmPwNzC2A611k7yykUlSzh31Vdla_H_0eFNjXq7tcPvfaX4npBFsg1iYS3WnQhg6TiFnYqygtw0aAfQNFMcPoqihMkoEZWlNxd4IuQa_UgRAGVwquSAVZo2TtrvO1Kr-3HIDMxr2ZR9CXVvwSFsJGwqMgURy_-lSUiJJfskZ4f13lm1sKSVy9AKqKqCotAkGP7Gs5kmG9moC_Bu_uFFaxlxfTQxxgaJbRnROoHRKgeT17q-OfDcP_KG0R5VPgtYoIlsI8E3hwf2RrAmuJUjfC12yzy7tnRyq8Unajl8nI3YiZ_Txzk3lZDMxogKID7fwNHfMsP6IsR-mzo7yQXo28xAtsbCDcfirnsioZYqRQpqMfndGpIWp0VlAEkg_0aWxsG1aH58bZD7OMX9qeXF3WHfyh06rf-H_Iz6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5hhD01Pi-gKDQyZ62ixROmhr-BG4zdqcP__phb7GaqutQwTqNLp1dYPVKE2mDcGGVbaNSk-u5moNvAfihUxloxSR-XMzSLxBztwsQLkcxpv0DUnVOyb9aVUkgu-tbVXtgDHTRm9O9c63l9f1IIBS3zpcWm3YiZ0HKgTXCXWzamDewIvSV3WaaSGnqooT5AOeU6v3EVYHgy7Y6JB2jGDcBZ56930WOIu8ISto1uIh5x8_bhpPh4koKUJXSjrpeyoN_C4f5r0OZs1e3TSks-gcOkkBcOQxuJiKhRaT3enF3z-fBzMMszn3oLY_HjAG-yKJPR_zFxfYuCjwqpy9o1ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nc46dKayW0M5hUXUliR3FjMeYHO8FSmANx0mF8u17ekzD82Lslv_ymGn-40kmI0pzQukA2PRUEEvbLIwNYXR15uWl9Ave1N-DLoaq8HNT1W2sslP2S_zLB7GzLje4J4ZFcz_lMwu665aa4VSG1oir0S_YllaxHzoiptKt-0C0qj0F0JSUy5A9P2ec9ys5U1KZ94g6oU6ZEd8l9x7sGUgLytYvAurrAcsMXPVobHTMm8o5oYIekU8ccJnd7UcAFWc2zBqI9a8kPXcclWgTtu6kMKwwwVhvAQvAgeM3ZIRP-pmXtw4kvYb6ReZJ20ptoG_HLQzEIyJVZhABFQE5Uje2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx0PQRikBRZJkBx21kW6fCQDff0s7Vyv_Tf4Umyq6lneVEPZW64cxXZKQPxkYhckisU4JBX3t9pV1Eslm9wogajdV7XaXh72eDBH9JHroXWj4Mj4kCYlFyDozOUOIw2R9KApITFvaNYI1S4ehMNK75V_9erirGcl8Ls4GmxknFiWn0lx-3oxjkRDR5ntRE-iBFUB3am5vWW-38hw0sX4OOmY5W11993OdJd2xL4gUs5J8Q4GZPEhaMF-gluQcqxpW_NHr5x1MyJtT-iy6GfWz1uDw0dRHSDYFAp1jHAwOEqSdIr3A0I3SYktMAbS5C4jdFCL2T7Lbr287GIb1_0fUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOW9tOIu_rBNmzYwKA-D5z92iKeGTbJSSmltlBvQfZEIwG2SZXbo4_qy8usvA7cInQZzJyipq9_w1tJaoXAg3rsa9UsH5VzPa4qowXMgFi7LQRyktQ-lWhIl5NTkPSSVQCTkVC1SMEKe7_u_OiN8OjrRr1siYu2CJSr1kshphikn_hSeeY3bhhl_6ay7Jj2aEl13DRtN3U8BfDB4Ri40SGI0r3K1zdaI4-dlT3fLOFFh5XUiPziSENB9KIVjEcQgxoDP1GkMThZwU6TSTIyHdZWxHHEAKFJAr99SKq8eDYGNd_v0CUR0UVwoYu4IHRt-Wei9YY-Cpgy-K0CoNrHuyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdfIzUD_yhq3ZMGlHzQjlmy7qX84YiwwrLzTm3Mdw2knlPi3U7t1a1s3F6oO5duSkMpg560Ld4oHiz41ucleiTUZAyojfYApprKr5QGAI1l-6AGTe29WVcK_AO0lxl47fppCwqYYa-Ypfxg66MvN-E5-ixcyPp-ayywXEB4dEGfSpdqeqgyyuAN6hGHFko_du8pghpXAVVHC6eh-x4QIMaWD0w7wWi7OP4xzkioEpcp0nM3zCrLeQW2skF0PO8qZcfP1T-jNYsQMvgRXr-lv-K75-MCYJ53q5n8EXPHCQIKBTEnlrc9q9AffNtwCjARq13MkYkgdnIJ_K3Ljp7_CWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTd-Ipbieyrs3Gygr66kDeeV1DwGgQVDPw7Vnj-QtssB9kI_eExyAGLY8fHGGAcH2OfZh8lVFU6WhRHq5JtqLMjhhxHghLa5L5AOewwvuzgmB05iiypp3RfjNjYb64bvUIroAqxlWf8x93FWxJ8sY74MX-_8i3pQC4Ysz70xNiT7p7R3CJ3bejwZVSFWaqdZaZ-V9aRcOrK4TKuZnatLDKh709sQzkqV0wICKkF4ZUEgqpSG5IKVfq6Ctx_N9KMDkdhbNjYujdKmhhj2hyEmjDHcjEvNjULsAioa1T_ViEkfSJFvNjDzywtkJk3yHSMv4SnMSXN6bzA2HYBH4IFJ8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrC_R-Hyq26EnHqyOPXl2dWtQlpNVOuyD--wiLEiTq71teY9CDLKD-QXYbJYOaint235rgPMukZNzcbC94T8Yat6a6yrLKxL9zEeoRN7vvXsyGuQMFD305-QbiBHIpu_bRiJpoAeuCQe3XM2xUlMZJEGPOoR1iFixOxkhFwYwwkXczm8NULBeFoWxtppbikeGx4lWv7huqMP_PMRlMNG9GD0oBwBYTTixo3-5VwMiyChITux5FzGnNosLdOOvJeDpnFmC_tT6jghfQOopgv5JK1BJC4UHITEqS8xurM57g_PYZCrE5O4nmjdF2UsJaMuU_LQNJG97UzadA8N4CYazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=v9t8tKfIbgoHOqLt0hSWWTY2Xd8GKEYalhFxglgljQaP73DXs1z-Ouettaon092vMZ2ufof7mESpS8_R5LbT4AI3gZaaWXxdbTo-tBLbqMsi3tT6DEtjAl8sCt2mSD3iCwMKYxs-K-lnBLPShkBkQeYVDxrMCU6PDnjNXUhyttKQj23UptwcLkYwBnhsl4DSUS_DLP1N32zUVP5N9MLzxnbtNSp1FMbdPWbYo4Fa1NyKFGY50O2MTTZNJT14g04HFYyD7mwB_RE2uMpnrWRNiDb6W1UEx-O9-4ueGNAgl4y178jI957okA-mHmlrahZicXmaPJFnjLFK4Z_5-gzdBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=v9t8tKfIbgoHOqLt0hSWWTY2Xd8GKEYalhFxglgljQaP73DXs1z-Ouettaon092vMZ2ufof7mESpS8_R5LbT4AI3gZaaWXxdbTo-tBLbqMsi3tT6DEtjAl8sCt2mSD3iCwMKYxs-K-lnBLPShkBkQeYVDxrMCU6PDnjNXUhyttKQj23UptwcLkYwBnhsl4DSUS_DLP1N32zUVP5N9MLzxnbtNSp1FMbdPWbYo4Fa1NyKFGY50O2MTTZNJT14g04HFYyD7mwB_RE2uMpnrWRNiDb6W1UEx-O9-4ueGNAgl4y178jI957okA-mHmlrahZicXmaPJFnjLFK4Z_5-gzdBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFM2ezaaEjRl9kR-VnCSMFSkI7u_uxiV6M41aaMoCdaqWU4-jcp8A04RzKDD_dToYv2ZQzp4uTXWtzA6ILaF1BdXgXMFOF8eqD98VSaVL_Bo5gLxZjMOtxNwgDrQFOFKFMZwwj3dymVQED1pid4bqtiwveDLZ5jnpFt7GWJdrlFpeccdBi4Da4fgR1JYjRlMtWC19MGnH2plp5EqKaaCvKVLhlzwtQhY71so_4l1kPp3RrEXwxYnz3_opQmennLXkMs2zDnkO4C9VShfhJgXdt2OC2xYdHUwJi5dgQsvWoG9zToZQUigpMhAfbu5xB01lG9Cx-Fk2uXRQHqHwoBKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8WJGM_qQLG0ZpqGHTOF4DruZtgUT0V2SMYERdulOrEVHcxiZQDrUcYLKHURpPJnB_4WaCu3kDdduFGcvDU56K4N1zWO-54BrBzplmRdnUeAxGVkPgjyEDnjVXARxAt7h7Ci4klwCi1EzKGM7QqIuqyIU40TobvMY4USysgr0CGY5kmX-yWZdAVN_yf3qGtnQ3u5i2N-SW-Bw_JyDfxENXw0ndT4lH5em1Yys--nPUfX2uBb7h9sGx2aJKHRCViZkDg6SLfCtZVTjPb0J-3pBlW32OJzknd3WI8vtbDDhUSCJqNKFa8w6xCB5SG7Ez6f-LcsdGzRPxYloqupAiilAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObcLwAgIxaM_ltiVkRX7bPplsen5rj2W_yrL25pWjp-S14vTaXqVeWq6UGDrOtdlEX-eoeOpcOLmThAisRz7vRtGKNZhvQmdwVZBLocklJPkt7xoYe3FuGgmmdAhij0b7YyjQAX-DmkpxuoGquaMA1OssJ9sNZUnvQ2RdXU94orG1xEJZcgugm969y4bi2Z0u9DyLb-cnTuxXmDkjux5vPUdt8iSOZ9tx6QIq3aU1Ju6acyY7xIbeS9qrq5Vg0JhhOS_DJfPD0DpU6j_3rHwUJ6aaRTe0-JsgrdSMd5b2oD9zjgAdk017en9oHrGnM2ZTezsqKmiiYvYR351_D4PBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO4We_L4ZPYaYcF4-jR-w0QQo9SPfW_FaKUXwdymXFPPfnVuI4nsu8edrM9zsh1EdvqJgJ9mvTYmmVQcRiJSf2M94WbUgiXmYIb1fBRX7Gv7w3wI8fTsvTYfBbawVpJMYFqLfb4KX-jcamULhcCmJO_3YUsLFwW0J18IAcQEvAdYGzQdzqMUWsbVoHQYGsDX71SkZx5koVvMpzvaT-vrcVZ0ilpETTtSnDwmm0ERbD9I6LvbJcVHrSaTlC-8c98MUVfrh7s8xiDCQ20iQ-5Xsx6plX_7Y2YrhCn24Ls9D8TsigrGS706SbFQTAlraVGGrxRTyedFG2aYH5flWUHLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_B1_Qdq-7pcSu43Q9i9mu6X-rRQOx4LkrC8NCxjIDmsyZRUzv-q81B6J-MIrr_CI04TzSi7dvNfqfaN-455iFwGlGHsb701ObyRPI4EOd8B0nL5QYiYxxMW3i3IUXhxMg0cXMTGbjmAH7BaYQQSY6lWJ7CtyO7_tpwiXQC6tx1tEnVgtl1S6u9OSmScaB-JutknkjaXmT74VmKVjTWLhNd7RcSR7YNIGPEaYef_5WJY_9kV1EdfuClTdQzOyDR1YbpFXjSE9ZM1KMki92orNC9oVIE21DHQN3oQOF3ombZE5kHlddchjuyhvjnhoxYEY6bkQKO3kklDsBWWRmUYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WobKySs5564p0N6vwzBOT-dC4tSlzI9DQkgn_sbAyw_1GIyaYw6ulhBXDQoCZzOlAfZ5xq1kJdHPP3PnE3dDwTTxejtZTgIgw-lM4V7vvHjKi17LsXXBjkDe4d9BYLhwS7V3DnUCwzw1_qMZzfLxQTav5-UU_k99iUh3Mewvae3F4N9ICKg9SoZTOCLYezKK5uLTwyv-lgyfJv4QpJX9T05nGg4X5gcZpaQW-WAv6UdaxF4YyI6pCQBABVl-jEetZg1jkkeWIVw7k3vwjKshtLzubyxm13xfgBgWiDKObbQxH9BYO_waF6oLMEfioMmrewHzUl-Y_riyDQOn9xHW5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRfDWALqvLCmuVK7hlVJRHTVZ9MKXnpepi0xrIRKl044iB2rUuyjAsRa9woPrYAfTmTSHSm9LgJ3y3L3ynlerFkADveff2LNSJh9k9mVxzCeeFrhbr9VZ7wK8qzI7Sy9pQk9KT3K-9kMh0cnBFP2ryZdEO4BK1KQ3-9U7RhLujItvTOQdfOPOhbyCZomrldDPNV_fe3S-LsTtxU9-FfU4fKdGkHxXZFe0asdNhXB3jZ8LN0ZpphCqOVheDxW8aAgGZErp1atJpqPrqBioujsEwRk4uNPcD5drSoJqC03vIJ90UrUKB8RAZhBNQr5wg8VAw29uRmUkiP6R4uvQ10BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYmHz8GNsxu5g0oQP7H0kChd5NYxMcoWv0OzbZIH-UKVP4MP1UXvXuMdDRJN7ZeCZn3f0LwLOF-3Vq1bphRGSOdUqR_QWgKRvR7_U3p48eAT5sC1Nvb_xThvJffa-frhPGbkq0V6ePT6xC7C76vFzLisd5w2qSAmorcV9dIpgmTuTBoBRjvWTKmNYDRY1F3QtTAvxBYbX35Awz6rQb0oFggJtKiJ5QBsLE2Pm_nsLIF7Ad2FIl_vAHL90ZoVTwHni8b2Mr5Y0CLS3DWAWgvlBeerf__GN6mW1aCOqWZCf1rubLSQSXnSCWdfqFGr7ZGvCh1g_kOZfMWZcyaVUBz4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPEDNilOrkz94qmYdYPqJWj3FqG5YAhGP2sIweB3OJrtcwiYvbY6dom5xRZ5enmJqV2DAdxAR02Sqdt2q20QKE5DWvdldWE31FZXTR3gjvrPIeUg_D1zfF0PjSuG6wFVLQ1Wus8rfdXFWG7AV4atziWnLcZLgnJvn45BsmLH3-_Vzsf8li_SK2-mSD8aqQnMhnIouYa17YU19ozI_yBKF38CS303T2KTmTJsSZJRJHXvJAT5UY5HTxujg1NXQrZVYzY8ORaE4B79znZOsmh00C536N9HhkVB1V0liFCer4uwPYHxhtTkTk_3A0zYK2VBoS6N1VgTcDQWJjLYaxt6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWkPvNqSPd9MVgh1WjySjMFyaxLGqbO2iZARcw5yJN-arLK3Rm9kwCzLNCUCjU_B0lXySI4l4jEZAQnJHmsq4sjXIzYiGPjw1TC-z6EhvGYo_ll85cgeaZRhfANz6rLeCvt5xoOBZJ3eKWWd_mDjXe_5lwVVZBNjBDSp10tMe4mkbjFpexAE7PC3pcAHz7yMokanFMQ78d946XeFJzfaXPqRIt_ZKvggZewL09u2-dNdvWGqwmPa2WIyToTr4cGdevNcxj0Q9N63kBAjjusnZcz7cNuQqXr9wWw1FORytORlbOTMbhuzxO5rSUCeJo1_zmJCtaduisKuzZa7REatng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4QHSXx-F6iRPdGIwbbmBaN0tulbKg6MumNAZWGosbxNfWUJp3lDnCgqnK64XkM1VIUkZ3yd2wLHPnzslcnHHGP2NDZ_Z5lNQme2ilDekR25T4gHuVzA0N7WzSno5OZsapCtPOeJqUF_s65RcbtLBlYsCx0AyECAYJR6X8CCDBuMi8yrxYW3pmAL9kjkp1S1zO_s_kOk7zWS9sGGUFCoJ_s9NANDB2sJKLldkrqCcB0FhTkMwxcnDtJAJ-9qD3plNJa51OhBKweaCLUiJ3yW5Asq1vIFjNjv7Q68NBj7M3mksmblXg1W7ec-xukHWr5SL6XxfzRsAkmpGRB8XnFFlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvFH58eIvFKZ0k4t0VPV4hSzIdfqCFYf49BpXCmKeNNQD-zOxgwfzN9NMNfcd_TQlskRmveUKeSbICFzdBg0M_OmOdqlgjoZb6H9yv9kyO6NDFgK5Db_20cNQRAL-Va89SRYpvboOu4SZ1cQRgWalomiD0Xzpri8xkfEZsr5v49awD76GuAHirWCHrT8A52L1wNSJG_H1g5pdagco37Tm3o6pO2tEdKYTtorgK_veYYjmxQ_ENn9t-VMlC8C-38ScoAhbLwj_cS5j0OBqPy1vDwqUD-UUnzZoQxjViJJTaBp2oUinarl7dSHowxkZp2RtF1MOmmRl7DJI4rpighyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckj9O21sm_9zZDjy197QW-mUXxV1BVWnoPTmAmL34Id0F0T4aIqxF4Uhqw_iFTkjP9zGyLYkQT-H4g5zfR6eHXG4Xt3jt4G-xZ4C82Vawt7ia0pRfDLzQ2_WRoAWm8HE9pzdWeiN2UKEnq-nDjB9cYQsatmRqe4upjEzqGBba9dDM1bTE5TWoIjv3Jdw15YzctXT72REVHATEkCWHOn_ctF5ajCTJImeo3e_QgRGjRILzViEAbW-dZG1LmgdtzYddeZIbACigcBAwtkq1LjhD82PWYkh20lurtSvr7EZWhKuf39MozHIkjyWZm3QGGv25052nssmV0cxQ1Z2NuNu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgW51EPgjTAAiQ-epn4A7A79H4x7cIUAJNPTMX7ByOlx85uvAeHVf-hUQ-8jYJMtAVgQqSqlnM_bTc0_UBD6HOxyj5TLTxEB1mvfA1yAFEDPwOyXXmxZ4pww7ub4W2wS3yRDZ3NDOJL33mTagtSs58KRQQxcT82ro5_HWycQ6ZFD5_QyyKaX9SrM8ZXgHjoM39L4Yi2l4iKZCBvmx2EEEWvRibp4wJIZcPtVt5nUAnoQXTcHeweG1oHi2Pn9qbg0IdTRyA4R5GOARnmVpWKrVvhc3aXNFvyds0o_5_iTnnZQ-pljWbP5Q-Nlbnc9RShLwY227PeuuwknDfStFJ_FhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puNgaNjZqqEnqIWp4yBMEEFbEgDuxaPgxa1QX7M8OxyL4HXBO9te0UZRnmXVBgnlimjVYKevUilZ5VhlHFfqm-C2fIHw9Kc_Kmcks28hxkUYZcRPaEz_M-63mgwZSSZUnioxgsX5Hsay0RrfXNJ5Pmy9inYc7jo1CGd5O53tVV-tWX_Be4-tLCSRNLuWspdfurDtUYUgMNowga06CAhUyykL3_3WaMcrJ7_4tRufbQCC4IQf7e7a-3DpXoHSLMk_CuJgudssqmjRflGShzsQDfNTlk9QtxmF0iMD3oqWHwOQX28dOUiHjI0SPqHlG28KUai2sBJ4HNn395_0VGZO_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=iZWRz3POPFDmhqPUhdoeUR3mQlcjybfrZs-cC2NmSm3ZdTnuKnIeWTdPyAVDQNLNx4A30EPmCfC5ll7rfVZvJBvA1PYOah26OqVnFOiV3U8qIIeK7vVUEZrkREv1iFBv3iGSDV9xHP__Kcle6l3mUsDTAmZAKDi7eK_xWhd5Q-_cOP-ujOq4wfWEmwXgcwKzoIg02-ImHARHgrBy2QFaiWJruyxz4csftXytf8aafrvfmb7qauiaUWIHhjLdJGgRcNTbXLgyKfKqRt8FdAd3x1uchnhkGvi5cJvocWo15CwH3fLmve8F9vymyFGsLooDQOEXpQE9QCITQGr193fc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=iZWRz3POPFDmhqPUhdoeUR3mQlcjybfrZs-cC2NmSm3ZdTnuKnIeWTdPyAVDQNLNx4A30EPmCfC5ll7rfVZvJBvA1PYOah26OqVnFOiV3U8qIIeK7vVUEZrkREv1iFBv3iGSDV9xHP__Kcle6l3mUsDTAmZAKDi7eK_xWhd5Q-_cOP-ujOq4wfWEmwXgcwKzoIg02-ImHARHgrBy2QFaiWJruyxz4csftXytf8aafrvfmb7qauiaUWIHhjLdJGgRcNTbXLgyKfKqRt8FdAd3x1uchnhkGvi5cJvocWo15CwH3fLmve8F9vymyFGsLooDQOEXpQE9QCITQGr193fc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QApDeyZibv7q_mFeWBavZLC6rx1ehsz6Tl8bMG4OHYbGRBq0kgBHi--dmNuH8PTFvt4Hbd0Bp0dXCDQiAh4oQnWBEKltfp7kaMakioXiCT0gXZlD9ct9qsMQWZRoxae7nkq8dWIO5-FFcVxb2-nCHUuG_OAH_FsRnHU-LYgsx0bGKSgBxqijAuq72_RSMfozfp_rdhE3C9Eml61Y48MB5SxOjwh0LDs-svktC7xq-BjweHe3DUH5LjDX-YbAbzqHN9IF1IV5Ar05v5E0wvINqklF-UScs8YTMYD_SuN9yk75NBCznn0pt3XPy-Nx1DuIRxsXWiNSuq6ba7bMamRKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6EMtUkXlc68gTFN1ATn40HNXUaCnGjuZ5N1kuBZEf9ed5Bq8sXg7uhqTWcBjzWgzymvrJTyCPIwsG4QFAT-x3iUnnC-fnFNDZCk5RKXjBNHxj64rZ9_AvbKXwwzif-z1RFuyA7_wqoyLrVZU8yQ_VRTVgQvnXhA-Z7FtB1H6LcyZqLVKyE2fdA1vOg8vG873rjSGkuNxydk7NDx9ZKj9B-3K3u3_2mDfIhycDE2DAAgaaReyNoKx2WvTI-X1EJglDaBrQttFzbepUNPCMdiOeYiPmRv9IiuWvf1HBAsW3CZSGfMM0GLyWLYuhYhimqo_5o46QKtIDQSYoHgkrbAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngeL1bNYs97QFJx_vZHpT6L7ne5ueEQu3FuzoWnSgGlpiANbRt4Ikr4O0EN1vvr93UAW_BxHstlbFJrOrm6acjoqbJ4XIPxwo3NwTKMnCRVos8aKR3eFFN5FXYuZtjCbHuwz4J7Glf_kKrgUCqbRGVN8q5T8hc3x7NMkPcB9dO6KTPkl2SaIo2v8Nw-dbqa5yJQqy6lhB86jBr3JAIYMnzgzSzVWJTEwV280tlBCK4jy4LSfoert8_t31NjAgUTemGbd0xATHY8PS6molpM5oqugPTOaHw7uZybv2jUNlxrSQHQUpPWD28dRruwnFOWtQIjEsJJx1ABc7GzTnhBxbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATlwijdBegvrA354EykyBDzQz8kcg4DJNes9zpXrk0j3rlelzp1G99BZS5sR6AAN4WApVMkVCxJjIwIjEH1qETdrCt0GE0ocUDQba-BM_LT5F7hlUL6pMlmg5VQA9iJPfRGkC4WuNTZ956xIJ18PcQmmE4deXC7ytHL5jmcqnh-Rw89gZ6scxdVb_hdryqe5LRkpKjTKkLSVGGCYXUeVBIxyh-5xg5jU5_3OFWTMLbg9u0he30xjzE7LXNvb-rtGxvNl8iv_QUnrPYLwZ-JVGYfwwAu3DiTUtwh3ytCWZVnHJ9xVJRSBrl_eK5HDpq2_r9Q1OXcT5NA2KqMyNbLafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4k0b54UJu7EnpJAC5qzxWfskQSg_ycX6Zbm8-AsCLbHWeEIG4YStara8ve-CimQY31dQxVgJIk19vXBPR1dmhDVDrGQH1txwD0W2UGsU92eWW2-N2-PjofDc3Fd9VjfuQwQlyekAzhP_ZNg9_B7oIE8DJBeFk4M1f8R7dF3VtAREuCeT2BMDZeUBDdv1Btt8kBVHufdmsZkUn54VRrF7bSl7ygVJEd2EPh8XSBnwOQVH4GzvCPdI8Dz6scacwcn4nj6Qca_ce8rYaylbFkwMWHkJ9JErRsl6E3aYP5OrMoeB8dE_z4q_gvX3BtpR8OBJoKD4zfTP2KdFThX87ZIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8lQFBi23SCpt92ZzzxvDZHzKTT0NoWdjpXq6P3GRDpNcgZhDrtOVPNDF9KkxHFz9e_exbFrsuAJ6HLfEgdx7uk3097LN0s4-HKXoK6Gf0h9j2nRnvwifAQsELnMK0kE_4I2nx4zti2Kn8e1wPxONYYjh6EefSpVfOFlnQLcMkEXFSy3h415F0_EE9VgcQCmyX3NyphRKNN97WdSIrC5xM9RYy6f0mkxYm-aaC3ojUMa7Hiw30FGa7jy4CEoZU7vlBD1iORjwzejq_zd6cpGfa8ZMv1lvctuEABYajXBMaOYxPwJWaSLZVHUyJ75Sw2v5kuFDo6Yr9d5LmKM72ijfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEYZoS2dSIyiEKqnWHj6iartwtJqSDZFvQ32QN5iQgT7tlFys0uuZAr7sr9MOairRFlOxYjRmwjHs_LMM-YBHUQKiXGgqxHLfho1K5SpxOD6tM62JtpHXBE5Kp3XyZuA_PA76H4RgjUiGFt6LjBk4NqNInvbhMyurWWqY4aCZ8vJnlsJX2lxDrDwSvMip9T1cVDrfesvtTpFissGjjZVgfOvdnuvt-NPh1zVpEArXzgcO9DP2mr605TusVJV7qAMGS-4MvLu_5GkYY8SRF1J_WFgf23rmgdPZGXGdoYOj_m_UztNHUR7ybaFO0XD6JUOh-7PJvoSySSV7H7eVLXpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nin9UKiacaju9S4oyl-zDNm45kKYTn5OvBf7nW8C1Fajz6xlHxX1L368Rt_Tb3UkIEiOvgS1jQag3_b-6Xp35cZvru42THQ_CF4X9V7jqGjqF_Hz2-n_tHGKtPpj2pjzDV5x4givz2uOJGJGvZeBGkzRCusZG86oFEIrL31Sri0QAthRcQBzqpckGmthOCyf_MSkpyA7WJ3Ez88zyyzsfzuQ5fEQfrBkDjiO43EN4nHbnxfKKXTxOCO6H0_NaCXfrCLFZXzkzN0PfeOdttPfBkGH0b2a29FpDlUgJOdF7_BthyMgexb_7iG0YTXATUwaIxquVELmQMFRiWMZK2nJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPnSC88OfSl7Kn4OW6iW5dMllClF3mwePrjwlW3MrcRu5izHdLTMJKOGJmAIazYw7hgXBgqWN7Pdjib-weFLbKnYDSxN_26J7EGxv4yrxUcI7OiJqYyrquYIYpORMN5ouszecqvSP-YWy_cwi-0TzQq1O2eZRE5TqbqyB5km2e5wVESLaFmXDTV8WKDgBRq0bnu16wGk-CLDP_bMYFUPRRHML3vTQ-_rifFCWrOimw5RXI0Jyc-OVecE8VrnpD58YESRh-jPUblDJCCbWwvSN5cWGziGEJ6G5bxsOKyNOHvRhdS-aVUeSmMbJLvCmrBJXQDqrZwezvrCH-Ox0mcS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqgUk0bs1E2QrR4LMy14wTVj10AwyypoId0mWK7MwC03pTPxd5XhUz8BXKmgdBAvSQfCjvEtXyrGFDYrAuZP9dq8HrH2p4hlSJvtK3MpXj_WyDg4uI8YnlGg2oVXWBEVPUfe0xuodT_BIKehgEEfefLH_Fb3CsBjV20PkO6pRujjuS1AY1Dwb6lX_pi3WFOlWjc_0yLyLV6c-_GMV7tAJ6jOwvrd9fxuqdpzt0HjefpAcYFmbvQlhkqmkHsp6w7Y_2AYpOaLv1XjONRi3-wY3j4dmboJD1dTyib4fkVTNSQgxzgD61c3Re7U8otEmw6XEiLJTiwv4TAV2eJBI64YrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=fvKCxL3Zun4qzieI1OboHESRH2UMPqVGREmHHU0Uc-z_Zut7tPwfEu0KKZEiqb__SQWHx8V19rFLhRwg0arOHr_SshXGfNN0rSW7LpgCwAMx23O7nCekMchvld5XPc0dwG4JUwpTCGJIMJZon3fRIeSCje-w3V-Gcu0F5SPOWyRLrBRZNO0W8x7ankKTBpnRXylu9UpOrtXOCrv3J84gK-PaGoyZjEYOmyprtZ-_5rTnwJlwRENeqX4YYnIB_znxlKh9HxWxUo-ora1_uu-PL3I5Aax1uK5HU2wArvkfJJ5VK2YiYZXmJxZMTaKhEn1L99aXUP3KEWpIiZTvqnosUXhpfkZE73celaOynk8MwpiSgqxhhyP3FjFQ3n9Gw1qxds2KwvOXyZYkp1Utb48pvHEhB5zUqIayGk_ha2W-GLTENtpRHGsvcQwmLl5SuDSySKccVf1EhTfumus3xlD2rEqUag-o3PRIbAT-v_QbHk0gIf7VxcrPPuTRim9A01RBcndSqvxhimHQDY59k5vsxnFX5tRAUXwKyF836TFIUxj76w8B5mckaaQhG3d3A0IpAymaJTwQglbmv4VFUCgFgyGQEQWcqDF9UME1OHFuV6mxUenSDsj5HXqwphx5-OOelNoten6JN_aByNoV_zAkKJjzHVPGucxTC9vah90Ot2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=fvKCxL3Zun4qzieI1OboHESRH2UMPqVGREmHHU0Uc-z_Zut7tPwfEu0KKZEiqb__SQWHx8V19rFLhRwg0arOHr_SshXGfNN0rSW7LpgCwAMx23O7nCekMchvld5XPc0dwG4JUwpTCGJIMJZon3fRIeSCje-w3V-Gcu0F5SPOWyRLrBRZNO0W8x7ankKTBpnRXylu9UpOrtXOCrv3J84gK-PaGoyZjEYOmyprtZ-_5rTnwJlwRENeqX4YYnIB_znxlKh9HxWxUo-ora1_uu-PL3I5Aax1uK5HU2wArvkfJJ5VK2YiYZXmJxZMTaKhEn1L99aXUP3KEWpIiZTvqnosUXhpfkZE73celaOynk8MwpiSgqxhhyP3FjFQ3n9Gw1qxds2KwvOXyZYkp1Utb48pvHEhB5zUqIayGk_ha2W-GLTENtpRHGsvcQwmLl5SuDSySKccVf1EhTfumus3xlD2rEqUag-o3PRIbAT-v_QbHk0gIf7VxcrPPuTRim9A01RBcndSqvxhimHQDY59k5vsxnFX5tRAUXwKyF836TFIUxj76w8B5mckaaQhG3d3A0IpAymaJTwQglbmv4VFUCgFgyGQEQWcqDF9UME1OHFuV6mxUenSDsj5HXqwphx5-OOelNoten6JN_aByNoV_zAkKJjzHVPGucxTC9vah90Ot2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=iFg_LL1kVga6PXoKBLQjiqBiHKTI7NyZj7qzVr9dzzZxCtNKQ7GGy12K5blW3YBuM7b-LlamO0u2_bpeSJdg-HGMu1EH7xHEPky0BMGJso4nKC9vxz_aXNCUQxerxx1LOzoLKE1ptSI2rnKNKk_iMyaqlsKkALBtg5rW-jji3nKRPwfEQ-T-fsLkdg4393HV-HSWFLKzGHEnoIF8RDbsvZc0ciminajl-KoyIa6kn5Pb5fdvWi663K4zBsUxViPobjAldFpydR-nqkMBRXbzelIr5hchIcSRvCoPrin3KhKIe1OCo3mmlcgypew6v82vh-_k4_dnrg9MgmMV09X-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=iFg_LL1kVga6PXoKBLQjiqBiHKTI7NyZj7qzVr9dzzZxCtNKQ7GGy12K5blW3YBuM7b-LlamO0u2_bpeSJdg-HGMu1EH7xHEPky0BMGJso4nKC9vxz_aXNCUQxerxx1LOzoLKE1ptSI2rnKNKk_iMyaqlsKkALBtg5rW-jji3nKRPwfEQ-T-fsLkdg4393HV-HSWFLKzGHEnoIF8RDbsvZc0ciminajl-KoyIa6kn5Pb5fdvWi663K4zBsUxViPobjAldFpydR-nqkMBRXbzelIr5hchIcSRvCoPrin3KhKIe1OCo3mmlcgypew6v82vh-_k4_dnrg9MgmMV09X-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23333">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23333" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj2dEgFvgxatTYkWkrauDAdNzCRwaYJAg1TIV29MiXAbrLb9tqzGSrQqpRWJdp3Agpg01G_oJbljSo8t7_0i0GnZb_3nxAIsZ6WYgvft2ucDJzaop2lvRlG8lQqc8Ocr73gFfC28JkRC8-elVTpRwfTOO3TiUodqMY7VNe7YBACfQcJINS0MaFUcbvQdON_MsaHnU2POIKClxkp2cCUZcm2sff4o39TU0xK4HiBgLyuFd2-2_s-Yb5lj21WElAB1y0sPqJHYJHbW0cEKU-vI39dzP_nma1-TNoLMjtorbUpMhC97yT0NFeIm-eMWEhwFvtJfKA001NhtmU-2vKULVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McTdy04LbUYmCtB-6tu2mrX0HKiM3dYxwrgyGzeebLoR5a95-bSfUudcRQil57h6sgicwtH3jTV5yGA-JDN8YXXT1Yf1eixTP_7ekruwxzNBkECunShVrUrAhayfarx9Awz3d_xshhvOHjtlfAu8udRhMXbN_nE5z-gZUz_J7_L-bohnvwOc_0oKdZ-jop6jMlLfhqTZ7XyR4xWCqpWoIkquuqM7YcCGtllZ2D0SAwKKMA-LQTAoMYtuHehQoU33xdoouu9bNAYDLUl5XGWU2xhvZsWIUQg6Pyc4pouNfX2wxjKxEfZ_bY1YMG7j4CD5osBcmI3DC9XJQ6Es59sN4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=AsY3FxY3VIS6rZ8-lHYouE2FAYLiyo443dm49LNplU21khiu4JaaGV_W4ko9oifdrEvFnNryJui2ZXw6-7C1OYZk5Iwp3vyqFtuEBMcUeajBo2FkhS7Wp63W-ji_fzbtX01qZUB2OHohdg-zTG7e1Z7kVv2RCm7nBqD6wHSuvbtJBc4QXUTjOXmtiJzm30ZWQ0uK408zkXjBVlHkgf6G4_JL6pSV-qSup03Qc3pkByYu8nePigzhexP_0Q7bYWQ-IrSaUzNHua3dJAz0BhMvZkxcqDYSjLHDTBNxz13LrpsSVZxrHX7_Mb9A7RA5JnCv55BIen-Gd-YkxwKu8dZtVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=AsY3FxY3VIS6rZ8-lHYouE2FAYLiyo443dm49LNplU21khiu4JaaGV_W4ko9oifdrEvFnNryJui2ZXw6-7C1OYZk5Iwp3vyqFtuEBMcUeajBo2FkhS7Wp63W-ji_fzbtX01qZUB2OHohdg-zTG7e1Z7kVv2RCm7nBqD6wHSuvbtJBc4QXUTjOXmtiJzm30ZWQ0uK408zkXjBVlHkgf6G4_JL6pSV-qSup03Qc3pkByYu8nePigzhexP_0Q7bYWQ-IrSaUzNHua3dJAz0BhMvZkxcqDYSjLHDTBNxz13LrpsSVZxrHX7_Mb9A7RA5JnCv55BIen-Gd-YkxwKu8dZtVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=sU-HG1QYW1mC7maWrT4yOXJRl8bmX2XggtwshbWruNpZl3h1WoX4W5Dfx11hpz1x3rTnT3UcSU9sYF3T1FpT-WiNfCrlcjE0UYKD9moZjg987utRcHQYt5pBRBgRufUnSeVcj8a-nicsrnDBBHAZ_jqwdP-de0Gz1QvIkkjsqjsFDxHIwJ3Q1nInv9_-StHo4k7nNqzoQOk15nAJdAgEYq3Oc7mdswZKyoWu8r7fL7rvT65md0aSNCioWKFpKfNaZStE227ICFruyrVIDE9lsdIdnOrHVA8d230sM8GZqPfgBhOrfywy8OtVdLE-MYKt5TTBWiRqo30LuZLR_X2uE6q-7kOn3IB_dAFlFu2giCloeUHLLDu9Zae6X6-sS_DqiDRj7-M4vsLPdv2ozLOvxSevh100f805SJyrYbFOYYiGtHfv0CZ6426k3kflhh8cOVkbmwDzalzBpXzYZlZIsm5Qc0PYPqxo1NqrwI5FyXSOQv2Yuk4ezEhaIp_4EBy0WLJsro31_4eiI2a2Lcq7o2Oz47QYlKoOL8CAlaK7cVPeuBoEa5oyHZL9R5CgkJwXCYjeW34fyT5xtGanoQoKnJxkSG6foOpUQPd07ENe7-dZwArDUEth7aNeWbYbk8Ev6Jjc6-YXQc0xqsZJek4hAGZN2vNa1QaueIVIDx3yBAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=sU-HG1QYW1mC7maWrT4yOXJRl8bmX2XggtwshbWruNpZl3h1WoX4W5Dfx11hpz1x3rTnT3UcSU9sYF3T1FpT-WiNfCrlcjE0UYKD9moZjg987utRcHQYt5pBRBgRufUnSeVcj8a-nicsrnDBBHAZ_jqwdP-de0Gz1QvIkkjsqjsFDxHIwJ3Q1nInv9_-StHo4k7nNqzoQOk15nAJdAgEYq3Oc7mdswZKyoWu8r7fL7rvT65md0aSNCioWKFpKfNaZStE227ICFruyrVIDE9lsdIdnOrHVA8d230sM8GZqPfgBhOrfywy8OtVdLE-MYKt5TTBWiRqo30LuZLR_X2uE6q-7kOn3IB_dAFlFu2giCloeUHLLDu9Zae6X6-sS_DqiDRj7-M4vsLPdv2ozLOvxSevh100f805SJyrYbFOYYiGtHfv0CZ6426k3kflhh8cOVkbmwDzalzBpXzYZlZIsm5Qc0PYPqxo1NqrwI5FyXSOQv2Yuk4ezEhaIp_4EBy0WLJsro31_4eiI2a2Lcq7o2Oz47QYlKoOL8CAlaK7cVPeuBoEa5oyHZL9R5CgkJwXCYjeW34fyT5xtGanoQoKnJxkSG6foOpUQPd07ENe7-dZwArDUEth7aNeWbYbk8Ev6Jjc6-YXQc0xqsZJek4hAGZN2vNa1QaueIVIDx3yBAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
طرفداران‌کشور‌های‌مختلف حاضر در جام‌جهانی؛ از سری جذابیت‌های بزرگترین رقابت فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23328" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚽️
ویدیویی‌بسیارجذاب‌ومختصر و مفید از مراسم افتتاحیه رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23327" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiiCFRdZzvoBeDBT6Q33cM4_D25T-fsadplT7rm8RUbdE0Tve7CGKhfNNq6S2EBT7oGo8viirBId7pCZ5KNOF8mI96Yx8DaNmfN-mNldo8I6wJWdBmYq7cG3jwfqPgeciYYwMswFtdRuIBHrSceHZpDhyn_wp8Wiesk4y3ahdtwW4GoyU3V5vw6PpOgF6ghyunjgU8A_RN_hd3Mup8e4XIXkdCTqXhAMfvmR-dljvStQYURd2yE4PDEVwWe1cuSUG2zfm-r9DcUk5EjvWeKENTlGPZnYbSal9rn2T1NjAi52Rub_xLjzLtfg606db4ylSpFNzxXeyAGr2i1VtEaZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idsbRPtaWdckkvbXss47lJvElL8KbyJhgRu657PHnAc0Kg4jlwJxswvu87zp0k_R-PfSaGn7EOnjeeQOK-QBIX3K0D2piiS1XXARYISNGOWfMWTu4dmxDn3u6pbqpoEdFnvv1E_ZsPojMXKO-VRKukbtuVbDKybkHU-wMSG9H9oh8V_1RrftSDX34Wr3vFH2OMEe6AtoVlz5XRgvvFY0KT79UBn_EFgY72keWbYxvJMmbULyOjTrRNJeG8v6lLA3tLQ2qkUWefDLr-jx5qDIIHJRdwz0N6SVYY8U_tnD2d8RhGpd-5COqYwhuzum5blwQtzPlLZqhYrjLPYukeizeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N--IRmIAX-rLEK962MyyYW1tXRLAYqdj-mWoD1WxLEO4CLPCsyZJXD6_Zx5Y3U1NbfvrJ5JoJcC5liQ6dqJZB6m43A5YnV-NM6sTydibuVv19K-8Ba0hVBvztMwWdEFMflmTtMky3JV6HWyxHR6ZA6c9ORAPE8md5Oz_4l0wujxr1x7yzbkdblzSmrptmQtTI5-oO67mmQ-PZdEOm6qK7M2Mg2vcS4oD9HTM00gS9VBxD2gF7mmmMwS6Ep92zAZs1buagxGpA6NECKbc2AbHbuMmDY9OJ57_iRXqPzqEDHo-KgRkgdZlRicRFc0Fyiflfz4n31r6j-cYt4Kr5fUzAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHIGHtya4ldt-QtnMfbHCd36anJkIx_1BVFrocOG270XfhxWdw0k-v7ROmnbVu2TOoHQrPsDpy8yHnl2Er1P8rTKrk0jZZkQrfv3fesUJeXvYXgBSQJwNMHDulgkIy1D0z_K9otnGULu3TMZIOkcVJRwqofiKs63EOMbnj8zIT4HE9SMISTMkEy6Ut8l9Gnc9yFREyG-CyYreBWB532HsXPzTVlyDLO2hzIbRlNp7GJ2tIdL_t5yf2fJ2AFc-6W48xL1WvxXKoOU4E2MqyBSx0veDP3Kk4EX_6P6LJpgonsI2FyhKyUQtn4eJLWRcHjTH9h7_aDs0I3gDQZ9q4iW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9_1f8GSrrIylwvFMmnWCcLBsEDEA1AdefY8O8vSaW4PC5OvapRMwZTXBigLVN-xRfSt9ohmjx1RUxDu3U7poJvkQz4i5ALpMzb4cZageKrjZ0sp83Uxk7KvrGuxMbCjgy9EJpt-05qyUyoiMkzYMIh8pPB69d14RngDO_NVQkOxDV6DZBEdpBg1sa8Ezf1mCNqMRiCE84DjjgfUtS0_5UsFhXW_jRpE8k6GBjnNQ_geOy4F6hxMFsL22fpHPDuOc--z_qcG8Oc1Qk61xxgi-OQoWnRd32STGDy3lSCDReG6xiBveKoQJKdOuyRIg1GLQQqEzjD_dpU64CsNCU-ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJLbBW6Sll8bNTj5PKw5XAmVPn__YBbGnZ0qXeaTG6y6tYBcraDWc9y-bjU9Ss0H__smqOG1Uvgkd2BdclGhiCgiIZyF92R7MruHp7Im1yZz8hXuYO9_yfNIgHIHHSP_hhqec890PPHVNo7s-w-TBdLK2OLyBvfUj1jTLT4gf9Xxapuy6rYaZ1NfhCYmROxxYXHchBrwu1-cEMBrDFvKMasQdW-VW1TZQfzPR-6WE6zjCAE8Ub0wAcqddO51FlmSniSz4NkWywqgr4zkD32o157q28dGQoUSjKhVP4uyJLO-MbyvnfIc9I3gCGGdDbCz8YpB15xNq_PyBkjcXpAESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7bVjrAQcKqkBI4ePJbRKMXWs-MiwdoddkMhMY3IAKOXrSGlxLBp88K-OGCz2OdKdoZhLPKcRbP108LHE5v0ZTp2FlBfvA1VHZJFXC06D82_bvAPPzTmSCvd8UWyo1fjNEttwNuoXcfG3ZwU4vAo3IAPqwk8tygmCXvVn1s7wKt0QnK5gPnFTDXpSbvrE1pVOeld8mlREDxne0ZgdIJaYQ-F4-qAWOcKe2yv6m70MszbxYBAIlSVNFH-JzqFC0oi8BliAsUVfIQlL_oz3a7J0fVBu7KKlXxU2AgIhh9rxlddRFlIbzIqH8X-M-lB4A2TVIfo1OF0B9MXpr_nOpC2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UEw2QqLEKWYqGJb4gogKrMaOmz-iXI66ejka5M4kVwkdOfXA-eQGrj1k0Fu2w4fLF_ZweT2fizspSAngYle187JKBnL9gQ8nFITHTya_NNnDxdWDJobGU7wejNjECuqkaNcUS55FP-BwkWLxrgrUFickacGeu5PzMttN5HaA1W8X5CVMd9D8ppnlwgDoSCCg0IVY0mSfoK7icSI6IkjY886z9n-GK26vWTg7UxdeYYmISbxENG6v5Cd5HW3LJcGj1y6dkO35PSAJNigB7clJ-Dm_rSw9Y9zoB8hYNSfHAyeP7zKHqPFrggMKGpB26Pv14RClQIOb2dihP3muJlKPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rJQN7rMSOAaoUmuofC4XxDwYf66kikbA5RTpg0Y3X6l1s-KxgTRgcqqV3WYg20hHfxCNo9N03WgMv_KCTqak849nc_TQwwftLwRfUkE62V6GqTq838g_S8wVHLZh7Mb8DalCmXgkTd7mN6hA5Z9SS3ziBdUG02X_qE1c01URB_HcQ2DVt6vntmYCmxLEwhRptOaQ0m9Nstq7GxP5My-bwzfiNF-gCvid8kgfl3u05_M0EML0nHXh7bCegFckBT1y4RF2UdYUUwu4tmlZasH8XyMjJqMsaLo1AQ3xGpph25wXJ2zjmAxnl7ApKpn-DvqSf8EZPyK82hZ7p_5pjRxpGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duNvjr8YPy6JVGUjSwxfRp_QBoZXvpH6ECYCZDyIikJoE17kvF5OIevc16NaOUtSErqRqxFYILsHsQ0OVWgKLqUk5GhMooSenqu1qOdnPQZGcNsb6ACGuTYYM59kGlaMvpeJJM0v-HJJztJtNw6e5Y7w4YcBPkFLR9JuVUzsVLAtxIbUSuEN3Fkdr2t2gehJbJA8MQqtv-97ICzVXSTIpr0R3Ixxh92E8yT2_4UywpH9A9VA9rahPOzVXIx4jmpozhCZ67V9YfwHD2uTQTbqF-kXWD3IZRurbJJaIXTwZaxPa71uP_r76mTT-XuvPKIKLKr-BKx8ImVCis1ja9ZDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رونمایی از استایل جذاب و گرانقیمت قلعه نویی دربازی اول ایران مقابل نیوزیلند در WC  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23314" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q23MX0vzvS_WGC0KijNmZ2E3wv80qEn2-M3usBh2C3va1R7TPgpfgXX7TUuFWgzRmMaxOnOGVG7kh_BX6Tmo0GT_DfLWw7wMBBGQcCoD5owk9NEsv8anSaqjOjqMOMFDwTzqO0A3AFihePIRIhdkdkITF2HAsVL3BWiVUs5WGESVPoBlGkbjhpndSLDZvpjAgD7b8GSn0tjMzm-pEkBD4iLA70f5DsggxRHMqL8_dvbPAq6wPl6wCah9HY-l10jChOD2iRXMOkF_yYWhZFWe9OyPDyVUeiySO0Fl8vc8Bk9SH1NNFBupccwd94NMStm9c9NLzlYKjA19oD94CwDRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میثاقی‌به‌منتقدای‌تیم‌ملی‌روی‌آنتن زنده:آدم مفت بر از جا خالیی ......تره! همون شعر شایعه رو میگه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23312" target="_blank">📅 00:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=E5AleX724ifwF71IQV9Zhpvp7DfPK72iUY6NoUZwQ_D13E_SGPazyWYu1hNLMOxYCYZXA6RfFw8L6xXamuHIW5-Kin-cmMwX_LBhJmJFgsnv7ClboE6ZPPIEnLgOAnGcJrgDurUW0HTvokEb7N-x6LhZtYFNoDhMENrRul3sjO9GXLjdkjREyHxMX1HkNwqxjGkPykpsxTbUr897Vk2UWnfE3X5wHIP2dK_buO_IgUPGMnHwJhg3no0RDoO-5-S3MXD57y6EEyeh6bAkFqQtBTl3Ez-MBz9YCqS3h5Lk9MK-ncVcq5vSsa3WkigVc_Cm-vKMVWNAN-OFYctIy0ZV7arze0ZkWTCBQi9Z3fMHhMfSi56b_sgfH_3zKbpyiADJoDseMtoGxv-heORewvrNP-tJVj5cCsIfehAngnkjhgMT-1Fi2kHQ9ugfMJsJZFwPdc1vHV6QR69NtyXYapNxJbv19soWJ9dm3U3HrJGPTzPudaEMgVahH5KcojbsMbtXmu9-e-_YgNBkx5_xWsxQ7HC8iwVDARSTdsl9Q6lf5UvYGSCQT9g9iAocGqQD-ZE31FcehVabbeb6ZTsNrOgmtX-GxjvYy5FYubVqLsjdrAYRYgcXt66zzXvtbLCzlV0BnGm8IIiJwXKkN_2gf_9Q2cAJAz-NntcDaXvUIVr216M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=E5AleX724ifwF71IQV9Zhpvp7DfPK72iUY6NoUZwQ_D13E_SGPazyWYu1hNLMOxYCYZXA6RfFw8L6xXamuHIW5-Kin-cmMwX_LBhJmJFgsnv7ClboE6ZPPIEnLgOAnGcJrgDurUW0HTvokEb7N-x6LhZtYFNoDhMENrRul3sjO9GXLjdkjREyHxMX1HkNwqxjGkPykpsxTbUr897Vk2UWnfE3X5wHIP2dK_buO_IgUPGMnHwJhg3no0RDoO-5-S3MXD57y6EEyeh6bAkFqQtBTl3Ez-MBz9YCqS3h5Lk9MK-ncVcq5vSsa3WkigVc_Cm-vKMVWNAN-OFYctIy0ZV7arze0ZkWTCBQi9Z3fMHhMfSi56b_sgfH_3zKbpyiADJoDseMtoGxv-heORewvrNP-tJVj5cCsIfehAngnkjhgMT-1Fi2kHQ9ugfMJsJZFwPdc1vHV6QR69NtyXYapNxJbv19soWJ9dm3U3HrJGPTzPudaEMgVahH5KcojbsMbtXmu9-e-_YgNBkx5_xWsxQ7HC8iwVDARSTdsl9Q6lf5UvYGSCQT9g9iAocGqQD-ZE31FcehVabbeb6ZTsNrOgmtX-GxjvYy5FYubVqLsjdrAYRYgcXt66zzXvtbLCzlV0BnGm8IIiJwXKkN_2gf_9Q2cAJAz-NntcDaXvUIVr216M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23311" target="_blank">📅 00:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPLxqmNb5V34xGzoNGLcUcDfqwdDL682y5ZnkPV0xEk32KUVo97ywZaiVbojhrBIYBqlZOCWVEMW6s5asMrYb-VN4AJUgE5HrAxXQ1sNkAMLDXWKRgNi5rEPFMheyNKa9NPn4lXOlvYT8nHAKVKY3hAvae21PIRKJmuLD1nCqUpJ8n8p8riT5RIVoh34VxMpPhNpQY0TXw9e0Lv_-NOZfdC-QX3hyPzcMfC8qHS-CwAwJGgDl80b0I8beAdZwSgn6GASNfByaGdOyjJJT-Dpqbcc6sJ0nbEzqsisUuiWp3R9Ir0Xo9MNu4U9Ju46oyChzAZcP9Mdp3NKySMYoEWVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول جام‌جهانی گروه B؛ شماتیک ترکیب دو تیم ملی کانادا بوسنی
🆚
هرزگوین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23310" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_5n8rVNoTQKMLG8J2BsUYlW78RCNT-SdWR_SNPMtNTZU6bK7Fwj-4aSnpPAQE6pAuxcq5tor5cj2uGo9CMZDdOYnkcXYpM-1Fi16trlreTPqJuGoNa-W8eKGrYR3hItW1iaFTb2thlA5AwTJppZFcr3V9AN_Rv_ZtgRfAjucSBAm__TbqfrZCpwKjybbswk8MobT62d4aOFm1gjwMhn_bayUrT5U6skXu98OgngKmVpQPX442cA3m779FnGPymz3hTmral47BE76XQ9bHQ5-V7ZBT51AHEAS5AC80ypB4Kb28H0JFuscLNH52kyFoPZOQ6cXqpnnNbbf3YTl1HwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPGXpo2-Tu5wcjv2aea1i1HsUrnEys0qiJpQYu5lFLMZPjk8N4zXDVa6Mtaw8xZQWVdrxOoWXu_AlqSxEYycOcaa_sfa_BOYmTg22Lp9lkf4qTpgwzzi8IMim1-4D-xPVa8UxXv7SX0aC71VUVcmSBrI2ZAe0s_MiKHwEQ4ymAmgF8fL55uJrbEH7Tim_vEUk2v-NwrCDOxUnaasDQ7g09H0dyAiEEiZwOF-xb6dMbeplPrIh7hChuE7p7DodnLVzUinG8Nml_x48srBJzkpYQV5dtsG6hljXWNpb7TclSC26HA_lZJXZ27dLcpsSggFujrgew9OA6hMld4jZR9ctQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23308" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAVzN7DtwSJnPUlF7mzgcR6JrLcqsDG5j8wI6VjgABPwtHcjX5CNq1uGvieN-XpRIt3jzYpeoDRWa1f8dLtW_7ySK1Hn6mrlRjEeBxg6ruzEIqHqnydZQTNkJWOtQ4WrbQbpi5QSEvLID3csWcLnsTXkp0_PqfEVchuWrPQRqqrSfxzeowR_7dS4lxuhCtbZfIojNHiGvAJQXIv1Aq3RGf5hIC6cktraJ99V6x3MXUNY4od_0iAHno0e1nk1Q88ZGEf5-UyQnxKfOh-7qg7Jw_Q61Ccb7dJ14XMBpnHIjHl3FjJTpMBcV_D2-DG5pJsHges99Kslcrc4WZgw0tSXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23307" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuYgAVPOZgEE53zLx0OfHMW8PCEI3d6y3GhbU4UvzrB7joUEsrhUt8Sxw25iaQmj5wW2vJuW0nRbURWm6THePg1RfMBYuPtksjbqTU478vNWGITL1QmoHrp7AFWE3gKuwzAA2iSk4l5pSuuoMmRv27U71ybUFuB3XBkN3vpiPfvHM6pFyjkXepLtMi5XjdboTJzV_FUpRGy5Pa6MFTUK1PTb0rGDXpCA1ekiqCOmP1EySv0IIGDrvgp7q7vBM1Y3AYbLRdML7-BGVfUbr39wcy1jnhxIgAIm36oyHTOsENCBziAGfI6e_Db9lNxEwZgPvrMiB8-J1aj773YAtoRc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇵🇱
#نقل‌انتقالات|باشگاه‌فنرباغچه مذاکرات‌خود را با رابرت لواندوفسکی ستاره سابق‌دورتموند، بایرن مونیخ و بارسا آغاز کرده تا او رو به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23306" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=AXJIkg3ILCWpxUkm2b0BTZPHtpLXg0XRvZTVEYLuQt27r0FGZVV7e_j3q3ZzPPAj4wyzCkkE4H678e7CJ4oDBHy-ZACEY0H9KKnl12WphKShBgGkAgJC2VeCJgx2nWSXucvuyt9J9YqkrWOS7pMpT2BbhW0rgmj8u1f0PvgkYoSZTlvm5BGsd5bJ8xE0CWpj_V53J1xGQy8rWdZ_F05T-sJx9sKjS9G37LyG-DJpB_fo56w-GK1cZW1CNRjgszfkUPE22SXfANZRg2PCDhA7xNE1r4M7p6l_I8i24Qo7vKaMHGS2YrC09yGt8sPOfHGfHKUBnu5OsH8TIb89FWHXGmMSuFlYV3VAEbWCQGVXe7BxQmJ4i6KoobCmIE-Wj0-4o-JdKeZsC-8JNcTGEdMOhwIBchvOqdiY3MWB3i0f67R2wXlheJrHhgsEZ3kJXyyRkQLMI3DgGeXuAPGh0tvInoIUlrKrSAyEzCTlHznGOx8eyLrCbYt0P4Rb4fd_xwaWZN_trpUZpeqqee9q8jmY2aGOvIARCKmc-2GVe40eliYSL1DOaMCWC4slmNlI3CFmmRqVsLLhMUAEuK8s1CoijjE9enUlBQZF6XWhKpxa42q_WOVCBhT_GhbtSfR_Y44m8RqFrij0mGXGBYnF3z474KBSnlCybaezz98BB3p9wYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=AXJIkg3ILCWpxUkm2b0BTZPHtpLXg0XRvZTVEYLuQt27r0FGZVV7e_j3q3ZzPPAj4wyzCkkE4H678e7CJ4oDBHy-ZACEY0H9KKnl12WphKShBgGkAgJC2VeCJgx2nWSXucvuyt9J9YqkrWOS7pMpT2BbhW0rgmj8u1f0PvgkYoSZTlvm5BGsd5bJ8xE0CWpj_V53J1xGQy8rWdZ_F05T-sJx9sKjS9G37LyG-DJpB_fo56w-GK1cZW1CNRjgszfkUPE22SXfANZRg2PCDhA7xNE1r4M7p6l_I8i24Qo7vKaMHGS2YrC09yGt8sPOfHGfHKUBnu5OsH8TIb89FWHXGmMSuFlYV3VAEbWCQGVXe7BxQmJ4i6KoobCmIE-Wj0-4o-JdKeZsC-8JNcTGEdMOhwIBchvOqdiY3MWB3i0f67R2wXlheJrHhgsEZ3kJXyyRkQLMI3DgGeXuAPGh0tvInoIUlrKrSAyEzCTlHznGOx8eyLrCbYt0P4Rb4fd_xwaWZN_trpUZpeqqee9q8jmY2aGOvIARCKmc-2GVe40eliYSL1DOaMCWC4slmNlI3CFmmRqVsLLhMUAEuK8s1CoijjE9enUlBQZF6XWhKpxa42q_WOVCBhT_GhbtSfR_Y44m8RqFrij0mGXGBYnF3z474KBSnlCybaezz98BB3p9wYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23305" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23304" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCfAV0c3A_QX35TK2OI0uPWHm54b6Qap955e6b0s_CgZ0-Szb2_BhYwZvsrmF9LppfNdbHzFAhmqBHl3LTucLFT0yh2paC9P_PPB6iGLoOtYzi3XfTdiPj1k3wsu8F-vksZFKMd4NNtPqWuymfht159wAZgOKj75PZbOwCmKZqBsVTdUpABG_iZPMC6TjiTgsq3bq7qWx4EFiVO_41Yh_THjlcrGVIg6DaobWuXUxwpndcbRIH_pUihL0GeR6Ow0DHD-cX-co8s9HeHdebTpKphEUTpARtzHVrnp7P0BQ1AB9F5qnrJf2d-sTUVSAo9NYvs_8BJnzWKQPchomHEmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23303" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-LMG2L53yvxmZ4b7OfJ0GvWuqRXMorJ6p_CKhgg60uPExW27gt8WcmyAuYCHdQmQEq-eN5T0t8_b298nUH9u1bb_fMHBEaNto9qDKfXiB0QypKojXe2_GD-gMWwZDf4mIPm3sjkvWHyu9F9ikmy10Z674KWe0byLIObSRGOriloEFQj9bhOBiaQcl3zFp_yd0Wz3yGXf04y_ryPJg1coLYbA8yPFh39P92Tath97xuo1pwO31xtyLwY7Fwr3hAzEV7oaLEUwFZ4aOknuzAuQcncYal2VEPgADQcI7vCycHdbDGS_VcCoN0FF2KkUjjpCsYQKR1o9c0V49q72NLwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5nY4Aee7zlBY2HF7F3tujFsrMRAQaMWp9QteGw_4Po4Bs_ZtdKaCdP7EZ7qSE3ERzH07i7hIHlb37fvJmmO0z83EG9mDYewvzw8woolIzBsM7Olx3f4FOj4M0tbqRdL-fT5JddYOOt9aGrBdr_yrnRGfJ1s9lp04EeBagxovbweYN7thK4kGZLa4OWvQYV_Y3YzDmbmdXPm4U3NTX6FTVrACEyQHa_Sv6U7rZa5dBZ6qtnXopEb4A02PMpl0jjb0AJGXhlnIYbzpEfLrtPTkP8VCZBpdj9HxOEUk6rVy-I5mYflJ-w7iHAehTaAGmYp-UnKz_YQhOeP7owOtbh-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfMXKdKfite3nvWonjK-AMb3tU_dICgyPd5oEuqOFUx5M7bFiiGB_5q_irY6IV2hY8rPMjJqHHyt570KBTb91z8NcSlSv8BCE363AIQB-ktv27xszFdyQptQ7Jzo0c-oY7NTXXwuOyodTk5qoa5VYNlHCMz9p2vaYh-kOmDD4FCigjcbrlztdD0ul9MXP_bEhEQBDlil2XprnwuPI78MTGQaQqelNT8WU67kdPv9s0d8qyQoE8lFmmZbs9iuIzH041KtcjB12eu-v97zEt5iAwa6TEyxXrmAJfPd9y_dqWg0hcFFqTQNCtUVDHIWSjN6XoS1_nEqBv7vZMUqMrQcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=bDxh34y7TJVTkUUG8qm7D8Cw1xc6LcoWLCt6aRWw2gZqHYTkkxD0UflRINihRzqGkAPcCLn8RtCMUlqUNCZmplJ_Mihn3rd1IR_SyTZ2cRDtR3mR5pCUf7rx4zvJ1hEjLoFwYF8Cv2G-qKarwacIpu_QdIE0hdMN7l4QGNK0xeoR6Yk1QrILciMXZzawY_m13CDqg25YVx0KYplwVdbRoXn8j0jEyfWLB7qjFZ3FHjoWEC9qvpxg5meL0WSbKfMGD5_bYw1Vmk7BBKFoFs3pe8FmJTa4Nh-ADXFoiZHrFqbmFnmFP9OO-3nMez5myXkOghKtCxgnkUWlGuTJp8bCpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=bDxh34y7TJVTkUUG8qm7D8Cw1xc6LcoWLCt6aRWw2gZqHYTkkxD0UflRINihRzqGkAPcCLn8RtCMUlqUNCZmplJ_Mihn3rd1IR_SyTZ2cRDtR3mR5pCUf7rx4zvJ1hEjLoFwYF8Cv2G-qKarwacIpu_QdIE0hdMN7l4QGNK0xeoR6Yk1QrILciMXZzawY_m13CDqg25YVx0KYplwVdbRoXn8j0jEyfWLB7qjFZ3FHjoWEC9qvpxg5meL0WSbKfMGD5_bYw1Vmk7BBKFoFs3pe8FmJTa4Nh-ADXFoiZHrFqbmFnmFP9OO-3nMez5myXkOghKtCxgnkUWlGuTJp8bCpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veMQd_oxeKZ0FeE216ywRBQSU9XOgRnkn2LdgNjclERT4IdPcOexlqB5ogg9kT0nPeUgAGq0sdtw2uYcIpR1C-BhKmYCMudGGpHFkygq06Uixi5jlfz4UUFE89H1E08aKPcGkVyH-vGkvFBURsaT3lPb6T7TBROMY6ooafSD7LLoUPLMHzQTPjtp04HsvrKaFuvCjgCvPWwFJVuZjih_zs8aaX0FLCbckwOBZdV7H1GMd7cHm0PZfer_a6yK99Oh_ISASsQ_gNVuwwvXOiYNjlbqs0TKYU8kAc-5AtkaALVWUcYurBhOM103OpidRYrVNoTlYdDY5N6Jq_JeH12B6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8Sv5CiJ9rg35qSBsEyVfzAY4LRzMb9H_XkuzjyULblFbNG3rmaG3dUwKbawn_QRTc4CWEnLfbOqtlKMMq2WPVAEcuMMJft0_0_8fbFl3k18zRNF79xjjuXSQubAlUkd3rC81IIGv3aFYgs8_MKzuQhaF-pPPAiPARTs5CxvwO1Qiac11csmdvSULuA5rjE5bqAQkhzrMYHs7qwRpzvPeE8o2qJR-ryumNWhFBd9k3GgNTL-vkfENdK99A9QIebTGSK8tMNzk3dav6l6vVvj5wpmsGactXrnG6QUT7buNmd9KiXLf97fpicVRNj1ys_XyyNsnWiDksPMsh7JNV4CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnfkncYcnsApZLUPLc5hxPdE2ce-Jb1PEmNO75LTPWupbfJ7bL12na7JAJOHUf1Cn9X4_hKIePs-gev3r5YOHdu_aVBwqKdjvLUsJhuVC7ZzCk9-pNuGyytM3b3VrYgs7LI4hs44wr_URz220xnHotP8FmOhv4dEt5imlI8pudJ2XT40nKhT4RKyoM8GN4m4UQs1S2TX_tVbVjGQ-9nlHRZm8Eo-kd7sEb7t7IBrHkzeOx7IHCdpk3ffYSdMguiSoabOtZ6dNpPEO1ZJpuQlorxKUKcFEdsNDDOgZ646xyaUXzfv7MtkkBFShjcEmbGV4RuCHieuZ_XagJSHM_1KnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txzy_XeQQ_28iF2_mEMQtzfc1W9YsdkdJGLAMm9qtxLMwFnLsoVkwHKDjkuAtNwUCIQUwexfMTSgMgRU2jRJSTg_CVjTzqvNg8dlCKyLmmoUocS_kzqTY0bu_OO_ry43QEffdTtMMuFFOBdHPKBZB8YNulijsZhVAYbaRFbBuBHvi9YKzS16NoTwDIZRoMytzbd8487KBDtEJdNcHLYDT1gGVsUWk71jpm8-5h3lqo4OrMLHBqg_I5CDv_bhi-Zc40gUjGxiPBLw7XM2WhJDPg2-m8gW2JoFyXBG_clY4-nw8uRaTANF0sz5so_XQpY_9eCTiggAvejV-YuH-_RXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=KHN8UJqimIMfkzzRN56FlTNyOMeqzX9JvHGCWXWa1VU47TukSrjvNeh55dOeyDzGMx_YZWmpzpSjtAIeLHqO5JqzqnfZaRvbmr9xC_gMD347HkFTmqIgGESwXQN9NwuJiQPLRb7iU6ZbxE6z02SVvfG7NYTlrgBj5abe1PPI9sobBX2OXKk7Y4G8_xZABEn3-8CGeYEXjqK7P7E-XBnLsLxZFOFuohwOOUbV1QPrwHjZa2kJ43VVNOUyU3rzllfHYSBFL9jPq0d5TjHTsmI3DK0hKUCdZUqt8QnoV9rwRm0iJa-jcZJkwdw1b3ibcF-O-oKSnYP782MrBlM0lucXRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=KHN8UJqimIMfkzzRN56FlTNyOMeqzX9JvHGCWXWa1VU47TukSrjvNeh55dOeyDzGMx_YZWmpzpSjtAIeLHqO5JqzqnfZaRvbmr9xC_gMD347HkFTmqIgGESwXQN9NwuJiQPLRb7iU6ZbxE6z02SVvfG7NYTlrgBj5abe1PPI9sobBX2OXKk7Y4G8_xZABEn3-8CGeYEXjqK7P7E-XBnLsLxZFOFuohwOOUbV1QPrwHjZa2kJ43VVNOUyU3rzllfHYSBFL9jPq0d5TjHTsmI3DK0hKUCdZUqt8QnoV9rwRm0iJa-jcZJkwdw1b3ibcF-O-oKSnYP782MrBlM0lucXRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپانیایی‌صحبت‌کردن‌جوادنکونام کاپیتان سابق تیم ملی با پائولو دیبالا ستاره تیم ملی آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23293" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmlfzuLhzzn6BLTllvEgDjpHub_rLZwCiL6kjSvLjwxZkGxs00OirDZ2mhTb5SU8y8XK87NNB97YgLuHJnXoNrLflTZStcKIeReoUxMfVTKs0eJ4VNjZGkZ5OQI5Q0GnPCosqI8jZQbmvnYqrnPBXlXsmWt6xp_BdNPAdGNxRadknM0sXv98sbIUIU-soXDUuyjiLQgnVRCvjdpR8j3997daRyIVEghl8tjaDm9I6WLhVcip6HmSXGWQzyzhYOlU6tp1lXBFARShLdXTZISeX7o_0FBAu5EhAGav2k43zjhJTUVk7aM50keouiTGjO_y1Uhlm9Vx3WcjB3FDcIGZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا برنان جانسون هافبک کریستال‌پالاس؛ با لیلی فیلیپسِ پورن‌استار که‌رکوردسکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23292" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5mUQ1r0kJAqOM9fKcqhYgiu7j968B3DbAZjeBbefc0tsuexBM8KDQ5G_YjOHFARPpnzN5puoEJcmxIVogUECB1z2gelk_RCbajlRc9405a0be8HxWNzzhMIQAHS2EwfA6VH0gtWuQwXOa1TBKSH13PoB25L8JdM0-QKMd91jUEyzXgNZx5pVuYvQz0Npmn9DzJrjvqbUm_CWhgQ3TWY1BcoQ3pDLOp-HPQt-RODNdDSAg04VofOtSO3SxBmqilTiBf08vgbNL0glb2D5BHxtCRKNC86G9Rv2Jmr78zj-N-GQs7G61RG86hv8MGzouygBJlXaRNcj2JIpVZompAgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌‌ بهونه اتهامات جدید توماس پارتی یادی‌ کنیم از‌ زمانی‌که اگردوربین‌‌لپتاپ‌نیمار روشن‌نبود، اون الان بخاطر پاپوش مدل‌برزیلی پشت‌میله‌های زندان بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23291" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXl-Obi_UEBqabWZoj8RIJFETpZDTjYsAUukSgwOL3lXynAo1S2n3pimpxjKdl_X-V-tkeEOCigFjarB8lN1HLEyfNFczo50ywjVdjF7M2tU8gWl7gsUcoT-t5OYCfgBag2cgDXLIN6W4Mxf8IdfmnCLpG7IQiUlx5JbQ4nDLeRJaFKdztoBMk7IyugpKa4ONyDC0RzlFMatNSEKQoVyxvZ5lY9HNA5-lLwT1rduuPuCCtWl4yNAiTvtrDYrQWyaJ1434pI97Gxb45FyuedXEkvtjwkD03_DkzLolX2OiRU--eo7pUkQPvDL8QRRZIUEd8oZvB072WrkySwJOBVOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23290" target="_blank">📅 20:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEHrhqZMcOmHNKp1h3VAbx8hiLb7cQ8KNm0ygV4-D14HL212Izc_AeMZUo1jDwgNYcDeaGvN1VAHpV25mRjFBzJvLI9WUeAFJDKXWujiGnPg3_z6JNAmff0Zs3S8b4qNNc3AOtqGdBOGoJF__knEPeodF8-kLLezWbkYZ-tTTBUOjjRFpGf9KwzMyUfY5JI9r8eU9-aTvxOttibTRkRYKstWTE7bUsCLZhvxUuio-q66-7NdRFfZMlZEZoqupBuWOPOhu11maTsGbXw_GY0rNO6anP_P-XYL6vuLrjKOYDH4mmWrss_K_Zc7RDqa1OcZirVxbCLrUrFL3FlW89zhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛شهریارمغانلو مهاجم‌ملی‌پوش اتحاد کلبا با اتمام قراردادش از این‌باشگاه جدا شد و بازیکن آزاد شد. شهریار فصل آینده به لیگ برتر برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23289" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdxsNn8WTDlkWeDNislijYc0FdKP3GZMlRSINdpJuQO6jUkUu6pI9wtD1KToy1SXEnbJ3Fp7Y93c8rjwYUYN0DmbPZfrPbYuHwhi6PS9s1S1LiqzN_IfLM9u3SX7CFnNOgHzrTiZzvRvuR3E4pmf7QFDxX-ZIcPunBwnbVBOu2pClUXRJq9t6FdW3SpLk2LqfFP0jYG1CmtngIT5Up7fi-FCB4oCtCmt-X_jqdHhoWbJ9C0rduQxgLVEYb9gc4K_qGyAp47LWJRYPc6JGnaQOPPWziU6pA2qEqeAJrBTsJiG29vDmXa3aFbX8UTiQ5RqJH1xjY4liJiFNAOl3iKr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saD0DKdjFspWUA3zqXQqBfF341J6bj9Pp5SjyIoJeQ4rjRSbWWiT1MRi4UhjaTmH0oC9NuiKhw6sKoKyGpZBRhEL_qsY30jKGTf8x3hBtrkn1oU59nxPvJTuJogBRW8y7nrClhIf4BnrqGjgjmqBrBKjJYv5bXq1oobI7bYf3qjCvIiJCKk3G9Vms1hl1TO7UyTz0Yy5FvV1-r_65hjETHuf2YoQYsYJH0yvOEazh6HMMJnqwQyrZS52eY0-LYwvELZj5WmX-Rh5fOtixJ_Gf1V1J-oEO9cgSbST0g5jdjUCgK2hG0MMy09GfsWiwbLu1M9CX6O375wgw3ZRU2Nn7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
