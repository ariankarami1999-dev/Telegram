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
<img src="https://cdn4.telesco.pe/file/PkUP8fUIlcEM7qBtK9mU5dC-xjhO6RTHt41ea1tuzIKXiqxf1_lE6YKUFoP8bLxoSmcZFg2zh2LLksgEcS3zWPDBb2HKoY9pttZR1SQ1kiR8zwI-LAtpmoESh0lqm9OTj9yPkKK6jERd8EF3p6vKJqBPlxk73mdaZGtpjVZaADsAR-15OMZ_NDRn6xS56XcvnQ0TIjb-EYFthbgHtOxK-bAeWAR3jLh_0NN9ALDHxw0XqWeSk0-74Nqsi1UvGqJqndVyDSTcwmQg4IQMkaw1qTChj92MwITIeNChgUPMeWliK6LkPi7RKDXsYcxQYHCHDRy3_BNYDOIZLmwl5aQdVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
<hr>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Remix Az Asemoon Dare Miad Ye Daste Hoori ~ Otaghe jang</div>
  <div class="tg-doc-extra">Yashar</div>
</div>
<a href="https://t.me/withyashar/24853" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
@withyashar
📱
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/24853" target="_blank">📅 21:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏اکونومیست: نشانه‌های نظامی از احتمال آغاز حملات در ۷۲ ساعت آینده حکایت دارد
‏اکونومیست با اشاره به داده‌های ردیابی پروازها از تجمع کم‌سابقه هواپیماهای سوخت‌رسان در پایگاه العدید و اعزام هواپیماها و یگان‌های جستجو و نجات رزمی به شرق منطقه خبر داده است. بر اساس این گزارش، هواپیماهای شنود و جنگ الکترونیک آمریکا نیز فعالیت گسترده‌ای در منطقه دارند. تحلیلگران نظامی مورد استناد این گزارش، این آرایش نیروها را نشانه آمادگی برای آغاز احتمالی حملات در آینده نزدیک ارزیابی کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/24852" target="_blank">📅 20:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک‌تایمز: مذاکرات آمریکا و روسیه برای پایان جنگ اوکراین شامل یک معامله چندمیلیارددلاری مانند رشوه برای خرید دارایی‌های نفتی لوک‌اویل شده است؛ معامله‌ای که می‌تواند به نفع دو گروه تجاری خاورمیانه‌ای مرتبط با خانواده جرد کوشنر و استیو ویتکاف باشد. این توافق به تأیید آمریکا و کرملین نیاز دارد و پوتین در دیدار با ویتکاف و کوشنر آن را مطرح کرده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/24851" target="_blank">📅 20:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4d2ebd7d.mp4?token=uFwvqZ8BtQunrhWmj3Wtahg5APqVeNcRyaXJE-WObn0xceA9QoHaEUJ6p4V4j-bx6KT4BJqZqN9ZVpp7Mihj4zeae2cJ4tDCWVFaBOX2vGG-ioOoWnc86WkB5RBvKr3BJE3NGrEu-yxquYTZaNleHrkfUPE6aREsOdf6A39dzxZH6NhhiByidr5UW0yelVC6N6Y-L365F5CCXA8XriT-oAym6TXweo5_xrozYj1NSBP-1c73VTYAwbweK-QT76qM_RtVNBa3ZSZ2wBpdxNZBULAUk9T3kLaxX_cOksl9IgSmyc1iXeugiCXkrmYQztDIoA5tCuazxQoxC0IgQ19rXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4d2ebd7d.mp4?token=uFwvqZ8BtQunrhWmj3Wtahg5APqVeNcRyaXJE-WObn0xceA9QoHaEUJ6p4V4j-bx6KT4BJqZqN9ZVpp7Mihj4zeae2cJ4tDCWVFaBOX2vGG-ioOoWnc86WkB5RBvKr3BJE3NGrEu-yxquYTZaNleHrkfUPE6aREsOdf6A39dzxZH6NhhiByidr5UW0yelVC6N6Y-L365F5CCXA8XriT-oAym6TXweo5_xrozYj1NSBP-1c73VTYAwbweK-QT76qM_RtVNBa3ZSZ2wBpdxNZBULAUk9T3kLaxX_cOksl9IgSmyc1iXeugiCXkrmYQztDIoA5tCuazxQoxC0IgQ19rXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/24850" target="_blank">📅 20:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزیر جنگ آمریکا: حجم نفت که امروز از تنگه هرمز عبور می‌کند، بیشتر از حجم آن قبل از آغاز درگیری‌ها است
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/24848" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نفتکش «اور وینست» هنگام ورود به تنگه هرمز، ظاهراً تحت اسکورت نیروی دریایی آمریکا بوده و نفتکش «آتیناگوراس» با پرچم یونانی نیز در حال خروج از عمان بوده و با ترانسپندر خاموش (AIS) وارد خلیج فارس شده است که گویا هر دو مورد هدف قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/24847" target="_blank">📅 18:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/24846" target="_blank">📅 18:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24845">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزارت خارجه آمریکا: نمی‌خواهیم درباره احتمال دست داشتن تهران در حادثه هواپیمای فلای‌دبی، پیش از پایان تحقیقات اظهارنظر کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/24845" target="_blank">📅 18:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تلگراف:
خاورمیانه در آستانه دور جدید درگیری نظامی گسترده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24844" target="_blank">📅 18:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آکسیوس درباره وزیر خزانه‌داری آمریکا: ما در جنگ خود با ایران به سیاست "دیوار آهنی" و تحریم‌ها و محاصره روی آورده‌ایم، سیاستی که واشنگتن قبلاً هرگز آن را اجرا نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24843" target="_blank">📅 17:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادعای الجزیره:
سوریه و ایران در حال نزدیک شدن به یکدیگر هستند!
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24842" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این دوستم تهیه کننده آخرین فیلم «رمبو» یعنی «آخرین خون» هست یه فیلم هالیودی از انقلاب بعد میسازیم اتاق جنگم توش باشه
😂
🙌🏾</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24841" target="_blank">📅 17:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24840">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3bf49b39.mp4?token=AvFOgelvbtNJ_wa3aebKeTrRbLKlQojIslg3JRYkXlba-wsg9ghuPnxYT7e-zJKgHTgZ7d5MfDBn6kDBYTLzXiWfYCFFISDMNi6wpU1j0Fg7cGMOcTxfPIwh4SiZKSbKkrhl3d3xbSivrJjaKSt5nC7JY9jmdEqzr-h_R7Qps6iiL5l1KoRSOZE-vbONzSiH5M86TNYXpUPZCfupsUIefQb3lGNHl_ouP56q0w9yhdaXHZ6QGmKsXs3jbzNKbBSThPS_ohR0lh6Gf5Ua9-eL2u1HkmbmC835hQT8KmiAORCUXHb8eIAKESC3Crp4S85iLI03VQtDKb5-11Fu9UlV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3bf49b39.mp4?token=AvFOgelvbtNJ_wa3aebKeTrRbLKlQojIslg3JRYkXlba-wsg9ghuPnxYT7e-zJKgHTgZ7d5MfDBn6kDBYTLzXiWfYCFFISDMNi6wpU1j0Fg7cGMOcTxfPIwh4SiZKSbKkrhl3d3xbSivrJjaKSt5nC7JY9jmdEqzr-h_R7Qps6iiL5l1KoRSOZE-vbONzSiH5M86TNYXpUPZCfupsUIefQb3lGNHl_ouP56q0w9yhdaXHZ6QGmKsXs3jbzNKbBSThPS_ohR0lh6Gf5Ua9-eL2u1HkmbmC835hQT8KmiAORCUXHb8eIAKESC3Crp4S85iLI03VQtDKb5-11Fu9UlV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24840" target="_blank">📅 17:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سلامتی همگی‌مخصوصا بهترین آرزو برای کنکوری ها
🥂
اگه خراب کردین هم که سال دیگه دانشگاه های بین‌المللی باز‌ میشه
😁
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24839" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24838">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhtx-97gYR06YSc879fN_2DNS1_0mNMs3GsU8leUscO0fxVKvaGx1MwoscPoo-Nli8_Zsym-UGhhJSvVmHvxbidX4LuMuyYIijTfDMkDuYssENEcwKSUZXMLUf4xbBqwtN605_QEv0Vdywmp3aydR0dT3cfOLsDSdYC9eB2vS8YsQJrDDIO0M_x9LH2L0aXcL9Uh8v2W4yxTZdD1RYRBaa1YXDdW-xf0qJn_n_fzReCch_uI5RjiRzqL4WyVs_BlzdN5QjUvWMQZbCNMGaP0EyJ0JZzl7qF0pSb_D_uDZYCgvKMgaivFstsgUpvblAYz-4EPHOc1gTsbbWtSmji-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : رژیم یه پهپاد زد سیریک ولی آمریکایی نیست @WarRoom
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24838" target="_blank">📅 15:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلار ۲۷۱،۰۰۰
یورو ۳۰۵،۰۰۰
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24837" target="_blank">📅 15:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیدبان اتاق جنگ : رژیم یه پهپاد زد سیریک ولی آمریکایی نیست
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24836" target="_blank">📅 15:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2207daf642.mp4?token=nXRmYBXuIdRzju0Qm8-f5dZYc6PPwlGIVsebCHpQJA6KKhb9CvSwoXEsLfjCuYP-BoMZMRMcY7FYC4ZGO1N1LYAurxSTbheaHvycDsN7TygNhTTzinXdVE5cm21yUwiD3JfsA_kSG3QLbNc5KUvDcuil1h_oTFj3PKzWL60zpsFdc3NJqYpnHaxV00chKyH7D2nFbyWHWKDIqV2ndALEt6EC2HwTY7j1Dj5vbS1TsXQnp2Da02iLspzLMMrer3iF8YkzEZ7qGfkP0u1QiqplTsm_owpkwfq9HKCJau6Wxy56P477Adq0DD4xyjo72sTK5Hfngy2GIu85cifremn6BCezrkb422xsNApLAxnWgikyu2HZk1QVtsUj--WdtFE_WBrVDG3BiX4i4N9rBbDATYhQH6qlGEJCUsPfC8ocVT1RHd7BnLRt908HveSe6MKloxzURqaK_dD4NY_ZC47aDw6YWOdFq-AiOxPlaKE1tCYwDqdDUxWR7zZVIjDiIor3O_g3GwHiW3eAISEGpebNGeop4RspoGWJAncqN5K7b7BR8DwMpwnjzEvU5vA6J4QhUMWeeEOCu2YCBljmMllzyhTtwbUZ8JDUz7G3RgMLJ-triDmcd9LCzaUJCK3-FHF_LtPDPnXtH9TLofNxHCVk5v_C1sNuNg5YiS3a-61v9V0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2207daf642.mp4?token=nXRmYBXuIdRzju0Qm8-f5dZYc6PPwlGIVsebCHpQJA6KKhb9CvSwoXEsLfjCuYP-BoMZMRMcY7FYC4ZGO1N1LYAurxSTbheaHvycDsN7TygNhTTzinXdVE5cm21yUwiD3JfsA_kSG3QLbNc5KUvDcuil1h_oTFj3PKzWL60zpsFdc3NJqYpnHaxV00chKyH7D2nFbyWHWKDIqV2ndALEt6EC2HwTY7j1Dj5vbS1TsXQnp2Da02iLspzLMMrer3iF8YkzEZ7qGfkP0u1QiqplTsm_owpkwfq9HKCJau6Wxy56P477Adq0DD4xyjo72sTK5Hfngy2GIu85cifremn6BCezrkb422xsNApLAxnWgikyu2HZk1QVtsUj--WdtFE_WBrVDG3BiX4i4N9rBbDATYhQH6qlGEJCUsPfC8ocVT1RHd7BnLRt908HveSe6MKloxzURqaK_dD4NY_ZC47aDw6YWOdFq-AiOxPlaKE1tCYwDqdDUxWR7zZVIjDiIor3O_g3GwHiW3eAISEGpebNGeop4RspoGWJAncqN5K7b7BR8DwMpwnjzEvU5vA6J4QhUMWeeEOCu2YCBljmMllzyhTtwbUZ8JDUz7G3RgMLJ-triDmcd9LCzaUJCK3-FHF_LtPDPnXtH9TLofNxHCVk5v_C1sNuNg5YiS3a-61v9V0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت: «ما از این درگیری با ایران عبور خواهیم کرد. فکر می‌کنم عرضه نفت بیشتر خواهد شد و قیمت نفت
به‌مراتب پایین‌تر خواهد آمد
. افزایش دستمزدها نیز ادامه خواهد داشت، چون ما شاهد
رونق دوباره بخش تولید و صنایع کارخانه‌ای
در آمریکا هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24835" target="_blank">📅 15:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وال‌استریت ژورنال : نفت برنت در پایان معاملات هفته حدود ۱۰۲.۲۵ دلار و وست‌تگزاس اینترمدیت حدود ۹۱.۱۱ دلار در هر بشکه بسته شد. بازار همچنان تحت تأثیر حملات نفتکش‌ها، احتمال تشدید جنگ ایران و آمریکا و تصمیم گروه هفت برای آزادسازی ذخایر قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24834" target="_blank">📅 15:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24833">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رویترز: ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که در منطقه هرمز مستقر است، در وضعیت آماده‌باش قرار گرفته. رویترز در گزارشی از داخل ناو نوشت خدمه در جریان هشدارهای اضطراری خود را برای عملیات احتمالی آماده می‌کنند؛ این ناو حدود ۵ هزار نیرو دارد و مأموریت آن در منطقه زمان پایان مشخصی ندارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24833" target="_blank">📅 15:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24832">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیگه عادی شده آژیر نداره
😂</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24832" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش صدای انفجار قشم احتمالا از تنگه @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24831" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش صدای انفجار قشم احتمالا از تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24830" target="_blank">📅 14:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الجزیره: حمله هوایی هدفمند اسرائیل به یک آپارتمان مسکونی در غرب شهر غزه. @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24829" target="_blank">📅 13:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d07a84855.mp4?token=NIQhUrgl_0D-M9f8kuysRhE2mt2WUM8_oVp-FSwXJTQxnfpMujVtYIF0YBLZTC6NcOYoc5w_mYTK9dY5P1Li6nii9aidsmPivUBPPO86NBXenkCge_IeNvXI6z9hm_EjLddCoOLTLTgEtCN3e6FP_YGF3yQDCDdN7QisU1hf-gjOlCV22SVbiFVJRL2yapgPUFGPtMCLVDNgNJYb52GfcQyME5M2IKBQ9qZBL5XekqPgZL3kHs88q6LS1HSG1_vg4DzYC_vVXuvNZC5PZ6M4O-nvJDhFT7nspDhGqZpSWuo1_Cp16joi4Gf2MNaD-TTMEI2xHTTauP5bloQS5I86fxCPSJfNDulYi8xhcrZyulfD97V8dxLH9PPUU85DTCs793k_HQQyDXCtHY3Pq_OgVlOIjmexR7VYjxXN7QobRDtdZnn07aM8Nsc5_iZYUUpJjizuO2JPSGL_NP4GkwsVWxHJu8LWJzUsNA6cOMAQ5igFOuBMi10ezVZKIeByJ6AmP-3fN2BB1RGE7_yqGvX92xPytpkh-G42iRkZ7LYyGoO-bH4jVAuq1fG-O5MVT4UcbogVr8KzzO7YEUGe957FmrDGZPK57rKXzXBXWSodV-zEsXoOhlFYf-MIDEaMZ0lhAzV7OqZ2FDtuFJBOv2pWenj_NE0rPK1qJ-zh8ss6ltc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d07a84855.mp4?token=NIQhUrgl_0D-M9f8kuysRhE2mt2WUM8_oVp-FSwXJTQxnfpMujVtYIF0YBLZTC6NcOYoc5w_mYTK9dY5P1Li6nii9aidsmPivUBPPO86NBXenkCge_IeNvXI6z9hm_EjLddCoOLTLTgEtCN3e6FP_YGF3yQDCDdN7QisU1hf-gjOlCV22SVbiFVJRL2yapgPUFGPtMCLVDNgNJYb52GfcQyME5M2IKBQ9qZBL5XekqPgZL3kHs88q6LS1HSG1_vg4DzYC_vVXuvNZC5PZ6M4O-nvJDhFT7nspDhGqZpSWuo1_Cp16joi4Gf2MNaD-TTMEI2xHTTauP5bloQS5I86fxCPSJfNDulYi8xhcrZyulfD97V8dxLH9PPUU85DTCs793k_HQQyDXCtHY3Pq_OgVlOIjmexR7VYjxXN7QobRDtdZnn07aM8Nsc5_iZYUUpJjizuO2JPSGL_NP4GkwsVWxHJu8LWJzUsNA6cOMAQ5igFOuBMi10ezVZKIeByJ6AmP-3fN2BB1RGE7_yqGvX92xPytpkh-G42iRkZ7LYyGoO-bH4jVAuq1fG-O5MVT4UcbogVr8KzzO7YEUGe957FmrDGZPK57rKXzXBXWSodV-zEsXoOhlFYf-MIDEaMZ0lhAzV7OqZ2FDtuFJBOv2pWenj_NE0rPK1qJ-zh8ss6ltc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو به دیلی میل : «ائتلاف اسلام‌گراها و چپ‌گراها در حال مطرح کردن این اتهامات هستند؛ در حالی که این دو گروه اساساً باید مخالف یکدیگر باشند. چون اسلام‌گراها چه کار می‌کنند؟
همجنس‌گرایان را به دار می‌آویزند و زنان را از حقوقشان محروم می‌کنند.
آنها مردم خودشان را در غزه، لبنان و ایران می‌کشند و مخالفانشان را اعدام می‌کنند. اینها در نقطه مقابل دموکراسی‌ها قرار دارند.»
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24828" target="_blank">📅 13:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دلار ۲۶۸،۰۰۰ تومان ( رکورد تاریخی )
@WarRoom
🚀</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24827" target="_blank">📅 12:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تا آخرین لحظه حیات
از آن چیزی‌که تا به حال‌بودم تغییر نخواهم کرد! و اگر تا به اینجا با حمایت شما رسیده ایم  , مسلما به فروپاشی این رژیم هم خواهیم رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24826" target="_blank">📅 12:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرگزاری صداوسیما:
دقایقی پیش در مقابل ساختمان دادگستری شهرستان مهاباد تیراندازی رخ داد.
این حادثه پس از مشاجره لفظی میان چند زن و با ورود مردی مسلح به سلاح کمری و شلیک گلوله اتفاق افتاد. مرد مسلح به سمت زنان نزدیک شده و تیراندازی کرده است. تاکنون جزئیاتی درباره
تعداد مصدومان یا تلفات احتمالی، وضعیت افراد حاضر، هویت تیرانداز و انگیزه او
منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24825" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTNiPI57PrSBNfbOH_X84_gQmVvaOlV0zyZOEApdvYoRnLGXb7sPe8TVPF_c3HB_K7CBS-ydKyhis_tdYnCuf_VAO6LLIsd-2ouDna8cth0T8O3CxCfIH4qCyUBG15YVLQ_jx5Ls786ogW-4NxLr2zDEcK75PQA8r2VbNwKpT3wWmdXp_6hJtm750CNyZGh-q3S9ZeAzrmbAURn75CAsYBLfSlHZu7ibQfLm7HhTEk_iS29NOvfsTYBT05Ou6wPCK8weXRspnoa90hO_DxhJWzRhOSH4TqtcKCuxDjlUMH-4p13F54DDyawpnd2A4lhfOSXu4MP4WzdvF8jhbP4ANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابودی پارک جنگلی چیتگر در سه دهه
این پارک در دهه چهل و در دوره پهلوی ساخته شده بود و ۶۰ سال قدمت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24824" target="_blank">📅 11:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار کانال ۱۲ : گزارشها حاکی از این است که کمک‌خلبان، شهروند عمان، با یک تبر سوار هواپیما شده بود. @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24823" target="_blank">📅 10:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آکسیوس به نقل از سه مقام آمریکایی: مقام‌های ارشد دولت آمریکا در کمپ دیوید برای بررسی اقدامات بعدی درباره ایران و انصارالله تشکیل جلسه دادند. یک مقام آمریکایی گفت در این نشست «تصمیماتی گرفته شد یا دست‌کم موضوعات به‌طور جدی مورد بحث قرار گرفتند». جی‌دی ونس ریاست…</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24822" target="_blank">📅 10:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRWjbf6LcWz3Z084e-uXGtjoSsixrmw5-L_Y0JtHwIAzEqeOGVmzlX3Nsx76jTaGQmI3J_TmnIbfFdqopWUTKnNZ-YqJa4Isg1rqw_ihroWAq7t4ApxGrhNzyIc1cDDJDi_zr-G39Q0H01xnsQDwCXH9544LX-K5O9C7UUp6RfIFnp7ryNrvR5x6Dggar_rg3AMuWS7kMPz-ndw3sjV9tzSzdMmsew9StXdqeyE9twx6se02P3bVlgvNmtFTxWGOwa1T7NXZBAFlugc-u_vgyYo7IxjIS6VrYoISwLj-544zjyjeca_e5gHQR2tj6KfIxpijKrev6ewpV5rutto8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه افغان نیروی قدس سپاه پاسداران از کشته‌شدن یکی از نیروهای تیپ فاطمیون خبر داد. او در اثر انفجار بمب کنار جاده‌ای که در زاهدان، استان سیستان و بلوچستان، در جنوب‌شرق ایران کار گذاشته شده بود به هلاکت رسید؛ این حمله احتمالاً توسط گروه‌های بلوچ انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24821" target="_blank">📅 09:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f878b1ca.mp4?token=O-d46NsMAEIZj52b-6v3MUDYJlQmEiPkhkwLZubk4PMUscthgvhdzJih7YoJWhCdzYtOD6zffzOHrc1Hex5wRFtsbQ4bU8OxGCjz1D2AdPik7zxq0_ic2xnqB9jORdiBPls0eLALFNsnKsl7NUXHfsDpC9w4DxbWl_g2in_XRS4cBUEcMeQGLTEXKD_yig-TjQDIKuG873nsGvAPqvIrNjHo1Nd4LX4LJZOl9jX_fffXa72VYJGB1nn7-qxtIMDLxgYj946GPVAyNHY4lJxlMkLdhzBNruhjr9F89oHf2usTGPvdMBSISsCYh7-Fn_J7HCcssMIBn09Uzs48eSI1QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f878b1ca.mp4?token=O-d46NsMAEIZj52b-6v3MUDYJlQmEiPkhkwLZubk4PMUscthgvhdzJih7YoJWhCdzYtOD6zffzOHrc1Hex5wRFtsbQ4bU8OxGCjz1D2AdPik7zxq0_ic2xnqB9jORdiBPls0eLALFNsnKsl7NUXHfsDpC9w4DxbWl_g2in_XRS4cBUEcMeQGLTEXKD_yig-TjQDIKuG873nsGvAPqvIrNjHo1Nd4LX4LJZOl9jX_fffXa72VYJGB1nn7-qxtIMDLxgYj946GPVAyNHY4lJxlMkLdhzBNruhjr9F89oHf2usTGPvdMBSISsCYh7-Fn_J7HCcssMIBn09Uzs48eSI1QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «من گروهی از مردم را دیدم که اسمشان «همجنس‌گرایان برای فلسطین» است. یک روز آنها را بفرستیم تا بروند مذاکره کنند. دیگر هیچ‌وقت آنها را نخواهید دید. آنها کارهایی انجام می‌دهند که باورکردنی نیست.»
@WarRoom
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24820" target="_blank">📅 09:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Auk-kEcfSVzxh9UXPEJlzKtNdd6F07nGAodzan-lIo_Fl6KhjEfdsIe3FjFZ7gYPmwFMsqrBcRQOFhBk_LGZ-BSw6x1Vf5oZ6XkqIpy1Dg0UxUo4fFS52Hq5PrExGbmho7QcTaxVDLPwps1KhfOcZZPEilSBZKN9CMDNmHb4De6Fi-FzOIVL-yE5-l6lCcdKhKM1i6EdxCw5mG08XA7pao4TaCuuxtKcZqRUfQdFVKU6tI9Rtkz9496DpCj1ghYqLa7q5QVD1PTw77VV6c_3a6OaSqtx9cEVhOkRWDo58kX4y4zYdKPUBAzT7AICWs-nBoW_Gex337Hsmlz0_uxYQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی اعلام کرد حکم
سیاوش جمشیدی
که در جریان اعتراضات دی ماه ۱۴۰۴ بازداشت شده بود به اتهام استفاده از اسلحه در‌اعتراضات شهرکرد ، بامداد امروز ۱۱ مهر اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24819" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24818">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس به نقل از سه مقام آمریکایی: مقام‌های ارشد دولت آمریکا در
کمپ دیوید
برای بررسی اقدامات بعدی درباره
ایران و انصارالله
تشکیل جلسه دادند. یک مقام آمریکایی گفت در این نشست «تصمیماتی گرفته شد یا دست‌کم موضوعات به‌طور جدی مورد بحث قرار گرفتند».
جی‌دی ونس
ریاست جلسه را بر عهده داشت و
مارکو روبیو، پیت هگست، ژنرال دن کین، جان رتکلیف و استیو ویتکاف
نیز حضور داشتند.
آخرین بار که چنین نشست مشاوره‌ای برگزار شد، ژوئن ۲۰۲۵ و پیش از آغاز جنگ ۱۲روزه اسرائیل بود.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24818" target="_blank">📅 09:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پدافند غرب تهران بدجور زد !
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/24817" target="_blank">📅 04:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شنیده شدن صدای تیراندازی یا پدافند از شهریار و اندیشه کرج
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/24816" target="_blank">📅 04:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/24815" target="_blank">📅 04:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f241181503.mp4?token=tomB3OwZwtmlMiyWDWsd4pRC498iqjh_vXmuw5KB1VrGbFDkne7mkEq533Dk0Wi55cGVJz56m_tBIgvcUpJ49wmyhH1i21wFSZgxdFQgol-ki5KS-Prm0_pWoz4yTnqO5P0KZOkxriu9rzLmdLaZh910jyk3ntrK4RKmzShVCQAxLAs9xjp62i6cmTYlsvMPEknyw0yY5wxBb994HPiZo9IkJuxHxrwEd-3aUFORIS2M5Z7t7d0GM_Q2IsQY4V2ekdkWwAmlYuqR3V9BIIVR1vUkXYQkDQZn1apH8T-pLIjXZKIepqaZuPEkijXWa91n8w8ejDYuNb5cU2yVZf_lUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f241181503.mp4?token=tomB3OwZwtmlMiyWDWsd4pRC498iqjh_vXmuw5KB1VrGbFDkne7mkEq533Dk0Wi55cGVJz56m_tBIgvcUpJ49wmyhH1i21wFSZgxdFQgol-ki5KS-Prm0_pWoz4yTnqO5P0KZOkxriu9rzLmdLaZh910jyk3ntrK4RKmzShVCQAxLAs9xjp62i6cmTYlsvMPEknyw0yY5wxBb994HPiZo9IkJuxHxrwEd-3aUFORIS2M5Z7t7d0GM_Q2IsQY4V2ekdkWwAmlYuqR3V9BIIVR1vUkXYQkDQZn1apH8T-pLIjXZKIepqaZuPEkijXWa91n8w8ejDYuNb5cU2yVZf_lUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «یکی از بدبختی‌هایی که داریم ، کسی نیست که با باهاش مذاکره کنیم. هیچ‌کس نمی‌خواهد رئیس‌جمهور باشه ، جدی‌ میگم : «الان با چه کسی در ایران صحبت کنم؟» تق‌تق! کسی خانه نیست.»
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/24814" target="_blank">📅 03:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8addbc83.mp4?token=HvnynOH95GF5No8ukTapoDOqWc0mfD2ZxmwaVmdTTv3HdRat4HDWp7o4EgHhNHLoxqhJzdKbCZi3orlpAMNYmP5PtzD7wm2hQOvzyQqonmmE66K329T5vkc89TAhhjd8sGH6-fUwa4uBp7luw6jxkQkdf3nBs0WIpEaKdSCqjrFrFYSiU70ak6t1kWgKI77h8uTGt7kzXgLkeGCt5aXkoIsb7xk1v1lmcSFoPLaRvZGPD7-bm4hK8BWRmgZXGdUkD8PIV7PN90t3XY4URP9c4Y37QmTvjghhRfxFuy3KSUDQ_CJ5HcwpY9aWmi8SNqpGU_YRFxU_KqgcFgF8ZlpTaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8addbc83.mp4?token=HvnynOH95GF5No8ukTapoDOqWc0mfD2ZxmwaVmdTTv3HdRat4HDWp7o4EgHhNHLoxqhJzdKbCZi3orlpAMNYmP5PtzD7wm2hQOvzyQqonmmE66K329T5vkc89TAhhjd8sGH6-fUwa4uBp7luw6jxkQkdf3nBs0WIpEaKdSCqjrFrFYSiU70ak6t1kWgKI77h8uTGt7kzXgLkeGCt5aXkoIsb7xk1v1lmcSFoPLaRvZGPD7-bm4hK8BWRmgZXGdUkD8PIV7PN90t3XY4URP9c4Y37QmTvjghhRfxFuy3KSUDQ_CJ5HcwpY9aWmi8SNqpGU_YRFxU_KqgcFgF8ZlpTaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «ایران برای ریاست‌جمهوری شورا برگزار کرد، اما هیچ‌کس در آن شرکت نکرد. همه می‌گفتند: «ما نمی خواهیم»
@WarRoom
یاشار : فکر میکنم منظورش به همون خبر استعفای پزشکیانه و بعد کسی حاضر نشده کاندید بشه. برای همین با استعفاش موافقت نشد.</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24813" target="_blank">📅 03:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f8e97b36.mp4?token=vC-h8ZnTuBS_bEs-umNf7rtjd9AlHQgtSKQDXo-TWjpitF30164akiALswKjyhooKZefeFfqaPWDKSmcA6-2zGf3iZCG7zQx93n8yJQ8D9PQIroP-2HDbduyrlEFada7opynNZLCvtrjHknfccC5HHKsmh2qtT2CuH3lxLAqHgffod9ZHrriJKhMql90zkGqqyx6Wp5XqgvzhxrKcVV8UCYb15vkfHB9K8pcdH-eYVZbnVTtXWRUG7DiNfnvEyZlK8dW4q2vmfFLpEdboo0wJkdcoDqGZABXgz0ZoWpi3SpB3llR9JiLsGnHlguhf0CJpnOoXSinGInSBVAM1IpPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f8e97b36.mp4?token=vC-h8ZnTuBS_bEs-umNf7rtjd9AlHQgtSKQDXo-TWjpitF30164akiALswKjyhooKZefeFfqaPWDKSmcA6-2zGf3iZCG7zQx93n8yJQ8D9PQIroP-2HDbduyrlEFada7opynNZLCvtrjHknfccC5HHKsmh2qtT2CuH3lxLAqHgffod9ZHrriJKhMql90zkGqqyx6Wp5XqgvzhxrKcVV8UCYb15vkfHB9K8pcdH-eYVZbnVTtXWRUG7DiNfnvEyZlK8dW4q2vmfFLpEdboo0wJkdcoDqGZABXgz0ZoWpi3SpB3llR9JiLsGnHlguhf0CJpnOoXSinGInSBVAM1IpPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «اگر دروغ بگویم، به من پینوکیو می‌گویند. من دروغ نمی‌گویم.»
@WarRoom
یاشار : خیلی خوبه این بشر
😂</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24812" target="_blank">📅 03:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f2bfed07.mp4?token=hbvg30e1KUXYMDCv6KA8j_IUcK9GYZNy9h273MSYTO7UfJ-sza78xjktGVD0cPNnMgLcwXBFT_k0kpMGWlywvEJcBKgcQGAKDgV0SRzsMZoy64l6ozB3fWhMMQSXjlWm1Db1jcdexMdN1_ExB0fRAy_CKpB7U0U8xB1VLQjKqbxnQDC1kWfI4vw_fhb14HPGtvi3STje00uJKRGnxkgzhv8uBDeCJUaM0mb7yxTKI34Rh31XzcFFo_bptyoAi3HkDA5rwgHJV2qJGPUYaqI49L3C9_laz8jk2-mrWLs0P3BqbTLfiQbQKj6BU-T9e_W2rEVoMWh3U1Mp0lOLZYIVAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f2bfed07.mp4?token=hbvg30e1KUXYMDCv6KA8j_IUcK9GYZNy9h273MSYTO7UfJ-sza78xjktGVD0cPNnMgLcwXBFT_k0kpMGWlywvEJcBKgcQGAKDgV0SRzsMZoy64l6ozB3fWhMMQSXjlWm1Db1jcdexMdN1_ExB0fRAy_CKpB7U0U8xB1VLQjKqbxnQDC1kWfI4vw_fhb14HPGtvi3STje00uJKRGnxkgzhv8uBDeCJUaM0mb7yxTKI34Rh31XzcFFo_bptyoAi3HkDA5rwgHJV2qJGPUYaqI49L3C9_laz8jk2-mrWLs0P3BqbTLfiQbQKj6BU-T9e_W2rEVoMWh3U1Mp0lOLZYIVAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «احمق! همه‌شان فکر می‌کنند کلمه Dumb حرف B ندارد.» (ترامپ با بازی زبانی به تلفظ واژه Dumb اشاره می‌کند؛ حرف B در نوشتار وجود دارد، اما در تلفظ خوانده نمی‌شود.)
@WarRoom
یاشار: همون‌جور که می‌بینی ترامپ هم اونور دنیا با این احمق‌ها درگیره. واقعاً احمق زیاده.</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24811" target="_blank">📅 03:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0v-KLPWXXMWJ-g0r8NnGpN5VpcCsHqGSWL932yyWxb6vKc0PIhoetst3OzME2mI3NyZR1_XIndRB3OhgyyLWxf4J6wxM_1k6hygtEXdQoIsbJufzxHODJbg6ZMIKcUysn_Go1wsEqlgB7MCP-FSQ90RzbXMO9vF-q-V2NS9g7PPH7ASWf1tzYPqlEr-NWRHDD7AhxpNJBaQoXX8I3HfDSKpIIOrg1lBIWEaw35blwO9hEwOCduFSG_BT7i5f5bcmPn6V9TPcBr8rsok0DPGzjWjIYg6BEn0-PIR3aFKqEDGPdxMdmBkeivWK0YWFtyZoicBBGuwBB3271duSKySOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش حامل نفت خام در حدود ۴ مایل دریایی شرق عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت.
تمام خدمه در سلامت هستند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24810" target="_blank">📅 03:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24809" target="_blank">📅 03:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24808">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24808" target="_blank">📅 03:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الجزیره: حمله هوایی هدفمند اسرائیل به یک آپارتمان مسکونی در غرب شهر غزه.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24807" target="_blank">📅 02:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24806" target="_blank">📅 02:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24805" target="_blank">📅 01:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24804" target="_blank">📅 01:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24803" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24802" target="_blank">📅 01:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کره شمالی موشک بالستیک پرتاب کرد. پدافند ژاپن در حال رصد تحرکات است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24801" target="_blank">📅 01:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSfpY8wjomeSTZkEghvrSP3OMx3ZPYtCzmP8UHnmyscCPySn0oaBaQM5bivNhIQ_F8e0v4lsjPThKo_h5SPLNrYG-5qRWz3FuBXLiNNQs9bvrvIf2_agBkmJ98pt27jhd63j_ux-BuMjwmRmkA1NSG4DRRWDisxU0IBtNi2Aoh-R2l6ZQJhKoRKWI1lqrPfetBTanQP-Pvsxh_fPffiq2VNhRfTk58YASvA7EeRTj-YbjbwdWIQtzb5e65b799WqFf-gmWUSOidgPw7qW4Ls_oAUNl8u6kUrEnAbuFksj8qUXwbHeG0OvmX1sX1k1gr-MdMfyHUhpm9Ma1DYpnKqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع العربیه: کمک‌خلبان عمانی مرتبط با حادثه پرواز فلای‌دبی «همام الهمامی» نام دارد. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24800" target="_blank">📅 01:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منابع العربیه
: کمک‌خلبان عمانی مرتبط با حادثه پرواز فلای‌دبی «همام الهمامی» نام دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24799" target="_blank">📅 01:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24798">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نظر مارک بر اینه تو این ۲۴ ساعت آینده میزنه انگار</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24798" target="_blank">📅 01:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دلار داره موشکی‌میره بالا
🚀</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24797" target="_blank">📅 01:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چنتا کانفیگ فروش دایرکت دادن برای تبلیغات
😂
😂
میگین به جایی ‌وصلن ؟</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24796" target="_blank">📅 01:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24795">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چنتا کانفیگ فروش دایرکت دادن برای تبلیغات
😂
😂
میگین به جایی ‌وصلن ؟</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24795" target="_blank">📅 00:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وال‌استریت ژورنال:
کمک‌خلبان عمانی پرواز FZ1073 فلای‌دبی که متهم است به خلبان هواپیما چاقو زده و باعث سقوط شدید هواپیما شده،
قبلاً در عمان از پرواز کردن منع شده بود
؛ دلیل این تصمیم، نگرانی‌ها درباره گرایش او به دیدگاه‌های افراطی عنوان شده است. با وجود این ممنوعیت، او بعداً توسط فلای‌دبی استخدام شد و در مسیر حساس
امارات به اسرائیل
پرواز می‌کرد. هنوز مشخص نیست عمان این نگرانی‌ها را با کشورهای دیگر یا شرکت‌های هواپیمایی در میان گذاشته بود یا نه.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/24794" target="_blank">📅 00:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟ ترامپ: خب، اگر به شما بگویم، یک خبر بزرگ خواهید داشت، درست است؟ اما خودتان خواهید دید؛ همه‌چیز خیلی خوب پیش می‌رود. ایران وضعیت خوبی ندارد. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/24793" target="_blank">📅 23:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24792">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ee0bbd03.mp4?token=cNdFT_nJde8VuHMP6W5aAK3edHil6Yg-5YEsJKAkdH9FVB6jW1UQ-_1UeKUL2ebmi8YKpx8Zt2LM68VQ12IjuFdMKGii0Q1MiHrGTSAh-NfxVAv4qEa1dVAF5JWQG_0MMJJCyglPyxV_2BWkZ3nu8mLl18udcM4_2J_o-H-5xalUNR6BxezISJbsbrFnG-sKQIikR4BD5bfiYa4mVbA7lF41_W5s44N2Vnxbf66GCsGdOY436vrKzQEJ6Hhk4yZghvyZTYw1HWRRXFzg46ETD9L5jf3l5jpUIrZPOSfNxMmBWKOFsB4J_rqNiDsqTo5HKMQh5hmWFtkGXfVgbpzjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ee0bbd03.mp4?token=cNdFT_nJde8VuHMP6W5aAK3edHil6Yg-5YEsJKAkdH9FVB6jW1UQ-_1UeKUL2ebmi8YKpx8Zt2LM68VQ12IjuFdMKGii0Q1MiHrGTSAh-NfxVAv4qEa1dVAF5JWQG_0MMJJCyglPyxV_2BWkZ3nu8mLl18udcM4_2J_o-H-5xalUNR6BxezISJbsbrFnG-sKQIikR4BD5bfiYa4mVbA7lF41_W5s44N2Vnxbf66GCsGdOY436vrKzQEJ6Hhk4yZghvyZTYw1HWRRXFzg46ETD9L5jf3l5jpUIrZPOSfNxMmBWKOFsB4J_rqNiDsqTo5HKMQh5hmWFtkGXfVgbpzjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
گام بعدی شما در قبال ایران چیست؟
ترامپ:
خب، اگر به شما بگویم، یک خبر بزرگ خواهید داشت، درست است؟ اما خودتان خواهید دید؛
همه‌چیز خیلی خوب پیش می‌رود. ایران وضعیت خوبی ندارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/24792" target="_blank">📅 23:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پلیس ضدتروریسم بریتانیا :‌
امروز
دو شهروند ایرانی،
سلام احمدیان ۳۶ ساله و رحمان صالحی ۳۴ ساله
، به اتهام آماده‌سازی برای انجام یک عملیات تروریستی علیه جامعه یهودیان در منچستر متهم شدند. این دو نفر
۲۹ شهریور
در منچستر بازداشت شده بودند. پلیس می‌گوید آنها با یک
طرف امنیتی ثالث خارج از بریتانیا که احتمال می‌رود در ایران باشد
در ارتباط بوده‌اند و تحقیقات درباره این پرونده ادامه دارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24791" target="_blank">📅 23:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جروزالم پست: ایهود باراک، نخست‌وزیر پیشین اسرائیل، مدعی شد نتانیاهو ممکن است برای به‌تعویق انداختن انتخابات، زمینه یک جنگ جدید را فراهم کند. باراک گفت اگر شرایط سیاسی برای نتانیاهو نامساعد باشد، آغاز یک درگیری تازه می‌تواند برگزاری انتخابات را به تأخیر بیندازد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24790" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزارت خارجه آمریکا: در بیانیه‌ای مشترک به مناسبت سالگرد اجرای تحریم‌های «مکانیسم ماشه»، آمریکا و چند کشور دیگر بار دیگر بر تعهد خود برای اجرای محدودیت‌های سازمان ملل که از طریق این سازوکار علیه ایران بازگردانده شده‌اند، تأکید کردند.
این کشورها همچنین از ایران خواستند به تعهدات خود در زمینه منع اشاعه پایبند باشد، با آژانس بین‌المللی انرژی اتمی همکاری کامل داشته باشد و نگرانی‌های بین‌المللی درباره برنامه‌های هسته‌ای و موشک‌های بالستیک خود را برطرف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24789" target="_blank">📅 23:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24788" target="_blank">📅 23:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/24787" target="_blank">📅 22:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24786" target="_blank">📅 22:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گویا معین هم اعلام کرد بر میگرده بزودی @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/24785" target="_blank">📅 22:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزارت خارجه بریتانیا: آمریکا، انگلیس، فرانسه و آلمان در بیانیه‌ای مشترک اعلام میکنند که متعهد به جلوگیری از تأمین هرگونه مواد، تجهیزات و فناوری برای ایران هستند که بتواند در فعالیت‌های هسته‌ای مورد استفاده قرار گیرد. این چهار کشور همچنین بر ضرورت همکاری کامل ایران با آژانس بین‌المللی انرژی اتمی و اجرای تعهدات پادمانی تأکید کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24784" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آکسیوس به قلم باراک راوید:
چرا واشنگتن و تهران مدام حرف یکدیگر را نمی‌فهمند؟آمریکا و ایران هر دو می‌گویند راه‌حل دیپلماتیک را به جنگ ترجیح می‌دهند، اما رسیدن به توافق از همیشه دشوارتر شده است. ریشه اختلافات در چهار موضوع است: واشنگتن توافقی سریع و بزرگ می‌خواهد، در حالی که تهران مذاکره طولانی‌تر و توافق‌های محدودتر را ترجیح می‌دهد؛ بی‌اعتمادی عمیقی میان دو طرف وجود دارد و هرکدام نگرانند طرف مقابل از مذاکرات برای آماده‌سازی اقدام بعدی استفاده کند؛ فشارهای سیاسی داخلی در آمریکا و ایران نیز مواضع دو طرف را سخت‌تر کرده است. در ۱۸ ماه گذشته، دو دور مذاکرات شکست خورده و هر دو بار پس از شکست مذاکرات، درگیری نظامی شدت گرفته است. اگر تلاش فعلی هم به بن‌بست برسد، خطر آغاز دور تازه‌ای از جنگ طی چند هفته وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24783" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏امیر قاسمی و رو‌کردن نام کسانی که با سپاه در ارتباط کامل قرار دارند ، آیا نفر بعدی که در ایران خواهید دید معین است؟ گزارشهایی هم هست که در کنسرت اخیر معین اجازه ورود پرچم شیر و خورشید داده نشد و فقط آهنگی برای ایران خوانده شد و در نمایشگر هم پرچمی نمایش داده…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24782" target="_blank">📅 22:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0950d9a5.mp4?token=mM6Lv26VsY7xI4JGiD3Xwj9LoXOTzOlAPOq1uk_In_d8C__OOcvwYGHV-D8ywR1qQcRtj0geP1QOqdRblKZ0pUYkY17wlMS5wNgUQFUz4AADG30FSX6Vx-SvJDUIgNdymnr3xhnThfSHbGdl2dI-YK4ao-_jmrXRI-ZljqCbbINhEBJ4m3JIXlxi4A6PqYOgcAa__tDaZ3RTmN7u4Ml5JTu0LkH6qCtSSTzCnBwVUvqd78fRGFAzUmymDgLQBetINzNn97VSeJeBlkOmmN365OLocSLpW7P_D-ERjEHS59k844C1oSoJStdWKAJUwoQDw7mgY1Bv5P1jZlxgW9sDtLAw7kmq7_LeCqP-bd8e7LWWVwEg80NjcGFgncgqiHIaR-8l7vuzJgyH-V_au5dK3mHwosAsDbuFhzgmy7P6L9NILX16sM6oPJX4U_P8LZsvh8uQdUhl8N2B3PplyJWyA2By4rvv6jSlFKxdJpl0BpquZ39si_2y6JOPDD4wouSH0E4nGHXrUJC1L4l_Mfe2ZOQzAof5xDHjZbAU0ERP5oajIpwb_ZYiEZ1Du5sFG86XfwgaJDL5nOehQyTjOMP7Owg8xvU19x1vM39nTqRmuu1hPQdBnfHOrbFKJins-b1bfg7KkNsZVYJLN_eH_2N1GJU5T_l4et76Ddm35ZR_Uvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0950d9a5.mp4?token=mM6Lv26VsY7xI4JGiD3Xwj9LoXOTzOlAPOq1uk_In_d8C__OOcvwYGHV-D8ywR1qQcRtj0geP1QOqdRblKZ0pUYkY17wlMS5wNgUQFUz4AADG30FSX6Vx-SvJDUIgNdymnr3xhnThfSHbGdl2dI-YK4ao-_jmrXRI-ZljqCbbINhEBJ4m3JIXlxi4A6PqYOgcAa__tDaZ3RTmN7u4Ml5JTu0LkH6qCtSSTzCnBwVUvqd78fRGFAzUmymDgLQBetINzNn97VSeJeBlkOmmN365OLocSLpW7P_D-ERjEHS59k844C1oSoJStdWKAJUwoQDw7mgY1Bv5P1jZlxgW9sDtLAw7kmq7_LeCqP-bd8e7LWWVwEg80NjcGFgncgqiHIaR-8l7vuzJgyH-V_au5dK3mHwosAsDbuFhzgmy7P6L9NILX16sM6oPJX4U_P8LZsvh8uQdUhl8N2B3PplyJWyA2By4rvv6jSlFKxdJpl0BpquZ39si_2y6JOPDD4wouSH0E4nGHXrUJC1L4l_Mfe2ZOQzAof5xDHjZbAU0ERP5oajIpwb_ZYiEZ1Du5sFG86XfwgaJDL5nOehQyTjOMP7Owg8xvU19x1vM39nTqRmuu1hPQdBnfHOrbFKJins-b1bfg7KkNsZVYJLN_eH_2N1GJU5T_l4et76Ddm35ZR_Uvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترابری سنگین نظامی آمریکا از ۲۴ ساعت پیش تا دقایقی قبل…
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24781" target="_blank">📅 21:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس انجمن صنفی تولیدکنندگان شیرآلات: اگر محاصره دو ماه دیگر ادامه پیدا کند کل کارخانه‌های شیرآلات تعطیل خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24780" target="_blank">📅 21:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رویترز: عربستان در حال آماده‌سازی برای آغاز حمله‌ای جدید علیه حوثی‌ها در یمن طی هفته‌های آینده است؛ هدف این حمله بازپس‌گیری کنترل تنگه باب‌المندب و تأمین امنیت کشتیرانی در دریای سرخ است که با حمایت اطلاعاتی آمریکا همراه خواهد بود @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24779" target="_blank">📅 21:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24778">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdT4UY6NyN2OqqSSeD2S06OHBxbrLShzrW61LsnkeMN0A6wah-G2xS0h1-RwsuM4x7ia0fvzKBIjsO0ajV_YkXJP4eQP6WPIUameEUlYqH_Alv8aNZvfTontcQXlRSrU4bJNrTqh_8hP4u22AU9hZhY3iuKMg8nMrb0AQ7cz-UPbdESMOCtu4lvqrN8ZOfmCZtuo51ZhndPBiB0ioY3qmqdbvShOWG7boRGNnvicZxvysgmkqee1BAl4HdMtb3wFwzfVO09sbrb2qeQzbJ6ur1jnJYxoekfDNrp2TXmKiKc6Mu4BDTlBa-ishq0w9o1vRpynWI6BEqTbzFhyuvlkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ پی-۸ پوسایدون ، ۵ سوخترسان ، ۱ هرکولس و ۳ هواپیمای ترابری سنگین سی۱۷ هم اکنون در محدوده خلیج فارس و همچنین سوخترسانی هم از اسرائیل به سمنت منطقه می آید
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24778" target="_blank">📅 21:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز: عربستان در حال آماده‌سازی برای آغاز حمله‌ای جدید علیه حوثی‌ها در یمن طی هفته‌های آینده است؛ هدف این حمله بازپس‌گیری کنترل تنگه باب‌المندب و تأمین امنیت کشتیرانی در دریای سرخ است که با حمایت اطلاعاتی آمریکا همراه خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24777" target="_blank">📅 20:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3w_U5ahEbJgIwd3z3Ymc64_cDtHeR2Rs_2Of7BBosKt9YaWncZMb0XEdWdqwnqHAl6h_NgAj_c0OJyXQhGVwq0ja23X5-R9GlE4c_XQdz7D9ALjHHYRgqttn7qT_RcXbBcRm8sXFfPmvgWaoAF9jnobD5-hE6Aq902GWzgTk6DEuCe2n_E6Atb0IokZSccNA6HFEWdrdUjoppkrToubBdFT-gmlTdELnEmN4dsp3Oz7VHR_7ARhO1meEjLtbUWkR1pdvLfE8IIgL0GvvHDgMxb1PChBbAZUtkwv3CXc8LNvBGgWGzL3Xs_qOQZmAzuPl0lsOjaTGKdsc5gQgjIjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان نظارت دریایی بریتانیا اعلام کرد که ناخدای یک تانکر نفتی گزارش داده است که این کشتی در حین عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
یک آتش‌سوزی کوچک و قطعی برق به طور موقت رخ داد، اما آتش‌سوزی خاموش شده و کشتی در حال حرکت است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24776" target="_blank">📅 20:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24775">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کوین‌دسک:
سیتی‌گروپ هدف ۱۲ماهه بیت‌کوین را به ۱۱۳ هزار دلار و هدف اتریوم را به ۳٬۰۲۸ دلار افزایش داده است.
این اهداف، پیش‌بینی بانک هستند و قیمت تضمین‌شده محسوب نمی‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24775" target="_blank">📅 18:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c6ae3f3.mp4?token=PSO3vqYcffn3O1TTDhI4C0MlxG_HOwMwZTsGo4KPVbPTNHHfT_7W7S3CQ2DH6_-vxK38PPz14SIADulBu2iGkM-nPMxwObdK8OSV6c0hGXRoWeApjO3BR8pvnZD_g3UMiAZP-h59oLf9MW6BiHZER0ZQHGYMQ8MjTW3c-qxpQahTBvODXjtOM2B0peM5rlBSpQOsJ78DI3OzOipJnBoF3CSJJ9ija7-_9i3FlopRoG4CIfS4ctPqrsXmNTSjeL35pTk43yxpC82XicilxmT32w6eH_o52Obt3zJ96lp7C05yIrW826Wwo-K0xR5kLaFbnGwN8-IS9nQkixKSlSXkEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c6ae3f3.mp4?token=PSO3vqYcffn3O1TTDhI4C0MlxG_HOwMwZTsGo4KPVbPTNHHfT_7W7S3CQ2DH6_-vxK38PPz14SIADulBu2iGkM-nPMxwObdK8OSV6c0hGXRoWeApjO3BR8pvnZD_g3UMiAZP-h59oLf9MW6BiHZER0ZQHGYMQ8MjTW3c-qxpQahTBvODXjtOM2B0peM5rlBSpQOsJ78DI3OzOipJnBoF3CSJJ9ija7-_9i3FlopRoG4CIfS4ctPqrsXmNTSjeL35pTk43yxpC82XicilxmT32w6eH_o52Obt3zJ96lp7C05yIrW826Wwo-K0xR5kLaFbnGwN8-IS9nQkixKSlSXkEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الکس پیلیتساس
(
تحلیل‌گر امنیت ملی آمریکا، کارشناس ضدتروریسم و افسر سابق پنتاگون
) در سی‌ان‌ان بخوبی استراتژی جمهوری اسلامی رو توضیح میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24774" target="_blank">📅 18:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHpHARRZGcqiEQ60K4R6dLV3flzZFaF4rfstiaAO4RLqiGkh34kmzJKb-lXmMIO2C4iyJRTGjaYe_DhTRimUUuHUYVSDLrxhiTO-DI5c1u_141ZnGtvE_P3xkXrYWeNPHfSuUWR9cWW8zxL4TJc6XY9aglrJE3womnLP4SZFDwnVy1H23sU-v0rBb_PnXbAZK2DKeYrZHDOA6qEvyOBL9QzGxKsjtroArzuVOXbYcgImbk9l069pROZiYN4AcqBLXPPI_ALSpAY9DWUqnZTQc7vjqZRv_rxIJQKX7iaAW-znYXYEufLQyYhM0bLYgTGbsTYaXaUhndjSAhtby8HAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الناز شاکردوست به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس و دو سال محرومیت محکوم شده است. وکیل او گفته این حکم صرفاً به دلیل انتشار یک استوری پس از حوادث دی‌ماه سال گذشته صادر شده و محتوای آن تنها بیان اندوه بابت جان‌باختن جوانان ایران بوده است. به گفته وکیل شاکردوست، در این نوشته هیچ اشاره‌ای به نظام، حکومت یا مسئولان و همچنین هیچ فراخوانی برای اقدام جمعی، فعالیت سازمان‌یافته یا براندازی وجود نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24773" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b731ebb6ee.mp4?token=mN0ghwBoIlJgeFv0i8m8Nvm4rJOedRBNHCbDAYApGJCAlphCHFuAHsrg5EzHFG5p6PyFRMC2RKe50DOJyf_CovYe5F-2INPdWtccKHashzOfH_t4FnOZT_1qdU88QkgQeM_SZo_NL9zggdC2MLGpDcZF_8kMLeOXcO986Ot8T4PGBTu40GpMxMiqAa02rCGN3jM2MljizsO_LcYhRnWzh_yNFX_ct5LdtDC7Wy1R0PeFGXp_jd5DQahGDrXbs5mFYCgbZzig8y6AXnB-AmNJCZQ5XGrRp6-wFKAb9CL0CMhUrLnsKfNep7oxoog3dgVCc9-0FvZs3H-iO3zZYdgB3y3yhjXGjylQrYjlBj_CVta15m4sXZb29JH4P1UekIk6Cd1Ldc9a1LVGOzZoUjOl-FDhugN_TYuuMFw4-KfDEQbGreqzpK8zhNFEmW7UuFqMiGx9Ajy_Qs1gDjODhKgIlwpHlMfQVLFBKOlD8MHOs8CVr_JOnnCHZxF12_rewKio1krb1WnI0FaFnMnI2ST49alp2wwiLwlLuG5RdZe6nLrMwZV187H0PoAPyg4hErreyJUNeuJDEouO4k4NQKYwayLUafoZQPoEJQhX_2amyI7Ed5yoZWHZcTQRhb9zCY8E12VwYJpkyHODtqaFP_41pYX58xpuC5H_7CMe00gfyZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b731ebb6ee.mp4?token=mN0ghwBoIlJgeFv0i8m8Nvm4rJOedRBNHCbDAYApGJCAlphCHFuAHsrg5EzHFG5p6PyFRMC2RKe50DOJyf_CovYe5F-2INPdWtccKHashzOfH_t4FnOZT_1qdU88QkgQeM_SZo_NL9zggdC2MLGpDcZF_8kMLeOXcO986Ot8T4PGBTu40GpMxMiqAa02rCGN3jM2MljizsO_LcYhRnWzh_yNFX_ct5LdtDC7Wy1R0PeFGXp_jd5DQahGDrXbs5mFYCgbZzig8y6AXnB-AmNJCZQ5XGrRp6-wFKAb9CL0CMhUrLnsKfNep7oxoog3dgVCc9-0FvZs3H-iO3zZYdgB3y3yhjXGjylQrYjlBj_CVta15m4sXZb29JH4P1UekIk6Cd1Ldc9a1LVGOzZoUjOl-FDhugN_TYuuMFw4-KfDEQbGreqzpK8zhNFEmW7UuFqMiGx9Ajy_Qs1gDjODhKgIlwpHlMfQVLFBKOlD8MHOs8CVr_JOnnCHZxF12_rewKio1krb1WnI0FaFnMnI2ST49alp2wwiLwlLuG5RdZe6nLrMwZV187H0PoAPyg4hErreyJUNeuJDEouO4k4NQKYwayLUafoZQPoEJQhX_2amyI7Ed5yoZWHZcTQRhb9zCY8E12VwYJpkyHODtqaFP_41pYX58xpuC5H_7CMe00gfyZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مرد فرهیخته ، ژنرال جک کین : مبارزان ایرانی در گروه‌های متعددی سازماندهی شدند و میخواهند مسلح شوند تا کشورشان را پس بگیرند ، هم مسلح کردن ایرانی‌ها لازم هست هم اقدام نظامی شدید در لحظه مناسب بخصوص بعد از فروپاشی اقتصادی
گزینه توافق و دیپلماسی کاملا کنسل است
‏این رژیم باید سرنگون شود..
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24772" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ در‌تروث : «اروپا به‌تازگی با آزادسازی حجم عظیمی از ذخایر بسیار زیاد دیزل خود موافقت کرده است. این روند بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24771" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شبکه 14 اسرائیل: ما رهبر ایران رو وسط تهران کشتیم و هزینه خاصی هم پرداخت نکردیم. اون مرکز رنج ما بود.  ما فکر میکردیم ایران کار دیوانه واری انجام بده ولی فقط 40 روز جنگید و بعدشم به توقف جنگ رضایت داد. دو دهه الکی ترسیده بودیم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24770" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ: مأموران سرویس مخفی به من گفتند به‌دلیل بدی آب‌وهوا احتمالاً باید سفر به اوکلاهما را لغو کنیم؛ نه هلیکوپتر می‌توانست پرواز کند و نه هواپیما. گفتند تنها راه، یک رانندگی طولانی است. از آنها پرسیدم «بیست با چه سرعتی می‌تواند حرکت کند؟» گفتند نزدیک به ۱۰۰ مایل بر ساعت.
گفتم: «پس سریع باسن تپلتون رو بزارین تو ماشین و راه بیفتید!»
این سفر آسانی نبود، اما نمی‌خواستم مردمی را که ساعت‌ها برای دیدنم در اوکلاهما منتظر مانده بودند، ناامید کنم.
@WarRoom
👏</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24769" target="_blank">📅 17:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4d8b2843.mp4?token=fK8DzZTlyzfgMva4-CjWkozvH22AIQPWnho9KMIZSgCn44jYTKZN4aeprhRXjYCztf3VAIbnsaG82aayq6k4HQPRhyeAwYRsI6zUvBKZafTvgJZ-MUt4OvPRZGE4Bgix7eWrVy0oGa7js_NswxTkLn-YJzT_UjcnswoZgmM15IFk1Qi0gqJUzv1GoJIExQhTYm4uYcctiYTlKjV_3U4KuO0XUD2HSt3IrhRsAVj4MTJ2BuiYZ3ehhBWUtlx6ivLAVPlAux4PkinOk3JbQ4DW_L-v379zta__dlMNeOjOLow6Pvvm0xi2Bkx8JgkALzlrtk6C5-FOtdOMnEyeycdsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4d8b2843.mp4?token=fK8DzZTlyzfgMva4-CjWkozvH22AIQPWnho9KMIZSgCn44jYTKZN4aeprhRXjYCztf3VAIbnsaG82aayq6k4HQPRhyeAwYRsI6zUvBKZafTvgJZ-MUt4OvPRZGE4Bgix7eWrVy0oGa7js_NswxTkLn-YJzT_UjcnswoZgmM15IFk1Qi0gqJUzv1GoJIExQhTYm4uYcctiYTlKjV_3U4KuO0XUD2HSt3IrhRsAVj4MTJ2BuiYZ3ehhBWUtlx6ivLAVPlAux4PkinOk3JbQ4DW_L-v379zta__dlMNeOjOLow6Pvvm0xi2Bkx8JgkALzlrtk6C5-FOtdOMnEyeycdsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
«هر چه زمان می‌گذرد، تصویر واضح‌تر می‌شود. این عمل، نتیجه‌ی افراط‌گرایی اسلامی بود و هدف آن، سرنگون کردن هواپیما به همراه تمام مسافرانش بود.ما در حال بررسی این موضوع هستیم که آیا این فرد برای انجام این کار اعزام شده بود یا خیر، و هر کسی که مسئول این اقدام باشد، باید پاسخگوی عواقب بسیار سنگینی باشد.»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24768" target="_blank">📅 17:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرمانده انتظامی رشت اعلام کرد یک روحانی در یکی از محله‌های این شهر توسط فردی ناشناس با سلاح سرد مجروح شده است. به گفته سرهنگ عیسی روشن‌قلب، پلیس در جریان تحقیقات به سرنخ‌های مهمی درباره ضارب دست یافته و تیم‌های تخصصی با هماهنگی مقام قضایی برای دستگیری او تلاش می‌کنند. وضعیت فرد مجروح مساعد اعلام شده و پلیس گفته علت و انگیزه حمله پس از دستگیری متهم و تکمیل تحقیقات مشخص خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24767" target="_blank">📅 17:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رعد ‌و برق در تهران ، نترسید
@WarRoom
🫂</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24766" target="_blank">📅 16:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ در ‌تروث: «با خوشحالی اعلام می‌کنم توافق با کره جنوبی هر روز بهتر می‌شود! ۸.۴ میلیارد دلار برای یک پروژه افزایش برداشت نفت اختصاص داده شده است. تولید بیشتر نفت و گاز یعنی تقویت سلطه انرژی آمریکا و تضمین امنیت انرژی در جهان برای آینده.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24765" target="_blank">📅 16:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو: ترامپ از من پرسید «این قدرت را از کجا می‌آوری؟» به او گفتم: «این قدرت، میراث پدران ماست که از پدران به پسران و نسل‌های آینده منتقل شده است.» @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24764" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c997284691.mp4?token=SIRyb0YOUZaLhEcCEZJHmJrZ81xkV_mjELDiBGD3BLAB8UlolJ-2dYZOrzSdzMEyXv8wRBHUDq1BY3lmcFKo9R0-MBIWEULJ-TF_-jVzWCe3h1ckXquWZjj8RuRMSScK1yx7SAz7wrb35FHrev8QCpLm8AyWtP5PbHOOrKv1xuvK-ByWe14hmy1ErzREridOLa3DdeBvSCi_dVtJfBoUFSo4M3c-3B56jCAiq5DhaKUMdnBobKH1hTDdRBoNY54n9mQSZxZOs5VpDjU9sL0EOlwiFVeyYo-aPfWjzN5IT0ue67PHDX_2QwNzHsBITVDjn9OTjInbF1UsSbpOohNovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c997284691.mp4?token=SIRyb0YOUZaLhEcCEZJHmJrZ81xkV_mjELDiBGD3BLAB8UlolJ-2dYZOrzSdzMEyXv8wRBHUDq1BY3lmcFKo9R0-MBIWEULJ-TF_-jVzWCe3h1ckXquWZjj8RuRMSScK1yx7SAz7wrb35FHrev8QCpLm8AyWtP5PbHOOrKv1xuvK-ByWe14hmy1ErzREridOLa3DdeBvSCi_dVtJfBoUFSo4M3c-3B56jCAiq5DhaKUMdnBobKH1hTDdRBoNY54n9mQSZxZOs5VpDjU9sL0EOlwiFVeyYo-aPfWjzN5IT0ue67PHDX_2QwNzHsBITVDjn9OTjInbF1UsSbpOohNovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: ترامپ از من پرسید «این قدرت را از کجا می‌آوری؟» به او گفتم: «این قدرت، میراث پدران ماست که از پدران به پسران و نسل‌های آینده منتقل شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24763" target="_blank">📅 16:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تتر ۲۶۳،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24762" target="_blank">📅 15:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24761" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41835d5d95.mp4?token=BhhXwjBqKuOZvLnly9CZFtVPr7QJva414Nv9anjOtuj14oRf-wuHbTa0yiR8MYRvp2sOTM4hEDCuFK1dsN7DBMPB2onR5W6nFD0EPnxTbAXwW6SxdiUKf9o06EjIro0H3d3EtyPu_X9PbvQzoEQnNn-8euD012KAxiaA6x4N_e5e-zhubfsglLYaeCANmKt8g9LhbvfB8gKop8E4r8hg1uGS1NwRWgke_cOtaGMYJbaAYE65TE7-WDWEfw6s9YsW_amVtL-khJPn3croGaYSFpjOIEwxOLSD3BvSPA6K5T92gPhZxNkmPw5S_iGvB57Ne26Hkv1VjfVM8LxODhHCOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41835d5d95.mp4?token=BhhXwjBqKuOZvLnly9CZFtVPr7QJva414Nv9anjOtuj14oRf-wuHbTa0yiR8MYRvp2sOTM4hEDCuFK1dsN7DBMPB2onR5W6nFD0EPnxTbAXwW6SxdiUKf9o06EjIro0H3d3EtyPu_X9PbvQzoEQnNn-8euD012KAxiaA6x4N_e5e-zhubfsglLYaeCANmKt8g9LhbvfB8gKop8E4r8hg1uGS1NwRWgke_cOtaGMYJbaAYE65TE7-WDWEfw6s9YsW_amVtL-khJPn3croGaYSFpjOIEwxOLSD3BvSPA6K5T92gPhZxNkmPw5S_iGvB57Ne26Hkv1VjfVM8LxODhHCOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : دیگ به دیگ میگه باسن تو سیاهه
قیصر فرندلی فایر بیژنو میزنه
😂
این قشنگه
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24760" target="_blank">📅 15:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حقیقت یاب
اتاق جنگ:
خبری که با عنوان «ارتش آمریکا رسماً تمرین تصرف و پاکسازی تأسیسات هسته‌ای زیرزمینی را انجام داد» در حال انتشار است،
خبر جدیدی نیست
و مربوط به ژوئن ۲۰۲۴ است. ارتش آمریکا اعلام کرده بود تیم «خنثی‌سازی هسته‌ای ۱» همراه با نیروهای
هنگ ۷۵ رنجر
در یک تمرین نظامی، یک تأسیسات هسته‌ای زیرزمینی شبیه‌سازی‌شده را در شرایط آتش شبیه‌سازی‌شده تصرف و پاکسازی کرده‌اند. این تمرین با هدف افزایش آمادگی برای شناسایی، ایمن‌سازی و خنثی‌سازی تهدیدهای هسته‌ای و پرتوی انجام شده بود. بنابراین انتشار دوباره این گزارش به‌عنوان یک
تحرک یا تمرین جدید آمریکا
نادرست است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24759" target="_blank">📅 15:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مرد خردمند ، مارک لوین : این جنگ هیچ‌وقت درباره تنگه هرمز نبوده؛ اگرچه حفظ جریان نفت دستاورد بزرگی است. فشار اقتصادی علیه جمهوری اسلامی بسیار موفق بوده و همچنین سایت‌های هسته‌ای و اورانیوم غنی‌شده دفن شده اند. اما تنها راه جلوگیری از دستیابی ایران به سلاح هسته‌ای، با داشتن هزاران موشک بالستیک و ادامه حمایتش از تروریسم، نابودی این رژیم است. هیچ راه خروج خوبی وجود ندارد. من همچنان خواستار
مسلح کردن
مردم ایران و
ارائه آموزش، پشتیبانی فنی و پوشش هوایی
مورد نیاز آن هستم. ما پیش از این در کشورهای دیگر چنین کاری کرده‌ایم و با توجه به ضربات واردشده به ایران، به‌ویژه فروپاشی اقتصادی، معتقدم زمان اقدام اکنون است یا دست‌کم به‌زودی فرا می‌رسد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24758" target="_blank">📅 14:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فایننشال تایمز: ترامپ در فکر حمله آخرالزمانی‌به ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24756" target="_blank">📅 14:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الجزیره  : بر اساس برنامه فعلی، نهایتاً تا پایان نوامبر ( هفته اول آذر ) آمریکا می‌تواند ۳ ناو هواپیمابر و ۲ گروه آبی‌خاکی در اطراف ایران داشته باشد.      البته خبرگزاری آسوشیتدپرس نظرش اواخر اکتبر (هفته اول آبان)است @WarRoom
⚠️
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24755" target="_blank">📅 13:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جزئیات جدیدی از دولت
ترامپ
در گزارش مجله تایم :
گروک، چت‌بات هوش مصنوعی شرکت X
، تا حدی در متقاعد کردن ترامپ برای این دیدگاه نقش داشته که
ربودن نیکلاس مادورو، رئیس‌جمهور ونزوئلا، می‌تواند میراث سیاسی او را تثبیت کند
.
در بخشی دیگر تایم گفت ، ترامپ از سوی مقام‌های ارشد مستقیماً در جریان
مشکلات مربوط به ذخایر مهمات آمریکا
قرار نگرفته و این موضوع را از طریق گزارشی در
نیویورک‌تایمز
متوجه شده است. ترامپ سپس با
پیت هگست
، وزیر جنگ آمریکا، درباره این موضوع بحث کرد و هگست او را متقاعد کرد که این گزارش‌ها
«اخبار جعلی»
هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24754" target="_blank">📅 13:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در‌ انتظار تایید : قرائتی ، ورّاج صدا و سیما ، ریق رحمت را سر کشید
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24753" target="_blank">📅 13:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtgLyJjypKXH8TXMFZWrR5IwYsEwUk1ezQteTbX1WRRz4gZfZ7ZavASWCo4VnIwfkU2tp7ci5eAQ1X327OCus92qprw6RsKgWA25xHk4MFTmA0dZyPV3RKgdkuIU5P5Jt9O2_2DRBbpOeFCVsypsDBDzIWKq_PK1UsT_sCJvQhl3JyhWym3u6vRkKxSulqc3TZYRfdn_JMqdBX9anlIrWLnzqbQYEqmKX2DQmU_d3Z1wH0yXqLxKZo4sp96IoWwb-9boV6RneXPZu6lEkbwCIxXZVsFgN_HvqG_kFvjAQQrJSHRrqVD4le5i8wPbG7zTNyxPYY_U_crFrPRznN2G7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلامیه خواهر عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24752" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
