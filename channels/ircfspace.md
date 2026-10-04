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
<img src="https://cdn1.telesco.pe/file/LYtSTWkTkC9sRkIxmGlfcZvh3CtBKE36B7k_Fb7MGWjZP2r-645sp1UPQ5t_oPNTp0nZ2a95Ypo_W_t3EG1Zbe38bgogov9i_ZLbdTDhq2nPk_-qJtWBv3rTF5io3XQNBNQTHhgDznb6RsO5j4ZTcv6koL3WxvmAeoHwByfrl6Ruw808q9TMTuz5sWlMyNMBxun_B6ygwGeFlSG_i7zb4e9ZaUF7j9ldiv6D7KiTUdu2tAfXHrXPPzMfObf4EP8spOOstTrWgfMO6HYynoami6-QmfEMWeaeDyRVlCGX6myg3VmfdmZkiPTmMUiYw5jv8frftAQExXcLerwdP1mA1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YXPZn5p0yDoM9OYzfZn9zKPMz9FLlpE1FQGyTWFki6hqI1O1BaFDNLdJvVCLNm02zUWGH-jHFWjmIIpy3SWDga31qUKOH5Oz5dybCSssrl4WIo_8Trui9YawAJvSSKbKHmDTygPThtZ9dEw1W1_uog_35u7-cC6LNun0evDo2R9GhcNYmHhpDn00WYwmIysjNwLM_a0MycypFu09oqsPbP47wanunuiAFK_WJOW2Xoggq9X4RcbZVZ0cXyPjvEojqFgpT9A5HH9MzWkC497qrNHw4oILNJRCyY_vzZXdiALp-NxJEPwZZppsR4f41QDTexubgt_VoxavkK2uN95KVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۸ از فیلترشکن اندرویدی MahsaNG منتشر شده و توی این نسخه هسته Xray مهسا آپدیت شده و پشتیبانی از پروتکل MASQUE رو اضافه کردن.
برای وایرگارد و مسک حالا یک اسکنر IP اختصاصی در دسترسه که از نویز و پورت پشتیبانی می‌کنه و میشه کانفیگ‌های این دو پروتکل رو با کلید Auto ساخت. امکان بکاپ از کانفیگ‌های شخصی، صفحه پروکسی تلگرام برای کپی و تست سریع پروکسی‌ها و بهبود Fragment و حالت Auto هم اضافه شدن.
چند نویز جدید برای عبور از فیلترینگ UDP، کانفیگ‌های جدید یوتیوب و پشتیبانی از Cipher Suite برای افزایش سرعت آپلود در متدهای پترنیها به این نسخه اضافه شده. FinalMask حالا روی پروتکل‌های جدید MASQUE و Hysteria در دسترسه و علاوه بر رفع یک سری از مشکلات، ابزار زنجیره‌ساز کانفیگ هم از Fragment، Hysteria و MASQUE پشتیبانی می‌کنه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZW-91koKxVULKG_lpXLo7DZ9jF2dZROK0Hoon2lhOgYNS4Br6_N9UlvLODILWqcU_Ib7tp6-vXI8N1zjkKAJV7z8Qis0xEWSG3hs2yl44ekkb-5ZvNdJWl8P0xwrsz9UlDh2SZT0kiB5HUwCRFLSQEn4z9NdFdRp0q93cm23RojsVVlxewp5n1Ui0818vSPmkjtjanSc5JADktJytMYArhz-uHiy6sP3GIkIWN7RPsnVIU_qRI27cIbHe_yoKLamZCsorX2BBZiqxC9fq8zb7YhqtteKNdvf7CRL5Makc1TuoLzsV8WEnrcx_iwnBMugii_WJJba0LkSEV057pRmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UP4eAPyfW0O2FenrRFY0bCp6ITsTVTj6Z5iyMsPCiyw_U8Qa8hr6uSazD93-wohquf8civzdWYfxBZ65l0hWJEMtaTHAdT5ErqinD1PSbYgoS9ietV23DcojDtPlOl0QC-9fF2g8_K4ew4HH6ejK0C-rqHCaxFGvAm_BTn5XkFsxiLT8DORqiw2Y5QF4aFaE49G8wCJyqvpxZMwVdbDb13i6KvtcOE70-kF58FfKMBtrIEVz6lDQKLUz6J_FPB90I_wufOiukMjuET9XURJVqvLvDHC2DRCgL2SRaS2BMmG60MpR21_NosiR3zXi2tSRw62Ebc9AEThiXnusaN87-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5QgAvcDYfx1UGP6sHuJg8o2cJxYp-CYfBiNMJjC5c1mf-ch0r8DpHrY6BGnI7d4sExm6QU1RohLE33jTfDxEiOoNucN3wL4FWYP3Z7x4TYK-7bI4DgC1Dor9avoIGy2Iy5XM17IMMGZmIaPCa4QpoTf5dr-cDcGSJPQVY4EQeCxj-lFFf-e17HF54W3qfarytlrqWpJBVV_OlFJy5yt3jZ-pLxrfrUE3r02TfOc8BDeZJSJRpyVUW-i0fBmOanMUddzVGkEG6fKltd_eZfZTDhs98mvR7aNEmzaDfRxvKjdKl_1TuYX8RrT_8RFBcLIkQOPgg99Tyt4ALoZ9vXXPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-KBmnxR5MyyAzIBj914YdX4aYSWy081bwHMq2SLSyqiqXRVPr46lgqpgUEPjGpCWzUwh_4093s0RgFjmaN8nvu-VKfoSwX0DmHqmeLTRHQ4qN1tS-LlHW-P_yX-vQcsaoRarQn7_b1HpFQi1I2hzDlOBpfquJzKPxQ3LRhXE_4Dfved_AQxSCBScyFNPWDzEG7rO-6rUlIMMj2zlclzoGzACPxexkRf_Pa4oglG4SCWToRwO-Uc1opHLp6kuIcgqgQBlFH1tVGIv4M1gGaVQP5rZT20RBXTB_y7_7W8EiZNV2uSsslygz3IS09Sufa7mD03KgR8wDdyTYpYeKO26A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vjHnfc98S87vH7vmgqeZXywvV4lGawltvK3SgCaIuAwiXoopqUHI1Tui29YyqfnXYCUrmWn70CMyx0nnNHizYueoXuyOC8AbwU87Ede_Tmp8czOOLIVVyA43LgAG4_jbBfYmsd6mQXPmW-ElPR-HWzjDvv3hZR2B8Eb1Pv8f3ZGs_4dpjHYdwLFXayorvFoYFgHzy4LgeRH-M8GiWR0ITARRPrIoKtsn8GtwOGWtfC9HERhacfYxeQbwZKp7xGaoZtNBwTxMkSacNmN1j-ptLAe8y4XLbYFDqmkC7RebFaCHi3oiJr7HtGcQnwp1lo3WYIvzyZ0X0uvfjXUf62MBxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gaydQtU5pwUvSJWjI32RAfZRXrMWmkTaaYuY1adwdW_oLhX1Ik8MjdA3gabjuZjfJnMySyKa-O03QuwiZ-IYNeXUbPlO23d6wIvGh0ECzze4rjUc8Wt7jJtwG_6qWtvbQnce_PyytuuGqGLSNJblwsDzoWT7fo0HM13fGJrY0M5CeFSr-5i0ETSv55choZCee_gKgck9wnBeFHxdjt3Bi5rrt5PmDmX1I-uggh9EMY6upGiVdxMk3CC5EhBTnK3SdlNKzPqNl3oauw7qlQsfYmnxRTtEx8pzFuioJIfDXLfHDrtLRKtMCmcwcNzNJwxPZUmRIfg4-8Rk7ERuQwHBcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HFqzneMzPpzh28nMunquj0PfJ7ZWQMO39Y9fDxFKo-aLrFltptltiflk4v3Yir_TR04pzbTgJ_nAFlw9sdgTu7BcaJa12a--FHmmsnGp1CLwl80kJ_97eu6i66Fex1yw-CRSws_KdHF7mo2QipSHQKdc_Ro1HXLWjpDg0MAVaSysUmt4e-bw3EEUfzTCYPV89C43wywS2zkE_AX6oUg9FQZuKsZ7MZC6ZjInZpm1F_pYqdu1AJmffZ7wWuCNnRqOCNQvh4zyCfcH7YhjWEqKF98qjD5A10lq0vNPJUygS14tvY3vkNhqrQr7D57O0rk8zZpfF5Lz4o5FaXmCWuUnuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C74WHE1mtx883uHfFIGPABxi0SEq7Wy79nKQtfAzP00yGS-9QRqlGypWvikmWshPbgKwEGDnJmuSabqADcJd3R0LK-wTfyjJZ-ZlNh1ESMrIqiqQRAo71-5DvyuWqgu4SMiy8V8XcO1_tRF9WDi58nNQ-fPiFdaTxN9iu0go9ayqPRgFWbdiZjF_2ZZgR4YBAL9y2ma3lElPgiAlIrWfVeRwJq_nzAT5fkLvT0VO_c_D9hYds6lh3j_JfVOkdjRz3PBWrwmqE8un0155glhRzsYd87EXEhy8sURvrUa-AA2RLfazMAlljajVzATKVplTwDG3Aho2fD8jysMWFtPmVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxV9Yd5RKhUCwq9D9uOl8YzPBoqB3jyUjG-W7wywQI6bq9jE6CRksxlIZI0cNue2F5-L9i89XQbA1Xqou2Iz-fNTXQ6jjg440_LdtCBxO8ObQwMOI4orBFJGNePZj9OeGQEpaCXl_VsOC2KatCV87W2XW41u3_sr_rD6g8Lk2C4mAKAqaLQOCpBOoeKs-rWvm0VlxjtPouUFzaJSVeJix7f5GRPhEjGbzpjtPAob_qxmjw3T8UJgbWEdq2RmD6FLO7ONA3g_v7xa4WVcqiWoTl00coc96KwDJb00bt7tkEcjZsYvPnayHgpd4z66B_uB17ZHRnOL-JOJB2_ZHhzHAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cC64uz2uJXFEH5Fp3DBrBcdW8IUcTZS0BACGaL2dmNofCm3W-oFnQItxTdaM-NRsz177f4ypzfgka1m5VljSSMjYO-T3EhwwSFndy2aHng-iMWecBRgr4AAPD9zsoYqMy-wZdzHgqbXB04P8CGadcyPhEzsBnrAaVnA70ZIaTaE48MBtnbyC5f1mAgLxs0NurpwRZ-1riTm76L1TJRwIQ1yR-3AOn3DKKm7ZTPp8nOJR5ng4H86GF7KOSIbb_5FDf0_x1VUKpOtIOGGh-XwHGp4UCOSaankiozy7i21RYMc9NfE-VvHKRvhwDpgfYbvPW8s-yGZamOMlBLUCZuvqyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UiYX4L9U7EkjhxRS6bp8ML7uDcGx1fark1-eM4TAInx5z2f2_Bj2yrU5ZezdOh_XqzvFp7F4ldKgDukmon4Ap9v30pEwGoWr5DCMDMhGI2QZ0CIOsuSVB-bYMUbblPtimlUYB9x6kyHu_gDHl1C-h6Er7dFzccyp-3RO8y-PT1tD1G2jbPdmLFMO7RtuOeIXMinWA7AS88G3hlJZfoNCuyMKa3h8OznC_DmIcEOLI3nQBbnwj-yZxcDSfoP0LOapReCRT3Rhb_UMynhwNSsMh_U_--WWkoeuLl7rRpNUHzaoP8Ti4vDxI3e8RFFeGGyz32ZEreeA_w374x4LYNVDIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XwomiCvLOktXbGBvvBitMD1bwOrFh5VqsOTGEqMKnnIaW1Xhmov5MTSF3yHpQeXgw4-SlC7YBjj1IbfdHWXZxU25vJUTD9faWpWlje7gXWVuJVEW1sn3o0BE6K3EZakCii545s3Tzrb7wwMttg0wPUD3nTMjjEFlx4z9JoCNrz308SbNbWuKV7Lh5irI7pV1bWfowSRHOPSBfoUulH3u7B5uI0sOc93quK0komMoodDoxYtJYNM6lVojzIzJJEXGkHsAxFOZ0eJkaSBp9csk51hE_nNEY_a5PB2l6nghiRVL_zesQmuUh4mzSZBTb8rejegXPlNjLVHjQ5G4TJhIvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QwrYjMiWIOwnyoO5knI-DLIUwNZUcW2WPZHe-3pl49SDa7A5xilyVE76_WXqZduWBIcdTtwHxb7Df6bKH1TeAB7alghb0xEhyWvY9wggTM1ri01Njl7oEp0qhuTPOqPzWVBE4uDbgXzY9HS-rgvsNCVJ8pjolWfm5Upv0uJBaOacWxNwfnT5wmskomEr9ztg1o38-hUioxMn4z_oSORMQa--dNJ58eGNTgWmoEreJyvThyngiH7J7PeGrtrvw0Bc7wEi95gNSdf52bOkP1bIeBoMr9MBK2nAk0vYtNonA_otuGeJAjib9U5Ss3EfW7KuKInjj6ZRoL2WR1_soL1ihA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sEGQ7QTr8Pkk4h7Gu0SLjjv6ZJwnScaEwSduL-NZXpY-hjkrLOBe0iYp_wue60pWzT4MD3FOusCAyCZUHC0UmZNFSJ272aYLqcaWP1oemqoL7bpFPMY4uw7hKMujdJplwe9ToluArB7UXDEgROZBrEUOBe0NlXiJdvfiToIb05JVANFsQo58X6SqYyLqxzFTzH54w_0Dp3iPTqykLYVZ4SmSe2SMmn_XxnDG3jj1O3uzEBur_gYqefHReOLWzQhY4XSYMUowYitzuav4Gcjk3nHsZdH8Xv3G7EZZP55lj8gwftj2v6uXFrUhsslMsmHdiEZLtQD1VtazRkVHw1p0qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQArgua2fhMYWNXTogM0cK3Ne6NIGX0dsKF8pvyR0t0yhHMzlmx9ZHaYymY25OrETtvHF3z2ovkpBFG8uzijgmWsxTfcZrON15nH5pggd6Q9tX91VLPW_wjZzXqpvZWxb2IyCd_sVy-H_aUwVyR0vmNFsgiALVKc6G-tGOjhBtkhCLO6O58nbvw3XHAu5rHRurWAyRNog8JEgNeY434JEEkpcDh9_a__JRG4tFVk619V8dHLT9IHhCAjhysgR5PiRB2TfvXHbbnStzrh2Y9YfACDwafqr0x8oomoDMaJaoptN4vf121O8j4YcXFM_QeOeMe9J84R9HslUn7DB4n5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T7A6-wRNJclfN3YFSxlXxdHY6hxPhVp8ggVPIhlM5YJ2Virp539fJDCwNw1jWOXhe2BnZi3jjraEhtgSgUCltZ3LIXfPFEHnqIf7-iogpj8ZXA4sap_HzW79L3_xJtuN46TtXDu6c0VsP9iXmrlB2yXk3jIdixmOr9FswO8sGslQxWITJ_pBu2pPon6Ehj9qTMuXArJND-cagSQ4eDlxWB_GeGF9_qjHuOrPEz7YmdOxcgcbuMm-Uzj1Gbp_hk0dp7GrHqK1R-cRDH-dwYiZbQ_gvqdHmHnwEi7OggVKRWP-i_JluvYJYq6K3GKE0wSs0Plcegqww15ZO8hJrwNNsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lUmN76WhkDcgFjuYpF9SonnatQhXRI2Q3r1YBs4tpq9DCVnGVq5mVoPsqc6CeTgs2HIX7OPw6gTxcwH_HRJx_9V8hoHqynDU9p1ghXiqv1HVGkCn620gmEjby4zJIhoKNdVPUHLRWkg2VGqn2o8ZUr3rCs66qAbWpUZRP8A---ZwtjqZYUEtGRQUHIApSuRg2Nb7iqIy7e2kF-2nWxBK4ZuGGemoWlDnYjAHGOZ25qs2-hbKTAq5eSfASMN2orKNEttRElRtvn4-CYKTFU00HuRKLJkGNwDuUZDy2VzuI5iI9_mNtRKQxd_7o07kgIXZL4eyfxJpOZ5FbHjkkgQ0IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ji0YjlDOtLjP3SlkjArcP7oD4Kv1GY14qoOSZTkjoAi6Em2b3KkV1_gj6r52AwqN0N9-_d-Ok28ymqc8C0o-xXGNwU1PGFuTOCPWltp49GR6lijyZvAqA9geoiJLOW5YJoE5Onl0XAX2z6MkAwPswVfITk-ZeW1EVfAj4uW6AVB9Y3Dl8OMB8Zt1A-m2rPiWLB9pYp8IC6bkUWdmarwpcqJ04idbdnSkgVSD7nCI0-Zz5mcz4p2a8AdB32g_KW31Qqz7iwJH9NBRafmP66MAREZzm5RW51nhzFLybRdpQD8Bs4GcT7zC_0eRgGULCbLck7xH-R-QZBJX3t3fADlhtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tAPhV2dwZ0WU5PSHVSjFevLEXLi1wnjHZutIz1hhKwUdtfHcZ7VBGofdqp5RuMeqe6TLsF_T5XcKhmFhKAB2aHi3oey4vGSt6gTWALrWHHTe6hg8tU2NYQQI6Z9TrlRZgU3dhkZwP-2Cjhs8d5cRhpnv_XPdzi-D5bnRnBZ19oQeCj5Ibj7suEbqmm1eJsNjnFLD0a63XcSPsNKwhMCPwecLv5YRcjmefZi36RMZ7Ov77rPfsj-PBRtOVceEAuYaV9Dl7nHg43AbMIOgvezreGNf7PLGB4exT2w73bHprKuAyethH8Oz0gTdPf83MAHs0TwE-56nmHmPeGfxgj4ceQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 86K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuuViyHAlC-8_PdN43_adosOmXkBa94WkzTKhGWNLaouBw3b1U2jxzTWSotAVm8tBMJUCPV3FcNMAFt5s8Zex66mImSL7foJUGbF_Uc1Zv8laWlT-Qtyy_w_RjDUj2rjjAmJTov_ZC9Xxi1qpksaxQ_cvY4JZ6-uY2FoyRfO4hKeCcaexhUG3hxBRs15uEAk14yyQGF-OVbIK1OdMPt_kCC-rGi4DSxQZlUu-DYZUuIOwuGx0xVXn2zsA61vI5sE70CwFTikRxsAfy5hC03K75JGRb2MX6CFwxejlWfw7ihUAuZCqRBk893jMLzAiD_3M18FufS5ZXbjpjv_IQCeXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IuAkDiPOINxXu65KEcbTSwA5pGNfqGuVX8JIb9D1bX0wdnkQYIZuqXcXMg4YIgE_XSxBVVG14I7obeyOs7MBGUCeX4oqwUmicw8iE2X5dRLjdtdP7D7tJQrN0k9aM-LfmMoZ1KJA8SyVFhcAwDcH15b6KmBjQSIRy40mDps3zzKyIWg6c9twwdjbJuidN-SCgBxE5fThLJi6pObXmugYYi1RsEGhfkUPgNqI2yF54GAxd-SgFQPWpWEKWxZa7YV0qx_a9P5do_6RRjJCOoGKGUoAxWZAngitjeBeD9KLrl-6x2Shf2hHT3SVBrrilFj4bz9qonrqxGdUAtbrwcEe9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A34k2iVhl-ps2ZrIqY8ArOEbp4kQpSPafAdwtsQSRR-vARv5STUHAGSDqEaE_0ytT5B9uU1y3_2jlR7-wxbKRJpWLbgxRyQ-lKIr5_EWaBcvsv7A_2PEnyLaVlTLfUdik-AJoefPulnXXnoVrunhGGtuUhc9cvYqBfJU3Klva96-rIUQ_4_36oC_Z_QnER_YnzbbkjvVHDXYulAD0dMXO9zl8AjNTXbFeoe4N2EHXpW70AmNsM1EBbVWbgWtQbSTvx4TstlfMJuMjUXPft5gOz3gNuWHZN9Uv4dKtpbFW861cEgN9K1D53IrBnZ5vFJEsQIGB47cwbj3wvJ3oLyIUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkXPfSgfM2Dm9BOS-1rTD3bPzRp8j5BMD70Xl5rYaVISxRPVcedY93C9RpFjTKI1140qWEKgGaALCYl3pKg_3pBvtQkpOtwSiKVNjDr8QKYZImGKy3MF9FZmjax1NiujD1O5sOrDdnxCATaWZ464sW097zPNXmR9XcxMmNRIHQQLLl6c6q8DEwkIxnTsl0TIgk6R0nDHHo_58AKfud6-WOUY-1x1zXhlkI0DKKYIZ7AXfG2Hs183d2VvudxPYqS5HvLfXsYhEI0up7PoUI5EYh5_cxUbmz7Sxe7bsFlqtmHnuZhFssl67PTNIwwGE8HUzdK6q6uZPuevos8DB2gcIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nm9NIQ5DBboeWWJk_dZaZj1vE-qBll0ja3wsQbGvFY__Z13MWNf3Xv2Uzb5gU61KM0U9xAfcws34YPH5sNCeBYP9pMDRjNt5WKKRHcHl7sOYt5UbIPAmfe10ihy4wLRFMi7hiucq4lQq5bZdCWa9XWn9mcgxjq0uvF3l26ltyS91kPPfrziJ8wXH02NMAxMALX3hmj2iMXJXDjuFJcb72YygZW0PIKEwNmUo2TfKOWkQjeOn1Ktkqk1oT8v1TW-N4u_iKm89J_BLXbO_xeIKgLs9vLxF_JTuLqn53g7GnAVhFFHLDgtsSuz-3bc-j974Eb7fYGCcu5ShvqX6K2icgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sujULq7-91jfxrBvMzCQ94ASv1B0f3mi0_3MOR1h7mZkqYU1xX8-pyOhqOZ04OUr8vnMEyHKZtHk-AGtWZoVMBvY-9sa8scdOExz5C-GtFoFigK53U_VUE7PzzzrJTzJFInJkZ_SWz0MPHUUv3OzpDyDjKojIJdQ9b6GlGex3ekCrlJn5ShLkMd5-LM8sL5-n3kC2_f472uS2nQpKelw4BhlOPJ5UEZYlyPrdvWnTRfcYERgF7n4Vvmzihgss1FBVHS31t_uqIUGd_35-_vZVe7R0SOnciiGtTAy4s2l8paaAJsl680V-Mzq2b1iXZtU7ZPlErGlNcQec8ycegZHcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T9Q6f55NCiL6U0h7iMwiIYWgFanXBWmidpU41yE9_dl0AIeBdH1EEFR1Syfi-6TpSiLvPcVpWXcQv6IC3DsMY7dYUtDYTeLTcmPTOpRQiBGbCgjjEu-BZwN3pzbgYXdwCVGoAOTQYSXNLrQL_dqGkLZVTWa6J9xW18XxDp3uEsvVTCwYWMh79g-Ihi1370mvDPCNzgJpNEbiIF6j0v9_-SZc4OSZNG6oem4QfFiv_z3tLCJ5VTktUfgOLqM-6JyjwJHq_rQceKSXteZftTzTaaQHRpMb0BFr_EA6y6crEoeWAaoStK5MCb5WpcrLFLBG2rye2u6t9HuYiA2jBqcElA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d1AnJ8dw1GxblGIGJsfgmLZyA9r862QaQJUwR1dD1WQSldVsWAcJfY5mwhzwVEMYE7Bpf3yeJs7Li865t_NmcudZAaapbWF-QBmlueIwN1LYTvsBkMOKu4PpQRPKLmJs3qZAbrXQ0PnLXeITuiPEIbIcRV0reS0P0hrLnmPV1t5-eUK80WLp4ty5DmxaHw_9YUF5GcRM0AvCi6wTSGKf4F61TsjcL4DkXigXuTL5C6dcmxDBcg61G7H4u7Fp3A9pvs9XsXyxNBrR2kYY95QbV0vtViM8EzBngv31uHxzVFFD_AO94jIXAsdWlj-kxFggotEiAjdJvIWCHcBwTxX8IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cgZB4nJslL9bdX0pYvHtEAULXWAXvjlpuQa5AWY9VUoimAIW0sTQ_30Ii82-c9fXJdY8UAqbuHsKz-3f5CB0d3CSiZ54nbiZuDHnfTJS21Tj9S9mdzspcvbJz9Kq_UIZYaAoXuRM8WRd_vtoMD_2cqjapnVPbCPMh4bxrE8-PEO88jghRVppVgeVgxu_N8hEajixxXkbfMiZ9EOABrBZj5gSytpnpt0im7-PAnDmuS96jZNIiNRgkw5Utc-bILRoYz34vA9pc3f21MVwLLfGaHcZcMIT1rHfRSW9aVPQDjrnMGkd7pvdKrng69WB79p74LOnty3vFChmdzcDzq_jMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0Z0Kk2K3dXae3bVo7sG5yYyBa_z4Tt0BR1iJ-YtjsocuVJ2heWKoX6fWU8lt4KQ6sc5Ralc5Uk2GnohG2E6mA8JQ5QkvwogJhwdxv-jgimcAIztLeKLz6gkWyEbE7kjbKtKCR_BSkQ2awozdCFduwVVTkiBtbhllpaYgyi8VzR95ywAthXRg3OEog9Oj8NTkOarheVbv_NoWwAwIOdyTbatMkjTRnHlXeHpQDJZLEunru69rN_pkAx-5tBYrercLUtFpB_ZQMrCCNqUIiVLTTfl1vn0_h-p8VQvGa3d8CVaRWvE7clyN0vypIHWeue90U7PQKjt3FC0CYUjm0MZbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cSjZHWf6git71yhRnTqNTdXsUf14m0kVrbQ8ZFr3i-ghMMBMaHjAhLBXJaZeCOzo2jqKZl310OUdxNygQV0Q0Mf4SONxMTtO1Lgl-xQlhunOBf4-Bo3esBZ_YpCdDzjZACbGa3BU9OmWOHSlcLjUIrYMzerK3XTL9i8J4HLe-ZY5Mq_gRA7OD7zeileyEgIJigZo4QaEV3pxYwd4skxu6qzGXSvk6yO2sLmyig77HGimXTfLuhXLTBEJJAArSFZ3tnRI_Ok_Q-d-kMDOdRM4MVRozMq6lPF1wleIJYgfsjFnJi5XSYst_iqcJizTTgZ0dQbvu-fxom1SDfNYWA_RUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YqICDo5CRbv1KELMTT9C6cVlYytgpfXjDZU262eKgkyq2eU4js5H2lF_dA8Wqg3oM_gbAcfsy5hruiBXen5HwNE36w9a9_p055m5VD_n5zLyOI2k540VYrrgVxzVh877qAlQFcO9aG8HOyOJRrTjLR9PAO9_kaEVqLrKkpdF5g1ztHqzH0s054-d0F2jzXwx_e1Ey_kJCisSgTSHRqBGedHMHOYdcSenvwAGDmlXQk2vr_A82x3x4AsTSbdUDoHVQa09_L51zxam9FzafVoI3Foyql5Sh-T-FIFwWMMkRxWOg__G1THNyg6su8eP3gj5Zv6Pjx9iZZV0Ngt-Ncvi2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W3ZJTsuR-wqhkXNQ8sktVy5MddgMbdzZ_Mu_uqs5F9wGq3K7Is4mDJSiyxWBgbYRctxiT7BDAqXt9_coTUW6E_74D-eDcU9VwczSCLyoilWXjZwCqK0PTGRbfHavGNt2yb_mt2cbQUSM-ZZOYgQshitYntlOyXC7OnmreOqMtbdYJtwbTZ7GmoVYf1RsHLDEXMLdkZc8dM1MGRqo19_VVb8gtduSI30yKIIdNHCxhfLyQQwBlVnbRmyieyXi-wx2R7Ms5yF38lecwZacfng_hJqBcHOH4lxTyQ9fOh_gyy5LHS1KUDKWll4o6a10eCcCJMXrxr3mPcw93gVTV9vRqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJb8PgtoBcRbR60ym5YYbK_0Y4ftcvTuzeY7k40T-mV7-rUeyhiaQT_Nm4_dY81pKt2b5W3a57zhIxMldSX0X8Jja-n78lU2otAegpKHl81AzFZfdftHiAslNuD61hxKzjV3WtsmzmV1agVFobXALmcedRpUVNcvgQQNlDzGkfTib1_2d2RhiYsDs_dH7jDZM1bfrzp1EtCeWuHmIxbautwWhOxcJgD_d68T9LJbCxpkubszjNKryTunbR91mQ5qQd-WxVsR6uXh9mnVmx8OiPI24cWOg6xbu70vGN_s6xJ7osLTouXOAAYjcX7ve-zynAuGl1tmbcwtsF6IA7InGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o4sOdunYWTsvGhkJCprzzSi23IHYCwVpjlZTL-Byml4zKK6JyLDZNewGpUFEFthJfgZzdqjnIvCoYPmjPhdtjbX444Rv9j7-WE7zyT5JDEQdv9L8wzw6hdmVJkM81jCSY2qRVSzZdFYI8TbWS6y6RwZAnIfkdAP7aQt1fwqqqqofUlktToej70CoF9ZknEyvrZmXTMQu2YGcVvcK1EamoA_ly3TJ3xuU0P1lyIXa5w56Wz5ZPt5EpKeoeIedCgj3RVDGXwMqdPWKaK19rDxbbzcS8E40iLUM9EhtPNakZN_JiAkW6LhX0lrYBQVEZZpwMUnS2aURkVxnUWGr2S_IGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PeCqxKJ_8fo2IBMNDjMU3i3-ebUsuRvcgQA3M_CP9OY9N5LvmPh_GYSk5CSKAT6xzWIpELRIKzOTBW1xg_3BuLuWmJcjsWx5Au4UR9N-4uKGHh6pQmsf6Avwm9A4dEkGhIXlT6e2Scs4bYnUhaBADlcG6t1SCgTVpmG3qsw67S1AODnqnEx8IITv22xfEZyMHVjb0DFUJ6fFsSDWCi3DMKu22aHdJvRl0dR4bZCq3KxFMgEMJZUEp1wOqprQ4sGQ3hXmklgCqWBoeC33mAqZo22cM7499GJSbnn2St0n2_mZAYtQ1KCzBUQNDF4dj2fEP3_Es3AY1-KTMSz_3h3eVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VhDnu2-eAQl8_4iFQWUS13NclhZWSZehjgQ918j-NM4RUiA39H1b6AWwo8I6_bXvSpbSzL2TavxlXkyBtxZsueIbEiIH3YqWG1Ysw7Aq7--PkZUgoNtgGyvsWQoYR9pjyk_ssJt9yeinQLLHcnf9ihH1Ubz6T4g8PZ9ou_OQDSvBl7YiSKy-K34o6AaMyjIt_EKZGXjh-0ZMxVuN2aF12-gdOfWpyhu0oKB54Gi-Bqf8tm7cWIt16zsZt9biR8cIEJCRJmKv3M8owTujuGDr8MrcJRozP5E6cLPoDWd-aKin5ONof1B4F-EmwCbbG1eYHoHo_AN_WQ0chul1RaR-IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dX338XZq4FClviBIA-T-6dFKKGGmZPUBPuPZ8mlh3CGXCRsd36M29MRUnkvX39_Kse1hsXsVlTf6sj84jwk7UFZik8fNQwxHjAb_14pJwGHMzqit6duXCVH33YEPKZIHe46mUPXcHkfkrA3Nr__Gf3_nVJEVMDMOE5eGucdxJ8_4STve_0aKhJYDIRRuna4qCtUIF0TH6oJKhFxeDBB36zT6TQsGqsJBsSAoluf8dHnV4AxhF4mXKMvpo3EYgakIdhbm2ez2gbhE7VijTqlarOgKC5jPbnX0QmgUaslmTSpx0pqUfoncUXcN2lENNZFQrtL5wYrrsvaNcjnqUe_Wog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LnKMXlobrTYXgtsgHgwgWUMQhNix1zKA5cgSieUdS-1cvTyB7akCm5TGKEEFXptgjCnzCWl6-u6pNpVVd-sUFYpT7O5XUeKusHbpMeh2NO6sKktjd6sjyxOjvyLi8HJRIS-hySX3HQtT-u0cb2RUE4eJJjif48mZVusj3Md8B4BGxPT1vJzlYO9Rhf77Lht0vwtDkNxvIDZqRtYiogcnDi7F1WMgA5GfqkXY5zSn-_ULbKzWC7P0sf618c_878XTdzRCqx29PT4Hzw6YeHun1NT_XfT_NcTY1KbH5_waUBJo2ghw6DSUVymacrmh_sj_PvhtTH5XujspBay2cWoJsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuecEDLGCokRp20MyOixy4k6BEhviVtm_3R_qLVIECOMDzusRdnlWZwsE-8Beqa5PaT2HM77utObXwPMJZCU-8VUI_zaP3eBhgjKaIgTflaQUK2Ph4_6ypyPNHoTBygHlEuVClK2gcOzmNU2tm7ojPhA6RzG6A_zYb-HWm54dGycQX6kNn0LHohArPP_7bFSKUVhAx3ygSU_WogiWo-oBSGx5yrlsPbjq4qNe2Tvy-wO6Sk4PgWOHT_ARTb-Nwhf0vjPnVPhIgnIvxRxrSyJI_qY_vIQl8PK-8GeSqYcim8lBaJZOaEXlWMUawG4WJKZD_mZQoRgjdcUXmxGaBGjrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bzZi0BLIrla1vVdmHXEzOMcYWpWqbNIlKh65Ad7KCuzA2c4Hx5yTufVjLPMhXXrSAyvc2MhnvP1A8OyVvBYxFSVgmSWp_zave7iusdVEKA4Nm_VCqimiUtIWPl4EqVi848f6sf4c4HwRiJa0561nRj9nu-2AUX9gBu1P2mJ-JxTNWWoqniyXYfE7zbNc4LwfS8CKJDxiUL_3CibB5RWqX_hm6-pRqLtIq3NTKU3k3p7wlSlh6jZahCYiYzrXkJJK0cIwRAyJDGZwuBIErNnPrMZCq0aVELRbyxiUrKMfQsBaOSL47dSOd2nZ0tL9ky1ccZ0d-4KOpzatONL4dDEL1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bM0RnOpBpF_BMsmlck-66FwIs06CZAzoKxtTif1-zO38ohZ8hlXTI3_fmkwAh1EJZWerUl64YuOHlUe31Rc-6uYvNuuG9sLFGZWhmCHAZ114mjwpRrqb5kB1_1QYym6UwffsgIfPzgI7UbE2ZmveWmDXrjK-4ujJ0v-F2jIH9jYmXBwkXE1DQrGZhlh1QCSX6qlAbTy_6OeJuZ8Rn7jlO384P8ILs8uFjCszWgYjDUPovwDh2WZSFQYAAA75CLSakj9OYIVVIlBytJ-Vs3_xXUQFJa7mqyO1DxhtSp0b4NHumBE_ASXang4V6rkeYSUtnyRF3fzX4Bu7U1sF5zh83Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I3LbEKLtvzLfQIISHMFY5t-shNxmDTczg-Gh0NsN2ir49e0-FCOl4iwRRgBX1pomdKG80p1N-wR18AmjGeLid7OkTWvHhYT29wOuJa9sKFDEyCDtDM3qKPeQ1kRXlKo5HohQAIhuDpM_dsZbM132mKX90tqLPGB4yT9HA-pgU865cqgU2cjSb7evjE01HSoZnkHdq2vFFxRUKdmIFubI2dc6j8Rz9JoGAZZBkni0mdC6RiwnKm7FnE9EHYCfD6VB9OEJChkcqxpiFoQCQcR9gocZuGFPOrzKrxvHBSGCnaCnVFAHzZZSQLs4nocFDYO_EYBA63ZAxnUcoJWGmGkOGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IOdt3VkCG6mwCKlseknge_nonoHR6LYvVjZ2rseddcwwgmyL-7I2Sh82OMH1MDO6tmQocGlBdb5Y3py-4_U-tsYmXkzQgVl_Mt9gz_yzU0zXVvSlwK7gn0t2guIdA7fHSCtuQoUaB5GQvp-JRJ4jFR28uZNFRK5TvKFKep6GHLgidwkQpTjPDszJPwmjo-1GbofYc2px-JFICKZijO7Hb_B2NaLu5hFOifCnyUbZLhzdHEMEi1I4YG8m851TMAViSJlWX62ONct0mZfWVwt2LVJq223dscI8zSKk2Vtskcm1ND1avaHcAl_3ZRL7vDI25GO-Gw14FIhCByMv1mfgrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cFftUFcnncRhv2dcZk_bVYALN1ak65nS-FELLfP1EfBeolyNwG9Lj3qXcaCO9iVfonIqp0qP9nxqqVKAZC8zvLuyABGmlkPjb8Se-PnTw1jyDWOPQS1h4CJ8ECUOGU2b4xw9k1d7C24qhaNgxPhT3n7_qrfOTK1Rct7Ubixh_Yu6sd16tAuhjHfB4pOTH7gq6N-6oWKHd78O-Rmk3H0CJdLKWMfbLyCC9EsNquhFPeeCFvrwYH07S5SBBimFHB5I0WDGbMn9WZqV7wp_UoYrmABQ2xmoIHzCuvFUkSz6er8ElUdndfwxzKN-P3UmvJmiBND8GmiTE6wpT5vkXsqJpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mXquINicG6EKPwsoCJytKGUjyRqv5tu-Si68Txl516LGWv7P7r7XjQ5US5uDu1K942QTwD7a1xgzgP2yawqRC69-rvIejvjN3Nl_jai8BQlsjrqDDwovEdE-809FsQI8f-qpgTFPE-7bMgaHZLSBI3d7c8s87f4oBHGw-xh2sGcB7tW6Xoa-0TrdaCqU1VORzJMsMNd1oJf2qBY3oBldwhXypjIxqXUIeJJ44o9dDUQQEGV7-skFNhFEO8fRBrO3DOWs4kZLOZllvekUvyIiq3kR2GJxkwd_vJDcfwRTup1nTD06Da_MfyGSF0rcbvxhfJwK01mgPbXx5OOgTYguNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qPziMxkUbU0u8EfsJ4aupE5wrnOoEYbB0Iwc2mnpitagsWuO7xzD44m-l2hVoXrUBeBPW_FWkNtHFeR2CqKkdI4TUizHF9n2yXqGpcPjTqmEISyH2Xuu_pvTi5q2LrGrnyiCkl-u3tI605Us0XjxWA1olCxfmoLJ-9xvR1jRcB-vP2Mlt8B8QT1bbZJ5o1BjbjRYvgcpoRraLd3E8Vxcaa0isk72QX3omjQCDs81iFxFux2CtT0YQq6WG1sDwb3BmoXqPppYB_XNHf4qKaJDi6FNmuEtVnyaJpCEdaGHt6ZrLYHXEJYWs_AmyZqtEpfoO7ELQt47qlA4rrDFWKOELg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Gy8HT-JpULB_bZOmZyE23DGwt7bfMu4C6dwOehF9EGJqXDOXIWlI__bVQxpuePkk3GIuO2-ZOYlWwH0mRSFCqcyDGDeyFaNb5BwDMll2UckH8ciJGRQ699hl3VS2Q1YbJcrZe7MH5tpvbAReHzJbWt3m5AQUIAlyjyEGYzg4j4P0fPbAs8CHR7mISppLJpwBR5ngjo34iCAri896BQZgoaISb8lMPmfUdCjUr301mXOwt0oTY8GVbyWV2lfZj5GlU0hrajascEyX7fvP3auWd65yF68gISQDLVkcogd8N6ojlBH_rLe0aG-Qrx1dbigfGkUYopbbNNVwILufJQUPYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Gy8HT-JpULB_bZOmZyE23DGwt7bfMu4C6dwOehF9EGJqXDOXIWlI__bVQxpuePkk3GIuO2-ZOYlWwH0mRSFCqcyDGDeyFaNb5BwDMll2UckH8ciJGRQ699hl3VS2Q1YbJcrZe7MH5tpvbAReHzJbWt3m5AQUIAlyjyEGYzg4j4P0fPbAs8CHR7mISppLJpwBR5ngjo34iCAri896BQZgoaISb8lMPmfUdCjUr301mXOwt0oTY8GVbyWV2lfZj5GlU0hrajascEyX7fvP3auWd65yF68gISQDLVkcogd8N6ojlBH_rLe0aG-Qrx1dbigfGkUYopbbNNVwILufJQUPYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lk3vhSgH6toczyoFAExFkPiM0C25YX2xYtxCLrn42VewSYiUv64l9NX-bGNwi_IqueGqMTCVAAiur9puII2EbG91Bs6orPnTZuHUjcrnBmKenVeOKmk-Xtf-GHqPQwQIDxrE02h_LZW3ZaIGFR1hkdwtZ9jebt-iPy-7FGmxqvzdcXGycRBI7mrc0kesCQUP9HxNyBLMg5OFTKFY1iyt_JwgiF5aCp0hmvbqfWuPwbFTWc8VpBUoF-F5-cZMlzIfqW49CSSl9LSBhaOvSiZNZ-ACTu4XWE8t8AstHfJi26XNHJbI0LJRHLV3n2y7XnYuRxHZpwaD411Lp7zAwSseng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8YpITWSVfyAPlWsztVV3GfG-ibEfWJ3dMKgfKCCGrsnh0m-FeB5FSxHDChHXsn8c2lvBhzbPuW0pZSbOaMLryO2Rj4lHkfj8VNt5qRFXKTkEZktEbX8gMUepQsKptpo10gApBoYlsqh2hjoUDSn5WRNXyJbsC9aChAMsCewO91si3TQ7ayUW56ilfK64KSwSrT9RZ_u-DirejcVh4FBh1Cprzwh5fz1ODOiPkvcn6_PlR2QuqPGAMzDckOSJvtc2sZ59mHW8mFvZANGJBLAqmr8C39rWbUI9R3jWJu6OvUT4-CmE3EAVgeIKzn6oKZHpEKjDbtD7W6Tn4BaoFYOJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a9vi5v4OuZAbmgf-YUsnibpgszp2tYi58qKrEY0rrWlpxKaazK-3fDaS7QgJwATiDJWrYIspzfzkNpqJX45xG-9by8AAy1LTlJo9POaBmEAZiGjwWcVoT0ENmJ8jgtvE_cDGiuV3wzuVavUvX5tqER4f0sS13TP-pQ_paokhbViQx_4zXqLftrI9x9TvRyQOYOApK3v6jZjmpcs6qMa4E6qS2nnc-EZBK2jrQ7mYFwq4EQCGVXeC-ua3pmpR5jgL3434L9Mv5OdBY9x6gEZ1CCFLGzIKb4922da6M92HX4Di2CWwNZr8R0cjGqUWcNX-wbZeqrmUjLgrnlLUfgDZYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/faiu1PjFKynhR9fMIms9ztkZzAJAAyK-Jw8eqjRoZO-f8j7b8h4jFmccr-PpILwxESNLu4goFLD9ddn52tKsnOS6pWxpdZ4aObO6lkfazYQGapzP0zz5rg2UdeJofcosg793XJKluODsB-5FRonjtlof--wQaRHy_jnkKy4w-4AXMO6bznIgWsWN1D7W-Zw6F2JDCYPfj5AyccMb-k_0XXmU3Khk-9QGvSDTat1lnWQCvTZpsERzFthkaRhSaW-LLGzd8mtrAiHNv73gvNEV0owS4T4Lw6Mn_9t4cPXnFSQG2966zeTP4DWLmhQr8vyPp7BEY85bAdhhh8lN6COHEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llLY-f_7ikyPFjQbyKVITyrz5y7BTA-cUSzGdwRhRp6a2QdARoeuCbuVpalTOTDhfc0COcEaOKkdOFVfKTcz3YqAygoEIauIR4ZKRn_IB9c6piKF9gFsCrSPuu8QtdHmethz15IEKHOi7cLuMOCd-LmekEy2WPdRYN6G2lkXwLdg_BmKtQ4DNTtywDAeD5CdMyCnFg86QjOcUbz_kfsoX-_qkTDALn_2Tb74MQAyxaxsVnVdYE1a2GNhyntOhSaz0ZYiOxdRX5vFzSkkX6mil9Oy1w0c7KZu6I6GonwPZpsSgDPE1-Y0VkyVr1wGYjJdpy_nOUQcJF6IvU_ngNG7jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MdBU0r_P_xnShkU5FEoIhJha4JNJCVbIRioWGwgq9jYowBkihLagMMQ9NFGNmL3Y16LO1Wuo6-vPkZZyApc75XBWWKmWGl4T2Y_Fug3O0oSwh0Fw27Ac-g9tCdR5C7ytrkdvt4xF4mJo_jWRCedBra-tK3ICtXmVu7_JFB3qZW-mDCznUtr5Lz66ZXAyq6h-undGgu2DhtHtufXG8WNITd-ZRDKzSLm30VKmuiWP5Cc69WlawEZcmnlYfQ7wlXLXVAQwbmaNbgU90ErVUjivTVEoGZEBoRmkuzFUWx03cLTU9zfHb8BuQ0fYf6y5zHNffhCv4UOP7jJnmxUjcYv1iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dr_ANqyCyi1xGUZdMxgGdIhA-E_vyd9ujS9Zp-ghf_ETCtDE4Sdp_UquA_b8z5Z_KkeJrjv0TSfXMcoTLtMu_pS-g2wdSVgTLFm-L04KyukopgEm5gYOwk_Tz3MdKlUdNgBx4DzuLu8ImFId-q_ESTFi5PPwVwvAOFdHwnjHz401O-5xNuQ-6wODYQ1nMkTB4XUz_Sgy93rdwxYlSmHOoOGH0alltBzSiw7T5UOmBLGuZ37sNGuv-XdWl6_5AUW-i4rQXx8U5bhEbQoU-q2H-Ks4Y4OV-Ob3puGl6kiKMXkqf4q2HpDvvM7NxLga--1J0gINasGxDIIB2jgSpXWing.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bBHasU8Qtm_FOpX84O-MyEPyIH95cG20p5283miATqlkazfBxqyjsUgn2io9dHt5PgeEKdxywxs10ahEHUexcaa9tBq0VmnFLTV0_KT9Z-5JPJhMGZJflCPg_6gQQA5_MDeMcVVoXtTGx_uGgm5apZEDKrsn22by-hFPPZfhVOE7KIY9F8aKsYVM4PU63UpEpqlF2Vt2AeyeTNbio2-vVrl6ux5ZMxiCN3STItYRijlW6ywk3CPQJCfO_I4ZEkulb-t57MGPlNya0UDExhTzZxyCzwrHWVogDUgeH0oQgTN78_7dnOsFTOuNTe592wd_5x7oI4wFm3dTmssV4p9haw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 64K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxRID6DOVRjKs1LjDCqWL-ThTjGPxrx18zvULbL7jAt3E7eTSFlbIcQHfwZSgW-oDptJ5pN3zOSb0WX4hX7scnHxVnT_jksZziBXEok6ja-cif02yKlTISpuGjVPzqIPUNYGvb6AfNuZ8WZSm2zBJPGa-IaHmXj3huUtIWu2SUIxIlgD_4GIgFYrmGCebKjB6waEs9Cd4dNYXelsePF8xwrLvq7913vukE4b5kS13BaobI8cqu3wHOKRDmzA4IRJienrNb556SfdRkCel0oFtV-Obnc2VksL5Vy_6zX0951SYhCq6rFI7Zr2AOtFP3_7W9mhmxAc3U7YMmplN3Ch1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mpSC1bdDpWFxkuJvFMr2BnJe_x612jUrCIBptd2QCISWOjOHZplSh94Q_xyotQRtU-qd5XLaPpbZgpWvC3xYug86kkd29Llyiqmesijmko4rJTrViYwrOYz6N3Vw-1tA3y3jpyXRw4j2dO4_WFadKg91S57S4H0DHtC8Cf8axb8KmyEzvLyhTDJn-Yi_-7h84KU0pivaLeiiyMvLp5evTEGhGU5c1bULYlanz8KOh9hm6qvEVCSjJcp3sTL2-BrpgIzTGDsOeLkxsHi_tGOzG66CRi5ae5IlXWKs2KQ7HPyRxfR727Prjwm6ENMWaMmIRHk4vJn9Sv8bHDNMv1Xipw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDQV2iC_EpT7UMF5nw8PaCkgmwWieBlYUvrINweVNHRAaH7-arx255hMpMUnrGupINkl-NUUpbzAmrVelyQ3K9Z69bbRdrPr78P5TEeamyqeaerIwDvs38VbyPKAcyr9Sn-wijbIn_60tsRJFlesz-4-1Xfwgy2CkFjMSfKE6S1Y8aEURaZZ173B5k6rZ4V6FDMJ765tIOX0SABvWYobKjeTxhS7MqkscBbqhy53X9SxxpxGMwAlaFjM8HtvmGZY8eD9LMVC0stdh-jb9Ppeen3_Sj0Q1ut6umYGvS4qQpvpqVdYHYS6YhpKAwsyaECITslkeDmBXmJFef8MoOP_5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iP553bMJ-bS8908DRTDlQPmH_z8UZDUhSZY-0ua7tQvXgao9eGXLotv_O13QbS63YA9sAXKDJq3I71p1-IKV-eXQh4KQ3-AzX3zf2CYA0VrQEpyLd3XwFZtzd3FvRXEiYXuCzMh7VJf5mFzUppWQIuKH6GtihfnwkEGx0fWxQB2qUI85cEEWU9bnveMJVaJ-5MizPawZxyex5vFFtfso7O6IttSLo_pkdWMX0rAIPfU8LxWQ7YsBVbdz-B4neR3xQdpY1gXdhg8bx7BiJ2KeNh2HHnon1uDGhXMIjlXV31AQ5Obzz-7E_7sbAGVGsqpvBC-LVlNHlm6DxP9xn1eAqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ls7LA5MwLDa894Tj30zkvwze4Ao917htVIFIOrYIJ4layVDinYvSR42XjY2rM23TxwIDTaEgAPXTZrDnvEe2WPrZ4OWYON2LnYY5Dq3e5lVd12ljhszCHJXQNamryZTyxILtPma0nWekYyJMWqD7lDXkmm5oL_f-fCHJkiS4Xu672ptKb_nLpmjNZ--QLzU1SXhx9974cP7AchKiZrpYDVpl9gkgGu3Gzxrur-YgLSVr1eq17GV1fMwY7wTpTenqe89K-YB6zEbQf6GqekjtlYxCm3VmudUA1sYGadtsf12iyr_Xw8LLqx2MkXO74Hbcbc7Ek-EfMo7cGGFxhRe8YA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
