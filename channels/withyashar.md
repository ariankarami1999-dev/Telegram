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
<img src="https://cdn4.telesco.pe/file/e84Qy6tCbC3vX7ka4lk6lgGOvIvG4NAEwWc9d17LxDfiT2O9iZtw4J5amRtGM5rh6aNC9mIoE7NT-G2lzLkvBCfTgVEDa7WavA7OpCTlUWs5TjxeEiqSPMOdDablr0T8bFFfBLW1bEwxqddUTr9tjKj92dhicwqaINh3LC3HP_PGJOyKqh-lfHrjPUx4Gwz71ux009qnpVAwDtVPztBEzXrGu0xZjOgNxrIvMhyuFEvEkcntxIVVm_4pgqJK-XRmhqS0KaoWJf94JK-jrH-IT7nokNtsSMMvNNz0Gjm7SNb7YeoADZu1uuVT4XXejWaclsYsBvaJH80PCrEW4QejVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 12:01:29</div>
<hr>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب لبنان
رسانه‌های لبنانی از گلوله‌باران منطقه واقع بین دو شهرک «میفدون» و «زوطر شرقیه» در جنوب این کشور توسط توپخانه‌های اسرائیلی خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/20705" target="_blank">📅 10:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=GrZQRlPzvUcx3RtYWvLK9yMKWwQ25l2Ro5y4gM4Ef9NFOu21GuQCVkSy_iADSmmBaS184hkna326wLr1HgvKqP2ul1-VU0gkHGmE60pVx7Kgx36KhX0-HI1ZR4qjLL2MUAeZySvLNenXQmPYudoFcVUaoujoUKY_YvIDe6_OSNyuBqm5GVutq3pTEFhNrgkArYdJVuTiZ-94StSV0DSLPXVP60h4gY1LsRAJMRNYNFJjiM-VXw3UnBBfDauaeCKwZcfoU3P6SqyfQJZqjciM783nfNitLCxOfxMh1GOmHUDD0XIV-2QaQx31Za9MxyTORTmH_ythp0LNOC9khHQk5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=GrZQRlPzvUcx3RtYWvLK9yMKWwQ25l2Ro5y4gM4Ef9NFOu21GuQCVkSy_iADSmmBaS184hkna326wLr1HgvKqP2ul1-VU0gkHGmE60pVx7Kgx36KhX0-HI1ZR4qjLL2MUAeZySvLNenXQmPYudoFcVUaoujoUKY_YvIDe6_OSNyuBqm5GVutq3pTEFhNrgkArYdJVuTiZ-94StSV0DSLPXVP60h4gY1LsRAJMRNYNFJjiM-VXw3UnBBfDauaeCKwZcfoU3P6SqyfQJZqjciM783nfNitLCxOfxMh1GOmHUDD0XIV-2QaQx31Za9MxyTORTmH_ythp0LNOC9khHQk5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی آتش‌سوزی یک واحد صنعتی در شهرک نصیرآباد، ۶ نفر مصدوم شدند که یک نفر جان باخت و ۴ نفر به بیمارستان منتقل شدند
@WarRoom</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/20704" target="_blank">📅 10:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏حوثی‌ها اعلام کردند پالایشگاه آرامکو عربستان سعودی در جازان را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/20703" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahn9AtA5Az6I_D3uDaqEGHiDGMklYyN52sPU3YkjdmIcoXitzXoSPMQNuxfDjvBHQVy_RD25FEHLWSha1pU3TviBO4TOXtogCD8hBsJnNz2GttW4md2kC85_tnT8RF_RhhlRq7om-dhOCN3nHw_PDZ-5g1Zmg3J2btzvcReHTeYXb-JQfeTaDOXCdzxYWrrTkC8Oj8bA_pgG80yAny5LVlSgjcN8vM_shyT7xUMuN3ho_9LwhXg5ZMBO4g34JKJ3S9sj0TlxDnlJcE_hIguSOylbH89agl8yHY6e_Bo0-M6uzoS5Sk_4pjF-zkqojm1_7bIQYPG3uBcEKfdll4-PfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورشلیم پست : ایرانیان آزاده و اسرائیلی‌ها باید در کنار هم بایستند و اطمینان حاصل کنند که سنگ بنای صلح فردا هرگز قربانی تیترهای جنجالی نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/20702" target="_blank">📅 10:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانال ۱۳: ارتش اسرائیل به فرمانده سنتکام اطلاع داده است که اسرائیل برای جنگ علیه ایران نیازی به تأیید یا حمایت ایالات متحده ندارد و اعلام کرد ما در حال حاضر در حال آماده‌سازی برای شروع جنگ هستیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20701" target="_blank">📅 02:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20700">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اتاق جنگ با یاشار :
برخی کانال‌های تلگرامی عبری مدعی شده‌اند که یک ناو هواپیمابر جدید آمریکا در راه خاورمیانه است.
بر اساس ارزیابی‌هایم، محتمل‌ترین گزینه
USS Theodore Roosevelt (CVN-71)
است؛ ناوی که به‌تازگی مأموریت
RIMPAC 2026
(بزرگ‌ترین رزمایش دریایی چندملیتی جهان به میزبانی آمریکا در اقیانوس آرام) را به پایان رسانده و به
سن‌دیگو
بازگشته تا وارد چرخه آماده‌سازی برای استقرار بعدی شود. برخی گزارش‌ها حاکی از آن است که این ناو احتمالاً در
ماه سپتامبر
جایگزین
USS Abraham Lincoln (CVN-72)
در منطقه خاورمیانه خواهد شد، اما
تاکنون هیچ دستور رسمی و علنی از سوی وزارت دفاع آمریکا یا نیروی دریایی این کشور برای اعزام Theodore Roosevelt به خاورمیانه منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20700" target="_blank">📅 01:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20699">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">😁</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20699" target="_blank">📅 00:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eND9nU1zofjK2tHs9FQTBnuEZHMGSI7DJxPrWgysmz2So1kO_fIVV8mbA1tCVBPhjuVdx5KxIIBmwrfRwol95Ss-df7TyYNdZHmS1lNI-7MOWIaVVnKAMh_Eolm1mUPjHY05-UOz6enWrKEGwko-Di7OWDTDQTKpP8iN7eDfr9jLySQsOXQKez3gYtS7BBuRaKQNx2uycyguYk3dKFZs-9h3fvxnQr00c1YDYyUORSci7u7eyA7wTfTJqddmvhTG3SDEsy3NA2Y5GzsCxrKtqlX-5BduwOVsIpPb9iWVrjU2H6SejR5lxtokuv7iNz4YQYZ-r2DthI7RK0fWWR45bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین باز دید پیج اینستاگرام از شهر های داخل ایران
😁
تبریز
🥇
🏆
اصفهان
🥈
تهران
🥉
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20698" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20697">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYY6V1LEMnimhWE4Xhda_ziMDN7ZH6ll39AdHIPcylV26zoGX1xSDu_DifAxCGItDnalnX0S00TSyO1vRQkasxzIzkKUCYUaMQ50UJFdPLnhD506rVxd99dqc0OJ_zvnDnbPoAlEpz3c52eQpsFSN0YLJ9jmi4o8bkgD4PBax4U3hTMqYbKiE49RK9vuFFStGNqcZD2z9K4DUPHn-J9dXMUt2iLCXcCdZfYm7e2dQOLRBz3jyxgqtkGSq_BaE_5fHSsdhGTFzDjOC1klY8kZ8UTPBQKuKbct-AhdeJNg88pSaYGSDVdwmt2PLfvLsiWxyrFCwIDQzZ9KMh-L8865VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست: تأسیسات هسته ای کوه «کلنگ
گزلا» در تیررس ترامپ قرار داره
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20697" target="_blank">📅 23:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IypkOiycCkfBfBZjnlWflYrvjgg_FWnK1618tBd96Zh0wSnZodcf2f0IJ3s_HNIy-uZUoZ-l0uPE2bqeAFY875IisFCrujkifcdqpLhukHIOQGKJhcXrB7ONXPbAe1jLEtaBTfh7SqLfl6V4LxAemoYIk33EerbQCdg2iaVVE5glxUZTOcoXOVQpWP0DpFA5jJNVDUdZkwBvyLJURh0qZUPdEp6P9S9lcL3IYpuBR7FtkuPy-d-WOy9BurHZM35rptLDuB-BqraTPaJENiIdGVd4Q_3CXrf4cDIVrgPDt8nxeTeHyouYUO4XzH_zvHmd589-HX0AjDdGPfEES-6Tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند. تا 8 آگوست، سنتکام 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20696" target="_blank">📅 23:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbsHAi3GjuF9zE65oFQzgwBK4IepJialYkpB-8_1_keqqOUxh9K84j81DOyORqlj2nsiQvQy8Z5_lI0MB9ZZeFr0Dh86m38OV2S9El371QmzDiX8Lnvwl_mXIVWNsADupLi1Ut3J3D1-Z1jwYxDWO6qszVi4KYWN8zHPVr2tgWu-QDU-QORfILlSFYR4MAS9YuckH92dLxJAbRGdmflLJ9oK0TP09QSghBSpz3_NK5AfQFV9k_sZ-hD-hu7cWM42WY8sv0Fc-7CDCKh6JhbTzI-tmddir0CvI9mfutJZ7ni1-6mq2NdNI_qNGwnS7dXkCt1D1gdOjUBEJguxPriY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد  برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد. @WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20695" target="_blank">📅 22:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تمام مرخصی های نیروهای نظامی اسرائیل تا اطلاع ثانوی لغو شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20694" target="_blank">📅 22:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وای نت عبری : آمریکا سلاح‌هایی را از آسیا و اروپا به خاورمیانه منتقل کرد، زیرا موجودی سلاح‌ها به سطح "نگران‌کننده‌ای" رسیده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20693" target="_blank">📅 22:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات رسمی نوشت: ترامپ تصمیم گرفت با وجود هشدارهای ستاد مشترک ارتش در مورد مهمات، جنگ را آغاز کند و انتظار پایان سریع آن را داشته باشد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20692" target="_blank">📅 21:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد
برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20691" target="_blank">📅 20:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کانال ۱۳ اسرائیل : اسرائیل در حال آماده‌سازی برای احتمال اقدام یک‌جانبه علیه ایران است
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20690" target="_blank">📅 20:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20689">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMWd853pQldCFOKvNujFbLtW-MRvwbCk5yW3gpTQg58IqDazu_Fa3lEaKtw_8Q31jg9v01pPq-YBwHzHBi0eXMbl8NwsO9PHBZsm0NQq4r4jX9SdEi7jSpSVKrsxBUww9ajw2OljYArbVIk3FGmE9qc3j08JgTQhmg3s2n9GxzAkDQuCP2VZixEDkC2sqwtDBEbOe3pzjPrkBvJVbKhnG72hK-cOVVdUU2Jg-Qs2abW2mk3nPBOxe7TKDMmJCbVruYb-nsPunO4PcTDEvIKS6NyvzD1Cdl_vC9-6orEXWdYNBuUUxzxC_kjjId5BCsmFhoeDT19rlBrnoTLhmw9VUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است امروز دو بمب‌افکن B-1B "Lancer" از پایگاه هوایی RAF Fairford (EGVA) پروازهای آموزشی انجام دهند و گرم کنن حسابی برا حمله اصلی . یکی از آنها در حال حاضر قابل مشاهده است: B-1B "FROWN30" 86-0124 B-1B "FROWN31" (در انتظار تایید) @WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20689" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20688">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وال استریت ژورنال : ایران به دنبال منع عبور ناوهای جنگی آمریکا از تنگه هرمز حتی با توافق است
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20688" target="_blank">📅 20:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20687">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJIXgavTtD8SCFwynvBDawN7AzWPXxUgjukEXLh7yMFVbWl23wB2DqyO0ndu4ZBG-MosQQddGe_KN_GD6J3Mo-13xfVXk5PYkxqA9yL_o-RugI1qXJ84z4yHPtQZq5uJFlvmIs6xvu7S98Cdcpnh0JU5XMR0uM2HsDDoM2V8ZkNx0y2Oqp_sHFVlqXP-6EHlPQD-wZH34OJEKiKb5uNPXAPMGSTcp2Ay_DzV9Vxcgeo86k09QdpDnE8ULDVPlwx2pVVZ11A1ir2S-O6QgmvNQhpQStM5h1jXflFDL55nn8c_xpT2El4Z9ETrDKKzZQkXf5yM3912ChPjMrKMfHUogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت سوخترسان از اسرائیل بلندشدند
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20687" target="_blank">📅 20:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20686">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dc8a5363.mp4?token=La88u3khSHy7FXKD8OuliHNTbgSKpGtirhyhhp4--T_47sCCnJtaH6-7wIBM6lziJ0LLuZouNW0yNf0_5Rfv42W6owZRM3lDS4gIaSaz10Jd7uJjfCzTWycUcFosgibAPJSnZh5EBCyxcD5mnHxYlkCDFqMtydR5-4CWDWkPYtXEBaZzOx174I0y2m2PMF-BvCt0WRgp7V1l3GPRcqxkS1hBWKVDs4ml4TGscc2IbEWR2HpGyihF-UYi5ExL55q0osqHT6K5MA2FGLqOlzpdyE_J3lXMNLqNfcg3dYCqKn-hhe3ft2TC91fhGjuaMMMBdIhPQFLWTVQDMhIMdfO0KgO2UY3utIVVAFYAkyiXi1meb7X-gSpljUvlHEdXj-cFjaBlhza2NY8Xe2Ff1Fv5OUXPrhPYYud8pIB3D7GsLbDu3YF4UuRvTk3n5maVROHI27AerYA8mQikYPkApgXYFRiDpTbb9twDJpTfDMfzozDJ2coM6-bWBjTAPPlQKyvWtp_mnHqocrY_vtkA0ZWJI8gTwvLas2mRY_ER-VAMngRRRRLLtrgyqYV1406bJdS04jvb0T3lvCcjVooHbHKgAoWCa-Q1UUym7EpBf3jfAi6exUsEvenS1D8_K0o6EDMspvAOKkpzIFOjx5MsCg7ZnsHLqz7T8ki6imuEsf5bPng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dc8a5363.mp4?token=La88u3khSHy7FXKD8OuliHNTbgSKpGtirhyhhp4--T_47sCCnJtaH6-7wIBM6lziJ0LLuZouNW0yNf0_5Rfv42W6owZRM3lDS4gIaSaz10Jd7uJjfCzTWycUcFosgibAPJSnZh5EBCyxcD5mnHxYlkCDFqMtydR5-4CWDWkPYtXEBaZzOx174I0y2m2PMF-BvCt0WRgp7V1l3GPRcqxkS1hBWKVDs4ml4TGscc2IbEWR2HpGyihF-UYi5ExL55q0osqHT6K5MA2FGLqOlzpdyE_J3lXMNLqNfcg3dYCqKn-hhe3ft2TC91fhGjuaMMMBdIhPQFLWTVQDMhIMdfO0KgO2UY3utIVVAFYAkyiXi1meb7X-gSpljUvlHEdXj-cFjaBlhza2NY8Xe2Ff1Fv5OUXPrhPYYud8pIB3D7GsLbDu3YF4UuRvTk3n5maVROHI27AerYA8mQikYPkApgXYFRiDpTbb9twDJpTfDMfzozDJ2coM6-bWBjTAPPlQKyvWtp_mnHqocrY_vtkA0ZWJI8gTwvLas2mRY_ER-VAMngRRRRLLtrgyqYV1406bJdS04jvb0T3lvCcjVooHbHKgAoWCa-Q1UUym7EpBf3jfAi6exUsEvenS1D8_K0o6EDMspvAOKkpzIFOjx5MsCg7ZnsHLqz7T8ki6imuEsf5bPng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بورب مودین ، مأمور کا گ ب : همه دیپلماتها جاسوسند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20686" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20685">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن. علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده. دقایقی پیش خبرگزاری‌های‌رژیم…</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20685" target="_blank">📅 19:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20684">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیویورک تایمز : ایران فهرستی از درخواست‌ها را ارائه کرد که امیدها را برای بازگشایی تنگه هرمز کمرنگ می‌کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20684" target="_blank">📅 18:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20683">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‎معاون ترامپ، جی دی ونس : ما توان نظامی ایران رو به‌طور چشمگیری ضعیف‌تر کردیم
بعضی‌ها داخل نظام ایران درباره موضوع "عوارض" صحبت می‌کنند
اما ایران به ما گفته که هیچ برنامه‌ای برای گذاشتن عوارض تو تنگه نداره و قصد چنین کاری رو نداره
انتظار ما اینه که صادرات نفت و گاز از خلیج فارس دوباره به همون میزان قبل از شروع درگیری‌ها برگرده
ایران در ابتدایجنگ، تعداد زیادی مین تو نقاط مختلف کار گذاشت
الان تلاش ما اینه که یک مسیر و برنامه تردد مشخص طراحی کنیم
تا کشتی‌هایی که از این مسیر عبور می‌کنن، بتونن با امنیت کامل رفت‌وآمد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20683" target="_blank">📅 18:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20682">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دبیر شورای امنیت ملی ایران می‌گوید که ایالات متحده باید دارایی‌های مسدود شده ایران را بدون قید و شرط آزاد کند، تحریم‌ها را لغو کند و غرامت دو جنگ اخیری را که علیه ما به راه انداخته است، بپردازد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20682" target="_blank">📅 17:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20681">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5SQs6uq9teENFEObyWay8jXNGFEeuT5bEcyizYdRdV440g_wMgB1VXI3l2z-ClXji4AOYnBkybyMJzuEm6DY1WA4Xh8wr7ORFx-zzITMhDf9Vm-hKyRh0o8QBRLSkfIry8Oz574qPxk1gy5nNCeocZPrJwygZ8NvIwBxJAd3Larsb4ai3aZhD16gmYisthd45-mLfEl0T7lAHYQQlGax-iCI384elHtoCB1oVvAwUMTv_1ERUw29-oOgTv7-p-OF2b9yrhb7OjRBwYBxh4PsjV0bddZfMQKIPZq6I1TEUxoNfFt9uToduSj7QrRg9n2_63nmddpa6IGfIPwlGNs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است امروز دو بمب‌افکن B-1B "Lancer" از پایگاه هوایی RAF Fairford (EGVA) پروازهای آموزشی انجام دهند و گرم کنن حسابی برا حمله اصلی . یکی از آنها در حال حاضر قابل مشاهده است:
B-1B "FROWN30" 86-0124
B-1B "FROWN31" (در انتظار تایید)
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20681" target="_blank">📅 17:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20680">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbm-EkHwjayH-jsQQGz3h3FAjjgSy7WyZCz-C-OwEGEymuy7oOIQxAugWiqGqf9TVLJUcKJ0cwbMxn6UEdA0c9rlJeJ8v7ydZCcnKv6UemdeIQJd1e0Ogt9wl-HK0UQJ-jJnlfnQPCmRoGQHMbgQw5TlGiFP2K6gAJMg67iJmpic6qoS4PyOGnavz5khN8zGWzJpYtloOQuyKFVVvFokBJ5dDwuQjOIYhGP_iSA-M8LVHYcWtYIVHLkCWZ90pOXTL44KDwgmB-9ZGh2ejU203miJkPVYKLjfqWU0PG_Q9WvhciXHMY_TlHdnoNJx-lzmeOf2laToO_A0C35iWLVe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش خاموش شده است. هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20680" target="_blank">📅 16:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20679">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb62efb6b.mp4?token=tSJF-Q3lprmKOHMFFaTALnQ_23M80QGIBTA7LTGlygcR65R7znRs0pKyBvbMNWvAua6WgK6StNfzW1Rq39MhUCwS8CQD3BT4535MgBMDcjjv9LVvBEs6k5VRA0Qt5ZbIdAWU2-R56hZdZpPLBiNMNCSEqfDn84eg2nhjk4nMX38QjfyXqRZnCbWPoFqASHtTBCdBjGoMUy8m09r6YBfPZyXqjzMGMHOfDu9HOh56tuJ0BDbsGI6bkpbQO_b5HZ0gzbNVWjRptijY_6yBYUyIVWp5kpBVdD61jgGS9Uvcl5OWiy9YxJYgZcFKoDap20V_laSeLztHIrZtuRHD1yB-9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb62efb6b.mp4?token=tSJF-Q3lprmKOHMFFaTALnQ_23M80QGIBTA7LTGlygcR65R7znRs0pKyBvbMNWvAua6WgK6StNfzW1Rq39MhUCwS8CQD3BT4535MgBMDcjjv9LVvBEs6k5VRA0Qt5ZbIdAWU2-R56hZdZpPLBiNMNCSEqfDn84eg2nhjk4nMX38QjfyXqRZnCbWPoFqASHtTBCdBjGoMUy8m09r6YBfPZyXqjzMGMHOfDu9HOh56tuJ0BDbsGI6bkpbQO_b5HZ0gzbNVWjRptijY_6yBYUyIVWp5kpBVdD61jgGS9Uvcl5OWiy9YxJYgZcFKoDap20V_laSeLztHIrZtuRHD1yB-9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌های توپخانه‌ای سنگین ارتش اسرائیل به شهرک المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20679" target="_blank">📅 16:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20678">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‎فایننشال تایمز: محاصره دریایی آمریکا بر ایران، صادرات نفت از ایران را متوقف کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20678" target="_blank">📅 15:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20677">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f01922dde.mp4?token=X4tenzfTqwGD97UJRxZHcJ3AktaaR5EmoZ01KnGRs-V9VB813Tu2qLKPECUjR1LMNRdFURC1yzRdlZM2IqFoWzIlfrvWjmJMkDtHyxcc-gcVDMmxXS911No9bWlzm65_XOeb8L_KVy09klx1yPzspVZGHwCGWxsZfhq9Ai76cbUcuCbfjfoWx9-i_OJxaSUjdeiE27D4OlV9RrLwviNWmCcGskZlh_OE6DGkTyNIQzzLw8MyW774NbeamLUgVO_bLLyj9EiGsNskWwATHNO7xeLZYxqnaxJzpiynZJfKpMYYwyQ-735m8VFCKvq4oGalxyojULojmDEE5sLkQ2YmyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f01922dde.mp4?token=X4tenzfTqwGD97UJRxZHcJ3AktaaR5EmoZ01KnGRs-V9VB813Tu2qLKPECUjR1LMNRdFURC1yzRdlZM2IqFoWzIlfrvWjmJMkDtHyxcc-gcVDMmxXS911No9bWlzm65_XOeb8L_KVy09klx1yPzspVZGHwCGWxsZfhq9Ai76cbUcuCbfjfoWx9-i_OJxaSUjdeiE27D4OlV9RrLwviNWmCcGskZlh_OE6DGkTyNIQzzLw8MyW774NbeamLUgVO_bLLyj9EiGsNskWwATHNO7xeLZYxqnaxJzpiynZJfKpMYYwyQ-735m8VFCKvq4oGalxyojULojmDEE5sLkQ2YmyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسنیم با انتشار این کلیپ که قدیمی‌هست نوشت: پخش تصاویری از رهبر برای اولین بار
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20677" target="_blank">📅 15:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20676">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : فیلمی که کمر خیبر شکن را شکست…  https://www.instagram.com/reel/DbwJLvzRBwp/?igsh=YzEwMDhhc3d3em9u  بررسی اینکه چگونه یک فیلمی که همه به آن خندیدند، پرده از اسرار مهمی از تکنولوژی مورد استفاده در موشکهای جمهوری اسلامی برداشت.</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20676" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20675">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آغاز ساخت پناهگاه در پایتخت
معاون شهردار تهران:چندین مرکز را در سطح شهر تهران برای ساخت پناهگاه پیش برده‌ایم و کار اجرایی آنها آغاز شده است.امیدواریم در نیمه دوم امسال بتوانیم چند پناهگاه را به بهره‌برداری برسانیم.اقدامات احداث «پناهگاه و پارکینگ ـ پناهگاه» به تصویب رسیده و اقدامات اجرایی آن آغاز شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20675" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20674">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وکیل ترامپ در پرونده حق‌السکوت، وزیر دادگستری آمریکا شد
سنای آمریکا پس از چهار ماه و چهار روز از برکناری وزیر دادگستری، با ۵۰ رأی موافق و ۴۹ رأی مخالف تاد بلانش را به عنوان وزیر دادگستری و دادستان کل تأیید کرد.
بلانش پیش‌تر وکیل ترامپ و از اعضای تیم حقوقی او در پرونده پرداخت حق‌السکوت به «استورمی دنیلز» بود.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20674" target="_blank">📅 13:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20673">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال ۱۲ اسرائیل: پزشکیان برای وادار کردن خامنه‌ای به ملاقات فوری با او تهدید به استعفا کرد.
"وضعیت اقتصادی ایران غیرقابل تحمل است"
پزشکیان می‌خواهد برای خامنه‌ای روشن کند که پریشانی اقتصادی کشور به نقطه بحرانی رسیده است، تا جایی که دستیابی به یک توافق سیاسی و رفع فشار اقتصادی به یک نیاز فوری تبدیل شده است که نمی‌توان آن را به تعویق انداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20673" target="_blank">📅 12:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20672">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmJFfTm9Z3hXAnGbUE7g0LfmjEAf_yy4DrlT95EZDDUvwhbI_XsJNNQ1djAw9EdAMacEjGHzWmrOWVKyEV_Bz5Jgqe7RvNoEhapdOuA0IxXWzB2cdvcyhS4hDP3hlVEnwI71wMcRiCATR26KgAeMuu0CO-jBUX1mbJghs193gTxH0xJoYx3f-Li-wi0_wn0lU-LtTXVYAdyzG9i5ahPCS7HndT2Lhdgy5g7rXiTD9DjUtKXOqalHNv4rd3p0VVtIV8AbnoiiD7wM4iWxaTbrf_fWGirKaM2qJdA_C0DJEQZuUEEKuhNkhSE3pf3iKw8zSHCa1I8T9De2psc1euNYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن.
علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده.
دقایقی پیش خبرگزاری‌های‌رژیم خبر کشته شدن این فرد رو تایید کردند
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20672" target="_blank">📅 12:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20671">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20671" target="_blank">📅 11:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20670">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=QENoeQyJf51UjD1pH2uAw6Svn5n7-pO_gy9UnIkgl2DQWRudWPVzPKdPUq6hlPet2Ee9yJGA4x8Axy9l1T50p16XU6aZxs-0NA5J-6yxUOmc0bZC1DjsMIA-eq63yso43IE13k2sW9hzm3EZ9UMHfKUcusX87cZrF3oSYOVQShJo-Glw5pHOWcsuowYSGHvFrNKLSv3Tk5eCqiKzwzDnyg68Ineds7l0qIZWHmGd3GyFnMBXM24IdEau-8irTnPkfAWJZqcqDLRQkd_36TzNJyYbU0XDCTI3WNx9LMTRK__eMJQjcaGNEcUnZMfbbsS6cwI98kUc2nS5HoUxnk38yYC9tXIrIDV88TmVhyaNjujEDqBEoH-lL0WG1_DNByrTGB98PYjlA7laib3A5uU_xYcjiyVW97GVJHR6zkstueJa_-Fgf0UmuA_gzdcBMPV8KYFbnrY-2YrXuM7Yny6xydNpofEBwK_w4YNfzxUFw9mhqwpEZ1bdqj54enUFS7k3Ee_UeFH4EEdES5lHmGPGbfaMdrPrCf9QVkFeTayM5eJXongXzWl4kJW-ThYIJADbR-rBm0I2nbeTWJy4ffS1vQqApW6Y7uqksPDsU74b6bJM5svlA2z9wx3tF7TNrLKNQlCeXBFvudl7oyL7hDhW5ncjr5zk42Z_HQvwpODcj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=QENoeQyJf51UjD1pH2uAw6Svn5n7-pO_gy9UnIkgl2DQWRudWPVzPKdPUq6hlPet2Ee9yJGA4x8Axy9l1T50p16XU6aZxs-0NA5J-6yxUOmc0bZC1DjsMIA-eq63yso43IE13k2sW9hzm3EZ9UMHfKUcusX87cZrF3oSYOVQShJo-Glw5pHOWcsuowYSGHvFrNKLSv3Tk5eCqiKzwzDnyg68Ineds7l0qIZWHmGd3GyFnMBXM24IdEau-8irTnPkfAWJZqcqDLRQkd_36TzNJyYbU0XDCTI3WNx9LMTRK__eMJQjcaGNEcUnZMfbbsS6cwI98kUc2nS5HoUxnk38yYC9tXIrIDV88TmVhyaNjujEDqBEoH-lL0WG1_DNByrTGB98PYjlA7laib3A5uU_xYcjiyVW97GVJHR6zkstueJa_-Fgf0UmuA_gzdcBMPV8KYFbnrY-2YrXuM7Yny6xydNpofEBwK_w4YNfzxUFw9mhqwpEZ1bdqj54enUFS7k3Ee_UeFH4EEdES5lHmGPGbfaMdrPrCf9QVkFeTayM5eJXongXzWl4kJW-ThYIJADbR-rBm0I2nbeTWJy4ffS1vQqApW6Y7uqksPDsU74b6bJM5svlA2z9wx3tF7TNrLKNQlCeXBFvudl7oyL7hDhW5ncjr5zk42Z_HQvwpODcj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ویژه آژیر خطر از فاکس نیوز: سربازان آمریکایی در جنگلهای بنگلادش تمرین آمادگی می کنند, حکومت ایران یا توافق را میپذیرد یا بمباران میشود. آیت الله گی قدرت پدرش را ندارد و اختلافات بالا گرفته… و عناوین دیگر که در این ویدیو خواهید دید
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20670" target="_blank">📅 10:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20669">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3moa5LzIhvDj3sUIpHFFx1mcY2XtA9wQifAjsHxmnuQd05gZ9tos53ov2myVBtcHdI_CKKVaqYYBMdTAOxzUmuNwAHOaopDJ_-01oHUeAX2XrYnEHolJ9znpDosATrBmEw1FNHBtztJSenCd16jfbbXevevpLZA_5FdBdCxNfNvzC43ZykkFiUpO5cyOsdRs4qjZU7wH-vr9HupzfBAzlHEIEd5aQcYGlAXfOJtbDWqZUwGzOr-nF-ND7E_JpmUVV2aKtVxkdBRgcm7BK55tEU9QrZ4wWP2UbIgWhqqTFgH6ZnAtUm0cKRR8m49q3pm_Dxb-3InEES3FuRFI_AMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن روحانی توی خونه خودش یک هیئت دولت خونگی ساخته با هم جلسه تشکیل میدن و خاله بازی میکنند!
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20669" target="_blank">📅 09:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20668">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سفر مکه
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20668" target="_blank">📅 02:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20667">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_XUG_yDuJJ_FKu6qW2sEx0vLzrzF1KTvW7tXYLEBU70rAAQAL4JMQRLq-TwAQNSqjf2CgFcCbwda5MGKAhoaqifKRWQISScy5kyWhNCVv9_rI_0UVZMqzVa3nvbuYWVw_hZ3fMaoCdIB5_LT-dQo18qEJ_xQ3UeFBe0jrBheHTmGGQudaCHpLtcPIbDx58SaDpeWz30kOZVBJ3omDAx8TUaYHihAkfsobk2oQR2hlkgm6XT01_BfjCFedXTcj9_rW90eACrbRPWZpONiuZA0AWCmjyTuoWsay6yF1NNRKBfYZNaSjMvq29rJnCIDrz1vns9qJOtYwme05y3GUl0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین به ترامپ : کلکشون رو بکن
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/20667" target="_blank">📅 01:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20666">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20666" target="_blank">📅 00:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20665">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هربار نا امید میشم یهو میای و با انرژی ماوراییت میکشی بالا منو. نشسته بودم در اوج نا امیدی عرق میخوردم، کانالتو باز کردم و ویدیوی آخرتو دیدم‌ و چسبیدم به سقف. خیلی خفنی خیلی آدم حسابی هستی عمرت طولانی تنت سالم بمون برامون یاشار
❤️
🧿</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20665" target="_blank">📅 00:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20664">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">هربار نا امید میشم یهو میای و با انرژی ماوراییت میکشی بالا منو. نشسته بودم در اوج نا امیدی عرق میخوردم، کانالتو باز کردم و ویدیوی آخرتو دیدم‌ و چسبیدم به سقف. خیلی خفنی
خیلی آدم حسابی هستی
عمرت طولانی
تنت سالم
بمون برامون یاشار
❤️
🧿</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20664" target="_blank">📅 00:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20663">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d253696.mp4?token=J6N8k4QA0RYn8uODOvVKr4_49YpOAKHHdrHgDeY1ilYnOR6D1-AP9kQRYp1OadK1k3z_dK1dBgqi948d8aDcg_nse4B3CesnfYjXKKAJF67ibPat1icy6JRl13iTkwUERzmFzFO8DTk1KDGVSMjPomHl8QPloOqT2A-a1aqJaAc6IcKNR1t0wAjdX-uaS40RU2ocx2mA7_lQc_WUBl_hGVySF70ko23Yk7xVqIWwOIVU5Fs4V03xyrh5WaHazCnk2iCqpOHKJftz1ew5AXqaaYBI31q9K9PbQP8Eezn-i_0aEPE1aTPiBQeHL4VVv5VGN0x2YUZpG2kCyp9jv85_9CUdbTw91LzgZjftMbmq7hFtrmFT97fAO2VPQmLzm0ZQv4RkPyflIB4GnWRdtkwfQKXE9S3NAkse6n32jiQYtHPY3WuF2wZhq9n9IbbM9QasiMIA4CaG4kqYL1PTegvGJ29j4ZRre1ti9OVu1RxYApCsZRZFvBV9LuVJgxvLaaw6HAWt-OdY9e3wsO0PgaA1lsVXpAuYd-dkgqjmzSWcPi3znKrXYFD1LbNRqmZE4jWFinwj_Bm8bk4frAHhSpzrdivW_PJtYM8_dEwQucgN4P041kBsARgTrfz1V4PYie16XRt1Z4YNJPD8G4idTsyl9nL1ZFZdD0ncPnQXh7znY7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d253696.mp4?token=J6N8k4QA0RYn8uODOvVKr4_49YpOAKHHdrHgDeY1ilYnOR6D1-AP9kQRYp1OadK1k3z_dK1dBgqi948d8aDcg_nse4B3CesnfYjXKKAJF67ibPat1icy6JRl13iTkwUERzmFzFO8DTk1KDGVSMjPomHl8QPloOqT2A-a1aqJaAc6IcKNR1t0wAjdX-uaS40RU2ocx2mA7_lQc_WUBl_hGVySF70ko23Yk7xVqIWwOIVU5Fs4V03xyrh5WaHazCnk2iCqpOHKJftz1ew5AXqaaYBI31q9K9PbQP8Eezn-i_0aEPE1aTPiBQeHL4VVv5VGN0x2YUZpG2kCyp9jv85_9CUdbTw91LzgZjftMbmq7hFtrmFT97fAO2VPQmLzm0ZQv4RkPyflIB4GnWRdtkwfQKXE9S3NAkse6n32jiQYtHPY3WuF2wZhq9n9IbbM9QasiMIA4CaG4kqYL1PTegvGJ29j4ZRre1ti9OVu1RxYApCsZRZFvBV9LuVJgxvLaaw6HAWt-OdY9e3wsO0PgaA1lsVXpAuYd-dkgqjmzSWcPi3znKrXYFD1LbNRqmZE4jWFinwj_Bm8bk4frAHhSpzrdivW_PJtYM8_dEwQucgN4P041kBsARgTrfz1V4PYie16XRt1Z4YNJPD8G4idTsyl9nL1ZFZdD0ncPnQXh7znY7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت قرمز ۱۱ سوخترسان و ۱ آواکس در منطقه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/20663" target="_blank">📅 00:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20662">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muF2jc0Gp6KDCZzFcRZ9uCYrDKG-yy4trhHhgRzHCTVdcKNVbTawu-BHmfLNRXC_Bg3ZLyC6JDcJkYkDSD2Tb-0Og7QMND1UflzwweLH0OWyWr6-p98u6HmzpxwD9GzszBJWGNvN6IVzqQhMgHhR0ob30fBvCpXES4Nh3RUtXiPkgwsVinC-YGyRptMAIBfPTa8hPFN4ymFDdwXA_PjUQxjkt1ZcgD7slb5QoPnmcZnOZqiFD5TTJmov75XkssJdTu6xKBOovEHdl9FhPbsglm0p9eAgvueJM3YpnxRzCRkbcsDmSJF8ikANG4p1i9PyvNLLYJL2DfNSaGs0s6a9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : فیلمی که کمر خیبر شکن را شکست…
https://www.instagram.com/reel/DbwJLvzRBwp/?igsh=YzEwMDhhc3d3em9u
بررسی اینکه چگونه یک فیلمی که همه به آن خندیدند، پرده از اسرار مهمی از تکنولوژی مورد استفاده در موشکهای جمهوری اسلامی برداشت.</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20662" target="_blank">📅 00:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20661">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:پیروز جنگ غنائم میبره، منم غنائم  ایران عزیزو میبرم
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20661" target="_blank">📅 23:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20660">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db8aff1a3.mp4?token=KVHfUewSLAxPuFprc-pFROLRcdY8vjcmhW2jZoUmfq728BaugtoOEC23oXFG2yR96qo75953ANVDU1OKlVEx27lw0BG07tW1RyXieUup8t1vFci8906AETHE_-nLzOgxpGYw8RYXEYtWQyeO1yE4SWwVirlmk4deqfYMb6ErVRVGRE5CV4fCkDMoENECSTCxQdzQb2aYvKVWl61u3Ta23YiwabYx8eunnH-osTn4zTjjqP-4FhcRRtGIsIEcAET-DUUOEi6IoJEDf12TQUePphP3o7FyjGHuLLXJZq-YXS2cQGOl_o65t5gjRfQLP1lI4Af418duAcBNwTAwMaqw-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db8aff1a3.mp4?token=KVHfUewSLAxPuFprc-pFROLRcdY8vjcmhW2jZoUmfq728BaugtoOEC23oXFG2yR96qo75953ANVDU1OKlVEx27lw0BG07tW1RyXieUup8t1vFci8906AETHE_-nLzOgxpGYw8RYXEYtWQyeO1yE4SWwVirlmk4deqfYMb6ErVRVGRE5CV4fCkDMoENECSTCxQdzQb2aYvKVWl61u3Ta23YiwabYx8eunnH-osTn4zTjjqP-4FhcRRtGIsIEcAET-DUUOEi6IoJEDf12TQUePphP3o7FyjGHuLLXJZq-YXS2cQGOl_o65t5gjRfQLP1lI4Af418duAcBNwTAwMaqw-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به خبرنگاران و حاضران : اگر امکان داشته باشد، اگر بتوانید به سرعت از اینجا خارج شوید، من سپاسگزار خواهم بود، زیرا ما یک جنگ داریم که باید آن را به پایان برسانیم. این دلیل من برای خروج کمی زودتر است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20660" target="_blank">📅 22:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20659">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓮𝓡𝓦𝓲𝓷🦅</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX7kPMFCB0A9qEP0sSqWvjE6GNuJzUJyFa_hf27XmnHMPiHElojYdGKP0OIXJWjJfvMSCGtFOnTBdnH6FXyJb_L9wc85JHZxJuJSEtJZCdMo2aR-RDRMEEg-2fvDnNjvTBLR2nZ0OJb8NzvpODjxvGoozEp5VeScJjkI1weatbLEfFGRuOgF8FBFI7PDXAQfX163qVdfOcztb2722JKGz9WgLKHh_q7AQSY-9s1guTXxdij3yoHc5olHMYzU8CtsEut-6XPRMTTX_lmtblg6-7x38owbbaK_lMLknrfgWGdTklnIYsL9RX8OI0T5rkQmxFuKvnqJ7fY-2Q4Ws2pnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20659" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20658">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6r-NQDDqkaV3pRPvLfWjPzDixIXgGLNW9O30gS3chrVoDyWzJTmaIyZ8vN1D4jmXFwzf0-94ApOHmwy3aYBzhj2hsYvQbAK8D-rRY3QIopWP6Xe-_0jTCYNlEBEBLOb69mBuJtKgjGM5kyF2_7_ZNh1zcu7owR1fbdM4TTAEADOQma_lh1Ox_EdxikTY7Bpox2cv1qevjuytaygHd-vvznOEaw3gSobQW0yxFRs4s98He49GG5AvunUiveBd-6mS5Vk02_SmPqZvsqbCp22BbHUXhf1j-f8LVaBeMfPXRe_gaK9MzxAGMnrdff21YxTJ0HrtAcUZCqbt77497_v4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخترسان از تل‌آویو بلند شدند و به سمت خلیج فارس می آیند. همچنین ۵ سوخترسان امریکایی و یک سوخترسان هم از کشورهای همسایه خلیج فارس در منطقه حضور قاطع دارد @WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20658" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20657">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رسانه آمریکایی WIRED گزارش داده است که پنتاگون در آستانه امضای قراردادی چندصد میلیون‌دلاری با شرکت AeroVironment برای خرید حداکثر ۲۰ سامانه لیزری ضدپهپاد قرار دارد؛ رقم حدود ۴۰۰ میلیون دلار ولی هنوز رسماً تأیید نشده است. سلاح اصلی این برنامه E‑HEL(لیزر پرانرژی پایدار؛ سامانه‌ای برای سوزاندن و ازکارانداختن پهپادها با پرتو لیزر) است که برای انهدام پهپادهای کوچک، پهپادهای انتحاری و اهداف پرنده گروه‌های ۱ تا ۳ (رده‌بندی ارتش آمریکا بر اساس اندازه، وزن و برد پهپادها) طراحی شده است. نسخه پیشنهادی آن بر پایه سامانه LOCUST(سلاح لیزری متحرک برای مقابله با پهپادها) توسعه می‌یابد و روی خودروهای ISV(خودروی سبک تاکتیکی برای جابه‌جایی نیروهای پیاده) و JLTV (خودروی زرهی سبک چندمنظوره برای عملیات نظامی) نصب خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20657" target="_blank">📅 22:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20656">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز: ایالات متحده به فروش ۵۲۵۰ موشک دفاعی به بحرین، کویت، قطر و امارات متحده عربی موافقت داد.
این اقدام با هدف جبران کاهش ذخایر موشکی سیستم پاتریوت این کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20656" target="_blank">📅 21:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه پلتفرم‌های خرید و فروش رمزارزها که از سپاه پاسداران پشتیبانی مالی می‌کنند، اعمال شد.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20655" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اتاق جنگ با یاشار : صدای گشت زنی جنگنده های جمهوری اسلامی در آسمان بندرعباس هم زمان با افزایش حضور سوخترسان ها و متقابلأ جنگنده های رادارگریز آمریکایی
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20654" target="_blank">📅 21:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20653">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شبکه CBS :  مجلس سنای آمریکا به طرح قانونی درباره تحریم‌های روسیه و ایران رای مثبت داد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20653" target="_blank">📅 21:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20652">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20652" target="_blank">📅 21:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20651">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20651" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20650">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamir</strong></div>
<div class="tg-text">امشب بیدار بمون</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20650" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20649">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamir</strong></div>
<div class="tg-text">داداش دعا نویسم گفت امشب جنگ خواهد شد</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20649" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20648">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMc3SdBrca_hDPLOVTGKdF2vcWXe83_cYRF11sfLZHFoI3lM6Ncthr2hgslAH1GnbPqgs-FNDNUdRlucpTGZ5kINJuSKDhtZKDTjqV4HNYiHMxi5gsIeQfs1jkrETLMqY7cQIftPvvZHFRnbeE6zOvrh-IR9OsxjYdg_wxzqeccZFjagAQ3jwfFTSDC4G8kMGT42BkEwTyCAcv5MHpx7Zt7kGtkEq2F3xWKpNNzSL8_JNV6cSxDpw9QS90prl24vje-JFmtlkkZw5dT1qJ22TUr2CsPf1gn4xjfcXpgvk-1S6dPFI7YMJIGC8RRpLaXAJNRREqTRyAJl-DvBHAD9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخترسان از تل‌آویو بلند شدند و به سمت خلیج فارس می آیند. همچنین ۵ سوخترسان امریکایی و یک سوخترسان هم از کشورهای همسایه خلیج فارس در منطقه حضور قاطع دارد
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20648" target="_blank">📅 20:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20647">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7RYTvX5AqSCDCbJtU3GQAtm2RNA3nODM7PUvw46WHKcNungNzSWIlYkU5CRMS0AbABZbAhMfdAc6uBl7CH8mr0uFcGXsaE2La8MVbK0sCYHf3cYawfLMiuSeIm95ENSiPqQZTrHCpH4uG_geHTS3HVL0k67w9rWDX9LFpFwL98ezB1LgObp4ayZQfbeYFCeZgZfJUFkZ0pefrVdCWinwrXWB4w45JH_4Jh-3kiEvHzeWKAXR6teSckMLZfxZSlWqrezOGksy38Hq2LxFjW3iWDWxHKrNQzhvl_7qa2Gp-AzvFfRP-zRxDvBP8Y-i1HPqp-oGko23HxSAvbczMVdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : خدمه پروازی یک فروند هواپیمای سوخت‌رسان KC-135 نیروی هوایی ایالات متحده، در حال سوخت‌گیری یک فروند جنگنده رادارگریز F-35A در آسمان خاورمیانه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20647" target="_blank">📅 20:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خزانه‌داری آمریکا: تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت
تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.آنچه در دو سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت خود کم خواهد شد.این تنگه به یک آبراه معمولی تبدیل خواهد شد، و من معتقدم که بیش از ۵۰ یا ۷۰ درصد از انرژی که در حال حاضر از طریق این تنگه منتقل می‌شود، از طریق خطوط لوله زیرزمینی منتقل خواهد شد
‏در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20646" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزارت دفاع آمریکا پنجمین مجموعه از پرونده‌های مربوط به پدیده‌های ناشناس هوایی و بشقاب پرنده ها رو منتشر کرد در همین راستا شبکه خبری CBS دقایقی‌پیش مصاحبه انجام داده با «آوی لوئب» که ترامپ او را مأمور و نماینده تحقیق بر روی این پروژه کرده، از دست ندید.با زیرنویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20645" target="_blank">📅 19:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20644">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سناتور جمهوری‌خواه تد کروز، درباره جمهوری اسلامی : اگر شما یک اسلام‌گرا هستید که از آمریکا متنفر است و سعی دارد ما را بکشد، من از اینکه شما یک کشور یا ملت را رهبری کنید و منابع لازم برای کشتن آمریکایی‌ها را داشته باشید حمایت نمی‌کنم؛ این جایی است که ما باید بر آن تمرکز کنیم؛ حال، چگونه فروپاشی حکومت را رقم بزنیم
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20644" target="_blank">📅 18:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20643">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=ZvTFOYjAvNDhaltyTncPFDU68TTfEVjKBhwYlPjl6LPhFrAAj29VVl4d_50HeO9Vaw6sb-eKoXnzPWEvGrZ3MNp01Z1mj0rYYoVi0kWDNYpoY10qjGkNPlIlFgXL3LBjtogioR6ulUBzA2wNtP_eLj_Gfi0QWn8aAkun9IDJcmRlGpsfWXDB10zUyjjCTELuVYMzoy9xcZyB11ijY1Wfi7SShoC61EJDEyoW0RTrORcEOTjMpMwqNfz6hVHV2pH9tInWYekPHAaU4jpzcH0w3pkUqnUCeci6GzSgMzF_2EVvJsutzlOTpWer8K3T1i01171fn-3beqUOmYsPaK1wLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=ZvTFOYjAvNDhaltyTncPFDU68TTfEVjKBhwYlPjl6LPhFrAAj29VVl4d_50HeO9Vaw6sb-eKoXnzPWEvGrZ3MNp01Z1mj0rYYoVi0kWDNYpoY10qjGkNPlIlFgXL3LBjtogioR6ulUBzA2wNtP_eLj_Gfi0QWn8aAkun9IDJcmRlGpsfWXDB10zUyjjCTELuVYMzoy9xcZyB11ijY1Wfi7SShoC61EJDEyoW0RTrORcEOTjMpMwqNfz6hVHV2pH9tInWYekPHAaU4jpzcH0w3pkUqnUCeci6GzSgMzF_2EVvJsutzlOTpWer8K3T1i01171fn-3beqUOmYsPaK1wLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شهباز شریف، نخست وزیر، محمد بن سلمان بن عبدالعزیز آل سعود، ولیعهد و نخست وزیر عربستان سعودی و رجب طیب اردوغان، رئیس جمهور ترکیه نماز جمعه را در قصر الصفا اقامه کردند. در این مراسم، محمد اسحاق دار، معاون نخست وزیر و وزیر امور خارجه، سناتور محمد اسحاق دار، فرمانده ارتش و رئیس نیروهای دفاعی، سپهبد سید عاصم منیر، و مقامات ارشد سعودی و ترکیه نیز حضور داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20643" target="_blank">📅 18:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20642">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHp7hei7qTJ2i51R16YOpA0GYy4BisfptHM9UktrFCg5hNAOp-HkUKutiB3OSB80fxePIoB61-YqNFu2Wt8BKBKqlXG0XXJ9iilPgwKqNB6x0kewVCrzmoZhhkuR3f0NOQ3z76woBFTubrYFzIb6BcaMGQFiK1evwGaXl8lrjnC3aAyrmhCdooA-cEtxtBViq-lMdkI2UFTgDtkUNR9gSrPjwgse7ipU8BzyVvUJ32c9Gjb9kULtXPFqSAUoq5NbjAersyN5kF6gmVhSApFOXs7sY36z8W48CtHTTEWKreeflYYoUQu9ZIcxHZxfq_pNn2rHqs26xae-0awEpMuNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20642" target="_blank">📅 18:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20641">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شبکه کان اسرائیل: ایران صدها موشک پدافندی دوش‌پرتاب از روسیه و چین دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20641" target="_blank">📅 17:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20640">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20640" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENenh-Kgf43vp1H-Z2nZgbjZESC8e-gi3nBZO52n-KTLudWOVTPdKcBT66-YWNqzQwQnrgIBPQmfwa0YaHgzpdmyke-LqD_8etbvoHO47umFOLXDl1IPnV4zZU5proZ3PTulzEnROnJd4oqah8zsyIymU7UE-dBJkoRbHU-ZUFVlYOLUjHhNPZirgP5F9fBT6UDEeqiKdGXUvwQMbencLqTepAxGTYiaHetNFoYcH6Cdt19x_uXd453RFgz7HSSj0Iw7DNgsm8XyqLGvHg2pC03XVQZlDuRM0Yy8xTr_cdaBMTUNEE-LfwSxrK9uW40W6oeab-RwPKd8kEMqO22zuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست وزیر جنگ متنی از مقاله که ترامپ هم دیروز آن را منتشر کرده بود منتشر کرد. این مقاله فقط دیدگاه نویسنده آن را بیان میکند نه یک گزارش خبری.  متن عکس : ترامپ در جنگ ایران پیروز شد پس این هم واقعیت؛ همان حقیقت تلخی که تردیدکنندگان دوست ندارند درباره‌اش…</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20639" target="_blank">📅 17:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20638">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏نیویورک تایمز: برنامه هسته‌ای رژیم کند شده اما متوقف نشده است
‏ بازرسان سازمان ملل برآورد می‌کنند رژیم همچنان ذخیره‌ای از اورانیوم نزدیک به درجه تسلیحاتی در اختیار دارد که برای ساخت سریع ۹ تا ۱۰ بمب هسته‌ای کافی است. داریل کیمبال، مدیر انجمن کنترل تسلیحات، گفت سیاست فشار حداکثری و اقدامات نظامی دولت پرزیدنت ترامپ نتوانسته توانمندی هسته‌ای رژیم را از میان ببرد. الی گرانمایه نیز هشدار داد در نبود نظارت بین‌المللی، رژیم می‌تواند ذخایر فعلی اورانیوم خود را به سرعت تا سطح مورد نیاز برای ساخت سلاح هسته‌ای غنی‌سازی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20638" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20637">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اینستاگرام رو  هر روز میززند و باز‌میکنم دیگه اعلام نمیکنم حتی ! الان برگشته
🤣
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20637" target="_blank">📅 17:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20636">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTt-N_UI7M5ZzESvxyVxT8C1HM2wT_1zf00ovm4qNrxqZOxDPtAO15gcRw4Swv0IoaBYxRWU1U5KWnGPWHQ2YbWzHy9FLuXUhKZVVqi-I2pp9KlW445Z0eIypiYhI9NOARqeemSMy0evBT_jY3O4AtEv_XAkmwo2TCB41NmITwtCLM-gjQ6AcBJDLz12Gl0n6PFivGtBp_GdFqKQO1hxBl0SOubNPzrcSU-NpDr8F8aMnA4MEooBJQSo0hjG5nCHSv3kbut-rL70ArIpk5xIF8w_TjzHgGINXXSS8D6BNXdmxVkgBiLAZH8MxpK5cGH_STOC1x9hL-YwkELjMq_69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست وزیر جنگ متنی از مقاله که ترامپ هم دیروز آن را منتشر کرده بود منتشر کرد. این مقاله فقط دیدگاه نویسنده آن را بیان میکند نه یک گزارش خبری.
متن عکس : ترامپ در جنگ ایران پیروز شد
پس این هم واقعیت؛ همان حقیقت تلخی که تردیدکنندگان دوست ندارند درباره‌اش صحبت کنند.اگر ترامپ در این جنگ در حال شکست بود، هیچ‌یک از این ابتکارها و تحولات در حال وقوع نبود. آنچه امروز شاهدش هستیم، افزایش نفوذ آمریکا، گسترش مشارکت‌های منطقه‌ای و شتاب گرفتن روندی است که ترامپ برای برقراری صلح و ثبات بلندمدت در خاورمیانه در نظر دارد. این‌ها نشانه‌های شکست نیست، بلکه نشانه‌های دگرگونی منطقه در مقیاسی بی‌سابقه هستند.
رسانه‌ها و تحلیلگران می‌توانند هر روایتی که می‌خواهند ارائه دهند، اما تاریخ‌نگاران خواهند نوشت که ترامپ تأثیرگذارترین عامل در بازآرایی خاورمیانه در دوران معاصر بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20636" target="_blank">📅 17:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20635">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به گزارش فایننشال تایمز، به دلیل محاصره دریایی آمریکا، حداقل یک هفته است که هیچ نفتکشی در جزیره خارک، پایانه اصلی صادرات نفت ایران، بارگیری نکرده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20635" target="_blank">📅 16:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20634">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شبکه الجزیره گزارش داد نشست لبنان و اسرائیل با میانجی‌گری آمریکا در رم بدون هیچ پیشرفت ملموسی پایان یافت. اسرائیل با پیشنهاد عقب‌نشینی مرحله‌ای از جنوب لبنان مخالفت کرد و تأکید کرد تا زمانی که سازوکار قابل‌اعتمادی برای خلع سلاح و راستی‌آزمایی حزب‌الله ایجاد نشود، با خروج بیشتر نیروهایش موافقت نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20634" target="_blank">📅 14:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">«توافقنامه دفاعی مکه» رسما امضا شد : هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
محمد بن سلمان، شهباز شریف و اردوغان توافقنامه دفاعی مشترک میان ترکیه، پاکستان و عربستان را امضا کردند.هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام تجاوزکارانه است
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20633" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0293ab00f0.mp4?token=LsJH-2aPiUe6ZtnplAShIhCtT8FH3HG8AMZrVgy2uNvQE7JFECDrebbR1_erDlrZLi0e5tl1Ka5FX_LaqE4U49rJdwmUdBOgRsOh1RMUTobxqfWlXgJYh6I1MVxMqvBzm4fHcO-NEZmovn3nQiWY-I8_F25dvfTYJJ4s-yFt1neB8Tv4-dDRm2Z0UyGK-WgCiG71gssZmc1bA_towGPXi1xnq3Mukm-_hd4YNifdIFvg3Hz0IQOmIL7-HGn2tsN6_YvFpshce_zxnA-B_IJhAjcT0zrWvOH5q-NW5q7aCHJWLeh0WFo1gk1wnKSGFk9x9iAZ3Y0S9QjD1sqPSgv1pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0293ab00f0.mp4?token=LsJH-2aPiUe6ZtnplAShIhCtT8FH3HG8AMZrVgy2uNvQE7JFECDrebbR1_erDlrZLi0e5tl1Ka5FX_LaqE4U49rJdwmUdBOgRsOh1RMUTobxqfWlXgJYh6I1MVxMqvBzm4fHcO-NEZmovn3nQiWY-I8_F25dvfTYJJ4s-yFt1neB8Tv4-dDRm2Z0UyGK-WgCiG71gssZmc1bA_towGPXi1xnq3Mukm-_hd4YNifdIFvg3Hz0IQOmIL7-HGn2tsN6_YvFpshce_zxnA-B_IJhAjcT0zrWvOH5q-NW5q7aCHJWLeh0WFo1gk1wnKSGFk9x9iAZ3Y0S9QjD1sqPSgv1pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
: فقط همین را می‌گویم؛ اگر اوضاع به همان سمت برود، آن‌ها این کشور را نابود خواهند کرد.
مجری
:شما دیروز، وقتی درباره نوادا صحبت می‌کردید، گفتید اگر اشتباه نکنم، ممکن است قیمت بنزین دوباره کمی بالا برود، و بعد گفتی…
ترامپ:
نه، نه. این فقط در صورتی است که مجبور شوم یک حمله دیگر انجام بدهم.
مجری:
یعنی…
ترامپ:
قیمت‌ها فقط در صورتی پایین می‌آید که به توافق برسیم. آن‌ها می‌خواهند توافق کنند
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20632" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20631" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20630">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پرات ریخت ؟
😈
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20630" target="_blank">📅 12:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20629">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20629" target="_blank">📅 12:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مجری : مردم میپرسند کی‌اینا میرن؟  نوستراداموس هم نتونست بگه! مانوک : انقلاب تقویم نداره … I LOVE YOU @WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20628" target="_blank">📅 12:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رویترز: نگرانی درباره تنگه هرمز قیمت نفت را افزایش داد
قیمت نفت امروز در پی افزایش نگرانی‌ها درباره شرایط بازگشایی تنگه هرمز بالا رفت؛ زیرا ایران با همکاری عمان پیشنهادهایی برای محدود کردن عبور برخی کشتی‌ها و جریمه ناقضان قوانین مطرح کرده است.
قیمت
نفت برنت
با افزایش
۸۵ سنت (۱.۰۳ درصد)
به
۸۳.۳۴ دلار در هر بشکه
رسید
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20627" target="_blank">📅 11:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e767e0b.mp4?token=hQ_TO3gr5HXHTiRQpKPTWTc0sM7aN_LSyge7-tXyqkoFQQAvlYtbl8fWh9azApF-6-7Y0wCtClbAeot1yYTF2vID37Cu0Nu9_pAHum22OFB8KyawARQ37Jp-9EcTfFTZ3FW7lFD764giDQRLIF6cox1XJdJzhZhAm-imcRYomSNcHfGogNxavibVMoTdmh34NUn7dSLnCnVA14LF8ClsmlPECv5OX4ImgJNiaLgyklZnq1eWA_Chkib0mhMygOKw0LdVjaGQvZBd5tJkBdGV-xjhtprwrVyN5JeG810k_iyX1jowLsjpwpNvd3VAzfPDsT7RRtProCxvA_uOAmhH5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e767e0b.mp4?token=hQ_TO3gr5HXHTiRQpKPTWTc0sM7aN_LSyge7-tXyqkoFQQAvlYtbl8fWh9azApF-6-7Y0wCtClbAeot1yYTF2vID37Cu0Nu9_pAHum22OFB8KyawARQ37Jp-9EcTfFTZ3FW7lFD764giDQRLIF6cox1XJdJzhZhAm-imcRYomSNcHfGogNxavibVMoTdmh34NUn7dSLnCnVA14LF8ClsmlPECv5OX4ImgJNiaLgyklZnq1eWA_Chkib0mhMygOKw0LdVjaGQvZBd5tJkBdGV-xjhtprwrVyN5JeG810k_iyX1jowLsjpwpNvd3VAzfPDsT7RRtProCxvA_uOAmhH5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : مردم میپرسند کی‌اینا میرن؟
نوستراداموس هم نتونست بگه!
مانوک : انقلاب تقویم نداره … I LOVE YOU
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20626" target="_blank">📅 11:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سی‌ان‌بی‌سی : به نظر می‌رسد توافق ترامپ در وضعیت وخیمی قرار دارد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20625" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏خبرگزاری آناتولی به نقل از منابع امنیتی گزارش داد رجب طیب اردوغان، رییس‌جمهوری ترکیه، برای سفری یک‌روزه راهی عربستان سعودی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20624" target="_blank">📅 10:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20623">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJD8-Zfw26uzU6LBRuRn1V8l-rthlgQWyYDS75nMRzwEKXFXf__yC1_hNlpvKuUdYReoUBaqbjvg1XGIVeyBs8gKDBH_6rSpy2AFZh3b__NeyyI1TPM6Okv19bhS_1ew-Ujv2m0sduBUhprTnIaWKuSUx4fTQ30Nx1FitRb5Ve0y_DxH_Z0T-GGbrb29rzs40FjecYH_VWi8CPomlNrG88xBsKna6ls2ywUibinXXZOsx0NO-GxbY7t-7XEIUP_AY-tKjNZGXdHUUBIky3ubHM3RSOcI_T3kci5Z-Zmc8f73M407P3xJi3xVyXs5jQFWfTQBFLarLfm_7PDrrm-aLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏لکه های در تصویر منابع نفت و گاز در دریای کاسپین , طبق تقسیم‌بندی جدید بیشتر این منابع به کشورهای دیگه واگذار میشه
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20623" target="_blank">📅 10:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پس از آنکه وزارت حمل‌ونقل اسرائیل پارک کردن تعداد بیشتری از هواپیماهای سوخت‌رسان آمریکا در فرودگاه بن‌گوریون را ممنوع کرد، به آمریکا اعلام شد که هواپیماها باید در پایگاه‌های نظامی نیروی هوایی اسرائیل مستقر شوند، نه در فرودگاه غیرنظامی بن‌گوریون.شبکه i24News…</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20622" target="_blank">📅 09:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">instagram.com/Yashar – Ruhollah zam and Msoud Molavi @WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20621" target="_blank">📅 09:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=a6RbM48AlUPwzsXJu6A9pKgM-yuRBMCxKoi8pgs0uNO6KfAqdjVZwWv9r6hK7hAjWSPBDmbIJ4EehyrFVIJOSoJI4oS1u7pjuj9qIaBQeG0I-FTcms038kLaWEAoCNE-g8CNZi9mtoWTo7CLI9_grCqbxQhPNE9QBfOggyeEGefFdqPnzz1L4MXa-02oa8n2Jdl_iuojHcLpHppYcL6l-LwhjQU1ylcU5S6RZgBxtMST01z2WbDTA0UK8eYvy-2Nx68R0AQsllXspt728GwAEcoZoqcCny14L3gZdj62v9qGxjbf85w2AW233CudcO_UTpdQUpclr2Rlt7m49WDnG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d2de94a7.mp4?token=a6RbM48AlUPwzsXJu6A9pKgM-yuRBMCxKoi8pgs0uNO6KfAqdjVZwWv9r6hK7hAjWSPBDmbIJ4EehyrFVIJOSoJI4oS1u7pjuj9qIaBQeG0I-FTcms038kLaWEAoCNE-g8CNZi9mtoWTo7CLI9_grCqbxQhPNE9QBfOggyeEGefFdqPnzz1L4MXa-02oa8n2Jdl_iuojHcLpHppYcL6l-LwhjQU1ylcU5S6RZgBxtMST01z2WbDTA0UK8eYvy-2Nx68R0AQsllXspt728GwAEcoZoqcCny14L3gZdj62v9qGxjbf85w2AW233CudcO_UTpdQUpclr2Rlt7m49WDnG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز سی‌وچهارمین سالگرد درگذشت دکتر فریدون فرخزاد
۱۵ مهر ۱۳۱۵ متولد شد و در ۱۶ مرداد ۱۳۷۱ آسمانی…
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20620" target="_blank">📅 09:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مارک لوین : رژیم ایران باید نابود شود وگرنه این [وضعیت] هرگز متوقف نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20619" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">العربیه : یک مقام ارشد سعودی می‌گوید چندین گزارش اطلاعاتی معتبر نشان می‌دهد که میان حوثی‌ها، شبه‌نظامیان عراقی و سپاه پاسداران انقلاب اسلامی ایران (IRGC) برای آماده‌سازی حملاتی علیه عربستان سعودی ائتلاف هماهنگ وجود دارد.
این مقام این گزارش‌ها را «تکان‌دهنده» توصیف کرد، زیرا در حالی منتشر شده‌اند که ریاض در تلاش برای کاهش تنش‌ها است و اعلام کرده بود مذاکرات به‌صورت مثبت در حال پیشرفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20618" target="_blank">📅 00:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=na4v_xnq7Xtnx8lWnJwNw2CvsMQ_RygAeWJfLRCbnwzn52VSd38jU5vYmzS2IPzxgSyCJ836Rm2JCVb59ADgGFI2kEygteDMlnrlyfTHl3T3XAwm2g5Lf6_FoU_S7ODf3ZgHk7sYERSUfgbFKrVlwc7Qae-vDpJNAYEzYWWqlilTHsmorbL14ymL7osSyseBLOSJrkuRSxSjaCX39zSmCPhGVJbPUcp6mku5oUex_UpTZpISoe3j_un8JbKchSwDd5PdtxZcfnyWQQZdM3UHYV37gekA8Kw1CJRgy9XqZKxCKPpItKu-jwe_9Jbyd9ATe13QE8l7N7NF43Oi_kpkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a684ce95a7.mp4?token=na4v_xnq7Xtnx8lWnJwNw2CvsMQ_RygAeWJfLRCbnwzn52VSd38jU5vYmzS2IPzxgSyCJ836Rm2JCVb59ADgGFI2kEygteDMlnrlyfTHl3T3XAwm2g5Lf6_FoU_S7ODf3ZgHk7sYERSUfgbFKrVlwc7Qae-vDpJNAYEzYWWqlilTHsmorbL14ymL7osSyseBLOSJrkuRSxSjaCX39zSmCPhGVJbPUcp6mku5oUex_UpTZpISoe3j_un8JbKchSwDd5PdtxZcfnyWQQZdM3UHYV37gekA8Kw1CJRgy9XqZKxCKPpItKu-jwe_9Jbyd9ATe13QE8l7N7NF43Oi_kpkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در سراسر جهان مهمات داریم.
اگر زمانی به آنها نیاز پیدا کنیم، آنها را خواهیم گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20617" target="_blank">📅 00:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=aXXIxJcDAw4M9AFKiDSRqYrfnHiqzbdYL61izRbUl0XrcM5Lqt61kppTxexmGbWbDccTqcmMoW32OYrl0aXcXzJWZljb7dPxN1qTzmCeL9ajTgR6fEc2Q7O7M2R6vbhMoH2e0MF5wMO5KJWrGXj_DTaqMIX2ZOLmlAeh0nDiM91zB02W5cAYR5V87DcI7PxL1OkVf3a13sX1Oghg83-RYFFf8MATM3dCw_h3-9kykNNSbjviA2pAAlbVqtN2VgnOtf_h567_d2QA36B9kr2oGJe7b4RpfDpcja7KOUlmoEmi91-VLbchzUMFN8FuBzhWyZ7_9Pvcnveencm32iPxWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0117ccebfa.mp4?token=aXXIxJcDAw4M9AFKiDSRqYrfnHiqzbdYL61izRbUl0XrcM5Lqt61kppTxexmGbWbDccTqcmMoW32OYrl0aXcXzJWZljb7dPxN1qTzmCeL9ajTgR6fEc2Q7O7M2R6vbhMoH2e0MF5wMO5KJWrGXj_DTaqMIX2ZOLmlAeh0nDiM91zB02W5cAYR5V87DcI7PxL1OkVf3a13sX1Oghg83-RYFFf8MATM3dCw_h3-9kykNNSbjviA2pAAlbVqtN2VgnOtf_h567_d2QA36B9kr2oGJe7b4RpfDpcja7KOUlmoEmi91-VLbchzUMFN8FuBzhWyZ7_9Pvcnveencm32iPxWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گزارشی وجود دارد که می‌گوید شما به اهداکنندگان گفته‌اید که باید کاری کنند جی‌دی ونس انتخاب شود. آیا این حمایت رسمی شماست؟
ترامپ: نه. من فکر می‌کنم او عالی است، اما خیلی زود است.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20616" target="_blank">📅 00:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=orw6It6hHCvy0DA7KrQew-WY2F9XzHXtK_nJIdx2GjE_ib-4nulW_ElqI6ZXbiebWNc8SultWdYVI7oSf8_iX6OW-B9wMMPFJpWBTQ_Y2Tyklm_TQyG_fV-FxL-RA7b00OxAXr8c-zbxFFn_qq-oBZA_YAqFcULkydRNwwOb0RedynVONXIdVN5g8mflaTGlmD4CtMEDVOaXxQb4-cH6pkLEoccVM465ePSZe2ALDbyWpyJtaCiCx1jabNDbpt1B3VM0lLXerHnXIIJ5yzKXqKFsr4ADBNsHn5QSeGR1jR_h8j8Fiy122D5WoaNKPvfOfcPqtcdx6hRSVgdU2NxRkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1081b3145.mp4?token=orw6It6hHCvy0DA7KrQew-WY2F9XzHXtK_nJIdx2GjE_ib-4nulW_ElqI6ZXbiebWNc8SultWdYVI7oSf8_iX6OW-B9wMMPFJpWBTQ_Y2Tyklm_TQyG_fV-FxL-RA7b00OxAXr8c-zbxFFn_qq-oBZA_YAqFcULkydRNwwOb0RedynVONXIdVN5g8mflaTGlmD4CtMEDVOaXxQb4-cH6pkLEoccVM465ePSZe2ALDbyWpyJtaCiCx1jabNDbpt1B3VM0lLXerHnXIIJ5yzKXqKFsr4ADBNsHn5QSeGR1jR_h8j8Fiy122D5WoaNKPvfOfcPqtcdx6hRSVgdU2NxRkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: فکر می‌کنم این جنگ خیلی زود به پایان خواهد رسید. به نظرم آنها دیگر نمی‌توانند مدت زیادی به این وضعیت ادامه دهند.
خبرنگار: آیا برای بازگشایی تنگه هرمز توافقی حاصل شده است؟
ترامپ: نمی‌خواهم بگویم که توافق انجام شده، اما در حال حاضر تا حدی باز است. ما کنترل تنگه را در اختیار داریم.
من در مذاکرات با ایران دخیل هستم. اوضاع به‌خوبی پیش می‌رود.
ممکن است به‌زودی توافقی حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20615" target="_blank">📅 00:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">محسن رضایی (محسن کج بند) دبیر شورای عالی امنیت ملی(جایگزین علی شمخانی) شد، اون سرش رفت اینم تهش میره @WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20614" target="_blank">📅 23:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20613" target="_blank">📅 23:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آمریکا : اگر
هیچ‌یک از والدین شهروند یا گرین‌کارت‌دار نباشند
، دولت قصد دارد در برخی موارد دیگر به کودک متولدشده در آمریکا تابعیت خودکار ندهد. این سیاست به‌ویژه افرادی را هدف قرار می‌دهد که برای
«گردشگری زایمان» (Birth Tourism)
یا با اقامت موقت وارد آمریکا می‌شوند تا فرزندشان پاسپورت آمریکایی بگیرد
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20612" target="_blank">📅 23:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تنگه دعوا شده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20611" target="_blank">📅 23:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU9yhyNBPQASCbveQOyyfI-N8zYRts2NZZJt-6fXvuMgc-VvWv8mw0PKziGvyeh7KbOEhCVpcn0xt_Vi1uEMdc-qkMtuthgNsXcG5ynit9_ZVKaLEto4Cd8a3uiNNPXM3IpM2e_Sw8-f2zz1NlTQnuvEZS8TBArwLul3cAbz1sZLWG0XVKWOguWEQZg50p0aQGqucUWCZX5JggSwBXSFK76tZlWjkoyB4MMLCMpXyEzQ_497s_a6Fq2Bnkh3fKP1lGBzJYGmaz8ahMeGU1ECOTvkxNHxv09LYeE0uRVFNRNKhj9GaNCuHkS11SPjvr2eXypYdqDzwLKYQCJP5tLE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم اکنون در آسمان انجام مأموریت میکند. دوستان بسیاری اسکرین‌شات گرفته بودند که این هواپیما رفته، لازم به ذکر است چندین نسخه از این هواپیما در پایگاههای آمریکا در منطقه حضور دارند. ولی این هواپیمای به خصوص همچنان به مأموریت خود ادامه میدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20610" target="_blank">📅 23:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏افشای تکان‌دهنده ژنرال جک کین :
‏"پاکستان و قطر بر سر منافع مشترکشان با جمهوری اسلامی، دولت ترامپ را درباره اهداف واقعی تهران فریب داده اند"
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20609" target="_blank">📅 23:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایالات متحده، اقدام حوثی‌ها را که آن را "حمله ترسوانه" به نیروهای وفادار به عربستان سعودی توصیف کرده است، محکوم کرد و به خانواده‌های قربانیان تسلیت گفت. @WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20608" target="_blank">📅 23:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgAOcwcX9sP_3avq5YApnZa3vxJqtbu1lVwT2diLeea7VnwojFi3_Ety6rTw9pICFZwkYV22X-nihyFnVnrQZJd03YXJlFaQcNOrK3U4pBPc-lNpflXmC1SEKwjBL7GV_FDhhmqeM7l3TSJhVaGsqRFhiuciW58OC0mA3TKirelcgtG-z8bG0XIhTJ8equnaJZ5IC306jOoarKXbJGXiRw0hFRLUHWYmA7iRUSccvqeKyntLh5UhDJsppzBb8IuE0DPre6J_tUqyjKkkYKgfH-xPi-i6yDZi-kfbQ4srkuOwyIujVyToyxPirhgDPLDGIshhGNnBk4sMSVWjckIW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان ۴ دهه واردات نفت از عربستان؛ آمریکا به سراغ ونزوئلا رفت
برای نخستین‌بار از سال ۱۹۸۵، واردات نفت خام آمریکا از عربستان سعودی در ماه جولای به صفر رسید؛ تغییری بزرگ در نقشه انرژی جهان که پیامد مستقیم تنش‌های نظامی در خلیج‌فارس است.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20607" target="_blank">📅 23:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZPh4IGDF_5CvvleN_RmlYhhAvT5YEh8PNlZNeg3a9c0c-p4_s5VkqsoVEkZcDppO5RMgzHn4ARBTO3Guh1BKDvtWECY11svH_Jf10Xu9hfI2sWnKWU_TpB6vdQnHXuPnW4R4Q-7MxHGAqUBQddcRF_uj3dznoydnfpQ8x0lx3vxCb2x4PZf7LuuJHMcDAeQ-vxpESrAYIIEtDeyyZbMvurViWfCVBPb4Vvc30KN72UpuTo3BMbYRp5fTWnH4oBtTRzGUqN96K7B6Ag-V87rTwxaLv4ixBS1ILjdSdi6adw0B1Ro7__2HB0kQbSeUZzBH8KPuIwR6zBiKxUiW_XaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در لحظه گزارش شلیک موشک، حداقل دو نفتکش در حال عبور از تنگه هرمز از طریق کریدور تحت حمایت ایالات متحده بودند.
NISSOS KEA و NISSOS KEROS، هر دو قبل از نزدیک شدن به تنگه، سیستم شناسایی خودکار خود را خاموش کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20606" target="_blank">📅 23:11 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
