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
<img src="https://cdn4.telesco.pe/file/TF5VU5EXClRNOWjcIzWzl57iqYxUzwjq_8beCc6MU455pTd7H9xnNvSAP1AJWQIz_H-jrEzaUp525VoHVKoFf5jpa9VxSV7Yq99avX8acNk5q4CFG7k9NsTZzSZSeS3LpVubPU00PJwBNWcfEW-7ULPudr4fWCTzkFPZtw8Ttapi5jS2_5rcvVvBhy_9ov6035OM9gW-z3gOuG14cO4NMEWaRvQdEnC6wfE_vi8xyRjUQWl6ljjcCTCoFoAU0oqMxiOSiPXZ5irapoGKLtJhlEZ9B_XGOU9iInnSgWK5pxoie1O7aK3krUu72y7PIePwTRZ6wfV92TVKwTKAozgC2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 10:20:44</div>
<hr>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، امریکا درباره کوبا: من مطمئنم که تا پایان این دوره ریاست جمهوری آمریکا، کوبا در مسیری غیرقابل بازگشت به سوی آینده‌ای بسیار متفاوت قرار خواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/141268" target="_blank">📅 10:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbB3gzNbmukDGk2JfjzIyFmT5muiy4K3AP_it11BnWDKklESLsvBIlnUHAYlN9XMZr4FiGfncIA-K4vs_QWdfxx9L1pDBUJxnWT9LXHQ8ogU-L29wvk_g2lGqQEpIiZxZslNtGOJ5hIvBasj_4jwrXqAuhL_aX6laj1bIhJ-iROgMGqg3-R_iFaIu6Gc6FTZivlpPRE9APbEX6JjrF1sSu_G3GaZgmv-iwYLKUjH8m7at5z8cSYlND55RpDXaGCM9pjW260hErYge9YPli07dq7y3_dk3R5rPJciqKMqdWJTr4AQCXuhqli25sHHnLIO4WH3w2cv14CQ72geBDF6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ایران فعلا تنگه را باز نمی‌کند؛ جلوی امضای توافق با عمان _با جزییاتِ مدنظر آمریکا_ نیز گرفته شد
🔴
مُدل پیشنهادی ایران برای عبور از تنگه (شمالِ تنگه، مسیر ایران و جنوبِ تنگه، مسیر عمان) قرار بود برای ۳۰ روز تست شود و در صورت انعطافِ آمریکا در حوزه «تحریم ها» و «آزادسازی منابعِ ایران»، دائمی گردد که با لجاجت آمریکا فعلا همه چیز متوقف شده است
🔴
دو هفته‌ی آینده، بسیار حساس است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/141267" target="_blank">📅 10:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: کشته شدن ۳ نفر از شهروندان ما در حمله روز گذشته به یک کشتی در دریای سرخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/141266" target="_blank">📅 10:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شبکه الجزیره در خبری فوری از اصابت ۴ فروند پهپاد به استان اربیل عراق خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/141265" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
الجزیره: قطعاً بین ترامپ و نتانیاهو شکاف ایجاد شده و ممکن است برای یکدیگر به «بار انتخاباتی» تبدیل شده باشند
🔴
هیچ واکنش مستقیمی از سوی دونالد ترامپ، رئیس‌جمهور، یا کاخ سفید [به رد طرح پیشنهادی صلح ترامپ در غزه از سوی اسرائیل] وجود نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/141264" target="_blank">📅 09:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141263">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae5a508392.mp4?token=GV8dvDkMZGTjtUjGsO7Ktj0gJPFKvXjnow2Sz72simYTPBDKTPbooXGQNjFa0lDSrCZKGvOYtrr8pdAY12BC26i8oegMgr7j1Iz9HEkndUvy49N2pRauh4_Oq1_HVG6xAkQ4eWLHvNdg9KmPxjwnuwAt4T5zgax1brumsYXJVWti8hslQpZiIN_mAZHnqUoHy587uy1nHBqGlGygry5Mys9trbiUUT8rqenvRdBjRO3o-Kk2Y1cPTOQcQgyVQ4r23MuIMNBoQpj5LIihLfyirfHXs4M_YR0cVbBFxDXYICt0l8hPUlVre3BACZQQMt9r4J6IkbW8zJw21WaXhe33cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae5a508392.mp4?token=GV8dvDkMZGTjtUjGsO7Ktj0gJPFKvXjnow2Sz72simYTPBDKTPbooXGQNjFa0lDSrCZKGvOYtrr8pdAY12BC26i8oegMgr7j1Iz9HEkndUvy49N2pRauh4_Oq1_HVG6xAkQ4eWLHvNdg9KmPxjwnuwAt4T5zgax1brumsYXJVWti8hslQpZiIN_mAZHnqUoHy587uy1nHBqGlGygry5Mys9trbiUUT8rqenvRdBjRO3o-Kk2Y1cPTOQcQgyVQ4r23MuIMNBoQpj5LIihLfyirfHXs4M_YR0cVbBFxDXYICt0l8hPUlVre3BACZQQMt9r4J6IkbW8zJw21WaXhe33cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله توپخانه‌ای اسرائیل به ارتفاعات «علی الطاهر» با گلوله‌های فسفری
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/141263" target="_blank">📅 09:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141262">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
هشدار سازمان غذا و دارو: با توصیه هوش مصنوعی دارو نخورید
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/141262" target="_blank">📅 09:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141261">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
مخالفت عربستان با پیوستن مصر به «توافق دفاعی مکه»
🔴
گزارش میدل‌ایست‌آی از یک تحول راهبردی خبر می‌دهد که ابعاد تنش‌های پنهان میان قاهره و ریاض را آشکار می‌کند؛ عربستان سعودی علی‌رغم فشار آنکارا، با ورود مصر به توافق دفاعی مشترک با ترکیه و پاکستان که هفته گذشته در مکه امضا شد، مخالفت کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/141261" target="_blank">📅 09:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141260">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نورالدین الدغیر، خبرنگار الجزیره در تهران، می‌گوید: مذاکرات ایران و آمریکا درباره تنگه هرمز ظاهراً بار دیگر به نقطه آغاز بازگشته و در شرایط فعلی، توپ در زمین واشنگتن است
🔴
به گفته او، ممکن است تهران به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
🔴
با این حال، تلاش‌های دیپلماتیک و میانجی‌گری‌ها متوقف نشده و احتمالاً در روزهای آینده اهمیت بیشتری پیدا خواهند کرد.
🔴
الدغیر معتقد است: میانجی‌گری‌ها می‌توانند نقش مهمی در تعیین مسیر بعدی مذاکرات داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/141260" target="_blank">📅 09:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141258">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWcPKSt-LFWrMGOsjEhdt7y1itm837EAofwOAWntsi0I5CUFREtThur5FuPQBWLC2fMFvtzMKHnmKWDqz0mG98SZ3uMQBXiDC7p-s58sKjN7ywJ9-6YOeQzlfBCq6KtpsPfy0lBx1xs_BSyfsOWhnAJYb00zuHgv5l_ZczMZHI33nEfzOWRdMC5O9O3UACEznpvT0O7qel5sAlVkLZPI2VS48q86Fyd5TbXDpkrPjeavOuv26D6hBTyCH-JkXsANDkDIW5ecIKpsYZs0Bkd5RT012nIzh7jUnywUOBdQbd9MgC-ZA1TN3eU7tUh2jaiDuEKzqrMnVoSpogH4Px_LMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0a4d934f1.mp4?token=ggv7sacgVAmV5oMuNWHnmTgMcXdj0M06rQWSNDPx0ZaXPD_cW0uJpU3vj5qZKyOiDh1xdqrGyLdaHYxtxpi4AwLatF2ci7_WvH8E86NSeofF4Znk5bBHNPwre369yxZpjlJ1ecwBiO80O-3nlwTrcNDz5gwW2JWz7b1act_hg7kWs8TNmZzHxdorRfsqbFnzIRMI6IiOKF0x6Jn6D3vBcapD0E-k-3xkcBorZWdeW2QTxSOJEDj8xi41iRFLoZx9IPSCHqxKE1NREOwJPIgO7CrPZw1cDtmDizvvUZ5Q_icszhSJFXczdtqO3slhzbGmYjZTFMIu-HgGPIRO2w7Apw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0a4d934f1.mp4?token=ggv7sacgVAmV5oMuNWHnmTgMcXdj0M06rQWSNDPx0ZaXPD_cW0uJpU3vj5qZKyOiDh1xdqrGyLdaHYxtxpi4AwLatF2ci7_WvH8E86NSeofF4Znk5bBHNPwre369yxZpjlJ1ecwBiO80O-3nlwTrcNDz5gwW2JWz7b1act_hg7kWs8TNmZzHxdorRfsqbFnzIRMI6IiOKF0x6Jn6D3vBcapD0E-k-3xkcBorZWdeW2QTxSOJEDj8xi41iRFLoZx9IPSCHqxKE1NREOwJPIgO7CrPZw1cDtmDizvvUZ5Q_icszhSJFXczdtqO3slhzbGmYjZTFMIu-HgGPIRO2w7Apw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات گسترده اوکراین به روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/141258" target="_blank">📅 09:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
به گزارش نیویورک تایمز، آمریکا در یک روز حدود ۵۰ فروند موشک رهگیر پاتریوت را در خاورمیانه شلیک کرد که هزینه هر موشک حدود ۴ میلیون دلار است.
🔴
یک کارشناس گفت ترامپ تصور می‌کرد جنگ کوتاه خواهد بود و ذخایر موشک‌های رهگیر پاتریوت را به خطر نخواهد انداخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/141257" target="_blank">📅 08:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0dffaedf3.mp4?token=VAkvltPBCB4bK4QytC_595JlewpN3IRJmKBNTn1CCxLGaeDzysSr02lm0Xdrhl_jySDus8Eusw4zyf_2gGIrHXScVFN9tTMBnjU8mVheRtsWLXQY2VThLV4XI9X3Sa0m56n2Iv-zsIGrUWxAqL_JkFfzEA0GzrixK_smJYEiVFb6Gddt3PzqvxpBEoqh8T_-Zzc-hw8cgytCwsH0ClWwHpm3ynO1gSw1jQ83G0KRr1PI6spKwQ2WLhfLsUvAvBHwyUguI_m-iGGbbGpgDGgOPtdEC_jbLFqP8Oyw4Yop96U8Yva3CKxM2da8NHdYQZvzgWw3DoqX7zMOqEwLJjRdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0dffaedf3.mp4?token=VAkvltPBCB4bK4QytC_595JlewpN3IRJmKBNTn1CCxLGaeDzysSr02lm0Xdrhl_jySDus8Eusw4zyf_2gGIrHXScVFN9tTMBnjU8mVheRtsWLXQY2VThLV4XI9X3Sa0m56n2Iv-zsIGrUWxAqL_JkFfzEA0GzrixK_smJYEiVFb6Gddt3PzqvxpBEoqh8T_-Zzc-hw8cgytCwsH0ClWwHpm3ynO1gSw1jQ83G0KRr1PI6spKwQ2WLhfLsUvAvBHwyUguI_m-iGGbbGpgDGgOPtdEC_jbLFqP8Oyw4Yop96U8Yva3CKxM2da8NHdYQZvzgWw3DoqX7zMOqEwLJjRdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من به ایران اعتماد ندارم، چرا؟ مگه فکر می‌کنید به ایران اعتماد دارم؟
🔴
من آخرین کسی‌ام که به ایران اعتماد می‌کنه مدام به من دروغ گفتن، الان ما کاملاً کنترل تنگه رو در دست داریم
🔴
اونا کنترلش رو ندارند، ما کامل کنترلش می‌کنیم، مال ماست، شاید یه زمانی کاری بکنن و اون‌وقت کارشون تمومه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/141256" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e1e30aad.mp4?token=aSBLSiXa_CHOeKmP4Q-yV8S8XZKaT0d-Ms4KFTw3KA2kFACou9YFDW_6b89eganKSaDOAZiA2DuynPxUyLIu-28Y6JrfOs_qfirVuRckAEXfqjxPTda8KRhqvrjynJY5_2f6Vb9Cql1Joe-j4gyPeyIcDPIe3nYHfFgYA0flBZ4xYeflXdQdcy2STNOxpKnD-LGYy8vADnc5jRrb8p0WTcQthnv8sMkkCTjDut4kOidZSHmxccYgM0iJh_9411Vm_OPtdpyQ4T58HskyfzyhaiXfF5HcPDZIOfk6pSvC_jlyZzsbkDXjrqYiAFNXxIACPpwiCjDxbdhtS5jBn_O-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e1e30aad.mp4?token=aSBLSiXa_CHOeKmP4Q-yV8S8XZKaT0d-Ms4KFTw3KA2kFACou9YFDW_6b89eganKSaDOAZiA2DuynPxUyLIu-28Y6JrfOs_qfirVuRckAEXfqjxPTda8KRhqvrjynJY5_2f6Vb9Cql1Joe-j4gyPeyIcDPIe3nYHfFgYA0flBZ4xYeflXdQdcy2STNOxpKnD-LGYy8vADnc5jRrb8p0WTcQthnv8sMkkCTjDut4kOidZSHmxccYgM0iJh_9411Vm_OPtdpyQ4T58HskyfzyhaiXfF5HcPDZIOfk6pSvC_jlyZzsbkDXjrqYiAFNXxIACPpwiCjDxbdhtS5jBn_O-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
تهدیدهای زیادی علیه من هست که شما ازشون خبر ندارید
🔴
هر رئیس‌جمهور تأثیرگذاری تهدیدهای زیادی دریافت می‌کنه، رئیس‌جمهورهای بی‌اهمیت تهدید نمی‌شند
🔴
فکر می‌کنم شاید من تأثیرگذارترین رئیس‌جمهور باشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/141255" target="_blank">📅 08:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ درباره اینکه چرا خودش با ایر فورس وان پرواز نکرد ولی خبرنگارا پرواز کردن : نمی‌دونم، اتفاقاً فکر می‌کنم هواپیمایی که من سوار شدم بیشتر در معرض خطر بود
🔴
خبرنگار : چرا؟ ترامپ : چون فکر می‌کنم همون هواپیمایی بود که احتمال بیشتری داشت هدف قرار بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/141254" target="_blank">📅 08:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65563b805.mp4?token=uPbpRFcMui5nHZKMK6kZ5iwbg0omozFqhckEn75AHd-mRdSKuXk4NDxEU6rl9SWXtYI-3dRXSRZckHL2tF6LBncdlnQx3b8fIJ_Av73h1Qog2kpygft4eLxJmCQ3Qp4rdejFnN4pa06BdxuwwQyXQMRotn1emEMyya-WIIN_eW0iwv9gIvPfXZXyWRaBwEvSDWdMEm_7aTiGmaPqFzbej0yrLCajwh5nrb7sX_o-5HCdUNp5nhdysvpfl2ymEhRoWEw2pt-iVYcV_gDNnVEW5SjhZuEYC0ClIYpzUjF-4QCRkg__i__uM643ZUv2B2UmPtRwIhn-wYFGZh7ugCxxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65563b805.mp4?token=uPbpRFcMui5nHZKMK6kZ5iwbg0omozFqhckEn75AHd-mRdSKuXk4NDxEU6rl9SWXtYI-3dRXSRZckHL2tF6LBncdlnQx3b8fIJ_Av73h1Qog2kpygft4eLxJmCQ3Qp4rdejFnN4pa06BdxuwwQyXQMRotn1emEMyya-WIIN_eW0iwv9gIvPfXZXyWRaBwEvSDWdMEm_7aTiGmaPqFzbej0yrLCajwh5nrb7sX_o-5HCdUNp5nhdysvpfl2ymEhRoWEw2pt-iVYcV_gDNnVEW5SjhZuEYC0ClIYpzUjF-4QCRkg__i__uM643ZUv2B2UmPtRwIhn-wYFGZh7ugCxxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
،
درباره نامزدیش :  دوست دارم دوباره تو سال ۲۰۲۸ نامزد بشم، ولی قانون اجازه نمی‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/141253" target="_blank">📅 08:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ee228998.mp4?token=Rim9OcFO3USdbw4n1Mw9hDBhxf5bmxolTzRucCr5leygc0uwW-ixeGzVnb3s7Mv-UWRs27qs3E-j2Jpjy45g2a7HGRv7G2jRH2yt-5NBoKNVVjViSZvFAHcoLR77tr6jLzGSF87yeNTOeT4KSqmcblvP9hQ-EhXwxSzEDkZzTy293LWATHJhkghpmzmfXD9ViJJACQSzaLoe9XzsuyOS1-iVyPGD2LorXAmHhmr22AtLB3ZaDuDeDqzUGY4vMquvx0jxJHw1uQIrQ397acMuyY8KelYF71xDSBRxV81prWsk-oLQSTxm4NhtP-QmUgS2XenwJ5PKqAwL1hArzGtvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ee228998.mp4?token=Rim9OcFO3USdbw4n1Mw9hDBhxf5bmxolTzRucCr5leygc0uwW-ixeGzVnb3s7Mv-UWRs27qs3E-j2Jpjy45g2a7HGRv7G2jRH2yt-5NBoKNVVjViSZvFAHcoLR77tr6jLzGSF87yeNTOeT4KSqmcblvP9hQ-EhXwxSzEDkZzTy293LWATHJhkghpmzmfXD9ViJJACQSzaLoe9XzsuyOS1-iVyPGD2LorXAmHhmr22AtLB3ZaDuDeDqzUGY4vMquvx0jxJHw1uQIrQ397acMuyY8KelYF71xDSBRxV81prWsk-oLQSTxm4NhtP-QmUgS2XenwJ5PKqAwL1hArzGtvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
اوضاع ایران داره عالی پیش میره ما کاملاً کنترل تنگه هرمز رو در دست داریم و نیروی دریایی‌مون فوق‌العاده‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/141252" target="_blank">📅 08:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e66e57720.mp4?token=rPktAjh2L5p4AiywyCJ9-TYd9gAvFDMBEPO_vuov0N-LHRXrQwfx4NvoXaT9QdMrOELlLP2_WanYdbDPVbkpXVWb--MbWKoML5im37-rhUy-8OR3newr34BTcbwaQhAj1Hb9omlD7jsO1GlT6oTbMa6TtlL0NYfDlGoMtkyaMrIGPna8vmnCzwpWjD2F3RiqetKvagYrnoF92j1Ocr61T7wVSusFDT2fYr6n-yTg6nsfJk2wAV85TvpgSl7Wohc3A5R7iVFdOC9szg80n-JYJsM2-Sln0Fxf5szDMHEPQd9T9e3BB4Nq8LXpSjz5qi7z9UI5OQ4jodgDQY5VK9I3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e66e57720.mp4?token=rPktAjh2L5p4AiywyCJ9-TYd9gAvFDMBEPO_vuov0N-LHRXrQwfx4NvoXaT9QdMrOELlLP2_WanYdbDPVbkpXVWb--MbWKoML5im37-rhUy-8OR3newr34BTcbwaQhAj1Hb9omlD7jsO1GlT6oTbMa6TtlL0NYfDlGoMtkyaMrIGPna8vmnCzwpWjD2F3RiqetKvagYrnoF92j1Ocr61T7wVSusFDT2fYr6n-yTg6nsfJk2wAV85TvpgSl7Wohc3A5R7iVFdOC9szg80n-JYJsM2-Sln0Fxf5szDMHEPQd9T9e3BB4Nq8LXpSjz5qi7z9UI5OQ4jodgDQY5VK9I3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شیوه جدید کلاهبرداری: گوشت بوفالو به جای گوساله و گوسفند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/141251" target="_blank">📅 08:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141250">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0bRDGgJ1_6-1a4caEaDfnJgOsWld-cjchpsaz_Qh64K1vXw7YKotFe0o9m9iYYWhbDe5l9oyHqeDHy5FMUnx-Jx5WyOYjDPW60sqk0tJKxyJtq_hgv8FACMbrcb8jzLacFtkzYWk7CB9OEjpCCYtkQOV-t9LXXCPFJt4X-JOSacwwqp1T2eH4PZCTlOH2tXWqyMOxLtzHMZ6WWWU3Q8kr8DlTgSqmABloDs3jRVqZ_asrvCGxIXowZK-tU65-2_bxv2Yr9CYR92q_F6J9usIQIH_1FhUnyah52MFq6dx2smIt767UZHOSGlsAftjZ9aUasij9mAL3K8QxgZJ98OaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار نقدی:
پیروز شدیم و به پیروزی ادامه میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/141250" target="_blank">📅 02:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141249">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPVaj4QcNdWFXPM0SgyyacVKRTnbRTIsYjcLPlEXklqbryQ8-eBP9MiLmokuVFucg7ICQLb35TAHFyEKtkBO8CwDc3eoC-V5MQLSr8-YU1EhevYvUp9rpNc78H1xuola8y001Lm18NAc0SixuehoUAhA_NdErqoV8OP6lfLgstDX-A_4ucJOsK2FzSR2l9FSkAAH-YnW64zGgyvdUoyOkeUDAExGzYQc8X_QUK-mhVirYbOhSJP9JU6YyXEmy9PIhLE3bGAb0QejjcbVUwgQtk48CB2x1aVUMBwlr7LJHNL_YmFgycDLAxm_XBuYjSpwqqCSxmAkTCAq2R4oQ6KiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارت شرکت ترامپ مدیا در سه ماهه دوم سال به 238 میلیون دلار رسید - در حالی که سال گذشته این رقم 20 میلیون دلار بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/141249" target="_blank">📅 02:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141248">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سی ان ان: ترامپ دیگر جنگ نمیخواهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/141248" target="_blank">📅 02:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دوستان تهرانی صدا رعدوبرق بود نگران نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141246" target="_blank">📅 02:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ان‌بی‌سی: ایران نفوذ چهره‌های تندرو را در مراکز تصمیم‌گیری، به‌ویژه در حوزه امنیت و دفاع، تقویت می‌کند.
🔴
این اقدام نشان می‌دهد تهران به جای امتیازدهی سریع، خود را برای احتمال تداوم تشدید تنش و رویارویی آماده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/141245" target="_blank">📅 01:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
صدای جنگنده تو تهران شنیده میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/141244" target="_blank">📅 01:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOhAaEEcxp23D99e40K6xfOVKlB8h1sXWufz3Z4H5mQUoUOKiLjCGx02iYtwWV8_VcOEU6ez7EIbU8s8xQQsYHaFlLzZ87eSxhVtE3K0FePgvMMTA-gHxKCmHlkyhj8UaDkqf4O_fXtpkUFDQVdmA9_uN_VapNEBU1cB9iPGHeF97B06QPhVGYLaUo_zitCtb_gKKvJbgB95IZK702RTAcwwkbJAH8XYxK6VQya3yEhs3_5BNQPkDcMA3K6corBMatpzz5b4eQhgNe_LtSWz0iqRNI6kqFJCxyNOBi30GXKRZCWNKkExvTCj1HmH7QujJWmkD7gsCEv9drVObgfdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: آرزوی شهادت دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/141243" target="_blank">📅 01:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zum36wI-E7VVNO8nzJJTFeYrzRpEUetW1xQtkotBJx60nnNR588n4KDQ5PewxWvCvqdCEiumDo5b9LOW13J5wiVT9x761XMrx3TN_tt41UBS8wmEJc-QF0qR9UXYctUV_Eg0tkaSsviIW4YXSmvutF8_Wn1QdfxNLdgtoHBk10S-Ns-VDvTJBOVtCUBkF4jo_BHBS0h8awMVxb5DQ5m9MCYw0FjITg5iDjON9gv9eo4SD5b61HhfjnYCXqvDZ9t-ZEPtPsCJII_5eUSL1-7OS04LjteW40_3cmqDdICQE4vnT5eD1g5DYSVxsamrkFJuHjdqJZ36eecD3th8N02g6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: نیروهای آمریکایی در طول حملات ایران به پایگاه‌های مستقر در اردن حدود 50 موشک پاتریوت را شلیک کردند. این میزان معادل حدود 200 میلیون دلار در یک روز بود، با توجه به اینکه هر موشک پاتریوت حدود 4 میلیون دلار قیمت دارد.
🔴
ایران از موشک‌هایی با قابلیت تغییر مسیر استفاده کرد تا هزینه‌های سنگینی را تحمیل کند و ذخایر محدود موشک‌های پاتریوت را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/141242" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbUpgixL5Y3XSk7jIOKvRgj1yicaZQWh2UmyH8SXMiPFAqVAk7kOkO4BEBKkKhIPfPesC3oh5QQ8OLhgtP7-9k8JfORiETrZK39tLKXzC4crntH035p1fD8cFdamQqhKSJQtqns5G8RqI54yL4wOgsNiHeA907POXajdshnBmJd97wWv1M489zRoPUXOVNGnuHbSVVxPoK8K9vIHUwux-LB21OS_62DG7o7AvvdpV6UlCJTuBo0JcEdhiMqTFTE3Jp1TXwVvDTnXgDYfHiqmd8G6DIB617v5_8_FCix6nBcD5DCaOeUWKpMzXEKPE2oHCJUVuXNKpFeGShaHOH46ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/141241" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLElwHeWTJpD0VEk95kiCS9Pqva_IrncgtEoZ0WWpLl3Z16eD7YW9ZCT04NJ4OIoLPQvPouiwYFl1lKW5QvGvzTXXPx5wfmxuXC8IbtB2VNkBRVjhD37q7Gvm3n9_p867tVRpOr9feasO0ulpc9MG1Z3291wcGqlY5VzDz_MHOHcYeAen5ONuh_xsHxZYwP3JlEs8D-v908hWUiMIXEMUSoTfhhWd-mDQza___snVMQdayv8f3RsdKxEnSt3tBXO65ZwWeVJwCyjLukZGfgOAQuOdGnHYfX7JPsYu76BIV4t606g1yqxI0cXtE4M3tzPkq1CfCKNYT7irz0yfLFFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت به ۸۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/141240" target="_blank">📅 00:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf2v9bR6LlwdjCvLnpDD4fs_O2ja4wRMOqyE1xPUtFrVyHeKGt_KiUCaVTsXAstJjrMCa6bYl1eveOgIlqWUhZL3Qb3id87EE7PYsLQqyp13ZtMqP1XHBI6lqyc2ozAgwXykb_tUa2xbA26i1IXqvnHLmlaekpf73TrLgYE8pm1lZ0lzMvtQSWbxSC7RLRmq1RRSs8Dt64WwUPam7IcI-5tfUVIk-odrCNHUo_RCNYTmgFQ6TZi98Uv29Ojupq4ERgxWLFbXTUomgkNtyKPDmYTrjj3Owl-mtaT-of6uY2FrFqqBSRjj8zOB3YOYNMC5FrWZ2ZwiDnWkHbNKSLs4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک :
پایگاه ماه آلفا شگفت انگیز خواهد بود. ما این پایگاه را طوری خواهیم ساخت تا هرکی بخواد بتونه به ماه بره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/141239" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141238">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c913fe1394.mp4?token=UqCYtqBvLmpH0bgIiKhL5yLAxiYrgcK3IL-S9_wqJQ9QjeUEpgih1lKpxan0gmb94dtBwlV8H-4uhrcZj2wReT8O38k4HubK07vnaMu3JKQqs72uZdWd-TXJscPqyhrvC801lTdk2v7mc7gVZ5shrTIuaX6k_hcw0i78GNEwqYhQM_RJi-FIh2deoUmbUop4PwQYNeN6WbuI4jlIb1q7Z0Lrs4n9ujaJJcPAvQ41lVrfNbkgfccuRtK9bdIy8GrDGLvwMtuNogWGmO63FArjezoq25CRpMpfaOx0qsUIYnpiiweILmcQIT1bbH3Z33eGR3nxdE7Wsjaki5Pi5agq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c913fe1394.mp4?token=UqCYtqBvLmpH0bgIiKhL5yLAxiYrgcK3IL-S9_wqJQ9QjeUEpgih1lKpxan0gmb94dtBwlV8H-4uhrcZj2wReT8O38k4HubK07vnaMu3JKQqs72uZdWd-TXJscPqyhrvC801lTdk2v7mc7gVZ5shrTIuaX6k_hcw0i78GNEwqYhQM_RJi-FIh2deoUmbUop4PwQYNeN6WbuI4jlIb1q7Z0Lrs4n9ujaJJcPAvQ41lVrfNbkgfccuRtK9bdIy8GrDGLvwMtuNogWGmO63FArjezoq25CRpMpfaOx0qsUIYnpiiweILmcQIT1bbH3Z33eGR3nxdE7Wsjaki5Pi5agq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که به تازگی از دی ماه منتشر شده، یکی از هموطنان که تیر خورده با درد فریاد میزنه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/141238" target="_blank">📅 00:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/141237" target="_blank">📅 00:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
تسنیم در یک خبر اختصاصی مدعی شد عربستان سعودی درخواستی محرمانه به حوثی ها داده تا جنگ را متوقف کنند که با رد درخواست از طرف انصارالله رو‌به‌رو شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/141234" target="_blank">📅 00:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نیروهای مسلح یمن: حملۀ امروز ما به مواضع نیروهای وابسته به سعودی با دقت بالایی انجام شد و ده‌ها کشته و زخمی به‌جا گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/141233" target="_blank">📅 23:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
جروزالم‌پست گزارش داده سه هفته پس از آغاز طرح آزمایشی خلع سلاح حزب‌الله، ارتش لبنان وارد برخی مناطق شده و چند انبار سلاح و مهمات را کشف کرده است.
🔴
با این حال، یک مقام مسئول گفته اقدامات انجام‌شده «هنوز کافی نیست»؛ ارزیابی‌ای که نشان می‌دهد اجرای این طرح با موانع جدی و سرعتی کمتر از انتظار روبه‌روست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/141232" target="_blank">📅 23:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الجزیره: ایران و آمریکا در حال تعیین «هزینه ورود احتمالی به مذاکرات» هستند/ این رسانه می‌گوید: هیچ‌یک از طرفین خواهان جنگ تمام‌عیار نیستند، اما دستیابی به صلح دشوارتر از پیروزی در جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/141231" target="_blank">📅 23:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frar6TydaKE_zFVvi311Z4-7QusTQVDpW3Nbu0PpzaeKrmyscXoMAPR_8LaEGEbc1kdURRO3S2rWFRefZJ14EFgeCWkuLWrlBTy7fu92HDP16k-6dKrSYHEJe5i7fC6oTPIz6ABfnunZ6CNTpAuHGdrD2Fgj5Uy6RzHu5BXYCmL3OtjOfzNCUmLWNPBhgruZEF1WcYIxnt43qgP1aNmiac26PWF9EwPDRsZ-B4ZhnpxhHO6SAsdpQ4zx7XmQUIq-4TnkOcXmkkcLJroXLGe_JS8DhS6U-dk6WVPKE7muzee-SWCa52ibyTTexV4rSt1ekNEQmvqqEvENfdp2kHEYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعدادی پهپاد رو به سمت روسیه فرستاده، طبق ادعای منابع روسی، تخمین زده میشه حدود ۴۰۰ پهپاد بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/141230" target="_blank">📅 23:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر کشور پاکستان در جریان سفر به تهران پس از دیدار با همتای ایرانی خود اعلام کرد: پیام نخست‌وزیر و فرمانده ارتش پاکستان به رئیس جمهور ایران منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/141228" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfI804gtsWoLF-0k5Vgg8t3e1R4RDWLcv2FlKWYavANilfy1yibVSJvNngnrSj4sZfHRZctOsj4wygcqWcUisE3O7hRJjgHt1awtcA-OMEYgF-98C5Dtgyd-nBteJCwdmwPBPYZgG2L7NZ3LIovhAXesNyInqXGm3rU9EDL85ond6syXw7YKHMO2695wEwD2-QlNIMr9MXXp6PnAuv-SDm9HpwW2THNzzeklFoGTmyo1guCprqjgeEZzVWt_7noYBvtrQBSnieD40nyf0SJHb0cyNexW7t0PVlkfETVS1nAiPREGo7KdVWkCvuMmV9uGCEhBzbttKD6xIAvE2sQjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت رهبر عالی‌رتبه مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/141227" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141226">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=fkMzkvE-USg9eQ4J6aOd0W27RLZaJrXTWVtIycDKO2_AhXJxrxC_e27i99O7yYcAtYK6dsPCw17BjTWwOGMLizvb-vZUZX7r-SmS_ur4Zrd925Px1lviekCACQY5tDnbQslThEvnvXaegVBgbJzm6M0il9C0DHcWp3DgmnZrrihBU21MSDihDDnCYpS3vDBOa1gDyktm2JQjxvsx4Tq7R7F331IuDkAHmNQo_-EXZCXICzn0PBrFqorgjnVQXYZYoMaTZ27rLza9dC1qVlnUx2OpdBLc4zY_2_8_p_7AlnSSR5gSEsXWCoAeshcAl8S4wYwp4Ntj9JhTnfbnSJmgAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=fkMzkvE-USg9eQ4J6aOd0W27RLZaJrXTWVtIycDKO2_AhXJxrxC_e27i99O7yYcAtYK6dsPCw17BjTWwOGMLizvb-vZUZX7r-SmS_ur4Zrd925Px1lviekCACQY5tDnbQslThEvnvXaegVBgbJzm6M0il9C0DHcWp3DgmnZrrihBU21MSDihDDnCYpS3vDBOa1gDyktm2JQjxvsx4Tq7R7F331IuDkAHmNQo_-EXZCXICzn0PBrFqorgjnVQXYZYoMaTZ27rLza9dC1qVlnUx2OpdBLc4zY_2_8_p_7AlnSSR5gSEsXWCoAeshcAl8S4wYwp4Ntj9JhTnfbnSJmgAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار نقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/141226" target="_blank">📅 23:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141225">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE-RzpMPTt_81eacMaOfXJEpUX_Y8MG4eXorCH2v-im6DkMCdtEfCMp7azi06EU2UBt1t6MdbXR2bVfkqMjAEYEfISpgz6pJOcUPBxqpdVNR9KweJP3yGbZqAF9Ysg22gqMLsNySHHrK1HlbGW-WIWtwEhh6ItSiFxBwPmfSf6wumR4ZMJ0Hu61yy0kfB764Xia0LFqIKoanM3u3W7oTGXEfHTAHuFniYa2UCe8yyroazKpgIUBXZg431UWFGML9UKgL-sqdzNkSEhcj6tvux-_5EVbMfDV3rt_a2lJQDp2x_9Kd0iALxAmMOt0klJmnQzWGRUKNker3MQzGY-bDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط فیلم مسیح علینژاد و دوس پسر سیاه پوستش منتشر شده که.........
💢
مشاهده ویدیو</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/141225" target="_blank">📅 23:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141224">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایشالا بعدی آقا مجتبی</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/141224" target="_blank">📅 23:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141223">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOSnIi3zyvD2VaRxHOmzhuCJIYlyS8e1fvHnJ2-r0OuZW-pZ_RC20v57R6XsaBrBc3v4CiQeVS29JiFpLrbAT6DZNQ1MPtOxo6sazpwwI9g8mJcSSc4h11qwj_AuRBO5-UfJr_DcFCOaL9Bcq6sUDqD0Je6BVURE-NiwWqIYoXTeyyAn5RwZEsm4zgrvG_Dy1NyHlUTYzPyBhOSTBxSkSTqsTpfApLUpNC2gaJ7myM66w54AQfdPbvh06X3f8oodInzWzG05syjV0geGwKZDDShtJIETPpgeJT9N7QGeIOVxuH0a-V7Dr_E7Rso91POof5Q21mNIJOyckb6WflM5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
کریس رونالدو با انتشار یک پست اینستاگرامی مشترک، خبر از ازدواج رسمی خود با جورجینا رودریگز داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/141223" target="_blank">📅 23:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141222">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac7e6c261.mp4?token=Z5PaYM3eloKxshfAZZZ34TgUDnDv82CP5ALf0gc0rmmzRhhBN_VmIGtbrVBBdapFARd5UttOBm5n-BpI-ArX2erWMIZ8IPouW-bi3SevrEhh-7KSE76pCsYpKymuQV-8qMuiJKOVsVF8tgvPjcYaaPnamhIFUWao0cjiabStE57bFap8sKIZv8HPBlwojl2ARAtJnvMeoggxPFwLyn_USCu4EgncUTCDSNX0KDQyU1aWkXoJmxSyBCWHQiYiwMI7_K6toivKngQ_95UGH7PFsP3PoMLmIQcn2UVkETdb9VDC6EKouFOa3e5VPuCmxdhTq7t_iz58uUofz7zZIF3vsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac7e6c261.mp4?token=Z5PaYM3eloKxshfAZZZ34TgUDnDv82CP5ALf0gc0rmmzRhhBN_VmIGtbrVBBdapFARd5UttOBm5n-BpI-ArX2erWMIZ8IPouW-bi3SevrEhh-7KSE76pCsYpKymuQV-8qMuiJKOVsVF8tgvPjcYaaPnamhIFUWao0cjiabStE57bFap8sKIZv8HPBlwojl2ARAtJnvMeoggxPFwLyn_USCu4EgncUTCDSNX0KDQyU1aWkXoJmxSyBCWHQiYiwMI7_K6toivKngQ_95UGH7PFsP3PoMLmIQcn2UVkETdb9VDC6EKouFOa3e5VPuCmxdhTq7t_iz58uUofz7zZIF3vsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۵تا زن یه مرد همزمان تولدش رو تبریک گفتن
#حرمسرا
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/141222" target="_blank">📅 23:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141221">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فاکس‌نیوز: پنتاگون خرید رهگیرهای پاتریوت و THAAD را ۱۰ برابر افزایش خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/141221" target="_blank">📅 22:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141220">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le4CB0meUCOo8kkzZwO2_x00vNBeRASzic7IVRKGEVq0BUWeFBv11hzapprDJohy0nM1X-5CU3ZBHg7m5q7Hj_dvyHhYPqndgwWVrQyxqqGF4UvMJShxSj73-o_5c5PuEWvjgZQzlpAZMiUmmSmpmmIl-cUXSqwWEhVZIEhCTjCpD77ZlsqXcz3t8CCziRUkEWWZnNo70UoU3uH4rYfPoNcG3blZXfP_HjTRP9G6Rz5dzNFYb0WvN0aXOEizMC3YcS04xntbzPYxv82DerjbImbYeSOyFxN8fdsU2YiprwNsbF82-zYQbgMDsQauIyHfwZubj7sIZm9ugertI2Rj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام مدعی شد امروز سامانه هدایت کشتی تجاری (M/V Vela Nova) با پرچم پاناما را با شلیک موشک از کار انداخته است
🔴
این کشتی قصد داشت محاصره دریایی علیه ایران را بشکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/141220" target="_blank">📅 22:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141219">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
باراک راوید/آکسیوس: امید به توافق میان ایران و آمریکا در حال محو شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/141219" target="_blank">📅 22:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7qgiEHQhwGMI-dBCL2LrodnzaxwQ3EXlpVcORf_kEcsi6IE8jh_0yL3OCqWq9qU5eo9qmYigbdX8-Hh7GbsclpqqV3agjzUVuX3--cfiXX4RPpxSDkE4YDYczN0BTYpL4sjB2h-j1xVczqbhWG6tOqp-MMm1wCsC_T58SBYLpKin6Xu672yEkFT-tqYxOA-Ri5Y7QRUs-_EcpbV-kqhK-y1s3P7Qrz2G3Ro81GwxSUUn8ZGrmVtALBXHqle6UBFB7COykDc7lw_IcWfcx_DCPC-CMBXONVvAP7FlzBElazB9n00EtYF2rRFkBtUDalZXgPF1iDeCpspDNP2-49cHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای عجیب رحیم‌پور ازغدی: موشک‌هایی داریم که می‌توانند کره زمین را دور بزنند و هر نقطه ای از جهان را که بخواهیم بزنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/141218" target="_blank">📅 22:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سنتکام: از زمان تشدید محاصره بنادر ایران، ۵۵ کشتی تجاری تغییر مسیر داده شده، ۳ فروند از کار افتاده و ۲ فروند بازرسی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/141217" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اروپا با کمبود موشک‌های رهگیر پاتریوت مواجه است، زیرا اوکراین پیش از حمله زمستانی مورد انتظار روسیه، به دنبال صدها موشک است.
🔴
ذخایر ایالات متحده به دلیل جنگ ایران محدود شده است، در حالی که تولید جدید به موقع نخواهد رسید و کشورهایی مانند آلمان، لهستان، اسپانیا و یونان تمایلی به کاهش توان دفاعی خود ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/141216" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
عملیات تجارت دریایی بریتانیا:
ارتش آمریکا در ۴۸ ساعت گذشته ۴۲ ترانزیت از تنگه هرمز را تسهیل کرده است
🔴
فعالیت‌های سپاه پاسداران در تنگه هرمز طی ۴۸ ساعت گذشته ادامه داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/141215" target="_blank">📅 22:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">فرهنگ لغت جدید
دزد = تراستی
رابطه نامشروع = امر به معروف
موشک / بمب سنگرشکن = پرتابه
کمبود = ناترازی
تبعیض و پارتی‌بازی = برخورد مؤمنانه
اعتراض = اغتشاش
انتقاد = تبلیغ علیه نظام
روشنفکر = غربگرا
رفراندوم = تجمع خودی‌ها
طرفدار صلح = باسن‌لیس ترامپ
شلیک به هواپیمای مسافربری = خطای انسانی
قتل‌های زنجیره‌ای = نیروهای خودسر
اصلاح قیمت = گران‌کردن خارج از برنامه
مجازات نکردن خودی‌ها = برخورد مؤمنانه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141214" target="_blank">📅 22:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭕️
⭕️
بخاطر افزایش قیمت دلار تا 200 هزار تومان  هدیه ما به شما عزیزان به مدت 15 دقیقه کانال vip  دلار و ارز را رایگان کردیم. بعد از 15 دقیقه اگه عضو نشدید باید با پرداخت 10 میلیون تومان اشتراک بگیرید.
👇
👇
👇
https://t.me/+t2df2MwRSAIyMWM8
https://t.me/+t2df2MwRSAIyMWM8
شانس کسایی ک انلاینن
☝️</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/141213" target="_blank">📅 22:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل در خبری اعلام کرد که مشاور حقوقی کابینه اسرائیل قصد دارد علیه مشاوران نزدیک بنیامین نتانیاهو در پرونده جنجالی «قطر گیت» اعلام جرم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/141212" target="_blank">📅 22:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WTaTvO_Aw3XRoKPCKS5KeMMCXGTkMqJp8eZ3wnu9ZLfcrSzkxnl2w8b4MygzjAoBw3mTS3FgX2JkyHmZ2JUDYouPg9YnTcQ1KdwDqg4FhkLrqn_bbn4K9QwMu14JFipiH7RKBgliAc4UdV_PmY2BRqg5vTl68XsYiKfifoIafQuTP1Tx4Xy9jqcB1_VyZ5Iz5EiQ01jY7YPsSNwrIiMlcDoUs2yo8NyGaRJFRtVcALZw0kM7ypmhMs_Bjr6pd78a5ViWX3sceqRsLogJTJihDdt5qA8wv3RheX8rwZhMjAiSDnfCdkKDMe4xnLAgYOxUBPdNKShBZ5kYnb0TA45ARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس انفجار در بنی حیان، جنوب لبنان تحت کنترل ارتش اسرائیل (IDF)، که احتمالاً ناشی از عملیات تخریبی ارتش اسرائیل است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/141211" target="_blank">📅 21:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
شبکه ۱۲ خبری اسرائیل: گزارش‌هایی مبنی بر وقوع انفجار در منطقه سیریک، در جنوب ایران، منتشر شده است؛ احتمالاً موشک‌هایی به سمت تنگه هرمز شلیک شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/141210" target="_blank">📅 21:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141209">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سخنگوی سپاه: درصورت وقوع مجدد تهدید علیه ایران، صدها هزار مایل خطوط انتقال انرژی، هزاران نیروگاه، همه سامانه‌های آمریکایی و غیر آمریکایی و حتی زیرساخت‌های جهانی متصل به اینترنت در معرض تهدید قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/141209" target="_blank">📅 21:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141208">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
صرافی نوبیتکس دقایقی هست کلا قطعه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/141208" target="_blank">📅 21:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141207">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhh4sBM-o7N50WX7x9k7hds8wOa1Gq22B7hug_otFZLEi4t0iKgtQJBXWuMUL0wHyYHCm7ODDMUKAIdkLcgf74elUhH83QKcFfqVvcOveMgWfPtq8YvrE_BtoeTUKv3PV45gNIh7q9X3i3UueTiGdCkTqFrH2R1gUE_33iIAmVNh2QJecuHdjneaPKv_gCKBf2BWb_uitDb39Nwqe5UCOaLj_EKIAaFtf84XGW0M-VvWicy4NENrD3oTngcx_VWumph5MuTS2u0Lu6xrEmvPqNagPioxo0s0kZ_z-Lmn-hT0HYYMg0ra2wCFaZllL-cHpYiKsjpvL1ernkAcqUz8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال بازگشت تردد دریایی در تنگه هرمز به حالت نرمال تا پایان سال میلادی از نگاه پلی مارکت دقیقا ۵۰ درصد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/141207" target="_blank">📅 21:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / یمن اعلام کرد یک کشتی حامل تجهیزات نظامی عربستان سعودی را در باب المندب هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/141206" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
باراک بتش خبرنگار i24news: گزارش‌هایی مبنی بر وقوع انفجارهایی در جنوب ایران منتشر شده است. به گفته منابعی که با سپاه پاسداران مرتبط هستند، این انفجارها ناشی از شلیک موشک‌ها به سمت تنگه هرمز بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/141205" target="_blank">📅 21:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هم اکنون حملات سنگین به جنوب لبنان در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/141204" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ef63b346.mp4?token=fwGj9Ul1Qos-JJHUZR_znVb4Npogz4tVAoWOZ8KwqHSgxdDaPNyF6BJLxhIH9FjooLoxWKg73ylUm1DmlOZWSk7bk-U4fn-Nz11obPsM9xAkn03H3buGIDWNR-LDtxXDwzxLPlBUy8wkb7z2l4sMugx_0Ytp03YdUjJYyoSx47yKqn0AJm4vHEPHf_dD7kHXRtO94uEem_jj9B0JW-YdhhScGceCOEreYPTp-rcjcWsafdVd13x0L2OZAh9w8LgTxRpUi98GYzYUwdqBHGK22tRK7KuGK7Uuwhm5hGb7CRLx25iFMEccJK__e4ewhPDCuHAmU8zBL4PXo-gekOryGmcmCXgmsKDp1aXxMx4XHJ7SxFOIrEeLO0q53t7vb9UwHKC50eufxI2vVetYkfKTQCQzwSg_9giofryt8kfRdKSYj-H8J0EdngK8IX_tmXBP-gQdds4hDUZACrMB9ECYgAXsJTSjqACCrK2tbQ-drCu1dkL8tgGapx6Kop0CK9V0S6Z8-ne4Y5M0RCgal8PNVXoea7FG0ZQLv9lgKBeFaQGizyycfGzoIkiVVKHG2xqMmrkkpRefSNRQP6rLLaP46hTggmSTbvJqSym6GSKhwvm6vHTtxLG7kBWS26p7fQ4encl6dII-_43QfC-YDi_BUCRDSAIN-lg1pMTBUT1b_QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ef63b346.mp4?token=fwGj9Ul1Qos-JJHUZR_znVb4Npogz4tVAoWOZ8KwqHSgxdDaPNyF6BJLxhIH9FjooLoxWKg73ylUm1DmlOZWSk7bk-U4fn-Nz11obPsM9xAkn03H3buGIDWNR-LDtxXDwzxLPlBUy8wkb7z2l4sMugx_0Ytp03YdUjJYyoSx47yKqn0AJm4vHEPHf_dD7kHXRtO94uEem_jj9B0JW-YdhhScGceCOEreYPTp-rcjcWsafdVd13x0L2OZAh9w8LgTxRpUi98GYzYUwdqBHGK22tRK7KuGK7Uuwhm5hGb7CRLx25iFMEccJK__e4ewhPDCuHAmU8zBL4PXo-gekOryGmcmCXgmsKDp1aXxMx4XHJ7SxFOIrEeLO0q53t7vb9UwHKC50eufxI2vVetYkfKTQCQzwSg_9giofryt8kfRdKSYj-H8J0EdngK8IX_tmXBP-gQdds4hDUZACrMB9ECYgAXsJTSjqACCrK2tbQ-drCu1dkL8tgGapx6Kop0CK9V0S6Z8-ne4Y5M0RCgal8PNVXoea7FG0ZQLv9lgKBeFaQGizyycfGzoIkiVVKHG2xqMmrkkpRefSNRQP6rLLaP46hTggmSTbvJqSym6GSKhwvm6vHTtxLG7kBWS26p7fQ4encl6dII-_43QfC-YDi_BUCRDSAIN-lg1pMTBUT1b_QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار محبی
:
سرعت افول آمریکا بسیار زیاد است
🔴
آمریکا در همه اهداف خود، از جابجایی نظام تا چپاول ثروت‌ها شکست خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/141203" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پرواز های فرودگاه هانوفر آلمان به علت مشاهده پهپاد های ناشناس بر فراز این فرودگاه به طور موقت لغو شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/141202" target="_blank">📅 21:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbPKNbwbm-FOo8z4EApTWI9aOl_OWNcN8ZtB6-ESZsOjxfwPylNq4isnayY8H07OQ_JkMqDvHjWX3HmvF4nIAX25GPIvmg7OH4phIqSWwB6-w9D_lip2Qq_XeqaYTqeL4Fo4MuInMRo9tJ65vOnuwLrkZ15zl8fpTrqGzghwCrr9xde3icdHxJuStV_sEkiik2X5tpbDvydwtunxj1dxKp9B3sSNpd_d3hpWdEsKkTZJWow7x2NMyw5GbDHmV7bu5aDVAbAQ4s2uuLBsEnXpr7MchBY15iW4tbjK6utFqP1avbtLc3nMW4MzIS1qPVXJKjq-wlpAn5IW5t3F0xnLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار الجزیره: یک موشک ضد کشتی از شهر سیریک ایران شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/141201" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de77474c70.mp4?token=LBhYYmE17lEfp5vGkc5czudU6kUO_wubS4g8uVCXBpkrOreHyGp0NLwBg495GvwhhKv1MMxYrMYVBVBlfen1vlPi94ucoWxhvDhytwauKPNsC3zKATMuhFlOXLrEOwV_cjJB9CxiowaDLQ2S_FB8mI1DcjTdqKpKKmEID15g7ow3b5JQKWDiZ481cKXsJFK_HL95hZovNncHslE4bZLkEa6J7dlpJ7DAlz8aGthzFnVcp9O1UwaaFwCiNAA2puIwlg8mL0jTKhLpXJZT1BDtZB0uBz4A73SyvQ69IPUL-ZXl9hJqoCU-2S8PwyzokqxAOSsf1Z6XgMXA5qUhCxfkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de77474c70.mp4?token=LBhYYmE17lEfp5vGkc5czudU6kUO_wubS4g8uVCXBpkrOreHyGp0NLwBg495GvwhhKv1MMxYrMYVBVBlfen1vlPi94ucoWxhvDhytwauKPNsC3zKATMuhFlOXLrEOwV_cjJB9CxiowaDLQ2S_FB8mI1DcjTdqKpKKmEID15g7ow3b5JQKWDiZ481cKXsJFK_HL95hZovNncHslE4bZLkEa6J7dlpJ7DAlz8aGthzFnVcp9O1UwaaFwCiNAA2puIwlg8mL0jTKhLpXJZT1BDtZB0uBz4A73SyvQ69IPUL-ZXl9hJqoCU-2S8PwyzokqxAOSsf1Z6XgMXA5qUhCxfkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده در درپالایشگاه نفت الزاویه در پی حمله پهپادی ناشناس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/141200" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
هم اکنون/ دیدار وزیر کشور پاکستان با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/141199" target="_blank">📅 21:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea51341f01.mp4?token=lESTfJaiNhGidGouaO9AI64Q0gi2COuXN1pA7XvOTXTMukO5lzqGTgBCyCemchuMTfPIo8_jeodCnb-5AL8HE_17BF3BX4R3NjZzm5UOB6CM5rFAFVdaX6t3ttmNh8uzm--v-6p7jzo5PcK04yVnpACIW61Hm56KZSyC_43YOHllyrugdLCBGFZOD--FRria6WYI19lZJrMYNQ-2SmmLyG7lfTyR8aISJz6UHMzT492V5sNbTiVHqc1U0fiMigJtyJIdoGWOF5aJKUJzfZecNntCGdSFA9FPk6ZKc7PL_vyQTcXsocmZr_P_fYfC2dtbEHb-jMaic36V1CKPBz64Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea51341f01.mp4?token=lESTfJaiNhGidGouaO9AI64Q0gi2COuXN1pA7XvOTXTMukO5lzqGTgBCyCemchuMTfPIo8_jeodCnb-5AL8HE_17BF3BX4R3NjZzm5UOB6CM5rFAFVdaX6t3ttmNh8uzm--v-6p7jzo5PcK04yVnpACIW61Hm56KZSyC_43YOHllyrugdLCBGFZOD--FRria6WYI19lZJrMYNQ-2SmmLyG7lfTyR8aISJz6UHMzT492V5sNbTiVHqc1U0fiMigJtyJIdoGWOF5aJKUJzfZecNntCGdSFA9FPk6ZKc7PL_vyQTcXsocmZr_P_fYfC2dtbEHb-jMaic36V1CKPBz64Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه خلع سلاح گروگانیگر خیابان ولیعصر توسط پلیس نوپو
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/141198" target="_blank">📅 20:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcDRBnq9T1qs_L-dUu6BJktGI1C4GkGNabld-dQVBX7IOBHB17toBF482WT6MioIh4vOeWHYUbS2Rtux4ndGNsLZp7e0WZmbuio8gr2n35PqnpvJiza0oK4tARi90dNYFP7dY1SNbu0tqhcfvAomJgSDduKuS9ivxyBTZ5ZwIw-JvefE05vwmGwVePskwTRlJrub-opadO2a9oQEfVsW4iTnmW8eyAZxFgKb2kz4QtpQDWAd9rLrOK6I7lKFqcfHDNy07sUbJ_IUu4ExML4nEqwbBYN1-lMd04T2C__-I3YEbdN_b6javL37VUDX3TJZITEmb1jfGjuIBHX7cKCDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میا خلیفه بازیگر محبوب هالیوود: تا آخر پشتیبان فلسطین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/141197" target="_blank">📅 20:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd248</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141196" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / وقوع دو انفجار پیاپی در مأرب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/141195" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
محسن رضایی: تا وقتی تو غزه و لبنان آتش بس نشه ، تنگه تنگ میمونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/141194" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کوهن، رئیس سابق موساد : مأمورهای موساد برای اینکه بهتر بفهمن تأسیسات هسته‌ای فردو چطوریه
🔴
چندین بار از این سایت بازدید یا اونو بررسی کرده بودند
🔴
اینکه آمریکا فردو رو بمباران کرد، تحقق همه آرزوهای من بود
🔴
اورانیوم ۶۰ درصد غنی‌شده ایران هم هنوز با ساخت بمب هسته‌ای فاصله داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/141193" target="_blank">📅 20:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/141192" target="_blank">📅 20:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: ما بر پول ایران کنترل داریم و کنترل کاملی بر آن اعمال می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/141191" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
میدل ایست آی: ترکیه معتقد است که گزارش اطلاعاتی اسرائیل در مورد طرح ترور ترامپ توسط ایران، یک عملیات فریب برای نابودی مذاکرات بوده
🔴
تل‌آویو گفته بود تهران با دوش پرتاب می‌خواسته هواپیمای ترامپ را در ترکیه هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141190" target="_blank">📅 20:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رسایی: چونکه نمیدانیم اسرائیل کِی حمله میکند مجبوریم جلسات مجلس را مجازی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141189" target="_blank">📅 20:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=KsokNiW7PkwH80DywSbRSds2ezWodMjKJbeLBW045UiBKf1Zr_EF7BWBVWw5DyDyeL4Xfk1cCtRH19GGwgSBS2Lt5NrflN--xS4Z171NdraGoA62DsxgodvIswSDUCX1eQYLg-BWc8aJ6L8reNcj7r8Kb0JKcmYJ7ZZjxu7mKeZn8E-zcZhDBBNMWk9neTxUIQ9J_iDQqozmZOcz8kl0Bn7pksUUCekj7jcNynbv3bIZJ710PaBl76BTMXn4sodMrHFgb_xhAxbXsfQJuHUTeNjpBDiQcxqOHXZu0hXBHjZWQ1ufra55EE5ctjN7PUVfRsCfU5VfFUZG8cBFIXX803amiwjkcNtivUo1ysGMACqi0DKt-xqudHopmTV_i1mDJ3Uuo3jWO4K1MERI0tC2lDq4ueHvFd6AjOjL12kAzlIB6N0UkNgSPV8rlsfmuvZBeeKVXNHMXJHiYwMlV_dh8ONrLY3u_1WVpotYLokCrIT-Klhype0fFXrJhstdnmFr7tiUX-A0mU2GSxaIcPw1x-r5GRwbXERpEboqvZXQWeEgMftutR3Mip2pv67GQLFazerD_XMXDLWVcnNQgGuRuF7TXaTq_aIdlPNPxRE0MTCcmhXmlK4jqbp-EhWHvg57B1OjfJKpgRjwx7cDyOWvFNldn8mp7rGZT0clO5x1_mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f811c57f.mp4?token=KsokNiW7PkwH80DywSbRSds2ezWodMjKJbeLBW045UiBKf1Zr_EF7BWBVWw5DyDyeL4Xfk1cCtRH19GGwgSBS2Lt5NrflN--xS4Z171NdraGoA62DsxgodvIswSDUCX1eQYLg-BWc8aJ6L8reNcj7r8Kb0JKcmYJ7ZZjxu7mKeZn8E-zcZhDBBNMWk9neTxUIQ9J_iDQqozmZOcz8kl0Bn7pksUUCekj7jcNynbv3bIZJ710PaBl76BTMXn4sodMrHFgb_xhAxbXsfQJuHUTeNjpBDiQcxqOHXZu0hXBHjZWQ1ufra55EE5ctjN7PUVfRsCfU5VfFUZG8cBFIXX803amiwjkcNtivUo1ysGMACqi0DKt-xqudHopmTV_i1mDJ3Uuo3jWO4K1MERI0tC2lDq4ueHvFd6AjOjL12kAzlIB6N0UkNgSPV8rlsfmuvZBeeKVXNHMXJHiYwMlV_dh8ONrLY3u_1WVpotYLokCrIT-Klhype0fFXrJhstdnmFr7tiUX-A0mU2GSxaIcPw1x-r5GRwbXERpEboqvZXQWeEgMftutR3Mip2pv67GQLFazerD_XMXDLWVcnNQgGuRuF7TXaTq_aIdlPNPxRE0MTCcmhXmlK4jqbp-EhWHvg57B1OjfJKpgRjwx7cDyOWvFNldn8mp7rGZT0clO5x1_mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/141188" target="_blank">📅 20:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141187">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: روز یکشنبه ۲۰ میلیون بشکه نفت از خلیج فارس خارج شد که بالاتر از میانگین قبل از شروع درگیری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141187" target="_blank">📅 20:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141186">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0160411b7b.mp4?token=Z7YVfsARKz8OxDZa7RBxBU7fgpYDhJ9ld-c4xD8xN2wFl-qbJtEPLmbYRyDikt8JxtNL6gQ9_sVHFwBDnC2Z9mMZdp5kdlfp8QEEOqN5_frhxLj2VbObg_2Z-vCRsT-alT1mb1YC81d_5IEGPOlAY7FrldpzFAqy4-bU1lMJ-zcy01_mkVkkp_WGPbLIGjnnFhU9_PF3vM6iwyMdBS7-aFlN0xUZSp62ksY_WjNAlHqR0OIdsxglUxZRv0STAJFLdLOTySNMNVXwOkA8MXjMJX-ibUqQ3NvoXSuVtcBRglIzwB4gsWdoFGB_xXqTQ1uJEFICqStpRsCa2phr8RsL5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0160411b7b.mp4?token=Z7YVfsARKz8OxDZa7RBxBU7fgpYDhJ9ld-c4xD8xN2wFl-qbJtEPLmbYRyDikt8JxtNL6gQ9_sVHFwBDnC2Z9mMZdp5kdlfp8QEEOqN5_frhxLj2VbObg_2Z-vCRsT-alT1mb1YC81d_5IEGPOlAY7FrldpzFAqy4-bU1lMJ-zcy01_mkVkkp_WGPbLIGjnnFhU9_PF3vM6iwyMdBS7-aFlN0xUZSp62ksY_WjNAlHqR0OIdsxglUxZRv0STAJFLdLOTySNMNVXwOkA8MXjMJX-ibUqQ3NvoXSuVtcBRglIzwB4gsWdoFGB_xXqTQ1uJEFICqStpRsCa2phr8RsL5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد اعتراض مردم فوجیساوا ژاپن به ساخت مسجد تو این شهر،دولت ژاپن اعلام کرد اسلام تو ژاپن جایی نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/141186" target="_blank">📅 19:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141185">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سی‌ان‌ان: کاهش ذخایر موشک‌های رهگیر آمریکا، نگرانی تازه کشورهای عربی خلیج فارس شده است؛ آنها نگران‌اند در صورت تشدید جنگ با ایران، توان پدافندی آمریکا برای مقابله با حملات احتمالی کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/141185" target="_blank">📅 19:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141184">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اسرائیل و ونزوئلا روابط کنسولی خود را از سر گرفتند
🔴
اسرائیل و ونزوئلا در سال ۲۰۰۹ میلادی روابط دیپلماتیک خود را قطع کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141184" target="_blank">📅 19:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141183">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزارت دفاع اوکراین تأیید کرد بیش از یک میلیارد دلار مطالبات معوق مربوط به تسلیحات و تجهیزاتی دارد که برخلاف برنامه، در موعد مقرر به خطوط مقدم تحویل داده نشده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141183" target="_blank">📅 19:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141182">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سفارت ایران در ترکیه: هیچ نگرانی بابت توافق مکه که علیه ایران باشد، نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/141182" target="_blank">📅 19:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141181">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFkcay9moYV6mcnWq9-6l--7l8LYJpaT2l4ffsyttkDDyJepEG_obl6Uli8c2s6D-dLuhnwlH8KiEYMRKQeyNwHDEh_NkZGqCMV4QSh8BzY9ih24H4OJZzVHPXa8Zajnej4pidEWE8dA3AD00C2tdkrOn-xnPAp2tPQg8NwescqJy6qUlBGS2dGuvxaH5niWvSS29Q9UwyLYEP-lLNRzNuBql24Ktgbm7IWYnltbpACGSiASlb8MIxLBWabhpEGwizJaU6xX9A9lc2UoxNZlnyzDRZ5diH4u_myjmfimo-0B77WprF2FVuiHVf8AuXYz0VKOWg_yQDRsnys5uf-mkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین گزارش حملات موشکی خود را متوقف می کند زیرا حملات روسیه بر دفاع ها غلبه کرده است
🔴
اوکراین انتشار داده‌های موشک‌های وارده روسیه را متوقف کرده است زیرا پدافند هوایی این کشور تحت حملات تشدید شده در میان ذخایر رهگیر خالی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141181" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141180">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJPuHwO247nDfo4iDi-5l3Imjr-FqmGoVfvZDWka605x2Gloqf-8dUXool7luuiygfixaxOxkKjU9GmaCTS6mERVaaE7sFbz7naGxuny5t_RjSyYm2F4XJBFPaSCmjr0i8HkB3qDYvqQWFlBUL84LixGllS9Qz-3wPF2i92CFCpSXcz12Tw_CT9qT-zDZBW07FuKKIwkfBm3ViFMskx2rkyDUyfIcTjOxsspNHpESMXaOUa6UqfxiGJwfae-Vi7GMfg_rWx-cagBHKM_zqc5CGBW39ZdAA5J3HRg40KkZfd0nJhH69hX9s77kGETGTL6YkceYI2q2aMs4d8ZX1yroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخبر: تنگه هرمز باز نخواهد شد تا شرایط ایران محقق شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141180" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141179">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
محسن رضایی دبیر شورای امنیت ملی:
شرط بازگشایی تنگه هرمز، پایان جنگ و آزادسازی پول‌های ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141179" target="_blank">📅 19:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141178">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMsOrycCi2maaFMyU88r4WrXgqG2qlVA9mO-sXJ-2tMy2eE226djVnNvqtfifS4qeSuT9qXxEPT7mypV641cFGWe9joO1lJ6NjgE9US053LzG6zRd_VagSmvN1odFjTtCHDSNDdkJMwJVZSJeOrHIW2zoaSE3XtzLWl-3lqD9RVbC3UDw_F69o_YW8fI7iJNhigP5uSIfC3oIigLRStkKFqZIJz7wg3l6HtOhp0hBstlV3kj88J-pKtJ3hLnomEvdZ2Gw1LC_joxlrkokhBYWXDe7NlEy00l-WLostE5VqtS252ZNIKBVWKzEoAWOdg3jkJLplWH9ISoZqoFqCCrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری: شما از آینده هوش مصنوعی نمی ترسید؟
🔴
پوتین: من تا حالا تو زندگیم از چیزی نترسیدم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141178" target="_blank">📅 19:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141177">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e386169ba.mp4?token=jqBkDp7fB5WtLK1Iu3a0ZqIGwvfMxjrZRUT6rdr2s7HnkU7spBg26lN26N_7w60YpSnqkF9Eo5gp-e1apW4WN7vuUUCzQX-QgU0Pjtqgzt8QlqvWkcBTQfzZiVFrmbM4TzMMTcRXkRMvtrC3THbaY_12xcbrU882vLax5KM87aWsRScmIX-bcjRUzUJtwPLY8LtqhJ1Ecjf_PPiVQpamOUuO15rgYUHR4T1mL-JZI-ktrsYJwFtJ07_eolgHb3x2FXMh-huHu0JMpl42wsZ3SxBKGJhxJXioexbO32lwAYwMZs26HbVb2TVt2mAdGBy-xeUegeHKtmDaHKQHuA6I8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e386169ba.mp4?token=jqBkDp7fB5WtLK1Iu3a0ZqIGwvfMxjrZRUT6rdr2s7HnkU7spBg26lN26N_7w60YpSnqkF9Eo5gp-e1apW4WN7vuUUCzQX-QgU0Pjtqgzt8QlqvWkcBTQfzZiVFrmbM4TzMMTcRXkRMvtrC3THbaY_12xcbrU882vLax5KM87aWsRScmIX-bcjRUzUJtwPLY8LtqhJ1Ecjf_PPiVQpamOUuO15rgYUHR4T1mL-JZI-ktrsYJwFtJ07_eolgHb3x2FXMh-huHu0JMpl42wsZ3SxBKGJhxJXioexbO32lwAYwMZs26HbVb2TVt2mAdGBy-xeUegeHKtmDaHKQHuA6I8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : این منطقه جولانه پرچم اسرائیل اینجا به اهتزاز دراومده و همین‌جا هم باقی می‌مونه، چون این سرزمین ماست
🔴
امروز این سرزمین متعلق به ماست، دوباره به ما برگشته و همیشه متعلق به ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141177" target="_blank">📅 19:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141176">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a895c6e9a3.mp4?token=My_t2EhFN5QDWkVBYYa5lK006Y6vUTK3iYQlzeD72eAcjVRftc70LDtAT2rhen_p3TvNy3MRHD9Us_HMXNVPvnJfAPWF1_ChTYwHJq8apXyHBLQBDqQRzuqLRklANDDdy3Lqjxs_eTr9A3KHPsOuT1PmU1bYoKOS7QVIBcXFq98vCR_LELP2slcnpWsO6LtdI4PTs-3FPtZ6gqHxJFMUKUuOrXuJGXN7uvoo4oRTwdJKgqBFQ8vuJ91K9Cqd7Te9MUdtivBfL8UTdvBIvp8BqRVQmnMYXr3hQ5yjfldf6ioCC8Nge1I85KWNFMTkS2-cugMlwcQhIAYCEiPeVJT17A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a895c6e9a3.mp4?token=My_t2EhFN5QDWkVBYYa5lK006Y6vUTK3iYQlzeD72eAcjVRftc70LDtAT2rhen_p3TvNy3MRHD9Us_HMXNVPvnJfAPWF1_ChTYwHJq8apXyHBLQBDqQRzuqLRklANDDdy3Lqjxs_eTr9A3KHPsOuT1PmU1bYoKOS7QVIBcXFq98vCR_LELP2slcnpWsO6LtdI4PTs-3FPtZ6gqHxJFMUKUuOrXuJGXN7uvoo4oRTwdJKgqBFQ8vuJ91K9Cqd7Te9MUdtivBfL8UTdvBIvp8BqRVQmnMYXr3hQ5yjfldf6ioCC8Nge1I85KWNFMTkS2-cugMlwcQhIAYCEiPeVJT17A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت مردم پاکستان بعد از توافق مکه با عربستان و ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/141176" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141175">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سوریه اعلام کرد آژانس بین‌المللی انرژی اتمی به‌زودی از دستیابی به «پیشرفت قابل توجه» در پرونده هسته‌ای این کشور خبر خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/141175" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141174">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شورشیان نیروهای سریع‌العملیات (RSF) که از امارات متحده عربی حمایت می‌شوند، در کنار جناح «مجلس ملی سودان» (SPLM-N) به رهبری عبدالعزیز الحلو، شهر مرزی قیسان در منطقه نیل آبی سودان، نزدیک مرز اتیوپی را تصرف کردند.
🔴
نیروهای RSF و SPLM از خاک اتیوپی به عنوان پایگاهی برای عملیات استفاده کردند که به آن‌ها اجازه داد به صورت غافلگیرانه از مرز عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/141174" target="_blank">📅 18:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تسنیم: درگیری خونین در ناو «آبراهام لینکلن» ۷ کشته برجا گذاشت؛ این درگیری پس از اعتراض خدمه به شرایط نامناسب خدمت، کمبود غذا و مشکلات بهداشتی ناو رخ داده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/141173" target="_blank">📅 18:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری/ترامپ: ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/141172" target="_blank">📅 18:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141171">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxKp2i5Pm0vLAAdNfr-7jTK7Uq7Ucbx1Ve1fnfqLWL9dR86j3ca_lfqumg8rzLhRx-tOTGZ7lFc2Xt1bupiOQPUSs584_9tczYcQiigahSaGZovsLiiMbmsI_hIZaahNz30wlrDbzqBK21A2lr7UuYPXEqIMq5DnKMwPDR5h7PIi3jfVMw9YsWZEfvZs46F-QhkbeyAjv2Z0emxqhdMEzE56DaEKe-CQg_ajQnTf6_-j-kZHu1zHwP7xUys8vTuwQJ1PmJxMh6XK-v7EiXcqcj_6LgWGijl9z8bE7o4WO2OOyr-Q5U90hY26OBUNMs1vTRdkkdOwOjlEnXetiEeUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور لهستان: صبح بخیر ایران عزیز!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/141171" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141170">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/ترامپ:
ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141170" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141169">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزیر کشور پاکستان با عراقچی دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/141169" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd2p1qdiIDzeClWtrfHk-VekmUc2jmriJIJX-tBTKZAJgNjnICrSjyauXr61dp_Tna2HC_u0JlOgL65ooKK308Zk_BMvIazi511V5k7Kl5KmF4frvyum4mw-nO03qU38I-dPU_IHa9ee3CZ1oMa0MkZEHy18v5pk5h3MrKRsvJtc8bLmsFxgT3K-noJytVztwTnQhK96scSzhKF6uC6FNKJzdwA8jxzFXhXHo2FBI1uY8bx3zjgVd1NqPR8alwzi42kha7KLEcHtkXswPh8wC-o9BKNKY1cpwh1DgdhsmReXERwmmRVGUjX0KVc9_jlaDIqb4-QJO36M_WDgL9lMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
می‌دونی طلا و دلارتو کی بفروشی، کی بخری؟
می‌دونی چطور ۱ میلیون نفر پارسال ۲ برابر تورم سود کردن؟
📈
با اکوتراست
✅
همین الان ثبت‌نام کن، تست شخصیت مالی رایگان بده، تا دقیق بهت بگیم توی چه بازاری، چه زمانی باید ورود کنی که بیشترین سود رو بگیری
💰
⚠️
فقط ۵۰۰ نفر ظرفیت داریم!
👇
سریع کلیک کن و تست شخصی رو بده تا بهت بگم چی بخری و کی بخری
👇
https://storage.ecotrust.ir/marketing/landing/index.html?utm_source=ArshiaYar&utm_medium=Telegram&utm_campaign=sinaps-marketinglanding-0505&utm_content=Telegram
Alo</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/141168" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: می‌گویند «آقا بروید صحبت کنید»، اما طرف مقابل با شمشیر آخته آمده؛ نیامده که بگوید صلح کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/141167" target="_blank">📅 18:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141166">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ:
ما از رویکرد ایران در مذاکرات راضی نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/141166" target="_blank">📅 17:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141165">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دلار 187000
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/141165" target="_blank">📅 17:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYJHV2TGqntJ8oK2vQ3QckXm433yHMAsDELaTettKOvPKt-7BJjXNuEqaff8mpWp_wsUachhOUuEUjqsbsJ1H32QZERy6FzLEeqdOfa40o_QpNydDNXWvsS9Y5fdMot5r0nB6zHKTTlNZTUG6WqvxGtXjJs-co1PovE2mvBH4N0bGpPyLftvBIvIQMap3-VBOnoIyGu6z2pp30eDcTX255coq2-bOpNMN6mOyo6uuu4UVp7RKgyGahIbqdPopgha4mILE37KXohm9ll2rctem2mjn89OmFL4iwKFV-UucKoICcXWA13NypZX8q5_zEFgtCI09tn41297TiFigTPxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: وقتی بیت رو زدن، خودم رو با موتور رسوندم اونجا ببینم آقا چیشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/141164" target="_blank">📅 17:32 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
