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
<img src="https://cdn4.telesco.pe/file/Bt7SwjRJB0mBd0-Z1uyT8ePOv84wFlowqQkjcDzsq6xNNTa_SG8T5391rB5usSRSEQi16Si9DVu5u6gdI-znIVYZdjopGK2fX9NC0FkhoC35N5-XiCJ8_OvgvY2NmGF5n4OI9Mjd44E6861T5KGgkaIj4rCVOIGkTEiulaa_gjIYiH3Xa13WJSg0y98CKo21W2U5N2tuzWoxaKvsnTujTsQ1Wh0nh6ypXHiXLC31SE3obOFQ9EG_VjqVdjql6hEVh0TqXQAsV6Eb8fOb6uEwkP190peR5t85IsKYEN1sH6z011gYYYwJ11KTFXNbf93T5je7WNcpoZs0e4P_dq6WxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 08:18:32</div>
<hr>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو : هر کسی که ما را دوست نداشته باشد، آمریکا را هم دوست ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/20313" target="_blank">📅 05:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgTbJMQ8Vht8_t-4axx1py-vahyUffDyIZc4BOx2wmR2PfBuYQo1BNInEoIDl3171uAPs57NSPNLzE9P-dpXOPCIRoVw6UQBesMBBETArYUuqa3GcVEjCfTd-2XFcC3nYi9tTSIRQ2ze58hU0C8yi7ldi1vwZpb2vUqsnL5kKvwRAHkABJNNzjZzV7_DyDrRqyx7MI_1EJnwFZpWczElXdQJ8GDm8wFdWU0hqqM1bJU08BanLvudX_C0S92QzkiMo1XlQZuIdl__EOP815lFn-BB5OnMOkmZIwN-QQ4-it903vOVn6wI_nKU6LnKpNtuDIxduuMgv0NzL1yyIb1YZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین لحظه پل هوایی سنگین جهانی ، از آمریکا تا خاورمیانه.، شش سوخترسان که حتما هواپیماهای جنگنده جدیدی را از آمریکا به منطقه می آورند و همکنون در حال ورود به آسمان آتلانتیک شمالی هستند. همینطور هواپیماهای لاجستیکی سی-17 در سرتاسر این مسیر دیده میشود.
@WarRoom</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/20312" target="_blank">📅 04:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال ۱۴ :
ایران مظنون اصلی حملات سایبری به تأسیسات آب آمریکا؛ رسانه‌ها از احتمال «پرل هاربر مجازی» خبر می‌دهند
حملات سایبری هماهنگ به تأسیسات آب‌رسانی در هفت ایالت آمریکا، نگرانی‌های جدی امنیت ملی را برانگیخته است. در این گزارش ادعا شده اگر نقش ایران به‌طور قطعی ثابت شود، این حملات فراتر از یک حمله سایبری معمولی بوده و مستلزم پاسخ قاطع آمریکا خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/20311" target="_blank">📅 04:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">@WarRoom
😂
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/20310" target="_blank">📅 03:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آکسیوس: سایر قدرت‌های منطقه‌ای، از جمله پاکستان، ترکیه، امارات متحده عربی و قطر نیز بر ایالات متحده و ایران فشار وارد می‌کنند تا تنش‌ها را کاهش دهند.
واسطه‌های قطری، جلسات جداگانه‌ای با عباس عراقچی، وزیر امور خارجه ایران، استیو ویتکوف، نماینده ویژه آمریکا، و مقامات عمان برگزار کردند تا به توافقی برای بازگشایی تنگه هرمز دست یابند.
این مذاکرات پیشرفت‌هایی داشتند، اگرچه هنوز مشخص نیست که آیا این پیشرفت‌ها برای حل بحران کافی خواهد بود یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/20309" target="_blank">📅 03:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/20308" target="_blank">📅 03:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen</strong></div>
<div class="tg-text">آره یاشار تو کیش همه میگن هیچ باری دیگه از اون سمت نمیاد قراره کلا دریا تخلیه شه</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/20307" target="_blank">📅 03:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مقامات آمریکایی به Axios: ولیعهد سعودی، شاهزاده محمد بن سلمان، روز شنبه با رئیس‌جمهور ترامپ صحبت کرد و نگرانی خود را در مورد برنامه‌هایش برای انجام حملات نظامی گسترده جدید علیه ایران ابراز کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/20306" target="_blank">📅 03:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c3771c8f.mp4?token=CuZ7dNj2BkdZZvKkTq3j01gNqubBbWtgzanrbKS7yrVIG3Y6obpqlFg7BwpKKDEDXQVeMlCciOl7ZW9s0OyA6cweKgiURM6mlMtmWY6zXI20wv0D5NPBKJWcIOKrM5fEh2PGu80FjhWvV4jxrwWx5idZf5KzdXfcSOUnX14V8TJmcQMS4lkKxf9GIg_XPXUW0FsoJbAKknZCkgfuzELQeLWa8c6MmJgQLZWXENn2KwfD6OMgBmBOw2Iq7j11Hpz-D8TJok_oiGj9kwhnu0BKLpgckritVEIdTbOjtfCb-5HIvxjaJ288A0WrgSSPm-2Dza1r2715pZzWOsMMLqkbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c3771c8f.mp4?token=CuZ7dNj2BkdZZvKkTq3j01gNqubBbWtgzanrbKS7yrVIG3Y6obpqlFg7BwpKKDEDXQVeMlCciOl7ZW9s0OyA6cweKgiURM6mlMtmWY6zXI20wv0D5NPBKJWcIOKrM5fEh2PGu80FjhWvV4jxrwWx5idZf5KzdXfcSOUnX14V8TJmcQMS4lkKxf9GIg_XPXUW0FsoJbAKknZCkgfuzELQeLWa8c6MmJgQLZWXENn2KwfD6OMgBmBOw2Iq7j11Hpz-D8TJok_oiGj9kwhnu0BKLpgckritVEIdTbOjtfCb-5HIvxjaJ288A0WrgSSPm-2Dza1r2715pZzWOsMMLqkbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون فعالیت سیستم دفاع هوایی C-RAM در اربیل عراق برای مقابله با پهپاد های شلیک شده ایران
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/20305" target="_blank">📅 03:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قوانین دریایی امروز کشورهای خلیج فارس</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20304" target="_blank">📅 03:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20303" target="_blank">📅 03:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گویا لایو از سخنرانی قدیمی‌ بوده</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20302" target="_blank">📅 02:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حمله پهپادی سپاه به اربیل عراق @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20294" target="_blank">📅 01:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عراقچی گوشی رو گرفته زنگ زده پاکستان ، ترکیه ، عربستان و … نسبت حملات آمریکا هشدار داده
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20293" target="_blank">📅 01:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">همکنون هواپیماهای جنگنده اسرائیل حمله‌ای را بر مناطق شمال غربی شهر غزه انجام دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20292" target="_blank">📅 01:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز : شاهزاده رضا پهلوی : «این وظیفه یک دولت خارجی نیست که تصمیم بگیرد چه کسی یا چه چیزی باید جایگزین حکومت ایران باشد. این به مردم ایران بستگی دارد.»
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20291" target="_blank">📅 01:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مارک لوین : رژیم ایران بیش از آمریکا یا اسرائیل از قیام مردم خودش می‌ترسد
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20290" target="_blank">📅 01:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حمله پهپادی سپاه به اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20289" target="_blank">📅 01:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بیمارستان‌های اسرائیلی وارد حالت بحران و آماده‌باش شده‌اند و پرسنل پزشکی در حالت آماده‌باش قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20288" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">المیادین:اطلاعاتی وجود داره که تایید میکنه گروه های کُرد دارن توی خاک عراق خودشونو آماده میکنن تا از غرب کشور به ایران حمله کنن
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20287" target="_blank">📅 01:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کان نیوز: نیروی هوایی اسرائیل در آماده باش 100 درصدی جهت حمله به ایرانه.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20286" target="_blank">📅 01:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کانال ۱۳ اسرائیل : ترامپ تصمیم به حمله گرفته و این حملات انجام می‌شه مگر اینکه ایران لحظه آخر همه‌رو سورپرایز کنه و بیاد پای میز‌مذاکره
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20285" target="_blank">📅 00:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حساب رسمی X اسرائیل:
ما از امپراتوری‌ها جان سالم به در برده‌ایم. می‌توانیم از بخش نظرات شبکه های مجازی هم جان سالم به در ببریم.
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/20284" target="_blank">📅 22:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کانال ۱۴ : اسرائیل آلارم خطر نظامی را افزایش داد
مقامات ارزیابی می‌کنند که حمله گسترده ایالات متحده به ایران قریب‌الوقوع است.
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/20283" target="_blank">📅 22:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تتر : ۱۹۵،۶۰۰ رکورد جدید تاریخی
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/withyashar/20282" target="_blank">📅 22:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این خبر فیکه یه چنل برای تبلیغات گمراه کننده زده همه کپی کردن
نتانیاهو: اسرائیل به زودی به همراه آمریکا دروازه‌های جهنم را برای آنها باز خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/20281" target="_blank">📅 22:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fABh0Qpt3ee1XUkULR0U2OqLoEUd95L2gZ2FsVdnvA9rkUAJgwT_rdwTMZ35tvt0Z3yuOvGFq48U7_TwXoCojDiDDZTFXDG_Rf4Oc8Qk0cHBloK3UeHcRGiO4PSaKnOvLBJ3NdTtVxp5v14fsx-k1WEJpIBwfVWqk8ixoPSAndVGp22UDOZvbYOldbGOKGPrC4n3q-_zOARnNe8V1RE9O5ixg3NhL8sv4fWpQWln_Z4HxbtXuP5pVDUz8xRdL57ml0ZHHBob5Ha2XmkziqONGgDvH1zjUdwzfAW7LwnhktANLoN58_S2kFY0WIBZHCLGyAms7Q1C_iakgWqvR7kdPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث : در حال نابودی کامل ارزش پول ایران هستم. در شروع دوران ریاست جمهوری من دلار ۹۰ هزار تومن بوده؛ الان شده ۱۹۰ هزار تومن.
@WarRoom</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/20280" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEsU6GxDoHjqvWd3o8koeFajvxr32a82V8xRC8T-bNmrjCJYTrovrqYyrGoOA5siwF9E3upFPu9I-W9r1QYNMuzmc0J5qIxPuHVFk-a0QXUyQuQPIOnWImgWmMfqD-ve-Y66Q7gtDJHeNuA-nOjdI9rFVspwMAX1GAS-5jSpj-Ay-zaBX7PKZhby0QnpVePeKf6DipgY2rjPL7yTbFW20YGiCqn431NTK7bwuJGEG3S3A6DqNc-nQ2AlEWpPFxvsSHJhuBpRS4zDFhMQzDVrfNYX10NMft09I4MesezShJZ8Nd4UgibGuuChFvxHCZN5wi2E5GMeZ2aFHEtmjSucUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما آدام فضایی را به مقام انسانیت می‌رسانیم
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/20279" target="_blank">📅 21:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۳  به نقل از مقام‌های ارشد:
انتظار می‌رود ترامپ دستور ازسرگیری درگیری‌ها را صادر کند و آن‌ها ساعات آینده را “بسیار سخت و بحرانی” توصیف می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20278" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844f298602.mp4?token=seJO8LRUxXQKGsh4jYc0NUNEsfgxVAYvBTUJm3IGzdznLhGIWWzeE-pZ32kz0YkZZoRirnS8Gsv-zSWhBDpQuuuTyJFic5iRTu50zxiYN0DVfKkL1lIRnOoXEh2cPpsreBnfS3EfA-OFninIyTeVcHu8eW4zMPCZQUTXCC6TFQmGu8HZzqeaF5T_C35PrZJEzRDshVkihWICAyotW29g1hyucIBCYjT5GO1zSMp2JPJWPS0PXRKtfTK4_ibOeA--5G5oNPxkhgO9PgyCmIc5KLY6xzpoSRTuL7cRLb1OyiEpICvgNUsC5whhv8v11Skn64wxG5xy5fGkh7e8c1XCow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844f298602.mp4?token=seJO8LRUxXQKGsh4jYc0NUNEsfgxVAYvBTUJm3IGzdznLhGIWWzeE-pZ32kz0YkZZoRirnS8Gsv-zSWhBDpQuuuTyJFic5iRTu50zxiYN0DVfKkL1lIRnOoXEh2cPpsreBnfS3EfA-OFninIyTeVcHu8eW4zMPCZQUTXCC6TFQmGu8HZzqeaF5T_C35PrZJEzRDshVkihWICAyotW29g1hyucIBCYjT5GO1zSMp2JPJWPS0PXRKtfTK4_ibOeA--5G5oNPxkhgO9PgyCmIc5KLY6xzpoSRTuL7cRLb1OyiEpICvgNUsC5whhv8v11Skn64wxG5xy5fGkh7e8c1XCow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قطر در حال میانجیگری بین جمهوری اسلامی و آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/20277" target="_blank">📅 21:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">واشنگتن‌پست به نقل از یک مقام آمریکایی: کشورهای خلیج فارس ، به رهبری قطر، در حال مخالفت با تجدید جنگ با ایران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20276" target="_blank">📅 21:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شبکه ۱۲ اسرائیل گزارش داد که نهادهای امنیتی اسرائیل خود را برای دو سناریو آماده می‌کنند: یا ایران ابتکار عمل را در حمله به اسرائیل در دست بگیرد، یا دونالد ترامپ به اسرائیل برای مشارکت در حمله چراغ سبز بدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20275" target="_blank">📅 20:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">@WarRoom
shabbat shalom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20274" target="_blank">📅 20:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اسرائیل حالت فوق‌العاده اعلام کرده است. یک مقام اسرائیلی در یک نشست خبری با رسانه‌های خارجی گفت: "ما منتظر چراغ سبز هستیم."
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20273" target="_blank">📅 20:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال ١٢ اسرائیل : مقامات اسرائیلی معتقدند که حملات دقیق و هدفمند به تاسیسات کلیدی می‌تواند تاثیر قابل توجهی بر رهبری ایران و افکار عمومی داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20272" target="_blank">📅 20:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک منبع آگاه به i24NEWS گفت: "ترامپ صبر خود را از دست داده است، نتیجه نهایی در آخرین لحظه اعلام خواهد شد"
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20271" target="_blank">📅 20:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9YE6F0MgGx2vKZqaN-yHIjw4Zpy7IX9qSW88-yMuK-rWx-DrFGnm-3ppEb0aHVUE2C3pLWiY1Iij3l2Dq3lR_PvQs4wMdVnIzpHTWp0j_gYvTJPiJ2HZlUZiXu62P0wmAmEcN1JrigaOf-ltzvE9BSpylfyRsvPGJFqrH08Upkb8xr-COW0AdKaEEklI5qCPu9n4ZUh1Lww-Ma_nhZGtMERzZXyRC5yOIdz0uQc8FrWtfblgBtnbf3ebzPrrLzesHqgUF_5aXmOIEVavo6zOXFSJUmWilRaJtKZKi46eXM048qdj5ba5I5P-34h4_cnsq5TVx8Glxn60r006BrQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام با انتشار عکس از یک هلیکوپتر شینوک دو ملخه که مخصوص عملیاتهای نیرو زمینی است، در حال نشستن در یک مکان خشک بیابانی‌مانند جنوب، پشت یک سیم خاردار که نماینگر یک مرز است، تصویری نمادین و سیگنالی از حمله زمینی قریب الوقوع داده.
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20270" target="_blank">📅 20:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20269" target="_blank">📅 20:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانال ۱۲ اسرائیل: یک مسئول اسرائیلی گفت که ایالات متحده از هر زمان دیگری به تجدید جنگ علیه ایران نزدیک‌تر است.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20268" target="_blank">📅 20:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کاخ سفید : خداوند سربازان ما را حفظ کند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20267" target="_blank">📅 19:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۴ : صدای چندین انفجار در کویت شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20266" target="_blank">📅 19:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیروهای قدس , برون مرزی سپاه : مجتبی دستور اجرای مجموعه‌ای از حملات پیش‌دستی علیه کشورهای منطقه را صادر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20265" target="_blank">📅 19:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزارت امور خارجه آمریکا: ایران و گروه‌هایی که از آن حمایت می‌کنند، ممکن است منافع آمریکایی یا شهروندان آمریکایی را در سراسر جهان هدف قرار دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/20264" target="_blank">📅 18:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9dba0c46.mp4?token=DiojRTUE-g8oIaFKF7huf_gx-kmcv80n3_gvWe3dTKhbzWMaLv52Dfu62Kj5OSrgv8Y88AL0OmrJSNfvsHLPtmofC3s3Wznp-J30vrBe5UMOjKyJSyksFMolOcAU_Qcj8VJjNTdvH9lr7mNcxr_yR7smjf15l8o13CZttv73ijpWjgNF4n_KCEWw-kinPUwU2o7RSR3GWNggrU1qpMzfgdgVT6bGHGgss6c1HzmSEUUL9MBRnJ02dWTdp5hT8eDV7pXKHGc9ti8YB8Zt-xlH4ghm6JyXQd696rFGWp5fssrqLcM4FPPzKsoL_TIRAk7n-Y0Pv6jDkIEZnnaqyHj4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9dba0c46.mp4?token=DiojRTUE-g8oIaFKF7huf_gx-kmcv80n3_gvWe3dTKhbzWMaLv52Dfu62Kj5OSrgv8Y88AL0OmrJSNfvsHLPtmofC3s3Wznp-J30vrBe5UMOjKyJSyksFMolOcAU_Qcj8VJjNTdvH9lr7mNcxr_yR7smjf15l8o13CZttv73ijpWjgNF4n_KCEWw-kinPUwU2o7RSR3GWNggrU1qpMzfgdgVT6bGHGgss6c1HzmSEUUL9MBRnJ02dWTdp5hT8eDV7pXKHGc9ti8YB8Zt-xlH4ghm6JyXQd696rFGWp5fssrqLcM4FPPzKsoL_TIRAk7n-Y0Pv6jDkIEZnnaqyHj4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عروسک های ترامپ و پوتین در کارناوال آمستردام ۲۰۲۶ در نقش کاپل همدیگر را بوسیدند
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/20263" target="_blank">📅 18:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ساعاتی پیش سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از یک حادثه در فاصله ۱۱ مایل دریایی در شمال‌شرق لیما، عمان دریافت کرده است. افسر ارشد ایمنی (CSO) یک نفتکش گزارش داده که این شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به اتاق…</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/20262" target="_blank">📅 17:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سی‌بی‌اس به نقل از یک مقام دولتی:
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/20261" target="_blank">📅 17:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta5Y0wySJOainI0xM61VwLLY212BJFUSnbZ4ATy8s755yPHzc4dI321EoS9G98v_Bi124n08WlIhzevqDfDqwIdMS1xQNQt8YPxygpb1ik6NCe_9j4RxVa6x15AnBFo_IOqRjlJyUlObIJOo4795gOiPVx02PgQdI6TFnK_Y-6tkGkgqmhXwx4hZjC4t3izZxdV96YbX2vqcynGlDNEFzhOgDy8l_lAZrQzz8OJDVbzWQm-gM7R38ebR3hGPXRzOjbAMXuQ-B5NA1V4Ll9yvg8BCA6f443-y7BU95emc4UTUPsE0L8g1fsjrfp-PjlYTXRGSt8ipB0RH2521VzgaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان شیراز - صدرا
@WarRoom</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/20260" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH7NeZj1Tbbk-A1ko6woTZBItIgSHo-ewR-Uwv78cDvtadBmJbt6VbkndVyYlwRpgZ9tlqH-IUdCOuOGu_MtPBFIS8DO642_BXdXJK695OgW81cXzSdQeVMo7MXSBacnS2POWh4BbD1QInYNg2LBqZt5gKYdBPndXQYEYjILVQCNodc4EGE0cPyOcVVPZW64cxWqSSSPGg-1ZwoUd8OeAZ69SnycHooN-TgH1fEfeZm58b-CVgakyW2BYhy4Rgmg1ZpgjzG-pcquNKvZ3KkIUq_iOvLi2FqR5qPBqr6H6HwyHIyLcBb-3X0cIfSdjYxXQQADKFrniIRXa7KZfebZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان جاده هرمزگان، به نظر من خودرو تحلیل اطلاعات پدافند باور ۳۷۳ هست
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20259" target="_blank">📅 17:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با یاشار : امشو شوشه ؟ بوی کوه سوخته میاد
@WarRoom
⏰</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20258" target="_blank">📅 16:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ2Pxvn6xG538TzZ4N3KGobBtm1EYM8wUyckMbMtqweSMMnYluqujzO09h_Bu80DH17Fs4XOfXYI7mjMsnKQC8W6MEAiuS5_GsJkzX8ZuxPifII_18Bpt74LUpbXNczZZbkOsLzLrFoTbb-c-a-7OKU9AIY3fHgNjMCNDnYKaq4cDKxwxrhCiQ0ifcfhW_kr9VemJl63Cq7UnPOj5R7cMSEKbP3c_0vBH7UC4F3qAilPYZ6lsY9k3g-JcWlyMzppHqO_XF3PXEueULW1kl397ICWxabU5jqFZbnQRVj3o2Ql1p4jpeSoQ9ABh3hBIRgZnare0ux7jHWwpIrkLmbH1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون منابع محلی در اهواز گزارش دادند: ستونی از تانک های مدل T-72، متعلق به تیپ زرهی 92 ارتش در حال حرکت در بزرگراه آبادان و اهواز، به سمت آبادان مشاهده شده‌اند و به نزدیک ترین نقاط مرزی می‌روند @WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20257" target="_blank">📅 16:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سفارتخانه های آمریکا یکی پس از‌ دیگری در حال اعلام بالاترین سطح هشدار برای شهروندهای آمریکای مبنی بر خروج از خاورمیانه هستند @WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20256" target="_blank">📅 16:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">instagram.com/yasharmotors
لطفا همه این پیج دوم رو فالو کنید ، بعد از جنگ هم کلی کارای خفن میکنم توش
🙌🏾</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20255" target="_blank">📅 16:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بلومبرگ: یک نفتکش قطری حامل گاز طبیعی مایع، شب گذشته در سواحل عمان و در حین عبور از تنگه هرمز، مورد اصابت پرتابه قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20254" target="_blank">📅 16:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">😮‍💨
پیج  در ۱۵ دقیقه برگشت</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20253" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">روزنامه «وال‌استریت ژورنال» به نقل از منابعی آگاه گزارش داد دونالد ترامپ، دستور ادامه حملات نظامی به ایران را صادر کرده و احتمال دارد دور جدید این حملات
روز یکشنبه آغاز شود
. تصمیمی که به‌گفته این منابع، پس از کاهش اعتماد ترامپ به نتیجه‌بخش بودن مذاکرات با تهران گرفته شده است.
به‌گفته این منابع، ترامپ به دستیارانش گفته است دیگر به دستیابی به توافق با تهران از طریق مذاکره خوش‌بین نیست و مقام‌های ایرانی را به جدی نگرفتن مذاکرات متهم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20252" target="_blank">📅 15:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbnuCd4a4mDW0Z5nRMDcVi0bK9jjuA-I5TCN1ez-MZvSUK9n0XllF97MKs76SZXBMbKBkQTh5GXqlfifCq5Pfjb7ZblAzjWM29fO48v00ma8krsh2cfD7SUQMU3YFYciAQtBlQZkMPhhR_yQPq-ITU5JqlAMr6S_1joGMj3WlNechlbfeirNGqaZqbrXylBtA6qNicJM4OFwJGA6MpdeLvliRjsrjhd9RXXyApWnPwzjklZncMxvFOLLAQyaQYsl9ThIi80wsKM7Uj0wBpab0p56pX64V4FaLF-9mhEzYUpcw-NY4sHJgaqI9s8QkV6vWSI4CjCJ4U512Kja9QHJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای
C-12 Huron
یک هواپیمای نظامی بر پایه هواپیمای تجاری
Beech Model 200 Super King Air
ساخته شده است و به تجهیزات پیشرفته اطلاعاتی و شناسایی مجهز می‌شود. این مدل‌ها می‌توانند مأموریت‌های
شنود الکترونیکی (SIGINT)
و
جمع‌آوری اطلاعات ارتباطی (COMINT)
را انجام دهند؛ یعنی رهگیری و تحلیل امواج رادیویی، ارتباطات بی‌سیم و سیگنال‌های الکترونیکی. همچنین از آن‌ها برای شناسایی اهداف، پایش تحرکات نظامی، پشتیبانی از عملیات ویژه و انتقال اطلاعات لحظه‌ای به مراکز فرماندهی استفاده می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20251" target="_blank">📅 15:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfnXNVQd8AWW1zT4l7d0O4Z1tHOU-NlGL2DTMA94PcPr7y3uKFoYXyDSIdnSA48iMEtlKxY2g5-l1kreA0erfyLccT4t7q-H2hLoT9cDpEtXHnCqLzb66SVjaey56jkCOPrV_8h_ybDrm33mQmYriLg71lcyyp8YfbglCVtM5KAU-h1mRH5Picoofl8DwyopZmbhju9uOaRVOZ7a6qtpk17zeHy8tyk6pFgGJ5IkLcgM6wj3WE24H2dYcyCDgpjrm6BN3IS9_iNwwJmeJhXEy7uQiQWkVZHoQkSu0VgkSA7f57ekooIwSEjRfPZ5ViI_vZ5I2byVNMdKeRdMyhRKmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین بروزرسانی از موقعیت ناوگان نیروی دریایی آمریکا، همچنان ناوهای هواپیمابر بوش و لینکلن به همراه گروه آبی-خاکی باکسر موقعیت خود در جنوب دریای عمان را حفظ کرده اند و در محاصره دریایی ایران مشارکت دارند.
همچنین رزمناو پرینستون(CG-59) و 17 ناوشکن از کلاس آرلی برک نیز در اقیانوس هند،دریای عربی، دریای سرخ و مدیترانه حضور دارند:
میسون (DDG-87)، ماستین (DDG-89)، جونز (DDG-53)، اسپروانس (DDG-111)، پترسن (DDG-121)، کوک (DDG-75)، راس (DDG-71)، میلیوس (DDG-69)، مورفی (DDG-112)، فین (DDG-113)، بلک (DDG-119)، هیگینز (DDG-76)، مک‌فال (DDG-74)، پرالتا (DDG-115)، گونزالس (DDG-66)، روزولت (DDG-80)، ایگناتیوس (DDG-117)
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20250" target="_blank">📅 15:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رسانه های داخلی : نیروهای مسلح جمهوری اسلامی وارد بالاترین سطح آمادگی شده‌اند .
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20249" target="_blank">📅 15:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سفارتخانه های آمریکا یکی پس از‌ دیگری در حال اعلام بالاترین سطح هشدار برای شهروندهای آمریکای مبنی بر خروج از خاورمیانه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20248" target="_blank">📅 15:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وال استریت ژورنال: ترامپ، در ساعات پایانی حضورش در باشگاه گلف خود در نیوجرسی، طرح‌های جدید حمله را که به او ارائه شده بود، تأیید کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20247" target="_blank">📅 15:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20246">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سفارت آمریکا در اسرائیل و عراق : آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20246" target="_blank">📅 14:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP99k8GUZFu55QuYhocdsO5sOme9yEqJujTm7pPoJUYYwscZh7QGn7klH8bWHwRVzLMGjhiiuBZVwJISjX30hpAjG7nUgpqtpQ_4nHMzbBfKKTz1aiIRD7Y_eOGJQ_7Cc0M0-BBnTqb7LrtPKsXo_V-Z88KjhK0Ka3ppCVoit6EMBF9dn0-xo4H4M48mQoc534-_VBY8FLPB3ngxrifXxePzoKT4Fp-yOJUUAZc4RKg_JACeEi2cAqU7WHrd8c1tTF0hfB5O9GkcDzT0UUW9SxOGRpkxN6LWf5cDtKgh1jrwYTAhWi9ZxmEcv3Ttu3dtihCCsxgHstvAiVwr1a3-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر فرد ناشناس با هویت البیبی التانکینیاهو
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20245" target="_blank">📅 14:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تسنیم : گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شده است و حمله ای رخ نداده @WarRoom یاشار : واکنش صدام به این خبر</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20244" target="_blank">📅 14:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asfwco-T4O3v46elNJzgwaWBIoOZrZgCc-Pe23ZNPEG3FAifAq8tln2VeRBQo_rVmHA149pPySHxmHFSO8mlWF77taPH14bRcAdB8z3JBtzxArlcYG2XbNJal9S5TAwR_24MbyeVyqz3TlC0LxXzJ3_Rn7jwEqrUbJL_YIO8k_g1GtuumFBkDvtcMYq_rNLSviQh_e5K_5dBbpXXVKY_qH05-HdJB-5C3D6BQ4-EnR_2lKnlxjqNccoRqzTSV9eJmUf18YTNGSfTv1xVD0K48yitByDL0pTgkncEyu9M19Ljis8j1Y6grbDmOpwjag36uQ4DVwS0BCTMJvRM_9QN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش غیر رسمی‌ ، یک لانچر که در کنار پل کمر بندی در شاهاباد استان کرمانشاه بود هدف حمله قرار گرفته @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20243" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ارسالی : یاشار تایید شد خبرایی هس پادگان چهارم شکاری دزفول تمامی سربازارو فرستادن مرخصی به خانواده های نظامیا داخل پادگانم گفتن تخلیه کنید تا عصری
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20242" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOdChLEwzWUrT1huAZisg_fZM-GfvsiekozKxXukt9vheEtbAVhZR2sYFt5Hj85KyWh7lxQQwI_4QzFU-XPLY7AToRdA64F82iaYNoSUyAwWPZmuT0yrzYd7oFSE2YN_ci_CKf5TSlS40CLKaOb364xiv_2E0TB6SsAv3GvV-t7CDHggnmT06nN1NvS1R1fydTyTK1fsbDifv3rOs02zCFhvn68ecoKBloeHwLak1uKvYi68VeMDKih9d2mqsIfJGZJVAD6x2NGa6zTN0O18QmpbmgCLgxWEqapgOwtl1xY84XDK697miVdF8yhJrL_j7E50FcCNZdDnBWtXsPxm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش انفجار در شاهاباد، اسلام‌آباد غرب ، استان کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20241" target="_blank">📅 13:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هم اکنون منابع محلی در اهواز گزارش دادند: ستونی از تانک های مدل T-72، متعلق به تیپ زرهی 92 ارتش در حال حرکت در بزرگراه آبادان و اهواز، به سمت آبادان مشاهده شده‌اند و به نزدیک ترین نقاط مرزی می‌روند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20240" target="_blank">📅 13:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش انفجار در شاهاباد، اسلام‌آباد غرب ، استان کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20239" target="_blank">📅 13:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری سی بی اس : آمریکا در حال بررسی یک خاموشی گسترده در تهران هستش که باعث عدم جابجایی گسترده موشک ها و تجهیزات نظامی همچنین از کار افتادن برخی پدافند های پیشرفته ایران میشود ، مقام آمریکایی فاش نکرد که این خاموشی گسترده ناشی از حمله به نیروگاه خواهد بود یا حمله سایبری
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20238" target="_blank">📅 12:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">براساس گزارش تحقیقی رویترز منتشر کرده، یک صرافی ارز دیجیتال، به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است. این صرافی یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به صرافی بایننس و فعالیت‌های…</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20237" target="_blank">📅 12:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش ویژه فاکس نیوز از فاز بعدی:
وقتشه رژیم رو تموم کنیم، عملیات پایان حماسی
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20236" target="_blank">📅 12:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شنیده شدن صدای انفجار در کویت @WarRoom
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20235" target="_blank">📅 11:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرنگار نظامی خبرگزاری عبری‌ والاه:
یک نشانه دیگر از تشدید قریب‌الوقوع تنش‌ها در خاورمیانه... ایالات متحده خواستار احتیاط و هوشیاری و خروج شهروندانش شده و از آمادگی برای احتمال لغو پروازها و بستن فضای هوایی، از جمله اختلالات در ترددها، خبر داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20234" target="_blank">📅 11:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فرمانده قراگاه خاتم : ایالات متحده با سرعت فزاینده در مسیر ایجاد یک جنگ منطقه‌ای گسترده پیش می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20233" target="_blank">📅 11:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ادعای کانال ۱۲ عبری:
نتانیاهو موفق شد ترامپ را متقاعد کند تا حملاتی را علیه بخش های انرژی ایران آغاز کند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20232" target="_blank">📅 11:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرگزاری ای‌بی‌سی نیوز:
دو مقام آمریکایی گفتند که برنامه‌ریزی برای حملات احتمالی به ایران به طور جدی آغاز شده است، اما این برنامه‌ها ممکن است در هر لحظه‌ای تغییر کنند.
یک منبع دیگر نیز گفت که حملات احتمالی با مقامات اسرائیلی مورد بحث قرار گرفته است، اما مشخص نیست که آیا اسرائیل به طور مستقیم در این عملیات مشارکت خواهد کرد یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20231" target="_blank">📅 10:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبرگزاری صدا و سیما : منابع خبری از حمله پهپادی به کویت و وقوع انفجار در این کشور خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20230" target="_blank">📅 09:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات آمریکایی: ایالات متحده قصد دارد در اسرع وقت، احتمالاً در همین پایان هفته، حملات جدیدی علیه ايران انجام دهد. @WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20229" target="_blank">📅 09:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات آمریکایی: ایالات متحده قصد دارد در اسرع وقت، احتمالاً در همین پایان هفته، حملات جدیدی علیه ايران انجام دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20227" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ممباقر قالیباف، رییس مجلس گفت: «در روز اول جنگ در ۹ اسفند، ما یک‌ساعت بعد از بمباران فهمیدیم که رهبرمان کشته شده است.»
او ادامه داد: «تا ما توانستیم سران قوه را جمع کنیم و لاریجانی هم بیاید، ساعت هشت شب شد، آن جا تصمیم گرفتیم اعلام خبر مرگ رهبری صبح فردایش باشد. بعد این جلسه هم سریع پراکنده شدیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20226" target="_blank">📅 09:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ساعاتی پیش سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از یک حادثه در فاصله ۱۱ مایل دریایی در شمال‌شرق لیما، عمان دریافت کرده است. افسر ارشد ایمنی (CSO) یک نفتکش گزارش داده که این شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به اتاق…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20225" target="_blank">📅 09:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em3bqRC4podHhaFQdT1NnhEZnJq0Q01JMw51ksCYFBFotdg2QaQ5ikAM1NDEkbBojD1XFgiFfWGLZEFeQgZoTYsIvBAApqYcjdodrQwdZU4fqJKiWS2ZYXHGXM31GQBdE2QfOyuPYnhuVri2St8G75ed-w2g9PEs4-PZtAtSrENEdgJACnohubhkejdy0LAIH821TA2am-fdqQW3ugv-dqe_4d6zbwnX7GVbAW8L-URuZ6T0EL-UWtl0aJD-NzmnnmA3uGSpXEV9JOlzq3yP9IOsMtT3AEV2faXzV7Mr5cONuQYBKridexWntyytHg9gOh2kgIGv0QnwblW6KH4VMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از یک حادثه در فاصله ۱۱ مایل دریایی در شمال‌شرق لیما، عمان دریافت کرده است.
افسر ارشد ایمنی (CSO) یک نفتکش گزارش داده که این شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به اتاق موتور شده است. این نفتکش در حال حاضر خارج از کنترل است و گارد ساحلی منطقه در جریان قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20224" target="_blank">📅 09:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا به فاکس نیوز : فکر نمی‌کنم رژیم ایران تا کنون با رئیس‌جمهوری مانند ترامپ مواجه شده باشد، چون واقعاً اقدامات را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20223" target="_blank">📅 04:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3upG5XR3GI_NcMDeujFJ5Oc4ZrjnoQqqOaZZhLy8UtPb3yjjL3MN7u5w6ISSCLJJluq-HfsS8QFZ7Rqy8mnMHPFn2Q3lxAPhPZjBT_JuOmAevnVtVV0V2tluEEZkP0nDlVXldooG2AKFMdxm2cQ3CuiVb8vOV9VnqBBYGTCAvptVhaTBGcksfrg2cLihPXC2EXcW8jAxCpBtmIAdQ3WEklDVQfiXbUFDygvaYYrmCaWltFBhXxeTh2UVVTsrbSRGU3OqARFy6SSrw5qpWS3G1io0gizo9JQRh7zBTE_vPNUi0xPEn5mo3zluGT1AaEoA4OFCVhEk8N3-vlvHyfURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7dee0280f.mp4?token=h48fSn570mQvOREQ8NV2fOWa3_yJnfGNzNj7fQxF4K6AUCqHzNMxVff2Pb3M9gBMJ-sQyIxinelq2-P8v3LN2-jdy1_VBnLkRTqHbLr9ouPdhW9iWn4YXlZ3w96yVc1jSA0pjk4Rlay6pwUQVNzbZmIsL-_EbuOZoBoF-ghjwzsp5JfPfdreclQ8ryXUlXf40VpG6yay9250ZtGQeUWaqAHGQYIWIQ3cV-BcSmeHgUj06wP84X-Bt3tvkOlKUDWfLg_9iBSo1P9DNRu2Iy4j4tpTSGhvcqmfpavK319_15DpZ_MLniixziaBabEIFHpPXvTViTniJbQupGdBY6jUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7dee0280f.mp4?token=h48fSn570mQvOREQ8NV2fOWa3_yJnfGNzNj7fQxF4K6AUCqHzNMxVff2Pb3M9gBMJ-sQyIxinelq2-P8v3LN2-jdy1_VBnLkRTqHbLr9ouPdhW9iWn4YXlZ3w96yVc1jSA0pjk4Rlay6pwUQVNzbZmIsL-_EbuOZoBoF-ghjwzsp5JfPfdreclQ8ryXUlXf40VpG6yay9250ZtGQeUWaqAHGQYIWIQ3cV-BcSmeHgUj06wP84X-Bt3tvkOlKUDWfLg_9iBSo1P9DNRu2Iy4j4tpTSGhvcqmfpavK319_15DpZ_MLniixziaBabEIFHpPXvTViTniJbQupGdBY6jUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری i24news : ارتش اسرائیل با ۷۰۰ تن مواد منفجره ، شبکه تونل‌های حزب‌الله را در زیر کوه بوفور نابود کرد. @WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20221" target="_blank">📅 04:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏وزیر خزانه داری امریکا: ‏"بزرگترین بانک ایران سقوط کرده است."
‏"دارایی های آنها را در همه جا مسدود میکنیم این پول به مردم ایران و آمریکایی‌هایی که توسط رژیم ایران آسیب دیده‌اند، خواهد رسید."
‏"بانک مرکزی مجبور شد پول چاپ کند، هزینه تورم را متحمل شد. اکنون آنها تورم ۱۸۰ درصدی دارند. آنها قادر به پرداخت حقوق سربازان خود نیستند!"
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20220" target="_blank">📅 03:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اکسیوس : یک مقام آمریکایی از دلایل تصمیم به حمله بزرگ آمریکا گفته است که ایران در روزهای اخیر «بسیار تهاجمی» عمل کرده و برخی مقامات آمریکایی از سطح بالای تشدید تنش از سوی ایران غافلگیر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20219" target="_blank">📅 03:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W__AjnTziRPudx5kU8GgCIOIUIvGexqJBAAaJpymwd7Dg6IivhGxslsSvoOpN830g7SCMuxdr7rF-9FLTYKzT22cYOArnhWYlzFTEUThLbtn6Ppn3dz19G_Upx-A_cRhrRM_TcMweiG3hqdehbvHpqEa16davofgEk_AZnk2W6OMMeZLn9ouwCcQZYVGZBDL50sDt7Je1ceYHdWgDr3D5s84Cwu19nuV-kUqNSdEQsFjjAJ7-DpvXUNxo3ZT0KJ-LMQg6Ns7QdenehmZBQ5eFd-QCsHHchHtWmuXTZkCpx0Jx6KHx7AZ_rZhrHmrsQ1FEZ0_dc3f_LNZ5TW7bBPkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، بعد از جلسه کمپ دیوید، عکس خودش را در این مکان با چهره خندان منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20218" target="_blank">📅 02:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سی ان ان : یکی از اهداف ایالات متحده، هدف قرار دادن سایت هسته‌ای کوه کلنگ عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20217" target="_blank">📅 02:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شنیده شدن صدای انفجار در کویت
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20216" target="_blank">📅 02:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20215" target="_blank">📅 02:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO336YlPb3RSRbfMhDfFO4vb8d9Lx8OfR9PtGnPm1H1D3XU8NV_YogSYXpjEcUHKyfQ3VNIlp3VknN4EtWxVefmokO_b4pDAwgrHWNn1BI3AkdONmXT_SbQDWo6VirUjZypfceWcJWBl7R1dcc_NTSZUfRttV77JoBah1lGGhqyCj44uismDSs-PUOOeM7BtDrk6773GtnxE7Hvd_hy33Fg6JG8XVTHyMdHgTV1Q0Uyflf8nf0e1gvq18rJUnqdvQolOhDLy6YNv0Gfq1gp4whdlq54F7JB-zGdzT-w-fWgeBPzx0c0cKUfrtNRwuOLmILFDhJEOfawO1G8R67HI3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : با ترامپ دیدار داشتم، نمی‌تونید تصور کنید چه بر سر رژیم ایران میاد @WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20214" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20213" target="_blank">📅 02:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تسنیم: یه آشی برا آمریکا پختیم که یه عالمه روش روغن داره
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20212" target="_blank">📅 02:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20211">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ادعای آکسیوس: اسرائیل نیز برای انجام حملات علیه ایران به ایالات متحده خواهد پیوست
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20211" target="_blank">📅 02:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فعلا پوتین سنگین کی یف اکراین رو داره میزنه
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20210" target="_blank">📅 02:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سی بی اس : مقام های ارشد آمریکا امروز درباره قطع کردن برق تو سراسر تهران گفت‌وگو کردن!
هدف از حمله به این زیرساخت‌ها، تضعیفِ توان تو ارائه خدمات و اداره موثر کشور عنوان شده...
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20209" target="_blank">📅 02:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مطمئن شوید که چنل تلگرام و اینستاگرام رو عضو هستید. در صورت قطعی اینترنت، تلگرام تنها پلتفرمی است که با ضعیف‌ترین اینترنت هم میتوانید اخبار را داشته باشید.
حتما چنل رو پین کنید تا بالا باشد.
🌐
@WarRoom
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20208" target="_blank">📅 02:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت جوریه که هر کسی بخوابه ممکنه سکانس پایانی رو از دست بده.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20207" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مقام ارشد امنیتی ایران اعلام کرد:
ایران یک طرح جامع برای پاسخگویی در صورت حملات جدید آمریکا یا اسرائیل به زیرساخت‌های ایران، آماده کرده است، بر اساس این طرح، اهداف احتمالی شامل زیرساخت‌های حیاتی در اسرائیل و زیرساخت‌های انرژی آمریکا در سراسر منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20206" target="_blank">📅 01:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شبکه CNN: مقامات گفتند که ایالات متحده در حال برنامه‌ریزی برای انجام موج جدیدی از حملات علیه ایران در همین آخر هفته است.
دامنهٔ دقیق حملات و اهداف احتمالی مشخص نشده است. هر دو مقام آمریکایی هشدار دادند که تا زمانی که حملات آغاز نشوند، امکان لغو آنها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20205" target="_blank">📅 01:56 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
