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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 00:08:05</div>
<hr>

<div class="tg-post" id="msg-140626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaRKLLH9Pmg0ZCcS5b6ot2bz6YP52UeqVGH6vYjKADcl4bSJTmY4UwGENmY5xfkPxcRe-WNFO9vsSbYK_X5A5q_r5D1RDbWpjdt4QbCnOUfceX1IMjPJjOalKa328-uW64Z5sw-CbsOYL0JUn2C95XSU7rmCSKDUYUT-9MTlz-GLzWptLs44umo4Grp9R6Bu-Wo3xC3kot5EtQTDvPMM7ob1EzKzYCU8XPs6VfMYCh49Fcs1n6R4hxIS8wzWR8kcPqW4OZaREUyDq9IGi30KmUwJUZz1XjctkwTBeTbtrdfYpbsi4kLwh-D8OI2gKNrJAL7lMMC_jF9WZalcbcea6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
🔴
با دستور پیمان حدادی، شورای هواداری تشکیل شد تا صدای هوادارا رو به باشگاه برسونه و پیگیر خواسته‌هاشون باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 626 · <a href="https://t.me/SorkhTimes/140626" target="_blank">📅 23:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkkJ2qOb7l9ApXUt6ZtMEyKGR_iM3Pqn6EXhCMvKzB6Ls9MaWykQpvZgrWLH4ZoWGt1-QKBmxDNx17whcfZyNg_PTFcUy7zzxbaFpSlvYI1zK3TsfeC9xTF-_3qQrExM_Nl21kGMb_6qCyuQydfeJUA_FhhO_0Ks2NSOEmJhd5EdwzO4Snxoufj9YKqSSR6onqHsVbI04T-TAYxWUUKZ5qwfp8pL1PJRbV6ohQhpUX7AlpE0CctnbzYoqa2wI8arP4mW9n96DPdGwLRFyr0jU0btKaFyD1x5-dnrfNikWW6vPXg778YK99Z7CtE9hUCUeSHdgkrEL9KpzpM0ljAxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
آقای فکت رسانه‌ای شما خواهشا از آسیا و سهمیه صحبت نکن که خودت با اون باخت ۷تا مقابل الوصل به اندازه کافی آبرو ریزی کردی بعدشم از سهمیه ای صحبت میکنی که بهتون هبه شده مثل پنالتی های معیشتی‌تون
❌
❌
شمایی که باشگاهت که با وجود ۶-۷ تا خوردن تو آسیا حرف از تخصص می‌زنین ، هنوز ۷-۸ هفته مونده به پایان لیگ خودتون قهرمان میدونین و دارین گدایی میکنین، جام ندیده های بدبخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/SorkhTimes/140625" target="_blank">📅 23:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
❌
❌
❌
❌
❌
❌
🚨
اورونوف در تعطیلات موفق شده ریکاوری خوبی رو پشت سر بگذاره و از نظر روحی و بدنی دیروز  آماده نشون داده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/140624" target="_blank">📅 23:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140623">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/140623" target="_blank">📅 23:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfce03f041.mp4?token=ec_aEW4eK4FhgCo2yf-SSsJ5zioOP177VSemTeeo2_lrrab3re3lbd2C_d2idY__O4iOo0yav76UbniFd9F19b6JBAcT2mNK4zNbh8Yf6pNE4DkdSdYFeEGmfu4EpFZ18L0EUUHNvOFJshi6BsoF0_7vsMF4ILC1qRKmUNEYZHPVOge7gKWcuTtSf9maMRPi6HOF6BhVVqmZmj0MORscsKnR7PQA3R03DRqHZrj1cKSXYcifSKDMWSrC1rpXGvdXOBCzEt4d39YKo1c1_cwYDlq2QsIPblgvHwdPdImlXyPk0jSYKhNYQa_0DRX8o2mLWINsucQqoS8ewsJUz-tSYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfce03f041.mp4?token=ec_aEW4eK4FhgCo2yf-SSsJ5zioOP177VSemTeeo2_lrrab3re3lbd2C_d2idY__O4iOo0yav76UbniFd9F19b6JBAcT2mNK4zNbh8Yf6pNE4DkdSdYFeEGmfu4EpFZ18L0EUUHNvOFJshi6BsoF0_7vsMF4ILC1qRKmUNEYZHPVOge7gKWcuTtSf9maMRPi6HOF6BhVVqmZmj0MORscsKnR7PQA3R03DRqHZrj1cKSXYcifSKDMWSrC1rpXGvdXOBCzEt4d39YKo1c1_cwYDlq2QsIPblgvHwdPdImlXyPk0jSYKhNYQa_0DRX8o2mLWINsucQqoS8ewsJUz-tSYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مدل موی عجیب و غریب یک بازیکن در کونکاکاف
▶️
#ویدیو
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/140622" target="_blank">📅 22:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm6t2IwoEMuCCNpn99apxeL6zj9-_hwjs7eDRh4Rbzo4zWD7_girtdw-O6EFn8eqTZ21a7PpdzDPKh_9u-EGSglAXr6Ai9roqgUojGmCPcfkSAhDS1cSK6Mm0gnAGw6CC7IxAo072zpSUsxamViaqrBLDYrnNGdnSxAoD3tM2fkEclSB8R2n-fLRurJVj768kbPTb6WNB3UL6mglGVP3xN1bKW-8HA1L9Y112DL9qX-PxLCjJc3tNim4T69pcyOTfcSru2yAEmaSm1Q5rVavRPOOygrpqsM50Ks4-yNxmoTG4CMR9nrjfoSQDGkI6j_cUU5Vi4jEFcby6JKWGs-MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
یادآوری
❌
وقتی قهرمانی پرسپولیس در کرونا درمیان بود‌، منطقِ اعتراض‌شون ٣٠ امتیاز باقی مونده و احتمالِ امتیاز از دست دادن پرسپولیس بود
🚨
حالا که پای قهرمانی خودشون درمیانه، ٢۴ امتیاز باقی‌مونده و احتمال امتیاز از دست دادن خوشون رو ندید میگیرن گدایی جام دارن‌. چرا آنقدر بی‌حیایید‌
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/140621" target="_blank">📅 21:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
تیوی بیفوما:
✅
• سرعتم روی گل به ملوان ۳۷ کیلومتر بود/ سال گذشته اتحاد تیمی نبود و شرایط خوبی نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/140620" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/140619" target="_blank">📅 21:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
هفت ورزشی؛  به استقلال خیانت شد؛ برگ برنده پرونده آسانی به دست پرسپولیس رسید!
🖍
ایجنتی که به باشگاه استقلال رفت و آمد دارد، مدرکی به دست باشگاه پرسپولیس رسانده که برگ برنده این باشگاه در ماجرای شکایت از یاسر آسانی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/140618" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140617">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/140617" target="_blank">📅 20:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140616">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
⭕️
⭕️
دنیل گرا مدافع راست خارجی پرسپولیس به تهران بازگشته و اماده حضور در تمرینات گروهیه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/140616" target="_blank">📅 19:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
بالاخره انتظارها به سر رسید و دنیل گرا پس از پایان مصدومیت، طی یک یا دو روز آینده به تمرینات گروهی تیم پرسپولیس اضافه خواهد شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/140615" target="_blank">📅 18:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140614">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/140614" target="_blank">📅 18:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
⭕️
فارس: آرای هیأت رئیسه فدراسیون به قهرمانی استقلال ۷ رأی مخالف و ۴ رأی موافق داشته و به این ترتیب احتمالأ جام به این تیم اهدا نمیشه :)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/140613" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/140612" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140611">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/140611" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/140610" target="_blank">📅 18:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9ahKaKl_doAjF9SuN3z_ReVp1-DUH2IpGHQiThy2MWbW6HI9JIEb1GNctTp_JpxDQTL8rSZf_zcoxhObJc5I5C4US60ZacyCqfthn9W6Rp3Vm5iUtfzOQl59oywSMjcKrrIh8xUr71O8X8bhuSNVvZuGxHwAHhbS9Xb2lbHsJr6XwCHSQAkfCVZ9hQxL9xYDvtOUIOjoUOjrbZdYt0YdeT75PLiQLBpNG0rU0u90WP0Y2g7a1X8n_so3GKmsNltBbURUC5WU8fby76F-qOTtP165maFWf_33ygtktLIMRnZbrr4BK7JLwrZnFEvq2f2qTN5Hci-NCiO_fDB43PnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140609" target="_blank">📅 16:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند سربازه و معافیت نخورده و هر بازی که انجام بده غیر مجاز هستش / مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140608" target="_blank">📅 16:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140607">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/140607" target="_blank">📅 16:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند را به مدت یک ماه تا پایان مهر برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان می تواند  در بازی هفته هشتم با استقلال تیمش را  همراهی کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/140606" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140605" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140604" target="_blank">📅 15:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140603">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140603" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140602">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/140602" target="_blank">📅 15:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
طبق شنیده ها
❌
ابوالفضل جلالی مجدد دچار مصدومیت شده و بزودی مدت زمان دوری او از میادین مشخص خواهد شد
😰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140601" target="_blank">📅 11:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚡️
⚡️
⚡️
رضا شکاری مجوز بازی نداره و صرفاً در لیست بازی قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140600" target="_blank">📅 11:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
امسال جام حذفی برگزار نمیشه و تیم های اول تا چهارم سهمیه آسیا خواهند گرفت!///فوتبالی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140599" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140598">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140598" target="_blank">📅 09:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">😰
محمد احمدزاده، سرمربی اسبق ملوان: یه مقام استقلال‌ به من زنگ زد و رشوه ۵۰ میلیونی به من دادن که به استقلال امتیاز بدم تا پرسپولیس قهرمان نشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140597" target="_blank">📅 09:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
✅
مذاکرات پرسپولیس با بشار رسن در حد واسطه‌ها در جریان بوده و هنوز به مرحله مستقیم نرسیده است. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140596" target="_blank">📅 09:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140595" target="_blank">📅 09:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140594">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OczkbP2Mi3N9Fa_WVM2G2UPkBtN8mDU6VUege7jBarDU6WdjNGKnT_B69mEgJnR39kOIk1r1YkIwM7WXZxChMopZKLpaDNBfCykJdYrrxwJs-yWZvOtJ2L5BvjNtGBNGu3f7LWWUMpihWZAwDYmpMjERvgpbj9arWTSMbTCcgvPE_9TNrqqjBmRmQEIO0K90L4wfCTCsbUsC6HT_UgnYfer7dF5GJDWCgHiiAY8nyLW64VfmrH0upLiVqyCCUDCA28h8uBOeX0-lbTpTu20eBKXn0WMUVzUmNNtmJD6499ggt-hkFHaqnjXf8b0v-mV2Z9TiXQ9mhewcCu8tKhdF8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140594" target="_blank">📅 09:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140593">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140593" target="_blank">📅 02:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140592" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140591">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140591" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140590">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140590" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140589">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140589" target="_blank">📅 23:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140588" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
🔴
فارس:
⬇
بودجه پرسپولیس در فصل جاری ۳ هزار میلیارده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140587" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140586" target="_blank">📅 22:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140585">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140585" target="_blank">📅 21:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140584" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140583">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140583" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140582">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140582" target="_blank">📅 21:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140581" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afZkglPR9Brv9mgmZiJoyzVMoaBCcg7bG40umKX35RApE1y6gqULnETOPQd4hMzUraq5DwdE67rmD33e9Zl3gormpnUyUyucfWp8a5SnS3azlpoHZFgIka2au2FvDWVPbYeYzeAFqqY1sUOUwhGl3jnwD9bMEEEjm7eI8mWy_K35MSHQRMmBlQ-2vfhRZdDRGUyWRAaaWst2WTDlTiu6Dex7SjWDmoQcX8Pqfb74P1n9BSvGoYjXyVNWjKruK1dKFip-CApzxfeoqD1OhEp5XgV59A6Ve4BZ87FFjdBzunnZYNYUoeAk2A6MNYPePrTEI-St46ZD9Eg9ORpIc0MJ3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140580" target="_blank">📅 20:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140579" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
🎤
بخش اول صحبت های حامد کاویانپور مدیرفنی آکادمی پرسپولیس بعد از دیدار با امید سایپا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140578" target="_blank">📅 19:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140577">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭕️
قسمت جالب سربازی بیرانوند اینه که همین آقا دو ماه پیش علیه علی دایی استوری گذاشته بود: «من هیچ‌وقت از رانت استفاده نکردم»
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140577" target="_blank">📅 19:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140576">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140576" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140575">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140575" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140574" target="_blank">📅 17:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
اوستون اورونوف و مارکو باکیچ هم اکنون در ترکیه حضور دارند و اگه مشکل پروازشون حل شه تا شب به تهران میرسند    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140573" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpaMT5gnMul91ZDuRl-T99kRcbtqgHag99cGYv-lZf6MaHiKVDpXTIzH6_vMEHoxljNpM1uiQj5nzYRWql9bo1Z9kIq4pWRdvpB_aK62v2H5PGW0dnrVUGrZfUqFdOMlVLvW5mX5hBv4woK70BdOSuaGgMSPl9Mozhea3kOvUKXTV4XyoqxVgQ1Q95lkY9RaDWNh8WBEYCP4UqZ1vOp9BvHq3PAwdfVRaqa96W5XPbB3XLzNUevJXMpaDwWr8VYMYnWiPom4vaO7Rq49AhCwqcobNoplZOwsiSMbsDQfQg11HHqwSqS0OkCHiWLY0_OwSIybwp3ok6ZZzI6sDuedXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140572" target="_blank">📅 16:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🔴
فوری؛ معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140571" target="_blank">📅 16:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZQrIZlP0oYXuo3ZHWvUW_PFPtCaKPBBBXgFh5EWx8MD7LWvGOBAIwXUoD6DDPGTus1pbinonMea2m70kW_iJ29LgA_LG7-NZktZ-LvadWiM2K2kJMWryS3YgndqheLDThk1F-TOoqtz2OGXRihKpSA1ETZAwyKNO3ib7gEKB8NhPMw3ewKYJt8yYwsCt3fx8A8j6gNGdmEWE9DTFmVtTdw3mjtzE8c3pthnj1CgyvuHSo_Xurgs9vKtdhVSHbWbsqd2hPoyg-az95w76pkGolJQYY-huchGGQmliljOnnteS33NywEwh-M5Y5Hd4CHEqtcM3_6ajOZ7UtyB9tHvVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از بدنسازی امروز پرسپولیس؛ شاگردان تارتار فردا استراحت خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140570" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=PHH1QeBwuHcX3pdsflqD14yFAQ42aB_ZD4gigdJxP3RKGFm2ewgIkRxU3nejGgImMZnb_zgTfl7IGyaMjqt1zScXK-zYo7q5j44U-AzXXXU1krwxU05a57MCLdoGBmJsQZXc5ikhiycpUiyH_zICVLBpcGHe841st-fPohzxCTHkY_0JQjdMkESQTqCqn7mkGJFi_w_U2Rk3WCOj6ydwnFe3i4umE-dgY_MXKkAK4_cRfvMkKy4vxy_Z5FPPtnRGxSyygIC6Ns20F4VI5ptVXnFBnYt-0bFenqs2BDhqvGu_5XMKY2CjUM4CLjzAgJx9Y4ck49K_knEDhiyhKXtf4TB0ZU0JwsmGwy5vcRQ0kpCQZKTxLnWd4XCbEHSA_CxUb-uOwjnqkrApEYuVx6WsgBsovfAOvAohZ2XlCeKYeddog1Y0QpkhDctceToVP1PAUmvTBlaNJP1dWZbJuuulY1H0pbdkWnVcI8AFh-2-KnWFCA2cGUniQTXbF7r8SBCRID7QpAWYHeIamsZDezgD7N48i5wOaltgtnhOSgPDWMWoEW-TVmmSoJ-RFFJ8uPAdemlgDdGYBtcwdY0_fhs2wHuKexMHwTTAgGSwIowitY8SEuOqIqLwCZA0JR4HmH0V5mZBJ9SfhAZjzXBrXCMWgsumswP5JlOLomKLiFaao9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=PHH1QeBwuHcX3pdsflqD14yFAQ42aB_ZD4gigdJxP3RKGFm2ewgIkRxU3nejGgImMZnb_zgTfl7IGyaMjqt1zScXK-zYo7q5j44U-AzXXXU1krwxU05a57MCLdoGBmJsQZXc5ikhiycpUiyH_zICVLBpcGHe841st-fPohzxCTHkY_0JQjdMkESQTqCqn7mkGJFi_w_U2Rk3WCOj6ydwnFe3i4umE-dgY_MXKkAK4_cRfvMkKy4vxy_Z5FPPtnRGxSyygIC6Ns20F4VI5ptVXnFBnYt-0bFenqs2BDhqvGu_5XMKY2CjUM4CLjzAgJx9Y4ck49K_knEDhiyhKXtf4TB0ZU0JwsmGwy5vcRQ0kpCQZKTxLnWd4XCbEHSA_CxUb-uOwjnqkrApEYuVx6WsgBsovfAOvAohZ2XlCeKYeddog1Y0QpkhDctceToVP1PAUmvTBlaNJP1dWZbJuuulY1H0pbdkWnVcI8AFh-2-KnWFCA2cGUniQTXbF7r8SBCRID7QpAWYHeIamsZDezgD7N48i5wOaltgtnhOSgPDWMWoEW-TVmmSoJ-RFFJ8uPAdemlgDdGYBtcwdY0_fhs2wHuKexMHwTTAgGSwIowitY8SEuOqIqLwCZA0JR4HmH0V5mZBJ9SfhAZjzXBrXCMWgsumswP5JlOLomKLiFaao9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140569" target="_blank">📅 16:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🔴
فوری؛
معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140568" target="_blank">📅 15:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140567">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=aWo4jxzuuls4DGek9jKSYKL-VKv3POoHbvc0aAEBygS1TgrRlnByRjV0S1OKlwXtOUC8d_G4cEXOWhq15B980ukD4sliR5pD-gpidXOtjQL8_Rt_HFlbS2Svd_2LLbxfsZy8AxZaV8o69YuKnHSQdivJrI6beSc4JG5MIDhkknLDx-czCo0asC8q-KWZLIPFqhIS2_x9BEKilsKFPU9jb6Bwcf6Oz8u1SIvtGIMLRmw5mB53P19dE2LkMmdFA9mzsERYM63ti3xwtWhrLziOxSNdByTKiDhOfLeqKkojTcj3uNIV8bYs8UxdUcrp2GJre85lS6gwVFJmMhiLoQNyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=aWo4jxzuuls4DGek9jKSYKL-VKv3POoHbvc0aAEBygS1TgrRlnByRjV0S1OKlwXtOUC8d_G4cEXOWhq15B980ukD4sliR5pD-gpidXOtjQL8_Rt_HFlbS2Svd_2LLbxfsZy8AxZaV8o69YuKnHSQdivJrI6beSc4JG5MIDhkknLDx-czCo0asC8q-KWZLIPFqhIS2_x9BEKilsKFPU9jb6Bwcf6Oz8u1SIvtGIMLRmw5mB53P19dE2LkMmdFA9mzsERYM63ti3xwtWhrLziOxSNdByTKiDhOfLeqKkojTcj3uNIV8bYs8UxdUcrp2GJre85lS6gwVFJmMhiLoQNyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور پیمان حدادی مدیرعامل پرسپولیس در ورزشگاه درفشی‌فر برای تماشای دیدار امیدهای پرسپولیس و سایپا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140567" target="_blank">📅 15:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru-o6rUca2G7yHX1e7rlRjA10laainAieoH5V-GfsmIyiIoTplMbe04AZQsO5FNmaWTq4ZBcE9vIgejZMpxLKb_mPBB5fQ-42vkjyfc2sxQ8mmpFkmUmFlGpEv4nywEIaUwHiWB5QUUa-D3rQ58YyM8wHNwwWFdQC4WJRhMQl7GdWebrqcSi7x_Xoeidj_LByt44BmqmmHVeSJXf0Y2TeguVupEzKEPzcrYmYzfsUwXlH9J9bXqDigYUMk5-jybq4lRigrDqp8VXYADH-18s5nsqxdRR5CkGnD0EljTxFsQNn0us6Ve_fOZmYYVWVjpWPd4ujSc5tHpzdo4BsghjMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz8E17cU09rqlRfUslTX8G7UHXstLe0_uWj9OFXz6_0Tit41UNdZR5q1jLYgi13mZnxy7ZA8A55XCzYuDFTKqlTt5XV_xZxYwwuqeyLZj5SYKuXEdH1TmpRvCxx0UeYDUGlyjbmJcdD0PepsoL46lK9IicAq95WjwJPKtUM3iX26B7MJoI1glhGFsd5VB6ZjG83oH8J4drG7JiOmJ5_gYDMT0aaBh4iVyQ4lZh8qrPc43sxoHDFuPBnLclvbL3TF3p8BV60S2tu7SA6xZUjQFXDoHAEyRwrqb7klEksOc0pwEu-tT5mA-P2wVXosO1IBTkGlZQnkwwROLRWs7ZuVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم قلعه‌نویی واقعا عجیبه!
❌
بازیکنی که از جام جهانی خط میزنه رو کاپیتان میکنه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140559" target="_blank">📅 14:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140558">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚡️
⚡️
تاج اعلام کرد امسال دیگه سقف بودجه وجود نداره، اما فیرپلی مالی اجرا می‌شه.
⚖️
طبق این قانون، باشگاه‌ها باید قرارداد بازیکنا و هزینه‌هاشون رو منتشر کنن و اگه این کار رو نکنن، سازمان لیگ خودش منتشرشون می‌کنه. همچنین باشگاه‌های زیان‌ده فصل بعد با محدودیت…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140558" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140557">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
فوتبالی:
✔️
✔️
گفته می‌شود فدراسیون برای جانشینی عبدی با گزینه‌هایی مثل فرهاد مجیدی و مجتبی حسینی وارد مذاکره شده و باید دید در نهایت چه کسی هدایت تیم امید را برعهده می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140557" target="_blank">📅 13:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140556">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140556" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140555" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140554" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxpxW0vHlPBUB-1W2OjWY5khGPQ7-lF3cyZlz-IQmRIrErm6tjgZayuaNkUco18JPLhVYb8D4Q_4h1rA6XAeM29RIT5eYJfPQSmJ2FI13fGAB_dzFqPMsCqIIvTpDZrCbA73IE-5iK4r7DF7gHnoHgfKdB7uGUQ10zj7LnFRhitt3VtnKXf378WpaQ0aE2YnoAARv4DOS43YbkTznKlGjVWzqU7TYtA4asbFaBiSeVGLUGvZ4lS676gUZE4aOpyCNxHd0f0AvNE8_OblEelzw7fqW-g4Cud7ykOvYuygIiHOJ0TJZRii-iZjIDKOFMy-rSUWdZRn-4k5Ex41zAZ6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
باشگاه استقلال در پرونده فابیو کاریله که فقط اومد یه سلام کرد و رفت به پرداخت ۴۰۰ هزار دلار محکوم شده است.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140553" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
❌
سه وکیل خارجی باشگاه بعد از دیدن مدارک جدید در پرونده آسانی اعلام کردن، درصد پیروزی پرسپولیس تو پرونده زیاده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140552" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCZ1ZU4nKVd0NYJwImEhfEIB1p_DgXY0YcN5iXE6eoih2rB5B5dOmFlab3GWgwgfC7wh0J3Oo239E1K-r2LGzETVRpmAhwX8mrXn2udh7XClKQ9ja5FJHrkRtySjxPCYH_QECTwn06Hdcm26FsslOd_lJfJolbAOxJ2pQTvgXPrU2uErLWQiFMaQZIncvupw-KoDs13X5nierWSUk3LWHUdw4n-fu2iT38plz05hzC7sSbdVcoEcnA5iYjXE9XOygg1WA8x9_uHeiodAxtkw4P6xGWnotemNVbba6oFzFG1y0N6Ik0a9Nb7Eh97wsffpLPBGT-ClOu7JbP_pfoSIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140551" target="_blank">📅 09:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsSRa9j91O88KVTPn7QHgiMBN3T_DwMeLw1PToCXnO1dB1Dw2mnAcjKRORKDbBQ1t5qqbfuvKM6sIAJ4xXkEBMvXclTKglI9LDK6nigkzYI6dGlcKjMSbQIslkEeLeHpqw166H4EHhNqYYWP-O0QKvXa_ItBkgrZhQWHPGGMhT1TsdcKhqnea_1CWMkZNKdyBZMdZtX5wrQWc3EzH55-uBOxzpuYfYuoKCGn-zI8dE81g7Wb4u_EG3O-kwHmm0IfVqTD8m6blWoegxCOXnhLZub2O9vQjIM3Opr3O-npekHMqzLlfvYejLFMJ27P9n4b3pRmRz3V5b3pD70I4PZ6wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140550" target="_blank">📅 01:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAERYeMEpWfd8bt7cwCsnq7oipt38gffWj2bjLPuSjTIKcnCvTUISi6LOHIj6ocunNSzDr1R3QaVVAcNWkcV7BSq0SyNyLWGrx8TvcSrSP8t7sX3RwOrfooNRF2evuMZvHipUIhJJyoFFH_mCwTb_CYTqz5JbnnZxxWM51FQ-PNguNeBFCA1grR7Up-D0fDBOUWWWWoQJ56ffXFEkxPsKaDyC4ZSWYKbrp3O2oK4zMVTmTcq0M7GImNjGiCIn_yexhfpHnnD4BjkqshiwQRVHrl-f1q-IXUyLE4TIpi2gDBsDZp5hQ0T5Re0u2VHaGeGluemBDj4eF_gOileQD0t2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140549" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imqP2TMQtsK_N_kwkm-CLenmrtOHJdR7oDhCaxAY3FOeUJedbXft0FX085G9i6hrGwoinKEjq89-9wESNYYcPlZ0R4tQ-Fuynf-kiukxbzNlY9I0OidGFmDhBrWShlr8DVTWdheXuxaDmldDo0GkqXl4ppZlrlll-2VGMtHj7PxNoGxgZtm8kz9KVAOGK863can8GHn-lDzQxci-hIt5SgDWDQzntwLBSNqHrs3_HkH63S0vm4aE2Bcjj2jBGuk33JUsmlPsqztHBjAHGizpa3Ad3ItX9PJv4AESQtleXKVxRjfsJ1xeQzJrBZMc-IyUueFQFKPCSbakTeyE-w9cDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نتایج هفته دوم لیگ برتر بانوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140548" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140547" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDuQU1GDBeB-qr23BKeQxlrTPW1v7OLE5JgeeoUGe5SyUrdVx-47tzRH8tLtx3A8cWCORS0nHtRqc7k-mSZpqfgrk_5_X7tPCIvcUdgK8QIAgG5m6HSGxQd1bzOg2xmgQvV2GuulXb9-XBus4zWbj0R07_0Q2UCtfFoAUuiCN_UmchnakCam7Aa_J3AT_7PgOuS32EN4MniRlqIISGsPjD3jlYRNMBMYiDDkv1P9mSAkDgI7WoYv5kt11XADcBeQJYrFjr8qfkEaIjj6eiy3n3wzfN5O7pn0YJLvC8BmgkeJBoZ_MqQnec-zuzuOa-qsDAdfJhiQHKqfqXzVOEBDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم.
/فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140546" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140545">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭕️
نتایج ۲۰ بازی اخیر ایران با قلعه نویی ؛ ۸ برد - ۷ مساوی - ۵ باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140545" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140544">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140544" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140543">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭕️
👀
صدای پای اسکوچیچ به گوش می‌رسد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140543" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140542">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
چیت ساز، معاون وزارت ارتباطات :
🗣
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
✔️
✔️
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140542" target="_blank">📅 23:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140541">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای  جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140541" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140540">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140540" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140539">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW_ZUqjCvZZkHGtDz-UDeEQ4UnLCxLb8nXrta0eL8LL0qeNSURpdcI-OjfLzbPKL7_la0xusNioMENwydHOxzIEuiYiObAgMAvAPleF2rbXBPRgZ-00jrBThQh5XJhQtAPiN2LQ35B3DCs6Ej4itRP2fOaymsjuhQjZZqk-ShHXuMXTK1CiD9bDv4izwOGyu4Zn1Hb-6QkxhNaEc2w6rqB4LF9UoNzF0Bp1D49ETLVkKA4EjnDsxER7BmpYOLqs0AUVSAb_bI97aso-pKIqmFio4EcNGU5oTNami9ApmI2xIiXNO3X82ju0XgvqNInKrtRzbOOdcA8candGUc28oag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تولد مهدی تارتار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140539" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140538">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
مهدی تارتار با بازگشت میلادمحمدی مخالفت کرد/تارتار همچنان رزاق پور را میخواهد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140538" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140537">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140537" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140536" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZtc4h3YpDY6ycGvjcqCOAO0eyrsPLu95uVS_N3zgqh3R6zfLd81VsGSf2m4OOyJHCQdCBgYihdd8Kr_yKI4qLZcKtcpoEBkSIjWKIVKTuzRGdCJ2ZRplvWFDiLiFIfxMdAkCfUe2SRKnCf9BadneMwGallvGiPyRebYeDz3lMYEgArgpluTJM6uDbq3E1MMxoO6rDas8FaaooNKQOEQhE61r06AjFJWtZYSurqqXdkw9xloOzPxQvW0iHIBLUUx2wW2S1r1e8gNcdRNKgl4GjVN_468bXNMXVk666Ue_yK4x3xh52dJ9hwIeNc8dngC6BvsA5_hfl0uD2BupGDlsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140535" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140534">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfMxPBcHSmvQ8neUjS5oadqXG_hcznLl6eX1VRaw6rf_fR2gEHETCYemvH5IZfExj3Bo0f8Dy_ix_qNZBIK3-kyrMAlD4kjdC9dH63v29t75wmQQbz95d73wiItsZxX5mgyS3-0K8nwsT9a_e4Qk-1bjNZ-wM9HDZcSa46jfKfjHSgx_NMummBBcHjjZMn2RstmY52CegOU_BpLZ3Xus-cQHUS932vEVrOoJJMadV5i9zCNsQ71NWjlZuipZa7D0BjJhjV0Uz-rNV9TX3gfRIsXMa31XB_p4CPdz3Vb86qY1W2coH4KRHkYHwCgFpB2Xy9B150CGvWQ86nmAs3tdyhiP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfMxPBcHSmvQ8neUjS5oadqXG_hcznLl6eX1VRaw6rf_fR2gEHETCYemvH5IZfExj3Bo0f8Dy_ix_qNZBIK3-kyrMAlD4kjdC9dH63v29t75wmQQbz95d73wiItsZxX5mgyS3-0K8nwsT9a_e4Qk-1bjNZ-wM9HDZcSa46jfKfjHSgx_NMummBBcHjjZMn2RstmY52CegOU_BpLZ3Xus-cQHUS932vEVrOoJJMadV5i9zCNsQ71NWjlZuipZa7D0BjJhjV0Uz-rNV9TX3gfRIsXMa31XB_p4CPdz3Vb86qY1W2coH4KRHkYHwCgFpB2Xy9B150CGvWQ86nmAs3tdyhiP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
صحبت‌های کنایه‌آمیز توتونچی، مجری برنامه شب‌های فوتبالی به تیم‌ ملی فوتبال: دمتان گرم! در کمتر از 48 ساعت 7 گل از کره شمالی و ازبکستان خوردیم..!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140534" target="_blank">📅 19:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140533" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140532" target="_blank">📅 19:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18169032d.mp4?token=pvDk1827-Ex_fNx2Fl1t7QEnomavSB79uS678BgbKOelQ9Ril-BtgfjtngoHb3DV2B3O3Vx7D5qGCm7d2BWcprcniEkpkhn2fjyvA9xl7ZkSiH4mcV3Q85wLGexDTxXJWCAhAWseKnemlY9RImKJR0uIaaxHeJT7KoeVx8C7qlhGSWo8d0UEOHgUEBmugPHCSNXFPmiLk7qCBZo3Ry_pXXl24KQP8FlgO2Y2LpzAC6aymUfXjvFKJtRyUeSM0Mb_Qc0rBErSGWQtJthMrhWRk3p3KQE3ZbGS9tCXprYI0l6T7ah8x1s_TzT45jIoSr6jI2APzi2KroXtTg8b1T0njTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18169032d.mp4?token=pvDk1827-Ex_fNx2Fl1t7QEnomavSB79uS678BgbKOelQ9Ril-BtgfjtngoHb3DV2B3O3Vx7D5qGCm7d2BWcprcniEkpkhn2fjyvA9xl7ZkSiH4mcV3Q85wLGexDTxXJWCAhAWseKnemlY9RImKJR0uIaaxHeJT7KoeVx8C7qlhGSWo8d0UEOHgUEBmugPHCSNXFPmiLk7qCBZo3Ry_pXXl24KQP8FlgO2Y2LpzAC6aymUfXjvFKJtRyUeSM0Mb_Qc0rBErSGWQtJthMrhWRk3p3KQE3ZbGS9tCXprYI0l6T7ah8x1s_TzT45jIoSr6jI2APzi2KroXtTg8b1T0njTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140529" target="_blank">📅 17:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATZVGvSB7GfF5pIDeksPnurOIJJNDBp24u0yGy0yiQDBuNe-KJEMHq9U2fAHfQSgnB2yCNAs79f54I0j7Tj0FFO_9E_OEiWAoCHpMgC3LRO7XMmwnqXSomA35Q8fyTB_n3OXOfnLKI771BH3Vmrits0WaYv2grAMz1-E78ws4HIx4H9bs6B87Teb5ec3fv-q-Wg380_tXvgW5JUurj3x-jiJlsThvkJ2N5379YTgJ1NYns_H4-bNnCFR9lrfjmtTskjg_0op_vUjNT9zOFCB_tNpwWpzpj_j_xFDe0ZOV_AUovjilzfhFwE1SFamdDMGVda3XaAF9WV-hFIRHbnk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پیمان حدادی که بازی پرسپولیس و چادرملو را در ورزشگاه کاظمی تماشا می‌کرد همزمان بازی تیم فوتبال بانوان پرسپولیس با ملوان رو هم با گوشی دنبال می‌کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140528" target="_blank">📅 17:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmRScR2IPqu_LUOlLW0JZwwl1Fz0QX4fjVsnBguKZOquFQp8Z-hTICiMogEENB6UliZlPBgnS2jfAFJ7QeLbKAQsQ0aMxN3hgVZ3mEz-bIcHBEtQV7bcwUgixhtmqHVuIo71qtisfRoNojAzu--1HHGYONM86xOGv2Ldi6GLtRfolbod_-x0fOov4Ul7Qz8JofUIfzWcSW47YTyqKtFrrH2LrJgG3H-W1frSw641XlBHJULSyTzTCf88Q6shWimGbbf1wMX-5r-BHD_C3ZUycDUH3gU56z8urpuWn4cTczUPvzoEfd8kjEuEG3uI4rZe2mEx8WxCY68dl6DxI0-JRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140527" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-yivlyppU9ZcgsvJPgcSmPpUK0ajh82fTboBhLwniTCjXurhnB-ni6nwDV3UXYXhbbpB8Ra3STRGRKsDH7IGLqeHLtjvONEBBSxcc_IedVv9A1uEd7FmkfcNm4ya66uFakaTwV0O5t7KvV-zVkTmByOAZnDKjyG-VS50vvJw-lszOCYlsskTotKf4oBZaQeKV6KvTrHfyixnqv5x93bJUhtm3tvqLXYDvaxQKvxYakc4h1i2DNAckC8qRuxt_b3v8Pm3CdnWewWJq0CPj5gqUe-Z15WAGIlPmARP0BHLolLmLumGZq6M8OXZoPRNLUY_2_hcuB5j2IDcxrXjgMHBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRiI-iDsmtgW-i9s5pP_p9VFap6yOEaRx9n-FSAtkVr5AJJwieekHg8G4M0JjJVl0DZF5x8pMIP8nKdZzRiXhTjvB3-v-hDfwtE7WHebBVfKRGDUeOShQ_hRww03ZCs91kmpFiMHE88N7DR-Kx2_1K-efYpkryCir_xUUVlztdX7CJQCjy25oJR-Fx1Ehr7dwDQfBaGpH2Qt9Q-yTvr5mMPvw4TLKB6lPek22lkoHGYkDkoOQw37wSpeGLfXT7kf2CpY2iSRLAjTb6yXuwbnnf3chuUNHaZgMJWUdOxiXdsJ-pKgock5Nem0tGcL2Mkea-4lFoyvLCgVXco4nAblxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
