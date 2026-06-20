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
<img src="https://cdn4.telesco.pe/file/SiN9eppKdy9R1kn8dBFFCnM8_cvFJs8HQu-8gEu3qkDx-yCd-lG79BXgGKubec4y05PqcldMyA-n4hXF1KmzpJX_BtSKPNe1XIg9FUxTWdinNI2Io8goKbbJBTPExYwYe_BtW813Yqn1xxs04jSLE626k2GR-sQ9ktsHSkh6yeKGdIHlr00kVGAaZa6Fk99g0HmQ19GcZA8WY8b0_Nt53TTwZjOIjhe2WrMIzt2W-8pHKbJZBrxuX4vratI0b2R-C7ZeD8mfWrziI_JXXCMx-DHzvL4WyQTJiGE2O2gvfpF0-Ikr-b2jwOKMs8XW3_lew2YgakyGvziXKnFCSmms1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 222K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
<hr>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDsTo0FJ0Yci8VQyCiPWwwfyNyX6VRWeYL4zYDoLo7pwhLcPxOCcvnSKBGKktdlGr8_ta_2UG7GCgKU6zMJqxuc51TzPmFMQE7_pTtvSW2ulKX4YJwWGBwATFdGnIh4cQpKDuMNmfgpUrRHkLIdfPFSVXcUIDOIHXjZGPVFTN7btfq4oM8dAXPL9EUVyT1UyYcgYzjojHfHMjTBCjQEcxvlDuQ7Br9e2kW8BQLIQ97-aqbsaHnrjDrJvplKMpe7lBoOdjXprhjbFBFMBRvRMpsJTPwjJ2Slm4HUXzyzH1pqs-dzsMDDQ3mS0G6L5CNg9Xg2beG27tx0ERSdLCq0o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=czTgNq5bHjXiN6bacMpp_V_JwgfYE8U8Edbwrem5NveMrAG41b1vmiCjAtnUbT0QJy3vuFflQWYQArLpYDNaNgMf3AjcmXq5DMpTRrUwAKm8c4dF6VSo7WXZ1k0QP0Y-d4HTMh2oU1RJlXQ-XC8gByex4PNyyWGXY7xAqz0zdZ1UbWGdv1nqs6mfQKAFcpyNzyT3H9gcHv0NT0f2LaSAYdJt7_XxlLkVqs1MIP4jTjrOCX9uELPmHByIwwqSzBZ-pfFLTCukWqG1rIdWuvYAdt3Tc2JNUde8aHeJkZnuhPfUNrzFmcyvW-nTH4EIg5UvsZXJIDuw_CcbIRVufzUd6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=czTgNq5bHjXiN6bacMpp_V_JwgfYE8U8Edbwrem5NveMrAG41b1vmiCjAtnUbT0QJy3vuFflQWYQArLpYDNaNgMf3AjcmXq5DMpTRrUwAKm8c4dF6VSo7WXZ1k0QP0Y-d4HTMh2oU1RJlXQ-XC8gByex4PNyyWGXY7xAqz0zdZ1UbWGdv1nqs6mfQKAFcpyNzyT3H9gcHv0NT0f2LaSAYdJt7_XxlLkVqs1MIP4jTjrOCX9uELPmHByIwwqSzBZ-pfFLTCukWqG1rIdWuvYAdt3Tc2JNUde8aHeJkZnuhPfUNrzFmcyvW-nTH4EIg5UvsZXJIDuw_CcbIRVufzUd6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=UelRZB1X05LpP_7C0iLp1TUHO_c7r_pip3y12ukVx4Av9qhEQp70KI4xPnOWjWzy_oAfSVNsblKpWetoMtOpIjzfaf1PJ-ElAn8LDNHZzP_fGZBMdYm-ij2I_C5F2ATByylQ82Yrd4iw0gryPX8LXBIXvrYBy6EvM3KoKjjLrIfPPqROtDMZw6bS0xbBUeTOqryGlwUQPYEhFvY8QPvWGxC5DZwhEjQO-3tpTpSqo0I5Aa4Yq3Q8F99jYSmSa9Tdr891KKeA19EbvBIShrd4wA6PpRbMdTJmWm4QhYiFb-5Pa7e8A4a83lHHSLvLiDAKUNQ4x4tiXitN1Buz4OGlaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=UelRZB1X05LpP_7C0iLp1TUHO_c7r_pip3y12ukVx4Av9qhEQp70KI4xPnOWjWzy_oAfSVNsblKpWetoMtOpIjzfaf1PJ-ElAn8LDNHZzP_fGZBMdYm-ij2I_C5F2ATByylQ82Yrd4iw0gryPX8LXBIXvrYBy6EvM3KoKjjLrIfPPqROtDMZw6bS0xbBUeTOqryGlwUQPYEhFvY8QPvWGxC5DZwhEjQO-3tpTpSqo0I5Aa4Yq3Q8F99jYSmSa9Tdr891KKeA19EbvBIShrd4wA6PpRbMdTJmWm4QhYiFb-5Pa7e8A4a83lHHSLvLiDAKUNQ4x4tiXitN1Buz4OGlaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJQ4Af5l0pM3ufgj31HLyVQ_jNGxixWN0zS4pNncPNXOu2UUqMnMTvIMCOBRHW-IMER7M_FgltX_YmSzrruZlpGHPSJVCK6usrroKMobviM6boe2USlOvl9vMXR-JZIzmK9Ua8nx0IMWTnwxmrUI3W3BuJoeDNmnDNwTRNiA5TyhWYkV0KVFX4juaCtl5r-s2sw7LbuUMdlONmrgRQSz57vuz3hnu9DfqDNmw4LBesw-U1hgSlXx2Iht8gPyIGMDsOUJ6Q2wOrXOgmNLhRxT8TNQoiMh6GExBv9qzlUag9xiMJzqfGLU03dG0hymkuGZsDCeDEMJpiNKPiouVKbnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXcpZJbLQOk0_xOofbUe_vgU_TnXZHko3ncC0wljj-inOoBjwX0UNWfOWkoRJXE0YDP4C5whrr1_g2fWHU5HyhIfe5sGP-Z5jxq2tp5YIflZBoG3JIABtUrtsAJOU2fHOP3oiwkQfQa6BE9ZlJwBx-SHf26G1GNshxeGMvkn0obYeNOOKiSHNOP73PdpJ7askMR0KIukiDP1D_vn5HsxwsMjZo655LyeZV46GiF0CdvhW9IBDSSPoBcKWcA1KyABc85YZotHtxF4t0dtHEzTql3wyAhoiHXdpCjKR2WWM7AuHKutbSp_-mp9DCraZK0Ohbdbm213qBMyHyRJ-e1abQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7zVc0gmxAdwrdyyzN_PsSHXboTA46w-iQM1jLKSdF872SXn1NehdQV9K93oB0nLC3AeBwhunrRzC3l6dY1PhRHm_PkzznwGG4eJG6iFtJnthIVdfCiNoI_2_kfA9doUARU7cbnQ37QbNJW8UTZeLmeCXUmK-JeTnlXRL44ZpsA0gtzEBZsgpC7xIZB1ccUbr5yGCHckuVTpUVUfxhnYFXHRkgroh_U2DhZBVTFYdzJsXp3QaeLnzCL9kyMx2ZTbEtrJGM9IdvHwwwyi9uF3xm-Ng1kNrgT5JJQosIJAIbyYFu1L5AxJBYyRkvAYWZR_hvgQvv4hmARaF414n_iaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXkopTs0BPYS6hFohEBSehhkZGiQQEJ_jej0tHtHqWyZENT7E7DtjAZvopgJKwux4rCiHq8DaPn3PUtB5EUY47z8FURiLsNfZQQCZX7DnXHtjOl4Z3UDGndYeS4d6T-fnEJ0pndAsalVMtRtzArKy3sidtXFuRBpXmLE2M8aCZgOXnK1yeM7ufFQXDAi1grHX9wb0Sk_bGKSvrkMPOPMLz8xpcCADkniuaKJYBP4-VQUB897FF-CoLne-1jfaoD740IGrzF53Jwb98bWilPL4LVzv5wGlwn3IfECImosgMiCUL6TMzurs6vuU6e_QUPAZDImnnLQZP6vjQdx-1_b4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8c_sI4bhpD3XlcUC4C3Fm1ONNWynX_9FsHirWI9tlJysgPmAacUXFG0lQnhquIt66zeHGL-GeQ0IglieoMfwg2vSwAMIzPXlwXsDFUOvKFjlj41dAYUeIsWu5x7k01YX4uWNUlzYUem2ELCeJwQCE2sQIrGN3lPUed1dyqMiCpqOX4wnvtnFWoAqLouf4D0Sj60yU24vv4lPkDBPLg-f1jiNRP9RtQ_BdCOQnAUC_C7YKF4ntKSKRLhDvXKPtpoe0_ybSs9vE-ud935cazBLcHcFEABnKpVm28fTmb41fjSefm3HOGUzRFEVWNbv5kkgagXGp0yYQ_wKyLlL5NReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTFKrpLbsUTt3VrGIUzYrmTaC-3UPhAjoqG4JjvP3V9Xhi-2vOIfOA400zctzFX4-9YyztLlSb-QG4AYv9jpqTQX5vx6wcZBUkj70bQSc_zfkSaAtKquHE0sfWtR9Xgv2mXNbPJau_axV-o-eyQrTXxWL4AZ8JOFmVunYlhnrNoyIfTgmACtSyl7AbBpQXaLCooqdrbmq7HFuHsK0nY6y4ajXUNGxdoP6BHe5phIMu_2FAA-968nyloD42hTBtLGWA5A-CabnKpuS7jANdmtqLT8mGiH1wVgDeX_Bb8HQ0ucDu-lF4MvOEjf3EYOIxbAD7AWxeYbOTMbvA4dh4ZAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrQyu_9bC2V9JG69shEaRJbMN-of0J7fvIYlPWMD1wmsx0F5lvAGwcFiZkI8OaLGyHsSdSfb_g66o-0jws8e-gpIGNLwnUpgnVGV5Uv9Ir-9A3b9EJVcw1lsVjfKNONvsWaVVhmdiGOSPm7rrjjXD4ivvIG5bJwWKlqF1-1TC1z7TMbl9RfUjLzraYneSdTUXWgADd5Yn6G9ErylSk0uHqXqPW0iQS6mPRQ6xAjB46hha0ZvaW473aYzVol16gI6B6HFNvoT7G3rreWku8KNlACvyxPX0fiQV3Jx4dCJ2cynGjVb7NUwspIAofQ9IB14z5NX1WKMGbHJzMyTm357EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=P3zHPcDp4y7kSuQqpSOETteZEiaHFpapcbySd5nTztKqeJ4MioYPBYjbmA5GohWPVV-2OkZzOcaZq84mR5u89Czp6-nIbVmH9fTx9UTu9xHBdxSiCu9exf6SjCoLZR5ckH094FAfbG9VXYkWdaaOuwzvXK7T1FC7vLGtUV5L1MFfDbZ2fZaEcMQP44OJhbVLH7jrT00InYA0PpW4SGyG4oH9nnHXWCKovtQ2VGX1k4jgb-52zrQZDEXkDut1CvTqbbrGZguUa7fqxTmTj1aFvUBRaw83XRHJVVggL76yyEKPu9VVLsDv1FVMyoGZer5UgSHKCmjMNIPFJmZC-rorGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=P3zHPcDp4y7kSuQqpSOETteZEiaHFpapcbySd5nTztKqeJ4MioYPBYjbmA5GohWPVV-2OkZzOcaZq84mR5u89Czp6-nIbVmH9fTx9UTu9xHBdxSiCu9exf6SjCoLZR5ckH094FAfbG9VXYkWdaaOuwzvXK7T1FC7vLGtUV5L1MFfDbZ2fZaEcMQP44OJhbVLH7jrT00InYA0PpW4SGyG4oH9nnHXWCKovtQ2VGX1k4jgb-52zrQZDEXkDut1CvTqbbrGZguUa7fqxTmTj1aFvUBRaw83XRHJVVggL76yyEKPu9VVLsDv1FVMyoGZer5UgSHKCmjMNIPFJmZC-rorGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=pjNHMs9qtLIRlV47A1VXKuHtX83FdvIai1dASQTfKSJU2eaqG0cwn2F-g9F7RoLe_qoDCRIwU-c-pkKbLK7qxiOsxxjkUeRHjrnt3EIQpuI_nZzZgee0ENb66fJbxuC8RX3brxoATdc_l6172qg-qGOubXpcXeUrqZVRH1URu9rxr5ehPTGxbHG3FuwLvILQ90V2EURyDsQpU0CTSyX9_D0jD2BVFYlfum9g9_0ROIzPrsoHovo7lrpEXKv7SnVNKH_Zxb-Co4YmswYalaGJM-5nh3A9N6KBXU7dWJ1N6SX0yJhpCZ6_lPsmWiJ38fEeFZM1EGDHqqquAOwvGAsEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=somjypIJQkeXmQnY6A21d8xpjQ5rRhWbOqMhtNx9fqa_zeJfVQ_3K1Q_-op8baN7DdjTiC-v7oSDJh72t_Cc-WbrEyiHIBdftHQ6gVQm22bnK0ziLC38BO5-dMBQh3-8ouc3_gZEmi4V3XYDEq-OYYFxD0-kKm_bPK9mTMOcV-7SEwnYnpIsbNGiEAT0zWY01pUQiOkucgzHc4552YomLUMVSQWimRJtbJsCpKJjC5GtSscICr1XlwvN6oXb0FglCqI0htlCFZO2i2ficx0n2sGiinHn4EZq3u98CbOLHDkyoM7_OOCKA1X4pZ58LH9izge6Se9NLQutsQzLRsSD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=WePaD2_p1JFvHSLloG8smPfQA2x2__n2nswpneAelsHMTsl7HxUY1nkcZ-NU0m9Oa8OQPQaKG5BOwy8QUTo7HVM37BO-d3X3ZUyXd5iggZSk417-s9HA_RY3sH7Jml5GwOvaNEGY3jxvWu1FgI1v6imSAWwHUXT-JI0Lqe0OJCclcfJG_kdHZSdHZ-iToiH4ByUrbGXgt3SskEUGOryTiRZiSUBx-eKak4iV_pzefuRPwO3fRxiNync5O239pDqkaUj0WjRGY-QtsI505jGpUzqd0Lvn-Wcs-dWh8VdjiPfJBb-X8tZjoOLz5tifP-WrAE2cmbEC05Y5e8aBzy24ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=jDekd-wYtk8ig96tVTinvciEFM_DiPfgUFIWCXvq5J-fljTMPUA9QDyXov9RyhwnkEAMSqf6DsmN-4PBf79PGYrCt_OwJM8tY3pVyCTGD-qGW9aVrWqDKsILzN005EVsI1wdqBNo1tkunfnKXkwidUbCddtIcuwW1SmQZhYMx6osGDf7TGRJewmUWPPDs7QREmFsE1pJSxfcMrBkfpril-vIYYDUFjniMd766_tXCoC0fHveNttmFTop61bJpyPK_bX4YGI0YaQPTFVqCOQJjzfFwxPPXnoNBKkldOUs0gxB_qGTo4xe5QBjB9w0cCF-a8QevyCTt5rypgpEQrhjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=jDekd-wYtk8ig96tVTinvciEFM_DiPfgUFIWCXvq5J-fljTMPUA9QDyXov9RyhwnkEAMSqf6DsmN-4PBf79PGYrCt_OwJM8tY3pVyCTGD-qGW9aVrWqDKsILzN005EVsI1wdqBNo1tkunfnKXkwidUbCddtIcuwW1SmQZhYMx6osGDf7TGRJewmUWPPDs7QREmFsE1pJSxfcMrBkfpril-vIYYDUFjniMd766_tXCoC0fHveNttmFTop61bJpyPK_bX4YGI0YaQPTFVqCOQJjzfFwxPPXnoNBKkldOUs0gxB_qGTo4xe5QBjB9w0cCF-a8QevyCTt5rypgpEQrhjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=AMv7a2bhDcHJfQ_7W0cBy77dHWEhoZ8ao71gq-ADHVxTc48RnDWMhuMp0xf4yXX3dTrfRo49sgyZj-Fuf2NT0LekaxRO3NhaSMoVTrPe8SZPwvOMSeEiC-AmeMygSK9C8Yi8ql-zqU1aJHirVgEcMLcsS_7xbfbj4JN55yFPq82v1oYKmHHOjvaRUIcO6H5lS1ryQJ41D0hCO_bFXPXA_dhCCT9AEvKruMYW-XhLdViFXcyW2H15uwNUpUHMdeUcPeOmxQJybUC6HD3Wxq2ClaBug1aJvAacq-KSRePCOmm0U6U8vrXhx9btpU6DpUu4M8khqLSAi4IkQZIgOUVWJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=AMv7a2bhDcHJfQ_7W0cBy77dHWEhoZ8ao71gq-ADHVxTc48RnDWMhuMp0xf4yXX3dTrfRo49sgyZj-Fuf2NT0LekaxRO3NhaSMoVTrPe8SZPwvOMSeEiC-AmeMygSK9C8Yi8ql-zqU1aJHirVgEcMLcsS_7xbfbj4JN55yFPq82v1oYKmHHOjvaRUIcO6H5lS1ryQJ41D0hCO_bFXPXA_dhCCT9AEvKruMYW-XhLdViFXcyW2H15uwNUpUHMdeUcPeOmxQJybUC6HD3Wxq2ClaBug1aJvAacq-KSRePCOmm0U6U8vrXhx9btpU6DpUu4M8khqLSAi4IkQZIgOUVWJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=FqCm7X4a1BhGKRc-hvfqTqRUiPscgjH7PofGSDyhDsxHI0ldpAC3ooB94BUkeUXKagAxPj7CBGfZAHn5HmzijJa0Pk1YFBcWs7iX_OQpUC3X-84bNOjFXk85esK-tEvN-Q1yM55LoveHgrbRZmKv4BcthF_0HBrV3mmFq38eD2vUUCyg7l29KoLSr2YMyVp-gWCjCRGkfelhnY2L1bV8maTst4Mi010JBBnXMe8yukR5zPPgHoMmAvoD5XBazMVXTnw82RCnOCoKkRMG9LjZVFUHoEtPrXH7lm9Uf3lKY20dsiRvK4RCVZIbNpiFBnxdSNoTU3RumCqjTkWRPRM2EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=FqCm7X4a1BhGKRc-hvfqTqRUiPscgjH7PofGSDyhDsxHI0ldpAC3ooB94BUkeUXKagAxPj7CBGfZAHn5HmzijJa0Pk1YFBcWs7iX_OQpUC3X-84bNOjFXk85esK-tEvN-Q1yM55LoveHgrbRZmKv4BcthF_0HBrV3mmFq38eD2vUUCyg7l29KoLSr2YMyVp-gWCjCRGkfelhnY2L1bV8maTst4Mi010JBBnXMe8yukR5zPPgHoMmAvoD5XBazMVXTnw82RCnOCoKkRMG9LjZVFUHoEtPrXH7lm9Uf3lKY20dsiRvK4RCVZIbNpiFBnxdSNoTU3RumCqjTkWRPRM2EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCq8b-PMk2FO3TZEh2ky8pZfKxTNxojGbswka66moM_sdvMv5ntzuwb65HYjNOumCSK8AgMvTXGPQdd-tzD-qyS7hOdy8Lj7DNxCt-MyeYynhqo1dJDLGhAkfsoLiJtnZ0qwJTpxeo4USbaR1zuKf2hHd1OFyaAgV3IjDlgABg2eOX6mV92i-EF35BNvYj7DikaTVEgKpw1uNdwMVVZC1n9RihoPpgT3hbujPbsfzWU6bfuBe0vmI52b-Kw-eJTn1y4RFvv8dnOEqdNxWWJN2LI6t-5HVmKjRN84kKGpZLh2hW2SVE3B8SfaqB7jLS159YXbeTVmDYygc-fabvRPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=en_Fl5G9Hr6W4esF3sMZp86RxA53LN5BdBs1To9D4AUtdpY7GAGF2YPhLVy2zP_bkzWqyXSZMWBOGJ7lSJU_lFtPSLamjz5rYwKE27QYKGGbDMlMHO6W-_XI7uEoIaV5sQ6OqcZKIlJ_K4JJdTkz8OfQ5kecRmmnlwzhLt9M32gGz1XTjO7iJTSQxkKyfpYDF4hRnSv-WLz-ZBrAbgQFIdkrO1J-af7U8l-AMlHGP9EBQIAochXbK5vrgp7K1XynpthhJ3jHz3LC2XNvlDWBKI6fn6Qlm70f0QMLPqwLD_xnxOPGslADCOsVGNeyvkJmf6m-evpaqFNQiRHJZ7zNqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=en_Fl5G9Hr6W4esF3sMZp86RxA53LN5BdBs1To9D4AUtdpY7GAGF2YPhLVy2zP_bkzWqyXSZMWBOGJ7lSJU_lFtPSLamjz5rYwKE27QYKGGbDMlMHO6W-_XI7uEoIaV5sQ6OqcZKIlJ_K4JJdTkz8OfQ5kecRmmnlwzhLt9M32gGz1XTjO7iJTSQxkKyfpYDF4hRnSv-WLz-ZBrAbgQFIdkrO1J-af7U8l-AMlHGP9EBQIAochXbK5vrgp7K1XynpthhJ3jHz3LC2XNvlDWBKI6fn6Qlm70f0QMLPqwLD_xnxOPGslADCOsVGNeyvkJmf6m-evpaqFNQiRHJZ7zNqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=j0lMtOxwOkbi9VmR6tAu_9Q5YVsSXRGSDPamFycvrHBUNmzIVqOdty5jaBW7Mog-8OHE_GM_HFNDgG1Hefb0MA051B6VwdfwWqUSbSCPgVqv0EpjcXjvIrCUnYYreiav4MkHASx95krPeZ9pwEpU_kVQBcvgvxG9M8x_DRHEmVaQ5D5s77MGjn_a0v40_VD14ozJk-bTYR-OM-SeqC4XvxkCITM-1CZY8Xw-KxFRBAmGk6dKJ6Tyl-MJgwLBfYJSPmpINIJ6oOa4sJyWGR_eIB1BA2a6lNt_r0agiLn2MgHT4QIC0jUaD6dZgpg-jCIgIUg2h6hZ8PJDjTfOfajGUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=j0lMtOxwOkbi9VmR6tAu_9Q5YVsSXRGSDPamFycvrHBUNmzIVqOdty5jaBW7Mog-8OHE_GM_HFNDgG1Hefb0MA051B6VwdfwWqUSbSCPgVqv0EpjcXjvIrCUnYYreiav4MkHASx95krPeZ9pwEpU_kVQBcvgvxG9M8x_DRHEmVaQ5D5s77MGjn_a0v40_VD14ozJk-bTYR-OM-SeqC4XvxkCITM-1CZY8Xw-KxFRBAmGk6dKJ6Tyl-MJgwLBfYJSPmpINIJ6oOa4sJyWGR_eIB1BA2a6lNt_r0agiLn2MgHT4QIC0jUaD6dZgpg-jCIgIUg2h6hZ8PJDjTfOfajGUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=ZLoV0LZG64iVJdS7w4_CiEEfDNY96DE-TRPYG4vK2gMYBA3jsqsG7DYITFr4KJmOSP_wwd8cXapk2qm45STMfAdSh9dwGGut-T2Vqug5SknuerWye9YM1tk3ErfYG0z8dwbIjUB3LGvth2fRdH-M6SKjw6p0o0d2I8N5rgWoiFyQzFAGKOO5AJKVNsNJNDwP1UyCIdYa2vdeQbmnglQ2iY3aofuSKiCg1mWw6TBtwTUivT0HS0LgVZtAmsH_gS5ObHShrYxkXfB-d1h3dOfDc58xu7fVYSGUjctPn5xVa6dL5Nib80AibgbB-OU_5SzKuVN-c4orPPzZOsjLK4dINg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=ZLoV0LZG64iVJdS7w4_CiEEfDNY96DE-TRPYG4vK2gMYBA3jsqsG7DYITFr4KJmOSP_wwd8cXapk2qm45STMfAdSh9dwGGut-T2Vqug5SknuerWye9YM1tk3ErfYG0z8dwbIjUB3LGvth2fRdH-M6SKjw6p0o0d2I8N5rgWoiFyQzFAGKOO5AJKVNsNJNDwP1UyCIdYa2vdeQbmnglQ2iY3aofuSKiCg1mWw6TBtwTUivT0HS0LgVZtAmsH_gS5ObHShrYxkXfB-d1h3dOfDc58xu7fVYSGUjctPn5xVa6dL5Nib80AibgbB-OU_5SzKuVN-c4orPPzZOsjLK4dINg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=NM-EByZnhuToUvl7mqtaXn2qZI6Iz9SpStCVt6H-ufWokvq2zox9LmsMxJJkfBBEJV3qAxeuGILO-Yz9dhrcq6amey_jJ9EmR-42ZRqjJLlh8JCoP7Awya4JjkoTSmIlggGERRNZplAIV-DCg3t_US3CH5RlUilbyin99jZx5zIXCmNVoIZ3o1h2axIxPXUtfFLMck095phwcm9wXv_WxwZdUNI2W7SeLiTZ6HkQpURKDHjK4n4LMGAAr5jVJOhnhjlUZDHp_dTzlkmrmMo0uHDLR6KZAjUJcuEDyPmdmiHV_vHimudIzJz81YR8FkCuWTUmQI4cXscjY_HPS7YFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=NM-EByZnhuToUvl7mqtaXn2qZI6Iz9SpStCVt6H-ufWokvq2zox9LmsMxJJkfBBEJV3qAxeuGILO-Yz9dhrcq6amey_jJ9EmR-42ZRqjJLlh8JCoP7Awya4JjkoTSmIlggGERRNZplAIV-DCg3t_US3CH5RlUilbyin99jZx5zIXCmNVoIZ3o1h2axIxPXUtfFLMck095phwcm9wXv_WxwZdUNI2W7SeLiTZ6HkQpURKDHjK4n4LMGAAr5jVJOhnhjlUZDHp_dTzlkmrmMo0uHDLR6KZAjUJcuEDyPmdmiHV_vHimudIzJz81YR8FkCuWTUmQI4cXscjY_HPS7YFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=tYWtaZR6UC7hmjZif6oCm66tUJeJHIj4WALw7go-Jt7ovdlHFF0V2q7bay0_sxRSGWrCU9ov2h-WyryM1jjSCVnuWqi45tiLpOKAaa1mdty7VTQMrP7DqyWB8uBlVvAgbyTd-D1OKcaWxl-qRz_4hXB14TVa1h_uSSyj6oXaFUtwXn9NuhOCOGvsfoiwuF1VEt4zsvkBONFv62L_6quxjkVFgl328SVUzRVY7xMZj2hrqaJRku3IA42iu9-L5aU4sMrDvztsfzbiCKlgemkhr8uWFU7bhISecNwSCzhRqylV07_uBknzUHE-QzvVcz90jKUqeVnUZtkNop7KA7kqDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=tYWtaZR6UC7hmjZif6oCm66tUJeJHIj4WALw7go-Jt7ovdlHFF0V2q7bay0_sxRSGWrCU9ov2h-WyryM1jjSCVnuWqi45tiLpOKAaa1mdty7VTQMrP7DqyWB8uBlVvAgbyTd-D1OKcaWxl-qRz_4hXB14TVa1h_uSSyj6oXaFUtwXn9NuhOCOGvsfoiwuF1VEt4zsvkBONFv62L_6quxjkVFgl328SVUzRVY7xMZj2hrqaJRku3IA42iu9-L5aU4sMrDvztsfzbiCKlgemkhr8uWFU7bhISecNwSCzhRqylV07_uBknzUHE-QzvVcz90jKUqeVnUZtkNop7KA7kqDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=S2v8eKzwCodXpKWJDkaCz6E1ed6gShHl9nsluUaUUa7XZgQEF80U2kt_sBHHauXiGic7wDX5_Aab5WVK4Ik99BtogTpGvrMYbu8iPzjKS59hXS36iSJ0reTN_bQR99tzUiQKY41wPkrPbz0Fh4kYDJCstaMvLZJMr4olfGtJYQQqK_Y_7jubIN6ocvH5wwpLQkgFhAcPex4Md-xrIKM9O1iMcfow4tvoiq0n5ZXNfEMXDitu7a5c6Z9a1QGG4RVcOVqGbpHltZLhiEpwHFL9DI3HB-DAR535pyfLLvqAEPKmM_Mjzbvx-UFfBggE2-oAYHrhs1wGVPrPbe3rPLMeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=S2v8eKzwCodXpKWJDkaCz6E1ed6gShHl9nsluUaUUa7XZgQEF80U2kt_sBHHauXiGic7wDX5_Aab5WVK4Ik99BtogTpGvrMYbu8iPzjKS59hXS36iSJ0reTN_bQR99tzUiQKY41wPkrPbz0Fh4kYDJCstaMvLZJMr4olfGtJYQQqK_Y_7jubIN6ocvH5wwpLQkgFhAcPex4Md-xrIKM9O1iMcfow4tvoiq0n5ZXNfEMXDitu7a5c6Z9a1QGG4RVcOVqGbpHltZLhiEpwHFL9DI3HB-DAR535pyfLLvqAEPKmM_Mjzbvx-UFfBggE2-oAYHrhs1wGVPrPbe3rPLMeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=UXZY5AemRHnVJbyJvbgc5doboFntlFcnO3Ma6WraZbEkWAfg0BUTW95SsOxEqiT04nQUjKYCwApI44OpQU3OfN0UB88jfaRy7GPfdg1ZnlG0QTkVTH-eKkBXo_GhuXbgvScptWbmd22Gw4COqUApC59sjvYilaIOB-g4hLB2gFzj1Hga8jSVpYW6P1rU5lSljBkzKolF0wDxHbZBxMSVPW5DE21b4RnjAaBAI6Cj3cjbHf6EkoJemRiHAMPcIJ9B5W0PfAB73iHYH1JK0HEk26LGrER5l_NmykMB52V_-j0YnxVCMiDlfPdGgBZKDjNumEQ-WtDnjTIUY8pMIM1BXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=UXZY5AemRHnVJbyJvbgc5doboFntlFcnO3Ma6WraZbEkWAfg0BUTW95SsOxEqiT04nQUjKYCwApI44OpQU3OfN0UB88jfaRy7GPfdg1ZnlG0QTkVTH-eKkBXo_GhuXbgvScptWbmd22Gw4COqUApC59sjvYilaIOB-g4hLB2gFzj1Hga8jSVpYW6P1rU5lSljBkzKolF0wDxHbZBxMSVPW5DE21b4RnjAaBAI6Cj3cjbHf6EkoJemRiHAMPcIJ9B5W0PfAB73iHYH1JK0HEk26LGrER5l_NmykMB52V_-j0YnxVCMiDlfPdGgBZKDjNumEQ-WtDnjTIUY8pMIM1BXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=oyQvZaomO54a_QZMT7Vm8_JBxrlEd4eIhxjze9XKt7xJiAQkjEriAa342xistCEqbDNVQWIlxtVOvk30XT8HV89hNK1GIypJZPOZI1o_QT9qxVPeX8-m5-LNmMWHyjWqDf4Zvyasa54Zm4kmLAHTKuoDU9zyS1eFv47I3b_pZjqW09Knq_jmlienok9-bO_xNjaNgtOhGaoPLEny6UQ5Xo9eBZvhLgkPFtKHdfSZM6UmxBhLU1jf1XEbcGGcSsXJlq1XoJ5wtN3oM7yMwYKCF_5ReToF9efIgbN441VAMRwE5X0CaeuTjg7-H88aV0pcsQW7d2vr-RIBMRk5UVOZUY1kkiEWb-wxQ8nF71SqhT-cq4CEn7PpiweMk8zLGHn1xZ7V2vx2lGlNIKwKw71xFOV_1aD3phCOTq7aGZ06-KtJLKcHNPcxY0aDst48Ni8jkUfrv1Hrnti3ex1vPMLGPO-mhTrU4oxWyrUUWTP0xOtKmQllIpJlLRJIb5wb4GBAnx6EgqxkzGGZOWHEVX0iYsyswsDRPME-6fXG8wTueM-Afc_fdqa8YNjbEJ29SUDmFAGswR2g9NhI_cYQIix76sGOlHzmJ9JIWO3kto0FVOk-rS4Wodj0U-BmA6IhLBQuck2AIeeB2Lz0GEjNN0TTTB4TNxkWL1apzcxqK_dL8Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=oyQvZaomO54a_QZMT7Vm8_JBxrlEd4eIhxjze9XKt7xJiAQkjEriAa342xistCEqbDNVQWIlxtVOvk30XT8HV89hNK1GIypJZPOZI1o_QT9qxVPeX8-m5-LNmMWHyjWqDf4Zvyasa54Zm4kmLAHTKuoDU9zyS1eFv47I3b_pZjqW09Knq_jmlienok9-bO_xNjaNgtOhGaoPLEny6UQ5Xo9eBZvhLgkPFtKHdfSZM6UmxBhLU1jf1XEbcGGcSsXJlq1XoJ5wtN3oM7yMwYKCF_5ReToF9efIgbN441VAMRwE5X0CaeuTjg7-H88aV0pcsQW7d2vr-RIBMRk5UVOZUY1kkiEWb-wxQ8nF71SqhT-cq4CEn7PpiweMk8zLGHn1xZ7V2vx2lGlNIKwKw71xFOV_1aD3phCOTq7aGZ06-KtJLKcHNPcxY0aDst48Ni8jkUfrv1Hrnti3ex1vPMLGPO-mhTrU4oxWyrUUWTP0xOtKmQllIpJlLRJIb5wb4GBAnx6EgqxkzGGZOWHEVX0iYsyswsDRPME-6fXG8wTueM-Afc_fdqa8YNjbEJ29SUDmFAGswR2g9NhI_cYQIix76sGOlHzmJ9JIWO3kto0FVOk-rS4Wodj0U-BmA6IhLBQuck2AIeeB2Lz0GEjNN0TTTB4TNxkWL1apzcxqK_dL8Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=UzoOT5bEf6e0APhJD0rb6rRtSpiEy-2EvN5vOvob34voIXZUIaObHQRGsrZvHqe5pmC1DLg0z8BkNScpw31ClNAUXQCDcbBOyWmPvAmCFqrrUjMPiwK7JBKS8Q76ofrsFcXF9SUOMN89vctV2gkq_FECvAaImoE-1UjqVpbp0VqjmkXMVc49qJhKmouf_PPbKbs1xHwPfLBKnR2VgVTQq6LWTrLZ4H_0pzy3hJ808_SBcA5x7j_kZT68p326Ja0zFAUYqpGtftNrO22zEg3b7jrGO0UMooWAKdjiAjr3iHI7bXVHd4OsVDwnRl-KvUVZw1y3xtZoKr8szuwQdqECWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=UzoOT5bEf6e0APhJD0rb6rRtSpiEy-2EvN5vOvob34voIXZUIaObHQRGsrZvHqe5pmC1DLg0z8BkNScpw31ClNAUXQCDcbBOyWmPvAmCFqrrUjMPiwK7JBKS8Q76ofrsFcXF9SUOMN89vctV2gkq_FECvAaImoE-1UjqVpbp0VqjmkXMVc49qJhKmouf_PPbKbs1xHwPfLBKnR2VgVTQq6LWTrLZ4H_0pzy3hJ808_SBcA5x7j_kZT68p326Ja0zFAUYqpGtftNrO22zEg3b7jrGO0UMooWAKdjiAjr3iHI7bXVHd4OsVDwnRl-KvUVZw1y3xtZoKr8szuwQdqECWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=NvwWJc8DHpMCbMIVdiKHYIY_wgdNXBndDlEkzTjh8MC9Tk02PbW-9GycQOnuWldOUQdAXd9ltH7t9DdczJtqbh-Oa26rmbT_HllwkiArTMqobfBYKaW8Q-XPaq44-kChgNVgLy8JGLexcf8dR_iNb6xWvHvS73nu339UlrYp8jz0JxWgh2_28JnVOHW9GH16NzVGIEjsiyaffr7yadRTVGsqPB6Ck5wBVaVlfa--rjOatSyl1Ii5bS23W3B_qtiO2FCxIjPAZ9DFUpWAuNhXzVIlohT8iRXiMDfjyHkSsYzt6hT7jAbomUO6xFKBbVUF11htMB_kSsXIuQhS7ai4Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=NvwWJc8DHpMCbMIVdiKHYIY_wgdNXBndDlEkzTjh8MC9Tk02PbW-9GycQOnuWldOUQdAXd9ltH7t9DdczJtqbh-Oa26rmbT_HllwkiArTMqobfBYKaW8Q-XPaq44-kChgNVgLy8JGLexcf8dR_iNb6xWvHvS73nu339UlrYp8jz0JxWgh2_28JnVOHW9GH16NzVGIEjsiyaffr7yadRTVGsqPB6Ck5wBVaVlfa--rjOatSyl1Ii5bS23W3B_qtiO2FCxIjPAZ9DFUpWAuNhXzVIlohT8iRXiMDfjyHkSsYzt6hT7jAbomUO6xFKBbVUF11htMB_kSsXIuQhS7ai4Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=vxcvuKmrffAPrFAW-oEMR71IbDiHbNzBmXNhwx7Xq3zBRKzOhv9d-pwIH9hUcykaeIEn1BwOe8eIRn6CUYNu-Ps40hgq-1PySBAatLVVbO219n42K52ONaEArmrCDB7lY2cVExXaX6U8nMgBSwk5V7zSn8EHaTILvkCO41WxZz1aVwAVxC2MgmMPrkovM_4UpA6g2Xu-MUmXuepgNLLn2YNWH5-v7zMgo2OTdoBidlObRv9VFdElh_M6f5UUzXtFz_MSFl34cuj7kmJN8DcyPgQTH4A8y4i3X9EDfzG1oKmNoDBmc3ukIhbg-Xm7ajIPJEnitWQO3Egmw6Wc3ovylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=vxcvuKmrffAPrFAW-oEMR71IbDiHbNzBmXNhwx7Xq3zBRKzOhv9d-pwIH9hUcykaeIEn1BwOe8eIRn6CUYNu-Ps40hgq-1PySBAatLVVbO219n42K52ONaEArmrCDB7lY2cVExXaX6U8nMgBSwk5V7zSn8EHaTILvkCO41WxZz1aVwAVxC2MgmMPrkovM_4UpA6g2Xu-MUmXuepgNLLn2YNWH5-v7zMgo2OTdoBidlObRv9VFdElh_M6f5UUzXtFz_MSFl34cuj7kmJN8DcyPgQTH4A8y4i3X9EDfzG1oKmNoDBmc3ukIhbg-Xm7ajIPJEnitWQO3Egmw6Wc3ovylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=RTym1rh19naafGTn_V_Fz5fXArQRRSDDuk7j_SdnOhSkLlrJvpBlTaM4MsX9IoXNs_vXKRK7iYu9hGLl8LQNF1HtQpoadJN7ZSWRWtVrNLP7OzyaoDDH8tDpmWU471gF9B0BtXQAdjrpu6nThc8eVdlJh990CCioRaMECdm6PblN27-BFtGqcTJB_J5-NZrkhYnLf9i-s7GQAC_pMmo_SRVYnPDeE5SQaumvUNJoMBxIc4sduImoKkhnBV3OtAm3aQ3cojRnnliMA0OZ_U5AfNlRZwJSCt3nv4aBCkjvO4CWVxgTd7t78j0OnmXEr6njBlmhYL7-dJiyZVFUW2Sdvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=RTym1rh19naafGTn_V_Fz5fXArQRRSDDuk7j_SdnOhSkLlrJvpBlTaM4MsX9IoXNs_vXKRK7iYu9hGLl8LQNF1HtQpoadJN7ZSWRWtVrNLP7OzyaoDDH8tDpmWU471gF9B0BtXQAdjrpu6nThc8eVdlJh990CCioRaMECdm6PblN27-BFtGqcTJB_J5-NZrkhYnLf9i-s7GQAC_pMmo_SRVYnPDeE5SQaumvUNJoMBxIc4sduImoKkhnBV3OtAm3aQ3cojRnnliMA0OZ_U5AfNlRZwJSCt3nv4aBCkjvO4CWVxgTd7t78j0OnmXEr6njBlmhYL7-dJiyZVFUW2Sdvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=cN64iSEuG_UzbDAMUb_LBYRnzyjGum4VCcMNCTFwYfv8v8JlgoewyMzD_RBu7hi0v8E11UwPL1VOSs6wEkZ8dZr5svNL8KJN5qEgbCoO5HgmDliA-xwVFggzLXjSI9wdnC6lEIQvF_VaFT0kZP0Xnl6uTOQGoryIMaguN1eqvNzel_xCGDP-B3UL_nqYXcRYyn79cHwYRW-pEIuLxjSLv8c-L9BlYw0oBc7DHIuwQLy5GOhGhOjTmytOn1woXs-dYvjuQRL2mhKVipnIFNRGJQEZOOGfYjYi6j4JLr8vYhpA0dL6nJg1tcJ7NMBySVd8eGsxuHlQcrLYgkWw2M9feQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=cN64iSEuG_UzbDAMUb_LBYRnzyjGum4VCcMNCTFwYfv8v8JlgoewyMzD_RBu7hi0v8E11UwPL1VOSs6wEkZ8dZr5svNL8KJN5qEgbCoO5HgmDliA-xwVFggzLXjSI9wdnC6lEIQvF_VaFT0kZP0Xnl6uTOQGoryIMaguN1eqvNzel_xCGDP-B3UL_nqYXcRYyn79cHwYRW-pEIuLxjSLv8c-L9BlYw0oBc7DHIuwQLy5GOhGhOjTmytOn1woXs-dYvjuQRL2mhKVipnIFNRGJQEZOOGfYjYi6j4JLr8vYhpA0dL6nJg1tcJ7NMBySVd8eGsxuHlQcrLYgkWw2M9feQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXB5RkykJhCpTaR4y-bik3jt_tYzj4NKXICxEVGVaDcmk9pH5RJbgOmrx1zS-65uwhM_q_ze9Xs4p7daGpEbl-lrMaDZ9mADNdP0JcMKvLVByZU_hes19Y_pX5C4uCdlFbN_ZsAQ5r3W-_alTjH6nuBeU_CQjxw_AG2SKHGExenA9bCEMpdJtBBrXvSkMWhE5d4OYbxMb54zUFPMbtzcZB7lt3LYh3sQoBSAHGD0h3JLkJKR_XXkHz-5e5-rOHY0U4jzi_Hb2UTnG7s2IwIoZyav3bDC18a6WAeHaufX35Uk-FOGcgkdO-A1rH2fHNNY0keRmaZzDy6xcJ_aqPEwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4Q4fLhZL7w0RrKisPU6CqgmdMMpAZKPhqjgaukyFQisS7Lxaxw-qWtazIaYWqrCD4MYsYbuyMk2shhP4z-3IgnvT8mqjpqNRNYDRWBrQtp2AKD5CfCURHfKj06rT1wTruel7brp0KyKvdfO4HuVEv18cUSPYAl8fN-MTpQkYFC4g_cxD9ttpzMq5Y954WIESgXBYns90pIUo3WDh9yr0XG-70P9QXPXz-dfH7umdVXCdUxLEd3bjhYlw5MhpRemvhK37fgUSEQGA-ahN9dI-PTYnvFynmYrWBTb6jerxeTj5EnXDpzgf9vinb1oFiklZjcMjjeVQ1e3AApAaLiE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH0lSmMOVGWz_HYA9HkMEbeSVp_afrq0YcLENv80rRfjy42g-RsofUUVh5Q36XZAOT7SaQv8BJVQIDAPeF-w4R6DV8W4lx-Q0b9n5aj2PSFSzYFTvw-aDdD14ZM2pZ8wu7NDxOWpbn2IuBAylkLhhtNsKFXW6iq0RIwoGYxmiZcRnru6ruEmDLogmVvqXqjKASVbSYz0AbuugtuunW0Nq6nk9_h9NXmD_q4Ba-yXkmMDUpWIJZdRSeurlCYqq8VOYK-uc9NCVxx6MMfnTOwzRd7R4vUQ-lzYuWP9DVnxjCDRS1-fBMpG8NhjTA6UD8o6Ri0Vb4qB23vBnPEMGPn4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=IQz2MOi8vW7ij5fe8iqNLdAF13NCUqg1TGNunSgSYhhzdOQspZ3vvIcKHa68XDabELEpOcW3V0yWk13Q9-g2r1uKjqUq9zNVJLV-Bqbzre19BE5pLO0FaFxLWZ2pidKExEFlRWOWc5LGTO7pB_1LG2AlsZ3f5OJ3orZ8EoWmZ71H-z1PbhFVhXyU5oJFGkiP7SvhcWfDDmREjC0qM6HVQWL_dULu3sZU7YJvQhflzRS6r-u54UPvQjq1uVdZlh6RPxlfIbLR9qW8MZcRiIUghB0pKGBNp9xu0-lfSdIu3pN4a-xg7mozAlPtp_PuKdFSYWwfZKnxMYGxlSrHNmkrYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=IQz2MOi8vW7ij5fe8iqNLdAF13NCUqg1TGNunSgSYhhzdOQspZ3vvIcKHa68XDabELEpOcW3V0yWk13Q9-g2r1uKjqUq9zNVJLV-Bqbzre19BE5pLO0FaFxLWZ2pidKExEFlRWOWc5LGTO7pB_1LG2AlsZ3f5OJ3orZ8EoWmZ71H-z1PbhFVhXyU5oJFGkiP7SvhcWfDDmREjC0qM6HVQWL_dULu3sZU7YJvQhflzRS6r-u54UPvQjq1uVdZlh6RPxlfIbLR9qW8MZcRiIUghB0pKGBNp9xu0-lfSdIu3pN4a-xg7mozAlPtp_PuKdFSYWwfZKnxMYGxlSrHNmkrYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=iwKfEn0vAjq97CdP_KMhttINnr8hYabBeiWt_i65NAw-yJJ-kCY3nUJIqaXornCtIVVjmlpmbsBnT0xZ4e6UWYIW8u-NkFAoK8ODuAw-tXPYjpxA50DUuHBUcR29ArSWpDWgCl6JwtMl4xx4PbY4LJcYylOizye_21BQ3UNk52Oup5wZH5oZBZQIHrS5u1jr9c6pB0zV3RMqOI92bte82HPwoyQLHaxJLuAJoSvMosHdNERZbFkVr8RZoqT9rbjtnGMpga5bZiz7_iPy2woTlfsK1a5UqZ-wpLZ37XjXq8rNtzsxrUL5z8wK2fbaeuNFdEDg0O4nwyX1Ti7QsIBfvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=iwKfEn0vAjq97CdP_KMhttINnr8hYabBeiWt_i65NAw-yJJ-kCY3nUJIqaXornCtIVVjmlpmbsBnT0xZ4e6UWYIW8u-NkFAoK8ODuAw-tXPYjpxA50DUuHBUcR29ArSWpDWgCl6JwtMl4xx4PbY4LJcYylOizye_21BQ3UNk52Oup5wZH5oZBZQIHrS5u1jr9c6pB0zV3RMqOI92bte82HPwoyQLHaxJLuAJoSvMosHdNERZbFkVr8RZoqT9rbjtnGMpga5bZiz7_iPy2woTlfsK1a5UqZ-wpLZ37XjXq8rNtzsxrUL5z8wK2fbaeuNFdEDg0O4nwyX1Ti7QsIBfvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRmOH-wjpgSZ4Wwuwc3W5IMokbxhQZVQDfO2FEhWG5W2Rn8YGakzJJJfOg0DMwxQRQZneG0extzkE5su1-NFyhjPrdi25e6WigwR50TTvR_Gyy3KuAVXIMZr5wim7s9Zzj1bwilpEqKfLkj5cG3IcWOP4VKX14iEks-4ST96q07XeesBXBHgke4_6nGQT8WXYj-Gh68HrW9Lwz0S8LFF-VzxXJVttg7XoHBxzAseXuzAKpAYOg1d_Wg7fbbQPW_L6v5oEf_cucEvAaiYSHlcXOuZW_BQKJC_NQ8LWdcV33NoIOrcC6KeOxSWLtheXdsnVVVQB06TJYf3LChVoDCfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=eEHELxE8GxuhgAPTvrUUlpk6Vjb02z-dcaiXAJope4vBjG6Rw-m9NBQS8sfw1aMgwv6iclNRkqzrzE4LQ8RiOtXc0m0dtyOolPJF5bsTssBORV3n_hjVYPYd1AQwut_eBwiyxd6Dd826hyS08WAz_HN96Sdb4v_hW2Q6fPSDLbMV_WehA4YQsOOaXxotitdEr1tfiodWV0rjb3QFBz_zfBW6l1D4B-vfj1oHPek87sLPUaDdrWM8tLf1k5IRvyDYqkiMC7r8Refcrn3n1qulUnQd9Reh1FlkI3mcdYHaGPIhonctOle3tZbZpLAUBI6Z9z9OP1togGbUkolae9Ex_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=eEHELxE8GxuhgAPTvrUUlpk6Vjb02z-dcaiXAJope4vBjG6Rw-m9NBQS8sfw1aMgwv6iclNRkqzrzE4LQ8RiOtXc0m0dtyOolPJF5bsTssBORV3n_hjVYPYd1AQwut_eBwiyxd6Dd826hyS08WAz_HN96Sdb4v_hW2Q6fPSDLbMV_WehA4YQsOOaXxotitdEr1tfiodWV0rjb3QFBz_zfBW6l1D4B-vfj1oHPek87sLPUaDdrWM8tLf1k5IRvyDYqkiMC7r8Refcrn3n1qulUnQd9Reh1FlkI3mcdYHaGPIhonctOle3tZbZpLAUBI6Z9z9OP1togGbUkolae9Ex_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs5fdR2HicDtv36IbkyZzGellcl2i_eFoGLjtk0S4thSi8xr848xQaz5hh_epAHVep1aLaU_iZgzVJ3_0eMreyu-krZohQkIV3jbGw-SeHiBPK9gEIhg1TjGXPJ65vvJBpH0b3gu5OjjH8Gfh_1u0s0g7XGSQRlAMNUp3P6CCI8ti4V4IgCAspczcA7X5nyt7ctR4pb0ZAETQnm0f2Q4-HiZGpNRKyRqayc1qpZLiXUBn3czOVjYrkhjclxAL7glu04np9AEI5kId3K4YpkplPucst1RyM5KMADGLLChIBuDbYPvUokXoh_zmc6Pw0tdxQrxMHluv0YrAgdw6y3YmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=mqkufQN0xz7N6YolSugZI3Bs2lWEWbkKsnQsX8syGYZ2S9e0JuJT4vnLR2kvamgT6ZI0vD8tTvtu-AaUmdiZeyV8y7mQAX1DJ9c2NzM8K3JlADtckTYrsMoQqdn2gXxK6NCmZ4Xay8laM0YoKJcf4QlMJSk25WjSO45LRch4gQLgXPtGUrnPvcmceAuF1Mmn0hScy-aOi82QXpTsc12LAc3zXGBZkK1KuXqMpf4q90OiCEBAzhc93gnVZhrm8x54m0g--dhUcccXNt6JVncKaHZpT33zL2FylSIGJ2dHXq651EnPzkmE4TfSJPqrO9pEy6WbKLC_bY4Oibbnk-615Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=mqkufQN0xz7N6YolSugZI3Bs2lWEWbkKsnQsX8syGYZ2S9e0JuJT4vnLR2kvamgT6ZI0vD8tTvtu-AaUmdiZeyV8y7mQAX1DJ9c2NzM8K3JlADtckTYrsMoQqdn2gXxK6NCmZ4Xay8laM0YoKJcf4QlMJSk25WjSO45LRch4gQLgXPtGUrnPvcmceAuF1Mmn0hScy-aOi82QXpTsc12LAc3zXGBZkK1KuXqMpf4q90OiCEBAzhc93gnVZhrm8x54m0g--dhUcccXNt6JVncKaHZpT33zL2FylSIGJ2dHXq651EnPzkmE4TfSJPqrO9pEy6WbKLC_bY4Oibbnk-615Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=v-QnkdWA47gxXBiBWmcBKJfYmG8BeXebeTJa5AypcJ_CvvclaqqMjdvToRzSLIFyfC_1guJ72cYC9gPsbo0zSj5FtQ1pppSdwTyg1-Omoql_WYPkkO_XjpI-fHoB0ULO-x-UM5MkUOMMf9p-npNT1-7jqxAbn0cVc00WhOTp_3cmpHGmYz--WmwmookIXBhZS3tSJejd4CV09gAE0W9o-VXuSoOloXJUyC57l5t15PrV7txGPFM-CWkGMQMLVNy890sWmkTrqwGxgDiWMdOvEy7IwxDC0KkqtAbRlb0N_0_ZlenNGnLASqwF6klMz5WHO928fOgp0WkSA70N5q3SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=v-QnkdWA47gxXBiBWmcBKJfYmG8BeXebeTJa5AypcJ_CvvclaqqMjdvToRzSLIFyfC_1guJ72cYC9gPsbo0zSj5FtQ1pppSdwTyg1-Omoql_WYPkkO_XjpI-fHoB0ULO-x-UM5MkUOMMf9p-npNT1-7jqxAbn0cVc00WhOTp_3cmpHGmYz--WmwmookIXBhZS3tSJejd4CV09gAE0W9o-VXuSoOloXJUyC57l5t15PrV7txGPFM-CWkGMQMLVNy890sWmkTrqwGxgDiWMdOvEy7IwxDC0KkqtAbRlb0N_0_ZlenNGnLASqwF6klMz5WHO928fOgp0WkSA70N5q3SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=YQIx46BZCIfyrUbmErd1o9yzohQBDIWQsXDOPhw-ky-ZHP-P8KyFgEV3siS4Ls5Mo3_Ru-IEKRPDxMwNT8d_2y_AhXbNpbk_A3mKmmqO0nYWnkL7nI0RVBJdxXlP5m-ebcZVGc3AOkeEd3LMto-s9yVLo5e-PASKvpTV_zgCoqjM_W7BYI-yd-2Ro5phTAYWw765Fm923DIJ_67NqEPedqK0WptsN_wpzs-6_Tu8oxBREV0tYTHv13BvAz5xA4jpW9V0BQQqqadgW6gz5QrwieQz0CDDC6X-wKNkf_MEBMKaMRxT3i9Eo2hZtwBRLIGEdLFA9cP9naD8K1Mi18WveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=YQIx46BZCIfyrUbmErd1o9yzohQBDIWQsXDOPhw-ky-ZHP-P8KyFgEV3siS4Ls5Mo3_Ru-IEKRPDxMwNT8d_2y_AhXbNpbk_A3mKmmqO0nYWnkL7nI0RVBJdxXlP5m-ebcZVGc3AOkeEd3LMto-s9yVLo5e-PASKvpTV_zgCoqjM_W7BYI-yd-2Ro5phTAYWw765Fm923DIJ_67NqEPedqK0WptsN_wpzs-6_Tu8oxBREV0tYTHv13BvAz5xA4jpW9V0BQQqqadgW6gz5QrwieQz0CDDC6X-wKNkf_MEBMKaMRxT3i9Eo2hZtwBRLIGEdLFA9cP9naD8K1Mi18WveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=CZbrsAVyX_dS3eHketBPBzleF18sQ7VbAZ92NFeTgbXydDsIPF3tTvSo119b7StyrQ4NiJqxynvfpr9kOEqICa9nOvMKZ3OPvw_3MrR50hgIBAixYjdVtfeTTZ0w5ppBI4qRcBUh_-HVpvoM-GIP3YEuuveqBeaiNc8kAlf_B2YDOE78bi7ljIf9b_s0RdulCQEvmCRjZq1Q7h42PK4Pntwj2kmZPp0KdfNRXLf56Y578xT9bzArc4tXb-s3lYN5AR6R-6dTiY8jf2pnltojqLNvNFfXn3yklFQQnsQogkpC5nGpiAtxQwgivsrbIxYH1TdV24OBLvbKuU3Y4Nyfig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=CZbrsAVyX_dS3eHketBPBzleF18sQ7VbAZ92NFeTgbXydDsIPF3tTvSo119b7StyrQ4NiJqxynvfpr9kOEqICa9nOvMKZ3OPvw_3MrR50hgIBAixYjdVtfeTTZ0w5ppBI4qRcBUh_-HVpvoM-GIP3YEuuveqBeaiNc8kAlf_B2YDOE78bi7ljIf9b_s0RdulCQEvmCRjZq1Q7h42PK4Pntwj2kmZPp0KdfNRXLf56Y578xT9bzArc4tXb-s3lYN5AR6R-6dTiY8jf2pnltojqLNvNFfXn3yklFQQnsQogkpC5nGpiAtxQwgivsrbIxYH1TdV24OBLvbKuU3Y4Nyfig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPqBECEk6v2zzoITeczJ2NsN7xOgTfChpfEdm_COPpHwyyHppuGUK4-cePwiS4SMsxx54OVC3a4TofQkmFh_f13LGU630wKoDZFCO5getuX9zfMLu9ugRIl_dVAu6soetIzgTk82YKywM4_4ohmUs5GiUPKkCVTUEQJW4vYA508Itg3vYSb95ZsQg_W0qlGMQdetmxF_4k0JohTLl4kyeA2siU6BXQYLVDn9LBAcSb_YVpLasjqxHQawTY4X5cy6GqCgMxEZpLwEC_uKvUnxg2sUvTIRKYT6Lm6ZrATtmqX-bHJniwuJimJriVD2MGQ233uB8xs2NILJb2yKCZee2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzf3tlVeiF1q-e04JThbdU4KlPGsANvHtM9oQkcWOXcGUFJJ9C7E5qFLEZ9j8ZQ2H5OQeb5M1yaJ9aA4Jap4pR3JkJreeebn0_mfJpnDOmR3AEONDU9JdTb_b7lYIqy3IdCxPS-nF6stk502hUM5_n372v7c2IkM1nE8_PvYsGOjUz8tDYZQvc8dMy5QEoS7Tye-726Tj1Kp6WQVtWJb4NHE00oXS58KerD3PLZRipbWF80xUj84E34wyIB0Kv6Nzw47LaSbbSIwCGAiWDF_z1Kbj-HLDZdosqmm5F5HOJFZXRt6c0xCrV2lm5wTd7dPt7D09NIqAo7mZhNEOOx9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMhtcQ2d5zKuSAOHKrlM9trYmpNOIA-TOTXz9CV9TUXjAZoQyR0UwtA3BeXh2W5VOJOuDnw8Vsdg2EbiHy4gu9k97Jz-Cu3MmbISxlrsl-oHtpPH05LZLUyNMEQgzJBe14SaGzmlEb6IcISgSnvMc-I0x5qKkpVzPbcPhoXZ-VwyAHfwOPPm2fVcOlK0u6fEowCqpb9wVPiGhwK7_amNqpFt4dpave5YjIS-N0o0iXWjmm_PVg3kEEOpCtDVkF0x7M34QhouYAQf4bbHbaqPj1ZKmfqql4GY7gisRqqbxZGGZN4MJ4phZfd5nto8V_rnoG-bId2lTSKKRcRoInK8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSY48DJZDpdSdo-FRLEGMQllG1PSkD7_RIEmicDhnwG30lw39TH0dl61Jr3m9BQQbiq0ylPA-o00lRT1YU3u2_K0578d-eGp6dladq_FIH6SDK54psjs7FXe9eafGtifjh2LGAc6AYU3JFIT9_ySMeCIUl016cArAWn7NLFqYRuNJRBACCQX9fclMc1uG5Weabw9FUBphBqMMQQV-5f3B2OOMWcxG2bkiMk_x12jz7hV1svyo-K8CP9SiWFo3Iff0fpoWH-O4Z61MRJZl5Y-WEG091W6LrpSu9yLmh3Nipr_G4XjxVVkZ7oStuk-aQoaGpvE5bnBRI4_mrWyPlIOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp9gpVSzzTa9jy_HQ42nHqn2Jp8Qs0Y4theE3e0koNmpNkRI8iUjP7R0xdehQX5NKF7yOi5Bw-WcO-VMJnnBczRnm5RDNFaO-ukmtxTNobhb1V3jSIP8JkuVCH9Vd06t2uMSnXi4BopiZLFtKcYFUK-GafOqHT4DKxPgXnDKCqkgCKUpydosIOBFBlaxdwUFQSt0LvuGyBR_3UYMUNXS9dA6-vlaU7Y3Op6Iaxno_Dcfa32CrCTmh8uhvwCwgTEsLYSSvRIWvrIFh7-mh0buUDLqI51Cc0vuvuzWYTO7w0yvQFh6JN8qGrJ53SZ_4r7rwASUayWv41IaosZ-H9GyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=Ls38Az4KO6JABj4LaThc9ZIS4IbqqQSuRNVOotTaA0gnZqj6hHW8uTgEO9DC5CfudQ4s3v62m9oGDp5e4N6AQith4rX5oyWG0HLfXfG2nO9Q4YiaE2m1JnWG9PLDpqcE_swAkoHzoz39yGCvxBVFSo2T5IEep6YQc1h7q0kBbhshtydtq5m-RAG4RfDwy8jxgGbleke8otGm33jN7_x1Ce5vwbD8gxxyY4Ls9CMODxM5G4ciU7irC05M2yPhzGPlSR5aiOWn1joLmuBwSnvqiWtZ1f_9Lqx1HXDpJnVNMGZHWYLPWcDzM2DfxFf4v15S3tzdrCa2loX7meEqVQuzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=Ls38Az4KO6JABj4LaThc9ZIS4IbqqQSuRNVOotTaA0gnZqj6hHW8uTgEO9DC5CfudQ4s3v62m9oGDp5e4N6AQith4rX5oyWG0HLfXfG2nO9Q4YiaE2m1JnWG9PLDpqcE_swAkoHzoz39yGCvxBVFSo2T5IEep6YQc1h7q0kBbhshtydtq5m-RAG4RfDwy8jxgGbleke8otGm33jN7_x1Ce5vwbD8gxxyY4Ls9CMODxM5G4ciU7irC05M2yPhzGPlSR5aiOWn1joLmuBwSnvqiWtZ1f_9Lqx1HXDpJnVNMGZHWYLPWcDzM2DfxFf4v15S3tzdrCa2loX7meEqVQuzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=Ss2N862_z8LUIDmbZfl27K71jXs6pOJ_Es4Vbs1IDaIiClziiFe9BpX-JqRNM-Ypy4l1NFhdmYGeLCfWFN-c0QdDKxWhQmH5x6UKoRoupZqb-QzLMRm8DfEYX4yDUhAed4d8yYjW19X8NAanuDCUhfn-UY7GT8_80Xox091lzQVNMtGsKqxhYHnRWiI7XaXYKXTwg8spOQPNWmp5mqO-P6cSBwsRJwr-iGe8ZKWHNT_J_DP1HzjMDwt8IdLfKrJzkE8g7yHrveDKCKL17T49q7WikRi4l7-xExf-y7tj1WP32ot0zvR8UYmIn1B-gQhoaR9kj_EslMChYU85Y2jcxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=Ss2N862_z8LUIDmbZfl27K71jXs6pOJ_Es4Vbs1IDaIiClziiFe9BpX-JqRNM-Ypy4l1NFhdmYGeLCfWFN-c0QdDKxWhQmH5x6UKoRoupZqb-QzLMRm8DfEYX4yDUhAed4d8yYjW19X8NAanuDCUhfn-UY7GT8_80Xox091lzQVNMtGsKqxhYHnRWiI7XaXYKXTwg8spOQPNWmp5mqO-P6cSBwsRJwr-iGe8ZKWHNT_J_DP1HzjMDwt8IdLfKrJzkE8g7yHrveDKCKL17T49q7WikRi4l7-xExf-y7tj1WP32ot0zvR8UYmIn1B-gQhoaR9kj_EslMChYU85Y2jcxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYeyXsgWZwykkKdeEbg2T9cAunYg8draHWgrZOkMJJAk4EJp-r_K7a7qyFa1E8H8AzxYge0LNR-O5XJoOBqA4-ten1YPGevVtuGo_fk6--5ceDtU16diM4LSVugZWh0PLzTX7AZSlgLWqmJEaCGiBPMAX32zJj_bSEHmeMhYH86UAA1mVcxP1PKGDAwyDVtlLP-8UcOmQWkL8H9bkl3d0QVsZD-6965Gqm4iej16Wjdr41o_9DBoXKPb4KEX5eCwUeH2iTKwEoBD9AU5D4ef1pEU7Ajl6Hkcn4vDU9D77DXdvqfUJtGOcUTyDo_46h8Jhwopi1O5gq2FUrUvTsiGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL4zPzJwWb-1skSY9ZyRnGLpqc7J-x8J3j8xDdhoAR8_dygIyq1BF8FHaMbXBAYMjSdZghfU_5m-fTK5CSdi073m0VUjZ2qz-aa9y1DoEM7UMDewRLngS5fgVMLEdvOIJ94tkddTFQXX7Us74ggnbKS9QPOBMA4FIltjiua8fjocw0NxJjGETnd46I-C0IOY-1QVvajwEjy8MXeqngoLzUurUznuikjuQCHZh9LCfl5yS8RVnWmEe1BZaGWWwwO9yYGzMe2m4FSIUtWDlSAAeRKgitqe0FlPD_PhuAuLy4MKERluCGJ7nre4jhruDLkXpwprhs9wcivb3wiLEW8tmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=XE8s0hdRjhhXe_0mP-LcpvdvPvb3BI91X6uujK9MnxL1mbO9stpBa9U59BDLJhwaK2fakxbiEc92n6LdDvDeeC-QfILoVbqjcJPZBAllczpuWtgzpeVNyEnXe-mjYPET0JZKgYEltWwvcfvBFnNQjLixfyUY3ui8Dq5eb_MCrf7B4Z8tt0gBj_EHwya0IzGhrDCuop85Sf393xpzpy3FRcKDVX9lb9ejc4rtmtIem2pDvzX7hsGoM8lnwaEVIR9zZyDVHtIGwqOUySFUBkoe-Nglty6oH_dhGs72bbTqtaQJOjfXw40h-vsnttx1cI44Ihz8sUPZG47k3gLjX3Lgow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=XE8s0hdRjhhXe_0mP-LcpvdvPvb3BI91X6uujK9MnxL1mbO9stpBa9U59BDLJhwaK2fakxbiEc92n6LdDvDeeC-QfILoVbqjcJPZBAllczpuWtgzpeVNyEnXe-mjYPET0JZKgYEltWwvcfvBFnNQjLixfyUY3ui8Dq5eb_MCrf7B4Z8tt0gBj_EHwya0IzGhrDCuop85Sf393xpzpy3FRcKDVX9lb9ejc4rtmtIem2pDvzX7hsGoM8lnwaEVIR9zZyDVHtIGwqOUySFUBkoe-Nglty6oH_dhGs72bbTqtaQJOjfXw40h-vsnttx1cI44Ihz8sUPZG47k3gLjX3Lgow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=qfMNjLJI1T6yv-X5Psm-OgcBkZ_UgYbdvkkVAYB8Pd0T5a_H0L0AUy3tkPlVq27wMnMYV3ku_uKDfqDG7lEbznA_WxflReTKyZ1VCubP8WRFnD8_y4kkCy-OQPNm-3LnfOXt0qTLaLG3yNhAXl9v2GdTGFwOmDJYcjDfc1IlJRwK98w_TRuHShsipOlnU2jVSsvH0OkR_a7qKVsyHtgZLcJfMVXKWnasor5VD3eWEYxG8ZsxKNhB5OAsuFW5e5gBNp3w2ztqGi2F-3BEf1zcnvipv4G39afmVq_150Y8jTQB8sA-4M3jLyugOXcwl7HKq6OJqWvF4R3lStMrhaEukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=qfMNjLJI1T6yv-X5Psm-OgcBkZ_UgYbdvkkVAYB8Pd0T5a_H0L0AUy3tkPlVq27wMnMYV3ku_uKDfqDG7lEbznA_WxflReTKyZ1VCubP8WRFnD8_y4kkCy-OQPNm-3LnfOXt0qTLaLG3yNhAXl9v2GdTGFwOmDJYcjDfc1IlJRwK98w_TRuHShsipOlnU2jVSsvH0OkR_a7qKVsyHtgZLcJfMVXKWnasor5VD3eWEYxG8ZsxKNhB5OAsuFW5e5gBNp3w2ztqGi2F-3BEf1zcnvipv4G39afmVq_150Y8jTQB8sA-4M3jLyugOXcwl7HKq6OJqWvF4R3lStMrhaEukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=PPDjfuPEN71TOnH5eSVEKIO-RMwSvjAUXEQZyDCMGDwTtb8_81f2SZFEBCPCJopaKnpxgyJKhho9tnh9E42x_XVmZ6NCsmeVW4nFKDx-NLTE1TNzsaUMojHvknHfzCVdQW_LWVnyYfz4Cce8KcIRF0CbSgOyxVFb_FlhBXwmzKO21RbNkCMsBBnCQWYjiVEw4b4AfIxhcLwa1571WeoW1TC4Eogfs_oHSU_uM46erTCZpCBid_hJXDndyvIjw_2Cb5J8CbbX9-JQh8p6DzzTnH77OajvH5Vtne6uDBcGDlsGqppCjyyyf9Xr-SCY1WL72nghG2qjMfboIRo52TWpqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=PPDjfuPEN71TOnH5eSVEKIO-RMwSvjAUXEQZyDCMGDwTtb8_81f2SZFEBCPCJopaKnpxgyJKhho9tnh9E42x_XVmZ6NCsmeVW4nFKDx-NLTE1TNzsaUMojHvknHfzCVdQW_LWVnyYfz4Cce8KcIRF0CbSgOyxVFb_FlhBXwmzKO21RbNkCMsBBnCQWYjiVEw4b4AfIxhcLwa1571WeoW1TC4Eogfs_oHSU_uM46erTCZpCBid_hJXDndyvIjw_2Cb5J8CbbX9-JQh8p6DzzTnH77OajvH5Vtne6uDBcGDlsGqppCjyyyf9Xr-SCY1WL72nghG2qjMfboIRo52TWpqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=h_AfQRJIhyuBeWQ7v_YSYq4Q2HJ6bhmHdruIB-_Ei8-DvXKqmW-uyDid7qS8pJ7mReaaVDqMSifb-AbYoOBgxbfjxZQzdRImeoLWvQ1BDsxY5ptfWZCA-bVDBzeJPwo_XUUJtCPtCSf4DgDSoj6mpHanzQPEdNpmtet6mJL3BdDh1nx0J3-Ehxvfrlj0S96Z0p4G-3MIg2MNCEjA8wbHEigoglggoUKwAxH3bZNbX4HdgXMsKh_taxTCtJ8HaWgS_XZTNQhhtH3B-YKY8G7hxECLYAtvdsL0uHbdeNsZtlYEqQ1x7eTBAAqTuijT9O5gVA1ALzzXHKyYz4fVXqf8Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=h_AfQRJIhyuBeWQ7v_YSYq4Q2HJ6bhmHdruIB-_Ei8-DvXKqmW-uyDid7qS8pJ7mReaaVDqMSifb-AbYoOBgxbfjxZQzdRImeoLWvQ1BDsxY5ptfWZCA-bVDBzeJPwo_XUUJtCPtCSf4DgDSoj6mpHanzQPEdNpmtet6mJL3BdDh1nx0J3-Ehxvfrlj0S96Z0p4G-3MIg2MNCEjA8wbHEigoglggoUKwAxH3bZNbX4HdgXMsKh_taxTCtJ8HaWgS_XZTNQhhtH3B-YKY8G7hxECLYAtvdsL0uHbdeNsZtlYEqQ1x7eTBAAqTuijT9O5gVA1ALzzXHKyYz4fVXqf8Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=rh0zfcVCabykBhhyl-PfjVYj0Xp14Ff7F-7PENQtsTCbdegbz6N_v2ezITwe0oKbdE2IcA8_v_FvFTzyhXr_t0IOnUbanN1xA36tFPUG4YAFC9J1y0-_Y1qOGoqV_cSPnWUC5kzWSU8ztkNOmF9WhKsp94IHstk1s9NgIShSrBJD-akvungKN5dAgDQ2aPh1qgMA0ksunnNt87kBh_LFJpDAcFrllF4TKBmAFHv4oXavM855uXpN8-tcXOHcW5OnBsOtd9xIJTmwCa0MdjQKtkwlYXe_CgNpJdzgAgKnZN6eP-cZryNL4bvZWWErvb8oGG9dnHhGBrwzDDflDARYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=rh0zfcVCabykBhhyl-PfjVYj0Xp14Ff7F-7PENQtsTCbdegbz6N_v2ezITwe0oKbdE2IcA8_v_FvFTzyhXr_t0IOnUbanN1xA36tFPUG4YAFC9J1y0-_Y1qOGoqV_cSPnWUC5kzWSU8ztkNOmF9WhKsp94IHstk1s9NgIShSrBJD-akvungKN5dAgDQ2aPh1qgMA0ksunnNt87kBh_LFJpDAcFrllF4TKBmAFHv4oXavM855uXpN8-tcXOHcW5OnBsOtd9xIJTmwCa0MdjQKtkwlYXe_CgNpJdzgAgKnZN6eP-cZryNL4bvZWWErvb8oGG9dnHhGBrwzDDflDARYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=m7eawilwFs-TchTMj3DrCZILCaailpHXaXHSMqYsdH-X3CsLYnTD9PX6etJ5g9H59t8jSboV4K1SOyoOFJ_ZeZ2Vo92o4kQPk7E3Etop0D167FdpObet9zw9jxSTeKjhNRtjHTCdNu31pZEcda7jXdnLLHAxTJqJTCQG0s7vG8bLf1vA-Q_mzy5qKTPi50uLtDvVX0U7h_B70VpwpPBHHsCIWuaTbrgjGZbxPJ3v2jz0S5AJgRh0saKUVnfpdzadRKPZTmY65NuZoDtrZGOk-UKHE38T_FuAYUFbqaElwQmeMwbWpl9gcYm08pjpPuWtOqDPAQiS5d0gPo162-9htw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=m7eawilwFs-TchTMj3DrCZILCaailpHXaXHSMqYsdH-X3CsLYnTD9PX6etJ5g9H59t8jSboV4K1SOyoOFJ_ZeZ2Vo92o4kQPk7E3Etop0D167FdpObet9zw9jxSTeKjhNRtjHTCdNu31pZEcda7jXdnLLHAxTJqJTCQG0s7vG8bLf1vA-Q_mzy5qKTPi50uLtDvVX0U7h_B70VpwpPBHHsCIWuaTbrgjGZbxPJ3v2jz0S5AJgRh0saKUVnfpdzadRKPZTmY65NuZoDtrZGOk-UKHE38T_FuAYUFbqaElwQmeMwbWpl9gcYm08pjpPuWtOqDPAQiS5d0gPo162-9htw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=vmGX9rh635lwShefPPYeppOPfN8WeijB34qxasSn_jU6QXuyiuXVg36nT-fHAqVmiJbXCBUMaxRBJ_LXZNwSC9Y6Csp5KmwfPD8pYQvxYmJ31uRDMyKUkrf9Qjqfswq3pWHCDClP2O5qRDWnCGmcc1TwlniHz-6LkfU4wmowt4-kynBUOsreNqX2jmVy0JCci-QXL4bs8TTTSFI4B3O4miJIT_wF8srST0q2MaXOizLPLH3OKoej2sE3Mwk1RbD5q8-1OAI8Yxz126tqbxM4BSlfMCmcfvF5tBX8u_aU36IXKDp5F1baAyrImuP7oCeSpJmTwiFHo0645BGXROc1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=vmGX9rh635lwShefPPYeppOPfN8WeijB34qxasSn_jU6QXuyiuXVg36nT-fHAqVmiJbXCBUMaxRBJ_LXZNwSC9Y6Csp5KmwfPD8pYQvxYmJ31uRDMyKUkrf9Qjqfswq3pWHCDClP2O5qRDWnCGmcc1TwlniHz-6LkfU4wmowt4-kynBUOsreNqX2jmVy0JCci-QXL4bs8TTTSFI4B3O4miJIT_wF8srST0q2MaXOizLPLH3OKoej2sE3Mwk1RbD5q8-1OAI8Yxz126tqbxM4BSlfMCmcfvF5tBX8u_aU36IXKDp5F1baAyrImuP7oCeSpJmTwiFHo0645BGXROc1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=NUHcoQi3lrEUdNABcIhSPTX2BO4W92d6uVJDQffkZeMQd-gck7mlLfnTr6y_qjHF62oKcAfR8vxbgtkaRcb8LsBVDS9-wUFHTx3Xps0BkHP4JiPd5AdeREmbk3R2d9_lpCQ35ofV4A8jxJqrBiDUAPY9z6Rxec5AhYjI9uiwkaSIHKe3CM6vLzi_TrKaDH2bOYli2Yvzo1Zkz1c1ZQuq0CreNWJyZdnfJR_uTsWqcRPeygyb2QvvyLk70gOCZev4UBWXZ-Ss4qdms5r--gh5a9FLSu5_MyYy005uhHYox1PRqYNzq03irRyHmh4hu9jkycTlHu1788-FYgQM2xE63g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=NUHcoQi3lrEUdNABcIhSPTX2BO4W92d6uVJDQffkZeMQd-gck7mlLfnTr6y_qjHF62oKcAfR8vxbgtkaRcb8LsBVDS9-wUFHTx3Xps0BkHP4JiPd5AdeREmbk3R2d9_lpCQ35ofV4A8jxJqrBiDUAPY9z6Rxec5AhYjI9uiwkaSIHKe3CM6vLzi_TrKaDH2bOYli2Yvzo1Zkz1c1ZQuq0CreNWJyZdnfJR_uTsWqcRPeygyb2QvvyLk70gOCZev4UBWXZ-Ss4qdms5r--gh5a9FLSu5_MyYy005uhHYox1PRqYNzq03irRyHmh4hu9jkycTlHu1788-FYgQM2xE63g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDECFf_5d2p1tM5j9dl71IuJUwqXd-tJ-uupCNW9lsFNdhXyuFHecUGLbxoLhFtUf9DYs6sNoCD9IjAyU2LVnpJ6IcLNfdms4xZ9DSIgC9YzaAx02LPdgKHrIdSqPe0_wk1Em8vP2Ppwd1ilm_KJfrbEY1EbR7Ua9lD1iYySYU_W9YLEF4kgxtMXWVU-xvRiMrKhgeep61lfiBeodMq3QK6O3ivHq7lqxxETdndSAb3jRyE2I2ykhNcRXrUeDoRJiX0hWhAtwxYUlc2CYsjAQc6JhTEcUZI4k7eZjpmmK6DBfHypB9HJqg6yNxNMWcUpPetDb1zN2jMbcfIvFH57Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=l1eDxz-8o3OPEy2vWd1gQXErDDXz3Y594clS8_VICt5lRDTiqXvPJRcd3o1TF08lm7SrGIhTqN1_mgfc-mH51Aaa41FC-C1EYcYqRNf7cn306hjaEMD_GOHixmL_HDWUEiwNh6bj4VknqB3HT7MW4UiFyVpGP4BwX_TGVbCUeg116YC5SikqSaB3mSd5BjAAXvqiF_C_BgNCgu1SH7XHlUOeFDdpSPf-lupdMe_lRzTEQTUrnifOTzaF7T9VyDtgKeFrp7HHQIf63xAaFyImZtqf7LvmhKTXk_CK7oGr4IKkiZJiUxDOJ4nj-aknNOcq_NowW5JD0b7QiOkTsl5m5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=l1eDxz-8o3OPEy2vWd1gQXErDDXz3Y594clS8_VICt5lRDTiqXvPJRcd3o1TF08lm7SrGIhTqN1_mgfc-mH51Aaa41FC-C1EYcYqRNf7cn306hjaEMD_GOHixmL_HDWUEiwNh6bj4VknqB3HT7MW4UiFyVpGP4BwX_TGVbCUeg116YC5SikqSaB3mSd5BjAAXvqiF_C_BgNCgu1SH7XHlUOeFDdpSPf-lupdMe_lRzTEQTUrnifOTzaF7T9VyDtgKeFrp7HHQIf63xAaFyImZtqf7LvmhKTXk_CK7oGr4IKkiZJiUxDOJ4nj-aknNOcq_NowW5JD0b7QiOkTsl5m5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=Ip_B-bTyGdg6qqS_lf2dUfZrq86l5dE50GhURlhdd0x2ShnOtmHI_ksNesz50U4PmU4-Ok8oJxx7ZxtW9qJvXK_ke0Jngivnx75D3Cd1oDbqkNnPQ7xeeCvrnOOIon98HvaNvpd4B8T4qnClhjzkn_7_5lVYYE7DTq9RxpZl1X8owVczw17W9sZeIzABGZEXlqlRbRjIW_vsvi4Foa8HWoXKzoYV6Et3uWfsxo1FAd2R-0SmaF8qlkg36exOmU_swVVnIap5IjB2NLSrRESaeqCXVwWFO7kk_2QnFu3L6U_oR2PD7oU4XzlsF99NXPbn1jquPQFUQvksIRBgh9Nz3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=Ip_B-bTyGdg6qqS_lf2dUfZrq86l5dE50GhURlhdd0x2ShnOtmHI_ksNesz50U4PmU4-Ok8oJxx7ZxtW9qJvXK_ke0Jngivnx75D3Cd1oDbqkNnPQ7xeeCvrnOOIon98HvaNvpd4B8T4qnClhjzkn_7_5lVYYE7DTq9RxpZl1X8owVczw17W9sZeIzABGZEXlqlRbRjIW_vsvi4Foa8HWoXKzoYV6Et3uWfsxo1FAd2R-0SmaF8qlkg36exOmU_swVVnIap5IjB2NLSrRESaeqCXVwWFO7kk_2QnFu3L6U_oR2PD7oU4XzlsF99NXPbn1jquPQFUQvksIRBgh9Nz3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=N0pRhYFajElaVWiY3qz32iAPaC5uv4ONVelx32ek6DF0MTbj27yqi41wKIYfYbgCzO1NXjq05zsuRno1j9skA14OK_7seZ-h5-tpWjti_ELcHP7zro3Wll1wfGDSh96E2vOFTYEdKqkWTfGfGNmQb-VRH-LzVzVVsd-H97tTJpk4t7_bnDK7T6Q_seKJLhxy8Ej1lb70hQDjx_PJxwiS3_e2tXiuyjrfIFFil4T7w6yN5NLNF_LIiZzwvurN9T21d3-97cR9A3uQ9Y9ykJ1XpZKvCaguo5dA8dm_7vcpmUS9AgbFDEmuPa3gpGjJyk6zCrMsJL-2-4SDJp_gFKyXwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=N0pRhYFajElaVWiY3qz32iAPaC5uv4ONVelx32ek6DF0MTbj27yqi41wKIYfYbgCzO1NXjq05zsuRno1j9skA14OK_7seZ-h5-tpWjti_ELcHP7zro3Wll1wfGDSh96E2vOFTYEdKqkWTfGfGNmQb-VRH-LzVzVVsd-H97tTJpk4t7_bnDK7T6Q_seKJLhxy8Ej1lb70hQDjx_PJxwiS3_e2tXiuyjrfIFFil4T7w6yN5NLNF_LIiZzwvurN9T21d3-97cR9A3uQ9Y9ykJ1XpZKvCaguo5dA8dm_7vcpmUS9AgbFDEmuPa3gpGjJyk6zCrMsJL-2-4SDJp_gFKyXwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=GrwUkbHsQxahppHsfVnneo2EEXb1nIdWYIqD4YNGvlFe43LLlwM43iMsL0A_wm2NI5AbTvXCaNxt4Rs63GeP9MkA0d7HMEeyGCBwdwHUCdX-O3kGBMuYQjicopHQwdXZ3R0Uwy3tqA8dpHI6k_Iqtms4waSaxxKaFQOgWvshye8dXYTIFoKtsIocN2mxnfaRtN6KrUH1hMxyfq1R65ZX_C7D8h469u017BM6Y0TuFIGukgT7-VVs_veJmA7XzUBBcZyYmc-SCDa_bDGsijuzZO9eIc6_Qm8ps8bfVhfA1nGuVyCENHiPZlqIiQLlk-wZKWvtLVJ79NpYi6p6Jo3dXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=GrwUkbHsQxahppHsfVnneo2EEXb1nIdWYIqD4YNGvlFe43LLlwM43iMsL0A_wm2NI5AbTvXCaNxt4Rs63GeP9MkA0d7HMEeyGCBwdwHUCdX-O3kGBMuYQjicopHQwdXZ3R0Uwy3tqA8dpHI6k_Iqtms4waSaxxKaFQOgWvshye8dXYTIFoKtsIocN2mxnfaRtN6KrUH1hMxyfq1R65ZX_C7D8h469u017BM6Y0TuFIGukgT7-VVs_veJmA7XzUBBcZyYmc-SCDa_bDGsijuzZO9eIc6_Qm8ps8bfVhfA1nGuVyCENHiPZlqIiQLlk-wZKWvtLVJ79NpYi6p6Jo3dXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjVVuoKh03Tj-gSgPX9wYX5P-s2qlkvk4blWqWJtjaXQ1VM1ccbz96NdFTU-l39wBSb0B7c6x5_qGUsy3xtmnp5hsvN5inTO333wuJ12FQEepxoiLwHVBo2u4xREYwH1E6byjbozfW3rhYRffDst1SFjwBdy3UqW_k4lcGB9Fu9FYdCDfrnDWultnu4Q_VlkvywjCSKDA7rr4B5cxl3mJQpfV5x4T4lkT0R4_wTBIeoLlvdWyS4r5VQSvKTVUvKmFDgficF8DiYvOCs6EfwHITZIzmJLXMt6i_mu2coPqHNAVZc2UwM4iy6YrEu3GsLeiymvoMMX01D22Vuf62gZhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkvZWlIymPnTlI0hY3ikmfWg9wLcQgHe7_5oRBEEj33AwzUowQujadVSHMP-aIwCbuX70YtwJPogPFEn8s1DwgN4NlQk41WZEx9m_dCC_FYyy3yPVKAwQPqn_RCfmIK3ktfpfzwXHfkoSDGKEugnKlRv5cDJya2jiLsy41agGMCCLninIkqjXBW3g1_0tBYlIJKDWfvs1i9MTyY3-M9sXhjtnYQDtJDn8HOFuSXmbYkF0eza6wOwpV4C2v1N9vF5DQS4_6ryT02NomalaGWjqe-KxovyIXpUlEbR4kAj967QI5bJMpT5AOCEb7j5fne7hoJwqnf7Zsd8anOL4y6K8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pl_4sSviwwI9al6ASnP8ZcGSO66GscxUBRud3aLgtNoATCWSOTIG8lD8kTTfOexViIEDHt0B0DHmQxfBmRLZNf4qTXtUvF1TGiqjeLTbiE8UiKFyftkXYktZ_AA5NCegDIh43MehctZFMTsi-qk6hB9zHjyoJWRG7FOzmRQVQXw6n7zl3EEejAFt3RZcgnMGZxFUfamsY85xujxJJF5FGTyoraGhBMwfDbDLjpJpLH1Np97CLGNQM-lXkeEzzCGPC5Q9csM8qJKNXCWengBOUHhX3XIlapvVfeVE6NVfF5a_d_-2BTYNLH_4pkWwhiCuULFw6IKB3lOhiChJ9-kaMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=jlCgsOLmcEOZ_nXHsiGjE6Ven73G7zUQcGJLLLHZ92ebiGeuEABWWN5KA8x8GI-G7A7AfgfuvCMPmsA-nP4Pwq2bs6V2ja2XczNOpdXo_yPcNQ1kW8BHIFnreElpZl-V_WjCkqJJCuoazP8YamRMqwBHQB-r4xRVUMdnGX8rCLQ-AslDXuLfHt3DsIXEQFJNg2rFat5qjN9b9idpTRGox3yZqrYuTnoJbqpe8hjho9cP3SEDcWlRjX7qT8KXpG9Kz_M94OvYERJvdsNcxV8jkC20Tv0Jn3SciY3U6uc_wXK3x_Kv0XCP7hEP-04px9NKnMwy0MEKNzIpSfQpnuhDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=jlCgsOLmcEOZ_nXHsiGjE6Ven73G7zUQcGJLLLHZ92ebiGeuEABWWN5KA8x8GI-G7A7AfgfuvCMPmsA-nP4Pwq2bs6V2ja2XczNOpdXo_yPcNQ1kW8BHIFnreElpZl-V_WjCkqJJCuoazP8YamRMqwBHQB-r4xRVUMdnGX8rCLQ-AslDXuLfHt3DsIXEQFJNg2rFat5qjN9b9idpTRGox3yZqrYuTnoJbqpe8hjho9cP3SEDcWlRjX7qT8KXpG9Kz_M94OvYERJvdsNcxV8jkC20Tv0Jn3SciY3U6uc_wXK3x_Kv0XCP7hEP-04px9NKnMwy0MEKNzIpSfQpnuhDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq7eX_8RiKnHeTk9BOFBMZnhKeDzjejxkjiEBWmHwU-vrG-0gP4WFrF-YDQvlPj9YRiDCoxR8t-7F2_3bE4XYM7On4kOl01rwdmoLq-OiENpXd76q8vj2YHhaIhFtBAImSriH_ogyyV-5vbazaqSy_NQxINa9rLSTFxZFYc_zgpxnbSkCHzP1Rn0FFg7R0g1sW4OKSXz3JWUNsqgOHkOYGVZ207EXtZc2e4kRWugyAAGGoMNGLCXfpg2gODNQ2X9YFfkxkcFx0Qnvj1lyJoNAZS8SXVo_zRWLl4Z0XGTBVq_FMastqHMWp7c_5-TGP051NcofsQHGRqtii4lxH8fiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=vTM9HV5Vtm-2VbBGXQqp2IUEJyVgcwaHKMsAfcVLXK61t5hXDeOFlWibN1545sGzErj3GKn-qtUpIerS7pG_GDoVDI9Y3gGgXfLOEKZYzNTIropFrrJCCeP3vKqbBSQCn1Wg0qJRzSsRtbS-ERsUTzZCtRT0FbAaS0I6yG2wjBEA2iZMzEiIXwISvMlbFjnSZmTbtATNR4OVo9GZPsRm-wBLLO9PxzAOC9sqMHYOxdy8X8drhNFBk9uNoLnXsOSC46TceOTsUXoDcSBggfQgqRZYv8FC8mV8JM_4SRe6-v1ncbCCKjtshR2nRXsWgqgqHB4qJJFQmYWVUmvJwBjuiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=vTM9HV5Vtm-2VbBGXQqp2IUEJyVgcwaHKMsAfcVLXK61t5hXDeOFlWibN1545sGzErj3GKn-qtUpIerS7pG_GDoVDI9Y3gGgXfLOEKZYzNTIropFrrJCCeP3vKqbBSQCn1Wg0qJRzSsRtbS-ERsUTzZCtRT0FbAaS0I6yG2wjBEA2iZMzEiIXwISvMlbFjnSZmTbtATNR4OVo9GZPsRm-wBLLO9PxzAOC9sqMHYOxdy8X8drhNFBk9uNoLnXsOSC46TceOTsUXoDcSBggfQgqRZYv8FC8mV8JM_4SRe6-v1ncbCCKjtshR2nRXsWgqgqHB4qJJFQmYWVUmvJwBjuiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=oRThubEDr6GvQzd-TQgdPvCFwag3aB7bOwoHv39AXIKTftWVl7W5BXX523MOpU0r4KZWibNY5OVx3RCb8I986Q5yx53FdfiBP9u7StSuAxKElVZ-wVJlsRMuiM9_RhqLAELeR6frDqgst1vtkwCvJPEjc1X8HMtRrJNBVA9ORpUixwCjJNgPr7KzKV2WK8XVYvy6h9JVCbRjABTDsDnfMJwFRtznuiIQv_LysDCpDxczr_BVQ2jIR6UdbbA1N2jzkUaCIMs8sQ7Gi2Zxi6huG22md_LPVI_GrHgQIGMQGMJFWwKEDYDG7YIOG22p3AvI5iKdplsQSvPbWv4buEaGAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=oRThubEDr6GvQzd-TQgdPvCFwag3aB7bOwoHv39AXIKTftWVl7W5BXX523MOpU0r4KZWibNY5OVx3RCb8I986Q5yx53FdfiBP9u7StSuAxKElVZ-wVJlsRMuiM9_RhqLAELeR6frDqgst1vtkwCvJPEjc1X8HMtRrJNBVA9ORpUixwCjJNgPr7KzKV2WK8XVYvy6h9JVCbRjABTDsDnfMJwFRtznuiIQv_LysDCpDxczr_BVQ2jIR6UdbbA1N2jzkUaCIMs8sQ7Gi2Zxi6huG22md_LPVI_GrHgQIGMQGMJFWwKEDYDG7YIOG22p3AvI5iKdplsQSvPbWv4buEaGAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=h52Sl8voT9JHfmx5TxfzPkbqe_VsCed7PLQQ426J2R4ACDW4IDjoTpyqdkHrSRiClXPihlSvuEJQYyf9X64zuRoTYxXyQAeSJmoB7dPlKAzBiDYVJanLv7Qf_tVLIT3mhLNqyy1q_1W3GfEUvf5b4DbJG4s2GqDrqQ5r5TDUtTDM6J7WSdj6WLxT6Xx_IOmfyXLuwHW7OSqEexbzWrJsba1TzXWOdvIzBVrVNxfVsxAY84FqcgG_TjNm1MkvFLbAqL9lQ8q5M9lhmDZ2ddJp7LEJwyk8j743uJWGpUJL6GTzBg_jsZBCIUii12j8Dm8bpk3atu0AE-WaYhC-PYNxKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=h52Sl8voT9JHfmx5TxfzPkbqe_VsCed7PLQQ426J2R4ACDW4IDjoTpyqdkHrSRiClXPihlSvuEJQYyf9X64zuRoTYxXyQAeSJmoB7dPlKAzBiDYVJanLv7Qf_tVLIT3mhLNqyy1q_1W3GfEUvf5b4DbJG4s2GqDrqQ5r5TDUtTDM6J7WSdj6WLxT6Xx_IOmfyXLuwHW7OSqEexbzWrJsba1TzXWOdvIzBVrVNxfVsxAY84FqcgG_TjNm1MkvFLbAqL9lQ8q5M9lhmDZ2ddJp7LEJwyk8j743uJWGpUJL6GTzBg_jsZBCIUii12j8Dm8bpk3atu0AE-WaYhC-PYNxKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTHsXmR8rnMMx8oJZ2s-a6Ak27vojSccZC1E5kOOSVtPqI8taE1LVHR4cgSiKmdrXSd5QeTC9h0v9jyIRgJg3Cp78rxCpHB3wq-oOIFdo908cJsTx13-VkQQBruNqYU-FZmibN6M4iAQUdMF7sdK8r7rL3ev005gYNSexZVfXPTxlSwE_AiVXbhJMJZJJMkWxIaYXGnAWKu_8Ex9t9_j_PZcnIbYP83ZeF7kvyFdjCNgsy6G6EsrHoLppvjEB9B6F0D_KCM5JjHWezuQ4sDDcgMALTxxYb72_47x2XWtc-eguHdQaX6xxLPIZFzkZKx-3o0a_D6QMRJ329JkwFRCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=TQZEJxJlPs_qO1Vb024Bi9C-W5Tprgyjn6QCktSSiMqabbAzFvaq3Em1d430B-oKNHPZCK0udaZNO5ga4ees3dYM87KztvnicS3bsRiQY5NsbKkH3i1ZZ5cwPHrogGnuCS7Ed_nsUi3sWu_NoSRzhvkNw1fvHcLWjUEkLmDdpESwntCae_3jIQkpfTLqShGLZQsDhBE9-CH0E2Nd2o8sRd9Tmir3PJ5inyKCblqwr6jsq4wnGkalV81PHzpHO1bTkkpY_cxk0_T3yoAY80AD9jLtf-mI_gRSsT5fjRqKhl-dWyTJMEuSxQwSCiI7dh5Ft8Y3ojBx9yAUCLs9yClD2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=TQZEJxJlPs_qO1Vb024Bi9C-W5Tprgyjn6QCktSSiMqabbAzFvaq3Em1d430B-oKNHPZCK0udaZNO5ga4ees3dYM87KztvnicS3bsRiQY5NsbKkH3i1ZZ5cwPHrogGnuCS7Ed_nsUi3sWu_NoSRzhvkNw1fvHcLWjUEkLmDdpESwntCae_3jIQkpfTLqShGLZQsDhBE9-CH0E2Nd2o8sRd9Tmir3PJ5inyKCblqwr6jsq4wnGkalV81PHzpHO1bTkkpY_cxk0_T3yoAY80AD9jLtf-mI_gRSsT5fjRqKhl-dWyTJMEuSxQwSCiI7dh5Ft8Y3ojBx9yAUCLs9yClD2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eWMaVG5FXxx6Ub0A_Lq9932ZdrDJfnnEDh7cjB_f_wOWopX39ZLaGiVR5l1c9j6lmInIBpDGEcG8Vv-LL39CrliXtlClRREOFZaf1y52QwDme63l37ToBvI9I6zFmfQDexnr9VOpo61xg9l_GMTbtrtSmc7kUeM7FvSDR3R-2ARkHYUuXJjP2rpsf8q-MXUOkBNgxexk3kvTklphpRYlEDGwvhxQnOdyckM-ooMyQzf7JhzzgrynA3M6i7LXSmSEYU9a9-ODClX1qWEXMYWta2qPX-DWxcUJU8hZ_sTY-DCpyusVDycQH0J6Hc3qUWNGwu5njRm6AagtR442895Daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
