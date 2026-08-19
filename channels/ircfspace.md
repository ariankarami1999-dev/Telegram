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
<img src="https://cdn1.telesco.pe/file/Zj75hZsM9qdSGlD6wNLAQm1wk-modvFBuDcYup59YSXya6X1ifyF_K4wng0CaSWkUwJTEgmKt5xcbHmSfykU8NQMnSmcSBU-fnmFQRKESJ7uX8UQ_NZsLW1yVq5D1smBJPD3LkvuBe8ST0SBk9YFzpUAE883ZTPOAkthE_AZ4yrvd0ntL6fFoBrH1Z1m1yBS8BOMcrzzXH0IcNBZc_bRiL5pIvfhMUVnaEwyk3CRNY0tN5gcPf2de0h0T7jzUaYOQNwI6zWsRDLCjMhVDNFCHqxLsqKMWiBXdmo5_L9cqUUeAPZ-Vm9GE0Z3SIUgAaYCTYgllcQlB3axVby5IEek-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 23:46:37</div>
<hr>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wix0sTNzLb6hz0VzyuURiySoNOKCWdSOrXVL_yKyhmoyFMJQmSkP1pH6SB536TLqe9bfXZhkLC9qlIsmsJfykJEB5UUXmtGRGtg9rhPfv6VjBHACZ2RfvLg339qh8Y5mX7GqtjPmAriW9MbUk7rkdnN2tIGnzFdDA8gFsgXwe8bpXYyQfEJsoXC6cyKnZHs4L7K50fYct_r0lg1RbIHmTFUMqx2HE3ilKcbHeYGzbEmUp1K6dGLw6HfuXIDf-QHaFZVkSfMWw9-cLCHOC3wSohDsTJ-me6gQGsfgvfIF3YdfCoQ6fPjeTfSVoaMuj6edvjNXNJ2HU9zhYJqv5bWSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RneUGqfNvhslQ8dRbhZRZtpfCCmmtmALt171Ge82jVaAmquqCVZfpNR8oG22vIHhrdpT75raO2hOJVgCgkGiN47ygYcxrRZvnCmAeP49NHVi9TqPxArmFV5MirmqXuMGyhOvvfeJrSfsScVgWOxv-y5ZfBJWYxtqzZQC56O1IFN2fyvzUnt568MGhi21sklVDv6vizscLx2pYsWFNYK3FoFYcnKTS5Kupqr6IeKuxXHVWaqwPm1R-cWA55fdsQCvM8s2CPGDX4JbWluesZVzWHvexZUHu48R7zSIb1cgG3qCyMTvpknrwg7RoXPZZT1qA2G6K1VtVrdF4N2N1DtzOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4F9-AHuZL2dFXUlbnM-r-xP8HGS9uQOIYtxChvLm1TNYPReJOHfr2pLQaKIsZ-_kve0-CXJe2OX5PlTBy6FXCk8eKxZagO-VYX46kEyNkuAuw64AOaeO2FixzMb1TjbIh8Sdaev8xavlZ37yaeaKY7chYNGIgU6yPHlOQx09TQrnxU8UrdlJ79otkWf3VJj4iJyLBy_byGSTfkwXiGVO2MPU14txTK0Bhoqu-EhB479JelFGCUvU0mqyUynuwWK1yi3GWEqzct_jhB9RskvHX-nBzNuZmIN59oOTi_nQILWIeyb9SJ3aTSsef9lPrHKSYazwnq3TO91PBjNRTtdMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=fCPk_rcrZjfBKyZM3PuY5kNvD5suGAdD46pjP6P0sVkFpQxxETwNVjELX9aLxa3rBBnYTr20TfS3vqK3LBEQFHzmVV1FqbIEhInoI5gZE0blOxPh5D17dAdlLxd71eReLKipqaNKf7UhfyPglnHUVVuoXpssVqoqEUf6oSTdHeMFj2rMyWgMo4PzbiJ5Y4GsVH9dPBH-kslSehw12UwgV2U-U7zzuIkLxDBzHrF2qTACH6M9ulGWb0ErAXMDvzk4PUY6nrxUNhFd8OM2VxBGz7_vepOiBdLZPfI2nq7R1LcIpw1HXSKEw7G0Uhfbo-8q5UOp1lCt1qIP_sKUlGsSmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=fCPk_rcrZjfBKyZM3PuY5kNvD5suGAdD46pjP6P0sVkFpQxxETwNVjELX9aLxa3rBBnYTr20TfS3vqK3LBEQFHzmVV1FqbIEhInoI5gZE0blOxPh5D17dAdlLxd71eReLKipqaNKf7UhfyPglnHUVVuoXpssVqoqEUf6oSTdHeMFj2rMyWgMo4PzbiJ5Y4GsVH9dPBH-kslSehw12UwgV2U-U7zzuIkLxDBzHrF2qTACH6M9ulGWb0ErAXMDvzk4PUY6nrxUNhFd8OM2VxBGz7_vepOiBdLZPfI2nq7R1LcIpw1HXSKEw7G0Uhfbo-8q5UOp1lCt1qIP_sKUlGsSmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M2jgVoesUGGbOaoloQrBeKIHdIRdMbD9D4RpqxvuTUjdpBAsjQ25rwVpRFtwC-HEzJIYwDMw1TsIfGPddQfq5pp89-xCXMOlX47pY9ZFTuMAhTYoufm6UuxePxKKhDz1MLJJjdtUaW_u6ryaPNxieIXZe0-96_u63o4uzZKlOv65hPKU-iFcdxjFMeuphXgWgDW72c02ymyw6q8ZaNOgACSg_o_Kzrt5JKNnrMJkhoJhpD3I5TKjPGhMaVULKnOmE2mTeM3zZTB06J9X3a81uVz4l8nvY_THOD0SMyJJTSg_7vW3sQ99FemaLtm3J7szyH-u9SDjZsDuTHq1uMX2yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUyztjaQgiKOUKE4CwiBR-4i1HDgKekbok4hfON_ZsOG1ZSZDQR9i9zOVimruZhDFbuVRYvW9YI3pf-oqnazAb3w139cBRC9ev2eCRAj7kgT7vOWm6PAtvZmpEbLNj__gLIx76uvkaG5Umbhg_22OkHcEXGXhGg6Tnf4nLc0ax32j1YNFgjQdd9Y84IH4oxnLU5yTmTbqi7XUwpbnV4WUQ4j4SuClZ_qaGgqeHq-jtF3hyuXVvj7_vEPSVzxbgiaQB_c-SSWDj_1IhtmUgbMvRKRsHuuEEPJiJmx2QGmf-_SaqDAb_3KAxlriuF6tzjxfWqnY5qm1LAoFXVWrxOtFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bK_nQuw_KDUxKmjGfCPamrRfAOKaeaE9P_s-fK1b9iNpCAnHRRdvBMkd6Um8DvtcsKNY6iH-br0oij7dgoZOzu6Og_s2m1ZBvaAeDMOVkwKMt6rkrNdn5gdObu-CGtTlJBB_06jJP7uory3_epXgO8cWi5L024s46ufFxEJyFhH5TmAWkQC78VyfvTLP0_aJINvzpo-Bcc-tjCVgm0lKaJQ43XNFYvyk7w-IyqpRGHmG2Y7fawx_Dgk3NoxW2a3h_dt2tydO-7PVGKyZoQzLi1JM0KyCG5Coj3_Y1VHbXLVkEph2qUtcCHz0xElvAh9jY3Qz9CAx7nps5E3GNzT-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CbHU3lLIHKnHKuuv_aSkdbS5qk-pJSz2pbbyDFcxT1x9gmVlP-dPVd0HuDNHtF7thGRaaTFjYjOK3WFudFsIzxOTMWv_WTdEaBAbOvYZgJzx3pPu16RlXvQXUkH2lLVvLXWxc-ZJrarGngWk6qGpR2J1DoIOhSMEgYsAlB36UQ7DNM2uYSwYObJis__N3eOxhskKgPvBKD2C0bxI3oJU181lSHVDH-0sYtoUr3kIBoEgm2Muj6mSpqs0DtwCUAlVOQrP4FCyrC-ITrifcIfPeQbah_uUX9TrW6F4rTKlXmrXC01ZGAc2BXpFsWIJrZhi15QzxsEJseHxXVMn5DwtVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhcp_kUHiXu29YvoT-FBAUdOyAvReHdi6odkX4gmVG66NS5Ve-qiQdW1fI1iYNnAgutyUCLCZ7xxIvUOcTImoI5hemuUg5ywfOH0Nr2jy6BP95a7BfMgJeeYXWkiE39NINQOvSMD1DRp6lMzXIxY_q4FIONcZaktTPrsRI3kJ2NjBDyGfImMjLyD4L9xVrj4PiDp7I8po0JqgIzVS8EVwq88vINy4hIMds7PeUmq3H93wgYz9atpHATvjmxbodVWO95wrvl-0DJOnTe2fnZVH0juz2Z7psBcISR85_d8padDGYrxamiigr3WmWuZ0zvdW8TKf7RbRwJuz1K_jDp9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vVsPf4tSdW1Hd6xaeHqBK1x1MwoT3G4fpj6l-kQMHB_SfrdavJ4NHFcK9uvhFwnbFTQgvtiuQJtPIZIU5cGucflMwtlrKngbMFboEeGrlAqQpkgsLzMuYeWnht5WhsYEWgBPlO_mwYednrDcjLwW6nFO0q96e6ZoUFeuBctgRTiyfP91OM08IUYYivQv-VRIDWsZhf2pHpcCpQ_VAne1sPCnCC-uwPppY5wGlJOybec_NXgp_SOlihFFfH_bH2NV4AZ6KChrD34jYTi4icB_7W24BK0mONeLD-VyicD1svQH5HDEYZ6rOljXAb17Udy0bPqWKubN-qxq1ydtVjFMUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WewonLnZXrULvZwSxw3xiIUf-aZaEM_6rISImzOre9M2JowRDzYuT5QgiNPZGkDaHdHlT_HhFQb-XGCfke1xBTwD7NmQ7E0VjPs3C5wnQVGVW3NnCgi5pfO7oI1hwb07Nxk-5jopF9j7V8DlXd9GPaQtObd19c2Y2YsL_71F00YcigVCTG6eUdjo9bZWwvYIRx9HxmYZuTuFeadJUN-fW2YCpgRCIYJaF6yDTpYSrpQkplEM4DKaU1R74GQHtv_9l9SQBLL_G152rV0DAs64nrV-2FZXUK8ZhCsrWdns-o67egflAi98fkPhzwcctp7cUE2VE3jB0nY4pz05uU3XTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vhcl4pvQdylFlOFRxoMEYi9MV-PVG6auwkCcAHLILNwm0h8cbT51j7UIHVYz_vq7c4gobeieFZJRRYsGK6zO5vGOvbNx0pPcPB2aD2a0l2HR_LBoecvaVUwxqWYIOp9M8XyWZRUKwPHcO1xIJEyyQnJQ8RbbdWaJMzFTL95uADkBReZYWk8NcKLmOyuvhBr7-_IW01JS9SXBHpAU2rI-SeOgrK1RuyEJkRxMn192JeO1hPqWz8n1zlQHDsBozbJEiTxunVbNmf48RLvUf3w9l2h1Yzhk3e1AXbOA4eneiddIHYdg_OdnXA-EFr8vW_Bp408W0U2AoeVDp_3IOEIoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I1YHUxdwUbJnyoEaLT47dVvlvTDPDgCapj4aCm0dWZYzwGQTJRmH5O-fQ74EOjIIaKkzoDh5WEyvs6si6rq6MwwtfJu8e_z2iJnpJF_2pb-mdq3thLjJAwam6CrFyDLVbALCJ8yEs6R_n8ZACXjCtMWuk-YBCoekp-vsfaw-d2PCvD2xLxL9paNg0LN7GT7liprAGQTEUv1y5Us6WWP11B48t4_lR456KYvJk3dqeMFVp2eA70z0ocrMMKmAbQgI_dAc9FYzB0dyKQeaLnsIx8vnB-FKsQJsTPrDUZlRqBrkKqnlWOrsa93usIhrJslFMjVc2MF9x27B__aznEf8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vPVK4t8O7KBBisH-ZKRjud2AbxlUJzS1CUO9ZVsm2zYY-jo5FXHDrKFREc5PCSCi3yEUQEgwTDR8dIJmV9jD5KTGuoFMABi7Zwzma4JFD2KOIMWPSqfhBRkMOmL020D2GmC5_U4HkA_sV8A4-wFLslQSdQlwJpkzASokuPAhjEvgHK4eZu2chri0n679A6m9T8FlKc2JEUbuhkxJ3WzBqRQWhmw5ev21DuhjtOEyF2SX2G3CXH_wtroUXPvWUUNk-TnTpDhSE_OtZ9lOAwH2dHLdZVibHrvWxAu6usabiIYiv3Nn2suyN4pdKis59gNw_v3ekpLiJrScIy6SdEHbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_DUxpNvvNJSxms-UZBUnNzLDAgSzy1IHg6B6qeu8Qwi9YfOAU8XSC8ZKBnRKbLmN-zbyA2y-O2rDoZ0H7ugpM8JxTQTRFiQc-tE37qnnc8a38S-in2AJkf4MfhPNHocRdU1-7VnKj28cb-YEcrIdwTNCCOhC5iFHEoRyW9N2BS1H_126sP3gMRzabBPP0VCmp5oMhxABVClPXEID55CZfCA1bnn3ZJfAKus2BVmpRRlhiCMgmM8qdKbXFUpW_ClntwW4JSz0dRJqj3JNW1jBj2KYO9f5nVrgiPHVtqsZ-fnOfXUuq40RGRKucK2JWP_gLZkuYHvlduxkjzwsrM5iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v7kplXLxDxxMJsR6ZdeZYjfLZN0tu81IHSzKEkMWE4_B9matyMRr1j6ahgoLA4Bbf9n_BNsKXwrEIygpxbo8XrcxoQcc9GUsiRejeOWmVoQkKs_oDgWxOkO1xuEdoYuoEFtaVl-8Y082emghtZZLk8lRjAGp_moHF577RpwJyPLx1MSmMsU0GBoF7hFrXDDUUJ-d5IB7CTjbA6UZqbNTtVcXXgsMFA7mXCu9I8teVEjE8MjjvlcNbf7KBTvsvH3hivPaHD4Kn4Ul7EH7OS0SLdiSJ-P9uNlq40WXpd4LG0yInDM6Sgt-47EN0vehD3pdzx9ADi_TbzQEqIu5usJG1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vex04h8kgPFrUP0z3BgY4kZuMHN0MzRpDklF9dIKOyoVC9Be2evh4W6gHbQoDmpxDQVeLROWwp61Z5tp3bOigc6nXd6OGHK0uZ7A5Zl_GY919xGFRI74Xnezm_UjFu9j74EzOWD2cUg0IC96NPM1Gd6z4zFxVP_az684bbwXA-oe6p30avgRrL8q4BAEemWjTm7OvhgC0dc7mWi3lDBeSgiaShAD5r6Yz6J8dNi-2ZHEcyzNLhx2qKIs5Pwysl-RgM0WnkfJ3MKAsqcNtJwzQCI3pzhwPGZtEClftNTfaH4i1zBKSiieXeStlV1RuKmCtYkono1tYKds35azo2lWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ty_4Bjo75GYSANLssH7RCISOUCmMOF1Ccq3TeS8LJEnL2RalCyTrUJLwoxmPCrqu8uiUlF1JBlASYEUlaqTy_Yx-f-g5ZVx6UACOMKcPQw3Di270GefmQQw7K9JN29iK5mcZdayrHZ1Yx1s1EbuidH-bCucGFEIoILQCIXuyVdJjH-_6f8Cgh5NP_ZaP_S4nHuvAwyUSvJI0q1L_CugQPYOwH_TTCAjLxjcA6oFYr5mwtnuoRyuVGAybJ9d6Yhh7WQpqssxjNZlqGKtpZvlOGRkn2c385llacnbD3TBDQrQ3mFUkMiDX_pMLHjsaUfxn_fnHofye88O9k8CqAjPI2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sqdjPQra62PwVsrZVeOy1LiX6nX2DIoewBPBchARe3SDAyOILzhw9QqUq4eoQjcXbI6rvbraqOSs-zeocd2fRJPtyHPX4Pe5XhHiYWi6leUuaMOs6UZrXPFaXGmbryusekJrka_BdNOaSpcXRk8LOBHj805M5PU6RDJgcMBCMuPA-GT6-dmNsLXLO5IuihlxrjVd-RLTfIXnfkGriy6psOKwxh-fpHuI6o1hpXYfkM8VzA0kGYV1fatfiINzJ9pQ0BA9FOHvFLROJy-cC7HBeA5BpqIDU6AcwcAbKmqbEcMkC6uTv-7teOZzb6C86uibzNYiLRXWQuE6gthPpkz8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2TbLLsK5DE_wexG_iiz1R9Fn6B4wNuxcy1sGhfI6kbELItXB4uxhLLaULZyKiboPtJgacuDtnLCBasFjGb8gqOhfMC9YWwMNs1JhQVgQS8IwvFSweLRrb4zq9s8WetXFaO5IN9rUuX256jBtLZxQZi5xc_Q7VuceOQhJi5g8vRGUyQpVkl8xfcF0X4Q78v0J2Xy_rRo8khEYz97nggoGHcox8lirkezX222p2U50Flq-zAz80E2yRK4u16PJamNahENfJQchgnk7omP20L0TBHoOs-r3ZgkCHETvtvVxLuWUJjq9HwqrVJdCkhh5KNxBzWt1sVNF3uMSo0FYCeXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/deX9Sv9mxJr6nx6revMICk5vTeA9N1osjCo2xTBmT9lnacdYzj0LtKV8Q5SuOfZPFVLBiBWUn6IJ-qbv4-PNryjOv7N4LgYuD4lhlvK-0BBQCRbEjEUN_afhScYuADFmoJnN6zMeEwT2lqZ8PRbyY-bB5fOVO3qYuYV-_obgMWA6ROzQnqWdO8g1fODLzG9xjB5gRQBLtjnxJPrHC-V5IK-XmMd3ar6Q7RZgM9WFWYdo7W17fq8otgzCbFcPmMRY_r48_RH0goOBOuDIr1FzFx9zdyDIleKA7E6h3BkK_iSQZrYCjTZbCHEibd7qXRvuOeVAnW_kzvfUblyvwhx2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hkxaraf_9c1znhRwxty9GXdwFMlmlE2CDsRiE1DLztgi1gJ4NH_nRhvgQChDG5qjW2SDzDfA027u6p4p3kgSCK0lnlV12BCuBTRcpyqTDnfe_nvKk2lKEE-inSw8IXDgba0WQ8gVqvzHC-8_cQDiTpk2K52OSrkJ7Vj9s5TxSOHYyctgTWACi0HqxcCsCmnCSDz9wHcaiKdmQQidHWUV9_sES8j7LETN9cn09yWZVxE2dXO7LgkUR9eMsjECuWfVKmlYKs2NH9FjtmCa-Qsz0WPdv7YW3Lr4jwdee_isVWGzdKd-OtDhVIwAdCV-PiTtAasLWESRrBYtNQ6rmzHV8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tGhKwrNfgXxepiu6prcK33sumDF0T__FoCSqlwIuYKaa0Kjc-tS_5Wmsyde0_iR49k0CBCSS_WQXcCcyOC-xuXyDJ2jySCprihqqQVNLoI8GdSTXgqZ9tI-40WdOz4NCngOOkoVtIWXRIT7ciEgT9_tLy0Xpfl6mnU2oXd8omXST_2dy_cZA0Yj0uK2E6_D30Vny-lqGbJur0IDY-QQuCsO075pnZJ3V-J89R2ACTIpmjmWU1EuVpitmjdZb5UiWX_Uoweq7qgJ9Z5nAt6MyYk-R6x1vLHk1twPh5zsp0mmvosiDgRlpvsULq_r_u-h92R0GBtwywb5_WSa48RhPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvjpByAUr5WqjI_3xfuIwBBJkXFXG43WqkUm8VVUprZJqojABUuQhuTaF0mFXK-tRssQW30w8Dxe_t2MAfqBmBwByAtqo4qjuDmXigRGIya4I563_BKZBDhyTWus_y9pzTaXOAFLE_LYPzokttFtUevYYNFZeEj4YwxzPIUJ-MnyA1eX9wNaMJw78fKLDE6AxYB_RTLikVca6dKmzJb4_iE3XVCuyHneIrzQ8GtDONfI5wfbaS9tRA4XsEGR6cNJZ6SlOdHNUMq2yAUoY2917D0hCPrn145SCEFIqu9PGzZQZ0foWFKnrwGFUv8s1MsViZkTJHLjMHRTEDInBq6CKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sKS2Ffm0G3Q0Wl8o7tPXrqmKfWzbM-x4KttyasjAxxQAzPEPMRVOz3UCllHgZj84N__tYWe1LgeOfaQ6wARfpJHsIo5VocEG8TxhaR6fBpP9AFbm2iYVReEWBS-CkvZTX3jcIPLF28Z772m9JU6-k1A_80gDfzq4BrPQvvKogrF2Tlc4UdKzkYeVy2CClQa5Ozbz-gc3pGtACbp8dFy0oUjQwDJilLfnZb4MHCQbqxCrVU0G74nX2KdCxLxJIPcvGB8QrDv6F2Lj4NQMW_JCQB5v7BPEdmAnuBMD46nOJL3pwwZVzrm_aW1RFIeq8BIJ3qjT_76ft48rPw2QlQOgag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mmdzeOBcSWak1yY6EN4lz6WKQ1x3_UhW_Jx1AXbNxA_yDMDL8Cq35mIqAruyq7LFY-P9m-daGFXuKJAh3V-zW4fxJ65wL4REo07BRoOboVeRA_oEDlN2ucqQF1kgwwCP7yDHMccK-uvA15oagjzbT4HEsmeDBpI6d9AYC3VW_Qvq3Axa68vnrgyVnL8-8s8u6YH37lBKwOePv9eUVW9c1kFUOijTcFCsUp2Z08axIbrZv6dG7suW85kKcJfOQF022largL2wwXTx79nzLPyyDaifI7LUGKT9mMqDIuPu3K5OIQVuKGR807QhuSj4QPNuC7DyLhhJNU-kAZeD5qiLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K-W8H37ndZen-PucAjQP014zF-2cWdVnH1USM8VEnCmP_8TgCvC-lAiLnlPduQL767mbG44kSFNKuSJsG1hKY5L7uWwcPROFzE_rsy2cPraRpfklEIRvCPk-LWjPfJDx1FDcblC9RHif5h2kbb9xhKR9YCAIrTT_rGqx1uOW47XyyRtZGW1erEpZRfxQNUg7UhpYjrYjb-wjp_clxnCv7CuCB9oBOQp5Q1DEVriiU0_jTBTgswnzeKb6ub1HxRdgTpVg-Uf9hytI4vS85M1qcOqgEejGteLrWX1pv1B3kiBJ-rN0uXrIn8SXeYVdj_t8j9jcQPultgrQAjtaksFV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iaNRuYKNG_A-lkrqoGkQ72IYHEQY2spATDo4vj9QG4Owc853QgL2n44sD55Xy_WQzo4GCe4lYeYbXinMPO8MJZpCvHoEhFw86BOXvs5tsJO6c8aRQeito3Q2BLPpOejsZoxLebO_SKtlUYWy9dbZV8CK945MgB4_D8WGgLlFuavjWwoes6ziX1ajENl-4IkbDpQyBLV7lgYWW_Sy1B9OmDxELfzSUASneJ_e7SyZNP_9gBoY8ls04zmgz-BWs1A7YDffUNGtgUGXL49ZhYxnQzVlI39sqeFgvsTakjnGeVZi4cZOQWD_bLQwFHcDigo-DWsiYF1Wc2ZkbY_EUwWLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l5SarACOca0v1PATWWsda4KR38RWuG4AfhBzZ7tuekUxazzLcWlUdfqCp7L1KDz0Kv6OQPyXA6FYrIQUa8DtGohOIt62LZdCOS46rTDXDKFODKVdRc8wtrcyX9_qKN3CmctaKYam8pYLFxvS4qInwm4ZnwSkSyKx1O1SbMCjvunGrD_HjFWXVb7J8uzdIqt0oQKtApYLpNHEVNBmULSvbHZAbI6hWYtU6c3YycHf3LeKApRH0oE4r6KpNL5kv81q1uLviPBLQxUBkfXnVILdFhupp3Beyh3JZKb5oJWnPm0r793ibvBvuuTX6ciI8rsPsogArW1ur3aV01Y4Z5mjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/toJIOZKzAwwjo_nl-H8oRpWuTDIUT8rSd9fNi7FrFIjrMN7IPijZnosjvw0TLc8u0hz0vEUMEg48QPuzG7i7eyqZGegoEwe2vzxCHL4IxtpGlJC4bxmx74naz2YtxCWn4oraSfzqc7BagC3mNNp4J7VIp3cIMIACE6MR4a_vKKKxKmapT_A958I-0PNH3BGWKQs3bWMr2wFtyWV9AJtiFKk7R_wDMs0srTOzP7czXLfAuVHRThm-Wdis5n62qnmfr7IdICS710A_fSqmjNCq4KSXW0NGMKiJ8ka7uachJ0MQ6LeoLj2qu43qhjBoz5UOEQXtQoXaHOHJz-H6WIKcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ClVJV734VrcGlpHA4Kp0a70vNCfTz5nG107tS_jv9REVp5WfEELB379x-XzlWbpZSWBO3Kcmv6BxX1OeWs-nfg2hd_MRF79esAKJtmji0K702RxBn3ADRX5dxZrhTZUZVLDcWXleUvFF5ICQT7NgCzKrQYjuTk7AHgVRh-fIAQ5wgRF2Sl1a9DQQwPkkj8_238fdy1bxKZGujP9bev6wsFylgrN_8BeDZ0jbeP5Jy0pjrr2dKGe39ICNTXsNAf6q9gaGxjqLHAnWQJ4Ub7hRPyNV6w6vheB1_iSvHs0Zvol1kHqGPjfVGktsQznxNR-NtBLGA9sb9m45t4L8CDS45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/atS0ke4As4KDXf38Dq_KGDTsCyJybk4MH-r2BRUzKIHUw_yQHuAhuVPdYkFOHAUf4HTLGqgLBYjSl2hxifLJW5UjvaYI4o1NdLWsT5_2cASAcWI8-5O11jK80nb7XylOptl7dlwaABX4VNkPaadUTWxDbi9vx9MgxkYCnFyht9MtAkrXm17uGthyBjIGzGl7SuRj-5IquJWJ4hrmQsIg1-_kSmLRtbWiw4Wo1RFEMlJTLUcDgBv-9rIoW7GQKFXCvegSZr7sfbPNmHKROsPXCiQ6oC7m9rUye2tBV-zQ48Z8XrKsi7lJClWC5T2XRJR3Vulx03Zk9E8a7shVdDaS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F20Xi29KzRO2Q63Vl7HHKoOa6r3K0u4K2e9335sfXmx5nDZhynB9fpZh2rRe5-vay0JV_gH4Zfpq4yNa0_8AO00sAAgu6WDSk4g5S26Xsem8colemUnPvKA8TTQa6UsnvqWVpzKhbwEjtPC996ezDUo68j08HgUz9nzfev5Xum1XpR_sHwrdqs822DHKsnDUiT3hS5YwyTlxaW0CCCPORl1UW_prHvpG3yPflOFnGpHfUSV5z3fxd-73fgehq85kaBjDf8a9m0_sX88YrRwlWxEhP4l0WzUA1-YLxZ7ZJMqLp2z_kNORXt8VsQB48BMz9nyeQvyzfohk8oMAT6Amfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DeKTyEjcZ2jlQMBthrA5KsjutpOrhZdF9zTlmA-p-eqtmGRH-tAQotYwrKem50dJQeUTFzLGqVL8Hozz6DsUg7PrmmIk2TQt3TjL7ZkaUUyzef8hGLymxtb3mApqAMEq7yOcNNfaC002GcuNDHRKLT961Wv3QyOBcbKSHTJZ0THvYRWYGF4qu0o7ehchQwIiEXLfs63S-dxrmBj4NB49LYm-T8iipsqQplsRY50Iqw49dlcfbVATRdP4y5BvkJX5nb7Eqj8eQzSExqptVWfU9YyhGdQ5tW5zm9vdkw_X-OAzCowNkEmh0RJ-jrB7XqetTugV_Uk4dOXgJwu2u_gXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cgbj5J4OjRdDIBiW3SMgLU9dpPZSUEj2LiysrmX5k8U15ve1pNm7HhLQ-vef1qLZ2uE8rtnsnLf_y0Ozn1lnK2Jb-1kBSTe5sTtd9-KGFlMBvcBySEWr3WGrk3LRkxzm9pRZ_PMNGHmuyegMO-81r2Us_j128bngQTOeF_BUvF3BIWN9pzTZegr7wGhFFLrIrW-YUw_bQY6kesZXuG4B4X-f-gkU6u8NRQ-XR4zF0q9BjZfrOboUuyzYxez9bDgk_2K7DAtXAHz1J33_r1WlWVz2T5gA1ljsUye400o4qEi9qa0FRymQb-ipnnlZMeJtXtg1KnBvq8Eqr9lfEmUWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bgijJtU4qve_CE8rt3rBKPv9OM3zM9gUu1aZqkP7XxciKFwBg8wgQWaFP5gKD50krzQBlDoRcokuFzUXq4qyawkobqW3bw47BEGYwd_K63xNTXx65nvmYW4nwE7gMzlLT77LasIoAbZag-gFl-r32WRKdItKW4YRunaL4_Aix-ZxELFG4QTbWFg4bZQ6oV7NUeVK-ADnJyhJSb3LSonIuHWh8yP0F53yjuHd93TpxuJChDRrrwXkjc4baboZjztLPzYd-iIx7RcyDoDoFbRg-iiq2OM7yPEMxWxjIo2slh0lJOGkmHAkWfjCZtWOaMhR-lh8nBectNb4EXZ6WGY9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pXrkju1web2d-kWzELGbI6aFMyL2C9m53bpUGYoczVYkyef-RYljeylCaHZ1emcyKtSzcKG9WXvFQMLzPEbX6aOOUzEqdELiZlT7YSpsYUcH0v4JiTaEhBacU0ZiNvoRfNPDZoksCnY2W1apIRy0up-9K934rNSJR2LjAxcl5S9gw11sUue59MMUvsiqZsSz1ZHdYa_B5l_fjvWP9PuJvVw4g2Z9yNb3ZEnYI_Or2KPRwbviU481L3iEZO6h1bSGxhxrn-gTgZL3988_P8_BtI8EHdo8wtqaUOo8pZua5_h8daPEVM-_uQiTCD1dIEEj00k3JSqmimTSO4hC2ooKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4WHqNp1_MQhWht21JDTo-oAuLwL3DcPGEqJo8n1igPzcnpTYV5XF2qvClJ-odsktiozmTMOrC0vGVzQgCviRYEZ0wWsXZ0290MHinTcC03QAnMTY3jZrtWMlpWAqDykbVCNg7zBIzsMhSr86-LFZIupjhmnpHKAFLDiEaA1kloPVvuwBB538TrVXKpB0HtS5E19SO6WDj_lXVXDu8cmpo0NPeZVJc71YigNEL_LaxBsZD-BLLlSWcwIMBqxZ8AQseJkP86DoyfavXo7Vz5jBVKUxFfXVFgKu1VmHXeCO6QjpBVxUeOzUnA9oennVFxYNEwBpRz1RCQPiFSaZN4mGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cb8vh2fcStNcNy2qQmTvo3KRGAW6uwyK_GmrZhbZT8P9L3DoNp3UzxrcVThjUploTw02IbpVNwSlpPSYI6hrwk8naVXSv3kfcip_xeXnA8QFk2Mv7WYKu1E2W8wGYTzPARahNzoRsrJDqNne_RczFftB7gxtpp69jKotkYJ0X7KMX4gbcqeSasohBuz7KjKNyzw4Mm2wcHFeoCrLqNGFVq03nHBpFpXvaIBNchuwC9v5WOwgJGJ7WLyW1TqvqciUjuPqdTvOcQNsJGTDJKFN7GDljJJ_0XtY_rvzBZiNfhCl2yroAQfMdnp3-CWVJIeiT2ug_DoDGpgVzj6bZHxrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lAMgYMxe3K4Bk6pa6Gaw0sdlD8ROc-fq1Cp1IS2BPsVUpQW97hoXmqhTBwXJF9GHY0xSxL1eAhGOnWTmcD9iEldePHl801_oE-0ns0cQweaTi5LOyT49_NbDKBVi_YW09H8eEusU0-FpO5UmHTLsNeEDj-YtmG2Kmyfyqdc6FS2_yvAQtQbOOgbhjkdMmxlEfHnG2wNuHK8ppDNopGT8FV6bOuedYWxcUT-0KRqUh8TCO7NebhfCpD42yhorqWXXe2A6B49QSeVTWdNYePMOnAwQYhW3yNFqX06OQxZs3ibkt6rAemjSM_zSgFjc5LgneFVPz0esi5gqOrsNCjfwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KeNNZtE4oXJkh7qy9gq7H-ghV-X_5BurWJY_Z3sKSG6jwr10kIAQ5ppAuDFt3VCIQj0pb2f9ciSMRsVOPFo-_pCw7s5P1eTZqk8iv0AqswgL_XSlOvAVlXv8NSaNVL1P5JwAHBUuPjwDnFZPGDc4ZJp4LkQBu-NzPINJucTZzpazgfCfvmSX6LJE95xJ07bg3e0hgMvigoqn2DDW9MZMMEGBSSN7vD3su0619ww4zCTetp5aKX62_K1NLwzDHlKuPnxhw_dOJscJjCXrD6wRTw-I0QUh5lSXle6Uf06QS3rZ5zYDe5SvRtqcZ7ua-65DibYnMUysmxFRZS7QSWSlVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UXd3PMZbKVgRVQGD2VEpMs500EeL7FDqD9sqzSlao0cjBxv3SuEf0vXg6U7TlpBEF1oNw7MxgzL8a12Qqa3Yf3ttIVq5Qe0uZaddmOP_DvvneiYKZu4f5m0Tw8r-CpQD8cYqwoqDcrTVB3h_pnvy5BY6Ay6yCI8ut3i6odcVuCZi_swyAyr1l4utb6M-s7betfltoF0rjRMwKx_xpsbTpdncR62SDfXVIEGVJ3j7g2d4wNIAPm_K3i38eE0AELUBzt7dGNrltvzqbMAreQGLiMnwPNaN3vexIF6tFdgdmew2shViGNUA1ZjwUzfAYympAkNyKwWV9Ow7mDPsg3Wc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cu191cYCKI0ipm1EqbMpLG3v_rJDSpwv5ecU770NZOMm0pSHuIOKIruNmXI1AlXyZjkKUrQRRcjdDzTCC3YKzXYMRcTA426DGa-wbgNlEiu8t7FiwAQWKfSP_lfqhM_C1NbwnGdqj2AGM56p2ghOL_d82DCLFHxakGYuD1_FvleasZkmYLTLdyEpm7TE-tCTM3Wes3te_mkc1ewI7qZ3sBGYGsJwN88Uma_L9D-hn4oPV-PEkqgdBJcdaIdB_kijOMxPNlDvdaQOvXx-SDrB601miC_4-n7vE1c_Sgrip3AW6quU6ESikthzEdysCmcWMooFrYV-_A2AAVCgnFkaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YA90mVQMmP0_MJkg0Lvk22lLPWw6o8M93hFz7YyWJpF9KHscXo3veN2R8qBTrFaeGjBhX7h8wcv0SJMHxa2CVD42RX0iSjiBexLt9rd2mBZPQuSF5ftlpGoGf0HZaW8sICID23XQYOyDxADCt_hZ9aht8AMtiw2zP0P-CW40vMzOLR6EFfTJPG7Vkl-EvR4hiLNwbCkkGQAG-S0pMEzz5jwKIaiP33V6edoFEHVvSUp1wv_PuCWeStfiABvMkc6beVI7wTlLvUMB-OZvxfZvb9YgD1JeOgoFoEao9jjsXFnd8WZxW1gIApHriGXgV-XnoicbxiwL-lHD3VTrT2Npcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ntQOwjHGxAf6RqrhDEGaVrp7rbPCHR_X8-I_SWWIoDlPF3Z5xwGqMxCTXYWjVhemmwbuKB7M2XdCjb55DtoslIp6JkTnOg5K9mztf4aEMjjjxT93oYShcTYtByQLtVi3IIRa4KWbQMQI61dbiBBuUFMB9lt4iLMmUGz1AnpOHZhXqrIrPXFHNzqQSQXFXtADwJczBUqML-vHVnWSDjdJmgJFjY6pO0dYC89MhrRXlVZdNkge_lDjgmDMpSBurtqN-k-0tC6UQTSE4oAGdonO1F7eAUjwXaeevuTMJnyJygnvscpM5HYQ6j_G3fVCvDnIyF3wW-adp4gvG17k9qWjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d83MQIRyJWP4svss18ey5bFdMK0yY82dK-iwuGbahs0g6fIAfs4wuGq23F83o3XtBMkfPvucwqUnRBI74aIAJrd4qmWaak96EU9LPF3kTss-Th7TKhgGddHB708S1PTvEfsdGdxgw_PEfx_qs4XVWh44O-Uo6CP53URXXWVehXrbOtWbycQVQPW4p-JulAaLzgG29_sOuqDUYoYJtahSCmXrMqXmiYMvqRd_jPWnwgX1PY4iHNXFv-Eezp6pt8q8nqO7q6p3dxdKv6_wdGwNWA1O89hHV7w6nI7QMJ9jnj39vnaz6eBiUijH-BWmUVqTIUZ8q0iM_6alElcakPfFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YNp9ewwEh4CrRyYcvAeoqvBVcvsq2EkKio-do4ufBrpja_X4APnMQi5YeC2Or40dgYm_jUUCP2j3rZDK00ZppAoWv6ortowNIaAtCqGhC9oX3cEwGVMFtHHctlMr2ahflajxd5T4Cbokkq0NfkOjVXz8WtEB-k5LZHyk5xUoeGLzVCerPRX5OM3Wt-jJ17H46XzosIQYVBmTR0mNJvznvfFs-JbabKFYnTu7WQxPXEFEbpNhhUxz0DnzueDdNiqfPYC-16CtFPZM7mU02QBtNBwxUbOKr8v-37QAuzkOuAhGtiW9FKPp0WzGB_eByst3nY73ycMBJFddFpOnBMKaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/axAY8Ds5rL5PXpTIeUVE6nEYa7wj32CDCJKtkosxErEraiTT9s-YYrhYq-SH47u9ZQet9fP2Zi5USI98GtLM_SKJHvaqeh1GrFILxDZtGKU48YuPFz9If4JYSzw5B1LCxJMp8Cg1qlLGnUc4gFEEOSHRkTTBC_T46HCkeWEFkvc0A7dwP0tumL4R2UIe1VhUzBnsHwXSn9VGymQpmOP5tbnVZ2J-kXG-DUEbiVsmfi3EXJDB5mHzbWLcmycZhj0K58zBtnks6IvYaiqfGvBtfyJJoblKQ6pFSxh_wahx43RWRGsxyWEQvZA9A_H4sBZnDu-Eb-dBlA-oKRdE86aZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ki4qPh-p0my9eRoMjJQEl3wbShlRzgokym34a6H9B4pQ2uh70S40VIlacEIz2SN4VY8hp8IH6fORdRm9OWybBZ4FhXknpyKP6zhBlv434i4WkjHzEhEjd87YfQ8G9o-WTmXQhkaQ28JU_9lOShZ6ubq5XsK_T65apYWAgSRiKPl32Yo2BmVibiR1itxv7BFOZ5c2KT_peUHc8bH7tgJA5j1xFF2mPN_WttTbsbgXjaZvJdNpN0QB8Sl5AtUNqc8w2_DagPL-mgBztzuuX_eVX9yjClAakfAhXePe_melgYbSi4u72i820QR6Y4rPXLperIJaCQrbNPgXYqkUG94twA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WoJQUlRMcR5MrpCfsABNysRSLf4OZLiw78-VnAAJ2rYVzi2sYlOdH-jihsl7ed40G_RItefCpciYqzdVzFRTtJnlwBmqrKJdGJoYuTfYhBd6IofXgl-5i4bTG5PTI5nbbzdbSwuN7yJYHncfQmdEzRtz6thctc1Uibbai1DYgMqM_eXUaf7YZFSroV7g-E3esL4XwOibi8pW6uUhQuwC3ap2VeK15zZ96nNJkWRJvkuJl6hoglBW95P0HCNlMDBIwTRObGKDXZoaAVZ7ZN5WANM-WJFNVwkApslkVC3gbI_FILl9Osev855zvpudebwK5IKoRqIThaNu6GuXp1bqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ot3eD5o9R_zZQEH063uZFBSe99RMwD6znRuQGVCcCw_5VScjS60nKlSU1CfFIX7zBKFDdypjYwhoTUNQC3GXqG0GtziHKRBUVsdWESZdCzRYisdNBbvRLwDK4_Bc2_AySXeiep_SZyHGR4ogkGbJ74w7Ym523eRss_xKH4o91HB5BgRC4WrKdOi5LLiAzSR0xhlgXgO_3CBrIIZEEZ5Fi-kmIpRnPWEAjbcWschq1V-hRuF6DaM3WEZqqlsfZAUqFM2ADM6edtgc-jv--QY-ZHwcxAJkMXte27AxlxItT9cAKaT_7InsDGnkPH0gvizwI8rYhX_aT9omy55bOAjcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDhkdj90h_M0iGs4BpTTRwwafuBoJEOhmm2Esg4Cho-ICH9wVhVTJ8fhv-CwC1f38akLzowZl_r_etix32jL0kXarle-YzkCFPc1xeubLTkajbuK4ysJDQeVOx67-BZwYRuFBVkxyokYEvqPaHcF42kTN34cHDqsjWtb4HGcPKPSyI8ntC1yqXyrjpadmxwqTRxesvvx3MxpDbrdwNlwmscGBLtN9TPOlVUQ_mtRCJUiQeQt-ltpGVYt5wrx6PGYGvjMUa89U50tIXlRExV8fNASqa_OkS6vM0LVkJ5avUZ-yEQuL3KeSXKGsoKWOElYw3hi0WEmRJ5LqRHb3H8TJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ru2-_R4U-gJBEl_D8yXmIA9VZTl1xCJwlq5lBtkK31U33Tln6m4bTjkFnatQzt09Q7NtKsIffBqxJgCg4Jt_W96W_UAqDp8C04tPoZpBwr2ecXmbwGMXXthXys_GW00VelBHIEF7-FNlZtwDiLtk_He8JEf7OdJV0qtR0JieK1oZ00cVP6REbvMdSCFfwGzxicz8M2B0tzzqf7DLY6uLApYKjEQu3RrA57eHwBslVTZj9V_Bcj-CCcmNGjDxU24npaFgL0aKd2Tba407teUtav36jqiKIIFobnQq4U9mlroOj2-t-1j14bBXl7pjg4ERQYggs3K6IIM10JAzCjwqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s98zo3rGL_XRgl3Tqgo1bhhuDQ-_Rnr8AxaHNH9L3TK7Otu940ElLnGLWVKw9GSgoJPm8GQLc5zexhOkUWoZxflzI61NZAMfpk2KglUpBjlK0LHOMG5fCZNXHQLpaAf-vjmHMWhrkIyg7BKAoOfpR31Y2X5Btop2bU8tM0Mafx_PRtqOTp6ZjEcZ_JLvaDDJRVrhuN8PcfL_n2AnG7_w2AvmnPPPgwQHm82o_wKI71A6LdLNKK9rUrGitunvukpocs35OIp-twHfhQ728dBSQ7v6FxA-SeUkhmF60wxMFyc8j5nKHc8WR-63Usp2O-hL3ooIHU-9szl0AgPgTvQuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DwjYM7Pv_6cMeT-CLEg3FKqCQ2VUyCWxbMoUANZlDV8dhdHN3pt66t1xNHtT9x9VcCXKE9LeIzmYWKClKiO5yoQ9y8KwDyd-eyt4AJDzV44Nk90klsE7qMgTc4ZI614v5iOyIdxJRpXV1wFgW8EG8T3oWdMzqfTzfqro_WkXLcTSYecub65bhqlQ1tjLn-TNDpYzFNW4bfFPlAdLgnC7FRdtzVHoFzYklSSL_vsSnYD7brKDQRvwX9zDjWWy54cm_UpEtfFCm3L16Z4U3SEISIY-_0kkg8Qfdsavpj5aNQzaY56ja5YXuJB-c_DKD7V9f2tWLL-Ts_pBrHWlm7lVUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRxRGbGLR_w9yE3Oq91G3m3vReke6jrOEwQr5KnrL8y8U1iOuDgVWV9g0tMRjBFE0ZouZvXXZW1Hqol1OGTe6q9VHUEl7UZZ9J-N_sip1LVD6-pG1koV25v3goD8motaCW6aIIF70eaGz6-vPawWn6S0y6s4d16f9sSJRDEr9OqN_3MCv30Tka__TIN8qCupnY11tK54UJhieOwH7VBx2m0BiLAdgs2BTtl3Q-nWqNS2qcHkMHeczXqRdQ0mh-Fz93oi7fY8bw9c-qe9B_7W-SqhjNQZUgx_wsl6PNG94ur_tY3avknpdCE-E_0BASY_I-azrB_IH54bWUZc-AgbNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fiIvG4d9dHXcjTln8B-NMZ84MaqE_bO2f3_JaZ9p5kxFsafgBypSTABIV0TQzWc4Ex6zpXWnt8Sgw_qEJK9aWha3Rz1EfHrXTVTqaO2plSSLbP4bzNu2Zhl0lD2ky0aBnuTrJKpt4H0aAxd-su2J6mkgQUWDPs3qbcVYM_Xkx6-VGZPFYqeuceYb21lXtJK1Cepg68iXX2KKV1dHwZXJ9xFJxmHktCEuCBsEwfJrADSpR1eU5k35AQgYe6XwwKaOWX8meLi5WdSTkzDBugZaT7aON4z1aplLEpziFDUs0_Tap9gePNXtdKnpMB5yv-PZHI5cuc3nIpXnKdLyo0PL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ageSrnmXjVLSN685uShYzSoSz54jTQKJP6zOM1eSpIv-DHhQmm_gDPUTZgW0bGwHwH7lC-ls15qRNarME3TEgmx7sqt_J-YqzQhuP_S0DlYXbF-SG-r_OJkpHd5U6DXHSweWFuG7DjqA30CLVeJ7zFOPCxFRzKh5D4t5A9L6QEa-G9IyxgaCiFgHg3Ah0zulxXl1Kt8niFePrvPTNkY98L95lFOIwEEWlYH9ogOILx2YjKXXEdPBaUJwOSrsxRioLuahCCnZxTS8g6J4BxTGL4R7Bdlg10xIcFgJ9Q6exLdmfr7sH0sVh_0w5ayTEZWFBQGFFfBrN1VipHwSn9qsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/THgZoGZ1I0U-6laczgrb68wxgoo4xgLi6bRy-It_KRIjxMmppkkUzQMaXLkPH9_Sawg6pDz4noL6L0QXjv0CgXad8K-rWC58OtB7O2LsTdck3kNJxtQ_dzYU1Y_HHfS31FPiMaZhYV6eIO5yv2Av8Jir-rFqgvNeOriR8lcCKA5O9hcRYni7kFTkNxCedUyZWm1PCPEJhiGD2xjLJc6G-8x6DwcO8VUURKj_tq7CrLgOuRs97NsnX1aenAHfstPVWLqK08HneEWVAAe7YchSA0HMS-BiWpf3g1RkVdIO6Mt1g_eS6YMFqUjlR-zfU-Q9CiYuh8yRtH9eZlV29Hhb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vIQuHSaaKD0bd700Y8Ag0HgjIe6FYgXTT1_lDIDZ92_HIpsOmvyk_yvyBnLuyDOrcE-sGJefIhLJsyibZ1-agj3nXZMzgkeEhvdvj-HClCadjX6JarhyzQlwvYB8J54o8LA4XEUE17h0MhqAiGOCWKrUdV4XECeUHdDN2oAz-UTowhWznNREuPDW0WJyHOO4C_XD1siO3kQfyAf9iXzLA4a6zEpOiySZK8zh2yNANGgKDyLcrSsTzNMDPSonmBp22fFCD2K6Fz834H8zlqXIrdSDK3tMAJxcRBrDn80GvS_Yi265lyS1eWAGOSmWFDarMQ7QsR7nx8-i460tyTF7jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4k3gK1ezNSJY5z66oItMIY8ar5tHIGlblyXzT_rDYw_xHdWhWrAL5d4kohZsUwKDnxNQAyzUl5sQ07zqiPRTC3RDdzxaljhkpYpHJFI64xJWap1AKXRdWY6OwjyPEt-cL6-30pNMjHs9yZYb6LjJ5mCWDP6ppp6gdJFBrU4zNfwGGEeDOfcNoAvhkEXKOxEWI_rej1kt3W89iHVJ1rBSpU-vc4YsVAM3V_g43qJL_FHuMCT3rMAuLqsePYWfUVDifrchpvlt9dmwT7jluNQsZ6xiLnQ71-Uf05kt5T0LFYaRljzjygSVIKZAKakQmzsEffU30X1nxziqjOEfNnEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4wZkVmBL8O0MicHZy-fs_Q75du0YSzVKkfXUlT3-o1C3bLcy2ang8Cn5GgbfE1c7FtlD1GoLxeQrmGDQxoPDEeINcv8WM-jK-yD6KcIFnLYlMptGf4oAm4vWea3y8Kbeev-AY0oAcKUPmnJ6a7cRSOa6fQ_l-vfB-xlxOcy2ElMg-DPEGtpNj3-0xe1YIMfCttHM0qTijU0RFAtTeyFZeWTNP5BCpHZUkxlFApvA-TxtCv-YPUxkJ54CQyrM-APJVIjMVlLK18CVIWtuKhNd4VHqRQC2FKhz4LE-IxYxOpBC5Xr2L6EzHbAgm5qBMWpuT-zshJzmGsu0ZIDLUw95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pKZviHwDIQa1xRRNw4ZS9AvtVQbRL0of1t4QZAt5v4q_d59DRqtlWmUafakiFmG92UbnRbi0tDOPNNFcFCsRYtbX19f1-KUfrAT4XCtFVn0GYnuLXYKIczxslWwHU7dk-t5_J550-D9vVU-0SwjU8ztf0DVIg4T9wIjQfRhfRRkuNiayTDE9z4fZaMSeNqHZoRXdem_aOmFVz6jpv_pJ4yILS-GpvEysrzUcv9bDhmZKRLRAEXn6lxemqyTyMQpb_3BGspgkK2OBnJXu8tLgsLgWCsd-hLo46qfqyGKotmxKT7HKoMnOSLi04RxGsGvXD7p0bjorK-dK2S2fiizTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rLLu41VAj9v1KKcoMD1fb1mb-a8PR5b6Ady51lmqOh9r1F5k_L2qpPy2cPfC5Px57AV2OZ9SAt7bJqjxhd5VWoTgZ0UBvevJdFiZaTxj8XZ8GrxCI5NDXzStIuuRVaem3T6zPvQ_bi4RnwKzhnKCoSY6urill9F5DqlTedn4h5s1hIUVufZXPS5JuVq9s-6QCRnoP4tufBv6A45AWMWsaBMwVZaa35asGIsDOnwOZUBMVyhSpGRMhY6FDka7c6ijuLEIDbzPVFu1qH_adiXKe0XrfwaWnXkT1yelBom9F4fBvFfr_Rbt088_O-wzrD1yGyeMfUBQ-RatpwA71A3qWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JraIsX7xiv3cv3v_ftRw6jJFFIZThYZA79d49v-RRJ66xtmC2dEwYaDy3jukFj0Shcw-wnEH_Wt2p_L4w6Je9vvRn9Ds8W08yeerhmI4RdrGO2FHrzTCMPtaBo0ynZE89WGKro8KTEgxlTXLBg0LlucSUwnsUWULVgBB7ow3Ct3R0zk0FXb-4oxwimwEAIUHAURjefsrrR_wAYQrfaFw6a5wZO4aa3mAScLXLqi_AEiITV6GK8W0airr3QHNc23LZSczeX1dt4qowdPi6NvBQTa5zZ-U6S8a8dLqOBg0HBhXy9ViZL8RxC3qDXl06fw9ocrLu6ANuvk5KA0DIBhCqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CGyKBwWIRi6YlJ9mZ8_GAoeQnw3TNthoymuLROFkqNy1hzJ0ErHRVRF-Bljmv9ERWjsR43wP8KYSmqH6xT3gsJFTN2nngZjnDZjOHjR66LXSGq0UJ0oGYk7UGhYpS-lbV9WKKv2THLVXchTvGacBTxvt77U0WTv6_EjhcG4B5UsOd5-8uIxeDJVVS16mNjM3SK0yJvgLW1-lTxQ9I1muPejWd5-SKa5a9dRskKH4kCt09Klm-2PlO94A00s8DSKZoYLOvXBQMZl9xmWbfxxmOPs6OGQNpa3ZNDHDDIo0R4GWT7nCWSCM-0Yp9e_zseWfdRDhrn1aIwEkMH6WO54ckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1i8oS8byciI69Oe9dCe9Sv1bVtsvKc9Xzq9UL2QSRkQopeqL2lVLXJD7fW-BxNuFs4mjTzVlqjkIq3G6iG7FWKsuQr_Xqzdsti0mwbRZxdrtwD1Egxv6uIA_mMd-MkjjKNdNYMP_CbLAWmjVSJL5uCb0IyKZrPhivTGtllNBtLd57H9FvxK7tR6ngQKRjotEk6SVdCts1bcG6WOHKtdvGfxfsidhxm7UQ0PNB1mSoQ51vW3X5X0mBLDUt5HpZZsquYowEhx55Khl440nge4VlZZdc2uHIljdPnraxIDT1R8XAf7gtTntSmX4HWJUmHo_02RfIRol4HPFKZUiEyuag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jA-okaJjG4QYksSHjMOx2oQLxnmR_Q2rL2aLZZgeEE9My6xtxK3Nnvbw_uKNs3Mg89ngaf60BGJ4hwJh-IIx8hqdBvLAI4E62RewxMdkXUCudy3IoP_X8LynrrZrRYhCV3h-yY1YfHZjlgqtrLrin8PNoA-pfErDRNORZUaRnRoM6BRO9F9uHkqIhNa20sMsbQ_E_m-eQT9z8yTlihEmx-xUncCOFjhFnzNVvDNRS3qI9ifyxM5FXmar_8e28ECESNNoFpFrFGOeu7qAscBG8Ieudf8P8-gDFu_e0SWBKox5C6nM602JjWNiZdhwlMeH0-2uY3Zq3U0jrL0QWy3Gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E8ta163ILjGLb5JxD-kAZhNq_t7QbeimkGSiTHaXk292aCZAFpzAF5KRkBf8rhxd6N4rg7kWLrabco2zr2Q1L7a4spGmaGi6ESs_tXrx2iasvU7VAjp-Ly6hwgiNdDTceVN-5qsP4OnW37V-N_InjDvhB9J-1D1xuk_l5i_r-f16QY3TfO9EWqLjVsm4IUAL_xJC4c82aGj9k6PSejhCgcfCjgTDXKMx529q6rrcDzQXyueP1FTlLgqJtHHLeNP5C_8oj0DItp4URBpzbL6WzzTIq5jskzKX7aQsEnn4Z3knlJl9KcCNZP77esRwtmh6B89bAFT2Qq5DX_pr9SGIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
