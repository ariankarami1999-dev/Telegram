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
<img src="https://cdn1.telesco.pe/file/lndGIb41RoUiD-aY2bmZtVI1zVIQU9v3JT4hCpC5oDaqnRctGT8Wg88cZCvPtk98zEqOO6sWkre7FQzA1zNwgxTv01fi6Wq2VM0B84kp7ZXuMDN36ZsJO8CHgXL3J3tCAZI83j4lasTzu0yLFuxmddA_WJwUyBbgZdY8p-qA4JTF8OiGGZKvnipBnqDRDtzBlEG3INOFfbHrpCB7YpVqXTZQc4rMX9X-wRJfDdBT1WWEEpuauPn1CF2Hky3odet_jCGEqOx57p4EdVGLJJFYG0yBYCg5MTJ0scgcR13Zek_V0h5DsqYGzh7ZlcKgw1cMoE7V4VcNBCtL1oxRqb_uew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 01:40:53</div>
<hr>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qc3C9ScT2HYdt2l8orCzN0fMuH3ar7pUCg1AHWNpfwS-nLWog-j9mFP7qUpBCWCSJHz558fOKavOXfJZDjry1pEwk0foPAh3vvPYegbl68LDC__jbJvsLYL1rt5q9ibXNGG7gj9ASNWl3c2-P15q-igeeWNwSqM8TfIPoe1llqMl2XKGTxXTApn-0IDiPyipM6CWIT9d_cMCdR4dxUslMSVulpHriv1YlPM2vB6BqlgNxOZyYXzMUoEdt9hdLTHEiuWmP95g8NH9Or3Hzz7x93JaorXzKd6Awjx2YODsjCPbFsKPP0ZrfExFXocXEghpaCsIYZ0wABtqX75qLHSbIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUzPPVnbB4X7g5UOLosjtWImhB6hy_kleToOl8AY_OSr6b2ayZ2wP8qmZHphRbmlSVqbMe6rDe4KRDL376fLgaTscPXX6FgdT1PcPY60-4sRHK0fV0x2T09vLvBOwwsco4V864H50WOtYWj-z4D1kX521hyvqmeTEOGN2URVsa2xJsF5aeVGB0eYoX0wZDeiU9-Hi9QdNFIAxgC-odugeMvzQMrWsTpZykJOVWToNeTVndYAzae3j93wC_nwDKQ_LH8sMfPT6qec7ZEyzmcyUFhQd42pEK6LJtgmjZDBW1wkJdG6vLG0DwrfYrkzjgMPgEkzf4UtmPATHIvHYqVRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVciKQ5WcRefNszMmyJvNpUWEY7CL_gUyvsgkMkrq_Y_A6JV0aAgoUXgAddEG-fbIqdBxcxkbpyl2e-8bZJUh-iTxRIld5DsMTRfU-fvsZ_vN8UFllhITyZO-q0pkkn7QrdXlLcUyN_ECZO0ogZeNX8cs9r0Gph8GzoFZ4hdVRicAD53JKxU5gL9Vx33r1x8q8mLYTFs62-x-mR8WEqZCjD-rGSWkOl58ynLHTeSrCWzSLkKnfUyNs859pAzIhLwuUN-InXHS1rwHiuN8NeR-nuLDUdiq5wpMTLHizYSppvlt_jEzQf8bogDIGOWgeHw-HVyhZnldoGv2coKx4nNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HrliiUaHOOZCyf1KnjW1hm_pUWsBzKlP3pYQpAym1aye5X3bWxgjNTnzAxKT6r6CLjy90KJNaufeInC8uPvjG9aJfgpsQj6nEG4Dn3mOLiN_uiM9My4cCu7IRcLztd83C4kkSd01LBc8XXo200lXM_C3CxWHWJyvCu9NCL7F8NBQyJ7669E8zlb0FZF6MRw57ZRkWN_EJ0kUGAVuMMZL95KBgUYVCG_vqNvXEg_a7ShwrRM8e6y5NwfVS4OhgPPeOmyJwp4OMlEXfXdJ1ZT2lFacXrBpLAZGvKWG-Q7RXzYW5gLrrofMCi-qVFfPB9QDW6uXpySdcuGVf8TX2COpJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uN_4_KIV203_lhkUWd6WFi4jYn8LyyoY1H2tl9bT4iOPn_c-f1nvTLN3ZqiH-BDhflTUjQnVIQRdBBtKF07Dtol6QLONirDkWJk9gbHFv9dqb8IEk-Fw3iQMKOLHhGOrlwqdHfjBJ2Wrz3EOEwX3SUi4dW-43LnNdCr9Etdc9hDjJlV5zqx0gbMyCkw24YmvtUAbQDqnNBazr0sIngrwUYQN19puYdHOTIGbP44sKhhgMDhIYeo_NZ0rCMIRdWI2Or4bmynrrdkecqbNfoctcBWrrqQEvRmmEMx2CwvMUXFI1fn7byDzK9WUQ0I_DReTLJftp7sueyXQ2F_wx5APAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WlkLTBcRaexD4DKSvvj7Wm77pUPGjQWPqBDVLuDGonYWtTu5NlBFn5WWpBvtjLaQeo0iamdZ_PXOYqmbpqLNRrSOezjwcTfnXow-4QpxFqv6nBy3kzvJV0br-B6KmGVKvUKrrEBGXIt96e6XNgVPYiO3sBqB5vmDwYVEWG0FU-AXKY3BBiFewWzSRhnqZXoPYE0LMfXBlKHCGkIeG3BnRQnZFBWInm0y2qPJ4IeFRYZ5ZkkwrBO1TSpnUCT4m-oX0xLdyKXYjqq31bZZRItsY_scKqbg6SCk0Ey_rxzIXfse0JEINRQJjQrlZWSnv9jEUxGtXk1vq12G0aI0e32jHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWnuRCZpysczkKnkjJ6kxx7IdMEKt2wPrr5tcag1Kd3Jeg6-3WYzetE1Kok7OYfAA5PskROk1xSvEr6uoyAzAJoSRoZ8dyLbPE_f_4CHFGC6klCwRetqWohisKY-iEWSrXasbk0NrWfksW8sr73pkvtMmkYn76x3z2hIwTAUgOflU2sok_Day4jRk1KcDmhUgqJ4_x-dPYVe85IUzqX438N4McTf9X4jfdSun_eGHvtatcqjGIouyeq0hMuAKMBaY12lWdCK3AjFKKplp9WArxtQfmSnzfj-jCdf8vdgl4m7Kcvmvoroc-kWV7blGuXxamw26qSFrlvjsz6NBSRgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AbjOLWsePu9wyB_Y5_WUCAI7AZI4HU3TbbF3dGv14lE7Ff2Y6Rs6JbXjtDYcXmKw6XiX6tIKTCQo3Aci98UsB1mrQ9Z0G_Gkls0yDJNIJMA0ynFewfu2BO1pv_5EsYc-a84SnKtIxvBvnq2wf6sh0JF1hWDmkpFqdgJRQe6ilh6h6tE1GgP4OJYOTU4AjcUsFS-1EX4Q_VIaV_-fv7PnlTJ5-Fy8rP8TGoIOubifpp5gtY67Tojqka9WcInEDDfLbVQ7-IobCeUJ2WK4hBG8dlfzX_noJZoh68_ncYmKkMZJSLZ4tBhTYhjzNonutu-3AeeHXviKlgkqwrswWRJ7ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kyrwWbrt3andaIRMWYG5b0XfYiBhn5FPf3jEQ084j24rF9ajfCfPDZW_jRbF8mlr94AaRQqVRrqGyXdQrElyijO2WjypD5uFYLTsbrmrONh6xaLxlqmXFkjEECMd79I7iHTIAJmCjqXKYFdEAid2CcodMkgz3zj0pjO3syeH30Kfql6_lmaC8E5WnGw5QGVbdkNJTDXUp3NGbrqK1NQ4vZPiuHZOR6v19JC8o2-KgeaMdqyPEROJ8CIlrt43k6aGqATZaHu_J_m1HIFbsDQxr_S7paRhYK1GbE8Mee-he7kV_Sj2CQC8x342azbp5RkjD__EW3d5bTlyAJzh8OkLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F1dj1KsfRP3bJH7zrOITt5sYHjQ_tTegHakzpvKGZhUomll062H7l6IiPuyS11FYvMKREZu2jTn_8M_TCqvqbZo3aL_cSw62TtyrW39sMOmEOfaWJwyp8FmSIE2xWTnT-FatQKUsmTOxVXH4yb6f7TCRmSey-jfEG-9TOzeGdkkhOT6yy9t3T3BugO_gGVZtg9ldSzASNWiZRzNtMZSoLz7-0P-rAdW2Fuec_kZZ9z7H97RaHohEvwZ5XblQ86ih3p_9_cheVs3Iv9OHItSG5oB1XSe0AsE9aCEX0o7NRs1JrchrjMXpV8wOe-UbyWfBf7eqz5U8_1n-cBIVNKdBCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQXUI3ZcieW0OqOstuCvsa-7B4I2B6kvdVIJpbbl09CPJjp5BHiUa_uoD1lkxkfeu3v4azrQmlFopyarBlPPTqJoG2DlLLw2gJUffVC0WcjZE4ftAMSZZJ_Ot23fhrQHQDjnzv8KCtyI8Wu7aS2R71Ez47shu-Z_RCrx2R0MtVYycAbGq5vcLR6DXG5Juh31FXrr7q6VrJWHJaYZm1trY3jBbnbdUxe5WdcXQ1pxRsiWEh6lijGRVSJjlk4T7nYNojma-TrM05ph8-TUF0--5vzH8aiLC7UNlr9LG5LawEWzAMXKsUqc7HhAZ2o3o-YdeULfaXLi0ZErWpKpfT5dyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vkchYlObELFs73MNESvYxD-amL3vGvhOF_QwZzNN2vHJ5gu5GA9Edo5JmfZz9ZqzTN1Fod7ukwMTkoThbZaJaSqF2GcPMV6B13opZsruXO3U6ZN_B4tdc625NzAvrCp2EhmIzdDcp9jbGndV-5gL_j1BpPO66mptCiOwGtzgGzvD9zwAzKlA7CCcS9V-6rENVhHkL6XszWiZHDTBOjsPQYmhXH_pLk12NOtXBLyfmvIljqpV3vzHEscstcx1XGwQn3lejtpRAUV3rBzLHBogEtMewczQn-0iHXS5QeDSQwEeE8pKFI1oVgJWVIyFXDT-50wZZapdWMmKH_TP4V1Yzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I1FuDy-S1gxUOYFVEcmg1G7au-EOgOuhcBUWh84dq7659ZfmELEKXNlHDvA7ekmBF4NzJw8mw7GixIOuOh89xC2zICnZzCtURjgZHCUkrhfAPa4Vck0KTdZT7g3L72vvqPqiTYjwWWc7kgZD71_uNN0PtKN5SOtHk2khJv2P4iVW2l0-WV1blVTTWoGFpPIcdeH7mFk3kdt2EVyxdRSsiaElhR2lN8FDaqOb08MBGD7KIyGdGZ7lxyiipf1x3gzkt2CgHRMua53oCkJj86-Ad1eXmNlb8dDBC3qUU2QiKtrXlPyndLx1YfrHix5-C4Hp5oksH7WimdP0w0BuLq8IJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BB81KQdeAwyhEy2N02SBxdHNhuQn7rjOwJ11x4xpCEfy_4jDCgLIR7H0x7h7uEEVREX9wzhTQijUmDMK8d4LW6IAPRnxlVbAii7tIkuJKzleiQhvypRsriOcOtEGTSJGzl2wTVpkvtccuKYNmMNtG1-FY_Z3JXif19lTQr-WJhBwx6Qiy8D11Fk1J4clU14ykdLhrwaRjhRN-oZkjKkbZ8nAB6w3an-LRwUHpSyzS4aV__vo2sNf8KDC0af9lrKnYxQJCRS9QdLfFYNTiFF4pu7ya6deNNuQt3M5YHKMHGvrQEfilwsZU1z8vx6P81mbX1FeMp0Z8HTjp25ppWrFfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rzJDWfku005dDDduTEsh0PWnAjMM9VB23Dw8djHy3CgElzjzi1t9Ic0rftAQBOoilegWweEYQMTSuJ0b8s9peRWYKOs_tuqVKhli5NEQHSlilSlbckZhwYU-fzT4hRsH5_JD6MBeoOuFz_poPa61aioENXdq3f-udlFudTvPGYaCPgxSBLk7XB1ZfKqr8piOOzonIK-RrFTrxxBAAPerRYP6StBN-Q-fqq3ohBAr1VAmnuzAH5g2ZaKC7yPcgCX63jbTV_Cam3iQ0WNwUWzmWcDmInKWAc2a_p8S9BnVr7pSPvlSaOAx5H_laaEEYTtqhFt2DxVBbFarlid6o6_g0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gQb4LSJO-wxtQFgf53r1jIXsslCZc3g4Tkv5LYdumea6XyWnb9b4h9pCmfeC43XKNK_VYx3r94HSbe_J0HszCavRcgIk1MTHUvPAloWjmgglf_QyJV4US4GeRnuy4omaH6_WcF2D5uNUE5ZLYOpUE0nwI8tt_c-rwYsvxTU0mMkF4aKI0w35zKlxfOxldoRS8JiHfV5l0BAtOM4UpA6tuwOw5MdHV5NQhIHziQxtd20zZUO64IaJ7OqO3BwIYPOrv4K1CHGKb008vu3gTdqmK1s9JhD79twtfXphnnHGh70dh1nKfU8_mEgijRX5TerbFT-GUQwlVToLyuCE3Hf9Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MvJ8xZpoq1AxDD3HB5sHi6poJgj_SXlyjQ3xrYJbA3l2BzDwhx-SXWF3PMGsTf6959S2lRK9Muw_5W2_Np6v1ywpXuS7rZ9SVy0ZO8XaZj_uiGpZJf5IDQ676heTQi6pvS1LoAAJPIaedFyGHWdx25ecDrzk5QV4GFdZ_0TonIgShhItWzqs-PXpUXveYtPoeGM-PH_Edba6EOCtqgPMEujveuGIgPRz0V9hSPIWzGFJGEwEZ-__oMEzA8U-Xl2VONDITpvQsHy1r_dwIdqTlXlydUVXuS8icCW8hzMuNj9MzYRUcbUpgDOuRUu92EKwe510a14bvrxKo0kDUnHrpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVgffufitG-fEisYRd6La9Mp4mKuX4sBmHkmreY1hS9kUXI0_r-9GEAZnnql-XFnN63zR0wiWEFpyTg3Xy3HMOWv3BnUm1QGSg7MfhXh6f7Jerapg2wZ32iA7U_oYYXxFZAX4Jr4ms5sMtkHzs034IlQBHNSXcPjt94VqhmxVRPOJqNCUvs-ti_auY0GBj6a16kSY3LDvvMy360fktSzbcZXrUKTx6-VKFDdJ6oLOYm5Aj1tbKuQGukZA2g0srIfZA1oGag3aTy5lD4HmHosPGXk0w064TWaHw9IOJmekOnug0l6YosH7NbKVrUpKYfKcDIF18WB0m6g5FbDmHcJlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZt3Om4DsU2EhwSUD_xSqk1RKSj9GRoOR76Qn9C0qyVWD81Y1jX7esd6DLQCAs4lRw_zjNZUAtEClIVFGCHtIvmGtevKKaoAZ7fXkZ748J-yN985qAm8KuNNIkIkPZE63fT1_LBv1DcdtMD-iW1odknAfVZC5r99nsFmmfNg4kUnedHS248AyS5eBgXjYlEEqA2o17FMm8dR3eGolf9l7l_K5B74RYa3RbPHmOQZhc2nRaM_DcEBiFxrhfQqst2lWInERr9pOBZwsxc9yL06Vqgy8sv3hkEn0XXbRPR2ESAZBRmfPqTuGDiJ0mwYJHkAeEeKryG56lFPgcFjRm6cIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nXlxIFh8NfTsDPWPl7xB2XUpqkri6LMNI4hmQt7-yvppKjyccFzXvto9OvSCzV-Muic16r56T3ZHVdCYxBNjmGp7PvikeyHU53P7X0U3ZqkLq_UNEhTBHrXCl_mSBFFdzK5VRjj-5d1LeHeSwauplY6HNCsZibkUenmnwYlXK_8GogDrl0kgN1IGAm5dlKpHG0lVdgCrlv5STjl3i6e7-wavdUIkpPbdquyVyC16vPvKLVQxGnoFTg-av1Xi4oWzHKKDdbJYZEsNjasKRvxBS3hc4sdLxBJwPurX2uV32jWl4RxudK3xErd2cOFJ9KlnpkrJt35Fn5WRukZ-cQ5cWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UGl-Xw9ACUKB6GP4JeW9SsaVnWXiLZi7JgoMJJZJuopmzFRempnthGdy5fG13aUb2sUnMq_f58FPylP-_XtLTUKXhilzeZLjVZq5AWnLPNlUEM2g5AXlLv_fUrj0J80l3B7tY5v0cKkiR_c2g9ocd6FXj4UMKTy2ki355fFYNxhyz7D23RqG-lyGO9kz8sKR9reYTVECL-derlE8kZ-MYGFFHVptxH0qAnl07JnLx7qrZ8T-Ow7sJXKWMei2gmfh3FXy0yp2zs1Xtm7A3U5iLpKDrkK0TCSXgCzNg7huUQ9nagoZawo626rrI8UdPPQC-X5IWmpJwmF5jPq1DYRBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sFZjz6uz-en5VCCvEJBzNp6l8slHiaVa43AGQy192cXLacllz-fR9Ja6Z414vtAG8xBRULdAF-ONE90qVNvR3GvVIPFGOQO16eUV4y8zoBB3tRHDwlORmBRmWeU7V_WaUaUutd2n2L1quNiqRaZFwYFVIqVLU3Qqw7HOBjeG0-EteWqxFcOK27QYsIh4gnXI5b2QZjZirHLhspy-sBxQ0LWBpOWRVfurk53Oi0c68dWpxHHj0A4RJC1Ike44IUy0D5NILfbPtoJFlPuFqkm8yLZUo24DJdwnFHYu8z0RJ5GGYTopbrGxX5qSIX-0PGswJXnmsx8js2Hi0OxRKhDxNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMMEe9ZlZG4szoFXBAQOC8FBB3iH8AyKKMxnu91ZQet4yiPvDeDTnu_aPcCkRIVpLn2_dlr6E_-9yGZDl3KAOlN4uq6f4pc1FrzE0ewkhQVkxdsDwkRRDW1AJ5L-EtU9YWqHIt11gpKQrleBl3UeWetSZuYTYGc9OzBmdtFRYZtl90KAZjy0XsBN0F8gSFQ--LD4mLIZy7Ey_Rzz6UsEn-gTR7am78uktQQSXBmF2no3iS4rdP2MYyaTDBJ24CWfi8Q91tPY09Ack0vXiX2PKEU7yrsliZpgePtqCNlmAzkuF8SYKx01Qwt4vUmODZlMSwwp7sd0mLdJODD4d6pNuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A-JjnuIGK7nJbmPZCcrP28LC6SQmDZ-iDDEp41tZnJibF2qtBKfohFCBLx9cLfZFO9KXtsj9unFxJvdIGWdifjMKSghDeqXAhhlbUZ4hCGisjiCcVm9hIArD6CWm9D6iQTXE7k3DgypXyvZUjS8jNZeRhlbkgtQL7-KRbDl9aoLcDThlaKl1gcu45oepfZlQcjya-djfBXkrayBR98BbOx0JmluwhbGoMtjaONh8spyD9TLHpD9tlKjwLVVgOS5l41ksqA6gP4qYB93GHpmgVqGeyWOhdIH0sw0A2EBV-AveghAt0narZVTinJKitk1cQij-7LkHFmaomDnCpdHiqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fea16yhgu7DxWT-juT4XhDf0ovbP7sETe9r_VciWTFNtmKIzNQOMOpls8Br7vgL22IP8kvFmC-BFxLbjb9Ph9la_eUSmyj29drw3cuRhjkEF2EkucJ-0BqQWDt8ezfgXFQJxNPPIVxVf0yhsyx7dvyBTMGjl6-xurcypyk3iQIe9NmS-yMRHzgVzfkP5EwQCEPL4yycDDd3l1o_PG7-qGeyPg-pcza8mWhujIEJ4x-ICakBRIvqC7zR4arA0OocWJIjyDj1SBqrRtlf1iLZB8XRr9eidt01JpVYRq-HtSvkZ6ugVEXPWbnaqJzJSN5pCWe6IZpFHvhxaFLdu0OwgzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YywxSUCwdMtLqO7I-7oJIPE7cMEwPO2CAV_Oml7XNCnn8LYTTxErSOTbf69uwL51rApiKyfa0Wb9FaIMV9keU3Ch-79OqG47sX34IEv2Ue9Ew8bQqurQPcNpo02IUvREOL2DxPDGI_qiiYI_w8dGnb9a4YcKTsCePK4CMnMCVyFR9dXVD9c6EHMqOUa1i45Z3-u3w3g1vuSnxB-_JFOmc09GhyfRy-NpkV3wrTssitblsTG-Y05uXEfOLn-6DeJ9FgHG_dbFSZHM_q8wQSe3NlLF9rVpRWO4JN8hZ0nz0FggZWrt4KWiIImOjtjKoAqVoRVVv2tQHsYMMw6r5Scl-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NFvvNWrsg1HBlPYiMP3S8iRJNl1-13GBWk4Pqu_L-7xrH7q77D5jYH6qpS_LqoAvVCbVBoWwuA0ENRnvcNi3vBMCSp6qcrCycxWYZ5zLll-ge9_miTzM2yUXGG69RICIAKEtPs4_sBPcRb-mahT0SLFAmSQlIcW1-FfTVBdHFGcaPvYuRYF6hyFM-hrcwRfRztKooqtx0Ga6hgISCxx14mR59Vpwf_zlSo4ZjRyH3D6-fxUiS1GAygWJ0C6s_f539g5Kt1SwpJzsQtjgR2ekFyglfCNo4qv6Wi30c1RfubiH6kZzQVezJNvWBNh9SjtTyOYpH9k5TGx-fvwevqgm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTDuBAV-A4O0Ue57z8XESlduggkyUm_yzGBiNXYP_UneT7qGXzJePpee0moJuoivI7GwVln23ac084L0LbHnn9Iw3omN3nlHFYDhgRj-SLgy3lCPH1wZTvOiFHxF9gs39Xybni8lmW-xDLN9pg7rYUc0YzK_dThiT3iwL9KC8TkstuoOs3hi-8aWpI28UUzmRqwgic6uU7-DBl_Mon0f1poZhqv0Zi-ja_f-Lifj6ZfQP_MijDomRp-5rF2nwgOPAOgGJPH2n9a_NMOAHnjgIA-MmDTFYqKA1SdEYumcO02q1E9bcTWuagOdMTDpBIDK_mZrOE8XK9OEducLBRe0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i5PuavAepx5OaykYCWr5krVpGEvGzx3n-ZUzi6bzcgV64rNq6dnr9rmz5VVY1ACsKxozxVVu60uMLzcfDVca5lj8BBUO4xs6n6DLPAcXynCrXwM3qpxuMEMbdh6nAObU6X1XHhg6vpLlKiKWh-MEMyNO4W1lpHBaCyZMAFjJ0Ar9lSznrl_8xiQJ1vj7m3D4bgdQnYFxH6097gsPUiRP5xv-PLjPkD26DU2T9-Z0uqUD8Y_GLAhWSDzUp058JitYpNEXjdo3wpChcmYy_pKHaB7-IXN-fobNwoE8q_gOi8UeUPITsUlfWYScqqczA4ywYxDcY58E_mU0FKvUhKhMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OBYbNYsmqToE4fmx83tUCFduYQfPEiUbaS3f_oi5ff6oZ0zJvDGTOko01qnm_IRVNaELzmK4NecOhNczXhOJziAtBq9u3fnvU7vAZ06rhe0QA--11NCJmcFi7CT7GEPNSmt7QBOM3kXoQCVEWN6Ppczt90x0lyCUWbIA99pGKpYlffFVAxvBBGg7KztistY2zIjvQDTedxn1tOwj6KMJ1M7uZkXUBYUTRJh5MVBh5G9OnQ7yjasGTcwJi-DIGRPvsT7BOnG9s2rpdjtQ_uaCOUc51kYqQaZnZTKPaSZUo4MGjmuOgdK0a0VL8rbTcCJgWQjIgSB0wZntFa2GQctKdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PlLUaSz_S9KZHDpYDCtWkteqQkqXxkR6mtyrzXXbEKvsS5lRrqSLWVNZZOgINWucHnL5IWE8qLiGO90gmUQjVQq5YnBZZI8LL1xFS_beRIKdMtm4BFG3jQxIO7oPKgExXUXxuW6kOOVnuEDUGufm0sIls0IReFOY9pTHGP3nGA8ygZ6nJ2zQVMjz36cth8SKfLHwAODL1yvu1DpcIMxsHKAtvD0iQ0bsRIhOEmJTLQprKH3HkRWRNlCRJt5oHAINyYH4dD8Bs5cT-1KI-MiiRLC_-_3SMW-qFXbZ4X4bbdSj3DLVYmFE83uAKwtKuY0UfxfjepR2OIUaDheM3sE9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TmjKzn5kY-HXdKxmxuKkXFRDQrc_XB4q00n6VpRMDz3jndmbLNePjVmaKXPjSvl40XxnQpSThDUaRnwM3fiqPZsDEFRALEm8Hnli8SyFhRIaaa06P4JlAsXHBlzUoZsX81OZz3J3Qe0uWdF19E3yu2xN45iEDWtCYCFZikH2yhkWm7sgm4xWgApXwLJnIAuQFxpDAm-OAcJeiBWpG_tBKjuXKxac586eAvFDAIOe-NazvG2TuthyrtvoHn5MkQkYwdYPVqnh07fHVl7AxzPCQEZ8I7QpjBJtFwKofy62auDhcp0fSRiPjlA7Cudsu-CaH-fkwTpdZfEgH-zsK5-oPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fKLxQwLjhw5wk1XxcyoTNVxIZRZo-5PhSfh_nktucS5ZOSELz7jkJj1bcXNqIOuHKaSjD3QUxEl-sUKClTSELNraGFbFerV2JgdLWLftU79QE_9cOuhPqe0WnucxJ4bH4GXpW7poSkwVH-920NkcXoq2qz64pyZYyLWW3cWbaqsXXiU1MlilY42El7C2kHGFFFcZESDnDDEYfxc1yzafSAuROOBlrmQhHvraPrGQYw-8Tr_NJhVTNxd-fJ-Yx6BN0UeUZtplsEu51lUfnKlTK0dmxAqQ53WGfe_T27wzETTwIyk50uuu8rxCE6x9lAtVlj5HuDUo51cIjmxZ_rQxdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZRcJ3Zrk6lIWULVuQAqfzXsS5QKJDTY6F34RHSaKuHXuNJwbpvcoXd6TZ1o8-j6piBDdcBGPrbdXuDxLQOUoHb5jcKXdOhvjCH9deF4HGq0MeG1GaV0qlPfr9PNb7YBM2t2mjtjoIO0poJWjkzVVMSHuukiwIX6QixD8dMElHXpyq-AxK2DNHy2AsrELRFkNoQNOqR1XuVBAJ0jbnPtqb2yH3jBSZ501yRoL7ZYjNMGDHbmbSWUpaqb2Hjf_sR8NiL-J1zq2lQPoePcgTD8dCTPNet3eaYzvT663uXodcgULpC1AQ_KLLkiVtR7Oq9yEf-sQxDL2DrvkZ-IpVU5vFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FEI_kGjq8ELTKZbY1RL5cCBlAWwiteG0d1rrBzyw1XWC84S9QH94ltxHt1XL_6jX7Yw_XdfL1sxw7fk7jNRNdX7nL8wc-egdJFcysjKHGfsH8RrJT8bdd-cIaq_Pvf9mGEeuHF0AfoJD1Obvnqvkos_WF82imUk5BUza7BQail2AzvIrXpCP4Ebk8LVEh9fFLDiQ0Gy6j947Cc0VylqJe0C5If7deXkUbfNaSXZXES8hXlW_PJNlV2V9WeuYDwnPkCIfEirbuQSyktb4c5l2xJcKjUWO3xp0glZ7xozmsw9MZEtLEGINL8yiW3iTlCMCnqQanRrRTLKDO8UsZIQNqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kyO--mWF9l9IGXW1cYCYRPeKsPw_-MFqmNTu2x-n2reUo7iSQCVf3UZe8ZMF-ldaE0U6UBYU92SmNpYBwH5brUdKD4H2b-WILSFrVcF9d3vv3qndXQ_hEKAhWJtSg7KjdXYEq19pH1kCfNNQCJ1oVXqnyeYWbNo0mXHDpbOlZPaM5OkPoxSzJokyE7ydmH9uQRp2s1p64c8kLzltZ_adRBcMOqCwq8WYbTTmlZddIEK9zAFt9VkIK7-dPS6AMlxQxsgHVmloRWMUumkpIGEqXtnPg-IYzin2RVHWK_9WiaBumGWYDP9KWZLY7mnyx4UW8a9IKNVG7DZWQSCzHhKgXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TcXkEPrwfWruji58imObmFqy-OkQCGWnkCAnsNspGcCPMB_PfIsqbwQ-XH4yCA1nPSgo_kHn_BkVwAvggt_ht7i207YkFQT2Ww4VdhbFNRh078EUE1r4DJSbXD4YGQr650CDK2_Demsdy4L54X83kmXrUMeiQWhZYeqnPjSNXouIvXV44OHMJDXNu4nYhvQQYoNbiQDCwY2AHYJQLhKzvikKUWushOfDUVV5cxHVx34IHWu6l8EPV0ONLV6daOwEzQ_QFhVu__Hs0WgvGoC2fPxRk95cKN3mrdhnBKNsXQS9ZWPHxRh3RfPZ0nNwmd7QxkXW2OrsMW3KJkvW5LtZ0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bCwnh2hvGwQ0cDNTGaBT8iBNLj-CmS7dtzMYs6HkpEsNl3-VtRTQRfMZsyluvwA8dSDzj83grWRdPGZDpqm4PCME9ekqkPme-g2S18a_sWiTEUcAofpFIFco2oBm5HyOZZ1gT8qOPc4jwPhYM30eryXDhTZUDSnNYd8dQA-nbX-KtCmyzOHYKLr6gM4QcCwsKtS0u0JTN069yxPBWhlQMzWF3D0RPYi-MZjm5eHJt1ic52OzVmhTmh9mE7YyP6NSe0QWlbNGDQjrwwWVva_3l4_kX2d0msO8sZgwqdO3v_xCYU9vrf_W1pnvZAepjKe39qfkIX8BlxkRL5tjah7C6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ya_YXFO_Fz2TaNBGE7aI9DNnNy3sH8-hQU6SGpG_-uswuFIRNZP_UdeDXh0LHU1KaFi-nnBNFzXnR-yAefqcPi8cJfhzrtj90gPkzEd68_VokHx69NbIZYdel6ztxMtmYR3TVaQGuaSmjat-_e2WyshA87c4B4smOApfpcjGIRtyIQOA3xuWCxdn7y2a_bCPLKsVqn0nL1jQKZCaPkkv8EQtMq1J8eDBYrPYnFnf9pl21wF5vJw0UNf5dv-sXQrQ25dO6wcV94r0i-Bh557vkKhpjOq6tLbEyAUpfjZGtVcC7wevxs0mxqpdrx5thHjQL3d_nbRjE7Iem5qLTXae2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uF3kA47Boj-UT8SDV8MRjrMJ_XNWEdVwYlxBqZjk20gJkTv-aTjfoqq_pDJ9xxBlNTiCd_m3B8__OmrG_5QVGxy0Zx2xbPFEg2aMxr81mjS4BNN4gzTaXhjJ3mruin8dssZNzlmFZBHvrn9KNZjb0lmsqLgHIs5ExPrb1_YWaTM-iFSJI5KqZLRIwxYf-4xQrxRthPN4qQVd-LaarWQVUorBrhedkJ5jov0jaVQZGUVaYt9v7D4bLgE3BWmmoaaGCRxSb8XTNnuYe5QDpjg3GwLFxFw2ktBTIHs7AUYSCCqZt0PqV3RbFE4I13APt-E5aVcFd-SpavnTPI25wjoCJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mHVv7cqZQC_ryNVidi5NQgnngqQ9XxYtnYGV8cZAaevI3dAMqru4SigyO1PY9tHJi3FW30LwQs2j9FHXsBJymk40NNpgih7XRz6rACnNnNkBDYXVSKqZmlbvlcit2u1cglsq_gjByUI9hr6JSYkiqDFIWXyTVW7vghdcbh2XcWimzWAQlUEFc16LdwnoVe7GizqfbRbn66lXBC75j6YICgsasZDu1wnJAxzrCZJrnNBQgrX13cBiHcSBjmQ6vmBE9iaxRqX3DYW4T_bOynv1hhucA7e_LdgEWn8VQW6obNB0iRJ1FAALEzL9TIh5iajVQw5TMFGK2tXLFFQ6eVB7aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wrllm3RVVCzIkGEcD27lbUSiKmBnSO_EdqCMhXPGpQUTWmTLLWDJRG7hY0a6wV2J5Nh3rZS0nDAFw98EdVhd3a68cA2axjyWONQSs_3XBDNJyFvEVq1oNNMccZUcD0cmIhKbZD96fkGR79ZoN7yHANHi46p0jSFpQ9SgXSPvZCxSAu9XNkTZfHVCxRP_hX5FCU_EsUZOtCdBVjTFRGedkYlGw4cWZfWXlwaWq_PMmx4bI1Xm225qwjiK25LwnLbcRoVVTntPPIEKhQld0YOSwwyPcqOcQfQFvg5v8s6VJaaepVUXa8nkxKrHEmIIJP4F6UGtcX9Ao-5yAo3jDR7_hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bqa34ZunXQEPict0weJCre9NCoLtm8s4TGrpGOd_MkIY6A8z_GgF6FvpDN82NdOaibyCNEBlKv43cm_pdbf8SEb9IA88qWpqX-royaOHUkWbHhY3j2eVnbllYRcpq183YhiLs33K_JhjSAtOOOt_r3Mm2MlCPfnxuKR_04lugaHhnWzekANKMbB14Tn68mKI4ndQSmVh1gkbOK7o6cecQOjyxZn9vU09JdK43r6GpbRwQ5Jf_LUVhB6eSlA_HkdJBY9H1UUKlOsIUFs6wSQFfmGvyqFGr-C1sHNme7eUThb2gPRMvDdMnhyuKEYPilPzyg0btzEZwdbJa8SCkUP5Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gtOPDuiDme-qALepah7GP6nnmEnqvEujR6CVuPpGEQiCCcL1R3mx--XOOkCzQ9ltJ_x-c5pPaOyrmvEdR7JVMDM951Z6x_cLWNWPrL_nIzJ8NBQTBzg7erwqRjU1l6iT8JlQMYXaO7UdXNhcHcTS1KA8u8_1hRsbuE_buPNjFu1AJBSNi6f3mNUkk8mHXdUMH2Wkh6ceym8829mnyiGJ7mki0tg7ZDDWQ6Fbb2qetIueDeULQAx9RjhKaMGwWHYN8iRxY1teXGlbzE56WzLDdGhlCcIFG-EqBoqHGT37NChGRf5UJ3mL4SUh_wlvEf6EaqhRXdzH3CO4htij22BP3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LTLu4Q9oEtnNuu_RLKrAxtEjU3KhHgOwdjEVrhHjmoaDXsBr3b5qDOBncXxr_OdGgNdpgC2hYmuI3o-x5es5QwEem8_iagJrH5BMjRygtyadrDFRuHx5x4u6nOAqoE975tOK_LmeISS9xVaawEfUxurewM3LGGUSmRANYfbYkGDpiBlJ5xjKdRYKv70Hcvj4yOTgnYpLBzXZ1fn7Qt-TAqeb1LaGMef48ukfMmRjqF2xUjETUn7MVe6m1EuNqpldDkAaZrEd_AGu4W5RX6mu0S98WdTmcaAhschlRFFQ4leUbRjZZs_0pdMSwA7I8RhnUs4rkxwOsHmE447krI6Wlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uzjgJO5Zdb7Vq2oDNXuMeK6hj_Ecb2AqXoB1xjep5xAfWDRquqxMx8b-PRGkKLlW-uKfFURUc8XRcTQXfcCHMpEsEw4GatCeHCx2GH9aMkrge2WKujoUWtf4yCXJ_robtQEUf84f_Ux55GEAuM_JyOvkGeT_7y6vnj__8mFPbIgX_S1J0Tvaohcpd4U9RldaiHA5FqqRDkTQ5fpPDbrBnHS-D6BGV_DWtwwi2HJow3QRc8lQVMt7uvRnYnzMGVRFi9MYFff6-oo-aq7fhCsKg2JmSH2kAmaIwvWS9cQ19VqEdwPh6fet7DgRlWXvbf-Mw5FSpW28W_v5XzR1Cm-o0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n-Dq3f_fWU2Gqha13pJ1HWhuJOKYZazn8VMyByaAEaaYlSYt4gs_yoaixSRbSKhUrh2JM-jqN4wGD-qQcy6SUpr3mSFDt6cvVugnu-qqqxkBk4b8GDPbAhv2Va2pjGrgb38LyeTyzEuImPpmFJd7X0yVRweKZIhcUcapqTAVHjUry38wz09BbDWMeyei67w6gmR_wwhrSIQEFPyJlSCX9wJhxICu9lAS2cqsIx71QxtkjnkzURU2hbXNKVrsQeRVIxij02TycvFPa1mVAc3PLfltIm4r5zu1TG3fSA-gKvWNbTPh3qiDC-YEX7lhtrFlMFre3DSeXwWtNZk7m_q4LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zv3l00g8nPzOR2frJ3WnzgZAlF5clFG1X7zGq_fWYpR1hoWJmN40aZm5Vjn8DupPtylcpHAFjhVKQVxmauqUnFnTsUUq7yo-nsJfj3JzIMOyb1MKNrx_sFuKLK1LiSAJC4PAt6iKngsV2jhfHmLZySnKJhv9bPeEGZ3z2MSAaI4atUDhLwnQ53HPQyCwUiCG2YxJWtH6d1UMKUkn7cDLBWzBhqbpqK9Ch_hOX96cPK8BM5eKaZA_Q4DDCngiXIqexh6HnMrS8TQSEaVKh0j7YCzGJyB11enSqa6T3gKWKNII_cAaE9LSKdQzKbEh7KqLxN7G6MfpZwsmdwbWz4huyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q26c0OriAmS45yIKSAw3xxnTO5H4eEbd2yNfY_hsKy3eBKEU848qMxEcO4fn4n_t5XBP3OaBWDbM39MiyZAD29TcCi3ZFUBBw-OE7cmI_w9y3i6oFJcWCYkbEXg2AK-7zr_l0HbXTx9Wjh5_sR6qDJP-8poGKNJUuHC1eqNxMDdExrNmxqINSV3EymQ4q0XUrZ0iTPxGYznk5FcVzB-YcBQx2nj7C3lIcfbDetI1Pe9O-mr7RMS2UYvT0jA9onBwTdMaGENEfNcp8wye7lQCQP8s03ukhAWofcCAakQTZBzy3oruU6AXlHP8POIYdMUy9eL6_rncEiw7Iem6KZ8AIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VReT6rz6tq9IwQ3E7b9oD-7xdX0EjYEmz7kfYJcZJti6xzHXk7Se1jk4T1U07o8WpM21sOxrEPJm8-UkZ95mLfCDAHqpHwojYZpWIvp4hY-zAP6ieKg5qBlTtsE96vY2CWe9VDQOF5jcGh1200Qgvgice9zVmRk8z5Tm7a_JhT_ruRzLj0K9lsbTL1gYrsMJRkCG3lf8X8dXJRJ77VZPOybF5bPFsxRwvcUQyRRHctWiuVwp6Xc7tikB3t9mTpq3Tgu45R_XhBoyqyUZFV2rHWvvpJp7hqrcUKU3A6hDIIKYZtQBSWGfiyC6WjnNGxApMc3hr-EcCUj_cWBi1aA14A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MjiDS9rT_LUQwMXDreGJi8_qyE45p7gYXHh5wr6rn5KxOmBejRTXyv_UPFR1RQKIPSYNrr0AanRuIEkQhxqKrcxITDa45nw7GX2E5Ia_XdMvfcyvxb0DzA8R3xsfpGr-n-CTlk4O-maTa1PgQ-7FFxCsEBYRuftHJuSGkDBPKQqyFtAlG5esUgqcDrL7HLLuIJ8Dlzaz624NGCuGTDNE839VmHxGvy64eC4o0m3TE8wxivUlXlWkh_Fysm6ANDe-CllfwFe3bZrUQBxFygX0QvswpEj3rhd9kkP4-atCBqhna3uZSfF9tDBMcg4pFKQEZx7C7BFAZEoMlYAtq0QGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbR2qhuXkc3MBmzmtdXnLicXPKvj9XW7Td6_bZ58SA7BwGID2NNJC9OBbBB2novBmONxEXb2rLmhnAXjlX__UsxHehQKpnq4kNjV2DiwoWe4A0uFWLkLQjCcQHl3PrAT1B_spiLdBdyEfmzNPg10zCFTDbGKdWV-1PZNJjbqlA_TbWRo_zi2VqMEo0ca07qGml2z5-V4cWzLZPIYBX19HxV1jQzC4Lnf1EM9io0WgbNWynRhx2LknNEzAoLtKohh5KY5T2nOUnfoU9ldJv51uhDJwQTcceo_HLmPnK4jICECEivExPTgiDhkLAMxtsrAr8yM5QpqCAVwFo4v-wtPyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlqN79y1PqpOS1z3KMJG4pPc3vMhGHmWDgSADn7eUE0KjSsxgwwG3G4DJrfUfgbKyJ5kCEipiLBN-B4rQeReBz5tWtPSrAoNhAnOhUQIV9zjO3EkuFJMhcFdYWYAKIs1Kj4BypV-y3M3CAvAnkWJZtqrbg4Vg24EfP-fzVrb0Y5g71N_w1KhNzhWxbv2kPfgRsu53H8rvOw3zT4T0VgbOHle_rP6qVg0X_fSn2uH4h6gOo_ULgZJzZ9AYkDEYQsD0KEoL_HnvkBFI63py8TgKJXr0lbFjMDEqU6XV5CMGUfyH1tLx031vJ9j3ys95YkY71q-CqX7MI93DS_E_FMWAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pb4WhDJSaWuLW8lYry1c1FcWEnsGP0lRGgiwhsA3Jze_bauHLiQUg6VUMZs296fdv2U0-CbZEkQyd6ur8CCdzS8FCe_8mkm02CtrILB2nyqCKK56AMnU7lQQUj9C53A7ygJHIPCFdO6PgigUHR1IVRnlG0P5BdjIwMv1aQZiwbi4VaE9tBPbzXjNJACNIbUG1H3PAiZl7phnoKnJtvfqkAWDuoUDPoYyiCJeSc7JsdoxOs4dZfn1hY5i8IZ7icoxXemu47-EPMUsHNljxb_888xfUjT48D5Pdz8KSRK2gZ2sam-WHLTRZkkxlcDwraqfY6XUofqCgJFqdaVF13l7Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ud5bLMvKiK6h5G88X7q47TebILEiUOEOLJYsS6CEObH9Rh8X7HNSjL1Kt0ODX2NPxocyjMYtcXPdv1HgXMyZHhGiT1FkFuGhfFTfgzt6UJ80VVbqzVNrNdFG2eFjvqYg_-x_AXXUodZ7yl3M2JJC9fCgaJgeSpE2_AY5NoDY0W3ynIf8N8kJNxkA8be-Vqx2RhQrNTtpHlReXdBT1WCvPjfiOGLoFeJ3wqkG7TUQJXThBrWP-TeQE2wXYb4QSQWh17XdTS60WrJzVU4pKXbLGwK7BrV17WXW0iAAqrSZ3UwUnOV28tKBTsRxYUuqFkkyYacvRH1IetS4XeGdAEQNlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UNmIUhA0tWIpbVhowBZfQ7NJWy8kL1_Gt40zUJ8MnekoMv2i7J58sNIQ4b9_xMYvnlNju7emdOsDEr0jD20Nmqkezn0ibFhoH07P4jLf7t3Rag1BPBs9i_KF7k03EfPzqLrIXFwczhv6n6jkUclk-7ElWlqmJbbShIL6YETH48oHOwf7KKtcwi7YyKBfUhPMJBReRKsrP-Uqa8C1ScVil-GYhs5-P6w8nOFjbtK3imxvOSv8pOQMEwrO--n4dv-A2u0nEr9YzmTA4VEjcS0ZcEfb1WITK5vmIUlF71WrO72oppbIvpHuJ1kLzM2NsG8sRkxCrJa5_mKp3iuZ_4k5RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h9XmZJ2A_TGp3IJ4_3k616hogTfm1h6gfFphkwEYTPjIxjj7HexTgGAu_j8fKSa3xj9xNX94DSmWzTR2khDI8nZ0myInP-LO6JDDjJqkeii7FEIYgMdFn03GdnPowWOJjzGO91QV3M89isHAw7uZyOYdaiSgbZbMKC-3YDIb_32hQ23xJEYGz5eOJX7Ff3mS8xEHM7tsYiyavLgXboN13oL104bWt4zXTui2uppaK8JZ0cBl8yaAougzz0DurekB6oPelevyi98rSEgSc2iQYVJNYAFJz3mWeDEQReGZt0iJQB6Yltk16rtipFgVvsUC5ZwQHiFdLYaz-RK9vZlBTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cAJOnKpkgNEw38XDa0X5uIGsvqxJ7trrGU6xADWAoUPPdbCwuFskoS3vEnu3EDcamX616j5rbxO6eHbX-USU5V9NqwuMXYsVKi-mDpwuumMreIaVVMi4qZVB-XojD3V2IIgjVvhT6g5DpTlqyDhGezCYNAMqiVqqnKwy_u_ZQhPkoGKaS9WgR_vT6hkAXQYxIDHF4pZzNFy8dP0j6DBmUYdQ9BSFpjf62nnkxloiA0-97NCF0iPR9jgwHwkOJe1-KMtmMeRK7fj-KVj_jpmgbZB7cK6_qk9vm4MFqzuUghtN2annAYQsOn5I2yVb75ukaqizqTUcHYd4NSbBZqWnQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ah0ttMWFWOQLjuDwIXwqOt7ibvV3p6nxB7Qp5SiCSDkLghh1j8-xdVaT54uaobObVxHsqSsdY04S-WaBJ_feOkSdHDuWxL6hqBtOUbZW5vUFqrw1e7AqUedBc0_GyatJVIbJQ-tD96mkF5Ge00K3aLKduCDboNY7TI0Tudby6UoA9bukm-Dt7UDO2TmGe3BDmLthet7IzWVUYHWScfj84a-taOZhHA5p93-VHQL_ntu0-1XyPLU8bZDP8f7eWlZYNbUSC5OzkI73MjWWQ6-1z3aCct6eNSPk0_Fms1-KN3MvoDybTAtANL4gBCuon0eqE07Vo69zlHm6dwts-rgNyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UrVooLjUxfRUPF8UW0l50jDA5sCK-Kb2eaUPeBEZKoTPU_8BUK2QfVN0nBbgxCzLu94r-Qs3-m6xcP2nNB26XXFmvd_CeVOex2QzKG3DrQlcEAq4l36TVKlpWfRTYacmphoQHHqj9JLnaCIzWnFLRPSBPKRokEXsmzpOGJ2qycJduBegR72Gh3gCsuuEFFvt-CdHm7n5LQjM2egJsuDMMMG2BFsK7E94LqtT_Zbld51kspwd28cBnBtkHpWJjH7U85C2fvctkn1j4k0TYpKDakfVh9edo4nLYyj_sLqq-LkcEf0sdW_e8FCtVsE-uoQ9poJ5rX9ILTKDpwZWizD9uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FFEqwJuc5guBCq_8kaPTS5jADiHBGULCaw8iAPNGWOvDwbb7gCE2QoyWesr7nwAJOg9wx7ZXh0QAG6tlvSYEiuL-WPLRl2_9V847sYHRJCNKesb6nW6tLVHLNKh_keuaXVFMzngqoRMnwJU52enTmKmeU4ADVxgTiXa0KM6o8i1ySwsy8jVZfriTXa6Jj07EkxzNPMLcJsjlyI8KZaU3d_Uu03YEZ85R1GJeSVt4PuUeQT3NxOEF42urmTpXPi_MwL9KbWZvnSp1WWDZybeWra5ja5vkraHuj6H4-14YCy35NoKkbY-vYXJIA5_60ttQBHJ8k5iKt0r5m5RkHJDiLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4nanDe_y-GBln9igMY9r7vWTx0MaNmBvj9qp6OtZVh_a9V3a6RL0foAuscmlllr-aPT7hBdQDgAARcWm1NJDgW--QooMqpa-f8TtCLUq6dUR0rh7i0TC1VtU6OEJgV4f7clYzv9GjCEJMVj2BYmEU0G6y7FwL8KxED4oLIbBIjsB0KA4xHqsujg-vOUA9P0Q5oKOasOArB3MONE9b2NqjfmpD0TGTMIoBtwvkjiWYzlyvBvM5I2OeIhuq8VdBtyX3pu3b1MJ5PzrmhJ9zPnoLj-b5BENUFPKFYVgGyiynPJGhzEqXGsL_mYKLHBNMa6Uq42w1qxz_gbUQ4VL9rf7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nc-_flAUiYgdS1MooR4Hmd9Z0hRoRi_n4I7HZnFxw0Pf_H_3HsQKnYPXrVhovLbUcwSP9Ifbrx1sBwBESfE41FGMKltRWrztwPLRTckaYNC5zL51iH3GX9-w9nJnZfBzHfl8AQuwxLiX2VucgvECMgyYIVpxPeFzJHxkn4LUJkmvidN21hwTSNRphTdExfh8BMIw8ngVBxzo0qZU8Oo11PCcuFkXVxlsvsjFoeUGhljFTpnRyuzFM9vdpdFmKHMMgc78OrJwi6ccxQjrID-jExZdA-EbZGyQWBmS5pkPfbwivOUhyGayUDvHeWFn6EO10uQPP3vuuGVprOQVbkALzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQYbM5ywFSAz6fT1D1AqTXTxpgNqxXd9oTCX32HEkGil3yu0cpLT8DrZXqRbaYpMmUBWz9Ih3v8iUgCMQ-D_UGI9VdkFBk1iy2ouqIIGRSVSG0GC2Kk3508-V2WK2551fdQVLJbU0OrskNzmW3CAuaJlu0sTX56MsscZJub8t7Rlk46J8fD2nvdCukXz58yF7WMDYBCUvN6no0mf-YKCeFEabZ0ci_C-Qtd5m4t8_25TslxpYkE48ONiNWZyV9X4A0BJmQWHJpLzaYTiY5QSYp7sAXtyg_mG3baNC_g0h9zoKxwqWQDdg-tOcwgibW8-pCME9y3bw_tIBDbqG6JqJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWGlorNQ8aUdXHBCRgM6WimxhXKUWGU7VeAEDt5yGyeEZpAKUoke2oHIo2iFfmGsm9UpABN-5pWHLOHzvFuS-UzDXeRS8RVAbVND5lO47dvEDsKBPYurGTD8UtqiffCMEGW4oqyag2bUFzt0gX617SKjnOLYBzC37YYxusKOyquhByOfNSaUP4alfarCIZzi1GIF-VaTv_mTfC4KhsR8wXLveRWLNWQ2zUDCgWuduhDkABuX4SsIC7UJKYx6Ty5Exmdkp0jkLcAqED12QsNyPURiu_QmLrrT4NS40yhyMnbUt4kZavPoVBQHnglWgC90gceh0_AiqKFLIwp5ba4PSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TVG1Ged4BNyyXRNB9znMsjx8zisKKV5T_m2xLDIV-LvCkAhwq-YBuY39yfpZ5eEnZIw6uqkzdPRYLj51g62Q-vSd3174o94H9Agu1dlszh_GLslOOEKnxZIS9krpONGQ0kZUH4v95IyLZUVFKMeMA4JJDe9iVTotMQywmdh0u_mCowmSGQ4Au__tNLZUjsmqc1h929OwCHamn7ykWoZrP7B7HrOTQxCPG6gaJG4s7JEoThC0SBud0i6BKPp-w4QUIkqqnnhTMhlPcLlAZsbCXif1SzPcqla4SiVntnTwIL8ywTAdR15tPmRTWnPceBVqZRC1liPoBr7Vk76g85GCpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jr9O-jw5qDaaMcdLvJartF0GxBVkzc4O2Kl88g43oiV6MwfqoRyaDnDlLb5KsMf4sjNTGvRnDUt8oWsI4kw4mf-68Yv26-z8z_PWavCg94HtHhmqAhj4PxOvxW_5nGUijsScnNZaxNch8t6-6qKkSdX2iiydtH8eglqF212WWsp2r437CFI2oT3R6TbJ2P-sVr9aIEn1X6_WV9L6hlrvIi7qqb9BoqpwXl2dpBZsmw4vcwsX4GEjdFmyN0YfkCSkHPG-zCOzjfRyWXNFN9TQ025uP1Xe0BkRxJS4BVSCUlpHY0jFQOCJIOunDOlEyeATPZOuOpmZjjhDxB7hpps7Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LJ-WPKGaM5qHFAjYR_mAQ5zmVP7MfbIX1ZcNO1f1IUm2sbIwDTQyfnpYVP2U9ytYPDv4Cl6D03c8BnZ_AkgbwuklqRP4svwyuxxCUNyHBRbg2zDntEpgvJDdgY1El82jBXtjImEFYJEJn7qSLOdaNVGEL45kkIefwbaBgeHgFe09rLzaQhj_X4CB6We9Im42DIQgqhU5m2KIHxiggvXTvXf5IV8t6NNpt-hdpCsSigPgT1Lvg4HBn8P3k6oxiuNRMcmloVEIRxasPVQsuCfSA0oa7MgSw6YEBNDu8PC_9NbL2JenfXIgAFhNExPpRM2nxiS7XDMmPLrM3og3eX_CTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tkqwTPDKAAYeE42uD59qnUrlpE98tVUUnQujOjKUxTt-F34iwICpsQzgVhpHRKWyDSzNjXeJsD56PgI2pWfhvykjNYS0wbvj9ovLi2B319D4VBjYOp41oFIszcWr1oiQ5QdL6N6UzhBDn62AzLZn09StPZQdVfxm40WvG8bSoeHTG-GKC6O9jozkueXyJsQRosjaZQ1bHVdwmXZuPTAaF-GOaEXOQTv33U8sm5o3AJ9K7OFUg65mEAh-Mh0bBv2GPkFqg0gWLvb22L9XgunKKrdr7ZgvdZtwEGVT94OvIoGpirxajGb_PYvLcCXLWwhw7ntodtODKMK1Z2taK0cKSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fb4iIV3XrF1Qzhru8tsP0p56uWXGwSvXASZG6Jfp2tfgV9vOoMTl8dvEucWRuzw4SDxWAaoHzvRD9_jkPwSZ4Sz0dkTjvb_nmdo-Oy_zd4WL3kXllLV_aV9n22EGP0-850Ckz7ysorII3549LSUOmVvSHmkpuwvtbuTjvJvhoFdsPR4powpybTr_LuSG6Xd2Va4LGmcub7af9iyO6zCT0fneq107bGT7I4zuK2SYL0rTdy_Vm6CR7kfhcs19z8ohcuB1O9An9yLtLMEtN4SnK7OEzOFxEM_JPDRJO22lK6NHG9dWm-QNmzvuXxyeXbXT2XR8w9Skl0oSYfGnzEAlmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIdSb5qNkaPik5pTkfppVF4ZCM7KZZE8Z_JI2FsvEModQz8BtRGnRXHRt9tyfXOHQK6_-3FtXh-fv6LGqoSbw-1uIp43xSZ74vB_aFE-doRHA7EU_LcZ4FnZKsFB2FtjHqZPp5e6eTdZjoA2PN06cS-rlr0wgvjxEzhFmfbV0gAh8CtmRpXs2ytmAp84wfx6szbZw-eM9neq6vupVnVW6XPnUyfpukzkN3THEZ4LW89UATXQfMP0cDdMb4iEb8jVGAb6c9UV5QNpo0QsUXwab-nUO2eCutUReyGc8Rd63Ylx6FxGyA8xn_48O7A53mZzzctRLsPuOmxcMgfjvk3_Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wBrDCpYH4-uLsN1PfuoLzk6JkiAK5sGFPJJPUECF2l5_8uHfon-ZixZ-bFqc9evE7XlCzXCASNpxpDgvLpjEDve8t6OXyRLi4LzqT-n1imzlXa4pSKxBzp6J2dTDohd7q-skmwLqgEeIv6Vce6yvfzAJLkm2JkaKkEhRXpH0S6H4mD-LJCql6kIvypRokJYIrQTsAGaa97AuqwI2L12Czh7Ji6vnNAkq5k1VQiW0IroFLfpyn3ACALw1LdjN_rlFmivJnCfY5zN9ebOmO6-0t_-_ipXO9hLyl2_0mLdIm8M8XqP8k5NWhlnxkmsK30FI0alstIOk0FdpMuXRQHdJuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lBdz-y1GmVXzGQlexH0uFy_WklRU_wWEpy4sxrwgeTA03sWTkSqpQ977ro7Tw5T0ZA39fFKhMODNeDdZZnJrEnXp9hfIx52qhc7QY9svBfudncFUb7YWCuQ9ahkqQcqi7ygR4VUYd_Wg-BNBSt5nLAIxYx5Fnymtn9vzEHfB_EZKBflOLw6-U8_6HjnEEAq_Zec3Dgw97jMVGySPqV0NmneTQWZwMEtdX02MIe8vcbC31-SF7e1Rc26EBV86KSoPefNOrp17edioI-TqjGATJr0a7g0TPS4d2ABBLF2a-HXAHTnKNhNfAvr8n8vpHr3K1tMmCLW_FRE7yAb5WUgwYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YzLTfgYjQikpXXjLgP6gUOMtOXLByc9gncNnwThvJqErAzp7_zOvWQAcZVjLvVoJR9IpDOKCrQaBpP6FsYGOnJX3LgsAZhUiQAlmyAVUjrHdTntxRDWByWtwT88AbFbBTI2vp3GNDiL1ohqzlBTZ6p8R7oVYZLwfngUO_QJ2_nrbLWwkDNnuCJMD0VL2c5w-JZ8hw-LCbmpPSYb7TTujHu3UpAS_ltsUPPXXGflUwu-X-sMFpvWr8JPJvOuEBzS-QSNgs4CrROSshOon_IsV8aXzZRQkwE25KpPBTg7SARjTmnwcomdO-4cEZ7YwBSqixC9wu8VC3IM-UiphSnpYSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mWCmT1PcDvY_Sopj3XPzhOmZp2_Z6Ef2M7JZYB_3C_73UIMpFcio9UFKOmpsA-Pt9BsAkssSGwG-g-usW8nyfFETNDexsrbpqRhMrJ0WtnaYjsO9g1HJWP2mQ9ptrVjAQgSJxkxFkipj_-RiDgZuLBAIT-5dNIVKMT5oAABhSqKrW3BYcskisvII2cKwYLIAVrsWbQtRubRtPV--lmQNVHvotkGbnzUNa6Ikw72WGs2R33k7fwKgMXiOaLizfptUOg2H0IzwIIJXUhU7vRCd9NrkmntytbhIH3ZCVt7-QsoP8rA_EjmoB4eE_07Z25dZieMo9GtGp2ey5DVx_Cr4Og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s6c-wNtCrwBbk-XZtTzfBUkfm63XzPG6PX9JarokNoNPnRW03H1zi1p9Fxta1DL_192cYA2qbxijceRqp6QZc0eJxLgS-qBCDlmF_lN8kqRcYh5wFpKP4h7J3Ee8uUI6B-LCPSpp0KtLLYrdu71KgFi5WcR2_5bVd-Yii9m41pThE38szJwNnZvW3V0fMMF3bmA-Yk_s2Sfk0kGVo3T1wLV0a9J54NdoNA3tJOt99E-uQJCrKUvW80dU5y7m5os_kPdzHvb1FkIynqQzy9_QrRqQ9Po2x2hSwbjlBX5__Kk3vUucFzEqsWPrKD6O5Mm7uhbtf_Sr6D-hwd1NVdtUzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I--3kGO_HU40nGyjMvUwVlgCx7bPNIDad0vDnwlnFFVXNClCZ_kUMCkxd5vqeywwAD0ri6VBEl7vGPIAFJZrBjTzaef_PjvMwijj4H0IMP82SFxsADdYCmH-QrdgL2sStZ5puWi3ENsv2AkHmkCZNE3-NUO_i0u_kJMf1xmmiWDeXYcV3YVqJi4tzQt7pSEwI29VR12HgjOeWQ_yO4BWuYLDYeNM04hho3Qig9T2WaiaROWouwjQK46NqB1kACqmeGaEkzxToZgBfVzi8dcNI_Tybfhj-C9lSuOpprxCJJmjHiNfIO7Pu3yfMjILWfutOyQbJ_V2_-YGB0uALjGlFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFbh21eqm-yGV2YxsnK-0E81l4CgTCGqvads8m4tcVtLhegJtOjkO5uo3N_kq7CRoYtuSPHfY_AsUwYqY17kIVZptb13UJrSUVQywdoWey5JUAJSYhnBHhziO7QxkTLx61N2cJKkxHTdjA5LG9o_Pxtrg2oaMhc2gYZAZREViU4dixq-HPLxN3MsrA5_pi_RxR9ED3cyqLLniqFjRT7_1UtXjSQUzDCQUquavIoHH0jNcDa_hERS-IjtgMteHcRCY3mpz3cPkQLI7Gt2UhHOO6N7oYushJsIFV0dHN0KYkhL-jYEMADhptoYIj62viKvdLO1iiGXfPOIDzKGTlq23g.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y9vp8JYRVl-UaSCFEzBLImACFomPaRoyk_F9qHFi3xHLQdQULWckaTg3txrRlLGAhUGzqwZyHkz-GqpgqH3eQ-LcDmeOPtAhzuEdL1Fd5BjfSOxgKa2aGychEUALPQk3x3JUyuK6jfry04AmZ1lZQY3cKcNxPlBjvmGK_d5t4LbmjYfmTU9ehMCbay1jarMMSD5KXEfceX8mrBxFA05PEGTG9QJxXt3hxMT9Ywq6ec5kIRM8zFu3Ub4JMAnjXInUIEsJJ3F83G2Jt_WIBmYZCDG-UfgQyX2JL9uk0VdoC279galE-O0U6J5Ia2RRJfaPOjgOVZL6-_k6tTh3Te7yJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CmLvxpKb_vjudJKBnyLvkfkwDrl1dC6wneJHeZ_3RYQLlZHPVLKedsUON7AFKx33QCj6fPk3f71oZ8ofDKhUK8FyYfQ5BXJ5mTDaLliTdhpSYl7GzBF-CqsRAQ-MwHOGTVv6SZTwPfT3DbNUlL0-Seubxe5rnmBOoU9EZ4Rw9GwUXi8UAsuAsXerXV44HEaOlLg4qrITCNH3Zdjb9DbYd9XY6_SF4XtvzaP8TtDQTt_bzpkPUfRYfLYTIpG94Cnbi-MiPZNUfQo1JD62GRXJpKgF8HD1d7RgmYCiZnGk8fyNLU42V4da2s-uR9tZyrtU2YHhVV-tACYoAIlL0NRSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
