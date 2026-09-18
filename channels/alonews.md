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
<img src="https://cdn4.telesco.pe/file/P51VLA4qgQyjtRxaVuHC1fmxf2ysBx0m8tIDEcC9uGD0Q_-4blU9TISMfK7KT54DfBTshgea86UDJlh0RNEdZw8WAz0KS7ibSc7MJwiWhpjnm8mQQp7whHO5AGRvX7MlrV_UEi76NoxO7P-DGFF3PjGSu2i3-C-j5gWCyybGBkYZU2YBP_VpZzrvgDYSkwSbfkSK27OU03COijcI-9asCbFtF26Jp64N5uakODyptAwBzX52wHm5iVDfkaLdzWuu230H6IOeIdxh5CqlrLVETzjYcIhR4szb3WRSrQBlPDmssYL8GH_Bw3FfJP1L1EmxZ2ZLWwSOYtDGnOa5pgQSkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 22:49:51</div>
<hr>

<div class="tg-post" id="msg-148098">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlKic8XFgqg_QEZex0ACIDKojoatL1of-g3QATGDKZtr3NH_iOzDPvUmJvwYn7sSZB8wCBpvyWTGmNfHooC8Oj4OgT4sWSgi8W0bWLG3RsWdq4KCr1sSVlmsokvaQDHVc4eyTTsQw_NwkRDQDe5lRobG8lNubCyudI-M8Sy0ebM6_2hUXV90Evj3blm2z8Ibia5YawQfO85iHC0Nj3PfPFfmV4wmLwatX2zVik2BGaBtfZYmMS_o3c8vdht7v5CNutBnYkuMW9juX11xDFAFcCtdGSIkFsLiZcqAhjjw1hLZMzMj-Pn1K8BTMb3CMA4TuIaecIy3A6ApH-rvop-_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / رئیس جمهور ترامپ اعلام کرد که کانال‌های CNN، MSNBC و نشریه Politico از این لحظه به بعد از ورود به کاخ سفید منع می‌شوند. او این رسانه‌ها را به انتشار مکرر "اخبار دروغ" متهم کرد.
🔴
او گفت که سازمان‌های رسانه‌ای نباید بتوانند به طور مکرر آنچه را که او "خرافات و دروغ" درباره دولت خود یا ایالات متحده می‌داند، منتشر کنند، و هشدار داد که "سایر رسانه‌های خبری منتشرکننده اخبار دروغ" نیز ممکن است با اقدامات مشابهی روبرو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/148098" target="_blank">📅 22:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148097">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بیت کوین منفجر میشه
‼️
‼️
‼️
اگه توام نمیدونی بخری یا نه حتما ببین
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148097" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148096">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfgaE7mahcRXp7EUZvLy4fB248d6Ncpf_XaYXO_j1mwHzHtHgpAx2N-KlCY_lY3ZI5tIYqSQJr1nbXY7IDk6SEhHc6uq8aP0lwNDz0jmW5BhQL_U-lSl7j1j55d9PvRmWpV1x5E92uOW_ZnEweW2IEELmUeK414_UDnag3PPVvtP-r6qjGNJi7o75kB4pEzvPzMLezroc72u0umhec-u4ppiasapl71Hi1z9FpBtXoUsMQ9A8gberlW9sXxEy8YGr0fITGoh-mxbV41SIQiyJNhFJ3Ezos2Pq-e7i1lOPuPQAYeUXAIZ3TyFpsHFpTfD9EWF_G2OVMVqK5wcZYl6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حدود ۳۰ دقیقه پیش، دست‌کم چهار موشک کروز ضدکشتی از منطقه سیریک در جنوب ایران شلیک شد.
‏
🔴
صدای چندین انفجار از سمت تنگه هرمز شنیده شد؛ جایی که پیش‌تر در همین روز، دو نفتکش هدف قرار گرفته بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/148096" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148095">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پوتین: روسیه هیچ برنامه تهاجمی علیه اروپا ندارد و آماده همکاری و احیای روابط با همسایگان اروپایی خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/148095" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148094">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOi5DfuYlEvjsxkoqU4URnUg5BTQXpK3RiAbqtole0JuAEYwfpOAUfFK5ELB6vPLo6TN9CNcCViM273d6F0TlWyTM0zPnNzrgWuQNDbggNGPvxplHRpZ570KPN6-wpsCpdyIeKieI-fYWIILutgC3D5b-t2A-ea79_xLuO5wHmnFpieystKw3XRW5LglPYwD-HvPs-CZTTho96zX7E67ng0HrvAMUZNOo2UXT7TgZJQhSWYVAsck67mevCyYxAInnPJQ0_r05yDSKM35t8oRvkqW3qPgM6oq3zTKZotS3xy16XSdj7fVPmnMBena4sywYwuhJU_9XTipmnisLpbzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: تعداد پرسنل نظامی آمریکایی که در جریان درگیری جاری با ایران در خاورمیانه کشته شده‌اند، بیشتر از آن چیزی است که وزارت دفاع اذعان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/148094" target="_blank">📅 22:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148093">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کارشناس صداوسیما: الحمدالله وضع مردم ما از مردم آمریکا خیلی بهتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/148093" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148092">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نخست وزیر لهستان: روسیه ممکن است به زودی به لهستان حمله موشکی و پهپادی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/148092" target="_blank">📅 22:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148091">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a967d061c9.mp4?token=B8KtDIRoY1Qr93hEWZzG9JXTS24qzUi_NrY5YaqW9Z9t-FyreDtyQYe0IriDnjZhPtUZkdFXDBqB5Du9rL_IQhelkWg0gMhAsN34pwE0EQfnuV1fxrqvCiCbtNhzWIPZtttPq5UqYJyM4bdEiO06Na4TGqM5HJJIlAr1Nj5tSk2nFf21f3nT740PZuYnYIvBD6rvY2mzdct-0KQpRod670h_bDYPYufCBiEA5LG0VR4KqhaEtzSq5ObK9QdaaMWeOMhpZLUoC_X4iFT3AAGlHvppyxdSLaOX6b8bwtqmDWJWCtSK3b4GQMXkmZ4i8VxhQZQ0q6jVwfK5C8jXTNMIlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a967d061c9.mp4?token=B8KtDIRoY1Qr93hEWZzG9JXTS24qzUi_NrY5YaqW9Z9t-FyreDtyQYe0IriDnjZhPtUZkdFXDBqB5Du9rL_IQhelkWg0gMhAsN34pwE0EQfnuV1fxrqvCiCbtNhzWIPZtttPq5UqYJyM4bdEiO06Na4TGqM5HJJIlAr1Nj5tSk2nFf21f3nT740PZuYnYIvBD6rvY2mzdct-0KQpRod670h_bDYPYufCBiEA5LG0VR4KqhaEtzSq5ObK9QdaaMWeOMhpZLUoC_X4iFT3AAGlHvppyxdSLaOX6b8bwtqmDWJWCtSK3b4GQMXkmZ4i8VxhQZQ0q6jVwfK5C8jXTNMIlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستاد اطلاع‌رسانی نیروهای مسلح یمن جمعه 27 شهریور، صحنه‌هایی ویدیویی از حملات پهپادی انجام شده به تجمعات شبه‌نظامیان حوثی در جبهه شمال استان مأرب منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148091" target="_blank">📅 22:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148090">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که جنگنده‌های اف-۱۵ عربستان سعودی از پایگاه هوایی خمیس مشیت، در ۲۴ ساعت گذشته، ۲۶ حمله هوایی به استان تعز انجام داده‌اند.
🔴
آنها همچنین مدعی شدند که نیروهای سعودی در طول هفته گذشته، ۳۰۰ حمله هوایی انجام داده‌اند که در آن از جنگنده‌های اف-۱۵ و تایفون مستقر در پایگاه‌های خمیس مشیت و طائف استفاده شده و اهداف این حملات، استان‌های تعز، حجه، مأرب، الجوف، البیضا، عمران، الحدیده و صعدا بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/148090" target="_blank">📅 21:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148089">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFSC5ZTjVBhGatL_Is6KNGrekPViRix00IKbatwyp1x6K0cZgA5X-N733Zwryro7k0INrSf208tIKv2Hj1v4oeDhhzS9eJgBKW7_QCzBDL0cp-71O5I5DqLhpFWGmvZLF3rrAARXW4vVDNIILBTGoMrc9G3a5P5AHwrrpw8xbpI3n7UqvZXq56tofZW523rS-5S4rDKhBEh9egP8TN6O0EDo-S2S_kfzsPNPIX2z8HgQ8Y0PtKa0wBrs389XobhxAnOWMMA0SwN5L2VuZjXrYmATQFC0kVDHoftVrtd8xCkCtunspldUzcZhrN_TJ3p0fai9mrMmhHdTu7DBnZa7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
روند محبوبیت ترامپ در حزب جمهوری‌خواه اکنون به ۹۵٪ رسیده است، که یک رکورد محسوب می‌شود.
🔴
رتبه‌ی دوم، رونالد ریگان با نرخ محبوبیت ۸۶٪ است. از شما سپاسگزارم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/148089" target="_blank">📅 21:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148088">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
احمد الشرع،رئيس جمهور سوریه درخواست عربستان سعودی برای اعزام جنگجویان سوری به یمن برای جنگ علیه انصارالله را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/148088" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148087">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/148087" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148086">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی وزارت خزانه‌داری آمریکا در گفت‌وگو با الجزیره: ما اقدامات سختگیرانه‌ای را علیه بانک‌هایی در امارات و ترکیه که از ماهان‌ایر ایران حمایت می‌کنند، آغاز کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148086" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148084">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REFZobirEb3zJn7V4mv5t0v4KC75fm1eUyZEeOpEpjq0fyHRrCdT4A_5ojqhJQcYgs2AmYXB2BfACwmgzvCSnbBPczQFjKosDrjxTW1yhAlrGIwcM5IJ3kQ5_E7Zgc8O8gTLQmHX1GMzl5is0wrqwve31IzJFJnmzfLgVAJu1G_tbtjHfwdFhUMkoRkEhGbKOO1rIY_vqAqj49SHpoZaAoL7Wk5oIJbT_upRj2JI6yes3IMeMPwrn3Cbh1wInk_Df_zzaKuzsR89Hzk8Pys5AKfG3vNv5a87vbfJf5uEI3AAx4RG3RIy1vJhkuLFjPszsGKO5fq15NIgcLeNL2NlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUPFGCCn74G7GanGJ4ZBGbQqGIDw-oUUyyEMwP2Qt2gPuMpxAJf8ZlXY9f123ADzQGS935qHeEShaJkfdl5XvgjVrzpSkAZDkT_zWRfHXn_TewSQf7-dKkhG5DwqVTnmQtHnl4sBpQbtaWf5lop-knDtPcZV81s2mya29P3X6rMULDs-apX9WVOsX0H55X6p21lYvw1r9kSFigiFUNklaDQXS_CuMyi9Uw5w-vIhdtKbzNap-TZ3tPh0-FT1XzcoxXvlcbal0PcbYl1sMle0-FtLXGAH-fpV1dGRhlce0_jdN8tA2DFEHeYofl4mat3q4vx3rY5kk7vs0w6RNvgktQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، با جیک پل در وزارت خزانه‌داری در واشنگتن دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148084" target="_blank">📅 21:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148083">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2f66737e.mp4?token=feLkEjl1pKBj5H3ru0JyeRyvxPmAjqRWjljUAu1dFbwLMLxqvxU3mzqtTpDoNgrCHX91stHZB3_nbwuIo8GomU0iyJIsDzVlI_ELpDiQHljDCWR3dg1q1th9e-aTwwTrgmLYmyTK90yO34TidOz5BgWvqTSZ6LcZFayCGrerAQP7zj_zHU0JzdjU8Kolwr8W2k8RQ7Cfn_26y1sMRM0JXTu7xrrzU1JUdqASNrgpW9OBR1kfV7TkYHDf-Uw-EqvZjSIfiW_m-2SnA_pNxcMuNt1-ywNi7R9ZTbGD23LsCYLYStOHtUJ1CSwLs2a8f-9ZxhhX6uO0Rt6ao6N8bpO53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2f66737e.mp4?token=feLkEjl1pKBj5H3ru0JyeRyvxPmAjqRWjljUAu1dFbwLMLxqvxU3mzqtTpDoNgrCHX91stHZB3_nbwuIo8GomU0iyJIsDzVlI_ELpDiQHljDCWR3dg1q1th9e-aTwwTrgmLYmyTK90yO34TidOz5BgWvqTSZ6LcZFayCGrerAQP7zj_zHU0JzdjU8Kolwr8W2k8RQ7Cfn_26y1sMRM0JXTu7xrrzU1JUdqASNrgpW9OBR1kfV7TkYHDf-Uw-EqvZjSIfiW_m-2SnA_pNxcMuNt1-ywNi7R9ZTbGD23LsCYLYStOHtUJ1CSwLs2a8f-9ZxhhX6uO0Rt6ao6N8bpO53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف طولانی تو چین برای خرید ایفون ۱۸
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148083" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148082">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
المانیتور به نقل از یکی از منابع ارشد اطلاعاتی اسرائیل: نهاد‌های امنیتی اسرائیل با هرگونه حمله پیش‌دستانه علیه حوثی‌ها مخالف هستند
🔴
حوثی‌ها می‌توانند سعودی‌ها و متحدانشان را به اسرائیل نزدیک‌تر کنند و آنها را به تکیه بر قابلیت‌ها و اطلاعات اسرائیل سوق دهند
🔴
در حال حاضر، هیچ‌کس بر حوثی‌ها بازدارندگی ندارد؛ نه آمریکایی‌ها، نه ما و قطعاً نه سعودی‌ها، آنها آن اسب تیره‌ای هستند که هیچ‌کس انتظارش را نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148082" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148081">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55aca14f0a.mp4?token=Ltp_0PQi0Y7D2GqpNWVs0o44WMOWmJl-cxb_aw-VeCH2BYgNBYpo2SFlcvNsRB90d5cjL5KHuueP1naHyj3cf0DJ1C49oBqdXYIp4vr9eIz7rDClwnr-j5bt7IUweqoFqwLUz3jcI3p_D2PlHSvght2L8prMx9djuGMmBwI0lRvv93yXw7bojRpYzHTrgcRxPEWm5JSX5v4_5s_QJirW63_FbwmuwLfCs9skCqGFR47_AQNnfyrkn9KIyNJWUYdAZ6CgI_if00rasUaeB_mMXxCm8Q8jhcz3arXwMUbI45WgSAOxRb0yAqlmaD4NdkUfCfln9krm4ntaBf4Karewzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55aca14f0a.mp4?token=Ltp_0PQi0Y7D2GqpNWVs0o44WMOWmJl-cxb_aw-VeCH2BYgNBYpo2SFlcvNsRB90d5cjL5KHuueP1naHyj3cf0DJ1C49oBqdXYIp4vr9eIz7rDClwnr-j5bt7IUweqoFqwLUz3jcI3p_D2PlHSvght2L8prMx9djuGMmBwI0lRvv93yXw7bojRpYzHTrgcRxPEWm5JSX5v4_5s_QJirW63_FbwmuwLfCs9skCqGFR47_AQNnfyrkn9KIyNJWUYdAZ6CgI_if00rasUaeB_mMXxCm8Q8jhcz3arXwMUbI45WgSAOxRb0yAqlmaD4NdkUfCfln9krm4ntaBf4Karewzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا امروز همزمان با دورهمی جانفداها به صرف انواع خوراکی، یه دوی ماراتن ۱۰ کیلومتری مخصوص دخترا تو بوستان ولایت تهران برگزار شده.
[
@AloTweet
]|</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148081" target="_blank">📅 21:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148079">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWF7-Dny6cuLyTbDAMzcQKaylz8NLn7U3w9JIpd9QWb2ERQUEQ6t_4iWBLSIpN0emVVad7bvYnAuyniS-ZUxiqf-pp7SwnbhPbZpJwK1bPrrb7dRuA75S2UtQJMCwV4rVforlJUAGO-v5CiXMr4kbPAR30Fv1hl92vt8vdK5OwtXfsebWsACJsbw2BiJn6ShoT4eyPg9YNt-KJ6Ja97Bc1g3-gFXBOlUhx9cj_D23wT2jEX_SbbLwof92mwxyKMSHKrOykSgCh2gxLbY58YPzFYoE8eJzq54P9jor1d7h7Wx23ltDRqrKIOpPPxYjeQSVbvGX7Usd4ULVRwfX6QoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاليباف
:
دوره‌ای که در آن F-35ها و F-15های شما شکار می‌شوند و مجبورید گزارش دهید که آسیب دیده‌اند
🤏
از قبل آغاز شده است.
🔴
آنچه زمانی سوخت خالص کابوس بود، اکنون واقعیت روزانه است. با آن زندگی کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148079" target="_blank">📅 21:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148078">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
الاخبار: عربستان آمادگی خود را برای لغو محاصره یمن مشروط بر موافقت یمن با اتش‌بس، اعلام کرده اما بعید است یمن از این پیشنهاد استقبال کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148078" target="_blank">📅 21:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148077">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBfe5BXQXN1koiQrZEOm2dHw-4UVsnXRvkUyhsMQLHXhWZ4sxRwp58zOiVcD_vQONGsV7MiFc8q02eOUM02rf00ETpMByIX2DJpbamf3PKgrl18WHnnB_YdbYT53sF7cGCJPVSmBJ_AZMG8tlXmeiFcEam4RG_knVl6luWVbLhv61T6zT36WHZ7jvYcxHVhCfVaIAcUYc301E_uO8anJ3kPX_DgoE1zRhIsjHWh7J0eDnUVeGOwR_91fsb-i0RdaCLldWaHD6J5llzb_QLwnc8eJJb2opAjGdJSXbCWiMfXJ7Lrtp4EJiw2gTAyLYX5W7yIykf5R4qPxJYkbl3PvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور چند داف در دورهمی جانفداها
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148077" target="_blank">📅 20:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148076">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
صداوسیما: دلاورمردان پویش جانفدا بعد از گذراندن دوره های آموزشی، آماده دفاع از مرز های کشور میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148076" target="_blank">📅 20:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148075">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یک منبع مطلع آمریکایی به الجزیره: ۶۰ میلیون بشکه نفت ایران، یا نفت مشکوک به ایرانی بودن، روی کشتی‌های تحت تحریم سرگردان است.
🔴
کشتی‌های حامل نفت در خارج از محدوده محاصره در معرض رهگیری قرار دارند و محموله‌های خود را با سرعت رو به کاهشی تخلیه می‌کنند.
🔴
واردات نفت چین از ایران، یا نفتی که احتمال می‌رود ایرانی باشد، به ۴۴۰ هزار بشکه در روز کاهش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148075" target="_blank">📅 20:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148074">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی، به عنوان بخشی از محاصره اعمال شده بر بنادر ایران، مسیر حرکت 105 کشتی تجاری را تغییر داده‌اند.
🔴
این تعداد 2 کشتی بیشتر از آمار منتشر شده روز سه‌شنبه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148074" target="_blank">📅 20:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148073">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
خزانه‌داری آمریکا: علیه بانک‌های حامی ماهان‌ایر در امارات و ترکیه اقدام کرده‌ایم
🔴
سخنگوی وزارت خزانه‌داری آمریکا به الجزیره گفته واشینگتن اقدامات سختگیرانه‌ای را علیه بانک‌هایی در امارات و ترکیه که به گفته این وزارتخانه از شرکت هواپیمایی ماهان‌ایر ایران حمایت می‌کنند، آغاز کرده است.
🔴
جزئیات بیشتری درباره نام بانک‌ها، نوع محدودیت‌ها یا زمان اجرای کامل این اقدامات در این اظهارات اعلام نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148073" target="_blank">📅 20:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148072">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / ترامپ: "باید ببینیم" که آیا ایران نابود خواهد شد یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148072" target="_blank">📅 20:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148071">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
عربستان: ائتلاف دریایی دفاعی با مشارکت ۴۱ کشور عملیاتی شد
🔴
وزارت دفاع عربستان از عملیاتی شدن ائتلاف دریایی دفاعی با مشارکت نمایندگان ۴۱ کشور خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148071" target="_blank">📅 20:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148070">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری /گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148070" target="_blank">📅 20:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ در پاسخ به سئوالی درمورد گزارش روز پنجشنبهِ اکسیوس درباره «تصمیم بزرگ» او: «آنها حالا می‌خواهند به توافق برسند. اگر این توافق، توافقِ درستی نباشد، حتی به آن فکر هم نمی‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148069" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148068">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ به شبکه نیوز‌نیشن: با حوثی‌ها در حال گفتگو  هستیم. حوثی‌ها نیز تمایل دارند به توافقی برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148068" target="_blank">📅 20:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148067">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/148067" target="_blank">📅 20:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148066">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjq1dr3eN2ovwZcFnv_Zy88IfecrwyQiVry0OxLHp-KQyWmSa9R12CJvy2zXn2Gr0yyf8w03mhoGQlH6V3F9S5AcbRbXAjVr-yfhxRgRci09_huEFSbU9JUgas-JBhXrcWY7sdtKRXEB8g_y-jYE3B8jci3WPWDslY4z3GaVNxTWiG5s5Aabdoy0UR-IURxno2cboAp3f9tZ7Y_Vp8NP_MU52nhmwdgbb5gvgu9tRizZ2OFkfNB52S0cURotsL-eXjknLDYKzfJsH3joAi_v4cC5P3TzV5EafppGdzesliHjnMAK1z4LKucOMc4i7y0jFWKYHZVxrxpe7ey877X_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148066" target="_blank">📅 20:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148065">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مشاور ارشد رئیس‌جمهور آمریکا: ترامپ مصمم است جنگ ایران را به‌زودی پایان دهد
🔴
شرکای او در منطقه نیز همین‌طور هستند؛ هیچ‌کس جنگ نمی‌خواهد
🔴
او به مذاکرات و گفت‌و‌گو‌ها فرصت می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148065" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148064">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX2ZnWcCRAQEUqaZ0wVbx0j4ZigA4jVy2PdpUW5x6xbHGLZHrP-epceIWIJqlR6ggMoRykd20m6NicuBwWIFdb-JTSx7L3Wbz0IuHXzYG4Np1CK77ptiFsaJHaEkAIPs4f-Jv1D4dR2LozvNKUNeUxR5dkd7qd4zntaZ9KYUgMxoC0KZGvw4rDrEr3STP-qbZhdo-4W2nqixf0w8QPRmYsSReQQDOckm054yjOEN70ebG0cBQkUeRkgSaZ1j8lvjK6O1FH_BXMOFFmKnO79q2vJmRR0XYaJmXOh3J5CBT-AJnYuzG8pm5JuIzmVLN0FUnzmwAsY2NaOBubmXsMrBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زین واکر، بازیگر معروف ایرانی هالیوود و برنده جایزه نخل طلایی اعلام کرد بزودی به ایران خواهد آمد تا از خاک کشور دفاع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148064" target="_blank">📅 19:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148063">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فرمانده سپاه: آماده‌ایم به هرگونه محاسبه اشتباه دشمن با قدرت پاسخ بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/148063" target="_blank">📅 19:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148062">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nt1yM0LWBk7H2whOtqjOplFu9U41L5gedAQI8F-C1mgRaifMWcJGr1IqVYipY4foc7J3r5iMt8by99MxKIkCnVozsCzPJt77Oq4H5-JhVpJzcvMo2kXDPgzQxDIgEhrVv7W_zqptHpbFcNmeAIQVlXzrgHBBkL3PXpTKOT4Tb78NX0GQu_RSxjq4V-4H6bpPTnjS5qejonjymBv4HDR-7d8titsOFg0kpnWKpxTumLEWhji1cnjEAKi0sbR1MevCmqpJbOpAHVyRpgVEYlAFwqZUQE5Yz6HD6dHMxMv7foKVX028xYpOtVzW0OgFrqOoz4uiRNx2bDRUI5IGmJ1WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش از این، نیروهای ارتش اسرائیل (IDF) حملاتی با استفاده از توپ‌های حامل فسفر سفید را در منطقه القنطره، در جنوب لبنان، انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148062" target="_blank">📅 19:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148061">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ce71b6256.mp4?token=Fk67hscHpOt9Ea2u2WIzHXBqjqP83n_F_NaOOijODabJBm3pLXcjz0E1RESxcRpQwf0hxFIlalhCizYVCrBvqVMjtGum0wxC6XCuhGLypHH5yBWh737Tbt1IT9XW2Zpc9BHce8AlItERsMve4oWG87xW16YkmMZRMrC7UlZuqSiy8X0h6ejpNE0JSH5C5lKIlDblJPPHVAI16UebQXr0xyqpuXTxhKXhTCoHdO7oNnmU11jQfXrRN27GEhjsqRG9gEvBcfmCx7Rgojf982IxMaFhmuIagoyg5ar5Iwo7EiHjBkfeXoZ1z1uiv3YZ4R5nDj9cPE12xSWICDQFVasQf2j2YD24Trg0hSDXtlzHcrvX7be6TPZgX7t8svMO5DyuTpVb7SuUXTOOJ7h_cLnPQFmVqYZF0zpLqXTAV1TRicjGdaBSm41juCdDWWXjEbNH2eZ2BdU1SMIUsef8QYTIK1fIsz_IBPuCo9iSHnBJ4a2eBESUgdapc6jSF08733sQHRyT9LfkY6YSQQFn_2zfxxY_WHo230qHD8w5shrHv7Mq_7Lcw63P3wotJRY0ynwKvvSBDZco8P6OT-tf_vxZqeaKHRi_EHUZ1sM7mZD3RnYYW_RsI62zoec63FhBU09Gf-RBGYfJI4zqVT8zHEyj29m-ekFpBGLvtTSAvNhh5zM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ce71b6256.mp4?token=Fk67hscHpOt9Ea2u2WIzHXBqjqP83n_F_NaOOijODabJBm3pLXcjz0E1RESxcRpQwf0hxFIlalhCizYVCrBvqVMjtGum0wxC6XCuhGLypHH5yBWh737Tbt1IT9XW2Zpc9BHce8AlItERsMve4oWG87xW16YkmMZRMrC7UlZuqSiy8X0h6ejpNE0JSH5C5lKIlDblJPPHVAI16UebQXr0xyqpuXTxhKXhTCoHdO7oNnmU11jQfXrRN27GEhjsqRG9gEvBcfmCx7Rgojf982IxMaFhmuIagoyg5ar5Iwo7EiHjBkfeXoZ1z1uiv3YZ4R5nDj9cPE12xSWICDQFVasQf2j2YD24Trg0hSDXtlzHcrvX7be6TPZgX7t8svMO5DyuTpVb7SuUXTOOJ7h_cLnPQFmVqYZF0zpLqXTAV1TRicjGdaBSm41juCdDWWXjEbNH2eZ2BdU1SMIUsef8QYTIK1fIsz_IBPuCo9iSHnBJ4a2eBESUgdapc6jSF08733sQHRyT9LfkY6YSQQFn_2zfxxY_WHo230qHD8w5shrHv7Mq_7Lcw63P3wotJRY0ynwKvvSBDZco8P6OT-tf_vxZqeaKHRi_EHUZ1sM7mZD3RnYYW_RsI62zoec63FhBU09Gf-RBGYfJI4zqVT8zHEyj29m-ekFpBGLvtTSAvNhh5zM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد کشتی گارد ساحلی چین با شناور فیلیپین
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148061" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148060">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148060" target="_blank">📅 19:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148059">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر کشور پاکستان طی ساعات آینده دوباره به تهران می‌‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148059" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148058">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس:
ما تجاوزات مداوم ایران علیه کشورهای همسایه و تشدید و هرج و مرجی که دامن می‌زند را محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148058" target="_blank">📅 19:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148057">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=Bc9kz94GwKodPmO1ymC4pxHsfe5vkywhELbCSxnyEBJnGBss0jc9AU6HPgWl7e397Mp7GXX-vXYdYqJC_igmlL7UCiW7rbU-hK7aE0FZ1WycUoXZaipYhy1cMxz8ouCGJX5MTgkQDI_fExpaEnGxGHnxgvSUxfF2wXymRD56Q0N41lQP-n43qxyWq_gO_KZ-fmKNgS3tAT4x2sf0hqnGcbbjQsWL-yydBp84rPtjwAAm9YZ6Z1_F9xkFDl5QrMgZr_nRUEbDp8--r0-U6hENsp03nzbYJa-RsKpP6KDaPRe-6GK8dMnG6xMRO1JE1rRyVyrMsJN3PRg1V2aLQaeB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=Bc9kz94GwKodPmO1ymC4pxHsfe5vkywhELbCSxnyEBJnGBss0jc9AU6HPgWl7e397Mp7GXX-vXYdYqJC_igmlL7UCiW7rbU-hK7aE0FZ1WycUoXZaipYhy1cMxz8ouCGJX5MTgkQDI_fExpaEnGxGHnxgvSUxfF2wXymRD56Q0N41lQP-n43qxyWq_gO_KZ-fmKNgS3tAT4x2sf0hqnGcbbjQsWL-yydBp84rPtjwAAm9YZ6Z1_F9xkFDl5QrMgZr_nRUEbDp8--r0-U6hENsp03nzbYJa-RsKpP6KDaPRe-6GK8dMnG6xMRO1JE1rRyVyrMsJN3PRg1V2aLQaeB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148057" target="_blank">📅 19:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148053">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTfWZQMpUI3x7hfYss45Co42BEOJNigFGPXWK9yCKSSu96qHGLiR3cjCV-VVJWAC2AtauONN740wSzDecUCly4ncKHf3OJ6NmOD0Ig8QE9UbqXsRUF5a28ziNlAcrgPu5jSEAW-e2WnFNH8vuDKlgh1Xhn-joAeQpSplBOJ586Gwaz-SfWLB79NaoHnWtAMD7-qJoXBvCtwGDl30aBCg_WgRuv-1zvzLwncpNapSifj6BflXXSVjGAMfe7-aTBx3536h3AgLl6iGQH31DGwOZ-zeyZ2i_xaLBIHae6oEE4xhfWPr0iZ9u9P0f47kVN9V1TNdNmEw5RDgJEVbqoOgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkOFnmPDNnFvrVf56tn5e7v8cFo_A64C9umOmbwRgVg6vT3ZHNpkQ9qKa16gY7rYPzgFq56LK59PScbdnA2QlqjD46ujjTMEoW0x6KjV3yp-82B86jVrjCBXpr0zUOOVSIdeER4j44EKdmco0jfZZQdGN1nGFpJ7bI_vlrcY8ri0uUW3SJOOLhjxH-TyRbu2hfbJxR3-qtIXlZhUGt5yIDA_qlSEOuoRzqzkj_AOCX1DGZcgFib61cE4qB7yA5op-uVdUA1EMGXdHh3a7x1WL_XVkrRHnfQFq0rtJjohmIuWpEzzfrynnz7dUq8pTbIsLTzgyxNi0SfXu-ppEgJPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAAHihLFLWcm7DqZ5g99qnX4I5z4pOJkoDq5OrnM0OBjDN3lXLcR0XQFPcUV-CPaRFdDh8WHoxZBhHsStWgX7sXzAUm6mkCUYNcjaPnVkMZPUWc1vKffDx_UwOM7QIBy4keyMHLiNzPIaBMbI9oV8Veb0s-zZsshKrAJCq_zJod13zSrVHnSAgIQyrab-X9BXyAsPY4cwKvNrnWahV4hu1oMJGRcQx9l1NYGYCADZFem-NMT84XodLhQlPqp0AIwaPKWnhaJuRhc4pcF8ejVRX3c2uDa3DTXKBaFxtiqnExfAOlo4Z0zi34Fxm2LD14k5G2dWHdYmlC-NCwCLKwxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKemG9CvrZBPP5mGbbI4cTKGnQ52GlrUfYUS95ewY73nYpuAlrIh5BGByWFQDd0H_H2u5nnxFLlGhN-rcbJjpn-l1i2DgVRh7cS1dPBotreim0yJd4GidBngeCzSN5YKhRUlpO-JFCRod1PXckKi5J2U5wu042uZ2Jrte8nT7Lsf7xXdwQBV2vONBRpUMMOonPBHOullMyxHgOmBT9GLrbYiHcbLkBG07Uk8n1siny2BQHVqjbL5jmRpkc2FPyNy90-HeFR9q3jmR2UCSQRfpEg9n1PsC-3ybW2I5FyM_dSDBEVYVrevTq6WEMDN05a1nuO89EqbCLHCzLMLf9qN9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یاشار سلطانی این ۴ شخص رو اعلام کرد که حدود ۸۰میلیون بشکه نفت رو بالا کشیدن
🔴
۱٬۹۳۲٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148053" target="_blank">📅 19:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148051">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=eRILR5P4uWb625CtpcwKJx5m0RudoSMYJBXtef22-HFRpE_SphdaVkuuJUzmVN79LwAYjhHe2MYBmXAlNrt_AFATI5vy588vGPgsAwL8mxam3hmUj2SM5LrBb__sdMz3OZfHGTIFRYcxdyxXLguUoDfM-lrxp0tvufWSJNeSxZ2NeEcR9LSDH0s7WEZcNE_kkR3xP1jvZ7jBuVwC2xLh3bBfBhsM6WRUSHTlXInVTFySgRFto9ujAeCI2zSInqckh3xeamP7KwssTDFN1gZOBa403yF77vopVsQFTsCDNxj5giCY3CGF_7fIvHDt3uG3fbv_D4D7JWMjy21GV6Qrvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=eRILR5P4uWb625CtpcwKJx5m0RudoSMYJBXtef22-HFRpE_SphdaVkuuJUzmVN79LwAYjhHe2MYBmXAlNrt_AFATI5vy588vGPgsAwL8mxam3hmUj2SM5LrBb__sdMz3OZfHGTIFRYcxdyxXLguUoDfM-lrxp0tvufWSJNeSxZ2NeEcR9LSDH0s7WEZcNE_kkR3xP1jvZ7jBuVwC2xLh3bBfBhsM6WRUSHTlXInVTFySgRFto9ujAeCI2zSInqckh3xeamP7KwssTDFN1gZOBa403yF77vopVsQFTsCDNxj5giCY3CGF_7fIvHDt3uG3fbv_D4D7JWMjy21GV6Qrvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاشار سلطانی، خبرنگار:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148051" target="_blank">📅 18:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148050">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع العربیه: محسن نقوی، وزیر کشور پاکستان در ساعات آینده به ایران سفر خواهد کرد و در تهران تشدید تنش حوثی‌ها در یمن و پیامدهای آن بر امنیت منطقه را مورد بحث قرار خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148050" target="_blank">📅 18:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148049">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIMrAjFgZiyJWnfhXYZp3VXrop2qSKngR6qKrz9G0BkJgvsjNgtl7GOCWBoFfPsbICQy5M-FrdlBsxlHEmvPnnSaGP-csp4p30vhPPbfnRMNy7fk8l1SDTXbnYY4pXomw6KX7k6MlSldisjs3ItmAgCJy9lzM6T0jG8zvgeMnfaSaDjCWx8p5tHFLjdh8MEgnSxB1Ta2h62twzQjNhRXa_hxhFdQxFY1v2oAcp1Heu3RRiegXmhHdE8FPijGUr1N-7n6gBiysNUCKxhPSjw3X70Inv7vDeHYB3Eekz4o9axKZYoCIeN-PA9-IiYqVvPecz60q8MWZ2-4jCrkInWPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: دولت و شهرداری هماهنگ شدند تا از ۵ مهر قیمت برخی اقلام اساسی کاهش ‌یابد و تا ۶ ماه ثابت بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148049" target="_blank">📅 18:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148048">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فیلد مارشال مخالف صد در صدی مذاکره و توافق و صلح بود و تقریبا معلوم شد چرا و به چه دلیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148048" target="_blank">📅 18:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148047">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA_UIspFG0v66S5QrOzjjL3Prj9HCwsm5NGqu4MQbYISFEKaq7iXhJ9L-d0uAqJIK-g6BMcPdC66she-E0O6biVNLCX8DRlLcp2iwTmQAGpAx1iVWbF1PaK6gPVEQW7RV_ufvyVxfTbCtUrfsMqs1pij411eEY5dJ4DgY3MHCkpVyNZolE5O9urD6ISt9VjJMvqKRGwHIxcqCVcaiwBToVSUSyl9wxzezwu9GGlK-uwBq2NIbZioaRKtqCSIOqOtWZcGaD9XdX1ooHiooaBpfyRhlFZ_77AoV1kL35zevRbzZlxsHaQwTVpI_z3Nw3HcRXL7RNFmXAfEFWoWYuG69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148047" target="_blank">📅 18:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148046">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148046" target="_blank">📅 18:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148045">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148045" target="_blank">📅 18:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148044">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac59fbf2fd.mp4?token=PgVUNpT88iY-GdmndyDe8tdpnPplCahUKnP1kUZPB9BpSatGzLXEmfHz7gFvqQTtX5Gmz_hDiP7b7pOP5sBHKnhAPL08OAqAlIi0_YKPVG-Ebw7RSsW3MQgvAJGa13r1kFdXRwCZG3jm9HHYaDWYY7t2Ofc1Wk7kYmPgL32Ag4MQjy_2BgJKFYK6MDkXwlhnYvcBuhoitxCxKC-WEt6s2pTrDUb0aZhmk1N9y9gErqdrRwxoljMYNp-ktysh6LOYHi-uAwhtnuj7wQCxQYONmr1omiPA3XmDbaA7YKF-g7MHnSQOmVXkyJdAo_JczJyKk14q3pP7D1iO5y0XEP7jPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac59fbf2fd.mp4?token=PgVUNpT88iY-GdmndyDe8tdpnPplCahUKnP1kUZPB9BpSatGzLXEmfHz7gFvqQTtX5Gmz_hDiP7b7pOP5sBHKnhAPL08OAqAlIi0_YKPVG-Ebw7RSsW3MQgvAJGa13r1kFdXRwCZG3jm9HHYaDWYY7t2Ofc1Wk7kYmPgL32Ag4MQjy_2BgJKFYK6MDkXwlhnYvcBuhoitxCxKC-WEt6s2pTrDUb0aZhmk1N9y9gErqdrRwxoljMYNp-ktysh6LOYHi-uAwhtnuj7wQCxQYONmr1omiPA3XmDbaA7YKF-g7MHnSQOmVXkyJdAo_JczJyKk14q3pP7D1iO5y0XEP7jPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لباس فرماندهان ترور شده در رزمایش امروز جانفدا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/148044" target="_blank">📅 17:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148043">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر وقوع انفجارهای متعدد در تنگه هرمز منتشر شده است و این گزارش‌ها حاکی از آن است که ۴ موشک کروز به سمت کشتی‌های موجود در این تنگه شلیک شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148043" target="_blank">📅 17:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148042">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=VPmGA1wyUArE03q393Tv8zfQVAB0wSpouphXhw924cWH7Yiw9VxkgPzokPOkj2mIpNMDsjc8tpODOFdllsbht62N1pdOnFWTEISteQZJRIOyG0XEuyHPOJ4EUUKVJZQ6GZXMcyKY1KzuZ1Ht1AHDV42RqXSK8JXRiHVVOR9ketXIDobcmz9ty_P342OHods-mmnYwEhMvFCClKL-NazQC2fsWpssrbv7nrYHFBmhA-ErFDmBMGCpwxo8OJNP_opYWjn9of8b8JQKY_h0JZF-koT4rSsQ_zey9hlIYaWccjRt2uVCIrfXwgd35VcOj4lcGuGa9FDMvCdggw_qBzmF5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=VPmGA1wyUArE03q393Tv8zfQVAB0wSpouphXhw924cWH7Yiw9VxkgPzokPOkj2mIpNMDsjc8tpODOFdllsbht62N1pdOnFWTEISteQZJRIOyG0XEuyHPOJ4EUUKVJZQ6GZXMcyKY1KzuZ1Ht1AHDV42RqXSK8JXRiHVVOR9ketXIDobcmz9ty_P342OHods-mmnYwEhMvFCClKL-NazQC2fsWpssrbv7nrYHFBmhA-ErFDmBMGCpwxo8OJNP_opYWjn9of8b8JQKY_h0JZF-koT4rSsQ_zey9hlIYaWccjRt2uVCIrfXwgd35VcOj4lcGuGa9FDMvCdggw_qBzmF5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت صداوسیما با 65 میلیون بیننده روز به روز داره عجیب‌تر میشه؛ یه آخونده رو ورداشتن آوردن توی پخش زنده تا این صحبتا رو بگه:
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148042" target="_blank">📅 17:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148041">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
صداوسیما: تا الان بیش از 600 هزار نفر برای شرکت تو دوره‌های آموزش نظامی جانفدایان ثبت‌نام کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148041" target="_blank">📅 17:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQC1fFIMklsOOFiZCnXACdy-Fg5WXezxh_eGizVmVykcTAHQnQNv4mcV0bzKq9JT4Kq0TaoLFX--9ZbRR62fhxPKMadFFpYDfznCP2FC1XNtE4fqBlufmVjswCughbHNqjG0KK4hQMxH96uTA8cTFrgGlSUWLzqeYAmfZQg0cNyA339Az3Sy8G_Gvwg1d_wxI4RQR0hDu0GfuHv1grE8JfU60r1iL0BLIJJZ--kvHBBkKpt7rorA8CDk7Ri4xsvX1jXgwEqKaZPf_SXQ03ebKQLF0oGj5Mlp0xq-fKhKPggCsagAuR9LkQpIELdY-bTyHXffDS_qNHS8N9j6pOUTAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انبار مهمات در منطقه "ایاش"، واقع در بخش غربی شهرستان دیرالزور، سوریه، امروز صبح منفجر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148040" target="_blank">📅 16:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148039">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148039" target="_blank">📅 16:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148038">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f37NfM-6Z4me4we1LEB-YmHDci109cmpI_NLD0vVzyXzhh6WXSBxA2upGXa2wVnHPAqsQb_E7SO9S2OvQ2ttZC_EUPJP8_nCWOk0eCC5kASq4Ozou9swhr6UUSZUj6Lp0RjmTOj8Lu6wFTRnWTB7c49cRPRrkSX0Rc73lJnwD5A5p5TyPJHFuHTMMITd7tbWwTrWO3SBmiyiU_eI8P-J0xN1Z3tHhYtQ_dbPi5yWC2FkQ9ff-Voh2Q7xh_ztsd1gZsI4FqRNUIFfcNeUJLCwG5C1jaN1Gh10ecyS6dD-vrfRHLbVPztM-D3ETbNNIeXaAGzmMPRgbq-gQNxEu0WOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کایا کالاس، رئیس سیاست خارجی اتحادیه اروپا: حمله‌های حوثی به عربستان سعودی غیرقابل قبول است و اقتصاد جهانی را به خطر می‌اندازد.
🔴
اروپا در حال کمک به حفاظت از کشتیرانی در دریای سرخ در برابر حمله‌های حوثی است.
🔴
با توجه به وخیم‌تر شدن وضعیت امنیتی، عملیات اسپیدس (ASPIDES) اتحادیه اروپا سطح هشدار کشتی‌های خود را افزایش داده و همچنان وظایف اسکورت خود را ادامه می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148038" target="_blank">📅 16:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148037">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / عربستان سعودی از تشکیل یک ائتلاف نظامی دریایی بزرگ از سراسر جهان برای بازگشایی تنگه هرمز خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148037" target="_blank">📅 16:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148036">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا:
اروپا به محافظت از کشتیرانی در دریای سرخ در برابر حملات حوثی‌ها کمک می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148036" target="_blank">📅 16:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148035">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه آمریکا در خصوص سفر هیات ایرانی به آمریکا برای حضور در نشست سالانه سازمان ملل:
🔴
ما اجازه نخواهیم داد حکومت ایران از مجمع عمومی سازمان ملل برای یک ولخرجی تجملاتی در فروشگاه‌ها استفاده کنند
🔴
ایالات متحده همچنان مقام‌های نمایندگی ایران در سازمان ملل، مقام‌های ایرانیِ در حال سفر و افراد تحت تکفل آنها را از خرید کالاهای لوکس در اینجا منع خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148035" target="_blank">📅 16:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148034">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رویترز: چین در پیامی خصوصی از ایران خواسته از نفوذ خود بر انصارالله برای جلوگیری از گسترش درگیری‌ها در دریای سرخ استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148034" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148033">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه:
«تنگه هرمز عملاً همچنان مسدود باقی مانده است و هیچ توافقی برای بازگشایی این تنگه وجود ندارد.
🔴
در واقع، وضعیت تردد و عبور و مرور نسبت به چند هفته پیش وخیم‌تر شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148033" target="_blank">📅 16:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148032">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEEyZu3FIB90QD7p6O-mwvMVITDqi1S6xtp6n9nrJDS3RztckpwnDChsp98yhxSzV6QfftrsNvmfGWihTXGL1Mj0ZIDbq-XpOPRQpmiT540Bj7GMHK1-648g2BgHv2segnnIlQsVfnj3CPQ1raZioddrhDD_vLOkg1i02D661h-EeY9IQ9UqGEZ_72Wyb-p2rlYgG0xtmypUYesO9Y4f_IKCrFXb3phoZsW8V70FKJ13cyNkAOoADC8rwKEJ__KwPo_V6NjhKwgWhZA-PUgAAVsJz176PYty-dFGSSX2B0dNA1XmkS-W7uDxVHUMT_XGneWrMoTVnmGY8xciXaDQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا با قرارداد ۲۴ میلیارد دلاری فروش F-35 به عربستان سعودی موافقت کرد؛ جامعه اطلاعاتی آمریکا نگران است.
🔴
نهادهای اطلاعاتی آمریکا نگران هستند که چین از طریق جاسوسی یا روابط امنیتی خود با ریاض به فناوری‌های حساس دسترسی پیدا کند؛ این نگرانی‌ها همزمان با پیشرفت روند فروش ۴۸ فروند جنگنده F-35 مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148032" target="_blank">📅 16:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148029">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3k2fXxIXizEG7trasyEF5Qt5zr6WRIS4aWVBOeX58cviu7ExjBddEoZoTduFJdUruHPxgExbdJGfO2EbZ7KQrQCD6zLpurlAd-jIJYAK8ru2Q2K3GBmsAgShuHKiXzPNWqSthDlEp1Nrr8FBZjykHT96fIWfA76uZbO-z5dcn98DPXivEQsszWCqsr2PGgYmET2am5SFIMriEJ1CjdOXcd7oKBCIW0YVEO0GbRqzM50YCIn0YPjjuwgw9NrXSWfn0KSy4lSulWQhifvuHlF9Xy102R52sKZ-wVgh5w8PxA8dfTvL62ZNiwBjf8wLetfbdb3R_E1Z1Qe6GP4vqVXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZt2S9Eu_T3WuH5Ul0yOpRA3YXeEBeNAVk3uanJRlimd-bt3_yzK7JR9qONj5Zgqzuk9MM16HRIAmiIieYe2E8xC7LvLRSIeLxY6_D6_xfmvAxqf9DuKhZ3LSinYaDv3rLDlUtvvk0Gx35NjhXophfwRVb8hC4kA6zHnb6Al53j1kPolNVXEYcA54s6ehFkieoAuyqzlcgq3x0wUWM5gXx8sTdaV8hfagzEkcVocqpAX144cLjMqv85DSvWZc5HGNMKNLJIzDISmnyDaauEs6HY4VVLZDAcqDgOJP8VtrCxl9CVtiBC8f9kaT2qvARwvwJAPwRVi3879u_CEeMREKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cA8iq5ysXo2l9PtQQ9GPBdIehy3Eh61VxoYayNFBd38fzPmO00TC9_fdmwXWqe3xtS2NPhWG76CmFOwBOtNr7VJnRETLvrw22tzO3XDO1vOHpR8whHbKAE2GvGHMq0E9jmUPnrizxuU8pzKuc49UdGM6U8Bpbfp6tfNae3vKHfJ9YUsmAXRYUluzNQPprgbElisO3ItJZoeYlCtyDy3rhBX5bsEN9SkezJQ4Kd47YQk3aFLIdGxTsVGhYKIVytMtita1vQv3_VFOeUMweROvZKWsou98Dremg9QGIzoXnCbkEolYjfkDk7GS_5O5l0JjLRjbVkSblBmbukfw0fHQag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انفجارهای متوالی در نزدیکی یکی از انبارهای مهمات در حومه شهر دیرالزور در سوریه رخ داد و آمبولانس‌ها به محل اعزام شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148029" target="_blank">📅 16:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148028">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مکرون: فرانسه در چند هفته گذشته، هدف حملات ترکیبی روسیه قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148028" target="_blank">📅 15:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148027">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGUMlq54iyZouXtf9N4e2ZKQH3CakMNvz1_HENCNR27IdsDqCejz2HSettOmT_QFo04IieHm91PfbAZhAtumBa9LyyzinY70UWwTHCRnR7lzFQnStrt7VVByUp4WnkCRf-QA3Jl4-FqUvXob5U_RPSEN3x0_Ry74T9QGFHE99eVsvXomQgV-qcgWu43TW5Ymfol9lWICLZRrvLs3OtSqjNSxSgGK75RQFVE47ZusuaqW992AktGb7WT44bmMrzECALhIv7KUF57dBwgm_wogm_rAH4fEIZ-rLJvXHVHPui6VuU1y0PepnBVUPbaGMBSM737PFMvp4K8s2mBoyqYIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بلومبرگ: شرکت آرامکوی عربستان سعودی به پالایشگاه‌های نفت اروپا اطلاع داد ماه آینده نیز نفت دریافت نخواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148027" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148026">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
خبرگزاری فرانسه به نقل از یک منبع اگاه: پزشکیان، رئیس جمهور ایران به نیویورک سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148026" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148025">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مرتس، صدراعظم آلمان: دوران دوستی بی‌قیدوشرط اروپا و آمریکا به پایان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148025" target="_blank">📅 15:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148024">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: مدارس امسال حضوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148024" target="_blank">📅 15:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148023">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn8PdlJ2TWiJFRWWAJCoMn-ipQlG028UKCwD6_vpb4H9kfcU6io_AVfoiSQk-XDH6IsxJqa3ni7LoU2QdyvtQNeXHmk2uQ_W8QJTaKiH3XeRBDzu4LBqz9GFpZ7z6UliLRbsFhFWjPrAKIOk8ogWJn-3uMBlieOPWAmojq9CtOCE8-VwnahW1gLC6ojYUGLD9CBqY4sK1Q4IOAc6V0Zk-Ic4xYIgkvf3odH8qdk89qMwJnJZPhDvPdnta3WCP7IoL3dhsHedIM51qvp9ShWwgulFFtCfQEsg6HJ3rjyJLH4ahZcufupNiJHpN5gaYXnwISii7i6xc9jLeO9N_y9opg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای باری مدل "بوئینگ 767" که از جیبوتی می‌آید، در فرودگاه بین‌المللی صنعا فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148023" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148022">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دراپ سایت: تحریم‌های جدید هوایی ترامپ زنجیره تأمین پزشکی ایران را تهدید می‌کند
🔴
اثرات تحریم‌ها بار دیگر به آسیب‌پذیرترین افراد در ایران لطمه خواهد زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148022" target="_blank">📅 14:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148021">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2706380824.mp4?token=Y7xrwOSXXa1rvvUAEgZre1w3Qct_Jc2y-y5WK7fBP5a6hOviUrj7myEddsu9ummBtXbdfZreiQiNS0sWHl0neycrHwpyQBYKLvJlo8zLZ2JskT_XSyxBkqcZVuajDsbgIgtJd1QxveQ5LqsP8GhiI6Ql2IiI5aIjJLRrz-cgj12jUc5AleT-v3-KnX3rDeLZeoWVEM5iMexmLFYfx0oJDyr0dp97-Mn2vkQLysukAQQIicWkf_GfxfDrwZOO6BgBnrxfDvvuPDcLczp_ZsvlobvVDJC08e1UkzrcanzoytivovQS2q_HGDWAcZpZ2yktJaqDJIf8f7268b9vwJdS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2706380824.mp4?token=Y7xrwOSXXa1rvvUAEgZre1w3Qct_Jc2y-y5WK7fBP5a6hOviUrj7myEddsu9ummBtXbdfZreiQiNS0sWHl0neycrHwpyQBYKLvJlo8zLZ2JskT_XSyxBkqcZVuajDsbgIgtJd1QxveQ5LqsP8GhiI6Ql2IiI5aIjJLRrz-cgj12jUc5AleT-v3-KnX3rDeLZeoWVEM5iMexmLFYfx0oJDyr0dp97-Mn2vkQLysukAQQIicWkf_GfxfDrwZOO6BgBnrxfDvvuPDcLczp_ZsvlobvVDJC08e1UkzrcanzoytivovQS2q_HGDWAcZpZ2yktJaqDJIf8f7268b9vwJdS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رژه عروس و داماد های جانفدا تو رزمایش امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148021" target="_blank">📅 14:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148020">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بلومبرگ:دو محموله گاز طبیعی مایع قطر از تنگه هرمز در هفته گذشته عبور کردند و یک کشتی دیگر نیز در حال انتقال بار از یک کشتی به کشتی دیگر در نزدیکی سواحل عمان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148020" target="_blank">📅 14:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148019">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان: با صرفه‌جویی جانفدایان در مصرف بنزین، گاز و برق، می‌توان از توقف چرخ‌های کارخانه‌ها جلوگیری و مصرف انرژی را کنترل کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148019" target="_blank">📅 14:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148018">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فایننشال تایمز: پاکستان بر اساس توافق امنیتی مجبور به دفاع از عربستان خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148018" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148017">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p96VEGsjtW684O348Rg1ZCxSKhFz7SDlqMUkFg2B35YY40mZl1H2UiAyhGEcz3XaMFKjDCamktS0x2wUYdS7Vf5VEJ1xPKlW9wrT3GFTQV0yoXzWuGLPP1jgXdV6Y3TXFqqqeWFNc-L5r8p0CnFf1Ws8YPFW_b3n6axddZXocQbxXdrtCGUGmK2fk30rqVhd7FSvPzfZi-9aG5Z1rMAnbAd1LOA7WKo7qN9lOe2cYjqZzV520qzTvBVlTZSd6n2VBH2mmSNv-wwMz-QY3T8G8TGnuGzhlEVqyqlTy3E7pXRMq1vREuc6GQlGSmvy-S2NNBlgk-IRXVhH0XMcGTz3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خطیب جمعۀ تهران: تجمعات شبانه به دستور خدا انجام شده و تا هروقت خدا بخواد ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/148017" target="_blank">📅 14:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148016">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148016" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148015">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: با وتو شدن قطعنامه ضدایرانی توسط چین و روسیه، آمریکا بازم شکست دیگه ای خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148015" target="_blank">📅 14:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148014">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnFNT17WiuOPyi6QGeDqKktqptVBuhsAQ46YO6olh5jpNtHD1fTM4PgHQBEXK4sQP0-0xT3USZVKbWWX507ivg4zHYKvjx6HCLangZ-4VMMuw_6ay4lSEerPdUQKo21ccSEBXStQXD8_pidwORBsTjU9mHm5gOKgn8RKyc_pqGkXsw3gqf67Q8XVuG-wWUhcsOA4eewVLpjSWjdBRVe8s0JbCQ_NOTo0FKyfobMH6M8KCKCUCfE0euf4UsoInnnzEbbdI0ZZA_fZuvqO3Uw-3g19CVTnIqeIpBNo3tt1GTPNk-I9eSbqawlUGop6oDVBdx2wJ7MMefwU_nNzyOYePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت امروز با قیمت بیش از ۱۰۳ دلار در حال معامله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148014" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148011">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=fENXpjx9eEeq28GPW_2iiSJesH5eE_nOBkgeNYPUyxswv2P1MC5WWDIB8PlnZjuSYBYwn1g2BJkD_EVZNaHeILnwPjUu8bWtbJMJUhLPVjRomByKW9zLF_k7Vj5J7_LUg_tD6onWWxv34qMY-KCG80b1R1GVczGjZIEwAKegQaRrFPL3g5ZzcSJXa6xdUGJ5jXfmszZ7zgG0b6mj6FSgPoQF8MItkPCFdG8ZJLoTuXnFq_oz3X4_WzXqikHfKImt_u1vtjR_S06b-2pc6pUC1WvJ8F47de14pR2KrI0cvq459WXZjk-cpLJz3Z4Aa3Wu_SLGNTxDGz7zJ9jX4sFd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=fENXpjx9eEeq28GPW_2iiSJesH5eE_nOBkgeNYPUyxswv2P1MC5WWDIB8PlnZjuSYBYwn1g2BJkD_EVZNaHeILnwPjUu8bWtbJMJUhLPVjRomByKW9zLF_k7Vj5J7_LUg_tD6onWWxv34qMY-KCG80b1R1GVczGjZIEwAKegQaRrFPL3g5ZzcSJXa6xdUGJ5jXfmszZ7zgG0b6mj6FSgPoQF8MItkPCFdG8ZJLoTuXnFq_oz3X4_WzXqikHfKImt_u1vtjR_S06b-2pc6pUC1WvJ8F47de14pR2KrI0cvq459WXZjk-cpLJz3Z4Aa3Wu_SLGNTxDGz7zJ9jX4sFd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاشار سلطانی فروشندگان نفت را لو داد!
🔴
از داماد سخنگوی پایداری‌ها بگیر تا خانواده فاسد شمخانی
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148011" target="_blank">📅 13:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148010">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
منابع داخلی: در صورت جنگ زمینی تمام جان فداها به خط مقدم ارسال میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148010" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148009">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
تصویری از انفجار در یک مسجد پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148009" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148008">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvhWP2YEDU5o2F6rWf2UaLiEgMEQArmW42CIrsH0vFldSIEpjBXuz1SvqnMyeMxpEuZt8KXjAPxyyGGr8G1k-p-VttIDK55_BYkluDwZy5eGEXGMpVQ6OjfKmTSpXDMoZpeeGxd6kaO1DnLEeBJcu2VT5wDbdrN01SSzMwkQ3AUFZI-IggrvrOQfjZHzUj1h4B7ORCMmEuJiB_uXgsAKqjL0GFXsxPC6-Gzw5tc-c25nlg9yF9X1aRf4KLnTbLAB6118K-3or-b2fQ64R-QvEb_t3yWahXZJxRvykukccAjaVxE1FevBlomnwL907ripNNBO7sZLV2QKIDqD8_lcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش اتاق جنگ اسرائیل در مورد تصمیم مهم ترامپ در مورد ایران:
⏳
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148008" target="_blank">📅 13:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148007">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiqtw4MjJGsi8m5BOyvZd33eH14FaFJjcTNoUu6iq49zbIcBxRdxY0P-rewokdG-m6maVuIkP5r8DZhRqGDyflGL-GOEiH3dZMGuj6jo89H90VOeSD3EFRQlCzuFpXqaF7pBpZhe6PA_hF-cEgR4m_rY8-ZJMvZTi28Al-UzwSk1YVBtR-NMTd-7q1_bgBxFN9DvHyFAOZ5dirkvdvAYNJJO_AqcKydX1BKMh0sPGiR8sbMdldfumQYFpMAYZspouQzIuk7TVtZLa4mowsDBlVwAii8E5uxIAfZMIyGuMKWESTKDDbVr7MF1j8uxLZQEJT4RBI1WHps29FOsKh85eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش لبنان از یک موضع تازه‌تأسیس در دیر میماس عقب‌نشینی کرد؛ این اقدام همزمان با پیشروی نیروهای اسرائیلی به سمت این منطقه و سپس تفتیش خانه‌های اطراف انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148007" target="_blank">📅 13:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148006">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فایننشال تایمز: ونزوئلا ۴ میلیارد دلار ذخایر طلای خود را به آمریکا منتقل می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148006" target="_blank">📅 13:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148005">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSHA2kT4_mQYFx1kmlCm5ZUpFENN7_9-kEcMd3diMiT7quxndwq83AF8xM156anUqGQF2w0LciYjJjIDGmLpPT0NeY94kdD__CRy6Uch1sbjVzlSB9U4bzzbpdvj2jfEA95P_wp9uAw_QN9krq8fmDgostKP1BAVMhX4zqkrCgdK2Tlua-XoWtOaH2m9cq6CA3Ns5EgAgBN_OOEK2uL45sJVzy9hGWufr2zATcL3d2kDbEVsGBB4nYzpmGCl2v87deqsRtmoEVMzuxnvD5JdBv2H_RvOtfjhEnKyk1O-a-7-FHZInw70AjQUNbB-g9k26-cYlMozQsMW66J0FtGJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
غریب‌آبادی: آمریکا نمی‌تواند با خروج از شورای حقوق بشر از زیر بار مسئولیت خود شانه خالی کند
‏
🔴
معاون وزیر خارجه: تاریخ فراموش نخواهد کرد؛ در میناب، مدرسه‌ای به خون ۱۶۸ کودک آغشته شد و در لامرد، زمین ورزشی به کشتارگاه غیرنظامیان بدل گردید.
‏
🔴
اکنون همگان اذعان دارند که وقایع میناب و لامرد، نه یک خطای عملیاتی، بلکه جنایت جنگی آشکاری بود
‏
🔴
آمریکا نمی‌تواند با خروج از شورای حقوق بشر، از زیر بار مسئولیت خود شانه خالی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148005" target="_blank">📅 13:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148004">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بانک مرکزی ژاپن روز جمعه نرخ بهره معیار را از ۱.۰ درصد به ۱.۲۵ درصد افزایش داد که بالاترین سطح در ۳۱ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148004" target="_blank">📅 13:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148003">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33da215b97.mp4?token=kPLJ2WoWX8gppgOL-C5vQiZqxu8YmVyFshBB4GdhBiFy-iFb2rmjRSuu-1KUjpZJ-7vQrcwYNCyBet465mc3ZjgsTS-UF7nZZfhbWqxKEFJ2sUin4SdyVbDA2lsR-5o3u2xXzot8OTqR7Tx6rutWdyA-rQf47wTF1mBfBPhMLBzDqEq7f02yQXkXoykD8dWRDO6wi8XLNS7Cq4moyldGtq57N6S31QUglucoWIU4h7nNJns05UJx7NH6sr43S1N220w9ZomWf-QxYLfRcTJFsv3KlKbbyhevbInJBTtbqYIo5NG-a1uFTsvEfoan3RPJ1pi9sH6wG8cUAVUqMm-VRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33da215b97.mp4?token=kPLJ2WoWX8gppgOL-C5vQiZqxu8YmVyFshBB4GdhBiFy-iFb2rmjRSuu-1KUjpZJ-7vQrcwYNCyBet465mc3ZjgsTS-UF7nZZfhbWqxKEFJ2sUin4SdyVbDA2lsR-5o3u2xXzot8OTqR7Tx6rutWdyA-rQf47wTF1mBfBPhMLBzDqEq7f02yQXkXoykD8dWRDO6wi8XLNS7Cq4moyldGtq57N6S31QUglucoWIU4h7nNJns05UJx7NH6sr43S1N220w9ZomWf-QxYLfRcTJFsv3KlKbbyhevbInJBTtbqYIo5NG-a1uFTsvEfoan3RPJ1pi9sH6wG8cUAVUqMm-VRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از انفجار در یک مسجد پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148003" target="_blank">📅 13:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148002">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
انفجار در مسجدی در پاکستان/ اعلام وضعیت اضطراری و احتمال تلفات
🔴
شبکه‌های خبری پاکستان در گزارشی فوری از وقوع یک انفجار قوی در مسجدی واقع در ایالت خیبرپختونخوا خبر دادند که تعداد زیادی از نمازگزاران زخمی شده و برخی گزارش‌ها از احتمال تلفات انسانی حکایت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148002" target="_blank">📅 12:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148001">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPu0H1hFcNCXJVOJplHaMszc4PCws7bjxZ8lrDUQbaCW2m_oXxwX8R5tBXrp-KabLV1kVsyIYpZqEC83nhsj-bCF25jInUemvSuLhmrxV1JddrnmIvT77RNtizsVn8MEDKOXIa_3qeh2Wd7ijDK9iQT_UAYWmXgBkkHSGLGtZek8V0g2j3dcALrhi39PmPt9UtVlqb3tb-Sp9euAujfKVjMdbYjBfJ0w2iYekap3fbYYNAh56Vp9sKaTfjyY48LQOFB-ojZ663up-ORJc_y1gFkAYahQGFlpxyOpZ4uCBgcpWhwD62aICKv_q5MyFutywqCfV7CLa2zBPItZfRgimQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت ورتکسا (Vortexa) متخصص در تحلیل داده های انرژی و ردیابی حمل و نقل دریایی اعلام کرد که از ۱۱ سپتامبر 2026 (۲۰ شهریور 1405) هیچ محموله نفتی از بندر ینبع عربستان سعودی خارج نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148001" target="_blank">📅 12:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148000">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر دفاع ایتالیا:یک هواپیمای جنگنده ایتالیایی مدل یوروفایتر F-2000 در جریان حمله به یک پایگاه هوایی در شهر طائف عربستان سعودی، شام پنجشنبه، آسیب دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148000" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147999">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMoQi9AAs4dKsNziz2IRtsg4nELKqVRrX6GlZ1tQJWG4EQvqtBHJOuWCFlNLCEHVrQZzeLW4terfPTDVEY3Uea-w_vccrtRyMJe72kXTzhPhZOfoU7eZ23MFjoadvAEEKJ5DCExmkYxJgVfM16hkfS4rUjWAWkVNVxZ2DspHf284DjY4Z0-e89VU0QzKxP8YraessK7WmIDACQBUXRjcJZsgnPGpcdq9k3d1bxUapM9Bn_1LteYbzRZOIPPOVwJBtURWgvq8lMLOMbutt6_HgnCEB4x8hGHRiMVBdciS6x0PVADitvpreGErUSdpmaRXxOXAFpceh8o6lqqRqRU-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در شبکه تروث سوشال به یادداشتی در واشنگتن پست اشاره کرده و نوشته است: بسیار جالب است. حتماً بخوانید! به افشاگری ادامه دهید ای سگ‌های کثیف! وقتی پیدایتان کنیم، بهای سنگینی خواهید پرداخت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147999" target="_blank">📅 12:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147998">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
جی‌پی مورگان: بیت‌کوین احتمالا از طلا جلو خواهد زد
‏
🔴
تحلیلگران جی‌پی مورگان در تازه‌ترین گزارش خود اعلام کردند که اگر سرمایه‌گذاران از لاک دفاعی خود در صندوق‌های قابل‌معامله (ETF) رمزارزها خارج شوند، بیت‌کوین فضای بسیار مناسبی برای رشد و پیشی گرفتن از طلا خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147998" target="_blank">📅 12:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147997">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
روزنامه فایننشال تایمز به نقل از دو منبع آگاه از مذاکرات اخیر منیر با عراقچی:  فرمانده ارتش پاکستان بارها از رهبران ایران برای توقف حملات انصارالله به عربستان و زیرساخت‌های انرژی آن درخواست کمک کرده و تعهدات کشورش به ریاض را بدون تهدید خاصی به آنها یادآوری کرده است.
🔴
ایران می‌گوید این درگیری بین عربستان و یمن است، اما به نظر می‌رسد که تشدید تنش، اوضاع را به نفع ایران تغییر دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147997" target="_blank">📅 12:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147996">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش ایالات متحده:
نیروهای آمریکایی باید برای جنگ‌های آینده‌ای که فراتر از زمین و شامل اطراف ماه نیز گسترش می‌یابد، آماده شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147996" target="_blank">📅 11:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147995">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
قیمت طلا در معاملات روز جمعه بازار جهانی تحت تاثیر کاهش قیمت نفت و تضعیف ارزش دلار اندکی افزایش یافت.
🔴
قیمت هر اونس طلا برای تحویل فوری با ۰.۲ درصد افزایش، به ۴۳۴۶ دلار و ۶۵ سنت رسید. قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه دسامبر با حدود ۰.۳ درصد کاهش، به  ۴۳۸۵ دلار و ۷۰ سنت رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147995" target="_blank">📅 11:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147994">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsdJnqdQabWIOqMMAYgBbCVLuYyVzzM0xMUxcStp9iEoum4OPUnC6wijF5QwFVzPRjnujV_OBTvDGc0Adi_onLK6thPb2O3xJ4kya3G_aZrCj6dqYkT0JPkXfFfnx2acvfoFB-riAwvjQPzaj2GCeaVtnGGzsT9QNj73xPf5Z5EdfrVcO5D9p--jywKH-IVzbbdh2Bqb_uET-yzJIXCLs5NufmKHF3t0vFHlel_304dO6yduePmS1wNyfWgVxs0ZfzrgQzQXS29Iy02z0yQFJFJLHykJjwh3J7r_b1DKxyQZp2NgtDqCkskOi3nztvmqGD8cW02TPvlwbvZk0Y48ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران از جدول سرعت اینترنت اسپیدتست ناپدید شد
🔴
ثبت نشدن اطلاعات ایران در نسخه اوت ۲۰۲۶ لزوماً به معنای حذف رسمی کشور از این شاخص نیست
🔴
در حال حاضر توضیح رسمی درباره علت نمایش‌ندادن اطلاعات ایران منتشر نشده و بنابراین نمی‌توان دلیل مشخصی برای این وضعیت اعلام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147994" target="_blank">📅 11:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147993">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رویترز: جنگ ایران تقاضا برای ابرنفتکش‌ها را افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/147993" target="_blank">📅 11:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147992">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رسانه اسرائیلی از آغاز گفت‌وگوهای محرمانه میان کویت و اسرائیل درباره ایران پس از حملات منتسب به تهران به کشورهای منطقه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147992" target="_blank">📅 11:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147991">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
هند: از منافع اقتصادی‌مان در برابر تحریم‌های آمریکا علیه روسیه و ایران محافظت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147991" target="_blank">📅 11:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147990">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فدراسیون جهانی بدنسازی و پرورش اندام شب گذشته در فدراسیون بدنسازی ایران را تا اطلاع ثانوی تعلیق کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147990" target="_blank">📅 11:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147989">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
تسنیم: در جریان تبادل آتش میان نیروهای امنیتی و چند فرد مسلح در زاهدان، استان سیستان و بلوچستان، چند فرد مسلح کشته و نفر سوم بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147989" target="_blank">📅 11:19 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
