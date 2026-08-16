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
<img src="https://cdn1.telesco.pe/file/NGp9OwHF56Jb-dVPC_9NOaDE6CaPtrQ0LeYOVM4AzerZp9fhdhfSASLLuH8dLn6i_mnay4Eu9ZdpZ8HTFqiFhu_667xBYl3gaTP7Usrrb_kZGIsZmJWBIbnb-tebVaIO7MEiSyppicrTd_ZU5uEXWtkLoO-JWAaOaDRv-MJoKpEkZWN-S742-wUAlDfX3wTLVbzRvkf4n58WSNasADi91LOoU2aoYXaz9Tv5EMc69lfGCAU3gTGUk41ocxlpHIxv1tYTGt_aN9DjU-DxUVq0VMM79PLB_uY9SHxtrEf5rDoNDOnEKpoaG96VRZTjEMZHGFGIRcA-lTdlZz0W4_Zbtw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 20:42:15</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pawC4ceWoUWzGQ86KM6-E529kXMKdWLlhv6gQO0tkX4T2gAjLDNhJShR0A8aXoDVFojDtMtt2hZ9pS78YO0eDGuNrSzzC0yVP95tPiLPx11Vc-eTsGHi_NQmIdLMNDNe04koFvNjdze6IpaOWulc_YSrgaD8VQaPL9xoUBZbNxr8qlCO7FysM91kpRW9ntu0jZH4LVrzjO13ZboUMHfTWPSGgIt62kBbs1fA1mIwpulP8fxoalavrQbF92wFw1uxmeJBWfIrnxjp5mgrmitU76nLDwuZ8K_dfgZDKy-NzxVtJcVyuBxBdXFweeCjRWYcCQKSxPXb1Vhtd8_VSGh3Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eav93SSuxl4L3NS_c24npRCTKycFNCMzMHzj_P3nwZe-7yYhXbrTwrr-HVUd67o5dPXqYxUFhNBucon3_roU3uiVYYFOqL4Gc8WGKcAQYM2A5yQgyPgMBnLZrCfCoahmvoPXEboTlXRoM0ZnmZdSOplmJo5cekIq16XVFzE0kMVSlMelMh9QSqn7ZMSnuG285zjjqrekKhDGgI8Myk5Umv4RQ-gbv1r-dvDwJqsBPTo7cuGyVCDI72r3AeVGQZEfHhMHZ-dVkp6q3kLHgnuA_zJWiz4WzgBp9r5L15KE92EoV4668z05iJtmHUA-u7J-LWTaqEU-gG4TN3G03ZYvaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=YUlt9w5XtrCsE5k9pFF7CLW73crlrTJcpHSPNPyioO45WlfzG8DbuxU1A_eOyDjT5rmTGjCKl7ZYFLDwwQb8TqmuqaU8ZgvSdwLeJ6hI1o2mU3z4bvMJTaj_2PL7Ea58v4LliUQjna2UpBXfGPibrhrfLp6n1_6r_Q4KH35A26EM7FtVbCdLqb81d7V3SMcu9fMCvHHkqVPCUYZIIidVHTytfwP4Zrp2AQodV7eRUwdFArnfmRB984_4qii56hVp5vlRPemIOm8YQsYsPErQ3ShulcOIzd7zCI6uT-8OzRqtO6wcELZnxKy3Milps--pxacn0vOuTJFDBIUgCQk9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=YUlt9w5XtrCsE5k9pFF7CLW73crlrTJcpHSPNPyioO45WlfzG8DbuxU1A_eOyDjT5rmTGjCKl7ZYFLDwwQb8TqmuqaU8ZgvSdwLeJ6hI1o2mU3z4bvMJTaj_2PL7Ea58v4LliUQjna2UpBXfGPibrhrfLp6n1_6r_Q4KH35A26EM7FtVbCdLqb81d7V3SMcu9fMCvHHkqVPCUYZIIidVHTytfwP4Zrp2AQodV7eRUwdFArnfmRB984_4qii56hVp5vlRPemIOm8YQsYsPErQ3ShulcOIzd7zCI6uT-8OzRqtO6wcELZnxKy3Milps--pxacn0vOuTJFDBIUgCQk9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QjSethD69Pet0qxchV8UhbwSA8wJzgpsTPTfFZxifbyEGoXZoJH4mGwAKte_e6At0EbGpvMnajna9ZdDcN2ATz-ZaStmAW59xGPTvpLbLFqV0ZiJBx6A_ntMZ9v5cCdJRswnQX4ZiLQXpvgysuxRuJDiB5v9NwUqXicYrodJqQCARqQUoF3ECHg-FigA6LmatI2PxOK3p0Q2sm0_k5OKqDaWKvueyTZdb5lZogkN0_dSSf5lVfoCGGinnZD5tXwEoCWV9bdco9G0ZQ3VN-0iXPe0NAk7J_tuQGKIkEHnsiS04XXjb0V6eGOuB44yDWtGdlZrVb4nH4d5yhyBKy2EuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZX-yiYhdlzo9jaUiTLi2TJOxh_kMvpWndfIuApKGcF3DL_JLVshBgDg-YH29ZnCxeH1Bh6pwZkpVfGt3dtFMnp5uozGEVGLC4hRcPagfp3LHafmZElmy4dHYCXAxzrJN7AFYy2Is8JGWO59dV6FX1UZk6U3ywNc989mcWxP7C0ljrHLExLhz84BPWGeH0Ya2GyoInLOF7i78ihfyDtOZtY0goCjZID3pR6CR5DFsQNE5lGF93_1ckwnMncWOmDJkWXh6Uj2f7XO0WNCx7tK8WJUiFMckaC0gVUHJiN9XdAaCUZneRM5UCTt5LNWcaWUjngp48_n7_a0oSLULoOc-yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VWSMpPM1KjAKK4N-WQYhr0UgaSIoYPLvpX_66A5iMK1OAQTlotdsfqzcr47l0D_Ki0b2oWZkor9bBdzxapETsQUneVdzwcm4VSt7Pd6xVgobfPAfT7QP016HFod2x11Ie1UU2iBwfKcaaDdDgaMonDti2D0zB0x8WCFIm8qr9nAD7eOp9NZ3ORkI0HTHo-y7aGAKOW_L3f9jGRgqOJwDBlqg0rgfnme2x7cNcjvVGtWwNlIaIe79eTqZ7RwEs9M8Vyw6VSiZGBid1C0y-LXC5PCSls2_fkn3oU-G2s-ZgUS7O2DeI8XI9p5MAr3mD9rKqmkc2TYbaJIBOobCRxj-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/phBejjwCz0En6544QddwoaONtBOVVWwM0KAeYWmiJv6zUOQgWXbtb4EmjVj9xY8TgNBU_VocRGBWYXg-s_Ctx-APpnBo-b6cYFFyAvJnzpnHB0iFetkE7SBuZXycbaacUi-KHWQipMKW3eJNF529fws5dnHCBlDi72O9HZcOlhndfMTFZ_jC7C4Cp0RFbhdK5huyjV8EFZlAcHHsNcMCLRz4IfOIRY_M23B4rq5TwAmCBfBK2t9J-jH1Az4PchHklB_7ivZg_1_vgLf4MYNZNHGzQtBmK08AjsEy4nYk74p5vbGK2eeuBi2UdoyIMdoBfxG8K6YUI7vLCltKckgCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CL37XkBwFLUyxmkeOV7xVQAhEq-QZBusSaSx_6iDl5p2wNSZ5aqDh30Zpf6NsabiqLyos60pBtRNvpP24uCwggZdUoRt00HUmrsjdSBVvanGHM9m4qhTrU0UCsQPDNk0pjGaHmHJhvLYcfctlxtSghH5Xu8ShlZ9A2cNzgTPAoWSE-sgAm-vHZR02S9fSoOuluhJpGbjjduuv3KeHAo9mN19Qcd6Cp3rcrvF6V3HL9jYJQIq3AXH5SbIHmfVDnfLV63f0dQFY3zHjDuARsKOJcz4XkIwyc85SOeGVcgmqrWjMjRNVep5_hxgiveW85ZQgRmlPNEsh9U-0TdW7IehKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ttuyOY5iCqvcQD1KDLLzgMebJ04OoXt7nWX6r356ux1gxBSZ6lIrgiCelII0G19asmY_rQ5dJKQFb7O19UWeYiIJ-HKSJNlt6LRqvKzLAFILPdiTUtAleBJNPuwSb7bAPajI_s8NA9ZqXHPhxeUMOUmOt91AiWmQCl13cJygJ8A3NShxft93sLJo8ELixLnmQs_XKpfMoAC1kBGNndGhpoLZ0FzQH2CUaHBN0NAQspXoXLZ49sNLyxNjUsz5pdw4JYS0kSMTyIdNlVsbhn9dP1JM7hjrmSfQorYe4_eJJxrUvJukmbBcAb3znGjNh7lVULg32yY_ww47TH-xOToyDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Po1g0roVPrHDDRq_qeJ44XQut-Rp6-XL65ag9P7k3bYBzJU4HWMT1UFaYGgbUF8VbwxfxrCFk59O3yc0g-587CcRz7ZPHZVVM8xIKsI2qEscLNYHPefYWJsBBldRco4At_QtUMMQTwVC3GH56aysF0YAR1jXwNNNLUOV_LC_ORFCqVKPcfi0e4ySztJ-kiDm1apTQzqOFCK8cPtSJ4fr9UZmt5X1ioEbpEfDEBZWWqVPMXwUxFQCiCzLYvCUet5LqD0Lik2L6KeFOgAodiQGc-JHOdcyjWPggzrTG-htbVtQd-y49JPeMLlZuJf8OeB_4gxy_u_HLkGU-lio8baOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o7QioIitcthL3uBsQEcnwF-hrLxzw9O3XYZ6fbQyzFlIacaeZbVx9MBkFms6JD3-2z-IpLfP4GgSdWzp89p_2ap4Vy91YEyoTqGBXDq-sO-NnxvJbZUr5HOoCAdoWkGNmnuLeGMI-geR-ZTX-Se8bCOYWwShXKd1wC5x2ZHUa8Z5N9En7QCJga6ltTp4T9_VrRnLtMK4043mXDWiU9MuNC6OSlmYVjwPf0M6csIb2fTIqn5gS7E5ZNeljwvhdBR0hbg7m_EYKVh_c5EZ3Z_ogZzhEJPlTkkjhJZUUpn3JnDGgbrumpYRW13DMMpnMtLOPkLAGddDe_lRGwSnuB53kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XTrdNqiTIbazX2vTC4yM1pbqJySUrHdj8POObGWcqSWLlwPUdgpc4pL5ni-lT5IIXwP_AdlOEk337CQ3y_aHFrjuckx4J-zsQbMWRlpO82WHVo5Z2orcFK_rCsPxKsQySmfafQJcOM-UhtYqj-lc5OFE1NTXOy7DKvX7ua6rdlN12wD7pr3GKKzmksM0Qgex75od48jgKDPmsiykKm4oer-0aUHLgsvczb1peDQUBGpSTvRGABUrvv72heC4bRKWVRnHX3o5zFsmFprI2T0BNDN6vSTdvGqQnSfQFHidjDhBAxuGqmFmsKPg8JdFvDtDLdKl0xY892ZJT_Yn9o_biA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mztvr_3wcpfgpwGBeKGS08vPaU1I5iNQpylPHIPaewcM-f2r-GQAL2S9-xGquNzEQm0HBT1TJKlNibdlQLqk9fJab0xDFe9TSRngH0jUuYPmVCCOQdHO7HpGrXOMoJ7Dvq23Otfx2KKKSLjm2XiQ9JWpd8lj3jWNTsXrjTL7S_R3cQjAIV_3klJGdaA0NQHkB3z0fjY7Wlnjfr3bCEx7AWEbcJV4VLDAzyZ1UvasIHyjV2xEb_rV6xPwSt7T-ve4kSz5Pujcrn9Kcvqx2qCnKngc0xgi1OeCnBx0LJgVw7TGdfEAQGl163aVZojLdF_zQaI2GTuGuu0HoTKmqky8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fb8PLH2g4LiN5ufY9rogRzLDNk7jhXtGKTw8zoDwS6QASFxccsySt3U9UOBTXKzyL_VNEqkLItRqehgj0OyElC70yu-MS9yI9LVsh0Ay1oIIEVREkP1ecCvryrOWI7bGn-tiom33B8PdxeM86tsKXwdDoakC0fo0JCy7yugpQW9sVRZOoVXptPdd5UN3_MwAHAPCv_Fk-CNw8qY4ti3UjNrtToF2i_5smSROxFpslyMyHp8SclkscTDPn2KSeuwkgd58T3pccS-0RqSwTWg9DkN-OZjTWU3l5PnRAOV4w6hkO3_NBIM7Cd5TbST0QG6xS2OBU0hV7WQU6n3oi7zxsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pk90vFsc1ul0g0S1goon3qvJKmqzZvUZG__b6XZWYixOZ5okhMnryurhtu3tf-kASMBl0lVVmHQ-iai6-2yeWzGb-Fw1Q4JxtNnvwiYa7VWwRgrUbPY0UUhMr3adVlzG4pER_czre_dR7wKSP5mW97TcC9oewEIv4cxkOxWAduuW3nkJVmsmuMqwHy78EfzIAYravMLr5w9ToKMTZ1Xk2zGvfFhB7fHfhQq5dDb1kDqC0lItDZyYOHb35KJC8lOxc2fdWGzskmWgBOfwDiXv73R3kU1uVtrHgcz0o4Qhc_m_QYyZdqujeiyVzEiwP3dTmdLJA6JJGkAz-vjr_5GvSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MxwngZYEN_4FzQ1EQnn2hKF_aXDGOoaWhZXqzMqpXBjiBRvmZRss73Dp3h67zv3tLMXj1UHlsYVy0xcTxBHKJdC-63pSgVakE5Tid2s1yIEjjMfBXpyW94upi3htoLPYyv4EP9TTVfj0L31uDNot5A2YIa4gWUjpjhQ1Ux_-Pui-fv-jFrsM4Nn5act6FXVu9hpAJT7Z43r8Q93Ep4JN0YIY2jLN6FTNJ-y2PKni8W4ThV6HvkIwMV0uqHbvDv8zTHmdKFBNh7EjH2vFSWn85_Xjrn68pm7y24U2X2_FVRLDnwxg667VOZj-_-zdBDcssxAJPgNZrrpk-DvBofchYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TrwvvGFBRIIMXrE83PYjjVC322LqTUp1ebOT0yTKa9m7qTk8Qzs-s6vswlkXW7Sd-H8enNBqzvar-_OC4AU4LnroByN9ajPZwcuyo_qNaulAD6SDEfZI-4sCeSU9xnRSQVFZntXIW1otZyF557MZBxXrLY_wj3ln3RnrjpXt9GBJqxh07rhkb29VXoSWdnAQXacG-pLAnstXmivG9sKpKI3VnBkwFpvCAJE2nCOa7vlAfDqH1dG4PfHF1tWodTfuDitQeZp4VJjzNNbMU6LjGKnPdiz29np7wO-Rd5UDPUd_S7Tlf_NO63ojheDp80Ca9sroepgqDGikXBogIHtd2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e-FwAVaX1zIW4g3imMLtxuDYxB1HPtvBoLWfc3tjOw_xZ3vPTG3ZJCuT-Awu5CHxw4p2FwbBlUGC5qauqzNEZgt48UPVSZRLJ-LDc5OFKBFtnfK0kSNnBJtxwNt_-AdVKC1kFEP3kF7a55tuKo3Tlj-mgrASOMqcOblK-eq_COI0m4_6n5F_9soPNK-wy3c7inW05VYJbs2ma1Jk8kUwXhzuj8-bDIUIplY5p_lIdPBJiwv6drXGIPjzfwXkGl9hazdXDxGGEaDndnKmHFMHOIIoMCJzSmTsgGBXzSzR99Lqj56U31apAO2_D1T26h2RGDwOVvOKBI4YKe6F9AJ8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GR0lhiuDHFg7i9YXrOlcnwdRihgxquGa_v30tN9lbl5_mj6LWZKsSXTOfD5kXS2E0gCYzdTEnoA1BgKbxyGQeSI5rtpPnaxbKXs4C8GMIvfNN2my4UTj1cMRChaSjwteLGumChA0zg7zZFKfHnJ132lLV77x0b13RYXrYzfIBBOQAPeadGiWWZQJhG54SRT0QWoNaRACcnYPdFTRepx7YQgKeAvVJeI82Hk1qK1EUQKv__N0DH-fwp1iO1FAbuD5gMjb0841HYDjMv9pvaLsqw6bTu-IxsI_JjToyrr2tSmxhRlmX4vePfgNy7npULm8QkaqIzVo4k8FmV_t0PkMfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nhjp1tItY-7Smi97f6WgSh05G1CXYHM4A5pScIj7cCMOCw-BDjHKGK6ke3dFfuK2No7jdnjDvkyJs0p8rkDQ4ISEbbk-nSBN0P1TADJHbMhOdLxN0Lut1KZd-0xhFW71vLKSULKIJF5brm-wr_1ctAqLsiTBs12afDtmZEf0WjuuWYSsUYLdLhfwOxeg1OFvsftbq5A0ttXQoq-w2AFmwU-CYO_KkwhphuX7_FjTlqX94JTWvgRfhdgqqtp2giG7nEyu2JaE9tjvLGoG9_Dp1vtdzUv6fCKVAm7LdyyOLBW_hdZfaOJ-dZz1UdOAx_eLdllYNBHSYD2vkwWlO-t6eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kKVuERO-JuXH5fxyjfyLTknlY8Y3AdHO4kd9D-RVUBPiCrzBSyevgvt2c0MoBmYF1VFsV96NmJ_fIv9iy7G2fFiR0bvNIS26P0a9DimkOlVK36S5MGdzCLfQgqeE5WI6hTY9iMqyvNHLQaQFCBMqPFg63vaDo0Cg9iXJM0zEVylpsg-uTTICGA8G8BLIO-bGEAoQHRT6_-sb-9fSy_pRMer1pSLiGlrxD7dbhhOuo8pxOL9u4xRcyH85KtnulOD2ID1glse-roJMSwWjdBuh2yJQETysSVNcpchEsmMy6629lCIjF1C1XwPxzOFITlmVJCmQv7NrX3nKjNeiabs9eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D5E3T98sAo_xthjno8T1qNheQvNoAW-yrycJlgsW7BtQ0Cyo3WXMOiqRCvzE3TWUj6o1BbTFkoI3RddxwaVEn-1plI8YPGSgXCk_LEWpJBJHjSB3ENQ9hm0v_mMVvbWnyEKLkolGK_O-RdgTi0VS4naRLAMX75SkWG_11M1folVR5ISZ7q5kJtu0poF5nbnFShqJbRoFGSc3gC2Pd6cYRn-I1EyiWepp6wf4UWHqzFlZTKeXk2WlCSh3GwhGVWpwKfZwtYI06kUgPAOyHeqsTgiVfj4_nLTxw6pYtkvpTJTm-QKRO1PxymyWs4DBfiyEFdgktbBbDndi_7NFiS1i6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ASVMQ2igWp9dtuErpd_KGIsl5L5k4ozBizte110yPjKl0ViBxsHUomX_QJgRJ-Bqmk8ixVtGfqvPikj4w9nOfefc2fJVqofsNq5pKwswdFFd1VEeGt1xKwzsMsN21dpKm0BcoPLW0UV4IM91oIm7ASdu7iyQXXFjDcOeCvFGMgFSJejdkg8qkNkeqaAhxCzybWa0md0GLNAsud7szFXxAIkkBX4Fp9_h2jefaCgP7jZT5M_DBSApWVSyBCQc1FOcupF0GWZr_I-YqVmXKBr7OJdmsRyGIEN_ER1d4hSuLF8G6KLl1EtPzCrbcXxks8UUNQ8Zc1YBjP9JyCh_KZ61Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sveHesi1vx9vTMXvfrBEvOxJ97Uz1mCJJISaoFBjdKVYrmaUQLmMq5zvA_dBCYVlk2LFVdo1xBZv7wvwOIYF9soj7CKnv8UQI6KtlNeCBg0rfaNk1egv2YafTL4m2NZ1K10qVe97fuTFrFK6t-RUazExiKOjg_KM5EZ7_dfzjqcyyJ1XlKUzstQENd8vjHvSfwEyATCoZ6kfqTA3Y3gdbxqn5x8T6ETn0vSmdiq5ne9XmLAUgVDaEvkdyCCeOEeUR7iFyS7i5lZue1xAa8lKTLiSSg17NPhlLOb_WoBLgxChhESS4LE-GVLwb4JVdrFVwyaXTJuzCV9EiN8WUVvbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rTdmJAAF_2jyLgGbhwBH2JOd71qtphJTnKizcZNIACA_iucabkae989aeGjz1p96uFol6bTJeDprILmvw32WReIkNTsRPOaR_DNQ-kEC7jiNwwJ9hNTxCJ_50K2xjFhkuZP8ORSvQ987tVvPyOk7PJipmaLpCL2XtkU3cKCjTJllRalSfFONdTY8gBtxWblDKfywvpVJahadQ7NElCnH7S6qleT6jstvMrEcTptR0P9Sw3O9ceYWcvl4hbdWzsFHQv3EmKxWirLuKirus1SQ5GxEz-LqyrxRx81QIYt37wKsIqG5IAoxBzAiJz6powmzW43G2fuZhEuW0XFJYMqseg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rR3xj3xSROrw7AAsvI3ZZ_6EdHz-9C-pVefnXlzSaIyPZ9m8tdTyNIlVFHBy8XOA0gJoSKAgpPtF8sHUEG0FRadqCMpR-WGlBmN5zVdvfvaL4bkqPdFhJQkY1NvsY9A383zVpabMx8zDuphRDwdwUXRPbJixl25Iws9pb2NzXrRCOYalKAG3vUeU7D4rhfLB0SyHHSAUh0h0RsfW-eJC_PfPXwin2aQRr4BxsIOKW9N_Wu87t3c0CEszjy6ijcWxkPVRyB9NeKb49npNfETmWCmSQ5axSlugdM8ddoUQPOqmM5hnRWluIynVywzPh4inv_NsgwYVwTMZV3eq8hIkOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPEISV_v97tmzpWApH0MjouPXV5Wm1F9SrMkkFfU4WHZ3IBXyy8RN9O6cCauzEE-XF3bP0a4aPZL9vq2j1rUPrKKeFFi97adjpHcw9n2WCw1BWYlf4Qq1TbaZz8680TdzAOFpryrlxbzyVrNXzfaTMX16wHxVXZHNBpjVs5mk5JXxTqWipNtsLIxAxTaC1esNY7-7rZ30MvOqYRt01SqxhirW-5utJ7Wy-XSIsQHsUsOKaswt6KLRm70t8axxboV8oaOh3ZWApEcAAgPjd9FO9A53fHYmNetNZBcAJFJ-6099sQ6MebWWMAUCcdFkjDZXuH3CxdniMQ-6uuFTltHpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIm-NUHURLA8c91dJ3VYkWsrCLPEnDONA-7b_skzOo8Bm8PvM5YQKtAx5c43hyBS7agL7mp8YzBQI91bpZK35aQhNToNmN3-LFo7VKEDsdfGdQetXmro2pZKCSy6hqC5fDD6uQem3JZxNp5DF6OtVy_hd44E_peFSQRoZP8E0kDN8jTPeQrrt0WcIUetVVBC6B1HcihTRcFYbzD1p3g3D7zRPkLr45cEoiGh7Dy39sDA5R6IC0mIlN4X59LKH0a7KzQgHkT-wnDRfRo9KiHM1iERO7KjvyrUbHYKDMkzw4XgthE1Ngt1wx73duQ_cjYayNlZcF_Hm56K2C_2J43Dew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eNhdhrIa8p3CmW98dH1jv1-mSQ4ZPcf4zocanGRJMPPY39cKVIB1B3uaKpu_nyb5Lx8rho1_Dm7LPvh4Js1F1Nz41G96pUld5KS8ZAN5q9MTSPsXccPr9DNJEA_jrrkiyimz-NkuNo2aUJWVadvyI0NwMY_9BO6iDbaBDobNGMUx94fN78FkleoC-39Rf1CyuFJ3aVHO6dRkdLvqRejCokzF2U35sEfFNSwCPmQNv9b4grlVZupUdDKHJjazeea56kFp6Yyzthj0NPdlqVM7qyTv8hRYC7b5SGq31Z3XZ9A6i7-eWMK_t3qKm8K6by1-eFkYTAorHu6-pRln0xGPQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/urvGnqQnjBoKZQ5FCC3x9Y0nMEWb3oY-a1KHIljIRsm6prOhi1zHZE1hpRO63r_Qs8sL6i8polMysybyHgezBvAx9a68xP1mlmFsqldZTAQfGx6rGSLRmf2FX8JHqXW9T8JIC61bi19TQzAkLCONdOejsRPE_BOhbRoF8g7eTSuv26RCWzdqxJ47eBHtWDjBFIx1XpEyndYmPsV-RmGzXHB-PvyqZMG5zhOv4cM8TU4FwawasN7HRTviNjbTdsQmVigz1g2y7ulki_h_7rc6W_D3mRo5LsTxv6qmuhUjqeM2YD6ekkwoeojb_QtrDlAvP941azsudUeCRilL_nQwMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OGZle1Td2O7-neJt7hmR5RMtEFpWPPM7ZPNWnr4Lu0xY1NW-jsp0Pz9ebLViftVjj5F8kHksuU3TBvdLdEXALJap6w72nQPxZdoxa9HfjuIR5RPv07gR6IZFjsOuUGB18Bu9gTWtauwBoouGvYKZAae55NtZyw6EedsY9JpwF6r3f5yBxS399Yp2BBnnSHCWQN_5aUuiD7eKAS49B8uQlnnhnMuUeBhYPYQ9m90EE7Uje3qwSuL_Tb2tRhnuqCPl65Vg9ODh5GtBM0gge7ndRNTmzlvRcdsqHs3bdYTDoBp5jTg6pEyDftbEhQbPsKPjWQrYYb2W2ZEtfRSjT3Llpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DW2Bcwpk5vDdUoosrjAn6PBoXGjBUslte19XKot-6OvdEoXsyjQ5Bn64K-JIMkFUXfsvkkfYdsiTRbEsfow91HfgDdyweznTQqn8WhM6MrrvMQftDB0fKifSrdufLiwATFPX6O3JT_V5B-YSfB8gpFxprivkymKp9TSo8-QVwUcmgk4BG0C_mKpMWS6aT-Tk4AYMbQiIAY8nMnPG84TCyjMd2w82iIhy_ZJUjdtc80i1jBaZcBr65MQYp0qNGYLBiiO3UbPQkgwFT5_ghiWdxMI-ZQIlMj59Q_TL1P6KRducg0Yha6kADGClZDOMBTLYUOiifpPIk_d9LHwjXsv-XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ja8EKESnWer7MFwL21Ho6-fqZjezzlc4Xvm-aXDt-5yhbe4H6E1e__J4_nMSUGeAofIDJuYELSa4G4z0mHxvAOQZa3VCF___YkIHhrDfojgOwPj3fOPoQ5g-GXEN7qbolIHd0oERCELYJanxs3qon1CUjK30Eb2xlvHPaerKO82sM2UXA2CyVsdGRrrHW2zFyxt9c1Gz1HUFI6rBr_tEZv6UH-fFrk5yNoXo5iuFFNz_Vqpx0-ZmTnR_1dL45_qvoyh3IQFCy5NV-bMocr3FKQy378LQpbKPJ5SkojHPuGeO92MC161aAgbTpMNTLNHQ_xCrau62miDNz3BIQNBQQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k8u-x6UrIe7Hz-pmb4X1ShpabxTS5Al2mHek0QUUUiQcE_8H1kilKSubsf_ZOL3aqzYtZd2scRDtlZz9Z7i-_huJbPu2-4dnrK3ns2K5w2CBb77F1CcAmVI9CKgshrY88ptKAJKWMuDPlKQafRN4lZVOq1rvhjr8rPajcNtJB2-gwt2kzCFLfQ2po3dmn_X_7WK9ACQB7V4Xljy3h9zak2iHmsafZL2zmKfNPVwb_qNlIgaGsEif_sRLRAAQ11NzPUDMtsGvGT0bVPZtDn42zu54lYApReUYkePlWl4sLm9KOY7PDrbp4fngTJCaiVZ3nmGbZ9FbQV6ZT3ZGqNvypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rSvI4RaZfET0752pVM0sMARQZb2bWLndoGHoQMA5IKNzdFw4OC-KTyOf5TAP2PByh0HHvfPRdGgLbKKRdbWatE1VOfZnoZU7r0J7BOGECmbWqWR6slV_0jgaLZJpmojz7jCTTPSowzPwcr1e1V1HUaWVUamz7mXVjG6dEiVLq_2bUMzHhuvpJ9GGDNDTZq-92smy6T2leBt3sJPCUUZeGzu49qr4HSfw-UZKisuFOHWT3cuiu-gWbe6jepw-Wm7GwAf5T_wgpkiXpU231rbeDR3f-dmDLIKOCpCKCLqJXSyawkjXFsi2t-2DTfhGkJ5aTaZALwrL_YHIh4kZsq3C6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mVzeQ4kPi3DmhgT3fdJk4gyfyi_Mi83scd9jtmyan2b7fqteI1oYzis_s_zrro5u7VaC_mYGtHUqWHw26k-dr1JSfRSpGwpcrcTddbsYx_4lAIgQEqtONkwJ8J_Vq5z1opggc0TbflpoNA3oT76ymS2nlcj6SmcfwP3Irf_Kf-Y4Z9ce8dijsmabzpnpvy0KbHwO5iL8XPDLudX1mgD8XKWad9BUY-f7sd1XL92h3EmTaFmhr_14DX6a0W3XyCHnjmO2fQJvZp8FrKtQlAVP5wZRPqDZ3pzhW39tEGZdmVUNIeK_hYr6kPq3BTD9LRnPmdvrgAWM77YM2UfXEHZ8OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sUDwo_izx3L878Fa9p5EHVVpmtkHAlGasxXR-qOGUnuaToNbrchSugIWgNNoLyqEkdTFMAOiuoY-ZsJgAKMJtbt3tTvU5sTD4YStb6RKRXfXX08uQtUst0B85QJoDIgQnzOkj8_RRGzRCduYy3MCvqVuhsYN2e71teCb-MLYqj6KJrAq35ssvFop-nUth0eAVkhI7FeFkjDbcl6I1zDaw44W38LbjBwWB7BRFphPA21Lf9IPhxTyvCQh6y-PUy680RyoveJ6USnd5lPZflBI2v2V9qQ-2Xx9m6bYCVKNn7S55ulsmdXzNDk527F4bL4kw9brDLQPNhBwgt9iM4v8Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DODtJ9B3iK68iGiPqdotK6EUK77KNr_VYqHHYpIVO6pGCtTeGVXmLs1EVOYZSACBTuhV89fNNWZ8qNBGnyu5Jpvofmsx-k0eDJGxaSH9tkBOqORR8MhX0PNvicF1WsyGmykYstFKOrAta6VfiNBj1-Youj_2eh3wEPCfyDE4vrr1iaU16igNm06P_rX4pcppNTPLafofv5oamNcpKo8eCCMdQMdYIEbZov25xWDYKZy_tt7dqlYCZn6415ALhHnGobvV1uNHr1kXVlaXE8-c2QuIYgLdajePUrjzTluMWirkvMdEqSg-iDn1Y7SHbIeKdSfbYTRscazTir6DIecaMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NqOsdMhIuSivrOEAbUN0_jRLwxLbYteo9o5JlHMpQeTTGgl3UNGveU06gJQbqK4hb8cvyWvJ7BEbYPqJhGGYoHSHpL8fzLVZ8zwt6tMVzWDM2rWmegHKjZnzF2zQQ5vjUIlDbI7zrc4-HjrUkkN9b5Hnpp394A9ksrHIWMgkknYpLOv7XNvpo3Y2QtoHuA6Qk2bYSSVWqZlXnnCD50bkbZd296x1lEfX2YP1V81XeE3nHISj3rrzHAmBLPuL1pqSNdSsmTidoI11FNoQAutkHaV7dAQ_xNk_jmL1_y3lWw05OGbkStQDUliU6wSia9nHbZw6sSM19FzZSzONnZRHrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uLtM0KwV6C94m1yKgGL1PDCVoVEpmmK-3OOuBKNDEuQmD9fDq6JCplftfF6yZeap32gp8GDR8qipAE4ucFIsKb1oYQTr2eIMmvDNoZyZKo-ifbiDgMHet90TKeiO8cY8VlUGacRGhMsIo5sYkcFOplgtKwZbeVH4GuocI-82pqSATIba94MHMyE-qv0CifXqcjShQzZUgOYjYn3l5IWgWBcfl73WOB77eqCYg8HiIRacG5dAsL-CUbDn_6hx9K81Suxl9DBjWVYWoL92tlIY0tR0HA1Xo3U1McAzSJ2b--otxnOQHsItymEpz0hV7Mo6rwpESPtsa0s6ewzalCERjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rKPDu8jJt-Gp50FRF6LSuwCiDv9wAce1nypPDaw2TTceXG4Co6tayxPLOAFWN7ctcgYGkO0SrE8TxaFOCLhKaDLSWh9ks_rrnJuT18_pP0iSQATr-dvL91cgIQxSYuAlBQ4M3XSOv83T6wprC2rmI0VV09DuNIiNLA-2gtUmaQJvzzF7reJvehpkFBUWAXg9lORVTWoWfIFUVbnsorlWeKO4Kirtn8VkRQkaNIBRAb3FRRRsiO3j2mnkip6qT_tvCf1Z4ZfHYspb70NhuhhwWPgYJ-gVNt5bWfbmZ5OozFbZrrb8RoQGR4BPROtkoDL9N3d9F2lKef_Y02E6Nq_WFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IB0i-mI-12X5AuA7yD9CLoXG3GY4W2KPHQvJ4UhWE0RKYe-sQ_kYLyeM3QpUK5VnmeMYSI334fuLOXn2ybW8cxHBzveHrCUwl9-z_LmLxpPX2gM3RxDvJ4BJHzo95VYt2mY9waNdd8evxO8ElnIEZO4LsN2oUIDqbnz2h24kCRcCFnaDm4yMYfvi0OLwmhCbZplP8ozZBocFZ6S3T6i66WS1H1WXUBRmmeX0GYi-Bb38PA86tfDUZQbshL1rvcMzcEmgug0DznQJnnwn2tvdG5dOasWJ-vuh5hvHmURe-eO3kn1yrXJW15VhEdCpu2BFJykMDKQ5mpieNGzI0KCnZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mqIzfaa7SFmy9smkjv9gvl6L0St0aegTl63Nls-o0ZsL88om8US5zTryOyrm_2TSZ0h2BROXZf_-L6nVPorj3F0icyGIOvz5GdYezctwtDjv96jBaqbhIoq7UUnW9aKgMbfVNW3Ai2C6hh9a58uQHPcko9BR_yea09zsHAke3wubRJJl8cNzqNN_JFyfBpDK8jKA3_KsCtNeWUPS2dqzXofF7fzZCF8UtZqAcoe1j16teRUGm1Nuu_jbIC4o2OdyurElgL3Sltl16vMbajR9YIqUsg_XSkxqq1m6bhSEtq8FOhYx0BuldNRDtEBP2cumyAODDBeMo0zwqh_3vnW6tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YXnjuV9y-nLTErl1NdMfKJ7-XzsuC8V54vEL3o6BYW3EU1VHU-zhGfjFekBRgmEI3HqDCsMAiyLiTC4yUZeIVnYpSYL-r4tILe0mf20oa2Z7n5bmlFS0ZMPdM--UnnT2nyprenXu8PWbDgCNSzxoPhXdclevX3ehgxJxH0q-aamA4OlMWXSkN9AM05JXhWs5blDE2b_TO-umniGJfrFX6Tnemi6ak29THmEgZr2-k5-08xhTVzmwfDMEf7RjOCU16PIEEDZFQnG5tgKp6i39cXCWmNkp9XGGggBzcVlk1SefFk58Tnd2gIcLbZps4iBL2M5kQxO-cS_EwB6M0AufIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUU3fJ0Ym9XE2dAS6brk4aXdSAyIGKjN8BFbq8oiVDJuN7bxXN6h0nnz8ZPGL5nQYhOencMtEFZnYCMdfrFGYI5jzVmq3Y2ceflYJsGr7xQ_PS5moD-ej7WJqntfqB-TFwSrKF5vpkjL9rcGNcDUuYnHANp7IRzncN8DIss66V_LoI6bJtPRgtQ6SHC_4Kp_7x49zNrkDnPckhULu2iGgPZOWkKp_NqfM-ZuH9Otgpyh4cQkfVg8pi7xPae8or08sz1Ni6UZLiMhrwF74xL3J2U2sBxOFWZB85hAuZr4EaJ4ZIcfQSFcksu3TDgwGqGWf-eh7nfczf7h6Sdz6ToqCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fEJFyKy4ol3M-67919RnyI7hgHfGQmMdX2UnaaisswtIAuLFJBkgASaYEvuafp0RP4m-m8c1YlE_CMLoOYJmNMhjhk6vWC9UtlKYmGHaWcgoEMgib7vWWPpEsHCq1DRU7okmBd2SdIb8YnkBTQ4Ug5NowQ4-k3LDeUhSKEBflsWYWrm8cSifjH7Ax22A26SooPw7IUP9UpZ84gp7sj25CHsgPJuSYyGBBoKm7vxQI08z6YkgqTR9yoUgY4Psq9ewOrkuUlXwBCNWrz0xOwcmg_HF5NB1yslZN_yV06X2pFyiJ7BttVMSqDMQgqSw9XExiqysuKOmlC0cDs6C0TiQQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqvUtqiIMsaK3uyzIJeSu8BOX_QjMb0sybx_s8xtZS2Zv5SeHLaCzVyipTXnXoq6JubpySUK3452AeiDVFBBWQMdc6CaDlGAqKdfnwjrSPzyedCJ0iW7UdnDOww7NNQ7HUtgW1ivxdMFVYxv3aeY3LAc0DGRefHggzmfjqfq6JTH9HLlCn50_omcbXVgMpQVtk5R28Et_ibPKv6D0220946vPtqwKZ868_y6O_4nc89e8TlKq_z3dmMxTimam_OwMT-U7v5mxPJBuchxMpBJ3pw2rggVS7fm0L0VV9iXOO-PvR29oDk79s_WAZHisrdBsnsQWsJ7Ifk20GN6hstUzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mH_zXXTfW6cPPm3I3Jgv3V0nQP3s4ewMHRUP_EB-B7t4w6TEq0rCRDYBilKkwlPszH-i1cy1VKgI2MWW1VRYx85bCt8qs3Rkp-bsKZ8Dk-HOzavoraLggqN4bXPsCD1IuZNUBxYNQbO32av_tWJwG2rxxsv8lThgenmKSpGMBfmuI8o9pI9a6gTgwe9J-MLZw-82nnQKlAEW4KpYv6Zzl5U63vfm4JFL6VSHjA-TR-mc1MRw2-OvGrObnf8a4qeWTSrKnKYoBG1h2La83HaB5yN8wWJInpDk_cCxOBsQcMOso6_sMg2jscA20Ue8Jzqb0ZTKdtveg2rci5QIdWi6XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LgMTJH6sfhLJtFk3g4Clq7jJbIC4Ho1nqKa8-fc4K5QJhoGivA1QDcXIpmjarT1VyJpwyMNaGW9KOZfDPvaMsgI-J3GlPw5QFbCvSf-zP0GaP7NvCiMEv9vOYfCfZyaRdSX1C4kvSPhEoNUnZkrWw6NrLbYc-fThr9TMzEhIKpzdhNEzLh8hjPFO0UosfqcNytFlpdzzBPumCIUtIqyp4xZvLmHoEUxpcfyyulupA7OG1k3yGGQ8-2X2SuvzEE5SCZvhnhkJDF1poZkXkYuQ9mqxtamDEdZJ6h6V9Fmkv748_bpOjp6RbyXisIsFzBL0U46tUxSVLDCK0SmYMXBrxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sz5XsYLPESG9WzrheJYYobqfdcN9moNNY_nj_VYeakvY-fAvfaz1qQdIOZyJNWMAE_M0R1oOYWp-reqUgu4FQpOnZqoFXGB2g4OyvmTBPur7eTdJyD5HJE2Xz3o4g6dqHkeCW6w8-GCa3yd5P8-RMX_XlABa-yDEQ6_pVtOU0YuhhGh6MT2QyZbpI5v8w4vg4bDFoV8n-Y0L42xJampSfwgjoZCuw-0lFJA1dJdqBkNBWER4ZpoMI0v-RFCjcWAJ14mMOJOaWTu-aJ4_de-fFMJpCSXQHZu_kxaQagnc5mkDI9ry-rtOAe66d30GjHa2TivciyLUi5e4kzZvJ9De8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqC7Hky_zTEJr8-6WfT8kP97ASUgo0iPGjN2qytMcr8mDHm3ZwRHS59zs6rA4JAW1xNHOOjjw5hbelYcCV0Ft0IIoAYoEHohFslYzB_GLv0TUFQiq4xl7EWb2tOYDkt5Rda5sczqhwTWPGz_5KLHFxTxPOmOqwY3qwd7riucdOzRiDKN7eipdMA-nBkLeBXbNZoKSwee4yVguhORYR3YFZch0RPa-mJAOFcnrsvVixNpB_ukfvXOI3k348Mxxd8WE-GoRrVAT7z2ckWGvnSK81H59yq-RX0k_m7NBMCX_hXOL3yxhG-0cNbB7m9dH0Kt4ajOr50Bmmif_Z8uL9qqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MApmdIYfPrpbsyhG78b-t6j820dQo1F5LHi2aAMaQSvcofJt33zKeXjukpz9zkF3p_qmgCyUuu3BZLQ_Y3bSs8a0uoKq70IYrvpQdPFU6R7JwFQgX3r7bq6vQZTXJr2knQdnsXoZpVt_zWRB1AtYKoMqa6grKGnN95AHU_ocqvcqmp8AafSOUv0LqTCn2zHB71vUq-8cJo98RsHLU8sxyRJ3lFKAImwBq2KRAtG3SbJZc3XzXqRQmtNmGdjs7T1NrqPglzONc9ZIqY9O8Xk-X7Scu8FCvJ0DbLxrRduvxKQXtDOAHR8sUk7_T4iQlkQ-3s-bB07fWMA6CMGjBz9GuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EWtgd3mRiH26X5h1b4P57DZ9tgg5daeOzLVPkTO6mjrnW2TdoKjh0mOJCmmSC3OStEKGwn3xSaYgEsDNcrh3VxXXhthMvoDWfPQp6cmhlXGyvMOueBc1jIBjgTt9Do15tZlFNkekOJANFe6U2ECe0LBokcA4tDYpO77z9Wo4vQagUeX9RE0Jvfz7zYs5-lHj3LRTpE-ezLP_qakgdJfWV7M7OVw-AfzpQ2XSTIzWC-ur_OcflzoPUC7r3Y1E8FSoh8M2IHfUCU6zcH3IsSR1CbpkkYZKjAStMugbE1uOWSt13e9nkpGXShZsIR6op8iA0VPCiWMWgcz67mYXruPPIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZukEu5zVP8kzFEWNjvLrzyWlxcL1BLDfPyXhkPglbigKyrOskOlz0LkCTuzbmYeIaz83QoUUwS6h8-hJqjUc_bzS5fdnZXLzMCMk3c01Txbh2Wpmz5EYAHC0tsVG6-Y8ih1-Jbvm7GuvTDgDocs1b7LB81RsX7SpDgRkuGdg5Vyao6X3IfMAg2liBmFeU65kcdRChMOcRsLDDESMu-E6taKXKw7Xgb5CMxol_px-CvdmhSaohGBsQktAboLyuZA7xymXzZ8YNa7XqA0DwWAJQEnjui-QH2LN2b46O2e5EPnVxCuo9Rlrl5RQwoTN9trcowTsUQnot6oliuQuT9GnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b71FwT5GvNxpH217W1DD_ols8-aaQ7nX0fLwlCocOnQcRTZyL_fNkGmgwJCWORf-4ATqp88LtfXeqSRRPWS_s85YdsH9yhfLVlMaButZogMHaSsTekwgoVhKOX_IbdlgSbCOyqc870uIxHBtwnlEHWbfk59lZPmYF2kGO4mtlrG1ArL_oPUC6kHVf4k10FBSiwJPf7DhSGR4lyar1S2esBJNUwXiP8ahur776KYZYLjdQPyCpRhKV5Xd39FzkBiCCQu-IAagnej_6UkRruhKWUtCuG_iBWHF7kdscSTzdzsHXXl7xmDURADvHUFGu7X_r5bgjfvb2LeCFuPsOEHNZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TzDHR2g9Q-8NNI2uJfXMohKgbr4v9-lGmY_XJKBGGA-d1N630FP2JqzxrTPU-HcfkGx2zUOgIVvtE_IgtFhZ2vDhXigWqlTZ2sef0Xpt45MzioW99EqxgnI0DCHs7BLICOe4BGyNbHnetqyiaMkQTzYyGwwLv88w85IzzkIIzeKemzflQOZzp9icn0iHlqfE7Q6wf5l9Pr5xbu21iOy4UNcMCv4-5zdLL563C-JHRmB-Qwu4dLoAm38puAWXLhEQY2xJSVq0mEu7dcEQ9jjqWxG39hUx3v_aXfbp4L3MXei_IuNvCLyaDuUm5RRSvGZYsD_x5BOxmtBvo33SW_OeEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TkVFtuVLQJRdKJV71NdSUdrrTV2tW9D5Pr-U-BKtQ_wXYVmqlXS59eCIu40kVNupTIttehEdsytXFkINFoSCgRX7CHXogDrrGabhFxUlsCYK9vSKF_dfSfpc2VRe6g0HNyWhw-zhvpbizw95c08WpXyIo4ZVsTrP0od1oXPdEn6CoS-6L8fGMloS12TGD9kraGZ-jDRCeCAYurtwXgUMiOD4NuH0k4o1JnvySNYTxmyzfl6VAmvABxJwizrCZHSi9gt7ey1h6fzoS6FqGHGN3n5n6HClPRRpazAsXV-ss09uc2Wtq4nm9NrD77YYA346xbuNyr9eLbF4S_haQV4Mjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ieNIyQhF7mA751I1iWT3eQtvDcpuSfuGlMvzCjFrP2oHgpF65EPm-0CBGE1DJC8LWZK072fgk9OaltIeclimC45H9fY6sYcWcNvfnPdEtJpBjbf4ZcdyaU0M00Oh1uG3KWb6NksGDDXoCP3C6OlZHxAXDzKb8GhBuCSuNVGaQmNsxF9IqAhoPQebx8fUeWIek4saBtj_R-Ub2_qh4Vxz6fjf06c-lpsTKGIteYCDPQqDb6k54MNhLGylx_2cQVM4ftJ2WaQnYYMZR0Xtm_YM0o2RoTdNmJTrvY37i6xijbnBjVtkjpkwo8-juvL6VRHfxbqz8jLeKZFy8yULpMQhbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KhDP02NlVCMptpvUYo1JEimaQWbL4JuBzHkqRG2djDlkMa115ZMuh03Ss44iJQEK484Cztz2zp7GTJN1ucmwTt0qfpCLNJu7SfMkTovlZv-X1RuBM3zi8dB82WwmG8Ls-7nHXlTz3rCLuLR5HliyOUjP2RTFnCS-9Jim7ojk-3Wntwgvx-oXvtal2xkl-_Xg_rY6aousHIrSsO_VFfToL9i_SJQNIKbEu6nHEFc9U3fmYlVtscJGNtsOlHPN6JECjf1ry2UdrDJXmZ7AxgZz2YkF4ZjUjjUB9Dr39PtUFBXFM2siNJSrEA8uxnPaayBPA5B8Lq2XCVjedJqo0ccHQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GUtkdegssWCeX3dQv6baRh90_uUC1uRcSwVai2e3FL6PWZaCV2ynXioNnn73pDWoYDhSBJ1T3GQhTNyqtNe6sB5r3AHS3nIxafw1IcgAwrkemfllzRXk9LCIWIV0R-s_g8lMZ6JMZbyFGXuD8r0lxyN2TheVQXi-G4sreUTq_ixUcHcfcyiczl3pHGRoB8eB6-UsxpFVrqPrJxRl3GdAC2bgfpKOTJzwtjSZ07pqzUl_5SbzE6ueX2C9nFcOIm0w-fw8-L7tV0iR5UZWV-Rt3kDm66rzy6UN-zSFu09YTAFMh1dfb4Z9FqpXaw-BK3ILbxyAnSv1jYWdfXKYMTa48Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VEhBN5A9qFR9Z_FsXgOwLLCYYMdr7Vv1oJ42cdJwxC7SpRb9uQpxUu69YAHh-7T5mJ0-JNljkjoUwN-as_EHYfD3YR-bcXmXUVjNNsAVYnsDYQsu07e4Wm6LiCp1U1AeW0JCjIyIaruaaaTOehk4gN8ZibliSRiAncFX0aFnqyhl-aUf8slywv9fN2EkZ5dNMXMqwaP8Gb0wQnxRJJHyj4OWKLCnMG8cFsGcPq4lITNCI2ZkqkfLTzMI5ImQtrYoWOAJ9yTqy63GbAULRZjDDg71atazG7zeOYHtXjnUlhgAtd3QLNL-E1p3aeDNRcX8_3fs_uzZDTdq4cV6J7-hcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/joV0j-rBTUufJPqfVTxciDOW2R7fzSIkmR0AHycmc7MuELb9rTbZ99Rsj7XbDDxW93VCS1fr2p9vaAQ6pgMh_gAewKeGVPv0LBbGyT84hReXpGqt6BilZNxOYJdn_8Y0h-m5iAgoFxhJwzDrxi1SMVarJdJ83Rf1qIl-NVEWMrtr81pvUGZ1tzzdR-g5oSz6RVnL3eGtrpWg1CIMRgNRQDO7hGZWNcIeHOWiJ42KjSZDgeyqFzxOcOANOLnhMUnlalZFKbar-YR24_2dl4kCc3RBwGchlyzURvwf2VkkayXzPAa4iYo7HPyCJGRuzfWug_B-C7NMm2pNla4y7z_VFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmWvvHK5N95_DHeHi82q16LZkEcnLLcRU_l_XzWtDu-m3cEWmdqsgbzJ1Kp3ws6BKCvYWC-pRK3rTmVsQkf2eOYrf90KHGObWRP8Lsd79Sh4gtdiBXX2Y7VbNck6pCYc0_cEIxGoxrtQmCfd7HkAGs1vl9yRfqT4mLCvnSTjoUIRx4rvUTZB6aAd5jdwQ2ABQTObB81oCxM_VSStaqMb0Wpbi0diosMS3GnHmi9G1H5SPLOSmGRhxYZEp5qZhOyV6lVBg6KFQo-Mb4bYMoKnFEp7g_z9kGAKY9nQs4iQsfKx6vHW5DvmOxPCCIZzlDfLCSRr0m0sbpRDO8-13O4MRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EBfokMzdq6Lsf_r_xlOm6WIwXgta_wugSesw4MR7B-GanEpJZUfOeDjTcZb5Zqg7rr2mVdCS7W1I9Pq3Up_Pf93LWd5qWymoHiavufgNfYkfneOvT4CopNOx1-5w4-4kA-WSrdmRdDWeqTvl8S-_7gPvzVTj6NaCQ0H_jUzJRUGWJuavZ-CkmN2g3bmQtOanQMmmXZnfExsFLmMrAsolFaNUk3NUZYIoSU2Gq6NLV5ll45m1eutCYuqq_eAD0ex08UJPE8fCGqdBJIPmPLvVe7x6ovO8_qc2rFbZugdzfuziEFa-xyjnxy4ojIEPH29UzJPQbzGgHUN6k9KQ6PPNcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b3Wh3Hb_hMOLLNDFZQDLwxqNrlkYQJyHRINPDBIUTGkxK8I6vmeV74TKKLPPMBl_tPKDv8SRieHrN8pxOjHVNCCNgRKoz4OHdIwLqJ4MlIbpCxTZuGKQywd4uggSnW-8310OJGgP5sZgfiSb-5QMEkRGx93VrD09lIjdME2xTlMvQg77hTB7icExZZJ_9EP9hbQ0jpA8wLYkp6HyPLU233Qq1QQuY-AXyC1DGNclHNHHjQL19mXQ0vF9CKwJ7uxLnpTSX-pGUWAQ4_ymIKTThBnkNT7nbaedL_MB_eoC48MzcdVBtMLJ7TTZmyPR_yfvttjQGhT8gyL64-4S9XXCpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TJmUuM8UdgHl7e9N1z51YaQXtvaluQX_3bpy3wjc_BR4f1eKfGm9Gr66C-K-vQiSiz_yUgqBYoN-zMdcuCi4OZeYANrcKEf_GuzpwVHjnwgfGVxgEKMHIPiv6yKNBticGgGP08OPBUrBtp3Wh8XOROEc4Tg_PH3Wa2kRf2hAuXVKdslsgkvfq-RW6-j8fb3iHge9stnlPN_Gjf9Blf8YYfuxLglVozWjSwePMd8KBcCK99Wdt3nywgAebL1uF2RuQUhDhj6fxTgxKDjbH1_QbK7RgmoRVoiA3LyhHMrFP8vWQ7xjrhstQmgH5tCEUHaIMPjjxNXhvVm1NsJ0QMkOSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjr0Snb23wEEX77zSpyL82Ql8JwKowXtP8yMarySu3xDZ8gwC1zQjaa4tPLcJotAOP8vs1wb7V-e_2bO4ZuB5D_c-UsOQ1GDHBSJa0wOXk5emjRsW7Bk4s_VuDeeZBOovNQQ8LwWOUNe15Xzkxh7GREZbJGPkQfeET_P32OMAcbDd6xkuSCa7mjit74nYtTlVd9Fd6-vPWAEIcsNROgbXJR3G0hChYaaqOY73FYlAcZFXUCtNPtPqOwbL5JBA2OOmqIVoAtCigZEG32UFThBc9iiKjn-tKazcecvSIJhIL3HCaeqaEUwsWaFy5_NKM7RjyyzboAclCsysRD-dlmOBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZwNCTeEXcRC1_7iq8DG0Lx5Ly3xG08ZBwwqQYoqjLVMl8SUJkH2akJfHJl7QmII1ek6ukhyR7q8UfW1tqx4IMX8CeT-qJ1hC4Faj0svabIKlFZljgXOe11YU1t7NpS2KYENfsZHx6tKvWeIQfQ5UHbWeZJemMTqBsVJIXnJZYfYxZ3n96rSULEo6p9Mx3zCcgTpVz_TaexMM7aMegIvhhTYH0wutXL_mbopGCNogUO4D8wL5jfhUsjYS5zOoCRGqQ372LkTRvhNtUmnaK86ZQw6EDqjpYmPtyZv3gxPHYVPAYYrvJ2dIoMcJKlaby_WplRVOzPx1KbV16GwGs44Riw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWMYu_jUmVGk0UUD8jZIMj4jzIrw4yVgOTpg3PUnn6wjkUzaYZY-ce-8SbZVMqfgGxNY-ktegqsaBmqcei31p2jHOAOFiNgsWw_u5pkkuecWihKEhAhwX26BoV9jW08isn2JFJTgzmsxIPgQ394t4VZ-SA9PQhKJ3rYW_T0NldiVjnFb1LC70x9PpnikvQhaqqqjWsZ9sYlWkw0uFkMgWkxLjPqp8kJKY463Y3teBdef6cSWJuQUPHzy1RLg1JOBHB1Qwo5Tm9kYgfOOxoBeSrPfzj6WvoektqBj6gR5PqfarVGGcHbTxT0iCT9Rl9wWMcYQ1sr55vOjAyVk45DA7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
