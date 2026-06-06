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
<img src="https://cdn4.telesco.pe/file/SV-X8qIEAhCrTii2W2xyXwK5q9buMEONZifqd3Y2RFsMyEtMQyS_nqAkmAULgEJfchOSINOtIxXqXl9Esij153xnEfP8DKKipNFiEL7V0dl42pdTM8N_7N3UUNK0MRXqF8HZImQv7xd9kN1W4E0nR_jrm3_USHNNX2Y1G1r5Gjxms0gTYJ6jlfeInGe5Mb4WqpoSYElNSJZJ1J9XWwdUzPl2LX5WHNqusxiLX5iTuTjsFAcLZqh_Z-Nbjw-V8drurRMysr6mkJZQ-0q070DId3KFjw68dJukJ8FbcRepvRkhTrNTlB0f8YuyI9oo_28nsJNMoJey8Lb4n1A-I-tj2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 22:15:48</div>
<hr>

<div class="tg-post" id="msg-132888">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 111 · <a href="https://t.me/SorkhTimes/132888" target="_blank">📅 22:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132887">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
‼️
مجتبی فخریان، وینگر پرسپولیس که به صورت قرضی در ملوان بازی می‌کند، قصدی برای بازگشت به پرسپولیس ندارد و به صورت دائمی جدا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/132887" target="_blank">📅 21:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132886">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 250T کاربر نامحدود
30 گیگ 300T کاربر نامحدود
35 گیگ 350T کاربر نامحدود
55 گیگ 450T کاربر نامحدود
100 گیگ 650T کاربر نامحدود
دوماهه
50 گیگ430T تومن کاربر نامحدود
70 گیگ 500T تومن کاربر نامحدود
150 گیگ 750T تومن کاربر نامحدود
200 گیگ 800T تومن کاربر نامحدود
سه ماهه:
120 گیگ 730T تومن کاربر نامحدود
160 گیگ 780T تومن کاربر نامحدود
230 گیگ 850T تومن کاربر نامحدود
320 گیگ 1T تومن کاربر نامحدود
400 گیگ 1.2T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/132886" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132885">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
مسئولان پرسپولیس به اوسمار ویرا، مربیان خارجی و بازیکنان خارجی تیم پیام داده‌اند که هرچه زودتر بگویند چه زمانی به ایران برمی‌گردند و برنامه برگشت‌شان را مشخص کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/132885" target="_blank">📅 20:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132883">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
از عصر دوشنبه تمرینات پرسپولیس شروع میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SorkhTimes/132883" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132882">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
در صورت برگزاری مسابقه، این دو دیدار در تاریخ 5 و 9 تیر برگزار خواهد شد.و بدون تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/132882" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132881">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
کسری طاهری تا سال 2028 با روبین کازان قرارداد داره و الان قرضی توی پیکان بازی میکنه، هر تیمی بخوادش باید با کازان مذاکره کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/132881" target="_blank">📅 19:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132880">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">#منهای‌پرسپولیس
🚨
کسری طاهری مهاجم تیم پیکان تهران با پایان قرارداد قرضی اش با پیکان به روبین کازان روسیه پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/132880" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132879">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#منهای‌پرسپولیس
🚨
کسری طاهری مهاجم تیم پیکان تهران با پایان قرارداد قرضی اش با پیکان به روبین کازان روسیه پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/132879" target="_blank">📅 19:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132878">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcce26bb71.mp4?token=ntTYTl3LSqgsLxNuLP7PTc_Vp2cYk7dQcsxmRbb6lV54vSvuQE5gyPm6Yuk7pxU4HIEEBGPpC8EakRjIB2VVlSip1-j-O0nV6Y3a6KAlgAk7vn5Tsqb8ACWM7SFpABP1STuwoXb7NVhDNxOnwIqVx8ojESEbSx4zBCex4OTrDLlN_2jeOz64yKGYM7f-lStZ--IQokszcNWRc7qBFu3J-sa4AyZePT_kzLC_rC1LodBOtmbgpso8lGNywV-rT2-NugZ9p1ckgxTfTMp-F97Yxyovp0tL_Qmo8JbvaoaE0_5M1HFz04zaCMA-xHKmOmOOiBb_wJyYKDAxFHVHnP2G_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcce26bb71.mp4?token=ntTYTl3LSqgsLxNuLP7PTc_Vp2cYk7dQcsxmRbb6lV54vSvuQE5gyPm6Yuk7pxU4HIEEBGPpC8EakRjIB2VVlSip1-j-O0nV6Y3a6KAlgAk7vn5Tsqb8ACWM7SFpABP1STuwoXb7NVhDNxOnwIqVx8ojESEbSx4zBCex4OTrDLlN_2jeOz64yKGYM7f-lStZ--IQokszcNWRc7qBFu3J-sa4AyZePT_kzLC_rC1LodBOtmbgpso8lGNywV-rT2-NugZ9p1ckgxTfTMp-F97Yxyovp0tL_Qmo8JbvaoaE0_5M1HFz04zaCMA-xHKmOmOOiBb_wJyYKDAxFHVHnP2G_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
حضور علیرضا عنایت‌زاده هافبک جوان سرخپوشان مقابل فدراسیون فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/132878" target="_blank">📅 18:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132877">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGC6mC-6scblIIIqK6UOxxWJGt4wZDHWVoCNEpZF0FK6wPPeocNKytWeEK1flxW-LtQdJy7lWRHvQ8uE5lS1UhC0z9zxsqwh8mpIDT4e8p9U7Cf6vHpJBKXtvCHJoCKDPYYlThMr76B79MnZlWY5rcaEmBNQCTGc8QYZHdfag7SSbAWydvd0MhrM-qV1o0nWV26-m7WH9IozoZR9dxvFc69he7HzZ-7oTnWMWe3jQMv2UDJzyAFibIF1VbDpnOBgZp2COaHNkU49YaQg2aYvtkb4tHElNdacVkA-U_5fUKCQJxULTtWv5O52gH3y6hqz0ki1x7WUbI4sjs1lbaeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/132877" target="_blank">📅 18:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132875">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/132875" target="_blank">📅 17:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132874">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
جنپو با گاوداری قراردادش رو فسخ میده و طویله گاوداری باید چیزی حدود 4 میلیون دلار به این سوپراستار غرامت بده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/132874" target="_blank">📅 16:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132873">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SorkhTimes/132873" target="_blank">📅 16:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132872">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/132872" target="_blank">📅 16:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132871">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
پایان دعوای سهمیه سوم؟
🔸
امروز جلسه‌ای برای تعیین‌تکلیف نماینده سوم ایران در فصل جدید مسابقات آسیایی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/132871" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132870">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQtbnjjHvOW2Ea_mneKHFsZh9Fq4EW_SDMc4XZIaQ8ysOrU4yDc_t00rJGv9wnTTTnbA7CoCdxqnQgs8RjyEPLytm5v21UJ6NcpmqvseiEGZwKHB1cEYM_aLmTWZ4WY8zrInMK6iKZI5vj0hmHe4qcklPT1T2WWE3suoQA98WT11qifYfxoduQtN6qVZ2ehfE8iUF1e10181Rv-nqeOl_DlruXp5F6QZC0Mbyq6JZmSVwhfGd-rNKv33qGZhSWc2weEH2NxJBJzPfFN4vjYgKcjt3U-pAWEFL1owMPZ1Yr5s7JN8657Bkbkiqf-KkpDsE-OnrFYSH-OXfN-qcB2ZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@Winstn_Churchill
https://t.me/PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/132870" target="_blank">📅 16:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132869">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
باشگاه پرسپولیس پیگیر پرونده سینا خادم پور و دریافت 2 امتیاز به علت غیر مجاز بازی کردن این بازیکن می باشد
❌
یا در غیر این صورت کسر شدن امتیاز این بازیکن که به استقلال و تراکتور داده شده
3⃣
احتمال تورنومنت 3 جانبه وجود دارد و طی جلساتی سهمیه سوم آسیایی…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/132869" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132868">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGIrZt5iwRP5fhVDpg_vHwTGMkRpx_CdZugsQP_q7zDOI5p2-CMhml8kAAaX-PkKJcV_Dbhv5Hv1k3qowxkwQf5lVDu87xrUle4oTpqhcVc-lc16k6bTJaold20V2Rsrnye1EaYWpapCQB5k_urhOHBVdnT4028oDjY-UWNHhUT2bIJW3sui7-SHUDUZm1mDB2O5J1Q0zGs39--IihHdLDmgqqnNc7MW44uqAEnX0K8CggF5bQ5eeaHi8MYMeClhYuRDN4347miHPlaYfhKRLuYbldtXFXv5qOZMlN_GblTebRsFmQ0qcxFn8i6hUHju2MXD4a_9iPw3rPfITk5woQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۸ جفت برادر تو جام جهانی ۲۰۲۶ حضور دارن:
- گیلا دوئه (ساحل عاج) و دزیره دوئه (فرانسه)
- اینیاکی ویلیامز (غنا) و نیکو ویلیامز (اسپانیا)
- دریک برابی (غنا) و برایان برابی (هلند)
- جان سوتار (اسکاتلند) و هری سوتار (استرالیا)
- لوکاس هرناندز و تئو هرناندز (فرانسه)
- کوئنتین تیمبر و یورین تیمبر (هلند)
- لاروس دوارته و دروی دوارته (کیپ ورد)
- لئاندرو باکونا و جونینیو باکونا (کوراسائو)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/132868" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132867">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/132867" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132866">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
چه پولای خرج کرده اقای پ.ج
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/132866" target="_blank">📅 15:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132865">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/132865" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132864">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
با رفتن سروش رفیعی شرایط تغییر نمیکنه امید عالیشا هم باید بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/132864" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132863">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132863" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132862">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
❗️
پل پرسپولیس برای صعود به آسیا
🔴
باشگاه پرسپولیس در روزهای اخیر پیگیری‌های خود را برای رسیدگی به پرونده دیدار این تیم مقابل ملوان افزایش داده و امیدوار است با استناد به موضوع استفاده از سینا خادم‌پور، بتواند ۳ امتیاز این مسابقه را به دست آورد.
🔴
برخی منابع…</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/132862" target="_blank">📅 15:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132861">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c98a8b0a5.mp4?token=E5Pmu-PtqI1JxeshtOQHA3T97v5nVexLvI3OZOrffDDz3sj-Nu0a-IhhmMrEsPO4ijAsYVnaitNkA300PqOktua7ulimKnJLQM0_75LfXosMdPh0jur1u7nvKFBBlHQVB60cVgr7pI3ekZ_1OeWHNTMXwzG7xropOMOwtWrXI1b4hFcK2AwVCqU-Lmwwz1eakJLrF5NNT_Hfy_UbBUtEgAhMF26Zzrh339uOmZ4Rza5NpCfT8F3zukMmAXSMaSJ4xT_2qKZRH10Ukb53xgJRQVb8ZxQz1sL-jQJFkzjKbaOPK3ZYlEXPqSkA2FIN9uYdfq2Jo2T0skSc-5PDIvtv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c98a8b0a5.mp4?token=E5Pmu-PtqI1JxeshtOQHA3T97v5nVexLvI3OZOrffDDz3sj-Nu0a-IhhmMrEsPO4ijAsYVnaitNkA300PqOktua7ulimKnJLQM0_75LfXosMdPh0jur1u7nvKFBBlHQVB60cVgr7pI3ekZ_1OeWHNTMXwzG7xropOMOwtWrXI1b4hFcK2AwVCqU-Lmwwz1eakJLrF5NNT_Hfy_UbBUtEgAhMF26Zzrh339uOmZ4Rza5NpCfT8F3zukMmAXSMaSJ4xT_2qKZRH10Ukb53xgJRQVb8ZxQz1sL-jQJFkzjKbaOPK3ZYlEXPqSkA2FIN9uYdfq2Jo2T0skSc-5PDIvtv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جنپو با گاوداری قراردادش رو فسخ میده و طویله گاوداری باید چیزی حدود 4 میلیون دلار به این سوپراستار غرامت بده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/132861" target="_blank">📅 15:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132860">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">💢
با حضور در لیست تیم ملی، میلاد محمدی سومین تجربه حضور در جام جهانی را خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/132860" target="_blank">📅 15:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132859">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
اوسمار ویرا به مدیران پرسپولیس اعلام کرده است که به پتانسیل رهبری امید عالیشاه برای فصل آتی در پرسپولیس نیاز دارد و این بازیکن حتما باید به مدت حداقل یک فصل دیگر در پرسپولیس حفظ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/132859" target="_blank">📅 15:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132858">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132858" target="_blank">📅 14:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132856">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/132856" target="_blank">📅 13:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132855">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚡️
⚡️
۴ بازیکن استقلال از حضور در تمرین منع شدند
⚡️
⚡️
عارف غلامی، ابوالفضل جلالی، آرمین سهرابیان و موسی جنپو با تصمیم سهراب بختیاری‌زاده سرمربی استقلال از حضور در تمرین آبی‌پوشان منع شدند.
⚡️
⚡️
آن طور که پیگیری ایسنا نشان می‌دهد، دلیل کنار گذاشتن غلامی و جلالی…</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132855" target="_blank">📅 13:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132854">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
👈
تهدید جدی تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132854" target="_blank">📅 13:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132853">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
پرسپولیس نمی تواند نسبت به رای بازی گل گهر و چادر ملو به cas اعتراض کند چون فقط دو طرف دعوی همان پرونده حق اعتراض دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/132853" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132851">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
محمد مهدی نبی مدیر تیم ملی، هدایت ممبینی دبیرکل فدراسیون ، مهدی خراطی مدیر اجرایی تیم ملی، سیامک قلیچ خانی مدیر رسانه ای ، محسن معتمدی‌کیا مدیر روابط عمومی و یکی از آنالیزور های کادرفنی به همراه افسران أمنیتی تیم ملی موفق به دریافت ویزای…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/132851" target="_blank">📅 11:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132850">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132850" target="_blank">📅 11:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132849">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f698e5343a.mp4?token=VjKQ-YE1retLC9LOSHmy_rc6Fyl4rENld87uX3mik_ds5-FPsvIwPaADJ9ZRbn1XPovHHYcjPrTPyfnrnLWGuvnojLUolNdKDDs6OmAcSwPTJy_hLBZv45NCoi_GwT6Z7YFuNz_wW2BltfYzBfg2vul7tEb_6-1yOM_GE0kdel3UU9CUhHc0pmQuytMUj6MsS5l9WU46TJPzTTcPUTAyko6gTUKHvIIdxwvRnP6MgmDtEkoJF_DjAsHcqJ5Kdp5EzaYJdsyIiQObOUFzVM96iJuWpiR2dWTgRjUFRMeTuARzZxEhxtFjJmryox2fKx4dBiYMLS65u1-s1hPRTabmsasVlqxXbJPvvCHNT0cxovGyRqNz59FYytnddwoeMPJbnWMRMVyYbjxwAV1D6NPo9ry0MdViyNMCH5aMeYBgYRyn65GJub7L_YSlkTt61Q005rNXshjkzKYuuhWhoo1HjmmbTY-v6A3FP6YAMRW5cTvhq9Gao1oK-ABRFVUUbQL1WmifJNy05TMBooJnVivXTRFsyv8vvlyFMfUBqtzMiVDveWkWXp0XOu9Y00KR-LsrAmsr28-OIovwovY5cNymdYpMHXjT3AsuqIMGOH8hjfXh0aEwt3rw75aPFsasMKBiIe0msIZUN_crrMeAX9Dz5laprOqJCyCUfot7pJJo84M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f698e5343a.mp4?token=VjKQ-YE1retLC9LOSHmy_rc6Fyl4rENld87uX3mik_ds5-FPsvIwPaADJ9ZRbn1XPovHHYcjPrTPyfnrnLWGuvnojLUolNdKDDs6OmAcSwPTJy_hLBZv45NCoi_GwT6Z7YFuNz_wW2BltfYzBfg2vul7tEb_6-1yOM_GE0kdel3UU9CUhHc0pmQuytMUj6MsS5l9WU46TJPzTTcPUTAyko6gTUKHvIIdxwvRnP6MgmDtEkoJF_DjAsHcqJ5Kdp5EzaYJdsyIiQObOUFzVM96iJuWpiR2dWTgRjUFRMeTuARzZxEhxtFjJmryox2fKx4dBiYMLS65u1-s1hPRTabmsasVlqxXbJPvvCHNT0cxovGyRqNz59FYytnddwoeMPJbnWMRMVyYbjxwAV1D6NPo9ry0MdViyNMCH5aMeYBgYRyn65GJub7L_YSlkTt61Q005rNXshjkzKYuuhWhoo1HjmmbTY-v6A3FP6YAMRW5cTvhq9Gao1oK-ABRFVUUbQL1WmifJNy05TMBooJnVivXTRFsyv8vvlyFMfUBqtzMiVDveWkWXp0XOu9Y00KR-LsrAmsr28-OIovwovY5cNymdYpMHXjT3AsuqIMGOH8hjfXh0aEwt3rw75aPFsasMKBiIe0msIZUN_crrMeAX9Dz5laprOqJCyCUfot7pJJo84M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هوادار پرسپولیس: سهمیه آسیایی حق پرسپولیس است. شعار سیاسی نمی‌دهیم. طبق قوانین جمهوری اسلامی تجمع کردیم. سه ماهه درآمد نداریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132849" target="_blank">📅 11:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132848">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
استقلال با پنجره بسته خلیفه رو خرید و ما با پنجره‌ی باز همچنان اندرخم یک کوچه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132848" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132847">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqmwOfxkxLT-7WNs7qtuKqYrScAWmPI7dNfCD-rEUH18GTcf0CxpwSu9wAJmBBL0osjjxwktNCJ8gQCGlv7QiL9zlS7-VgEibJYXBVFTTtW8GUq1DqMby_cqFHLsLhsort5Iqaw1rIDK3qlgNd4XmtcwP2jR7skcbXFCYV6pIF1U-uqu2gXKnPvW0eN_07MVKBNSS2wiu30LibxXDN908dREdN1XfUBtVsGoljqTT8CnZRWAlyPueBVSn89KLjD0kGMtd5L2LDZP9oHU967U2xBt1-Zj7KVOIFlAKEkmBim5-tdAuSw-JsWUtswL2pdt7_zYgUT-NlHzFWbnFNOASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132847" target="_blank">📅 11:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132846">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAGm8LJflm_vgbXb9NbIVLQzF3oA8OY8jjIYzow8xYD290NZOpSZy41ruqXWAx5WXLfwBczKHRwksSGGjWHlfy_ukhyf9f6t0foJ0UNn-sNgrxcO6hfnrv4VN1iUethFZSUJ4si-KQyFuf9PLK2ZrhgcFLcMN96Anhdlvh13Jzozl1qN90vQZsXqYhPRcAsohBEWoV3PAoByhXZIW-Cp1qyt1ECFY2FnTZ2XWjFb6U6VIRsYNrM6ZT4JOfh0GbR524h9DXQqu76ESyLDWOS9Q2vv1HQqNPlnacnQLYR44etwOtkv7pTdHcuF5gpPirGJbclSQR0A1MewsXz2ZdRaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
اوسمار ویرا به مدیران پرسپولیس اعلام کرده است که به پتانسیل رهبری امید عالیشاه برای فصل آتی در پرسپولیس نیاز دارد و این بازیکن حتما باید به مدت حداقل یک فصل دیگر در پرسپولیس حفظ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132846" target="_blank">📅 11:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132845">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوووری/ حدادی مدیرعامل باشگاه پرسپولیس: در صورتی که سه امتیاز بازی گل گهر و چادرملو به باشگاه گل گهر داده شود به فیفا شکایت می‌کنیم. چرا باید فدراسیون فوتبال در روز تعطیل رای صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/132845" target="_blank">📅 11:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132844">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=MYsd0Ra52OVxPBEnaMkLc8aQktsMDVRM-mwBA60JcGGTKbMNy1l3MKcI428RYZ9pfIHDptjMc9dxvLXXLgCdI3JcaZolPuxpoA9ybAayCLWIELTQ3QIsX3arhGV-hCwnShqIzmTAK277E7XR2WrLjX3rYJm1jeZunb8aErHimcuF0G4ciWHZNVhKrArqMDPzzijUn426GE-RfJ94hS7buFnxfAm0yNNkgwb2I_HzdSsq67yfRGrjcI81XygCYaFSdBwVGJ_X-_acqdzdh8DNU66mJpE9pFgnN695tvdrmKJ1d9fwaVgXfNkWXLndDkL1exJMYWhrqeullfhap4QGyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=MYsd0Ra52OVxPBEnaMkLc8aQktsMDVRM-mwBA60JcGGTKbMNy1l3MKcI428RYZ9pfIHDptjMc9dxvLXXLgCdI3JcaZolPuxpoA9ybAayCLWIELTQ3QIsX3arhGV-hCwnShqIzmTAK277E7XR2WrLjX3rYJm1jeZunb8aErHimcuF0G4ciWHZNVhKrArqMDPzzijUn426GE-RfJ94hS7buFnxfAm0yNNkgwb2I_HzdSsq67yfRGrjcI81XygCYaFSdBwVGJ_X-_acqdzdh8DNU66mJpE9pFgnN695tvdrmKJ1d9fwaVgXfNkWXLndDkL1exJMYWhrqeullfhap4QGyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوری
👀
تجمع هواداران پرسپولیس مقابل فدراسیون
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132844" target="_blank">📅 11:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132843">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwQ9AFVUpo0dHuwZo4_3kx5AEUrxojUWzdqld05yylDu-SoxZ9KVVrHokswir-yP6LJD8Te-0v4ui3Gr9YdIH_dwerf0Eh7XAZZHXodELkRN6-iunz_lO0feYiNEJoHkc1eA-Yu-9BJOO83t7xCSHDnXXJ_HYLca5AMOi8OQGyhRGWNYVBmDHJ0LajUt5ApY6k3THNk6XjnN1ZANP-NJkR-BMethTW_W-0VHA-KUAQK_FpywweeIhO50HYQ6PgE6AytMYwtBw7Gly5zVwkq0AxbXOXlXrX0EfuwQQuVVnkRB7yaLuTObNbb4FB--X-JG9_kgsGquIYOAl2IQMtjGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
این یک فاجعه است!
😆
به
بازیکنان جام جهانی ایران
ویزای ورود به
ایالات متحده
اعطا شده. اما اونا شب رو در ایالات متحده نمی‌مونن. اونا در
مکزیک
مستقر میشن و سپس برای هر بازی به اونجا پرواز میکنن. یعنی اونا باید در همان روز بازی از طریق
اداره مهاجرت ایالات متحده
از مرز عبور کنن. این یک فاجعه است/ تریتا پارسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132843" target="_blank">📅 10:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132842">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH7pTosBp447mqIlOCgyNDqpmAy71mKDHqtY519eDIrnQZcShpdWgP1ptctH7_BqEDUPkrB3OOgKxFaL82TaiMiuFD6DpOl2ffuvZqApqffQoim_UIfsLaL0GGKiEU1I3CrycXlfzUOpL0XeJfQQnjjgBqkY-yz5Flp_cwakeSaLN8mqrDfoAwoSHyVATvm-ujDUF59SYLTvhrMwuXWM-qBAulRRh6ehBkXCk82OY6BzQnfHObLHbniBgazU0D3jbiM_mmWPLXPootPzAjYuAlrkjCnhnEFGtRK5hbTzRNHdzu5R39-VPvSDJpyXZTyddkSpGH14xZMwvI95-P30Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132842" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
ادعای الجزیره: ١۵ نفر از تیم ملی ایران ویزا نگرفتند!
🔴
بر اساس ادعای تلویزیون الجزیره، درخواست ویزای ۱۵ نفر از اعضای تیم ملی ایران صادر نشده است. هنوز مشخص نیست که این افراد شامل کدام اعضای تیم ملی هستند اما به هر حال جزو نفرات اصلی درخواست‌کننده ویزا محسوب…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132840" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLcxeiC9medU9ubMhLV-qvqYUDSWDLw5eND7_0XqfP-XqVsK-GIVNHJsxmeHEVQsyokdNzdAE5SrFAy9m8JjUuGXoyV-2JDQkkCxDvBOAEj6HwDr2_cGbGaEt5ARgNAu4LHh-dkh89fkvE3fO8y-kCv6L49DnsbFTvdFVBQyDjNNnbmw32QeUEY5UYYABWhblaoE_GeVOLpSMP9S2r3sMt5hIw3Rmxb44SdL_p8Ak_JKUa6xOoWs2aVBbQgHyU79Enj2RbTnBkcT4ASJnX1gHicRGHv-kJGs83Ws0FqerwdZbx0bbMQcjLeHXHw1Sg8BoQoIpPTLTR2fxz60K6FndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
شهریار مغانلو:
❌
می‌خوایم سه پیروزی بدست بیاریم و با ۹ امتیاز به مرحله بعد بریم
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132839" target="_blank">📅 00:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132838">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAaCbepwIqO7PITFKkBYD1Y-aZdOuNhvpxWz--ClW1RgFQH-HF83eYbkczBBqfDqJ7ExrUv341zXtAoFC9IGgLHKcl1R39ceemrdJclOLMA9Rf5ne8jY4QxE5cFKF-ig5oPyUEtZ-lvr75UEqlVJhCuhICu5os8SgXW4bNHIZnIy6ea6wly_WYJjiijN4Xd8pTDo2IXRh7l1WY6hlF643c6rBkS9YkZwghvT77SJ8rY5VtGXfy85-dY5TLEnQZz6Y7QT3BEqo2JNfP17yhuopl7pA-o47XBeEQ1xSKM1UrZp9KJGYaQ7SUtKR4-T0b4hfUaUpWDgjxBx1KgIbK2ZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرهیختگان: پرسپولیس پیشنهاد داده که میانگین امتیازات سه فصل اخیر رو برای لیگ 2 قهرمانان آسیا در نظر بگیرند و طبق اون نماینده ایران در این تورنمنت رو مشخص کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/132838" target="_blank">📅 00:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132837">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132837" target="_blank">📅 00:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132836">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎙
🤍
مهدی طارمی:
⚪️
اتفاقات تلخی رخ داده که همه دنیا از آن آگاه هست، اما کاری که از دست ما برمیاد اینه که با بازی‌هامون لبخند رو به مردم هدیه بدیم. ورزش از سیاست جداست. ما در ورزش نشون می‌دیم مردمی صلح‌طلب و محترم هستیم و نه اون تصویری که از ما در جهان نشون داده…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132836" target="_blank">📅 00:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132835">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a60445fb.mp4?token=H8A89yT3DBeIkwWBo85sq_kQ9CNoPbuGaSKRlDUjzB2u1EEUcqAt2EE3Am0qSRXm7m1tKJHwt9wx42yH70rbFOptxTsMlz1fxYOjF33pv5doGPji8GNlXj29xQNpVrKe0OZRnPd0iTtwb1qQjwzpzWAx7Z4vTbrU3ClcF74t1wiQUI2Mm2IV-5bG5FBXE3p3aAvbFR-sebhsHUWW_Yql6BxURCVyH3WZLfRuLMm5VCVsxdQ4Or9XvgFsZsZEvzQmqvUm9o_S4_PV8kre_MGqJPzxgzWgBjJ8LOOgDmktD545TmUd8w9zynbxWlAtBTSAYrZYk4rWCUjfz7Oqs0K3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a60445fb.mp4?token=H8A89yT3DBeIkwWBo85sq_kQ9CNoPbuGaSKRlDUjzB2u1EEUcqAt2EE3Am0qSRXm7m1tKJHwt9wx42yH70rbFOptxTsMlz1fxYOjF33pv5doGPji8GNlXj29xQNpVrKe0OZRnPd0iTtwb1qQjwzpzWAx7Z4vTbrU3ClcF74t1wiQUI2Mm2IV-5bG5FBXE3p3aAvbFR-sebhsHUWW_Yql6BxURCVyH3WZLfRuLMm5VCVsxdQ4Or9XvgFsZsZEvzQmqvUm9o_S4_PV8kre_MGqJPzxgzWgBjJ8LOOgDmktD545TmUd8w9zynbxWlAtBTSAYrZYk4rWCUjfz7Oqs0K3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ترامپ: اوضاع با ایران خوب پیش می‌رود
💢
رئیس‌جمهور آمریکابه خبرنگاری که از او درباره آخرین وضعیت مذاکرات با ایران سئوالی پرسیده بود، گفت: به نظرم وضعیت با ایران نسبتا خوب پیش می‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132835" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132833">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👍
🔴
استرس در آنکارا به 100 رسیده .شایعه ویزا نگرفتن 2 3 بازیکن.و خط خوردن آن ها از لیست جام جهانی.بد جور در اردو داغ است  .و چند بازیکن استرس عجیبی  دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132833" target="_blank">📅 23:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: امیرحسین محمودی در حال حاضر هیچ پیشنهاد خارجی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132830" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d48505e0e1.mp4?token=Xe4xttWL-FlAlMYg9PlVOWewWnO1b4sGVqEYw1JxyXyo0NrF9J4aYwGQRtlTXTj2A-Z6TONdZZnt2Q9sKzq84gZQbOvWpYGvtQV0wnhUksCaOYN95gDMNc11Nt_Ai5o4tpRcH0P8pk8DFj6ROQVcBFoUDmFwSAK2-Sx6HGz795GpUDlVZDd-idY2U6kM_t__gDQ4i3k7sgb4oQLhGC-tLS0B0kV_JlcSMyNZHlDdQC34RFb7cYC9y9HIH1MVhH7B4tPSURaXYfTcWGmLVpT5UFiUcDVRBIeEkDDSRd-3MvfCn-7eK1Xz1AAdzvyuGWrMZbi1jpAexp6_gHBzN_FJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d48505e0e1.mp4?token=Xe4xttWL-FlAlMYg9PlVOWewWnO1b4sGVqEYw1JxyXyo0NrF9J4aYwGQRtlTXTj2A-Z6TONdZZnt2Q9sKzq84gZQbOvWpYGvtQV0wnhUksCaOYN95gDMNc11Nt_Ai5o4tpRcH0P8pk8DFj6ROQVcBFoUDmFwSAK2-Sx6HGz795GpUDlVZDd-idY2U6kM_t__gDQ4i3k7sgb4oQLhGC-tLS0B0kV_JlcSMyNZHlDdQC34RFb7cYC9y9HIH1MVhH7B4tPSURaXYfTcWGmLVpT5UFiUcDVRBIeEkDDSRd-3MvfCn-7eK1Xz1AAdzvyuGWrMZbi1jpAexp6_gHBzN_FJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: به هیچ بازیکنی نگفته ایم که برای فصل آینده قراردادش را پایین بیاورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/132829" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f362ea01.mp4?token=vc20332e5ddiJr50o7RtVBZTZxw3Rd4PoekvjxwA614x5atrowshqEnVai4lWiwIjT63vNkjFOhyARYr4XG2jxhXxEj5tf9kRhcPf2XGjliTUwPaZz7N3ZUaN52_44yiNNzn4TC-Ii2nUCDrQd_kaRChj1u1Dts8fGX7-qHnebzzrUZ6K9BG-sHc8j5GeaQITrNybQpu3IZivZDojrz4QXCrxJGLZEZI-MiskW4uhcGC3uwZfJ3EAdWnzdf5o9yhsu1Jz3jAPDzIkhEdq--wElwiOaI26Aik3JJmahEUcfas26CsJ7ZMi_kpXNFbuhTIzo0G9v33FENKOa-MoxqhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f362ea01.mp4?token=vc20332e5ddiJr50o7RtVBZTZxw3Rd4PoekvjxwA614x5atrowshqEnVai4lWiwIjT63vNkjFOhyARYr4XG2jxhXxEj5tf9kRhcPf2XGjliTUwPaZz7N3ZUaN52_44yiNNzn4TC-Ii2nUCDrQd_kaRChj1u1Dts8fGX7-qHnebzzrUZ6K9BG-sHc8j5GeaQITrNybQpu3IZivZDojrz4QXCrxJGLZEZI-MiskW4uhcGC3uwZfJ3EAdWnzdf5o9yhsu1Jz3jAPDzIkhEdq--wElwiOaI26Aik3JJmahEUcfas26CsJ7ZMi_kpXNFbuhTIzo0G9v33FENKOa-MoxqhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: اگر نمایندگان ایران در آسیا معرفی شوند دیگر انگیزه‌ای برای ادامه برگزاری لیگ باقی نمی‌ماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132828" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوووری/ حدادی مدیرعامل باشگاه پرسپولیس: در صورتی که سه امتیاز بازی گل گهر و چادرملو به باشگاه گل گهر داده شود به فیفا شکایت می‌کنیم. چرا باید فدراسیون فوتبال در روز تعطیل رای صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/132827" target="_blank">📅 22:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132819">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfc635883.mp4?token=X6ODib_Ghl4XuFhDWAGQOtmmt2xYl6gtlYfgeK3-t1LhCC4lrmkE0n0cd80ABSRYhTkUuZJh_bdbDX2bpWgp1J6apU6-jANTQL5lSsB3g7dLXIfOJAwnJ8oqIe0S3ynj_5C4qqEa9KJXuTP3P8OJIQu17VYLTTJSVE_MljvOre_gH-1B8ixOjVnxz-R4ipHSDGH83gyb6UDU9VpU-Akoyu65z0Ymy3gmGur-dghpHHrCMscZPEijEUeGOcZf9u9PRP-Fse9k-OlWeciL3z6k8K57bZRbmzvcXf4LgKxwDXJOYVkMv2rkXKA1ICwfRY3xpyjGQC15EqSH_5bChLy9dDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfc635883.mp4?token=X6ODib_Ghl4XuFhDWAGQOtmmt2xYl6gtlYfgeK3-t1LhCC4lrmkE0n0cd80ABSRYhTkUuZJh_bdbDX2bpWgp1J6apU6-jANTQL5lSsB3g7dLXIfOJAwnJ8oqIe0S3ynj_5C4qqEa9KJXuTP3P8OJIQu17VYLTTJSVE_MljvOre_gH-1B8ixOjVnxz-R4ipHSDGH83gyb6UDU9VpU-Akoyu65z0Ymy3gmGur-dghpHHrCMscZPEijEUeGOcZf9u9PRP-Fse9k-OlWeciL3z6k8K57bZRbmzvcXf4LgKxwDXJOYVkMv2rkXKA1ICwfRY3xpyjGQC15EqSH_5bChLy9dDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس:  گزینه اول و آخر ما اوسمار است مگر اینکه ما اعلام کند که قصد حضور در ایران را ندارد که فعلا چنین چیزی به ما اعلام نکرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/132819" target="_blank">📅 22:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132818">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b0f1c642.mp4?token=mf_vhG0cPmh3sBE4VM1KBdBPBZJkgpxl0dAgk4LW_9UYB1exbGTdn_h9nxeDqjDVVbIz3O8IHAIZbdA_k8VimxBu7uu5-PsMhbaK9HBwzr89n95oirVfNxbVHYWErN99Q942v5yKP-kqv29fAG7yElSvU4v5ZQbHyzGhAsOrsoDRHZiBRiK1hqP0Eniwf5QJ7n84g7hKnx5VMRk5Qaq4Tktksbs1wXp_e-0kx-Nncn6bqC16WMS4hVQ2t2Hg64B3MgEsXMBuX-LDWFrV60NJZfhuAjCf5Jh6hmap6aVUvovVZ3j6C00vrx9L4kM5SWjRIzhgtZ1pBNzflql3Y_elnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b0f1c642.mp4?token=mf_vhG0cPmh3sBE4VM1KBdBPBZJkgpxl0dAgk4LW_9UYB1exbGTdn_h9nxeDqjDVVbIz3O8IHAIZbdA_k8VimxBu7uu5-PsMhbaK9HBwzr89n95oirVfNxbVHYWErN99Q942v5yKP-kqv29fAG7yElSvU4v5ZQbHyzGhAsOrsoDRHZiBRiK1hqP0Eniwf5QJ7n84g7hKnx5VMRk5Qaq4Tktksbs1wXp_e-0kx-Nncn6bqC16WMS4hVQ2t2Hg64B3MgEsXMBuX-LDWFrV60NJZfhuAjCf5Jh6hmap6aVUvovVZ3j6C00vrx9L4kM5SWjRIzhgtZ1pBNzflql3Y_elnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مدیرعامل پرسپولیس خبر داد: با هیچ سرمربی داخلی و خارجی مذاکره‌ نداشته ایم/ فقط با اوسمار صحبت کرده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132818" target="_blank">📅 22:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132817">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e073252128.mp4?token=WvgVwISaRl2PRQUOFQCktXBWtQ4XKuyo0C7siL-zHr1TBcmoKkkP6Qf3e5di4iilhFMHaW97CnKkfyHwrVCvioYsywuylVBY1XpnYItY9jqjqoyfjDyXnwYOEUAnpBpkdMVQ2ARPue5-Dl8Grq5g-lGLEwiV1p7n_ePp9tFHJ34BYNIGJj69rDqpabdM1ZE5DddPcvLDncBq6rQz78L_0G94C4SabIvKx00sonG_rqVoUlZrBEu6faXKShE2ljsq-pvKlES3AMvJ-50tGYbSo94qmli1_S3VqhhF41kYTiz1MMl7N1lVBvCzBSR7h4Pqloee38_HbW6-5dZ9P_Vd-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e073252128.mp4?token=WvgVwISaRl2PRQUOFQCktXBWtQ4XKuyo0C7siL-zHr1TBcmoKkkP6Qf3e5di4iilhFMHaW97CnKkfyHwrVCvioYsywuylVBY1XpnYItY9jqjqoyfjDyXnwYOEUAnpBpkdMVQ2ARPue5-Dl8Grq5g-lGLEwiV1p7n_ePp9tFHJ34BYNIGJj69rDqpabdM1ZE5DddPcvLDncBq6rQz78L_0G94C4SabIvKx00sonG_rqVoUlZrBEu6faXKShE2ljsq-pvKlES3AMvJ-50tGYbSo94qmli1_S3VqhhF41kYTiz1MMl7N1lVBvCzBSR7h4Pqloee38_HbW6-5dZ9P_Vd-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: اگر عدالت رعایت نشود حتما پلن‌های دیگرمان را اجرایی خواهیم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132817" target="_blank">📅 22:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: برخی‌ها می آیند روی آنتن زنده و می گویند قطعا پرسپولیس نمی تواند در آسیا شرکت کند، بهتر است دوستان در حیطه وظایف خودشان صحبت کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132816" target="_blank">📅 22:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b4c5477e.mp4?token=LtURJXvMg89wpwQ8wBnziD0XN39BlVQKXLAgCdcL9CegE6Rqh5mfkpGuPwZMmjAgUJUomtqfMImCpHhhvmuYDPZitGix6_7wPLlqLflCYpRhCt5sI8qkGgYFWoMZHsIkDytH791ir7LkTb_Z_pb2m8ey3DU8NfWPNzoNYEb5daynwYc94fjoGriNtgryJHQWJqmgKnEDqGmG98gSCOG_EOFS5OEqYu6phT3mxz8Kv4_mIt9KseCgw-N_hWiPphvWOEdbgTajG3pSPqSYNI0cfBGqlC1KVjpkKDrelSlvFmmfhe_wWgiLfL2lMXuqIZd2p0XoXvAiYM0-ceauinS3x3JE5HLea73jO1XQJIskgQfPDcBLLZ4VHO7p8OgXFXsSUQ9l5R8Cy9xp4otTLqBvBirGuOM7mif09g4oJwX2TA77yWIE3Jbb5xllZCgXgj3Kb1-SovRsjzJbxA6IJkCniSPDDT5JywooMvCX-e4adDTmx-KmUrLR6VxxljersXFMCYGFebgJ_uXiemr2l-lt0NQ9mhpSP45ZkhhENjwtEhe_ZzLcaO3e8og7GNBdc5I7m8NyoSWyHQz3HCM5rRKyzU_Uc5hRRA_-De_u0e-6iQ1qn2X9hZTfcePzXGvjD2ceJbcVesDj-hXiAMEuhj6kit03BhM7_GdWz_uPZwSWDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b4c5477e.mp4?token=LtURJXvMg89wpwQ8wBnziD0XN39BlVQKXLAgCdcL9CegE6Rqh5mfkpGuPwZMmjAgUJUomtqfMImCpHhhvmuYDPZitGix6_7wPLlqLflCYpRhCt5sI8qkGgYFWoMZHsIkDytH791ir7LkTb_Z_pb2m8ey3DU8NfWPNzoNYEb5daynwYc94fjoGriNtgryJHQWJqmgKnEDqGmG98gSCOG_EOFS5OEqYu6phT3mxz8Kv4_mIt9KseCgw-N_hWiPphvWOEdbgTajG3pSPqSYNI0cfBGqlC1KVjpkKDrelSlvFmmfhe_wWgiLfL2lMXuqIZd2p0XoXvAiYM0-ceauinS3x3JE5HLea73jO1XQJIskgQfPDcBLLZ4VHO7p8OgXFXsSUQ9l5R8Cy9xp4otTLqBvBirGuOM7mif09g4oJwX2TA77yWIE3Jbb5xllZCgXgj3Kb1-SovRsjzJbxA6IJkCniSPDDT5JywooMvCX-e4adDTmx-KmUrLR6VxxljersXFMCYGFebgJ_uXiemr2l-lt0NQ9mhpSP45ZkhhENjwtEhe_ZzLcaO3e8og7GNBdc5I7m8NyoSWyHQz3HCM5rRKyzU_Uc5hRRA_-De_u0e-6iQ1qn2X9hZTfcePzXGvjD2ceJbcVesDj-hXiAMEuhj6kit03BhM7_GdWz_uPZwSWDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: قطعا برای گرفتن حق پرسپولیس کوتاه نمی آییم
◻️
ناراحتی دوستان از رفتنم تا دفتر ریاست جمهوری؟ حتی اگر لازم باشد از مراجع بین المللی هم پیگر حق پرسپولیس هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/132815" target="_blank">📅 22:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7fcad3a9.mp4?token=ZcKPuDe6V_3F9pxnmbDI0Nh1si5fOhb672va8QYoYGSN8pWvV-JHdpOWKFVJDeSIKOYlxeO2Ae7cNW0n8_PldgFcpSF5YjOrkjFzNb2vGceZHGaSINvkWIaAn7h0JBBr-ZXuUzm8EclqmHbXCL4RXUBgvmbtI61GV1KG_ujhXAqMONgYGCvViWan0q9rh3In_6OjR5PyLBM_5OhsVcDNq9cnEeAhHpAdVkgs82-pNLHg693cwjYoyWMzm2_XX3QHx4JzxuHbsLqPtUwkfN3yEZCIrwxqulHbvRUg9-htH4HJgJXBpEbPMoFsKaSweP4DQhpxxntNWRni8gWL3Q0VYzopJcnMBXH0hy9cxfC4wOyS7EtUxAkWln-Z0xben5cVdYuQmVUDM2aKKrXXoN0hVsYFJSL3ZZkbLFtnLE3jdplFrSkVSvBGzk-JzWl5LEqWFF2TO-OO46QHWCmCqqIp9BgUNqW_Akem1RLj43dJbszf1znJ6rxX6zpsPp3tl4Nto02BX6czkp3LIpfE_AClHgoT4GKM9nYT9lTBtPoZkkjYw6emrjtsjfvm2IdgoQnKW0ufxUUVube9bcGlonW3v9MOFsn1FbtdcjyseommHzF1_e1sAMagOpVAEXffVIqXJ29N2aLMKcIMWWU1tGvF25zrOxGuyRK5TBeDG4HXiGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7fcad3a9.mp4?token=ZcKPuDe6V_3F9pxnmbDI0Nh1si5fOhb672va8QYoYGSN8pWvV-JHdpOWKFVJDeSIKOYlxeO2Ae7cNW0n8_PldgFcpSF5YjOrkjFzNb2vGceZHGaSINvkWIaAn7h0JBBr-ZXuUzm8EclqmHbXCL4RXUBgvmbtI61GV1KG_ujhXAqMONgYGCvViWan0q9rh3In_6OjR5PyLBM_5OhsVcDNq9cnEeAhHpAdVkgs82-pNLHg693cwjYoyWMzm2_XX3QHx4JzxuHbsLqPtUwkfN3yEZCIrwxqulHbvRUg9-htH4HJgJXBpEbPMoFsKaSweP4DQhpxxntNWRni8gWL3Q0VYzopJcnMBXH0hy9cxfC4wOyS7EtUxAkWln-Z0xben5cVdYuQmVUDM2aKKrXXoN0hVsYFJSL3ZZkbLFtnLE3jdplFrSkVSvBGzk-JzWl5LEqWFF2TO-OO46QHWCmCqqIp9BgUNqW_Akem1RLj43dJbszf1znJ6rxX6zpsPp3tl4Nto02BX6czkp3LIpfE_AClHgoT4GKM9nYT9lTBtPoZkkjYw6emrjtsjfvm2IdgoQnKW0ufxUUVube9bcGlonW3v9MOFsn1FbtdcjyseommHzF1_e1sAMagOpVAEXffVIqXJ29N2aLMKcIMWWU1tGvF25zrOxGuyRK5TBeDG4HXiGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: اینکه هواداران پرسپولیس را مقابل فدراسیون فوتبال قرار دهیم کار درستی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132814" target="_blank">📅 22:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132813">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ccb46629.mp4?token=ppxxlNnYjVWC0WX0s2ccc5kNwzwCw-FeFjGpkY9XZmI0UaoepVRVqdPfe7uD8zZymmpzdN3NsanzX15WEgxMYLINyr5fVJOE3zYe5rY1RGMRz_m8F8eQqZhF8Mlf43teH5TQgV4QkWcnn52pReCT_pWmzNBZHNLx_09NyaCtAdTkQbYw2BaZXxrdAYaKLut9xMd6XJTwdBC0inoOXspXItZx8Tj8NxV8Sy3k4kT8lDMWeoNrGlbGQ7oLA3n3HwXrPcBG4RDI7GprZ3aeNsgpxVpL5SPWpZ0mzvcjPz6L6EmojDKnWyyRzFEyxt0kNxlLmovyc7EfKqb6Gm0eWFhmhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ccb46629.mp4?token=ppxxlNnYjVWC0WX0s2ccc5kNwzwCw-FeFjGpkY9XZmI0UaoepVRVqdPfe7uD8zZymmpzdN3NsanzX15WEgxMYLINyr5fVJOE3zYe5rY1RGMRz_m8F8eQqZhF8Mlf43teH5TQgV4QkWcnn52pReCT_pWmzNBZHNLx_09NyaCtAdTkQbYw2BaZXxrdAYaKLut9xMd6XJTwdBC0inoOXspXItZx8Tj8NxV8Sy3k4kT8lDMWeoNrGlbGQ7oLA3n3HwXrPcBG4RDI7GprZ3aeNsgpxVpL5SPWpZ0mzvcjPz6L6EmojDKnWyyRzFEyxt0kNxlLmovyc7EfKqb6Gm0eWFhmhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: واقعا چه اصراری است که رای کمیته انضباطی شکایت یک تیم از تیم دیگر در روز  تعطیل اعلام شود؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132813" target="_blank">📅 22:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132812">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d515e687b.mp4?token=FSOf1wRdrDHugSFoz7HFRNyAxoLovO_6m7leK8eESedozlkFUzI1ORQHIBRGqmA3m4R6DLE-iuNt4MF8qbcN0w329diiHm7FnJj0RzHPGNo3JLUrqTdoec_oT4P5RepQTLB12fq0GgzP-wm8VkSwA2G6GFcWXeI9841Vibxx10pE61vK5zyD1yyExUjxu2sDMYypWeydUQS4ApEyYCYgEI60xGnrlUt6BPiHdFyQiFBgUnlAPB1ykoMeTfXJFiQXa3etHhWr8Tgio-ygWo8ceSEg1w_qs32b4LAkgd-LtEvjZ-ivBRdcBXFizjJohyygW6SJGyvSJpu5kKGVHlAL3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d515e687b.mp4?token=FSOf1wRdrDHugSFoz7HFRNyAxoLovO_6m7leK8eESedozlkFUzI1ORQHIBRGqmA3m4R6DLE-iuNt4MF8qbcN0w329diiHm7FnJj0RzHPGNo3JLUrqTdoec_oT4P5RepQTLB12fq0GgzP-wm8VkSwA2G6GFcWXeI9841Vibxx10pE61vK5zyD1yyExUjxu2sDMYypWeydUQS4ApEyYCYgEI60xGnrlUt6BPiHdFyQiFBgUnlAPB1ykoMeTfXJFiQXa3etHhWr8Tgio-ygWo8ceSEg1w_qs32b4LAkgd-LtEvjZ-ivBRdcBXFizjJohyygW6SJGyvSJpu5kKGVHlAL3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: کدام جریان به دنبال ضرر پرسپولیس است؟ همان جریانی که دنبال این است که پرسپولیس به آسیا نرود، همان جریانی که مانع برگزای لیگ برتر شد
.
نباید از این موضوع به سادگی گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/132812" target="_blank">📅 22:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132811">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس:
اینکه چه جریانی باعث شد که بازی‌های لیگ برتر برگزار نشود واقعا جای سوال است/ در سال‌های گذشته هم که پرسپولیس قهرمان لیگ برتر می شد در هفته‌های پایانی امتیاز جمع می کرد و قهرمان لیگ می شد/ این احتمال وجود داشت که باشگاه پرسپولیس به صدر جدول برگردد، واقعا این جوای سوال است که چه جریانی مانع برگزاری مسابقات لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132811" target="_blank">📅 22:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132808">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
لیست مازاد اوسمار از نگاه رسانه های تلگرامی:
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
میلاد سرلک
🔺
محمد خدابنده لو
🔺
سروش رفیعی
🔺
دنیل گرا
🔺
مرتضی پورعلی گنجی
🔺
سهیل صحرایی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132808" target="_blank">📅 21:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132807">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0Lx6vAPpdFe0xdgYYMmttXouWN3pjHHacx2-hioR5hammmbZeXKkzpVOaGsxy-bQ0-agpRj3DCLvfO6ERJ60bdb0kkG1tcyxxZj0GDtAawJLkEJCTYRn1ADOXojkX6MUtkt2UNXUu9jTHe615E1pc2AizgEo-BjKq5yPWsIRC3QrkyKPaVZViCLG3kxyHwOMrxr_LYpG-IloOWpbaX3meg0S0Mc8JJJhNblTy746KdOR0gxY-b_0Er42g761O8Qn1LR8kaN7FJ8GfTlSH0FImzODR1Ywf63ESBthpPqfMS1C8A8NMcBhAQDdsm4ZBSI_dWvG0dLIujKO07WKocqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
دیدار جذاب و حساس نیمه‌نهایی رولان‌گاروس بین
ماتئو آرنالدی
و
فلاویو کوبولی
رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132807" target="_blank">📅 20:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132806">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
ادعای علیرضا محمد، دستیار تارتار در گل‌گهر: باشگاه پرسپولیس با تارتار مذاکره کرده و اگر اوسمار برنگردد، تارتار سرمربی میشه! او می‌تواند پرسپولیس رو قهرمان کند! باید چه کاری دیگر کند تا سرمربی شود؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132806" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132805">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
خبرنگاران کاخ سفید میگویند که ترامپ پستش را بد نوشته و در واقع اعلام پایان محاصره نکرده و منظورش این بود محاصره رفع میشود اگر رژیم ایران با این شرایط موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132805" target="_blank">📅 19:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132804">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
یحیی گل‌محمدی به تیم دهوک کردستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132804" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132803">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
شانس دوباره محمودی و حبیبی‌نژاد در تیم ملی؟
◻️
امیرحسین محمودی و هادی حبیبی‌نژاد هنوز شانس حضور در فهرست نهایی تیم ملی را دارند و به‌دلیل احتمال مشکل ویزا یا مصدومیت برخی بازیکنان در اردو نگه داشته شده‌اند. در مقابل، امید نورافکن ظاهراً اردو را ترک کرده است/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132803" target="_blank">📅 19:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132802">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
باشگاه پرسپولیس:
‼️
ما با آقای تارتار مذاکره نکردیم. این حرف‌ها برای بازارگرمی است. پرسپولیس تاکنون هیچ‌گونه مذاکره‌ای با تارتار یا هیچکس دیگه‌ای نداشته و این ادعاها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132802" target="_blank">📅 19:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132801">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
علیرضا
محمد:مذاکره تارتار با پرسپولیس را در رسانه‌ها شنیدم / به خدا نمی‌دانم به او پیشنهاد دادند یا نه
💢
من در آن مصاحبه ویدیویی هم گفتم که در رسانه‌ها این مطلب را شنیدم و منظورم این بود خیلی از رسانه‌ها گفته بودند که مهدی تارتار مدنظر پرسپولیس است. خدا شاهد است صادقانه به هواداران عزیز پرسپولیس می‌گویم من اطلاع ندارم که باشگاه پرسپولیس با مهدی تارتار مذاکره کرده یا پیشنهادی به او داده است یا ممکن است بدهد.
💢
من فقط نظرم را گفتم و هنوز هم می‌گویم اگر قرار است آقای اوسمار نیاید مهدی تارتار می‌تواند مربی خوبی برای پرسپولیس باشد. ولی اینکه با او صحبتی شده یا نشده به خدا من اطلاعی ندارم. امیدوارم پرسپولیس موفق باشد و وضعیت کادرفنی زودتر مشخص شود و نتایج خوبی بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132801" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132799">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI2LTmXcphPKwjjgQYYwDzpcv9UtujNz-i7FNhLSV2VNANkAJobkQPy9MzrdXHr_kc8743euXhY7HS-oLTwzb_QBMktE1KU1cK1-8s246Zof78dp7EuZrJTLBqzwryDicILWWgenpuzoo0rQA6QPYi1HxKJZb5bjFCfOVXFMjc3HWctvR1vWsCK8AS0gzEm3PdSEhRskqaQS95exjJ1_VxLrRrUb9_HN8ZZiuIZ39z3Hs4sexi_yaejTSRIi9kIMNT2PZcnodQ4zAN0S_TlXAZSs7CP5Ll03s0FGzBg-CngZ5qGfMG3-WYt-S7mlBASJKNblamkBiRaYM48-yvW4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
دیدار جذاب و حساس نیمه‌نهایی رولان‌گاروس بین
منشیک
و
زورف
رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132799" target="_blank">📅 17:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132798">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNP845R0ZCuMSreG2fcPDvwYenzS9ZdEp9OFzu7z_l9JA7gcdfUFvPBr9hxL2rVF_36IDryxCDA-ElWIUbmJD59SdplJlvgtUXgaK1xOZidV7qocGcUfCJvzrRuw7jkoEdMo97hhAqrA-AeaS_Ut0LT77oBN25dL_wIjMaPIgZ8jxVDfhrQRjVQG86jDRsyE4VQqzTSrJF-RP-8MqUxk33-AG-rkkBvDQnOH1igwYxHJGfrYRXPC6MOIczN9vHpp7zoK5j9eWpGrEeRhvrMm21_qCjxdbS1dPs3C7DqxO0mj_Ef1a7EeOVkXbMojcBZo7sSlvupr5R_GaojxQ0T_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عکس تیمی بازیکنای نروژ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132798" target="_blank">📅 16:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132797">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132797" target="_blank">📅 16:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132796">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEkCss9o58e5dip6scvbHkG8CQo_IzJo5OzB7cdKabAFI0onEcBb6jric41B-g8wyUo39kKMmO5SvI47ztfzlvVHCOAU3B9UVVg6CuCYv5ARGLRANETHWEV5P161prerJON33bxh8lrz_ZpHHy9uUS-7rHNtxyaoHMzfPVvCvqAVhMfPKB2W2ktoC5NutVtfIOkfjC0P7Wb2E1sQLhaYdVMrSix2y9Dkjm28jIAF56_tOSHYPXc8k5Vh5c4kQFLWr4qneupAQI9x8I-JrwlujqbAmG4xod9twrfKpGyJslgTaAaBcCC62GFB4KzpemQaYz4p2JrlxyQjSCVZcek_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔼
صعود یک پله‌ای در رنکینگ فیفا
؛
🇮🇷
ایران دوباره در جمع ۲۰ تیم برتر جهان
🔴
در فاصله ۶ روز تا شروع جام جهانی، رنکینگ جدید فیفا اعلام شد که براساس آن تیم ملی که در آنتالیا گامبیا و مالی را شکست داد، با یک پله صعود دوباره در رتبه ۲۰ جهان قرار گیرد.
📊
در این رنکینگ، آرژانتین تیم اول است و سوئیس و دانمارک تیم‌های قبل و بعد از ایران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132796" target="_blank">📅 16:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132795">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🇮🇷
🇺🇸
🇵🇰
العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132795" target="_blank">📅 16:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132794">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCl-_HwibYD6GwX-Sz8SfheFB8Q_MAHXIZ3RVjTJ7y0pgT53JTGzSb1UlnTnllU6V5g0jADOLvo6dSc0mbQ1LVaJoKhc0KPffZ4PD3BLZPq_HxwAIhqukRWlbS9CpwZBGmY4K8uO5jjBHJpCWpOc-OchqcsZkC-KESUhHgS8_04VOMVEjGziImWFyTgr5COsUzbTulIPXbGSZYCx1_yTAO0edKaDitUjlV81o1FjlfGJXezcFAr7WlUfwWk9O2PHcHTFGewOjvXrlEEY-ZDHnsA2HSx8PB_nhxU-KUl48rmo107Uytq0nBltzdBnd0okYTqowEGy1CE20I73x1C8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132794" target="_blank">📅 15:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132793">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCguYZn2GeNn1_JAPB5SZ_lvcDpHyrT4s4EnGqLIagiFyN-I09ahEA_nLtKtAudH2TsiK_FpGKtdhDN1HuF5nJdCGvZLryDXpjxs7DL8fY8XYba6siyDdDWicZtZaj7HOoaqW_m32J-1Hcswcjr3lYM-LYSAgtVNojbGFDDyAv4D-kD0WQJ36hqXJaFli8YbuxqjZ6aj4jIsoaBCW0iOcjMU6O2bPLZ-UBWGoVjYIatU2bxmNPItnRthlpH9-CjJ0hs63SreeGn7N_wsiwyNi2TOfIF0ZNQha6GVz2f2uqYvi9iHhUkgJEJahCXNSnqg893wO0hTLNnu4_14O3Vbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سروش رفیعی به طور رسمی از پرسپولیس جدا شد. سایت ترانسفرمارکت هم این بازیکن رو بدون باشگاه اعلام کرده.
🔴
رفیعی در فصل اخیر طی ۲۳ مسابقه به عنوان هافبک بازیساز، آمار صفر پاس گل رو ثبت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132793" target="_blank">📅 15:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132792">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7zbz-DbqpNPEMRoLYYWv1z60RnUKbKC4PGBbbOAh6ONjaLyX0XYfdCspzKBWRtiVkCgOLGCUj03UUw9deN2oxZDpGs54n5uW6uzY8nmbaH9NDoQiYYPYjVv5Zl-4y5YnKOznyxXPbk4pgwPJV0LLOUMAidOEeOYZPSMQCi6_AYGmtnwrvot1BFlR4v5mqJuJ75WQYL2APLtI1JDuCHd-bHxceRbSWmgoVjDf_4RqVKrMnY5mc4y-ihhMotY1jbtYKnmgnpFSB1hO-malx3JX1taC-TFfdO8B5JSeYcbXwhiL0phlomskFNcP_2EL8K2UUxhDsDCUvCECaYkMPFoCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
با حضور در لیست تیم ملی، میلاد محمدی سومین تجربه حضور در جام جهانی را خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132792" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132791">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
🎙
مهدی تاج:
⏺
فقط با فیفا در ارتباطیم و هیچ تماسی با ایالات متحده نداریم. کشور میزبان حق اختلال در تیم را ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132791" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132790">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
شبکه العربیه از منابع مطلع:
🔴
جمهوری اسلامی میخواد اورانیوم غنی‌شده‌ش رو به چین بفرسته، به شرطی که چین تضمین کنه این مواد رو به آمریکا تحویل نمیده.
🔴
به گفته این منابع، خیلی از نکات مربوط به برنامه هسته‌ای جمهوری اسلامی تو مذاکرات الان حل و فصل شده.
🔴
بر…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132790" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132789">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
با اعلام ایجنت سروش رفیعی، این بازیکن پس از سه سال از پر‌سپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/132789" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132788">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت  بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/132788" target="_blank">📅 13:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
اول یا اخر هرکسی بیاد و بخاد بره؛امثال سروش و هرکسی که حاشیه سازه و از نظر فنی به تیم کمک نمیکنه باید بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/132784" target="_blank">📅 09:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
در سکوت و سکرت....  فعلا،مذاکرات داره خوب پیش میره///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/132783" target="_blank">📅 09:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132782">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
امیرحسین محمودی علی رغم خط خوردن در اردوی تیم ملی حضور داره و قراره همراه تیم ملی راهی مکزیک بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/132782" target="_blank">📅 09:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132780">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCWBqUvTQ7wkHSrxVscme6vc7d3b_a5H8Dw7T3uSL6DH8GVcZKCBBm3QXc0UzrV6Qr-CmEXcBarlhuqRq7wjXFdbE6Xzj2xVci9YdBKc_J0Gu5QA4RStI_gJ22UhMGg63djweRRIh2CamskEsDD8paDbjFsSryRTMpr5EzRbj_39qxj35ML90Nj64UduTqn5nFUQkFyw0Cqv1xdcRmT-WT6530YdGC8O0r5cEeTHLnQw4F3anxv8jHDWKT6fZrRpMdJeZ6pKaJjsKcl4LTIOmzprlxvosHxu9mUc0t1jigr-up1NjyHDpSBrUqoRnnRzKIWdl6cJ68hWwh594VOtvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/132780" target="_blank">📅 01:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132779">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
امروز عراق با اسپانیا بازی می‌کنه و جمهوری اسلامی با مالی!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/132779" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132778">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
اوسمار ویرا :
◀️
با 40 روز تمرین پرسپولیس را مدعی قهرمانی می‌کنم.
✅
اوسمار ویرا سرمربی برزیلی پرسپولیس همچنان تاکید دارد که در صورت برقراری صلح، به ایران باز می‌گردد و در جمع سرخپوشان باقی خواهد ماند.
✅
ویرا از بابت شکل تمرینات و نحوه آماده سازی بازیکنان…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/132778" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132777">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f9110aac.mp4?token=bc8glIggcduFS1hW6I4hmAmuG6PruWGMgQJu9nto5E8fIBQVa_tPZOsd91wKhApViWG3itnQH3nlkDdYjCg-C39vPLGmHNjpwUCws7UrDnQr4Nk7Le18lmbX8BGAVGo9ezpujZhkafQRdBkWPFafaUtQr2QY31eFq0eMsw9WBZI6clH-yYKsMlJywuNuM2e-3BUYunDCKPHdhxGtuDJpJXS8CJ7NZ49pm9qOYSOZZrN3HTr8U9gDZPGrCV19Sq02vusFbm1rKPHdX08Z2vHhhiEpoQ3GmcF7Q5vygzzO9mBN8PcSUnG9Jff3Kxv7qkpQRmwMGuH_LEJnk07lv_dRnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f9110aac.mp4?token=bc8glIggcduFS1hW6I4hmAmuG6PruWGMgQJu9nto5E8fIBQVa_tPZOsd91wKhApViWG3itnQH3nlkDdYjCg-C39vPLGmHNjpwUCws7UrDnQr4Nk7Le18lmbX8BGAVGo9ezpujZhkafQRdBkWPFafaUtQr2QY31eFq0eMsw9WBZI6clH-yYKsMlJywuNuM2e-3BUYunDCKPHdhxGtuDJpJXS8CJ7NZ49pm9qOYSOZZrN3HTr8U9gDZPGrCV19Sq02vusFbm1rKPHdX08Z2vHhhiEpoQ3GmcF7Q5vygzzO9mBN8PcSUnG9Jff3Kxv7qkpQRmwMGuH_LEJnk07lv_dRnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ: مجتبی خامنه‌ای کاملا تو کارش حرفه‌ایه. البته یه سریا در موردش بد میگن که دروغه، مثل من که یه سریا به دروغ در موردم بد میگن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/132777" target="_blank">📅 00:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132774">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
فووووووررررری
🔴
حمید ابراهیمی : با توجه به نیاز حداقل 2 هزار میلیاردی دو باشگاه چادرملو و گل گهر سیرجان برای حضور در آسیا وزارت صنعت با این موضوع مخالفت کرده و به زودی انصراف آنها از این موضوع رسما اعلام می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/132774" target="_blank">📅 23:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132773">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2Rt16BP8reIhZb2u-zHP6whMrKIpsGub9g5JOb_T5kgw4raA3IaFW7VRsEinXVzNyDx5LahkwovmoAg19_nLLM8-P_x74bAtyh9SZCxaWDB6d9cp8hAOA0r5wiTeUGKP4MT96li0uQntnivDIsWsnPoGwpENDhduPMgIxQUYMoO7DpzicBkZNNoREFr3DjiN3cOMAauz6EDGxEg61K3XnztgzwbjlYkZOuWNjrdQeMgNCJz-oO0HewkpujIFRy4qsLf0ERuVmHB_tRLuEsgahGDAvKYr5vMFFjipTFEQdMG1ATX-PM68VvA8Cf4oly9AbgNJzkB7zB-YFEq24OH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ایران با دو برد مسافر جام جهانی شد | سعید عزت‌اللهی دقیقه ١٢ و رامین رضاییان دقیقه ۵۵ گل های ایران را به ثمر رساندند
ایران ۲
مالی ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/132773" target="_blank">📅 23:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132772">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
فووووووررررری
🔴
حمید ابراهیمی : با توجه به نیاز حداقل 2 هزار میلیاردی دو باشگاه چادرملو و گل گهر سیرجان برای حضور در آسیا وزارت صنعت با این موضوع مخالفت کرده و به زودی انصراف آنها از این موضوع رسما اعلام می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/132772" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132770">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRzXRYRsdlPfuISCLfDWaOhIc74RDA_88_V6hq4pzfJCTl3rl11zgGnmcCFnXHVFxokY9feL1bfhlSJvxVW7A6tP7GdluFhbEDYuJEz0anVaeKn0QDiwl6QV2CnFk-J0HTogMAUbT5X0gaWNrZN8ohM37gg1yjA0ZqXej8EhJQ0I_P--7hTkZX0ycIkfaHafGTD_YRnRaZyY3I5MRmhCnN00pa-Oz0gT4uPzBXmF2JjOkowOjsaSzCGk3EytgZPYO3kg9GwMphM3fIImBkbbiAx1QiL5rjiueFugIH9m7DVsaj-M1An9H_YMIKWFoYoaIs0CoZqgG8sivWboWpCZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گفته میشود که قرارداد امید عالیشاه با پرسپولیس به زودی تمدید می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/132770" target="_blank">📅 21:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRmgiB1fjS2NrfzERKpGZCbEHvOb2Nhd1K1Bkaoz-GlByPrRmQN1E2OTf1wWs2Ni2O_uX28zS9cQaKhUtECyTH1QKZ4Ca5Mo_JrGtjWU1XKkF1g8axOl34oZyhsRPpuT8QTK9-Uw-tvjXZFB1wwMABi8J9cr-8Tkh_L212w9o3NOaq-sABVHrchOHDb3kmjJ3FPDNhgtx133SkTgxLkdNmmR04u6mQDPzJRUWK7wL-1V2Vv7JEQnTRxFuxJ-7Za-oqKdCrLI9_MKyI_4_WyxZ-nR4d2P8k2KNJIL0uazknbxPtLy8AHJT1viPVBmCeTDIGf2vFBVZS5AsNUgSpctkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:
🔴
استقلال درحال مذاکره با اسکوچیچ سرمربی سابق تراکتور است و جزو گزینه‌های خارجی این باشگاه است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/132769" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔽
تیم ملی امشب از ساعت ۲۰:۳۰ به مصاف «مالی» می‌رود. این بازی پشت درهای بسته برگزار می‌شود تا بلژیک و مصر نتوانند به اسرار تاکتیکی قلعه‌نویی پی ببرند
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/132768" target="_blank">📅 21:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
فوری کمیته انضباطی آندرس بازیکن چادرملو را غیرمجاز اعلام کرد و نتیجه بازی این تیم با گل‌گهر، 3 بر 0 به سود گل‌گهر سیرجان اعلام شد.
🔺
گل‌گهر با رای انضباطی، به رده چهارم لیگ برتر رسید و اختلاف امتیاز آن‌ها با پرسپولیس به 5 امتیاز افزایش یافت
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/132767" target="_blank">📅 21:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XT94G-2EEJDstB4XTA8wVrt_dFtdIAB2rVqWOIfvpUg1WQhS-MLFqSgpre92U1OVNtvQ1-E_cHomalCA7B7ZM5BBAESwyV5E17rz3G60xckpILrd-5r6cnsaTFGOzB8MNgAFjAO-ZKQky3zoeKVAVnDxaFuXRZkYztQvHNAnlGA7pYilwXzo4ZXzBz6aEsRKepIsLSfY4hlw3FaFFqZdZeQdwCa8kgj8p8boFdjQJO_3Y3EJSpg0ka3ZHY08SgoK6ij4625LPHGKShpzIyOnegj5TN-xurM3ohebCQHdx0TpGukCj2C5BiLdAEATUCCD4jW1AkBVDxA2EhFqnKkIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امیرحسین محمودی علی رغم خط خوردن در اردوی تیم ملی حضور داره و قراره همراه تیم ملی راهی مکزیک بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132766" target="_blank">📅 21:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=G_DSJCkQZHk_ZANKxwF6S4YX13-H3g7mEZOJTOV7S8PMpws-8hplp7oZxDRQ1bbO8VlfXB2EMnvxTYZ7fosD8dwM_-6G3QXUlqSWthxxhrM_BoplOqA_gRgPsdVAIOo8CjyTGfGyCSOEHLl6RQPJ3c9bBZ8o0IunNDg9NMFlmqZByLOQQ-YCfL9RJCJHBbF-4jhDYRc2p5am_yjER1XYMBUzk8ilxhPKXG0wy28XfZbtp_FehECdascqSAsIz87N5o0kpROSdKefHjmr-4d-4pErQ2ZF3phcLcWh0Jsyv19nz4sXReSZ_Pv692WSiR8abqNdx0RFCFBzxnT7m5zXVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=G_DSJCkQZHk_ZANKxwF6S4YX13-H3g7mEZOJTOV7S8PMpws-8hplp7oZxDRQ1bbO8VlfXB2EMnvxTYZ7fosD8dwM_-6G3QXUlqSWthxxhrM_BoplOqA_gRgPsdVAIOo8CjyTGfGyCSOEHLl6RQPJ3c9bBZ8o0IunNDg9NMFlmqZByLOQQ-YCfL9RJCJHBbF-4jhDYRc2p5am_yjER1XYMBUzk8ilxhPKXG0wy28XfZbtp_FehECdascqSAsIz87N5o0kpROSdKefHjmr-4d-4pErQ2ZF3phcLcWh0Jsyv19nz4sXReSZ_Pv692WSiR8abqNdx0RFCFBzxnT7m5zXVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎ اگه این روزا سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/132765" target="_blank">📅 20:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132763">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSvtsyR8C7rGLaPm3gleVZHjtjwC4-OXu5ch58F0WGiK94ikcu9_B-Dwe_I81ZbDt-cgD4KrFlsEqr1lxs2cn49GJhCOJdymS0tPqyn4-TNuP1adSK69IPtG0VIDYpSwCEmasHiVJnVbaYyi7Yo46P8l6NsjvmD1y0H2irC3WkfYPEni3nPoMa_-IiCkWCa2C7nRf9CftG5u6KdlvDsPO4qEM58J3rv59pXyJRP68B09KUkE8_6B7JNl3NrTcBTg23GsHgXyiWRZoN6v9T7dLnlKJeRwY8ZpGP0lqGmKQYhrp5u_Vc1dA_reZgZWgX3Y91qh86q-VlFqRO4VHO9tyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#رسمی
| با اعلام رسمی باشگاه بنفیکا، رئال مادرید بند فسخ ۱۵ میلیون یورویی ژوزه مورینیو را فعال کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/132763" target="_blank">📅 19:36 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
