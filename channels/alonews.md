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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 11:37:42</div>
<hr>

<div class="tg-post" id="msg-135922">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
واکنش سخنگوی وزارت خارجه به تهدید آمریکا به تصرف جزیره خارک
🔴
افراد زیادی در جزیره خارک لحظه شماری می‌کنند برای خوش آمدگویی به نیروهای آمریکایی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/135922" target="_blank">📅 11:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135921">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/642abbab66.mp4?token=uii-QkuOPRB-hcKH7dQGZks541QpidUleUXYXJriZo0KMwzm8hUnl-ECz-mJMAT4SSlLbQw9SpOwNIeLOz1Xsmat4BawQSQvmK_noZDN33lg0ID7S9We0-3vaQcdOcQG-Q9WrJ8BIGHxlct61fPCCBMqBLzCQdTUsu9TXuWFAdd8WvlbrQJoIk5D36apMJ_W1nY76vyEDRg2YsGBHmqSc3laUpKrsao_9A4T80RpewjuBVwEKNGmMki206Yw3NrWw2Yl_y3jVkm540J3wmGTIxziA3nNZYA4Ty_I75aiI1j3JZHFCGVtetJcntZ09aAl-sAiHFFbgw5KLLxmjuQ_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/642abbab66.mp4?token=uii-QkuOPRB-hcKH7dQGZks541QpidUleUXYXJriZo0KMwzm8hUnl-ECz-mJMAT4SSlLbQw9SpOwNIeLOz1Xsmat4BawQSQvmK_noZDN33lg0ID7S9We0-3vaQcdOcQG-Q9WrJ8BIGHxlct61fPCCBMqBLzCQdTUsu9TXuWFAdd8WvlbrQJoIk5D36apMJ_W1nY76vyEDRg2YsGBHmqSc3laUpKrsao_9A4T80RpewjuBVwEKNGmMki206Yw3NrWw2Yl_y3jVkm540J3wmGTIxziA3nNZYA4Ty_I75aiI1j3JZHFCGVtetJcntZ09aAl-sAiHFFbgw5KLLxmjuQ_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی : هیچ زندانی آمریکایی با مشخصاتی که ترامپ گفته از زندان‌های ایران آزاد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/135921" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135920">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:  متن یادداشت تفاهم هیچ بهانه‌ای برای طرف آمریکایی باقی نگذاشته و حتی خود آمریکایی‌ها نیز ادعایی مبنی بر اختلاف در تفسیر متن برای آغاز مجدد حملات مطرح نکرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/135920" target="_blank">📅 11:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135919">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / الحدث به نقل از منابع آگاه: وزیر کشور ایران امروز با نامه‌ای ویژه از پزشکیان وارد پاکستان می‌شود.
🔴
نامۀ پزشکیان که وزیر کشور ایران به همراه دارد، به پروندۀ مذاکرات مربوط می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/135919" target="_blank">📅 11:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135918">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تخم‌مرغ گران‌تر شد، کوچک‌تر هم شد!
🔴
قیمت هر شانه تخم‌مرغ در تهران به حدود ۴۸۰ هزار تومان رسیده؛ یعنی ۸۰ هزار تومان افزایش در دو هفته.
🔴
خریداران می‌گویند با وجود قیمت‌گذاری شانه‌ها بر اساس وزن ۲ کیلو، تخم‌مرغ‌ها ریزتر و سبک‌تر شده‌اند.
🔴
تولیدکنندگان گرانی و کمبود خوراک را دلیل افزایش قیمت می‌دانند؛ این در حالی است که وزارت جهاد کشاورزی از افزایش واردات و ترخیص نهاده‌ها خبر می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/135918" target="_blank">📅 11:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135917">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa3dfa981.mp4?token=CIE7D0BQlOMaBx8UyTcse8h2ZIuDyfzd8-YK0Ie-VzmsKMnATUCDbLYZBsf0BJ2_DM70n1Nz0H2sIhVmtxvkx7_XU_qKLF4uOT-yW4NClfjsBU2Bq3EHcsINrxu69wlICtVZdT7EF7y5Y9zyEu7oEH6SOhFwIiWnjtcJ6UhHiFR3TCUYDZJaJFEtaHVMWSM90U-Nzlg1KqlAMJzq8FpMiDMTs5PoIW4u73eGWhDxB-aaYdI0M8klK50TIuWM01iy2c-aT5_CaDVQxgaUQqI9O9ZFXB_BkokxKeFltytzYO129irwOsMOS2wj4326W2nljdXYE9nFAx6kwuZ4RH6MeqBdLcqvzk0QPmh_tVgr01aQGvChn-zVqlR7swrUa6yovoNYkYfBq11_xrQ1MnnnsbB5kWwPqwS8E64KTtc5383XkCjrWDDwSvEuipKCzwyQeF6kZznaMzmTfo7eL8pGKlgZCQSz0jT1fAUPuS-zAnjpzmYmOiVVTSB2xHPIHREBAvL-emjeqjt_6Zobhgpb-bkj_U6WzdOdwZWfBvutSWpq0za9omerOohDLzIn8TjSimjQnTIhp23FNitatRRJwKevol-rC8IDWP9GpDP7yEzzsKbGevkJWnXeCfeWf3t_1BUPhDi4naURnqAGh1bIcDWVUxjg1qR-k1VxiNqyDUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa3dfa981.mp4?token=CIE7D0BQlOMaBx8UyTcse8h2ZIuDyfzd8-YK0Ie-VzmsKMnATUCDbLYZBsf0BJ2_DM70n1Nz0H2sIhVmtxvkx7_XU_qKLF4uOT-yW4NClfjsBU2Bq3EHcsINrxu69wlICtVZdT7EF7y5Y9zyEu7oEH6SOhFwIiWnjtcJ6UhHiFR3TCUYDZJaJFEtaHVMWSM90U-Nzlg1KqlAMJzq8FpMiDMTs5PoIW4u73eGWhDxB-aaYdI0M8klK50TIuWM01iy2c-aT5_CaDVQxgaUQqI9O9ZFXB_BkokxKeFltytzYO129irwOsMOS2wj4326W2nljdXYE9nFAx6kwuZ4RH6MeqBdLcqvzk0QPmh_tVgr01aQGvChn-zVqlR7swrUa6yovoNYkYfBq11_xrQ1MnnnsbB5kWwPqwS8E64KTtc5383XkCjrWDDwSvEuipKCzwyQeF6kZznaMzmTfo7eL8pGKlgZCQSz0jT1fAUPuS-zAnjpzmYmOiVVTSB2xHPIHREBAvL-emjeqjt_6Zobhgpb-bkj_U6WzdOdwZWfBvutSWpq0za9omerOohDLzIn8TjSimjQnTIhp23FNitatRRJwKevol-rC8IDWP9GpDP7yEzzsKbGevkJWnXeCfeWf3t_1BUPhDi4naURnqAGh1bIcDWVUxjg1qR-k1VxiNqyDUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تشییع جنازه ۹ نفر از نیروهای گروهک های کرد در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/135917" target="_blank">📅 11:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135916">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHa0Kr70m1yLtd_m1t4tb4h2l5a6yzYCg0RmXxVpmeueDkVooc6I3_HJqLpcPMpFafRWl1zsyHN6mFDeh9qp9oQ3d4pp7xIyfc7MCH8Xq5FNmvlq1Bh9USIfvcD1B6pZfyEt2q5M3R6zgi09USDbeWht3PfY-AjfTzYiaLuQmZW6Yplb21lp9Jw-anYLnbS7ERG1g9cK2oAIwRE4DNh783yfWs8Yesp5jd-2ZG6muoFqPyjj37MFVx4L1oKHq4LlnmKsuyhRkWh1PVIKSp-3CDY7M4EH2ReIyio1KsA0CfwJqVmukZk-23UjRfQ_VY5-ZV-o96pPZeVYsDExG1AZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب گذشته، اوکراین به یک پالایشگاه نفت در پودولسک، واقع در منطقه مسکو، و همچنین به سه ترمینال بزرگ توزیع کالا متعلق به شرکت Wildberries در حومه مسکو حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/135916" target="_blank">📅 11:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135915">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: پیشنهادهایی از سوی میانجی‌ها مطرح شده و دریافت کرده‌ایم.
🔴
اصل موضوع که در این روزها هم دستگاه دیپلماسی فعال بوده و هم ایده‌هایی از سوی برخی از میانجی‌ها به ما واصله شده تأیید می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/135915" target="_blank">📅 11:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135914">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اگر انتظار دارید دیپلمات‌هایتان به خاطر ترس از فریبکار بودن دشمن صحنه را ترک کنند حتما چنین نخواهند کرد. دشمن فریبکار است و خدعه می‌کند و وحشی است ولی مثل این است که بگوییم کسانی که پای لانچر نشستند و از ایران دفاع می‌کنند از ترس اینکه طرف مقابل از تکنولوژی برخوردار است، صحنه را ترک کنند.
🔴
دیپلماسی و دفاع دو بال هستند. اگر هر کدام نتواند به هر دلیلی وظیفه خود را در دفاع از ایران انجام دهد قطعا وظیفه حکمرانی ما به درستی انجام نمی‌شود.
🔴
به همان میزان که به مدافعان میهن در پای لانچرها افتخار و از آنها حمایت می‌کنید دیپلمات‌هایتان هم به همان اندازه شایسته حمایت و دفاع هستند چون دیپلمات‌ها در کنار مدافعان وطن برای یک هدف می‌جنگند
🔴
اصرار بر دوگانه مذاکره یا جنگ ، دیپلماسی یا جنگ برای کشور ما مفید نیست.
🔴
اینکه فکر کنیم دیپلماسی نافی دفاع است یا اینکه دفاع با دیپلماسی سازگاری ندارد به هیچ عنوان منطق صحیحی نیست.
🔴
کاری که سیدعباس انجام می‌دهد با کاری که سیدمجید انجام می‌دهد با یک هدف است.
🔴
هدف صیانت از منافع ملی ایران است. گاهی با ابزار دفاع و گاهی با دیپلماسی و گاهی همزمان هر دو
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/135914" target="_blank">📅 11:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135913">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYRlPmrlz1Fi3IKHMXLr5WBwWlLmCv5cpIozMV7_-fEuIJ4cPFAJNjgrEZ9kgW5a1l5ZT1AtQ0APunbyWzVd7agHJg98YKGE_TbeXVqzxHqoXIPI8p9mxa-325WHpt6va1U5CFRtb7yvl7Fw-M9MfMKcLSvM79mqfOz_rmSo9AFJXfLqc6wYI6RGS4TiVz0_8pZODToJLNeHvRM24DjAqQz39ijAKEvS_jz-MBBxGvMML5EjsFLdHjh03-VOcUqtQFGmtmH13U76Keie28GxK2JshNXtyMYGRgRLcruHHXWMgXcrX5pk4Cdrlo0UetstCuA_ql99hk-ICXlefNYt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه اسراییلی: پایان بازی در حال نزدیک شدن است: بقایای رهگیری موشک‌هایی که به‌سوی عقبه شلیک شده بودند، در نزدیکی ایلات سقوط کردند!
🔴
مقام‌های امنیتی اسرائیل برآورد می‌کنند که پایان جام جهانی به پایان خویشتنداری آمریکا در خاورمیانه منجر خواهد شد.
🔴
تمامی نهادهای امنیتی در بالاترین سطح آماده‌باش قرار دارند، زیرا احتمال کشیده شدن دوباره به درگیری‌های نظامی وجود دارد.
🔴
با این حال، تصمیم درباره اینکه این اتفاق چه زمانی و به چه شکلی رخ دهد، عمدتاً در واشنگتن گرفته خواهد شد.
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135913" target="_blank">📅 10:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135912">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZIvndZJGlu9OOIlM0fp9wY43fZb66tlJ4wNaACLYIAmZ8Qa_ugD6BcXZy8BKqjitHNgN5umL1qdfPGyfpI8uAox698qQ1HYcderBobVBXRYekUAN0_lyz4O4jFYacLOQz40gwNImEN2kIh2tNTu7uNHE318urL73W1Pl6_nKR3PVw3TcvnNuVN63Yxwt819VNB4WC6jDzzGcR-gB-b85eblu3Rz-02uC3N9ITmKhx2_j8F1KLD3C4GjxNhUkTZRC8eGGBKf1wClqlYJsEfJ0fL7OLn3b_1au5vF8IVoNnH0cHtlB2NLWyDQKfaAE2acUpaSi8vXnA3_9mDDGToOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
🔴
۹۱ دلار را هم ثبت کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135912" target="_blank">📅 10:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135911">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3a65c5f.mp4?token=s8z34NCUns9zWG0IhcdKjRNrKtYBPM7brbRv4vmFqoEYZwQt0R_nRl4J-OEJRmMIDkjH68u1SagVElKB5GULXMcIfBNUpGOEl-a1qCah-zKuL6GbLm2GGthfoAlBfQTJGg_P0X9J4fbcB8GT663F6BFbo4I8TKR8RJThyOI9AtSI5svqSoQCp0z3jYYtYh7NVIU0ya5SCxjzLh6wvKrpAWgpbjqG_nIIpRPkkS0Krm-sFeqY_XtUoSRDwt0R7ieV66v8kPnztQfmmm_aBdK1APl1vIQjAuqbS_0Lq_ps2V2LXnuRxv1UQpqBv121KErkHCCfNT42y0k7PCzUBRD44A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3a65c5f.mp4?token=s8z34NCUns9zWG0IhcdKjRNrKtYBPM7brbRv4vmFqoEYZwQt0R_nRl4J-OEJRmMIDkjH68u1SagVElKB5GULXMcIfBNUpGOEl-a1qCah-zKuL6GbLm2GGthfoAlBfQTJGg_P0X9J4fbcB8GT663F6BFbo4I8TKR8RJThyOI9AtSI5svqSoQCp0z3jYYtYh7NVIU0ya5SCxjzLh6wvKrpAWgpbjqG_nIIpRPkkS0Krm-sFeqY_XtUoSRDwt0R7ieV66v8kPnztQfmmm_aBdK1APl1vIQjAuqbS_0Lq_ps2V2LXnuRxv1UQpqBv121KErkHCCfNT42y0k7PCzUBRD44A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: فکر می‌کردیم دو نفر [نیروی نظامی آمریکا] در حملات ایران کشته شده‌اند، اما سه نفر بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/135911" target="_blank">📅 10:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135910">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری / نقطه‌ای در حوالی اورمیه هدف اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135910" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135909">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae303cbc4.mp4?token=RVG_C-qiHjW9PqaLcG6wVyy8fHK5uFttE9aWR59W6z34Xh2ykMfZLTLZvxjO5p8ZJbBIEZYTeCki2DRnQhv9-sfSz0vGha-45kFupZhuB3q_Wl4Hj8fsuzqu6eFPdoNhGZUPj9EO25362aIqIz69kWaj-2ZuJQM24z_3vGO4f-PoNLD_vGEH82vTIL_Nw1gNhGqVmFrrfieKYf8Nrp8AgtH27hFJ2istEkcsWYm6ZLPyNSBtyxDkYNi9stfl0rJVNJ5OkOE4WkqhcvHk8YkR9Ko_1-tEpI3FhRqRm-lkdIarlB3IZlRkqVx2ChK8iO6u7rIoLiUvAngvodlIKI1-uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae303cbc4.mp4?token=RVG_C-qiHjW9PqaLcG6wVyy8fHK5uFttE9aWR59W6z34Xh2ykMfZLTLZvxjO5p8ZJbBIEZYTeCki2DRnQhv9-sfSz0vGha-45kFupZhuB3q_Wl4Hj8fsuzqu6eFPdoNhGZUPj9EO25362aIqIz69kWaj-2ZuJQM24z_3vGO4f-PoNLD_vGEH82vTIL_Nw1gNhGqVmFrrfieKYf8Nrp8AgtH27hFJ2istEkcsWYm6ZLPyNSBtyxDkYNi9stfl0rJVNJ5OkOE4WkqhcvHk8YkR9Ko_1-tEpI3FhRqRm-lkdIarlB3IZlRkqVx2ChK8iO6u7rIoLiUvAngvodlIKI1-uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا کویت به دلیل از کار افتادن بخشی از  شبکه برق، که نتیجه حملات مداوم است، از ژنراتورهای سیار برای تأمین برق مناطق مختلف استفاده کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135909" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135908">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
الجزیره: وزیر کشور ایران شامگاه امروز به اسلام‌آباد، پایتخت پاکستان، می‌رود تا با همتای خود و مسئولان این کشور دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/135908" target="_blank">📅 10:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135907">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / سازمان دریایی بریتانیا آتش‌سوزی یک کشتی در نزدیکی بندر کومزار عمان را تأیید کرده است.
🔴
منابع خبری و دریانوردی این کشتی را با پرچم مالت و مدیریت یونانی معرفی کرده‌اند.
🔴
این کشتی در حال حمل نفت عربستان به‌سمت آمریکا بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135907" target="_blank">📅 10:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135906">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
انفجار  در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/135906" target="_blank">📅 10:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135905">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سپاه:از اطلاعات مردم اردن ممنونیم؛ هواپیماهای بزرگ ترابری c17 و هواپیماهای فرمانده کنترل p8 ارتش امریکا در فرودگاه عقبه هدف موشک بالستیک قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135905" target="_blank">📅 10:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135904">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
روبیو، وزیر امورخارجه امریکا: ایالات متحده همچنان برای دستیابی به راه‌حل دیپلماتیک در قبال ایران آمادگی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135904" target="_blank">📅 10:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135903">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پرس‌تی‌وی: گزارش‌ها از وقوع یک رشته انفجار در سراسر بحرین حکایت دارد و انفجارهای پیاپی در چندین منطقه از جمله پایتخت، منامه، شنیده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135903" target="_blank">📅 09:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135902">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
مهر: وقوع صدای انفجار در اصفهان
🔴
دقایقی پیش صدای یک انفجار در شهر اصفهان شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/135902" target="_blank">📅 09:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135901">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / نقطه‌ای در حوالی اورمیه هدف اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/135901" target="_blank">📅 09:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135900">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری /شنیده شدن صداهای انفجار در بوشهر و کنارک و چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135900" target="_blank">📅 09:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135899">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a646ece7.mp4?token=luf3CJPrGZoKYtK-WGU7WcJNnMKA42DUh_7r-XJR-W3HDgpWi8zl4SdFuOAfZTcI7icscvbmqHt0Ky24dtdUXRN5_irePAaR0V_vedekx95oCpu5x43Ecsfy8VhXBicfJMCf1fwexsCQEuGRi3ob4n-kkbM-mnmzn1VrZki4F7G9WSoMuaOXebXAGxT-objXa0G_1oC4Dan5b3ykYShJgrVfo8SxqvStrJrKorB1AG2ujXoZROqavDODW4aeAWAd_0CC8wS76tEwAhfDYxW0l2OtV-_Ug8Cg__MzuhlFTeAtf8wQLHkYjTN8xeH3NxR3g7GbSwsaCDQcyskbYnOOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a646ece7.mp4?token=luf3CJPrGZoKYtK-WGU7WcJNnMKA42DUh_7r-XJR-W3HDgpWi8zl4SdFuOAfZTcI7icscvbmqHt0Ky24dtdUXRN5_irePAaR0V_vedekx95oCpu5x43Ecsfy8VhXBicfJMCf1fwexsCQEuGRi3ob4n-kkbM-mnmzn1VrZki4F7G9WSoMuaOXebXAGxT-objXa0G_1oC4Dan5b3ykYShJgrVfo8SxqvStrJrKorB1AG2ujXoZROqavDODW4aeAWAd_0CC8wS76tEwAhfDYxW0l2OtV-_Ug8Cg__MzuhlFTeAtf8wQLHkYjTN8xeH3NxR3g7GbSwsaCDQcyskbYnOOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاول دورف»، مدیرعامل تلگرام، اعلام کرد که قابلیت Carousels به این پیام‌رسان اضافه شده است. او به شوخی گفت با این قابلیت کاربران اکنون می‌توانند تصاویر گربه‌ها را درون اسلایدهای ارائه خود بگذارند. با این ویژگی می‌توان با کشیدن انگشت به چپ و راست بین عکس‌ها جابه‌جا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135899" target="_blank">📅 09:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135898">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
قیمت نفت خام برنت با افزایش سه درصدی از سد ۹۰ دلار گذشت و به ۹۰ دلار و ۷۴ سنت رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135898" target="_blank">📅 09:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135897">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تعداد زیادی از هواپیماهای باری نظامی آمریکایی به سمت اروپا در حال حرکت هستند و مقصد نهایی آن‌ها، خاورمیانه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/135897" target="_blank">📅 09:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135896">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD7UFnZWCkPp8qSZqytEzPCH9RlJZV4IgsG3e02ZLS9vtWdcD_5J2-Mh_BSB7bvIf2qnTkcOZMp4sSsxQY8mCFjB8ZLmmNwKeeEdllXmdt1Y7_cFat2u5A9S1wj4JjN2hz62RnJZErxIyLVEEB5KWT6d2kEQ_tYbyXxh9z3oj1irOpNo3Cwki9696XDD4swQG1vq4yebiJG7kBl-Xv1K67PxxxuGyG0W4CxM4WoflCGEvnDdA4vBm_WfOvmmP0GkqC5ui7AgSsNtijKvUelEqa6emGu8E9I4Qp3mu_rV-49wS36uvx_53i45cpuIpQ1Fb03aWWrX-UjVqL2GAY5YMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعت ۴ بامداد امروز مولوی محمد انور ریگی امام جمعه اهل سنت مسجد علی‌ابن ابـی طالب (ع) شهرستان میرجاوه سیستان و بلوچستان توسط افراد ناشناس ترور شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135896" target="_blank">📅 09:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135895">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت کشور بحرین: فعال شدن دوباره  آژیرهای هشدار؛ از شهروندان و مقیمان می‌خواهیم که آرامش خود را حفظ کرده و به نزدیکترین مکان امن مراجعه کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135895" target="_blank">📅 09:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135894">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeaIe5b5NsINpNNkr2GKKEGWcW2xTyr1vdDBT38gMQL6knqIZ3bjuSy3tk67jgGbyQbgIKxVmWyG3qrW_5jAizwtwk-T12Qnu73QEOI-rnCrfCITqqgXNS8O-_0PexPaXoPl-lMqAp-Kg4x3qU-Z7Bme3I-R38fWwEBzX8eo5lVWvX-jmK0vAgyeFxPGCajcUUwuwpujT0zjgv_PEcU4Em843dCYOSl4W-1qvJh-5a7WM7OklZsoLFrcVRpVu6FaUeHcsnPzk7MYS-2nqJF7MvbX_FRLU22Lktd0UNB5fbvrPu71gytc2u66YakPYLkSQiUpSCwYemSE1FMNLSB_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهرهایی که شب گذشته تا کنون مورد حملات ارتش ایالات متحده آمریکا قرار گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135894" target="_blank">📅 09:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135893">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3yZ3UyJMJ3hj9kMrC3q_ikegxHNggZeCU4OR8n-Eei8eQpKkOrGAgNam1HjzeK_UAKHeNWYv4pVYYBa_9tl6VyxjJ-ID0cDcUEpQNtMfe5_k7uuxaxXBvjkhLqTky3L6zuTTG6mRxLWGPKf53UD7vYilutlpVZJzylQ4SW-TtZb8KZwf-4FwXYcGN0LgOHFl_yk7lOkiMctCiubzeEDPYBESKfBe_DiGPJcGCAUPeaGJLnobOGgtVaiuAkcfhtlOTQqwVY4AAsX8pmropTQ7RuUzBBJJmYalHcVr6ftUvTzLGVbqGHSPK3J4mHk2H2Tii5CiHIuYy9fnqLI64Yk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاپی زاده، نماینده مجلس: سناریوی مدنظر آمریکا ابتدا گرفتن مدیریت تنگه از ایران و سپس طراحی هجوم زمینی از جنوب، غرب و شرق کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135893" target="_blank">📅 08:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سپاه: دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/135892" target="_blank">📅 08:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135891">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c329b9d64.mp4?token=cGnxCE3f3gZBCUTgL4OlCYn-lC3lgM4ZyCrXR3AcZaVZoKg0buKBjggAYTeZluki08h8o-kpDp_G-IuFRytZmY2bcA7hBg0WnJHdktze9x9kAhGb6QilT3yP_TZC3hLYVzAtD2OQgWadO7fjVoY7K9EQRs4NP4bfd6LqdAa4Yhoza0Af6G5Ej-Hl-iuMKlrQ9h-Cag9nYIM6WHxJOnMcuMNb0rui5Coq-b9cdeqGpt7y6JORJ3sEvsycETJo7WU_W7qId0f7h1se6z8aoSWTzqRqWxK-zMsAwH3Kt8M0wcIKCTrXKss5161N5IIr2_xDgBSZyBLDLg68897V0xP34w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c329b9d64.mp4?token=cGnxCE3f3gZBCUTgL4OlCYn-lC3lgM4ZyCrXR3AcZaVZoKg0buKBjggAYTeZluki08h8o-kpDp_G-IuFRytZmY2bcA7hBg0WnJHdktze9x9kAhGb6QilT3yP_TZC3hLYVzAtD2OQgWadO7fjVoY7K9EQRs4NP4bfd6LqdAa4Yhoza0Af6G5Ej-Hl-iuMKlrQ9h-Cag9nYIM6WHxJOnMcuMNb0rui5Coq-b9cdeqGpt7y6JORJ3sEvsycETJo7WU_W7qId0f7h1se6z8aoSWTzqRqWxK-zMsAwH3Kt8M0wcIKCTrXKss5161N5IIr2_xDgBSZyBLDLg68897V0xP34w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر سنتکام از حملات دیشب به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/135891" target="_blank">📅 08:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ : ما تنگه هرمز را در کنترل خود داریم و آن‌ها هیچ کنترلی بر هیچ چیزی ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/135890" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
لرزش‌ زمین‌لرزۀ کرمانشاه در ۵ استان احساس شد
🔴
لرزش ناشی از دو زمین‌لرزۀ بالای ۵ ریشتر کرمانشاه، در استان‌های ایلام، مرکزی، همدان، کردستان و لرستان نیز احساس شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135889" target="_blank">📅 08:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135888">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از روبیو: روز جمعه، با وجود سرنگونی بیشتر موشک‌ها، یک موشک ایرانی موفق شد از دفاع هوایی اردن عبور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135888" target="_blank">📅 08:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135887">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فارن پالسی نوشت: از سرگیری حملات آمریکا به ایران آن هم بعد از امضای تفاهمنامه نشان دهنده آن است که کاخ سفید یا نفهمیده که بر سر چه مفادی توافق کرده یا اینکه اصلا از ابتدا اهمیتی برای توافق قائل نبوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135887" target="_blank">📅 08:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135886">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
لرزش‌ زمین‌لرزۀ کرمانشاه در ۵ استان احساس شد
🔴
لرزش ناشی از دو زمین‌لرزۀ بالای ۵ ریشتر کرمانشاه، در استان‌های ایلام، مرکزی، همدان، کردستان و لرستان نیز احساس شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135886" target="_blank">📅 08:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135885">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
همزمان با کویت، منابع عربی از وقوع چندین انفجار در شهر منامه پایتخت بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/135885" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135884">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/135884" target="_blank">📅 03:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135883">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
انفجار در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/135883" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135882">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
منتسب به تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/135882" target="_blank">📅 03:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135881">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYe4iwUG4lO09OIzS5zHAwMHDEp9mcVz9YEbY2reqmtfeflN1SGY4a5fVdXXVsg5w5qCkODT86dRSrFVWQm6R43CRVDNVHm9NE6lwoFjiW60_JNdwUKtZk6C39Q5_QiladL4sndaItI6pfx-nOxk9i4r5IgBhbtt5_dyMOr4o3QF83DZaziaKHE9JEL2Wd--2ZK9apLsLHarwBub6_BXSE6UEWbFWMZmoEW1fUBpFvAPRn9oPtoINZh_KlE0YFiQpYi3j-msemnClkS3yvhwKtiQfkFdJ5TP6qITFYk0DMXOHFt_f7lal5fOTX2tH2147-lDBvPAjcZxqScxVBeJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/alonews/135881" target="_blank">📅 03:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135880">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRY4jF7uV4P0nDalqyRVX3z4s4scTczZU_Gt_gBCS_aF4Mi9M-damoEmCiQqb8tB5Ij43Zh1OHh5Z2BKl_qa6GTIPn2XuIJy9V_0n9ZtZUd9ab9QZK3npqG1nlb2Arz9ansJ0tJLoyiCEVnciGZ79hkseViMts3CbDpAxTQMlEPbZrPNrBcZek-EzB6nPTK7Yb0kr1BNtdYaIv3d2H35J-v8YFOh4nAVYBeV_QTJgA8BWCzZ8h1mH3Yv6Rjso2kAjzRIeaN5yGteLfUfgXqI2K-wlnnV0R0ulEqzQL-YrycrVvzyXGsLkg4YWZSA3X86QcMntyOA2cRm9ELbAdbWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت بندر امام
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/135880" target="_blank">📅 03:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135879">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFrbbm_B_gFvuF-lTHeQvCJeAnkTZtzBJqMNYbTQLbYFEM3SkcBFr3-hcZM2talyKyM_U3tvbdLhsYc-z88qJJVsx5BosKTLP_JR9Csgj3FWV3KwennQPlJsjE_17B-YPvkt2MckyI-sE5IbtUUpqj_Jk_f90wd6_-GI_T9oevcMD18zPr_5JTIZ7Q4KasizgQQowMNPX5yE0xfBUR7E6jP5IJtk-d2Wd-BFCsaDCi8CNVJpcOkFJKjCGovsgXGwWO5E1tS0VF-XdRL5FTiSMBw_MR3AI1LY7a6Y6_0sRg6JTTl6SxZmXxoBKbTlP21OlcfOTh7HNY2aCuFImz7npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه کشتی تو سواحل تنگه آتیش گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/135879" target="_blank">📅 03:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135878">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
انفجار در راس‌الخیمه امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/135878" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135877">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/135877" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135876">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ستاد فرماندهی منطقه سوم دریایی بندر ماهشهر مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/135876" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135875">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/135875" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=YcrBGW7ADnb2spwcKyZtEGstyLNKr2DGBEKWnNnlAi706NcrL6BofbSBNvV5R4b1G3p6ZVp_WgNlwejF9vPwwy3kV9_CEoRC3dNgfmAsZaERpE85PtEH0XDhpFnIEqwAI0S9MSBEqI93KcKVrTwb3h2yxOx04A_Sqr2QM2aq-IV3LXN61ztJMxzyGSZUtXgDphh30VJ_bIKr5kYSjxfjf3qNa9wEqBrxDtw4qPlgrAHrQp8ywtP68tMApxgKw4zTYAjYLPVR_Ora-1sJfWk36hMuBLuWcRw86UsLxmvxnm8aqn1dX8us0F6XHfs8O3eGkXSB5a26FBIqZLpbVH2rDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=YcrBGW7ADnb2spwcKyZtEGstyLNKr2DGBEKWnNnlAi706NcrL6BofbSBNvV5R4b1G3p6ZVp_WgNlwejF9vPwwy3kV9_CEoRC3dNgfmAsZaERpE85PtEH0XDhpFnIEqwAI0S9MSBEqI93KcKVrTwb3h2yxOx04A_Sqr2QM2aq-IV3LXN61ztJMxzyGSZUtXgDphh30VJ_bIKr5kYSjxfjf3qNa9wEqBrxDtw4qPlgrAHrQp8ywtP68tMApxgKw4zTYAjYLPVR_Ora-1sJfWk36hMuBLuWcRw86UsLxmvxnm8aqn1dX8us0F6XHfs8O3eGkXSB5a26FBIqZLpbVH2rDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتسب به شهرموشکی تبریز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/135872" target="_blank">📅 03:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
حمله آمریکا به سایت موشکی خورموج در بوشهر
🔴
۵ انفجار شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/135871" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
انفجار در سربندر
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/135870" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
انفجار مجدد در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/135869" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
انفجارهای مجدد در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/135868" target="_blank">📅 03:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135867">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
گزارش تایید نشده از انفجار در ساری
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/135867" target="_blank">📅 03:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135866">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afed7de895.mp4?token=HLn3DnDtIUF67ohVC8JAaKdsf6A5KyIO94GbxcALeKxJl7Mb4mJdBT1shIFY7s8M7pDG_vtF840bhqGQ19bBie5YUZ_QelY4H4qrpMiZKJ0oCSF5eEkBC3PV0IXMeWJm68f_APUE-KHCIGpabZ0y9GcipfcZ8QeP9WsW7moPeBsz80LwSWYRvhSdK0avLBsRQiaoQKbp2JJruS_Gr11wmiLb4Ol17T85vkx9eiXi4pFeMdeIZOYeMN54vVrlIVh3zaoaDYkKe_03P2SgIRqPbmvvEWr8oXddYASUg114TMWQYhbZU7Dspv-JUirpp1TGuJIZrUalyQ6sBHV0C6eQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afed7de895.mp4?token=HLn3DnDtIUF67ohVC8JAaKdsf6A5KyIO94GbxcALeKxJl7Mb4mJdBT1shIFY7s8M7pDG_vtF840bhqGQ19bBie5YUZ_QelY4H4qrpMiZKJ0oCSF5eEkBC3PV0IXMeWJm68f_APUE-KHCIGpabZ0y9GcipfcZ8QeP9WsW7moPeBsz80LwSWYRvhSdK0avLBsRQiaoQKbp2JJruS_Gr11wmiLb4Ol17T85vkx9eiXi4pFeMdeIZOYeMN54vVrlIVh3zaoaDYkKe_03P2SgIRqPbmvvEWr8oXddYASUg114TMWQYhbZU7Dspv-JUirpp1TGuJIZrUalyQ6sBHV0C6eQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/135866" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135865">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e26657ab.mp4?token=dBPDKnqetdCR2v8pX4bEM2ejAGS8c6wbAEKCUlQh8Y85QucZBPgbU4Pbeflx2g4egtmUdttbWJhCYLpw-qAkn67BIA_INWsFBZZu1flhf9-ixwBdV5rCtxMEn3kIli6HObRs6w1yFHOkzKUotv9ynSiRYFqQWZ0UBioLvYZtCTHNsL1ExHJlDttZEoP19Dc2MALCMtlLeMtZx6EPPkrLYQzUJw_yiroRFfPQukuEFCSh-XtrBxRkT3qV9bueuykaoFvmx-Ti-37T0Wlort8Yn7Qh6CwIizhehZAoBI72EWyvgAF9G5ARMhWprF333rK_eiBSEIsmq7irhu0Z6Nv2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e26657ab.mp4?token=dBPDKnqetdCR2v8pX4bEM2ejAGS8c6wbAEKCUlQh8Y85QucZBPgbU4Pbeflx2g4egtmUdttbWJhCYLpw-qAkn67BIA_INWsFBZZu1flhf9-ixwBdV5rCtxMEn3kIli6HObRs6w1yFHOkzKUotv9ynSiRYFqQWZ0UBioLvYZtCTHNsL1ExHJlDttZEoP19Dc2MALCMtlLeMtZx6EPPkrLYQzUJw_yiroRFfPQukuEFCSh-XtrBxRkT3qV9bueuykaoFvmx-Ti-37T0Wlort8Yn7Qh6CwIizhehZAoBI72EWyvgAF9G5ARMhWprF333rK_eiBSEIsmq7irhu0Z6Nv2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک های آمریکایی‌ای که از کویت به سمت ایران پرتاب شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/135865" target="_blank">📅 02:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
حملات امشب خیلی گسترده هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/135864" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/135863" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7pAQ8RTTY8G8rH3-u728S_be3prG8GguDUcGo1Fp_iROd8qu9PWJs_HK51y7VFPbuje8pTsTJvoNtATtyrAhuDsNb9MQ8uyiDpiPUhQnG_jXlxHxfOCrWmo9pEtzwRGowmq7uYa7j7ZLQ17JGGEg4rdBY16UM3oLnRaDwxHQbbKKQPqLrVKc1dP-_eitqmYZQUB2TRb2pM_LuPWVvzwBkK7N6BFpp7DFkfr8utsLybTbw70gVd9mJm1leiqBm59epKB6LNJfKvss4tOHtIIpEe6IinyGfIc535oySj8FQ_Wv5mI72lewK3pOKNpdpRGZApUuJ0NHX5KyY_zBvm41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: امروز، ساعت ۷ بعد از ظهر به وقت شرق آمریکا، موج جدیدی از حملات علیه ایران را برای نهمین شب متوالی آغاز کرد. این حملات به تضعیف قابلیت‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی در حال عبور از تنگه هرمز استفاده می‌شوند، ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/135862" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/135861" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/135860" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
انفجار در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/135859" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
هم اکنون صدای جنگنده در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/135858" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/4انفجار در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/135857" target="_blank">📅 02:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گزارش‌ها از انفجار در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/135856" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135855">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=gpdz1RLFaTTgE_H0A-MMZ76N5acff0OvjstFFFPnQO1lxgFuchG3a5mexwVN44-02kilMyR28eq1klmEPb_19SeNpSV4SU7E9BjqyuIwfUmWCDy-varEx8V4x5WdSuIH07lIx3bXC7QcgGmIDI4-EXOveGvmJKrGKlZLNCAuEwbgs_sNh4qHs4u97eKR7erd48l-GFoCJ1jFYh2i5V20u3sNZlHWzl0Vhzm12cIbO60Ht4z8NhBQn1eqJpca7xaibp48tjypj3JY2CdVb_xXBqZY0kxamc6OUzuilog0HPPM_bhT_VACUxuLol5h6K3pek_F8ufh6w8mrbTsgxGa4YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=gpdz1RLFaTTgE_H0A-MMZ76N5acff0OvjstFFFPnQO1lxgFuchG3a5mexwVN44-02kilMyR28eq1klmEPb_19SeNpSV4SU7E9BjqyuIwfUmWCDy-varEx8V4x5WdSuIH07lIx3bXC7QcgGmIDI4-EXOveGvmJKrGKlZLNCAuEwbgs_sNh4qHs4u97eKR7erd48l-GFoCJ1jFYh2i5V20u3sNZlHWzl0Vhzm12cIbO60Ht4z8NhBQn1eqJpca7xaibp48tjypj3JY2CdVb_xXBqZY0kxamc6OUzuilog0HPPM_bhT_VACUxuLol5h6K3pek_F8ufh6w8mrbTsgxGa4YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل: قلعه نویی موقع جنگ رفته بود ویلای خودش تو آلانیا ترکیه بعد میگه کنار مردمم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/135855" target="_blank">📅 02:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3tgl0Mz-8iZcf5qi18uC_PXYLCLw8K97QWvmU0_GAqQpTKyZ0MEQ8XtFvzJVDjAOVrHC62WdE4bGbDmFW-Fu7lFfGPVeOMinqnE0O4QPSCbi2V7_x2SrxkcHleskUQt25Qke-VMbzbWA-j5lMR5bmo2bRe0_J1dm1Adzv4DhZGLxl0sJVZFOrPMHa0g4LhiiBKCjmwgxdQm5_DTmQuXIT3LxME_q6Qi61bfy-9i5qQulPdT29tTIphyDelEGX_nL189OfiPQhHuQ1hLNYsYjgZCS8kQHVzmND_0-20sn1xO-27CQ81UzyuaFoH0MJILSc0dTmP_Epgje4huwSe2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از دختر پادشاه اسپانیا در استادیوم
سفیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/135854" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
این وسط یه مدال هم به ترامپ دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/alonews/135853" target="_blank">📅 02:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ میخواست با بازیکنا اسپانیا قهرمانیو جشن بگیره که اینفانتینو بهش گفت مشتی بیا اینور
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/135851" target="_blank">📅 02:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
صداوسیما قاتل رهبر رو نشون داد
✅
@AloNews ‌</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/135850" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTLWqMUHXIDf7MTg1aPsLzKn6iWSzA49iIGfkJKpycMwxAdUen1FixaT8N6hwnS_eCaEjh4JPG1IoJ34R2Wy6LQPxZKTZtT6ZYhlyXiPWaLMCg4vWY-jiSsxZh-TCYAorEmD-vx2Qgfm-sidsDSNaIjQCVqMQcGagXlZcIcZVExmoThovB0C7EZGyvWoo8nG0gSNzHgFuPTdtfn2eas5GmyoMNtVTNBbhrXoPz7VzaMs1MV9u-PrwhEKhn2H5IZrAJ0hqjyerzlTcKELFdBtuGRckwTp2lnfQTBEXY2tn1jm63OQ1bSUnzd-mfMkaffLMsviwZhRvfC9OXejAXjNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما قاتل رهبر رو نشون داد
✅
@AloNews
‌</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/135849" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UpY321M0t0WVAKwEzQC65i7_Ia9KL7K_sDzKV9EjhZX9RtmERTCIP6zdewMIDLwDu4NQYPZFDIVuqFhxe8kyRerYAvys2mkfJxYy_MJwtCIA6gIFM0EAY2C5c8VcGDsBp1R2Yj2YtJvNYQ6-czrxNis2FCVZ3hZ7ZtLgx9JEusSNEARb-Xy1gtFO6ylNKDfTgevA4J1dQ5oYuOqLWEFZLtIeNpfiFOsrlcDSvnf_x2055iVvaxhQxOAf9xlaOtpADHdc3Z59tCntzjKQkLJ6wK3m3r7nTv178pJJ8GLkPOpmvV458OFeKdXPB0a0ZC8uvptSReyU-xpRStOeh9kvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسپانیایی‌ها و ترامپ جام رو بالای سرشون بردن:
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/135848" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135847">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=P_iZXHjK4fFws1xB7K7iBY_fQxdKSTdsvMIuWB87KAbfZXQm8l0hbCnewKiVDgR35qlNtA0V-bCkIhdjHMqqUGnzkjc5VF1du6EafPej-Zmw-Hj3XEjE1_eHXAJgPPun1Iw8so6Ch_MoXRZBtEa9ERbe7G_EcL8pF1cKtOWG9pTC0UedcMp_vkn6zSBQWJiuuYw4I7AnGjMrnbJwYyclJEn0uU3h6hEwY6heNgzm2KK1IefOWd36-tmPzkSuIZHDK0Vsg7S7_pzW1uDnywNejm2nl9Rk_l1JKwxSfzyR1QXmNjrMfZL0zQ8rbRhJa0-DoySDyJSHZkrXnSUiOI_Y2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=P_iZXHjK4fFws1xB7K7iBY_fQxdKSTdsvMIuWB87KAbfZXQm8l0hbCnewKiVDgR35qlNtA0V-bCkIhdjHMqqUGnzkjc5VF1du6EafPej-Zmw-Hj3XEjE1_eHXAJgPPun1Iw8so6Ch_MoXRZBtEa9ERbe7G_EcL8pF1cKtOWG9pTC0UedcMp_vkn6zSBQWJiuuYw4I7AnGjMrnbJwYyclJEn0uU3h6hEwY6heNgzm2KK1IefOWd36-tmPzkSuIZHDK0Vsg7S7_pzW1uDnywNejm2nl9Rk_l1JKwxSfzyR1QXmNjrMfZL0zQ8rbRhJa0-DoySDyJSHZkrXnSUiOI_Y2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اهدای مدال طلا به بازیکنان اسپانیا توسط پرزیدنت ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/135847" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzcQzsWzEQLfFYEcLGIvmBE47osNWDbABMY7Uv1StwbhtNE-EFr4O0WtN1EKZvnRLOWGoWxFMRU3qxNlj6MEvJHVWk9E0MUZvJOZ6rVclB1bdbxjFYAaRFMNS8dOAb3lRsfCoDP4rnyLVNI4kNhZKxeBMofodd4UpNHirPKp-3W0DsVGmg8vpaZ-xBPTI5BCYFYhcpWoaUoMKhg_IFPcU9f1jJ-xyH4wN-usA3R7AhwE61OV4daLkELPHK6c6GsyujwLu2q_Yp1mZzXh-mL5MvGybCg8nSLzryiKdakYtozeJ7_Uv6DxmL0uqswsJ3qqGCPijkUcPvu9msA1M7Naqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت عجیب ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/135846" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLH_3H2uQ2uY4ETXopgUGKVmeeOQwRWgMb8CLDNIgIjGqQQR6p4rQVBh6LFezKc-sFMh4bld3Xsksm8zJmsgsUW4sAHP3g20yuV-V81amp6Ckka210v5-RD0W-uDZqzc7bXKvrux3TMB40xfTmFYH5PKvRnhq4MLocYDvIoQ6uiVjHpRXQmBmDibc9eY2GY6icznr-6PphLeIfJM5-BoDXw3Tchx19eoqfOBv6BtYoLno6PxiMBZ8G1ZU_UoLeaQFQhB6kionjaNlvHytc5pUhaOSEc5rtXDxgUZ87xtcNwoTqZgcL4b1UpZ1K67gKb1jOosrhtPMnXOjG6OiB4U2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گریه‌های مسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/135845" target="_blank">📅 02:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135844">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مسی گریه کرد</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/135844" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135843">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
مدال مسی رو ترامپ داد</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/135843" target="_blank">📅 02:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/od71Jtz7tYBHjbCkSp5TiDJ2D4mbsHogoqZvS12rJm9SSR1_HjmVd2hFuUzR1bKWg_YYxpQm-hq966j-q6NLN9BBLDn_7xdGW4H2-WkmP0d8n3h2lhkT0ajZlC8N7wTRHvfz-eBmcsRjpNMuQruJ-6BWZExYAA-6f0ihICkgI5KRA2bXUh9hOjbQww2KzgBCiAq8FbNbNvklBCyHgY353bCi4V10YLE9chdXORvlC-wkFQfWtZg236mqznmO98knex7ubPM3DvtZjy30XUvfTgABdwlYZcf4tHiJoIa_S3XQ5k8uPMFVyKJvfaEz4XWuKj8YtmexCt2pg8euja1GHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ و بچه‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/135842" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ برای اهدای جام اومد</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/135841" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52273b72da.mp4?token=Ffa2gMuCKRpN_-_3I3Tw5rU8b8_xvlQ3S7Hmj6d2tivF5eoIZJMY3lYJBfNNE9VlNmu8OzhX64oYNutwvwwaMm7lGaJ78gffbqOPFe6rRC5tyIvAnZ4bEuTJi4SFYCCPVxA6Fa1cQhVqja58VIMhMgajlRR4YHcTZOTE-C2_2LEiYAhgISuLh2ZzvfGgHGGMVsfKnxli7ep8QcXZBYRh55NO1Rpn_WzG0vOwJSJiNJpqTpd96wHBqqcMNgsoAIR6CEV-tdBMNiwV9ErbvDqITpXufP_MgbinTJSwu6xs22dpeowL45F2AKT2tJN3SkSOeLQefqGP1oy7b7_IRjP5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52273b72da.mp4?token=Ffa2gMuCKRpN_-_3I3Tw5rU8b8_xvlQ3S7Hmj6d2tivF5eoIZJMY3lYJBfNNE9VlNmu8OzhX64oYNutwvwwaMm7lGaJ78gffbqOPFe6rRC5tyIvAnZ4bEuTJi4SFYCCPVxA6Fa1cQhVqja58VIMhMgajlRR4YHcTZOTE-C2_2LEiYAhgISuLh2ZzvfGgHGGMVsfKnxli7ep8QcXZBYRh55NO1Rpn_WzG0vOwJSJiNJpqTpd96wHBqqcMNgsoAIR6CEV-tdBMNiwV9ErbvDqITpXufP_MgbinTJSwu6xs22dpeowL45F2AKT2tJN3SkSOeLQefqGP1oy7b7_IRjP5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قلعه نویی قبل از واریز 140میلیارد پول
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/135840" target="_blank">📅 01:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135838">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QczISdx46XLBmFkVY3SojE6Od2wgKxKbbGND7yVj-6jqAYNdTn4DMLhvwIVpOoHxlQcYs3UJtrvZ5soB-KsGlAP5251MKTKjrdhiHZSkcacMyYwej4KWiocJhy0CJdn41Sbu-CAigM54rOYNHOIFzkarXeAuwgwXrsOSfF-soIY5uJqEJFpDN6rFrFycNM8m6y-QszpG1DDDdlpLwWTvLDSQxgv6QsuFPQAu06VG4CjXxB2i_c0oOBB-CuktZ_gCkByIaXZOEY_VGO4jWqS1nEQoLBCdSixj-8B0SapN68CA_CNqZkbDEQqjBCrg0GQOn6fL7qYdTRz6JbODxYqaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAM0Njnsb38nTYXmYIFeh7t5so1_0ekzyCoMVPCJdoe88T-dby549y7-uVe15YOy7r-ts7yc3-3J-7v_I97aLt618BV89tim91PbFhiOKm_yQg2L9yY-plymGMhnJHe9hdm2H96YFu_Fi-TaNu9WHrC0rcJnpwD6sc9Kcv9b2H0aF8F5_oY6mkZzdCHoVSn4vG57uXAYEkKcU3yDxk7H2fuqDvp0H2QoIoHmKftck0Np_kVq_q0t-CpTc_mHo8DW3bCI3J1O-FvfNX1cp3rMExEQfuI1eukLHArLndokaD0Lp-d9GJZsqXWRC46pEubeqblolxjT-KQExnJ0WEY-Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مردم روی این دختره که امشب سرود تیم ملی آرژانتین رو توی ابتدای بازی خوند حسابی روش کراش زدن:
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/135838" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135837">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6163e56d.mp4?token=f04ZEjpHpbvTOaE1WCm93nIAfxY4EfGAtdk-i2cRfinMlcoyE9WRFJKwJ_-w4CPmsmi5kl1-Vt4aV0msMqJb2JOoFh80c3I46JpRpW4490MZs_6WLUGvKe1KMf_gKBz7LjpFeLGM5t-fqT9qfT2qNmr1fBIuuyf7tVQi2aQzPcvIRdXDOpezdHHOzS5T2VzlhR8N1t7vFvjlGheNze2mITwvTsBJx00UPQiGYSPf__rok26PKCMwTFYYrLdug_FysTy57t72N2H7h06NkhIdEdwwjpGQDiu5RypWNGWfo6FJpFVUHKZ7b6tLdNIwky0AkRYcuUIGjSSTp6HaiPFwlTF_fuuMxOGcC4Va8GhckEpyZtkkeri6jK64YCbyzyeCQjjYV_BuPZ40T86aRe2wSf3TbQ5XAl4ILmZxu_r9-KLB3wEQ6uy30bo8Gpx153mKIC3PBoBd3w0HqX13Fny9-5jdXxnJ5D0lL_E9TjuO1zfLAraT3tqAkv-C7sVAgANZQh53qsISGWAeR7thDbBrFVMXqfBCcFPHjxD2JjxnwicR9rhJ7288678Nl9AVZTfijtIK5KwurlmohSM_yXN-j1isDoLLb0XLfdHzxmdiq4TP_fAeqVZYiOTRiPM37UEsPpbP-FO3OnJaa6faZy3BQFY-3iOx303ZvEwLxhaU0Es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6163e56d.mp4?token=f04ZEjpHpbvTOaE1WCm93nIAfxY4EfGAtdk-i2cRfinMlcoyE9WRFJKwJ_-w4CPmsmi5kl1-Vt4aV0msMqJb2JOoFh80c3I46JpRpW4490MZs_6WLUGvKe1KMf_gKBz7LjpFeLGM5t-fqT9qfT2qNmr1fBIuuyf7tVQi2aQzPcvIRdXDOpezdHHOzS5T2VzlhR8N1t7vFvjlGheNze2mITwvTsBJx00UPQiGYSPf__rok26PKCMwTFYYrLdug_FysTy57t72N2H7h06NkhIdEdwwjpGQDiu5RypWNGWfo6FJpFVUHKZ7b6tLdNIwky0AkRYcuUIGjSSTp6HaiPFwlTF_fuuMxOGcC4Va8GhckEpyZtkkeri6jK64YCbyzyeCQjjYV_BuPZ40T86aRe2wSf3TbQ5XAl4ILmZxu_r9-KLB3wEQ6uy30bo8Gpx153mKIC3PBoBd3w0HqX13Fny9-5jdXxnJ5D0lL_E9TjuO1zfLAraT3tqAkv-C7sVAgANZQh53qsISGWAeR7thDbBrFVMXqfBCcFPHjxD2JjxnwicR9rhJ7288678Nl9AVZTfijtIK5KwurlmohSM_yXN-j1isDoLLb0XLfdHzxmdiq4TP_fAeqVZYiOTRiPM37UEsPpbP-FO3OnJaa6faZy3BQFY-3iOx303ZvEwLxhaU0Es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Comming soon.....</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/135837" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135836">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گویا صدا و سیما مراسم اهدای جام رو به دلیل حضور ترامپ نشون نمیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/135836" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135835">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIVdJ9vLRunhhLHVRw-w-s1XZWuVxMlI9o3yeClJ5Dx-LrunbLGkBK-aq9e0xQGaNxu1szaFVItKH9NyFinFaPHNTjhZVw2HNbUuRwWlUI5c9F7LIMD0pbp6SzsF0hmwlTcETdu-mEDivzvl7gmVhJCC_-Ne278RNKjPJoM49j77wbvdi47gbytoZ_GZE0Tk_-8Y4Kw38cDtKKHg6eF3x2li5UTm_M3aSKzvpcsXkiXbCvgsofIoKBXweHaXfAZvWkGpJ8su5CnIi9-nwxpwEqfQzhfI60t2v-gJLWgV36U04Ykdn2fDRu-nf-RkfNpGvu1YCrHGJD09BoowUyKrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت مسی بعد بازی
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/135835" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اوه اوه پشمااااااااااااام
😐
😂
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/135834" target="_blank">📅 01:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
تنها دو تیم اسپانیا و ایران نباختن
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/135833" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135832">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xzw_Gmdms7SGIIaRfCWq_rnpbzSDhiyDhS05eNG58DFKBvL11swBsx_b0Zkn_E3CLLbxNS_yxnPxEuVoRJZ6S5rWJWr-redR7oZPEHQeWW86rxVY69Z_N2DijJfW2zEcWuTJHCmf8IIgltXwgdxBC_9NGY1VeySLkxGDi_GPtNvrZ6O7kCFFQ8kRHG7uRCPMkE5wFiikNIoyqbNuolpSxcMvpg4Hgxzj0BgBUjoJ4r3OzoatYHRVhug7_koixei1FasSn7oULPRH1s6fI_vAjJbtftkoeXiyFcqsFAPPEwwAGoHssWTqOQUiValltoHsBKPJypR0snKHUmIFIsN_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلیل قهرمانی اسپانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/135832" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135831">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اسپانیا با شکست آرژانتین قهرمان جام جهانی شد</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/135831" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تمااااام</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/135830" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/چند سوخت‌رسان از عربستان، برای عملیات علیه ایران بلند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/135829" target="_blank">📅 01:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135828">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فک کن هم طرفدار آرژانتین باشی هم طرفدار جبهه مقاومت</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/135828" target="_blank">📅 01:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135827">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کجاش آفساید بود آخه؟؟؟؟؟؟؟</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/135827" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135826">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آفساید شد
😂</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/135826" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دومیییییییی</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/135825" target="_blank">📅 01:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135824">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مجری تلوزیون: اسپانیا طرفدار جبهه مقاومته و ما خوشحالیم، این بهترین جام تاریخ بود چون هم ایران هم اسپانیا نتایج عالی گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/alonews/135824" target="_blank">📅 01:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135823">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5g-nhVjXdz56-mMFIYejET1YK0tH7MT2VOO7D8FG0KFdYRXsnCDHtrN4k1iEWnyjkGQdjiDZ0hEEuodoO46YOgPpwzub6g9kcvH6M9At0IBv-r7s8OJmWQi7qj6YhBzfVjayO2U8KS4fySINvqIn6GejVYdN2jGRtWLK74iAGKDKlqE-R6-40bhzPjvr9Dl9PDjojijg3mak9lDhYHkZglxbCAB4zwJDHXSySdntbnAooGkm9X6DMtao_DSuxW-AsQ8bRbTYo4OrOEW5zvb8-FuToAXSN6TfDk4nDi3uxd_-PeHU-lOb_7dIhbr5GztVTdYOZrd3eWohGVgGzSVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفانتینو بعد گل خوردن آرزانتین
@AloSport</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/135823" target="_blank">📅 01:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135822">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419e6d9637.mp4?token=uENz_8VtdPUmRXeQ3DT5CUt8YAZHFZGvV9uEuh2En3eJxRDbliPJ9CTwoIM3t6HD7wpQKjr186Y9ZCmCRcj4lPkISF1V4uLQyLIs307sUg0rY_m_C3TnKXPS2LuAnRdrufEW0tDeIGUFPWPUkrXG0MLKDEl1JuvI0_fXlpwegP5FIcUJDhKrAMx_Y4hzAzBKUJ0OKQGN1D_qsJAMD5lcxuexFNm3F0ABzuCM1i2tDTP1Rj2UqBoIIFZyWoRoJrUSKzEfGxxeYCVoQMS1AlPn4N1EQsvDfr_eByiK-4sIs47jH9OFUNcgCqibD4NtY7IJR9TLWImilG4D5riHhXK0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419e6d9637.mp4?token=uENz_8VtdPUmRXeQ3DT5CUt8YAZHFZGvV9uEuh2En3eJxRDbliPJ9CTwoIM3t6HD7wpQKjr186Y9ZCmCRcj4lPkISF1V4uLQyLIs307sUg0rY_m_C3TnKXPS2LuAnRdrufEW0tDeIGUFPWPUkrXG0MLKDEl1JuvI0_fXlpwegP5FIcUJDhKrAMx_Y4hzAzBKUJ0OKQGN1D_qsJAMD5lcxuexFNm3F0ABzuCM1i2tDTP1Rj2UqBoIIFZyWoRoJrUSKzEfGxxeYCVoQMS1AlPn4N1EQsvDfr_eByiK-4sIs47jH9OFUNcgCqibD4NtY7IJR9TLWImilG4D5riHhXK0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گلللللللللللللل اووووووول اسپااانیاااا به ارژاااااانتیییین تووووسط فرااااان کوووسه دقیقههههه 101
@AloSport</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/135822" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135821">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسپانیا زد. فران تورس</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/135821" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135820">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/135820" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135819">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuTjyAm9H2KKBtB1MaE3UY0jPnWz2UC3CDjEsTXPW0XdOMwLEFoI087pBpgZ2hlhX9bQ0FrnHnB_ZanRkKzZCjzwkQ7V2a4RRPomM5LO2d_xdiaBqe1MeapbgJA-TRNdpG_FmZGZNgzHvY3_rxiDia5zD2SnqD9bMkoxwOvJ5qwFYFcuKsVLyT9pNSjihN1PtkBgjJ-wCxZk7a_cgIFRwxfLWtNserUqGr28L1hveksOzTTHrbCpeRGrjkqTgu7dlg_kdGPyvgVr_Kmh8vkd25jopIjhL9z87XUyPyET9lcI138tr0WY-5QqO2ypsVgc2DkzvA_VmEP31GrhjPrqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پسر فیفا
👍
👎
؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/135819" target="_blank">📅 01:11 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
