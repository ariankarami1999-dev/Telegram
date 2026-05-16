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
<img src="https://cdn4.telesco.pe/file/XjTzlKTIm8fmowK4EN8YY9NsMila3UbIvmwxJ-p3Su8ctj5h9wVyjxJh-SxDopMjjpnhZsDHj7AzCwa7wkkVDvRgcAlBPjso1CgVrsFzDAQzudWslzCR7j4y2XxEqzaalBWGdRhXqQJYVicjEDXlJw1XObHG19G8pGSSCi_g_ieVWbmO6nUHh4XFowXBngQcgIySidL5_UQ59FEjAQ4HAaxj-pbTd52tSASWvfiv28Z8X4HKxaZ1HX_j6OleT3bdddpr_3ZktjXh7brNiEMXSYwcpP575Kx4ASgERC5x1HOwVkLfHNsAtfb5NW68FgNHQemflHIGfU2Ri3x9weJ9Pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 21:19:02</div>
<hr>

<div class="tg-post" id="msg-131735">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ: اگه حکومت ایران به توافق نرسه، دوران بسیار بدی در انتظارشان خواهد بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 176 · <a href="https://t.me/SorkhTimes/131735" target="_blank">📅 21:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131734">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔰
4 عددسرویس VIP موجود شد
5 گیگ فقط و فقط 1.2T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchilli</div>
<div class="tg-footer">👁️ 238 · <a href="https://t.me/SorkhTimes/131734" target="_blank">📅 20:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131733">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🛜
سرور نامحدود ۲۱ روزه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط 4T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 252 · <a href="https://t.me/SorkhTimes/131733" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131732">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLZ_Y7GIXW8Q-TLlI7DRd-sQ5-yGg21eNQwLRX96Kfk7Kn1Wp7aT8bvSGFsR5POBD_bcNLlbnRblGyNjUsAhfEAq2TisY8TZdnJqb7sQ5Jzllg61FsYneWClBzsVzo7s_walClK-M3aHnl0LWFxCwPUgFI89Kf0qwPT7dz_xcT5U_Pb82xiOUuc-asSjFojPhdFcTld-T9iBxIBv4n60y1m14zbZbG-Q7OeNpgf6SQEqN-mjV6VWf-v3xWR-_GJ1I_KnEetReOPKdSwGi5FvXiNYS3jhG69LBxVhUu94iq6akOaFrfoOSfzw4ohxtPkF8HxKVsDb-LAW3QUB2akbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Nassr -
🔵
Gambaosaka
🔵
فینال لیگ‌قهرمانان آسیا
⏰
شنبه ساعت ۲۱:۱۵
🏟
استادیوم
الاول پارک
⚽️
النصر حالا با رهبری رونالدو؛ در دو بازی باقی مانده از فصل مقابل اوزاکا و داماک، فرصت دبل در قهرمانی را دارد تا سی‌آرسون، اولین قهرمانی‌های‌ خودش در تیم عربی را تجربه کند.  تیم خسوس، آمار کاملاً بهتری دارد. النصر در ۱۰ بازی، ۳۳ گل به‌ثمر رسانده و سرجمع ۳ گل خورده. این آمار برای اوزاکا در ۱۲ بازی (با احتساب پلی‌آف)، ۲۵ گل زده و هفت گل هم خورده. تیم ژاپنی با فرم ضعیف‌تری به‌میدان می‌آید. اوزاکا در پنج بازی اخیرش، متحمل سه شکست شده و این آمار برای النصر، در پنج بازی اخیرش، یک شکست و یک تساوی بوده.
📌
در
ربات
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 253 · <a href="https://t.me/SorkhTimes/131732" target="_blank">📅 20:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131731">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
فرهیختگان: سپاهان مشکل مالی داره و به بازیکناش گفته سقف قرارداد ۳۰ میلیارده و پرسپولیس میخواد از این فرصت استفاده کنه و حزباوی، لیموچی و یوسفی رو جذب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 342 · <a href="https://t.me/SorkhTimes/131731" target="_blank">📅 20:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131730">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 260T
2 گیگ 520T
3 گیگ 780T
5 گیگ 1.3T
10 گیگ 2.4T
20 گیگ 3.6T
40 گیگ 5.7T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchilli</div>
<div class="tg-footer">👁️ 483 · <a href="https://t.me/SorkhTimes/131730" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131729">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
وزیر کشور پاکستان یهویی و فوری وارد تهران شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 472 · <a href="https://t.me/SorkhTimes/131729" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131728">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
باشگاه سپاهان به مشکل مالی خورده و احتمال داره از آسیا کناره‌گیری کنه که در این صورت پرسپولیس شانس اول برای معرفی به لیگ قهرمانان آسیا هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 652 · <a href="https://t.me/SorkhTimes/131728" target="_blank">📅 17:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131727">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRo20f1q36JYqGHfNtBllCLrTLBhPpegdhvlq4CB8q2dSa6JN4Fjzrshui70NtvElWViMp8tbspSiKeSkDOc_R42z_AWtufwN9duzA7F06U7hO5VFCvNEQnTeKqj4SBNwVEscJgRd22NMbtTluK7KO8lBFEwkjxF_MV8I9RgPFND-5rkekhJmqQUWEYra2OJsKii9RlCoNUA9-5ipH7ntq4B7r8hHc8nzfbK53Y5GJV0_rdZRe-dafqr0IT7Pa_SaNSYbQf-PM6_nXRqkBpTMWixneSFMbq_xmTczl01_yBQbT8OakMynQRITwykByzwLlvLKoZMa_BxUsI8W54CUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب میتونه یه شب رویایی برای النصر و کریس باشه. اگه الهلال نتونه امشب بازیشو ببره، النصر قهرمان لیگ میشه درحالی ک خودش داره تو فینال اسیا بازی می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 803 · <a href="https://t.me/SorkhTimes/131727" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131726">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
اگه تمام نماینده های پرسپولیس در لیست تیم ملی برای جام جهانی باشند چقدر پول گیر پرسپولیس میاد
⁉️
🔴
نماینده های پرسپولیس : اورونوف - سرگیف - نیازمند - کنعانی - ابرقویی - محمدی - علیپور - محمودی
🔴
یکسری از رسانه میگن که الکسی گندوز هم اگه بره جام جهانی پاداش…</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/SorkhTimes/131726" target="_blank">📅 15:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131725">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sURyqTCaW3Nv1rS9B5NUoYssG8TB03nq_XWtbS9tvJ5Z0wHKDoO8qxXl39PXXm9wmYs_e_pBWJdTw5Ff__NWHUA_pHpML59gIRFkWStTIQBcxTauzZcjKyTtqOKZhM9m9JRzMV8HH48ar7QVo8rSmFK0sA_BkcIdJ57AiRyTRM4l2ohqcSIOccu7_DFpT5rn5Bc485TpjZio9oxgzSrqfSLEH4L_WqZlJje9TRfhJVG5m7NMMmcQ0daNOeHjXGIUU7NndhqGaP9r33aysHGADi3cZ1bNpCIA_zKCzmYgh4cYKDGrU5B1XhY3hH5dEFrDpfdQuS1gQbNbHKS64_mwTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مراقب پیامک‌های کلاهبرداری «اینترنت پرو» باشید.
🚫
🔴
اخیراً پیامک‌هایی با ادعای «آزادسازی ثبت‌نام اینترنت پرو و هدیه بین‌المللی» ارسال می‌شود که با کلیک روی لینک، گوشی را آلوده به بدافزار می‌کند.
📱
💣
✅
راهکار: لینک را باز نکنید، چیزی دانلود نکنید و این هشدار را به اطرافیان منتقل کنید تا کسی قربانی نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 726 · <a href="https://t.me/SorkhTimes/131725" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131724">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فینال لیگ قهرمانان آسیا ۲ امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 651 · <a href="https://t.me/SorkhTimes/131724" target="_blank">📅 15:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131723">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFVRJWq6PZyQyUoUMnuK8rpeJ3HB-f9nAPAPkgmfkZpf_150hNmsb1I-YoytyAp7UtLsia97e5acMyIgwp0jdroxjxvU25V6Izj86m2sgj-rlXQizuHX0EbxpLuwng8rDCjXNpoZEMTgImgLa4yiReQlknQ-Lgo9GW16kQZbeUNvzwmcmNT8T2awX9tX8kCyh_XJiylFU0ron8XhuxYTkA6psG3Thyoonyn4rQ67oah2ITwOPnmr_a_Jn8zF0880E3pdST0753mklUpFT5FxGA78PkmUKVGZIjzHXfFnIp307NyLGvAbVGFA6LXckLQQtNgMZgwkI8VcAvwWaK7u_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فینال لیگ قهرمانان آسیا ۲ امشب
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 644 · <a href="https://t.me/SorkhTimes/131723" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131722">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🛜
سرور نامحدود ۲۱ روزه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط 4T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/SorkhTimes/131722" target="_blank">📅 15:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
پرسپولیس حداقل ۸ بازیکن تو  جام جهانی داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/SorkhTimes/131720" target="_blank">📅 11:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131719">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/SorkhTimes/131719" target="_blank">📅 11:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131718">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
آتش‌بس بین لبنان و اسرائیل برای ۴۵ روز تمدید شد  پ.ن پس اگه مجدد جنگی باشه میفته بعد از جام جهانی ..  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 727 · <a href="https://t.me/SorkhTimes/131718" target="_blank">📅 11:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131717">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMim8StMKvBTBNmp-eXPjVfHjBd_je2Bosq7ERumXrwZ1jy6_R6LcvqjuD4MCbH-RRwYAbMw7boESRxo-o44Jq1aNltn9UGjpYXRsVnoVRh8FnUr29_XrJV3nKXB5FMHHrd3LIvfbuVqwEvnrCGjMjhDUr3V3EpOW7qZxNMN-OPL7ixc59DdJNBbXH8kDUi1nAHt_ku_UHi2oCeIjHO197IF1FGvm1rGwT_5lPwqScpICwULtdATNlbBo1h3xIQom94f968Ug9PQ1xlKjbuZTvN_OSLWDzCQdaZ9EaRvXbYbQz3DdL9GbIZlp3PRDashRXmLSHuBpgt1qLCii4AlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس
؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 725 · <a href="https://t.me/SorkhTimes/131717" target="_blank">📅 11:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131716">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVBA86pOWb6xUMOSNilrfFUwuxkOg5ehtYyYk0yFHhkql34QmuETYZ9t9aJ-XQsy2jnyfqaNI13_Aggx1bR-gtg273gi0EPDQm5NXWwTHmTLVBWybSj-2dpjp35ShR6DBdZNkEOCDaRtWeeFaYHcOP_SWMCD298mmACKdwdbGjfjGX-QI_RedfS4u9waiUDRqPEcX0QfkYP55wPlYhZXWERs7MoQAOVl-Pb0xEOOtWJcMMmuO57E8SLzs7eww97KsjmfBKtyIVuR04SG9U5yqIHojbdZfOXtqIP4la6m8M3J3pDCT63IY10pUI67GM7D6wO_s-TXUMr9tue3Z0H5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز امیدواری کرده که باشگاه بتواند غرامتی را از اوریه دریافت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/SorkhTimes/131716" target="_blank">📅 11:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131715">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYcrEVmyeC1hfCV3m1RaHmKiA2yQFyZ6Ij53l9tpR7XHB9PRJWqkYU0Ro0KYvIYx-ZrsBEBogxDSgjqO8dyr0POx8hwbXHJ-yZWxf5G0qlK7s5NgqYADgc9toSO3EVEsjzRJXM91FiehJ6T5RHaw3eRRivaBTfaOHpjNr2EfHwrdltG3QYJSGYq66vYonQfW3CrVPs2b5O3qz50ad-o4utlS02YJ1-iUOyfiwZySOslnF_b87u9UWqR6WVxOfxK6pjgjmlPRwo18gPuYIJs0z5dg-EhFztRddSEmIstgHPHLTo8XPuoOulCtshT18t90DuueaYgmsZQJUy3MV0qriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه بازی‌های مهم فردا فوتبال
⚽️
فردا دیدارهای جذاب و هیجان‌انگیزی در فوتبال اروپا برگزار می‌شود که در مهمترین بازی‌ها، سیتیزن‌ها در فینال جام‌حذفی باید با آبی‌های لندن تقابل کنند. بایرن در زمین خود از کلن میزبانی ‌می‌کند و دورتموند هم میهمان وردربرمن می‌باشد. همچنین در دیداری حساس و در فینال لیگ‌قهرمانان آسیا سطح دو، رونالدو و یارانش باید به مصاف نماینده ژاپن گامبااوزاکا بروند.
⚽️
بازی‌های فردا رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید.
📌
وینکوبت
انتخابی حرفه‌ای‌ برای شما، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/SorkhTimes/131715" target="_blank">📅 01:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131714">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d607431a7.mp4?token=D4xoguYWuYKo2agqCS4phDdKQSbd4uuBJKTFT8-4iTSgIGVnu2hrgQA2uPH4QATBv2j6-1x-DAotCVIi5_bm-HkwIEdZTgTnIrditRCmDVexRfT5Ea0v-IO44hpzj596XfRfgtDuMKRA0ostbqzqKEfoPUnEkhXNhb4k185A_rIq8wLWpdsKHbUHuGess_hWMoM-oQwVuzQ5DMj4NQpoc-7Fuz3iIsjz0hu7QDRrRXFZRl7KAnmru0tvbzuDnbibjZ88DWw4iy1JpqAmU7crdvmSRvEWdmKf5RAm-bfjq8GFSluWEPNuIivnzIFx6ElV-sBBfE1cRe1XBWTQn3VSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d607431a7.mp4?token=D4xoguYWuYKo2agqCS4phDdKQSbd4uuBJKTFT8-4iTSgIGVnu2hrgQA2uPH4QATBv2j6-1x-DAotCVIi5_bm-HkwIEdZTgTnIrditRCmDVexRfT5Ea0v-IO44hpzj596XfRfgtDuMKRA0ostbqzqKEfoPUnEkhXNhb4k185A_rIq8wLWpdsKHbUHuGess_hWMoM-oQwVuzQ5DMj4NQpoc-7Fuz3iIsjz0hu7QDRrRXFZRl7KAnmru0tvbzuDnbibjZ88DWw4iy1JpqAmU7crdvmSRvEWdmKf5RAm-bfjq8GFSluWEPNuIivnzIFx6ElV-sBBfE1cRe1XBWTQn3VSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: از اوریه غرامت می‌گیریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/SorkhTimes/131714" target="_blank">📅 00:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131713">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-L5eu3OCqCUByOBUrTqbz3_ypmwDs9eYLYK6161CRJJCKdhoxyiDRJe0bgfolDHJB3y99iOHrzuHuxCDMwBKQmjVkjiQJxq7RVYjYBEg2nrHdXJLcjUpjKmCAiwjGDRbIbMP6604TXOWxBs5p_1cM_3fobpUtQB2Z6Z5oTrN4UvjLa4o-GlB9jATOsqNIJgmtV4HkRLhYzgNgXL2clvBecv9EpYpICGu8_UvvZ6ovZRycTfk0hoVDIwm1lreUkgQIK_ZBy_EvoXQjRK-KgruntvLbkCuNHGRL4umiupacFec3-tKCvo5YbG3-3VjslEMHfdM_BpyABc51qFq-mkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
محمدمهدی محبی، وینگر تیم اتحاد کلباء امارات تا پایان فصل به تیم فوتبال سپاهان پیوست.  پ.ن اینم پرید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/SorkhTimes/131713" target="_blank">📅 00:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131712">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4ec80a48.mp4?token=FfHSSYiVL2dmRqdQP5pveHlp27jiwyngE8TioqVMCOxhT8P8ajzhucldr5CT25_HTBQom4IdCmCtm20enhrSsSb4Gyu2q0pHt8CEP0NmWo2NtgaFwZ7v5I3--BUKYJl2TX1lYDI8T1vdr54TG8YGs2PZ7iNzbRndiNE0euXqUhBICoLxPditESckt30jOZwTKriBtgrqNzc2lmwUEEqbBqwWL5rjJDC7Z3Vcl3N9ZRUBTjnWFuBw2IvmDORAI0zqINMXrAVABmJAtLhPcmbLpnu6QFQlvyNlvE0pISgwCviee7ajMyGUYHFgKqzI5iSBPxCSy6V8J26CDMQb1DM7zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4ec80a48.mp4?token=FfHSSYiVL2dmRqdQP5pveHlp27jiwyngE8TioqVMCOxhT8P8ajzhucldr5CT25_HTBQom4IdCmCtm20enhrSsSb4Gyu2q0pHt8CEP0NmWo2NtgaFwZ7v5I3--BUKYJl2TX1lYDI8T1vdr54TG8YGs2PZ7iNzbRndiNE0euXqUhBICoLxPditESckt30jOZwTKriBtgrqNzc2lmwUEEqbBqwWL5rjJDC7Z3Vcl3N9ZRUBTjnWFuBw2IvmDORAI0zqINMXrAVABmJAtLhPcmbLpnu6QFQlvyNlvE0pISgwCviee7ajMyGUYHFgKqzI5iSBPxCSy6V8J26CDMQb1DM7zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی: سروش رفیعی به تمرینات پرسپولیس برمی‌گردد. صحبت‌های پیمان حدادی در مورد آخرین وضعیت سروش رفیعی در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/SorkhTimes/131712" target="_blank">📅 23:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131711">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💢
پیمان حدادی: اگر پرسپولیس برای آسیا معرفی نشود، حقمان ضایع شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/SorkhTimes/131711" target="_blank">📅 23:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131710">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/091a89d5de.mp4?token=A9ro2ehrGqYIJfu2ny9IQVBofQIZ5wLgU4QiAqZ_gqmhPW2nWWgQVJSxTdrafkXA9kwq2w_ln38L6fDF1f6CZvCSL8g0eaOlQ334g781oYpIzEBtkyvQR67C6Khi5Oflb56SWpPONR-oOHQlNhLqAP5HrHCx4xq2GzftDywkmt6sxpkIQynsJCA80cfTX0R_cXkZA87ZLuI4r2r1yObvTrQMF1VV0qXOVOebWXguyfVqhu--82XBKroPYQ70sGXakqK_S98uzPsKhGfsARvPcfGuHpiSx4gtP6FDoPA5D6hlbcjDApk1ZlugVZQQk15m8iVEVV0GSdAg7VNABGACb0_kDoN2UmPg67TCzY4YY8hUBxdWFHNwKvDOA9js5n9ddORkhEH2cB8euLMQkzE-5rugbhM5KWMsmXBSGRTysnWMtYc2RGo8wznTVDV0UaIOcZxzFHGMl9gBYlODXEnSISD_LojIceDupGoil9emB4NESkGsGXyHnsd6Vw1uWlhdgl0PFl7Ux520pPJokbNc3e3J90k47nmy3gphR_VfE3jBNzyYOGDziE6ftHgYP6-aTMDbWnTYM5ojgumEhaHDqcZQW6ODHAF-OcO0Of0YMllI49Ta7-ozFYOMa_XTw8HvvoB4txXH8lf6E6ejLz1P9llSN11dwagmSmXtsaPLkAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/091a89d5de.mp4?token=A9ro2ehrGqYIJfu2ny9IQVBofQIZ5wLgU4QiAqZ_gqmhPW2nWWgQVJSxTdrafkXA9kwq2w_ln38L6fDF1f6CZvCSL8g0eaOlQ334g781oYpIzEBtkyvQR67C6Khi5Oflb56SWpPONR-oOHQlNhLqAP5HrHCx4xq2GzftDywkmt6sxpkIQynsJCA80cfTX0R_cXkZA87ZLuI4r2r1yObvTrQMF1VV0qXOVOebWXguyfVqhu--82XBKroPYQ70sGXakqK_S98uzPsKhGfsARvPcfGuHpiSx4gtP6FDoPA5D6hlbcjDApk1ZlugVZQQk15m8iVEVV0GSdAg7VNABGACb0_kDoN2UmPg67TCzY4YY8hUBxdWFHNwKvDOA9js5n9ddORkhEH2cB8euLMQkzE-5rugbhM5KWMsmXBSGRTysnWMtYc2RGo8wznTVDV0UaIOcZxzFHGMl9gBYlODXEnSISD_LojIceDupGoil9emB4NESkGsGXyHnsd6Vw1uWlhdgl0PFl7Ux520pPJokbNc3e3J90k47nmy3gphR_VfE3jBNzyYOGDziE6ftHgYP6-aTMDbWnTYM5ojgumEhaHDqcZQW6ODHAF-OcO0Of0YMllI49Ta7-ozFYOMa_XTw8HvvoB4txXH8lf6E6ejLz1P9llSN11dwagmSmXtsaPLkAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پیمان حدادی: اگر پرسپولیس برای آسیا معرفی نشود، حقمان ضایع شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/SorkhTimes/131710" target="_blank">📅 23:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131709">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: دوستان فدراسیون فوتبال زودتر اعلام کنند که آیا برای فصل سقف بودجه گذاشته می‌شود؟
❌
آیا برای فصل بعد قرار است برای جذب بازیکن خارجی محدودیت اعمال شود؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/SorkhTimes/131709" target="_blank">📅 23:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131708">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🛜
سرور نامحدود ۲۱ روزه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط 4T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 855 · <a href="https://t.me/SorkhTimes/131708" target="_blank">📅 23:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131707">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 1.4T
10 گیگ 2.4T
20 گیگ 3.6T
40 گیگ 5.7T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/SorkhTimes/131707" target="_blank">📅 22:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131706">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: دوستان فدراسیون فوتبال زودتر اعلام کنند که آیا برای فصل سقف بودجه گذاشته می‌شود؟
❌
آیا برای فصل بعد قرار است برای جذب بازیکن خارجی محدودیت اعمال شود
؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/SorkhTimes/131706" target="_blank">📅 22:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131705">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
حدادی: محسن خلیلی تا پایان فصل سرپرست تیم بزرگسالان پرسپولیس و جانشین افشین پیروانی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/SorkhTimes/131705" target="_blank">📅 22:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131704">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
حدادی مدیرعامل پرسپولیس: با خانم مرضیه جعفری سرمربی تیم ملی فوتبال بانوان و خاتون بم وارد مذاکره شدیم و قرار است در خدمت ایشان و بازیکنان تیم خاتون بم برای فصل آینده در تیم بانوان باشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/SorkhTimes/131704" target="_blank">📅 22:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131703">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4464cc1d8f.mp4?token=jOec9a3wBUvkOsOl_fzuoM4AYBOE6wPtjJ-DtSMRkYv58oVsU3c3DWJ0tdhv8nKetJ_NFOrwlq6Eh82bhNEg3nhjf_xk2MNWRifp_CsEv1T5YnGcwh_0XXB5h0jOGp7Yr_vSUDeIchCbZVsYso3Nx4R5LDm5zCxVih79nkVRECf28EA31mg6BCMmjLzMWuUqf9KUBU1G7biLAcS3lQh7BNF3BSuhelD79_FTfh-cPcl2CEpAKOipeibxi8pwW2fSwdim0juIudeBwXGEPu31oK6VYmXMEKQj_G6tPYMrW5wplwBAY68aS7TU8dSSyQTpJlNiSc9TJc-F7ZK3ouNCTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4464cc1d8f.mp4?token=jOec9a3wBUvkOsOl_fzuoM4AYBOE6wPtjJ-DtSMRkYv58oVsU3c3DWJ0tdhv8nKetJ_NFOrwlq6Eh82bhNEg3nhjf_xk2MNWRifp_CsEv1T5YnGcwh_0XXB5h0jOGp7Yr_vSUDeIchCbZVsYso3Nx4R5LDm5zCxVih79nkVRECf28EA31mg6BCMmjLzMWuUqf9KUBU1G7biLAcS3lQh7BNF3BSuhelD79_FTfh-cPcl2CEpAKOipeibxi8pwW2fSwdim0juIudeBwXGEPu31oK6VYmXMEKQj_G6tPYMrW5wplwBAY68aS7TU8dSSyQTpJlNiSc9TJc-F7ZK3ouNCTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: افشین پیروانی قرار بود به یک کشور دیگر برود نه آمریکا/ او برای رفتن به سفر از من اجازه نگرفت
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/SorkhTimes/131703" target="_blank">📅 22:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131702">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
پیمان حدادی : پرسپولیس پرهوادار ترین تیم ایرانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/SorkhTimes/131702" target="_blank">📅 22:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131701">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
حدادی مدیرعامل پرسپولیس: با خانم مرضیه جعفری سرمربی تیم ملی فوتبال بانوان و خاتون بم وارد مذاکره شدیم و قرار است در خدمت ایشان و بازیکنان تیم خاتون بم برای فصل آینده در تیم بانوان باشیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 834 · <a href="https://t.me/SorkhTimes/131701" target="_blank">📅 21:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131700">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
ترامپ:  ممکن است مجبور شویم یک کار تکمیلی کوچک در ایران انجام دهیم، چون یک آتش بس یک ماهه داشتیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/SorkhTimes/131700" target="_blank">📅 21:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhAIRdHark9vSP9MpIBQCgAqUsNZo4fcx8HYxFMPC5relwIvjdA7eMIz6b2j5zbPd7RPu82QbEcYnPR9VGrH1P-kNnL6ap7XwGBfMgTZyJ4Qtwi4eYoyax2jmYwswg-5A_ODYm2S6IkcvLHzeZBstyTv2TwTOJkI-wj_agqVFdEc7bsVUsPFhXLy_HUB2xsDhLjIdY2Wn2-m7eKXxtfp6sCkXWJ1T2o2LTR-PrtzdKTCQJB97sIZBPFL4zelVRxIi1ww6Qpywci1fIFBsQy_z40WsOO-pwRqzWCLHzZXECaD2iHMTFAdruGkt2ZV6YYkqQXDdr4lz2aEpB6m0WQWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توییت جدید و عجیب دونالد ترامپ
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/SorkhTimes/131699" target="_blank">📅 21:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🛜
سرور نامحدود ۲۱ روزه Anyconnect
فقط 4T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/SorkhTimes/131698" target="_blank">📅 20:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
ترامپ: اولین جمله پیشنهاد ایران را دوست نداشتم، برای همین آن را دور انداختم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/SorkhTimes/131697" target="_blank">📅 20:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
آشوبی: استانداردها را به فوتبال روز دنیا نزدیک می‌کنیم/ مسلمان نیاز به فضایی تازه داشت
🔺
تفکرات و ایده‌های بسیار مثبت و قوی در باشگاه، به ویژه در بخش آکادمی وجود دارد که به نوعی برای اتخاذ این تصمیم مشوق بنده بود که در ادامه مسیر بتوانم در این حوزه کمک‌کننده باشم.
🔺
مربیان آکادمی سال‌ها در این رده کار کرده‌اند و شناخت خوبی دارند.
🔺
برای از دست ندادن استعدادها، تیم ب تشکیل می‌دهیم.
🔺
انتظارات هواداران از چهره‌های شناخته‌شده به حق است.
🔺
محسن مسلمان نیاز به بستر تازه‌ای داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/SorkhTimes/131694" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131693">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
ویزای هیچ یک از بازیکنان تیم‌ملی ایران تا این لحظه صادر نشده است
❌
برخلاف تقریبا تمام تیم‌های حاضر در جام‌جهانی که همگی ویزای خود را دریافت کرده‌اند[بجز عراق]، تا این لحظه ویزای هیچ یک از بازیکنان تیم ملی ایران صادر نشده است.
⚠️
مهدی تاج قراره در ترکیه با…</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/SorkhTimes/131693" target="_blank">📅 19:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131692">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 797 · <a href="https://t.me/SorkhTimes/131692" target="_blank">📅 18:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
ویزای هیچ یک از بازیکنان تیم‌ملی ایران تا این لحظه صادر نشده است
❌
برخلاف تقریبا تمام تیم‌های حاضر در جام‌جهانی که همگی ویزای خود را دریافت کرده‌اند[بجز عراق]، تا این لحظه ویزای هیچ یک از بازیکنان تیم ملی ایران صادر نشده است.
⚠️
مهدی تاج قراره در ترکیه با…</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/SorkhTimes/131690" target="_blank">📅 18:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
ترامپ: اولین جمله پیشنهاد ایران را دوست نداشتم، برای همین آن را دور انداختم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/SorkhTimes/131689" target="_blank">📅 18:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
مشاور وزیر ارتباطات: اینترنت بین‌الملل حتماً به حالت عادی برمی‌گردد، خیال مردم راحت باشد.
🔺
روزانه پیگیر بازگشایی هستیم و بخشی از خدمات بین‌الملل هم‌اکنون برگشته است. امیدواریم در ماه‌های آینده با تصمیم نهادهای امنیتی، دسترسی کامل برقرار شود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/SorkhTimes/131686" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
پرسپولیس به دنبال تغییر سرپرست نیست؛خلیلی روی نیمکت می‌نشیند
❌
پس از کنارگذاشتن پیروانی به دلیل سفر به آمریکا در میانۀ جنگ، در روزهای اخیر نام چند پیشکسوت برای پست سرپرستی پرسپولیس مطرح شد اما پیگیری‌ها نشان می‌دهد که باشگاه برنامه‌ای برای تغییر موضع خود ندارد و درصورتی‌که مسابقات ادامه پیدا کند محسن خلیلی روی نیمکت می‌نشیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/SorkhTimes/131685" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
هلدینگ خلیج فارس به مدیران استقلال گفته پول نداریم و فصل بعد خبری از خرید خارجی و بمب و اینا نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/SorkhTimes/131684" target="_blank">📅 17:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
پرسپولیس
حداقل ۸ بازیکن تو
جام جهانی داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/SorkhTimes/131679" target="_blank">📅 16:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thFvDNYSJBhi4e_QHnGBuBwFCk-HmcyUtMVebeIILNQDSMs_HYxmkqCZ549S1bw2IsSMg6wWeX6HaKaZQ7EZF9AOaDwa8qCnkHe6Yuku8ut9J3bKrWeBLzQchZNxXJaOPI65C_nQenLUvlnxm2V1d5j_KwT7nYcoXCiG8ip_TABZtZEvCKQK1HJ7NEQI-F41bHnkHnncTi2GymuiHNmb3rJKUtUrnkDXhR9_itA1MK39TxvnxWn1MhEvTMyXzn08ddEC0kXQ-NyyMg1R21IsO-1YPMhSms9EeRBahgE5unU_5mNLVRbdHwYjfetUifwgNcVTmkBLHMHrLF50q12htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی، شهردار تهران: ما قصد داشتیم قبل از جنگ بیت رهبری رو با معماری جدید بازسازی کنیم، اما آمریکا عملیات تخریب رو که بسیار هزینه‌بر هم بود برای ما رایگان انجام داد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/SorkhTimes/131678" target="_blank">📅 16:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2kHcc3vuNoK8ELuywHURWErRIlePXL09nINoGdOgF-VxoozEzCjsmZVurWOhsWLxU_jSk9GgItqt4te9Hz85vp_JOKEkWuMzneXy_CC2OH2vusrb1W3L6HEbi4Yi3GWAGH2bxT9XLn0TcVg5ChPME0OzXrwLWmIxDHxIvcSLW4AzV7O_BGQNz9_XYXGL1PuIqXoeye0nWxZ1dSFgjkJgsFG_qhH4O_JK9tnU3GzGA0GNE6Qv1hvXoh39cxNNY2eWGEZhxM2_JbUsn92fCK7yhdzHEDXRyecQLovnmcCJrc9euX4Sp3zo1GUiUp92gSAWkA5A4kr7ddIbzUPkbL4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاربران محترم برای دسترسی به سایت وینکوبت فقط کافیه از طریق ربات وینکوبت وارد بشید.
🤖
-
@Wincobet_bot
🤖
-
@Wincobet_bot
📌
بدون نیاز به جستجو، بدون لینک‌های پراکنده، همه چیز از طریق خود ربات انجام میشه.
📌
ویژگی‌های ربات وینکوبت:
👇
▪
︎ورود سریع و مستقیم به سایت
▪
︎دسترسی راحت از داخل تلگرام
▪
︎بدون مراحل پیچیده یا ورود جداگانه
📌
اگر دنبال یک راه ساده و سریع برای ورود به
وینکوبت
هستید، این ربات ساده‌ترین مسیر دسترسی شماست:
👇
🤖
-
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/SorkhTimes/131677" target="_blank">📅 16:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1942fb9fb8.mp4?token=mNEe8U_dDI5I214YzQ33dUPTNV2OPOi5ZaYUaTc0xPzyoZEYSY8dG93Gca6syJflJtNV2uPxEAuSu-r74c31Bzu2XudaE_bvZSEMxONq-x0w75ByI6uIIY3gOPTVXa5COBMSkSR5euEdvNALij8ZIMnVWf7hiaA0pF3kgcvUWsSzwP662T-YeA_ZpHMLJ2xvWM1i47KMnA1e3XqSjASdTKYEtH1cHPXdYUBkn9e8-d3Pc4DhU8cDOWps-KjWQ593FUFL948IeGy0dOsszBO8N-NLgKc3CEwS4ujvUwKMXAf9EXHetqcWtWhAThK7ZYg6qhBSBuVfPJWc6l9myOHuKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1942fb9fb8.mp4?token=mNEe8U_dDI5I214YzQ33dUPTNV2OPOi5ZaYUaTc0xPzyoZEYSY8dG93Gca6syJflJtNV2uPxEAuSu-r74c31Bzu2XudaE_bvZSEMxONq-x0w75ByI6uIIY3gOPTVXa5COBMSkSR5euEdvNALij8ZIMnVWf7hiaA0pF3kgcvUWsSzwP662T-YeA_ZpHMLJ2xvWM1i47KMnA1e3XqSjASdTKYEtH1cHPXdYUBkn9e8-d3Pc4DhU8cDOWps-KjWQ593FUFL948IeGy0dOsszBO8N-NLgKc3CEwS4ujvUwKMXAf9EXHetqcWtWhAThK7ZYg6qhBSBuVfPJWc6l9myOHuKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
افشاگری بهزاد داداش زاده مسئول برگزاری مسابقات هیات فوتبال استان تهران از زد و بند خلیلی در آکادمی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/SorkhTimes/131676" target="_blank">📅 14:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SorkhTimes/131675" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
ترامپ، رئیس‌جمهور آمریکا: ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 910 · <a href="https://t.me/SorkhTimes/131674" target="_blank">📅 14:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ترامپ: اخرین چیزی که بهش نیاز داریم الان جنگه، ایران میتونه اورانیوم خودش رو به امریکا یا حتی چین تحویل بده و دیگه جنگی در کار نباشه!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 959 · <a href="https://t.me/SorkhTimes/131673" target="_blank">📅 14:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131672">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
ترامپ، رئیس جمهور آمریکا: من دیگر خیلی بیشتر از این صبر نخواهم کرد؛ آنها باید توافق را امضا کنند!!
❌
رئیس جمهور چین به من اطمینان داد که با داشتن سلاح هسته‌ای توسط ایران مخالف است.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/SorkhTimes/131672" target="_blank">📅 14:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131669">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/SorkhTimes/131669" target="_blank">📅 13:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131668">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
وزارت خارجه چین: در مسئله هسته‌ای ایران، استفاده از زور به بن‌بست رسیده است
🔴
درگیری بین ایران و آمریکا هرگز نباید اتفاق می‌افتاد، نیازی به ادامه آن نیست و پکن همواره معتقد بوده که گفتگو و مذاکره بهترین راه است و بايد يک راه حل فوری پيدا شود.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131668" target="_blank">📅 13:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131666">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
رسانه های مملکت : ترابی و اسماعیلی‌فر دوس دارن دوباره برگردن پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SorkhTimes/131666" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/SorkhTimes/131665" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131664">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
دیشب تو لیگ سوئیس تیم اف سی تاون که موفق شده چند هفته قبل از پایان لیگ این کشور قهرمان بشه به تیم یانگ بویز 8 بر 3 باخته و دو تا اخراجی هم داشته!
❌
همین بازی باعث شده تا فیفا به دلیل شرط‌بندی ورود کنه و ممکنه لیگ این کشور کلا تعلیق بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/SorkhTimes/131664" target="_blank">📅 12:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131663">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
پرونده های باز باشگاه استقلال در فیفا
⏺
منتظر محمد: ۲۸۸ میلیارد تومان
⏺
پیتسو موسیمانه: ۶۵۶ هزار دلار
⏺
کوین یامگا: ۸۱۵ هزار یورو
⏺
ایجنت یامگا: ۲۸۰ هزار یورو
⏺
آلمدین زیلیکیچ: ۸۱۵ هزار یورو
⏺
وردان کیوسفسکی: ۴۸۵ هزار یورو
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/SorkhTimes/131663" target="_blank">📅 12:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131662">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
فوری/ آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
❌
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
❌
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به…</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/131662" target="_blank">📅 12:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/SorkhTimes/131661" target="_blank">📅 11:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131659">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
احتمال انصراف سپاهان از آسیا / پرسپولیس جدی‌ترین مدعی جایگزینی
🔴
مدیران باشگاه سپاهان به‌دلیل فشارهای مالی و هزینه‌های سنگین حضور در رقابت‌های آسیایی، در حال بررسی احتمال انصراف از لیگ قهرمانان آسیا هستند؛ اتفاقی که در صورت نهایی شدن، یکی از بزرگ‌ترین شوک‌های…</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/SorkhTimes/131659" target="_blank">📅 10:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
خبرهای اولیه از توافقات میان چین و آمریکا میاد شامل مواردی :
🔺
خرید بیشتر سویا از آمریکا
🔺
خرید نفت بیشتر از آمریکا
🔺
خرید بیشتر گاز مایع ( LNG )
🔺
خرید 200 جت بوئینگ
🔺
ترغیب ایران به اعطای هرچیزی که ترامپ نیاز دارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 928 · <a href="https://t.me/SorkhTimes/131658" target="_blank">📅 10:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/SorkhTimes/131657" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131656">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
مهدی طارمی دو سال پیش تصمیم گرفت از پورتو جدا بشه و به اینتر قهرمان ایتالیا پیوست و همراه این نتونست هیچ جامی بدست بیاره و در نهایت آخر فصل از این تیم جدا شد و به المپیاکوس قهرمان یونان پیوست و همراه این تیم هم نتونست امسال قهرمان بشه و فصل رو بدون جام تموم…</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/SorkhTimes/131656" target="_blank">📅 10:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131655">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYDqO3tGxE8S_GMZt_nQRMAh48qbI2evjBnUd1xOyU_E9dkDo3j1Eeq4vLrZJLCdyRoMUz84sO7_olh6cNmXE3vniejA9fatl3rvkwWeL2DWp6ubXG8NBiT9qzLwUG0GgZY9_CxulhdcZRBZvgXD_Ii07mFJTls597N0W5VpatEJvpw_HvKeAelSzjMUDkfjzgQM5HqqQ1dqmCxKvCDLQZ_vHct6d_EB2aMZu0lBnpmE1n78El84vYPHjqxC94efEf4yenlxJJ67Zjga7ndzjGSEw8AAKFAKsgrLB3ZGtRtVTuDPMfhvAkKubxJ2WA5f8f1-AYgC4gGHDwHeevy0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131655" target="_blank">📅 01:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131654">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
#خبرگزاری‌مهر : برسی آمار ها نشان میدهد استقلال، پرسپولیس و تراکتور شانس بیشتری برای حضور در آسیا خواهند داشت
🔴
این در حالی است که سپاهان در دیدارهای مستقیم مقابل رقبای سنتی خود نتایج ضعیفی کسب کرده و شانس کمتری برای کسب سهمیه خواهد داشت
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/SorkhTimes/131654" target="_blank">📅 00:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131652">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
با اعلام مهدی تاج، باشگاه استقلال مجوز حرفه ای گرفت تا حضور این تیم در فصل آینده رقابت های آسیایی به نوعی قطعی شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131652" target="_blank">📅 23:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131651">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚡️
⚡️
قلعه نویی ستاره پرسپولیس را خط می‌زند!؟
❌
در تیم ملی به هدایت امیر قلعه‌نویی، رقابت در خط حمله خیلی شدید شده. حضور سردار آزمون و مهدی طارمی تقریباً قطعی است و بازیکنانی مثل شهریار مغانلو و امیرحسین حسین‌زاده هم شانس بالایی دارند.  به همین دلیل احتمال دارد…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131651" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131650">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
فووووووووووووری
🔴
به دلیل پیش رو بودن جام ملت‌های آسیا در دی ماه و برنامه آماده سازی تیم ملی برگزاری ادامه لیگ برتر پس از جام جهانی منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131650" target="_blank">📅 23:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131649">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
معامله‌گری: تنها با برگزاری مجدد لیگ عدالت در فوتبال ما برگزار میشه و قهرمان باید با بازی کردن مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131649" target="_blank">📅 23:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131647">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
پیغام عجیب بیرانوند به حدادی، مرا به پرسپولیس برگردانید!
🔴
به گزارش شهرآرانیوز، علیرضا بیرانوند که خودش را برای جام جهانی آماده می‌کند، نیم نگاهی هم به آینده خودش بعد از این مسابقات دارد. او از چند ماه پیش به دنبال بازگشت به پرسپولیس بوده و در شرایط فعلی…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131647" target="_blank">📅 22:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131646">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔺
بخشش جریمه خداداد عزیزی توسط کمیته استیناف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131646" target="_blank">📅 21:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚪️
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131644" target="_blank">📅 20:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
معامله‌گری: تنها با برگزاری مجدد لیگ عدالت در فوتبال ما برگزار میشه و قهرمان باید با بازی کردن مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131643" target="_blank">📅 20:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💬
🔴
امیرحسین اصلانیان، پیشکسوت پرسپولیس :
◽️
تعویق لیگ باعث شده باشگاه‌ها از شرایط آرمانی دور شوند و به اعتقاد من هیچ تیمی با آمادگی کامل وارد مسابقات نخواهد شد. حتی این احتمال وجود دارد که لیگ بعد از جام جهانی هم برگزار نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131642" target="_blank">📅 20:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
حمید رسایی: دولت میخواد قیمت بنزین رو تا ۲۰ هزار تومان افزایش بده
.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131641" target="_blank">📅 19:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZ6Bb-5QGUF-CZGtJP-zpFi5HAMcAQaeXjc1tnWCiHPR-zmU6A1oDDQc-tsmdfk0Cy_g8KyNMiuc5uDu9HN_zKqJV3qI6OhFcDM_VZ3OYT1Zp76y2dzFwJtaXbIeK8-xlRyCovOMELWkPoxM4ywlTDi4_GpubbSQU_UQd6vLv5z5bUx47GthbMqUvWKWUOe2pXhHJfeqrPpKoIc96kHRoNiHqzP1UVKjKkw_kGoaNqbQin8WDgsgjWhdcWJ3FKJGJFkCXt1eN141LbofXb9g3i6TBb5pjNvtyokSCGaqCrfB5DQ2xaiUbGjvHUXh06K2CmmgrJNqUzMuKDDnwZiPSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روزنامه اعتماد آنلاین:
🔺
اینترنت بین الملل خرداد ماه وصل میشه
🔺
هفته آینده به ریاست عارف معاون پزشکیان قراره زمینه‌های لازم برای رفع قطعی اینترنتی فراهم بشه تا حداکثر تا وسطای خردادماه اینترنت وصل بشه
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131640" target="_blank">📅 19:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBeVlL36-dVof8Sh4HJtVaz0VG3uA3TXHhJX_bOiq9s4R2nIrcbslllY02ovsYtlstYWRycgJHtWc_Py5n9Ne5g9CsGRUOvdAC7tHX75svj70OoulDmfJxIXOg8LYzrEieeg7A6UmwWYCR7xvrXJKr4gJT8AeQjxIDfnd-wEFmAM_k2OGXHKb-vhybdM4rbC3QI_EdEh-sWQsWSlWHsqAXTICAuhT5--2-8U2s_DwRMaBl6dTv-lraKmDObCHBRXnZ2eqC28qjl0yKQ8b8SJchxZeWQDmvnCfnJjRb9C_Ac3x8qbuicBKTiSSOcJ0mgINDF9LwxyWHg032IUPwlJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دنیس اکرت، بازیکن دورگه ایرانی که برادرزاده آناهیتا درگاهی، بازیگر سینما است، نام خانوادگی خود را در سامانه فیفا به دنیس درگاهی تغییر داد و مشکل او برای حضور در تیم ملی ایران حل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131639" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🛜
دو
عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131638" target="_blank">📅 15:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
خبرهای اولیه از توافقات میان چین و آمریکا میاد شامل مواردی :
🔺
خرید بیشتر سویا از آمریکا
🔺
خرید نفت بیشتر از آمریکا
🔺
خرید بیشتر گاز مایع ( LNG )
🔺
خرید 200 جت بوئینگ
🔺
ترغیب ایران به اعطای هرچیزی که ترامپ نیاز دارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131637" target="_blank">📅 15:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔵
تاجرنیا خبر داد: هزینه‌های استقلال در فصل آینده به خصوص در جذب بازیکن به شدت کاهش پیدا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131635" target="_blank">📅 14:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚪️
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131634" target="_blank">📅 14:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIZjWlWzrcsMhsQi0EDoZeXpYpOL4xypU5MIQ1d_YazTsS0swtFMUwGmrft7Oe_N3xGREu-lTCmDBWvojviCBCueeWn4RiqepX0cbP5HXqSHf1eLrAOffKIrohwQLURrCZxJy2ujjMvdu8ChfFug-W7GPWi0gA-xLnUbhH9xuww9gQPLXd6e_EpSNWkisLf5cIRz0TBlRLKECL1CxlqgkwhB9COalrRpzZaub0EQKNicsQUepE28-EnUJWh-MlfKasyOxz4HxNwkhFnzfEdjRUmXeKAe79iJTlR5k-LuGWh3Zy1rJUfIW71cqdSISWQR8MCrE1ZYHbxmQey4s2d1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
🔴
امیرحسین اصلانیان، پیشکسوت پرسپولیس :
◽️
تعویق لیگ باعث شده باشگاه‌ها از شرایط آرمانی دور شوند و به اعتقاد من هیچ تیمی با آمادگی کامل وارد مسابقات نخواهد شد. حتی این احتمال وجود دارد که لیگ بعد از جام جهانی هم برگزار نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131633" target="_blank">📅 14:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131631">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
پاتک بزرگ پرسپولیس به تراکتور؛ اوسمار ستاره‌های سابق خود را می‌خواهد!
🔺
تیم مدیریتی جدید پرسپولیس به شدت در تلاش است تا دو ستاره سابق خود را برای لیگ بیست و ششم به تهران بازگرداند. به ویژه حالا که اوسمار دوباره هدایت پرسپولیس را برعهده گرفته است؛ این سرمربی برزیلی در گفت‌وگو با مدیران پرسپولیس در چندین نوبت اعلام کرده که خواهان جذب این دو بازیکن است. ترابی و اسماعیلی‌فر گفت‌وگوهای با مدیران پرسپولیس در این زمینه داشته‌اند و به آنها چراغ سبز نشان داده‌اند!
🔺
این در شرایطی‌ست که از تبریز خبر رسیده باشگاه تراکتور به محمد ربیعی سرمربی جوان خود تضمین داده است که ترابی و اسماعیلی‌فر دست کم یک فصل دیگر نیز در تبریز خواهند بود و برای پرشورها به میدان خواهند رفت. باید منتظر ماند و دید آیا انتقال این دو بازیکن از تبریز به تهران انجام خواهد شد یا خیر؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/SorkhTimes/131631" target="_blank">📅 13:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131630">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsLd3xg5ZgX_O_MPH7BnFS3WWPFph2p0pUVrqKjJbZPJQ92nz64ar0KRCQ_1-1-xbFzM_UIGJQjAqrscLyPdQZhc1mS7u5-v30mat_UprmVjqw85GHABeXCrG8ld0PEU3oZvLDIO4VqlJ75DWDItlhvJfD5liptszaQ7qC26kl6VyBvA4QcSuutxcZYKyRjDulY450Mspctx6GC4ISO4Ge8ym1Vh9jMEWTdvzsLG3lOqor8itlYJh00QXLH6GWA_JY44Iks3T6sa6sivDRNM5oIpRQQZ0pytBMj9oPRXz9iGXBvPpq2FiRzENGzJuzXc9KSMvSxwxUEbP9abq61YSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
هنوز داری دنبال لینک می‌گردی؟
✅
حرفه‌ای‌ها مستقیم وارد میشن!
با ربات وینکوبت، ورود به سایت فقط چند ثانیه زمان می‌بره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡
بدون فیلتر و دردسر
⚡
بدون لینک‌های الکی
⚡
فقط یه کلیک تا ورود
🎁
اگه سریع و راحت میخوای وارد شی، این همون چیزیه که دنبالش بودی!
🤖
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال وینکوبت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/SorkhTimes/131630" target="_blank">📅 13:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131629">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚪️
سخنگوی فدراسیون فوتبال:
۱۴ باشگاه گفتند بازی‌های ما را ۳-۰ کنید!
🔺
سازمان لیگ مصمم بود لیگ برتر را برگزار کند و روز ۸ فروردین به باشگاه‌ها گفته شد که تمرینات را آغاز کنند. با این حال ۱۴ باشگاه گفتند که در لیگ برتر شرکت نمی‌کنیم و بازی‌های ما را ۳-۰ کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/SorkhTimes/131629" target="_blank">📅 13:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131628">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
قرارداد علیپور دوساله دیگه تمدید شد
❌
✍️
باشگاه پرسپولیس مبلغ قرارداد علیپور رو افزایش داد و با این بازیکن برای دوفصل دیگه به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/SorkhTimes/131628" target="_blank">📅 13:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_7n8NHU3dskj6AlN6egVw91PdzXfpoLN8WE7z2GvmtbffD4gC6ThosTVPGlBJNv3DxRO101RJSMjUkarzkJhImN-tLICd_wdSy0N9pMxFTuNf9IFWuXInMwq3XzQq9SVouxhNA1OWj1XHhMZ9abv2qhYYkR9GjqX_edobsbL_NLe6yZ_6cKLDICWFHiA5VeS7cufAub5pvVVsskJA3DtcNUUsSQEwJNVW7IfQYrVekhJPoqPd2BLOYy06b2XZXS7HGe1ysELY_0igkAKVh34PHpx1l9v9RsUi8TlbZOEnfyuseNMPUpgYp-H3_jiDOOI1vCXdo8uPnzYPJvnf_z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیغام عجیب بیرانوند به حدادی، مرا به پرسپولیس برگردانید!
🔴
به گزارش شهرآرانیوز، علیرضا بیرانوند که خودش را برای جام جهانی آماده می‌کند، نیم نگاهی هم به آینده خودش بعد از این مسابقات دارد. او از چند ماه پیش به دنبال بازگشت به پرسپولیس بوده و در شرایط فعلی که لیگ تعطیل شده است، او سعی کرده تماس‌هایی را با مسئولان باشگاه سابقش داشته باشد.
🔴
حتی با خبر شدیم که بیرو با محسن خلیلی رسما مذاکره کرده و آمادگی خود را برای بازگشت به جمع سرخپوشان مطرح کرده است.
❗️
پیمان حدادی هم در جریان این موضوع قرار گرفته و حتی به دنبال این است تا اگر پیام نیازمند قرارداد سنگشنش را پایین نیاورد، به موضوع بازگشت بیرو به طور جدی فکر کند.
✅
جالب اینکه بیرو به حدادی پیغام داده که حاضر است با نصف قرارداد فعلی پیام که ۸۰ میلیارد تومان است، دوباره سرخپوش شود در مورد این موضوع در آینده خبر‌های بیشتری خواهید شنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131627" target="_blank">📅 12:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4k6Z3OSUEvdaixISQn2_IShugT-rHpJj-ze_BX0RcpvmmpobfvCUIEu0XRSo5l4F8OhiBdnauy4ZMX-4Iw2bXTuznWmlQzcUCbpCeIuCIkX7IA73WuHHA1NiSCE0NMVVsdjFghLerjKHsAh6XhfxokVZYdqaXmpvinLHOTJOZQxiUuKZ8I0iRbMAJQxZndkMUg3pQf9vM_fvSPTEdauKDfhGI9JUSfGQk4Yqudeu-fdq4kVn5z4FSzLjPh6A4crekidJavYoggD2RFq4Ysc64RKSFPxCKARarVarCT8NIseTT76rKzItYPSzaY6swSL9mg6NNJyz0GJGevBouE9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
معین
: قرار نیست واسه تیم ملی آهنگ بخونم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/SorkhTimes/131625" target="_blank">📅 11:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKO_yKjzr39IzLHEPoWGoAD0a8ex4ZXp9BrYgTE_AL5MmwRj5rkzx-uyl0Bv6QiAFgTpucb-a31_fJsxKd4l2Tr-RuLrHmluFsRpE0bo4XSMPSovlGBE-vJ4x177PLSccMpEdBqpYj4xS21LJ9j8Ag9i2mmmypPmoPy_qPBlq1WCMUdFsXiuJHNmE276t9MuA42pFKasxG5ZwsFJdoW8HBf-Y2QhYN2Mj_QjqvRg7OckpBT4-u6D6CTMmzx6RO2c3vbttFjqOdU10Xfm4d5eDP5x8d5l9YiOphsNTyxIPsHoOQ6hysg7bzIUd59pm7FHeHggHSYplQj5ma7ecOhwdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اینکه مدیران پرسپولیس بتوانند از لحاظ مبلغ قرارداد میلاد محمدی را راضی نگه دارند وی به مدت دو فصل دیگر با پرسپولیس تمدید خواهد کرد و درغیر اینصورت به لیگ ترکیه یا لیگ یونان سفر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/SorkhTimes/131624" target="_blank">📅 11:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnlqirV6Cjeo3Pwa-FUyxdCCYz93sR2nuiphNbvCDEP_6c76ROlOQip4izoz--Hek8U0qW6NKwTt9NC8Z_Q1jR8eWMD2apGT489Ipain6AQHkgWBQHfyDCmTr_c8gmlHA5t1QqLAS6fnJhPGb9taJp5Dvz9XwElk4H1cb0KerfhaiJ8LwjwhZlG5lHQA2RIdNUT8Qxm8BDVuuokpeITRMRbv3URPUvdFlTpMUyzZTGAmB1oljdLRnQ9eTREFKdiRPD-_g2ucISAhDpY5F1DkErNmB45Av3A6xm6iD_nOSzAz13bxtduF6iTuFqA0jQYzpvc3w_MOdxMZhFtlQM1Glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تسنیم: قرارداد باکیچ به طور خودکار تمدید میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/SorkhTimes/131623" target="_blank">📅 11:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro95mVS9OAzGP4FZtxvJPZd2P9Vyi2lKA0dJ03wikLzWf4A_UANU4ckWRasH81INb-SI3bMd-0aUQL-hf7KsTrZpAo59dXqOBoGaWG6-Ekcuxe5ko6eAN8upMfkDGO2J0lrNUbd3bxTLHoaxSgOOgTIKjZ5xXa1eCqQ01QvAbUtbBQQy3Facf_E9xg3ZOBvS3gpEPfzC2IFaOW1nun36luJGP1SolrrR8mBcGTBIY5FVjCz1HjuVt3aYoHN1gBO6XMEJSNS0d6V_cjW2P8jdTaicSZoGBmacNyGYtOzGGzEfgNvzAmK00sSYZwhes4ImPXKPVrJtCg3oMSsRHjVqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/SorkhTimes/131622" target="_blank">📅 02:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYfz7c3fThcuvs8t6-d4iAQ4g9zKvNOcuEi3OSHYiVsPXqRB4KaodrNOwIUTI7wybtold8riEEVep9JIeOSq7KkSo8yK18eCMeqEHIQ4RYHalL61FX_96G1LJVK2_JE6fAQozwUS0GaNde9HBVn83yH6k97AKRLy94X3iJCjUlMQiWgzfpL6qa5-73yUjzGhfT-XHfqifRUUQW7GhctET_6aVXDY3MzTISUSGWoofHBGn_5no-BWtNApDM1r59jnMqE_E3LDuSjuDrkueLBB6imK8yugCsqXMVtWkeh342pFLUHwBPOtpMf_7miJ7oSqjiijR8bdsdUSvcIuJWY_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مهدی تاج: شنیده ایم معین برای تیم ملی تو جام جهانی قراره موزیک بخونه، ما دخالتی در این موزیک نداشتیم ولی ازش حمایت می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131618" target="_blank">📅 23:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE5oRlPjuQ9NkCctcFbgEHhrJxLDtnKhenGXwx0gV3JWN93gIUMDIstpYBSjJY3lT2USPm1T4JCNYl_Dwh4Dzl1n_UUFvPKyrKpXH2CZ6CJFkKqZ7FvdCYD0QNicofzIROKbK7Ij20WuOd3kcEtvFTgn1bay43mmfCNGMzKcuFsKWRiroNrBcUJL8hHLN9kRHuj2GF-X9q6Bgvb6RZabyob44xUDT7VWjah0h0e9Dl1BlL1ZNIIbPRSeI7L0TVJeQPwVlsfHQb6iWGpZ85tZVKxQHvjvMFDh4FfHz8oRPpd5ZZP1TRzUN9_21R-UBS_BRKmzFSqSEOmV9GRqWoTtAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
از کیت جدید تیم ملی جام جهانی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/SorkhTimes/131617" target="_blank">📅 22:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏺
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/SorkhTimes/131616" target="_blank">📅 21:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjvpJiCXY6svXs8xj8bc-AHRyxswVYjOVqJpZOzbqo2_QoDnYc3Vdif9OB73RZ4ZGp2BQQWWPQuHtjMa01pE6dYwT5ztFaxiXQlcRhma4uJCVBTsedycouM6Ftf2OykEwd6Aw1qychPnxWQh0yk0TZVMA36aq6b29I1y7C2yLkDW_rIHOeo4o0x20kB8BwewGCHiD3GRpcUffAKbwNpIkZyJXOzA6Cb688eoz3r07zW6abERATPKK4ylWCuMwEvHmyud9TwioVgyUJnomlMCrraGoypqUQoztXx1N3plNSV41u_Bf5PIXCD_Z1uBUgcN6V7O2mTFSB6C8_zS0D1iVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 978 · <a href="https://t.me/SorkhTimes/131615" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131613">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcXDBmlzuNAi9YBFbLsdFpsJpr3jHIEyPcGJEkL3v9J0RB6IufR3iE8e3hromgaIhkAQRq8JG5zzaA4QyfsMmcnlt7Okvll4h3o_MmMNd3a84mRto5y3IwUy-0mC0t76Qd7gjz-IZfQ3z6Zb8g49MnK72ZcK5j3sV4VfoMx6-hBZ4ZlOL1KYbT5cLRTlNzu1MYonxXn9rY8l03BqBPRI4R3W0hX2V-QyiC--EMUYGb1C5MXFE536VnyIDRf2nmnESJjV3JRRdx4kdZkdybtKVc0C5KjsPXhprSKyHK3Hz8nA9s_6i0CtsSJVFt4QLmFRlnaWFGPptgbYM5Y4SIB1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنای تیم میلی کنار پزشکیان عکس یادگاری گرفتن و راهی جام جهانی شدن!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/SorkhTimes/131613" target="_blank">📅 21:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
معاون اداری و پشتیبانی وزارت ورزش و جوانان اعلام کرد که برای حضور قدرتمندانه تیم ملی در جام جهانی ۲۰۲۶، مبلغ ۴۰۰ میلیارد تومان بودجه در نظر گرفته شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/SorkhTimes/131612" target="_blank">📅 20:45 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
