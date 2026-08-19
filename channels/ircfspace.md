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
<img src="https://cdn1.telesco.pe/file/Jizyjotfg15flbP6B-Q_pPwhi0ZYOk-LasTBd9G7D8-9roaJpIJtfwYM6xJRqtn6_4Io-hedttthD8FFxWv-rwaKHvwQuW9Y7gO0kIMTqVFHEUzaxG5A9gZP8hluhbagzxS2il1SP81yUf7_FvQg4nFDMxhG_4fAqxMlTwq_PIA9Ex3UBOX5RhLNUC4KRhD_581Gdqy20HhjZrl2v9_RvkapRUOHCc2dH_LeXt4p0gkwYAOS7soKR-U716Xsx1_nxf21Rrh4IiqvkZ3uurzBsxTi-zj3uVeJ3NgcsWgUeBxTF2t1aATtXcUXbpPMTv_ScegXodaymJbVHoLoYMureQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 06:52:56</div>
<hr>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DwDnl-AS_FJH3ZTG1cmSFOXbNisHFue_aD8el8u_hT-bAAjpD0X_QKi9egh319Lsa1BOVZ7z3oP5i7QAsXeNmlRWiDGhUNH59ExFaoNekm3VPx0C9dgxenwTMoMl9zH-xjAVD5iVk9mBao4nTUeNsu6mOPYbss5yRzqKUJ8IcLVLLBLg_feW-6dU6UNO3zdFPOuABCOq1mE4hzt6Q0jjGs2pVetN3r0hDiBiiFKB4Wz0_gwva46TPJJ2GLsOS8NTAVXjv5UitdANKkdZBbvwUV_sXn0HuQkntsCR7XtZWv8RV1mA0QZz_edXDXaIZXMaizGp1D1BgeYVfAWMzDAekw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a_SK4nm6rNTxJ9i0dR8_i6bn8ieSgueXTVnIYowKSTFYriVgdmfheds755LL6VeNbqcWTLEJAV4qugNr9yHBg86EXreVUK_IU1v9xbB0So5PTs_-I1ZMGLuI0fNc_iowDmRYZN6dJZomvbIPOvauvegZV4NpEMEejf7CnbQ33ZJtNHasVzFWwqVgq9bL46OIVZx9YqiAB0yv5T-AMeh9hoJqP3ajpY2oYfHo13tdaRHVar0xL-SdyvrZoGiNhuC-dSnZ-1-4iw2TxUi3vD22FTVTG0REn3PmpTq2k9mmtqGHXs0ANQD2vUizlEFP_h9erhdDzOSBdMrc7bdnlY3KrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=d16oaHAyfnUevjShOHsUb7vCHv0XGxubh8nzGYzjXOgimB_h6DTrrT4OSEcPlKTK42OzcZTXw5slKBRZm0bb1eOXyjwaXx9rto8zj6XXjntXsWSNYXF1LD4I7dxaDLwbkxBTGg2uxxwDg1nVDdaHEoDPW48SWtB3Ap4X16tuiKON10Tdu3wDkKDuvgNzdsl-M1Hwig3UGKCFiYAy295DRbbGkATptt1izL7s9WR183Rwr136kz1C18SiQGLTAjnwzTMWQBAt_3dT7CSfRJSkSCMr61aU2YohJtDixWe-94CPUFPLDBgiwx2tA7oGFqdKvzUtuU1yfU4LkJhoR0pnIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=d16oaHAyfnUevjShOHsUb7vCHv0XGxubh8nzGYzjXOgimB_h6DTrrT4OSEcPlKTK42OzcZTXw5slKBRZm0bb1eOXyjwaXx9rto8zj6XXjntXsWSNYXF1LD4I7dxaDLwbkxBTGg2uxxwDg1nVDdaHEoDPW48SWtB3Ap4X16tuiKON10Tdu3wDkKDuvgNzdsl-M1Hwig3UGKCFiYAy295DRbbGkATptt1izL7s9WR183Rwr136kz1C18SiQGLTAjnwzTMWQBAt_3dT7CSfRJSkSCMr61aU2YohJtDixWe-94CPUFPLDBgiwx2tA7oGFqdKvzUtuU1yfU4LkJhoR0pnIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AYPiGl7FcO1kp0_mASeKh3BPUmJ1BHNjawdZ-Q3pztx2PCvnhKxyrAf8askQrnpHkigMZw0IbH-i19e5tSq7bkwq2SYCJ6z_NOnCFg7S4JU0YV1cOWc0_Fr0lDarWL3r8A3OifKby8V4v7nJcflw9oWqwTwblyG4e-IyIpzaQHW3hX-WfuJ4y8aC5ZRobHuS3yCKKkGUc1XJmexQ0e4Nb-Nqm8jeTuYa_kviVnQKykjjDxH1nLd2D4h6VT9TUaX-Be8rMDhF7HqoNo7b9ghGZvtIG83gsVsjvZiNJXpBxx1i1Rq_BF5f541ux6c0J1DeTXAqlQ1LC6aZxBwRiuEyfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d7mmoz1wgGHbewaWJDopBSvhCBJW4E-luHlW3m5A4EI3pN2mfT08uZePHBwQadf1fbOfSYzV-x8ixaXGaNCVNm3-k4cA0ZRP9F8BKF0fqVSAZ1aza4Ywk0PMZ8Hzpwe_ix_pBL776_hoG_x59AloS_WnrcmDFvugXgQ_eHdX7rQku6ppWKK2bd_L3rvFq9Tx55dVwlaaYnEftfq6orqWSxVMJ8FXMZKxNrmE3pARSnxvtrmY8i8a3VFhYOaLgkvGcS2CIKd_i0KYdWZmXWSY0-LoUsq-cSY_AmrU_HpSazWWIcGCbGay2afYjdfilfNMiQsOlYgh9MLxyHS1_eHOKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nLMlHJmN3ByQbc7eyULgUopD8iaLjzJjrY7v9sVmaJbDfEKxG8kMXBMBvlwkOtqBDgi9uVH9hUWLEqqzw9W6J6-_WLqiz_yqkugWEtxNPB1WtsKKDphiOYGX9wY6r_qjAJBnLwCfQ59_B7b9ZjoZkNOxeyFHltqed75Mdbx-suWL8Y5RXtuFcwOuXhuAhP_wl9Vq-lrB_t1mhr5TXyxtGCsE2-5CwRSzPrW4hrdfIVeCJ2i-8qu96UC3aq8SMCy5KpDLWs3hznZYpx1kJsSFNnryrfXAPxmlquDZtn64PUM1l07ESbTR6x-iEahH_ZdkarAIg46K8R9CbC4AlYckPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nukRibPcU5Bs1wJnuPduziQauNXBo2893mH2BAYbJYLtPf87PNgoVNsBF2LD_M1TSy6diQ6wls50EM-HgIZ-k8Z36Q7ayxhGcICPQZtogTVSUScN6Opk30BeGIQIUSVv-Drih5oom8VKQ-qiGpa5t158mUFWVjCA9vZURLPa5KMM5yH9IVQzQGi8pu4R3QO3JJTrsi4gklTfAopH_eG-NCXA6WeCkbwaHsJfc5P0eCutVcCglC0iYuGLy0YwBaC1wiMbyeb_owNNOj0EcLwBDFAjrAfRIQ1QqQq5Z50_sOVAdDiIm9VfyF7bo8dq9V5tGAKsRbjFMJJxHbKks49VyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i1ELSlpOW9aoqUtGjvxua-uzotrPQtrAKlvjxLH34WAsjP-VG2JXWt-jlCOKSz4NGvyJm_hv7RLzte7ndAqWSPqRoPHmVzFnm7IODFJlMRpA2IiVCQ5Z7dkE8y2kOAX0vvLJv7bHShacnp_ZJZxV6IxoX0Z-Zz6-G_ifX5n5LJIHhcMsLAYLKj2iaO3eD6UaLEm4kykkwF7JG4_N7kzuNBkxnaYNoBPZRLlw-bhuS-dH_fnRIiIkeUCgw5hP_uoZ9Z4mHMG_hrnk0ooYNImkjEJP2MIzrCs1dFz7qa7akC93lz5PICp6W2t1vSLL1YR-mmozRBwO9gqR880B5ktRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MAHDKaEUsB3Jk_ooCIjXvfFleehJEaqf5j6G50DEZpogQdr61SjuRgeGHhjsN7btT_cKT8LSvfbiCkqzSUvlWdVUwRTiXDArPjcZ8KQI0ZucL4peMOy3CiZJW0GsWtFk995A6_poJvNV3DycuLKbOf8hTVY9JpXDL7ktX0lnSTuzrDxu2Fxr5EjV6uQGaafrIqV4Hv_Ezt1_ARCfJaqR5YmeL2L1qzUhDNhnwXSgz8Da508jokurGm0IdAknji2jafcVPZvidwhqvBN_8J2ZLQq7DOmIDQTwtEJYUcT6VWkSR_x3idWJJXitrY1vQ-b4GMvxWb55PVlKE71VmEPQvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arq7a4JLDUz9YDD-lcP-2eoYxvfwLlMKWHSQqr2QLcShB4rs9a516llIxCheOIBxx2bMzcpSs-Xnu9IEiGJ8LsN0P4yQ1wkrOnGvPdvz9fxkda9ll-XhVvEn-oeh6r8ohUo4uw5Lr-vm165Ap8OLCMQvrfbsSM196TZpUMY_6Rr-ftmn7ALzGk439YFGkmCAC5yiX2jAOfD022uZaIg4bECaZuBaHNwABEs2-EVV3xPOSpUZSQbONaqTFsCE8m_dSKeBexyNINPF6YTPcrlwZ2BNmByjV4Fff-6amO1RvRTZcuc2KkPvenVfGpM2iwpNeOK3oH6Ep5ikPXc_bkODQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RqbKwAFEgrV7J2kaUJNUgjhAPADpT43px76n3SosOqEvSVlRrBzBHO6_9GkIwooigqkoPAbniaAWt9dwo7OeK4RN-V-NCLYLPGVyHAeuqAnwPF4APwChqOnEhGFbbo5nM6ED2ewRY-e9fj_gaIo-Yym0gBh6UfU4CPRu4NgVAP11xBMJR0UbUged2Vjb9uqP3eGeixksaX8bP7UF-iIsiopXgpAWlor3LGsczerVE9WZjtb19yG8auMjHkh8bmfX_K8LrKTacn2aQqJ04hF0xflfyl7Vn2WyjnwjYvQFpLX7BYnI4A1otOBKddndTSBquV4Qmo6IzFKh07VZPeAARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MSvRcVR0Um3Ssatq13EKyeezfXHXbW6ALzFWVedkttqAhYdVINPFwaHPOh2__TvC-bADmrY88lu_2ft3vxK0z3gxKVy2gUPXIOLQkR6L837bVXlG7o3ONe2P0MHMNEJhHJKONQg1ayglpDYgUgK3BXnhPbv0pygJZE5iaWFJTVb9PNt-hUEOqw6UK7-xpbTKlPCK3KFYWVcvfbvlS3CFJjcY4LIZilIcU1W3tTY1q1GmF8s58Bt0xPKuWjZhvGEZarVdPOVLmUVsDn2IVH9nhf9pH2D6o3incH6AQbe3Z8VDYHrBctecAOmc9-RP-GKpAmTf5tQUI7VwBR3cnfXaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ng0nsMTvfn4_XEvMayb5FB1mY_9hTPjL_XBqtu4MwwGH4DFoB5xTi3sFh7Bj8bR5WCwy8gD-1dfe4qw6lOrJYGo-AyVYTNHal-AyRwzpzp_IXhpm8hOIV3kO6GRjXT-fHii8iw9JPFRP9ejX9JBf8U_UCwbZpyOybkiTyLHiiUV3JjA4rgknTfLFxae6Dumi0Csd84mvo6G9b2bdn3xMJZ31z8TnTmbHYVhv2NtJlsTCJlxrVflzc8VO7j4O7iGCXu8Yx_vw7QOGC2Sexv3fAiGnyvlala0gQlfPWIK0BjZrfR4RPZ65mOLg7sTcfsnGuIYdE57bzEbvwIW-Loe3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dxr9qt7C1Vf_QRKc8_mMWNC_0kH0PhQgYS00zBs9ItjI8wOoWIJPw7G3qqBF0V8Vg1D9JmIin46TWlVlBo4PCZQb5Q6ulC1l5cyxnVYqGywBzYCj-XGcgmi_mnRYfnvgcKDjTUxz_Hr9ZWiJxMsQD91lxFgQzvzLZOda_W32O-itzVl0NOGQkK7OKP49Gk7rARRrvvtWF5feWrEN3RgljcGdlMSaVTWNjDQyndhGcKSoYQ_StRFIIt32UNi-Eifg3ReX1HxGVZ8T0tj-HBPFBv-kr7mygnDIXBMVOtxgxwfWg8pYnxjuo1bnXsyN9buNB5pXPqG-VJackGVmSqAP2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FsrX64mqbhKuYcaidkzei1S-4agUWCrMlQ-BFq465DaxUEDURaUt06iqJ_fumBo_9V0yTYxAwFrW3s-whtMeClPbwuQqjJPQDqk3KB21ezDAhiD20Yh-4j5_aaG43OFMiT_n-PvsIbXucdcxuvlAuH3U0rziljfsq7FcEaJwzLxl_n7P5Brrm-6GzyGnAASUANYnsH14IT6lTpu90Pzsb7_T0isvuwqVY9w_arB6tDY3x0P6DWT9f-9UgNl2bTEuaz6SgveiNoOSR2SPNRa26cHrH55bUd8F1Fo1nD3j8XH9qckHY-O5_3wKw3BFPKMZZRD38nWwH_OF-pjZ3U-gDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bvv8eCK3BpdrzPF3sWZSWVbQeNTH8CD6mtkziPpSL0jycPi6u8RRXleV0IsIGgBFSD4aMKXZfdaoutU2zMMAxAx2kLbzmaA34tEsIO6kB7PJzF6NNkJTfNcF5QR-60jQAQjnYNnPcB_WwXyP4VVMNmK0zYVHXiR8vWTfImKQBe96E8kSZcDu3NgvPTD92HQYSjTUfcfxbAsM0fMwjpjVuVPD8Vj_vdliTj-EBFmzTo0gpnDrNKHQs9IMmWrmijQ_YGYLRMpKOtE_QeEMkht2YeBKo0Z2NTxwIhocTfZnnrsAuF2Jvf_rLPuRXpooELPdfWpZ25vqKvIpLPwN-MYnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/enfhQSGlL9UGbjgMdrKQWxk4rQYwxzEfl_itagsTZcZLciJ05ysUOqmuczemWksjUTEItNeI6bsM9zoQJDjS-cjREgldc43f2JIaFnYWXqKuN_9ESCqywPCEK1Y6rG41ECKhiF0yPRF7T9FSwqRnW3cPc76FNP0b3kQFIeJgqDAqQp-8cVexzipAxyvqLrHPNKBRsuJZJO7jC4W-1-2TuYSeqoNTSxzk0P0MHJGL9wzFw67AYtpIATaixJIET67RoUHLPe6Y_Q_BncEnrBMPUGQGoN6G9NIt_h0XeZj4_LMfnrSalWzm7Vscobt3gC5YyxC97QA_M8Dv_QiWOjkO4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnRfRlzbikgBy7rBNm3R48G_dgIlMl6VQ3oYy3HojmJd2VG-M-N3AjEVdcXSoyBaARR1DRaE3iFu-gCiaSBSRvhywz_vzQgjefGLwIuV7B_eyB-C8fRiV-QkDiS43lTlm1kBNPbsVcPbnYFI8pxpUw5qqLp30yaEs17X71LvByTMUifPCVFRTziMtQEU1qh8hI1EAYCvuWjLcXO-MaerQLBbik5AFKeyDwIE4vXJfUNQedhSzL5aZArBTekB8BPXOV-ZzVNHE4gyzF3gL5DwShzXQYPy3I3_zxdW2UY6nU4rD0p70G_RutsARkqXj4WLWwrsOdouokcvjLTwtPbFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q8e3SNa2P3nyT1gEF9HxcElU2wuh8jmHC9V8hyGgerptFRQmdkey4rbMPCxahyQQKBPWHW8ud0bz2k_5vhCQ-y2yVF8cxxhMJZA5F9zixDlad0OkZ_3GWvXcGsUIBcaLeRMDmbPdWRJOo7aNj3EAeK_vfFDgJhbUOnMgbVpO9LrhPwWmD1QzLmltYTHCXZEFfdrIrM3W33q6kPH_lGp8wgYkBdFjG8EkeQLukNC5p2sQJxgUbfLN8jDOK-M4LjU7iC2e43I96NfZvocRJQUYBfrKPNft9PDHT6T6c6vbF7_P7EgIAV6B7K0QD5W0MwOdNTToaNbuSPc0U2096TEM5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KzUtFzIDPh1r2Aaiesz7BlNHuwh8KH2Xm4MzVwF2zxaiMEcboXEMbQ38C3ykULiQbc2YFqa92OjBBMgZw6wbd4YCE_jEmdA83v8fts35F5Ccf-BOIFNEu9t6KO_5Vv55ePMlB85Wop1e7ozcki5Y8IZAaqBXBLmJXznFAD0Uul80zezHp1JiA9T7U42YUynfe5xK9CDY0i49g1eCmjWmktmriapKfCHsnBlWjYtKeSDOsu5htW2DqMPAAKNLI9lEt1Pqp9k1qeb2IJTqwz9txYzyoK3t75hcxc4E2HnD48aEiK2SOIdd6TtXJhhHXpCHZt5kQ7C6l4gGcbQv5r67bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CV5rl-B2PAm2Rf-tKrTrh0UYzoD2lu7zZ2frz9GBkhF1RtuAbE60ZXPF6zpOQmPQ3R6HaLYntXjhb8_-mVi3-yjESAQkwV9GFdLoBG8ht4Y0kJ8p5FfIi6wzd1hd2Z4ogDf5rez8-94M9HLBA4PPuqP6R-gSIA6n1PgqA1smL3PomLr-BjlB7ixZkBykYNDhYO6N7tIe0BTSTeLlfRlkLhqRx5ExH7eokGdgE_mLTCT1wSzMaJ4G6Z88E54JCyHc_maPyy0wFISxn5BOs5Omo63eEn6rnZz7ovYpzeKBogOcHymJpX_jtz-lk5sTkvDpkOSB0yMvmPH9ZR_4Hw2vaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-PnlIT_SpRzd-Fp6F5F8mD7JVUSZ7_nBgJJSI0BsW4hSfhLFdBh_4xJNcwn3rTotH4P8j4JMQREYV9hY8i9zLc54TAfl2Nao3JDABE6IpGGdpOiyrj-PFXwHPnZJA7Su0eifmSkrGzPZWtF95gtG3x_MePWE0fq9P-1mWFvwHtygh3rjpGBsxyPfnGZ43s7if4Ptk77D3RJCfAKsB2vcheZc3TtCGmrKox7-bHZK4e0_CzlZIBfK0GwVv5ilJndvcU-DfFLaawBtkp01GdRnLlPAAll6uDno-ht_hkhZRjZSfVlY7zwocT9hfNoVRDopxja7RE_PAD5aRpLx23rkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C1V2tJYEWTgGe__O8bxbIOg3ErRis1HFTDdGSDCc3OK_TXjumdJ3BQ5KvFIG6fgMkZf8i-Z8bmOxWVyd0rbKUO-xUjxL9u_N94vKVdCh3gw3iIBE4E_cL4LDV_Bo1U8y6336uTbVQ58loKls5Kv9HnIqw_-vUp32A9pSkUaybh0WULQVAIJoVZfD82uWs9DE25Ouz3BVvxLJCEYQKxu0Ewjrth79xcfNzOzSX361Zw1O_Plsv92B2NSUlbgwibveCkVxy8ovWMMPzQhZZ0OS21yIL9wucHJxixEXUiLZhqpBjcqR1lVf2PxuXPm8tOiO2ZZ8pIqZoCdc2IA_mfiNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MPMrrqg30oJYOYaU9QgZmjqphXlAav3SPV1ntVHXgXGGwdBSr55YYa5E4qcR63t6ef0KMFbfFX47NsHnV6FRxAP3LZ9z0eQ6HDh7toaTNsAI-ep2s-29ilYKJ1ly-qHuO7zvyeyCveiZwI3bgOFnF1-igxYWmMoYS9Q1Tn0T2xxNhkxV7WNMopDlf54b1aUrnmfMo155kpbffKLf1s5v0mOgiG6jRxyanIien3-vX-TxFtKfANQTuioOMK3GRahSzjX8Xamrhttrq6RVOu4A-AdJ2amNAMhblXX5K3dQrH_cpDMrn1vMotxPMTVeQj62fD7Gck3cOHEm9nb1FgBLRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bbx1e9v8a4liFLbkosT41FNMKIqDfTEe-_2LprugaGR9v2RMEBXKPN5VDmTItMiFrmVGl5jNsqswnpfXAEO0A0ia38iEoSxBLwCYPgIRcgwxXSZxVSCYMBW0Dc8eCHR_fqrnRWXrwBpi3wXhfc-JZu07yRsltyoME6qd1Cd7UC550CRxSDcgXYH8eLnevZR3euvUf9iQUgmaWNAosp9z5L2WDJYvM8lOBVqKl2ceLpLlrPWACgs1Ct0drvV73a36FLkSRCYzT-XI5UCcefHN4Zm24xHoeHzXUDeR0y9gYsWn6aRRKOByfupHLVuHhM6tG8VSZHk9Og4LoTlGfVTknw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZSLXFyEOvT2dBu4pfGFpGHUHpQg0pK8AZd7Vm0DVD0aUbcVZHcUMZwVy4n-WPORsA5thO0IBiI2yT7ssCwk-bv2VfHfxMU_esg-YDkcg0_1HOXXFMVH4E4DYg049WHqwknu-DKWAMs55Mle-qutePEKm8T-GGFatrT62VOseCnae4zmlAYYdRTd2iKY9PYFH59mspowtKwoBkIz9Sp9-9BGqBzWlQNn805EkC4wX9197J8wkTEUB9lIPyvGm8TFu1zsHUbmorKbFrTyOz5XGOpHnqLjxqhRuGLCTfCMSDjPvVtvQn5ZBmt-dYjACkWrm7Fap_drQJ23ROKSMGC2Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EXuzp7_bPZDBfq9MAbQm70jviLGeGBL70ELPJDwFS0Cm6Brl9HgFchj32VoPSpw7_igCPEOsyrSdSs4xZGCYEuY5n3-5A4Ped0xV6-a3q3VWFWq5T-ASNupYm3TB29uFAWPMmyCWBJobhPwfEoDYdMfSx7Nef2nlvaNLrf_dmfm2kmzjK1Ay5WroE5MPPq34oz3NujrF9z6UzL3IrWUSS0Ni8EVehEIrK2SnJdxAZlTpYBv1aI4WsAMvkHVNnwyYh7tmsqL-BibAn_MhN4nDTUKJSgdCa4_1jp1wR3EnF2RnrKjNsT41DpF4NYEx_gmXMlCTINN3aP-m-dkH8sUxnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fhvj2F0P2Ys6z4C8ZptWl6mY5ImfgKW-oU_-tdINHjBoq-HM5yPDgMTMnu9QiWIkc_9y2remVn0QtvrhiYZz4r9oLvg6EL4a2ZniKCj3Gh_Ohjo-Mu-UPactfQnfiNFQ93JxnUF1r4TwkcMGZttCNsxgOhhcXFvgRP1A-FjGfpyjIMdFLw1teCEFly2UpCtH5ayiEqf6TO4phIYWaiFQh2lQTV3OgDwDvK_w_-aiR2eqC69BwYsmYlSdFjyBcmg9jlsbMLBsPtOgV4suAb-Ax9F4As3uATVAmxu49-z6_9E_XcWGz8nZ5La2oWle6Q2O89MtJ-m_8pBMY1PwkOIu3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YVYcamhOXxVBBlh24DIo1f1sEHADcO24-ivQYggHwfcK-_7vrCnrF2DNY98gqcOEkv8_vMOVkw4CqbYBEN9TniN7qElMNxDtuCAo0cZQ79z5WdoSnxGxYsw9RTFIeU3fMyjp4Ggwpc6ryoVXMMBO_k-XZ0xyE2sZ0rPkkO-P41QXM1SYgkjFisCrOMzzgxR_zBYVMCNEfKbD6fSYI8JUIIthSkz3NvLEH5yXyCI1d5L2Tt0LyJAlSR65gRvEwZtA5x3dVbNOOlboP0cJm5B88XSZXP9Ft86kG1-gm2PfblWI5hPQp6zfnQInf2oTtFs0vYmuKKhdpcW6Ajap9-FiOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7vSnF6CPmEkAC0QlptsEg4HXB1IMewkzAA9joLgBg4GE25DnxDlrav97_ecLB1hfPZcp0ZXzU6sl_QwYnQLxegqeiGhIcXW7JdIL26NLeofUiZLUNga4BFSTUvw4GDHfBW5VMSV2ZNDDu7bakfp6nAKkSSOxnmCGXmFJVIB1IyDXgD4gvNqBaPqfikBT9GovETC8Bd2P5xZEWx5zEG7ss7OoxwW_5fc-rkyI9xB75pknQx4mXathQKdOSmOlSmFLxRB0DynDpL8RCk9DJTFSomDk5IFbHlDRhY8H03Tg6YIuHi4WKKoe2QwEJByaoJlUCVZgeRAW5JXQDvMXYPNXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MLUpPDq4NOyiNrMpJ08QgLEpikxgZqp03LTfwbGht6cHZYmuaLHAmezrOJUbKgwrrJoi9iJrCTyPZUTn5RzjZKuGRubrJg4ZtD17mf3WzHmjgP1kpkCMFROLS2KOZcJia_dhUS8xDyQ4DpCa_wqZsnKg0t8BFyGaRrN6zkcFzMEkqE_sHgneNv05C-YoMMuCCFV821gyHe7MF_MbdnLPGUIjr1R4i3ksTGwHeAwXyXbU9zOudLVWQJxsdkJdfuKFrGqkls77dxewP_N4hZdO93AWHwft7aRsioHhF54jCY4ZSob03_TQgY0hzLxPXNDTkAVUmiR5nsqxzZ2NDvyD5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aN5SUqR11RhBXbA1AlPornv8Cq_AvhRSHL7kXI-aPGJEEmPufvXnZtX-rvpqx1qSaqmuq8ZcOEDc6DkZMncrhEYtBBTeZyIBkMIkhIhaXJk1_wDiHxSj02NOYLD2f1wAN6xil4zZQDqKImWrvf4jGpqh5XsmOi1AdIXM8kEhHKbIp15oBSRZJR9Z5XvhFV_-WsvQ8JwN0Ge1PW9B6kZrzp5S61JiA_KDaLTS7-MnVl35TE_yKI64E7hgB_aYWyKSCmiw7q48l_I7takJ9Vrt0BFymnO3An7XLyJFfqQaHW91lHLqd0-lvbxYvNDvwGj9j05C0zDp6zy_iP0fcV5qcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jX0Bx9iy9qAF0WqhAw4h_m1J1pCK6jHLsKdStEKuPi3Q07oa_4hF5NCGEccqssBWHHQ-ijoMzptk3VmB-C92lw5nrHOtjZ6sPrWKEoQD3kZQftvWUMwt5YBiDtRQ2weDYOW1gjKPJ7dixFW1ZbHdTUetB7CBGylolK0O5zZWlBbhfjDaISqqnV5tZoQAaDepXs4IN3r2RkGXn_C7jBtxk14IbFlaj-LqrUuaTc9XNT1laH5pWwe0cU4uwMq5faxB-S_Noy2jWTAT2NOiWWBAU-rECM2Vi-lqnQJwHEtFsrlMAvbYz6lgy6P4Td8MV57GOU-tdBHMdLI8RkArMf6FBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rboGTWGkxa2B-42Q_-MvDncITyHDzehJTVzlKTeYF1u_xAgrHtmHjgXLswy-p3euK-WG2biYiHFOFJhec3jYIUW7rbzhvyN0kq73nSdXpy5zGuQVb4CDCfSSqnYBXSUvYi-X_V2IcWdnCuywe2p_m0ChTPbDqXW6EMYtRHu_fnucERUgDudXCj2PRbN2_GpVb3JRLndppAGvhnrnUJLJPTKMw28lP2NWv-R8b7d-19Ff4PANw3dT67LEIn3GyNN31w10YTMGd0w7YTgAzMLgGG-XIl0GogIvEoYPvup-4u4HCzrwfGI2TezM7AqLJoinbzF7vxjJh6XLcRgmAD8yVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j6Z5S0berVhXSWhOHTf75GkZW2XxOy5mdpVDakjQptDjva8QgHuPs7pvg2_gfjNJmvuaOGWQES3mFXhMWNdA9j7uifAuouXdnqSqhdqm1sf4_7afPYfhZ2d8gIV5z8A-kHtzwYnjmgUj99TQkvAHOncIlKXey3a6UktbyyCCmImM0446mCz20d2ljQ4aHlbWZrrLJZvJ_HSlZ_bNq0KPAZL26IthbMG3k76rQZ1WzuKialMF3JxLrRr6Ze1hsV31j6cNYLEDHMcls10Eguj8T9h3oR_mhEETE_fCBlXtBmBk8mEz1Fw8WdPbadTZUBE-OIGBznMDyUebU7_6emBU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RlzaHeDRhWrvF1yDeVyX8HY1sLRJ7nPBneLeqwscavsU5Qeqc6KyK3xdNv4Omp0NvSqZRcUxp_hBPlDAXS-kVtFW4LqwrkzvGUHCyhN1xgo7WUV24vCft3v8bjmTQADP_3V6KKrcVs_ERKLoGBzcC7MwCMeeNJlWlbNCXrBMsyyt77cBgB97_4utR0M788VwHIszSHER7O_7VGmE-I1YYvK97KTioUJCGoHzZSOKXwGwXukPxiW9z3kFqOG1rmu7NNeJEkuiFdFXQp-ECYlwYEngzojFxK9f_LISQ_GLIx6bdBmncdqEM2JvGlA5skLQKEFKJH8jN4b6X4PWLTPQHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 47K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c_GG0lI0CUzjdIBYuxDLdg6unVxn2ilRhRUugBUnWSi6mso_LbnaZn4c0oiWVSShhGRxvEzlDzij0sdHiLRi-prr_RKWEFaFSGXmUABMFehNvgpdfpiEmfN4mGvZzBLvi98waIzjpwcW4su-N7bTklnVsJ7iPGYOQVDgY26cmfHc6qOyWybdJPMJXszeYs_FygLsJ9XUesYwpSUJXrAUHvdznhcn76xKei3WvTRJG0ePez3N6um3Ztgy9BmtyKSg60p_3-QHY_DN0yFEvfc0CltHk0b9xlqOdHvJjTvTkwhyvmxOdaV4d6DSIwiBNlcJQ6Zcl48x-hduf5mR_jiG3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Za--j8R3PXRl2OM-RX_Nuv7mYCbri96Y7yKMVoNWbzWWmKBIG6kWp0UKscSWhGa_dFZiGwNSNS_5cXcjCn1YF9785gBUwYSEnRnow0gvo1DIomvKb3zcmYZL7MCc0P1CJJPnszasDQlB_nXDcBYNApWVsQjGMt7kqGRT_M5AYQDswBPeHSMAmAnt8NNErOy3rpviZ3LrTmCH53TfCj4zz192OGyfUiSv9jgOlGTwZyuc5_urfiFpWTj2PnRGpT40dm7KvCowFxjtHaNXOzUIFAdA2jHLKYGNJLXTfpvgicRIVl8Zay0Fytb_UWra0NWc_hNHQPhaqfaxyIrCrt5WUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cJk07bqyBSn5X0K_XOfM_umY056dv3lYlAIZDfWEnmThMTIRJMPrNFttOIR68VT95uizv_8_DJruYs67_Wnj2MtrIYnJLc2H6ySN3Zp7kaHL_43Pso-3jarBqXinbqKwSTNg6h4RfdQDNQdrEyS2cyLdNWUSJeiLkNwTeV8lwzM8_hf1l-y_C8111LxOCx9UV6oPDyqScTJ96o0efwscHR-kxrVvWRuzEF8hWOP023lmWsqc9_Uf1WHGv_E1nvmElmfYThij_R83WYgwf_E2f2E_eE0AIbNkxmVW-a0R0AlbyLX5Rc44dystwqdcWD1JEXIUpOTTfmc71UICyPYcZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UXd3PMZbKVgRVQGD2VEpMs500EeL7FDqD9sqzSlao0cjBxv3SuEf0vXg6U7TlpBEF1oNw7MxgzL8a12Qqa3Yf3ttIVq5Qe0uZaddmOP_DvvneiYKZu4f5m0Tw8r-CpQD8cYqwoqDcrTVB3h_pnvy5BY6Ay6yCI8ut3i6odcVuCZi_swyAyr1l4utb6M-s7betfltoF0rjRMwKx_xpsbTpdncR62SDfXVIEGVJ3j7g2d4wNIAPm_K3i38eE0AELUBzt7dGNrltvzqbMAreQGLiMnwPNaN3vexIF6tFdgdmew2shViGNUA1ZjwUzfAYympAkNyKwWV9Ow7mDPsg3Wc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QdlqO1SThFgByMHTal8q8RZnlAtw-077Keq9CAdvqzP0PqdlrT1qdFZcd-0tv7f3xcXYQA4_-GKFPEPtvkMDeXcaAffXDzYGGMvoo0JRJnxrM0b7vFlswG1tLrEA3T0BwU9tnScjysuSaf59yfEQ7X1xwNZxuKXFh4tLzgzCpW3sNP_0eoqK_6D0JI_lS3ELEYeVLw6Sc0FNRVtyheGkcHpX-GCdM-_w4-hsVcXZRVdw9FS5vBf2w8poWV8Zr54jp8flGZNbyu5SarLNY8p2EqJ7NdKu5kGja_jDJByaCM2kJgDNDr5Xyzd_Gs6FjDBxDgDjavq_hOoA5Vfepbiewg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7GZldBN_ICHnkG9XtvbCNQL2Be-oBrUa9fcoMOTcAOtwMJzYxBOC78uj1ShfZULqLDPvoT47pT3ySY0sU_We3dZtqsAd4akuxtdzKlMnDzYmPxKo1KYRntt68jwiJJtJmlu1PbZKB01kUULk07NmYDkWAEi6EBFpz_u6397Ndj1c0WF23B1LtMZBN8798sXMIQLsqQhCTyHMCuM8DVMCOqOVxDd-2y1CkfYk1b2KJXj0puq8xOOZzFW8nG7hEFwYDJfLlwkH7PdzE98m3izqVJcrGsCB0HDBkMlpQR3HFe3sQLevXtoMFM_jbYx-lMvmciQMe-_vjJgm3Ygjrye9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JN4F-YlyAmz0H6J1XGlc2TT1ZWwUWk2ZnU34iWIkx-iY3FrqcriN2y88wqHEfpSXiSz-3u-TLXYf_RIcOaTcj6qzry8y5ZzUu-zilm0u2RRQVQlTxS3KX29LNc-zATlmQZH3SjhlPvWCJSwV3GjRj8Ly6lwktoDx7GF1qw3vKNXqolhuqiiOAafH0jZ4EyuUz6lp29TZYmiQe53YrXTq0e0GBXyLAtA9A1zWTWUlS-uh25Z210CsmtIKjImkaoJ3u-o1gcWcAuP-0xEnJ2w5SyuiLfpu0Nda5XNxxglTJFN4U-24QBR6WR_eX-3izpbg2oDdxVkFetK14fTv5odaew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h4oTItgsyGcA55nC3K1detvLvvD73w34-Y3YvqAYwSUnAtw7RfF7fpqXDhbziV5_Ew1nYKUDCpQ3r_n_awCwI2T187Vv1_fG5k2eNW_F6JajnokYITJ8movifaz7PzTAd6lAwqLBx4a46bk7GDEbqVVxXF7CbWz2cRckP5LJ_f5-dySokI1jh7jHmT3xO10qiqlogYoRZ9K3P7WO2Z4SHkzq-dck6oW3h2JuzTSDekvT7KBykE7isUxVVkOZFwD3wCH14L-NQPDlKWuP_DZhAfCtXaCq_5AMoK0ilufgnnqO1AwVONSHcOx7CjmJTUDW9g-2Ivn_tYT7p9oirb3z4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bo7PEDSpK3oW0VDucASJ6L4e3t7Y3MtN6QRs1U8gBNNCzI7a-scotQLUSJzQczi5K4C4jniAVgrQjPXxBxX56rjGQVNpuIboDJATiGbY9YCnMSTv8q557zw3zQHqZWLv1_NjZADJsT3fGVgMjuk-UDWbp7O5QZCptKXPUs-QCseOQnweXjpaTkeGP5bln81E7HV-XnscjSBK5fBAfe0wllAtkd3Gh6bacAnHwDKbGFu8YyTcsQXWoSgUtPBRmpGD-PYXz1bEdO1v_ORBmSguRGoyw3ys3r7ndl5ADYNsWCOwApylxpcj4zOpGiKgt9LkLcVsO61iRs2W95lU-wDLJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gK6yE1X-NeUCmYtYxsZTf_kutmEWal3Nh609D5ZWSntHFvLcPeOQu2V103_sLOguFwPiQeahaZakF4n3vCqHTeVwAWqtfTwLn6iEEZ8gXm0VFY_leLxG1drHLRa0Gl6El4D_x_m1Y4OvONjZbzNdrudzzUSZTu8bOiizE_F6nkMksOTGlzd5fn3iwHaJdA_Si8eB3IOsOPC4d9hTT8clNdl4bmYp41Ulcfx9Drf-zzIBx1i3ZkIln5LNAr6NY7U8tmDL-4FJs6zmN_fPPYmxxw3F7OUtbsBvSOAkjnr0KOI7A7j6EoQtFgA-SDvvx39wZQ-25HpC6Y1paJoP9rqhow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T_JutDVIUUykAievK2kTFYpRunjiZPHFGA0ITAJU87hRMBz5eP6uWNe30_14n0JUy6K3WGvyrXJK5ulibvgBObyDunmrXJ0F9xujkMPDBpCmvwFIUuEyJJW1H10BQUI-iP45iPeh3hXpAAFgJdd0o-Fihcj-Fpsyh5k4ZnHeqDikC8p-9cX_zHLM7pXIbjWlpMe2kQkjNwzDtMUKoaOwHXY10QqRaSDPymqNFV--BzJJhaTS-J-bFYkbXJRatSv4rzqtZZyyhSCS8rlNKEzmPsnkpaEBb9bBtsizdQCOUlQyER7Zu87ZRo0aUNvWS0DsWZMUvStdgX7ODLIhNRYv1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpAnUoPWvPlf9dAqBzOpC__TBwsMPOWDX2AwmyI5gdAuCQH4sLm3iP2xPFbo-JjD9xoZjbFTtbeQW252SQuIubesSVN87BLkRr2s6QpUnuoqzghRlNjBy6pCBjQmJNe83lJo5q8R3897wtBqT8UBl_cUnDTvtEYxCp2NwRK5l9hOhlPMNwonPlIVtrEQWO1-vpMdW8L5zJbnPAslLYIQxG3VUOm03TKiDbtIFDy6OlfREEmXFxTtP70-B4xnf63ir2PSHA1vvSbU07fRrDObBfFFAx1uLFrNnUhxRbsk8ox8CBuygPIilAp10pIlbZGLAJmYEINIF0Sy2yWb3IjWyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tAZQHPzoqy86_zf0r0gk3M2oglHnf7p_catpXijEPfMxrYBBuO74K5GD1sNBmHxLJ0Dex-NujguRgjI10iI8NSr1_xTULfY6egN-IqZ2e8aupoi1ECb9cKhIsmbdwTeGPe1uo2zjKp2iFHZxgNyg0Hkei19NoS291WWRDqAUMmT8BGWORI_X86uxy5ecKkdyjVDW7G7ZURzF9b_-nzGIinMOOS2TzLClLcqaLTfiCYbucp6eMDr0XbHE_PtAsPVfHHov0r_oypCmvt97NraD6eacvrY9G2cziJOgb3OZgc_7C-0ZFz0714KPYMIvlW_yyJwBgFKEX0TdRkPXDc7wNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 96K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NMQqDE-8t953e7LfR5-7T3mDs0KR035hSXlSIcmXIwV3baDNLbJ3h2elUDpuj9l9dcE7_NbyDs5FcNXFI3_GiVyeu-NSHHWYkjXKk1EhlE1sMjie09lm9yGPRhfcgUrs4eXYPmHCD9eKNkuwTg0VtSyC2DE8Qd0DeLaXYXPS9YrTsGRFidxlYo6FTve5OZGH9ePe1OViI6aVVCN1TezdFiGBiCLZCTFmcvjXf1S2LzXJiUnHcNOW353XN3DoMU8FDPwPdTlZK3EZ0YwAiu-mZItgD8HyVUa88FbCKHgCJVQFhLjvNlNlF_hKYkec-JrfDOPk3bJhES3HpOXMLjxxdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jh9YS6PXHZPAA7MWUkXlpy3XIEbQwboNZ5RKJAdt7HzpQqPf8srZquyzzhPPgRbhO1ILyxgeeyZlfkMMAY7cKp9fUjaKQY_0QZHPernOCUlG1UVLjWrfubZHJ2iNOjelx1tgc0eOJHMRC8dzUvh--HkRfLb5RsNelsnXYGMWabFLpNP-G4-54MmQaNra0krhZ_ViKBbL6SgY0S-gOhPghlNCCedcIAP6L2_DKiCdtybZ9o-HC_KuUglXM4dAzJaXzQ4Grt-ticXDQY8VA9ZHAqDOdjI2Lhpi3Q5kCiTJ6Un_z8S9FG-0__yGpGYEIGz4mMFYuGT0pQ5xFvJDSbK7zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nIoK9S1QCLZ0RGbTUeyNXF4c5AVRrw0aK3ZsGJQZkzJqRK4Sltu_l0-n4-LgkMjZ0_7d86hUtYIYvhOeaCkb-qDcXEx5q7rMYwY3Jn5Gbm83IRTiovucrEkRRN-sQtfrxN6Gzl6Sn9Sq0SqImDI_msdQTpM0VUVOJghjS5OTcC77Vb1b8bUCG4neguCngs9nOCySYFhWu2eeQ-1IGns8sO9hytjQhQx4Tec43qDMsVCrVRPp5eo4NJKRdYtqi7Q6X_EZzehyaxxZKyhzaOAkJ4QlvRCPBZisWbt22lALPIVEAZzg88Vt9JiyuY5_TCbN6yS3doOP3AtUKy-k1wF0OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVBN0wk1B6DlRmeH-6pbmbQaiU_nbKfbxJZ1sK-rVBU58Y1zK2ZgD0YWcUykGDpdxp7dA7oxTiaz9sZkiJt_pjohwk9uEUAsgW-Q9Kdn2q8OLzgRNbaqL9BRGTyPot4NIXNOXp1K4DH8iRwoB3g4zpn_y10GrEucmvdTRQDE0KjoUtZLA0U1kZnw33MQCu3y3l4yJQfNpEQCKogKXM5wc5sKP9pZvK6pXVN-ZfeBaIzuglGY3aZk2HanzH7pA3ggCgaPZhr0HNM5bZiJHAjNMXToZtTnP1CkC-gC76rZxPNzJ4XZO6c10XwJgRywz3r-7g6A7WErSSWS4e9BUPnb8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsrOfOuX7_JIWKEv7AhGM-_i1uBJyaG-KVdMNov8JAKSGebTH4opgfefQMswktTUW7KUbN4oCng4SaaIGYj5noDFHm2fQv7pZ6YSZuCp0K1SzkAs7QVTJbM6F6hZ8pT6bwlXUtBdIIMKSJHJL6OgTApWOcaoRTXVzlIOXdaLaLBf0PuphRVC1JuwJJERkDpt5hXDyFIy7rOyALoPy49HF4a3M3S04TwdW3yDEipejVfl0FBwIgR7OjAsxpmfx7AUcT9fbMmZxvlzCkg_PQpGifKj0jv-YC7D30afJMZqetGh9qaS3SqgB4Qc0uepc5LEttrvcThT5E4EPdW_uLQ1lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/evimH7woBNhkNmM8YOIlPgD119OzasJ_ARdhlMZ1osNHxpeebjLA1r1WcMlVtWwTKj9X7bSntX0lT2kx9gBXlMvcD2IXljjkAtx3DqCz8iMoU0RieYNxv7KHGQW4TRNFyg6U60zUAzN-rw_jWlY3SxAipn7cy3agCBWXa4SjQKRB4S2bh0jlcAELh9LmZSaitI0x2i_bv5hqeez8PC_1MipGYyztZo6eHk8Q3ROxk0XredDklVhhSIUiZEN3lAPSctYCzV5js9G3UEh1mQcLCx3BrhLWhi6RyLA5n4Ob6xmziNRetHqc6xRQ5Y1pzDrgz921ThusiYyZCpnWS_UFKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cC7J8wwA1RV_lHxUy_7nRTwy6bFY9ctC7YcCgISASPp2-CxzUQKLFEE693rUO7KOs8rTDyZetdAvVNeq_JFbw3Zxyiknb-CS_KTdZVl6moQxjokDuJXdf1YKvZNbjrBT8LQqON7HjiK-ir32ij6dhppssPhL9a2_IZ3mzCkc_OFBNy2TE0Fqq16q1SpFJh2n950AvlyjW5d0SVKjxmtRMT0dRFVR4mxD89vlMjzt8PTXnazBpIR0ULewRBALvjmCxfIwuWlc8WegJdidFLCOu5zxENsVnrBLBBsuqz8he0b9SIpAZv1vmGVUja0T4YpDIk3ztIg2VFDCl_4SpWVS8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ie-DFiLaNr72JMWJ_iBNEOJ2D-xz1QqUI9VnNArsInwIi5XMWjN2daZK-KBLEtoIoh3UR5Hn5Ebri3S4v7JCpQFtTNlPcO8koGraeCy-axQkeDZFA6JSfbikGEEfVDWvLsg_YuxFYh64iGTd_5EChRlVnZFPTNII3AkqtELrtGIfkppNpWEosj_Rw5UznKE2c2sLW3dLAiVvg_DqygI-Vl7BJFvf6lnPBvwqiQh138mhMu6qiNfxkfxGDc3Jk2H4OjMiBcwDJB32O-mPQauiT59jRhKIuqze1lNZ7MqhHEeGYP84HqT9XookPSdTO-v74Fiw8WEhi_cykw61tLuB9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6EJjNFhCs1FjLtJMeURsUHsOIdnR0jiOq5zhSlJ4NhzdVye6RNkSekDm6T-26amjwg2_ubiUngz4XM8WaeWbeTCHgB-HgovcLMVI7jQIhxD02qJQhNkhMLBxQRv7Cz6HKhUWks7_U2fMVQ1IacSupPwd-IkqTfvyqKpaQ4RLp-U_VyfsyYzAxhLMG5IuDWMtOl1NQQixzNXrOxtDQjM9GkBw3yjTo0EYNF1P0Vv5md-j0o8Z5QR3dmZv7V-t6aOnxZ0EAP0p5JEKwc7Z-4AI3z-VZ2OO-ka8iL18YL9-AbPzF7J7d4vT5aYViHbRtWBiL-dTmfZIAeQ9sPcoM4nzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ke9NCI5l5ZaIDE2ChZ9ANLbEltKffIDf6OK0UBPaqnaQg5M-LlMgCY66JPJ4HTj_X6aijesx5kOXww_UGsKUpLYLYh4VvsgZKnrw5bbNfMfJlp-esQEN3Cy5CYC_X6LV7IwlOyJSs7DnZPNEUZ-HFIbeYU-96XvNuKkhbT97wbYJv_28MU-kufFJvsv61kVugPrnjlNeObyaHV5ArJE7s2mUGZ0hke7Yqoc9egjZmhAKzYoAEgspC-n_3FRH7FID5LOp-mMfz9nZhwrfA4h53jPifzVxW6voOV50F7jCvsIoKmFXp9KOBHKmWwwK6Uykg8wFn_2zKbiszDIn4akq4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DNxjB6SFkh9ox5xbPKm6RwraERTal_Eg6ARVPAnMHWxTAuWL06y4HiIrG15fHfNxOZpRwWo8Z-bIA5LNpq1X2BL3h4dlhw3JUCj1ivyBBk_OOgTgAvH4SZKxQIeeDMyLzn25a5UCESHw5n5NB3-7QhMd6hyIljYGHj_pqn7cV-NosOmlASrYGVqbMtrQIm0Wq9yVySV0fUCqemfAkmizJ6yicE9lS6IkNM20DH2BX6yDU7FRvHZeIQWrLU7LUHse191YhyyWtzkZdYM2dj2slKchB7XsnPReb419CD3q38gtePSZArKwBu8vtuaOdaNSWL40_o-twf6pnq0VUyatfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uUQV8WERYBuanZGT_gpnPjSP4lbzfE42IiBjyiYFEF7aTACWSI9hHabR5BuUNba2SJSsDlgDh48sNjTCbwFYcBj3UYgX3PWr0jzg9M3vSS_xXDVoLcRK9NQOaPfvvg12xMK6Sk8qczEohB2CJhJmUlXAqlRX6zSk4ecnWYetXSL60T_YQ_gYo0KEA4qGCLklPHbz1CLBN1LwL0VEiFjXXm9Usuoz3FX_AWG_RinAFuc5zppMmYfzUmsIyqGHWE59wH1SJQnny9kBnFYpFrBrmtLYLzcuzhjJIlomxxHx7s5nJOlOdPyUYKgRrS-wxHcciOU4G-ctxWZC9NuQq5KbeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iu1DH-T1KvF9OMD-QI9JfGNaW0APqXqYvwKIP2CbNrD2Cqy7BrBb-bX3DIFToyyHseoj6TuUkwfHW3hdJtHuYDwvs1P4hPW57SKUoAcdEo4tsTzBsbf2kh5iequbFIZQa7qNXVCcNsGnwXwLCDiVg8BGO2KeHwWoXu8_PB8QBKNSngkXjrf-o7r2Esn0B8CghZP0mOX6HTQZ522njg_FdBQpcL26zIKw0VoBJAQ--Uq2GAdRqqA3iSI0LmhxscJTV2IxV_QAyMHivKor88KWJGohlvw1zgDoDeqy64gKOtMGsUMfK8hWvvxB4oPgNpjKShMGCVonreeLyYUgy41uQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOcKquCubU7pY_IdpLjvUJpJeT3kEtvQqxZGNZ_573RFm6c92eROXcr_tXK1OzU7yj113igpgdNXQe6iCZwqIESuzNF8--x-YzffoPu5Kw9GnfZN6dWWbDYRbQ4UqKvhtALKBOz9HnogFs71Ta5BFHnQPdN0HeN-Y8D4ngCxvfSBx08YttZFvgSzw6sl5EbCQD8F2pfPUvEFr_MXoYssTVY4JnMBY1FNDMH6HxgWGa0MF-Q7D-wuDvbHNk_gxbvxqT3TI0D4G_3A6BAE8-bwyoqgXpPYZucqQYTEfIiDCrVv2f3H-dqIqa5fQZ4l-KkxjufQVSle1aATQi7REEWA7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lyRppAf3Eti9_SbY07CixK6cvU4ucd2Y5xncNwr8DxEXvXiXE1H1TQHuP9fgEYE1ZgVxQ4KaQ-qmVAyxcVPiDnaA5fCLBl-NFsk2tzE3BLIIIckx2lTLtGhDMBmQeCGS0cLNvdC-LVzf574AyLAiafFNybV7GDB5jUm6B-fTUbuYq4UDHjcCQZh6hzUxIxb-1kWlSED4DLciEXZeoE6D1XsnSIXkuagZrPv8oMb_pglKJgnyw6b8ShjpDI8cLCOFc_3fjgpujFaHwYG-Yg-MlNFN65zTI3BwKxmkszIB9mgryCZRiJmp4LzbyX4cZVKqWc9bch3O5ufk24xG0Asq8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAq4SZ_p3sZhcb31LOwRxp_G_BvMsXa_EtA4cyTVE2ERlfcyG6GkMgl0VNZJ7MrNEcVmA64UWa_p2jdQlbI8JdOkYpmW0lzmPc25EcQsL_8mF1w1TEEjEWsYcPdIMqiujieT6NJ-gJ7iGHdLcv2gjof-M9KsLuTe5_dFHPeXipbrSrM5HDOjtLFkbEVP-JtOkWOLYkJyPi1CA5D4i-YdES1rfmwc0gwuqyxJujE8j9pCJ1yMLb764_HsqGri2i4TtEdI3IlrHkFWh-h-79P_xGcOF1U75-EqR2OsbAJI93zGV1rkC8_tuHHwGOYgLUOvu_ZGmLXFBEKFUBeFwCXPbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NwSFmiv1ABWon6OJoTlmJExwSkeUHG9Q3Zku9rjxrew8Y-C2RkX_1rLMinvYVOeViGalVi2IMD3FHFpgfxR4Ccpv6GaRfOg4DXMP1jWZLlIrMSaR_GgGSUNazS9tN7O3NCEBqS7CaoEywv70DPTulLV6r53NnuOc-m9XHnz-5uKDeh7JQ3xtzoRMW73L5OQfO-havQlI_HBX3Eip1Ps0lTfAS6yEegAOynAigrG4FKTy1et_fofdATNfrJtlE-TxBt7EYs6S79YBfe97ivcqOW_OpCaRzQmP6aHipd0GTmVZRcSvHcGacPbxm-eogv_AMd55S98l9bpayrEkOVamqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSXcShpV5dz4_Tf99DkDogzL9_Q5BdlM5KvoB2NOM7rWbkSkHBK2JbrXTuW13dJmEfdQYkrl81JuLIB7h76IISn2VjXq96HpNblRy8h_GcOYhHWSdrk2k5izWHJo6gDR4HDYUHlYRl-ikIBgeRYLHXxTaXpUm68KUOp62SUIRwcITG_1QfarJ28Whn7wOsBvzqSQqY06x_PKOTJ7EEZdgI_xIxVoU-nA4EmsPjxXdkEe_6xvIKsAHw8MAfMXEXJKexxlPvaTIWepvlEEbH0mM_5OuBKxGHX6VCHXESqPHazJxB_juezRhl3DF_RHq4whV13MvUca8c0mlureFcQJuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hetBsaLWkyMnqI5HRHwQwU4GKcCzo93PjGs2EbgXrzPzoEIJqIfX9iBYKw4z29PEi6LF_2QxZj7dnhODbCV8cXXChlqmcuOJ-Bj3ShezCVO-xTMpynaiwW-GpUsbJj976j89ymUrxuuFMFzYnR9kpJDreDG-oa0AkI-a57MCad4H-D9F4v0-G0Xz-357CxHjV7CBK-JiigLUnBDhV6uu4QoO3F5-MpcZW0czQ1WcV3Cr_lkyAGJHBqPGwRzcnwKWrjjH1WSM4fSH2sM0hVXcW6aTuyoJfBUHcWc5nONNIAvnHVL_UQcQiI4Rp74qSyyWPguBYqGSX8U_c7qnhpZzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
