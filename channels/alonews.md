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
<img src="https://cdn4.telesco.pe/file/kF-7X85kdkktmzHvQFspvR44Z0S0k0TotNH7CzwYqCxATVyV4Kwb6fOpXRsUBP_XW7CAtAGbhAiwSPsO3nGoI3_UsT1qPd7bVfY3YI8zaIX1oZWW-_jli1gWptMDMANW7mDWIkT6mxDuKM4PHX3hVXIQMhhNenrG5WBl0bH05-IuF85aHfHpjY2_0imotGtiafLzPoGFHNImvuPK78DkNyD799dTdZkw0Hx4_oSe0ZHdOtRmnQeViFPol6omDlZYwqsUkNslR1Wv7uOOkh46EgREbLEuorSvS0SiPxBdGqugvg9g8A-x09ZfgcmcJS_QKEP9MW7RBdYUMU5S7pap5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 983K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 23:32:41</div>
<hr>

<div class="tg-post" id="msg-140107">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یدیعوت آحارانوت: نتانیاهو امشب جلسه‌ای امنیتی برگزار خواهد کرد که به بررسی واکنش به تلفات اخیر ارتش اختصاص خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/140107" target="_blank">📅 23:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140106">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2ebd2079.mp4?token=CxgwxlToUiPCnyQWA1MdnRImEtT_4uz6dPJfNpUUKVXQ5RRYd9BfasTDmiDkWdAJLWL2pfrkVJt8Hs4vnsBF_iBJoLb5LQaQgrgKJ3M28hWnLsSTn-Qm1FiECZ4Zl9x4KgIV5YI90glwJ1YafiaKygjrCnsILpaUpCgphb3UHRGgigPzH1BYUX9km9zHeLr1X2LcEK2EJyJIK8EvNLXvsnW9kyTn1SNaPr9hu9-9IHLYipaRzjZpQWiAxxfKWjgJJ-jmKjYQ8td4yzqQ-3vYl3kNN6sSBNNM4ZhTgdCt8h6DAm3VSIOXqFZJrlzc9ancQ0VVISRt7ewq9yvdgGHnKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2ebd2079.mp4?token=CxgwxlToUiPCnyQWA1MdnRImEtT_4uz6dPJfNpUUKVXQ5RRYd9BfasTDmiDkWdAJLWL2pfrkVJt8Hs4vnsBF_iBJoLb5LQaQgrgKJ3M28hWnLsSTn-Qm1FiECZ4Zl9x4KgIV5YI90glwJ1YafiaKygjrCnsILpaUpCgphb3UHRGgigPzH1BYUX9km9zHeLr1X2LcEK2EJyJIK8EvNLXvsnW9kyTn1SNaPr9hu9-9IHLYipaRzjZpQWiAxxfKWjgJJ-jmKjYQ8td4yzqQ-3vYl3kNN6sSBNNM4ZhTgdCt8h6DAm3VSIOXqFZJrlzc9ancQ0VVISRt7ewq9yvdgGHnKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات توپخانه‌ای ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/140106" target="_blank">📅 23:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140105">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqQ5uuDI145cAA2xLPT1HiMX1D_kWb41u0_a3jmDaXUSjUGj7ReU3H0ePs3BoZUO1_1t5UE3Dsh3wDx1DqbF9TI5IphoxcXZ_Y-np439XCshzQ1DkC4NbpmMi4wPdYP1dOGDRgVF1CHOagryq6b_N0fj8h4w1W8jw51PJMGpI-ukKAsDmmDlhSnlMp-qgCiqPmGnHXYUH2v2BTxngjK8vVEL3Thl-KlFzja1alEnQ5OY1BXWwEr5dzecteeERYnNAxIK0s71mEd-WrdRMBDmDrSxb5fHYqbXOELOKS73RnN9o8D2vfUUGYT_aYC4EFwxK7HX606nyw872ZqMCxMKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکسی که حساب کاربری وزارت خارجه ایران در بوسنی پست کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/140105" target="_blank">📅 23:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140102">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef0d6c980.mp4?token=qy01gPrHqmBvBmFu6MfDcBVUSqEtdTk_KhNgN9FgvkNSPbmoaEIXNmePvYt5bLo2bjS_Uod2YyW1wDVLxvGSNRSU0dLfvBPdRylUo4O-woCr-indJTJMMe-tSH1dmchTsYTHanSmEmwqpjAniKvXx0dv6gf0kQifQncJMEShjhqQaSGW3KqRLGfZ68iatDgZJ1SZVZ0vKA22SsTofaMnHsXxHna_FZJzRIWT9XxwsaDbLMefc8Jb07e-M0TN2ezlf5RFSqX-RXYx-70bVpJQFiPfHNIJL8k89n4RC8QztDzJTde6NYkl6DOJUl8Nwgv7DyD0QFGvORJIfrbqKbxFNQuOHu1CyQV90MPMQr5HME1_w-GLmOprpJxlPfNxSOECPn7n_FDoZYGe5LM_ogmIWmPWR6Fy0pYM1PNrrNvEcJY99gP1rBsu7m5X9ML9LbTMwDepKiRT85yU0QbuVBnhz9jzIjRRpMi2ho2JjLqxq2_PAedgacFJb8rjP0OBNimWiYR2Xx9HU61OvhFKKT5Oi0G9WP_ZtCQ2869L4I1bJNmL4YHA8EPyDY42yfqFElm8nWfMptaoehid6JJRcF1mQ6JMTsqunxpm1Fw2UrZ2Z4FjkV7O10yKPB3byQeRNQRqgx3WcUbZA4kAUohJMCPDFDyjhcN30rAddXfua2qeWXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef0d6c980.mp4?token=qy01gPrHqmBvBmFu6MfDcBVUSqEtdTk_KhNgN9FgvkNSPbmoaEIXNmePvYt5bLo2bjS_Uod2YyW1wDVLxvGSNRSU0dLfvBPdRylUo4O-woCr-indJTJMMe-tSH1dmchTsYTHanSmEmwqpjAniKvXx0dv6gf0kQifQncJMEShjhqQaSGW3KqRLGfZ68iatDgZJ1SZVZ0vKA22SsTofaMnHsXxHna_FZJzRIWT9XxwsaDbLMefc8Jb07e-M0TN2ezlf5RFSqX-RXYx-70bVpJQFiPfHNIJL8k89n4RC8QztDzJTde6NYkl6DOJUl8Nwgv7DyD0QFGvORJIfrbqKbxFNQuOHu1CyQV90MPMQr5HME1_w-GLmOprpJxlPfNxSOECPn7n_FDoZYGe5LM_ogmIWmPWR6Fy0pYM1PNrrNvEcJY99gP1rBsu7m5X9ML9LbTMwDepKiRT85yU0QbuVBnhz9jzIjRRpMi2ho2JjLqxq2_PAedgacFJb8rjP0OBNimWiYR2Xx9HU61OvhFKKT5Oi0G9WP_ZtCQ2869L4I1bJNmL4YHA8EPyDY42yfqFElm8nWfMptaoehid6JJRcF1mQ6JMTsqunxpm1Fw2UrZ2Z4FjkV7O10yKPB3byQeRNQRqgx3WcUbZA4kAUohJMCPDFDyjhcN30rAddXfua2qeWXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پالایشگاه نفت اوفا در منطقه باشکورتوستان روسیه، مورد حمله پهپادها قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/140102" target="_blank">📅 23:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140101">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزارت نفت، نهاد ریاست جمهوری را به پرداخت ۱۳۸.۰۰۰.۰۰۰.۰۰۰.۰۰۰ تومان خسارت محکوم کرد!
🔴
در‌ یکی از کم‌سابقه‌ترین‌ دعواهای حقوقی در دولت بر سر اجرای اصل ۴۴، شرکت سرمایه‌گذاری اهداف زیر مجموعه وزارت نفت، نهاد ریاست جمهوری را به پرداخت ۱۳۸ هزار و ۵۶۰ میلیارد تومان خسارت محکوم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/140101" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140100">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزیر انرژی ترکیه: ظرفیت مسیر نفتی جایگزین تنگه هرمز را به ۲.۵ میلیون بشکه در روز می‌رسانیم
🔴
وزیر انرژی ترکیه با اشاره به بحران عبور و مرور کشتی‌ها از تنگهٔ هرمز گفت تحولات ماه‌های اخیر نشان داده است که جهان به مسیرهای جایگزین برای انتقال نفت نیاز دارد و آنکارا در حال مذاکره با عراق برای توسعه مسیرهای جدید صادرات انرژی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/140100" target="_blank">📅 23:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140099">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwZSzzeY_343FPb53uKCjeCdEq89AhfGNvELcPvq4y856KT2RvEQCmA-EthmmFEUpezqJXPUphojz9EJqtpCTGG7wD-6cNkEw5iBAiUiXN3QBr9dA9dbobE7C_U2fRG8F92HqBi5Qzb2d0iqA506--KDiHwgvg7CIzg418XaO6JONNqSo-8Pw3FUQVBr9FvUQibgMEU4cOa1F9IBtNUKko6WC5F6jivqnZXPJ6MCd6rKO6SNr5sYwL09gQgpmu-vP4espRlZiheQYkBJCRZT2OvvcXVjiZKHmTNF-3ocsU847o5Wv3cjwA32WBN-rxJiYLiyMLmBM-K1DPa-xi8iKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کمیته مالی کنست اسرائیل نقل و انتقالات بودجه ای را تصویب کرد که بودجه سال 2026 وزارت شهرک سازی و ماموریت های ملی را به رکورد 242 میلیون دلار رساند و سیاست دولت را برای گسترش شهرک سازی های اسرائیل در کرانه باختری اشغالی تقویت کرد.
🔴
دیوان عالی دادگستری اسرائیل در 5 اوت به طور موقت انتقالات مورد مناقشه را متوقف کرد تا در مورد اینکه آیا کمیته به طور قانونی در طول تعطیلات انتخابات تشکیل شده است یا خیر.
🔴
منبع: تایمز اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/140099" target="_blank">📅 22:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140098">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پزشکیان درباره دمای اتاق مصاحبه:
من زابل خدمت کردم، پنکه هم نداشتم، دیگه چی میگی؟ چندتا از کولرا خاموش کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/140098" target="_blank">📅 22:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140097">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایالات متحده شامگاه چهارشنبه اعلام کرد مارکو روبیو، وزیر امور خارجه آمریکا امروز با اد میلیبند، وزیر امور خارجه بریتانیا دیدار کرد.
🔴
وزرای امور خارجه ایالات متحده و بریتانیا درباره تعهد مشترکشان به حمل‌ونقل امن در تنگه هرمز و برنامه هسته‌ای ایران گفت‌وگو و رایزنی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/140097" target="_blank">📅 22:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140096">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
پزشکیان: ۲۰ درصد صرفه جویی در انرژی معادل ۱ میلیون و ۸۰۰ هزار بشکه نفت است. کل صادرات ما ۱ میلیون و ۶۰۰ هزار بشکه است. اگر ۲۰ درصد صرفه جویی کنیم کل مشکلات ما حل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/140096" target="_blank">📅 22:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140095">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b349f9bd3.mp4?token=AiTyUgRMIYt6Ibs0mdXMRu_6xfzfScAt0Ji5kmjFKmM6YNZAapA2CKKu2qFxt5R82uXPsAWqiEu7EMun2rUl0Cz_cdOsVwqmsU2XXUa3K0-rq9sgV08wraK2CYElHjkXt0l_liXHn-WvRwq5k8ap41sR8Hr_NzqjQa5HKOaiH9PovU5PwIRLkCX6YpaxdEcBSofnbWxYGu0gU9V9U5TOjUjogcJqTXyk1MwGgKIOekWtWbT0xKGcv4a_iv5WJk1AsqwlNy3eOlpR8vEGqPKYTkwNBH4CxO2qTPnRBuo68fjYi5z3GwWbLYLipig3q_hut8kKqfcHJdbb0We7cRTvTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b349f9bd3.mp4?token=AiTyUgRMIYt6Ibs0mdXMRu_6xfzfScAt0Ji5kmjFKmM6YNZAapA2CKKu2qFxt5R82uXPsAWqiEu7EMun2rUl0Cz_cdOsVwqmsU2XXUa3K0-rq9sgV08wraK2CYElHjkXt0l_liXHn-WvRwq5k8ap41sR8Hr_NzqjQa5HKOaiH9PovU5PwIRLkCX6YpaxdEcBSofnbWxYGu0gU9V9U5TOjUjogcJqTXyk1MwGgKIOekWtWbT0xKGcv4a_iv5WJk1AsqwlNy3eOlpR8vEGqPKYTkwNBH4CxO2qTPnRBuo68fjYi5z3GwWbLYLipig3q_hut8kKqfcHJdbb0We7cRTvTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: هر چقدر که فکر می‌کنم، نمی‌توانم هیچ دلیل منطقی برای این پیدا کنم که چرا رهبر ما، فرماندهان ما و دانشمندان ما را کشتند.
🔴
بسیاری از فرماندهان و دانشمندانی که کشته شدند، حتی خانه‌ای هم نداشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/140095" target="_blank">📅 22:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140094">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس‌جمهور مسعود پزشکیان: رهبر پیشین انقلاب توافق کردند که ایرانیان مقیم خارج در صورت بازگشت با هیچ مشکلی مواجه نشوند.
🔴
حتی اگر کسی مشکلی داشته باشد، باید به او گفته شود که بازگردد، نه اینکه هنگام ورود به اینجا دستگیر شود.
🔴
ایران خانه هر ایرانی محسوب می‌شود و برنامه این بود که مکانیزمی ایجاد شود تا هر ایرانی بتواند آزادانه به کشور سفر کند و از آن خارج شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/140094" target="_blank">📅 22:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140093">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پزشکیان: کسایی که ‌که کشته‌شدگان دی ماه پارسال را ۳۰-۴۰ هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140093" target="_blank">📅 22:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140092">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن:
ما نفتکش سعودی «دیزی» را در خلیج عدن با موشک بالستیک زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140092" target="_blank">📅 22:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140091">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd906c65a.mp4?token=EKxD8tNZa46lRRaakTvMEefd-0kdX8aTK7A6w7BzRwfTU86i8dFjQU3A4fRQOloeo3yJLX1gQDCUNWSCTsHhaYsiKARYmkAO9Ff3XVU9LMmiG1d-thdgIvYx2NzdOGvcMrHLJt2noAKqKaIHfAz5GaAR5oYk_PKK2MwLIJlaNy7vQOvREvi4SKE7z9ie1PSVyNB4hKJ-9Fg4VOruuxwZUCZzWSdsZLE3o-2DMh6pfy1gD0CmajJe_fCPy4pImsrHRIlLJuFIvYUaf_Sa6YyiHaiaHysWQ7yeRt22T-ZY19d0der17fIKS2MXbPhEFAA9K0P-2Ansu-gqpo1PwiaZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd906c65a.mp4?token=EKxD8tNZa46lRRaakTvMEefd-0kdX8aTK7A6w7BzRwfTU86i8dFjQU3A4fRQOloeo3yJLX1gQDCUNWSCTsHhaYsiKARYmkAO9Ff3XVU9LMmiG1d-thdgIvYx2NzdOGvcMrHLJt2noAKqKaIHfAz5GaAR5oYk_PKK2MwLIJlaNy7vQOvREvi4SKE7z9ie1PSVyNB4hKJ-9Fg4VOruuxwZUCZzWSdsZLE3o-2DMh6pfy1gD0CmajJe_fCPy4pImsrHRIlLJuFIvYUaf_Sa6YyiHaiaHysWQ7yeRt22T-ZY19d0der17fIKS2MXbPhEFAA9K0P-2Ansu-gqpo1PwiaZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پزشکیان: نقشه کشیده بودند ایران را ۴۸ ساعته مثل سوریه بگیرند
‏
🔴
شهادت بزرگان ما در جنگ رمضان دردناک بود؛ با همه سختی‌ها و مشکلات امروز از ایران به عنوان یک کشور قدرتمند و با عزت بالا نام برده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140091" target="_blank">📅 22:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140089">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3ef09d2f1.mp4?token=aP-CZ4eeXnPxPW9Yvy8YiL0PYB7tN9EK5cs2djS1lRS7RtZZm4jx55ylsl2VrV961i1nm-sHr5wQec2D9nt4qI0EtlBBer6Nhv_UX4PVvbdhIGtfwQKXOIBFCoxcWFiGXBR9IVeMSgQFO2cEaywjhjotdSSznVgohrb5IS7rx6FZsK7ZOiAN_A6bZbMmNj_NkyeyYJSTxcK_Yt6CQFwQ3hr7gVxTSeFCeLTTyhkZdui-Uc_Tf6yDwShUGj6vWbbch2spoDVSwIPqr7qdR-YUIAokiRlq-bB_P1lj9ddYQjT2pLVhw6IEvMC0lEx7rDcVECCZnjkLG49mKdOKeNdARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3ef09d2f1.mp4?token=aP-CZ4eeXnPxPW9Yvy8YiL0PYB7tN9EK5cs2djS1lRS7RtZZm4jx55ylsl2VrV961i1nm-sHr5wQec2D9nt4qI0EtlBBer6Nhv_UX4PVvbdhIGtfwQKXOIBFCoxcWFiGXBR9IVeMSgQFO2cEaywjhjotdSSznVgohrb5IS7rx6FZsK7ZOiAN_A6bZbMmNj_NkyeyYJSTxcK_Yt6CQFwQ3hr7gVxTSeFCeLTTyhkZdui-Uc_Tf6yDwShUGj6vWbbch2spoDVSwIPqr7qdR-YUIAokiRlq-bB_P1lj9ddYQjT2pLVhw6IEvMC0lEx7rDcVECCZnjkLG49mKdOKeNdARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: امکان ارتباط با رهبری سخت است!
🔴
رهبر انقلاب در مورد تفاهم، نظر کارشناسی را پذیرفتند؛ ایشان گفته بودند که اگر سه‌چهارم رای بیاورد آن را می‌پذیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140089" target="_blank">📅 22:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140088">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZCCA2hFLqaoxer4pn81EV5-FdgnsoQ34jdzr1FoXU8tHRlU7ifVbLyxkL0wZWLtqBKUd2RLDh-mdepYLMkD2iG2yTmoJRQsEoknZFGXBqKfc_hJofZ7MHQQijUBKgg9RPFF1MCAHadqvQ7JyvGH7jMLfwoGf388B_tz0PY_8DE6n1qseuBTN4elyQ0ZCN0mt2-RwtUu9wOtW2RIQyVSMNGBSaBB6NYuba9WB6BjoFEBs9Gtonu58RIyKuV8_AV-4Nnm2LT5h_ej6JZLOf8k7nszL3sc-SsFtJ765gxBkvmhNOZz1drOF2IDIFIZKpbLFE6s1vDvumdn9eIgvQYDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: و اعتصموا بحبل الله جمیعا و لا تفرقوا و اذکروا نعمت الله علیکم اذ کنتم اعداء فالف بین قلوبکم فاصبحتم بنعمته اخوانا و کنتم علی شفا حفرة من النار فانقذکم منها کذلک یبین الله لکم آیاته لعلکم تهتدون
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/140088" target="_blank">📅 22:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140087">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پزشکیان: مردم همه کسانی هستند که در این مملکت زندگی می‌کنند، مستقل از عقیده، باور، دیدگاه، جنسیت و قومیت و حاکمیت وظیفه دارد بر اساس عدالت با مردم برخورد کند.
🔴
در این مدت تمام تلاش دشمن این بوده است که ما را از هم بپاشند و تفرقه ایجاد کنند و اگر تا حالا مانده‌ایم، همه مردم نجیب ایران را نگه داشته‌اند، نه فقط آنهایی که در خیابان بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140087" target="_blank">📅 22:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140086">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4569f98205.mp4?token=RoLEuxcr93FwJVgWWnWNBzSltsTWXTnnkk5iaGMJ0aBp6fRL5ICelu1vg9K5PS0VKXdU1mld1e4r0GFNWxYOjgs1XpuK_mTBUQcbMBMyRWyRIe07UKwgo84tq7k1wFyIebdQrOwI_cm70osKPlgD3P_yyW3AZXHHBMWt1leqAsSF7MZLzXI_kP4cnar7x80hB1ZzSgN0GDYGyCWwmcJ-jLBJtS1QRdnx2pAONeBwlQJ8FBkUddoodAjHSYDpTLGYdHn8vFcGji22HpKuvQ02yX-bWHhcfcFSj0HsLGO6zUZ2P4jPMjFk7KfwDp8RbJswdnC8dGJ62m976eWpqgV9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4569f98205.mp4?token=RoLEuxcr93FwJVgWWnWNBzSltsTWXTnnkk5iaGMJ0aBp6fRL5ICelu1vg9K5PS0VKXdU1mld1e4r0GFNWxYOjgs1XpuK_mTBUQcbMBMyRWyRIe07UKwgo84tq7k1wFyIebdQrOwI_cm70osKPlgD3P_yyW3AZXHHBMWt1leqAsSF7MZLzXI_kP4cnar7x80hB1ZzSgN0GDYGyCWwmcJ-jLBJtS1QRdnx2pAONeBwlQJ8FBkUddoodAjHSYDpTLGYdHn8vFcGji22HpKuvQ02yX-bWHhcfcFSj0HsLGO6zUZ2P4jPMjFk7KfwDp8RbJswdnC8dGJ62m976eWpqgV9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلیپی پربازدید از محبوبیت فوق العاده بطل در رسانه‌های عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140086" target="_blank">📅 22:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140082">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfdvJD2Al6dz8IIBlx5q2Y-aQRWup269E6FQ22wKhIUsx0vPOqi7BlZqsm5APhJArEWZ2L-oUgWckzECBMe-Fim1yaSuNGiHIrEG7OZYP7iSs3Rvg_OCXIGX56B8w35oAwL1YAnN3dhIZaT_hTYHGEttYF8ylPVpiaeI9YUjRHk1lze1fIKKbQQ58hTehnWzXpRnh7lCb_I6tWPv-fqt3CbUXLw9os3JRDjiwbWmpXeVMuupptqcPK30K1a2a2SUTgSTg73jAM0KroyXLuhu5prs_puaZffQvEO7rd2TCt09xnbqVPmnYIyCXfohICBDOhCq9ApSHKKctIDaCjRXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hveHRFVIY6DqlFpB6ntry46866Mk2cyc-YXYobt3hpLcdtDlPxktPq0s1dDZ2kSorpOem06AfHhnbksZN_z7hoXyVkIgr8JDntknUoq--d8M9R54WZr4gXpabJGR5S4jxUOOEzHOk_TRexyOVC9XZqyBDaYPq9lG2L7kTy53Ot0cBvLDZY68HL4B8Do5kVSgyNBTLv8Hdz8YogOidn8pTBobNj_NRskJ8lW2jo0VX-t76VO8gEeKkcmKtF06ywAanm9n2uZjTM33aChKqqF8EsfKY78H7f3Z7NLxihX0qNXQltk0X7efY6k9OOpNOWA5NcGavwE9VzfuVbeycH__Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H79bs5VITfSOOlQyL6auqouhy28bujDdpD18Xpw7LOU_IOEEsqSAJo_GSr9nQzMZXMZ4Yy0VFDmcPFNBSJCKJWT_F0LmKMgXKi1rf3IuUBORHqr4UXvuFuFGn33Myx0HbAFtOHnSLTg-U2DqnauYhi6IyBgBP8w3n5kGDwluWFIsSAOmfpIwbpdeT6YFcFKmi5l66d0Xs-xmcJhOD-ARuJ6MjdevYeN3J6iOXmnPJQIRv9ntPAHlUmvQ91nXvqVn09IF_1fAa2WwemhDKDWTJKgJd7_KVTm0bULf-Gmi5HLz2UWOH0tjyB2SJLri4YsW7cfEVrCdYi21CYQu8xNsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Km4hBSGxn0V7O2nT6Fwhsy52sb55Em-K0k2eGSSUD7qHad0e6FjtSgVceeL_4PdYlXfNO1mN-yx2kiSkBEHCadjl1mAgYIuLtcUyjqsp2Ggsaf-GcZmRLw_zfw6x6Z-k-3v2okjLkYpMdoFmqWY0q7T-y5fCbvasTKjXT6V4l8mwVGTxKGFHQbdMgHmSqoki6fEayyU2x3WhMrmKlzNKt8U9lIwPgnmffHIMqCX0ns6maufMmHjdBVRJUJ2oYipP8ri8ipEVyviY92RpaVkxPzkM2ANBVoDEvdexsw1_jNlyzBrLxyVIgnhJp2ijMFs52pVv9l9uAE2nHnd_MhrAjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از رزمایش تیپ ۲۵ تکاور، یکی از یگان‌های ویژه نیروی زمینی ارتش برای مقابله با لشکر ۱۰۱ و لشکر ۸۲ آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140082" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140081">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d191963b9.mp4?token=ai18bSI4IAcLVl3iDNJAWxjyINxOhfkF8V-KPfR0mXrbI0Jgg5lcALei-deb5A23Zj44vjXSIKQ7avmuR5J1yt55qBcfCrDC_9HXwvzyDJChGUbw2gHEYEBGw3nbzL0tyyeJgsPFwLV-kgeWFkOrJRLdLYKk90E3ygwzqQWAXwDFit-hRmRZPLZoUnYXzdvwmbMs4udqCwGmokF_cZliNYF3Q7ybZcwePCzjlOJ8jBv0H1BscPdlbX-m9f35H5GwPdIEPhxqnJ7_ZK9W_HyLkrUvgpdG--QqUB9WUqqFn1oZ5wnz9SAiD68XM0avCLLwXZbg0CWj5MBzo0hwp6adgJJKAdrhcf775UewiWUdYUL97z2lmPxz5JL5wgZRvq8ra5OWsh5qQIqLFNZmcDvvp5Z2Y6wknSazjchPreMhXFwQckc8lmEYZdVU-P9o3RBQ-Yz95AIp-NJMs9iTkWFlSSqPJafSf7n15JMZOgF2WEJJ9cVNLDnnkuplnSzkUSic0wrgxMJ72hViF-neuXU7W1umxZXFPql1AfycFBFbk-NhBFDF89a90D_HZXnqVf8UqDjM4GeIMxN4C8dTIamImG4t7pFNCs7I6b1g3PYYD_6nRpShsUCXUVNOnUjAse6yhUK-NXnxNvaltC3jReWK3K-6VJuh_1QbFhslqrBkNPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d191963b9.mp4?token=ai18bSI4IAcLVl3iDNJAWxjyINxOhfkF8V-KPfR0mXrbI0Jgg5lcALei-deb5A23Zj44vjXSIKQ7avmuR5J1yt55qBcfCrDC_9HXwvzyDJChGUbw2gHEYEBGw3nbzL0tyyeJgsPFwLV-kgeWFkOrJRLdLYKk90E3ygwzqQWAXwDFit-hRmRZPLZoUnYXzdvwmbMs4udqCwGmokF_cZliNYF3Q7ybZcwePCzjlOJ8jBv0H1BscPdlbX-m9f35H5GwPdIEPhxqnJ7_ZK9W_HyLkrUvgpdG--QqUB9WUqqFn1oZ5wnz9SAiD68XM0avCLLwXZbg0CWj5MBzo0hwp6adgJJKAdrhcf775UewiWUdYUL97z2lmPxz5JL5wgZRvq8ra5OWsh5qQIqLFNZmcDvvp5Z2Y6wknSazjchPreMhXFwQckc8lmEYZdVU-P9o3RBQ-Yz95AIp-NJMs9iTkWFlSSqPJafSf7n15JMZOgF2WEJJ9cVNLDnnkuplnSzkUSic0wrgxMJ72hViF-neuXU7W1umxZXFPql1AfycFBFbk-NhBFDF89a90D_HZXnqVf8UqDjM4GeIMxN4C8dTIamImG4t7pFNCs7I6b1g3PYYD_6nRpShsUCXUVNOnUjAse6yhUK-NXnxNvaltC3jReWK3K-6VJuh_1QbFhslqrBkNPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه عربستان: اورشلیم، شهری که در قلب میلیون‌ها مسلمان، مسیحی و یهودی جایگاه ویژه‌ای دارد، باید شهری صلح و همزیستی باشد، نه میدانی برای درگیری یا تحمیل یک واقعیت تحمیل‌شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140081" target="_blank">📅 22:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140080">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یک هواپیمای ویژه ارتش آمریکا وارد ریاض شد،
🔴
گزارش ها از ورود مقامات ارشد نظامی آمریکایی به صورت ناگهانی به عربستان سعودی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140080" target="_blank">📅 21:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140079">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahlJ2VgcFh_wPH_zRBx8mTz14gr6WIrO6gZZUitr4G3pGKg5UI-vT8FEvdB4Z2ovhGaHJLj3KPPB-vJmQYk4h0cY5PnWJT1djNWc-dGL3Ly0E_ewsxz9FJYIRcfvcza4tGNMTR4d5ogFnx7Ptbq9SZ7arsIIqqnHGsBl_hNCzk7txKd80OkvwF-tRY2f9lz8JjPngnWfJD5zsh8yKVxgDrd4eFkPwzxhkyukltd-f4YNMLHC4aW6MZNpYAdNv3XCGIR47MS_j6PGO8bZfaykdRurDB1-3BMj2ZV3FJDNVmfDT7-sOLwB9BXqmQyqYP0k1EAXY4xtRqVFTjyETbm2oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست عجیب نوید محمد زاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140079" target="_blank">📅 21:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بنیامین نتانیاهو: سربازان نیروهای دفاعی اسرائیل شجاع‌ترین، بااخلاق‌ترین و در عین حال مورد تهمت‌ترین سربازان روی زمین هستند.
🔴
نباید اجازه داد اتهامات دروغین که از خارج از کشور می‌آیند، در جامعه خودمان گسترش یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140078" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2acbb794f.mp4?token=Zt9H5Np0C4U0GMnHKAjjkg72ThT8nKpwevQq7x1KCRL0K9Vu0W10iHhxgQ4bx1_Bp2Ckt16z8WqaUY1cPd0MyEW1Q1YScJISjLI8A8_TmqXAbCPWm9AJ4ZYVs9RlD7hjdZ-WBP6bdUjEWY5ds2HYQxxz-J9etn9dsZnb-itmN2q5hCqHSDtI8DUlyWFGtQRbp-fZj0yVbdWvNpyk3_O6O2dZhqhPNQ0CTknTpT-vU8YAqeoX5kr9l4Lh4o9N15xOmFUW0zqAymt57Lt2A8cGwCKx9EanStDgaxdvAhbBBUJ0D0w5xayLlRGxNQABwMqLKeq5b3TA78RA2P6NPhuDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2acbb794f.mp4?token=Zt9H5Np0C4U0GMnHKAjjkg72ThT8nKpwevQq7x1KCRL0K9Vu0W10iHhxgQ4bx1_Bp2Ckt16z8WqaUY1cPd0MyEW1Q1YScJISjLI8A8_TmqXAbCPWm9AJ4ZYVs9RlD7hjdZ-WBP6bdUjEWY5ds2HYQxxz-J9etn9dsZnb-itmN2q5hCqHSDtI8DUlyWFGtQRbp-fZj0yVbdWvNpyk3_O6O2dZhqhPNQ0CTknTpT-vU8YAqeoX5kr9l4Lh4o9N15xOmFUW0zqAymt57Lt2A8cGwCKx9EanStDgaxdvAhbBBUJ0D0w5xayLlRGxNQABwMqLKeq5b3TA78RA2P6NPhuDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: صهیون پیروز شده است.
🔴
بنجامین زئو هرزل، پیروز شده است.
🔴
ما در حال پیروزی هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140077" target="_blank">📅 21:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
چند نیروی روسی توسط اوکراین از بین رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/140076" target="_blank">📅 21:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فارس به نقل از یک منبع نزدیک به تیم مذاکره‌کننده: در صورت نهایی‌شدن تفاهم ایران با عمان، بازگشایی تنگه هرمز مستلزم انجام تعهدات آمریکا می‌شود
🔴
یک منبع آگاه تاکید کرد که در صورت نهایی‌شدن تفاهم ایران با عمان، بازگشایی تنگه هرمز مستلزم ترتیبات جداگانه‌ای است که شامل انجام تعهدات آمریکا هم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/140075" target="_blank">📅 21:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7003e27.mp4?token=v0GDlSMOiybwNJXbP-sPWi6PiiUuLUYCDne2vrhzAlFLMZ-2wJN0jj-orrm0DwzBMLXJTCR7xuSQXqWwAbbdIHOW9oq_N_QedrXRLfg1tVYxF9dC6RGvOtuhBkLs8lpbWWySWJgCnGmj7KQ7YOjQghIzSdkproQA3Wex-M1dXARSSMIlKrp0xhVlJLcMhN1jKPbxXbLvuu6gDgqGmpWjQZKfCVUWrb_2Kaf3Z69rXj5DKeIDkchgne6fgDMKwSVyZpmsS4jSKD-BeiITvggAk8SspLIypI1PE8vV7cKHUQtjl8sFy8hk5gZZmfFl9pdvfa-0BvTWL2LRjwKDLtYaPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7003e27.mp4?token=v0GDlSMOiybwNJXbP-sPWi6PiiUuLUYCDne2vrhzAlFLMZ-2wJN0jj-orrm0DwzBMLXJTCR7xuSQXqWwAbbdIHOW9oq_N_QedrXRLfg1tVYxF9dC6RGvOtuhBkLs8lpbWWySWJgCnGmj7KQ7YOjQghIzSdkproQA3Wex-M1dXARSSMIlKrp0xhVlJLcMhN1jKPbxXbLvuu6gDgqGmpWjQZKfCVUWrb_2Kaf3Z69rXj5DKeIDkchgne6fgDMKwSVyZpmsS4jSKD-BeiITvggAk8SspLIypI1PE8vV7cKHUQtjl8sFy8hk5gZZmfFl9pdvfa-0BvTWL2LRjwKDLtYaPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نفتالی بنِت، نخست‌وزیر سابق اسرائیل:
نتانیاهو متهم به ارتکاب جنایات جنگی در لاهه است. فرماندهان ارتش دفاعی اسرائیل نیز متهم به ارتکاب جنایات جنگی هستند. پسر شما از سفر به سراسر جهان می‌ترسد.
🔴
این قطر است. و ما هیچ کاری در مورد آن انجام نمی‌دهیم. این کاملاً پوچ است.
🔴
من انتظار دارم که هر رهبری در اسرائیل به صراحت بگوید: قطر یک دشمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/140074" target="_blank">📅 21:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
الجزیره: تنها یک یا دو موضوع در مذاکرات ایران و عمان باقی مانده است
🔴
تنها یک یا دو موضوع در مذاکرات ایران و عمان حل نشده باقی مانده است و  این مسائل به نظر نمی‌رسد چندان پیچیده باشند.
🔴
در صورتی که هیچ دخالت بدخواهانه‌ای از سوی سایر طرف‌ها صورت نگیرد، می‌توان امروز یا فردا به توافقی دست یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140073" target="_blank">📅 21:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده سنتکام: ما به اعمال محاصره علیه ایران ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140072" target="_blank">📅 21:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نتانیاهو : وجود اسرائیل با توافق یا بدون توافق قابل مذاکره نیست
🔴
ما کشوری قدرتمندیم که به هویتمون افتخار می‌کنیم و به مسیرمون باور داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140071" target="_blank">📅 20:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=CncgaFWttU8ac9LDHaAFsBfv0TvKIEQpjidFADlUAk7wIlf49xTQwqdCL6Mj3OVO0UKK9mtpSFHVNfB_BpGBFuvGtV3JkihDcC6MKLnyGbIj9v4rpgci-eLIG0VNAQCt5YMaDTedxNT5M8MzpcxYH_qC1zxnN0DFm1QpcQyYahncW2396-xh0FMsiLBVdZGAkTifOzz2_u08M-vLHsJNTgy86MRU0PofOZX8IbQ4ILh_mFXLNXVWlBw5qw3DK5LHJ9wbWgYc4Rsz850GHooxMm5yE07-7xCcVoHPvjFuToOmPH-gDejotPHjkPhxqXdep-zbuOAc4undgHLBqzZk4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=CncgaFWttU8ac9LDHaAFsBfv0TvKIEQpjidFADlUAk7wIlf49xTQwqdCL6Mj3OVO0UKK9mtpSFHVNfB_BpGBFuvGtV3JkihDcC6MKLnyGbIj9v4rpgci-eLIG0VNAQCt5YMaDTedxNT5M8MzpcxYH_qC1zxnN0DFm1QpcQyYahncW2396-xh0FMsiLBVdZGAkTifOzz2_u08M-vLHsJNTgy86MRU0PofOZX8IbQ4ILh_mFXLNXVWlBw5qw3DK5LHJ9wbWgYc4Rsz850GHooxMm5yE07-7xCcVoHPvjFuToOmPH-gDejotPHjkPhxqXdep-zbuOAc4undgHLBqzZk4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محسن رضایی: به عنوان یه سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن، چون ما داریم بعد از آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم؛ این شرایط گذاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140070" target="_blank">📅 20:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
غریب‌آبادی:  پیام‌هایی از آمریکا دریافت کردیم مبنی بر آمادگیشون برای بازگشت به تعهداتشون!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140069" target="_blank">📅 20:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
غریب‌آبادی: در گفتگو با عمان روی تمامی موضوعات مطرح‌شده، از جمله نقشه مسیرهای ورود و خروج ترافیک دریایی و ابعاد جانبی آن تفاهمات اصولی انجام شده
🔴
بخش قابل توجهی از این مسیر جدید در آب‌های سرزمینی ایران و بخشی از آن هم در آب‌های سرزمینی عمان قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140068" target="_blank">📅 20:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کانال ۱۲ عبری : ارتش اسرائیل از مقامات سیاسی خواسته است حملات گسترده‌تری را در لبنان انجام دهند، اما تاکنون پاسخی دریافت نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140067" target="_blank">📅 20:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نتانیاهو: هرگز اجازه تشکیل کشور فلسطین را نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140066" target="_blank">📅 20:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
غریب‌آبادی: تفاهم با عمان به معنای اجرای بند ۵ یادداشت تفاهم اسلام‌آباد نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140065" target="_blank">📅 20:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
غریب‌آبادی: تفاهم با عمان به معنای باز شدن تنگه هرمز نیست
🔴
باز شدن تنگه هرمز الزامات خاص خود را دارد.
🔴
تفاهم درباره تنگه هرمز باید صرفاً بین ایران و عمان انجام شود.
🔴
دخالت خارجی در تنگه هرمز را به هیچ‌وجه نخواهیم پذیرفت.
🔴
آغاز درگیری‌های جدید، ناشی از دخالت آمریکا در تنگه هرمز بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140064" target="_blank">📅 20:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
غریب‌آبادی، معاون عراقچی: تفاهم ایران و عمان در آستانه نهایی شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140063" target="_blank">📅 20:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b59ecec6c.mp4?token=HtSMxhCLpD08MGdgzq8Ja84FQ3trOMRk0hkwenqyTCGQJMyvT9jXREn9ib3F3IYPc3cY-kvWlj5-yOtnCWEBvP2lS3azHeeA4NLP7YH39VAae3Bz1R1VerxFHPzzwRxdYDngTD8Y1C6eUpbk6FopD9W6uSA1ruXN2Fo4p8SX4fQGXW6OtIcxmxqAGNXwdNQcIL7Kcz_2IhYcgpPOe60GqDxHo9Kpgdn4KUWpfsNNnIA1AnRSj7MM5xVTsN_GxdjDWnr_iPTNc2HQG1NMBtkg4nVLbCyP2C6xNMo6nx3FS2aSK8JX9JjPJWL1H9RPTlm0mkhe8zppFSWKjT6I9jUPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b59ecec6c.mp4?token=HtSMxhCLpD08MGdgzq8Ja84FQ3trOMRk0hkwenqyTCGQJMyvT9jXREn9ib3F3IYPc3cY-kvWlj5-yOtnCWEBvP2lS3azHeeA4NLP7YH39VAae3Bz1R1VerxFHPzzwRxdYDngTD8Y1C6eUpbk6FopD9W6uSA1ruXN2Fo4p8SX4fQGXW6OtIcxmxqAGNXwdNQcIL7Kcz_2IhYcgpPOe60GqDxHo9Kpgdn4KUWpfsNNnIA1AnRSj7MM5xVTsN_GxdjDWnr_iPTNc2HQG1NMBtkg4nVLbCyP2C6xNMo6nx3FS2aSK8JX9JjPJWL1H9RPTlm0mkhe8zppFSWKjT6I9jUPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد رائفی‌پور: ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140062" target="_blank">📅 20:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140061">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/140061" target="_blank">📅 20:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140060">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3iGS-X1-1GMnkKOBbCKm9eNnetsKVpucl9ATHA5NU7Kj5GEcOTRhJM4exqiDlM1OA45kugWhW033OnLa1h3sT_irkBVQFS4MDYe8jnohpC9DrWhMduS340GnGQP6P7eoY-ad6WxPWjp1589FxqD88dKsn3EIJD5hhv1U1yhdt_V88XeATRp4y_dfnhQqhJAbo_B_SzRFxeRmII26_ywhc2iIODT2sctKxRIvFUoXw5AVfdLdFAUA_4okGBT3RgyXMkxwcad8itwa4tnk7lZFbs-zIKmHaOlkqw2STV9tyxDuUbnYHLAF-ZTWqzKWu_jrqfAIbUAX88o-XQK3y0XGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140060" target="_blank">📅 20:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140059">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/votL544J0bIAC_l8JeOCDZmEP89GJTYkkWQvNwxt99_bWtkGaASdK77MAPQdoje3x7dpMQJt6orbQamrIE8Je60j-H_ytq4W1wWhb3lxuELvfkSGfUS9v4ZrzOlgKWxkwAKDVy3bzPwh1gAbUUa_UakPHAEtLABlx7Fm0qZqNXMKU3UIDALid1aAUj0J9zaZArA4ADM1uX0hOAumI52iU7d5YR1WZLmckF-TDM9tNFaERkNwq5rI5U3wPLghCPoVO8nNw3j7bDcVeDR0D_yDN3QF_t1YYDQDlbb9gHmk45F5BHfFHY8yRO7aJxawfFWR_Vpp4iGS2sHAIJ1FD89XoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار سهام امریکا تمام افزایش روزانه خود را از دست داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140059" target="_blank">📅 19:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140058">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر انرژی ترکیه: ظرفیت مسیر نفتی جایگزین تنگه هرمز را به ۲.۵ میلیون بشکه در روز می‌رسانیم
🔴
وزیر انرژی ترکیه با اشاره به بحران عبور و مرور کشتی‌ها از تنگهٔ هرمز گفت تحولات ماه‌های اخیر نشان داده است که جهان به مسیرهای جایگزین برای انتقال نفت نیاز دارد و آنکارا در حال مذاکره با عراق برای توسعه مسیرهای جدید صادرات انرژی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140058" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZOfF_8OgyMpwbv7yWUmKS3GIV4Dl2hF7SZOZJ-LMWqsGmpvT4FWWkm4Ej9Uz29DKjlQZ9xNzf1XtdicpoIPTApDUgQx_SYVTWemdpxFNk6XyW6K5iKtb9Z4Oj1cqSVTeETQmgyAuxAlfQgR0NG3PCTyKcwuVhOVZC2xm0yrEhWTTHMSwHJFUTRR_gd8e-esS36wqFX4Lit27I4cwnbCOKvDcSWkwkwpDRHRntKCA9-ZzgjBQ3oJkJL6aHrG9CbWlnWg9m_WtXJkECGQaoSartHjEL4PbhFeBStlWiObTs_jwpfFWLzplQJLTNc07c4Qt6ATMN5aXyXH2fOifGUTbow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز UKMTO می‌گوید ناخدای یک نفتکش از شنیدن صدای انفجار مهیبی در نزدیکی کشتی خود خبر داده است.
🔴
این حادثه در ۹۵ مایل دریایی جنوب شرقی عدن، یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140057" target="_blank">📅 19:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نماینده مجلس: طرح موضوع بازکردن تنگه هرمز در مقابل لغو تحریم با واقعیت مطابقت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140056" target="_blank">📅 19:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140055">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فووووووری / منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140055" target="_blank">📅 19:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140054">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فووووووری / منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140054" target="_blank">📅 19:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f4c0e158.mp4?token=dVoeY5atjqFeXu4Y1xKXcMKp0DNcW1hadBBD-8_X1jd_A88j-zqzo79Wm5Ymg4ZGtrhvdEH3IT4-bYToeis-qzUfvK_4CmI5d30m9EHhchrslOMnoKMQtoBR62HRcRZOX9uXHgA0alI1YX0Jz9mHQGYQSHCrRVYaXrbpOGeMITMnyU9o70wjOonaDAZ4gN5YSYg3FrVER1eC-BTOf27fXO5rK8RZ1uIL4n3I3mBBYI9saV6fdaIiK-ecnynID2pcUjhSTDUDlnWlFj5TaMEalUx2duWyBc_FJ_mOo6ZFK7yO_MJDXJ_qkAfHmPB4T0vFneLgwVvU6IcZaX6f-iuRzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f4c0e158.mp4?token=dVoeY5atjqFeXu4Y1xKXcMKp0DNcW1hadBBD-8_X1jd_A88j-zqzo79Wm5Ymg4ZGtrhvdEH3IT4-bYToeis-qzUfvK_4CmI5d30m9EHhchrslOMnoKMQtoBR62HRcRZOX9uXHgA0alI1YX0Jz9mHQGYQSHCrRVYaXrbpOGeMITMnyU9o70wjOonaDAZ4gN5YSYg3FrVER1eC-BTOf27fXO5rK8RZ1uIL4n3I3mBBYI9saV6fdaIiK-ecnynID2pcUjhSTDUDlnWlFj5TaMEalUx2duWyBc_FJ_mOo6ZFK7yO_MJDXJ_qkAfHmPB4T0vFneLgwVvU6IcZaX6f-iuRzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل اعلام کرد که یک آزمایش از پیش برنامه‌ریزی شده از سامانه دفاع موشکی برد بلند «فلش» با موفقیت انجام شد. مسیر پرواز موشک از مناطق مرکزی اسرائیل به سمت دریا قابل مشاهده بود.
🔴
وزارت دفاع گفت که جزئیات بیشتری درباره این آزمایش که به صورت مشترک با ارتش اسرائیل و صنایع هوافضای اسرائیل انجام شد، در زمان دیگری منتشر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140053" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
قیمت جدید بنزین سوپر در بورس انرژی ۸۴,۶۰۰ تومان تعیین شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140052" target="_blank">📅 19:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
المیادین به نقل از منبع امنیتی-سیاسی ایرانی:  مذاکرات ایران و عمان درباره ترتیبات مشترک برای مدیریت تنگه هرمز به مراحل مهمی رسیده است.
🔴
ایران تأکید دارد که یکی از ترتیبات ضروری، ثبت هرگونه ورود یا خروج از طریق تنگه هرمز در یک سامانه ویژه است.
🔴
ایران معتقد است این اقدام امکان اعمال نظارت کامل بر تردد دریایی را فراهم می‌کند و به جلوگیری از وقوع حوادث در تنگه هرمز کمک می‌کند.
🔴
عمان همچنان در حال انجام رایزنی‌ها و مذاکرات درباره این پیشنهاد است؛ پیشنهادی که ایران بر اجرای آن اصرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140051" target="_blank">📅 19:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974ee64391.mp4?token=QQuL7FnUm7WH0eCj-ZmFTpV5J53HhJU_UscFT0Y2neqPrpzh8jJkSPS-Dsoj6t2Zphs-FJh97b9IxY0aEG7QWvjAS-tg8uAhI-xwHry3__-kmhE7hQ0194glybWN2VHA5K-RDsE6nOuAHcT_H6EN77lIPKg0aT56i_KbrQ-0d_uE8f5ovTvx9WmTZWvOA4ABXfzUi_EfphYAx2RY-aVP2npFoCiQ12rVTH7HZTygV9oAW0Y_4ayucCAtXnqq3gX0watQeiE-vDCgU1TgEjkYCeV4i8Jy5r-ZzlYmkcW-uX0RbvOEQXvLGrXY0RmTGdRjH3p4i3DswTBD98TuYhf8Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974ee64391.mp4?token=QQuL7FnUm7WH0eCj-ZmFTpV5J53HhJU_UscFT0Y2neqPrpzh8jJkSPS-Dsoj6t2Zphs-FJh97b9IxY0aEG7QWvjAS-tg8uAhI-xwHry3__-kmhE7hQ0194glybWN2VHA5K-RDsE6nOuAHcT_H6EN77lIPKg0aT56i_KbrQ-0d_uE8f5ovTvx9WmTZWvOA4ABXfzUi_EfphYAx2RY-aVP2npFoCiQ12rVTH7HZTygV9oAW0Y_4ayucCAtXnqq3gX0watQeiE-vDCgU1TgEjkYCeV4i8Jy5r-ZzlYmkcW-uX0RbvOEQXvLGrXY0RmTGdRjH3p4i3DswTBD98TuYhf8Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان فترمن: کشور ما مسئولیت بسیار ویژه‌ای برای حمایت و پشتیبانی از اسرائیل دارد.
🔴
ما دموکرات‌ها هستیم. ما ارزش‌های پیشرو داریم. اسرائیل کشوری است که در آن منطقه ارزش‌های مشابهی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140050" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140049">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ecff42e55.mp4?token=BGbBmsT4pq55T2vDawT5dvNK7jW9LYGRP3v82kTndNaoPui5g1PkqPJj5g07C5xw-mztF3XJNtzpmB3EmLnif0Q2HJU2FxqhIh4_oOvhgOWJqCo5Oz5s7YgeiGfEOHcR3Negyo_t22IHHZ3ZtvhIHMY9NTg6QjufGXTGWJC2NfqyKOI9BoNPoRYDmh_u6MAdd3Ksmc8CGGiYV8lz64j1v66j5AVJ7xZBIwL_7pNWBcvLGJYq5HQFW1JcpizILaB0Xorl1Mu7Qzgo-owuY5ABVOA_1gLQVAkPiyX7sOLkxmjMk3BLPZyJbC_6vePJjljEKtCS0Z4emzJx9EDbIcuyvTcd6uIaCfU51KBmTqU3Dju_xAt7Aa7joMArc3xeiFEPu8RZqtgSoq0JtctOEXoB8-DZMKIeYetubCYaFmloqLgmspBsYn_xDP3LZ9d3uSa31YICHngRxCRT6EqiMD66DVA3RBr9ECJs0P5rfSsiKcJv9mJJEGRlUTChEecvHDIkCtly_PwfWLRMzzJ4kXwuM_dqLoyydoSHbgVhXMC6VdlPqtKR0md8_KGZcc1ZrGZzq5s29kuIILhAk_kbt9PhV8hSWDeG-ogRjdWexLLIQdQTyc82-EP_TZG3agExmM1T7nHzrrcMrorAOKkUAxQJqNMMeuyNBAogixYzxUYOgGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ecff42e55.mp4?token=BGbBmsT4pq55T2vDawT5dvNK7jW9LYGRP3v82kTndNaoPui5g1PkqPJj5g07C5xw-mztF3XJNtzpmB3EmLnif0Q2HJU2FxqhIh4_oOvhgOWJqCo5Oz5s7YgeiGfEOHcR3Negyo_t22IHHZ3ZtvhIHMY9NTg6QjufGXTGWJC2NfqyKOI9BoNPoRYDmh_u6MAdd3Ksmc8CGGiYV8lz64j1v66j5AVJ7xZBIwL_7pNWBcvLGJYq5HQFW1JcpizILaB0Xorl1Mu7Qzgo-owuY5ABVOA_1gLQVAkPiyX7sOLkxmjMk3BLPZyJbC_6vePJjljEKtCS0Z4emzJx9EDbIcuyvTcd6uIaCfU51KBmTqU3Dju_xAt7Aa7joMArc3xeiFEPu8RZqtgSoq0JtctOEXoB8-DZMKIeYetubCYaFmloqLgmspBsYn_xDP3LZ9d3uSa31YICHngRxCRT6EqiMD66DVA3RBr9ECJs0P5rfSsiKcJv9mJJEGRlUTChEecvHDIkCtly_PwfWLRMzzJ4kXwuM_dqLoyydoSHbgVhXMC6VdlPqtKR0md8_KGZcc1ZrGZzq5s29kuIILhAk_kbt9PhV8hSWDeG-ogRjdWexLLIQdQTyc82-EP_TZG3agExmM1T7nHzrrcMrorAOKkUAxQJqNMMeuyNBAogixYzxUYOgGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین زلنسکی
:
اوکراین لانچرهای موشک بالستیک روسیه را نابود خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140049" target="_blank">📅 18:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140048">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3589745b.mp4?token=CnMWZ7RNbn7PwRPrIJT9FuvWLwcIdco_4Xb9hTHeHArsDSez6dMPL1_e0l8PMCwT2rqHbpBTXu63IIPFRlohFXH2kC-lKI82lco20fpuj-lOyXwOAnsDmcWbi2-w4pzgbeRCZPJzOSOgdSI84usnmWzsgFOhZV-f2Gl4MIhhOdSiFFYemiaM0fDJJMqkjPBVHfCFmbTjutNyB1Yf6pBLkzDv-OerAjdoHmWn7P8hhdNmAw_5wu3LM0jisi37XySyPtelKqCIpxQgLRJDKzrZAxCEWRSFBDjoWtVoEEPBxf_2Qy-j-idh191ShUWzK_o61MTtWi4gKm58osAkOXzljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3589745b.mp4?token=CnMWZ7RNbn7PwRPrIJT9FuvWLwcIdco_4Xb9hTHeHArsDSez6dMPL1_e0l8PMCwT2rqHbpBTXu63IIPFRlohFXH2kC-lKI82lco20fpuj-lOyXwOAnsDmcWbi2-w4pzgbeRCZPJzOSOgdSI84usnmWzsgFOhZV-f2Gl4MIhhOdSiFFYemiaM0fDJJMqkjPBVHfCFmbTjutNyB1Yf6pBLkzDv-OerAjdoHmWn7P8hhdNmAw_5wu3LM0jisi37XySyPtelKqCIpxQgLRJDKzrZAxCEWRSFBDjoWtVoEEPBxf_2Qy-j-idh191ShUWzK_o61MTtWi4gKm58osAkOXzljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو با وزیر امور خارجه بریتانیا اد میلند دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140048" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
شهباز شریف: پاکستان به تلاش‌های خود برای صلح در منطقه ادامه می دهد
🔴
رایزنی‌های مثمر ثمری با دکتر پزشکیان درباره برقراری صلح پایدار در منطقه داشتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140047" target="_blank">📅 18:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مختصات جغرافیایی مسیر مد نظر ایران و عمان، مورد تفاهم قرار گرفته
🔴
چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک دو کشور مشتمل بر ملاحظات و نکات عمده مورد توافق نیز در مرحله بررسی و تدوین نهایی است.
🔴
سخنگوی وزارت خارجه درباره احتمال سفر قالیباف یا عراقچی به پاکستان یا قطر در پایان این هفته: برنامه‌ای برای سفر به این کشورها نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140046" target="_blank">📅 18:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/لحظاتی پیش نتانیاهو یک جلسه مهم را به صورت اضطراری به دلیل رویدادی در خاورمیانه ترک کرد و اعلام کرد:
🔴
نیازهای موجود و بسیار مهم در شرایط سیاسی، مرا مجبور می‌کند که قبل از پایان این مراسم مهم، آن را ترک کنم،
🔴
ما در حال حاضر شاهد تحولات نظامی و سیاسی مهمی در منطقه هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140045" target="_blank">📅 18:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
مدیر سابق موساد، دیوید بارنیا به شرکت فناوری دفاعی آمریکایی اونداس می‌پیوندد
🔴
دیوید بارنیا، رئیس سابق موساد، پس از ترک اخیر آژانس اطلاعاتی اسرائیل، به عنوان رئیس جهانی و رئیس هیئت مدیره به شرکت فناوری دفاعی آمریکایی اونداس دیفنس پیوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140044" target="_blank">📅 18:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نتانیاهو: ترامپ بزرگترین دوست ماست، اما موجودیت اسرائیل قابل مذاکره نیست. چه با توافق، چه بدون توافق، هر کاری لازم باشد برای تأمین آینده‌مان انجام می‌دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140043" target="_blank">📅 18:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
الجزیره: تنها یک یا دو موضوع باقی مانده برای دستیابی به توافق با عمان باقی مانده است و می توان آنها را حل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140042" target="_blank">📅 18:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL4AWsgeqMD3SFe_okQFNlNV9vexylHHU34WA6fENX-pzaWjS4XJWwXk8co55DOnlySAMeAYD5eTIMvhSlnCE3RHBsG3TXcZI1gT3WsYQvTHT9323unwR1Cw0AzyyKnHtmBuAfrgPBze-UKBPEA6sqBJa8Mm516d2cPkYkefJYfS_yuOb0wBYgEAJhWIt35xpnZdSqITTWktIpMzZrxDYicZ0-2zyYbCUOSe17_vMRbxcH-pXG2crMZHw7425jvmkpUjG1hkqTCLbmXCOcAWzstIRcSkddpbcI9W6NScAXmiVSkc_ugLa-sLqaVA-WMbnwVoYbezKea0MntjapO-1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات رفع تحریم ها در وب سایت خزانه داری آمریکا
🔴
تگ IRGC چند شرکت هواپیمایی و هواپیما حذف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140041" target="_blank">📅 18:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شبکه ۱۵ اسرائیل: بر خلاف آنچه که خبرگزاری رویترز گزارش داده است، این اقدام یک کاهش تحریم‌ها علیه ایران به طور خاص نیست، بلکه یک کاهش تحریم‌ها علیه عراق است .! که با شرکت های مرتبط با سپاه بتوانند کار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140040" target="_blank">📅 18:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7MDX11i-BpFKlzj26RJpB9orqPgm9Cr6BZR5yF5YIwt9A3FQKKiTIog9jp5t-9uVz8XHXob3UIJWVQubG2Hb_ArAla5Bk8AFAvlg5Ml-yN7_ksjdHSehXLwNNZ2Ta35MZPJbV-IUtDhLwV84BKBR1I0faFhiAgArX8j8hXkfNRzn5FqVazTo3ehMY7EEOJ3wsLuvQyF5EkkvnapIHR_06eJVCc5t0i0bCeMAuKDT8G_psoJDeSho9uSgS_ygdqn9zZHmHYrut-08_Y4pw6kprErPdz2hcYrW5TWzDmylt4wdA0pkBbHd53NdWdPGp2z9coa5ouWwBUxdT888Z5M2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وای نت: قبل از شروع جنگ 40 روزه ایران و آمریکا، یه طرح روی میز بوده که بر اساسش قرار بوده حدود 15 هزار نیروی کرد با حمایت هوایی اسرائیل از مرزهای غربی وارد ایران بشن؛
شهرها رو یکی‌یکی بگیرن و همزمان افراد بیشتری بهشون ملحق بشن تا تعدادشون به 150 تا 200 هزار نفر برسه و به سمت تهران حرکت کنن.
اما این طرح به خاطر مخالفت نهادهای اطلاعاتی اسرائیل و پایین بودن شانس موفقیتش، هیچ‌وقت اجرا نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140039" target="_blank">📅 18:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رویترز:
بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140038" target="_blank">📅 17:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوووووووووری/اسکای نیوز عربی:
وزارت خزانه‌داری آمریکا اعلام کرد تحریم‌های مرتبط با ایران را لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/140037" target="_blank">📅 17:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140036">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس:
مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140036" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140035">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:توافق مربوط به تنگه هرمز شامل دریافت عوارض از کشتی‌ها برای عبور نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140035" target="_blank">📅 17:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:توافق مربوط به تنگه هرمز شامل دریافت عوارض از کشتی‌ها برای عبور نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140034" target="_blank">📅 17:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140033">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رویترز: توافق بین ایران و عمان در مورد تنگه هرمز هنوز نهایی نشده است و عباس عراقچی، وزیر امور خارجه ایران، در حال حاضر در تعطیلات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140033" target="_blank">📅 17:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140032">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
فرمانده‌‌سپاه:
وقتی آمریکا و اسرائیل خلع سلاح هسته‌ای شدن ماهم میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/140032" target="_blank">📅 17:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140031">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
جائه‌میونگ، رئیس‌جمهور کره‌جنوبی با اشاره به نقش فارغ‌التحصیلان آکادمی ارتش در تمامی کودتاهای تاریخ این کشور، خواستار ادغام سریع دانشکده‌های نظامی ارتش، برای جلوگیری از تکرار کودتاهای احتمالی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140031" target="_blank">📅 17:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140030">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
هواشناسی استان تهران: از عصر پنجشنبه وزش باد نسبتاً شدید به‌ویژه در ارتفاعات و مناطق جنوبی و غربی استان، همراه با خیزش گردوخاک پیش‌بینی می‌شود.
🔴
همچنین دمای هوای تهران در روزهای پنجشنبه و جمعه بین ۳ تا ۴ درجه کاهش می‌یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140030" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رویترز: علی‌رغم اظهارات رئیس‌جمهور ترمپ، به نظر نمی‌رسد توافق‌نامه‌ای در مورد تنگه هرمز هر زود امضا شود، زیرا چندین مسئله بزرگ همچنان حل نشده باقی مانده است.
🔴
مذاکرات در حال پیشرفت هستند، اما هنوز «زود» است که بگوییم توافقی با عمان حاصل شده است، یک مقام ارشد ایرانی و دو منبع منطقه‌ای گفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140028" target="_blank">📅 16:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ارتش اسرائیل در پاسخ به «نقض آشکار آتش‌بس» توسط حزب‌الله، حملات هدفمند در جنوب لبنان را آغاز کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140027" target="_blank">📅 16:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIbpN40vHGegrWiiqpOUPmWxL-P4L7OiJJ7WXE_J7VvM9O7K1ZpnI0VUtmzhzoRvhB7dD2GLLBfpXCLPbsfh0dd9vixnJiKwcDnZZiF2YU82Im6MLr3X81ydMCXesamHwBx-6Hm5ee8Rjqu7nW89zW4HC9xfGY_6Wg1wYfZ-FxouvnLUGg0o_-c18q3Iu0RQO9-DV4hek0m0iNsmt5j5VGRFq4ngyoU5HpkUpfj8pF2kRlihN79opHEHig7rBLNITljFO2gQdh4AvEEMr4-6UbBZ-yZ6yD7w5io5a2T3YmfEIE2uO1LjsoWakSy9f3eTLu7AcNTJR3-trqzw7Yx6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : کره جنوبی پروژه راه‌آهنی که برای مدت طولانی در نزدیکی منطقه غیرنظامی متوقف شده بود را احیا خواهد کرد که در نهایت می‌تواند با شبکه راه‌آهن شرقی کره شمالی مجدداً به هم متصل شود.
🔴
این اقدام بخشی از تلاش گسترده‌تر سئول برای بهبود روابط بین دو کره است، علیرغم بن‌بست دیپلماتیک در جریان و تخریب کره شمالی از پیوندهای راه‌آهن و جاده‌ای فرامرزی در سال ۲۰۲۴
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140026" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140025">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام از کشورهای حاشیه خلیج فارس: احتمال رسیدن آمریکا و ایران به توافق موقت در روز جمعه ۵۰/۵۰ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140025" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140024">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزیر خارجه سعودی در شهر امان با همتای عراقی خود دیدار کرد. بر اساس اعلام وزارت خارجه سعودی، در این دیدار روابط میان دو کشور مورد بررسی قرار گرفت.
🔴
همچنین وزرای خارجه دو کشور درباره تضمین تبدیل نشدن خاک عراق به ابزاری برای تجاوز به همسایگانش گفت‌وگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140024" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140023">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGAZ1DEatMOJsZGO6HTh7ToG1uRI3mueyuD8XFuxSIU1nARcdb2UvzjXkbF7KIiFDcc0hofkrZrETw1qiFJPI1wy0tygOsdgsrnp9CF0xyr_K3N6obHyd-cEEZdmGQcr4tB7XS0IleuaDXRrlPxuUeYBv3ybaxns7NnhrbMT6Dwj5f4_4YmuQFg3Zhf6eJYFEjLc4AyMO4r60PnJ7H24WT4dgjogu-5w81SoNZJyogcMmtMAWYnjZ37cJRIzh1pDPoaeCC1Fpsc4qkd7uWUISl57AA_W2inMZ_lrVMiSA2dqqDK-uORUs2HmfkdbVUm9Ec2LF13-Z9liiQWWgp8qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرگ یک فوتبالیست تایلندی پس از برخورد صاعقه در حین مسابقه
🔴
پلیس تایلند: «سوفوان آوای» ۲۴ ساله روز گذشته (سه‌شنبه) پس از اصابت صاعقه به زمین ورزشگاه «سانتی‌فاپ» واقع در جنوب تایلند، دچار جراحات وخیمی شد.
🔴
به رغم تلاش‌های تیم‌ فوریت‌های پزشکی، بر اثر شدت جراحات وارده جان باخت
🔴
۱۲ بازیکن دیگر نیز دچار مصدومیت و به بیمارستان منتقل شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140023" target="_blank">📅 16:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140022">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
حماس: بر پایبندی خود به توافقات صورت گرفته با میانجی‌گران در خصوص نقشه راه غزه تأکید می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140022" target="_blank">📅 16:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140021">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_WxhH8-HiBB2jr38etQitHptImKoUL0XGxH_cRx4R_H8vFe4e-1R5Icas7kntYiONLTpHgWpSgbKRpeqb9Im7MlAyTmF9arnq4ryIeNqrI3W7rxo5ELe4EdzQiunriuxKB8rVBqiTv_Q4ncpBHaCPHRCfmrTylU6NDqKmucResN5qL3TOTWLt_K3mqJAhjiEgoKGefb8x3Pl4vI5uOIwYR6jhUB_BaYiihKFkOHeWjvy5lrYdTEHGMW6ZKruzuX-uOKSM8mhdn1JiW_ORdtkdtlDEob17JimMb794-L6Afdm5-F7P4UvTqTgfnIS56QsBKGcwgq-r46hWSzbpDk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار از زمان توافق چارچوبی، ارتش اسرائیل هشدار فوری به ساکنان شهر المنصوره برای تخلیه و عقب‌نشینی ۱۰۰۰ متری از شهر صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140021" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140020">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رویترز نوشت:  داده‌های یک شرکت ردیابی دریایی حاکی از آن است که تردد کشتی‌ها در تنگه هرمز تغییر چندانی نداشته و همچنان بسیار محدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140020" target="_blank">📅 16:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140019">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkjx4UY4fKgmnwZIOi4hKBLACUn8li3MBsI7evS4I7EEgk0qhang5iTzMQ5W_YokksKnrJAetiB4lWwF8WJ1PJIavEFu_Gh4xNYmWXvZe4FQ3_Nv4V90wWm6PRJegkM7mncuuPBKp2Gj96XT-AA65kkwK5AIjPk8uLP4WVFt7lTHxfINDX7jEnSnsx5twAD4lUexUJetJVHjjbKjSnPvpH0BMH5dIRG3YHrCjYiGrprhLk4d3Wfjxxg7GAmQcGwGQb-hhfG1ueRQRaZlY0zrPHeSZN3CunAfIdI5PvrFmEIZkheXf2Xj8BQaN-4AjujczdY1ZjgIsAjFDnFwt9CIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی اونس طلا در ساعات اخیر بیش از ۱۵۰ دلار افزایش یافت و به ۴۲۰۰ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140019" target="_blank">📅 16:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140018">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri_fi8TZWD6kzWySzLAv_Q_mn_Qx6IGNHI11Lf2KNMkXbcnqAhL7HzHZl8PoCNHVaTLqDmRLcmH-vBDg_YVOyuowhMyX8CC4PV_TDqtg8Hl4-r6kBu3NHfsBJOHV_KF0jDUSSLhTJb-kLsj8-F7okjqj0ebgpPalKXnZucOpWPMYPfj5Jd3zpSZF4Tk06iEnzUunrTeerxjigwd3sy2J6hBHaDNK6u8pHlO_YeXemVCckA5EJUrvWjb8YBJHRYj_pki0SGeP2N-iGtGBU77Ubw7UJroFU3yhc6NcWajO4TO0Vt6ugg_I20vRJ1vHyxuf3Lb0KjjmM_VYenb1YseWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آمریکایی مدل سی-40 کلیپر، که مخصوص انتقال مقامات ارشد نظامی است، در حال حاضر وارد آسمان عربستان سعودی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140018" target="_blank">📅 15:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140017">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرنگار المیادین در تهران: چشم‌انداز نسبتاً مثبت و خوش‌بینانه‌ای در ایران درباره پرونده تنگه هرمز وجود دارد
🔴
اگر مداخلات آمریکایی متوقف شود، عمان و ایران می‌توانند در مورد تنگه هرمز به توافق برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140017" target="_blank">📅 15:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140016">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرنگار المیادین در تهران: چشم‌انداز نسبتاً مثبت و خوش‌بینانه‌ای در ایران درباره پرونده تنگه هرمز وجود دارد.
🔴
اگر مداخلات آمریکایی متوقف شود، عمان و ایران می‌توانند در مورد تنگه هرمز به توافق برسند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140016" target="_blank">📅 15:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140015">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBa4UbGa2HZXNn8_boM9RDRRJSeGbbZxemxz8ywY8EpQCvK6EO6WpHsF8ac9AwwAd5dxeNVqEsyIptF-_5n9I5xEMPgfWY-x9KDHQnVNnA5ccyfWS_mHqVMkAPSxUbmf1fnNRzX3TDGfmMVgDIotYguwKvyxgsKyXwx5Ka1OazKzsmR8fM38y1F-F8ivqFTjOkhBXdRA1pnrESdJCIVCGeY3mUAA4Zu4PtgHg4n3srj24CQVgIx94Prpoygf0vruYvj9RyfvxNEioHdqaUZz8T51i_uACZkidEQ6Z05PIefsZyVQFbf141NX_xMTQJJosAsl8dkVRicGWzlHD4Qsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پشت پرده حذف تلگرام از «اپ‌استور»
🔴
پاول دورف در کانال تلگرامش نوشت:
یک مهاجم با استفاده از ترفندهای فنی توانسته بود محتوای غیرقانونی تولیدشده با هوش مصنوعی را در یک پیام قدیمی ویرایش کند تا از دید اعضای گروه و گزارش‌های مردمی پنهان بماند.
🔴
این اقدام با هدف باج‌گیری از مدیران گروه‌های بزرگ انجام شد تا در صورت پرداخت‌نکردن پول، گزارش تخلف آن‌ها مستقیم به اپل ارسال شود.
🔴
باج‌گیران، راهی برای سوءاستفاده از واکنش‌های شتاب‌زده‌ی اپل پیدا کرده‌اند. اپل پیش از تماس با ما، تلگرام را از اپ‌ استور حذف کرد.
🔴
این رویکرد یک ریسک ساختاری برای تمام برنامه‌های میزبان محتوای کاربر ایجاد می‌کند؛ زیرا اگر اپلیکیشنی با بیش از یک میلیارد کاربر بدون هشدار قبلی حذف شود، این اتفاق برای هر برنامه‌ی دیگری نیز رخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/140015" target="_blank">📅 15:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOpoYMp63daMAFuQDgn06qcoBfMWIsXSeDjNcogOlH2Kc_PNUjEw_A2xEB17kX-WpRoM7_ATYiPpmTBzNxAzmsH3JDwVWrmXPU7UvwmQGAIOUTVJsMpuJThW7VqrolFpkUOoZ_n-XzpQv5ZL_gxPLxnKu1IxlQdHczssy4fw-P2X0gcXwYoYdL5Xd641P0rOFsSneUdO4CKOKeNBbxJPu1pw5EOU4ZFHDNZmOBEHVR37zwOfdm0-o3gNJF5MR7NOt-AH7B71eEirY4wBsW_xfxUvm69FGhf_s3GYYhH7R7xxy1t1eb47EyLtASHUZg0BEtkUNTmjRSFtj70tbOY38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون_این کشتی مورد حمله یک شناور بدون سرنشین قرار گرفت که منجر به آتش‌سوزی در داخل آن شد. مقامات محلی خدمه کشتی را نجات دادند و آن‌ها در سلامت هستند. گزارش شده است که کشتی غرق شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140014" target="_blank">📅 15:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
برخی منابع خبری از وقوع یک حادثه امنیتی جدید در دریای سرخ خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140013" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140012">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55a3ac7ee.mp4?token=tbEk_DbLbc5tEouqGN1kwLX9nvbUlnpNrBkAV1-EvNpx3dUcGCs7u3i-FYUtmSL-DLLoUecKqpGky2VQX69g0_i2Gxx2Lki7wgw0JjAvD3VsZPMGte4OGYVur3HlyIXgy-Kt1VF66FmqurgOKCSsTxg7uiRpOcmmlXJV2rYrVbgf9JVD6Qe1UWgdP1za4sBcSktkuvGjY15ciJwPSiO7zygEwFQAk46k9Ov-IEHI-nOlJ_GIMSN13SpR_FQW9ZZqkJvKOcQYAdUWwI2RX9PaFGqWUegi5kU4D0YVCRKOUqlHjrNqdbKovL2vi76cDX6_D5wWB45ZRQivcO3QsvbSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55a3ac7ee.mp4?token=tbEk_DbLbc5tEouqGN1kwLX9nvbUlnpNrBkAV1-EvNpx3dUcGCs7u3i-FYUtmSL-DLLoUecKqpGky2VQX69g0_i2Gxx2Lki7wgw0JjAvD3VsZPMGte4OGYVur3HlyIXgy-Kt1VF66FmqurgOKCSsTxg7uiRpOcmmlXJV2rYrVbgf9JVD6Qe1UWgdP1za4sBcSktkuvGjY15ciJwPSiO7zygEwFQAk46k9Ov-IEHI-nOlJ_GIMSN13SpR_FQW9ZZqkJvKOcQYAdUWwI2RX9PaFGqWUegi5kU4D0YVCRKOUqlHjrNqdbKovL2vi76cDX6_D5wWB45ZRQivcO3QsvbSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور روسیه، پوتین
:
روسیه یک یگان نظامی جدید برای جنگ پهپادی تشکیل داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140012" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
برخی منابع خبری از وقوع یک حادثه امنیتی جدید در دریای سرخ خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140011" target="_blank">📅 15:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded1face75.mp4?token=UB0Nt6nvuShFHKy54Gaca96neuhboJfGnNte0yM6xMHtVDLUG0IsssMzJmyZFQeeCXBzoxg9cRLxUD1hAo2WAmsq0Pq5UCJxOLgO_Uv4sTCZteQ59X0B9-j8jxSdlZI4TDWGxPBf9fuy0GgT1VM3PAY2p1mAsK3RHasste9NN_PfbrKTZy4OOhqWUaj4nKTDQbZM1Fl5lqXVqohbaHxeHd6Y7VwlM3sU2duCAnT-aZM6OG4N_4_s4NDm9Y6cTh8R_Rrwsc7m_WDWmBCLrcLZyn-HejC0Ts-qTAd5l1eHvFxeSaxM-AnnZOuwRQHQPA4pOdQgyDsFuA2TZUJarq0prg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded1face75.mp4?token=UB0Nt6nvuShFHKy54Gaca96neuhboJfGnNte0yM6xMHtVDLUG0IsssMzJmyZFQeeCXBzoxg9cRLxUD1hAo2WAmsq0Pq5UCJxOLgO_Uv4sTCZteQ59X0B9-j8jxSdlZI4TDWGxPBf9fuy0GgT1VM3PAY2p1mAsK3RHasste9NN_PfbrKTZy4OOhqWUaj4nKTDQbZM1Fl5lqXVqohbaHxeHd6Y7VwlM3sU2duCAnT-aZM6OG4N_4_s4NDm9Y6cTh8R_Rrwsc7m_WDWmBCLrcLZyn-HejC0Ts-qTAd5l1eHvFxeSaxM-AnnZOuwRQHQPA4pOdQgyDsFuA2TZUJarq0prg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت هواپیمای هندی به زمین
سقوط این پرواز چندین مصدوم بر جای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140010" target="_blank">📅 15:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
معاون برق و انرژی وزارت نیرو: هیچ جهش قیمتی در قبوض برق انجام نشده و هر کی قبضش جهش داشته، بخاطر این هست که زیاد برق مصرف کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140009" target="_blank">📅 15:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140008">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک منبع بلندپایه پاکستانی در گفتگو با ریانووستی: انتظار می‌رود عباس عراقچی وزیر امور خارجه ایران هفتم اوت (روز جمعه) به پاکستان سفر کند.
🔴
وی قرار است با عاصم منیر، فرمانده ارتش پاکستان، شهباز شریف، نخست‌وزیر و اسحاق دار، معاون وزیر امور خارجه دیدار داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140008" target="_blank">📅 15:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f81b077e40.mp4?token=b8MLTn-q2cuUePKSkWPRu9QpeLMqIKZhzLQutx7iYFRFinNNqWVgZ8PJCsI7O909XNYA8Ptmp-VYtEAdMYEq4aTx3YvBHOmuMvPDoPNrUMUjjtNut9Co-Ht8QfDnrWS8EeC-Des5qLoTWBHnHJIEnhPhjRxZIie0eX0npYBL8BgHxrrN3boc6typQBpByYcWq_9Omq-rqo43-IOiP5carbELwYeq3NSuizrs6wFcstVR_2S9g58DXoKNIpen40DFG9O0VQ2VAPIEy-1zTL3PsC_hP5WBZ_9S9l8R3i2aMDLbKK979vvUsbttUwbJo2vqNiqk6Qgv_iLAFAiw6cRrkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f81b077e40.mp4?token=b8MLTn-q2cuUePKSkWPRu9QpeLMqIKZhzLQutx7iYFRFinNNqWVgZ8PJCsI7O909XNYA8Ptmp-VYtEAdMYEq4aTx3YvBHOmuMvPDoPNrUMUjjtNut9Co-Ht8QfDnrWS8EeC-Des5qLoTWBHnHJIEnhPhjRxZIie0eX0npYBL8BgHxrrN3boc6typQBpByYcWq_9Omq-rqo43-IOiP5carbELwYeq3NSuizrs6wFcstVR_2S9g58DXoKNIpen40DFG9O0VQ2VAPIEy-1zTL3PsC_hP5WBZ_9S9l8R3i2aMDLbKK979vvUsbttUwbJo2vqNiqk6Qgv_iLAFAiw6cRrkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز روس بعد از فرار از مواضعش، گیر افتاد و کتک خورد
🔴
لباس زنونه تنش کرده بود و داخل یک گودال قایم شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140007" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140006">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
🔴
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140006" target="_blank">📅 15:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140005">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پرواز جنگنده های اسرائیل بر فراز استان درعا در جنوب سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140005" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
حسین پاک، خبرنگار صداوسیما: خلع سلاح مقاومت در کار نیست و نخواهد بود هیچ سلاحی از غزه خارج یا تحویل داده نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140004" target="_blank">📅 14:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAVC5MBmpPBoyBb5rIACfJ9MDVi6zQuhT8yXm90xaPLmWpsWznCQ-mpXEH4smqwrQiEUol3m0Aau74Mc0Nqymd9FTLdq8ATYLBmr0QGbJh_oJKuMW6OyrErKfO6jH6j_-IxIJx5XZtarxrrh3JsZqYcc6F3rFRx089c6QUUsb_ZAdrzYo_VDfyhn3bhRqK0q3KcZ7W1MKdWdgdKvwZoE2LZmw1j5kVVRuh2UkpWc0dfejnn5v3cXxVEa1nTjM3D8bEzxDS_aYHzQWHA0HLF-taXcxIT9aaKFQDbbh3snN4gCosHBet4tG28O7nj47zz66crau7NXH9QDAnhJHft69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اطلاعیه وزارت آموزش و پرورش درباره برگزاری امتحانات نهایی معوق در ۴ استان جنوبی کشور
🔴
ستاد عالی آزمون‌های وزارت آموزش و پرورش:به غایبین موجه امتحانات در دو درس تخصصی پایه دوازدهم هر رشته تحصیلی در مرحله کشوری اجازه داده می شود در امتحاناتی که مطابق برنامه ابلاغی به چهار استان جنوبی کشور در روزهای شنبه ۱۷ و سه‌شنبه ۲۰ مردادماه ۱۴۰۵ برگزار می‌شود، شرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140003" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
سرویس ترجمه Chat GPT بعد از مدت ها بصورت رسمی فعال شد و زبان فارسی هم ساپورت میکنه
🔗
https://chatgpt.com/translate
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140002" target="_blank">📅 14:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140001">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=P4tr23iRLkkMJ3PL7VaTNe8woWuO3_UGvGvaB6eav06uPYgQiswBCxxDgfn9zvUKfw7JUzi65O8AJrmbxSfF8aJXFkhfeqVoC6YXS02RnLMNimYgnMV0EQsUHU1IGjeCPZYNiS_xrpH_lQ8TooKv7AJEK22Mheuee0TyFZCflfqnGXUPdNUzL6YZqu9hxam388sK9WBXoqm0X4Slu4ej3ZZwmRWIqp3UUz4OwX9CTKTW_xZtuTjm5yg9TQu7QlnF7izzKJJ7IPUIhhl-PVIeNc0SzlqR-7gNaSIf4OAD_deJkp6x05ussnGOP4Ja6xjAfRlS2qWY6fvbUgfwwtSvVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=P4tr23iRLkkMJ3PL7VaTNe8woWuO3_UGvGvaB6eav06uPYgQiswBCxxDgfn9zvUKfw7JUzi65O8AJrmbxSfF8aJXFkhfeqVoC6YXS02RnLMNimYgnMV0EQsUHU1IGjeCPZYNiS_xrpH_lQ8TooKv7AJEK22Mheuee0TyFZCflfqnGXUPdNUzL6YZqu9hxam388sK9WBXoqm0X4Slu4ej3ZZwmRWIqp3UUz4OwX9CTKTW_xZtuTjm5yg9TQu7QlnF7izzKJJ7IPUIhhl-PVIeNc0SzlqR-7gNaSIf4OAD_deJkp6x05ussnGOP4Ja6xjAfRlS2qWY6fvbUgfwwtSvVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق گزارش رسانه‌های اسرائیلی، دو سرباز اسرائیلی در اثر انفجاری که در یک ساختمان مین‌گذاری‌شده در منطقه مجدل زون، در جنوب لبنان، رخ داد، کشته و هفت نفر دیگر زخمی شدند.
🔴
آسیب‌دیدگان به بیمارستان رامبام در حیفا منتقل شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140001" target="_blank">📅 14:45 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
