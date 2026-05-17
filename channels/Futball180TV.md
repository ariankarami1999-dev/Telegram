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
<img src="https://cdn4.telesco.pe/file/Ev0KO_6O2yDoZyHsoFmLu59XraE-TvDTYs-NkWyO9qG6_K78voT1Rxoy8tYAQj_LK9-nIO6P92kQZaXS3A5T0YfAAkVUcXjNOZ9h3ec31ZZpdkh2dVcs5fjr3I1YbNoU0tSuFEOoGlZO1HzsD0YDxKwI4gjAcfpNgwV5z_jMKge1n2sLqKNiuX-gGP0stOVEDwS28B6GOrTcK26jGga7_IVy2exE8Axk6LYYxMKMZFOtE41p6NAkPM7jRIRpTywHZxgzV8XcI2hrDgsa8_NUpzMEaUvS2q1DarMH6K3XCKupqSZ35-BXGzd5G2hKHJbSz-r_yGmhcJlfbLUxsDVOxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 134K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 02:56:55</div>
<hr>

<div class="tg-post" id="msg-90027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/Futball180TV/90027" target="_blank">📅 00:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90026">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oltP4hM9K4urcNG0BkvbIKVyNY464KV3ew_mhOzDJpNm-emzLvA3RvmZEPXCPVY3taN-74fGw9C9ufJPzH8J96a7b4l_cWlSRfWVkZuCAxdDeAIBRZ2USIOiAFrXWNtLMpvbiX79ey4frH62qbcrr05sXGefzLPaj8fSKlqOqm2_6xI5hd8uIL-VhRF0fkhLMzWWJue1TkDHnARwZ7nZxwiMV6f48C6mxlk0ii1TkS0sS6cDL8yBOyCg4WoRMFXu5vFozr8DTj-puvYcIO6YfNk4BdlzL45TzIVNTk-D43-AlzqNdoIEegnr2upmJbdUjoNy6nBB-mc4uzm6RwmNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/Futball180TV/90026" target="_blank">📅 00:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doFrFVqiVp1kUQQG4GIW6tAUZqaLLONCpJU_VAGOM4FZjGb7uvaQo2T0prP99TFVaPItwhgbAwUchMCO-MJAX15FaXYc1WR_76yNFL7AE4bG-QrDQHjKZCel9T2049mfafWp_AnW9sfEko4rFto3v-ESLKpwV4mzyjTapCx0OWiJ0YWajz1vnmybsPWsGx6N0DacAxKLMmv1RmYcjLq1iRvUTEls-0ED3VBdArH2IVnUJ5pyS8Jx6qtCzwpe9dWpCtFLrhe-0h6J01DnZqh7bFcZoq8imEhQU-R5FblKTgwp7UJBNBqE6uClu0ctLflko5dr8r46D3lovDi5qGE4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫪🫪🫪
🤯
برای فهم‌اینکه لیونل‌مسی چه اعجوبه‌ای هست کافیه بدونید که این بازیکن سال ۲۰۱۲ موفق به زدن ۹۱ گل شد و تیم وحشی هانسی‌فلیک پس از ۳۶ بازی لالیگا این فصل موفق به ثبت ۹۱ گل شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/Futball180TV/90025" target="_blank">📅 19:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=iQPxfHv7b1Rt9qzeYQLd9CQ4LI2cecB179CBEAGN0aslaCTFpJc-RwzI80dAE7fjEBxuaorsSNNx_j8-zkWimxnhuVvPhjk44LRNmlgLpQzvGvML708NAARgijzVeg-8cMYGlxmMu6Al9T-2wLAfq93Oc4OUyVdFTbq2LsFwMZw-jCeNL-B4UojZyar9SZpX-eehsvGmiFABfM3kVgbDYI6WafAbWaO6dwx-TmPCDGe0m1Me-1W8RanUmQhPGfv__p4PR-G4ScMUnGODlU1Abh6BNViKVnGdXiYtKrUix2RnYdgSYZTR1eJ88JBguc90NUMzUrfqJ22DlnJMK6N3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=iQPxfHv7b1Rt9qzeYQLd9CQ4LI2cecB179CBEAGN0aslaCTFpJc-RwzI80dAE7fjEBxuaorsSNNx_j8-zkWimxnhuVvPhjk44LRNmlgLpQzvGvML708NAARgijzVeg-8cMYGlxmMu6Al9T-2wLAfq93Oc4OUyVdFTbq2LsFwMZw-jCeNL-B4UojZyar9SZpX-eehsvGmiFABfM3kVgbDYI6WafAbWaO6dwx-TmPCDGe0m1Me-1W8RanUmQhPGfv__p4PR-G4ScMUnGODlU1Abh6BNViKVnGdXiYtKrUix2RnYdgSYZTR1eJ88JBguc90NUMzUrfqJ22DlnJMK6N3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👋🏻
پایان عصر کاسمیرو در منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/90024" target="_blank">📅 17:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=VEAaeH5YsQ9AlI4Lzgxxx8dnckzky6KQlpNltSBg1C3YNt-1LjAhMSuQMxbMdpg9pigXK2MqHW2PCBIeqCOiR7VYSjV8fDNrO5RTnanJPA8MfczYgXxZq_0vnkZjpagU8s-K8lqzj64g0LbzbB2wS6S0Bc0JpfYpx43P3LdqaZ3fnebvXxcisbdcPidvNDPx100dykSaVmlVlLLc3MQGFBFhxzA_a3uJxaMaJIK3F517kmTQeZBH2ZYm3koT4-xjoWxHQlPl-1XmkplZ0b9TNJkb0uhWAubXCsQgowZvHVQQZrH_awmx2vuDuIlD9Hpq7HyuD85Yy2JztYS8662Zsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=VEAaeH5YsQ9AlI4Lzgxxx8dnckzky6KQlpNltSBg1C3YNt-1LjAhMSuQMxbMdpg9pigXK2MqHW2PCBIeqCOiR7VYSjV8fDNrO5RTnanJPA8MfczYgXxZq_0vnkZjpagU8s-K8lqzj64g0LbzbB2wS6S0Bc0JpfYpx43P3LdqaZ3fnebvXxcisbdcPidvNDPx100dykSaVmlVlLLc3MQGFBFhxzA_a3uJxaMaJIK3F517kmTQeZBH2ZYm3koT4-xjoWxHQlPl-1XmkplZ0b9TNJkb0uhWAubXCsQgowZvHVQQZrH_awmx2vuDuIlD9Hpq7HyuD85Yy2JztYS8662Zsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
لحظه شکسته شدن رکورد دوضرب دسته ۱۱۰+ کیلوگرم دنیا توسط علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/Futball180TV/90023" target="_blank">📅 16:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
جزئیاتی از درخواست‌های آمریکا از
جمهوری اسلامی
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/90022" target="_blank">📅 12:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtIbzCnvJ_oHMXHOSMYwqmd0ITDN5DvlkOhFHy3OLmiYUTCjJvw5V2_jfxd03Oyi5xqDDcMJvV4d3k-ouT-Xu3x8IpIr6D-5rDE8LXn3NsICayl9kxcWY26Q4mKZ57FkYSmfoz5ReuzfATkyRcgaw4VNmAcR-ZV2j09HxXlyZZtOtB7jxq5OF7gyST_sgB31muWsGYIB_oRT5Sc4_J9-eaTxZVoVx5Ubx4p1_ctV3Iukl3feXDNTdES4MyLCZZ6GAacaZDOc5KrdVlxG-mfjGGWMv9GEoU5-2SVUfGTxstBmssHP2Y7DsITlIgaeG12R_aaCcPj1fmf7ikQvgWzMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل‌مسی از سال ۲۰۲۱ کسب ۱۱ جام
👤
کریس‌رونالدو از سال ۲۰۲۱ کسب ۲ جام
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/Futball180TV/90021" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90020">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/Futball180TV/90020" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90019">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1wuzG28jOXE3QfwHMMG3DFixHBZSDscI8vb7YJ2wN-rDSg6_mg50fa3L6z2oZP-qDfIiabueXOm9hza93mQoD1y89CxhM_L7njDaIrC3kiAppHOjg5ErBXUucu4z05dc0D10q4OZMhrJWXGTbStz0uKAZYrDyclgYu3_lg4ri-Bbc6d5bIzNORTX8CEQIwhUuhRUYmPu-PyrnrzKmPc4J9IfC69GtgSvarqsY1BJnHIqlNlgNg47TUFatjXAjPe2b_jdP0Gy_2cc8t0Y89k9c3olBxbYhcKdOh9GNZ2m6mYVjXZ5l4GNGPnGRvlCvN_JLjnGebHdUNeW-F50oRvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/90019" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/90018" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fShTKsQKP9150ROxOazqWG2QIyK0-jmEBSieGAIHSAtR_qSe6nPS42q8nl4ovk4exXw84hbaQ_796cP02FvreF8b58FNwwca6lAFfR8RCSgu66aMGjfknPMruSJeZGT1NEsdDowr35SIl9y87QZKuVmMZMYLayUzde3b8-hiI3H4A-8xRVcM9Ny_k1xofYvvnG6yjraRWLjWYBhpy_8xCN5IU7BUpGyY2V75h-m0AoBicslXJBOA-JZGv_P9XKmFAhFXYlGz7vYfRTVkiY-_lfZnDR_iYeQD2oQ0Z0mo7zJ9P87pMWwInRF5FFt2SHiGZffuS3y5jyWX6uUolYNp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/90017" target="_blank">📅 11:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS5nzm6KYYB7eR3uCqT6datJTFCYCV2Lw4yDJ_Ci0Ei53RzL8rE2-scDSd8le83FX0UCXtZ2QhtS3GqoDxP9NH9FGtnEE4YAruw-_Kbl8FGke-1neoZV2VzE0712LJJWkaU_kUlPIi4tN85Tz7Bn1N_Zb9Jk3za9PfAHcG2TNhb9uM2AAdbed3uDeDsqBcMXqXTjyeqiI3M8Y5b6FnGYK6r4azTnirwBQ9nvUW_Feutz5WI_h9xj6ZV-WX3cWvuIr_BxqXW8aeVbCzwXwG_x-3zYWAnVB_IT-FFRpu_5y0jBPj7ZFE_aCF-cNps71JsbZxkLT1BgLaYKVeVJbNcB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
#رسمی
؛ ژابی‌آلونسو با قراردادی چهارساله سرمربی تیم‌فوتبال چلسی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/90016" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
⚽️
تیم‌فوتبال البطائح به سرمربیگری فرهاد مجیدی در لیگ‌‌برتر امارات به لیگ‌دسته‌یک سقوط کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/90015" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=NZf1C4rtCq62iLou50_CsVl4ISxEOCmr7p5mLN8wwt-qUufUxbhf1e4h1_UjUk_RHfljqUUHm_uJz9plkmQOhA-liY7GWl8O60p-wXQbss5sQ00QdKZCjDd-6p6gblsnAzZ0G7-nEyaVekDM_REIFczW9qjGPhLGx2AjX7RATMEChOBP1dmhLv7i9jjt8vlwi06dsKZopeLHoKc5rTMcgZIHOBCiR_5TyeNqF-lCGXtZXCDiI1GrmP7BUZ7_FBxMP7WG8pbQMtsFy8j1fkcjw1OmF0_U3jSOyMVQuGwh2-BWo1DGWN_m-RZ78NoUpyL7viph94sk3hyYclR1bOvK4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=NZf1C4rtCq62iLou50_CsVl4ISxEOCmr7p5mLN8wwt-qUufUxbhf1e4h1_UjUk_RHfljqUUHm_uJz9plkmQOhA-liY7GWl8O60p-wXQbss5sQ00QdKZCjDd-6p6gblsnAzZ0G7-nEyaVekDM_REIFczW9qjGPhLGx2AjX7RATMEChOBP1dmhLv7i9jjt8vlwi06dsKZopeLHoKc5rTMcgZIHOBCiR_5TyeNqF-lCGXtZXCDiI1GrmP7BUZ7_FBxMP7WG8pbQMtsFy8j1fkcjw1OmF0_U3jSOyMVQuGwh2-BWo1DGWN_m-RZ78NoUpyL7viph94sk3hyYclR1bOvK4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/90014" target="_blank">📅 10:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TA2Xn7DK7ZdcxlVS_7XGEZDdFD_UAYmLbqQJ6dV8gDHnD-QhjaJznd3OpMItcQjdrYrnabBr363JdaxGpyOmb0egjftCDd4z46fw_ELx6pyp8K6VC66-LgHGbrs_BLBZqWjdYCaDVmXRwB8oDhy6Chw3oILQoUjxyjMhLbmVv1X_FuLycVb595JEcVeD_lVo2rmqPLd99FXeA69uVOSim6oeUBlpiTTOLk8JUnPilYoAOQARTPTpLHUdRQTCkZ1gsE1jjYWWrFHsKjKSHDQpob-f6gsA0Yq_lweKfO5CduxYdFLombGnKpJ_gKSDjmNblSUdA1kDapH3pkT5Q0L16xk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TA2Xn7DK7ZdcxlVS_7XGEZDdFD_UAYmLbqQJ6dV8gDHnD-QhjaJznd3OpMItcQjdrYrnabBr363JdaxGpyOmb0egjftCDd4z46fw_ELx6pyp8K6VC66-LgHGbrs_BLBZqWjdYCaDVmXRwB8oDhy6Chw3oILQoUjxyjMhLbmVv1X_FuLycVb595JEcVeD_lVo2rmqPLd99FXeA69uVOSim6oeUBlpiTTOLk8JUnPilYoAOQARTPTpLHUdRQTCkZ1gsE1jjYWWrFHsKjKSHDQpob-f6gsA0Yq_lweKfO5CduxYdFLombGnKpJ_gKSDjmNblSUdA1kDapH3pkT5Q0L16xk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد رونالدو در بازی دیشب النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/90013" target="_blank">📅 09:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmqxsKN0OrW89yZPdG0Mf2Zzihz_yOByGFzijzLgJI1PedW9W-t7rGvNInTXPfUlWlUVdG0-pAs59evrY6m1fq8dwNfpTthdNgdh8ex_ORM2-RdbqBq3i3WCYrjOU0gWV4qTN3B1EcggdTTZSEIvSCdBk9dK3e6g5QEW3tpkej8rBu3O35PCQibUen7PSkDIT1tkfyRD4EdYkP7156PqwYZ-c54w34110eIYq1H9ZkLbs00xMuP2jiYuHlhrx66S44wTSPWC5bt4dUfNQcS0oDovuubuQa0S0UQ2t6sKpJUHbWFJ6EvEJ2t9W8_XLcnjqJKKkHmgyF9SxF7e_VkCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش رضا غندی‌پور به عدم دعوتش به اردو تیم ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/90012" target="_blank">📅 09:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90011">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/90011" target="_blank">📅 00:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90010">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pe9mXtifaCfpX9Q5HFIigm9SHRA7aktNBwgjg4OVMOJHbDO6gt8YVCaNMnNFb7ftG2KWnecgx4AWsxz3ozCn1TgtOlK0aVB51iNiXkA3CqMMRPCvdYc0w591YiC7jR_Tc-2o4PElVczK_ILcmk3KxaB2ISLSsAWE3ceY6aEK_h60okqRqfhYilsbqodPn5HptHwZioHxwrLFtP23_HC_x6WbscUsRZjGqVcQxkE8ubaVJVMXm092OCtCgkOl2pEV-2tW17g1glrPyYj_v6h1b96V2xm1up69xdDiEtx-m3UWgvuzMsy_97yKt_z8l2Y7KtmWlghGtzq3ORkOri53nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/90010" target="_blank">📅 00:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=DecDruLCGc-oYWeGedxT8o-OiJD19Zcc7wuK0M-UZvEXktUppWXbVhrM5Kq4FzwRsz4sV0GXdqRXoisK4qLloZEq5mg4kLsNIrXaYX2YswDmqsW7PGafC6UC7FEVAZwDzG43WyCdSFrcYlqfdmDDFeR3h7c9fqMDapTiOktL2VpwYisvwu62FFDPYO9NrsxTGLEN8KRv5BNhhjw-bl6UdooCLx4dlxv23c67hy7AiJVCKkqBKzWGBnNIru9vmswEu3_xq-euhXGbiS-Iu-1iIAEr8-9QOH5YseQKfyZGqRpUzSxzEr4HO_49ahsFtTGz_Bz-88nDs3GjiDaeo-8Qww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=DecDruLCGc-oYWeGedxT8o-OiJD19Zcc7wuK0M-UZvEXktUppWXbVhrM5Kq4FzwRsz4sV0GXdqRXoisK4qLloZEq5mg4kLsNIrXaYX2YswDmqsW7PGafC6UC7FEVAZwDzG43WyCdSFrcYlqfdmDDFeR3h7c9fqMDapTiOktL2VpwYisvwu62FFDPYO9NrsxTGLEN8KRv5BNhhjw-bl6UdooCLx4dlxv23c67hy7AiJVCKkqBKzWGBnNIru9vmswEu3_xq-euhXGbiS-Iu-1iIAEr8-9QOH5YseQKfyZGqRpUzSxzEr4HO_49ahsFtTGz_Bz-88nDs3GjiDaeo-8Qww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوضاع اصلا به نفع رونالدو پیش نمیره.
🙁
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/90009" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_byEavjJywDPIhWqQxB4uQU79-Y30MeC3bOfartCpeKOvJkTctejEL2knQk0e55lKPuWOVI9_PSMFRO4LzAZFUhrlK5QhsfBYjPcpFc_1Lnkpg_b9eGvUM-tu_8B1NAOCBocBnF-Yi0B3zCgcb1shoLvtEW4SDSfHAvwuJHPE_h92-L9F4lRKBSPifg9SY_K8B3SvgV2ecKuZkpAKk1X_mUWTULHZEKAojegBWY4TBEwDlpvdAX9yuCOuJ1Ss5Hmw9Jn2T64s-L9XbeNwgtM9ic9A_JI-KF44MYaOr2xXBIAPAHrx9ZDL1du9UwATTl92i0_cz2e_CnxkuIJqgXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
توییت‌جدید ترامپ: آرامش قبل از توفان
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/90008" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90007">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVdsdMiDuINCN0LTXLxTwIck27EZbaFeD1VFOxLjf87mWd2jzCln6jlR8OdOa5XGNRcuPO1iaS7bRHbaqfLVLY3NCGA8ZfHPCFpeCL5aPvlwzkTAni8JUJTZ6KFl_6uEm2Y71Med28dmY63PhQHYRGf2NpL-e-Nd5YbXTOgWEUHdPC1L731EuUomMIn-sUk_PWLJj5mgUThYWvqGkhYJcV8cA_iwEAbkTbbHpgmA4CjtQmVULUYpMvjXqvNePa1PfdDfdDuVt8qBO9vLnxGfIrlufS9C5_ssom-5C_0BrMCKS4U_bQLxP94DDOTu3DfK0Dm-ngT1AIjBlADl5bGeyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
النصر در فینال لیگ‌قهرمانان سطح دو آسیا مقابل گامبا‌اوزاکا شکست خورد و رونالدو بازهم نتونست با این تیم قهرمان بشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/90007" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThWbnQAvFT8IgoOmaD_PAbZI0Zzb7wLgaG6UGpX9P0FrP8Z4-cXIbTA_CeahYLmpqPAiu96tcH4LcmU77p-2dZzA1U8jd8L1T8T1EFNtQxM4K6IP089kQULhbzrWfg7SY7_MIKQXVjjo4jdPgOeIoDn8nMv11af5w4ArX_I7gkE9KjS0NfYFxM4pusZfXJRERGtbpfx1l6JsuCc8xXKCcdrKvhpnGr6hG5nsXbjjkw-4pbkZpuGqBT0S90r1nKl4LvRM35sq-ownSD3qS2AO_Kbk--cqb8hAwnrBVAnoGBhkl_hFPwbwi6MGQQRkFvWPfA4pGL-YDpIr_cVbBjZNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/90006" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💥
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قائدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/90005" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO355-8qjFZzt3mCMSDCdST4M571ZdHYPaJOnL0bW-MZkTOpRgupf77WVlARB1PgsO3XADqyjKf3i9nvQ0ZrvA4WeEZ3_oQMDFXK2KBC0V0wUP8etwWj0v6_UBjRFsQIbX5J_iSkNIRIe9PPKlGvTqxlrqUNFJHmsrwQE3swElg6PKegLjonhnpUiXjQoc70sjrFDidi3VDAyC36PJ32leR_nFRqQZpqWSGkNzJh95HeXPaRPRA9mLfhcAfB-SXDXnlLvtB_RkOyqh5B4Ww3ZPc_Xnz6UwdUQVJmEe0KJQKc-da7g26kBTDo6hkxBxjSvR6WcnU5aowtfvGY8nbdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/90004" target="_blank">📅 20:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAGvNNPrao7f0pTAsSkLMXVPOO2F7nGohM_H_QM3-Cen5-vYQZfLPLr-PZFJcjpFUJpu8CEs8qLOIFx1OfQ9GP47ad-2se5sSvMfW0V7AlTgFiM2H9EzXDEFH_R_Eu6CTX21FXwqMCto31oQuNPMGOcZ78SXTo0_IFlehmYaZOwwVbOxqwk9jEaLhI15fnU5JlKoxAwykK3aliLzl6iNQPGPB8n1GwP2GpI2G4Dx8iU5Nxf_kwI2Ruq5YcJqW_64Rqz-zLYHyFcCD4y-gyezSBE4b03UEfkz-IrdCGcwy8RSECGIpokNWguI9mluXqOxBDiW0USYQd-7juc0DeefbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پپ‌گواردیولا طی ۱۹ سال ۴۱ جام کسب کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/90003" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVgnnq7nwPDgAjXZ1WmswpV3PzHH8QMT7AraA2ZupLGLuwuNGsrknS0YBGj8WpO70m4GvoXgLMyPPNquxZpeseLX9alWWCuk1MV3LUSPI7uiHyfRI0sRMqREd01LaLJqsjEQPyBsG4IdNPIVzGS5g74fXwq-Zf4smO76vA65gkLd5aCdwbLQASMzmnoqanCF8VVLQfl6zJz3mC4jNI2ATYyGH4cT5AEMAIBNeeom-u1eOlz_s7Aoz2OaXLbIgj_kpyBksJV7EagnAsa66CWce3TFz_2MgREKYUQ-SVN3B4k9aRFDpHjk3izYVH-UlhPoTOruVw7V5CQPPO29wNVcEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منچسترسیتی با برتری مقابل چلسی قهرمان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/Futball180TV/90002" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90001">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90001" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/90001" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90000">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAtX-ejtZ9kYlJBxdCJPuNAfl8gmqZLyuoaG2DjMrnmbmdlJ6V5_b77i_fTDZQrWRqVIR96_2QWWIgFMT4Su7xG5FNpwpLZXhtk0IYCHBQP1TZgnSptiXOYplyB6g5ycv68jlN2hos61BwC8Yy90s3TGlpqdY1h9cmrrO3mo-gvTNngSTqnCotJXQDnVg7dmOIDteEpCAeo85A6KEA47jZD_IJMKqzKGFWpY0ILOYsaTc-H2NVuo-twMT72WV38rr7fIEXu4ccrSd2NLG_aEHQ2H4x0bPk5NtQfuUZ8xNQB1EOHaeqoiaFkrNyrdGSI-8ALaUxhb_tdofNBnbQzE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی جذاب
🔵
پاریس سن ژرمن vs پاریس
🔴
را در 1XBET پیش‌بینی کنید
⚽️
فکر می‌کنید کدام تیم برنده می‌شود؟
👀
یا چند گول در بازی زده خواهد شد؟
💥
🔺
ضریب‌های بسیار بالا در میان سایت‌های معتبر بین‌المللی
📱
امکان تماشای زنده مسابقات مهم ورزشی در اپلیکیشن
⚽️
اسپانسر رسمی باشگاه‌های پاریس سن ژرمن و بارسلونا
اگر پیش‌بینی‌تان درست باشد، شانس برد بیشتر دارید
💰
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/90000" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocJiaKsw9pMKKE_gOI3p_1WMzM_k3ZkYG1tyL-QDuzKF64Db7DebVvP3TLVbCBtEV8ogq4M1kab6TRY5z6ypZ00cHmEK-XTHMK_G1QY9oruP_jJVVYnLfGO9Vl26W6_wkXLufcSf002xewSzaI1fl4RBl2sOoF8ZwXeiC8nVbM71QAUd0-18tVOCEggCcCaAjMbBL_KN7NmR8I3v_niyriPq8xwQDIx0nnPijfK26OwZN2m1p5nLLK5LlfbA5KPeCbEmUoYwJMt9CWAB2p344V2nsEzNs6WYd3hETAE7KsPx1ApIRZk11oDHFWYLJUdtwZxIdYvR5phxPbwLOJjlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام‌حذفی انگلیس؛ ترکیب سیتی و چلسی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/89999" target="_blank">📅 16:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT_NXZKQkWZyCK6wM-850e_SZsDIAz3Ik_KXbR86sE5ugC5Q_D3zyfr2LJgt_Qh2arEQuAKc0tV08hC79F3x2RrpT264uiHvabHyBYqal5BikRGRtFaLhlEJXC0bBETwS9GfT5FrwqOfXNVFRj6E6QqLLHdGcKyNp4uSYeCupwOPQChsORs8yp6x7PXYM6oNRFBLzALCHQNCjrbrABEjRQncB8xp30E79oUW4IQJoiWOm2Oss5A7bcumRs5L8Csx0TJMK7aHpxB1gQN_Kl9Mp8Q6vD2apwe16SmRhv2aO9a0KKXPeRpUBVxN9uHEA0LCzEiYuQ8Ae_DE0kTqqkXw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
فهرست نهایی تیم‌ملی کنگو برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/89998" target="_blank">📅 16:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWEjiXf_yvdxDpjcTUFmf0-IsRzYAvKzkinCzvPky6oTJ9fAUHdL7kw2eZwXM-FZWb3smJsGrOzdWHnaaN0qfHIKc3SIFHAK7Fq9SnpLD_xLC94nxTGSkA5EaxtJZ2oAmsiRgBxFL-Jt1JMHQ51EZyXx6bIx-2MofQl649DVfXPK40LdJXVx52blZ-hOmzb4CHoFH5GzPnm438Bj-TihJYYBea4NFNP8ghFCfQ8RaMgU9InzeVyqc8TspH-1vU6u4PrGN5GYWGVHaaDiC13Ikn28qWiY3TZjazM_DLd0i-S1jYqszW7bhXXEd0DSKJg-n9tro_RV8054lRsp_Z7UNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پپ‌گواردیولا: فصل بعد نیز سرمربی سیتی هستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89997" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=IMXgHhnchRZWySteeyaM6rPum2eEze6bTb2yBUvrYBshadfATQSzdCyMFoXhYk2xnVGvszjpYDPhvLpSKxLQgMcSsuTJW_dTd5iliYqB0qnlYke2aqghaHKADt_OTLvsyq9zJWrsnWGYLzL8NYmrB8-DA7xZM8P2VqoKGMSZL0xiYvIMRQHDx9tjdr1f-d0WuWWPDlwDEBZuriVZdJogy1A3wcTqduiZR3ns5SVaxsVK5faK_HvpWZg0-F9ck6aXJ6MZYZx9Oca-5uDkCzQJxj5MWDOfbbNQWLlOOaoIKk_eaUSmidft7Aef72JyHi_5Bi3veq2CoCeMVRdGNwmXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=IMXgHhnchRZWySteeyaM6rPum2eEze6bTb2yBUvrYBshadfATQSzdCyMFoXhYk2xnVGvszjpYDPhvLpSKxLQgMcSsuTJW_dTd5iliYqB0qnlYke2aqghaHKADt_OTLvsyq9zJWrsnWGYLzL8NYmrB8-DA7xZM8P2VqoKGMSZL0xiYvIMRQHDx9tjdr1f-d0WuWWPDlwDEBZuriVZdJogy1A3wcTqduiZR3ns5SVaxsVK5faK_HvpWZg0-F9ck6aXJ6MZYZx9Oca-5uDkCzQJxj5MWDOfbbNQWLlOOaoIKk_eaUSmidft7Aef72JyHi_5Bi3veq2CoCeMVRdGNwmXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📲
پست جدید لواندوفسکی:
بعد از چهار سال چالش‌برانگیز و سخت، وقت رفتنه. من با این احساس اینجا را ترک می‌کنم که ماموریتم کامل شده. چهار فصل و سه عنوان قهرمانی!
هرگز عشقی را که از همان روزهای اول از هواداران دریافت کردم فراموش نخواهم کرد. کاتالونیا خانه من است.
از همه کسانی که در این چهار سال فوق‌العاده ملاقات کردم متشکرم. یک تشکر ویژه از رئیس لاپورتا برای اینکه به من فرصت تجربه باورنکردنی‌ترین فصل دوران حرفه‌ای‌ام را داد.
بارسلونا به جایی که به آن تعلق دارد، برگشته است. ویسکا بارسا. ویسکا کاتالونیا
💙
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/89996" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPAZfJz6KLE_UY18GofYjUpchebAurYcIP0GSglOWmuErPJjnnbH6h4quLEO8Mb_myWXHinOeiuQMOIpbBWClXqWC2tno-oTfhiNwkZaZSXuOr2-FAHnSPsVZ1ZepDCJr0ZfddE1icAyQXpbrfG4UXlehlGUkP5hjfboN9d_QOfhpHrVSSkTWEt9rHTsYF8P-MLlK8HhPlMjnqX9ALGBuAMUJZF3JA6QlxXgsp4pcw7lX8N6_u8k7kX7lqrQz3-ywIB0sEbgkoc8td9_eDKu6Z1nxymJTXc64OoGz8wuXXYIAor-EaQadd8roKCHGdWtZhaNjFIymbtuO1BX8PZZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نت‌بلاکس اعلام کرد خاموشی دیجیتال در ایران وارد دوازدهمین هفته خود شده و اکنون به هفتاد و هشتمین روز رسیده است که در سطح جهانی بی‌سابقه به حساب می‌آید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89995" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89994">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89994" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89994" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89993">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfU3JwbHa0N6BzgvcX6kHNKQNCTaRwekjX2aglCZfzemU_CcfdZZJmBclGPJrv3jhvMEIET-BgFMSEWK13I34hxoif-5qQygrQ7NObn-GgZ_3V68R_qIui6RF-cCymOHpCZU6czQEHFwQcSa6g04GkcATD-To2MTGBLgnbaUvfD14bns5AwJwKLDPDwuVQMVBdmlHHA_lXgWPTCa7kUpzWm18juurRcvsvNTNO5YTACGree2Dek8bWlgikCf1L8A9Ak95hhfoSRNivLfGAwVM6ko-UEdo8DKrcX3jMu75FsRCqGtWwQo0ZnREE3gYESI2fzhlsYXllCcEb4mY1wYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89993" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89992">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZo7LRneKu7IzYbPJslBOuMN6xUoYHR_VMkQWexqrq12ybZJtM2kB9XsClAH38LrCuQyYtrfORvzVh7jW7hvlb_wANQ1fLo0r0U_4FIS4I_mi-DxXbBlWtG6eUMFaTk4eLiJvEZfIicr8RejlT_liL5TUv1MlD5dVlyqZan7RvU4t62NrhjTIUg1IRJljVjPv_T8HF2WCxFhb5o5m35q11HgfVAnzK8T3ghKfTmwBE7Hse6Ei9SaTF-tfF_k28BZWN1SjbaH3iijoV1-A1y_K6-fad7iNurFHbeSnqhTLa_tBb61edWs1OJgy8KY8J6nwfcT_Az-HJB6AZjWgk2h2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
تا اواسط هفته‌جاری انتقال ژوزه مورینیو به رئال‌مادرید رسمی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89992" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89991">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=gC_ESn49AvOOpi7tXUCUnWtmTFnjvh7EZaqDbw8r2IuU2hsTXCivXoVSOXGKiDIN-kzEwrwvr2T9p9BdFKd8OlUxGUGgbc73iTE1UVBYJ8LhBQtm7tddYcgFXN7ioYSgcQ9JA1embFDt0gxGZaXRhYZ50fpFDINy_yJXB6kt5Ah09aFFpixs6e0uoeegUl8HFUm2P8bRGfbYDT_2YeyUoO9PWEKYSoQ6tGtjFFaO0HbhqpkRnMeiqipJZTzfD8sKQMgURh9BW8-qjwRqwoCI3hH85VKjIBCqUyUyAXnsEtN76Ll_pBoharCnFJ3keoiPiJ2V2uvtN8irQG-AMwnYlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=gC_ESn49AvOOpi7tXUCUnWtmTFnjvh7EZaqDbw8r2IuU2hsTXCivXoVSOXGKiDIN-kzEwrwvr2T9p9BdFKd8OlUxGUGgbc73iTE1UVBYJ8LhBQtm7tddYcgFXN7ioYSgcQ9JA1embFDt0gxGZaXRhYZ50fpFDINy_yJXB6kt5Ah09aFFpixs6e0uoeegUl8HFUm2P8bRGfbYDT_2YeyUoO9PWEKYSoQ6tGtjFFaO0HbhqpkRnMeiqipJZTzfD8sKQMgURh9BW8-qjwRqwoCI3hH85VKjIBCqUyUyAXnsEtN76Ll_pBoharCnFJ3keoiPiJ2V2uvtN8irQG-AMwnYlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آموزش‌مسلح کردن اسلحه و شلیک در آنتن‌زنده!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/Futball180TV/89991" target="_blank">📅 12:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp3Za17zyy6pgiqq66BqwzNwcgRAAIQuRTJ7sIyoxYg6mLey2H1dS8Ohp9EJJr5lphAgZo-TWlL_8fk_KbIvVtYQArtGnxPfhloLqJ40lIvtZ_c3EMH4F173Ud3GkWyzb6eULTWkYME8VN6MLwbnWVYoy4_g4yWizyAUuwRZYiCAYFnhx8PgudbiPiyrGigUGyiXlZieTSTDPyk2hpT5VFE4PTo9b3JafYEuX-8Fu_UvLcg0z6n2jf7yA8-Vt14Nmb01jzFf2vFORlGmHiWdv1XSNAYvY_8G4B-hmO_O92C9LsnAQGctgVleTAcmEbRJD4N3FykqYb0-wvpIIu9TiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هانسی‌فلیک با ماندن رشفورد موافقت کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/89990" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU4IYQB4CBvUMegqMEBhUNiWkfgK8ACb_gA024Gz8exN5p2qiXsPdkLxfGY4x0jFs80R0RwtFbhSyG-A_NIMLQc4KWx5FXzKZWqu6exff_P-4Z41mFglB_FDu_jp6Ea91DJ-YId52tfRPg9ktAyXrDd94kQQoNTZWvoQWAMhpJHWrLZ8DEWln171-8qEw-7FGI6DBFiS1_qgfHmuezuiOyg_Aai1Hs366kwEKOUt0dMZEPcFouq-qQsLjFwbLA8PuHRwOgq8g59wSkzsxbWpolF5ALj7OnBhS6QH9f3y9cGtf-v9fglSt1UUmNrFI_ZdoJqDawQOqtT-TH-RLhs3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
لیست کره‌جنوبی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/89989" target="_blank">📅 11:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwF4fwNDEhqGJsVMGN27yOKhG3u4rVSeVb-B3xz3ZTfQ-wUg0AyO1Jj08LGHqifreWKdONVClENNqPjl8i9zZCTtDkkx53P0_K_lM71HQsBNUx7FNOSpdSqtACIC37dh8RoXRASQucoYYOtb3BYLqD5da2nlFRIZzQPMiJYDqWaJROxEvLWz6DqPszvCfpJSbQK6o8CmuxOujkCyXx6AGPMD0vZ0qGq6dIMICgUq5xyp3TmEFE_p0fn9IGl2nKlc8cH_H1Xr3gGnc-sBD9sHfH_xpQAcGcR72sILEakcfzTFsGpSPc70NcgwD3cOa-tUGElrAJK2rzvVkY5Cs_od2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شدهش رو به آمریکا منتقل کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89988" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فوت پدرم باعث شد از آلمان برگردم/ کخ سخت‌ترین دوره فوتبالم را رقم زد
مهدی پاشازاده، پیشکسوت باشگاه استقلال: در اوج بودم اما به دلیل مصدومیت‌های پیاپی‌ای که داشتم، وقتی خواستم به استقلال برگردم، آقای کُخ گفت که باید تست بدهی و این برایم خیلی سخت بود.
به ترکیب استقلال برگشتم اما دوباره با دو بار پارگی رباط صلیبی لژیونر شدم.
کخ مربی بادانشی بود اما اطرافیانش خوب چیده نشده بودند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/89987" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromADS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM2RYU-raakBZbvWA-LB0g_oqWHsoGV3UHrB4da0SCQ26FYXK-XyxTMGz9DtIAjX6UARTibAPIiAbBOh5-FW-Ycc6QDgmpUu0TARENjEBKCWYfk1wafrSe2ND5rlp10Sq8u8ug1VUnsBJQNAvSP4R8b0_6Fpg3SWkAHEBOXTH9E-y67sRnlF0Ik18MLvxU6ZZHeZ9gj8eCxrCR258bhU6X3gAXd3ytgbE4DeZ2vQPhK5SMXJLzSBbxAdUf-diL2j7DvUkhHoZkmyPVkFUXDZccbMMWGhMg0pMNpEF0TL2wcZAi_8D-apKLARkJvV7ry2Y89xCSRybiMNTOkw_r785g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
بونوس ویژه ثبت‌نام – ۵۰۰٬۰۰۰ تومان رایگان
💥
با ثبت‌نام در سایت، ۵۰۰٬۰۰۰ تومان بونوس رایگان دریافت کنید و شانس خود را امتحان کنید.
🔥
چگونه کار می‌کند؟
⬅️
ثبت‌نام کنید
⬅️
بونوس ۵۰۰٬۰۰۰ تومانی دریافت کنید
⬅️
شرط‌بندی کنید و بونوس را به موجودی واقعی تبدیل کنید
🔥
وقتشه بازی رو یه جور دیگه ببینی
⚽️
پوشش کامل مسابقات ورزشی
📊
پیش‌بینی با بهترین ضرایب
⚡️
تجربه سریع و حرفه‌ای
😀
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
A24
😀
کانال تلگرام:
🔴
@winro_io
😀
هدیه خود را با ثبت نام در سایت دریافت کنید:
🔴
Winro.io
سایت اصلی در روزهای آینده بازگشایی خواهد شد
✅</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/89986" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCxIQ-YZSngno6DT3i4VcC3Fn69iYiwkOmBNwbLFOvyYJytyqI3RvxSa-BdQuEh2WHrg1nVLtA8SKoaWYZ11t9999BqeN2r7JGVNi3r0d6RbFuuzcth2aDtFFD02tTzaIadz7apDHGmjfAzgLgp9DtsqtJ8AFx_Dny-s8tBm61XfP0yx8Y8F6ugWq4pywkIkspF5vC05v1Xo5q45fCqhbCdrAH2o1pUytBjlQ-2pflSKmvVgUs7c_zt-RDPrg1CsRdCl80DE98gAyPYwcnXMuhd7x5Hb87LcULL40WAv-NHTz4skvBkk1NnEpJ4t1wZbDXqXKX5ienH0mx1ILpPbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژوزه‌مورینیو اعلام کرده که پس از پایان دوران حضور در رئال از سرمربیگری خداحافظی می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/89985" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💥
🇹🇷
جشن‌ویژه باشگاه گالاتاسرای برای ایکاردی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/89984" target="_blank">📅 09:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDa3tLV3kg3hzk9yQ-0yOAx0sXZsld6T0XI2LV-WBX_uwZYR0NdlDRwdonSQLS1V7yWmzdNGw_qu3vcuqvEvQJx1If57PHYVcnKWise6oFJBbKaRhXoAvYDp9c8WWTgTfa2zopzWY-s2kVESx-al_AWwGzhbvv6jitEloMjqTO0x9rBkMH7AoG9PPE9SzPR7cw2-QzmLdbMYkMZ0DGvUDZ2_fmfQE4LnQe5qWryjDYkBOPcwHTfmVF2zRK4PgUAtbcwd3_FeJD8sRnrLT88l-UB6_J5RczDfyrIvl7FUDuQHCoAOx15v8t0FmuWGSGiYT8a_7AvXoxYergr4gvuLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک سرمربی فصل‌آینده تیم فوتبال منچستریونایتد خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89983" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89982" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ctVsrrGF145gBJ8sqp-GjcrbpEV1l1BFHYKFiGmUGMBlrhZc6boXjzQLMJyQbPPfWbO0KpfxkUBbM30G5rTrxQGQ-v6kt-LN2ARmTCmFmdfdiBcDSwRIVfYCkGztYuoNfwW6u2u-FfS0raE4jk2qQnQ_iSmOgOstfUOpQl5yNWukmC63_y2IyFw7D1VjbdI7V0ADG9RnO_BWRFmPOM5PVkVnZEBeCOOByNtlovm03hEID4tGDgEArtVxVSZdrZKu69QB38_TgCaUnSxDwxoYe_VmYRtbscrbSZelf4a8fIUjj8y2qVWocvLMKN0W_fGPvLI0wk9XyNxbJSl2RSULjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89981" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPzEsYZKDkL7V3FYbXSrVwcNdK5SAER9PaQOW8y6jCAbzMatzg9o6gY3-UBGXIdZw0VM0uzwVXjG_D445SbTheWqxJPG-ccg-DGWKwBj01y3xFz09NbnshKge6ejTqCl7KgUJSeDeOyzK4KPvI7yR1w9sw94fyIEckcjX5by3hFONmS7uyeXgURUI6RZFx8-qBSJAICA4iGzTPvLaG3MYxfgBAfZQsifDymNIQGgaI1CzHQPrhWdqyzreymR4s_jMucn0JjOn7S4T9rN3znLs_Cu_X71lyKjRwkWJHWVyYdv-KxYRGjzzajiYSnJ_bIHA6OFz6BVIbnLCwZ5T6SpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل لیورپول سهمیه لیگ‌قهرمانان اروپا را کسب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/Futball180TV/89980" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsXiOgD6Bi7-vRpVXJmj6_mqTX0NpN9874_zteHNAUABPqjKomMhchN-SEdXepjXIBcXufwCXN9_yerAKplIER4h4fHiX8Pau0FiLu-5Xsy5XCVmuW2ZyEyQLm_4ihlDTlhbjBXinTAZJtk9vYb7otXBK-_V_CUHxWcrgX4HotzFbwUrd4o1jggS30819V5IrOtITNqmwkI5TghT4bzj2E82pxIhw3-Loi9qvRh8P3FJBD7xMDAhsCy1pYbQ8spsLdcEYX5xdJaGfYsvcTYvy17uJPD_DAbHYkKg3XLn3qzkIwel-5cYIBaAje2G1ks4YU1iaWuQ4CzNQ52pQkW9Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89979" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
‼️
سازمان برنامه‌بودجه به دولت جمهوری اسلامی اعلام کرده که با وجود تورم شدید اخیر، منابع لازم برای افزایش رقم کالابرگ را ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89978" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx8ci981lBwNvp6npHcZOcKp2Z-ThN7ZHKJE_Jpp61ImI0F08EdfYTlvTgMZfzxew8z4h2od4sTKpPmIXb78WOCpO6QVat3PCkiCcscr1FZU11dby5gadp-162lr3TNHJQVYusChUrgi9sA7ZUmv3pr5g1OzlSGZd3xNGS29EbX58qce82bLDvknHVUP4BkmMvrS0DyKLJfoOhefbihm982Av6DnAV0zIT2i8r9eJdSt4uLhZJC8WBg8A2nh1P0c0_dXC-f-GAfnYGd1qr7zHgMAQYkgO0Ab3AdrOn96z4xVlsWcxmn0YswEpaYXmd1jNoafMu7YYcu6_oNovUuJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇱
تیم‌ملی لهستان از برگزاری دیدار تدارکاتی با تیم فوتبال جمهوری اسلامی انصراف داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/89977" target="_blank">📅 00:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtwR75CDun8nvXpPQ9J0nVLJ_hMW3xmdJmMxldSz6QhsTDkEerw9wfyxg5WTBuLpC_GYVfpySyL79zC1DMQ0Qe-NsouPBAFkHU6-zBSjaBYzHeVhoUdTlEbpzyZ7H18kN8ZFJbhO6PedeezcRYM5zEngu5kOi-qRTW-Co_LrHOfCRk92Ecc4F4B5-Nl-sUCnQ6mtMtneysE9JUbrEfk7n1RWhU6MtUBVo4IDLrGYzEy5uDyIa4ssVX70olN4mSGZt-g5IOx05WjHEjjLhfQoYdg9z0NpndpfykL_cTBBGEEvUf9uhx81Q_C0zGgBlKmmrJ960kNaB9QbjOfqkoZgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
لیست‌تیم‌ملی هائیتی برای جام‌جهانی با حضور داکنز نازون مهاجم تیم‌فوتبال استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/89976" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjogqOeqKCjpiRkI_Jrrxgb8fbiHHG4FPN4VgyBCwOr-TvGpTHshG9Ypdkdmuocmbksz8_AeVAudYgj03G1VCr8hH0JxR1y47Pkj5xsjxEtEZbCDfxBzAX27cy8yPnG-PSCl4O86kfAaLQclxxezuxFZutv0cnLdp_A116uZCcv_Js6cT1oa9fSBUngsTjnXI0TrUi-wKhIMdaHfqv32ZVpcxSpAMYSqIrLfFBOqoO3SyPqZxotS_rbO6Svq9_e5c3WZ3mjvEsWvqVWvuGLNcnUzkZcNQ26Cx_GUgS6_pRyGTCDHDpR9MsqNyi8MqV41pZz5HKNmEWEMk5CJJgDMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89975" target="_blank">📅 19:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89974" target="_blank">📅 19:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAD1PKOJsCiY8wCO7Oq21A1vQl8qg9niFxQjNR4kOUiHQ4Bi0IUPHh1PT65SYq9QjQp-Y98gaxmtr_DQ-Epln362e082F7QdUkA9MJr8hpwfEMuqprPKD-f0X2urMdaan2lspsrw3KGRBeDndOmjaR9Ol6a62E96SspLSNhXeaSVvd_sYkT4yf_GX8IrLezR6eThPPdZdkQk5fOd4f-CpKdfdvBQgg3HngmgN76Dz5jU-_alUb8ZWVDpxK5kqAoHZ0xmZgdAU4BiOcZu24YrnTfTMO8Dt1Lx_P7IjLHQpBP37S9xGlPFtl4AcBAzaZrI0ibSFofPxYir5CeWrQeFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/89973" target="_blank">📅 19:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArBqvK75u9pZYc_HRqgukfau-JH6VDtxnRxHKareDK5NadWuEe54-N-lYvgKgVpAhWhtYBv8Juy3ViWqECI-mut9qMRDEr6Ip6rK3T_5K4ZKZC1o8ck6O23PFGEAssgVJ10p_b6SftxZoQAn6lnrXTpVd0pU9qhs9JOjmRK0RRPORvC-AFgLs8wr5rSzYPXfD3FsV2OzybDka0AovTnLaumvnNtTBlhifzkfRyF-b2h6dlZE3QyR9yZQnkx37w_n1FNntdDj_OLkNa2zb8rEpdlWXx7gfQF6j_qNkat_bNkouPK-8y5N86OuCjmBuUI7Qyun7e4CipW4fNBP2l221Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
لیست‌تیم‌ملی ساحل‌عاج برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89972" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPbJ_paD-Sn1PaZRDzkjr1v-ABwdCFnXASNFwOjq1bcKCtQY3NN01x8wYi7FKxA2N6mVGnmdb7DGcFcizdN9mmU1q1Rdz5xx84-wW0PLhrNOFJZ1KYfJg7eH4wnm5ita854dA9RpE9ce4ReiviKKLCisPjDKaskGsBxi_Kz1NYHwcWQjelTWXg7lFcRt9mMhAxYYjD6JNBPe0HY8CF9OzlmhlEoJQ8X-SNmf441MqR-VM08VWV0Y8fL0WvQyhWBNi3noymv-ufhrOd0U_ad3Q6bj6CTL_umj_Oeh82S-IbY-UkSBUBQQQb7-LWVIY52blBG7R7t5sqZKg0o3bpFXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
اعلام‌ لیست نهایی بلژیک در جام‌جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/89971" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇺🇸
فوری/ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/89970" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxMzJTNzrCMs-jVTa69_zHmOMIi8AtsP4l5a8U_WrCfJgtMWMh6m-XS0BU2JAA6WKK68vpIZD3I6qTIIMF316Hmm08eWWlloLUX9w7OZgYDAGTJLmkNC9aItoQuejXMNwLTzQytBMVp86tHkT6kztsYBeVX6g25T6e2V_3sw3YtTApO1GdSZY0D4h7Xqd01AyQedAtfvVDdH02l6BwKXQQwzae6tb33aXMpm2zIWk0o7sS-NR5f3pVZCKjMqNd3eaJMakzT8IfoiIYzdsxjCrERMyGrVS2mVjaeYmlXJzXz099kEO105AdJVN9Z57UocGhQkAHqJsy-YxykrBaHQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای بهترین سرمربی فصل پرمیر لیگ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/89969" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89968" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZnOzyab8HBuOq1r2YPn_0fq3xtsec4sDUQZ0NI8dDkt4ssV765ZKRLH9dhtJPrszMqZUMrkWEWUFOBS5q2dx8sD4Cq-5YgWunf8ewHcd0coPSZEVosEEHlbfWTLYMEUfR3uT31IAaTFvh5akQTXJzWCSOpJAZgnElGJiWyPLZcJNqjzS28Yk5I1Q8Wr3q2Ukma7Q9q5AArZEHxrFPt8QywxU2lmZb9Qxyk02MxticvCqKu5k9AHyKWwMQPXc8-lB3AxNR775siC1YDXAYBmSSEZ2oeE4Wqfh2ypTHpRetC0zqw3DIJjvyRD3Q6lDBZXeCwbkoJcw5L7X165q9b-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89967" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBcVTKen_DMlTb5k48r9UL29UsPKfrP2fE2f5bJXhbHL29q9sMxx7uvU6WmjqNGDqSgSsBS6YOTOrSSSGXoOQWs5y3pCppPT9Nm8uVyy1N7NDE2Sptgx2V-7GshfiYCobVnRJ2gL8RyWLevKpgZTQVS7SEdLQv6GBy-i2IE1zHMr55t9k0hysUY80-DqttslvXtzGr0MCYpzYVxPEnh4fZc5DpWGtaQUCQSvIuYuESkbEXYQhZXJFhIcZcCTbY-yTpnV_C1PLjy2vUcbMc9efvcc3nAIZ8poIIfnOcAIu4Y8i95qCtjSwhafOaD_7uA-tiFHP1jzpOwWvSypWY1ZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇺
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/89966" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uenqbzjH_1gaGWjriEIywtuPV9aRBXG_ZgotrG1NXBPsFkDVzs_1keoBvR9qUsq6cVS0jflw5dTsl-43chE3HINjAcA4tdTsEozVO8k0UQdha8QgeeDYcjLlQytjc3IzAeXXAYdLrOs05TTfWEQbvBuTcLVrz_MHPoQ8AVyXLMGixFQQImTUtYQ1u69My_urCOQyHqYuFB0jqJb0F4K2z6yn409V--3dL0f64RlNBbHf_fe6uUSR9uRnesmrUt0HuERzy8yPZjSDOKDeUXcuD5mGnh31bAR_4UWZ-8VHgKOZVkrnwgr1QH7vI1CjkA8ZQbJ2LNHMKGAMWgjPFvKe_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
فهرست تیم‌ملی ژاپن برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/89965" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL_kfh_uakST-gmHQqI3MquwTbP5ewWzHjPiUV86W5ZEoZYoFfvTg47X3m2MxGOFz5KWBTJmXQ37yV4-js5ZTVMdOmi_LVhVo-4jeMRCrpAq4pyv06ZYzozPaBrq592Hcml3cQNj9ChO-pX0bjZ7jVygXj9d2M7DbhCBgk6xyldke2F67vw3UT9M13wIvVrWk0s70h2_7YrHATV9N7Cqm44JbGxqQ6BbtcuUInK7z4F6Me8yloQuBDOnCJp0JXbhePFAOUlFOlXDad1mXrZMJIWtipZdTVM14oGxFOtxXKG0oK75glq_jB5le2-Eahmg5qLck1-pLkP8cs-if55MXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
امباپه: سوت‌های اعتراضی علیه بازیکن مشهوری مثل‌من عادیه. آربلوآ بهم گفته که مهاجم چهارم تیمم هستی درحالی که همیشه آماده بازی کردن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/89964" target="_blank">📅 09:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
وزارت آموزش‌وپرورش: امتحانات پایه‌های هفتم تا دهم با نظر استانداران با توجه به شرایط هر استان به صورت حضوری یا مجازی برگزار خواهد شد
امتحانات پایه‌یازدهم و دوازدهم تا تیرماه برگزار نخواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/89963" target="_blank">📅 09:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5She-PlG5zWW-HzBvhgQLqYcYM8J6W_0SjPs4Bwlt7A1fnf_3T2oQBn-E1x9sRgRVjJdOyXzgrmtqe8DSAMILYoda4yHtqbAm62XN-oE9PIHE1qzSnvPnY5Iq-Be3q6EPphImZdcmT38xh0rWM1jWJfrLF2S320BZYSGTTWLJLuCmRdLOdWGnAceS8fJIzpWcUpweBxLxl7o7JmP2txDNWsVU6i6xxrn3yrui6dSaGDQOX5Jo4-XqhuRHzCxXaUzJBOoEpFCOEiCbc4fTtiMhX0rP_sHsJJlFBV4TfKiDLyaRZzc1QK6sGnAqRAEOVxc8wUnzbr8EJX7Yj-ZKcqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که بیشترین قهرمانی در رقابت‌های لیگ در ۵ لیگ برتر اروپایی را بدست آورده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/89962" target="_blank">📅 09:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=rLaZb8JsgCmnegx3M5X31n8C5HFnbC2VLfeBC1K8icOpNX9nonYI6JmYlwlyWPXcv_BKRCJGt-8R-7hMpcsJ1iEhHQIXIHfbQWrTiLxq7OfldtQBivzDK5WM3h6yLEzGKaJ4fRONmS1MzXXz1E4aNecj0BmZDDS2cCaKQjzPGP0p-hNjLmqnJSNTYmWdnE4cDOnmyyBbPECN-krIJTuAjojWiNTBDcxlXYZJUwSi4tvAPy_21H81O3pkVrNZSg99Fke2ACyIXr1tp7Q4lVYQlwcyb01VbOqNU36A3f2r9qpMeaPqq-Ci371yuurQXC1h-rqUoHpNdSe2PE29HT2QbI9foYodUMA5bTX54J7bbKOrmzmmdF65EZphB6pBhdFbFqfCZAfkC0KyW20tuyValPq1Xp4RaOnqhu9fXvhmIX1wFEnWXGog5zZJhnjmn7jC9xrMot9Hncz0WBesVjj4VESvrVHBPqcXe8ONbNlL61LMGow68k7t33doXZ-AelphvzeELnR6Dyw-zV-9yy1k2t7PWQKzQGIUOTlZBsEC8IsCtMcrfnQD1zEdZuVR11NO41fkBDfDCeM5Jv_K9GARu-2Tw0vHESvPQy6TdtCpE9g8D9rjH0sJ_CZ7eFDQLcHd24ONfwuns4C5QuZ5-jjK2fhwuXsTlr1DmZG2ERwIkiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=rLaZb8JsgCmnegx3M5X31n8C5HFnbC2VLfeBC1K8icOpNX9nonYI6JmYlwlyWPXcv_BKRCJGt-8R-7hMpcsJ1iEhHQIXIHfbQWrTiLxq7OfldtQBivzDK5WM3h6yLEzGKaJ4fRONmS1MzXXz1E4aNecj0BmZDDS2cCaKQjzPGP0p-hNjLmqnJSNTYmWdnE4cDOnmyyBbPECN-krIJTuAjojWiNTBDcxlXYZJUwSi4tvAPy_21H81O3pkVrNZSg99Fke2ACyIXr1tp7Q4lVYQlwcyb01VbOqNU36A3f2r9qpMeaPqq-Ci371yuurQXC1h-rqUoHpNdSe2PE29HT2QbI9foYodUMA5bTX54J7bbKOrmzmmdF65EZphB6pBhdFbFqfCZAfkC0KyW20tuyValPq1Xp4RaOnqhu9fXvhmIX1wFEnWXGog5zZJhnjmn7jC9xrMot9Hncz0WBesVjj4VESvrVHBPqcXe8ONbNlL61LMGow68k7t33doXZ-AelphvzeELnR6Dyw-zV-9yy1k2t7PWQKzQGIUOTlZBsEC8IsCtMcrfnQD1zEdZuVR11NO41fkBDfDCeM5Jv_K9GARu-2Tw0vHESvPQy6TdtCpE9g8D9rjH0sJ_CZ7eFDQLcHd24ONfwuns4C5QuZ5-jjK2fhwuXsTlr1DmZG2ERwIkiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltzK4VbRzjnKVy2poGVHMphLR8towjURJRl1VQkTbbYeYZHYKQqcjII6N0UVGAPlIdkngPMkQdYHx3pCKihIs3udLlxx_XmuZM_hL_oMjfDlk6ATszeNyKvoMcb5UuaMGaHueTST5lGQlFja2bJy6TRsSfDE2E33RtJ-xhF03EhEQdwWwzzqjv0t3agVcvxv9nLrzt3RB91sr8LigOcuBzWmR7VRNyuR7U8RjNUMwwZunCb-grabMAWzsui3nI5gsXlD38Ldk2UeWgHJq7Gjc8mq4nz73_ImC2VNxvWqHCVuXfFo6JGk2VR62mt5iIzOSUR_QwFnL_xpy7-BLMiP7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6k_TrMZJ8klD4XGsKNY-_i6BX5pyzpnGTDY9kHx5ai18T8T5XDNgLhP4dp5qesRnTis-wxk-Q42vkVrnXtsxH3mtHVzR-MW4wFod7a4pi2NHCsbvT_Vfl-Da5FZNn-E2Y6tR1tLUVG1ERddbKEc5XLPh84wjiROZXNgXH5Xc6Xg91BGclbwt0nVCIgpOAnbcnEwzP7mv0gV5J81ZbnoL4p4F-9LV7lfbNcvDRzPgkFtU8gSQVvI9aXySvBYDcXYCLlShn8ADe-qsicklhAZkyAX_c3uBq7bDjwnxRR_HJDPZrs2ee4awo_NpEZEv10tNy0lemScbrOR5ByfDAzMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=AV_A3V-8Nld6bx9UMru-RcosH9Rn_w4rTi_MQBUG0-8ryKghVQMr0XVZBWecit6UVooUJ1BdXGgeTZbJCDGdBe3iuQT7EV6xGtLZ_xVUxfJkhkx1oR3vUI9-iyJVG4DOu2iC_ohpWYjLku3QHIzKur4gbQLr4cXsl5-XAQBv0YlDTd0aG8WeqczWIJ2-m_xhAXVeDCrMZ07Js_iPEfm7wjSNDTWdceLSVkB4z8lqLJuet2LRmOnzGymVtbnysq_M5Dv3Kqn44KzYS8hyMTi732EIwYrZ3PB0BqGdQSqGVJaTdbBB1FB6ncEp6Mvbl-gTJubQV0uP9o-vwzkNE-AtrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=AV_A3V-8Nld6bx9UMru-RcosH9Rn_w4rTi_MQBUG0-8ryKghVQMr0XVZBWecit6UVooUJ1BdXGgeTZbJCDGdBe3iuQT7EV6xGtLZ_xVUxfJkhkx1oR3vUI9-iyJVG4DOu2iC_ohpWYjLku3QHIzKur4gbQLr4cXsl5-XAQBv0YlDTd0aG8WeqczWIJ2-m_xhAXVeDCrMZ07Js_iPEfm7wjSNDTWdceLSVkB4z8lqLJuet2LRmOnzGymVtbnysq_M5Dv3Kqn44KzYS8hyMTi732EIwYrZ3PB0BqGdQSqGVJaTdbBB1FB6ncEp6Mvbl-gTJubQV0uP9o-vwzkNE-AtrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEvqV-VxMKscoisb9O28fSEP4d6yEwLL0LrxzVPFvmT0CtJnyUvlDLs_Lmmvp-1YkYmYjt_6p8c9-mg26_wgGqAmZdIvLFC3vROkhwyrG9H2mZK6rHjDT2X7msZxcCoVS-K-u_8jXJvI0mQGev2kIHdwIE18Tj4T1fyx-NHuofRbL4T5LVvZcnrYr-tVrTTnGm9EhUnCM5tfDOXv4JgxiR6gBX6Y2VBBeYOMMGGoP82K3OBwoPGp_FwuC8-bXerXd_phFHXsjOh7BdtvbBmEvJQBTD4N6-0z_lq0OV59e3lnpOsSfaDvmKPlN5KDPz23xsMspnoYpyx4E9OPUIVQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVn8mTLERHqmcpF729M1zPahhWLHNk9LzLSusc2_S9YqBdm-zVxMk25oZZU6Mg-3JfwjXkxCSiHr6KY8GbCLk_xcXuVUPNLQfbRicBI90Jh7kxonD8nLYWxQYkXr-Fq2NWJsq0wpIJPNsGoS4mnbMwSkJkoddaCJVj6MMz64cgsfGF0DlYaYvB-0Eo3cQ_GAbtUF8mVZObqIb4etrDjxljh7LmN-N651z5FG-NhrXtHMVHBRoerBEY2kO73EY4LgUntaBUnPGnYO2-BYqrEs39kVrAVtKWDAw21KTN2Np_t7LN8xkKppbKxCp7FkCN9HNtHN0gLYQYiKyTHlww-1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djq64NQ3F59IiSzUzgO-JAzBu_Hd3hkWSnd0WQ42oP5hBP7Jcf6s7P6tKyYPIKfbl3Yx2IkIAWwryCSFx5QXtqvCfyIg5CJ2U6WYOe9v40QF0tUsI0akL-50eIgg7V8_wYiUVeRovDmINjaWDooftXCAGnBb7jfAvSxLjEUkEpRilj-dWbZSG8GvC-0o3Pt_PSKkQSy0VRRbbhXChx1gipbLyqkfXniGPDO9ntKL6FjCo2BaifXG1wrlH3xfd9SbSTloeMRTWaJ8TjjpyCZsDj-LjK27ViZric79Ui-jf6uF2ZA1CGXn-zJ6jl2MWIJbHzgY6Iqgs1MF5L-ZOn47mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn55OwemNTExPy5-pzLNVVCmY6870b7sLvI6B7czoAcJN4lFp71tvN1gPSgiZBGFjyEOcNbQYqRHrUi99qm1qxlYjrEnlegQ56bAXOR2jyLPxnz5ve3-Xm9-vvw2LRKf1cLZpE8xcpBMA89YzRK1zHrlderPslvzvNHWJf06NgFOibUH2dtivdYH82tIcHUIelrk9Go5wMCrM9cqmcMKfrxgr9RPV_4hOYwPJvFa8PpDNzlJUDyDN5UsS__VVYu_0PU8ak5_REx2BWziHmGlIebD-dCd9jMYCxfa3SCDOmak2TvivPyLsXZ5QlC9wWr652RC6-JF50SXxVyRx5-o-5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn55OwemNTExPy5-pzLNVVCmY6870b7sLvI6B7czoAcJN4lFp71tvN1gPSgiZBGFjyEOcNbQYqRHrUi99qm1qxlYjrEnlegQ56bAXOR2jyLPxnz5ve3-Xm9-vvw2LRKf1cLZpE8xcpBMA89YzRK1zHrlderPslvzvNHWJf06NgFOibUH2dtivdYH82tIcHUIelrk9Go5wMCrM9cqmcMKfrxgr9RPV_4hOYwPJvFa8PpDNzlJUDyDN5UsS__VVYu_0PU8ak5_REx2BWziHmGlIebD-dCd9jMYCxfa3SCDOmak2TvivPyLsXZ5QlC9wWr652RC6-JF50SXxVyRx5-o-5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebnmv8adMvekzrCDECfBU3F29se7XMZdUr9u4-WoGVnXdMH4mqAtA0mp8VEN_nvAUlTgSyqpC9vHm3hF2UQWzBRxC02LkLVybQcp7uMzCeqDwgGE_b-W1LXnc23DoM__DUSmEDl5ZMtnHb6dI2fuvCGGR9p5sWoNsUoHueQzXvIObIUwY6GjZ6wOuKXOg0ljYDEgzDPQQi-b-A5mTNNaiU2kbV6UaEh7W18UiofFAV5LUOM6qhkVyonelpZlLPZj0xYe7pSMn4n_0hPiNWFqWQouBn801L8xVwk0kQ_sqw8YjncZZTQixz4FVBCziNJXibWCyeFvnjul7vzNpVNJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=SKgxzM08Dzfly_GjC9T0qJxck2vokeVjGkhu6petRjgrY2UPJ3i6HAqtAqGhtuobnhJPh400Wfiqp8pKt2SQWj_mkQZlKhnjWNyHIAnB2kzJzIP9kMaO-EiQ11BcsCI1hBmus1xvh9OlCD0ge2eXf-52YdSLC8tXhDADXAybwOuXYsx5NnfARF6dVT8arVGx-jJc3nJR7cEdBk4G7yfsKMkDU3YMUXAqyzDksTBDZDuW_7FOWvTaJxssfe26I4yzwpoBKtLNRkTQUAVSw0qeE8PeofC3h-iQhLh81sFCL_jkDzcw0DR36THgxy-W1lsdsHPXq79a8c5cxNQanpmlgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=SKgxzM08Dzfly_GjC9T0qJxck2vokeVjGkhu6petRjgrY2UPJ3i6HAqtAqGhtuobnhJPh400Wfiqp8pKt2SQWj_mkQZlKhnjWNyHIAnB2kzJzIP9kMaO-EiQ11BcsCI1hBmus1xvh9OlCD0ge2eXf-52YdSLC8tXhDADXAybwOuXYsx5NnfARF6dVT8arVGx-jJc3nJR7cEdBk4G7yfsKMkDU3YMUXAqyzDksTBDZDuW_7FOWvTaJxssfe26I4yzwpoBKtLNRkTQUAVSw0qeE8PeofC3h-iQhLh81sFCL_jkDzcw0DR36THgxy-W1lsdsHPXq79a8c5cxNQanpmlgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Squ_uUE6HIHvhsM1hHWT7Q9nPg5p0K0Ek-CfW2kS2k2SGaFOkeNKy5DGD7vDrq_wbs82Z0U4BjDWCNfTJaqiGRnJT0O9NPcs0TR1V_R7vyGJ7EE2gZfYuNqsCAJUg6WTi2JvkweEzeHH0jN_2kXntVb8AvolZdAvup5T5b47YbKoiBGV6m8ZIVF-OklLkBXUVjGxTgWp5pc6_Yodb5U8s5tncItJWW_-SgTpLJAm4_IjO01YNFpD_uxBo5BQ45Pg8Jl4KD4EN5lxYUWc_oow8q2koruA5UPHKngZ3euxIRfW-O1oV1g3nXLIdvpo0smNmVkCqv6kCdw5IhbAG1gm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pupgROc3oaOy4AQwAyXHiXSlns2v8H-6qMI23w6O0-f_FxzMw_lBIqVoguOaYDMhXITGen56aXBSqaXWnOgOTa-J9Yi_DHDxWwgPMcsA0MwHkl53dNdurbbAATXaTfPjwQ24xP6TiIkmvGZciOf5calo_YlIuURQJDvl0yaXEM7fQGornbdKCbe-_F_EAeZgteYT6xqqTzJKd8eNuHSc06KNPEOM3lKFR571wlgOuqLOX3NTs7DUUoOFcQl2YMAO0h-LPH1PLpFkDNxJ28QreVowUo0yx0IlrQR4g8FtGmtxGFXrT3fu8ya_zUPNLzRGQSu1MFadl6HKS31qEu6fNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqKCn3UfblgJh8U3wGeoxO9tXburj5E-GfF77F-Nm6bSvTEk3aBZ2zT21jgyDdSF7e9VMhiMoA1w4vPWPe_S9U4CxW9ZQk686A_-0Hx9b1KvfIOy_NyRmJRV400wRAN4ApzaksbFpPXUUoV76r-c1p6Qj0zuEgW_dJfwWvAVKjC5wBuX6V1he8MijBhhR4iHHLkGTc7nzXU8YCwS9qJbZuVrWdbheQybAaHmlXfSeYnjb2NYtw3cQbwjMxg1_x99Wu6UVmEMRO6henNOq1TPO-cCF9sieQ7lhoR5_BooC0YteGwlu4vff-l8xISQVdzmiuQjN529kS05VqR1VNwdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFk16wDpyzK33DmZvif-lr5wWIEoF-GDOO429bgz_ymE2bwUamSRmpvD6O_p3nZIQfbP6jcapqOdHzLpjWAA24zBHNVuhVJVfnrKkY_T3TJ2z-py7nSYLELaAeWmROzhLDgDGmj53QtxW0PfHxhCtXemfsBXuSShiSMJzSGTgNg07fbXHTvA19ppixkBl2DfDHd5mCuAUt_Ify4XNfdNKmux5BiEsqnJfmvLN-TLBpdXmnqLShQUehCMyTV8oWLFYJT4N8m1H8mZHClMohW7ML3BM7t4XJI_cHpHPkjLb54iu1Cj_2MarZhaZt25OfTc9t191grNUBsN-jCxvZ6nag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-aGyGQwdFA_djThqCXGRO-6UdtGXygCNvA4oP_pd7BkU3ik9hzsomPka7yTNsY8DdwwFU-ai4gDdNQ8l9ieYNSQyOVaJTAbvOnzQjOE-0hLUsg7-Cl0IDECXBz1jCCY_q-Tno3jjLx1fuzRy2zIeQGSrO8FyAoftufMALkQZ1U7-Y70G8P0Anyb2DIofL0U5VhumlJtq_OBpLr6bzJdRrcT50AigTA6WrgYyiSqUJFhmvlFlE08ZwzZY_W7GbNWCY8t42QeudGtMyksMLIx555ST6TJctWmaHzlzQ912tGg9dxRZGikbpdH7M6hipTLc6EMR83pWbnMAg9nf7iYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBc38oRjK790-m9_O2Gqesnl6aymLbZhQ4_8VrliaHRGwuLhRb25V975-tZTzpvt4dBPWtqnGv9acSOwAX-pm5KfIVK6yb3APSOAYe4lczyvoZzvASMgnLRMtlz95tK3fA9BMBK4rzta9VTq3Rz4bucXej1wYZ174qXZousBeqlEou68V14V-ofGKyYfWC5PapE7hF604fvph7S4wOXLdKzcZdrUPO_HtP8Puz3qWqkNkgIyVPWDJnqaH99imlLLTMfpX310hTsysP05kwaSw0902jW96wTGG9QF-OzWw4cVNrV9x0-3cMno1BOdpcIV3S90kwbzTc6ZQxeZnKNWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGjIoo0pu2pwe5aIUUpR2RaVRQ_anscNtJdfs_As53vLZYvRX6tuSPdhpW1z2l7Zp5xA1HTV0UBRMWTMi7kQmjuPTiBbizC6Kh7kRS_B5wv4jDhItBdRYOaWeXU4C71Cew67pF1jwwX0wELPRT-tPV8WQXgMhzWcDdxaA-Dq5f5kEedhYsAb3wQ8pBVW2aSSI564eWMk7mJN30XYpB6BvrvU-sJq3CsZv5JwYCRUWPfYoUE9vYv3r0pNXyEMvOLHlY_MtV91lWqyHGLV9AJUo5dckIUGezyXDGRYkQiirvmE_NYAqo6xT4qPUQs8JWLBIQgShvJ8dbLPmg5mRjrVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSwSTTWEttpRXknSK1qCoeABHkuR0u7g_aIQXck7b5sQEc-5EobuyeoxdWm7AqWuz30cPX11htMnVDgeqp3ctewgMyzgj6WMFfbkpHYQwdiTWX6T4oT_LZlmXBFLfC5-Tb4Ds-0FxOxZzY20hNp83o5ffFsBd6Mc20FdXV6e3VQ00o6dwVrjrmh_T5qaWp-0J5mcAnQnV_IAHS9ukzx3QXE3xaY1tm7z8aAvVNT1iBMAeFnj0h6eoCQa4mURCo2lder-nDDJ81rAtJVKHdb3FZYOpV2A49RwPHZ_4xPDS-4L5spqVR68__uFyVdoE5v79P1A4cPD59q44k4twepfCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXiwRkzSAhbL1CuIOapCPhzn_RI5H3OTWPJsVKn128RV2lY6yv-3Na4kCpzePJXdxfBIhIZvVUV_KcveiU-rkKdMYPHXMiducRw_Ll3qGJ8gGnZIgJ9h4wqpi6w2jRwB4BpMgfyXdL29OEAovOKEXm63yWF_dHT_JZon0hrZyT_uU70u0NG2Vxp5a2sdtCmQiTb4KtvRWjv6bzN_d3aySTDrAVrYslZgPzTjjCgQqwQLjlZ6pKGDbhRwcDQhWRCgsyq1Ai5gLRtk4y1TJ_vhECap5w1EDXv1KSMQ3q8bIGGK30leOE1BhwIFRGORg4PlX_E62AzTbKTEGOjG6b905Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ebzq8JZAJMStD8Mg_oX1gcm1OIzLBFz4W1TMtK2x84AVihZUfwa6GhM4V_1pq7iIoV8zJSXTN9fDW81UHNZs-J369647XvutKO9wQpDr93E0hjpCmWH7wPFxDB7ffnOmLVkk4BfqPsfb6_qXLlbbkcV94ZEnpciuocVoZCVKD1IHXc0n_lJlvdS2vkVZKRzau--9EHYF5m6mOUSg6BJwOlK7GrOwrg99gubaSpBOQoCb-RuJqYays5F0Z-9TAlAajsQzEEXC_bI9TPFnynx5kMFQpwwoDEpLH0Y7h-Y56jO-vctKLYvRZuuc-8SdkdkqZJjd3GkeN2lwmSuqFs38Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP77CoaOP0dVhDYzxiNUHutuNdPaoWVFQz8c8rPPJBN10wazhVMzs6_1cEIPToxnMW3cG_2POpGKE3GFckuI5O-pRIVnbntBw-UdmvF72qTyBNWxyLF0aTmhDJZS_xFaibsrUQ1_dXamRvQVTK7uHHZecgb20aDWFVst-FLgf3Z0NOToilTAweg4o4EHCK5ySVkJSwyYwXi2bKJROjj6L_70TgMcMHte4M0hCv4LqXemNClSZbMBko9bSmrkHFa7_HXWqQNV0P3sbZIlxlI1nae9EJXy1F-YqyxXwADGVFQVCamyVDei8wwpcZn-VlUIC5RbYajhVyzWsp9L_GYulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=gnUTlmFgWYnIu-tO1GH4G5otxnbjo_ji6gwXPYYthCDfBcD3oRT40ytI8bOG_So63QagVZwCrWKUUMtgeoGaasS-MOmhW66_z_Dr_0rtEwAcA6eaCFwiBul51YOtvhVCxL8WUE4Sh91SC-kJLuAceHFT_4cJVMmIVxeMlFZYP35F95mRW8u_L1fPjgItbW3UTcprBl1V_-X2EOB7EVJLvpbCx81Nop-CYOKtjSQjF0xF0a1Kd_c_HrNdtLoxscot54kM5MMjlJmerXLULXugfSkUDhhnBNM5bBxe-88Uli6nghbPqeIeP8k1fT3D9LWGLrhH6Uu4-vEWChqaqLosjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=gnUTlmFgWYnIu-tO1GH4G5otxnbjo_ji6gwXPYYthCDfBcD3oRT40ytI8bOG_So63QagVZwCrWKUUMtgeoGaasS-MOmhW66_z_Dr_0rtEwAcA6eaCFwiBul51YOtvhVCxL8WUE4Sh91SC-kJLuAceHFT_4cJVMmIVxeMlFZYP35F95mRW8u_L1fPjgItbW3UTcprBl1V_-X2EOB7EVJLvpbCx81Nop-CYOKtjSQjF0xF0a1Kd_c_HrNdtLoxscot54kM5MMjlJmerXLULXugfSkUDhhnBNM5bBxe-88Uli6nghbPqeIeP8k1fT3D9LWGLrhH6Uu4-vEWChqaqLosjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyta87u1lWMc78TlfRFTHRpT3HD4WobUssYePdEsX4m-65uygGDxUxwejRzfNADL0DxCoNXYZzQzgygIBqy8H-3HGTBvLpLU1t2GX0ehzgumIZwTIqZreAanNUF-z4oh5lzaqfoA-_GxuS53iTigFyhDfaMB97GbOCIV1c8CUIT163C-Yo-N8lbBnkmpHEgSBZK2xrAV91_Foh8azUECtEDJOKDPVUYkbHLh7j1LHsIw0rPq_g7WjrAs7hrlYC0XcxklWbLX9zJu9ef0K7nFCPajYkxoc1qUNtUTlTcmFmtHDIt1YMtSw7JvwLIxl2XxMsXtNTZDqRCvvY0ctK1PxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhtic0zd5s7kd-SuQGnMQNuJVJIggnFHoHO3MKXHLrdZRW5w0-a0wKIqEo9UFis9s6EQLtDb7DkXSS3Vzq7JfELDMEsTL9Uw2jlSMMbjaMvgn-RX-6USiY54E_S3F-OrMyGLvwKPz9CAvwtizD73zuhdiUsLo1dk-6qwFf30GkxRejG_NWi7mjU0vnxCMej0Azb9k1ocLrobzFW_HBKKY0JKX06pAF0MByDJ8pDr_jnckibqz5xB4zBDsOVLHc6UVZHb_TBpeit5dGkeij2GYL1ZyczIvfm-MY_bHWxQ84t1tXlWQsswyhZhQmrGghJi5YtcvQl6atMD_UGVAlPQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNdCU7s9tR4E4jVWUUPFgfVbAtQB4R58PHGRxdJDz7Qx7E7IhoPF_tOYupgYa5vU60_dCEt6Ipqppg6e0yBXqZVA4HusLKEqHbxEy-Vw0RRW3wtOjC3gOEKjb92Dy6dw57Bts_q3_u5VSQTqELyGcmPkE90AwX69F3bg7EKlLfnzHYrpIeKX-cheWadmr3Byx9x2b8BMhnZLNmyG-sod-cLGczaiNuLIKrwaMcfEGkWPbojAUFXqR_RPEjbqbzw3dfLxT3kKV4S5ypHJW8DYDG9B1poEtrqOcY8FTJ-Wgnpzao472XEnxU1pYqC0_bfZktFaggaL_aWt4Ec5HaH1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdRAxcHMMfV18YJ6UK9bhKpfX6rONPIElLG_qPcjux5O3N4Fcp0PkWNwPFIMIHZlZiUTRgltby0wnMc7dVcJo0gvtOUU8mKMlMc_xgVdmYYX4uyzMEdonSIMJCt34KIj_SRpUvJr_UWdu049_QOk4okhJe6n9X-SHBgadM4WtsahZbHyhLKPCC_-i5WvbTDMcKpOfzTCPvsAHhUQORVMjxsJvwhXwWLP-yUeCkGVXW4umLZJcEG7k2YnQOVBbrWnkoTW732Mz9QsTvFZAKlGfjtuE8SRrvYsS4IlF6oJsGiLi2d-KECZquWdc4ADzxQ5-X2BuSBeLBr4B3HxRUhALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIN7DzOQcKvcbfKpcz7Nm7iZYkO1UXmsbZi1k_1UT5Pt9On-BFD0QaRhgRDgOQ2aBoEZUfwGMDruSICN6ihBaD6Hq29T7u1jlcvLwcHcDj8mFlftq6drq3p0JajoAm_RpafzUSJNahmqx_oB_c1OctMDhM6N-8az1U5BW1DrT2aYMiBnGWndbUd1kAdU7NRReIDj-ZYzOxYaA-6BagHnADnHc4UmAJzpCeTL3i1MyDTptGZsNsH81K9KBYX8hc1kCM1Npw-gT6TX8m8FqZR3Ln32yRwOyqS0v-NB0DpTYkUHhWCpo5i1IKWN-HW0DH5vNsmgwPslTLZtMj_4ultNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J44rjApSJDCwyLKATIRHrjOZehn9X5-jgXTDFtM_rkQZDmx1aHjtk_zlsgbjYMfGjRkbnrFRurQ7eNW7_mVDsOPR4P7wKSIjzjDVHkS0fH11P20wswX16wW-CoOTn2xh7FzI8cnsc33zoSBEy39QEfy3riP2eySnk5iKapoxBrzObijEDYLKCIzpMrkSGnFi7FXVadjTAvQxoKRY7Ox8s4CrOSIiPvYth9wYLs3V56TSn5RlaFtqAap28gjvOP7u16z9pjact5V63zjyKR7JcnZCP6cxBo0uhEWbIrE0K8WRotdj9g4Zbo2TNErAY59kp3TA2dn-5rSY3e3uZOwGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAV1u_bCLEiz8L2JEzP4N0sBJqm8PufUX-6TyIaCO5ZKFjxE_mEa7DApla2qfonAXUmMQBoBJsDpRoYrtBsedQWUelm95_i22bLZPNmoR2yRP2xgY_9KRzuzeQezbHXe_-aJb4o1eBqw9-LyJ5RMh3T2wqPayJMsMz4J12KEeQrzn0nUmB6P3dVnAC2qBANLpVAnYE0mcEMwdi_gq0baTX6pKxLKW-1v_sH9Al8Gtw06TftrqDDjUnr3wzGmv-6-KpaLWaPSjd_b6u3iqedPDyVla_5j2WmkTLQOmlk0M1_sqcdzRI9lVhODBXKsi7uVnNpiCtYZ_7kzLJsYhUYYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
