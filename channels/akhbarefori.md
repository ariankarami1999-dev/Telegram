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
<img src="https://cdn4.telesco.pe/file/i58JyhUHqgRorKnq0hR06cOP1HlmhmLaf1WZgc_51rUt6ljGSwVDzKAWqDWXz3CmN_twpNIg40yDOQ3PfU_oLn1NT19fjS90MX0wixWFjXJBdTwKp3Tcj2nFW-BwMpVyjJM0U6h6ibjY_R_69D8hm8-7PLJbUrtxn-38GppcDuXDw3z80DSYHthuwmnXRsUvUFeo9X2Xsr2SrEyyntcJwbAjStyQ2owav118SMUaWHup9yOTqCcuNje-xscnlAuUHgdThPnTDMHlHdgrR26YW8w2bDo3cg3OyxOXq1tz3BgxBUkyj4fuYFhT7RtCDnzD3F8HXV1al-5_bzT0Yoo58Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.14M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 15:22:34</div>
<hr>

<div class="tg-post" id="msg-665295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1UcV4V1BhGgEOB-dN9WQIDH7b8fV46pDmVJKu2Lpxy9exPUaDgkFo1UCoAXrPC527YYlwo5JRMz0DhzLRVXgpYZ0nEzgNEohi8xoOkpo21BBKYUFEzLBeyIcS3HZCdaW2KDvnGSzIhjxFE4BshzP6AW-Ec5gde_8wJ-Lvg00CdimDSVtiD-_FO7fEwy8Yoj8VzhEtdbREKsokZ_o3SBLS5n5m3JfqiUu1hsoesDVxqDeIfQwL2LwdZEJvYrfzf_foE5rgbzBL4dOrgH1zfYsvIZdoLD7w6vNc2unRNRKiwj8jR1rMVWyJJ9HEvZ2Sf6gEAranI7FBac9Tta3iMepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری دیده‌نشده از رهبر شهید انقلاب در کنار موشک سجیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/665295" target="_blank">📅 15:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
فوران کوه آتنا در ایتالیا
🇮🇹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/665294" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXQeWd2OFWXraGSZvgYPHb58d40DuxoC7CCNS9KD5E9g1k-2mEnTwB-z5DBr4rHma8lF0oHA0qX32MPC99q_LXFNQqkmX1BdERXMbWqcQtq7uW0eUg_o4l2D4iYLQ_d2cPPT2KquSvn4yEP332OBzJRsYvUmFthiDnaSplHyT76CDHF3xSJgVUDWiMEsaUrTw3yBsxpt0E299mvXJBj6VsNH5wKRViOHNscM4m29kMlU1aSW1gnytBsNvxKgFVjCYRVCrw4lGK70-OPQtKOG7QS5vPlaHApnEFBQHLFkuwwjfPaDoGtHlyuB71pwF-Q4drfSADiEHYmSKFJJ-6fkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله ایران به پالایشگاه حیفا کارساز بود؛ ۶۰ درصد تولید نفت اسرائیل مختل شد
شبکه ۱۲ اسرائیل:
🔹
حمله به پالایشگاه حیفا، مخزن اصلی بنزین و نیروگاه آن را نابود کرد و ۶۰ درصد از ظرفیت تولید فرآورده‌های نفتی اسرائیل از بین رفت.
🔹
بازسازی کامل تا سال ۲۰۲۸ طول می‌کشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/665293" target="_blank">📅 15:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای العربیه درباره شروط تازه ایران در مذاکرات دوحه؛ رایزنی درباره تنگه هرمز
العربیه:
🔹
مذاکرات غیرمستقیم در دوحه ادامه دارد؛ ایران خواستار آزادسازی ۳ میلیارد دلار از دارایی‌های خود در ازای هر پیشرفت در مذاکرات شده و هیئت‌ها برای بررسی پیشنهاد عمان درباره تنگه هرمز، راهی پایتخت‌های خود شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/665292" target="_blank">📅 15:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تصویری از آتش‌سوزی بزرگ در فرودگاه بین‌المللی بغداد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/665291" target="_blank">📅 15:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تیم ملی فوتبال عازم تهران شد
🔹
با توجه به تاخیر بوجود آمده در برنامه پروازی، کاروان تیم ملی دقایقی پیش آنتالیا را به مقصد تهران کرد و حوالی ساعت ۱۸ در فرودگاه مهرآباد به زمین خواهد نشست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/665290" target="_blank">📅 14:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
گزارش UKMTO از وضعیت یک قایق مشکوک در منطقه
🔹
طبق اعلام سازمان UKMTO، یک قایق کوچک مسلح با ۴ سرنشین و مجهز به آر پی جی، پس از ترک یک کشتی، همچنان در منطقه فعال بوده و خطر بالقوه‌ای برای سایر کشتی‌ها محسوب می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/665289" target="_blank">📅 14:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPygsx7uCaa8gsi0VxlelEW7YDAR4Ss5XzyOugnAYc_OFY2qgNlLS7U5fcixkxEuLJwqrWzPvhH9QSPMIXYdD-nTCaW1vVdN6_FNt3zP0QS8FDwS-ADLoQ0WwAYYhiPNU6hez_f_2YbQmrHGVdfZztX1oNIsOoRraOafq0kcfM8mRQi89Sc-HxkqH1aPLQOKawxRFaXtTqFfeDtaGmjCW7NsmIY3ufC3bR7Y3TcfLX1DHUOUT9PyeVhofVwHUmAFy0FH9ZCNjgslkWx35Ft8dRww3p72t-SJr7Wr1R0TqpjVQAqAwvVI2ZMiEIiNAdR00nmDJOZ1Kd_4EU2hZ_5_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ بیت‌کوین به زیر ۵۸ هزار دلار برای هر رمز ارز سقوط کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/665288" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAVTSJ9rYU-EvxVRmvx7SwdHMgv_-MwivbF8SXB72AfUQI3vY1HP5nRlAkDdaff1eJf4uuyUX1r2Ai9FI2WHMSL4D6bl2272tLG0g-T16RKowz1VmuCA-2iGRxMnAYr0KXFZxNlsEtcll5bHvXbZUosdRZoo_PamptIj9WrKDzsZWvZCumLT7YpiTUHKM5Lc2GxV1NywdsPlfE_XN2o69LpVT3FAQmKKjA0ecdA4QhINVIGQDqnoBdTYcR1OjgMRqAn79rOld0HdARtUN67yioqKPnWlJC5c_rkK5HlUh7M-AgPmrU7egDyHdcNALVQ226PVqxbIQeVLk-hbpGBtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رز ترنج؛ امنیت دارد
🟢
صندوق طلای رز ترنج پشتوانه واقعی طلا دارد. دارایی‌های صندوق در قالب گواهی سپرده شمش و سکه، با پشتوانه طلای نگهداری‌شده در انبارهای مورد تأیید بورس کالا قرار دارد.
🟢
واحدهای صندوق فقط به میزان طلای موجود قابل انتشار هستند؛ یعنی ابتدا طلا تأمین می‌شود و سپس واحدهای جدید صندوق عرضه می‌شود.
🟢
با «رز ترنج» بدون نگرانی از نگهداری، سرقت یا اصالت طلای فیزیکی، می‌توانید به‌سادگی در طلا سرمایه‌گذاری کنید.
▫️
صندوق طلای رز ترنج از تمام کارگزاری‌ها با نماد «رز ترنج» قابل خرید است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/akhbarefori/665287" target="_blank">📅 14:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSypSvZ8Zr2KpqaNh04FUd-lFl1wQABJJ7_lX2ZX3Oksib79Jjs49X94H90hjc1bjjq1vJn8p81lUYN_jq6SZCtiXxWtACviGIEO7mpl6LQ19JPRDcsqDjnFUGFGfRPOK2lItGEbIdJE1Q5Wwq2LuwHkWUBAyPJXoo5NCbaA7IDZttN890DF9mxWdT-cJrLvbJjiRrNdd3hsVIhdHxqWZoRAfhV7iPfoDKgrxFzXSjlys4yVf58LYg_fsUmSq6v-C0YyKSIG99RRBhmegrqjbyho7YjoaKa236WTIWtmMo5sEJazbCnJCdLkL7lWSTuTk_KDUzDprgY5agNQ2xOQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا خبر داد:
بانک کشاورزی در آستانه ورود به باشگاه هزار همتی‌ها / تمرکز همزمان بر تقویت منابع و گسترش تأمین مالی تولید
🔻
مدیرعامل بانک کشاورزی با اشاره به عبور منابع این بانک از رقم ۹۲۶ هزار میلیارد تومان اعلام کرد: این بانک با اتکا به اعتماد سپرده‌گذاران، در آستانه ورود به باشگاه بانک‌های هزار همتی قرار دارد و این ظرفیت جدید را به‌طور هدفمند در خدمت تأمین مالی تولید و تقویت امنیت غذایی کشور به‌کار خواهد گرفت.
🔻
وهب متقی‌نیا رشد فزاینده منابع این بانک را نشان‌دهنده افزایش اعتماد عمومی، ارتقای کیفیت خدمات و تمرکز بانک بر تجهیز پایدار منابع دانست و افزود: این شرایط به ما امکان می‌دهد منابع بیشتری را به شکل هدفمند در اختیار بخش‌های مولد، به‌ویژه کشاورزی، دام، طیور، شیلات و صنایع غذایی قرار دهیم.
🔗
مشروح‌خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/akhbarefori/665286" target="_blank">📅 14:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
دستور قضایی برای ترخیص خودروهای منطقه آزاد مازندران صادر شد
رئیس پلیس راهور مازندران:
🔹
با صدور دستور قضایی، فرایند خروج و آزادسازی خودروهای دپو شده در منطقه آزاد و گمرکات استان، از ساعت ۸ صبح فردا، ۱۱ تیرماه، در بندر امیرآباد آغاز می‌شود.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/665285" target="_blank">📅 14:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6db7G-eimb4s4ljEfVmQOOpvtUDPQuFLdOiFoPmZTlFarYJBlREgwXFZWAJ4oHaB5_AZG3t_mBKuTEM7IYqQ1bfW9CTWapaXZcwoPaWYq5zefOwtWriuwRztyxgGxXmV20HJnCuS4ZkIZ3eSDOAkU-YIaSvdChFQwhVSLn66v7fK2IAEGuwaPhDuyrW9De3Zg7lL7LXSC8-yxMsttBnnYwAtH48rQNOK89lC3Kofk5TuhiFYXlgqqYKvRRpMkM46BSWLzaiZSNgTe1lYvPeNI8x0RWLtk45sVcOowHyMRopz87ifiPaidVr57JyrKGkKzIOidQeWc_3WFQbhZrEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از آتش‌سوزی بزرگ در فرودگاه بین‌المللی بغداد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/665284" target="_blank">📅 14:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
وقوع حادثه دریایی در آب‌های یمن  شرکت خدمات دریایی انگلیس:
🔹
یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/665283" target="_blank">📅 14:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
کارنامه مثبت دولت پزشکیان/ صنایع در «تابستان» بیشتر از «ماه‌های عادی» برق می‌گیرند!
🔹
بر اساس اعلام صنعت برق؛ از ابتدای خرداد سال جاری تاکنون، صنایع انرژی‌‌بر ۱۵ درصد برق بیشتری نسبت به مدت مشابه سال گذشته تحویل گرفتند.
🔹
در سال‌های ۱۴۰۰ تا ۱۴۰۳، مصرف ماهانه برق صنایع، در تابستان کمتر از ماه‌های عادی بوده. موضوعی که طبیعی به نظر می‌رسد زیرا در پیک گرما، اولویت با بخش خانگی است و برق صنایع محدود می‌شود.
🔹
حتی در سال ۱۴۰۲ صنایع در ماه‌های گرم سال ۱۷۱۰ میلیون کیلووات ساعت برق کمتری دریافت می‌کردند که یک رکورد منفی محسوب می‌شود.
🔹
اما جالب اینکه این الگو در سال ۱۴۰۴ رخ نداده و اتفاقا مصرف برق صنایع در ماه‌های گرم بیشتر از ماه‌های عادی شده؛ آن هم به میزان ۸۷۸ میلیون کیلووات ساعت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/665281" target="_blank">📅 14:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665280">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bd6a5f10.mp4?token=NhrQVURFrQyi2CQEr1kdOtZ1n9Ingaij4aEcdfEUPXWbSlUUziSyCMPjNKVvl-LKPi9V-gL0PaiAnbw-i2LneX3IXSOFsuF_PvSl8srLQFQ6dWR7WvZbsrCvg39dhEjTdy0Ha65lnYk4CzFlDqL3QsxFa-wJau_dBWVie2MDqeqFPXWiM88n5ovdYa1lkJ_7xJ1QCteO5aYkSdF-sdtjNkOYK5TDMvsDTRyWQpxxDYTG_rn0cw7BipqTVKPvwBdGLx1_uK9DDj8RDQkx5MRPaisd9FIA22PSLAavHl4Wlwprc-vahpD9aXDGxRb2Bq1W-hF2iOuoscjDKEkNOFIZZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bd6a5f10.mp4?token=NhrQVURFrQyi2CQEr1kdOtZ1n9Ingaij4aEcdfEUPXWbSlUUziSyCMPjNKVvl-LKPi9V-gL0PaiAnbw-i2LneX3IXSOFsuF_PvSl8srLQFQ6dWR7WvZbsrCvg39dhEjTdy0Ha65lnYk4CzFlDqL3QsxFa-wJau_dBWVie2MDqeqFPXWiM88n5ovdYa1lkJ_7xJ1QCteO5aYkSdF-sdtjNkOYK5TDMvsDTRyWQpxxDYTG_rn0cw7BipqTVKPvwBdGLx1_uK9DDj8RDQkx5MRPaisd9FIA22PSLAavHl4Wlwprc-vahpD9aXDGxRb2Bq1W-hF2iOuoscjDKEkNOFIZZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: یک فروند کشتی که از مسیری غیر از مسیر تعیین شده در قالب نظم ایرانی در تنگه هرمز، تردد می‌کرد، به گل نشسته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665280" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665279">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
شهردار ایلام بازداشت شد
🔹
دادستان ایلام از بازداشت شهردار این شهر به اتهام سوءمدیریت و تخلفات مالی خبر داد؛ طبق اعلام مقام قضایی، پرونده تشکیل شده و بررسی‌ها برای تکمیل مستندات ادامه دارد./ فارس
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/665279" target="_blank">📅 14:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9fa897e21.mp4?token=OdGJDWXu-0kku581W0LpFF9W2h2HB6r4ESjXKqHn0iYkA3Sq4lWZRB4aAoYaA1qj8SPJDL95L5DcdsYHN7GI0NmGq25T1KP5v2YC-19Ne0JjVL68-fwQfNRKBeNHad_36gsmFzmXIMfZDyUNiQ-c_ERasVHd6XfOMs7aq2za8bTkzsKantkhCQKAtqU-t1NYdXIDbf72aMkfOEBn-KNtyHT8mAo2Y42e1xlLpPbfWp0zhhuANqe41Ud90tmwJwwzY5mqAc_abhxoQFyb04y7_QgqwpE49Gk1GB64PCn2ARVANTIyTgZKFgxIZqEuwXs6DEIgRpmOHUbPv6r-kHmghi6Vy4-dhHyg9pGpo-xxONEkMEzOw6DLiGPaBlyxyipKgswQVQlws0K4u5nKg3TiesSX7NlGFHrU9rUKGIE3ebNiPvm7qNDfm-hv4yi88uIuMYOvmi70XSLagJHaUpdaEhSB0kTRvz0qg5HDJeA0l_6lGLlBQYXeUooH4K2y5xjrhGJe4JTSnXAZY9PbBvoAmO7-fIwoSxl6Vd8pFS73NmUZ_ZJSLOM_d9Kty9ARWQAmKivYoyL_qo1pDsy0lqBRmldFxE3z61UMbOQbmsfdZsDFdHPMxEgknMvdlJXjwdcy00BYkxlKEPwLs721Te4kVbF-JiVh1AwMd43JPLv22Zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9fa897e21.mp4?token=OdGJDWXu-0kku581W0LpFF9W2h2HB6r4ESjXKqHn0iYkA3Sq4lWZRB4aAoYaA1qj8SPJDL95L5DcdsYHN7GI0NmGq25T1KP5v2YC-19Ne0JjVL68-fwQfNRKBeNHad_36gsmFzmXIMfZDyUNiQ-c_ERasVHd6XfOMs7aq2za8bTkzsKantkhCQKAtqU-t1NYdXIDbf72aMkfOEBn-KNtyHT8mAo2Y42e1xlLpPbfWp0zhhuANqe41Ud90tmwJwwzY5mqAc_abhxoQFyb04y7_QgqwpE49Gk1GB64PCn2ARVANTIyTgZKFgxIZqEuwXs6DEIgRpmOHUbPv6r-kHmghi6Vy4-dhHyg9pGpo-xxONEkMEzOw6DLiGPaBlyxyipKgswQVQlws0K4u5nKg3TiesSX7NlGFHrU9rUKGIE3ebNiPvm7qNDfm-hv4yi88uIuMYOvmi70XSLagJHaUpdaEhSB0kTRvz0qg5HDJeA0l_6lGLlBQYXeUooH4K2y5xjrhGJe4JTSnXAZY9PbBvoAmO7-fIwoSxl6Vd8pFS73NmUZ_ZJSLOM_d9Kty9ARWQAmKivYoyL_qo1pDsy0lqBRmldFxE3z61UMbOQbmsfdZsDFdHPMxEgknMvdlJXjwdcy00BYkxlKEPwLs721Te4kVbF-JiVh1AwMd43JPLv22Zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی چهل‌سرا در جنوب مصلا برای خدمت‌رسانی مراسم وداع "آقای شهید ایران"
🔹
فعالسازی تلفن ۴۰۳۰ برای اطلاع‌رسانی مراسم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/665278" target="_blank">📅 14:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d2420819.mp4?token=jUMXl_t-OPM--5xHGT-H7YWTijnRras2fEyN3EUCfXeuS6GIi3pw_ZqD88q-QgfQP0QyRrfXO-bwHgzFHB7E7SUIoKwsZmQNyy7dQr77ypr9y1BUgAk8GGxP-bCl10xrpX3yWtL25djuTwbXurSap_jDjh4xJD9ldDQWZORmBQPib-f03PC4zGuSviZgeV7FGLqqdUvgqexGL1RVgdbpDXacxMfaTnXaEsUOuWm6iN-yzrn6cfsq3qAEBM1R1rd_fA5php_ybw1DvwSQgHzwQzRP5VB906b6D9EyIIr35Hlz9tCcurDGWPyJBcCTO9Eg51_WduUh4P9rvM59rjc4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d2420819.mp4?token=jUMXl_t-OPM--5xHGT-H7YWTijnRras2fEyN3EUCfXeuS6GIi3pw_ZqD88q-QgfQP0QyRrfXO-bwHgzFHB7E7SUIoKwsZmQNyy7dQr77ypr9y1BUgAk8GGxP-bCl10xrpX3yWtL25djuTwbXurSap_jDjh4xJD9ldDQWZORmBQPib-f03PC4zGuSviZgeV7FGLqqdUvgqexGL1RVgdbpDXacxMfaTnXaEsUOuWm6iN-yzrn6cfsq3qAEBM1R1rd_fA5php_ybw1DvwSQgHzwQzRP5VB906b6D9EyIIr35Hlz9tCcurDGWPyJBcCTO9Eg51_WduUh4P9rvM59rjc4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وسواسِ والدین، قاتلِ نشاطِ فرزندشان است! پدر و مادرهای وسواسی حتما باید خود را درمان کنند
/ مدار
این گفت‌وگو را به طور کامل اینجا ببینید
👇
https://aparat.com/v/jjy2nnk
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/665277" target="_blank">📅 14:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رایزنی غریب‌آبادی در قطر برای اجرای تفاهم‌نامه آتش‌بس
🔹
کاظم غریب‌آبادی، مذاکره‌کننده ایران، در دیدار با نخست‌وزیر قطر، ضمن بررسی چالش‌های اجرای یادداشت تفاهم «خاتمه جنگ» و تحولات لبنان، از تشکیل کارگروه‌های ویژه برای توافق نهایی خبر داد.
🔹
به گفته وی، زمان و مکان آغاز مذاکراتِ این کارگروه‌ها در حال رایزنی است./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/665276" target="_blank">📅 14:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv5o0bRb8lYuDJ9Liviovv9Wpm2pI2GJ9zESWoHCWRRVWf4xA86AA2mFLvEarhrXUN9AC9hAJNsNk1VZWcInMkoA2va8SeZ2T443cx5mB0-8z30mshizRwLTpy-H9QsvszsxHINZ7RwA6EdRJdAhF1AvDvtGVsfnvuVvDqtZr28hdLpGw132x6nvlSXuod8XjsgEs8npW5y3CVWwcgAqX7Fahe_zmH9p9KT_OjHXER0_1ZPaCRje3hBSTYkSIR0rNNGvQLc7vx9EKfgWrhqXz1UgLajbuMsb6o3ZNDfIzoXiNaEPXrnWQh8V0RhG8V3hetLWw8QRpEdfb8p4HYs8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز یک واژه، برای فهم بهتر خبرها امروز نوبت اصطلاح «کیفرخواست» است؛ می‌دونستی یعنی چی؟
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/665275" target="_blank">📅 14:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665274">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXeZ0rfaLxuh1yfuWMiIkBoeqMf_Pu3l5ILaADZirt5yrJKEfmSLLDMX2TMrROfrNL7YJTQ2fOla1OojW4SnZCtDegV9HeXKLsPVt8UBHrtGTymFTK7Mztb_p2RBWfenRlWWA9CX-pRc1czRTBEOHIy-4zXL_DR_5f5GkRyhhlEP_m4sMoMtK1VAzpSYVQIxr8ltzVAE4xGQHCSzPDg0J3QDuA0MP3VmSWqdoOq_TQcRR6XroatPrzPWQsNvr_SxnlB-xoRJHDPigz_38xd7PQIOmFWOcnHTo05gdRG1fNEjLDjq7K_TfpoUUKvtXVABUFOud4FwX5nQChE5PaAKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: مراسم تشییع رهبر شهید انقلاب باید نماد وحدت و انسجام ملی باشد
🔹
رئیس‌جمهور خواستار تبدیل مراسم تشییع «رهبر شهید» به نماد وحدت ملی شد و از مردم خواست با حضور گسترده، پیام همبستگی را به جهان مخابره کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/665274" target="_blank">📅 14:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_o3bmvNhrd5mVIRt6m2okJT6Z70tsxHMYIZUNsCpkuABkHMrzGGU_2VBv6TPfE487S1jGprgpOPRbcbm_AfuKWBed01Hz-QKEl6LEYE1ahSxfsBDqsHUoH1xJjG0coggSj9x0F7T9gsRkJvjmXmIFic2eszlvs4_YY7uZNFft25fBLwyctZpkOMldgACDAGwtllkTTxiD3uUus46CGWoOjuIubSaxLFw9ljWuRfkmqsbqam847IAM2TwdXxJKTN4UAfg1zJ00AVHzPEwXo7LHZ_dRYP0iu3e0HSvP1kImS8O74KU-2TuOz5doGrJ8zvyil0BN_z4WDLlxxCqTvY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ قاطع وزیرخارجه به تهدیدات گالانت: اسرائیل را سر جای خود می‌نشانیم
سیدعباس عراقچی در واکنش به اظهارات خصمانه «یوآو گالانت» علیه رهبری ایران، با تأکید بر شفافیت مفاد تفاهم‌نامه اسلام‌آباد، هشدار داد:
🔹
رئیس‌جمهور آمریکا متعهد به مهار این «جانور دست‌آموز» در تل‌آویو شده است؛ اگر آن‌ها از دستور ارباب خود سرپیچی کنند، ایران درس لازم را به آن‌ها خواهد داد و هرگونه تهدیدی با پاسخ فوری و قدرتمند مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/665273" target="_blank">📅 14:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نماز آیت‌ الله العظمی سید محمدرضا موسوی گلپایگانی بر پیکر مطهر امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/665272" target="_blank">📅 14:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پیکر داماد رهبر شهید انقلاب روز جمعه تشییع می‌شود
🔹
مراسم وداع با پیکر مطهر شهید مصباح الهدی باقری کنی، داماد رهبر مجاهد شهید آیت‌الله سیدعلی خامنه‌ای، روز جمعه ۱۲ تیر از ساعت ۱۷ با حرکت از میدان دوم شهران به سمت پل شهید احمد کاشانی برگزار می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/665271" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665270">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkC8-fKhqbk5QmSHruemZFTRtGPMB8VFTADAZQoqosnKzia1vm5mpXkEa4WSHzkafFWCwxBfB3SoVneDSoTKII9wfrOgJTc8Mc8kTRPZziQEYsfc8QmsNJzSvruUTHOx0jis0HiPenZxbJCKiTnb8XyTCBkoTN-0i_ESqDnX0qfAuOKWCaJFMyTDDuVpfPoQH0-EEneruUSSl4rIaIXJeTXX_jiQp_Q9kJFDwo-ssxaN1zf-cAvZx7vJ9QnXkq_Ygk6NvjqyAmXxsuWBubovL31rvHdmesuZveoprksLGJ5-1MjkwfI5Y-y3Y7dwRu8lxtWjPp38Zio2ae0vbmK3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاتلی که پشت میز مذاکره هم می‌نشیند!
آنتونیو گوترش، دبیرکل سازمان ملل متحد:
🔹
حملات اسرائیل از زمان اعلام آتش‌بس، بیش از هزار فلسطینی را در غزه به قتل رسانده است.
🔹
کارتون از: کمال شرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/665270" target="_blank">📅 14:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZBC5LfyOj-UV5FYcOYC1JWXNcnVj3AUAbNdm6iR_rTsWUyvBlXkThU7BmlAgduDcK9ePcuwG0Zjpy7WfnJZSxD0R1-TRZOGIQIizardS6Hv3c75HuN4ZrjOjYgfQVIY61o8MhuRWRTEveQ08HjySygbYPEJLMBU4D4SNp4DHm_d30cTmTDnYUc5CrpMpkq3Wm2pyaF8CbJzD43toqD6P2AsJtvXatCZTkzZhkB-u3VXQSPuP70PT2u0bm19IrYXQLW-RBPFKZ7nxcI_MNv9fckx32AewScVzdyWvjiF_pZdx3sWmwQEin7gzs1noTdSYymEJH5SSGewDsdJdZbpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی جهانگیری، رئیس گروه مالی گردشگری، به مناسبت فرارسیدن روز صنعت و معدن پیامی صادر کرد. در این پیام آمده است:
«صنعت و معدن، ستون‌های استوار توسعه اقتصادی، خوداتکایی و پیشرفت هر کشور هستند و شکوفایی این دو حوزه، مرهون همت، دانش و تلاش خستگی‌ناپذیر انسان‌هایی است که با نوآوری، مسئولیت‌پذیری و روحیه جهادی، مسیر آبادانی و آینده‌سازی را هموار می‌کنند.
فرارسیدن روز صنعت و معدن را به تمامی صنعتگران، معدنکاران، مهندسان، کارآفرینان، مدیران، متخصصان و کارگران پرتلاش این عرصه تبریک و تهنیت عرض می‌کنم و از نقش ارزشمند آنان در خلق ثروت، توسعه پایدار، اشتغال‌آفرینی و تقویت بنیان‌های اقتصادی کشور صمیمانه قدردانی می‌نمایم.
امید است با اتکا به سرمایه انسانی، دانش، فناوری و نوآوری، شاهد شکوفایی روزافزون صنعت و معدن، افزایش توان رقابتی و دستیابی به افق‌های روشن‌تر برای ایران عزیز باشیم.انشالله»
گفتنی است گروه مالی گردشگری با حضور در ۱۱ حوزه اقتصادی و ایجاد بیش از ۴۵ هزار فرصت شغلی، در مسیر سرمایه‌گذاری، تولید، توسعه زیرساخت‌ها و خلق ارزش برای اقتصاد کشور گام برداشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665269" target="_blank">📅 14:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نماینده مجلس: جزئیات حمله سایبری به بانک‌ها مشخص نیست؛ به‌زودی از سیستم‌های جایگزین استفاده خواهد شد.
🔹
قالیباف خطاب به تیم ملی فوتبال: جنگیدید و اراده و همدلی ایرانی را به نمایش گذاشتید.
🔹
عارف: امروز دکتر و مهندس بیکار داریم، اما تکنسین بیکار در کشور وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665268" target="_blank">📅 13:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5969f713.mp4?token=RtHPzx6cIkQv-3gcvfxIYw51YwIZpBXE_zVx1qlkAv-Yr3qv37esrg81XqdhvXFmG9p6EIxXD8acuKmyq-HTon8NECWkX10X0Pqdm8QM3hzSqNI3_8Un8zwKIsnvLPjrAZ2yy5DIxDJFvZnLWaW5le_8E63RyK3TFbUKnyJVrs2Mjpn240jah9jd8KGcd4BZvL7lw_jv19aF-aFrsNUCy4LraB4XQN6PykAH27xAWAjB8QM5bLC6f6zeJcFqIylFkDQU1--V46qz6UyrSs9qayOHNSNbz79FW97Ew8H41l5JRSb26RZAiO5p0LbANDanY_y3IOlyv1FxHdEemrYmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5969f713.mp4?token=RtHPzx6cIkQv-3gcvfxIYw51YwIZpBXE_zVx1qlkAv-Yr3qv37esrg81XqdhvXFmG9p6EIxXD8acuKmyq-HTon8NECWkX10X0Pqdm8QM3hzSqNI3_8Un8zwKIsnvLPjrAZ2yy5DIxDJFvZnLWaW5le_8E63RyK3TFbUKnyJVrs2Mjpn240jah9jd8KGcd4BZvL7lw_jv19aF-aFrsNUCy4LraB4XQN6PykAH27xAWAjB8QM5bLC6f6zeJcFqIylFkDQU1--V46qz6UyrSs9qayOHNSNbz79FW97Ew8H41l5JRSb26RZAiO5p0LbANDanY_y3IOlyv1FxHdEemrYmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان عجیب ازدواج و جدایی محسن مسلمان؛ ۲تا خونه و ۱۱۴سکه در سال ۹۶ دادم رفت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665267" target="_blank">📅 13:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665266">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f147454758.mp4?token=SKatDpfC9UwpcPlN2GYtbgNoB9h6eTJ-yVmM6ER6rbTe2Q83V1MAGE-9JnuTuV9hvet7NMjyOUT7woAkljGYYO103KP14oyfZb-g28Ce9uwJBmZWj3TyVwL5HU2iWUUBEqCa2KBfryM4IDkmYK4Gev4e8bXVE4ccx104CTz21Uv0FeppTdHEFGe5vBQT9Uu6hnu__UFN-CjpyymQ9kZBJ5ZaSdHuF_LXhCFhcEw-rIkdiZ8LTEDdX2cAOEDezn8qOEbljuZ8h5SE-_CZYtp2IlFnpfN0unsv4Mt33sP_1Jwu-n_Ebt1uPwAhhtjdC_Ue-en6GrgV-PpkKz0Uv212Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f147454758.mp4?token=SKatDpfC9UwpcPlN2GYtbgNoB9h6eTJ-yVmM6ER6rbTe2Q83V1MAGE-9JnuTuV9hvet7NMjyOUT7woAkljGYYO103KP14oyfZb-g28Ce9uwJBmZWj3TyVwL5HU2iWUUBEqCa2KBfryM4IDkmYK4Gev4e8bXVE4ccx104CTz21Uv0FeppTdHEFGe5vBQT9Uu6hnu__UFN-CjpyymQ9kZBJ5ZaSdHuF_LXhCFhcEw-rIkdiZ8LTEDdX2cAOEDezn8qOEbljuZ8h5SE-_CZYtp2IlFnpfN0unsv4Mt33sP_1Jwu-n_Ebt1uPwAhhtjdC_Ue-en6GrgV-PpkKz0Uv212Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر آمریکا در فلسطین اشغالی: خداوند ۳۸۰۰ سال پیش تصمیم گرفت که اورشلیم پایتخت اسرائیل باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665266" target="_blank">📅 13:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665265">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe9a027b9.mp4?token=kk9PwjwaeVWn5p_NijlfXvnBefd_s6veL9jvcg3HhPNJAQ1uI2RVtlQyvnF2hu65E1NKY-VdJORlASFmR28Xp47R9ADcKVS857zSoFI43iXNCNcHYpldEaCBawHRnlzCnwwl0icTrCPh-nje7VbjsTJybZuCUJG7F4Gl3dtWsQmUOKKY0M2z1hN3ksAgs5e86Ro5qMIReeNQAlnvcgwqjMrDA6YhpsL-1tzDwbIb2HpMrxPylaFuP1RLs1eDiqZ640aP8NxSpdXrHLuAMV0cuNR_LnvlHa8jGLngTUKZnyw6RZAm2RUbDKPfr8OIx_kQrNJ39by6ws8MiUlMDVSyjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe9a027b9.mp4?token=kk9PwjwaeVWn5p_NijlfXvnBefd_s6veL9jvcg3HhPNJAQ1uI2RVtlQyvnF2hu65E1NKY-VdJORlASFmR28Xp47R9ADcKVS857zSoFI43iXNCNcHYpldEaCBawHRnlzCnwwl0icTrCPh-nje7VbjsTJybZuCUJG7F4Gl3dtWsQmUOKKY0M2z1hN3ksAgs5e86Ro5qMIReeNQAlnvcgwqjMrDA6YhpsL-1tzDwbIb2HpMrxPylaFuP1RLs1eDiqZ640aP8NxSpdXrHLuAMV0cuNR_LnvlHa8jGLngTUKZnyw6RZAm2RUbDKPfr8OIx_kQrNJ39by6ws8MiUlMDVSyjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قتل نوجوان ۱۴ ساله فلسطینی توسط ارتش تروریستی رژیم صهیونسیتی در کرانه باختری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665265" target="_blank">📅 13:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665264">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTxvKgQHRyxklfZZz3jacNhv8BviG_8bLobZdPmUi7y23cM2aCoJLoPBU4igH1pyHRhDulmCtc6JprFrGNGtPa23gPVnJkD360UThLie_uUx86LgT1wCFNQortH46PhzGio8pW_xdWe64hptTesPRkHMKate-XgI9A1no8XH9vQ6EcHWJNVjG3Y1mSJxubp3ZNKN5r3baq3Gz_DgPb635nlrrWtLS06CTYHHLIzkMQ5HvESEBcO-UqKtDoNmu-QyNMnjr0N9cf7A1Z_u1QcC3U3if-i6_aX0WPv8_abmuXynq3bqwd5gY1-VQcENW2s__S1FbT7Q9I1BsSoPo7ou-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرفروش‌ترین بازی‌های جهان/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/665264" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665263">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8NK5vTCJRbEv9HjLkXQfXC8cmhZSnuYei7slFllD6YtYV5-RUzyHLmr4Qb7blAQDXsHI5QVB-paLHw6YW_hBidreSRwuCq_ChMe9wyRPyKnj3ogR97sQksyNwnGoSCS732ebX0q2elyvkMGIGeELwgKDEU21gAeDr197e9ry6Uur-IyMoiF1uMwrH0LqFxmptfnfAJ2W6rX9c2PQj3czLv1hrCvQllG06rSaTNZ7XTLI5VEcYQKOsA-wWpwO38XMKxB-q_Y7aInXRrg-0JhbnaToxQXvITrT5Xcmg4DMjMll4yMvcYMTywSYnS99nzgToGrM3Vy0lFArBDDAL06bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت نفت اسیر جنگ روانی نخواهد شد/ وزیر نفت مجدانه در حال انجام وظیفه است
📍
سامان قدوسی، مدیرکل روابط‌عمومی و سخنگوی وزارت نفت در اکس نوشت:
🔹
جای بسی تأسف است در روزهایی که ⁧وزیر نفت⁩ مجدانه در حال انجام وظایف و تعهدات خطیر تعریف‌شده ⁧وزارت نفت⁩ برای خدمت به مردم شریف ایران است، عده‌ای معلوم‌الحال با شایعه‌سازی به‌دنبال اجرای نقشه‌های نخ‌نمای خود هستند؛ وزارت نفت اسیر جنگ روانی نخواهد شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/665263" target="_blank">📅 13:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665262">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d177a891d9.mp4?token=dhr93xo6SxF_HRzEs8KJxxqfq87w7nym1bWrr8M63rAiUDfjddt8LlEvmMoniCp0_YUBdA-IUUt5iY4QZhpxHTPx2tiZIelFQB9hjRMwsrqg4LVnJ6eZNZ-c-cn1C_8It4S_9Ui3P2R0-9fHG-NEQ4jJTPu2q5R5-9Raz-sp-d-5XMo0mbDGQVo68ls9mzhs5NsgCgRDEKFTP516K9xFb4J34Ah8sUUJyqooapKQYMcwCHl14glafCYZXT9GqvtorMIzE96FYO9dSP-rhwmFMn3Jl1lyX-7513tae4P2b2PbVprDMP9KQPDY1CMwaePibgEbB1xz9iOaV5xb99cZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d177a891d9.mp4?token=dhr93xo6SxF_HRzEs8KJxxqfq87w7nym1bWrr8M63rAiUDfjddt8LlEvmMoniCp0_YUBdA-IUUt5iY4QZhpxHTPx2tiZIelFQB9hjRMwsrqg4LVnJ6eZNZ-c-cn1C_8It4S_9Ui3P2R0-9fHG-NEQ4jJTPu2q5R5-9Raz-sp-d-5XMo0mbDGQVo68ls9mzhs5NsgCgRDEKFTP516K9xFb4J34Ah8sUUJyqooapKQYMcwCHl14glafCYZXT9GqvtorMIzE96FYO9dSP-rhwmFMn3Jl1lyX-7513tae4P2b2PbVprDMP9KQPDY1CMwaePibgEbB1xz9iOaV5xb99cZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدیدترین بروزرسانی نمودار مرحله حذفی جام جهانی ۲٠۲۶ #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/665262" target="_blank">📅 13:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665261">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YInJEe_PILdJpwrkRIWby8P0FaxNzcEtmeZiQgMkztsqlsSp5AsgBMebgFQLtCEo8Ld0dT8WjBrN6jkoykUQPVwKBVeGdzRaCvHTFRmrHuCVhQo8se7U2580rzVvpQitYbZIJ0NOD4YSAt3PEWyPgYhE5Z2-tdATyyN1bO6uW1ZBSgzhO-eCHKXm-BH6hg_ChDaomaEXBtY1mfGv4UYEEykXodwERT8PfPG40xmRSTxvadWwPDqJxQBSxtfi18veT44H1EksHSfsHyF0lP2ylUrOllQPjxDhuDe7ASjfl2pW8EqHYpzCSYqZ4E3NMIVqtGSxZIluteBXWKAE5VFKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
علاقه‌مندان به بخش
گزارش ویدئویی
سوگواره «بدرقه یار» می‌توانند پس از مطالعه آیین‌نامه، آثار خود را از طریق لینک زیر ثبت و ارسال کنند. در صورت عدم امکان ثبت از طریق سامانه، ارسال آثار به شناسه رسمی دبیرخانه نیز امکان‌پذیر است.
#بدرقه_یار
▪️
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
▪️
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/665261" target="_blank">📅 13:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665260">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbdhRGrXb7PJG4bjmmP83YZTNJ2HJxColOwlw3urXdcN5ejH76WOvzRTW4Lk_rGGEUk4pEVZ13lnxjI9vvCvAddcBcYAN0rSLu_MBFdxBlAlCq3KJuuLxzGwNGs3jbYFKPjxlvpzwicRrh8Ga6VNfxHpJWRNgCJSJIHha7mjkXANcBj8Fhi5oqBax0d8praZQJrLTx1HaypYvihNwmk-FL9fxP-R3V4-0JXxbhC9-byC2Uf6AL59VFmRZRqgnfoMDwFfVbDpBLrhjtwfLMuahNlC41RNkFxYriD9MBSxZEKM4QYbVOvo0ckU_Pjfg4inAM8MRgt4u1-s_po9xcMAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات تعطیلی استان‌ها برای مراسم تشییع «رهبر شهید انقلاب»
🔹
بر اساس بخشنامه سازمان اداری و استخدامی، استان‌های تهران (۱۳، ۱۴ و ۱۶ تیر)، قم (۱۶ تیر) و خراسان رضوی (۱۸ تیر) و همچنین سراسر کشور (۱۵ تیر) به منظور تسهیل حضور عزاداران در مراسم تشییع پیکر مطهر رهبر شهید، تعطیل اعلام شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/665260" target="_blank">📅 13:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665259">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048ccc1bf3.mp4?token=PTEGE2tRx2hmKWNk9Ea0LWZMB6znF_ZIjvBq26dtAyyCl0O_fxx1Wbu4oR4FeYoJotxArMIaCRSv4gP5-ih-KJyxJDKmbGvNO1LBwjHSalFPcWq2WSSYCNrRTwRdnSvMaSfHqYKCWG3V3V2sXhHXOBfm_o_ELbP69Jr3LaGjh5tJIA7dkkH6ZLfyhRE0sRx15krK-lXaqesAiw7tGV8nT4Qj8KuE2za5tU45e9bov5ifjh3KpyjmEyY40cdTwGlu7FEFcvhZ0klHMJKgcQeOrJvDBGACNT_XFgl58TfJ2qYc2BgT2sQncRQbfuw7CwBtkLdk1aZr4om15F0z7UJ7lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048ccc1bf3.mp4?token=PTEGE2tRx2hmKWNk9Ea0LWZMB6znF_ZIjvBq26dtAyyCl0O_fxx1Wbu4oR4FeYoJotxArMIaCRSv4gP5-ih-KJyxJDKmbGvNO1LBwjHSalFPcWq2WSSYCNrRTwRdnSvMaSfHqYKCWG3V3V2sXhHXOBfm_o_ELbP69Jr3LaGjh5tJIA7dkkH6ZLfyhRE0sRx15krK-lXaqesAiw7tGV8nT4Qj8KuE2za5tU45e9bov5ifjh3KpyjmEyY40cdTwGlu7FEFcvhZ0klHMJKgcQeOrJvDBGACNT_XFgl58TfJ2qYc2BgT2sQncRQbfuw7CwBtkLdk1aZr4om15F0z7UJ7lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف پمپ‌بنزین‌‌ روسیه‌ که در پی حمله موشکی اوکراین به پالایشگاهشون اینقدر طولانیه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665259" target="_blank">📅 13:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665258">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
معافیت تحریم نفتی فقط برای فروش‌های جدید است؛ مبالغ قبلی را آزاد نمی‌کند
علی مسعودیان، پژوهشگر دکترای حقوق بین‌الملل:
🔹
با توجه به موقتی بودن مجوز ایران، باید در قراردادها، سازوکار‌هایی برای دریافت قطعی پول و جلوگیری از اختلافات بعدی پیش‌بینی کند.
🔹
اگر قرارداد در دوره اعتبار مجوز امضا شود، اما موعد تحویل نفت یا پرداخت، بعد از پایان آن باشد، ممکن است دوباره با محدودیت تحریمی روبه‌رو شود./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/665258" target="_blank">📅 13:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665257">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای رویترز: مذاکرات فنی غیرمستقیم میان آمریکا و ایران در دوحه، با میانجیگری قطر و پاکستان در حال برگزاری است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/665257" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665252">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fx6oboJ_Ko7B_rGAwVRM3VYA_IFrAW749_YIaK--D_g4-O3qhsJSyabqegoWuIJIqyEBgT3y1K-9o3xr-7yG81fCa6jn9hnAKcdGwZ8OwIu5uf_QeA472mloMpwAKcJCIPFG5ojs91u4odBz--mBdsIybqXeF3pKkZXmVt_w6gnUmeoNrXjjG1u5EPeLqqQccaItJkSi_NweaOE6Di_8BB3izmgD8-YGNRKqegH0g5_vk70fPwmx2bl7d68EMjijxO0Olci28ZAsDHkoLA7njFHvj3CxABwe1yrl8gAtcEseEsSytzmQiYn02cXPDera9-tGnb6wi_IDfVDRTsPncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwbdMOvcEMe35BiKF1xnj67Un0rD3qs1NYshyiHwjQ6n6110TD22nHAZw4rlk34vIhli9y3M9BncvWUOId90KK8CV_nGKV_eqSUHqA8LADiSNgS255GxPhm0gsXP67oYNXG6cQiiDZPLsFJcSeiAU6NWlftLGi8M7RYVGNf0a9h3dolRZW6cPgvRIklCb5fxUyec7T_t20y3VLPHq5sNVZHedv9Jt14bQ5Ui8ka77ighIO10pDLmYqzEKhsshyUeS-SxZJNpiL2cQKG4yirTam0DDbN-aKHYDKpnQ76lKKeXBCKKZbRjtgdVhC2l5rLStTwd84sGToormKnagf3Bzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TETeS2w5ByIyMI-srkwbbRRnZstAQSatSAFpiMoYr_4qD4OnROAC5_F588Iz51EFEnpGreEEcWGWCIrCKtL3N2KQPzHlB8xMIDphWme0IeKMkf7-EIMC1EA_6ycxBxEjERjj68mrvAzAZl2PYv_7RAYKcWGwprFPtPUYStWou-oqRDpnf_uVuxGKB4tYvzutifOJ3pF3aBooufOB_E_DisBdXGVIg_9gf_bG8FIRww9dbuEfTsjLTe8Z2j-8oRot5PnPWQEIo9rkzP78bpy8KxAbN462Txpg1piuKJQ0Y63fAfUHLJxxo-eRKr3ZzhGUThVp0jE6CODJPcgmOxPqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSrsM3h1TYicFwX2rvRRHWyHOcuLLs7S2FDsJB7zKzY3UIGdB6KEfwyiZLSoNwFG5z7WQaDjaidvkJeQYKfT8wvPZRRUfU2CehmT7qgGDaWQ9Vz5DLQymAlM643H2flkDlO1K4I-HCmXXoRkMPXkz-1Zs17duDGA77akDViDViuVVY6oFNXBR6tyOXhHZZM69ym1qNewOlG8v-DRDoGDSMG5mlN-A__1W1Oa05gGS94qtqv3fjTx5tDdqUVzjCSWsJFywcyNkwOBoUWjyOn3IoNCY1jaOhNllOMorfpyUA0J7VS_vE0Bw6MH69twM40k5spdkCzzXWwpWVv8WFfbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlxJ9T9R8Qpdywdl6GicZWYO6prMErSH1xMkYwB7mSThG3OYME6nilTW_q_HIAcmlphKqvbP-ELjCODW4f2Xv2RcGrT1gghoibdD0UWR23hCmt12gQLYvXahSKDvk4KOtTkh40F5T5n2mUMvfc0HIB9eBW-t__uDLOZF-04-Mcyc2tWQQBkFNIM6h1AsJpNFGU7Pm7IgbElw0aJPiTv5gwwVLr_VKkf2-t9pD3El0IuCWkYm3z3zuNVUr0iDzg7foebDOtC8bijJGUGdW607nA9WY_zWnXxlaUYTaVe8xBwJpGtWaAdS_UMJlb4QP8kJv7bo5O8Hv2XTLt2-ga0exA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نکات لازم و ضروری برای حضور در مراسم وداع با رهبر شهید انقلاب اسلامی
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/665252" target="_blank">📅 12:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665251">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وقوع حادثه دریایی در آب‌های یمن
شرکت خدمات دریایی انگلیس:
🔹
یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665251" target="_blank">📅 12:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665250">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ایران تلاش کرد عقب‌نشینی از جنوب لبنان را به ما تحمیل کند، که این اتفاق هرگز رخ نخواهد داد
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/665250" target="_blank">📅 12:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665249">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4741c4b552.mp4?token=r2HYhC6KWR7hlGfw4OhER-fB_ZPxXs2kcK7Hj035tqFPTcupun1qDYfGJ7rvRWvkf94JcgOruex_dfV1WpUQZMjpXknu45N-FRPy-pVLqI1XwPOWBnctKi0o89DiytREP9-mgp81_SeacgPTc-gVmpHcHkE3j-deEbawmxiwg1RJt13zUE4kVDsa99DwP_tkZmSgC3KV58uYiD93ydc93ur3E6z1mubkyg7X2h6smWkhnUzxc726iuk23pvPER665PH38Wc1qOGJb_HQHhkL7_ceOEpqKQyQqLCrDlJtC9AhgrOKBA4jaoRrBUSJwI7LTt2xYgdWaWMY-erOMdm2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4741c4b552.mp4?token=r2HYhC6KWR7hlGfw4OhER-fB_ZPxXs2kcK7Hj035tqFPTcupun1qDYfGJ7rvRWvkf94JcgOruex_dfV1WpUQZMjpXknu45N-FRPy-pVLqI1XwPOWBnctKi0o89DiytREP9-mgp81_SeacgPTc-gVmpHcHkE3j-deEbawmxiwg1RJt13zUE4kVDsa99DwP_tkZmSgC3KV58uYiD93ydc93ur3E6z1mubkyg7X2h6smWkhnUzxc726iuk23pvPER665PH38Wc1qOGJb_HQHhkL7_ceOEpqKQyQqLCrDlJtC9AhgrOKBA4jaoRrBUSJwI7LTt2xYgdWaWMY-erOMdm2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دونات فوق‌العاده خوشمزه و سالم چون نیاز به سرخ شدن تو روغن نداره
🍩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665249" target="_blank">📅 12:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665248">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNq0vhrIbMDyc9sMagWPpklNZJLsWucmUbZo6Q8xthK0lXKbABADTtoVF5xVsNmd_dy7yn7Hjds2OW4MbXnCEayD2pUJGteFf4fkrsiHsaxfLcUE3nnlvwLz76qWThUq7Q5e_qsPn2-LrMobMqwCpzOYXt97lTSd7EsCnoZfNHPgjRvWnYcxKlrK24O4FIn5D_ZVH_shuD69AhbwgKSgN3pCts3s615FE3oX7qm9s9lUBZrOhKV7YISh_Ex6VUF_bEFJOFiAHVLL771gMOixpvBm9eBu9Cp1FWd0CpJUDWtI0I1j76_fd783gGAxThV1twFdXyyfNgQn89GbfQHhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
میزبانی از زائران مراسم تشییع رهبر شهید
🖤
#تهران
#مشهد
#قم
🔹
اگر در تهران،مشهد و قم امکان اسکان دارید، با میزبانی از عزاداران و زائرانی که از نقاط مختلف کشور برای حضور در این مراسم در حال سفر هستند، در این حرکت مردمی سهیم شوید.
🔸
از خانه و آپارتمان گرفته تا حسینیه، مسجد، سالن یا هر فضای مناسب دیگر، می‌تواند چند روز مأمن آرامش مهمانان این مسیر باشد.
🖤
برای ثبت محل اسکان:
👇
🔗
https://mahame.ir/s/gsA5HY
✅
یا عدد 40 را به سرشماره 3000143030 ارسال نمایید.
ماهمه، برای ساخت ایران
🌱
🌐
www.mahame.ir</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665248" target="_blank">📅 12:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665247">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBAmp_p-sV9AhPKmGZhdqVkJm_SrqGRgQZSOGOsTUXJbYCptvcxJK-jCGdhzSmQon7UYnOCMuAmAYXzBJ6JqbrgbxV3r6iN2E-t5PfU_Q8F_r5LbMdwx9hmYT1wt-4Ti9lVcDIpZwWau7qTMqMwwhElHuhAuM1owQ-lA8RTDO4OPL31XFAh89bbeBlKneMvSLJDBbCd77_jJiSeVuBafCgAsvUz6raLqsoaRSXzn9XGkLTUGTcSmhFfS1ddBTgKzecT9-hptRqpxgX-EKcLSvOzDCjtu3Qoa6QsH20EopI7ryJ0PPzDucyKZEHE0QctU1IUNjNAtMZBIMmFPdYTxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با جهش ۶۰ هزار واحدی به ۵ میلیون و ۱۸۷ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665247" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665246">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
صداوسیما: یک فروند کشتی که از مسیری غیر از مسیر تعیین شده در قالب نظم ایرانی در تنگه هرمز، تردد می‌کرد، به گل نشسته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665246" target="_blank">📅 12:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665245">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3b6141bd.mp4?token=nLWco570VMbzoFGkgir0d1DX5tEs170x9agfBWgqA1NLmUk7txzZRMhbkv6bZSG1nunPcHDyt8l0txbWvXq7i43NVuTeBrHlI6C-IA1exKy0OURvdBuazahw4TfbfGIFboZ8jMnM1aovfJO1S2UiTKn0r7tTcb06z49WlgDr4OiU35NJL551oN_LBGuZSoC8TaZRr07Xq90pcvR8n-TTFu_qeaPWbOmMNmCugyg4FUjKhhOD6O_10CSZHg-hdSNhwk25aWgpIzJz7Pn4DM2AXPLCrdvDQgzvXFehmKQsMzhzZnkdkLFiKZljWeJrcL5oUPK6NzwlfuxTDbfh8gGtSzFOOxBEG_9LVSFTcYxBgwbx6cyfLPBkQFS4ThJy20hBV5vP1g1Gik8cAbgA3_6ZU3bwnXyaJKkclhyIN9PFlRo8PwkVOR1_fPRtvugjNpS3Mg8wlLFv-6JyTTj8E95PLcRqbR5QZixhCs3bqhgrkf_3bPcOeYckKt-9ZtkyAnLayhxxJF8T0zf_WqpxBcOI95zOdKb8ltSY9DAEPZIq5Z_zp-F7GptjDDCOe1ZgHXE6xAvo3K8UtG336SZyv8Wmm7Mz13cVhnWwFS1nrWico0dAg2yaL0CJCQFDQzFx9XndGqLI488f7aoqA2A5EZk-oWfrQTKS2BtTbFZVmBtZVlo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3b6141bd.mp4?token=nLWco570VMbzoFGkgir0d1DX5tEs170x9agfBWgqA1NLmUk7txzZRMhbkv6bZSG1nunPcHDyt8l0txbWvXq7i43NVuTeBrHlI6C-IA1exKy0OURvdBuazahw4TfbfGIFboZ8jMnM1aovfJO1S2UiTKn0r7tTcb06z49WlgDr4OiU35NJL551oN_LBGuZSoC8TaZRr07Xq90pcvR8n-TTFu_qeaPWbOmMNmCugyg4FUjKhhOD6O_10CSZHg-hdSNhwk25aWgpIzJz7Pn4DM2AXPLCrdvDQgzvXFehmKQsMzhzZnkdkLFiKZljWeJrcL5oUPK6NzwlfuxTDbfh8gGtSzFOOxBEG_9LVSFTcYxBgwbx6cyfLPBkQFS4ThJy20hBV5vP1g1Gik8cAbgA3_6ZU3bwnXyaJKkclhyIN9PFlRo8PwkVOR1_fPRtvugjNpS3Mg8wlLFv-6JyTTj8E95PLcRqbR5QZixhCs3bqhgrkf_3bPcOeYckKt-9ZtkyAnLayhxxJF8T0zf_WqpxBcOI95zOdKb8ltSY9DAEPZIq5Z_zp-F7GptjDDCOe1ZgHXE6xAvo3K8UtG336SZyv8Wmm7Mz13cVhnWwFS1nrWico0dAg2yaL0CJCQFDQzFx9XndGqLI488f7aoqA2A5EZk-oWfrQTKS2BtTbFZVmBtZVlo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاوه‌گویی‌های سوشا مکانی، دروازه‌بان سابق تیم ملی، صدای مجری و تحلیلگر صدای آمریکا را هم درآورد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/665245" target="_blank">📅 12:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665244">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61525dee8.mp4?token=gDstB7C4IMtQo-MzWRgWVCHYNmL3_oylTma8LVqOG_sKDPEZBBfFjBp9-0Ce4D4JIRWAbRgrWqh8QwT5-vhxEfQtfCzPa04JXrtEWtvosJHjjRIBlChwneQ-5mWMp_OlBzh3caoX9gNrRcmxkIaaDuvUv801Wg2YHMDsL3cxeQGB_1tcZAujKNi6m1dNVVvRnJtNGKmbP_75prbXBFbTm6k8nZ4QdwiygAoCAzmvu7EwDNfBAPmdAHY8mItb0pJx3AemD6dii8J5yQs5T1yua7i6qn3z2aleGpQRgtIwCmbh8NxiL1-c5DLLzSUKpVm5houMeED-K2-ADelpmEKXOhGlEvV-CqTXH2op-4vhpGkUjN93iD3l31qqM1LqxK_C6i7wTnIAN8BNE_OXJYTnOz9T4dUuokC72jFO3_BIQCrhpQK3tG_HolS5hidl2LRiral8P9IcW8oOiTMchzGLITXy26O1GIo_-9rdcu8EoUPIXlEK_TUm-7qkpxAj3iu-HqvH2Zzjoj4Vwz7cpF0tm0lZozkj_H8mrSncDvN148Xci-uVFHMh_f2y3TEOHFyPUEWnaNbxmvf1GcLBb1g2bnpTi9QKTjZO563_RsIAlCeSz-g8KN3lHkpVx_A2yRtaG0unAIPc_bH_CEhLcRRI_kO5TeczW_p-onrZTGumFsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61525dee8.mp4?token=gDstB7C4IMtQo-MzWRgWVCHYNmL3_oylTma8LVqOG_sKDPEZBBfFjBp9-0Ce4D4JIRWAbRgrWqh8QwT5-vhxEfQtfCzPa04JXrtEWtvosJHjjRIBlChwneQ-5mWMp_OlBzh3caoX9gNrRcmxkIaaDuvUv801Wg2YHMDsL3cxeQGB_1tcZAujKNi6m1dNVVvRnJtNGKmbP_75prbXBFbTm6k8nZ4QdwiygAoCAzmvu7EwDNfBAPmdAHY8mItb0pJx3AemD6dii8J5yQs5T1yua7i6qn3z2aleGpQRgtIwCmbh8NxiL1-c5DLLzSUKpVm5houMeED-K2-ADelpmEKXOhGlEvV-CqTXH2op-4vhpGkUjN93iD3l31qqM1LqxK_C6i7wTnIAN8BNE_OXJYTnOz9T4dUuokC72jFO3_BIQCrhpQK3tG_HolS5hidl2LRiral8P9IcW8oOiTMchzGLITXy26O1GIo_-9rdcu8EoUPIXlEK_TUm-7qkpxAj3iu-HqvH2Zzjoj4Vwz7cpF0tm0lZozkj_H8mrSncDvN148Xci-uVFHMh_f2y3TEOHFyPUEWnaNbxmvf1GcLBb1g2bnpTi9QKTjZO563_RsIAlCeSz-g8KN3lHkpVx_A2yRtaG0unAIPc_bH_CEhLcRRI_kO5TeczW_p-onrZTGumFsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش خیره‌کننده ۲۰۰۰ پهپاد در آسمان هنگ‌کنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665244" target="_blank">📅 12:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665243">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac3fe55de.mp4?token=rIDLskD-edinw_bkjcokIVXIWhuql3WrSNzgyKzgtRHuEtk-R9cT8TuGMGvLB3UcidpTfdQcBQK2bERRLmG-TW-VDFkc6ME1ETusR2PMjrtb22IrbuuZJjLlmVo4AIgpM1dS7VyADYsxmLk4rg55oizC9bIchSj0_3s05vw9NypADW4mK1OcB8yWB8oUafGNp3xfz0lrglyuB8PO1O7JF-4jWE_KrBau0YDszTW1UjD76oHjwjcPSaYZ6btCt4TI-0aiF7zGKIUdWTAMj6RewnuOQOdRBt_MfvRdTBEJUkehLJCsO8S5jF1xDAX0yfSAO7fpgjacDUaM3DypBOJ5whgl0sKiU6tIIsUQ0Z5zCUTyaI4j-l-EhphEVbFXu6mecOzKLzD8Tpm7dIZiCqSj0jX2dDicDhahpbvjCu1lQ6F1Z5cxlpLgZLF4TLyfI4GsSBXNmkKXCQG88k6vOJ07Wx08_e4pkbRkFZIv2hEZ55_9SHujrWhsGcQmUJ41gh6locvp3KQeF9P1YcRH6Li56aH2nqBMYVheqTWL-uKM7umoldtddGQrYxzJgaRTws8UlHXvJhtOws2Xsy88gvgaMtamD1D6dkSRiJgATAjRFqpBDfVM0CevtMqNbksQKEVyyIF13Ge5xVD7rkdu6YvDQC5lXB72GG0WwavR2qu9PBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac3fe55de.mp4?token=rIDLskD-edinw_bkjcokIVXIWhuql3WrSNzgyKzgtRHuEtk-R9cT8TuGMGvLB3UcidpTfdQcBQK2bERRLmG-TW-VDFkc6ME1ETusR2PMjrtb22IrbuuZJjLlmVo4AIgpM1dS7VyADYsxmLk4rg55oizC9bIchSj0_3s05vw9NypADW4mK1OcB8yWB8oUafGNp3xfz0lrglyuB8PO1O7JF-4jWE_KrBau0YDszTW1UjD76oHjwjcPSaYZ6btCt4TI-0aiF7zGKIUdWTAMj6RewnuOQOdRBt_MfvRdTBEJUkehLJCsO8S5jF1xDAX0yfSAO7fpgjacDUaM3DypBOJ5whgl0sKiU6tIIsUQ0Z5zCUTyaI4j-l-EhphEVbFXu6mecOzKLzD8Tpm7dIZiCqSj0jX2dDicDhahpbvjCu1lQ6F1Z5cxlpLgZLF4TLyfI4GsSBXNmkKXCQG88k6vOJ07Wx08_e4pkbRkFZIv2hEZ55_9SHujrWhsGcQmUJ41gh6locvp3KQeF9P1YcRH6Li56aH2nqBMYVheqTWL-uKM7umoldtddGQrYxzJgaRTws8UlHXvJhtOws2Xsy88gvgaMtamD1D6dkSRiJgATAjRFqpBDfVM0CevtMqNbksQKEVyyIF13Ge5xVD7rkdu6YvDQC5lXB72GG0WwavR2qu9PBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام کاشانی: اسلام دنبال چشم‌و‌گوش بسته قبول‌کردن افراد نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/665243" target="_blank">📅 12:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9UldgaY8suXF12Y9WT-KQtfl3IjxIJNrhr-jK3qewuuapjwly5CUXsAgo-SzyuogzjKHtCIsoCBHV_lPKSKpq0zZLu3JeG0dAeQhwsQLVR2vYzny1-TfIdxXuGEE25DHl5oe_Ce52ZyJk4KwfZP0AFdYaGgtH6EWoQRwmkbcegY4aC1w8WsPUR-3qAGijuD6KhdaDNCqE-tPCQ5Oh5EZufn6rxDK_JRtas8Buis5uoQpXfLYuRBcykRqaHxvul4dZFgWeLwqi6znIPNKiU-zzW_vS_kBUKvMiaPUsIX8p_5fD3zWkwbV1OigRQZdQ7N4TbxPMipFueJ7cU27jyXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹۰٪ آدم‌ها سؤال اشتباه می‌پرسند؛ برای همین به جواب درست نمی‌رسند! می‌خواهید موفق‌تر باشید؟ از یادگیری این مهارت شروع کنید. #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/665242" target="_blank">📅 12:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5bd20ec96.mp4?token=JC24NPPiT6-wu_8SVxHgodEt-MXbAwTuhh-XsCOODa6EddOYJKc4L8YondxouOTFbK2RSF4sE7IJ2wRyqbJuy27KaBgV84QozxcQgEyRgSGg84hAiYGEn72rMlt_zCkKxeBqzhhZjYR7_6QmXstcgGR4TN0EWSS6f45LAKeiryojI4vuz1eYN5hfgIULSUENuoEPIh8SzpZGTakFu50tTvJ9exJU2CiEmVwK_37824fkyA8fz7SXirxFTfbD5yD_Zq9SL-IRlmvwcwYRfgxUZAVaoADzXJ_8pk2RCKv-dvjgQf_bqHY2wgoLP8BocerW84M06e1ywNTmBg0mmxM0znNiRiaWHnT-hmygB4Y3MZPxgvzx7ygsZ3CcUC_sG1AApY_SguyjXKeSwMntlNL0tyjyMbvsTS4gB_LuOsPE3-l_7V2g016vOwl4BW5VLqCkaeqj9HGixPnX478SFKQwWIywZrLYxGTGnxwowuhPsQKooOmVuERndkGluBxRnOrskuLmoKSLB3x9zfujKP6CCQg4JE4HxQSPFF51Tkj3MGkjY7rL26sDmaNHbfanMiNbwK-h412QfoeO3ZNhv-uW_uYoeTNHzkZu6OdFuPIl3TKpewDZxKB1OXVxjDM4ZUFoK-_RSALGW3FU6eivqlDfqQHKtL4thsFQWylAg4NPSQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5bd20ec96.mp4?token=JC24NPPiT6-wu_8SVxHgodEt-MXbAwTuhh-XsCOODa6EddOYJKc4L8YondxouOTFbK2RSF4sE7IJ2wRyqbJuy27KaBgV84QozxcQgEyRgSGg84hAiYGEn72rMlt_zCkKxeBqzhhZjYR7_6QmXstcgGR4TN0EWSS6f45LAKeiryojI4vuz1eYN5hfgIULSUENuoEPIh8SzpZGTakFu50tTvJ9exJU2CiEmVwK_37824fkyA8fz7SXirxFTfbD5yD_Zq9SL-IRlmvwcwYRfgxUZAVaoADzXJ_8pk2RCKv-dvjgQf_bqHY2wgoLP8BocerW84M06e1ywNTmBg0mmxM0znNiRiaWHnT-hmygB4Y3MZPxgvzx7ygsZ3CcUC_sG1AApY_SguyjXKeSwMntlNL0tyjyMbvsTS4gB_LuOsPE3-l_7V2g016vOwl4BW5VLqCkaeqj9HGixPnX478SFKQwWIywZrLYxGTGnxwowuhPsQKooOmVuERndkGluBxRnOrskuLmoKSLB3x9zfujKP6CCQg4JE4HxQSPFF51Tkj3MGkjY7rL26sDmaNHbfanMiNbwK-h412QfoeO3ZNhv-uW_uYoeTNHzkZu6OdFuPIl3TKpewDZxKB1OXVxjDM4ZUFoK-_RSALGW3FU6eivqlDfqQHKtL4thsFQWylAg4NPSQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کامپیوتر در سال ۱۹۹۴؛ فرکانس پردازنده: ۶۶ مگاهرتز
🖥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/665241" target="_blank">📅 12:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665240">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4ZtS8KkO1huLCSVTmoCN0FBnCGYs8DZV2PmtCZY-ngQuQRF1EbImvKte2R607_1WWTPf9Sp0UymrNMbtfFF6p93GcEnzCcByuYE-oHFvgXcjVZzVspQrj1QOX38gwTjEN-6Nx05tsdxfUPiRqh7Aoy370rjW_QGEXc-JkFGiZv0Lg2-Lm7qGDS163ap8VNrIE_JclFHQ_swq15jWWbwMFDsvF634vzt6rtjgBBWmCNI6sSNQWNKky1xdLYWCTIc-2hQuFiAJI5VkyKbydVsvQzVrgD5xp7qp1F6M-ovcV6Eo4WuXn96n4h9if17BgHoRzwcipT4dvkNxQQs32Vy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازخوانی بندهای کلیدی بیانیه الجزایر (۱۹۸۱)
🔹
در توافق‌نامه الجزایر، ایران متعهد به آزادی فوری گروگان‌ها شد و در مقابل، ایالات متحده لغو تحریم‌ها، آزادسازی دارایی‌های مسدودشده و عدم دخالت در امور داخلی ایران را پذیرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/665240" target="_blank">📅 12:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665239">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpQZsmksF3_an5OWKsZHU3zLzkEnlAHNhMFK8Am2mnKmkkwrY_wSpQqJ59HT6hgbVhkOOfVel2ktRiR_uWm_1pPe7LK8S1c2xc1lpJlZIqQswk5VPF_YAG0m1a9PXQd8baXILBbqzz62X6aVBfbeNFtxljPguoRDNO7gm4OyrAInhmyXLamNjTphGqjqQ3IYtORJDl-mg8OAIEBDHrCVs7BU9BEMQxtuZpWzkhZ9M7fgFYVnkit4s5YLPyasxCG8PhwNf_9ksxW_cX4p0m1cH7o2eFKARMsJxKqSi3qKZ6DEnpWnaIv_tyo-0_tH1BP171Pph5rMFaSX7PMBLD3KhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی عضو تیم مذاکره کننده: ایران به سرعت درحال بازسازی زیر ساخت‌های غیر نظامی خود است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/665239" target="_blank">📅 12:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای رویترز: مذاکرات فنی غیرمستقیم میان آمریکا و ایران در دوحه، با میانجیگری قطر و پاکستان در حال برگزاری است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/665238" target="_blank">📅 12:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36c3ef379.mp4?token=t3rxc1q9-uBNjCozcmYFiDWZVDVNav_7qFKaHWSsthHsPBKVsbkn2zQeFms0qWH6USxFWCtebXXmuXu0ZfluBmfugdtv-HmvTsjEXIUvrE8jL0y9PYj58rySpU_fcaEaaBrP8fA9Fz3NTcmfBUh6rUzkruhehpAB0ozAoRgyOd5YwpoUHbdBLBVw7eI8LzESCOjZV4uSMvlDxK2zOcSi-Pw_atSGC87BYpSvhOAFBmPLjo4AhE0vaJBlbpb5WcdD7ZcGpVkZXNLGYNwaVmKQhseCYGdCPQGYOdAJl-o3FV1QBetEoBgJ5r8bqRyKmH-wX0wzLl4xDA9E5KMlTzGJ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36c3ef379.mp4?token=t3rxc1q9-uBNjCozcmYFiDWZVDVNav_7qFKaHWSsthHsPBKVsbkn2zQeFms0qWH6USxFWCtebXXmuXu0ZfluBmfugdtv-HmvTsjEXIUvrE8jL0y9PYj58rySpU_fcaEaaBrP8fA9Fz3NTcmfBUh6rUzkruhehpAB0ozAoRgyOd5YwpoUHbdBLBVw7eI8LzESCOjZV4uSMvlDxK2zOcSi-Pw_atSGC87BYpSvhOAFBmPLjo4AhE0vaJBlbpb5WcdD7ZcGpVkZXNLGYNwaVmKQhseCYGdCPQGYOdAJl-o3FV1QBetEoBgJ5r8bqRyKmH-wX0wzLl4xDA9E5KMlTzGJ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداها رفتند، خاطره‌ها ماندند؛ بیشتر صداهای خاطره‌ساز دیگر میان ما نیستند
🥺
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665237" target="_blank">📅 12:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665236">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سرپرست وزارت دفاع: توان موشکی و پهپادی ایران غیرقابل‌مذاکره است.
🔹
معاون شهردار تهران: طرح ترافیک در روزهای ۱۳، ۱۴ و ۱۵ تیر لغو می‌شود.
🔹
سازمان هواپیمایی کشور: قیمت بلیت پروازهای اربعین هنوز نهایی نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/665236" target="_blank">📅 12:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665235">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f151079d27.mp4?token=Z47rbIiRxvn4dhtPx3yUq_iYrBmX0Kk5Tmdrd7rqBexNZevITmj772WgdI9MzjYZsYaGuIFVP--oPYSbR3_oCUaVtJBNWZf5HTcOb3ZH1A9t9i3bVx8ifrjqUGdJLdi_ruuIjI7EQb_rZhFCDekrBTn6vphsF83Lni0rWTuPxh9ByvNHamSSCZZqmO5XI2YMGyK6OFttOLjzp7NQenr5i_B1s7ipoWAZHN4aWGhchuyjEykZjsT6jYZ7kBpzyScGcRPL5_vN5GDvPkCbBHmo0O2NUPhZrCj1diaC2YWiyWYM-E_xO5Kh_UX4K-99g5ayyvidG2GHu57IN2CZSBCauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f151079d27.mp4?token=Z47rbIiRxvn4dhtPx3yUq_iYrBmX0Kk5Tmdrd7rqBexNZevITmj772WgdI9MzjYZsYaGuIFVP--oPYSbR3_oCUaVtJBNWZf5HTcOb3ZH1A9t9i3bVx8ifrjqUGdJLdi_ruuIjI7EQb_rZhFCDekrBTn6vphsF83Lni0rWTuPxh9ByvNHamSSCZZqmO5XI2YMGyK6OFttOLjzp7NQenr5i_B1s7ipoWAZHN4aWGhchuyjEykZjsT6jYZ7kBpzyScGcRPL5_vN5GDvPkCbBHmo0O2NUPhZrCj1diaC2YWiyWYM-E_xO5Kh_UX4K-99g5ayyvidG2GHu57IN2CZSBCauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی حرم حضرت معصومه (س) برای آخرین حضور رهبر شهید انقلاب در شهر قم
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665235" target="_blank">📅 12:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665234">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d45a19551.mp4?token=soGIj4xZh1dVYVhqsazTbGkvRG8kCuXfIJ7dJMcya0JLAsPyCWY_ETZDG-n4PTI39StOvnBk7QuHrucXQ7DJf2l2r87wzJPkpsSfBZxdomOB6ovSIDKQBIdSl4Krlv2C8d_Kh2TnGxSaFtXTOwmWmOI2fbylJ9-fDKECgA6Kep1YU3jPUQ_UCsl3HbuYM3wxsxndPM_QVPL2HCgmAcIeHUKfV_sJONSRFN_n6SxpMmWQAeUy5kcKhmUfEQZ4qSh6hB7xAFnftjA1Z0xCzDI-G2nEhggPPsuz0xz_RzHbLimOsbqVBtC3GbpkL4oMySQ20lN2-JfGMnf9ZKtqQxQcJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d45a19551.mp4?token=soGIj4xZh1dVYVhqsazTbGkvRG8kCuXfIJ7dJMcya0JLAsPyCWY_ETZDG-n4PTI39StOvnBk7QuHrucXQ7DJf2l2r87wzJPkpsSfBZxdomOB6ovSIDKQBIdSl4Krlv2C8d_Kh2TnGxSaFtXTOwmWmOI2fbylJ9-fDKECgA6Kep1YU3jPUQ_UCsl3HbuYM3wxsxndPM_QVPL2HCgmAcIeHUKfV_sJONSRFN_n6SxpMmWQAeUy5kcKhmUfEQZ4qSh6hB7xAFnftjA1Z0xCzDI-G2nEhggPPsuz0xz_RzHbLimOsbqVBtC3GbpkL4oMySQ20lN2-JfGMnf9ZKtqQxQcJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
نسل جدید رنگ‌های دیواری در راه است، تحول صنعت ساختمان‌سازی با رنگ‌های فانتا کروم
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/665234" target="_blank">📅 11:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665233">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pApYr7vitQWiEg3-bfA38a2NwIBB90br_FhXkAPe8eRgWZ6O4OdVpv8_ryWjqzkSU8BIA6Z3N_FtgppgZYgt-Rnn4157wyC4EWcHIddhirSycX7EIKmJCOX0rxJrjmHgMHXVer5N5uIBoon6C5qdf3ZiPeu8OeRA2Lfu52UqeEp_qLw6YlIH7shwBverbBYmjMFauOyC7SnEqvL-qsrn4AMAGpCaJ4xk1DTBfVdif2r5HlCMaNtYWR1zROcPXeNFXhnyt7WMoqQUI03BVt326mSSwD0RjvYqd6RmzPBZ-nDBtg4U1ZyP6W5UvkQEpboNUqNSEGnsryaKSuxt-pn55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: پرونده انتقام خون‌پاک خامنه‌ای کبیر و شهدای مظلوم ایران باز است وآمرین و عاملین این جنایت به سزایشان خواهند رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/665233" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665232">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoZ-7_ZinXu72irNtReeRRRvSJvCmOnWIgJNMA9LAR3V--lVs_rOliHkXEuEUlP-iXWNPSJSpxZPAURtEdf8MYEitsTg5jhbHnd4FxdsHjI82aFJWyaFDxhoyMQBBBVipiPHb4j1YV6-r3nTWzGhwdq5ZZKzBBQksi_5agD_UMrXuBeJqVoyASzPld0RorwlRQ_9ugxRFy1o9HocF2IwAyrbKxcOKCAkW8RbfrDDmZIOVAiV7nZs6_K-Sh5NCDBqjhSxS4LNOZyAFdX9k8X2nHirdtXGiIL-EvbJBSRRGw3esCM-c7CaFsbOhCuJaOMOzZSkAJo7p96PdD6Z1GLWqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران در دو هفته ۴۰ میلیون بشکه نفت فروخت
سی‌ان‌بی‌سی:
🔹
ایران از زمان لغو محاصره دریایی توسط آمریکا در دو هفته پیش، بیش از ۴۰ میلیون بشکه نفت خام صادر کرده است. تهران اکنون نفت را با ۲۰ درصد حق بیمه می‌فروشد.
🔹
ایران موافقت کرده که به کشتی‌ها اجازه دهد به مدت ۶۰ روز بدون عوارض از تنگه هرمز عبور کنند، اما اعلام کرد که کنترل اداره این آبراه را حفظ خواهد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/665232" target="_blank">📅 11:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665231">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
واکنش قاسمیان به مقایسه مذاکره با صلح حدیبیه: اول واشنگتن را بگیرید، بعد از بخشش ابوسفیان حرف بزنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665231" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665230">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv3xldZlyXJluv0aC7m9xk3Qu4GykcN_Wen_Torer2uLg8pOSumI5RTHiMllL2sgtq2vy5d4VPEh4uRpG9-3WCk84FYde8vg05btrJNoVFTX1yOl1TTjbc8wW21cicUjIK2htlGGR9nxrXHdFzM28PmXw6yE1m06SnK7KW_exd5zxdI8xOnX9ZTPm0IRAF5Nhkrs2GRgMGcJMHEClxUAYDUrm7rfUz-iXQNykS35u6FAGEei7Ys1267fKn89r2s66uXRqUXHI0ri2kBzxnTOIeM69pobNykVuwEHHP8rp_CPAnSIOl3jS1U023SzvynCvGLiPhQtEhfEr7lh92_Xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت بهشتی کوهستان گرین نهاوند در تابستان
#ایران_زیبا
#اخبار_همدان
در فضای مجازی
👇
@akhbarehamedan</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665230" target="_blank">📅 11:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665229">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اختصاص قطارهای شهری و حومه‌ای برای مراسم تشییع رهبر شهید
مدیرعامل راه‌آهن:
🔹
قطارهای عادی و فوق‌العاده در مسیرهای تهران، قم و مشهد برای مراسم تشییع و عزاداری رهبر شهید ایران اختصاص یافته‌اند.
🔹
قطارهای فوق‌العاده به مقصد تهران، در روزهای دوشنبه و سه‌شنبه قطارهای فوق‌العاده به مقصد قم و در روزهای سه‌شنبه و چهارشنبه قطارهای فوق‌العاده به مقصد مشهد اعزام خواهند شد.
🔹
همچنین برای بازگشت مسافران نیز از روزهای پنجشنبه، جمعه، شنبه و یکشنبه قطارهای فوق‌العاده در نظر گرفته شده است.
🔹
فروش اینترنتی ظرفیت باقی‌مانده قطارها از ساعت ۱۴ امروز آغاز می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/665229" target="_blank">📅 11:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF_9pw5OBEazomwlAbNdNsK9BmwBXYqJ04-skh_RJnppabA1iDn0-s8L1Gsdm6NvESfR6v3K3NEFRMlAb1BfYIpFsl98jkogydYn9qgMtWHwqrYQGE28Wl7mc4NT7yaPhl7gK3xG0rwQ2h6cdVFVtBKK5Kwako7QTVIYcCv6OPfyx2KXVBLhUJFPGTUgjAvzJbLQe1VYBjLfs6C_1D4fwKbDRTqAcSLQNoP0ZSrSTUaoehKFnvQ6tjGCVePrez0Kvv4GD5FYXYt-1-mWl7-bREyZ7IFiirnmTlJ2XfK9UZLpsrWAGOqnWL1rfCjU2aVeBVHYvxdf7RooPYIUVgkKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا پایان سال خودرو چقدر گران‌تر می‌شود؟ پیش‌بینی بازار خودرو تا پایان سال
بر اساس یک سناریوی تحلیلی مبتنی بر شرایط فعلی اقتصاد ایران، روند تورم، وضعیت نقدینگی، کسری بودجه، رشد هزینه‌های تولید و چشم‌انداز بازار خودرو، احتمال وقوع سناریوهای زیر تا پایان سال ۱۴۰۵ برآورد می‌شود:
🔹
افزایش ۱۵ تا ۲۵ درصدی قیمت خودرو: ۱۰٪ احتمال
🔹
افزایش ۴۰ تا ۶۰ درصدی: ۵۵٪ احتمال
🔹
افزایش ۶۰ تا ۹۰ درصدی: ۲۵٪ احتمال
🔹
افزایش بیش از ۹۰ درصدی: ۱۰٪ احتمال
این اعداد چه می‌گویند؟
🔹
حدود ۹۰ درصد احتمال وجود دارد که قیمت خودرو تا پایان سال بیش از ۴۰ درصد نسبت به امروز افزایش پیدا کند.
🔹
محتمل‌ترین سناریو، رشد حدود ۴۰ تا ۶۰ درصدی قیمت‌هاست؛ یعنی اگر این سناریو محقق شود، قیمت خودروهای بازار در اسفندماه می‌تواند به طور متوسط حدود ۵۰ درصد بالاتر از امروز باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665228" target="_blank">📅 11:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
🔹
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌‌کشی و با پارچه پوشیده شده است.
🔹
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ از این‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد. احتمال دارد پیکر مطهر رهبر شهید در رواق دارالمرحمه یا یکی از رواق‌‌های حرم مطهر رضوی آرام گیرد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/665227" target="_blank">📅 11:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665226">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6483a8f64e.mp4?token=vt9kITRHg3GfnqV8X0pA06qrs8n8D6wV9uzxKhONGg5y0qfoGvQ52fUbtArImsctaX1uHdsGPZw6ZkFYOPrZQB2-Auc_OCQwwbKTU579WQEWKXjCB_MBvhAVtqp9i0X2_kW2Egr-iPXKmZHWI2QjBoAm2niJCoZWbGaWIYKWj7gLleOnFtj5GPUaaFbHQczS7Y8jM8OIhUsc8Hf1gpiFZ7L0yJmOX1rB3owFZnNXG3q8avs5UIbQWHIi4Avt-W7JHefa_74klVjA_FrJtEM-z5DqlZ8mtN1Ea9P9yfP2nNzFk3ya6E6r56mo6DR7fx_WYH3PvK4KSD0MgSCKRXWpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6483a8f64e.mp4?token=vt9kITRHg3GfnqV8X0pA06qrs8n8D6wV9uzxKhONGg5y0qfoGvQ52fUbtArImsctaX1uHdsGPZw6ZkFYOPrZQB2-Auc_OCQwwbKTU579WQEWKXjCB_MBvhAVtqp9i0X2_kW2Egr-iPXKmZHWI2QjBoAm2niJCoZWbGaWIYKWj7gLleOnFtj5GPUaaFbHQczS7Y8jM8OIhUsc8Hf1gpiFZ7L0yJmOX1rB3owFZnNXG3q8avs5UIbQWHIi4Avt-W7JHefa_74klVjA_FrJtEM-z5DqlZ8mtN1Ea9P9yfP2nNzFk3ya6E6r56mo6DR7fx_WYH3PvK4KSD0MgSCKRXWpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی سفیر آمریکا در اسرائیل: بدون یهودیان، آمریکا هرگز شکل نمی‌گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665226" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏆
پیروزی کوبنده فرانسه برابر سوئد با درخشش زوج طلایی کیلیان - اولیسه
🇫🇷
3️⃣
🏆
0️⃣
🇸🇪
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/665225" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید   رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/665224" target="_blank">📅 11:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665221">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8b453312.mp4?token=J3o7tOJMAwPW_CQhT79DmrYKmSRJjnNwtx7uHS_7c0M9qGETcnzpaiPVFPnDWDXEFnYQJhrtymjSbAZJgC5gzY8yPi5_7Rds7CpU6enbyJ8mE3Uqz13H9NkyD2Bhlkk364-BL7ePbNFRGI-5I4wIuZDxBOxqsqMMVWxaECOlpy0PoClp3nuhovvEtM4NoaVTKsjObPQYFl42BmT16dpmXFxU-TQ6AshoG2MPAxbnF_FNySCoBYQiY4ELs32zj5IrV78SeeV2htVBw_lDd60Bx722RKgal94V5B4FOqxQrU96rOmsPkBIeCQwr8iXSqxWeuph-jgpsBBulzFATLOqRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8b453312.mp4?token=J3o7tOJMAwPW_CQhT79DmrYKmSRJjnNwtx7uHS_7c0M9qGETcnzpaiPVFPnDWDXEFnYQJhrtymjSbAZJgC5gzY8yPi5_7Rds7CpU6enbyJ8mE3Uqz13H9NkyD2Bhlkk364-BL7ePbNFRGI-5I4wIuZDxBOxqsqMMVWxaECOlpy0PoClp3nuhovvEtM4NoaVTKsjObPQYFl42BmT16dpmXFxU-TQ6AshoG2MPAxbnF_FNySCoBYQiY4ELs32zj5IrV78SeeV2htVBw_lDd60Bx722RKgal94V5B4FOqxQrU96rOmsPkBIeCQwr8iXSqxWeuph-jgpsBBulzFATLOqRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شدیدترین سیل در پایتخت سه میلیونی غنا، آکرا
🔹
گزارش‌هایی از کشته‌شدگان و تعداد زیادی مفقودالاثر منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665221" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665220">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYsuwpNGZE0HPSHbfe48OPEi_ApVG471fPJqu5jzGrL4y-2OEdrY803OfrTTSDtzPN7tGtkMWUT_uFXbf9L5IlMyOEF75OKa7DP18h_zw8KPyqSbz7m1QLV4TAcP7ALSR613hZ0BuTSj_Y1qoO9r-WK3RVP86wEdx3xuSsbaTXz4Ca12c9kMigHincgJiYhiYdE8ptriDadsZxhN0XyRBXGlkWNFHA5IACSVmZ3NmG86wgPHXMpY8lZ5FJ0nsdTWMK69MCv6mbcy3mrX-7MXWBPffpstvqCzLSKiBa42vKE49qexibTMa6TmF-rgCqreSjBQbIn4tGCg10KrxMZ4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوهی عظیم از دوچرخه‌های رها شده و شکسته در چین!
‌‌‎‌‎‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/665220" target="_blank">📅 10:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665219">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حضور مقامات و سران ۴۰ کشور در مراسم وداع و تشییع رهبر شهید انقلاب
سخنگوی مراسم وداع و تشییع رهبر شهید انقلاب:
🔹
در مراسم وداع و تشییع، علاوه بر حضور گسترده مردم، شخصیت‌های سیاسی، فرهنگی، علمی، دینی، دانشگاهی و نخبگان از اقصی نقاط جهان نیز برای ادای احترام به پیکر مطهر رهبر شهید انقلاب در تهران حضور خواهند داشت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/665219" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665218">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzF3oqXrvhvupdlgOYL-DuOCljJVcn3JLlDJD7zTGmJf4Tmy-pETQvOBcQwsfaz54OcZCiSwZC6FMdrxhyGxenUa0Fd9X_dUbrjyD-IKzEAC0lKZ3lMq-2Cns3h_LR7LX42lw9DqO-RbokFl8fD70Cd9vQgrrvygKx054o0IHRMCtXJcyWLlVMb_jVmJMaWtWiYYF4vBwm75tk0qg73t0uFau8JijLgUhEQ4EaRi3NpHcI1iZF_oOWK1d8uzRKfNa9BgRf0dS7r-sE-GU4iFVs132EM8Inb6nJSEMOUtU18jmsjiaFqcnfGyMoAggoeTSww7lpLGvho2_AHqpE6vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرجمعیت‌ترین تشییع جنازه تاریخ کدوم بوده؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/665218" target="_blank">📅 10:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665217">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
جزئیات تعطیلی فرودگاه‌های کشور در ایام مراسم تشییع رهبر شهید انقلاب
رئیس سازمان هواپیمایی کشوری:
🔹
فرودگاه مهرآباد روز جمعه تعطیل است و تنها پروازهای دیپلماتیک و سیاسی انجام می‌شود. فرودگاه امام خمینی در این روز طبق روال عادی فعالیت خواهد کرد.
🔹
دوشنبه آینده آسمان تهران و فضای هوایی فرودگاه‌های مهرآباد و امام خمینی‌ به طور کامل بسته می‌شود و هیچ پروازی انجام نخواهد شد.
🔹
سه‌شنبه فرودگاه مهرآباد به فعالیت عادی بازمی‌گردد، اما فرودگاه امام خمینی به دلیل انتقال پیکر رهبر شهید به عراق همچنان تعطیل خواهد بود.
🔹
هجدهم تیرماه نیز همزمان با مراسم تشییع در مشهد، فضای هوایی این شهر و فرودگاه‌های اقماری آن به طور کامل بسته خواهد شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/665217" target="_blank">📅 10:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665214">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید   رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/665214" target="_blank">📅 10:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید
رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا می‌شود.
🔹
تردد انواع موتورسیکلت از ساعت ۱۲:۰۰ ظهر روز چهارشنبه ۱۰ تیر ۱۴۰۵ تا ساعت ۰۶:۰۰ روز شنبه ۲۰ تیر ۱۴۰۵ در محورهای کرج-چالوس، هراز، فیروزکوه، تهران-سمنان-مشهد و بالعکس ممنوع است.
🔹
تردد کلیه وسایل نقلیه از ساعت ۱۲:۰۰ روز جمعه ۱۲ تیرماه تا ساعت ۰۷:۰۰ روز دوشنبه ۱۵ تیر ۱۴۰۵ در مسیر (جنوب به شمال) محور کرج-چالوس ممنوع خواهد بود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/665213" target="_blank">📅 10:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01586d97c0.mp4?token=g2tNQjD2qEhVqH0OYPdJveezdbfAFgMrbOOLE_UD1pT0BxHaSmWhrvyj2kywouXL_PLVSHN9HMM8qZgIkvfDte1sYANYiTfx4JmQ7FmbVDCW8fAhHSdab0lIM14uKLj0r5t-UjACM3xCkbuzcm7BjHM7b5DUibr-0zee2tvPyUz9KJJogBvH_CRGhBafQKJKFOGNVE1mC-8GKlVHi2ywnNaszlPnAO2oaqrkWf3ydSnYd_MUOsHq6E6fD9U_9AWpf-s30CVkjqYe3ziSEXwmrM8tzzs0WHanMA9o1ef_z1vW5192RRwDun00_ea-b1dt28UwjwxJnpI6aCwRebEMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01586d97c0.mp4?token=g2tNQjD2qEhVqH0OYPdJveezdbfAFgMrbOOLE_UD1pT0BxHaSmWhrvyj2kywouXL_PLVSHN9HMM8qZgIkvfDte1sYANYiTfx4JmQ7FmbVDCW8fAhHSdab0lIM14uKLj0r5t-UjACM3xCkbuzcm7BjHM7b5DUibr-0zee2tvPyUz9KJJogBvH_CRGhBafQKJKFOGNVE1mC-8GKlVHi2ywnNaszlPnAO2oaqrkWf3ydSnYd_MUOsHq6E6fD9U_9AWpf-s30CVkjqYe3ziSEXwmrM8tzzs0WHanMA9o1ef_z1vW5192RRwDun00_ea-b1dt28UwjwxJnpI6aCwRebEMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضهٔ شب تاسوعا| قاجار | ۱۲۵ سال پیش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/665212" target="_blank">📅 10:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b360968015.mp4?token=dJAz49ggbvXioEFl9c9EVnrHj0W5WWz1Zb3RBRGlsE-XMA4AbUnlMDNL-oQ4tot4FKh61jzmwoD1IY2SZj8jTq9a5Ps5SMN4ZncnZfmN0xqKnBilh-h69MEv06CqTACVP41Ob0EZr8Dv69uZpUlx063a38YBm8SvLS523PfsK_YIuzMVtRMJpjyXBJFOEXQjAYzAVGMWbIpS6f9PLYC1oR6FmfcYSc2sL6UD-GUC_8bIejm7BnK2BAE2BR_BeLSTpHJc0gGDWT-ZhPmaiGzcKNyTs5_1OSx9ykTmN2BWKoc1UMJLbF08ipNStelhyU-pZoBwmuQY55NFxEwSzcUoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b360968015.mp4?token=dJAz49ggbvXioEFl9c9EVnrHj0W5WWz1Zb3RBRGlsE-XMA4AbUnlMDNL-oQ4tot4FKh61jzmwoD1IY2SZj8jTq9a5Ps5SMN4ZncnZfmN0xqKnBilh-h69MEv06CqTACVP41Ob0EZr8Dv69uZpUlx063a38YBm8SvLS523PfsK_YIuzMVtRMJpjyXBJFOEXQjAYzAVGMWbIpS6f9PLYC1oR6FmfcYSc2sL6UD-GUC_8bIejm7BnK2BAE2BR_BeLSTpHJc0gGDWT-ZhPmaiGzcKNyTs5_1OSx9ykTmN2BWKoc1UMJLbF08ipNStelhyU-pZoBwmuQY55NFxEwSzcUoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ ثانیه از قاب‌های که دیگر تکرار نمی‌شوند
فقط چند روز مانده تا وداع...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/665209" target="_blank">📅 09:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOeEm-VKqsklAcWQR8mltz6XfiTa1p47VlodA7n4iKRX_AiFXhneIbX12mX6zvMDVwXlLzBfYutiD1f0dwIzh_tp6JYhtK5_Eeqy5VWMZDxTtMUU0ogxGQ8qAgQf9Schzjd3PnPSPK98M_p0Jds1OExVDA_N5v9WD71F8Fjj3-ujh8QvbYrM8x5AnO_q9pc5kB7brDojgiu0ke3aqasjWueJh8d_ElXhdaSbk35whIH5h2iUNml3qFERd2JgwvvtkxSIagmxVy-8eNHQ0NOqLK4460JIcpyWTprevwltfZcnmX2N66roniOweMT-IOJXptbO-lugdFplS1W8NJwCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم ما از میزبانی رهبر شهید
🔹
اقدامات داوطلبانه ساکنان شهرهای میزبان تشییع رهبر شهید برای پذیرایی از زائران و وداع‌کنندگان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/665207" target="_blank">📅 09:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
چه تعداد از هر جاندار روی کره‌ی زمین وجود داره؟
🔹
بیشترین جمعیت متعلق به کدام جاندار است؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/665204" target="_blank">📅 09:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665202">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96f5db9cc.mp4?token=e9Y5f67QO2fPUef4PHLf-VSXVylIz-TApwGsqYWZbEkLBhVNOXoYdQdN1JZvJA7uaK_h6XZqDW-5BVevd9EOepHNMGdEndhLkMXZnZbjRyTljyXJgVZbpn3bj1D9p1gmvaG1v0Glc9J7iBBBTeO-uExdUCUpB2jHXUCN3fjnsC2dZa_evkV1MVbUI3bMRUV8qOjCtJyIll-qEiFYGzac7LQDjIeYV5sj6aN1vG7c5gCNf3p0wfmdL2nu4TXEKrBhmQBdkKq9meul7SnI59fpoz7S1PaXlYnApxiPQbBCVIPGtRBmtA0NRVyRLogf4a19kCyluDYgn5NH3AqdiSj6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96f5db9cc.mp4?token=e9Y5f67QO2fPUef4PHLf-VSXVylIz-TApwGsqYWZbEkLBhVNOXoYdQdN1JZvJA7uaK_h6XZqDW-5BVevd9EOepHNMGdEndhLkMXZnZbjRyTljyXJgVZbpn3bj1D9p1gmvaG1v0Glc9J7iBBBTeO-uExdUCUpB2jHXUCN3fjnsC2dZa_evkV1MVbUI3bMRUV8qOjCtJyIll-qEiFYGzac7LQDjIeYV5sj6aN1vG7c5gCNf3p0wfmdL2nu4TXEKrBhmQBdkKq9meul7SnI59fpoz7S1PaXlYnApxiPQbBCVIPGtRBmtA0NRVyRLogf4a19kCyluDYgn5NH3AqdiSj6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم فرانسه به سوئد توسط امباپه
/
صعود بی‌حرف و حدیث خروس‌ها و تقابل با پاراگوئه در یک‌چهارم
🇫🇷
3️⃣
🏆
0️⃣
🇸🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/665202" target="_blank">📅 09:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665201">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0dd83e1c.mp4?token=sLq2yLZiPRJ6zEE3R88F1pNFk7Zpdv85p-W1NdbLJ9_W8zv2IMmYzAee7BduvVRL8zSXVFoH8gaLDd3VzpLD2so1N0Wv7066Awd5ev-bpkRcSBX6NQhftSv0mtzY8ri97gOyhE1BksqhvvSzUskY2lloEmwnL877MJUlNHLIosgdDJvXqVzg3ftk8Fi_b2KSICmPh4othLVfxTVYWBKme19MK_pSuGiT6yJDnk4kuCX_ZphrvPb7FoeTvcjkbgsMM6asb9OMv62ROQ9Aze5eoyixICQP9UBd9fAp7KTWrH6nBuY1VbYwFIsA6trNtqu7BV1sZDbK4T2fB6_7zc2rLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0dd83e1c.mp4?token=sLq2yLZiPRJ6zEE3R88F1pNFk7Zpdv85p-W1NdbLJ9_W8zv2IMmYzAee7BduvVRL8zSXVFoH8gaLDd3VzpLD2so1N0Wv7066Awd5ev-bpkRcSBX6NQhftSv0mtzY8ri97gOyhE1BksqhvvSzUskY2lloEmwnL877MJUlNHLIosgdDJvXqVzg3ftk8Fi_b2KSICmPh4othLVfxTVYWBKme19MK_pSuGiT6yJDnk4kuCX_ZphrvPb7FoeTvcjkbgsMM6asb9OMv62ROQ9Aze5eoyixICQP9UBd9fAp7KTWrH6nBuY1VbYwFIsA6trNtqu7BV1sZDbK4T2fB6_7zc2rLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به سوئد توسط امباپه
🇫🇷
1️⃣
🏆
0️⃣
🇸🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/665201" target="_blank">📅 09:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665200">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExE-fMHJX78tpFLMPIAXFTIuZpzXK5c3cJ71oiZtRcPMtbz63t3EXyV0VG6izOQ11XTOEKbJoZKH5QdYjR7E1xsEogBaxIlUe5OYc14SQXaYRGEL7cTIJTjSSg2Qs_p4Y6zjUhbUIxoX70CDYSHcxwE2BkVIhcSLw1RqP7piEiJFT4MkGFTHHzPBE4Uy7fdLq7H5S2F3GnE4AdQbqUDeZZ2yj5YGz5a18iSkVxvtfQi-DMphayoLsSn2tBLceKncDw2g04g3ci5cCqDRZ98dHiDf1G3SaTw7WGWsaKCzp5H40UJVg24THXkew_-jW5sk8ATNBrWbUtH4Gb-cVeaU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند پیشنهاد کاربردی برای بدرقه رهبر شهید انقلاب به کاربران فضای مجازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/665200" target="_blank">📅 09:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665199">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سه‌شنبه ۱۶ تیر تهران تعطیل شد
فاطمه مهاجرانی:
🔹
هیات دولت امروز چهارشنبه دهم تیر تصمیم گرفت که به منظور تسهیل خروج عزاداران رهبر شهید انقلاب اسلامی حضرت آیت‌الله خامنه‌ای از تهران، روز سه‌شنبه ۱۶ تیرماه این شهر تعطیل شود.
🔹
براساس این مصوبه، همچنین روز پنجشنبه ۱۸ تیرماه مصادف با آیین خاکسپاری آقای شهید ایران در مشهد مقدس، در سراسر کشور عزای عمومی اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/665199" target="_blank">📅 09:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665198">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z71lPbq1jYCCiyzDSyxIADteUPh_dAIBGRgILnAW1hK3qBCGvB_YnuuVBYDkMnJkLK39ZMKZxZBGDY83zdD6gESKr5bzATjoV45GUffHXY8XZgTwgDZ-ub1YpJs_V0bC3m_5NZDEvxycy-_MWZMLLbVjW5jo1zZyUQpt8eZ74lXTR6E9LzsfsYV1NANBb3_8Rp2iO_50ibWWwAIss3SYS4X32J2C6wij4yxuzexGBIN33gYSoePgQNJpV9Azf8V6zia121qoWfl4VZMjfWm6lHYwSbvxhuBfTT1M9tyzRaGky3dmQDnBfu5du-14E2WOZgpOpqZyiuajP7Fa176hNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه رو اشتباه نخور
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/665198" target="_blank">📅 09:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665197">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
۲۵ هزار میلیارد تومان مالیات بر ارزش افزوده به صادرکنندگان و تولیدکنندگان پس داده شد؛ رشد چهار برابری استردادِ مالیات بر ارزش افزوده در صد روز نخست ۱۴۰۵
‌
🔹
جدیدترین آمار و ارقام مربوط به استرداد مالیات بر ارزش افزوده به مودیان نشان می‏‌دهد که میزان مالیات بر ارزش افزوده مستردشده به مودیان با رشدی ۴ برابری از ۶ هزار میلیارد تومان در صد روز نخست سال ۱۴٠۴ به بیش از ۲۵ هزار میلیارد تومان در صد روز نخست سال ۱۴٠۵ رسیده است. رشد ۴ برابری استرداد مالیات و عوارض ارزش افزوده به صادرکنندگان در حالی صورت می گیرد که مجموع درآمدهای مالیاتی در این مدت ۳۵ درصد در مقایسه با دوره مشابه سال گذشته رشد داشته است.
🔹
سازمان امور مالیاتی کشور همواره تلاش کرده است در کنار تامین درآمدهای مالیاتی مورد نیاز دولت، تسهیل فعالیت‏‌های اقتصادی و حمایت از تولید را به عنوان یکی از مهمترین راهبردهای خود دنبال کند. رشد عملکرد سازمان در حوزه استرداد مالیات بر ارزش افزوده محصول این نگاه راهبردی است که تامین پایدار درآمدهای دولت در کنار اقدامات حمایت‌گرانه از فعالان اقتصادی می‌‏تواند زمینه‏‌ساز تامین نقدینگی واحدهای اقتصادی، تقویت سرمایه در گردش بنگاه‌‏ها، ارتقای رضایت‏‌مندی مودیان و در نهایت رونق اقتصادی کشور شود.
🔹
استرداد مالیات بر ارزش افزوده به فعالان اقتصادی و بویژه به صادرکنندگان از جمله ابزارهای حاکمیتی برای حمایت از صادرکنندگان، تسهیل فعالیت‌های اقتصادی و بازگرداندن منابع به چرخه تولید است. بر اساس قانون مالیات بر ارزش افزوده، برخی فعالیت‌های اقتصادی بویژه صادرات کالا به خارج از کشور از جمله مهمترین فعالیت هایی است که از مالیات بر ارزش معاف است و مالیات و عوارضی که مودیانِ مشمول بابت خرید نهاده‌ها پرداخته‌اند با رعایت مقررات به آنها مسترد می‌شود.
🔹
همچنین در مواردی که اعتبار مالیاتی مودی نزد سازمان امور مالیاتی کشور بیش از مالیات و عوارض پرداخت ‏شده باشد و مودی درخواست کند مبلغ مازاد به وی مسترد گردد، سازمان امور مالیاتی نسبت به استرداد مبلغ مازاد به وی اقدام می‏‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/665197" target="_blank">📅 09:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665192">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qe8wjm1YPwYZF_9iDOmbvufpVfr9RL6tpkFUXMiCJpLhs5qYqCJY1VlTZ-58EI0W4a8Xtm8uficVL1jTQ8mL-Amx6UCJjtTqrefVoTlN3vpbAD2X1wTZ1BLKE3s4x7SEEXCvX4CsGSKaKdWQPLtKKcMxGNeJsBfEGo68jnCirv45NL8t6MoNuKDdQUD13hUvd4P6WNxkHmG383w9plprXVkxaZfh8GGSkdls1nJr75UCEq1R39OfIqtnIlk3FJ3cbW7Ot6pJO_6Ggk5_z9POdv1Sl1GnUuhpQPCI-kMFYYHgo5BeZZr2cKCVmkLDxYp7HI4e2jZUy3OBBnWRvPjagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErQ-V1P0JKyD7_eXVW_6kbu0TOMtAc_TLThgvsymVEYd4oa5aKeuYoHkX7-M7h4umCmEAJtKBNntknlAGyai6XpbGc0YfQsEH9PyFfk1UVvdMXSVgZAsT_SJdExbydKU-wxMhUkNNwSfesrOLWq0lT-nm7Fg7vyRc8dVArIWZQgXFwPJHjo8niXAXvdPy_N1QZKHIcMbxi9MDyTChEZYMn_19z9Q7GiIEkesxLSAKFeru3SAnEpHwaihZSUA-6S4zhUeCZAhlImHkRqnOIfSdJlA5ljtWTNW4YJqrlBywVWpysiKTrU4zLjdp_jb6MxhxDasx7V7O4HX0D7_CkNCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4gxGABB_6GpjlTsIE0PfjVcxYmxRwEOboEVf3pbRvhSrBc4wASBtoMTfKlNYP-RTLN1ONNrCA28bFOhsE6G-_3YbwQbKLKxGBbKfLH2phe5bxju6i0ttxZaX9x1uqQUxhGEk6wU30zDKMGxO9YKZiZSXWLvf1ohky1rahiJd6MyHFfiA9oXOYU5eLCX1KmauVfyTVzcELJgEcC9tYScK1kMj-_MfGZvBnooXtzNu0-G8vFizdLomkn62YzrbDIIUQ5GfiyLqmG4DW94vteMwUD1v7oDgCjpyr2W-g2u3-S6vRGVc7EAVnnqHkAV1PRGzY5B1tHycZXLgEaA7A12fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f47ab637.mp4?token=Wc2Xeqt9DJ1ZHUeCHxwOFM6TbwMKNitSE2UfkHEBMQssIGJ8_-JIqjvd-PRVx1mLyUT7qmz__6q9JAhCTxcVC8PB9PyFhEJIHXUDF8B01EjV4xrFLZr2ccy9zeT4le_uKIREo7-AGP8ap61heAqJ_sEIV7B_2X4hI6RjzYnspOrYy_dhQHQCDCqvTEUYKz-RA6ffdAjgew3V-WnZc9OLZE2fswW_3GlqIMZDqwn5htvNaDHlUmt_nJ5MU7VNUsac5-8W6BysExBJX26pLRVLDnQ13qh1qQmbMORsTYyd89UxnaMNTNbz44v5de7YtLk2QkNi1oD4hkiVvxAGI8LpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f47ab637.mp4?token=Wc2Xeqt9DJ1ZHUeCHxwOFM6TbwMKNitSE2UfkHEBMQssIGJ8_-JIqjvd-PRVx1mLyUT7qmz__6q9JAhCTxcVC8PB9PyFhEJIHXUDF8B01EjV4xrFLZr2ccy9zeT4le_uKIREo7-AGP8ap61heAqJ_sEIV7B_2X4hI6RjzYnspOrYy_dhQHQCDCqvTEUYKz-RA6ffdAjgew3V-WnZc9OLZE2fswW_3GlqIMZDqwn5htvNaDHlUmt_nJ5MU7VNUsac5-8W6BysExBJX26pLRVLDnQ13qh1qQmbMORsTYyd89UxnaMNTNbz44v5de7YtLk2QkNi1oD4hkiVvxAGI8LpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان سرخ ونزوئلا در پی زمین‌لرزه‌های اخیر
🔹
تصاویر منتشرشده از پایتخت ونزوئلا، آسمانی با رنگ سرخ و نارنجی پررنگ را در زمان غروب خورشید نشان می‌دهد. بر اساس گزارش‌های منتشرشده، گردوغبار برخاسته از زمین در پی زمین‌لرزه‌های اخیر با پراکنده کردن نور خورشید این منظره غیرمعمول را بر فراز آسمان کاراکاس ایجاد کرده است./فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/665192" target="_blank">📅 09:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665191">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌شش | میرمهنا</div>
  <div class="tg-doc-extra">میرمهنا بندری</div>
</div>
<a href="https://t.me/akhbarefori/665191" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
♦️
میرمهنای بندری (مزیتِ چابکی)
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «جنگ‌های نامتقارن در بازار»، «سرعت در برابر سرمایه» و کالبدشکافیِ «سندرم سقوطِ مدیرانِ تندخو» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/665191" target="_blank">📅 08:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665190">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22dd9a174.mp4?token=sGK5N06jG91lmqqBs7wbeIpwrtwad7BrvnGE-eoUeb8ngazOzhHHyT84FR_ZXbhSp5AXEop2R-gTLPwYAqZF4W_5tFW5nthmumeKK1qbygBua98s2JogEmRGFSbLB8IbO8vgrPaezSm-gCJ4IcnoG0eyTWg1IXMFvWjuU5HV12zOku7ZsmPJo2JYG460YyoAxCknG4pVZERTSI_2G03jQ18pCSUfW9Y4yiAEUnvkzqRiELX3eELdRvTSUFVvcq6shz602nTUjsT0B277jcjCvqCfZyJ9BSnhE8wYq0SgxhEKLSKQ9WAGkJdRoxISDYfBy7nOAYf43K3V4Mf0HoUsPaiL7nPC08spg-0-fpNg05KDXvu_MhLnhT7XActEP-14iJ-CYTgRN2k4lqYClt6tQs2HVmW_7-p8scZnpWNn-VujPACcgauvF9ArV8aEuSIkSnFKhroHbuINbqpdiNXcPX_SOK8wJKJFaKewofClogPMVffciKPzlky4vpXoRNA3LIPvVmwB54SuK2uADEwsqRjAhHSgdJ07fuIsY36GX8YTq2HsaqJXYuTpfJA3IpfTCwIcWLd0e0pkaGNC9TrB6zPPpKDiqgZJA_frcah7NRCWjUAvKVKpUJxFmxpshv3grilMAmXDCAlp1eqi_vsphTLYhjHvG_o74KMnhh7gHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22dd9a174.mp4?token=sGK5N06jG91lmqqBs7wbeIpwrtwad7BrvnGE-eoUeb8ngazOzhHHyT84FR_ZXbhSp5AXEop2R-gTLPwYAqZF4W_5tFW5nthmumeKK1qbygBua98s2JogEmRGFSbLB8IbO8vgrPaezSm-gCJ4IcnoG0eyTWg1IXMFvWjuU5HV12zOku7ZsmPJo2JYG460YyoAxCknG4pVZERTSI_2G03jQ18pCSUfW9Y4yiAEUnvkzqRiELX3eELdRvTSUFVvcq6shz602nTUjsT0B277jcjCvqCfZyJ9BSnhE8wYq0SgxhEKLSKQ9WAGkJdRoxISDYfBy7nOAYf43K3V4Mf0HoUsPaiL7nPC08spg-0-fpNg05KDXvu_MhLnhT7XActEP-14iJ-CYTgRN2k4lqYClt6tQs2HVmW_7-p8scZnpWNn-VujPACcgauvF9ArV8aEuSIkSnFKhroHbuINbqpdiNXcPX_SOK8wJKJFaKewofClogPMVffciKPzlky4vpXoRNA3LIPvVmwB54SuK2uADEwsqRjAhHSgdJ07fuIsY36GX8YTq2HsaqJXYuTpfJA3IpfTCwIcWLd0e0pkaGNC9TrB6zPPpKDiqgZJA_frcah7NRCWjUAvKVKpUJxFmxpshv3grilMAmXDCAlp1eqi_vsphTLYhjHvG_o74KMnhh7gHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میرمهنا بندری،
قصه بازپس گیری جزیره خارک
#پادکست_کافئین
| فصل‌دو،قسمت‌ششم
☕️
🔹
چریکِ دریایی که نشان داد چطور یک ساختارِ کوچک، باریک و پر سرعت، می‌تواند با حذفِ مزیتِ رقابتیِ رقیب، مغرورترین و سرمایه‌دارترین غول‌هایِ بین‌المللی را به زانو درآورد.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://aparat.com/v/xmlax4n
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/665190" target="_blank">📅 08:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665180">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84fa43fc.mp4?token=XZ-WZM12G3XUS22tyo9FEdIX2AEBaVTg7dQYtxlo4-EE_u01bJ11jdSDe_PGuJ7UqeBLT-UBEa2SOLV9FNV8cLsuMnBvUx9suyAn5VG4GnUKcke3WlUAa0Rb4tf8569anR5DGfyANB_wZYsRDTUPaZfPA5uacI4gwzcuYpohFgFG_34YAVhqA1gg9ecPW57W_9Gidc6-osyUucY9mQlpUuiVHI2G08M85lhN7CD_wFaHvhfHePTyDu8KE_kFb77bCG34GD1oWMtjdzoSG-Rzih59voGF6oWzkSQfeYjv0oqnCrCv6-mBFRaTeizFHk42V_AJd9U5XjABefZe9WlEEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84fa43fc.mp4?token=XZ-WZM12G3XUS22tyo9FEdIX2AEBaVTg7dQYtxlo4-EE_u01bJ11jdSDe_PGuJ7UqeBLT-UBEa2SOLV9FNV8cLsuMnBvUx9suyAn5VG4GnUKcke3WlUAa0Rb4tf8569anR5DGfyANB_wZYsRDTUPaZfPA5uacI4gwzcuYpohFgFG_34YAVhqA1gg9ecPW57W_9Gidc6-osyUucY9mQlpUuiVHI2G08M85lhN7CD_wFaHvhfHePTyDu8KE_kFb77bCG34GD1oWMtjdzoSG-Rzih59voGF6oWzkSQfeYjv0oqnCrCv6-mBFRaTeizFHk42V_AJd9U5XjABefZe9WlEEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب کنترل‌شده ساختمان ۱۶ طبقه آسیب‌دیده در جنوب ترکیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/665180" target="_blank">📅 08:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665177">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ed4e62aa.mp4?token=lcwUJKXIoMuRoooqfhSccZKAaLIFl3GHvenEVDYqbBrDsyzg2vKcpBUNqvhkwQemxbK2L-CkP-p0jDPSrM5wFpZfVyNyqdUR0vv2i7LM5T-mC0l6zn24O1TRVOvtzJ01iS7sZiUOTm3vutIKJKBdxKLD7NbwzJGe2oKJ0MWN5HWHv6xe9rp2zduPXRXixGmi0ShMqybf53IfdIV3qcS5fwkxa3kG4q11_XAggh_zFIr6EayAa1isTxry9G7aTHIPu1k0hgI_6Qh6X2ifs7HYBfJJrNTRmeV_5fE9ZZ5W79iJ2mKoGLKVL6Q4giY6lq_f9R1j1cHLZO7_ok1QSr35HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ed4e62aa.mp4?token=lcwUJKXIoMuRoooqfhSccZKAaLIFl3GHvenEVDYqbBrDsyzg2vKcpBUNqvhkwQemxbK2L-CkP-p0jDPSrM5wFpZfVyNyqdUR0vv2i7LM5T-mC0l6zn24O1TRVOvtzJ01iS7sZiUOTm3vutIKJKBdxKLD7NbwzJGe2oKJ0MWN5HWHv6xe9rp2zduPXRXixGmi0ShMqybf53IfdIV3qcS5fwkxa3kG4q11_XAggh_zFIr6EayAa1isTxry9G7aTHIPu1k0hgI_6Qh6X2ifs7HYBfJJrNTRmeV_5fE9ZZ5W79iJ2mKoGLKVL6Q4giY6lq_f9R1j1cHLZO7_ok1QSr35HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرمای بی‌سابقه در آلمان؛ خیابان‌های برلین را با آب خنک می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/665177" target="_blank">📅 08:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665174">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ff8a5c13.mp4?token=rnnKkEohLgGgTNPULr8FK0XuSFMwDYyMWZ9i1XkRMrvrCegirMKYNdPg8jbKHGeSURWSMrQtJtUu1p6zeLMN-ydAa06rAOrywpOHmWvnGAIrAqKTXr-N0b3nvvXkkUWcqnjq0i4AxAIuGWAiHhp758QQMRj4j5slrbbiWMO-jmfgr2FUkRPQWjJMDhtMmvraj4tI3PfqWv0DUm8hk_eHPevHqt6ZFfNifh52y9IMctRMiXSdgl_PJPdmQC4P2flUZ0sX47skkf1oEAJaMBD6uKPwDdpyHINhpSzeWJlISkB1nlXAGnWs0ai4Nk4OCd8kqoCvJC5raZBV5maBZfon1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ff8a5c13.mp4?token=rnnKkEohLgGgTNPULr8FK0XuSFMwDYyMWZ9i1XkRMrvrCegirMKYNdPg8jbKHGeSURWSMrQtJtUu1p6zeLMN-ydAa06rAOrywpOHmWvnGAIrAqKTXr-N0b3nvvXkkUWcqnjq0i4AxAIuGWAiHhp758QQMRj4j5slrbbiWMO-jmfgr2FUkRPQWjJMDhtMmvraj4tI3PfqWv0DUm8hk_eHPevHqt6ZFfNifh52y9IMctRMiXSdgl_PJPdmQC4P2flUZ0sX47skkf1oEAJaMBD6uKPwDdpyHINhpSzeWJlISkB1nlXAGnWs0ai4Nk4OCd8kqoCvJC5raZBV5maBZfon1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی منتشر شده از خالد مشعل درباره «شهادت سید مجتبی خامنه‌ای، رهبر معظم انقلاب» جعلی است
🔹
کلیپ منتسب به این سخنرانی که در فضای مجازی دست‌به‌دست شده، با استفاده از هوش مصنوعی دستکاری و تولید شده و واقعیت ندارد. بررسی‌ها نشان می‌دهد این ویدیو با هدف القای انگاره‌های نادرست درباره وضعیت رهبر معظم انقلاب منتشر شده است.
🔹
ابزارهای جدید هوش مصنوعی امکان تولید ویدیوهایی با شباهت بالا به واقعیت را فراهم کرده‌اند؛ به‌گونه‌ای که ممکن است مخاطب عادی را دچار خطا کند. ویدیوی مورد اشاره نیز در همین چارچوب، بخشی از جریان انتشار محتوای جعلی و عملیات رسانه‌ای در بستر شبکه‌های اجتماعی ارزیابی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/665174" target="_blank">📅 08:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665171">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aedbee200.mp4?token=OrEk8xwhMzN37fbyvUFAnjW1vjMj5giJOMGSwShZPAszbQvPTB7RJXLQU6jGSAfuEoRY8M1SLVPmIvSAXth_Zbmiy3k35CR2npszTQgaOXLKytbHEyp02DeacpVSOIOJ93epYMtiLJCqv71wmRVwwpwsEJp1pd9OSOuDbJ-_NPi4r1lUURbY0QelbMAuuTpvpUhgPkXAuCsf6a27upy565IGnSSjt5BgpPEbGNhbF5rpJffVA2a2JOhr10WOl-qRLzRfugYf-9EELEhOYIw4VN-ON0bjmIHUmcUeaPXXso_A7ti5dSIbyCvh94MxJEV2KId9_2zKFRI8GV-x9vid0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aedbee200.mp4?token=OrEk8xwhMzN37fbyvUFAnjW1vjMj5giJOMGSwShZPAszbQvPTB7RJXLQU6jGSAfuEoRY8M1SLVPmIvSAXth_Zbmiy3k35CR2npszTQgaOXLKytbHEyp02DeacpVSOIOJ93epYMtiLJCqv71wmRVwwpwsEJp1pd9OSOuDbJ-_NPi4r1lUURbY0QelbMAuuTpvpUhgPkXAuCsf6a27upy565IGnSSjt5BgpPEbGNhbF5rpJffVA2a2JOhr10WOl-qRLzRfugYf-9EELEhOYIw4VN-ON0bjmIHUmcUeaPXXso_A7ti5dSIbyCvh94MxJEV2KId9_2zKFRI8GV-x9vid0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر میخوای بدون خوردن قهوه صبحگاهی، کلی انرژی بگیری و تمام روز شارژ باشی، این فیلم رو از دست نده
😃
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/665171" target="_blank">📅 08:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665169">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwfPKTxs2lUFXq0hWfzXWs5FnfwZw9NRFyOztnuBjOelU3AxP0oL8JW8Hh3eH9ZwlBNa8zD7Rh6tSRU-mWcaczRzwwKm7gFfo7zTNE65YwniTn-NCGkSZqYuBB907u9gVs9wj0zBFbc0P_bvISGvJVgO9wplhQnGzpnu7k0lsjYlq6c4ju6E7Kpu-WWOs1AOyKZs04_Bnx_vPOzeJGMvayi6txksv7TU4uFyf07IgfbBv9C6nmb7EYfZE6Cxhe_ztHZ9Fa0JhZbIEFXybyRpGcfO3AGMje8fyuUTXBjlc-JLRwkeiyRgHOQ0_kJMeiw3IeWMygZjYyAvRoDerbxsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدیدترین بروزرسانی نمودار مرحله حذفی جام جهانی ۲٠۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/665169" target="_blank">📅 07:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665165">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StyLVfkVWUZyDY2Td-Yvo-gQ5RY38vVGFE4dqQ7mmycRkqd27RknEgrb0dtSGJY3NkQZcKuJJVdZr99tS84tcsMEA6ahoE8vhwin8GZbbrrq5PnK_8J2dVmMD2kU6yu1UgsCBjBwAr5NwzO7b6r4hALzAnSUBtPKagLJ68d6ryGVybz_YED5T2PSTHm9xekbKBjPo8db2mH3OVnx9SSk4K0zTLWCe-uNPL4faOPdF_Jrsr2urdVVIWb0jKVVzbWiZ00Fy1gxFcWq9mMpyhtnGg1kICyoW9_yLUlEIBSJzBnv2Yqj5m2DKQaG87XdL7KoUMphRBFxj6H7xEAZ3j5TJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۰ تیر ماه
۱۶ محرم ۱۴۴۸
۱ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/665165" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665164">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0riwx0AhSVM1IrEpJugjgW8MomccLkMt1x7HM8qA2VR8aMKAhO5ZqsNEhXcUNIrWQPkBJgzJy2Vp8YM2NOIlBJ9s0-dikfBhSLQE8LadWr-HnmKOAN9u75T2-A2YFPhzmdCtKVR3uzh3WCeumvCv3yBYYfbTmu0NfeL684l2p5LntrlI_rkxO_wsN7ix-cgdwi5QT8eup8DrRMQ51zRSvYX6X1tat7NBPxdClJj4i6yZeYdtSURv6xn6XL4Mm-9CeeLxJwhER5ikkWCvGm5hsVBus8hWj9J4dX6i73n9xJNIsN0A5VWAVLtdBiORsL-kbHHCQbK7oU51DOYsxoAbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
طلای آنلاین، بدون دردسر
خرید و فروش طلا دیگر نیازی به نگهداری فیزیکی و دغدغه‌های همیشگی آن ندارد.
سرمایه‌گذاری روی طلا، ساده‌تر و در دسترس‌تر از همیشه.
🔰
خرید و فروش آنلاین طلا
🔰
بدون دغدغه نگهداری فیزیکی
🔰
شروع سرمایه‌گذاری از مبالغ کم
👈
برای دریافت اطلاعات بیشتر کلیک کنید
📄
#طلای_آنلاین
#سرمایه_گذاری
#کارینکس
💎
با ما همراه باشید
اینستاگرام کارینکس
|
لینکدین
|
تلگرام
|
وبسایت
|
اینستاگرام آکادمی</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/akhbarefori/665164" target="_blank">📅 01:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665162">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9789db7080.mp4?token=pRLVfv6KvZvBU5JyeYtxCLie1DWIoWsdQQnKGS0VniYlgj82Zv3zfultcMPk9QORHjaZ8Sopgsm-LG3EF54is1W1lvLwuJYTFIaB3Vkn5flVQwz1zgCYoxwlyEEStSsdUzPYUBFKSv1svPqcv_Ydee1HkPeQwUXedqs_bwPOl2J-bV-4Z8oBcu_aEH8LZo810EHoTxYy0ANb9azIgxiIPebrT8_Pw-r633wk2TiO3qN6ht3OtEkOCErP4I6D0IBvFTLWNU7PWL9CP_KkVfKk4T6G3iUPnQw74X-qZfLXPf2WHmGSoqOW15wb1S3OdSnofY58KwtPTuBJOIEsfsqUhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9789db7080.mp4?token=pRLVfv6KvZvBU5JyeYtxCLie1DWIoWsdQQnKGS0VniYlgj82Zv3zfultcMPk9QORHjaZ8Sopgsm-LG3EF54is1W1lvLwuJYTFIaB3Vkn5flVQwz1zgCYoxwlyEEStSsdUzPYUBFKSv1svPqcv_Ydee1HkPeQwUXedqs_bwPOl2J-bV-4Z8oBcu_aEH8LZo810EHoTxYy0ANb9azIgxiIPebrT8_Pw-r633wk2TiO3qN6ht3OtEkOCErP4I6D0IBvFTLWNU7PWL9CP_KkVfKk4T6G3iUPnQw74X-qZfLXPf2WHmGSoqOW15wb1S3OdSnofY58KwtPTuBJOIEsfsqUhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به سوئد توسط امباپه
🇫🇷
1️⃣
🏆
0️⃣
🇸🇪
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/akhbarefori/665162" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665161">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f4d30836a.mp4?token=JOYKMSbd0AlCa-ijNsdhN_6bGGvvPeljrdoUqwD05tR_WnAoP0lDvRZeB6-ftnVcJTV8TZp8WMQmEGqQSWPt_bVN6370v6t5MZLuPYQ12-6jronVSneJOWP7T_xvrksErSWnbwXYOzpRmlty-SJAD9DdRtxH07funOFwBzwgkWLqNSpirulOjtetHMOGrLxffig1Xn9L_N6nPyX6s27lh0dfTg-Qf9bqWZkQqcZrfAqvHhvQY9a5WByfllXmMSFPzGiDhX026IgdkR57w0XkMkrxHTVL697qhitiD5fB2kr_ZKy4jewbNgzWFAtae53ReLAUyn84qxpgzOV7x7kE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f4d30836a.mp4?token=JOYKMSbd0AlCa-ijNsdhN_6bGGvvPeljrdoUqwD05tR_WnAoP0lDvRZeB6-ftnVcJTV8TZp8WMQmEGqQSWPt_bVN6370v6t5MZLuPYQ12-6jronVSneJOWP7T_xvrksErSWnbwXYOzpRmlty-SJAD9DdRtxH07funOFwBzwgkWLqNSpirulOjtetHMOGrLxffig1Xn9L_N6nPyX6s27lh0dfTg-Qf9bqWZkQqcZrfAqvHhvQY9a5WByfllXmMSFPzGiDhX026IgdkR57w0XkMkrxHTVL697qhitiD5fB2kr_ZKy4jewbNgzWFAtae53ReLAUyn84qxpgzOV7x7kE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایتکار افراطی اسرائیل: آماده‌ایم شمال غزه را غصب کنیم، شهرک‌های صهیونیستی بسازیم! فقط نتانیاهو بگوید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/akhbarefori/665161" target="_blank">📅 01:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665160">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
صداوسیما با قطع برنامه گزارش قالیباف درباره اجرای بندهای تفاهم، به‌جای فراهم کردن بستر پاسخ‌گویی، مانع آن شد   روزنامه خراسان:
🔹
قالیباف اگر سکوت کند، متهم می‌شود به پنهان‌کاری، اگر بخواهد گزارش دهد، صداوسیما ترمز پخش را می‌کشد. صداوسیما باید روشن بگوید،…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/akhbarefori/665160" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665159">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آستان حضرت عبدالعظیم(ع): حرم از ۱۱ تا ۱۵ تیر شبانه‌روزی پذیرای زائران است.
🔹
استاندار تهران: تهران از نظر امنیتی در وضعیت بسیار مطلوبی قرار دارد.
🔹
وزیر پیشین رژیم صهیونیستی: الجولانی تروریست کت‌وشلواری است!
🔹
رونالد کومان از سرمربیگری تیم ملی هلند استعفا داد
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/665159" target="_blank">📅 00:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665157">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
عصبانیت صداوسیما از افشاگری قالیباف درمورد توافق خاص دولت قبل با آمریکا
🔹
صداوسیما زمانی مصاحبه قالیباف را قطع کرد که او در حال اشاره به توافق ناکام با آمریکا برای انتقال ۶ میلیارد دلار پول ایران از کره به قطر برای مصارف بشردوستانه (غذا و دارو) بود.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/akhbarefori/665157" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665156">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gh7FttZ1pCCXrn2zFq9pradg-QJRjh63zIALo9LnJEiAqsTu3M0M-_ujgHNjpP_gnMLOnLd3z-phYqi7N_ljZ2GFqh60KzEAmwn3qGkuSAq4XnSdITNtwBxFvf6toliBMmMRxE7CdfzHIK_3k-WTNUdU9Nxat8i4yJYFjPB59mTM0vxdRd0UvkdapqooQpKhm-q-2fJiZZJpM3wCU_T9oY78pHl8WKmWaERWPeGm18wGPeZTX5O7SIiWeWYyFRJGkAWKX-M_Ikc5NgD_lQs9YWWnjikvyUzsTGcoys_GuI1IoiMD6cfx3MW3HNYTcMEb8DWeZKk9EBncnT3GODw2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر امام شهیدمان تا کنون نه به خاک سپرده شده و نه به ودیعه دفن شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/665156" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
