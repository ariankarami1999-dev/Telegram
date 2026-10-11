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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 62K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BqfDissuIji3166jCG7o1Pb09vIXS-txnoxVbzCKyNsPnY5MewoC5-SRApOEE5V7d1IEG5msAFUUzS2JgB6vwfFoaqcT52bVsbOaIBi8sI4MRAAypI4KPzCUzh-E7CgMhZzZfSwOvu0yGoMQPzQhnj0dt5LPSrasG80GJ0R_62YGy5L8iyMUqznBJXdPehdAVKwvyZKrCs6OvuDyVVOdNQVrMkkFDBSj5FeSInPN0Vvv_RQ7TmJY9mG1tuNpnkgQYm-ofidox-rs4ZDbvcUmgjOWUCOicFCoZnZNYaM_0scessViRUAlpRY3zaKrsgANgVsyFsyC76JqRnCVjM833g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lj4WyeUbpS_5LJc_Q9qZTq4LMaaeHvQ3IKfteyEhgcO9AR6r1aEyNrJaivnFj6KVx8ckSq9kOaai5CWyRkFgdZtvR6ddpK3F4Wro9C7-ERv_2NWIT1CbYMyp5e9mArEtKZQFx5Lj1GHe9y6zOmUdgTIKKZcx0ElpUJhtYQrW02F1-N1PfzDkFzO9CzSN2GozXjqRO7hYIwa7sB_thdD3qZwkpoUECJiXJCRgjC3jhoWkiT19Bnn1HDmitge8KwKkV6XE-0W0M2ReWKUfM9H400C2WXNJQHOlH-kC8pqrzI328Kycc7vkZpQjwY0lMovEa-OXOYpdd8dim8MxvLoyzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bqCdrkrPDI0VJ-rLyhClilgbUCJu_wxnLrwSeK-LwgH3ItTp8D22iO6dEUQ1HZkTocD5fefmNsp3XxsxBrox0XP4WgDw6I7WluFSTw-5kdEWyrkMk79dZufzMAWGVI0N7Se1vYitQXxCunkud0eXwK61sltb5rjAwumDWvEK_sNhmAbiGo1V2_9_Ob-Jqq5LHnrMsqjsWzAJw5dvRoMnV7jfDuWnO-mNPyWGblZF1Gb01na2kqtlsSktKmqvLmwXGUJStevVcqGL02xF12Zvl5_rYKLYssbmjQ3wX0JwhfaFOV9ubZtuFAqgGQ3BVWrNNZIYnHPTwvA5WaGg_kK8PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MG5xn1oQSNT1-uNKCeFoNvabhHvzS6bFr8RHMCQY_MIRNSbHcNuBK7OZdtM8j5oaP3QRAPoin_B4c-sZ1MYUw7VWzuJy6fP-uR_gdoq4p9LTm5fByDqdVdE_jortmJ5jQiGji6vXKKfuzQQxModfcvi4IppDfW9ARpXCLHWeeChbc25VQ-qcExuP3nUgOrox5meUtv_3EQ5WU305-iUGxnvTctNmLVMgNkumglsHR8vjK2M-Adbe7PEuC8qTkN83T2yXtQ_ND_NQr67aGGhkdPHgdX98uVi7-vbbGO-s-Mdyq4HlOhdoLlK-NNy9RIIWNsnFIMyxcDLrHGhYSyzPdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RhcMjRViqh1yMr9vzQavCwiQctjs1LRL99inVsd36VRsY0SletoE4jam3GaGOckToHpJ54GlIqKqpNmc8un53HmdDMLpkmaNJ_MS3s8h7neYtallMYP-LzkSNvZxirvJ5NriDK6CzaZGEu4CUOCA-GessYnCWMNRFC6eTrk5kMDdnpQa_fqwDf9XvGg2jBfqN1MQUefT0KhGZKgKgR3WWu_jTDEhXZVGVHr162_kRmH0GUgsp_lpePmpLGrkAkMgx0rRALy0XbYIsQbanRczGeGV4jTEjZNYn3QGCia8UJfRiQ-2pqGJrYxv-bHyPBqhyzApDOjjB72jAI_zOlwXqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_3oovRu1W2CM9TpNuvQ025oI6daCVUuhw3tRz86CNEKm2HHKkv79jF-0dAO691rFYBtASBGVy6vlfLEwTc-I-3akyAR2A-fT4Tus3s700Xiw6x--qscrriJhF53xle1Ko7Id8mvdmZ1A1MLzg-rhBMCHTqBtzDkDi67owOs5W-OzrAJP8JWmznKn5TXcIqTnZ5JUv6Fb2CVVCqozbLwH_5mumncVbdkEO3T9plgUoUnEUMujEphydw_c4FV2RqCBYoZuVfklAStMyz6AEDcF6mpCD-fXZ17isSKGZoZutruIEtAZprvWOQSfdF4CGdpAblGlS2Rp0Y27PwNsAuyjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7VtzSgTMOcZ--0rVfGtqXeLHPr_sgWyPufNI6B47Plr9Laa-Q-B16DGBMN1gkchLWE7dFPgVgabN3J4Lf3ic4ap9StZA3XZ0ueNQ2KPZSPRX5tum52tAZPV8FFiAafMhBQRI9B8Q9HS51Vta0yCGBrJNMb90wCWS8B5YJGJy0uWe4iFpRiD8pU20-XqT18xRJ2FWPnAzy3KA9n3-F_GbhdUsOhQ-O4ExMvB78e9PR13-3ux6WXlYQ6msDcfrWvERdZFvYlEgQ73oI_2S6dPuvT3Wn3cKwEJVV1CG-2mxB06AguLghEuxOIgWMfebcR1jhAizIbCY25XIEGSeMmr8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kTh7zTfP5lY3QFmT5-azl7tg4BM-P88WE10A7M65sb7NShhSqlTTNhIPj72nFoB8tkmFGHnSSFMkc8aCSwzWbxd2IiyQF_Nc1u6VacbcuYJlXRTvzT5ZpVfo8xeANuLMs55W6DXNNXQt9HfXINqltqPtGM9HTg7KunI3GqCXLGXXjNJecJifvu2snQPEx1i-kcMaWrReyxil2gaV9CgDXQaFqMLI4mdFwxEc4RtwRRSFIXiZ4dGJMWCpFnkNsvHc8UBxsJ02n1F1hWVYSKXBZeqD7muqzg2gPyFaXgVHDQE3-L_WJAO8Jj7yZ5kNAITntSxZOthdMXokZvwN6xq1EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dWPYmbJP1csbsJdU1ki7a6VhaI9el-Jwt35w1eP_c48bg3p_8Zh3Mwio_IXq3t1RMRo4T8g1mCLIt2v0lPTAA_ljWpMtIos0ig-TOxBiLWWFHRt9cZoZ1OLGWX6fajmXf6Ou9bsq-_BvEgiFS_n2_ZKjPU9qBJwhJlK0usdze3u9yG9B39iFnXjoqLZa3DnRjvpL5BVzg1I2SkdPciBzSIUDrn58zPrpw0YV1WRMeBuCtBGMO-Ujx5vvuGgQ_egkJVrWM7sHQ5lfkll2-iZuqFdIaVDYa_6TlAoz5JLZIbsQBVo90pfNizbrE2RCOqyOTEJs1_DQpFivojLtn3_CGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LuyBDom3SIYH0rQwVQ72vQW5A0ut1Xlz1owQqa6kLAaBV-5pyeqCC72Iza7Fzbmb3tO27Bp8n7aVsS-6W_NkaPdT12bL7XWpQoemWcn51jmwzshI2hGpPmyj8IcGNTSCbR8f-wOSxdIXtmz0TrDxy_4Dno8ukFVOFw5M3YewBqpI7hn9tVUWv4xaXT9-PMVq0a7424zJ12S9bWVtNdgYoYkAzUkiBvj_iWkOBt8OUCmLM6QyKfc1u-0mp6h4R-jqVBQveVW_NsEtqjNXZOt7WLLUFuLzZLvtd7K7-rlRqbAy0l9wIaxg5pCrXrVnrsV20Jbgs_fPbhC_tMxM4yKS2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KXVrugDJCQf8M9pJ_8POTnlWEEjQXvENic9AzKV42wmJR2FzYMOY33_fsYT4db8IXPJNCQYM4tUPYjN-dDBtDDf2-1uDgYmSDifWAD_9_P46Mn_39fBfZ5w7oHmBTp3-DNwM6VO8ehgH6ajysIQ1a3PTmheyxNK37iqhTwvqkVXZ9HRL8xaCgkzwtEFG11mlyUhtQQcSjbUtEl1PhsU-YXOCThlFMKLuFWifM7kMUUbL3Z59AD98uDpO0kVITIcgYy9POdze1I2UuwBlkKNCxSa24G3E6-YRreeVgbsJyvC7VEHPf16X1oNi6F0UrzidgHEWOIMC56E5xOCbEh1DIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lrIO1uRjgTY9ZrznfRFFEUWcxdNOIsZz0YooZdFX0h01UMI0V2IbFPSTIqUvvxPdOQDhoyyIjLazfHx0IjTzZ-0n7fZXCZRL1TSyLYQ63eATHoSpxVcRb2Yt8DkGgyxIgbSf6t_iyq0RDt6rko5FQScmjFG2yaH8zx21T9iR30hH8AZQOjSsH0BA9t9_j8L2Icy2wemfaxWhRh_kzpPQyssDL0oAi67W1Q0ZTeU7Ky5YiQB0lHMd9L3nhQNVs5EBtYw5yK1XZ6iiWd4eaFE3fBcuQFMLBj8xPN86DtT44czrlfjzUjGKa6iB_YLJZ01t08odJ7gu4_yjTwrJWIciDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTDP_roFDj2SZETBXz6JRghW06DJCmrV-wQMrBfx-Hm9wO2rruD_8dEs7GRWQeyohag9kclOgYeN4-Py9OL3v2LhKpQIfRqdJ9CWWP2Al6te711b4E_1gII9bLyTXJONA7s9g_U_q4iZd4Sv3XaLWaq4EBidGJlCZ-Jr57FaNrOgAPkUWFecKpyDsayAk9crBBdlYE-iuWS196bM3MpYc_dZkSEPN_XSZOsKkszBmg6ROd3kqqb8QAhVbkXHakIj2MhRkRfGgGugZfSC4nklnOkllna9aPyNvAoNtrSQhCoTUn31fEqG69bLzb001mwE2Hrqj-erzxvfDpfmov2EoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KY9PVgXCjru6lKiGlZOdEBYgol7H-idiqI5GQ5mth6NT99u9vcul_vSBYP8B5oor3b-5wkaKbeAt_XRykqDWBRcdW0ZzAYAGPq9n1cnlNCUT7Bt6EOG0DMGAGB8SV_RfgT0_VWm943lgcnUJfQYMgdn1APY2jnA7n3GgnxvEdvzQI-6p1UG7B5bIiuvc-Cl15DZe6fsZSCJZU8BDipuycH-hkjPy2L6LSdR-MULaHhuPewfBdF2px6PxLAjxFZlCDUADV2EADGiPCBqgUiasYIzRFEi7aLBkNTVzSnFRFm4ig36sYczBBYHNJaeShOHh7-m4azCW6aQsr9ze4VMBDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pTRRA16VsN7WMk7Mp7HowD8nZwlSaXl2CsuCGtR2TorM4fq7ULTK__Vp8kBM8EqeX7WcpPJMHA9LVyzrfq11ssgSHAzaKLSQfVLpUgu2OxDQ65rBw7f7YcvLiVAJsWvNv9b6nat4T78_4Hc525ElN2eKWg3qa0ouzSKeU8wCQnO-u0JAQ6Z0GKHuYqz8Q4Xm2x1UC_T7TiUQ7K2BeV4WbtNhkJycxFX5N3ElY1xRt-LNid-dsbkvFexGikmozDM3kgbs55-wcDpraQKsewTnJ94od63otUATrD9XzyRDgdyE_lhKFa_SLvbx5Y7WWXeTATcdqz286_G8TjCqMo8gKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UbHVhw2MpdfNcZm0RDHWMSjXrQfIg37EjmmGXWQSf2U70lS_7dpBDsufToLUO35QhqPiTNb0ALD_AWXHa5e0c28OrS5RwMI_92wA4fATORqPXgAKAu1nCPfbc7jMOmqn2y8pA3PSSjfGkdvJwFXLmoNvkyweduzlfL4xJmoRzdOVU60EyLMov8-yvk5nrCSJjdJTiXQvi9JX_egnXOCG9AfvypjncRzV_WWDJhtJUqzRHq-OU-BxRWj1QCBxVL7OAC4JrKI6407GDU_3U6sYcmi7iPpLm9RK3KhRzXT7BgPvK6N57n2q41JEsZpDnIq_oTst3s84OrZxkuO6stiw-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZ2mUddRNelMWt5aCwlD3HT964_l6TQnvt89Wm6NT9bfH_4URF8zh_4FJ8Di6IocvIHvlALYK5KfY85a9NFA1iMzrm9BpmsgSuCed0YtThwzDHqh8cV7Z92Bl93aPtxRx-gKG_qQYu3N-FSWXrDHK0q2JzhA36l9noOJwZiRZNpKfBU_sq8-fYiLLupc8nWR72onYpHsYj_cU2v2YMP1PIq6KDVVMb6SAtqa-OfTImoW6HoibRRyNQCMDc0NyEeuYRVG49YZmoi0t2Ti8Xp3J0pusBefNMPPk61CiEQ0NnAxIfsp3o_kBNzH2k-WseFbKrwDMQO0UuIWwZS8499Nag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1Gm_rpTBcHKcNmln8nYRbziZJCWGBy86pIYevrsAdF3LqU3Bi7EdpeaAqqddJ7LvxNySfvejJagbxxJL-L_rZTWddbgYAsDKSiflccVTSzo18Mh-J4SEG8AuUJ4bIna53i2yXSVTwlYgraoO8PAcYiMJy_UJ8woOcUC5YPXEv_gpzjlvyg6QeUz10JXXBqGSa-cGeVdC-FGxO42Ip0rPdMAs-jnoMpZw83o7KPvA2SNeWCM2YQ4eNcpiiUvfZgI-UxLc3rjqLm9RDIb8HB66O-DpcwJDmK1kQkdNOcxgHpRWjnC20_f0r2-lGmqoMDJJ3xxIdb2yxSHeg9aA6nF-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkhFUHPj2EEsRx-WSRr6MQdd0a0ubaJjSUfMcgOm6JpC_fRBldUuqmAC_1yWFjXA2qPu2WMVSxVZa7irkfHdY8GIO5buWYdGCAJOc6lx2Qnilr3bFufmVFDA0HONrgOe4NGjmh0aWPHXWbBbdUru0eIRFHgAo--43WoffD9N_8npigqR8sfX_dLpa8tulVfUQfw1luM-bdi6XPW9biYT8sggG3hb3A20sdIBtlUjlr6uCmgl0tcQjY2jVFF4SVdeSZYCToZsI0CB_fi-rPCUSEoX02PHE_lrM2eKTYD3pdHgeVJRUa3loK3HnNgyPQnsN5H6-KxcrC0NNg6AY5P6gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 90K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N-8uzlWJ22-oRiWjbqR7V0w0p_qPtYTEIy8B9uT8d5PO_jm99OkNjPchYI3azLM_mGI685b8MlADEeVe6wsgx7cmyZWBa6rR4hz5sWHtSNScDyKNHfFnRte6lQRmK-OQS0RlaQZzd1QRGHFV8S0NB-lct426HaaGqZH87L24aJcP4Lg7LwRModUBgOvT_GwQmaDOhPxBMFmWeXGYwcqIkm6nwQW7dI6FT-BjHL-szpQepbh03YmTB7eP-P0n43F7wnhG3T5wtZ18AoreHtmUFXLTa40gqg4wu4eO54dNCAg6tLVS0s4R27KLPiviNanPhSJ_sebBMU0Bz7G2nGNm9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cI4nPUqO3F8fzdBbhtvztj8Zmz9KoqBkkXho-BkCR-a_OOOphgM9zXDn5IG6NvN6FRBxv5wnLz7Q52PzLQ2n89-NkrpCgDqjEnAYLY2Q1HKQwnfE5qOciQB1RBZC61vP2rqMfUQJtdMD7oZejHIn1PXkXx2US3zjyTPfYoORsnaPm1OFM-0v1s2VBQqzgoMnWpvgy2J739dvSt6zuftQyCGllGX5OfwNMkvw-7upP6IVOy-CiWNG0RhQ4Pl3Zzi_ueXk1Z6aM8CzO6TxwUfMVaF4g8FHDzTVWKGrtwzRFkTiNgwSAmpH4a7IcoeGyyWvGTQlhdoQRGHXtvEK-WTaRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uiQ5ye5aP03f4qWL7-g8c-ApOTju67xl3W4-6SEk-djaZcxrET-lyBgz4hxsiw5Vl4uGrN0j9395LXwD9SWbI5jMLeFRwUt4M7xs6hd6TuWHWSOj1TGs0bip5pBkYBkbrskee2imwSUt82PqTcubxPrGk5HMsrtXUtpmU1ox6UrtZLXqahzNl_WJbsuJwX1UvuvppssAHMYzHfolhK0OJT_6PlLD8N1gPZztEyH9NKOW8F9mQxj5oj5E5y6XwVV-_QtrkJ4sstpvrb5Hpiwawb8ZWe30YCQ_gS-HZC1m3OVHkB4v1O3mcN9e1fp50zFugfO4iqAW1hwet6q-gCdAcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TO_7EZZRlLbAx17bYDyrn7zIu0FMEPZK8Sgg9n-fbeHJG4JG61jsbTDarAaMWa1h3HUrLPV3VPb62UAZyv8NNyWC8AelfA6wMJWgCrWkGYWdoYmZLMvLr37_c3OBfnEvr6BG9fjnglF4bYWMrSV-PW8rRd_EUI5YnEF3FADwBiOAQHQHKL7oMqSlRh6JOa1jpBKwwDcM6mPEcVk5Ow1tDr4V62RJ1ydmAqgeNauCoGWCqOLEebg4O4MPlt7zBKWSby_Vm9Tan9babZhmbEaOF2BMJJMT-qQyAVXFkv4OYX3HcY1ihZ7P1St85PtjNSQJohK1WboHd7MZ15izn9Wi1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rIEJvZP9qYrruM62oNQI3oniP1Ju94zY_GeUd1Ck2DylKlno2otaMb5dBzLyz-asQ_Itd60-zTgsVNFynnOErfysQoHs-jr1VhoFvEUeBciv6jLEUhsFYbHmL5Wye-MZk9WaoLB-7w_arCQdT90ZxNrQOgzxslavqa3BA6kEk9xqwvGb3FW4RZW1dBgouYHTosiJtBShtt1b6ZxDgieqp4Ep19mlK9XHMqjA2-Gkaqfk0bfVya0qzQKhMXN9gHHW6dduwnE7k1dZW-Jxs4mjT7o4ZxcGfJ1FSNm6aqAYVzzALr5EFez5wInnZ12FCXxrQt80oElyAZnbBSPtqConTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AIxBr5NNiu2Vu49gTjaPBJODatOb5l2TUKkq8IgPtq8NZKqngfRMnP0z4n1BWKMrQJwBKFkwRfnIMa1Rk3KCtgIoH8IZYWrn5yU6fB66u7LCW2HtReew9psqkTC-UCuaYrQ-UqKh3vFLgRzQrcj0XSirteIBCCAl_LaeYWx5-xRy_G4wYW9SVlsjoezvqLOmShTEqWtFB1k0nSNz0Hft2dkil5HcVs364udKfMfJZlHMev5p7yCNrfkZzTYXKhbflMsuzGZBizXtYGtoUqgDnGEBWiMd3Qw6EmFvOicUhaC2J4sMl9M3eoQG-JT0qxTSLgsf9HOuEgodtmMqRV0DXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3OIuM7o1J300R82hePwsValOQXcMMkvkBZMuJT_rK-_uTgoTE7BYB3YxnvtwhfOenY5II82DxepslcL_h9utFd9KFASc-MLT7dupjgAy6kCht8uf2-JHb99NZfxblrfklVYXHaznpIbu50NI5g0NTs6BfRON6rWc_v1VsyviTOaDPXru6SHZFex9vLmbEUMxmP0jbROGdyel6gIbTqejOdXSMV8old4g5J0UxZLhuULRo6pR6KduAuNzc4ufVqTr8iGyNFVqAbYTRlbSwfMPqZe_ya9jFDlPAMfLtWgoBz2idy0VGbyvK7tOyDBbZEwttj5-deQDPeX-C1jyL7WpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YT0x_VR9qsyA6qNKKXQVV5B7x8R0Z9SBADJP0nplO91x0g17utZQFL_XXvjOJ3OkIwNvI4WEQU565ydRN9VfvbITDObzt013QRY27RuLbSzUnXmawkFBj-twV0JVEi_2A7enIMgKUMFEtnnME1DnZnL7-FAqhJ582P4IVm5Muv8tWn6_UjyARViuo0nGMBERh7e-oTyuYF0637vVqLr36MzKkIvuPTidMKoKef3VtwlwD9dQHMd6M4PQ-iNGU30V7cHOCEmY4cNynuTCUwh6EpDGsM3azxU5TGIz5qG02E6SF5ig74FwRkX_Q2p8D85T8DcJH3dlpjon_Ii5J86V2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qyWpOO5p7LOzFUmXgOwrPifxSX8-HEGaVlRyhGjW8B0COGxO-_6pgmrL9FL3FZfH4sliNSXIlblAnagPZK9btLfKTabpdg1gedUhOb7Oh5UlBXrdauAiMadOiugLkGLCkg6JZdCzfJH98h8kLQOy-dSZ3vXQPS9N5nNqoodlLtBXIWnuIdPr634tF62JkglcSvSNthH5ktETrlvSbqCNEg0UPave4NFVizlDO_945nZ4CS4_Ti8VG0YlsX0L40GygdTyFNGR3731sLcCE-cCDN7oKm4dzKAKUloXKcbeUnggTigBwDu9CrF2RbCv7OoBPw_hKIMq8XuM8K2lwi9Gjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TmV6jhEP03iJssccTDGmoqeNY3EFZySIUSXsFdcrQ5C2DRfvVXFNV_N1SIO5s9dTtKPZTcNye8aK3GV86LFWBUtoxegNuM2GC9gsJNVIo5LmUanzda15xp7sN8Mb5Ip5CpL3LkJNhrlwa49VhRKBK0ou_P8Ej_x8fo2NaF2J-JJw6Ks8ApUlWAQybKpNDetv8Cb9OOzmumhkZWHxbZ0jxfJr-S_jJTcjuNHHzPRpF13ei53LOPy0erAa3iyhF7F31TwsyZT6z5zy0e7AgezBOB_H4uz1TST2YAyDiQU4z-FN9qwmowvy3beFumuIVA3gB9RTxnWlsms2Z0zGDkodRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQd2jgtui9jDiKdQKO7RKv-HnatcQEixQlcwHKV84bViWvfacP1mEw1F1CzRL6rTLRb5E7d0BERXik-xEVNSDC9BzueCZey4etq80jmUMZF_vn0rBwnRCxl0Gl48VBeYe8b_NIF4pAVr2auauvFfJ_7SymLhY0sF8VafDsSIrbEELEi-2_db8SsOzPXMlhaZ09ej2tfOqRe98_lT1H_krJrNUbAG832ppcKZwRZwz3g3IMw84D0p8UMQSi8pBQAUmV4ZVOmZXNDVNyYW59jjlOXjeULsaqEOBavZU0AkvYVZpOmNRqkwskx1Fou3R5WlKtCvWHmxfgXKErxoDfZmdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKoM0KSko9P7TRuFuGvXvRfGIj5KWtuBP0x8YzSkejlhsyx_TSP3C5nyClPtgWxppECDSyhvqlm1ofREjY36l2z7q4NBY-YZMIOtUYlNrBzWHMzdcmE5vz0kXlKVv6yqxsHH14WEajJiPLSLXU1_Nuu1p_us9nb-Ve1QEuaShFAJOly8brUQz_1Ic4ttoJR4yJHbJLaJvMgmDnyxKDCAJQLb25NticbGW4RdKInoZula6yzWidwCNDRLyosQLlXsJnm5nsD6Cak9PamstqC2NclLW0AVfeDcI2pB5T3-vledQJIU-tsOzN4SMRf4Nz7MTFom2Yy4J2tztoNizaYf_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fn85KZBACye0eKq9TYj9Ni2uI6aHNvzU7PXdNvXXpFEjWxgS7sT8EQ-LIhGDXRtPpi7HwJWl71zHBZXmmDvN7IbbjRfm8wTRqTlt_uZh_DbcrogcVDy1MtbK9xyNv22BTIrgECriFdToNZA0M7mNk-UVt-L0_2Bq9S5H97q0nrArWUfLI5ePNv9RK1Kya_wt0X4yEwMfWBrPzlZvFVT8QayCF9UWhvRKElecY8cY4EUgNNM8fcNDFG-8H0PMtGsDM57iik5wmSxSs7Dm9SJk3SHtFPYhSlMGyfHBOj0aUcisFYzAoFnm92aG2V7gjRLOPUmihScfB6OFixl5vh-6JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/keikvgCNWIsnE4gnursaHEmUrvNANgjoG483GqhbyE_itNaiLZS2U5sRLKQJkH8h_GxgvbBqDKBdVPnO4ETg9vuAGifMFKDYIfW2ZHDiYsEA-oK-LaYohl2gSmCgatF-_u1Vl4niHMM1kRFNWrxI7k1hfALzBEnZ5hNtaD9UsiZe6P-GQDVdantWqEOkmCIA4TEBen-Lh-2HsZQEqk-6CIhyU_tU2iz0TP9taadnuCskWp1sch0nLeGASspo-L4S-HtfTQqDKWUnFvv2CMZZtIk4GokpxzKhj6353Wl9cWah7lDfg7MGJ1HkDiPAIkudWPbKDnRj1qSvHlmo7rIxxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPzkWRf28cXRdtZBz6k-CRzSF7fzafd53rgmu3OMRyJuf0-mbQSadHF_Ij5zYcykRs6t-5fb8aOuw42l3pYFz3MomVNjtiEusEI_u8YUf5GwoxWbG62_tgA0iryNCzRQYq9HR8BYa-2DSwmyIEYyuPv-bN9qvkwYrk1s1d2xsyZX1pL5AnFLVX-TdjP8-F7A6VX1oUNFVrUTv3nDKKv2iitjY7bqS8_xHbsDf6rsGyL3OxXaIThRJMavjmFJLi9-LVXCdYvQyIYwoMEHZwsUI9wzeiLTRzYqydjR0MBsR8eY7g8IR1uYjvyuxKamaeepgSap_x9wmOTfuvkSyUmy2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Owuqk1B6T4PUYgtUDSg2ngoflLhpkeokqOK5S22LCyKmRLAflsckJnZpOUEJE2fzFKSjTwFGAkZ2QzGyZx-i_JuJPPh-IEXUW5XmebkbgJFS6B6Hya2Hi-RK7PKIf8-6nZhxz4CUGUPK15eor9FtKMFTO9NZCa-k9C6kbN6qHzVPkGw3gthQNMYs6W4YywDnH9exc-zcR3cAYy_IKF0KrGJN9hPi4kP5Ewuy-uL8atlg6eXqE_vdEx3N6I7Ruv2kHDowpP4yHxIeaDsCTgUeORcgqijTGoVg714vAfXnUeeMbBXygMcMgFLUeSDf4euntb17o8tabsDePqu5zXF-Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8Cii7PsuweANlm96gt0nyW3DM6El_ooYaAWrd3qdX3AYFu5xNhpA6kF1FxgQAqflwYQUiaMcFc7ZmgIhr9tr7AZvTRF1hPK3dczrnqz5Tt-UE-a27fWQkX-8x0aV9IVkJZHsue58cpCkiBfWuiH21Dfi1PxC3o8DGCBKBupubru3fTQv44zMOqOjZZWDrWrWMV2erMj__Y7TTTrZt1xyRgISUxDVYO3jgjMNT8z_TpDcTg8kgEMuOFAFApiSrwLtsCL776E8hu7DuK7BBrgWum0Z62LLDa5MaAl9pNsAgbUkhwoU96zkaA2oPF3rm862g__9Oxw11whyR02QEIcjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQMCPbIwVicBAShHA8lzI0eXaNM_NyxWrQOTdsV3pHDM2PXAojwVLGyu0ET-YLqEhPq6H8bX35utBE5Wac3vNjoFglEXVQezQgtvtwd3Lv6W9oBa0HWV5cJxg4TPzGrdABZa_9RmEPZcXNZXVoMEmNQXCqvWcpHmBoC3vZAJ-ObrjAKK3r5brZTnVZqx5kZxS9oXovFtOefYOmnWe7b9wTDn6kSveVKAYCbzskPANH2hD_kaaRPgVvc7e_f7syUUcteyz5HmqyLTgpwofopwXVZYFVw2goivEUUfusgM6Qf0NTGLhb87RWIzKsDMDU1wMQ5NE3d-G54IwYYLTp9tpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WwSPjWb_iRzyL5oZqjM_80aN5M28Fgksn5w1zTz0d1QUOrG4c8kLLqIHpMP8DiOUWMPKOTc1qEuoqtyebHUbHlK1GgV2c-7GpwiyrdTC0qobaQXiHhq-bXYlJnLDQNQzJhaOTexDwoH5FgrVDYJZMJMtHWytLxjsujZeUHm-pCXUBxlJpfMLDncVyO4KhiRpdfP5W3vVTc6aopV-TOoOW7CwYoSFLIBr3tc8OVEnpfYxKgeJybWBj1PWjwYzU17gE_qR-6U3YbLO8RRMDP1rTcqPNKT4xKmKkgbsObmmETzAKPvT4DSWTREraKEfr1ML7oo6EEFe7SF9pzM8TrUi0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sWZ7jR_mnqQa8JJtAcj_ut0hly8PfmGT0pLzgruQC7DOR_zCQOkEEoC_o2yX-OK2GcywEDPMjkF54r2YDJeKEvaoYxhGbmDlDtJZO8-qMeTLENQh9lbD38Va0aVerZpl12Cm1Urv4cVuHL0FVVT3LdPKwS66jsmSsb_EQ-219L15IxJBemR1lb5cn08WL6ZCmFXALFnYx_zMvcwLbLEnOgK0M8axo6kHuXo-hbMsQK3hxaa1Ye08CQFWCI_K2omG_wphFcJhCChErbBQxb7WH9KijXq8sq0Zkv0LikAd8C-tiFCkQBm3MYPWwzZ76HTD1EVJRC3fgQM0odoB77fH5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FqfajAZU-wVsYXqqH1n0tddN97q0DtH8LFXrhoYJeEcpCb8GkplD5dam9k3X8FuITz7HRPaXmHMirosrekAQG44dTccYVK-sIVWE0BVBfE_etiSlyrFn3IeV6B_btX0FCC_ZXKDqRgxt9KadR2XYzB0Nvht5-Tu8lP4sr71PkRVVR0ieT8V3KQrIYbS9wJJvAr_lFw1TKl2b3NmInxiOG1deX-XOldblWutuOTqgyyNUn49jHvwLA8FWfnWgVzaDIVUMKpJJUFusBr1uqgUwMzQ7_tHha8CuhSqXmWI4ENM-BAyXLYUnKfuW-tGyd9_bksCFWCNJUaUWFRJEsFbTCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DczuU7et-wBXV351rVEKl4MK3EkQQv6TCBlt0Alm3DcQwZbxoMuszX7wHhd68o9k-bdwqx7gbCYkeK-LD_ZQ5P_LpIVrKR9B0Zrzs108_rHHEUwpHPf5znGX9qp2Dfh6Hsv8ZP3tFilQseTMTIJhTuUEmy6tSf1b31cTgWkkVLkjcvOY0RYVgNC0oNszn-j0L4zMdB3aDiIrK3-BvyWObeAyrHjjkfo8DULwjEj8hOnWDWg8Akq79yZ5oFI9b_2JbWBXCkw7mCQlrQ13o2ZwXcF3iBQ3BRpDAkrrMZwzGUlymGrqIpNzSHPdYAjTqksdaNHbGFxLe3rIsGnkQJ1QBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AfrVhCQ0dFdbz2EnBXXNarb-JKF1AWHJ6uLTDQzy1frSTW1_QsBHkCT6LvuFPOiACPTDNyZA4Iknl_as_7vDa4zTZKZlX5CnpBYDWVEL1xNSwj2SyW4iy3JgxBGTS_Ih6iyn4vX8FyLD9lWHGSs8GGHr51WonHucBHL1npiSb5PJTAvXGcW95qWMz1WxnbO9EPc2wUGBMA_ZtnamuUkZUxk8JlQgOc1eedi6o6EvbWATK4kAvvKT8omht7CzhOiYtpSBobKCKH1YKoIXMMTlUmaoTA9rEXvJNvSFhHLCtFScFHdIdipeqf_xuUcmWkPtLN1afMugqRkxRkUE93o6fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T9-o6_yBgqcLd9ZIMArR7A6CBN3n1hJ9riTTTdGHxvqNOJzdIG1jhoRbDfEqUr-d1BvacRbkK5aouuDpxZRkmXvaJ_Z64N4NqzFxqeFw75HH9_Qv5ebj9sJsE32Z0wZGWVyLSq5r4TA50JjM6a6rZkzyN0vFI3Z6NPquKfgwx4DuLqiemzLJOMjfZM8qvV69m7Xy5GqzVuF2G1ahSKiuECqDt248r4fG-HwQWKlbhCEt-DrusZTwVEXC12LY7Ab-Y66ASmz-ZjUiLWMourYs4UCVsqsFslUW-HLvQAI9torp3gegfeWq9qAMbMKXXXxR1wlB5X4vveRBSdRR_gYOXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0swyZqsjEAlgVVJ7p4aC2RLJ3D1jxjOdGoyFLIvU4no4p9gScb4f72VZw-l0dawD3lVwwj-8jsstD-T-8FroLoq9th_ttyNagH83vz6Uxnd_OWcO-CJD_k2jcXgeSi8HT9TTN8d7UJmfGGIy7DaRdksrAcyNNyOFYDuFh4UbcQjo_4xfHvow2R7K0MSykyIN4TMo-1miPBqIdGFB_S6fgBy9b0QPzxN8GhajkTku4lhf3oz8bAyycEYSQ_yE2YNAqsG25n2QK9729zqL1_kXaMx5fRRc2quWMwx5zx-tAaGESW6yRcGBMNtt1bZ5hRdWskzP3OcEGElqbjPa3bgrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZrIMRvmauY5-WM5tfoIFp5boFPcqwC0H0ynlZOZuMhNa6FQsWIKFWb89fFHyN9XsIMzJ9vYJUb29lZxVOFwFgcJsj58tSMzzCA4h7wOpvFurS9y_PCpT5IrEvITiESirQbjs_E6pZiUETNH8nE0deV8Hs_RpjRDngU76tVgjZpsnkdFZ2ihJnGiqkrhn4Lq4UfJDhXFh_kiOj68MhypCthMeHTkvMz2fu2P8IKQUinMgNw6gCKzCCe-Ies-Ei7QwYFrdvCoBpZAU1Ad0kKlTTQ3gxHWfF3WpD1_jpJgEVJAbEhPXe2OYxbErDiDIUV2cXtITB2ol2yzNru3Vy1ue2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cxYqvmDmX03BSGFTO8GIWq_ISLnGqMy7gK2ylf2WVCI1qPk8IBX5v2JMrsN6cuLtlklsBULJtsOj8pBTQL3rX_bG10CN9e4aElB-Mit_7yqO-WzIdVWY3U8zFh6r5alMoX81MSoOdXDM0-op344t5ECytCa84WuEo5tAJZxD4K_PBb6ICPpKSmDJuJG6tFtGJ75pfMQDWvygxm26_CRlL1Cu1DXJ4tBQRVopulq2-eU-cGR5hROaV3YIGWbF2X2SMU7JcFw0ybIyDUfGEIUBvzMftEURsLNxg6Nl0NLdBcLA2cP7jeLM1AV_INNIhfDA2bXfJdol9IdCTwQmcpY0Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C7919mIJ4W1KbL6u32SR8PUcRs3xCz7ocYTXjs4RAUaVXfyzUwRnWUhdniQ15rE_JHnwqLWH4MU5lAIY2EPT-kcFgE8ynHT94TVtSAT8846vCJ6k5snbKA0w4U7Vwij9uUNKMdCBtHwDW1GSCTvGvBnQ4QbZuVgML0A257yC_gsXby9AbjO11uY7eGYYO4Nd5KD1n-7I-a6E_N1brI14LsB6odXxvwIS4AOXxlQmEPvRLfCLLzuTutUlfrx35NCXVDfT7dJMf-ZmQX7nuiNvniock7qfSa9UaFtTt8bT1Rho2EQ3X39PE_SpC24RhVtEMonDyT1ndTaF3tLsHd3O_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uab4AYvJ24WHmk9JdnppRqVgnrJqdUAmEr6LKkkoF5NUtMxJGqzkO4mBE88AHvhTCSqBVDnvxo3GU-aopd9ijjMKOtjWKloOxb8yuxYsxHLyTGWOFDlQy_H2a30pzwwVJ9-_7YpZsYoPm80Aa21ZK6DUYF83qNO5RW-z5qrJgkcrmo015462vu6bv4Fvz2velAtlqXbhVQwCCJ5MfD7lT_mDV_6fU3eDA8YY2A0ptAFdq5ficDWI7x1yD8fc7eFub4_jihGTeQ9U3pQ86v1B37u_Mr4kNf2uNBBJsOz_a9Ro3IAjFXVbig1OjsZDO6EQjfics-qXqD3ImPrLFTZ3sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/smzteVlptho--zs_WHfDtptRR1Nqd8d0IBB2oYA5bl60g_lFawxNJ5KwHj6Pg9R6uTVFHGcVh8t03Mm9Wf9FpRNTn_y3rgUHkS_AOLlImDAr3qjFtnDRwyyHmOIkLtYqMAKLEEoGCkPAwPPlGl_r2XSCBk35YmulgMRiBK2hGSlB83u1jq6IuA9ldBtcJ4oBHyAIbgu9Jyfoq8kbtqYsfj-vOmbx-zQs5Im2dC3K13ZZtv7Y8SmJwWp3_cYF931B3iRUafgVbfwTxN6eQH9z1M9E4DqfHxNOEjokUck0j6faSNOXmGiizZsk-SVzuU3oHaJWSZ5zA7AYXbsZCfpPVQ.jpg" alt="photo" loading="lazy"/></div>
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
