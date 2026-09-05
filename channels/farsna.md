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
<img src="https://cdn4.telesco.pe/file/uh8VAOUqO5UZccEO-9qIfZHYBoTPfMYHN9NcoKX-gFSrGEYth1etg3a9Nldcg90u9Br0I3Suq_SCFeSONIgt7P6_QaVdP0JBKvN_iqjHRaA2Z6Wmo7tBlLAFWzn1F78cifs7UHCD_A74viOZeXKZZIuBxgbulqEhqlW_qpzUgJse9gyfckVmdMRpVSiZ8-7ubVhznpN0apkU7MNX483kRXnV2hbJzTd2sK-6637IA5GOn6wbpCCbGsV47ZzcZ6cZseONfOStlfTabdBdYG-k2J55qM7jw9L9tGtRZhHyKdLKL-ejCdLE-_UHHttJGySuaoE0FbDmHIy8Mp4GO6o_rQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-460277">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f0a87538.mp4?token=E4w2gXUNAcr8dsAA6k4R2lQbKQ3y5lF49pkyZpu9AAQ7IElX0ALC-y5exmnmQXT7VWoBkAlowKDVqXyKloHYUIwSvPi66Z5rXm9jY0yClGUQUH-MOWSx2_pfaIxpNhgMfWXaObNMApwmaUvwsrVbZTSnP5J-a6iAaWiCXuVfMoFIz8Ef4kk8nExrjI1LcSEMODq78-dyYPJCm107RY9Wusr3v07YB0hsoSbKTQMALMYjibVRkxbZHaQUzOon84FPm6R-gxo4t3fHv1jNE7Uurx9O2WXhW3on6LqAjd9fE27mQ9Q46BgZMXrl-jXm99tkUQG6uAbemkO6jBu2ElRY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f0a87538.mp4?token=E4w2gXUNAcr8dsAA6k4R2lQbKQ3y5lF49pkyZpu9AAQ7IElX0ALC-y5exmnmQXT7VWoBkAlowKDVqXyKloHYUIwSvPi66Z5rXm9jY0yClGUQUH-MOWSx2_pfaIxpNhgMfWXaObNMApwmaUvwsrVbZTSnP5J-a6iAaWiCXuVfMoFIz8Ef4kk8nExrjI1LcSEMODq78-dyYPJCm107RY9Wusr3v07YB0hsoSbKTQMALMYjibVRkxbZHaQUzOon84FPm6R-gxo4t3fHv1jNE7Uurx9O2WXhW3on6LqAjd9fE27mQ9Q46BgZMXrl-jXm99tkUQG6uAbemkO6jBu2ElRY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت ملی گاز: شدت مصرف انرژی در ایران از همهٔ کشورها بالاتر است
@Farsna</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/farsna/460277" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460276">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f302008996.mp4?token=BiFVazWIKyTKJeEoofRP0CwTh7ePUqpOHUT-3Jua50RemF-X8m_En9Mn7BwJ2FaZgr-kwQAv0lMYFr4aCMlTAyZ9cVFzEYwuyRiKo3hEwqG7PPfoaZ4u-30xT6ghZckFNrWSDWSuOqlWkt_6agWoeQneYvZbtxF5pE_ZKha_pPCzvEe6tIpPaSyUIC5kqkgnvT0Nhf1nXZIOObq8itD1FWCQFjdbbbx6DAFhQkJvxB3YTmPiUArs3AmotrLFf1pcHFztN9S5ItDKOppj0-8nQ5lZXA3bF68c9V2eVgXr_8Jsp8wwy2CaiRKGC2KOj5_Hm-6eFgCb8AJmecOdOpBxsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f302008996.mp4?token=BiFVazWIKyTKJeEoofRP0CwTh7ePUqpOHUT-3Jua50RemF-X8m_En9Mn7BwJ2FaZgr-kwQAv0lMYFr4aCMlTAyZ9cVFzEYwuyRiKo3hEwqG7PPfoaZ4u-30xT6ghZckFNrWSDWSuOqlWkt_6agWoeQneYvZbtxF5pE_ZKha_pPCzvEe6tIpPaSyUIC5kqkgnvT0Nhf1nXZIOObq8itD1FWCQFjdbbbx6DAFhQkJvxB3YTmPiUArs3AmotrLFf1pcHFztN9S5ItDKOppj0-8nQ5lZXA3bF68c9V2eVgXr_8Jsp8wwy2CaiRKGC2KOj5_Hm-6eFgCb8AJmecOdOpBxsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صنعت کفش با صدای زنگ مدارس رونق گرفت
@Farsna</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/farsna/460276" target="_blank">📅 14:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460275">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkFng0ORrwS5jXFp__WJLPnPe2BinabS0SSYqlDGoeVV2r2VISOz8kTN5FBulWIDVzxsAKeGKZny-5ClM2W5m2ZdwOGwZtic4Gohktx0QCS9jIBNH8skV2xEC29T0s2tZiAGwakJVs0tEAl61Xv68QcVq1T327FfSnFNYWL4Blc32JrU7c_3a7fUD8fKROiP_ZLYzcr2KgVU6BivlPmrUNEryM-6h1Z8Io8tuBqjDQbJZyZBv-1S1jcAC25QHk9--mfiy_QGOajNlGk8HLUp5AqAxymEnn9aJT889UUeFCcm4qcEKh86VhAmn1jFzDnqJfT3x8vkvSDU5PhRpFY9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد فروش محصول در هلدینگ خلیج‌فارس شکست
🔹
در شرایطی که سال گذشته کشور درگیر دو جنگ تحمیلی بود و صنعت پتروشیمی از این جنگ آسیب دید، بر اساس صورت مالی منتشر شده «فارس» در کدال، گروه صنایع پتروشیمی خلیج‌فارس توانست برای اولین‌بار میزان فروش محصول خود را به رقم بی‌سابقه ۹۳۱ هزار  و ۴۶۳ میلیارد تومان برساند.
🔹
این میزان فروش، حاکی از افزایش ۵۶.۴ درصد میزان فروش در سالی است که حدود دو ماه از آن صنعت پتروشیمی کاملاً متاثر از شرایط جنگی بود.
🔹
نکته قابل توجه این است که این افزایش فقط شامل رشد ریالی و دلاری فروش نبوده و تولید نیز علی‌رغم تمام مشکلات ناشی از جنگ در این گروه در سال ۱۴۰۴ نسبت به سال ۱۴۰۳، رشد داشت.</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/farsna/460275" target="_blank">📅 14:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460274">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duy1mMrC9WsCoAEPFehv62m-QQ6xSgiH-18MNHCVQz7W91mVDeEyrIhYs5s9jeUp9EGjvpjmyz5QcAfN0yZRLNG0lxi1p8djnOvMIo5GdeJw_2ftpFJrXQk3FVVQkdqVhbGW8giwBzcZLTN3TMbdj3wEd8_sDp43CdrRPUEqNwaFrMBT2rRuDiqUKUE0i2GZOpKFHCWJQjIfLTLgwDLzg82SU3_KbXpicqoUA7kdr7OZQXmmFTk3PgLQphf47z3iSha7irkISoszr_bmD0q5X5Q3tfSkgXnRqUxAQwvGgN6G7HQI9Im0_BMd3nDYGcsLQGidRBQqq7o0mVHVlIqPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
🔰
آدرس جدید دسترسی به سایت و پیشخوان مجازی بانک مهر ایران
🔹
آدرس‌های جدید سامانه‌های بانک قرض‌الحسنه مهر ایران به شرح زیر اعلام می‌شود:
🌐
سایت بانک مهر ایران
qmb724.ir
🌐
پیشخوان مجازی (مهر من)
my.qmb724.ir
🌐
چت بات
qbot.qmb724.ir
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 704 · <a href="https://t.me/farsna/460274" target="_blank">📅 14:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460273">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/farsna/460273" target="_blank">📅 14:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460272">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc3n_A3ra5eaYd2kbTR_8UBMRGgiNcc-_MIZiAhYg3dc5TJWhVYOp__0-JdbjOLDwpZkoLzvy9pTzS2D51rAYeZPrfFHtwbDoP5naETVkio6MzfBcklCj48stknfZ1jtKk0r3vXqTQpbFTFioewMBntHQ4YhJNF2tvk-97SLX5nl6bjJm1Ezkifo9MEfuNNVDlJU5Xp1Ym6jVGhqxaJjdotslE6QTbbsJdxFlXOEqbQZ2XzO4F8Xsin06QGPL_48UCC0XoXvTq6OeKVgGSGEpjCw_GW8dGhKz9bFAMZpdp7sKp-Xdu-AcrVpxxxIYGa9UdTql9j1DNqsfpazUSsgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم سنگین فدراسیون فوتبال علیه قایدی
🔹
با رأی کمیتۀ وضعیت فدراسیون فوتبال با توجه به شکایت علیرضا نیکومنش، مهدی قایدی به پرداخت ۱۸۰ هزار دلار بابت اصل خواسته و حدود ۵۵۰ میلیون تومان بابت هزینۀ دادرسی محکوم شد.
🔸
نیکومنش مدیربرنامۀ سابق قایدی است که گفته می‌شود واسطۀ انتقال او به شباب الاهلی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/460272" target="_blank">📅 14:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460271">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da34dd991f.mp4?token=lQnAlGGgYxDT3AIqmE-lZQJnmRA-cVQwckInuh8A1mUPVGZPyOwCYPAvt0qjP74nQjin15LOblCjCbqsKsRjDdXBvnM5e5xtiRz7ryFAEN7Us-HldVjeAODmUVLcNGI8r1Dyj5slF4OoQhAd_0NaDJ7tlxv9vmOtCuNNJ_DnW8Lvgf_LqEGd6LSbGHToS8WCcSEn1O5Vwx22N9vlQ1zNmoUylAQG8pjMadveMN87UM5eKiCTmOeLI5uKlbhXhheDGYxmCeKFaCKdMy3MVPT4XeukXEgA4zBpZ-pfxGsSTeET63FxOkbDhnMBJY8U9a_Yt2sqRh6IDXU36oYgpG91kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da34dd991f.mp4?token=lQnAlGGgYxDT3AIqmE-lZQJnmRA-cVQwckInuh8A1mUPVGZPyOwCYPAvt0qjP74nQjin15LOblCjCbqsKsRjDdXBvnM5e5xtiRz7ryFAEN7Us-HldVjeAODmUVLcNGI8r1Dyj5slF4OoQhAd_0NaDJ7tlxv9vmOtCuNNJ_DnW8Lvgf_LqEGd6LSbGHToS8WCcSEn1O5Vwx22N9vlQ1zNmoUylAQG8pjMadveMN87UM5eKiCTmOeLI5uKlbhXhheDGYxmCeKFaCKdMy3MVPT4XeukXEgA4zBpZ-pfxGsSTeET63FxOkbDhnMBJY8U9a_Yt2sqRh6IDXU36oYgpG91kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک جنگ و ۲ شکست ثمرهٔ ترامپ در تقابل با ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/460271" target="_blank">📅 14:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f08242582.mp4?token=unDHFTRI_WrkwBh9qKG4Z2I8h0EuMqE8KFvMMpiPmUMFwnRlFcnUODDBjkA-Grlu38_Mgbpggi2mq_bV7uqD77Z7MryyXW8VbGwm4u5Ikm58lqnnmZAaZKg7z8EUolUcF8aYdwE2SeDG28vKeEU2ZcPOijdY4SXtcHAP1v0GnWXW5aqAt340FUlWbolya1Am2OBcXUYwfM04EXlZfiCTfNjXayF0h1lA4HM0w3PH28Qa3ZTltx2Z4x_iHLARRUdGkXXCK5vOZW_XKjy0OD8yJ4hJegaamuJDFZFZIslVS_qVX52diCnwP2Kn5S87pQHB8e1kPDUK2U8CE5b5aq-O0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f08242582.mp4?token=unDHFTRI_WrkwBh9qKG4Z2I8h0EuMqE8KFvMMpiPmUMFwnRlFcnUODDBjkA-Grlu38_Mgbpggi2mq_bV7uqD77Z7MryyXW8VbGwm4u5Ikm58lqnnmZAaZKg7z8EUolUcF8aYdwE2SeDG28vKeEU2ZcPOijdY4SXtcHAP1v0GnWXW5aqAt340FUlWbolya1Am2OBcXUYwfM04EXlZfiCTfNjXayF0h1lA4HM0w3PH28Qa3ZTltx2Z4x_iHLARRUdGkXXCK5vOZW_XKjy0OD8yJ4hJegaamuJDFZFZIslVS_qVX52diCnwP2Kn5S87pQHB8e1kPDUK2U8CE5b5aq-O0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از گشت‌وگذار آهوهای میاندشت که قبلاً ندیده‌اید
🔹
روزی رسیدن جمعیت آهوهای میاندشت به ۲۰۰ رأس آرزوی محیط‌بانان بود، اما حالا بیش از ۳ هزار آهو در این پناهگاه زندگی می‌کنند.
🔸
پناهگاه حیات‌وحش میاندشت جاجرم در خراسان‌شمالی ۸۵ تا ۹۰ هزار هکتار وسعت دارد و بخش مهمی از حیات‌وحش آن را آهو تشکیل می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/460264" target="_blank">📅 14:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e70915585.mp4?token=b1G7oRG8mVMFcOKHCGykm4pQ0CZV_7hbSwAo0jUmg8xYa4Fr0JD9-U6m3TMtZwZmH94MUvvItEO9bQlx4Ch8bYKZRiI41nWt4JsGo8jqWS4aEG3MYsCXiBx1MNsy-Al6AzyEP0kZgTHe53oO7IFVWmbdGZQU3MhfXMUCtjT1hhJtVQGNEo5K4oD2PXJ76jlSGgFetnf_vQA085tFTYCHrlfgg_cm-nI3e1lr7a7VsRsfHzbpB_arHZXH3WZe74v1cPewoS4VdjGPp1att07G6mknzsrK9YvTQNFqnpuBN6-6dABeiQy1du8D4kAbQuyGKyHkNDHplp3fwnwWCkhgy62BWpwGpq2MW9StTfTfQaaJIMnQnQjHsSuEi7g5UaWR7hcUC6YRRHnjjBABqi72KKia-3q9x_5xGP_vwmasEfnqEGhqtHuA65SqJu-ZC5GM58OdA_C8wmdmVnJNSHExe9mpJKjD7BIi8B8beC4NuCIOKmn3qrKlB58n093iDE_h7XLdXdiZbLpKo1HT_sTB8LLNloJGQ1jVC8PmHc-PrsbY48jrAyTs-h9oKAc7C7BHEoUsal6fY74u-oau287gP5sPjH2lF-kPiBEWrmtL2KakwQhfNRfZWAM2ZsMs62lG4b3BgeujMFnA6satCwFEL3FsrI-cAolmXLDmFKdBydw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e70915585.mp4?token=b1G7oRG8mVMFcOKHCGykm4pQ0CZV_7hbSwAo0jUmg8xYa4Fr0JD9-U6m3TMtZwZmH94MUvvItEO9bQlx4Ch8bYKZRiI41nWt4JsGo8jqWS4aEG3MYsCXiBx1MNsy-Al6AzyEP0kZgTHe53oO7IFVWmbdGZQU3MhfXMUCtjT1hhJtVQGNEo5K4oD2PXJ76jlSGgFetnf_vQA085tFTYCHrlfgg_cm-nI3e1lr7a7VsRsfHzbpB_arHZXH3WZe74v1cPewoS4VdjGPp1att07G6mknzsrK9YvTQNFqnpuBN6-6dABeiQy1du8D4kAbQuyGKyHkNDHplp3fwnwWCkhgy62BWpwGpq2MW9StTfTfQaaJIMnQnQjHsSuEi7g5UaWR7hcUC6YRRHnjjBABqi72KKia-3q9x_5xGP_vwmasEfnqEGhqtHuA65SqJu-ZC5GM58OdA_C8wmdmVnJNSHExe9mpJKjD7BIi8B8beC4NuCIOKmn3qrKlB58n093iDE_h7XLdXdiZbLpKo1HT_sTB8LLNloJGQ1jVC8PmHc-PrsbY48jrAyTs-h9oKAc7C7BHEoUsal6fY74u-oau287gP5sPjH2lF-kPiBEWrmtL2KakwQhfNRfZWAM2ZsMs62lG4b3BgeujMFnA6satCwFEL3FsrI-cAolmXLDmFKdBydw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانی که امروز با ایستادگی این ملت به عزتمندی در جهان شهره شده است
@Farsna</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/460263" target="_blank">📅 14:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460262">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8-iUYZysNzOKqTcqi7g60x3cBQxK59ZaK9-GLuXxGvRC1V0FTycmagACIn5m0WilacV2e8jq6Q6f8cp6Au7FKAzEwd66w232yffdUvBKDdVWmFlmMYRRWQdWvsfHwwsT6h3H_yZkfsVyB1-vlNzzMXlVnIpGK44WMSWPxtTeJX9zWflt4vAcocpMROOhp0EY7MOXqb9J9cZ-YhYzk3Kx7U5PNSwKXIil71a1SCMt0TNwL--Atnzskx2ON-pAHYGRgJXVmSyRoo2WyAC5y1eDMcH_ypZndDJ1KQQHtEIQt7gpMpn8yZG8pS_KuqSxZscwOtJQpr7JumL23mlcWefNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب، صالح را نمی‌خواهد
کاپیتان استقلال از برنامه‌های سهراب خارج شد
🔹
‼️
بر اساس آخرين پیگیری‌ها، سرمربی استقلال درباره صالح حردانی از موضع خود کوتاه نیامده به نظر می‌رسد قید حضور حردانی در جمع شاگردانش را زده است.
⏺
سریالی از بی‌انضباطی‌های حردانی باعث شده تا در نهایت بختیاری‌زاده تصمیم به اخراج بازیکن ملی‌پوش خود بگیرد. از نظر سرمربی تیم، کاپیتان دوم آبی‌ها بعد از بازگشت از جام جهانی منزلت پیراهن استقلال را از یاد برده و دیگر بی‌انضباطی‌های او از سوی کادر فنی قابل‌تحمل نبوده.
⏺
حضورنیافتن در تمرین، نوع رفتار در مواجهه با دیگر اعضای تیم و تلاش برای دخالت‌های غیرمتعارف باعث شده تا بعد از ماجرای ضربه کاشته دقایق پایانی دربی، سهراب نام صالح حردانی را از لیست تیمش قلم بگیرد.
⏺
با این اوصاف صالح فعلاً به طور کامل از برنامه‌های فنی بختیاری‌زاده خارج شده و سرمربی استقلال معتقد است تا زمانی که او روی نیمکت تیم بنشیند، حردانی اجازه بازگشت به جمع آبی‌پوشان را ندارد و تا این لحظه هم از موضع خود عقب‌نشینی نکرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/460262" target="_blank">📅 14:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460261">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bbc47942.mp4?token=TFgvquIrSQvhj1zU_MYzENfk1-mq4Ypf9JXOceYIsiiGKi8FIMQqzbnPl5GyNtoL2qWvhMMi_RHRUFZYf_eUo-AOCtZEOiuBXSr4JT2q4At-Wo3WlryaLASp4xIB14DXM79KZKYPXaTTdcQ2Qa6LFVMKRT5H0RbGQ-lX5hB1xYIAT9xrUilCUrea280Qivlu6GKBO8Y1ErqwW-plBtpd_BNJ55q_9TX6jCL3PriZOvwB4vlJNPYO5yDAp5ldiRjg5kxs4REAOex4pZ6l279YJ9MrXE_xOal4T-M6C7ifed0CwZ18Kx3_kOJinJN-7KwxJhllf8pLf5yxH8IMYqSQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bbc47942.mp4?token=TFgvquIrSQvhj1zU_MYzENfk1-mq4Ypf9JXOceYIsiiGKi8FIMQqzbnPl5GyNtoL2qWvhMMi_RHRUFZYf_eUo-AOCtZEOiuBXSr4JT2q4At-Wo3WlryaLASp4xIB14DXM79KZKYPXaTTdcQ2Qa6LFVMKRT5H0RbGQ-lX5hB1xYIAT9xrUilCUrea280Qivlu6GKBO8Y1ErqwW-plBtpd_BNJ55q_9TX6jCL3PriZOvwB4vlJNPYO5yDAp5ldiRjg5kxs4REAOex4pZ6l279YJ9MrXE_xOal4T-M6C7ifed0CwZ18Kx3_kOJinJN-7KwxJhllf8pLf5yxH8IMYqSQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نباید از کسی عقب بمانیم
🔹
ان‌شاءالله خدا کمک کند تا راه حضرت ابراهیم را برویم و بت‌شکن باشیم.
🔹
یاد نگرفتیم با هم‌فکری به یکدیگر کمک کنیم، یاد گرفتیم دستور بدهیم و دیگران اطاعت کنند؛ اینجاست که کار خراب می‌شود.
🔹
وقتی جوان ما در خیابان مشکل دارد مقصر ما هستیم. ما نتوانستیم آنها را درست آموزش بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/460261" target="_blank">📅 13:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460260">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هلاکت ۲ تروریست در سیستان‌وبلوچستان
🔹
نیروی زمینی سپاه: یک تیم تروریستی وابسته به آمریکا و رژیم صهیونی که قصد انجام اقداماتی بر روی اهداف از پیش تعیین‌شده در سیستان‌وبلوچستان داشتند، مورد ضربهٔ قاطع قرار گرفتند که منجربه هلاکت ۲ نفر از آنها شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/460260" target="_blank">📅 13:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460259">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade139bc91.mp4?token=WSTgc4OIRzSuR5oBQFzSRqoEQeY0RdC2PeaURa9cv-1NnbxzW_9wICpGhK8-y3mVkU3mcxW5MQARZ04muFrP1y6tc9upjy2CpLg835TdI-YnBVW15j0rzF_c0e1NvEjg9lmSsiabBl3sHVyoBmfx-rcl6qsHboXb0qKVH9I2hD0Q33cZeTa9arzRiICJrmqhY29OdVKEgTC8eouaoQJukaPQcfRpth_vXArWUetKyYOLQ-SgyFNKqhBR4fVUwDWwH5ww9TAlOuxTMD0Y5YatWeHBzfuCJKX3wpE7RnDXqoeRFcBnq31dGw2kpfBUXCNLQyixc8n-1Ani6x5FegXSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade139bc91.mp4?token=WSTgc4OIRzSuR5oBQFzSRqoEQeY0RdC2PeaURa9cv-1NnbxzW_9wICpGhK8-y3mVkU3mcxW5MQARZ04muFrP1y6tc9upjy2CpLg835TdI-YnBVW15j0rzF_c0e1NvEjg9lmSsiabBl3sHVyoBmfx-rcl6qsHboXb0qKVH9I2hD0Q33cZeTa9arzRiICJrmqhY29OdVKEgTC8eouaoQJukaPQcfRpth_vXArWUetKyYOLQ-SgyFNKqhBR4fVUwDWwH5ww9TAlOuxTMD0Y5YatWeHBzfuCJKX3wpE7RnDXqoeRFcBnq31dGw2kpfBUXCNLQyixc8n-1Ani6x5FegXSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلار ۲۲۰ هزار تومانی از کجا آب می‌خورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/460259" target="_blank">📅 13:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460258">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXtlMQCtPoW9ppjKLa2nxd_9VNqFgoGe7k2yBbNzIHHCrMce4G2-efDds8MwpP07ga2Xgt0Ty3jwzFHx23IGvYiGB2ZK7oK1_HCO-vUAUtvl5m_kGCM58Fm1d2gJMtfCLQ_yF-DitF9xqt5ifYE2vWEB3maus7ksOmkqoGYMpV5NG4KljPbRaFZW5NtJRw27L-UprDw6qsXj83EQELfzjLTFq5J2UdwuoW0T-rAqUhA7BPKi6KrFtOKTCAxbhZO9F28xqTmFR9XJ2FJNbASvedXXXSXBzyTcHOrTGJ1kGkwCXu3swfTf8y40KN8nONp5LDIZONJ1oJOfprlUpkJMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول بازار سرمایه، رکوردها را جابجا کرد/ سود خالص «فارس» به بیش از ۱۸۷ هزار میلیارد تومان رسید
انتشار صورت‌های مالی هلدینگ خلیج فارس نشان می‌دهد که این شرکت در ۱۲ ماه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به تحقق سود بیش از ۱۸۷ هزار میلیاد تومانی شده است.
این رقم نشان دهنده جهش ۴۸ درصدی سود خالص «فارس» نسبت به مدت مشابه سال گذشته است. همین موضوع سبب شده تا سود خالص هر سهم این شرکت در دوره مدیرعاملی شریعتمداری از ۱.۰۲۰ ریال در دوره مشابه سال گذشته به ۱.۵۱۰ ریال برسد.
هلدینگ خلیج فارس همچنین موفق به ثبت درآمد عملیاتی بالغ بر ۱۱۲.۲ همت شده است.
این عملکرد درخشان فارس در سالی رقم خورد که کشور با ۲ جنگ تحمیلی مواجه شد و تعدادی از شرکت‌های تابعه هلدینگ خلیج فارس مورد هجوم و اصابت پرتابه‌های دشمن آمریکایی-صهیونی قرار گرفت.
عملکرد مدیرعامل، مدیران و کارکنان «فارس» در میانه ۲ جنگ و روزهای جنگی منجر به رشد ۱۸ درصدی درآمدهای حاصل از سود سهام شرکت‌های زیرمجموعه «فارس» شد و این درآمد به ۷۵.۴ هزار میلیارد تومان رسید.
این صورت‌های مالی نشان می‌دهد که رشد سود «فارس» متکی بر درآمدهای سرمایه‌گذاری این غول بازار سرمایه است.</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/460258" target="_blank">📅 13:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX_nh6ch3cqkiPwIxkP-NBU8k_NZQzfT56XX5laCC1WhPrjfQFm642Vd0rJVyWoM44aHnHWmXqEs91mTyIQYmWka8c4hMSGp0Qid3iyc1BYkMHBvYkKO7th-TvDhNkL1apfo9jEOr7EXu_w1K7Zq9Oakqdjp7oJAnE4BLOIMkXsAlI-__XwiEMjAV-N_agGPWSOlo1dcp4H68F_EcPo9vS3wtbipjHUDrEVLqpBIVk_lhGH99oQdNJz9T3Mt6sjSDOG7cIRlbq79FzKyluafiMXLq3ZEYX81WPOy_a1G5ERt-NUEV0BkwEpGt5hb0jSWeuXKg-UOJOAYf8-9xzOeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
خرید ۳۳هزار میلیارد ریالی شرکت ملی مس از تامین‌کنندگان بومی؛
🔰
تأمین اقلام و تجهیزات مس ایران از استان کرمان ۱۳۱درصد افزایش یافت
🔻
ارزش تأمین اقلام و تجهیزات مورد نیاز شرکت ملی صنایع مس ایران از تأمین‌کنندگان بومی استان کرمان در پنج‌ماهه نخست سال ۱۴۰۵ با رشد ۱۳۱درصدی نسبت به مدت مشابه سال گذشته، به بیش از ۳۳هزار میلیارد ریال رسید.
🔹
براساس گزارش مقایسه‌ای شرکت خدمات بازرگانی معادن و فلزات غیرآهنی ایران، ارزش خرید اقلام و تجهیزات مورد نیاز شرکت ملی مس از تأمین‌کنندگان استان کرمان در پنج‌ماهه نخست امسال به ۳۳هزار و ۱۹۹ میلیارد ریال رسید؛ این رقم در مدت مشابه سال گذشته ۱۴هزار و ۴۰۳ میلیارد ریال بود.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Tb
@mespress_ir</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/460257" target="_blank">📅 13:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/460256" target="_blank">📅 13:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460255">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a0985eb1.mp4?token=C0xRsJr1akAxyD5PPPEniAD-xkffXz3ejYNrxAOfFIAhy78BSjUY7VR7Uae69pChlU6JdgXAGcBTTSj-TY_W-xMyIe3hFhHljHfz7akY8fgzr2f3dBYVWzoWTDSHrcgZY5RIkau1aIoRKs7rVeHmpGGv8pHDQXAlffUXDJS8_Ke4BNb1Rba0h-Nb5b67P46ovMO4Dn-C6UEwHNE-V32cWmY6Ty2B27WRWQ_8nAninFqwT8LnE1w2WY-hTFIEg3RDP-mNGlAQnPH9k2wPvyEXtNa2M_2ZGslt3RyBWgJNkiPZplRFEJl71gr7o07uKbhIwWbp2ppz7mqPlurMm61NgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a0985eb1.mp4?token=C0xRsJr1akAxyD5PPPEniAD-xkffXz3ejYNrxAOfFIAhy78BSjUY7VR7Uae69pChlU6JdgXAGcBTTSj-TY_W-xMyIe3hFhHljHfz7akY8fgzr2f3dBYVWzoWTDSHrcgZY5RIkau1aIoRKs7rVeHmpGGv8pHDQXAlffUXDJS8_Ke4BNb1Rba0h-Nb5b67P46ovMO4Dn-C6UEwHNE-V32cWmY6Ty2B27WRWQ_8nAninFqwT8LnE1w2WY-hTFIEg3RDP-mNGlAQnPH9k2wPvyEXtNa2M_2ZGslt3RyBWgJNkiPZplRFEJl71gr7o07uKbhIwWbp2ppz7mqPlurMm61NgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: امروز ممکن است این صدا، صدای ایران باشد؛ اما فردا ممکن است صدای هر یک از کشور‌های حاضر در این سالن باشد
🔹
در سال‌های گذشته افغانستان، عراق و اخیراً ونزوئلا مورد تجاوز نظامی جنایتکارانه و غیرقانونی آمریکا قرار گرفتند و هزاران نفر از مردم غیرنظامی…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/460255" target="_blank">📅 12:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31bbe4143.mp4?token=IE9drkvIVRq2FsC92Nx2t3lP2_ZCbJkDa9Wtz5TW9qAS0nkt0Fad6sVaGM4zdVxfcZHOGpfHW75JStEXjokMyMa-gpO5QwLLD8SGRDtUMZch3aLUKCkgsBvw8ngfdB4Idc9QA-kBPOn-xqS_BR509Sn4JFFEwJIYEGZ8O0tHa9sihApcWzotVkoxsYNkv_7eTByDSlCbasAiSQ-miNjmWntyo8tajuEh4JAA6Mk6Oisn8eqgxCJqVhXcE5Nkr1AyKuatJrVI0mFInOghz4nOQDTY4Ted1nH8TpbO8cf0ROc6qUx3RimXHIguu4kQyWkBtfwm-tzl7vjBdL-7Hgqd8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31bbe4143.mp4?token=IE9drkvIVRq2FsC92Nx2t3lP2_ZCbJkDa9Wtz5TW9qAS0nkt0Fad6sVaGM4zdVxfcZHOGpfHW75JStEXjokMyMa-gpO5QwLLD8SGRDtUMZch3aLUKCkgsBvw8ngfdB4Idc9QA-kBPOn-xqS_BR509Sn4JFFEwJIYEGZ8O0tHa9sihApcWzotVkoxsYNkv_7eTByDSlCbasAiSQ-miNjmWntyo8tajuEh4JAA6Mk6Oisn8eqgxCJqVhXcE5Nkr1AyKuatJrVI0mFInOghz4nOQDTY4Ted1nH8TpbO8cf0ROc6qUx3RimXHIguu4kQyWkBtfwm-tzl7vjBdL-7Hgqd8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: اقدام آمریکا و رژیم اشغالگر قدس علیه ایران مصداق بارز جنایات جنگی است؛ اما متأسفانه شاهد بی‌اعتنایی سازمان‌های بین‌المللی به این جنایات هستیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/460254" target="_blank">📅 12:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460253">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlbWrbuzokGJpwYB5DKgiPR7VEdskqTEo_QhQ3Atev4vjOfKSnJCxvJFJr5dQb5VzGVYkAjH9bzOnrwHF4LbJbWSr6YkqDAEHsCArZhTzMCwQ0Bxd2v2lBk5qzSdPaXU6Wb76q5FjZg6x54mwOA0--rRsHK67TUEP0BFjHwcHjrOyWtuZAf2SekuwkyUeu2EARbvtqcaDyF6UPnveu0PBsmgGcbnPvdhJqkt_rKMpJHqdlDGgaKKv43GpgdfgQOPp5EB_9CdmVZM4S3Q0I35q6tWCxw7zjxj0jFfBXpGlLcsTVJOOPz2vXXdUVri7x7oX7IZFheYuSb2j773R4YpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به ۶ میلیون و ۶۰۰ هزار برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۷ هزار واحدی به ۶ میلیون و ۶۰۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/460253" target="_blank">📅 12:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460252">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3381f657.mp4?token=iFTPFsOWfE5VPGNnDP3UpMQ8_iVlB9N0eaQKZs0fB4BINxg5b9S_9cExHCmSPqCd0uCgYFxuVjfxcFH928t-IVPqeu3HExRWSuDAC6LyJarqfy3rlxPZ2y0ydOxpYYkJNFnG1cxNG0O_xLDPxaBH-zmXRwkPShKQk9H9UTTxsHkC53kl_OudlUIBMMrinPbf0i31diY5LXHCrqouzrIB4qRumOjX2-NrOGHYRsjBWkVg3VmOWDuxCDSzx3GV0HlZEwmkf2dU6TnXkCi8-tdPCLcNaWwFthcnNy5EbcYG4u22f-CNX_Hy5WQX8N1VtzQMUgySIFmvmGIJ9LkuPsW4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3381f657.mp4?token=iFTPFsOWfE5VPGNnDP3UpMQ8_iVlB9N0eaQKZs0fB4BINxg5b9S_9cExHCmSPqCd0uCgYFxuVjfxcFH928t-IVPqeu3HExRWSuDAC6LyJarqfy3rlxPZ2y0ydOxpYYkJNFnG1cxNG0O_xLDPxaBH-zmXRwkPShKQk9H9UTTxsHkC53kl_OudlUIBMMrinPbf0i31diY5LXHCrqouzrIB4qRumOjX2-NrOGHYRsjBWkVg3VmOWDuxCDSzx3GV0HlZEwmkf2dU6TnXkCi8-tdPCLcNaWwFthcnNy5EbcYG4u22f-CNX_Hy5WQX8N1VtzQMUgySIFmvmGIJ9LkuPsW4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: نظام‌های قضایی نباید نسبت به نقض حقوق بنیادین انسان‌ها، کشتار غیرنظامیان، آوارگی اجباری ملت‌ها، خسارات وارده به زیرساخت‌ها و بی‌کیفرمانی عاملان جنایات بین‌المللی بی‌تفاوت باشند.  @Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/460252" target="_blank">📅 12:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460251">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f55e58a6d.mp4?token=RhUBXg4yrfdysPzBufVMtzepNwhxvUV3kF6cnGRzty9nlxdoVfEzIn1bLLGZeAcRSjoKvwvpk7uatkYg9NnFeqrqIOrpb5hGsqXDwwebWLUPp04fFVvD3BZ3pPeBCtWtoORdZPoLoYoLqDrYu81s8S9a8RQ2Nxd7hxBNCiHIYMuIrywjFx6LYNapLy4IF4SRbcOxJJgeDwyAF-TkcK1DCxoQ6fCDJO_2H33xvKbV3DIHvSNTQbJj6zFMnYUiiQwuyvX6AFxKzYBEPHXLorpsoC0ii4oeKywz6Dzw4BzXYgd6Lvh9H4Ib-R2feMLumCEGmJCJKkxukqB7rjIOyZly5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f55e58a6d.mp4?token=RhUBXg4yrfdysPzBufVMtzepNwhxvUV3kF6cnGRzty9nlxdoVfEzIn1bLLGZeAcRSjoKvwvpk7uatkYg9NnFeqrqIOrpb5hGsqXDwwebWLUPp04fFVvD3BZ3pPeBCtWtoORdZPoLoYoLqDrYu81s8S9a8RQ2Nxd7hxBNCiHIYMuIrywjFx6LYNapLy4IF4SRbcOxJJgeDwyAF-TkcK1DCxoQ6fCDJO_2H33xvKbV3DIHvSNTQbJj6zFMnYUiiQwuyvX6AFxKzYBEPHXLorpsoC0ii4oeKywz6Dzw4BzXYgd6Lvh9H4Ib-R2feMLumCEGmJCJKkxukqB7rjIOyZly5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرستادگان ترامپ عازم مسکو و کی‌یف می‌شوند
🔹
استیو ویتکاف و جرد کوشنر در حالی قرار است فردا و پس‌فردا ابتدا به مسکو و سپس به کی‌یف سفر کنند که واشنگتن مدعی است برای ازسرگیری مذاکرات ۳ ‌جانبه میان روسیه، اوکراین و آمریکا تلاش می‌کند. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/460251" target="_blank">📅 12:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460250">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b9829fb4.mp4?token=G0CI6-F3jmTGVt11zPr28I41WUOpss6PmkTG4Bq0DIwHvSbNpvNaFXEYXXm9JsbO0T7LSToqICtSWbdCdQYtGN2dc5NcrHm7a2zkWKAOF6IuPs4q1eM6AxJYFoNLx-4GnTmWrU_mYnukenBzb8mup-Nh-RQpN_QnapTw8nU30NBkkavQaET5NICyehhXIzWOYEteZNSiL6q3g2MUihqr0nwN_HO-2sVg8xaBIjSuHIdQEmFGsty1dOAF3AADkmr0XMNWeI62B5m6uTm2hkahfLtuZQdj_vLxYHfje1vVGm_zDAe-PU60Ys1KeVQNbtPKq8CUay1DDnzORk1_TZqrmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b9829fb4.mp4?token=G0CI6-F3jmTGVt11zPr28I41WUOpss6PmkTG4Bq0DIwHvSbNpvNaFXEYXXm9JsbO0T7LSToqICtSWbdCdQYtGN2dc5NcrHm7a2zkWKAOF6IuPs4q1eM6AxJYFoNLx-4GnTmWrU_mYnukenBzb8mup-Nh-RQpN_QnapTw8nU30NBkkavQaET5NICyehhXIzWOYEteZNSiL6q3g2MUihqr0nwN_HO-2sVg8xaBIjSuHIdQEmFGsty1dOAF3AADkmr0XMNWeI62B5m6uTm2hkahfLtuZQdj_vLxYHfje1vVGm_zDAe-PU60Ys1KeVQNbtPKq8CUay1DDnzORk1_TZqrmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بریکس نقش فزاینده‌ای در شکل‌دهی به نظم نوین جهانی دارد؛ ما خواهان نظمی هستیم که در آن هیچ قدرتی خود را فراتر از قانون نداند.  @Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/460250" target="_blank">📅 12:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460249">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a846caea2.mp4?token=V9eGVCNey8q-VOK4fNFZgrGqUqW5F8TsjRpMCLF84eEyaSJuCBJwDzSLhIIdUZ5etPKcri134Ww6v_25pZBRmEGPmpftEFuOTDvtFmXdZLa6WvVZM5dBoPrO27Y6Uzktb74RhWmrouBI8OTgPW-zyUTHcYR5EitbhW4qo_rsqTrqa2Gl7urIrxwWzLTjJlupyW3M99T_82m_vensHHVgjNGOqVoB783vZmqumHY3-d2mop4rVuwOrqFQHf_iZVtfOUijemYkWapUKAB8j0tPtiu-C35pjCkbp394Htv1faSBGeu3RR-HO1OYHBcALSkBOs2_jZ3PYuOQEslMDFp82A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a846caea2.mp4?token=V9eGVCNey8q-VOK4fNFZgrGqUqW5F8TsjRpMCLF84eEyaSJuCBJwDzSLhIIdUZ5etPKcri134Ww6v_25pZBRmEGPmpftEFuOTDvtFmXdZLa6WvVZM5dBoPrO27Y6Uzktb74RhWmrouBI8OTgPW-zyUTHcYR5EitbhW4qo_rsqTrqa2Gl7urIrxwWzLTjJlupyW3M99T_82m_vensHHVgjNGOqVoB783vZmqumHY3-d2mop4rVuwOrqFQHf_iZVtfOUijemYkWapUKAB8j0tPtiu-C35pjCkbp394Htv1faSBGeu3RR-HO1OYHBcALSkBOs2_jZ3PYuOQEslMDFp82A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای در نشست بریکس: ملت ایران سال‌هاست هزینه سنگینی برای استقلال خود پرداخته است
🔹
رئیس قوه‌قضائیه در نشست رؤسای نظام‌های قضایی بریکس در هند: جهان امروز، در کنار پیشرفت‌های علمی و فناوری، شاهد گسترش تجاوز به حاکمیت کشورها، نقض گستردهٔ حقوق بشر و تحریم‌های…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/460249" target="_blank">📅 12:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460248">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdXN-B4poZIRJCcT6hGRTd__M9gZJL-ejBy7kXbyb4PULDQoCCsuv_KLPW5A4GjUs6SCK5_xPufBf8oPnUBXCvDgstuF7Sw-Ym1TzbW2KYC26O9ebvfRGRDR44hn5FWw-l5hpaiJvt87oqogL7pNU3H96lsdmOJKla714hPU3nUFi7fa6SfwRL9x3fJLcq3795vHWqRQ4MC_7ZjaVMgN-4FFVBWUnScpYx122vIL1K5a_V93eOus8s1RczU2zP6JB8zjCRst4a_hvEMhU-m856KC8gtAy5Ln0PmCSCB13Y1hI6teSoU3t6PhSN0oDo_VpFQ09szjTavH_2O-Ec9pWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف بیش‌از ۱۶۰۰ کیلوگرم مواد مخدر صنعتی در اصفهان
🔹
فرمانده انتظامی اصفهان: در ۵ ماه نخست امسال در یکی از عملیات‌های مهم، یک باند مسلح حمل مواد مخدر با کشف ۸۲۰ کیلوگرم مواد مخدر صنعتی متلاشی شد و در عملیات دیگری نیز ۸۱۸ کیلوگرم شیشه از یک باند حمل و ترانزیت مواد مخدر کشف شد.
🔹
در این مدت همچنین ‌۱۲۸۴ خرده‌فروش مواد مخدر دستگیر و ‌۱۱۵۹ معتاد متجاهر جمع‌آوری شدند.
🔹
۲۱۵۳ متهم جرائم اقتصادی نیز دستگیر و ۱۲۶۲ خودروی حامل کالای قاچاق توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/460248" target="_blank">📅 12:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460247">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYI5mbETuYZKKlszhg1lya8ztCqqAPbN9PxoaMzaiR3qwMcCDZo1yfTLqAdWNx2TTuRdG2prQFhMCgERV9jLUplAVc3nqmaGCQQ81xbA8qZ2JGYJ9ZYZ3lueeX4Nm8DQ6RNSHreC3lGcLddn00aZ07wbk0kzL3VmSSfWm-e8o6wpab6YfJ6QS147yN9zwaXKuduG1YvTermY5G9y__ESF5KUQlq5GnCVV3F3kh6Mbh8FuqYGhyHuJFf0Q5UftKW5mFgOvGNQol64HPY7G4E6t9WtYhErxX7etOW7pCcEZqyIpCdBrzYI6iJtNPmsSXUu2B2af_swof4UpdY-QT6QOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ حوالهٔ دلار به ۱۶۰ هزار تومان رسید
نرخ‌های جدید حوالهٔ ارز در مرکز مبادله به‌شرح زیر است:
🔹
دلار: ۱۶۰،۵۰۲ تومان
🔹
یورو: ۱۸۶،۴۸۲ تومان
🔹
درهم: ۴۳،۷۰۳ تومان
🔹
یوآن: ۲۳،۹۱۱ تومان
🔹
روبل: ۱،۸۵۳ تومان
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/460247" target="_blank">📅 12:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460246">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تکذیب حمله به تاسیسات هسته‌ای اصفهان
🔹
سپاه اصفهان: اخبار منتشرشده در فضای مجازی دربارهٔ حملهٔ آمریکا و رژیم صهیونیستی به مراکز و تأسیسات هسته‌ای اصفهان از اساس کذب است و چنین حمله‌ای صورت نگرفته است.
🔹
انتشار چنین مطالبی در شرایط حساس کنونی، نمونه‌ای از تلاش جریان‌های معاند برای ایجاد التهاب، تشویش افکار عمومی و برهم‌زدن آرامش روانی مردم است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/460246" target="_blank">📅 11:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460245">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go7CzTExUJqmGhZhg2HXxHTtEclxXIZIUuG0gAC_H_n5Q4bt1DAjpG9iIJSsSLXqGbohIzZeWlTR0idUxy1pf9I1Wnn_n3lJXB3PZ_4TyKNPKHRMabZ3R97oTzLIeH39v3YP1tOV7oci2pCm-4WXPNlix8v7byFdWn8QP7zpr4gCpQlFyKj0IVChKDXkpnaThSpPFpGM-RenS86zDsYFtc9U8Kl_K4SxGaZM0s5vPpYhfAtCwMmUirFjKwYfBohJ5Fcfiy6cRcvTswRx2cSWCrIcSGGizR37JMOqHPeFCdXJpQrvG9XMXFyxTdY7MDHAikXEHwh5-4qvJl1wcZ2l9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثبات استفادهٔ آمریکا از تسلیحات هدایت‌شوندهٔ دقیق در سیریک
🔹
دادگستری هرمزگان: پس‌از بررسی‌ قطعات تسلیحات به کاررفته در حملهٔ آمریکا به مراسم عروسی در کوهستک سیریک، مشخص شد که از تسلیحات هدایت‌شوندهٔ دقیق تولیدشده توسط کمپانی ریتون آمریکا استفاده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/460245" target="_blank">📅 11:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460244">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b899b4b38.mp4?token=J9bqyo8lg9wffOq1ic5WTDbQSDs8fpMBauFS0nAqKQyY7SUqQ-ZxvINuA3Lr_TUzd6tBVCL0x8OdgLvdPrME42T9iTsjmuoD8fmTQgNVaeUqzsWg6RT-NkGJgMkOBMhujb0tU3eq9CT28qZr1pA4QhvG3WbcrnydKpDqLwkoHSCXGh3lBYwhmB_lttmwKq04O-1R9XyOarvg3DVehJk5MYHyPGOjqfSV_EWwzdFtboBIPJJwHmiGKfzd1tN3lc7r7I5S6_nVVpeszXsJMQ9sL6m8qA3saG9P1Zdq_wjqUOphw85TbTNCDfKDOF8eA69pv3lna20NMNUQnwKMK0_eIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b899b4b38.mp4?token=J9bqyo8lg9wffOq1ic5WTDbQSDs8fpMBauFS0nAqKQyY7SUqQ-ZxvINuA3Lr_TUzd6tBVCL0x8OdgLvdPrME42T9iTsjmuoD8fmTQgNVaeUqzsWg6RT-NkGJgMkOBMhujb0tU3eq9CT28qZr1pA4QhvG3WbcrnydKpDqLwkoHSCXGh3lBYwhmB_lttmwKq04O-1R9XyOarvg3DVehJk5MYHyPGOjqfSV_EWwzdFtboBIPJJwHmiGKfzd1tN3lc7r7I5S6_nVVpeszXsJMQ9sL6m8qA3saG9P1Zdq_wjqUOphw85TbTNCDfKDOF8eA69pv3lna20NMNUQnwKMK0_eIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی شورای نگهبان: مجلس مصوبه‌ای دربارۀ گواهینامۀ موتورسیکلت بانوان نداشته
🔹
در خصوص لایحۀ ارتقای امنیت زنان در برابر خشونت، لایحه هنوز در مجلس به تصویب نهایی نرسیده و به شورای نگهبان ارسال نشده.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460244" target="_blank">📅 11:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460243">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صدای انفجار در دماوند ناشی از برگزاری دوره نظامی حیدر کرار بود
🔹
روابط عمومی سپاه حضرت سیدالشهدا(ع) استان تهران: صدای انفجار شنیده‌شده در محدوده شهرستان دماوند ناشی از برگزاری دوره نظامی «حیدر کرار» و استفاده از مهمات در جریان این دوره بوده و جای هیچ‌گونه نگرانی برای شهروندان وجود ندارد.
🔹
از شهروندان درخواست می‌شود ضمن حفظ آرامش، اخبار و اطلاعات را از منابع رسمی دنبال کرده و به شایعات و مطالب غیرمستند منتشرشده در فضای مجازی توجه نکنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460243" target="_blank">📅 11:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460241">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05b64f373b.mp4?token=k3rJkKGjVoif6AS8e0JkQnqn22pWOqimtmn-DvaOsmdpixv1sz0_KCQa42w9wo7PS8BxrpbhqyztffEcSgJ-LWIQmhKoqURvMNPZdfmULKYcQzXCpplrB64yqCuYFWHP7PQhnQqLgHpsXiWqHAdDnoUuUEwMb7NxkvMueDIJxz8GTmVeeVN2Qk-ct_wvO852hRIV4Pbg1r70y0L_5mU-REqNevXOR8UY1fe2wMZC8d4xtTHGDQ9WrUI3iVW42hx0XLxIzpFJREtDAFaKap_vyj2Ro8fkLsiFZMhCLGTRtfENx51QWYNIIOCBRtq3eN22tNbLsEiQFCVocnKZBf_Y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05b64f373b.mp4?token=k3rJkKGjVoif6AS8e0JkQnqn22pWOqimtmn-DvaOsmdpixv1sz0_KCQa42w9wo7PS8BxrpbhqyztffEcSgJ-LWIQmhKoqURvMNPZdfmULKYcQzXCpplrB64yqCuYFWHP7PQhnQqLgHpsXiWqHAdDnoUuUEwMb7NxkvMueDIJxz8GTmVeeVN2Qk-ct_wvO852hRIV4Pbg1r70y0L_5mU-REqNevXOR8UY1fe2wMZC8d4xtTHGDQ9WrUI3iVW42hx0XLxIzpFJREtDAFaKap_vyj2Ro8fkLsiFZMhCLGTRtfENx51QWYNIIOCBRtq3eN22tNbLsEiQFCVocnKZBf_Y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعام تصمیم گیرندهٔ نهایی دربارهٔ زمان برگزاری انتخابات شوراها
🔹
سخنگوی ستاد انتخابات: براساس مصوبهٔ شورای عالی امنیت ملی قرار بود انتخابات شوراهای کشور ۲ ماه پس از پایان رسمی جنگ، که این‌زمان هم توسط شورای عالی امنیت ملی اعلام می‌شود، برگزار شود.
🔹
بر همین…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460241" target="_blank">📅 11:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460240">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjlYhbq3VH3RPzTyeAUuOgHi2B91QvnPxZ2_eWx19-HB5S1Qe4Vn9wt_RCnSB4DsgJQGKMp18iZFiIKawQ4ASvxEr_A9th7h1kIpeTKibVQk4uG_Zlp5fOT0pm2LhuSjea5l4dD234iygAWT_2vfjZYWeCHW4YRTeYyZTVrDhIfiXYq-igWIbgLyo7dLk1zKRSyYV4EyY_P4SCCzIo2oumOFc9wtG6XVIm7TY7yR2cAvLEN36UH25-ui6Zevl2t2jtfZz8sR7bOyyM4eiHbe4JrrZWDS_19K89hhgaWGwQhQcqtn9UJsIdMm3f78q1c_x8BhVLa0JebYWnQX1HfBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۱ هزار و ۲۰۰ فشنگ جنگی غیرمجاز در ماهشهر
🔹
فرمانده مرزبانی خوزستان: یک محموله شامل ۱۱ هزار و ۲۰۰ فشنگ جنگی غیرمجاز که در یک شناور فاقد مدارک جاساز شده بود، پیش‌از ورود به کشور در ماهشهر کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/460240" target="_blank">📅 11:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460239">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl25gUNX8Zzpiiowlj5cpwKyzwvCMyCnVK7VZmPwYtbmc__YkwyYHNG76X-LTqzLUxoiLs4K-IyMOkTrTB50ZPfg3oQughYn_mH8R5s3Uvq7ENz4ZS1BZ87tbOa0JCM5Ef39Iv1L1Sa3844zwyvESPVVQY4AuD0dJ5NYYdVp1Ayqd7hHJfFwZSaYf2rbHgOpxL2tIij8JE2JKPbsaviujSbH_nGL-M8XbNqvNN7zq4i6ETeXDgKl0fjmKe2mqmsfcRmhNZhAacwlosoN5fTaR1gY2jxAH8unjLwquxWLqV2q8abcYps1VC_aBrkM5-Ey8hH7Mb5KKRDj-A6EkSzQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شتاب چادرملو در توسعه معادن جدید؛ هدف‌گذاری برداشت ۵ میلیون تن سنگ‌آهن
همزمان با نزدیک‌شدن معدن اصلی چادرملو به سال‌های پایانی بهره‌برداری، توسعه معادن جدید با هدف تأمین پایدار خوراک کارخانه‌های فرآوری شتاب گرفته است.
فرید دهقانی، مدیرعامل شرکت معدنی و صنعتی چادرملو اعلام کرد: در پنج‌ماهه نخست سال جاری، بیش از ۳ میلیون تن سنگ‌آهن از معادن جدید برداشت شده است.
🔹
از معدن D19، یک‌میلیون و ۵۰۰ هزار تن سنگ‌آهن برداشت و بیش از ۱۵.۵ میلیون تن باطله‌برداری انجام شد.
🔹
استخراج سنگ‌آهن از آنومالی ۱۰ نیز به یک‌میلیون و ۶۵۰ هزار تن رسید؛ در حالی که این رقم در مدت مشابه سال گذشته ۱۲۰ هزار تن بود.
🔹
برداشت از معدن چاه‌گز هنوز آغاز نشده، اما چادرملو هدف‌گذاری کرده است تا پایان سال، مجموع برداشت از این سه معدن به ۵ میلیون تن سنگ‌آهن برسد.
دهقانی همچنین از تداوم فعالیت‌های اکتشافی، به‌ویژه در شعاع ۲۰۰ کیلومتری مجتمع معدنی چادرملو و محدوده‌های زمان‌آباد، بایچه‌باغ و کال‌کافی خبر داد؛ اقداماتی که با هدف تقویت ذخایر معدنی و تضمین تداوم تولید شرکت در سال‌های آینده دنبال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/460239" target="_blank">📅 11:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460238">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MecKFH1_rJu5nATu7W-_9qTbUQTRQ4JUZAD7TrWmDla7MiStthJTAbDATvNhYWJ55Zi4_ePEuN-xjgztWdMVvc024LQL0iVlCMg3gGPyBwVmFPSh6xRVsa752uum86cAuhfHYJeLB0B5Z6kLHqlze2yrHMUfCUGF-9fjmg2_T1QHXl1odOCHAmgTGI1rZ9YXDBBBbJJlBpqY3BexKmPo_BPDi4CQxaUB31yULVP_kNSi8yy-IvL22eDLtZl0Ywgh5CjiVZU04QTUDMlzJgwJ5FeK8pmbasGGKZiAXZ5f2wH1BroRky6-XBZAyt4xkEtueSg0dGnJuZ3Ra_cIV015Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
انتشار اوراق گواهی سپرده خاص از سوی بانک رفاه کارگران
🔹️
با هدف حمایت از تولید ملی و اشتغالزایی، اوراق گواهی سپرده مدت‌دار ویژه سرمایه‌گذاری (خاص) از سوی بانک رفاه کارگران برای شرکت‌ شیمی دارویی داروپخش و گروه صنعتی پاکشو منتشر می شود.
🔹️
علاقه‌مندان تا پایان روز شنبه 21 شهریور ماه 1405 فرصت دارند با مراجعه به شعب این بانک در سراسر کشور نسبت به خرید این اوراق اقدام کنند.
🔹️
این اوراق با نرخ سود علی‌الحساب ۲۵ درصد (پرداخت سود به صورت ماهانه)، یک ساله، به‌صورت با نام، الکترونیکی، معاف از مالیات و با امکان بازخرید پیش از سررسید منتشر می‌شود.
🔹️
از جمله مزایای خرید این اوراق می‌توان به دریافت بالاترین نرخ سود اوراق منتشره فعلی شبکه بانکی، تضمین دریافت اصل و سود در مواعد مقرر و... اشاره کرد
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/460238" target="_blank">📅 11:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460237">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/460237" target="_blank">📅 11:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460236">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d111e6078.mp4?token=Y-d_tHWHhnJEGsPk6LZxuEIJqkD2MGZP3sQWHodSCPkapnoZDElFhjLcSYSVJU66uXfjYQklSWrEtY6pxGXEbiLqh1KSgnLjf_E12p-NdigtTG7eOJhT4OIt4dv9USdlO-t16OEUbvcPlyj_HGvcvh1kL2y8KQT5xC2y7zp5bG58ECF2mckjNW90z--HRE_TFKOHjZGDZVuHV8ffXENWhEXaPyfKjjaALuv_g76_oZJwov7IhhDCHeUp2R6TwhBFY0vN81hZ0MLitVJTNozCj0C653d0g1VRIB1pEhmpgTs5Jw3CITGnCfG-XYUSBnjnNH-ZODATlzHLu7pIXeq1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d111e6078.mp4?token=Y-d_tHWHhnJEGsPk6LZxuEIJqkD2MGZP3sQWHodSCPkapnoZDElFhjLcSYSVJU66uXfjYQklSWrEtY6pxGXEbiLqh1KSgnLjf_E12p-NdigtTG7eOJhT4OIt4dv9USdlO-t16OEUbvcPlyj_HGvcvh1kL2y8KQT5xC2y7zp5bG58ECF2mckjNW90z--HRE_TFKOHjZGDZVuHV8ffXENWhEXaPyfKjjaALuv_g76_oZJwov7IhhDCHeUp2R6TwhBFY0vN81hZ0MLitVJTNozCj0C653d0g1VRIB1pEhmpgTs5Jw3CITGnCfG-XYUSBnjnNH-ZODATlzHLu7pIXeq1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغازی بر پایان حبس بدهکاران مهریه
🔹
مصوبات جدید مجلس برای تعیین سقف مهریه و حبس‌زدایی از قانون محکومیت‌های مالی را ببینید.  @Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/460236" target="_blank">📅 11:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460235">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1180fc6a1d.mp4?token=fRxkfNCQ5LAqmh-cYFVIf0ZlM22OJ6aWWZGtLlIhh02aNNbiJPbQIIKPBWbl_3cWsVEx4d0_f4H6U6R3hskSPeB5wQxZiYUFVAvXe9zAEFH0N3GMlFIgYFyDzjudSTKa8r9aXNMdHb96PsAO1TI6DYXI6_3a87MFCD_b8WaIgvcZtNngxrvBu9koYxfdWdi83k5VjoRz-kMa3Z9xVKlsfK1wncqJI9d-7eKfr_OkXjhaZsm8Te1hr5PbKXwZsmOA4Cgz0VoqdnYOCegIedOgkvtnDxl0TyxclwCq3KJ_-yCIWI667wGNk6wotuPWeqOq8V31iEj-Yi3lWrbzd7WZjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1180fc6a1d.mp4?token=fRxkfNCQ5LAqmh-cYFVIf0ZlM22OJ6aWWZGtLlIhh02aNNbiJPbQIIKPBWbl_3cWsVEx4d0_f4H6U6R3hskSPeB5wQxZiYUFVAvXe9zAEFH0N3GMlFIgYFyDzjudSTKa8r9aXNMdHb96PsAO1TI6DYXI6_3a87MFCD_b8WaIgvcZtNngxrvBu9koYxfdWdi83k5VjoRz-kMa3Z9xVKlsfK1wncqJI9d-7eKfr_OkXjhaZsm8Te1hr5PbKXwZsmOA4Cgz0VoqdnYOCegIedOgkvtnDxl0TyxclwCq3KJ_-yCIWI667wGNk6wotuPWeqOq8V31iEj-Yi3lWrbzd7WZjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ یک میلیارد فوت مکعب گاز در راه است
🔹
فاز ۱۱ پارس‌جنوبی اکنون به بیش از ۹۱۵ میلیون فوت مکعب رسیده و طبق برنامه با اتصال چاه دوازدهم طی چند هفتۀ آینده به حداکثر تولید یعنی یک میلیارد فوت مکعب در روز خواهد رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/460235" target="_blank">📅 11:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460234">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249e76b406.mp4?token=Av1OOIpbE3xVVowKuuq-AZmn2ydgzOvEQPXhv5GpdsCwmUAzggxVlJDb5OgJvcuoQ_H2r2fKvGHRQVzicIgiPo_CQBOK9HhjnIVX0QF4swYqd1OoH2UffZh6do0GuEEYhN0i4Y_WEp64zeake4lm96IYqfWZJN8H6lUhZEO2wZvespB2WWOR4cDiR5QwPGv4YesVeCBAGIu3j6cL1NvVz_Ie6H29IvO8ZtC4m248lrYFLrWxkoQXVWyW0mWH6-ESoN1mAXhZBfWUoASd41z79wHNZrN5Hu0XciyxhxKZ9jzMaNHuUNRUYJlYr8Q-Bmpt_pkrMdicsYHpXxj2xNwlrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249e76b406.mp4?token=Av1OOIpbE3xVVowKuuq-AZmn2ydgzOvEQPXhv5GpdsCwmUAzggxVlJDb5OgJvcuoQ_H2r2fKvGHRQVzicIgiPo_CQBOK9HhjnIVX0QF4swYqd1OoH2UffZh6do0GuEEYhN0i4Y_WEp64zeake4lm96IYqfWZJN8H6lUhZEO2wZvespB2WWOR4cDiR5QwPGv4YesVeCBAGIu3j6cL1NvVz_Ie6H29IvO8ZtC4m248lrYFLrWxkoQXVWyW0mWH6-ESoN1mAXhZBfWUoASd41z79wHNZrN5Hu0XciyxhxKZ9jzMaNHuUNRUYJlYr8Q-Bmpt_pkrMdicsYHpXxj2xNwlrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی هیئت‌رئیسۀ مجلس: طرح مقابله با نفوذ محدودیتی برای تعاملات علمی و اقتصادی ایجاد نمی‌کند
🔹
گودرزی: تمامی کشورهای جهان دارای قوانین مشخصی برای نحوۀ تعامل اتباع خود با اتباع خارجی هستند.
🔹
این طرح با هماهنگی کامل دستگاه‌های اطلاعاتی تدوین شده و هدف اصلی…</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/460234" target="_blank">📅 10:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460233">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۳ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/460233" target="_blank">📅 10:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460232">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2797232c53.mp4?token=t-Dahm2EUt88ePRkK1mjGxVa9W0XlW7PE6eXYLvk1n0HCGvyWu2Z8rMlGvn5g7_AIy2-onrDJrf9vNemmWrMmZRLuerzLFtSWET_h053QMQ5FBSQaZGt7zSqm3hhLXYbGU84p-Sq-V7SwMhKJ_dygaIj6PTk9iYhNLTATLVqTbKRfoVqFyXPclzo0T_ZWQXooOJk_8ecqhxso4rzPTrvb8E0ZIfMJkDgMJjwh3JqU9GvG6I2TDNHfqxdFt5YbkQ8CTIUMga0r2hkbzX40nNQOBh2yPpeuchUyH1hcBzGU1X1kZtJrwFHDLsu-2NjHhxGGCh8nJupxsBWHBTr_JMK1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2797232c53.mp4?token=t-Dahm2EUt88ePRkK1mjGxVa9W0XlW7PE6eXYLvk1n0HCGvyWu2Z8rMlGvn5g7_AIy2-onrDJrf9vNemmWrMmZRLuerzLFtSWET_h053QMQ5FBSQaZGt7zSqm3hhLXYbGU84p-Sq-V7SwMhKJ_dygaIj6PTk9iYhNLTATLVqTbKRfoVqFyXPclzo0T_ZWQXooOJk_8ecqhxso4rzPTrvb8E0ZIfMJkDgMJjwh3JqU9GvG6I2TDNHfqxdFt5YbkQ8CTIUMga0r2hkbzX40nNQOBh2yPpeuchUyH1hcBzGU1X1kZtJrwFHDLsu-2NjHhxGGCh8nJupxsBWHBTr_JMK1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لایحۀ یک‌فوریتی مقابله با جنایات بین‌المللی</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/460232" target="_blank">📅 10:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460231">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de329f1.mp4?token=WFVGihltx68HQ-2_rpK0AIjWVBReiC9bPMxhW3TREPASD23F6owHbdcZaOr2t-UJ0NEj0L5c4QglzeejRlQmbde5ilZeYMzx8GyvQTZomVgfjruqDv06CLC1ozC-CBlvH1kjgTp3wuiBifHc41xI9NmgsTBgSEifhDF8irN1UPIHeN7D11ZBqGyvyCCbSCHRUXHdldw2Wb5aHVsm-7N-S6_Wryt0n2kFifRuGmq7gnv_nLP2u0ZHBQ_HWJ8VCz-pqKyz_x98m1ZaEyRYCI2amkoYDlZe7dzV4h5fUah0p3RBtW3zqvlVcXq6gMLK-x-dAtHs_7_xMfQCR3P-Z6CXqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de329f1.mp4?token=WFVGihltx68HQ-2_rpK0AIjWVBReiC9bPMxhW3TREPASD23F6owHbdcZaOr2t-UJ0NEj0L5c4QglzeejRlQmbde5ilZeYMzx8GyvQTZomVgfjruqDv06CLC1ozC-CBlvH1kjgTp3wuiBifHc41xI9NmgsTBgSEifhDF8irN1UPIHeN7D11ZBqGyvyCCbSCHRUXHdldw2Wb5aHVsm-7N-S6_Wryt0n2kFifRuGmq7gnv_nLP2u0ZHBQ_HWJ8VCz-pqKyz_x98m1ZaEyRYCI2amkoYDlZe7dzV4h5fUah0p3RBtW3zqvlVcXq6gMLK-x-dAtHs_7_xMfQCR3P-Z6CXqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرح ملی توسعۀ هوش مصنوعی اصلاح شد
🔹
نمایندگان در جلسۀ علنی امروز مجلس برخی از مواد طرح ملی توسعه هوش مصنوعی را جهت تامین شورای نگهبان اصلاح کردند.  @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/460231" target="_blank">📅 10:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460230">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFXbZQUuhELD9ashL3NNkU8cfMHx9wwi_uRIp0R3gulU-Pui8t0ALly1WiUGOCBmcpXijCg72TE8gkb0fRbdxVZgO0iE77nJrC8LAqbxHnR5xhL9lLJtrFVXyiOOQ1FOdCYrKqx66F-wGBgeiS0c86-e7SOfzGlZqzC8DM3Uc6ZwHlwtJ_R7ccj1umVWVB20azsXWPVsAA3qZHl2HIdLXMLFNWSys0Z5Ve2FoizbeKqkrFfEPd2xR1h3s_3Ut7yPz-eSFc5JfjVV2rqETiZ9ik4hUPirhJmPOlD7Qkm2NrqilnnFWPaA0YAu7sywPE4tMhljj9hBt5k4dCbmb_SIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌باش باران در چند استان
🔹
بررسی مدل‌های هواشناسی نشان می‌دهد امروز در بخش‌هایی از شمال‌غرب، سواحل خزر، ارتفاعات البرز و شمال‌شرق کشور، افزایش ابر و رگبارهای پراکنده پیش‌بینی می‌شود.
🔹
در جنوب‌شرق نیز ارتفاعات سیستان‌وبلوچستان، جنوب کرمان و شرق هرمزگان مستعد رگبار، رعدوبرق و بارش‌های نقطه‌ای گاه شدید هستند.
🔹
در مقابل، مناطق جنوبی، جنوب‌غربی و مرکزی کشور همچنان گرم و خشک خواهند بود و وزش باد در مناطق خشک می‌تواند موجب خیزش گردوخاک شود.
🔹
مدل‌های میان‌مدت از کاهش تدریجی دما در نیمهٔ شمالی کشور حکایت دارند، اما هنوز نشانه‌ای از موج خنک گسترده و سراسری دیده نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/460230" target="_blank">📅 10:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460229">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnPVVqCCvlOcSB89l_CNxnThPoRnmMaMInKnOnY7D9Tyy6SXVdqJKSk-dBx5qAgIAJSdPexUKedkZiAQfUuvc6obK4hAVrWKOMmJXRn3rTGcVWr6xeK3miQ_1wy6LqCIRUdFWfeAbr4cJql_7EPcRIFnQYCfS---3b7rVF19HWjM4RNyecE4NaCUa8Y-BVeqh9L5o01wc9JRPhlmFawlznjfLgQfZcOlFFjiTjT1uO7lbjXJ6BN3ZDvTxaKahc5nQmfq4dL0zG0lPwbx666HUlymPepEEsn6czpS726XkQlAJCt5HQOlsKRpeaI7toGoDJcoKIqs9cUlc9t77Jh-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سونی با هوش مصنوعی کودک‌آزارها را شکار می‌کند
🔹
شرکت‌های بازی‌سازی معمولاً اختراع‌هایشان را برای فناوری‌هایی ثبت می‌کنند که به‌نفع گیمرها و برای ارائهٔ تجربه‌ای جدید در بازی است. اما سونی در جدیدترین درخواست ثبت اختراعش (پتنت) به‌دنبال محافظت از گیمرهاست. هدف این پتنت، شناسایی کاربران مشکوک در محیط‌های آنلاین بازی با استفاده از هوش مصنوعی است.
🔹
سونی در درخواست ثبت‌اختراعی با عنوان Large Language Model Powered Social Integrity System، روشی مبتنی بر مدل‌های زبانی بزرگ (LLM) برای شناسایی و مقابله با رفتارهای مخرب از جمله کلاهبرداری و سوءاستفادهٔ جنسی از کودکان در محیط‌های آنلاین پیشنهاد کرده است.
🔗
ادامهٔ خبر را
اینجا
بخوانید
@farsnart</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/460229" target="_blank">📅 10:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460228">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCUBxf_ou7blT6xGeYzPmF1JK_h4sGL4AshFyZQiiLHaum4EKt6456NlPXGMVHfL9Kq87r-Ft1USPOxOCTZqau8vUJRz0Fe5cS7vfswTEeXVcuT9UVgN5Jg4BGathZmSymfy1EGCmAHZYCZvlJoMGuO-OpBo2iRVeBbGD-j7iP8VUh5PaIyUmVSNZaS3gl8Xx-CSCtebwXZXTnS8mxG7CnzTU3zqbdSBjOMhuen_8uIRE7DdKABTeJI9NV5AApNPso1vIETPyJmwFPlLQomdQCjbCwUzfaVju_ZIWw9VDe2NoOL-eqKlYIILg65FfSjoNLaspslF_SnLGXUhhTjPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرومیت یک جلسه‌ای برای هواداران چادرملو
⚽️
کمیتۀ انضباطی چادرملو را یک میلیارد تومان جریمه کرد و حکم به برگزاری یک دیدار با حضور صرفا تماشاگران زن به‌دلیل تاخیر در ورود به زمین، پرتاب اشیا و بطری و سر دادن شعار علیه بازیکنان تراکتور داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/460228" target="_blank">📅 10:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
🔹
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
🔹
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460226" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6XJe_2OH0pKaufaAPlroLRsBxaFWu2tK6Zxq2oqtzhcvOnsYjhj47A9ahcsXLhJBDNaj4fai2258dD4JP8UJuHJ5MqD3OhegCb8SZzISox7tFhlLDRrjgUjBMPR9EdDoVfIyR_sLo4Ii0umS4BITlYY58lRbL8epQcYuutu7Ibzi4f-YhiTg9FC9ONPyll3IYfriTwl8J9gFElSMONm5eVnd6ad7j0tpJIvxEpmDKv9xmLbN8uP1-sHp5hbtVbyiPp_nMyVVk-doZdIc951TP-B7rFGJHdUpho_JrIwoyOTSdDx9psQhsjpzN5ePd7Ev5dY-zau41tktUkRYqnFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اژه‌ای:‌ آمریکا دنبال چاره برای خارج شدن از باتلاقی است که خودش برای خودش ساخته است
🔹
آمریکا و اسرائیل در سال گذشته و امسال همه توان و امکانشان را گذاشتند تا جنگ ظالمانه و غیرقانونی را بر ایران تحمیل کنند.
🔹
ایران پایداری و استقامت کرده است و آمریکا به هیچ…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460225" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mkAeRWd5C1HeUSaly4H6pxlTt5iXCdeLbc0JsYpukSux-rcjOXeMejGzkVXtfnTxjPR3eiu6MMixf5ZNbGUR-oFmGwb-R9_-AH1A6tRSXur0OpegxJz65rvgIVG6GlGEiyBnZ-UHGkl7hQf3yeeCNMEPUomG7BvVq5bL7ov-Mr944-ZxFgXhKVMr7hotT1yBj1M77xvm6_mUrwyF81U8tVECYm9m59R1MU0sbKDCrizdXY8exRRldz8Z5mxcbXH6zuxR8xsHEdZMqNlqCtwPS8fuOBIufcQH92k0e6gHOk830b8cT4GBYasFBmdD-usu5Cavjq1n0oohniA2W_dEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVS-Uoymvm-8T9XzfgDn8VDRT0xOeY6pd8cGHSMgm9UKxI5UBF5cHLYeXGvnRXggUHWtDU8rZgXNyUifXyo0LRM8yiQN-VpmqxkuOQamMELj5K-R8cXriXIykzPqTrJbZRlCz8qJSQhnj8Fb7y0z3hv5cs9r6tjCl9AqupZxewusWrO3qw15FUVhHp2Kn9G8eNBgo5DYzAr1QhbfdNREZgkBf0d7rOQOnY6XtiQdRMDQqwzJ8vCd9JnRW8-y6YeR7J9iWGQOuLRRWMPxvVqwuNoEDyEkw6dvQV2QsRQpNJPaRQWvSqeADRCI4aVa5MTTYsc1-9XAV5k2RA2ysm37QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yaa6WHxWMyR_Xa3VQfGTeMsu6J0VST1q3kc7tvRUqPWuVrDYFYxddoWEUsbgNpRizn5wONE4F3-vCfEvwJGLWl31yJwBGXrW5zXbk10oQ5COaGxcSZ__aLBOQ8ntx0yU_6xZrEnSFK7gxzkfnOOtXkZWSzkHR4qAckpv3vTsdSb8XpNMjCVvNqtcrMdyK1xSwdW5lfzMiKunTyDVhLxROzcEVhfRoe93dHSaVN5019U5bHovl-a3u5c-GqjPAyx2H9Dpx2140kPy31rMTmB0J2NZPQJp0MGrj7zK51a4PzXqXuzSI5cdynF1Eeg5zUL7HuTZro1-yA0TzJeix1jrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOCUnPkrXV_0Ti7c3qeJ1-K8SZVw18rNMXIOgnRVj6g5UoXVzT_5xaOenbL4VubMqfnzBNna_F-ptu1ta9MvFPNrXsewn2qVwgDUr_UM4jORkDMlf_PWdUrzoFEBeVfKna6mEjK_33Gy1EcaOVQMJ_Wnqk53td0i1tDakVSF1jpZQYKLAlSEjZq_BagcK3VOWEVKKVxgUFbc4fVs7wEQgeZH1Zjeef7YJxCaTNHWq6dt9XmBWehFIzSAdntEXXxlS_76LMDyeSyBfK4Bi9lxkltjJz88b87ol4UaUQnwebyjUdKLYMQZX7-V5gSpGbM25IabBgrtaaWy9i1tBEKF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsHBq_4bH_8geRznAaWWoMLoKq4LTUsijm9jHPCKNRzvbfu8vNaVLwPCpy7ymGVmwCMhIOw1M4mkp6a-gB9PW16LoDNqh2qKIk-h6dRIgFxf_nEVtPMUI0Wbbfx_bIXdn97zH4K1ORFr6ko97XqOmcHnKaooagXdJT3EkgEj49J47MTll-tnA2BmLZGLmbuq8HhFlYyp3b-0zFMHI_M8jUJcyY6JrDyLMFzx-JybZtZaLAtHqtXkNDXJmjMnTvnKb5cwr_fi1qfRI3HqWTleDYQqsbY00h3ZZR3wwFV3WwnSkThLjEszIA8FxvLQjYqXraXnUrgv8nnyHR7mq4SVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfhesrJ8XOVURYHQh4P0QQF0umAf_E-QoI5Y-lhjmBmHsMKSM5ydrKGSmeGp11LGHae966JtTRmzhG4AteATbH4SJFdjkjnipEQvQnyEPjSfI8a3pvzEI6EJLnAEU03azL2mMHj74o9SnUuwRluI7_TZ6EbAE6nFCl0hmj57RFUe-frqfTWIanQSBGT-I9idaN2Y6f3mfxTH-ICw0UTS-fX70jM3VJ1aHbokjzsnZWP7BgMAuQ8ufu2AGP9qCnIAJ8WCbP9Eg3CQD9ifAdlMkfeyF6LU6bOAJVI2emMYHLWgwcT5OQxLEZk1MzcL-H1_gJIv5LYSdh3TuU9XSXN_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArZN0SnAruRlEzhPn0vYDzhUK-DE4wrzCyuowagNpi4MnYpI6h2JuWqIimcCKa4rd_KZfVLIqKbw2G2eVogk6WE-Fo6eaNcZuk9GymUQNVvgT1OFU9HH92zUDvf_x86as3gFVrERD3oLn8G4Hn1CyIQfcmzL6axZsWHb30c89KSBv8lHxmObRm90SSIHm8kdgaiE24WTpgjG4ry53e4dNf2IABPqge4o0tteue4oWjigIucagUHGn2buyQlih6HBE1HQYVnSziTZO31OvOuW29tqMcLdAeByZyAczibTkMq_xzE5CTDR0Vyd9BLqNUthWSga7XO7POKSUX3VxoaP8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آبادانی‌ها در تکاپوی برداشت خرما
🔹
برداشت خرما در آبادان و مناطقی همچون چوئبده آغاز شده و نخلداران در گرمای جنوب مشغول برداشت محصول هستند.
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/460218" target="_blank">📅 09:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عرضۀ واکسن آنفلوانزا اوایل مهر
🔹
سازمان غذا و دارو: با وجود تأخیر تولیدکنندگان خارجی، افزایش قیمت و مشکلات نقل‌وانتقال مالی و حمل‌ونقل، واکسن آنفلوانزا از اواخر شهریور و اوایل مهر در دسترس قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/460217" target="_blank">📅 09:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiM5x3IzTCV8iFzOtTMKQ6YWwfeYkF3IgEaMIkXdx6vW66LtqjDHui2JzqzUFqf_FiGIicEC1BSaVsRCgT8W0I5qt027OnhO2rCVyj1Oi4gn2egzB2mK1dqogDba5WCmY-xCH2zh1a8k83fqBWDp4YAfkbtdfdqrZJ9sK5xQs7OS7vJrb7BlZscov-CNdKdG4dDhKhm8RsosW3-dOaRGyeb02g1tcPGP5YFAGu7-a8_6iicbl_AgEZkfqvPveze7-qlx--qzDMjJGNE-b1hSWiaBglTU3TPbQtqPO_ociAM0hfppjD9DPtKLS3OhwSbFXagqOg99BfCIi93RznS-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/460216" target="_blank">📅 09:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c6f58dc64.mp4?token=DXSamUK6sqT-oJqrivi5-3iFuMbyb2YcLU1H2Sh7EMrB-UwD070BZqsvFxHoUC-7ZEdwtqT3xqgemgn8TgU9Y1Uo3Rg5EvDo-yymXEPqJ7XhyadZ1LADD9WJW0x__cF22ZxehbBEPrklqeSSd7HtPnkFxBVv8kF2xsH8vJctnpGgYsmRUF5CW6G1rvumSm1FyIGQ8LTpnmseFRhr72N2ZgIWfy9nqYfJOjrG6BpDl1MQUYYkqE-7sfAZ6Hd11NY1IY8LeretRpU5y7J2XnVoPfd32SA7pycQkvCWKU6mQTOxH8Kh3Fq21BTPbtuk92KgSXoTA-f_aujifR-zydK4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c6f58dc64.mp4?token=DXSamUK6sqT-oJqrivi5-3iFuMbyb2YcLU1H2Sh7EMrB-UwD070BZqsvFxHoUC-7ZEdwtqT3xqgemgn8TgU9Y1Uo3Rg5EvDo-yymXEPqJ7XhyadZ1LADD9WJW0x__cF22ZxehbBEPrklqeSSd7HtPnkFxBVv8kF2xsH8vJctnpGgYsmRUF5CW6G1rvumSm1FyIGQ8LTpnmseFRhr72N2ZgIWfy9nqYfJOjrG6BpDl1MQUYYkqE-7sfAZ6Hd11NY1IY8LeretRpU5y7J2XnVoPfd32SA7pycQkvCWKU6mQTOxH8Kh3Fq21BTPbtuk92KgSXoTA-f_aujifR-zydK4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سالروز ورود حضرت معصومه(س) به قم ثبت ملی شد
🔹
هم‌زمان با فرارسیدن سالروز ورود حضرت فاطمه معصومه (س) به شهر مقدس قم، خادمان با گل‌آرایی ضریح، حال‌وهوای ویژه‌ای به بارگاه بانوی کرامت بخشیدند.
🔹
همچنین سالروز ورود حضرت معصومه(س) به قم در فهرست میراث ناملموس کشور ثبت شد تا این روایت تاریخی و آیینی برای نسل‌های آینده حفظ و منتقل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460215" target="_blank">📅 09:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6105bb16.mp4?token=S857Ex-IjcZk_XYakTYlEglVO_8DvPqh3RmMZCmfJv0ltrHyNriB-MBOoPBg8ukkKmua-gY7HorfaeQYn-fwf9Ge4zTy4SG4PJP2Wd2qsTln-bvMmV9ne2SMidbhBwCpk3y_p3oYI-KuEKE6P2VTZ2RHLVKlewYmDndE9dSe6FZPO4B2YKEH5OgHsuKmUqYAovzxVh4QrtmsHSUzuQPInRi4sKg8fIbDUdDyZsNFrGFsexyvVnCE5ruxJvPAq4q47uV5HGtVvag1sKes6VD7swS9rYdfSsOZ-7kYHdBmqRcvn7bK27qale0u09797DsrCfhZ0fTOLxlTqAU8SrJKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6105bb16.mp4?token=S857Ex-IjcZk_XYakTYlEglVO_8DvPqh3RmMZCmfJv0ltrHyNriB-MBOoPBg8ukkKmua-gY7HorfaeQYn-fwf9Ge4zTy4SG4PJP2Wd2qsTln-bvMmV9ne2SMidbhBwCpk3y_p3oYI-KuEKE6P2VTZ2RHLVKlewYmDndE9dSe6FZPO4B2YKEH5OgHsuKmUqYAovzxVh4QrtmsHSUzuQPInRi4sKg8fIbDUdDyZsNFrGFsexyvVnCE5ruxJvPAq4q47uV5HGtVvag1sKes6VD7swS9rYdfSsOZ-7kYHdBmqRcvn7bK27qale0u09797DsrCfhZ0fTOLxlTqAU8SrJKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات ۲ کارگر نپالی از یک تونل پس‌از گذشت ۹ روز از سیلاب
🔹
درحالی‌که عملیات جست‌وجو برای یافتن هزاران مفقودشده درپی فاجعه مرگبار سیلاب و رانش زمین در نپال ادامه دارد، امدادگران موفق شدند ۲ کارگر نیروگاه برق‌آبی را که به مدت ۹ روز در یک تونل زیرزمینی محبوس…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460214" target="_blank">📅 08:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrB9qY76DpSc2WEmlX5i_6xzwpglt2kfu3NuWqsdLVqJCmzQqMlq78KN2vqiC0d7rmR9I6-FRo948624yA1INinHc1INK3nfdLPXrxaF4lCw19I2dPTa-CZCIpGdH0rGw-K47pFPhlh1xMjK4X79jpc69QyvKsEq8B8Llal0M1hPyOFPB6HuAi3tRi8wf6ySQa9TP7c_VXfOLQyL_8rAssWEf6-1Q4D3C4IHOSicGaWb297lkkm7YbbZrufMHq3f_Ka3BaZgYbBAF8rMOrn762B_lIcKxl1CxU1zwa9hzrO6daaROPnorwZPrHXCPIEpY3Omyl4bv7EDlj4y4BjkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست نیمه‌شبی اسکورت آمریکا در تنگۀ هرمز
🔹
نفتکش حامل گاز طبیعی مایع الغشامیه که در کریدور جنوبی تحت حمایت آمریکا در حال حرکت بود، از ادامۀ عبور از تنگۀ هرمز انصراف داد.
🔹
براساس داده‌های رهگیری کشتی‌ها از شرکت تحلیل کپلر که در اواخر مرداد ماه منتشر شد، کشتی الغشامیه به‌همراه چهار نفتکش دیگر حامل محموله‌های LNG از تأسیسات صادراتی رأس‌لفان قطر، به سمت شرق و تنگۀ هرمز در حرکت بودند.
🔹
این نفتکش حالا به جای بندر رأس‌لفان در قطر، راهی بندر فجیره در امارات شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/460213" target="_blank">📅 06:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هوای پایتخت «قابل‌قبول» شد
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۷، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/460212" target="_blank">📅 06:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31bd66a806.mp4?token=FMToGxi76tHr6Pb4PPTbkvr3YhcWR-lSTVHwnoDs2R8UsNBnflcmJSmnnW4yvPMRT42ScXdARtb-v2TcXejyi3yNL7FBPX3H5_5ZiM_S0U6vy9CdRUxHOd7ekSOxV4D-NENtSZEr79uoK4oajSzwC_TPDIPlNFrvME07b6QhzEUItX7t2IA1SabnouLiyrl2nfAC4oCaRQGX2YpDKV-5-kVJDJM2ootmSmGqt3_wm6YShWiXh7KWE5IXlqr7T9JBRfxa-1blASEuh-Yvyoemyxd24iomR8Sw0jPx6iUUEzghdhJzybrbs6ypLA0cbU4KbVGgNtSr_ARmmubU54JOFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31bd66a806.mp4?token=FMToGxi76tHr6Pb4PPTbkvr3YhcWR-lSTVHwnoDs2R8UsNBnflcmJSmnnW4yvPMRT42ScXdARtb-v2TcXejyi3yNL7FBPX3H5_5ZiM_S0U6vy9CdRUxHOd7ekSOxV4D-NENtSZEr79uoK4oajSzwC_TPDIPlNFrvME07b6QhzEUItX7t2IA1SabnouLiyrl2nfAC4oCaRQGX2YpDKV-5-kVJDJM2ootmSmGqt3_wm6YShWiXh7KWE5IXlqr7T9JBRfxa-1blASEuh-Yvyoemyxd24iomR8Sw0jPx6iUUEzghdhJzybrbs6ypLA0cbU4KbVGgNtSr_ARmmubU54JOFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گیرافتادن چرخ‌های تانکر در آسفالت و فرونشست زمین در اصفهان
🔹
مدیریت بحران استانداری اصفهان: شامگاه جمعه هنگام عبور یک دستگاه تانکر از خیابان شهیدان کاظمی بخشی از این خیابان فرونشست و چرخ‌های تانکر در حفرۀ ایجاد شده فرورفت.
🔹
عوامل آتش‌نشانی و شرکت آب‌وفاضلاب به محل اعزام و نسبت به خارج‌کردن تانکر و رفع خطر اقدام کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/460211" target="_blank">📅 05:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d878e5adc1.mp4?token=Hqc1oxFGPhTPdh45iqZaTTdH1ro1a95tpTLEruPmwy8N5GCmXwTnPub5DWYWN3bxiQEOa2fl1fOkpjwlox8s4h19_8DZz2ypD2eS64P7-r2lxjR50RkstMmLvKkqsaJwXKRCldwaDxTvls9tTCPnK_d-f-rYk3zCJMWkLJmGVXfEDxDIikNwIcEYLdos_k9bINRIU0m4g4xNGRKZZVnd3i-3p2WnrwrRO-b-P9ZzpeK1vBLDZhkfPOdmPRS3rYUgsQe7mrF7kgtA5DXtb0Wi4VRf9ffckXyoXGMFjkLxmC7XWggECubk6wPSx6e0KN3zHSLyNPGabJICbdWNQjhSFIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d878e5adc1.mp4?token=Hqc1oxFGPhTPdh45iqZaTTdH1ro1a95tpTLEruPmwy8N5GCmXwTnPub5DWYWN3bxiQEOa2fl1fOkpjwlox8s4h19_8DZz2ypD2eS64P7-r2lxjR50RkstMmLvKkqsaJwXKRCldwaDxTvls9tTCPnK_d-f-rYk3zCJMWkLJmGVXfEDxDIikNwIcEYLdos_k9bINRIU0m4g4xNGRKZZVnd3i-3p2WnrwrRO-b-P9ZzpeK1vBLDZhkfPOdmPRS3rYUgsQe7mrF7kgtA5DXtb0Wi4VRf9ffckXyoXGMFjkLxmC7XWggECubk6wPSx6e0KN3zHSLyNPGabJICbdWNQjhSFIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش اخلاقی با اهل خانه عمرت را زیاد می‌کند
🎙
آیت‌الله مجتهدی تهرانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/460210" target="_blank">📅 05:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460209">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">استفادۀ پنتاگون از دروغ‌سنج برای یافتن عوامل افشای کمبود مهمات
🔹
روزنامۀ نیویورک‌تایمز گزارش داده وزارت جنگ آمریکا تلاش‌های گسترده‌ای را برای یافتن کسانی که اطلاعات مربوط به کاهش ذخائر تسلیحاتی آن کشور را به رسانه‌ها درز داده‌اند آغاز کرده است.
🔹
طبق این گزارش پنتاگون حدود ۵۰ نفر از اعضای ستاد مشترک ارتش را در ارتباط با افشای اطلاعات محرمانه به خبرنگاران، از جمله اطلاعات مربوط به کاهش ذخایر مهمات حیاتی در نتیجۀ جنگ با ایران، تحت آزمایش دروغ‌سنج قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/460209" target="_blank">📅 05:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460208">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
لباس سفید، شب سرخ؛ روایتی از حملۀ دشمن آمریکایی به مراسم عروسی در کوهستک سیریک
🔸
مستندی شامل نخستین لحظات جشن تا بیمارستان، وداع با شهدا، تشییع پیکرها و بازتاب این جنایت در رسانه‌های جهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/460208" target="_blank">📅 04:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460207">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">یورونیوز پیوستن رسمی اتحادیۀ اروپا به تحریم‌ها علیه ایران را تکذیب کرد
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا اعلام کرده است که اتحادیۀ اروپا رسماً به کارزار واشنگتن برای قطع ارتباط ایران با نظام مالی جهانی پیوسته است.
🔹
با وجود این یورونیوز نوشته بیانیه‌ای که بروکسل در نشست این هفتۀ وزیران دارایی گروه ۲۰ منتشر کرد، در واقع چنین چیزی را نشان نمی‌دهد.
🔹
بیانیۀ کمیسیون اروپا که بسنت به آن استناد کرد از کارزار آمریکا استقبال کرده، اما اتحادیۀ اروپا را رسماً متعهد به پیوستن به آن نمی‌کند.
🔹
اتحادیۀ اروپا اعلام کرده است که «از تلاش‌ها برای اطمینان از توقف فعالیت‌های بی‌ثبات‌کننده ایران و ورود آن به مذاکرات صلح با حسن نیت استقبال می‌کند؛ از جمله از طریق فشارهای اقتصادی بیشتر و عملیات «طرد اقتصادی» تحت رهبری آمریکا» و افزوده است که «به همکاری نزدیک با ایالات متحده و دیگر شرکای گروه ۷ و شرکای بین‌المللی ادامه خواهد داد».
🔹
اما در هیچ بخشی از این بیانیه گفته نشده که اتحادیه اروپا، آن‌گونه که بسنت ادعا کرده، به این عملیات پیوسته است.
🔹
بروکسل هیچ تحریم جدیدی اعلام نکرده، با فهرست تحریم‌های آمریکا هماهنگ نشده و تغییری نیز در نظام تحریمی خود ایجاد نکرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/460207" target="_blank">📅 03:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6yrFrNJNA3JT9lrhTnDIEqzLPOcBzVtfXYT38havYZfVl0FJo1_uKL-VvZDqF-HQTOA5z2uSRmTpnmzPkRII-EfhQkqEIMopLLRxMedi_gTkKMHQ4N71rxvH62PdBdwuKUwOhWzf72mfggVaRJMEAPXGpoiP6m7waMG7tnVdzMAxvul3K9qpcpyVuhA2Dzx8DPSsI-IdfrrmvQiOUrM2pR3E85opFEcuhhsTVeSGOpktA1y8l_xvd5TXu5fRGhWPNkKc8eKynG2kpraWWvn-GVTg69yFk5tZDajRtMqIqVtlKMj5LdWOc--eRu5iydk1xTbxeZ8fOzH7pMx0X0IEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عموی جدید سلطنت‌طلبان چه قابلیتی دارد؟
🔹
سلطنت‌طلبان هر عنصر آمریکایی که عناد و دشمنی بیشتری با مردم ایران داشته باشد را عموی خود می‌نامند و حالا نوبت به «اسکات بسنت» وزیر خزانه‌داری آمریکا شده که محبوب این فرقۀ تروریستی شود.
🔹
این رفتار سلطنت‌طلبان در واقع چیزی فراتر از حمایت از یک سیاستمدار آمریکایی است؛ آنان با برجسته‌سازی و قهرمان‌سازی از چهره‌هایی که مواضع خصمانه علیه ایران دارند، به اقدامات ضدایرانی نوعی وجاهت سیاسی و اجتماعی می‌بخشند و آن را تسهیل می‌کنند.
🔹
وقتی یک جریان سیاسی، تحریم‌کنندۀ ایران را «عمو» می‌نامد و از مواضع ضدایرانی او استقبال می‌کند، عملاً این پیام را مخابره می‌کند که فشار بر مردم ایران اگر در راستای اهداف سیاسی این جریان باشد، نه‌تنها مذموم نیست بلکه شایستۀ حمایت است. حملۀ نظامی و تحریم، ابزارهای آشکار خصومت هستند؛ اما مشروعیت‌بخشی به این ابزارها، لایۀ پنهان‌تری از همان پروژه است که از خود اقدام خصمانه نیز بدتر باشد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460206" target="_blank">📅 03:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKaziMcuxtuJRgRQs5Utiv1_1605i2bIBimyxgtcML_CoCgn4AUFTiDtTmrpsN0fQIwAPkzXByDoO25XW59BBfjsxZzfF7IotAF_LLOG0W4nijykWKVrpbbnzuDOCllLPLfG9S-1wlvPMj94PlvwIQqok79g2o9cj8FYpSPNn35m-zhwEBeWV_yI8__uk9K7rlcXOz-87hOJvgO8i3gWXsxLIS_o9xXvVMaNqgFe5hdA_Tepf5V3Gb8-eMWe0cWE_5Z4NLt8XTmjPm9dHJsvBzi0-TttfRivvXlJNVLven_h3Bq9u67bPzngNWQ8jvGN5pHjk3cl6Fz6iBXqd7-CfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاشنه آشیل پرسپولیس در نیمه‌های دوم
🔹
پرسپولیس در حالی پنجمین بازی خود در لیگ برتر را پشت سر گذاشته که یکی از نکات نگران‌کننده در عملکرد این تیم، اثرگذاری پایین تعویض‌های مهدی تارتار بوده است.
🔹
این موضوع در آخرین مسابقۀ پرسپولیس مقابل استقلال در دربی ۱۰۷ بیش از هر زمان دیگری به چشم آمد. سرخ‌پوشان در شرایطی که با گل محبی از حریف خود پیش افتاده بودند، در ادامه نتوانستند برتری خود را حفظ کنند و در نهایت با دریافت گل تساوی، به یک امتیاز بسنده کردند.
🔹
در واقع مشکل تعویض‌های پرسپولیس فقط به دربی محدود نمی‌شود. پیش از این نیز در دیدار مقابل تراکتور، تغییرات انجام‌شده از سوی سرمربی سرخ‌ها نتوانست مانع شکست تیم شود و حتی در دقایق پایانی، حضور دانیال ایری به عنوان بازیکن تعویضی با اشتباهی همراه شد که در نهایت به ضرر پرسپولیس تمام شد.
🔹
در مسابقاتی که نتیجه با یک گل یا یک موقعیت تعیین می‌شود، نقش بازیکنان تعویضی و تصمیمات سرمربی روی نیمکت اهمیت ویژه‌ای پیدا می‌کند؛ موضوعی که تاکنون در تیم تارتار چندان امیدوارکننده نبوده است.
🔹
حالا یکی از چالش‌های مهم سرمربی پرسپولیس در ادامۀ فصل، پیدا کردن راهی برای استفاده مؤثرتر از نیمکت خواهد بود. اگر قرار باشد روند فعلی ادامه پیدا کند و تعویض‌ها نتوانند در لحظات حساس به کمک تیم بیایند، این مسئله می‌تواند در هفته‌های آینده به یکی از معضلات جدی پرسپولیس تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/460205" target="_blank">📅 02:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsFnUZVTF9mQJWfPtXW6MDwB9B0XiAIayr8TJgTDjqZepo6f9dFw35NmR9Gpdt1DLwtvmE0lXYrjaQheb9lO-Nrjv-j7ca7iKl0MuJ2JF3Br5BkzP5ySEMabOuXPYgDM95y0TrAfIamgsAnJWGHxfxztbGWeHrUd9H1PxXi8iD6CWEVEfeE3OsW7ATWfp1BQ3XZ1xV7djqMuMNtlHKB3oDWz6y5xOEqDqUIDz7UZQM7bHDnrltQY55eVgQi0_AGFv4HDmXB-JGg9llHH1Uc-j_BreGsO0Jagcn8s7h-Y_S7znbm5O86qlm9R86sI2OojQkQD35YXPmO0ME6XWsx8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زباله‌ها در مسیر تبدیل به سوخت جت
🔹
یک شرکت چینی در حال توسعۀ پروژه‌ای است که می‌تواند سالانه بین ۱۰ تا ۵۰ هزار تن زبالۀ پلاستیکی را به مواد اولیۀ مورد استفاده برای تولید سوخت پایدار هوانوردی تبدیل کند.
🔹
این فرایند با استفاده از «پیرولیز» انجام می‌شود؛ پلاستیک‌ها در شرایط کنترل‌شده حرارتی تجزیه شده و مواد هیدروکربنی حاصل، پس از پالایش و فرآوری، می‌توانند وارد زنجیرۀ تولید سوخت هواپیما شوند.
🔹
این طرح هنوز در مرحلۀ توسعه است، اما در صورت موفقیت می‌تواند راهی تازه برای استفاده مجدد از حجم بزرگی از پلاستیک‌های دورریختنی و تأمین بخشی از مواد اولیۀ سوخت هوانوردی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460204" target="_blank">📅 02:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460199">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlndK9QIuqCXOicgc2LQLprMTm_fT_Bdlma655Q5sn02Q6BDTJ4PQUoYKc82ciX72ZHjaI5IW8acnLKvq6GsFV98xQlnp53EWv8IWR2KmT1E96q97cuLnPqKthq-bfRK9us6RfImr8OE8wJna2WmbijDBb-RDpIJAiKv9GAMvNli5UAG0el6-EdJdGI0g-F2dD3fOUddXdsgqyHOfjyWHgpspCcorynkwGbGx7u6N5wCatpE0SnZcZ2QSVZtTf_yfJDgR-tcuafZ3KBr1WEuvNB40IZXWd1X0G6e0BXnzyWMG8tXa9_-1zEUULs4oP8YCtoGwhOEhhgP06EMN7-qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SN9TgahFZ8pmfB-Nzak3Fu61LGP8GUgPNCc6yFg88opq9xZ9deqZ9agrMUOTCoKEgKa6qirXOsoZTROHqCvGbjAoPZrMm1AagNfFB-lJYZ8cX6XEIhi5JR79SphpUyM4NK1kQbyzR7ssNMUM-hpnLKs1RjfbUDYUoDgECJS_60llG6fajc7OeDSvuvOjxVGXTX-W7r_lWVwy20IpZDsnbPBj_5idr7zLTzCjspAW8vOOQUEoEHy9q-hqPromZSd_9-5FwnY_H8fAND07xQb0gX6t9qOcWO0LpgBThp-zBUQR3NLEuMOrIayaWGlUkoPflcklW56haLaJGelkPpsg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMJXMBbkYvgsdLL9YE3NC2UGSD2deOsbd3jMkac3dSBd82WmxhrVxhL5Z2xgmVSXUGLxf3BAWdX62hdR4uijl03eXxq1t-hp_ib5cJGvlV8UjaGJN5vHz7wtPqhLtrz6POxNoNhy1nQhphROiSnhN6df4nQNe8y4le_wTqlmp3GJBh07c1xS1ieRp6Si83Udvv388PIExqHn3_ahSISfvgFES3xBh76v2IzqdORBAtqYLyIB5vR1gD6SLTHPaJE6op6NNhzuTI21rXW2Gu6TwyOdXseDnAZon315R5ZLaMmr_OtqUPzpIeBk_WlPaf2j20Z0iMkOezGXbSs3qlkFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0X7a4Q3yK1kWSYvzvUscEUajr7-nuuyfDGWr35wJHknR8VLQCcbthoFy0nAwJ5xuBHtLsSNNwFh1n-6KGVqR4788eJell-xKUr9tqV4ILpzm6DgUA5U0o0qUe3sxsMxbA0FAtQ-QT9tYPx6T--s7Rjk7d46KN5M09hPEQ1pGVtsreyQ7zQFud2Pr7dVW9SbBMh06iwkgk4TCYiKySaBF_Hli3G6-rQ259naqAz2qPHSR_HYq8QzidK-FYlnvUnb0ACCsn9MYVCU4MuwUl8EgazvqypD0rEp7rx0dbgh-dI8u2-4BbSvLND6Vq0G3qBux822L2gKnCncp5x2EupMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIy65l0vmfrxaFI_0eyr908P9jSSkoP95__VxYoWAIG4P1WANFyQQ8esZNt3UaP0YKt4ySi54PCyEHNkQYYcxtze9S6LmvQyr8qt_DW3iHlqQd99MISzRERu2pypl7yXb4GI4W643bocTyHooKVW_ERBnqnt0hkk6OceJvcf_caEoO2wVcYhtQh5Ey-gXGwfc3HS4GMPsjGQS0Sz11PeBL8-4SzfqajEztwgrJUBcXE3PstEyzw3N5dfsajkn7rNjbnRKc3l5yn_s_dBYg47llmVBel8y_YlSANUTY8T7leO6vWtFimtL34A1Cm0S05sO2qq-Hq-id7B8wcqvRnNqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۱۴ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460199" target="_blank">📅 02:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460189">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfdUBZTCGEGdeQP7NrLDvm2WDGGkjAWFA7BkiG8iORVCCWnCH5hp7YjN0dks2yGMOzruzk975c8-KLYdTzL_R9wqC5S4hnKVm04qqHOpfguSDcFsfIvkC1KaZ5CHUAEcHDVMhZGb8f1PoVimtEnRMOi4bIA-61jHjk9tB8_e5FWq9_CsBQ_bV7Lky8EUZBmW2KVBNr83sOUoa68X5SYPZqXyT91XY0h0IWPEFHnZA4xMNPJE6SjZKKdqWSStnYJ3uIGfCqoUT6-s0EywacnLghe-qwqJ5gu8lxEyPlYJINP7H89-ScYZVtoH8h7MVgjuqP8dNjFDddZKL-cR5jvLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmiCfNFABjKZ49sA6NO9ajhScCb7vEGJx6UifTKTn-LfJ4BKHCDYxUM7X8k2guxLI3PnnDKW66uxgCglPjzsPlFB79ZeR5QeE99sQP6MFNVtc8HS0rIZ0_xjKTNpVrv9JXCxTMiiBm4kQ_SqSN3ZiK_dsc1aXv4RmFolmkqPyDICsHRlP-RBEvB_2p7Q4NYYntmhRcR7NcF3KJDw9WgNv2BDrThpuw_cvNiogLtLZ0am9k6zA70pxhDWfe82jhbf3pDydIzd3gkhOhoUGhdeZGJfsRi0BEwmjU1bJA57j26sdK3mrlS7Husc4qLjflaWOG1jwhwNzddFCg8FMk44uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WBRPi3jX5oHTwF8n8mL6fXJBYUf62JOrNMXiNbTPcwriHdQKhSIloBC1moq4EiML6dFTwHXB0Y1zercL15thmrQNh2Dp07saa9NeQfH7_NN6EqfdmSWO7NC48QIOiNUeZjPKpxvbSIrdiJx-CaU3Zk_nZAxowh71z2srcVUGq6KxW6wFIXrkvAHLeh4YIugGBe1pdAVD_VPTQpZUt0OU8w5X3xYQlBpsMwRLXw02o_UpzXn3MHov3k4SYRMSyzbaAY5CVNyDDsKPpW4EdHBUahQg3FyLnihvRrpBdEhAEKXGO_3mH6dmDorvylyNy-p89NsHqYcdc84OQq9pm2ChmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7OFpz_pkdwDyEPdeMsGNpWV99AYAlVXgkb8PE2sr335WTJQXPwXtjrqlCn1iGuHo3f5-v40SthxvaIMvltxv2HRpkcq2fwtMd71gqug3s-VQeUqdVtCyY8Y41udNBuwDiWSLUjwqRsVhtN-IzEi5-psndSrRpt5--dqiDrrrFy2JVqNOAxgT453SANdB85x74rQzWjXtTztVvhKKPP2NlT7DFYPM0UBUnF7F8cK5sobdCT7-UJpg1FUChL2mxX9QKfiOtviu6HU_BiwNkz4mQUy6CLRXj9naVPZ0NqdCqRCPNzSbPUxqSOtCCz1FAymynMzZV-9ZrgBM80KZgi8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYQBeCtCriw35rMqfrbjh3XU_2z__ND9kKgT23pcRh96De-zg8gc4qiRj0NapZ05g1fNeiQI4UHSyvst0SzxlbXwJQ3IDRpAHkLFmbgGLZl9tcEXheOlH4lJVCM2US2Lkn3H9VXjsKtleX-cqcnKedXcF2n6SINNDfbKxh8tTzN_9wgJw4vG8Ov5oxdYXHRT_gjyyOS17a01CeID1WmXA7b-eLY9-IJpTtVbmZZdVGsIGS75aiWCRacYoftwpCrsg36c-YUlZKA9PAwab-90CJLWxev69-u0W0aELcZRdnupSyNjZvpuiJkD9SWCwIClpLLHCB3NVu7VJ3gxXBDKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1PDPumZh66SsyEoykEEUnvcHoFr9vGEz7937hfZu1G_fQFyq2cSPq5iD4mGUuKkMN7Cs6DiYcyOR2OHRV4w437GkiAC5cgW0pq4Xt4V5A6t2-f85-Ce5rOP3HF9g_LUtnGkKlNJ7iXQBY0sS0QceO4tt6JTc-CQaux2IYFkub2G-LbPVxnGho--w-vaU2L-Nd7xi2NF1qmMVt8d023_g9QCmhPTwkKZRBTj-_qfFXHRNqtvTbLcG1fEoXjeq3j1KAZum6gVZ7u-4jekkarhMiSd53mipCnviZG7egeJF_geT6_1JsgYhHqqly3EoiT-F7LlS8don-p12NOcQ0gOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDW1sSZpA3LUIfyZYcO1iilH28ymfDORQPRd6OfUqT-YMNQU-DOX1IzqE8_PPbN1VViykQAtYNtgc1kcT4BZB_liu5ioHncFbxzyTw-GxC_648hX577qEka9RBPwQ9agHCdbfWS91WZQiwoCSBBrvrs2ZVu63rZi0t2sDnpcy4dkMpCoLI8mxKbuJGvIqvOt0F7V2vpjmFl5CLUtFsal9JaBofAd0uGL6qyz87wF9fmzwZtoUQeqhVpskxlgm72ZWl2Pl6XjsDgXz649Cfpnn2DUsQctnp_0fEYseccQZVwVNdAKNswhBslKqX3REjlJv6_--ce-7Vdeaq8GQdrMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XArIKC9FyJ03t1VU2FcYUZ2k9_x2O01i6GXVefzmgp2P9dmeNzSclzko-7vVs5uIe8rlY7lRXQKv8lCyibSU6gmneCT16o0Ng30BhpqM9ls_GpEEwlXIUf13yMsIyxnYS1Xr30YowTsnNT0TiYmVzjZMquDrdF3vcI-AE4tToIktYejqAgwYY-kMCaD2bRNlQNZufoIN9HtG7-BUKtxRoS3iSVoeEU8yRNNn9Kg-r-981QdemA-WPqCCpKTXx_e-neLtmhpYagvioJ7eQiy6Nl09W3aUNd19wC6wifQfGd9Di46VsvXvTWDVvZXGXrc4-S3OlJ4_JepvFsDI501O1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3DqmU6x18HYuBczpe2VPNcrTZFmTrczPCm4aofthvzBCqDkg13AaUt1KrHCtYOUPYNFr4Ih6jk58Vw3L-EXopbsFneA9V3uiQg2z8rbKqOrt5GOrxQ7aI9fuEHmCT1HSpS5892WX9ywkLjvqj4qXAfXgWO_kox-b97BF_l9d38TJoutiDfMnNLN3wGwHz6LK3_6NfCQ-1BsPeqo9Pc6FzHK6SY5_1Zxejm6Lcz-owsgFIS-pTJwTCa9lux_BdvF234D_G1jjlt6DjRnfeau23qFEe_2Gfy-a7QUyak4bn_wwyW8zdVBobXQglH8lG8dqui_c1Yk94wt-4wh6BRBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0i-yFzxcq5AJOF3IR1_Nj9Rxr95_j-yiZv-R-3CFqL0IHYrucJp-073mf-0kpsiKdrsQKfv-qpdBYC_YrofWYMwC8tgVTR_Xw8psre4lkMYNpbVsKGY6Uz6f_XDkhCnfHRoAhTCq5LMJyzgCNsIYsMRTrHveSWLk4rkyfo-w93cJ9BrlyBKXGMYCdgf1PsKZ8LdIcTSD-j4tbrAKR6BnrYZ0R_yvMAln-PRn_PkQMaWUXn4c-DBtnqJtmJqf-eAVQHhp7X0YFoY4ckBboitIwqCI2EwzyOFfse8Px6TOKPP_ybiZu_18T_9hASws_SgBLCPPrug02m7WWO8OQeAjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460189" target="_blank">📅 02:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460188">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پیش‌بینی وال‌استریت‌ژورنال از شکست پروژۀ جدید تحریم‌های آمریکا
🔹
هفتۀ گذشته، دولت ترامپ آنچه را «روز D اقتصادی» نامید، با هدف وادار کردن ایران به بازگشایی تنگه هرمز آغاز کرد.
🔹
روزنامۀ وال‌استریت‌ژورنال نوشت تجربۀ اعمال تحریم‌ها و فشارهای اقتصادی غرب علیه کشورهایی مانند کوبا، کرۀشمالی، ونزوئلا و سوریه نشان می‌دهد واشنگتن برای وادار کردن تهران به پذیرش خواسته‌هایش با چالش‌های بزرگی روبه‌رو خواهد بود.
🔹
این روزنامه در ادامه نیز نوشت، تهران که کارزار آمریکا را «تروریسم اقتصادی» نامیده، دهه‌ها تجربۀ مقابله با تحریم‌ها را در اختیار دارد.
🔸
طبق این گزارش، تجارت ایران با کشورهایی که با آن مرز زمینی دارند افزایش یافته است. ایران همچنین یک نظام مالی موازی کامل با چین ایجاد کرده که سیستم بانکی تحت رهبری آمریکا را دور می‌زند و توان واشنگتن برای اعمال و اجرای تحریم‌ها را کاهش می‌دهد.
🔹
جاواد صالحی‌اصفهانی، اقتصاددان دانشگاه ویرجینیا نیز گفت، اینکه آمریکا می‌تواند درد و فشار ایجاد کند، یک واقعیت مسلم است. اما احساس من این است که این فشارها باعث نخواهند شد دولت ایران برای سازش تحت فشار بیشتری قرار بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460188" target="_blank">📅 01:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460187">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQvwQCaYAy9Ficp_-37D5bdmN8JUsb6wwAOkOgaunRqi-CwsiP7u4MNxyUERlL_Lrj699LvxkhHgJaXd8QyHiQWEwfnHOUm5gA40NCZ-cjxhXBkF0jY7_cqHANTKvSVH7PwnmOkMDBRrnpQySlI8ivUwa8gdSCOQASZkkLpC5aHxqxjcspmYTNHeOSIVw4MXOi9t9LN7K8M02E2GNzX4VpAkqIKpYJHb-UeRR9BfBu07zbSoUEonZz4a7aqqKPIoYJpipLmzgTyMiyQkyzn7-DEUPNLKn_SAA_PlRJC5XLgTqERGlmF9dSBKOSKEv5beyEEJsBtvXdwJ2DXzU9Kxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار ایران به کرۀ‌جنوبی: اعتبار خود را فدای آمریکا نکنید
🔹
المیادین به‌نقل از یک مسئول بلندپایۀ امنیتی-سیاسی ایران گزارش داد که کرۀجنوبی نباید منافع و اعتبار خود را فدای سیاست‌های تجاوزکارانۀ آمریکا کند.
🔹
این مقام که اشاره‌ای به نامش نشده است، گفت: به کرۀجنوبی هشدار می‌دهیم که تهران هرگونه مشارکت این کشور علیه ایران در تنگۀ هرمز را به منزلۀ مشارکت نظامی در جنگ تلقی خواهد کرد.
🔸
دفتر ریاست جمهوری کرۀجنوبی روز گذشته در واکنش به فشارهای ترامپ بر این کشور برای مشارکت در جنگ علیه ایران گفته بود هنوز تصمیمی در این‌باره نگرفته، اما شاید «یگان‌های جستجو و نجات» به تنگۀ هرمز اعزام کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/460187" target="_blank">📅 01:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460186">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۳ شهید و ۲۳ مجروح در حملات دیشب اسرائیل به جنوب و شرق لبنان
🔹
وزارت بهداشت لبنان: در پی حملات هوایی دیشب ارتش رژیم صهیونیستی به مناطق جنوبی و شرقی لبنان، طبق آمار اولیه ۳ نفر شهید و ۲۳ تن دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460186" target="_blank">📅 01:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460185">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0646001051.mp4?token=iy-AGqCrvRRzoLkA0rfN3UCOqmWPPSCzrAWJVDBL7eo_5u_uAUM55RzF4_oJ5RXuhOz0YRzXQ6hXYZiP_ivLV9uJIWzYsOogTIXHEVuVFcKdObImIPGcnQ8pj_cQEtkTfyz6TItbrEMkeSAnc2aPKal6xcLy8BGEptcCCb1nvhgk0C3_jQclZJ1x48O2B_W2dCwx9AEKAHdyEB7Btdf9TdWbJSTjSPHaqJVw_Gx6OetDm0JrXJXXoeoRxmdOS-MRXF8Ap2kZYdEfJjnOKMf6YeNr5CSq8s-437xpQunjDu8eARQkvfkR6KsZtm94gQDJ7hg0nklVePVCTznROpQZoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0646001051.mp4?token=iy-AGqCrvRRzoLkA0rfN3UCOqmWPPSCzrAWJVDBL7eo_5u_uAUM55RzF4_oJ5RXuhOz0YRzXQ6hXYZiP_ivLV9uJIWzYsOogTIXHEVuVFcKdObImIPGcnQ8pj_cQEtkTfyz6TItbrEMkeSAnc2aPKal6xcLy8BGEptcCCb1nvhgk0C3_jQclZJ1x48O2B_W2dCwx9AEKAHdyEB7Btdf9TdWbJSTjSPHaqJVw_Gx6OetDm0JrXJXXoeoRxmdOS-MRXF8Ap2kZYdEfJjnOKMf6YeNr5CSq8s-437xpQunjDu8eARQkvfkR6KsZtm94gQDJ7hg0nklVePVCTznROpQZoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پسرِ شهید به آغوش پدر جانبازش برگشت
🔹
در پی حملۀ دشمن آمریکایی به جزیرۀ لاوان، شهید دهه نودی «مهدی بحرانی» به شهادت رسید و پدرش نیز مجروح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/460185" target="_blank">📅 00:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460184">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofAmOzagg2l4fxGf9sWA7Dpm-RWWd1foTbHRzHpB_og43cwHNkVFKouYHHHbfw-3SI3th9AZCreZSnKLrCiCNyJ5g46SE3LvafLVG0QKoHti51f1wm9Ric9cJhf28dW2sMoirglHK82cizWgMlbCdgpuBuATStWIMWv_aoFy71y4tXlfv7enZLMtvDYUSydv_0TgHJzIdH3VqVSgMst-0zXddQ1lgAPyiRJ1vEhIOJfNIYKBqvvV1Q1eBMPSduOH4wauKpOVJjge2MNmQNvZ6qCB8P_BigFRalnNc6-cs_4qD3iEAeJeNDvgnKYV7T6div4D6NWsTcje2HeaYHGZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون از ترس ایران ردیاب‌های تبلیغاتی دستگاه‌های نظامیان را غیرفعال کرد
🔹
پنتاگون در بحبوحۀ نگرانی‌ها از حملات تلافی‌جویانۀ ایران، ردیاب‌های تبلیغاتی تلفن‌ها و رایانه‌های نیروهای آمریکایی را غیرفعال کرده است.
🔹
بر اساس گزارش‌های منتشر شده، شاخه‌های مختلف ارتش آمریکا شناسه‌های تبلیغاتی دستگاه‌های الکترونیکی را غیرفعال کرده‌اند، زیرا نگران هستند داده‌های مربوط به موقعیت مکانی بتواند محل استقرار نیروهای آمریکایی را در اختیار ایران قرار دهد.
🔹
پنتاگون همچنین از نیروهای نظامی آمریکا در غرب آسیا خواسته است استفاده از خدمات موقعیت‌یابی جغرافیایی را در تلفن‌های شخصی و دستگاه‌های دولتی، فوراً متوقف کنند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/460184" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXIHHdx0-GsoD6CosMyqnxuIFBS6wgJKjHtGqPjQNoaSH4845YQSxXER7yDpfMowXyAn3eO8Q62Z-WD8uqK74gINJIRmMoSZ95idZxoJkwSpnYENphSSR6Bq-aEyt16tvPvsqHrn8htnEpzaaM1yyRkY3SDlIAM7JNNAw6C9vBLnbfYGbckBBrLXZJlUyPOC3vDhoPVYGYEL4BHDYscwgcz3Eh3XVg51YWtRnILV5vX7yZYl0qk33JmbNx2JX5y6dDgROSNs1hFXQWFrfqufigi3-qxQc35nu9crTC5db_WCrrL4CT6BQI0wjJIyoAa968j4CDMaHNvDOXXmnoMi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقایی به مردم آمریکا: نگذارید اسرائیل هزینۀ جنگ‌هایش را با جان و مالیات شما بپردازد
🔹
سخنگوی وزارت خارجه با اشاره به مقاله یکی از رسانه‌های اسرائیلی که در آن پیشنهاد شده از دانشجویان بدهکار بانکی برای سربازگیری جهت جنگ علیه ایران استفاده شود، نوشت: آمریکایی‌ها، لطفا فقط یک سؤال از خودتان بپرسید: چرا باید به پسران و دختران شما وعدۀ بخشودگی بدهی بانکی داده شود تا در ازای آن در جنگی بجنگند و کشته شوند که اسرائیل خواهان تداوم و گسترش آن است؟
🔹
اورشلیم پست آشکارا دقیقاً درباره همین ابتکار بحث کرده است: استفاده از بدهی وام‌های دانشجویی و کارت‌های اعتباری جهت سربازگیری از بین آمریکایی‌های بدهکار برای اعزام آنها به جبهه جنگ با ایران!
🔹
این، یعنی جنگ دیگران با استفاده ابزاری از جان و مالیات شما!
🔹
اجازه ندهید شما را به پیاده‌نظام جبهه جنگ و پرداخت‌کننده صورت‌حساب هزینه‌های آن تبدیل کنند؛ همان جنگی که هرگز انتخاب شما نبوده است.
🔹
اجازه ندهید فرزندان شما را به مزدوران جنگ غیرقانونی‌شان تبدیل کنند.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/460183" target="_blank">📅 00:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8ac924a6.mp4?token=Spo7-sz4Pbdvkzj6CwESCwF4erg3F25aTT_Z6u80uXJFQnVx9T6i5CbU3ZIlOuz-l7rju7jVyDKuNhGWbmbsfESUwxn6bkc9dgwSc2zfLIK7oTRLWaQFKQlil5Qs2lg1eV3Zyotlj2VYyYq8JjtDRpfKuY0kt85EgY3UROmFk87oIrZ6apDhlML7IwH5ddajOHlWx0FzSKsh-88FRw3q1XkxKq_3JXGPSkgAVgGpmQSIeoX5ijocSjvcQcJBYqWg06oIZDTPgpMSpt3GikuGNRYNgVz4x52xvvQ_dBwPJuIE5oBZd6GXbeFqQRW78957dQqnj6C1A_eaf4zfEpm4Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8ac924a6.mp4?token=Spo7-sz4Pbdvkzj6CwESCwF4erg3F25aTT_Z6u80uXJFQnVx9T6i5CbU3ZIlOuz-l7rju7jVyDKuNhGWbmbsfESUwxn6bkc9dgwSc2zfLIK7oTRLWaQFKQlil5Qs2lg1eV3Zyotlj2VYyYq8JjtDRpfKuY0kt85EgY3UROmFk87oIrZ6apDhlML7IwH5ddajOHlWx0FzSKsh-88FRw3q1XkxKq_3JXGPSkgAVgGpmQSIeoX5ijocSjvcQcJBYqWg06oIZDTPgpMSpt3GikuGNRYNgVz4x52xvvQ_dBwPJuIE5oBZd6GXbeFqQRW78957dQqnj6C1A_eaf4zfEpm4Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان ارومیه امشب با حضور مردم نورباران بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/460182" target="_blank">📅 00:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da596b0154.mp4?token=D0hsqXoD5-XUWWTjmZSTprqW-HVedW-oEhw22lk3NehoydNwwQv_jwAp61Q6Z2vpUxcxqyMAiiNrk7oi6JuZpokcubMqm2AjiUUe5WQe6uNix3YDVeH2kppTpdJdbEFzkdaLZC8GlWTljJq3UZCZoAfDq9yurhBb8A-hZ8mhcKnjgYvoUfQb5D9a3yYoi2baERRst_Dr-p1HAiAgAGnD6bijgMznRyes0bgklz4mTvPZUTrNyOo5m0nom-DODARWu5Yp8lpbs_9PfG-qb6FOEECwhsq149xbJ1ooMvZ7Ief5SV1go7OisBVXD7dy66YKCFIj0zer337xLBRLl-xePg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da596b0154.mp4?token=D0hsqXoD5-XUWWTjmZSTprqW-HVedW-oEhw22lk3NehoydNwwQv_jwAp61Q6Z2vpUxcxqyMAiiNrk7oi6JuZpokcubMqm2AjiUUe5WQe6uNix3YDVeH2kppTpdJdbEFzkdaLZC8GlWTljJq3UZCZoAfDq9yurhBb8A-hZ8mhcKnjgYvoUfQb5D9a3yYoi2baERRst_Dr-p1HAiAgAGnD6bijgMznRyes0bgklz4mTvPZUTrNyOo5m0nom-DODARWu5Yp8lpbs_9PfG-qb6FOEECwhsq149xbJ1ooMvZ7Ief5SV1go7OisBVXD7dy66YKCFIj0zer337xLBRLl-xePg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع مردم بهمئی با پیکر تکاور شهید در زادگاهش
🔹
ناوسروان سید مالک موسوی‌تبار در جریان حملۀ اخیر دشمن آمریکایی، در حین انجام وظیفه در خوزستان به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460181" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOWsu4C-3RoGaz3j1UO3LbC06JZOwLT7p4ufFz6DJAhkjsrGqjwrHeHQ6fc0hVC8nf5hrnnPfzP_f5mv6KnwAu3xBcOVV7LHb1O0J5lQMueWeGRAktRoC-zgMiz83IcHttJSUTgU6MCRFLKhmCNUTa2unBNV5K_pvN5cj0jjvSvVMHPfyL2iRdPlU66TLADIK7-LxjNB_b_MARdN1FdhidDPIo-oZV3A2KHMpljcVbujrxdgv-r0rqoj_UUEe_c7-G3ifuajyJjBZYFHHh4Jo9Kmd6Zf6tUCzR1odwoEBfuWOtzSDFWpsSDud5ErSAr-lKNvc5JWA9HUoFaFLRepMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوخو۳۵ با این سامانه جنگنده‌های رادارگریز را پیدا می‌کند
🔹
جنگنده‌های پنهانکار نسل پنجم به‌گونه‌ای طراحی شده‌اند که امواج راداری را بازتاب ندهند، اما نقطه ضعف آن‌ها حرارت تولیدی موتور و اصطکاک بدنه با هوا است.
🔹
سوخو۳۵ برای غلبه بر این چالش، به سامانه الکترواپتیکال و جستجوگر فروسرخ پیشرفته OLS-35 مجهز شده که بدون انتشار کوچک‌ترین سیگنال راداری و کاملاً غیرفعال، امضای حرارتی اهداف هوایی را شکار می‌کند.
🔹
این سامانه با بهره‌گیری از حسگرهای حرارتی با تفکیک‌پذیری بالا، پرتوهای فروسرخ ساطع‌شده از جنگنده‌های رادارگریز را از فاصله ده‌ها کیلومتری شناسایی و قفل می‌کند. مسافت‌یاب و نشان‌گذار لیزری OLS-35 نیز قادر است تا فاصله ۲۰ کیلومتری، اطلاعات دقیق مسافت و مختصات هدف را برای سامانه‌های هدایت سلاح و کامپیوتر کنترل آتش سوخو فراهم کند.
🔹
ترکیب ردیابی حرارتی OLS-35 با رادار قدرتمند اربیس-E به سوخو-۳۵ اجازه می‌دهد تا در محیط‌های آلوده به جنگ الکترونیک، حتی مخفی‌کارترین پرنده‌ها را کشف و رهگیری کند، بی‌آنکه خلبان دشمن متوجه رهگیری خود شود.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/460180" target="_blank">📅 23:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460173">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeGGQjxbj7q7k2BtOtLuMmUCgtuQgf2NAN5j6KoB33mV11iWxWJhXh_sEe3Tpov22_DWq3fTOTlAgAgbjAznd639-SNKOO7p8HrEV_gMdgiffdXZe7KRSntBScWGMui59-p-bJ6w-jWIzYOkLwPgXmVZisCbU4Q37Cp12i3VxMVEiy0r9nkGgUlpopvca9IuEIirIKk-qxX34ileFXpkpRpy_mRRIKDPflt4pYJj8Lp_-VT2TNeoS3UnzcZLx5fbSyOCKEJRbD6evFHWQ335vYlhXWLP74tGQbAY7E46UGuKNIcBkT0IwiBCBdE6sRE_BbllDx2mpA3DiDQFBXGYgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBtXR4XRowtAdxomCEU6ZHDrLP33OB2qqZhjcEuSki9BL0h0NPyhpAjYnLM2q9WJ3QatPY9LjP8ckHSB5zwF0FRfBgmjrGhLxqVzOVx28ZUwj3Xcaw3DAUh54bxKSw37KzALtutF-zdKKA8xHo9ur-lOvEFLuaNn4kKrk4eQ8niWJIlI6FRI2ju7abC_YehQ6XKhDZebe4rGNRq4j-fOSTT3qiXsrJmHiglDwC0wQVkb3mhEuCM6KqVmO1KLsfPQX9i8U5h3NZCf52MKnCik2Cc3BR_nR_YByjK_O2MTsBu-Tpt0PjI9aawOYCNfhy7ZLGyJ2NTBziUIS8KHGrEALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p75BpUipD32fSbmghevFKWBdCak78KgiPcBdpiZqTdEI5rtghv-1BsplOc7filzrAr8nMrrE9ay-15PMVjQvcMau1QZu7IwPcAQ5aBMuM5ZIvChzbjzdT1T14vBkK7AuFAz4atQrL-yyn_GqN8PHRKkWsj1fS4po6cSOrTlg-61pzOaOzG0jiNnMLnG1Af0rIinfINDUhqw6UPc2v3z5kG4syctQOAAIevMKswcz1bY-XiHHrMkvYOs-lB7b9aKXbTGe6l5ovPeOI0Kp41dRlRzpiUX43E9wO_hSsxXZ6MXbyyQpxyit8eWHCN_ENMb9wpoBq_FxOptZ2V5U7lR78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DReTNqbOLofCNduqim090c4ZhGJywIUjL7PvlMei7Cg5GtiCh5zQDUbUO_RzR6QlNdbSr4xaN5bTDo5auAELzhQYX7NrEZzmses5IZy_2M47KuTZSSsEQzVRHUW4VCyVfiI1IDTb3lg2vJ0sxkhgvyJXXVIwwwAvsoP54uxdcnGUXz_5PShedNLiJLGf3mMTjtM2xWDA7lnEQQ5dFhyuuXBheQ1xrr6kWXiOxLTzGmTHU05VWTYGd7buE8l6WmtNzSl090gyab1jc01SusEU9fRNYDygczrgi8P7o5Yd3fLOWmEq_X1JjyGK07PcQDubU2gzLuj8QnZYNDVlW8AcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pz1ubGIA96Lh4IxUVDGHQbw1XCMFALLisE9nxZdc1gJzNsS_qaKqCj-oeO337kr5aJdD9aG15JUF-u7v35u31eAiHAbkLKWyxIKh6lwQbB-iCLDyo_mYEjfQuhU2ujesrQPRdgeELTnBZV6YM1rQ9SInMMBIW6sK24_itlEhBeQ4l8cwB-ViyIXW18XVNASpWTAPKOYHf4EDEYdfscjbFwSkcMHL9Hmd4w5ZeTpR0u1TOt9w1_-f55BW4VbeFk7yFftseqbLgSCR3yAdiEEKWuiMXWaIfpvYzoFXn7aqg2K2LNYNjIZDv44qAmlVs_p2_rcH__QJzmIzFvGm78neWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORhog7bsdvf_uHpeaUBMrS3iw3yuVBdxePxrB10SD60HvBZ3LXwXLG8ymvB2uubprYVXJBbCFoCWgb2nuxNsANnz-qSs_GwD13_FEWMVVaLwUD-G28FRI7IVlInRia-iJkx5E51NLNNR-O64VG-ebJFS9RKUR63Uc02gwY7n3JrbZuzObW4ErLSTP05EsWngG_haKzlh-05oRk2DlJNBVXj0aMZ6ksklk74q99bzrI8XJd5oAjHLDemOfA6Zf3e8B2oxFGh23zmMT7P6wA26chfvF5gX4NeWIMWijqrDZ7dnHn6BQ0bqtBT7IOdBIcFN2zlDQdgfBsTMQhJGIdvfGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRaYu86UpeZ9PHvjUI_kBHnc92eZ2U3SiS3OMdaMN82TFcMUgGQGOo8QLVdZvQaNipUJ4u3J4-cuPJxfD9s9H1okDxk9F9rPJ6nnQhQmESqUgcNdWnoRUPsiMDHaPCTiO33i0jevaLsuqSTIVkBOqpp8FUra5zbpjIMkoKPt4jv9EGb23GJnr-kDYOGUC28tZilX1ztNAIIbsHX60tSjks25CZPh8gSQY8F5yeM-oB3EfoYM17s0yhrvSb4cfn2ec4h0PG1-5KcK0b5eQU3TQGM7SO9WaqYkoLnXsAkJkYR1daNpETz9GbkYIDLZ7cmF3YJFBnx64RqtMMwJ1yofOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع ۲ شهید حملۀ اخیر ارتش تروریستی آمریکا در کرمانشاه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/460173" target="_blank">📅 23:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460172">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93759ae0e3.mp4?token=BDiFr2rTcfoH5WVz4escVSYWRkQ6qs-T2FlfDNrLSn-U5fnxgg7bFysfQF6Lh_bwqPzv_Nh2gJzha508d0lSXx64kYJbbHwD0KCh5w6z5SaHAk_xVNeAYOu7cChomosYMyDvECpJTcJyqHgTa63yB4BPwMvWKxTJfz2RYo8nMzMr_6iVu4m-w16B03scJ5iRsXI_7iYlazPcyyTT6nsA23AzM8j_IrDK4c_HIGuo3qCJp33BJnmlPqLu6oqgzD4IsoI-x81BCK0CCmhaeHWilCoTlaQl_N8yDvqBWbia6GOBHpwH93HkT3NSt6c1fS9nlRKglU3Jhevu-aBXdDbicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93759ae0e3.mp4?token=BDiFr2rTcfoH5WVz4escVSYWRkQ6qs-T2FlfDNrLSn-U5fnxgg7bFysfQF6Lh_bwqPzv_Nh2gJzha508d0lSXx64kYJbbHwD0KCh5w6z5SaHAk_xVNeAYOu7cChomosYMyDvECpJTcJyqHgTa63yB4BPwMvWKxTJfz2RYo8nMzMr_6iVu4m-w16B03scJ5iRsXI_7iYlazPcyyTT6nsA23AzM8j_IrDK4c_HIGuo3qCJp33BJnmlPqLu6oqgzD4IsoI-x81BCK0CCmhaeHWilCoTlaQl_N8yDvqBWbia6GOBHpwH93HkT3NSt6c1fS9nlRKglU3Jhevu-aBXdDbicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور امشب مردم کاشمر رنگ‌وبوی مهدوی(عج) داشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460172" target="_blank">📅 23:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460171">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd179be9d.mp4?token=fb9to_RcM6GSpL5B5uxwAFlh1M_4mo7qzJUrWHneaOhspBBUenRelcxmLqlWcvj849BNi33RPZt4JLGZ1mK4F2iXEbf9ZHxShrVdXYSp_IIbjOD64Tr8fwVtb70sMp-l7xjWGDjrEKD0QdYr2CsLdvUzk1YVO7Gw-mnx4dwuaVZaCp3MhqpII1CY5mtb_jiDIkHv6n4qyRbCXNbj2q1S28MqfzpRRsDXtcCBbfUfBr5rh-UMNQPzHul9z27IBMFHBh3LoxirbwpqMTZ4uC_IX7nFrNvziuu69VolnIRgEN5ATfMmVCJekhTJrhSWcD1w_hcHfHRmIj6lTe8RZX-hiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd179be9d.mp4?token=fb9to_RcM6GSpL5B5uxwAFlh1M_4mo7qzJUrWHneaOhspBBUenRelcxmLqlWcvj849BNi33RPZt4JLGZ1mK4F2iXEbf9ZHxShrVdXYSp_IIbjOD64Tr8fwVtb70sMp-l7xjWGDjrEKD0QdYr2CsLdvUzk1YVO7Gw-mnx4dwuaVZaCp3MhqpII1CY5mtb_jiDIkHv6n4qyRbCXNbj2q1S28MqfzpRRsDXtcCBbfUfBr5rh-UMNQPzHul9z27IBMFHBh3LoxirbwpqMTZ4uC_IX7nFrNvziuu69VolnIRgEN5ATfMmVCJekhTJrhSWcD1w_hcHfHRmIj6lTe8RZX-hiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«حضور ما نقطه‌زنه، تودهنی به دشمنه» شعار امشب مردم کرمان بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/460171" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460170">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
منابع لبنانی: ارتش اشغالگر صهیونیست به نقاطی در حومۀ شهر النبطیه و بقاع غربی در جنوب لبنان حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460170" target="_blank">📅 23:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460169">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f799ea13.mp4?token=PtD-1Ieit6pShFV5FqbrZi-ys2D3ZSF45S2c1Fq0G8kuzxUPGIMC6IuOS8LKMOO10L7TAyp_cfEzOprxD0jC6RZneDqiKY0oOE82Uto5zNcSpfYNAnpH-Vhfl_-BYK078QN6SX40Wlhl9xaovEFiUA2rQFl-x1_LnxiCn2RfoEeYV52xD9cQFeSwLd2_wH2t9_SPU18dJ-azUknrMVioOkyxjdX8Cw3J6hBgFj_4z7tAfj_YHP99tcMk-hxu-rxgABxDIRLp2l1AhcBEgx8fdTzvGizIvma5wjoNqX1RJz86MtI2_wIGc5Vq1X-0iVKFdhE-6sAXR-hDY5s6BeK4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f799ea13.mp4?token=PtD-1Ieit6pShFV5FqbrZi-ys2D3ZSF45S2c1Fq0G8kuzxUPGIMC6IuOS8LKMOO10L7TAyp_cfEzOprxD0jC6RZneDqiKY0oOE82Uto5zNcSpfYNAnpH-Vhfl_-BYK078QN6SX40Wlhl9xaovEFiUA2rQFl-x1_LnxiCn2RfoEeYV52xD9cQFeSwLd2_wH2t9_SPU18dJ-azUknrMVioOkyxjdX8Cw3J6hBgFj_4z7tAfj_YHP99tcMk-hxu-rxgABxDIRLp2l1AhcBEgx8fdTzvGizIvma5wjoNqX1RJz86MtI2_wIGc5Vq1X-0iVKFdhE-6sAXR-hDY5s6BeK4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم محلات استان مرکزی به ایستگاه ۱۸۸ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/460169" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460168">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61d130790.mp4?token=cHHrEG5XQ-z2qz9lWgdGWeU_muhNf50IdVbBeD4pZfXGl_zwinXbz95AT8Y88J9wUAqaxEo9Qivey1Tr9wqZO2Kd7aGmGR5HItpsbcjVYg7CAdhto9pN6aMraej0pZtp0Zcp0aaB0Lf9Xo_O-peDHEbpMIH0uABiOcQEq9XGw_leAEANn5hep9ZFmb0yqAcl2F2hP4JU8jJmDvMiDw4ocEHstrO6SgGhOCah-J4OXp9xaGRmOtxgiKIIHNiQ4DLMlB-HdTGUS1HlLe84KmgDQ76OgBkvybFOws6jHvtbahOfJ5dU8Boml1OYyt3e3_jX0cStQ71bx3TiMvzZswNdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61d130790.mp4?token=cHHrEG5XQ-z2qz9lWgdGWeU_muhNf50IdVbBeD4pZfXGl_zwinXbz95AT8Y88J9wUAqaxEo9Qivey1Tr9wqZO2Kd7aGmGR5HItpsbcjVYg7CAdhto9pN6aMraej0pZtp0Zcp0aaB0Lf9Xo_O-peDHEbpMIH0uABiOcQEq9XGw_leAEANn5hep9ZFmb0yqAcl2F2hP4JU8jJmDvMiDw4ocEHstrO6SgGhOCah-J4OXp9xaGRmOtxgiKIIHNiQ4DLMlB-HdTGUS1HlLe84KmgDQ76OgBkvybFOws6jHvtbahOfJ5dU8Boml1OYyt3e3_jX0cStQ71bx3TiMvzZswNdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار بروجردی‌ها در شب ۱۸۸: لبیک یا خامنه‌ای لبیک یا حسین است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/460168" target="_blank">📅 23:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460167">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISnLhHUqSbRPdQZ-LsI3_PytYgMCG0mh9mwBCUrifNUsIltXx08GomGOrd3JJrSXzZMak5ihDmz0cEbrMkZ13o1ebgzu5BmO5BXoImkZ89RDORT-D4RaqJ35jwhM1IcUuYQC0qmARJPQWcoMLKpH1--aRwGxAf5W02sPJINd231AgPAnvd6oIcG7URLjRmnUg00O_jYZ34wuaMjSoAzIuYCAXX4Qm_YbW_z_ve2_94YWLJVqqkrSAs9_lXQ3AgwuFzHIHMecyvzr_kMemuVJK7fxWmx1_5T1my7kF-a8WEedCQ6M53NgJ_FGlC8RGvtkClXsysrIX57mFkvgjRQW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک جدید ایرانی که دشمن را آچمز می‌کند
🔹
در حالی که طی درگیری اخیر ایران برتری خود را در میدان ثابت کرده است حالا سخنگوی ارتش از تاکتیک جدید ایرانی سخن می‌گوید که استفاده از آن می‌تواند دشمن را به عقب نشینی وادار کند.
🔹
امیر سرتیپ محمد اکرمی‌نیا، امروز می‌گوید که دکترین نظامی ما پس از جنگ تحمیلی ۱۲ روزه به‌تدریج به این سمت حرکت کرده است که «باید از جنگ پیش‌دستانه استفاده کنیم»؛ ‌البته حقوق بین‌الملل نیز به ما اجازه می‌دهد که بتوانیم به‌صورت پیش‌دستانه از خود دفاع کنیم.
🔹
یکی از آخرین مواردی که نیروهای مسلح ایران عملیات پیش دستانه را علیه دشمن اجرا کرده‌اند، بامداد ۷ مرداد بود که نیروی هوافضای سپاه، یک پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن را پیش از آغاز عملیات آمریکا علیه ایران با موشک‌های بالستیک هدف قرار داد و مانع از اجرای عملیات دشمن شد.
🔹
سخنگوی ارتش درباره اجرای عملیات پیش‌دستانه علیه دشمن نیز گفت که ما «اجازه نمی‌دهیم آمریکایی‌ها ابتکار عمل را در اختیار داشته باشند و در چند مورد نیز همین‌گونه عمل کردیم.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/460167" target="_blank">📅 22:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460165">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266a94e115.mp4?token=uNyi1X4g5c1gCsXev_5LJ6YoMNIw1egae9Dbs7rcbwUtjOZigCvCgmH0UysTI_ZSbSyC1fU8sC1rorRlsz6tUWeYwa3_7P3fSyCoX8odsgyHarhYZOIPf8ESo-N_w2hlBpdbSwD3O2yhmeARXiBmM3VXxYBJ3RY06VK3FLw_LRfkNjhvwLtaZ_41E4joRN6kwYYQsxZKTmJRvanyeZNNN1zFhUJITB0s2eFzoSaQfczPAKmaMQspFUoka6Ed3P3cYh14cd0xO1SdH8JhYd2mKty6GjY9FheeMMHtwob3fFdgcMpM-Ci7jJsFc_jpXSBtrjDeGdYgTJGK3Zc7QPt1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266a94e115.mp4?token=uNyi1X4g5c1gCsXev_5LJ6YoMNIw1egae9Dbs7rcbwUtjOZigCvCgmH0UysTI_ZSbSyC1fU8sC1rorRlsz6tUWeYwa3_7P3fSyCoX8odsgyHarhYZOIPf8ESo-N_w2hlBpdbSwD3O2yhmeARXiBmM3VXxYBJ3RY06VK3FLw_LRfkNjhvwLtaZ_41E4joRN6kwYYQsxZKTmJRvanyeZNNN1zFhUJITB0s2eFzoSaQfczPAKmaMQspFUoka6Ed3P3cYh14cd0xO1SdH8JhYd2mKty6GjY9FheeMMHtwob3fFdgcMpM-Ci7jJsFc_jpXSBtrjDeGdYgTJGK3Zc7QPt1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توهم جدید ترامپ: ما کنترل ایران را به‌دست گرفته‌ایم!
🔹
رئیس‌جمهور آمریکا: ما کنترل ونزوئلا را به دست گرفتیم و در واقع کنترل ایران را هم به دست گرفته‌ایم. اکنون چند روز است که هیچ شلیک و درگیری رخ نداده است.
🔹
تنگهٔ هرمز اکنون پذیرای کشتی‌های زیادی است؛ کشتی‌های…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/460165" target="_blank">📅 22:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460164">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c06f4c83.mp4?token=j4KzYCY8hb8Rdb7_oUk9K3Wz58yL32wv-8riKAP2gW1L0Xu1wHgOWFGRNCcSN6J0vH-jWZfnLaSN-ha53OS7O1xyB23GmFexEfvwSFmeI4BB8oo_Lg7O1Na0prqwaEf7wgoZy7QLdWdxql-ZAPQUrcvKR2Jm-dZlkChuc27h-tMth_WKV_TQU05IZHSARMwJfiDKVFkHMFmepZc4_UmQT16aHU_jDAyvgnIKHFO9rLfOvHbvwhK4CAFBduZ4T1eErV6QC_tQrfSMEFKPyaGIsWKBsFIPtiq-2yzBq2bxGLct7kOqQ3R8jINcPdAmMu9hrH8GkpqB34wZ7Q8wE2stqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c06f4c83.mp4?token=j4KzYCY8hb8Rdb7_oUk9K3Wz58yL32wv-8riKAP2gW1L0Xu1wHgOWFGRNCcSN6J0vH-jWZfnLaSN-ha53OS7O1xyB23GmFexEfvwSFmeI4BB8oo_Lg7O1Na0prqwaEf7wgoZy7QLdWdxql-ZAPQUrcvKR2Jm-dZlkChuc27h-tMth_WKV_TQU05IZHSARMwJfiDKVFkHMFmepZc4_UmQT16aHU_jDAyvgnIKHFO9rLfOvHbvwhK4CAFBduZ4T1eErV6QC_tQrfSMEFKPyaGIsWKBsFIPtiq-2yzBq2bxGLct7kOqQ3R8jINcPdAmMu9hrH8GkpqB34wZ7Q8wE2stqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: اگر درگیری با ایران نامش جنگ نیست، پس دقیقا چیست؟
🔸
ترامپ: خیلی‌ها به آن جنگ نمی‌گویند. من به آن می‌گویم یک «درگیری نظامی»؛ چون برای ما موضوع کوچکی است! ما در مقابل ایران فقط ۱۸ کشته داشته‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460164" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460163">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2e1fb1a6.mp4?token=Dqqd_bpwUHtXBKDEZX5mKYu1txSYAq6M7wpEMq-akPgHfUrjeweWk1ipEV_m49lsCP7DzdkyuBRXbZiS27MRyyuQeHjgun7LbAkJB8lTKb4c7gVVrKIByeYDGYW3MmD59E__SX2RV5HupH8Y0Tsgn2090Ky9JRmeXfIZh5s8Jl-eJWZZ0dmfWZbkFHG53R70AWfytsERAobcHFYFmwSxT5yJCB7UtQzRKFkpbmUmR8s4_m6cfPy1tKzDkL2J5IYkJSxzA9rQtd2Pox4ODcFQXwl43LeENHuG3TC8ZEr4zJqeLPiqin8PhMRCGk7zmsT9ozKiRqkeHWFTH3u-cNHSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2e1fb1a6.mp4?token=Dqqd_bpwUHtXBKDEZX5mKYu1txSYAq6M7wpEMq-akPgHfUrjeweWk1ipEV_m49lsCP7DzdkyuBRXbZiS27MRyyuQeHjgun7LbAkJB8lTKb4c7gVVrKIByeYDGYW3MmD59E__SX2RV5HupH8Y0Tsgn2090Ky9JRmeXfIZh5s8Jl-eJWZZ0dmfWZbkFHG53R70AWfytsERAobcHFYFmwSxT5yJCB7UtQzRKFkpbmUmR8s4_m6cfPy1tKzDkL2J5IYkJSxzA9rQtd2Pox4ODcFQXwl43LeENHuG3TC8ZEr4zJqeLPiqin8PhMRCGk7zmsT9ozKiRqkeHWFTH3u-cNHSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاید آمریکا قصه‌های زیادی برای دنیا ببافد اما پایان این قصه را ایرانی‌ها تعیین می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/460163" target="_blank">📅 22:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460162">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4wvB7C9Wj0IddgJNxF1Y0JvGSTshYlpua7uRhEbn0IOQSkcRlGcAVLVHlqHlE1oVrkIP3jRGyweYlcL23q5ViBnxVpHmXn1xhZ58IZpecbXLgWMv8kKFnQDCeuzLPdYWr8PB5eNU6_ToE0EYR4k-F8yGqld3DnV2wGacrO3XYIWlu5kvl3dtupmUHlYQIO6JsdcR8gALEE6n0dI8CQ7hiA9X1gIRZ-KugezLrQDRTNyB0y0Dlg7575XMKDxM9R1bREcjGhIX14Eg0462Dpta2SUftdegXEPnTS_Bwxv0l4MioC-EOXnmTA8zQL5LWZc1PVnthctcdB8-LBRqUlG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ سال جنجال برای پتروشیمی میانکاله؛ روایت تازۀ پزشکیان
🔹
پزشکیان روز گذشته در جمع فعالان محیط زیست درباره پروژه پتروشیمی میانکاله گفت دولت برای توقف این پروژه تحت فشار بود و برخی می‌گفتند خود دولت مجوز اجرای آن را داده است.
🔹
پزشکیان تأکید کرد وقتی پروژه‌ای به طبیعت ضرر می‌رساند، پول آن را پرداخت می‌کنیم، اما حاضر نیستیم ادامه پیدا کند.
🔹
ماجرای پتروشیمی میانکاله از اسفند ۱۴۰۰ آغاز شد؛ زمانی که سرمایه‌گذار بر اجرای پروژه اصرار داشت، در حالی که سلاجقه، رئیس وقت سازمان حفاظت محیط زیست در آن زمان گفته بود که احداث کارخانه پتروشیمی در بهشهر بدون مجوز زیست‌محیطی امکان‌پذیر نیست.
🔹
در نهایت، سال گذشته رئیس سازمان حفاظت محیط زیست، از تصمیم دولت برای توقف پروژه خبر داد و در صفحه شخصی خود در شبکه ایکس نوشت که پزشکیان در جلسه هیئت دولت دستور توقف فعالیت پتروشیمی میانکاله را صادر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/460162" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460161">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cc7bfb46.mp4?token=k7age0-dQqM3eNFmfJ_DDC7uYXfHZm_XeEJlPZS3EzznONZnb1isremcc0yYGJ8qwbR966knmpR8ewWymbHku7R3fe4K_rm8uRoA4_dnCqGhRkMZtghYoJzq-BDIhF-juyGeuBftGt_vaIRpNmpxD0kDBVlT9RuywHS3Hz2BKGP7rTYR2FSNhpltzaOL5FfCkpB-xqrECvsSbuI7FtbBPeDeE6GanbKuUoL3sX49uE6OsiFjjVbRuSR38ubV-65wG4FNb_jpaek0XJyfIBCuFMEFXS6OMx926E-qyBnSH1Rsgfm320dm37RYUvPWofjg-XnwqcSixfLJszsm49qIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cc7bfb46.mp4?token=k7age0-dQqM3eNFmfJ_DDC7uYXfHZm_XeEJlPZS3EzznONZnb1isremcc0yYGJ8qwbR966knmpR8ewWymbHku7R3fe4K_rm8uRoA4_dnCqGhRkMZtghYoJzq-BDIhF-juyGeuBftGt_vaIRpNmpxD0kDBVlT9RuywHS3Hz2BKGP7rTYR2FSNhpltzaOL5FfCkpB-xqrECvsSbuI7FtbBPeDeE6GanbKuUoL3sX49uE6OsiFjjVbRuSR38ubV-65wG4FNb_jpaek0XJyfIBCuFMEFXS6OMx926E-qyBnSH1Rsgfm320dm37RYUvPWofjg-XnwqcSixfLJszsm49qIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: اگر درگیری با ایران نامش جنگ نیست، پس دقیقا چیست؟
🔸
ترامپ: خیلی‌ها به آن جنگ نمی‌گویند. من به آن می‌گویم یک «درگیری نظامی»؛ چون برای ما موضوع کوچکی است! ما در مقابل ایران فقط ۱۸ کشته داشته‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460161" target="_blank">📅 22:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db96ccdf81.mp4?token=amclsvf-TfTuWTKCvYacB_6J9nip0KYDsf4XX-kn-slEXK_Cv_wTlfrS8eTMjDdGtoH57VL2WYUEmUsjLvIDpLwx1ba5tXnjyLNHlqfcCxbiRhUoHcZU5otJwAGRHS0V_2WybofE4tiJ5aDMeJfg-DdDMpNAkjHPWjOubyyhMMcUHwCW56TlFf4MkAfKPrKpTqXry3GzQACLVLW2L85KfCqdoyUDvqnIbPfOCoEWraeD_C0rvJ9JUu_RpEEecKXKtfYTNdauiCdcdm54va6rtWegKcAhaInQJ2XtQlNXgbeKoQqpg0zAYztHBD0uvH5vCMa4QXqRGO0LU6TykPT2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db96ccdf81.mp4?token=amclsvf-TfTuWTKCvYacB_6J9nip0KYDsf4XX-kn-slEXK_Cv_wTlfrS8eTMjDdGtoH57VL2WYUEmUsjLvIDpLwx1ba5tXnjyLNHlqfcCxbiRhUoHcZU5otJwAGRHS0V_2WybofE4tiJ5aDMeJfg-DdDMpNAkjHPWjOubyyhMMcUHwCW56TlFf4MkAfKPrKpTqXry3GzQACLVLW2L85KfCqdoyUDvqnIbPfOCoEWraeD_C0rvJ9JUu_RpEEecKXKtfYTNdauiCdcdm54va6rtWegKcAhaInQJ2XtQlNXgbeKoQqpg0zAYztHBD0uvH5vCMa4QXqRGO0LU6TykPT2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های برافراشتۀ ایران اسلامی در شب ۱۸۸ تجمع مردم مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460160" target="_blank">📅 22:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4d254ab6.mp4?token=d6RsIiLWlkgvL3GVuppx3SzOOUfBkcrOEydimc4YezNsqXdb6_zqQXUBy2ZKOCUW8zsskfCH-IJHkZLi9dbOCOTsMzmCfpoNWAcsaSPrDvT9ClBZmbZ1NrU-AF_9PHmKLEAx1pLaDZfC6vBab61mYr5_I9lAsu4gDh3Xij82eQRRQ3uuFYq70eP6mkPkmK-n3cDR-9gtbXg2B2TcRsv4dPEp1EcR_oQFIzhcYOdv3iTpOiiAQmY5F6Pxz2Syzy784q4imn1in_Pm5RGkFKVko8IjlKF-wqgKOebH4ga6_xxJWYjGe0zCMFWea-fOQIOo8fXosgkzE40Vm76iC13FUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4d254ab6.mp4?token=d6RsIiLWlkgvL3GVuppx3SzOOUfBkcrOEydimc4YezNsqXdb6_zqQXUBy2ZKOCUW8zsskfCH-IJHkZLi9dbOCOTsMzmCfpoNWAcsaSPrDvT9ClBZmbZ1NrU-AF_9PHmKLEAx1pLaDZfC6vBab61mYr5_I9lAsu4gDh3Xij82eQRRQ3uuFYq70eP6mkPkmK-n3cDR-9gtbXg2B2TcRsv4dPEp1EcR_oQFIzhcYOdv3iTpOiiAQmY5F6Pxz2Syzy784q4imn1in_Pm5RGkFKVko8IjlKF-wqgKOebH4ga6_xxJWYjGe0zCMFWea-fOQIOo8fXosgkzE40Vm76iC13FUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم: تنها تفاهم ما با آمریکا این است که «هیچ تفاهم‌نامه‌ای وجود ندارد»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/460159" target="_blank">📅 22:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
خواهشمندم موضوع
عدم واریز مبالغ سبد کالا
به فروشگاه‌ها را پیگیری کنید.
🔹
از شهرستان شوط آذربایجان غربی پیام می‌دم. برای
بیمۀ اجباری تأمین اجتماعی
، در ماه‌های فروردین و اردیبهشت هر کدام مبلغ ۸ میلیون و ۵۰۰ هزار تومان واریز کردیم، اما برای خردادماه مبلغ ۱۱ میلیون و ۷۵۰ هزار تومان پرداخت کردیم. اگر ممکن است
علت این افزایش مبلغ
پیگیری شود. ضمن اینکه از پانزدهم مردادماه چندین بار به شعبه ماکو پیام داده‌ایم، اما متأسفانه پاسخی دریافت نکرده‌ایم.
🔹
یک
فرد دارای معلولیت
که تنها منبع درآمدش
مستمری ماهانه
۲ میلیون و ۱۰۰ هزار تومان است، چگونه باید با این مبلغ یک ماه زندگی خود را بگذراند؟ فرد دارای معلولیت نیازمند زندگی با عزت، استقلال و تأمین نیازهای اولیه است، نه مستمری‌ای که حتی پاسخگوی ابتدایی‌ترین هزینه‌های یک ماه زندگی نیست. لطفاً صدای و زبان معلولان باشید.
🔹
جمعه‌بازار خیابان بهشتی
محل خوبی برای خرید و فروش است، اما متأسفانه برخی فروشندگان به‌جای بساط‌کردن در محدوده مشخص‌شده، بساط خود را جلوتر پهن می‌کنند و مسیر عبور مردم را تنگ کرده و باعث کندی رفت‌وآمد و ازدحام می‌شوند. چندین بار این موضوع را به
مدیر بازار
تذکر داده‌ایم، اما متأسفانه تاکنون اقدامی نشده است. لطفاً مسئولان رسیدگی کنند.
🔹
لطفاً در مورد
برداشتن تعرفه تأمین اجتماعی برای داروهای شیمی‌درمانی
و همچنین قطع سهمیه این داروها هم اطلاع‌رسانی و پیگیری کنید. چرا باید سهمیه داروهای بیماران شیمی‌درمانی بی‌سروصدا قطع شود؟
🔹
بنده از طریق اداره‌مان، در تاریخ ۱۵ دی‌ماه سال گذشته از شرکت
کرمان موتور خودرو
ثبت‌نام کردم و برای تأمین مبلغ آن، طلا فروختم و وام گرفتم. طبق قرارداد قرار بود خودرو در تاریخ ۱۵ اردیبهشت‌ماه سال جاری تحویل داده شود، اما پس از گذشت ۶ ماه همچنان در بلاتکلیفی هستیم و پاسخ‌گویی مناسبی نیز از سوی شرکت صورت نگرفته است. این
تأخیر و عدم پاسخ‌گویی
باعث وارد شدن خسارت به مشتریان شده است.
🔹
حدود ۱۰ ماه است که
بانک آینده
با بانک ملی ادغام شده و ما برای
تسویۀ تسهیلاتی
که قبلاً از بانک آینده دریافت کرده‌ایم، با مشکل مواجه شده‌ایم. هرجا مراجعه می‌کنیم پاسخ مشخصی نمی‌دهند و حتی بانک ملی می‌گوید پرونده شما «مشکوک‌الوصول» است و برای تسویه باید به تهران مراجعه کنید. ما فقط می‌خواهیم تسهیلات قبلی خود را تسویه کنیم، اما چرا باید برای انجام این کار از شهر خودمان به تهران برویم؟ خیلی از مردم با این مشکل مواجه هستند و توان و شرایط رفت‌وآمد به تهران را ندارند. خواهشمندیم مسئولان این موضوع را بررسی و راهکاری برای حل مشکل مردم در شهرستان‌ها ارائه کنند.
🔹
تو را به خدا به داد مردم محله
کنارگرد حسن‌آباد فشافویه
برسید. حدود ۵ ماه است تلفن‌های منازل مرتب قطع و وصل می‌شود؛ ابتدا در طول هفته فقط دو روز وصل بود و دو روز قطع، اما حالا سه هفته است به‌طور کامل قطع شده است. مخابرات منطقه فقط می‌گوید «قطعی نداریم، به تهران گفته‌ایم و خودشان می‌دانند». بارها با ۱۹۵ تماس گرفته‌ایم، اما نتیجه‌ای نگرفته‌ایم. از طرفی برق هم تقریباً هر شب از ساعت ۲۱ تا ۲۳ قطع می‌شود. و متأسفانه
ادارات برق و مخابرات منطقه
پاسخ‌گوی مردم نیستند. لطفاً صدای مردم مظلوم کنارگرد، در ۳۰ کیلومتری تهران باشید و این مشکل را پیگیری کنید.
🔹
از
محلۀ افسریۀ تهران
پیام می‌دهم. این محله با جمعیتی حدود ۱۲۰ هزار نفر هم با
قطعی برق
خارج از برنامه مواجه است و هم تلفن همراه اول دچار اختلال شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/460158" target="_blank">📅 22:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460157">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">کارشکنی کانادا گریبان بسکتبال با ویلچر ایران را گرفت
🔹
پانزدهمین دوره رقابت‌های بسکتبال با ویلچر قهرمانی جهان از چهارشنبه ۱۸ شهریور در کانادا آغاز می‌شود و تیم ملی ایران در گروه چهارم با مراکش، آلمان و کانادا هم‌گروه است.
🔹
ملی‌پوشان ایران که پیش‌ازاین برای پیگیری امور ویزا راهی ترکیه شده بودند، قرار بود امروز از طریق استانبول راهی کانادا شوند، اما این سفر هنوز انجام نشده است.
🔹
ویزای تمام بازیکنان صادر شده، اما هنوز روادید بهروز سلطانی، سرمربی تیم ملی و محمدرضا دستیار، مربی تیم صادر نشده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/460157" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460150">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTm6EnJgQ4MXQ6Of4aShXdbMx7LsZOdQZWFvA0QjdvSjOujFrBBpYbFpz60Od74frccnNZn912RoZPzDu1YF_nY-s40rnN2gx9_hFxDSITtf8gMQVJYJcAqJBGVQRfcFhqH-zwaj6qN9xLSznefvGQSMWQwThY2Rbvot4H9xHaqA1r2ODEtd_kctDq1I3P7o3VkBnRglfX8rvid-2lOamV4zBl_lwLA0PH6iJTNNZdCbPsnPWTZ65rrBj75Tkd_LxnOefWOJE3cY0_JxwRqr6AStE3p6aRmui2Q4mrR-7FT0HLZRkzB_iouyBLbzXHcZOM-tiwHADyBHf1e5Lh_4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThQUY6phNeodpixLdHgmCVrbRhqCVh1tdD8reGn15pXYQQSAUthPaZ1tRFfn04ACVkRLhXO2NKh0dn9E0VkmY2BZwD2dUII8aNGw5xf92BhVSC-EQTWvkZxyHppGmWKUmiG8-liRokm8u9UcCYr3dmSGxQ_eXIUcQ0RRZKoQl6sI69UE5ZEqZEwublSZIJgmi9iQfuGMt2Uvt8ysa18-YCoCX_k-9vGXVCZCVcqzjSByJ2uzo5El0tPwS_xDAntDep12Ck9tFLzX0O9fr2IL_kuDnGZE3OJpdRY0uaQar01Z9LMj-DsFuN8H-Jdx5ZKGoF_ymOYevLIEnYX7FchFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9ezQMoEkz3RbrsNWWP675PeootQdvNJujefgDhb_EUDg7nFk6ibz4oA7cSiKGRKlgNPjUvLtizcAJLZylmN6sm5SghjEKBN85J8J-5jk290O6w4VvtXsoTjqGgksDAJ9T4XeOTooqU70maeqTD-Zue1eKsU0a-7vc8vcJT-T8jhs_cMVwhG10-NqrPsyV0E-neUHulNjHgaykR8MH62wfg6QsH8hmOeOOfXshfgP1mw9S1N7FDcz8MVjYAAIbTkZShyFfw-_QSUyDZp4S2TjB0YbhEq77EAcLCm3JHOyBDwIK6xkIsCDiHbOUNM4xJm2jAfuvrNABhnqQfSSWFCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PU516aZXV8qz8XbRnY62e9mT0G2P1yHE7HjaMpz7n8nVkpJ47RON8Da4kFYkZwnEK1wCcH4nUKpxjj00HUuR5XwiNYMx7kgTFV4HAjYaWyh1_Av8A24AskV4b_rpywhd-qZ_aucNzeaDyvUmvVHit1MxnHgLIpaOvzJzDKFbbWhrrQl8BOMilPzv4ox1gp2ns9JC5wK5zHTZwNvtxXktvmtNhthcfPDrpvI4u-TFMiDfZqHIFtOHCWv6WlFDV8m1A_6vxRLKpv8yjszXKir7nWrLgc6FvE_fOQoD7z_j4x39HuA3nsHPpKpvMUFC0x3eXeaZm_sQ8JGhf1zf0_ngGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDk6nb7ppZE3QL9ewgZumYAr-qkardhsnF5ROZ07vLi0h4L76FXnQvBBK0zpLJjc2oWEBs6tHmtULOOvRHi10kPaD9h-mo6BOEyefDlQj7VlUJ-z3Dqxybzn9Eyin5cU6Lq59hVGOnm4O5ipoJogCXmdDFDlm49wYdhAQReW76hUHek9R1mvCLeWynvlAUc-L6LPOBdwuJ7PgmMSeYicGg-NRIBSOpFL-enco6IsXEK7noXWwRJeq2tv4TZeivATGu2SBWVt9mGaKySBr_l9IGhE7OywmrIICyzYr3i4yais-P1MXloTTYvsZh6ktBkjsr2rSetlCsQUN-1pAnu4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDhbSFmDiKDfeC2MswzL4nvFIjp1vIfeEpwpMI-hO0bbct2SrPqRQxknS3s2jXlGPy083XoWneqEaEB3lU5nnt5ARp1pWLGUz49OZuoUTXnTF4JR6_MraVPjHnkSI3VgB59TN7_NKFZsoOfPwhoIJezX7msG8dzqUnrXk51FgRhq4zTOdReJHDxl5vWaMtNuMggF5ofSxpWY86nKGkI-A6-Bx2glPgvvUFsPOFzcR3DXtoV9ztnCN9-rUmNnwP3UUqRKGW_Mb2xVJ7DXbIZuYRlhuAgkrtzqYLo02Ez5AS1QArXRClKBvxkaqdptyWOPihroNqPhz43ilWeYTn6koA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nW4JYiErlV-rmY-DHg2tekvEHldrIez5cj6URFIzTvwsTIicZBmxGrMBoLoLyscPUcS5ptIqrFJQRLOdyNq4vvZ-trMZ4BrWTzO65LzBjpsISV4ueEggN6PpZ6j7BRcGqDCsYLxRRsN78pHyl7_eRt2Ibqk7dZegQ-VKFiRzlBZ4OUFThquuXrGunmX8_YNA_F-PJfXSYZNIWWMjIn8mZmhrrzJchQEfILxOhbH5svlslaWwFL-RKK4DqARtrPKf6vDLc77yholb1IcjYZrNknMqA81RPIRhMqHnPCBnaeVIrYlhPoVzCXTOVenbuyrmgvUQ82leBbNKwu08f2eSmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرواز ابدی خلبان شهید مجتبی حسینوند
عکس:
علی صاحب‌محمدی‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/460150" target="_blank">📅 21:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460149">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e0e7346e.mp4?token=e-zz40w_R_j9ybN4RoIh3CgOhgz7p_vFLaiDUZPCZ-Xvwl7oHTi2v2vkrFGCoFFzguf_W6p32P3OPpIFW5tcmOxcz_QFMEfosIVIgENjUAPvxT_usNntCAsCsD-xwZVulSBir4i4olCaK8MJO4X4uxSFvW9veRUvDWCNO5Iy73ulO7UebG7xNfXue3u8G5wzxtIe3_WmGGl6jrr_tE4GJGQ7BrpEayahUZTjgvGCk4w0xXw0gZCBOTJ8chsa50oIXDF6cyEtJ1VRlFY3R6DBhr6LsxzGH_QSAZexSjz6MhdZvlMEI4kySqM66i5zGltbEkDMRTBm8o2S5ejOCktaTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e0e7346e.mp4?token=e-zz40w_R_j9ybN4RoIh3CgOhgz7p_vFLaiDUZPCZ-Xvwl7oHTi2v2vkrFGCoFFzguf_W6p32P3OPpIFW5tcmOxcz_QFMEfosIVIgENjUAPvxT_usNntCAsCsD-xwZVulSBir4i4olCaK8MJO4X4uxSFvW9veRUvDWCNO5Iy73ulO7UebG7xNfXue3u8G5wzxtIe3_WmGGl6jrr_tE4GJGQ7BrpEayahUZTjgvGCk4w0xXw0gZCBOTJ8chsa50oIXDF6cyEtJ1VRlFY3R6DBhr6LsxzGH_QSAZexSjz6MhdZvlMEI4kySqM66i5zGltbEkDMRTBm8o2S5ejOCktaTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شبانۀ مردم میدان در پارک ساحلی بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/460149" target="_blank">📅 21:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460148">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2zzEnko5UMPHzc9olqNUOvbvVHR2ZW0K-_nxBX2QMRgI-hP0XiqRMI5jiseKwZB_OYpyER6J_ge3hOKmsiDt84gB1LE7qIq7Z7K41Sm7nxF9N4UKd8SyaDb84qXigYHRy_aO9EnAXjtJsSUTZZKJDDnMoyDTZywwCpNM1LK168jIKDx8wSkQd3h5Um1c5r_tZE4wD1V58XkUG4jZskv999Y_GDltXNHfzvZv8VRVMmj5uqEyO8IPk0Ki-QCTaEFlUcjRTTzD2zAZsCeGlE3VP1MWsGJi2DBNFEbLMH8LFHcpjW5ljMlw2gl6UDJoAlkYguYI5yBBYMyl09Fu1kBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از دیدار سردار شهید تنگسیری با رهبر شهید انقلاب
🔹
این تصویر روز گذشته از سوی دفتر حفظ‌ونشر آثار رهبر شهید انقلاب به خانواده معظم این شهید والامقام اهدا شد.
‌
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/460148" target="_blank">📅 21:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460147">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07b37167a.mp4?token=ORzlwgm8nIjmi0muMUtxUZ2PcV5ng590mdbCCnW1b_Xe45n6t27IraijDIEnrqzMsKbdzvUaJtIZwHrIfp7MKUobfcJL3hWhaMTC1GmgxHYnNIyUkEXo-fzdRCAdvFGLuKGm3ZYGlRyiUbLXm3Nd0YMNZXZfNubPEZNX-OrelesN_cammKM1wDcyGYf9zNjsLpFvHLvLtcb147WwQw23G3bsqQBzmQ73kdZv8GoMWqX38pPjuHH7bL65S0I8sYewuLLUVosfzF2-yzVcSsuZWlyobMh55xsLCrhRVkH09a__NQ00MRQuiFB1c7qxh28m8NUpMlaL9s1BUdeQ6sSVgkVMI7nAlgKj4o84MWizyqBUCSv-OMVcIzplFlN5EYD0QB45UAyFVc0Honxd_-O7j2Ecq4fWYeZI5Z41vO8XLFosQQd-fDQwj8NPyi1lV-ArnmLhgcNZMZxIU9kUBjYlF3KOrHwJdktn2TG9VZxc3w1FZfpLU4A8opWaZJXC6PiQsY7cR0UNGA4IyU36rvXcJ6L5Amz-jI0SlFuB9Md2htW735oy25ioFmzFjBDcxQr3pexIU-r99B5CS5lCxQxLMpfdgJkozQzH3Zxp2Bk-cAdtNY71aihU34OWO04kQJ8RAzw5GbH5PoIWAGEpzmWZAIpqKxvi89S4IMLFHPe-fGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07b37167a.mp4?token=ORzlwgm8nIjmi0muMUtxUZ2PcV5ng590mdbCCnW1b_Xe45n6t27IraijDIEnrqzMsKbdzvUaJtIZwHrIfp7MKUobfcJL3hWhaMTC1GmgxHYnNIyUkEXo-fzdRCAdvFGLuKGm3ZYGlRyiUbLXm3Nd0YMNZXZfNubPEZNX-OrelesN_cammKM1wDcyGYf9zNjsLpFvHLvLtcb147WwQw23G3bsqQBzmQ73kdZv8GoMWqX38pPjuHH7bL65S0I8sYewuLLUVosfzF2-yzVcSsuZWlyobMh55xsLCrhRVkH09a__NQ00MRQuiFB1c7qxh28m8NUpMlaL9s1BUdeQ6sSVgkVMI7nAlgKj4o84MWizyqBUCSv-OMVcIzplFlN5EYD0QB45UAyFVc0Honxd_-O7j2Ecq4fWYeZI5Z41vO8XLFosQQd-fDQwj8NPyi1lV-ArnmLhgcNZMZxIU9kUBjYlF3KOrHwJdktn2TG9VZxc3w1FZfpLU4A8opWaZJXC6PiQsY7cR0UNGA4IyU36rvXcJ6L5Amz-jI0SlFuB9Md2htW735oy25ioFmzFjBDcxQr3pexIU-r99B5CS5lCxQxLMpfdgJkozQzH3Zxp2Bk-cAdtNY71aihU34OWO04kQJ8RAzw5GbH5PoIWAGEpzmWZAIpqKxvi89S4IMLFHPe-fGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال از پیکر شهید نیروی دریایی ارتش در فسا
🔹
پیکر محمدرضا بادرام از شهدای نیروی دریایی ارتش در که در حملۀ ۱۰ شهریور آمریکای جنایتکار به درجه رفیع شهادت نائل آمد، با استقبال مردم وارد زادگاهش در روستای سنان شهرستان فسا استان فارس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/460147" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460146">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حملهٔ مزدوران سعودی به یک منزل مسکونی در الحدیده یمن
🔹
مقامات محلی شهر الحدیده: در حملۀ مزدوران سعودی به یک منزل مسکونی، دو عضو یک خانواده شهید و دو نفر دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460146" target="_blank">📅 21:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460145">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa844588e.mp4?token=lodG_P9jAsumMNqW3AdjWQfvD9_9UqcVoKWCdkNF93kfEa2RnSuGJK5M1iWxWK52hcbeHwxASvP-zEyFoq-vQJcX73CSrsqihyra0TOgSEZ9Zm9eH4Rtd5xC5oAYGt8sCteAIXGbU-xy4fZMqiQjo5PzgXyJhNhUPwml9pcM5YdIjhPgNyl1X9c0eEPky7ubidRdVHgsmNhZhNukhd-uwP9XFbIAasyie_sU_GbB6U7QvcuakgydVKwkPx9qvSR6bDBg4wb5B1pxM3EwHoKaXunjzbFm2kcmp8i8uIUreSXaq8Qg5Sb6LVBLE1rVExo_domV93QMJY7XiUT3hdqNITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa844588e.mp4?token=lodG_P9jAsumMNqW3AdjWQfvD9_9UqcVoKWCdkNF93kfEa2RnSuGJK5M1iWxWK52hcbeHwxASvP-zEyFoq-vQJcX73CSrsqihyra0TOgSEZ9Zm9eH4Rtd5xC5oAYGt8sCteAIXGbU-xy4fZMqiQjo5PzgXyJhNhUPwml9pcM5YdIjhPgNyl1X9c0eEPky7ubidRdVHgsmNhZhNukhd-uwP9XFbIAasyie_sU_GbB6U7QvcuakgydVKwkPx9qvSR6bDBg4wb5B1pxM3EwHoKaXunjzbFm2kcmp8i8uIUreSXaq8Qg5Sb6LVBLE1rVExo_domV93QMJY7XiUT3hdqNITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطایِ نقطه‌زن آمریکا در کوهستک!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460145" target="_blank">📅 21:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460144">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fffbd748c.mp4?token=r8idoPoq-TQIrPYjIBUahExCYQMN5707ailW7MCHWjv3v09XoKJozzzayi1TqssywDpSIxEJDZFYBe6YYihjcyTJY58tEJ0rhDn_UITlIaqmEmO5e5De6eL7JmAxznTxf_IkSKbkbNywbmlnGJZ5tYylZmZa261zlUm58N_tHjvzjvCwgBm9eSbgs3n6L3lFUghJ0kDgCSlWrmeHmEkTrnGfkif_C4FmKAsJcwsOOGwy4xr1qN6TbZz9C9CuJGPMxhHhg_pURuavMttCiw7ageVDW5gIA4lj-Orack6H0fs9AF865NlpQ-A8L7Cjz7XOdr0NBTRHDe_cZo2ZDrgK6E3oUiUeYasGRMzkkhTbQNdO8wsBxQgNpHrdB6BuwytvjwncxiD4Q6_rr6Co-7Lzyv7bR3qPfiXTM63ZvU5PHpb921hCn0ms1Z292OPpapMmWgU2Gb5FgsF976tMI_RtLvT-4OJ6xf6-qmcb7roh2KoZ440QQDBzEjd2Vy5p4Mn4joVHQ6XiFBoKCK48ixqowMO0Z1pbQ_XxxXRcJ_-ugpBJ_aPSjpCYl1iRMn-AnpppxjiCC4i1xJlfxpFzN7cKMcd9xT0OQsONaFVaFXoZhfideQBvwdP2exJ8Gkln3TgBFiE1GowCRPgYZx-Yk3oazgkY4nPsR3FZyj7QEYyASwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fffbd748c.mp4?token=r8idoPoq-TQIrPYjIBUahExCYQMN5707ailW7MCHWjv3v09XoKJozzzayi1TqssywDpSIxEJDZFYBe6YYihjcyTJY58tEJ0rhDn_UITlIaqmEmO5e5De6eL7JmAxznTxf_IkSKbkbNywbmlnGJZ5tYylZmZa261zlUm58N_tHjvzjvCwgBm9eSbgs3n6L3lFUghJ0kDgCSlWrmeHmEkTrnGfkif_C4FmKAsJcwsOOGwy4xr1qN6TbZz9C9CuJGPMxhHhg_pURuavMttCiw7ageVDW5gIA4lj-Orack6H0fs9AF865NlpQ-A8L7Cjz7XOdr0NBTRHDe_cZo2ZDrgK6E3oUiUeYasGRMzkkhTbQNdO8wsBxQgNpHrdB6BuwytvjwncxiD4Q6_rr6Co-7Lzyv7bR3qPfiXTM63ZvU5PHpb921hCn0ms1Z292OPpapMmWgU2Gb5FgsF976tMI_RtLvT-4OJ6xf6-qmcb7roh2KoZ440QQDBzEjd2Vy5p4Mn4joVHQ6XiFBoKCK48ixqowMO0Z1pbQ_XxxXRcJ_-ugpBJ_aPSjpCYl1iRMn-AnpppxjiCC4i1xJlfxpFzN7cKMcd9xT0OQsONaFVaFXoZhfideQBvwdP2exJ8Gkln3TgBFiE1GowCRPgYZx-Yk3oazgkY4nPsR3FZyj7QEYyASwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون تعارف با تاریخ‌سازان والیبال ایران که قهرمان جهان شدند
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460144" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460143">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a8b8a488.mp4?token=N_JvU9I0Iby399vSl1hZAtG7l37kH0QcrG9lS6gpCqLUpjXW8AqWyAqV_LuqgeAlTancx9EjtZW60jpptHM55uCHCMQmgTeikKV-w3Xg0mdp8SZdjAc7rUt4d5mAhr8YFPFCtylqbP3G4bODUXt8-rNzHPtFLk7UzqQaAxrPCW-4Gl0MGHG99i6QVVrtsOu9e5orY79BXT6MV7blwkIlcG2w0BPF-AqPHK2FYIt2JtycI_QCGujxEjZErMFwPA26s8lhmo7fWc0SNWj2mrVmyyguxd2DtCeR-H02L_C7DdC1fbCXctoeboPVCngJP7r89dJ8UbSugTaRRrQfmUvL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a8b8a488.mp4?token=N_JvU9I0Iby399vSl1hZAtG7l37kH0QcrG9lS6gpCqLUpjXW8AqWyAqV_LuqgeAlTancx9EjtZW60jpptHM55uCHCMQmgTeikKV-w3Xg0mdp8SZdjAc7rUt4d5mAhr8YFPFCtylqbP3G4bODUXt8-rNzHPtFLk7UzqQaAxrPCW-4Gl0MGHG99i6QVVrtsOu9e5orY79BXT6MV7blwkIlcG2w0BPF-AqPHK2FYIt2JtycI_QCGujxEjZErMFwPA26s8lhmo7fWc0SNWj2mrVmyyguxd2DtCeR-H02L_C7DdC1fbCXctoeboPVCngJP7r89dJ8UbSugTaRRrQfmUvL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دشمنان با جنگ، محاصره و تحریم به‌دنبال ایجاد اختلاف، شکاف و آشوب در داخل کشور هستند و ما نیز با تکیه بر وحدت، هم‌افزایی و انسجام ملی، این نقشه‌ها را خنثی خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460143" target="_blank">📅 20:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460142">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twlI9ipuQ0Q8kUAEX3FUEAQrb8tLl3ndowuh4tE8W3DuoHMOqff7wAPYQnnKBBtiql6ILJo_kOXW9dDvoiXxP1Qkuji5L6SBqlrb-UV2g0zD99TyioNVSyWrzXiPLhpIitT5ONSd4gOyi9W5p-gRQmQgg5M7hcPcIJnULBmbmAFu5gGDnFjMnxN9KNAvUskQPymu1EBWLd8eZygJbc46ztcyzBilvs3T_lvNqo0aaj9-5MC91DtSjeWU02DnUR9i1SaOFUccWp7nqYphxOLXC29fXW3bW-tDSj_81fpPc1YAkr3vyj_OuzjVTTzv2PYpr84rFyCeJiR5JgcMzXARjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل عاشقی مرال‌ها؛ جنگل، مهمان اضافه نمی‌پذیرد
🔹
همزمان با نزدیک شدن فصل گاوبانگی، تبلیغ تورهای طبیعت‌گردی برای تماشای مرال‌ها در فضای مجازی افزایش یافته است اما معاون محیط زیست طبیعی و تنوع زیستی سازمان حفاظت محیط زیست، امروز اعلام کرد برگزاری هرگونه تور گاوبانگی ممنوع است.
🔹
فصل گاوبانگی یکی از حساس‌ترین دوره‌های زیستی مرال‌هاست که از اواسط شهریور تا اواخر مهر، همزمان با فصل جفت‌گیری این گوزن‌ها، ادامه دارد. در این دوره، گوزن‌های نر برای تعیین قلمرو با یکدیگر رقابت می‌کنند و با سر دادن بانگی شبیه صدای گاو، ماده‌ها را به قلمرو خود فرا می‌خوانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/460142" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460141">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQzn3bJfwEGK0VqewjNlwL405gCKtxHsGJ8Mbk2YHanDW_-e2mET7gBGvF_NxbvUjLq8FfHh1k26SGRlRkcIQsPGUFcT8joCLuUYyTKAZ81zwXNBHw30xtulgQ0K-Lgl-5g3c1UP-NKrCH5B__HMLYtJ13zKApCJyNQUdfUmRtRQvKV2ABCJvK52CwBQo92QziH819eUonrWRQ_HuzXaz5TjY7N0kI-rTkNe1eJx1V9J1HeYvQpEeB6su9CX-T7iFUlLRTbskzxf0E-GbnnrogF7jLiwGtuax2bIcUEPACC9B_fd61zwfTaE2R7EV883ZXJb_ivZTfBAA0jibRAInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: ایران از ایدهٔ چین برای ایجاد یک معماری امنیتی جدید در منطقه استقبال می‌کند
🔹
نمایندهٔ ویژهٔ جمهوری اسلامی ایران در امور چین: تأکید چین بر تقویت امنیت مشترک، بازتاب‌دهنده اصلی است که ایران نیز سال‌هاست بر آن تأکید داشته است.
🔹
کشورهای منطقه باید آیندهٔ خود را با دستان خود رقم بزنند و ثبات واقعی تنها از طریق ایجاد یک معماری امنیتی جدید و بومی در منطقه امکان‌پذیر است. ایران آماده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/460141" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460140">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930c9bbe22.mp4?token=gMzGJepo_rmpA-KVxu6IJQfisy0QqswlOFwo4e6sSNQ9PG0wV2BkZRBPhOEStl_21HlZwuba-ZX_Y4LXq2XocjblscXOfk762BX9o8Jbzj3YNlRXP8p0zyoLbIv-Gv83pc8thkRKxyOgDhWl6XIThDHVimbLqm3swcf5Tkq5wJNJZiGXf5QBmGYoLMRAfqSczqcsyJGXSdX75GtqnGXjw5pIe4QDDd5bZq9oYVKIA_Qbc2USXpPhAanKWrB9-b3rCEOjvALUewRQ6TKxkXu5gPGgw_ZrdaxicIvzS_K2HMRRsC73G8sI2bSUx-L_IJO2k34fVXL2v4sfNlQI-R8ak2aGMjS7Smdoqr1vOROu7TPhwCFBKbJD-Ut_rk2MP6kIuW8_U0kbRAm7GjhBpw24x_zayWhpzmCJ7hUAQowQ-pdQADEJYwLNTcm1sTpvEn7oDJoI1ahp3jifH84Hh0_IMfwVRWD6aeZE7DM8s3hMNEYgahcjUJt-E3Yu1qtml9qy1xCLRianDAvq4WInWTD_JLDkDEdAqmkRStQEyhxZBQDShykbh4TCSXkTrWVAE0IuolshsdHEYNmIq289oFAM-st0vkXUNWMVDitwUnoKXuRGVIt2mGT9AiKFi7dsgd4K2ge5TKbCoNdyZYwgW5qILRw1ZAMC4jXNwSXHGuV41DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930c9bbe22.mp4?token=gMzGJepo_rmpA-KVxu6IJQfisy0QqswlOFwo4e6sSNQ9PG0wV2BkZRBPhOEStl_21HlZwuba-ZX_Y4LXq2XocjblscXOfk762BX9o8Jbzj3YNlRXP8p0zyoLbIv-Gv83pc8thkRKxyOgDhWl6XIThDHVimbLqm3swcf5Tkq5wJNJZiGXf5QBmGYoLMRAfqSczqcsyJGXSdX75GtqnGXjw5pIe4QDDd5bZq9oYVKIA_Qbc2USXpPhAanKWrB9-b3rCEOjvALUewRQ6TKxkXu5gPGgw_ZrdaxicIvzS_K2HMRRsC73G8sI2bSUx-L_IJO2k34fVXL2v4sfNlQI-R8ak2aGMjS7Smdoqr1vOROu7TPhwCFBKbJD-Ut_rk2MP6kIuW8_U0kbRAm7GjhBpw24x_zayWhpzmCJ7hUAQowQ-pdQADEJYwLNTcm1sTpvEn7oDJoI1ahp3jifH84Hh0_IMfwVRWD6aeZE7DM8s3hMNEYgahcjUJt-E3Yu1qtml9qy1xCLRianDAvq4WInWTD_JLDkDEdAqmkRStQEyhxZBQDShykbh4TCSXkTrWVAE0IuolshsdHEYNmIq289oFAM-st0vkXUNWMVDitwUnoKXuRGVIt2mGT9AiKFi7dsgd4K2ge5TKbCoNdyZYwgW5qILRw1ZAMC4jXNwSXHGuV41DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ادعای صهیونیست‌ها در مورد تسلط بر ارتفاعات علی‌الطاهرِ لبنان
🔹
ارتش رژیم صهیونیستی مدعی «تسلط عملیاتی» بر ارتفاعات علی‌الطاهر در جنوب لبنان و تکمیل پاکسازی زیرساخت‌های نظامی موجود در زیر آن شد.
🔹
ارتش رژیم اشغالگر همچنین ادعا کرد که برخی از افراد وابسته…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/460140" target="_blank">📅 20:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xh53ER9YxqL75lBr7k_CSagnCLZ_52GaXB31fyb87oEhwZTH21qgV52OJMu22NYkEHJWtnbhN3NrWKSmZZXD1k4dePjGmCentvlfAyMCkQP9zlqAZoeRs5FkAkxlFXE_bIRRAE5xQiwV6CDr59FwuFws-wXl62AtnjH1jjcnkFAG9ItF8rHHZXzyP7tSvLtB39WzvByg0J8ARoS3VJjZwoHZrXZro6FyamU_UDZw4bryOkc-JOWTSwgXo27w77RyEjmVf5KFRozlXqDkZUjp3_gKUN-Jlgv0jB2Y3o5gb_6RWP9T_QNCzNeyD06_viPuCEhlYZ-PUgH5KeIecoBevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصبانیت ترامپ از شدت گرفتن انتقادها از او بابت جنگ علیه ایران
ترامپ در شبکه اجتماعی تروث سوشال نوشت:
«دیوانه‌های افراطیِ چپ‌گرا، دموکرات‌ها و کمونیست‌ها ترجیح می‌دهند ما در جنگ با ایران
شکست بخوریم
تا اینکه رئیس‌جمهور دونالد جی. ترامپ این جنگ را برای آمریکا به پیروزی برساند.
به عبارت دیگر، آنها ترجیح می‌دهند ما ببازیم تا اینکه ما برنده شویم! اینها آدم‌های واقعاً بیماری هستند که به نوع شدیدی از
سندرم
TDS مبتلا هستند؛ چیزی که گاهی از آن با عنوان سندروم جنون ترامپ یاد می‌شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/460138" target="_blank">📅 20:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
منابع عربی از حملهٔ موشکی به اهداف آمریکایی در شمال اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/460137" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
