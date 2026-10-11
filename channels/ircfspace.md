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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J8Qwtt3gxNWeZJExHZ8vDKKmdN4Eu0gHpmcHgcPiPT5uaztUEQSIN6jOgfVqc601dTAzPWANon1tJX-Nh2ksPlECvgtcGlExycRMfX0s3i2rE00tsvpNgQnuBIkJsP4FdKeAkB6LbuDrwyOCAtw34-BRCiIwf4zXNM5g0Dhyp_70GCrmCoEXyw8KKTuGKzg0BUtFdB0nFhMDgSDcn1aCEqLViphd04VB2-hL0iKHySzBf-hHqPyuh4KtOt1cPrdjRQwQf5Y2c1TZbmPON4uMjEz6IHfHKQbdwQ4qxFzX8eZwS3HiSjc3-uf5siFzp2nMijR1a9Ui0koc8j0T-BnQ9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QodMFm3qJy7pu2s8C7JwnVdtB6Iew_jX0ms_0t2bgNuGw9nJOQNyQaBL7eWl9ZPqFsZ9HNppXOa-AfKhd0lAb-nNtcBvp5u_45e_JpNJvQA4Y4CRor9CSrVMtyPXpKjtlSevk6jDMDc7FmffpmRrO5JTkNlcEqfC7L65Z_V-ucMq-Qxr-Z0aUSTt6mX0ERjEYYtUnW5sNNcx6nDlMtZE71K0a8MxsONWHfcbLt_WeF5PMJNCeXI-gOlQL3I6JRuaRhPGsWBV4x9E4cAHjONRQjYHtzp6rUMMmFJXSiNxaBPo9Tet5QiifTZhOkqiFF-q09mJB3BywsvsX_RhCd4FyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQdLgqEaOysvLtKbPAnx-adW8BzIJ6-0xP0huU23Xez7u-hpz55nCeJ0dbv_DcFMKhlODpF_hYov42S54UK5rViJfcvB8u692Yb3ylSQm7kKN52rjb3Kmat1hR9K4trdFA6tTSHrosF5V6SQFBTrhRz0TUmsLSpi4OAnwdqOIj0i9GI1ZU1FdrSqd3r_rKCsXD68LbNyLDVcKsoTunLxa7AlZP8kn4kBtGvd_wPa1xq4G8Z1FUoYENXZlPBKWLD4ecy8qfGO9ulepEknsbTwVDKPoePpLtp9x1BmM0ozeGBZxwWRZlxO82L-PC4wKlQ0tivh3WftRUXBd6dO2-oocg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdGn4l3jBYkSrai0qvkZzu9ezZ190EpcNzWDUhlus4UjoPX4Ye1NhW9RytYRxR9aw3CGZu8lRD3Z-gsyLHu7ziG_NK7TxVfTcD468XVthmgE40PHKai6vyOuqbUwsOE2NpqkeFRKXMoyLbzoJr9si149KX04G9MPzbUOdq2NNaljZXLks5bzfunUfzYG5atYzdCh17FM8ym0KCB7hOT9uH1_KWdLReUB9Wq3RUnj_SfDsLSxXt07lAd7O9JE6M3aCky2e9Gl7F8vkfHbhLPKs7GPASUsRaH-h4P4krubgiU48xIge6uYo83VLC5_7ks12ptgEj8hYOJMiAJNY5QZ8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MkrYf776dUwYtDaluTcZXd9BC94nHdq6nX-tjFJnLGZOB60x4i2bykQOd-d9XbLxFbV_GOXQt5ku3KZxtRmKVAq2GhPhUk_sBzTngrOVjaKiigbgPepCWq19yprRqiE1ejHOtL16t2OlIWm8WXKpvduN3b7Gj9RjUC4ri1AemQ6ma199pGhz4kmZxBLhk-lkw4bptu1100WJAF0QUrzorqgvhFmZlEJ5aWAD-IbPSLz-qRiO8rCqwKm47PIYYWOdazv8bOVjhJZcFE9HFE9pfXUWziwRl0p5rieCGmaMtm0K28mZxjrWaFfGXvA4reepcKHp8d3qE0WvZuZ0_0Ik6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1BMeek4DUSIONrKLir2-xngXM_rKQfvVy9xEBsZC-v1NGdSPHuDZYYSDKuzXXz1EHWzE8VfzlbotWcehRJ5qc7suWXsMMi3taPcCTGeN6aJNAcmA5bcHDcWMt_IcDiX835ndmUklDdP_aW6Y1QtMr-oDR3GZCPUUur_Q3a_ZDtWLxBjMrzpv_MmFU-yZo5jPcOJAsOp1qu5DkJuniWmPP9XXiQcBlrVj3IHtQd4_Yy6Tf5nCZHYdR2hdH8f17jHvx1-ABkX5Y8uh9PRhtUoaAOOtmyvB0rDOl0dtj4jP2i60G53KBu5hp6iMYoxba8H35Kv2w3rTfPk9JfFWdyqhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNfldJSMD9ArhkkzUcfFAmuWwF0waW_mYffix6B8QIqlIyTiUnwQPHmnkYQeN_J1iWDkv1c97AQO6eUS91YRMe82G2ooo5z2W6RWK49HJ2_agBRmVMfDj6LSHzSfP8VOzLt5gfyNaatIA6JdGC7fWAUnBJdCu7aC2gV_EMrwcTUf_XrUPAGWVdot5ltWTiEDxeYvW69BoPh-Bm_lYQUlozW7VgE64TEfrvrseujUgS_3-ThDnV93iNlE4EHw_oipaYzjT9r84XpTTXs8NIURfDHlCuWkvj1ChnvwbjmygWWwCO4TDGT1YP1SXrybYDYUiL2fPqCHOcKglFOIbn9m2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qwBw-2C2O2OXlM5HkwDR-7W6vr5Z6rMoFrNQ5KXT2MkCRZs4i0hatFY4W358CFes9qmwszcueIEnPujFBGj1TO89hawZuahu56HN7BU21Sbj1f2Gb7r40zm0r8Yh_8c5uZJSzY_idZdvMK5XkaViEbf8bEXa9jRGt0gZNUCr7GvAx0a6PExVl-M26sgTCsM5swkjS21h5hAn4EjnW6OLYZvgE8PTf1wfnTCwsi3x8YhB21TZ1GR44x9oCBkhrJq0YC8Asm26F42ztN7mJr_nFfXhHx2kxNz04SZ7yk1cAc07T9rLso0Y8HyvfE1EgzwdC3L6OSy-ag9Pd03etYtBDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pHZOlghFj7vco-WTn6Totl_1OAVi6bgOiG26u6Mjl_ACZWMPDtK1dfxEG7P2etWw69DpTSnZgyz9L45N3oLFwsP7GYd7mpHioFgvzNzyhTZuZocrZwRG_sxv1-UJ51HqOgpVezMOSWoQt_gJUIe3Aws0XhE3omgTO98qZlbEUogrrNieWP3m1i6UNIIJGbsJyja5pKpM8219H3K5uQ2pbZabTObCHbuu06KotrQ4QZnlGcJytiwcMIjaCuOhGDg7tYWFQ4_uevogKiYv-ftp0b99dYNHPNvDKKIfneHU6b18K6H9w9StI61VsBvhajZnFjqm4stePMWZ8NmeG4JLOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CqeyvQaUvW8Gno-UDUyuzt67FnRraVRmzk4scXQEdcpch4ADy_aNjjwitXYK47uLMnS7tNLdbiF4Z2iR43PhY8uD2Hop8xKmyH9Lzw4GTPQ0BpaEcpqCHlgqxcsHvvkgjKxr8vSIkUzIgYg30899eVmlb57Sn3ha5yPx2s2iXDKWqCGBPU6ADN2hyrpXsfrv537NabD4UJmXR64zvOWf5iPobaRjzlXz6aG9UvwOGpinjC7vEkNqw_lcM1Hlh1RTGxm6slIfDnXoco0aB7uec3ieP0vj58ztgXYOA9lWdMImh3pNSgyf8D-eqMB01OUIHDFKhCXJs82KBRjpu53cBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CmFRTpp9DdodjCbH0cL_by4mBXEJGZYg-jprrAKt1c7JTP01NfUsl7VQ1UX65k_JjY84LVLO3-LQ_gu_9BBrriyUyKLwTUbYAPQdHj9-yItzm0cs1zP2D06pIFrL6peD4OXHYxli7w-4huw7nsNfAqiXVZMJlNTh3EKcgFiUgAW8W09nu9ula2MkZaRmmny6wj6D2-tu6MMFHnW8k3gNKUK6x3ENlXnBsEF3DfxonIzrL3QEoEstDubCdfAFlTbies0QIS0opQBvwKs4Ra-tTSRtHBrKjdeZh2Ido2SgH2ad5lpvuj7KzBAhn3GzK8YLOfebMXZ7L75k6SGp6ChoWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GwlAo_ljObomgjMVfAfOio4tB6K1CZPWxYFncIoURYMwU5IuW5MUpfOJ-jNb3K3qbSc_JQHS8w_-7LkfTnKhyshKijdPKoQnA2J_W2bqL88LHrZp8vXdPCXP3EvRpC2Rro4CHVYBvyFg3mPgbzXCyUZMWKVHpbgy5ppJnqrRJJvtH0drPd6mzAvKsTczh4d-BhfvVg_4ih9U2TTm8XnX5jvPrTicBVayo4B4UPQHVvlzXZtOtAgC8LP6bIryeS7qELhwR2LSCQjLhXTA1HX2JqUMSyX72O4eDALZTv6OAKnwf5rC20n5A0_T1NjGOkpIG6SfpvZrH0i7kThkUnTfYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFKiF0Ren-cFH6yE0PQRBfVCA_VF82cdX2ecLyBVaP-0XcWt1OLtpBdX_3NMCM_Vmc6lcPR1wFcqfOXgWLBd2K2q-LcQoSChP7RuOyte-R0gh5WkbUdN6xS4bPwUktxRgFnhT7YIRzcvv1D20yQVYBA_FQxSNNpaz-zv8exHKuxdbuPSufuEEd45j5MPyV0i3QahsVRbZozi09FVg-5MwZN8eK0u15ldgUlLw7bj4eS2gtp0gaVxmeZASUbBQ7GTJSrTc3dp9zkYjShUra_pES-YFdkXNuHhGQl_M1p58uAG5G_zGQkKd6hnAZHBhNgN2Ciu3ZfJOv8GB7gAPhhkVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8GcMvms24GBN0t7JJ8j7QK7gXkMnidOdY8NXOboEi91qmE0YsYd7ZAUpUfTQ9ah1Bu4W5kiJjKeXN-rb5cHlEkDT7lga59TptvdvKCcyO7q3XNgWcE708Gfgu-ihlwNIDH0evgqXsAtDsGsECPdqOXs08MTsbL8Iisfl3ID6ntALDe2MVRUmNptCGDgVb2KspbSrydRh42oL2tig7cL6I_Cx20A7VMOCx7wkBtXAESEO_H7Hbpgl_NUzHsSvtZmU8eHJK3eYgjLMEbUWN7MQn1Kctc1y6E5gA8kIDX2JWhUAhhcRy9yf5JHFfQbSINc4bZuCiBT5zsdk7A5HCPk1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V19OQKHKRBvdzVZwmyN6c5EiY88tJrCL_kZ9NY7tvlibSauAhZIiCNXeHTcO87SqCQI6HfBwgjAjhKRvox5Y3wTjFQlzBvoxiDuiycdkKgqfp1fV5eCvZy8t_i35rpz-KZCBGr_efs0PpYpusuUXySMpfDjAsxlhX9BHni-He0jSib81e-B2L7r9Hh_ndbfW4hggmK_RUwlZGcCMzVSNJtcQHISsBqjW1MdElci8LGuRG_wsazv3CnsusufxhAnEDqHjseE_YTjyCXe12eHweNFFv2Khg9rQFFJyyuTT995xuwvn1_0PxMryPWHe6Kt-UHPasvATkpcJl7iOggLEHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MIIXiWBngLgFDWqWaAR1baohAOe88mOEGT-2Wr9Y_WQ0I3Uy5U399T0oEYmf1IfjQ9M8MYDxSR4RJJz001H4zUOOzcWXB0D4funKi3bHGJigjK-SfpmBhBl8cTDQqLq887a78fuOv6hvEwOjLmal_FSKbbyvUlXcBHwI9u8aSgjh7MqHlu55dktkYaGc9qEkE8zOYjQwUGuYpufnbflCtIzsrDLfCPBHLvScbPsLsZNRmAYV8d9iQdPpD6Z0RHUmF9YVEgPHkemz3W2Y54P-e4Sq_7UTMSUnZtimdjmocxV3tw11rp4UGQiLFfWw6xYcf4COkT2Qbdz3JZxbrY0i6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gR6i3Im3nhCS5B7QP3eJAIZ7yTRfI8x7bSJeHQmhsrpSdftlF3lgHGjcBkaH9skJTtLTyk_NCgm74Tde8l3_GddjNUBYu0BpS_SkG1eMXpy-ThF-BXLF0Z6s3lx2GypcOdSsiKsgq50nwMjlETljV-47-7pfcnlxgFIFCRrsQ7IlpLniU1FsPBh4w-r-CnvVZm8CvIrm3V3SZyraLhHeEM_o_2bxPmNEqPfnIB39CNghrrm_zWPnuBvVlNpWMvvd3CW6v4RTIh5ockpXrphwW_ZxxsIuTbSTb65Vg1AHTJqD5wTBVWVlZxkcyfTwg1R0V284CWybWAW3vdp5YSe1wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JryQXv0mjvmxQwVh9flgcqY7Nwa2E32wgoE2Fy7dsc-qimEBkFniuUmDWfl7CMl5UQxre6PIs5orGqB6gEEPxomewxD3NxS9XzahiChiieSi4sQa8xNLetLZv6MsokJE_cEVyDMIv_SnqzxJYR8vvebKvsmmD3tqtyC6z0im22Z86U6PJu_dv7rrNQoCAOgZlbzMSsKKP59SDEz7Nv9jFC-xkifUAlzcI6E9gqUat1uSN7EMFXlCGRWUg5QInWzTBUsj_QG9Bt12Qu0PzrYzd_NRakCfQulxUh5OuEeS6kHrovyGQTvooSMnGAP9WKvOVMf4NxJMnTK26ZKN_4dL1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rx5DKbGgbPkiEpBj6pEfQMuFiS_klwuOcjRq3GWpTJ0p7nYwA9pR77haVesshZpQ8te69TJKzxn-6HWpV6c5KGhYFgmKh6MmvjHFmW_T7DYPW1TyEl0iL1SRXKB0iqvBxk1BB6zB-m4Er49w97Jk042PF1-eH6toVxzUVTS3rILfGWseo1SEl3ZOp52jabhv67Dj4vx3tW3jNvlu98-gIHZSS6z0vbH2R_w8k9q0iQNFGZjtHB1XJlxdVN4ruz3Mn9ZFdtAlO0d0xgzeXdPMYaukwzEnVcS2ywgQf5TjhYpudO5xOIXadbvtjuMS-Q0P8RiVEjtoANFduCssTz_AuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJGHNLj62st6IZnQfBLmPTZ8lLS-IboMPx9EEIw5oICM8JFbRiUAlSBjhyNZz49pWH0dAvkqJadDcdcdRLGyankyCvdSIlKe_pSjBzMQAulXrKGRfHYpf0CVF351mgDxDkUqZ4t2CpocDKz3S6nlcmM3yXD2RNL4Vq1_hoYcIKU2hp_hb-5Xa89tYN4YyP5aHbKRGJ_u1xqKusFQP4dFZTpPbY2CPAnYbGWEgZPt7JXpbKp08IXb7hfRXBJar7ICktyVDhlO70W92qNF_uKDAIALfXYyi-MuGExDYl9OLuxgZmK2UEqSq686hnLhJXyeFY7HIizQpOqF9apaDP6CLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hL-HzS6e57msAUw8IdWTxnPblcr70IVqMVVPXaJGIJ_yTZyZMYx9gj9_12WjRJIHY3hCfFtfBUHvsDMt7JufSVa8mblQ4WNYf8noirNs-ys4HghSP7RuO0-dNm9jlOTwBvolIgmZlzS9DBdjSKd-S2qacpLkSm3svpIYKxamPbTYJawPl8RCUnB_LjGCOwS97JCVSUNJaQl0Q2NJaKdmUcGbau9vTOq15qxvA3ia07VvZ4YsvRAdxxfB_gpxoA_bHxg5oIYK73g3x3bcS2k1miJWDx8wxR5qEGNBQxMFvwD-4dq5qvmrm50Zcr1n1XH4YSOdhBQ-MY4YJe_NfiQ0jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HhwbTL4Rpn9a2dnWoRFEq83MvPE2EYs-ttyLpuPmd-9R726w5f4KqYMbBLqyQQ4-wPls4cz_rEQxToMtg7ouu32ZMVC4u8vW9giH6x2WvnCmRrFYT3eLoAPUl4PtFEOnN4Nbrw78J7yfHj3sDEew4wELE6QZ43lNn8XZng2ERjjWhVyqc_zyt96-CGieAMzjrI4O-oydpt6OC9u2zxFJj194r2PA0JQWTCFo7R0EoSYUnosIkfCz4GqciTgaWvsBcvfeGCeMyHENoJ3L4qJIQ8a7mDhIWIOo-F57PeQMfLcCPFko6C3S1Fulo1diAKJvqnX9SZCneEPDJ5a78JGlGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAhrabbwsJ39XVeg2IGIATiEAjQkNk30QnaREyk1R-FAyq1M1FDnfo17Nivxrff55xnlhER1EvmFlhUX1J_au-a94kp4M_0OmqvWTE5zTRuuOHoy2ZcgzmApi1SetgcYix3mDW-PVLEQs3uPFnMDR2dqyzU0yzIxP7qnmgC485A2PLXBYEZVcaqBnT0g196fxRqbX496YWonrzE-6X-SeT7G0LrTo2G7qUr9fK9fjdTXfToE7vi2RtJdWjGDIAGT9YGPCogBMfCVg4gfkooWb0xwNkGMQWA14yfBNe3tBm8re3QnaoK2sJ3XO4hhiNBE2m6Iu5tSk66YTNhyMJLSpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t8S5GLTUMegXYEtR10Nr-TpzQYLGFhk_VtE9OZtWDSO3CUVSZ8gv-XEaZO-elz_O5ec6jBcgd8AB3TBmvYyH2IAs5UHuWwbNx8EXow_5RJge63xxQPUUb3rrDHT-pajmCFT1brxnCde5CaDmeyC5b9EWzBltevo3_scevVWuoIXFHU54AQjoiKj4Yu-ak6-kuicOxqCrIj4LCSC_bdjzfsVTX2FBSEQeUB9EEG1JH0q8UTIGtWfypmdMyhp1Le7FZCzSG3PjjM6ANdFvMHATqdZbAPKuh7lVyWLRN3VaviNEUsAv1ie5JYKmej6cU1oJDtdKujI5dbIu2IVkY7WzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQGJ4JqHrSyivX287vazYcoOZXXDx6OofjobW5PRSb2tOqJrTtAnP3Lq94fKVlHSnpA6pD4ahDReapJfRR3_bKWz5iarENeeYN3H3E7a-3GYsqQXoNd_ufFvgQuwlr950KAMF_PTMhpUy5R8t_Ts3QXx6KUFqxKDWrZq3rW6eR-qr0ktJhfOVXrfsaitrZtt3Q6OK7AjvMWzL3zkzMA6l39udIkFJ2dRZZ1HbU5PdghIkijb1GLeX8yshh9vrejHnXpGR9W4LTPY7IdgAriY6mSCbs0HWQrVDYxeDtO1KTHemmovREoL04IDMkw-xb1R3M1WVB4cKUbCmqasifd-Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUq_VoVSFrNp9was5yM6_dWgciIcbj99h6tXFknqoeoxLqYRJLHvsl9NjhQSHokYC4u9hAK7uUuI5DGzBUqmYXTVao8YepNyHHFG8SIOqfjL5lASKS9AGa_gT6Yi4Mb1eij_dNDkOxVkLHoR6APHEb7PsymGwCtIMeVsF5kWbhwTWhjqxFrI8-FXtYlbLC7xVdAY02w5Rh-QEvMOnThlUiBZBTwbYCBTuHs-6kOtBYfCXJLSEdymdth9I_pKseisIaJ86toMgxBq3GwWeZyGvLG7xJgvFlqVpHINr2SksaTAN69sdnK4XQGcFIGKgkhfAcpVzHSl2OfFHk_ZGNRmJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YOfIAw15_9xSRMI0PeRCXkkaQW8oGLDuss46fLxTXGdzTYg8ReRkH6RvS9BdU8lMNG_JdBXMM_LPvyIGpwFp53JCM-lWXLApPiVxIOlpxvAswZItN_QM7TlVLDFJOqaNcTfEJaha4uqR5IibjcqL8w-MR40qor1vaZASiq9RDjH-8MSJl7fSplxSKkc2_GFR5OptoxASX89tKlMXP3EzAV4BeIWeMHB39rWwhHpx3pzR7lyjLvN_9bDcsl2VzhTueHy6bqOJwD1vzWJ7a4wjmcXH8yhcT1vqzukLIsom4LWoQ3msXbGVIomMlQmtGSF9xKGyiKSCV_fBSDDxY_aMEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NVKgqN9TsehQ48RAMYOws6kGBYEnp_vuhFVmHvtTxSE74IWXMRi8hg61K2-j084KF9aRW9Zyjd7UXVfI270Kq4tf7uN9zr9wgFKIB9HHKleesNHTCa5xsV9l0nTwCEHQej_4Fc5qOajNaipMWhdWOGnCXUj74AYd7zNVOQSCuBGgHf6lEqp6xTOEqKARtO-K465io7qbmuvye_Bdtd7kn1QH6SIi156EA-bu0RSNsIcehbUbw1UMZmmPuIw35Ejt0hC79JrxoRVqyW-OXUC18N8DAfgRsBze7pIwgCgBe19A0t8e-opnL1GCsrSA6hRVNiQiVNcMie7YwZGd0CcjsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ae7W9V05oNmsh2HN5eUdfraXalcOcp-5WiHZyMRlFeb75rxrNJpNqV4RbP4PTGHREILzKL0UeN5ynwqbL-9MWPQ2T_hWB7NpkOd8Pz6tA1_x6Dr7G1l3dM-L-U1bpAbotbeiL9fjudrJ6NIYQA1-ir6mBu5rdKKVanN7tB8DtWwFvBpWgB7SoIKqtUzGrO-Yj35vqa3XHuQW-86kknW4a-4yQXXtwMLj877TSTVf4Yn4vZP1UI1dRgThqdx2idvEoRREllbyiiTS71yHJS4yqaNOfqGVOH7opejQRleQiF7CbLKvWeLviTSi0xopfC2couZMBfhG9u_RyQ9LbP657A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGkKyoLNBmwOVs5P3XhOgvy0loRB2osWU9J7yCVcW15u8U9sPTxKnDNQ68rUjdmZFiW9cj8VMIDxCRY8576N7CCQyj8bgmhgulNzYvug-9sOxgvqIU_H0BA4eGUW5q44GntoVp2gAArO6GAu3ogJy8OrCOQPPygKYs2LEe_iJF6HdHKX6UN2qBv-k0s-iCTcYvrd7M8GGcmYro_qcCBgLzQYaMcHTAc4bBiATrM5SKOgfw-zIgqhwVSzBn8roo3WC75W7lmN8mVXjLaVqdb2X1PBToohm2f6XuyPlRw9tsFs51SEDELEeL2Q9gLgxVZQXqxFoc7fytl1i8NnLEVpvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RstCrYd9Z0Iswg6iPnonGUTWhXucNGTI3oNOcmEf6gDycYj_IXBAOP3tArFC4xDe8XGDrMYRgBSmsV4DQlolyDKNYCeOA4esYCPUM5715vhvJu7onvmlvYWOym1ZzDUKpqyLTwlUk5x_TFBkFgcLQABudJmHwVLpLnCekG0RMcsS3A4XvpLIu4gKPO1N3Vvx8uHxrglmWiWfAoCMPQrxCMVtTnxqmXqvdyg5iCivBxxuGFbZGYISX8HwNGfW3J9KhxWqTnhz4d6bQB1LDgsE_oLweecLK4R3Mxtb8ifIxko8lovPj80-c7_5gozQapdjnjsdyF7z5g2MRbER9FxRJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcC5ppGAQL6YAt0axXuEczt0QJae2PBy13gsi7af129jrZ_PbZecw9ioPfC1FaAOSP-b9GaIRF0qE8lBh7gjfiQSQt0uvukvcVfOJbaSWQ80cQw9D2IXYMlaZniHLMZB3bVqzyHgj1xq-CIH3Ucmdgu9PbCRBJE-XMdzWnVl3p0y9XoigdSaNjHNwOtYDY8N5LlCBiAUh1OHyU-EU3wOiZY264sbikKgXmlDqzu6tBqN_DMakAyna4NLQQHM9YChXoNbJWJoe82LTVoFifMqCZ8g_E0lYPUiwP4hsXd8xPhQAk19cCiUs76zERfJdBl-hCcyD_QMbSP-44idCtb4kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_8bD19heWzUJ8BFlk88XzKZyM9tHMHixjDySF4PyRIqnbNuFuHMyBdla2p-0uLeMt-7p0UqVFMy7knU4rRySIxv9BtDbcdTODxo0eTYUf7R1S0BimRYoIDHJXnghNZ9V6S8qclv85NXGycYlB8LIONa4Fsd5UNQQT7FLLUFz2LXvVh0BSbCAXjpeJ4MTkoCiCYnt_WBUrGpb_LSmWcS_dYau6y0Bg2OTG9fyDFck5H4xRf0C2gjQ1M-OUKKp1ZDGQLkhu2SwMSGP-HTVC1LnRkdTbVEzX_qdi_IgT3gx8Q6qxqdQMVsf0FLXiczZBW-ykoUrmBHnrvrQhXOP7BIkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OHvOdIjXJViz2YjEyYE3rmWggveVT0Uf-XYN0CzszC8Xlnl0tn0e0ZZgQngSR-0lruwLt5PE2BAqD8vLii3vLYGk8hMWLLrE2GDfiC9yFdR8m7R_8ys7iSP_VqRBGmPQ7g8bxh_0coBoTGrGfsDH-KVgLZbGSA2EWdIqC14vkzApJ3C_bm7ZHlX9uQFR7t6L24X8M9Wma7_98gKKAlMOLzdMEI9Umd7q-lOnnpif9QVkpnf39U8YxSVHXdodHfn8O6UBZcdHdAl3lekxuIwWo6Omdro5XAyY3Yr6eD73J0K2cnUvuDpQpAvt9OQQT9OfpvL8ElVFjTMqiACBkiHn3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PhNDWEzt1qUxrzVJz7_PrkX-J1pZiTLtd6tsa0cGsQd-YGlE_BM5uZoZibQ_3zTLWyBEOw_pKuYATRLAb1ZLZ225mNX_iKhYZVVYXHOBGB0KIqcu-MrI5x6ssm-_VBU-TqVlgHqLOVBqmPaHpCzOdvXGRzuJ8zRbJGtOLHFHN6jEQ8L1ow0dvqk-sFNOn3Yz02bX46Z4vrWtCdjQnw1_0pCPQCWbp-52TI36hN9jhEdEJgzyXITNQlHwx4OjKNdoAe57YsgE8L2kmF-Fy-yWhIZCerfguNyKedcgm1Iq8zg092lqSXp3gtBJMBTQP8Fd7YiBv-3N7qZ3LE9kMtgajA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJ5dI6DNz3UP2Ma5nJqywwV0b6YLDUB59d-vmJBOmgSIITc8lcZVKOuFhvw1hEiwo6GGFfeFaj4HLonTYTvgWdMhtI4BfkWEkNY5yVZnXw2tYDuZY_cKACu1ZzWZuwO2pBpHLUfOFp7s2wGIb71Ug74sWNSJnNeNLTY6E9h5W7ZDO_p5A0SIaiI7gXqoZ6ppbHcrAPF6QBt3XM5qKao71oJBKk7QUI6Popg0cYoAATbDl8SPk4Y_qndmaEwcGoNfbAAlF1Fe4prDxQmzTG0QFWsWoqAfeF8JcAWPTM-Q-AwZJpcj3Q9MvAYfFjvYw-jiHmi3g0J-S6qYM9fLcHQG_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jnbx7DleoMXnUU3xSqNuqiUB-vKp_e0S6_5fQEhWFn9g5Q_EsW7j__gKGeG6xNNdSK1JySjORseWT-gUTgGhNP4GYrS_bjh3DCl5ReFzLhr-HmuZscOEIt6VIh9g-O0QBs4EmYaw7UxK0E9ao7yvh4eymeo34HpYRNL4Nwa1PBKY835Bi0Zyv03mc9s_kbQrBc6O4vK-DKURCj8RlLTW6gZMxwI2GjrcTUKOyiLn68knNuSrm8seO0MkzF0crviOpohNEQJdYJm2kFihlZPSmJq5H-aloFH9G_68Z_sRboXHhCmIrZui2VY5f8d1HO4nGeloGguI6HPyXhnysr4DIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GwXCpFS_B2pVJcGEMpjWqN8w1U4p6nm3wWhFfykokWayXPXwck8r-eLieJgpDgt12ICg5q3D8CNvuhq0FrmqIYvzANs22H0SaheqXidgVNfci0mtlp3HKLvGlJCeNL12Ln5gA5Dm_L6hTHKu9KXF9KtZRDYPm1RJdADO98UenMMQoC1ze3M8-6GQlzU3tpIWtcJyopePnI5HCf0vb-5S5zNc2vwHejkZARnMe1TTAgd4QbOfIWW1lM5TU9euWwIbAJ3Dn49d-2Yr-LPBwrWOU63-b_ZKa4mqwc8ohJI_ySKETFPuLOXsVd4qpvu6JcVE1x37W46e2VoTbEFAJ9bMJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/byUobTXFMtrGVSh0FVJJ89lgD_aQC8YeyJ3x9-lvjGGZ8QU-lpcP3eLm8446W4f43_bEZymIzUjWrnVhhxc2j8DKMJUjzeb_2nLpk3EGiezfgEJa6R2X4P9QSw0ucMTeS3O0Gz6j7052TMbkjr4W5SMzdANG3IYQYdSN7RF1kYacJK8khgC9i13xOJqI3DkrCziKUqh28JmrhMxps-BrgNcVayjqnrQKiv-KmBcqa1aHOQNsVuF0EVN4kwHWAKZNR3Fp14kLWg_wDwyzMAn1F4X0Pp7c48Vf7psiHxLr0DqdY8KxSVs9xzFodOp2as4Q6V0prU7bNXj14CnCNRslxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbDD5rXl7X2WXI3GPHzGTd0GMYvSywEAk57GZuwpIpoj9YSC0vWeHyHjmRAhHYXzvqSx3x2i4rRurKfet2S4YmWcXCDt0Nc7C-uqEHtgoxbho7K2d3FkyDJ4h5CPWOOLbXOpWs2uBLDb6MNKkEWBekt4FUE4OlwypRsMzsg2TzWhAgJBsJ2pKryq9pQfeMH9mb1sQ0tvtaVwDIoImPPSLa53TMd_HLczWFJN7J8WEGxdIq75uAP8Zg6aM8HgP50fRfJvJmzijuerwVr8pAATTplmniC7Gk7l6sfCqpMdYHoslggIKnzFU_C-BRCdFPLUHf9PTI0rHwBLRFBxXtG4ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QjuLyHcHfmw-fdechh6w6zwrNlBPLk5BdDTEbGJdTMb9MrpkoFO6kiyun9M2Se8rkdaltxdL2BgkiTb0_T_Nfsd8juD1HQkfNcCkCXc111AaCQ_0aDNM03m8a9OZaK8ssorpxZx_QehSfAPk8512r6hinrzWm9wUsZCr4qSRY-LFeMY8FaJL4g3JCUwsoCzTXn23eHpqsXCV25qGTWL-gNpk52pMThrBG7yOAzqTrb7W7ltLbqYeNanV8XLWZ5Qhx071kWcVsFBGwBS1OHbm2puhIMsiDmUpjk4CvGsndGt7k-ncmvAi3cCaAcGNbeWe5wD-o1aftApB1lioyUkSOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cjngoG_nfsVHL5tqZfCw1vSoD_jkjrth-Alwv8nU0hEm2guL6Ydz9VcOoNtcw4YkR0eTxnjHWSV4Mxek9aJ8HFvk4vra2WFhZZdEjL36xkQF-CPqx49jVNzPwv8ZIkyfz53cus1QT2p9mLPJoBu02dFZE7Rt17MaPugyfqdzyq0FLrbV0FWBA3gQK7Hcf03QHOgV6d5D-Wy8jaBpdUc9eHTVh3EjR7Y1OfyRSucIevGgl9sOH37TObRyngpNFTcMGIObGWvoKij4i6WBjJAPEw43kvIyfZ0FkESUPQX0i052oedEJBHGY4ZVEkzDw53T5pWYJbcWHpHan2OBdkYUQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-yz877oMRJuo1VGXM7kJl_PuOadeOn3_h3m7p503ez6-Mf6krvjzeuRewHCpL3y9oym5Gp8ix4HSesMLUH1prhk8uIDIcjVDt57Y-2BQd5-Dnk6O0EWuE-4unyG_Z3DDhlK_z2F5VNwILSvAjiN4IEfGpZL4wHKYFmEQE7_Ci900_n6yUPTTA464qqaI7H8xMl4VcD9Nd93w-bAcamrM6uppu99sG71jh9MyyWJkudGvrKMTULaAq5xs6SyUFJ8UgHMyPxVfesHSWqtdhoVbeBzq4up6z5UCW_zJ2MoG2imU46lESsk8ad3Arc-ljkVNPtVgLCKCj3QpcoskV9Aeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RhvDus82PfI6DxPGuE6dooznSpYgeHWBBupZ24VNkERTX_N-P0m8v9c7fOME2KBNwy5mQK00v-JH1KooWp7Cts2AesoNGLz3dOUzq5M5_7yUenItByf7K9oHRaS7fw132xqgTo4yTIR8HH4_SdYwbcvfu98YOWypQ8w6L9ySsGGUxAkYM_LLL0bU_l6uKjA6iKFcYan4Due__xt10jU1T31ZXE6oKr-mFvr4nV6mjzUhFn-NsAXMSW-SWYozVaVRMXfUHg7Vgmt_o3wUVllcARaMqgIh1IfiXwiWkm5aKag226st9ZlK_a2X0t8WlsS15xufAoKmcR7xIMasWpRfOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PS18X-2EpQYSiA7Z6emo_YayolkeTJdvCipisAAlNupmdy-gFwaMkGSbmLlsfDo5-4Jyh9VxD3C-MgFUzVwQJjwXxyYl-jRgf-RJsLN7akScOLycmaHNDhB3unpTaHWt5oGDzCaQeqBSchUa8cQUGfSlJ1n2v-P-y7gPpt_oW5aNAU5HGNLAps0ED0PLo7a1E4KAhJ7626zQn1hzjN2bf8gbqq1gv7prpthekA6ETIASWeQr-HPFDCT_lORbo1MmCYniGN3Yyr5S7_MXc7LnkbzYJ_SEiY0GVctxw9vcZk803DBpg4AzIdktJywnF0aMA92C-F97cWHpUczNyq9DsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IMwtwMx2EZ1aJtgPYyTpISAh895quxEfpfk9X6W4JHvgvp9U4iypREpy31sW0uQiYL1g5ZkQmPEjtILWRc_iz07XiuzodZWmItCVF6YjzHfgctVMBIHA7X0bqoWgXTRvLrIgLUf1jbzwHudiFbWo11_m_zEEANdOYIHucRr7XNICwZXUoSz8XzZnSzGDINHSl0IQWtyfUNbSZKz1EqItPR3iw10TzYsnKKOY4HxUvc0tl02yjhDsj-DneTFJT4x3tahvQT-HAwwvJMfo60UNC6pOn6uzt7-nFvuN5XH_mEJJcPZFg0qqYttwt3kn3ayKPg5y3X7-7QO7atVY81_fng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A1DaB2dAxDfI9PT9wmBt8RUwCpxZcKZK6eZOZmlotxP-ZzgAdB1ZqmRA9Hqh-fk544TrN5E_Wrl3NaWkmgztPmJfLMZTwvvLycpKh8kOgeJ3Xb1EKGs6BQEK0ocyeWtQZIAxl0OqJf-y-Yg9DQ-xP0qVQMVSotEltb6ef5gfTUfZLkB32Tlfumm3oVBjc4YPmsmXRB93tPLXWzV2PTsrDzIB8dhSqIbigP7D22_BSeP5d99WArGGxrr_iIJtZ_sZwKn_tdq_OuyRJGVv9vXqIh1FhVcbkdQm-iT4ZPQ3VO0wLOwdCcSr-oKIIQoGZer2ltrl-fSpw8RkoxtjSEq43w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SeXtXA9lcjbKh062LoPNhSEgeVWY-2Nh4wuGhUm1sTUpCzsZmz-QI2txkSsl6ilc2eCBt22KQhZxn29fKQZL9qMPrSper0-KN-yTIdpNOGlmaO7NI8-9BYl94xfGyI35bDbV0J_IMuPBdVf-Bf4AiNA7E7sjJz27Q2dg50PkxkQfCdGuG4lYH5CYTm7XaALciL3qjA2J8pYZlq6l9_yUPjBYIDNbiwdDmgU0pygSQMROCqbMJZUEShwYq0HE_rwpELsSSDZNizLj2yUU3rv0JH_lxUgZdTRsyT62S588NJT4FwWH77sNRLd2anGwU5RNvN2fC8EF-ntwVUj2gp_MZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EfSYbc6W_B1kI3WepxSeOvNfq_SoCERDN7qf6kxa1btBmo80r1cn_EevyE_cIcK3_Lpsx-uol8xvigpFU1Gc3v4aJEruBIpNO-DXNp2L5ESjQP32RsQNyJPxhDsRy7ppjPYTWZqI7UzMwMharzLroec0bEsN0Y6TCLxyhFgbteUsFzCX3yWexvWKPeuj1IwXN9ohWsOjZ7y3WMGhtcPBGgzh_yKw2u0NXk1dMKkmg5BGJ6C_0Bb-8jwWdOIzbbBt8xVeiB_6D4fZfPmBk9VNwrwt2CvbNaji0qGawjfpzmhcrbrg4dGo7OT3v8w_mxT9tOlPdYgv3ERnIbepWk5UKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NEVKiQH2lrmx6IR6o9WRDIVsr9cmy_1lY44mCPowgrcJ1B8C6J1o2RzoCLCLaurUTUli6kH0GZRbxbV0G12C0Mz54O6IYVslVPRg17Q_BXZUINplY8h-e6zHeyTNO395Z9aoNxUOoZMWCJV2pb_t_xdNiCagIzi3bAlld4YpOMFH7gF305eRVDF89VrTNez6Spw_PljBfzMnbEITOf5obsfym84usSFu7AJarXuYgpERIQwHs9yTUdt714IB-D2pTvdlf3m5JqJ7P7wSJOKWR9K4zsppl8_vV6BnimBpctGlbHAp_djDpAYopfI56qjBP5lMcK-qGFAay6L42IBlUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQhu8vKmhgv1Ae9oqlpCKhmYrfNxCix9Pa-IoVURc_mbFmRrRGgEO9DqyN-g6RIa9mbzSKs3xpLVM_WfU2Tr1e6_KO58DbMDDEXVk1YD_HUKStg0JsX43AwU_nWzJQQyhaddstVeQjs-ppXBP4JgZ3WmdktQJD5WMkWYByuDpfsrHnqORUc8j0l5tH1r1mdFJGhj6sOTD2r78JqW8bnrpFmsuGm79_52bpNtav8wxGmGRS9lbDyQ62O24TJMN3VXX7LBj03x8UyYzvbqWXpeZ7Uh1MzvUdtAXhjAKpAGiY_PuZeOSob-Pa7rSkJ9_h9eQCEcgVRbQYLsHZU5OnYW9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WvXqjHeL13K6ntWh4A0Z-1pziiNrF_K8hGpJB1Pp-F4RBOvDDd9byrxA37LUeYQ3z1c391DJLGtSIqFS0ZiK6SrAxC8y_WGmVGtU_NDVovVQXfdBVWhgA5Ke_UjwHg-KQhJ3ikqjmCnXY58QWRHgh8fJUhplYlke2OPlyTz1H2w9_K0fxnCQuzUpkJ0GhhvqZ0fPQDvAG8pFDrc6qj7WnnUCN4GSgBVaKzPAC76z-WueJAz5yMjMuJPoX8rpt42u2Jaicl9H_Z26xN1oYhXvgnEyoOG8mw1rbyT3GIje8vSUp6F_Zz8Zgo5WnXQFj_jBjcIE87DXlLk82XnptPiqTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5ZMv2-lbl0_jt9deNPOO7_xVanjEKFLK9P42F9QQ3CtMzJrL7rJ9qRt4BZf1hwk5UN6rYeDTB03pjkPQplylk1uj8cHjZfvPs0YcmlgSd9sJgpMA-Nzscm6G4_s55fegopMteXdfqRVAk3jukspzAE4PSNysGnAkUr6hLIvTN8H7JdRv4luNksqlLGBxu79mpbrfxxOfo4TNAua3rDqj17EBP7DeLGprYXieLlvMvQv8cz1ZFOhEtLm-u59Nw6YYyZLp-wAhVTXVHDB-rVoa2OxynSlMRklp0AYbSZXXZylo4CK03NVvPolx7aNgFxedqMguv2RXpAPvc-S5el-0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PU8w0ASYwMe31LI2lb71oVAdrmHi3R-TYHA5y4mJlHXL5znOnKwVhu2UXNSRA2nv6Aq9lwm-xDrzL8jpmReXw_h7_RIgnn4UZlXcs9r02kwMynhr3Yf8aVmLDUMUS8djGkiH6E8QwGALb9ZQzhMFcKwgSnOyLcqvYabPUVlnxyCgJ4Ch2YMxWtUPNehhMuTWXlORQO9S8euSX5RV89ApdAZ3qQTXS1n-NOLw2uj34vXhsipvMBspIrki2zs2LTx8KdnJcOpmh7xwEbrDjzF5nhdiaOTNTpr7hBtJ4vIYnNMrCU6zJmPHv6oWqBN0SlK_bJuz_HvmZJlKSxfaHBELGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uSgqRJQ4EnewMcfqw-Xw_8rzV2TFrT4zMq75ARJCRT3kGGtQ3U_Sv6zRMZxnzkb3kyY1TT3T3mI8AwFtLWIBQqrFd-mJ0QPpL808-Mrt9dvViWruVKo_09nhTXdCfvI-36h3eBbuJMKDCMQWYQkJoCQgfamH5DGe65MUc1YM4TB8b6PJc76nAKp1gIAjYbtAG9h_bJ0xzK_PwE5GZ-E3Htv07PyYtlsb1QpcXmOAtiZkfbw-l7PxUQpdLLQch7C4Fh05RGs8v8U5WnG4FmaTN2XZ-zbM06kj_2KHYNQolzfzOLaMivm_YkSjFmDWNR2CqheHWmNqKyOg6ARZ8t1lVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nnllIyWwS9T6n50CO4jPsgQKjrBGcY2fwCMPbEaI9880DfW4TeGtmaJ1MMIarRIGut4nIeB0kK_Y3_Jusy7QeJX0KYBJHm6l6Ukd8XzuobfK9s7_6YuPoCSVHqFZewXMrgNqe42WwUUCCijGxQ7HIGeG73PXoc1rA-iACWuJA9kgUHVseSzdVGENBxwtzpptiYfABoC93QfXI2ggQAXNbt8j8gxWrhpSoPN3g9UCxwLGpGMXFQzlC5tWykLJyGitJrwxkA3ueKMQ9jeAFcPF4fZN35syM0yx_xonYPF9J3Yq6LNCfvTZMX61zTlYhUDVllGvLgq5i1eGjQSMvowDPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LPT-3uupLx4wwQJIvVaWZek8sgCoG8ocWMmPRoXCxmV3-ujYagzECATR46StokoywXB7qS6weRi3sET3BBP1ZiSA-rfIYRYvSncYYpElMoLUvsw8bVxaB6i8GfQQJiQUHRXvldn3PEjsnc73Ph9Nr19rZuVNgkTJAiXkpOhrdSGlwpucHh9z8yyBCKzPtHsByDUBRQpPzTIbbeBSyiWxxjOc4mEDrO1YQ3XA9Hu7lS-8E9SvsJPHpL6sOFQP87Yk0cwlKXDR_PQgVvT8pfPYeeMLfxxtqLkROuN4Au9AueO21ZEiGYWyViAfeDES_u7N4JhE8-5heN2nHVDHdrUCHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f7kHu31LUKyCtaED_lvDMItoQcd8jHvMBtcrLG3TnRxpGVHVqFf6qkqywMU-W03m5hd5iC15PexkjB2_rpNiDGz243mTZwTwowR3zly6Bx0XNXTfgXmj2DVxgExrIUpiDtUpkB7QdkB2y1kKKwfHq50DFehulYhFkzCoEnltYihOfngptuxY1gz-zJQSYiV9Pu-U_k4igM1KH9KP62MYouS2uxxORVvdcuA_neT2IF-PSFL-51-xrb2hk1uasvGDwnDfNttwwGyx6GHj9XD1kSUBqdJ8Ms8UqIGrZPLzuKGx0N15g-DP8N5PNWzfWNi-bLgx8KN-3X-HlTm77RChVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QLcaKgYtCMdHd2UlJl7D-i1PTLBuxO2iJcAz8-zL-zMAM6K4Two2BulrfuxVMyCT1zVkspatX5DSUnPQPsgVUUtnve7za_FuOdiT9DD-LUOVCkvy8Nz6t2SnEywINomwXYxQBZXi1nuLPFxfv9nKk5LSVbWxfIbCsDl9DJnZfrWIe5VFAaCsR3ppTc09dxBm4X4-xHq6ATdO2T_2th-cxoqXcbLVxAv5tcfXnVYwGgz1Nh2TXdV7-gHISc5QX5lEu1GyeT0jaWGStl_vHvJiNM3CcImrhyvcrx5jW28tZ7xdCZY6L63WVlt_2xFv68nk4SLyHOVKN837W5Fr4O2krw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2uau0m1YOWB922joDxGYonjPBQ7mZUTV55_SjcIS2JXrp4CzX_c6rnkpqAiKj-UGi9f9-9IiTYTLtq6g9dvt0LrsIj9-ngRzXoeWWpT6NsqK7JrEGl6Cy9cc1jeccO_LZ71XJrKZ13_yjc65t5tetDO2HP5eTkp3oHb35mASk24JO1LeqF0A5ZPffH9gtV22pmYSTzl9QWzghEG6F7xWL7k0mxNTd7Aij8vi5vfLN3Y5-c2NIcbxp87IvhOSDq1WlAB_pH2bH_tgf9UMvs5jCnDx65FvME84wfXNTb9oiskLV9_T9eSpUhKcQrdMfnyFEOV5ZudlUljlkN037rXMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C2WuXJzUMhATqFobAjCS8hBgOjM8KNLOfQXxEoKr4dVog9SABtxYQuZj1BcJPwaB2ZwG6ZMDRmJlfcwA3i-aj-gl1XKIEPMoS6LDeBCzJFa-Wmpa8QEhUbHgMwsgxEzcFXPYFomwE_smr1CswH3Ors5hIKIz7qYOObJb8IU4nMA6VkVNJrKyJpek-3yJkCQfn2_e0y67Ioc3kn3weHZs6EMrhya6dRO7ryJ-5wz649foIJNZp86iuORIFAqVI9nAxaMP9QD6iO2rlKbZFsblEMfU9GEcv2rR16J_RiLsAmVwTJxFsh9ds8sooro1lwYuadrmTw4Gk-M7CFqoMGeUXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HR7k_x9oMObosuHTPr5VH-uFcIRYfbiyRjIFxSWuQi9wjjYV7nRceAWS4F4BGutk5wg9aYCurZPvwgXgT37uC974q-E2iwniseczd1bsV8is2X2Hn8lok66BiSds3bodoW3_6Moi0ph9WyKUdi63mO-KBWp-r-Q3nVhoE2Wo7xUbEZ_pKkzbjPjhJcUdMw8q_tluwIcZfQSEXrdYDpdxQGYhB7UAYWE0kNycu8AXWjerHJWcNiVSgfYsld2oMjpgk7jtG2YDQT0iAUvL3ObrAq-ZZJfNmX7-QvjnzbAYISCzuZKNw4TQ24ZqZGvhCMzfTKqn9QhnCwEedfE4C_TFwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nrdk16XQhwpuTb1qL5meuxpXRkbEkPHOr-Ce_O2K90_IC84K8lhHddsMaj_tS9qBUYptm0kQ3Sh-cWTvZ0dLr8HCuT7mvONg4QiErZ0pSCLmnzgJDnHBItgpW4RA3LdrPZqlCwdBledjoLUae_qc8ZxU2a7LH5jfj4BVLAVYcV8X9B0lPu_kayt_dID6NLYIRp3PQ-1imXZtks4V995Lky4Br2Ky02Az3va6Q_9TQ16fhuaLJ-GOb0JFleeb0BhsttIny0fd-fn0CVbTl7QjfpOR7p_cDm9Ii8m-Gav8flOb-iYjDC0ZU10lqfG_5s_U4Oa_WswWTUgCoUS65uM3Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ps7UlZqG_tTw3KbuzAzkkBxAlSYIhOI0FSUKMebpZVgzWzvZO6eb0ZSeq-lL_XbUX8Z6lJ87Intps3QBrKXO-oiE1CCqtuSEsqqv4qh46QAAb_P6zPR4lLowlpyH7-M0sH_VnnaUWlj0GLMHAdcntEn7sgtM_KQ5d0mv-rwyBoT8UVsxy3MZpHxZY_hQxfsSw7FfgpZGd2-C5kJIV1qgqH1819B-Jg0k3TCGzhMrCRZ5DKvo73mK6oq6zZJesZj_ZMvon67RAtVt4vNVsPNm1MH2ax24HNnOUJmV5Lx109quQjq2xQqtczSuPZmFrcs2ThNfx8wcrvj32sDt9D_bYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d23ELGSHE5poXlzOGoo2a0Y5ZOB5BDQCvn6gQofcQspC7ukESn5ChLfRGWuxo6NS7CrWYL6VbVoOWTpS-fjMSmUt9PORPpIe9lmmwoFfaP_mjRHROwdekllZIcjYxMCh2po2A4IAtgdQr-ejJa74cE106yqK2rnfkuYtrSEKcAf37YgoczahFB6eRONKKHQx2h1a8E2Y1nC8TTsC3WZ95M5hz1mo0NyHVodFaidvTW3uDgjmqiz0e2r-HQwCv19lL3jJXWsswcUIxE34KwHuG4d-Bod7NCYx6DxifLD4uCRDItmm4oRhV5kwxDJp5BaftMq4lo0mSSO8Sr-mAyrtHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kFUoQpL-tdGOpvnH7-VrPlKvNnbArTM7Z3mn_krmRuShUatM9qUna-2-s_ABS4dVKLAHze0rrhndwfHsYEdLkBj1FancIduvF2K-0EfWPLxPp3B465abgN9dKjkdx2ZmTlJxpAUhMl6_aeuIzZiALEAPIl1P23Tr6ksJoN6YXb6UwMjhSFCbf25bCOm0Py8wkyAbT3e-yd1u1fCvtANn5WwEVokBU3MiHzVPGYVy8F1weDDMozWgGGux3d3u_paRAH6_ER92BNPzZfV3NqUrQ6buatYz8P5RNw3YIybxQJJCIqqaOw_x5s2kqc-neHn6V1uieEzcTXlexflqhgMHlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8uj2aq_AJkzZC7t_jnHCS1K0MRib9xUhNq6v50Fs1kcUOPunbXSmMKKuHvWtGSEfwhhF8CkYT0BAXYjZxaTbXBvC0rGshM5IJuQLiifclKk2QypdDtH9V56daLdxXUD-K5DSNw_tzvPYFBTxtc7p2Tgt4-bqJURMLDrKNBZ03WGu9654TEMn6eHFYbKZgz9pXCEDjuoFpMcewn0QAznbTZSU4qDshXDdEAMPEdOiHc-L6PIReNYJpwvJziT0Yg6glOXVPQPPYNV4zhDR5cFdqa-18a1V1R06KQME1kePecz1XPRQXnNFHW0olBJMN3yxHTDdoWnKdM9LxSpdH0RvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aecZwDk3pkGqQwV93wLxSf76SRAokBxlJa5XYEgd9qB7_bGQbTbP9lB4O1Z1q3xGrtGrp5-kCvypXQq_5WoABLyKNG1jFT4Ra-KUb0kyT4xPzyFrptw4y-Pu1aae4-f8auRKijECPo9qM2IzSj6fZ3NZ7ns4iDMCKFfwpQ6DCKVayKUWIenCNcvN5Ng4wR-QdCAzX01y_4LjKxE9L-nNXq5Mm6k_PuyOssAYxofj6S4rYxy73DXybAEOtyw3ZgFZ_FSgJ7XG5gui_r7FDY0nJeeve00GGz5SJv87V1lfjtrVsyIPCazfbfQzOQ2X-vFrj4s3cdJGLmvexV93yI3vYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nVnahfvTeG4fQW0kuvsQZCVXFCDwPLkUY-NwbjJ0aG0PD2jx8wT7XujjAsWGoA0uI5qxJvHhAUHcveXfit9aQg8mQkusenhPbUOk4Hp1SFnCHrmrUFPS85nNtYijCn3ug-ANE5BnsM9_aR9BYS0qvnzSY_LCdT0yIhv4NLrnfcjliXiDcXcqfjB88n0ET93tk9gdz_ul4VGT5QpId6JN3N4KKIkFC263grKx3g6T2smlxvQ04Sdlwdd8W2GUV26lXdkqpUUebqleEECcchnNos_9-PSgocRZmRrEyJ_0orP6JX23cGoH_WyLT3fbntXuHx0kh9ZovE4t5Bfbu9JDFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ag0vH0rZJ8sTzkAmnmwDWKrqs3vfQYoCkxfRwHRT0176WLvGp7_VBJD7zuFAYU1JUo6YrAD6-eKueIfzQ_UEKIW3nSzlLUoCRkXaMmSZLUe0axjjmrkRBCgF8hkeMPmlFvJVdg4vkFfqqNo7SLPVvy88CLwkr9bsGUXd-Af4iKKIb5yd7uuYZDGHgmGPRkavSyXEWH5osMfk964SbXMxOTJdQVlJTUJTzHcSWW3cKMSqzxqAfHkE6P3db88CCb-vD2U7oqWoK2J9rYIEeiTF4REw5BlNOq2-FcAoplDfmp3ui9OLumvQKImmcaIZ2-XWBFQHSpaBEXIQR2W-_sOVLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JoZgC7QzV0KPkgBEDZvUI25LJfe_b5gluPHIMPlPqh8pYrQ8EwBISq6JbDE-khgDT95j0UvaFcNEVu2uQ-Lv2o-MOqxfcZ9dAkrt2h6Y-bpY6VELgaEg6X0dkM-4N4bzhiScDMmxmEElJs3mM5S2njp0hSITD1qPts8JpCy9UCpTdH5f12DX30OKOBqS18Bl4FdOWq5YwSiIJizL3hDIvTleVfMcw3qIkqFqNLWJB1QY3M0TSKEVIarf9vKRAPx9dyJzE5g9ZumJlRjSYlnhVvZPY8g0NeXXPd_ru_KwzMiTYMERy6B2DzLmTgOw9N73nFH3rtidWIG3kD7LC8kOew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/im2VymnfNmgZhIMLoAzhi3S2WK1Aclmz8bbuTDIXnlf3VoSTjZ_L0MzmnjcxryMaln7lopG_xiImZ-mkjOsedN0DF3IBux-KEIlLtMh6dTfCQYC0wUE25kwKFWQQChhbFotVonPRSZTY_xfX9ZQ4ZJiY973YplqqGGhu2AjS2sibPUEkj6BQzb68m7pwAeooAt6K0AP54biVllh3AY-1-lurEEd1LgH6G4d2Z7V5p_XZdJjfkZL7JRCIiUagNdlLcNj41L6lgwFsErJGRaMimbJ86iyFho669nY1xdL6xXkvCMjlwveXe49c9enUn4IdKVZSiKY5cLIldj9ZGxfRXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h0oFUkeTxJUauChFz-ockRJG7cQ_eyouZW6wPauTUnUt73ynhjF8inPlCYSPPV7YyyIQuDVtKR9BKSNt2m0sW9AY9ctwshEMBsQktlSruJLazabgmsbXLtzpXQBOon9JDVRWNT9DtrpZNjjW1p-NnCptChZ1_xMC7nptmN6_Yu7_W93xZoHy8f02VAn-VpVuGqXDAAv5L-JBnYRswz_adDusGMjEN6YeOikfeIVgMtfy0WktKdA1wYcQQF_IuvMRnV3vwnIyj0K83ISMtelAs8WKxcc4GfyDqbCRzIduB75p93lXSGBMEnONAVNFbIc_v0_5X1kyxBprufdXg0GHhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UJBbYCBCrhRWiUqbhzUS31pY4jcd-8iWkhvSmDXVU7ST-LilmUbjgcFLmokqeS1kCK66bKGLH_dUkAFacj1KXE-ynlNlOdmS_Hqr5EkZog-XS7Yb5A8ibipLgg2uKnZw_BSRYhGPKi3Kb9CHz3TxGzeqyVrqXhXYLyXfnNrOvzV9RZ2V578iH5bJZMizqVqrQqHOnle52osmWHaRubo8FszDZnverZfzCJW2F23F5vb_FP2OA_pXEV921YoFp6LPx8H3vF2rIp5_VTf27clE9CbMQ1j51scUBRdI3_GwmV-HoNF19jut-5p141oV_cY3gtak1Nkz-tce-uGjbOsbnA.jpg" alt="photo" loading="lazy"/></div>
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
