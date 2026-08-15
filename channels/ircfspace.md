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
<img src="https://cdn1.telesco.pe/file/owzh1-RYE3910EXidIUh2-9TTE0vRgjOh1ttAmVnHUtVAkvvvtVC815l6SLY1K--dRW8nczfGmTjH25V2akMMAArruA3la0KhwyjlS3PoKlTwLNV4fV3A-myITQM-4PD5zLz46QK5AGs-1Bbn5t3YjnpySlBmpYSgpU3D1yXOyrBpmwOdQSbOTWIkvdt3njvVKE0O_CXze0HGFgsGr3FiDdUrGZzsZ4XGn2FAPM75LxdZ_nHXknZUMKH4iOzavXUE0AZOxgC0AhEVJzvaBjEE2WQ8cs38c7srhj24jIHl1faQRC8L4Za9i4GWp8Holp_2P2ZaRd7CpTamyYjeqKLAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 22:23:19</div>
<hr>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G3CQzP5J8bbRc1EERrbkYtIGJ-ZfM0oi5eJyzxpOJOn_ex0LV7aoNIuEVRwYK65FY0p733g70vLkEuqAB-0CwEyfwHUPE8tIM-gIlgFZFlwWeG10eADR2jtw-GQLhQ2XCiQ_b5JIMpKotqG3MiBhq9SfvX_fwKu_eF6LEuCck2zND7lptneCt6DBv7kWI8FnZliOoMlkMJKBo7ksI0QvRdP-pTDR_cQJ8-s5XM95SdiEesWDloKEbriAhOdc72S90XUs4AkKh2LqPqkiK79ogM_vRdlSzUR4Pw2gTRMAKVG7vtG9TjBno3TmuCc1o3g9t9zhIUnAQbZFBZrZOHA0rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LoXUNv6tLNwpsHlCl7mN0SHmGNNFYTKEEZxjgPaQtWQMt37QHZv4_gY1TwrP3zQmOxXhw5zF5ZLraBPuB3muNDWpbbZl7-nxLdWkDdwgtBweCV4Ohp4sOWv_BZXDqVSYKFK9RUQMOP6YF5Ot317GoKg5Jp5nW0CSzDqCJmTNqoHzgvh_33Mn83CSberfe45ZenAgvY2WIXOdgOUp3JrK9S-9pbsB-0VEFhxMbNHNZ8BFCP_67XTLWfCvbh5M7_V9wb-VwSUaZQ47743Wskb-iyqx_G5jTcOTfyyf1YviQ7je0wwE9JbGkUfRQ3uKU40kQpzRdify03hFltoCqaeRpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=ks9o1XfAzQ71Kx0ycj7hI4jTnpLw0_1EXFwzC7BkRHGJPx94zTfctRmJgyWG1zKec4n5Z-DnhtbGxmGgTqQD7jR7BjYjeOCjvNYN3TdC-2A50HEi4HkZ44PRr8zvmz8rc0POKd_9_EKntD7f_R11X4aKU7n41kvdJK-aEIDDN5pTbg9x9GxC5d087LKibAY47VwcQ1U20Aa1DGthJeo5VxKT_GJFCy9XNDPibJKuSHWerDc_nzrqRDrkCJDkdhn2Ope2UnsA8jl7aDYLmBkgRdyLMQF1tMQMag0Unk3UNok0VsE5LSZ2oSk9htLdUVxhjXtG-GJ6QQAhANYrYKUjgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=ks9o1XfAzQ71Kx0ycj7hI4jTnpLw0_1EXFwzC7BkRHGJPx94zTfctRmJgyWG1zKec4n5Z-DnhtbGxmGgTqQD7jR7BjYjeOCjvNYN3TdC-2A50HEi4HkZ44PRr8zvmz8rc0POKd_9_EKntD7f_R11X4aKU7n41kvdJK-aEIDDN5pTbg9x9GxC5d087LKibAY47VwcQ1U20Aa1DGthJeo5VxKT_GJFCy9XNDPibJKuSHWerDc_nzrqRDrkCJDkdhn2Ope2UnsA8jl7aDYLmBkgRdyLMQF1tMQMag0Unk3UNok0VsE5LSZ2oSk9htLdUVxhjXtG-GJ6QQAhANYrYKUjgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eHPHfCkxHzv9U7wnaiUJyNrPbexjwPIF40x9NC08JRsjQK1W7uDwzM3eliM39gRuxaNH3tsZsMx6o5rurIBMDuAsUtun7HnN_Jg3VUDYFF3r0_Htnf9zfq_18cN_-EY11w1mJ5lBY2MRk-Wq00Z9luv1vD0l0isQRAbmDR4TEYroHhQ2oI5uVkNqCMCa7E3BFV4mqNu9OguR8_gBclb14aBOxuVUNGTsFn5w0blaB-9OGbwppG3fIQdX9BYxHn3XYI6ntXFOOIeQlVJS6ISv8doiihJEOqXuozXBA4IbZK3zR4ClHOOMnE8C-UHQUkr6BPs8Ku6SPErU07zWV_Rk0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NwSG1UHoIctaWmASnMql1fUqVDub6WeDoaaU3l6StPk1OawxaewPWd0k1RmjrghLnDbyRlz9jp84ZEIjz-0wcaMN8yPSktJVGO1-KtYCnzUFb32p6FtpCiihXV2yhzzfeea6b6jFN7XWx5SFTg0to4msVfWiHJYSxYu6xyDczmEtTEYP0DkdomF8SnjzM2jqd5dSxlm3q3lQo8I84hE-s89GSIBnEb2Osi0Mh0Tm10drBQHtfmbaNujC47vlkxnEU66CsWpl9HJYG7Tm-ClbCmC9kT-ZTvFkDIPidfcgM9O9P7s-foR9ccrrZ-wEd7IVf3h6Ox-ygWXXlQRbeMlogQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vP12sJno5Lt7iyjINSy94Q1quUeLHc39sMwMV2UVskcPXmKUo7yC-vehwhNw0Tluo2y3bDffsvA8jBXgn4Bkfx8bWKi_JkT4gFtjsMlhpyhRFKEBwfEgDwcflKJ9Ec8SuYuvdBNYUptzhCMYYA8CZWgwNxYx3KBMEoZIlZokuIhvsAcZ6nKH9o_CddmoB8RusRMW7YtIR1fBZLVJhJ3DTocBQh3KHntObvOyFTHrY78XiV6rKbOvPeSsrnpCW4cLc2uJmFJSHH6-MFz43nl6PMoDgquDnEcRcRcWfiuLumQIEJNkkLYV8jaenRXD9f-DpONYGM7xFtD_qZ8OSA2G5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oW8tSkr6FfI1yGlcU-RvRQry4nr3DI1m3ysFDBPwfUXy5OgUZQEB6Ne6--86D16GJdVzn8Gf8IM6cImnB1oEYotbEXv8RoX86MPJmIQVrx7TY20TtPYFfXpFfY8eU-A1tyrPU12WVyiJqSlgm32W0u2JpHiS5H_1sj1wB-xqtVzfEVcLlEEMqImZb588aMuijrJ49OZiO9bJZHhA1Bm0hWEC0teAB-dJfJTu29qSxAetE9JkO12jOs8rbHL2mtselDiwmW9ZLHEfryc1NknPqgIAhJDxcnurdT5BHsA22gboF8t-NWkWAEsizqaA13FY1aNwCJth6MCpHf_EGWs93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDIwiJ4zHxToIeSV-m50-LfRNJfBOTgT2CJ5U00oMemE4HzUyYVrVHFMBjnAF0ZfNei3sTLRkU1iX3GYVQHbUI34Y-h6HEGM0TdBJUjvj2a0xalzR9P2wCRXDo6tBgoXmv5tCOolCWxZoaAuetyQXeTZNBTdoudGjJGa47SQxHqPP9NVLVUdyr2KlhOMv_j33t7asVuVOPugJHTKwmm66QhIpTCKAB-CIMrcDnPVx38lxCSlgPxAZMvOivSmcNt-4TK4sl_URN6MRMISkAQM6ZJ-hsc3umsvFPoFKePefih-3xraiCKS8z-eaHDVADU5nlvJl8ZDExwegytSVJi8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXeYOe8s-rHAZRflYlJvuqGrPpxCVIpDOXCYVCx71wU_t-uKdlEfVEJfJvSQ-sXB57TEN4MGuDaaAtNkM4w9q1BoM4wQ-2UJJhcS9PeMFJrIc4VATt3Mw_95ivS_PAt7FhtgH8_atzXIc5pvdXatH-_NREElu0-bmHWCl2a-fhVduX4EVf9maEOIMao1gAOTIsw7DHHoycfXRJWx5JL5hmnFuE8Q5VIjlyw6HlRniWtVQNHom6F0wf1hQJv_TLNNODPyo1wnEdtji-DKDwD7ZQ2MowHX7ifz4KJwccOkDjnZ72yFiAX-0rXbv9q3ZQNCeFkYurWKIHUX6JRCAd80aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nEkdtzdhe7r0QXBNPOVX7G95ZEPjsuMqW8aP6lm1tc_kA2MiPcrk64BWyuZcHAvI-Ks1b_aOjFP8d-qpMUBGO6s0j969TfGhWmUo0XH4Pz5sRwXeUsKCRIl5HCiLTGoFGZBkwQ8riRT88KRClChkszD_yoh0SSo0f67Se0b0owvsz_ZA3ljMmOSXLCfu9bnKhcgpk2hHH9e5e28VLihlo293yqDHp5R55pR98TOTEp9T4nec5czVTHZfYfFT2-c4ay6OdFjm3MvjLNYHvp6aH72dGPGCLXBHCcGHdPpwiCLz6G6ER78d25A5vXrwpVNoxseZwSjZyOZbu4sU2sn7RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AcPh9-ilZcawwr0gtLjNpFlN7pMmmg3Min5eEAzPO8-enrt_Z3ThjkuZAw15UXlfMtHwIbBNTAzv4dxKcMKAOLtOGsFC7C60ji9zJlHNJzLUVMJtqKd3LsGKt5Cvn3uUR2AAsyG6HqylHQ5WmfCV8lXVARaV49sxvuVvdbONHX9Ia1OxEIPGBYPvVEAw4vxLowFuq7GoLRN-EDy9hDVW9-pnhkUivjTaLYW9jKbOvw35kp0jK7TpU33vdZBaMPFW9PvEqDDxVy67Ahdf8GKVhw9kH4O8SBYJErwsJCLBOwy_ob0bgKw3qkzJ9y2ND1rFrDth3a9yzTwI2b2xIsCyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 54K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lbd6N7JCEAd0-a78a2v0sxALs4bjCZPmEk6NgGFjLUHqjPvpefIARcrJFy5j30nAc5wC8AnFiICuy1TV4_xWb4S-1eX8qEoYdXfKGiqvws-LgxNUMnSswVm4NnN65qPsOZwPb1UzZIbNnHXwm4ZjFdWyZoec1akCXjRJNO-NZk7qPPvxy0YpgPRphi6WfAH2HAQedyzx45LQyTUBHlMEKQqJ-31Xoa-X7e3oYto5oaLsH0YAr38qHnb46PDI_6mCMVyv8gt8LTF1HYwh26kRIJv0rHI0yioiQBSM3W_bAl8E7jPEdGN30GT8M_-hmicHbbOviY66UrI0iFO3LbQUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X4ApjgLQFl5yL6yjI3VIqYXapbqqTG_6QBfc3ZOi0eTWMeGTwz9pUc7-PYOhr2v_QiXLwB5Wj6Df3cJywDzL9fv8cKNftMRlLqEpejgqRcjKmEMyTCPQd_bXd2w-T2Xr-deIa4hfKdNUm5jJClT7rbSHodpu4dNsBxomGs6C6XXszpIrz6QKg_DobA2DjMq45YGfEUCQSgYthziVKGQ-zFiqhQUGSEw9qr_8uKBQQFUf2ukgO40Y8dVeXpEYwj_HuqC7oH0njowbBzl6Giy9cM5da9VWt_AnK7qIQlcgfLs81DAp3ZMAoX1oI6U5ex8npbjBXNb5rhitbJVxl4Vp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TU_wIi_i64lCt5KEw3U9SKeKi1QieKYTqkfpy96ZWqGofUY1RqEv5VbqnaJ5F1UpWebUo2uYKlqcI03g9HV_vyHapUBUUkphwmdUakoQR_k_ABPogEIMNR5hAHpM7h6XdFmaj5uYrpHQF4Zj3iN5CleHTNe29nc3Hm5Qnz4FvnbJBvYR6lGkd5UGNV5xXOBDN5gSu4a_gzirwcEuLq_4dZMwGbhqRbLCb-_pEeIZUqV32jICJkDcK2baW6i_P1ORX4cb8xLA10Co2HNEAKkJ0UJm2fjuyHZx28sNAV-o3RsedwrLPbuWeh22THt3u_if7TdDiLkr3Lq19kmppPKW_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V2epk9E65oO4mE7sz_EGsSmaS-iyIXEY6OcALDiFtMapMszxSItyJGcqIqnEHaXEQpq8lneT1f6G4iGlAV82JfLL2RIVEHVU5mKvSIxFLZ_E_VAKwut0h47J4_pjzK3zcGCXq4yIQtNMuKoNO_DajwXKdm33hDts4zVjJjv2p2cgqnekDKjVCSxqQ7s0-KZcEsRdffVCC4keiT2NTkvFQi7RDe4V3zBOUuHuqknMHVGzX9mI9MZSbqSTreDLUN0Khi9ThGx9F3--CoBdtZjysSfYlhoRgf1U-syvYSf7vGa24VvWFl9SWG8XagZw1PGxRc51exy6DsHuTHLjGJSRTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAE9Ok5lRCB1-28qR1DKIb6rXcnl3VTDQxR1em__4gtPg1IDPR6oeTECOTvzfk56LY-SBAR6XCgfeNLRneSpyH55bJoBacCSpb2nhG5VOzIUJEAq1_hb6jwzSKGeTTyARtUdJwlBQOj1vt0FYF8VUTVJz89BPRwe_syx1edRcz-v27Dy-eLbPp9cm6e1SjEXmquHmR1N_Kx6nXrw1KMF_UZOTveVZG911VtWgK6Ba8BBqvV7z5VFOQRQiivsIAVMFd64X-3QU7HL8tv-J6K6RxUPje7vOlMavoGgdSIMT9Km0x9rIeBUrL6tAwA9IGh40MqEM8sMzMj4WJG3Z0d1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jP-mvaz8lOBvHmJaWxsO2eBaJx7xweQZ1hBUsdINTRNBiiBUT-ru-SlFDH0uQ9JP4BSoh1YC9A3xBmdP5oxsGp3d6sNzfUiRKCBOh4Qy-p7KHCblX4UzqNTT0N5JdPnldcxxr_B3AvF2YRQv89Z4o3ki6rStqMei6PNbKZlhEPwFlI5T---BWcTljOj5FQBk4BBtYwZw-w2vWwKdKo3L4HjFGWalCA_xY3OoNAcRYn9pIm5CrhW7GtXBypBoyvgkLnsRS-4UDUA_CKHqADeBZFN7Ifm7vv73QD8p25FLqQbTkGmKanqMc58hYxqQaOxklMz-moT4S1DJQUjH2kYwjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3wKQhW3bnA9JWZTa4Nhb_l_1GqJjA1dVRatCGf9dUVJ2OeP1rHTsumzOZGEHyIzJoeW2L995pGp9MAjTXAbkgmFjEU00aj3keAh1TkYWdmN9LLwLGWHp03u3aos6cFAoVOdAPOjG7ik64TOACRcfQweJXN6fUmJX2CSacrpHwrw603-hzl41IEK3Dcq-5vS-e5qUBYfwGIfxvmiJ-hOifEaQjG8eBS877EBgs4DGrAjul3WOEDZB31Go43Byc3bAk80SkNHfxyTQY3Qo10iJHAdbHZLykdWyZrOHyvIf98hPvt_MnRgHnyu6yPJm8_uJXnibZ4q6oAEYoh_hGE_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNDvnXIMaNeq9kgTF801acMehc5X-bx9nargo29cnKF2rb0gmJapqwmOYPlE-elIAjyYxi3DN3tBk3FSOpOgDAQowBP7nBMwYYZL1iXlb6h9XgHUu0a-AYiEjGBaJoYbCjG8mH0jPDwbwcO-J2PqvcKqjFDWHTNgI7_II6yTi0G13IzmIgk4D4WPdTIgtwXWjtuUjiBwN1qQ76oRn0oPbbW4mvM1hVOSEO4xAF6-14XC8ou7-ShI-wRBb5QF5OxBcbILxrJVnaU1LhcmiiNFY2v1OZ1g6ywAbRnnfcX8bM0tFy-RgR4BHlcvOrC9-MMNrRyOwegrUnx1K85fUBlfSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXNWQZcOxoZfkHo9djx-Nf2F7hMiukIBPUxnOWlqI3fAE8gYldkhijZF-R0QFTEMZNWGjP7ITNZutTUxRXZl1AFwNj0RWh3JqT_ABLe2jkOVlYY4mqRYT4Co6ZJhTPwEeWIK7RcnRvjMhuLh7ArhJijKIC5HBzgknfzXCOrdBGxqpJBUwHuGUvJhlO_rhsifbcamKyjCT0vSV3OU1695VwDykqg4B0COI9S7806TIgBlrUv6sobERl8yTiKsTMs8iOjcqaQuINLBxLDmHDjR7NAwbPQH_mdQMHRtPrBu0cXURraXYRPOobdRuvkB-MQ90HWvSc6mdZUnQiJ3g6DiHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVmPvw8tkukF3PdUF8vR4ZlL4DHfIrp_8dJjNa6CieDxRmextEFu57ZJdVTf34kQte6_GMpnE_7BH2f4WT4qZl2rKxE0o3ABD-MJUxeVQ_5mQ1ytQLbDkhA96ahEqEb0gyuxceiAmAdldYcTSR5jMHJVEZzrKhm52DvBtsSv8EfbYsxhWxPJhnohDK_fwm7JBuAwYsL7-PoDIGE9Ppa_uZHBT_xl7vlBHR7z8O8Tw67o_k0h4f3ijjQaOL7IxJEBa4D3AE7nokfWJze_abwWA9lQN9N_9uQv8xA7ZogmkjHDJfi-kpBi06_MCh5p5MpxRcff5kzxWmM5foFMSuBNRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u3GrKBDR7HkhsSMDjUDt3YkIXHFum8plAc1zydArmfOrLS14TeXnLCO9o-hTxf1gSm5kcgSngxHLEYvvy60SyiN9BmhyZG-hg53FTRfKhwQ58uZ60pyFPPXViclq6lprzxSh78ZozAzcIs_L1GNNAonkOq6xhud6jIUGx2IyUuWR-sFyhYkVE553W9FYd6R4MgSDoREocsUZMgbTuqf44jCZKZiaaspkTkhNfjxYyab6SWRFUqG3WE9igB6NQ7Qr4CJeY-j4JLnOrlj6ZBPI7VaXsE6UlbuG8gg5QDMFFMnGx3hoAa3UlbkdAG24pMVEgGkDiBecE_D31c4T0kYgig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FN-lu-N8oSfDovFTBRywvovboCgOcvEPMxVpJ9yWGAFoRhMyLlI_3T0m56UAOE_vG8d-qNq-5pAXJId7BeiGnJ21kUxto1vkTjmJZyXbRcHkpm8R5evxGJNBLnfe_JlH0vdh0_c20iNhQelODlXGVqPcxQ1jd0DUk_2G4k8vp4S6lCkxEE4E0w1lCE6WyfQJpHj2plY7-BR8EA51KK6wvDEu7UK7hRvb40Lu-poxKU6LH8OQ8dJelOcJuAELqXP-sfZWMrO2cN-CMeSSNCgzkxw-QLusSZnhbSTX8p3djli4vb42NbnwHXIzDBTqs1XQChEYIs1ToIYhxkE7mXBRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H9MKnlcRjXgzrA_Wh4EYfknsMWzp9HJK1sJag5rUTLxjO455NtbBrBktHWO1D-ukArVPQDA6gywVo5e7eHhFpvFwt0m3bkO83V0J0Ljq-AZOK7ecWkZbnoYp10l0W-tX3OShPoIH2jY6sRLGNjTmdXKjKRa7xa8vs2tm1H43-ax9lmRx1OG_nDtICORhe1eBKknsg-Zq2YAgPahf6x7RfxQDhU_gqIJBP0224V26UgYIvh31qCCxEZOdZJKrRZDkdEu0KyXtWHLA8quBXc3XkyvyzIVUcD3FfyLTZA2imgNVnqE6Dhux79spvf2c_hp48O-uitpWFvM6POR7pCMUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oyv16uycEoFHZFI-0dJISPSZT1D4DBUAyDSJjJSFb14cLSK-jt9tsuFxJVJdTCEqb0BJfE-z8lGIs51uFZ6jtzFzR42lo_kde8GQunIppaGNcOcFi4HulgM0U_3SZDOZKZ5BldYnRJcQz6nWTGLbAQv16jkO9UHp8jfWq0zx2MqTJNtjWzwpcRBY8tfi7GmRfwhyohKKmwUn2YHGRZTM8sGYfM0JMSs-k9vzPkgYLQrh4lDrYVfj0axLdTo4CF_m8BqEF8SCbE7JVQ4rxqhwlt4sKW3-NWQ-f770K80InksqPhvFrkBdWb9ipk9UNcwcAtDVPYMl9tK2vJdkOgBTuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mHplbHLqiP0e77vpg5QmxeqE2ZJ2s9xjEescJuel6K2MFeI8lZpUndj6iX_U3OthZimETwr3n1L673cB-_r6tQSTEoKpy247XeaO4YE76VtSzn-uUY0MK4-jphp9X6-HZtvzzLsx1GJbDBhk_FEvwzyMPDNte77DoEZhKwIeChWyE1UfOyPtTj3BYyYCc2p_GPJ3MJr3YUnU8RBHgXC_QaciKnVpYxIMQXacv6iGNPgWlYOL14CI8IbCjLAug0YhqSDxVWGou7nCGU7zWdDxrM_VffzbhztmOxG3SbkxqO4mLjUhdQVWvqpgW2eLEJWkW2NmEazCZfSBe76QsqeDbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C7KOTfdIa-wtJpgZGzUfMGEFTHMDsYifmBuHppgcee08kwAze6oBxR0b-OHoCqHZaaJZZdzXPunIAfysWfjV8Hl2ZnDfH1wFWEcOvHCkG0w2wJganRek3Az1XGZAzysj7w9aC1n6abauoFRjYZVMmQFY0-2YPFUQl-SZA5zlGeAzw84J7APjxS9mv-Bp9h_u_i4z8YTb0w9vBPXMFCo3NvaecXE7oOcD7xOXo__1iPxHt4tEvgA0IEdVsxZpiWNTT-f69nwQZSXFCdCEbzrExyVqVjsmYGRDjfL1kVVGshHIbTNaxfArQG0LNsTvQcCdgsdHU6OfwuCBzn2dbgDOTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BFHhI1sIh5O4mzSeSQY6A4UdUQencibqCx42P-E7Z17izjcxiF19rnkFUWHX3GXap5fafN3PqIg9un-wT4FWaHjnWVwKmK5mX3HM3WVquwDRGHzwq-VriaKS9c2x8sDIsAJVsVWoOW6CGo6RBT48rimdhhX_3yjZwVzagE1ozq8F3472hpncskfjfRtINNJ6zAMs2dFW7zJmy4qQIt9LUIyYIVh_rnkQZJ6V3UrYw0fQPylUHnpiF3DG_a2Yplp1Ri3bUQuRshwL7XuamyA079zczJy3-dn812vqa1DS5p80KlFl6kcUHA7-sIlAVf1ENjmVaSPSkvwR5EA8A5gyMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YcoUD6bf8SrL3wTImV5x8qQ2opf8D7ICArGk79Oxqk2tG-ufOudfdlIlWcFBXAMTSGv0XPV5q44_oIy2W3I2CQUrQVK088JwRz4PhH_5IsGnzrugJM5qYTIwN5B7xY31OGvO5TNum3zDY5ESrMw9Mw3Ev5bQEJj3Jm7Q9CeRu1_ucEeSmvp4W2AOylFL8jpc1Tn2LrVHKM-taldRk6-xb4u7ZGpcMzhsteUUYOXNyt2Z5Kl9WdHQ8ZiGzYNt2BRm0wIWQ6BnV_qtzXe_J26ilW5jPdU2GBSe0gvezOBPN_CG_WpeQ1FA_M68C7-FX9uR4lCe_htOeWmWLWOwr_dWvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B4JCQX4ul3sFY3qG5TdTq3IsNBv4kxeDe_kEyZdbqMWBZQw2V1MqRFsgS3KSxtscKkWwWUyHs2tg-Bqo5_BIdYIAm9gQKlovmVdE8J6Md-eMYJXrXknjuJdLEbwoWXpEfe-nkXFAszmr4fA6ZvvJ-AVDpTXOXWvLH2M-sQJrwjZsD6BKSXH3InviJphgj8Pni5vTO-9qlz4UfHY-xx-Fg4mzyLL7zhLqyiK-i_0eX5B94X9-n-tLyTLujgQ72qftK2oXoRw98ABmERmuO6vw2hbn5cIPSJMZHlmHJFdIoZW4DJblcjzmiz5ATCMKOQ-LLyVZiRT9_9s0YEH3lhq7BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/paJclgQYlC4fjIh4Tbu_5wWtoZCASLETFkuJjsphY54mA7IRfbZyZUZEIw1iBeFI4zeOJb80BnY2z0m8JcpQbigm3CWOsKaNKYSJSVaIA9WGX22DgpjcJw1aF2QNqwsv9J0IwQKSttxgOAGJXwOvlcNOc-3nNQtLcNz4tjInm4fyXSixaesYblspoeFuzssEgkbdGp_U0w5UN4lXmLog6O3lc14FyiBoIeNdzvARLPi-4ETY4fXyBm0RSJkF2TEw4loDOT-C26bVfzESmDR0VHX9USoZSk0dtsLd12_uf-lFSwqZsbVIKtTkD1QjcZD7R7jP6xnbGHJ8bAmF9EBqDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HKkfrHcIAS-6A-GRAm5GG-A28OE2cosRK_5C-y6_825suIvD4I8lMnBRc0Rfi7f9epA2xkQpog6KLx41UgO9TIz5d0VQKZ7tHoRe5FZT4wrwdXFm2TlP2wMvWFW2qbF3yHHiqTsnhHlDN_ZSRLSePrEdpcwdZx2CIYAfRY7ghDib8Tku_YQPeCdp8K3fkNBdSY_1DR785hwInpcO34yKL5kazPalVduS2uk250VGnqxVOVBNS8Bgu_CAybB73uz1enku-t5zOUtXp_lXgHE0oaUMi0CIK9nKL5JGfM2Yha5L2h9saN6brVMzTNKX2G8r2CNrZQI3kYgecTvNYIgmvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T75EGhJ61FtTvYKuVp5nmGa1VWsRYtcN52qWodQjyIEs8ZUUL3Hqz4RySoq9DfxO7jLRQF3UoFRXSt7PMuPcGffTwnSKg6HOYzYUpbwJAYgv4fxoGWf4AdsyxLMCt3FXV9XswnK78kj2PFnZlWtUC-ZZ8iZk8j-VaEDJVpWoNEciXCvi9TnYAJ2mBivoMfksQcASlPTNfiqXVg6mfoOpIuNpUkezPn8hO4_TktWLjq6NkhQeXW3CMKxZyDcODhRakqal4uTxzByxscrnX5ht4mqhwkPbOpbHevbBjKDxjIi_qnyGBRqFvE1sqwVsq2OYFJz_i69WUmpJBbrqZX_6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HoEb5Ad95puWnYjVTmQWDRGPjUnGTEjnDjjsw1qkOsni6uLNRZNIs8ii5Vbhta-9e6GBtXbpvPxCTNCNUNaeKVTviUNVxz8A3jl6MSBD7No-fkc48WBPJGEHI3F9i_C4DLiCsHrWw2ZRoQ4ZlSmd0tFWLDdh89sp1v8rYqikYe9ZJgTYi2E6zdsgb_QFmTzc1Pp_q7i8NjHEcBmtc7R3974EquZPqnIqcn2kpKevtT_5r0ioPLfIyE3wlvk32WL_mdG4nPv9jmnUujDaZrcvVywskq6f6Kt-yz6bPjBna1UAuTvV0u7p3qQ5wf-OFvLNHj7RhJNcZE3nK0r1kb4RaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U6u2nch_JfTypobNEIIVp0-B6X45HXjyO3zx2sitjWKYkcm6VjPsW2XLiOq0tmCtbQaYbBdu6N9Msp9-q-SdqlAsu7nymZ9NIpXKjRBDOfFg-yTuDLmZOP5rSf0gSWX2DLVx4opWb2QwYJ9UxYP0b4qJqmzq79Z3oPHmO6-gsLYQ5GPmG8UZ1VYa9VSXPTnnRFm_eN7XursD59pWuVnDD-QYQCSb9Y3kCtpiAJrRT4gwacDv0ZLGajC2Iyu0k8XYTFCtmu8tQcry-5BVdDcc3xutEp2rfJkv-dQ59-tvTCanSAxqqNc9iA1NU5PvbT7SCBhdr5YenfRu7jlPD5zPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VikuSAvS8zSnSVo75udGhLA4VMnrns0KdYay4h3ANFdzr1vYd4loWRM0yWgKeDDpwoItXBfkn2q_j4V8-SKfNVW6yiKc7zK1yt3ODjwW_BnKcCaR8tIV1razqHD7Il45YuS7GREMHCNiiKnMHVJmFd9dhBLiFhROqgYHLaDs0ExjjniIM_86DvtbuY4Mu-mCah1FdkFbhGb8dpHnnRTtWVs4zLYcOpU3yGEg_MY3MVJL6DgK6zT8iKdOnTXUnr5XVUDNzamZdqCxQcyuTOJldtLzm6mpoOdpVBZTyDzbpS0fhu5bm5ngqKEF1D6cUNA2FSsMqIFcKQPI4DlmOrZavA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m337HmVEDcP1JuXl6Lp1y4TpZgrNaP2ak82465xXekIoitxScKsDW4CqbzX8w230YHnbwt78SP2ccfJ4jHJhXybZdnKszEjRvizlqaxvzv1lmvdj_LrhX_RIVb_-I8p3OND-PDpG4U4pti3WAo9-7D7b1BIs_ISlOmSsOFOlAkxwLk3HDmd4BDDfojuvsrCla2WToqJcw-zO3lzn8CtdmmPOA-ZaEIYam1vfKDjZvU6_5A3zpMEoDg4oQK6waMVN18G8l0-YdAS-USe7o6zg3SuN3Ktlj_oSDRTveTw5PH_mbATm0NlG3oys2rFbNpiD5mNtdVmNChaKIidi3Lhvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dc2LybMkKGpbRGqCSfHeq5h90Ew2THPBgKrxrzSk6V8L2Hmu-uAMbVPW0HzntGX8KjqXCrUQHe006xPuqd0lSn3hCa5uxQG8OZF2Srpc0CTnfIF-Ap-sMugc2EdA8bLpTbyAB8MRwq9KtNiZk41GHgTQXPFSlX6BU9pCdDTWxj219mBARVZCZ4xg1ZQYFpgIkXO1BFUtyL1gkXzH_EKFOTc0Ju4TPiPQPbqTFxDnzLaVg4JKkwFbjQINu-nLLixT1yVVc4jjsis7qoCXBebLCWBZaPZCZBFzBApDo5JNDfG6FY-tilP413S5SMEo92HTjcqYvt4K7mBqrfQnv7rE5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8XU1Ov1_WeiPmxgDEcrkIRbwgXoKtho59qVSU1XsXMMcQC6FoH9o_e2-pZSqfi-1Lp5M1vS1w8LhmsF6_FdKq8kh9ORzI7KaY_Oc7V5CPFLXFn7T02C1k2DEFSkSHQ63aSl_5O2_cNu6V4X2JQerglpQUETCE5ia8L63zTdBSTMHXmhTvh_w_RDxpQKdr2HjlB4RNCmX6H7Mo5F9XsTOeOqDkWtM-sxW_mtBfCFrMP-OF2ukzKozYkBSuuSiGWwbQodE3GY3uDNJv0IKfnPVNZ9Tp0qJt_t1frlgq8TQp8Sy-1VaSRuVUp0rsR0Xu-4FdkDQAHnr3HwcFUE8dSWhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OH2ZKeSNObge4oZmYOoZRU5_b7HFm0vb-NHsVONxpsJ5w724raMzFXEiBuIOMujZwL8vDfvhQ4B9qGg9v-0w5mR-KeY5IEYNKbWMAY2n_i7gaGaX1G5OWyBjJUl05WUjgdeoAtvq0nousSGkQU2YmPC-wZUrep3mvDOM1my-0Y4v8Fqf8swF4_KvGluIAD5FyeoFD26zMA8XYKsBVlyaj2QM2eAaC-ucQa0BZOSrvY5yVO48WRFmJn66zjCYto02KdxqVHZOz-dz6k7CiD2Q8XIIx2pMED-rYUSIYjj6cpDq8Wphcb7EuExRG7oUCHpNUG57j0Tv_2Xbx_8RlwP72A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKSja6k-ImI4bIYPhw-mVmxXn84LpdhkDRj9jHAAjXQY7MOpwLddXpLVxHoboEZPmBkNPFExFS81cTVofWegjKOLnXOi7NWHzIS-olzLAvekXBQB8panlsm4ZesElc1Dk9-iQcuklESL1qqpyzBDw5_f6y1Pkphx-aU4VrCLB7ujRG_RR8vl4XhqhRForQbldR2nxIzf8_bx-HgPOA6u3q4CQLhSQi1dcRkVkc9r35xFcKEnpQEA38Ks5JvgBHjm3gLavK3n4CXG6c9NaC1x2E6AKxVGDvEARw4Xy_cLmiy_V-HpwuilIU7pHCiv3tyD4kVG1mT_Vl9zvRlIkoazcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E6fdeKzcyWT2lQ3CCSUEe0E0UsU7ZGomQDiEdy_BIs3xqHQC3BVDriD4hhEo6N3b6V71TBYCCaJ5nAC-iqD2JALAQaOYOLNF2nCGr3rhYqpDzyb0QcY_bh3LZ8yrfyEwzXaTRw8ximg_w3pEmuUDOxu4shlVwuMfbtUNIXcXyFUIfSAavfeGVLYPtZpTOSyAeu5Ieen3Y3f1uYp63h2kpbPEMpFaAfrhui1RG6j5PW_zthlrCTUod4jJ1DfYOU0FEzluSZ65_Zb4upAo5k-p6zSM3Ha_SOV8ht1wnCdG75kW3tPhG9ccOJwVcm6ONlYdZkIJjT6th6RtJ0o0R18EGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ornPHD0czqXM4anIJaYacuk5Oo1Y7Plin5NdogSLm6OA6qtlF4VWp8mf2t7vlThBqjtTXg-FU0Joh7HqBb20hz-8aJuhKxdsdFtOz2-lP3W2hbS28RvR2d7YEOH62gBw8Ep8WxYNmzNaaN60TwOMCDIj21gpEWuaaFO3Uyiq9-8XBXOz28ogdfbPbrEfZmgd2zWRPizyN91NjmoJWHBLZ2h5sKx9naGQx6eX_1fmN6IVekD2cP0jJcLWYT3H1EGckCLcjEmi4_dPT2NAvLmREAJE-JPlOHp2VBhVLZaaqjxI6gmYXYiy80hTVFAkWO0OBySnwHX6E2rOoX5RFoZTEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mmJsd69QK6ejme-tVjLE40fDVNpvSk-DdKsJnyhTI0FKuKXz0ll5qvZ847g-jqF7Gh98BgiEo53M8EJsqIL9UfYnocrQlShyKOFG-L4YXhrP3SinVWYw7o8zgj-fLKQIkvFGTJqgTnhSR0Du2WfPpCy06Z-wBZr2ilBxeaFp6mU_7YmUeyJAl20qRyIubFA6sNJIkHhN-teOTUcAWLoop1EMNtrB2Tbu3NRAHU0RdNbi7Asj4i07X5NWmrBFw19xMWmHs8u-QKZHKVtw_Nm5dNZiS5C73MmYemXkkS3LOVCLX2c0JFsrs7IW32dF5I2fHjiM6kpqpOb1L5Lq25sbFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UpOe_ThRHph0ndDPxurKrYda5jYyg6MjmlzOXsveVg0DboVZlO61q5MfvGTg0se50SbLF1nB8wWJk6mft5IkA2NG_-4rrd85JHBAR5HM--2WdGMSZgkEz3kkMClYGjIqC3ZxpqYaSKuHRiuSDkpf2G1MeHOyD5kiM_oLL0I6vjcYyFgtQ5XsYK5DDZxqJSU_KqU7nq-UYFmaCTiV4qWoXuJXrL6ToDNdxqyjMMzeW78ONwTW4PbQyklZ4dZ9NjqZG8XD-zKHfunrAYoTiTXEJGS4Da9oV2ED4DOhVVwTftqA1HEHTLUddCIGu3TIgYeM-CI-BjVk0w6orOqPjBzqaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mJSmrCR_sZZHAXaXVIedLKljuQfi694fR_kaQ35tSrvE04OclhWvwXAjScVgeCpLKx3p5PXiYg3piuqpotMOxaZZbV1MPXCuGRUcDA3WfBrxusn6jkYohAngT1fx288eLadvG2-wZ-YdSiLc3QWVKWa7W2GuLspIx5rzrWQ_7ptaX7hC73hMuq2ubBopHedhooNzosoDKMJRqyBjTxWD6DC5wMZnENc_0yMv-I7pB_z7I8pWuRrOmbefZMUQGpve-ERu9BQcAFWmPrBn_y26dmmFfci4FYf1q71n-NpVMLueS3e0idG5EHEiSX_8Tu1JkIrvW2YRrn1DZgtqkOwLCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZ2ycqgE-kJ2kt5NuA6c6KGseoQz1zQsJsG5CWv-F-Y5erCge9n_WGkdYRV_JL_6xUR7z3RVOT3Wifu_QjYx2Q11ngXLu017Qkuqa7NjbSn7PrrPcvygeP_Uu8RvPeDsMGk9hymsxdtMpozpkmbWPyx8BT816jyDyKxZ1suQEBW75TL_4kkky1RCKTcb6wZF767qsu_461Q1CM3_yrjjQ3HS2m3om9lNCViNgXSsaZY-mW1ccKzrgaqi4vroba1s4f6q5gO2hKVLQZKPd5NXuX1rcyt16N7qA1r2HP-E5rShYgaXUGrnhYEHhNMyV5QbSy9pcSyTKvhkgDubAW6ZgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g74xwmfzcOAl7X-HPBEv0JrV4k4nWv-bK2nZIQRgztdwK8MKAh7_GKXcDLgf7__FAmfOcz7jGuMpEBi7jaF3ua4xvxkWR7siC48MwjnBYVsi73LUwifdtkgMERbtPuGsSuHHdSH99ClefpubSzr9xBzIgNxs5PViI-E70X4b3SN3JP_YUMx6f1md1KtmEwQssMu165TN2on0g1UGFQx-lXLhGBpbWDPHlmRF5ZWiawby1tAVpvWeNzUbQ9XN21DALmcYjzfPhmfpmAH7nM338DUgnO97lKcVeFRPOb92ywC3FsB8dY32zjBT9aT9oeIxfpEmtwURruE1-HoGnB2Jug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RTeFFM5YKyXziSUbI8qnBYdNx7L0jxK6F3J6UUY_HDLZLivDSOOB6XfQNap3VHn5lZOjiJ0f-8AcsJy6XwqWAbhpJF1ltAOSGaxb4uXssGCgNJNZ1ECn8rSII3503mlFTpBSDBOcAgePJy7QiwXwINLw3BBl66N_6Cc3SPTTYhbKHbdljS2h1EWZfDVZ-FD7xHIGkDofEmaJEi0o2han3Ah_6P-o6gGMw5nVwZbz8uQG-vUQndlw8AYE0QKNpvJATY0RfULKb3mlLw8s87T8DClXeaDdDHZQOMsUfglezvJlh0uVBmtc_rcPk3csmkreUObSJgDjh1f9YqITQchH2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9Zgo_dbwWdVyI4d_AIRSNEAzR-3Zoczu5K8e9Lu0JID3QlTv4UFf2qF5BQTZyU15RUsReo96-J-vChYzedciDNQaAmq9qU-Ubo_uPAgSCsGOkvS3BGMsX6Hf5ehC-9aj0EveIz9cn2zYJ5DXB0J2IQKGsKAosV-hKrmmLdORHyTNAZDlregZ7ZdXzwI6ahl8Q7kdOTnuf7HaMNQMnDw4t81bJwA3N9hiLtd4h9M_uMlKGp5d395b9FJX9KCaTk2gkC5-ME2WehpK_PsSfy8rLv8Ik8eAcG5kayIIU8j-i9eRTtfHYIlaLLW5uK6iov30atQMUfG2F7-QwZJqF_gbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RFcPx9bwQ5dZnzd3JA_t8dX4f88rQHskocGHRwyXA_jnwshE24szWbUvc4ppL7X0_on7tUFrCNDlkOkpChs8boTL6BCp4CS_4WijmAytFsibuwxqGIkny6k2bJKrIZ7swdWgjeQ6BZcLBhLuPgH9N1FjBwIbqY8Ilyc_Rbsvpl5qoL8UffyGgvdNltu3A9IvNeDT4FO-CfzIDhJ-i2f3hPAuYoYfw8_9ec3NvDownFtKIjVgFAO3s-Mr6haq8BiCAVtm4rVV3Z3lR9NFU9Ewt-LrNMYZSBvXgSayrAgp9sWcuYKczK19WbnJenexSgjRVBNTxAZ8jlqcV_N5Yv00fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D36_VjY5J4noQEZN5HhxkNVIo3-FeN3PVxU1XxCe-FU2LofxPBuPrKmD1fu5kt8RZBjoqkYWBDJtTxOkXhUSxye1s4C8q9YvyZ15i-1IrE6zTjmlzYvXUVzCkbNtRSRddcCUgNHZWROJjQ9_8AHWzPN9IAA0fiW0u0LIPvcyGcZSH2H806jpz-_MPlSt_54WwlothCKLKcnNMUl-qD1-kED-3as1l7VstWCk6ozJOixFcl_Kt1Pxsgc_Qlnyzx0Ov2B-7MrcBPMcXtoU25QR4ss8fTr6tC3MMKt7Y0EPoMo-NVScYcX7s2q2ZHYX2lICmdQLG0BCadMmTHb-C3gE6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7unG_dpgv9bWNX4aGXldLUBRp3z6gyumBiI15y9oqHEg6JPKPz2vG7PwNeCI7FIgHDV6tfSEKp4YN-QDX-toQt30C5eIXKVFYg2tvNb9O6M4b45cGrgnr1xPFRrPIOMLkIsRK0SnObQaWd1t29lGPKCB4jVMD3VUyZhgRtvHn5ZR632-lIs36hPV_MVsLRbUgmiBLkEwCg2RzHZf4nuFf7HYikXKMn99jzauaNZ2wjRMjOFeH_8a5r2g-Np1UcLp9dkqi8Ug2qmSjYWXMytCRUjJoFeN8-GUE85t8hY9qt38yRwIbrFOD76rnJxfd7nhrja8A5uQ2LZfY-HRx0u4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AMebzuqdncQhzpd2Gv_JzEvTIMG4UOK50dvU13EeTsY6__PTU9Zk3dGzYxcZcsbLrYOTEIqPGuQ03EWBCqrYhL9gwBhyuK6ZSfARWMK0DPaQh0FdNU0LUUuCfpb_-dt0ahKNy2-NnCTG4xSY1FmeLOc3Sz0p6ig6GwBo5g7Ee_le5mNJ-k520-0OMX40z3ISmY1YlG6I53OlWiSXuN_OAPL_Tbz66Ozt6BARbpoX8h1yB-gC6b75hrNsNqp7i3quUKtF-kdP02hi49lS6jJndtuMzcALRx819dmi9nwDNeKdXVHw5IJRQVni2sq66gVRD4rqh2hJTjA8UXMVY6kVQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ongtqBRLVENft-NHs4_Zjv9aG8KR5vBvKO-MavU0KoOvzjrnD14GMieeLOz5nSBuKnPGZx5f07aJYJ0JeKrESlY0C9uHZDi1Pd0M820VoLlibhv3Fuan-zz16L9A9HXeFn3jjmbxw3CrcWu9VAt5xJjJmGUy5dOcJ3fM8BBaSrrN_ZTbJMsPGxoA1SfdvZTvbloSGOk1481tUFZ3BWmf0DrZXZgPKtr01WQDVVqtjBkdvyrAIuwzlBZ4PE9mbQ94KmcwMYXQmAicOz4CTj-ns2w6KuGaO5LiyGt-gJGCP54sgweo2VGMDzmIgbw415qn7ML8SIl6ZZgVA3xvpGeicw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bQS2uVn09mRDWPdxzenyCoJgCOiCsGZXrFb6lHwPs93zBDfOX1FH-gUukgjFhA7yyGXaTfH_StLN8-sjVogbzOS4gy1vZOcHCL98-FIS1WxdJsRoAJ7pUPxGJ9fHbh_NTiXSIdjY0eYctw3gnH3ORKYzCadh3hAU7ng_5pG_Xl5IZv3I9_depdy8LmPbSUG1YE0ao5OzdA80a8Mx0ChBLWvsWaMOwj_561JNuwgS2_MfwyheOc0k2-DazgN-HNbMHrL69ZEzrC3B0TzkvNTW4YgYROIZJk5uRDyE77HQgwmeEODwBTkEGRd2CkXbm5BlLJsLGe6ijZDHR6vvgZpXzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XeSEz3p474-PG7zedZSUwFYjAcb3T2AtLWXMeItZm734HhJ7uWXvEPZYdZS5vLVvzbsIf7LYxuCAVFNfs00ZmHJKCxKgHZVbdlNp1Mcn2GzeHDFnYPYbtfpv_T2gQWsIZKvIxG5lTWeMwzY6RK9zXPE87RZ53acBqkBbiyrt-mV5e4Eh4BffpG3qUnTekAj7sGQdniE8hwgehOZp5XNzcPhuPK77qvdsi8TRS06tkE130F7LQSLUAb3hP-cCLIc7deseKbTHdl18X2Ll8rFVvCvjX9gnLzVmRJ6kNZe0yXzR1x-Lvchv9URylDHcPvn8JT463CCsjsIqtfRknntc7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OwdkV661viUpKDu_lpiOA80F4d7dStM2QQ2ji1F3YnuRrbMKL5BSvxafEd9BbTPicaOzFNt3y3MBDsoiCHkt8MarPG2YI4vx5nva__NQOqp-PEBEcRbQeKgQMBy1UmEuow72RVUjHVYPDV6LuitCBewMDt9jcV9XwsiU1BIcc3JhdO4DPQUpW6h-PL3VA_jzF7LFNN3fbQTak_VcvkeqNokZPt4r2bpDCXCZF_omiG43wuhyTgty3W4z9y2c2TtRQTgm2wbVyzcx78Z8JvpKEaXsm8r7p6gNA51sD4xnT6nq9DZeww9G27TBM0lgNgfPtSZDlKsBOoKkUlAerAHlAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrN-gxu8fgRIMlC4Om6BNQy-BSGIiyvt0uw8099FZjumeqLZ74OWzCT4aSCJ9qeJYyjAAxFEq21XEMTqe_Mr9MYvmyM62smb6K2fd1OmmEkyv4GsoD8XZgMUgH_bkM_h20M5eKw2hfSFVSTDRVevdrS6w0M_kEADLEqj-nWMvd_WDL_OVImqG9WYwK4fMYjXBYS1y9SsDroQ24hloA-uwF6RkpdNfbhHP_Zv5iGkHp_PCWTAGetjD5fwufUWTd31Yx6RJuSTspG7eRp74yxdEdRhOWtbw95HbtbJEFgRie1UBy4r8oPkX40isu0gl_y8pHCRNy23hu-Sin0nvia_Vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kwxp331FajCgX3yQDcFe-4FX8k3-8wZdn-KWL374OdM6U8ZGnPHuHOIqAfgQr87Q3a6G10X1031Su1e1UK493gIPaEycwc0kf35BL1x2Sy2D83dxnY_V1keFY8-yba_tVZX7hH17YaxSiBU3ainNz1Xi-1ZEB9R7PbpK9cwYZFcIV-TfsmHYGX9Q02rAYc5sV1lmdhXXQuNxbbgrUrrcDwt522Ale9LcP-f6zgXRIcvyaBB8e5wyAltZcTxzg9eTwHou2wE4fIPwnqvA5RgBML6zsXxTZDJildDaNzln6qd3jGLDqNkxbTqpBkUDDdI6LLqblYqk9-e85jjUDYgxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DRzd6mWkU7pnCHlYnqxBo0rq2fRffH5_VXTPb1lgyObjPlAgbAXx1uqYyKVwQfVYy6F77ABt4tieHCLmzFaja94SDQjNP2MSZ1BA8WuHY1lwCeE8kKxHFVDOMvnD1mKnm9TS_OuHIxO7ZcEv2Q15tPIis7uKLVmwr-ugjLwerW8OhVqundtaH7XQubu7yo12oZ1DgaD6PJ_fmDXLf_1_3FnN9r_C3ujnGm9zaltuXRT5lMDXCkIgcSzeeDnIP8Wz9ymBKwR2ISfbAxRoFT7JJIWAG9bPwSuHF0dl1P5X0-mfO7dl6B7ju5gpDuSSVBhDUj8HFFFQQs0T4bug27FyQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/as-yjVe-0hrDtKP6Owb7oZI1-Iv9ivBbyb1WKVIuz7_mVeJB5jLi249oPlU6x4uK55z3W183TkYiWyOFFlpH-mKlAF1pEu9g4SsUghZ4YjsZBQKw7qq_lvr9qIWX3PL5EY7fgbexnYQVtdgp-O8AlQELhWfMlA__VD2lpGgsdUlraDhISeTgEK8v0HjnuGcGd6uX4QCdbfJTiSiBiBaJSz0d1d6w2Bp4USvCx_Lw_CQB6IjeM5y9PXkuBdOJEa6uks6ziFp1muGslmw3X5uTjdD4nkm_1LAehl2I7ozohKEOY3n6_Px4ZtqFdvx-xrGbaf4UEV9WOMa4PBLazTIwsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ne_pUaTADhmqiOH_biFr0kg916ZgR4Aa4toUHLVkFGz_hCbz-3nAaIdpCNTTwbWmwUduYma5bAFIiJe6pKlP9mkp4gG02v-_Onvszg9DfNu3vNlyMDX_wkHElFVlsasFfYVXEhZt72uPflks7clAxFFm1W0Tqy1G-6xeyg1YnzVSUGXwzhR8uhfPU7GfrF63TkhOk_gcBHiwYidmyUPM3620obfdB89tOAIWoRBJCXu5EKjaTsrkBa9kyYUgCAQWVtkg1eI9EX7GCS3gcWOVF959UXaOnRv4YNPwDdfXdc-koxEQmxLS-41JHB7GyxcoS-sTz-QtQjJVnwlhUtRpjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6URV4iQkSAtiiYuJuEnf7vyAdKyRlqlVsqQ2-5zCdFhzcz_NS47XpUPkxwK4whyGgdCV7lMt6xgSh2XNl0vyrbPRZMKjznbqfP2jtQDTRIyaxxEN_uyVskbqSCPy701Ex-Wb9jcxsMepISbv-GZo6AqpQBgzAIteAo8wxP_rGv9vMzarDzsp5AAwBFOxziv0uIE64_6eUZnuMiehZCYE6jex__T-Ob3Xy4nK06Kskuta-QuoYOJaWCeycGTut5oZK29vDlkyiwzlyLWoYmgSjw_1UP6U9dRoaW7G_mGmSa3gc_3QYQ98biroPnj-Fc50SDLgZzCNXbdzbjaol206A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dK4wQSCXj6Xzq3hReovjNy-PLog328kf3z_v3jm5BwZmSeWzBBHSU4P7swf-1q_tt92Y1Sa2a1FRs9hoN-al4PmHeFflB-AFjfA74Lb4kMwlN_6aPlmP6M7PgcnBmNe8o_lEdvaDd_rJ_AYS8qJ43HiXiF5Iugj47oBNDRQyGjp_g2hMpfuvTWwj0mhY-3XDLiiDGR4Iq4yU7ymwahvA6o1SWHxPT3RwKnQygavvS_p3Od8oC4B0Ph_mlYLWB4Wp6hZk29oXRlemmK3fmKnfxJreNVjEIlrHh5qaii_c5pIlzfCvDJyfcDruywjGaph16Z_F7YeAAlxQtoEsPH2owQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/avBuBJ1cYVS8UaGZoR5_SdAuSHf3FRXAIEX8AZFL8Dn851oopUga-MpD147OHI82pqPkqTc4tBEmmkOZPWhMlwaX0Eov6lmdJcl2IvxPZViE3x2_ue-qCtFifXxihDFGZyWT12qWOf6byG1m8dGfqtoqX4t1zC2qmIVtfQFn-nNjNhlQxVztICK6ANY-xHxgtliiZCUmCa9qnHZGh8cQ-zen7SjCUd94fRC5j2JdnPJ6m6g2ySjcmdTeRpZKxCNMzr9KPSugnkEFoGC3QTMUZc4-rkfMpUjTLk8ew0LWicQfoRgiMaADOKg_pjWRPHF78P5oknFYvEOP0ICcd9UwcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mCvGio7VrhTuR48qZgz4nAor5agLsfZNNp2-F25Dllj7MibC_lMBPz7rPPYiN-BEqam1KH40GDIw_3fBofRCqrs0wRCQ2XVExUMRXvqJxx556e_e5IHM6QLA2_DMLcqeNPoAQOWuiqYeepDfK1_EiM2Oiv6I_vxw2A5AAhgXqvlOm_mQtbDnweyzjEvZGEyRHI_Ux5quImgZijHTBsb9SELoPJ5D1aW8wNbyjoQyFyKqHBfiziphhdJO_-FUDbNUIkHCXzD4jYk9wpCJWSw5WtiFoFNuBCrSn6xOsPJB8cA-YixqbcG0eTGMzw-THxqD99RlWALA_bXhY_v8ABHUZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XRFKJdSVA9YXI0y2TtN-UKN8ksE_wlBIWGiVHCZ5l_6WMRfNpDhXkV6OD4NmcUn-GCSsCI7uo3W5o3_6TTfe3vWFhg39J-P7dmUg7jfbPI4r4C_kxNHT03-JPCJNQQmPH9Lr03g38wPry9dYUOh63HpRNBWdlpt3oNnnfOSNYt004VAkVP-lAaoVmLFjjfvYBRy60cZhEdvLHTXMA0nqxoy39IlNubBWN_m5JYcLidkvvqrUDlsx24fZ1_TiH9jcKkZvCHJEBPz41TSr03Fth-tUEdxPqpfnmZ1JLFqa_ME_Cb27P60NwkZVrdg41RHn9jmPsCFZfmcvuTvGf469IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sHTgS-5v1jLbPEkza7dlNA5t5ZKNPq6JIZ5V6EsuYern27Es2pqet8podvZCBSEPGqltD3ibV939nD6XPaKSmYqaeu90FExVA086N79Ed5k5tYrcPC2NbtlrKsseYyDFb_Rl377YxBZPZJpPSwrICR1oF3fxbeLlUcAANfDY902eysl3UfkV0CvT0XguBZ3-QenpQFDlDab7JLiSaKli2bd6Ybz4nxzIsKvKkPucawUCJX-5JiwSUFSGZNZ1CE_F0vVKGxJFTl14WCmKXptYqvN54HGfA8DGRIghXRv9JtwqfDaTgaMfwMlOP3I_EpfS0jbZ-GTmHux-XLObNEFIdA.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
