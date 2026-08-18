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
<img src="https://cdn4.telesco.pe/file/Sw6rLk3K6jIHpErAQS9UTOwgOjR6XoONE_D-mcaAx6JgAVHlXVWrHwyeCoV6jzwdO7ki2Pzyq_8qMqVxj-OjoJzNaOrrhStf6oZ9qFYpzYx0gT507yi9OjRcNfIy00vl6sZfrMCngTljYVb8wat6UJOob0MU2GLOakTIzRgXOEX9F-U84xnMrWpid69u3miIUMVdy51OEJVbxySkyzn_mYbNBgxkOItOLrz2TsxLdwNu-sxZForYckdASU2gvAoW8iF8d0aBOpfZJUKJy0vuaoIeVQ_TmwGicxsrjz6dgkAMpChq8rXMwX7f8jYadHmnyJ_nw4vgBh-wv0kyspOLsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 985K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 21:53:45</div>
<hr>

<div class="tg-post" id="msg-142505">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b515710a.mp4?token=TJllpAlZZIosZSsLAvuI6wP3j_VGLSOcC35jdrncecdVLWQ0YQhIqVxLZtJHX0IXeyJ9UM74DFkv4sKVdJrFZBkilf9lIdfU_sPyPFmmJSATCNpO0L_PJuQCDfEp5Zbzxo4mhgooGPe7wG5mTKSOPBjentzrrckE5pMHoM3fo4eyE-2OaPWePrp4EutZ__D5kVRy612J8nmUNoYEsezOrZIQpgVbsxhEU72o3kPUEM3k8h-krK7zXgL9SWNGV5oX8abCn3dKrneZdkNKbcyqU5zI6KO4lKCMd9YoefMbgv22uKtYWwqBs-AFYuQRK3t3nGu0Ze2eVWRunNFJ1xcAkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b515710a.mp4?token=TJllpAlZZIosZSsLAvuI6wP3j_VGLSOcC35jdrncecdVLWQ0YQhIqVxLZtJHX0IXeyJ9UM74DFkv4sKVdJrFZBkilf9lIdfU_sPyPFmmJSATCNpO0L_PJuQCDfEp5Zbzxo4mhgooGPe7wG5mTKSOPBjentzrrckE5pMHoM3fo4eyE-2OaPWePrp4EutZ__D5kVRy612J8nmUNoYEsezOrZIQpgVbsxhEU72o3kPUEM3k8h-krK7zXgL9SWNGV5oX8abCn3dKrneZdkNKbcyqU5zI6KO4lKCMd9YoefMbgv22uKtYWwqBs-AFYuQRK3t3nGu0Ze2eVWRunNFJ1xcAkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه، لاوروف:
روسیه حق دارد مداخله مستقیم بریتانیا در حملات علیه روسیه را مشارکت در جنگ با تمام پیامدهای ناشی از آن تلقی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/142505" target="_blank">📅 21:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142504">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزارت خارجه: ۲ دیپلمات فرانسوی به‌عنوان عناصر نامطلوب شناخته شدند
🔴
ورود آنها به ایران ممنوع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/142504" target="_blank">📅 21:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142503">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بر اساس یک سند دولتی اروپایی که شبکه ان بی سی؛ به آن دست یافته است، روسیه از طریق دریای خزر در حال ارسال مواد منفجره، قطعات پهپاد و مهمات به ایران است تا به تهران در بازسازی ذخایر تسلیحاتی آسیب‌دیده‌اش در حملات آمریکا و اسرائیل کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/142503" target="_blank">📅 21:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142502">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا، توموکو آکانه، رئیس دیوان کیفری بین‌المللی را تحریم کرد.
🔴
این تحریم‌ها هرگونه دارایی او در ایالات متحده را مسدود کرده و تا حد زیادی او را از سیستم مالی ایالات متحده محروم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/142502" target="_blank">📅 21:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142501">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b672ecc080.mp4?token=TTLorQsUUqlUJdLc9lRZWFXI5dbwqKapIcu24Kagbm1F3gZdJn7BJRu-Qm-U8jQNjsNfP4B6TZRWfFlSBoCt8r7io7Tp3DYOWEZPL2E78qS2oy_zC-9mTTGlhrtqSDkL8Q-tPNGbX76ADxMJJxsRttshgbdU10ACO3sYTUz9u4f8MWaLywTNpXMjGBpYbfXfAjgfCjej2hfSL45uKRf3xDgWFFB9V0_IQ5baFCNMmXiLDRqpluYnD32Dp-1fEQA4jayU4oge6sUazk-T68wjFQCHwe5IhmKcWG0SeuagcEzI5XbY8BFRjddACHutPUohj5F2JkkwAKboIgVscsrFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b672ecc080.mp4?token=TTLorQsUUqlUJdLc9lRZWFXI5dbwqKapIcu24Kagbm1F3gZdJn7BJRu-Qm-U8jQNjsNfP4B6TZRWfFlSBoCt8r7io7Tp3DYOWEZPL2E78qS2oy_zC-9mTTGlhrtqSDkL8Q-tPNGbX76ADxMJJxsRttshgbdU10ACO3sYTUz9u4f8MWaLywTNpXMjGBpYbfXfAjgfCjej2hfSL45uKRf3xDgWFFB9V0_IQ5baFCNMmXiLDRqpluYnD32Dp-1fEQA4jayU4oge6sUazk-T68wjFQCHwe5IhmKcWG0SeuagcEzI5XbY8BFRjddACHutPUohj5F2JkkwAKboIgVscsrFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: جنگ‌طلب نیستیم، اما جنگجویان قدرتمندی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/142501" target="_blank">📅 21:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142500">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
هواشناسی : از روز شنبه دمای هوا میاد پایین و دیگه کم کم به سمت خنک شدن هوا میریم و از سه هفته دیگه بارش بی سابقه باران و برف تو ایران آغاز میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/142500" target="_blank">📅 21:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142499">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر بهداشت: سالی ۵۰ هزار مرگ و میر به علت آلودکی هوا اتفاق می‌افتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/142499" target="_blank">📅 21:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142498">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef3ebf5d21.mp4?token=WuJRNiG546LhRNV4FeytOQtJJzsfDBlNLG0oiIc1kJh-O86hNmKZnVkgJHDFZXUqdIZdiQ61UnEYByh-Dki-DymS_m3syVf4H1pDsDTF2_1i1IJrLOiXBOmK-_tMqBCfKqOripPMilmfWIwetMA0_6vViVxePxklLN0syaNVPJN2zc9VXpqbWnKiwbOA_MdY3NSmETbfH_JYtyJprusUb1272NKZcx0hES4UZ60tnXIy3ufiMvwEFL5BScM-6GR2ihd-h4YO0H8QLDRR7xQmBi3d4RXU45UiJpXpPtJ2v5cTEp2kY2j6Z5BcBbYmXIyG3XzIlUnUrkwRlwBYOlvsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef3ebf5d21.mp4?token=WuJRNiG546LhRNV4FeytOQtJJzsfDBlNLG0oiIc1kJh-O86hNmKZnVkgJHDFZXUqdIZdiQ61UnEYByh-Dki-DymS_m3syVf4H1pDsDTF2_1i1IJrLOiXBOmK-_tMqBCfKqOripPMilmfWIwetMA0_6vViVxePxklLN0syaNVPJN2zc9VXpqbWnKiwbOA_MdY3NSmETbfH_JYtyJprusUb1272NKZcx0hES4UZ60tnXIy3ufiMvwEFL5BScM-6GR2ihd-h4YO0H8QLDRR7xQmBi3d4RXU45UiJpXpPtJ2v5cTEp2kY2j6Z5BcBbYmXIyG3XzIlUnUrkwRlwBYOlvsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه درباره عملکرد دو ساله: رئیس‌جمهور بارها به دلیل انتصاب افرادی از جریان مقابل مورد انتقاد قرار گرفت/ بزرگترین مصیبت جامعه ما دوقطبی‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/142498" target="_blank">📅 21:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142497">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd6673d4.mp4?token=prblHgUGOzDC_W2MSMuYRvrknt31_XSby6AJ7X-nUksMo-X6vofoNRyuw-FT4LO2tSu2OnIq-u7fG59RTwKxWUHGjlaZD85uWmFJxY2a6vbNOPwpFPEcbPB8vuueEnGybvWujCyBsHmaMQj8ZbAXuua0hQ7MHanjYJdnuwC0qGU0Yc1P4RPqLFYrXdbICLGBISEewUvXasVQDS6Da4PGjQYCzyocix8bmoHvT46rHNWkV9RAXlQhCWOds2_GShO18NgiukL6MTBJSXZJE9ttcbGEez0lHrc2xNtgOQKHBikOBQf0JL76UjFbKOJ4uZqaoE1ThNUsGsK_q1EfkOqC3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd6673d4.mp4?token=prblHgUGOzDC_W2MSMuYRvrknt31_XSby6AJ7X-nUksMo-X6vofoNRyuw-FT4LO2tSu2OnIq-u7fG59RTwKxWUHGjlaZD85uWmFJxY2a6vbNOPwpFPEcbPB8vuueEnGybvWujCyBsHmaMQj8ZbAXuua0hQ7MHanjYJdnuwC0qGU0Yc1P4RPqLFYrXdbICLGBISEewUvXasVQDS6Da4PGjQYCzyocix8bmoHvT46rHNWkV9RAXlQhCWOds2_GShO18NgiukL6MTBJSXZJE9ttcbGEez0lHrc2xNtgOQKHBikOBQf0JL76UjFbKOJ4uZqaoE1ThNUsGsK_q1EfkOqC3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی
:
حتی یک دیپلمات ما در طول جنگ رمضان خدمت را ترک نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/142497" target="_blank">📅 21:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142496">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
هدف قرار گرفتن یک فروند کشتی سعودی در بندر المخا توسط موشک‌های انصارالله
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142496" target="_blank">📅 21:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142495">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
یسرائیل کاتز، وزیر دفاع اسرائیل در پی حمله هوایی به اردوگاه الشاطئ غزه: علیه هر تهدیدی در نوار غزه اقدام می‌کنیم و امروز چنین رفتار کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142495" target="_blank">📅 21:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142494">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراقچی: به طور مشخص در قانون اساسی ما کاملاً روشن است که تصمیم‌گیری درباره صلح و جنگ، با چه کسی است.
🔴
ما کار خودمان را، بر اساس یک فکر و عقلانیتی که عقلانیت مجموعه نظام بوده، انجام دادیم و طبق دستورالعمل‌هایی که به ما داده شده پیش رفتیم.
🔴
این چیزی بود که الان هم رخ داده. ما در چارچوب وظایفمان و در چارچوب اختیارات‌مان حرکت کردیم.
🔴
مسلم بدانید که وزارت امور خارجه وظیفه خودش و مأموریت خودش را خوب بلد است و می‌داند که چگونه باید حرکت کند.
🔴
بزرگ‌ترین مصیبت جامعه ما دوقطبی‌هایی است که بیشتر کاذب و بعضی وقت‌ها واقعی ایجاد می‌شود و ما نتوانستیم کنترل بکنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/142494" target="_blank">📅 21:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142493">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnUuVQCcug64GUq4dbyYfv7WMUXULHt39R_30qKS9qciNg5TWpAfJ8d_R6xurj2K2n5pn3ao96w34E67cTnlrlN8bPpcI3G_pkhBe9Aso5nCHyeXDBwbqorhcfaYJsWz9UcpDsZXwfqQbFO_m4jg18cMUo4aIPKse-OfBvi4zrQ52pJ9iB5ne0loLsXvpuWVQhDAWy2FxY2efbnsZ-dhfgoW7qSO8wsRe4GZDwxpuMpKPD_6fiIrIuAG2JglRJ_82V2q-Lh1CT7thIuXhhNSf_G568YeLsmxdkNtxbcJpqPuStHsEMdrMeeahwYZYtyOdJa8mW_orEI4q8CTEN8DWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال رضایی: به نظم پساآمریکایی در خلیج فارس خوش آمدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142493" target="_blank">📅 21:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142492">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh8PxiY57IzGIZxMKhmGtT4pxRoEawaZOYo26SQXdRU7Jy6AvFjMnGS421wOoE5plcUCbS_J7ePLiVwamNRRUQuLg5F_Jo3gHCF1lIrib1TDFI1PUYt_kas6SDuIezM575FJmSG_Rxsh5g3Utlahm_Je5cmUtKGMl0aYkIR63qMWPL5PWFiScV2cNb0Tbrz_eYtnuWuRxv0IJTfWi6LmvJ6llxRLV7_-H_xq5LQCyQ01p3dzZ-5Izqj-rcsF1AC5HD90FP8661GybQHW0XrmM5QxdOCvFf60Lhe_pZQNSOwQ_s6Q8eQjXduL3oqlhKygLIEhRiZp4TQMljUXYWAsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نرخ های جدید کارمزد خدمات بانکی برای سال ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142492" target="_blank">📅 21:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142491">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عراقچی: پزشکیان به کل جامعه نظر دارد. همان‌قدر که به آن مردمی که در میدان‌ها هستند توجه دارد، به مردمی هم که در میدان نیستند هم توجه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/142491" target="_blank">📅 21:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142490">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
عراقچی: انتخاب آقای قالیباف به پیشنهاد رئیس‌جمهور بود و ایشان این پیشنهاد را دادند.
🔴
حتی در صورت‌جلسه‌ای که تهیه شد، ایشان اصرار کردند که باید اسم آقای قالیباف به عنوان مسئول مذاکرات بیاید تا صورت جلسه را امضا کنند.
🔴
آقای قالیباف تواضع به خرج می‌داد، اما در نهایت رئیس جمهور گفت من با مذاکره به شرطی که آقای قالیباف حضور داشته باشد، موافق هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/142490" target="_blank">📅 21:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142489">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خبرگزاری i24NEWS: سوریه ۵۰ تن اورانیوم دارد. هرچند این ماده غنی‌سازی نشده است، اما مقدار آن به عنوان «بسیار بزرگ» توصیف شده است.
🔴
سوریه اعلام کرده است که این ماده و برنامه هسته‌ای آن تحت نظارت آژانس بین‌المللی انرژی اتمی قرار خواهد گرفت، اما همچنان در دست‌های سوریه باقی خواهد ماند.
🔴
دمشق اکنون در راستای نزدیک‌سازی مجدد خود با آژانس بین‌المللی انرژی اتمی، برای دستیابی به یک برنامه هسته‌ای مدنی، مشابه برنامه‌هایی که ترکیه، مصر، عربستان سعودی و امارات متحده عربی دارند، فشار می‌آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142489" target="_blank">📅 20:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIZ8P_RJEmCjM4Yhw5pEtLbcBFUJlQAoir7HczvUHel-YGSUlDr5FEWGuEP4sSUlMA0eJ3dH_8_-xgJUXePtPGRBjbz-M_UtRRUdSq9CFyF1eUbLAR86Cc24ZiFW1V1rPz-Q1G3MC4q50kl2xWX4B-YtMOQen2YIxbOyIOxNf7pswjqfkeBN0_aYwlYn1R5vkGbMgxnD4bAYOKKBCJKTGe5ckhGwNKIOcNXFFb33NGnH3XjePStd_V_pIHEUjgTosDeExQ2ed_KskPd2k9qtY2lB_xAT1NyybxxYMQKrSivS1ChnfdhbyiFKIY9lKzsq8R9agHTwW-y4X2fNofOoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: منتظر معجزه دلقک‌هایی مثل هگست و بسنت نباشید!
🔴
با تشدید فشار نمی‌توانید از بحران بیرون بروید یا از ایران امتیاز بگیرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142488" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d0d407f6.mp4?token=tlYk-r511aqRqhxfiuI5M3lUMlaCdKlreJiNcyo0sf2wIvUFyBzvDl2W8yN8dMhJmbOIYWfTenqUkBQ7bihGGAwlKiydwzR3s6MnU4rZH0NwAYqU_BX-wMzGRlDcuYXOmzXHFXQ3EfSeP2Ndf9WFPHiO9lzIOp-cBVKObiIeXQjr2EYqw28LNdHYm_T3YEs3EO6hhM-ZcybH7v5qAoX_fUETAHSvkjx_7Rh_RtW_VkBC1z1GdkJCDLAbXdYrmzoRL62m5tj0OolHSxb8y7pRKokIHjJcetJ-OGRMFgOFi4Rq9p84zdHKZydz6P9nHwBxo9md5hn0vILFyy3mrkYxJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d0d407f6.mp4?token=tlYk-r511aqRqhxfiuI5M3lUMlaCdKlreJiNcyo0sf2wIvUFyBzvDl2W8yN8dMhJmbOIYWfTenqUkBQ7bihGGAwlKiydwzR3s6MnU4rZH0NwAYqU_BX-wMzGRlDcuYXOmzXHFXQ3EfSeP2Ndf9WFPHiO9lzIOp-cBVKObiIeXQjr2EYqw28LNdHYm_T3YEs3EO6hhM-ZcybH7v5qAoX_fUETAHSvkjx_7Rh_RtW_VkBC1z1GdkJCDLAbXdYrmzoRL62m5tj0OolHSxb8y7pRKokIHjJcetJ-OGRMFgOFi4Rq9p84zdHKZydz6P9nHwBxo9md5hn0vILFyy3mrkYxJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه درباره عملکرد دو ساله
:
رئیس‌جمهور با یک تماس تلفنی با الهام علی‌اف، فصل جدیدی در روابط ایران و آذربایجان رقم زد‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142487" target="_blank">📅 20:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf67e20826.mp4?token=oBckfP9hR5NLhEjyFVom8Gex-_rAZcYuq0OLqxW4wqV7273JsW--fl1e7W72hViZhOlv3CFk154NXUV7PXqLcdySZeM0M24fBfkTg9Mrf8UfccoBsIMD9zyQjcwBFmqdriAUR2azVJfcLwdQcajgUqKPSMEolKSn0etdM5P87lpdYY9bcBklJypJRUgWVNM2Q9PxPwcxFZ37cG8EyW7pmlyun_2KxNUNAC7N3MhbI01ERrugiOplBMVKiBycjC7DjKKmT8JOViGogUmXaPaBOrEeDR216dcyLR4Mqkl_QKAq68k6l4xfIIOvdhcoCNlcmKomCQteIjCHiSTpTWOuxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf67e20826.mp4?token=oBckfP9hR5NLhEjyFVom8Gex-_rAZcYuq0OLqxW4wqV7273JsW--fl1e7W72hViZhOlv3CFk154NXUV7PXqLcdySZeM0M24fBfkTg9Mrf8UfccoBsIMD9zyQjcwBFmqdriAUR2azVJfcLwdQcajgUqKPSMEolKSn0etdM5P87lpdYY9bcBklJypJRUgWVNM2Q9PxPwcxFZ37cG8EyW7pmlyun_2KxNUNAC7N3MhbI01ERrugiOplBMVKiBycjC7DjKKmT8JOViGogUmXaPaBOrEeDR216dcyLR4Mqkl_QKAq68k6l4xfIIOvdhcoCNlcmKomCQteIjCHiSTpTWOuxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه درباره عملکرد دو ساله: دیپلماسی استانی مکمل دیپلماسی همسایگی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142486" target="_blank">📅 20:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نیویورک‌تایمز گزارش داده عربستان سعودی و امارات قصد دارند حجم ذخایر نفتی خود در بنادر ینبع و کره‌جنوبی را به‌طور چشمگیری افزایش دهند.
🔴
هدف، کاهش آسیب‌پذیری ذخایر و صادرات نفت در برابر درگیری‌های احتمالی در منطقه خلیج فارس است؛ یعنی بخشی از نفت، پیشاپیش به نقاطی منتقل شود که کمتر به امنیت تنگه هرمز وابسته‌اند.
🔴
کشورهای نفتی منطقه ظاهراً دیگر فقط برای بحران برنامه نمی‌ریزند؛ برای مختل‌شدن هرمز هم آماده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/142485" target="_blank">📅 20:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMaKDGgxmL5SgL_PgwWL1FBDyvjjvzDQThutLOnRL9Cn4lr-zdK3KlGv64SOS_ZWSswT-EHf1gJSDrlqORSbl1MUu1bo3MJx4F72AJ5Y8f198k9d6hvfxnYp9n4BHx5LfbHauYTCktaRm9Ql4bOEqDIpa73k_1WujOwNU3Pn6GGDnFFZdIw3KEhuWHdAglgTHnYrh68-Zaiyv2g6L2KLzyvgME1LA5w9oYJnSfFHlXH4L84q00geFBGK570Cibf-WSoIb1FaBhmDyYSkD2YhkCMm-I3NRA-0hG7YQq93wUiS710CQsaWcatXgfhAHUjtpjSCPVxDaAHknFVrqbvJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‌ وزارت دفاع امارات مدعی شد موشک‌هایی که ساعتی پیش به‌سوی این کشور شلیک شده ازسوی ایران بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/142484" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6ABYFurWa67YH_29p8qnAUD7j-zqr7f2fJ8rlwrb3RNIaFRScPWczvEAVIcfYZIuH5M8JuilL1U8i9OR4hEAAHjk7lcvSPgy75WeMlTQopk8spuv-LdeLojOGgDzSAvzMmCRUpWaF1Y4pHX3J5fXgwAxxAV9G5aAA5Jngtm7evdTUGYhqR2rySBaAwtTNOjGF30Xj-VAeGriSbbTPVGfDW5SZ01AZi67FfK3eIKpDOLzdVuWMt7rR19Q-9NUcd4xiY_Z5i9u77MtIIFm3owpcQ1uOuhcAR__MmbZUl9Jo9AdrSfDhItiUc5BEEYGxMyCN9XB5GTncr2wTfQIetcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت جنگ آمریکا با انتشار این عکس از ترامپ نوشت: «ما پیروز خواهیم شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142483" target="_blank">📅 20:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef9b951a73.mp4?token=hjrDHhGCodGsp6Qc_VIK7uNzw48g7vcqgaMg8vbzlN9C4ROLsFfdWJ7GfoL89rsdCbIOPB-mVCZuMgHhDW6TWJELA0GSMWMf9Lrr0uxBmpdnvKVlUvPn8WcFN9oqliGynixcHDVyxM30Ku7_nNZjhLIMQziEAkWmJtX2emytSItxLKrVnnSb9H-XHn3-ho5baADbwVKaRLwZ84DR4CfEPLBhFLNSC_jmzJkS-jOxJEgqS1Iyw1n2vatfhekbx651D24o8NXq06sNv0jujD7ukAVNTx7RIU4XCxZIq29YpOb8eTv2CqsKE8UJ8Azi4xKfBypbev5ecMnpf_Imn26Hjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef9b951a73.mp4?token=hjrDHhGCodGsp6Qc_VIK7uNzw48g7vcqgaMg8vbzlN9C4ROLsFfdWJ7GfoL89rsdCbIOPB-mVCZuMgHhDW6TWJELA0GSMWMf9Lrr0uxBmpdnvKVlUvPn8WcFN9oqliGynixcHDVyxM30Ku7_nNZjhLIMQziEAkWmJtX2emytSItxLKrVnnSb9H-XHn3-ho5baADbwVKaRLwZ84DR4CfEPLBhFLNSC_jmzJkS-jOxJEgqS1Iyw1n2vatfhekbx651D24o8NXq06sNv0jujD7ukAVNTx7RIU4XCxZIq29YpOb8eTv2CqsKE8UJ8Azi4xKfBypbev5ecMnpf_Imn26Hjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
قالیباف: ۲ موضوع کالابرگ و بحث نیروهای مسلح، موضوعات مهم و فوری ماست و باید به نحوی پیگیری کنیم که خدشه به آن‌ها وارد نشود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142482" target="_blank">📅 20:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd37dea02.mp4?token=XEg4YDJqF7kIvUcj_PReiS4jvCXAZhgGE1ZJqime6FggLtkCX3JbRbfJHXei3pfNM1XuxWT2gx_BkA1nc714TBUST6NkMYbB3mByZNoqJlHxHG07Ai3dLIHa6Qs9DCn_0bRVc_Wx-IULnqpP_CqkYlIPoYda7XHcH5fV41u5lFSfYC4mIreOro7J2xNKN9UPdG4jAkA_7EjVyo5aK4Z8lOx1hBCdIZDWYU4ZKp-0iS34ujRxY7FPNlqhSmSKwTLtgeSRINg6ENkWwb_NXdcLo_--xBJWQn6REOoHoNTTrMhpruyL6cflHm_iP0Ne9bvhryH_pdnHXolZvWFKfUdhPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd37dea02.mp4?token=XEg4YDJqF7kIvUcj_PReiS4jvCXAZhgGE1ZJqime6FggLtkCX3JbRbfJHXei3pfNM1XuxWT2gx_BkA1nc714TBUST6NkMYbB3mByZNoqJlHxHG07Ai3dLIHa6Qs9DCn_0bRVc_Wx-IULnqpP_CqkYlIPoYda7XHcH5fV41u5lFSfYC4mIreOro7J2xNKN9UPdG4jAkA_7EjVyo5aK4Z8lOx1hBCdIZDWYU4ZKp-0iS34ujRxY7FPNlqhSmSKwTLtgeSRINg6ENkWwb_NXdcLo_--xBJWQn6REOoHoNTTrMhpruyL6cflHm_iP0Ne9bvhryH_pdnHXolZvWFKfUdhPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
:
اطلاعات خوب و دقیقی نسبت به تراستی‌ها داریم و باید در این موضوع نظم حاکم کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142481" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره: ترامپ از تیم خود خواست تا زمانی که ایران آماده دستیابی به توافق نشده؛ وارد مذاکره با این کشور نشوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142480" target="_blank">📅 20:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ارتش اسرائیل از حمله هوایی و ترور 4 فرمانده ارشد حماس در شمال غزه خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142479" target="_blank">📅 20:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142478">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3983b3aa.mp4?token=nss_hF0NcKFenbVjpiZjFHslPEQagcazlhuWbIuHJSkJX0dnfEoWUr5EeMO6bpZ1j5Q5Ev-_UKHNj6cfojE726JOgyYv6uRqXCc49UFAtfvXSkpELOIkXUCXfG5WGkOM8I9rQ2sNiTLqPUiL64c4D2LM2NeKDhgi94JKzdhtSWefXrMdj2hT5OyCdQ_VtxOY4gvitsFLWm2yT-IAYmaDG-JFoyE5WAFN8jcRMPV7W-AcfbNmRCtYJyYTn_fbPML1fQ0WP0OloHii_kK_8rZoOAwIRFaYoU380j1ycchv7u_N96lMfL-RcsX2db3_uSBZAWEmjmgRap1tb95lvIZGMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3983b3aa.mp4?token=nss_hF0NcKFenbVjpiZjFHslPEQagcazlhuWbIuHJSkJX0dnfEoWUr5EeMO6bpZ1j5Q5Ev-_UKHNj6cfojE726JOgyYv6uRqXCc49UFAtfvXSkpELOIkXUCXfG5WGkOM8I9rQ2sNiTLqPUiL64c4D2LM2NeKDhgi94JKzdhtSWefXrMdj2hT5OyCdQ_VtxOY4gvitsFLWm2yT-IAYmaDG-JFoyE5WAFN8jcRMPV7W-AcfbNmRCtYJyYTn_fbPML1fQ0WP0OloHii_kK_8rZoOAwIRFaYoU380j1ycchv7u_N96lMfL-RcsX2db3_uSBZAWEmjmgRap1tb95lvIZGMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
:
از ظرفیت‌های خزانه و تنخواه باید به‌درستی استفاده کنیم؛ اطلاعات خوب و دقیقی نسبت به تراستی‌ها داریم و باید در این موضوع نظم حاکم کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142478" target="_blank">📅 20:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142475">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6c137ae8.mp4?token=k4VACZ2PtgkBotypdQi_5qlJRL5MdB2lfKgsgER4cYLVBfJA0lynHClmZZFBbZs7Vj5CxBWIPmohN1u-Oo99pgKqfLvjZ9MxpgSs6fy2xAOmAHfhJ1ntCk0XGe0RQDGNVtvI77fm3Vhyiqd7i8SJwJjoOs2Tx5NhMDH_4qFFtx-iUc5QG8NosZRDBQhvvTvDC3UiBx3llrhR8F7zQu-1lKe5gQYV-BI0x3-m067p3F1c_IkNSnFQvbeMV_SqTYzlxon-E57T66LBLiFXQyF5bt1vOlxrSqfW_ainIoFyKCG6f8T03CT0FywakgRYq7Yk5B7RjPLEVwlRJDX4TALfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6c137ae8.mp4?token=k4VACZ2PtgkBotypdQi_5qlJRL5MdB2lfKgsgER4cYLVBfJA0lynHClmZZFBbZs7Vj5CxBWIPmohN1u-Oo99pgKqfLvjZ9MxpgSs6fy2xAOmAHfhJ1ntCk0XGe0RQDGNVtvI77fm3Vhyiqd7i8SJwJjoOs2Tx5NhMDH_4qFFtx-iUc5QG8NosZRDBQhvvTvDC3UiBx3llrhR8F7zQu-1lKe5gQYV-BI0x3-m067p3F1c_IkNSnFQvbeMV_SqTYzlxon-E57T66LBLiFXQyF5bt1vOlxrSqfW_ainIoFyKCG6f8T03CT0FywakgRYq7Yk5B7RjPLEVwlRJDX4TALfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون‌های دود با منشا نامشخص در سلیمانیه واقع در کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142475" target="_blank">📅 19:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142474">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
الجزیره به نقل از یک مقام آمریکایی:
در اظهارات دولت آمریکا درباره مذاکرات با ایران هیچ تناقضی وجود ندارد.
🔴
مذاکرات مثبتی با ایران انجام شده است، اما ترامپ تصمیم گرفته است فعلاً منتظر بماند.
🔴
ترامپ از تیم خود خواسته است تا زمانی که ایران برای دستیابی به توافق آمادگی نداشته باشد، وارد مذاکرات با ایران نشوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/142474" target="_blank">📅 19:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142473">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cudxTKxta7ujCxbgKcYQFQTnXTolOfMGS6U9XJMny3CMAEtpq3NoCWaod0vBkprDIww3R9lstdnpguQ6EjEBHqijr9fiYithSJlK-x0i0bsMDLVGy2hsyT5UMLcaVXXSSLUTlzkDgnJEGz2HTQcmZgFFhJSyH2aFoVoAi3nAhQ0u6ygrSgHaOLr09uMZUFGW3Hv94lLLKFksQD25Zmbl8MAPYwV8Rei7GlNYibLzvVjdPlWe3sIvOvtEzm9C8dOrm-UBA5pzk0C88N0_NwPdHi9NkL7f2MAaS2BbJbawHEd44Bmk4gAmFzNXqvD3b64lyAky0UOc0ha1-lJS1aG7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع پاکستانی:
پنجره مذاکره بین ایران و آمریکا همچنان باز است اما فاصله بین گفت‌گو ها در حال طولانی شدن است. اگر شرایط همینطور پیش برود، جنگ بین این دو کشور قریب‌الوقوع هست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/142473" target="_blank">📅 19:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142472">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA-RsCaTwARFNQEa4m7VOxSr-ViYAYbm4R8d0ZfBYI8TuJr1JUCzBLXmjkrpmXZwz7NJ57_swF1IidThltV9b4XwdbKQZu7cW3koxuvWIaDSv6YrSqnrNrhOcDfWYmJjSwm-b0hxQ_WJ14m6JBu8XfjI8MLwNZsyRDyRxNd_n_yYTDOXQhznvsHuHG5R8bGPAEsnHvvqCMgkQyBLIPZ8EXd4BviySkn8fKOR0uUa4-TvJzqXH0uz_pfz1wfuSzihbptzAAxSE7CWyRJ2JVMmJJxFzyqqWv1aK9OVfTHr7sKPCWdrF_nAmfv2EZGc60fO6lXXjJh1C90mjqtyWWqAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست
: پنتاگون در حال بررسی کاهش حضور نظامی خود در خلیج فارس پس از جنگ با جمهوری اسلامی ایران است، زیرا حملات سپاه پاسداران آسیب‌پذیری‌های پایگاه‌های اصلی ایالات متحده را آشکار کرد.
گزینه‌ها شامل جابجایی نیروها به سمت غرب به سوی اردن، اسرائیل یا عربستان سعودی به جای بازسازی تأسیسات آسیب‌دیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/142472" target="_blank">📅 18:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142471">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/انفجار در جبل علی
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/142471" target="_blank">📅 18:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142470">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری/انفجار در جبل علی
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/142470" target="_blank">📅 18:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142469">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
آژیر حمله موشکی در دوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/142469" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142468">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtDoRd7g3Me-Bt0C0Ze6q-9S1lenQ7l_q9ErrmkMBxSSPwY_g314AXTo4c6MAElMgf2kFJ_fEo7Cawu0gUfNTKZdphqxtDzYrHCCtJm_kdpy3oiEsC9dQ2ohLQuSkg5odjh_2JlVP745FS_L3JUatAZDyR5hJ1iViE_XTsinsWxxAo23CqrQT9dVnrj4uaDApJOBZv5kWehhPTh8p6w9tp8glSasdtd_DcX7bdgVvBsYH-zuZO3ePW36MvW4TQs0B7taiFUce4k0toLrgDpz9Qi0vE6GQ3uhynWLgpgHpmc1l-8SrmqjEHcxcJ1BLIkBSln1dIS7e5jLDmKj_xyPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار حمله موشکی در امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/142468" target="_blank">📅 18:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142467">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c196185a6e.mp4?token=eqebSFdiDfkLGvh8gPNwnp4bwUVDX2LF1sE1xPnsR02jBscRFo1eJu7_bhEY_8lIagF7dve-VJygrafDf1m4-TU9BjTYWXMeV5o6clk1FhPvtxFu7lCnzYaQzmpQJud25Cy0Arsxq98oPiIp2yc3Zi3oy0bTnq1gXJW61R9LJekTY2jqhBVAfCOuTRSdydBfS1H0JqrTZ9oWJqEnlDNL47V1BQr3xQbnfycxHfvvKAGey5S7Q6IRxXAPrC7ly2tt-_rwq-J8wyzI2cg0JT6yqW7GxSKkmK9FxwJayTmGKGiPUnp1bRzoh1oz8h39-VZqALcqyGKygFYlWl9JWFt6Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c196185a6e.mp4?token=eqebSFdiDfkLGvh8gPNwnp4bwUVDX2LF1sE1xPnsR02jBscRFo1eJu7_bhEY_8lIagF7dve-VJygrafDf1m4-TU9BjTYWXMeV5o6clk1FhPvtxFu7lCnzYaQzmpQJud25Cy0Arsxq98oPiIp2yc3Zi3oy0bTnq1gXJW61R9LJekTY2jqhBVAfCOuTRSdydBfS1H0JqrTZ9oWJqEnlDNL47V1BQr3xQbnfycxHfvvKAGey5S7Q6IRxXAPrC7ly2tt-_rwq-J8wyzI2cg0JT6yqW7GxSKkmK9FxwJayTmGKGiPUnp1bRzoh1oz8h39-VZqALcqyGKygFYlWl9JWFt6Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اميرحسين اصلانیان، بازیکن سابق پرسپولیس:
علی پروین واسه همه بازیکن‌ها "پرستو" می‌فرستاد تا از همشون آتو داشته باشه
😐
@AloSport</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/142467" target="_blank">📅 18:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142466">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc91c4a70.mp4?token=uBocBSjeJ-a3FuPDWkd4nCsN4BBYnYdnGYUmUIlZYi3ZrRSK34tVxei5EvsH5kDR4cZ6_wUTkITXFZROQeFa__xscsXNIIO5XGkEQi2SXXHJGtLXfndQ1J7CZnYxy7EVTMOzIK63cB34Pi4gEQlKzw3lELPCOq2BzCTE1Jm-vmHHdO2E1GKTyrO2fwxfF06-QKtSxKwOfAXZW7JZFZOd9xvrxPRenGAQItJxIYb5C9N3yXgo-26DWf58J9FkPaNF7voXnn5dl-KlsGzp4gcbxDVVGySzyGn5fxAznQjdLwmgLtO7tdRmSBJA5rT9RK8MwDjk4NwjsbUwSox-u5JxnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc91c4a70.mp4?token=uBocBSjeJ-a3FuPDWkd4nCsN4BBYnYdnGYUmUIlZYi3ZrRSK34tVxei5EvsH5kDR4cZ6_wUTkITXFZROQeFa__xscsXNIIO5XGkEQi2SXXHJGtLXfndQ1J7CZnYxy7EVTMOzIK63cB34Pi4gEQlKzw3lELPCOq2BzCTE1Jm-vmHHdO2E1GKTyrO2fwxfF06-QKtSxKwOfAXZW7JZFZOd9xvrxPRenGAQItJxIYb5C9N3yXgo-26DWf58J9FkPaNF7voXnn5dl-KlsGzp4gcbxDVVGySzyGn5fxAznQjdLwmgLtO7tdRmSBJA5rT9RK8MwDjk4NwjsbUwSox-u5JxnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو کنسرت الیسار زکریا خوری خواننده لبنانی یه نفر پرچم ایران رو بهش داد اما این خواننده اونو مچاله کرد و پرت کرد اونور
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/142466" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142465">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwhBckB1T-yJuMQQQBbbJxsqs_s0sTxxueKVfjn360t3xlmaiPyWStcjKD1qw8nX6Jqdi94XAAqtwrrxht5h_isi03zK86PiJ0UQuu3Wdg1qhAQpQYiKKwdXb-MW3iGlYhOtya2-KcNqEa0hkpAtEdi8bgfHfJBSmuA9du_GV--OK-xLdlwuwKjl8pxrw_UucFtiw3VQikPXiqqRfOagDWliu_qEdqDaENj5X9yVZ885l2OjM_l7RAlOOLf4SRwatZ6qrI2SN13Y13v2kC0V7LWDSJJtKqJgFvLtmUrXyCtjjSzZq8kxmC1CnwZkaQNOHvuJq_27xZTEoBMLMchfHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا
:
یک کشتی باری که در حال عبور از تنگه هرمز بود، مورد اصابت یک پرتابه نامشخص قرار گرفت. این حادثه باعث آسیب به قسمت سمت راست کشتی شد و همچنین منجر به زخمی شدن یکی از اعضای خدمه گردید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142465" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142464">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/142464" target="_blank">📅 18:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1wiw64zKqE0g14qHeCnxabyts-YYiuHPRf5wheKJp9oNNuYMABT9dkZcbQj1FgizuU09L-o95JXjZQjxOekdjNDGX2vKv950D-aBMTHi4pan_IJnckxK8x16WXDWdua_YHdC5dvti0-KlQwtqswSNsvRR1D0IFOvu2CinbmLRbC0TGooF-sTb4YRdtfROjkFUB9b-NV3YG8GcgmCdrAqO5DIZbMbqS4jR-qXQSmtojO6AXJtddsp0sTwhG6TLz62J3a61gneWXePv_IZjJU-1CHJMiMK_0yLsCBxMwbLCdxtxB8OBYcd7i-IW1TV-R8g42nmln88LBxZSGfA_Q2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پدر، پسر معلولش رو زنده‌زنده آتیش زد
🔴
اوایل امسال مرگ یک پسر 18 ساله در آتش‌سوزی به پلیس گزارش شد. خانواده مدعی بودن پسرشون خودش رو آتیش زده، اما پزشکی قانونی بعد از چند ماه اعلام کرد سوختگی‌ها احتمالاً عمدی بوده.
تحقیقات از همسایه‌ها هم نشون داد پدر و پسر رابطه خوبی نداشتن و پدر بارها پسرش رو کتک می‌زده.
🔴
در نهایت پدر بازداشت شد و در جریان تحقیقات به آتش زدن پسرش اعتراف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/142462" target="_blank">📅 17:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دومین مراسم چهلم آیت الله خامنه‌ای دقایقی قبل آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/142461" target="_blank">📅 17:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142460">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دنبال وامی
⁉️
بیا اینجا شرایط بخون
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/142460" target="_blank">📅 17:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142459">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpwTN1va7KFzuKnyi-JIZAF7uqQ6vuMD-uid3m5WL8kJ8XAjl7sjFfquzhqMWdHKuX3D2x6nDg-JvLMtlv2M1dvx2y_D5CfaA0ZaCEU65JfJD4pwE1Po66-DCrzUMehc56NMCRaftb1bdMpmHyHQvaawISCzbhG8fl5MS5Sr-igIKHXX3U4TraowhJNLf4rdmp_gQlYL9q23-DFsp2nw_bbBbRuapEHsK1lqL6JM-bxJAUitxyjzBt6O3Kftxo8mhPYTGWDR9bijkAzJUTHkek-gkQHR8bsxzh0IsYlEP5lh74ST53EmF5U4gBQdGa-DpaD3VxTBzd_lYzUibnGvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
لیندسی همین چند هفته پیش داشت خوش می‌گذراند! کلاهش را ببین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/142459" target="_blank">📅 17:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvZnNPKslpd73sBLJBzs2uvhonVe5V_Q4LnJ2oyfFamquECPwucIpaurQ5-cZQTlIDO4Nqb1ERrSgW4s6QOdhu1fuoZiOvJmBqXNMmRQU-vPPdlUtPsPKkEtDwHuOi-4ZYogzy20JjGf5HbbF_7dmAdOwNpd2XLl1rYCOOJwOdXa3dU25p_EQpJTHj5IYYOHnbh6wBzpp09HccNBzmqkhnjHB0mZX0irloWF0HAlP2boDiyMLm_b6xmhGlsOSMitzR109ULWyWrschAhzLo-q3xKYQ7PcJstLvlt2ON-fH5nUhC-ngrEL6uN4l-056M3XLcdpVoLcIj42Ovtt9scWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داریوش، خواننده مطرح: اپوزیسیون سلطنت طلب بارها شکست خورده اما هربار به جای پذیرش آن به افراد مختلف فحاشی میکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/142458" target="_blank">📅 17:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142457">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlMq8epLAr2o6N5rbe_DT4MHiT4SG8WZQF9hV7xK4vhfgACMoHnDUfxL_gKxiWOvEdHUuCjhqL2Vv0JIB4i1Q2JVpscfv1EyBmt7wkTFcIAnZ5APxuv1cHwIupj9Ye9UY8HCQORDKFaVgzpBQFercJgVvxXsBjrQSh3N-dp1enQK6vkOoVOtf3g8gB5p7E-sGXncCvWEm8CcJOVlXTeZUjkszpkXe9gFe7mInt6YnjRYGbv0eQ5DagfQ7RYm_fIdWEBEQGdSWC8W486uha02fWJLHlmXECPnALe6_0_nrqeOs3D0W82G9o1IYH1xgEAQf5YCUB4bCayqbMmbm-WlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ترامپ در تروث سوشال:
‏هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است. محاصره دریایی همچنان با تمام قدرت برقرار است. تنگه هرمز باز و در حال فعالیت است. همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند. از توجه شما به این موضوع متشکرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/142457" target="_blank">📅 17:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142456">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a9aac2d.mp4?token=Y4mBc4H3HXiQtzXM80eIsL_OXY8EJ6hPPKMbFF0wjDRy8aDEaGLiFCd-oxmA8hWRc68gGkwhQjAKj599M6Q1QQIpfUM4OSw1pmt2hPHnka-L7OTh2D1zBPtBJkv9_N3uTDkhqrGbYgiI8FQ8iGHclBLQ4a_JxCMDXOoJxXhjeg25LI2xHXbIQJN8wAeCOwTWqENfgbbuAZUnKqWGanO7lsIu838bfUtbteuU8VCAwZoWH9p_SKWHJkOXEFIUMeOOF7dZguneJaTPkIBZeKUhwR_Ft4ORDiZIYT2tpWdv4LYdjMpa7uE1tgJtw-m28CiPKC9JYPoJMX2xsLcnRwCOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a9aac2d.mp4?token=Y4mBc4H3HXiQtzXM80eIsL_OXY8EJ6hPPKMbFF0wjDRy8aDEaGLiFCd-oxmA8hWRc68gGkwhQjAKj599M6Q1QQIpfUM4OSw1pmt2hPHnka-L7OTh2D1zBPtBJkv9_N3uTDkhqrGbYgiI8FQ8iGHclBLQ4a_JxCMDXOoJxXhjeg25LI2xHXbIQJN8wAeCOwTWqENfgbbuAZUnKqWGanO7lsIu838bfUtbteuU8VCAwZoWH9p_SKWHJkOXEFIUMeOOF7dZguneJaTPkIBZeKUhwR_Ft4ORDiZIYT2tpWdv4LYdjMpa7uE1tgJtw-m28CiPKC9JYPoJMX2xsLcnRwCOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های ارتش اسرائیل بار ديگر فرودگاه ابوالظهور را در حومه شرقی استان ادلب سوریه بمباران کردند.
🔴
این فرودگاه محل استقرار تجهیزات ترکیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/142456" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUt1coZyM0YrHDg7rsDV-6BZyjJ2QEv4vREVSpKnXy7jFwNbW_Y5mN4DJOtyDMhAahhBpcph4b_4DEpkCfKORlzbk-XD69TgkTwL_xhhAhN8iWK0G_fU0TPPJmFrW0N9r0Bf8zqhiPSglByJ_8mJ_vF3uIQHTKuXwSyll40CY3JN7Sq9rqbP3dOe-4yx7U1_1PyRVjB0f_HIBhCF1PiogJzaInbrwuEPi7IhKRDGnkiG9eCL3e9_RKo1lhHN-XiesspMTP5LgXaHsADe7sZrWCi5jqhslbbskFUFyfhov4FtfT7Jy4JbQMYAdcjz9YsxlfFYU3rAJIByymZxO9Ylyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار نقدی:
بعد فتح اسرائیل، کلاهک‌هاشون رو برمیداریم و سر اونا با غرب مذاکره میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/142455" target="_blank">📅 17:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwaZEb4zPdjblQrHkXv0RbAUBOsOEkWHda4IPX-xQ64XBwAwB3fzXj6tH-Gi3-vlEmNx2EepwLq7clopugrxkwzAS0MzSfs-xGetdBcFbqljwmBnkGmtLOguEgq7Woh2mKpkwwvv2Rgj_Ix-UEEWI0YjUv-uc7HvD8IuGMU5NtZqQ9kAqwzsD_DANfs1tU15Sd3A8VFYWMjBgZS96OFY661zLprAYnd8lPpu8lypkZbmYmWYknRc2svVOxLKeHAqnsffIQXkC35M5mDDAn0Roe6qcpiYTh9WOwkmqggqGzxLKDNFGdVIZzDSIsUUuK_Kbgc4dQeKFXfiWU7McAu1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش نرخ ۸۲ قلم دارو و رشد ۱۲۰ درصدی میانگین قیمت آنتی‌بیوتیک‌ها
!
🔴
در میان اقلام مشمول افزایش قیمت، قرص دنپزیل با افزایش نرخ حدود ۵۴۳ درصدی در صدر قرار دارد. همچنین نرخ کلاریترومایسین حدود ۳۰۸ درصد افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/142454" target="_blank">📅 16:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=Kmf6DSmkQKYXWM-L170ibHFPprKX3MW2onzAYbiWytI43dcCOzXSDxPJDatdOjTU0XJo_se49cDmyoyI6LQwF3Yu1ODvtrksLGa_2gaXMY9LgfqpH1KNfQSpYjv39LglOGuHKUqVzzRwLfJcO8akM0_rVIHfjC-G96MWo_JkxgU7LzqF7_33WqmY8Dnlktck_j8qIKjcCghzVJYsEsScl-SEMTjXwewSQpKAy4xOHooijpPvrcCi90XJaJahG0zh6j6TVpjDUNmprRwkR2Hb6rawvmyDw4xWjt_Aw9Ak2oR2zSHJm7uh5eL6FLt5-JvCG2NShbZXfaHiJBvMfDag5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=Kmf6DSmkQKYXWM-L170ibHFPprKX3MW2onzAYbiWytI43dcCOzXSDxPJDatdOjTU0XJo_se49cDmyoyI6LQwF3Yu1ODvtrksLGa_2gaXMY9LgfqpH1KNfQSpYjv39LglOGuHKUqVzzRwLfJcO8akM0_rVIHfjC-G96MWo_JkxgU7LzqF7_33WqmY8Dnlktck_j8qIKjcCghzVJYsEsScl-SEMTjXwewSQpKAy4xOHooijpPvrcCi90XJaJahG0zh6j6TVpjDUNmprRwkR2Hb6rawvmyDw4xWjt_Aw9Ak2oR2zSHJm7uh5eL6FLt5-JvCG2NShbZXfaHiJBvMfDag5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنسیس مدل 2013 در امارات متحده عربی: ۵۰۰ میلیون تومن:
🔴
ارزان تر از پراید در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142453" target="_blank">📅 16:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142452">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f99d209784.mp4?token=NjxCklvy2OwZQJFDR0TqcBcN3x3QeuTqHrWPqtctbAkUVQjmSeSgD6a3Jz9wDCeyhr9E0vWlYRmwMpC8lUNQ98tV-aPf7w1idBVHpnlZpvtzHBCJof_j3CnJpYTUkAwIYso9YdTfXiVZQE--f2MlgTdaT_gi13P-67H38H4DdnkA9inZw3DiNgDCmglN9-FlMCu-w5MXpfKvb4WQwoydTaRfSAlXtDitzUcG5oxGDMxvBnSDBw_-LbytwKqk0uwzP0iPq2xxKVMAEcRsFoZmOEbkTdU_cb05RGT4_CbMUWmYxB3EQxSNB96RjyAjScRFU2EGkZsHjEqYhutKufQCHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f99d209784.mp4?token=NjxCklvy2OwZQJFDR0TqcBcN3x3QeuTqHrWPqtctbAkUVQjmSeSgD6a3Jz9wDCeyhr9E0vWlYRmwMpC8lUNQ98tV-aPf7w1idBVHpnlZpvtzHBCJof_j3CnJpYTUkAwIYso9YdTfXiVZQE--f2MlgTdaT_gi13P-67H38H4DdnkA9inZw3DiNgDCmglN9-FlMCu-w5MXpfKvb4WQwoydTaRfSAlXtDitzUcG5oxGDMxvBnSDBw_-LbytwKqk0uwzP0iPq2xxKVMAEcRsFoZmOEbkTdU_cb05RGT4_CbMUWmYxB3EQxSNB96RjyAjScRFU2EGkZsHjEqYhutKufQCHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تلف شدن ماهی‌ها پس از قطع برق در بابل
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/142452" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
طبق گزارش خبرگزاری رسمی سوریه (سانا)، سه نفر در انفجاری که در نیروگاه برق حرارتی شهر بانیاس، واقع در سواحل سوریه، رخ داد، کشته شدند.
🔴
مقامات در حال بررسی علت این حادثه هستند، در حالی که خود نیروگاه همچنان در حال فعالیت است و از این انفجار آسیبی ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/142451" target="_blank">📅 16:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142450">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4tZMXBE-FCkdwL31AjWa5VDApL8RniFFNFXFS0KrPZ5lYGer1-IitbOnXwbbzPmSEPSXZdTGgoOMtQHHr5orWvBoGoHnSLyt3MKbZmSMqOq4wbDRbdx56-xawIE4tvKfJPvcp1Uubv8BF9tHCQd6ByCwLBUj8JRHuDXLpRweuSzrq6uZDpWUrp3BWsbG9GVgZe1hPwqo4qChe5r8OnZUwC4HC1wB5r9vCfI_Ut_cWb2rH5kKS9xOsM1gqPzwz6FmyuBUJBd2Pa-m-GiggeX6CWordRQFHMFMkeCk-2uOXjCGNmRXKHgEKMHRn5W4ALldZoN31Pfdcf19r6eSKhwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین احتمالاً با کانیه وست ملاقات می‌کند
🔴
معاون کمیته امور بین‌الملل دومای دولتی روسیه اعلام کرده است که ولادیمیر پوتین، رئیس‌جمهور روسیه، ممکن است با کانیه وست، خواننده و تهیه‌کننده معروف آمریکایی، دیدار کند. به گفته ژورووا، این دیدار منوط به هماهنگی زمانبندی دو طرف است و از نظر تئوری امکان‌پذیر است.
🔴
این خبر در حالی منتشر شده که کانیه وست در ماه‌های اخیر بارها از پوتین تمجید کرده و ادعا کرده که تحت تأثیر شخصیت او قرار گرفته است. همچنین او از جنگ روسیه و اوکراین به عنوان «جنگی که حقیقت پیروز می‌شود» یاد کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142450" target="_blank">📅 16:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142449">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
زاکانی: اقلام مصرفی مورد نیاز رو تا ۲۵ درصد ارزون میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/142449" target="_blank">📅 16:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142448">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du-0LGH-Tyt2BZRHwQKgK8Ky8DlhRVrwV0bxlZJLpT6GeK65wVh_Vn55ACO2GBLAygGNiNq3Ew9wS_zv7wA56mY1AhRdpwBJbhuKp-kdypil8Y6MVfimIFasfpNHXPVFMjJXMpZChMYJ4kfEkpQvsVrew8oxDTAzqreyvie_NnYHSV8x_uz8xiln8HJ1RKZEQPLTO_uECVvntqibDu_6fDCoyOa1ltRDSP2RcuQ-g2hEnyzJusaTWKXA5iuhajOV9qeoM1satBkJEZp3dNlBeMDDTq_0YcA-Ust26v9hoC9Z_5ft_vmqa3xeSFKeQplkJSTqZo77GF6fVZoxu9uafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حساب رسمی نیروی هوایی اوکراین درخواست کمک کرده است تا با موشک‌های پاتریوت برای دفاع هوایی تجهیز شوند.
🔴
همزمان، ترامپ نیز درخواست کمک کرده و از شرکت‌های تولیدکننده موشک‌ها خواسته است تا تولید را تسریع کنند، زیرا به دلیل مصرف موشک‌های دفاع هوایی در جنگ با ایران، کمبود این موشک‌ها احساس می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/142448" target="_blank">📅 16:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142447">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ویدیویی دیگر از باقر خرازی: آیت الله مجتبی خامنه‌ای اگر در این سه سال از دفتر رهبری طرد نمی‌شد، شهید می‌شد؛ مرحوم رئیسی هم قصد رهبری داشت شهیدش کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142447" target="_blank">📅 15:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142446">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
عراقچی: وقتی آمریکایی‌ها درخواست مذاکره را مطرح کردند، آقای پزشکیان معتقد بود باید به این درخواست‌ها توجه کرد و از همین طریق راهی را برای پایان جنگ پیدا کنیم.
🔴
از ۲۲ اسفند که اولین پیام‌ها آمد تا یادداشت تفاهم که ۲۵ خرداد امضا شد ما سه ماه مذاکره با فراز و نشیب‌های بسیار داشتیم
🔴
حامی اصلی ما در مسیر مذاکرات، آقای پزشکیان بود
🔴
انتخاب آقای قالیباف در تیم مذاکرات به‌پیشنهاد رئیس‌جمهور بود و حتی در صورت‌جلسه‌ای که تهیه شد پزشکیان اصرار داشت که «باید نام آقای قالیباف به‌عنوان مسئول مذاکرات نوشته شود تا من امضا کنم».
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/142446" target="_blank">📅 15:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142445">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
حملۀ دوباره جنگنده‌های اسرائیلی به فرودگاه نظامی ابوالظهور در سوریه
‏
🔴
منابع عربی از حملۀ مجدد جنگنده‌های اسرائیلی به فرودگاه نظامی ابوالظهور در ۷۰ کیلومتری مرز سوریه در استان ادلب خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/142445" target="_blank">📅 15:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
درحالی‌که هزینهٔ اجارهٔ نفتکش‌های غول‌پیکر در مسیر خلیج فارس به آسیا در شرایط عادی بین ۳۰ تا ۴۰ هزار دلار در روز بود، گزارش امروز بلومبرگ از ثبت رکورد تاریخی ۵۱۰ هزار دلاری حکایت دارد.
🔴
بلومبرگ دلیل این افزایش را نتیجهٔ مستقیم تشدید خطرات امنیتی ناشی از عبور از تنگهٔ هرمز اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/142444" target="_blank">📅 15:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142442">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8eb449cd.mp4?token=tfNiDeZJ31oazZxC7xct18IXqeLh0OIlDFv5a3A0j1G2Um51fcnPRcz0fCIO97-dgYjgq3P9TXHfJ1n26hdgmJX7CxIhpCScJoJdyTObTuqnPiy1mdN3piuQP8let91844reTn0-gxB_IS19a5oJHvXycMqQo8k8N1Mg61C8RZprv2RYW_ALC_hYGfeynrJP3lw1vm2W_JFFEUtEEz3hzEAf_WZDHkAmBjYCRmhbQvPqWvZSzye3DPNWaL43w6fqP5PPMXxRmpzbk62lun8em1-vbJjHTBOBhBetHnqhvIdfv7V1rvjYEo1HU4te8b7qQPPSAsOvLRoql0-qytUZjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8eb449cd.mp4?token=tfNiDeZJ31oazZxC7xct18IXqeLh0OIlDFv5a3A0j1G2Um51fcnPRcz0fCIO97-dgYjgq3P9TXHfJ1n26hdgmJX7CxIhpCScJoJdyTObTuqnPiy1mdN3piuQP8let91844reTn0-gxB_IS19a5oJHvXycMqQo8k8N1Mg61C8RZprv2RYW_ALC_hYGfeynrJP3lw1vm2W_JFFEUtEEz3hzEAf_WZDHkAmBjYCRmhbQvPqWvZSzye3DPNWaL43w6fqP5PPMXxRmpzbk62lun8em1-vbJjHTBOBhBetHnqhvIdfv7V1rvjYEo1HU4te8b7qQPPSAsOvLRoql0-qytUZjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست عجیبی که ترامپ منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/142442" target="_blank">📅 15:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142441">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ارتش آماده جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142441" target="_blank">📅 15:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142440">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
شرایط وام بدون ضامن تا سقف ۳۰۰میلیون
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/142440" target="_blank">📅 15:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLolKSNqarGn7Gu6FiuHaxZd1A563wJgVGhAgun5GoQgzfK7EbavFfC9zrrZxoPGYxBsHWMVFEQnPXH_JbN5vr70z2HPbomLf83nxzubNF6EWsGEW_QmgzpSM639oqnKNIL9zlYrip4zed-xcdQsXWP-mHW6a-q-VQuB5rT6YVOpTsnB_JcOEW67htPU_zLS1znwaaS72sNRwKaeJYFn7wj53rx-2vBSNdcwf2VvxrDQ9eLMXngt9YaRLet4UAsE3ezRHDVxZ2d2wzgv1r8_ee0Uok706IYHwd3JoBeRlhCKDVbA6_0rzV3R6kPb8rapl0uknwejeXYqpBIuBdEqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش معاون وزیر خارجه به توییت ترامپ: به‌زودی توهمش درخصوص تنگهٔ هرمز را هم اصلاح خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/142439" target="_blank">📅 15:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142438">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
خبرنگار الجزیره: در دوره زمانی ۶۰ روزه نه مذاکرات واقعی‌ای در کار بود و نه ازسرگیری جنگ تمام‌ عیار
🔴
خبرنگار الجزیره گفت: در دوره زمانی ۶۰ روزه که در یادداشت‌ تفاهم ایران و آمریکا آمده بود، نه مذاکرات واقعی‌ای در کار بود و نه ازسرگیری جنگ تمام‌ عیار؛ کمی پیام رد و بدل و موشک‌هایی شلیک شد منطقه اکنون رسماً در وضعیت «نه جنگ، نه صلح» قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142438" target="_blank">📅 15:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910d3b9d30.mp4?token=YtH17x7Er5vLSXMTsUHBIZ79ticsdKkZp0h10SquoUCW13ORTgKSnCSIdjORYooknEKsG85phAIF-SuBPCazYmX25ye4bC4Z-0mv-1nKTuDJWotF5gHQ4ZampHrLh_qfCY10D00s-unO9ATFKYcLRG5Q0MCc2dikeck_mj30G_Et1mpO8kCVGkGtSECJ8eSqWyk4hvqMS20C-NwvmAazE0YPpgR2cyynVp5BbD8u1_XpOSlMKEwB_-u6IjI22Q1z0sUkavuLvAjagQfraJVZ9RBWfSu5cc-xXUQeAjvT75bgb4a_nNHTJxm095lRrzw-y7_Xgbow1_FJFJcxH5gcLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910d3b9d30.mp4?token=YtH17x7Er5vLSXMTsUHBIZ79ticsdKkZp0h10SquoUCW13ORTgKSnCSIdjORYooknEKsG85phAIF-SuBPCazYmX25ye4bC4Z-0mv-1nKTuDJWotF5gHQ4ZampHrLh_qfCY10D00s-unO9ATFKYcLRG5Q0MCc2dikeck_mj30G_Et1mpO8kCVGkGtSECJ8eSqWyk4hvqMS20C-NwvmAazE0YPpgR2cyynVp5BbD8u1_XpOSlMKEwB_-u6IjI22Q1z0sUkavuLvAjagQfraJVZ9RBWfSu5cc-xXUQeAjvT75bgb4a_nNHTJxm095lRrzw-y7_Xgbow1_FJFJcxH5gcLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور دارلین گراهام در مورد اسرائیل:
من با نتانیاهو و همسرش ملاقات کرده ام. آنها برای تشییع جنازه لیندزی در شهر بودند.
🔴
من یک چیز را به او اطمینان دادم که در کنار اسرائیل نیز خواهم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/142437" target="_blank">📅 14:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: میانجی‌گران منتظرند عمان و ایران ابتدا به یک توافق دوجانبه درباره تنگه هرمز دست پیدا کنند و سپس به مذاکرات گسترده‌تر بازگردند.
🔴
در مذاکرات عمان و ایران هیچ تحول جدیدی رخ نداده و منتظر دستیابی آنها به توافق هستیم.
🔴
دستیابی به توافقی درباره تنگه هرمز می‌تواند ازسرگیری مذاکرات ایران و آمریکا را تا حد زیادی تسهیل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/142436" target="_blank">📅 14:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjynST7eBzOMprgjbVhktdu70rERRZzGZIR6vtF1iI9GbztI9BgM1HgHFzUsjxdDtd44VXhJBcGrOWPMf9uyyk0v5iz6OK9Ywq5VQVt3-T_XiuiOJl0s178xt5MPnXncx_JGhRsnICAZuS1Xa8X0qv8NkoxmQlUuzAWZHcnwAl6jTFvXPI5b1N8px_EBehxgm_XGLrfIHLC1u5fDPowwUOwAZmjozdtI0MZhXuvFZ77rVAkeBQbGuAFozyQIrB4CWdqlNAa1fb9iYuwB8TiMqsfwKBE7Giu75M7k7gC0J-5TIlri1vNsHdbel8Cr4FhpE8sUMO7uMarF7z4wdK37AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ تنگه هرمز را منطقه جدید امریکا خواند:‌ یک منطقه جدید در ایالات متحده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/142435" target="_blank">📅 14:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز : عربستان سعودی نقل و انتقالات بانکی امارات متحده عربی را تحت نظارت شدید مالی قرار داده است که باعث تاخیر یا برگشت برخی از پرداخت ها شده است.
🔴
مقامات سعودی محدودیت های مستقیم در امارات را رد می کنند و می گویند این اقدامات بخشی از کنترل های ضد پولشویی است، اما منابع آن را سیگنالی از افزایش تنش ها و رقابت اقتصادی بین دو قدرت خلیج فارس می دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/142434" target="_blank">📅 14:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142433">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: تلاش‌های کنونی بر خنثی‌کردن بحران جاری [میان ایران و آمریکا]  و بازگشت به تفاهم‌نامه متمرکز است.
🔴
تلاش‌های ما در مرحله کنونی بر توقف تشدید تنش و بازگرداندن دو طرف بحران به میز گفت‌وگو متمرکز است.
🔴
آنچه ما در قطر می‌خواهیم، توافقی برای بازگشایی تنگه هرمز و برقراری آتش‌بس به‌طور همزمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/142433" target="_blank">📅 14:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
تام باراک:ما نگرانیم از حملات هوایی اسرائیل به فرودگاه ابوذهور در سوریه. دولت بشار اسد هرگز به اسرائیل تجاوز نکرده و نیروهای نیابتی در اختیار نداشته است. بلکه بارها و بارها تمایل خود را به کاهش تنش با اسرائیل ابراز کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/142432" target="_blank">📅 14:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر:  در ۱۹ مارس بقایای یکی از دو خلبانی را که وارد حریم هوایی قطر شده بودند، پیدا کردیم.
🔴
بقایای یکی از دو خلبان را که وارد حریم هوایی قطر شده بودند، به طرف ایرانی تحویل دادیم.
🔴
طرف ایرانی به دعوت ما برای اعزام یک تیم فنی جهت اطلاع از روند عملیات جست‌وجو پاسخ نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/142431" target="_blank">📅 14:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از منابع غربی مدعی شد روسیه از طریق دریای خزر قطعات پهپادی، موشکی و مهمات به ایران منتقل می‌کند تا ذخایر تسلیحاتی ایران را بازسازی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142430" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcXVem0PcPY4jWCmp-uaCdLQTIX6L8C1wDOTcD8719r1otOhqVOwSqIrusj3Tcy4dofE0CjeIuK_xa2wMbmqU3seit3ljltSoYik3Frm6bGTFemSFJGCRe_OO73dV66AYgAJQgyqOfgHkmSZ--UUZmeeWZXerUEQFf7UZ481EAB6ARPRNyddiFkyvxTq-JvFqOlUNVSnrHS2YMHRSTRtvG1tVKUhQa4uyQEOXAd1y64rLZ-0A-KnHJvCrtiOcCxGJavpZ2bw5qZKGoZXirOstVb0XyvtvzxfKETKaTWLO9z0MgKorgWut0gy6FEx31T5yNvabIEU47KVZpeNWAJDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه سوریه حملات هوایی را که به پایگاه نظامی ابو الظهور هدف قرار داد، محکوم کرد و اسرائیل را به طور رسمی به انجام این بمباران متهم نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/142429" target="_blank">📅 14:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
قطر: تلاش‌های کنونی بر تنش‌زدایی و بازگشت به یادداشت تفاهم متمرکز است
🔴
سخنگوی وزارت خارجه قطر امروز سه شنبه اعلام کرد: تلاش‌های کنونی بر تنش‌زدایی از بحران کنونی و بازگشت به یادداشت تفاهم متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142428" target="_blank">📅 14:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خبرنگار الجزیره: در دوره زمانی ۶۰ روزه که در یادداشت‌ تفاهم ایران و آمریکا آمده بود، نه مذاکرات واقعی‌ای در کار بود و نه ازسرگیری جنگ تمام‌ عیار؛ کمی پیام رد و بدل و موشک‌هایی شلیک شد
🔴
منطقه اکنون رسماً در وضعیت «نه جنگ، نه صلح» قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/142427" target="_blank">📅 13:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtV5g51c9Iiv-OhhIjzDdXt92dBT6eCvnJ0b5dcNNNJpn2vmzeAPuC7a91ubox6XEO5hNXf2I74_Oh2F6-fgSXgZ6-fRm4Iz-k9VI7gc82SKEqls4qFGQHNRzRRn4Zmi2XhhYQqPNENCWcR2Y6fwGjfED8Xj1nSPbvlbFCJtr520vO6lXOrQob3drqTmPGsCvQqkYimuvSh2b8MeHwmhxjbwCCDz9NEem0ypoExzKfZAqTl6MMNtjjbOpHepWIkCAyfLN2V1T8Ze2cG1K96gI24lrn2zHAcEx7xybZoyetaxuy7U22JZFpyD5v96NUSsSugicWL9gQVhgHrujijy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: تصمیم تهران بر این شده که مسیر تنگه هرمز کاملا ایرانی شده و صرفا از مسیر شمال باشد
🔴
مقامات عالی ایران تاکید دارند که «بازگشایی تنگه» در مقابل «رفعِ کامل محاصره»، «آزادسازی اموال بلوکه شده ایران» و «رفعِ تحریم‌ها»ست؛ اقدامی سخت و پیچیده ولی شاید شدنی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/142426" target="_blank">📅 13:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9rkl5aiDgh5vV71M0NhBnElzRrTUOD1ReXgz0gzrCjgUrO50mwtp_jzjj9QZLdUWhxWUOvZ05CiIMPtxoisSny0w2Dux1yhz9Pz2UvayjBUa6z7vF5-VGhfpOtwvcHTHII9Wsdz4G_8K429iHA9WuM7QI8wY2EUzSUvP3f7fdHqJ005j2H8PYPX-f9Z9HTVtHanGPt2JljX9eqvYwlev7A1OoOMc65WgOUIMLXz5i9Tc9yvRvl_OO_ai-3GN-rFJ0qm-pQoqBuvwGkMYPRSgz8dahWRHffkgB1O133MWhYcaDFj7g0PXhrxbzcWjhYTDDhDOnSp0SK4hwcLuPmz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uzb5ELPJpp3n1xMmZiDY0yxoBHAENOtZnmkM7o6gNvSFIrQsNnwl9L6dSInqDSY_4rRwDZf9FNwU5wvc1jp71vL685ITbkYGzG-jQhzHTVmnh0CIRnViDJt1KdfqFgTV-KzCxsMtsiY5e_PcJt02qXoTsv_mAzlOiKUvvTWGeOzd5s6jyoDFHYXbMFLnFZwLMr3Bl832F6bCWlARa5CuPgUCXJfODikJEq_0PaV9Gj1-sWXfyRhTY5cROzHJmk2gTADFziG_uK5vXpZAqjl1MQ5ylWfIMxuUWfcrZ9TZaE7Ryt8O3KqXDVJ8Kh6ScvWBzC3OtB6E1xkR4jqkXGsOzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d3d7902a.mp4?token=MB1jl-fjBHVlgHs2PCNGZNddD7X89wcRxaA0RMnxusRvxg7AbH7VNuSqiDcwYTVqnoifA5wnXOH1ovHXxPpuU4vziEJNejU-v-KMQ-U9IKJv65aSiSwEXIKV-z6Kx3OJv9m0uSsVgbJyrydXv_cVdd7plKnrmRcMF-YMP-e1ZVWsBeRTHFIJkSYwueJu4y2dScsf6HfWjhjFBhq-VpIUG1uf2YiPFHITfUw_5NcFUKHa6uNRt3vPa-S50FYUDONsLpxVJ4HVkro5Ps0vga8JKRddxoxBZzVifrwI68FMcdHcpR7R2J-lYPbxmrrgrc2SIrxv1RfNVHsZpkxq_cAqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d3d7902a.mp4?token=MB1jl-fjBHVlgHs2PCNGZNddD7X89wcRxaA0RMnxusRvxg7AbH7VNuSqiDcwYTVqnoifA5wnXOH1ovHXxPpuU4vziEJNejU-v-KMQ-U9IKJv65aSiSwEXIKV-z6Kx3OJv9m0uSsVgbJyrydXv_cVdd7plKnrmRcMF-YMP-e1ZVWsBeRTHFIJkSYwueJu4y2dScsf6HfWjhjFBhq-VpIUG1uf2YiPFHITfUw_5NcFUKHa6uNRt3vPa-S50FYUDONsLpxVJ4HVkro5Ps0vga8JKRddxoxBZzVifrwI68FMcdHcpR7R2J-lYPbxmrrgrc2SIrxv1RfNVHsZpkxq_cAqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند جنگنده F-15J متعلق به نیروی هوایی ژاپن، پس از بروز نقص در چرخ فرود در حین بازگشت از یک ماموریت رهگیری اضطراری، در فرودگاه ناها در اوکیناوا، فرود اضطراری انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142423" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سخنگوی صنف جایگاه‌داران: استفاده از کولر خودرو مصرف بنزین را ۱۰ تا ۱۵ درصد افزایش می‌دهد، لطفا رعایت کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/142422" target="_blank">📅 13:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe3abc88b.mp4?token=V_mhtR_ntwId5mtC5KpZv1xWa-57Xag3yLL5ZpHpxfQ5-IrEf0X1qFHVWhfEa-iOHrnsPzRj_I4jwT96ytLRRwYYn8YoPXmEEThC3TbB7ziPRmOxfExkVvWtGODgVHxFX6rCxkmxBBFTN4bnO4RNt8_cuevUfOy0V2SszmNadXwyHWalE8IOoB4x7r9WzQ70fl6jl5zEM7vM-5EjmPTmkYJV-FoaVzeUImSNYdnTlMTgbCJwTXYhyrI0sUh5TiF4FU103x4pGSQswt3vfwVSebq89m6rkOfgk90AtQilgWJBqrhYyFrwjuaKGMEIJmpkj8v77grBAkQvQxg1yzRYiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe3abc88b.mp4?token=V_mhtR_ntwId5mtC5KpZv1xWa-57Xag3yLL5ZpHpxfQ5-IrEf0X1qFHVWhfEa-iOHrnsPzRj_I4jwT96ytLRRwYYn8YoPXmEEThC3TbB7ziPRmOxfExkVvWtGODgVHxFX6rCxkmxBBFTN4bnO4RNt8_cuevUfOy0V2SszmNadXwyHWalE8IOoB4x7r9WzQ70fl6jl5zEM7vM-5EjmPTmkYJV-FoaVzeUImSNYdnTlMTgbCJwTXYhyrI0sUh5TiF4FU103x4pGSQswt3vfwVSebq89m6rkOfgk90AtQilgWJBqrhYyFrwjuaKGMEIJmpkj8v77grBAkQvQxg1yzRYiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دادگاه جنایی دولت سوریه امروز «وسیم الاسد»، پسرعموی بشار اسد را با اتهاماتی به اعدام محکوم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/142421" target="_blank">📅 13:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
الاخباریه سوریه: حمله به فرودگاه «ابوالظهور» کار اسرائیل بود
🔴
فرودگاه در ۸ نوبت هدف قرار گرفت
🔴
خبرنگار شبکه خبری «الاخباریه» سوریه به نقل از یک منبع نظامی گزارش داد،  جنگنده‌های اشغالگر اسرائیلی بامداد امروز طی ۸ حمله هوایی، باند فرودگاه نظامی « أبو الظهور» در حومه شرقی ادلب را هدف قرار دادند.
🔴
به گفته این منبع، این تجاوز منجر به خسارت مادی به زیرساخت فرودگاه شد و تلفات جانی در پی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/142420" target="_blank">📅 13:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIlETVAqAvcAftwknV76mr-VyTIjqGm0MpBakYHCzxp7Zk9yWKfHhPnlBAIMnNjuSmxiaVVHu1kbA-2j8qSQJGKw0geyJVr7PbKhfDV4UrKVKzd2mM-SlEXvB9sSfksGojuk_rox0O3uSmie5ld3OT48q2elm11EX1Btgep8xi1jCJVLn6BtCdb2coWfB_L7yCWdk4G8zV3_tMVHE_CQ9Rxs3iLY_cDkzMEBcE-fiuo2NvPUucA7CpJbTM1LBp1YdCQR0087J5Zv_kNlz14f2x3gpai82UUJ4JvZFL-FxH9miXxX9_bctU7BK5TEpTbJK7lmMO7mnjZRuFUl0Hr4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از دیدار ۴ ساعته دیروز نتانیاهو و جرد کوشنر، نخست وزیر اسرائیل هی سیگنال مثبتی برای اتمام جنگ در غزه را نشان نداده و اینطور به نظر می رسد که فعلا قرار نیست شاهد صلح در غزه باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/142419" target="_blank">📅 13:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=MccqL4PVSXnt2bRhRT47JdcoeAUGEqFp5bndUkfIYNt4LV1Aaj0iwnTEAwMzjsdblt3_lIoBiSLB1dsOGVWOMxNV0SssauWBPknUOYa2cMwnjN01mp_4oDWP6iEPqCXXaETqYRYdu9vzlqs1hkp-_hWbbRVXDb0sLyG-ADHdj2sJgQhNojmY8y6bFUSHen4rjLktZvJbBozVh_bkYS1TLCApVmzciiPNAamkir9zHBeqImwFSPEUKLNLwk5gT2K5OFBmcbFW_r_ZKsvstD7RLk8sXZ0IYErokojWAPBnQEWDF6KsObTNFmCCphOSPKVViEEhWpgxeUwWrc6L5y3gJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=MccqL4PVSXnt2bRhRT47JdcoeAUGEqFp5bndUkfIYNt4LV1Aaj0iwnTEAwMzjsdblt3_lIoBiSLB1dsOGVWOMxNV0SssauWBPknUOYa2cMwnjN01mp_4oDWP6iEPqCXXaETqYRYdu9vzlqs1hkp-_hWbbRVXDb0sLyG-ADHdj2sJgQhNojmY8y6bFUSHen4rjLktZvJbBozVh_bkYS1TLCApVmzciiPNAamkir9zHBeqImwFSPEUKLNLwk5gT2K5OFBmcbFW_r_ZKsvstD7RLk8sXZ0IYErokojWAPBnQEWDF6KsObTNFmCCphOSPKVViEEhWpgxeUwWrc6L5y3gJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنسیس مدل 2013 در امارات: ۵۰۰ میلیون تومن
🔴
ارزان تر از پراید در ایران...
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/142418" target="_blank">📅 13:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
قالیباف: صداوسیما باید کانون انسجام و امیدآفرینی برای ۹۰ میلیون ایرانی باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/142417" target="_blank">📅 13:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گزارش‌های جدید بلومبرگ نشان می‌دهد که هزینه اجاره روزانه سوپرتانكرهای غول‌پیکر (VLCC) برای حمل نفت خام از خلیج فارس به مقصد آسیا، تحت تأثیر خطرات عبور از تنگه هرمز، به مرز بی‌سابقه ۵۱۰ هزار دلار نزدیک شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142416" target="_blank">📅 12:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142415">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrXCjBPJNHA7-KHLnJnH__7de-sfEetliRXq2qcN5-OOE0Z5ISoNUJx4xp5pvRsp0f1zQPBvBsBoqlM8TX7w9dIJ9CAlRTn5-0AT9cQL6E5o3PqfxPIS0YZJP5XzWlWXiYZaseNX6yTBP1MHccWfx6bcC6xuoMkDOwEPUoihhEzNrnlo3jULeGJvhkos_5eVaPV6dYehBgyIQko700V9CwmH7XzISOu5xYeQ0kkWSeLUR9oMxgs8E_U-SWozA2Xd6XJVg4-BkD4oxRdKXs0oGeglzB3Q6SFqWgWqivEi6iIiEoIrDY4tzj_SZCqScxW0-YuT-m8JVRuD_-aUZxNqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در محدود کردن شدید راه های مهاجرت های قانونی مثل کاری و دانشجویی از همه کشور های دنیا به آمریکاست.
🔴
تنها کسانی که پناهندگیشون قبول میشه، سفیدپوستان آفریقای جنوبی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/142415" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ارتش یمن، مواضع نیروهای وفادار به عربستان سعودی را در مأرب با موشک هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/142414" target="_blank">📅 12:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d3695c74.mp4?token=SEmBFLHXr30JZNzfVqzoWV0guIe9nkRnonrdIfJhFdavKkYcR8QzHqej7urqUw46IWGwMJmlDzZSGtYgY51OqHdYG8_1xxLw1HtzuktXof4BDiuAQQRanXgkWLyZacEfRT3K-L3gI2XMhoSEP1sjOf1jpuNSWSu2n1Agfr6J1mTuiCgR1ZtBB-nIUY1HqlBMsOzbwfdZ2eGukL0BD5Adw-1D1OLnrLXywMZWmf5l2L0W3ZNB9NYHPzjKGhmIWb4otekBioS9FjJSvdsepq5BtheDAwNEGcK8R5Am7aQ9HDdfKhpqgMhuNdJNyc1oysoG-alN3eRbi78uSJpM7wBh9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d3695c74.mp4?token=SEmBFLHXr30JZNzfVqzoWV0guIe9nkRnonrdIfJhFdavKkYcR8QzHqej7urqUw46IWGwMJmlDzZSGtYgY51OqHdYG8_1xxLw1HtzuktXof4BDiuAQQRanXgkWLyZacEfRT3K-L3gI2XMhoSEP1sjOf1jpuNSWSu2n1Agfr6J1mTuiCgR1ZtBB-nIUY1HqlBMsOzbwfdZ2eGukL0BD5Adw-1D1OLnrLXywMZWmf5l2L0W3ZNB9NYHPzjKGhmIWb4otekBioS9FjJSvdsepq5BtheDAwNEGcK8R5Am7aQ9HDdfKhpqgMhuNdJNyc1oysoG-alN3eRbi78uSJpM7wBh9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: یادداشت تفاهم اسلام‌آباد سند پیروزی بزرگ مردم ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/142413" target="_blank">📅 12:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eusnWqrHLQQpMD4kO1CFB8ZUGbtBha6yf8KrHMwXXeOX8ZyRsMdAHBxOuvcFTsk9xxGjogFRi4NgWh9ie6nG5Uk_wxQwGez4_5mDKPvRVhQp9C232MOYdaqNILYDiiY7EGZewIQMaGUGl7T_2KLGBHE5B30eAODllXY6290alFWnYCJuZS5pJNzmHTEw4D1yOzvpmJO1q-Wlq7KaTfyT2_kqHhxKXkSjQUKe9PDSiFO_xC-9Z8t2WhDul6MDnsxNOfozGfzU66PUMm6uR9XH4QjBSJMmmRTKAPL3SkRzlemiifm-Y03Ie4NrXxfQw6ZwhBXOc2ctzZgc5NpMfascGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: با رد ترامپ برای تمدید دوباره آتش بس دیگر امیدی برای صلح ایران و آمریکا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/142412" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW3BNj1foNXLf8NfT4FyEIHC88XHblO2pyoP6_N5yiEgZRGf_zWXfek9SD8LVsiV93-5Z9FHYKmXb6hl6SU4sLdJTbIjHjTDG9xXubHSdtkt5T5f3JnDIRb3xFW3BritOWntvBdYv6bhYn6LA-gGskgy_AkmDOJMAnnczA3Hezv5dePP2KuREifNPGImZET9ML169KKynhmsbBivG-AU6qH7FbcMtwJbcFKkcNwxyV71enjPMnpyK_Gc1PMnYblmwUWNk3-xrU4lz5XwJqOJHwNWoF2x9qNnvIhzgJAwYpPSgIyDlzNsrNTNgFjbu-uvH0UX32QOYFKxpjnbibf3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی به شدت حمله به دفتر مسعود بارزانی، نخست‌وزیر منطقه کردستان در اربیل را محکوم کرد و آن را نقض آشکار حاکمیت و تمامیت ارضی عراق توصیف نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/142411" target="_blank">📅 12:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0218bba7.mp4?token=BdxA2tZuDUFO3HiwJyzOwUinW3B8hHvp2B2EERRqpl9PAx5mlWZuB9j2i665cFlXc6Jeu3yO-u1bemmWTkB_NhtIgQr8Sz-goVEWcoLZ-KkSNsXD2b17mVDWKTsLGna0V7gVApKjwjpbaq3e2WN74vQCedGNWYgzfWR801ou5806zAOSe3t-K0XuCqGDg3vLk5ShMU6uJ4afa0s32_kdJIn4H0HhTtOsVe9dQl0hdetC5BsF8d_LmJr14FmutYwMX71yCVZP1MtketDt9aXz7M4jzhTdFQIN-FyvXFdprirK3Hl7Cq8hu62r6AhgQxWSBcgVZK7cXV6c-xLJ7iJqaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0218bba7.mp4?token=BdxA2tZuDUFO3HiwJyzOwUinW3B8hHvp2B2EERRqpl9PAx5mlWZuB9j2i665cFlXc6Jeu3yO-u1bemmWTkB_NhtIgQr8Sz-goVEWcoLZ-KkSNsXD2b17mVDWKTsLGna0V7gVApKjwjpbaq3e2WN74vQCedGNWYgzfWR801ou5806zAOSe3t-K0XuCqGDg3vLk5ShMU6uJ4afa0s32_kdJIn4H0HhTtOsVe9dQl0hdetC5BsF8d_LmJr14FmutYwMX71yCVZP1MtketDt9aXz7M4jzhTdFQIN-FyvXFdprirK3Hl7Cq8hu62r6AhgQxWSBcgVZK7cXV6c-xLJ7iJqaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: در دنیای وحشی حاضر قدرت سخت حرف اول را می زند. در جنگ این موشک های ما بودند که محور قدرت ما بودند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/142410" target="_blank">📅 12:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عراقچی : اسرائیل تمام تلاش خود را برای جلوگیری از دستیابی به توافق‌نامه و عدم اجرای آن به کار بست و این تلاش‌ها همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/142409" target="_blank">📅 12:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142407">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS0PyPheJNMc9UbdVvBdhu4Gp5xpe5X1UGl6W4_qFCiXWAyfVi2xTboyT4lD0l_-78KePk03MU1lNnTq7CTlCC4ff2j38o_3CQxbT3MbMPI_IIp_hwIwgUsR9BGdp8ntwjA5dyJnGXE2oAv9KcOhjxh8ptPz__9bkc9rA2dxQscWz3DWp6kAm14RhlqCY-NiuG84NaVnZwQVbSHPVwTccAyU3QSyoI7a-lOgeTBhEyGQmgdE2j-O3gasmFmSXM5fe2MzSVZae5urWj-rhmorPpcL8W0T5JzgMZNxghjqZKfhU7u3cBbTllDE2qjxS7xaFClLa-Z5scUqYUkafLGY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZgYxgS7m6Mge2pwTK8d9mqe0QAA7uCQydj097bcbXhODa-QFH8fiItfsPQn0yo2zXjVoXbD4Rn80kDT1ybs94vx8gsM2XDE1AGMdZ1-Hl1aPNNR4xJjMMEUXXwqkGj2jp4zrNIqGOnXdf-wxzQoQ8qHdeEn3dBpnbxQlnlJ0c9jb5CWCk96llEhPKTnuzwKUtXXaL13StY0Y_gRFnB_J57q79NSWe2bI5rX8LYGKz4fOtgBoGmme2gl1bv75uFH-qwNQG8DwUHuxNB1j-tndbgno-zuitLvAzWZijUkdEyjEnAc860nvYsapw0SZDFbuImAYiEnOShIM7kq_sH_zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی که دیروز در تنگه باب‌المندب مورد هدف قرار گرفت، این اقدام پس از نقض ممنوعیت تردد دریایی بود که توسط ارتش یمن اعمال شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142407" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142406">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTOfKyqYiCvoGqPHxx1kvQFUnNlkNEBTk7RsqvrW32pAyzRry1qftcyzSpjZvMx2ETK08fqu7ZO96a7LzidhBOPN8xfJSxUo9y3aTdc4L9hfalDaT5cyBKPX5o5D64oYZj5FlAKnRXYH7bvc0lKU1c0XfMY-aJdtNAfNorgGEijNO9KSMGY16JWWr1SceYAj9euZ5eorBRrcTfJMe6i8_6GPjgDJIiEQj7gnnF3HWDfa4HF2kiNL86PVZMmVmkN9O_0CxXG9LOUKhfbCkQpouG6km-4nWk4RPug171k9MblhkKtNjTrp2oXm62-KHj87_-nVydqVMOm5_eNXtifBlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلنا: هر خانواده باید ماهانه حداقل ۹۰ میلیون تومن درآمد داشته باشن تا بتونن حداقل هزینه‌های زندگی رو بپردازن درحالی که دستمزد اکثر کارگرا به ۴۵ میلیون تومن هم نمیرسه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/142406" target="_blank">📅 12:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142405">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8c1b68c6.mp4?token=AxsADPbaxlKnrq4Ru_QSPrImuMWgIgJNEOzUJ4UUolae4qsQmpPGcU2dpI-Kip3NZvnQbSZx6MkiiNr6cs37OOJJ-lel3vSiJKVJXMSh5sNuu6ryjYKjpdVVhmlSRfjjrsuWAV8RLWbE7qISBSO_7X1Lm_k3Azp1saYx8STueDsUFH4I5RgNWeBsm6pbePqawcgafwFoy64E05dpmfErWdmZD-O8N4qwL3rGhxIxXSHp20WPnJtvr4NEOiJ1yI-nlLyVERgC21pli91nkbFkIyffm1Yy08-k49UPrjmJeRqQFFGPNM0tAaRVVcUzvm9h5OApJUM7ZsICplcq7Fp256dB-0XPeGQ8-qcX-u8aRsDjUjqa8MpZl_YcCVxppQllk-oSvITQXqbVqonjJ74O7dxtcd_PhG1SQzJs4HNKw8T4lz1JnyYADiqumjRQle385IqOPhl5XJ3uoUfPWwyQxmcgOmjWlk0UC8raGZvCAi6oj0l_bClFGZgQgBi6fOHWxMY4vLYaVf8K1gDWnw2wYBMid2LS9tmX-3zuYOcebzN7gYRHnruyqogkNGrZ5i12M85qyIpFSB8GbnJ884HhI2TPikW7NEbGfexWT7gTdI5DpuSOC8REWDnEvZaQFd73I11jThJEE8IpVrPLJuQ8WkvJP1GeGlYx1s_EQ3qR1w8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8c1b68c6.mp4?token=AxsADPbaxlKnrq4Ru_QSPrImuMWgIgJNEOzUJ4UUolae4qsQmpPGcU2dpI-Kip3NZvnQbSZx6MkiiNr6cs37OOJJ-lel3vSiJKVJXMSh5sNuu6ryjYKjpdVVhmlSRfjjrsuWAV8RLWbE7qISBSO_7X1Lm_k3Azp1saYx8STueDsUFH4I5RgNWeBsm6pbePqawcgafwFoy64E05dpmfErWdmZD-O8N4qwL3rGhxIxXSHp20WPnJtvr4NEOiJ1yI-nlLyVERgC21pli91nkbFkIyffm1Yy08-k49UPrjmJeRqQFFGPNM0tAaRVVcUzvm9h5OApJUM7ZsICplcq7Fp256dB-0XPeGQ8-qcX-u8aRsDjUjqa8MpZl_YcCVxppQllk-oSvITQXqbVqonjJ74O7dxtcd_PhG1SQzJs4HNKw8T4lz1JnyYADiqumjRQle385IqOPhl5XJ3uoUfPWwyQxmcgOmjWlk0UC8raGZvCAi6oj0l_bClFGZgQgBi6fOHWxMY4vLYaVf8K1gDWnw2wYBMid2LS9tmX-3zuYOcebzN7gYRHnruyqogkNGrZ5i12M85qyIpFSB8GbnJ884HhI2TPikW7NEbGfexWT7gTdI5DpuSOC8REWDnEvZaQFd73I11jThJEE8IpVrPLJuQ8WkvJP1GeGlYx1s_EQ3qR1w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
قالیباف: افزایش قیمت بنزین توسط دولت تدبیر حساب‌شده نیست
‏
🔴
کاهش مصرف باید با بیشترین عدالت و کمترین نارضایتی انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/142405" target="_blank">📅 12:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142404">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
با تائید حکم پژمان جمشیدی از سوی قضات دیوان عالی کشور، رای صادر شده برای اجرا به واحد اجرای احکام صادر شد.
🔴
چندی قبل خانمی جوان از آقای سوپراستار به اتهام تجاوز به عنف شکایت کرده بود که جمشیدی از این اتهام تبرئه شد و به اتهام رابطه نامشروع به تحمل شلاق محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/142404" target="_blank">📅 12:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142403">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56de43f40f.mp4?token=Az9R26-n9prFj85cazaZu4frNomxS98EhbpTuUzAF9Q79BaEggzJd08qd9sI4Dd8tJrYDcx3IYE7KkG90cuCUG1xLnHhmNVyMnCzuHJ6FBQiFw72fM7NVxezcOPrH2UPJizttynykIs4W1xCtWyBkbp-m--lIc3fcPk7k7tG6eMxc6ouJG7bmpSWphJbnHYa_OnD918xPWlqovp7_3bsnCuFCFPY8NvC6IaveEZahGK6qARkYuXUeqyZ6tfOuGH7t_xoqIomoUMfj_LGV8GjKgEMzlrz2dVbptOTedP5Yee-70F32tjVrHVJYZAfUuhJQmOWBMYM_pqXSyQ_WSE2M4EfHgPNcLo2xI-hHLGwAtSESFCJrxNovoj_TB9I2TB1_5GNj_iufylpzykMqmQMbU3vQbZuambyiKg-11FsfcKv3qspAl9C04TRJolb1pGclBUu7-mzGgfwVgz5Y1jZDZhuOLNnMXomTSERmqbIwq1EqVzwpGqsWwO7FDU679xQY8Y4Iqlb7E1y4WRUjLmk2ikf0z440nvNy3zLBfo5OUn3tJjnzxuRq-Xiy15cNxa_aV-6YbIg2im1sxDn7-wO9X9OkBY-WoQHNS0fZ3nedkCjQcbekvDj7fg9kPXCM7JWNyuHCMQCy8fncKc5_k0ItmVzVyYwVOnm3XYx28ydz1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56de43f40f.mp4?token=Az9R26-n9prFj85cazaZu4frNomxS98EhbpTuUzAF9Q79BaEggzJd08qd9sI4Dd8tJrYDcx3IYE7KkG90cuCUG1xLnHhmNVyMnCzuHJ6FBQiFw72fM7NVxezcOPrH2UPJizttynykIs4W1xCtWyBkbp-m--lIc3fcPk7k7tG6eMxc6ouJG7bmpSWphJbnHYa_OnD918xPWlqovp7_3bsnCuFCFPY8NvC6IaveEZahGK6qARkYuXUeqyZ6tfOuGH7t_xoqIomoUMfj_LGV8GjKgEMzlrz2dVbptOTedP5Yee-70F32tjVrHVJYZAfUuhJQmOWBMYM_pqXSyQ_WSE2M4EfHgPNcLo2xI-hHLGwAtSESFCJrxNovoj_TB9I2TB1_5GNj_iufylpzykMqmQMbU3vQbZuambyiKg-11FsfcKv3qspAl9C04TRJolb1pGclBUu7-mzGgfwVgz5Y1jZDZhuOLNnMXomTSERmqbIwq1EqVzwpGqsWwO7FDU679xQY8Y4Iqlb7E1y4WRUjLmk2ikf0z440nvNy3zLBfo5OUn3tJjnzxuRq-Xiy15cNxa_aV-6YbIg2im1sxDn7-wO9X9OkBY-WoQHNS0fZ3nedkCjQcbekvDj7fg9kPXCM7JWNyuHCMQCy8fncKc5_k0ItmVzVyYwVOnm3XYx28ydz1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: هر فرد یا دستگاهی که با گفتار، رفتار یا تصمیمات خود، باعث نارضایتی مردم شود خواسته یا ناخواسته در زمین دشمن بازی می کند
🔴
تغییر شیوه‌ کالابرگ  یا افزایش اعتبار آن ضروری است و باید هرچه سریع‌تر اجرایی شود
🔴
مهمترین وظیفه ای که ما مسئولین کشور  خصوصاً مدیران اجرایی دولت بعهده داریم  این است که وسط میدان حل مشکلات اقتصادی و معیشتی مردم باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/142403" target="_blank">📅 12:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142402">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
قالیباف: خیابان، محل میتینگ های انتخاباتی نیست  بلکه میدان‌های اتحاد مقدسی است  که باید هسته‌ سخت ۹۰ میلیونی را در خود جای دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/142402" target="_blank">📅 12:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142401">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d5daba12.mp4?token=Z520f7nJcsEBtIkEJ0NCpJf190b2M4_JSmOmdFTVgaHc8D6f6Dmo22akCPgilkgld7NR4FuIExRSN6RERxGZkGwxbot5UV00pvoRoXN1lzmH0KSO5sCdS_VpeDpCNuT7L5DUrkbG-VqwB39nLS7qykgoRYjGU9U1TiUeWaBO0yKKppsOh4x4GIvGhYbnFV0bfa-bXu7ClcpZTCj6u9eXB5CQFHoZBwHCtiBjxgqfRVph-cy5TBlKU0cOEPi2-kQBCJIWm1S4ePYVwuSbaH12sDoHdKSRI_XTm7i1-GO9BC-PibDW-zpYOXAvqNU_-dkvZWyQ36ekFoS3w5cBw4VW4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d5daba12.mp4?token=Z520f7nJcsEBtIkEJ0NCpJf190b2M4_JSmOmdFTVgaHc8D6f6Dmo22akCPgilkgld7NR4FuIExRSN6RERxGZkGwxbot5UV00pvoRoXN1lzmH0KSO5sCdS_VpeDpCNuT7L5DUrkbG-VqwB39nLS7qykgoRYjGU9U1TiUeWaBO0yKKppsOh4x4GIvGhYbnFV0bfa-bXu7ClcpZTCj6u9eXB5CQFHoZBwHCtiBjxgqfRVph-cy5TBlKU0cOEPi2-kQBCJIWm1S4ePYVwuSbaH12sDoHdKSRI_XTm7i1-GO9BC-PibDW-zpYOXAvqNU_-dkvZWyQ36ekFoS3w5cBw4VW4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: قبل از رفع محاصره، آزادی اموال بلوکه شده، رفع تحریم  نفت و  پایان تهدید و عملیات نظامی در همه جبهه ها  و دیگر شروط تفاهم نامه، تنگه هرمز باز نخواهد شد
🔴
فرصت بدست آمده از تفاهم نامه در رفع محاصره‌ و آتش‌بس، کمک شایسته‌ای‌ برای‌ افزایش تاب‌آوری اقتصادی و بازسازی توان دفاعی ایران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/142401" target="_blank">📅 12:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142400">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
قالیباف: تنگه هرمز تا رفع محاصره و تحریم نفت باز نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/142400" target="_blank">📅 12:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142399">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دختر متهم: من با حمیدرضا رجب زاده در فضای مجازی آشنا شدم، اون مرتب به من تذکر حجاب میداد و می‌گفت درباره مسائل سیاسی حرف نزن.  ‏
🔴
منم رفتم به دوست پسرم گفتم، او هم گفت تو این مداح را به یه بهونه‌ای بکش یک جای خلوت، تا هم او را به قتل برسانیم و هم فیلمش را…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/142399" target="_blank">📅 12:05 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
