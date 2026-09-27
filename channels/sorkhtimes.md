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
<img src="https://cdn4.telesco.pe/file/mpizN3Id1xxYauX668NMja-wCPRhcvWgciZCnr9TQNNCd5HjfNM3bNQah0oZW7FsJRq5PFMM8CAWViYX9ZiwDP-wd8LtJOoPGKpivlJcOabnlnA4ZXI7HzCmEOeiKKEgZn7fcILsJgTVbZK6e17n-SwRT6A8NCIyEPYqo5Lnm_gfWxbIs_lLCxBoWmmTyvbpX7O5bLdXK3cmkOvRMSUd7iGD-4p_z8rlzj236Zis2od4IKR9UP_2TrKkbeb8yZpj1W2eWDenmOm0xq_lQHZ3HfPIOG9rMI4r3Av0m3yVZogt6Uij2vM0G163gpeF8L6cRAYR8JRcL3QDyv4SJR26jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
<hr>

<div class="tg-post" id="msg-140618">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
هفت ورزشی؛  به استقلال خیانت شد؛ برگ برنده پرونده آسانی به دست پرسپولیس رسید!
🖍
ایجنتی که به باشگاه استقلال رفت و آمد دارد، مدرکی به دست باشگاه پرسپولیس رسانده که برگ برنده این باشگاه در ماجرای شکایت از یاسر آسانی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/SorkhTimes/140618" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140617">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhD1_R376Dmamo2VBkeuwT31Ek2suR1YkpOalFvvCIk_ipcf5vKo185s28n4MU2N5eoZBsyEL29obY5ItIp32FDWs-w0vNn_x3_J0WsV5nGFGYMVBT-QHI6UsTt1WqkZLKLIlmwEWHDP9Z-uUUseXAB0CHS8qdFNYDPmRTxQsKSFUiR-0-2_mRXx4hBHc8mTuDpVKPMscCB1K_ppS7Gc-TNLbcrO1tbdYrlBsTSa8P3O7x_YP5L_Z2JscbGvnCjeNHMeXtQIodxqFuPPzM0vHIXNUdlZAjZwI3eqjPABKLMQ8p7CNqLW-K0Pq-E6lFEVqZIMyP-bh9Z42EI5PfARYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد ستاره‌ها؛ شبی برای تماشای فوتبال در بالاترین سطح
⚡️
[
نروژ
🇳🇴
🆚
🇵🇹
پرتغال
]
⚽️
نروژ با تکیه بر قدرت هجومی و انتقال‌های سریع، می‌تواند بازی را به دوئلی فیزیکی و پرموقعیت تبدیل کند. پرتغال با مالکیت بیشتر و کیفیت بالاتر در یک‌سوم هجومی، به‌دنبال کنترل ریتم و استفاده از فضاهای پشت خط دفاع خواهد بود.
سناریوی محتمل: گلزنی هردو تیم بسیار بالا می‌باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/140617" target="_blank">📅 20:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140616">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
⭕️
⭕️
دنیل گرا مدافع راست خارجی پرسپولیس به تهران بازگشته و اماده حضور در تمرینات گروهیه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SorkhTimes/140616" target="_blank">📅 19:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140615">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
بالاخره انتظارها به سر رسید و دنیل گرا پس از پایان مصدومیت، طی یک یا دو روز آینده به تمرینات گروهی تیم پرسپولیس اضافه خواهد شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/140615" target="_blank">📅 18:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140614">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
زنوزی علیه کیسه
❌
زنوزی: کیسه خیلی جام دوس داره بیان من پولش رو بدم  برن منیریه برای خودشون جام بخرن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/140614" target="_blank">📅 18:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140613">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
⭕️
فارس: آرای هیأت رئیسه فدراسیون به قهرمانی استقلال ۷ رأی مخالف و ۴ رأی موافق داشته و به این ترتیب احتمالأ جام به این تیم اهدا نمیشه :)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/140613" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140612">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/140612" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SorkhTimes/140611" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140610">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/140610" target="_blank">📅 18:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9ahKaKl_doAjF9SuN3z_ReVp1-DUH2IpGHQiThy2MWbW6HI9JIEb1GNctTp_JpxDQTL8rSZf_zcoxhObJc5I5C4US60ZacyCqfthn9W6Rp3Vm5iUtfzOQl59oywSMjcKrrIh8xUr71O8X8bhuSNVvZuGxHwAHhbS9Xb2lbHsJr6XwCHSQAkfCVZ9hQxL9xYDvtOUIOjoUOjrbZdYt0YdeT75PLiQLBpNG0rU0u90WP0Y2g7a1X8n_so3GKmsNltBbURUC5WU8fby76F-qOTtP165maFWf_33ygtktLIMRnZbrr4BK7JLwrZnFEvq2f2qTN5Hci-NCiO_fDB43PnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/140609" target="_blank">📅 16:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140608">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند سربازه و معافیت نخورده و هر بازی که انجام بده غیر مجاز هستش / مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/140608" target="_blank">📅 16:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140607">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpncEHhi1g9kMWZd_kTFO-Y_rcvJmscfo2Aw6e6uw-GWHDFUq7NLqO39E2hfV_cPqB1-B-wV2WrqZsy2UOR_QpP6vnkHrbzcBhcTsi_gVXXZt6zuJQspQi5l4KqEIi9J6Jl9FBtoyuXdL9OdP_FY8aMwaD6ypVmIFuN8qlOPH1vZgUlOLN_tB53c4BwZQmj0xkcEultFlIarK_BWZsMT0f-fnXXYXYqlZA_VXRBwgP5kBuBG04Gq8F8BUHEUxBhWbEy2aX406Pj-6mIHc3i_Jou3T8elG4mlm_RKEfcmEazZOfsOsrfmmkthi4tHn0OCsYJh0wZJv7UQcm2tEPZ1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Norway -
🇵🇹
Portugal
⏰
Tonight 22:15
🏟
Ullevaal Stadion
🇪🇺
نبردی بین فوتبال مستقیم و مالکیت هوشمند؛ جایی که هر اشتباه می‌تواند معادله بازی را عوض کند. پرتغال با تکنیک و کیفیت در یک‌سوم هجومی خطرناک‌تر است، اما نروژ روی انتقال سریع و قدرت خط حمله می‌تواند ضربه بزند. انتظار می‌رود بازی با ریتم بالا دنبال شود و جزئیات در محوطه جریمه، تعیین‌کننده برنده باشد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/140607" target="_blank">📅 16:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند را به مدت یک ماه تا پایان مهر برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان می تواند  در بازی هفته هشتم با استقلال تیمش را  همراهی کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/140606" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/140605" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/140604" target="_blank">📅 15:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140603">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
❌
فووووووووری از ورزش سه
🚨
اولین خرید پرسپولیس در نیم فصل مهدی حسینی مدافع‌ وسط ۱۹ ساله شمس آذر خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/140603" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/140602" target="_blank">📅 15:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
طبق شنیده ها
❌
ابوالفضل جلالی مجدد دچار مصدومیت شده و بزودی مدت زمان دوری او از میادین مشخص خواهد شد
😰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/140601" target="_blank">📅 11:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚡️
⚡️
⚡️
رضا شکاری مجوز بازی نداره و صرفاً در لیست بازی قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/140600" target="_blank">📅 11:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
امسال جام حذفی برگزار نمیشه و تیم های اول تا چهارم سهمیه آسیا خواهند گرفت!///فوتبالی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140599" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚡️
⚡️
⚡️
رهایی کاپیتان سابق پرسپولیس از بیماری سرطان
⚡️
⚡️
سید محمد پنجعلی کاپیتان سال‌های دور پرسپولیس، مدتی را به دلیل درگیری با بیماری سرطان زیر نظر پزشکان بود.
⚡️
⚡️
خوشبختانه شماره ۵ پیشین سرخپوشان موفق به شکست بیماری سرطان شده است
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140598" target="_blank">📅 09:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">😰
محمد احمدزاده، سرمربی اسبق ملوان: یه مقام استقلال‌ به من زنگ زد و رشوه ۵۰ میلیونی به من دادن که به استقلال امتیاز بدم تا پرسپولیس قهرمان نشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140597" target="_blank">📅 09:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
✅
مذاکرات پرسپولیس با بشار رسن در حد واسطه‌ها در جریان بوده و هنوز به مرحله مستقیم نرسیده است. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/140596" target="_blank">📅 09:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140595" target="_blank">📅 09:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OczkbP2Mi3N9Fa_WVM2G2UPkBtN8mDU6VUege7jBarDU6WdjNGKnT_B69mEgJnR39kOIk1r1YkIwM7WXZxChMopZKLpaDNBfCykJdYrrxwJs-yWZvOtJ2L5BvjNtGBNGu3f7LWWUMpihWZAwDYmpMjERvgpbj9arWTSMbTCcgvPE_9TNrqqjBmRmQEIO0K90L4wfCTCsbUsC6HT_UgnYfer7dF5GJDWCgHiiAY8nyLW64VfmrH0upLiVqyCCUDCA28h8uBOeX0-lbTpTu20eBKXn0WMUVzUmNNtmJD6499ggt-hkFHaqnjXf8b0v-mV2Z9TiXQ9mhewcCu8tKhdF8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140594" target="_blank">📅 09:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItZr1W2Ya1RHeuH3eYpIHZGzT5d5ejpwPXU9hKog4uHp9ktGreWKWGXBY3GUFgkFZc2nXlgInz7sYYzGaKtDcsuvIkpABqe_Q1jWqOh1Pk56eufQ4-pkDRwbSAfsoDDNA1K5wdWsKeX5uaW4npZoUDR3aws3Arovt3W0B7tWDTj-W6pW0Mste1E5gJ606FdIrtIoxf9w7IZqkYVwMej75icS4kEh5CR2JIFHgHoVyrWzzhC-le6w2amp5CmIBaWqSzrn_e7p2A3AruGcPS9SoB5274ptDrll7pu4Ie-fUP7MRRMfPNVvR7Z5doIJZrGcciKnpBwzctkOVj9h-0ZgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
فرداشب لیگ ملت‌های اروپا پرهیجان دنبال خواهد شد؛ بازی‌هایی که روی کاغذ ساده‌ان، اما داخل زمین قطعا داستان فرق می‌کنه
🔥
⚡️
⚽️
فرداشب چند تقابل نزدیک و پرریسک روی میز داریم؛ از برتری‌های نسبتاً مشخص آلمان و اتریش تا نبرد کاملاً متعادل نروژ و پرتغال. در بازی‌های ساعت ۱۹:۳۰، هلند و دانمارک دست بالاتری دارند، اما صربستان و ولز می‌توانند معادلات را تغییر دهند. در ادامه، آلمان مقابل یونان و اتریش مقابل کوزوو از نظر اعداد شرایط بهتری دارند، در حالی‌که ایرلند با اسرائیل و نروژ با پرتغال نزدیک‌ترین دوئل‌های شب هستند. یک شب شلوغ با چند بازی که اختلاف روی کاغذ، لزوماً تضمین‌کننده نتیجه در زمین نیست.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140593" target="_blank">📅 02:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140592" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭕️
⭕️
قرار شده جام قهرمانی در ازای بدهی ۷۰۰ هزار دلاری فدراسیون به هلدینگ، به استقلال تحویل داده بشه!
✔️
✔️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140591" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140590" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140589" target="_blank">📅 23:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140588" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
🔴
فارس:
⬇
بودجه پرسپولیس در فصل جاری ۳ هزار میلیارده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140587" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140586" target="_blank">📅 22:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
#فوری | ترامپ در سازمان ملل:
🔻
با تصمیمی بزرگ در مورد ایران روبه‌رو هستم؛ توافق یا نابودی کامل
‼️
🔻
آیا به توافقی دست یابیم که به این کشور اجازه دهد به ملتی بسیار بزرگ‌تر تبدیل شود، یا اینکه آن را به‌طور کامل نابود کنم
⁉️
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140585" target="_blank">📅 21:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140584" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRyEZ28qcjsbjLEq_L3inC0-zU-CRvakbiC_hIHQ_TdAuDfRYdMrcp_XFGVFLoC66fKr-odpROyBV7CS0oXFFP0xfjmAEDKxrTowAcbMKOMRV1rKvFP2seCVx6_yfSZWo9itCvnq5Y_xn-t1xmMW1kDc8gX-pzXzpW3fxFZsDeE2U9TY8yGq3SPGqFN7Iyaw6SlUvwuTywqiHYw7a0hCAWAzsBESb9zHjHf3JzmkNJBeHrQkijMg0FNRJHgcGyEAFr-g1a_J3LkEVViKZXTqeLvB4eKra5yIRGYjcEC4QuFuZCCHjuFPtmIIQZtOB6Dx--GN0MqvRhcyjwqGXTzkAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
❌
افشاگری فنونی‌زاده از قلعه‌نوعی‌‌:
‼️
من با سند‌ و مدرک به شما می‌گویم ۱۷ تا مربی در عرصه‌های مختلف ملی و باشگاهی که سابقه استقلالی دارند، توسط قلعه‌نویی به‌صورت مستقیم یا غیرمستقیم روی نیمکت تیم‌های مختلف ملی و باشگاهی نشسته‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140583" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
با دعوت احسان حاج‌صفی به اردوی تیم ملی این بازیکن در صورتی که مقابل ازبکستان و روسیه حتی یک دقیقه بازی کنه رکورددار بازی با پیراهن ایران خواهد بود و از علی دایی و جواد نکونام عبور خواهد کرد
✔️
جواد نکونام ـ 149 بازی ملی
✔️
علی دایی - 148 بازی ملی
✔️
احسان…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140582" target="_blank">📅 21:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140581" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuFRMouVy2tnmXYb-kQtzDAC88diMAn-3R2oMrK29WzfkDixYqXy6nKpV_GcB-iok-B6TC7ltdD4jZL8dlYgNAiXRQKfUvSZjvjQUiMutC55IaOdmQhWJ5EVlwKk6ux0k6isar1YOjoogw1nTlKy94ky3ZVf-tlu_LfUNQKVFBiWbZeVJl__wWcKdLOSM5xB4B7gPGdPrjOhJEXUyy2o-TJ64sAgxw3-fIensZNgAWTTeHn-PC2My7ioscI62BcPWU6X0AXhfwDUXeHHt8RH9APlTWT-cQkUl5NnOD0si1PQEb1bg-ah54QwZ1FKWEEAjkg6By6c4sjJ_K-Uk1S-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
England -
🇪🇸
Spain
⏰
Tonight 22:15
🏟
Wembley
🇪🇺
اسپانیا با ثبات بیشتر در کنترل بازی و خط میانی منسجم‌تر وارد ومبلی می‌شود؛ در مقابل، انگلیس روی سرعت انتقال و کیفیت ساکا، بلینگام و کین حساب می‌کند. غیبت رایس، پالمر و چند مهره دیگر می‌تواند تعادل انگلیس را تحت‌تأثیر قرار دهد، در حالی که اسپانیا با هسته اصلی قهرمان جهان و اروپا حفظ شده است. از نظر فرم، اسپانیا در ۵ بازی اخیر ۵ برد داشته و انگلیس ۴ برد و یک شکست ثبت کرده؛ بنابراین انتظار یک بازی نزدیک با موقعیت‌های دو طرف منطقی است.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140580" target="_blank">📅 20:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140579" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
🎤
بخش اول صحبت های حامد کاویانپور مدیرفنی آکادمی پرسپولیس بعد از دیدار با امید سایپا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140578" target="_blank">📅 19:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭕️
قسمت جالب سربازی بیرانوند اینه که همین آقا دو ماه پیش علیه علی دایی استوری گذاشته بود: «من هیچ‌وقت از رانت استفاده نکردم»
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140577" target="_blank">📅 19:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140576" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140575">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140575" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140574" target="_blank">📅 17:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
اوستون اورونوف و مارکو باکیچ هم اکنون در ترکیه حضور دارند و اگه مشکل پروازشون حل شه تا شب به تهران میرسند    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140573" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpaMT5gnMul91ZDuRl-T99kRcbtqgHag99cGYv-lZf6MaHiKVDpXTIzH6_vMEHoxljNpM1uiQj5nzYRWql9bo1Z9kIq4pWRdvpB_aK62v2H5PGW0dnrVUGrZfUqFdOMlVLvW5mX5hBv4woK70BdOSuaGgMSPl9Mozhea3kOvUKXTV4XyoqxVgQ1Q95lkY9RaDWNh8WBEYCP4UqZ1vOp9BvHq3PAwdfVRaqa96W5XPbB3XLzNUevJXMpaDwWr8VYMYnWiPom4vaO7Rq49AhCwqcobNoplZOwsiSMbsDQfQg11HHqwSqS0OkCHiWLY0_OwSIybwp3ok6ZZzI6sDuedXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140572" target="_blank">📅 16:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🔴
فوری؛ معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140571" target="_blank">📅 16:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140570">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKdBl45_BZ_bxpXOIEiwfJ4u7qMl79MdVCYy0wgnCPk8ZCycJinxtBlHHjRpLGZfIlNtZC8jQo2q04s2R2yBxnsZd80eIIl9tNH4Zc7GWmSP4a634ay5RK23MwqI7VOjThRiAVrErUdoZyEXjpszzo4Ot6ZVK5hz98IzBqwYU0rqC1zru2EgzKitH7T0eBX5iuBIsJJ9lwmYOkobOjuhLB-NitBOrtcpqf4LGzv22-3xjv43IC6Axi3n7RM9m0FGtW7r4v_zbC03B4DFHDGBeMOGNK0d9XGWQeUao10zVUDeQKRvt_76G07vWY1oV0rIyQLTodzC1EXZTdU1zlKqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از بدنسازی امروز پرسپولیس؛ شاگردان تارتار فردا استراحت خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140570" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=aT06W7A5E2Nps1fmJkg9ir7857TLRKK_njQ-_CwDyVLghD1GNoWIhpt98bbOSeeDkHFxNbBl371kteRemvJX1YRpDTir5bVLc-JIeJHGDXkGgSFhfqfR4xX74LOjwkqtQrlaRahKi5Fscwbq1tOwkQWFtP8y6uiP_UPPMU2hkGeOv4t8tbpngWwHgljhWalfUB7yyuUnTWh8M79tiLzvto2K2maCDTkawyVGo_4pJmr-iUEcf1dywaYZtN4oOkmmE0iP6scsy0vehoe6CrPFbuBsK91kv4NRC03lVN9NNKuphJgBRfZwIaEIvGKv354-CyjsDlmDLHWhe3goKKnI1DGyjYJthRWkVC_o7XdKVnPDYsMD9aIMtxRncHvkJZQlE5axlWX8qRJ_7CkEzDPfUK_aqnL1_c-PDcWN_zwmw21BxOJ-alsSSv1WZEn9r-1O0-ji_Qx6KJHUdKbDm9MDgAA9ldKQuOkl3dXGyGWjgQzsal_9qVFnR-Xfs63q-e-sFPlv-qkW-imTj82NbPILew2h0PoTJwSArrPHyh3xv86KFqUrl3BJKPo7ubs4yigO5J2dMT6FQ69XSNSUey9lqh-w5P--b4QE-1Qnckt7W8mBgZyjDQ55N-NLVSLSpOmPkgSxVmsCrb14hCA1YAAgo2i41BbpTnWU7lEOXNIR7_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=aT06W7A5E2Nps1fmJkg9ir7857TLRKK_njQ-_CwDyVLghD1GNoWIhpt98bbOSeeDkHFxNbBl371kteRemvJX1YRpDTir5bVLc-JIeJHGDXkGgSFhfqfR4xX74LOjwkqtQrlaRahKi5Fscwbq1tOwkQWFtP8y6uiP_UPPMU2hkGeOv4t8tbpngWwHgljhWalfUB7yyuUnTWh8M79tiLzvto2K2maCDTkawyVGo_4pJmr-iUEcf1dywaYZtN4oOkmmE0iP6scsy0vehoe6CrPFbuBsK91kv4NRC03lVN9NNKuphJgBRfZwIaEIvGKv354-CyjsDlmDLHWhe3goKKnI1DGyjYJthRWkVC_o7XdKVnPDYsMD9aIMtxRncHvkJZQlE5axlWX8qRJ_7CkEzDPfUK_aqnL1_c-PDcWN_zwmw21BxOJ-alsSSv1WZEn9r-1O0-ji_Qx6KJHUdKbDm9MDgAA9ldKQuOkl3dXGyGWjgQzsal_9qVFnR-Xfs63q-e-sFPlv-qkW-imTj82NbPILew2h0PoTJwSArrPHyh3xv86KFqUrl3BJKPo7ubs4yigO5J2dMT6FQ69XSNSUey9lqh-w5P--b4QE-1Qnckt7W8mBgZyjDQ55N-NLVSLSpOmPkgSxVmsCrb14hCA1YAAgo2i41BbpTnWU7lEOXNIR7_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140569" target="_blank">📅 16:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🔴
فوری؛
معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140568" target="_blank">📅 15:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=o9Ze3n939eXnKvh_okr6ivkoUrmsAftMvUpY_NEu4LirMUaByJNq4DCZ9OqbxOSnldr6W4P6VgrXr3qE7ZJTYVUhvJddidBysoPj5gW1IEpvwSoNEghbi8puPWdWBeqWftgqR8giASn1dUhB3G9Nq81v2NBsDFAAARcIe75wWKC9AuWscNahaUBEHy7ulOkV3iOjZyXxR5vUq0C3LfraAtFi3G0uk9K9Nv5R8zhpQRJvHWzpeduGsU9BGxsePSjooQeDOeYdztNKYiwdymclvF5JIp9w-VcQwHJ_vRIIoXhB8E26aRLeLAAVrJcEaDmbtPj62FA7sd7jfGgLtG0lbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=o9Ze3n939eXnKvh_okr6ivkoUrmsAftMvUpY_NEu4LirMUaByJNq4DCZ9OqbxOSnldr6W4P6VgrXr3qE7ZJTYVUhvJddidBysoPj5gW1IEpvwSoNEghbi8puPWdWBeqWftgqR8giASn1dUhB3G9Nq81v2NBsDFAAARcIe75wWKC9AuWscNahaUBEHy7ulOkV3iOjZyXxR5vUq0C3LfraAtFi3G0uk9K9Nv5R8zhpQRJvHWzpeduGsU9BGxsePSjooQeDOeYdztNKYiwdymclvF5JIp9w-VcQwHJ_vRIIoXhB8E26aRLeLAAVrJcEaDmbtPj62FA7sd7jfGgLtG0lbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور پیمان حدادی مدیرعامل پرسپولیس در ورزشگاه درفشی‌فر برای تماشای دیدار امیدهای پرسپولیس و سایپا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140567" target="_blank">📅 15:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140560">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYXiYnE-2M3ZR8inUTUpHs3i0TKzW8qRAtJodGPe0VB90na_yrXev0hfX9vzO3awzytUmXJ7KnB_6xk1jqaMReB7iK9qDdLJgWhZyDajThVHHZ8a3O74HpM5wmN1QJwEv1dNKGuRkBhfnlRjnxxf8LkC7WfZ4fVEJYnrrmYLcpgm_Swqsr-QZos_10dxYTftsdh-O_0c3_52lDjU1WiWYOmHAkWiXQgpo5kSBuvTyet_3aiKJNpXm4vambYZlI1Z_lQPCZSX3PDfrf-rXtSnpqw_G_rcjR5uYb7X6SYHAANrHWBVI0ZnryiapFvs1MvhXtcXQgpgmavcFsPul0cQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد بزرگ در اوج هیجان؛ اسپانیا و انگلیس برای یک شب تماشایی
⚡️
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇪🇸
اسپانیا
]
⚽️
اسپانیا با میانگین مالکیت ۶۴٪ و حدود ۱۹ شوت در هر بازی، از نظر کنترل و خلق موقعیت دست بالاتر را دارد؛ انگلیس هم میانگین ۱۳.۵ شوت و ۲.۵۶ گل زده در هر بازی ثبت کرده است. با توجه به فرم هجومی دو تیم، انتظار بازی با موقعیت‌های متعدد می‌رود؛ در عین حال هر دو خط دفاعی در هفته‌های اخیر آمار گل‌خورده پایینی داشته‌اند. تقابل در ومبلی و شروع لیگ ملت‌ها، این مسابقه را به نبردی نزدیک و تاکتیکی تبدیل می‌کند؛ جایی که جزئیات می‌تواند تعیین‌کننده باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140560" target="_blank">📅 14:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140559">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stamNnkmlAmaMXbINFBHzu8dqzg9HpjbTUeHJe-NtvUNsqjDgSoXB0STmIbxMuMoL1491pf3i2LpqTYE7VRSpjNV2IexBNH3nb_jwma886KSoHLBx_euAOLtRb5SEVh6PzUY6eXvPqM_mC-QkMN6rIK3EqGu6VTT9tQLxaXSO7h20QhxRGWiy0GxLTIhFNt4v_NjS9T7dWqw2uaZ1dRopWgxff2V3kH-sd6jtOqdAzOMDD9nXxVVWk38IpDJGLVff46ssA6i4MrS02Ne0HXn2h56_ZcynQGwHJWChe01XSyTRXoc1L_Nu0_XTTTu0iZSROjCcIYJ_ipnzEVurBvSUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم قلعه‌نویی واقعا عجیبه!
❌
بازیکنی که از جام جهانی خط میزنه رو کاپیتان میکنه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140559" target="_blank">📅 14:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140558">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⚡️
⚡️
تاج اعلام کرد امسال دیگه سقف بودجه وجود نداره، اما فیرپلی مالی اجرا می‌شه.
⚖️
طبق این قانون، باشگاه‌ها باید قرارداد بازیکنا و هزینه‌هاشون رو منتشر کنن و اگه این کار رو نکنن، سازمان لیگ خودش منتشرشون می‌کنه. همچنین باشگاه‌های زیان‌ده فصل بعد با محدودیت…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140558" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140557">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
فوتبالی:
✔️
✔️
گفته می‌شود فدراسیون برای جانشینی عبدی با گزینه‌هایی مثل فرهاد مجیدی و مجتبی حسینی وارد مذاکره شده و باید دید در نهایت چه کسی هدایت تیم امید را برعهده می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140557" target="_blank">📅 13:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140556">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
در صورت تشکیل تیم (ب) پرسپولیس، گزینه‌های سرمربیگری:
⏺
محمد نصرتی
⏺
اسماعیل حلالی
⏺
محسن بنگر
⏺
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140556" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140555" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140554" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEyzSMS6n0QE8EvhHVJ76HrBINan0O4Bui0BcMRDB4GmeYBUB023sa4wH53HVAAfVNvkrJYvY9WjYkbiJc0arwz-uZhYcc-h43Msi29YcLOLWrhqAaYhD8apBZcQrnk_2Y-Yjnw_6ZOHOjZ93Y7OsixbnU2fac7J14jMQnbgzqZ7WT9uqZ7tOJbxv8J7xGK7PBr3pjW32d-n-H8-l9olsIGPPMPGutlyT8ZyMuCIQ-Cdx19tGyjcYGmlhJ_xU5rs1mKLRUnMU52DA2XmBb1GGH4Q1y-MlDyWmn1zZeP0QEqCZ6nsSb7urIiP_CYAJnIYoK9dd_Lm7Cm_d7vXyc5kIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
باشگاه استقلال در پرونده فابیو کاریله که فقط اومد یه سلام کرد و رفت به پرداخت ۴۰۰ هزار دلار محکوم شده است.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140553" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
❌
سه وکیل خارجی باشگاه بعد از دیدن مدارک جدید در پرونده آسانی اعلام کردن، درصد پیروزی پرسپولیس تو پرونده زیاده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140552" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tozaB7suZE4jHGzoVXNOm-74uyYH8JMcZdnM5gLtSKJQ3tsz0U91wK9RxiMAQU2ZOqkhHp1iACJInpDw83cyGGKKYhjSIqIswMGrWN6hDO1PjgPFmsPV27wsbDlwjY14Viw8RLpTDmDXGNbI2sQ9PpTKjTeT2m319GBekAf_-866C19zFKw1n8onluS4gMxP4hN5V9z9DcP7t63eu-xqU4y6yOlCvaedKyjFIXaGm_CPA4yeuVSf9VSykaAQyrYYceWfdzRbMxEGh5cy8eUJXGwK9oJx44MysalRmUT_ZfGd-U5AkVPxo1A8AwjWe2I1LmiLfZZ9WAAu04dMF9YjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140551" target="_blank">📅 09:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITq-SU3coPD3GaPiyPAmcZrmQpZuwj-cPSYvMQndINCbk53qfbB6wHMBl0290mwjzR2LPScwN183pujNmakETth7J-5vgk1S9jx-Ucjjn9yoDm38zXcu0GfQVLF1WWgDRDmT7MvXwDcSAgF0rEOW0tSplWGgO1e0pHc8mXQ8gV5090e12bXmVAkOuZanXUH2ltMrAw4AdDi6zqqRL2PVYJkQL-oVXbI1S9cCbX0DFL_h8AD87CHm3eC4agR5lXy2XkN68ws_msIR0JhasKFTnIb5YKVtLzKX-xHxrFIELzPkzlD9kZgACgOx77lyPu4OGwIHuej83cIJ2zDHOYBLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
شبِ حساس لیگ ملت‌های اروپا
🔥
⚽️
فرداشب چند تقابل جذاب در برنامه است؛ از جدال نزدیک اسلوونی و اسکاتلند تا رویارویی مدعیانه چک و کرواسی. آلبانی با توجه به ضرایب، شرایط بهتری مقابل بلاروس دارد و سوئیس هم برابر مقدونیه شمالی دست بالا را دارد. اما حساس‌ترین بازی شب، انگلیس و اسپانیاست؛ دیداری که می‌تواند از نظر فنی و نتیجه، متفاوت‌ترین مسابقه این کنداکتور باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140550" target="_blank">📅 01:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdVxQ2PWgbS5AFd9T6VA1VxShm7F-m2_BxYXcH3mrGd9qLgOUYv2j2QXADuodf-xmd9nvp8dajbQung-fcRuIrm-tHzlRF-oLeh5OzSf4vq3zwPQ7LENUK7WcRGV5YO4fjLboL4fblXSWSo2iKhGN29CmSsn_OPY4HnevDuiSZkxa_TsXES9W6h6RQQXuajqRCyq4QTCAZr4PLNJq_8N2EUiWAekXJxPCgorr2W-fXN-yUNjI6maOcvouGdkFNPOzFqYJqpRwdcwgyzDycLW0MDPg-MO8uxvkqtQJu98OT0mMLZ6bBkDUaKhCLsdrTxvVu_AcBClRt59wUuDi6qntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اعتماد ویژه تارتار به جوانان آکادمی
🔻
مهدی تارتار در دیدار تدارکاتی امروز مقابل چادرملو نشان داد که برای بازیکنان جوان و محصولات آکادمی پرسپولیس اهمیت ویژه‌ای قائل است
🔴
در این مسابقه، ۷ بازیکن جوان آکادمی فرصت حضور در ترکیب را پیدا کردند تا خود را در سطح تیم بزرگسالان محک بزنند
🔴
این فرصت می‌تواند سکوی پرتابی برای جوانان پرسپولیس باشد؛ حالا نوبت آنهاست که با ارائه بهترین عملکرد، اعتماد کادرفنی را پاسخ دهند و مسیر خود را برای حضور بیشتر در تیم اصلی هموار کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140549" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zijoz4MQtVrnAt5wBSk4_Zznoh9QwgwjtXhhlDCf_5yxBBzxv-L4VGdR7D_oiBC3EuZKXxexN1F2p4H5TDtGRx9JVvn8g4-DDIuM0y1IjnL-26OdqKQjIvEmmGqImEcnBZ3gAmySqtULS2rDWE11f_0L02-kh8y6k1Afj8wAqF0o0d5m_9_F4GmdjIUTfGTs5CCic8PRpkDYT_Lq5IKwg3B8m5PQzaK5vcraGDhL4ymcv6oD2FyA3KRAMVMMTUVP4HiVx1SiBnvFYDOkLCBBE-cSqcxXf9_c7_vMoSc2FxRRANTuA_i1iMc6ASGSWkIynumN4R8j3QFPLKDVpyImAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نتایج هفته دوم لیگ برتر بانوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140548" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140547" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aihg9lKfeV6BCpqC1x8rXzAskdrPIucE4yhQjnREHZDJKFEdSMe5ZJtNeXlGuWiaI8l-5bCb2xVOXNEe9zhhgBmebLbExSVW26VkRyZxAyl9qBovXL-uMnlgVOlj_XHZcls-LxVh-lqNkteUGkosamsqleW2aEkULgmI725oF2xCybJdaV-K5F-qquokfK7FJ1JlK6cPoQwTJPedvbL141a7kUq_oM7uw9aX4aGxNz-CPxLdz8I3oobmmXRLuUsNCJ7fXOgAGaCEXK4w0Q81fSfKkJd1gco-r-0I3SgmMzjJBZ5oe9oyOBOq8H_-bKR4GVD1Y6sgZ4PGMqJ9004FXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم.
/فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140546" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140545">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
نتایج ۲۰ بازی اخیر ایران با قلعه نویی ؛ ۸ برد - ۷ مساوی - ۵ باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140545" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140544">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140544" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140543">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⭕️
👀
صدای پای اسکوچیچ به گوش می‌رسد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140543" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140542">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
چیت ساز، معاون وزارت ارتباطات :
🗣
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
✔️
✔️
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140542" target="_blank">📅 23:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140541">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای  جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140541" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140540">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140540" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140539">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgNSz_QJFt0ZNAXvPuwfQKJDxz7Mn0KXLos8QzNQixxmS5cGhrvT0T_0RKzGAP5yRKcNms-On2O_ufjVduNboPCOq99YWESepv-E0_lxI0NNiBcglRnoFkHZouiqxgcBXRch-ZZ_yIryIV5oaXc3Y98kawiI1VnRXcWkUEWg6xlDe5Pm1e-qbP2AfW6CQXuSRj3Gk_QrJKwKjI6H-rIUzYmrTuX2vvuTz_L_MObVNn_WirzNdtbvsA5mANg_dr1FV54ZOtUrUZEXPXCcYwE9pK-5WKpcmtpM2OsVgVhmbEnGlPSiBM3hEQV4NbYM9SIq9TL5zAE8GJEtNobU1FrRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تولد مهدی تارتار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140539" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140538">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
مهدی تارتار با بازگشت میلادمحمدی مخالفت کرد/تارتار همچنان رزاق پور را میخواهد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140538" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140537">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/140537" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140536" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHQ2tVXutRSOIIHX1izdKhGCDb16wDOvC8Xk8N68ef1yGTe6kQKYcewj7MRbv7doLB7IJBuVenm0bXmtvydn59u464DMRkQkiXiTDXr3bIyTb7sOl17VXxkvMhaQj-GMKlFKmlHMkzYYpnGJ4w-pDCfb1eNTSjZsjb671ZSW-E23NtDnoFsh1zVXLUA2no2eS63qibF6X24-7F988euTmikccHD-6YMQFcnAPgotY0PnNcgrKEm85vAhTfsrOtB3vPeOpzjT8QQQ9Iu4YPKo7Uq5VJysQcXVRNJVQfntImuy5QjaazeS3n5flDJq2kWNp2Ce6_oG8maHZhZmGw0xkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
ترکیه - فرانسه؛ جدال پرتنش در قلب استانبول!
[
ترکیه
🇹🇷
🆚
🇫🇷
فرانسه
]
⚽️
ترکیه در خانه با تکیه بر فشار و انتقال سریع می‌تواند فرانسه را تحت فشار بگذارد، اما غیبت چالهان‌اوغلو و ییلدیز روی تعادل تهاجمی میزبان اثر دارد. فرانسه با حضور امباپه، دمبله و اولیسه از نظر کیفیت فردی دست بالاتری دارد، هرچند اولین بازی زیدان و تغییرات ترکیب دفاعی می‌تواند هماهنگی را تحت تأثیر قرار دهد. باتوجه به فرم دو تیم، بازی می‌تواند نزدیک و پرموقعیت باشد.
سناریوی محتمل: گلزنی هر دو تیم و برتری نزدیک فرانسه.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140535" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140534">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfMx2QAFdf5A1i3Vpk8n9FEbYo51RqDGFZ-7pZmTdD6cHoskdCA9bGAnEswzlwGvIA7vamoGP3V8ALGTo9RPFOkTZYwz-QG-yfGpY-x-1kaKVzGuugWKp0aTuAKNnVFGGpPYB0qAe68shtjfR23btW7ri4EylToNn_g8yaMUHQFGxPwmeqczlCa_WwalSzn5bPbKR4wzxsSPZHdmk5w5u9hUYoW0vvWz2Ot432mgD_tTdbz_6erU60glN1VaugAV0E8JpVU24fx6dUu9iSCSx1tjacS3N3FO8_M4d0qqB1cuXuHKUk0xX_gS8a2O7LOXg_T5DbeT0LFgbWyOBx9eWDyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfMx2QAFdf5A1i3Vpk8n9FEbYo51RqDGFZ-7pZmTdD6cHoskdCA9bGAnEswzlwGvIA7vamoGP3V8ALGTo9RPFOkTZYwz-QG-yfGpY-x-1kaKVzGuugWKp0aTuAKNnVFGGpPYB0qAe68shtjfR23btW7ri4EylToNn_g8yaMUHQFGxPwmeqczlCa_WwalSzn5bPbKR4wzxsSPZHdmk5w5u9hUYoW0vvWz2Ot432mgD_tTdbz_6erU60glN1VaugAV0E8JpVU24fx6dUu9iSCSx1tjacS3N3FO8_M4d0qqB1cuXuHKUk0xX_gS8a2O7LOXg_T5DbeT0LFgbWyOBx9eWDyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
صحبت‌های کنایه‌آمیز توتونچی، مجری برنامه شب‌های فوتبالی به تیم‌ ملی فوتبال: دمتان گرم! در کمتر از 48 ساعت 7 گل از کره شمالی و ازبکستان خوردیم..!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140534" target="_blank">📅 19:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140533" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140532" target="_blank">📅 19:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18169032d.mp4?token=M4T19Iy1ExhV9DxCmQTI752wKY0SVTWiylvVyvoNl2Myh6Svtg7CXHHg8n0DPuOWusZLVmAnTGjEgz0IDE3nFcgi8amFTksf90iSfjjf2eoh1W37u2IPJPjPDIMSa7-gsIll8_ilMOiVkRwphugK27gvyEvmVYhxYYY7RrRCyBxR6ha-FqGBcpDS6a9mnxO071HdWXfaglzhgDX9n8PwDTsVgRg4xtKYQAFlkhtMopVI3tuDxeLmnMjqdlRP6zjPgdUmIv8ioGMYwmiZbsPb3AvyaTD6CmaxPKxINoBwb0dDlZny4okaHMqoKX12vWDNCdJPJlDNNvesdXZblfVHXTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18169032d.mp4?token=M4T19Iy1ExhV9DxCmQTI752wKY0SVTWiylvVyvoNl2Myh6Svtg7CXHHg8n0DPuOWusZLVmAnTGjEgz0IDE3nFcgi8amFTksf90iSfjjf2eoh1W37u2IPJPjPDIMSa7-gsIll8_ilMOiVkRwphugK27gvyEvmVYhxYYY7RrRCyBxR6ha-FqGBcpDS6a9mnxO071HdWXfaglzhgDX9n8PwDTsVgRg4xtKYQAFlkhtMopVI3tuDxeLmnMjqdlRP6zjPgdUmIv8ioGMYwmiZbsPb3AvyaTD6CmaxPKxINoBwb0dDlZny4okaHMqoKX12vWDNCdJPJlDNNvesdXZblfVHXTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140531" target="_blank">📅 19:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
پایان نیمه نخست  بازی دوستانه
✔️
پرسپولیس صفر ـ چادرملو صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140530" target="_blank">📅 19:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140529" target="_blank">📅 17:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmO1yhDRnutqy4kj6GmW8L64QoglrYdEFLQPCgxUnZsRg59V-FhNhREbT30XH0LmdjA90jXAfTRA7pNuig_hzGKb2pKTc3wzRrJHts-jtUl7oHBSDslM-lHrn3Uu7-s0JwaRX0QTEMg7_IbKHxuq6_a9Gb2SeweVrrYpyId6ktOCKrrGsb-Ps9QPd6tpsiFUR5wPmSGWlDYxkrhE__0bR8-jBXUGvJWFp0YjJn4-pt6j8udO-g4NvAcfjW1HI1jROs7I5EWgJDG175Zv0AVAmxyJxSh2S-tvh9GCzwAgcmIi4rJeHoi76ScwYZKlY-8zGjIbPI94HTU5Ix_8Gy42pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پیمان حدادی که بازی پرسپولیس و چادرملو را در ورزشگاه کاظمی تماشا می‌کرد همزمان بازی تیم فوتبال بانوان پرسپولیس با ملوان رو هم با گوشی دنبال می‌کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140528" target="_blank">📅 17:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWrtAWamcj5EnJsXyIyFo3zlXC1FuZD4lcfC08YJ2i7sXgj0SCuKsmVSdn2K6czH6_eRNeZMBc_1dhcY4rNdF_ddlzvF9-9spiKR7YFDEa94thoEWai4XU32tZL3CeY6JXAj6NM6FNpDGItIyP5pXiXAuKRHhO6V8KMV2FtPkuVc__09xsQY15EN5Gyv4fsb3OoKoUmdehk5KkAevI-fz5qVD__ndwjCCRXx0Zzz1thjyg2PEtVgbz2R5xvmmM_y_vwsxgjLJDW0d8l7esUgxCdCYbUh7rOtixFWt-zLPe6cbEaZZGy6x07VGyC7m5NNpZZeaqL4ivRLebY7EwX7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140527" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
پرسپولیس فردا بعدازظهر در دیداری تدارکاتی به مصاف چادرملوی اردکان می‌رود. با تصمیم کادر فنی دو تیم این بازی پشت درهای بسته برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140526" target="_blank">📅 17:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW47NNZnQtxcfmVKRFHlEMoZXZGBX9x_lJxEH5vrnjoZrW2u2IdGgeGPp1ntD__VZIxIzXcRjG2Cgxogy2JR2GgEv-5TgeVXf74JiMYOxNm1OLFRACSIiNc7jHDdGWJ03mBHqLyiuxBiUP4QF50MK4iAp6lEnr292Pvkqtp2bRvBTvZl_azSG_Q6s4t1TASGBfVRSpLP7iVUE9yiF4CvY4Kc18PNzi8K-l-qsigpJU5i1DEnDKU08ZC8zNbsFigDROet64wxnjmTcNqWaIERYm_EtMg5YdFUzAI7vUvQSpqQiHvbQZjX32Xk0v-vBTE1FxdVoBxNMTnfzWT6yM6b7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با توجه به حذف دیروز امیدها؛
❌
❌
میراثِ قهرمانی «برانکو» با تیم امید در بازی‌های آسیایی بوسان ۲۰۰۲ دست‌نخورده باقی ماند...
❌
❌
این آخرین قهرمانی امیدهای ایران بود و ۲۴ ساله هرگز دیگه هیچ مربی نتونسته تکرارش بکنه تا بزرگی کار برانکوِ کبیر بیشتر به چشم بیاد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140525" target="_blank">📅 15:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140524" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🤩
فرهیختگان: بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140523" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2kDRnhKpcnRilCNlpXQvZ4KNpzmZBVJrYXFHDpCJQPcQfndsqwLbdZjcUe0BMzW5ki2dtTagxqCdpohUptYE7dT7PzA_xhAUjeeJu6u9C_pyPF__EYn219R-Cg3RLSY1kG2eEsKnIasfNVBoz2ZZjUgEd6kEaMTtumHysJZ7NZZZLoA-Ks3czEF0aM8kp06RIZBw5PuFMkrRNEV_iw3tCFKFYKAF9KP5nPGrq_6gNcqEF60VoARw1L127_4eTByo-KpA36DSdCwVYUGVbkNwqFQdbgMWTSgfNn94-IzusgDSKYCC5DBn--7fFOiAQ7EVPxMlXW2MBdBwjOMk2JtjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140520" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=d-V-QOXi8VY1NB29IW-w4T6rr8PLI24AiBDwdATiuBk2Bm2jBcbVO5d8VX4rwIu0k51a1qAdg99VaJTTYqhXWhWUHqgMaIOv5HzQeVN2WLqkQqSN9dL4wOsfoCZAAq14ceHSTZE12UzpnQOkzToluHqDli1KMuNm9mARHwHddTu-SnXCpNQTvDN3RX03Bi4XCVpYH4mcMjPb9o-Yc3hZY0LWzAvMLB3fXCY8rXPa3SmWQQ2gC2h1i0kNHqfrCfCQvDxo6xqmM8qFmksJaxIlpt7Fyh8i5J6rQ6CFqBZKsgehAaTVUDbfkU0RqFJ4TYeR6FoE8G2N479HAE-yx_u6bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=d-V-QOXi8VY1NB29IW-w4T6rr8PLI24AiBDwdATiuBk2Bm2jBcbVO5d8VX4rwIu0k51a1qAdg99VaJTTYqhXWhWUHqgMaIOv5HzQeVN2WLqkQqSN9dL4wOsfoCZAAq14ceHSTZE12UzpnQOkzToluHqDli1KMuNm9mARHwHddTu-SnXCpNQTvDN3RX03Bi4XCVpYH4mcMjPb9o-Yc3hZY0LWzAvMLB3fXCY8rXPa3SmWQQ2gC2h1i0kNHqfrCfCQvDxo6xqmM8qFmksJaxIlpt7Fyh8i5J6rQ6CFqBZKsgehAaTVUDbfkU0RqFJ4TYeR6FoE8G2N479HAE-yx_u6bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140519" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH5viTlF1q7enq0FYcAkJm0v9rxJvdoN2WrW6jgzJy_LAlcLwpPQDAS7bXqIIXWcwS-ELGEZnbqziuLppXc_mY7GxfEzK4KUEdhaDpuUCtQtXVyGNuC2rdntr89jFOuAWdtcwDV1RlllwJxqZ4t6SIaO_vH4LlWSS-9BGixhzcSqSa9andTR5ZYCVEylbTU1-bJq9wciV-k3cC6asPIf4IY9zWZRDPAwiZfiYRtXhghJIbgkUgllZeEwT0gjjlXCEz-bxyIQa70xdi8sQTEQ_lyqxPEg1QRQZehb4gCay8m5ICOoZPr3-eFG2b6X-Ihe35y3sgRNKnkJc5Fd6H-Wfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140518" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140517" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVy7LEMQdouXYe2hz8hHM3pra5dCA8zsYGFemdquJpJevABD04Ibcm7axEI-4Mntvu_lgbV7ajJZAbAxRa4I-LkikLVuZZJ429Ukj7VXzGsmwGhrEms5rJe8r23svuAfcBnMEcyuDO2KBI_OM51B5rPzwq8fRt7ixGZ1IzNjmxucOdJ9TxRzkHUEEt6lhTLm00mMQVj72ci7K_alLg-JHkNBpv84AAAWyGvP_FMgQWuObUTLZJFnmQkFmDMzDvAY4AtwmEeylPkp8V3BnRtMDbLebsMr9mWOh8VSUfpO1ss1p0sIl_f1d3UX2-QP33F1VoxTYD6RezOFoluSKjCBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای
جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/140516" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140515" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140514" target="_blank">📅 11:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚪️
⚪️
⚪️
مهدی تیکدری در غم از دست  دادن دایی خود عزادار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140513" target="_blank">📅 11:52 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
