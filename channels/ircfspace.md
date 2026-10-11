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
<img src="https://cdn1.telesco.pe/file/Cc9yR4o4Y3p1KHmSb6wEEWWwCNxrHzJRxVH-J2bc5-z6LWo3BHYWotUabgovLZyxZBRysM6BetHu06bJS3OCHcJHlouyf7kNfl2wsxqvKat0OnRaaLdrqHP-Jadd6fC7RN5gfLJArpUzkKHuW6mO-L0KNAysvNTRpFXpWnmHN_LNYUr7tpmvh6swyT17JgpFusfVlnnCcpZ4KrsTciySW9RgbbHqmRLykWK8xlXUmpU0Lo6fPQgBIL2NLv_h6K_Li8QDkhHEM2LUS849RBsGfCOl5mcL9CEfhCa8Fspy0iWg_KtN5_bbJ7wW0ljtexG4LW8_lv3U3uoQ0FoJsZLd8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 03:30:25</div>
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
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/ircfspace/2665" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/ircfspace/2664" target="_blank">📅 22:14 · 18 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/ircfspace/2663" target="_blank">📅 22:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2662">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pEF0JpuwqvFPEDbkvpP2AbIC2iQKxNdh28hxFcRgWyw_4byo9zIOeJBw21OG-DmsSbTFd_PdKR3ixlIyh9XkgG9ByEGw-KQIMbuYXOe3cQG1Vuc6Ic4RtZ1AqZdJ0KW1rI4Epgv8XEzdyvE-O7MO_ZpEpT6LqF871Xc65ra8mZ0-OORF2s5wE88t-rYkwS0xASOjhsFVg95P1QJtd9vysY3UljfXfGVLjfoSivlhx7LLbUuNgCAP4NG-ulhWeywYRPvr-Zbh1fA3ssjyqSckDPMKdlngxnkFBJ3ZSSe1D5nwLYPh_kSKrnHVc4zHIckO5o-o2oXjiugVLf912wuLqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/ircfspace/2662" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFE12FgQlv8qEAitp7F7GX2oAPQe1wjoLM2_l3C4HYrzRK_kAj7Q0vxsT3NP5NRUvDJECqQzADVIuCDhueRRes5eYXDLuRnwz9XMEfgOdrfgKyecY1R8Sto9WQ5cusW21IzwrRDjzr5yb0XL5PKAVI3FwQZkPBfdwschYVQA8nrwXDc1NiCptGgZT9B2C-7_iNRT2OKtLcQlsEvAtZkiiCELZcME8QSy0QWI4HSWlVjyw3cpXYSnWfzevOECiJ-wD0F2NwbzsfSzaC3JiR0C72E4L1QD9LvQBJDsvxAgknoerXSJvAWbrU0uMhkwFKAfAiQdh3FcjRyKPHMFsv-7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌کوچه در مورد Jet VPN که بیش از یک میلیون بار از گوگل‌پلی دانلود شده، گفته معماری این فیلترشکن دارای آسیب‌پذیری‌های امنیتی، با شدت بالاست!
این گروه قبلا در مورد خطرات استفاده از JumpJump هم به دفعات هشدار داده بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2660" target="_blank">📅 15:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dn4xHGjt2XmyEPAfkcmkPYp6IkxligdNDwh61GCq1Ai64X615si84tn4R1Ran7kuAhuyCPknVrVAVcUXZb4HrvxwUX8SAqnLLjurKSgHbCGKcybGJuuWwGSxCvqeM5zhos0GXFFm-HA6T1UEhlFtdBCOEhoTUvCOK2pzwFog_ckO9wZSARO_wmT6IGwMaZqPxpGktPHWvz_kk1v1N6SuYNIw5eyfJeZwez1PbxkRH4VgP0326YWcpESIJ4QTodg-duotyO3giEhBpNzJmIkKTJKy6tUXlRUKn6zQ0oB3UOO9igVhkXh548sg76vZmjYWuAGYKDyyBRt-i9I9JPOraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاونت توسعه بازرگانی وزارت صمت در نامه‌ای به پلتفرم‌های خرید و فروش آنلاین طلا، از آنها خواست اطلاعات کاربران و میزان طلای تعهدشده به کاربران را به‌صورت کامل و صحیح، در قالب لوح فشرده (CD) به این وزارتخانه ارسال کنند.
در شرایطی که شرکت‌ها برای حفاظت از داده‌های کاربران و زیرساخت‌های خود هزینه می‌کنند، مشخص نیست اطلاعات کاربران پس از انتقال روی CD چگونه محافظت خواهد شد؟ /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/ircfspace/2659" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2658">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZXXA1czwGaxqgFi8FFVmojACC4qds9smOGxI4LyLZEgaAGbVoaDuVZfi88NAP1qtKHSr3UNOWrTcEj3XUhx0Kuvv0WPIt_lV4ZfGntg4EfRj6iKi7-sMBYnJf3e68lrfNVE_H70IVjNJ0lQtUrFsfjD-CbTVtbTwLtpfaY1VjO4i3xMp2v1XJGtZDZTem5pAsGu3fdwib5gfw2hSHKfLHftgRiWyKWulNevtHPQTB7YDMepnuq8_3dKF48Ak33eajZM0plomt1bRfdKoviXktkV5jV2onnSBB_5F_848-U1-3lsGiantnIERd-vkmvomXUUGLupYvSXP-lOw565gww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/ircfspace/2658" target="_blank">📅 07:51 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnuMEFlKoMUigWhW1cJykFFSd0oAzPEy6EZERI7KkLK_qh5p-eXqBItjj-WpIQc0qWxCWGJ1ZZ8sT7nac_GmxatuvKgTMPZd8S7h9rDRCWb6CKkGL_zb5AWnEv3Y22wE9MlDGINSg8zwbzpx13vTWUQiILfQ5kXzStS_zAyOjtFBjXhuhAMwVSfgbctV8XWCciQ3QGRgHyKkloEosdQtzyYjiG5PJ4vBLRGpcde-q7lO2KSXmiwEYgbfGjw0my1zX6WPb74wBKvvHvPovCbtUB89wW7HhLsCrerezD4B-3sAJsf0-16MSbvdvhzQPpHYceHy_Ye-Akr9AJyZfZ2N3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/asqvgCRsM83YVqKgAkDviCTArpDxR9ihUudxkCWXgP_Dm086vtd5olRhEoHS0RRhvFUKSiQr4vMd6BV0ML0ELNnWfRLT_cU5AfDi1JJhth-M3Fkdf4T5CM6YsjGCLGeyFjPeVpS54giyx-WDUXqdY3FOWVDgf-oYKfiFmHrGSj0leJ8lO6PJ6BKUWeNLTu08s6EPhsoqs6ogTY-XrEcXnisyIg3KKeB3nCrATEw2cnC59e5LGK0hFcOksl8GtPVyWxcQd3GwM8HwOfRgmX7gMfojmCopb2x7zA7yXBNhXxldXQfhwSgBkTf2sUb5q5a70hYBkdR7N1oa0yqyahmZ3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iy8L1Jvujo2b8wDzBKteNwhwteHVOq6ax3-1JKbBxiiwWGipaf5vAZOb1YusY8AOC4rfi-CtDabMKur41AGXvfZ2u2igsay4R2ZLIjnJ2L7Xs-bzHjmAsZBB6icaUucaVUlAzSxn6v4k3Xk_hQ0rz39UCcOnmAggsQyciVkVNxRKHSaLgoFBRZUqB0zu0Q2bgPj10UvQ1jCrpgvnkY2baTGnPWs43W2GVzPorE6IEgTF7ROeVqV76UGoJ-WNO0npu5ZhuIcE9shYAXQOkr2vg1Oa_SZm5SLcgeqrorH0WqGkh1OX-y2nrGaOPoWT8VxQZ0Tyn2KD-yde5XlztLQvoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YWyVa0ODXdHPaWj6N0uFB1EoAJqmC0E4NQbChR8orkmvjDYb4mAyYD72SGYnEauwnl4WIELh_WVZvBKFr86Mulb_fqgUeBBC-SWLBcQDfAMz0qt7bL_4i3oejeyFPmw2TJF5nZ54moWYi20KrfDqC03UwMsoJJhmYWsVQ-CPUDTb_ZQfF3QUqLBuUptRRUC1Ujc_1td7iL-39G7ev-58DaoyBlagnFrp6xyfWKEQVbRNN-dSM7Tkt1Z8u5Pv8r9X7cQzveWEuW0Y4cK0ghPotW0DYzBc_KXdhWJGj4MO10wNSvYAcDM8XuYc1W4cRdQTKHSwY2-4129KYOBiGw-0_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LukarzJdcf4k1Oie8BTDxpmGPBJyju1uZNJtD7tev6-N-wadnsiwtu0Ayjjmo0KqdBKtBAlzClRM9oZQlLMpQiTkWTAqR5t45FaBSufzNXWJzjSah527uRg92NfPg4-oEJYt7wZJuxx0TGLXbxrtJuTWUxTiyku0fxL-vvP5o9_Ah2hajzLra_a0g-aojH8CQiEfTpl6Q-dF8DYEJizmxbzyiM4zvSS-mu4iUvaUCzC1vvRUQlpOl3N7RRzd3vYe_6oi-x9f7_kT4SB7raDkNEJ3uEACVjRykkTgunQSggxvgLMt3R4HvUm5tQLYwzn5-iN709n6Kaj4PFHxNgadqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RWDh3b5bc-nlp5QKpBEzg97xnW3zROqrOJ_u298jEkimzCWuOY2n4LVrDgaxL0Wk6a0R9NpwhThZDUQL57ff827rHtPDeAJdFooEBdLOi7Yu3QRwREycD7q2CEhJ9bpRZFlDDXvP0cCKVvVTNk1u0VqsCplUz9TBvo7lft50lAwsM6kRc-QkI6dvwA_zLbHiHcHihTwMuyNiULTudu_bZs-ZtKcXucMWMHtnYkam0s4hJEne7W575x8XJ52dXyrTrNfTRBdDHe7RrH4qfOBii_qtSYZ7rIa9uLZlHCSCUmx28FFHho6u8tfPLoROtbL3iyotOwcQbf32O4JUUpJNmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQSvGvNmbQLv5q-E4WGobTCyuaCJb82oSK6Aes5kwUsdHydZoEDhuU6sX90HpT9Gs38RNpDNcfcg8P5Ged5X-feoB0kbBFoDHRQwnzo6ZbwSmgDd3TwNs1oIRuHBIPSHThPBKmIoH6Ts384kGD6Vg5Pj1Cy6ruSb98b0PvU5Ys2aIAHaXn8VzmQ0gn_rk1IVy4S_KKn0UeY6GPulVEAP_ZhZE98P2lRrVTdBRy9WsLIk00zZA-HHfMS6w6g0eHYwg8h1cpL6KpFakYrWbB9rtPHziwacoUPUjItF15twZ9Sj8nSFQ7dYJUARVANn_XGfemRV7ERwVTH30HCrPS80ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RviOFP53c9p6ROiVFBdEKs7L1mGZY5FEGlabqGCM-eAxrxu7BKLH0dC6UVuxgVs-qMPfkQq3MdNETlmQgmWtdMrKX7Jh2JTfn-_t3eupqYuxyHlu6Eap-ro7xV0K7SdcrC3ODJDDS-KRH9c8u95WgJFvMpe12gIu8qNMNUEG5f3n7rpDVV6isg5T-wuqEJ_6IajSO-lQy2-MZFfi95UEqpuM6tytFGyY5mEF50UQEt5G7k92NEj27Vw3Djw7l76JMswA7VvdkVfgWFB5NBRIhKDanUEHKDtixy7PWAjwQLuvYIplpJBo2oqLf7oh9Y1YCHu15cJ6Ebce_7YIupF6Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cPUInI775RfEptn2XycHTcbDt3tDACOjyfvQz9fisC6jY-9t9dfZgXmWXKQySWnrYSVJLTDvnEhn-lH82iojZqGZPgY7bpdTtmjWmF010d-kh-WnlhPTOFsj6hzviv0OkKlXLrjKN3Q6lfO04pASm-DvoVhA06ndUadpPySUBsF6_15b0IkiApmevfqhBByH6Mw0vo8JhpLxYm8CVqLBQowZ42TDn_swZ6XnbDDNjJpxHJX7sbjaZ-ImRQA_1YVwNonq9RECxxrb8SY8k3BhQNTot8bVT5CvTKPA_aM-fKZLuA8w7mKgEuLLfURqV0mdLJKSga6mkpHS6pTvKwx-pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cfkX9tou9sJ71eZWE3Nfnkdr5eJ0WPnhoVmAaZH8mb710c9jZSW67BBLOtusprqEq3kigdCsBATJLLhfQ_h06S24kcUUnzt8Hqi26IO7br2BWx83_6sr54ackuVVdfjJJNIzvkxh6_AmpOHAhIB4XD9XaBd8ZZaG4rzYA9JTw_9LSXYkk3GlrkOAhbuWS7ngDpisKLFxWp5OLSeK6K_qn7drfDwu9D1zDtZDKBbceXOk9iFZO3MxS-lrBRtUkpJQdxj_qVplBu_MT3lJrvWZdwcsc1Cueh6a-Pwe3vphtAN9xZWEdc7X2Y7cfdECRNIHyau7HUviorp_2mMH2jQgMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2Z2P42_4GNcc_bU3ItDL-2cULizXFgRBN-yVpLKdxY7IjJdGnQER1sijj5AFguuWqRCrjxcvr3t8ppENqRrt0mnld2q3kptKBdBtONAcvh7iWLGuq4K7BYtC6QURWUWS-9aMRUDp4dnUupJCVC5N_rl4AErszmVQIwNpQAe5bomzSW9mks7dS-7qIECELedOa8uI18hKRAExmaqocLF1yJoHUA24WVj848WjA7j10s85v4EKLk7UuEAKbeRh4bNfKDWdgCedZzXHS2lij4BzAI4UtpIqBN6ugjHuHQhrsDrm5lUpvBaIK2GH4jYDpivN-aPwXLERtxwR-gKnNRKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aoMjW2-NnbexGp_RQmWFWNYUeER-oh5G12e7Lac1EoqHnUEjA_DuwQ70xNEJpgte9yrwVMe7IrTRVMcG1w6E-SWaFNw8kHGUZHJMAXsPCwRZn9n6cg4PmPNMjnfxwEvPympEIB_FsFO90fSD-MZtZ3WmoFGRy1rZTYE522hUJBlHGjvdfTSuaIkXTahh24JxPGCGQ9Pt2N8tndIPGNP3iw2SIE0CVSB3-9b38BhJRjwNQWZD6asdttCzn3ZYl2yzB_RFkgZi3cqJGZATMv_6Rj3-0yDl_L3Xh0iRJFM3jwQaA42hJaLsI2UW1Dhs_XvOdiGV5cGKhkvYzozMvRNPtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UVfCaJOO_LfRfnZJRYp4JcXGKu2OKSDKc7z0RrlpnZp-GQoGzqNBxTYxyHlI4C5DEyYqKaEKqvOuGBg0_QG1dNONfCvYBZ3t1k2-NGegrkGjVc4EJTtrKNgpfkxBeM-MQlPR016VE2GqBg8lMhjUwcXJA86roFW-DAExeYUCQyS59ckD43cr6-v7fM8Cbz-YhXL631lHXN_7qCFt4TsKxfUVaOSudz5R2Qc6TN-b0Fjg5zjVroDQmyfEU--uYrwdhXeuxTssdM4KumYwRrsWiQwmX6h6H42BodPI7_f5xKVjn-Y-VN0lI7vC8K84LWFdbVVdg7TPmpCIQnG8P_n6yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KfO-Lmh0LA6dfHXZ-kpSZm7YB0Ai4xsoaCmFjvCHJyFhFDT-n7RVf0SYfAbtHrQ7Yh8nzTYHMpGC59OVYPpRg2AMNb5E7APSE2DS0KsSxaDyBR1FGtzl2g3gdL3xbHojR6p1xPqU0vWfKoNQXMupn2--DmUEBsoDfvk6gd15Isq-SQhBOQcXEhqakdGBinBt-wCVcp1h69bqH-0gb_9bVBbOB1dSvo--jyNAwP1L-Tu7KFXERg3mg5eo3MCjdqdpog2zeqq9IgIfQowheKpYkMmiOY7Cd1KUnIakV1_0BPi7FyieFSrHyt7iDLMcEsDNJtHh4S6ZICRWqB4lz9ykaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mEYIfSM4DFMGdydtHii0D9fhOZ4l0YwqrGPB6CtGWE1QaifSGv3SBIzfY-iUco5V0cUCScr1ab6-g8XMUQJnJFPab15aGrjFow6B3VmXvRXwVaP6_56zpawj5fKZtb4u0Fw_q62FCSxCTGsQ6nnAyx0zenwUvpjSb9uhzxCYIiuMcxzNJaOh776sYXDv6l7jWnIQjUx2RDloxoL8WxNA09bST4qOfTQ2rFygCro9KRbi6s5RTGWVQfN76dpFDv59Y2X_bSc3LFJ9LYyAqxdZVJPSq_JV7eCr9Bo7VD_5BLxo16T0RU2qmTM7nGqpklJRViZQd2OwNLWn4hFoAxgXDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MCdHo6iFaENd-c7ZKlCFpcx7R7GzZ4veGEv6bQ202qfdRpoEOZstvNpRMtVupx9-Lh9MOOmglC6DMtj4neqUZwwTX13PxC1MUQiOypSe5YnlApt4ddWnDRVsyJJse1aXNqh_r8ZPRjFgY7dsaDJIhSTu8vQlDswNoGJmyQYYMlNUwmNJpl5jIcU0V6ilkWTNA7IN_jpjk7jb5HV2cYvhDXuMZOcpcvrhtnbOCYq9PHCLfMfkl9SNRtt9YIkROIleQllRhwN6wZ8OBGVZmRLuAonjPx9pXECOKS5_8wWn0EdJD6gPZN9jcruUpAq-QSih6JwUre3YRa5WG6d-cTkulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DsLEUWFg684GUOfRev7ROD91KGaOrMr_bNdwBbXK09CznT7NkP2ItOjARYHMGUp36-g4g5uiG02W818CIeaJNrFTVgj5cri9_MtUgTQnAtJ9m1NwcVt1QlwOp7EsN62oEtQt0Pa7lJyszrwEzVdY4V6X8S1muCoDnb3F1LWaNH-D9MFQBBKZClJire9YGibcQeoPcGSVk884I--8VJ7aV7QDaXDmDMomwhjZDaAXJW0EQw_DB87z9gKMKaipIwFkvwucOWXvVB-EyvE-yTer9jNzuNiClvjPnRNjTGkanvHqbs5UuW54cBa57XvE28yWwHYGIPyNeC-egZYJ49LKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AB6eHE17uixZYjxfbDsIasLkO_xpK2D7GnAPIcPyRQEpcNANqiEE1JxETHW0kUR5sgsxTM0KcBOCXhCsV2uAA7E42r8xlTp4B1G0KdZWPxiWd1jMtmnPkKQhd6XyXFMk0N7jRzZMVkB1MJHOWG-agg2KtYNfZeQomKURquxnKCaRsHU2osTk22NSiLRP_If1HokZ4CwTOcktpH9K7zKfUjJoPK62Z9UhNP30ALILmnoQ1W2_SkBIzdB7GmZSnFCvF1XpW4wAQFuazoq4zY6Lqo8pnekBSjZ6zVxbbvLuRpujHB4OPQSgomftr635_xs-2iF0pZm0BVqx8Jqz6nDo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vA79wrkH9GFXsqKHBdM4Eu_eAHYKBCFU4km7hIJOHX6C3-W8UVXspjkoySIA8mr0v8hP9qrtzQz2DWy_men8LkNIJg4g9IeLFi5DJHTq-xi1rll9xbQvseVssoREnLHXq_bZPumRmZBkCl2YgDdjjO0oQ3tR55tYkeZkUS3FaOv75g8fiNKWeUXpZB53Af1ban3PrA8nR7QpXmJN_JjYXC0E3vKMqh-9iquTu664m-ELoFf3dWgSlsC1S7zTG70SHGdYi0SQUCfv5i7874t4a8F_YeBl4fYJs8gc0YEky9H9cwt-5lU0k2qBcgAQtCecmmbtPUiNgtBsiIOuGHtL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LPWQXsxwDfsJq0yBPZUl9YjHxXAinzOt36Ax-X8n0fDIWdenzOjGiGnxsXiQjlZ7ARHUD6hTzGT7S8krMD8FJB6fpL2VjEWqAGdQDC1V5jD7GG1q8hvkpa3yKmV4JU9tKSoI93ZSljZlahZyAcLdde3vNBmzFoToaTZxtrGtjURhrEsfU41iAI6VCwtYF_jufb4zg8SCH-8YSVHfVpnVeAUL6to4lCWcolp0V0aczbXj640B8SeOcUVPoHvzGCcbRdxC1dg31USyghSkWW_J3rOtZDjR3Elrm3sLgl8XHgkCRFAHmEH5fg6MarYvh5--RraFWhjVMr2l0PPundecmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oMHMIa5TqUdWRRAIZFn422JhlI8Q9yAYiGgghn35wKye2ynZvTipa6U3gzW6Wc-tBEOmuZ7y6sr-vX_HSILG9YGqDHQQAzlJ5zRSPy87tlOnl_p2ZcO4k5Szoc3ThYgEHWzlqZP7cbZlRQ3cLuHVk5fRT7Q3Tuoo7Xh9eYBTQN-hUmb2UEZTibmmUiDt_GVE38rRVMuZvfvN1WtDeQOnVWxaJWb2vf5L-4Jvsq7t5l4557p-gmU7jVh6yfw5Cv75GMUc5W-ByRjVnhO0Q320VagNLn6M_O1kafY3Hfj2n5TSt9QCK3tfqA_hIguY5aWAqYKrxLMyIcOr3YKFWcMwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yg98YaAzPoHO9rAvj402D_6jJxlsNLQ0Hpq3NmBN44_v639y4NZIiZj1gau9K2fQwpDbcq_asWi_3vnKmRTPGPHlYLUOmAewR-tAXhLWJ2KRm3YmNJcg_52_O40Ccr6rUgrQNqNJZeBxXFt3WzQscZisseezyWILG2q72c3yoG1Wc3Ci359GekfVTY9Ol_UkriOli7eRqNufEAr-bEeTCnT3nIJ9czWgNMAKy8vVC28hKBrzdekFar6MXSkt1X_EJ2LORjz5UMvyHErbxwsExijE7qCCEh1X59nez5YEAthXM_rNu4-ELber4fMv6SXDjTM-JAF60CUaDOA0QaeldA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XXQgW_3G2pvDbzGRnKQXBf7LEjajyMCrx3M9zLo6rbPlcsHj4d3Gsv89uzfsKwWRjKiAgt7DdfnHbZZ73EPirIxjhRNnV9frd29QMz9YiLv79fGRlYcf_ZHQ1dB6mcg5gV8mPbylNzwiP2SPriVAPXDiS86HR2d-lzKsLupxaMs7U0yqBZf26rFXB4yKbEGT3qTTdPwY-cfiB67Gc9tzLirelXGLOPHfMFKUsTiUi_8tSpURrzcpUi18Cy5c5pknYTlGpHhZllDW5IFoPNnUyytMJWyyTXv67zsDwyVK_IJm6CDgXDHYUuQgca9npoBWdZ22s60XvkCfLsXJvCMwuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uML-LOcwkUiSAdh9zuP08c6WblpoQXrmEfTlbuUxUPjbPXWVN3YmaWox7-mMv4kZ60Z7jq2Lj0T6YU2sHNJGgOGz3iecwi8P1nKDb6bnLIjJGVDHq1FMlD5uA-AlycsY6g1G_KYS-uJ_Am6RUwmuVwJBd5diVZSKEmSaIfidZBWUPbVWuD01xd4lFHHKrAckIDUWUrAAgT3kII6eYEMYZSqMqHPTyHEHC4qi-FMv4rySsFzSOKQ_6YZqNDkyF7APlEoa_GU1n9Ae4elOBR0tDptiWfJq8clzSTk8zyzESE8D5mTkEn89SKuou16pCMqPweQn18YE1SiNX5sx-JQm4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QKagKQj2LoVo2MJ8Ov4J5WkKZ1LP8S7k2CR6rFkLOTLkaNPQpEkcr-mIDToPq3OBkCxw3aV_vcWstk0E6WeKgcm4OTCneDY8pWM0IBrq3nQPDEf__67Vy_KNLyTnLIUptYjXuSgrRLglpgUL6fa3aCWuh6LIG4oWiEhHWI5-eM2Yx_qSR9rNdpvaBcZvJWFtCqk6-htk8atWWetI0W3uzTb6G_F5uTN6XY6QID4cJ5WS2rz7co1sonemfr8qDt4o0lRQXBHPIv9b4uADac3iUcBtGu5lGpKP85YRbuO6ZfkphHNMZTo0n8O71oNpPn0u9EGtbbKhbqE05We45FNL5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K66aCNoVmnKnGtnptzjPf94yFJR_xQPSHSgD3wjzhwpki363f2aS7j6vjT3Mx31xuyHP4ymDOEkBFmxGisNAFAJhfYnnE3XKicfEr3V2YWw0aL--qttGIbtzs57Y89cfcG3pTGoZtYlvNMWwnXfzp04s6G_lYVBAA5c2fkcj7iAhJLgOaOCAGzPxF-09K_67isY8wFzJTcNxBtIeGzba_V6xcYXM3qOlVHiDmJrLvI_r-Bwmeg6SN7qTWo78rswhYqZ4dnHv-E84ckHLYsOIiFWmeyZ_Ercfn5bmIA0cVBpprTyMOx3uzScA-rdwIxZNIh_WucYnGSU9ThOUFrhHNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jMwBIPuyN8SGaOexZj3rDITpmfK8nYhmDu--Z7eBIcZg7Dq7LJLBiM2r_GPJ66cZFBymSgbDxac0z_GRJcqxGbjc0NRKOVGhbqE6oadygHbPLtIgLAQ10K0orGdO7DVdKhxw5OC_fUTcVQZh5mmPLR-ULaCnbv4JSwbcOUioqPlbdBxOLqH3UK04v2NK1Ab7VItzCAhwjDsxlwbON0dx0AFrqdPvfAig26J8TIXS7QEn7N2f_pX7HezaI-_69wlt8_Y0AJubg8CE3aY6ZrGlyxU-qAFLnTeoj14SpGnPIjADhKgw7HV4mwANX9lRUhpaLiWFPFhbhKiZxnrA00Y4fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i2MSd7KidXZurQY_L0htt5nybPP4WfQM79cXAph6Np0oYFG5lu974NxHVI-YEE4fh4ChiZ4bIifHEbmMQTjeNvEzmHCbGckf75jB2dD_XFEYeBwins9IrRqqRZvt3W77k3mM1zmf3mZkWBIJwU5-uNflUV7xQp9YlfPrPXu6wiyNz-ZH_U_3t9rFBbwdSGUiDXdx18v604lnN7kWtsXR57RHBvrOEvY51oMH5QxTrB0GcyhtDM1GaFB3UjgSLNe7-wd4O9q1BaaaR_c6G-b9Yezx5JTvTZGa7maMzukwRUX77it0Jc2DLErOqgR9Nk3r-ePmlHtyFQdVUjEbPfUppA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TxgsOR-CLfzTdNRJcXCr0WlletP7gdwsBtVDPuJLgWBVJzb5crSItWItqmuulNjXfhVDXJURy99W9he0H12aTwLFOBPUjU238HRwIgxC2TboL3nRBh5cjN92PqRafvf6Ey1fQQ5sNnfFAzog5PvRUshtVpObbaDZ8jBqxurCUlZ-DIM1malAoVnNfkHMQ5I2eML59pRJVs3d3pZq6aomhf3njwNcYRsEU4kLtJ0Uyts--FFzM4IHJH9t9Jh_CokmwGVlQIK4zRAgr1J8a9GNDgNuB_oJZQeazI-co64J8jvBZoelblApQ3lt8OBrI6ionUq-jKL66_UL3z2_7CIRow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kOmed2Q3TT81B6a7IJj8ZDdEWRy5_0fZ27Ttza00TGr8ho0uTxXYdybgjl2DCF3TBJMKUVH_ik72HP5aVF_MaC7KKTIzhd4BD7kOKfIt6Rfah6ESr0B1e62Rk0H2Zt-GdiWHBc--OabEAPuz1YVwgw1hnyrWW747Kd5H1wAlO5rTxuZDZ8ophfwu87ntmJ1JXFYWufioH9b1lv-5a8cXFEZ_DVLTcnthO_GZJOsYQX_NO3Gj1sVLouVbBN4m5VaOY4oK9VCAe59LgwVb8XEa9Gg0r2-lan1Jv_IuATVXNzmKfTkEocBQbQiNaJYUuAdur7pO1UJMl6nqXD5994EH_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1CsSHv7Once067QDH4s91eczUgUGyLXQ_8Z9ERsjKpe-SQdN5TdyL2VMX6Td3Ho_G5D9LVrC_27jmQwebsrM_srufYii81aroYq2Tzk6zdW7WY3or_iLF99x-1urtDvpjMmGOwJBu4fScrG06hgPEoOInEZfFnYu2jXy09dp1eEZe9yc5Una311KX4vpj7wfeofi215bUKl6Ozd3dLS_udlx6aTgf-ICJSezVA2C5zjuHCXSzOaTR9oeBqx9NmJXtYbyoPVLsXN3F9D-UExXB8RyaPhEhsZ5cIuwM07fvhZB8Kr_yPBRUREpaKLhJeUTBm_UZh1vqXdVVcE2QaR1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qBwDfJdaGhXjQuiujP2R6w3X3k71InYBgLggvLpCcJb8eqwJSrNrzaV9Y8Wnr220jtyzxv5UoS1zd9i0adrm2HxvDaFYjeUgYxhlHfah1uf9kd3byXLa6KdbOHZs32WTkCuwiputLEDCqNhg1wyj_lPsbJwYFKDtfLTTHdtSfljoqveAAK-2dA69DX_Ud-B5mh1aZjPhCC0tvStWRkEhYle68I2GKDcGtrOjxkhY5v7od-I5w1ueHww7o5g7lwOD8Iejm8OTfhEDkSTBkkMknCMXqMLurpP0vLXN_a-Ze6HqnJgyC-JSHZUvpAPWLAkoIgTzKn_yDS5Nng7Nh4jETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KNXAvJLsi11sGWbjeLMaSwDntOIBjNct5zY9qyLuVNHTiY5fS9J5zxZok-LaXbVIVwrQkQx96SipidnXrvLh1XWs9UWOAi0W3fr79S_up9d4ItZg-2-7EBU2grrMwAonDIdwir-ApCZkBH17jcPumC59s_l6EB7m6ZnRAQSY0gYshLTZqShZTjD27vR6LbjIPcOSI5vConI9uJaKh-AL-1GZFBQ68GrYYnPZsDh1rEmT76OHZDNKFFf5nrbOkUaZb6es4hIDPIO0IHIwa8xbD_yEamC4nZQJEw-7enkm1Da8ly69W8LvMf2BrzdFWBO3QEFSxXkONmD0TkjzN4VgUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KD4fKdzltjQ2_tEh4qWd13dZLcYdy-5F0J035Ecm7b2U30hVUJZVGBFh9sFJdPgEEU9VJNMfVLb-spjIJYYQujCOY_OlZzTe34Lzgb_Jx204AAsmNuIWGJh8PHAU5lvS1nDXzy9_aO2CA-1vA8BSqVakvtO1JMCJjXJW1SfRExbBtOJjrIpXvQYlN0M710Q51aZHlmbi80zXCSVTO4sXuDpgnX2XHyzui_knLMeSIlmbmrtjYq_8_1EzrjAMEGW7Li4U4gVapULmOEv0pnejTdGnjPuj5lIuyT1nk3bM96W9lV1rz_r_1GcwpOaKS5pwAYIoZBAhBrSGoa60QZC78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lk8KhGExEXqhuRGkgQ6mEOeUKVKGIeZEM6ClHT4zP6o0GMbtwUlktXDO86U4sVgBEwuPYz-EZ0ykpP_cO0Y2uTolsL2yX7GsYVmp1Q60_R7-UPTK-JKykKkEzOLp00X596-cd-agpgbzTzdzvDkBt-s3W3jN2yiWziPmGZSW6hfUtFAq2KwOvVs4YvHrtbvV-R238GMY7U6eviVfwJbJFLTpWEK5XE7PkwvYjSSzDaiFY50AGxgHS3bXc6jNe5AdvtHsUTvSeewfp8iGzw7duS6pHs8YnyyMhtPeNPEh9QlhDVGbPSucBKgahCIvoufoHF-q0yCOg8q8jZ4gbjc8fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kzqEmrnPA_Y_3KUp3WX7CJCBYnauticF_LvLfX3M9nAUeHZpDQC0faPWE9Z189C2OR3IQplfLSbKMnIdJchcqdTtu9UnRTGLaan61u_Tf61S5A7sjaeKjDtDg2okFvelEShOtseRR46CjCGt_oDyhJl6rLmQ2R-NSstTLM_-sRh-boIs1HW-4MJ2L4gaassNK03IFji-DVhsQoPKyosXBF0yW9v8XWUKeYo8Bj092hjoonx9Q5isF6IqlmPBxju8STljEMTp8xY47a2Baha1UVMF2wEw7Uqh46rvMUIyUR4fRa5CPo7LoYutsnBqx4Fk8Vqpobi0obeIHeTSOlyGoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sgf4TIWki8rxk78P4WFgALZ_IUHWdKTgDBXmlsG-Zs2wgvrHMSKsI93Uj1Skbpuba-IjHSi-xrhHA6px7RoXO-WfmuthAH2GYmBQYe_of3JmS7EwAjVY-buJYN2dgP1b7s8WPJTMMWPQlZ46enjeWASJLFj_zAIGB0RS8OuU9T3D4wzZkrdD8sehaOM3NiiIU3b9KIz-58HPDPgumWS6QTFBbOGdk-WoYxVBosTkHMez3Z4l9vNHNbRTp_jTi89tvD-vEbfGMDl_yzYNC8qfOpIZTY5dAPtQqkrsWY9U-Xff5LdaQyax8tWk9EMUhhAD3ymL5mKmBqz5HjS7Wzc7kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJ0N7gpYLW86o3UF0m66gxReoL2K93bTUkF3AbZjnDltwDUB5A0Y_afsCr0SKnUtkLMD0JsqrFJ3qbJYBbGBIj2o1RKKam3DRGv8mf35bnrzxT2fMBERuBXzSXrWX__ndl3Ihxd2_WdNtOeo3Ow6nMmoxt9t1voQ1ierTV7kqQ2sZygpIUfMtycsaEPHchwn3j2dTzlcH5OMz0G2dNJQaSJN44NwAORedMco_4CA28DNcYzspXaeUuIVvqRcfVD9tjHnauI7Et-igECUDnmLT6YhAcv_GMJO8eoG06lAU7p9bIv65dXhwYi5KLN7a7EW1Ozy7iFzjWd8ulYTfA-pxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNtnV2af9SMoqeyVpkAdj_05MXUP0ZgQ9AMu2f0n0U6wFKBKFba0B0OyY0oK29kw1BiYMi1-9Th7-zK5wwgMOLazaMhuDOmCbCjoP538_Ib4OYgre_9VeGuMfLi0sMqagKDYAMNOwqXvXZv-1uRM5shlUFvsufRxelLBvI6TnrnwBdaG9x6U5uHs-jBRA-WRMs_F_L0rOh8blYjMqmzCI-_AClQgSW3O-iPPj2h-43FALeve2r-1C267LuY7jWijwonIdbT7ivjB2J2ZjYTASRmMgHRe4e5RBhi4PqP6Bzgfc-SAflZS1DpjcmR9Wr_aDJoHTYko9iNXmvmC8Bx4Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WofjdVZgpc4j4GxskZprQN_sMVMmeCabc0RjIstjdaAoElr0-T4Lxz9PuVOST9s26pcaJ0lxJkysP_p7ZhPxplm_mgrLGVdiL40nNLJNFtVNnQFzjW1Av5FPuKKYVr-wieHfckplS_rVynqiAnhKj77WybUzGeilfazcaCkpMJydluo4JN0fCBAoBPlyA9JnOEVAWxgjSPh2lSJ91OB36mp_W2IvQmEh0WK-sNxS_mgGIsdlG61oMAJbifoSMCmj2fQoFJjT2ynTtqTzOXCtTXX5WzvxacVZDcXLcBEX1teRxaBPouXbA50NEDWAcJczdghpWmgCB2IsODdxEWu20Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/srbXjP7VkBWwNu1i6Vt1qS3JYqVQsVaxbxYNgQuDvwHl6dFZECI6SVV4TcuEVJApJ9RPf5Bi7hVbfVf6e9eVRZlvLZyteFd6DFyXAJxs19vDxNqGgXq-xwttycF0dSw5EKBURKxtvFLwYKig8PwvmXSwd3R5l4MvDsoE7croB9X8y86-8Jrkwl2M4S0meJWIkpFo1-bO1FTT_WOteHGbqoUIshRl-CyfeHGLfatT97Fu8N2PxYiicxevkPgywDsPPK9WPqaKbrzPPEw8bMhiaaRdg0kG65MOxbrOzyROHSB9j-x6NhrrtbxlLYGGstzm8fTQnhOfaxEDRfCBSS0JBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ofSLb3fwoUViMH3KS--kpGiP19R1z4E-tR-K6R6ax8a9h11ip0wBKFfKdS-Fpa_YeWlxBSWhsIIIkZkwD-a9Hmgw-TVxwp1jnp_8PBN-pdhsXh3olI7-Fm5hWCqse4_thnNtDuj2jMzAVzzV9uS0uMrJP9XGu_d6rYr5vx1qdV7u242ikl_-GvN-JQOAyN_ckLfrYsZkeeTtT24olAssAHvBr1gV5Zhi459LGk82wEjchwQ3V59aGNNLDyZ-5gLfGi1zIpgVIjFt6LPCCnDd1m5GNU_bVsNFvylF6vjOpGl5yPg3U0MRJ6gcKZrZ-CSeckLotQzdQUDIUP2MNqRF9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UqlvQhr64YFa_G1esZUbFe8NbR0bbEg8o2aZzb5mDTdIrvT4FepBFtW_KxEolntUUURjAElX0HOuLZvDtkmgv95huWG9rzVifDoFCU726tdh_XfoKprlbDyA3OkqX4UxkTFKcoLCVTX78nzDfTScH_-PQau9ibZYZekmzoVdoX7ytL7f-6rUVadK3HsO7cqJWh_ATqXioKrvXDYsjSqkrShPnSIqmuH1e_me9DCvOo0Iuozz24SbH8RKJnW61f9egrXIlaN7tJrMBtJxM3eurMQgtsP9eUxrVTf132kAZePStxjgPuNYKnCYPALSre0ZMVZa_-cbwuMDWSXnbtKCPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ygua299KFOMvtn_JM81YQdjdoixtaVVHh6xJRPvXgPnFoVS7oykF2FWgRVmJBLqliWa9BOJsXkKpvnasvVWJCUjPqACTZtysM31N4kOF09pAkHaLzjrNuQNc-lUHlsAyP8FLY2Og8yavaquXAXx80v_vkc02mSgMfSydpyNqAxtM1qBQ0MzYwLZX0RFOBT8i3AvI0a--WaqevNOZHlR-cg44MQgb4l7CUw1ALB267cRLucLwIfKOxB-oafRLAjWXMZDLw4r04AeuFLHogGYnP6WW8rmYBH3goLp-SCAmX5NzBXqPqpWrTsmFWaaBkQnus_jkSXspg6JhSdRUqctIww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hA1l4JZ2jn0bbfaYEpGz9tyNEJGPlHiKhtWecq8xL5gBKrXzaWJuSj9dIkVutueZkzihQJv3cllePP4_97lRf9eBaRV9cKXFevZI8PPnj0eXliaNIqP3h1SS-drL_4T93Ile5HyT1UG_B_eWK_qBnZwTfBSp1NrrWvVsyAyD7q1f68s-zlSh5WO9phBVtFJ-ab3HAb3Zf47lTsVZADMWJ7dMHnpKnOE2pfQ7-n9OhOtf3JOb4r_jHJz_HFlOiQ_IU2sGiGv0WaWi07dGPUTZBvscKTkuzVLx3NlV3nQ7AEjlgUmLH00N1P1ZmgTHcPHCzAM1Dh4TbJdnNM_5srDRWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nv0XT3y1SQXJwnpeniZsKwHYReTcRStQHgkMlLSnT1iuFvkL1lsO6oW8C23Z0FNN4Qpyi4UAQGWtiztNsC-90e0lX5GEzXoEe_amb_sgecNs6IuOt-BpAeV1QxLxJa71eSqMJ6NkolJq9Ib8nnRftoXBPOfJwgWJu9oo-DUW0n2JzxSy24y6C6ce_ReAO-kH_musQXShBB5fEfs4BfuBU5ZYPE8tcXM_MO3m4YNdP-J-vy9oIXNgIV437PbU-daq1LpMFwkdemFJxkknfm2YrUaAPWWawmr21yrMQlbozhJI7V_LVWNNyppYwEKM7ePtz2OfZHRfIsi3i9j2ufwZ_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t7nMF5qNvEYTBALddXJ1tVtPYHhV0UV66g9BtxwujOJ0mug_4eeEaaoEZOOGF_NXbfHJEmb79-QRzNjzN6SU6RMS0WfW8Y8zuM3MmyvEIKCew4TNMkmZ8stFgcVoitkcdVYrh9t4neb7kJl3fKh7HUDlUH3peiVuIDrkxvlZFDin21yelfpYz0YehJCl1hSI7T0KgSzu13MxtuPLxIl_uFF-oTK_QGbw260aHYJXv5BVw1CZXqMhnDmPkRfisd_Or6-7zcZhv-zuqiNMQFUcCg2Fh6SDdNtQwKo8WNSt2jpBRSfrJS2XjCxzLr7KZ1d5S2XXeqkYEd_N9WBgZQvp9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DlKfFxLLceaBMAzx4eFtzF588XnSgQsh7BwNFjU40MErZXmf0cllZ3faRdzN6txXwmBiYFIbTR-TAfQg31YBKSXhsMJKOeFNiN7CyqRQFmKA6Vqh60QZnZRdlW3airRJY_SJD0lL-lupgyukiA2TdyQasV7wXD8wXAE2GUp1EPFty03xflPL1l7g9OhNViwvAqi9HLXYgitK2f87THxHj9QBXF7kXhN3VEeXJiYpnYD-HfnoXqrT5doiL6KB5XiSzSJJpEmKif4Se0zoBkGnppMQ-y9yHFhlAVVaJxnFBD8vGwJ5OcM2ipmiwhBKJYhCBcWF1P8NeBVA7cKsgbIDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d3qVWnnQ8p7uN8xekfcoOXlAO4nBDyIFqbcbe5iJTFBB8miWsM5zV7Qwwayjth1O2x6-k0T-rz3qlflH0RJjnlrWnZ1kEF8hS1W62lKIGwWleS4lVJ9HCdCo_QqxjgFdF9dG1cqekBBm6m0NDrectXtm1XDLywuW_xPjPOXzP0JGwXAzEAnSL4yupjfG4n1o5HIowgku99NRuvH2AWt-kAaX20SsTpU_9t6rVG6dsTYWrCIof7d-7INZhAOxz-soDA7_kgoCLNVzi7HN7dzA3_yodk3gof5x1OT7OxhFOZGSxB2xYO6jws8YLg2BqHSDt6sve_fQqVJn7H-rZ_LyWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c4LUHyDtnMb-3n_ywTsPZShwgDqyU0MR5a0hDPYzOMSA33lBGknRTgoQnFNjdwRQkMQJ0ZJGRV542oYbKsYbL7BY4atVZXYCi3AKXvpqdknEnFITTtbFGf_El_cTopy1Y1PNrrdFlAnUb1Ygg1GYPSYqTqn__-PPgYV1Q9Bsy5cao4jnENflkS_87fjUxFRq0-tvYz17GFSz9mvbtHMuJBiBWek2nZvVrQwvS-sVEZ_nlDMyEDYbrT0MOe2kWyK7pvX5JFNkoCNZmAlFC3ipIwvQKTZd4L_HIyyhctXahG_N_jrNqID5-Zk8fnfVJD1t2_lXs5iVPsHaivrzXsZmgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DKPoGqDPkDAcK3iZRBEHxktYpYavr7ipYkwu0Yz3rVrEH_CwINDlgLbdjGeOkJLj4Q8Fxu8Q0rJw3PVGwt3NRVKssAlV7Ag8xtNLrXrTfAbFwV_-mS2yAW9sdmcHHnXvJbiu4zTxJMqwhVzHL5NMx5hOPCQUPagUNLCeMsSv2hP6rt0vJaFYCnHAbtxpcFK9fLKwpYqPKCTdgfw5OL2mn1wUS378J8uwGvZkvkxvlelj_BS4l_07qXx8cdHphcukO5C8PPLYbmgjxHnFyf2eT2cQfcy70uIU3z3jGxe7is3WJBatZXp6v6Zan1dCCnyuxeVEF6Jmw9ZtWe_jV97izg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GE2HnwPOiz-wJkRIl7jurZMANZnaLIOJOAQbsf9cFQox8QS0OZymeGusGMxzQkYmPML65jZTV89zmpmhYVlCUYO-CUj7GgMzeiUFuIXo2TouBkSBl1a41UFB4pL8DNXtBI0MwGRZqBu69Thb-rBu6IqH6Sc_uCxh1JcCzdEYt1SNXLnbkAWoFmAELJSbJsGfIfURYlETxU5C75lMZarLbbe86Ww_JMZ5V1Wngsg_BlU98bK0umoHxPNgi8PQrsaAMlggZygz-o8ngV3LC9T4y-RkM-ZaGGganhPWrJRObQbnVOmsB9zsWjT-K_JmcTwV6ecZNYpi1c7qky3eOxK-ZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sSvSW6hn9XC_J6-8MYnR3Dk1MD5kDBcKjQQfCaQt9FEqrL0WymyZGvWr_wSe1Jf0lwp7J3biHlIcKc8D6dRL_gXhnoPLFwCI4xbBte3PVXV_l2EuV5wPgxVx41a9C8ckGiEmBkvJXaLev8rFN94BONn6jCLTnqtKtHmDvioSpLLqSeKCAWSgCBEvgiaCkHQby6Bzu9BeUIQZ95TSqcOMpJoGXnlZo6XILCHSoS6aEcn04V2wnxt_2SP0Vr5HzAzWPlZy-DSR4eyBduA-WKoZBk_nqcHyWzfTiGxTgowje8nHNA03zXDzIl4VSeBvFsWsqZFXP7TbWc6IU721QUamLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BXTJ8mptUNgNWCbThIuvS5B3gcuTp5QP7eWzRaCjBQjxQ0vD_pe1wMTPmnHCddlY5iA6gFK07X-ngRz_G5fJMNlfjLSrXl514evLNPjWdivymwvhkO46KL0E7HTDbbSncENHGdidwfY7K1huzOqg7Nqz2hWyH6FgS2cIeNN7i1wnxyu8pFgWpnm79U0ZiTfgJrEhZrLtVBWVTnm2TQcahLDA0Ncl3edqX9l80g4paOeXQ4GXuYXzpkVGOyi2XgFUQWNYeTJLdF8K8iU25ES0YGF7hVdCrH92ilnGxj-7jbN-D2h3rDW2u4odkZh5tdfndLkI1_BXVbKKhGlP7hmEYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gnjAGVASQCm8uhKxTTQFQcFE12QCm8ToRWkGU09bNPrTYFS-da2JtiYlkkgy0kxYn3cjiRbMJgALBToRLm3t0BYUWVjC1ReN8PZj92kFw-ueujIWfDEzgFB6Mr33hTMyDOgnAXDDjBe53FS99_RlgfEWgl-iJuSPX9-GVrQo4R7SXPws4DPmJaPoj5qgK7F3e2sP8jxjy38t397wAQ_v1hRNLYhbTwkCLA5VWRjp8cR6ARPTHfi2ftC94s10NnSvyaw-5sB4vVDR2TGzUbdm66XP_DfywcLwdYM0osEoDFSKFHrXdlxol2CME2Wr68fwL39Dc5X58Tw9FxxCBrXwxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q9IBkegPDI8TWTtQnhEH0vnonqBIvjnKy9HYLZc5rPD9O_luwsdPw3vUD_H9PrkDzTxW_GjAJlkW7-S4c_ei42fZe805tGxMH_fU8wWFzZuVbudGmXW2zmoRe5zKfizirR8KKH65Z2FiWSqTnrJ7f2h1vLvgg4ms4UtN6-HKCUguwPtXEJ5O09uQkCOpmLejPoHFR85OkQuyusZGrl_VnNVBxMtgrq6LshIqjDWRkGCGmqB02SJ12RcquqkBClRehFKHlfWW9k1IaoD_iWNdrZ7o7ULWHkYYrESi3voD2FoFWjnj5QFCoJB_DBkh1Sucpcqu0bndsro2Z5FblIa2dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l17YC-PkPZG_heqQbBRQSwmRiZOjTINLg65b1oc2vnLQMgWgTeAagoRQ84NcA96Pj8A0UWH_t8bpAgTnBqdzstpVVE4aKywUrvfcH3myY-RtW0UcdErnv2bbyfDWXzinLTzYM80AfJ77984O53H04YC_oukYFnoL4IRzZBxCgJQANhJ2miPydbqAW97JX1sgPjllXHH0sQ8qexCyd4EYWmnQ981iqIKnRUSFRIro9d3cTZGiogjBPOVzxe3V17uQKzJUu80mfGzeGhuXbM8YAF0d9IDh5v_pIR4nayCS8pr_oNBplEwpz_lOX1oo2ZRxLehp7PYtbE6yVe0ZGCyhFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G9kxKWYlVqK6B1hKDDzdjRJRT3yLh4G7uIG5gwjmnuqwSOTRfSoEPPGwV_mQVfsRvvObZB0GnBj9sTNqF4OAsZVLu6uhucDzpYH7pUrSXQfgy5Es9D_Xe65sAp9cLodHmdRikN5dKTrmlgSUmSENeE3ggXovFKOxCZobeE1UaEfqg-FbXr4eazEUvZ1TUw1zJ8mM5PhL-nmUaCisTqsAF9oiWmCWQhITvmg5OQAu7rpkDS8gISfPW1hGTQdPDiGbKrGctFq9KNyeqqP1jvw-dsw4fzpqp48hgJEEW2PDkGODhr5OoEAG66BwA279oFsqNUpagGEfY8ZPUdiYSFefiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jfT8GYRe_i_7fcDhPb5uEYJuhhmJ_jqUVFq6voup5EFtbmjzgncLW1zbsjPLeHa1E7cxGSOqyZEw337oEKzSN7EzLWWqcMIDsGGpcR0eo4ojXHRkN4NIVLD1aCGvqRHPbBNmD-69kjCCRbyBnwgJXY2p7LKYpV6k5zlA1vudFb9CKiWWEjmJC6dzV_JF5jwUXHO0vElBkg-VEawn-IE5yE9Rfnssk_J0IzEtBhP31bRmsVg1-wobtd53N09XSCe3Zl-43PVkK8Ee4q-ODB3omZCwVGWO4AAuWJ14eUzburItyya75Qdgds3bK0uVtgAPzDPMiiZpFqNlMihVQa54-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cXlHZW_V3pXwZI2P_V4YhVa3hz2kfJ2gr8nuNsxsTs2MqND6Ku4OtF92mPm3V3OJ-dOWv3S6GF3JXJjo5sHopBrv739QJU9O0EyDllG99rbslfKeJwVtL72EI2FAheYEnTNnLajudVXw-NOyS4d4GfJ_0Ylh0-_TwrM2gnfeNV5YmW0W23TKMsMGW59EVo9ecRGLXNX1omodwO_6f1z1gZTWsPC4bJ4fqpi-F4B5tHLuVZUOdvqIOTjd_Ey3sBPDNjeLuYDts9HqgE1V8CQDqpkWPAF-Rclm-qFhJqbdz3KD7SlVRNXPQLPf3v53wIlOmkmuvo3ffjFlZdMVCv_gNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0_eo5KP2fhhITSX_J683DKrN_pAiw3ZE_oBcOe8u2Ds8tpuw5KnnseIQT31tcYwPjyLCokja-2KuhCOQ1uC4tzBbPuUQsle6C2cTKine-KyVScvRb0Crv8U8I9qmr8I32Fq4vvzCT-v-3BgOeA7jSfniLzvxCxVwPEiedj0rA3UfyzL-W0CPfMpjScPRVOWEHpEBXy-n86Y4kCJi8iqvLSgHNhPsvHfWITIrIEF1avITgof_2-70UrtQT3kglBBcDh1h3ekInSYyHoR47f9irm4T_J3iwalJAbSJSoaYDX9S8ED9q2cLuR2dLriexq4yTPUl1odVvXLfpbmcMsIBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXjne8P5UWCK3I6kuqf2wF0CifuNysh7bDQbiXLe7ZZsc6RH9rdOPyZqc_yrHJeN7Q37FpZCpUAaRqoL1QyDRdZbytw-niMR9rcnHcuosScapjbE88l_ylw_dNWMKlIvSunTViy1uXM4AeZui5KxUb2GsK8-XYjm9aqoYzVjXTJcFWRsfPzkJyA7VHCpFGDVPWbG7FrS22tEzuf8quKrixUSMNYn7pn6tgKyDTP2EXK78qIhC9R3-uu_p2qLTFnfkBgAc3pk_Q-NwwWi-lnRWlTuAX6zspCyiOihvISMh408Su7UM4fUSstrHepk9KUkcvIbclsasyvqzpnNBRDsAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bHZ58uyNTSCQIEmfTLVBRgIKT4Fj43EdDIUCR8mjjUqGkdjChAe39SNh-6tR46p-Bo6H_9gy8PUT5xHQIFHna9zKMr9xqXK5gSbYIVN4sjJv_30KKhfyk5QOBDNj8ROoB3EiUvWop2ryBGTx-G7r9QuGfepdOWC4-rmDcH3Z7AzErk-5gi0Ofuu_21qKCUdeulEMYh2fwolOGys2jxAVCc-Xmbgcjf0IA7b1sQgCVAMdamjPImd3XzdtiozUOJkNoUkwBF4npy5kz6wy-jYTvHAI2ouFsFn9Ix8BQKTCvz7bJFr_aHXixhLEbVIOiZHgbqaKtGhVAaVDH1pLbkda_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/egHSdXYm6uNsLnmF0RvN34NCpZtDzqrVhVhdmAKWBW_eAJPiKks5j0-WGjU-qiYzoU0J33TjBUcs22LITxUK3HMed33794UIhpBSh3PGvlljEiI_rFVkAGjJXTBB3jFGV2raDIcUISNkAa7DW1BWvxvCsJ7FfjNL8f6eB_x8tH46fqkeiQl2o5Q99lJurOu64h-SP2F_GPnQIfmhUwK5NUch5R-QLqOAqsz2SbU5OV7x4bxJZjEuEDHWWEc_YcVMw_IhbLJVLb1TnNu7qFqWBtoPTYFu5XFolkd8ocZtT-pfyJTNCKYCFw11P4MvteIYEoIowZEaM42DFBWKmFlbjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5Jj2clQsFY7ulfRdsXaQY6M8HgcEi4FIpQuCNBDLHqX7VSblgNbZmcKQBuwQNOJkj04JMOgG2gc7kqgxows5VUu0pC0RCKotwccs0LqwsdluixmvScY3FW3BPlEPulWO4ZAhs4t2HJ7qE4LZt9mjpVBE3A6JNPgNsJA8s_g5Sv2J_c4E1Bm5kav8hMG40J2kkw1903Epm8UJXP5SSwEZN8534lBwHBt4acr9vgu-UgKnP23qUPGLSRo3Wt4IEENGt5fMBtkNhSEARJ48UWK-xFIx9WKC7jw8Roq3MOe4Q9k_JUKmtSFL5UYbVr8zfTD_tKKaZAilbc9h4Jfc9o39A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PUgMFntUCMQ_onc_rm9Y-JT3z7vYQDgUkVyVjnHwZsaW1zOnjfIL-QvicbRiTab_Vu5-mqO-NckmMazxnZ1KAZfgt1lW7aRjZwBDSfmOg9hWv3OtVB-MlQSLr-RmUH8yYJJnjRyr7Esi3Fl0_hmSzxJOWjAPwrzojpQNLiU3kk4WqpTiZX2M9bFXLBRxvLG2MVO9V1vUmzCVNBWvd1ZDK4-LU8p9ZjPNrQcoV9vZ9zcdOssvBJxvDq4T8hRLz5U-dl97QJeqLJaYePGab7dYnw6q9riNrOamGOJ7UFlANA7SznGhobijAx6AlKx-F0mdt-z2m7a85GywuDwuoPn9aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJwIBg4IeWpk-QixVqqqHuBWyqV_Q0ZGG8NamR8X_zPMZAEY4WEOy6y2K2KzSQ-u46nSslqFjO0frMcrp1SKlW2srdSJXG77b5MmLl6qgGd1UhRtg2cPy3tjMfMRewZn6l7TPwqkA5m08yZ_e91dAqwwXGmpgXl_foyjoIIasyP6eue9ULAmAlAKcenn7j80GSGnkuWBmLIeoShmWcbZDKjy5e5rmojwUvPr5kxDVVt_AFJIHJnb9vPyWzSGwF9aAMejG-3Ysu9I7KO8aDv36NXUbz3dfV4pjbmwXiLp5C8JSUkZECir8GXWdSenpCp_FGieomrO8qDaJEIC2Nqqwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlPTVIvGbeHgOiENb9nzkc6Ymw6F7puAtwG37GMVeTyamIusUD4S6RTylHCKmoEtr29J9xx5A8Op7XIvnagYtHBTse6phY0rurW6hPMv0CuR9kBqlgFCZi3cChu0P4TvXxuggReo0mVGhY28YWZxihLFpqgpzJ51WMezUF6s1PzuJHmGrz38cuASJ2ftQptBPnK5GJnsFQ7Ucbu9Vn1LgdLAYf34PYkNDcUtMSHtPn7xrKVIaokp7761IqF9fCssfRmaVD9TguBQ8RZJXB3dLsbthD5XwTqsyup5d79qNtXjYXrAFswacQPMoF9KMR8HV7IuGmhks1SMrfCPCn3yAw.jpg" alt="photo" loading="lazy"/></div>
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
