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
<img src="https://cdn1.telesco.pe/file/hylYwaYYYqQtAtea3LvTYAShv1HcpB85ejGQwYo4KiqkQahNjLhK-2t_NbUW95Rks8K2kYiDK54gcurtrncE3aWlG6VIxqyKi1QOzoR6HUMvOGcLo13zfbARETkGPpjU5QZaeIV_N7XIcAXogqxZVNrD-M2SU8OBwqaDEWYb0Gmu3GbIoHWujWyaETDL-W8zSEB4X6oUbGTidQWIo23aXacPgYe4113UwBl_2sZYgJuvV1z9zBnZpLCSaTYxXnXSthlQcZ_rrhJcTIxVXWIizljOSxHiwmCjrxrByYGmrCmuLgdgbVQYu3be0ZBhYvyHR0cuuRE9BrhBZf1od8WI2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.3K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 01:45:10</div>
<hr>

<div class="tg-post" id="msg-2390">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عدد ۸۸ برای چینی‌ها نماد خوش‌شانسیه، برای موزیسین‌ها نماد پیانو، برای فیلم‌بازها نماد سفر در زمان…
ولی برای ایرانی‌ها، یادآور اعتراضات سراسری سال ۸۸ بود و حالا ۸۸ روز قطع سراسری اینترنت و خاموشی‌ دیجیتال!
جمهوری اسلامی اصلاح‌پذیر نیست و بین اونها و ما دریایی از خون فاصله هست.
از فرصت استفاده کنین و دیوایس‌ها و برنامه‌هایی که دارین رو بروزرسانی کنین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s_SpuvsF0liXRWIeBw3QnLSG4SyFzM3J5gM-gLGb2hIvDRyaJFZdsXeEL-OxzN9nIIF1iVMeeSvDkR30f2ImFn17T6g2s7tZWsUOjPuGYQS4RYjbHpYqsNWqiaCi5Vg-ZSJ5Vk5OuhkV-UZDuetl7QmPoHd6rRCfE8YZ54gupoUD2P5PYoLqb-vgpdN7djihVnsPfA8hMZjobbnPYeDogEr_tGDvwBf3THeMuqZ2ZhO0KEggH2PLdJ7UJtHhsyblXV_6hv2zx4oFzBrolUlrdxabbNCJYf-U5CsGIbfgdppCsLneRQa6dxD-20YnDg0563jwiRYe8jbf0asvbLoRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O3nA6woAjZt5ttFf9N9MnE89zfDZ_lcUjm74EvISyceMIZSHt9JrAtphFogCL0Mb9I6NhAp1GvFlcaKk_rRrg243wFciPE0TZWsxLR3vnqyatHEsq3h5RWZNk1J7vujQnbOLztJ63VAw3ehtEMeUIYc9ZenfAHxg0PbM5jxuAYF8oHFQLQ2_B3yFUJTvpz5lmxoKgo2MfLWQ7L6VMME8VYkhx4X-Zr-dwDRkF5W0fISRXBIg0-57nOAzMiS3V8msTpJkZpa1t6pJ5AaO7ukQD10v1MWW-2ggDCFGlXdH51XhLlprZFhrDWyFFvcdm_sByTO8dLngG_GmVpcqMQi7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه از وضعیت این روزهای اتصال نسبی اینترنت در ایران آگاه شوید، لطفاً نگاهی به این نمودار زمانی جامع بیندازید. ایران هنوز راه درازی در پیش دارد تا به همان سطحی از ترافیک بازگردد که قبل از ۸ ژانویه داشت.
©
nimaclick, DougMadory
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lwic9frY2iEy1sNwWAQXOOjFACS2u_gMN_7YKJPxYTYd_pSjeMdbVWKZQzRhFqMCvO8FuSJN9aLdqBQIsLGZlcxMrhCUqy7VKfg_c4Hpz2HMOzv3Z80dKh2KnlKoK29uc1fA-ZUvTha8DzA7Pd9Gt9O_6TqL_VQyVlKvFs2psWHyk8VaWsHOeYe_r1-56bKLscF9As1a2YDL7KurBx-yixZ3-qEpte_i1Cny-_oR2W0iR-d89X-bJw-YmkK4GSJ5VznwwLHtioVA4Fj4JLog65I6JGKOd_lphe8LB6fdd0soict1keWB22TCbFH-ab7krb4cD42vI6HOebNM6XZlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه‌ای از تلگرام اندروید که از طریق سایت APKPure منتشر شده، ظاهراً یک نسخه دستکاری‌شده و آلوده بوده و محقق‌ها متوجه شدن APK مربوط به نسخه ۱۲.۶.۵ امضای دیجیتال متفاوتی نسبت به نسخه رسمی تلگرام داره، که داخل اون کدی با نام DataCollector قرار داده شده و میتونه پیام‌ها، مخاطبین، فایل‌های رسانه‌ای، موقعیت مکانی و اطلاعات دیگر کاربر رو جمع‌آوری کنه. گفتن این نسخه به سرور مشکوکی در هنگ‌کنگ متصل می‌شده و داده‌ها رو به یکسری API ارسال می‌کرده!
©
vpnreviews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بازگشت اینترنت به وضعیت قبل از دی ۱۴۰۴ را با ذوق و شوق تیتر زده‌اند، انگار فتح‌الفتوح کرده‌اند.
کدام اینترنت؟ همان اینترنت ناقصی که UDP و QUIC و IPv6 رویش عملاً بسته بود؟ همان اینترنتی که نصف سرویس‌های مدرن دنیا باهاش درست کار نمی‌کرد؟ همان اینترنتی که برای هر کار ساده باید ده جور VPN و تونل و کلک می‌زدی؟
اسم این چیزی که شما تحویل مردم دادید «اینترنت» نیست؛ این یک شبکه دستکاری‌شده، محدود و مهندسی‌شده ا‌ست که هر روز بخشی از استانداردهای جهانی‌اش را قطع کرده‌اید. بعد تازه اگر همین شورای جدید واقعاً قدرت تصمیم‌گیری داشته باشد و فردا یک نهاد دیگر همه چیز را دوباره برنگرداند!
این‌همه خسارت به زندگی و کار مردم زدید، حالا برگشت به وضعیت نیمه‌خراب قبلی را هم دارید مثل دستاورد ملی قالب می‌کنید.
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GLcTLMQbTWtTriZ2wwwZqRsoxKrX3wR_oMiGL5m6f111HUvEv-_d1313EgMhEO7sMlNIVp6K5HYQckwsZa2IMyFgyxyoxDRySp-S_8NovSfgl2Nf0sRa5_PXY8RuAjvsj3NwDvqIEgHLBlvSaYjuPR2-g6wjfdnEHm68DB3EBGwokHOW5Qm3xbw9AeTHwG6k8SUctfqEHfrugPujKjMxxNSD3gaTkWgR_7upfo2AQWN1yJB0CaRBBefgFVlzbQx9-OGCWzIYN-W7PCSt_Gwgnu7xEM_qCNjRU2hPDAVj3QQ_BCmYVQQ3YDPonrxR-c00nzcmMxuTwIrsRtx2T3PvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-mhhd87HPAzFmlGdx5SkV4fFiB7Hgnttq5Je916LSXnvZrQ94NjXfwkTs-SOyOLLRzfZXNl5AbXFrVxAl3WkmmzOlRmD3OiZjM8XV2dR6OsOXK2-gOWNxiD_IuPBx21spSGQv3HXbo4vuO4fmp76m-if1Mwd1R9DVgyHxWl4_wEa53VsLjw-BLkWGvC0pDJ3P9f5Tz4RFD6JsjaIw3VeL7Q1aO8GTCZ9DsSFeGnVTtLhpMuWpAvloontlkePhDbu35qlUsNv3lPk50WUhQzOanbC6NOnKEaOSQFPXD9mDKECW2RWKMQggPX8Vt1rxJ8oHIbrTr3IaNzovEOVXYc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e2UHgZVmknnhq2AGazbfsTJSmdqXNpVuqsg3U7C6zQxCtwrP3b1skcq3fBJuEikIvZj36k1xK611oOh1NrsXLXm6STT3lghzX0cwHOQ9ZGjjB2rbyXD512PiuhnHeYl0pwsbzHyTr7BFTJEwVGCEv6pHr6uPZo_xsLZqb3QxvfwdLx6z6HeHPovbhUyvRp0tX6ISf9IlwHUTC3RFXIFPLSGGpx3QthjtXePNr--GSAGcOB7hax3Fp3FSOYH82GM9MBsL2YpPzmyeQT33pbymLJ58IYpfCJXQWPWdBZJmtMUMfBs37K-gUQCY3FmTwvVadvuHpSPUHtywG7uSnEaYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XW-zdO6gTdvEYfQEHR_ymZQpZVC4XuinOsvrb93RAuES_feYyZgJckhZQr_yQbIBW4qdEIVgn42-ZmP_VPEvtoxUV_ykfJMidgMnvZKOvKbIg-c6vjCnFZW98BTIa1d3TOH8YtReTD1dd0RZfxUTmxIBx9vSoW5URCEOw5E15iJ1zWtq3KaZXVYjYqGQo2GdO2bsaAq5G_kXodAXYHrKnFDVW7Bu4ZLrJAk1fMrb0iyfkzgTSGG-6B1BdVK-zfXj19numBA8VT5wVsF2tWFBnr8WX0clM1WNlVeOi36A5sB_uc8tXzZvNDVJkoUQJDM2odwqtZeojnCUh93ygRbcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I9MsZ3fltxl7dvKi01Sfj6eZd5oBURvDV0_loD1j6M4IErv0JKTMAJVKJJSJpNfJNFTkde5jFYp1a6hmwo3XQjvZTL1ujFbuJ5VLPkMmBRNsRWHgZocQxWzsvd2RVAA42hs1MRTCYpcX7RnF2oMg6GGPzTpAY3hcJA47bgvhjY2kApFANCr6eMmCfHXVWWHvSdGMoOVIoiyXywje6ub6dH83IqIc3sMX06xEgZW33M6TxD4olSCayDKCGQLbsJznYKDXetT1sNijBDq9VPp4p2VBLiYGULxtL5IyeMYDD8-6RxDuj3kmCrwddgj42q72X5n_avDPnVdJtkpMsWCyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی آپدیت جدید از اپ متن‌باز و رایگان
#شیروخورشید
کار خاصی نیاز نیست بکنید! حالت اتصال رو روی CDN FRONTING بذارید، اگر قبلا آی‌پی و SNI ست کرده بودین، پاک کنین؛ بعد روی اتصال بزنین و برای مدتی صبر کنید تا نرم‌افزار خودش آی‌پی تمیز پیدا کنه و وصلتون کنه!
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/5515
©
yebekhe
آیا این برنامه امنه؟ قبلا
اینجا
توضیح دادم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مامانم دچار آلزایمره، از وقتی اینترنت قطع شده و نتونستیم ویدیوکال کنیم، فراموش کرده من ایران نیستم، فکر می‌کنه باهاش قهرم و نمیرم دیدنش.
©
MaryamA89323145
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmhjNeBERAi_i4rfHtcRiEixC9u7ZAwXbGZEixsvnIr2d0_8OGhWhCCF1BFg5iOcsrb1nR-sFwkK1ZOuik5afv5iMkBjFOStBVWkls0tbYPn5x6zsxGy4ntJlW35ZVUoyhR2Zr9OGOvcLbYqvpeCnkBqAObmmDJwRcoNbDZDypaXNOsl8qSRUry_0WI3gwJsjPYJTUq5QMrpTgnaKvalmOe4_-acyGauh7fH1BG94GrLdfhtj2fFEriFc5T8Eqytk8QPVK4EhHxmd-DgX18fNgauAXK19CAghdIIEdXg1RLjENdOBND2I1K0SykS_ul9gE_wNkyPqe9jEOn0rQp67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=kAuDDIlKMUb9kKEzYPS49SeB9pIEHe0HyT3FlCAm-jfFfZAVrDohzPfesnT2dtFfON5_dKhOyEnpDmcMKa-AUcm7luxhk6wRYVlCkqPgdnzLBZqKINjn8GNCEHlfumVDCtycIZiaWsRFrdQ7lfOQwgO_6X0abY2PeL6qsHeP35B5g4h-3ZJ_mfyxvI-pfmf4XMxEgRfjAvZ5EBrugVUnwV2621etaAQdBrChqmFJBG5XpZgcETJj8mVtmnjfmUEYl4Qc4WvJxw4Ya3Y56wgjp2yakagEaeS4p41rQFbetS5CLLbv_QXR9vb6n1KQ23PHvfhRJy_BNPry6pkjaImtNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=kAuDDIlKMUb9kKEzYPS49SeB9pIEHe0HyT3FlCAm-jfFfZAVrDohzPfesnT2dtFfON5_dKhOyEnpDmcMKa-AUcm7luxhk6wRYVlCkqPgdnzLBZqKINjn8GNCEHlfumVDCtycIZiaWsRFrdQ7lfOQwgO_6X0abY2PeL6qsHeP35B5g4h-3ZJ_mfyxvI-pfmf4XMxEgRfjAvZ5EBrugVUnwV2621etaAQdBrChqmFJBG5XpZgcETJj8mVtmnjfmUEYl4Qc4WvJxw4Ya3Y56wgjp2yakagEaeS4p41rQFbetS5CLLbv_QXR9vb6n1KQ23PHvfhRJy_BNPry6pkjaImtNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم خداروشكر كه الحمدالله، وگرنه والا به خدا
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رئیس کمیسیون تولید سازمان نظام صنفی رایانه‌ای استان تهران با انتقاد از تداوم محدودیت اینترنت گفت: پیام‌رسان‌ها و پلتفرم‌های داخلی هنوز نتوانسته‌اند نیاز کسب‌وکارها را تامین کنند و مشکلات فنی و محدودیت‌های ارتباطی همچنان پابرجاست.
حسین ریاضی اضافه کرد: راه‌اندازی اینترنت پرو و اینترنت ویژه برای برخی گروه‌ها، نشان می‌دهد که خود سیاست‌گذاران هم پذیرفته‌اند محدودیت‌های فعلی، فعالیت شرکت‌ها و کسب‌وکارها را مختل کرده است.
او با اشاره به آثار طولانی‌مدت اختلال اینترنت بر فضای کسب‌وکار افزود: ماه‌هاست درباره آسیب‌های ناشی از محدودیت اینترنت صحبت می‌شود اما هنوز مشکل به شکل اساسی حل نشده است. در عین حال، ایجاد این محدودیت برای اینترنت باعث حساسیت و نارضایتی گسترده در جامعه شده و بسیاری این وضعیت را تبعیض‌آمیز می‌دانند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRih6s8IQd9S-MykwJ77hbE1tQ0KTXH9ftMuPdDVyYG9FuH4Hv9vzW38S7Xcu1JtYhq5eByfhxlm8Heh9Ncgo0HYbe2xHuxqwacHVqmmd9qiLLeeBSUXaF97jUuF16-FKL0JgMuQvAvoCbpD6E076ixddqRo4Yi3vJvuY7ZtVR-6BZXJr-TxSCl3lRhZL6gVS1EfcmbnIQIyFhKxISsb3B7ZBTBziRcmwzbXHe0i7CqmNl-XSHVn9LdDilVNUePxOOjSXslXOQczXAn1lhXAJ7NZ8UxvUu83AwSNX3AvbuxVJU9ZLIl7PK5OF7cvwqWRbXpfp9nD7dqGlvmBgMT91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۵ روز از قطع سراسری اینترنت در ایران گذشت!
قطع اینترنت در ایران، یک پروژه چندوجهی است. قطع شده تا بین "هواداران پهلوی" و "پهلوی" فاصله ایجاد شود و همزمان عده‌ای بتوانند روایت جعلی بسازند.
صدبار دیگر ایران بمباران شود، نظام با بمباران تغییر نمی‌کند؛ چیزی که جمهوری اسلامی را ساقط می‌کند، آن مردمی هستند که شعار دادند "این آخرین نبرده، پهلوی برمی‌گرده" ...
با تمام دشمنی‌ها، سرنوشت محتوم ایران محقق خواهد شد.
©
AmirHadiAnvari
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OQVpatMiBgxl8wshjJQDy4xsQknAPXVPnOdfB2I2FCzpouimFFgxQ6KS1U14lk7L9g2trpbCchyHZfJWfMfXy1BvY9zFEyErobWDcZzPBt-d-dDhp39m04ABDrOruTXa9bAmuVp0XZfqzhPPexpiQ_1HAEhjhAvmjDl0NSKYUlh3tOyStSfCGHNSCKGiGXycbYxkJOIFurw-eaizyIdzfQVd0PyvccOD702XwUQJa91Jq71LvbJK1hpVQs3tb1LR7hdcn7aWWhkk09mj7c-fwa2sy5lM7AUKmtfKcPLh3FMf8wBwNw1BOvI4xYw9-a2FaGFS4BPGsgg_uvuhmvM0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طی یک عملیات بین‌المللی، سرویس VPN موسوم به First VPN که توسط مجرمان سایبری، گروه‌های باج‌افزاری و هکرها استفاده میشد، از کار افتاده. در این عملیات بیش از ۳۳ سرور توقیف شده، دامنه‌ها و سرویس‌های Onion بسته شدن و یک مظنون در اوکراین هم بازجویی شده.
مقامات میگن این VPN در تقریباً تمام پرونده‌های بزرگ سایبری یوروپل دیده شده بود و برخلاف ادعای بدون لاگ بودن، نیروهای امنیتی به دیتابیس و اطلاعات کاربرانش دسترسی پیدا کردن و هزاران کاربر شناسایی شدن.
©
eurojust
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dl9TKk2SkWQM_V--cSYJibjPXtG9ccL8xv1fjslbmru19AzetjqFxYCe1NgBr9oY2tRJC8saFtQTWEnMBvbqOv9dMmmvyh5XN9eKIDpqd40ilPNJLl03T4UqyokwkKMRiaRWumih0Sv33bXO0nYwqGPk5n3djsJh0RRuBBoL32GeW7RXjxa1SyBs_0eCGRA5Kcx4FiGSIxtvFO_Q12yp7PhbPqiBEQeam6bfnKufqMlFRjUgB_SATvY0IsWHMIjXIcigMvEOfay32Qkbd7t8AbCDnmGuIIsnZlq9lNseU0BAsL5Udw7emdCtyAyQxlZmbKCnJhIUOJrsMEk2xWVu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ouz0w8PCXsggswDvE_9fxpNym8JdZKvMwK4Cv9dd2lU3PmoxgDXJmax9MgJaqXwvlEDvULS63kyPwaX3GlPbhLqK2bh667BpSLPwA6wqlbmHQPjY8dyUT7Wr9xF9mLAOpmRO4hj15G8g9ZsJwRrs0ja9ehTlG-2vz5kifh9dq6bukK_84VcTx-uK69SvXPy4gQyIcG2oYrDQo147M9LLCA8N56PsPN_KyQFqd-z0kJYJeEalBVJtm-yodzZLyqhri6pc9OX1NPcUX1W1dIrXSO82ppzbYBgnpJTk9wqotsFOHQXV1UeXxAGmF_yphli37m9G0iiYKvcdXQMkhiwhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IxsGuSg0rwXOC-LPITZVTPu-cWC_foFKEEAaAQGOK6EeAQJFih4lVTIiUQYYDLCV5DxoCi-fJpdpYUz9yAKN6UbTkNepoQ1z_Y1pAUOHC8BJfJl3XiyimV5oL-LBBAo2BzWDra2YmDruDSWKW2U8yDdM_tt8Bz3jDd2n-W21RXIqkm0Lg1AZ4KoCqIfIirOFomUMms_7BB8Zv61u8cMGdN1MG2883uDbXM_SImmgwn3MrddnVZ34UrO362wLjg31-ar0WoX8KPvGupKp5AnfZQe7JAuJKUwlqDgD-2VUnj8Ct_QlYQz--4n-jIFlI5AzVRXf96MD-gwwgSM5BU4hHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CVBd0dNMltt-PxAmidTkl2uHr1tOrSbpT1k0UL06cj8BfdSK8kuDtQUKCbKHLznGrJ3GctZdEGQKJvm5pMeZJ-8JBKbKWksupFC0EZ6g2sxIVD9gFh1tXMTrvdcRXNAyPLMwt8YYALJgvtwIEbGeM5SrAqzWNh-yEdFJmkZQBLUYRb4pGkgJbOXipDmwo7DpwVS0OlFOJ2xLVlPU44lIncGpSufmeQyMAEhX-8PsFmzwGxN0iLCHrLUTBdaH0h7-ozTHMGX2uN8O-jfOEq6kU_nSgt_qU5gCgiZeAwqnyoVjFfw_K1TZNbpWTMukePVIQwSGgTFwJVIZdDtEMHFWOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p7y8iV83jMSbsP_fkkIUiKt1wSXA4_Vor6TdvZIEWu2evWR8wsIFTsVPumujpy9GMOMcfJb_rhLkVJBdI1MWhfsIU0fx_IZklEZ_qjZrGg581NmQttLPNQ_bJnFoNUN0Sfiz-ieB7CxQZho0HgrB_N4OQ6jbz38vRn_oXBbAZQiYBDOgQ_hZwlKRHUPAfDx6G4_v-7hsdSNZc_JvMEGuYtaxoceC2I77rPbBwEvLCvkzaXHWKHuLMqoidNdyehqiFFjEk_yBOanldHiZTYakhG6b6PVo4RFdi1h82YJUk2YxJSI_X6_wY8lmiCbwORJqrg4-EealCIG4CfAcXTpozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-uspIvDwDchjF134OXRwyDmxTaiKNLKRwldxOAkyhoZ1hjbp-H4TRE_WElljmvQfMh0YKJzWgaohao8AjuwU00yrlVbXvfgb8yxm7W5nUIWJAcvSS4VRLdwQi_03mv126ZkJIzZqz4Z19Lxh-9_PhLibhzpSCcz9D4qlA6Wvt5axLEDpJvTV0ZSvFGrHmk7HOmmHnBSMiJgKOZy7tAzTHSV67SBTlIBaz_lx8Z4_MZ9iYAEgztNioAfwl4TJkvKRIeqowItnlBm95XK5b5t7Z8yy0zceGdHH9NidZMQADaT6lI9JdkfVr4wO3rx6QG4yOR7x_FCRoWZT31KQYKvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nrf79QuSH4-f2N9CKHpqAc1o_unwZdqJuUHsTinOAH37litkibL27oXEKviRzQUH25FVZdx9RYfVpFdX8BsaeDOY8Ynn0LYpIih_8BeW6wZpfef_3non2HCre76zs1-i06QwFeLhnVHl6cG45VcUtdYV1P-1XY_UsuSt_xYt89hbPh2ZK_UuJd2Dn74w0No20ctgA2jThfGyBOGnB6vcl2LfbAGLjsd6Veg0Cw6Qn8UCKjiJj6ITqixXz4KcWJSorfjUU5-GqXILZ3OHLqD8wtYEmogICVXHyjoiogFUtsoYnwKO5RB4CzFwuKY8pXIfyreVRp9laJ53D21_oJ8J6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ApmMlA2_FmzwLL9OcsV6QChjZcMWwQMnFLcjV2UUMsvkYYV1PDug9qPS9DlxoeoCzS9X5wuKtxCAjdRJi_pIHLcoEfv4hMD1Fcv4Jca7QPoPOeHHGv_f17nd3bgKSNNOzIhvxdxx3MVkV0Ju64t11BdTV_COENXADoV-Ni5Xr60OpVCPx_WFfua2pdzxpe5YxKwi2GhETRdOpHcCDJlZNKZ4qylKqu5t52UHBv8eLHcqWWEZXD5cY7MRxNv2NS1y5rebhO7WqxvRz33qFNt5L0L4nZKc_LS1DfrKRAWECClGRglfHotSagU4r9XFufIk0-VIbRcpcIM_qqQDsSKwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAdmIPz1_jcKa7RkY46As_LYmsJq-r2v5EXLdDo4h1NTHY94TZLxZCiAsFyUIi07g3H0no7s2hllPnNm2KSINnHtwKDXnW-SHQY-spso-8jCIXph1ABRoa6L5OEDukX-4vF93-mUiiNdRc8nCOwHwqoSwaUtSPddRPhBLMAiK8-z8XqPHv2oZRXI2UqPJ6bzlJmZxIqILuWQKJuR4BNFuOudKHNkgaIo8CEYLSYDvnHtEPTdKRP5_BeTOBKKL6yN1CKnUAN7NtZZmb6DZzylsXgBBK-kdeFbey-50zxmENWTeJovNNqhhBsFZV8rPq1IA_Pz7Wr5WzUEt8dB3f_d0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNOQ0g4We1l5xOJBegM4ZvoTKzT61HdOGapFa2bu1vgkwsen2C5OvuPjIIgwGm3z2mDrSu193OF3O7n1nMpg3wS8hmFM3pBFc76vR_No4JGy1fzG3kvaANQxo3RHimyd-F-qaTQKMwKSWTHXEzcwO4nnF3yAMoet-eug08StomEymbg0949bDLNYMR6Q31O2HGSud7wtV4sUsgJm7M_TCuTGIIcmKO_0QZ8JLELiq1TFwtVRXRHGAu5mXdhup03tzy6ZLgAHHGySRK8Yek5-1IDw-EWrZeZ66umoOdqmESX-AS7Xx_QZw3ufDVVO0KmAYMDWt0XVjXQ1R0_qqAwYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ns6hQH7GFzx1uGIaBKYeiS5efgV9WTI29QdFV14Lt_5b4ETv9L3PVD0-78RRfa5wFMwfUKjOGfEsuMidj2_sDsWUvzhAE21esv53PoCAFsleEfAXuRk7C0TzoiODXKM7TYCiQgNg9WADrWyCdQKD8fHKZZfDCm2s9CUBbTCkA8s3stJp46w-ffmYlYrCv8hRm-zLox2Vh_lwyaVTmLoXOECKEXSqT_kd_Ikxc8gXIfa15P2sJqLEtKCtgWXsfUjvCXcPfNB-DiWbzjj-wkkGwL1yI0CtMczoL3tDTJCvNIkEcsh_SSzsQY2DB-e2B4bKqeB_wpMVbkAHzhYbpV9kow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bP2xWUgRBYgKcv8fysO8HyScU_3ntHAsC5pm0BkCjKxp_8S3X2trIuxUMBVKl9BLn4db7fP6ppezuIERmNlflr6sv3uV6ekOaYLufHE_pllPn27cq_Pocw-VnerItcI-xVNpZkyG7glndrM1KFaQ_yqbS7532UCv6wDbrm1Cfmf2Xx0MCFzRdwQmnd8VcY-MWAAoXdX5--s8amc8KLi2nCB-9fSgX0oqFf2VtL_laR_eSAGqA3bq300wc_mzOwnNvj8zNnl5reSGow07-fg57g9fmQ_5aETWNpPsADGYgIFp8e-UMU9YpMP7UCPxxbS0HnCynVJrGGq4ooZlxbt9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LquSPcBVFNXXUbkv01Xz95yXKb_Vt8WErzlwkq743Qc2g8orK8SHFoyZwSfNa4uGmXgs7yWXmLATcHxhZzfRd_GVB3ogtzKCIjRoBSnOLyRPnDo93piib91F7FiMaPYBD38oohqfCcWTY1zjZvpIN7jvOBoTY4pKN78J7CRks6sUPOVqC3r0nuxcKGJWv2ph0-h2VcocMIW19ycgSbtqLGWWCbvsfwoEFOsqnqMjf2nnu4nSh68b_fHreuaDhKTQdCIWaR_ZzYtWWYke6W_G1GPQ2zTWOGM96FLz_omK5vS7JScZuKDy5yp1HbFtvvz9S50AZT5oEy0VzkvdsOxQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eNcZAST2_O8iJ7HqEpDKf0KrupBA4wF0d30cu_pez_ZnjkmL67ZGwD-8wtEik_nESh422wz3B1lTfJXB6KxXs9vRIX19r1dXgtv_4Cj0S5N670NnpABCjxyKhU_OWjxRNjp3ZR61jZUhthSsVxsL-JLXc3vlxbOIIdsY5Ngh5qwJTZ_KOpdzrNHfT0kmsIX9Eqz_hFFMYIarX7yDElNNq_oTW-F3Pdn78apjmWlxyCeZIoIdnOsJ1myjpqissF7Nmw3ZgwUmpiwBVXGGLrWNIeNYtMjj4yUvWjOBNHm3_tPlD0Pwv9TOUKoRz7aXz1t73Y4oPyQb-YowbV8d6Tbwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kWI67Qe938lXgy2cZ7ChEDs8IyKn38bxSOucWQjEHEkqcgtHkXHR57MykbXl2y-lbGdrRytEIxnMb2qj7xLkQPJWYz_-YltfANQZHqfYH9tuYkbD_rFCwoYplkcOS8PP7DjpLFivfyojfNYR2YV__bHtllaHLjCF4Bk43-mRRm8U4TwLGQ08ORQdg8E7rASDDpsdmGDAgr0vV4SAbsOZpBBh9zkWptDPwZUnu45BC88FYUPtlqbCEnu23hssjp-1xcFUb_IEM3ZuEkymMNsh6MrOemJFVUrJhpKv1H-I0ZWCLt5iVJu3AqpBKlBRz95-Qr8bpSCUb334dTeQ_KwRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fX9jKiR2g7CiGpvDxxJU52J6fN-UNVQcE4UIn4JFUs5Bofxa04tUh3WnfjwgREuNwnWNvtXtdvU2MEvEg5tAPEIOKJtAcPzEEcOZOaRv6yKx9GyjHVu4fCCw4L2DcoftLYs5HpSclJ9IxsqaFepADFP9tR1PoG39xSIsVqb2OZHxEFMVCvcfcMhcVevS9VbzpZ-oWzRniVG2-ycRv_rvj-Gzi7zyLqUu0hVz6BrW-WPcFk3HF-H9tGXzgNU0e_i37CBaW_qhVFvMabO2SVMQ-h1QcSZZA2Qmegg0do1tkyA3bk4Ms41rrviFoDjoRElcpU1_obokXOsj9PPfAZwddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vl8l-r-YTOfKXc9l7F04W4o1PVbfPVMhLkPdvdUisi_vmfffuEH2DiwC-ijDnofzH5H52ajbufMPqyUIAEmnv7nM3Svx1Iof3D2GbRQGFIUkT7aNhSTttK_4XhQkQl-uwKl7UKV4MJEmbQeYUpyD57Zq7QBmDlnewC097MrBfFhlhzFykPHx-GNls7xg-RIeDJq0KzzKNYtngQpeutRIw-HtsCxIcWnGUBErr0IHVZLptqdjn5NsNO-LcvVXP9fvN4pPhcj0xtv9MElV27EAWyRb-EiIGFR0ADnGgKfprG6eaDvwCx71rL43VjMHa0Hzuj_jKsv-EqVGMLU9QrsHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hP70TcnGLtU0PXVoRMBAPcPWPP7pagPuQa35kamyaVnJHGcrSdaQOKO9-o5lwo8qRFaakN87ZIlSLnAILCONEBd9y2wLHmTPqqe-nQEQuPRe6CTUAliknC_-5v42G1NMHlpKP_IZO4ZRDDuVDYcTt78VLUelOVoVRlioRfHl4LTPzNuKc74DUUnFNgm4QkxX1Kxyd-epEruin_jH0ypKcoTQuMPa6577rUI_w7tEA8oqLPxKrp8JBEVSvliv0IckZAtfCxSWS-W4GUwd-lg1k9U-72UyFXDiFoy1tAHWqgQMDd79satQBZ9ytVQtff_9jRIAA9wOjJ_AHA45g3bnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFO2u4bwUNSnnHpyL_oJkV0XCD-rerahem6JKZJuWh3W2flH1KCtoKLwEzJOEJoM-tXWdZ_8DaPSqNjNpRMcxTiuJGT5JAK_jRLzX3O6sMHwPAKnhrI9YJknAR0JE8Ar1tisWySmmnUradK-_tOpENEz7TWhq2pZts5QO5eYcas0YMwTeb-Xo7gIRwASNDwd55tkp6oxZ-Eid9W3Wou9-6TU33KbZoZplnMy8c6Zlw_RBvHqxVssi2uKUaYAwOQmYKTS560jlJZKJwaKK3K3sNGRv6HZ9GSd7LFgpJgJnDWDuI90FNatcCj0DC72lJd3ZNaAsLqHpnSn9VFIUv0cXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kWYjzeSoKDV7VLKg23F87Kwv9DGMsFn6CaIU5hg6HjYhmTr13cVw49q08c_8yhHSygzF2Eu_Jpi844dXD2Ey6go0myLueR-J9nvng9yxRaow8XRF4km2PncQLisnXp37xzUk9k_EtHUBZJM6UHldLQaWnm7IOpd6xBZk5sIhztRhsr9vjaZKxwLBl91zpcjSbF3IBMQxH8eDA840d421HEhX77W1oQrXZdL5XoCU4SGWPup6nDIxZxe9EdWGP6QJlOP7sBQkbjyElQhauEBtH9mB6mdZ_BUKLDNjjTJGmgJGWQ85Mp1DIickMijDq6B9sLaU0fM0G1JV1_WE8JEAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxyFU8YJ6N-mi3LA2ROwxIDA38PKy6yNxw2sguIbm_G8lGBsGa0ZkUQJNTdwyoPlkcZUxVnGvCw3NsCMZ3rT5e_mGU3ztQVs-HBhpcq_XDR-Bgqn3KFJEmxfFwi8qCymqJyaCtvzrrqzXIhBap65FcPILt33Xk7UlkTc70ae2TWNznjjPYa7As_CIak-Y06mrVuzXSrZVt02wIBHvVZ_1HQoXyvZMUm3JBhVDLkbufvwlmrQit4JOSNHKZzxm1Emin52W7XuQC7T50PQCkS2TNwHAu9r98w1mn95lkGDEj36NinYB6qKQbHS3imOsYsdDU8yUP8BRzRGkplTDr5HSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-v5VEn-AdezkNEFCvSRlgi5hRsSHaHwAiRS-hcaJ0mrbFKx0lzHQFMAbeq3ui0wbmHzqKyjkZJemAsNmqRzBPwBvRiE5_FvMkCkNIWBOOdSqHULwh8IoXvb67BGXXfm8QTUnRnSL8mtqOlhNEPjQXHJztoEAEtleslAJX9innioimss_Gw86JVmL4gt5Pzm0aZEMHbWm9y5Yt3VO_-UFntPW4v3hoyHOLYa-bR62p5dQJ644temdVUhmzg000XhDamuG-oUdn1iW332YcJS_wSdlU4tmHa9t6QC0mY4fITIvOaOAa-6SXrdDV-5u1gRkp2dZE9hf0Z1PEfs9XZXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glz7nT7NWwiOK5w0nrNMbE9Usdmd4ujAqJGPyKLiFOEl3FBOKb5_QEaBI6cCerXhIOJRfq3B0s81RF4tkLIQ13H63VYXdTLh3x6H0CuBOQR_z9W6tM-nJonvx5qgGrhcoER6Z-rUT7EgKkadNw2hmscGW4Aqzt7Utx7DQnitzARkVgPvOV6_0CU89pb9WjSaF4u-8rUKErDSSQbg_k71BhUDo9RPJSLWfRSoXVm1pkF4NJfMpAzjTVuwyzcc_JxhcGw55PYPGmU_4uUpEPpTb6cOofO_PMCqDSw0e1KlWeuoEOvYnA-U2W7MI9xq-Ax9GMK062TMC6B4O3_a8niIQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PRUBPVKcdgzOPkSdg1wMT4uGd8COS6qQzWSyMvBJ03Y5Ib2Y7o0f-d5m9hVrKim6034jaRWySdSp2EDHHIByJlMU5y0VV5pH4aGX8rf8QpoTWskCPGJjhKL6rrkcN1nVP-l8LX18vZ25ZoUqymHUEDpxQ6oeuTeSpe8cVwHQ2czxcnJ1MAgxhTBAO6jMhbrafmrD5QYssK5DxOp9QClhJZJw2RiQhkMhyTY839D4xPL1iqmK65QCoru8uLBtCXRng2dskK5XyScwQz_slda1vGODpt1xDCfMjY1YOTbScEFB2qhxbF_UjHj8NOh7Q2cs03FlfRrn9GMrrBDbONMgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrFraI970rKspQSRw-KffcnHMiSiaZOeflpMInX0nuhtBi8kdNdIV2qKvxSfZbCKdBz-tpiJRBT-351FzP9IDcAtMmcqY5ekT5C257dCrGwrYoVtAdspMHasbxKM_prZ_H_OoLqtXVXORFA6K7qFv-zUk-NBtaqujQ7m7xzZK5es4x40JxI7ZOEPe6a2-iy7ZB2oa_OMWv3xD35mcDj6CFhN-eCPfz0V1vmq-FN3AyT_pVdLOTG3BduTzzXBRzMklmwnqyjU4jPs678BPiLGmC2U9ZtAxyIV1eA0RsrcMGl6MB4_lb-k8kC88g9SP8Doe9w2aAcN0DKIF08npiyDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jKE3TU_HEpi1NKCR-ZUokYDKHq-7lJV2qSQ7ikzi5cDZmn7YpO-9MWaQqUB-8OCjqd2JTo4j_a2k69bBgbmrsfjS-VHWea_7l6GnNXTfYHqstp7iHVilvkJH-fhLrECqt8qQTCbsLPG0nwYmM09hZrulC7spySid9xQNF1FK78hCxQYNCJFKvd2KPx333ZPlmXlotcXgbcqOtMw2SYN9gTBP3Zt2lQTNJxZVTOS64tKQWxbbrN3mooi_zNb7BGDE45V1-XSFvHJcqiF6erO1REqZpts_7YPqqKjyhgVkhDTrV4rTeLYGx7PCrLQcrjSA_fG4rhdVaf9y0o8qCkk6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=GzMUG-5Or2FSM_igzlizbvLysZ4HIaBQTg1t5A8wkZcsyRG-TVzBqkN3OI39fa7WWFdFiZWKF0WiZ2qabjL7RDHPY8JAd1GUKBwPxls0AMm-AH5VUKp_vjwSosuYtDs2OzmG7odLRLP_1EfrBs6_k8pVuYHa_XafUz5fO_nlYDtLal7wN3EKnxwdGsS8PUmiCCOA3cZxwx-Z_Xkku547P-WrZ_Cwu-nyUbF59fyKgkcYxVhgNPKqLz7qoBMkiGDVTrhR_qs_2ZXQ704ha-WchzOo9z2SdeBXT9Tl867BVeiB3ZCDaiHwITDWHfYKAkNzGGTcBfLFRV345FfNbs-Qmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=GzMUG-5Or2FSM_igzlizbvLysZ4HIaBQTg1t5A8wkZcsyRG-TVzBqkN3OI39fa7WWFdFiZWKF0WiZ2qabjL7RDHPY8JAd1GUKBwPxls0AMm-AH5VUKp_vjwSosuYtDs2OzmG7odLRLP_1EfrBs6_k8pVuYHa_XafUz5fO_nlYDtLal7wN3EKnxwdGsS8PUmiCCOA3cZxwx-Z_Xkku547P-WrZ_Cwu-nyUbF59fyKgkcYxVhgNPKqLz7qoBMkiGDVTrhR_qs_2ZXQ704ha-WchzOo9z2SdeBXT9Tl867BVeiB3ZCDaiHwITDWHfYKAkNzGGTcBfLFRV345FfNbs-Qmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jgMIDeS1-MAr_JOZcVhO_gzeoBstPDdoexePcBOJssgLpd8hLD-mGy-DEiXUVtkZG6GkflvahjZAgBiVgl3vWVwndADcuN8Aw5cO6kK0gEznhjyN4RHnWVUqucY0iyzAHjeMBDHg1-1O8OFopcFLM4rQ4hAkMSlFu4uKuxm713b_gSmttxvhvnI_J_4xc1fVg-xlxgvdwbctt6leBML_ZxZW6xlu4KzSeKhmn_ydel74CqcO5i6_aKd0LDf8oqx9kkTAja383yohloBTOwQZOu6nkHk3Qo9R4GJOO6Ls9YSylxZAIp8yVGmyXnj242zFwsK6KtSt7pmJquAvRr7rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r4rmjIjIBZy32JyPLH9VxDrQTa1rI3mIEls-8bpaAZ2Z5S6_P4sQwnpG6AZfYs35AdzhMJfpPfP2g0p75eVfdbt5vC_nQF8GdjtcxheG4g7lD8AHtkcxQy0BaVASAM8xtfmfmSA-bDhgPWke7wojO-9f2nccHm11tSMgthYOcy6SjW4NboZNPLfRbSnBETjI8k4Z_t-GgXEyeZNHYB3GQLyYkSJWpUa2Z07J4J0TOUXyfeAq_CtnVf86lJZnE4NTDQgagd_8cD9k9d63Spozia2aEU2c1ycAepphjZNT1BNV2Mri11ShZSg9sKRsP_mH1-YIO1-2cTyH_xJu7O5eDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAQQx1Qg_73Xftkn_3th2bJiO4tBKRCWK9fn3AmjEkDGCO7DNnffT02bYclWXqnTRP5u_mqH8qxRW66UdLR_09uz-JOlio4uxTuj2ogY3n70Q2lOwWJDd341FjAaXl0M6rYErh1pXo8Be58nil1qiQNvZFxsX4h3ShbHqak4xjh4i5AvawAQyr0ESVidi4Pd3uNMG4dbrKuuhJ8ecPjk3LndBpq90sDUGThNFQJ75WxHfMtPHd631escZfkCeM5c25NdYtFlCWPhnQTcjzwj3HIqRq3V4BXO1h9RhZttXELYbtK_jVuON6qyQcJlDhxnj-V9X8TV9fqbo8EUgFU8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vxwv4SlRIvivNZpLcuV8Xew3G13RdWLBkqu3J6bg21qsuph-gAk_FFP2AA8VEhrsMai0BdGwDb6V-jprb5cD3BRapx0vAdMxVQK0OP3nezhnam_1dbhMsiEPoxV2UIdXsWUhHWSoBMPLXgYFkiYVPYtvuRLvrTsrQlubB9BxM8CgmXccIKTPBn4WPZWQka4p57zwFp9kMnn9kW-BBMsFZKJu1dZclt80fLE3BnhP9INnNR56Fny9Emwyv-n6iNVrzrvZProMcLsg2KdD8wfU7GM-PEKPPqZ8GkBJ-5MUZi4tQdQGeYjWjdrOMsZlPavFiJTrA6pWsrAmjCsS2mflaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZXPRyotCBWx3s3Saukg63yi4aAkzweSvfuexWtvrtDoLhJqRpjYhEfv2FrwW1o5cl6_vJt4hyl4apKU6BVnVURqGD60_JPXp2J8TSK5p5X7HBYroffRpBZiaBnr7qMHm0AAAzwkU9K57BFGmVUAK2_apq3Ba47zUVZGOw-NBaHW65ajWuEt-GW5k6Ccte2Cr1h6XrjxHJ5hi72ebuI1qiT0UVWEHK4a2ddoaa9YG4TxFtvh_j7FvAybEnYe3iHUIPdRaIo0Gc8gd5fbVt9_-IRQS5wD7l52ZvLMqPL-plgNecWGxvaKjl9WGtoDC3iyx52m_38hrc4V5hYTe5kV-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G-vT2boQSWb1FRPZqVj6kvxhKc24XpJIf3k3B0kf4pf9a1HM9FfCw_1xoX1NF1YUAumronQibaKNKgzMykgAawRYwCHkcvxfrTYOXmOe0GGYjQvw4s6lE9GXH7-WTB5SNcNXbER2H-DsjP98HiyRv8BvS1FQqWzp-FEVZU1Nz5feTR9UlsuodIBcVkGyX5OKubvYgAzXV9Ure2M1y7UAf8sn44Z1okZqyJcAIlwPgAdKEkkLbEURdDepyVViMCq5nnayXa0zfs2nPuQTvcSfvcbL0Al18oUv69RO78rAbfcZDnQrTbNwAJlMYEI_gp3MrM9MLTwD3fuyxDmPClj7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XQSxYiAVS4-GLTr8apX4jGjOUMoJtfLsx4prEfuE2Cne8UhVBw8soSiA6xXYdnWmK8L7Pm9ZSZAA9Y6SOEg0z4Jg19b6i1jKYhuN8v0a4ADF9Liwax4UUhCOSK_Me6fe1vw-9xczf7p1Gsk9UQDudUHSxYzbCc2zbPaEVSE9emAHDgSXna9gHfPahrDErs35umQQFaFYOkMCNWgdXPcLd42pQzqSuwy2563laxFSHZjKtfeQHw-__eF5USQs9F68tfzCCy4l5GTg7BzOT5J1xXH1MIC-f801l_nkf3F0gYG1Dv_DuPPkIr2wwTG9dPBY25ssml-HDmRLQlAwiCqD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ivyjWaMgOAd67UQY45-6OFCpNjn4SHfrwiJTRFMgZ8MOEgAE8DMkws1g9Z0OgkZ6QDEfInI2X7U73SRruoUCLdKNhXOODhCAXbpDHY7oXV_Y0y9_INWW0gc9Vo-v_qOnv60uNblYHjDzBpUTiu-mHLxfO6UQAAPujiImFWLEgvpBs7GUg7XftDkSP5nx-_Kyz7CEj4upVaUv_vl5KjGbIF2zOG_SPlhOJ3vjEgSrO615WuKW5paoHHKfWH75FPzBesfdJtpDjc4JkOSHs4ZFmE6wLc-7DqdX0UWk_SVNt2o3BS5sG4NWJUH5h3p_s9JyBrccsH7F5fm6yOHrL9g4zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cx-qFym0H_Dgd1jXBBUtuP0GN38RiCHFzQchgEV_e5qXAzco2_SbgTwKfDE69JgyKwx_UYJszLxpn9_ufLWEbBr9VginnomfnGHyWIqbL023g5Cdq-sHPMxZ2N6beMGY4VlJYBMNGanIPDBmyOD3zEATjcZ8iRatPvvF018Z-3qJ1FVVM3uW9hnklK2it_oIqxPysZ4_JzSjWH4eVPGUerM3MorL_-FoLOCse5oSNPk0ldT82x2a6OxXUBOT1gxOwREqSMgzayiNdLY3-LKBkWCOJ_dTTWjN-CirbtDXgPynd7dbYUSx2IdHMi9qldIGinZ1FGD9n0IfT5rJWfqwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ra4Q5JZcjqjWWBxBBbDGFmCoFpw0TRW6RRfbBUZWmikoIxgfQWYi5bRLSgtJXBLleao3tJnUD3yc9lxYBfiOE3tPEMbJSvBe_4ZVHrfyWOwOX2RhdJrh0Cp864TYlf0CUpWv9bEloIg0cl-2GGeeKAzJqIP52wQIOMqVrR4JE10Sm-ZFSU8yhUNMxEmXZZHVLeruRnlSD-b_frrzXpBpIuoBwIlWYCpXhcPXi8m69_l0W6qP8s_ovyD4CraYEXutMa4Fi3FoyY6inPwDtbopqgFiOsgN2dsaKESMbdJ2tLs1nYipSEZiTrxGLrN6F_QANkSac6YOX8fDasZSYTXYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l4gQT3zguLnctptWWXzF_ksTpJ8xv-BuQKgmgPIoDdzR7rq4F49vEb6HrtNErcm-pxbj6Khv7viShQTeTB8vL502_T36XpERW9rtggSZEDGCcnolxUmitQ7z44fXjxOFh6uDDHOVahVS2vW50NDcyed6Nk2bSG9kRVk5suRno9-gzqscOLXKGoxSlpR4Mcwf-ytZu-ZCdkEUNp2LeN67KwhhswBfKwj0cF1uoD-Cw-Y_Nt60bg4bWvey23A7ZBnxk9p8ZQwhwu9ehLYqtg-lYUgjUW5A6u4J9sLpVpDAluaH3lcY36XdkKRS9wmrDhfjzpcfq25qpZLK3h0_OFH55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v-DhDeE5fyybOuxkgrTJGD8Mvqj7_Z4rOOg3paK7d7EQmj589_x8y2XP75u3szHDS-eC8275m4j-cO6ohHrzJlp0y6Sj35YRJaQK8hxzzxT2Tpfh1hqB4YMay20JJd3nQTZEHNjZsHFpK3J4nfR6q0ZcoiM2hS8fQfXgBm4Fnjhv1PyC8gthP107p28dayc9LGQ6-ETXr7YNSv5NOuqjwpNjMdpKAWCkzJYP8kxrFA0gCAuz2ewOHY2xxMm8RTo4-Dn-WtQ5-D-x_GB-cLs0ih_Wla1r9h_U9wtOWKdrw4Mj6RCdv9epsdFuLo9azjqPjCgxIjeMAoGyRkHhwcraHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjOCfuQezIVZKX7LTiF1Nkcj1X6dsX_H4AOu_EzsRepVIh0GeTO3IvYfk0oCnLvxsQdQZuM292DcV_MpjP3pAL-fTOwDd7K-lTzrlcxYNeYGvE0ad4btG1pQmkm3wQfCx2j6tv9rNqJm7MatgZiaBf_g33g9Xg5Judq7hFNsv1UYW8N-yZL9Onx4A5XdE63KY1RfIIeu1FAZf4qHFiIAdpPdAXEzj2rJGaKeQN8-d3MyTMUwHF_ne9DqMlu4RTd5dMsM9lkUvxIDfZ59S4BmhwikLiuW47SEgi8cZVXtGVE3KFitA1BBD7qNACzkU_tLcIRJHdHO6i9U0UajLhaRgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LeXDQ3xK0P0IIoFqs31DpaRPNjAbcpE58JEM66ZkvkQWH4IjApJ2Je09ik3qVT6MK22vHNVt4PR8rupIEvBh-CUVQuFCxxfXgLHJcFKfZhma5t3KZhiE58BuX0eWSPNK5TJ6ZP7fVd6wJlSGCBu5TRfFDIdpfYYzbvJzy10WH8s7T-YmyZcvLTJTs6og3aWO_Ez2YLv9m7UTZJ7bKY8dN-h5r2FwHMpe0q-2NyGXN8hixkARlBA4vgXs518IX6S7uNKgT_ZPAThVj-2AAeMoL55ab9oCXs1M4IKKzvinhA3hOqPTeVoHJWpjzZYREF2iQyURQ1666D1E0WKmUdH6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bm7s9TnxopAbEz--az-E-Isk1fTGYOsUgPQQZp7Asuk-rpRAgm_t7ElozOze1X9V2udTNuAv_ShF-Saj12C5H5sCjHa6eh9TzCYq-y2HvIa-4IKbnokUnEIE4NlKDFu77dZ3hxUu6cnB9MBZKINKX-kQF2ZT9opQzZl0G-BMsykFUCzlT9gizgsUUtdZs73vtzeGeG8-XLq7uiDNInw1Y7mN0rEH33K6AtdMvedvW5aiqT1Quq4qP_MFB5RSdwWn1TqtdIsYPTMoGyGP6g1znxY8oesECuk4-IDU66w-3kYop57Hb_lgxSN1eLO8T0-hM_I0-l3-sfLq0qZNkdt3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CGFHatRnp91HtkoeUzno5KfB1tD-awSLUzGEAQppb9UpcOttYbJRjb5SFwsByymGWb_uGkzkxzSXWsiAJtZ9xUnThRETeRnqbuAQqotaJLEmkFpLCxt9CfgzRs1VEQvmbB9kYkG6K2rLS0s_W15BDcONNe9XQmuCboQcfcDhRx6f2llertua2Ynsk3koXnXvOPj5ub7exjljqLv8hc5cQvxmsilKFvNKQQ5PFUDDblvmjTQTKl_laO5JvW5zVvDOfTBuhN_0JCZRuValzOWXVCnNNDprRTiR8pOBgtTaUfnjLU-fcpb7xXkPmP5aNe5-TeDFlgbixYmQnPUStPObZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQig34qqN6BK9Ulx2pC3wO61Ngez19xqcAbZ1Ss1mJYG_klUXAXRUP_4OEJ9lEcFWtQE8c8v1XbJMZVBof94CATg5ZeUuJvKn80vitIskG2N1arRi3zpuu-e8NpBTdkRtPOhvpGGX0886upjaSTE10P_4z9vy4EO027Ufd7Vdz0pg271kDNwHNeT7jMGhSm2LdlXiyAMtEWW5nY5VshLtpPlnEIMXXwFd88f5nI2xgOajO3aA2EJ78_rcb1U1Mdc9dV6cwGFXOGlvrHXu4df3vGJa36IjvbboOGmCya_4vEvotKBrsO-8ofzbWEyHt1zuSCurAW7eN0guNWjxaJ7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dUkDZt3xSz276J81JzcrtOU7Ge_BWrxAzKstb9xIS9tmVr2cE-gIZOtVCB3EQQaSqOjF05CVyazKabatWoS6ifBTeNPOOqzi2k5QtfOaz7wEoziSIl9ug5t3nA3SbfutLvKIPAopvQMoipyPqzNWFaXyMvsTX7lB7IryjivNL83oOH7ZQVSP_2A9Kg328o7q05VaqHF68Aj7xJotCUorBqPS1-Bu_N7oORasFyKl9GB6OD_GFh-2VRLHH048UA7UfzacoJ9NU1wyfZnnvg1jcjURlOHpA883vREJ5lVw1MH5EmXsZrNAmYqv4LQdje8OGkWxGG0K6Is57IbDpugamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcHT1gYNs68IwJ-myyk0hCJO7jBtl1tkf-D_X91Einbz9YoI_ps6wxrRWwPM4zKbAxsCmDRqF0-KbaANj2Rxw7udy9fdFfwL3g079cxbbcSFGe8eJv_n1g11kJfwj4dHngvfz6rhzI_S64u0hW1X3jX6nbES0x5MZlFvqbgdI73LYOoe29iDt4L3znbkeslOJf0J_b5ESlA7YpztW2jb0LYwVsE-QiSqwILVn-umtytKm-QWfWvfJwtEBx52caeB5xaS9hlbyj8bqbWQbtXMhdltZwUXqIvNlZ1UvqlOhYOFLqaoU71HDJvQCMri-aoduSLzyseW90CGTA65b2gU6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UqWQYj24hMbETcFnOZwNA7kiHahIT9sqbpjEzD3h9PrcWEFCZgSXFJnHnuHCFU72DNCCDSXJjxe5Xl09VmIj_UT5x-Hu4CKppsT12amPs3qquymL0Ht4JCUF_nQqMbPW_rWeJG1zfDEFCeBdeQ-89EBqg8d2HqzpJzN3eqi1fcg5_dPnyZ1BfpQ4IlLBC-4Z-Kb2e4fX13pfnUOIeCFbgwn1nCQKMrhERhZntv7vBqcPp43pW4CK9aqTxA1IhNO7QIysKo9zCpDYbFVAlJOlVJ3EPq-zH-nMw3jQajWJDd5oZxKYUWFCZzWAc5Z9FwQzt9-ym3pykniSiHi4pG1eeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ruaO1ntwv0jTf35Dsn91MJHxnZrjLkh1USgJT7clrfIEt7AzosLb1HV59sRcuAJZjHBkxj3HvHVbM2C6_4HoKlKy4ib6fo3EQWj4Sj20PdRh1-ce_qMah1atC3kh-EGEWRUfwTt0JmaKj-99DS35ZYBcTjtHGBrf33OL0O2Fy1hdzNRdgu2CLmjNoT4dA59Dlo7bejzlt4E7ygJ10CdXTwxeENbcpjf2IanZVi1j1TsVqAqFcewWCbjzXbCW5195X8c_nGP9Cwo034cb7ZnQ8VndqcwuIIdsJgzoUzF6XuoByhwgTQvQ6uLnwVBZHcZ-eLeinef_lqij3-e85wmEHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYSJCuIsXkVFG4_0TI-98YTJB7iOnHy1qRJnX42ECfQ59ejfhNgVmJyWPbeXOQ0_WQxC5Rz7JD4IM2PUyWQFZrH_oxmLac-ROxGid6PS9iYeKD8dQbSHIQtWBonxR255LNp0-d6xP6pN2U0EfGr5O11eZ23-sYdV-145FLyEiJKa5rDjni3JOMON_bDtSnjzu2YScQ1CwESZrAAZafKcQmsWrKG2kilMb0Bas7DEELEErDQGCogseTi8Ggo4cBCsjiAJrHoHu2YfYkHrtr7gDyT35_TTSvnbzm7C1mKJ0uR9pNQDHPbhoaDMPLBEKLrzA8_hBUtrjt2UxSvQ-MJ3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qhir7vNMHE5zWSJzkYSt_yy3CVJe1Z03TC3Q881JID5EnpiehN8G7yBULHHTlCI-IglkeMcBeAuR5NtP5VAObSv_zrl_NdXtvdv11kOvNyQjB7iaa9cncgiec9rQmxKFqnwE85AY3I60n4PQWULdaU9MRnLsnRoCrJF07lLnVhIo3NnM_C2Y9-Ox8an3Bo0hgh1PkXGsRQWoyCticns6SoFfI6S7yGZupcdbIWJuybuxdDFnzlg9Ts6dSxaq3pYTgSO8lmFuz5KXS2E-Jj_5-0W1XqsxpVPhBsgWp8y5n-QKj_naHYMJdCUu_EejiYoJTKh5R4-K5NrLO8CVppE7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJauuwM-iI00ewEbHDGGO0yIEhqV_r2i2xQwzH0_etTfuPGISZOBb-bVyHxQqWt2yESbH-ZpmQsslCK4D8xpegNzeMRzSQrzrWksdHAG5dLe39rI33AnEVFG4Fmi7VMYxhzjQsDdbzfqAQr-34BCG9HT4qwp920z3ITyFGOqt6oVF9CIxbb3l6C4qmpvMGIh1r5X85v1eJmpRkjQvuJyY6mcgzZbD68NDrQAERjHHXAu04Fus4R7XGLrl33A5ZQvDOnmNgKTSTDH6nEscj78qmL9CBBFwm-euPLLWIXM1Ucy49cCLaUf4TlwBbcF-t6aQwBH_fWxsLa6qkG4z1iUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OwGdXREHaKRAC9e-lXLfH6qt_-T_mVpDF9ypt3yIwugWsZDF93Z07MNSV3iDjqRXBjwEBfnDA5WSqo9mDKkjNDUBT3EzisV2smYVGKqaefZ3Oz2_RtmKQu6xvTUlZmRUsyh_lUg-ZhPvbSMP1bbhkDKsnmRZrLJuZBJ6qj-RpfmTQVIZHwx7XWAy4pLtEJpEUXFslIyZjYA97nY26AkvkPCXd86xKi2aXpwdfSEVytec_PJU0LBB97C62zNkQgGdbzxgVtKWsZPZOWu06XSi_aaKo2NuXvaVrwNIqhtNIC6EaIRlpL8QZdu4Gg7Yunm7XfPZStZRG_8PZW04jr35Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=eRvtM-Fm-EPEkYjQlT6lAdkhIErMmsrZlnAkT79M9NJ1lxWfjEUHFX4ppDLeddRk6momnVov38mcnQkwyZnOZQiyUxzjCMRVPIR6jfdXNK4g0MN1KadfdabGEMDVo6g8M6u0luZXE0N1lEVOYGE2CO8xbFq_3o5n7Cv9gSHRidWNHm-EyReSPVVQEtznyDLlfPnK_fbDXXOEBs7ZoRiiukbGptBYDByzC7ym60mFKgRzaj0QjO6qlt9GFAStJONUVaMQQ4fWz_PlU4rkd8797SsPz2ownN3u_zOPfcB-uWeC9XuiJeKmd7AXbonWGueyac523-fEgtv0RDLRUjkeiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=eRvtM-Fm-EPEkYjQlT6lAdkhIErMmsrZlnAkT79M9NJ1lxWfjEUHFX4ppDLeddRk6momnVov38mcnQkwyZnOZQiyUxzjCMRVPIR6jfdXNK4g0MN1KadfdabGEMDVo6g8M6u0luZXE0N1lEVOYGE2CO8xbFq_3o5n7Cv9gSHRidWNHm-EyReSPVVQEtznyDLlfPnK_fbDXXOEBs7ZoRiiukbGptBYDByzC7ym60mFKgRzaj0QjO6qlt9GFAStJONUVaMQQ4fWz_PlU4rkd8797SsPz2ownN3u_zOPfcB-uWeC9XuiJeKmd7AXbonWGueyac523-fEgtv0RDLRUjkeiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
