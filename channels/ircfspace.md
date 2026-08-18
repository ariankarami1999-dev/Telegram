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
<img src="https://cdn1.telesco.pe/file/NUdUsK4mLpTN55Vrn6RvJYFT_EcaubultJibs-_TuQK5AIkZiLJW2fC2hwk_dywcT0SNUaWsTT9Z-EEjxXzorqHsUAjPtU_rC7ja7RlcxLPyOp4t-bQ779N4ffBzy4-cCTD1DIYOyEu7xOZ8HdJNTlWtrgWsPxX8O2EHp4ugSp_noXQljF2zK6F_90lib_g_iMQKm8AvOGxp_QI0WILdQSkNepQlytPxbi15QfNWnwtbBGBXJjBiKOewGzFylXWVk0g_zs2dgNJZ2cD25HH_NEL46bAZtsXwwuYo3w3mXKrppMjNflOzmnoV8GHArRrvFCD-LJap5CSC--H5qxEr4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 14:23:10</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T6TX3ub3-sdDlnBaClCL6hv7Dlcrz8O0EEExNu6XX0Dq4dmNpb121DQAgSqW7dDvzWmHFHMlpKqtziNoEaBz9dpq0ZC7g0KtJmVzxNRPJFSVm2U1jVvHJprAh9twCS-G4_NYeOz3YkBdoAy8XRj9ZvzqwqlbNsHiTXk_Fw5W6ErG2Jw6NGMmi_xScXIwHMy3R5SV-amaSWrjNeyOTHUxjfeC6V2ZooNd09QIx3W10Xv0G0KiqcBGb3f-DJVZMMU7PSxIvBajxAzCtZ30-lGp30_vnwhgbOkyqmqK09t7695NlGS5Iy8i6bofySj-bgk--09ep_M2Dn6U2fdPSqpNFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qdWD4vVNS1P4ZXeAARWaH6APKzljL_dGl63s9bAOC5ZWHxo8HHGfc22lstb95NvSGxDkhN6jNAU09WOtp-RwI9FPy-H90MYOW9JenmUHXgW1ez15ruS6eeKWO-4Yqf1X2uVMsdc7_yrUPvx_S5pHOOuKZhbbOKdY2K0GuLkn3VX2yS0GT1PQ_hXMNLpJkdZ1IATdwcXOrlcWbA2Uml-sjCZWd9Tb-EFw81VNpzduZplqh0-XmfMchv_5k5ZHdAleKbXOWa6_ykbAuGZP9i4Aq1oIfGXhKIhk7vbWDcvYyFRduYcQ5QU9cRuiNfithaW1Af4Xxo4gQt-VBOIyCwUyoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HeeZzWhOpM34E8PT--GjWjE-TVDDGVSfcXF4xjSJmhgrNQX9trsNDe925Qclzgxdn0pR3WmRxRgR_OQubQGmJq7QkFXZuHm7qoIiHJyjoFE8HRnDoo281pz6qzmcH9Xuwpm8cu7V8aF74t978F2oI0d2kVpx4EnG40Rts6AOkVE_kbx5JDWyL-BHj_0kxleETgmUuqyvixL35FmBWZ_EpYJqlzZXNaiIWG8OemijTw9CNnOn_d4L_sf6Fj3hYThk71hackiyb3lkHLlobCN8ATFfoHJS2b1qIVGHe71ZqK-JHEzJtdvv6RA91OHwzpo-4h7A6xlYRHQ5Sv8ytjU8jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YaQa6jNbDiIIJUzsx6YtTswtSgjyYrHnZfpYFY4Iff0oxnKCdwDSfR8Ic5I80s-ZkDbvoTJPcxbdYnVXtb4oAx2-tCeyzyVsaN-Ej2YnErh1qtkdoqYst210W905i26XIJPDu5j7Lb9TH0uNZzt5spvckZRZZshVHAZsmS-ePcTgcc6h_CcKboUlF0LghiteGE9wjTaUzRioZ4rFPOKy-Nhn5jAXO6BE2S5eQqIP-JCyLzdRwZQ7hk8RNRW59aKYkjRoKbkVAd_QJR7-CSBTNVBGi5uE4L5-Wyk75EgDqU_6ZWlKculkzMoZuwZhqDP5mPv3F_kR55bvA3rBHJ3dBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EGUnncHLGLXAYPfJYk4FspuS8OZO7Xlf7Nt2leb3yMyFwlXMd7f7NvgcaVbumXhRyREMAbCxD8D6OemNJ4_N0TRCha9s6mArBWKzwYCEplyUPh_JuCBfnVYsnjf_oAybi8iZyNUf4kr2xlHvCxkf212yEf9skSNW_f40BEgKZwO68-37-CWnt5FH4m9ngrNY5kgxu2V0OtM6Xk79AkJtayrNUuwBQQ7wSVpB_R2wr1w3-CIIwfau8CD5YvpBSKyUGuXjoE2NxnEuE-rMJfzXcnWq4lOBI1ll1UWMSu5bRuDbj9inP7FtyR1QjjIO6XK624upSx5tSKlvAaU2BYtGDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/scvvCOCMiTJ8vrkgiKkClLvaUo_6tMHz1-GUy-oDML-DEp3UDAAt37slCY8GChHcMbC6-LPZbCTn6amdPzAdT9ONvLKtYxLiNo873I70SMd4ZAmo7TUrlFFhq-2sEVD3x7ARL0CDXE-dsHkIYlPCjVJzRhx2WUy4iykvYHHl9Zxp1VJ7r_UpeorIA5esD_ZEes-DslqVVYdFrbAi1qiUPOFt9TwLn3R4sIPVriRXch-g7gUOwmJloBsqMd-H8yKlvqQ4U01wkoY2MjO3ORdlLKSOdA6vGJD7P2pWkisORUoyYlhOxrusZ0fHDqiTjhFVdVOyjXiE1kRn2koj3UAxDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oF2KDjIXdkj7rvDFdnuffRlIMCqIGjfxNoozSBWp2OUXTpIdyNtMScy5maK2EmJskj_P8hu67U4Ml9wPqRqsMcNUtl06-1ry3lggKLH1SAPygufdTkOjz1JlSl0GIj1OQGjdJEf5RGXxja2G6NlIlUTNXMydpa4VY61Z15DyhZu4ejg2FpPSyKKeVugyQlQs-SRQk0ZiX0RsgeRsDhmOhHP1gUXVoNPuwreSvMDAmhnttQJnXLsc4ABurcQXTKsOB3Jff7-faK5z7Lr-GoiNG_93ZlDSaMHj0sQc5hteiryFyBZOos3-nXTZ91pzvvnqh5zONlTCNdYXPuYBl4B-PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iIJORlkbE2f-hN5sMr0CPYTUESjKin2-P1gnfkra-CTTxl5BnB6jHqkqtxsVhPli6hIpr2MpTmh0fpmYiwmlbRM5K6a2U652IBcoVWzVTkjcAeGvdyl8y6rWdocCFu5AuepBwrvi3dHtBblfM7de3A_tQfyJWFYrsUiqGu-X5u6YaPR-eYlKV_j1GKdVMT6z2J2bvMvgipxFaYxKWjeNgkQpHjfKFgyLMJ_R0_41XAF9kkecGaalkYg-h8uxIGC9yKpLKuh6rhPervjfHphMnRJ1X6JbL0d9Wu3tE35G8oVK9nzAsNtTq_jkQ5iOSLQO4kKv40C6YDkVqw1TOXvSgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QMTOXYSdLIGoIz8dXshEsmMd_8KDiQNCVJk0GGbqjdT70o6FQtyRW3kpe4c9PzGiPER1Jn0ItxZgMasBAn0azcOoaXCcyzH_eCCR1TWxA3d14kJkpVkumsfLAENofbuLCzH1MF-G_xjXEeaZSjcAHwYm4UmVKwLD7Ctm2uE9C2SJGgTml-KuPq_CSEiJuP0bnDbSW4J3YFaydgKcPj6sE-3twSSG0s7Di9O_gpA5skBs7w9JQjEn2J39h58SzXUnqx39-DtSEAZ_Vr2CzsIphgRlP6fSDUH1KO_Ek0ASxtU5czAbAk_eRX1nPiuyHw-wLLRV6QcYcVML_W1NKSHhGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W20d-g3L12sCkgY3ZIvU1yZKJvsxqwLwjUQXNXhO1zJmRlgUZPNh4tPrsuA0SHwmpMN0OrDpr_JyKNtpL_aUtUtno2OtC9hQkmiCDTxXrTB8ULhWOl4XL0TuoKrBulBNfOkaQaZ3-jtQAeXZ2N8tv4pq69z-03T8NfqanPZ-RiVStMRin5g2oprb791qwPvwqwDKLQcBkLOsN6gygZXoqVBMFaHYjW6hslU-6cJ1zRXKpCBPk0hBLKbsvkleltPDthpY3r4L9v1s_XDk83FWEviP7tUsGQRbwPkvIW9EfAp_6uC53QeWHRUQGa3wQWZSEFHiu_h1WXopG4aDTKiEJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uoTOnclAGql3E4YxhWawMldgstOK7vGOlJsd3QTOlKPf9548pVD9BWGczM7BP4E5t4xN_TfXvCmHOxHUFeSLZp7SCGE-aCfXlCYcpSg_gPHTpJJYnD1tKCL7zF-2qwfTwHVRVq0hb2x9iQbjNZWHBnVJIheACwSrwyKmasSGR65P_GADibTO721A-vyNG3iu3Lw3okCCI4rOsrQGyae-x30maSUwb2J0gR-ut9VqQw82H2pd6bhMCLbRNQVE9XKcPb54l6TWs57SQsjNyrQbpUR86iLTUabLWJpMMrGpjypHE8QbcoVoAswAph8Dydr-yzot7fqgdvfjZL-pDoPXoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q8-kV74aTjeh9UKPbxsh1ntXYUOkXRedIGeDzBa4wHSrbktyDWU4XqAQNpuKd7ZCnlQEEPs2O22ksW8jdFsxBrskstyvXQpFLvVsR2GYnpyv1qGq05xLhIB-QozmDmVWhnILiAww9CpbGZj-gTyIRyfKf8yFIzGKfOMZqb_Rl-iRH0MxGr8pHkz6P78YbO7jjrLD2H8ox72n8fdzZMWTLBvbTyUKq_SQ3JY258D8PGdRvQbrSujEXeOd7zYNur_O68qQoNDPWcIqoGrmgUoL_9R8GI7u9F2zhY4v-DNVLOq2gc-hajGND0YPe6gN29JifKh78ugTV_HIpjuz9O2IAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sbl3RVLgPRyworiRbidUDEkuYiRUIgYfc9ILLH-Glz8Iw6KjpFCqmWSIwQwovkCQuRWiNJO8_uSMBeqBKS1BIva-gARtkxuUrNq012NxY0Hpdw8-iVSzvm5NINAM0yGKOa3NbyGAd5Yq-3Rhf0ZcILZ9bcypz6MqH-cBm6ER9Fq1ORlw_A271GtKPyFc_XyIGS4ZP4Zf32NdkTZTzjapjNzBx4mr4FGkqMCQihxSyvv5urMCuhkcgTYG7IgrloYnWDzlcKQCnF1QfCYNrIX5JPZb15uKfPNuSbmIcjgGRoQWyrU8AX48cs6Rfnl-ul4tKS4rQHLs9CBxddvPjX7iNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e2EoQwCFHfGj5AGRlYDbaxlUtufwhyWHR8fjkOilJF9WHAfvsVY9iUzp0gx8sr018uR1Zfq4jYeDCrVynNsFXfVSo6PGnbK8DdhUrTfUvE23UeCuv9LT8C9BWQaYR6gClHiGMo74jnhOZMMNUrkpLzrKk9rjSE6Tzt9r96jgS3aSss8vCxntxs9XOYELCjQGmso3y7Y9df7VMT2n90vF0n0pcHT431hVZBZI-H3Y4fUS7VWev9Zo1PPuE98F-swRBd8SK5-kgAS6GDPPCwVsfHosaXz-kBAFzVaoZxKht9Sd3JCU8zFA_iduhreErI6MzsPzZzaJCebvWRLx3ImXdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZRY5YXhTaM1uYNoHL9VhWc8qVHTmmXEznh4WRy2a_Mn4OKoFzbK3VQNBShw9__I1tZHYR-TvPaOM3yJAwnQn_x_-Yb3re7nQ7l0F-qyoDX-jJzNT8xXGnoF-JlmpDdcVyQwnaPkwf1XrK1DKKgKb5SajjjLhe1OKJ8YI-bl_UwAyjlwGySaCv-Dug3V_2DpJk4-nc91F0TiY5i6pThiS8E6HXbukZHIB85gYjjS0Adcha8ZCpHytjgrGwQ-2gIAscOjqXnCG-QkvoTfi005imNqawKsaA-aZWUtOdUNRz10oFTn9SfQjWV44EMcNnLEWJ3s__YdINrt8aGh33veLQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jsu-jHNG2aYCX-o9__Zi_-WsTyeIQmtcqVRRdSymh8i3z_EZ5gtKwDgMZnjwChJO_CAVZp7IkNmgptMtbu64GwWX5nYJyx8yu1GvQI1Le74LVXnsZX9bC5BmgR5-AFb9w5nzAqUb7YKkfl9YxlKaWIQ4slU6ifllvrOMF5SwRre9Zry04EXMcdnT5QkeRtFhoAmz2pHPSgcLkRzXDL6aWTtISrfOmqv1ubJXClsQMpLWjFhAxQ7Z52br-DTJf77qYrJP8Rrv3TYnIokq_8k__zyqLkbYPZJlWChri7rS-Aw_o8rr6JwvPNF5UuqJGbdy1LoiUvkvQ9yaCt8dmkxBuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/paHPrJ0f7j4fj8KaOpRhulm8QuYhN4QqxdD1a4BCDTReZDuVrMQNbxVcm4cmHrwylx45o9UzRWg1uToDuM9YE_vdjXv0RZBIWgshwuNbkLtNXXOk8-_sUFv8D2FX3DIIs27NYtQT9gYT-elPxanWN3OPPjSw5kluDHzKUY4qv1rMupo4EPBGckpgxZZgCLGAr7MwPhSymuGaqXgME9RQ_yAdiUM356tkcD8fCE409OogOBw_f8JacHdkEPX7YmMxszaJSNImbl5GXvEhI8lXLXZ6z9a9DAMaCy36z6R-J6bgmDS7P17IuT5oZBnVKtSKfmqUbFLe3NcCieBaiNrghg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bApCV0o-4TNrZlj2gxfE9-xrt2BzKkdKQ12hDBpYjuQbKdAumquiydvUU-ig9HNiMaV7mT94-citiuxRhLc0rMdWASH1oxis2ttJONFQM0ZStnBFjLDfzhu5-zkGOZTkOARqWasLTHpTEeZ_uq4zGLhivVRyFeZfkqITOX-1z9tOZtXXedDlSSFbkaVEP2mc4NxSMPeVCkLJxhBHfyv1tC0DCvGrdfjMgp-G_yk6bFS_MUtDhjT3c4aMQwX7jBQ-dfB7DCSJ4bns0pJNPX3Dd_sjhklUJwzVC9kbICCvGNx8onWT3lzNp_9HXePcM30Wne84sJUpZIAq6BvIvQe38A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqOw-CZPOBD8nfK2dfP6E8rhTX5B37fuVR7q6cYVGNtrOf7rBt-65kNJnSfkTd5iSqOYnS9bji2E5MDQulqgGWd81zzzTrq1_zS4TFtcoN68xb3yKhamDa7n3skSzz5fF54eBxWQvpfYbJlKwVvFUQCIbUDdt4GacZJ7XnNLOvNDI0gmlLpMympaHmL-rXaAQF_prwXLpb05_XXqmDc_r0NZVtsW3xKKpMgsoMAiUlQCQJ663MDjknhuNczotOrqXlKrBrWhiD6dSL1P-QAZx6YIN5UL3M6qX8z7dB1Nr4Ex72xfo9n5Y1rT7qIPaHXLkjEj6jc74S9zNq5QS48d3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7xse7oKWzxAhQAb0vvlNhY3beZN4d-kYar8MjDloheuk0lD1zZY1xtm3DWNP70RkDzKbYt7dUyPqagAEbyaBMQJiItaO3XnTe4j2D5IBZxlA5k0-ATBk5pOGDLAaY4Fa7A9AMyAb0DR8cjeKoCXhocCENkNSKfu-l5DoE10VZunY1fffDL6hBOdpyvtMp3deDR_4-KPG7B0j_YuxhDyEfdvTJ-MPvjDRHRrnMqICU_WvApj80Fjh8qPaedIYGvv3FW8fn4VB_G0ZB3qfhSmelMblKpiNNXtHgk-lJNk-Ats8Rtp8wcTOpG90_kFGKhCkFpkT2qtw9MmQNwm8Ac-kA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Si8jcvMpJryW63IX-WRSju_Z8uOGzsLtDGRyvF-iIbrGx24hOA8GpVXi2Pi1jedx57qwVzDhSphK3xp23lrdKfg_SCwIW7IGQzvZCNpK0prGqz5oDW9Rmo35VP2K9YI31MIxESSlxVss0Wkzkvg7yUV66FK-pPMaOhuz_18W6OfsQplbllR18jory4KtBJZEinE-yfczitUgWQRX5pgn8vympUFdCXL4IAZzZM99tgF5dySFnMXqzSeKUUV0i1zr30ulyl5qKQK9MQi9McEIF4HaAeP7sQQGqeikYi1ssqZ6PSnUbDFOoiR8G0Gdrs6-_Dy2oghDJgeS5RrKXY9png.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2ADA2dHsLsCOEItSrwojv6w1lbkPrS9QA1UMgeYb-DjZKydUE2qsfN072g8KB20D78wLQepPaT4lYN8hv_2xdVHwQs8HSiBlD3ulZ7U7ULqcBgZyooN4fwy7d9fqsuGCD-OSaiPnEkikPF1wUnofTcqEAPmEKLpvGWVqE0ibJOd_6zSqand82bTpJfXa94h6Ix2ZHlLCJoZy8I3hENcTXQx-OHOWElEFU6CLkHI5STRXt9MH6quR5CTMH5ULFp0XWoZRTleNhb6H3oiQesuNXNI3vhy1QI0nY1fhrvw0wqI3vVj-QySSKlbfOLF3OYSmE4Qte6-t-Pr2aFI-Y_j5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Un6ga2wJfXBj7Ni2Mv73Md4t2UL9_UjH9XZlUN5hELc6oqf9DWo_ndu_0W9hTOSUuGZ4NgfCtD_NOrkSv5cWJhadxdYpmJpP5b28c9f_d9A_oDzvKUgg2FUowIUEZdXYYKfMAopdTedwwlw54ChVSSoq9P6ygiX2haxdKTsgLLet3PtBUO_3zJSorUyGyv7OBy92DgD2osswAW0y97Iq8UZz2dX9W_vbTzP9HJxvuTFurhpdpARZH-pULBrk6FNwaGE0dKFXrKDPAQqea2NGKP65IfMvegKniYyYzILnsgeqeYlBJS4benTZWqaqPJUJhgDWOCeQN0JZeKPEFCSaRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCvp_RkUq9xiBciUt-V0kwHgf_OjLdLT3X8KbZiYgdR8NdOJwgHYIccgleYU45JDRqdwbSv78k-0YCyl_roQ78h8YqxF9SHIT1ltFJX_rgym_05UdrlMTZYhSqiR6hil_dtVpnH_fOcfoznoOWo7r3Pwb4pCaBktwXX5K0wOEjZrAeDRN20V0BrD9dvjyhdPXuayR3dnGlOGbR9ymX_Igqcyn3wWFIf5uxoVpTHHPG7jxXoXk2AAK5V8Ruvyv7lRXSor-mC7ovAwqe7JJb3JWWmZnDk8CKvYvyyo6rxYFPk4GTL4siN-ke6AB57h04lC4YZziRV_2UeIQ_XJu6IVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kpop7y-hneDa4EXNk4ClkwyXhvsqrRSSb8cnUXpPP7wOAWZG7OMlMUj8jev1eG547kdAkenF6s3FpfsEnn69gtX_EpomVjoPjdz_u5iHrPOJ2H4Iq_zcfVhMygnGGxg9YC8iKrCZfXww3oy2s9ccI2-PlYH0OobI9eQKBhFYZhgARPgHIH0TUkxGNr8qKy8Gnw_9rWsccTj4WQFf6-XCUYTCD0EmKxDyv26JlUO6cdmsWR8_XcyYhmx_Tfe_elAkRQyLRqoM73seNN4GFtoGi_ZsZ6DfMSPMUzFjN3HvGT1JRmlG8C1kBNnxMnycBVP0wkWsD8cMiXX6nJdEuUttlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAl3n811_AebYlMsK1qVT6I2AaPZbGsvw6dFqS0sHLzfd5Ul8WlIumCndurVkMPf1XezJpnpIO72G5xHHRa8zBd0CdKqOD344s2_JUaQ3aAqSBB-WC3NxS76pIS-gdUodNEdVcAa4zrVgGBg1HB9KpAvxCKWMlNFY-twqAsXL7UM9HXSYmVQTs-dv2k72KSH9sZKFKbAnmsU-Xwm90xkh3O8mSLmWjNqFkzNRRCe4noPPHKwpkJ8TuM72qkigf3Kk0XL-VvEsxf-2sAYzqwonGVnXX-a6ZDQfcYUibKj09suD1ykrMLolIf-vKkqGkgaTiaUMFdfjdP6dfMFo2FFSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NxP27X1Dlyr1mOJffAPWOv8Kp0yU7G-ApfXOy_Zq2xzukNfDwRxCs_f_UvOcY34YRNcPldPpbrQtMm3BfoLKnZ4Nx1BvZ9qVTG-Ysq3WP9atnY-C_4EBCNWEVCB0E3Q9-sBxCaTzyCA7Spq7h91p3tXyxes8rJBiIn-3ZSO5m8VLRpj5Ubi8hMfrKYJ-sXW12R6b2xZ0vKIp2IMHhPMQUzybmpZ9JY5NetLO65-jSoco5ht-lXa-qoILZB-0lkL_x5HmMoDKYuc_MbKA5Nu9U1Te5iiesmlZw97v4nbacI4Ju3iAmIj_CFy-JdT9bdEASLfp7gSAUu-NbQnVNqO40Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nUVxC8EA8jqEIs9R1zksPizGJKRt4g2w2GFWCqi3Zsav-qs0cgqOplzxDO3e8KtlR2QR6_8dClVDutJjQvAG6xxEcSIF3O_Id9ivb3RXKbVxzY8bcHXXJh9w0Qm1sf4KLMbXadp0-NEkJbUnoKbYWRxjrLIywfS_lyGb6o113ZRcXYTskmd1Zynb3zGyVAmlV0Ipizvu6i_17HuFQN0TCaoVDLSqReEsCFb1T6jMqUhp4WBzU5k_YbakW-nXo-amVznT9OpmN28cAQBF7qnsbLALh9TuOlwWVOUT4y71kKg07P88eJ2tFjZh6ylMwBi3xn4l7_sXLJWttm7kuxjv3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ll7XMdxRrwGfQ9dvOfc4FDIpvIB2zU0app8A7ztT8_X3m56X7DXOn3nzi961XvNrEsunU2F0Y0wI4yb1r57VHIho7L3j9mcKjrHxxXLw9qUAW7kEl6qJyLSfG-yjYxa1gw5uM0DaFEhO1vnOV1eJ0AbRVu5oATz4jIG2vLHCWD4mwSyWvL9pXyGHF3YjyFqlfNCQyfSdb1jxJ_td5vFxU0ChHNUK__Hrwamk2_mis7wJEbNkxpw3ZXRNK-bwEPFxwpcyEDMMDGVWY1JZI8kntS_QHiAg2xmD3e0GnQ3jxWoUGMwoeLqjeICVVFY3bl3UTO2uRFW4ctHmGEjtGdvc-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ASIOOStc2d7F6TPwUcP7d-ho_p4IZKBVeEZ1ZRSZ5O8cOaJvoAVmw3ERcQd-9se6OpCM3FI-WEWxr-CifT4Ki3omhwNLR5yov4g_zo4DQxAVFHL-4WV40Ltt2GUgoO6MLUOl_lSdS7MUfHz-V56z8_y27zci00_fpBYaGw9fqQhayVB4VpQfpmenzZJqkMeUsgWEC4KVoRiHc9lGpVbnwoO-gVX8-_CW4V6a-ufo7zE_YLz4F-7QeK0sj_XSWbXs6Sb3jjrLB2XXw-htLhZl7DWEqGJ1f4paq2zlxLGi3bdK6Jr_AT-KMEjGlDhN5nhTkTckShB_sXFWv7SE-u37rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VuSD7iu22MClpBEYoNC2-QVb8jyEEu3FkufgFNxilK3_zqFr5OQKOovMhaYGJPmiGi7JfLmxxbrX9GHgwwchM_0_cL01UD67WBd643se1AmyLETymzc-OYpGfrjvevlLisLSEpIGgF6i9zOeLoGwwM5rB_RHyrV8kcD06pmJroeEyw_d0rhv11UeCFFz2BoLWLfevr_FS9TUD4XD5RAxRRlZDP72frSBfbdLrzuBdNG8unsptB_MA7YlpuATMrQhMz1nhuZQLsExFWi93v-Edu8R-25LiDAo082qrHqZILZf-TA7tx7xR1j0lVChkgsx4uikFw1Ac-PNAnA1YCfnAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYcdD-py5N_ANCGnx7OlRubuE8rKGolXQzk9CFSW1Qa6PJgAZMFi87hnuNSGMDxgdF2DxyuZSTEFIskIaJLHRyNzNeCze-rxmXwbbitD4gdzQ3-wDr551gLB4Olf6aoTa1Tt3sQ18YGIaFw_s3lwnpGmWcWjO4wqcyB1Jy3z7DFhhrgCHc4df2UtOwkklXfFf0QepJO4i8_DLbvktT5MyLwnxjuez-LlYFtMr4Obe3X2C2yEiDgDnR0-ez89pX-qmxa263bg_D58lLROPUfHwFdvvD-zLJjvrXNj_g9cjkfh72gMN9kQeBcfVkU4F64wEF7F_axHmjx2r0uJgQLl6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NbIgpGYXs1bX3ryPTNkMGXtBrhYT1421UjRT8cU6oVHXXDP3l3JAd_0Rf30JHdgd9ShOlTe7b5ha32-Eo95oYAWV8tD5QE_ux0tEc_II5bZae2ZZ1YXAYYIqtjyyQfEA89bmn9OJVnmCT9xotjmOz_5ZVJG5PefraLV-D4WY3oRpsh1AtB6X9vaLLG0HsDmOnSYY8u_V6WZwxmQlIB0TTodUN50HJA3xzsnUn6PkUWup3UmH6Ule_35tO6xJ_PL4dxX30zS1ga1M8X0lpM_KurInXn2fPryly9S7FtxsBnW0AsOTAu_niWEATdSg8Cr1Ck4nl9VqA4p9cT-Hxwla1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LqB6qZxPzp-m0ye9mhxZcSE5mgry90eIpu3RTuRgkZzJ7ARysqhU6_ZTO87HMSrU2UShAHQ1pG-gDP98Qqkvz4FQ_WkJXm_ho5ukZp4vDSKyWfEQSt5PzmUwXq-qM3TJogPZDQc-0tM5m8X0PFvnlVkWME5Pv8GBPKxWGptqWznEVP7bnNOF_f3SGKIDlwWX-Y0BsHo08CUEOz054VVMCZv4c2RANhaS0-CfI3poOahrAx7Lxk-bBTs07iPMjCYcQoSHbhXQi-Ss-0DLRsURM2z6e36Jz2qe4T8aTKQvYqtpmfYT8qGucXljfkPsYQxFK7zxhXzj47ARLk1R-1_uLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mRckRe2OjrjExtzltefPwIrvwoC2pjHH89iWqaxP6awp5Xt1N6AjW0E8DHly0xqui_oFxM-KrBi099OK1mW_v-yWDnadoZI0OAGnQO30Z8Hpa1hoz9n1B-uvo7gxY1X9fAyzTqxwX-bNaMXek34n0MxqJ9WWaUhR5fsvV3gsvlTiXRXRL7pFLpifILCSJdMhBa4UEWLtg1LsnrpMA3TLO5y8XiDNzLobAR8Ey2lmNBKld24Op7OI9qlOsepxoQqAEuFHvcPp0jvOSBTpUTW_vIxuYsA6lH1ysX_8-PHDxrXGIrC0rwSWvv33Ql3kBI0RPPic6XlwtdrQcRkwy-lamw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNl9hCSYkEDFBSNfS3v77E0R0z9o3NZBy0yEL8yBH0-zrojMRS2gURbpFvUWArv_w28m5Crfqf76Rt3W61u9vJHNC6xJb5GDCOoG9Mr_PbU3rf0HpxzdRgQtSjYRvVKE46UrqT2Cs8YRaNBWEUZvenXzSFIdChybox6-hTWkH1q8jB5lCaQ01fsxCwT23nXgSlV3YCGRLdnj-TuSqdkQYm8gIvVcmzOL3sOxgqyPKlNHmCDWkLgO8TQ5ZSbhIFygtrnNwouuv-Zmi3GzRiEH7fHJ6u_aA-9Eyg8xNIypH7BFUFB7KUp3jpepoKbQUqMxNsYuEXaapNnv8_3Ov3anPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQjpRKkN-cWiw8ovUwdBDHoBdK0V5TMrCknhyPJFF_k4EGad4M0H0FXzBeIbI1Taw2aM18j8Y0SpyI48FLCefPWZ3qzHj_nExcYR9Dwz3e1jgrk_VW7ZqiOGt_gXvUB2BKppZ2M7F1ZLtqxwJ0RsWHk6-5QqEyZPcRuMvhjlj3cum_r0ioKjqZ_KPJsBwr1Xd9VKEGfoL1_6jln6fppbi9GlyYs3r6eDXNy-PkrM3f_C3WM9BXnDyIpduIxQVpw3ZAraQFT3JkcuCyn6b0Lm9K0uas4xF72Eu1YwDm2X7HVXWY5KCbf1mTwJx_jxcUhoBRFA8V96xRY4F0-Evcregw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJSecuf_rL1Pqk167VlXGoFktQHYnjUYv_kzsC5ree5_fVT1q8svSeuoaJHDuKG0o7DavccoK01W73FN8Cmw9nP0SluWjaGJRb_p6k7ZjlHD4-PJRg65q8XT_8D_y4PaOAxb2UfWDJ8UPWYcSBw-iC3qEWLD9SgS3_ar6DdDTSmtTIpkx96ShD6q0GxcAZYLJlFjSDp6St0W5QspjQCa-JE73kBhxPud36cRVvsbhRY9MoINmt6p8p3AYQECMwH_PnDjzugFLBwV3LVq0qClI6ssMt0gO9aKCFCdtxMHyeTgCXvG3B8hO_bCGlzKgqJWM0vrvjO6lrkuckl9GR2k9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jtCmMGzly3pzAABB6Pa_TzAy04D5Sv8x1Hy3qHEtFqwet3OIhgeKggV2WqEMZruyiPVaRH0XGNFufZEald32wAvJAvlAhQaDJ9hydm8Dcb9lrIX1vL8BhfmMOwEM9_OurR3KJu5R31tNzlU5K_U5CMpeognm2HPm91FEdR_Ug8WPhgMjS1AJY570USfG407MHlJizLLmlXmDjA700abjQ7KUUIV_689gEjox0qDD8sI9cYz7ixlhmomXW9IE-TYisegW6MZfPuSWB4gWA6niqCLN6uESovBbY80k3kbHfTs4qBxR0uXFAUzxb719WDdy_G5sKT83FPVlbGGdExDEjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dV6xNd4CAq0j_K9dwcREPJt4J6WWstIdmIqmj_gP_jpRFrxtMZ7doksu0jvP2vLhN9q3qjO_fI6lU_KVdPBXtqGw1C9jDUHkyJv75LOKTNTjQuVrKnq_8Y93OA4Gyfeq4bpovRcmjYA9BffmAkLH1reApqOOiICAwPdG5qpVFXVCcUjMClSIIByK9OoUrW3IKoC4WmmHHAD_SkhyYVrDB_XlSz8rxXqpDn6dcAQYb_GGjOMo-yaJWE_JpsNnCt4WFTRYoBOqsavOTF-A_j1C22G6iIGdVLCBF2xibsz_is-OcJkTrVBPxKFmLcAMvv5Fpfm2VGnrE48FzZe68S0Kxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rio4hNF0CNwm2U_PSbtFR267EvVYdipJfRNk0viCvkDHxdLGTFUyHpVhRnWYeTX3JxnnCmbwr3O9vDjqbEiEKHp_fayp5ex72Ph3GHF5PDqTeSKB_gYSnc44KIxbNgLe23wN3nazC54qfIirkLjz1FA8aYsbaRGYFj7KEhj_z1v8ERrv49hqD7XqQ9vA2VlsLZI3wLi_EzmUILuvpRipIySwLlSaUwD8acQPZ68T-6lLCOcswQ8ryuqHFKsGEaxRV4mCBec53I8m_n6p28LQdkK9bovOgx28AporF8n7y7eKtebT9uXz3vO443kjHdpoZf-AalDqKwd6xbeG6HB2-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o0fYmSKIBwMVdz8DFHrlzgxPExM3I7jUyD1pCa8eO0bE5lIAdLncFiDKTCA-sJtf4pTS4bFSOnAZ_aLbxv-_69IPVXmP_Bf9LrzkXyMukOl3iWhzs1dRxtGfXtcBNCjYt6FueoUQ7xZP0SDY0Nl4Ln_zIjmOXGodMVkCJX2g1qNBidUU4MyUR40LDkN7fJhwAVmkt9PbnRxiS-lgly0b13EhQQF1WuQhPEum0g-Tlft2BT_xAKDGf89VRAzcvMbKluVNkKctl36euI7PRfwHXWM9x7VO-oVIdUkN94hV3c8C0HDtHDGfn1pnQLravINABWuH5ul8UHPjvXm9cuqU9g.jpg" alt="photo" loading="lazy"/></div>
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
