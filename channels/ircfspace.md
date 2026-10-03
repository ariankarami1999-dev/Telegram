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
<img src="https://cdn1.telesco.pe/file/J-k30NQq2igtmc5N-XPWwloqHI1sJiH_WrDoUSiQUC9pZI3KfHYtcNuKbstpUBvYLb15PyKDrQAOATGrRUV_FOWiGv6NzDx8zjNfcL73P3d3bVKyGxUjF6TNccR-xKXpADIz7rJlgJedKKPwebz6Stv-tLs-6sLVvIIyVFrPA5Avgr4LGYGioJvt3i6MPLBGroPQrfiHAgKyhSqHVtMfzsgvm1dtOQNNi0czCNxmhH_a5GA9jiS8rujWnKR_b8JzDJLw0WigiY3ULf-jQLGITm9JVCWfkcJXgckV01MgsEKVySr0vVZlCIe-kmMX8j-L8LvZU3ANvVtCLxMrnfXdQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 01:05:37</div>
<hr>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fWZBj3j1a5-4MdDKpCP-gJcKO6a6vZaqwQ6hVX5WereBYZ-wv-QXWAK6eusslyWrf5ShUPLkNEOvrI5b8gKvIPZ272FpoHAQxXg2chFzE5vkvoGDX9HGuBQ7zd5_kWPFTFb_iM9kl5QFWz5z5MA7AT2c6oVrGqJLEpAs9WKG4bY3a6wJEbrpR3pqL58VOEejh00H66ZlfEvk_QLxQSTIKf7irh3nn9UdGAFDSJTYia_iAfaRBhiH9LJoHk5W-zP-K85GeD4os9x3zyVrLazOhAZnuSVngWhEPvF1Bplxnp6EMTWfwQnrjGVD_M0EDQydb35lvULGj_SF48BsD4Tu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KT2BtwDCYT71U3Pe6VB-RJbbx4tjHSWAnGP66dqvqCgeK85o8f0qTLzYyqa2MolM7aBUHpAan299qa3Lkxk6PpN3Lu2pae6IixYnSKb5YT12IlkHoBMwiqjJ0wlQZzBFpWEzK4fVX5Df3q-U2JBmAwgMixwtf9fd8It1ixpEJ9_FZSVc_9A7WkMnS-rjexwjwvbvnf0P3R4EXNx3JAyhAM4JvOwOmTqFMuzHz0UC5ESpujeYsMl6hUOTqDio1e5cDgP_vlA2EFFCkRvg7OdWk3Dp5HZ44GAzNodfKqPa_5RsMdxFfq_FbcdwgTFRrpLAsCxVEBPdlRNqgnu-wiXWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F-bBUezedZSskea3QRKlgLaRe7Niu6EDr42FQYaNtBp7PEJhGtknwk2SRLklwIuhNEmHjfC8cSwTLHp9otd6eapCinH8gDQ0w7aEzmnf1oiJJ3kv93RBNcYxOycsxB_O1EMDdo-EH2Pa_oKVfoApXLOsPrjJqw1wRy_DwS2gPGPe7rBZZ_wVMFcNs3kRSXsjTNaU2m0I61nc4Dz_WZsQxGGoayKISgecl5YKGuJk3X6L8ZZfx0lkpe7LnVnsw6o2jQ9efLTnPKa_ka8mQElBaEIyfzG1X8Ezwt-SO7XAu1gNaI2XgoPEKayH7nrpETMk-ggzctiYrIqoTPQmHWQmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AqloXxAQGJIbkTZIodNRLM24bOC8Q_If-bzEsjyYwzgdtkV4GqUAXm8OIuXmMexZyU56HHF8nKf2Ouxa0GjQVbkoO3df8si1Tg38GYn4xgUOxdF9uoPVO2p6jgwmVg2uxNbBgH0JjUvgrSFKS-RktwoWg9a3YGDQoJMFQk2cGg7o_msA9rdBcZkltmydFTnT-lX2rPZu-U8fgeWpONhgOwyifXPHLaSY_s0Xj75Rs-HCyU8CCzaRHK-OzyvOxxj7u9d2VqEuVly05-PxPomQuFl8MdoLZdsfyZCUyqRuu6KDc4g_i6adxKsw4uq9AhSoaL33GgVSafbfvs-hUN9s-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLlqusHm7fOshWAdLMlofFCbktHMtu-zsnp-c5xmkvgyixTrSdruMo15FTtp99UkEFlpe6afralcfP7bMWCikZ5SYKZi3P84K1P6CmrpFmfmvBKNVnAXJXSPoQV7A-0Y9cu2L01Waj6Sgryd40A-Zmwn29gTI7Xwps0KB6oRVdKOue3bvRGFM1fzdb8vIVJjqFbb8sG_eoSJhjGqvKJ-OaT1i-KlHPVUNhuop02nLOKrRDoJ3OJTw6kK691mBYJGZyr8YfinBt0rKiKc7bH4f-eQDb01Y0xE5L-mjue8yAbmNPyRtM4CkeG4m7MBSqpinPXnbTgqYgaIMI-jh4s4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-bFo1_o1CJa29E8w0IG90GyTmLeBVS3OrTgMQzdokzLI6lK6FfL5xUWhEAHOX4QUZT5DywwN9elJsJDkRV-JEdQ6x45nj_CDqTOx-rBJn9Iht-YMqLrZHxmkLJj32J-OQGSwd7HvykcJO9bRie58Qt8Blfeqn4e5BvJ3l3qfNTbhwC5nJBVV1ttcu4eJStF3CJQPEQ9UCZltii9fYfpgKmV_Zx26bxRI2hX1PftM1LRBx3_gHZ-3SVS43b1VJ6bYyxT_PIDQNQkuHQWueBBCdMTcD6xeeFm93wFMqVMNQ5pS81SXCEbXZXO3Y0Er-tzjm5O7s7gEpoWPR1nn8gWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PlevegkyQ4BsQYVyjvpEJArWdtsjXznDyL-y8CBeUdNaFhFlNg7Kd7yeg1me7UjsLNp5vAdxHQhkrPUgcHyxtU62KRu70EYReUDnXgHAbn63bIMd_DWXYKubav1EYPqzKbgch4PagZDHVTS40hNbcUMZRYVL845JgnRjm8m-5Km6fJzcpX_Q2QXUOpCPrE5xn9mjbugl75oZjoFqpdmGtID60BaZHvcyr4wqte6nHAHIWH6YQnAmKsG65C26p4kEeGRdH6syuH0tfw3py6-KtNLORQJeu3nK9IIB9LhlHOyMSKXkII814GALQNV_9jkGV94xWFy6L7m0xPutZ9ag_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jXXzERcyiV657NvW2NL6GFLud9kvW9lUAuo1_Mp_J-crkPlVbVtUB9f2Ig_HpFolWrNDgWY2q0XoPbhvbCho1K5be56rMIFpu1HA6rmtl-7JdVxsGUDmjiV7owkdkpmPuMzXrjrp3YhmV15SxtEwcSTCjyUYebh4neuGfiF2enxeK3ns4Pjv9kdwLZmKYvBRyoAr14KAqxEb1r2t5u5s8GALP0cwwZLZKDyRw9Csua-1kxhox4_j5Gzcri1AKbR5WgcuwQNZfXQG2g0fU4rCwmzN8uoG0cQASlh0IDTZsj1ua-GawP6cpTt-TCOIxLJDkxaGoWc725jzxmOtTCtI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZW-91koKxVULKG_lpXLo7DZ9jF2dZROK0Hoon2lhOgYNS4Br6_N9UlvLODILWqcU_Ib7tp6-vXI8N1zjkKAJV7z8Qis0xEWSG3hs2yl44ekkb-5ZvNdJWl8P0xwrsz9UlDh2SZT0kiB5HUwCRFLSQEn4z9NdFdRp0q93cm23RojsVVlxewp5n1Ui0818vSPmkjtjanSc5JADktJytMYArhz-uHiy6sP3GIkIWN7RPsnVIU_qRI27cIbHe_yoKLamZCsorX2BBZiqxC9fq8zb7YhqtteKNdvf7CRL5Makc1TuoLzsV8WEnrcx_iwnBMugii_WJJba0LkSEV057pRmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UP4eAPyfW0O2FenrRFY0bCp6ITsTVTj6Z5iyMsPCiyw_U8Qa8hr6uSazD93-wohquf8civzdWYfxBZ65l0hWJEMtaTHAdT5ErqinD1PSbYgoS9ietV23DcojDtPlOl0QC-9fF2g8_K4ew4HH6ejK0C-rqHCaxFGvAm_BTn5XkFsxiLT8DORqiw2Y5QF4aFaE49G8wCJyqvpxZMwVdbDb13i6KvtcOE70-kF58FfKMBtrIEVz6lDQKLUz6J_FPB90I_wufOiukMjuET9XURJVqvLvDHC2DRCgL2SRaS2BMmG60MpR21_NosiR3zXi2tSRw62Ebc9AEThiXnusaN87-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UoJTbKM_LoGp9fOWVzV0dr4_v9AzW9SHHVWxb-VnUghH84eY1whApwg_XnX9xekRZROQBH9CSxJWl_BfXwIdvHhkVltYvbdIgBjTv__PUBdnhekIlTCm9iPdbgO28QlD8kFl3FDyuPUI4pLGYRvRwGzu2w-1vwSSzoR-1evi0LPZEFHZQA5h1-8bT2GcjSCcru1071fGRjx8IF1AhzLDCEv-TWtHJMJhaxvIqU5x_mWeBsmaA1ke45OsRFkxE7D9rzxvJ3DnKyEhwSWykPkOixGRJ7lbuyAa2x4mLEWXG5wLGhDzbMZp5FxRMZRJnuwjpNxjsjKMW_iWf0fU33g4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OdXPFFRnqxpuuRITdUALOh79pq57Qbq7IVtcsOjFGBF3_iiTqE0e7xgbEEH6p4rYyGJM8K4w7dqLqXxizcz4Y893AziNCoETTHtFwE8hQ90X2ifR_9ADgPlEJXtLPeBuSo-WPZ4GAYzvS-qmnsFPMGg7lAMDA3IAy8-M1wNb-YNqQQJZVcBHhJPu8kabim5nfxm7pV15VXer4JXTBfhkjMlTlWEmRWoFbBG7CqZIYY6S_H8A7MkB18quglMrvPIXDsRLjh7MQZuk6zPSAQrsa1C3Rt39yS04Dv1_NUn2Bz8MIsslPYyOoGz11TBUI2t3QSynBVbccET8Y3wnO5bdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GGsQaXvuHrcIVB3hIxIiSgyaisJYXR_CTPiXLB9YJFbY-z4mmyS8nxU-guLUan-FLOEItIRgZWzSTILxhHEgoil4FC9953bSSd6AXav6PenXRymEyVKJQX7RRyfU6k4Gd92Zgr0Ncrl1aRbAbTJMNrywk9w4HZxD_hZxxwP12fGq7yWWMgI1UfcL_LyXYKd46PvayhNgbHsR2x4o5KAT1aQMFNfW_kkh7hvo8oOrV6hC44d-x_2j0dnzQ8paVFsvrhcxDu52KZZRaKmYiOeX_59q-sxUy3eCf0O70PB9HNLpga8fR_RFZKDIDfNxy3LY6juQY0kGrCxk7NOWG7MoYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvuU7PQ117se-zbb5GelJUeVSfN5U4TqnSwJVimk71UwM5gujnWSMY1QgGbPvl3HAwdG4U1EskUJldOePRf2h2bYh4vBWbH0aQTpuhcD4BO8AKg_bfEKdcbntpGJbeKoClvsRca-9XR2fzfv37N10MEWiRDjva75sYwYckYvhme9wqrfUE3tdhJE75b9PSrJI3nvkFaIipq0N2-HZx3_S3BDOk3m9jx0u6_mN6RrapvIH0tcc3GVdcmR6M5mC0171ZlqIMVpC0EGcsfPPVhPcbaHLW6gv5GlUvJF1W4iqFCSpC6fncWufBqmr93XzVFeIAYXev1ml5EqE4TSouNG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b98WmZBxBOjVVgMeKIxmmJ4Ij1Sl7KeH_ABz69OQElsMHtJm77bS7CMbnMlzxSU4HosKaiiIkioPjR0fGBlh2ACiIcgiBM_NRkJGI4vGdnVM6Gk3a_HoKNy_c_g4NDDVXZHkEhk3p2w5tRDbjNY9fwUw2WMJMrWzlZnKu8kmVPhlpBGCu3uk53jphQU_6QeVoEHR5h1tfptQRcLnIOGhW4r2KBb6s6z2v98rjrIlRJu-ONhZ57Cj3kV6U9RuyzdB2G5fOv5gp6YWh9tApfLcQFVim-7f4ZXDG_Yn0GR5RURiy7ll5Y5OmG2brx_xdI1KHLztmvAhmj94IFqZ1GFx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCIRRe01GozR3fyGWrBS_OOAH356JyEQ2RWWBRR0kMg0_dx0jt233alPh70pzNcMidSZtg5Y-b3uGsGatzJA3DBblVgGZVQP2pCYIMARv9Vp2Gs7Dn7v6pTV8EvXdmdOqsWB1Tlgt_57fO0VhyYoVy8vFhmR-XVd7TqGl8A7DF_1XPzkekaot7q6H2bZGf6M-9aEhziE-fYLSajaDk81NCqjalaJexDodB0rGxHvrodY_w3l93G43AUTse-xmfrz8_dRop40x6JUz2crnsT029kwUMaHOGN4bzPzT8GvkSFETNnM6-IqQLDx4yArRYAedHRwee5EYSR218pAvcIl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfahR7E70u43YlkV5RlmJHSQLVrg0XTkWZZa4WqMg9Hv-n1qUgCQb95In9y2MNZ0qriegG7sevOWUnbmEQIKHeZcY0fknuwzwhGgKoHYL96OLmPn8YIIm9c57Pn5j2YVZsH1M5xxh1q9CXMv2cWwZvmt9xk7A-18c43Q2Jxan5eYiw0mHjE7jwZTlywfK_eESxZLnhOqOhf4_DKynZ_NW7hKYboejLpjFH-GnYhUYJ8VTowwptLqaX-Y_74p0X9DTl_A8tujgW7cH1tru3Psi2FXKQyIL_oyN7MDny31NYGDAXUCgt6vB0nLuRHThbvwa8BTwA4LDNR2uW-ZuKFiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RT6oIdlB9S3oiK_wHnZQ13s9QAPeqab-2H5tqfp_-VwQDJsi5tRmQTpt0KYOJg-e7SY6PZFYV2Wx9-zQLZVi9U3b-oEDU1jfV49NNdloU2RdeOgjoHzpTBauRzQU38RMxg8CKEZTi7A2TgYOWh23mVEzEMUBabD-sWVXTYdT4kdaJQiuI-UQs9J7dShnhJFFmxSlwDlNnNf1RUadr0bgQSt_i2oMCYNWEGMMk_wBUfNq6ilqLBD5TM-1hNTkybsY7-9iM_M_mQNshkESsqx8PnsMmLOEBjZgAxOF4lcKUdkLLjSaVKW2WDlj3UxNGikuNZnqF2N6AmN7NDFlz0798w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QWk1IBWt2HDpO_4j0Ltm4rhf8N55ej15ccfQmj27hXIep2oISI4gozq7GRgBoVXyIGXlwelSrIfNn_kV0TI7atFokJ-jA9m36uUocywk4nqUBY6af7UYKHaek0X8nb3Co6Th88wQz8ShhHXrwMZ8cTNc51OqoOD82RIeJG7ns8UJyL7RJxyrG2LLsxTkxIagYFW_aRPvgcVtWqZ_xLvAHE_lU6bphnPBd3E8Dr-iXkreL6kqPgf4itXrLF5ZFbykiG9FN1MRN8ZU6VBd-_hetf-SWtd7iGmvdRRdutH1SeG9A8Ge6arO0PEYYQQxJT8eKqAX-JVfBEndSPbNX055YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iZXfKyxs47I2F0UOB71RpGu2q0Cd_LZPykFHmwnY-GpwFqStToiVJ6_88btNHUK7Id6NXxfk9H6du_upvF-ZIbIR60MK56gny0lf0kKcWr2mYnkjzBXMt6tNbCkv0aBnIQBtn7R8rVPzGnIslmzT_LKz4d0VHj6LCb5KFS-aCZjWs8VnF-Hu9QPTjhsN5Xjmd_lIJ9d8AYOahc128FVjWfjNoRtHacXC77IHt3UIcLmmJPhZ_E-0Fbo4DtmmQ-__y9HHsO8vEN4RC_Qv7CnxmplHPmJ1aQ3WN5_Rgww62l2FFuVpWgRff3wbVAHoX8KEkw3FYTNJTa0ZX325Arveyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MWmmIW3bezknyqzYM0HUk9SPMf8XUGmRrMGmiEmV-sx6NCWFMRuQyGoXziG484OMSxqqsGKgfVvZgdtcdUzN1p7QYSOB-gUV0_evutyoGwhCXAo5I4xzMb86oSGaLVNCgSuoxzGa9mn8T1qChAiO7RiQG5-CpfbjVGOyg9FLKvV2cntptCgHxk9k19tYookf2s5Ysr2HyMFpRlIlNG3tw93jAf61nphvQfg8iheCZNs2xAn-3fNn7IK4UtNqJleN6MIjaBrcBfrQqj5lFQWcgQSy5GXK43HhN02V5VY-jyqVTSvYhzqltzYP3hayD7hto2ZklFGvBgb1aWef0WOCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rl5vO-NhqxbMtOBt77jJMrPKdZ7gPhPGqtAW8ks-38xvhhj2SOj2SQ2KLjtT8Yd2obOquVgWWHXBIbyy0l5Yhz0woOoK3xFitsyaTD4Fjx8eoLOiJ2-OhW5GnTr0uMmyXNYkx-ZiIvbraxYsFBSYHLQADWS2wmlKhdiH2oy_cj9oInCy0i5jSyKJMpUlHb8QTDJYrDz1uCssxFQLkhC1Es41xLv5d-bx7yozVpBnoIoK2BijRaNCqJZXrNmRfAd_JjSUFa7xQ31s1wVr-_1bD5EBwdK0WNFdgmYToWwU6MXJvmwY_0l4iolwkyy08ZixDE__J3DAnxDiNz4Fu2WtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tVGXYRYhgCvXbTgl0M6Trtt2ucQ-JKlUD8F0VnBDSUXuWAzG3pwIkUzuQZwk7RCLr4R8u78OobjeeTuQty_xHzo4ePbQwLs44oAZGLFrltNNQr7mNQHDHxM00TT0kxkMfwaThg7PbpzUEOhQVdljz2fkrKHsYSsDaUUZPviFPgi7ppxN_t83AtGHuvFE_rB34mFWBbq6nECd1S5inJbdC9KZ9eN--9yCVkaBUBtNBm8ckfrZzX4mvSVyRVOpfMdiIVxvMlL3rjLRKg3pWfej9n12VOEHzp1WKIoA3wyfaQ9WjD7geCbRLuVXjVn995GnhSjtoE1e8bs-dh9isSBxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/siKB979SDAfbP-NW91EaT6e8PcB0ut17DtuYwfKxhuCpJMGvlZxPiS3XIgdUnEpXcMX5rrldk_e-uZZrpLJbbicUMEKXjeKyhHHV2IU6q9_Hq6avKyrofwEvG_fv5k1BqeQDC46DBt1MANsGzCX5_4d10212R9JpfJI1dZ235D7_wQni-_S4vp3GFXIu6Se46muhk_xkLcC8BSX8aBejh_vYbQQtJjZxlAe-JehMSZUKI6YhYJFFLAWl5us7kXywfcQfb_KRVnL_VAOjryzm86rHevD4Z8Zm8IMuFFjF8j7foaPPM4-1lxMh8jdSOAWUrL3DrR9RryW5DzPG1MBv7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E20s4sTHm-PhcZuVxeY0O2dWKt5lAj5LkDDDmVaoZfhkWCcQgpvuJK4MPUnwd4Q4u4ITijakzGJtbq0DQmFb8U3y4LIAn88Np9V66AYJ74_ogCsDrCfuyT1kL1pOEz6Y5lTn6QBG0fEnF6eTsx81VfB4pw5A0jMzxDVluKOZnRBxwwRt9fZgDeJeO1AW80uK5qbnTq97hOMkU90e4Capv-SoviWC7E1tqMW-JkLSzxh-pyz3ns7YgYSq6jvp53EHREY0eYIYWXBOyJPHLbAn2WcBOQIljeZTnW9ilNIxfBdMoAm_s-Bp6RS1AVr8YA4eUP57O6rI4fT5sF7vt_kclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQArgua2fhMYWNXTogM0cK3Ne6NIGX0dsKF8pvyR0t0yhHMzlmx9ZHaYymY25OrETtvHF3z2ovkpBFG8uzijgmWsxTfcZrON15nH5pggd6Q9tX91VLPW_wjZzXqpvZWxb2IyCd_sVy-H_aUwVyR0vmNFsgiALVKc6G-tGOjhBtkhCLO6O58nbvw3XHAu5rHRurWAyRNog8JEgNeY434JEEkpcDh9_a__JRG4tFVk619V8dHLT9IHhCAjhysgR5PiRB2TfvXHbbnStzrh2Y9YfACDwafqr0x8oomoDMaJaoptN4vf121O8j4YcXFM_QeOeMe9J84R9HslUn7DB4n5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FfvuAOzNqJqBuZb_dgtnNA33Jubg8d3IqKbpMEP6lC7jyFzsOIXTiiBB8KU14lhQ6yvAJgVN7NUDqUMtEbLcZkxEGGUUGddU8ZcsBgII28XxWXiMzzJmnFez8SaQyIYsYO9CV7uGCP1zioIyPOLfuY4h0P4xdNWSpSyoDfY11sO_ivmlgY1tHUcgGTpF8kvf45HGfJkqT0tsabVecboTuMA8UjfblrqwyaPvyS_AOGttIFeeE0_Ww_fNsl81_2Xj4CuCLWZlJ4SWAUYhn6h_SIfv4gVFyR8-oHZ8YkrUBATqE14oS0Z2ID_61q5e-V05bXJirQwIzfvTDswYPZPx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oR6fPReGNKNIumNNEw3E1udqGVqfTvTe3ptXOx38X-1NIEUBG4irAMBXBc7sc6ONJKxOsusIhpAhfgojjpgfb-TeEhzG5n1YJl0qj6rFTCTG3PveklisPo-8X8_QuO530GRv8_L8dNvPO1GWNQjJ4nk_B6NxzE7h6kwI2OubFZDAkDcUrYauxXLsHTYRp7b0031QtR5qJd3Aq7CDA5t8qYnUF8EoEoerZd_xD7nd8dhbNVQV_LbeLc6YsJ2-DZPzlYPtrQosggn1GLuGhdOziswLy_UsGxgiIMacxZZM_WsdFCC0W_hg8FhhqjgGwtPxMQ5pZ3H0w8ty9upgfSBpyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSPoexMTIKP3bn1x-TLSusZrqCx-0iwXCyQ2xV1xjBhqXWdPFsdXB_JqUbbhVUdHnkqAuJc5aUZN23Xr1-clKL6SNSKar2xBIof51d9DQvCyymuqigr1Pf8261blE961oK7C7jbsr4-1gFjTxyiQInYJaGw657OWqs4kIYc4lBTt-hTxXz4nOuBZmynJqt9C4zSp0PA4a0hYxrAsImGdR-QMerKTj0JiCJHmf1-Pt5LT9Itht5HHgH4081yuGj0sbopaSlB6ypSxIXBQVBxOV-wMJHCkrTmGOlPYWunE-K8O_UMV3M9lwV4B7xXRKhU086Nj3opg4gJ3adW9yO2bbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dGIZEHkFYgq-tKLmSAqpmfP9aHu3TxxAXCKS8Bk6o6HiovVejgqZpbqHVrUYN0wcP2gRDok86CvSkbgzLD4t5STlh54i7wH9PL7yEck0XCsXaplm66-KBZ-vncX70sajsjEZ34TYmEN1z2d7sKnnmAhYJPkCecSNs_sZZ5A0V4jux2KtnHHTwYuJziwpdWK3_Qhz4GbwCmpMyHkiLv6cqDI8eAUOCFm0lUZW84ZH6avtca30nFqVEDiMqrLs8LozQbaA3rCekODH3ismIEabDHSfbFCSe9xPWl4OyW3wrbFiYWECh5OGctixZa3sOwewo7WuEzqxAx_ZstDT4FCqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r-K3UlhgbbpKxJ3XQhm19NhZnlNR4IXBJ74QG7tzlGVWPZobFut1MU9jpxGjeeDlpmzBBNNu1I6FxiUY94JgwW-IAtggXCpxz3TMXgjz9hoOyWr1pDbv1taKMHi7AbneSdfJv5MVu0jaYLJFwCiDIO1P6e1wZMzgT92d--cS7LEmtvBCo0hWAiqLVAhqpVJ6ueC8HYuF8nvaDFMtm0G_LtSP8SXmJn_k2Ua4QECCC23u2avG6qWW4uv7jw3WYxnfdE_yNh6noAUJucXdoJJgiJp8SO7OHyX5OugOvkSwtpWMGCY91RuefCKbuchwIwNs2uZyyVTosN2iV8YaFZLxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n0KRnt0OIH_O09PT7TIQ3VA2zLDYyW4mG_Z3GRL_OFu8-i_ZOZ-spw7eGhaQCK3dvb8tkw2Vx2mE56h8ZEicChMQGwX9gukLZ4KbTBtdGfYRaJeAcDRGbkA6L0apjPAGyDzB4ki6PgGQs8LhMJFIb018mX4pKKAoVFje6s0Ul_mmq0E79vEC89rDhU5kBcW_R9pvZFw5CQpaHyzCmVKA0TLVCx_H9qUXykqIl8CvEk_4oLDaF37Qrrr5XWzJ7OxrOSl-jXTkPKJdNvFtBOtzCfSwj88ndX7x6JZvgSz7cg84aI0EP2SdMxVqiYCbPoZjbj42rvDvxYUmUfogVfLQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VjB6nrfMmrp5uRyCuji2dG2yKwAxjVD3-Kr9SI8aZh3zewPh_eapZZzsXAgbY4phzUMeqwIMYcv_q39c6VSRmNNPySMdjZp1Vj3azZ3hj_cegLKuTu7jOqKmzgNpn-uMb649DDFJew2WPhy-Rtb2Rf53rPFW80nNWcYutn8LCZQtL6o3uh1-Y3ijB89g0646CyOlMkZa0JyzFn7kPyTUnetPQaJCZkwmuq9-ScPwV_XdqOCm-HuyTjtLGJhJzrRHzlQaSV97h8cUKm1QkiuKYxVtcxpLOkCesTeKVWZwxtzfDsXVLzsZ2OFDvoIFKsiomlLdo4v775zjJZiBCtA-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u8FI6jv1E2RAE8dwrtJpozh9LHkrYScV_qGa1LnEDgF2vGH2lZrKbDtbwD45J1tRs44WlrFiySyAmb5JHpxI_DWDYU6FaBRN1Pc3IYo-CWUOiwS8p8wktg1uREsYCsLs5NbvJkENKarrvJULdDqhp_7-1bSc-LIC8hJppR8Gq8HdY6sxPxsBqYQZDctqzWk1N7PQfdYue7AT0a3LdqpUTH_RTZg5zf8_ZnmLKI_n89GTPg6DtNRJvyvqO8XEJaiMrXTVosh6NxUv6gIhlX1bmxPlEYOIZYM8vToBrX37UI7AHS5v7oxsQziEqoWTlWq1YvluLQeA60oFZU2afUj76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c7YWyv8bme7TnYn33WTUN3HjBmkPp7CIgPTwXgZPh2D3dUEl5CIiNwvYvOzBDjX07-qzEarYJM9ffRslEFLoWHqjkBJhBRp4Z9q8GYGB9OysWQkIAtDfz5Pk2tKocHMwYC1Uhv2OEeQ_fGEx059XVGgYOosW_HC4kt_w5VsbUgZ7EG23QeE-jc8NDvofMzPJCnv6pRWdXnxicttJrWJhdj-r_pngWOcuPud9RynuKvDQTVjTYFd0fxidDoDUPD8EYZOCRMHOIzTGdcSzbsX5Ts04ckkzW6Z7k-NVL4Dp0ypLf09WnKOZ1wZo8YduOxiCpLU85l3zz6QVquN9FsQPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACmY-81mm5yJttaMBh0QMy_LeoN_1RHw6mjSDV3AcmCZKK447QjAZypQ_wTl1nUIKAvBTaTadEg2MPQZeNU4nUGTMqfuABoXrCpyzCVp29kpvlZZ9E9l5bx-Pta3tZO6qNj_6MckNt8TD_n_uZTbStstcz5HjvdyOnmFY6_FxRD989VYBBzGXUjJhg8hvvJ_qutqdWHCdM8BBbTjQYQVMlKqg7U5K6aM1ABqLCQ5s7RvS1ANMGSnuleX7Zve40sDNCK96tkD6Nd1j2VU_Ru04o6jSlOL4iVeU-Z9fQQQrZhRv0Y_7XKcW-T9nqzSlpx41oTLfhqtXDsei8g_pWqWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IPBpMQSyCKDuCH9FL7tShdyl3HOk6utGvuibhwnkchi5HtqnSNY6EW44yHWUXVV4syj2Rb-BGwhMuYsJQw4UNbxS7zDF5qstYl9ablSa_1pZuM46LCXv3b5BpQS1FTyZmfzc1YWzdlZwLfoqxiCN28eFTugMbw2GhAR8mVkiumCSTlPmZKM_dzjK83BMJxLgV0VfFNK5P__7M78GWHoRgRMRnL-tCIyTMlMPXwpbjiiWoRXYtvb_YTh8F-3tUIjnBduIrcOc9T__Yq5rgaHGUpJ1pGRpZytLwuB5Sf3zvHC1Ex9bTZCIbeoxxcL_YNOfUeAYcR3RJeizeZ_ZtQKlTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IaM9RChZxryVVX1VCIW3xEqdNWXhDrpkUGfAi8IF5p2LbERz3V5V5aWfMvRv1gdJLTfm18Cc8pmG_pAtBB-Jr--hWXZ_1ZwToMC1NGf2DutWQa1HcNfxC6107kaj-ztNmwkop4ee8nqHozLDcR5Z7yy3XEzHNRuXm9iVlrd4xBLOVjf4XybqYNSr08XhXGB2Ie3qzthVvfQEZHPxj1LgcS7hnKW4JFrjkVa_wugDtd7uLb9gKJQMpF7gn9_rqjnnTLjYLtSMXWVx_CbMyTVfItXecxa6iUUjunvsEYs31LqYKm3y1j3JNVJUa_mhNyAA9X2Le8e3Nz6kTjiP2Bn1LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E0sAe-mHfhV5CdHtq0Xfm35aKaRMJcGbph7nQFs1lmH_GDzSwkbIzHQPVux7FIZZ4IVMg9_4bPbGQvL-DPEmDGf4y76neeeQhwXkfCotUJEnC4VBKnX46JpPrE2Oqpy2YSGuosoxedivzPnQA_GqJGFZT65bplbNqEOLI3UouW8a-UDneGNP9kJILm0giRc9TfG9Uc_V1AaRZKOWKTYu1W62Sgj3ltIS6qcAXGklwBm-6nrQi-N6VrGkAnHUE4rQyLh6dLEEJjqgIxZLsDovPpJ9UPXUNn4wYfHej5902ljY1mxgjHTy4-rJdJMZOusOMdahNOhPNcf0UvEulpcZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lhtmU2kQvnUPT2f1s28v0PEoNgUUp9onF2yE7IXHdj7GWaJL7Kg075Tiyo4P45lpH0AH2svoYVm5qoqefVlXfJZ7MVzW_6bhJ72_ppFBuD1UVElLjdXvjrTOrQdByAc_1AWpxSurBQY6W0N8lHAj707jo3QFDAJZWvjF5rQDYpUnk_ZPgFZXOuA_OxYTDj_zsnA8d3M4DnpUIOuG8UD2j6LKkgZtyqb5ate-vGsUF8c-iVWP_cXXAAkbOJeZ72t4xwWhP8icfX099QaS0Uf_8xTOdeMN_TnKsCP5cnH2W5Of0urwWxFXdRwFKWTGpMtCP7x41luGejStJsRlfBpGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XK8KmqntwdD5EgBzYR1fwWYcoJxrVf2AA7sE2AW7UhD5QGAB0XED6L1kPP7NkdgBJ_K8NmENjUm0yNOaJlhLQ1lkeCRz9UczTVWIHFtNiyPVt_sIXMmlpnSFbCETzcL9BVixD4fMeK05y4eBy7xdQFtwU4Yi5XMIg6mA_G3LAKO_H_0q6O1QB7zKcMttYivCC4ArQxf7IWjfSu5P41LFHQySGdhiYs66wOmVN2pSkepf1VOj0ac-ENjTPdlvrXHcuiApZ2ymMMKQtVva2s5RTtAzJdheP3K0kgAo26peSNIKUoWf714FavstanI8tuL5puJOcHtLLzPIMmH-y8mHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ty9SWXyANhkEhvzTTKTj0OlzmV25pCO7uceCBEKZfo0yd9OnuUvASbu_V2s5C2x5Mpdhe8Zwu5jKBu-ujryC7EaoEfC7zgM_FyV5l_bf_GTHot332LsTXvHbUnys2K2r24TfrF1pifUevQMjr9p-Q3wsP07OyIEV1b_R1lmPkXi1glhKYr3EjrRSBQXulcmdrzIxnjfrO5gTfpbygcLAWLFYvDmVYy32pAsssD6d76L-4nUsvkZ3l8hQgD2qN1JJTTpe-TY7OIZaAgTqxroYBWAvHF6npGDdG42QJ1FLYEW4NC5DQ-9GuxrdAECd212jBH1r6DuAp2r4PB6otHri-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r9I5bmQRnO7-lIgnRQbbZJeOnJAJnonUcuHdAeups9207BSLjg_PI8Om3UoUybnFTygTFCDAhkH5iLFmxA-Hy0XhXLo6WRszNYqbMkbhB_qSzTWe9P86mOfd4yd36CRvOvMVh-i0VDQ7jXN0WgJMt3DwrVUqq60RyRbilS3_i36P_C_GRBr85_Us9rNCganqV7V-li--ogqXTQ8JhcIOg50WrofpAUyDmPi4HS8vj5dUl948FEXGXU8f3M8sQE3i0LAZV4aVqSqn7cYXc0uB8WVc3Tp9_aEBe1TTOgG5ZV_BZFWzxceaNTILR7Y03mb5AoR_9ufVQKIzBq6FxUO3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o7lKflduJS8jKbOomFqF8h6l1yIGyucf1i1-4G87-G9A6-ybhkfQHDKQKORcSfZBs-t79o7eKcyuFnsDpaJJR-yBiPpKuz3gDArvGGeoU9ewuthBUwTkryMCj3lGUsxEPIfSboz1VTVfucbnhUYmCsijiG1WSqsa8IuwUP8sOC6a3N2FrMTout033op79RUjBjKAovCyYSerGlREvaGXGolNM0xYsXrkKKXO-WNzQ_rVWBoU6-z4ulXyJgeq5K0C0keTrml_AYleMroKjAhlobtJW-_SqlKkFF_pSDLwh5H-7oevFHn2gu4W07HdTcQEo9lEvxE6KNDLkPKPainhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FE0fSLALm3nOFsMH_FtFAxU6gm8ERZVzO4ebLfaWOLrmLx7xqHOKYn8hoBPSCQcPNYdozAUbDAlwFOBrx1wZm2p2HKIqpnU_4uWzRuZDWg_0gXecwUIQX3C5FLaY_4yyMq8bTaCGqyUC8HUmO0XivJ-T-f0zPbRfkAJ2zIbkxnN3KkTzDrHnIkv0zCwVZQNpw5lRwkDF5mihRBbOp-79Gt1N_pmpijQ7owOfAKQIffcuRjSsNpI5bIOIIpq3LU5oR1sAMYk1ooyk0fvW--NXTC1zTUGF3fO78PNQ1EBsidFgR1a4_MxzVJNY4tfTnQO9QovTaR9IQuvkafPpSC90MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lawPNO6dVzey3SMoXIWZEbDa7XRNzqql34-8uqEabpx1O1D5UwwIUXFGi1yVrCnTFTG4c5Kiv8sj_ru8XbBubPIhfN-MC4kPDOaZpwPmZcZB5uEQyEU_zJh1Ruk8w2zpnPFVJfKHCbcRmy8cvi56HNYY62-BXJWTwDN48YqqNCnP6U1Nockicdydg_ZXTGKJgAdrn9h6gDZx_jtMjoyyVsl2Ivfjba-rTtIM089Ksv70EaN2GyNPkyDnwn5PIuYpAJnUE9-O95RMCckGYnX5aCuPhGMaJEO2IC3PgTRKH5y0PcmtBWSrvJHhI-S9KkUGeczzsU4biRPcaifaZmyQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/erAuYWnS6fEneQmNIC3WfCyzMtSRm-FF8RmEy0Hu7LGPSUUseHd-50lFdjxNyR3r56nMUx0bMcTwJG_kzh2yPbv3QOpSC40H9u5xIWXL8abUvA2cRJj8XILJuT1804msQFRgbaCbQy3M5f2iQ7uHT6cWqpIDzpliglCLYmdUWTshg4d3NBZZzQcW06Wv4N8u-1sQus7lEEnPnmmGYIIzel1QmPwXKt3S16Pb0DD9Z_w-n1CvNxGAUuNhjCtYO3DcLAQY_yRoowB9Lu6DrzPuXR8CY69sbcxdY_ORmjn3aRAmOluCKrrOefy6huojK0liPcSd8dYypEJp-cAycGHA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjz6xOKe7eHQOOvuQLNEXxafqExxpebkH9V03f-1dgs5OVeO_HPW4c_gq5f169EkBRv0F4FarUhntxIQxxPPM_ngh27jqCeJyFByvLp1Xx-2e3w7R-5IQoU9_gZOO_AnKZE0hW4ChXuMtbK_sGbXMi7LlDQbijGpJq38TC74zWjNM8sx06YrfgFPeg9yGG5bgTSyB0OiA9XyTRN03Q5DTPZHi8i1hPbzLdtlmt8Xqy1cc4yCVZS7ubabJyMolfibLGJPMEBslyjqGs2qOmFibnKVcRmqFZNmtOM7khqJhR_-yah92-EDnX0pS3bssNe6_C8eh4FOMflw_tZsL9s_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/szLPhb6tkLKBvG_MvvNsonuEXqoZ_fqQVH53vdy8htes_H_c-j2BKM_NvqJnWq4o4CP7Sc61r0BRozFa7GW5tmd7RbOsMcGLpbxpPBRCUBkdYM4NWl9kZ8wwGmc8JLmiojwrHQd9aWIeBgVhgZ8NmJDjYexxG8ehq7i1QUbeCIPlB-WpYpvyyX5MxVGzL0L6XET3xQyUVE56GCdXMJDXFKjH-WvxK3BlpexngNDp8e8U1bEFlBFtUAna5Ckaps07hR4to7C1HQam7OpH1eIiyZ-kXsZLwySm3Q8sYEYtDwKtHfgqdYb1MFilvQWsWTxRnyflNWuI537l7h5WopVKSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f15REleHsRzaIi2fM31jvSKouspmXzotkubws6FB4DbyE3dPN2SP1HJn8FtOMi4xXRpQd7Zqt7ABvxjo5OHBth5SKZaknfPCWV3JGTv6F2uIH0POF918fq0nfEiIbqCYYw4qiWAlQ_zSLc-gNkHHg75b0N7f-9_NAnhEdCXrpYM3EO1AXu1lep6LwY50dQVilh1S6mLjUuuhBlopkjtIDkLACkpjxdsef8zNA03nQtdBC986FVcZBVTqzekiJhQm4eYCNhh6uZX3aVTPIvpYNugBjG13aEf1jJ_gsufzxEHtTjoJVWqPhEm6FSLRRpCrZ66XnmVDFIJnirSIcTQ8bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o44JY2jnxlYIiaS-nOEea7jfjWJTdH2yJ7-eDS7B6THnI5zTbE37Q_yAtE571_9HwCqx-dkEUdN9BEPNZM9ZYiF4fTpSjdX8ow7yh5-Dj6P5aDgj2zAhhz6xRGqy5OCrIkmDD-KNqnSlM3GkD7BlaiMujyBZM6SRGBF7ikfleyNI6jzWuyWptAmmb-5R5bFgrTE8UMDgNfxDzLg5OSOcLLVRYv2uNWIhKhN7ONSfiVaSxDFBYUKQNI_Lv2kP4bcFanid8qUlTDbCTgfrkig-z_AX8btsgqrX2obPeSlIsltTtf-Vrzwgg_azM2x4X5wuvU7_XB7k9PXtw43Ll8qXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Co8NyPU4bu0Iw1N5NHvyg8827nazkCd3ES4f86Kc6IWNCEkv8T48uNNsPayNFLAEjLG7vnFNUt6B67laCQGNYWrttxy_1Eiyb-1KHJa0bT1jxsmxPin8wVGtwiARqTkeVghR8z0mOmpRAJ2j69sJSVRkJfhv_Wyn0_oeCuxZfTfSKQmyWJFb3MBMovSGQn7GDW-UfTUzLOt_2qpqSFg7no7DvijQ4_1RJCvU7bH3AuGhZFAPaxXe4Ew0558CDBBP9usckQxdX87VgxjFMW5UkZ_P5beJ41UYM9mHSdnQNLTiK7f1eTzA5r8MGX__jkxj-gH_p5pS3w-BKVtHCbURkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sHF-DgPvORCFNUw0pDvGyk9hoPrGYH71_jUv5dyxj5Kz29DD_SohdZrWn24_9oipZkTi63Ms9euZvViyYQ2X-GNFAMRFIe8b0vJiD6_vcMbkG9NJMvxlV-Yl_WjnsoQgGQQvyxhQb0iYJIuiOn_Cy5vO8FuJmNhvRr_tSOT5Y92W5X4o2_VlEPas8oJRDWg83UsEn8V4IbCjt2rYssd7BRhslv20vmT-CbGVZCw1KBapIdbZmWfVqjRD67K4lv8ncFkVJP1miHCQIszE10dzcQ34pS2mwDdMKOfSv3O6xILgxYOaylbnBX_xSIsBJ18O5Atst9szZwdm3QxCrmoBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ff1aQUbx54gpta2CE0LawnA-oyEdR0SIiLIBXKNVgJDvt1hMd55ZhbqQaXYb6txsR-Q5NN7kBAPwniN3MvI29SmJiRSBJwfKCbnm3ukyM2HQvZgfQe6ToLmtzom2W95iYd4JliXN-GP1FOHpWKHpPDfJW-GBkhc0f8vi8mMlvkfBSOUSSpjqB62kzArnz0GOc-Fl4wBEwwAqT8SKqLxMF5lBJeMmOhwXTY4mHykYEii65wkYnsKgwAFvUJNe7pwR9M7_pCRCJM6smZ-DtZ1D2zUPKiRRzPYxzKNshqq-5iAjOL1J-ZAj1KSEHSvmNnY-tFdTGa9zM6TjdoFGlSwOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DFmvlAVduidVuViKCOhe5nlqjBn2Xu4sXxdEhT76i1TZdlPVPpPiw1kme2udy-0kA83Vca8XP_4piMDr8dYO19li1QcYjj-RioJMIgpNI5fzuezT4zpdGpmKQDn1Tl1VvoWECsI3oUNmNfu3Z7sUelqnqcgQSn80xXK1Torg3Vv0x-iHnbBOqh9t20KqYR7hISmuk5TfmTMR6FSkMEYkYBaCfEAgM4jx03k6I4rtY463-4o0I2GvK6HmAulQNpv8gZKJsiGBaoHhkGQvIH6UeYiP4oPjcruu33BdGB7gUDwflwNqlOhGHSblYijol96_nkDA5HbPcAwpZQgqOVVwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ow-PbmsiDo8oksAvRBg4hgPwK_q-Smdh0g1OJaxSsFCDDTQrEn11r_I-Mp6tjuYxTx9R67-uj4EEeY5Ich_ZyOSso4nqDTkW2vBVISTZBEDy5G8xXqHXuqYgSz1Cqhgy-QlmYyOz6aOk-UdMGhAu9w3vtDyLuAg43NMGybkvBXb7U_46ksAkgu9Ys4qQY0htJtvU_g_pN3aH8NYWKWBi7-6dd-i1JNRJ6T40GlQvsneQ4s-8iCgRBVo3EVu_n5TCK5bVhle4xEesWB8iqkL9DBzCnU9WZj0Y0SZWPCbYN2c_0dylw0oJk-7GRdXf92gHbultVppaZIKvagV8XAeYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r3KqO962B0fJdKSWb_alVEy7c6qAnEXYZshbYYltZQN1SdP6f2CJCgsteA87Fwksq-HIQNEIBDLT2qGyKXObuZkhvrAeAz8GN7gKM46aMw_xYWVpAJSCoLA4m9P5BPvlPxwOI2nYarRekY8_-4jnjpr9dhPuz_UGk--ekDou6Y_Vc1z3lRfwUYZXiTK9DKVJW7pYtl8x5lY6Qhohor4rArtAXJhLF8ilHmnT2ebQk_ErTGMKoXDuNDwANuZUTgFkcxdzSLNxwmrdEKt4xQ9clUcfQeMrptHDevgWKRg60siBfS1gVMTx3BLcZx4FjnvKWObMk0dZlesrrwB8i51oZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAAk95xIb1og5WoPcv6ON9meaOanDb3jhMp5aucPLFVetfc7b-bLsouZ44vD8WICvGOVeLCscK21csmzYtV_l4gb2JqkPw4gecKEF4TM2iuJ0WRrrgNC5S3S5mliN4T-rMkSqqv0p6cbsc77VAOlFyMTtv3vHm0JjQe5TWgOCr3QrRb4QMQ1OdxOXmCgLrFBOH_gtFAfHIGSh57QvFWtdSWk9a0AIRom2qJFasevldsaXmssSPV-LYsYrEgsDZy3PQUYXpgxCGC82ERY80081lbCkSwu3d9EbzFK8lYTgJ_DT8D-TRTJiK60OzCE8ULsHqvFTVy44o4TNelnOeWueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZjS_ovNbTPdPtWNRtnCV-f-4UGxOJqXZ1MJdbTNj0o9eX81vQJFOOHRc93SER1I6ercxfQi4tzToFHboYAbzeUDo6Rnt3S4FyKqX8GF8BGvtk_54DsAyk4CzILvRF9R_C7k7Lh48wwA486dt1Dbu8m6MTnt6odGf8wKknGFKG4_2Jr-R1Z7gf3HmbQyyyvON_G05xSocjhPg77XPlfJvZZXVbkUimYQF0IYsE9aJpFhIgWKv9bNJ-IhpxZMrzH-rvoFEqCkW2gHwOl9zg-V4dspUOHOa_aePd8h9y-2__v3oI_jY3l4n06GqzWd6BealJBAxIpq2YshrrzIP7W4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dYte6nLNpgFwS_RzkWm91YfcW232Ffs8xI6Sh_YanFsvlnuS9M1MwZmGgI10NhznxS2EQihp77DESj1oTVKtXPLvFvFuYz_3rqb8oB31ROIiFkncZV0LIZszJ-53aAB6DUCrymP34Tpl3oAv0lESSHkW4nXMU0C6IBOEUesjHA36XMa629fanSi2mG8WGHaZ3gvJmcqJbrL18WYCGdjjRbmLrsVmP50JZxjAv5f-fo8jS112s5Nc-3SdXROYWXohPHUMBAe6-5eiRFSMT7TbrESHF0x2VowrjJMbu1fwINQIgMkv4coOjDcJqa2O1a8tvugxGtBhnUF1nDJLtSMwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNuVnb59y56fzs_zXrxuTHyFReDtpW9DfU3ciCCeVJxcN-zCyV8f-eE_t14bMGSkpTvHhKT-ZqlqnF3VFXgXfU1PmktezpdXrLWhK4c9GT0xhJ2pkO_7_nF6PrzkXaqSnzh9YNj5NrIfX_EVC4nNInR-heitfDe0EG-IuSIc1voDQIXhRO8DUDqwBji8BsHlYboJivG0w2j-Zf_ZjuC-tQzJTl-7TiMruunZ8qYTyNrugyeWIjt3qd1_hdhlmAljiAPll-UVsKSMXgZklzSRs1G2OPOzbZeq6Y8yXsCu7sT_qoDReXsCYZVaUPQxqb0dNcfybXW3tn8u4MIFV8wRfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HeNPjBfQujSCqmFKQ2M8a4kMQsWZjpm6lOyRFq0QTeMekKWJ0l_qc9ORrI3Kh8JiHPLBFmhjmR3H_kAfRl4M-bVu9gUFCCUFZAJfEyizZZ0ifN9UvLmOrt4mE46PFaj3LvyyNyu0ZnyAdCWKVjw6doitJEFYGoqpcvpfHLNrVmPHi3cEmSpb8XmT36rBFAvaeRk132fMFmzRIpz6A5_dwBDJ5eRbG_PsKW2B_y-t0BS0xoDJ-m1IPvlwGYpWaW-POs1HUxQj5TQtfiePeYV80BoPkgH0ZaccZ1ro8NcFl5MH5n52c2IE-yi-jPDFrS_yD7X--VaDR9fyjlP9_H0DqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XrL9ASkxUMXm3fDRGKArrikAztBsTM_KfXoXnC9MVWz8ReAV7zGS7CmSZyadNwGGkcB8SGdt13oq6212tP27Pk90uvfg661MKBvTODCFtGcvU3OWlYGqKOKyAGRt1CwhfwZptfyjB-HegLrZGhecWOYnANWY3seeIcEZc8Fgpo6qZjSN3aSxNxPRTOBb9aIy6YtJ89pmG-T4n0ymVWjuiZ4Cnd9CicdCb3Pfa2HTH3d7gs4U8dmVDGUodqsORbEkuUMvyNxnjvyfg8v-dJt5SzD_5rcxzdR0chbGYAqrTa_oHDzO1jgiDgi9IABBtbkD5fMMwvoWp8AAU3NaOZ8slw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/idSVqJixr4uR-KYPx8vnq6D08NhUfoH6UwsT8zG64kE3IQCbIGU9DUF3vweV5WrEYweiUeB_HE4Wdh7h3za5tEYV-qGGG93t7otk8O7We_49fMXMhU6KMLxI-2tIE-5bPdF4HJkL-NPjK-PqdxFvIhn8DQvgUzjRihcUiDxyeSrtiZ0hjQwm0k0T6U-bBB8QJh0tCvPXtUPk8u6icFMDxVR_YzDfVJSDvKOccOGPURjx_Cm0ugdBVbtPuhYWJQg3ncXegJDzSAJ6Xd84RgOpDSvlC5TpYn-GRBW0fUzg1qbVbq8A4nlc9BD1bz6GZLFCE1olxcy0xyqZJyWWCwX-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=lelELq_nyUVZQyZnH93nFYtv9XtQhK36arZGRrnPF8fTQYBMRHrsxZSYnzvT_B8RkpwgPGRAT4r0Yb4VavICITLKkjmI545ZnmFIi9KAAN-KBE7QX9rAkv4h_-Hr3_MbB7pAIkW_6yZiYJSnY8SjC_Hpi5xkUWlNRCUuF3c-zfyv24jV7LzAA_nUEQGOG7bsBJXGFAltmPXlFj1t44CqCppgWxHzbsVgo4_nk8XhdMixJtxJtPrR7K2_wFaphcSBJJUxnzjRxtntGdXkLuPRhqmYzSeKzg9esRO310Ug7ddgOOcPa4xuPJqKnjvvD4F7cGok2qknhUiVD9l81Exgow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=lelELq_nyUVZQyZnH93nFYtv9XtQhK36arZGRrnPF8fTQYBMRHrsxZSYnzvT_B8RkpwgPGRAT4r0Yb4VavICITLKkjmI545ZnmFIi9KAAN-KBE7QX9rAkv4h_-Hr3_MbB7pAIkW_6yZiYJSnY8SjC_Hpi5xkUWlNRCUuF3c-zfyv24jV7LzAA_nUEQGOG7bsBJXGFAltmPXlFj1t44CqCppgWxHzbsVgo4_nk8XhdMixJtxJtPrR7K2_wFaphcSBJJUxnzjRxtntGdXkLuPRhqmYzSeKzg9esRO310Ug7ddgOOcPa4xuPJqKnjvvD4F7cGok2qknhUiVD9l81Exgow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3FseFcdYC46gBBxQr6-8Rb4m-3KDeiY3LcYn_7GpWdSiyrc3QxrnXMdDQBjotj85cQOO8coImPycTFKoMiCcqwNLSPUUfqW29_1OqGBe97XRArj9Y1DoPDwJZHRzwbG5iKcn0ly97pKOzRyTkvxDdkCM6z-lP14MUwJHRRtDEDgEtj_NzA47meRJwJ3T_2fhnxx8a-r63A7isyncTM4EpykjOmK9mNs5ITLikqaDsLJfc0vDNuQC-up9ApZsG3RO-G5ATevrQlDt0-d5KEWpR-MzkxI6UvxKzzfuHnpGHEc0WXyqxywnQXt8adU9wnqKRRmuoskPUomwAboqPOzmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c8Awsbqf3SKpgD8AJjRxL1AChlkt8p3dPiiRgrrnKMAvUPBNlWW_yeLv2XRmRvJzXObN8FBO2-LK4SfhBiLc-09uIeo05US1tFr33hr1ek9uPbh_DU66BBYzVK_eC8e3RnlW0KhMsXTYPEiyzALUwCzfaIdJMwzmfcUzMWWpMpyakhrNyWCf2MI7sdwUj_OvYyXH-BLqRbIxOuPxkJyIXYsjl8xnls1Fcby6ayFGA4o6JNXgbC4sqc6sr1TfuFTMI9BscXPrJQBUtGyqr1B_edIzGA4evvr5VIAC-MyNV1RknahC42ky0z8eqbMHVNz9cGRm62pGja2tC6ilofFC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cP9wCmYcefvGqp5VVuGB-b1x5ZLB7dui8BPvHr8LQVtOPw2gu88xiFXU-W83aVbB545p15S3fKsfwVElI99dn4N2dFKHH4e-p9knzwsUGcqsRAMA2VVl0Hroa5YuQz-ugWzKNLeNOmI32srCYvFkHpB1c3lVyF0g-xnHYhAUKx15k9gsRzutvAYW0AxMqLGY4uA8UsCSQxa321pQKTfyBLYZF33wOzwOOUrpdcLNtOXu-IZZoodGKKewRHcNPmS58Sy74s_3khAkewMv_ay5tIYL1WWfnj41xzYZZgKbouF18axJlNfYpqFPSI8B2tAb6X_m_wVulV51u-5hmCYnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P6oKYy3ZNjB19nTFFHRJ5dk_5ia3NaYOf11JlSAbGutwm7tAoToAPPuJup2C4ihS37YYzvaduJ80E4q2I7chgv1dHThtPnFBbao4PSJoB520Mkre9qBDxlHVYSTEtlGp-woBBBrEaFRWsWqHws6Ahql8DzZeJLmygmxmw94MV0uzkpfgkFnd8P4xKIs2o5QFdTH95Qzrk_AF2aBbGtQMLY0vp4uoQ4wsbeGgTxtH7mw5JnSiNJM--UyiV9OI1kgWcVyZvcUG1Oyu1yceaaaUP55Dh7XwUTLnmkMv_9rSl_VAQSAN4miUBSJTC5BUl63dBSikpLnFp6nNibPlPN1UAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUq5L2Kjksn02bc7hhDy8RPgSc0dv2hAC3so39tNt6hlp4UU4NFKrDkB211T3OPmOELQx62j_c9q3Ssyw_dpRMitlN7NcMj0buli6XwqFiQbXdwARRjzfclKQbtvHggFQg6MTWqWRsnof3_OeOpPQYg0bP0f5996Set4uDs1-fLkjhyjWpM7Kp8lsC-0OZD9eqfFNs-kr8BbVocrdVUacKgLLxBKGbw3RWmsm43JeduH76_OtdA3VPxziRS-VxfrYq8Zn6ZcALqcQ7wZRcc5iWtiUGdaWyyD4uwrm0VOap80mjHud9SvKb9GGRbpZi8XoWowpn8lvYPh-x0MedIbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XRX01nTCFpFI1WJqVIy6yGy55sidOZSt5oIpL3wH4JVJ_CQYp8IUPVHnDboKCpIWKH-9gU-EA0hPreMyW6e8yypU_qRoINLjt3L06xjoXaO19jZ7aqVbl1LfBTPSpScrXaARimu_rMmwP8vitYcoAy3Wa8WkCgPN0aoZ4B5zcIvdiCwKdeWkMpMDsuDX4EzaOyTz7xnTvNA88Y-pgxvZla6e6OChGVXHr84srv7hjspgq4Cm2NgSsNCTF1f5XuniaVVpLgA76XFXzFu4AyEN0K8i8OUc1Nyq4541Jk0RUCji8UdvbH8i2yjzegA7tyMyZwrs11iSwviUQ9nbkczokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PVzPss4t7aIr_aBJokKNXyy-qLhAgZNhgVvbvLX3nkjjqU6UWUFlpDqUN8vkzZGVeu5bgjGNkwFy-k50YGBlwoOWH0npn9EkLtavgIc2yFd8cVk4weW7-XQ_G6mGiK4Z_LCoWE0Y1VNmFCh8FsFWT2MfCiFHz2-eItjT4bcT-stQ6KzkwbRZkNGinY8PVkDHnfGMs3GGDS4or46b-XhBqPWiCEXrBRuePgjSCtztinEujGVQNW0n4gbgYAUIFl037zRJ32S7TmpEpjFcF8Gi2PuI7ftDCTvMVFPkfvAKUjH0KOOrob85myrRRha6Z5CesDTw44cGEWAEtJVoKcUTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WSNdPG3186u1rg-EOYJiug4HFInTuAtc9x-2xGL7q7eB5CO-EMNfdmJXAwbSfiO86xIVaY4A4qn_oJh-bo-wNOFYyxT2I6AayrhKBKTjF_i59F-Pijjha_jCxx6AmHfLiTNfjoYBZlI6LaYnDEmmG2Trvaqk-RwLzOfF3GZ_QyIiqMNKLSMRaIlPGyl4mK1pJX19WSDAt947Vr9Wt1KHRtk8_P1GaN5xD_NoxhjtFVaXje9_xO44dk0Zm25r_hGJ_2LVDqQDvH3jfawDjzBbvHZ2C87QBFVNc3yFUFAieOS1WyRMYy_4WOXj5n2pWN-txNxgpX6-whPpwSqi6gBRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pvmRe4NGdApvJJLvZMSH3crZQxsokg_N8uIDLdTK4Hybrk-fpEvqr8uWspeB-bcwIZpVMzgbMESVKIXCT2wdm6NHLUPx8jxvPhGWnYWTDA29ku6Ab0kOJgMQQjnX90kRBMQGx7GzPPnRGV2O6IogF_K9vonQto5Z0pgLEvrWCW794zrgKMItNZPqmSlmrqvu0756u27IUFfTvTgbSU2BbKHQ0QdLN1XbujmRZhYuKogaqvcHOswUpPYIFV-5tiSWJBqBJAXpjDO3C257VzLQMWNWbzWP5crYZ4Uj4x4-gIPSP552vVCCqO7lwBmaffQr3wzsB5P3VyIEiU3ZQYpaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJysn_Kk_j6BnwxZyX7cTIdypiNXAFIhpm05_fLEaBjUNl5XIWU9FzxCzWWi3ubQdM4Yn1ftoGzxDcIdpJH8T0VONA6EnkOEJ3uEeOR65xJn_ByU4el7awimXJxqRg5H5jQcvttaJpZQj8lTMowCDmNW22CKy2bY5ml5z2Zg29ILAHiGqUAu8wKCf1pZujbaN0ddtM4KqvVpu4L8Xc3K3yQDzhCrAVQTiqccFgCfUdze5V9wY1u_JUUlOg6xzosoNT1-Pjep8EEbiIlhouYTBVquZ2Be50CfD6P-5a8JJxjpNtqFewMXn20EtfFfGgKqkzdcL7mxqFIlYsgt40Fgxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vBLVq24YyBvTke5nmRcjMSktwtz7VchnYw0kwTZkO_jG3ookuEzhkNzeDQmvN7QWcgwvB-5jto8L9dgSoQJ5APqinx-G816MAbgIUnClJoTf_z2fBCnOI9uaMFP7m66tB5of1A5LR-D1JJcDaV9Kc0xF_RllGAnqs8rYr_WbAjCRx9y51IcbOLOJWYducvBFukp8QQRycSs_5-RD8vr7wpV11VVqqA6M_fGcobvvJ718lIOKqf1jVdZs_M8W3MWEMHQt17ZDcd24HPA2D12k9VbAd9rRsf4LOVhEh0lXjtoAcol0gwLXBwrVjI55bksUDqrmKrwC-NAt9pYf9hgxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3qFRwRf804iQTYdmjtuPc1A1mvTUsNfbjMtVLXAW8NHdsiamHKLZfN8jZ8H-RbzQeTNn41_Xmvq4KsUPyqFX2CJvImDZKZ8QoYZEhHegSpMivuTIahdu0jUm11TJIXUsHfty08He7tYbPc42MWpawOl-nhTYSVY92MzDHoGe6xgo-5OKhwNbo4h1kOTAV1MiYWGsKQ2GrnmBM4TrF3UM5_VimovVc--YVLOFV8GxcLHum5oJE44Lgl1hvjc5Lc7oZ52hkCQs0YlfvZlL--AQvv0OxGhhf6w7UgTYjIzGh4L3-w_hnEgHlsH4H3repSQfCKp3lpBj5vWUCER6dtIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_Yv6qe6k0GG9QLEjPmJRwTacNX_IawuY4PxEuImZl3X-hty3FYde930JOZmDpU1S2kKO4eJGi7nuFbHjwzxqMgDWOD9ny8sIIr_DwfyTcErmxCGq3bbx0lhhNAnTbpicmMopibsmt3EW5HA7sLA1Y_M6KqluszwhpJCLNIw5bYtLCldBM8xqhXwIjXY_B_rhsembSoP18n8tPkZa8qGV1EIMGuqJU298qDk7b4W77LKMac9Nof_ZxYC6M3C5bUVCbX2DTUJcG6uLa71ZVr9tV5YO_hYPmWV_g15T_zXaGB5DDKf75ueVmJUG1bLsj3ZRdDA4sd-C2UQ0of1pHJPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IoDI_3qaPtRt2Higz62dZcKcfkxYtbD6L-O8EL1X4N1S10JQZmmGGepy3GNb39-29H6gjkJ5q4qjO2c-KYGT3p8zoNSZa-_vnFB-6nckaPuxXFMdIKPs_K7heGN0Ufnp2vScqJSsma1glIHb0J9E7wxD3M5lx-psXe4buo5y0x1vJBmegBUYO8lpYmPCM4vhn9YkWBNs0Rvwhcdx1GuA-gAi-5jVUQB5BaZAkgW0Y6FtNOMFiiOP8r6tOs7s9ArrpvX4lKUAW0kG7f3NEHEh65I8JbJQ6gi6zJhIS2_eCfV4A2MXvqX8mNjlIqsyA8HeyWcHoSTMch46r3MEvrOYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
