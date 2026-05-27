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
<p>@ircfspace • 👥 97.2K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 23:32:33</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P9pmfVDU0QwltRlS-aAMI1ZjDsIBS9KgCZhLpEAht0H_CXYsomxgibifK7akD1fI0GAQ4vDIka82c3zAxNeudgIN3_3cdHH-cYZ4Oniil00Rr59ZEpnLwYq0MNg5a9MoOraIB8ejCqD-BJ0KJ0KQF2NmSSeqY3LCqiR6YinKLBxHIriCN8VSu6v6lWsstNjcOI1D89mP48LnfkuddSBUcA6iO8Q0Vy57ywC8t-hB4BV4vw3-4jMuIQ3WHUWCHRENBExDQlKBnqlmpskZrAPLy4O4RosupSxb61wxg1Dr1zGFWN-wIxKfWvj3l8ImPxbki-iLNnfyUzk9kXUdbYmBJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oviW6vuVCs6m8rBdiIB2Xae6OWZGc5kaf9Msm-ZPZgXS2uubLHXP-s7FN4V5RFX5W0RIVsxPUqre_8yuPW3LtgTTxXgsG72U03CvZafhTJb6lMZI7TOokU1q5R5qLiCzZ0g3yB_WPPPu5aHwknBOGwxWn3JOQ4uerrO3_HApN5U50eQj0eFg--K8UpeSX5ORWFEzwi1MuQHS5qZ1sXBCY6C4RY4fnf00uzFEPOn6kgoEpGVKAs84jOOR8HAbBczMBEYHfO9bJlWwO1i6pruT9eMPSRGGna1I0KziFuzQHtkWA8gdc6lYLErP6OVvCknIlN8DFICZHJKGbxKMSmQF3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eiBOLpBvG2j6m0J_RCQ_pgk5UoAwYsiWPAh04mXHFWKV7iFYHHwNWyBrFp6UD9AKlOfWGAV1N9jP0ZL-MhplUuD7dUVfavL-dgmaQtbyhf4bAsAl16S6NiwUEqLYf4NRy-k5vp3X4fmc-qZ2tmWX68ZIIKh6tQZuKoH9HgN0wJ7I4tbsbkr1Np6GnbG66_SJ8pvlccC6mQ5qPK0ADHOi-_zFo8S8ECDWhJ3HyhGfhDD_ycY575UIPDMU25x-0SR2fCPE1jflKPGWtLV3RZAIXGCc_BB1X0KkQB0sLxnlf1IybgtxZINPIo09Kw3znmRLYohUBUrKtwBKwNAaKHeSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KzQ08fnAPOnbbO4L-FVXmJ_rxN5XBjFANA34J7i0WdRSJ-6OfnPAgo8brgtiM-NVd6e0VXBKw1eF6uuXv4trtXv-k-iAaOcAfOvqCD9ZRD6jDh6fhnSeIf_ewkeYdZaWSNN0-n27dNFwhwexNaC7oGtYss3fM-BrnblFXydcsNDX2GoiLYdPBXZOjWwwjx5RlL56LmsoCOVODTMclmgWW0TimlUiINj8ywOSClI8Y0--SCHFzlCIRL1sG8bNAzbihFpfvQIZJlIbBIlKYPRtnRFGVnqLwB18UfWmJ0X0m7xKw-FbmuEkyOBHZJOmZulvULmIyJldf9_peY16RCSpeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZV5JYHt7AnAcXsqyJv_Bz_-c6edPSo03Hw80-MPxuKJnYJ4ufE3DW1bQFu3E7CgGZ7xOAQ0DppVpgaqJSW0gFlHEq8woyWezBGDAJlcldGCodHW9MTJk414LKX1bZohTStsEBPeDUaQzEhiw3yJ9i9qqUZ-nomrGL6mKkKr-x8jemWLF1wyZrqU8p0UXSWUajQDqZJsWymhXHnFdE-eZLQGZX7uGTDmeb6Npr51j47Rb29m_2EFY7taJik93Gn-bdQS7fKHeYrzixIq96wNEGHQvzMR3ykh9v44VJqeOK5rSe9Sy4_xY0uINIo8m_2wyKYGtE9lJq6Sm1OU9i4qFXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TENtwWlvXf3IpZjRmJQT4JyHzZJ2-HnzWdPUqJ6tCgI0WGZ0UxoPQnTkErMsMoivOmcVCn7xeJQXlKqVZi8f3wwQ2hGhO2yCoIk2GZ-a9VlbS3Bl_PAIbJdhY4w9hDjYTQmtkjvPXvTuGjo0oOLtUcJtLHzADXkJ4BsblozGZ0V344IwiQ44dR0eTL6zq3NDLOwXZpUARInOtI4ozNBM9uICIRMUlFm243OEBILbyDowzpZOmFkLVmla8oMYwsUXGpXbaKcame2_Y1oTf39Ytl-KynZlJUt2MgAEWFrWQhBTZ5KfzgBbnONppm1YVSIpPr1vlsQyxPnNUqK5E9sVEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VVv2i7yVXxd5N-RuEMoxK_l7Nw8d_8Xa-R_EFXfSTDBgh-hqlE-0Yahq-qgCiAJlaix63zQ1ULobig-n_v4YnYGrLSO_Ym05BY13RSP18HU7cDO82ItDUigbEicvFttBpEbLWTOVld-mKmYJuSMI5QzHBSOC-qwJXnHcv6RgkGgY-3sSxb0qEz-kOvFTGEQN_-wp2Ky6VnzHOX6fi8k7QFdUI5U061RP5WZywUFknCHc_Wzgl0ctoke8B3yXE4n1JWrEmmBwYg9skWFyXFNronc2MMpiBo4gm4pQ03rqR8hlxW7-fY-2Wq48-QC5ObFailM0WW93M6c5gSm0msVWNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MjmB-kr8ZDrZKl3qB1HeuPYD0VgzwsdRjE8_EHNojflk-j5yIvCvGVdyQYIjMSo6OrcRVgLOoNoBxv9AxHi4RSZ0xV8Js5RO7YWs9qMjQTb_MawVNdKbOXHiHbki2XMZiLW-DO_RR6azb7ZILPj8JokVL2KCEHcgjyrM4BfnDR4GmZiLFWGCA9IeIpW0zA2xiKoq-5Yk6hlBy7eA_YxTLECVhJ0JYiTN6Tn0xtMq4-RFmGAk5lQ5mNi711_T9qwnGh8uBAtnfexzKY-lOJB7Itp2jaZcLrzLPAEOSQjgS8KS9DT6vLlma9cu98xy2lkLd4QzmBrSxOj4GwDRL_eJfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YB6YSFTeZXP3UvkSRtBBqHaY86bPVp3RA-TG8GXfV8snWVz9xiNf90Rj_pYzb8nlPLfGkZ1CFCfsIxD9jmzzTej6Gr8HCU2RpfHe7fusBU_bF8nNPCZ-x8BhFucPYJtHxGtH8t5KsdNPscsEb8D5woFF930q9vDRXBLNObMgpFGNhnWZF5yp0tp5oEb2wwLx0EmBwrASL0AQBHuIZJJ-zAP_qVY8wpQfLU1knJHskbhxnqRHEJymFYrtr24CPJpFGKKgl1RfMNW7khL64AFpjeSSPQ6MxwO0MLCPqMvfIOiMSUSqE92WCsJg6t6pVkl5ng_Gs9ibGg4Iu-6ytuCYvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9YLOYzH1o4akStBbn7Qm_6M_i6INsHO6IotyuPLOFvVIqkliM6t2Jl-aVCiiEfgFcShoYasCNJCJQErAEY5Rw8VdhAtzSIynVQotw9GJVJEPb6nheAZ5EKrXL4yLPmt20Zx4m6cXfMPCu4VX4mi6bHgO1zRhEOcPgUg0UGwAGfQCx27xN6EH5RUbDYl67UGEY5XAWiBmD5IE4Re9hF3cabGsLiIgyR2Ek8hDF5O_gDkRcCsfeYe7dXzR6bYEIivesPrx7DdHcyrW2t-eZoHNPuuyJ7ENSdzw8tE9s1mXKb9DtgLXU63FBSBPi-LDDBV5GS1A-GAJ7HBSiU3vrO9Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A1f_-qjjLZvn5ajh8oJ7tbdwsa0ihfB2u3mpz_VMEgcmjPWmSKCfO888hX4Y0zyRXHFkfri5qoOg2TqzMv6bh7-wycirwyrqZiXsD1vfbI7RyWsHq8Od70Q2oncIVBLkfvb_7T9KGn837HqHaMjMca6aEfOpnOygdenkXDN4NyBbAmrqNyNkxo2gRvzPEHpDocG2SQHmRXkEVTIcG9IA2SQCDmMsJCvn3aFrgmCoUiih_jQE7hY0uSgo8Qbi8jH2X-cc82KUCmxHAgi9puOB7Rof_m26GmQinpivOKGZINw3KFZsKZ5dB_vcwCm3aRM701QEZIPMeYE-VCFEiuGlOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IwVG5HgonhIIXS8kbad-C41oJnE8JZVgA5S_YB6qsEQzjwHaVdEBt-pPcImxrZwC2C6bmUFumvDvD4eehk9iyP_aCbVaBmlIWg4rSRNJD18UDZgwKKKzuvl5NaAEWxkaIrPZXGd6J6V2W9GFYo32asLcJX3bDcHuGjGayRNW9RoZxwHZGLLNCSbny61bl7tLaPHdVPAfbozMSUDqUMQAGKCL5Ni9PMwUvBUwpWW16_TiLpamV0Z81eK6MgmJdQ_a_eGNmr4zRqPElgQHQsU5Qh3qi1BglqshnNY6uWZDfxRAaPBZq3gLgs4CbxBb-DY1WB-pRmjQ64DhKaRPvQWA1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AP7xIT0xs7PuB6OzJF4p9IikmBObLwhX6uVCAfu-cqamLDTKXIrgl9DP2QbPDu7WEiqj-XBFUWcr0U0rnGL_ofzdL-JvvqyDDwZXIUpYiWyhaQYtqzbf1y7pviIPFynvXlKMONtQxre1y2lzQmP4NEl8PSPR13LvXXojBq193jQHW-MpFKEpC6Sk-TsuggKfbheXiyQpPob8JYLckzgGRoDrCrUBccfYuyUmX0S7Xlvf-9hJ3cF7TOOBwtw13x9oCSooNghpSq7PdEZgv_KtZOEG7915rQ4FnAHUhx0DJ4sUvxg4DbDfa5jWxB48gUSaHuI6wAJNCGtMAjLeXz8Fmg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=bHhGSocanmRs0yFRoLI7iy2NzV-01R38bn1a2GqucLP5siDaEolbakboVIe_C-9ocyr8GiWFScbOVAYhGyOoKJ513XqGS9gMRuZJA6gxHIP0IPpMkgRc2V5MO9Wsj_4UjxkPgfg3JD20IsURNhrniaDKtAQsAaCCc2QaPCs7BjQxEp6OyZXy6qQrQEFo_JoqQlt_URLp39GWDbyxVUKLP-WBitvKdKBhCWVY1ZtGsS5XZ8fCGQ24dBMyyTt58gGqEG8A5Zph9UMgQXY68RqNYmj2TjqdtqyhHPdDxmMZZoWzo-xNEeF7famrnOHH13oeV5JuD95qBNG6mT_9iIoQ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=bHhGSocanmRs0yFRoLI7iy2NzV-01R38bn1a2GqucLP5siDaEolbakboVIe_C-9ocyr8GiWFScbOVAYhGyOoKJ513XqGS9gMRuZJA6gxHIP0IPpMkgRc2V5MO9Wsj_4UjxkPgfg3JD20IsURNhrniaDKtAQsAaCCc2QaPCs7BjQxEp6OyZXy6qQrQEFo_JoqQlt_URLp39GWDbyxVUKLP-WBitvKdKBhCWVY1ZtGsS5XZ8fCGQ24dBMyyTt58gGqEG8A5Zph9UMgQXY68RqNYmj2TjqdtqyhHPdDxmMZZoWzo-xNEeF7famrnOHH13oeV5JuD95qBNG6mT_9iIoQ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9XmCflsce0THshqiTO-TdPc_YfNwXmbHJMLlH1c4Ad-shm0a6SJZM31Qu_RkFvPrxmvjyZvNEcz0VW9RnJX2JEUTkVjLG87oGkpYZ8bORKAezCMWlIdWBlNzDazLCZbgvnBmNiISzbeawxOHftaHCrLESi8jFNkjZ74CIcw6EeQtRmoCEaSMQtdQ_Mfv7w7ph6eUNTCI5TnoiJkmOdTdhQ088Lvj7oU4EMXzQShg7XiSvtb756ZfAaxiV01sz77YWBoOkO_5u4W1raY0-QGq7RF3NXEJyoQF8rOgR_CDYJ1N2H2dsrJfwiQpzCqKDTZxacBq4a76vwXixMWVtICMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/quhXtTBEdeye6GzdVN4FXHaBLS7ajErddssBEdNRjp-Y0QnhIuyMhTwpObOHC4XRjv2nh5XN5QhPVN9JzmjUD9YkQX0JEBBgCWebWz5qyP4cta1FCcH1bKmSio7fhEdgABvWzvj31-Nah_7Tcw4yBkSD_Yns525R9F38C7hM89i51Ao6ojgMcFuT5O-BGUw8aMsombecZaWUhW9tcAVcbfAj7qTxPf1RedRKCO_aR0MPIQyjU2H9c7_S3oN2VGa2HPH26aKI1pHQmfe0ZKpYjpfNSMtvrhCzQwTjQwJ_bl06ODJ9B_8YBOYRywLPOpzhahr5AmlczAcEkInaLFmq-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SjLZZvlT3OWjzRG3yhF9_AR5UPfX5fmE1hwMiko2wre5adM9vyreWFbckOpKkYLjdGHfhZcHPj9M5BHr4SdvHC0yo2OTFb3PrbEKNow-uVJQXEEeG4K6GS2Y3hQiWo2qHZVnPxI-g8pQQs8dP839hT3vuk3Pro9D1143KdI5ojTW4yFxcWHHgj3ELvq6D7zKFqTctajSdGw3xy2Fc8Tkq0DiYrcIgAtciOYAGwv_GbGeUlU0rQcbWcEydkZ9PW4H_q70obiy2ih5WbVwtlrFNw_NJWSiKWp3HR0ynMhkkrsh5hc4tVgzDO_ftqqkOhcaZ6afvsq2TjAIcVxETGqtIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3-siKV7uFqLCq_gF--U8YQ3Eqnh5B1vHeoaKHv75j5YKoLVGwKlywESRRUm_FaPaqIXubRo-AyduoaXYOAg8vBdO5S2M_GuebU5yfR164XPFXy_GbnVNETgP9DG67x9_Civ1vXH7s4ray-Vo9n1C5GP8L7X-w2gI61dOfXhkVwPCb-m58PPHbJT3lX1SVnx4hvWRKE2hIFlA4Mn0TIoghlbb0qh49A21BDNFKytwXWYiRdGfK46yKVeBxH0HPpM6mEjXmZfnENau_DFNpo_NE33Zp3PfjtwHDTMaAtRdMjgxNGyeLzlj1UtjTVh21NKkEiaCZKT98DM_S-GMQ7uGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKOGQrUhB9Y7LVjXWuqRKTS0Wr4SGOzTVedInGEVcuthulHnMwspCYK8I5PWaWUXPuGFm6knBr-b38ZhRwHTAJ6Pi7Ooc74lj5Ljg4Gyg3ODDSsO8OQZLV7K5wXYmnBsTOp00KZN7fVCy4r7wUnTlztv480gFEMiKhT6Y7Cgp-pQJ-vKh8g4YGgUfQatKMmASiMPYllqmlYmIqUHynBx_QG9ynOCOeCzZ-vuBbOpwZFohaIPqyCIDSWRy6851dmrIGkZI8QatS-mIsVX_eQidk77yjH0QF1eryZVTPy08hoWhsy7AtTIfJhjH-qQud6MK_MaAShstQdkkLKljtIZRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VdyGSebEVBkrN1JtoeqkotyFrMeMXg11B6qsuV1Ty9tBlqLr6UGMlA7Pol65B-E5IhdX1z4hhrxcCDxOw2WfHBCUFLWxu2htsHE21HIIkhjX3bpiBDG5ryvGS1KWPsjKTOvZ6_gCWc6yD7UP1HrsLVp1NoAohKESCKft7CIpb72vLvT3YH-ip--3mr1Fux8NMJY6ihUUaUCwdUX2mZH9O-nJyUkfvrjiL2nLXT5nauORmoRF4eLmay33owFp1erFvGjwO-Ea2MIlyl5jOHEefv_5cTIQpjchkAFBccbNH3XG4aS-c7BJ7ghdMhl-_vq2t9-BlmZOBbkK_QAIl9A6WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u-GWyavGpt1kZ_ocbX428VO_8cHRIMhcarNtEnT2-utSVVJ-fX3ys5gahrnAO13zULGMQp0x6RuyPx0qzAddav4kuk-z4rJ5qkXNS_CmoMOwIapRE-wLMY2GYNRAeh-gMP1msyHFNgm0FEMyR9w--q7OSarYUCuogAojam0WgrLwFb2LjMiEeUj2M8JP1c8EUubfCyhVcnmAebRwWIZwOPSFRhxc1vd-Xs1X78_p8hPyj5CRgDHnPQpOFUxsIhNNP0t5uM0HfHWOR64wvhxUGS6mJpaNwEN-iTMSZhmhyVKh_NrjHbDcyJJ32V2I_pKy3fesca4EXMNjFe4cneQYMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jfuvX1fxmKVY5nN-wAKxrNnVUbNQ3JD2zuceWHxew6KNqJG-5vl3dJjX5niGz8VbSN2or2crhS26aXBiM6IyQXXFvJp9Kd8zIhB-w88kDnGFUr2utKe4mHeZrH502E5DWIs9m9cqZXkaPkPH9Rz1GN2nngwoGExXECgp1nD0A1rWXUK3ke-7r1hTV3kiuKaQPZkfAmchckYFCsR5cxDHbHhI204qrOqTVeuUKpNSl_QZOD_FQofUv5WShcBsUHghMBI5EeZAVr6zcZycI6tkPcKLcgTgg35CfEPcwE5Nyt_N0FjVqyyJL1PnMXlPbwLZsCChmNnT5-HF2eC98L_mdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sKPfDBNyrKKhVE9jCAMKVmjnt8fIli6T_HxPieBj2V7IgmSIsxjqacu0ZypeLvlVOwoEIhJ5TH27yh_3ugMf3CwWPBZq80gCkJG75QT8b-6_CGEMIATgfr-UYuTezd63Kd0FL4tc-mE4DRsOO1RgwF8fkQ3bQN50rF4pNQJPZsR4fv5Mv7KP-R6f_hIZugZj34V_M4bq0y89OfVm96Zkq24jbZbkSUSsBtQlyGtr4ZEWnEQUlO6lxXt0QUVyY5vWNFh3wLjaxC39duvs0jAK7wOvgR0FHhlGgIa8AsaCC6aQjn5pPH-HW7O2lZtzzu_Qld3RAvKyLuOEg1-mgnT8HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sRgqMSjN6CfLQn6usdiaIxMqZ48J-_XIUs1PeLCoCuGCIT83ad14_mQdUTUaCS_RvpdibDh79Jz0xxouoiG69onJs5jv4o_LDJRt0qzghbw8KKCrFxXdoWeqKQqqk6PCoD3sY--SeUrsLY6a8a5XeH_czL73Ls5D6urccHcnvanTFUnIhSNDIN1MCMdY5z5Nfp2AsmjfT76QgISorCpUwKuWaOsz3ynCRnU68KdmHtapJCtCH7tVBdYevmsp6zzcvN8NtdE1cAh2L4GXcyRbIyNldSLgUaz-wTwMUCZu4AsoL-Z-mHa-uKldsK1sdl5UxpOFM9tPEIXV6VRyzvDxfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lQkAN86CSMkK3rCqoCnlhdxWMQXc0yrQ0o6PBXbTlvG9Tdj80_p_5AtUXdEsI3IZ9D3miXqZLFyMWDa8Z3_pqIHghDgEaHub0G2GaPACB1CuPrkTFln4NdB6k8F3EsJ8qcCy7b-nwrfXlIPNyxPYKNDKfUhYWXWedq3CR85k4KX_rQMY7HwdEeybmzR6FM0iSalfXPjHu3zMtXF-kopruhygQbTxFFkbpahQEPLiT8AQjAPYah2CM1SC0Yw431tv1pZkwvJfKQ_tKJiMjF3_X9ezbqXBxtaoMmiE2NUZBraNatKjwYUnvZicug4THmvMlg7Wh20XMCMYAMNJTr03Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pYg1Im7RxlNpLBxaYil2zfvSfxAFDuN8aHAtjRXXoN29q7CrPEV6pbmCPHDsT0-fC4g5HpA9xW3wXj4iQTukp9cscLf6MdrI-6RMPvkUoxyOKVEaiQatPSvMqERTZs9klCsHCsCWrF4i5NCJKsGTbqZsdeP2SalxdtScBr2RdRQdhK0-mIkgDj5n-IJy8H31ZQbnvcpJPvMidNcMKMcRR72Ajj16FpiByCpoPgsldlblOUKvZ29VEnKv4e9ZySZ0RgCcjMiAEQNJVqZrLrJrD_TFDDjie_sbV_q3Lv7UDRArjZo4BhRgvTCFxl1xsnkTJdEw61aDs0l6FZXxQLD4VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eghNDoCcatp_oNcI39ktjeHSFyJDwyy01zHOx8CNnI4jq0LmM8bJtOF-jnSiDZqtES5If3pPOvu7q1RJqssj1_sfyWpIvmEjhDfh95ukcfBEDBozvg9OU6zdSCyWG9bLjywJCrCYC8PRUTw1uhECC3DJfyfsIsWm9YQE7oVYqKqoTsZTUrq-GgpW_cNDzhQkCfuMjEFrAQIioNgaHlcP4PsiXK2WrqtcrtShRy--v2td9b3rVtzGwHgYpjSyoXjjQ8QsJ-Z69GEVIinyTzOE7GjCZ63jXgP6hfQkdxAwTd_98ILR0oas_PCTwiLtYGBxbARotkgG02pWxOoFfR8hKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NtWRQe1MDlBQPGCl8Gl6grap1AP0RaSqROGI6_BtGBKaA4a1eWjNAHu9NuGqOQ4ugO2LuJHrBm-bpy7-zIJQgPfKGIGN7XdXh-nyoVkBoBlKDqtSlGw36Ie2AQikaLNWZZPNnDNCuDvKF7tBpthJWA92nCDEL9pjPxIKqlB6yNDyyHOg68rhhycI7CW6qMoCneBTv8DC652L8qGaEX7O_M60PWJHu90pp2wn9m9BqIkFsBzHbbKiKP0mkIGKCurD5D_luFIKJknA7PfwUaDpiXzcA4d1cHr7VdCWKLRIUfY8qni-WFVKRR_fIPxFsRfGHCpEMjvg6C6OuiUNGnr-Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dUcZoIQTa1RcCk1hTz-x2xCy4MXVaM1nOPI3C1q3jVtfqpSS7LMvRkmeuw1Aao7dpK0IRZEDiPuBPlTQC_wI11zxwsPXohj0_tCUt1BzsIwJ7eF8B2UKAIIxkiyeJOyBMyBan2k47gSNYsJwoWn1nyZJ38gRt2BQVUbXF8dkyf9mVjf8_IUMEgu5S0xPRtG4FGom-wCGvA8rTeJ37i5fFPvEkpVrJnjAnyEVAHgZsm8yyRlNclQRZkhqHWRZezvy8BC_q1a8y0X1-DsDPXWNx1Qsl_Z-6OdKTJ_NKUKFbE2nI2CPvTI1KTarcVBlQ8Y5xDFTWZBL9ApcISCbw-OiAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VPJuJxcW-IKQk5s6XPD9Ik1mApFGLp1DmugVIAg8vXNOp0Tv5IlbAmEWqURI4_wgWDo6CcMWDkuA63Ij99ytxTqRlQaxSqvdByIm_LZnB57_boX9gtA6zaYlcHN_swA7fIzptvv7smNRdtysv9SWAwSwmuF0lc_6gFzBEaa5ndPRVy1ip2LUOdwLbY52E6w5ZV_k7GXFN_sh69qk-HUbxXhgILNkz6RxXG96donOqCCG_wgVCPaXXXgWxZ49nRH0ICm7TK2Ge-EHhHW1PmiG81Q6SYMHII8dbcZauS8YxHafEryfhst7ebyN_4f5TGsaQNBq_dTmECjXYMMsI1cqkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mk6UMK9HtDCnV6IN5759WnEFwJLTTrwUADrwzvkRy5mzXrw1kZ5B5ryaC85GO-NuvC_llbod7i05lklFXGHRZpq0mdwXVzScktVh2Jfdqc3oqlKJmiZmDGgZFAVOKa3AtiSK7L6rvYsFMRPmHq545SLtqgecCJ9Vmg-e-A-mPiH1oYYunDFMld3KOn5SOy05k7019tOGEDnCf2J_plUmodpcBPA6GpdzKG8Am8-T8rgmsPOM1X_deEIQdwjBs5FYc0Rs6hlbiHsZT_UiQ9zGZPT_PzDahAOeHc__w-ddObORw9ZL24XBTxv6AL2WcleRM0KLWWF5SZA-LJ2_TlObqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rR5qUyhso6Izk9mWP2luG-mWv4Cw2XrJouO0i_TrGMpgJRW1sTvJUPBHRiy7PfSm-DONcBm7L1jPZUmBz0qyGCwWVcve-7SB4ISmwYz2xU49vT7A1Bp_wDMe1EVYcYdDRSUzYOIRteVtEXEQciu8BEecLraDXVKyre05B3gL5Kw27lw0w4DFtx67zlQH8itBcWYj2-t1dYAnG7B7_pmphUhYjQXM98Xt8wf6_3lWYCCNyu1DdGug7KtY-8HdAmQcf3rQwfkLlcwBAY1yWwFyFbSTBlqAWbyoEeKPRGyBiqXCwWWtQKaqg3TeLJir-FLrF_wpDUFaMbC0prQcXcNlVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bLP4EbxdhEdQQ3NURev2OjU7eZ66bkLtvLe3QBMYCgk5CGC_wwZbgBUvCysdHHoACdANwFdPsI5WXFoHmumFu3DxlmMOz7Lq-M-G-aeb3fSkTU3PYAcMxktE9JTz6bVB9Ux2tbYUq6AG_F92rdiwFbSEh-VbBjLYeGIcbiMdMj_TeaVOVkmhgk4SunHJNpI7iKQyP-BgRt8CrvvEmQUpGSxwBTu_GJlzwcdAciGXSg4-KPl7O9pgHwX6MLdpTkV_P6eBVe87Qk-t8Pd5CjWHrz-ZrHi1eqcdTx8CTmbO7lAvXrbwW1UWsCmEuERP4WywMEW3jim0bDtG3YG8IeNmaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZA8K6MATwmucNSp8NpT-WiLm0gEP5lmEaT6vh4dsryUk9JepEl5d0DsG67nX3AYtg_iYhxaLixRrEKqsHEHcbHLLiP2chvCup_b-HHvmJUmDRhIV5dnoG2XptG3fNjOAi87U8mfqywb_fnrruZRU0yQAEXoAfVyVbMhXyhJ0I-2O3D3mDDq6YuIF1G1rcsPu6xf-x4d0Fl5Ta4BpgodEwBrM3-xr9_zImI7Oyc3lk8gIqEQbxHTLoatfAlhL41kKPdLdeL_S5_jCXsiPkwYLwWoxGlYaxQbqxFSGjt0KtaF9bxAS-LbXigLo287dh4JswXpIVUbgulsj4fFUT-Xjvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fjlAYWpbFd-iEDoEkcogqdWF0toQK2E5yk6p_7qr0Goddg6vxIt08YLPQ6xrnZ1kdbUZlNPmv23X-FVfg9fWWpD719UL1uuzvLep1Gm44xGxT5e-N6pfVfhXb_5i4sTUZfjmIDAfAsfGRGOaGqRW_ixuinfFoSB0Svqdgg9ONQnQ8XbaJLacvsnIcPtVufIp21W6sVC6iMDJTdzQ0ZAsx5XSzE3nmqoQ9S7-guCCkLLNdw_StNnFWg5RXwm895HPyNlvzzXn3viS2WjwrerY0Cn_1kmj9oEyHy_8Q6enQykNxU4wzfqTrlpjegTbrJ_EL7a4V_JWag7CT2YnCPI07A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Acz3SRU55MhTvwFyOoC4imCojpORATZ7WdJldnJCg2aaCzypFCkn9ck16JWIaE2v8P7L356IG3gpzRUlSexKAFi-9ba9Ejrr8QymQrWbJZ6b4P-o_ELhV7MH34O06moatFQEhoU9j3y7RkjhUQqb5xICdbgTz8aaq2d4spp83y6a1Vb6l9806MfJ6wiqHifOCujF4PHnkMwir4KrSXm-6aM8oDeJFFoUG9UpSObNQOZgF9LMiDSGA-Iws540MBcLVusdDyVQfCe6_PP7cssDlifFAHRT7q4iCGpxtPndy-ugWER_EtAF32DWgRBS0I8Yb3MGEpYjVt7lpRMrr3Lwjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lokQ2DIJyaeoZx60nPe9lp_Cdi7fF3aNVRvhANMn0fuHWr_U_JGdsRsKXRxR0vOzdN_MBpFQoQ35_BW2_txdKcII_azNz1R1r9kgcuYi8-je7dvpCUfYERiFyO-_BV8fdvNSvX9uQ2OLLMkVILpXUYxBRsBiQtFBTZYEnYSOTSs3cGg5ebqUrSFoPxwRQDeXks-gigtMtWJm-9GHUoNKEUcWyTuOOyV7I6_pm4QjCrzYzT6BNa388uhWSgET-aA00fkZBpGOV_ikfvQKaxcPQcoct1CN_idqw4Z26XXzpyiEbAZ-m382uHXDLHKFnS5W9O_KpZU6LEZ3v9JwX7vlag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MttFAtrOwvfWn8j6AawsyyL5ieSQ0NUg4mPuge97CXMbXZTmvppg3m8QLkoMrCFSB3SuFMluqJeCnugIQrjl86odytZiEogPbdPHSTuSREbP7OUO-h1Gzu_S9S1msKrTX2fCakmxauuY7MUeUHHOctnJuCrV5AFXzUYBN-KeQEj62pDS2bsaYx_uVmdnQ3Yi5R8FGdIC9Ui2dX0muBnjS2ZqH7czvw4OAkmnicuYY7US_Mpd32-CambxaOqtBmz4_SzUAaV2bggAvQ6JZJimXUaVd8vSU3IRo_E5ALgH-QQm-bFMNLHIOhVR6vscshaa9vkQDzaCDp7gzSk79mBrGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BM6kNV99xpiCv08FuxyCVD0yd6GM8irUgahrUPLxNcqUEAtThIV8ch1pzUCgK6VqjQUTZm1lJW1zhieTOGoROZaGt0TgIGhcCXFExfYDIgQbBO3W8YtltOxxnk9KInzh3OsN3miFXftwyM47j940dtYZc3bQLtd-TFRTAqGX6yugw8psZxwoN8OU0Vq7NMldty9AdcxcscB0dw9pEEY-oNaCWKCMjrdX6UTxrfg-4Qf8lszFgnvb2963woCgmztm2jmTi8cDEmyTQI8vEJp3sZkNLSqlGV-LKUsYfi0ubi0Im-R485wXjKpIVbjM86yU3foHH8AzDxnWtLz5wBZhnQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=rZhOqroNyFeRlrAIgSxpzdjk6oCiV0LclBWJ-I38eyhN9JG6LVNREH2KRYI0J11ObtOSv_GnEe6c4mAH1wK4LRQZ31h3-k7d5A38Ce_mlj8aW8GPnAPOs0ABzN37z95Cu5vttUzDRgb2x_GpApTSr9YCAEKhk_fa5BBPtqcAHslLKatfa62iWM7A14mmtlzJJKnZpSp026DB_-md6pqH7uAR8Ut33-YNL7Yycm3x5GO9zaT6SAaU-6UfSqxd-2fSf5w_iVmVR51lNsqtSPJ9Rks5KkpSXLXzScnNFsHd7L97iDirsyFScWaybWktaDlXuW5Rt2-x0qWoZSsEGLc8fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=rZhOqroNyFeRlrAIgSxpzdjk6oCiV0LclBWJ-I38eyhN9JG6LVNREH2KRYI0J11ObtOSv_GnEe6c4mAH1wK4LRQZ31h3-k7d5A38Ce_mlj8aW8GPnAPOs0ABzN37z95Cu5vttUzDRgb2x_GpApTSr9YCAEKhk_fa5BBPtqcAHslLKatfa62iWM7A14mmtlzJJKnZpSp026DB_-md6pqH7uAR8Ut33-YNL7Yycm3x5GO9zaT6SAaU-6UfSqxd-2fSf5w_iVmVR51lNsqtSPJ9Rks5KkpSXLXzScnNFsHd7L97iDirsyFScWaybWktaDlXuW5Rt2-x0qWoZSsEGLc8fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
