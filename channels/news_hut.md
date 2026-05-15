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
<img src="https://cdn4.telesco.pe/file/W7OXpp_XK8V_zTcTsVV9tessjLYI-OuuypJ4_5czJEQZCyjFf7MR0s4ukZFJthJ-j3D0HUvhN0DX-m0oPs1ameYkSN0DF1yZtTzAgZKzrZEa7sXk3Ge6QoJywCkLqH6ZH-SyDLO8yKIuThSHV5doLe1gjJpMT-kSWzHN0vspa1_qrgCnhUkxxptlDqsWJ225pTTASatr14Cwwh05y9jWgi_DDogruNx67VLtNp1y6iFNxl_aEFvJT5wBXadkcLPWRRkm1NE93k6xT8efzojwbKJYjNqoNjOe4JY-DM6-cg_BFNe2a7Ugi91hXq1S_qMcY_uOV9RnIlZKxYFvQffMbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 146K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 14:12:51</div>
<hr>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjk7COUTUHlHZYLLprftiuZ5s-dXv8Rmu0XIKxoDycRLqOPinhtv3QHmSJqSMqJTJHddgbSN0p2bFtGoXZ5hSlyqmee3FRAf8YH8o7wcn4IC7K_xrkcFCeo8zAHZpXMUtbPCDvQ6l7UkuDByePX1ttAfh5Eby1j6p-gdD8eH0cLCuV2wa2T00KWMh22grkJ6sPH036v0mrCKWtWDdM8Sy4wYFykTvPmNp0rp3mvsRg7efQxOlQPmVFFHSsjih6fMcJR6YikIbObKdgDKRgqXYVfi7Ry7UsEa8pFyun8To-pkCZ7RYmvBkFNj5mpliwQfhkE1JO3sU7ai11Jpqq0v4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4w6G-lswnuRC6bBj8RVNzmJeiGntwi0RhAUpkbl0TZvqp7j1-no1IdqQzB4IUKLClynwCJZOR6wRBg1U0FK2jDmLVBdSsJg5jNR6ryB0k90Sqyec6e0zpjFC14PJ69Jo77hohCaJs_wrFdF2Oas6Wx1cxZ5fO5pzZr9twkEiMXCO14t1xAbCFyb7tLWl_nTk0bwbDKhmdg-ltlMAxhQv1E1hODZzoqT3e7vnKGIFIaaNW45kj5-6rJMpB6oJsRf5xbe3SEXLdsFrZNUYE9hAm8pc2pdrwlq476XM1kOw9xRkHSzueJVSzcTQeztQMw3N3qaMau5WZMVTuJD4RPdbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVHNK1AiRWWEBsOLTMv0HmBXfB6f5YB_LfeQgQlZPxWCFXdylen5N2XlJs1n64bhh4hqkwnXT6ERU-P_mgSRSSREJeMVrC1fbT6g3paPyjxgHtCyac0fzBa1M7AStkIjMM92AzM5nWuZ-BHGOCiV6qbSvWqYGk2ajT87jsenphEXXAGw_I8A9lyiu94vj26d97pyCkmvlEyL0ElRoFbhY8lg7RoDat2IQl-ZpprIbdCJ-lJZKw3YSwvIKrDL5UjU5FESuAZ1QmVPNbiC6QwhTpXc7tWTeiDdPw80BufcIAnOdAily05Q7GeebbnE4Phc4QXZOHpc3ANimkdr2o0OfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaylE6p610F_0KuYOsMF3u2G0KtIbHt5mpqjTUy4hiZLhdLJKQV00UlWn1oLqCPJCCcETKMj_T6U_BABZzXmxHbeBhSCxOglsg8m1In9BCJqcOo2vQiVYSzFx9-yiq1t1BEh7Lai_VNx8UHmbFp2AyatJZkRUjX7Z0xQ0p-o14bPtezpLszvekcko9sRzGtB4hZ-Rf4vbzFQAeGUK9UGOUhsCvvYjok1xLEM9QK-LC-0vXj8O0oSKBmv3cP2KG1d62IOsU_843txDITyvA_u80RHV7FY3rKSxJe9vnIFnKvF5Gjrcenrf520P2FYZM4wzfla4PQ9MWObPu1lvGZP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=Wu9sArMxTFavOUYZBcNFAoUf9EC0cXwa7z-PL6UzFKjnuCllxthjuXaWbhgkKpzXlWFylzrrIQdBMcNUS8JKJqtxKAvM5m-Gx6AB2NmhEy_c8R5evtVVkwxC6-DihaVKMU-8whXw4iA5ivyX0keeN9yI0VDBOVjW0N5QgMpB2hLQ3gU29zlaMIW2tRPh7nkQ-yux5vVZGzLpIQh7rLA96gbCjV0DeJRA9vA_XaSjMW1C3D0TkJjhS8BDyBMG0Ywpo4wN93gW2pOlbqatSkTokdJDDogIlO6_hm0vY8QGJweDWCos-Yiikp8KV2GLqS9hm9uAu_w_bLyTHdV9hg87KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=Wu9sArMxTFavOUYZBcNFAoUf9EC0cXwa7z-PL6UzFKjnuCllxthjuXaWbhgkKpzXlWFylzrrIQdBMcNUS8JKJqtxKAvM5m-Gx6AB2NmhEy_c8R5evtVVkwxC6-DihaVKMU-8whXw4iA5ivyX0keeN9yI0VDBOVjW0N5QgMpB2hLQ3gU29zlaMIW2tRPh7nkQ-yux5vVZGzLpIQh7rLA96gbCjV0DeJRA9vA_XaSjMW1C3D0TkJjhS8BDyBMG0Ywpo4wN93gW2pOlbqatSkTokdJDDogIlO6_hm0vY8QGJweDWCos-Yiikp8KV2GLqS9hm9uAu_w_bLyTHdV9hg87KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Sw5xpicVoSG72tYYBau1hEdlBzSdGQtd1nyDjRUfowuB7JcO9AQhTJon5Xa29wBmFRZAskd0wXnOKc1fJT_DGpl9XQ1Bb9OTKH6qfAEfFvRy5wDys9MVPIdnDqV-Ym5KnoPHPu4QXoPyVyVfDUE38UbDbiy4NDaKAFEw-1arSRV3KMRGcQk7rQkc_neThau168sYiBeqL6hqsnXEO_4vGatn554ffktFwVl5nxppVH7jgDxS5qo424BGUqBGIWt9nH0FE2soup7l_6MUXFxmYw4mB0XmrrI1YEJIIPMpt7QuTjLj3UIDatnbwfKMnyoKCRGlEkgI21VmhEM7oVIWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVPHReCSyIWk9Z7ACn6d0L0_UR4ptMHq1lx348bNwybq-PFY8GERbcSqewBLqQliwl97F4dHBi_kQkyxO4wWRCzunScdvA1gULVpdXvT4nAOG5T8lDseH3SuLTUmKj73jM9xcpHofipXsKRoWIwP8fsO1XulP4hsbM9KZtGTSoBt693PV04wHp9bB27UaM_n13QrljBQq12nSGCIfi57rUV5ApTSfTkkBOOvwh8hzoP9pHTml3Y-sbZu5Pe9r5ZqJbJIofHhMj02qwzs8iR-ZCzya32Z16CgonnCcJ_HWB5HXF0_DWXOPdURAlKMScgPSA_2wycG9gMUr9Rqxzx3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=jMasPhynyX-q2oSFp4HQdoFJuI-uwwLg1w-hMN7H5wDLg5qOmcRb6sXMTKBxBC1-Pd7ZY6MUdGh0av9ME8zZgBk0GZzhXFhURo9NsrUGVSHPhRH7qLQuAqxhoeUyrW-Da-06aN_BrEXGbXdkuNamNX65GZExhDYMX5JH1x3mU8z-R3sGndlKLN3g_bnJVyMV6cwrCicLNrqV-DHClnwdIkXcV5vZBaYNcY9JvvcGzVmFla0TswTPN3oefFGgwG2RGyvC7H6U8-FDkR0SkJQ-09Dj1cWiNLQrcx0UaXRUsaa2YYrruRXwqna3kt5sgBadU4WJFyKAj4KjvIv9jEb7dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=jMasPhynyX-q2oSFp4HQdoFJuI-uwwLg1w-hMN7H5wDLg5qOmcRb6sXMTKBxBC1-Pd7ZY6MUdGh0av9ME8zZgBk0GZzhXFhURo9NsrUGVSHPhRH7qLQuAqxhoeUyrW-Da-06aN_BrEXGbXdkuNamNX65GZExhDYMX5JH1x3mU8z-R3sGndlKLN3g_bnJVyMV6cwrCicLNrqV-DHClnwdIkXcV5vZBaYNcY9JvvcGzVmFla0TswTPN3oefFGgwG2RGyvC7H6U8-FDkR0SkJQ-09Dj1cWiNLQrcx0UaXRUsaa2YYrruRXwqna3kt5sgBadU4WJFyKAj4KjvIv9jEb7dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzD0m5nXfp-hae4r-47j2HdC1_f1Hwb2x6ItrmRyhQDI-vkSXq6vG-C4njtCO-vPmAGqvnjv1MWWmjktvJOVApWHwrGPoYPt2uARM-9gP_cVp9m-fAc3les1usjro5or33tz5mVGoRwAJ1F2YcclT-vK1lx1eTy_r07nffaFgT4FQ6B-XnokOgNF6s3toap-uGrgBwk2TKz56kaV9rI7hq1JPpnwpRQDJOnuCm0HTU5pfVP8Oni1KSFyTBndGtAsyIk0REhZi5tmuQJqg6lTUY2jiorlqR3ImS9OBoJUdy0MN3ifEnUzfEo4LpWzyRfCxqWBff78c7UW0Gl8ZojXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgQLcyVgDGzxlU5nu2bLlbbbAKNhm82z48ZUhWAcR0otayBNX-cFcJNsHR0zumeGQqVefovagSacGecrdzrSY7jInTAUoEIndgb8BoZOZ6srLuY7gWEymdrypxC0sAqujS9TbR0-70eJm-3kQH-oQD7I_gCqoqiB4cJMs2k3MJ9y4uki8IlhOYm_oJRFAIn5kZg_vu_CxyBYckbxjN4diG5cLn2J7qfs3TZQmdqxXOvYkh6cgIVguYvpR-eT6YxYdJ5Ay32kFgpzwG164FsLH2Mi3qMirWcQujvZ8o_AqQ-xijw7Zu7K17zgFm-KUNSfcTIkxCgAS6hv4NzQlii7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxQXBCPDwHXTLqZRNw8-qIAf4NmfkUS8q021OQLKPG3Lxea-jhbnNSpf-nv0X9Xg5FPFHxNglSXdPv1dEmEqkqN_q-tboqpyrvQ_J7790XKejrAKe8-Nn8vafTLdwByFhrcq8psoxROUjOPDPD7lzScnofFb1IUEeMpcrjknXm1PVFt95MvDWhUkn0heXXYAPMemDb0FiHEQYrIPDH3oly_3PHtHhleK95DYwAaZna4q02OMNB1wUs-NjARGLBv-qVNWo4rkE72SHk3XWO2LWmj0KekGORuEanKklOSq30eCfR_G3v0JRuayC58Cfx0upiRJdUo10Skehr4g6KXNaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=nQanVCsX0k6eJlsZD9bWw_ch0t2FtIFdRVpNMdoEeW_LRi--aZq0uZ1RzhtqjQFsrz-mdOgeA9Lye84VYku4rCpvs05rXHR14sNEz0ewHl4_qqj4VogA5EH7dOwG6IT6IfpoCBx0-iXYn6NTVOjBych0x5Asp9nwIN9h3y-yxwGeV8ywr__bJhU6y_43tsO-d9LeafXvMqeHGNrhGS65IvlGRLTXSM3L59_3W3s7JwR3C8BCTRD8h6GND--3dBS1JuSnFDl4rjNUzHPDqcDJ9s0jh0ehX-ZZphVvJlqn1e_AF0tnCvBzbRRTKqs642MLiW0r7bNYog_wDtUTBafBIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=nQanVCsX0k6eJlsZD9bWw_ch0t2FtIFdRVpNMdoEeW_LRi--aZq0uZ1RzhtqjQFsrz-mdOgeA9Lye84VYku4rCpvs05rXHR14sNEz0ewHl4_qqj4VogA5EH7dOwG6IT6IfpoCBx0-iXYn6NTVOjBych0x5Asp9nwIN9h3y-yxwGeV8ywr__bJhU6y_43tsO-d9LeafXvMqeHGNrhGS65IvlGRLTXSM3L59_3W3s7JwR3C8BCTRD8h6GND--3dBS1JuSnFDl4rjNUzHPDqcDJ9s0jh0ehX-ZZphVvJlqn1e_AF0tnCvBzbRRTKqs642MLiW0r7bNYog_wDtUTBafBIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XoI5lgRdGBULjG_iWk9ANCPwsaC4V5m-7A9GHuXao9SSa5maHcJa7hsfw0IZeNqjiyYe6sAl1O1WsaY8shfBloe0G3hZV1awrwhSJmmc1b15-WcRqrsK5ORKucuxZF6pFqXwR2qmJ-uQ3Zb6o596ovDCZYr-VlN5Oh4nrCt3Iiu0b0M7z400rNVBWCgvZy6T_Q8dufsHUidDyRpDzQ1SWoduKf4P_JTBraxysPrOpEL5c7FLDMBdDn8IJG5btG73dwgTL392QpCiniHMg8zBJysLWdtikc2zj1laOyqaq7Z_pCTVhLYgixrrNgAOSs-NS07rflggzIvi4vOkYRoqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ICkoUxQVHKDfhyqzG-WCrwiPrhc-3r-na5evd7wT2qmnRttBFhTl1MSox19denk2RlIdf0s1hEpYXD88kmrPjkUUgwY3aFpIcBTDJNxtiflBiNPTfjn01PUoRZnCVsX9rWRZuR1Jsb8bkaTDbTUNoY7pQ-9FwZXgtW0CVF_8d6tC-kYjYr5rRWkUH8FTwHWVzGRqTCWx5jVc5oMS5Nv5hFQPHkUgXbof85u73sOiMDsJOcCuJmtfDc_iDQdAfQNlfkEBAxWGM1vF4a1A_fCSgsnq8g292GZgAz4X5DE6DI6n1R6lFwTkSDpFfWYrNCG-kma44EHEghTVqrTj4ABVNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pb4YItHpDGRZ_jcCebGDrWPm2lfuKbtv5w9bWx4JRjs2AzN3LNIGLbZmOeepNOmrHxeRxm4RoUUICTLTZAQN2owIRT5orbDu81_Miwmap1qdz-H3a3azu8jko7fcd20D8CaK8LqK45VR1nBVPQrdOcIT3hJ-FfQspqoobprXFsKGGQWFnYxpY08SCDqL4mgc9mibAsExA24ZPojYy9HCJkIwz5dh0kMDEUnRpa6GX5fX1KEIWntx7rGur1lFke7cVyGKz380hryKClzT30udjjmpws8gPRKpTlveCwBUvq6ag5RMkzfpBr7mbM3BXjBRUbtCa3ci069t1Gz2i-di6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Di4EKnZcmbeuzAUG78PokagA-JNEKDrOglIkLZAEKkNWz8lvqhI9MhRCXd9wBg3bnIZjJ75eEH7QuceSnykkLNMrxts6fzTXxw7TV43H4TqFhx_Puni9IFJx1ufs4BdP4HycrJWaU5JlxY3x-zQUSo5EBhK9cLC8d8OP5813NBiGgU6FV9CBsegu6bLKSnZMRajwvBYDnKOSV-KBdDBMuF-Q_CJAyI1v9c-5qfUikfLt2qHeqzqqtkzd_Lec_nGU8RRFPrNf62rWsyEICo0HU4ud44EOM6JiT4SnZd7q-bhtpY8hNFjlCj5jcMJU9Bc7bDviQ_puf4yMZzTtNK5LhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AiNrJdZtPdm-v2KooBHOX7ficmkqQHvJOFdYmw3iT_0kIOP0WE7fGPNEfWfN3pZxfitI1IwAc8JONNo90s4l6Rx5x1u5gcHS5lYI-VJ7D2XqrMzHdRWEvspeiZrV0QKw7-NEKxagsOgCtqfeh3RpARWES-3cMqAYDMuUtzzBuYS69rB-l6G0OtG_lrHNthYQhQszqfgILfvvBUSKn4pFMba351s4xQZDQ3dynb9iiuUHPm-ky1HkxmnD331gNWsJUUpOj2y5uRV_CbjbbhMySts3VSqJqR80SwenA44ZHLFq_qIMRRNDdq7O4jvN_iw3pGp1alNheD5LYNjrZ6dQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEUIUqGhVmSKtgZkvRJaxBhzoTrZgbCqkMj7xrGDiAOQQkCptEnUbmz6Ppjr0AbzO7f_rxhd0-gI2rnBhePegdEIGElSMHgTNCDfzwxgt3XNzWp9q5-8EqcAMjEh6HfGGyaxwzsLnEIU5kBXpAm194SnCO3LBCteyEMl2zhAJdm2XSnV-PwSclNUtkfa_mjNihn0w8pcgt9jweUB5oKfI2QW3hFzfh0JlVD_crDtvtF4tSWMQ_YeY051r19vHGFXhCLzriTcsqa7xXzJGw_jBPywDBQ2QqdMMT6MQxoFOOOWk3CAmgYLfpWF7gGL7U8SBo65JST7X4HM4nrLrO0Mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=D-CeSTJF3PeLj3RN1bs7pny3zTpa_xK97RJCUgegzs8hkZ-ulslNvxUzitY5L5eyYq6PIvv2ofORTyz3nEJGCur_eGhAwW38WgGnVhjPlZjqLjTUjg18QFBXdBJVRf9-nvuUZNmj7LOKutYJj33zTpkHrVft5-VEIf1huhnlQrb9lTqiupWTSnF2Zd6d2dP7mptkUq3IGJt_s6MQAcgplxX4iTrJnHfpljSvQMe837X6_eBVcsYmk4ImeMRGoVoc5_y46SO2xgItrDvyfTSJa54pe1IYiPTio0x8PNB8r5efJf0sc_zk17M30OqziD-sEJq3LEp1MCfm0E13H5AKWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=D-CeSTJF3PeLj3RN1bs7pny3zTpa_xK97RJCUgegzs8hkZ-ulslNvxUzitY5L5eyYq6PIvv2ofORTyz3nEJGCur_eGhAwW38WgGnVhjPlZjqLjTUjg18QFBXdBJVRf9-nvuUZNmj7LOKutYJj33zTpkHrVft5-VEIf1huhnlQrb9lTqiupWTSnF2Zd6d2dP7mptkUq3IGJt_s6MQAcgplxX4iTrJnHfpljSvQMe837X6_eBVcsYmk4ImeMRGoVoc5_y46SO2xgItrDvyfTSJa54pe1IYiPTio0x8PNB8r5efJf0sc_zk17M30OqziD-sEJq3LEp1MCfm0E13H5AKWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CS_LlJqjgYqhv-tRMdpPkvleKtwOpxK2XoWnML6zOXhwNEUwlY-MPGX7oWacXpjZnIkWV1EqxvOyFbq2itmj12FNEGHnFHoP3GiufmH0SUl__GqGHu6cwBr7Eukj_RTCEXrmPCNtookK-k0dEcaKTCkDJxWDDQMWNX1XM1DVeVQIxnanBQ3s5SqicmMMAYyQhSjPYSASXVsFNhKt-h64isdnpCrZnzXCSMb502MGXO5ER_tp6L_3hM53wPapyXpXm2KWI_-dcNmW6UKEpjkIrMo3xn5JaVFJ5cSkEpPo_MxJTLGBeFGb0sh1ZQ2gKhmngN0hAD96qqrTaBCcUsR3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KY47M2weuFwLaKJVJiYzmtPWVRpWcCnBz0xzIKBsRg6PR7cSXOx08Q2IECTkIVrXc8hJgQttZf43eu9XPJ1NRR1CLSgf9el-wEQShuY3qimAd6PvsCGMEM3588Fche3ypz9FkSs4ueGrytN0Y1SDJcOTEllBNKhSTBqXUEveM9J3osTTwDrFFUgfbDuQlHGjOAzXsrkh45prR5qAPIlmAJvdQq14iyTStORtf6py6FcozP5p677li82xxgpDGjreCPl0qMI_RSkHGviiWUsFJq8pZrQBlLPPfUM1FBpc1f8ncLpSQ7htG3vt7bO8679xBIAx1NO-NnkMMDA6iQAKwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxHss1r11t8AjvxDwe_CoicylL3yFVoMb2GGTXTEyIrqeDuehA9iD8gnG9cEJF5nskF8zepgPeARV0qIraE2obCiu9Th-9Tz0cc1HIUKnn9ydmOKaVF0haGRptpmoaqK2XtQUGGA5UR1c017AfqIUHsxERsvsFfPyQmVZXI6Zo1YWbWR4-hxZfeR6UdIM-n3GAUgzQP0GXFpDVN2hm7ySqp1CvO8-xnnxm6xZfySoap696n0MbcMHjXH9rEqrmEpHRQdHiuTVCa3p6oXmEKdkpQbMNmgQ4fTAP487akzAP4tzCV0z66IO0NdMcvZB_K4-lJEAdqU4w_JqM9Y8CEbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=beWxp35BhIOFHI9whXub0RVQxDSqpztZKlCT-JkeRobIEEz4Tnr2BdAngV1bwAUHJ9vGF2HbqcEnTN4t0jQYbMTlcJtkgkx0irEGOe4LPerTKWa_Y2t46IWOqzEATt6vec7Qm3dkzsbXllrpiQpjR8dSLBbyQcN-shMRXZm_TIMiIONo2_eM62zEJDa9_zKyK0Vk52uqMiALewikbkn9u2m2eBpCXrqGSYwme26QdxnuYbrs4NKq47c33Bv9T-isWZQ5pPaClo2e9lJpWc4Kjm83jJe4xgGsaQIqZBswpelwgv6A01_dGWavsU-5e1sm6hYAJBbo4ayHjxYj7ewk5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=beWxp35BhIOFHI9whXub0RVQxDSqpztZKlCT-JkeRobIEEz4Tnr2BdAngV1bwAUHJ9vGF2HbqcEnTN4t0jQYbMTlcJtkgkx0irEGOe4LPerTKWa_Y2t46IWOqzEATt6vec7Qm3dkzsbXllrpiQpjR8dSLBbyQcN-shMRXZm_TIMiIONo2_eM62zEJDa9_zKyK0Vk52uqMiALewikbkn9u2m2eBpCXrqGSYwme26QdxnuYbrs4NKq47c33Bv9T-isWZQ5pPaClo2e9lJpWc4Kjm83jJe4xgGsaQIqZBswpelwgv6A01_dGWavsU-5e1sm6hYAJBbo4ayHjxYj7ewk5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=Xuf2R64WqnrpLyQOpH3w0f9-8-IFaKA4wcUAOo6c7ojx8uL0hVMdYy1lLx5hkG2aL7DeA4R8yp_j0OsO_8uo-oRopI_EgUYa-BgWxhQZRQ1MEzDYVklhsvE89eXfnSX9-lOQW8BW9un-Qp4N3jckQZIiJi7Bwp1-44Tj03wNtI4jAAN5mzsbSSg1ssFXsKUs_egRy7ByKJLeCkOO52z45TDSPnfXdo5Jrbt_74K8l78iLjITiCVZbHHjzq2os4y0cnvZIkYyxnHafDkwFJEeARF-q_2vfMi8bpqjPCPDQ17kPvlfyAVC6RrQC_Kh2g5N0fx8i0cZItK0mZsAVXbOTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=Xuf2R64WqnrpLyQOpH3w0f9-8-IFaKA4wcUAOo6c7ojx8uL0hVMdYy1lLx5hkG2aL7DeA4R8yp_j0OsO_8uo-oRopI_EgUYa-BgWxhQZRQ1MEzDYVklhsvE89eXfnSX9-lOQW8BW9un-Qp4N3jckQZIiJi7Bwp1-44Tj03wNtI4jAAN5mzsbSSg1ssFXsKUs_egRy7ByKJLeCkOO52z45TDSPnfXdo5Jrbt_74K8l78iLjITiCVZbHHjzq2os4y0cnvZIkYyxnHafDkwFJEeARF-q_2vfMi8bpqjPCPDQ17kPvlfyAVC6RrQC_Kh2g5N0fx8i0cZItK0mZsAVXbOTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZTWYE3YnjxJXdNheCKWIfTkxeh2H756UHrRZQ_pqY8q9qrK2cdKroc50qg6U6yB_Ca0mRzhRuJM1HMUbYp0P677CDeCTdz8j9UKCjwSCkMkZsp9CNfAhz67ByN54U-ikS9B075Ahi-Les9AtnD3e-Nrqmd17YVMTSc5h_Lv8Mr7N2iJIRDc-pVF3DktMEg02G439OaJocON_bfPqpthT3Zn00wXzraSbX3LwOY604P6rSOEeCSqkKAIg8MWi3WhmqZCuL6Ps2rJ9k58b935C590_89PkZ2w6cPrLDas0oM9UTjiuXnP6Crxi0y5_eV7SdRj9qhl4iktqcozwIDc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرَک | کوتاه فوری</strong></div>
<div class="tg-text">پلن های اقتصادی موجود شد
🔥
10 گیگ => 1,700,000ت
20 گیگ => 3,100,000ت
40 گیگ => ‌5,600,000ت
درسته که این پلن اسمش اقتصادیه، اما کاملا جوابگوی تلگرام و اینستا و یوتیوب هست.
سرویس ها محدودیت زمانی و کاربری ندارند و بدون ضریب هستند.
خرید:
@SorenaVpnRobot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/d52oj7MvdlCc1pFSTfOLtAPqa-T4hZaJf_n83OD6290LFt2RPrMeE9CSahMg5MxzfTBTXH0bgiYdgbVYLVxeINf7HPBdwY-8z37g_JUCbxddbDJlYuc7zCHDA1qfz6MPGBcwt_bztw5e9FKY1ybuW57zIkcSIn0el5Nhird0wZLm4bhIYhEeYRzux1HAtZe-cncgmVx1vdUf8Ias45qyxuQ6JrCcG3uUWHuFa0UAF7qqC51wil0meY1aOYDsw8A_kMTalWi1mdbib_30ghm0PGr_EbwlJnUhx5N98eGjDRgQf-vpQi0w-Fj3mF5Igi1ejNUTezLyAlC3MRm064eabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpOQ7GIBzviLj5f3pqGEAoi9DBcJRqOA0WVhQrwkmCt-E_c5jHJvZ4AWIvwg3PXTxpgZ4tEdtjg3kwxcnAHoggi-Js7OAhpYENrXEUpBdeXQVjdBY7X7ZM4co2ikmT0qz1KoKFw-NJcH9yMO7ZdKL51frCvTSyyad_Jh8YUBRaZ_erkSaOHlF0hrl2kda9--tS2qwaCSeTaTdW30l2V7qnMWWYBgJtgnFOflLZltsHl63ekgX10HdCN1EuE39A0N6UkCsQd2E22tW7JA2lDkClBMalwt_bH67IInLoOoY7_JBR9l9zMhYlzixLDfyF3Z78ZkoMM2NOiqBavX54sVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMPC4AXYIpRr-dtxDJnxOJ4sD-Jh1qoDjdg3tiKDmdQlNO9RecN92vUgm35G3Q7f51yFn5MXTv5nRTUw0VDCSL_IZFkIwJFQJyA4ECzmZrzZpWugOUApaJ2IS9FpmBGzQKA6cjj4zj3jQHTAlelLI8JqMXRsNkcPKNP7ur-2BaPhZG0oKvDbq1BMwjLYRthOULLVIAfdGNLIwbsPh54oovk7Av6K-trrvQD-DNis85gfyogJG8PJvPvWAIRs7tVyOClBe_RDmgcIywbb7SwvUEoHEPjtbtxA3kDeB1dPbjBYn7lAVaCKckHjzfQCI-wlcz8P-OmVel0EKTjmmQsFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbzHiNo-WDQDlDDX0_hp1FE-hEeQCfdiYHLcmB-IUWNSPFDD_qUriEd6bPeeK4MNSk6tu7AFR_k1Dk_ZqAha8N4PzUH6cl40mFmbhBoD0TFt7MzPvmI0o0AICNDnUw6F0cRaomRCQR-Es7dA5_z8p-XA6fNXCj6UtPTUdHadcEWK0bgigjwNfXxoCV4m2SvhiW34q8mNOJEtPloirjVKfyIfbp1UGsBpD1oE561uxqK7m-iSRBsj-r3Ba64hZ-OHl_iuKZNzcTY7c4H657DaWdJH02ilWTfWpJl-LC99aCaw3IlSJ1mXJlcOPgrKaGf4IU0mKjw9UPyceySo8svOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=gBgVQAodcsFbp9DkHCNiuw2AwIpHB5GKHiyU2zGvBjSvYc5PMlrfVgvcMTlP38iST3K1_p9EFUvDWQwGtYOAHflTNeazYGIyCzzfaOrWhMpBCr53fRkS0EgQuj5f9joFjbRh1CG82x8y05mkdWC_9I2sHBxGjoO9CO1NodtxBfvHIZBPcKYMNr8c-eEAgd1gPmy75-p5JD0CPj1hkG_ukqHs5HPcAFyLjK5iB5Y38JhM1B6mWbrTvMlIdkq3eJFNw-ez2TnnHJFqER9--9WWCCR5Gcx6vbNNUvIo5D4BqLEDzdO9FNkeIvE1mzCquvjt1CaH-StPkOoCdlriPaanew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=gBgVQAodcsFbp9DkHCNiuw2AwIpHB5GKHiyU2zGvBjSvYc5PMlrfVgvcMTlP38iST3K1_p9EFUvDWQwGtYOAHflTNeazYGIyCzzfaOrWhMpBCr53fRkS0EgQuj5f9joFjbRh1CG82x8y05mkdWC_9I2sHBxGjoO9CO1NodtxBfvHIZBPcKYMNr8c-eEAgd1gPmy75-p5JD0CPj1hkG_ukqHs5HPcAFyLjK5iB5Y38JhM1B6mWbrTvMlIdkq3eJFNw-ez2TnnHJFqER9--9WWCCR5Gcx6vbNNUvIo5D4BqLEDzdO9FNkeIvE1mzCquvjt1CaH-StPkOoCdlriPaanew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=GDp7FjZ-ViqaHIJXRxC9Q6BFvD0b59eDWCAW6XXd7vQI5DIDzgPJz2t2kOqrv2sMT10zNlUEBtyPZtICP0LyY-C-iUZH45Y-JmMVPDHR8fe3gg5ySh5lkMnb9SHp1xq2rlFyYM9JnhdRE9TGhgEoqg9gT-vSMKu02OcIwnXCoIn2_VPaCu8gzKRqORDoKACOJviSkb9xSjtoxVhtbeGR5qW-ILYA0EboSIBpwpj4vUc1G9SpDuelWiQVeVTKKYfRm4aITrng74cAEQwA2Dquseq9Fvlij0C0H4r57vFEp-ZH9vjSE-6E5fkBgW01E31oknUGqTxtJ4-_0ZbzQmkukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=GDp7FjZ-ViqaHIJXRxC9Q6BFvD0b59eDWCAW6XXd7vQI5DIDzgPJz2t2kOqrv2sMT10zNlUEBtyPZtICP0LyY-C-iUZH45Y-JmMVPDHR8fe3gg5ySh5lkMnb9SHp1xq2rlFyYM9JnhdRE9TGhgEoqg9gT-vSMKu02OcIwnXCoIn2_VPaCu8gzKRqORDoKACOJviSkb9xSjtoxVhtbeGR5qW-ILYA0EboSIBpwpj4vUc1G9SpDuelWiQVeVTKKYfRm4aITrng74cAEQwA2Dquseq9Fvlij0C0H4r57vFEp-ZH9vjSE-6E5fkBgW01E31oknUGqTxtJ4-_0ZbzQmkukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kz_RrjATs9ywYh7T8cMXXq3UgU6r9KHBcx61P2ryRibbWCqqjoPZjRXqCNOg5egekT7Ok7mIjE4EmJLccSMmYR-ewAhEY0LSK87TOriU02AN9Fm9caW9AMFiSNpJin6E-XNXEgAaOXe7vggDw7gC4oiFIhqz2LKbzKH9kpOopJdCHKU9Q3GzUnT_xE2HoRmdyb9h8ZDrQhQq7KVjIqTnOY8KtLM0lPKWmVYw7MNT_NuoxCXkmFD0laQ71arBtiL_LuaQhqRdR9C7w0zByZp96ncm0H8UfVyzK_lR3I9sGQ2I5RqGm-yxJvxO9xCQjVyqJ_qx6P61N_KX-t9UY3zb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UQxpguVL2fhD2WCwd9yfPzRuxUNIHKaRnwUKyAtDvgmvYI8PmTzsARPUJxOEVPr9arwEFLyZeApInsD3-r1pPtlZWxGnVAaYM4mx1LZ93dJh_l6yog8Yi8c-G86Zju61iyIGoNLk5MnfKIHEh7CIStASZlplaacYypWbIr6lZS7gI0oWQznoZrv6EtidZLcQakaj7aCSnmvFsjVLnkuTGI04dmaVszP7I8wULucHa4nivcI30okEjUPIte8o6jn1D5AtQA4q4p3w91mZJ9quHkIahDH9QOWAZ7Jallv_Ny-tVaPWFaID2tSU_oUqvQxSMdYN4WCWTt9VQ62H00ooEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJvqTDQQZ83JgdcwXYrPrpWlrrOST-rnHgepjFqaCjiUScSrKfB-n-a8Drf7Rvr490Bw42z5v5vyk9SrATKYlAVj2Ji59g1X51fP2OmD_Ft68aY3ZAZX4BurooehxlYiQXBAiIzlAQzGHcyGGM2UCvRvwLPXvHuSdxCnBCvzOnCf6yq_Rjs8Jsdb8ZpSRjMg_LDsnJoFUfNG2z82AAmP5p_vR3jASc8PmwZyDGJqrTTvbbKSa_dhqSaOPt7ZNdYlLvWDm4xMMSpvNuBmHgsKmp7TBLuckCgYClYvEB51f73kLBv3ZDjsPRUVY36JIXjWi8GXmg6yaLUwL40qPJBA0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhGmQdgtOBBfFplMPyofDsC8GeteoLq5pMZRzYhY9B5uYWGT4Ge2cBHCgSZKSE7esZA7ILOesHyS4xIyC3KPQpiBtX5S-FQE5To1QOjDt27ytLb1ZFO-W1mf52KVbcgVR41ENcQxRzBI01hKVck1KNkTniZ5JHkr0FzNnmOuWXoGpaN32xjcM7eTBq6Q5lEJmGOsdQW_heOaSyV0f4-QpMefgrpjA7G1xi2TVHlKFJaICVRqJ2yuBRFAh55Ko7YjjqkBDMX3MKKd2TByK90G7cZRue3l52hnpPl7ihRNtNTlgebOcpX1qcbfpJ6i9MsvdoEKk0y_1yjRqmvZXKKiPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=N6F6DR2MVhS45VhjUqnkqmAKzdWMk6kjN0694K4GDz94D-dYCpXxutxwDuIpgQ7R48G9xbfS1f8iDCxfi_SO0daYvyBuim6cZB1RQfFsn2lX0htqk24Bgu4W3riEGmmIyGhTOqZJ-Z3peJYG1XeNWVwo_ErpNXPxK-dDz3qDIYlDq6bN_BJLUYCJF7-6KbAMgewOHv8jo_ZFgwiPtioneJJGr1v3wNGwXhkk5_XNxxJ_sGCojBnfPagN193XkPIeUrAoPA1lCJh6d7U377R1OSNzCGoSbeajFE8PxCoXTnY5_kySB4J1cOe6jPtCLp-Rd_XGnupA6zsAkIXemmq7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=N6F6DR2MVhS45VhjUqnkqmAKzdWMk6kjN0694K4GDz94D-dYCpXxutxwDuIpgQ7R48G9xbfS1f8iDCxfi_SO0daYvyBuim6cZB1RQfFsn2lX0htqk24Bgu4W3riEGmmIyGhTOqZJ-Z3peJYG1XeNWVwo_ErpNXPxK-dDz3qDIYlDq6bN_BJLUYCJF7-6KbAMgewOHv8jo_ZFgwiPtioneJJGr1v3wNGwXhkk5_XNxxJ_sGCojBnfPagN193XkPIeUrAoPA1lCJh6d7U377R1OSNzCGoSbeajFE8PxCoXTnY5_kySB4J1cOe6jPtCLp-Rd_XGnupA6zsAkIXemmq7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc4nHz4cM8ganPSFOpqeaxZFqvuQKmMVQtBH3u__XQolTsVuTtQYdK8bUSc3cPHSWu0JIyeydvKd_A_xz5nmjiPIV_Wv8saovUXxkilne7kmokUZ1-eFVYcHlxe9hSybGhlyaaVVf3x7m7XfCxC4ROjIV1XShOHbOi4uZ9iX7Jp26ISPffIHW4sJ9VE5UKup0bF0h5O2iROzZmvsN7mjeLKXQgvctiXDewlHwTpqP7RXt4Q9B1XmPjwN1yyBsgAd9yQ5NUs-5X1I2Imw--kvNkKMZGX70droX1CbBa1JWugZPY58X83bs0EdSnd8OXYLiY0xJ_7UiAriJhhwm75LlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=FNfcL9ez-Xu1xJh7C2qKfISJP3BLdzJbsDFcmvQZ5RW6Bq2STAZyZmCfzBZSRGr8qib9OZ_15y_SUyZLbqYxn58mqRi3StQmLLXBkcmadYfbLqAHnpLx2EcEqQEXS4h6EGuFumwAb6GPSRb_hdx8ZeXSoKhOoRlQLcKNqwbSPCM9xRLd5YWKMgQ8rxohQwugBOmVfJbI2NGFxJtGlldLQXM5KSIi1RqtbQTd7TBjlXaxwXq5nvI2SpPUi6L2FoakRTG_KRQxVJJ56KCosGGwAtZLonkEtPSwLLvG5gNIMiaEWZyHido2jsrFu6lhNIZoHtd7RFFLAPPIEjT_cZXlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=FNfcL9ez-Xu1xJh7C2qKfISJP3BLdzJbsDFcmvQZ5RW6Bq2STAZyZmCfzBZSRGr8qib9OZ_15y_SUyZLbqYxn58mqRi3StQmLLXBkcmadYfbLqAHnpLx2EcEqQEXS4h6EGuFumwAb6GPSRb_hdx8ZeXSoKhOoRlQLcKNqwbSPCM9xRLd5YWKMgQ8rxohQwugBOmVfJbI2NGFxJtGlldLQXM5KSIi1RqtbQTd7TBjlXaxwXq5nvI2SpPUi6L2FoakRTG_KRQxVJJ56KCosGGwAtZLonkEtPSwLLvG5gNIMiaEWZyHido2jsrFu6lhNIZoHtd7RFFLAPPIEjT_cZXlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=O7OaDSpZzIN9_ZcKbNUD3KZomHZVkKqpkuqMaTzFU3FQRp6uAZS5TtrW5-W181lDgZrwo5IrRYqn2MwZWAqdEmV8Mqx87Ul-vfvyK2FJHpA5jFxJjz4fHwEkDZcrH0BrRnniCpz_h-BZT_EPmTekPsLIyQKvP6JCVpke34_dVMbmy6Glpw5MtW8el-e6nCrGO9zGij7qpcG23wGB9u-nl_SDv_SueKwuDKiFlawziOCaiBPtHufWbj4JUD1wAWh6fmasy0_u9prWqjZFMJ4nKauULDFYR5fWfwgcpRY80VW6U0jHdFpa0tiXjwZSSqwNn8gO9AKgVBo8pwuEbxWRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=O7OaDSpZzIN9_ZcKbNUD3KZomHZVkKqpkuqMaTzFU3FQRp6uAZS5TtrW5-W181lDgZrwo5IrRYqn2MwZWAqdEmV8Mqx87Ul-vfvyK2FJHpA5jFxJjz4fHwEkDZcrH0BrRnniCpz_h-BZT_EPmTekPsLIyQKvP6JCVpke34_dVMbmy6Glpw5MtW8el-e6nCrGO9zGij7qpcG23wGB9u-nl_SDv_SueKwuDKiFlawziOCaiBPtHufWbj4JUD1wAWh6fmasy0_u9prWqjZFMJ4nKauULDFYR5fWfwgcpRY80VW6U0jHdFpa0tiXjwZSSqwNn8gO9AKgVBo8pwuEbxWRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7HTQxyvyG5sEwWEO9pOBJMr_XDjewyhc7c7psF273nyjoaXbbLbw0gnjAatu-uLTf6wQ9GYuxdXd3cQ87PLh9ZSeS0h_7ojRWGKbHpQ5SO5mFGiX3k6vG3ON03q82HR5zJufLeKZhzpOyChvHQyi_bejrWwsPGNXSeWYxoekf1z0rDw67uLNnSiRr3Um6B0BXIP6JSf0kjeKiv1re48pvWMewlgLk3mpkNzYiRcSVdgYEWesYZ5AigR13rXbLupx4BMt1GnZWiHbi-eJ2TLop6jBNM5itXj0OFWBaIC1QZImANEmgoEkpfasvpKHIyJ4fDBX0cUWEINZowsySpaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u6X53JhBv8J41TVuHnFdbP_zdGNhMHUFZOjfZbha_UwqsY4riBgrIkFJsZRprHa4qFHu9uzbSvWFQ4bLIMB1LdOIZYgG6JvV-UpHU-5ee7IaTD-rV0Wp4RrmyjuZDoZ_DJX31F8vb2DI3wx9TApcYmDTYVA1YVt9PE_1RNT52Utpojtk6rS3zcc9gLmrSIOlpK4edeTwrRIrGZ7Qs3SYoKChDHOBb2lWYexZjvOdZUDVjUUY4Xh3WBYLiteOLBl_mzXMtrcEMXrF6Ht25uWTVnSbfDzvF3VohxZVElQbrkM9uUREOYXIO3V4PoTbZISjH4QSWh604VKmkTOOpZt7Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=Mfn9yxdw7WPS-tjBgOqLCh084PhQtagP3JRbpEotVEBjn5GF6x91v7thuHFnSi903QkODb6Lt6xjLI-gjHws5ugu6kyCApdzDixqQd2KKGL87snODOJhtBIvsVSBV818PYzvg-FgfxqFpCOIxhot3eWX8xFpLBx-7dsNgd_9zlwjnhix8HJrN4D4tSb3lE-U1TrUJq-05g6I1uDKB5YIbuh95w569TEjMvyOOeqQ1ip6PTrcKtwK8IdUfSZj_rZegRNDcE_nJUnUBSEGy-MgdhBE2HXeu8UkLKhj32H6yIr0gjs7-JKUDJ8rJSSSS01oCMCH8aNYWII9mooEx-NzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=Mfn9yxdw7WPS-tjBgOqLCh084PhQtagP3JRbpEotVEBjn5GF6x91v7thuHFnSi903QkODb6Lt6xjLI-gjHws5ugu6kyCApdzDixqQd2KKGL87snODOJhtBIvsVSBV818PYzvg-FgfxqFpCOIxhot3eWX8xFpLBx-7dsNgd_9zlwjnhix8HJrN4D4tSb3lE-U1TrUJq-05g6I1uDKB5YIbuh95w569TEjMvyOOeqQ1ip6PTrcKtwK8IdUfSZj_rZegRNDcE_nJUnUBSEGy-MgdhBE2HXeu8UkLKhj32H6yIr0gjs7-JKUDJ8rJSSSS01oCMCH8aNYWII9mooEx-NzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=Q2YEn5A6qtnsd1kMmWJEZuzNLvp5LHsxV9XtCfd8JJzJMAOOIaxBXY9LCNfsBRAiVxyNXKS9A1pfppf1LhDuY-m7cZb7kyyV_lbIPUhmsDJ4r7lzo6ck4O2MJs4i-a0Zg9-YOc4ZZPhrV7JszsttvJ821Oz9mH1ZVUw4M5C7-gTwvdoOp2JkXZ-AGvij5MFu8kzIqGxlf09VKnb9S4H9xFWFUyYDsiMRpgsFsHKQdUvNnTX_6fk4BPi_XnlwQg7HX5thqM-81jW3ISO8kStSsl_OBiSDFLaZm71XJf3uP2ZhG9IzPvKvfDo5Jw-pVB_0HWDc0EJm0p-jBGWrnvZy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=Q2YEn5A6qtnsd1kMmWJEZuzNLvp5LHsxV9XtCfd8JJzJMAOOIaxBXY9LCNfsBRAiVxyNXKS9A1pfppf1LhDuY-m7cZb7kyyV_lbIPUhmsDJ4r7lzo6ck4O2MJs4i-a0Zg9-YOc4ZZPhrV7JszsttvJ821Oz9mH1ZVUw4M5C7-gTwvdoOp2JkXZ-AGvij5MFu8kzIqGxlf09VKnb9S4H9xFWFUyYDsiMRpgsFsHKQdUvNnTX_6fk4BPi_XnlwQg7HX5thqM-81jW3ISO8kStSsl_OBiSDFLaZm71XJf3uP2ZhG9IzPvKvfDo5Jw-pVB_0HWDc0EJm0p-jBGWrnvZy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlzTNn-QIn5OOBlnkkGHCF64Exy-tga3Jm8VMUq0qy3tUHzuQcccKkXXMMVJXRw7fffHx21eCyTgpUn4JxN5Ua02DgbWGuhnwfYLer8mGU0I6rfx509_1xJtok99jcRCh5VDvT9TwcypZvGh0If0zWn5rcuEuhKAYtn0PAY07S4bSMDO33OTrsXQ09f6q0H74dBdvMC4tWynKcHdtRYL_hZPzUtHoigJcmUafVHKACWeypfdRPYWMRbIAJeTuaiYEU5sT1OmaS79Q41Hs0RYiIdc_Yhau48FqLZn2_QV1SuN_mc4b41Jm3cMKv-0ClTgKxlyUldbZYxhe89ZcPWvoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBolY45Pmrg-svtqmZ9ClS-lE-TAGDD4gpgu3UtQBu2Q6ehc2NnekCNWXrpmowgGemEnRlJkj8x79yEY2OqGnllc4EKMCVvTNlyCGUrN2UVDoFrIBLOAyBJzeFUDlq5XhTnD6XEqGyvRmkXFihV94MFcoVwVTOYlJp4lRFXhGZP84L4qbAX8P9c6QBebTWfXvmOkYCNVXfS6d8tfPEgmOwmluJw79ZJc9MKkmWO5rPvAuSYaj-AFGoBusDkeW3KIx6tAdeNSTY8HFNuIOCyFEw81c4fA163rVv4BlnsC88RTOsPpJn8tAM2Hw70YDo19Jnp6zMcuPbWgfAw5c-O0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ranbaQZhph7d8EBr395uSes1rluXid_DxwQz6h77oZnsmISj9zKBE68Nn5wx2qYyPvtT6Kiva02Y5yInxL8iwxo8Gd7gf1aI2zbF2QGvGYb6JKh1cKNgvYWUUbGZp07_8phvcEVGq4zCgzGYq41TGjVst6j0EQZad4EDa6sb3LnQP9V0fE1zMV49m1WGhQHKC2F4Da6ZESZWKcjcMICC6rgdtYNyDX06CDRddY8fDEMbIKp5gq6k7GahWgX_VOYt_aBG1D8ZsVx4F5pqsqxH2rCPvJERpXu2o2jPXkb4jWf_pZO4fiQoNkULtt5Qf_EJHX1HvnS7QQV8ntUv9SwyfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyBw0t08hbHhRgy_LVPf5NtfCLW2Eu2_-3d73FLinmQisHx6G2txRf4SX1JAIBm0j8c-BttfziR2yfrqtiS6aV_ei7as4N-qOCSbem4fUYsqvV5OTobpV1nLQdx7nCoH_Jy06aExmlVWbnSyk_bEUU_5YxAiarujwcJY4y2UHFURYNORRwdXtFwX-7qw6pKnfCuYi9Ku_Pu8hYnGn6iVdt2xoTbZyjdjHvaYdCYJbHllbMljxVI6_F5h2F7XGGGjC5XZN3ezeyT5jh_OwDBNCuOuhteO4cGXUDUrHgJLFYl2uyTzn6yqaypXKLacuMnFVvOp3mQxcgMI_eTtocWOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=CQbTG-e5iIlGYZgfL29RP68VAcbc7p1BB2BgqyovQB5kSubWGR9ojAmfBGSToiXuXWNiL3Ve2ahVqs50NZBkx5CIrrCyhudCd51JEHR4YMnhwr3IB05CB5bEPutpeoeE4r5Bjou4lJ8_-QQ03M_gI4eABJ3RB8YKHTNnxbEbrENXcAjQL6LoF1HOcO3VhGuJ-w6icn5X7HAsyafH-jy7v9luqmrd3JuvbhIpQV4EwekZqXGD69MLHOcFK6FH4M_IyxU2NwgNjhuXNJENOssRgDpLxJaBDAjOGOzqXljITQHHaRIhPPpqzqQIcLWs2THi_e59wYyoXdGqoTzRVdICQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=CQbTG-e5iIlGYZgfL29RP68VAcbc7p1BB2BgqyovQB5kSubWGR9ojAmfBGSToiXuXWNiL3Ve2ahVqs50NZBkx5CIrrCyhudCd51JEHR4YMnhwr3IB05CB5bEPutpeoeE4r5Bjou4lJ8_-QQ03M_gI4eABJ3RB8YKHTNnxbEbrENXcAjQL6LoF1HOcO3VhGuJ-w6icn5X7HAsyafH-jy7v9luqmrd3JuvbhIpQV4EwekZqXGD69MLHOcFK6FH4M_IyxU2NwgNjhuXNJENOssRgDpLxJaBDAjOGOzqXljITQHHaRIhPPpqzqQIcLWs2THi_e59wYyoXdGqoTzRVdICQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64840">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
مارکو روبیو وزیر امور خارجه آمریکا: ایران به توافق جواب رد داده است
👎
خبر بالا فیکه و روبیو چنین چیزی نگفته
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64839">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کشور عراق، تلگرام رو رفع فیلتر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64839" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64838">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ترامپ: ۹ جنگ را به پایان بردم و در زیر دهمی زائیدم
@News_Hut
#Fun</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64838" target="_blank">📅 16:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eStPN4Mq_-nmYzgaegVwr5NeaB4MmU4Iycneqyi26yYWp8Q31QKJlKRj-0iDKd6UBXtJEaTUUGayR909A6bKbEd16Vf98uebQofnnjyA4z1nJ06CVS-2TT452yNNvKxKyyCiDyhNL1WcgcbrrPFGINKYu7kDxFYrEefIvHMBPjFHLbY2DqjtpzTv6WHQe8bLeE8Uyl9eEC8NV74SM_HUonK48wr4kwK-z8guZB1tK_bnUvdmCWndZ_fy2YPJ2HaTGy9ot5UkVYw6JdmOpc43tQL6ss7Xp2qUar2LC1gjFEEYoaJ-0Ph9ku4Dg82AavoMOL9kKDVKUl3iwWkoge6jRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#مهم
؛ این لکه نفتی اطراف خارک نشان می‌دهد جمهوری اسلامی به‌ناچار نفت استخراج شده را در حجم بالا، به دریا می‌ریزد!!!
اقدامی فاجعه بار برای اکوسیستم خلیج فارس
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/64837" target="_blank">📅 09:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=ci6LInxMGRW-gxA2EFOA6VgfcVIQTc6ZxiHSy1rB4gF5rr6MKg6o-T-fShpa78L_oqBGMFNYwXyuX0_mSfZGhXHK9NrQvVeuQg23hzKoIWgd9iblFIxRK-qhRKUdPw3x9MwgsW9IdQyV88x5HLV9g11OK4wdIN-MNe0voTKbdpqDGIL1mfdXlIiu3NGBVh620HE7d77WGyHa8D1FBXtg4HajQjqeiETyzg_YR88Qcl7uPOYWJSePSWT8S_1LEc0irgr6ob2oTznCq_zrBiW5y1G2TZOKs7SSOzW6dKgJp3fG3ASMQrxRowj6GNy8wZXra2lZguIP13Sk3CaDTP5yQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=ci6LInxMGRW-gxA2EFOA6VgfcVIQTc6ZxiHSy1rB4gF5rr6MKg6o-T-fShpa78L_oqBGMFNYwXyuX0_mSfZGhXHK9NrQvVeuQg23hzKoIWgd9iblFIxRK-qhRKUdPw3x9MwgsW9IdQyV88x5HLV9g11OK4wdIN-MNe0voTKbdpqDGIL1mfdXlIiu3NGBVh620HE7d77WGyHa8D1FBXtg4HajQjqeiETyzg_YR88Qcl7uPOYWJSePSWT8S_1LEc0irgr6ob2oTznCq_zrBiW5y1G2TZOKs7SSOzW6dKgJp3fG3ASMQrxRowj6GNy8wZXra2lZguIP13Sk3CaDTP5yQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آقای رئیس‌جمهور تقریباْ ۱۰ هفته از اصابت یک موشک به یک مدرسه در میناب می‌گذرد. چه کسی آن موشک را شلیک کرد؟
🇺🇸
ترامپ: این موضوع الان تحت بررسی است و ما به محض اینکه گزارش را دریافت کنیم آن را در اختیار شما قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64836" target="_blank">📅 09:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
ترامپ: می‌خوام کل ماجرارو تموم کنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64835" target="_blank">📅 03:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
ترامپ: خواهیم دید چه می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64834" target="_blank">📅 03:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مارکو روبیو: متأسفانه، تندروهایی که دیدگاهی آخرالزمانی نسبت به آینده دارند، در ایران قدرت نهایی را در دست دارند.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64833" target="_blank">📅 00:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64831">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dikosWYjQ8vd0R851x7hn6tMPmAMtzdijEapqc6tC9yXECkZFGGtEmiarOd1tmVXRlIfWL9AxcuojpJDFycLj5Jb7Xh06V-kb-ij2zMvyE82K2y9kTfQrb1UyGYcJMg_he32GRnenJR82mf7ZrgSSIHH9k9LLVZ2lYTI6E6lY8cbEPXpXr2EyGtIgPSwFpeZv78nCAX-aIcuBYSSsOtR6zYckvakwP8KWQwuXehUbdHR9nreRwHOlRIw3mpf63CoU4l42i4La_gy1vBz3yjigFx9aw44Tz5HHHGp2NvrpxCr1Qu7dsLyMwbHi9uC8HfnHWdDCI_tkdN-fAOGG-FqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHnAWWsLnDLxeiUHfB0ssz4QP7ZYvYzq1RyW0fKP5Wx-1IgjWOABdAfjsnTzLxcdnqhwlUsksVAJx_z6Kp_f8xP09lmBWTjegZDvhdMh2QMffONNsCXTYPLz-xai2ccBEluDX1dE8IQLEeR5YKV85EDuh1XriJyb5NI1Rr9UqHzod6PoyP_Le3U3m6LeKEc4WPVMpI8e-sTUXKQgh6Sz-96CDOzuGH3KbxpiADtwro0DXoMqlb33WX1Cg_2kE_9LY5o9LTF222urYUtP9wJZrBtOJdwyCbEe00-OhvqL01DyvVFMso8nj7LAc3CL7AUDnChLgRsbwPc0-567hiDp9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZVc_fbi7Dyf0NckJ3PQUKJumWKbH_FVrfWjMNwkamibvkavcWyQFaZ1hct4yB0KaTqitGQ-klqNo5CTLSXHrp0ythVeZBbfSDuZ4lY1wg04qC4KkdtylMeI5KVUtqoZDigcLCuKkuRtJZhGkfrqsSg4t2FWMX51QPbC4bC8AsNwGRSlyZH840vG582-OwjCEXLFThxBr6syCAZi9SMQpzsalBH_kQcmPZFuxB-4-qmFKwWURmGVGVVo9SFYRaqVePp6TANCt6mfmrbe-JQZ649rT09Ipy76GRJjkNkXL3KVqmgttcQDuWF2snogEud9DBDQEkpBkQVgt6Ts4zF3M3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMt1u0c2WwJv3l4KZKjVUlKT552O4hOYrX6VZnpbtJAzy-d9sYRR7_jp5oCMs0OXZF0uWs8_unV2obaGDvSFNo43jBxxZaSqs8aSeX72yf8V_DEV6qnXGvVibGXJp5ZaDmwGhDO1fxcyWPmm3FBrDyHLPjPPDU1iH4epcuaxjUBeMBWfEZfNDyFSupJdNH7TM7afXwAkAJYECbTWTJDvvEFvhWJtScldpczaRUwxWBrSDARLDybDIMb3mntB6lR8Fi9pNGJCA8KfSuOGHebKGiadKR-Pw0hVJdnX77osZpwIxvlL0bKiUedj4N7YMCtZQWItbiC18gq3AA4IP-Ek4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فشار جنگ کم شه
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64828" target="_blank">📅 00:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64827">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=IiD2dfkF-VRRnejFcbM8h8rMJKgZXG4POqwnwMcx-1-zaoHiLLSEnoOQe8i-Yfw-wMjvgZPJo1TB7vCeG4x5Av9BLG5DIWiU9cXKHoB88EE1OaigxvN1j8wo7lgJUcIOPwtk5YcGqVag_i2qLlCX0jyheqjHsnrK2JKy8AYclZF2B-7_TGGu8N3mS8CJIpzL-jmoa1g2m0rewWeIL73ruRtuan0DoIPq_X7XlEeAqgfkhar2YPXPz5vNwa_CcZuEbNz2ULbztOQ3e6fmEShPCamr_DgsnWIL78WYb8YMjYk6kUslqSn_cuI29ETunBOLPh0aTtWY6nsYdO0xzOvEcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=IiD2dfkF-VRRnejFcbM8h8rMJKgZXG4POqwnwMcx-1-zaoHiLLSEnoOQe8i-Yfw-wMjvgZPJo1TB7vCeG4x5Av9BLG5DIWiU9cXKHoB88EE1OaigxvN1j8wo7lgJUcIOPwtk5YcGqVag_i2qLlCX0jyheqjHsnrK2JKy8AYclZF2B-7_TGGu8N3mS8CJIpzL-jmoa1g2m0rewWeIL73ruRtuan0DoIPq_X7XlEeAqgfkhar2YPXPz5vNwa_CcZuEbNz2ULbztOQ3e6fmEShPCamr_DgsnWIL78WYb8YMjYk6kUslqSn_cuI29ETunBOLPh0aTtWY6nsYdO0xzOvEcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی مسئول دفتر علی خامنه ایی درباره مجتبی خامنه‌ای:
خونه اقا مجتبی رو زدن ولی ایشون تو راه پله ها داشت میرفت طبقه بالا و فقط موج انفجار بهشون خورد و افتاد زمین.
فقط کشکک پاش و کمرش آسیب دیده که کمرش که خوب شده و یه خراشم پشت گوشش برداشته ولی الان خوب شده
مردم صبر کنید دشمن الان میخاد یه فیلم و عکس ازش بیرون بیاد که کارو تموم کنه به وقتش عاقا خودش میاد باهاتون حرف میزنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64827" target="_blank">📅 23:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64826">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2VAjTuBv-5Pbx4WOI7loUvx1Lf6iBUXusBQ7evO3Bd-7EbpeFVUInzhOW_yQmx2coAh5SqTPtHcp9aq7FPqxAy2UUirNj9WwIVuU_4FoxjdhxAaoU8ign4bKHNWZpMD3ls_HPJpNrrwvJVly33zNAdY9dt739xjOs5snkziyNbUEo3lXALKcYGXF69b-l4zuUP1wXwUVM4stDtrEooBHwdJEcLtv7jQutIufbh_J-huo63pTyVoupYWcYJWuqMQivcCfh0MiT_UxTil3bX9h5hLR3q58z9GWomWMIOkq0U23kAW01eBr3CJCQ8Cs3818uqYXbfl0AUABu2hC-93PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ ۳ روز آتش‌بس بین روسیه و اوکراین اعلام کرد:
خوشحالم اعلام کنم که آتش‌بس سه روزه‌ای (۹، ۱۰ و ۱۱ مه) در جنگ بین روسیه و اوکراین برقرار خواهد شد. جشن در روسیه به مناسبت روز پیروزی است اما به همین ترتیب در اوکراین نیز، زیرا آن‌ها نیز بخش بزرگی از جنگ جهانی دوم بودند.
این آتش‌بس شامل تعلیق تمام فعالیت‌های نظامی و همچنین تبادل ۱۰۰۰ زندانی از هر کشور خواهد بود. این درخواست مستقیماً توسط من مطرح شده و از موافقت رئیس‌جمهور ولادیمیر پوتین و رئیس‌جمهور ولودیمیر زلنسکی بسیار قدردانی می‌کنم.
امیدوارم این آغاز پایان جنگی بسیار طولانی، مرگبار و سخت باشد. مذاکرات برای پایان دادن به این درگیری بزرگ، بزرگ‌ترین از زمان جنگ جهانی دوم، ادامه دارد و هر روز به هم نزدیک‌تر می‌شویم. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64826" target="_blank">📅 23:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64825">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuV8DulYzfMIr6XaBDUH6flTEu_XIZNl-dZdofZM6-rdB1Oni-IxC7p17U5puT1kUNmb7E7wZjfv5OAQ0mKfd_YPlRiSSxovDdNU3m_lGmLmkiUIaynu7M23nvh8ebIorCGyrid4OdrFZ16bE4WfTOPXmwzq-s0Eou3k0k2Ee3GcxLgxdSom59oxmUJErSPE0EKWIJzlCyaYMjuzz-CXAFmhXrq-nTz3fYr9f9Lyt-Miwb2brIvpoYbqz2VI8g1ibFrjfCCva3ljYoqqS13Ms6Dg1Ins3XsbTwjv95wW4QeRffa9RPzPoWVaG8pA4lg83aS9Bjjhb2je7R0YInmSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
در مورد وعده من به شما، وزارت جنگ اولین دسته از پرونده‌های یوفو/یوآی پی را برای بررسی و مطالعه عمومی منتشر کرده است. در تلاش برای شفافیت کامل و حداکثری، افتخار داشتم که به دولت خود دستور دهم تا پرونده‌های دولتی مربوط به موجودات فضایی و حیات فرازمینی، پدیده‌های هوایی شناسایی‌نشده و اشیاء پروازی شناسایی‌نشده را شناسایی و ارائه دهد.
در حالی که دولت‌های قبلی در این موضوع و با این اسناد و ویدیوها شفاف نبوده‌اند، مردم می‌توانند خودشان تصمیم بگیرند که «دقیقاً چه خبر است؟» لذت ببرید و از آن لذت ببرید!
war.gov/UFO
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64825" target="_blank">📅 22:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64824">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
چندین تصویر افشا شده دولتی از اسناد بیگانه‌های فرازمینی، پدیده‌های هوایی ناشناس (UAP) و اشیاء پرنده‌ی ناشناس (UFO):</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64824" target="_blank">📅 22:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64822">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=M2LLYpdmztccurgsEb6NwcjZo51aOVYAwmSFNJXH7KpTP8iJQbuRUnb59mkTwhMlLZrzKDKajFXqhz8RZvrQ1wAIZhWzFtsBWvD6M8usPbtspcYfb-o_sOGAgWzekuiBrEAjDXvYgO0IlRPfYskzeW1qYqlZiEYajoHthq93RuueaPmUi3FQYsEd1LPrI0YnctpwTNzVKUQzPFbXNdyTfsfZP-Q6DqaeXwkkzQoxCv8Pq21gs-BHnnWU-ircSr5q8oC7_iOM94dyN0Amto6NS_cCXiBbCwsNVoEyrRVRtbmcxIDDr0hzfDmGDYIl03GpsjjlsHT_itEgubSJghyMXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=M2LLYpdmztccurgsEb6NwcjZo51aOVYAwmSFNJXH7KpTP8iJQbuRUnb59mkTwhMlLZrzKDKajFXqhz8RZvrQ1wAIZhWzFtsBWvD6M8usPbtspcYfb-o_sOGAgWzekuiBrEAjDXvYgO0IlRPfYskzeW1qYqlZiEYajoHthq93RuueaPmUi3FQYsEd1LPrI0YnctpwTNzVKUQzPFbXNdyTfsfZP-Q6DqaeXwkkzQoxCv8Pq21gs-BHnnWU-ircSr5q8oC7_iOM94dyN0Amto6NS_cCXiBbCwsNVoEyrRVRtbmcxIDDr0hzfDmGDYIl03GpsjjlsHT_itEgubSJghyMXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیو سنتکام از حمله نیرو دریایی آمریکا به دو نفتکش ایرانی M/T SEA STAR III و M/T Sevda که سعی داشتند از محاصره عبور کنند؛ این دو نفتکش پس ازحمله متوقف شدند.
این دو نفتکش تلاش می‌کردند در یک بندر ایرانی در خلیج عمان پهلو بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64822" target="_blank">📅 21:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64821">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
📰
فاکس نیوز به نقل از یک مسئول آمریکایی: ارتش آمریکا امروز به نفتکش‌های ایرانی که قصد شکستن محاصره را داشتند، حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64821" target="_blank">📅 16:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64820">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: امروز پاسخ ایران را دریافت می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64820" target="_blank">📅 15:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64819">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0GPe5n3RIpJqHVTUspt5w4eZuCNPAWtkau-6crJxXqTuojtQGRe_Dj5Yw6A5tILvzzBNpsBXkmZgB1-DHXMsus7HI9hRACmpVi_nQi6Fkg2gycCdhCQQGJmlyzAy63xqs1bjWd7y_NyzjaxfKTsePMoTUhI6d7xMQB2_1HtHWqyZZv5eHgPOKw6WkdKF_-ww-jx4WsXRsc-Dv3WtkFZqAXrRHxXHtVDjM0rskZBB2tzJMiUai_yFaL7hfuTOw7TBJWkAkMWGYH7OilPYWSQJeP--RWA4vaEZeEaFRAAIoYak7miMxqdz6-dfzDPRV6E3EFjYBncEuC2u7UU8TMUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات که نه، حتی اسرائیلو هم بزنن ترامپِ کاکولدزاده وارد جنگ نمی‌شه، چون سفر و دیدارش با اون کیری‌خانِ چینی براش مهم‌تره #hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64819" target="_blank">📅 15:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64818">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64818" target="_blank">📅 14:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64817">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64817" target="_blank">📅 14:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64816">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">باورکردنی نیست آخوند ۷۰ روزه که مردم ایران رو از داشتن اینترنت محروم کرده، چقد شما حرومزاده‌این که دارین رکورد می‌زنید
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64816" target="_blank">📅 14:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64815">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=ZeJrC45IjwL94D60hyJM-h4fZPIuu-S8wxOHjn_mboNFjX92RwKLK_Pu7PkaUJSC6UqhmfX1Lc19CRZYCoMFZGjruiV7Z8achFwUPrxyGNd6Gr81LtLazA8FfQ9C1dcnucpY7RKh1-0qI5oCbrm9yBxUADLRn7ooB-YlkgRA-wo9BPCyIZdWMfZ0Y_DdfxUQLV696vZM1RTgjpl-6MC3cUcbzof6db-3WSt8zVhKpwuaN2R1tnDjer1J7G_K3DO0VBJAo4cxGIvyx-JwEffvGI1-i8k63zsPWcmwFvCM1ISoHAtlUsRreDqu3Th6ngorZE5P37lAHjma3uR5jg6Y4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=ZeJrC45IjwL94D60hyJM-h4fZPIuu-S8wxOHjn_mboNFjX92RwKLK_Pu7PkaUJSC6UqhmfX1Lc19CRZYCoMFZGjruiV7Z8achFwUPrxyGNd6Gr81LtLazA8FfQ9C1dcnucpY7RKh1-0qI5oCbrm9yBxUADLRn7ooB-YlkgRA-wo9BPCyIZdWMfZ0Y_DdfxUQLV696vZM1RTgjpl-6MC3cUcbzof6db-3WSt8zVhKpwuaN2R1tnDjer1J7G_K3DO0VBJAo4cxGIvyx-JwEffvGI1-i8k63zsPWcmwFvCM1ISoHAtlUsRreDqu3Th6ngorZE5P37lAHjma3uR5jg6Y4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دلیل اینکه عملیات “پروژه آزادی” را متوقف کردم این بود که رهبری بسیار خوب پاکستان و رهبرانش و فرمانده فیلد مارشال و نخست‌وزیر در این موضوع خیلی عالی عمل کردند.
آن‌ها از ما خواستند که در زمان مذاکرات این کار را انجام ندهیم.
اما اگر لازم باشد، دوباره به آن برمی‌گردیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64815" target="_blank">📅 09:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64814">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64814" target="_blank">📅 05:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64813">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64813" target="_blank">📅 04:53 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64812">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64812" target="_blank">📅 04:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چالم کنید جاکشا.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64811" target="_blank">📅 03:03 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
