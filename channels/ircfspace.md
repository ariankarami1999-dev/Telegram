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
<img src="https://cdn1.telesco.pe/file/shODN06y52eYIQdBXXjlh6YgnmgwNUNgkxtjFhvKdgJFyR87oZvoRfBPFW4LmmZiF7W4-PXnfIjHqmQNJQkPcdJapJfFtV-S6RHCCDu1XYxuNDzK9jdI3D3VAVzEecIUZ2MIAmZkzMkKL2rxtaxqADcmRYzXE0bf1vOk7naAKSET0q0xcccpgEbDrpKbU4KkYHhDOoo-OKHzT8bLeJfwC37gxZaQGcD4G9oB4gesHOYJ2j72OtHFAcdSeKQRX5XVntrP9-tcM6n_ZYTp0tzwljn2qLlFLrfxTnTLez6TJUUlGv-JRTl3GjfwIyNNyZcH0H5KhH1yKx-uH45KutkrOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 01:20:35</div>
<hr>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V3OFGc3iuZ2YxWQmf1QyfNXL3wzmVRiExbZclsV_M2lpL2qpVYhHgbjkt1-GCWAEgj7fQ8uRJ-xHsufX4Rj0wEg-KnaaETFYaSZ1prfvc_KbjEDMYVbsnon35YR3uy8lQwWTIi7fHMC5JWLqLldCxD65DmYw-1JhbrHxIISjIDIbDwI8atKPXt-BGsqT6bBkpKgaZR4PkYGfiykrUUNN-jbxnDSmWOSt9_Ii05irxqkdUWGNXmCXFJwr4hjQFWYpvqQC-Ul5SEyynqG09fv5WNdRWQtU8qw7nssHvZr_lai3FRnR-poOrv2v_wubQ_Vg6DxA05WhHh-V7utdYG1IgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FYqJoUvA7xgynMpLfWFv3bBgF4FkZpFVENzb4i-tCe0Nk8j7kBuJDa3UfBebGsp2oQcQ__nKw0gRQpM2xFIejRjEHvWfXei6wNHI6A8JMTKwLzAcFQ7WL-nGq53Ujyoodn_9K5auInYbzr9OArBkXlwR7Weq-J7IALLym7o3eAg6nQnnmEeUpN-m82dXO8CBzowflX7Dgq69meBLHRZA93frW4fkD1w8nFqSkON67fUb-gwLPdh0nda99bjYyuyjqbGSRJ_OBcwBQEhqalsAn1OWiUqjesyWqsoM0Hz9eW00Z_YE98zaBzgikXhoUj_tpSvQSEgw5jb9HVp38EDGXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQG2lJVPNjzGOZ4ljmCcaNtN4sF-0HVSlUNve46Hi2IZioljP89KWrQym9Ccqw7xD0vARahETIJTFevbiCH_1MabJ4cauYUA3cH5CL6x-m7k3ZgUFYPJfIc5uxJAzkF3nMqJMrPVVNtC5dVYzajk_f_iDnUP_snInJKXKccjwrw0FRG1TVBdat0sgLcysOwzLBL17OiI59OiLx0lakhODMEf6Wfhokdx2ykS1eyr9lHpzJmkQHtBdILougTyXkMGlFxpGaLrG6EffJuGbJWoU5lOj0bWuG2f-i6qxSwuUs9vBdV9HyMHuaiHTES1HPB45tlntLEC8JogMAET1I1gOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=TnsKnZcLNAaNmVa-38S1Y2H5NUMdcz7GWpdh3s35grDSm5u0bQIas2RsTnrArU8PvCkTiRvNi2t4lUzWhVrCROecDVE91xRUjD88ZG3cFuzFlqCF5Q9Zmk3GqMHp06_lt3BZTVUWD7IV9mD-cPorcBsAi6-aMAGJ2932-KNF7S6KzSQ8FMkc3k7P-zpI7ksq8Tum7ORdG_Lvut2KXcc3dgaZmtbRnYDtzVWLEsFv1lELXcSLhRvYzbQeRsSnkbRHjJ1e1CNxAqjT76tA4nA3O7Q6xbwRJiT7c89vpO60p86_7ClW-tHyS5nduOvvb11swA6WsU_SXX_qCWYxWpXcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=TnsKnZcLNAaNmVa-38S1Y2H5NUMdcz7GWpdh3s35grDSm5u0bQIas2RsTnrArU8PvCkTiRvNi2t4lUzWhVrCROecDVE91xRUjD88ZG3cFuzFlqCF5Q9Zmk3GqMHp06_lt3BZTVUWD7IV9mD-cPorcBsAi6-aMAGJ2932-KNF7S6KzSQ8FMkc3k7P-zpI7ksq8Tum7ORdG_Lvut2KXcc3dgaZmtbRnYDtzVWLEsFv1lELXcSLhRvYzbQeRsSnkbRHjJ1e1CNxAqjT76tA4nA3O7Q6xbwRJiT7c89vpO60p86_7ClW-tHyS5nduOvvb11swA6WsU_SXX_qCWYxWpXcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pIP7N83tLScBoFhVOLagpRNRgD-68ass1KAcpTfRchYpwhEYEQq2SpSeUef5layCmb1EPfBTezyNfB91W90HBeeNtuG6IxhHAi-I3bC8WK7TSWSiq1Q38PgRAGJQOcbv1X_iLjrXaPg4hfXCuJejakGD4c-DdTZ0JbAUFsS4r5XCBYrKZbaDzfidbpT6MKipOLXNn94ztdjkuN6QDUI8zPjk9MLKxx_bamd_CGWT0mG-VaOfTPgF2EzTGx8wtDfQkwoq4Lo5FnzreYKZQjcTLCzgWlRYu0ywyp8AzOR9glS9BXDE0DsCg_V70rl0DnUxhfr4MD3so6yy-Txdl5W-cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XxrqPPppv2QkI-q3UgBbhK6gqPR9-eGjf4NH_VbBf1e4paIklvwqGBwggdN_6HzvlUYfEdCSq4S0bUchGGYje0wEFF_ISBJ8uQlyBQoFFYbqFpc3EYSQc7eEMRT17a2p1jqK_WoOWMn8sH9dujnEgH3qEoUztCNGaAdJqDfIZEaOxSgUw7tPCkBbFoHXVkB-dEcfOzlpGQMRQNvnwIx-0u_VFyTnf_BgEResd8mOk378nyKS5oTHRRUdOGALHU6yy0ZZHs9-0rir3H3JSdVRtkH6SbI6qPcxgnt9g9JaSrIRpSUuDdgytmD5DpbX677ihMMcP1cOqfR2OLVlr4w_jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-Ckkd2WXghNKtBzXYC9thxvUeEPGR-9MTwodtqsDgvdFsXo6DQG7YYB7MxAIXy0WMlRVMcJRuW4QLnw77NZ7qUpteBGoj_RErJ4p9kyHQkNbMhHGLE4VOsCf1Wb2VGIdx5ABEch5MWzeCkybbKfQrCZj6ndnPQbBcVw6XAVt0U_bUgJmIuao1_vHOicmAv1p65GMIlIZ_OposwQx1hFzXI1McOTsWLW8s2bIJGPFhvqRgZ5WJRnpIgbu1NPpo8dTFPAOB626NUSMSRpWhEru7fS0Y09kcO2_HJj83StIMbq3vE9wfZpWaW6vBIaOQB1lIZKJXlZnouKXTyBp6meKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tF2f_Qb4pDz_YYjkUs-saI1A8bgbayGSJCu1a2YSzQdAn0oVUJvAixAD3u5wtBn2P-FHu2JWBPH9Bgj8FYcDNlCf-ofq0UrF-ffleFPp4UH9tzEqLS0cjog6rhq2_Hdw_1_rG92WvBQ7syempi5B6b44vUn6X66yze5OIdZU3DdxwTPXytrh-IvUa1LTLZ_zPHqBm4thqAINK09zXbX9mz__6YTZcFDBa7K9oHLLbS1NbKGo2wFKWaCkJ7Lt5TOp5McG1Oe9MVeqpRgRh0by9ph4dg-T91DrvFCdbh-pD1YhhsZPw3ryAxGWIVcO3fveXX8CEehvaRkL208m6W3k3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WT2YHL3NUoezx396fQt77YdW43q0sIe30XQ9zxzgiO3Eb1aSVzEFww6GIfNr9CMfFoU6WmbBL4EJKkiq8BgKErmT6zHDnaYFEj32H4Sf34onHYWuGhmssv4etsoGcw6M05zJ_OHn0R8ZSipOVIMygjyR0ye8Mi2AVMSH3invVWxiFOffvZAF0OstXGhWjbcWlXYc3LaOsORUBMSPtT4QCTPx04tj-Y5exGk_v0IRqn-eVPxkIMAGtfJ4upCAtmSqdU3gerIgAVxSAeBXYIIqHtDs8B0hRLfdlG6r14tg_8smuSP7k_b6wfG7hs5SJPdA76paYTAkrzemDqGi2E16qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUU9oSUZWbBF6HFu9GWxtx8HFRvY0tjY7zjXmhK_vQMRWmOQG1iYKcgUmSVRvNp317BcXJfWa65kZpRozguj54xyCug2soU5dUxuTT2gC5LrCapO7UGgjjloKgtz0071ZhFfzbx-LTi5aOZ0cVFVjRTli0E10sVUqJu6k6pjaF_kjewxEJC24InawNoqOWxPUity6JEdU0BnW65g6QoAiVt58FP-8eb5yTDPwmDIalw6MLY_zC9PcWzqFnVz9bYDE6fzpemvPBPcqDS2sFAYMgYdP4MzIynll4eeQG0A1eIiC26PC8qM-H26EF_GHedi2HX8AwmqZ7nZTPAFWYFhGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f1gfk8Mbx9ErWZrJFOzh_M4WlxmR5F3D3QMAX7fhun6uZrGUrO1rrg1D5qd5BUI_tsNsKX_5Ag6tyLSij8M2zndDWaMvkBvWLbUY8eh3iKzi99e8UgglsPYtax-updNLh2vyW0-b-uOKw8uTd2OND7NB3Bz7OFbe_0wYe-jFCs2qx_pu-rLrb47MRrhiFJWr3hLwqm_OQ6CNyi-bGkBVsw57OFhLvtsSHd7Ub-fnYbXhf5Lknx72WvlR2i1n1ewLUY3I319Tem9aAzHu2x1HyvU64sr22iKtC-XcHlWmpxNIONDNbF6ym_42BaXrxDXVjZ3ISYapuCK-ydcpHCyjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vCDPUzRVK0NVoSTvmkipO9xRWFC5bdcK43tceNYhFn9BYxVZ3I3qZh7tehci0gyN77iLo7CuoDLxv4YFZFMq9v4PVnSW1g-VDXk5VWhlfTpB1mGPzv-H6XkD7uoxu4Vobq0jefJ67lRObXpOhBCh_jD9bEjDrhCf4saungg5eGKAT0QmEJfIL_Vekz68kp3uRBtxwcPhX9zfDR4Fl8T-4-3DXoizUrIEXsqLHeysnvBRALVSfsj7oWl97yolrk01QT4icbz9ex4KeHW0uj8NN5nyhUCsla9-fZ_w0mVsLc2X0L9ochIZ3OkVRdquxora1pcBMvrEUL8yllyMVnqoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFVY46F2j6uzMqIjFulYFMUA0gZyNomiJfg8KqqkmmDmzY8oVjg7YJliS4q5Q1lCDttRKfTB9IL3XT9b84omm-A2Ge8WZBg_Y_HZlgKCGYRbep-PICrPaw5CqhGYBWoLzHmfWtlR_QrQ5Uky9QWRnP4xb0pJw6PMvwic5IfeLX8-lkI8tdWHDddPm5ObeQOVd2SACT-FKxaDO5P97-jSKOnWZK-PejtxBVrX01QQD5dF3KesqeSzRujRRGjQa6-UBZDQdkWoXwMflmEd61ePrTOl5Ohj3bO06QVqpZ2E-GcztIbNighw6zoXOfC7GJW2ebUfnCQT3HtMIwaW6lIyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQZDBCi4MUWW19Fj9WadUp8iCwAcIsR1h3e8X9CuaeAuf1HHylhr6IaB_Y24C4b8J0RopxLYKkzCjtPEI4NVlFKRkDH6mjeS-kjtiGS_AeYUcYptmgMsGX2G-3ZGP9QSRLbYNWTLY7oMDP8bCjFQw6RbdgCDsWi9gVhzRDu9xcUTL7WfUFubsKfOoJ34vw3jYLSBkFTkNhwfmXSgkhEcGeWTnFtXbcP29I3GeTBD5je0ESiVAfhWOngvhit3vqMisJ0eFNjXgxtDV2J-8QMPPXNYnAo79GsXIoLFcuTHthMKGNnnQJXZapbNoSHGAe8KbfJUGvI1mI9XW3sATrArhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pH_Lgs7q-XR08Dfvw9bA3eu60p0YPFcbDC43e8ZmKKXnEz3vXk2GGL_pa89qyS0NJVyo6hv4h0-f2GZxsuKujN54tNfudRE0AqXcH0fPU105ekixwdyma2fyPHgDtYHqDgSO0bN6HShFGNcG-wy23PuPocF1pVxRPI2dmT2u6sOL8UeVXVhzUfy-47QfTsrcW4vJW-h5jY_QPQAdv1vlTahvmcDYemLi1efkcdrGaBGPdBo2_fLvpMFXUcHDk-ea3sOf8gNph8QBPpcvnDHaK-thKHO8Pp9tx6ZyXp9y2wp5GvZR5JglEiCrRgQkXG5ZLBrPiEoxKynwPYFGJCOpCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3GueNcF498CJuwfcoPQkIyl0juesH159ogufMrjdVFrsqdPr9urQgNmJJlufNC8YeLkEqkH-QXfi3Tp_Wh8OQQz-qF9WsGsXIvXbR1EyqsGU-OL_tFLvdzXZ1GrfsWE8Re1ixR_A3vQMOHMqUaOCd4mHOuQ6IvAwbI-4gCuyC-liMiM-NyrTDOQQF529Wv_VpDyKMs2Tka5T6FAiSOdcHXdTqXxPXPm9HzKP0wmBxFOnJxbVkhpVVRA7y0YuiF32OCJZXKfyv89-RKh3Fts0nEbOPaaDUpq6yeapffrRvuhxlClOfDbSkweRPN3kHkVXPqVV9hTkDh2CmBwTtE8xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJD_p62y3Y678XVvj8okAbAcmnWC5KinQ_LSb45pruSuFgopS7syBXFbKGCzojFglMPT3DqNBCP51giBAtsvd8ix6wiflwwyhLmbvjgBawxyw7Pdk7zupqzGIUvdEz0oJ6FMDCZdr1RCkis2LEQDd22sKH4E-yc8mjnCD46GHXqxlTr4vdPQ8EEC_W0HnHHDtZ8shHDTCV5sj3eZNJw3Ft-GFZ0uOCgzU5AmfeJ3VbMC6GIRavaKjWXOxyqDoNjXdgDO8yOSiUq0YpxeR1juebcIfoGALC_Itm2OEUMjr7lQ95a0ToHfp8MdIxGCAFsqcBOfXqzgMryt7V-18hMu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r2gcMf4rV1jcuPCKc0MbKTW6Yo7ojy3lnVep7baGLju-QJVyNx1lFJGz_b8-JRLoQg8Xi5zbHqeVe97CowRDwApaf8Kv6mqXAE9bRmM43dWP9-tgL3LaN6V8F7b-RQEstaGbBu6qbcAkBF4TvNVya_dGKpZCwLgDdDxfjtuOVBnnwCEXEBIXYIbbGlOIX1KgcdRYaCITlnkFgTBoWhLIDY-VGdYtYwJ3bRAqrJ977NYGPSkb1Cn4JlULHjMkcjDL7BYaWbO4q5hHOmlMROyiRUVw99Xjn3a7tGziaTOMOE3DygWkqMZOah60A-QVDNfBDh0yFPUPspO6EJtvl9xxSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ur_zRUJ9mQw4l4vCcdRImgQohHsR64ax_DUaSHQo9YrOX331YWnI556YTmV5A_zfxibh0wgSwkfUIYufVP6TJq1uj2nouIule-mNlX0Gm5zztA0dD4H5HVu6dVeVtTEBS7ygJOEbWXCWpsZzlaZptnWrAWt12-9k7Tuyr0su3jSBLOaLtsoRQrbZUTkow9ur11HFcDgCvJgFJ_mCL0utjROP626HEjVh7nKVkHIorX3ws_ahjQ9ANfPSI4JJNwiGJEKYhGhYpG6D9MX_FEak7neQFygGgjtmX_lymxmNM7naFlVfJWqn8NXfG6g06lJnLTaTe8nnRmui5aRK4JJRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZR1DB2i2xlwkPHUFKe1paYp5tFDr97jvYke43ElAclvogXLHRD83ljHELyHgkcLe9kX5Y7vz-P1Dq_80oJ72jxXyGEzVNLoJscRRG2T8EZrgObHBCFMjDmp50IT7GUztZ1mmJnj-UnDDRIaNKoC18MXyad-4WiGahfxYGgRNJ3PcGqy9IwMFo55EtO9A4ebXzhiqj-Z7gxMJs-NLE9DwDmQw0bYfqeGCchRDabGdLjDc_VGmbFKplbRXs3Dygwj4Rqnxpp0OpxYzEUcR1Fqm3n8Rrddcq-vDfu_RZCDKe0avIz6F_ZVIvLGzeAOM9HR_tc03WrLtymi37mD9K_0n_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TR4lyhvWpg0HXsodvF3Zd1Loo7k5Opq2GK3Nq9-RQxSwWl8GhV8HWHkgSMQbfzYrYsBCF6L5Sn7qvIx4O8zvRP5U5GOM9VatxUXnGWn4wbSs4NYFptl7v7gCvPv5V2VVNjGqcC1dgcBgiw2BxqUF0tw9-3hjefG7rVAzvlzD4xh7xa_GbHow2sM46r37QxOoQbx7S1taiv083sQg0Wo1O3yPQ-MlbPPrYs49CU8MQe2StACxlElMPHNBJbMmZWyVjRImQhgLwEWrryeBsAkU9nNyWpVWbcOQJ3dEOl-iZV0Lh-QDVwMHvW_5Ehal9z59Wh7C4QVesZ9C-hpa7pAY6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O6k3RGijuMfiHiAk8rpXz6L7CjOb8U21cEDvJbGtze-T923mML8JErpFpJbw17CEEoOGXhA8XNERVnVpJhxBTKbMG38GdIMj-xwLU6KELhvjhN6Nc1F446lP9uLnUNd0TQNaZ7eiIscjXcrtX9gcaQ9V2Sr3FxkFL5U4cndaqrvvY-FbVRtUtRH4Cb_iP3lEPCIqSWuYspPAbSKVs9wwQc23-Th2txbO_neWSedKLjxYV7sRMA1kLLg-uyLg6xySMxpnN5jPcjFaH8q23y5pbmOOsFW5DiCU_WcchsolRrBulRKVRLdF50yeT3WwXflFNPWOPHoXVRiLtmK665yppQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKOW6lja1fUlDW-KqXoba5pgmvsTxfAH0oyx8FgZGiepk5eVRGetmbBq9eEGyWyPrJNvB3jI1-2wOm4tg0ZxsDdt6eCJCmwkp0z5UR-GXpo3KS2E85mS1oF2OJY0zcfFkqOFCMYz7_8P211DFQ61Cv5JhNab87sQtCkrG8iE7JexAnW0LMvTZ6NRgKXpfZLA9QtVHE6k_t6Sre3qEBWxOrk0DSajBVFUr3mVsVghRoESFf37-iyjNn4ugYaJxc82zBHObkzv_SW690ayEZ4oVgQEgjmjxiW_DXpu14AqO9F6Tb-5uc8uKWhfRZ3l5WXk92IrKnfNKrZXRy683OqzUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/juNIgsSBIQhivdfKZH3lvkAG3BgDiwhfmHkxX5wQrKcty3Kn8NwaDJdjGrrN_yIfQIhKr2Lsiz1C44i73c7BSonJAb6R0x6x8dSvvMNrqkYDFe2PSPbvPxVOC8bOfdNJCHZtAKJf54kiU04EsUY-k1PCquzd7mLuP5fwD692YW71v7-jYv_kv78IB0U2aVrQ54ise5YQFRfbbav4er8tSF6piUEZ9IF_946CT1dfft3Ds4qtVtUuG8R_EWDRMbqjZn0nvCnuan4onX49bDoHLfUEkh0_q4tXZ8ZUXI_EztwT6g71cOhZfjLkxbXTPecdButJ73Len0cBknr49BGu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IyNhN5i5APxygDgcQSyi2IuCZYE-P710BDE5n0mPIu_5sCyO_LHkMJhgU01akmfT4l75RjMUZTsFSHqzu-d3DUESDl1sEWq47vgQXeVQ838S3oo6KyoHsss3Je9KQqxmvLM9o-lvpQyA7UU0EhQfSZKWCfX174_Vyy0E1WYbdDYs3hmMMHCknDKT0pP3iV2cBmDHmyUSwRoFx-JuS41fBBkwBNb4SnPnAyVmt_7j00z0SMmneDGFGGSrSY4N_yxXso47IQgzp-bBgrKAGrMYkDJHgb2WLhTjqJ4RMXKZzdf1j7IH8zKK1fljGW_exvxdC5Kxq3Q7bycTgAsMuMQzSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G_N363xN2BHVRr4lfqii2kOErQAEPYU9sd6x8KO2j5ty-6Aa3UFQYNrVcep5i_dp7n3LhnlmPyYJ0-DLuEF-tM8yRzniSFWV2Pw-f3bM5nyYCSF1R09TUYOxCkjDotyFEfb2GajqAjVkMtOCfrDPppM95juW9AC3nvwxHozCLnnCEA-gdnavBgnP9kN3cNZx4d59FTGObOn7D_idq4PHNxvW0k0iikXxRqoHBb5KJXleszCvPtIumc6fFRQso3TscCNTKjlXHCv52wta1bQD4GsaYHsj3vpLmyw0-7RqdqrlyRFaGePN5V7XY4yU-cR6JWTJ-DJDMra0vm8NRWGDew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfPkK2HqM85YMXUrp7BRns-RWnw38uWNfvpkHvbVq5oEsB59F6REY0MCD1-wnH9x9y3shdMCONbI57oIMtNrqUrXxq84T5MsQWfVUbqN022Fz2wU_2azWwtSa8hhPVt4KVskltuoZbcZDaDu0au_-qy3lpymTZNhFtSkFJhQCZWnzKCKKiiaYI-GorvTpUcr1w69OU1GFZuq-mi3jsh7ILYAvB50C-GMn-G6inzhT5WpUeJhAAvRO9qbawdGDdAu6BrgwAR1ClvZvmAlXvuIDSAnN8frVFf1orDqGBG4Jsh_m8pJ9yYZRyqfe_eICQHUOxEnHUnrs-4Ni7NcMAqYJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J7gvRZxukgVKMX9UeMJ5oufWAsfG-IipaSHLtCpa741bi_jLjuhhN2QQyxM6fEqWepSSikE7dL6JNNntIS346DNptOd9G1Ap6eQNWpeds-oznhQTKu9rqwrLcYYSNfzsQmn0SiJHd0CfzzRWIgd2vnoZIy2sNbPHKHAs9D28lb30dTONl98sNLar9-I0k5sOT1f15Rr0QJf7q2e13rcsWOgcSmDivTnIAu0AFwlcpcO1L-_BNk1B1h3NCZcqFS3blGDDVBtbdsMFpGhcYhnua6DcTjwDQMAwvTbHj1276Pu5Y2zvt2l-b2Mtdlv3UKCSJP-xAzo6P4EGb890GxISXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CmCx9OF-EhyxrDxn0lYwpx0chpSTarzg1AZH2nUbTcnUbFPuOQgWkPCHjKKLnqrhdR1jpgP4-7I8NWwWVR7OvNhsTtoRvZgnCg9tMClpawIasZNc1wASj764U20lZ5X9SIY9gRb-Tp6MFSclBJKsPzjDav9HDxXwejXB9b0AqLK3hJCB1iwhJKp7eB3dEpKNiN4osWxTwIBJOmUn8eZ57IgXmLDiCahCtae87vFsXdEnWvyyCB82HrZkJl7tCODC4NKN0-QdziAH2KNiXMU1z59MaTAIc9dDfLupDOkrrdRVaAeQ2m4Jq3ZTH4jmevFQk79XDnNcfR7AtG2ZcNhzUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ExIeYKBdD3D-uM7LBg2tUaXpWQ1vXZcil2N0ofI_sRLy8dWdPtjQQM_nbXYfCcwJuxJAtLQf4uxvhRFqSuP1Ggitx0mLSVP0NKwUY6hu0m_jLDmZ8ssBLcuUeQnvoOd1A4961BepOZiHxDtEae0qfmh1pbZ5DnF-l_NS1c7sMMnMIb-ZYUbUFQGv3aQsjrjbtFlXboTukbjVtyCOrV81X1_WOgzOEky6uXPe8Im16Wwl3IiKptEflOUyDrWtzctF6I-yClJs7G-9_iLA7yeyfvJjJDQr6JLtn_9DrT0DUSlKaZ9nhNdf_PijqVdb4CJUEAv-IfhiOUT2WO8NcKciHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yx7gkCuoLwrI-vq6AQ_-xUnc3Wy-O8NgtW5qlx7PDripnSXA6s_oQfx3tYdqCf0Fbgl_qVFi4tutXeX4VhBYt3dePMEacy2EHtGcgqrRP5I2JFOopBT4NZzsdbI8YLTkgiv-IRFI3u2w7Bw7AWu9qb4X7yt6pcBuyQJCSrWaqEE1b65GRf8PJkSVYS4Hh_YFTZ5qmMWY-GmvxSRVrVRIRC8IGdSR0OOYJdva-JNuLWrdQ72WmQtJTjYXlYSTnquW1v_7Hn3QVDgLQjgakRB4SfZlnAtpoJHXDHiqBtw5w3ZS4v2JzRwyf4gKtAf19h2Q6ulV-vb_5m96NGQZmtkgqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mBMlFyCqGR81XI6kxVSkg0PKK3h2HHWU4Gxb1LLvnttqvGCCpbzRQwf819X5BYjHbCuH4oCmouyCS8ikbz_UMCYIGsmhkQi0XQLwpOfYhkqqa7B2V4Y2QGElqpXbE4NKDVGkqU6f3dM3OEOG6yjSquGpB-ikbnJUbcbX_H5BFaqrenTN53b-loJoC1kYWSrMIkvXylTDAX6bh2L3ctm7inKh9jruOQiFd30Fvs5bj_0BJP7Gunumpa9B5kvNC_wDwWp9qS-G6Pa_vVRjFeCo7Szlr4kS0uKx1fI4l5ZokmHMOXU11ljaVIAR72bVwYddaXGm1XktGEzJ9B3TPvcTNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DgP_sM4Hmc581uOQHLc-97qKtoVm1PComr48XfkJLqgbUKQiSxwqMfKDzw2ZIGrCq2qdoZvZXyWZOfHCt7CWTrmadVEXY-sIGGROOJodyXNYmVFHDTdHBb43vnZZU1ZzQujnvZUyl9T34q6vIOqJEMxt4Ro3w5_OLDXCtkcWPoJzRyXWEdxQHTQSsNEwhGspw4yAZbv-yADpUCHQzEmM4ssmz5I2IXdskT3SZlOqaMw5V2BAgHeTp54K36hm2EIvc0oaz7AV-vH3lq9VuGQf-uXJRqXDgeO3g5X2XIewsKkCc-S7q7oY2jda5ioxOCw5uNzt0VEbBAxwQj25dNreTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m6KXRrjD-GmBzFgGhDbWnJTdEA1gZvGgccXM4jktyBXNBrXcQ6xd8fXux5C1TgjQDm1fdP-cecv4FGVC6P81TeGnm2eCqf6zpTsM8SfNbN6vapym7YEZBy_fQvM2cSPZDqw-aOW62_jrxFn2T0mO4afXytwLSIZ_BSY0UAg6c5NMRfN6aPTltRQzDNMF8LDeBfzWGCZn9hIOdV027V4T_hTNQYoUyB3sFkzaAxSmmxiIyiXCTSmMcYsayJh4tiNOHWxMfeu8G24yJ3thcfpVNUaZ6ltXnekBFaVJqXDu5YdELdMb_tiFCjgTX-vUGAJPlHijB5MDHf4YXElxZg2_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLl3XwUF_RzSS9J9Ae2LDMGambuZfYdHEv-TnJFSXKSbfCu0aV_OeIix6idBmvTqFOFljPZxHRbL48GOlvSSaWfgfhBiCl50hrMkr412e4U51F4S6Po9lVcHUNa55EP8_dXPWYrJ1_h5pYNaKgqygfVVGSCJxkyFSpsqpupD8joIxVCTMM77GH4iWfCnSRH7CSQr6XRMGN2RKPIGpZYyumNv34v--8dCjUpSHgBzriAd6i3dxin14trVobwYSxEgCGQfQ4JqJ8AUrUKN3SQz_5aG37XkOwF8cBvMppOkDCxew6GsdZfb0DaCiQkUPu8U_mXe-Rje6UsXSxxWO3kpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4W7GHplnBj_D0rMXs04-gMm3oMkRKkI2j0P23Wgd-gAiI3Gh99wgfGTJgD5ltSkVt2vOTE-APb2nT5WItBjs0gqxsY7Ol1Ulc9RYGRYERBG_hdvTIWl4EWKmzc-qg4swBr5bux24jiTX3kd9tEPtMfCjGPMCEaJc1-xWIfzI6g9baXPMWRSRzMxCG-DSce26tFfjZxtLpcATrH-PYzQtn_mK7LW8GaPU-CICvm9cxauuTtW_VX4qEDwhhj7m7iIhlmyhnnlHgIiJpTG5EEPjD5WLQ0yrhKxcjPJ48ZeUS7E-vnjOr4OZjNQRfRjc5UgrvnLn5fJpUzzlYO-K-1usw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UlW-QFR8mZj5-w-SUWDNjQIzHrp8-y8HQ6bzvxCOgporktkTfbNPoYyZQRIDYaiW6WeNUaBFp6eduP9xS2dRf7obDohIh4tsd2VNnwJscqdRR8g9bIoZep40KEUOb99iXRJieiNbqPEIRJORPDWZCCfLJ1LdYgPo3UEvHAT66bKYdttivcNADtzgdcov_bpq6EKpw5wq4su7oqjyS_tPB9hYom_RyyshNlOAf9xuyJvMjCaVCTkYXFMINutCllgdYiyTyhFv-IkrAsmRnpfI1yLbvt4ba78TBF0RabU1iCQQYDc9phGP2dz0vghaEvPb22W8SKnHKt_MuPXmURUDvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y4JQFiq__wCIR5HBXRNzaWZEItg0yaNJuBb78K7it8BPpvLQzDqEhYbTO9pyc-Zsaw0x1fLcLAWDViCCSD2u9nvlmKLWYz_xo5Uq0Tldj8NlHzMA6xewOXvSAA8WIG3hSzyPSVxyAEnvNlNV1oK-JUg7--ctMI4jatKOz21hri6M2nnpfJrzyCFLJDrrDY847jirJ4cxOqv5DJPuYqD2W3xHC464jdBIyW2Hld6w952wWJDPFCT7Fzupvzt9I7D8AqpnFeZdHjdJKN3N0QhBkJdFYSaaKIoYLrAvTOVGDZllG9l5mzgrszD4xgQq6NDys8y4gcUfxJv85_1EfFbmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a64ntH_CA1m1LCzEDoDQoHKXAwgekibPASzZxoHejAaU3SzkxIa7PqnEhIwfJqag9pqDpl8X13cAyhIPIvmukIdqw1eeIN7bWbR2HRO0TIg2Pe7Q2INXDol9SXzhNOX0Ljp06ZfRa99LFEbkilNjZ7GAq7NdII6DYho6DMoxDWcbUxJtyTmyNkmaTsvhmWRMgK3f-BKtlBLLWxcRBYkgGLT0YSxpaXRjN323xaAJpZQCp8466GuZwa_EHVdgb5A4CwPBrjqR6yPqjfriGJsnk9oi4Wj45gWBvAqGzHOjiA9cFvRSjpJD99VNA5aMbcc5Kf11sLil7FdzQTGsEJq9eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YMkjAVTQUfu-IibxKYMM4nZVi0sI5oW1HU584LgA7SuICRrTdcMq6BA9i6psshefgEKc2qUr7HQ1vNVqVkz65o1oxAY7nEGQjaNx9ZjpUZ4q4obpda3usPYncvapWCk4v2lCQAMf67zcW69nwm_X3se5E6s6OwEjd46lEK0x13SD38PIlg4e44VZ2EevG-JBV2DWxhobVQe3xxPNHbpEs6uhy2G9vshU2k1zyjS4FElWm70ka5ItbnBT-g6UduHCjPZFnBar4DENlsImLwVx83h_rofpO9vRtwGyY-60KPkuDkCNhTWzmKIzodTfHthH6_qfih2uFgLZkRcQ7HJhZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AqZBfJhISLa-9fMNJbVFWkpgSEHC6jN7uO2Yk8wVlJCWFniCZOZEc7TmZeEIVrO1kDbhKr9C3-2Gw8CHOcwwcTo_l4ehJd1-ooUrV3gr1aA6D326w6JhT10gNYKwofeN2ae6WKOWo--s_MIyej3rmgUQ6GLWcJhd6qs08mOJdUKTgi8lTt-pS-0AHuSpX0ROBAA2Nh65NXWVWR4EXu2fFN31OEX7gwCm7T2QdloByqnDoOIs6NCOUJmkv3O6itxYREvvdguqOIALvdTGjALqqdi6GZCyzOct6HpowjPr3Opfu-W70PcwUuSWxTueYqQe89n8DwWFUdPU0Oaoy6IOow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XaTHxiKGrIohcmOJI2EamWqIhGP5vX6xPUJZ40HkIBQJ-Xu08Pz_dSsZitAC5y-P_4xQJB63AgaOGcJNb_k5CxVO7kGScYiu4PZNa0aSNlzRcrvpJTwL-fk5y61JF6HtaNUWdXNciLSxKaBjg2UnySCPy4Sr0j6vpdz5OU-Y7-n3g5k7kL-oPIOPOOr88eLopmty7RPZjsDJGdsIpLlA-pJgv25rpX-u1haERRq05Qa1osR1Qsgfog5m8qwc9BPNRw8S-NrbXQPjISeVp5rP1kPBMDJk9hiEBbEk2qUFUhX383qhSbZdLbqWp6a_l7azTs0yFiML7yiUyOxkdAYCGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DY-7_MQLccFkBPB6N3xuFxzNQ2AS5RaYIpqZb6UOWA_b8yyV2neKaM9-p1Mkpkhid5u7F2fz7bEgjVfE9pBdadhwbDrnLptPca-9B9ZgwNuMgEt9x1WMujxT48Dx93pimYmxxSnfMCUXR9quQQhb7SKhqZQ4TbO6Zx36dXeQJ27hGoIepzTxz1TqFS7aLMGWAevqUyFARnPkc3LxMUUxDpOOD-XgNdcGDpF1RGmlYZbHCaALFiz1SWUzN4q1GT2eMXsRDE3GT74hEQPjt0nwmLiaUnEPBTr_X8qkGV3TSzqBWJH0gf9PT8kTxB_zMrUH0d5hxYI38RtZqkuhRECGxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AVlKMZqEI0wueT02_jRaie6GFqK_0M8EMS9vqF1iTed4AHLe7RYwWMDNk9sK_98b7q9zSBuPL6LfPCbcnUmYSQpw-tz_7IIyqBC6YnAHxObVc1BHuECmJXeeBFBlWrIjZ6_Ms2-Pr8-aw2cwV3KTcvSAr4y7k7Nx2Hn7JhWunNKfGB52W1IPuAsQnUXbHzQIL_LK3dGY0cw5nnyUy2sWe45c5UCfc_FdYPMhN-Lhyn7wY6LWBbP10gId1YvNjfnopxP6Gt63oLBIlSBNAIQu0V9xXIPRLdKZerMuqTf7UEw6Rozh4qX0gOFzUGhTQ7kdpGaAwlTbXLIgHoGvw0lUbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L1hDhTzQgqP5qtp3qFLgA5KHJ0ZrnSlX4Jk5XDhab6DQQ1na5wBHPOHy4_RXJpyOULZQqwo1dQHqI-INeKLqtFFPcyTVoMOVp44esVEKPlqNEthVAwjfWIyFA_JBsJl5b8ntUPyNNfwHFdgKU4cgSLnKwlefFcQvI-8zW58ojnzd5WVKweO86wxU4UFTNfHmXwIuQL3x8WvNmnpOI_CHFrmz1SWwhDoAPKKFC4wQWRgHTdT6ZRAdl_u-r3POXjYquUVt6tH6CcO4CEhDwD9gWn4POujs1hviYvV6wcY0C-ZW5LOLoHjy2GG0cDU7WpJ1YiGrG_wnLfN4A_fpE2aoaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iy3iTDOFqEbhNRXye-P5P_kx2M02ZVgqWu9ZWv6ZSB5pjtkUYh8grAPlDFX9TqVTKAlf4ch-8CZnJgjGwxkzoJxUZZ6cUW_OEC_mYCoPPCvRGz91AbWNWP-5PCOfrizwpqNaBl-MQCaPcMfbuF60QZWx4wYAM9lHCYqUjOj83rrlqHO5_DRNlLXxL5lqBxaFC9oePuQAcrlO5hvaZyUuApcttPWdDnCoA0hDDztub43YS6WQDD4rdZPd29Az3HdSVUJqkgAh_Ylc_iALTOrdY-cYQ2t8XntoIqGGkSufIraVjc0fmbNPwgTwO-V3u-7g0AIOKWxK_z5suWva9zEDOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3E5sjHxY2lz_hXiazAStfLYiWynoqaSzp6NJbWlfSfzdFC_kSUG_Fwn4LHxb5uVMeDIULMKF5vcRJNOwFX_zMvjkd5a7avf05thrptGrCL4YuTfvOrkYusiI-G7Lb1x5uSoMbOb-6bBDmIZH0ep1JTj-Pdbj0_ZqD06aKNOvbXqFQX28BNrxy-KxDMM9VXgC9nJdTFRC_mxuIcO6lXB7-qsQJIVCfXbxkqJvGRK8fPij8hWKojZL59cRMIi4_-LbA4jPmpctXz63_QmOTMwaYTuxsmyIRf6jrhUwuxh2NNrkuSL__y4vI0Jtcjlro44vcfY8pYIMHocxoMPuheW7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2kfX_CteMLojOhY0TBeLwBoxAvYu3F6IK4-sG9Mue3WFyUCPMGccJ7RmCQ3BOlz663X_65QAHLI3GSMOG0fV3edWkrdi7zz2r_RcqSwVITbiG9z0PflN8jWpWWuHH3ZoPCxjbbadM816izxE2gX7JPKB7nnAuyi8YobSli6NooaHw26h05ADLqmblmXcLmGxeoah5727FLNbdwUlfyHag5a4gWzmiNdhbxRA-4IFKkBlf3__gJnc-SEaxTO-l8bm9NuE8t_SpIdRUrmA3uLb62Jk-O8l3Es_9TEc0SzV7T0szgRIt5QDa4cGO_KLTE2pVjl3Lhze_qZMwoDdFiYaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ul4nvvI8jZSNboeWR-Vt4EZ3kd-G7T_Xi4fOesk-UlPbjpCHuJ58A4AfY0HU0SYnPPMsJqSduCfGodTIRCCXH-_XUmZ0bN7ursR10YmoWapfFyJuF0A66Mi4zKW6ED_bAxWkp5SKv_BB8CZaLZoQAuoQOBNqvV4LI0hAo3gyar1AD143Ce1GD_oqI8G-SXmvisH2I-O4C_P42VrhEKPcOJKZ-FS-173-_IwJ55COtJrsrf8qlyxii1pM9N-dWdBuKBbhmZuAyzWyOOTxphnWbowD31yCBJsJD9uY9s3sz8GZFRYbFCpWHxyAWC3w3lBxqj-xjgFtECHkxjD-8Hdl6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d8Fy_b3O5_MCwcADOoO2FgZRPlzr6U7K7qS_obKeRB6u9EBgdtAQbxekn-BlKpQ3SJAvck_kBqAx6v7WKGtMucsMpNNftKEdt05S8h1exBV4xcp24ou3XqvB9QIIWGEeE1F4BS6ot9aUU7fbI74mbPKzIL9cmPPoDSroJimzC49MueW0LJZCpmVUKp6O6f8D626O0esd_EYSr5dVLgvrQyMKmZYjs_g-jMbw6Wq_i0dPsAUMOAjpdaEvzTfA_NwU8oUYCn2S2NnzNNYuUBvdSaKMjjOQN4J_cmdS_DP56snaCnwrdMqLBWRTY7h-ni1p81z95RVXSxLtijQvuDvTYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BgZxDjO483pslXputyFQVLqscpOIiC7Ys3cS2nEDPwmKcEQw_OmI7UyTz8hBlS1GzwenweLOIuHLr0FLskgtwfQ85P_mbb41iVUfckKl82T1miu9LfeEJ5W98u0rPU66oCLKwZNYl5SyP9dERm2Wd6fWJBH2ca4Fcp0h8xtfOcSSxYq4Xc5ynYRNUzwIBu9pWiB0AUr78Q-GCdk5McfMNMV1RLCg8u-srDMgZ1aw-89xqzP4KTD6Kdle9sXxnOUFThDgvoB8o5ZeCdrAONkS32QDpd1l0ezgzUBLkduwi5Uespp1Czh-Ki_PyWuGtVsZ5-gVpPoicNiAtFj7JbR91g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdWeszIZ2CKVMBSRqINyGRqRc-QfLA2uzNbwVbvH4Hbb32RTrMW4wsIVdZIl_VE4UmSI--01jr-KFjNoKP57ebTB0spSutYFU5v-7IyP6piQI_ldbFZO7idKtcu4EXDXJKSvP56tchXxZcubIelPtUEhtbYBDyh3lWpqsecIc9j0LQ4XVarOXiYrhwgDsV0CCReUuMnSU_fmXSNCXRrHVnx8zD7t83rwcc0Sn-OWj9cq3vXjGA3B4feHHQ1v6KLPFK9Tcgojmr-0cWb7FqPjH8mpQNu7JiUJ2iiT4vsV2DLTUKeaZgwcEYSyh6H8z4Zgj_cedf0JUYQwQyKVl2Ei0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fdZa_B-9nBMRCMlnn2VxodoBZZLuoJyzZrNWCwmx15qzAkon2JvJUxvpv7w9gtNP4NbGhkPy2weEtM8pm_eJy7qtGQZfhzWZ3opCHXMR8xVHHkwyk2qndBNn77I6_L4bqH0amFDS5rfnR1TsNOmsmZAtnWw2z-V1gZQyj2Ri0JzYPQn5AA6n-vQakWnYMwOw1zNDb9z_CDaFFx_yk94XIaold6eriVPcN2bdKhx-TX9FzZsW6ZFh-9bXJ4Xjp60_5E9PxfjIvcK_cYnMSLBp_E0gkznWlUjr3eS5iKc48hI_2A1phNllkgIQk-Wv3kSu7gwy0mGCVBLBC5IG7rYQhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wp9JWLvDuAsmQqD7jc8PeU6Telc4H1aHSZ-wDPfIF3Y2rUX3vFmlytI9zlQJOpmhC8txmm52UqgvZ4f_veGxCdBkz22mWwOwfNO4cxf-038gU3mGh-MuoQRjdw3tGjLrgsnEVxwhgJsvcX4sKM9GRoqoWB_zdzzplPrbsgeRBy93bg55QbK3CWgrLgVKTeI_MYZpLhZphxg_hoZie8ybJE2K9g2kcdw5Naoq2DJ_nBPJqdc-rGHNpjvN5EwPcXjh4tlXopN2MB59P2ieqaweqVpTi63S1yo39qsl0_ooSup9DgvwNX7tqBod1y5Tb8vF7qVsw0XZzbjC-4kaCf6Nlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SIpPmDAsAXxzemtQ9H06oBUH5ESvXI6klW4pkIzDlZdxOKFHk3mpgPXrIZ0UGyflTlrNsAm9VIsXYSvMFB1fAFjFpW03DSSpPnH0c5hYxaM7gPL34-uF91E2t3bKYa3Fc99zL0f6dqCve5gv4sNBRu25y8mRLKoDr4wkgGUhC19ZxlYE6qm3SQveigpSnF5LAA3ixJ0blVUydbaaJFvpsT7cX9Lu_Ax7AW4eTfE9ki5gOWKY4a13r16HFzjHYcuuttFY3y9vyq2uWgIeUF28bZTAAuDCvGt1OUr1lzowIW04lEwsQBbm-etcxiEgTGFFsSUZuXblXii6xUB8VYNy_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JvFyj0PLL94IhENhQCmZdmV6KoTnmwkVZDbJt6KpRIxmZhzug3iA_F2n4Vva1SBnpJc6Mi6TouTN9iKb3Uvpf9Q_kOxbPNuNS-D3eHFYJhDGz5h7oV6shNw0r_M-O3va2YJBg8lo9mbkZ_g32jUpWMEYz8y2t78f5rGJmMj4_zZcyHlBww-Zgd4s5FURJx26v71wiRu1KAIVhelvIZ26ebmWFTKcLGRK5FrmnkZSJJ--Qt8nF7m10AYpnDDimUBbvQsUTAK56Op8x-SfwWqsBt-PT9CUPdS3yoc8wAfy80laG7mk4jG7yhND3o0ZJ9jq7KT__tDXt95n-ptTOQPEUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ha4IS7af54tPspXFBNftzh21JqZBNhyhBTGstuRRLMPWc0F9P7zFaHT2TZW1BW-4Qq4Ta6mhkeWD87PWTwJdui_KDHlkIDAIV7zMBBwgF3l_QuO8Ic3sPSPwf5lSqh-eFN5j5yZDBnTHlLpz5nEkEf5Mj26ILQR3WpnkR0XsH3bvnP1899yrm_9XlRYy1LXrEbv0-DWun78Xe2x80yUbVKLOZgKs1OJOfHGrVzhqLevx_I3PYvGZjlI01KdlY2yNb0tkUGNXdDtyXA9_shBmPHdVtRP04tFWsFs3KIotZMzzst1iMtMKQmPtchnzp1sNuOm-cVAwXUpU8P_UDXyqYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iRr0yVNwm4dF8GNucMHCGN9bk1VCBExX1YcjT58jm4LSRCzHwONW_ojFGHxgNVm3g_6rkglhiBps2jDUv3M6TdsgowlgeyfaXRet_BXAxWfVrSUhzy5lcBoCtFGfrcaAUa8yVuvIL3vjnUbeIwURGrYtPdI1KogeWPnYSOeMmXBI7Z66eEIt76PZbT-AgDMWokhVwR7Gl_00qX6VaPzPJwbU8QBJoczE-SO2zgYkUrD0Bo14Qk25NdbDohabYnXhMCBH7co9ljmk5wqjnPg_HltmwIN1WoeOya21R_0UdmDqKRVAUpdgkG1ikU46BKIVyeCL1CBeT8_khb65E1MCIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oiq1yOPSXxw2uCxn4FoIH11H8-2jyxSwxBxvxI-1MzL-b2X1Q2zX8Lm52PHW59gSVtSEi9F0zfDcH5BdBt0-WlOIlvDUrv4s1Vhe7Pjtd7LpdsVXnPrRBlgJzsRQwgExGOsfO1VYI6z1e9RQewck3qDrRsdh2nLW86AdF8Ztc2tJrfwFIycePm-RZv6JTnR1Uuv6FsWMI4VWVzVfvQ7iC_yaI7iCzv96PME4ljPybu4lsUcJA9-BqiE23tgttLHl3WeW-tgL61Q6uaFXScZgZ6n5C1KpCvwzynpQoHqwOQvGV5Ee7VNg5sAgpysx942fEe6yYlZAymSBCJMBkImcZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/epUjgXpWHxatiyuRzeYFLm8vzLhDlw-8l4jsvP9yhwji7QB5tNlKCKylUb7Xt9VJfkif92PDMWo1tdyP7_Z344f3sqpk5E2r1YwqHH-tngqGzItRrqFNeNnblVgW_c4Cm_Spzov3o7tirMw2fTRZYouGYYxnjRzqgNXhjk-nZDJAy9zHMOh5_3d7AY6V8ouFwakkh1Als-cirb-1ast3wwn3PYRTcI5Gw4c8enFpWOCMcNp6Zhr9Pg0hnvY6US2Kij4dVdwPVqnF7RdX8sebUaIvWuPoH0gcHS2GDnxfcBDXDdnzNGSt-zPbgRBFAEH0iyZZVch-nDqZI0sP6Qkz7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Olh_BKxiDX_LkDGtHrG34OYQzEfzy1yCpcTFMbZPeewjLwFqwNjDmMB9h0SBleSpVl_zUc3QNTrp4oqc2lnwBfoyX4QW7X9DumizObt1WwlKIxF4v3DLTIHf3Cl9jhB-kgiljHGwmw7uiSCJhSc8u852CWEszwVvRgwbz2oj5vOoYpbOqMmflhA0u8PXsj78rpCdV83mSfCL-b2C2Xfj3Dukfzj1I79t_ycYJMIzX39MYI1FDLEKvAQk3Ktj68Nmxulbp9lYF5Y2Qio03NmSVkNTALvDAG_be2qQh0CrMmQ3QsriqXP3g0raizAvSO4coxpKSdG7miAKm_ljWcLcVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGeZ5nFiMSh-vOWe9fmBbrUQmUajhgjUOdBc2Me8eKobgIxpz0d-bDY_gP61y4HcjhDxvZ-EKfcchLYmvsI6RMPQYwZL9SGytuIbZ8ZE5TEOvZeojsPYaaCr-nlvfzv7pyrOfH2c4ZjYUm9SrrG0QRK2XOCY1sPIGnZlLO9D7tufgZX1ObMMAogtsMPllKti5xqwRqZx97IBBGY84KbBqHQBjr38z0gDHq7JLWUOc9sjN-rmyhhsJumz_ouZSV1Y8NpEDstWGOoc8IOKuopBfe2_L7N0chI80WM4lPr1fpbomMIPGbiGQJQwHdAXlQF_2ncZqcGTbEjkorZgMkHk6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dklbv4WcuKSi4KwmDXUECNWp6V-pz_uJEoQ24hd8DYxaFFSZHfXu0k-9rS-gFfv6cO2w-sBOzbeIEN2QMqQwtC8t9ojdOYViTf01r8aghB9ZJr2g-duR29RuG16i7JQ6Y82JCu0zYbgWbfTUW0MUpkBvgYD7EVaj1bzvzn4Ru5Th0FB9Auomyi_PQwJv-3wFZZh8H88B_qG4uOP-PSRqUhdrqmc1k_5yCnBKPGyEeQe66lkpdNivXyExaJGvnuSRtLIgSALE3vWR0WomRYbs44Iu7kHqSvWZB_7xlWSbwfWFGb9nG9N_EPkPPv2V7XGNzjRwChQ3fC2MJCrIQWP9cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIKXJrzjZen7jhqU_4uLyOU6PlAYJZwdUmwRhoSF3veOiXc3jvDkyz5Y4nS1BbpOzYZq_t7Vg0MuBMV_xgcvWLuxoDDPJR3Pm4rrEYAhzcPwYrAeo1soWIkcO75FpPrEVHF-QHPUROKqGF4_prYarHVsEuDmjE1xiNDkkM5EnGo4Cp3ul780PBP-iGimMBAXAHjZjpWvNmUkny7xWcVCQ8zKiM4M7cmGS6rf_omTXiaWmdY0gBE8IpI3g_0WvrZyG8GiT4gpMsGGFTFEmOPJcNV2BVzlf299H6InJuVCwOqIeBLfcva28VuYSu-kFdbOMOrvptCyurHOIfHbCWV8-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OSpsxK7z601q8XS9VA6Q_PKU0u88HKPrtq-4dyEq8WPvB3i-Bb2dNjIO7qiX1AibBuV14KPsmGSCmZ0-2uiPmxDM7tkZLAxPfUNu4SfhJ9PtGQDodfS2VbK8XlhioLEK9QVpPzwEpKnLU70FQICICgB6hCZueBCzo6_UPGcqYAG6BLQnQg13rdfE3vIV1_V3Dg8pBsqHX0hSy0Gui_y73ILMprSwqDDbJIRoajnQpCEsxnvFWUhUEnaYNw2Tz_eX6G_fXdrggkiDTEsBYZy3TU48RwoPMsy5wXH_aQG29pE0N9uwwgJArdFRjEY3kUFhuvyDt49nKKJL3Wpzv_ZlTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sO-wS2QKrQq2mzsPeyG6pITUI0MRSLxq5v0butdFgaNBiGC0OsxBXF1ERS2m03HdkpPM4uhCf_P3udL6KQolT9FNcUH-A4SLpjKh6AFwalTC-LK49QabMgZylrBqEoQ8MXSKppAFcg02ml6k1oco-q2Qrw0CBzc-1dysisG_Iq5g_cuAEf4KkPy60i22HICx2uxwnPp8KDAmtyzQ4SQvlccztbmJIdV2dcVHeZ5_ssHZJGRZ0772ZzNNvtEpfe2-6Br9ER9kc-WCPYk8LL0vDBAqgYMPgYOAEA46yMgKztR7HAp7jTLFilPlHiWqXc5P5LQwaCagfoTFk94N_coz-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgLqvySSkALPLxvG9DFrM5BnhRuR8WBKKHVH7o0GrxvWRYpC9ejNAZ49UvWAtb3-Cj1jGk5S6U-II03FmlEb72lVoqHZJ4a71qfZRWrgnc9-rHhA-qDOBYftA0P_pLqthgyTetiQEqu2ZkZ55QykQWQ9vo1fJmH_pxXJAxi2fbMiRxJEBZoF13D-owJ5iWlofoJ_ohL2b0X9Gkyt_BjcxsbJpB4wXHGhqZnoAxvGr8-ds_gdw54QTT5Cav3RJfa527IiE7ra3VVBV02urUz4O2kswwVbq3FBrRxN4F4jUriuxGvJIQ5M7uKuoNhvD4brmUd8cIIQl8HEDehxVlE6iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAInwF92uI6isE9c6D1a7jjBvCX-l8oHDjh0Jb2iN-mqr_CNx01C95tDqCLon5_hN47HQ9CNyvrT1oBfK_9bzbFs6QQRWa45vzfxn-Tb2HfxnVGz-QvHIpr716jLYkz6A63xVeLjHr_clYs0EkbNc63DrL8LAFjBYmpXqlPQIcXLQVfSOEdS2qgn8KgFL1-eTVOEJG4HwqkwZ7fNsnxGIjJFTHV7QiGp0LtWF3bB4PL4rfMAl64E4YPAuJCxd5CHPwqpvCcn1Y08_gfQPkI0X5GdP2kG6-tyX7lajdWCuoAHh2i-TLzr-kC8QdzhIqbaSxiSTeP2Ivr79oQw3qddfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o_GRRMZ81gVB1-QWIgINqByYLkd3Kv4sbjsJauQw_Wf6IYk7wK7WjJuiiq5YRrfPcAvDsilcm-27WYYgzDw-wEYJC_8zmcTiIagLANbPX2jWwRgFM005w2CO6DdiY0_4Ang1joVn3p_gTvhJ1qKbYd-XnytcFxsp0vTLDo00aSMpGZN1f7PwR9PX66xazzK_-5pQCSyeQkyLj31yMCywbIhkTwUPzN1vORcU9I--X5qVIIY6ajlYNAp7Hxnv7RVmUK_b_eL5ZVdEl4LHqM_t9USrDW8WmTTR83MnghlnoB2dEE-ywZr0-6t8WfVev4syrK7Alr0gcLXpjDcBeciOAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
