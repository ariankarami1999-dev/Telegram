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
<img src="https://cdn4.telesco.pe/file/gWifMOeti4AiOPQU_FI4zCHOaAdgxrqeXbzynWSQUzlWwRcfBCYJjWQLBiTFbhnTA0dLHo39_FkghtME6cOEjBmunTvvIsTTFdmshRgxwbYIShUBuv43MKGn45qxcmb9-sexRQAzyp7FGXVU_YPlnglqMQoJvF7RSvCvsy0bgJdu0E89DghmXRVX-gHahk-9-9TeinoVcwtDJA-RzYD9w9pqDo5091w87TLKGzn1Isef0sko3QxWZnq944Z61xBKrB8WgGwRPrxpyAYY_P4kVCIbsFgjUjcK0LZI0iVcTTDRNr4OTtCJxm_MWkEQAZH_SSnjvlL_dkUgiFv1-C7rzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 18:15:29</div>
<hr>

<div class="tg-post" id="msg-679209">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15425cb351.mp4?token=NE9-IbPLWu6YHa0viG3hXuGetgIxGQAQJ-vHDstvXlrXtRFYBs-En_mC_t0V91-LH9CTgJjWFgyFNE0WQ2uHvR_B4wWSdrkDHGaOCeYfkTaKSTXbYR0_zZW9Fc02i5n3kFMPNcRFRe6StZS54p-wo_33Iq1C98LBBTb8aa7oe5L3sKEGxGUV4Vo6drFWzsTSr1HTvEE7pW4HhFPFTjjZR_gniMC5ECoRJ7sy2tVP2LAJonfcL8MFTp13htsOf_BNv3Ha_sLC0VINhOSukRqcvpjV8WAlrTM3QnAcmvJVfWvBn9VGfMrbspMwWI0gn_DVnTN-qrzjqBGRqP2VaOoIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15425cb351.mp4?token=NE9-IbPLWu6YHa0viG3hXuGetgIxGQAQJ-vHDstvXlrXtRFYBs-En_mC_t0V91-LH9CTgJjWFgyFNE0WQ2uHvR_B4wWSdrkDHGaOCeYfkTaKSTXbYR0_zZW9Fc02i5n3kFMPNcRFRe6StZS54p-wo_33Iq1C98LBBTb8aa7oe5L3sKEGxGUV4Vo6drFWzsTSr1HTvEE7pW4HhFPFTjjZR_gniMC5ECoRJ7sy2tVP2LAJonfcL8MFTp13htsOf_BNv3Ha_sLC0VINhOSukRqcvpjV8WAlrTM3QnAcmvJVfWvBn9VGfMrbspMwWI0gn_DVnTN-qrzjqBGRqP2VaOoIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار، سوئیس را تهدید کرد
🔹
ترامپ تهدید کرد با محدودکردن واردات کالاهای سوئیسی، می‌تواند اقتصاد این کشور را با مشکل جدی مواجه کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/679209" target="_blank">📅 18:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679208">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ته دیگ
🔹
رسانه‌های غربی خبر دادند که وزارت جنگ آمریکا پس از تماس تلفنی خشمگین دونالد ترامپ با پیت هگست، قرار است یک جلسه اضطراری مختص به کمبود تسلیحات برگزار کند. سی ان ان هم بنا به گفته دو منبع آگاه اعلام کرد که ارتش آمریکا در جریان جنگ با ایران بخش قابل‌توجهی…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/679208" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679207">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای معاون وزارت خارجه عربستان: توافق دفاعی با ترکیه و پاکستان تهدیدی برای منطقه نیست
🔹
توافق دفاعی مشترک با ترکیه و پاکستان محور نظامی یا مذهبی تشکیل نمی‌دهد، ارتباطی با رقابت هسته‌ای و تسلیحاتی ندارد و تهدیدی برای کشورهای منطقه یا روابط ریاض با آنها…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679207" target="_blank">📅 17:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679206">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/679206" target="_blank">📅 17:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679205">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عضو کمیسیون صنایع و معادن مجلس: در وزارت نفت «رهاشدگی» و فقدان پاسخگویی احساس می‌شود/ فروشنده نفت وزیر است و تراستی‌هایی که پول به حساب آنها می‌رود، باید توسط فروشنده رصد شوند
🔹
علی‌اکبر رنجبرزاده، عضو کمیسیون صنایع و معادن مجلس، با انتقاد از ابهامات موجود درباره بازگشت پول حاصل از فروش نفت توسط تراستی‌ها می‌گوید اگر در وزارت نفت «رهاشدگی» و فقدان پاسخگویی احساس شود، استیضاح وزیر نیز در دستور کار نمایندگان قرار خواهد گرفت.
🔹
علی‌اکبر رنجبرزاده در ارزیابی عملکرد وزیر نفت درباره فروش نفت و بازگشت منابع حاصل از آن گفت: «موضوع فروش نفت و بازگشت منابع حاصل از فروش آن به داخل کشور، همچنین مسئله خالی‌فروشی که گاهی از قبل انجام شده بود و عدم بازگشت پول تراستی‌ها به داخل، از جمله موضوعاتی است که مورد توجه نمایندگان مجلس قرار گرفته است. وزیر نفت خودشان را مبرا می‌دانستند و تقصیری را متوجه خود و مجموعه‌شان نمی‌دانستند؛ در حالی که فروشنده نفت آقای وزیر است و تراستی‌هایی که پول به حساب آنها می‌رود، باید توسط فروشنده رصد شوند تا زمانی که منابع به خزانه بازگردد.»
🔹
رنجبرزاده در پاسخ به سؤال رویداد۲۴ درباره احتمال استیضاح وزیر نفت گفت: «هر زمان احساس کنیم در دستگاهی رهاشدگی وجود دارد و پاسخگویی به حداقل یا حتی به صفر رسیده است، استیضاح جزو وظایف نمایندگان است و انجام خواهد شد.»/ رویداد ۲۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/679205" target="_blank">📅 17:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679204">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق، شامل آتش‌بس ۳۰ تا ۶۰ روزه، خواهیم بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679204" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679203">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571d5e5bb9.mp4?token=DLcH2tBL-rECQfF5GJ_b1OEnb4UbcYNlWTA-X-9Vk5K-Oh9gzyKbX02K0FHzdTJPRsVkotmhy0Y0n2H1GkuBVJYspd_GrkTb5__S7ChKrbX-AMQUQ51pUjyzN_PyvjoE7vA-tZCCDva9FG1sWADE_u62JEVEsvKQj858JmoYn3QnTZOAPPcvoWBuhDwfvuKv4Y-jxP7TBGSNl7IjolS7HyN0gyPMRVLPAhdoUdja2snzMwIFTtKYp_ChGd34tyWqq7LGhO6aiLaxnX77pM10a4L_fkk9UVeIXDGa-TA7fNuxx-KgUokdniJ16vPC0b4-jgq5YlpNgokOwz0erNi9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571d5e5bb9.mp4?token=DLcH2tBL-rECQfF5GJ_b1OEnb4UbcYNlWTA-X-9Vk5K-Oh9gzyKbX02K0FHzdTJPRsVkotmhy0Y0n2H1GkuBVJYspd_GrkTb5__S7ChKrbX-AMQUQ51pUjyzN_PyvjoE7vA-tZCCDva9FG1sWADE_u62JEVEsvKQj858JmoYn3QnTZOAPPcvoWBuhDwfvuKv4Y-jxP7TBGSNl7IjolS7HyN0gyPMRVLPAhdoUdja2snzMwIFTtKYp_ChGd34tyWqq7LGhO6aiLaxnX77pM10a4L_fkk9UVeIXDGa-TA7fNuxx-KgUokdniJ16vPC0b4-jgq5YlpNgokOwz0erNi9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ساده مساحت مثلث
🔹
توضیح محاسبه مساحت مثلث با کمک مساحت مستطیل؛ روشی ساده برای درک بهتر این مفهوم توسط دانش‌آموزان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679203" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679200">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/679200" target="_blank">📅 17:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679199">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqpX-4W26-D3Xwyxjdaar-MSjo-8bcyb-MxFXjlKb1Woq74O1BANE51FL4iztaFKXIVQ-Rwh9yUhfQKFgPZaSFQHTzEKR1l91C9ntY6NC4gjfPGo9N9p-BlcjzvnKzawY0s1yyf583mhmsJxEwc_oBnbdTTMrq75k6D7349duyPLWC8P3M8nOIWs_aBg1zdmex4wajYY752K6509nC0iV1d9F2aEWV0ZZGwDcQ_xv2srmXPKKwqRLyS1t5keiW5nqMg9SMZGTHeI9ojPA620Y-eJedxJ0Ny5wCRnqanCz0Ekbz3x-Ud-WrR7rdYNdr_wRm-QG995kx4sFM1iLJhxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وسیله‌ای که بعد از خریدش میگی «کاش زودتر گرفته بودم!»
🥒
🔪
خردکن دستی چندمنظوره
✨
سریع، تمیز و بدون دردسر
✅
اسلایس، خلال، نگینی و نواری
✅
بدون نیاز به برق
💵
پرداخت درب منزل
🛑
موجودی محدود
🚀
عجله کن! لینک خرید اینجاست
👇
https://khabarfouritel.affdn.com/lead/48457
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
https://khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/679199" target="_blank">📅 17:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679198">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تخم‌مرغ؛ بهترین پروتئین برای ورزشکاران
🔹
تخم‌مرغ به‌عنوان یکی از کم‌هزینه‌ترین منابع پروتئین معرفی شده و مصرف آب‌پز آن توصیه شده است؛ بر اساس این توصیه، افراد سالم می‌توانند روزانه ۱ تا ۲ عدد و حدود ۴ روز در هفته مصرف کنند.
🔹
افراد دارای بیماری‌های قلبی‌عروقی و کلیوی نیز سه روز غیرمتوالی در هفته مصرف داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/679198" target="_blank">📅 16:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679194">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMsCLW7uCT0b2m85l_b4yGg49lLAEAqSQT-GG_FeByIkqt6DA7vXWdZs-D4guyUACJVGIij9mVJxtoJACpsc-L9QeAkqYgwMznc-BmAJI8M6kAqleXrqbxAie9b6UJAwl3jZJ5D7TfqFUvBFJWRc-GutnAbkL6_hPswr0miHVSUYIvUIZW6PdMjYoGl2KwNlmp4Ur1pqhRZjdRFhIk-z_4uegKUU4qDrCtbR2gi4mRHGBxmgh8eo7ExWsv6O-QpAWsMZ53rAmSrQrELVfZdCWS50m019LGdiblU3NJ9euitbWNdb2wpn_R21WXByY7276NhTHqeSlAJGzyvKn0vlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wma4bTDlhpSyypM2bYBwPse-gzt7Yzdrole1Q_cgIFkmHiSxnrhslBb8UPJLpEXl3LF3pZUXExNA5v1pgq3nB9qPWsOHuO3kxYoWI-MQiZFDuDtrGFZbK_l2xie3aTIQ-N5xZWWDEArZXfocSmydYRsuAocOkj329Faiq_Ex9UtwzPE7kHQ1yIaRiH48IXZIpgrZ5YDqNZXTU1u-xU01Qnd5ZuDKVNDEgxKlGdnjd_sF1aA2qpXjt-YfxFT3E2QjHSfCjh6s7lYqyDxvF9ZfOg6nl2Yfa3svNaBCjjmQgI6qho6Q0myTohjSyPUPZcS8qZFhkC6-PUjAS4Wj5Wpdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvBrZQQ1KZcB951H8AtVJPKQnLlLKty_3JGjRrIS3gNeTaXc8vXLjklz-zg3VSGH2dOX90uWiAt-UYI5uuw6J6SXboOEaS_4tZVFe2jsa1TO-uWsyz56b27s3z1yIAhL2htJPfTB3EPn6WJDN98iZQYEW0jczdPPHdnVFo_-laHJUSUvkoJOd6fBfdoPaQ8amTKKUDuKO0_LP2-doE4zzcge1F_U90osnVUXk0H_IcLqmRGY_XJguldcoL3L2wIgb0oyUMys8jb9eCvjYg6Ep7J4e9QbmjOENZPX6fn7hZR458bJ1wQIoFjWPiYzI3FAhHU3ayXNjj_f0bQIG57KOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFQQ2qymBq8yeq3A-57_MxT6hMCW3WAevk_SKrfBbZpQrNfOBeQiC3d21FZczYlGi7OAArQGHHdv_4w0RcutorzNda636X4yyQpYh_GMOKKmkA5jVXdNp0qx74Fu8eJO4jgIBCSFK2YAnPUq2g1rCZM39BzKDJkPVYXTBsF3Gui-YuJgGUtXyDEk9kCypdb0mNuX9b3nVvk_JNxgG6-JD_V5s3bJMXRfqSnNXLzqHTnswNA1aIe1-g3Jw3vO9S2EbWQiFjumCdoP-vr1T2k_jDE1V_abJ__c5tDgkB5EUCzZ2CZ-jBluX4s8o1dPaMPUj6Sn2d8NE-WrOHCLgXF98w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/679194" target="_blank">📅 16:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679193">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679193" target="_blank">📅 16:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679192">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4478015bf5.mp4?token=djcS8gCiJei8wl8uAWG5ZiyToGgPB4OtbHDM4kqw7rgTrVyFsf3wc_5R8EtvxHDrxDMpOv_Ti_QM3HgVEnDluxxs0qc-MkHQiHcmzK2Po4DFPEsF1VwFU-e60KMOm9_lGr9ssxjqxvi8a-HA3yXv1KLNx7-tLvgSHhgTTqmQ6ZCHVkSwXaWJNY4kiQ-FXZBapEZAOuH9RqdTFXuxCsSjsO4kSqkZzBf3Qa51eLMNwrBhYG7iqlhwY5sec1pzVN3RFYCZSx8uSHk2Uaq_ZqoHSnReZbxrT4BogbkF4-BbajCK8jXhS2ql4tqXgDY4vJ5H4ntvqSt_D1MDWkKqtWifRQoF35rbfJT9feLgNqthstZ-niGYT6C2qjefjWVy9B9uq9Z9hspGB0es__ij_I1LGNYO89nkO-zsKEwzeOIi9lgsxqGRsRDXa7D1GXSsetvM7MvQ_z4c58JOYVhPzDEvLD4zdK8-8ob4txRl-2hZt3PsChAFQxvHhpy2QzZh-VPVQ-hRkvQHC3T40bAZ-RJwkeZEfv1NPn0xhgQmLIRR2Ulu1fkxE0vmH4TuttrtEf80rVRmXnp8FGtUfz5xRm1y06mq_m3SadM2ell4Inf37_QilYhE02KpKY2S90_yMomDzEP1zYPKhaPITjxTSytkLDBHZuftvENV1QBMd-czDf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4478015bf5.mp4?token=djcS8gCiJei8wl8uAWG5ZiyToGgPB4OtbHDM4kqw7rgTrVyFsf3wc_5R8EtvxHDrxDMpOv_Ti_QM3HgVEnDluxxs0qc-MkHQiHcmzK2Po4DFPEsF1VwFU-e60KMOm9_lGr9ssxjqxvi8a-HA3yXv1KLNx7-tLvgSHhgTTqmQ6ZCHVkSwXaWJNY4kiQ-FXZBapEZAOuH9RqdTFXuxCsSjsO4kSqkZzBf3Qa51eLMNwrBhYG7iqlhwY5sec1pzVN3RFYCZSx8uSHk2Uaq_ZqoHSnReZbxrT4BogbkF4-BbajCK8jXhS2ql4tqXgDY4vJ5H4ntvqSt_D1MDWkKqtWifRQoF35rbfJT9feLgNqthstZ-niGYT6C2qjefjWVy9B9uq9Z9hspGB0es__ij_I1LGNYO89nkO-zsKEwzeOIi9lgsxqGRsRDXa7D1GXSsetvM7MvQ_z4c58JOYVhPzDEvLD4zdK8-8ob4txRl-2hZt3PsChAFQxvHhpy2QzZh-VPVQ-hRkvQHC3T40bAZ-RJwkeZEfv1NPn0xhgQmLIRR2Ulu1fkxE0vmH4TuttrtEf80rVRmXnp8FGtUfz5xRm1y06mq_m3SadM2ell4Inf37_QilYhE02KpKY2S90_yMomDzEP1zYPKhaPITjxTSytkLDBHZuftvENV1QBMd-czDf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیر شدن گردشگر اسپانیایی با نظامی صهیونیست با شعار قاتلان کودکان غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679192" target="_blank">📅 16:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679191">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/679191" target="_blank">📅 16:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679190">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ax4gx8bZaS2KZ3oCYlXNFI489qK_BXw-lvcJ261NF0jTcLCgJhrd2YCJDl4bpavOTel3C6-gMNGZDYSZAKgYnSiFVKE2hT_Zdw0LkLCVRLvyEMblCdlVv2Ovb86FC5RZkaNmvzZm5GagUPvg5IYgFtHLLY9liy0AbMZRuaHKD7yBW6Rvt3CEM8bWcgyE6M62me7penLM3Uvtr8b7fYtsZc3cidNySB0elO7GS_O5tFr1jCif0r9Mbkn-sLzTu4qJLpbYWwa1CpFd86IPp3wfNvRN0rOQdrh0XjVDvsChENbZ-87lFF6X3iRInPzQgCw89JrRTgQIQkZHF451bxaWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از انتشار آمار جدید اقتصادی آمریکا قیمت جهانی اونس طلا ۶۰ دلار افزایش یافت
🔹
همزمان شاخص دلار تضعیف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/679190" target="_blank">📅 16:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679189">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3fdfab4e.mp4?token=t5Nn3x8V2VBk1i8OhjTjaA2GsLBCgBA1JC10lloDniDo3WHAX-9G_o7WLVfs1xudPmsvzlfubSTxdCN981OGjli2AmsMoLS2hDexVUWeSMePK-EgP1H4wQ6YD83kWr53RThhq4hXi976h-ptkuqC0mbHDNcLhIyicZ7ShbBZBpiFD5-6hnTfplJMFNeI67BpQOCwxZo8gnH65_gVUFweKMqH9OGju4p5xfopGxOl_2pbth1IVmh80mg-TQ0QqmOWLN5HnUkKxwt8enZ8guZs9CnQv0waLxdjJqToaaOlCZ_wCxSrYKqTlC643M4M-UEaG8xodbMaRa-nPZ89zSOaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3fdfab4e.mp4?token=t5Nn3x8V2VBk1i8OhjTjaA2GsLBCgBA1JC10lloDniDo3WHAX-9G_o7WLVfs1xudPmsvzlfubSTxdCN981OGjli2AmsMoLS2hDexVUWeSMePK-EgP1H4wQ6YD83kWr53RThhq4hXi976h-ptkuqC0mbHDNcLhIyicZ7ShbBZBpiFD5-6hnTfplJMFNeI67BpQOCwxZo8gnH65_gVUFweKMqH9OGju4p5xfopGxOl_2pbth1IVmh80mg-TQ0QqmOWLN5HnUkKxwt8enZ8guZs9CnQv0waLxdjJqToaaOlCZ_wCxSrYKqTlC643M4M-UEaG8xodbMaRa-nPZ89zSOaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورنکردنی اما واقعی؛ تبدیل خودروی اسپرت به ربات غول‌پیکر جلوی چشمان هزاران نفر در آلمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/679189" target="_blank">📅 15:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679188">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
منبع یمنی: صنعاء معادله جدیدی را اعمال کرده است
🔹
یک منبع یمنی تاکید کرد، جنبش انصارالله معادله جدیدی را در داخل خاک یمن اعمال کرده است که بر اساس آن، هرگونه حضور نظامی یا تحرک نیروهای سعودی به سمت یمن و یا بالعکس، بلافاصله هدف قرار خواهد گرفت.
🔹
صنعا از طریق رسانه‌های محلی به فریب‌خوردگان یمنی توصیه کرده است که هرچه سریع‌تر اردوگاه‌ها را ترک کنند و از تجمع در نزدیکی افسران سعودی بپرهیزند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/679188" target="_blank">📅 15:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679187">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رویترز: حوثی‌ها در نظر دارند برای کشتی‌هایی که از دریای سرخ از طریق تنگه باب المندب عبور می‌کنند، هزینه‌هایی وضع کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679187" target="_blank">📅 15:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c638a3753.mp4?token=ZkgwXHp5xgVzJFe0YVTyc5S5IbVuEwYn6sRjoQdUG1dQlS5GAM-TOa26K0J85-pR0qOV69kFChbjOHugqY0QBw6ZZDuT_cKBcY5qEId6nTvJprN2yZmxzX2BfBOjPLTZkzuHa7eAOdMYaNidopocN90XNgZKzHA6GjDiXoQS63mygM22jF9ux4Mqm3kmCjMadEVpV8fqL2DSW4piSDDyfHvySm_wpvix-gzIMToKnjgAScE4Addry8_I8XHTK0rxkP1cgYtITLvZWNcic1NbPy7X2YOloeRpac9IGMYMcrighDHzEPNXPAINWXAtib4DkzFc8ZjnIhJNjgsz4zRrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c638a3753.mp4?token=ZkgwXHp5xgVzJFe0YVTyc5S5IbVuEwYn6sRjoQdUG1dQlS5GAM-TOa26K0J85-pR0qOV69kFChbjOHugqY0QBw6ZZDuT_cKBcY5qEId6nTvJprN2yZmxzX2BfBOjPLTZkzuHa7eAOdMYaNidopocN90XNgZKzHA6GjDiXoQS63mygM22jF9ux4Mqm3kmCjMadEVpV8fqL2DSW4piSDDyfHvySm_wpvix-gzIMToKnjgAScE4Addry8_I8XHTK0rxkP1cgYtITLvZWNcic1NbPy7X2YOloeRpac9IGMYMcrighDHzEPNXPAINWXAtib4DkzFc8ZjnIhJNjgsz4zRrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احتمال شکستن دیوار صوتی در مسکو
🔹
بر اساس گزارش رسانه‌های محلی روسیه، صدای مهیب احتمالا ناشی از شکستن دیوار صوتی توسط یک هواپیمای نظامی بوده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/679186" target="_blank">📅 15:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679185">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab0df4751.mp4?token=qcO1olWNQtWOlYW38ElsUbmelEC_4xeVQBTiyNpGuHKDXDvfXrhb2l37WeMfwrxdFipTVrjqzZhClOYNp3lDtXKMU2dhk4jXLo27BT2iPJaJSunED2kotXVMnnYIuAOZx6BQ-lfnQWZIk0wD6JPuVTH-28lY_FU76kFQmpp5zACQnpeeMob5QbqatrzDovs4oouRJVWIDQCMpx9KJzFR-nStF5W_KQlkWna9e8uxYkfLVHRNWiVf4kaVLnIVJnY8Dpw_u3_6TSVqT7RYsipYcdr2fG6Ga7tXJ6UoUx_EBNQVSmYYkwS-nY5MfyZlrNtVhF9sxXtfIfuKV59e-FB-RxsVLFyBcnwhaeE4ePeqf4O4dmEBXekwW38TXbPuw56ANrqy1jEubITLjw74etaad9hmpdZX19MuxQYDg0nnnuq4WC05-qSYeP0hAcdxZTSpX4Lpq-yBejHtjU12rhM_nEMgh17vjY9h1lxpzCskmMfNkBew2A_if5KBN20S475Mg103B7OU0EfKp4NjoZme0ru9TD0g6Q8irJJfkYl3KbQ1vOhAhtPXn7Jg6fcwVXinEkM1guKiWu0E9y9uQ6nOZBkl7cnvxFInxStxYSQCQ8b1MLa5lQVsAx5sGQMiusD8nmw2A1xaqN_Xjljh0UaKtl3Mj-guD6mUYg5TRCnWtYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab0df4751.mp4?token=qcO1olWNQtWOlYW38ElsUbmelEC_4xeVQBTiyNpGuHKDXDvfXrhb2l37WeMfwrxdFipTVrjqzZhClOYNp3lDtXKMU2dhk4jXLo27BT2iPJaJSunED2kotXVMnnYIuAOZx6BQ-lfnQWZIk0wD6JPuVTH-28lY_FU76kFQmpp5zACQnpeeMob5QbqatrzDovs4oouRJVWIDQCMpx9KJzFR-nStF5W_KQlkWna9e8uxYkfLVHRNWiVf4kaVLnIVJnY8Dpw_u3_6TSVqT7RYsipYcdr2fG6Ga7tXJ6UoUx_EBNQVSmYYkwS-nY5MfyZlrNtVhF9sxXtfIfuKV59e-FB-RxsVLFyBcnwhaeE4ePeqf4O4dmEBXekwW38TXbPuw56ANrqy1jEubITLjw74etaad9hmpdZX19MuxQYDg0nnnuq4WC05-qSYeP0hAcdxZTSpX4Lpq-yBejHtjU12rhM_nEMgh17vjY9h1lxpzCskmMfNkBew2A_if5KBN20S475Mg103B7OU0EfKp4NjoZme0ru9TD0g6Q8irJJfkYl3KbQ1vOhAhtPXn7Jg6fcwVXinEkM1guKiWu0E9y9uQ6nOZBkl7cnvxFInxStxYSQCQ8b1MLa5lQVsAx5sGQMiusD8nmw2A1xaqN_Xjljh0UaKtl3Mj-guD6mUYg5TRCnWtYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از صفر تا صد ساخت آباژور؛ آموزش ساده‌ترین و شیک‌ترین مدل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679185" target="_blank">📅 15:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679184">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXzC6i5SvZzTugyF1wSw-vFLIbOYuXwzFx9gI3BTG_lHC-ktV_N31JaYlG4dt9RKg5PjqLnMmzNPTkeudw3fsQ9n62K8yfYfwdebpacxpQ2pqr9HSBUhCVCDFMW2GF-o2BTKN_JLnfq1KqWtz8k9GHdIw5oIKM4obAOIg_SpqTHr83NvhhkIKAe9CgXs-xUX4P1hnsD8UCDpxka-Vr3UHSmDtao8I02In9GNxRmFqgUmtGRpxElFNOoXskRt8L8Ux0qpPKM4NBCoCu_-cPPAaAc9NGd6YFYPk5PXtl6Y66rcaU-DmUoid53kdkEPsR3ZmCNl3XSjcBXlIi5j0r_zDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/679184" target="_blank">📅 15:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679183">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785649430b.mp4?token=hvB5zpij57Cy3Nt5zvQCKkrdK_jnxud1x75sR5BTLEJ-q7a3zdxosQsCFj7ndXV_2--qO7hqjrGU8AmgGSGf0Y3UFTo3nuxoiYOqT153xsgH6qsbE15KFpYCFISmvfN-dFQUwZwUVU-RE5CUvLOoJpI12uJ-q6_BdvAplU3NsbVAEiJ86JT92QUWJ8-HWWlJDYLEVRhcXDVtul_f6GhnAdeM85xyFvm2iOammq3n1lKHWMcpr-sv5vWLZbozTB5EWumhbNiP56ZOoKsUp4Yo8A0H3NsY667eyUuB0I30PNBntNJkflFRk5ZJW0_-ExIzAwTGi6NqIxjuPyzXud0Faw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785649430b.mp4?token=hvB5zpij57Cy3Nt5zvQCKkrdK_jnxud1x75sR5BTLEJ-q7a3zdxosQsCFj7ndXV_2--qO7hqjrGU8AmgGSGf0Y3UFTo3nuxoiYOqT153xsgH6qsbE15KFpYCFISmvfN-dFQUwZwUVU-RE5CUvLOoJpI12uJ-q6_BdvAplU3NsbVAEiJ86JT92QUWJ8-HWWlJDYLEVRhcXDVtul_f6GhnAdeM85xyFvm2iOammq3n1lKHWMcpr-sv5vWLZbozTB5EWumhbNiP56ZOoKsUp4Yo8A0H3NsY667eyUuB0I30PNBntNJkflFRk5ZJW0_-ExIzAwTGi6NqIxjuPyzXud0Faw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام ترکیه‌ای: توافق با پاکستان و عربستان سعودی ماهیت دفاعی دارد
🔹
این توافق هیچ طرف خاصی را هدف قرار نداده و سایر کشورهای منطقه نیز می‌توانند از آن استفاده کنند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/679183" target="_blank">📅 15:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679182">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883121b681.mp4?token=YT883pyR4zF_74DZ387-1ap6X9IEaYMdcNepwpOZbdu32E-05-_qH3PPjt2A0wL0YeoWJntrhkYcJO7kAD__fOzu9pYyNTnCpHZhH9i2RoK6nY1szlgNqgoo6lTpcVg0ViAHTuQEVrilETjWRc9AErZhcPigEHI9gFpa4d6cCS3CGjVpDDw1yYYig-eHml4ZggPwqMby32slrJ3HbhW1lOgwB7wvqo5bpNUA9WuerB_aPCirqO5kOL3-ESMRQD9LEirz66yRYRME_ZLSj204lZEDwPjbee-IxTeGwLjJACQMhCdM3cB4Gx_W8X1mV800RoGjk4utqEOHrFtJocZ_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883121b681.mp4?token=YT883pyR4zF_74DZ387-1ap6X9IEaYMdcNepwpOZbdu32E-05-_qH3PPjt2A0wL0YeoWJntrhkYcJO7kAD__fOzu9pYyNTnCpHZhH9i2RoK6nY1szlgNqgoo6lTpcVg0ViAHTuQEVrilETjWRc9AErZhcPigEHI9gFpa4d6cCS3CGjVpDDw1yYYig-eHml4ZggPwqMby32slrJ3HbhW1lOgwB7wvqo5bpNUA9WuerB_aPCirqO5kOL3-ESMRQD9LEirz66yRYRME_ZLSj204lZEDwPjbee-IxTeGwLjJACQMhCdM3cB4Gx_W8X1mV800RoGjk4utqEOHrFtJocZ_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان آرژانتینی پرچم آمریکا را پایین کشیدند
🔹
در جریان تجمع اعتراضی علیه دولت خاویر میلی، رئیس‌جمهور آرژانتین، معترضان در بوئنوس‌آیرس پرچم آمریکا را پایین کشیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679182" target="_blank">📅 15:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679181">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a02b17cd00.mp4?token=Cc8d9xy03uUUbECG0tp9gLh17Bn5INyP-oe236ElB1ShCAg7JG5f3Ht5ZSyzyrl7p42MTGUGUF4KNspiYgONDJ1aV2aVvL9gMEwl3CRR8ip3Ndf2hsSjnnwadtc_vqFIlRlDcja6VrytYIV-QyiIlitjjbb7WZSIfKANfpPbhNyAXfGnSME-Qat3ECZbs6lYU8BBESGk5Q0w0MnR0xi6a1zpyyPdvHUcs0BGcbOo7z_hCGhA8ZbYiCzcXlUxIQvNGLvYhlWDqEuhTTPRSWOjTIXIgi00IDXAuzovNvZYP4uLPWulToSeJdtPoQuHPwfOn58TSgqA5YTlFUiFrUxBJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a02b17cd00.mp4?token=Cc8d9xy03uUUbECG0tp9gLh17Bn5INyP-oe236ElB1ShCAg7JG5f3Ht5ZSyzyrl7p42MTGUGUF4KNspiYgONDJ1aV2aVvL9gMEwl3CRR8ip3Ndf2hsSjnnwadtc_vqFIlRlDcja6VrytYIV-QyiIlitjjbb7WZSIfKANfpPbhNyAXfGnSME-Qat3ECZbs6lYU8BBESGk5Q0w0MnR0xi6a1zpyyPdvHUcs0BGcbOo7z_hCGhA8ZbYiCzcXlUxIQvNGLvYhlWDqEuhTTPRSWOjTIXIgi00IDXAuzovNvZYP4uLPWulToSeJdtPoQuHPwfOn58TSgqA5YTlFUiFrUxBJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انصارالله از حمله پیش‌دستانه به نیروهای همسو با عربستان و وارد کردن تلفات سنگین خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/679181" target="_blank">📅 15:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679180">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUSYKw6htpsTkJLfyDJZB6dBcZk7SguWKho4IhIHs2-PsIMDhOus_fY6sk3qIYcytk7y5OrSbrZRavFBvIvy2214_J-IhMNgudZt0j6-I9C4rDw7pa_kHhpp_aXKWe0EVhe0_3zYsTUQRFKgh0PjcOKSPOmb0xnYBxsGdUBvZT6vRuXpGAs90BRHUmEkZDHwHActKs-9CsXly3WXZ_3WPBc3JKsQfBDT7mCIVAJ4Wh0aYTe8aZ9MSqcMZpUbkVvkssCbLLjHXmzNnLKTuUmOxHvUFxE93f2QLH0c-gVFXYBCwzVwRU15GPwEXy_aR3ceDtk269xSGM0ByLHrweNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همسر اکبر عبدی برای اولین بار عکس های عروسی خود با اکبر عبدی را منتشر کرد و نوشت: ۷ شهریور ۱۳۶۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/679180" target="_blank">📅 15:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2fsZxLM8CIz2MTNrHzNC1A8_FduGCgW20m4fEijdYP_O-hICWsrgynzPgfKhs80S3id_33ZDk8ACBvZ7B57YKbhlL9Blc1e8Q7dzkybJ0ULkt7zQtUTAec9dsFZiuqU57xbpGPEbZ39uFy3wqSv6_VfeU29m_pimVS-fAjhcgNr2UlkSbqWnHwpDp04ny-pCsa-gp35ddX5EceX40rMETg-svpMtqhuVQAZEW-FeOv6_nJGU_nvG0ZB0_W82InA6t147br8cRRUdEMumAJQbyzB8XdWK1iXnNg2BZ4I9Em-U8ZHEuRc5IQ-KwuIq6KZsjTODUF2YwXCypett1e9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: دیپلماسی در جنگ متوقف نمی‌شود، اما ادبیات آن جنگی است
معاون وزیر خارجه:
🔹
دشمن نباید از مواضع ما احساس ضعف برداشت کند.
🔹
انعطاف بی‌مورد، طرف مقابل را جسورتر می‌کند، هماهنگی میدان و دیپلماسی امروز بی‌سابقه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/679179" target="_blank">📅 15:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
چرا قبض آب و برق خرداد و تیر ۳ تا ۴ برابر شده؟  اطلاعات:
🔹
هزینه مصرف آب و برق مردم تا ۳۰۰ درصد افزایش یافته؛ مثلاً فیش ۳۰۰ هزارتومانی خرداد در تیر به ۸۰۰ هزار تا یک میلیون تومان رسیده است.
🔹
دولت باید ساده توضیح دهد که آیا الگوی مصرف کاهش یافته و مردم را…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/679178" target="_blank">📅 14:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679177">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f391c287.mp4?token=YDW3SAXpjKimc0PZazz3H-oALlzH1SBqXtzE_2299xfJhqtpxVv9ppi7E1o3VNreblcoo6a4I3sctESfSCUlt_X5gUhunXGpIKdfJ_6K-z5Y8gfGP2SCH3gehmj04thabDeKLvsiLjB010FL71fhfGCyGUApOiiaNf0E2rnW3x78F0lSUDJh7_Scq07V8Pop2dV8oBPdrseaXqssgLEeUBgQ_RzIoS1kL9FzvLTTZ0y4EJBbnjk6kglvhotCwRhBtrFZAzCh4E3m3NUh6lhAAYafPqME8aHztky0mKhCYk7TWWADkXRNTdSK0lT1BqtVJBe2EaDcNsEhm49ZwOAAnaXpH2rcuer6OaPUOoY2gUSFs2_94TvNtvfxXGJN_kEzsRfE84GcQmWSMYGUYKusxid-tARyhCXfn4Fbtz8oUJPCFEYMwvu2eOkZjPvImyKA8aFY7YXIyWbM4Fy8Vw8sW6fXhduGHyqSOMIJB5rujdlMIaQO9M2nJYOTEzYWyk8zPIZ6EtQ__EQ_Oh_UjpDw_QDos4VJyTxZKpecZWKNdiqsVbkXpK8h975j3A7AyTjgL2QWEjdFrOb6I3OxjBkTb4-XsMT01D8gDbmPRGbhQu6YUi_g_4Sbml5mnc2ozcoGM-STfM3cIl6IsDrwO-FqagDPEqhhbrKaVolzInbR3QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f391c287.mp4?token=YDW3SAXpjKimc0PZazz3H-oALlzH1SBqXtzE_2299xfJhqtpxVv9ppi7E1o3VNreblcoo6a4I3sctESfSCUlt_X5gUhunXGpIKdfJ_6K-z5Y8gfGP2SCH3gehmj04thabDeKLvsiLjB010FL71fhfGCyGUApOiiaNf0E2rnW3x78F0lSUDJh7_Scq07V8Pop2dV8oBPdrseaXqssgLEeUBgQ_RzIoS1kL9FzvLTTZ0y4EJBbnjk6kglvhotCwRhBtrFZAzCh4E3m3NUh6lhAAYafPqME8aHztky0mKhCYk7TWWADkXRNTdSK0lT1BqtVJBe2EaDcNsEhm49ZwOAAnaXpH2rcuer6OaPUOoY2gUSFs2_94TvNtvfxXGJN_kEzsRfE84GcQmWSMYGUYKusxid-tARyhCXfn4Fbtz8oUJPCFEYMwvu2eOkZjPvImyKA8aFY7YXIyWbM4Fy8Vw8sW6fXhduGHyqSOMIJB5rujdlMIaQO9M2nJYOTEzYWyk8zPIZ6EtQ__EQ_Oh_UjpDw_QDos4VJyTxZKpecZWKNdiqsVbkXpK8h975j3A7AyTjgL2QWEjdFrOb6I3OxjBkTb4-XsMT01D8gDbmPRGbhQu6YUi_g_4Sbml5mnc2ozcoGM-STfM3cIl6IsDrwO-FqagDPEqhhbrKaVolzInbR3QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وچهارم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای رضا معظمی گودرزی که به گفته خود بداخلاقی را نسبت به تمامی اعضای خانواده حتی کودک‌اش اعمال کرده و به خاطر شاکی بودن از زندگی، از خداوند طلب مرگ می‌کند و دچار گرفتگی قلب و جدایی روح از جسم شده و با تجربیات شنیدنی در عالم برزخ و بازگشت دوباره به زندگی دنیوی، تغییرات رفتاری محسوسی در ایشان ایجاد می شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: رضا معظمی گودرزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/679177" target="_blank">📅 14:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679176">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ارتش یمن بیانیه مهمی صادر می‌کند
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که نیروهای مسلح این کشور به زودی بیانیه‌ای درباره عملیات منحصر به فرد نظامی خود صادر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679176" target="_blank">📅 14:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679175">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/679175" target="_blank">📅 14:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679174">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTvmH1Jp-ArTZD5sF6shLM-g_yHJKLP7GoBB9xUkbuoU-BPKVOggFa6q3xFZBgVgDZ1bxQGQSXIsm2f3vyOo6Dc_RO8ccjnM7p-T0wUKGJ-idRs3E1Mnkg_MM4qt0BcR1YWH_YnDHoEKWtd9o0WLnyJ4aAarj-uq8oCFxMRnAPJBJM8ycZty6UsSXHhF8CcrkUOqqVOX3Kkv-jtXVEsgfMH2ykN_5f6Z7tQSSPf71CgUBrj6fwlOa9Yw9Y97Z_sSRtySxBMUyCA_tWlpynwGzxmjd7I-yJfZ-cbA0OIGBZe5qvPoWowDWkfEvZ8dbETFZQv7wQBCojPQpwfbVN1uDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر تازه منتشر شده از صندلی اف۱۵ سرنگون‌شده‌ آمریکایی توسط پدافند سپاه پاسداران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/679174" target="_blank">📅 14:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679173">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7102a082.mp4?token=IjxgTXKgw-LauEAUU3iukblCGCJD8zYTeR40sNRhJ76Hl6Nnzt7vUkapSLAHn2PmGPJPefdV_IWb0roLi7-FshHsscFToje2QtQgQpwITVYdPmq1mD0PNNN72KuLk40qX8bDqni8S965Q4YkEqJC10Z3hbw8kTZmtpwG1aXVfPVQVviBqzzeENjv2cXaIDYh6SrwxK3DNwCL1XVP_NS-d9PGbPj4Q-g5JPrgQTYS0Jp7SNVOdOcr_m8HuTRcTc7j5oyEuqepzaj9GGxuepxk7aZNM3WQrEACfX9qUJARE68QnPZq0BaUOTmMICwTb7gHTai8uAxTo4x20YxfDW0oJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7102a082.mp4?token=IjxgTXKgw-LauEAUU3iukblCGCJD8zYTeR40sNRhJ76Hl6Nnzt7vUkapSLAHn2PmGPJPefdV_IWb0roLi7-FshHsscFToje2QtQgQpwITVYdPmq1mD0PNNN72KuLk40qX8bDqni8S965Q4YkEqJC10Z3hbw8kTZmtpwG1aXVfPVQVviBqzzeENjv2cXaIDYh6SrwxK3DNwCL1XVP_NS-d9PGbPj4Q-g5JPrgQTYS0Jp7SNVOdOcr_m8HuTRcTc7j5oyEuqepzaj9GGxuepxk7aZNM3WQrEACfX9qUJARE68QnPZq0BaUOTmMICwTb7gHTai8uAxTo4x20YxfDW0oJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پهپادها و جنگنده‌های منهدم شده آمریکایی توسط نیروی هوافضای سپاه پاسداران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/679173" target="_blank">📅 14:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHHmCUrmTZmR3cvk-oJhLjYLQrXt6wn9a1wSS0IMXr04GdPiv9ErF-XXx6vh_7v0_I8POqXuUm6Isw8al2v9_-UXRnvSmk7d0VfJx_5Mqg-vGS0kfhqozmpccn1vIIhGSn8vBBmwGldtlpIhLrs4-_0ppudqs35X3BLeWr2lgSkBwgFasWjFN5ZvWnTtNqyROt5bi_4k8zl9fHyahMWRbQPB6YBgXZzMKdv3e9v24MR-Qq0Q46Id-P5PR-lTeNJlOKcp1aTjyzr5_uQFN2Ne4UfM1-cLSmV5r-UJefwS_jUItuunE89hXNCchEfYW8Of0TFwNOSpf9myZ_M3rx4SPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه: عربستان سعودی، ترکیه و پاکستان «توافق‌نامه دفاع مشترک مکه» را امضا کردند  توافق‌نامه دفاع مشترک مکه:
🔹
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔹
هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/679171" target="_blank">📅 14:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679169">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HK3yydbxkbqUPtzWxWAzY4hM2On5mLe3-WbrSuA7b_ai8SLFk6LLJxxrXqnL2KoIm9DqC2P2p6O0wzp0p80h2N3Ft2NKtR278NrkDbh_hHRUDSu1nHJS7YY3bykuBjGPE1iqs7SBSj7hBtrwGp2oitX67Ma_rIYG8fAIOIOTczpZNXJrrjZxpCHSsIOEU_HUvxb5q94A9AtyhSkykIPMfPcVMAFIjalXzCQ_xcztpSrYgpU87FXDqM1RZpwMv-SzjcbFr93haI3nVe5xy_uyAPOIDqqKgNKk8oR5o4zrYCIsl5iEoB2hrUArKWSbbAWLh5VceiJCl3hVGkJF6Cz1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKgPI5kuVy9yMSK0QLzbzZ_60yCVtW5qHxX2A6XoZj55XP9CLK_nNqgdDjYBOqeqfIod6mNBel4P40uFzy7Vi67gmOTqsCsVGangUU0Ng_v2VqdWoTX_IHXPzlLmq2xSvcTx0hb2QTfP1JJJZ0wPeD3uYu75y_1DebvwGuokDA7eWIrmUPmlI0tnAXxk6UuXxUcTU3H_WsLbI_3XT1TJbr80ZHslTWYSL1eQpo5Y14qnnAfnWhLlSzw0UApp8zidV0wbWK0NvMInkECsfTjWscXkgDn6-O6B7m8wq0U8vD8gpUr6hTIUU-s1o4UXSWch0_duydQoV4bqSc_XqLYTiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کوچک‌ترین گربه وحشی دنیا را بشناسید / کُدکُد؛ شکارچی مینیاتوری که نمی‌شناختید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/679169" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679168">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYBJixopkVGzJwA_T-eCFUhXnlfhbY7BB3ZaRw4mQKkbuGK0PayUB3QIszlX6C50cvtFjQ8Xj1NaCNQNpKQIpVteAYdmEk2PpIglJTbwdJxps89xbsMSs3pHsq2RuHpIP_RNmVS6turqeAjrSq9Hc7YFzMJtD7IokzzDWuO41Y89IkVcKIuDc7FppVTe-eOkaMqAEuaP32Ch82euK1sd29foCeTR7_GT7ghKc_LOgx0S4jOWi3HkdjGlqq3buL7jYXDO2A3Qk310he9yX8hAqQq1Q4JfwQGZ93iPVlojt4PcRN_Mgp0A8VPzuS9irHCG7Istzg8vJx9P-4TBqjMjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام برنامه‌های هیئت قرار در دهه آخر ماه صفر
علی جلالیان، مسئول هیئت قرار:
🔹
هیئت قرار که به همت کارکنان خبرفوری ایجاد شده است، همزمان با دهه پایانی ماه صفر برنامه‌های متعددی را برای خدمت‌رسانی به زائران حضرت علی بن موسی‌الرضا(ع) تدارک دیده است.
🔹
این برنامه‌ها شامل برپایی موکب پذیرایی از زائران پیاده در محل تپه سلام مسیر ورودی به شهر مقدس مشهد، پخت ۲۲۰۰ پرس غذا در روز شهادت امام حسن مجتبی(ع) و رحلت پیامبر اکرم(ص)، آماده‌سازی ۸ هزار ساندویچ برای توزیع میان زائران و همچنین برپایی موکب اسکان زائران در نزدیکی حرم مطهر رضوی با ارائه رایگان ۳وعده غذایی(صبحانه،ناهار، شام) است.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/679168" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679167">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCbNJ7sL6RmBtzDYORS90w2iLq92W1PFXwSW8bEdAe-Rhm5bcm0UMkNlCywWveRp9OyQJ_W7QwRZSCSg0-RrXbaXe_O50TBz8nPp44425FfU4Pi0bwGIaNd-bA2LxZupeOFp39A1th0VvUoPggI1ZEkwoq1OZ8OLz7Jb3Nt8-hfZOL65OQE1CmJD-MoxywRdqL1ISi7VOur_KWoxasHVhMngm1ehKXWISen9lOWu_GorKOoQze6VnK_HVCrmuUUrlrdZpJ5z_5SymWYGuzdC7PaNU65YMS2iiApxuFXQbnG98YfKi4qAjQ06HAVrPT7d0VElBD0NSOPl7KF16-cArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/679167" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679166">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150a2c1bf8.mp4?token=FpeOiJvV9Wc0cNit9xtM7HWCoWsppOPo0uT3sE-0jI3vv3WGRObq6_LbQGbkoJPcFfpN20-4djeh5_AfJwjoqJCj_c365HFU6Hac4xFFVjqlbMD25iOkH3Za_ydEx4y2Z5DI8oxiAkLcgAskr5GgLu8xtfgYZM0eevx1xa8LYjOMf1MaCS1J03mqr74J-BxFIpSQPpDVA2I9AXfpaH9W8vSTA6PZV_-Qzkf-gli4-qEyaFr4iPCRgL_jW5095K1gQIETYQPnjvHtAmyElknSiKd7pOeu7pHB2N6CqFRsP02pQs4alo9p6XSYZcSQgWcXnApJiBBto-fuayRujGI0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150a2c1bf8.mp4?token=FpeOiJvV9Wc0cNit9xtM7HWCoWsppOPo0uT3sE-0jI3vv3WGRObq6_LbQGbkoJPcFfpN20-4djeh5_AfJwjoqJCj_c365HFU6Hac4xFFVjqlbMD25iOkH3Za_ydEx4y2Z5DI8oxiAkLcgAskr5GgLu8xtfgYZM0eevx1xa8LYjOMf1MaCS1J03mqr74J-BxFIpSQPpDVA2I9AXfpaH9W8vSTA6PZV_-Qzkf-gli4-qEyaFr4iPCRgL_jW5095K1gQIETYQPnjvHtAmyElknSiKd7pOeu7pHB2N6CqFRsP02pQs4alo9p6XSYZcSQgWcXnApJiBBto-fuayRujGI0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس: چهارچوب کلی تفاهم با عمان مشخص شده و به زودی متن نهایی و جزئیات هم بیان می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/679166" target="_blank">📅 14:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679165">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_OkTvNIi_4JzAZs0OMkIYd78vpWo_RtVRNWWXb5RQg4BrnVVz4LRhmLNfAFbVIRyJREzouOgGFplQd5ZdcEp1mJNOKlFekfjDX5sFZUXvw9IuhdKscM5SctGH9TguUTuuekRsO1nb9y1jMpatinQlWUixG7m_2edRfQp7QZ7BW-SQSCuLwTbSDdzaAHwif88H1TeJt0qMMoFgYO8ozkB4x90jkF2BirmY6RrqpWQXJ8YjmjLtR4Blpc2TdhOxfjK1Ghh1Q2uVZKpHDrcqKoCOBMXmOg9sUuijtCW-2rLrFOTzpJYLYeS0RvfPJICj3yReaPKdIoYpNt7AUVCjzomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خرید قسطی طلا تا ۱ میلیارد تومن از ملّی‌گلد
فوری، بدون نیاز به چک، ضامن و اعتبارسنجی
با سرویس خرید قسطی ملّی‌گلد،
می‌تونی طلای مورد نظرت رو همین امروز با نرخ لحظه‌ای بخری و هزینه‌ش رو در بازه‌های ۱۲ یا ۱۸ ماهه پرداخت کنی.
✅
بدون چک و ضامن
✅
بدون اعتبارسنجی
👇
برای مشاهده شرایط و شروع خرید قسطی، روی لینک کلیک کن
🔗
شروع خرید قسطی طلا
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا و نقره</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/679165" target="_blank">📅 14:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679164">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyH-Gc6yoVCJqGJhXlgFeVOsTMWK8l1x-Rt-etSurXi0xIR3Kwiu5wvvb9a6ZmpX0o8_p8lwBKM9LOHQNNyOkFQWnbIGJ1MRDomSt-A4PC7SzpMaeOSftwn5tMzuyYQN8YUZRbyQnW4Ig6mBdRt3QJVvh5VzthCnfbtjgrvSy8TOTpXwYPGPiwlJ14sTbQkYq4oXmvfC6lJRIgXJM38MTgkpvZbw7SbOrsHwwNwrTBSyw7UsgZRZUoFO5BWEufpOGNELM5wd8zG8p8lkIQnoq2n5ED0anDRQYTfX1kqEgCnPSbWNWWed73B49ejB4U1kS0i3eqxt1TTe26vw_MFtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت مردی که با لباس عزرائیل به بیماران بیمارستان خیره شده بود
🔹
مرد ۲۶ ساله‌ای که در ولز با پوشیدن لباسی شبیه به عزرائیل و در دست داشتن یک تیغه بلند، به بیماران و مراجعه کنندگان به بیمارستان خیره می شد، دستگیر شد
🔹
وی در دادگاه مدعی شد که لباسم شبیه به کلاغ بوده نه عزرائیل!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/679164" target="_blank">📅 13:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
الحدث به نقل از منابع آگاه: واشنگتن از طریق تماس‌های مکرر به اسرائیل اطلاع داده است که لازم است تنش‌ها در لبنان کاهش یابد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/679162" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679161">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اجازه نمی‌دهیم چین با رمزارز و هوش مصنوعی دنیا را فتح کند
و پیشتاز شود؛ این دو حوزه برای آینده اقتصاد و فناوری حیاتی‌اند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/679161" target="_blank">📅 13:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679160">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ثبت‌نام کارشناسی ارشد علوم پزشکی ۱۴۰۵ از فردا شروع می‌شود.
🔹
نشست خبری پزشکیان فردا (روز خبرنگار) با اصحاب رسانه برگزار می‌شود.
🔹
وزارت دفاع روسیه از کنترل بر شهرک آنیشچینی در استان خارکیف خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/679160" target="_blank">📅 13:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نتایج تحقیق روی ۱۰ میلیون فرزند: ترتیب تولد بر بروز بیماری‌ها تأثیر می‌گذارد
🔹
فرزندان اول: بیشتر در معرض اوتیسم، بیش‌فعالی، آلرژی، آسم، اضطراب و مشکلات مغز و اعصاب.
🔹
فرزندان دوم: بیشتر در معرض میگرن، زونا، سنگ کیسه‌صفرا، التهاب معده و سوءمصرف مواد.
🔹
از ۴۱۸ بیماری، ۱۵۰ مورد به ترتیب تولد وابسته بود./ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/679159" target="_blank">📅 13:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر ویتامین برای چه کاری مفید است؟ این ویدیو را از دست ندهید
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/679158" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679157">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc87a808aa.mp4?token=Eci-_k4VbLRCGsj7SkoBEOtGjJ8ZUWIgt9KQqdCLukO98j9BZfK01wd0ASE6ugDzktV67-izyTx6lWADlBI1-fFzuWB-fjLKTHrpjDmNRLcr4hyOBWXQwpxpM89BMJNYf8tb-Dr3wD42SSmTMBkZi6PiqS55OlygtS-aVBDOu8HZBg6pqAhWpbmT5T3Gto8OA3YuDJwK_Qp9kRfUMHNEiOopi04g-uTAfLcy7xCut7he4pUOTiiVCBIgeRG03kYEuS8uewnVn_z3QEGbWHwfbo0gEqcQFVB9B1as4pdMA-taQq4iAVOk4wZUOhcGfH6QNTV_CxyS36rJMbnnAoLoiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc87a808aa.mp4?token=Eci-_k4VbLRCGsj7SkoBEOtGjJ8ZUWIgt9KQqdCLukO98j9BZfK01wd0ASE6ugDzktV67-izyTx6lWADlBI1-fFzuWB-fjLKTHrpjDmNRLcr4hyOBWXQwpxpM89BMJNYf8tb-Dr3wD42SSmTMBkZi6PiqS55OlygtS-aVBDOu8HZBg6pqAhWpbmT5T3Gto8OA3YuDJwK_Qp9kRfUMHNEiOopi04g-uTAfLcy7xCut7he4pUOTiiVCBIgeRG03kYEuS8uewnVn_z3QEGbWHwfbo0gEqcQFVB9B1as4pdMA-taQq4iAVOk4wZUOhcGfH6QNTV_CxyS36rJMbnnAoLoiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ترامپ شیاد درباره ایران: آنها می‌خواهند به توافقی برسند
🔹
آنها می‌خواهند به توافقی برسند. ببینید، واضح است که آنها نمی‌خواهند مورد حمله قرار گیرند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/679157" target="_blank">📅 13:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679156">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
۳ روز پس از اربعین/ پایانه مسافری برکت در مرز مهران همچنان پذیرای زائران
🔹
۱۶ مرداد – ۹ صبح
🔹
تازه‌ترین اخبار و ویدئوهای اربعین را
اینجا
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/679156" target="_blank">📅 13:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگر آمریکایی: بیشتر عمر به من گفته بودن باید از جاهایی مثل عراق بترسم، الان در یکی از بزرگ‌ترین اجتماعات مذهبی جهان هستم و همه چیز کاملا برعکس بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/679155" target="_blank">📅 13:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679154">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb7ng9JypbxotOkjO8wMAxZVltSSiFlTd9AgDZ7sv-G5zfUEz6UpwvydtD2-CtsNlVkf_D3sCvtYx1AzO89WB5ZQFXKvv-GPe6s7XTiSAksP-xupqCk5luCQPwNvpFbYOc61GH8pGGufeXRT6KZ3cWIiUE-oC1OQNTX3Rn0d9x_3eGGAPZn3TF-R_Q-lrUKjbH5NyWJ0qTNYh8nKXxYMqLF0PSDVVw-AParPAWXIjmV9bEKjeQ9xBjYI7WdUSZVMMywtV7laYSrPnzt27_uz7fFmuIbPH2_qP2PlBWOlAsMdZ5Xa3WuHXi7u0_GQl0zkSHGxMMTWUBnSLtffJ7TQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: ماهانه دستکم ۵ فقره خودکشی در میان کارمندان فرماندهی سایبری آمریکا، ثبت می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/679154" target="_blank">📅 13:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679152">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZurXuxHgQLpJm4oiyA3vBB4TTsrS_XDde1KTM-lLYyhA00FvTZEvQNGFUTtkBNglu-bqY0Rb-lY8iZL-o6eVu-h0b4NG3Gl3RuC2igydIFtcEmUwojnsNLwbFDhFiQT4_uqlYe5sRctAoI2NwhkxU6pGA-cFNeSiTCnKEZQG9qFlKzauddbfdkXsnj8YL5CiIK-sWhlGcPwJUUAoSb9TKtlKmLpWj7PuiYHIG4U7qYJwjWY_kbRSYXvBb3oAvFh8e28d6fMhhUZK_KlT4anuS2Tt_sI6I0E_nVuUwBRFBdmt4BEuZkEGHkP5e6txKa9qDF-LTetfLgYsI-pg6QnIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uv-XQ5HnPJoyaKADsB-gUZTkfPtX6mquRsH-p3K6mpWtD4u7LxeEaSscLYEvVwI397uDfDr5HhYIEr4leuSgHtVfZuv_SdHSSXcIl0aYzzBVPN5alZRMACa4Qh--FECbkYFPp1v9g0JpN09FfmxSPkF8CrD1LYYvY2wePoZSNnzZIRx3PJecBsNQm4ARW9uLFNdBORODCCzATapu-Eb41STYFJf80PNYMElsscjF9VIkHRE7OAynihDNqSpUuOZN5iEqVyYraY7pNatrXQoeqc5EwfLuEpbr14KYk_AGzRau7_i_jUQ4uWPOY1mJO7a6GxTSIDMlZJDSfCjbHNA46A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/679152" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679151">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfvMi121UXV80QZzwoqB3AIa8RR_IM0EkvpbQyyxx433cnImfSdbg0_go53dLkClmHQ8wbgjpvKb896rIS7sqj14ju5bVyiZVYCS6uhIzNkqACdP4N76bfOH-M2SzO9ckddyIQGVh6gIcvqbFIwA8V-nKKigPkOMP979m3egGuwXXqj9PzjRZO5qItiiuPcbgDwWw__aqt5dWbluS7y6T-JFHZ7R4-9ZtEhuc2DRGbqC7LfCfeeBW5Z5dMDNN4h0OhgOHWmEQ9QQS2m4WvQBsgeacL68301zMibeETb8WGk6E02bIx3stdJ0YevNpfowgx3Dl6lUU33g0u3u0kWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چت متنی داخل ChatGPT نامحدود و رایگان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/679151" target="_blank">📅 13:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8332585a.mp4?token=TZqFpIDeYvG7Md4mPq7DLS1cAydILUAwJHNdO8f9Z2QRgPGYoJiofheGwih2MCX6m2yxO2jqQod93JJfiu1dvP0OqMfOWwZg9saqMvLuOFjcxQhaSW4Q2TVnwBhQc1-cMwDC2vBSKmXiyL0TuqTHBI9JQvZbGZZZEApDD21jh4sAy5SUiUpv0v3BHR8IOJ2h2IsIMFr3PvqRW-skC_YviRnVMHfknfJy9PBsPCV5w93s2lL_u1p0asN6ho0T0O4_zXZB3FXDP1cDkx9aUVZQYxeZQfG4R7-QH0EXi_4vWum4WXtiFhPRJG1OtbDHaqBOIe0uTvQ_RQtLVm8weOaqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8332585a.mp4?token=TZqFpIDeYvG7Md4mPq7DLS1cAydILUAwJHNdO8f9Z2QRgPGYoJiofheGwih2MCX6m2yxO2jqQod93JJfiu1dvP0OqMfOWwZg9saqMvLuOFjcxQhaSW4Q2TVnwBhQc1-cMwDC2vBSKmXiyL0TuqTHBI9JQvZbGZZZEApDD21jh4sAy5SUiUpv0v3BHR8IOJ2h2IsIMFr3PvqRW-skC_YviRnVMHfknfJy9PBsPCV5w93s2lL_u1p0asN6ho0T0O4_zXZB3FXDP1cDkx9aUVZQYxeZQfG4R7-QH0EXi_4vWum4WXtiFhPRJG1OtbDHaqBOIe0uTvQ_RQtLVm8weOaqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدیویی جدید از مرد درختی، شهروند ۳۵ ساله اهل شهرستان خاش
🔹
عبدالنصیر که به بیماری نادر «اپیدرمودیسپلازی ورموسیفورم» مبتلا است، می‌گوید: «من هیچ‌وقت صحبت نمی‌کنم. ۲۰ سال خودم را به کسی نشان ندادم. دوست ندارم مردم فکر کنند قصد سوءاستفاده دارم.»
#اخبار_سیستان‌وبلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/679147" target="_blank">📅 13:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
صدای انفجار در پایتخت روسیه
🔹
صدای انفجار مهیبی در مسکو و حومه آن شنیده شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679146" target="_blank">📅 12:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b728ef516.mp4?token=e6DcjR-0CgstPS2z-lYoxRM8Xee4cVe-oNfLkU297za2UfeYlO9ilonXW09_FCxBoPiTKh3mGd6Blb_eVmSjgRy1NINOekg3ruYBMgv1LUsnmO1qHaA9SXWhoBSEuIzkQczg-Wkwk7nYKnXuxzSCi-1A88yubLC-1EZmffKcM4KjEw8nHGkvI0KjUSUGzm1NSGRm9eKKWgSFmypC3X34FZSBgt2LsoF5XvKlQ2zwcahJBEJIPSlchfaCFY051PziqhxCBjuZkWvtRK6GHrNBUJdrGQJR4zncG-f-edfaUD_voarEiZ4LammoOpFRNQCKLM9Jep8mKntq5y3FkcxA0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b728ef516.mp4?token=e6DcjR-0CgstPS2z-lYoxRM8Xee4cVe-oNfLkU297za2UfeYlO9ilonXW09_FCxBoPiTKh3mGd6Blb_eVmSjgRy1NINOekg3ruYBMgv1LUsnmO1qHaA9SXWhoBSEuIzkQczg-Wkwk7nYKnXuxzSCi-1A88yubLC-1EZmffKcM4KjEw8nHGkvI0KjUSUGzm1NSGRm9eKKWgSFmypC3X34FZSBgt2LsoF5XvKlQ2zwcahJBEJIPSlchfaCFY051PziqhxCBjuZkWvtRK6GHrNBUJdrGQJR4zncG-f-edfaUD_voarEiZ4LammoOpFRNQCKLM9Jep8mKntq5y3FkcxA0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیب پیست نسکار واقعاً چقدر است؟
🔹
شیب جانبی تند پیست NASCAR رو به بالای لبه بیرونی یک پیچ است و نیروی گریز از مرکز را در سرعت‌های بالا خنثی می‌کند. این زاویه از ۹ درجه ملایم تا ۳۳ درجه شدید متغیر است تا به خودروها اجازه دهد با خیال راحت در پیچ‌ها با ۲۰۰ مایل در ساعت عبور کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679145" target="_blank">📅 12:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
صدای انفجار در پایتخت روسیه
🔹
صدای انفجار مهیبی در مسکو و حومه آن شنیده شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/679144" target="_blank">📅 12:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679143">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تنگه هرمز عربستان را وادار به تخفیف‌دهی نفتی کرد
🔹
عربستان نفت سبک خود برای فروش به مشتریان آسیایی در ماه آینده را با ۲ دلار تخفیف نسبت به شاخص عمان-دبی به فروش گذاشته است.
🔹
این تخفیف درحالی اعلام شده که صادرات نفت این کشور به آمریکا بعد از ۵۳ سال صفر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679143" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679142">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تشرف سران پاکستان به حج
🔹
نخست‌وزیر پاکستان شهباز شریف و فرمانده ارتش این کشور عاصم منیر، به همراه شماری دیگر از اعضای کابینه با حضور در مکه مکرمه، مناسک عمره را به‌جا آوردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/679142" target="_blank">📅 12:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3b532a75.mp4?token=VujUZvZrpIMnjxSRK83x2FBIxHqYzTLOekA15QeIYnWeegexzC8gvCGGkPmtr8RyQP_hm2oVb37Dvhci989O6ziQhwbmSzXd8AeNGVkivrwH6WPCk3MjU6I6GxTDbjpojlOisVcHaGA8c3lisXhRNUfQW0k_A-9QAUf7WDRKJTyVxNq3pM1i6feLHhhm-egWyXM1yLAk-SmD97wATK-hYe-AcAR9YydBLOh45wXDrhNQeCkZrXSjOOK5FhdfI6nXJHhg5jzc_JoWa1NSzxK3WxnEI0iudtftJrBfTdJj4XmWxP2RyNtZ-KHfRY1jWum7-5XXA4gZIEtFkTEbGeg5rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3b532a75.mp4?token=VujUZvZrpIMnjxSRK83x2FBIxHqYzTLOekA15QeIYnWeegexzC8gvCGGkPmtr8RyQP_hm2oVb37Dvhci989O6ziQhwbmSzXd8AeNGVkivrwH6WPCk3MjU6I6GxTDbjpojlOisVcHaGA8c3lisXhRNUfQW0k_A-9QAUf7WDRKJTyVxNq3pM1i6feLHhhm-egWyXM1yLAk-SmD97wATK-hYe-AcAR9YydBLOh45wXDrhNQeCkZrXSjOOK5FhdfI6nXJHhg5jzc_JoWa1NSzxK3WxnEI0iudtftJrBfTdJj4XmWxP2RyNtZ-KHfRY1jWum7-5XXA4gZIEtFkTEbGeg5rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلیل اینکه ساختمان‌های ژاپن در زمان زلزله فرو نمی‌ریزد، مهندسی ساخت آن‌هاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/679140" target="_blank">📅 12:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679139">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59a91566f.mp4?token=K4Bjo9J7sh8Ufr_0gQi0vSG97zObrgfwIGnCf0DH9DUUpicCOIMafUigY9Dy35n9RADzhj_ccaOh22FhDXtEV5sV5UR0AWTrG8xuAhIx2aZzjep_I1-Dz_wnYjOBwgLyIjdmqMetsaU5ZXhu-Vxs-BeMRHKB2KCG26PEmn6qkm8Yuw2vaM3M6lBBtqEwZelbw8EmsaZgGolaJEfScG8b1G2BnM8Ho8eJ7IkCrvCuJkajBDwJYJvWeZ6D7C5NBIJNR6vzeiarX2J8h-VAUeGM-Aj8sWylmAWdcfhjNjJpa8EWkoipxOwqFAKu62KW8eEEoWMk_EKo4JbFGpLoeIxSAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59a91566f.mp4?token=K4Bjo9J7sh8Ufr_0gQi0vSG97zObrgfwIGnCf0DH9DUUpicCOIMafUigY9Dy35n9RADzhj_ccaOh22FhDXtEV5sV5UR0AWTrG8xuAhIx2aZzjep_I1-Dz_wnYjOBwgLyIjdmqMetsaU5ZXhu-Vxs-BeMRHKB2KCG26PEmn6qkm8Yuw2vaM3M6lBBtqEwZelbw8EmsaZgGolaJEfScG8b1G2BnM8Ho8eJ7IkCrvCuJkajBDwJYJvWeZ6D7C5NBIJNR6vzeiarX2J8h-VAUeGM-Aj8sWylmAWdcfhjNjJpa8EWkoipxOwqFAKu62KW8eEEoWMk_EKo4JbFGpLoeIxSAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ممنوعیت زیارت عتبات و اربعین برای مردم بحرین
«حسن قمبر»، روزنامه‌نگار بحرینی در اعتراض به حکومت این کشور:
🔹
فقط بحرینی‌ها در میان همه مردم ممنوع هستند که به زیارت عتبات عالیات و اربعین در عراق بروند. چرا؟ می‌گویند پادشاه به خاطر جنگ نگران آن‌هاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/679139" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679137">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1531d231.mp4?token=jTs4Vq-cjvUalGWlzl7RcyozrCvU7DGBq35mPARkxkYL7UwSRE9Y3zo7NxMz7fPwbkdDeRqm8ntD6n45nHI4l5akANBNho5TNGPyVaf4LYntskAuQcom-rdc-Cajawun92dCduUQdR4v47hwKNmeu6jsWNEfCar0kw2wiNJbfQ_91pvDt-9WumVYV7NVzdQhPM9scx7IZ5IudmlnfoFSK6UmMqEuuC0pwQe0n6_K4Z_3s-Z1G_h05KdafsOmcFDKTTN-P71vjT3IThNnGafWl7LnuQ5aYkadzDPEBMdHEY4x02vt1tytWURRmY0JlSbCI1e3gHWnaScr8w9TTaYeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1531d231.mp4?token=jTs4Vq-cjvUalGWlzl7RcyozrCvU7DGBq35mPARkxkYL7UwSRE9Y3zo7NxMz7fPwbkdDeRqm8ntD6n45nHI4l5akANBNho5TNGPyVaf4LYntskAuQcom-rdc-Cajawun92dCduUQdR4v47hwKNmeu6jsWNEfCar0kw2wiNJbfQ_91pvDt-9WumVYV7NVzdQhPM9scx7IZ5IudmlnfoFSK6UmMqEuuC0pwQe0n6_K4Z_3s-Z1G_h05KdafsOmcFDKTTN-P71vjT3IThNnGafWl7LnuQ5aYkadzDPEBMdHEY4x02vt1tytWURRmY0JlSbCI1e3gHWnaScr8w9TTaYeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشرف سران پاکستان به حج
🔹
نخست‌وزیر پاکستان شهباز شریف و فرمانده ارتش این کشور عاصم منیر، به همراه شماری دیگر از اعضای کابینه با حضور در مکه مکرمه، مناسک عمره را به‌جا آوردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/679137" target="_blank">📅 12:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRl0fzp7UhDx3ySkZgBosxXY3ZAJuANkWDz6Q5Uxm0o90I2dI4OjSFPtsNgdsihbl_Sf7eZCqgVRR-BekkVsksT5QFLOn6lTuJR1BQuwS9RDHzTksZ9OSFPb4xqCbl8jbeNVC4vQR0VQi-EDwof7RDmN1lhHLAK1vawCm3Myf89ye_DeR8EfkOSXAN_sQ_dK-SnwoXWJ-GNI35u286Yh19kUuapKSP9pM4EeB4IEywTofX3T4p2W25YgQWHoofMIWaptjysM4-wIWsvoilCaGWvMUUitD0DTk7460wkhKAxb-uNSAel0-CZERa1N9WkVpDIYlczZnH4vFt6V6St6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhmIX3DBGIgIk_awXf7Ka4gWETQ90xyLSBfQGuXI1ZOEYgjQhvGYatEKl1VAZoM3Tts2Vs8j2r63zcjXQ7s4TDcy3madTIcssnoLQD0JbuwoP544hv6KnOtgGuHKj4rXkyIQW8BSXhrKOCu4TrQ8s6QBmUeXoWJwn-MD6aBPDLY7_QjWopFbLHTuq9NngU8Cj2J2SPBiq7Cw8DblSX7Tz9Axx2Ecds1FY900XFrb1HmS9BH6sLv4NNkebqJ7gdHoPWmJ7eo8ztVFNDT5WO-1jTpCXIf31p3Uj8JErRUsspiBWMgodHyt_Wq7TaKtrUZ0_AGcJQLAFs-L56MJH5Iu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxfpy3WuWAhbHfCTv0I6j4ygnoSzWwLVtuqgSHnOdpytLXsXlzL1KlZUO5ONS3-kU3LP7Q1YqwjDdY3Awf914itPVb_o3W9S74MO_80UdxEBCchz3uCI8BnyuSoCaBRc7uMTHIcEs4iZ5dmaQD-cFGu-RF1zvnZ13WAfbpD81TeztkuYw47DNoJr7SdD5Zzfjs4pFhHUo88i1Sn91_-zCqAPsqljtLi7VjFEY0YbDrQA-shd4VN36g4hpmV-LxCGonZpviP-XTcrVX4Ic4qMqWYcmHmPma6TlSmOHBYHtiq7rcBKIyX49zPULd2LcyGmJSnHsODKMxbd3vxW4ZryjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دهکده زراس در ۱۴ کیلومتری دهدز، شمال استان خوزستان
🌴
#ایران_زیبا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679134" target="_blank">📅 11:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679133">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ced1f85eb.mp4?token=mqIAD7toszkd04Hrs5VrsrxajvllxfetRnzddrR1usgFNWvNQ-RsI0CEgVRVhRMUdAZ1N0VSnFk8kQcOaXpULkHvsFyCNvjWyZ5vkKIMdtXvfcqirLrQ6MLby-jn3N43dwkbabcYnYe50rM-JIoffWk-XJfGxlAs1Rfjf5v5dVNPXeymTYsFKz4JQ9HJP9HL10cKEkIF865ywzku_uZkgcx8d3Hk06QLq0NCFcYvS8jQEGBi7suSss5g3eBOTrctA2YelRwylaDgMHglMMdkfjWaswf_iG8tnxkzWWNzAchN9j0ZSFjutsEdXlFON7ThBm1z-v1pGmwwajxYZYbuJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ced1f85eb.mp4?token=mqIAD7toszkd04Hrs5VrsrxajvllxfetRnzddrR1usgFNWvNQ-RsI0CEgVRVhRMUdAZ1N0VSnFk8kQcOaXpULkHvsFyCNvjWyZ5vkKIMdtXvfcqirLrQ6MLby-jn3N43dwkbabcYnYe50rM-JIoffWk-XJfGxlAs1Rfjf5v5dVNPXeymTYsFKz4JQ9HJP9HL10cKEkIF865ywzku_uZkgcx8d3Hk06QLq0NCFcYvS8jQEGBi7suSss5g3eBOTrctA2YelRwylaDgMHglMMdkfjWaswf_iG8tnxkzWWNzAchN9j0ZSFjutsEdXlFON7ThBm1z-v1pGmwwajxYZYbuJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر اکبر عبدی برای اولین بار عکس های عروسی خود با اکبر عبدی را منتشر کرد و نوشت: ۷ شهریور ۱۳۶۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/679133" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
مقر مزدوران سعودی در مأرب دوباره هدف حمله ارتش یمن قرار گرفت
🔹
رسانه های یمنی گزارش دادند که نیروهای ارتش یمن مقر نظامی مزدوران سعودی در مأرب را هدف حمله موشکی خود قرار دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/679131" target="_blank">📅 11:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e42a9228d.mp4?token=nbBZYFi55eRZvXgQIeThxn4bbrgaOvJpde6871WQNjV92z21G2haeJmREJhvdGFyGq47smz-Hv01thFYGKLhCuXisTybbAaEAuzyMHyKpsdJXyfduWvISP387At1kTn_0kbHEYEgR0qjtj7kynMhPyAHMArUMxH5Xg5cpLngsPKi4zqirk4XoD3bgOF0HmoBKhsJkOK7eV14zkOxXcx1jWv5kvb74OUnTyvmkOZbta8Ho9it-h-NubTxIB3s_KnXYW3qDYpYMu3zSN4zFerUESS7cI4sZvCthv__48jso7RfngZQTwR0Z1U68dKGFOd1JJGPJ5gIjuV14dOIgDdnQzVeQd8GdNY3v156hGiHDBnhWN8ZOFt77YHDouht0F3Ss4OOXzRDSAwaHQt0VzwjaaH9K0stfsoP_iESOzgULW-LaTO-n74DMyKdpdv3enxsCyh8DuyllAkzAvZFhu33a3yPt7KVEJ670GAyrybcWauQkFSKRxUpaYgA5Fx7MIJR6SafrseUL2vQ7RTW9eecQqSYzSSG1iQzDBBKEJBj6zGDV5hReSgDeKI3Bno9QgcnhS8Kg2BjBSV_xLPmd1N_N5u1Qx7Y7BbsMvfh_uMKBYXq4kcxlhO-BxlH4cS3VF4cTOMDtgsYAlABuN2gUuqCyFTEQ9RaxU-bRJzPKVBT78w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e42a9228d.mp4?token=nbBZYFi55eRZvXgQIeThxn4bbrgaOvJpde6871WQNjV92z21G2haeJmREJhvdGFyGq47smz-Hv01thFYGKLhCuXisTybbAaEAuzyMHyKpsdJXyfduWvISP387At1kTn_0kbHEYEgR0qjtj7kynMhPyAHMArUMxH5Xg5cpLngsPKi4zqirk4XoD3bgOF0HmoBKhsJkOK7eV14zkOxXcx1jWv5kvb74OUnTyvmkOZbta8Ho9it-h-NubTxIB3s_KnXYW3qDYpYMu3zSN4zFerUESS7cI4sZvCthv__48jso7RfngZQTwR0Z1U68dKGFOd1JJGPJ5gIjuV14dOIgDdnQzVeQd8GdNY3v156hGiHDBnhWN8ZOFt77YHDouht0F3Ss4OOXzRDSAwaHQt0VzwjaaH9K0stfsoP_iESOzgULW-LaTO-n74DMyKdpdv3enxsCyh8DuyllAkzAvZFhu33a3yPt7KVEJ670GAyrybcWauQkFSKRxUpaYgA5Fx7MIJR6SafrseUL2vQ7RTW9eecQqSYzSSG1iQzDBBKEJBj6zGDV5hReSgDeKI3Bno9QgcnhS8Kg2BjBSV_xLPmd1N_N5u1Qx7Y7BbsMvfh_uMKBYXq4kcxlhO-BxlH4cS3VF4cTOMDtgsYAlABuN2gUuqCyFTEQ9RaxU-bRJzPKVBT78w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار کوثری: آقا مجتبی و مصطفی خامنه‌ای در جبهه حضور داشتند
🔹
رهبر شهید پیام دادند که اگر بچه‌ها شهید شدند اشکالی ندارد؛ مراقب باشید که اسیر نشوند؛ چون من امتیاز نخواهم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/679130" target="_blank">📅 11:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679128">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=ncWyk2Y0rpY9MWPMpiIyTr_jR30FAoOuRbra8EOYsd5n1O9fgy2-tHQVVhysPqk8vtMeLgRFdjg8TJfqROZCdXZ8Wy56al7E0lhifkKS9KjRE-PAPLKP0pBEcLgQEpak2Ib0m7YYuT27ran_OCItV7S-n_XUVsg3RP79xJB6NKr3VQ8bCn0ruY5vFZLI7iUK4kxRtDWGz1FoAREEUzwuhnv5nC7G_bkCFKIsyc1W-B8erYJbh_8nuXhg1hLUlowyP00bJHe8fE57x1xdopQHpuQrksv8D_-K3XTmG2dMv8RFGARV9poso7aB80AJxEamnbzIuzS_uXBEciPp-Vb_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=ncWyk2Y0rpY9MWPMpiIyTr_jR30FAoOuRbra8EOYsd5n1O9fgy2-tHQVVhysPqk8vtMeLgRFdjg8TJfqROZCdXZ8Wy56al7E0lhifkKS9KjRE-PAPLKP0pBEcLgQEpak2Ib0m7YYuT27ran_OCItV7S-n_XUVsg3RP79xJB6NKr3VQ8bCn0ruY5vFZLI7iUK4kxRtDWGz1FoAREEUzwuhnv5nC7G_bkCFKIsyc1W-B8erYJbh_8nuXhg1hLUlowyP00bJHe8fE57x1xdopQHpuQrksv8D_-K3XTmG2dMv8RFGARV9poso7aB80AJxEamnbzIuzS_uXBEciPp-Vb_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار انگلیسی: تنگه هرمز به نماد یک تحقیر تاریخی و ماندگار برای آمریکا تبدیل شد
جاش گلنسی، روزنامه‌نگار و نویسنده انگلیسی:
🔹
تنگه هرمز به نماد یک تحقیر تاریخی برای آمریکا تبدیل شد. تحقیرى که ممکن است برای یک نسل در حافظه‌ها بماند؛ اگر نتیجه به‌کارگیری تمام توان زرادخانه و قدرت هوایی آمریکا علیه ایران این باشد که اکنون جهان برای عبور از تنگه هرمز مجبور به پرداخت عوارض شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/679128" target="_blank">📅 11:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679127">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=NkXagdSMQXL8ARusRdbuoSqCM8mltlMwpffDo2WHQraFqCDDm0EVptxZLmOBSUU8tme8lKaqbqW0elDMmF7KoF0sg1b2PAO7odq-azAe_ziYGIFGfpdMNJ7qA_BAfWWNXYH4_j2qKbQRgSoYKfJ2OAd0LaGBo3FwuC3vuX2qzPZpFd2Zh5VPYL8voQzkiFuYTy7ZJWc7UUk8pVoOKlQLTwb_P3ikniv4Tq0G8zXOa0I5qBMWUjmud8sofWQFYTp-fnHmLObuBgbpQA4m4PnnbVRHwXgw_2p2pGii3DSDO4OxCWFOoODTjHR3DDwJJ35nf-yyN0YZrcgRmlEt2wZX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=NkXagdSMQXL8ARusRdbuoSqCM8mltlMwpffDo2WHQraFqCDDm0EVptxZLmOBSUU8tme8lKaqbqW0elDMmF7KoF0sg1b2PAO7odq-azAe_ziYGIFGfpdMNJ7qA_BAfWWNXYH4_j2qKbQRgSoYKfJ2OAd0LaGBo3FwuC3vuX2qzPZpFd2Zh5VPYL8voQzkiFuYTy7ZJWc7UUk8pVoOKlQLTwb_P3ikniv4Tq0G8zXOa0I5qBMWUjmud8sofWQFYTp-fnHmLObuBgbpQA4m4PnnbVRHwXgw_2p2pGii3DSDO4OxCWFOoODTjHR3DDwJJ35nf-yyN0YZrcgRmlEt2wZX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکشی ضارب ۱۴ سالۀ مدرسۀ تایلند
🔹
دانش‌آموز مدرسه حومه بانکوک، عامل تیراندازی بوده که جان حداقل هشت نفر (سه معلم و سه دانش‌آموز) را گرفت.
🔹
او پیش از یورش به مدرسه، پدربزرگ و مادربزرگ خود را کشته بود و در نهایت، در مدرسه خودکشی کرد.
🔹
مظنون دانش‌‌آموز کلاس نهم (حدود ۱۴ ساله)، ۲۶ گلوله شلیک کرده و ۳۴ گلوله دیگر در محل تیراندازی پیدا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/679127" target="_blank">📅 11:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679123">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EX2nBnNNOuxZoptok_3JtB3XDuudYvoP1I7QrrPw232c8TogkmB0i7o8jczGEYgu471a42D4P64kmOHZ2DVieGRIcxDvFtMi5XZ7KtdrRSZt-Nk2-i0ueuVugxeHdOzAEMDz-BfBznKTqO13LVELnhtQxQs5VFt1wa_SagLi0VQ5lHCD1zrGf0TPdBwJL8-ugItiiyD9waDHb1FpR9yK7cHpI7Ne1MtsaAYe-3cIcUvCYLjew9S7uvR3Figs40cpaETA3S_5v-xJMiP_5Oe9FuA8X4HFtp2C-yjjlO2V5icbuY4qr7gLprk2lnLLo-A7rNuUQNVqUFA-T7jEzahbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4vueUm6HjOY5ZPWL2r5zD_6skVmjOdTXhL-TQ42tbDSFmdxVt9pcsz6Y2kE7foT_s1BYyXbBwQTl41fFZf6a-DwPMECYozf-tDP2c_PfnoChej0QIZkfNEV19CEmY9ONnPTQp09pvcYrec2PnfndoK3GvF9n38AnFjpJ1kUUIQSg0KcnyUm7XuFkjbhbJSYWTHKyVJOK_lOJgpZ3a65DJ8W1pLRUPcWXFzs7c2xsbRvMDbeD686gK1boWpcYV2LyLZFiVzQoYfS-ryE9yKcCaBWY-sdXf3AP1DGFqhaJMHogvcSS4h4Bf_5dfaL4E8ioW6U-LadltzfcWU2sib5kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این گربه‌ای که می‌بینید پیرترین گربه‌ی دنیاست که جدیدا ۳۱ ساله شده
🔹
غذای این گربه فقط آب معدنی با ماهی سالمون، میگو، مرغ و تن‌ماهی هست! اکثر گربه‌ها متوسط طول عمرشون بین۳ تا ۱۲ ساله.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/679123" target="_blank">📅 11:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679122">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مقر مزدوران سعودی در مأرب دوباره هدف حمله ارتش یمن قرار گرفت
🔹
رسانه های یمنی گزارش دادند که نیروهای ارتش یمن مقر نظامی مزدوران سعودی در مأرب را هدف حمله موشکی خود قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/679122" target="_blank">📅 11:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679120">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=O77fElw8zUIY9v5GTLc-Y3rvhQtx2IU7Svt9mEPItuD574emLJTsBCC6TZTewhiOuIyE41OVgc4Dc9r0vSxgLntUubYDBsECwj5cnmTNvl4dch1XD4dEcvBrmyqahNW970J5-83rKsr2qEJiy7hTRWC9o95JmOEnMOzKmRaAPyPaR-x9-FURQLlqt6m6icTzLwXDERPO5RdROFGNkGdWcfhs2hdC3ERBWIdpvNs7WaFtnb53J79U4tW8chVJ_zJiiKyChKw38wQ3A2VYgcZTug0D0s7Kyd5SahSCZ2a8WZ7Q8sgqLN3cXAR00G6DoIZOAZxgTbliXmkhNk_w5uTE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=O77fElw8zUIY9v5GTLc-Y3rvhQtx2IU7Svt9mEPItuD574emLJTsBCC6TZTewhiOuIyE41OVgc4Dc9r0vSxgLntUubYDBsECwj5cnmTNvl4dch1XD4dEcvBrmyqahNW970J5-83rKsr2qEJiy7hTRWC9o95JmOEnMOzKmRaAPyPaR-x9-FURQLlqt6m6icTzLwXDERPO5RdROFGNkGdWcfhs2hdC3ERBWIdpvNs7WaFtnb53J79U4tW8chVJ_zJiiKyChKw38wQ3A2VYgcZTug0D0s7Kyd5SahSCZ2a8WZ7Q8sgqLN3cXAR00G6DoIZOAZxgTbliXmkhNk_w5uTE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آینده‌ گوشی‌های هوشمند
🔹
این گوشی رول‌شونده به نام MOTOROLA RIZR فرم کوچکی داره که توی جیب جا می‌شه، اما وقتی به صفحه‌نمایش بزرگ‌تر نیاز دارین باز می‌شه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/679120" target="_blank">📅 10:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679119">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28871f432c.mp4?token=UXGvgcpCEZg4Vrd0BBlbzEYj1afOjy1a4kQcVI55z_E4L_noaaTAOx6moEFBZ_OXro6xyHLnfDPL-WS2jG8wB3H49KXVv10ezGR2stfCNZvNutM5zIjm0pg74xBZ65IFsc-0Y1kEnk5ux8SJWLpIuT7_JZWy5b3-mfTEoP-6hRuYZLlS4vV6bfWgFTmUgR74DH5PjQTb3SxCSAAzAvW2Kla0LCV9JYY2q709f7XgKQNnRr4V7h-linMy0A5JVpZcVbJsiQz7ibX4waErLKkfUgSgTd_2vuEPmSCvkFQTGv-9wNvZ6u_0-8dkrhS9bOUNwGzZPfzfahO_qLKJ-ykRhq8RZ__eciMXYUvICTYG0jhYM9NSKtAQbnoO9BAYyDBv8dKSXwk2cBJhb8Q9TtqjNA4jmebywXljqfzsXTndkD-krA8V0a3JGwELtzeMJlc2Z1KsWlANQDARdzwrkD88Yvpt1881mvmSrxxPaTf0Vz5emnVYZvo8A1MkygqyD_NCQqLxQD7tmeZ7fC0_L-Yfcnoy4xRZuh5An3VxKg8ioca2lTPonxuD0wEv0A4FMtqn7SHAajbIn7GiZo-krtNlGfCVNHhR3YzOI1MpLCp6dcy_c8Mr-6Rvq4z4EDWDL278-Jo1suYSuGCq0fCTD86UcGbKePVbA9-fhT7r2ZJr5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28871f432c.mp4?token=UXGvgcpCEZg4Vrd0BBlbzEYj1afOjy1a4kQcVI55z_E4L_noaaTAOx6moEFBZ_OXro6xyHLnfDPL-WS2jG8wB3H49KXVv10ezGR2stfCNZvNutM5zIjm0pg74xBZ65IFsc-0Y1kEnk5ux8SJWLpIuT7_JZWy5b3-mfTEoP-6hRuYZLlS4vV6bfWgFTmUgR74DH5PjQTb3SxCSAAzAvW2Kla0LCV9JYY2q709f7XgKQNnRr4V7h-linMy0A5JVpZcVbJsiQz7ibX4waErLKkfUgSgTd_2vuEPmSCvkFQTGv-9wNvZ6u_0-8dkrhS9bOUNwGzZPfzfahO_qLKJ-ykRhq8RZ__eciMXYUvICTYG0jhYM9NSKtAQbnoO9BAYyDBv8dKSXwk2cBJhb8Q9TtqjNA4jmebywXljqfzsXTndkD-krA8V0a3JGwELtzeMJlc2Z1KsWlANQDARdzwrkD88Yvpt1881mvmSrxxPaTf0Vz5emnVYZvo8A1MkygqyD_NCQqLxQD7tmeZ7fC0_L-Yfcnoy4xRZuh5An3VxKg8ioca2lTPonxuD0wEv0A4FMtqn7SHAajbIn7GiZo-krtNlGfCVNHhR3YzOI1MpLCp6dcy_c8Mr-6Rvq4z4EDWDL278-Jo1suYSuGCq0fCTD86UcGbKePVbA9-fhT7r2ZJr5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزد؛ دومین شهر تاریخی جهان
😍
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/679119" target="_blank">📅 10:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679112">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBnfxrwUHa2GmT6HiBHQVGrXWV0BtSOcw7Y2Er0q7JZwBC4-tLVUeOyRHmj3iCA4v1IDRoC4nskBSFlENLiVhjrqcbREnEwioSC-4ZksChYgdnngcHKpa-1u0CIqSF9xHKFKNe6QsJG7HvW3rS13unYaAcN3RnUtEfinX2E-qRnmSyshBMeNYLGe4g0GbVqxZy9ZR1_PBetXTMNs0g8585i_mDwvbanjcjTDuV-gs0dPI5_O7BjwtvTQjF2ZnQkM7nJhMfjBzyfnucrmIFw8upx5VcIqoYP-CV213V_f3JYt24Q_vK_XIWQi_7OFLvvKSo2ZY2NrfoHPYZxGoYt2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4rIhk2hdXtEbYVKiDTa2PTRS_P5HBuJpdf2j_g6kBHZML8AcWp7hFqVUwzvY4XEPUhtCkf5EymochEHM0lZ3hpkgkxqkSWm6h2A4gw-bTAl8vTJWRGJXRhDMpFX_FMxZNeBJyRB9nGFF3pn3ksqsK5bjL47q1XukOgq9c-ZiBvO_zmhkWbrKLkIo_Vdc8UuiKue1OFRnOoNh11RmL132lR4WkYGnYmY4TmGnVb6J2coaIBYix-deJCA3gROSAgcvo--7Xnki5yrCJk5fDErG8D1r44YofVQo6QkSjh-Xe4Do67B_HvuBBF4-MPiFi4VDoBQReZahexrBFNl5mA50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmujQg2XDTPeKjOqweJ3lKOWHhfYJAQAQw2I08LLS2WKbA3rB-XuTNXq2eJNCl7vJn6908O325kSHStRFXzWMXFg4KZhHiRMlU7eWAUGkymJvSNzthyMnJvsRGTnPetm3Jj1-m19Dg5RRGe8i7W8i38eq-z7t1RpTF5fgfQvbS2F8I2mHx6QHOrKcPU8To-FgpnRUpEVYiq4_D6XWlOUyMTvNDfEy2W8HzDs2IAcb5YAvS4KC22eXHY-L0hQIN12Un8w0r6jBK4QTJuEHn2Cr2cwVqH74p-FNmBfCluczjbeMqzgub6-XzlXJV6egqfc1M-V3A9ncOhYq-ba_ujC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsJt7Mkszrksfj5ysf25KqWGCEZZgV_i0PwPE6QElWWSxdLI9r7D96q2ulw_QeRec5ZvXVGlXVdpFezzyBWJKRdSa0EjsHGLhuqLelyxD5pLFu0Yr3DtmtZaEV3XWwf5DzIACfrZdhgmBq9UTBtle9M69VRV49nmXzxYzQy2L89h7MIHw0nc2fomqw4Y5T3Jb1Xk13joWWI3n5smxE-zydhyqxC36tXK_JQGCZBepMT27ftqfjZutsKjVyZ0wumNGuw6enfRbFjSuI3lhNeaxwQwOUWQv_7iZ9s369rdHuzUfdT0HhvtQ7P8Y9KWEsDDVl1lYHxuyVIlpqfr8nroew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi_mtSzPNm9XETVRbQIkGi3YPObQzveW-M8Zrv-8Lz-e_ahtq8AUqLMYP4uZF7B68dPCagJgqb3mYFaA19jxtAzOiBE2GdMCyyehq7vb1XtqW7TBVROz4kB06QLEWtr7LUQDsKAT_JBOcI8DyRmqAN4s6nL7J7YaB-OyguHAT5k_GkjUtAT6CUuS05W6fnhhNEWyXYRrKaJ2ro4IllpjmiaA9g8rrDq1I2q8UlE-gZgUDnfJ1jH927rKqsgLIEr2enR4X06tlL1H_OV4-XB0XklyCQny1p5s3TiOgMB4IQGZgVBm55giGR7rBqUDEZQm1ynNnvCcaykS6l416QT9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFtwK7FeSi69RMhAcdmkptOjMZT7VKjAt_1hLw_JCu10NmS4OoaNJJsVL6QMdb4L6AGLcMjNdFLU8D2j761jkJ7JLjl0IcO3gt3UqlrfVxNtBZt2tsYm5vz_tGQjNFQCKeXmnKNmh4MPnLKE2JoiSlimTi5X2KmJQyvMWZM_tNESHtO4660dR-io2XW6aHyQvOcFEL7tXtKecNIB3XVPiwaOgZLjpwrKC-XwE_BWgz9S1ky2GjQsd-V-AMLzrkt_sYVBV3qg24pBQANFkQC_nfg355bXBjhKzPLIrA2bBX_0QTs-HwYm7sdULtmX5ZlPXnDClqQw462Z0La8ZoWz1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترش، تند، وسوسه‌انگیز؛ آموزش تهیه انواع ترشی‌های خانگی
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/679112" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679110">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
تجرد قطعی در ایران؛ از وضعیت فردی تا سبک زندگی
🔹
به گفته یک جامعه‌شناس تجرد قطعی در حال تبدیل شدن به نوعی سبک زندگی است و بخشی از جامعه تمایل بیشتری به مجرد ماندن دارد؛ آمارهای رسمی از بیش از ۱۸ میلیون مجرد قطعی بالای ۴۵ سال و بیش از ۲۴ میلیون نفر مجرد بر اثر طلاق یا فوت همسر حکایت دارد./ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/679110" target="_blank">📅 10:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679109">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/679109" target="_blank">📅 10:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghr246KRyiqskIyhyq0OyL2JRcuovM7xrp2Hi-FEKxabWEjAgGb-JcArKiHYXLXrKnmCDyqC6q78Lvem9hvKu23HgLnJxPggdzwrg2c4qOXrqHQ_EP7TsYiANSsOPuiXC2JfJyokQmTo62mIsyqb3KePRV5TVNUDlhSa5w5Ss0DG_TdbLlCN9cbhZX8fOxXQ-jbqzr8YKSD0RHeCprGCpgCZLBRgZeNQLk7QZmZiaJvxIp5AO06Igpk_wQDqAFZISsGL_Z3Rcbzt9GO6pYnCWyHoT6ytZODNr_QEPM4VqAicfqMitZXDyQaaLFchC9WiUw9TD1F2PmGta4BrsdvvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجاد تاخیر برای جلوگیری از تماشای مسابقه شناگران پیش چشم مادران مشهدی!
🔹
مسابقات شنای کودکان شناگر مشهدی در حالیکه قرار بود امروز در استخر شهید هاشمی‌نژاد سعدآباد این شهر برگزار شود با اتفاقی عجیب روبه رو شد. این مسابقات قرار بود از ساعت ۸ صبح آغاز شود و در شرایطی که مسابقات آغاز هم شده بود، ناگهان با تصمیم یکی از مسئولین هیات شنا متوقف شد. این مسئول ناگهان با ایجاد اختلال در روند مسابقات، اعلام کرد تا وقتی مادران در سالن حضور داشته باشند مسابقات برگزار نخواهدشد!
🔹
این تصمیم عجیب در شرایطی که مادران بی صبرانه منتظر تماشای رقابت کودکانشان بودند، با واکنش خانواده‌ها مواجه شد. تاخیر در ادامه برگزاری مسابقات و لجبازی مسئول مربوطه در نهایت با ورود مسئولین ورزش استان ختم به خیر شد و با استقرار مادران در بخشی از محل برگزاری مسابقه، مسابقات ادامه یافت.
🔹
گفتنی است عموم کودکان شناگر حاضر در این مسابقه زیر ۱۰ سال سن دارند!/ورزش‌فوری
@fori_sport</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/679107" target="_blank">📅 10:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679104">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکفایی در صنعت پالایش؛ ویدئو وایرال شده از یک برج تقطیر با ظرفیت ۱۲۰ هزار بشکه در روز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/679104" target="_blank">📅 10:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنی سندرز، سناتور کهنه‌کار آمریکایی: ترامپ فاسد و زورگو است؛ جنگ ترامپ با ایران یک فاجعه برای آمریکا بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/679103" target="_blank">📅 09:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نمایی
متفاوت از تشییع با شکوه پیکر مطهر رهبر شهید انقلاب اسلامی بر دستان مردم عزادار عراق در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/679101" target="_blank">📅 09:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حمله جدید یمن به مزدوران سعودی در مأرب
🔹
برخی منابع یمنی از حمله ارتش یمن به نیروهای وابسته به عربستان در پادگان صحن‌الجن مأرب خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/679100" target="_blank">📅 09:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کشف بقایای انسانی در ارتفاعات شمیرانات
کمیته جستجو و نجات هیأت کوهنوردی استان تهران:
🔹
بقایای یک فرد مجهول‌الهویه به همراه وسایل شخصی در شکاف میان دو تخته‌سنگ در منطقه بندیخچال کشف شد.
🔹
هلال‌احمر و عوامل تشخیص هویت در محل حاضر شدند و بقایا با دستور قضایی برای تعیین هویت، علت و زمان مرگ به پزشکی قانونی منتقل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/679099" target="_blank">📅 09:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679097">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدرسۀ تایلندی هدف تیراتدازی مرگبار
🔹
طبق آمار وبگاه تایلندی «خوسود» در این تیراندازی حداقل ۷ نفر کشته و ۳۰ نفر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/679097" target="_blank">📅 09:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679091">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجم تخریب پادگان مزدوران ائتلاف سعودی در حمله روز گذشته ارتش یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/679091" target="_blank">📅 07:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679090">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDzDhMJiRPQsQ_u3Dm3f2Fy8_rsKv0qgUp40hC000p7IFqMZ-LFvU75RWdJyiOxcC4SOi0JhX2EjjXHsXQ-lGE3nxH4WFWwKKTn1Nu8Z2r6p23kL2NmtoPbb6AJXoePCxmAM7-uK9Dz-XUaKNJfGo11Qb47jMKoabn3xu-RRL-zTkLv2yYrXWjsUzQu4He65evoa7TFuXrREAwXWP3RvgUKjAHHGSxj0yBUQENJP-uaouyG46vMeL2CyAMhY9EmGSuCwVbJwIFKODRr2ssInEBjecJ6aKtvS1B8RKNj2wW_ym_ATUhUMJubYRPV64wm-K1VMaYZTTtbwr4Iy4CL9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۶ مرداد ماه
۲۳ صفر ۱۴۴۸
۷ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/679090" target="_blank">📅 07:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679089">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD90GhWUNbic7nz36Dn8Y0yqgA_yMRrrj_oiliN1zkMoOHu9brQa2Po4dFSbDoRJ48Rt8KzwUyDk9Dy3y_lOZs27MrUXwpC3MhQga6xO0Vc5nD8XlBY8VngSwJ1M0Z17ix86uONwGPsppFZalqAD4mWv2zSNCtetqs0DyA1CyvqPcSnu5CPrTePZayrlxA8_0t-1zzhJiE2BWk1ZhCLdr81MxdFfqG3al-MpfSzW49JbZoLwrAWlDW0Y0SSqMs_L_2Ti7Iyxi53--S_u3Hs9IOcUtaUiUqh0Bn0pZH2ZQTNJaiOl4ymG2ZoeTkTfOGT58PEZHxM6Z0hoPcy1E_q6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۳۶۰
مرجع تخصصی اخبار نفت، گاز، پتروشیمی و انرژی
✅
اخبار فوری
✅
تحلیل اختصاصی
✅
استخدام صنعت نفت
✅
پروژه‌ها و مناقصات
✅
بازار جهانی انرژی
@naft360</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/679089" target="_blank">📅 07:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس آن‌ها، هجوم مرزی یک عملیات حساب‌شدهٔ جنگ ترکیبی به رهبری موساد بوده که با همکاری مراکش برای بی‌ثبات‌سازی دولت اسپانیا اجرا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/akhbarefori/679086" target="_blank">📅 02:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679083">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رویترز از دو منبع منطقه‌ای گزارش داد: ترکیه، عربستان سعودی و پاکستان امروز در عربستان قرارداد دفاعی مشترک امضا می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/akhbarefori/679083" target="_blank">📅 01:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679080">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغز خودش رو بر اساس چیزهایی که بیشتر بهش گفته میشود شکل می‌دهد
🔹
هر بار که به خودت می‌گی ضعیفم، شکست خوردم، فقط حرف نمی‌زنی بلکه داری به مغزت یاد می‌دی که این‌ها رو باور کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/akhbarefori/679080" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679079">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید حاج قاسم سلیمانی: ما در زندگی خودمان باید به الگوهای بزرگ نگاه کنیم؛ عمر ما می‌گذرد، تمام می‌شود، همه می‌میریم؛ اما انتخاب راه درست خیلی مهم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/679079" target="_blank">📅 01:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679075">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6460030eb.mp4?token=RDjr1ZzWkqW7BAvAFE9Nof8Lq3xPclAN-Nyu00TOsWKzZZXZtFYwQx0mAL4UxqwsCibnPp18Lsuuw4dwB8oKHmCCgGoPJT6UtGfkJt_qPUa7mXjTELR7kqI2H_V7z8jcOOZKFLZrubBgJcfSOzac_h_B7ejB3O8cNCxjbYlhIBzMBRfb1vDxuLKJAJ3vYA7qOAffaa7fVSEiC1NuDNIZEr0UjbeIuydoNO0fcKiMjCfS5_gOZ5fxNWVTacEvP5Vw_jYEyJLaSsjzYHsWT10yb2ErTbs9gxTjEwTS8SuCdL2cU0zCLA71sFR_782RcFKelo9-C8NW4bqCmp1W_fm38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6460030eb.mp4?token=RDjr1ZzWkqW7BAvAFE9Nof8Lq3xPclAN-Nyu00TOsWKzZZXZtFYwQx0mAL4UxqwsCibnPp18Lsuuw4dwB8oKHmCCgGoPJT6UtGfkJt_qPUa7mXjTELR7kqI2H_V7z8jcOOZKFLZrubBgJcfSOzac_h_B7ejB3O8cNCxjbYlhIBzMBRfb1vDxuLKJAJ3vYA7qOAffaa7fVSEiC1NuDNIZEr0UjbeIuydoNO0fcKiMjCfS5_gOZ5fxNWVTacEvP5Vw_jYEyJLaSsjzYHsWT10yb2ErTbs9gxTjEwTS8SuCdL2cU0zCLA71sFR_782RcFKelo9-C8NW4bqCmp1W_fm38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراحل آماده سازی موکب هیئت "قرار" در محل "تپه سلام" مسیر منتهی به مشهد مقدس برای استقبال از زائران پیاده امام رضا(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/679075" target="_blank">📅 01:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679074">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
در ۳ دقیقه ماجرای شایعات این روزهای دریای خزر را بشنوید!
@AkhbareFori</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/679074" target="_blank">📅 00:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679073">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc78f30d4e.mp4?token=nnrG10_f7SX5L5-cio0ThjnwXSbE4oHEfmiQGvTnPpmDaN7kbXfVShj7deSYnlUXBESdD0bYRydU3M10TcGKAwFjpFK_IAP-AzSzuJIO4t1Lglz9eXJMuTURumIVm4mPgSQOZjSQ-MsCtcIJgF70Z6b6TOlwyOV6mpjf04oytdpcu7ebnxlrU4-RhJOet5_SS4mVWolpaMGXzex_c5rMt12jBLIEl2w56UH1MSPTcYktq9ulN5uYvBwD0pMCN6u9kIqAbjb85XvZFMKz84yxc4_atCJi6XecpykfmCmpBMScR7GRmZWeVfN8B8tTtkuz4qSszIjru0V8IVMneTKWmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc78f30d4e.mp4?token=nnrG10_f7SX5L5-cio0ThjnwXSbE4oHEfmiQGvTnPpmDaN7kbXfVShj7deSYnlUXBESdD0bYRydU3M10TcGKAwFjpFK_IAP-AzSzuJIO4t1Lglz9eXJMuTURumIVm4mPgSQOZjSQ-MsCtcIJgF70Z6b6TOlwyOV6mpjf04oytdpcu7ebnxlrU4-RhJOet5_SS4mVWolpaMGXzex_c5rMt12jBLIEl2w56UH1MSPTcYktq9ulN5uYvBwD0pMCN6u9kIqAbjb85XvZFMKz84yxc4_atCJi6XecpykfmCmpBMScR7GRmZWeVfN8B8tTtkuz4qSszIjru0V8IVMneTKWmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی به موشک‌ های ایران می‌گفتند آبگرمکن، اما امروز خودشان و اربابانشان از آبگرمکن ایرانی ترسیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/679073" target="_blank">📅 00:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679072">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4deefa9dfc.mp4?token=PIK4nSY7dt0Czcoh4WUu2uQsjcqJpH2T0LQyoNmjquBCaY3iBgp_l0MdFGPIaNrnjqlw7Gx2xyZrtJKdl9MJyoNZie48mg_T38Bb-R_acRwtI1BivFoen4mF9pDYafM1tERr3IqLQ2z6KtxoQrU0J69TQ8sHpOlIs4aH3wC20mXAmL9EIIne31mPu1dbvdR3phaF7hhsCntLdZVMV-v2F2l4xfTk8yffpCTRehzWhNNpm19nHaWhySaSHC73ogq1I8w14tv8aLFMeLptdtCass7mrRjBV6Q8mpod48vIpUtkhl1PeUBjVklgDR4WOLIi8EdmyOS22YbRbKzndJmE5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4deefa9dfc.mp4?token=PIK4nSY7dt0Czcoh4WUu2uQsjcqJpH2T0LQyoNmjquBCaY3iBgp_l0MdFGPIaNrnjqlw7Gx2xyZrtJKdl9MJyoNZie48mg_T38Bb-R_acRwtI1BivFoen4mF9pDYafM1tERr3IqLQ2z6KtxoQrU0J69TQ8sHpOlIs4aH3wC20mXAmL9EIIne31mPu1dbvdR3phaF7hhsCntLdZVMV-v2F2l4xfTk8yffpCTRehzWhNNpm19nHaWhySaSHC73ogq1I8w14tv8aLFMeLptdtCass7mrRjBV6Q8mpod48vIpUtkhl1PeUBjVklgDR4WOLIi8EdmyOS22YbRbKzndJmE5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای فیلم اودیسه در سینما 4DX قطر؛ تجربه‌ای که مرز فیلم و واقعیت را شکست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/679072" target="_blank">📅 00:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679071">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7982f7e7c0.mp4?token=Yt22mk09FFgzHPf56IrJoEkDG3kqQ3TG2bzXjq62AcTet2BHzb91Y0mOuziQlayYh9u2bAXyOk4rr3Re8eGbrc9lkdeU9Hc0tQ_1_ygLMlMuaF6Bb2N3ShyCuo6P3v9EFfTgroHfqWBsXJDfijUT3-6f6sBUCLWugw69j2wmFbzNU4U0E6BgpJcDeAcrGsS9ZYdWY40qveiD8OITiVTIumljhj29g5qrD0KcN-66esXzAIsqFi-Ghp0iilFlhyC98tJzeBBT5Vu3E9oxil9KRU3tjKCUHe_X_ta9FQLwOXBZVwzSVyZsDUaYMZgXimLv1nP8z3yhzLXY-M4LQf6yJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7982f7e7c0.mp4?token=Yt22mk09FFgzHPf56IrJoEkDG3kqQ3TG2bzXjq62AcTet2BHzb91Y0mOuziQlayYh9u2bAXyOk4rr3Re8eGbrc9lkdeU9Hc0tQ_1_ygLMlMuaF6Bb2N3ShyCuo6P3v9EFfTgroHfqWBsXJDfijUT3-6f6sBUCLWugw69j2wmFbzNU4U0E6BgpJcDeAcrGsS9ZYdWY40qveiD8OITiVTIumljhj29g5qrD0KcN-66esXzAIsqFi-Ghp0iilFlhyC98tJzeBBT5Vu3E9oxil9KRU3tjKCUHe_X_ta9FQLwOXBZVwzSVyZsDUaYMZgXimLv1nP8z3yhzLXY-M4LQf6yJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آهنگ "گل یاس" که در وصف حضرت زهرا(س) خوانده شده بود توسط شادمهر عقیلی بعد از ۲۷سال بازخوانی شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/679071" target="_blank">📅 00:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679070">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/679070" target="_blank">📅 00:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رسانه آمریکایی MS NOW: عمان با چارچوب یک توافق موقت با ایران برای بازگشایی تنگه هرمز موافقت کرده است
🔹
هدف از این توافق، فراهم کردن زمینه برای برقراری آتش‌بس جدید و ازسرگیری مذاکرات هسته‌ای میان آمریکا و ایران عنوان شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/679068" target="_blank">📅 00:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وقتی کلمات هزینه می‌شوند؛ ایثار، واژه‌ای که نباید ارزان خرج کنیم
🔹
امیر قلعه‌نویی می‌گوید پاداش صعود به جام جهانی را به‌جای دلار، ریالی گرفته و «ایثار» کرده است. اما آیا هر گذشت مالی را می‌توان ایثار نامید؟
🔹
در روزگاری که هزاران نفر بی‌هیاهو از حق و آسایش خود می‌گذرند، شاید بد نباشد واژه‌های مقدس را با دقت بیشتری به زبان بیاوریم.
🔹
گزارش امروز، نه درباره میزان پاداش تیم ملی، بلکه درباره مسئولیت ما در استفاده از واژه‌هایی است که نباید بی‌محابا مصرف شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/679067" target="_blank">📅 00:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxoYJHw9orPcl9UsLZldQccejYVSdGx0A4-MUgWAftmovH02TLn-CayOwfeDdKEdteKto8FInSWV6HxyNNh-cW8WQhpayd9_335iSGuZ783FdIC5nMzzPJaa0JxlIyzWrtlqIH3a70VGjZOdlxHkazdsyaCtfqZ1aHg_AjGhCWQS2fXlRRYJ_EKbT0f3q90xXMWuFfMUE4SScCE-yvoybtj4PXZpV9KxbfkH87wS-bBzLBgmZ2zfnpOOqkZph0ocmuLlgooMgKPwlQFx7gWV9STC8XlWv0_0sSb6gEtcQ5HG3hqxPvwRWYSh7e5rIP5fdoJgjGdSkm_WXcoXrHC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: اجازه باز شدن مسیر دوم در تنگه هرمز را نخواهیم داد
🔹
اگر محاصره ادامه یابد، کشتی‌ها و نیروهای آمریکایی با خطرات و تلفات جدی روبرو خواهند شد.
🔹
ایالات متحده باید رفتار خود را تغییر دهد در غیر این صورت ما این وضعیت را تحمل نخواهیم کرد.
🔹
ما هرگز اجازه باز شدن یک کریدور دوم در تنگه هرمز را نخواهیم داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/679066" target="_blank">📅 00:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی می‌گوید که کشورش نیاز فوری به باتری‌های موشکی پاتریوت دارد  ترامپ قمارباز:
🔹
ما هم موشک می‌خواهیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/679065" target="_blank">📅 00:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c926eb53cb.mp4?token=NrI4_YtOn_6Q0x5B56eNcpaNzb6ePytR4EaOdvand2fMd9PZxmKh4MEvWL4wNzItHBEdU3by9XBcLln-5lXJsWqpBvr8qNtCKSgnfHk6nBkCrwid3UvnIbLUlNkb1AMl8_VUntIP_-0OHu-YGNgQawyzfs9NtPuifKZ2z5jgMIaruLaG2zEFOu474XfK6TFTNUydS3VFwzQvMoZ3dDxYbvnADJOZBTA_lAp6RrIfMCh8akGSVuQwbRtuUvPE7qQEB9NxKk8lF5qdKdAv_Z6wQNvFhpZThRKCMN1fx_CC-Mc499fPuizsgVzNi1s26WScOkQobfMTORCRst4jx-RsiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c926eb53cb.mp4?token=NrI4_YtOn_6Q0x5B56eNcpaNzb6ePytR4EaOdvand2fMd9PZxmKh4MEvWL4wNzItHBEdU3by9XBcLln-5lXJsWqpBvr8qNtCKSgnfHk6nBkCrwid3UvnIbLUlNkb1AMl8_VUntIP_-0OHu-YGNgQawyzfs9NtPuifKZ2z5jgMIaruLaG2zEFOu474XfK6TFTNUydS3VFwzQvMoZ3dDxYbvnADJOZBTA_lAp6RrIfMCh8akGSVuQwbRtuUvPE7qQEB9NxKk8lF5qdKdAv_Z6wQNvFhpZThRKCMN1fx_CC-Mc499fPuizsgVzNi1s26WScOkQobfMTORCRst4jx-RsiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی می‌گوید که کشورش نیاز فوری به باتری‌های موشکی پاتریوت دارد
ترامپ قمارباز:
🔹
ما هم موشک می‌خواهیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/679064" target="_blank">📅 00:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwuUxToA2f7TJZtz8GSH2ROvQtXxoAjzGlsiSYpAOF5sGVVrEOlC_aKMnFxjGkkLmZtkdR7_ZU3IByl64_o8c26UE8n3e2eLxKJOaXDXqsqj4wbgjbdtQeLH0aqh7ecJLAJ6qtkUZMWJ5gkYlybtxBefgFbVqhkeszxeMpqc4ZYZJ9Rqs849-lt06qAwUdhXK-QkHZ0Gz9qe9O6cLlbZRemGbPRxL3ygmhLlbR9BEqW1LBFKh9ffVstMMGMQOtLBlvkhmTbuaiYKq2UJJDT9jlI1HtyPxJPMQsVLw-UUL3C8ve02imZmMGjMOCsRbYPGnwmkgsESPgVLwVjtu06b5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BurOt3BNXTvCd_kruvXJQa2vBjWDHlmlOSMolPzmhp1C70Ogf5uJbhHBBS8ViLG-gQBqyoZHOur00hVqrOqDWSvpjh0HXlDxNJ3HUAq1T0sPu5_-Pr7w1mRxJ4jKCNfqOmjaz2fP6aXQvExOKb9Psg-qThHoP2zn2WqybnzQj4swvTQsL43g2ZCpsqss7Dh6cquLOrFLMwwa-l_-wFafeWL30FZoTWGF2t5wcRPNtVLpEn5i91Gn7syePw2OidimDfVgr0kWkP0ulJcUm_xCGFW-pvQ5hUM0GWskj5NFomIOD3A6oO3Du9OXVF3pnr5-NFNemUqW-BzaaXqw9_FM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyYIVGO52IDmfDqoexaXB1uVRI75XPg7yxscYJUfjh6LiFqL7lu-8OCsiFVqLUbzLzFoP3apAQ0Eyiz3mcYjMOnb0dXOPYqGOGkSNSfFtySBngjeMWxSMCmsyoDhTI1XRde66picHjF98Dci2hIu7GI7Wz5RkNczrsmDEmPiZFe34ceWA39YXR5pryr5yGK0TjfHsp55M-SqR0bBCwTE1gSC37ixsQNTAi0tKQYOV0HQIFJ36FWsUWcP9V06UWO_D7r1LwknDlDU8Y0NINa65aelKPXpfWywx_NMmvpPWTtChZvmW9USWfgC-nrpuaUkigmK_adrUxY4iQTZ8HYjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_xtXiengKtsrnhryD7hklwkUELgBADO3LHI8p85_U0hv96sY_aweKPr6UPQpJN13ZjcMa4XSdARzz4tUjMBnKAbOo6oQC3DTFNLY1D913uOJtITkzyDpy7s0HBvUQPTFQoAjAx1ZICddze9-HD5kAljJAJldWnomLyRC2lC-sLWZhUvj29Qwec0BeIUVyvk75r3DjzHIdGVWnf-s3tWQV8TDNCErPeFRj4JqB7NFy_cXyGHwm9XetNoyYKXMRVC2N10OPCGLn8PE7hlRBCV_rIjsutw-DK2NcK36AWU2u0-E8C4-RAO8XSXkM708-bnCC0AQ-3Hcad1fieThcbk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtoSOaqRD837HZUEDc5d6793Sqlkl54IYhm81pxH8jn4dt-kEV9GDMhNqgotKKRN5sk5nWx7dbEFhCsi8uQW2h-sWElYuRWtP8LbKoEJoGaBAU7ghKVk2Xqh72pOCBcXxWv7IPze7zlMlKMn3n9BYK88EhBrWp8vmQugQUYBxKiIKfXgu_xr3eWCmIoea5PmHPsvtlp4bfS92shf3G9LvKhKj0fBKNDBV3LOA385ja0HEF1Jtk9VaqXArcQDnZ107vdppzwVuGAa0WP2rxrojpDJpLjkgCkqKTmGLwl_MEfZrnqPfOsTzsBHcZhK15z964CnKFru6dobbEnHwNwSVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واکنش کاربران به قطع اینترنت در دوران جنگ
🔸
بر اساس نظرسنجی ایسپا، ۴۶ درصد کاربران اعلام کرده‌اند که در زمان جنگ از قطع اینترنت بین‌الملل به‌شدت عصبانی بوده‌اند و ۴۷درصد آنها گفته‌اند از این تصمیم عصبانیت کم یا اصلا نداشته‌اند.
🔸
در این دوره، صداوسیما با ۳۹ درصد، اصلی‌ترین مرجع کاربران برای پیگیری اخبار بود. پس از آن، شبکه‌های اجتماعی داخلی با ۲۱ و شبکه‌های ماهواره‌ای با ۱۴ درصد، در رتبه‌های بعدی قرار داشتند.
🔸
اختلال در ارتباط با دوستان و خانواده با ۳۸ درصد، مهم‌ترین مشکل ناشی از قطع اینترنت برای کاربران بود. پس از آن، سرگرمی  با ۳۳ و کار و درآمدزایی با ۲۹ درصد در رتبه‌های بعدی قرار داشتند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/679056" target="_blank">📅 00:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679052">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f5ae7020.mp4?token=bMBnFnOT6VoJ0tTDYkcLus5p61TalfaRAaLVbl39PZRIpCt702fALav9yZYuKIanFFsNSMXW43Hh9uRGXtge17Yj7et9kdomNTTt8qFiLgOrABOY1zSHXcbQ84SbghtGCjp6BWarvugPayd1iTPU8UCO2VYu69en-j5d2wq1IXbcaXe2QfQACMg81fJNvT6Do3yZ8tDr5U_BU1faNBxRO89i-3sR3HGxN1AmkBa_RGeKqQcxlOZa4kV6nJdo6gxb3y7Q9tiCE8nyvh8yX-ZAfX9EWqaUlOulgFBczVSqOnp8SqDAtvsq3cr2m9BiCWDf7xkc0TEifgdBMQwPlGDALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f5ae7020.mp4?token=bMBnFnOT6VoJ0tTDYkcLus5p61TalfaRAaLVbl39PZRIpCt702fALav9yZYuKIanFFsNSMXW43Hh9uRGXtge17Yj7et9kdomNTTt8qFiLgOrABOY1zSHXcbQ84SbghtGCjp6BWarvugPayd1iTPU8UCO2VYu69en-j5d2wq1IXbcaXe2QfQACMg81fJNvT6Do3yZ8tDr5U_BU1faNBxRO89i-3sR3HGxN1AmkBa_RGeKqQcxlOZa4kV6nJdo6gxb3y7Q9tiCE8nyvh8yX-ZAfX9EWqaUlOulgFBczVSqOnp8SqDAtvsq3cr2m9BiCWDf7xkc0TEifgdBMQwPlGDALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا توافقی برای بازگشایی تنگه هرمز حاصل شده است؟  ترامپ متوهم:
🔹
نمی‌خواهم بگویم تمام شده است، اما به نظر می‌رسد در حال حاضر باز است. ما تنگه را کنترل می کنیم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/679052" target="_blank">📅 00:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679051">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10f13cb18.mp4?token=kyAmF5FoTsUNQJoCUkqPewwWRX0hiBWegKu3blxkBvccD6gJ5G5zfKJbgdp9vP3h2Cu0yr37_OgYE8eRD0av4C1j7y0QsArGvmBZEjpWcCCDeDfT69CzLRKzkp3AL34mTxm5OwV8dNCDQgLAjCvJRFPqZvQ_SYCdDAimR20l6zYk1xdHvABUMw75vARXx_NpzEYGAQNSKalE2fMITErrdQlXkaMEvEjW4IqgqbRMXFTg_1Jsve1W0R3opOIv696VHhPv2ZOjP6Sxq8nD5tn5s9H_1TRVKZnPf94s18HTkBJTs-hLrENo68SG83t7NDyKVZ0xw9_oOUU4AUFUOlB3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10f13cb18.mp4?token=kyAmF5FoTsUNQJoCUkqPewwWRX0hiBWegKu3blxkBvccD6gJ5G5zfKJbgdp9vP3h2Cu0yr37_OgYE8eRD0av4C1j7y0QsArGvmBZEjpWcCCDeDfT69CzLRKzkp3AL34mTxm5OwV8dNCDQgLAjCvJRFPqZvQ_SYCdDAimR20l6zYk1xdHvABUMw75vARXx_NpzEYGAQNSKalE2fMITErrdQlXkaMEvEjW4IqgqbRMXFTg_1Jsve1W0R3opOIv696VHhPv2ZOjP6Sxq8nD5tn5s9H_1TRVKZnPf94s18HTkBJTs-hLrENo68SG83t7NDyKVZ0xw9_oOUU4AUFUOlB3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: فکر می‌کنم جنگ به‌زودی پایان می‌یابد/ تصور نمی‌کنم آنها بتوانند بیش از این ادامه دهند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/679051" target="_blank">📅 00:03 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
