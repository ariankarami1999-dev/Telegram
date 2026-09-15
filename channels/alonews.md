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
<img src="https://cdn4.telesco.pe/file/vU0cYvg2ehFajBZI3vdfpz2vtLz407iAWJP-prkxAaFPuRfcmOjf3ZasNAdWKUsIZWylwET1i0NCFNiuPS1n29QNGUHYFKLq4yoXdz-c5JP1uFlwVGqwc0W-uFJgYP7X4U6gZe2ZHqWVqiPhQkUUVtxHN3RQ5ph6mVWxhtOLgpvBACSq2FgFv0K86-SmvEB0L8RuLkbE0Sw058dkdUntaZY03n6AfJMk5JLlk_RA96R4s4-tx-d3cX2XccIs_kUYpEWfId3pn6DV8BgXKqank0ulKemmOJ-ArEwYwyWO5CjufAW-5YKzv7I9GsTXIQoZrye-805k0NYhfwHrUyEI4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 918K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-147591">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789860f816.mp4?token=gC7XTRksSc_T8AARaVwwIAkjvLC4gVLExp73OFO9g6PyMmMNYk8FLYtj1OiVMnJVkuBezoIQyh8dpXcLE10aok1V_mgp1F1wfv1FiQ-eekhhutH0PKrmoDMKgpfbBjqKevMhaLLUxCJztay0dgdjdGyxqU7U1L9V3RIIqAyl--H_iqU6IKWS164meu2X4XS5rH0vJIwirpuxEmTT-_UunLxMxR7_cklGV1tOzMYBbqHA3R8ah8KizMYMnkHCD2UFa7hqNkabmQsdWpIkpfd8M0Jie5_39N5257_FIM8F-7Fai5CpW0oeDaOvWrCSnjWEL1PYHkSE-dqofXvPAY7Azg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789860f816.mp4?token=gC7XTRksSc_T8AARaVwwIAkjvLC4gVLExp73OFO9g6PyMmMNYk8FLYtj1OiVMnJVkuBezoIQyh8dpXcLE10aok1V_mgp1F1wfv1FiQ-eekhhutH0PKrmoDMKgpfbBjqKevMhaLLUxCJztay0dgdjdGyxqU7U1L9V3RIIqAyl--H_iqU6IKWS164meu2X4XS5rH0vJIwirpuxEmTT-_UunLxMxR7_cklGV1tOzMYBbqHA3R8ah8KizMYMnkHCD2UFa7hqNkabmQsdWpIkpfd8M0Jie5_39N5257_FIM8F-7Fai5CpW0oeDaOvWrCSnjWEL1PYHkSE-dqofXvPAY7Azg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قائم‌پناه معاون پزشکیان:
حساب کردم اگر بنزین ۸۰هزار تومان شود و برق و گاز و... را هم گران کنیم، می‌شود ۷میلیون یارانه به هر نفر داد‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/147591" target="_blank">📅 19:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147590">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1a4b63c66.mp4?token=EcXlohSuT32v7ERI7W5b9rjo-cxxkeEL6MS69rxRc5s-ThbxHYj_D4GSazn9YIOTR_p7Ani-PzLco8E7VqEQBTE225Odp8nuMS6yoeFNJkdXR1uMyE-GNEMK4DCcuROuuVV3DX56GpTF4QkxlOd8qxyJkPyg9Q4uJzudZj58X4MwiuU4MyuRI4o8zUD62E_TZ0yly7upvA6YoLolMBY3g9OzttiY9-oBEypqCQnrWFh3K5SI8agQ_ULov_JMc8QKnc0xq27Xl4kM3MxgYlFDVMNrU1SzX5IUOU2sht-ZWLhEoqrW6cOs5Q2xXUOft9TvStSefwYj5UNKS2upmIwfbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1a4b63c66.mp4?token=EcXlohSuT32v7ERI7W5b9rjo-cxxkeEL6MS69rxRc5s-ThbxHYj_D4GSazn9YIOTR_p7Ani-PzLco8E7VqEQBTE225Odp8nuMS6yoeFNJkdXR1uMyE-GNEMK4DCcuROuuVV3DX56GpTF4QkxlOd8qxyJkPyg9Q4uJzudZj58X4MwiuU4MyuRI4o8zUD62E_TZ0yly7upvA6YoLolMBY3g9OzttiY9-oBEypqCQnrWFh3K5SI8agQ_ULov_JMc8QKnc0xq27Xl4kM3MxgYlFDVMNrU1SzX5IUOU2sht-ZWLhEoqrW6cOs5Q2xXUOft9TvStSefwYj5UNKS2upmIwfbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از عشایر میخواست بزهاش از رودخونه رد کنه و تصمیم گرفت این حرکت شاهکارو بزنه
🤣
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/147590" target="_blank">📅 19:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147589">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رو کدوم سرمایه گذاری میکنید؟</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/147589" target="_blank">📅 19:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147588">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
اسکات بسنت در مورد ایران: ما شاهد فروپاشی ارزش پول ملی بوده‌ایم. ما شاهد افزایش بی‌سابقه تورم بوده‌ایم.
🔴
و به طرز باورنکردنی، در کشوری که سومین ذخایر انرژی را در جهان دارد، اکنون مردم برای سوخت‌گیری باید تا چند ساعت در صف‌های طولانی منتظر بمانند، زیرا مجبورند…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/147588" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147587">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bl2bbFVt6oGKTJcPZ5ikfsC5BdYKu645qmFX28ZRkq1o5fm2z6LTYI0x_vdCuK809sDR90pnIdu5cDUnQZGSBBrDLSTudt7bEYQtLPeL_pbdtvLlEjJ-LCZpLGm3ZqSHF93HwpXALepNKRX0gdyUTTWqP5BQVvjkzU_2II4osdTMYJpo2zONm35h2bje7nlZMV99KzabPaMZKF1m2ay2UvS_qFMmuKxY8cGMIfcQxT8b5yRB1MlqgJM5pKWUu7DcmL9IEh9lZUzjrLlKwPWbyE9QQJSsld-yFTGVRbyd30fhU1wj-MbK38rBMpP5spsXnFJXfZouYWCHldGosCX8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبلی رئیس صداوسیما:
همینی که هست و کارمون خیلی هم عالیه، هرکی میخواد نبینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/147587" target="_blank">📅 19:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147586">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09289cf68.mp4?token=QCEUm1K0dkXrR5lNWXPd27C3I-soOTjOomDtaXe3dgQVLB_5Hk5swQ8u0tya0KlKr-S1B7gREbT29ak10xLMcM2O67e-oNj3P0LJkGVtknnm0FWPhpaOvl_wNoLiMipWFD2h3ouFcP9gzx5Ox1Gst3UML3d3Rx4ultE7rs7MYv4paCeU8um9Fj5l-jw4w09hGTdEPyEXRgRXrSvfGFbKkX7huXyVQvph4N2pJpGoOItJXgvu4cC9tzoghX1lvX5yfs5oxoIiWiLGDP5xqiwIp6TdoBtakBoHVDZKQI5mw34mpB9Vv0HQ4pRr_AV0ysmmArZ1IERdG1lvxRqVTYZcfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09289cf68.mp4?token=QCEUm1K0dkXrR5lNWXPd27C3I-soOTjOomDtaXe3dgQVLB_5Hk5swQ8u0tya0KlKr-S1B7gREbT29ak10xLMcM2O67e-oNj3P0LJkGVtknnm0FWPhpaOvl_wNoLiMipWFD2h3ouFcP9gzx5Ox1Gst3UML3d3Rx4ultE7rs7MYv4paCeU8um9Fj5l-jw4w09hGTdEPyEXRgRXrSvfGFbKkX7huXyVQvph4N2pJpGoOItJXgvu4cC9tzoghX1lvX5yfs5oxoIiWiLGDP5xqiwIp6TdoBtakBoHVDZKQI5mw34mpB9Vv0HQ4pRr_AV0ysmmArZ1IERdG1lvxRqVTYZcfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت در مورد ایران: ما شاهد فروپاشی ارزش پول ملی بوده‌ایم. ما شاهد افزایش بی‌سابقه تورم بوده‌ایم.
🔴
و به طرز باورنکردنی، در کشوری که سومین ذخایر انرژی را در جهان دارد، اکنون مردم برای سوخت‌گیری باید تا چند ساعت در صف‌های طولانی منتظر بمانند، زیرا مجبورند سوخت خود را وارد کنند.
🔴
من معتقدم که این واکنش‌های خشن و تند که از آن‌ها شاهد هستیم، نتیجه‌ی یک موجود زخمی و در گوشه گیر افتاده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/147586" target="_blank">📅 18:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147585">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/147585" target="_blank">📅 18:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147584">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
اف‌بی‌آی: خنثی‌سازی حمله داعش در پنسیلوانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/147584" target="_blank">📅 18:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147583">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
👈
وزیر خرانه داری آمریکا: چون ایران قصد داشت بمب هسته ای بسازد، بزرگترین کارزار اقتصادی جهان را علیه ایران اجرا کردیم
🔴
تاکنون سه بانک کمک کننده به ایران را تحریم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/147583" target="_blank">📅 18:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147582">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
پوتین به دلیل تهدید پهپادهای اوکراینی، انجمن سیاست خارجی را به مسکو منتقل کرد
🔴
کنفرانس سالانه والدای پوتین پس از آنکه سرویس امنیتی او نگرانی‌هایی را در خصوص گسترش عملیات پهپادهای دوربرد اوکراین مطرح کرد، از سوچی به مسکو منتقل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/147582" target="_blank">📅 18:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147581">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
عربستان به مشتریان اروپایی نفت: فعلا نفت نداریم
رویترز:
🔴
عربستان سعودی به مشتریان اروپایی خود اعلام کرده است که به دنبال حمله هفته گذشته و تعطیلی خط لوله "شرق-غرب"،  امکان تحویل محموله‌های نفت خامِ برای اواخر ماه سپتامبر  ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/147581" target="_blank">📅 18:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147580">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsICjSmBqUDgMZ_m-tDgyfozYwK2inFPhlRV9YTz7Nh1I6oSHn-RINwwrVzLqM4IFBXtDrYWJqxwbjPK6kIsQfdiaIkYaktPnsX9EBzUjQ6mQn6Mc0Qm28WRLcpixvpbxLENfAoC0g3gfBe9KY6O4bg4YtUnlIv1kCgApNyjEzCcG66A2vMPYXiBGMQypDXpRide7DY7NtO-_VNHdQkfJ8LVCrRNbZdqxqrT3NQ1sXa_TVDhEUzqMHLZ9bcM-YMSqWM7LX-tFQoZ2qP5zAVWGuvU9Fei8AwoCCRXCzJoSQme2S2tQXKR20wvuXTlambpyG7loQlqOKfi2VOt8nwJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/alonews/147580" target="_blank">📅 18:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147579">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d827e0ad6.mp4?token=XP7gHOK3l5qYdo0gZ5H5gbXqQLYkcyS7WOaFGVS_LsCS-VXrqXX1fmpZR3mnuuLXW-aBtXuzDjOtDEdAvmwqjuV8P_NEk30q6JcwtElheJ7AeplMF7qpYQswPJ0aMZToKvKNKrmiIH5a1WeQV9fY-Uz0W5AsLXAuI04TG_uSDDr8wN8ZWwbn7JOktiqV5B2EarBLfLGyF3IK0ne7U6gKi7gDII2MhAx_XUq8hzKa5E2o4QAB538pDMnp1a0l03h5iVwu4jGMe7FTYchJtGcvl54d45bvbsJGnTLON6qyWaUtw3ZP8j1PpeV-u9n8imjUoHHDumbLwh29RqLs0r8M0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d827e0ad6.mp4?token=XP7gHOK3l5qYdo0gZ5H5gbXqQLYkcyS7WOaFGVS_LsCS-VXrqXX1fmpZR3mnuuLXW-aBtXuzDjOtDEdAvmwqjuV8P_NEk30q6JcwtElheJ7AeplMF7qpYQswPJ0aMZToKvKNKrmiIH5a1WeQV9fY-Uz0W5AsLXAuI04TG_uSDDr8wN8ZWwbn7JOktiqV5B2EarBLfLGyF3IK0ne7U6gKi7gDII2MhAx_XUq8hzKa5E2o4QAB538pDMnp1a0l03h5iVwu4jGMe7FTYchJtGcvl54d45bvbsJGnTLON6qyWaUtw3ZP8j1PpeV-u9n8imjUoHHDumbLwh29RqLs0r8M0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
یه خبرنگار داشت جلوی سخنگوی وزارت خارجه، تخماش رو میمالید
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/147579" target="_blank">📅 17:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147578">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12945af81.mp4?token=gsybzTfMI_k9WOkfg1ri98NVPNZn22LRODp3Gm6_wtDZhQVESDredgI30X5MUbwGdtAnCfYUzfn8OQI_jcEKonOyXFnjWv8rGr_gjP-lHogkbIV2tZvR7dJfEqNZ-S6H0RTnXDseyRcEz43OiXek51HihA4lVi5Bnf5Cmt0cVNaDiYB85G451nUuoYx_GRHXPoKoTDb_IyhMxA4E4fLWH3czcfXJ7ra-5rTMKHWNA3vOslLlqRzrMXwqa6KSXNgp9xr6c_LmQ8FiylxAbVqrN0TxwwP-ATwlpZclsveKiuve6Q7vwXRezgHdgQ4hJiNiJnTQQdkceiajo7oG8EbISQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12945af81.mp4?token=gsybzTfMI_k9WOkfg1ri98NVPNZn22LRODp3Gm6_wtDZhQVESDredgI30X5MUbwGdtAnCfYUzfn8OQI_jcEKonOyXFnjWv8rGr_gjP-lHogkbIV2tZvR7dJfEqNZ-S6H0RTnXDseyRcEz43OiXek51HihA4lVi5Bnf5Cmt0cVNaDiYB85G451nUuoYx_GRHXPoKoTDb_IyhMxA4E4fLWH3czcfXJ7ra-5rTMKHWNA3vOslLlqRzrMXwqa6KSXNgp9xr6c_LmQ8FiylxAbVqrN0TxwwP-ATwlpZclsveKiuve6Q7vwXRezgHdgQ4hJiNiJnTQQdkceiajo7oG8EbISQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ترور مولوی یوسف در زاهدان توسط افراد مسلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/147578" target="_blank">📅 17:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147577">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اف‌بی‌آی: خنثی‌سازی حمله داعش در پنسیلوانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/147577" target="_blank">📅 17:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147576">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
👈
وزیرخارجه عمان و مارکو روبیو، وزیرخارجه آمریکا در رابطه با تنش‌های ایران و آمریکا و تحولات منطقه گفتگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/147576" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147575">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
خبر خوب برای معلمان
🔴
کمک هزینه شروع سال تحصیلی آموزش و پرورش برای معلمین واریز شد.
🔴
هر معلم ۳ میلیون تومان
😘
😍
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/147575" target="_blank">📅 16:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147574">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqv9sdJJqOamRVHQDfkN-Bp3HrECmHateAAQLxRAmYKpeFe2dKkQxBC9s0maAWRofCjYR56maNoQK49C0pIVC0Vopkpyi_RDkr4J42oU9wuyoLEDiOplHSDxWZn_hs4ezL5Dze6QiunC6nLnY5t_4vwy2ooCXna11-lmTsDiLmyJjS9nwjhnOZS_jo6qiZuDwfRZTKAUWYgG93G0gYUpC-JXX3QwfwXCSSJ3Nt88B-eLI0rNoVjY4_wrDWLxbQSYMSRynwKyowsIyV7ciaKpTdL1lscJc8GFMiT-eopqr7SvhCl1frPVdeHUbvFVRWryaJHqbhV2Y2qcyPkdq6Jl2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: اونایی که از لاله مرزبان حمایت میکنن ربات هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/147574" target="_blank">📅 16:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147573">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تحلیل عجیب هوش مصنوعی از دلار و طلا
😳
👇
👇
👇
👇
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/147573" target="_blank">📅 16:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147572">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
دو قایق کوچک ایرانی روز دوشنبه پس از تلاش سپاه پاسداران برای توقیف یک پهپاد در حال گشت‌زنی در تنگه هرمز هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/147572" target="_blank">📅 16:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147571">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/52bc7ce3db.mp4?token=I9XAV38mQu4JcGN9VdfMW8y-vTSoW4KJtGnqVrMRtauLFcDKBF7OZg0wUl2u3e_SONyWhHMGWSY8mDJoIAiIgPR8fikglGbkcXCvjYPoQ-Yqf4gVweQdXhVB_Ul_3d1ed2nrKK2QyVNiQ8azVpb5agDEvx5wCmDjSSB5AyrMlAY4p12HM2I1CyRrG33Lt5FIeuuapwubh7pW9DjPo4L9yoYs6mZk5x7aj6zuH-keQVs_fgp9pukiPzVXt47Hd3lVAJQFs3NGvrm8AUHHaJqVRPsKoIlIrrAxLIpm4z859PdZFIQg4oqXgkxjbuIKmrVLiQLDT1z960YByqaXbLu_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/52bc7ce3db.mp4?token=I9XAV38mQu4JcGN9VdfMW8y-vTSoW4KJtGnqVrMRtauLFcDKBF7OZg0wUl2u3e_SONyWhHMGWSY8mDJoIAiIgPR8fikglGbkcXCvjYPoQ-Yqf4gVweQdXhVB_Ul_3d1ed2nrKK2QyVNiQ8azVpb5agDEvx5wCmDjSSB5AyrMlAY4p12HM2I1CyRrG33Lt5FIeuuapwubh7pW9DjPo4L9yoYs6mZk5x7aj6zuH-keQVs_fgp9pukiPzVXt47Hd3lVAJQFs3NGvrm8AUHHaJqVRPsKoIlIrrAxLIpm4z859PdZFIQg4oqXgkxjbuIKmrVLiQLDT1z960YByqaXbLu_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند بوئینگ ۷۳۷ شرکت سپهران در پرواز مشهد ـ کرمانشاه، پس از برخاستن با مشکل در یکی از لاستیک‌ها و احتمال آسیب به موتور مواجه شد.
🔴
خلبان با اعلام وضعیت اضطراری، هواپیما را به فرودگاه مشهد بازگرداند و هواپیما به سلامت فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/147571" target="_blank">📅 16:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147570">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اسرائیل هیوم:
منابع دیپلماتیک تأیید می‌کنند، اسرائیل به عربستان سعودی در جمع‌آوری اطلاعات علیه حوثی‌ها کمک می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/147570" target="_blank">📅 16:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147569">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1m4cHwIp7tbIrU5z4GCriukZd90iIQ1asWPjElgH41GuydBnIE2glrFmn1dMMkejB4UjprLl3mCS2q0tBJf3qATVcg5spOoVCSzD9-6WhbJ0IQPYFXC4X_W2EZhFyHoZO0frvKnSxg4-fQA2pbMmNZoZ2k-yODj7lTzbaiypvJwV-oNEl_vvRQuf_83JubPfpeE00M16BLSG3te2HS1R1JsfkXniaWQ5_Ws1c9mjXYarmTP24T3yuKvtdoSs04YB5SZ4o5ur0XlILaSQy7HjaM5DsPLUMY1Za7Mmmxv-DuB5WPIMS0Eolwc4pmQcd31k3qu3Mp_G_rfekHGOEdFHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ایلان ماسک:
هرکی بازی ویدیویی نکنه احمقه، بازی کنید چون برای مغز خوب و مفیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/147569" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147567">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYCkTSqo8dRUepjONtuDxyTrwrVs_Jz9AfWyEIZovaCcq_c-YcS1nZDA8oZQOG3omHM-xHrXqvd8i7ahf5h2plC9rk0va-TLQKvVHjgV6EY0B1U22ObKuimwxHxeHpc0blJxOn6HCw5PSv2GhRfaPlTGiF-3ah5KiIOhIfU6XNtqJPX2Cdb6tQnkl-IwJpeu-Xw0k3ktM6G9hEENf63YrBpEsOM5FJosrnt09vNjIIXA5OzjGfNbcKmCofnDzaDBM8AaBxbvYuNj16sGRZcdC-L0GgZFJBgLnNfwWhJXsez6zRZmSGgyZNSs0Mnrk7tVeKIdqutNiuuuYxcp5Dmubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSHlpjs96Jr5YhQ0hyoCRlThIB3hKSKbnW5F1lZkcznmaZb1XHTvTfe69ylMuP53YtRvYxNmG79FPqP2FGm2yEjtEworKj40DWXYdZGYyngwRhtvEuOH-DbD4k6I4nwJUAde-qpPqZGxdfOZpMn92molNeTwtPAuMTOK8IDjy_FAA1ke7nEXT261lQmvtKGVRRnga8XXqWvvN6TzyRshi55xiO-iRI9GA8b8UmT_LYeyOf1O-hkiahgL1nJAjT1PK-S37gbaVkrMOqzdPCfTZCq5PCMg46qOzbv4BWZswsEikYY1j35R8dIWOgzr30Y6ZKgGxNnxwdwdNmNEsCEyOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
نیروهای اسرائیلی در جریان عملیاتی در اطراف
کفرشوبا
، یک سکوی پرتاب و تعدادی راکت متعلق به
حزب‌الله
کشف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/147567" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147566">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان: اکثر کشورها از آمریکا حساب میبرن چون ابرقدرت هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/147566" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147565">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
عمان: در حال پیگیری روند انتقال نفتکش مورد حمله واقع شده «ال گایا» به یکی از بنادر هستیم
🔴
۲۳ نفر از خدمه این نفتکش را خارج کردیم؛ جست‌و‌جو برای یافتن ۲ فرد مفقود شده ادامه دارد‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/147565" target="_blank">📅 15:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147564">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAK9j22YkpJiqK1DX_VCti9LPcqfcZWBlUkqjUt1KN4AjJhp8waqHJ_ZBi4XGcrcs8TZxSwLfGJLq8x08zti8CbPDjWzJtodkbVcTMZk_lYMJxsPyGHv94zayf7uoOE32u-6jkos3ks0dQm68H-9-ZUEXr_yWKN57OK4vTuO1TK7DdK0kXCmNc4zXMSUIaZzAP4JhqPN_8IyruIjyV5Kr_7itFQDKcnmZv6WxgRJwJGEAa5tusJMAlCxTxcYH0tWgJgDg72KevVckyoM-d3B5_dY1Dp34m2-xtZ9ke012__nm4Q-HNa-6uvh51NEJGYD0KP5-bMDANYirLFTPltxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از کفر تیبنیت در جنوب لبنان پس از عقب‌نشینی نیروهای اسرائیلی از این منطقه به سمت قلعه بوفور
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/147564" target="_blank">📅 15:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147563">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed891a24b.mp4?token=Zunjbb5X15MYN1KWtqvu9w2G_8pHnMRNqQfIJQIR3C7ANkeE-zbVBUPIRW1F8192eKzGGKXzlW6eZ02l7ACsCr2iUYskrSz08_J6dLRLOfSyxao-XzXv7IejzZ0tWsiMiPcfEvXWUhbKR0x0xUtHalJcKm0EE4Mv_rHhFGIGgZUrlvVSUxNBBijvA5-9EI2iVCa39JfSKGRfuck9EBKoZYyYsEp0OaJtYXFBJIIGScwCytqEyefURfDVPdPVgjR8UCbwBDv9yaqL762Myl6Lrrkdpu-ybJ9d_TDyQ-hDTqd3tEJVy1oDNOwCalpjeU7UbUD_YsZScwfyGAK0uXohEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed891a24b.mp4?token=Zunjbb5X15MYN1KWtqvu9w2G_8pHnMRNqQfIJQIR3C7ANkeE-zbVBUPIRW1F8192eKzGGKXzlW6eZ02l7ACsCr2iUYskrSz08_J6dLRLOfSyxao-XzXv7IejzZ0tWsiMiPcfEvXWUhbKR0x0xUtHalJcKm0EE4Mv_rHhFGIGgZUrlvVSUxNBBijvA5-9EI2iVCa39JfSKGRfuck9EBKoZYyYsEp0OaJtYXFBJIIGScwCytqEyefURfDVPdPVgjR8UCbwBDv9yaqL762Myl6Lrrkdpu-ybJ9d_TDyQ-hDTqd3tEJVy1oDNOwCalpjeU7UbUD_YsZScwfyGAK0uXohEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.
🔴
از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/147563" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147562">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رو کدوم سرمایه گذاری میکنید؟</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147562" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147561">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9fnLYGxoPXclzxnNdoEAhu98EQgIcEZfnrkEAhXbAyk4Ed5-BgiD7921Y7C1vlAf0fG_JEyAYAf8au25C2vvkKJhpVY6uLf28UMql2sAZYZialzUzp-6N2t8H9qFdKdXFinJCXe-AlVEV0dw_IaVEkG0WCKSTzEl_I5X5-nM5wRSs7ZfFd1DEv0p_-HYHAvHd367aJlScD5lvrsDaAMSS64yQZBKuaPJFLcky-8Dz3JsaNQ4jV-SyqM9CbswY2inEpEW54j3gGbWuWGOiZyjBStKkjDI6jcxXCizBYeqz8Thow3bWVdg4twdLiKUBg6dGrabdncqc3jdCpGAHI2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147561" target="_blank">📅 15:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147560">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vsax67SpOWYgVQTb1eyy9CtQ661fYhRGlNP-BPMo9k-jZPTPT-sX6MlH_yA07iif_IuholY7T1MiAtWgnsF7uDlSqaZSYBtyaH7AmWij_NjsNNU4SeptZ2WcH1dIjJ1pkphy_U7cgHYMnzWcaqpB61gFX31CDpD5u9Ms_ArUxPIzNsF3DjfJizMWBkZa4P27p9R0_fmFoVBrT3Yba8GBbCpT2b-nXetBNSLPpJGp6ygPIk5G44AMWScd9QW7z9WHrxBD1Mez-5GWgDg-dhbUKbbr3B6VZVPZYe-U26BxBiZAYC_CVl8uazgL1KvkVqnxqtOkuv3ve5ESbRaU2m_Eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس نظرسنجی‌های رویترز/ایپسوس، میزان محبوبیت رئیس‌جمهور ترامپ اندکی افزایش یافته و به 35 درصد رسیده است، در حالی که این رقم در اواخر ماه آگوست به پایین‌ترین حد خود، یعنی 33 درصد، رسیده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147560" target="_blank">📅 15:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147559">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
هاکان فیدان، وزیر امور خارجه ترکیه:
امنیت، ثبات و رونق ایران، به طور طبیعی و مستقیم بر منطقه ما تأثیر می‌گذارد. از این رو، ما خواهان این هستیم که این درگیری موجود در اسرع وقت از طریق راه‌های دیپلماتیک حل و فصل شود.
🔴
افزایش حملات متقابل در دوره اخیر، به طور جدی تلاش‌های صلح را تضعیف می‌کند. این اقدامات که باعث افزایش تنش در منطقه می‌شوند، باید فوراً متوقف شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/147559" target="_blank">📅 15:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147558">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a03d9b86.mp4?token=ETd-EZnh31REN_btMEcZOXAnkms0WUZmZpvLE7HKAN0r3f5nzLlphpdBXjnEJMdM1MrswHZtD7_-Ah0etatkobVh6JW1W2_dJIzgh6qx0YeVIGHOHHJHIQfc9KHcQ32rPbevxk0DPDH6sMTYsaS2sMnP7FmQkheL2tyFFmXfPCz40iUdw4Q6EX3uCEJJtmBTikpQ8tSb4LyMQiAYMqOqai6OJ8HxMwxOX15fJvSglT47fpEQLuKnk6TyzfPLNzdLytfx6v_J9fzboj7x9sOC5ShJm-dqUVj77V9YDXLq6rRApzd9WgVnzX3eAxgWz0GSWJr6j6HP3Hyl7KxNyM9jQUu3PHA0Wa2OqItbFOgF8ihS2BZN7AcSyIOuX26I6AKUwud3Kvy7gBFqmF24yr1klxmXYdHINnnofCu6oePJdPiseSLeBVbhletrT87vQvIPJB-1m2Yn2TQWTgAa5Govd_v5tZYpatfztO3a_QcEfAYsHluJk9Kt1JLs7_fZtUJ4ALxmIx3FMoe6rUEodzK5P8VouerAy-BAkAEgXjQft61bKopo3jTDK5jRX1bEZneLBgn-aKxnnRuFkPtmf6PvYr3ye2rxSTaoEUxY4H2ik3rIhzXM5KIw7GKxZ5M_gll3wWJtTbop7DTrzdxoOiNPBH4PQgJ-564p80tuR-ufEj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a03d9b86.mp4?token=ETd-EZnh31REN_btMEcZOXAnkms0WUZmZpvLE7HKAN0r3f5nzLlphpdBXjnEJMdM1MrswHZtD7_-Ah0etatkobVh6JW1W2_dJIzgh6qx0YeVIGHOHHJHIQfc9KHcQ32rPbevxk0DPDH6sMTYsaS2sMnP7FmQkheL2tyFFmXfPCz40iUdw4Q6EX3uCEJJtmBTikpQ8tSb4LyMQiAYMqOqai6OJ8HxMwxOX15fJvSglT47fpEQLuKnk6TyzfPLNzdLytfx6v_J9fzboj7x9sOC5ShJm-dqUVj77V9YDXLq6rRApzd9WgVnzX3eAxgWz0GSWJr6j6HP3Hyl7KxNyM9jQUu3PHA0Wa2OqItbFOgF8ihS2BZN7AcSyIOuX26I6AKUwud3Kvy7gBFqmF24yr1klxmXYdHINnnofCu6oePJdPiseSLeBVbhletrT87vQvIPJB-1m2Yn2TQWTgAa5Govd_v5tZYpatfztO3a_QcEfAYsHluJk9Kt1JLs7_fZtUJ4ALxmIx3FMoe6rUEodzK5P8VouerAy-BAkAEgXjQft61bKopo3jTDK5jRX1bEZneLBgn-aKxnnRuFkPtmf6PvYr3ye2rxSTaoEUxY4H2ik3rIhzXM5KIw7GKxZ5M_gll3wWJtTbop7DTrzdxoOiNPBH4PQgJ-564p80tuR-ufEj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: عموی من احتمالاً، به طور خلاصه، یکی از بهترین‌ها در تمام دوران بود. او ۴۱ یا ۴۲ سال در دانشگاه MIT تدریس می‌کرد و به عنوان یکی از باهوش‌ترین افراد شناخته می‌شد.
🔴
بنابراین، من کمی از نظر ژنتیکی قوی هستم، اگر به نظریه منابع اعتقاد داشته باشید. من به آن اعتقاد دارم. من از نظر ژنتیکی برتری دارم. من در مورد هوش مصنوعی (AI) اطلاعاتی دارم.
🔴
ربات‌ها جهان را تصرف نخواهند کرد. هوش مصنوعی نیز بقیه جهان را تصرف نخواهد کرد. کل این موضوع یک فریب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147558" target="_blank">📅 14:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8ae5f579.mp4?token=mLVzkp1GsXJyQumudsXDzPRcJIbjIDilGUWzdu6O-2NPuUStYbuVrg7aqZa8fOAR4ahUZWA-9FxZVvos8UrZa3xcC1iA-k5ZjQobADyXEVwa8jmzl7dJbr9VKq24rVRr0SLyNC9jUWpQy-_Jn8nvZN8cGFO0mJgNd5Vyyo2Bmt6wLi15EsoI9iDgQlPddwxDVuaGE9S2MUwLcE63Y6mYwyPea4eBIQJRZSjW_nxwKMsbZ4PtSSpr99Xfx9lLbqz-9ZvnM3Q4j0_bMCpooxx6tqGJwFuqw8TBLjlU34UVUyTZH8d6HpD7TQ2JGjMrqvVAIsDZNMgNTtBP2KS7-ZukuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8ae5f579.mp4?token=mLVzkp1GsXJyQumudsXDzPRcJIbjIDilGUWzdu6O-2NPuUStYbuVrg7aqZa8fOAR4ahUZWA-9FxZVvos8UrZa3xcC1iA-k5ZjQobADyXEVwa8jmzl7dJbr9VKq24rVRr0SLyNC9jUWpQy-_Jn8nvZN8cGFO0mJgNd5Vyyo2Bmt6wLi15EsoI9iDgQlPddwxDVuaGE9S2MUwLcE63Y6mYwyPea4eBIQJRZSjW_nxwKMsbZ4PtSSpr99Xfx9lLbqz-9ZvnM3Q4j0_bMCpooxx6tqGJwFuqw8TBLjlU34UVUyTZH8d6HpD7TQ2JGjMrqvVAIsDZNMgNTtBP2KS7-ZukuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
ربات‌ها قرار نیست جهان را تصرف کنند. این اتفاق نخواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/147557" target="_blank">📅 14:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147556">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عمان: بحران تنگه هرمز به زودی به پایان خواهد رسید
🔴
حمد النعمانی مدیرعامل شرکت گاز طبیعی مایع عمان (Oman LNG)، امروز سه شنبه گفت که بحران مربوط به تنگه هرمز به زودی به پایان خواهد رسید.
🔴
وی در کنفرانس بانکوک گفت: بحران تنگه هرمز طرح‌‎های درازمدت این شرکت را تغییر خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147556" target="_blank">📅 14:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
آمریکا به دنبال توقیف ۶۱ میلیون دلار از دارایی‌های نفتی ایران
🔴
گزارش‌ها حاکی است آمریکا برای توقیف حدود ۶۱ میلیون دلار از درآمدهای نفتی ایران که به شکل دارایی‌های رمزارزی درآمده، اقدام کرده است.
🔴
در این پرونده نام دو شرکت چینی و صرافی رمزارزی بایننس نیز مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/147555" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147554">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کرملین: روسیه معتقد است فضا باید عاری از تسلیحات باقی بماند و امیدوار است از طرح خلع سلاح کامل فضا حمایت گسترده بین‌المللی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147554" target="_blank">📅 14:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر خارجه طالبان: هم جهان اسلام و هم غرب از ما می‌خواهند مدارس دخترانه را بازگشایی کنیم، اما نباید با نگاه غربی به ما نگریسته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/147553" target="_blank">📅 14:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
طلای جهانی در آستانه تصمیم فدرال رزرو درباره نرخ بهره، با افت جزئی به ۴۳۰۲ دلار در هر اونس رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147552" target="_blank">📅 14:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147551">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رسانه عبری والا به نقل از منابع امنیتی: تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند
🔴
نگرانی‌هایی در مورد اینکه آمریکا با ایران و حوثی های یمن به تفاهم برسد و سپس عربستان و سایر کشور‌های منطقه را با مشکلات حل نشده خود تنها بگذارد، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147551" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147550">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کرملین: پیشنهاد ترامپ برای برقراری آتش‌بس در حملات به تأسیسات انرژی میان روسیه و اوکراین، «ایده خوبی» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147550" target="_blank">📅 14:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147549">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💢
رو کدوم سرمایه گذاری میکنید؟
💵
دلار
.
🔴
طلا.
🏠
ملک
💸
بیت کوین</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147549" target="_blank">📅 14:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147548">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX4riMRkXXrbLGuv-r4DdiBztnmzmGBaTG2i5K5pXPdZP7YjSMEhTHxLOZq9q-EhE-z1PaVuw5UhUZtosCv0bXGtk0Vp3PFMWtJSBYkDOOpXcwUCgld_fkj2Nh6NPIj4lfbAXtCNWuYC48FV5SNDRBzL8-wnbhSfdxzmEoAPQXFkSDbTgfkOQd7Mjz_5_-EJc1VQUtnpm-baZbPmncKZFzfEF80tRBR-4qkmtz9_YiGv7kPz2JxaH7sULTTn-muZ-IyDwvgaYbqF7KlVmrpUu1sRdXx3UBKbsbHkT64xucXsZI9SmZXE0ePl2tWwXoIMggXAkCzQXRiJjOX367OddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کرایه روزانه یک ابرنفتکش از خلیج فارس به چین برای نخستین بار در تاریخ به یک میلیون دلار رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147548" target="_blank">📅 14:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت خارجه قطر: دولت قطر با جدیت و همکاری با شرکای منطقه‌ای و بین‌المللی خود برای دستیابی به توافق درباره تنگه هرمز تلاش می‌کند.
🔴
دولت قطر با شرکای خود برای پیشبرد گفت‌وگو درباره امنیت کشتیرانی در تنگه هرمز همکاری می‌کند.
🔴
دولت قطر از دستیابی به توافق درباره تنگه هرمز و توافق طرف‌های ذی‌ربط بر سر یک راه‌حل حمایت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147547" target="_blank">📅 13:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عمان: ۲۳ خدمه نفتکش «الگایا» نجات یافتند؛ جست‌وجو برای ۲ نفر ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147546" target="_blank">📅 13:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147545">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
چمران شورا تهران: ما تو جنگ میریم رو پشت بام، ولی نتانیاهو میره زیرزمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147545" target="_blank">📅 13:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مرز چذابه بسته و کامیون‌ها پشت برخی مرزها متوقف‌اند
🔴
رئیس انجمن شرکت‌های حمل‌ونقل بین‌المللی ایران:مرزهای مهران و باشماق بازند، اما در خسروی، میلک و دوغارون ایستایی کامیون‌ها وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147544" target="_blank">📅 13:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147543">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آخرین قیمت نفت: ۱۰۸ دلار و ۲۰ سنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147543" target="_blank">📅 13:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147542">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
دفاع مدنی عربستان سعودی: هشدار رفع خطر از شهر مکه، استان طائف و استان جده اعلام شد. برای حفظ امنیت خود، همچنان دستورالعمل‌های دفاع مدنی را رعایت کرده و از تجمع و فیلم‌برداری اکیداً خودداری کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147542" target="_blank">📅 13:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147541">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147541" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147540">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پروازها در فرودگاه طائف، واقع در شرق مکه ، متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147540" target="_blank">📅 13:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147539">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPTBsCIAAwsP3AWlY5TvRR9jMipkV21fvJ6bQDjUcPuQaoZzr9fckIG2sK4ZNmzN0lWxs6b4eVKhACnUmXgrVCdYnV9xdkSijhftjPyWwrTokCG76ry5sj501kLx3zl-UKCl8AacrqCTU2i5QwIgeQnnzy_fUXjDBAwp8Of_OY7wWnVFsVdilgrZ1ad2ZSkbGXfeMa2NvfNn-rbnNMthz6DburMzp8LfX95hJYfXISOnsAbUvDQNNCm3Mkdtvow_Wfzjfz8Nt2rAvwm7yDVcLACRjFFhG3y61N-LzUg957u_s6aTIIzQsiKBa-bs4A4wAd25QCOGT_DjzQYlBwYNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروازها در فرودگاه طائف، واقع در شرق مکه ، متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147539" target="_blank">📅 13:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147538">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
برخی منابع عربی از وقوع چند انفجار در شهر طائف در عربستان سعودی خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147538" target="_blank">📅 12:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147537">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی درباره هدف قرار گرفتن یک کشتی با یک پهپاد ناشناس در تنگه هرمز دریافت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147537" target="_blank">📅 12:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147536">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5knPYk10nFRg0rvq-HZEe0YL5uXajeL7-RVqwiPBFhXHulwNUOBt3FF2n0uti4Iz8g3Kz-KUr2mw2O-_aUwQhNLoM93TXKUrKi5Z1VW83BuhopHvcEcFOVaZ4d7gcmMIBJbrEGCxZ5L5yxYRYdsATL_LKyTB1jivLCVGayiP7HhdYoG5nR38tSW-IZNwQ1sgR9giowid7HdGr8vh_UgnN-guKf0_Q0uRTcCA0DzADU4O7kNz_-hED8TjUJx2MnCoFI-yjdGZDepPfbRUpJmGmvUygEJiN02BUJHfD4cATDvhrKI9orW0wRdj_WtkbjH6PF9IqCaaAORv2-zaJFgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه طالبان: هم جهان اسلام و هم غرب از ما می‌خواهند مدارس دخترانه را بازگشایی کنیم، اما نباید با نگاه غربی به ما نگریسته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147536" target="_blank">📅 12:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147535">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147535" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147534">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147534" target="_blank">📅 12:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147533">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ویلیام لارنس، دیپلمات سابق آمریکایی:
مداخله آمریکا می‌تواند به طولانی شدن درگیری یمن بیانجامد
🔴
واشنگتن می‌خواهد از کشیده شدن به درگیری‌های منطقه‌ای بیشتر، اجتناب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147533" target="_blank">📅 12:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147532">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbV4f8GRgsy8kJdQDXmRvpbZzRSrZ3jOlqttfojrnx1fwYaqwF9Yj0pcG06kPQA1a55i5ASG_Ow8GSNGnFORLbHvwfTW0rhreW6PD-so94nsntlwfPksW5jl9iX-vPbfW_VH9sL-Vi3fKM_izYZ44BH2Y3wYy1x8aETIF-eprXqNCvTJ_wnwHfhJk1D-ys9EVq5Sq1Mk9gFVqyrxOgyWIu0V4Kwfi3wybVqQMm5QIkmiQtuzJNSa5L2CsfquoeBSmeM9BmgpuI34aowAUWCbfrL19Yp8U4HCwupUU328tbDUwFOjiMjfLHA_xLSON7ZKSV_Hw5lRi3w7Xl0Lwy7-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین زیر ۷۷,۰۰۰ دلار سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147532" target="_blank">📅 12:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147531">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کره جنوبی و ایالات متحده درباره اعزام احتمالی نیروهای نظامی کره به تنگه هرمز گفتگو خواهند کرد
🔴
به گزارش خبرگزاری یونهاپ، کره جنوبی و ایالات متحده این هفته مذاکرات نظامی در سطح عالی برگزار خواهند کرد تا درباره اعزام احتمالی نیروهای نظامی کره جنوبی به تنگه هرمز گفتگو کنند.
🔴
کره جنوبی هفته گذشته تیمی را برای ارزیابی وضعیت امنیتی در نزدیکی این تنگه به امارات متحده عربی اعزام کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147531" target="_blank">📅 12:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147530">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز :شورای امنیت سازمان ملل امروز درباره وضعیت تنگه باب‌المندب نشست برگزار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147530" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147529">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
عراقچی،  روز ۱۶ سپتامبر (۲۵ شهریور) به چین سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147529" target="_blank">📅 12:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147528">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEOLQ5legS1d3aBOEgVjZXY6e6hAUM8H7oLxyPRZX6MKIszyTMXUpY-u2j0FYQvgHIZuBGHlR3xqinun_kS8CbX6Osejcg9t3_7Jn2qnM9ZRHriRYHoZMJlaWYMzSKuXA9Hq5jwv9RLgqTakfNWAOmxVQgt_2RCitqxaTVIv4zIeEwd7J7cMyyxG-Nt174Nf8SaRhRlafoeztE-9wqMXq0GRjfZyZ-2zjp-Mp7qQxOMrGnoUnotvR8pjLw2K9A0qvATbGTSSkdQvJbkfXqKWsGvT_v1tsiajOf9e4t1J9lHKgwjB4UaiUAAqBhieUR9xWovMI5ymgW8nfA9mPifQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحرک هواپیماهای سوخت‌رسان آمریکا بر فراز کشورهای خلیج فارس
🔴
حدود ۵ فروند هواپیمای سوخت‌رسان آمریکایی بر فراز کشورهای حاشیه خلیج فارس در حال فعالیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147528" target="_blank">📅 12:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147527">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFSCeNm-eN91j8rGFG4GjQZNIAkBgFLqybcpq9xrlzGIv3BlxqGH0vD_ObmQcZOv17DGtVr7KUyey4KQ-rlEzurvXbA9eFIjYBmhuEUhLqMjxvRzg1YRFpkfpUaYq19FElOTlBwiQQh-mXOCwIDsPrP5ds5sJu7wdNY1E-P3vAGGU-huQj-yffQILTUukhQ1TzyGnXLU7xl4L9X175FvPzfdxxYoRG-Ir2EXerrojfRbiYm24ifqmD9PW3T6EgA7K_M7KlkULoCeWF9xdJBZkJCSuNAPYoYZBa3ArRduEE6CnfWIzPDH6IPJNTZrP2_5_7OqAFlpMBeRwpnROP9ebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت حمله موشکی یمن به شهرهای ابها، خمیس مشیط و طائف عربستان سعودی را به شدت محکوم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147527" target="_blank">📅 11:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147526">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8539665416.mp4?token=DpDdqlKvtxEY9wgeksns8sVzRZhRufq3wo82wfoi9yQL8ZEvl7PXO4UgD4cfFaQzk6AsPnXDWEKD9NPgyy4cmMsMQSXXU86yNEJ8qORenB2CFjbv7r-Ln_03gNrbstMSLsU2wYVUEl-wll0LQ7_bAeF9o_8Z-blA9xCdwV5o1b-7Yi2iMv1EHxRJ_i6miC1yLnnKi7HN6we2gg1Y5-6QOSQ7MUE7DRy3LK9FzkIyo962RKW6iJ1yBSkCGJM5UcCBJYJLeChDQyViSXxgqJFvrzgMF_E7vaNKGiTZnEFs-s7VwZCxlWvsURifBKfkSl8p1U3iDbhd0tguVB69peqyHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8539665416.mp4?token=DpDdqlKvtxEY9wgeksns8sVzRZhRufq3wo82wfoi9yQL8ZEvl7PXO4UgD4cfFaQzk6AsPnXDWEKD9NPgyy4cmMsMQSXXU86yNEJ8qORenB2CFjbv7r-Ln_03gNrbstMSLsU2wYVUEl-wll0LQ7_bAeF9o_8Z-blA9xCdwV5o1b-7Yi2iMv1EHxRJ_i6miC1yLnnKi7HN6we2gg1Y5-6QOSQ7MUE7DRy3LK9FzkIyo962RKW6iJ1yBSkCGJM5UcCBJYJLeChDQyViSXxgqJFvrzgMF_E7vaNKGiTZnEFs-s7VwZCxlWvsURifBKfkSl8p1U3iDbhd0tguVB69peqyHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک درباره هوش مصنوعی: «اگر هوش مصنوعی بتواند کنترل سامانه‌های نظامی را در دست بگیرد و مثلاً یک سلاح هسته‌ای پرتاب کند… این اتفاق بدی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147526" target="_blank">📅 11:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147525">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DGdmsirTT6pm2MAYFgWSxHtNDqFkFti1XlMbw-wkkJ62PJDgPLm_5_D2jVgo6Qh_AF0wwGqvq6VmIObzruJfE0rs90LS9ZWwKdIQoOLbX4JYm6OyjPquGR_TQJD2y7CX2AbdhinTWdZ5irysO4u-gGdY43xtIRYUCoNz86hhfYIwrj-V0AbwON-IMRGyji028ejlVI1GAKDPUofKmkKvTP61VBRZT151nl8lT7md0QchTjpQTqM-ZUBUymswAmxL35WKn2SmJufBfWHSQD_wSo1IwwFhdcb1WRgvnUuejUwqPvndHtRQU9bUEKUybzYBuF8aaLb5CMXcyEqb6Ar0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147525" target="_blank">📅 11:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147524">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjJeXqnDz-wOCEY2FUoGv57aCthEQFIhmqomFGXNXVCJ4sGRXw1l7eulg-uuLslkG9xlvhXuvU6oNoIOFcN7R9zged1PysMfA23os6xXWrUmtqt6-8aMGry7FKCBFRX3BjLG8MteUaUeiuz28xbZXf6tyrW2JCovzNNB9bY5uiwix7j-7yKdzIJ1K2q4PanUvYbFoOQ_8hHgSEcuSS74gilsJnTXZScNZWvPmbsTppK-zMbKaxLOEDlEoOyYMwY0JTdSaYFSQvcGaiQiU7sYIJloCKi84NwQ15CRrMzKMsegsyOLNAR8Vqy_N0_dL924gothVoqvnj254ocVeV-_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نتانیاهو:
پیمان مکه فقط یک شوی تبلیغاتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147524" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147523">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
اگه میترسی طلا بخری یا بفروشی حتما یه سر به اینجا بزن
👇
https://t.me/+jkJGKa0y56liZGZk
https://t.me/+jkJGKa0y56liZGZk</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147523" target="_blank">📅 11:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147522">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2pXZXaqAJj1v3hH6vNRggDof4VEXk1dqGu13jQoBiKpfb_fEoGmcrxsrxjN5NGBS8RU-AUIGi2IPuehDCmG6lhgfez5H3uTlaNso36slVUgMbeXGjHb7E5FcTOdsV9yE1natQ2jGtMazm-APeDStb8J0bmIr9wDuI7YxidnKq3K2GuaePlO1OCXF9WhGm3ISl3eSOQzYVhdQD992PuWE4k08cLtLkHOqz8BXBq5LUyh_9tiGd3nBAQhgjEcsgG43P5i6Zdm-9rQKpijE-_jTIppLQBmXqdyNbkuOqQIeZqNN5OmLb87y6JYNHDyQM-dWUbBUx34ltMWRTyRyW5Vkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بافل طالبانی، رئیس اتحادیهٔ میهنی کردستان عراق با عراقچی دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147522" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147521">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
الجزیره: درگیری میان عربستان و انصارالله، اکنون بر «مأرب» متمرکز است؛ در صورت تسلط نیروهای انصارالله بر این منطقه، روند جنگ می‌تواند به طور قاطع به نفع آن‌ها تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147521" target="_blank">📅 11:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147520">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
تحریم دومین بانک بزرگ روسیه به دلیل ارتباط با ایران
‏
🔴
قبل از این هم آمریکا، شعبه بانک مصر در امارات و یک بانک ترکیه را به دلیل ارتباط با ایران، تحریم کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147520" target="_blank">📅 11:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147519">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01b896d38.mp4?token=fxMkvm4U5cc7RjMTkp-MWaiZmrXtpgI2D589TIizFCza5lL7z65G1QHn02VdmV6ci3B_lKhGS1TZDC3A29bAmVuAFSVLUgXpR2yvcuwMmZoHcX865gNkTA4IFB9ad2eqPw0stEa-Xidi-lfMIkXCZKH50RxYqC-EUQPqhfJozpdzUS8Mow1G6VSniRGehCm0ivrsnyeuo25CgtKkPzvYyrAB6gL1vGbLKC4z96syCY3lgaE-VA7VnXpF9EK3I-W_8QNcoIcWbma55D77Z3dfIDQTs5s8YGlzNKUgZ3ZGFhulZnQx7S5K_dZFtjFx0DVkxTyC3AIT_kT981rulecyyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01b896d38.mp4?token=fxMkvm4U5cc7RjMTkp-MWaiZmrXtpgI2D589TIizFCza5lL7z65G1QHn02VdmV6ci3B_lKhGS1TZDC3A29bAmVuAFSVLUgXpR2yvcuwMmZoHcX865gNkTA4IFB9ad2eqPw0stEa-Xidi-lfMIkXCZKH50RxYqC-EUQPqhfJozpdzUS8Mow1G6VSniRGehCm0ivrsnyeuo25CgtKkPzvYyrAB6gL1vGbLKC4z96syCY3lgaE-VA7VnXpF9EK3I-W_8QNcoIcWbma55D77Z3dfIDQTs5s8YGlzNKUgZ3ZGFhulZnQx7S5K_dZFtjFx0DVkxTyC3AIT_kT981rulecyyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجرانی: ان‌شاءالله شاهد صدور گواهینامه موتور برای زنان خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147519" target="_blank">📅 11:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147518">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سخنگوی ارتش در واکنش به فیلم نجات خلبان آمریکایی:
طبق قانون، در صورت سقوط هواپیمای ایرانی، اگر ۲۱ روز خلبان مفقود بود، ارتش وارد عمل می‌شود.
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/147518" target="_blank">📅 10:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147517">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
المسیرهٔ یمن از حملهٔ موشکی عربستان سعودی به منطقه العصاید در استان صعده و مواضع حوثی ها در شمال یمن خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147517" target="_blank">📅 10:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147516">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnPsjGw5_PzVQN1DYp0kZnTeVnO7kHQp8xbt6oB7tssrWW65egHru7xQK_9J14h-NjMp9WahD--itQH1hWESmeDtbBEi0VU5Va3Ygcu_9htE6_CaUFrrnvwIbG5RYYlZ7IOC3qd76j6tJyNJtJXYyRlsK8ysg6kWz_5TiPcBM2eYokXoh3Y7fI53WQZ9sYG6-jjzOY4RC-WPlGm6LsUU75BUl3XpmhH_03MU5-V2bCbl7S8wV-Ep8g3VpDHVUUNV4Za73Qyn5UXo_vKs920ym9ohcaDG4dcOu7Z6salku0ScmT0e-71ur5w2jm_o6F8jQ7fmUduiypqCtMwKvFG7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که یک آتش‌سوزی ناگهانی در یک مجتمع نفتی در شهرینبع، عربستان سعودی، رخ داده است. این آتش‌سوزی از طریق برج‌های احتراق رخ داده و شدت آن حدود ۴ برابر حد معمول بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147516" target="_blank">📅 10:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147515">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💢
رو کدوم سرمایه گذاری میکنید؟
دلار
.
طلا
.
ملک</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147515" target="_blank">📅 10:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147514">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی دولت: مصوبۀ حذف سهمیۀ بنزین خودروهای نوشمارۀ بالای یک میلیارد بازنگری می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147514" target="_blank">📅 10:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147513">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl8hJIouCUIZpEMTViGJCSDaLxcKSqwKEPmHYFjJMsHCHZb3wlQ-fsvZxVidhlnLSeEVHiyot1Fib4sDz-dLjALJ-uBUX_H2dWNshFw4PpWfGYzKoEeEAyTnVWHSKkflXoFFWgaGC_eWsB2BvrEjYeIlhvpwrOHjzQuAZ57XIGhakwSrsdXumI5onucfi5CHV99mbbXaaeOYskmqG3XlQSfJznsDap31gx7uFD8RBz2xV_vcL-qJRUWPD2d-EVxNnwWJOgYzD8omda3xPnh8Cl69AICmb5bvwWjJj83V7Qw0Ik4y0o1vBKDHOoT5fWH33Z23K-vxsP6iPEzEpJknoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد البطش معروف به «ابو اسامه»، فرمانده یک گردان در تیپ شمال نوار غزه وابسته به شاخه نظامی حماس، در حمله ارتش اسرائیل به یک خودرو در شمال شهر غزه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147513" target="_blank">📅 10:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147512">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Imhsd-VC0efJJZ2bGgmeoew3O7y2UMdqFqYlhcHBH4j3izPbMEpO6WfiLOvtB80XuPaEtr6ghpxJggHWFYDYx6uYAa0zbc3dztI0ClhMwf2T62rolGNC1h8H2uYq2ZuIDAXb8tAOrS4g3tbaRnYqN0OXeTAr47bKc22BluSrlQ76ModtiQQsEYR0ME3COALAWhM5AY5PsqJZxSBDZzgsxUTOCPPL0RO8jOOdfEYewlB9US-w9GYBNrGfb46WQcoVCV42gvh0bOMdOJbcprx_kNla6npfuqXctz4hTvgIw84BKcUKre_zF36tF7UPpRDnKPGcohN10W8SnpJM_aFjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بحرین حملات موشکی بالستیک و پهپادی حوثی‌ها به عربستان سعودی را محکوم کرد.
🔴
وزارت خارجه بحرین ضمن اعلام حمایت کامل از عربستان، از شورای امنیت سازمان ملل خواست برای توقف حملات بیشتر حوثی‌ها اقدام کرده و مسئولان این حملات را پاسخگو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147512" target="_blank">📅 10:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147511">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=PtMARlwvF1vPOc4Lq0msyF9usiG6CBtPCJPYeaMypou1iSaNB4JDTJPTNoltXot1DmpzHW3i5kK4nzB9IOE_V_y5vJmrtxr37mx4atYEh8hpbTLo_mfUCFi_yQ8xvVDIxFSQlEWn4vQWY1S9PaOWt3aMUyJvrnahXHK9JHUGnvrs5tBBYF7BMDfmUibtF2tr1ftTqExkH7iOlS2bRU6-gc6p7P7k4Iwo4kj7UXB8P7kF4-WrEQ4uaNUNefScP9JriQpWvQKyfK66pGosFtM2DvRj5Fzv-CZ7r__w6ehhErTBKNXl6ntPjYmuvN66tt6GpJyBWs2bFIkNtxI24-0swg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=PtMARlwvF1vPOc4Lq0msyF9usiG6CBtPCJPYeaMypou1iSaNB4JDTJPTNoltXot1DmpzHW3i5kK4nzB9IOE_V_y5vJmrtxr37mx4atYEh8hpbTLo_mfUCFi_yQ8xvVDIxFSQlEWn4vQWY1S9PaOWt3aMUyJvrnahXHK9JHUGnvrs5tBBYF7BMDfmUibtF2tr1ftTqExkH7iOlS2bRU6-gc6p7P7k4Iwo4kj7UXB8P7kF4-WrEQ4uaNUNefScP9JriQpWvQKyfK66pGosFtM2DvRj5Fzv-CZ7r__w6ehhErTBKNXl6ntPjYmuvN66tt6GpJyBWs2bFIkNtxI24-0swg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: بارش‌های پراکنده‌ای در بخش‌هایی از کشور طی ساعت‌های آینده خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147511" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147510">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی دولت: بانک توسعه نوین (بانک بریکس) با عضویت ایران تاسیس می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/147510" target="_blank">📅 10:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147508">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMUyVcSpCFoUHVUQG5WqDAAcMaJnKGvcGt1iRLXlTY1IrnyAUTB3Kmt15-UZnKtRsO4QEMNzZAueLRFLX_RfUsXWr2CZWwYOrQajdtYi64MH55Mr3bcKpbMa8S3vcs7O3o9yDq_tWYLtD-CCaWQYItmfiGJF3pwJl5QEZmzYe6_Mja4dzEcqVSggEr9xqPQHHpdad6gluwHcITPBYeam1II2SuKAoNHJ1vKA1_NjzXUMjww3TjHc0xLA44U576ZFszxTpf-86UZTg_216g5SkONyP4PPzh6Ljp90R669thSLzpnVLvc2Lg0TTSskkVUztxxhiHVd-9WcPldsWB19mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZVPS2ymiTZnkeNc0n3eN_5q_Hg1iyDPmEM9gyAU8SOOj_7MgOjH-xrQ3nLHwc5DEaYrfTSg7nl0szpRXJdXkfkiz69_hZOE-b71YdTBM-jcF07HF6c8O25d6TDF96qEsnkRfuHYz-OtJ84XMWzrLORGpet3PrV3EHiglgp8IHYe7KhaAa-JD5kvSo2acEUbQmK60ZHTi_e_e0Hnyz36ItXSnoRQTr93RrbXoBfmHbbSuddzO9ByQYMUQNw4jgPjlS2iPWXOIu8foKRxf-uLcoSMU9a_j5VVfSjhxgrBwNxeMUngaLBFJiYaNoOOD2AU5oGvxOY7k86FXvQvW3AHXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تانکر ترکرز: بر اساس تحلیل تصاویر ماهواره‌ای، می‌توانیم ببینیم که تنگه هرمز اکنون میزبان ترافیک روزانه دوطرفه ابرنفتکش‌های VLCC است. علاوه بر این، حجم بیشتری از نفت خام، LNG و LPG از طریق انتقال کشتی‌به‌کشتی (STS) در دریای عمان مبادله می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147508" target="_blank">📅 10:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147507">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
روزنامه هآرتس عبری:ارتش اسرائیل به مقامات سیاسی توصیه کرده است که از مداخله در یمن خودداری کنند، زیرا معتقدند تهدید "حوثی‌ها" فراتر از اسرائیل است و به کل جهان گسترش یافته است، و باید یک ائتلاف بین‌المللی برای مقابله با آن تشکیل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147507" target="_blank">📅 09:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147506">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر نیرو: صنعت آب و برق ایران در برابر تحریم‌ها خودکفا شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/147506" target="_blank">📅 09:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147505">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-JobumDY_Mf0GHZDWWTUoEpmPWTjUIQ_lLorh657fMzcyYDOu4xClCafpb3SOIVmjP7bLFTuHloDpdEwOIWFgMUIOooBe2oWoz9_SOf5LHtv4hhKGnH4hpxJ9K-a2P_MBKj7EMnCZD5fMcynNbGhf92I-edT79xYI2AwPrXtqpyRczwA_NBd8ahTOcWt_w1Clyztqbw5suqCT15CnDg9LNm-KxWraIANxhJsjZ_wtH2kPnBzjiSUXUR_dJrxiEdBfI2pIBZi35R7nBkfXDuSXuU357EvAKBv6Vd-DHKgIpbsQXgBINyRUYtxx97lmrqoZDuXEpEB4CSMoe2Jfgf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ترافیک دریایی در تنگه هرمز پس از افزایش تنش‌ها در خاورمیانه کاهش یافته است.
🔴
این موضوع نگرانی‌هایی را در مورد این مسیر ایجاد کرده است، و به نظر می‌رسد که عربستان سعودی ممکن است در عرض چند روز، ذخایر نفتی موجود برای صادرات را به پایان برساند، مگر اینکه عملیات از طریق خط لوله "شرق-غرب" از سر گرفته شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147505" target="_blank">📅 09:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147504">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
الجزیره: مجلس نمایندگان آمریکا رأی‌گیری درباره قطعنامه‌ای که خواستار خروج نیروهای آمریکایی از اقدامات نظامی علیه ایران است را به تعویق انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147504" target="_blank">📅 09:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147503">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
تاکنون، حملات یمن با ده‌ها موشک و پهپاد، تاسیسات نفتی و نظامی در عربستان سعودی را هدف قرار داده است:
🔴
ینبع
🔴
طائف
🔴
جده
🔴
ابها
🔴
جازان
🔴
العلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147503" target="_blank">📅 09:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147502">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiRci5irlYa3-ygv7q363I29v1CT96jncgNpX2b9X61ErJnJpVXjcPQSTuSsY690QsM4psZhpKD4qa55JU5-oF8nkzTJZYyCFP5cnXjsURox0oGSfSChHD9E53cKBTHiaJEZ6pzNWGbuPFNIwOcqA7vkMhKyEAXZ2z4lkLChXO-jc3crMijx2VjTnFR9m-zRPbhoZtm7_xo6HKcE7ZagNSfjdFEbM2gxPdmbRbWZFDnCWvZ2Nx1DF9ze4OYG1UlFiS7dQFP-RbOXyTZnMSjb7h1JjD24d6zMCMrVF5BBApO2pZf9FfzumXya9Z1J5QmhlXLKJJSNrN-ObLp-y2GxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات آمریکایی و سعودی: عربستان سعودی با "بدترین سناریوها" روبرو است، پس از آنکه ترامپ از مداخله نظامی علیه حوثی‌ها خودداری کرد.
🔴
عربستان سعودی نمی‌خواهد به تنهایی با حوثی‌ها درگیر شود، به ویژه پس از اینکه عملیات نظامی قبلی خود در یمن به جنگی تبدیل شد که حدود یک دهه به طول انجامید، اما به اهداف خود نرسید.
🔴
هرگونه درگیری جدید نیازمند حمایت بین‌المللی است، و نباید فقط به عربستان سعودی و کشورهای منطقه تکیه کرد.
🔴
احتمال کنترل باب‌المندب توسط حوثی‌ها، همزمان با بی‌ثباتی تنگه هرمز، "بدترین سناریو" را برای منطقه رقم می‌زند.
🔴
با وجود سال‌ها بمباران عربستان سعودی، آمریکا و اسرائیل علیه حوثی‌ها، "هیچ‌کس به راه حل نظامی" برای مقابله با آنها نرسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147502" target="_blank">📅 09:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147501">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T0VugesB1bZtTxcHbOLZLLlKWN9KUTq7dCVtxKgjP0vlKfecJVhjBfCvGpK3IY_OMty8ZdPOJdjIURHk3fMuF3s1k2AEiknnHuszcJ-LQbxbgz24BRpRn5fX31hVbxW_P8PvDjDsUcrWsu_2OVOfvUG3Z9gCyemHCy-uIvzTY7_G0KCC7yKRCVrpFxUe4e4aYWYphjtwUPAozlI_CgRkNfPJD34GquWFRGIz7cg3fqsCId3lFyEkZOBdLFF-OvyORtI_nhvuYYN5kagj4q2DJu-UKR_NhX2g7H0tpoSLkE6ndpTFeCqUD5VDUlMk60pOiRajPF5aSmsrAXj3N13Q-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای عازم فرودگاه بین‌المللی ابها در جنوب‌غرب عربستان سعودی، در حال حاضر در الگوی انتظار پروازی قرار دارد
🔴
احتمال دارد فرودگاه بین‌المللی ابها هدف حمله انصارالله قرار گرفته باشد یا این اقدام صرفاً تدابیر احتیاطی در پی احتمال حملات بعدی باشد.
🔴
هنوز اصابت به فرودگاه تأیید نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147501" target="_blank">📅 09:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147500">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
تأسیسات نفتی جیزان عربستان سعودی توسط حوثس ها مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147500" target="_blank">📅 09:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147499">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNtPRGVnWYLWrT--8R_Hmud2KKgG754Ax-T3DdLqwdDK4vEEe_LM7Np4JTX0v8Cw0TM4LWRdICcwkkEnyWWQ1d01bS7z7TudYCdi5qFkv-bDtq-HVw0izVQPeWjmngwz9NZ12-Gl7bRiRFatU1e33qnX6F_vSeLi-MH7UCxhhthD20ttOvOgcDxMU1zWGReGZV2PNmNaeRgfHKIulU_jB34Tc3jP0D9vj_THDFl2TiQxplJR0AqZGqsZ-Wt5YE3axRpexY9AUb_aLNO6paOTKrua8k9a8r5atiBj9WWFzewvazs0fLmnn9TKWrD3CrW4PAw444abhZtHXl7BdDsJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147499" target="_blank">📅 09:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147498">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc8166669.mp4?token=G6X22Vf4WuHTa9pAdoFrUCGcW_ZZm9Y7Y4j_1mvahTTKOk3qF8-XLpPxE1idH7Z18T29LJdpXSnW-05zURYx_L9VSDQzARwJLmdAbTs4FydGrxTrDvt4xV2WVZPyR0_2E5NCexQSr0M2gAgCOeu1e-KcbWOE4wZlgSwuOieOafXgak9MOAUkaTcx650-kLCLS4P72iIA0w5mHkA6jRMHqYuzAEKsMeNhVrf7Sbcu442j41FJmlmlvh0Na_ZdXbHWOVDZ8AbSGDb-1FbsmUpEX_GQjs170ftKCu5GmoanY6Xyzu-t5-e00Rp-H4BDUvaS30PEi-CNnhghqTRJp1_32Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc8166669.mp4?token=G6X22Vf4WuHTa9pAdoFrUCGcW_ZZm9Y7Y4j_1mvahTTKOk3qF8-XLpPxE1idH7Z18T29LJdpXSnW-05zURYx_L9VSDQzARwJLmdAbTs4FydGrxTrDvt4xV2WVZPyR0_2E5NCexQSr0M2gAgCOeu1e-KcbWOE4wZlgSwuOieOafXgak9MOAUkaTcx650-kLCLS4P72iIA0w5mHkA6jRMHqYuzAEKsMeNhVrf7Sbcu442j41FJmlmlvh0Na_ZdXbHWOVDZ8AbSGDb-1FbsmUpEX_GQjs170ftKCu5GmoanY6Xyzu-t5-e00Rp-H4BDUvaS30PEi-CNnhghqTRJp1_32Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشرشده از نمای یک هواپیما، شکل‌گیری ابرهای عظیم طوفانی بر فراز ایالت یوتا در آمریکا را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147498" target="_blank">📅 08:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147497">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRXbVKK8M9jpTAbTNX0Q0Z_hT0xc2oVLGsQVw_2kpz_2Nrsy1zv_N-Y2LMGI3Ac34fOV5dwnTKYMOxUaNjsEZm8uqow59KGmlYnU4_YmWUxULaa-l2J1D38SSSCEyrsonSJR8x0kI7YiKp1iwzEF1ecgylwCa30BlVh_N1y90t5sRnAS3lyJxGiIfhQopKPkP6ZfVYBknC6jF5vLEkFJ2lBxK6oQfjuBU7kctzGZqx3CoS7ayux-PT4j-wQ8xwc7U4MAqDQVJOp193VwG0JR9qRepZ28fVf3mHwJIbKwK-TqaXY1MzJ3n0zS50okp60YDel27NScy7rqffDeM2gHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای بدون سرنشین اوکراینی پالایشگاه نفت شهر سیزران در فاصلۀ حدود یک هزار کیلومتری خاک روسیه را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147497" target="_blank">📅 08:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147496">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت دفاع ایالات متحده برای اولین بار اذعان کرد که سلاح‌هایی را در فضا مستقر کرده است.
🔴
تروی مینک، وزیر نیروی هوایی، گفت که ایالات متحده اکنون به "سلاح‌های کنترل فضایی عملیاتی" مجهز است که برای محافظت از نیروهای آمریکایی و متحدانشان در برابر اقدامات خصمانه طراحی شده‌اند.
🔴
او از شناسایی نوع این سلاح یا افشای قابلیت‌های آن خودداری کرد و گفت که حفظ محرمانگی برای حفظ اثر بازدارنده آن ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147496" target="_blank">📅 08:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147495">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLr_mb8X3Hy4t9jwQqrFomarL6EN-HLIRlGNImjgElYTUltjK5hYLUszYTa83Cvc9OnSrlAWZMVcWHxpBUF1SR3bIuxCy_xTz1-R4AmRFcnZA9gF8_SG_vkuPq0KMGPDUOGa6YH7hSWyvNSHHdWpSmhUvlaw4mn9FWR-NSCyzad-rI0T1DSN1gygHGTh-DV-tAlpksaMU-VTDji0HaBhizrkPcRELJH7zGIqH6r7B-mWMfShErWobCJi2PhckFw4vfavCo4kFxVvOmibmuyZECJw10Y3RkFFPHZ5ybMpveLy909xwztEUIKVyDP6xUb5yWScwN98VvWIfcs0lJA81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوآوری جدید تو جنگ اوکراین؛ پهپاد چهارملخه مجهز به پنل خورشیدی
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147495" target="_blank">📅 08:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147494">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqO_5rRn_7xF8OTk6g5dgdoUPwF0Ftzq0r-_UFsYjiGaj1cYktgaH-z87H-yImcNR1LjBqRiJydrufvajozB2sOcmss4EMLzfWbsFrqC97QUHo3OZiXE7xoR7qAjLEILc8-ztcIK42kGdIi3ZLjGymH1ID4xrgqI1lpBUAKGdpXOEZ2MmuomjtjNbHJMon3AScP2NRCsvLZhybA20xu6ZWkxUXEOJQ1nkOHCKiMtuCwa65gq1K_-NCt02q2kg_1Tfj7MK_oza3YVCvMHYiCM0lMOfrHOQEwY16UMciBdNuGKo0HoXf3WLm_MbUr24n5HY2v2G8KKcCdXqtSG5qhcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: عربستان از پاکستان خواسته تا ایران را راضی کند به انصارالله بگوید از فتوحاتش عقب نشینی کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147494" target="_blank">📅 08:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147493">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سپاه: بامداد امروز یک فروند پهپاد پیشرفته MQ1 در آسمان غرب تنگه هرمز زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/147493" target="_blank">📅 08:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147492">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBRmjx_PLKgWZVqDlMD2buDPWsbwDarQlqC3meb2gEZOHGK7VPnSmZlAEyofKNTTof-s_4uQY6weeIl2ad9RyRCqE3t3r6UXQYiwTh_rp5mVdCSumDF3Pi_m167pU1WRdbCftl8uPoz1C2k3hgAkNw3ZWa8tMQRkH3VBmg-7ynoeknv9bQIcvsqNkeFT-OnJb-nZwZo9X9RlE1kx9LNytSbYOFFoERFvng-RaRHLtdaY0hVTAFX2GT3KuGUlfAbdoigxyPR3jbHPHSeCPWRQYH-ZrWU0RVbLWRNWZLwNvL_y7BhSCTs4lpYl2fy_AOFKnmMgGKicyuBYl56YNBTu8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد بارهایی که دونالد ترامپ در هر ماه علیه ایران اعلام پیروزی کرده!
🔴
آمار سپتامبر واقعا نگران کننده اس. فقط یک بار
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/147492" target="_blank">📅 08:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147491">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erpNYWg9sTi0RnRIGTQRydzHSi4rC8st3cFNxS8tQVKEq7xTXIIjR6eXOx5V9mQITIG6iIGfXJA7xBkvY7DN448lauirJ2mRISQcSI8dYq4JZWCFmtO7ICKUS32EGqK9Y38DE9r_7Vyy14UF8HR6vRg4ztnRHXIbwzYb0LmHtEA-Hp6Z35xRVyWrAElUZFyzLuh0RCjoHB32LNlQ-BZgKQYOlE1_XPKrveTIOavGg7Q-5WbXm-4UWanikDS-Y2WGQPJ9igmbruu0U-2Ma1PAyJ465fGGzhp36eDj468y7vGzDR9ZFpW3QcmlgTDWYnOvbLBGmYOSYzWvoaQkfufj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت: در چارچوب عملیات "تنزوای اقتصادی"، وزارت خزانه‌داری به هدف قرار دادن و مختل کردن فعالیت‌های آن‌هایی که از نظر مادی، فناوری یا مالی، از رژیم ایران حمایت می‌کنند و به آن امکان می‌دهند تا فعالیت‌های تروریستی خود را ادامه دهد، ادامه خواهد داد.
🔴
وزارت خزانه‌داری هیچ‌گونه حمایتی از این رژیم را تحمل نخواهد کرد و به شناسایی، افشا و منزوی کردن افرادی که به رژیم ایران کمک می‌کنند، ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/147491" target="_blank">📅 07:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147490">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/147490" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
