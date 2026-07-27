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
<img src="https://cdn4.telesco.pe/file/cQ79wbpHrLoLNW_V08LYYBqZCW7DauVVwShr6iOeZvfqQdj8SSg-QuMkso11oqHTqQ3kA_-RV7rQwWNWbd_IHFnkC2rzvJC5f8KRCUf0ft9FSZ31PPiYFuhXweAr9el7ZlYmsJylD68F1Dl5R0cRVmosC6OFYK5hOxDaagLqNpKLO9rxMsZuq8DPo_xr7XYAxWPVsxPuJ7OwgwsZstWrHJK6vlTukEQzy2amHc6oDbSQS9GRmOTgu4F_oLGQUQawHmhKYo-eiA7WFop5JXz3r1yk_kYn83BgNruI1Eu6Yc0aQsGDmR_pLnuvFR-SvnmcAa6e2pHwqNVtgz6_ndJnBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 961K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-137845">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9015499bb8.mp4?token=ocZRf9GvHqWnWkFUsUf5d8590sEcvtaB_h1dhm6ejv2VG7scGsPT6x8WUo6czkIj9oL8PFmrwwCxOtx3uhDQ8wbz-XQqvg6kWMkNwocKWrOXygViLApvnJE6XiSD1HcbRFu_raFHYD2ZYjP_HQ5h0w-7YrtuwoVr2Vhyj9iH8eEVbSKmVhJramKl5DrxQGSxamkE9z0Z9QG8pGa6rDC3gt86IP8EM72cD5CpL59b65qIKtF7IOD57wqSOM5XtZ_I_fndKolbTh8xmfijeMHrxLBkq6EacHYrTYc-VwnJtUhoIegXeGSz1zHIZ_vAMMburMhXoZbUknml_VdsZKbTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9015499bb8.mp4?token=ocZRf9GvHqWnWkFUsUf5d8590sEcvtaB_h1dhm6ejv2VG7scGsPT6x8WUo6czkIj9oL8PFmrwwCxOtx3uhDQ8wbz-XQqvg6kWMkNwocKWrOXygViLApvnJE6XiSD1HcbRFu_raFHYD2ZYjP_HQ5h0w-7YrtuwoVr2Vhyj9iH8eEVbSKmVhJramKl5DrxQGSxamkE9z0Z9QG8pGa6rDC3gt86IP8EM72cD5CpL59b65qIKtF7IOD57wqSOM5XtZ_I_fndKolbTh8xmfijeMHrxLBkq6EacHYrTYc-VwnJtUhoIegXeGSz1zHIZ_vAMMburMhXoZbUknml_VdsZKbTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت ساحل دریاچه ارومیه را مشاهده می کنید که غرق در زباله و کثافت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/137845" target="_blank">📅 12:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137844">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErqnzHgbKuKr4kHGuyW-3FUErgGGmiit5LL60d1f4YJbjxMDUU6gSc1xcFMP5OLVv7kzxwJAxP8f3JCjiW4ZvlmINjOw1L7FFUyKwMnFOogkQQyLNvu0IVCoBNqNYAtlck3UM5bWe0VIeTPdhzEIeDV2lw6GadB0gkLAcE9iPeEKsejIiiD5G-gfZcix46wYMHsV4o0CL4-vj5oGenNbaZhCtR4HihifmZvJLEB4uCypFwrFutnrbb0LWiByuBlDevy_v97wor3KZvfkc6_nHlbekboLLJN3RReZESLff-KFlIdiDMjl_XbjAwAXvScW_c3TrNGkXMKaufOsFFyEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از نیما مرادی، جوان انزلیچی که در حمله اوکراین به کشتی ایرانی در دریای خزر جان خودش رو از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/137844" target="_blank">📅 12:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137843">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26576790db.mp4?token=uSIdil5fM43E39cQ3tSkiJV02bzBlP0M1Gq3piztqvTHiZBtp6yflktV3hlJ1VMJchRzwwJpOez908akSKd6RQhrTshu87L5IXFKyoeY4sTzgOY7wma8KlK1t3FK-9IuhmFRNCUM1z8Ne__nzexqfXEjDME40qZMK3RBeuWxwr9iJPmasxSXMMiF1qEer12eA1ozmZJq00HqBIfeA0gMQqYDcIyzw8qYwPFVJA1rVY_PN4ikKrPE1R1RQhtXZFxq8f2RNQiYDsw3SAyS_uEPm2IYp8GEOlvy0MsYyT03XwX_QiC1GlZqKDGk8PGaKbDcjPscdVoH6sdE9d-0K-tuWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26576790db.mp4?token=uSIdil5fM43E39cQ3tSkiJV02bzBlP0M1Gq3piztqvTHiZBtp6yflktV3hlJ1VMJchRzwwJpOez908akSKd6RQhrTshu87L5IXFKyoeY4sTzgOY7wma8KlK1t3FK-9IuhmFRNCUM1z8Ne__nzexqfXEjDME40qZMK3RBeuWxwr9iJPmasxSXMMiF1qEer12eA1ozmZJq00HqBIfeA0gMQqYDcIyzw8qYwPFVJA1rVY_PN4ikKrPE1R1RQhtXZFxq8f2RNQiYDsw3SAyS_uEPm2IYp8GEOlvy0MsYyT03XwX_QiC1GlZqKDGk8PGaKbDcjPscdVoH6sdE9d-0K-tuWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی :  بخش زیادی از مردم و نمایندگان پارلمان بلغارستان با میزبانی از هواپیماهای نظامی آمریکا مخالفند
🔴
دولت بلغارستان باید بابت این تصمیم پاسخگو باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/137843" target="_blank">📅 12:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137842">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بقایی:  موافقت ایران با آتش‌بس ده روزه واقعیت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137842" target="_blank">📅 11:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137841">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری /
بقایی: هرگونه اقدام آمریکا با پاسخ قاطع ایران روبه‌رو خواهد شد ، در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137841" target="_blank">📅 11:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137840">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بقایی: نمی‌توان اسم وضعیت فعلی را آتش‌بس گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137840" target="_blank">📅 11:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137839">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:  چند دور مذاکره روزهای جمعه و شنبه بین ایران و عمان برگزار شد که مفید و سازنده‌ای بود.
🔴
این گفت‌وگوها درباره نحوه مدیریت تردد کشتیرانی در تنگه هرمز انجام شده است.
🔴
هدف این است که ایران و عمان، به‌عنوان دو دولت ساحلی، سازوکارهایی را برای اطمینان از کشتیرانی ایمن در تنگه هرمز، با رعایت حقوق حاکمیتی دو دولت ساحلی و همچنین حفظ امنیت و منافع ملی ایران، تدوین کنند.
🔴
درباره وضعیت تنگه هرمز نیز تأکید می‌کنم که هیچ تغییری ایجاد نشده است. کماکان، به دلیل اقدامات تجاوزکارانه آمریکا و ناامنی‌ای که این کشور بر منطقه تحمیل کرده، تنگه هرمز بسته است.
🔴
این مذاکرات هیچ ارتباطی با آمریکا ندارد. موضوعی دوجانبه میان ایران و عمان است و گفت‌وگوها نیز همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/137839" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137838">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه در مورد ماجرای دو دیپلمات فرانسوی در ایران:
آنها به بهانه ارتباط با جامعه مدنی، مرتکب مداخله در امور داخلی ایران شدند و برای خود مأموریت‌هایی تعریف کردند که اساساً، طبق همه تفاسیر معتبر از کنوانسیون روابط دیپلماتیک، مصداق دخالت در امور داخلی یک کشور محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/137838" target="_blank">📅 11:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137837">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a72fd89b2.mp4?token=iKgfclxTjhpwo9mf2Wbxeop0TrRSwU6liW4JITItEPd1Vk5EqzA7TR22jle0W_RKpCVqEEqtz86EZ3wDRfp458KZuFKvstgoD_d5mz7nFdVKfvvKaM4USWOlwcutOeS5QI98-DHNbCWnP03ziRuJgie9a-ReV0swzgFpEPXe0-VmqVLfrV43NYUsWsRqDxia5_Qo4b6rPP0UPc1BBLWozkAA0CuMQpOz7NCv_6Mlq9S-8KpBE7M1684JxfXdzalYq_ytS5MQHou40MA3K8zswR3CTjx0YwvRxREWHff3jAB1cBy_X_1NHcY_iKztUL-LVWy1OMvmAlqi5UqbqfgE-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a72fd89b2.mp4?token=iKgfclxTjhpwo9mf2Wbxeop0TrRSwU6liW4JITItEPd1Vk5EqzA7TR22jle0W_RKpCVqEEqtz86EZ3wDRfp458KZuFKvstgoD_d5mz7nFdVKfvvKaM4USWOlwcutOeS5QI98-DHNbCWnP03ziRuJgie9a-ReV0swzgFpEPXe0-VmqVLfrV43NYUsWsRqDxia5_Qo4b6rPP0UPc1BBLWozkAA0CuMQpOz7NCv_6Mlq9S-8KpBE7M1684JxfXdzalYq_ytS5MQHou40MA3K8zswR3CTjx0YwvRxREWHff3jAB1cBy_X_1NHcY_iKztUL-LVWy1OMvmAlqi5UqbqfgE-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: شایعه تعطیلی سفارتخانه‌های اروپایی در ایران را به حساب جنگ روانی آمریکا بگذارید که در آن استاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/137837" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137836">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تصمیم‌گیران بلغارستان باید در قبال تصمیم خطرناک استقرار هواپیمای سوخت‌رسان آمریکا در پایگاه‎های خود پاسخگو باشند
🔴
اطلاع داریم که بلغارستان پیش‌تر نیز اجازه استفاده از فرودگاه صوفیه را برای استقرار و بهره‌گیری هواپیماهای آمریکایی، به‌منظور پشتیبانی از تجاوز نظامی این کشور علیه ایران، صادر کرده بود.
🔴
مردم بلغارستان به‌خوبی آگاه هستند که مردم ایران هیچ مسئله‌ای با این کشور نداشته‌اند. ما طی دهه‌ها روابطی مبتنی بر احترام متقابل با بلغارستان داشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/137836" target="_blank">📅 11:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etOcoDooijkbHARVUMmct4oALxNAYApGSWlOiCFAauEydXCIun7469R3XoamRxRBMYsnAU7zt_kexjAx-SQ2EjF8MuxVI8SkDBauc5Z1MzTmqvxUNcZLo_KIqlOsVsvdL61jam2Yptz6CSVKpQwn9Li_RcuSw2XvV8LenPN-5lXD7A00GiAjBhdK5phL22U6zqkm2rD3ufG8ZRW2xpXkO9rylBwBRV6-12StDYeMtK2WI0Vmshb7PKMtjXp02Kk0LdCXTjsghK1xVuR50OBWPsmb-Wb0s5topYhPbmRrQ0kHSr9_A4x6gW7jXx8GFdgw_CZk5d3Sy4J1kOA6qulogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماجرای عجیب قاتلی که همسر اول و دومش را به فاصله ۱۵ سال به قتل رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/137835" target="_blank">📅 11:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : دو پهپاد تو مرز اردن منهدم شد؛ منبع پرتاب در حال بررسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137834" target="_blank">📅 11:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=eHdM4jUADq9aKPu_I398EOGKgMSlDG-h31GGTMSO475yVwzuPoFqgohHNY2Yj2cg62aveKibr-UZZOT5Y-90Nq60WDRWCPnJp6nToKJ2_YwbTP1Z-neq74NC4VcKGwZ2Pj6eMUhXddd5ViW5y8snSANV3QenvHH6wdKNmhiNoCrFudbGzzMEyDhVeIiWa7LtBromlxY-53q7Me8H_Ilu0H-0V0NZlnKp9Ss42MdGAfawpB4bs3w_Ub5WmYYvG2Jm72j7W3g0b1JQouwFFOcqqE1ZwadsM_S1SSimSi_7zev0zPQWUQE0XjTHWI09AxhGm0RMQUrWhmgtD5W13aCwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=eHdM4jUADq9aKPu_I398EOGKgMSlDG-h31GGTMSO475yVwzuPoFqgohHNY2Yj2cg62aveKibr-UZZOT5Y-90Nq60WDRWCPnJp6nToKJ2_YwbTP1Z-neq74NC4VcKGwZ2Pj6eMUhXddd5ViW5y8snSANV3QenvHH6wdKNmhiNoCrFudbGzzMEyDhVeIiWa7LtBromlxY-53q7Me8H_Ilu0H-0V0NZlnKp9Ss42MdGAfawpB4bs3w_Ub5WmYYvG2Jm72j7W3g0b1JQouwFFOcqqE1ZwadsM_S1SSimSi_7zev0zPQWUQE0XjTHWI09AxhGm0RMQUrWhmgtD5W13aCwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا می‌خواست در ۳ روز ایران را تسلیم کند اما حالا بعداز ۵ ماه در باتلاق خودساخته گیر کرده
🔴
تصمیم‌گیری دربارهٔ منافع ملی کشور معادله‌ای چندمجهولی است که در یک روند مشخص با مشارکت همهٔ دستگاه‌های تصمیم‌گیر انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/137833" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137832">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رئیس پارلمان لبنان: اهمیت ضمانت ایران، عربستان و ایالات متحده برای حفظ ثبات لبنان
🔴
تنها راه قابل قبول، عقب‌نشینی کامل اسرائیل در کشور ما است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/137832" target="_blank">📅 11:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137831">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97719a0a75.mp4?token=gAJkZjk-_JVD22TNvxnwsiFs1ayWdqhbcdsBFv1bhmMSpSsFenV_Uztv-3Fa9fRDrsof1YaM9NI2YEzu1gXqqMX9N5zD7gdBdB7e0gCqzK3bcR3PKO3WPwm-4VYj_lhmxqSiM1BIe7IsLJlYkPFFmCypYkqPQwRBXj3SPDPnoPD4Epv5ThsYSCP3Rj7KY2CNNXmIhy80K8aPLTx7_jJX5ZoYZYZ9wX5avAu7Kr9B9iOsEvigb_zB5V1WMv5bp-18eJnG4lKLTfs15p0byXfTG_htdAn3dQoCc9AHcPwGPM7pAd78xZv8P1TqVFb96rgjHr7NOhsDtmsps1AOstEctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97719a0a75.mp4?token=gAJkZjk-_JVD22TNvxnwsiFs1ayWdqhbcdsBFv1bhmMSpSsFenV_Uztv-3Fa9fRDrsof1YaM9NI2YEzu1gXqqMX9N5zD7gdBdB7e0gCqzK3bcR3PKO3WPwm-4VYj_lhmxqSiM1BIe7IsLJlYkPFFmCypYkqPQwRBXj3SPDPnoPD4Epv5ThsYSCP3Rj7KY2CNNXmIhy80K8aPLTx7_jJX5ZoYZYZ9wX5avAu7Kr9B9iOsEvigb_zB5V1WMv5bp-18eJnG4lKLTfs15p0byXfTG_htdAn3dQoCc9AHcPwGPM7pAd78xZv8P1TqVFb96rgjHr7NOhsDtmsps1AOstEctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: بزرگترهای زلنسکی باید او را کنترل کنند/ ماجراجویی خطرناک اوکراین قطعا از طرف ما بی‌پاسخ نخواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/137831" target="_blank">📅 11:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137828">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQv_-YNWo_A6IFPSD2YBz4zUQOwfOwtuLi8qZhOIbBhc9VSNJI6BqACDRk71qCAZMaiQkUIQtE2Tw-n-dOtY8QiVgZYCBW--7J_Gx8d5fsOqsHKgQpMKRVTDOeXv0b52AxF0XU7xvRJ6moZVMawZgAH0_jbS2OSSVchYasVnhiLHzwQpvrlpFH8j5xSyBZNLSFyr8J_7EQ-IZK6M2eLuEnwY6tW3z_IlwrgBgZCVi152vDqPxZXTHzPO01pv63jTXeTZ4_Ly3MMzDVGZhwpas8Mwa6AeozbcQ9B2Awcr8K51S9h9VVggWu9G771-dCJwpoMnI4LOiyFRGRXqUQOubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvPDQTaXx_P_kC0qsuiSQmSCUgGSdLPjZQUTDBKmE-s6uxfl5DU4O0QcAWRKY4GwInuYu5g1zY9OlzGmsjGr_LATc6PRZi4bHIA9X3E7JcvUGwa1IAMFmb0EOI-8VFYwymETb86W51a621fj1F6Z1uKTI0tMviF6qIf3jKLDdSXgryERObl9DotbS5HRw8BvrfFxTY3JiFu4Zk6RtELrYJVPCB8Fa49xYGo0B8KE5ZviId5ukX8JhUVH_AnJPF8LsGelWLZfxsoTLB5Eq5GMGRXmW24nNtGh1JiXFAt8r2Hee6Kz_fZfCC4vY6KIa2H4o22Vn0nWI_ZGkytE7bOjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQ75LD1DpbjSWtqzj1-DeelxdZnGuhbExrYpCsH0c-oqtlOpA54ZmWIHUKHURsCaghFmBdYLkNwar56ZR1_7zpskPeUZ3KSXqmPNCVDBbj6eZJLIzh3cneAOKneY08NSlayeFJmvPln3xzt-JVvWPqoza7FwiPGWDRykkISfHbHIbU0lXCk6MxBYr8s8s3r6hLFUuVr5MiGG-spEv7TfXp-YkIv3ePk4p_9zBuYOBWOE1mE2SrFPyrV4xSMc4tfNI5KBC0qYhC5rWymd4X4e66BA01kHPkct3OKFC7TKWwBGQcE5ddJq-xyxSmLecraXFWjsyAqlf2qUM9spQK-7Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی گسترده‌ای همچنان در پالایشگاه نفتی جازان، متعلق به شرکت سعودی آرامکو، ادامه دارد. این در حالی است که سه روز پیش این پالایشگاه مورد حمله نیروهای یمنی قرار گرفته بود و هنوز هم دود سیاه غلیظی از مخزن نفت به هوا برخاسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137828" target="_blank">📅 11:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: هیچ وقت اجازه نداده و نمی‌دهیم آمریکا تعیین کننده زمان جنگ باشد.
🔴
هر وقت منافعمان اقتضا کند دفاع می‌کنیم و هر وقت احساس کنیم از ابزار دیپلماسی استفاده کنیم حتما از آن استفاده خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/137827" target="_blank">📅 11:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137826">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند
🔴
۲۱۹ شرکت خصوصی به‌دلیل عدم رفع تعهدات ارزی ۲۳ میلیارد یورویی به مرجع قضایی معرفی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137826" target="_blank">📅 11:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اکسیوس اعلام کرد که دونالد ترامپ رئیس‌جمهوری آمریکا فردا سه‌شنبه در کاخ سفید میزبان ولادیمیر زلنسکی همتای اوکراینی خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/137825" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سی‌ان‌ان: موساد اطلاعات کوه کلنگ را به آمریکا داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/137824" target="_blank">📅 10:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ولیعهد عربستان، محمد بن سلمان، در گفت‌وگوی تلفنی با نخست‌وزیر بریتانیا، اندی برنهام، درباره تازه‌ترین رویدادهای منطقه گفت‌وگو کرد.
🔴
نخست‌وزیر بریتانیا یورش‌های حوثی‌های یمن (انصارالله) و تهدیدی را که برای آزادی کشتیرانی در دریای سرخ پدید آورده‌اند، محکوم کرد.
او همچنین بار دیگر پشتیبانی بریتانیا از امنیت و فرمانروایی عربستان را اعلام کرد.
🔴
دو طرف درباره گسترش همکاری‌های دوجانبه و همچنین بررسی رویدادهای منطقه‌ای و جهانی گفت‌وگو کردند. محمد بن سلمان نیز گزینش اندی برنهام به سمت نخست‌وزیری بریتانیا را به او شادباش گفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/137823" target="_blank">📅 10:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44efd8a92a.mp4?token=U0kJk-cnwi2aacLndhVlgD-acZQAgDpmH9RqudML2mltOVFWkWp_vGyx6pBgzpA8MjJP8mZdic-jwlyWT6RxCd26SnbUBcfNOiS7ppeZ7m61YBT5mUDhfJeglz7S1s-GOIxFg5yNcONulCoUe0NB_eCRhnpthhNYUl_C7m9M9FwF62-hX6d5ryWPWWw35DmLfmk8dq2Recxfjtc2roqXEut5Up8GXHlPKvE9Vx1w-T3-PKbMuteQgnN_AVq-FCfIwpmGYwkgR9nx0hG1oMP3K_oReNxYmctK-D3f39AqUao76DkAlkvU1bwvRE03QS-JCPobgmBVkbq0ko8TiwPG6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44efd8a92a.mp4?token=U0kJk-cnwi2aacLndhVlgD-acZQAgDpmH9RqudML2mltOVFWkWp_vGyx6pBgzpA8MjJP8mZdic-jwlyWT6RxCd26SnbUBcfNOiS7ppeZ7m61YBT5mUDhfJeglz7S1s-GOIxFg5yNcONulCoUe0NB_eCRhnpthhNYUl_C7m9M9FwF62-hX6d5ryWPWWw35DmLfmk8dq2Recxfjtc2roqXEut5Up8GXHlPKvE9Vx1w-T3-PKbMuteQgnN_AVq-FCfIwpmGYwkgR9nx0hG1oMP3K_oReNxYmctK-D3f39AqUao76DkAlkvU1bwvRE03QS-JCPobgmBVkbq0ko8TiwPG6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده های A-10 وارتاگ درحال اعزام به خاورميانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137822" target="_blank">📅 10:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a9d77e38.mp4?token=VhxPSVinMq7kaxLB-ajue8ifbNoOnK1Aq0dd58VwR4jAoI5nEZB5IdhfvZBjtpUSZ633z0193L8mBnwBCsq6Ag3HeJRvkP72oAp6hbAXGKgYYPfnHxoBN7BY1yEeTHU-MmUYAcg2YSRJq77LXlfVGSYp4XC1y1y7fMtQH6h2M9XVno41jOEV1fZ754NY6cy6k0M8uPQ3ntB1zw7tQzlxeLpC8grarJhttBxQNSks9WMY1ySKbq6cwFcRYnjXHmxreYEAZYKw5eRZK2sGMfyQi2w8KFqDvDLkCf6WxdfytX1p8snL0QQecvs1cKRf-Jv79xYG8xLQwhCzGhmgMVNUoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a9d77e38.mp4?token=VhxPSVinMq7kaxLB-ajue8ifbNoOnK1Aq0dd58VwR4jAoI5nEZB5IdhfvZBjtpUSZ633z0193L8mBnwBCsq6Ag3HeJRvkP72oAp6hbAXGKgYYPfnHxoBN7BY1yEeTHU-MmUYAcg2YSRJq77LXlfVGSYp4XC1y1y7fMtQH6h2M9XVno41jOEV1fZ754NY6cy6k0M8uPQ3ntB1zw7tQzlxeLpC8grarJhttBxQNSks9WMY1ySKbq6cwFcRYnjXHmxreYEAZYKw5eRZK2sGMfyQi2w8KFqDvDLkCf6WxdfytX1p8snL0QQecvs1cKRf-Jv79xYG8xLQwhCzGhmgMVNUoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بازرسی:  تراستی‌ها (افراد مورد اطمینان حکومت برای انتقال پول نفت) خیانت کردن، پولا رو برداشتن و زدن به چاک
🔴
جالب اینجاست تراستی ها رفقای همونایین که میگفتن تحریم اثر نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/137821" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کانال ۱۳ تلویزیون اسرائیل گزارش داد که بنیامین نتانیاهو در نشستی با وزرای کابینه اعلام کرده است ایالات متحده خواستار خروج نیروهای اسرائیلی از غزه، لبنان و سوریه شده است
🔴
به ادعای این رسانه، نخست‌وزیر اسرائیل قصد دارد با این درخواست آمریکا مخالفت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/137820" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
صداوسیما: در ساعات اولیه بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن موقعیت‌یاب خود قصد عبور از مسیر جنوب تنگه هرمز را داشتند که یکی از آنها دچار حادثه شده و بقیه تحت مدیریت ایران به خلیج فارس برگردانده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137819" target="_blank">📅 10:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137818">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
روزنامه تلگراف:در آغاز جنگ، اگر یکی از سکوهای پرتاب موشک ایران توسط نیروهای آمریکایی منهدم می‌شد، ایران برای بازگرداندن آن به چرخه عملیاتی به حدود ۱۵ ساعت زمان نیاز داشت.
🔴
اما اکنون، ایران توانسته این زمان را به شکل قابل‌توجهی کاهش دهد و قادر است در کمتر از ۳۰ دقیقه حملات موشکی علیه پایگاه‌های آمریکا را از سر بگیرد.
🔴
به نوشته تلگراف، این موضوع نشان‌دهنده افزایش سرعت بازیابی توان عملیاتی و بهبود روند استقرار مجدد سامانه‌های موشکی ایران در طول درگیری‌های اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137818" target="_blank">📅 09:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137817">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
شبکه المیادین گزارش داد که نیروهای مسلح یمن طی ۴۸ ساعت گذشته سه نفتکش سعودی را هدف قرار داده‌اند. این شبکه همچنین مدعی شد که از روز دوشنبه هفته گذشته تا روز یکشنبه، ۱۶ کشتی سعودی که قصد عبور از تنگه باب‌المندب را داشتند، موفق به عبور نشده و ناچار به بازگشت شده‌اند.
🔴
بر اساس گزارش المیادین، این کشتی‌ها اجازه عبور از باب‌المندب را دریافت نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137817" target="_blank">📅 09:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137816">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL8d_QJxFQs71EHVa6hfz4qukD0CJcStqfSii7rVfgReSwu4VRVVIqin5qbE9ktkf1Gy-XR2mgwVgl5vpbK0E620EBKJXQi71TRwEtdTdkrLSSidgJOt4XTQzOJhxVql5uh9O9VN8HhYGCJ0zL698wDdgB94kU62TBiyZTxSsbGK5YuxdkJxJeh4U6q12LldGU_ElXUPH__5tJIVErlAwbjxvPTmzgupXKAPBOfcxou6IrTaVw7DP5W-MMCuFsO8ugorIqI091YNl7VmYV834STwAE2clZROr-XPvDfkWyP-O0jJq_oDeRTv9hKOAi83vCbe3QeHAcNAtGmrb1U5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت 92 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137816" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137815">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCF-Yn7KVnqnAyr_MfqIXW5W1JQYprxucPJHJTBDuQ4h7XWCxVvmUg4V1sTqzU8xZTWQaU-Iq_cHq_wly-z3wvTCCb-zUJTUGtzoeMSDK_EvgqKtqBIMiRFK9DzyntcPVHi9Wma1oQWGzTxz1oh4RwvbrCZOkFGSVU9uMaQwgjcR0LjDBnxMXt64ojzNamOkdmwSTA3n0cPs94zhjaziZs2j2_pWJN4y2GyuIXXkbSQ7kzkKPWP3DWQgNGLEhQitVVy4jECpKGM9p6aerNgMDUBAfgTVIDl8FMDPQ1UBxzn_MH6IAv50Xqm_yb4ZBjieBWKbFZngIO-GYE1a_f2khQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران هزینه داره و آمریکا و اسرائیل این رو خوب می‌دونند
🔴
اوکراین هم ممکنه به‌زودی بفهمه که ایران اقدامات علیه خودش رو بی‌پاسخ نمی‌ذاره
🔴
فهرست کسانی که دچار اشتباه محاسباتی شدن، همچنان در حال بیشتر شدنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137815" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137814">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سی‌ان‌ان‌: بر اساس اعلام پنتاگون، بیش از ۱۴۰ نظامی آمریکایی جدید به مجروحان جنگ علیه ایران، اضافه شدند
🔴
نام چهار سرباز آمریکایی کشته‌ شده در حملات ایران که از پایگاه داده‌های پنتاگون حذف شده بود نیز بازگردانده شد
🔴
از زمان شروع درگیری‌ها در ۹ اسفند، ۱۸ نظامی ایالات متحده کشته و ۶۲۴ تن زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137814" target="_blank">📅 09:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نیویورک تایمز:مسئولان آمریکایی اکنون نگران هستند که پوتین و شی جین پینگ ممکن است کمبود مهمات آمریکایی ناشی از جنگ ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند: در اوکراین و اروپا برای روسیه، و در برابر تایوان برای چین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137813" target="_blank">📅 09:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کیهان: فریب آتش‌بس ترامپ را نخورید؛ ذخیره تسلیحاتی دشمن ته کشیده، وقت شکستن محاصره دریایی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137812" target="_blank">📅 09:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رویترز به نقل از داده‌های ردیابی دریانوردی: در طول تعطیلات آخر هفته، روزانه کمتر از ۱۰ کشتی حامل کالا از تنگه هرمز عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137811" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نیویورک پست: سناتور جان کندی روز یکشنبه مدعی شد که ترامپ دوست دارد هر روز به ایران حمله کند و از آمریکا خواست به‌جای تعلیق حملات برای اجازه دادن به ادامه مذاکرات، فشارها را تشدید کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137810" target="_blank">📅 09:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2054add09.mp4?token=M5k00xP70DxYvFmxD79kE3Uw60SOa9WMIdmwrGHDBB9mVZvRQzMo_rRkfbgLXuaNJO-nF3JiJptLoDt2cChfdmNlPN6btghUpx3jjy3AlxPZVTOHe33xPe0j8h-lH3QmptolNlfComSqOKSPNIUAiYT6-SisoDLxtZhdg2ah-gZmdAh1XaByvKYN6CDtFlmWZ6pyOvYiUOgq9ofLnB3SLFuxcEs5JW6f9uoWAIjESTLBQNXddQyotwMaA-IYZ68Wh_U_5UCdphicE4wlZr5hAFWe54XZIrHg9IH7OhKQVWXVnYkNVQUOk7GO5wyASoCLY_lJmhW-C8tTcevMe2wMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2054add09.mp4?token=M5k00xP70DxYvFmxD79kE3Uw60SOa9WMIdmwrGHDBB9mVZvRQzMo_rRkfbgLXuaNJO-nF3JiJptLoDt2cChfdmNlPN6btghUpx3jjy3AlxPZVTOHe33xPe0j8h-lH3QmptolNlfComSqOKSPNIUAiYT6-SisoDLxtZhdg2ah-gZmdAh1XaByvKYN6CDtFlmWZ6pyOvYiUOgq9ofLnB3SLFuxcEs5JW6f9uoWAIjESTLBQNXddQyotwMaA-IYZ68Wh_U_5UCdphicE4wlZr5hAFWe54XZIrHg9IH7OhKQVWXVnYkNVQUOk7GO5wyASoCLY_lJmhW-C8tTcevMe2wMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو موزه ملی کره شمالی، جلوی تابلوی کیم جونگ اون، رهبر این کشور پنکه گذاشتن تا گرمش نشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/137809" target="_blank">📅 09:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137808">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خبرنگار: آیا نگران این هستید که ایران به خاطر اتفاقی که برای کشتی اش افتاد ممکن است به اوکراین حمله کند؟
🔴
زلنسکی
:
ایران از قبل به ما حمله کرده است، زیرا سلاح‌هایی را به روسیه ارائه می‌دهد، امیدواریم جبهه جدید جنگ با ایران باز نشود اما ما باید آماده باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/137808" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137807">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77fd55a10c.mp4?token=DG_S0qaHg1zZ9uqyAa7cSGYLV5Ik_AMbvtWsbO3cZ5NvwBtIIY5xUGO1BfIbgvj7RJxNr62Rw0MVTDeBtMrUCI5iJL4QwOhxYCcuLwFQ2FOBnkwwLEkvLWn3tqYSxzQX5cQd9oVSJNV0OgD4vAfHM2Bf461wUJCpLzoFvo8_Pwx4-2yTFNi53v9I_VRYE6J5t6g1bGXmfhhSWzSdi81jVFQKg6SgeyDkUwTtmvjNe6OZUA4_6C6hHMLOeWth8elOxNgiFvO3ggEB0rHqhW86JFh3RAN6zRVgq1_wbdRAYYOPCgJlV77dgTpA0u9Z3DzpLjazj9GPMxSpKFWXei7XjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77fd55a10c.mp4?token=DG_S0qaHg1zZ9uqyAa7cSGYLV5Ik_AMbvtWsbO3cZ5NvwBtIIY5xUGO1BfIbgvj7RJxNr62Rw0MVTDeBtMrUCI5iJL4QwOhxYCcuLwFQ2FOBnkwwLEkvLWn3tqYSxzQX5cQd9oVSJNV0OgD4vAfHM2Bf461wUJCpLzoFvo8_Pwx4-2yTFNi53v9I_VRYE6J5t6g1bGXmfhhSWzSdi81jVFQKg6SgeyDkUwTtmvjNe6OZUA4_6C6hHMLOeWth8elOxNgiFvO3ggEB0rHqhW86JFh3RAN6zRVgq1_wbdRAYYOPCgJlV77dgTpA0u9Z3DzpLjazj9GPMxSpKFWXei7XjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهین‌های شهبازی به پرویز پرستویی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/137807" target="_blank">📅 07:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137806">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6494dac8a.mp4?token=o9-uq5LjUEj811jfsIJMgKEEvon07cwSaKpRWDYTsjeb5u34-RS3aJK9NqNKKwXYV2s_cCUoSNNOuc8fYkCPcUUBXwIYAkYan3W76AlvIV-kWoLqsI_M7fhvWjgZ89UqHkGsCTIMrhxyknBCoj4DCf_UCIHMGpANdx09z_z7ShwROR0O_mgyWDsxI7xoYx6K1-4TbpST77ZdWTEpZrCh7XNjPkUKz0OdULACzVS0LbhV8MUzJzyeJp8HBrNBg0fbyR2LmIf0g0W-Z7Et0AOg-kRKEHgrca1lwZe2WTkyhvCptw6_v7ON1mVVSnflrOdq3guRKHLydh6pIG1QVGuR1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6494dac8a.mp4?token=o9-uq5LjUEj811jfsIJMgKEEvon07cwSaKpRWDYTsjeb5u34-RS3aJK9NqNKKwXYV2s_cCUoSNNOuc8fYkCPcUUBXwIYAkYan3W76AlvIV-kWoLqsI_M7fhvWjgZ89UqHkGsCTIMrhxyknBCoj4DCf_UCIHMGpANdx09z_z7ShwROR0O_mgyWDsxI7xoYx6K1-4TbpST77ZdWTEpZrCh7XNjPkUKz0OdULACzVS0LbhV8MUzJzyeJp8HBrNBg0fbyR2LmIf0g0W-Z7Et0AOg-kRKEHgrca1lwZe2WTkyhvCptw6_v7ON1mVVSnflrOdq3guRKHLydh6pIG1QVGuR1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمدتقی نقدعلی ملقب به شپش:
آمریکا و اسرائیل نمیتونند جمهوری اسلامی رو از بین ببرن، ولی این وضعیت برهنگی مثل خوره به جان فرهنگ دینی ما افتاده . سریع اجرای قانون حجاب اجباری رو راه اندازی کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/137806" target="_blank">📅 07:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137805">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj1GHz-KOUkGw-1P01qEmAntaRj-8dqa6MCINZphBl3YL9I4X0TYmUs0ylVr-_FZokCm7bqOKl0jsBfcAWGR8az3F4jxj3b7VTkxGAu5cpd6r-fVLRqTiL3Xh1SsQojq5U8PnJCwrcNMVunb-Xs6_OryiSJkWLt-HgKVmQ6L-l8z8m1SruB6mCYWsi_1q2iGm_yVqUwWZOYg57xRiZvMoZnC4_HfFULjQp5QX6nWSpD3lY9M9zAAvqgqoAZKbts62ZPp5jnO9a0YvxMGdG_YImLfBu05MLKo8k9-zVBS9ry7SRPQUNNc-2GdzFL7rtjq55_PVSwT9Azsia8Sfd3tMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/137805" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137804">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sklPqnC3DI_EiV77R-T5v5eCUiHH7EbNZ07D8DeT5DFKnNNulishe2CnfP6wIPDVyh6xhu7kdUTzoXWpMJRrTpgXVN-M1PaGuuSMFQF0pU_IX-eAUDAMjyIfJVTH2_dDIpwhfAS5g1z-9RrNXPqbjSQUCfT8znra_e45DO_ouRYA3XURcOftLeuyFEXMeX6KI-7WS7IPCvkYlk8b-ZYLaCx5uVDjKsZCuucqcjZeKPTx-Sli60cXccB2mRMxNNkOibquVHHLdWCbuWYjO8AXdcCU7q5lntdmSiFGYO5rLB1VOnfF-Y2P4qdi87Yp6Gw1jLGE37HfcweTiZ94WPLGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلوی هست.
حستون رو با ری اکشن نشون بدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/137804" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137803">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_e44PjddYWHkPSsNrWYCXBhdiQqRmtDEkxGE26kVezKnVZbmMcsY_cHhvj7syXidYo6Nu2SqL4MIP7ycVU370OxszHqsTjYPb9i6OYr8Z1TrYuy3SlF242FnWzH2dyG2P7_48ad1XhuT-hozWMhiVRn7yWSfDY9sofTfN8o0jlGgdvyt-xr_fTkf7vWUyx1KRDVtL6yJiO7b5fN5J29_2bXlbM_byMLQ8myofQH_6MRXiB77aXrgYA6RVImBpEBlcxc_-yRM7w16Pis4N_-QEIVk1wtPkaGT0YRLuUloorsu8fejy8OrMy7dxgYJnhCzT69Fx6Rs88LM2nIAjaN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک منبع نظامی خارجی: به نظر می‌رسد نیروی هوافضای سپاه پاسداران در حال آماده شدن برای تلافی حمله سرویس امنیتی اوکراین (SBU) به یک کشتی باری ایرانی در دریای خزر با استفاده از پهپادهای تهاجمی یک طرفه است که منجر به کشته شدن یک ملوان غیرنظامی در آن شد.
🔴
کی یف تقریباً 1850 کیلومتر از تبریز فاصله دارد و این شهر را در برد موشک‌های بالستیک سجیل-2 و خرمشهر-3/4 نیروی هوافضای سپاه قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/137803" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137802">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufBo3to-97oAbl4NRk6IKfJeTvC6xZ7ZMqOuR6HYDSGInxDfKbVpN_etntPXtBc2L-v9LQ6u9iADsBDbPiDFyuhyp9W69gbIKLJao7hzwSjiq4e9Asp7J08UHZYr_qPIO_jJpGQU8EcijvNoB4QQkggcT_RgChbSss6nN-igJWtO3czewHsVpaRlrZPEEvs17u9bFGGP331QnX2YqhvK77Vw10aWxBu-DQDlqvsUeW425P0yiDXmme49Ro3G73MpTqCu_t1H_WydtMKmitexDGYl1DOcn5w9AI1dKASnmL5v1EevH62rcbPo7BaEDHz9UQjFyAT8WObs73ERkiLquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ادامه خودشو تبدیل به دکتر کرد و نوشت:
این ستون مهره رو میبینی؟ این دقیقا چیزیه که می خوام به جمهوری خواهان برگردونمش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/137802" target="_blank">📅 01:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137801">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-C6HVHJcJ5hQVwQ7lp7PmI24ORdiL3UuJuXsYbiUE8Zboy9f8sSFyPfp_jDT7MWFQp-uSMqaCo2mV1KKsma0F5zbAs93AKvazGPxJAybLPEqeNS4lK80VeqvJi2tD2l9zrkZpFiiRBDW8I4H9vFOPoPKwb5rAH0wv-u5zLWYnHNUJBCwdqoGC5x9xnrHyZwrGYl-W7nOvKPouZY5UOYOhkIfgAXE2WIDBoA4MC2sX-Gs6jA6E7muOVEyN7oYYHTJaqjTwuDpDb_TNdTb4Wv4dKSX55GLMICok-1kqQjVfFjwDb1xG8VvxS57VYEGKlQNffAxWnuDL03QwhwpxJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: این نفتکش حالا متعلق به ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/137801" target="_blank">📅 01:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137800">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گویا آرام بعد طلاق از سپهر وارد اونلی فنز
😐
شده و داره تصاویر... رو به طرفداراش میفروشه
😐
چندتاش رو خریدیم و گذاشتیم
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/137800" target="_blank">📅 01:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137799">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcS6HCvrCD2k1gXwN1SvEHGzEgR3aFq9kUYng6qXngcHjCVmLnz5atGytez5E4svjpknuzSjvP23MtMVggsju7xBixj7YjjnNAkvDjUupkBlT08WzzZSWOOst1Sfqhh-VRNqN4ucYswGEE-33Y1VKB9YATYHI2wYT85xZrxl61BAuBaOUQMwlUsFIxkwAdiNPFqOpE46AvWbCGOaZ_QLIe01xd-wXY_0L5LF0WCUMX6M2dlNkhaUgdQkUVG-xoqs9diMoMHthfHWI-pPrGQVtGaVmoF4V9R7a4l2OxZIOMOfRMWaIeurHSypReh28iNTyna3TJHFT80-6-gxNrs-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفت فروند هواپیمای سوخت‌رسان و یک فروند هواپیمای هشدار زودهنگام E-3B آمریکا در نزدیکی سواحل ایران در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/137799" target="_blank">📅 00:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137798">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLaanB3gKh0-cjGDedoQm4lA_02epWIyvqI9O3AJtjpyU1t7dlnDhVmJbOvPGdkazhkDxj0XRQaR4hg_70YE5JxO-lQASm4Y6ADNPj-VoIOp9RvdcORRyV1H_mX1qQmln5XJscel8hdfJhylkRuo_tYlr9LQxTUFVnneUij0NdEuFVl0uxQT3yh40oPERKn2wMO3mtZnFg8n7qsV5DsKS24wO59utI6zgv4yW-BWp2N8Mn4bLsVd_fUpxfLOAPGw4_cIoro51krGegZhCJAkk6z6XM_0IvaGqkHV-k-CITv4X1lormrTZkTZd9OP1hjNg0nW5I3srx36uOJk6NPANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید دونالد ترامپ:
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/137798" target="_blank">📅 00:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137797">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca4847374.mp4?token=uluX-FnO8ntJD4EYXaEHH9cb8dhektlnuuXcvwIaxauVJy_gdGVUYxJKxxebdlbHnuWzxNoG1mSagi_7nkx69R_7yZWTCcPBPwSRihQYNmw9DwbuvbKL69wGxvIZzQIPnIB_hYiOB96B3ADodWu2uf0IB_jODzwcbaItLpxO-dK7hApEaS5Y98OBJD7E0Z9r80fKwYKdkDIWlb4HBe8m7gPsDhXtJK4P7QFlJqC69L0nJR9MssGT2-HPdiyxaTWgVUWbGCub6q4jq47onp5L0JGdNy8FdvhupD-0ZzbpwkqpLpohDytEhv97W-alKiLSHvnDypvyhTNtmWzCLz-doYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca4847374.mp4?token=uluX-FnO8ntJD4EYXaEHH9cb8dhektlnuuXcvwIaxauVJy_gdGVUYxJKxxebdlbHnuWzxNoG1mSagi_7nkx69R_7yZWTCcPBPwSRihQYNmw9DwbuvbKL69wGxvIZzQIPnIB_hYiOB96B3ADodWu2uf0IB_jODzwcbaItLpxO-dK7hApEaS5Y98OBJD7E0Z9r80fKwYKdkDIWlb4HBe8m7gPsDhXtJK4P7QFlJqC69L0nJR9MssGT2-HPdiyxaTWgVUWbGCub6q4jq47onp5L0JGdNy8FdvhupD-0ZzbpwkqpLpohDytEhv97W-alKiLSHvnDypvyhTNtmWzCLz-doYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرف‌های حق شهریاری به جوانک مینی کمونیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/137797" target="_blank">📅 00:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137796">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
فاکس نیوز:حمله گسترده به ایران هر لحظه ممکن است رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/137796" target="_blank">📅 00:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137795">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKBVVKWGsNwe9DDxkHIY95IWc7IuTg1n3atKJQVCr95aa3LBjG_hPIWbEjiIBr4m-BhmEieUDWkJR0dB_cMnaAkUnpVRhsn891-1t6ByH2nZYPbzFo6DvYtnneFW5cwi-TNxgVSQ8rjfAdZ_sfPoQYdHo0dCVq5T6l0vCcRUhjpSKa5xFiYHjzz2aBBB8LA3ygwdIkCTVYVuwuQz61DjUM6zVFpJ_8XvSIKoAhZEhku0frjAK6JgoO2MxC2oe5yrPKo0NUYAqRftW1_wCPYIGra3zrRJSpwtUMBdNYjYTi-c6i_28nipcD1_oKuJHbhfpMhwyq0aIuG8DoeRK40k4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆕
کانال میلیتاری خبریه
@Breakingpersian
@Breakingpersian
📌
رو داشته باشید  لایو 24 ساعت اخبار فوری جنگ</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/137795" target="_blank">📅 00:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137794">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وال استریت ژورنال: نیروهای نظامی آمریکا، حملاتی را تدارک دیده بودند که می‌توانست تا دو هفته به طول بینجامد، اما این عملیات به تعویق افتاد.
🔴
فرماندهان نظامی در مورد اینکه آیا کاهش موجودی موشک‌های پاتریوت خطر قابل توجهی ایجاد می‌کند یا نه، اختلاف نظر دارند، در حالی که ترامپ اصرار دارد که مهمات آمریکا همچنان بیش از اندازه کافی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/137794" target="_blank">📅 00:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137793">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
انصارالله یمن: تنگه باب المندب به طور کامل به روی عربستان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/137793" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137792">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCkNigcevKyD4AejtWCUmUjKNv8qaq9V4p6YRp3SBPQSXX8QkyL4jDmj-EdTlPKWeREYXTWmzRNrumTMqwdzfgCya3kQ2oeBwhPscEtOheCtXknOXCXEsmG2A5xs0aGmT3kXX428oh8cG6dHES-0T_kRJbpj3WqYR5qvWb53sZ_kSNeWkh72fC8MLOKt9zgV-2GXnLEfRqxRUvVgEepE860Ong0k6gSmMX0kzMQUhVHf_AhhHxwFS7vJNzipkdZUZ8Pe9P_avWXlDn5E-QUJcicoROqyMBzfOfcEPlFoIpUb7cPonNG-3JVp60A0k9JxR4gxROjzuy-G1EELZrnSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/137792" target="_blank">📅 00:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137791">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وارد تاریخ رند ۱۴۰۵/۰۵/۰۵ شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/137791" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137790">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل به نقل از چند مقام: این ادعا که کمبود موشک‌های رهگیر مانع اجرای حمله [علیه ایران] شده، بیشتر به یک بهانه برای خودداری از انجام حمله در شرایط فعلی شباهت دارد
🔴
در اسرائیل این باور وجود دارد که ترامپ فعلاً از ایده اجرای یک حمله گسترده علیه ایران یک گام به عقب برداشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/137790" target="_blank">📅 00:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137789">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a7d60290.mp4?token=ZICe6aFrL1eWmtUjI1cAngRohG-QWu0Nr5JOfTBogwvW2FYqNg8gSbOaA2Bb6KwCTxSqhMEtm0GJAvfcsCHpIH98652DGsrg4YRw1x7tWZVGUuzBnwfuY950CxLGe-6N-RgyxW8YZv7UBn7jbrdKkhZzvUmxX5FnAg50bCH4p-1971soAi4afDTE3a4MpUtuMrPm2H52zjqOnxi3P3Ao6t2_gEzNc_62FG6i-L2hkibDOaOxKS-wfxB5jqjo_5I0ES_hLD-gTHUa-f7-tRVPHmvwNeBVEIQFUWDI0HSqlN7c-6BqsqorDZb8ZW6ldiKLqFihcBtmIQHEuB8mslA9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a7d60290.mp4?token=ZICe6aFrL1eWmtUjI1cAngRohG-QWu0Nr5JOfTBogwvW2FYqNg8gSbOaA2Bb6KwCTxSqhMEtm0GJAvfcsCHpIH98652DGsrg4YRw1x7tWZVGUuzBnwfuY950CxLGe-6N-RgyxW8YZv7UBn7jbrdKkhZzvUmxX5FnAg50bCH4p-1971soAi4afDTE3a4MpUtuMrPm2H52zjqOnxi3P3Ao6t2_gEzNc_62FG6i-L2hkibDOaOxKS-wfxB5jqjo_5I0ES_hLD-gTHUa-f7-tRVPHmvwNeBVEIQFUWDI0HSqlN7c-6BqsqorDZb8ZW6ldiKLqFihcBtmIQHEuB8mslA9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد الشعار، رئیس‌جمهور سوریه:
نباید همیشه مجبور باشیم بین اهداف اسرائیل و اهداف ایران در منطقه، یکی را انتخاب کنیم.
🔴
خود این منطقه باید سیاست مستقل و هویت مستقلی داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/137789" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137788">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وال استریت ژورنال : ارتش آمریکا یک طرح نظامی تمام عیار برای مدت 2 هفته جنگ همه جانبه با ایران آماده کرده است که هر لحظه با دستور دستور ترامپ آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/137788" target="_blank">📅 23:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137787">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سی‌ان‌ان: لیندسی گراهام در فیلمی تازه منتشر شده، تلاش چندین ساله برای جنگ علیه ایران را «بهترین کاری که تا به حال انجام داده‌ام» خواند
🔴
او می‌گوید «ترامپ و نتانیاهو مانند روزولت و چرچیل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/137787" target="_blank">📅 23:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137786">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پوتین : شرق اوکراین برای ماست و غرب آن برای لهستان، مجارستان و رومانی است و به زودی به آن ها برگردانده خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/137786" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137785">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGFkJUqdjzPGYHHlqqX63JTY_cQstDmICrnli44oUXjrYi2_vEXAMDBiJUbwWE67EIGxvcSZZcoSesXLUuzN8ZF61vUs5twaw-OV9Hky2_MW_5J6S25QP4fmwIzZch6kMlIFNp5aiAfAWmo1ZgM8DCNjUppiP3CmEs7a_HC5WDPIwGZskrbgexgnW2lsQge8d3znZAmG_b38Obrqel5gnV49VranEdd5PV60wZN9Ji89J6dpAN7aRe7TomhjHbDI20vo93cvrX7PmdZQCQYx9kL4Ob7IfKp2t-tNaOaRKY8g9lf3vJNtdQ6CsxAsb5qj6-Lg7VoUBn48Wt9SHWWZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ اینبار رفت سراغ بایدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/137785" target="_blank">📅 23:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137784">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34aa341c.mp4?token=jESQZOVMTzx0lV-AAh-ThjemzrCZH7PKLYEPw0NZkhVsN_wORIuTuwX60xux0JrToroFZdU5le11oTZsWf3dyibPG78Aig4I-ZndEoX_gwxr5t1z6Tljh1elLPgKni5WXGbWLU0c_tnHpMRFmQtJhCsDWZ048MWh30Vi0sEGqqINNVngQlOUuAbaRgj6_CkCoyqn6x6lBV15VomFFz-Vs_4xqKl5baaNkPhbdxJyMD8xJaie067-9hoYhXWJ4gUH0RsTdOVUENybe1MFlIsRDWzSpD6Em0y-_ovPwAn3jbNEZs6MUrZB-3xcY631xknI_oLzR2lawlRhWC6rS9Pb1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34aa341c.mp4?token=jESQZOVMTzx0lV-AAh-ThjemzrCZH7PKLYEPw0NZkhVsN_wORIuTuwX60xux0JrToroFZdU5le11oTZsWf3dyibPG78Aig4I-ZndEoX_gwxr5t1z6Tljh1elLPgKni5WXGbWLU0c_tnHpMRFmQtJhCsDWZ048MWh30Vi0sEGqqINNVngQlOUuAbaRgj6_CkCoyqn6x6lBV15VomFFz-Vs_4xqKl5baaNkPhbdxJyMD8xJaie067-9hoYhXWJ4gUH0RsTdOVUENybe1MFlIsRDWzSpD6Em0y-_ovPwAn3jbNEZs6MUrZB-3xcY631xknI_oLzR2lawlRhWC6rS9Pb1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مداح اهل بیت، عباس زینل پور خطاب به ترامپ؛ اینو تو گوشت فرو کن،
خارکسه
جزیره مال ایرانه
😈
در تنهایی گوش بدید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137784" target="_blank">📅 23:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137783">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vc-IdOrbMaCevcOMgnwsAkBNEolO8z0Z2grMe1kA4mx270MET5JPtmnwVNH6XgAuyhJzVhvJNGMnGbHc1NyIMjv-8s_U5KuV9w3bnEktN-ybOfuWDsuAu5hBfp7QJLBmeTsUr5u2xNEmbLMgdx3cZ_DByZgqC-SUznKVmHcTX-XXOfa7Xb2aZwyW5YvVHXP-Sa6fqEOEkJwUXCQPHBJ6RlrS_wXyhwBP-gvbRIe3jgcyj530exHSOwbgQJKO2rwUrdDFSyXLcEEl8Dbip455FORuQJ9l0KSzRPmG7QEKBP2LqEu7zZSpR8p9v3gjaXas6kuYnqTitScnmy3YlYFkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای E-3G Sentry متعلق به نیروی هوایی ایالات متحده، که یک هواپیمای پیشرفته شناسایی و کنترل هوایی است، در حال پرواز از پایگاه هوایی پرنس سلطان در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/137783" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137782">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: فرصت مذاکرات با ایران نامحدود نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/137782" target="_blank">📅 23:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137781">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وال استریت ژورنال: دونالد ترامپ ادعا کرد:آمریکا مهمات بسیار بیشتری از آنچه نیاز است در اختیار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/137781" target="_blank">📅 23:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137780">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxgmjwaeVSdznxWyYj26eQuawqfUzBQmNlX2AqESOsIR21_x7IS9AS74AlcjCPmJBsKajibLOUGXnurm8qiBm8d4cjD91KyMe1u__HMrasxCBO4TPhVFmcxdC3XrXu8ZTDP2ATwn6BkI-HHSCHfYj0Qf6RMpffUDM8Orxhq5qHI-hsztaw748QjIEuts3k3wpan4zOpFIRlVYz7p0fbTASYthDnqFFKY5bk_elj4NHbvHFTGaxQVmScUiCwsKk4TevxuZ6pUT2N0qtW8z7SMh6XGkrIyFWHUQweVFxRFV7tvutJg_lppoXD21Il74gzreAtpGxjtiI0GjMFC6pLMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: دیگر هیچ موتور [حرکتی] وجود نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/137780" target="_blank">📅 23:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137779">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW6nCA6LGeiXrYyOxAmHn6O0_RHiBUgkyxvs1GXa6VNDUJWQiAWn_nDFzTkBldqGXBL_ywO6abrnoOZcwJbvjSG72TPgjiPFJH1SxWs9pq9SIUj6N6omSO0s-BUgIR36q6CPY9biP8XyhoP-gsCotYdFE_cdSWU_q0umhGYiXt7xDJMAy7t0Xl9UvJyFhyzQ8NisaVc_jDvXHTI1BpOZaUmlrG0Mgewm_Z-iyumrqIQWcDJSfwXPLQFrcV0JVnQ11F7LgUpqjjQpeBwjsUDi6NS65zNzi-fS057BXcVJxj1nAeeIYQfTynTma3pb382x9Xn6IJtfxrzRnbYXAHhM6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه اجتماعی Truth Social: به دشمنان کابوس تعبیر کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/137779" target="_blank">📅 23:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137778">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMtZKN8z6Rz7n272btUHjNmWv7c5XCdGj-S1yHvWD3abtA13iOgEE8RLnm2niG8o4ZmFdiyP87FR_1X8W9_aGUIUgOqAqUTirYy-P8anbw1fzhzPepev1PJILKFJYWIROoLEOzvKJ2791J4k8CALyg4IbUaIZWj2fZZF2_9_oD-ed2in03jn6UK28zDW9PjX0I2EfnKiJHlIeGPqJ-dPb8oddGFQ_1UR472hw0atAP1sfVnJq_QFERJJtjOumKa56uSl9NgHKWbJN9BfP76W2zyDZrx9NbOr9WJUezHiJ9o6PFxnyIjoolldrSyaMnW_TioZFsWAFOSN8ZeOukFpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : تصویری از پوستر یک فیلم را در شبکه‌های اجتماعی منتشر کرد که با استفاده از هوش مصنوعی ساخته شده بود. این پوستر، او را به عنوان بازیگر اصلی یک فیلم با نام "فرمانده کیهانی" نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/137778" target="_blank">📅 23:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137775">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnK9c-dTMu-bDgcduVv38rfUCUWSnU2NyJuuOCwUHq9jKCxMH4ThKw1gkWfTjHZRYmd63qWmdv069_v-xJx4FhOmMVx_Yn6EoMjDCS6cV-TjYSHHcMLHTSenoPjAUdf16rCCS0ZfAANWPI0pe5FeYRV6x09bfJFcYwNQGWPjap6xec-3xLVVkCVA4MVJzSCeJ9MXp5KtHzln3Qbd6qp1t75-VVBht-f8P9GJIFNUUwPVcsUm4_I3SYZuoKXZGZT9k-nb3x7izfbeFb5uKooOSO_bsMdoWsIsmtBbIWIBphju1Zv4oQNqBz7I0mqA6PwDhxgoA5rGYY58anhkyoWZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZVil7LdvjpZ5521aTKO-HzZOgmCYofzpZcWDMC_RuH4SRYhcuXCKoJeq062DS9HPnZNYVTD73AyibErtAxnrKm9q8pGpXs1C5QmGxqKSb0MOFgK8WEuZuXiBDzO64-IRak3S9a21FxvWC9quwBioL_rW4vA9WmWZl-4gVUFlfNdLm3nN-75mnZWqANP8dQ9qvBQn_qd3eAlMHOJ8skJh_TkdB1uPtlB-8koSPXhYuja4tPtd9-6QNzULWnpiYDciDgZIff3vGV_L6AzY3ulNgNhKM6aZThtW95xLpmh9GMjJiFCL8GAzaRLDfqE44chLu8aLDLCNl_ZCC0eIDqjXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ToKDnyTYOO0PHvGehcZFEuSMTWGHYYuxRA6Obnv05Gf0Peollg9aEviH9gIU-IOiRS6mNcVqXTeMDzl_Ih8C27uGS_R0vGIXih03eu3IhICRF1-nL0L0JK9pB_ulGD1OYHbbf9DgfWyDVWSZV8lJ-Z17UGAtkQOGZsFPZvd2dTdzknMxRMb68wfv71JVW4JrSh7bufsFXMxUljx-GtrbsJRI0zD37341y9wYAiPiZ1j8LWJdV8cCfMc37iiJ308sVod4JWmqfQvSLP5REsJ_esj5uyC0ax9gbR1D7V2Uxw2i-YVXfd4xy7zb9RnrOkQia5Lka0NtJElGkFa56nxiiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ تصاویری که توسط هوش مصنوعی تولید شده‌اند را در شبکه‌های اجتماعی منتشر کرد. در این تصاویر، او در حال تصرف یک تانکر نفتی ایرانی دیده می‌شود و در زیر این تصاویر نوشته شده است: «حالا این تانکر نفتی متعلق به ماست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/137775" target="_blank">📅 23:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137774">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2aizGebENvl3UZJ8rmjE7QZ6BlB5TBodtZWLhnTaiJX2SlW0ug9mftlTdRKkCsKCrPNKpzBZdhpc4LKRkPWKsvwo04cFW9hxHbF-ijbqyVPk2h8hPTJiVrD4hmyLRS2JcM3_D8YGekssoPvDZDJ52YTyoT9o3ZXA5lfNqoieTE1RTIBCav45XCj7PGjNRFOtkD7XZlpK67oaQ20dlZfyyJySbBX5s_8ZjfE6wqXEfDn3GhvAWms13hPVLrYjhQ23WbVonr4Bfx2umQlh9PXNJqIYPgKxd5Q4uzfsG7GkEcVF9-Kj4z7tAalvsRMSU-Lqi_HQGczlqDLsSPukSCShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ترامپ: حمله به جزیره خارک!
🔴
تصویر شامل یک حمله هوایی و آتش‌گرفتن تاسیسات نفتی جزیره خارک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/137774" target="_blank">📅 23:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137773">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfIx1uyzIOm96ZqLbGSLUlu1mCMeDjU6Q6zGTwfR9PM9X1jkYYdKrsXtK6wz3YjvWstQB86ps7GIlYOdfHCVdQ_qdvuXQ4fq84puT0vMR8tl-wpjzNWKqdEsy0YcqutKoFC1dRn9eFMwUCUdb3k7YQDjkcZnyf3yJgrouL6VxRinl9B_C1tBihXRg33pVt2OqRk6AYAjmxUCAnsmTpI4KBwmx6T3qyITjMdcN4R59TCKx-dgA_NHIeKUSiH-2RQr-snVL-BItXB-rMCwwv27Nk0FTVzjibaQgwOBzIjQ3AgktDgaN3CxDtLM24pMpgItrFnxPMEH30MKqtY68bXNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقائی: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت ما دفاع از ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/137773" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137772">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
علی نصیری، رئیس سارمان پیشگیری و مدیریت بحران شهر تهران: بلندگو ها و
تجهیزات نصب شده در شهر تهران، برای پخش اذان است نه برای آژیر هشدار جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/137772" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137771">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
العربیه: تماس‌های چین شامل بررسی اقدامات متقابل برای اعتمادسازی میان آمریکا و ایران است.
🔴
پکن در تلاش است زمینه را برای مذاکرات میان آمریکا و ایران درباره امنیت منطقه‌ای فراهم کند.
🔴
هدف تماس‌های چین، مشارکت دادن کشورهای حاشیه خلیج فارس و دیگر قدرت‌های منطقه‌ای در حمایت از ثبات بلندمدت در منطقه است
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/137771" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137770">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الحدث به نقل از وزارت خارجه آمریکا:
تبادل پیام‌ها بین واشنگتن و تهران همچنان ادامه دارد.
🔴
العربیه به نقل از یک منبع بلندپایه:
رایزنی‌های چین در هماهنگی با پاکستان برای کاهش تنش میان آمریکا و ایران انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/137770" target="_blank">📅 23:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137769">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
معاون شرکت مخابرات: سرقت کابل‌های مخابرات به بحران تبدیل شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/137769" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137768">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">فردا 5/5/5، هر تصمیمی دارین فردا اقدام کنید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/137768" target="_blank">📅 22:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137767">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا :
تبادل پیام‌ها بین واشنگتن و تهران همچنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/137767" target="_blank">📅 22:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137766">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نماینده‌های مجلس امروز طرحی رو تصویب کردن که بر اساس اون، تمام نیروهای سنتکام و تمام شهروندان ساکن اسرائیل، چه سلاح حمل کنن چه نکنن، نظامی محسوب میشن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/137766" target="_blank">📅 22:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137765">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXXUe5pCeHYkLr6uDmYB09NVjnm4jHF-c59Znos7-rWnfpwV3NqFZyewXRVAO-sIiodNIJ2nP8CSFiGlZnlyOiKulV5Ho0v5zDbkXrFvzesTo2B9sJEk18MCu5ZR4c-VI3zRSMCAfGpCc3O7g9dJ4t6V-ZXYa_ByCi94Fwt8dWGrLoptlYxYlvRS4wjOSxTP0N-KjDeRIA1GpBFdhodfeB_D8osX4oDsqyydCyW2FySi1lmpI4NTBqX1dbem6mF-q-rymNjufFOELlD1alDJ_7F3ggrsBkE4K5BHqawXG55TTK2cKPwfq1JqsRnHbX84b8-ZmtjQnU7oRTxnnG_yCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
مردم فقط دنبال انتقامن نه چیز دیگه
🔴
پ.ن: با این نخبه موافقید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/137765" target="_blank">📅 22:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137764">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1EOESJuIUPR8kYX9CB4WwyAyPy2Ernq7-i4Uf8H6pSlh7rLw1veqn2HIdwpwdn2DS0UhkWR_TwIOOWdAbTOui6HPZoN2wdulLT3TBee7PPuEyWzMn3IIVQXYrZVDduD6X4Czc-q9_UIsgLBzNTzLjnvS3JnS4clyZK-eUTxB7mByrEZ5Jub8fOwESQYXkFkrCsZj7TQPdLb_pZGoRw3jzl5CZRZEm2oP75G-yQ2g589330JE3VP8Y8NmkxnWgyH_9Rn4gWotUxKjlxlQBJ84OhUhRj3MuBP17Us61ZBCltgb_ZXUgXRxzW5MJ4ScU0xaswwE9wb2a3piPGOWyV_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون فعالیت گسترده تیم مذاکره کننده آمریکایی در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/137764" target="_blank">📅 22:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137763">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
المیادین: نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/137763" target="_blank">📅 22:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137762">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO6DQ3fplkoxzDDmdzdMXGTOAId0VMsnyv4sJ5iOwWfEotErzFKS9pYhC1IdZImfNqL7fdFtgoOzLN9--swzcYFGCEqXlwLo2Iea0ekcYiTnacsR0BwIMejyEMSEYEdvp7HplT2PzexeAs3UILkeCmSqFzTfBxlzxMzcICupDpUCFBYvgos-Yj2sNawbkrgD7wIu6ChfPH_gXBt97FGrg5uMNh7zZ0hZOxYxzPEVFw6JJbBpWtuN_A0pSGqe1uZ-bKRl-9QVvMSrA5H42uJ488jjDnfBc8QKZ4mNar_iXDR9xI1PY43YB2IbYXpzK2bm_2EdCyQ0y2cMRBU2fFc2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرام جوینده همسر سپهر حیدری اسطوره پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین از سپهر طلاق گرفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/137762" target="_blank">📅 22:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137761">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c2b00254.mp4?token=JxE9fXUu7LluS5YYPldId8tRNMtJKLmhCFpfHc_N8uk8oa-cvUEqqpPbMHIq439UdIZs2o8AvqufXUMqH6S53ZsBlznGrj6YNoGc4ZM7AS0hKT1JAYbvqR7ykY1W1CKwwMBTQQDT-dQkNIgnHqJ61pWGL1zkaxURdeqxN53WXlRuLO4FJi9AHf49vWSZFfCM1S3GD-7jtD-pcGZxle88fyWWJ3p-fYDWRYCfECP5GEDQmSulB007ioQT9f_JpYKp4eRQISRHbQD5UxD3WUK72gFCm9kkCLC-VyzMrH3piqjFqHfbEzMsm3zB7sJYPBwDQre-jDH7sWK4pnHVtdthHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c2b00254.mp4?token=JxE9fXUu7LluS5YYPldId8tRNMtJKLmhCFpfHc_N8uk8oa-cvUEqqpPbMHIq439UdIZs2o8AvqufXUMqH6S53ZsBlznGrj6YNoGc4ZM7AS0hKT1JAYbvqR7ykY1W1CKwwMBTQQDT-dQkNIgnHqJ61pWGL1zkaxURdeqxN53WXlRuLO4FJi9AHf49vWSZFfCM1S3GD-7jtD-pcGZxle88fyWWJ3p-fYDWRYCfECP5GEDQmSulB007ioQT9f_JpYKp4eRQISRHbQD5UxD3WUK72gFCm9kkCLC-VyzMrH3piqjFqHfbEzMsm3zB7sJYPBwDQre-jDH7sWK4pnHVtdthHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی موزه ملی کره‌شمالی دو تا پنکه گذاشتن رو به روی عکس رهبرکره شمالی که یه وقت تو عکس گرمش نشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/137761" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137760">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/137760" target="_blank">📅 22:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137759">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8_yerKShwbqnHD8NLsvU7bSKfFurHYYWaU3SgW4t_bRwEd2LNQ_cm8506eixbcUEuU0NZZqTKUQokBjfApu3phG-6ST1_8q5HMVbMfMHPWa9SIkW1Qb2cg2ANTo5ekvt8nN8JrKgyeqWMlECiUGjy7-P9knJt1HaIbXwY-ApxiPbOR4HuiX666zMc7zofqraToBEK4TDFPxtHqg3Bx7-iqDQbr9ZZWZdwvLAxv5lD0J1khvv1aCplU_ybN_hHhluLcOd_vOGzjC5r_BZZgA96rliU58LrO3epcyV5DM7miTqZEZv8pEaDfEgUU-zigEIaIdkDJtdVfLiDqW1z3sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرام جوینده همسر سپهر حیدری اسطوره پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین از سپهر طلاق گرفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/137759" target="_blank">📅 22:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137758">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
باد شدید در هنگ‌کنگ داربست بزرگ یک آسمان‌خراش را فرو ریخت.
🔴
رسانه‌ها گزارش داده‌اند این حادثه در پی وزش بادهای شدید ناشی از نزدیک شدن طوفان «نول» به وقوع پیوسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/137758" target="_blank">📅 21:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137757">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مدیرکل راهداری هرمزگان: کنارگذر هر ۹ پلی که در حملات آمریکا به هرمزگان آسیب دیده بودند، آسفالت و فعال شده است و عملیات بازسازی پل‌ها نیز در تمامی نقاط آغاز شده و در کوتاه‌ترین زمان انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/137757" target="_blank">📅 21:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137756">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ادعای العربیه درباره رد کامل پیشنهادهای عمان توسط ایران و خروج هیئت عمانی از تهران، تاکنون از سوی منابع رسمی تأیید نشده است.
🔴
گزارش‌ها فقط از ادامه رایزنی‌ها و اختلاف‌نظر درباره سازوکار تردد در تنگه هرمز حکایت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/137756" target="_blank">📅 21:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137755">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567a79a6d9.mp4?token=OIgY36e2-tQEZOW6fY58q9pm4pG8mdfNtelm4N9zbVAUifM9wFWTNaCcELl56yOqiupx2Q-bOHHSbBCYZy40bqeBQSXu92MrgXsZugSPH-vFmEjbNBRsxT4xpJNMHLdFg42qQQGDrAJwhx8FMWDwMwyEAMGhcy13ckrZOWXS-CJsmXBa8kl1ZG4O1Xzin5UIKLMt1gkpC9vATj5gidrLW3NgDz84nl055yiR8AT6I4z3-kkYBnpYN1O2YgFK6E__Aty4fsZIJRveG7te1atbQa3ZTB3XUCIvKAZnnwERBk-gK39zGjXFAor26KPq1RYMgD4xMqacxk8WKjSL4UcIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567a79a6d9.mp4?token=OIgY36e2-tQEZOW6fY58q9pm4pG8mdfNtelm4N9zbVAUifM9wFWTNaCcELl56yOqiupx2Q-bOHHSbBCYZy40bqeBQSXu92MrgXsZugSPH-vFmEjbNBRsxT4xpJNMHLdFg42qQQGDrAJwhx8FMWDwMwyEAMGhcy13ckrZOWXS-CJsmXBa8kl1ZG4O1Xzin5UIKLMt1gkpC9vATj5gidrLW3NgDz84nl055yiR8AT6I4z3-kkYBnpYN1O2YgFK6E__Aty4fsZIJRveG7te1atbQa3ZTB3XUCIvKAZnnwERBk-gK39zGjXFAor26KPq1RYMgD4xMqacxk8WKjSL4UcIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی عجیب از جنوب اوکراین که یک قطار روسی را پس از حمله پهپاد اوکراینی در حال آتش سوزی و البته نشت سوخت در طول مسیر نشان می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/137755" target="_blank">📅 21:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137754">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) فیلمی از پهپاد شناسایی و مسلح بایراکتار آکینجی ساخت ترکیه که توسط ائتلاف تحت رهبری عربستان سعودی عملیات می‌کرد و بر فراز استان الجوف سرنگون شد، منتشر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/137754" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137753">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtMaLSiySRcTPcKem_GFmxQkWbwOxEY3Ex2W9c-A5babkncXJ0i1bp8W85nnG8kvLbURtBulyEdJt5kUb2F1H212z4CQlqMVmBWUc0hoCjcAWRXlZpKSzmmHoITmqX_1DTNSx5Sfa1yd78-2Mj2r7_DP_mTUkNLKtIntydDufJhsjZgj8wC7QQFo-0haxCfA7vsXBuKjBKqRYMooEkISctB4Gwc4O8DkMblJ6iZN_c0i_vBIJtDcT7eaICujp5Er1ViB9-vD9ZyddkGWxSgXdyC_JQItt3kDHdQltP4eczztdiLs-BxsHBVzrOZHR9B9I2BHamSTLL7gZBW10KRBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب اما واقعی ، لیستی از عجیب‌ترین و پشم ریزون ترین دلایل طلاق :
دومی عالیه ، طلاق مرد از زن چون زنش مهمون که میاد خونشون میگوزه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/137753" target="_blank">📅 21:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137752">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۱۰ دقیقه تحلیل مولتی بازار | سیگنال های طلاجهانی،نقره جهانی، نفت و بیت‌کوین!  عزیزانی که تو وبینار «سبد ضدبحران» بودن این اپدیت تحلیلی است که اونجا بهتون دادم و با هم سبد بستیم.   راستی امروز کانال سیگنال کریپتو(ارزدیجیتال) ۲۰۰ نفر ظرفیت باز میکنیم دیگه میره…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/137752" target="_blank">📅 21:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137751">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7dnh9ioSFuAnGodA7zjDytb5mTSZay-sAV2-IW1lNTp5OB34uox9tmHD4_6om5SC9q1PiuVyL5ZxW3v91Zb4ayQVepw1r8ALTive4n-H3xCNE_xTBTh07wjlwOZsvB-RXmW4SwySkCyif04EgMAkdZLVWEAUfUuWp3gAGNhLBZ4nlIcetkNZvuhVekOginFYfsqNkaLO0THzJE_PheMnuv5z5KRFlXNCOTbYkwqWrrxs_5ZbNPLPhnp4vR86qb29EA4LRta0GHNZiQI83nrKYUoTkY-OOSm4XC7mo1rTu87mVnAg2JHBcuSRIu5yqqt7MOxfGtbsRpFkopjw69Wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: تو عراق به من میگن عباس قهرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/137751" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کان : نتانیاهو به وزیرهای کابینه گفته؛
آمریکا ازمون خواسته به‌طور گسترده از غزه، سوریه و لبنان عقب‌نشینی کنیم
🔴
اما نتانیاهو با این خواسته‌ها مخالفت کرده و جوابش به آمریکا اینه : «نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/137750" target="_blank">📅 21:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137747">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AeF7OWIC11tk2Znkt5EJk5NCxmxZf1OfHXbX-pBzJ8gvC5GNJeJXIPyfURLYa1mHmdBkgszG0aizDfZfvOJQ3ltlyQ7zqf9tYCuo47hoAfegWXrS7vGnC6KKX-mTwpjafwSQJBXuQshVRjD3bRf4iktz5blUyGUicBxm13VIxypiTE5iw4PlNqpVIiAjOtvA4HBlpjTGPeyWJC-OTgjb5gDA1T6qzsPRUIdUzrxHZz51-sMwWk2z6jhDZKq-HinMZu7CUUincxjKKAj6DISTCpo7oBFSQpGnVKuaBFWrdujT7_8HyVhYWGtOJM2EV2wkyEJzDcSzQwVUgvFHe3YizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o57i7JUNppdlOC2xuwGnEkZEhRwGJkF8Zu1-XI8aJrqOXrRdet8saOFP2enj8eFRW3X2am6ulZ7acEyds7GkP0UupwGATj-zaEZE5VObvpk8VQpJ-rCJv-vre9K2axv9Oq9wz4ZRkj-a1gtXBvvRcsQGLkAMw2Eyy5TYbcvl0cgggw7HcC4Z1pn5TO9SlJDuyfoiTGgjzzGcOmAUwcrm9shg3n44WiKh-nW2HzAuZXY-YgwbT34rM3ftOA3hYpgd1J3d2rg_I-IPSNE8DYx-cXRBxkd4U0cHj-z9hdXLlJDx64I6lgSQLd6OZmU_5Rlu0VbGNHm0WvLMM3alUZBGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IcmilY3rBFtq4i2Tk7nUgQAGJ0Lz8sxoBsjko1OvH01JnkNVw0cjMzcckTHZb554Yu8lQTpMq-Lm2-rKkrQB5EMGZbRYGxyBQzZ7eiOM-2pC-i4IHfoRxJsCOLjZ3V89zK1YKvuwjN7JK1EG0wrD58YCrKR-NHlDMM_oUqRcp2EYOcKR6YZGlatUhUHUEzy4oCrJv3E0HO9qBfHUGnmcL0eeSJgigmEzK1GIgaLRh3CZ1m7kcrr41Z6hKtmKyKA99Aba2L494oJ37D6E3oPvIU1uiX02NViXZMd6bkWBxl3sq6_SyY2rL4ygPJzVwG_i1F_I_vVoIkrlGhtnphML0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از سرنگونی پهپاد «بیرقدار» ترکیه متعلق به نیروهای سعودی در یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/137747" target="_blank">📅 21:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137746">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
آکسیوس مدعی شد: آمریکا و بریتانیا هنوز در حال بحث دربارهٔ کنفرانس بین‌المللی هستند که می‌خواهند اواخر این هفته برای تشکیل ائتلافی به منظور حفاظت و پاکسازی مین‌های تنگه هرمز برگزار کنند.
‏
🔴
تاریخ نهایی این نشست هنوز تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/137746" target="_blank">📅 21:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137745">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سی‌ان‌ان: عمان پیشنهادی شامل پرداخت داوطلبانه برای خدمات ارائه شده در هرمز داد اما گویا ایران آن را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/137745" target="_blank">📅 21:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137744">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بیانیه مجتبی خامنه‌ای  :
🔴
نامه شما، رزمنده‌های مؤمن و شجاع حزب‌الله، باعث افتخار و قدردانیه
🔴
امروز که مردم دنیا از ظلم آمریکا و رژیم صهیونیستی به ستوه اومدن
🔴
راهی جز جهاد و مقاومت باقی نمونده. هر کسی هم تو این مسیر پایداری کنه، وعده نصرت الهی شامل حالش می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/137744" target="_blank">📅 20:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137743">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzt--miV8zbKNUsu4ZsGW8FeK0MVqA3egjxZwPXPrhOW9CW4IRHWdLDKwC0v6IpeGTQLOQaGlZc_H2Dg8t-LzXib3s1LJsLOSjZK3-rFnZTYDte-GSNVrpgqX-amlGW52Bq9aqPEty0B369v5S55fTSLV01oDL22h6BRJ8ioO_ldYUczlbWYMTfPlAjxLpaZKwzs8HWc-jpMmOPFmR9fR55pueh013r9hwd5tvU1RFqaw1Zd30UYHVO5WrnNv63mf93yHkvpnjsc-0U6rKWxmFYwHkoerH4dVI6oH4dSN7P00mXCEkGAJL2DsqpxTZRXeqqG70B8C6P5frKfIHLjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غلامعلی حداد عادل : سید مجتبی خامنه‌ای همراه با همسر و سه فرزندش تو ی آپارتمان ۱۰۰ متری زندگی میکرد
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/137743" target="_blank">📅 20:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137742">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
العربیه: ایران با تمام پیشنهادات عمان برای ایجاد گذرگاه جدید در تنگه هرمز مخالفت کرده است، هیئت دیپلماتیک عمانی پس از مخالفت های ایران، تهران را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/137742" target="_blank">📅 20:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137741">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9QWsNKaNICjBJOzsxNwFygszmrzTDFP-f35A4azRZlvANxovtalkJXDO1T1F-xuQC3GmXwO6H9HTPTiKsjZJ62Z1zPZrBT3xqrDF2eB3uXi7NfGlMWoQQrjjeGl-oJl92zjC27MDRjB-Hlxtc-nbxf4PsYgvj6KB3Edm8Y1_pYoP2cisAz6oZ4ClZ4O6d1qrmowHjKk3ET3QrbVcsSsrKmLX-acFidYX2wWuTaRU3RwzC5eDEFqqj9WHwwmbcEwgYN5TMqJmj8d78QwoTmh_Gbk6z_46xv5KSsv5uIu2ohbBcdcMY28RiluH80EDW3pqg30_4yjj1ilXbEEt89PuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس : ژنرال برد کوپر فرمانده سنتکام، پیشنهاد داد که عملیات بمباران در اطراف تنگه هرمز متوقف شود، با این استدلال که این عملیات به حداکثر کارایی خود رسیده و بیشتر اهداف تکراری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/137741" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f700083cc1.mp4?token=EYm-8RTcdhDyOjzo1NwrkEOA5ly-Xcfvw2fSoKeemmmV1R1K78X5X3Iez5pzmdvlctUgqVWxNBKWlnmLaOhtmBb9korkoGPfsNM-auuvvC7izbL9OOcGM7KWyhdqrZpA_6A61bz_QvhAo1buyONNF3XYav__8mwXpW5ygdYG6ztt-apjyensRyA4WUGkm-u-iu5lK6-c9IXwvGVnmw3qR_osMvMpPDPStwuA1jTHt2Oob7fO7QwQzLrs3oj2TH9MMgANK-xIKTWXtN9zrJ6yXPptngxnbnFvgR4G3snS7JBOcyx1fk03I5scG6TXy0IgLvM6pmBro5c15yY9Q7zFEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f700083cc1.mp4?token=EYm-8RTcdhDyOjzo1NwrkEOA5ly-Xcfvw2fSoKeemmmV1R1K78X5X3Iez5pzmdvlctUgqVWxNBKWlnmLaOhtmBb9korkoGPfsNM-auuvvC7izbL9OOcGM7KWyhdqrZpA_6A61bz_QvhAo1buyONNF3XYav__8mwXpW5ygdYG6ztt-apjyensRyA4WUGkm-u-iu5lK6-c9IXwvGVnmw3qR_osMvMpPDPStwuA1jTHt2Oob7fO7QwQzLrs3oj2TH9MMgANK-xIKTWXtN9zrJ6yXPptngxnbnFvgR4G3snS7JBOcyx1fk03I5scG6TXy0IgLvM6pmBro5c15yY9Q7zFEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
ممدانی خود را با این قاتلان همسو کرده است مراقب کارهایش باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/137740" target="_blank">📅 20:24 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
