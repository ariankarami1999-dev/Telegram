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
<img src="https://cdn1.telesco.pe/file/uhwZcofF1_ViVohlIQWSLp9M_DFdjJXei0vt8rXiCcmRn6iQo-KXkYntGh2F1yUxFWM0sYHblpSrSeLXRFNe-bT0vRHi-c2JI5fwEp6w0cQQ49uxbVKpU-qXTI4Gxt1QqE3UUaBSv1hH1VSdNPqMjNZZKCd67vg1QUdMU28OJG6wLbxXT1LgUnGK-v22aPl6sbmcJOQhkDBdxTfS-hSX4eW-457rIXCmlvo09CFmDxGsDxrGL6YMs21qRDcNrgZZbmyns9s2xvWTsSqsMy0-ui_o6NCoPPGOSJKaozpwfy6ZNRsaQVVsEzdCkZMThpCiA66Pnw4cKfGen2nZEDe7kA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.4K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 21:27:45</div>
<hr>

<div class="tg-post" id="msg-2397">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس کمیسیون تحول، نوآوری و بهره‌وری اتاق بازرگانی تهران گفت: خسارتی که کسب و کار‌ها و به‌ویژه فعالان حوزه اقتصاد دیجیتال در این مدت متحمل شدند، اصلا قابل جبران نیست. /ایلنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2396">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این اینترنتی که وصل شده داره نمی‌اینترنته ...
©
okhtapoos80
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/ircfspace/2396" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2395">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sqd0Of7t5C-nhlq2K7h-eNE84Jml39-2MqYJ7QoM9gaBSmS6cf5j18fmq-8sfFZb1D9kcstql2Fve8qUO_Y_GWKKcN0bJmOPr9xBTzzZlxP6p91Ind1tSBINim0TgINr0APg016HF0AsQ9cGJ55o-BSw57xPsuttccYMmG1FqiLm8K30K5IAQrUjGtkEinTVH-EI8cMvroeU6HEkjlXJijQsU0Fffct7tDChORKSjhi5Gt8wlW4xIUIVMKcbl3OKLhS--cUsVcsX4wONQXuLPUPuAIwtEgROuF6kfNhiQzw05xT2VOvsat0xAjrasF2Qw64RkcXAeLvBrQGcgBDVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که اینترنت در ایران قطع بود و تیم رسول جلیلی موفق به مسدودسازی Signature وارپ شد، اپ رسمی کلودفلر بروزرسانی جدیدی داد که حتی رابط کاربریشم تغییر کرد. آپدیت جدید این برنامه الان روی بعضی از سرویس‌دهنده‌ها داره کار میکنه، هرچند امیدی نیست که در محدودیت‌های شدید بعدی دووم بیاره.
برنامه‌هایی مثل Oblivion که بر پایه وارپ کار میکنن هم تا زمانی‌که هسته‌های وارپ‌پلاس یا وی‌وارپ بروزرسانی نشن، کار خاصی ازشون برنمیاد.
👉
one.one.one.one
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2395" target="_blank">📅 08:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2394">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بعد از وصل فیلترنت یا همون اختلال‌نت، اکثر VPNهای متن‌باز و رایگان دارن به روند آپدیت‌های منظم خودشون برمیگردن. تجربه قطع کامل اینترنت در ایران احتمالا به ابتکار عمل بعضیاشون کمک کنه، تا بتونن در شرایط سخت بعدی کمک بیشتری انجام بدن. به مرور سعی می‌کنم بروزرسانی‌های جدیدشون رو اطلاع‌رسانی کنم.
👉
t.me/PersianGithubMirror
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2394" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2393">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دسترسی به اپ‌استور و گوگل‌پلی روی خیلی از سرویس‌دهنده‌های اینترنت باز شده. احتمالا خیلی‌هاتون دیگه حتی حوصله وب‌گردی رو نداشته باشین، ولی توصیه می‌کنم وقت بذارین و حتما برنامه‌ها و دیوایس‌هاتون رو بروزرسانی کنین. حتی سایت‌هایی که دارین (از جمله مواردی که با وردپرس بالا اومدن) نیاز به آپدیت‌های فوری دارن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2393" target="_blank">📅 08:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2392">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعد از ۸۸ روز قطعی کامل اینترنت، جمهوری اسلامی اینترنت رو وصل کرد. فقط یه مشکل ریز داره: فیلترینگ انقدر لایه‌لایه و سنگین شده که عملا فیلترنت ۲x پلاس رو باز کردن، نه اینترنت رو، و همین فیلترنت پراختلال رو به اسم بازگشت اینترنت دارن به عنوان دستاورد دولت تبلیغ می‌کنن.
بماند که جمهوری اسلامی میگه اینترنت به وضعیت قبل از دی ماه برگشته، ولی ترافیک شبکه حدود ۴۰-۵۰ درصد کمتر از  قبل از کشتار دی هست.
©
AManafii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2392" target="_blank">📅 08:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2390">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2390" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2389">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bd57xoKf7seIezEhJiiP6pClYqlG1mGbBJKx5iabsMGbwmweo8Cox15I-vWuuuCefrc5RmQd5-Mtn-SL87c8ajYLqm-7cNx9BW4d1AUmGDFmAQ1sLGNaaBc4-ylhp4CioIMFXVq_QpCTaWKoNbC3D_b8oJhFt3Co8nSprm6z7L_vZbC2lFPhMK0RHhux7oyIEDX46REga9-T2KlCyyci5mthizrcSdipdozvX8Xl2e0-ACN6VCwv3bUUDcvw8CNaxYIbLcPbqAg-tKmfxrwtsLdGn63DTq_NYSeHf1oIuA9gFoSXxW5WdQoPnBdhSGGmlvCeRGZpazeAmfTmu-quCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس تایید کرده که میزان دسترسی به اینترنت در ایران افزایش قابل توجهی پیدا کرده و به ۸۶ درصد رسیده؛ هرچند فیلترینگ به قوت خودش باقیه ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2389" target="_blank">📅 21:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2388">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/un97CVqgAe65jrECNbaz-S2qUo_uoU5yphMZ4AKFMnpVHXvaYEbTJ5i-0EhRVX8wm_wnxrGP1VltAQvHFqbpLmtOYFPu8XidXKD7HGoCFnzkXmm_ip7cxu6g28qDltx_xeZ6MXJCHcEpWYEfHAPxlYQMFozhn1fSqtlQWLiBerxEhDD4YsXVjue_-VUq79TgsARpvmqoOELHn0IHoTkzvsy3Vydkrq-9ARfOCMxl2InS9yHaNhCSdXszDIcUQjxkQVLI84AFxgvBCGlFTqZBaYlcLm1WuRpwBet7aOypWVBv0SIh7HEPHIU5_KONBeCR7EIcN66wU8YVSvae2MPk9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/ircfspace/2388" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2387">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hu6z-DJIactCCFf3lNuTRH_gGDneMFot4oZo4uyq4PTJvcTkT9TMvW6b3mWw3PUuGs6VaVaXdViWorP6-x6nZ_fDMLVZK6POs0ajtDAeLQD89GGw73gdwdp5LERLx5hPPw-fIGK5wNdJJVjk3xRQ5VkSvuZkvMrPFxz96aIIGHXJnUFh_IIDSALiB1-oOzKA7KwkM0rW3Azl5YcUJJC818MLw9ixlUPC3_Tm0rtRSRdPowaQIaAJZOPTvrBZmXVQNYJ1vFfHAHrvzBzNRBVIIIPccxYFFh3Vrs8O6-3oX3PUH3oK3v-yDWXEy3rM0Zgqyg5vYq5n7S1wN3xXWLcgSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2387" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2386">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 47K · <a href="https://t.me/ircfspace/2386" target="_blank">📅 17:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2385">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ME57UYjAWx7XJnMX4DAsQVg9PLR1XMpnNepfNspTF2J6USxHC7NbhjQwrlEIVm7e2HrKOx1a5fCBLHvpL_9rXhfqiB3BwMGf5F6bMPoY2kRoVx1l-8j6DTQZhScH8tvCoAYM5SSxJW6xWRKREfvDkreB6tbTQmT1XcKiFJniux1J6d7mQ_p3UAHs-dVMzpv38H0J9u6H50km_7h6yPiwd02-SFCO07m0Tb4PiXGARjanUAmxvss4wX3_m8pCLn8O8KzuqEu3j_Ikx_I5DWhUIf-LSO9lKIjy6VW5O7t4VhzKmaSwKAhA1OxpunYHaYqeH6uQTiYvcCW_0pGwx_zTXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ فردی که در دیوان عدالت اداری نسبت به اتصال اینترنت بین‌الملل دست به شکایت زده‌اند، کامیار ثقفی، رضا تقی‌پور، رسول جلیلی و محمدحسن انتظاری بوده‌اند. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2385" target="_blank">📅 17:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNT8-fPOjkdPsKO0mjf1a0Rbn7mdC4U7oFhWD-VXP0uK70bYV5e4bAARx4owgWJv8k_1ZMwdVKwD9lpKq5dfXJwjPZ3xPiiZVberH_JaGRmG0T0umhuwjLsnZ_-Q2m_TgV1LuMCqh532jeiCKZ65ZuMjj7FYunOF4a9MFI51zVsX4jDBxIQBifIjiYp-nKC0xRPoskXfzcURAp-QlRXmj8Dq1Ih-e2k8udFsg37uoLWOIDBLdjwIoJ_aBSDJ4ehgpZmHTd3sbwxhHXD7EY5bYVRZEhcRnA0QMbcG2CXQtqeZXj8Qq2kTATNROgs-msYLfJif63fbsz744ICltEd4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌های زنده نشان می‌دهند که در روز هشتاد و هشتم از قطع سراسری اینترنت در ایران، اتصال تا حدی درحال بازگشت است. البته هنوز مشخص نیست که این بازگشت اتصال پایدار خواهد ماند، یا خیر.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2384" target="_blank">📅 17:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دیوان عدالت اداری به مصوبه تشکیل ستاد ویژه ساماندهی و راهبری فضای مجازی کشور ایراد گرفته و گفته مصوبات و تصمیماتشون تا زمان رسیدگی به شکایات، قابل ترتیب‌اثر نیست.
فعلا اون نمایشی که پزشکیان و هاشمی واسه وصل فیلترنت اجرا کردن به دیوار خورد و شرایط روی ملانت باقی می‌مونه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2383" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e2UHgZVmknnhq2AGazbfsTJSmdqXNpVuqsg3U7C6zQxCtwrP3b1skcq3fBJuEikIvZj36k1xK611oOh1NrsXLXm6STT3lghzX0cwHOQ9ZGjjB2rbyXD512PiuhnHeYl0pwsbzHyTr7BFTJEwVGCEv6pHr6uPZo_xsLZqb3QxvfwdLx6z6HeHPovbhUyvRp0tX6ISf9IlwHUTC3RFXIFPLSGGpx3QthjtXePNr--GSAGcOB7hax3Fp3FSOYH82GM9MBsL2YpPzmyeQT33pbymLJ58IYpfCJXQWPWdBZJmtMUMfBs37K-gUQCY3FmTwvVadvuHpSPUHtywG7uSnEaYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها نوشتن که مسعود پزشکیان مصوبه بازگشایی اینترنت رو امضا کرده و بعد از ۸۷ روز، بزودی فرایند اتصال مردم به شرایط پیش از کشتار دی‌ماه برمیگرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2382" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X34QB2CWm6XMKSEZiqppI9hpPl_8IGDm03Nus8AswKFC3TFoa9SyWb0qBkY2toePA1uEU6FsbiR6qJ9KuO8RdUIbqRIDjm7e_gY1cr5nPIhlOmuF_EHHHiiTDVocWZkwGKiAUSd9AWlYZm_cLpRVKoIkhlo4MnuNsJS1GD-09ZCUyZTLZ879zkYVyz-XXQ2UyhkYjnpQ5OO3WfD0_JvCqBz_X4zCNZjlqc2fG90DhzPFH6J0rdZ7miqALCnXM7unNcNZe7Q1kHbvWWZ6upR628BPUXUZYJhBPsMYQJpe7piEX0ER3BCEoG15RqUQ2A6vRjCYWZ25XwXBcY-dQxMU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: اکنون هشتاد و هفتمین روز متوالی قطع سراسری اینترنت در ایران است؛ محدودیتی که بیش از ۲۰۶۴ ساعت ادامه داشته. این اقدام هرگونه شفافیت درباره اعدام‌ها را از بین برده و به شرایط غیرانسانی و بلاتکلیفی روزمره‌ای که منتقدان زندانی، مخالفان و حتی گردشگران بازداشت‌شده با آن روبه‌رو هستند، دامن زده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2381" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHCyG2iBSWYegYO5D2IAZUAHotTuIcM-_AHXNmAsD4BLMsyk9Plg-TNcFRhdQsnvdZ0EDEyLCQzd_qOnVaiy5Y5SPWSai5hH-Jwd-XFmkyTHkUGrHRUlBQ_SnFn03GI2Hf5ImnMxrKobCH1gwPh2TXyHPua3zwKdUUqoouq3lZ3tDSl1OxrlAjly3PFnO_s2ATOP-_uSCEfGS35q8O8fSQY5mMd-SsUlX_rwLhY876maFsi6pjehzsvc57oYRRVTkQBLEzmDDRD81HCIuc7oPLVdOeymIcde4SRBI29wWG3MX1tMEh5NfSyDwJzn3LVk3PKl03m9EeemYC-G_EDXYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2380" target="_blank">📅 17:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2378">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2378" target="_blank">📅 08:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2377">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVcyCPQPsBNvGwGbE7al_oa3kZINk4XXcU_UoH2i48eFea0jg6kj-lUeglQRC6_rAp3dyjJaPFFX6P8tx1956I5j8Nuns2te-kpYz0ANUtmqwQKTQa5HMe5kkRsdBvHB-238T-O2wMaZus2mS2AQ5By7eYA0vzY4Zw5zLYG2mZwYLsHnALAmSnZaCAM7poer-5v9JeAaTTC5Jy0doUYYz5v88PLieNjdcoFldm6MmfEQVjOOY66n5XIa6RLsenEPjrHdq4LnUvt_XjOWDItK-Lp4bxg34RTB66ESnqyz61tXMPiAv9excwcEd4R5rjIgVlJ1tNNHi7RdszrS6l-WJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز ۸۶م رسیده و همزمان توجه رسانه‌های جریان اصلی به این موضوع داره کمتر میشه. انگار دنیا معمولاً به رنج و فاجعه‌های طولانی عادت می‌کنه؛ مخصوصاً وقتی قربانی‌ها صدایی برای دیده شدن نداشته باشن.
Iran’s nationwide internet shutdown has now reached its 86th day, while mainstream media attention to the issue continues to fade. It seems the world gradually gets used to prolonged suffering and ongoing disasters — especially when the victims have no voice powerful enough to keep themselves visible.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2377" target="_blank">📅 08:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2376">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=F31vZtRjzfzl3YBERKC2m-0AXkaxlN2Nmy32m-liKf_C4MfoEOhszgtq-3jlq_W_H3V54KiW-Vz4BgmQ1-_I0GyPE6rpLfybrIdQ2A3cTu1t0rYY0nYrKInOOSqGVLS1ldHrf3TD9YitjjtraBLSLc5NH8KqiSnQxPRXZc128MbYCG_xrf7m_rvV4KwUMPGbUgE5L3txl5k61xg_VWegIfPI7kNx0GUHc49Goy_zOLUcgS_kqTqXSqC8mxn8eAxATFcMJ8B5KnO8rA8dOW2r0QK-3BtlRbqdLSde8SPRCexyfYM31UIAEojNeLSP9bHZwA29SQfyY2pOa50aJloWcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a874f4f669.mp4?token=F31vZtRjzfzl3YBERKC2m-0AXkaxlN2Nmy32m-liKf_C4MfoEOhszgtq-3jlq_W_H3V54KiW-Vz4BgmQ1-_I0GyPE6rpLfybrIdQ2A3cTu1t0rYY0nYrKInOOSqGVLS1ldHrf3TD9YitjjtraBLSLc5NH8KqiSnQxPRXZc128MbYCG_xrf7m_rvV4KwUMPGbUgE5L3txl5k61xg_VWegIfPI7kNx0GUHc49Goy_zOLUcgS_kqTqXSqC8mxn8eAxATFcMJ8B5KnO8rA8dOW2r0QK-3BtlRbqdLSde8SPRCexyfYM31UIAEojNeLSP9bHZwA29SQfyY2pOa50aJloWcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2376" target="_blank">📅 08:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2375">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2375" target="_blank">📅 08:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gY8w1mVp49c5_iGtIUMJAAlIdxms8N6pNX5mFgHYAXxa_kW3V7Zj0zCCHdx5mbj1bHYgLVFc-Gx1KsHRdGZQCmY83Hq5djZB621WFnmTfcfxOYzSNnOrWSVdvVjqwfMtjOkHZXPapFJPSKxCEQRujtDsm4lthXJNQUheflMWUK3a1BAdbKkJmFWwN9YmxufAskD1x1T4sjK1mK_OWkeTJI5rbxnwwqrNEuCxBrgka2ejVivUv1XYFy3WGoqUZmonGWpCghSxF7SmC96Ukk9fEGGgSVQ2I2EHMT-5TVu1h9BMCfneOytU5bnSdAvTsfsFy9CjLfvi0UZBTF6VS6w0Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2374" target="_blank">📅 08:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hKI1dRYfwEBydGILSbwxZkz_lUrObJJMvWcu3GAQ80AyilskC6_TuT06RY9BQQtnTIgp4DHo6Meg5CG4HFfWR5B6bvUYBUHz2oqsquvBX2uM5LwYMDvpX14V9ybrSQVasY-7stbXZ6x3IOn8OxE0la7jP2MzIStZ4q4QwOaykWIQ91oVhYaym-t1GMME-8njFxVLAwIJ6AoTB_3Ootl4uZKIdNwyUcWo0V50962JdoLO3j8maSkZZDYoyHbUc_7FRc4bjhscBXlrR7y94omA4vSBBjUAE38IHnWke3juGShoilmvhhvjKHziW-PUc8QNfIPV_2vrJW_i2nPY-qz0fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2373" target="_blank">📅 08:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Not-HzoRWW4jSOFPyF3BgpUgveMMUg8rp6s9nPZj-dRzUAMatV7xHnF5_xw0EhbRLDO-dDRal0rNhz1KYiO2KNMDDN49bT-CAhOwL7-JiZ-kJZS0Je8Tr3sLLZmI50rACuvcpwtCHN8wcYMd_NrBELJiBCEpIGQlF7pZcU22zlB6v7CnKoxqlYDv4gD1TV1wppKgHo3Jt6lqK2gD7NxsThdHfqD8k74iGvW5dOQWpxo0kgdpJOerllm7H1D-qGNgQAUHmOuzuB_wHiP2H-gVs60qDokd6zWuS1qFMR0iZWzhLqHDJd_PFRBZjJoSz3Uzq9sEBszi2u5MQMEy37wxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ksnY6ePWiRukI5vHMHYrq0X8qsZAu-fTX9iYnqbEsLzgReK3mNPMsNCKYenpmB6vnbtkIZAufmcDNT2OPysAQlmInM_dwyG2q7szmpb3OSpNQjnuHVk6b-Nf1JYpcYfa_wjkUnQ6W4MLKuWsAWvkW8mBFeKoQ1umQLvCAnf7jW-ROqBHNDKwJbyRAlMmuPTRO_AZuMK9twxC8EIJviYQ4adj_1ETLKLeroXtVqNSU5CuEjfn6Gy0m0ZZVD4Gg0WRyzNBFTWYrGIsq_egHSRYfJKArAsrKZhR0JX9s4bbhxz6dWPT3OHuewclHEkMauLor4r8HM2b-w2zHKdX1TZK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V7OodAJAo6Lr0QNtjbhbEGz9u6myH5oKN1ieiXzCfEm7F9mHHXIGTyzBbDrCkX5w-2EIBnjw6zd1enBLbSa7WzPADjUEyVAf1flPxedTeGa4TZyzp-0XV9rTMGItfybNyA5MWEcXcufVyjG01T6PptD0GWsFOLAwES7XsYylfz7bPa2AVmQIcR3VsHGQMrJV37rOWrXhM0KH7eRJYqIe_TAIRSu1Wnu8N8ifHvBbzbvLfYDIlVoZ4NxtvEwoGeA5d6ms7THtNzpnirZRVKJ3IL3d7OtN5HB-Jt2aG4LHyuFZrU-U-_mLSry-Bz6u4okHkPZ6vvwjUvHK9siBX2zQxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SA7ZYphLbDLAodeUWwW5YPMqqnTIv2Q0klXYbb-CkwXUmpNMtbZPhgAQJLUrPUp-OsXVpSljzK0_NuXyV2C5w3_PTiuwpibtJ8ymhKcIe3Kx_PWhV_NiBaYARhEdaXI4ht94Cfht60eL67K69CVhPor36bPg2YY4nPGqav9T-w_KHEgT8nT7j_-Hm9zrFrZ3rOhq7YT9OUXm-_xxrCOXGPGt42ZL66aZ6ouu_KPy8Uc-kTNXuIoeXQcnMcdAfolzmpJVISHFRy5wd8ZzaTEJpLxTkldS5WBi-euhaK0SjrEXP7WpMP1d-XAa0U_3mLsce3Fm9pMjzaD1qGV4q2IN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i9erDV74zIWxCzHBYc4qqiO0IzJPZnj95YklRbwG-94crCXt6NCXZYkr9foc3whyal1Mea9ShcVTes_iTidtCLX6nMAWE8e4SMrsmHTmnAlyafMyh0wCBCEcDOjso_5nr8pAZlWogo8Wv5LFuvAHyH-Bpg3HQm0D0rCjAG4FxEaLmSTCpg3_nZw2CVW8cxS1FRPnBZlznYEwN_BFS40YRbn78q7BMKFL8afFe2lPsMXX2GLVzeRWvnW1lnTHs_FUD6-OmmbLuqfp4BkMtoiHZzcUIkOnTGvGGK5w7C3pxEZ7VZ08WjtY72zcMjh11HYC--MxQLJAdJZwnWSTv_Q-pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMr5tVBgcnI-xGT0tcZqroxi5TIvnuiP4LH6xaqXOEWy8TJfBvqbgFhhe_X3fLjCdDHAUyV6qlcjh4JdGmFnOp43JCYTmphklbRH93KZGzqBO1fghfMLgca_usVWuEu3MbAM25YrL9xaEPWltx7wkYnHTXTpnhMvesFFTIrVbQf8Bp2_gO2u76a1M_bCDz82-onKtCz9WWxpmbPJIJL7IAJI1JQYfK2R5J0RuD4mt3o6knUHN5yhSYYvz1ia1Owfjb890a4cR1FsPb_x8kgEof2u8PCDN88Za1s3vofsdjfIT19_bWF33O4DdW5vvjOLWYImUlHIHJ8gZx8vOVnrbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2Gad7mSJr7NlHBHXSUYbQ4P5XJbkG-L9f9uaAGAkgZaT483gV4Z8B8wM4DGM-NpG0sGmk-prvYt3P79zypOD0bjjoEsxCfxSMW-nFle7ZhB7O3Ben6UBBEGI-gseXv0T7ftWW8Uc3QOOWSsA076XqDi_cfEUXMa-DIcyrvVgsiuU3MBj0pKmJVEVfgzVXHweRfpZXIPvajFu_q7_g-uXnL2FEbE0qEgEBc7_YHiCkL1c4NYyFUHbNWPlvVlZwG_OP4rT36T-jnkIb3oWXlteI7y1hZC8IC5TSoGy_sk6MCJoygPjKRWv9Py24xXNEuLnKDR_8yCJSKP_l91sJaciw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RW_r8H0risPZf3bsTzMarYhJRYaFHgBBx6YIPz1DeKGrKmNc_Tbf1pJGO6vA9wm8Vn4EEW0c1IVeX4XYvtkP8j1QcUh7JFHB86X05fkQzkv0ZWOGEXcgoI92sHso8x0bMyKkur7YfDguQ3kr9cHrXc5X-DLEGbdxroXuWntBOf2aCriFzXU0B717WCRGGkZ0wExZC2a6x1Q7TRkXvv5dwzL8V_JUJIEX1_lBZAUa2kwkS5KBVMGfjgt0ztByGMGhgVd2y_--cYErSYYnxS52HdbNkrAXcrbqmXnyfPTETn_seA4vNQGHkr6k00QF08Uf2ZwQS3aOLJNnYR_bXTuBqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X_jbb_Ls7I5_G5GgbUI4yas8cx5kG3glgA7CFBAfngVQ6y2KuWmBXruwPUXBi2kbDhsYEt61sMedT2oDLGgDZ2YxuEp4pfEEgi6wUgqHkoyhbCXCFt8K73ZLE6q_WzFq8OjKkkZCwtlitb6IBJLb9mSNhAkBNiSi8kbC2M3evXMlYKnkmzi1wwplwG7Bc4byk03kt-l93gHQoXhLpmq6-_DvgPWT-Fu7J7XHjIi-IfStHBuonVAxCdluqrm1_Ju2-eiG_fQOSLtN6f9fRw8defdnwSJi_pKv3eivDj_OGfSKbZHVOyidx0-L7-tk9PnQMQKoxM0lEm9ffpgfDDYaSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nyaJEVtwx2AjAg7D3mWCnlGXD21je5jD5QSyRjyN20SFsjO_chlPYyMGWdVZHOaep084BGCQTHeuA3HDbduxj4n2SkwCwW2jvA9PMDZY2ymWjKps1jY9RojtnpTdZm1XQnPTURg6353ZQxLRh88cqJnPODxnOwv_kASqDMCT3DP1FvYxvcJG7bXCDJRrrp5xVpLQP1YigEvxfAaWAv6dVou8UNf9qfb9LQwWzXtJbEJpPq2Y6-zDnyXJu_q5ubnau5RtJMO97g9_Wt74UveJCoWlWWbNyayAfcajsdcIQ7TskockuQ4xEGRQ-0ZLD1aobjWEjEurnus1M0CBFp9WDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGvkGfsylSYpRfBid82NB_4PSbyJquayFpZIM3T5c8Yse2yKC4izkwgzFrFZ6vfoLcgvZyjdrSv9Xnfrdn59do-bXFXCox285F0ecYImzK9pDGLC0bDzac3BNDvrjF_vpzEpD4H1m4ZaItQLPlW-u9T7od13PY86Y1YlOMCalwc-XqUXMH3Z86fXc7jpiYqKnJKnGbwzDJYfPmtFIl7J6saaNMzhJPqvisNAMqy2Xyug3hJ0YXzIwLbbQ6wQdtHGZZ7uWnTtVzT2H-C49NlxRVLGDHvmZVXxturDS_MgkCIODeQqCaAqn_1_ljNGBfk3HZ5AMEhdFRdan5W4vaBkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbZPDqe8P8sjJVIiuSbEcEjGpvjLmDz90tYZmoC1-Wh99WNeNiOLItGHXrKOtddFSI7oFaQ7hM5nolsj6UkyI_0DBLK8T5lfulpCP5TPcgJ44xFu22-o17JyFeVzs6-DzhfK12PNG0-h4Oy4vvKIZ3Si9lNBu-y4ZifLTgUxbWQejWEhp-_HwEWUTD8_vmyoY1A1yIRaBXML2RBw_vr3XvepF8jTnwBUVyK6MkMD6JCIDMo9bJLD1bTaXjFs3kaPVoGVwQjAYFSnosspCeHRHeO1KSd_w6unrliff3da5FaTimbnw4hdZWwEBHO-KKw76pT5n1zCktUAB5GU8y8MPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIhUC8dNhM18GtvSqXjktBMhKMkPZM5Lt1Jbs1B_TqT2pINXykesSIJVAvZxze0izBENBAme2P1zxhm9LbSQWk0Lhq1F1PwzbhOD12nfxMv9TAUjKZXj74bJvvbOmsG8HLqqeRhGdzSuRvLumH0ibmmy4a-gSHjst4StjYeuuqDlLM25C1gTp6Kb8ZJS_T9hbqZzA1NMlg6U94dbQTCkSfVQcSBaMvnuV0oE0Tpk7jDXFSSuGgAY2xmSF3Pvl2cVTTVdoXuuuzyGRBJXqdj2TkLcTV5nSQmH6a7toHUGFkY5t0Ph-yDOuBn9VIx1vO-8YtOGfD1ajO_pTCjsF3rf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y-dIHR-Acq7WIn6GNwK05XlCYxTgl-KbH825HxQFqgd1JMwpiz9QX4b6piU7nzxn3cys2WvohApKMKH-064bfg55AEh5EVcihkcpgcCKRNH9LfRgCNYgOCCu2p_9FyBq_1l074_UzI48WLRRceF_TXlWQR6gnWzxzXfkUVQqRSTkiyKYGIycgudNo5xFp0Ud4yrBzIMbP7Q1zBLQr-4GnbwjT9APyi2ZQk-AGtbwJjU_n_J8gatTSM96UnsFPUMH0eNPvTiQVLlhdR5w8V8GFLFgHZYz3RZ5WdSkNtoQFNqD0epwodMFmmEb43ZFKzz63VDLKLquZe5ao_mbYa37lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDJFtD2YJ8QOlTqJ2Wv0mBTMxAdz9CjsXCQow_drjaBTKeNms_3xuIR3E_fhZqTjinNidO6SL5OouXuCqmMesj7_7kF5ndaWA0eOqoB3zxInUNXZzut1RkdUC-8NOXH97JJXaQGaKy1qYli1xpgDmoftRQu1u_EhgbQhqIK9RgxI1sUdIJ_V_PI-zrH-K-hTfX75qJZuDAgZDQHFbvFrXs52rnkDtZt1nA3VK1xNaarQia0k2poNagLHIEWln7dAS8nvVevuD4HOLPV-09CCBcsd9IDHJ0tWxLTeFx6zlthPgGENefs6W4VMdfWZlxz5-ngxjPN8JsNwwYzxaqsG3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bajtY2Aw-dmENVKdZIORkEOfJqujokpECmZELe1NfxklPo2N5LEM95aWgaIx0L3O1y-I4nIcb4mXWo62xczIr3vKPgrMzetw9rpOJsRbeUk2Q0pUOhKrbRykH2T9odL-2lxSyJ9Pw2-o1Sb7ZtRkwwJ7pPyICiUF6JPhfdTT8OqBQK8tBb52_soc_kjkIKDFelFFaWd3LgcfiYnJ4rtLO-Bplt8brHrS8Z6GoFkJ3E1mPp8UmjLCglLta93UgNy6OpRyjSb9ECXWD7-UOjJrFcYO1HJtDhLprMr27Lu50n-CHOu_iAxzzhDIFoVsK60EH7HG9mguVfKaBS5yMKmeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MCFYkbMGCZoN2Xv7ZQz8aIKD0BKgu1e0KarhTRGgKjowF-qZPpFsjIz04v29eWhYXM6mYHygucBA0NS6-3PwiPcQYY_IxIccgFBDB3qqYqHNflT8sJpJ4awbTS5PkVhbOo6TXuI-S9yvp3SIQPiRdVL4VxbFtYfONNhfgDe7hcjamw5xGzXULiHfJ4RCsVeXk4BDR9OIt4U3hnUG1KQpS9K08_sPlin0AW_QqkSAWVxfhRFqEVsKNwIwT_RoX690a1n-FE1wtbF4IN0xZx4ZDpYkw96JsIwklxukpi3cA49UYp4gweYNh2NOm8WL6Hbj44Z27JA5r5791Hu6rcgXfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f13FNKJUrW6vnShycT8BD87Rs0hgc5uW3V-shPWxomLPptpq0ixsxECGYQ7Bxoc6-Dtr3yWI8D_yi5yZnlj_qR0g0zeMmMvi89m_v7KT4tra3MGiWb_g-ze0dG3CVWWFB67SEBALPO-WWcjSc5wVK0GwJoQjk_O7Sxc4VTGOt2YjgBIRwfQif0cN47j8EqL_lox30z9rQvQJivBAEBmZjTkhJVDtKgrw2AwrVAvzltiUEfpGGjyjuqU73cubM2qvSQfzgfdH2iOYoqR2MhDc2r3yxKbyJoIhZn3mSeftblaJ1p3OyUaBQCDh_3QSCQZQjUegbdECIb96XnVEydrCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EDZo8lUcimnq8uYISSn3pg0HMBTJN4LhHRPwDYnvwtX8oUaVIUEznDYZnP0yv85o9ek1y9KnUWPeEJ8TMIIqCGHpEO6VVSWYVAagj6VO7sA3fhXH0R35_GKxZFCfLrHp4Oqh7r4ITIp76tOwMMrO53XSPT3AZ7XPicoWQVThMZ8Kj0w98KMuyHXZDe9Al5YGFzklGQiJz131Zl6HIrZ-DCvmB4NKYr47rHhaI5BQ_dovyAkqRbMexxHTHB1T2-Bmtyr4Ug5js-ra1Ixo4Hug5ibzT3Ladjeq4RpDimZmdR2jh3q9qRwULdtUaBDdGJfkKyzNtSTUKxK10Pw6eVzkfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G-mLrn8QpvGHIvmljOsLBUGN-15tw1-1bcAYL7Hd6nLU93Hn6xU8fooH6PlT9YMZI3Bp_ppgpRhLeg-empYRIelQ3I7Ohdm3QKw1NJQVe9vOuhjnxZxIGtSOZVzISERI2CO15oJ4BLkIOkPqBwIjtn2KO-oET7RH4fwCevMDFEOfL5HMmCvrI46j4hTDfJyad3Rw3TbCwCSpX3d5JFtAHWJ86I-lIyxWShEDLiRiZ37m0Ypo8hCBnVG4Mk5b-96olUHL8ms004zifWmIF0Jc8iOdIlnpvbQnklyHqcvETeXE_mcjYKFfii1P4rBdwlG_u5m2-HmTmgNI0xSTzrLnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NWMXMD82IlEM_xjc6kNaCrw0bcckxnZlLUcXgJdm1ftT2jKdA7AxBu1ctcEZaeQbgWDXBSvcbQb7RcJawKtvWqV6OmW2Rd7FdmeYwhUyZ3R2KSq6wAcgC5TOcNhitPiD_JSKfhLy8qWv4-rl_Uo1iZYyNiRp1n5wx9YhlsFYjFNrNN5IUH9lrd72p3Up_Zs9NJ3jNOWkmweubTI83GgFRMzO_oBivUvJ62-9zFJ8L2RsF3Zx5AeDD_zZAu1pftCu_qb4MenfEGdJiWprfXQbxF0A4t4HItCEziHQ8-qoHFydJiduhBG_Df1o9xS84ONifo6QfqmJ9jNmnc-YmBIYkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g08v8PT2P4sMLPKMPAwKzMFi8vEbms_cAC5Uiwna9usBnn-qn0qyepQS9iy8m_3CJc4y32K0BzNNenKv3cF1htcT4zRQJCz5DIiSeo1mFpyHFfP3_vFuxR7hfHqGWBjPONmLzAz_JfFmm3x30GKmT2FOXckJkPNGDeD9NEvWrsWlJiJFATTsugycza_AuWPjUtX8jtIASkc5pBnplP4VPYa8Ew1IPR5ub1khc_Fu8EyIkcRyNKV_-jKmythNM9IG-2KGEnpL9yZdKNvkSzEBpCsstdpu_eAGkZAlMR25WR_kJvHP1mIQoZ_YPDzfWlGmP4zN80otwdciWpMsD7cyTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0tviJF0CXak34LpDsyQ0z9WFAHjZv6dLLtWAzIIppMfD441Sjx_vHdINvhZqZWtS__gXkG8h1caMlz5kiWras0at-9ag7_RyHy7C9FhazLRYDbldBU0MIbKD-bZ2sZ0SdfLV6JGEeH2b-zjx2DUM_PUUPxrGFxIBR2zzAJNkzZW1Dma1aHi4_RBs35qGVIW-7mGfEKtWOITSb9y6Q2PodPIH-MJibN-S05ymim-GiwWGeVCt1jI0mqFKw74xyE1r11aLavQEfxKPPyLbMNS5FPC59Cu60NN0TjVBa8d27JpdfwHQM38kZZaPiBLmSI7R3nH-dFZDuYvQvecOcBzeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vsRIwMBiUKwL1-UB_g6fu2KCuZn1RXkzaiqbgAP4xRIXgVhQxHW8TDijzC9VHazzNwU13euuImOWjBBhRh8FCMDNp11DWJBHPiH5bweieJ9rn0GUEwVJVeGMSpD_vOnmoUoIzKiyHtbiofYNdF7RzlgRhhsm1b3gWnzzLHsGQ2eCtkG8C_a0J1eIaTxBpQ46fTD-cNZjG3316HRRHsHmfDiEYLthecvCY7N7Uk3ab5dvbcnZd2AGT9kVvo6OhZvDanCwpvd2GtweqZtbmWl74LG2n1Yo20i-QYhqKeZ3UjlXGKsHBxPi8zr7J1n0bqLQ8cZ2r4siPpB2qDwe9lLW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9-EpJKr384ff_eAL8RIXI6Aia_C18sawZYxt1kUCqXJ2QmP9kzVQ92Aonma7cQpTayGy4_mDLm1ME-IGD66l9pCfuRA-dhoCYp1gCAoUthScPMNWCc3C5U0xnOGIyunwDeuY3XyeKj4KToEwsWEsUu_qmJUOB1RikdXVL-q_OMMY3iFYnPEHoEjUfYHIhn2mCWBodbgwLLfTXWpATQkMdZBD0ZSDgV63A53ejs1PKvTPspzVPg48HTvb3guNKemPGjI9gHiXXJUhVs-sfa1QcTqU-c85yuJ8vsuuHvRoqa4lKlJSlSq39foXDD93umtpvtWHJxvL-fRtB6rcbbu1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F2-4zqZ29sTJzi5vc6Z2LW6wKYp_rlJwd23DDQNKp9emRm3L9W3hU2QPtl7r5bOQE_TD74boykGfVkB6Mp5aGgB5efCdhpt3u3ZYoecEzIvvkkj5owYz85TiRaj78e6QvWeNEpN4dpABONzLRBGfFIRatWDg0d_Ocpk9p4cLdFT4wp4oVzOA-ZLNeVBuEYDye0wpLFBZ8XUxMWkWJnsDDlhzvLJSrgyjur8sKz_0EOJw-rlI_BB48TOznZgNEfTaT54vrUR0M6kZzBDw4VX5FtWGxP2zeHBtuslNngvAmsNgnKDk20KivAQ1mP_dsK8UAEKl5ajHhjAUd-nLaKr1Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=NZgJacO7gLwX8FxEV-kiVVMX0WdIJq2T6fWQB2b56jaoQmX9TsaCQnVmM_BTHH-uQu588yDsKecgQVlU2mgysL0_V2L4gw82BK2wZ4cInMyEbYSO04GhdVOGcS6l38L9Fm4r4VR-hOicZPZovYOasgc38BUdaP5TUgYqPo7unrfjN0wxXeU2hQ0OyRPSS7t4VhjoUHx4yJfiWQM7so-9NL5FLMO-Rh0IED6HvmemuvAsdz72tHDRpW6Jc8XDnZS4EuOQx46UF3yHj0a023PbHPYlQLz0Ttp7IX7w6WJEFd5bAh2zT786eFzZva6Ec_z1EhEkqQWngGQ90bmApYmXGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=NZgJacO7gLwX8FxEV-kiVVMX0WdIJq2T6fWQB2b56jaoQmX9TsaCQnVmM_BTHH-uQu588yDsKecgQVlU2mgysL0_V2L4gw82BK2wZ4cInMyEbYSO04GhdVOGcS6l38L9Fm4r4VR-hOicZPZovYOasgc38BUdaP5TUgYqPo7unrfjN0wxXeU2hQ0OyRPSS7t4VhjoUHx4yJfiWQM7so-9NL5FLMO-Rh0IED6HvmemuvAsdz72tHDRpW6Jc8XDnZS4EuOQx46UF3yHj0a023PbHPYlQLz0Ttp7IX7w6WJEFd5bAh2zT786eFzZva6Ec_z1EhEkqQWngGQ90bmApYmXGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/syajzLdntQQAM_CX8BmHNLWlddSqzfv3Ncoi96w2Yi2Tc1NBuTCCNuaqh7g80HW9ZRhpxCjddno73MoH9Xdk2fhhDaX0VUS5pksI4Ffc48shSrBT7_Am0IGnIJsxEJQ3JTnMDdEbhjlZ2liacZM3VF5em2cbdwwRpAnuW4DeTXe0VXGBqiNAaqcDGoFW8pQl4_OI5gAW_LEb8tvrk8DAlTPd4fj_w4MoZW3_AuU8mHU5SJ2UvUXAeFgrlgmDEPs3gK0qKAKgCBmK5Id9Jn0f-CThA4VI_whXHg7C_Dqha6QI2FWySQWKblTJI-RDQdDzAp-GnSN4oMwwKlggc16x2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mcFFW4V10o-uF03lbJBS6cy7aTyKuEp82WMRZUpHEGBRTsCRhJzhOnwjs_c0GFjWqnKMVL01rfFW36bxjURHFac2vbjwUvV9uGk9uxvz5Sl1k3NH_X_h8bwQ4MR7N4eiy4EfcurIcJSw9e3VIhxlNygatwTZsB0-DcUSK-UXCo8hPJy651bEqVXGflFTjOpNYdNqV1C30Jklfikovt3Ci4zkEDxkkN_vBgLCU-fOa_9ETVz3Fo5FdpSTyYzT4sLuj2V0G5trDx5gpe1npK6Stu8htm64GMqey_0joWBZEny83MRkxeBvT79Vso96YCs5Y1JyLiyhuKfPzLUkzzeYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bN5NTnaN4_kYhpKu4JpOUzt1q6ymHov9oelpzl03nu8qGCaMYhGbsOWNYmDI5DFOABBtP5lpWm6087Beg7BtBmpeOlOA_zTzKs35Nt_fIXcqOngRwPoaRNUg_qBTbbeyxNWnrVmTzWIzMQLEWwRsQdg5qPWlUiE-3BemSjPyKGjYONWW7AQJ-mPw_DOCH9qMtxxNCh-snYADhifjxVq05CmQrdrfEjxnbJVYxf8UmHFo_50NDuHz_7aKYbdS_X3O3SVUydclTJANALwEpjtANlYcUnJOVz5vV2XcyfoRyJ1u6dYIWTibQ7kkcVcmNDziVp7XXeK4mHXzx0bQYzgigA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L13tjLzhhdo1Kdb4GRd63Ha2rAxeSyHdjIERFYEO_fqexsTOTlOOcVxte-LgPy7AHVR23W28OlZj2tb6hYAc7MfH3PTKTIfiCxA9NV2hxg_wFFJqRtcfINPQ6SQXsa7ALHYWHUKFCoQeK-cXMiIT2IC-vhThHsU-SwQdJv-RxydHd1nbRFjvijhgFD4l8abEuNo-OTLJHJsQ-mvU1soRtMIYnLy7j6nq4Y5ETwR8hs4FXNUER5z9hwH0_eNkDpMWCHCmWyS_ghkGWLWC69bjZnetBH20e0Y0DekGhFU8N3CZ4xrj_hB6lRHTfZyOkk1sAdI_qIMtJTzsE_n1EHKpfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZZAXyBMiH7si0DZ5XJYmJ8SiVoFFncxJaEtgD7RE3dnf-wUleuXgwCU1OC6vzLHneRj-fvYQRHUMRWOTeYqpSIlXmzdc4gnoPiPfeLa4se8gVf-ilX3Fb5UTdieZ26XxFDQws4DQQGzksyo0boPYTMu1PN16-5vMENdd5hgrg2DLzK9smRMql4fTxiHfE2lIwEbOdLFrT13J9bjAFpPfsaxda6RODSmWJVlxgx9tULi1VvY5yXbiBUWhBxuPIon4eulgQb3yEtQbzWbNKUIo_G6SWcjBYFoc0NHXr-8-VUw-n0h8kDekn6T301t_WYl3_QokqN_Y7SeYTfesyNfiPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DE_D6awLPQDR5UQw4mfkqS0zvRg_P5hhCscLdGj-xauUIWr-kNKUnbDZmXBeRIOCkJFDjI8Lt1YW3JyUukuS4xqDip-6A-CZH7faCFDYuWWK8TQNwng0DMfp6GhOFzs-ZyFP4VX1RtDovfU_dwGT7Nl5XTba1aEGo4Jpg8K6tzTOcjF5FjNErfCISKb_sN0tnUp8yGkQB9ZenTeegdy8HKRKENUp9vL7vcB28-pZ83t8vIekTh9FD8cRnS7r20P2NEoflLmdudNQbu6oHI5h7zResFfDl-xAkUVdlXqzfvJGFZVHyV_UqUJDzgVPd2XgDV3P6isXGmqz-pjCjRdLnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HaCI5U7nUyUShADPasLm33qSdbShEtU3Pmnv8K64J2kI9or1GNgEPqW21EUnDwGrsDTTR6XyHTyK4-RDsFxqDNTzf4X5tUgu-2isLIVmTzhHlMlaUHhuJZkJYABhVGnhxEqqbML1ZI3JOElJcLGTwZGWQr_M_GJ5uYYfQp4RngtnUiR6SBtYSheb1iHN-ymAE0VIDCcbgnI1fEdD53SDRed5odoCDJ01jk1lnAiVc6yZZBG5xIGCbsoUAb7of6VhFe9lgAtEFBmoi9dx5Q_F-hYdj-mjTuKbYKozYoKu12xW9kxO5we1smEnzC2t_w2vM5zQI5VXM_n8Yh6wQEOF1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/duLq5khQ9LPmAyhN6YxAh_SrrIp3m7EYixE1SkSTN0br5WY92d3TQd7l6mOirqltX86uafeQyGFAZb2IN61EpVe9DSQ-X8EjHnk3D4ELZoc85uOJMeC_nX5k_dvPNS-QTVu08-7DEDI0ou9E1ql28tOcXwpoObsQZDRY7fH5CeLCCtCFJAvgYATVALu-OliU2hIDz11x8U8rDYKzGCCho8Hbg4-Sqf3oQYWa_7Ojyczt7pDUkeWoi8zYFKxR6auS1-62TTKabq5cLrAdlz_XRCSkmf_saZ7K9ktsuSogR6I6O9HFrBYKb2rRxjtwr1q8WlLIZbEZtwS2-NPXn-FiMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KjGC6V2rwLm1Br_5pMU1Fx3dvgwOm8PAGksMWbR1TXtHpFKGC2F0zHaWr9sepVBOrdXQF6J1Y3wZBonSlLJoTa1Nb203m9z-yB-cmsv_2dV0a1-3lwgYHy9d2ys6sbv-H0YC-lGVGygLF964hGTKOktFwUp6nMHTmWu6Z3-Kncu6z3ehlq0Iz5NGcerp3VO5wZLGBEAopFdUNiVxG8JAxsFFr4p3HezM0pSg4gNdjcEhBTqoOerEahVJWSkhXI8C1xTabDP2hddjLh239Y6jLYa9daZ4434MUvy7RYyRyBGC_gOLW5Q16DdgSm_6Lr06cyDQ7NMDWlt8a88KVXVtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Io7L2XJPvK95WqQK77S2sh4AgZFL3ga5cLYcv1JMmYLgUo_Ivi8hjykd5nq6HYCdQWDoO_DsQMtleOOwvn94xDs2ulRoYXk9yBT8pkv4XaKCYI4RHd6oZoowTK5fUDy3v7TdN1STyo75UUH3eZFG_pKrOonZI_NYx-GopHd0QIymBFgpAf4K6CWc1w3uQM6DK2qyfKeVimUk9DEe6_3QWt9Vun8WDktiXtkY_n8iFhWy-SLlr-vnh5aioCBD6_FTj-7d1P77ukfZs4B1_WVh45-CECDxjkOy-ej5TQU_L2o_zJxvz3toWaITv_dSfih2TrYr-njV3KomQEILEl_RkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aaxn50khGMt3Acxh3hqK7gNN2fXodopFK-itlB6eeD4WnWQFbaGNbwG2jGrO139R3U2QqT4np3cktLiZxFEae8U6UfAlkfUC-h4Z_Geu2F_PQYLjA-NeBk29hug8kII9waDTo-rFQyo_6dsuRl4N5NmnyQqE7YtV00H1wWrYXpdiPn76bKcaEdUtYLK-pBOPEITS3t3EAACIZ5gvWTcj7Lnn6a0aGs4GRK7293MJ6ZuohmzgmUjdGDb3BZB2gooA0XpAKdD6-dVvKEmPTtQuXy8Kb0fanbHHLzranzuXMl7HBfFA8OtEP-qtozoutTzmlPHuZfGfxm8qbKVuE-G2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sRGoQcqAndR_OPfEnYFDrjGFlSWcuxSbghcq2fZ78mK6KS60-uc6oF3bkQq84PwFmzs0wbEzleil-iw7rAD2goWRSWO7NeZjvdZ75H-4g0qXlDYZXjCoaDX1aLluEEODQZq5PKN7qqCiY3JSs3zVzE_ZoSOVjtmfYxDV_9iXGddbIxBpNYHDNgCFvA9y2hWa5sc_jP5biLQWH81m42i9gGke27HErBStmQd9ZDKn4FjhYNelTXz6k_ZkgTkMEjf582rixMeGglR2lIjMeMycUmy8zMOQ_S3-ShLutBOulYSPKeYMJxOuSAUMzELTCTGD_D4pViFDRTzO9JOWlqOn6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K85v3-cFtEPJQ_ouSjghrwC_KGatX5s8qv1nVVuB0XzMxghl2pQhLG_WH4yzVC1s9rlr05hY10xWpg3GaTQpolmYIhaL4y-3q6xRT44SEq2mmAVFXh6EdCWMDQLUKQEOEmuP2EkMT2U4vDNviAKMDuZa5GG0fLUMchSOSHwMn85nsVscAyi9uVgG86H6Bwit4cqrsf8LnrOvHCVIdHs4o1oOMM3PoLrFhKnlBsMZVSH2DzFEE5AmSSDPOKCH8dIw4L5ee_-Gi6tOQZZJD3f9XfTdGxqXy-eQJLYwqvrkCEqk4r2uekFcHTb7JkFWPn2vqd2mBQvrBcWPEMv_Fimztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NE6l4SI80U4h7rHQZc6DlEiZvM-Rg8U_E2ed3C5OZq9OcT-_e2GCkcAojz-qZLLgouOOmogiSWcbpJ8q-1WO9aSHNY-h_uiV3y-AL_wft2XWdWQhn1BfPFZmE8C2GdwA5oUKeT0deBJvUV94a5efZHFxfHGuaOWSIRiIhswTjMXNgPFF4LqJa8nrRdR34hTCQ_KF-VXDveumR_HiVbS8sYd9yt5WmUuahbKgq3YS5DbCVRg8vyvL3ZczV4M5MCzP6OqWcB0WpCrFT2x75_CPXStu_DyNmc9kdFBmZGqLzZer0tGdbAyUPvwk0EV-SojRixS6mv4a7fyKa8OOrCYicw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y3nlM77EqiZF0m-2Rp52FtrdlnlOmRgXvZZLGP3aEoEsinIhiZd93igP1-q0_Q8hZtziHQk_0DgZXJz-oi_Fw9hYVLnQgIN4_2C-rq2uYCKcZ2W154YVpY4Zx7gffkSBaxQmFiqql0cExPHwmqgv20VLjjgMRT9xVXxnoiaShFSaFVAa5pJWRUHh_l0pWLS5Tjs7FsmC3N8VEudYfMKr-4DHvqm3s9kiaPDwQQV06Lhz2ClfMjNd9x12Oe_e4HeI2psR9M-G52bfdbmfYnHCWkLITpZJa6S3iPu9Y1p5XvhcPwzfY_A5BhQUPggxF57LRMGr0FOBK7tZJLAspw9Jfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LJlJybbLQMNqQV2tzVR9dEzO1m_xyddNznXmp2_S6BfauIX25L80uybKpmgYYDksGVyjJ7TIYV_Dvi_GYyFv0rfCpIcKbONnLG0AJ0IbEA8Car8v8v4t1iukMEbufdfaC1f-pDYoEhRfXltRoPdjYk9d5Auvk7WIS4B2yVrssU-CZ7mLJJYbRzXDUXUHCsCFZIi71ca6UxCwhN7AakDesexCHRyBIiu3VK1BKisb2U9RWNI3ka2OsKyJ1neXStCnYWhNWrGGRnloTgp4bgnv422zKKwRVsgCKMp141TH2raoLhBFO7uMWWsDhMqa7aRofAvAgEyftWDSCpT60AI4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cis_PuL_v6UKlqIa3k12bUerl7YGkhdSoUH6oBikYHQKPR94mkrmaDlgonEE_fUQD80VGkSG7ysYgDA9sXi77qpRzw5nrbvS6FuViNbgwgB-tDs0zzinEQj7umm0mroIHrRX0bxQw7qGcu9MD7Vm5ZQBNIBZ8F7cTokh93-9U1qMxhjSdc7hdkOCJV1VdFV9YDjQ2wGueoDVJ8Bik9UvSjoy_OfVS7tM1Gz6N2O0dZBCOa8RlThjSFZuKb9WdQitEFjMSc464Qod2f_zY-HZRFZpfBB5fsRayFdIJl64gy4wcPUhJryH0r_fVw_GBgZZAdco-JlTDHkRX667VwBF6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aW82A2Wa-HjMVPUO8LgOXoCXYeoJhlPBVdHFScRXrp8hXU8CFTD-2c-cGHOXjdxZUadxen9Xn4RTy3D1FXxMdciZDV4jG67D7_DcaBlYfR4NoaSIHs8oGuOKq7ii4xBy30Gk-WMyj3yNlyz6ldLo2CFFa1zoYWETwvnLZJVdez1aiyYqS-xTTqdYvxejMMedW429y8nbnG1H0IXITQDQoEcJ_YPWNm28IPp1SxHvmvvBxYWZsSLXhOZxX7boKvFEnZ95sCuwTEMOPLcYfQejixOXHDkKLOYci1BSsj-25GTtYFWlRywcXILKr6eNLXfSM0KT2LHE1M4l5RvRMk7ogw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/svzbHCeVmMShSeorbebeyUCw3duocgbg8DFmFHTfUmDix5qh2qJbvWBs7SwELA72Vc-o196IkdEnS69iPSuOj3TgWIDNHPc9HyTIP4aeQCTRoh7HARxERKqyQtP4geCIJBgVyfEsjHssJZGc9emRsU57KCX6SjZ5xjw14gH2KgMCvbTLh9toDu9u00bbJdPzhain3F2RU2bI3Lexmc5XqvSx28Fo0_oyoTtbOEdxmbOhEsRCzvnaAXZgzj80vUDuVqZUjEgmnAKCO49050NpYMuMs_3IIPcl0MyCnx4C4e_pB5JeztV8xhRI-TPh8TSwBxD_QaOdS_-lnsAuA9pMQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PLbtJLa5oREbnKq0n8GSO1_5LK3DMt0nmWlbhY7F-u7vQwj1pDeNMOdWiI-kvXI6tB_60kO_hd7ijs_PWkcsvi2--pA9DWPuW7b8UVVE63P6wVBHN4gDhrO9RPX394PwT_nXE8U6xEbXrOFJ_jTcc9xxQy7nfgElTqRgz_fpYO-F8-EpGZDPzos8SKC5ci7VH2oTrA8O20dJQYis79OH3P7xvhCMrvZY2n1deO6XvgKs74kJLyno4I91PC40LrlPFa0vVYqvLeh93KG1o57x3XZbEv2nK-psG7pakdSGibsySWKqd3EGZkhfCao40wXZVe6FGjQ4HfW-gJo8Xy5PYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LcJmL9cJAbVLzpyC_5LV6hL1TExNvLRfAYtCpLpJmeu9HVTNAEsH1FTkO_5LkMQ2ndWrF-uhCsalzcidY-zSUpps7-sKk8UfG-b6sGqCPmmcMxOFrZ2xnjUng7ulb1b6JgKxAw3vIXijOPsbR0LXgJi12dQBtYMTdB5V_dNO32EwcPxmzbBwwlZJVv-Cgrg4XAAx4hCDpf1x5kim8zgRURLgD7KH4-nOE2oRP8ERDED1ZfKL8VoKez8HugWF-gOvwB29Bl7j7mEGL7OqXE2xv0hZBEu1lUnT5kZxa2UQ8E1zWIjqn8IWlE-6d43to8KvS9pgY8ylGAHeEVXcq8-3iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BFonmRyoMglhfXnGQ-5YgXvbYNI1bo3o514TqTljKfieKLDFogtzM6pDqsnMP0k55oxnwK1O5wCUyBTCrKM0D67kofWudmy-ka7FUhlUpbDRsnQ5M0FQ3UQjD0PLu0zmjtr1asoscSWsVa21-dB3FaSG-trp69OODqz9ExbTtijF_GiBTlPNElw98WNVlmTPEO4Ck7xUuSA0Udj-oRuXHYSWWDwZ4V-jT7vTthfgoXnQRUpTKmtoNNgc6RieslJWPlHi8rkSHdKF7Lwzs9ymbR-ZurJfv6tDDdqR3hk8ORW1OCl8BTiPEhk4vrlKJvIiDQZObwqI0wVcloZJzi34nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vl9svmygV_nFO5RhuV1a0TpMRLbN-hGCsv4TqoDsAg3BF2myZY_LPJTmcpw9NBsPArhRsxmpkbnvbYeHhfVlI0i_rR46iW_vxsJeO17kzlenQwtDZr0v6myDU8v2_jKq_mfODyUfgnk699pLuGrlI9s57MJDmaBviYmcygN7R7wxChpmVu-nQ7pPzHinpQNq3-JzlqLQDWAvSF8xHAKEgLYstuwKpz4zIBDwk_rd1R7AK7XPW2HsKf03AR05c_OTZ2fCGpOAUx3H43KPIpHjjxIrZWn6EOEg-sTK6EKgYqVr09n8GM2QyeHDxqpv_zo7mjXkhkD9aJhdWR1r133XJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
