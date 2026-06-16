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
<img src="https://cdn4.telesco.pe/file/ZST8GQZAuGoKIuxjVOLrbtnEh3uQLdxfuR56-qfImCCcl5kP7H3GM75I_bUzFX45dIVegsX43X38u2d2JKVKRcg9PsMgrhDv62q_X_yrgZfseSj-sJErCUdot1hhgdl8OLl7uFplRqAIE-0JE1mZJRQd7ssKNpVyLNghJv-KloKyDsSEbyndRQLbdGKDR1tGK_XTSU-kPk0xX9Iu-aoVtgWcWIfcvOVuFOBST6-7FWt9lQh2nepth3nZEFLIrZ6Y09LT-V6l82zQk5Y9GTMKO240WoMOxIi9OJYHeUQcFqc_-Lz74Denl17TwXLJiAexc2zS2a6paYGZOC24RAAerg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 296K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA5jrK_6lM0Ead20Byw646i3z4uf-cwDVjDRyDVsLJtB5OuK48HvFK5sdv6ayJ852SuNcAuI8sz0kqimVEK-I7LqPPJpJnJVIQeUqwHMBmFmTO0rt6Vn7dc56XESXpc7wf6fgOogmVJu4rwF1Yvtz26JID_ka7ITQLhc6lQ5_eOvquOnRx3FrkmMdw72CLkGv3cXtDziypjrwbCnbYWQcoFzxxuI5zui4kumTWKdjbjXOxUmTV5PloS62ptUPXnhW2lcMX3l75v4NZwz-TgaAxZTmeVBq8NlRtA787r4q0VXnvOI_RwP2hRTHLAqiunhBwT9WNrKqyqwUGz1sSXRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/persiana_Soccer/23585" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRdDC2AR5AwRUt6GPIs88PmgIs2AUFS73N90Wd1MIkx_TI3KF1DLY3pH4mtL4H20EGi6_PtLTPD7ySjXSefSs5LaguFG5Nb34Yds-uCVwIWz7KGnIq3rcdy24WAQ5zlym1NvrxBc5wlYGxuCRn4BXFf8wrI4az6UmRwD37fdO9zMev05i5pT0vl2h0SheRMI0GxxNQm-rY2yp0HMADIn88acUBpZPbQnXiYBldNzZ0T2_LuJgoY_VZx0xr_N6ZQ_EftQZvngIpQuutdqnbEu1Gx6sl8NEZKj3H2OtOxgFbd1uJJHzlxaSz0lwmYLznawp-AXw2ArAzy8L65UEfHAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#نقل‌وانتقالات|رومانو: ژوزه موریینو شب گذشته درجلسه‌بامدیران رئال‌مادرید از علاقه خود به سبک‌بازی ماتئوس فرناندز ستاره پرتغالی وستهم خبر داد و درخواست جذب این بازیکن جوان رو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/23584" target="_blank">📅 11:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚽️
خلاصه‌دیدار امروزصبح دو تیم ایران
🆚
نیوزیلند در هفته نخست رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/23583" target="_blank">📅 11:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7leCbhBCTMYVpioIJPwY4oJuhK9iPbnfJsGSwm1XyxTQBKSK-aXLwU3NOS419Oe7lLuqKyZz_6L3dg_0dvgz7Fb3CpnKoEUvEfoL0BEOG_t5NCOw8RWWi6hrew31r3C8wev2hlymwdd8iT1IxYoAMLsEJXJU06C2ZkvlChO8ahgyQ9Rr-edbuLnw1R7ktSiqIVVzC9lqhO2EwniJWVoEFYIQDuG6i9NmD5tr3h3IIpSGhqoixsTqwDGljtcEU_EFoLqmlRnF1YqJVZOJbHSVuny2eDqY3ClQiRpvy_SUjkdV_Ievqnh3v7nhe491XPNiY_TDR27AwrjMqAk1cEmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/23582" target="_blank">📅 11:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmt5iyUvFcTBB4jRiNm5JBy8kFS8ht9w8P6G4HFAZCan4OB5-N9aQnSkkPt6wcvw6gDZTNXKgFjUHBPAoN33cSt_fpyNoRcn6a8qFoW3Y_X5agqp59wMdnpbCZ8pzQ4IP-NQXhApQoj7p5AyEdMaVn-UnRowZO5LPu_rYPnmS_4VvgAbXmy4GFVPiouJfRbHdih21VBQkyu7M7YB8wEijUoycHNF0baQjE7RrylBUk6v0BEvrJOEENsCn_TjlALgH7apAruy3kqPOCWSe7P8ExeyPUpkzeI81lgi_qqA3ripJNvFMlZ23INhW0HvdPV4SVy_-7wcoVoZha9FyeLbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امیرقلعه‌نویی‌سرمربی‌تیم‌ایران: میخواستیم دو شب قبل بازی بیایم آمریکا، گفتن نمی‌شه و فقط باید شب قبل‌بیاید. الان هم میخوایم برای ریکاوری بیشتر بمونیم لس‌ آنجلس ولی بازم گفتن باید همین امشب از آمریکا برید. ما مظلوم‌ترین تیم تاریخ جام جهانی هستیم. ساعتم هم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/23581" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=VYN8ywNFpQi4h5m270PFzhHFxlgwKJI8htaF6Gk0t8pRJkO9y9Tx_KfTLoT4C3ATfUt5LFHG9CxVDDFrN5WHJS6NVBiv1DEVKDxGaIa40kCeJL_5L7mEb7iswjPtelju-ksjjJzpI5H7gpRoSg6LxziJoxE2KGVRTAti5XPOjxoTKsmKA8lT44lJ9SsjhobD-PSLf56QKR3GDohh6F3OQc73s6HF3JtXfu_ydU_Ml5rti2ORUJ2t4HB2LdVe15XLw8pedJYxgb490mWKnexqfEmLaA8Fuc0zwKlJofSrYd7h1tU1KH--tCmqfqYhLABPSZYfq5lNoxTqXYRFqdmDYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=VYN8ywNFpQi4h5m270PFzhHFxlgwKJI8htaF6Gk0t8pRJkO9y9Tx_KfTLoT4C3ATfUt5LFHG9CxVDDFrN5WHJS6NVBiv1DEVKDxGaIa40kCeJL_5L7mEb7iswjPtelju-ksjjJzpI5H7gpRoSg6LxziJoxE2KGVRTAti5XPOjxoTKsmKA8lT44lJ9SsjhobD-PSLf56QKR3GDohh6F3OQc73s6HF3JtXfu_ydU_Ml5rti2ORUJ2t4HB2LdVe15XLw8pedJYxgb490mWKnexqfEmLaA8Fuc0zwKlJofSrYd7h1tU1KH--tCmqfqYhLABPSZYfq5lNoxTqXYRFqdmDYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
امیر علی اکبری در ویژه برنامه شب گذشته جام جهانی به این شکل انتقام همه رو از ابوطالب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/23580" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwNOfMYac1iJrAsA_vjt45mxnbQojYkRx2uMxq1AkpKZ1wlU9LolqVbuKnNAFsnkAVQIVmyPXzuXLMPuo6UrANesa61a2yDMZqr4RnJxQMr0LLhHe1Kkw5FixMSgZP5xsSnuyQmyl0T2PzKxuNkAZeUCemTNfvjILZHEWRrrBMtNlTUweYYdFj_VWrKoCWYLyXiKIRJnqeu_5p-g0D-PYBaDTcWV8gnpCuhksE-8Qd3_iMdNnJZ2lqAmSi_0VTAvylGIwJu4_yas9FIsAOo3Ai3cK8ABxFaEPYLjbQ5TZ6YhLomlK6z6k2uex6B-9hTGtFmqPGMOTyxRIThrG_l-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/23579" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=FiE1uNYmSgCkTnZXwiKtp9TQ216eQ6GhFownwdUYoHSEO2Sr1_ZFsg-0xV7piur7wZzosBLS7scyizAJ_vcBlR4c44Zu7RGbnbIebO3HkjEg_BIezeQH1rNjb2qI2q3cUikGLHBbiDwGAfReDnkLXqKlo16Fx_P1SS9OZ7UX7SwFXfcDCsD8UzKRaUrBtDCZuuAWTzPZzUyy_wfSGoQ6yga1oRrrceiXjahSoSMPOJOXZ5Tneg7OW3HhqiEFUYF7UollRT6MEH7sfohfAioTC9qCmcPnTqEAwELbMyx1ZwVveQ6ltbD5GqNdMh0vZow_jKwcbEHTuomHNtoxf6kA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=FiE1uNYmSgCkTnZXwiKtp9TQ216eQ6GhFownwdUYoHSEO2Sr1_ZFsg-0xV7piur7wZzosBLS7scyizAJ_vcBlR4c44Zu7RGbnbIebO3HkjEg_BIezeQH1rNjb2qI2q3cUikGLHBbiDwGAfReDnkLXqKlo16Fx_P1SS9OZ7UX7SwFXfcDCsD8UzKRaUrBtDCZuuAWTzPZzUyy_wfSGoQ6yga1oRrrceiXjahSoSMPOJOXZ5Tneg7OW3HhqiEFUYF7UollRT6MEH7sfohfAioTC9qCmcPnTqEAwELbMyx1ZwVveQ6ltbD5GqNdMh0vZow_jKwcbEHTuomHNtoxf6kA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/23578" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3u0Xr3x6M1SGAj8sfTTR4ZGNX4ZVMDFQkjYKfyIi4fIUCH4zd1I8fLuSmGY7Zu_F8G6RCaYOjR5FOJDTe7jJmC_9GU4FpA56mWNGj33FSxXoi7bgqB0R4xSNXwJG5RHEwLZpBxGZKEMC96C48VKh2qpvjOcNdh49IH-bh92TgpQXz4K8vug9svX2IFHWzOd0oAar3a6jkHSyO8o3k5wKKYukaGDv34GoKaVae62cz0pBOwuA89fmW4l0ChjZNMYDjVQGlX3SEKQiusqBWOLTIgMsPoZa36iwYwrOxMTUvHqdK3FrcT8VLJDRy0LA1AwjlJkUPsWaAeJsPWh59paZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/23577" target="_blank">📅 10:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzj7QE4Yxe_P0fWw748A0ccjYLny7TPDA_QN5PeTIs-VwRog0Zsr1ragsHdyxCdfxlbZPABwqlrrZGQGO7kIJEs0UgI0Z4VixouhT_4qH7EtooY6N0MjV5iZCWVU9iGKSFljV38zrEepwhSey2AI91_NQU0XaxTZXAFJsxZPCcHu8DDEHnU9VKN9nbkiMFSA-qeRkdOhSKXEKH5CMMgiUR1lWqx-kk-qa0soDCSs4aUehiyswwyslzcMHhl81A-b9iYts-F26CHWolZuZoO91M-sGtSriwV2K5EMqapRgnntARpk_H9g6vEib1xpJQ-mQCjik4upPJQkf0HGJRUBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23576" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a244147c.mp4?token=sLnQKVXT0J0qKCTVi2I2enviAJFgYQM6_XJQppreonnJAiL2WcrztHn7OXojow2XaWD-YTBG_hiYMuhU48Pp6iNDrCin9B2BUtniTB_UhaFW3xRM_Q-1FHCnUulFGp9zSA1e37Q9XNZprV-0UJc5aWAbZ-3UEI3xSOcMKjoEXINFmBEK3ioo11f4wwzLmBm3juMn15oMWvrYWM4TY-H1lsb1iEJcoXIk1svJ4f8xr7yP_S-U9y6YnLIw4Hp1iVApgSpe6A0S-6KHhl9wKb7PQPkd2EN7rWPRczwpjbUmPitW0UP_YCRxyTKWaHi-YFxyLnj5KOlcA2fNW7I3MZQufw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a244147c.mp4?token=sLnQKVXT0J0qKCTVi2I2enviAJFgYQM6_XJQppreonnJAiL2WcrztHn7OXojow2XaWD-YTBG_hiYMuhU48Pp6iNDrCin9B2BUtniTB_UhaFW3xRM_Q-1FHCnUulFGp9zSA1e37Q9XNZprV-0UJc5aWAbZ-3UEI3xSOcMKjoEXINFmBEK3ioo11f4wwzLmBm3juMn15oMWvrYWM4TY-H1lsb1iEJcoXIk1svJ4f8xr7yP_S-U9y6YnLIw4Hp1iVApgSpe6A0S-6KHhl9wKb7PQPkd2EN7rWPRczwpjbUmPitW0UP_YCRxyTKWaHi-YFxyLnj5KOlcA2fNW7I3MZQufw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سوپرگل‌دیدنی‌امام عاشور ستاره‌تیم‌ملی مصر در بازی روزگذشته مقابل بلژیک درهفته اول جام‌جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23575" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23574">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✈️
معرفی سایت و اپلیکیشن مل‌بت
🔄
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/23574" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe0bZXiij2GDDh2WmewEIqNWFooJsERKcMTulK3PlRq4b_t9IvoXPi_SsKLQcbHX5p1RiE9A6OOLySsNAZ7eir9e7QCiQkvGksFJJubI3NEUaBOqIFwG3HLhVmYj29WJnxc8gl4c_GzQLTG8qvGs_65aHBOVI1iCE5vQAoCcEEKqnKSoMa6Y8G-O8NVnDTSnO8Ui1F6sLhuigETbs9MbO7m8WDcGvoQl-Qt7x6btIFEp6e5wDwwJujuw7KayAAMMcuxcNUN8jmGhXmjZUZ_SAY5fkK7SqHRs0SznORa7GIsdwcgfCUVk9EDX9dWJ0traZqtIiZTaT5tzp1tBzwP5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23573" target="_blank">📅 09:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwwtsAM8cYKancuYrH_5bjmCM9_l0x7Oe7VqcaZQJVlN5QJY3BKtpYKGuzuCrAUljpTuux27iNfFX4yIcHwcVpdV2jdFDbRNf6IEJ9jXMxibd029S98-JEQrBXqOPxxCA8LvSPuU6UKy9h78rw2a0Smrez6-i47ueSt_Q04iZnWFxVAcmxXQ9PeJMrRtCK-gsBNLc2m48FaGPve3gxMtyrCSFtMSUT0Y0Hmsu6HUd9y7s4PMpkfMnaH3U83i4GCjYWQqvLSWSGbkixZmNK2y-q1XzvGYCr5T06j3haVDzdZQI_0NJMb_vsEHXZhQUMUqnguBbTSBBLwwX5kBRAB7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/23572" target="_blank">📅 09:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=PCJIFYC8UE-7dILZYoG9kJvecDrK4u2FsHwWR5H7a0QQwsd-5TArJw9whNE8oIdG7FMC9jQ59bCclw6yT9xn-L7ZoYclqLLM3fCVZNkQCVLe5nE7oWk3ibPJqGVFmx-Shhi1xjKvH9OQ0Q2g6SlV7ESgty46A-9EeFfIFVceIMxbj9_qYTyRXuAon-AJetzPcJWpICFtrwXalNrCWg2SfeR2MEb-aLp-so6YB1VTtJT0V9-w11sWME1lc2kXiJlnyN8eGl8jqSZX7kSeH5CNpi4d0Ll4g_CidqwTrBhtB4h7LM8QC1FPuBS7PNafdVxXzoC-H62z6F142bJDSqgHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=PCJIFYC8UE-7dILZYoG9kJvecDrK4u2FsHwWR5H7a0QQwsd-5TArJw9whNE8oIdG7FMC9jQ59bCclw6yT9xn-L7ZoYclqLLM3fCVZNkQCVLe5nE7oWk3ibPJqGVFmx-Shhi1xjKvH9OQ0Q2g6SlV7ESgty46A-9EeFfIFVceIMxbj9_qYTyRXuAon-AJetzPcJWpICFtrwXalNrCWg2SfeR2MEb-aLp-so6YB1VTtJT0V9-w11sWME1lc2kXiJlnyN8eGl8jqSZX7kSeH5CNpi4d0Ll4g_CidqwTrBhtB4h7LM8QC1FPuBS7PNafdVxXzoC-H62z6F142bJDSqgHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ولاتی امیر حسین قیاسی خطاب به محمدحسین میثاقی مجری سازمان صداوسیما
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23571" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n725rFM23X5J_lPgxr_bY_m2ONoE8g43zbGcSYOdPVCzHe-IOF-FHsU4BCt2Ls_QNfg2W5sGEWqHWCJ_XQJtNA2HAzDquMZcEDWafoSnygPNhKY2eOo1A7QzBImSL4CdXMzuOq7Hh67lOpTHYRisQnqnaKA_uIgtAq8A5QeYbXAoQ-V82iBYZ0973qE5HYlvuKkvOoL7GRRH74eW-nw-ByornBqaD3802FmEoHRFjTHeHNXp_uoIzc6ROF9uuJKSaf6dSSL6e4CRyvOlTPs21488_FdlHcfygnP_bS9tgbv3XXiJAkwH1Xrl1qKaKtGTOWTRhjJ5kkNmGVTDQkXYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇯🇵
موریاسو سرمربی با تجربه تیم ملی ژاپن با شنیدن سرودملی‌کشورش‌اشک ریخت. یکی از تاثیر گذارترین عکس های جام جهانی تا اینجای کار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23570" target="_blank">📅 09:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=MKSCIwO-bDAKvuZ9t5vAIOW9nnXwE2XpPyEU6B5OBIXiu56KZe9mMAIg33tRfT_SSiU3YvY0kn-I6eAA1s1j7H_6h7FyTIyKe3_7ceNeYLLV63u8UNAYV13KyL0hujyEU7cmf-BVG3nuKY1-tmMC1-8_6c-uIblz6EwMobt_yvv-7o2Bf8CsGfuIGM_44JmFhxQjs4j4HmffS7Bjuo610FyHe3_z1tN4iIdM9PlT3XsDViaxcC3pc0hCueKcTPcYrpoyfH3FXT7Fl78Z0xhqjeQl2BnTi_6vOsHj6iRIwObU-ByS8DPjkUQ9aL2Y2iAtQ5ISD5zoreXjFMnMxO19qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=MKSCIwO-bDAKvuZ9t5vAIOW9nnXwE2XpPyEU6B5OBIXiu56KZe9mMAIg33tRfT_SSiU3YvY0kn-I6eAA1s1j7H_6h7FyTIyKe3_7ceNeYLLV63u8UNAYV13KyL0hujyEU7cmf-BVG3nuKY1-tmMC1-8_6c-uIblz6EwMobt_yvv-7o2Bf8CsGfuIGM_44JmFhxQjs4j4HmffS7Bjuo610FyHe3_z1tN4iIdM9PlT3XsDViaxcC3pc0hCueKcTPcYrpoyfH3FXT7Fl78Z0xhqjeQl2BnTi_6vOsHj6iRIwObU-ByS8DPjkUQ9aL2Y2iAtQ5ISD5zoreXjFMnMxO19qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی در نشست خبری هم ولکن ساعت رولکسش نشد و به‌این‌شکل‌اون‌رو به نمایش گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23569" target="_blank">📅 08:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5ObNrvHLtHH-k9KnNMy-18QLz5gmKZoXPFMibBbId4p0mpC_JPMSbFwJxUqnbMi8DGhxuCeGgxiO8xcUH5HbNk_PrUSYF7jMRRrjot3wOWwgLzKxSVWtIZ0buM1zpREm_Um1QXYpxO4f5_Xa6XnirsS_elcKnUXk-oSx65yUzKunHjAYz4SgLn9RSwhW0yVJatLAETVUWVN4lct0M9Nyz82OTz8354FGKKsrUB9O-UZsX1Mcbqkg5UxVkfbc2QYFRdC4YC8M4e-UcZJHnEIDM9wnSsGvVUF_ngiQ9J6cNKKfIoJV2E72nglAyZPfyAk6EcIGvtTdUQykNuP14JnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌ بنده‌خدا دیگه رو برد امشب بلژیک مقابل مصر 8.5 میلیون دلار شرط‌بسته‌بود که خیلی شیک باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23568" target="_blank">📅 08:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNVRWHgZ-lZ1LMChjO3_3gLH8HoooFIZUNmS_gBsmU8JbPjQ9V5QcDslIjZ7Bw8OqH9P12KxNWbxbSHnixQumFljtXfNzSPq76F2xIHu1zXjuTKYUeMASm7wU_PrV0KQdjfZa-HsN08FacBm9ykHhULfpJTHdTt0NvpFJjDgs4n87OO6682Yx6UeQ1-xkySVrJRuOMGZjYNgz2R4CBXQIQcXQaS2B6tXipfOIYxBkU0HcQL_mfWgUx5V9kt2zXSJKnC0EBA52bHVTMaaTsL6IrIuGlJV-cChoIgV9KfaUzdDjEO31R0P3S5FWhbiCbdmVek9TaXHSBBtWRij5cTY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxfCBNNDweMyHqkf6Wtn8TiPld5EIGV2-0BKw6t6nQNzO3-WJlcrdM3qYgbRfqFNhPcUiEgdW8JHUBJisXBzjU5J-iW9Iit6ldRzTiNMeipZi0Yy8RCESEb7WysoITYG8Cwg_h3xYXldSJ2MrSBcKNPXd0SZGK9csTfvqZ1UBtT87ojim3bWQkhA8TfzLUY6LtFoPh8tdPYXPeSiNn8wSgm6kZHncwCq7hDZ-wnvcEymKc4QothTHZCyYySRF9Pv5V49R91iL-I0Of_B6RFnZOdYgtmuW1KJvSDheoQdEOadYgltcm0HFKoDT0mo74X3eWqLFAU7K4KvxnzlWrKUfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
نیمار جونیور اعلام کرد که پارتنرش بارداره و قراره یه دختر خوشکل دیگه براش بیاره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23566" target="_blank">📅 08:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRGrfXkZMJhhFFxutQzF0K0J7wKRn1Khk9fkrE2GtPgD0Jey4gkoCLI3ux1GlGILOum9DtAH9Qu2ERasPr3-YqrIUBp9xJmpHIF2gpPuAPq9ydKqaHl9qCXnt2ewgMqY-UR2fKa-z-tSRZ4k2KDAyGloievB7TBIBXOUIrZ3gSCoyjOhbEgZA59oRrkIOz1u-Za2wZOM71HwbDZ9TQZ3cCIlT63ojiiW7WAUTZwpdTOGZ9HbpcJ-gK5rrl19ZUIrijNkqyU85H65Et4_PuRZceBF9KGz5CKtPjJaVxRBjC3AZ5GUr6Dplkb0ZDCI7c8Ykb1maTXIwu6_RkKsInB6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23565" target="_blank">📅 07:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=V7rhrNEVXtmf9LS8_DxdT3ixlsKUOzd0f1Io56bNLYDv5vJdrxqd7awcCGnlbocNjUyj73OXKzGVLxEMmZaG7-LXbziI2DQ0hpRkCi-KP2cCg8fXwvKAjUBXf5XxeN0WQXp3e6k-X57Gmw0NWCVnvWES9a-l2Ovm3T5KEfmdKsY3ugywyBqTRsmN3q9wia8jU5qYaB9J_1_g2jnCqRCRo5GUsBL18fSmjBAAjnK9s5d7WuvAiCMRI8Ysy-V8kRzNpjy0TjyjUm8Umg-_CtUIrb5L-gzVE3pCBPmTiiIU9hxk77OLgFi-tTAbwGNX13nUXDVo2J5mchqOQPQ41tiiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=V7rhrNEVXtmf9LS8_DxdT3ixlsKUOzd0f1Io56bNLYDv5vJdrxqd7awcCGnlbocNjUyj73OXKzGVLxEMmZaG7-LXbziI2DQ0hpRkCi-KP2cCg8fXwvKAjUBXf5XxeN0WQXp3e6k-X57Gmw0NWCVnvWES9a-l2Ovm3T5KEfmdKsY3ugywyBqTRsmN3q9wia8jU5qYaB9J_1_g2jnCqRCRo5GUsBL18fSmjBAAjnK9s5d7WuvAiCMRI8Ysy-V8kRzNpjy0TjyjUm8Umg-_CtUIrb5L-gzVE3pCBPmTiiIU9hxk77OLgFi-tTAbwGNX13nUXDVo2J5mchqOQPQ41tiiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌های دیدار امروز صبح دو تیم ایران - نیوزیلند در گام نخست رقابت‌های جام جهانی؛ رامین رضاییان بعنوان بهترین بازیکن زمین مسابقه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23564" target="_blank">📅 07:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=gIyS3-FMw__0dgqZ7FOSFzewd0vezZIx50yVloz2UAMlFIyDulJFonzCpGO9lnFdNErgUBr-IKCcLUfpPg6nECuvoqS7FSdEy-ELsXDgHbzX5mhyCbfL_Rsf3nvfKB1kKwYlpiOgYOi6uwq4BJOzT3g5GKBWlMSwo4D9ZTcZy6rnA9Ifwus_ARIv7fmlTc_3I7bydNoX4R1Gioov1cOx8VcgGFLjNqYl5d0NfIOmRAwD8oCXuWcbe989pZZI5LQvgej3uh_OMnCDOhqpgN3mYo-S9D_1SL33BaiJfBmj_zKx19XPYswxm2LaOzm2myYmQ9Iizu3gf5ZLYpXBAxYHrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=gIyS3-FMw__0dgqZ7FOSFzewd0vezZIx50yVloz2UAMlFIyDulJFonzCpGO9lnFdNErgUBr-IKCcLUfpPg6nECuvoqS7FSdEy-ELsXDgHbzX5mhyCbfL_Rsf3nvfKB1kKwYlpiOgYOi6uwq4BJOzT3g5GKBWlMSwo4D9ZTcZy6rnA9Ifwus_ARIv7fmlTc_3I7bydNoX4R1Gioov1cOx8VcgGFLjNqYl5d0NfIOmRAwD8oCXuWcbe989pZZI5LQvgej3uh_OMnCDOhqpgN3mYo-S9D_1SL33BaiJfBmj_zKx19XPYswxm2LaOzm2myYmQ9Iizu3gf5ZLYpXBAxYHrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23563" target="_blank">📅 07:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23562">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/23562" target="_blank">📅 07:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23561">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIJaepZa9bChdfbkGJaUaoiHTWwyCT39_QNonoh6pLDzF6RY9LuX81F4TcsY8FHFFDBaETI7GmJncOwxe03JVu_twUM0DlBQJyZrY6zRp4Ld3tm3ZMnTentsUeocRW2fAZ_2S2_YH4No5l_2XnXlw49X1a7oG2IFblOlDoJ7zdA0ayCkMhYdTOgAutW579vhPj_dwoSDh9YrI69eLFa_HFqTaGSLMuxzrpZcgiI4cTquK9Xfo3EHC4m2h9b4RMzUwSBiMtOoF76h_k6vt8lrXHp8SAukGtS4YnNQ3RtaSXkbLI2SfEMa1yj1HaYo5ytUQbRNiC2Mlu93eV8A4oitpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/23561" target="_blank">📅 07:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23560">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPhNNg_6zYi9DlWkfQu11uhuUuGUFe1bfjaKNB2q9CppgaVncrCXOjCvvYeYzlVwJ3wtIcclgRmvFdkR-iNhpfZttQO4um8U2ZHQif1MzyLQMIz_xv9-EhZcZlkGXwPfSRV6UnWU60dbZVad5rq3vW8CxDK2l2BjoTlQ5c6qmrC3syeUfFhU79TivDUtMt8ZMuoiU1cuA02Oi3DLteC2GEw0SamXORstNpyuGgNMRy08GN4-OTlQkvTn9GuJKlqdh62VDG8lx2kdwAfiUoOGtDMtx-jmPNX3MQ8ppqn1lGNvC5WFFZDHaUklUzUhX9cnN5KiWBhFF-Mnni9x7Me4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احتمالا فرداعصر ازتیم‌جدیدکسری‌طاهری ستاره 19 ساله فصل گذشته پیکان رونمایی خواهیم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23560" target="_blank">📅 01:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23559">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY-YiFV5uv8VHNp24N_yDoZ8YDCdt6lmE1pHW_MxwGXeoLComDtbbuAdhc5hN0xQZof5zZApdeVLK7n6eF1ZYVHWbM9b5lJ45Slw_bX0Bs947hrzyiZ2EGMfEME_QC1qdeVFg0_r4Nf4ekm7fJaCNYtkBzB3FlQbrMyvwi6lGTwGZPqIVigldVyL7w4c88gMF9P_4hxYS6Rw3P3UT994aiItRGRuXmjEgJYCzU0XIjfUOjbvOtmmsRGo2j9NYrsbu-OyPHe8iB3CcPcTzwbFxlJXEIDnLBS6ACA0dMSAiD4-PLHML6f6dEZpgmaApKoaEn_SujnizD1Ou6A6mUpB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23559" target="_blank">📅 01:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23557">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTZQLiKvLvE1o_h2TTt5NIyjVrUiYoLoR1P7y40DcovcqM94-JkXfIc6ONw5zp53b9pXQBZOigskxiO331uNf41nzaG_RwmT44uZqJLFRvoDiQ_DXK4uwXFd8HoV4Z021NOweC3BBZQx6T-l45ZIUoHBt3WXO46my1OLqFoHt88jyJeGx3RAI853tO8vulb3_PlCZc10Lc9KMnhTDh4rU-DstebM_-iwa6NmBfeEP2WN2j3JjBKj8adSH9ALg3fPiRwb3PTDWzZfSFRGcRoARSqLl1VuEDwFzElFkyWSoWPct5elfbPIyNc7rG4n7Ec0p5h-1kK1e-Gg_AFrm3Dqqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف شاگردان قلعه‌ نویی با نیوزیلند تا اولین قضاوت علیرضا فغانی در تورنمنت در جدال حساس فرانسه و سنگال
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23557" target="_blank">📅 01:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23556">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmXMmC34yHRsObCFUP84faIh1ziuThjAzwmv51IvL0fKWZqU-T0qZJYIMwrvfPpphFoOlp2GXmiP96M4GLEdSbROlKVfSqP5d4uftHbCTNZk9PlqhkSQHq6qXau4-QXqxEjlP6zgoplbTCVy7XH6sf-fLmtvdu56yzmz7Hy_MGGwnhTtFtUpnbk1WsLsujlMB-TE3N2lu4fBd5Wl9QleqynfHGqfifb33Jo9RMqDiPzZbF7kRadslvQwstvSR8u7Aqh4tFlHz6eB1IHkFXHxqtoECIcj1KEFJoHNVahCntvrC4zX6XeO4Q0ai25xmFL2cESgKITXgbGd9GLdJAsZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌‌ دیروز؛
از آتش‌ بازی سوئدی‌ ها بادرخشش ایساک و گیوکرش زوج خط حمله خود تا توقف‌غیرمنتظره‌اسپانیا و بلژیک مقابل حریفان خود
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23556" target="_blank">📅 01:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=tDfUmgXdC0t_dHyCFt04vYAv6ptyWUC-BLWrK-o2afu4bAf7YNXAGJMOB8_DdsovuuDvfxj5FACk650yfAd4FdXHCsciVsPoEtuv_npuw6KKQv2b-kOhgiBHV2SsO6Tjjel_xfcmpAMs653olCeDcTbhpEqEtR6rbpW4Pby7hKhYH57zvxANDdxvsgdA2EQtqgvIYukAzHGfRfB6ag3KfTx3pNkzBn2bhGKh8gfes8ZtdDw4tyvusmIJxAaQPR7wT2JK388SlTsrsg_6-gzjWRYX2KaneuGwRkUL87AAeuNxNT-yosk1V4hxpCpTSySIlb688QqZ_6-b5ZttAqn9Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11adede3d.mp4?token=tDfUmgXdC0t_dHyCFt04vYAv6ptyWUC-BLWrK-o2afu4bAf7YNXAGJMOB8_DdsovuuDvfxj5FACk650yfAd4FdXHCsciVsPoEtuv_npuw6KKQv2b-kOhgiBHV2SsO6Tjjel_xfcmpAMs653olCeDcTbhpEqEtR6rbpW4Pby7hKhYH57zvxANDdxvsgdA2EQtqgvIYukAzHGfRfB6ag3KfTx3pNkzBn2bhGKh8gfes8ZtdDw4tyvusmIJxAaQPR7wT2JK388SlTsrsg_6-gzjWRYX2KaneuGwRkUL87AAeuNxNT-yosk1V4hxpCpTSySIlb688QqZ_6-b5ZttAqn9Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
نمایی‌ازاستادیوم‌سوفای‌درفاصله‌کمتر از ۴ ساعت تاشروع بازی دوتیم ایران
🆚
نیوزیلند در جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23555" target="_blank">📅 01:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23554">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=AbqrgvQwYjzSkuX9lgeGGZ_30SVVAZwk0XhkgbrgdhS7u89OyxPgleHwnvyt4Z0qEnd3alwefAp_EbAfG-meyi0cgA20cICgFaaQh4MD2xGKlF6j8Qxf8et2V6UA7UZJEsnP3fkmPntFEiB0YY63LoeyECfT2gUrs9VDP6zGwelywh8Wq7_1-rWit1Rogx9kZi7bZQRShMoMhIUwBpX0hCXd8B6zcP9tsgm93q-m4fdfeCn8tThJ3oZ60DxRAzWnMt2VNi6xAnHofHEX7oxVMhC0utcP1fxS2V0MaMNSHLQ4zJfeL-vIPFLAlAiDUgB9hbtxPdyTHKoSvBDiQFZV9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a904e7169f.mp4?token=AbqrgvQwYjzSkuX9lgeGGZ_30SVVAZwk0XhkgbrgdhS7u89OyxPgleHwnvyt4Z0qEnd3alwefAp_EbAfG-meyi0cgA20cICgFaaQh4MD2xGKlF6j8Qxf8et2V6UA7UZJEsnP3fkmPntFEiB0YY63LoeyECfT2gUrs9VDP6zGwelywh8Wq7_1-rWit1Rogx9kZi7bZQRShMoMhIUwBpX0hCXd8B6zcP9tsgm93q-m4fdfeCn8tThJ3oZ60DxRAzWnMt2VNi6xAnHofHEX7oxVMhC0utcP1fxS2V0MaMNSHLQ4zJfeL-vIPFLAlAiDUgB9hbtxPdyTHKoSvBDiQFZV9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
🇪🇸
دین هویسن دفاع اسپانیایی باشگاه رئال مادرید و همبازی‌سابق‌سردار آزمون درتیم رم: سردار همیشه به من می‌گفت باید بیام ایران و ایران کشور قشنگیه. مطمئنم ناراحته که در جام جهانی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23554" target="_blank">📅 00:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23553">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM6z9-bFspDEED6Da6rgs6ntUrSt07JN_rsOufhZ14pBGzdyolnRJ2etg6JhAw0TssePNN3EWf3ZPKScYyVLugp9YiZrAOxOu1iCV_ANJrDIPfu26Vkm4PlsJq6Z92f4_vAEUUlhHr3MH9lYutWULSzQb_UX8zhPvKBmCrU1j1fxb5w_AMFgkNL_rck-J3WIPkBASWkqh34KND5yXoQtjgfiHidjJR-_SuowjF9IZH1xG8LXb78QJ_Y4Bewx5GFxBYNBmXL-LmjBwxgXeTB1l-fWiNhPDEM8TFo1I8pdABvjzAPe6zH38y9w1EoMvHyMbpstH-ZxcTsYtOAfi21G2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده‌خدایی امروز برای اینکه 85 هزار دلار ببره 1 میلیون دلار روی‌پیروزی‌اسپانیا مقابل کیپ‌ورد توی Polymarket شرط بست و الان همه‌ی پولشو باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23553" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23552">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyZZDtZN3hMP_gYFHz9ResSkHypA7IBixv06PgvZ3CYG09nTvNhlXDJja1DrGgEKQ0VpeuV9yjF4hFOg5S7bivfIFgFPTQMvCjI5M37gVRoMSjt7hGuykBq1H0ik-DfWdwDQzOWepckltEy-BuzdoL2JCTFs4W9VF3ogSGr-wGB7bd4oVtkSrYXYdIPw-rMTagNBtck1qAr4kLnUA4YaNl12VWba--CYMJ2uxEKdRB4l0yToEachCbE4ndloe8lzb8zZWyh1sW91MkQdUHKbp0cTj1hgXxk5urEVaSYw2cqg9mL1griZdGxGLSu7iEQScxJkU4e9Mtw1apwe5yaFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
🇧🇪
این‌هوادار تیم مصر پیش‌بینی کرده امشب مصر بانتیجه سه بر یک بلژیک رو میبره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23552" target="_blank">📅 00:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23551">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DACk_ws_y-WAe5in1Q7LfI7o0SoOLYJ94m3nB4pak5RRvtk6xCNl9UUlPF4gS5-p7yT-12EvYL95bUu-8YYU-4tYWA0q1xkZ7X6yIusStC-wB7P6qhrk5yWFW3-iiXB4gcKnj1Udc8plJ5Z-Oo89tjOazrvO-tfVwYzB4DO7dbJY7g-h3H8cIaHRz_If7DYg3zS5EXgchFWGAuEjX72ngh0RZeklRf78HGX45691hr37pPzycVMq7Fv5PwWgSn_GrLOB4Nwaix-3W9CxHf9JJYyrwVZIzX4xPb41QIwG7iU90nGgnFrFko40qiMrrNjF7xZ_DOSx-8uG94F1P2XKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که دیشب هم گفتیم؛ نماینده کسری طاهری مهاجم 19 ساله روبین کازان امروز صبح با باشگاه پرسپولیس جلسه داشت...اما طبق‌‌ استعلامی که از مدیر برنامه این بازیکن جوان گرفتیم هیچ قراردادی بین‌طرفین امضا نشده است.
🔵
جلسه‌نماینده طاهری بامدیریت استقلال…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23551" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23550">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHy04deACUryHrYRfQ7ejcxIsUYx0vgfZzq_34vFllZVvFCaPo-bTrrBBb-DkwVrMEELj-KzVYmbNRzlM_FiM_7zUij3m3zbJfKRgCJly55Q0Alrym3ynRTvwnGrRGJp54utDbr2Cs1VasjGXRQJO7L8sbWqKzgv0oxqlXR-FkqpvN2jZN_h3dEPEpFQYqjBBn7xJvuOBp4iUu2tCDs0e4GOkRYBGCpNaN9Fpqcs3-DrKSZIbkHhib6fG2wmH8yUitFY8EwBsfJV-R1A7PJOhiAtr_HW1BE5X_APdj4FWnTU-mdzflc5N8OzzKKSnQ4Cf0Fmt2WZ6Ie7xYsb98WaPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:
2014
: تنها یک بردمقابل استرالیا و حذف در گروهی.
2018
: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی.
2022
: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی.
2026
: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل عربستان و اروگوئه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23550" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23549">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_V5_VpBbRg3P5JwGyQ5OhAPF7AWaBERhqACX0ykjRygeFdOt26KNRRQWCY3javvxRlzHyAyTUNJgXdu-oYL_966KDf2BK-APxasGyz89rroxrFIu2vTgns8VfCFNvvZiYaSVLPYYp4nAqnuGDDPuXRbc9kSRUJDAK2rRKkn-syrHWYoJGlQZtP30aMTJ683IHobTVovCRo4BbLWmEzywndfKdwH3FyzCRD2aRKFFriqAqzf0W5ORMrpwxOBK17cTrgHHfksjNSnojW1o77JyCbIiWO5eaC1iy2jNcY8osc44uV3p9mLTc4CuDN2jV1QMA45kzKRQEVRH7RJPZvBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار امشب دو تیم هلند
🆚
ژاپن در هفته اول رقابت های داغ و جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23549" target="_blank">📅 23:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23547">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=s0y2yOocaToNp1QSIt_hCaAlr7t4iyFygOURy4A7wfMwhcUlICiXBVovyb4Hu2fXnzcVz4AqZgvCSkokg5dSag-kF5PDIyhL1kYNEHmRaXcAa7lOQ-0dFbs1gQJPcEqFLo8HDMVZInFjFaXqHVtawbk6TnEkAyAROdJTznTYxwwRWzd-MZ75TwlNJQVp6ugal9NS2Qu1VXNe-qQ_emNc3nrk0sgVnSncYnc6ScYo3UwMXRLjdqxP-rx37gs2EDEmzpfZiKM1pwXmDpXqZpVw55ko-P6iBsYeA9LFGlzOquGPzSZqz8TzRoExLMwU0cqq64PsSjcN4MEfnAKjsUtU-ilbg2-k0Zo-bGe1WVqT6JaSdWewFFR_E9qXkW28rcbDfop8qRzcFHd_z0Q_aYJUfgWYX0d88tquGQQ-Cbj9GjmP2lOjFAmjUdDpXbw-RsuFfO75ahMyZLoNQDQ_WHcoXeA-mqR1PAVx5dSRB5Q2DaEt2Ga9wRnMp2ZpCWUffxFtbzxfEF_au268frjmdX5OpO5RhwqWb1-kdbHn2M0d5suQr8vtB8GBrByePjoH4f00RqxSkahunlluYRS4zSSpDab8pi2ziWP-ZqBnIv5vucfV1uIo7WmfkOs6lHhRCTJ9yJfvrKRwXSoSeANISOljO6YSVggjD0nuHJDHpfzuJUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392bb7bb0d.mp4?token=s0y2yOocaToNp1QSIt_hCaAlr7t4iyFygOURy4A7wfMwhcUlICiXBVovyb4Hu2fXnzcVz4AqZgvCSkokg5dSag-kF5PDIyhL1kYNEHmRaXcAa7lOQ-0dFbs1gQJPcEqFLo8HDMVZInFjFaXqHVtawbk6TnEkAyAROdJTznTYxwwRWzd-MZ75TwlNJQVp6ugal9NS2Qu1VXNe-qQ_emNc3nrk0sgVnSncYnc6ScYo3UwMXRLjdqxP-rx37gs2EDEmzpfZiKM1pwXmDpXqZpVw55ko-P6iBsYeA9LFGlzOquGPzSZqz8TzRoExLMwU0cqq64PsSjcN4MEfnAKjsUtU-ilbg2-k0Zo-bGe1WVqT6JaSdWewFFR_E9qXkW28rcbDfop8qRzcFHd_z0Q_aYJUfgWYX0d88tquGQQ-Cbj9GjmP2lOjFAmjUdDpXbw-RsuFfO75ahMyZLoNQDQ_WHcoXeA-mqR1PAVx5dSRB5Q2DaEt2Ga9wRnMp2ZpCWUffxFtbzxfEF_au268frjmdX5OpO5RhwqWb1-kdbHn2M0d5suQr8vtB8GBrByePjoH4f00RqxSkahunlluYRS4zSSpDab8pi2ziWP-ZqBnIv5vucfV1uIo7WmfkOs6lHhRCTJ9yJfvrKRwXSoSeANISOljO6YSVggjD0nuHJDHpfzuJUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ماجرای شیر نگه داری علی اکبری قهرمان بوکس چهان در خونه از زبان خودش در گفتگو با ابوطالب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23547" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23546">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d02367735.mp4?token=aNSyPsoYP83v7B5xSwdpr9elWEVcBUIJwpuxs9YKOV1y2unVCXWhbqAoKjH7xfQ-SVZJrIwOAG166kOTUKlq1UqJAYrKyzj5-W5KyzLp1sZzKdC0-qEur83gBfTn-E3qFUioin1udodyttU7f3-lgr5jQvkCMnPOA79d63Auf_IWpD7uVbDT0e29Hy4KRSbSeOtWIoonRSKlrwOuLa26B2uNs3AeDhWlyZ1G2EVMuNp5ooN6ESx7aakdxqV5ZyrkFv7dH5f03HFHl28bv0PCaXCBMt5o5Q5PiTD3a_VLQoIQJ4byMz_fxHQq5vWH1Zf4k2ADgQQLp4yhOupfp-ASaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d02367735.mp4?token=aNSyPsoYP83v7B5xSwdpr9elWEVcBUIJwpuxs9YKOV1y2unVCXWhbqAoKjH7xfQ-SVZJrIwOAG166kOTUKlq1UqJAYrKyzj5-W5KyzLp1sZzKdC0-qEur83gBfTn-E3qFUioin1udodyttU7f3-lgr5jQvkCMnPOA79d63Auf_IWpD7uVbDT0e29Hy4KRSbSeOtWIoonRSKlrwOuLa26B2uNs3AeDhWlyZ1G2EVMuNp5ooN6ESx7aakdxqV5ZyrkFv7dH5f03HFHl28bv0PCaXCBMt5o5Q5PiTD3a_VLQoIQJ4byMz_fxHQq5vWH1Zf4k2ADgQQLp4yhOupfp-ASaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وزینیا دروازه‌بان 40 ساله تیم کیپ‌ورد، قبل از بازی اسپانیا و کیپ‌ورد فقط 50 هزار دنبال‌کننده در اینستاگرام داشت و بعد از درخشش در این دیدار و انتخاب بعنوان بهترین بازیکن زمین؛ تنها چند دقیقه پس از سوت‌پایان بازی، آمار دنبال‌کنندگان او سر به فلک‌کشیده و به نزدیک دومیلیون نفر رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23546" target="_blank">📅 22:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23545">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oImryE1AtRWg96V35KoY_0ByS_gYblY9mk2RoKV9Vl3wwmVS2QCSci27_pcVoZ4_0k9hpFFcty8NdnPangCaPunWWtkBRKqh5q7HLCsLuxkUVb52D_4Frf8MUYjCA0ji2Bipf1qo-XLIqWCh4rjDOAbT-a4iUNatnSa2IQzyqn4GXpBTOBxo5Psc7aQlwjkDMshtkyOyvx1KUx1rnhJWwma3OArtYMS4-PhZ4rQ7S4ebMi7PmS8fBSt-n6-96p4cF1A5tlMQB7VXEWq3lxkkQq5mYsDA9bo-exbLuPazoGEj_MMEIcGj1HeebxOApcIUB_N4OBRwpBABtK2la5wxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23545" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23544">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lULf1jcs_h-3DwoWrmDNFM2c07l26fN6MLr6HxhRKA97uqQTPqSkM_v67PZfmqZV8N1XhD2GaiIrrzL6V_iSAocsV1PpYGFhi0y1WSiF17luwShvPjMn6sW8W9W6YzZiEzigpL8GA4YJ4KBZomMWO7JGdA9mlJXLiSCnMj_ZXr3swD8isY118LTBDjkpwcYYCSLMlbcf10_apZRGsjLmRsmBmUbWRveBNl73i-fvSFShkLvqIdfuub0w8Mrq0DQRlMRKoFYK89mNyQWMk-12_IUOefZUvqWXSN5rsMEpxOAuZuf7uLfdGGgVCMkHi7byphgfJdaHegrpW67p_FVpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
جلسه‌نماینده کسری طاهری با دوعضو هیات مدیره باشگاه پرسپولیس دقایقی‌قبل به پایان رسید؛ ایجنت طاهری به باشگاه پرسپولیس رقم مدنظر این بازیکن روبرای عقدقراردادی ‌چهار ساله اعلام کرده و منتظر پاسخ‌نهایی مدیران این تیمه. جلسه با تاجرنیا حدود دو ساعت دیگه درسعادت‌اباد…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23544" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYvguUbG_8rxCIYFzmTdHgK-0r1vM4Jb2WrZm09EKMde-sXdPBUnN8pqNtOAm60xfsTk4i6t3AZWDWz5tnnHa_jjcefkHwMR_F-tPJLB-umK0Kc_HlNpOJefCmJN0-PQb_UT7Bu2ACQwLDNQGWODIhMWF6grGvzNJUp9Hw35dpxBGgaFxp7OA3RmPO_ZObplNXLvUxZlbfugYMxbvO3GDU3ioU3oY6kwexlGuF5xcb5BNXXwdf44qkC-RV6spMAorh2zuXKi_m-kn2jx_neT4a5oqcCile1zGDvGdO934Qtk5gFwxqwPYTTrbPSACTzVcS2z_7DJECTwwcLgW6z0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23543" target="_blank">📅 21:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23542">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI8-mgiiArVbRXuvmmxLd4Mz2uCJ22F7AlCI5JDL2qzWqeXLSOkcy36MM4FhN0qOj4mWNy9uPLm-fsK1iJeENVlPE2HovRe_eDaxVAULwlgsi85sRZaWvRd7smGvKrEqCpzd82HWJT6DJ7GHXNfUyUrv32CJ1yujkLh1N080Q9Za_p729mkENvCcJaoTYN93eykeHmdX7iW_d7CU60U5qCXNxFPPOOvci48JuidoF9wsoXpYRXuHAz0n23fB_r2Gm4ldd-M9jwgVYk_DZyHycf6yiz82jMGEPIfpDK5W2yg87lY_oMU3sPvqPyxo-DT9FqbX4b4CH0DsRk5vIWtSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|توقف لاروخای پر ستاره مقابل کیپ ورد در شب درخشش خیره کننده و استثنایی دروازه بان 40 ساله این تیم گمنام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23542" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA2hxRVvg_RIgsRvby062RvnuQiSElZEUdYTyDWEB2HOCQFYAftyjgt8_zkGIGx1Jvm1cPxa1JhBYg-JHLzS1yf7i8VpGZJZLe7M4seg47tGrj531sorVztdR8IRmhCeBUjkoyvsB0rnBGTqvG3uWoL6sh_WRbdN-Bz3Zg6su_ev88uluFGlmeE1gCtZUYYjR74iwceedRpP3wdC23fKe5aAodM3OcIEDd7-MlQTiX2-SdeczdSUVp67kA80mQ51GWEnjLfWCOb5sLal5GxJT9fr_IjVZR8xX8go6GHOfOfFMVVeYCMlmuLiVHA6qoCVtwoC9LyO1eyTA2JPa1jTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درو‌ازه‌بان کیپ ورد در نیمه‌اول دیدار با اسپانیا 7 سیو موفق داشت و مانع باز شدن دروازه‌ اش شد 40 سالشه و ارزشش تو مارکت تنها 50 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23541" target="_blank">📅 21:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmKMK7qBBXqItA_dhfYeb84jM9BkgjYNl8Oh-rI-lteB-prINYOvKUe32uMpgZFGpbGONp26JSNEcTSFmLIUBjDljCwSbv1vTjn0hxdCwp-fR6e9SX1DkBPUqbkoNbOgfWy3CPdK-SDe6j2pzWsQf9lX8kJV7fgirAZ1T2mvoAc2uOGRW_IF0_R6jdGbsGotjn5Kdj7iDdD1RlhnzVsqHZkaVn6fyX5bTvBDzHx76jg7hred5UZC2YEfnE6MWdhJaSCaHrakr_2Pi95D7w3DPGBysmnFLRW75ahkBM1D9t7tPV6aWN80cuU1Iig-L2kOu4UijHqZUa6I2KV7uHS7eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23540" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNmv_dMID_D-5BuGHSVqhnwluSNFXR2hvJJG0W7f7AlDOmOZHM9LBoJE6lKSVfcnbfyuNgwQa0XirA4CLNoxJVWaPLRzYtkwW7hd-1Dx8YmHN_r7nr8qd7cdMTRN6dJpfePaBdp8V2OnhhU-A_DeMjkKtsz3h1xJ9etJL0v4hS3l_Zzm1ut_4XRBbkXYrycM_ScPkBW8tQiED6HBvP5P77tojcwiWkX4sc6pbNHtSMIPFHdHdq8pVbbXpD0bU30nZVjbz0YOCE48YyNaGGJpXvMS2TWFdG7L63Bxf1qGrQej-eNeNQHZaIegnldIMZ8g6-65gaKqi_dlgpcqnapBEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23539" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23538">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEQ-P86tM4xcARHosv8zpDyjytxKO82FnWSPcOMUpPvnYhr6XvEJEoNfj_hfUEYNWU3IUjZLD8QiL9Ohpfi7NbgcESsiu3K-MOZ27zUUvO9XIWXUyQdu4GyncfZDt-ZocvVrdvUVYnDxeg5qEhlwv_FjM1Tjg5EP8K-Q4zLuK8Xnhz8JDmTYmVFGzYuTlVjbUtUEdqYX66Bmp1D9zABCfh9jh7KI13wiQaPZlN25sUw5D4k7Ce_b0eaxDk6TDxZDPEOygOW5cvFSJC9mgHFOCxUlYu2K6ZNe0C_co2briRbJcfn9OJ7D399nFEVw7WrnE2cL69JKTEfGW17QQAmSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - نیوزلند
نمونده.
🇮🇷
⚽️
🇳🇿
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
Apple Watch 11
می‌شی.
⌚️
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی
«
لینک
»
بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23538" target="_blank">📅 21:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23537">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehOO45xwVeNz4Qo1dpS24t1LkZ6-ARmw5lHeqvGog8k8_ZkjreN4mcs2nkEzQTbMTT7fWryD-Ri_V37qvIWiwOzT89Ksyq5lukgwjGX3hsSJ8W-Rn4oQStkUHb_1ktfs45mvQsN5OTo1NdLgJflhIHjmQy752RlTO75Yrrcu49FtTDWIe0aW_3oc4CDwWrX8NaoCRXCesypeq0i54fUwU2zsxF-YFqnS9CEQ7bxUdd9gofUkUXqlg2PiMdrE7paO2JxaNYheGg43z9ZXT1x2AnWjWBXKSpsfx_2_o0tcSBLhVnoQYZL7cafQXQPx7DeG7ER_MH8DvqzdlyVfsiDXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛
فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23537" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23536">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e29G-AfPeC9pmsX_xvCXGypGQknoDaPX4FpZXE65VxWlma52K5RCEQ2KU7M1-8UkyFn1FhtnD_j3L6HPXOue_bmVEXLGqhzQKW8fxaRozMMC3hBRyyAh5AUl5SgNfWCM0WQLaPQSWVzQ4ROUjqAgjudC5aO522b3Ca_xrDSLaCJtxD9K1O48kkf0hR61WQRWyMKyEmTuTYC3i9gfPE8prUq9o8s9hAQ-BZmpj_qQlk_WiE3hdQj7neH6hoT6bGMYj0do_xfkwM-VtSn2lOHnkDwvoprXztqz1_lDh5qTPN5kYudScItb_6fKtXgARXYWpWo7nrxZW6wtsqSnT9ww3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23536" target="_blank">📅 20:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23535">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBYeBlIfADpLqPlZHUITWgBe5_F2RMtz3JqAGQKU3gyqoF_x9YJ9WfRWwIraZh1jCI5pe8Kq7c68zBd4clmDEPPQvAT-mWDEEijozvqwabzOqg7jZ7u6Au9HKyq2j3nw8JKPQGQVbeY7ffQmYtq6MX6vG67vbEjEzxfiPVH1MOtdYIaVjlkZ0JtDf5HksmzUi51r-ZblcEiW4quBrO-3HSQ9dsimmw14xRxNvKkt0rChDrKiZaUMTTPgb9WeG-jU-0eFJYDy4QTD165Cfwzlsl8i9fAQ2o_iuw2ZOaoDh2w2qhNoUiT77NGsM0SZk7UsV_PCEI0hVdAPOec-Zerd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتایج‌اولین‌دیدارهای ایران در ادوار مختلف جام جهانی به‌بهانه‌دیدار بامداد فردا با تیم ملی نیوزیلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23535" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23534">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=B3Np4Th3TI1tC_JcdZ5qmMSrdU8P-AkAj3vOYjjqOtBnloxOlXLIyLv09vJl5gtseCGSP7dd4OaSSn1Ag4O5zeLgrpMNiHUhcdtXUc-xaeOout_yKuSMfjQ1G6oaVLSRbRGELA8QUz47mZU3heVQMDGC2vWsHyCyTxN2afOAqhEOdo4JkLKQuLhCcNegbB_-7MTGopGUiQ1wS_4fkqbEqLPKd7Mrk1W9c6z9qa_Iwsv7KevpCi_TWhKPNNc03OKATjHw1UThrH2-xuRZ9q9XxKxWU-LsmFviHLVqi_KWasNcXEycZkpcO-OU7x0YxgzXafyqr5vrLCw90jH16CwGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3e86a106.mp4?token=B3Np4Th3TI1tC_JcdZ5qmMSrdU8P-AkAj3vOYjjqOtBnloxOlXLIyLv09vJl5gtseCGSP7dd4OaSSn1Ag4O5zeLgrpMNiHUhcdtXUc-xaeOout_yKuSMfjQ1G6oaVLSRbRGELA8QUz47mZU3heVQMDGC2vWsHyCyTxN2afOAqhEOdo4JkLKQuLhCcNegbB_-7MTGopGUiQ1wS_4fkqbEqLPKd7Mrk1W9c6z9qa_Iwsv7KevpCi_TWhKPNNc03OKATjHw1UThrH2-xuRZ9q9XxKxWU-LsmFviHLVqi_KWasNcXEycZkpcO-OU7x0YxgzXafyqr5vrLCw90jH16CwGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23534" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23533">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De3jdFxtv8LXf07dNZPOjkVxtuYdAU-YIuAEHCsejDPd1dOh1MgTCYgZthkJGguy_sf6fyg2nS9ntmz7tHMCGjliWpod0SRgV4TxUI4VHzTjm0757UssucoHfsMgz8AwcfKsJ898J_9JUI6EI1rcNlml1MIxPgq75ujh3xIFQuvxqpenYM3Gq66nsPflDqTFMZ1j7jVwtxGcmqDdyXWHQGyyRhkXOqx2EqUHBmKByOxEKixKGBUSqIKzNJwYVTc1s0lOFNNpKmKfKv8Ud9ZDlq07wvHCwATeoFuYzQYb5y9_v0EBM7c_0j1FlAkj8X3GUyOVUvRzV3HIDOsoEjNKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عادل فردوسی‌پور: مشکل‌پرداخت مطالبات یاسر آسانی توسط مدیریت باشگاه استقلال برطرف شده و طبق اطلاعات دریافتی ما این بازیکن فصل اینده‌نیز با پیراهن استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23533" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23532">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEkvueTGZYa0guDtlW4Hu0oXvojMPkskcLXmmzWV5rDhjyfWhnQ14b67_SM1AQw_Ls0Lr7LiczPLuwUwOSPsWyMcic-FXvVNLi2OkbGSJAJAMMMmqC8wU6csjAT8C0QUoYgpfHaQdMZ3ofW1oT1pwDQq-ccmLIUmpB3R7VpaAmNHbvPIc4JXtvUIXVV4IrURxUElRE0MvGgeFhkNhg_g10e7AdbOaDL0S0ecWgC3i9OpBvxaZAN4zfty0xVV9KQqD_Y6BLSrDWCPlvsP7EN_nRnFkzUvvumKl2hStgQjk3fVX6JCNoAzRF10w7u4cpll3zYQusF5kC65wzGuPX-8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این نظرسنجی که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23532" target="_blank">📅 19:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23531">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzu9n99GJSWQhaMQOHM56sZW1F92Mgmah5-8aa8olo7xPVh9_qjVsQYQyg2lCRMzDkV8PHMykPbHvveU7LZAr4Lq-BxhACtQ5a19PXHZRQZjVErr0vbTXm_EsiLQQfFUGNL_FKtBr7Oj0nBnIY5BmUnKcVOiSlB31ZdU4fBLvErKOJIaZQF0PtqZ3vbonLLKB7NhKcyoUyzjmSWCN3TmK1xheowuaXG1KtbwUQGPCtkEsp1Rhj2dGLgddThk3DIep6OQMnKx0h08pslekK2vTJ7yb2wiV7spYVYF4Wine6JpB5NhcjZ7-qNV2iCuIg2Cqy2dQuWIrWh0aiflKMiGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23531" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=i45o_l-g0lu22JV_ELS6bBFzw_sSSY83ISHOBUqX4fRJ9ZoedcIsy9Qr8urIl41CXjSpqtv3Y3Vcbq8SPCdkEg17_XgkFvX9qlYclp0olY95i2lvktklRCWEGK7zIB-_2vuwGrdztJYSNPQHJQvEo_gRLtGpgX0GaiFVRUS4S5u_yNOhBM5W5-hukk2G4uhc-_vtobFW3_3ngw0o1uL3PL5WayS-pywawAnJlMQGkQURZ9E2DR3drqMMrNoViS1hK4nK1mIlUWM8lj-_EL9YbGKaheY8slaGp9O6tHzSu05CouruGKhmsboEkS5FNrjaeqhn6IiPYXVaKf6fwDmXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2efb67a.mp4?token=i45o_l-g0lu22JV_ELS6bBFzw_sSSY83ISHOBUqX4fRJ9ZoedcIsy9Qr8urIl41CXjSpqtv3Y3Vcbq8SPCdkEg17_XgkFvX9qlYclp0olY95i2lvktklRCWEGK7zIB-_2vuwGrdztJYSNPQHJQvEo_gRLtGpgX0GaiFVRUS4S5u_yNOhBM5W5-hukk2G4uhc-_vtobFW3_3ngw0o1uL3PL5WayS-pywawAnJlMQGkQURZ9E2DR3drqMMrNoViS1hK4nK1mIlUWM8lj-_EL9YbGKaheY8slaGp9O6tHzSu05CouruGKhmsboEkS5FNrjaeqhn6IiPYXVaKf6fwDmXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23530" target="_blank">📅 19:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23529">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fodMgcobLFtXjupWNJc_-d800gITAqsV2pUj1cPEqPACcMef3BYWcGCj0g-S8ObVtqbW9nP31pBC8YCgppJfiD-WNwXxlBoNrMaQMNSFcJtGITy_iL3Ko9nS0dvkNevKBezilMCzldrQ72AgLYad1xzpCXX-aZrqnNfOStHdGIDPeh5uOv_NQI-PjNRRI9yfySY1qXuQ4Obs-XboPrAjB6Y5NKsbFxgEnH--AM6rIEoRPn8VH9P89Ys-WybMYPoYVUtUpafj5CD-yS4ecj2ZomWowuWarN6bKaldawO49L3-t27cahu46zBtEeXW1jB9JteFSO-1Fw8eO-S3BmaJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد...باتاخیر چندروزه باشگاه استقلال امروز صبح مطالبات معوقه یاسر آسانی رو پرداخت کرد تا مشکلی برای ادامه فعالیت ستاره آلبانیایی ها آبی پوشان پایتخت برای فصل آینده بوجود نیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23529" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roHqv9R1IdFPpd56JCDjvbGj_sn2vsEYNZo-zD0GRY_ZiFBJBJOI8liXwlzAuz7Zsjjg1bCQ5uu1FwXp6oqYBDsqZHyhpbqSmKktpBFyPIwLw2ykWBZ2FlnZP49ytjmj-ZWMfu_S17AeD7Tx9XMv0N9fseVIzrYHSh5aBl7F478N7X0aebbDxP62AmGI11kbCN12bQPEtopi7iElF-troKhxq5nKj0clW8MNmpsvIfBvlP5aJ-X8CIJCvN1c4-M5mmvP1uSVS21RCQ-olD_v2WDBKbptEKEFi0iSy1NyRPOtBCnAWYdH5Ib8kqoqREfNpPd4XAl-PORjiWnExSnYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
بدن فوق العاده کریس رونالدو در سن 41 سالگی و آماده برای رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23528" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnDqtFTIvjCfigRhcxj12mwXKW195DhUxYg2u9d60aZxLMoO6dNjHYsmRgGuYHUUjQqPM5j4N7lrim99nffHe2404R2A05kNaWo5nyLrHVErSYQ4XcuvGSn4F420cVymv_fXx9lcrvHrVnDtn3NVLHIhzmIHsRVh3g81gJ0Ki6m7YwnAysMSYUoWHRfYKWDsimfx-YSXMjvPHJpDGb-ESDjZVUh8MwfrBumZTfONgKuPfGPD0eOxRcyNFYR1Mf7LMsFZKMvcoHE8kgETJ5lWCIHtVzbMdcb10nZ3t6Gd5wcel8EULrBX0ZQeDec4q3KezN_mFmaCSOkpAbRfZjiKHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#تکمیلی؛ال‌ناسیونال: یوشکو گواردیول مدافع کروات 24 ساله منچستر سیتی با رئال مادرید به‌توافق شخصی دست یافته و حالا توافق نهایی بین دو باشگاه رئال مادرید و سیتی باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23527" target="_blank">📅 18:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=k5nT5O9T7Nlm34KV6BjgofwlwwZ6G3MB-jiu4b_-xkLvhmbmUmxO0AMRFHuaOMDSowUfECDvb2-WIkXIMhEFwCtPOlRr0XB7dXHxZPku4mX3RzEDX_MLKbCPKDvoAmoxxD45A-0t6msufq6Ph_N7GYXCRINLXJXt8Qbe_bZRjAKxztN-v1qQh99oMlZXxmaKkn7XSEl8lElJ1RmurRr7FNGRcbzeRUxCOVxhAlrokBM5pDexgU7ZEkfn-SEG7qxPaj7XZHOdFA7iaFNgQw6DRKY8uLTeyaWl1xgRKFZ6kH5F4XO81xDQLG17UMJu6jwnQTYb8r0UjOUJHsvRRkb_tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d57c883d.mp4?token=k5nT5O9T7Nlm34KV6BjgofwlwwZ6G3MB-jiu4b_-xkLvhmbmUmxO0AMRFHuaOMDSowUfECDvb2-WIkXIMhEFwCtPOlRr0XB7dXHxZPku4mX3RzEDX_MLKbCPKDvoAmoxxD45A-0t6msufq6Ph_N7GYXCRINLXJXt8Qbe_bZRjAKxztN-v1qQh99oMlZXxmaKkn7XSEl8lElJ1RmurRr7FNGRcbzeRUxCOVxhAlrokBM5pDexgU7ZEkfn-SEG7qxPaj7XZHOdFA7iaFNgQw6DRKY8uLTeyaWl1xgRKFZ6kH5F4XO81xDQLG17UMJu6jwnQTYb8r0UjOUJHsvRRkb_tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
برادر از 4 سال‌پیش‌تاالان‌داره مینویسه؛ سرمربی تیم‌ملی‌ژاپن با همون‌استایل خاصش همچنان میتازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23526" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEildknynl_r1Cq2hNOEm9_0p0l_TLzXRioureEjVNQMDH60W8lNiX77tESEeduHlRosJ8MOvIw5dVUpoodMwuLYed6SI1mHtf4wcDFpzf-qd1a2E8N3805GJZZRgPV7nhrdifkzZKHWkSKfWZ-WQoev7SxOm5gL3Nca-QYQ9MJiO5myW8sSyhxHCDOfCsqkDkuAqohEpYZy204mQrnoD9-H5xkZD5F7BiYkG0CBICJ7eKjak3WiOhKN6P4eO8o3VHOsvTua5F6TBglmOu--vx_tEHHSidN8oRvnVEZUfK4jMJ7gnWtGPWNAMCz-5JHvKK2_yO4ktbGlKHFFr963Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23525" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=J84Gp_1jgCoaTziqFCedhs2y0CEi5oedfP1VshBmOCaXcsPsf53uIQs-Ldi7MAyUFd3FMSzriC4FaXa8WYih8jqS0qQ5KAIok_yg_b9xwnbbXZyyASLORt_s_J-I1GMIgdA6obkCrmteGUb2_CrVF0tiGPy6aD7g5xrb1bylNAxfPbVPm3tRvvCv49MrbL-f2ib-wLyqKz_tVB_H6oBZq3RPUXATD1r1VlhOSYfwf8WDKCHwtJd35jCQ5adFA39TNNcCdwO3efJA99hDaI1kt6ZT_Kw6NtYox0j-4jbT6T7ZCYvZhpPLEHG49SFfBynSIwjKxy43FR6XO8eOoNJyeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=J84Gp_1jgCoaTziqFCedhs2y0CEi5oedfP1VshBmOCaXcsPsf53uIQs-Ldi7MAyUFd3FMSzriC4FaXa8WYih8jqS0qQ5KAIok_yg_b9xwnbbXZyyASLORt_s_J-I1GMIgdA6obkCrmteGUb2_CrVF0tiGPy6aD7g5xrb1bylNAxfPbVPm3tRvvCv49MrbL-f2ib-wLyqKz_tVB_H6oBZq3RPUXATD1r1VlhOSYfwf8WDKCHwtJd35jCQ5adFA39TNNcCdwO3efJA99hDaI1kt6ZT_Kw6NtYox0j-4jbT6T7ZCYvZhpPLEHG49SFfBynSIwjKxy43FR6XO8eOoNJyeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
آردا گولر ستاره تیم ملی ترکیه پیش از آغاز بازی با استرالیا خطاب‌به‌هم‌تیمی‌هاش: یالا ما ازشون قویتریم؛ بیاید این رو از دقیقه 1 بهشون ثابت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23524" target="_blank">📅 17:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIVEo1xzJDPe2U1vXL3_Fow8ePIrRtej4QPEtMoBwPJTE426twCJnJqIG92e6bOJDaiRTBiKAqVvbo8O1ng7v1Bwnt4u0SXYMStiSw4kx_8PYfKs_KKgyfCJpuZKeKMurHNwXow6UZU15mPsIDJ9JKqBphq0b2JPc2V1OZ5-SCxI04jfW78z72UrXUWnQoCROTndN3G-p7SH3keW344p7CD2LFfLHrWOEt_rQBMo0569NnC-YJ1vMX93cd1oIdVjXYtzrTjN33pbvLMHu8Td7-qMWS1wwljzLfG705xIX9CnMtGjE4z50L5wNLTwslR5TL_G2upnXdBZEkOv8lTDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23523" target="_blank">📅 17:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxzTBb1DhoQ2MFhceMblx1Nz7keuAuXhL8EiOzvSQwrY5e6SsYVca-EDVe68P8MDomNRoQY_qjBUR0_dab8Mfo4flhS8Omg9-30-8oRCxSpGG2UR8mn5lZby7BhFs8ewSWZtw352Q2hDMGWxVL_mU9by_wVQ-iTM1OguglrX8OhafufWYqIibc4GauaD2mnRYyBBwxk0x0h7vRtdo_8iD_yFmlyHVDP_uwQ8-vhYlyBnn1Md4jlWHalE22VaSr6FoXCkn2QfWb_mlu_DPy_JV--9TSZlHuACqcEFOVNJxJ93a7UGe1vQXcMuL9CFUEj79kF0m2UH7dym2hwpZs4dHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23522" target="_blank">📅 17:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM-2SgC6Y4oh_cer7xrCCx_pgoWIrvRC8VqrexME2vrmf99i2B70HjW3imMmW_9oJMdsH5BMhYmBUyTH77TBLqFJPEPJdc8RKUiJPQ08QZ8Cl3JoaC-8xFgNL_t7QxDdDOO7uT-78B71JTLmx_6cjfEDi4-DFdycEI-MW-tu6BViwQeQLxzYv95Z5JHlKUtx7pprde2Do3RCV8Immj-aUe_ArVEt-up7gyRtPkp5f8Ewf8BQQ02pSZA6cMmJWj2Zdph7Gtiy-G7vVewV0hJyVJ545l3swp95PnNVJMkwEuW_dCqP-iSR91gxk-EkUM2T5S_bfzuTMLHIDv4QEdAbRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار جذاب امشب دو تیم ملی آلمان
🆚
کوراسائو در هفته نخست رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23521" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=MXehyMxZVBwhQKrO_tsg1G-QNzrnEg1PZzRv9PdE14ZmB7QQqUUy0Dp148Vyr0pazVBquz74WCJgJTRwA7FvAhKJF192oRm8QN00mn--PzoByYUZ5mvuZ4zlUwTsjs8J-WttZZcpbuZjO5vKzSDlWLeuG6AxUQAOJwYEHH6GfMHlfcXqiLGfmjffBCM7iVhsBvG3TAxh1a6AbHAwBE339-J3MwPoOowpxz131-R_9qjazFqOM-DY0k2qDcXP3rtaPoT7HeOGoT713riRVODGsG12B_5eGQA-erpCE0VOijMPIyhVDKNVucXAuYByHTftqbrET0i6KvxWZsYPWW0cJjCPEYFLR1q77yHE5LLV0oGIXzEm9s2ozr9lktkt8MBSE6GGRDiuIQSz9Hw22pG6mxdWh6pE4IkOJaUxHOu3v1xOTl83DMXcs-ELryomtkrW7Bp97S3wkkJec2Jcy2mJ5TyIFrlaVy-NsNF9JwK0m_-6qlx3IppxS0tAodH88HckR5E8OGqnzKJk0rM76emSyuqsB0V2-1GyyhC8yJzO9PkwO8cCI2MTjyxOZ8L4ZOUxqnEQeaHjx6_cqUmdH3T1wi_KQR4GTQkt3UN_gKKrKuVzwK5vI3Asc5EqebvU8IVaMItXFH0M7ySb8_4snzyeZGVhlXRfv60cKqoMs4CbCcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=MXehyMxZVBwhQKrO_tsg1G-QNzrnEg1PZzRv9PdE14ZmB7QQqUUy0Dp148Vyr0pazVBquz74WCJgJTRwA7FvAhKJF192oRm8QN00mn--PzoByYUZ5mvuZ4zlUwTsjs8J-WttZZcpbuZjO5vKzSDlWLeuG6AxUQAOJwYEHH6GfMHlfcXqiLGfmjffBCM7iVhsBvG3TAxh1a6AbHAwBE339-J3MwPoOowpxz131-R_9qjazFqOM-DY0k2qDcXP3rtaPoT7HeOGoT713riRVODGsG12B_5eGQA-erpCE0VOijMPIyhVDKNVucXAuYByHTftqbrET0i6KvxWZsYPWW0cJjCPEYFLR1q77yHE5LLV0oGIXzEm9s2ozr9lktkt8MBSE6GGRDiuIQSz9Hw22pG6mxdWh6pE4IkOJaUxHOu3v1xOTl83DMXcs-ELryomtkrW7Bp97S3wkkJec2Jcy2mJ5TyIFrlaVy-NsNF9JwK0m_-6qlx3IppxS0tAodH88HckR5E8OGqnzKJk0rM76emSyuqsB0V2-1GyyhC8yJzO9PkwO8cCI2MTjyxOZ8L4ZOUxqnEQeaHjx6_cqUmdH3T1wi_KQR4GTQkt3UN_gKKrKuVzwK5vI3Asc5EqebvU8IVaMItXFH0M7ySb8_4snzyeZGVhlXRfv60cKqoMs4CbCcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پیش بینی 4 بازی امروز و بامداد فردا رقابت‌های جام جهانی؛ ببینیم چند تاش درست از آب درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23520" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=DQDjBTyemqsneijs8RjysEL4QfwTV1IpZ2rklsW4B6Wnc6eaJ1ZhdiHWMFzynyZhsJJ0TXTQi4n0sG_qInKVfxhsD7dGnasi2vw_3ZvU4ojCbQZN2i8oZRUvhZMBiNS95P4PhqDJ28v9GZDlMUnp_3QOMO-CHcWn0fzUZdOZEEeKSsDXIlQkhFwSFBgDfVsQGcseTrTmWYre-BPjXQ1b358lJHkCg36ppTmutIPuKLP6b7HtVT5fL3FThPxSox7ABWpVak9eay1cKgBEuFB5vWZlXkN4TllUaZKAvXq7jy3nzx7HiPez1u54ROq_CWiO2btQ8m9Jp-BedShVm4tffQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=DQDjBTyemqsneijs8RjysEL4QfwTV1IpZ2rklsW4B6Wnc6eaJ1ZhdiHWMFzynyZhsJJ0TXTQi4n0sG_qInKVfxhsD7dGnasi2vw_3ZvU4ojCbQZN2i8oZRUvhZMBiNS95P4PhqDJ28v9GZDlMUnp_3QOMO-CHcWn0fzUZdOZEEeKSsDXIlQkhFwSFBgDfVsQGcseTrTmWYre-BPjXQ1b358lJHkCg36ppTmutIPuKLP6b7HtVT5fL3FThPxSox7ABWpVak9eay1cKgBEuFB5vWZlXkN4TllUaZKAvXq7jy3nzx7HiPez1u54ROq_CWiO2btQ8m9Jp-BedShVm4tffQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23519" target="_blank">📅 16:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=pAkqocAV3SgOjhxOaUaIylDvMJ022-oUTJFL9QyOn8PQZc_wtBtjspGFi6GvICETrP36cIGidj5ve92sEpsFKzpbKYpCtIkBbKDz_2xtoVwA4iQ0bmwH6LdtVxcRW5ubjMILqd1IBCAUS7IU6jxWLTB3s3-QBDpZxbIaLZ1b0fkhWHaMotATOkTZt7dbf8J9supn_AtXdDB1sUCubX4kB3Lp4IwCmmb44RlM0CzBVRBlUUhron0NepMrKOLn2LYSykUMgvAKqX9_m3LBeHBYBzwQArUslRMnCDKw5PwBsdCTYELgFSA4xKh5Pu2Sl8Z9fNJT-8XeNW2kxTC5ENwv2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=pAkqocAV3SgOjhxOaUaIylDvMJ022-oUTJFL9QyOn8PQZc_wtBtjspGFi6GvICETrP36cIGidj5ve92sEpsFKzpbKYpCtIkBbKDz_2xtoVwA4iQ0bmwH6LdtVxcRW5ubjMILqd1IBCAUS7IU6jxWLTB3s3-QBDpZxbIaLZ1b0fkhWHaMotATOkTZt7dbf8J9supn_AtXdDB1sUCubX4kB3Lp4IwCmmb44RlM0CzBVRBlUUhron0NepMrKOLn2LYSykUMgvAKqX9_m3LBeHBYBzwQArUslRMnCDKw5PwBsdCTYELgFSA4xKh5Pu2Sl8Z9fNJT-8XeNW2kxTC5ENwv2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت ژائو کانسلو ستاره32ساله تیم‌ملی پرتعال وباشگاه‌بارسلونا از تراژدی تلخ و سنگین زندگیش که در سال 2013 مادرش جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23518" target="_blank">📅 16:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFaVvSmwOOHkIcizNecHtL_izCYIeoGGPVCTQlbO6Fz_1_pmvcFkv2lGAwu_ShLdp7q2Uu9cdtft8PAPD3VHpmnjZp3gzgjGru5Ww9flymFDlQ26rma0BOgkWi7YV6pyJ68g6hitK78yefat66VqgSxD2xBP0afyD6-LysoK1sWka_bwSGBg57QTu-dCBUxBIcwRQ2ic24sFKd0B9kPmHCtijPwEpzHBhuq8mm60TBgsjS_BrDerl8FN0n0D27c9xBItMd9apzcrseC9ZC7ak27kp58-JAR1-C-WITU1tmZOqqyA6zI3zM-ZptlepTRUhNiD35G1A44ls75zsNLjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک‌کوکوریابازیکن‌سابق‌چلسی‌ومحصول اکادمی بارسلونا به رئال پیوست؛ وضعیت باشگاه بارسلونا:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23517" target="_blank">📅 16:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm0b9ULrVImQIoz3_nFZ-ocgXLDr0c7_Ug0QBnatHZ0CvKyd15Kjq23ri1twnLOsnowKX_pAA7SPD1KthrHpppafuv5K1A4gg71xhXax84LoZgyTmMZVmZ_xiggM3t1VxE_6BkpnyyUbUq6rcaJ4f3A31y-4xfJb4p_Z-f1s4esLKd13WzcJfI0hHryzaPXExpBAMdYw5mMwbWF6qPZKnYbA4hN_2wDh8S3L5NK-d_UwqIF7HP1FWjtlBSOv8NQwflyvsPoyrJEHa_QkAgKGDP3uuan_S4hcXniqPlZQfCEIlwRm7uXtYH6hzv9m26PbLnZ0zLAmLfyIa00fbwahag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23516" target="_blank">📅 16:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN5wo37Ibn0L2R4ngRoF_AQrozlZ7JhTFfjOA1DWOqDWsGjhadULcU3wfyGV-HlvCY4bxOa8wBFrLaMvWZzH7hN4FN2XM_n6RpVadr-Pe7c338KBrjSEz8RgKk9q7REZszUfy6VcgxpaonNEHxRszLyyyQy5MND5gUsVr26EiruSugmv2yXMqAa-qhSwDrnnil-oN0lCg6tH9sFsLtiUDFwdDaXkqu0IUk62YLq5qzGgSSANn_hGJYlGw2ZTTiTchgqCxTcEsUN616e-CSnI3qVfuFnG5pHrIltlmViR5LJJ_53xTEEktix1umJv48rpLsblxSEgbDp6ipVFsWUutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23515" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8Z4rd1ViflLxyN5CzYmYnOmOza0rw9f-_W2JbYx_GImWXT10ZywKJTWJ8A3Wb6BW4y5TL9RCjwEBYVyVzynJREXlSQeIZkuhzwm9sYn4rqOW9QpUt_fJIKBXgQhlbfZcNEnwnPcsiCESJa3CoD1RA41q5HV3XS2IuBeKDhMDMh5xl6ecPrCQGg5Rf6-TaMUIg-E2hqejn0wtC7j6lvd6WXlH6gYCyhsKNYAW7oPJD7LJTa9THziWgDhOIrO6B0sCqkIGzrnqTteqmXLv4cutvB_1U-bPXYXNrw0vR5T_Zunj5EV6acJv9LjQCXAxqpVOSfB14xWYN-q1xn7JpoA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوسمار ویرا سرمربی پرسپولیس: بارها به مدیریت باشگاه گفتم‌که‌به‌قراردادم به این تیم پایبند هستم و به محض آروم شدن شرایط کشور به تهران برمیگردم. لیست بازیکنان‌مدنظرم‌رو‌به‌مدیریت‌دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23514" target="_blank">📅 16:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9SBWHsRHW0YgNfCXZDVMjh0gjwVgbUstcXV4TUVp_9aD7EPEBT9jnDxduMQwXdqllEzXBbk4_0UMzj4Urp9a2ePASukv-W6tL4uzz9LMVPbYbJL1GU-3Gf2ngSgci-4OCcD4N1qw2IglGtpm-dj6z7NZTPeBxobIxxc91lTp-0ODsk4s_pj9Sdau-hdL9lGoVByra1vNMzazoj9gQucWL4WIV1V4bGbeT6fG_iko7lLBk6OHVpPZ7Qbsyr0dGTDbXyR7R8ZP6cZJd0RoJBovZej7fMlQYrwJjy0-j27tBHeQn9iALcszzDFaKqrc5y-q99mmnGZ2vo47BKlXlG3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دایانه تومازونی‌اعلام‌کرده به ازای هر گلی که برزیل توی جام جهانی بزنه، یه عکس کاملا برهنه از خودش میده بیرون و اگه برزیل قهرمان بشه، با همه بازیکنان تیم برزیل یه دور می‌خوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23513" target="_blank">📅 15:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=ArqFGWcSWkxFcPRQoVxhAjRTUtJvAZ08Ctr4I9jxVLKF4sYiumx-3_cpFWE7R4bp5gjyEpPf_WSwkMBiL6yC-e2At9E90XYiAcb_cwUQdfbqpuhf6i7S0XHhi21arvLvUQHJZiN_BOJdk8IgvU348SqOUfVBwnIb6eGsMZuWsR9kRAzvTYBfF06FklzwH-verqcEOuvnot0bbq7UTZR8qlJhRWcyHvxRHBcxqeMtzpc3lZGkDuHrFc4bcCgKlLhcMNOu3x3xzGpJJXUdU7Bf1MEZDiXVJLDYk7jbZ0wyk07HxKXX47zutYW5CBwduMqcy_EOSz9NbZJHZeZuTHDGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=ArqFGWcSWkxFcPRQoVxhAjRTUtJvAZ08Ctr4I9jxVLKF4sYiumx-3_cpFWE7R4bp5gjyEpPf_WSwkMBiL6yC-e2At9E90XYiAcb_cwUQdfbqpuhf6i7S0XHhi21arvLvUQHJZiN_BOJdk8IgvU348SqOUfVBwnIb6eGsMZuWsR9kRAzvTYBfF06FklzwH-verqcEOuvnot0bbq7UTZR8qlJhRWcyHvxRHBcxqeMtzpc3lZGkDuHrFc4bcCgKlLhcMNOu3x3xzGpJJXUdU7Bf1MEZDiXVJLDYk7jbZ0wyk07HxKXX47zutYW5CBwduMqcy_EOSz9NbZJHZeZuTHDGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش صحبت‌های ابوطالب در برنامه‌ دیشب درباره اظهارنظر رهبر کره شمالی که گفته بود عاشق لئو مسیه و دوست داره آرژانتین قهرمان شه عالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23512" target="_blank">📅 15:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=UyispEs5RF6pU4r4jZxQHLQezQG3mKfd-pyyzxrE-CbLATa7AWGkG6tpumUos9GXGHYLXRBRA2uNzD09AI246hYbY5_cmW76TLjUFDC638NJJdBiIKF8c5M0V4MzbmBJCF6xi9zGzC1PcayNcFyqH7yX0iMFl_467MYbGCb-Zpl0uwLiztrN8zP0cygcBpzJkKZx-AJBVKBjFrm3_JETO5qqD_4juFF4sJITcXcmV-qVdI9uizlKgpZjqrNfDR2ZP2doVB7r8oRZCUWvksBSt40NZt9MEWTLa0PVihb_7S0K8r9b6JpITDLx3Hj-OL5eBhzsVxLZQsvIlArmZsfE4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=UyispEs5RF6pU4r4jZxQHLQezQG3mKfd-pyyzxrE-CbLATa7AWGkG6tpumUos9GXGHYLXRBRA2uNzD09AI246hYbY5_cmW76TLjUFDC638NJJdBiIKF8c5M0V4MzbmBJCF6xi9zGzC1PcayNcFyqH7yX0iMFl_467MYbGCb-Zpl0uwLiztrN8zP0cygcBpzJkKZx-AJBVKBjFrm3_JETO5qqD_4juFF4sJITcXcmV-qVdI9uizlKgpZjqrNfDR2ZP2doVB7r8oRZCUWvksBSt40NZt9MEWTLa0PVihb_7S0K8r9b6JpITDLx3Hj-OL5eBhzsVxLZQsvIlArmZsfE4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همسر کوکوریا مدافع‌چپ جدید تیم رئال مادرید هستن که در مصاحبه ای گفته سال‌ها رویای پیوستن شوهرش به رئال‌مادرید رو درسر داشته و حالا بسیار خوشحاله که این‌اتفاق مبارک براشون رخ داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23511" target="_blank">📅 15:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZBL_Jntfwi90-gYRe18HREFG5QX3a4SAxYUcSiaV402glqGQABtZV47Cl_-YQdNgjgzZWo6sKAdWznd5XpU7ARPZdfmt8O0L0Y6Ti1VFEcy1TmyRze4sp2HCF2KAnCSgpseBfjPPlNPjUznapiI-9Z5v8tA6sH1Fm7fjIb3dSEchE6DFsimpDzzwu7LQOkAH3hJBD9aJT8TumPegAkv65z58_j3eQ5epMUIFfLWaqA50wav9cL_YsQCCbKpJTn-R8afaZV6QmNllDrLX3ThD1ie8cqv3BCKJwHzHVhYsR_mdVgsBeLwBgekICyOv5QoQEz5quis8qGmSMhYb8Fi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه‌بندی‌شادترین‌کشورهای حاضر در جام جهانی ۲۰۲۶؛ مطابق معمول ایران اون پایین های لیسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23510" target="_blank">📅 15:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFdbhlw-ykWNQGe2AzU8M_3AvKhDdREfk86KReJHsBD3aqGR19yLkE116_6lSUpa6Lliqvqa1lB-P95b2VzWtLSKJRg_I8FwyABIu4eKpn15WauTlVP02wPvAzPkBHV4gquBxdO8q_SDziVgsy3G5JpgcXPJ7QSV_QzD3dfb92CSUHSJTWtSkTUBScZ4uQ0X3M6gEkoyMpYvD-0xzwD5fkF2dCc3oozpuvSfG1N2Ifhb__tMtxHtMBgsLokeCT67JEtwYX3KGDpf1goKa9FxpR43aPbDQ2wSDSNc22l5TvV5BL7kMG5XeCVHJYeDROVgkbrN_Slc2NjIp4bpDYXclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نیکو اشلوتربک مدافع ملی پوش 25 ساله بورسیا دورتموند آمادگی خود را برای عقد قرارداد پنج ساله باباشگاه رئال‌مادرید اعلام کرده و درصورت توافق دوباشگاه احتمال این انتقال زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23509" target="_blank">📅 15:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=Wu2DOI0q_yAFoBnRFuwJ2rvwAKucRKJlzzSeRRMugD9e7Qh1eMLSVBZyShJWVFVM8A6oHNL5kjLpKtpoB_4-odygeFyEUTrOvQdJOT8aXuMvQd6pg0hJD2IQho9BurE35u9__61hTTqdTe5bsEN-dd7Gi6PE-EivkliG0BXO8Nd0ELgVl4K2awBxa2P8ACveLUBfwNhjFfB1sUH0pVyW-DX5y9TllACvcVJNnNby0mHHerBqOcuOvdoGUj0y6PWvhQa-ds9SOZY28WFQIc_QYNPCDX8aI6fd7V1_CzVG0Qm8pcvC9CyXL23TD5qfWQToEmUWL19lw5e6-XRGQvsX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=Wu2DOI0q_yAFoBnRFuwJ2rvwAKucRKJlzzSeRRMugD9e7Qh1eMLSVBZyShJWVFVM8A6oHNL5kjLpKtpoB_4-odygeFyEUTrOvQdJOT8aXuMvQd6pg0hJD2IQho9BurE35u9__61hTTqdTe5bsEN-dd7Gi6PE-EivkliG0BXO8Nd0ELgVl4K2awBxa2P8ACveLUBfwNhjFfB1sUH0pVyW-DX5y9TllACvcVJNnNby0mHHerBqOcuOvdoGUj0y6PWvhQa-ds9SOZY28WFQIc_QYNPCDX8aI6fd7V1_CzVG0Qm8pcvC9CyXL23TD5qfWQToEmUWL19lw5e6-XRGQvsX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شیث‌رضایی درمصاحبه باابوطالب حسینی: همه روابطم باخانم‌هااسلامی بوده! دروغ تو کارم نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23508" target="_blank">📅 15:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=oqYLEhbci_-IXyJuxZ3J6fxfRuihy4D2x4X9Obedv-ktcT7moE2tC4X-kXCFJIGVF9um8mmRk4l8ErAPbloxDs9ECt4XLXm-OXwrgYwPogDT32mqpwC58SFzB8dvkbggK3RwjOdNqYBgFEPVxHELJw63YzThivNaKxceVxtyYVxAI1ymKhP7dNGQN4H13pOBOggKeSN969Eg5aEhKZvHv4IpIl1eUXQ-PsRM_JCoRPLUf2JfEfCrzQAUPX9NAFiuh8nf4OWm_XuCbZUOcxnzRUaJhy_GW57ll0RA16QpeCXBpe1DrJ-ZBIrWJi-5ufF0NzyKd9XXXbVNLl2Eut1WBiJkD4b-Yk9P1FmX7smAXE_L1S5jVk27eQz47ZvUzXp1BLfe07Oi1d26mT4Vh0GWz1dxa6a0Q6pjT5fa1q4eI1AkJ7tSE0Ate-2IQimBnp_Nl6AiYEeMKt9rRhD-XoVR_M4AFPHUxUKKMGkBn6owo0FEoMKaaKqSuQLZ9BFx6CQRW4RO3qSFjY28Ftl_8UmjHfpeYZ0tIQ9OCSSZhXRW39CfMgiEUjudfF2zP01Xiy1wf7N7OW1c2gj95VYzvoBRjSnsF4qriIqK7JovzsciSw4WkQHAqsiuWqb7FgTw8KkpjBc9Tt3o7Md6hO7oTDKFC8BRdjRPH0ZTt6smdi30YNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=oqYLEhbci_-IXyJuxZ3J6fxfRuihy4D2x4X9Obedv-ktcT7moE2tC4X-kXCFJIGVF9um8mmRk4l8ErAPbloxDs9ECt4XLXm-OXwrgYwPogDT32mqpwC58SFzB8dvkbggK3RwjOdNqYBgFEPVxHELJw63YzThivNaKxceVxtyYVxAI1ymKhP7dNGQN4H13pOBOggKeSN969Eg5aEhKZvHv4IpIl1eUXQ-PsRM_JCoRPLUf2JfEfCrzQAUPX9NAFiuh8nf4OWm_XuCbZUOcxnzRUaJhy_GW57ll0RA16QpeCXBpe1DrJ-ZBIrWJi-5ufF0NzyKd9XXXbVNLl2Eut1WBiJkD4b-Yk9P1FmX7smAXE_L1S5jVk27eQz47ZvUzXp1BLfe07Oi1d26mT4Vh0GWz1dxa6a0Q6pjT5fa1q4eI1AkJ7tSE0Ate-2IQimBnp_Nl6AiYEeMKt9rRhD-XoVR_M4AFPHUxUKKMGkBn6owo0FEoMKaaKqSuQLZ9BFx6CQRW4RO3qSFjY28Ftl_8UmjHfpeYZ0tIQ9OCSSZhXRW39CfMgiEUjudfF2zP01Xiy1wf7N7OW1c2gj95VYzvoBRjSnsF4qriIqK7JovzsciSw4WkQHAqsiuWqb7FgTw8KkpjBc9Tt3o7Md6hO7oTDKFC8BRdjRPH0ZTt6smdi30YNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی زلاتان و هانری، اسپید رو دست میندازند؛ این دلقک نمیدونه ایبرا خودش ختم این کاراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23507" target="_blank">📅 14:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAjqK3rl-iMNkg7Biqa8oH7tjUSiHFsfFKEV8hvqh1eMwEAH2hFIMouAQsPMt9DEjRqop_hzRWHcZh3MRgOLTWpXecDH5W_EBvPs_y-3z1GOx7ErNO80NzXVYj2cXst3ARnoenl7wSyW12VCbCupNdPGH5nLaG8a46gbANnEHLSKyJH4BQzGdOEeMQm5-I_qTxOHIQhmrp8KIt7vwx1n4HL1nefvGMxP5GRM5hbDQn0wP8jwiBW123jYNdQMPdzyx1B9pCCkHoFNu52YnxSV7X91fD1M8hP6ifPj58Y7ld71mvmbqev6_rXq9M5EOL77Bqn_tAWjtQL6lIa5jmkMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23506" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-udaA4KYOsUgym00dROHUh7i6w3y2NnZ2mXsnYdjqjbMEq6KbhOLChguQzkUcSeEAWHEjvan2KQdgcXhD7ZhEQklc2rDxrRzYatwT6SLOOm4XbhX9U1aGI9J-2KKmMcF3BGloLxGqhlUzzfpPIiwYjF7lnbYkqVEZHSA01G-pQY05FhMSK1dp5PBtpgNA5PyoxWW86MnjkdrMehEVkUIR6FycXGdsgYGY67Ukl3NdC7ckNxN5DP69sn3J6rkjb-Sl1Q9d7lfqOeQNZE3UCTRNdgOnihagADqlVp28EKQ9fudRscMdekC9zsWJGgQB7jntq7SZ7FgyGQl5dhkT5FtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23505" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358a407b96.mp4?token=Kd1RIj9I5-TUjzPKJm7W3e3IuOk-ZONRLZm2fXnCrTU7qs1HIB--ghAvD5pIGTc7iIuuGs3r2Kxx7UpXwzBESoAItLl-JlgXhYz5NjBYGxxW-p06HoirfbSZG8y6gu0gL06v_urRvSPYWTVfAQBMyFolkZPmJJDubb3nSAw04WNKB1S_yM21MqCJntecoGUZp3WoZtZ6NJBjiznWhay1NpmypuxUdLTsOOsph91OhRH8n1PWA8qqlExE00dtXneb9gIoEVXny7cTi5szADdjKaI2wLpRlDHuf4Xb38yBI61LI41bgNABo8kni0N6BW65gz5AHKQH-_6VvY0Py3We-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358a407b96.mp4?token=Kd1RIj9I5-TUjzPKJm7W3e3IuOk-ZONRLZm2fXnCrTU7qs1HIB--ghAvD5pIGTc7iIuuGs3r2Kxx7UpXwzBESoAItLl-JlgXhYz5NjBYGxxW-p06HoirfbSZG8y6gu0gL06v_urRvSPYWTVfAQBMyFolkZPmJJDubb3nSAw04WNKB1S_yM21MqCJntecoGUZp3WoZtZ6NJBjiznWhay1NpmypuxUdLTsOOsph91OhRH8n1PWA8qqlExE00dtXneb9gIoEVXny7cTi5szADdjKaI2wLpRlDHuf4Xb38yBI61LI41bgNABo8kni0N6BW65gz5AHKQH-_6VvY0Py3We-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احسان‌محمدی‌مدیرکمیته‌مسئولیت‌های اجتماعی می‌گوید بخاطر اتفاقات سال 1388؛ تیم ملی فوتبال ایران دیگر در هیچ مسابقه‌ای سبز نمی‌پوشد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23504" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=lDphsEvka2ohHaV_6enCo4GovWbKu0wyF6miYZktfxurXUMx9IFLpLVjovk9aUtvMvCQtaxrSEmAETzdCotxkJK3QKNMKSpjiANtXAHKf1HMk9fo1S-hfBVDHqApuWDONUF64_Hh7yfDpEX5IYXzSihqmOHT13DTv9Dksq75eAE2AVPTRlFABPadbzdZrkAzrJJghwlqnA5nWW6GoJCh4o24y8FVIhr-a5h8loZlYKDDv4sz8SOqv0guyUXvIC9O4NU4TM0iS7wSpgHTiDMRTHijs_0XAI1kmrKwC39cwKULf8tLLvE3scwzYMy_ANzWnQF0Af5qwwSW0Q_rEY_xSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=lDphsEvka2ohHaV_6enCo4GovWbKu0wyF6miYZktfxurXUMx9IFLpLVjovk9aUtvMvCQtaxrSEmAETzdCotxkJK3QKNMKSpjiANtXAHKf1HMk9fo1S-hfBVDHqApuWDONUF64_Hh7yfDpEX5IYXzSihqmOHT13DTv9Dksq75eAE2AVPTRlFABPadbzdZrkAzrJJghwlqnA5nWW6GoJCh4o24y8FVIhr-a5h8loZlYKDDv4sz8SOqv0guyUXvIC9O4NU4TM0iS7wSpgHTiDMRTHijs_0XAI1kmrKwC39cwKULf8tLLvE3scwzYMy_ANzWnQF0Af5qwwSW0Q_rEY_xSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فوتبال‌فراتر از یک‌ورزش؛
بازیکنان‌آلمان برای دل گرمی دادن به‌حریف‌به‌سمت آنهارفتند و از تلاششان قدردانی کردند. کوراسائو باوجود شکست، اولین گل تاریخ خود درجام‌جهانی را به ثمر رساند و حضورش دراین‌رقابت‌ها را به یک دستاورد تاریخی تبدیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23502" target="_blank">📅 13:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5NeaYM8IdmQC6maqp-ksk_IxNhG2vjq31e7aeQEwe4MM6rEwN_MnBHiMscfskjeM6hzFfOiLPDWd0pyojSQ1nD_lWBy6g8-NNlz2cKwqqTJd3kPk3wZ5WGiADj_LMsafSQdwtPxykKRStDZaPJiWhkQdS1aYLJeDUmg0K9gRBOlgLJOYyh5scRrG_WIHVbJiyOK7MDLyVnR_bAQNXlcQXyn7llHafNx6F8XSZvjHm9tttxftx3KAzkv5wSuD_ruv5fTNkmg7NBctyrilH2AgS_T1erK8XjMFwArwKenc9WneKT1Sdars1Idtjun9p7FoitEUnWj-2GAdxYg1ul45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌بهانه‌عقدقرارداداحتمالی آموریم بامیلان یادی کنیم از این‌توییتر‌که نوشته:زنان باقاعدگی،بارداری و یائسگی دست و پنجه نرم می‌کنن، مردا چی؟ یکی از فن‌های یونایتد هم گفته: ترکیب 343 روبن آموریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23501" target="_blank">📅 13:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiXzznE1fpL3wJzvbmLW0nC7a8ldCYnyYd6myiy_Hg5-bxh0MTxPqNIlFrauD2k4qtmQX2xxliOZqKzh42P1d6nR7gkjeYsL99PgsXfYT-hPrqEYIRwF7mDwl2FgQf_yfiSzXc5Db8uBiEK8ALf0sH854ExwFHhMee3k7a9Kn-gSZwxGGZANJ3P9db1jgrZ2zw_WZQtmcxxjQ55XBTf7_ziJBw_iVcmBN6jkD7VnB6DRAo8YfmUcKvEBLBS7eMrwN-GB33OmDcKmUQhQ-hxht_7zM88IqN1rqD_S0ayjtAldOLpcdj57QnWNE1qQE0ROn8sVS-Nsw9EhGo_C5ZXqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا درسایت‌خود رسما اعلام‌کرده که تا به امروز 19 هزار نفر از زنان سه کشور میزبان باردار شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23500" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165e001c95.mp4?token=E5hrmKUp2fUwyrQ0HxOxLxCfpTDHgOhLLEs8L8iGxKRepwwmEyLqlcL_VqiMOFUt7qDDuKyU4aig0096tEhR4V-0RnWVR6yvFdhE1V2NG55hhfzD8_1rUIFs1x00uTaoI3WmiJ77dAePrrq-0f7W7DcI2_OjpiPeyVcBpSTvM6BckT351JSIcnEfiPR1DnhR0yEZTk7cSAWVU0A6A6ZY6dGqZT9P7QHCIi5BRXbybLk26V2JfNFAsFrezpYUr5FWconhBBc_uq_oUuw2TIfzei_2_sLGLx7z4MpPweFnwW94Jqb5I7dX-ie4AhKSwSbuH8cPzjeo3s90uw_DxNlbhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165e001c95.mp4?token=E5hrmKUp2fUwyrQ0HxOxLxCfpTDHgOhLLEs8L8iGxKRepwwmEyLqlcL_VqiMOFUt7qDDuKyU4aig0096tEhR4V-0RnWVR6yvFdhE1V2NG55hhfzD8_1rUIFs1x00uTaoI3WmiJ77dAePrrq-0f7W7DcI2_OjpiPeyVcBpSTvM6BckT351JSIcnEfiPR1DnhR0yEZTk7cSAWVU0A6A6ZY6dGqZT9P7QHCIi5BRXbybLk26V2JfNFAsFrezpYUr5FWconhBBc_uq_oUuw2TIfzei_2_sLGLx7z4MpPweFnwW94Jqb5I7dX-ie4AhKSwSbuH8cPzjeo3s90uw_DxNlbhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد سیانکی گزارشگر:
امیرمحمد رزاقی نیا هافبک ملی پوش تیم استقلال که الان مسافر جام جهانی شده رو من کشف کردم و به فوتبال اوردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23499" target="_blank">📅 13:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23498">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiMptdU8V5zlUkgSXJksqmJPUX_z5bBpaLiz04SF-0tL11oKrd5iIV5SwvNYEZQSZ10JiizI2Ljl7_IOCu1E9q35YwSWC26DFFRoo5Sa-XW7y-Izm7tt91K-PjWukvRauTPjv6iyKUjo2eDltMPoRI7pYUF4MYQvWPR6_ukyRfRNU30ezgbIesbSnxGWErTsiCtTDNcSoqGJ4bgz5qZC4-bAfJhOaXwsnRD7dnGefPWPzVg-fyePz8jQlvwWx09NNPS-g4pZeTtxoOyPc5r0IXyR5nx8YIQ2goi_nTuAmKWxfCkiY2df5eMsYxEXuBELxCoZyD2d00-G3iXC4xz4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات
|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23498" target="_blank">📅 12:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23497">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzYSzdE-HGEW835QaOCjtS3ZVh8B6sYMI1WxS23i6UPpgdi8_eG6gaZnFqx3oFgem2P973G4ZzIpWUaE39C-2So6te69T9UF7y54bow2ER6VEekhgc6WTocsjsOVD9JKOo59IrXe5b8wIwE9Txe-F0mQujxhE3W92TBsA6Y695FQai27hRuD2hRN32c8sqy89Ta1Rn4AOdEXLmXBPjTEH95Z1lKs6nqHzFiR3o6cRPecT3LQNdwPR1-FCE2rtRPHTKqt0OnHiqPgjqYGTVK2P_25r0vxopZw0NN09r1YY9_kBcxVlSsjoDo-UzjAMP4QsznsXUcaH0tWFGOf1PeONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این
نظرسنجی
که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23497" target="_blank">📅 12:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23496">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMSh_5YY1_g9nld-G_At3OFimWhCmDZzztzIBP7oBExg1UtT29SG8wm6PZb9yaZl1_wAF67yFs07z5UUVya4ViVGM8p1qaWLU5laZiC7MhrKYDG1WQg6ygixIwB2qHBW9YAaml0lZCO3KOarXBuxQH9GOcKGFY0vzYC0XsDWT_P4yfXfEe9A6aXH9KsmqSJq4bLhQ_59JwBDUvi-dJojxVcPHvsD3EWmdMclsIc2cG3rAfMHnK93h7bbqB8n1z3bBXB_kN8L0vIiMTpYkNxxrzZzUSgSXm44GEhOBMMKT9vffPRfs-dwhHYaAlHpbqSzoMiTwqVxug0Xo0k8HdV30Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23496" target="_blank">📅 12:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=Yg7ROPkkrx5VNP6Hf_r30M80xmn135dQpHkP9jZTUABbNHKzJUTLN8hNShzYSGY7mAQknA0GQm1471qQC5C28dXbI4SkPYee06dXS7wRcEiDOsxUx43Ju4s-HyphYPCp4varBFyEPbtt8_2QpIVluJlyQv8JAtbg5R69X51yZnZbU--5prEvnY0oJseYxKR_T8bjAXwXakDsXOrCGE-FO_V48HHbU8roZAfcT74qPBQu2214en1wNTipDPTlrYSeJRb7FUCGTQ15G5BpmSq_k6ePc5cyBipIsZJyceL1kHkNH49CYssN3k8JyI6CoM4VwQ4PFI4XpGmeSzAdzdKVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=Yg7ROPkkrx5VNP6Hf_r30M80xmn135dQpHkP9jZTUABbNHKzJUTLN8hNShzYSGY7mAQknA0GQm1471qQC5C28dXbI4SkPYee06dXS7wRcEiDOsxUx43Ju4s-HyphYPCp4varBFyEPbtt8_2QpIVluJlyQv8JAtbg5R69X51yZnZbU--5prEvnY0oJseYxKR_T8bjAXwXakDsXOrCGE-FO_V48HHbU8roZAfcT74qPBQu2214en1wNTipDPTlrYSeJRb7FUCGTQ15G5BpmSq_k6ePc5cyBipIsZJyceL1kHkNH49CYssN3k8JyI6CoM4VwQ4PFI4XpGmeSzAdzdKVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23495" target="_blank">📅 12:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJBhKyXbLOifQh-GVsms4J9SQfwn4WYpygfdr_vF82lpGhmjkazraz10B5q5Liz_UHb_ozMcxDmUHtYMlMR4hnh0uYqehveP1ubWw2GEAjaxTVKwieINDb1RtwRmtKgfS7O1EzMvgjw3z9C2GawDBTt4ZP_22WpmkSrFW9QGoQbXYI5TAPk50-Y_fFVO-oO-lElvuxvhRWO9C3HgJiWAXFHGEkbgDZJGrutN0oSZOUs4riujKa2Mn47PRv9c4dl3y2ver7ImpuYPlLb4N36vz3W6h3RxhTBpW47aexPtkx-3E5xysNvXvJ10KAj067cswr7xVyhF5I_n3cXS2UVqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اروپا هنوز راه شکست دادن ژاپن را پیدا نکرده! سامورایی‌های آبی ازسال ۲۰۱۹ تاکنون مقابل تیم‌های اروپایی شکست‌نخورده‌اند؛ از آلمان و اسپانیا گرفته تاانگلیس و هلند. بزودی تماس سرمربیان بزرگ تیم‌ های اروپایی با ژنرال برای آموزش راه شکست ژاپن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23494" target="_blank">📅 11:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At1v4saSa72CA1o4nI0Lb7mB97eBz9cJo8jkIhsHWdjKGTolEXmZcUBFALHUJZQifoDuk2_UbdQcLGSKJKvrNtzYnkjyt9ha0dU8iy_mmRVwHTtGexvAl-TwTD3MhTa84MjCKd6kiCe346C9WZuHodwKB5VSa9dxLuagrlf_3k4ywb4B2AxEPY86Gst-SRplUTUj9uzdBINj2Va0HQ68WlTq-cXyF1ta77mZRmZssFsl0KYVy7FxPqhRFLF5MwoDWLl7l20QhII3k5qU_YXndlJI8rUyQTwyS53dlIKPzaIyJZ5iW_tDpMdY9NW_AFqX1u2yotAh4eam2JuFf8SzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23493" target="_blank">📅 11:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23492">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up9gJmTezLUkLXhcI8-YGYVq-Zv7sAvGXc7u8yE3pfoLGN9Ma-rF31DZPjbMGayh1DyoA4SN7-KhOEh2dX0pGygU2fLy6fxOG6pRbnS_JccoQQqgiA5uYH7vwCSzERxWLRF5rhSziBdVuQhhmrjk7gHnHMU9Kv9oqI2FEPgTnmU8kjfzP30iDxW9uvPvotD5z6njyErFSbePUscp2pO3ZwOk88fwpCbhxoOZH13P_8fF5KMWslnCWhXfET-tAZldPdkFyL-EF96E88ODuvZH8GtgDFP6Ykam5Ug22F7USjk1qdKtoVehoGC2u1T9d6Q1IiwF6yozE4y3-qt39z6s2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23492" target="_blank">📅 10:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJAW_8dHFCusYuCWs9KnI18VWGvsf5Q7vlRlAN6YmPXTF4A1IC1O4Jl2ppTz1Kr8pEH450aWJv2jQiIq_UZItIV0UMzp1tOW80fSUVR41hCRGZAVgxhuTJbP0pSsRL7e3XJNEWCjBfaiYZy8cpH7q0Po-Rvhw89YYOVtNjFq_FtGG2Y276aqjGDQmDeetEvV4noBbmx8xrAggObg03X3scHGNaBqlEet_JklY80zYjz3PIHZjfO5p0qeEJXoFNbvxvvHs79-1SYDmkb4s2DhPoLRGwp72qxXxwBcxMvPuroqyp4WaGH2x3PMwYmlnnEGwRNNlswnmXcTizB55HG9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23491" target="_blank">📅 09:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0NIYBZLvYU2j8tJrZ2X0udiGacqXD75JI5SkaiE2TsvC-2SBdLO4e4KNrSr83yEK7CzOTzy_uY0wAwNStg24xONNnJ1ylU2gA-CMuCXfOVE9Mm5aCTOHiZKWAEnUZjHho47rHD-eadkdyR_-ckVffAPN7trdcgFRbm8XDRRolT2wJ1_-RyXPksISgxhFI8MZiWrPU8G3EQQTKY0C1pPPrwK44maFlnatADU1DSUoaIEgx8TJWjx7eINeSUX6WNEAFO-Rio45OST-FZzADwAuREQjoGEYEclTF9KH1xaao3nevs0FPhYeWr94jS4s-re9H6PvFPXH4m93L_k6Uou_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های پرشیانا؛ مدیر برنامه کسری طاهری فرداصبح‌و‌عصر بامدیریت دو تیم استقلال و پرسپولیس جلسه‌ای مهم برگزار خواهد کرد تا مقصد نهایی کسریِ 19 ساله برای فصل بعد مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23490" target="_blank">📅 09:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=hgBRY1_QgkW0Xg43LiqsMpFrX0H9t6SjEcZ19B2SLKjUEXzarjru1WKDtc-NAJhCtXs5dl85BG0EeC0LuD3Iv56oQopKc7ccfefjKDXYuli9qmpAKNAQxvAl2YA5VdLDF96zWK1Mn3uBc6F1oRVq01r1kHIPzWm4zZ2f4v86gT4X4QgMwRpwRZL6Drkw92x8A_mFeFGIGP7Uve9vlisNOK54hWthncd-MUIecaIesvjXuK1ynTFD5YsRQrNN_WYU2Xjz5ddV7Coc-o7j-q3gdYd5jtMcX0-GdjUbyIqTijPIQNaIarfi9vKnBkXI6iRjJSdOzN8Tny-yh4p6m5bi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=hgBRY1_QgkW0Xg43LiqsMpFrX0H9t6SjEcZ19B2SLKjUEXzarjru1WKDtc-NAJhCtXs5dl85BG0EeC0LuD3Iv56oQopKc7ccfefjKDXYuli9qmpAKNAQxvAl2YA5VdLDF96zWK1Mn3uBc6F1oRVq01r1kHIPzWm4zZ2f4v86gT4X4QgMwRpwRZL6Drkw92x8A_mFeFGIGP7Uve9vlisNOK54hWthncd-MUIecaIesvjXuK1ynTFD5YsRQrNN_WYU2Xjz5ddV7Coc-o7j-q3gdYd5jtMcX0-GdjUbyIqTijPIQNaIarfi9vKnBkXI6iRjJSdOzN8Tny-yh4p6m5bi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مهمون‌های ویژه بازی هفته نخست آمریکا مقابل پاراگوئه در رقابت‌های جام جهانی 2026 رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23489" target="_blank">📅 09:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=c7pBkVYuETb9vBX2979lrFw7MVAQfqfffhJngnmd_d2LMwBwvdNLC9QlIBpqE1Z3GWlc369VJKdiZnF3P686FSx2PERaxHAn9WQgbSAk4yACyb0lRY60cxotrojVJ_FUVzwLKtBuW3Kngse_Wc0rWl5SUpkW9ifcWiL-mZsIHSZ_kC33zCQpqj6mz2XSitQdc1dWLQuRDFGCviIBBr9MVwSf9nvOepcmVDBtDGVEdorvCbTAe-DQIy1DdNHuZ3Evk1h5W26Yq-i-5W_A-oebnMJBztIskwMhUYWfqWcqplEvqVhh5tLsSocsg2ukfuCvU3-5-wQbE99HHwjsb61_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=c7pBkVYuETb9vBX2979lrFw7MVAQfqfffhJngnmd_d2LMwBwvdNLC9QlIBpqE1Z3GWlc369VJKdiZnF3P686FSx2PERaxHAn9WQgbSAk4yACyb0lRY60cxotrojVJ_FUVzwLKtBuW3Kngse_Wc0rWl5SUpkW9ifcWiL-mZsIHSZ_kC33zCQpqj6mz2XSitQdc1dWLQuRDFGCviIBBr9MVwSf9nvOepcmVDBtDGVEdorvCbTAe-DQIy1DdNHuZ3Evk1h5W26Yq-i-5W_A-oebnMJBztIskwMhUYWfqWcqplEvqVhh5tLsSocsg2ukfuCvU3-5-wQbE99HHwjsb61_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛ سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23488" target="_blank">📅 09:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23486">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/To3u743TPWaQ8HmGZ54uV7tji_OKDUGzh83hLfJLqBCiuVqXwFZSjy-wRm51TpP9TlmqftpQYR7epl4sP6iO8tHJXsOTaSzVmT0PqF56EaLWlOygGPIV_nyhNEuduDHiWI-2stU1AZWso_WhMN5eUMqFXQi1tJ4nFzQxKQbBV7xSeYY0Jbl-0HaYc-s0sOOyaQe5jbNYQzL3I0nXS-MOt6cZlHpm96h0Z6pt6X_cKnCvFMYlhB1qrR07bEyzh0ayzxOumtK9f_B9n66ssw3wo3dD0Y8o7WFm9sTk-AVm1zXw-naLnmJH5mHF9utam2DmMP3_mzUrlQj9UIqUpLM0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LftCStE4p-YoFbDLew_x-WaxXnNUkEUOzPs65eNFGjE-L6YVOoc0Ethr9ce4fWhyL73a3JtIY-qhdFw2bTBQ_VBlqtL3Ckgvmhm-RpfKqHww2yVon1idLb3wIZTvh8QeuxCy61Jk0KPhc2awrihMEyqq5FQq1I9tK5smm7Zf4FeFk0g2KoIN0w4H8vGGt9VmPootf4s5Gk2ve-vZzPaNpZX_5WiTwFDG9uSkXmhyRjEK1Mw1KfB3fmJN00d3e3kcgBQCRc98_rZQkFfScmqCVLqmKqmEDJ2b6EwVa6Ohmd2twalMS3ExEUgh09gXzmL1Z5GFCLSKgIXAuq7k507NGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23486" target="_blank">📅 09:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGJ4No556JsjFFdPDZ91nMBtP-vE7uycffZkbS7No2g9Kw8y_bsdzAZeVfuTT5NVwslgTsVI2L4vz38VUmW0r5cbmljJ3a206lBn-X4VExrWFgOnaMvOHVmwdTxQ-fyXidzkROjPsRLYFQdNkUV5He1pGYROjkSRkSMGIO4Fmtuppjh94k779S1y2s2sP5652xlBaMUCcvIwE3QBUpyhlDhk5u-ImByYOGL6SGNE-9rNZPZRpl8yAVZdhd6j3XsJztpJ4_U1HD8N-uGVT92gRdNYraxmxiVapDe1HgxhBVIW5mV1xp1KCyOnc2kVu5YBWj5kBtB_bp6z_B9GoYYxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌چهارم‌لیگ‌ملت‌های‌والیبال؛ کامل شاگردان روبرتو پیاتزا کامل نشد؛ سومین شکست ایرانی‌ها در لیگ ملت‌های والیبال در چهارمین بازی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23484" target="_blank">📅 03:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7hk5UirVzuOXubxtjCiyf-vv8VlqM8SPkUTO1BiWcrbOlwNjfy5QG_guqQopTwF5BoXPYjVkvyDQiBlY4xv0TLO_opzuABvEyqSU3Scv4GhdvFIrqiWyQTt_JPoHXw-2Of6fJmWMQFi3FY400UBzRO1QTXpWbCxohxDmx6GCgpWzm8IwUBMuCKBO2ZICjuUdsU9TQQEBQEf0w_-fpVoxHonhNDFVlFZp3wJCSbO5QceXuaVKcfoUx0l7TWbznfIlrWWiuUHK2tIHqqFwlPw1tlH1uW4ut5Fj5YJw1MsMShcxoaeNTxGhnPcpvYOguu-j2NH45Vrbo5zWnTAQ5NECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نماینده انزو فرناندز به سران رئال اعلام کرده که این ستاره آرژانتینی بسیار علاقمند به پیوستن به‌این‌تیمه و حتی‌حاضره دستمزدش کاهش دهد تا بعد جام جهانی شاگرد مورینیو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23483" target="_blank">📅 02:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HT7KAa5bWExuVS7mkBxZ-jNScvQyRwEF9LOO8hGPgLlnDW2YfEzXf02RXH9PI6JIA4U3sydtUWEm6-gGCin0DoWHqpvQ6eFgs1vAfQpfdKeRntcomy_2AAP0aIV8m9N53aMSRzRk_LdQ2XTxpUVLaCDWJEfNqanlRIz3l-8Nv_O4XgzkR2mhimdZWf1xXQOAgjC3L4PYeWErOQKZHm1PC6ryMwA0wWVNsHcFFMrKfWmILCTzOE6gBG2hRVLrfFD87lpsN8Sj5aytKvQow51-q_NQM2JQV5xQUfNd2arq4Sty03Ea3totWaFEIPiU8t2S2QobUbs8Oe_yIAjVhwon9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23482" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0McUwnTLTtOROlCtXNch_q1T_hWbbGSrI8rq3TmGghmD0PFaQv1p-3sVF0jNZjl97QzQCBiUHZlD-0pc5IRpT_-Is5-vY7mg19Lp_-y-Jhz41eYGZ3-FbdovvVtQ9MmXNJK7VndmosTbCUxDHVgsQlORlPlOjqZg5KgA75Z8ZJK2vYYT3ueI_Ma1Z6i7AnMCNwFizpGMBXvCZ5tXVWGsfT3ItpBW61w8cKdNFbvMYJvkc2ydoQJUovTpYgsA6XxkxcrRw52oRYXg3rES6hPz5Wj8i56NW2dEQD9z4i4CWGivkTCru8spB_y-lY-EB2OdEx9vRCyETDws9v9y2uLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23481" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBlSDDSGfk2fyK9sSdEZ6U48UbFw4IkL5nXBfjBbmh6EKHh-DB95RrT7DP5T1IBHKH5L85SHwROrThjK3lPLJ8wLBJhXKD6HElv0Jejze1IiAs3Hlq9Ng3JwngrkvwNzCerIiW_n65sGKQYnXF-4IqtFPVHOV-Jzia-I9M6ZFSgYEJVEVEAGZ9JUYvBqXx7X2K_rMshvk3I4t8cRy4RP8Th5S8-KZR5EyGu9MH287wsKvvejPsdDH1BYkaBK_qt5ujGCgZt25wwrJT2dMGGReY0wwbFSluqNDJ7j9ZLYsje7cltE-8DFsXjBFrRV0ttLAddS6wLRz_5_rvZYpXoVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌جشنواره‌گل‌ژرمن‌ها درشب دبل هاورتز و تقسیم‌امتیازات درجدال هلند
🆚
ژاپن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23480" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
