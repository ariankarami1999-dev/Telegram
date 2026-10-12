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
<img src="https://cdn1.telesco.pe/file/szKxsa23Py-3OhHntADxWHwd6xAzOvkz989j51tKlNca2OTO3Wtzf4etzy9z4nGKGS7XxGqqnPDbajQ-lfEcRmWEVFREr9xQfg_FVbhAUE5aLu0KY2tr7bJRIDhF2GUEYuEIRNQ3iZqG4Vs0cN0jc9u_-OFI8eB1yX_-PYTUic0HT6QQ-MABuqoa954FH5CBS7b7cCfAFW9nmSSg3Evhql0QCfSbvOE-tFNKpomaJbGpg9qyY_y10hBRqjHuUHbkODNuKScKHeZXADLFeQk1kZZj4T_p3qwvXHNenVMVnG3WHbc0krvGj8qLlrmTGFpIVp7c4bVGkDlHeehoDx3WKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jtW2W0gRiC0V1OOCqC7LfifowcDCVYX2f7Gv3AMrHBndSNXOaEC0a1YT8zZLyeED2jdOqQ9C3Q_pscmjXcoDBw95R1EcU1e5l40nMX3nFSeJVTjPh3zhscPfrehQ9ZchiYFph4jtPa8ht8ajgNihE2vn0I0lYJufhwsGC3y2cnCilWpBidt4QuQZWcbJ2wA7JgQyILeOKKTjaZFEb5wjq-xZVDu5xhUyFcPNwdT6JaBcHIcOWHrSnEkbNTT6HOEesg4JdfSdY3wrYbvRvAvDNBS9gI1UQVnqKXKWRf47OCbpB_xcsXDY1pyAuz7fxVfPtPoIu0x9mF2Ruclqt9MBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه CLI ابزار متن‌باز و رایگان GNet برای ویندوز، لینوکس و مک منتشر شده. جی‌نت که قبلاً بعنوان یک اپلیکیشن اندرویدی شناخته می‌شد، حالا با نسخه خط فرمان، امکان اشتراک‌گذاری اتصال VPN با دستگاه‌های دیگه رو هم فراهم می‌کنه.
با GNet CLI می‌تونین سیستم خودتون رو به یک سرور پروکسی تبدیل کنین و اتصال VPN رو از طریق پروتکل‌های HTTP و SOCKS5 در اختیار دستگاه‌های دیگه قرار بدین. به این ترتیب، می‌تونین ترافیک گوشی، تبلت، تلویزیون هوشمند و سایر دستگاه‌ها رو از طریق اتصال VPN سیستم عبور بدین. این اشتراک‌گذاری از راه‌های مختلفی مثل وای‌فای، لن، هات‌اسپات، اتصال USB یا ... امکان‌پذیره.
👉
github.com/frank-vpl/gnet-cli/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/ircfspace/2667" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2666">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y-8NwBcAaI7Y12dWPDNNSjAQ1Tcftj21PXoUNiETItWz_UlNgdwl5SBkqgR3NEaaJbbSb7TxnRDK_ModItq_hmHt0NXT8MkojWfRFWUzT1KauBwST9z61aHtdqR5gyj4lF2zpYsKLeE07rXu5M2m0Q-Y_rK96d_EwggVg_2CEdSU_C7Mz0IOmvC0PV2XFsyawG_61IaVsSE2PjxnTFj9QX5zfoS8BBap5Q-rq5zXG4KNhLaQmqm5y1wU9hYdFTbKomi_A1CrPgglRD906ED7PZVQ1LskWkza4rha3fx5gVK-HtIpFaz7wJIaXTMmE6dbUJpsfwbDv7rxAyxkh8u7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست در گزارشی نوشته افرادی که از داخل ایران به ChatGPT دسترسی داشتن، با استفاده از هوش مصنوعی و هویت‌های جعلی، نزدیک به ۱۰۰ مقاله درباره جنگ ایران و آمریکا تولید کردن و تونستن بعضی از اون‌ها رو در رسانه‌های آمریکایی منتشر کنن!
این افراد خودشون رو نویسنده و تحلیلگر سیاسی معرفی می‌کردن و از ChatGPT برای نوشتن مقاله‌ها و حتی ایمیل زدن به سردبیرها کمک می‌گرفتن.
طبق گزارش OpenAI، هنوز مشخص نیست چه کسانی پشت این عملیات بودن و شواهدی هم ارائه نشده که نشون بده مستقیماً توسط جمهوری اسلامی هدایت شده. این ماجرا نشون میده هوش مصنوعی چطور می‌تونه برای فریب رسانه‌ها و انتشار محتوای ساختگی استفاده بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/ircfspace/2666" target="_blank">📅 07:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bfQTEJzvg7gPXCXKXQaN5ktw4Z01NFbRRL_PRv8qzwhhYUYE8LA877JrH5Pxonsq38udi9RINI_Z20By-2tYvc3y5oqMs-VQjFYGy2ootm6scMUH4U4UFowNV51VsW9T2jE1N4tAK2VacwFmzwj4jwl16nXZeLQMn59ValKUMO8j3WoDkbAm4oVvBH-Vi_MLLBRZMBuajhkP9Dw2QCxB_UYpiuiJLJfcdiz0Zg1BJnBnfBsO0g8hxADmcQzoB1SoJ2kf2AtI_wyB-OctFTGNkAHi5k-nLfqu8UrgWNl3dpRvmJi3c_juCAeL41-9Snhte-Mr1StORq1q6QvwpwwKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل WatTunnel یه اسکریپت متن‌باز و رایگانه که برای انتقال ترافیک بین سرور ایران و خارج طراحی شده. باهاش می‌تونین پورت‌های TCP و UDP رو از طریق یه تانل رمزنگاری‌شده منتقل کنین و اگر این پورت‌ها مختل شدن، ترافیک رو از طریق ICMP عبور میده.
این اسکریپت از روش‌های مختلفی مثل ICMP، TCP، UDP، TLS، WebSocket و gRPC پشتیبانی می‌کنه، امکان استفاده از کلودفلر رو در اختیارتون میذاره و مدیریت همزمان چند تانل، تغییر پورت بدون قطع اتصال، پشتیبانی از ICMP معکوس و داشبورد مانیتورینگ از قابلیت‌های دیگه‌ش هست.
👉
github.com/JohnWatsoon/WatTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sLmGRhWTcIKeCUqlPtMkH-dEh2iGg1s7oI0mnkul7XvE353VUsLkvLSHW1i7EiVlDtrSGExS_4BafQhVvJgtqZyzlbwUIMxKl5oL2QC4egjFBQwdpAxITMECeQJXJXRwV8m23zcb2gU2cTF_1P0p84CWcIox-LZS0-m0eluEN3vMsWq8IpiTUmEKoV-M_P2Yw5ugfWlZEMLiMToYfz9YywuR01kcC3jIin10oEl4aG8t-6sVNBKaqFW5H4XcN-f-ZjNiVhN4lttrd7Vxc2rVy-WF8gxKF0qBrWTCzd58Wn0hZETpzfQzAZ_TWy9kFbsNT3qPCBrYsbjextkjD-iH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون توسعه شبکه ملی اطلاعات وزارت قطع‌ارتباطات: اگر جنگ یا ناآرامی رخ دهد،
احتمال دارد بار دیگر شاهد قطع اینترنت باشیم
؛ اما مشخص نیست که این موضوع در چه سطحی انجام شود. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXJW2Is9A9qhvFGnPdgadNWHHEv3yPCy8unebBUOPwk921eJmEEHr4X8EtY-xIxoikvvhPd3LE0P_53tGUOwuCB_NYDyuDUD7KEuFVongfeoiORUa1m5zb5-JY9DR1CQ5wzo7jz8JFKRr1XxtdQx6wqtlZACVTXcDXK3GI2owGqivYhiFuMnD6HV1kDWV345pQvfRC2Vf_TV8Q2V3ghxP7965ajYeBUPGtAu36gz8ND1EJz9d1BcZI5da62vbOYR1YZw6ap0zXquc1aziUlKfgi_bpB257y4J7FmkyW1taGyCELP6ovjx_qiwMSMxr-_AinFLa7MkpbIsicJbtiR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخیرا یک آسیب‌پذیری امنیتی مهم با شناسه CVE‌-2026-‌107181 در تلگرام دسکتاپ شناسایی شده، که باعث میشه در نسخه‌های پایین‌تر از ۷.۲.۹، با کلیک بر روی یک لینک مخرب خاص، امکان سرقت سشن و تصاحب کامل حساب کاربری تلگرام فراهم بشه.‌
تلگرام بی‌سروصدا این آسیب‌پذیری رو حدود ۳ هفته پیش در نسخه ۷.۲.۹ رفع کرده و لازمه حتما اپ دسکتاپ رو به آخرین نسخه بروزرسانی کنین.
👉
beaksec.github.io/posts/telegram-desktop-one-click-account-takeover
©
MilaDnu
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oF-q6hkCwBYOBUBmc97BRE0tfXfJ5IaeWEChTiSeAHhysvqn2THLzrQK2iu4hpVIIW3IgGgDkgCttlbpcXN9xNAua9d8NP69nyulnSEba826P1pd-d6_PI0reNaRmxjkki3hx4nc1u_YbI1bmMzcdscvWwz22IHN9pBigiUYXWU5Wmwwk57voFOV5m7Zl4ksh856yvgyc5sufWVmBa5zpmOwOY5XJI49Ak-CsHja49wqQcj30R5QzJLFxqbdIxGgUtOGy_ObzN377YqyvCpz6yNaJ21UBxp8Rq-RdwF65KxmLNCfDL9BELt7YoeNzMZ_MZ5R4_psHegJf-OQSWi5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل NoRoot VPN یه ابزار متن‌باز و رایگان برای راه‌اندازی کانفیگ VLESS/XHTTP روی هاست‌های اشتراکی معمولیه، که فقط با PHP کار می‌کنه و برای نصب و راه‌اندازی به دسترسی روت، SSH یا باز کردن پورت عمومی نیاز نداره.
این پنل از هسته واقعی ایکس‌ری استفاده می‌کنه و ترافیک رو از طریق یه اندپوینت PHP عبور میده تا حتی روی هاست‌های محدود هم بشه با هزینه کم کانفیگ VPN ساخت و مدیریت کرد. اگرچه باید سراغ هاست خارج از ایران برین، اما این روش به معنای ناشناس‌بودن یا تضمین امنیت و حریم خصوصی نیست؛ پس بهتره برای مصارف شخصی و محدود ازش استفاده کنین و مراقب اطلاعات هویتی، آی‌پی و ردپاهایی باشین که ممکنه از طریق هاست یا سرویس‌دهنده قابل شناسایی باشن.
👉
github.com/mr-r0ot/NoRootVpn-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dfwheETfG5Aod80QpzF98pzFhEjFH5mY-MSqdjUFGNg3gzh1jANKeIvGt9aMcfT6yU5nd8OBBgpBazn8vg9-hmk1mHQUR8d47b4441vFIhQdC9BAQPwFHO1eSDPlLFAORf-N7WMt8-3h1KrjZx_daJ-24vTAkOxM9c36iqniuxblb2TcWl3cea1XYIwJohmj8rnss8M3wTQxTuhbzm2w6H77MYCYOkiyLleJt8vhtrlHpbZy9kSZp5AUqf6RCPOnUwFm0pVPn7awlhFbULEKoOzhCd2XrvP-_mQgj7NJIS76t4XiKhSzwZDNYkiyOE_hawVcxxLqw4mOVbkietIGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7eNmdQai4CqZoy_GgaScbH_V4A6J9Igotqs0yk3xptzDgglbluGh9fGw1ssIdiyDLVStgVvGK4qMI67_zx63FB--bGFjU4b4Wvjf9MdWtLl1sTlUo97KHidBQMIrNT1lyz_mzii_g0SMOkbDI59yaWfhDkvN4qJR5IEZl6VClkSKVY1HMq_-Pdh5gHPgBcDEeNl-1LyQWyEr1nxsX6YI_4ChCZxq1UaOEfT1Y23APD-NfwEZHG5v2oVuotfFHVofast90OorQrDqmcexQJdy2-O5fRhd8Vupz_9P7knC_lPip74eF6fWcdMMEq1AR2029N4RLifurB7DSGeFOxSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hcp3ZshloA0x2fpJgoDlD89ZMx7EQLfTLOjwNBqmORcslhZSpumFaOwUqW8eZR-8dxi9sXUUlljMW_8NImLfrl4B-pswJv9CZ-3D3EJ2U6rOb6oAr9Jxtk5PVUNo1DQghNdD5DD7oiEV7qOzKQvhZTwqf8vYuiyJEORizTaq9y_SSU6wdNXwsM-ElJ0n7fY8jhL4u6s9vVYEalMXICpGdUjBihYTwsqf5QlCC67VvD-CDSO7_MgRXDpGGYWB12sAIwZl8P3i_YnginBF_tggkXEokC6y5oHNi5Pdy4r5Z0kJeLGEFAvALT-NkcrnFRuGYjcqy32Ycv-rTBzWU1pTAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه Void Verge مدعی شده با توجه به تغییراتی که دارن توی شبکه ایجاد می‌کنن، اختلال‌هایی که روی اینترنت و همینطور اتصال VPNها دیده میشه و مهمتر از همه خبرهایی که به گوش میرسه،
شبکه زیرساخت برای قطع خیلی از پروتکل‌ها آماده شده و فقط منتظر مجوز برای اجراست
!
روش‌های مبتنی بر کلودفلر، ایکس‌ری، سایفون، DNS و حتی تور جزو روش‌های اصلی اتصال فعلی هستن که فینگرپرینت شدن. تجربه جنگ‌های اخیر هم نشون داده روش‌هایی که عمومی شدن، زودتر شناسایی و مسدود میشن.
این گروه معتقده در چنین شرایطی به جز استارلینک که البته دسترسی بهش محدودیت‌ها و چالش‌های خاص داره، به مرور باید پروتکل‌های ناشناخته و ایده‌محور جای روش‌های اتصال فعلی رو بگیرن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lwZ3bpgP3OfRQ2Sv8cmLsYc4xVXWh6ecjuXHYL--lAnzEfI5hEllCNgtDBqEbmTkFA_y_BsQwHyMbc_Bk8dwpQkDZtAn33ZiI_qg6Tyhp7Sw9u5s4Ojt0qULnv9G-bU5t23oX52PYEWoP0o0VI8oQJI3_pp3q9zi_Zl0ec3tGaKK8Meb8oSlWoXo-Ib3mmQfTQHly-FZ5RqqrDxtcrnF9wVVvwriyjX8ME7pzGypmlWz2y93dOf_b26hhE-vOSiNyG4BmCXxOn-JoViXX15qYUzWA7agTQ_5NmlXrBB-ziu9TZJJMfg5Cxdg5T_jhxMbhPHJXIwU2XPqtJccoOcRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت متن‌باز و رایگان ZedSecure آپدیت جدیدی برای اندروید، ویندوز، لینوکس، مک و NixOS منتشر کرده. در این کلاینت از هسته‌هایی مثل سینگ‌باکس، ایکس‌ری، اسلیپ‌نت و شیروخورشید پشتیبانی میشه و در کنار پروتکل‌های DNS، امکان استفاده از OpenConnect (سیسکو)، IKEv2، OpenVPN و AmneziaWG فراهم شده.
همینطور OpenConnect روی دسکتاپ بصورت VPN سیستمی قابل استفاده هست و امکان اجرای زنجیره‌ای روش‌های اتصال مختلف اضافه شده؛ مثلاً میشه سایفون، تور یا SSH رو از طریق یک کانفیگ Xray اجرا کرد. روی اندروید هم قوانین مسیریابی میتونن بر اساس نوع شبکه (مثل وای‌فای، دیتای موبایل یا اترنت) تنظیم بشن و با تعویض شبکه، بصورت خودکار تغییر کنن.
👉
github.com/CluvexStudio/ZedSecure/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uf5HdX6F-CU1E24xN_OFOvJr9C6OWmf0uXlOSHFV-kZ-vQu-8sLbgmTYKAwDEmXqXnkwfHQ2z14pCgkvCnM5hvyEbF6thTJvJH4AaRMrhZ-55b_Hd2K9AkhNlp6-XWnlfXXsrGNonpXcsL21HH3WduNwnOPegiNSyu2SvlNa5zv7sRSbVR_NIg80GMt7uWH_AgN9OUVZU2qTwF872xlJ3-pyTWhf2n7Wm7zfh1TaV1nljW6H3YLraZsbf0DWk6hJQcoCY23C2lYEpWDUsfib7ca9A5zq9Id_Za9LVcqgpufj5r9A294_h_dB_P2SiZIGrdx90bCiPn4Mm2I3SBr7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oUjvkdTxuTAMl2oBoRtSebBqAIPHIdZsx85Kq9WuzjtniLvgizvUUfznUfiKrDS_XDCDiCWnfxfnA67m2CXaGMT-VsIUOwlHQpbkkUDmDeeDVmCUqttL0B5n9KwqmVUhtDLTws91IPhy47itJYhBnrxvwflmx6Q9_2UNh7GAaQkodujNR2NkyaapjDonraeVBwhwg-gS6h3uZ5zvzn15mbQnJAjx-7_BoUR12pMOMZ81BXVBpmcAQzC_eMMgmu-XfxVamfYLWqY3S_nDszADfxonbRq6xisDhmPD7DJOHagFsb0faEKEnlMzKRNLP2L6T8KhT9Um7VfyKMHpND6WXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AnFdfvMG5SZehKLfXYgNwM-IuNpdjj69UgQ9tYvcxFfhu4IbCKA9QYHXHM6NnEYv4paWBxzIpC42v1M3EU2YHKJbjhDLFaMghh1y1tuV9AZ2-3OU3N3qnG1kmbTlw8ZtcwbkxyFXWBgjIMxTWqJSsyKM1Meay0GFtLwtUQDmbk1lReFo9ufDmINmn1o-pIDeSyeXHpyGYrki2ngXMaRDNMoL1azbnDzplFrAoZ6C_lTC10xrdL7Foh4b6lzGyfeMMf1j2aVfN2boC1O3-SUY6tLPrbWqgwXhXZ-CjEM5BUWxoG5BVXlce-ZI87Jj-tyMc0zUA3kx6ibBvxiWqN7a0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اسکنر متن‌باز و رایگان SenPai Scanner برای ویندوز، لینوکس، مک و اندروید منتشر شد، که توی این آپدیت قابلیت Anti-DPI اضافه شده و با تکه‌تکه کردن ClientHello (مشابه چیزی که در PattNG انجام میشه) امکان دور زدن بعضی از محدودیت‌های DPI رو فراهم می‌کنه.
حالت Gentle هم برای اینترنت‌هایی که وسط اسکن آیپی‌های تمیز کلودفلر قطع میشن اضافه شده و حالا می‌تونین آیپی، رنج یا دامنه رو مستقیماً وارد کنید و اسکن رو از فاز دوم ادامه بدید. امکان ذخیره اسکن و ادامه دادن اون بعد از قطعی هم اضافه شده.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شستا ۱۰۰ درصد سهام رایتل و ۵ کرسی مدیریتی این شرکت را به مزایده گذاشت. قیمت پایه واگذاری ۱۳۰ هزار میلیارد تومان تعیین شده که با نرخ امروز دلار آزاد، تقریبا معادل ۴۸۳ میلیون دلار است. فروش به‌صورت نقدی و از طریق مزایده دومرحله‌ای انجام می‌شود.
©
stup360
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/de88BTvkiWgz9YCX-jmHxkXGiyypT-xOUVaCq6Zm2uddP6x_hIXopnRuOchYdgamFxMQR9icrTc2GWFurcEQOoloqkasjgFOOd2q3Qj70_UkYBDppaqoXIF0gL8PFpHL499w8JyjkcqUm8l1giTlj2tOZSWL8ISg3SZqJdwDAJka1Oba9mG9qsDZnA4EW9zFx2ru4sH57gWtrYccK9lxkb1rLhZNlOUF7tBNd6u51lwgMy-MTP9o0JE5R9q2iKm_MEcJaTWp2_FCO-sNZ6awDMQK1aMfiJRp7ZzbZWueJ6-mhEaZWb4o_0XAyVUCIsex-uVbcgpeMq-n-ppYWPo62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها در تحلیل وضعیت فیلترینگ ایران، جمع‌بندی روش‌های فعلی اتصال به اینترنت آزاد از طریق کلودفلر روی فایروال همراه اول و ایرانسل رو منتشر کرده.
بر اساس این جمع‌بندی، روی فایروال همراه اول میشه برای اتصال به CDN یا Worker از روش ECH با یک IP مناسب استفاده کرد. استفاده از IPv6 هم یکی دیگه از روش‌های فعلیه که بسته به فیلتر بودن یا نبودن دامنه، تنظیمات متفاوتی برای finalMask داره. برای WARP هم میشه از متد WARP-in-WARP در اتر روی IPv6 استفاده کرد و با اسکن، IP مناسب رو پیدا کرد.
روی فایروال ایرانسل، برای CDN و Worker میشه از متد F&F استفاده کرد که نیاز به تنظیمات مشخصی برای finalMask، cipherSuites و فینگرپرینت داره. WARP هم روی این فایروال قابل استفاده هست و محدودیتی برای نوع IP وجود نداره. علاوه بر این، روش MASQUE/H2 با اسکن IP و تنظیمات مشخصی برای فینگرپرینت و finalMask می‌تونه برای اتصال به کلودفلر از طریق هسته اتر مورد استفاده قرار بگیره.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tHdzpzABHaz9OvSdOnGkx3i0LyhPj2T34J89l1aZrOwX-PS4PEWJZu1mIJrHOGXGNTEJedK6n6hDZ3ctqRvyxbM2Ks26j4aT6DmcD0vHS5EOyLN4303hYiOROgQ9zw2na2w7nojOFJY38h5Ng20NB1_p2YYXJSOOKOf39C5_ZtsKE7gcwYcDZI38spT2qqY889eOoqBg738KZE3ekU2UFnHNrCZOMK5Yl5OQo9B5pc3AYU7DUTWjDg7PROZ6glhzPwrgd0UtR2LO5Age_Q_lsXs2eYKDTfqWME2ddXq8r2Yrm6nF9ZteTwJtPfa08zhgey1znbgQ7z0ofRd6LuhMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن دیفیکس توی جدیدترین بروزرسانی خودش قابلیت تانل‌کردن کل سیستم رو بصورت آزمایشی برای ویندوز و لینوکس اضافه کرده.
در این بروزرسانی عملکرد کلی تانل بهبود پیدا کرده، مشکل نمایش پرچم کشور محل اتصال رفع شده و چند ایراد جزئی برطرف شدن. این نسخه درحال حاضر روی گیت‌هاب و گوگل‌پلی منتشر شده و بروزرسانی مایکروسافت‌استور و اپل‌استور هم بعد از تکمیل ریویو، در دسترس عموم قرار می‌گیرن.
👉
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlgqmVQKxqBTWSR4blBDmMZqvF4LlkE0vOn_rlc3v_c3Dm9OGUCUSoUeUoM_CSW9b88F4rWmpfe_SQyCFUD06_E4IEwK7p7It1dduFtucFTMcpxT9OV_tsU28F_5FFM7Tua8y8Zj213WaKuWCvCO5DILVC6w3OuG5CFbxwkAFJtyZJCyhHp-in6eF_92vgFsBRpbESQumOni6YDpDnmJpu6xSn43mGrp6u7dhrJSD_EF5FmcqOGRd4D96aDSsaUf_YQDGVJqC5GGDGPi4RQgyzGlz8JiMuQ08NwbTIOVWd5TgqmafBHabhzvXLOUQ8-Wp52CLTzaBV4iaKSN10hj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N5ENOm5aLjqR4ZfvrRG0jw2DpgxplIoScxkNpIaUqcMJDBznvHNVTXEWnCpXeCgvwQo_rVv6vh76920MBqfmajAYqW7OxZrKpz5EjWSSGWbrmOhxJpsH7dW-3s9fLopvqqZmUIMrDoiBXjrTPePiRV9CiA6mmhzUlLH4cA_q6ojt5KkeWKRsAr4MHSXUqyVGZP3HAmYDARwXm_kaJkpnmsbW6U6HNOy9PaKmMMc5siIKZuhYk0vGZen3xzhGt18HmvMJl-artv1stgr-PlAqBqlqIl6qKdWY8ecxFuhNFZGjphaj48Lqf_PylHbSYNVKMfJeWykcenbHG9cK70ZjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در جریان اعتراضات دی‌ماه تونست با جمینگ و GPS spoofing روی
استارلینک
اختلال ایجاد کنه و حتی تو بعضی مناطق کیفیت اتصال رو به‌شدت پایین بیاره، اما اینکه بتونه استارلینک رو کلاً از کار بندازه، دور از واقعیته!
اسناد ITU نشون میدن که با وجود این اختلالات، ترمینال‌های استارلینک همچنان تونستن به اینترنت بین‌المللی وصل بشن. حتی راهکارهایی که SpaceX برای مقابله با این اختلالات اعمال کرد، باعث شده سرویس در بعضی مناطق دوباره پایدارتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNG8Ju05wmFAEzThqZzuYRubKSw6YGsiHv8ABEUkaKhFhaVVDNTJgPKuD9rOk_FPZZKVtasQgk8DwZbVrUcrZE55gpjADL-R9ZKwk-tzMCYe1DFwXFd8ZSPmyOTxote2iKWQTez3mJn4rzzSlhCi3dfSYRaaJPGPihvNCGGx97h8Krw-IVMuwIIwddbhA1nqw-1pOu0MMgeqmknWjXaaHLFAjg-oQti9ei3fjLI7HOHUlPyLEFrWg2tfNHqqnUPCagB0C4neWt9ZXT5ag_I3acHs5SaHsBljpTdlx8LtZcT9a6KV_eSmH-miCcxXqVAma2MiisoId6WMQf8ppWbTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-ayiZ24xH4kZUQ7ZWoKyoLXaHmoH1MjTWOsOwGjHCT-Cqyvecv_sKEsEDQ6zxdysOlbY70HB3_G1w_jx9fwF1GLtck7C5tfVekBdQp_54xul0IyS2QaooRLJUHYWPIz-JJmUSEWdQH2-FyACiCFpJ6YtF-mHcbriZrcaoLzJAlW-9noeXifzL8K8GeXw-AGXeo6lMTXkKHbjc5x0WxcxMNjpbL7G9igoUHFHfMfCdH5O1sDlpF0-_cD5A2GFysmkTHFAtciMclntAFFiTmefXIjPHpaCHAcY4dUkfTHfYnquXYa7mG18XAadVvXzio0iYoYX0pQ_lV2zUW4_H1NFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از فیلترشکن متن‌باز و رایگان Aether-GUI با آپدیت هسته اتر به جدیدترین نسخه و اضافه‌شدن متدهای اتصال سایفون، تور و مسک‌این‌مسک برای ویندوز، لینوکس و مک در دسترس قرار گرفت.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gxpd9xHWrC1dkVhH5zVe6fwjVk8PwQWtVGl9fm0L2uXwapxKn4fKRlH10WsJbG6sM6orJhH8sPI5H17iPcWuHkMRlHAmKm6HAbb574TVcbO7psfZUSGubRHFS3Q-UrAoHfCsKRb6VQIF2ON_oCwqQMFDhbV4OOEaG0ADiK_olQHnwywkkJP3-Oq6YWQHoaLkaNm6zRxbUBPeT8Q-PWoV-o4X7W6I6gU17mBpYIZ-lnJiT3CytcypP7qZOz63pe6lXGa6yzfoi39-cOXHWx5pMVPRQVvEK27hx2p0oKR_BdadCn_mE-oO_FAKcWo5TYke73qibC-0P9WohbTa79Dxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mPjIk5LbuYfrQbGQPlRLycq5pZ71X2cFnqLvhU1oBmMDX5bJAFrm7LOiqZ0g7WB4x-4FKFjkF-jibgC6klVZjmGVhihyPjNCYm27Y7LdGL0kEk_rriwEhauo1lSArDRWZcXsaQQMd__QEiKzqHf_izYhGXMplotJzfhJMuMcJCcFRe6P2p1b0rFgzoIRCVZr0M8x3dkyrY9285MSFEWxDvvG_wr6M2K4MnLsQxVxqSQjq1WjutaFujl9-hzbid6pzUPl-fG88jKGO0I5HML7wusAl7QhapNVF3KEqZXmBVXsWFmYU571dGy-baC7Pn1t0P9LRs52zpEvWOm5yZPYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زومیت در گزارشی نوشته که در حال حاضر دو راه رایج برای دانلود فیلترشکن JumpJump وجود داره، که یکی از گوگل‌پلی و دیگری در گروه‌های تلگرامی هست؛ اما بررسی کارشناس‌های امنیت سایبری نشون میده هر کدوم از این جامپ‌جامپ‌هارو دانلود کرده باشین باز هم در خطر هستین. فقط خطر یکی بیشتر و اون یکی کمتره!
جامپ‌جامپی که از گوگل‌پلی دانلود نشده احتمالا یک فیلترشکن دستکاری‌شده هست و به نظر می‌رسه این فایل یک exploit یا آسیب‌پذیری قابل سوءاستفاده داره که می‌تونه دسترسی root در اندروید بگیره و رد پای دولت‌ها در نسخه دستکاری شده دیده میشه.
حتی اگر نسخه کرک‌شده رو دانلود نکرده باشین، بازم برنامه اصلی دسترسی‌های نامتعارفی از دستگاه می‌گیره که نشون‌دهنده ناامن بودن این فیلترشکنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PpCCVQJ23UEiC1qdJufXrRrLC7H9-5Yl2bngnzVxCjqxjXh22xyueSBL3xgOuoNQ1b5bdDbvxuTpYBrZnUEo5B98tiUj-wduMNjiYsSODmxHjR7AyCV6f5HNVaJAdvhrRONh4SUctnFihLdAwToy4R54WTeZmvix1GpMdGjGvbFkhdoM_xP-uuCkq27P29X-F3JIZTcKd9gSPFz-mA8w9lJ-nv6NfAQp-SkgIPfgDHkA2W6uT7Xn4mWDlSaXt5tuBaP92ZlgGlL-4tKvC-LXIzFzRxxH9wnnd_D14chyG6MsmprjYBy4bNCb8Z9H8LWPoL2EjfBRTWVvEEXzrtU0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اپ سایفون چندروزه روی اپل‌استور در دسترس قرار گرفته.
👉
apps.apple.com/us/app/psiphon-vpn-secure-access/id1276263909
💡
play.google.com/store/apps/details?id=com.psiphon3
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V_qqrFzvRf8Zde7S7MhSXwUmm9mgUF0ZqMocv_Lv1WvexyQix2kM5wgDKds-kX8HtvdV70peGwQpjKGcMopznWOLt2e-tFxK_qRNWohwB8vNZ0Uc9FC4Z4fbN7tv2Db9O6uyV6i91SwI7P_WWNaDlqXZmp6VhI5KO4cDm8nAMr6vzetRSumKzTtZomDGfOXs5hJd8Yg8mY0WAvg3lVZqEjuXMHZrcu9EVuICoC3n9aKlpL5vtEkUVeKqnZZ2kziQxBYyw5ukXlvnEDhTYqKTltsnENCscoNZOJAMbuQT1bLS1EV9nDxUDoNruQ1LeccOSmi3GjjDzCTIQHnh1hHiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8EHfyq8HCd_28uYJNUpv--srtrePtSIcLXBlD9I_I7Z7LUZwrTUKrXcNTIJqz3nx35yNvO8feSTqIRrr9-GCzwWX6YvxrcxMI1feXj2psOnq89mk4WU7HERmUXoQYTW1pPCUHP9IYMJsG4vUdep0MrmErIlOzRhJWQVI_WP-lIBtOiZ-k08AbpMEqPf24_MGIjMNzTerRhZFZlN0QcXzkeDYZsAwwKnGqcOSdCnrDzJP7Maf110Bjsj8awvW7tbRC1RrHMSdomNEKJqUVSZRvrr4JEtfFCOVNe2gUtXF5mp7AHZfnam9lNcIqxv1wzizYAJfQyYWjAYovuRhmer-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه استفاده از برنامه‌های PattN و PattNG برای دورزدن فیلترینگ
📽
youtube.com/watch?v=CnEQipAJ2hE
💡
t.me/ircf_toolbox/25
©
𝐀𝐥𝐢
👉
github.com/patterniha/PattNG/releases
👉
github.com/patterniha/PattN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aEU6S400Jb8nwMG5w3hNL9RGmV10aDR4DSDg8Y42VDJAwL5I5WwSARC_bRgpSV5FEc-PZdQMvYRsQYJNdo-F2FiZZdNwVFvmeXoMgkncPznXXRXii8BoTuEv_bSaPrUI7UKGU44ANsCQ54IKIVQHryFuyk-n1Yh7tZgSl51onQpSJPR2MSGrIcWjovli43Rf_n0NoTYcx7L6uTjFK8Q0gezyps7jtyjCJ98QWBViFgWouGurSc30gFkk8cxEewcJC8utDYHA99sbCuJTjCc_QH2RokmgtRxlqMtedVEv_Zpjb2y3X28KIpkw1SFlIC4Mhtu_P4G-r-S3YrnP-J1WXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از هسته Aether مشکل برگشت آیپی ایران در متد اتصال Gool رو برطرف کرده و محدودیت اخیر دریافت کلید وارپ و مسک رو روی بعضی از اینترنت‌ها دور زده.
اگه H2 روی سرویس دهنده‌هایی نظیر ایرانسل به هردلیلی ایراد داشت، میتونین طبق داکیومنت از فلگ فرگمنت استفاده کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RvKb_gJDyMVZWeJGv_6sYzg7zrzz1JgnPNjWo0TUhmowgoSJRZbrEXSppbawc5szpcFRWLc5L8hhfK_yH6gEpycfbJTaee2aGHrVdZEDmwfnOllHIWwZMczds9lj42s5gFuTE1gb4YQKgg8YCH0TAwCh_Rd1cmes7FCWZg4iDXRLlVZeSlDCb6a8k3Jp0Smazvg19WGzv0ckuFvqKK7IghOaVxDfUgv3e7Tycjk5GXF_8WaIfiO4sie5Nrj3VEjKZrCq943Q2JacGG-p2uG613oEoDCs2NQcRVRb-gGqAL2r3tBhhTDAXv4Q0PP1T_lapynnijLiwmoG_xHgdvm5dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qj0K2zyBwhjmtROQC5hKpVJDE7EW6UrIqnDbzxa7XV5MHx-J20TKVYXymO0LF--T7iPB2M6Dee0cbnxt7rpRUdBMhfjUC0xqYUvs3u94CYajFZl9dPMHiyYiUhiwvheyd-Ga4GxZ_Nqk1_TuGHf1uocusoqndUB_JigmsvHEjPJlw2WCmaZ2beM5UAy2yV4o6xfc07x0IOK3hNjQw4vzfCpGe_kMAYei-Oz91ueDa7nJ4CMT6nGI2I0WggbickyDWl1HnL1k--jxlMM4GYFUPextIAq9AtbjHI-HbGXaMCAw6__zjr5GoiffHVwxASE6qsxyOhkQtsi9OHQsN5vwRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/reJpRVcbZaDFkafvH6bNkRDW2z7fdsNeVCzEAoTB2mw1aM2yLFop4Lez6SqCCKYStAPEctQf7_Y6M_PJOQ-PwxzgY_AJsWZ-hXf5-pE7Hq7avz87FXinYETsR8nIz8EoVEh_yFdAlXMABdnV6aV3CHMIHBSUNSzNda7TVQiHVcFs-bX26ptuRQGuo-MqfmBtIJa1IK6J5d-kzgPVx9F910cHOd5MbQgdUDcekFShufjX4v-1TYNhPERdUnH5LEItLjnc8Jpi9jvCe19PRbQ92sf3N8tYhtoA6XDnGyd9qSj_umLYI2yWHSiWVCJ7bSYOMvXZqNhFpCqoq15tROc3-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I2MvgkCYc_1vPXKwtq73jhDA1lhyblgFPA3oRoDuKniFoTYZLG-Fd1LXmpYrZ2Fd-kgkHDpg--7Kby9sbdfVVA8z4GWyPTt-O3d47Q67wGORCH56GAjJWCxzrZk5WheGelP85WANmyGWyiz0e3pkV5pXqPaT22RK8T3OhLu8sp9DOz0p5hu3RGUPmMO3htEQgzVBymhaEvj4mZLe7hKNwiU9PdF7Bnj8XI7PAnOQmF-rzXjT8f8tlazskYGn94d_cSxAO9zy9zpsq-_q5TZUME8yp8s7CtdVplXTUAyiQbdM4B434pRgpFI_dHOn3s_XjPuN7PkQbzG0DcA3-kVmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ptBuWBo-NZ7eS0GTOJezkgHK-nNkxkdfC_kITKAvEtg1_MI5pAzVhrQQknjChPDtJFjgw3GCyXUUKiFjvaYyWUyQeYnEZ7h8rf9Ho1ljA9c22Ql7PfVnJ5jSY8kPLm6GJ2EqN26xYKmoY6IOnBbgSMXYJ9p2M63XLc-XpefZiBOODNE-RPIKNAWtZNBzUghXFiCgGBRtIy1s4gLFDJcu1kLiX-dgiardZImeI69eM_rCdR-qtBxiFPQ2Mn6sKrqAbDlTZYSQes7pa6yrL6rPrxXZmg0quQyr9ZlaZAzpGtTmqg2YqpU9tHtHNvLAYyVhMUoGm_7wiDD6Bea0HYNWMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C_DXJafBA02VFNY4va4fjnZ4W1mAeGqs2mUGoZDEGn5pmha8GGhqQzEKEPETFQaUtGuO-UdSTkvVHA6KZqTrbkL_W-oE3nXywG7cph2fh7AcZ6aTjv1lFSeIrcTxpkwqt7se_SpDT__luelLrefEvOMf4UUWyM8rLQTvFMdFEkQVlULI7ru_sSkiy3UegF52QwwR72-dHcLzrMVUjG98ktMkz3412aEdD8dLKZJL8XgCsDjVeCv_6AbxkqVHRiXOPXDYotnRp0_q9Lz8yJh7IaPjxLl8v5a69Inmma5hu39Eyzlv_oqBesQqmPtMeuJcKmY5h-yOkkRvsVpsSHmvUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hpeWUrXAvIRl_AUVU3Kk_VndbTt2Rf6Wno56hzNug2YynzCSLVjR8v6NWldU9ig_gvy1j1S0FIMP0LTip-59ZfUaDFOCw7_Sr0eXxKLBcrwk_KsfzUPVzWOsRmUHIphzVxly8wRjs5jf-93_6rRVQy7gkZ_GpEnXLGM1yRkDyOkdBwVD3_an2fXda1vMuGBSKn_F7g3IV4A2VeJe9rEi2SmRx24uu56Jd8paMaBjEMZWJxlEvpG8PzLendxSBIgFcCo5fLMxkWtVWJ3sKW6L03nF4QmUvJgG2rgSVCSZ-Y7pD_4QtGq-c2yvaX2LINUarpF0-DS05V4wMu1dixwEHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TuHRCL0ZDlKEBy0Fit2SwLhb69QmmxXirzwh-z15Wu6o658x6LeAx_FOJQamHH5PPZ1oJbQODgKmOyK7Ri4eQvjNo-6qF1vpf23ee0UvMeZKx4SvyvFZbjFINgHxsVdvLfCOhtdobUwakZeX1gcWsB1zjlyH2mj7ul5KRWP-rpwVOnCypI5aG_LHCtTuknn8_76MszOOoRPaeYbVANFv8BqgLPNit6HqnMQ1GZAQPteSFyY6xGuuxluF41VXA_dD3D7h-OCYijXLOURPwO1RhlRBBG5I62f--Q-jV3ARNuu7PI1P-I_-LewbD0EehublEMOnSsVu46kFLg2LogmGfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uk4HDZfINJkrdDVlvSc_OfEavF0FQrlYmIUm9n8WcPI-8WDQVAU5dId4FBYFWrk4cbgmwipn5SW5OrWkV8WdeIAcIiUm_jc_EFJQsKQuAci6-AQoOB4FU4z_13mN7fAtnWevdZ1qMVr8tZ9WZM6JHPRNxdoI-wD08bmqJqun0e8S7-DddsICbO3hQVYLWJDB_xR6npIFnFaRfJfjF42q4ihCmoxkHyrbjtT4YNd3cnCMEIwNKDrcR2rz16bFApgljP9sheSyne6rO1_JfSA4YciHxEmpvL1ckJK1N5XExtPk3fngtNa5tTAKNp30oNjZ9FsCvq2-uzEvdMDXcL3uWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJKo7kVxsBW1BFVLucgNa2wV0enaxQ7xoyCuBuLBlpf8XuYiAlwuMhptTGjqoHJt9bpeT_Knfwit-YXJc4DPzlYXKfGK_wVTJ4CHdHIiNjVdJY8AJbmOf1zNouQO8aH7ADID6_Og927oc_C28kVbueS3ULFgX2lI0pQwavI_LLioDlTLbN8jOTuFCHkXDhex1orVZFaQuzX3dH0WoZQOZGoHh0PyHOMTCLhVbv8eXHDsGBmlnwQtWYmGV_aZheAtq1vfEgamn_3Q4y0NYqFoB5iTedLy4tbMwtaZAHRadvwytDUqxGMpBn9Q0ToLz7DIJECC7nggKG_fDb6yZOfWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AoNgLOd3VX07DGXPABGgg2XuLwzhLpIYpfAT47xFbQvToEO9MtLtbYNFWFmWSORQbYkr_ShDhXD7VdRBs7_fpdRwPWMHm38wx3KGglFTHjpPraX-p2ZNElWqvDnwmDcV9maMKUbEgXuKDlZMb-qTdRop_XzDOXA9e2cUx-xQ7JjPGOOFyc3JWZGjjzmGzzNbVWrk-B7qq7R-I9Y38s2esnOJyhJm2bkmJ4YQEiJNUjCF1DpFpaT4DZUZDyC_3wFPZBzhvhHlurKjBvMJEr1O7HSHfuYgbh1JJnqFct-Tl9TSE4ojoHmkE9DEBm12fnCgdbfr-HHFV3oOlF9u0X2UaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mjTX6amxgmC6PoC_p0NJJfnOJfxlvYFezt3JGNiM6JunAk257TQ7lI_yOKXFsK3tXP4vOJhKqLDkZZc4WJKGkyLF7Jm3ctzyBYcPGGJwC4aGhmXpdMi7M8ROdqTsDWjwYaqprtAIZLewoad8iB-bDYPsxWk57wWVhKI2KvdTrxuQcOBo82wWyvnLsUYtOZQnJbHQrTvwgx_UE4GVWqIiqIEE2cHHZVyDALp_pg-8RZuo2ztzympUnA7C2DPaiYOYNgx_T1C1KD4sO67IQHctzV1R88f9zOhb0iw0snYBnczCnAQ0bH3OF7Rt5JC_zxXymMtLYMYBXtYBGYFVgow1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XMcDxeedpjkWprcccXB4wcBvQO6npOgM2Qs39Hhzo6jJMYEdlnAzCLz9sOV76NRsyvITzBDYw2uxOo59wNW6BuGkIsOdKpqFvv3lw_XVuds4HJ-yWDD06SIcQIJoc8Cel4GX8Xj0yhsSldMGVPKUEwFNPPK1VCRUosu9E0qk3O5ve5eD_6EfhK2EKTM9ZthP3Yz23uc3nDQHlKqcBEtjDMe1qoFNC9NG_fFQuvwr5n3LBOTJmkLdflPZWOvzqco2ys5dcgEicfYnFoECzgN7A5aHPUcV--NQVblTvg-8RU0Llce5NOHrxO7Dz3nq6RDQIQ2PxzMRKP6-r41tebWJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/By3xaGVNMo_U4b4njFWdjeeK7Sg29N5VSZ438ntxOq6_9WIe9cWAHbHXbhdWuHo2W1-KN_7stvvtROlEwE48ubFAMez0_jiUlvnx94oc7-VLgqRqRgsWFI5k7_5WtzyFRnOB7SipcRK7wGune1my82Z_D8uyGri_ppG615EtelOUvhEjK2j4NpWpJTXSg-mVWkNOgIO0dzhBYxZmf0cMDz2ywLmIhtW-Zqiifwuad1iL-SBvrkKVp4XjEITeY4eIi6J4hS3h-STHSgg35gIGKWCVCGNbax4RS2SvnaKMmg-tsK5Kl47_cQRUqklgnq0FFoP0qYfN1LyZdAHrY8zMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e68eI0kgBDcCOcSu69CzzxvtQrpwHaeYPBFJbFobspTQatfd9-7pOyBudr5RGrJ2Bdbrr_5QPOs5LyMPaUu-L_Y842niIl9ILZpTrMttnvnbCxRhdUZzfp6bAOc2eViZt-X8U12UrXvCGIw9nUPL8P3CY1Hq_aZZOopUMpAvjTSOvKLiHHQVf8PT2iC4CMlD2qMHj5vnP5tHbUno8DcsoPhbbHt9906h6tJyxNEtfAx1fLSJLdn6-JAKOSHboU-9-zzvdoP8vaLNLwAONT5ilrGBOGK2EmGcoolQzWR1fCgLPSw8nSMgicUyTPYPy2vE2b4D74ZalZVSwXzNULXirw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h4Mwd566Ubr5qEa_3cjg4VhpgK06H_3xKwrZLMm1GgSMczk5GlPyM6s72hQSt0ogIXtr_JBzHij_54KSfasBubP64idGB3xdIKL1XhKAGKu9tiElfB0Zc-f9PGMPoHo9TRfyXv1zReGlB9FDlt-LxEHaaxX2Q_nk-ZESgRl_wwNX_OsJX2t_R0Z5KVxFjVDQnP4Ej2VC7F_DG0VESdgMmy48CMuwiMq9T27iGbrRmOUI3bf7KpKqRWr8HCKruLVEWDlYsiIyJ5BU6wrQd9RJZFWF8_oLzB9hw1zjTcZpnFklF7QtGg1s74HfG6SS7r6T-5oiI6NzgqS2jYFIld1oNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cX5aj8h6O2_LOCrbhHW54oZjvFFPM_aYMHpK6LvhusC4YzRM4LXPZdNOmm7RCJ-JaoS3FA6Jk4u_cwdBdLibt2iD7XrzQPOoQDlYmq2wK3Y6McbEm5sZv7uAsp7MZNz7T97BTqf7MGJiQta_pbGscODRnvy7pc_okYL8cFwezMTQ70hHtuKfcGix58nHpWre77fZsb9oVO70lGYpTD5bwR_QtYDVXkjFef6xmLsUrhAmeltdEzwEA03zMkmsYi4BUfAUX9gf5XjJZP37vCxiDqVyvG95VakfIE0wDeeEZz3co1LvAMPCXxS0KQwOKPqESqF9-wNx5UC0Wt02DOsKHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Skd1T98aaINHLsQJTTnjEI1CmSl-hP4LykaE6CQsNnpvto1N3tr_tD1EmbsAoRPeHCh7E6qoZXYk_QvQhjlOMFLqzVh4oX5wYkX8cKEteGneSB8qMEOIsvDlS8BMPGGygNZEETcMNkSUKAehwLesd5NFlJF2tmkff6UkuF8MW1g4Dv1JyXgwj_1GTGwkCnPd3BkJPSkpob4q14uwuRJNEhdZsCzodI-Xsef3IeyAU8kYEkG6wT8mefUvIPNohAILIV4BubecPQFxFh4atlmiZBX9deyzIXVQhwAWhwkFSo-xEYq7R550Q-GLoeIHRNjmdRGDW3HxsBjHahXHqxbHDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tukJCHQxw1UqNb-gECFdiNLDurEPjUJLt8SicxnfjpM-vcx39irpDdVhvJd97ZMM0cwrjmtIVnlGCjMy1fOq81gC6uCeZH-ffT53_kciqxiPkcACnPVKuJXefjxV3d4sEoWegw-3M7tH7Yy0eFUdhkZge2Hgj-FtbiMhcLZ76_yHsjmdnsIyUclDRCI-G9SwCc8DwQKeQh7vUDrhwLQMsnuaFdknXSnfODijlpz3tL3wXAiRMtvn1L8C3FVhFvn0vLkWDA5zC2yz9fzrxpFUybSnQ5h_P178icUt_CR8s0S_pnBXyGWgVpFKlTzdXh_NkiB-pPbhXtre9pTq-aBypQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJfyO09kLpPGjDp9ThiqdMb1FDsdjI_rbUl-AU1FM7GaIpMFYM0v6wJAnd697eP0ij3FFu3VFsi3CQnX2q-xSCSTOnfbYhMlzgbOMnRDDv0VTtkwIdrqRROtOoSFIN-FX4_IP_I7zUaGxNPVPyxuX89x5AVQZc8iBTLFfBURbQqir0Mo5XYUvTp-8IqRKjIoTF4cczUstqqIudVSaMBPOBhDgfm0_gQd32CCK5Ui_iWuKmZw-X0HbuYjWDHwgObyoxdj8N8wHruPramtrkZT2je76AszvWOT3-Uy5ORgDhxh5obwDCAeHnhTpNbTG-lII8OQLMaBlMch3FHSS2i2zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EpUV5VMlq39Cp-K4yIk53unBNGgZHcmMPNMEmfBeF0r_tvw5AMGgogFb8P9x3LALwkTuz_nmUlsr490sSRKAutjD2dayZy8ciXeMTKD060CmdSn-vwGE8JVzLJBCgWkfbmIB5HoGLzZCHjkYQSqW89Rgu0imqHP9nX59HQ7Uam_GQJjTrRZzwrti_AQUqMB_OfYsJWEsH-LHJNMQx8nSYEhPLx3PEbgBPSyp2EgLYRiC2hqOIOFsQBWzBpljt5-K55Iv4qn9APFAeTq78DSFEQ5OsB4FkmJyuLUycGNqe2ID7Rq61N7jUcgZWtV1LTnqbTgY6Rh27BSPUiJZwqOxpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kJf2XVVhmLgNhXreLH15MixXfrLtZGb0BRmZheBcSQr7eNOHSJcU44aTkZwUwI5lvCbvV5swB7KV8dePIKs5tQp_Jumw940pB4JqV0-d6u-KfvpiGdl_eY6GkjrmIjyMKcGtt8oQd-WEHV5Vr13D4-cxV5ciY1BEU51iyUkSCWKSIDlImBDTJ7CQRiaqA7d6ujvggMT1qoIjXcsfzTcp-aqaUYLU9SIA6Rhe879Dq7TvFIvqwEbQb_hSDzKuI190KpY9xmb2cHA3cLY-5NaHJEJRM4EoGkOn2O6kL6TqsahzuOoZth8Z4PHo2AhjlaZj7F6hmrqWCCxYzHR4nGZCBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gF6yq6mk7fNSY2X3JEzrL0JLgnqfqQkOktYzEfd13UesTeJMXQ9tMF0z0BylezpoI6lytwd8aoGJC-Q09L_yTHakvKy_ANnHWCzbocYJ-sgLJXhLmOFEuSlLt2DArM5pLTaI2w_d18JZNdKfP041_IHWqwLH681jWZ_NH8RkkE4PfWH-n0r4Fb2QnHmmfiJo5vKklVdz3OK5q1oCJYQxVyi6E606Vl8uRPvFjFa-85bJbj2InGzt3uFI8hXAD39xKd5Kgney4Iy6xLHtLvP1THuU_ynFyLn-UC4E9pJA8_rQ4fg27PT_RSbgnFD6OHULedXsvBVPQSmmacf-wjwh3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZvZN9szgy8zakPHXSmjwU8sOaH56bYHXHGmM6HfWG4oeORFKJVg79PLRCb6ula0a3OAWrKPDqurw3qIyU7Gbln8NuHGHpcE1DumkklCLp5JTqqilKmYI0X-P7WJLlltCIyg_EB_cNLQNkup4Dz7KT-x-mVguYWDA2AUa1bEk0oCJbgbC-VnZqbvJoW3xMrnCck1xgvl_0MFp9E665Oz-cSEYNZKHYOxZBR6qWYjdfqV9ytaZkJU9HgXvQrg72lNc15hFDICXParH6Yqn_rJicSt7W0h3YI1cfPBPRXdARbJbI3fsLXdY5NSoRf5MkCUkIgRLMrG_STkqZSTvmJUg_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A8GQ2qixtCs-bVUfbYKX5zwTG1sy8vDTmWHVeYAZk0ykYmMENI1hcu6Wn6XFJKROWn2CBNNIzR429DFajY4j6lAL8cagtzNGbYZL8JFw9EHzsvb9GPGm0dYf4sKROCemh_YSm3MxEnH3_0EsYtlQiau1ANCTT8-lN-4VnEA7wmaKldned6r3EhrGB0fhzU8t_Eq0sAmRkI764CBPgcE6XJK2rvpNtaDyPvz_pcUnGrcKIpfGL3vgwIZjyu5maFCpi71-RA8bL76U5D_PqlWABcCRpfMYlv6QcqYifniVOkBRY8t7YRMyEiokOHlqCjzLi_2xQylLjInZ_VqMajc5_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxtJOPY5NwdEdT9VvI-TlWCOAH5jlB6Fsup4OCU8J5Hc9R7XrKpHn3lPQqVkUILTwd0yVMgGRNm807ljzqaDU-Pm9AyHDwS-7en-aY5rwWx8b-Re4sdVnv3tGPlmNDEB6ThMPfe4a9Y4u32U7Vke2BtKjLieujBIj5H8OyCNCJffRXYH4Il8YYkbUdgdrdEe9x5SMzpKwUsdCqdGzCB8nHCLx83RbmSrtF2MDdWELE5NXHdDouJ7tFgx8iKkheEBvSAn9pjXc_7gVQRkeYxqaXxnqzriEVROHca_47yj4e-ZA8nu9nfb_CNCnR67yV33x6lfhhr2lDcHB0E0HVw8-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VIJ_cI6hzPF8jy-HlfMPGjoOLcuEVwX7FdjaK4IwbN8Y12UnVY8llXxXXyB7iwJxZ3RtOHDebbCiCOZ4IEfcWoh7ezfgSYDbYfdpGsi6ZRJYIRreiSnbKgKYwBS5ckmw5D_9cOx7JyP1JwKw6L27trKbHWFjVUDi7wWCa11TWzPEKUqOAau7V67i8bkJ8pM4acDauwyQ8I3ikPHEnk5jx9IMVWIZVe3oeHtaIiNgsAfqVfpB6KqYFKuaZpb5WhuR-jrh6PtEQNb9WQURt4IlUwAFNVDJHB0E2zwutVKo4mfyFRAKqgMv3DpQ172JhmSJ6SPyE4-OokSg5MwDLluRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BSw9gdzjt3vAGsebfH9YIHWEutBIXM75_Kr4xinJHfA8h4EYtN-v0Rh0gsdUNGukx1ehFsSr9-NUKMkwyhrxwlFapM5ESwb2d7vC4zdHpGlFo13jdZvoKOKrOJxlEUYG-wfaYvBUdAyp4Gxf7PX_DWoSQYWShlTD3WJV9JJ5ioZ1weLWDbJEyKbPNKWgisZU75bHzDRb1sd0SzhY4kLHcVtpcct0kz-Nmp1gcCKcQBTsFh755tUU9jZJwXBKv6_UBkfDf6IDBZgosAaZy4AFa5vneE2yxEWeKNmur4wws23PWYKgauPrlgYZHmBqx02EADNtp0-zxwERY92tSOVSGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KVPR2SlkM_81p9bx9HwAYNep6ejZljAxLGwOWNcFfbijNKP_uxZG2S-fZu5OIQLqdTGInQ1OA_mQbU1uvcbLWRR9QfHh8__BcBnaXgDqhxJ9lNojOTva1CQcMd3m0nboUBGjToizxnvpR1_jEzmP3Hh30wayVGwT5T3fUTIn_tF5Ltrt1LlQn5Zk_E3kZi-yZsh_5tqa9pixE0GTvZZIcK4trxFfvp-hYUcnaDef8Lv8jOPE4wvod6E22NwAajccjYIJlH9MTGFhMkxtSGU27_r1ss5mrhf2kEVleFUpEivvnFLPwGuZn281DDTFMUMIZQ27cSrHA0b8c4VoA0AxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Who2lnF7LSvGg5bEKAa85S75MsL4XGWon0Je-1vzu_7piTyL9IclIE9xtPQIwr99uU-Ob-NpLA1sBM4XFzT46kRMrlebvEk-QL828poIZKJFp5wgx8a56KgPvAj8cGM42UbBlAFVGKWvGw8G-XwcO8VC-g-LiayBPpLlCxy8jAd6mj1jvVQ4YEywRsvuBU5hOub26T0HeQUxbiJY_p-dA9AVTkESml8BxiVKjKneRIy3KHm49y_YWTPph7edPnIuptik5T-al3ulkhytmFGXABTzFU1sohTqkt3dGBAnutcJNd9cLsCvW2j6iXJ7_zI-QxbZFL3HrRI4dTJC-ZhHZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Op40JhIvwKx8Msro_FL0ukHJjUj054af0KmAQighuJFnhm0AWyu1DaZM4Dgbbptcbe4sHFn1lInvOmRO3jUupUpSCMluFDBXGhNJC1ymFJ9pAqhmlmbTnWEJFxlLt5anWSDmF5xA89FSlXqt9KTwQkKvUnUTu06WqzZjB62mfSZ4Fz5gzEov206QKI0Sv1FBzqiQEeRc4UAaf-sRll24c1TzKNBR42Br1TYjvZZTLshY2w0p1jIDMHtvHgglR4yEOjaeOjHGsmVINQvXLxU7CSEyWpFUi-qMH6RLQ6xSq6PhmJadItv8-nvVscLY2StU782AZpofjpVQgv_3SiJ1AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiIHp_xXrxkP2ad4RSVXJDlKQN81ZMEKQykKEo9CMT-t52jrIqwy7fgc4Rp9EwIIpW-02jpcPciCFpc-haXum-faeEw1Rcn3aThbtoVTwIfofdjvZEQRHtZg1ceCGtvYdozv6SQjxcWUo8YlkHNWyvfYRpUcTxkPebOP-8DRU_CeLu6Dj0ua5JFJgfnjX_uzvXFkedBzUm0FtCd4QKd3euwgFCSdERxjLemI_Qu8qZyoP48Dnj6zrEmC3hxohUdE_tKdWNaN4oq0eRtAedHqTve7weyc21MumLaJ-HBvnzCfnPR2vYm_cilE-xwC0rztynXKBkENcvtV_UwXScpFhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O3P76T9l0xZpfB1SzFDc4eO59txoGadoqWhBLKXaH_WeVRbdykSLYLPEX6gtJfS4XuR0UBfex2SsaanrIvcTOEp9T1Ak5gWyIr8SNnHfM9KRQux5A9zX6xiyoTJUDJSm7_wz6MZADnrB4xCoyjf66_7gxLQ-rwJED0TtzvX6m_s9QwcXtKd09VrxS3UXV0iDT_au1Uwyo5TT1pzzt-rIBh0yk5V2_E_c1vVzW-JcFcj4EUVTPoSOvfO85HXK_nmytqAMNPXIveSgS0IdWmGrQwdPK7jcVTzjK75IcvkxM7Ztq3kDevbhPzE0LHifhleA6SUWD7uqyLYIgcadjAkK6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aa9eJbApJMEeA0SS999sCvkA1cUqmXLgv1Qhek4tYqFR6HPPtPyZB92EIAgBDQ-xC2JRad6YT8Pf_1ksaDHRSvnqIEZ3PHnIbwpauE_rXqnk3ERrDLAK0k9eGpQE2HLRr6O21GNOGb0M0Xxd3pmskY4biQUkIg-XOmkZ0emZIYH3K_AXjeZauvyH9-9hcYX9LJOOKj5pwrXsJQbv_IbOu93ScdaTxtsL-Zaf61mX40WxCixwHMCZYfYX_fjPPB7KmwLVBFQv3uj3_N9weEuN4S2Hj_C_fU0UljIz0v63mQOdX8P8qxpXCr1M6u1DydjZAfYllKNKX4t9MzTiX2FSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILrR8Sj5TsaNuBzEeH83cBbuIqzyESe7_4Wum7Kc8JKzWcpa9JFm_QokAGxeqWrS5eiOkOW5FaDBh_rHgOSdUjyDPV6jn8NpU8rMIjlI4WQzI9w1-x_2GUVJSY7lv_3HJJfUXzQrQeXIuN_yySBhQzFnbePtNyXUNnpcUZnpOqdEHqgPJx5FJoSgO341CZlxaQvnnrK8hIaAD6xIh3lYSiHyg__maBJYFCr7G9bLzlJp38QDaT7wV1bBErcslKPlbur5NujT88ZYXGwOVnHBLT1UPtODi4SEsN1rXRNMpvGS9vFoo-sKILghYN08TmvXFTz-KGfQcV-EnENEJnCnYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p8RvPzAEfMHODGv1mGruRF09NfBUExeYLlVEAkxeE_SQIBtQhD8bZaZy6w19xqh-1oTpRJipH1C3MsVJdXlFqSYG1fhoUq4lnH5-4-Zwu8kY1R89ZcYMlIS31GxB-Ntnhh92vEhb-DBy5uMxoq3i4ssK2V866XBw7KE-OIwdBB668K5cBLBOj6S4TL2Wc77CWYP87DUBWi_zYgZPY6k0IsQy3oZJPakAtb2eXmscTeIqFYDX8j4o87WJjnUCUgOnUlMWcY9qfqb2drWffnl-EbhY7sNcyJKuEsSeBVzodBtOT8toJv_Yq3wQhhi-aiRE2C6GNmFlzTKFL3-9Y0k0ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kjcd56x4lrLcCeKKtSFw3WWq7A63ZNndq8rGeSZUnrjPx7wLr-VZS1pa9-wz1avhan1vhb4PouO_aitgb0veFIrChyZgXysBQk7ce2-uM_4IK74eTdvJgyjnlxjdtXHnGtY43tBeckIXYXSWDE8IN9BrPQzyysX3FeSSwycdNQR1209peuYY9XNzGtaBf2Lw2_116aRXv2R07CpbmjFDdXUpAUPimOIqg-Pw5B3Yq_iwZ3y2FLeCWLM3_hTK09i6mqyfMntuk7HTEyuCcZ1jbw_dOXygjdDCXE9GYD4fPCDW5Si6wtnabCuKhjPiCUCSYspBV9zN72L7PcZsJz-5Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G5jMapJH_4S6ydLdpoQQLncAJgpt4kxwV-ucT1AelLnn8Ww8rSuDykD17zzHClU11oMBnABWen-cYQewazMwEg9ZkH0RHWFQVuv3OgCGvaK_7CK2lBNIdeGh_knGrZuu8LpgWRPuGwZC5Yb_JJ5llBjqvcbgw4PvdET5tNHHrUYRbtOE61JTN5MM0VqrqMH3rSOsyjCn4QvaD6wzuYOUBhAE_izvD46pGS8kgLtYPtsJOI555h4TGDZc4W0x-3g2Ojf4ZXDHb_ovC07ODTVJ73JjyOcPSxBvWJZX52OK4x684sF8XNeFxxy6He8YQYq6a8WXPrNhRwEDq6cDj9bq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FgDXSeOGgamjGZhqRjKF_nmtmQTdFCwiWSoC-SanOfPaM1kA4TFps5rkO6NngwIM6qTe4HcAeG68T_WnLrSR2LluDnDzEaS4cRPxSUzoTRqxXt1tMc3f4dUSCvZQPcYZOg_BwLqN2P43hZHr2uz1Fa0KiJ0VLGpEU-Zw0IvSusK0GmImnRqWQxJ1t66ZgPMPAcatnfOSV2irx117j_Tf7KfAzHJUtLcE9xjOLMKw0byLInj7vb2lqOm_v8jU3Xy3sVDa5eO2hguAsFuOExnMv6tCzbIiwFVHqV-gVTGZNaOuL7VFewmyshwFIpOxnEFqi2J2nX3QDfXWus-pZ9TfNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KX3Hg93ZBtgGekA_D8kKjwgl7QGlj1nORosd7d6EvwCEE3mc8LQ9Aj0JZ5f1IMwkjS2_aq6gG1oxw9dorZ5WMrmEAUC5Q5KH67VwH0GJFO7YbJl04ahnAMOf26G15lfjFAFdPKxlU9u6G3XG3E4nkq2lgDA1gmvCa0qEF1k1_KCBzOb7HURNbWzlvoJe7JGfcNZXXtaK2oCpyTIF5TgIvLHMOKbq09IMkV06A03Kd3eJ3IPTFtEPkNgeDDuJZNNg1_r9YsPuVhm6dWALOfVSDghPEzKL4aZJX36Q1V6UTUNXuNLKGqLemUQeT6UuHyEim8vE69rsuw0HA54VadGkxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HQszX0ByJUEYBXmFi3L15WIDzOjn_IBwa5jTJV2KQdqVTavdIh0iwvgt13fWcKv53C5yvVw66Wlt0XQJ7JO2R-byk2AN-bn-sb1nA21zsLSWvd_fX61bkrwtR4O6Sa88pUuqfy6zoX9BOERHKiHvlcnlBlyW0HaMAfaUIPtGWCa_Du6jvV5c1QjEm5r-MpESmXu9W2UOp2pPefdvWYk9vnOO3G31jSehSr1k_fmo-W_5ZRvlVGiuV__hZffpg30Lg2WyLC5TxSukLgSNKN4xa953fjwQRhls4kh9RIv_uMPM7ZBNe_GAMlKDj7ZlTYbxWVu2FizTY8l9n2kA0o3CHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dj9-fkwS5aqVXBlFOiYjiyA3_liYk3-89H33nvK3nyBR9dxNhTG5f2jRuOlNY_DG0chiRu4rXHij1GJzKQpf0wdpohlCxXRtxXffYvLjB104pZzGRw5v-YdnS9FdPuHEdvMxsiUU8i0x9rPUYy2hFIh-gowWs1bNIO6h2VTXDS8FQljEYQtnSd1io4ET8yvNVFXncQjbLLv72Sm_XrPP2vrGwxNvsHSSQ1PvUOSl69l7TXjR3ciK2A57-3mdRrooLVGJ0HaoY1w4Bnsd-yH7I6yYsBaRNloX1fw32HCIRfuNFlPTXHY21tXuKIv4opoPvZc_TzvfK14s2BgCRo7vPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbRmj5MJ6JCzk7_FXoFzke5HtiyuCTFFP9z73Go3qQAyNALyGEiVtwyCR01_Z6b0VS_kTItrkrKVS0aF2vPvTUET-EkIsffvORvL5RNNvOiBmjnF8-NYo1-ZXVSUFPZc6xhEl9dOeQNHNEZ5dLQiNWTkkAeMlr4DQ6PUTZv8ll14NiXiVffzeDdtEun2em1NMUTcrGSFEJOxCaPpc723r1Ic4Fzz5g5om0OqG-o5Xes02aytTLDvSHNFnw1SEKCvg6gmxL_B8h0ssu_WrBB3Du0zGNlsST3YfJbCSImv6UJ2BhH3J3qcxWDWT7nguZ4-_HeBuPppWa-yWKMkuhxm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CkzyQn1dK_NKqi8PObgLxWkA2eZE6I-Cnl4qQy4t6sREXbCfuyipl8xxFZc65pHjblXaNKMNsTVUs7xC3gKw7w-DqsT_JPB2vl2Wz2QeU4-bcrxNB5SHUOaZboo4nuqZ2gAln9rnyceyI_KZTplL2dsm3Lv1wYxVf629_Qn0ikn9r7v7HOBoeJlbwcYTHGa0Ey3KIltawUYpZKBEpGxfiKAN8RvkyU2QUkhwiE-X4IQZ6qrhNdhhM_DuDL-cS__o3mcA6VROWlvUHbVtFXPitnuHcDjO6TkKzGN54uiy9mQr5hCnxMAfwd2vucEWJSXp28eCrN3hwROHCiGB9QQV2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oxOZ-0_Fa03vYbsbQd5EQEFG8MHFGdgtkPUfTLlMknEm41KmwCdcdYtrKzLvCajmFjCGJmTJYu8-dlJrmzmbFcCb8Qw9miltnQ9cV57jifN2bPrWruSBRX6Pvo0U3k3m5Wl16SPKpPkI5RubWr-KZegR6fgxYKHV6Mh4CqtfQfgRRE5LnS9DAfBL07XZNqAy6jg8rwLis0t14pLLVy6KRGVzNMaev49mLViIi1_xA7X49LWx9aBkyAPFHkhHAQmpbHpTd-cHtRTb5qgk26a9q_yO6lq8M2v78_brsmlCjIJ6xzu6ES1_VNLIZnk2rUh4pCPFrM4luhnhbSbGLZGTdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IbTW9_QP4imiV-UGhhRddS-ipKP9xgFT9Hh0KQRBiE6evoDtBoCeNmNOgvl9-kU-M4ZZhDMQFscXjBhJaNIcLa5B6KW5lC7z6PYPpiYn22eOfBG-u8HpEb7gWaBnF73BE0AZWc7IYBDzNfrVC_FeBUxn_fWBX8hzPQ1bdi3d6IiVp8lDtClmsRvzxtkprV2PPy_txM_DnscHsvnuc9sfXeXGsgfzSmcXZXyImLoNiFMumshFmIptHLHtBh_kNUEHTBscV0SU6q6HfyHR0yw0ml8oaJ-BhvGrOa4fZeZEkAib-PSYUvue6oiOhe2rVfvKJ_yZ3vvCZXIkqLzBo-pI9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EDoLuwP_SlqlggcrX6vWKhal5BfD7IMnSVWqqd8MpkaFzK3nk8Grv1_q4mP5aPyJJG9R_ZSATkDj-5aUB017na8XjvPmj2zNCzqzs2ijVRbnnZNZ8_vY7JdkFa1J69DhTIqZAxhzd17wzzsVl-p0k1PpGaG3ZNZ_NxRdZo5n1iz5CI2COyEsTeR8HpewYrJN4aq6H20w26cmug9RiMLCyr5UHuRpugRRo6sQV6Scq6FMrKhujrbrj41oOCLFs-ngJe8hCThaq8VvotNMuVLIKXp2hXG3CPRzF0TEuPseSjsG0akGwVtrjcf4ekPoCyu9qe6njuLIhPOwVyXdiTXtHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lzP0S8-zLg2eo_jfsAm74-cG8uAxC8QmLia3mXWLUnf4sT7DDeh3PHnmE5kBJnQRSFgCWtVRfokQd4dqMSrlaok1be4KH_kgjrk1WtBSdHzT9_DdmsQr1pdoE5iUm4BjkWHF3ZylQifbLdrrDPxZh4B7RKwwTrWkTa2IZoZttkClPfZQakfvxv8HNal48BJLmPKKXP8nCP6aemKmmH0zmNeQxQ4DwqEas3XLkrw0TL_j5n5trcrr_s3a8gxKGKrdCrYo9_20oY1_vI9KG5uIiGwJTE04tAJTYazDRI_-aRams3at30xUKquiVlI-gaZG2bfzier00hKsAV1Jo96eTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OrbZRZWEwsngFWDF18kgSdJttlB4QTmRrfymiAKVd6jNBzklCl1iQe3ulK5Zzd0VwPidu1xI8Dwxd6jpsKXFy0ncV2aF1R5YhL_kLOXyO2Y2RST_lUeD9gxnUhWIU91P4SbqPRotnjUmGBpKEvLyETOq50HxSFlpRkS9aSNKx6zGfvmZ4Ig-TvjqklgiHcKakPlSYvkR-D3mL_vw5nfdtXO3AaIM16Mzw03OMZ5hL5BvjI3ZWm18mKVD82TpF6198pOrlBxBXcUuQL13Wi9um56-tB0NFzlEoP1mIKx5NgaWiGmN1sIDx0f9hQoBGsqb1-y_99jF4mcB-SZYFucRvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jBqC4hL-Jgs9DGYhl_tUUpofOz7puoE7EqNSjOBsWf_sE31h4XCNf6L4gpuUHZjs1JEbMVp0VqYEtaWaEmdS5rUI_HZMi8Xn2_CfqXm2t4cpVCat8C0J37a98nQgVVVKkfhWVImAX2QGftkxcU4VZISHCpPP-Wk9cwZ609RGBPTVHU8vpXHCvNumYWfuWDg91VSrEylWuxbU5V60lJIoC2GVHFgBZPZvtQRlcpW0CC8l6K4WcaLA41dlXBRmZzrVi1GN95RT9HcNEDGXJdKz-rP75My-natPSjDkEP_OMLztVGYxgj8Fwwwea72iBL69jtRowK6jLI62SDaD5J4Oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TOZoUcmzHK9Nnp-vjCIpTKsg-ASlGLpcZNMQc1UY83PS9gOqEDeYbMRyA1iXCk8oI7K1ip8rW8Bzvz9FnYELGsFa582jEpWuHv9Nnaue3BL7eyphngXeDAx687Xtw8G8FeivCxTyQLNaNokPXTX_Rbnk3BJ9W7fXNAz7JdSyHHpxXNlC-WHoFRnYUeWkctPMOp3owz5TOBhLyok6EQdVNXmvnK4m-s2SPY8jCo9fhQkVtVWeIliMVIFYMG6301b5KJG-1o8DqYFkStENoI0_HFpSzKrl_tawRtkD3vgv-6OJ-BI8R6ECIAmJ0tHCtPY9eubfYP0g0HIzvZDM7SH5Qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MUodCw9BNU4_k-WBk0nH6BJPVmoexVh5wHsWSilKKO80vt-39QKF5zqHy4SDpZG_H5coWGMk2xf0tUopgYLkg--Cu5fzjlmtBqie-vEgag5vGoY-wqGMiVeK1lozyutgLzY9ocRRxemv_FN-UcklM-tIh2aKFSNKwQQIcMuxGaSdzYuIcwQzqEiMtuGgvL2m9WrHIQuPvkLB1aI5zZLW3-snTLIEDxEuPWLf4HGDmF83IQsuUpG8pkjXeCx60jddAPkda9bjV_-O5sAVDHUQfpef3A30FvBJ1tuwUeHjDrQxVv6xHYMJ8sm7OT7zvlW7RwkNREtf0z41GePqiFpQqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hcTJ8XS0OttXj2ARBqc2giqkg4Nd8DJEvdXjMtdarxyLBCYW00r8KAsbDEyaPDikMzC7Tav0SHFZ-SSoYl88k5tFj57fntVfd2QzGbDvG9qQPdHdntkzpYpJnHdHpBDu3D1eKlbc4wBH1kXSVv3NsnxhxKVCtkERnkh2Hb4pVqmWgnMddL2k1Fa-VYRCLuyiG61NkvkmYcnvhcpS0W4T4fO42u6QYNxK4Zd8bwD8o3iE2s_GOcYvrI1sgkgygN0YhIYxXFbvMxnhiOyPosP4qQu98CvRgx9U0gLKVIAm61c6M22KsLsI34hF0a7r73BG6dJgnr_szJosS5wQfU3GMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nfx3Dr2O1zHp4HYGtdGxI0VZA3q-ET_GjdVPdyStsats4Zetp1V1PpjJr7QvCjf5MrzITu35Z7Qam-Y5frt-uYUx7L5pKCaSB9xSgWjshd4uiuVRK_n7XrY0Gk-6KllIW6qKKfR0QF7ySF_4t23SLYTauEEcUJii0Jwzqhr7JObVZcUD_Abx97NW-cnCrEOR8Y8y2iZ5n7NlyjejPBglzfZeHXDo-b2EBeT4Stk9nJ2f_N0Pjle9ibol1V-KFe09feWwDJMfMMx1wBMSbiOte11qYZusTBq2ttN6NZlhoh5pq2sjpKNPcBumcjSAWeIsrfoPSv-pPGdhrK5Hye1BtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOPUHT6wTsfv9Xmi66gktMV8hKzo0BV-Vh67dv6bH09uK87bEVLDpouMLBqjCy7_p41xIbYDt6Mj67eJjUvHSc8q5NGoYq3cJxHhbMX8iYXGvu6-qGPyLO18slKWzDyD0LE_PAef69vLzjD6ppfcNCipjEOU6tn7dQQcFpb32Tpx7-Bl9KeXAsJxypbedqpAWpQk1TPzI4nYjroJuijtz4UKzsOaPSTIvaBvE3u-yA_9WZV8WLBzY2P3Ih18GIg33BHdTz83n1XTQ2T8I35eEKPAqcrUwG8rqcL9W3CxeXNG1HzUWEp73MSAO3jtLSkzeWLKA9aVpHXiefHddb3yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J80hY_yG6AJ3zo9UWjS60X4gWJ0UzWJL2AZ-wRTecRU8VdjRAqCz2eDPLXdaYODHD7ERwkAeBkDsQf_9Yd-iH3rxMPP596Z_a87WC7sW35Tqnggb_S2wMjYn_vESRQXeURE8L_NcI-gFiN44C572QL9I6wdvykr-GJz3PzTMTwhrWeF-hXqGecyqAjxxuDE8sNJ95cpwYuDe929PXjk_Mwz9qWRnZ0Bs9cxNgEDuYiXJE0I9wdIHuq-081Me-XDeNOkk2YaNCl1sNaSu_xfkxSTKwcIbZYvIgXsAsmAinaKttGO09KjTMzcjwnMKJUV-x0eBbh1MVWS0Ksae4EwWag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhN4toftX1al492B9kGhNd2z8zb6r9HakVHg29IbeP34f6PV69ZWzFvvSQAPACbDMrTP5X-YVCsACNvJUPqWPvX4tvPaZvj7WM1D6k-XKacNU4wWSbHKP15B7qfErULyCvHJs5B1YV7jVCitk5mVr7Y-6fKzchImQqT_-1fkyEr1FYav2CyQSCO8QvUsNgPApJ557Gbn2QC14Y9VJTqxs8CQBZ0chwV8F4pitsSwPL3irTRJyYy37jyZkXA7pQT_ys7NHJh10Tm-AiodXd8aI3LWH5tcDlnPXtVxwKW6qZTiOBVmjJf6qR3eEk1PEs6dtUUy7GJXnumgj2pQeEJaog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkZBktCmeUI9jsddK8XZPShPDXZMgNE2fcIY7MtVryCRPsrTBF__Ba5-dOYnNAffQPCwrJDaxCT_CX_A7Ek3FT8vQFime9Y_dmmEF_Yxbk8jAfG1EWZlYyNeP8ajzf9QIvOda9H9JQMkdGM8Q-_bv4X1Lr8Z-85MqfkfPw-KOi5RKaLiL6qES_r5mUIiMgL0Z0IItYNM1l9WGk3ClPt8Eg3Dg3abD8otp9IBfefFFt_ChlshYlQgC2ZYK81V54u2HrMGq58_efQGLY2vfnvbShAkn6VNeT5p9BOjdXchxBNcPbxndXK6FsrdoDwM6pnbD0ysQSE5QNqzKKNGhLc5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AMqy2rjFgebC-xrPGxHTTmcgL6MhEnu53km2D6cw-dC_ji6ZLECQlDYzuWeXi_tBVVhT7rNBILeQHGOomnx6wrJ-UVEcypKqBru3PfoRMsyRSkmU8QJGQTzUUzJETUt67E21zRHnv9r387LHnXC5RCK3qozpSCXxxdIzZMUKZFMOc-15S7cKdWgGvBxERipJaaCnlaZsRLrSqEPgT5b2_1c3yb0EC5DTXA_7YaSDvR0bCqfOM2yGAL_4klF5wnYJbP_EXe25cyCMKFIjMo1GYkhnHWgar1fx2nWGyxnV701VkuoRtgCSvAkhL1MtgvuYfRAlVJiJ7va6QI1iX4WL6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cY2ZbuwTXvR8RjEega6Ubu0pRC_CIAn6NC1HQTswteQlRApJrO1KW7Tpw6ZX6ZTpbFcWOAzVWa0QA33ZvnOiN9cXt9brbQoSGlXAdC7WgA9PzePzsVQ071jZTo9hI2mAicP7byh8kVi6tIemGGvwu3UhVHwNdk_yb0aH3gCUNPIqIYthgyySv4y3bcXjPGLpHb6ZZKFvZzUx_CgPtmaMjCxm2tCXMWguCiYrKFC-eehIgns4eoLQGnkAHGO0RCayvxwLewmmwokI-6yg4p8bu1nY3SKjxtWhw4ofagaRqwiC15lD36ddSLuh8Kw6QFUSgooDQ2-rl2s-ENEepE4ECw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l3kMkwTcQMX6w1glj8UBfzZlVM5qXk5xNSjPdqlzrXPsD7xx9ND8pkK_RHHgzyvnDN25mc1rvxwtVkWuZkGz-dlsPMDUFcXRQS4QmQB9GAF9tLlU2ADs2cr6GlyB1aJN1ClzRlSZhqqJzOGJOrPyFYbJWcmNFQWa33skW_cmtHrfa6qdN2rdiUmEj5ulFo2nqI2hvOdJCyhH8Wt0jvf561KO_BGt-SG8f6Wppan37erMw7SYqnQHLCBSiRZ7MiEuMEtAS-sUeds_Yxs3wUKdUxbtllsHfrodjzmPXgoKmWkgA2dnp4n20X_cYMb1z2kCf2ltDVxvO1FrtDi7TQ9TMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
