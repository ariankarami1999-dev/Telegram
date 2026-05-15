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
<img src="https://cdn4.telesco.pe/file/Fm76Vp1NBMKuN9McGFA9E1OfbuIneL1Zl5sky832gz0NsBNOzrRvKveNfPmpgbhMKkZHVBJljXNb3vCrB0H0jb1Z5dJFASuzgTEirEGMMUKGGkyOggdVjFRJmeeOFnkReHbwmHpp7YNyyQSZJHyqlLGagj-P1lx2RmjI4_Y4v1JpE6bsAthiMzfxm2LKxRF_VD-pHQb14IbhZtp-GLLjORrQhcmlwkZLc4KkNkNZTskrcedhqSRRVaCC28MbD52G2OTxTgnDADbfkq12A9AscSJyDkgIsOqpFvFy-J25q2v-fgzqvYd76Y1TpSin0UA91cbD9cXidnxiLV9PKLd1PQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 18:30:12</div>
<hr>

<div class="tg-post" id="msg-131691">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🛜
سرور نامحدود Open VP
موجود شده فقط 1.5T
مخصوص تلگرام و واتساپ
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 96 · <a href="https://t.me/SorkhTimes/131691" target="_blank">📅 18:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131690">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
ویزای هیچ یک از بازیکنان تیم‌ملی ایران تا این لحظه صادر نشده است
❌
برخلاف تقریبا تمام تیم‌های حاضر در جام‌جهانی که همگی ویزای خود را دریافت کرده‌اند[بجز عراق]، تا این لحظه ویزای هیچ یک از بازیکنان تیم ملی ایران صادر نشده است.
⚠️
مهدی تاج قراره در ترکیه با…</div>
<div class="tg-footer">👁️ 126 · <a href="https://t.me/SorkhTimes/131690" target="_blank">📅 18:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131689">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
ترامپ: اولین جمله پیشنهاد ایران را دوست نداشتم، برای همین آن را دور انداختم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 134 · <a href="https://t.me/SorkhTimes/131689" target="_blank">📅 18:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131687">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
3 گیگ 700
5 گیگ 900
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 186 · <a href="https://t.me/SorkhTimes/131687" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131686">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
مشاور وزیر ارتباطات: اینترنت بین‌الملل حتماً به حالت عادی برمی‌گردد، خیال مردم راحت باشد.
🔺
روزانه پیگیر بازگشایی هستیم و بخشی از خدمات بین‌الملل هم‌اکنون برگشته است. امیدواریم در ماه‌های آینده با تصمیم نهادهای امنیتی، دسترسی کامل برقرار شود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 182 · <a href="https://t.me/SorkhTimes/131686" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131685">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
پرسپولیس به دنبال تغییر سرپرست نیست؛خلیلی روی نیمکت می‌نشیند
❌
پس از کنارگذاشتن پیروانی به دلیل سفر به آمریکا در میانۀ جنگ، در روزهای اخیر نام چند پیشکسوت برای پست سرپرستی پرسپولیس مطرح شد اما پیگیری‌ها نشان می‌دهد که باشگاه برنامه‌ای برای تغییر موضع خود ندارد و درصورتی‌که مسابقات ادامه پیدا کند محسن خلیلی روی نیمکت می‌نشیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 175 · <a href="https://t.me/SorkhTimes/131685" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131684">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
هلدینگ خلیج فارس به مدیران استقلال گفته پول نداریم و فصل بعد خبری از خرید خارجی و بمب و اینا نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 286 · <a href="https://t.me/SorkhTimes/131684" target="_blank">📅 17:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131683">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🛜
دو عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 297 · <a href="https://t.me/SorkhTimes/131683" target="_blank">📅 17:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131682">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🛜
دو عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 330 · <a href="https://t.me/SorkhTimes/131682" target="_blank">📅 17:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131679">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
پرسپولیس
حداقل ۸ بازیکن تو
جام جهانی داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 357 · <a href="https://t.me/SorkhTimes/131679" target="_blank">📅 16:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131678">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ6pb_zn9-yiONaidFWDhmyweWIHKcNlUb1wCyD4-TRe-uZYx2NsL3iLvOlAdXOtHKbDXtK2IVo0y_Y-p9QawcOu95Ta-I7BTGP98Q-FSYfnjWjHdhldL91x4CkvklpPMSx7Q51jmlDOQD79etCxgMoOtNqJVo2H32sN1IO-nrE1eS0Y-9HC9HrclG4Xfyk-pUnnhuunRlUwQ5p0EeSKISGIm5k1MJXKYWtvobCXmuRxTjxi-vnwy2yokP4DIbM5WauzapS_KgY-Uq-7rFrE45l3r1WoRvE8WzvhOxaU_u6qY4wtRuSuY3CEJqe5YoZlgfXr1hbc-UKTxK_zaKaaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی، شهردار تهران: ما قصد داشتیم قبل از جنگ بیت رهبری رو با معماری جدید بازسازی کنیم، اما آمریکا عملیات تخریب رو که بسیار هزینه‌بر هم بود برای ما رایگان انجام داد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 356 · <a href="https://t.me/SorkhTimes/131678" target="_blank">📅 16:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131677">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUxGIvW3Zs2RUWfrmC9yPWUEHyym0L8W12qNuu4IaI8-ecYWk1ktZCJR-qDd3nTXNHdDG4pwSM5fbTxCLyAjCPp7Kxw6LYS_6-BvKNRZ_aY2tS3Fzc3xR-wKQ33tLzTyzqYCoYuvBGJ66ZAzHhJPZPpg5V9Ii2m14_OkuKKZ6dsSJm_HAVYpVIrE909GLr9nGTUQvCRB3cQZA-K1rrY5NwM6mQBJ4BfRT6gmXsdJcLjjWDr0Q6pCB2inDpIR2lLefbdyC9q51x83K9Y6YxhtMv0YbeA_dzRO8zDnr-loYu202Vsg5ActF8wmWsfMY9hQItjzoXil-T_YPH26YL9fSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 348 · <a href="https://t.me/SorkhTimes/131677" target="_blank">📅 16:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131676">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1942fb9fb8.mp4?token=h0wdfHBgneDGjtCTb1u1a3--0s3haAwSE-jOQxNRyk_LYs9sIoSm3nWbr4bWlWA1dvuMxSvYaQ0GFCzp6qrXRd68waDLXIqESLy41VoY6ExrG0dx0MyiZo_1Ld40kMhv8dwi0qfpFG20yJcai6kIyrOGCv7Mmw9rQwxPPO2PUKnGXE4zctEzkRwEnK7-HxXmlU_j7T4_gxJE_aGE6afVpjEg7iyCCyo42rXEJuA64yStkTjMETpzACPEnT4okCGiEyKoYi7Ih8E7nTTL_L03wA3YgJm5Jr7T-4R8wcC63knuBP8ZFlEiYzJGudrJseSNIDRCXUzwAnN73XJuKGu-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1942fb9fb8.mp4?token=h0wdfHBgneDGjtCTb1u1a3--0s3haAwSE-jOQxNRyk_LYs9sIoSm3nWbr4bWlWA1dvuMxSvYaQ0GFCzp6qrXRd68waDLXIqESLy41VoY6ExrG0dx0MyiZo_1Ld40kMhv8dwi0qfpFG20yJcai6kIyrOGCv7Mmw9rQwxPPO2PUKnGXE4zctEzkRwEnK7-HxXmlU_j7T4_gxJE_aGE6afVpjEg7iyCCyo42rXEJuA64yStkTjMETpzACPEnT4okCGiEyKoYi7Ih8E7nTTL_L03wA3YgJm5Jr7T-4R8wcC63knuBP8ZFlEiYzJGudrJseSNIDRCXUzwAnN73XJuKGu-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
افشاگری بهزاد داداش زاده مسئول برگزاری مسابقات هیات فوتبال استان تهران از زد و بند خلیلی در آکادمی پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 540 · <a href="https://t.me/SorkhTimes/131676" target="_blank">📅 14:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131675">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/SorkhTimes/131675" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131674">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
ترامپ، رئیس‌جمهور آمریکا: ما ارتش ایران را نابود کرده‌ایم و شاید باید یک پاکسازی سبک انجام دهیم!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 549 · <a href="https://t.me/SorkhTimes/131674" target="_blank">📅 14:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131673">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
ترامپ: اخرین چیزی که بهش نیاز داریم الان جنگه، ایران میتونه اورانیوم خودش رو به امریکا یا حتی چین تحویل بده و دیگه جنگی در کار نباشه!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 551 · <a href="https://t.me/SorkhTimes/131673" target="_blank">📅 14:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131672">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
ترامپ، رئیس جمهور آمریکا: من دیگر خیلی بیشتر از این صبر نخواهم کرد؛ آنها باید توافق را امضا کنند!!
❌
رئیس جمهور چین به من اطمینان داد که با داشتن سلاح هسته‌ای توسط ایران مخالف است.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 548 · <a href="https://t.me/SorkhTimes/131672" target="_blank">📅 14:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131670">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🛜
دو
عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/SorkhTimes/131670" target="_blank">📅 13:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131669">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 635 · <a href="https://t.me/SorkhTimes/131669" target="_blank">📅 13:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131668">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
وزارت خارجه چین: در مسئله هسته‌ای ایران، استفاده از زور به بن‌بست رسیده است
🔴
درگیری بین ایران و آمریکا هرگز نباید اتفاق می‌افتاد، نیازی به ادامه آن نیست و پکن همواره معتقد بوده که گفتگو و مذاکره بهترین راه است و بايد يک راه حل فوری پيدا شود.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/SorkhTimes/131668" target="_blank">📅 13:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131667">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
3 گیگ 700
5 گیگ 900
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 635 · <a href="https://t.me/SorkhTimes/131667" target="_blank">📅 13:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131666">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
رسانه های مملکت : ترابی و اسماعیلی‌فر دوس دارن دوباره برگردن پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/SorkhTimes/131666" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131665">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 687 · <a href="https://t.me/SorkhTimes/131665" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131664">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
دیشب تو لیگ سوئیس تیم اف سی تاون که موفق شده چند هفته قبل از پایان لیگ این کشور قهرمان بشه به تیم یانگ بویز 8 بر 3 باخته و دو تا اخراجی هم داشته!
❌
همین بازی باعث شده تا فیفا به دلیل شرط‌بندی ورود کنه و ممکنه لیگ این کشور کلا تعلیق بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/SorkhTimes/131664" target="_blank">📅 12:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131663">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 680 · <a href="https://t.me/SorkhTimes/131663" target="_blank">📅 12:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131662">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
فوری/ آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
❌
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
❌
گفتنی است ایران پیشنهاد خود را مبتنی بر مذاکرات دو مرحله ای ارائه کرده بود که در مرحله اول منجر به…</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/SorkhTimes/131662" target="_blank">📅 12:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131661">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
مصطفی زارعی رئیس کمیته صدور مجوز حرفه‌ای خیلی کوتاه گفت:
🔵
❌
متاسفانه به مهدی تاج اطلاعات غلط داده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/SorkhTimes/131661" target="_blank">📅 11:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131659">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
احتمال انصراف سپاهان از آسیا / پرسپولیس جدی‌ترین مدعی جایگزینی
🔴
مدیران باشگاه سپاهان به‌دلیل فشارهای مالی و هزینه‌های سنگین حضور در رقابت‌های آسیایی، در حال بررسی احتمال انصراف از لیگ قهرمانان آسیا هستند؛ اتفاقی که در صورت نهایی شدن، یکی از بزرگ‌ترین شوک‌های…</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/SorkhTimes/131659" target="_blank">📅 10:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131658">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 715 · <a href="https://t.me/SorkhTimes/131658" target="_blank">📅 10:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131657">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 704 · <a href="https://t.me/SorkhTimes/131657" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131656">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
مهدی طارمی دو سال پیش تصمیم گرفت از پورتو جدا بشه و به اینتر قهرمان ایتالیا پیوست و همراه این نتونست هیچ جامی بدست بیاره و در نهایت آخر فصل از این تیم جدا شد و به المپیاکوس قهرمان یونان پیوست و همراه این تیم هم نتونست امسال قهرمان بشه و فصل رو بدون جام تموم…</div>
<div class="tg-footer">👁️ 696 · <a href="https://t.me/SorkhTimes/131656" target="_blank">📅 10:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131655">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXNi1JhQaKBUbQdw3x77JDeuGZspUFQRcIG77-R5XbsKpXFAcN7m0umKHmnWFMYpyd-fg8o7O7WPj1sO0HbgiR4i6NFFg8KK-1fEqRwTohs4WuASV7RS3ZAqDWyGTBOovGMX0QhUKlQqyulYGzp7CvHqNWV4dgVLbNvFNEbB0kA2n2mxJVwDQMQs_xtdlyrWMIi_ynaSMk8OqZCadRIDl7iXaxCqSONv9PxotOx0uArKDmADkRNfNjf2A50jmUrOjWbLC7JD6oc0JxFNehPwmPvlc6pHiNIaySALf7MDoheNX4ZXf-qUOfhUr7zbHc5SR8X3XnXHXlV3TbzUW5qwpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SorkhTimes/131655" target="_blank">📅 01:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131654">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
#خبرگزاری‌مهر : برسی آمار ها نشان میدهد استقلال، پرسپولیس و تراکتور شانس بیشتری برای حضور در آسیا خواهند داشت
🔴
این در حالی است که سپاهان در دیدارهای مستقیم مقابل رقبای سنتی خود نتایج ضعیفی کسب کرده و شانس کمتری برای کسب سهمیه خواهد داشت
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/SorkhTimes/131654" target="_blank">📅 00:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131652">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
با اعلام مهدی تاج، باشگاه استقلال مجوز حرفه ای گرفت تا حضور این تیم در فصل آینده رقابت های آسیایی به نوعی قطعی شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/SorkhTimes/131652" target="_blank">📅 23:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131651">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚡️
⚡️
قلعه نویی ستاره پرسپولیس را خط می‌زند!؟
❌
در تیم ملی به هدایت امیر قلعه‌نویی، رقابت در خط حمله خیلی شدید شده. حضور سردار آزمون و مهدی طارمی تقریباً قطعی است و بازیکنانی مثل شهریار مغانلو و امیرحسین حسین‌زاده هم شانس بالایی دارند.  به همین دلیل احتمال دارد…</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/SorkhTimes/131651" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131650">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
فووووووووووووری
🔴
به دلیل پیش رو بودن جام ملت‌های آسیا در دی ماه و برنامه آماده سازی تیم ملی برگزاری ادامه لیگ برتر پس از جام جهانی منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/SorkhTimes/131650" target="_blank">📅 23:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131649">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
معامله‌گری: تنها با برگزاری مجدد لیگ عدالت در فوتبال ما برگزار میشه و قهرمان باید با بازی کردن مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/SorkhTimes/131649" target="_blank">📅 23:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131647">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
پیغام عجیب بیرانوند به حدادی، مرا به پرسپولیس برگردانید!
🔴
به گزارش شهرآرانیوز، علیرضا بیرانوند که خودش را برای جام جهانی آماده می‌کند، نیم نگاهی هم به آینده خودش بعد از این مسابقات دارد. او از چند ماه پیش به دنبال بازگشت به پرسپولیس بوده و در شرایط فعلی…</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/SorkhTimes/131647" target="_blank">📅 22:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔺
بخشش جریمه خداداد عزیزی توسط کمیته استیناف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131646" target="_blank">📅 21:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚪️
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131644" target="_blank">📅 20:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
معامله‌گری: تنها با برگزاری مجدد لیگ عدالت در فوتبال ما برگزار میشه و قهرمان باید با بازی کردن مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131643" target="_blank">📅 20:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💬
🔴
امیرحسین اصلانیان، پیشکسوت پرسپولیس :
◽️
تعویق لیگ باعث شده باشگاه‌ها از شرایط آرمانی دور شوند و به اعتقاد من هیچ تیمی با آمادگی کامل وارد مسابقات نخواهد شد. حتی این احتمال وجود دارد که لیگ بعد از جام جهانی هم برگزار نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131642" target="_blank">📅 20:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
حمید رسایی: دولت میخواد قیمت بنزین رو تا ۲۰ هزار تومان افزایش بده
.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131641" target="_blank">📅 19:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ5nzC2dizdU79XDCSnsPGYZfr2K7dwRLky2KqzcetU25kF2Dve7ak9tVfe_eqw5st4p53PQk9G8d_f5vgMvkxSmt32EbeHxuIAPQ3TtxHWmQZXN7h6mAseljjRlnlDrtci645be-7_wip8SdOgdAvV6ZvvP6X5yaGGo2zTh6iqm9RribxLIlqcM_sV_RDw3sPW74aRpIWoG-ixsxO1nxi0vBjgVq3Kj2N5fSkZ0yMOzOwYOCXXJDTvC2STMmhBJZKtsvGWZX-kaolAAhDkiksDW5W_HYu3boKWfJSTXZ2FHQwV3WW2N3qUKShkIVNSPh7mr61LVLLYjI0l_-JgIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روزنامه اعتماد آنلاین:
🔺
اینترنت بین الملل خرداد ماه وصل میشه
🔺
هفته آینده به ریاست عارف معاون پزشکیان قراره زمینه‌های لازم برای رفع قطعی اینترنتی فراهم بشه تا حداکثر تا وسطای خردادماه اینترنت وصل بشه
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131640" target="_blank">📅 19:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxN_6YRtiJD05k_783xuK8CX90z4Jlf8MVcnJtiOnth0itQXCv3K1pxSoppUk1TS4Go5DM6Aq_zewSFgwJXIkZZS2w2B-lG1WX7uqi3eo58l6WM8gSRYL-BxnRZnMlsYjPcLXXxtcqJgNf65-FgpbE8_dDN8lQM32Q61AkflW4dp2QrS07cdXSoaQupf8vsdAe3V0cArG5brQ41LOsnT9Y_9Vy4oViLDgC3aUHQs4jiIE1nXr4seEf8GLm462tL8ZbPSVw_29R96hbhEfpTRVnC9gK7GwnGiMuwRr_jjnodnuc8J5Gn66FBy6_Zt0RAE17XL1m0nwfF5oCUAEY1FfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دنیس اکرت، بازیکن دورگه ایرانی که برادرزاده آناهیتا درگاهی، بازیگر سینما است، نام خانوادگی خود را در سامانه فیفا به دنیس درگاهی تغییر داد و مشکل او برای حضور در تیم ملی ایران حل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131639" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🛜
دو
عدد سرور نامحدود ۲۱ روزه Anyconnect موجود شده فقط 4.5T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131638" target="_blank">📅 15:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131637">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131637" target="_blank">📅 15:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131635">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔵
تاجرنیا خبر داد: هزینه‌های استقلال در فصل آینده به خصوص در جذب بازیکن به شدت کاهش پیدا خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131635" target="_blank">📅 14:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131634">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚪️
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131634" target="_blank">📅 14:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131633">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULzvTTw0spODscWoCcqaS7-ylrY_0htU5C8koP-AHCcdiVoD6iAy1F4fI5fInr87A5JUwUHjB8tXrhfMyPz9dZn1ypp7T8F1c76b7G8NJmUcJoIToy8RYRI63kjYWMuk__RTjXeSBDbxtCbMvgEOaDDwrdA1nrrRiJwFKWF8J3Mz5I8CDUHlMakRiOt_WHV8aDGMzun1Gl6cN_2pbdtBOnJ3FvOC6qqSsbJWbjVxt-iDKiMxO0fn2gyI3g_j6gAJkO7m97CwjyfiJhfhtJlk73mjf3jIG-kcsNVSD0fj6AL1ACNNMspT5HOZpN8GCHkfV2QIYFlsgOkawMXy3AImRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
🔴
امیرحسین اصلانیان، پیشکسوت پرسپولیس :
◽️
تعویق لیگ باعث شده باشگاه‌ها از شرایط آرمانی دور شوند و به اعتقاد من هیچ تیمی با آمادگی کامل وارد مسابقات نخواهد شد. حتی این احتمال وجود دارد که لیگ بعد از جام جهانی هم برگزار نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131633" target="_blank">📅 14:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131631">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 891 · <a href="https://t.me/SorkhTimes/131631" target="_blank">📅 13:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPnR6JzgP6mybQCV65kNNeYnKiT3UTjxXt1ueKF2DO8IdfAr85IJ6Xxz-E5e4ap0LMs3kNeLvLlFy_y7CQDYgtXTTsEafV84qk7ZiK6rQ6ZOIXIJ9RsNF_2jcffw3doAz95U5sNQUPVZe9qLsGnCub3QEojls0LMp5JsI70i5QlULDYQLGYCcpXk1DYxMYppS9qJZNxuOEh8WaD9cdKCjJa04C5qStImNsgu60vcqe_nYEKVfDXdGijFUiP8pT92vsBjSHabgj2JYW0zQMr2YgMxeW9xo1v9TtQKV-G7WfhSBeA86Jy4KEYL1WhFyvX2rIuZ1SzvSkH_3QL-tp7EKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 856 · <a href="https://t.me/SorkhTimes/131630" target="_blank">📅 13:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚪️
سخنگوی فدراسیون فوتبال:
۱۴ باشگاه گفتند بازی‌های ما را ۳-۰ کنید!
🔺
سازمان لیگ مصمم بود لیگ برتر را برگزار کند و روز ۸ فروردین به باشگاه‌ها گفته شد که تمرینات را آغاز کنند. با این حال ۱۴ باشگاه گفتند که در لیگ برتر شرکت نمی‌کنیم و بازی‌های ما را ۳-۰ کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/SorkhTimes/131629" target="_blank">📅 13:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
قرارداد علیپور دوساله دیگه تمدید شد
❌
✍️
باشگاه پرسپولیس مبلغ قرارداد علیپور رو افزایش داد و با این بازیکن برای دوفصل دیگه به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 864 · <a href="https://t.me/SorkhTimes/131628" target="_blank">📅 13:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV_rMiXsPD7GHazjiIGS4rN1KwL-0N1LcoymKjvMKKG5DjDq9siY4yKo9Q09q4TT_HS2FSKGbrf61QIu9SWdXY9B8jGKJlCYtnNO8AF7bG6E-FJrLnpg7vOrQF9rAe65EEuup-SQomPOS0ljl5SgyrthgXdAKYVVpTKRhg0fZv3GKtit6ilOV5J6oKcb5MG-YoQyoEP-1rkV7fS9xBTriR_TCy4Yy3eBc9AhH8418kUSBck_-MGHhk-xQkc7rIl7iROfUBIQ6W-SWyJ8h0xh5Ege_JqVd8NWNNgi75_by87mgUakudFiwnwtOLpkJm9B_4TPWYiYacpnMohAdraYuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 968 · <a href="https://t.me/SorkhTimes/131627" target="_blank">📅 12:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131625">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM_0Gt2_j5Erf6iodfpWKJTFBnhMEgjbExVw2IxSnC55sNEz-yAwau22LL5OVRLJYQ1w0Dw6BG3Z0m7VKQVy3jqHnRhgLu1n4KVfe3tIJozL1XcOruskWWdrdVKWThAPhl94K3bHQ4LKa_0mq_R6r4BJy2yk7kA4tr_KLIae9Tfrect-k76iWDXYolvZLjnDTjzLb-w1YaD4qenW2VeESvDXS5vpDtNz8Y_q-n4uWg2dUU4R8J7jfwRzw8G4ot_SHfKLe8jZpDWU9Tr6dM-Qajybd0OmZSuOyXD0dJ9gFH4kQax7t-xwxBOYEVta_pqSLS8LXWtYvTg_LL5nIz3uSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
معین
: قرار نیست واسه تیم ملی آهنگ بخونم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/SorkhTimes/131625" target="_blank">📅 11:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131624">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBcW4gcz6T5laCKqu06BXujtQ6gT7TCk3PAOQ5uuqCGMqTDaFm0bKFT0wNPYmVGTM3cEgJS6CtbfXyJuJzWgvzkCMA23rE93sjagnA4OCbdgJyhy7CRNb0TaTSRgHT0kzDJH9bByUZhqM8yYCJVdy_Q0xZIRtTPn_z8Dk-i7-VsUqosf9sqhtY6JFQw9VaKc2lqfEpqRm1RVWtVaSOO-hN3SiTsyqw-vcYNE24JfmEr5Dbnuaf4sRGy-SKz_GQrgKhsR6X41OtDRYlpm9UKlSJaEgQALOtm-Z4OI3W91av6ch-R1upjIZgwVdEJSNCawd0Cn4HdmM-sj3Ize7dreTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اینکه مدیران پرسپولیس بتوانند از لحاظ مبلغ قرارداد میلاد محمدی را راضی نگه دارند وی به مدت دو فصل دیگر با پرسپولیس تمدید خواهد کرد و درغیر اینصورت به لیگ ترکیه یا لیگ یونان سفر خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/SorkhTimes/131624" target="_blank">📅 11:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131623">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekHWARcY7TRtVZRdGP0ThCN4tI_jtndbYiPigoAmDslXV2vSW3knsuzpaC9yLJpfDFTz8BL2sOkWzrZfB3I1kZztKZHDXCyyMw56FgVWDG7A4jW8OM-p0adRtXT4vJBKmgOOt1s0DDtxLS3hbYQUZ3nZ95QS84_EDM6eOIrpVk7aBuvMfpfvnEe54gh3Uv3X4gHkSH_7H6T4nDB3LSVRERMcYsaeG1booVzY6PctLW2ixCL2C4YQ4AeoLVLRfcDaeS2bAkaCVnenq4TI2FnxSJLuISr5q1f2AVrH1b3oXz5T-P_XfTKhsqGxXZDrozkTcnnHbNH0uIf03i6TvqbDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تسنیم: قرارداد باکیچ به طور خودکار تمدید میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/SorkhTimes/131623" target="_blank">📅 11:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131622">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSEurpdEvsb-PvTf6xZQQ9mrYPlq5dKDLijtpqp1drFD3U0Ov5Gp5myIxQ-T1xIeO6WLeX5BM38Qdjn26uhwe4b0g1WdTn_P5wZiE2QbvDY094B7Yy4FV5ltJu9XzsfJFJUQPpBB7KjjGYeeT8MNbM4eF5k_CZ6o31iTBPvSMkZnEWSqasPffVbXbHXZ_Dj5nJg2zE9VA2IuhekVOmt97oTqwfAzb2VZMj_nfCePAx53SAQDw-0IoectyQp705fEmmgCbEy8ofoRFgK1pf2-ZzQj2DxHbqFj4iATQEcYlW43H7RETwazXeGiR9SKqUeQIlEtLEPmcSA6ldLdeG15bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 929 · <a href="https://t.me/SorkhTimes/131622" target="_blank">📅 02:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131618">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToqT7fBiO-FV3qXSOhKvliGhjoqlA7ktGxbRRnwuX-uPM0yZSdB4PqQXmR3xb88ErzRiX8LP1wqQ6jrq7BO1xZRPbVgFTCAp01iDH4n1igqxiq_IiCRGIoMfrDOFdoWPmww2kjohjrn7pZKo7X0Bc6hzyhXF_8M1FzqptBzstcV8hHhDd_pCysqcTVJnxo3h8qlGU7X0N7Y7vhkKo9AtZuRIYcsf1PnI1Ib4KgngdwENbtB5bnb90c5uFYJWdTOfgLMlvW1ueesFCqfYLwykj0IJH_MBkChWiUU22Ze7QimiaD9GItJKxEZwWiJ4voo7by5L1pkttuV0WcMM89QPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مهدی تاج: شنیده ایم معین برای تیم ملی تو جام جهانی قراره موزیک بخونه، ما دخالتی در این موزیک نداشتیم ولی ازش حمایت می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131618" target="_blank">📅 23:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK9QmQan4BPjEqSiN41QSk6Hs4gqxlf_ZNgyFLId-CnVRCDKv7C1zDlB7YxNQS8JALcyPU-GUddj3cfJbLZlcQFv7EnQzvASmlAw3sEcm4-mqmXqb27oSQcbbLUZ2e3sqnLGgDftVhHkKsfuwRjuKsb1Y77jOqQgQX5SJLMmTcDSbVhF6mXMO75nzXR6Mf1sfqkPbjO3Bm6_WXcn5TF63KpZL4doWAjJbgab5egkG7sjmnaFOGcwVGPBaR0t1DvVfwfkcvDDaklA9bWiaki568G14cdpXSbTIbIV6yPTIHHmEa9AaF3s4Ti8RcU8TRJqKSlByyDXBUguOSE2ctSSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
از کیت جدید تیم ملی جام جهانی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/SorkhTimes/131617" target="_blank">📅 22:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131616">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⏺
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/SorkhTimes/131616" target="_blank">📅 21:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131615">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siZBlXWL390Yk1tVA1ov7NCSi9fH3F1jd4jHtnqBaPhErJU42hjlNVQphVJ1cJ-uCiFkBxgnHfESrnnwXZHFtNfwnA-xRvvoGR81q5fLLSqnozJoC3w7tfZyG7Ht3L7BzSyMIzhQ34hmy8D27MlEGbpEefvaODLgpsT3dgS7wXaNEvhJ7el05FbCaQuJn7rDYjE6HlMArtNj0IYxLI4eHKQ4aszXQCQhajmdwGZi99q7n1fPH869uSUmZYsk1xzjHebJPBMKQplhEyYfz3E8_U6m_HfARrGnoPmxTMA7Y7NYp9ShJtoRLKrGgNueHZHkhL5YnzfcV52yhPBIdWRp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SorkhTimes/131615" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131613">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2QIS2bpQ-eXA-I051h_0tvpImOOrJKPTscPyX5oALQb10Y0Ey_RqUM-AIGvRZI8zgrPnP_bwPqgHenjRLMhO2TM0Bs7BPYH4ayLMLm6uRQ9Dp7gTVNITpf1r_BYAsLxEEIoWtTBIE88POyuX0qJW-WECYZgD2dZybnKFwMLWodepX9qv9yUviP8N1Tw4PUDRM2Lrn341qCzGzGPaYeNIoxKsxRpPSyNWTnMxbHYfIJrVs-AS9pDZPesSB1LxbjlOTmH0xMEad0vnoSiiIPLZbFej70O89RIcAPYvjA95eB_ROsHKZGdH3IxSi_1lBnS17xiHppudOWDVQe-bs_q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنای تیم میلی کنار پزشکیان عکس یادگاری گرفتن و راهی جام جهانی شدن!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/SorkhTimes/131613" target="_blank">📅 21:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131612">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
معاون اداری و پشتیبانی وزارت ورزش و جوانان اعلام کرد که برای حضور قدرتمندانه تیم ملی در جام جهانی ۲۰۲۶، مبلغ ۴۰۰ میلیارد تومان بودجه در نظر گرفته شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 894 · <a href="https://t.me/SorkhTimes/131612" target="_blank">📅 20:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131609">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
توافق پرسپولیس با مهاجم تیم ملی فوتبال ایران/امضا قرارداد قبل از اعزام
🔻
پیمان حدادی مدیرعامل باشگاه پرسپولیس پس از تعلیق برگزاری ادامه رقابت های فصل جاری لیگ برتر با اوسمار ویه را سرمربی برزیلی سرخپوشان پایتخت برای فصل آینده به توافق های لازم برای تمدید و جذب بازیکن در پست های مهم رسید.
🔻
حدادی در نخستین گام برای حفظ یکی از مهم ترین عناضر خط حمله این تیم پای میز مذاکره با علی علیپور نشست تا مهاجم تیم ملی ایران را که از مبلغ قرارداد فصل جاری خود با سرخپوشان ناراضی بود به تمدید آن برای دو فصل دیگر متقاعد کند. نشست هایی که بالاخره نتیجه داد تا علیپور راضی به عقد قرارداد فصل آینده نیز شود.
🔻
مدیرعامل باشگاه پرسپولیس تصمیم دارد تمدید قرارداد این بازیکن را قبل از اعزام تیم ملی فوتبال به اردوی ترکیه که هفته آینده خواهد بود، انجام دهد تا اینگونه نقل و انتقالات تابستانی سرخ ها را آغاز کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 995 · <a href="https://t.me/SorkhTimes/131609" target="_blank">📅 19:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/SorkhTimes/131607" target="_blank">📅 19:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/SorkhTimes/131606" target="_blank">📅 19:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXy3y9y_mm0seDl2KRpZEW_w7GKmLpPikAo8INoTRowBidUWlrq7HasDjtYO662g2DofoYpH5o5b0aUihKO8tBDhnwikZPE5-Z7LE8nl_Coul3qaphLi1N9cytqaV7yJ3eVQf3jmEo9x7h4QyDBqihN4-6WK_ztH_uyqnsfEsSir1kWmiJM1Z_sTYaoa1DL6yvZctJHsL6FjnJas6_rsP62wf_RLgG2B4uX32IkguR5oImtyLwINnUrNsYGaHse0mibqF80cVE4WRcgq93ZuqBjxER_BWOqDMQXK9SY8iY1yJg5MmLsD14cK48g_-k76IjQg9635oCmmaa9IIokfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت علی بازگشا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 952 · <a href="https://t.me/SorkhTimes/131605" target="_blank">📅 17:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131603">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♨️
🚨
نیویورک تایمز:
قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید 60 روزه حمله به ایران شروع کند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/SorkhTimes/131603" target="_blank">📅 16:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131600">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7IgzAi76yR8rLInXt6LeZt5s0wfXvp47RupcrelSW7w3SozKioGLc82pGznSwdnDW_U8rxw6d8O4rvANXPJpCI_hBQkfiaRWGKjzFrjidFXPBeO4fcIFB3kYp6Sl8Rx95tm2dLXeyj0Ejh2p5uLV5qlGfqv8DQIp45FRWTJhRLKzqrQTIzfh0siXfludzPbbY0D0Qb1RRICg6BnYqgAv9mgwn_A8Mz6Fw4pziftcjo0Li5UiJPfhtBIzVVGe-15tuq1g6szJkHLkMojddvOpAgHvjaHGjS61c9UQswhN_mx_0vDxr4oHQlkaBOSelRK0B5gLKF8Ky32mnPUJ_68Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
قرارداد علی قلی‌زاده تا سال ۲۰۲۷ با لخ پوزنان تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/SorkhTimes/131600" target="_blank">📅 15:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131599">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCS5nf7kdEr7M0owXske_WGoY2fcjPDz7tP4SlKzBeTAjpvbaJAo3sLIOr_JMHILkXIIiOAKxd-HpG20UGCXxpFDOZCUROd-o2umK9SWfuesJ3H2PlPYylkRg91XX90MKdlhXOCTxU5YAC0ZZJwgBbZLC8S6RWMMb73QyKO2S-svGwGjm-Wg3RRESJcuRHIH9zM3GunYO66cu1vqfkmyqiiPk-IzmLZQaO5xya2lVVQqxxkmAOsoxSt2F90cMavsMAA0InWR29oYATXApVKvtLTQ4vnIk-emqvQ9iNIf4Z34Z3bT3DFSbcdTwgyA_DIs3kEskmo9aqlCTe3lxTC7dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن مسلمان به کادرفنی تیم امید پرسپولیس پیوست
مسلمان با پیشنهاد بهادر عبدی و بعد از جلسه با ادموند بزیک مدیریت آکادمی پرسپولیس به عنوان مربی به عضویت کادرفنی این تیم درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/SorkhTimes/131599" target="_blank">📅 15:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131598">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iy10S7Wh8wqqcnxNh2yls6d4ry2CaTr2Rtc1G7xaChiYXtTuxLmv8iX40pAti9o9YEKsIaeyE3PLyBKXQLSKduyeORqDUw2g_ifu3wYd07iFIv2M7VND5Kkgmi31NNrYLMgV8Mi5JpZ9qYqUjoSH-iunUnWsru3d4Pk_WosGm9zrJ6uKrB1DvYc4OhV2X_pUEvyFMGoc0QaDepu2wIxhbEcwaaIkK9yDYtuy4FUzHohOVzrVGwt6AlGR8fVcDKaukpfVmi5BXHu7-Y1c5uRUQ4XHLygzDkb8R6BSZ7h-czpQnVIa3hATjtzUQegPhro4noBNcK2HtdJ-t5mrqV3lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها و ورود به کانال وینکوبت همین الان جوین شو:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/SorkhTimes/131598" target="_blank">📅 15:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131596">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
کامران غضنفری، نماینده مجلس: شواهد و قرائن نشان می‌دهد که آمریکا و اسرائیل قصد انجام یک عملیات گسترده برای تصرف برخی از جزایر جنوب را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 967 · <a href="https://t.me/SorkhTimes/131596" target="_blank">📅 13:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131595">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
ترامپ رسما اومد گفت انقدر صبر میکنیم تا ایران تحت فشار مجبور به توافق بشه.
❗️
یعنی ممکنه تا شهریور تو همین وضعیت بموییم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131595" target="_blank">📅 12:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131594">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131594" target="_blank">📅 12:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131593">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🔴
شنیده‌میشود محسن‌مسلمان فوق ستاره سال‌ های نچندان دورباشگاه پرسپولیس بزودی به کادرفنی این تیم برای فصل بعد رقابت‌ها اضافه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131593" target="_blank">📅 11:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131592">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY5xGI-SZGDPGF4G93NIUJJrX2YDogFBn5WdBRp5rJ3Bqh5zDvgk8s5yt3kjpsgzbUWu-RQhvgYw3zu-kVBpVzmyorT0-l8XtHD3zSHFBPMLqg_TUALRFrjwrQM89l7AV4dNGltjAJ2QbC7y03brTrP6fJwPXqnDPW3BUiCCW2rzgA4LBBOHP8clzFJ-Sg2-E_AKhTxHeEmL7ey_-xj__OdXAIUxKnUxsMKnrukfcraAXzo_dpHFSkKdzfy1eIERAw9cy_9Ig1h2xYaut-GchANM_RLkJLd2Rq3ITsrMNHtp6dNWf6gwD6IOj6mi50RFb1MAKw9v0VlERpME0VzizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پپ گواردیولا:
من بی طرف نیستم من طرفدار فلسطین هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131592" target="_blank">📅 11:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131590">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
🔴
مارکو باکیچ تابستان گذشته با قراردادی «۱+۱» به پرسپولیس پیوست که طبق بند الحاقی قرارداد، فعال شدن سال دوم منوط به حضور او در ۶۰ درصد مسابقات رسمی فصل اول بود. با وجود مصدومیت این بازیکن در اواسط فصل، طبق ماده ۵ آیین‌نامه نقل‌وانتقالات فیفا، مدت زمان مصدومیت از مجموع مسابقات قابل محاسبه کسر می‌شود؛ به همین دلیل باکیچ از نظر حقوقی به حدنصاب ۶۰ درصد رسیده و قرارداد فصل دوم او به‌صورت خودکار فعال شده است.
🟥
در نتیجه، قرارداد دوساله این هافبک مونته‌نگرویی قطعی و لازم‌الاجرا محسوب می‌شود و ادامه همکاری او نیازی به تمدید یا توافق جدید ندارد. همچنین اگر پرسپولیس قصد کنار گذاشتن این بازیکن را داشته باشد، احتمال محکومیت باشگاه در دادگاه CAS بسیار بالاست و باشگاه باید کل مبلغ قرارداد را پرداخت کند. از سوی دیگر، تاکنون هیچ نوتیس فسخی از سوی باکیچ به باشگاه ارسال نشده و تمام بحث‌های مربوط به «مشروط بودن» قرارداد، با مفاد توافق و استانداردهای فیفا همخوانی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 956 · <a href="https://t.me/SorkhTimes/131590" target="_blank">📅 09:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131589">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVvTufkqFfysYHyruBxu0cIxvaWWqo07tTxHf-KgVkHsyDbBgjXTNhv69-lysNwQsJtfmAFUplMfFAoU8GbCY6X3jmsJ6v4S9M-qIaIStF_HhqxOuJ7eISKoepgRK1v0SU2OjhJKqRS9XB-OQPSpcplj872WEmQsrAm1M1Z8U2Ve-nTB5ljLZE_fsJJo1ZmnNNbPN7uDbwYuElrHn6J8AoLdk136Fohh_Q_pP3Irj4I3kqTokmJOKJhlxo6SydqnabV5tl9Nh5gWI1QUJFmz0pinyGe9-4X9ZaBbafNgMgqmPM-Ywz3l5GutmHKYtuGshHEdYWN-vOEVxzQJ-r98HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 978 · <a href="https://t.me/SorkhTimes/131589" target="_blank">📅 01:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131588">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
همین زلزله رو کم داشتیم وسط این همه تورم،جنگ‌ و بدبختی، فیلترینگ و قطعی اینترنت!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 895 · <a href="https://t.me/SorkhTimes/131588" target="_blank">📅 00:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
جزییاتی از زلزله شدید تهران   بزرگی و شدت: ۴.۶   محل وقوع: مرز استان‌های تهران و مازندران، حوالی پرديس   زمان وقوع: ۲۳:۴۶ عمق زمین‌لرزه: ۱۰ کیلومتر ۸ کیلومتری پرديس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/SorkhTimes/131587" target="_blank">📅 00:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131586">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ul0JEc_pTGu3EYidJ_U5HgDp1LHgOKAckDMDRrg09qdkUE0pZ9PvhO70hp0FtILNWfS6qdfYQrmRchV4cpvZYm356F5wVlq7PKj3Gd-ut0SstnQ8EXNlcG8mNuLDLdzGSV5dCln3NPaZztWDbboemwFu2fimo6MAsSWhbWFQv3002IsE45QD8evqAo0vlISEyINeXMh2CICZZNRFw9aU2Sr0bgyAMMH69IkwSnRwlq9Gaty9avLMy_7l8UrgCXIZhogKbRB0h93aHSbGwr8X-Hwq2SQKeSD5icQAG7QVHyTKA2ZrnhiwHxGrXrXJ1rSVAsAUvdBtZCkVsFcG1SYpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جزییاتی از زلزله شدید تهران
بزرگی و شدت: ۴.۶
محل وقوع: مرز استان‌های تهران و مازندران، حوالی پرديس
زمان وقوع: ۲۳:۴۶
عمق زمین‌لرزه: ۱۰ کیلومتر
۸ کیلومتری پرديس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131586" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
کانال ۱۲ اسرائیل:
🔴
انتظار می‌ره که ترامپ بعد از بازگشتش از چین در پایان هفته، تصمیمات نهایی و جدیش رو درباره ایران بگیره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/SorkhTimes/131585" target="_blank">📅 22:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 986 · <a href="https://t.me/SorkhTimes/131584" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
درگیری لفظی چندین خبرنگار با فاطمه مهاجرانی بر سر قطعی اینترنت
🔕
مهاجرانی: ترامپ گفته آتش‌بس به تنفس مصنوعی وصل است، کشور در جنگ است! امنیت مردم مهم است و تا وقتی سایه جنگ از کشور دور نشود وضعیت اینترنت به حالت عادی بر نمی‌گردد!
💬
وقتی مردم اینترنت ندارن…</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/SorkhTimes/131583" target="_blank">📅 22:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=JTAjPlezYVnDda462mra1Q_8oSs_XUzvXyjPwEUnP2i3OVnDguSgDfLaRQn1xg5HlBU1CkJ8ga_QkYlJvCTl7eqpRnOl3L3mhq7wrpyBzImW2JXKUf5HKyyo83xaTgRJJRXKy6VUpyiaWrmnM09Ec13CDXyS_Zrwcor3QN65dc1_qTqOPA3XTqnmgw2c_5_0vsZHu3XyhMoUrb_MeJSKZypbgrrLNeLvZiLb1QLUm24m_M796Rkr7REc4HNstgCoTT-VJ-qVAE19iAxacC1soI4Ta-7oyy6dL8mzoRF-pRNc36QYV6jJkpJL_MY5uDwYFX5OT-oTlBlKoTp1VOkP4K88vSUhX5thB4tftroHIyvvwLB6RyWDW5vKc4KCurIcjGpzPyCIcIyVWWHszgyEao4I5mgWzosueJvTcd5ioCIVQ3NuJdPvFSMNDA0qIG3i4PMLj27wZd4J23TZaoq0LGbILUWpZBcfGrRDZGGaYij9EIDsiU0CtxD3fL7rNyH5W3e6Q4Me8Yi0IHvvBtAwB52vfpqj7dhzBROQ8wjoWmHe7MofcOBRXJUK6ut1kHwAO9dSQO7zGe8HjmXVYnXh9QStFbYxWQvrZzAhADodWCoeMoDklHKPm14wPoxBpTVoSKPOTwisN8y7_lMUDwpdeRVXfiImgjksxhvXQ5b6whw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=JTAjPlezYVnDda462mra1Q_8oSs_XUzvXyjPwEUnP2i3OVnDguSgDfLaRQn1xg5HlBU1CkJ8ga_QkYlJvCTl7eqpRnOl3L3mhq7wrpyBzImW2JXKUf5HKyyo83xaTgRJJRXKy6VUpyiaWrmnM09Ec13CDXyS_Zrwcor3QN65dc1_qTqOPA3XTqnmgw2c_5_0vsZHu3XyhMoUrb_MeJSKZypbgrrLNeLvZiLb1QLUm24m_M796Rkr7REc4HNstgCoTT-VJ-qVAE19iAxacC1soI4Ta-7oyy6dL8mzoRF-pRNc36QYV6jJkpJL_MY5uDwYFX5OT-oTlBlKoTp1VOkP4K88vSUhX5thB4tftroHIyvvwLB6RyWDW5vKc4KCurIcjGpzPyCIcIyVWWHszgyEao4I5mgWzosueJvTcd5ioCIVQ3NuJdPvFSMNDA0qIG3i4PMLj27wZd4J23TZaoq0LGbILUWpZBcfGrRDZGGaYij9EIDsiU0CtxD3fL7rNyH5W3e6Q4Me8Yi0IHvvBtAwB52vfpqj7dhzBROQ8wjoWmHe7MofcOBRXJUK6ut1kHwAO9dSQO7zGe8HjmXVYnXh9QStFbYxWQvrZzAhADodWCoeMoDklHKPm14wPoxBpTVoSKPOTwisN8y7_lMUDwpdeRVXfiImgjksxhvXQ5b6whw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صالح حردانی میگه ملی‌پوش‌ها از سربازی معاف بشن تا با روحیه بهتر فوتبال بازی کنند!!!!
◀️
شما چه گلی به سر کشور و مردم زدید که درخواست معافیت دارین؟ کدوم قهرمانی رو آوردین که اینقدر وقیحانه درخواست معافیت دارین؟ چرا یکبار درخواست شما، رویکرد مردم نیست؟ چرا همه چی رو فقط برای خودتون می‌خواهید؟
❌
جز اینه که هیچ جای دنیا چنین پولی رو به شما نمیدن؟ هیچ جای دنیا به چنین ثروتی نمی‌رسیدید جز ایران!!! باز درخواست معافیت سربازی دارین؟
🔴
چه تفاوتی با یک جوان کارگر ۲۵ ساله داری که اون باید بره سربازی و تو نباید بری؟
⚠️
تازه سربازی شما که مثل بقیه مردم نیست، میرید تیم ملوان یا فجر و بازهم فوتبالتون رو بازی می‌کنید. خبری از پادگان نیست. چرا همیشه طلبکارین و سیرمونی هم ندارین؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/SorkhTimes/131582" target="_blank">📅 21:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/SorkhTimes/131581" target="_blank">📅 21:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/SorkhTimes/131580" target="_blank">📅 21:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f2cd4206.mp4?token=INQRTbqEzDrAHGTY5xjSxAFmEpiq_lepvu2gT3LJyWDUGKsesmwgWmx8lWSt_Ul3pRsDlpkZJMObrVFqcQGVq-ck_ue7uckF4fK6LOqvEwVQZTH746fI2pight_CNU5PBGZ2v93e8tRqqBX9JN4OikcNVZPJff6-AyiTDpfeYf1nqS8w_GAQFLHtcWjy10WOPda8MpujMoImILtj0XO_MYgSuH1BzG9rhpX9MmydmZQNQ-Fw2STSnLTrDVlOXhiw6OaARANKJvBu-8ndIoyxfO2pEZaUC-k30fILVMdAE7nppNxM6pMBbToMNn9CMYqksrM2t-Di9wTSa33PzIppzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f2cd4206.mp4?token=INQRTbqEzDrAHGTY5xjSxAFmEpiq_lepvu2gT3LJyWDUGKsesmwgWmx8lWSt_Ul3pRsDlpkZJMObrVFqcQGVq-ck_ue7uckF4fK6LOqvEwVQZTH746fI2pight_CNU5PBGZ2v93e8tRqqBX9JN4OikcNVZPJff6-AyiTDpfeYf1nqS8w_GAQFLHtcWjy10WOPda8MpujMoImILtj0XO_MYgSuH1BzG9rhpX9MmydmZQNQ-Fw2STSnLTrDVlOXhiw6OaARANKJvBu-8ndIoyxfO2pEZaUC-k30fILVMdAE7nppNxM6pMBbToMNn9CMYqksrM2t-Di9wTSa33PzIppzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/SorkhTimes/131579" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🔻
فیفا یه قانون تصویب کرده که بازیکنای خارجی که ۳ سال سابقه حضور تو لیگ یه کشور رو داشته باشن، میتونن واسه تیم ملی اون کشور بازی کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/131578" target="_blank">📅 20:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3nVw2kUPyxd9-g-3eTg7vcFyL7YKOBDeDMGO3hS-Kf3TPJ5fFvbechHy9bN5jmvS5VQfQSDu5axmxxDdtB9APPaVcjUJ5C7LOC0lEoS-N1v3C3pcgiuzWJWP182WUTYOnISLE6_YSn9WseD4nui-iexYlN4ix2jqKEDi9HON2DcPrX8W_3Vb77LlFu11p8NffleR4-mG9fKb-Px-AN-EWtimSUxOuu_R1-VFrGuzizJD0XPe0hlde7Bsu45EsHiZ11FVsbZJAU5PaZk98mTYchQzHyMfGpl8R0EhKiyqTi6fznbpPI850uoB5tRAkxxeAjRTjGzIz4L54WjeUX53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
پزشکیان توییت زده قول داده اینترنتو وصل کنن
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/SorkhTimes/131577" target="_blank">📅 20:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
باشگاه پرسپولیس کارهای تشکیل تیم دوم خود را انجام داده و «پرسپولیس ب» در لیگ دسته دوم فعالیت می‌کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/SorkhTimes/131575" target="_blank">📅 18:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚪️
تاج: تیم‌های راه‌یافته به لیگ نخبگان و لیگ قهرمانان را انتخاب خواهیم کرد
🔺
شاید بتوانیم مهلت معرفی تیم‌ها را یک ماه عقب بیندازیم.
🔺
۱۴ تیم مخالف برگزاری ادامهٔ لیگ‌اند؛ موافقان پرسپولیس و گل‌گهر هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/SorkhTimes/131574" target="_blank">📅 17:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131573">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4B_-A2rPcMAg_ghef4qtaxenbcOK-oT6NukG3nSyLC2mm-fdxsnfxzR0oQ7n6QYv3PNwX-ESTeg3yJbZFZz8Hz_JHX00CHAPW2-dHzSgI1I7anSJFIi69cP3PphDG-M095qkergGRUFHojhFPvIJI0te06tmeaiTetR5vJ7ChcC2_tobOOgqNL_zy0aL72WwG4jxqB9bIY8JTbrDAdiF98Whj2qdFa7-cg0RyqCRvw5luLIPbi9kZsHbtR6Stfyiv5r9nVBcuc8OwhG33EyfcbccAjS_fZMr_vH54tSivVcbPL5TureSV7yxeLfzdUFR5l87jRnGnSMBHMbUGhxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اختلاف میلاد محمدی با مدیران باشگاه پرسپولیس تنها 3 میلیارد تومن است و مدیران باشگاه پرسپولیس قصد دارند با پرداخت این مبلغ قرارداد محمدی را تمدید کنند
/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/SorkhTimes/131573" target="_blank">📅 17:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131572">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس خواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 753 · <a href="https://t.me/SorkhTimes/131572" target="_blank">📅 17:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131571">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/SorkhTimes/131571" target="_blank">📅 17:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131570">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwIZUgTXjzmYtVaLiA2Upkk5dp4Vl5sXEX2LLEq_tPbeVnXFyx87sR8P9NL1U6YERySRx5LbMLv-vuYgNUiUqI5Gs8rMFV2EIJD5TMxlR9htIPet11LFeYF7motXVWyFpoNXxr3KceZ9eYEPE1r7d0wciL6Jt33W7rT0cEJdg07KWt2hqcSret0HFjZRqXUg2dWloiPNtww5ymcDBGwvTkV_eYh3iNKorRG7bH-MRh65emsnPr4lh2M3wSfnW10f3Zy3wmycb-XuBuifqP5Tr676DKZs_LbApJRKYC3PR0Qv9bL8jXGJqGWtydWB58NNfBI4tJHidxGrodtxmbBiAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شباهت عجیب لوکاس برالدو و محمد خدابنده لو ستاره های خط هافبک پرسپولیس و پاریسن ژرمن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 797 · <a href="https://t.me/SorkhTimes/131570" target="_blank">📅 17:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131569">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/SorkhTimes/131569" target="_blank">📅 17:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131568">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 825 · <a href="https://t.me/SorkhTimes/131568" target="_blank">📅 17:20 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
