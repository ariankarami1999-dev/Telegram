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
<img src="https://cdn4.telesco.pe/file/PYvkd-GTfp9RNpmKWmsuepLgvDaLAPwRDvz7YXofKsG_C-LMOf7PppC9eW_AR1JjDu1K_zN3hSYYsV9ZmGs0Yvd9t9vJtqDQ2kyyeehLKb3SxEHnC2DC1ZTBOhWV31OlZ2_VOJObeSwD7RND4WcFRmHN-6gImuHzvbII2IVMA4DCYaneKJmq-OCEsQ8rB9lZ77kIVRFKR3aBTMjCWrpe6RkuDQ9_D03xAY7anW1INRYqyVoWhQt-8sjCmR_XioTG0M8xRlyi6QyQhaxWppCN4PquuF7D9L3iiRnocQRSCwcc72X2cDpSFRp02KffArMwGsL_Si4hIyiD1LZatzbH-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 23:39:17</div>
<hr>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrNRm1kIEwuZqmenYVIr8_HjJDOkg5RvyCW8kkLwVU960TT2hHLdyelx4Gw8a3MrUSaQtFyVhpUAMvhDQMYcKnIedO-uAQM4RBI7HNgkqxeUuJSNH9joIvO8YaiQ0PMOQBa6xVF3Ov6gZ5AobU-dRLokAm3nA4wdN0J2ho0a20JmOZD-Kq1gaVOI6E7W6E3SW-h-zoO2bGgavNJLdPLhW-vxS5TR3ebuoRALb4wWauZDYWc-TgU-KY1kgMaCMoyuCeYV_cgKmNOPpbFO66Bsh0Yb8hveiVDMAVDnaucFXTQOweR93IHABxa3ijKejClLKOnCy_BGU5HlLQnjf2Q5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFAHgaCBLOtnj_4Mf4EEzIWRYJ_RIDfyYj8LA96j7JfbtvWkT1JsdBO9NywRpixZS5ZbAHjHmD4njphW2mvX0C6u5b2Dnh4lIR7xyEfAa6rkh1xOPObDlflG6po_EF0FSIb_gcV5RLZO0etLbS6ol9AuFqrFgxw5B6sz1rTEW8DRBh3tUdwX2-QsogvL_W_3eQ06s14bAzJEivA5YllCXIaFtkJxjY_FY6siJKzx6JHK6--JnNs2B65pA0-wn1_4lItOiurriEfbV3PA6vPJMKlsLr3lV0bL1c0fd8OIThsWHAMHRdzCM38_R1m1ZClxReSD5Fk3J60-GLFls8shHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onpOWQkQ0XwlHH0k93a4FtttvtJriK_E0bzxTS0g7SxP_ZeKszT9kCtDOSXnnRdD5UUmVClUAlwSjoXf35VA0JQH97PTtEiIbk-gTL3-URpX8kdqddYw3iPjzqYm9GOfFFyUE3bW1LCAPq5SSNstw-bW9_2BHyfQ6HpTIpj57yng2LSI5-fgvE1W24epEfB5-IVOZ_xpDclZEQMqnr8vU2b4OsPL8S5jidGNf2B22MJ-hBRfQVU_EbLx6HDoUo-cZQ2t9N0JlLEszZFUA4tWc6tEMRPvDzTkm6iWIZS6oGMEnuzFfbsI5n7_77lbnIvU_y5zpzDcC1MC3Yyuyd16rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIk7SBkkg9hdb2P8J5t64xU5pLvUo8ZWjUaNOwM1hdnvMKoaI4R9tkGu4wIMCYDGMKq_hLOGnKfY9W3AM9-VClSnpou6veLT8y2T-4Z1IDqqkcxkY1KIaooxneDkTD2PUGfKeL5luRnBYVewxJoAosXaMtJb51puzxJaVU8oC62fX91ES4ML5E5rvNHW3A5OFS6sXXfPspLGD86uWYc2x2Y6gkPz7MmB67ltWSPJ8wxntdROGzEbxtNXlqQlie_FSKMUkkm79cJBc7oUp5vUc18uV448WxTpvFYHbkQ8YixhkrTGo4DScrF2CcxazoIR4w13JgSeCfhSg3bKaw3Yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=WvI1iuhKV7ThIxt4McMRn45tNyKPHnATYZ2qXfE_zFOXvIEBNI7Tou4B-rKcN3tDaCSc5sAL3xUqs7EOFy3Y9xUUv2D7FMh-QnPecWsd6EMipRSzn8qH6esMn-CFsItK0_uLOFpMawhXmheHrbpl88kQW0HfKrwbJWqKGAlDcGlgLjYtrmH8RY5TpgzJXQK9hoqxDQ-wikf-tdhbaichRwV8bdK4lPAab9kWzBQkTkW99epNXjzq5LqoEh4-JvawY5ZVJ0Ldy4GQUapkqgiIHn_lihPNwY9_tpRgVi1vSbfvsmiuAzXJJWkm48vwsOZL0Y761AhYe2ZgSZjCwsaL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=WvI1iuhKV7ThIxt4McMRn45tNyKPHnATYZ2qXfE_zFOXvIEBNI7Tou4B-rKcN3tDaCSc5sAL3xUqs7EOFy3Y9xUUv2D7FMh-QnPecWsd6EMipRSzn8qH6esMn-CFsItK0_uLOFpMawhXmheHrbpl88kQW0HfKrwbJWqKGAlDcGlgLjYtrmH8RY5TpgzJXQK9hoqxDQ-wikf-tdhbaichRwV8bdK4lPAab9kWzBQkTkW99epNXjzq5LqoEh4-JvawY5ZVJ0Ldy4GQUapkqgiIHn_lihPNwY9_tpRgVi1vSbfvsmiuAzXJJWkm48vwsOZL0Y761AhYe2ZgSZjCwsaL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVx0G89pxfoUR4kPsYzjXUt5FGR1EOAJfeUnNESwHvK02-fQ6of4KKyUJ_60ZwAsVQFapTRZXFHecuREI_4PNUHtpMZeIhlJ-bS5z_cjzDAAHRaSG58hOHCslSJAcH2-g6WAjIA6cEL5-EAWW7KjDqOytKwf-5kxvb81pe1JVYoNtIwc5aVrIaO-vB8ZZxWgiEEeLCRmy7UgAdJ6QBZR7C6JzPuo4FKJOnRy-E8E011MKb6yDiX3FpBWm1d7OTtY1uDo1zL6yYzJniGKf6eun4763JieoGkbp8qLPX_1GjOrNJjeS-hdheP6VFnmV5c30Ypmtj7kQRZ25uxXuLSxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlBXjLGChHNXHVWE2n6vSVTLkRWlQfWEwSf3v9eOM4ecuA-aojg0M7RZGBuwB1SiEeXJUbQ8pRO_99VOd8GOWrg38-NkBsmSP56gI7O4aQZfCuUMIdTKBO3HQVfcQcfNR25wfAUXeNsRdVpP4FbXaWxTV3_xZvvg7EEqEGRqMW8f9lxuNYZHGg1C94tvKVYKRxxK2LQCqxjuaLQ6n2WiIS4yDZ4DRTndMYJWsuI3KuiYm08dMMErhmBZVkauEwqWbA9uSb4T7OGO9FXMq6xrk6tanxst_YYD8yab9Y8VDdQ3LTSN92f3Y6QcX5ZDqX_nKIt1hyqFGbpdozDmDjeqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbeqHRoYFDIkOOY0akZ1BOqNs3G-GChr9bx1bbevs725x3ZIEUc1LIqzoa5HTih4UuHWgWNd_er-MAsGqfbsSnUr31N3PvKL4bHY3jOyV8pGo7ph5P5A5fy4W_MWfsPARa1Wcevivu1DHSgn_5hiLVXTn9hv9ZrTGNAwnu07tnIdo9KremnOGfQAPviVtDM2y0SLhdsYIyNVejjlvFXcSfOD_WNejeVVoT6xAIfDVH8Uq0vJQ2tI0gHa9t9p68uUVVBNdPpJE0nFEIbsPBj1NjU37XY7neHolLEoerR5oMfowm8jLGuigVnUtUSY2jzkJ5WQHFGXrgvqbKMdU8OIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO3x_yOkZ1Nh1aSNC9PNZdGBreW8lSjBsW6FlZA9E6CW8eUqwtuLBYUXHo4YKTarMvWlzvHw6aIT1Y3oVQyAAIHcX8oYfyexB72eh-vDRT41W1uSiXoW6X5KFgtrPecRG0r5rMb2WfhMofPUVENB0KqYtl9_EW1NdH3N4qmFgNHsGRiKD3zBvs78F86zhvJUd5E_CUU56UmQl0cATD-R-MEwiyKJX0m1IWhdgyZIVK4Ny4jr9A3uYvV35anvr6PtA62olYimTxmEd8XMN0IsGGyba_q8aZrswn0I8seYOl7vXsFHhvWEbfIlk4fK3ElPox8ExWOijxs1qwjqa1SMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=foNhdtwJQKho_gCIKy1OBgW0XkpieEAw9tk09DAPSxd8-Cja6JSZ0A4oF9JISCy6tuzEAvS7QZtDfb18_KtJbqwHTUNfnXQRqz0PkDhs5AolRz-9-tqOnEfl5EKH7uINRpFSNkRR7CBFiUgf13qZ1ZPdUxcKn5mESOPMwDh1rs5FUPRLw_LRHiePCvCRcHos2Z1YVAgkPdFqup1aPspdz08PTd2U5NCYlBQSjbCk2YGXTXmx_L-_bbJuClNqPcTvn2QVXbQc3fTHYBfwKE2b9Oom49lEQ-Gy2JlJNQSh8YNmHce0YI34t2burs453EiVqokBPFRIQbGFgwUp2g_K0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=foNhdtwJQKho_gCIKy1OBgW0XkpieEAw9tk09DAPSxd8-Cja6JSZ0A4oF9JISCy6tuzEAvS7QZtDfb18_KtJbqwHTUNfnXQRqz0PkDhs5AolRz-9-tqOnEfl5EKH7uINRpFSNkRR7CBFiUgf13qZ1ZPdUxcKn5mESOPMwDh1rs5FUPRLw_LRHiePCvCRcHos2Z1YVAgkPdFqup1aPspdz08PTd2U5NCYlBQSjbCk2YGXTXmx_L-_bbJuClNqPcTvn2QVXbQc3fTHYBfwKE2b9Oom49lEQ-Gy2JlJNQSh8YNmHce0YI34t2burs453EiVqokBPFRIQbGFgwUp2g_K0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=RTbYuxlLCDmMEleV--o4CYoWhHtAJTMpxA8zR2b5U0Q8CZxmA9vLL2mhJQFE-SrJrMQ8aed_DmZpDxFeiVzV4FrtqAoKyv74n2NwJtx4Owg2yxHMXTwj_JmxqngP0X5l9eeVlGQl2ipywCAOWRS6rGOjmOWcL7Xpi0OoJRNqDNQaGe9c8J01QB-QGl42Mj8XKiUkJlU1D0Sk7zDaBZJfRdfCL1PjX-aq6IWLOMb5OEGvR8iIBU9DAZNVsL5KL_Hk9UQm8qeedY6OuqSci7M2WbQQj_MD3D-70bKY_CO7UKVxSVArmqRPGLv_KJa2Nc9xNXtszCkvnJMWubkluf4xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=RTbYuxlLCDmMEleV--o4CYoWhHtAJTMpxA8zR2b5U0Q8CZxmA9vLL2mhJQFE-SrJrMQ8aed_DmZpDxFeiVzV4FrtqAoKyv74n2NwJtx4Owg2yxHMXTwj_JmxqngP0X5l9eeVlGQl2ipywCAOWRS6rGOjmOWcL7Xpi0OoJRNqDNQaGe9c8J01QB-QGl42Mj8XKiUkJlU1D0Sk7zDaBZJfRdfCL1PjX-aq6IWLOMb5OEGvR8iIBU9DAZNVsL5KL_Hk9UQm8qeedY6OuqSci7M2WbQQj_MD3D-70bKY_CO7UKVxSVArmqRPGLv_KJa2Nc9xNXtszCkvnJMWubkluf4xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm0Jj9lN-z4W_ajLriiR0duhnv-GVsedoKabU3HUh_xVWPaaEiNHZP2pnE0E7Z5Wn1v3DBraNagsuc98T9koSw-IXT5uFD_DRDxkQUhUy_vj9eHNFLrxLfB6jd3yqeGTY8-fqSMdd17ra4PdyySddpgaC_FXXm2Yg71_58kdB6fhJJ4qEFwr0WYHs_NglLvAqRb1KM8jPhVlA4kE6kLQxlUKT328V5FsUBEoOZzLTNY_Wf0IjhoJ-pgVZkY2inqQu3K_0Q8wWFxOPx_RmaZWXEGW6s3BRk2mAtDZXJjbWd8yzrYyfmNd_Q22YXXnOUcQn0mv-j11SpdFBMAmhlkGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g75wtzPZw2SblXu6oXv5BZ6InUgOfJGiJNDS6VdHetuZLJ77wDSsl7o_Q20Kk2v4W4U6ri0uz2DrjIBinIkSc3s3Ik-Vd9TqKtwMcYNL3Epxj6dhCKz2Ugmjot4AA_9G9360td4-p1TFkLN27Bj0JLgmTxb-gzuahMSos42sSYWuL7NeFwp7CxexRid0KLmW0QrSxXka4tfSMmxkregjXJssT1N2CwPw-gWjm6dlUHqfG8DA4vrtEpOETP5upkUbokYxGH4f88BjeK2Mb8ekMwYkaz_mhl68CfeJChCOtIeytOtriJAaR-ZuY76eRTu2aNIzk3FoOnkWr7X1Vxg3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-NTtkv-Up4LkjTEf8KPckOUWDbxnriyLA65RRPt518bla9DVh14li0S9MDzsQER3PcDHiPudoI6M4KoZM2dVGSesa3Z8ETS24l_waza2LiJR2m9jBeENORsPlnQAbCSk2jvygpAbbH8cG0R5m9NYdJ8m4G2jOr6I3Jna1M-s2eGNhXr4Ewz2sl8k3-CWn3gR792ZZk6IjakKo4j_uNu3t4Si0IPQyIDxw1_IsnCoCGrNgbO3Z1BqftXM48FenACPR7_p5QcwBnNno2FCtHncE98frk6EkT2mdOKgV4u-V0Xf_YC7V20_Cr4s7f0GzrpSYQWkn_obU2JpqxbS8PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LHRd6ziU10MYZnjCkxjDvNuFiNRsOj-aOyCzAUrNjbvjUMQhaZZ84WLOxJHPEo7Uzx57X4NuPAyMhpycLadJLe16etp81qA49RuoCtMFXsZ2EQ0sjb_hAOyC3aOPpJprHuUPYIyw0XA8bnc-ZmEz4UdExTHcejfp_5wl-oU9F8yHBTS7Cv9_a78m8Xdn0tgzEOqI8iXLm2QUkJQFX-iPPakMEa3osK6eLUGzyo_sio5s7VuRzfPu9vQLHY-VMmclYr9Bgd-nH-OgVOTLkwZ_0conZDDkAC2ukaakWa7labGcCnqIiMiCwbSF1h4eTsQA9E_f8jTV-XFTZMsPicRGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhM_LCqynRbZ266g7KnyCRJf15p8chELdYMfkhw7O-NrCFhIvTZnrZXaOmB8yCxUT-651pPxhDlBomOxB6vDR3MZZ3g-NciJK1f5yd40ZEuzige_0lmBbWmC7d1jFGbEG8x6_Xq5zT7yPmdhHXJ4mcS9H0x7cjnACicR-64aIgyxfg6LQ9g3QQtKszryCl5vO2-p5rh_Xf2EDXVJRd8ljP4P822trlz6lzQM6a-GPlf-3rU4DWTWgBIsnCeyXbYlWnoNNGTnOtN7WyV8vqMiZZA5fC6gOH4ZAxn4xm8FLGanscRTWdEVpvkdol6OxdmcQeFlL0QJhxBjYmbD8yXJvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuT63B1GKxsVNAKqRniCAOCIUaGABCPKioWq0veF0wpQxRwTHMm6yPBV0vdUTlHocifarYQ8ElQsUtVhu63bzxKlG-Z_7mfp5OgN5AaJ54_h4u7Cupl9rgFSjPAZxU6QtIbvb2mfwj_K6_9x7ZHcilwXNxuYBtTpvJk7gFPr5ACnYCP2drwcV-bDDfAIPEH7pdzpi5a_2GHx0NRlHcYJtVTJJ6gm7QejECQ6My_r1932nS6XVRD1g47NZH-n-SodnHdVZVy92kFiUtnGbm-BHW8VsX5aGGx3GdLnkB5aIoNtq4e4NRlpwcY32lGxZ3XcbMW7bLH0j9J8wN2RinIZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt8n_TpB0cFjFBi2s1PaMRRl7PeUTtpqBFH-tTkq0ukwrlfIKpSJxcmGN8y-huDKaIl8z1c6C81fUyKW8TVDbL0wRwS2GvXHXXPojazRy2RjXhMUYgpwUuZqg0OlzsAHF4YLDAR-I5IbhwIP8rZfNty-kmGKl9aYX_vlFNLMEilg7YouudwY9vBCPnHHdGClvdeWc61AjJwwY5IO-y2QAsL0mDL5-1NDDcijEN4vxhcQgmeEGeWt89siWnFBvwgMRCHWPUfWRmUEdat0O24bLGL2pfRSIYHWhWlw3PwNKr7T6BvBRu3F3BcwDVOBYnZ3wVV85UeV0FIWuubvnIQmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=dZemuUSUHeLd_TDxsVHw5FtiPkwMKgsQ7d8KndpgmHDoNEc1hppSUdOAawigR_tig5Od9nMS7W7O8XyWIvtIJUf1vUN3kXLqiHaE4l4j8rAmrnu9BPqxp1gg-7ASdq1E_ksUmXkBgTVjsA8M20B0ujtEFEWjCt2HAa9mKbngR2V7cIvnFFXqE6dR45bAFUxGb2GhBM7l25wkuaOULDlC_HH-xV9rEKu4Ma4Bq8Z6q_e0mOydHjPWvPg8eowBNE3hAxa_8y1MI4rJWLW7FxaxEV_HbEa4DmrKDjZI7ZpcIbrEu3LG7BglcEQeWGItHT2jzdNUPbx9dg62IO5lhpldHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=dZemuUSUHeLd_TDxsVHw5FtiPkwMKgsQ7d8KndpgmHDoNEc1hppSUdOAawigR_tig5Od9nMS7W7O8XyWIvtIJUf1vUN3kXLqiHaE4l4j8rAmrnu9BPqxp1gg-7ASdq1E_ksUmXkBgTVjsA8M20B0ujtEFEWjCt2HAa9mKbngR2V7cIvnFFXqE6dR45bAFUxGb2GhBM7l25wkuaOULDlC_HH-xV9rEKu4Ma4Bq8Z6q_e0mOydHjPWvPg8eowBNE3hAxa_8y1MI4rJWLW7FxaxEV_HbEa4DmrKDjZI7ZpcIbrEu3LG7BglcEQeWGItHT2jzdNUPbx9dg62IO5lhpldHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPuSlFEvPKAf6UnEcTXiXBk40-lzEv7iUcNQ9n_wIS3PVbYnP34p3LhHjckNuIMmH-Bkzf8CLAGBWNzGVrrlGzIwB5lM74yIpEHTevr8H5cAHjEXLd9YmhrafRXOOGLsm6mnKNIC_BAQFX54CPRFdf4kb9e1Ywod11DtAVB1Za1Jw9Za3fuWWHX-0vyGndLNLkTB8KULUs_OQ7tmvyeYut0uf0D5tqbbeCYYsh4-cNDnntdqkshsxvDiPzE6DlkjFSE1wbqr_kaaraUwpAiaTgVMr7Vac6ELMQIV080o4-NAfq7-oIpStC4iDZXLr32YvPVmrNvoIot2jIffwg0-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJA-5wUYFhQ0ErrHe1NevRq7vQZdJweh7cLtIpI4AyKoEXPohUvWR5Qhs2jCfo4lwQB4BUr64E1c1sCrnFiOWDcN0h6v1YA0oCLrdYKmqwkdf0Qt2_IA_UrHBgxmQ0nt5bWsj0BVAm8PTEe8NwKM3m10i7jdf0qDmG7ss5DoJuZAyxHDXEQuRKVnQ5lYwfhoopiUQpG1NeXmctggJqfkgtL3_GyzpGfjj1WQuJ_42LKnRT8Tb6D5F-sv3g8TfIkxPyEMuO8xTBnmeKqZeapZYmGnxLl_F1gI6voNaeJMW92CSb-yKWS7nhVKTqEy9l3fVJqmZ75U2GlHZ2xkxR1ERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5v7W5kj0oqKG-bbrFxcJV7DJvEZj-gIIAHfGSHvC-GfGt8c8pC4-DyUA2hF9hduInLEWCTTPkthdQrVVAfhYh8h8E5doXs8pVo0_IwqvHbmdSxjr6VoaJ1NnBxkQqzPST-3obnV7VmWD58EOoRUwvG3taqjKCS9Dkh_2rPNpKmYQPAeliJQAsogFhtmNdfL6JYw3o09DqGKhZikj_9PxXcFh9BHEU8L1a_r536lQYefYABXfiv8rRXwFdiwMgc97TnDRO8p2iGXL6S1Poxp1Yn-VGQssYE71ojmLHmOQ28-bLYYAm14JFYT02ML8jSbfUC8lcM8-taGDzpCM3YQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxc9Qym8xalQhVnW67xkm66pQ_zSItx_HIeCdoDE3kKoEsP3jxCDCCiMXqsw9GYh1cFri3q1jp3yzVdCZ-yX6xRxB4jcdutc2j89tNYSSwTZOwHeLvrT8cEZKsUoZAfmZQR1MV1NcJ2237HNkGOXQpazwO3HN09JxPP6L_uqWme2zfu8tVW2Qrenw1zzmTgkhdDKmhRlTmcccqbNaoqObcV-SplkpXravQlcsp2FMJuEFuwKjdIwb_Gaeim3jV6ixxLYQorhAM0rd93npLQmUZK3eSStKH8FzEBDpuDQHJJ7oc2jlDHzXO4nyZkASA0kGfjMmDt7MTOggXS12U40QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=nvRPXd6JsJ5DkgCndPFIPMhI-6wAvOVF2bYLhWm8fTQ3wV04NyQseqhwTaTrG0-jFGWaxa6EzFKzmUDtlYafQ-wpM6OgOYDLy8uAdIBttjXYNL7T1XW3Jsv2rosdgUZOYzjRUbLqsf_uchTIlDxs-cgRYXJ5u-7T58tFFDoFIm1V5iRkgC4y_7sz6Su9PBGh8UIekb1vNg2DzedFx6vhRstdXGPi_-dR3NRLqlMYrh04_0I2klgk5he25_X19DQS5LB9qujIK0rQ89nYnLy2cAf7QdaxR_ArU_GdUASbFd5_ifBxRp9p9lFGCOolVqpH0ctC2zyznwHjj4w807np5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=nvRPXd6JsJ5DkgCndPFIPMhI-6wAvOVF2bYLhWm8fTQ3wV04NyQseqhwTaTrG0-jFGWaxa6EzFKzmUDtlYafQ-wpM6OgOYDLy8uAdIBttjXYNL7T1XW3Jsv2rosdgUZOYzjRUbLqsf_uchTIlDxs-cgRYXJ5u-7T58tFFDoFIm1V5iRkgC4y_7sz6Su9PBGh8UIekb1vNg2DzedFx6vhRstdXGPi_-dR3NRLqlMYrh04_0I2klgk5he25_X19DQS5LB9qujIK0rQ89nYnLy2cAf7QdaxR_ArU_GdUASbFd5_ifBxRp9p9lFGCOolVqpH0ctC2zyznwHjj4w807np5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ppppKPTccOL62CZawbdi_fa7NLwRoTnpH1MwCMZ-4bKnef6O9N83B4hnwATg5KbyBYun6LrOpn5P77Hwps9GytlgX1LLZCNFjexA4v8Bd_dcY3YbDoEkdb9YTPr_9_9ZnJyXMXrIfGGVgcrnHj4E89iWpoq8xw8dc_xpEwbKzspWVeDDK2bM-tgvAQwQGyX1cEtUaPSP7tGz1hTHqdmlTU7ghbhJXaI7xQdsOVMlHSUiNp9XaTdWmptrY_rGgYSwoYMdi-2d_cAtnBCO6n64j_-gyuKECA4AhcCv5hWmXgb2MQcDGTi4ctS6j79AOnsb0R8HgRAl5jp-rh2NAsbSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ppppKPTccOL62CZawbdi_fa7NLwRoTnpH1MwCMZ-4bKnef6O9N83B4hnwATg5KbyBYun6LrOpn5P77Hwps9GytlgX1LLZCNFjexA4v8Bd_dcY3YbDoEkdb9YTPr_9_9ZnJyXMXrIfGGVgcrnHj4E89iWpoq8xw8dc_xpEwbKzspWVeDDK2bM-tgvAQwQGyX1cEtUaPSP7tGz1hTHqdmlTU7ghbhJXaI7xQdsOVMlHSUiNp9XaTdWmptrY_rGgYSwoYMdi-2d_cAtnBCO6n64j_-gyuKECA4AhcCv5hWmXgb2MQcDGTi4ctS6j79AOnsb0R8HgRAl5jp-rh2NAsbSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9esvzNIcONC4nDcq0aFOW64uckWHK0D0RGGrp6XFurg7jSMAxzKQaU9h8tYv_o-uvDrez9OHZRi3gvVDzljrhXH0OGfeZ5qdt7D0WT6cVoaiPH4aphSUDI_dBFrLjfJBUdP481ABIw3qN8IrogosYTAimRWGDU6bSQrCw9rtbr7zBNx50IFYgvbBOth6y8oUhpk2Yn75UP5qOgVVxub_ThhRGEhOD5SIV4jMfGLtukxI-IWPSovwwkGbO_YMXj-JaKS1aKMc10lIm6lT6rZl2eV_vY0qKza4YSNqkeQiapqTgM2P1y2Yn06Np6Gb8NsFZMgA3mN4FWKgZ_Q6oPKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=cQP33a7K7uZust4n-j0WXRAs3XN_PBAkCgCkYwrzwEyy6fReKCi5uk52h4SNh0lC7NLPMAPpey34WYKluVK1NpVHy8zU80NaKjhVa-2nvQ2l4NpSQmQEAisUgZGlqjk_zC7TWFA5rxW2D9TjnJdhK05j0RDdfBHxjXt0ZwpR7QuaI1TUBiPaRTTuI4GnQwTuADlAL-UIdX-bJJaP2pheQI5IwrIHklQd_5yx4uy-LU-AK2azpvJLtddqfZddObl2ZDAv8sFYCwIfgJLTbeS-lFmS-3LEfdGkKQFlufK77ulA6QmHV6O-YkNzfurNGzE3sN6a8CBIui9RGi1LYjIXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=cQP33a7K7uZust4n-j0WXRAs3XN_PBAkCgCkYwrzwEyy6fReKCi5uk52h4SNh0lC7NLPMAPpey34WYKluVK1NpVHy8zU80NaKjhVa-2nvQ2l4NpSQmQEAisUgZGlqjk_zC7TWFA5rxW2D9TjnJdhK05j0RDdfBHxjXt0ZwpR7QuaI1TUBiPaRTTuI4GnQwTuADlAL-UIdX-bJJaP2pheQI5IwrIHklQd_5yx4uy-LU-AK2azpvJLtddqfZddObl2ZDAv8sFYCwIfgJLTbeS-lFmS-3LEfdGkKQFlufK77ulA6QmHV6O-YkNzfurNGzE3sN6a8CBIui9RGi1LYjIXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=DPLGD5_1NK_Fcl2jMO_c5K12U0q-qwdW1XrCIwq8Tm-1BgfyH1gLQVM-5R-TAt3aOWTbC29fPn7LWgvrQ49o7KbRt_4-BPm6XOtfitMAOF9u9YhBIP6Xwr-SjTltgkqH74IQkZH_s9RlClwqtIlWObNnFlU8L-1XpdbnryhZyhOROUkvzwaFu0gegzXGOOi6MfdkjA4fgsH00n6fHpnaxdR_qHjYXqa5zQ-ku-Dj9pf8Wx-Quhpej28BmC_F-URGdeoQZt2yp4dMqTAf8JmerAaJEl8cB2mgMVfgTHpwj1_KImRJKTDq4hEArp3CUSJtGIkWazWIkuR5FTJ42MMlwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=DPLGD5_1NK_Fcl2jMO_c5K12U0q-qwdW1XrCIwq8Tm-1BgfyH1gLQVM-5R-TAt3aOWTbC29fPn7LWgvrQ49o7KbRt_4-BPm6XOtfitMAOF9u9YhBIP6Xwr-SjTltgkqH74IQkZH_s9RlClwqtIlWObNnFlU8L-1XpdbnryhZyhOROUkvzwaFu0gegzXGOOi6MfdkjA4fgsH00n6fHpnaxdR_qHjYXqa5zQ-ku-Dj9pf8Wx-Quhpej28BmC_F-URGdeoQZt2yp4dMqTAf8JmerAaJEl8cB2mgMVfgTHpwj1_KImRJKTDq4hEArp3CUSJtGIkWazWIkuR5FTJ42MMlwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=TtxsRSi2Rjm7qCHqPuJ1ExnNE1U2gszH8zRaVMZwlfGjAOKGXEWervW_PS68z4PwT_WgwdErTJhHg2HYsaOzCVjJkHccxz4CoQFdMMSE1fWObPs3ussWlAsj6UzcIpoK0YAtm_30RnvdTIP5HKqDQnyFsqgZ-i-k-FTssW4ikhR8O39zajX2K-BFQpvYrUOWyKJ4Vn6iU0t60Qyc5cOqtVwe5IZBJoNKooaBpC8Ou3C1TJEN8sUaks5lfMyRBqEWiBTe33cAC7GNRvmy6IkiPe-r0Sy4x1ACfSn4dVUtTGrOpLrmwpSByGQTXxPxeQFLBrAYCfw9hZLdj_nQBFeApA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=TtxsRSi2Rjm7qCHqPuJ1ExnNE1U2gszH8zRaVMZwlfGjAOKGXEWervW_PS68z4PwT_WgwdErTJhHg2HYsaOzCVjJkHccxz4CoQFdMMSE1fWObPs3ussWlAsj6UzcIpoK0YAtm_30RnvdTIP5HKqDQnyFsqgZ-i-k-FTssW4ikhR8O39zajX2K-BFQpvYrUOWyKJ4Vn6iU0t60Qyc5cOqtVwe5IZBJoNKooaBpC8Ou3C1TJEN8sUaks5lfMyRBqEWiBTe33cAC7GNRvmy6IkiPe-r0Sy4x1ACfSn4dVUtTGrOpLrmwpSByGQTXxPxeQFLBrAYCfw9hZLdj_nQBFeApA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=J4vDQxQCRUoySJ2XYfgefT9haPtUhugRf38u_12uwUQIUSe7um_QBjkNFB2SmUBTOxj9HH4g50_F9ksjMX962o-1Jq7-zoVFdGAHqGqMGJbR0vbvwVldiv6Fa8xQ3hULYQKanrj3ER-Cfzu4a1fNJreeJspir8cZmC4VYkjBLgXfCBMlG-JAhzoXxCHSuWcEpyYHf6NqOYA46tHyhxfizNXk2wADWfbeP6t_EPyW_Bt37M0xz4o6GglU8uxuKKYZ3_V9YK6vhRrOyj0cixaE8U0dhXDRBmSql19cShXrXyCkynbSFnZMRnMTghBC3lX6p48F7eARDO2utGTSQ2W-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=J4vDQxQCRUoySJ2XYfgefT9haPtUhugRf38u_12uwUQIUSe7um_QBjkNFB2SmUBTOxj9HH4g50_F9ksjMX962o-1Jq7-zoVFdGAHqGqMGJbR0vbvwVldiv6Fa8xQ3hULYQKanrj3ER-Cfzu4a1fNJreeJspir8cZmC4VYkjBLgXfCBMlG-JAhzoXxCHSuWcEpyYHf6NqOYA46tHyhxfizNXk2wADWfbeP6t_EPyW_Bt37M0xz4o6GglU8uxuKKYZ3_V9YK6vhRrOyj0cixaE8U0dhXDRBmSql19cShXrXyCkynbSFnZMRnMTghBC3lX6p48F7eARDO2utGTSQ2W-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7HHcikYtE0gQgZ3qqZUk1bu09lWkLauDgHD3lidxAyrEJAumYrGQKjAmODZo0mKVGDhj7q4pcSCDkZyBrrp5DTRGzyU0HZgcs-tF7bFYWAYBDijJf9VqzOnJJXZ7hS922nS5cZtq13NO1wp_nYagMQ46RJyTaqeh3JIpnMNorktnW1ySs7pwLEq8GgwXgzN7w8VdVb_lTJdGLEoR7xBg9QFppoeCi4JSq12W33QemV7U-uG16aRmRKX8oU-PuWl3-2io6A-64xvRSJRzHlz4SZNBSmRJqzEuREEYggShXAS4YW4n21af0PDECs1W98oHGDgPvYGR4uYRB8943fTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=PEeyVRENBGyEgQ7Hv64ehDqJSJijuuqah95rHznHpf4sfCQl2VEASn7xA2QOqa6vDDYK-9yh6wHTehEoQJnF9ni8SH3fPhmSIY-c0hfk9hTGu6FqrNpmdF_zA_syhYx8Z6DUrOrBlZQvi1ysVTdJ9zuKupVsV4xl-C1ZmVWhs7F46MzU4weBsOjZ5r8pf37m2xbaFojN_-eyPFT916Au5heBZTYvOSO62GRGL-JQ9szRkjrI9W93913bSeOD7pthSNCJLna8pk0hVd7Pf82rk5si90dU9p9m-lm7r6ps2bpA_vt7GAQ58ZEOJtQVdAHJMhtTqvji8TcHiikXQG5OPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=PEeyVRENBGyEgQ7Hv64ehDqJSJijuuqah95rHznHpf4sfCQl2VEASn7xA2QOqa6vDDYK-9yh6wHTehEoQJnF9ni8SH3fPhmSIY-c0hfk9hTGu6FqrNpmdF_zA_syhYx8Z6DUrOrBlZQvi1ysVTdJ9zuKupVsV4xl-C1ZmVWhs7F46MzU4weBsOjZ5r8pf37m2xbaFojN_-eyPFT916Au5heBZTYvOSO62GRGL-JQ9szRkjrI9W93913bSeOD7pthSNCJLna8pk0hVd7Pf82rk5si90dU9p9m-lm7r6ps2bpA_vt7GAQ58ZEOJtQVdAHJMhtTqvji8TcHiikXQG5OPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMRZF1o8wlOZqo8FuMWSZVkfCHN8YdBkn6T31NOECDHpV4M4qclzjR5P0e6UVa9rvgsF9tiBDKdAamMRwLbgxUC3__NKKQ4phUt1s-pSsTaf7BllWOIyMxgYMFbil_5Q5PFbXHFkDziKh1kWDjP9NeRlYqimuX3XfGq3aiX-xGPB63fDjFgI-pZTc1mSBaKFISN1wG_8B0ti1bjf6UVcEYVsnteP-GL6SacHSeiHRD9DyVdB4OZCe0Q1QqpC_J8E6s3gtcwkYXA45Uzr2sOUbAfRRWXCE9vgf8m7IqrH8hfDFEMMJ0KrYYksORfzcu0CE1AemLaq5uv14tL78EWCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=tnvMAMK_y-tubAsPV_t_NapWOwpgmOrZ8rtWYCUBnbPMtME7F0O44AcAjvgKDm62q6HVCcNDh7ZYzC0fpIB5mUQMIfrS79c7f1RfgQRVtoSCV-6ht5Ps0kKK2R8np1lfJjWi6iwKA2BmQ5ip1ekRq6iHMcnJbmphxq-FsC4Qw2XaEKcgsOdiZ2O59-cYykMvUYpquYMSWN445fXrb8Ac_GMPbiIK2IMbTmyhywjfllrUYTeTXN54GU8QVJiiIO4rEKbHx59iSVwvsuvCQwbmpvlu5uLC3BrFTk5HyZQNPSALlQ3fAFoJ-XLgn8m7b-4t13h4GFAn6-Zv5hr-L2ajDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=tnvMAMK_y-tubAsPV_t_NapWOwpgmOrZ8rtWYCUBnbPMtME7F0O44AcAjvgKDm62q6HVCcNDh7ZYzC0fpIB5mUQMIfrS79c7f1RfgQRVtoSCV-6ht5Ps0kKK2R8np1lfJjWi6iwKA2BmQ5ip1ekRq6iHMcnJbmphxq-FsC4Qw2XaEKcgsOdiZ2O59-cYykMvUYpquYMSWN445fXrb8Ac_GMPbiIK2IMbTmyhywjfllrUYTeTXN54GU8QVJiiIO4rEKbHx59iSVwvsuvCQwbmpvlu5uLC3BrFTk5HyZQNPSALlQ3fAFoJ-XLgn8m7b-4t13h4GFAn6-Zv5hr-L2ajDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=OVB4gu-GZDqUojpd1NN5bp4mOSRaw7E5Xg-QijbsOO3SuAquBUa2s3mibUZuZJDWKeHWNRUBjzYMMrOCAoSMHcsAZURwjBpHPjk28aTu8YFfMIrfv5HK89neuza5x67ZOlV0R0pgNe_1cyjjmWGEDT8kgbbWW5loNgRW3emTUd5aVCuDMdCG5Rwmqgr_jEF9y_69gqKAz0fTe_Ml6vgukR1_YcjRNFIZC7kkarSy3esaN4ldIcNOt_OqsIgey7yiJ7WHXLquRHVACR54LsgGM3etraOL_U8Vgtj-q6dqDpQJronLrmFtkmu3YdhlDs_Cp6BHXnq-hR0VlO-zk_VkwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=OVB4gu-GZDqUojpd1NN5bp4mOSRaw7E5Xg-QijbsOO3SuAquBUa2s3mibUZuZJDWKeHWNRUBjzYMMrOCAoSMHcsAZURwjBpHPjk28aTu8YFfMIrfv5HK89neuza5x67ZOlV0R0pgNe_1cyjjmWGEDT8kgbbWW5loNgRW3emTUd5aVCuDMdCG5Rwmqgr_jEF9y_69gqKAz0fTe_Ml6vgukR1_YcjRNFIZC7kkarSy3esaN4ldIcNOt_OqsIgey7yiJ7WHXLquRHVACR54LsgGM3etraOL_U8Vgtj-q6dqDpQJronLrmFtkmu3YdhlDs_Cp6BHXnq-hR0VlO-zk_VkwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=iopf5IaAF7cCCsMuiBajiZk9UaptERfe9RRp1WD66Zzv5Nuylk3fwmiodf7ChKOWNFzyez2oFBqy3H3m5e_LEhnX1pS-tfzTUH5ktaEABtcGbXyHJrenBxQcrwBbWT6BTg7dQA7qN1Gxljb_ECobx0z5vuc1Z01VYkswfq22dywTfQdU6tsYxYFRc0f-jJSSIIuo2qq6lImNodMK6aWoblapSuQrqIF-SfcCRcybqZ1f-HoGp_0Nad4uydrkl4NKDsimUu6nWi2bQz78hdE42sLWI5bm3Bbg7dJiUQdgNac5y4Bnhbj8P9r-auZlFNtdif_k53iI6maZx5nmZt5QhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=iopf5IaAF7cCCsMuiBajiZk9UaptERfe9RRp1WD66Zzv5Nuylk3fwmiodf7ChKOWNFzyez2oFBqy3H3m5e_LEhnX1pS-tfzTUH5ktaEABtcGbXyHJrenBxQcrwBbWT6BTg7dQA7qN1Gxljb_ECobx0z5vuc1Z01VYkswfq22dywTfQdU6tsYxYFRc0f-jJSSIIuo2qq6lImNodMK6aWoblapSuQrqIF-SfcCRcybqZ1f-HoGp_0Nad4uydrkl4NKDsimUu6nWi2bQz78hdE42sLWI5bm3Bbg7dJiUQdgNac5y4Bnhbj8P9r-auZlFNtdif_k53iI6maZx5nmZt5QhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=RammiFZMJSg0HTY67EXdF8-JePOSmktbPaZ2hgiuLQxC6NAMKk8_SWHEXY-Wgt4M1RPf9Gqda8nDe0jKk1BW9AgORe9UifRT2rETbQZhFyFP0_qTbScmjfUu4CpnvN4dKKLvW3NrjWtU323bYs2w5bJybWtMTUTvFZy3zHSdrmrKw6QxSCDvk363q2ymfBuHu2kLte4RVlVVVGiSTBzS6dLiM9esg-S41F9b5l9YQmDUHkBs1-bgXzRkz6gnCR_2ba6eUV7-v4yfVWDnzOi_OnAJSuwZcB-QlHOetKYVYe_YeWq6ePYMQlhgMf4w1fW3WelYD61z-KGA5u9NCW74s4plZ9rtQF61HEwizr-yXfitRw8XOTB3u7Z89Fjsj75sU5r1IdUQDdOVJeyN9BN0iTAVNDqqg5MlD8-MpGXuf-pJW4X2Gr8oOIQ7dtIGOr-FPbnpYtnwCOP4ED6VLBMrMIbb2ayHbzm9R0BMCHkNiJ8D_nOZ0eAhczqHVS1LHL0tv7FuqwLFXgRm79SGAQYPwiW1pW68TunlrGidAdgggUnH468VDWXVJuNrULR4az3tUnCMMMTNkWY0L7hDCILammiYxDdDCpFaPkNxES8ekJzLyrF5NUN4zPyrBv0FbpWS40x0CRP95VW8A24JimWqIzCpp2c938rAnqrTzgareQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=RammiFZMJSg0HTY67EXdF8-JePOSmktbPaZ2hgiuLQxC6NAMKk8_SWHEXY-Wgt4M1RPf9Gqda8nDe0jKk1BW9AgORe9UifRT2rETbQZhFyFP0_qTbScmjfUu4CpnvN4dKKLvW3NrjWtU323bYs2w5bJybWtMTUTvFZy3zHSdrmrKw6QxSCDvk363q2ymfBuHu2kLte4RVlVVVGiSTBzS6dLiM9esg-S41F9b5l9YQmDUHkBs1-bgXzRkz6gnCR_2ba6eUV7-v4yfVWDnzOi_OnAJSuwZcB-QlHOetKYVYe_YeWq6ePYMQlhgMf4w1fW3WelYD61z-KGA5u9NCW74s4plZ9rtQF61HEwizr-yXfitRw8XOTB3u7Z89Fjsj75sU5r1IdUQDdOVJeyN9BN0iTAVNDqqg5MlD8-MpGXuf-pJW4X2Gr8oOIQ7dtIGOr-FPbnpYtnwCOP4ED6VLBMrMIbb2ayHbzm9R0BMCHkNiJ8D_nOZ0eAhczqHVS1LHL0tv7FuqwLFXgRm79SGAQYPwiW1pW68TunlrGidAdgggUnH468VDWXVJuNrULR4az3tUnCMMMTNkWY0L7hDCILammiYxDdDCpFaPkNxES8ekJzLyrF5NUN4zPyrBv0FbpWS40x0CRP95VW8A24JimWqIzCpp2c938rAnqrTzgareQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCSeCaol8IifRqxlKkKVd7nagft-laMNEYIVLfKgI5taLNXR7r43Hsu_ewx7545RGDL_eg-WFZDDkjXbX04YBK6T-B815_RAH17hHwm2FHij6QJxBoNwPSEw3S166SzaXSMsxx4wVMIRj52RyoQvu-LHESkhxA2EtTaGzO3dClrROKL3JNPbo9yY5p-EoXDZH4vJC4GZV_sIf-LK2YILjALqpGWHws2Bed0x3SDLVlIUSc5yt3w6n6ghq60sZC1EH1acL5IMmmiVJOJTRo9ZOq0nJyp7db_EpKg-nsdKCxBOGIcge5-prpo3_RsqDVhaZ08gZXxpVRdBxlxeVq30zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Q7sVLFwle0qlD9b-SBdKX-jLMnWzD1_orm99CMaGKtSMXQdgmnrFSoMnSrBBaYKdWYyVAQUjBgmvj6EPEcBDxhDx2D8Zk0f4_15VEk3INsMXExc-TJagl9Ew5p2ycAHek41qISHa-pvWGmH8AP4O6MOPR5Ui-aSOTUjiIAyVtiOOBFjtFFl8Lewcek_rYqYadqYKAOM_YEhO7w4InG6uTiEp1RbQfBhQSgzeAZ54Y2xdUaG32EveVci-v9o3fOfbLTMiAIBGTGFmZ6pzQjhQ18yO6zk9e34YG7UFlRl4E-Gv9-QABOG5kgw6KIb2Ul-fcVRTV7vmY0gmf5A5lIC0xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Q7sVLFwle0qlD9b-SBdKX-jLMnWzD1_orm99CMaGKtSMXQdgmnrFSoMnSrBBaYKdWYyVAQUjBgmvj6EPEcBDxhDx2D8Zk0f4_15VEk3INsMXExc-TJagl9Ew5p2ycAHek41qISHa-pvWGmH8AP4O6MOPR5Ui-aSOTUjiIAyVtiOOBFjtFFl8Lewcek_rYqYadqYKAOM_YEhO7w4InG6uTiEp1RbQfBhQSgzeAZ54Y2xdUaG32EveVci-v9o3fOfbLTMiAIBGTGFmZ6pzQjhQ18yO6zk9e34YG7UFlRl4E-Gv9-QABOG5kgw6KIb2Ul-fcVRTV7vmY0gmf5A5lIC0xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcBFYkJqss2PRaorDZtAO228J2sKgpol6qPgUyMakkE-xkwNVn4H1LmAryjHZ1ceuCpcNCy4o1tL0VsxT-LSEbCNxIP5Oz94pcRTtUzg13NqOvaxWMVRKxsmDCXS1EAOt6xAEW0E-oBbVoClSIJegb8ERUfRHpXgk2B3lwlti96pgaPRjhUXzzDDqN_YKC21KDDtdUeE_qZ8SmoWOf5qWS0hs9D3hOWNeUwNE9dq-XvjYraQltRSm6kuwSo7fW4xy_hNE7iCUY63h_VrbSsvh0oIOFAK-yZr9VqqrX5cFhqsbk2deIReY-dnYoc6FkRUImqJPKxu0rgOu0CZYj1DlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGKAF7n96J_N1Kyg-OL9n-6L2mT9vS3ZbQTpi6p-8FD2HzyfSqU1oWYp8jXP9i2vXgb7D-a-QmH_3w5AmZZmzn7Qo-n_mEPOOQ_NxZVwSCgpkIfWBtg7ONTDJGAvnNlUPysOUas-w4z6vGdv2N5DtUcgRrkobMCk9H9wbtm2iWlSbI4gYEQEezQDjEMHeHxzYdgwXJqi_vhofDPf7xOa9dCcQb3JGgEVmugRhNBHYnJYDdc5FCyM6yysGzNfnLFleu_VJmfYbazHJlNPZHMdJqDxGWgglYpaRwzayliXVrzEhqA8Pb_DsE3O4yQr6yEy2RGnsMlyp9ehs8t0FXyl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXdEXh2eiPIRkPFoEBaTs3kc1BbdFKaynB9jQUJ2zw1bQePO3Y1o--U-Sd1mKjdJvWIORKttciMayR6VCHVQtXAZlEMotf8MhsjXUlTkSZO-L9J9kIKwBCwCPtPMiHoNXqmiC2KZ7v_4T9I1frDWww4ZbPpvWsljr0isVNTGkDaZIfnvvJ3hqNOL3LwN5IJTYCu8fSZiKdrs0mxZbxcxqPSb3luwyYhce0t5rYTGZ4RVHXk4YKvTivw6A-8h_s2LQtndoChcIH0YPeIOcnOQ7Dsk8kN665uvIY1vkDsO029LTqdCCar2ltd_Rgq04N4jxOJIOV5Cv-iyVVgPwftP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc_eR-9tqW5LKaWdfz2-KKDNkzLxDGK6Dk1ppX5_FSbr4aFHVQyB4F1hDX1__b13FBvrLdPbwgub_2Z4iiX7k0MvNiDOWtHm3oyC-xtOQarAO1xsvXX3IPiLXvVR3Le1anoXril1WI6XURGPQIb--_SG0IV2HQN207jVxAFClErfBaL7nhkieu9GstsrPJjwoeue1uUX15tXhFdHPoq2fa5VMwxcuHCYV0tyOgF4U2z87MoumaxZBaVRL1E6GZWh-I3bVqhhtKxqxppQ-KliBtBuBbnBEbHuzPzme8N54ftTRB2EkiwGTR0Fh2KT9L7EjOZuq32D1h0B6rQ8py3nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aT27M5Y2EK_8C4WYxQPy0Tr-nRHfz37oEFJhMfhj9VM4_Vqk3Ey8-pvJIc8w2_mlkYkdUHSVAbOVgs3f6gv9gYUr0Ue_K162tbPTdsV7391V62WIuiRcijZuy5UQmtABrFsD-E0LPpHbsYgVSL-QfAnI_7lqBO2ZbKNJxnP6ftGJjohuezPmqy-nX5QTOplC3JFW8cPA_vGFH2M8ofNxLLE8661Ge5V9XWez_VmcwLHmUVrPf1Jy7bmg0Te-_xz5bre9kJcaIbM4viXj2BCZklWisfJujLXoxoDz_rPVZFqta088VvlGPCVVDWj22s_854jfCdr1-szQBxtYm3nF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rqvcqq_7V8Vdrkm75iiL0k58SsZ1iV0DHA7BaENWX5sn4HKZu9BVWgih_jrTPu3rPwydRMlGxJ74gwrvXsb7y5Z9S-_w1Fy9-JhSbuXOAJ536bj6I6ak40Dq8a5qNT_c5nHRWlotbgX22n6Nr0niekDMOJY1N2PFZFnKcNrhZZn-hwUdCFuVnnJjEtFMDddI7Y3D7_tftJEtwZrQXXAe7EjmCsJaEiZMCAZyk5LC-WEV59L1z-3-ZTxvQsWa89zkcC2VKCSA-3O4Nh0982gjGLvkTzYc-oBw6AQhcjjBPNSJ1iiKKWHiHePA-WkZrDeVBlRLicE2vP4lboLq88IGQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=XHVkp_7K3u5kPAbg3bjchR-SjwAgTWsfvPWBrobX_Vefgkx2D1G6thB0hEjPdLLsuwamVPtNs34KKRMaGNTXDQwalvKb3sOB0J683w3AEqK-MK3eBJdai7B8qxzTPzGaVmiWWCmTDGBEWr9o3_kp8sLrtojJxjLWwBI_-ZeXbQ58dAiNTjpzdhGFCL629n3g8Sav92L6r8X7GPa_N0Zgmj7dZ5vpMee_u-Q9U5_WmLu4XHOZEihdCo7yVmjHpjLDcav9Hs3fgwt7u4J89ifpvfRhIJg-pxMfk2kCxTCW3qVx-N8uMP9v0EQKOf_auAdCcucCu_-Am1xMIdCV3RBbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=XHVkp_7K3u5kPAbg3bjchR-SjwAgTWsfvPWBrobX_Vefgkx2D1G6thB0hEjPdLLsuwamVPtNs34KKRMaGNTXDQwalvKb3sOB0J683w3AEqK-MK3eBJdai7B8qxzTPzGaVmiWWCmTDGBEWr9o3_kp8sLrtojJxjLWwBI_-ZeXbQ58dAiNTjpzdhGFCL629n3g8Sav92L6r8X7GPa_N0Zgmj7dZ5vpMee_u-Q9U5_WmLu4XHOZEihdCo7yVmjHpjLDcav9Hs3fgwt7u4J89ifpvfRhIJg-pxMfk2kCxTCW3qVx-N8uMP9v0EQKOf_auAdCcucCu_-Am1xMIdCV3RBbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=s63dQmmwTGlo6nV4cOHfsRlJLvPbEiIVFORs2p2iXvWSYt2B66x9r-_vgudoIMto0qmlECyDFnmbBJlqA4WhG__PH0B-D2ovyRvFx5vZz_Lb6X9Sl4fE_EdQYxOIMjwXYAzD44L6Z8upi48TxX4i6oYRj6J_eUbZe8rGhaj6Nt3ldE8I7K_DE9-9fqFaCWwT3YcjyEPNHEa3udcZpmuaEdzQV_vJZ6LlVoB2ICoxQEBX4IVPZw2eW1QW29zLmwdf8KGsY3zd2E1nMSB0TGAdA--xYsBle6s3lZ3RXpsY4FhKOtTie4VdDEp9JRd5G8a1NPZ93BgtCv-VcpuEwUw-3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=s63dQmmwTGlo6nV4cOHfsRlJLvPbEiIVFORs2p2iXvWSYt2B66x9r-_vgudoIMto0qmlECyDFnmbBJlqA4WhG__PH0B-D2ovyRvFx5vZz_Lb6X9Sl4fE_EdQYxOIMjwXYAzD44L6Z8upi48TxX4i6oYRj6J_eUbZe8rGhaj6Nt3ldE8I7K_DE9-9fqFaCWwT3YcjyEPNHEa3udcZpmuaEdzQV_vJZ6LlVoB2ICoxQEBX4IVPZw2eW1QW29zLmwdf8KGsY3zd2E1nMSB0TGAdA--xYsBle6s3lZ3RXpsY4FhKOtTie4VdDEp9JRd5G8a1NPZ93BgtCv-VcpuEwUw-3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=BL0_xZdZDHU_1xeXBrpciX9DDzUiCfFDAGrXNfmH27cpYq2rb7UaL2gCV3KdqjxWkV1z2eWU3lxp-9qrQlKWS1H28jQv2m2hkZXPj0gI37Pc7XEdQUubUyhwPQs3b7WAIMWvXs6HRzTCGhd4JDitC3dHLqmc3TBqw6U72-joC7i5ZAIXT7netnPPU-SgFnDQJLlMZjfSOR9kZkzlp1k6s1G6F0-Bd05mB2fX5DBZTjcggOvJvU54IOe-1tLgNIizMBgTd8FWQyOk18nbMIi2MZkw3zv7O6YXS2VkHMkeXhinPmataUtM_fk2VWgKopNr5aPl23FL83SsFRRVLEEb_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=BL0_xZdZDHU_1xeXBrpciX9DDzUiCfFDAGrXNfmH27cpYq2rb7UaL2gCV3KdqjxWkV1z2eWU3lxp-9qrQlKWS1H28jQv2m2hkZXPj0gI37Pc7XEdQUubUyhwPQs3b7WAIMWvXs6HRzTCGhd4JDitC3dHLqmc3TBqw6U72-joC7i5ZAIXT7netnPPU-SgFnDQJLlMZjfSOR9kZkzlp1k6s1G6F0-Bd05mB2fX5DBZTjcggOvJvU54IOe-1tLgNIizMBgTd8FWQyOk18nbMIi2MZkw3zv7O6YXS2VkHMkeXhinPmataUtM_fk2VWgKopNr5aPl23FL83SsFRRVLEEb_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=Oa9ZWRevBppeYDiZA4e79feS0IjBEDuXbMdJR7try9oEpfT9V-j2i5_2Jl7mihlZ6HHl1D0bCp5d3cZ1bYfPYD72x6gDAo2i4-fWpqJZQHHn7xnYnAaKAIqG1zQ6ma6pP0uMIW5li76SCbsRgtvLIYddnA4V7tBFrJB5ZorjNH17y-kYrXEZ5FGW2ec9nRs28yv6O4r1gkT8GxNw8etzSeNs-vmstKYqXDR2jN-W3uish-aJvHUW8fth5XwjGgfAGQAuZe71uRLRvj5XpejA-2zUKbKzyApy9GiNLsxrG0DZRvlwbrpOPFUh_rU2r9vi-fvqLpRGXDsaRv8L0KcNMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=Oa9ZWRevBppeYDiZA4e79feS0IjBEDuXbMdJR7try9oEpfT9V-j2i5_2Jl7mihlZ6HHl1D0bCp5d3cZ1bYfPYD72x6gDAo2i4-fWpqJZQHHn7xnYnAaKAIqG1zQ6ma6pP0uMIW5li76SCbsRgtvLIYddnA4V7tBFrJB5ZorjNH17y-kYrXEZ5FGW2ec9nRs28yv6O4r1gkT8GxNw8etzSeNs-vmstKYqXDR2jN-W3uish-aJvHUW8fth5XwjGgfAGQAuZe71uRLRvj5XpejA-2zUKbKzyApy9GiNLsxrG0DZRvlwbrpOPFUh_rU2r9vi-fvqLpRGXDsaRv8L0KcNMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=rMArgPzQYYHI_lJaNn4IMiIBlL98SjicqMRi6uzl4t7_mRDj558jgv8n4W8vbzeMeuLEwbTDTsyTZXqaHYbSj2p2s0AHZsX0y1qmanmtzlat0AxTkODuOOBeFr3O6-6xwP1IQQJ7_JGyIHbCxCM-L7uyc7oIYsvV_NPIa4pwFYfFE3BUaEjcXE4Hp_P6XE7Df14hI2fntS_WaS3GGIkclLZ3UIUH-0ESjhf2cwKA9jrAozJ2S9KDFNN5TWPd8VNYDTViww5NdhTelQAnY3K3P0klR_9LJhIWBwm5u90SNMghsPQULhOtH7dJEwqKZGGf1LL7nmDAfxnxweYlL7B-GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=rMArgPzQYYHI_lJaNn4IMiIBlL98SjicqMRi6uzl4t7_mRDj558jgv8n4W8vbzeMeuLEwbTDTsyTZXqaHYbSj2p2s0AHZsX0y1qmanmtzlat0AxTkODuOOBeFr3O6-6xwP1IQQJ7_JGyIHbCxCM-L7uyc7oIYsvV_NPIa4pwFYfFE3BUaEjcXE4Hp_P6XE7Df14hI2fntS_WaS3GGIkclLZ3UIUH-0ESjhf2cwKA9jrAozJ2S9KDFNN5TWPd8VNYDTViww5NdhTelQAnY3K3P0klR_9LJhIWBwm5u90SNMghsPQULhOtH7dJEwqKZGGf1LL7nmDAfxnxweYlL7B-GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=c0HO2r0DNc4DkLK985SJZv6tesaUoBsASgzRA6oRHbEZpEy04rM0ehrxWA_8ohnglwa-aTxKTz6ZuCBYbu_EMRc2VVoiqTz6DOysvSKbRdDghe6-TP1wu22qg7d6pr7stRWDLZOYFuuGcQiuq7Oq3DnVdmjhPD6zBgRYmzItGUldLK1cfYtWRp37TgeeCDuZ4__a1OwYQwaQDHBKAH2RoOb5p_t6THf901XWzT46vsJVNrpeURoWgroitwhjFVhbFWSsqmVhh3brx7VMU4ZB7kOkaMgdGxEJ-yYyzsSb7Oc2fiI3lJUklYgZYC_phygzcNdirLtkxtJ7bQuxtDCVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=c0HO2r0DNc4DkLK985SJZv6tesaUoBsASgzRA6oRHbEZpEy04rM0ehrxWA_8ohnglwa-aTxKTz6ZuCBYbu_EMRc2VVoiqTz6DOysvSKbRdDghe6-TP1wu22qg7d6pr7stRWDLZOYFuuGcQiuq7Oq3DnVdmjhPD6zBgRYmzItGUldLK1cfYtWRp37TgeeCDuZ4__a1OwYQwaQDHBKAH2RoOb5p_t6THf901XWzT46vsJVNrpeURoWgroitwhjFVhbFWSsqmVhh3brx7VMU4ZB7kOkaMgdGxEJ-yYyzsSb7Oc2fiI3lJUklYgZYC_phygzcNdirLtkxtJ7bQuxtDCVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmsbb_Yv9dszFU3t9lWrzxSOhHKtqhBYFxILRgCnuYY1ot2jP_MSYkfOB9JwYoPzCgyC0xfcq0KgaTE_PQA7zmKMVSAd2r0q-Gwu2ojCfPz8j3fKU44-I9Urq_O63rtmS7iu8jXx5KDSKwMVqqXyeFkt9NadsFYy_IkV3V8yw2jo_BS16TtGmfxqw_ibvhAYYI_yedL-KrLwNBmMdXrF01DHta83pcHYBlLDqmQjPzheHpfgHmYq0AwrDhQjQTCIyN9xk4UduWp--nu2HDMUelehO6tYVhhEfqUtLcBC7eA-gFUESEv15nWuveNOl4drEx8phcQoKOkdwu-BgD4Ylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX7mTqFX55N9Zu7wi59_bksAVYjuFLqXRoc7sAS8Gz3fRNiC3IYMdpc0046HuQivCWF0eiTY1NeBrpQRj0xUuXIanxd012BgfBTsXSvMSBbb2yBGyfRDOrNxfAoiJfcfI04NTULHviETWHxgB6dKeUj2kesMokcKLq8pA40U_uhMMYu50PUBwzxUB4RCv3A5bleDNiR7ggFU5fkx9U7f6NxKJ3avh1x2PyUPw1E2LewU15169EqDsrfdpnNmpkp6NiibB-xfXvJqZA6HIJ8pf4fI0FlDN8MEe_L21_3qZSnn6AFcHe6q2FszeJxZaVvW5JITPDGDeFqL4EuqbeExPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9adeCkWtsaN17NZdVRfwmJiHmIisSD6YHJxx-IQ9VKpPYsV3O2ucWj1bcBg7mhvhHyLjYFJHZdwna-DyxD7rpvBqD9efnjxAXfPGb84Ze9DBwVs7iec3OYxP_-3jlL55HeUeuxEG0Ehus79Qf2u3FUC4DXfJ8Nwk4YgDLQbQJzNcWQ6VmS5a6ArKaLywokwfmVDG7D8Cb5StPpQHJ_ikr7Bk_zmUqmCCMSYf3MjOsMADV-2n1FxwQHHcFg57FmHJF7ttqm8TESWXKH2l1607OgznGiNiUK8zWCgIRRWOmPyLqj7dqbikTmM-zdJi6k3K64aJae9tyujjJQYttJ7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=D65UsrOvsqHrh4ldGLu8pRboey4JZ6CRXqf1PlEMu4Icky4UiFOx9ELzAcSIj-YbsGoxrRBT7ik7YTu2c1nKXAA0KRk5nG_BOD0SDUKfOBql_iGNv4N3FKQyO-RhyAsq5m9B5pik4IentI4Cd03tM5xSpC9n45vtHMthwcwUSQbnOl9Rl9AFVibRhpGVGs_pRYEHf1wHLBMwp05A_QaEgWcyR8nFKKOq4Cc0e_EJHtvU-VabyrYC9OvjaUH7Lvf1ZA4fgpjV0QuPJkjktx3pMRhr4yo1K_vhPS6mO4Tt1q6e7YxN5YVxzli_SmjeLfNRpQWmTLBHPv0sRTMv9sjMSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=D65UsrOvsqHrh4ldGLu8pRboey4JZ6CRXqf1PlEMu4Icky4UiFOx9ELzAcSIj-YbsGoxrRBT7ik7YTu2c1nKXAA0KRk5nG_BOD0SDUKfOBql_iGNv4N3FKQyO-RhyAsq5m9B5pik4IentI4Cd03tM5xSpC9n45vtHMthwcwUSQbnOl9Rl9AFVibRhpGVGs_pRYEHf1wHLBMwp05A_QaEgWcyR8nFKKOq4Cc0e_EJHtvU-VabyrYC9OvjaUH7Lvf1ZA4fgpjV0QuPJkjktx3pMRhr4yo1K_vhPS6mO4Tt1q6e7YxN5YVxzli_SmjeLfNRpQWmTLBHPv0sRTMv9sjMSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7UZRHDghJI7hoEI9SLIn5-xZhtvBhhGgKODRD6hD9m2bqv7NDKeC6xGQqIgjPkrM_hR3u9bsNzp9d2UOSSwMivcC-xCEvlBWw1BVFk7S9DfliZbEVQJzw48-gkB2ak28OMXXELh16JHiSRgsgFJGLdWGMaDUK7khes4kIWlmoQju9jEk9UKiu9prQuRgTqkAfZa9lY6brpqwvGBd90HRo3zggtDA20rXlMYsmus8JHSsnxKGKcagstgfiiFVhNUujx59qsYYbxIlskHf30KO0xc6bkDzh4J97EZA2Xj6R_Rt1qkKcV2ye2Oj7rbUctXl81j8iEvGrd4YeHNnawwOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueGqC7sIdRlTYqlnCuZeLEFa55cRnYuz2FpfjK0SGuoXRaJGaI6X1JTJJMYnieFDq33_WZ-4aF-XWsW9j41FyGtO-Xk1l_Hzf5XFREpZZ5ms-PTxsasAdhmVqojBi6vt1tcRlFt7fp-klui8UnLypJINvau2rdYs0YdKiU4P5S-iUDJu_HveUmMiP1pJ_T33NAo86N-vBmbETgMuH7CMVX5v8eZTBcon3vNycD0X0A57DuoZxIPtS63NCfI1Kc3_tqPyuQLf_bmG5uo_9m8zlczigkh0qvEL_Q43afTJdRegvo13cQxyTB7hm4bJPvjrNHX-2nBamtwdeBPM-maAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=CbSCa3Gpgqzz_vvV9ZM9zZdWbplB_ltfao9lv5aurUOq4iaxAT70uJ-a6DmcELYNjhiq63U27xyY5sn8pqBxCCdfKhk7EYJWtYH1cPSbm_nZHBrBzlJyHSH6xkobggttX7xSic_JisxTtJlslHcaNnP7aZhVhvvDw7mZj6aI6SSCW963VFM99Qmaj6lij-catw0XtHehMjUcwbFK2eJF3bZ_jJsLh6RMYvEXMuNVFVjRUEMkFslKXH6Y2wmlqyvl26hTIc8beRbvmVspE-gfyTY9Mb8j3kB3Bs8MOBhlMc4l0ph0X5jjZQfLWIOD-SJSNhPeNamRwmmt-72er4Am8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=CbSCa3Gpgqzz_vvV9ZM9zZdWbplB_ltfao9lv5aurUOq4iaxAT70uJ-a6DmcELYNjhiq63U27xyY5sn8pqBxCCdfKhk7EYJWtYH1cPSbm_nZHBrBzlJyHSH6xkobggttX7xSic_JisxTtJlslHcaNnP7aZhVhvvDw7mZj6aI6SSCW963VFM99Qmaj6lij-catw0XtHehMjUcwbFK2eJF3bZ_jJsLh6RMYvEXMuNVFVjRUEMkFslKXH6Y2wmlqyvl26hTIc8beRbvmVspE-gfyTY9Mb8j3kB3Bs8MOBhlMc4l0ph0X5jjZQfLWIOD-SJSNhPeNamRwmmt-72er4Am8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZzS7x7FTqc3aS17fvrWW9sUr7ikffgGiacZuJXpdPMSjznoUfKtfl0F5c8SMJHz1tFLhnnJfpwZbyZEHJWXAjWXq5RCeS6doc9y4As_ZGktyBKi__BiwMiSacoo1-RcOjB1unbGidH74zSy2SbaQpFSECx9TF8qevo7PJFVD04HstOeYfxhPwxvQq6Gla0GEdvuYASx0gA25PWbW0yptWMYA5-ZysRfvvtOT0nFRlQ8ev7jUquKX82pCHxYJMJqopQ6GpoJB99SKXfEOnUCX1O9Lfjgn3rxOw1pNHIY9l7zi2dO4rS9EUhng1QNDyRHWQKpIx4jF62be3M34zQYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNk7hvlKOh_OYQEbG8JfK2xX83dw90kPzGhR0PBFjWGd7mhDXVE4-6GUVnEaQetrZJJbPA3PnGX7tAZygbPwvFEtT74F7gJ6jVofea6DenAGP7JCtOANtovdEMiI_pLagFcW31LmTrN66Eyaq1zwV2iFqX5QRhWcH5pUE6vDD1CRy3Vw-sh1B-VIZy_3sCTjL_aIZJconPUQPoup7wtwKmXz9vwqQIDOZKwWyxcwvw9O0hVjArM-4BDCEa23WhxXWUwCySe28qw0xPCyqHKfuxY0HQ4QY7gpsiuZ3qv1G6cqYR2gtwSTZi92Sjxzgk6fzZfBw3XUdYhPPdveBKLjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfBr5BnsE2mNFPgY12pBQ449XxJ2kD5mrEUPXCNX6ZeyuQfQcxVez1uRbPCT7TOJT3pX6hTeSG17Bt587bqWEVtnwKDoiPmpfaxIoKIRRY6AueyaN2iwqIbwRJXrsO6tn6ry090nVl_58tupttXEymR5hYd_SeqeeB-I4KzSSnfV4WsXOKz6QqJM08B08HhXyEmTeQCi3-rJ7hJDC8Y25APX_W4lGmUaM2PpJOuW-akFaY4ikG0hPuQjYwYiFUxYmGbHqaU5aGhtl-4bGpp3Pzmbzufg_IyQV17KSIl2CrNGciukZaAcSo7okM-Czw44Puhx0CfVytkLldKoeUwu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RV1WUGL1QDuXML6vionK0i5HOpTeizyOteKiuBYZRn8fgFRt1dmZksnQhg8_lVUjLb-lKXmOnze332NBRnIYm3OwReh-HbfWyy5qrxsj_eUPx6CebzzAxwGdrtTcPqMVWWSVJsMbOuG9en-fysU8IEYrH_207Yc3Z8v5y3dYEP7QF5vfjuq2BOWYDWuOxEgSeFicJsCpEd8s2TFqx92-IvowCo7VcbccgFrdVrAHUVV7uX_jOSNG_epAtLBeWaARb9Hgtu-MRT2EzY6COyMFQGrnIffvPIIO2d43oM0MvpTXXUpt95lSShxQF8V8vbtuN8c-k_2XSvIwEGWOPq2sZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=C6iEAAx2_adhfx3q-yiyMIiIEGNJeYmAxiHC13b7-OddTQ7oqHQBopvq2aGD6mbUDcHFoXMm_Rklfqf2Y8y57e0htIa5P9JCqRImcdaBN2iwzKhiH0RZEyBiVMCupFO7ymfl7hSqNeDikLO1d7SiTsWhVQxTRUe9OAWrrWuXIQqagZDfE0LnVbcCMGo8kkDrAJJk1G4Hnw_pJzlGOA1eunhcLp-BMxMxmwAcrO9IZLVwzH1xy16mpS4e4m160vJeLhRgxteApuBwbp8LwKfQLOygo3VQP2KiDJXZzrU6psIKOlINKEpDJQEDTzPeD0r4WJ-LrpEWQknXmz7V_k8REg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=C6iEAAx2_adhfx3q-yiyMIiIEGNJeYmAxiHC13b7-OddTQ7oqHQBopvq2aGD6mbUDcHFoXMm_Rklfqf2Y8y57e0htIa5P9JCqRImcdaBN2iwzKhiH0RZEyBiVMCupFO7ymfl7hSqNeDikLO1d7SiTsWhVQxTRUe9OAWrrWuXIQqagZDfE0LnVbcCMGo8kkDrAJJk1G4Hnw_pJzlGOA1eunhcLp-BMxMxmwAcrO9IZLVwzH1xy16mpS4e4m160vJeLhRgxteApuBwbp8LwKfQLOygo3VQP2KiDJXZzrU6psIKOlINKEpDJQEDTzPeD0r4WJ-LrpEWQknXmz7V_k8REg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=fmd-EgU6kAGC_gX4WP5bWeTs9u1tDvFcPVjsr9Mk0_nZ17nvwL_7Ce0lhzhREjYZhYE7mfTykNtcGhIe8GFBRLn6ZgGX_X8P1L1e5Rc6cmelz74CiB0JqFOo8eA2FpvdLSNFFVbeESn0WGbXoVa85tMc8bjkI7pTHYDhnCSAHqIo1YW4hdSd_ys7PO67b_WLPvJtwxhAChw1McADdAZrvCXI9sS9h2W8WJKwt16UCGWMLF05Qhi0FbJ4bK_kad131wEnf-MWqgCWfX8clEEkPZmK28_XEas1xL0ZioezC-rw80I106_yZeP482vSAletdABrVa6qQFeGPSfJfW8VHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=fmd-EgU6kAGC_gX4WP5bWeTs9u1tDvFcPVjsr9Mk0_nZ17nvwL_7Ce0lhzhREjYZhYE7mfTykNtcGhIe8GFBRLn6ZgGX_X8P1L1e5Rc6cmelz74CiB0JqFOo8eA2FpvdLSNFFVbeESn0WGbXoVa85tMc8bjkI7pTHYDhnCSAHqIo1YW4hdSd_ys7PO67b_WLPvJtwxhAChw1McADdAZrvCXI9sS9h2W8WJKwt16UCGWMLF05Qhi0FbJ4bK_kad131wEnf-MWqgCWfX8clEEkPZmK28_XEas1xL0ZioezC-rw80I106_yZeP482vSAletdABrVa6qQFeGPSfJfW8VHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odccl68FdWTazIxpz8wTYdq3nV9HUpAGykgKKKiVICqCslZi_R1DTvRTXF8YgPwwlrysgtRupz90UrgZrmmVk63o-peVh_DB5vCrOwJu3pxGw_DrqfFuzbxVvSoK2bbxbE13rWWxmzgxRlnnAqXhu4pKtzNSMPczQ4GsWiEX-uRKQfD4gIMB_uIaGscoNe69RdMLjI3J_sX0dPnEwpj3QFyBLP2UE-AQOjCXNd7ABRgrjCBc4Wu6MqOGWsH-DJhy6UHnhwNnLLdTapVbxEj3jvY-QrR5iyhRSXgE-IaVV1isHDgavKLquxUZxLKanXLO2REf4zC1ZzZ3EIKPxQMu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=ZEpO4ZpHqY5fo0eBkRtaZakOac-GgbXwJ0S09Gqc2vQ94YBGNbvAfDcNI_YqeIiaCnvZs6LnQcoC4-gAjUEHoQNhm6n6CuCW4fl8VmlNuGUDWxVP6P_XQvfjIIBkY_AdMGssUbPLkZ6690h-Kf9Hqa2Y6MQ6KV3IurV4nJ3AtUGdjFjkf_EvKKdVHGV9AZEFghAigicjr21U2LtaLWd02xsSzgE_b7WvE2uSfRnaB2neD56UMRJa0oFtqqeuDjWWapU_XqSPNuVxK3Mi3IUbyie4qFoqhM62Rwp1udRV4uWqf39I1taZdlNgdPm0ez1gPRrN05ayJQ4856hylmZc0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=ZEpO4ZpHqY5fo0eBkRtaZakOac-GgbXwJ0S09Gqc2vQ94YBGNbvAfDcNI_YqeIiaCnvZs6LnQcoC4-gAjUEHoQNhm6n6CuCW4fl8VmlNuGUDWxVP6P_XQvfjIIBkY_AdMGssUbPLkZ6690h-Kf9Hqa2Y6MQ6KV3IurV4nJ3AtUGdjFjkf_EvKKdVHGV9AZEFghAigicjr21U2LtaLWd02xsSzgE_b7WvE2uSfRnaB2neD56UMRJa0oFtqqeuDjWWapU_XqSPNuVxK3Mi3IUbyie4qFoqhM62Rwp1udRV4uWqf39I1taZdlNgdPm0ez1gPRrN05ayJQ4856hylmZc0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=rfjdkq4Z9qnmRY2i6aQU2p-KyK1gzVraYgUncrCPGDjhqJ3aMm1g-0kkttMuR7b1dMQlMcZZAC6GUry4fZ9C9jes5gAyqTs0aB_o7n1gd9TDuL1m5vCOTtQouV0ZVUpIssa1cKx8B9E2EzOBt_H1ORHTKlm60TOTZRsf9hRkrFdYd37BEGbgFp8gPdDYm1VWZjnYcQIv7-3Ku1ssTiF4FM8eEFhmnmt0gEM9y4OK7S8tGUXc-Qk6w7RH2XWyBjfpin2B0_GiAURei8jU2hlvoRZq9OPpmRiYo8Bqeg0l6Y-mzLn-5mhcI8E4vo37QflkBwTVy3G2yumznf7Jv9XeVJMUdYVmLaNIAcNjEYgHSQakmhi3anEvf1z7IYX0TbdVwiSUumFPobZbv0c2lQTrZ6z8CrCNx4bxw2L8MiRCtbwT9-Nrw1A_uSR7RN9PBv50_JsjrqqHUsji2tP2iDYWZX_fEfdkEsYNiiVqNjZmpWQih-NOCnkgBMqSNJ26K__iblunEu6WBfIGMuWBO8cOv49UrymgH-BxLl4fixfuJ-UadtFmx_nkKqMLMDw4aZkehHMqMl6ctHvIfLDWcKf_crPA6YJY2QeF3myzKZcFUor7yGd5fLjYqIVq5Vge3RVcp8XXTqigEv-c3deWHZJX1jhJ-X1gvTsHHyfdb92rOxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=rfjdkq4Z9qnmRY2i6aQU2p-KyK1gzVraYgUncrCPGDjhqJ3aMm1g-0kkttMuR7b1dMQlMcZZAC6GUry4fZ9C9jes5gAyqTs0aB_o7n1gd9TDuL1m5vCOTtQouV0ZVUpIssa1cKx8B9E2EzOBt_H1ORHTKlm60TOTZRsf9hRkrFdYd37BEGbgFp8gPdDYm1VWZjnYcQIv7-3Ku1ssTiF4FM8eEFhmnmt0gEM9y4OK7S8tGUXc-Qk6w7RH2XWyBjfpin2B0_GiAURei8jU2hlvoRZq9OPpmRiYo8Bqeg0l6Y-mzLn-5mhcI8E4vo37QflkBwTVy3G2yumznf7Jv9XeVJMUdYVmLaNIAcNjEYgHSQakmhi3anEvf1z7IYX0TbdVwiSUumFPobZbv0c2lQTrZ6z8CrCNx4bxw2L8MiRCtbwT9-Nrw1A_uSR7RN9PBv50_JsjrqqHUsji2tP2iDYWZX_fEfdkEsYNiiVqNjZmpWQih-NOCnkgBMqSNJ26K__iblunEu6WBfIGMuWBO8cOv49UrymgH-BxLl4fixfuJ-UadtFmx_nkKqMLMDw4aZkehHMqMl6ctHvIfLDWcKf_crPA6YJY2QeF3myzKZcFUor7yGd5fLjYqIVq5Vge3RVcp8XXTqigEv-c3deWHZJX1jhJ-X1gvTsHHyfdb92rOxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqWvLID_vew50xZGNWW4lp-_lDbzi8zZjFjb9m-Yv14nEgb4lvRCBBD-pnLnRs9JDzf-r9EV29GRla7WBid0wQN4_-gBrE8KZcUgQaDJb5dAAu69snU6jZrBs0CXrAlOmQD31H6Wi4Q0qAZufN5GZWUsv6C4g8bTaBOgB50YPDT3tRq4YrONZ8h8g5HFMBdX8hK5UdO6Ag-iS9Pjrwcdx6Qdel7HzyFBhsWRsLEo7aeLEYmk8yYKl3lDQjYwultUuiZnNwEn1g-kXtt6HXn1BY46VxpeX3HMkb6g9KlGMKMs3Vr61qc8RD9GpajQPzUXgyBYyA7SJy2sYLJoKBVj7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOiVHZet-YjP5PWxCVioxiZk6ILkenpiz59pTDX-EOApo9Fk4-x-S81Y2ye2id0T4V02Lt1k5tPLQXLLX9_ts-3tPat35d3BIIjEFTNjTn8QYm3TgNDAs3_6_Y5hnHKfaVtj8AC2r8BWPzDe7oOPUoVXnkQpZQsJin2_UqvHWlojAG9y4LxxiD0z14-sUP9TJTkGsW3hYM5sOsIKNAuQdrT6Kn7_8ZMwCfMlgVtus0Q-N9ZSN6DhuT_2LySqt_dUIEGe35kYA7FCcq24anXufRjQt418hlf8ZEIGjWd-MV8gG3OTSQ5ohq9kBagyRxmgdbNgLpqRHMXeoQD_TlAKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgF8uaEqiCgWmN5VCMmTpud7xnodH34xcaNvDOSXl3J390nECHoObeZN8O2ayH7Y16vCZO4pQHWFVsnfNAJ638e_4QR5vY2SbsC0-ZjIqNzip_pAxpA0ghe53uzkCRtMASPBgzhfCiZerVTaYjQQah-_ouR8xdoJoEWCi2AxnInL21hRPC_DM1YSe2dx0bAJ18t647h2U9Olp_M8DmVwtCikEyyTqEJI5eiDi5ghBuSLOnfMYFO_NfqlJFYsxmX2NotDCKasfPdQY-3TaxyDGpz-ukhWA_pL7LUL__djQEom73PmCUHvlDBOhoyPgEGN2kC6tt0fBrzvEEVvbVBDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgn5FOKyggYjxhx9-dXRLO-eUI4B-OPefk4Oge3oLmd52P5mA7h0NEPIo7jSJ3cpCw55vW2jYULFd3CazAdqLBpk95hVolZBcmhR_vKhvUm3i7NAgENK67SiivrzDappXuTfJ4HnfcOneLGa55RnXTveP2i2vta5OWOQKWJ1p3AQ_dhJdxfYxf7Y5qAzj6Y6uUZC9UOQHFzzfg6abdjOTKTCYmwEVUY4JuZVxrJsiNO0NxG9_g3yrJis7auK5vQShJTtVvyfEYNan_EMcXwuehDLrpXc1_9fc5nZGxEfQTXiod8EN10ti7fsJb59apRSC1RRM3aTy5YeUU8QiWpZZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=jroDTaOy4QY-_blHRf4Olq4s1pT6ur5QHCZl8hKR-h3pkJg2ZlqC37XQZo9lw7clYXGzEhqfcGyUHR9UxYD463jQlJeJGzDHJEiKfhw9uUVggYBQO_39MhHSSL8peHMHzzY-pz24KlHTtCSw4ZspmmKPAEuEWNB9_N_ku1tz-q2hfdUAQ5hoEPhtvtDooD1z0vlhXr5L_ZOBDKsRzWXL2QZZdj-6Jih1J21mMLbewazpM2wt-sFMsmMfZYI_z3kOPSuH-FsYsqJtj1jVHy7N25GeXfockUpo-3OvE9kPcrnDQWtUSWoWLz8w9qvkuwW56J95Pzn2JdrTjVb1awRS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=jroDTaOy4QY-_blHRf4Olq4s1pT6ur5QHCZl8hKR-h3pkJg2ZlqC37XQZo9lw7clYXGzEhqfcGyUHR9UxYD463jQlJeJGzDHJEiKfhw9uUVggYBQO_39MhHSSL8peHMHzzY-pz24KlHTtCSw4ZspmmKPAEuEWNB9_N_ku1tz-q2hfdUAQ5hoEPhtvtDooD1z0vlhXr5L_ZOBDKsRzWXL2QZZdj-6Jih1J21mMLbewazpM2wt-sFMsmMfZYI_z3kOPSuH-FsYsqJtj1jVHy7N25GeXfockUpo-3OvE9kPcrnDQWtUSWoWLz8w9qvkuwW56J95Pzn2JdrTjVb1awRS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkVg-t_w0A7JUCzTF_nkF7Je2-I4GzF0knVNRCUggWWaQ5qOVRq-TczneGPdFwRR_0h0bnBQytFlraxAPjLetVyOt8xqhW12Wk2G3WQN35UFlX9kmHkzF8rqabJ2YQI_wx0LpslFs-9YMVPa2wSCv7oJV6rWWpNsEaW_BLmUpr797Lzbbh9NmeeDH4D5BMP51NmH3d7XOuLk55ycgCCfg5lgM2fpxYttBqWtuOWcizp4JVdLLJ5d_tdJy8XXR-XsYCQ6bNXm1eaS7gGb_Rl9TeSm-R5pslGmKzuyigneBqotMev0mFQZ6ypbyY-TUp_nKvI6FbPBk4aJa9K4_AO_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaA2mMroG_ykqjULwxe9XJXTFVd0b5y5btkG9w_gO8JoVqTcDQVp0QX_PD76XjdUSaaxwcaExfu1rgken0guSUHQb54rnMFY4o6RJpYgytYdVX_q6JKMzjsLA8kYDYxC8Wh-BQjENZe7ef7wPstlLBDQU0TaEqlrar_H-k0N0vMu981A8DhkEcw7vsT4fqawCDX3jUvXgrNeEn3_sp22RiCf_p6qzRPC83-36U-hLejNTQXE-AtiOb8UVhW1zoKYqe0PIlmupFQtOqMlMOp1AL5DZtbZeTa4mX3P2wpm4mHbr9UUaXZ7pkuesgA4FAVD0b2Lq64OCvEZNRtdlKMeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=POdXZnaBkg8fMHswVOmc_z7ItcmqUJG9Qoa4dj40FegNZLy3NEr0zevwquG8FzcUsO2XrSHzTPvWkKMiAgeswozovWD9-_IuU95LkeldnghZ_KACoC0iS-bkFdesQsSjxhCi_KOMre6MHxVw70shOVDIBgy5FrSu3E44d04BaOS-ykCeAiMsnP1uK_EOm8S6JMQy2hNkXX4iZR8fbHmLLkd-LErBouVxIvnh3xta1HobX5Mj83UfVtZk8ZsnuhAzNHchqvfx-Wo6T0BzYldxPkTyRGm2pTIb809mYC1G5BAJhS8Apn8NsMsCBX9w0qHsKMKddzoLWRZHon0Otrs4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=POdXZnaBkg8fMHswVOmc_z7ItcmqUJG9Qoa4dj40FegNZLy3NEr0zevwquG8FzcUsO2XrSHzTPvWkKMiAgeswozovWD9-_IuU95LkeldnghZ_KACoC0iS-bkFdesQsSjxhCi_KOMre6MHxVw70shOVDIBgy5FrSu3E44d04BaOS-ykCeAiMsnP1uK_EOm8S6JMQy2hNkXX4iZR8fbHmLLkd-LErBouVxIvnh3xta1HobX5Mj83UfVtZk8ZsnuhAzNHchqvfx-Wo6T0BzYldxPkTyRGm2pTIb809mYC1G5BAJhS8Apn8NsMsCBX9w0qHsKMKddzoLWRZHon0Otrs4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=c9cybyiO8UiGDtlYJJLu89e1POE-WLVsOwc9EujAh79Y6r7SKBkecPCHnF6jfJhZOp3oFhoS8pDvlKVjC1f6kc5bk9PgMUqBXtzQSxdN15L3QRmZktGbXJ5ZAGNzEOx9Qifme8iPUdgMdA79YLpbz9LUZK6c_cfWqVjCcQPON6s3HuqrhA-hYIalB2awS7HgcclQlJmr0H-ElC5M9t1LzKbfkDpjFIdkAAtm_MyicatN7cbaQ_-03nBzJGuXK1pmL2FqG0ueYtOmDnp_eJkEfV0i7bGGUKnF4al8E28KGMq9OvYClq-dQg-B9wYA_sdBiBlPeKe8Wjx43jrJTOcfYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=c9cybyiO8UiGDtlYJJLu89e1POE-WLVsOwc9EujAh79Y6r7SKBkecPCHnF6jfJhZOp3oFhoS8pDvlKVjC1f6kc5bk9PgMUqBXtzQSxdN15L3QRmZktGbXJ5ZAGNzEOx9Qifme8iPUdgMdA79YLpbz9LUZK6c_cfWqVjCcQPON6s3HuqrhA-hYIalB2awS7HgcclQlJmr0H-ElC5M9t1LzKbfkDpjFIdkAAtm_MyicatN7cbaQ_-03nBzJGuXK1pmL2FqG0ueYtOmDnp_eJkEfV0i7bGGUKnF4al8E28KGMq9OvYClq-dQg-B9wYA_sdBiBlPeKe8Wjx43jrJTOcfYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=bhbZ9l2I0tPZuDx67AJjiUGc71uleCJmahB1i8YSYrUNxCOyVIgrEMl-ISKjtzCtKdYyR4PubFrTgP4Ia8Ubrd5hAgFmVXvnkvRG_kylcoH_Jge0s6l62XF9-oiBClCjPyhMBmlxyel9gYlOohgB1CUjjLQNBC8v4DnArW3rH9-j6HzNdxbLgjqoTDdW_g6XkxmQ-CQZ3IZ9Vve0m4TD8xzEWo_-ALG458ad49riifdwkQNIRSGcyAfbvjcpfQsq9toSTKTSmw0Wzj7BUbiGC6zxvnFAytCnPkKZwEyHU7G2tq6eqZkMuMrx5HCqsxp28B5MSRuedfiiKZo_3GTFPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=bhbZ9l2I0tPZuDx67AJjiUGc71uleCJmahB1i8YSYrUNxCOyVIgrEMl-ISKjtzCtKdYyR4PubFrTgP4Ia8Ubrd5hAgFmVXvnkvRG_kylcoH_Jge0s6l62XF9-oiBClCjPyhMBmlxyel9gYlOohgB1CUjjLQNBC8v4DnArW3rH9-j6HzNdxbLgjqoTDdW_g6XkxmQ-CQZ3IZ9Vve0m4TD8xzEWo_-ALG458ad49riifdwkQNIRSGcyAfbvjcpfQsq9toSTKTSmw0Wzj7BUbiGC6zxvnFAytCnPkKZwEyHU7G2tq6eqZkMuMrx5HCqsxp28B5MSRuedfiiKZo_3GTFPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=rlcxYk4G3Oikh15G9w_DVILmAnKRWeWB-PRs5q26zkxyfJlcpT5pw34Ey3xtaqjM6ODQ2vyMOvjtXmM8WUs4c6nKY1yfSQfxuizGBh4BAZWax0YpsdLKD0kzV0lvB4AsG0ozAy82Mr16dpYSQNCpnk7F5FSK9bE5oqcxc1oMigOztM7hFycX7AMud__Rrynwsf58h0hjTwQhTyfe7j3HI3PyqLiU0Ax4Fof057LA_6nK8LiTcYfSYfEZTUoqRG6S0pCmcvomEwvZx4dTpvUbH1-ORL-SG-nUT3MkOgWfTjsqcL1_xkn5EWdkHQMqs-Cpba7V5bMmtaL1jy4baqa-FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=rlcxYk4G3Oikh15G9w_DVILmAnKRWeWB-PRs5q26zkxyfJlcpT5pw34Ey3xtaqjM6ODQ2vyMOvjtXmM8WUs4c6nKY1yfSQfxuizGBh4BAZWax0YpsdLKD0kzV0lvB4AsG0ozAy82Mr16dpYSQNCpnk7F5FSK9bE5oqcxc1oMigOztM7hFycX7AMud__Rrynwsf58h0hjTwQhTyfe7j3HI3PyqLiU0Ax4Fof057LA_6nK8LiTcYfSYfEZTUoqRG6S0pCmcvomEwvZx4dTpvUbH1-ORL-SG-nUT3MkOgWfTjsqcL1_xkn5EWdkHQMqs-Cpba7V5bMmtaL1jy4baqa-FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XFKgHJ61-BeO5Gyh9MrJRPdmCIvgl3x7egvA9SblT6h5_egaLEhzlK5hN8UeHCd7xbgA4TtcYsx3_am3F4WNyPXBgWMOFVVVCrJseOxo4TPb2bwl0yiKDGqVO8Wuyt9SPg34Fjb-PGhRX8TquyIqs0kyt1Pu_E2_jsEzSc6amgAOHpBgzMBmSNApW4BaKeEUeZXafaDKEOENExrGhrBtk3RYVP-RIGIioBiSkoHAfzTJEbaKf2FhaQo6nPUiLk7FY4jzEp9GlzIX7SgrZHf9u7d_LdH1VN1GO-TWugidXGoMEahd6i7pcIMsg6PQfW3LhRgix67Ypc6afXc8I4uJ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XFKgHJ61-BeO5Gyh9MrJRPdmCIvgl3x7egvA9SblT6h5_egaLEhzlK5hN8UeHCd7xbgA4TtcYsx3_am3F4WNyPXBgWMOFVVVCrJseOxo4TPb2bwl0yiKDGqVO8Wuyt9SPg34Fjb-PGhRX8TquyIqs0kyt1Pu_E2_jsEzSc6amgAOHpBgzMBmSNApW4BaKeEUeZXafaDKEOENExrGhrBtk3RYVP-RIGIioBiSkoHAfzTJEbaKf2FhaQo6nPUiLk7FY4jzEp9GlzIX7SgrZHf9u7d_LdH1VN1GO-TWugidXGoMEahd6i7pcIMsg6PQfW3LhRgix67Ypc6afXc8I4uJ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=jwjyfzckxI7asJuprskSCXLtKcOW9odo6dgb-IbSvrrE2NoLxkrzlr9JOVWE6cMZ5tk2BpkGKfa8yRsIq_hqJ-tmAnWNGvjS_JURdsG9R--0T0Y6y6cFMkhzq53fmlCuuw1k1uBJ7E_X7Wa2gtpRggaR3rMbEn-T271_2WFzdGRNzA_ctiqfARd2__UkqWwnXNXL_moCBbu1jsdm8EJD16sH_m5GPjAqGZTo7VYWGoJ3W-9p9yB0uDJS4jDZnb3hhdVm-GhGVnnQPQLb3noBixdC4njj7G0YV1enew-0y5wmffxkOfi7LdXJcPGc87GrmM0c-GRMBUev46aEFSfQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=jwjyfzckxI7asJuprskSCXLtKcOW9odo6dgb-IbSvrrE2NoLxkrzlr9JOVWE6cMZ5tk2BpkGKfa8yRsIq_hqJ-tmAnWNGvjS_JURdsG9R--0T0Y6y6cFMkhzq53fmlCuuw1k1uBJ7E_X7Wa2gtpRggaR3rMbEn-T271_2WFzdGRNzA_ctiqfARd2__UkqWwnXNXL_moCBbu1jsdm8EJD16sH_m5GPjAqGZTo7VYWGoJ3W-9p9yB0uDJS4jDZnb3hhdVm-GhGVnnQPQLb3noBixdC4njj7G0YV1enew-0y5wmffxkOfi7LdXJcPGc87GrmM0c-GRMBUev46aEFSfQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlGNRvLybSPhe-HQ8NzqAzkaeC3GxDCBDaXJR0xXO4IsVj_107Q-I0k_WFe2zdglu1Sd65oyHwk2W98oOTsM7NG-JJqFdPTGkBUfYjLz1kg-sygRZpPUQTTRMRMexMx291RJKnZmuot2Ch3HA9eK8lJf1Nn3NjD2jFe-v3LVts6I2rZjhGk14rPvT9LRicLeXNyAF6AS48hoTMfYJVhT7ZhUyCg7Qb_GmCkz6zwbiWdi6WZodZWxpcDraeWOGhseofENJnMXXu5IwvWmAH45u6pjYpJdpJjYvWo0IhnYGT78T6VTmKZsa54Ue-OK6596h7IYVJrckuepLApOq_wPAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYy5Isft4luGhy5gqlnF1uXCWF_KZueXM6r1fid9SbP72nmJOoiOuWfBt5XN0VgHilNQVVbCJFf9jBPtzhiC5U9T0vOkvCNMl6mjtFnHOqk0nACe5WXfsIVnm6tJ4qOQTZo-a1IOQS5b-_mF0zQC6yGX1RegYX_hldtKMxLEDioucpcD4CiDMOM6PHeyjJyi5IxsuThC3TSEhqIBOgm-ko9KOBYZjH6QIzHp-yvrP7MZzv1EaYLZ9KnjPtoPDiXlyHprg8qQ2ELZOzBCXIOB90YkqEF5-DsETRU8tUwnfVUS7HOCeG9TbG7zXX2eGV-VmRFo_WsCzNlw0vs8I5foog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
