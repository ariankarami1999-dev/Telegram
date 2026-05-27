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
<img src="https://cdn4.telesco.pe/file/Eh98jeztykIUJ13-IGr-8Ye0_IZWdCBtRygvPkqV49v_ocQO1XkiTAlnMe-FGskVCpdgul-537QZXgLRyfNZJSm4xy4JNfVLPp9CsLxBjWR6e9310A2WZpV-0K6s4Csbgaq5gj1Gy4-ZUF3FpU5WBB-a8h7pXg-X7NYLPrgnw8HPlqJ85HmsNw_cy0Dko3OPWzP1BWfl86ecAjsrcHr1KpyWMDBaa3B72GAhf5vyQbS4xRjpNtBFLPM8PJeWf50vHtzZkLSXOwqRpiuxj_0XQN0zkDymHXv3UruUZaL_6U2JxBLu-ay_Oyc2yHJTr9A0JkjgKdO44nfkOEwSgugCAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.7K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
<hr>

<div class="tg-post" id="msg-132306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpqkBWQWwLd-4OO_JFmKmvYguMMTnzArPec3ntjoAqgKCUOmpk9A0-kyYQicLpKtZRKFCLoxEfiFY1evp-EfQU2cr0XHYvyNhFiMTQ6sp5R9YjvFAvl2NghfZygrSaMM05XRPF0BI45ufJPCsQpUEIYCgjbVqgDItB2WWO9NleHXgB_2HKTMAlmdlLo5Lc2y6qTON2-SVxssqQgIIoiqiTgVYycpS5jc5kU8d1fqsAb2_hOrzywY8fJQ6SJ0mo591BAkh4tt-AZgV2Tziy0lmSmaubDdlwaV2clFDuphp4WbI6lngNiB5chA-vOowXfwb1ib6b04rNDtqhSAC8vRfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🟢
یک فروشنده در تیخوانا مکزیک، برچسبی با تصویر تیم ملی فوتبال ایران را نشان می‌دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 322 · <a href="https://t.me/SorkhTimes/132306" target="_blank">📅 13:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 400T
10 گیگ 700T
20 گیگ 1150T
25 گیگ 1350T
40 گیگ 2T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 581 · <a href="https://t.me/SorkhTimes/132305" target="_blank">📅 13:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است.
ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/SorkhTimes/132304" target="_blank">📅 13:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132303">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
سردار آزمون به زودی با انتشار یک پیام عذرخواهی به تیم ملی بازخواهد گشت.  #خبرنگار_فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/132303" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
ایسنا: مهدی لیموچی در آستانه پیوستن به پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/132302" target="_blank">📅 12:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132301">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
طبق برخی خبرهای ضدونقیض؛ تندورهای حکومت فشار زیادی آوردن تا مجددا اینترنت بسته بشه و هر لحظه امکان داره این اتفاق بیفته. اگه کاری مهمی دارید سریعتر انجام بدید. چون هیچی قابل پیش بینی نیست.
✅
هنوزم بسیاری از آی پی ها فیلتره و اینترنت اختلال زیادی داره.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/132301" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
باشگاه با یک بازیکن از سپاهان به توافق نهایی رسیده و این بازیکن داره فشار میاره که با این تیم فسخ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SorkhTimes/132300" target="_blank">📅 12:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
علت کندی شبکه اتصال زیاد است به مرور پایدار میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SorkhTimes/132299" target="_blank">📅 11:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
مهدی هاشم نژاد وینگر ۲۴ساله تراکتور:فکر می‌کنم خط خوردن من ترور شخصیتی بود. دوستانم در تیم ملی گفتند که خط خوردن من برای آن‌ها باورکردنی نیست.بعد از مصدومیت قلی زاده همه فکر می کردند فیکس باشم اما دعوت هم نشدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SorkhTimes/132298" target="_blank">📅 11:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
مدیران باشگاه پرسپولیس در روزهای گذشته با ایجنت پوریا شهرآبادی ، مهاجم جوان گلگهر جلساتی برگذار کردند و خواهان شرایط جذب این بازیکن شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/132297" target="_blank">📅 11:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
شهاب زاهدی که به تازگی بازیکن آزاد شده؛ تمایل دارد به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SorkhTimes/132296" target="_blank">📅 11:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
مهدی لیموچی در آستانه پیوستن به پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SorkhTimes/132295" target="_blank">📅 11:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SorkhTimes/132294" target="_blank">📅 11:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🟡
فسخ لیموچی با سپاهان؟
▫️
به احتمال فراوان مهدی لیموچی به دلیل عدم گرفتن دستمزد خود در سپاهان با این تیم فسخ خواهد کرد و مقصد احتمالی وی پرسپولیس خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/132293" target="_blank">📅 11:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma6HOfcAFIG_9yK_JmzqBa_AXyP9pKjIBUuDOfFO3kI7O2Z2N-6UqYSzosGyMOLQqiE6Lhf4byNKT7HnC7CWdaTALlDxomleD8cKiw0JIUD9jJpyTVZ9oifS5AdSkkZ6yGlMpwwKF5o18C2AczmJauJl1nin0EUsGPO6ZyrnsguvFDPooTYSrTqj1vSt2-fYssVvMKa9j11cscHbSLentLiuX-3CLHN9ldvm0MmLR4CrBhZcZcay5fOOhlK53n87OE-rZF03rg3NVNderiPrdHfRURgtDE6N5-vARvP34kshqRFrkhZukD3c-wl7d4o_gHo3FNF8V5l7fxFgT-lSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهاب زاهدی که به تازگی بازیکن آزاد شده؛ تمایل دارد به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/132292" target="_blank">📅 09:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132291">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
🇮🇷
جهانبخش نزدیک به یک‌ماه است که مصدوم است!
⚪️
مصدومیت علیرضا جهانبخش فعلا مرتفع نشده و این بازیکن فعلا امکان همراهی تیم ملی را ندارد. این در حالی است که 23 روز از مصدومیت جهانبخش سپری شده اما این بازیکن همچنان شرایط تمرین ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/132291" target="_blank">📅 09:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132289">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlPZMLhCxeDHPpgmLEFnBzbyyS9l-urWpIwSwL35G9qoSUrR2Piu4nR_0QTG_oLUdNpQM1hxw7hI3YmywCCwDmeHwiif3OWmJLiYKa1pSEqvWaMZZrLmBAxO8uVWeMY1n80OTxEiylQfxN8ENk2jbZJLVw_hk4aw1Z6cjYZBQOeHiFG-wmYYsh1z9G3nMnOhG8TTeNl6aIY5Y5uS9bGMCxpY9HMFnvx623TV9llQBs2iwWYYQsD1-qvd2HsiY5ig7MwlUcibrhpYAZVrTDLDfmRKuVPF2_KSyjCfSAMuQYUMYt1oa1JTjbLmVYjTu1cB6lJnKylGJv3H9MIlcLPmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد سایت وینکوبت شوید:
👇
🟣
ywincob.com
🟣
ywincob.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/132289" target="_blank">📅 01:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132288">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
کارشناس صدا و سیما : وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/132288" target="_blank">📅 01:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b15265d538.mp4?token=mE6idckFMHl2p5VJD6mHU_QvXEX8FB2KF7Z19GNn6XMk-VWBjqrvkhIEizGHJJHFGfEbW51jnUPOrJx24PSJEx0h9DFuZIvQd4CcpuFQsV214k0c_BXTpx643iIpxIhHvo3y3qaoGVgzDRV-m72BpCtnPMm0IKW0tHx80ZpWi5zOsEIcqep00D-BelWkdhQgrPKyd39Ni0lHu_yRoWcPvLlb4OtEZ0ZKTo1Q0MG8Sykr7cTU0wH26L7T8jJfARJ6_XteDm3zr1gw1rtLpXu9v9eFK3nFQBx8fpwgK6-m5z0Og2dobMuwZ_KR6eiGtToh3iDnIYom5aPgHo-a_3gQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b15265d538.mp4?token=mE6idckFMHl2p5VJD6mHU_QvXEX8FB2KF7Z19GNn6XMk-VWBjqrvkhIEizGHJJHFGfEbW51jnUPOrJx24PSJEx0h9DFuZIvQd4CcpuFQsV214k0c_BXTpx643iIpxIhHvo3y3qaoGVgzDRV-m72BpCtnPMm0IKW0tHx80ZpWi5zOsEIcqep00D-BelWkdhQgrPKyd39Ni0lHu_yRoWcPvLlb4OtEZ0ZKTo1Q0MG8Sykr7cTU0wH26L7T8jJfARJ6_XteDm3zr1gw1rtLpXu9v9eFK3nFQBx8fpwgK6-m5z0Og2dobMuwZ_KR6eiGtToh3iDnIYom5aPgHo-a_3gQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| نورالدین الدغیر خبرنگار الجزیره در تهران:
🔻
همه چیز انجام شده، چیزی باقی نمانده جز امضای توافق
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/132286" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP9t7gk6BwCSZi-M1jXaOAV7N7RExxxNpQbLDnv-FupDmJ_wmIQhO5whOeVnkHEmstpq4o1Pox3QRE-qptI08phKJZLj0sZ1eiv6fHLgSOIAnVhI2ZGmmAt4w5AMxXf7pf-WEDG3-ZtKr8HWy9dqIThfig0sx8ZGs569_YLJmbyy1vs-T6BfsFD3vf7mfQDRjE147q8uMV7VrFxM9fgCnZu2AuTN6ufiBe9dAuL-gONP0Oxtgu-uWSlDu81pBHXMZTUzxgQ27x4rVYXdcAGcAsiQG8HP_CDmcxsDNlUelLMFbcr2c2cIpMHd1Fw4-sJflI-Ry9hA0JLb5Kn50mPVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔺
فیفا اوکی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/132285" target="_blank">📅 00:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔹
سهراب بختیاری زاده فصل آینده نیز سرمربی کیسه میماند
😍
✍️
خبرگزاری ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/132284" target="_blank">📅 00:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
با معرفی نمایندگان ایران در آسیا؛ پرسپولیس شکایتش‌ را به فیفا می‌برد
🔴
به دنبال معرفی نمایندگان ایران در فصل بعدی رقابت‌های آسیایی، باشگاه پرسپولیس اعتراض خود را در این خصوص با ثبت شکایتی به فیفا خواهد برد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/132283" target="_blank">📅 00:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
سرعت اینترنت در زمان قطعی بیشتر از وصل بودنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/132281" target="_blank">📅 23:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132279">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🟥
فروش سیگار
به صورت نخی ممنوع شد تا
جوونا دیگه راحت به سیگار دسترسی نداشته باشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/132279" target="_blank">📅 23:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132278">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
اینترنت سراسر کشور وصل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/132278" target="_blank">📅 23:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132277">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
شایعات
🔴
مدیران باشگاه پرسپولیس با درخواست ویژه اوسمار با مهدی هاشم نژاد ستاره تراکتور وارد مذاکره شدند
‼️
قرارداد این بازیکن با تراکتور به پایان رسیده و هم اکنون بازیکن آزاد است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/132277" target="_blank">📅 23:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132276">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/132276" target="_blank">📅 23:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132275">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🟥
تیم ملی ایران برای هر بازی جام جهانی فقط چند ساعت ویزای ساعتی آمریکا را دریافت می‌کند و بلافاصله پس از مسابقه به مکزیک بازمی‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/132275" target="_blank">📅 23:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
یک بخش از صحبت مهدی تاج اشتباهه.
🔴
اونجایی که میگه اگر‌ کمپ تمرینی تیم ملی به مکزیک بره، مشکل ویزا حل خواهد شد!
🔴
ربطی نداره!
🔴
شما کمپ تمرینی رو به موزامبیک هم ببری، برای برگزاری سه مسابقه باید وارد خاک امریکا بشی و در نهایت به ویزای این کشور نیاز داری.…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/132274" target="_blank">📅 23:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
الان چیو دقیقا وصل کردید؟! مردم ۹۹ درصدشون قطع هستن…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/132273" target="_blank">📅 23:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
ارزش امیرحسین محمودی ستاره ملی پوش پرسپولیس به 500 هزار دلار رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/132272" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
به روزرسانی جدید :  اتصال مردم به اینترنت بین الملل به ۸۶ درصد سطح عادی رسید و در حال افزایشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/132271" target="_blank">📅 22:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/132270" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULdfoPx2cNdSvp8QRRttpZonVm0MM26m_AXZqQ2C701tA_gPfq-GcpCmUPFrA_5Rkri_03ISclADl1twMk9anh5_WSvTIVYYNHghWg7TboUayQ7WAGJ4GjbR1llf9YJr52ETLmcsw6hiMixFZXDgPpv8IhZGDkCt2fa6p0ok4tA9D1QStrEaBPE1etPzqqMdSiDwAMlOWd0y4PnCMlYj5QDgbzdUjodmoNylIAyWGdTRFujkWn3kYBSR6vx-AfAp3NSccwu9CcfzXr2UFEMWwUkjQL-6cPcuK2uZlSF5l_O-X1MA0KPpHVLfe98bHHJvsZ2SsCgIcEJiXbK80AiGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/132269" target="_blank">📅 21:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIn3czSOufU-X95b_m9hG9ez6Hmoyk7nA9ACOG-JfR_Y5LNTt4qvMRaYdVxFqyr4yXjBWtgBAe48Y0Dts6PsJwDkVfc4yQhW-NugGSIOxf_Iib0aHPuwCZvhwgqdM4tsMwY1THxke3KBEdzjpGFJUnZkC0aBamr0Kmf7KkbOmkd7az10ZZjreKI0OYYUpmkGBQI31lA_LC9OykmrYWOr9PcVL0rWub2MSw49Mofc4FjVUjVlac60nywxtsENbPB9XKAqvP1Bup985WyKv3dT2uK0zuJdFi7uLn27NYhsYwMc53Bq6guDZWSI4MUTe63izk7d7uQhEroQrAye42H6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/132268" target="_blank">📅 21:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
💢
🇮🇷
🤝
🇺🇸
📰
الجزیره به نقل از یک منبع آگاه: میانجیگری قطر به توافق آمریکا و ایران بر سر دارایی‌های مسدودشده تهران منجر شد!
🚫
به لطف توافق بر سر این موضوع که برای ایرانیان از اهمیت بالایی برخوردار بود، احتمال قوی وجود دارد که توافق میان آمریکا و ایران فردا اعلام…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SorkhTimes/132267" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
وزارت ارتباطات:
🖍
اینترنت گوشی های همراه هم تا ساعاتی دیگه وصل میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/132266" target="_blank">📅 20:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
‼️
وضعیت اتصال اینترنت بین‌الملل کشور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/132265" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZYoAZmSDXTRvju4smjyZVri3RFgNw7dZhAIxOFdiTv8DjiHmU0axuiodJ0acRu_y9_mtnxEGXvdkgcrKPw3ajXTX4T7erFQCi5_KvnWKGJbCz-g2Vis9iYm_xL4K_UVgAA4Ok3uoK6THtzueUFqveoRa7W4qT5daZABqH7AXhNUOZ0MIwnjG40fYbbzPG5yNxCmGwd6xL77HkM90-RwlYilF2TQ_PVHwaNxkcEQnlZlZHiedA22Ype7AeXu75xYr-uJ6S2szn1utiLkdVSfPaUYiCWLrzgX_TO_joMlO8nbhwh3ocza-1XyLtneIMOPgvOrTJI4NDCRCepJWjCG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
وضعیت اتصال اینترنت بین‌الملل کشور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/132264" target="_blank">📅 19:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔽
وزارت قطع ارتباطات:اینترنت همراه، امروز (سه‌شنبه ۵ خرداد) وصل می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SorkhTimes/132263" target="_blank">📅 19:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
تسنیم : یحیی گل‌محمدی به جز باشگاهای عراقی یه پیشنهاد مالی خوب هم از تراکتور داره و ممکنه بره تبریز!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/132262" target="_blank">📅 19:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzM_glBF7r-rjWvQgmF1L2z-yse1H7XVkoFg0t38q4PGyF-VDxUzzaG0kSVhzTSdvAM3qjwCLANWyhPGWXY3pxrwvK1mJaFWVrv75QzPlXyHaprdDABU54U6fRHWr9yfuEh0numC9DzHsm-GyV_z0fqyhTkT4gE3KxLoziZPcIH8PUgdFnfrEePzMm77PgoKUcdRZVWFExARI0MQ7HvwUT_hzGMGhY7D7yLytfR9k8xgdNRXDnH7eZcaHPDUab9RnPlIBFCwEsykDV5ooBAI2EwSDJzRw_PImR9QS82OmEfeEX2blBk5rg5hCDnhjYk_qobl7ov9lcMf5EOaYnqwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شایعات
🔴
مدیران باشگاه پرسپولیس با درخواست ویژه اوسمار با مهدی هاشم نژاد ستاره تراکتور وارد مذاکره شدند
‼️
قرارداد این بازیکن با تراکتور به پایان رسیده و هم اکنون بازیکن آزاد است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/132261" target="_blank">📅 17:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132258">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
پس از ۸۸ روز قطعی و ثبت رکورد تاریخی ۲۰۹۳ ساعت انزوای دیجیتال، نت‌بلاکس لحظاتی پیش تایید کرد که اتصال اینترنت در ایران در حال بازگشت است.  وضعیت فعلی در یک نگاه:
🔹
اینترنت خانگی و ADSL: اکثر شرکت‌ها وصل هستند.
🔹
اینترنت TD-LTE: ایرانسل و مبین‌نت وصل شدند.…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/132258" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
تیم فوتبال دهوک عراق به یحیی گل محمدی پیشنهاد داده اما یحیی میخواد تو ایران مربیگری کنه!/فارس
🚮
امپرور جان لطفا هر گورستونی میری طرف های خیابون شیخ بهایی آفتابی نشو…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/132257" target="_blank">📅 17:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
دوستان از برخط به online شدنتون مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/132256" target="_blank">📅 17:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
دوستان از برخط به online شدنتون مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/132255" target="_blank">📅 16:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
خوشحالیم که دوباره آنلاین شدید
❤️
🔴
خوش برگشتید؛  امیدواریم تا شب دیتاسنتر ها هم متصل شوند تا کسایی که وایفای خانگی هم ندارند به اینترنت متصل شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/132254" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
نت بلاکس:
🔻
نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SorkhTimes/132253" target="_blank">📅 16:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QAvmKOMUi5gtTOEwti97bg1QXFkU9xgoPjcBBJdkFpxk4OubldzCrgMH-Icb1NiP5jT5jz4KoRDqCOe9bIK2nq_4a_TQiVy771SvuVbRehz_b407noTzj6byHe2nHDTukYB4OgTOHLPw1vqjh3FRhxXV44dhVz00IhCJqU0xPJb9lvV3OlSzX_3Pfl4k69MK5OVEMq-g9GMg2PFRyxiuTbS6I739T-q0pD7YAKxoMPjnftHVeiqcsaBwXZYAtgkW9cchAa8TXEJSZv_KuSazzmg1ChJAUAGeGfzTPPO2nJWcJ7mJ7ieLp9OeXaMp9-PkTDRbTCj0Mn5L56y31ELeJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نت بلاکس:
🔻
نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/132252" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
خوشحالیم که دوباره آنلاین شدید
❤️
🔴
خوش برگشتید؛  امیدواریم تا شب دیتاسنتر ها هم متصل شوند تا کسایی که وایفای خانگی هم ندارند به اینترنت متصل شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/132251" target="_blank">📅 16:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132250">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SorkhTimes/132250" target="_blank">📅 16:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132249">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIbpjCwre3tAz3Q5jV_Nu9JCHXfI4N_mekaT3UMCSjf2BDFfki-A07UjziA1tLT2YQmuquJG0PKQURRm6fVGV-MHpKM7jBOJxXoEoiyH43JQgZ3vuk_ETgqboo65elC2AEAHzU1qvBFpxbAw8nFHbNdigvi8fgiqTSNDMvLTeqQi_AUMR_gUqIzuN9tyfJICWtk5aDmMZ3ob8hxdo3aAQP_gSzZT5sjMDK-KTKKm1_ws_8IwNSWVSQ39m87jZUiD3_St-D93nsP0vkQdDZ1LO3Ul7HSSxPzX6dsRUGZPRWBUfn1mRUxJfPFIGRYxDjSTbBsL6_dZ1NJDMYpxAgoaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
بازگشایی اینترنت به دیتاسنترها رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/132249" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132248">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
نت خونگی وصل شده .تست بگیرید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/132248" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132247">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا ۲۴ ساعت آینده
🔺
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/132247" target="_blank">📅 15:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132245">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoGxFW1_hMmkjKD-ss7qUTFeypKBrY0fhJKEQmCcL-ToBW-jd2ss0-QklHOkE7vpmySe4GWrvwX5R5Fz_vcuZCajCebUnZ8WJz44dXYYVy1ro2QXNr8GuPVaQBvXoL95TAXiQDa0S-m_vcpZZecUJimmhshkAcP5M84I2tor6ercY0q_rQYl2hwb4TrMWo7Sr-mQ4BOmCubzhDc4Fk3qip-Exu8Y6PSWIvbcY2D0jbZi4ts9nZ9gnfhhV7uA-lGPAYkZae-GgY0THBiN6xFb-WBny4Bb1lTxrIqlzcIM8_MvWVIczrg4rOOpm0oru1ucbMwHtpTM-34ebPyL9bFkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
فسخ لیموچی با سپاهان؟
▫️
به احتمال فراوان مهدی لیموچی به دلیل عدم گرفتن دستمزد خود در سپاهان با این تیم فسخ خواهد کرد و مقصد احتمالی وی پرسپولیس خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/132245" target="_blank">📅 13:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132244">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا ۲۴ ساعت آینده
🔺
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت:
🔺
دسترسی کامل مردم به اینترنت تا ۲۴ ساعت آینده میسر می شود. بر اساس اعلام یک منبع مطلع، برخی سرویس‌ها و پیام‌رسان‌های بین‌المللی نیز به‌تدریج و در چارچوب فازهای بعدی بازگشایی شبکه، در دسترس کاربران قرار خواهند گرفت و در فاز اول بازگشایی قرار ندارند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/SorkhTimes/132244" target="_blank">📅 13:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132242">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=Uum4U7qs8p4r3wp6--_PMlHUoCt9_66gInz6MY7pCreTnPA7lYjKX1lBygtVtixLSD-N145hW0QTGkSFTD6pAAQgYz4Qon_O2FlvLYBG4K1kz8DYTb5PpuBe1A9KswGlzSOV_kkuWWRE8Z6HZqYXiMcBKPCKp8p6pLeOMZhtRRlKf6M7zM5ModSNGsro0ZUMCgJtGvQzn2JUATRsfh63ol2DqiixI-SM243jRbORUyOgFFNY5d5aKWf_eAb12XehvVUhpgEYxHIbb-o5w87-yYUfILmJh62Pd5rdm-AZUsx1CKbxCJ1xohxArpJ0JIM3G-5aRCXmDr6Ymvx__eVFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=Uum4U7qs8p4r3wp6--_PMlHUoCt9_66gInz6MY7pCreTnPA7lYjKX1lBygtVtixLSD-N145hW0QTGkSFTD6pAAQgYz4Qon_O2FlvLYBG4K1kz8DYTb5PpuBe1A9KswGlzSOV_kkuWWRE8Z6HZqYXiMcBKPCKp8p6pLeOMZhtRRlKf6M7zM5ModSNGsro0ZUMCgJtGvQzn2JUATRsfh63ol2DqiixI-SM243jRbORUyOgFFNY5d5aKWf_eAb12XehvVUhpgEYxHIbb-o5w87-yYUfILmJh62Pd5rdm-AZUsx1CKbxCJ1xohxArpJ0JIM3G-5aRCXmDr6Ymvx__eVFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کانفیگ فروشا وقتی از خواب پا میشن و تلگرامو باز میکنن که خبر هارو بخونن:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/132242" target="_blank">📅 12:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132241">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
وزیر ارتباطات: با دستور رئیس‌جمهوری و پس از برگزاری ۳ جلسه فشرده کارشناسی، فرایند بازگرداندن اینترنت کشور به وضعیت قبل از دی‌ماه ۱۴۰۴ آغاز شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/132241" target="_blank">📅 11:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132240">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
وزیر ارتباطات: با دستور رئیس‌جمهوری و پس از برگزاری ۳ جلسه فشرده کارشناسی، فرایند بازگرداندن اینترنت کشور به وضعیت قبل از دی‌ماه ۱۴۰۴ آغاز شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132240" target="_blank">📅 11:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132239">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k12Ydv_QyrP7p_LJbxWQisM1jU767JOUMftLe4GtC6Ujg8y7yxLtqQZOH6EVfQLUWC13fR9Vmngi3yHti8L6mucHhFpv0WrvLt1-STqmS5_JtB143IupkCBbO57rxdxYr8Z9s97uDAB_YOzc_FADhYyDAEjdgs__gOT_4QZxPV7LCCmutPbpB8Mai3o5s5zqqMoF3FKMXlyp2aqjjZsHR0D2duInCq8g5kA8_eilqrLIBkMDPR4DJXU2P-t3Bi_MmbUphdK7RfMXf0apg_GxKceBFaHcuzGnPk0Y5tZR8hrf7CloPGFA7kthXrRCXKpMM6G8YBG0wqkG_QsUTMolPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت به دیروز وضعیت اینترنت بهتر شده و از ۲ درصد به ۳ درصد رسیده
😂
خوب نتیجه میگیرم در آستانه بازگشت نت هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132239" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132238">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
ایسنا:   دستور باز شدن اینترنت از فردا اجرا میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/132238" target="_blank">📅 10:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132237">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
شهاب زاهدی قرارداش را با باشگاه آویسپا فوکوئوکا ژاپن تمدید کرد و خبر از بیخ گوشمون گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SorkhTimes/132237" target="_blank">📅 10:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132236">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulZt61_ZMdS2czuPtpi34uL3T2mMSYqVT2tFsYqTDfXuiKnbioxgX2AJ76MWBDaenBQ_VSj4yoi7lDwBY4OC1KKa6TpLgAMKCJZMEW-tlp67OVTgYILFDUTwbaFKoM9MCctbhEqJJF4pkZwvT2H02wSjz6cXfhr5MNkN8eWO86EI85-4FKq7L3JrH9Ntd5MFrs5CNYpxAChaySJAMqnWQmA34DOU9j7IHPsocIR85yHPYEcyMWWDL3YNu24UCSoic090JIpATGXweL0Kh1LPllknJYQvHdDTEZGw-j7p-unLWAvAcyGwr4m73lVYzNFrRjN1few8St0WQFYAUCW1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/132236" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132235">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvSahx_8PyGXNxwyYT4Yy9CGfaRwbe06kOil8AbUFTOhvAUbVhDhe7F85Yqb6oOhroXC4tnNIqhoIL_SVhX-sB0tqdsgWKsh0CF1F5cplQcDc7P8syWo110TnoXEEM4_ejwzojqiSGSFHbb-ophZQdk9w6BRwZvoUVAfsN4YKMTGJrIdOe969Ng60O7SPVL6QMhdrMt2sLNswRBVmjeyY3HHpd1R1T2qmAkl3ICe3OAzRtKKWhbMl1TK4nzQpJyo0AsqcP5yDaLH6HJwkUKwZ5uXXtUvzQp1Y5oyL5H5Stu-kuymk3ZmpJmzWSneHal8bFIs1QqnkS3zmyhPOGWRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صفحه اینترنت پرو از سایت همراه اول حذف شد
✅
شکست رسمی اینترنت پرو
همراه اول صفحه ویژه اینترنت پرو رو حذف کرد
✅
روسیاهی موند به اونا که خریدن
🖕🏾
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/132235" target="_blank">📅 10:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132233">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AahBFHHiP8oh1_1sEV9-cJXyjvq7gtZXVxvvJPR55kaHxyLCQ_2rn3PY3Mk2nucysCFDbFk4azt0xJH3C_RsQq90RzHS_R0CXo8ykc5fJGeLupM0DkO6Y4LWciy5y3wwXX4rvEgXBW9XZhMEFJwUQhjqcxgcv8uPLdTOP15YSRdoX16pGcLpjAu-7RaM4hPEB-t4sjca88NXeqiMJx_T9f6Uksvy3dugysydnbEvjmptwdXGqgwWRgFhtkxnrMKA4yDXFiSSw5m1ZToTNh-t7R2Pn4dNkaKVwRlc3NnOMbfL7xJQ1_W63RhW2p0orh3jT-ttBSpAYhkXfsk6nTFFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از بین شهریار مغانلو و علی علیپور؛ یکنفر از لیست نهایی تیم ملی برای جام جهانی 2026 خط خواهد خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132233" target="_blank">📅 10:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132232">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
ایسنا:   دستور باز شدن اینترنت از فردا اجرا میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SorkhTimes/132232" target="_blank">📅 10:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132231">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXb-ttY38QW-CELTln9IWa7pnKk8XCbNaCe56Z4S9xL0uv3GyM_o413GaheuwVw_d9CF1tNKNLXr9eIGz5hhRhziGUUZvkc1Hyj-wbiibL0rzsP9qYwL8abFnU7TSsxJpqepyGHjnJL_3s_y3Y-4sJ1gL2Px2bKpNUPry66lh2mANpUbLa3StUjYwp6kCXOc9ysPI6ghf0JQchLfzEqXJ_WgGb-D314O0g8YWsalfzbIKsTZgwjZ6c9y9kQl0nLIgnA1O6TfQ8QtYbTBj88AqFhhAAF4t7Vwb4VT6J-xnSeXGpLnjL6S1VThNAvR29hfraAQmphYKQNSl8zpkIe8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارزش امیرحسین محمودی ستاره ملی پوش پرسپولیس به 500 هزار دلار رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/132231" target="_blank">📅 09:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132230">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg7Yu_XVyKggnFclmFzqOP53bE_1FdtLgWh7iEQbR1YpJrMKq9T0--tZYqlXNhMEulgp7t6Is23dNgDzO_2io47eNVVa0ie6VuhstttUEyWQ5SCad3prQU3Ug3r3bfjVlZPyUmO9Fk_vAzaTG9ucUVYjEcnit_wHz5Qmnerbo_8jm7tJlYUP7Cs9Y8e-5A7DPVz-tYmiEkO5EEE2U1rj0xKn9SZ8XvTLrtWGpZKkJbAhNsfskwEtHSYneVZ6dYiZaaEeWC6SsMeFJn2F_uTghxFSMc5w5LxlEH5TsT0Tc-0JN0k6vShW3lsCfuPP2MYO99oD9SPQUEYRm7u1zHLC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایعات حاکی از این داره که سردار آزمون به زودی به تیم ملی برمیگرده....!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SorkhTimes/132230" target="_blank">📅 09:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132228">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a864573491.mp4?token=M_ZZ8GbVn8jMh4ATSNHXpuiroYgn8u2oChr6iV0erGgIuuZs5OB_PC0_kHQGhYHYOdYy1XL8eCAbwKrqeP8_AKz-HOE88c0PNosSEJsSEuPpGmRVoeem4J6Q7wDpjy7FD-L3Y5fWqPZjed_Bf1bWBbwGHMRYHsRVYCypMltlRws5pkFSFlADVK7Pv9BAo12xIB0Dr_wQq_NE78lhJy8zNFH49BihvsFGoTq6M08Yudw2OH58eIMxRR2x07ICDeN3GpI5FLThN_nUTpM3R_zLYEU9H8PITmPU2rUyUWoMeAziGmt-bOUqqP0_3PLusY-THdFP71quNRLd3t0ecjyCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a864573491.mp4?token=M_ZZ8GbVn8jMh4ATSNHXpuiroYgn8u2oChr6iV0erGgIuuZs5OB_PC0_kHQGhYHYOdYy1XL8eCAbwKrqeP8_AKz-HOE88c0PNosSEJsSEuPpGmRVoeem4J6Q7wDpjy7FD-L3Y5fWqPZjed_Bf1bWBbwGHMRYHsRVYCypMltlRws5pkFSFlADVK7Pv9BAo12xIB0Dr_wQq_NE78lhJy8zNFH49BihvsFGoTq6M08Yudw2OH58eIMxRR2x07ICDeN3GpI5FLThN_nUTpM3R_zLYEU9H8PITmPU2rUyUWoMeAziGmt-bOUqqP0_3PLusY-THdFP71quNRLd3t0ecjyCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
| ترامپ:
🔻
«اورانیوم غنی‌شده (غبار هسته‌ای!) یا فوراً به ایالات متحده تحویل داده خواهد شد تا به خاک آمریکا برده شده و منهدم گردد، یا ترجیحاً با هماهنگی و همکاری جمهوری اسلامی ایران، در همان مکان منهدم شود،
🔻
یا در مکانی دیگر که مورد قبول باشد، با نظارت کمیسیون انرژی اتمی یا نهاد معادل آن بر این فرآیند و رویداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SorkhTimes/132228" target="_blank">📅 01:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132227">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔹
کالدرون: کاش می‌شد کارم را در پرسپولیس تمام کنم
🔴
اگر می‌ماندید پرسپولیس قهرمان می‌شد؟
فکر می‌کنم تیم در آن زمان شرایط بسیار خوبی داشت و ای‌ کاش می‌توانستم کاری را که شروع کرده بودم را به پایان برسانم، اما متأسفانه این اتفاق نیفتاد. به نظرم ما تیم را در مسیر درستی قرار دادیم و یحیی گل‌محمدی هم پس از حضورش کار خوبی بر پایه‌هایی که گذاشته بودیم انجام داد.
🔴
پس به خوبی پیگیر اوضاع پرسپولیس هستید!
در این سال‌ها تغییرات زیادی در سطح مربیان و مدیران باشگاه رخ داده و پرسپولیس همیشه باشگاهی پرتحرک بوده است. بازیکنان زیادی هم تغییر کردند؛ بعضی از بازیکنان مهم زمان من مثل شجاع خلیل‌زاده، مهدی ترابی، احمد نوراللهی و علیرضا بیرانوند از تیم جدا شدند و برخی مثل حسین کنعانی، علی علیپور رفتند و دوباره برگشتند؛ بعضی دیگر مثل محمد انصاری امروز مسئولیت مهمی در باشگاه دارند.
🔴
خبرهای بود مبنی براینکه باشگاه پرسپولیس در پائیز سال گذشته قصد داشت شما را دوباره بازگرداند؛ مذاکراتی صورت گرفت؟
همیشه شایعاتی وجود دارد، اما شایعه فقط سر و صداست. تنها واقعیت این است که در حال حاضر من سرمربی پرسپولیس نیستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132227" target="_blank">📅 01:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132226">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f501face.mp4?token=Rv63Ek_C0whMZsT_KkpmNkAL3biymI5g9H6JYY615unvFPjyeOTOHF11x6VYFf8GqXUEcbV-99d-PTiR3NWxqPlsjbvpuzhNI8FWfloezMSnTaRPu5r49ObWu7RnX9YBEQfebsUeDeQB7BM7_Ki7_28ugVU6WY8_FCKTznUMz4bxM3rWs50rNyVkd0tmPfH37JdfX6hou9jpYOqOQhOmJ1-l2VL80naZMjY95c8fZ0Illa-GkzQbzI2DUzbQAHvFqekeHFGYX8wGabZbgYlAt1yx_u4FqTk1i4hpnm_oZfoNZWfi2tciPMNElCM8rxbfZqvh-qf8z68XwsTnr0GmXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f501face.mp4?token=Rv63Ek_C0whMZsT_KkpmNkAL3biymI5g9H6JYY615unvFPjyeOTOHF11x6VYFf8GqXUEcbV-99d-PTiR3NWxqPlsjbvpuzhNI8FWfloezMSnTaRPu5r49ObWu7RnX9YBEQfebsUeDeQB7BM7_Ki7_28ugVU6WY8_FCKTznUMz4bxM3rWs50rNyVkd0tmPfH37JdfX6hou9jpYOqOQhOmJ1-l2VL80naZMjY95c8fZ0Illa-GkzQbzI2DUzbQAHvFqekeHFGYX8wGabZbgYlAt1yx_u4FqTk1i4hpnm_oZfoNZWfi2tciPMNElCM8rxbfZqvh-qf8z68XwsTnr0GmXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بازگشا سخنگوی باشگاه پرسپولیس: پرسپولیس برای برگزاری مسابقات اعلام آمادگی کرده است هم زیر ساخت داریم هم پشتوانه مالی
🔸
این نمی شود که بعضی تیم‌ها بیایند نامه بزنند که ما نمی توانیم در لیگ بازی کنیم و بعد همین تیم‌ها هم توسط فدراسیون برای آسیا انتخاب شوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SorkhTimes/132226" target="_blank">📅 00:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eemiuGMy86wjK6HuVL50NFlQA9IL66So5z2yWk2sooalEIsTf0u15zT_QNbW6oSzo33VLclhV15Vpfpv2AJVD80uApNOMnL5b4SejltrASnhyyBHyqM40VVEN-WmnM2pKodJrpaFW6i-n-JKTuz1qrLFsuDSILpopR61IL_mJxvclXfBihw-VMiqjA1_lboYb_sQeJB3Em-qr7yYgmJ49LRVmVeWR89nolE1VYc7sfrHJN51LGb-uhdZyxUHGQacq4ndGnUsW4Wf-kmBvscd2T0XmJBBswESqiGG71lBZ-lJSCgU9fR6vaptBnFJYZ1WBa8xoN8U7iNi-6_i2p7fTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق آخرین آپدیت ترانسفر مارکت امیرحسین حسین زاده جای ارونوف رو در صدر با ارزش ترین بازیکن لیگ برتر گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/132225" target="_blank">📅 00:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132222">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تو بندر عباس صدا توافق میاد</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SorkhTimes/132222" target="_blank">📅 00:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132221">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
الجزیره:  احتمالا توافق بین آمریکا و ایران، فردا (سه‌شنبه) رسما اعلام میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SorkhTimes/132221" target="_blank">📅 00:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132220">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تو بندر عباس صدا توافق میاد</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SorkhTimes/132220" target="_blank">📅 23:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132219">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/132219" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihKbBpTP9yw05wFjrVkCbz5WL9a38IRZfeKf8e9kACIyeO2mRV2JGPw2CTKcQhT-lBeBpSvYd34UUwppysjxJ4ZvvySYK2vesKqL-ohOgX9fdQ9xQoc5bbIJF1ROmrQhwXIlHmyRe88yn7SykMX6QyPoVAOkxFc_O8aGBYKHMLoKQHSvaONtgx00diwKDTSQW0wkl-BQhNFdHDSKoy1O5m6inFpRkXzCHHArS-4cZldOXgzJqgELiTh6rZyTDi8b7_KmXwqpdWVLdsNJR2DML331G9yfEyX3FW9d66inAbqOFSvQHANFIadLKg1_wTEFXI2EyhVvHYe81oTGSijigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پیام‌ نیازمند در جدیدترین آپدیت سایت ترانسفرمارکت با ارزش ترین گلر ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SorkhTimes/132217" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132215">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
👈
نورالدین الدغیر خبرنگار الجزیره: احتمال دارد اسرائیل پیش از هر توافق ایران و آمریکا، دست به یک عملیات نظامی بزرگ در لبنان بزند
🔴
با هدف استفاده از فرصت زمانی باقی‌مانده تا توافق ایران و آمریکا.
🔴
یا برای به شکست کشاندن توافقی که بر توقف جنگ در جبهه لبنان…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/132215" target="_blank">📅 22:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132214">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
واکنش باشگاه پرسپولیس به معرفی سه تیم اول جدول به عنوان نمایندگان ایران در آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/132214" target="_blank">📅 22:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
و بلاخره بعد از نود روز وصل شدن نت بین الملل و شاهد خواهیم بود ...حال الان کانفینگ فروش و خریدارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/132213" target="_blank">📅 22:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etLf6jRoyl9p14gvm2IIqQHk1uwMRHJYqF7e2WhCpcenYF8HyqGWZgZwYuGW0h-dvf1D7fie-0A0m9YTio_mdtuunElIYU65QqIRzwhrs-WKZ5EXiEOp_3RK5q-rzCtlVMIN4c-CILhDKtFZ88asG0UBq3J8thvcT6e9zpS3Ain3LbDa3v56qQl5dLx7-wQ-1X1Pox-k2nQQwSYeShP5pSs6GtY8O5oN0oRDQyhaByXSrp05p2d0ow19fXe9T6i6Sycvh7-srIT-5KCnIekNPfZ5yQ5VLc4Kw8PIf14wTx5Bkq5olD9a_D49udPiuwNF-ZYwbWm-cwW0L4AizEoO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
واکنش باشگاه پرسپولیس به معرفی سه تیم اول جدول به عنوان نمایندگان ایران در آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/132212" target="_blank">📅 22:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
🚨
خبرگزاری های داخلی خبر دادند که اینترنت بین‌الملل از فردا به تدریج در سراسر کشور وصل می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SorkhTimes/132211" target="_blank">📅 22:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132210">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
فووووری/ مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132210" target="_blank">📅 22:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
ادعای عاصم منیر:
🟢
توافق ایران و آمریکا در آستانه نهایی شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/132207" target="_blank">📅 22:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
فووووری/ مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132206" target="_blank">📅 21:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132205">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ورزش سه: پرسپولیس از رقابت های آسیایی کنار گذاشته شد و استقلال، تراکتور و سپاهان (درصورت تایید مجوز حرفه ای) آسیایی خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/132205" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132204">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
خبرگزاری فارس: مسعود پزشکیان فردا سه‌شنبه مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه را امضا و به وزارت ارتباطات ابلاغ می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/132204" target="_blank">📅 21:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132203">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
تغییر نظر عجیب فدراسیون فوتبال با پیشنهاد سازمان لیگ
❌
در حالی که طبق ادعای مسئولان ارشد فدراسیون فوتبال قرار بود فردا (سه شنبه) جلسه وبیناری بین مهدی تاج و معاون کمیته اجرایی AFC  برای گرفتن فرصت مجدد برای معرفی تیم های آسیایی برگزار شود، هیئت رئیسه فدراسیون…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/132203" target="_blank">📅 21:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/132200" target="_blank">📅 20:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
خبرگزاری تسنیم :
🔴
دستور رفع محدودیت های اینترنت بین الملل تایید شده و فقط به تایید نهایی پزشکیان نیاز داره ، در صورت تایید اینترنت بین الملل تا هفته ی آینده به حالت قبل جنگ برمیگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132199" target="_blank">📅 20:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132198">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی…</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132198" target="_blank">📅 19:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
تغییر نظر عجیب فدراسیون فوتبال با پیشنهاد سازمان لیگ
❌
در حالی که طبق ادعای مسئولان ارشد فدراسیون فوتبال قرار بود فردا (سه شنبه) جلسه وبیناری بین مهدی تاج و معاون کمیته اجرایی AFC  برای گرفتن فرصت مجدد برای معرفی تیم های آسیایی برگزار شود، هیئت رئیسه فدراسیون فوتبال امروز تشکیل جلسه داده و ظاهرا با معرفی سه تیم اول لیگ برای مسابقات آسیایی فصل بعد موافقت کرده است.
❌
این در شرایطی است که هنوز جلسه فدراسیون فوتبال با AFC برگزار نشده و سپاهان به عنوان تیم سوم جدول فعلی مجوز حرفه ای کسب نکرده و پرونده این باشگاه در کمیته استیناف بررسی خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132197" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
میزبانی مکزیک از ایران
⚪️
«کلودیا شین‌بام» رئیس‌جمهور مکزیک، رسماً اعلام کرد که تیم ملی فوتبال ایران به دلیل محدودیت‌های حضور در خاک آمریکا، در ایالت «باخا کالیفرنیا» مستقر خواهد شد.
⚪️
با تایید دولت مکزیک، تیم ملی ایران شهر «تیخوانا» را به عنوان مقر اصلی و محل تمرینات خود در طول مسابقات جام جهانی ۲۰۲۶ انتخاب کرده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132195" target="_blank">📅 19:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی جدول به آسیا معرفی خواهند شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132194" target="_blank">📅 19:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
در حالی که فوتبال ایران تلاش می‌کند استانداردهای سخت‌گیرانه کنفدراسیون فوتبال آسیا (AFC) را برای دریافت مجوز حرفه‌ای پیاده‌سازی کند، اخبار واصله از باشگاه سپاهان اصفهان نشان می‌دهد که این باشگاه با چالش‌های جدی در مسیر دریافت این مجوز مواجه است. عدم بارگذاری به‌موقع مدارک و وجود بدهی‌های انباشته، اکنون باشگاه طلایی‌پوش اصفهان را در موقعیت دشواری قرار داده که اعتراض به کمیته استیناف آخرین تلاش آن‌ها برای خروج از این بن‌بست است.
🔺
سپاهانی‌ها اما در حالی به کمیته استیناف صدور مجوز حرفه‌ای پناه برده‌اند که عدم بارگذاری به موقع مدارک توسط آن‌ها کار را بسیار دشوار کرده است. سپاهان که حالا چشم امید به کمیته استیناف دارد، بسیار بعید است با قصوری که انجام داده بتواند مجوز حرفه‌ای خود را از کمیته استیناف دریافت کند؛ زیرا این باشگاه در بازه زمانی مقرر اقدام به بارگذاری مدارک نکرده و حالا کمیته استیناف هم همین موضوع را مدنظر قرار خواهد داد.
🔺
سپاهان که در جایگاه سوم جدول رده‌بندی لیگ برتر قرار دارد، با توجه به اتفاقات رخ داده در جنگ سوم، اکنون با مشکلات مالی نیز مواجه است و باید دید چه سرنوشتی در انتظار این تیم خواهد بود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/132192" target="_blank">📅 17:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
پرشیانا اسپورت : لیموچی دومین بازیکن سپاهان که از پرسپولیس آفر دریافت کرده و اگر شرایط خوب پیش بره ، لیموچی به پر‌سپولیس میرود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132191" target="_blank">📅 17:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132190" target="_blank">📅 16:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132188">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYhda_xqneapcwYC74Y_LCBeRtg7X5Qs2cFQF9-rLGT1pMaU0Y78h83iOKTw86rn0vv8uQw4iP73KK6HGcapCVP404cj4BWEpcLyDOzeatI0DvHkhPUqfKW4MNEscSPRmbd-Ud_wweQcdCuT3z3OYMEVHTU4WP3Z1b-5HANoooEleSBlwM0aUiB1Uy3J8yU38S1lRyE6LMARFJjLhnCCcr3xZonwhOZZKSIc-yEanaDptP-4uRHJd1T7Tx-NAJGGrj4APUyD-3rHbZtI0XZo4Mu5w_DN_3truHnk2EJCESAfHXyJKIc5GZp_FI8eUbI9LCThqEXg1t5sHigXHCnq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔽
فهرست ابتدایی ازبکستان برای جام‌جهانی با حضور اورونوف و سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132188" target="_blank">📅 16:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132187">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭕️
#فوری | خبرگزاری رویترز: مذاکرات در دوحه عمدتاً بر تنگه هرمز و اورانیوم غنی‌شده با غنای بالا متمرکز است
‼️
🔻
رئیس کل بانک مرکزی ایران بخشی از هیئت اعزامی به دوحه برای گفتگو در مورد احتمال آزادسازی دارایی‌های مسدود شده به عنوان بخشی از توافق نهایی است.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132187" target="_blank">📅 16:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فاکس نیوز: امروز پزشکیان ، قالیباف و عراقچی رفتن قطر تا درمورد پایان جنگ و توافق گفتگو کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SorkhTimes/132186" target="_blank">📅 16:28 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
