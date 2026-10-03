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
<img src="https://cdn4.telesco.pe/file/A7T-A-rN4FjCOsiK2q5g2jjVdYUh8gKrbIg7EkhcwRuVn449tgbDPToGiYYXRCc8FQNOeztntzN4ye9nJkMU_Tc_gLcUtWf6HSFCkOQ67t9OZRBthTRNspFKmMh9SKteK5yyqYazfSNDZeMiZ8vFAzD-KI0vZe4nC-vtUL0zloDrT-5eEK5j9xaBq1RJ5__85zr685LxXAIEts9htrYiguPynkqot-Uk3380SU-1LHYQMKwjYOCMCR8zNjU_SIHH68a__9DGTPUxEHUNGKEgO6UJwuQn0kv3okfkFu6PSvPqCJ6kz13l5pFpYi-zXN4bcMzowcj9KQY10yl4i9jCKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 421K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-30900">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G05_PvMWLLLMttJMaried3IvgJ56AcFjrU5AMrmUPhfPBJ52RfpuUfo9v-XbMdqXv3w-X5GIRy47WCJYtx0h67N3vLgUPWW0TU0p6ON8qm4piiR9-MQWcrzxYWe77OrfIfcAcuwbki-5SiCnhtwApToU5xz0CE-7BYJ3Kgfl74zJkBioAUQCKCg6DmR5gv_3v30YjHdL6_kSVafMLR8iJmS3qrvrZWXKs8bU8Rdig3PdmBddoCuvU1U-uhCoLahamrIhfC2OWf7IJx0pyuSf8_f_-xGKmGKTJJJ8T5UBtED5dsfVL4_OS72T2NC5bOKd6_Y-7ND4S2Mi1LcHL2EJWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قیمت‌پلی‌استیشن‌پنج پرو تو دیجیکالا به 345 میلیون تومن ناقابل رسید. خرید یه کنسول بازی هم برای خیلی از جوانان ایرانی آرزو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/persiana_Soccer/30900" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30899">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNOEM_zpiwRhZL3oRz6RZrxyvudr7lrhjacB9DFCBmnTnMs91PfIuBSzvpN0x2tvrZEAP9IdkSouXH4ouqAfEiH3LuG5fPCrO2-tRLyqlR85TJ0_CVVuAF2FXFOQyGWSfZmweJg7M5BdOcIjiM2LMuWUExvVVyKPVq2jG5aBhnen6cNMpUV-Jl2YlORJd0UtT0M4rtz9px0Kjh5qwwW5lKSppj_3BRC5eTXkrWRnbtS6dicz34cDh6WM3CXHY9oePRyqK3WtVbsohnSHbowoRYwqehghEgyWu3XpfM9aC_qbbZ9auxlQjOPakLE8udN3TJZVBAHTKjc1pYIeeKhpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/30899" target="_blank">📅 12:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30897">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
حسین ابرقویی نژاد بازیکن جدید پرسپولیس: باعث‌افتخارم‌است که هم در لیست کارتال بودم و هم هاشمیان. تلاش میکنم بهترین عماکردم را نشان دهد.
🔴
از بچگی پرسپولیسی بودم. مثل آرین سلیمی که همه اهدافش را نوشته بود سال 98 تمام آرزوهایم را نوشتم که آخرینش پوشیدن پیراهن…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/30897" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30896">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plSgy1NKUpJWHTAS4TVgJq-km8KGTEh8dnWWrMBrVuwk4i98ZQYX2o49bYrUeXsZyKF8cjk6stwIRGEZN5hULe9uPVmpAfKP1IbUbz8xqXXjeOb4325UNOJO673BmvjytczwrGYKjG7G00TBDWLUN1uOo0dgwCa11Ub43NIq8Pcy_JQOZpGvZRm364qcp6P-dorsZy8sjgT13Z3Ho7any47cV_VoAAl_YqLIWaBsn0QdWCOggspVEX4GFTi5lZ_eOt62oFjKRqd-hneltG3VgmJJL_dZu1yqrTe73yx71yW1K8xftZh6eS2eaFK2D6ZSb9ZyXTq2hiP-WxVbAlrjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیرعامل باشگاه تراکتورتبریز عصرامروز با علی‌ کریمی برای‌پیوستن به این تیم جلسه خواهد داشت تا درصورت توافق نهایی هافبک سابق سپاهان و استقلال شاگرد نکونام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/30896" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30895">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=GV9j8yapR1iBpovWvV4bW1BxORAtTMEwH30EeX_q5izJpi1JmagElt-UVz1B9XglAbLArwL0pUkDdjNEq69O79udIXi1M9IKqLBcLVCGF1LieIpuf8SkxvbFM7DjNKdPqSD9Y5RKSwVmkqLVIBEYzes8e2f_npQ5m6siWiK04C73mxLQvZAjkDKL7hJuNwcwQsHbUoATwYLCtkbU6-U50cs5DV9HxFCdHg-dEfcpatV4G6MbkE3Otz3hrLgZRmGvRi-6dWo503PyTJEEfgCwV_MBRPrHMx0fOnuMWNW1-JS2CCI7AwDWTBpHe9Z7HdWb-2L-RF5gSqER78S3hCEkQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=GV9j8yapR1iBpovWvV4bW1BxORAtTMEwH30EeX_q5izJpi1JmagElt-UVz1B9XglAbLArwL0pUkDdjNEq69O79udIXi1M9IKqLBcLVCGF1LieIpuf8SkxvbFM7DjNKdPqSD9Y5RKSwVmkqLVIBEYzes8e2f_npQ5m6siWiK04C73mxLQvZAjkDKL7hJuNwcwQsHbUoATwYLCtkbU6-U50cs5DV9HxFCdHg-dEfcpatV4G6MbkE3Otz3hrLgZRmGvRi-6dWo503PyTJEEfgCwV_MBRPrHMx0fOnuMWNW1-JS2CCI7AwDWTBpHe9Z7HdWb-2L-RF5gSqER78S3hCEkQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ درواکنش به‌خروج کریستیانو رونالدو از اردوی تیم‌ملی‌پرتغال از رفتار او انتقاد کرد و گفت: نباید میراثی را که ساخته‌ای با غرورت خراب کنی. اینکه بدون صحبت با هم‌تیمی‌هایت اردوی تیم ملی پرتغال را ترک کنی، بی‌احترامی بزرگ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/30895" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30894">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj7ZR8urhqJIBqvIkvgjdlwUnbH1Z7GMxYlNgdizmLkpvudj4qq_zg4D77D0IKTgrwbdiruDTW-hCY400xyTzk5uz9U37cd0u_ZQLoJoDfjOfFyExNchVm02Gyy5qh-fK379AH9alQl5l3aeHejJIeTinF__x_Y0bNS9MrUdvPjZHJaRcjNpQrXEO43XRZskofz34850t3CzEkWSXZkCFxlIYOJqwJztrgDjxlyHFta7Iko4w_R7zvzXFfkTG8yZbLZDUg3SLZwxSac34VKgbjY9gIY1VYKGGpm5k5DtNjpya0jXL-lkt3e2Dt3U3XnZaWV-UFjGdvaA31om0CHoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/30894" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30893">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPdUePSa76PLoRYKAnZ2r6olvCfVKMjfSWzfb0S6ar4RQDSaik623urC-EKV3wFH1HXHsqladCYBCmDNhmqjqmYnF36LNnvEF62m8gJSADCdBPsOrIZCisbPP_C3kSs7Iwk608CsF7oBPPDfyVQ8iBrU34VVzawTYtSVag4_tSvGdgBwDHBZAIhi17hdZNcpIJq2wv5xLIZ0D6Y7TyAHgDcv8Vzr-c-DKJYFjAjdyUmTlRetvh1iGw8KHNgsnqk6otL2M7bbO9P1c2qDp3TCWWdMIEe9xQ01Fn-VNhF0gTrgQ-MhJfzym8CUpCLn5v7kqMeI3AeNKaDgP9RPfWnqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه
آاس:
رئال مادرید توگزارش شکایت‌اش از بارسا به یوفاگفته بایدتمام جام هاشون از سال 2001 تا 2018 ازشون گرفته بشه. بارسا تواین‌مدت 9 لالیگا برده که تو همشون‌رئال دوم‌شده و اگه این پرونده به نتیجه برسه 9 قهرمانی لیگ به رئال اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/30893" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30892">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzw8hIOT9Ep58yubgyZFlhlRIHxba5mLNpBFRf45j7LtLge5p0_ULetbn_BviJzX2QYQpPQhckTVidzksDR0oRgBRIkv8Wsnzgtt9km9so70jaITXIJ5AyVUtNKPrfszuLTDMET1PzalH4QyPWeCdSsWRoOJ2Cf2vabbyy-uqGaR0hiPopW6AwMktljdvQj8krU77rkcXLf00FzvCiz7z_EczV0wS_mP0VTSpdphEmTpjDm3InoZJ3Ff8G4iy7nVvE1Uh9Dsp3oCN5VtlfjyUfOo-v0bDbmyKvqKjWeqvRLmO44OfTfSGEu3Hiz0APcjXEgoJNCubJQwJOMoAiUfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو ضریب 2.0 دیشب که به راحتی برد شد
✔️
✈️
@best_form</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/persiana_Soccer/30892" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30891">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGIryV_sEVhNsCHf77YseEVz0gRk1k8mqFNKrhzyVeCgiuH2TWw-nzbYqGQhkFkMFCZXKSiIIrZ_mqigS8LZWJ7VQLq_Eks_lZzf80gyY5FKfFilQKlmg33Jfr56ONM9th9a-JJUWafDCa1YAmUi7IDr9O8Ory2FPsK7C8wNQjwTxx4vvWWBL1kRdwQZBnomw0P80pb26IzM2nHukexznlvW0Rpd0MfcY8Hf1Shng0I4EdejmjIswwDxSfp_fFZQT879d6wSZUFkAtLR6NpOJWPvja9Ii81r1lhNuEMPhwil3FLus37eu6kBpwM0LQtHxa387LYi4T6mJGYmkZsIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 بازیکن‌ایرانیکه سابقه بیشترین تعداد بازی در تیم ملی ایران رو در کارنامه خود دارند؛ احسان حاج صفی شب گذشته در صدر این رکورد قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/30891" target="_blank">📅 10:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30890">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcxsyBETL0mEoMjBQprUZULpumImowcAfaM8Oq7obMqWEV9cUrR7GWLmz9XAnvxWpiEivhcH7S3rheIcV-7_BH7pA5iTQBiMi7JQe9kftpW2w5ZmY2m4JDqRYjrgc3JjIFKX10M-7BVb_fx7JWGty3jgG__rqoh7NWO1xtqcsH9on47yuwqq91umUOuSsse1Fy_93QkkMbTqU-41xdsYa2YoxR8MHzTO5pib9RP6kxEJ2mgqvc0HwkTP4yiruu-8XGhlgX6iiuvyWe_uMhAuDaSOnE6flXRwGHNqd7UucdJgFOamrHine1XszdGJXF7zm_jrjP4kvVhse0jslhQEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ترکیب‌منتخب‌فوق‌ستاره‌هایی که تا به امروز با هییچ باشگاهی قرارداد امضا نکرده‌ اند و در مارکت‌بازیکن آزادند. محرز یه مدت با باشگاه الوصل در حال انجام مذاکره بود اما به توافق مالی نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/30890" target="_blank">📅 09:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30889">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMJBW_90Fv2tF1Vz89wRJYHsQ-YTAzNxjzqSkzrPHG9zNCMWaIrRnVmAXGQWhxWak1cE8jsJYF9YnDjGd-dbWjQLjPxvvXy2014_ARATupuuBnm8BMKOasMqyr4XUQ0hjB9sHZUKO-Rg4Ar1zsAWawgjc4RjLPkVZxhHCgOwXCmNd1wfNQPfnui2UmRnt2Am6-z8Z3wYHJP-w_fNQc0Z6VNxdy8n5We4BePa9FlGyjwzbHX2QHlGIDsdcGeauO7uOd43_rOQ6qrYtwnk-_cKoce2RkPPosge2_z2NjJvaOmBVccn72s6FlwqfwCp83vgLAylzymJzOgHA7z7HbEk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان که‌چندروزپیش در اردوی تیم ملی جوانان گفته‌بود که من اونقدر حرفه‌ای تمرین کردم که هیچوقت مصدوم نشدم تو بازی با روسیه مصدوم شد و ممکن است که چند هفته‌ای دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/30889" target="_blank">📅 09:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30888">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=tASSB7Nc5rya17UbL8E-5uADWYnspctEpACXWpAYVuD1piy7DuzW6M4CjmROTGEX8DcIIqWgv5pmDJVIY2EQ8a0PD8CoRYTLRf0wAGy-xpT1zYJILnjMl7zNgmLdew3Uzjrzib9vkMoGNwt49GJ4YoPRhlXClc17KCLRA9Mg3spJbU0pIU2SABgSnGD0TSbYgwS2nImyEOdJj2daQiB9vEGMKK1oFsMe-NbLnPDZryw50-MAqO48wfOWCtj0b1VD32L4Ke4UhtEG2-P6AmbRn9OnHo73O5_P090u5aD5Qt1JC4gV45qsPt0UMYSicG8LREPUv32MDpT6Np_FSnRUZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fabc89fd.mp4?token=tASSB7Nc5rya17UbL8E-5uADWYnspctEpACXWpAYVuD1piy7DuzW6M4CjmROTGEX8DcIIqWgv5pmDJVIY2EQ8a0PD8CoRYTLRf0wAGy-xpT1zYJILnjMl7zNgmLdew3Uzjrzib9vkMoGNwt49GJ4YoPRhlXClc17KCLRA9Mg3spJbU0pIU2SABgSnGD0TSbYgwS2nImyEOdJj2daQiB9vEGMKK1oFsMe-NbLnPDZryw50-MAqO48wfOWCtj0b1VD32L4Ke4UhtEG2-P6AmbRn9OnHo73O5_P090u5aD5Qt1JC4gV45qsPt0UMYSicG8LREPUv32MDpT6Np_FSnRUZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
صحبت‌های جالب عادل فردوسی پور درباره مدل ماشین اونای‌سیمون دروازه‌بان تیم‌ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/30888" target="_blank">📅 09:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30887">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM8XbBoweeDpE7DGstVIjoU2qrp6yNTKJbD86uKYVHbxqKA8Wvi64Khf6Sp4FOFTPG4VspWxSudHJkvUe75wfalDcG0M17S1mIvOqLFOQurvYV0PoeoxR2LdVRljemmzJZYr2CoenuwN8BWwS7wLfC3cdNGCntHGlnTcF_xJdfVWGHJt972rG9x-ViLXVdQ-oVzpgHx2bdCMQKofkGHzlJX6e7LwYIM3gUsC6ugdyv8TLL9gmTBj6Fe6ksxCNLlVjHhbkVGkKAPKwtkwhBVUy7Cuq1Azn4JmTKlWqCdLQ_kO3qUz6y0vnSpjIZOgkJFUETbvz9QYGrS3rLsDPtciyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/30887" target="_blank">📅 08:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30886">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpdzsFYS4gacJtCfBQ4K498KlhCJGzE3_NRJNE9cYcGOpclozrckXjBYiuyb4JbnwO8m7ZoeVJuC-T74XKQoBZdXzw2_Yk4psMMEVPpANUjDtX21WksJ1jdxgjjX_mQYKszJkLZGoWJZM186GPboEV0h5e_GIiOjFepTwzrvA1tL1lyDLfWJNPXPoiE_UZyL06SSZ306EDOJ1UtMTpfTuNA-l8geSYTADJKKuPsrV_eTS3J1w-mNuD4kaHvmXVJIkhD_xvPJbOrQSM07MjLw4Je1xcPg9XrxmfUEZL-_TSUf3tm4tKaQi7BwImIn1npWLg5P1dhWROTZzAk2XYSUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🔴
معین توی کنسرت آخرش اجازه ورود پرچم شیر و خورشید رو نداده؛ وقتی تماشاگر شعار دادن وسطش آهنگ خونه، ترانه «بی‌بی گل» رو هم اجرا نکرده.
🔺
این اقدامات زمزمه برگشتنش به ایران رو جدی‌تر کرده و احتمالاً خواننده بعدی که باید تو ایران منتظرش باشیم معین.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30886" target="_blank">📅 01:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30885">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇧🇪
🇧🇪
ویدیویی‌زیبااز دوسوپرگل استثنایی و محشر کوین دیبروینه 35 ساله در مسابقه امشب تیم بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30885" target="_blank">📅 01:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30883">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATpUL3dgGz_kH4E1k0NCgD1KWv8Z25CPC-6EiQ0s33ewqr5Yf0Old2KQaWpyhRw2raWOcNW9KqATT1zBiGM_H4I7ZTyOHKMOONqfwiNLwDXCdp1stvr7pJfMEmhv7EM3IKIEUSkT9EBytHMNR7XhxRuIay3QbKjHsI2vgdGw7R3sWedYRvThx9VCx9A-pITIVbLGFOcTEIDHUEPEFTZj9raW9olQlNiRWV4NShwa0kEMeAvtR36RYxYtGT3s9W_RSbuJJqbkukZ6s_t-puCRBz-GPV3s20s6JFvVQ_9UtGT6Gedjyg4XGTfLWJUM_L-lGmsiPlqPXWwoTaNlZg9gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30883" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30882">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEKUn9PtGWUknrfkSzvHdtXd7Vm3hPFaSwjSju1zgPn7TvlwQQORdOTh0Fp2a4OFxOY1Ms4IkuZ4zhoBEZXGETS1rfnmBEGcfUJfYjsx6rua6LxUIbTGjZOiMdx3zQAwOfXIGwbObyEYhj167zhj8z2SuLGVru6RVhM3rM728Go1qn2zPMRE3qBgfTlSYbTGFDigNhUDS-zUsYxLa8x2kzxFS7ABuS1u50URztjb6vZS1vT8SMSxDT0ceKyY15Sc2agQHVqRKb7AiRH9t3H-iUhZ7bb1kNzkrNIKCQILTrMlms8gZFspQoogF-_vNzuh5IL6B1d7c6Zt0DeLyi5RMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
توقف‌ خانگی‌ فرانسه ده‌ نفره‌ برابر آتزوری در شب درخشش جی‌جی دوناروما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30882" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب ایتالیا - فرانسه، بلژیک - ترکیه و هتریک دیدنی رابرت لواندوفسکی؛ لوا با این هتریک در تاریخ مسابقات ملی 92 گله شد. گل‌هارو اصلا از دست ندید فوق العاده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30880" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX5Bf0fHXDzdP93JY0u68ELL0sMMNg8liPLfISVa_2MYE9rIoreN29tpfBllzwLKtPeIhXJJq2tehxVH9bfMD82eNb8fU4Y4Sj2SgWJavLjA6Zihk4Ew2ATquODvpL0pygQ4OeICH-2FW0k5iTAMOoDJXPUqm2vdMWiCCH8qIHpw7Qt_2V52gauB_6yBMLz0FBp6wCdraun8wzXSS9AVCI5fDZNYypaF5xgT7sZ8xWpE3vttVoCI7JAwhWP7NpIjDswh9aQmk9cNBr3NEP_u6VG4yGiaYT3MIm8mmttGGYfMZC7Gxgz6WX9WQe_3CQj5gDgsrzCW9jLt3t09VShriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔴
پوستر رسمی باشگاه پرسپولیس برای زهرا خواجوی گلرسرخ‌ها: 2 بازی، 2 کلین شیت، 8 سیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/30879" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30878">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxWFQPhgMUodx0DoM29WbV4ucdB_jfnMvQPs6NnnbgxLR3fRFrUG1EISmd1Iteq34etNRAwB3e1QIt2xSuvEx8wUbE-0o_Bv8NyQ8fPLfc9xL7A9FZkAtHoQOy28kg6onoIMRpdbSksEBA40mCAEH101QwKiBwUJzQwgox3UZeP4LGkMhI2gNgHZeTdPvRDw4MSpAhzmIUbt3Lmsu6Y5um6C-GzWO-tVMLfXpgAMCbRrGUzbl47abA7KRBT9qr8TRrFFr3I_d0K52NVDixyx0jk_NDTfUbzc7ac7BIeXEjiPgHzl6A3I3YAIR19AzmNZgkpDsYwzCEGP9HLK-x7kLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های‌روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های‌مدیریت.سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر! P۱۰
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورودبه‌کانال‌اصلی(آنالیزهاوفرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه(چت‌وتبادل‌نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30878" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30876">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKoARRh2U9b7BrxcZrzp8tJaSaJCFQmkKHU9TRmV9PE47jyzTJGvAX06r3IFZnlhZBLPS6sV3CmoIuLMJWUZMsRtFLgwNZ-6Z60LeWiwtZj7nMtg3R4M_Ja-f4c_Zw9-hx8I87ltjzujrSQwU6oxRg6mVtUE-2rkeMJ2BtyA8Ln7yatwlhIv5jK_mqeNNh8WP7t0asW0pLfR-oArAjdhpvCFoNYVU5Sd_EPM1w6n_IgJ5UCC6Xv7w1MLHYc3b7iMUKRxFhdD6rPxxnL6NpjRKdwuhqCBnUAuRVFjQaUAocXmst43RM5ohDRIyXOjltA7zjV1-GNzeXIO9agTipjyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه A لیگ ملت‌های اروپا در پایان دیدار های امشب هفته سوم؛ فرانسه با ایتالیا مساوی کرد. بلژیک سه بر صفر یاران آردا گولر رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30876" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30875">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1WhMUhwsFvDr2ANcDhuv9U4fBOGSaLrhBqGdTeGw9oRT267ItoLaKQssXmlOs2Jgc0DM4D3JG1iIoNkH09ue4zFLuy5Z1TW_9t6-L2FmFZBq7hlyXc9WCO5FSpTn0KQmzW97wVAQXz9IG_pEP3K3TVxJ7fJvB4gcBXCzxfS-EYCwuRSAmEVcVYZn9o5R8gOh5boGEkCBZZWO7WepLNcva9l_1zzNm77vVzlIafV9ZASwZ1tRA4Fo_Nm6p4D2UgoC6AZpUJAXJd1Nx0g8cnR2cK9iOXMXdEqcLTF62Pw9UKmA383gRYNTnfZGBy6FN0D3zwGnCCD6byfBD4cUYztug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/30875" target="_blank">📅 00:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30874">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKyc7dAZqqlR8AkIRCcpud95jHCsBIpUdiZqhSAbUA7k9OZdUGtiiUl8iC3Hrz0H_6Y1iKK6h3bFHKomnedDH1NvBss2w-p1f_rhdaQoAS30K6qOwHADgvJPti9Tb5gnyayYboxkTPweeLfi6lv2keRSjmR8o9WKNxQ7v7rRHj7LVSv9IU18njQMtUAKgadnoNQZMyQT6VIK4vRjggNIqWFWPHoIRRP_Flc3p3RLVKGOIob3KNwMOHlpUo6wSpvA5SFOdr4G-t0buVEz9PNHpQmu43E6iPHypiDswrMOWBZNvNP8w9Pcv2aWei4WBkHlbdy65vtTsaXVizVv6zOREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30874" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30873">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnhg4x137I4BB_Wht8ZkNRj4CW5fVGXYE98ZwJg_JQb34oqLyGTuqvk3-UjfP1w4B82OE3Uni4bUvvp9di5zX6sq8O8qJ1au5SHNkApxDaoBr4kfeKUmos0oDyw5LlV2nIQB3eL2i8GOZPx_PphXLvJkUpj8GNo7LIhf51aT1kgJLALPwkoSDCCv9Yx5j5p13XXt5E4TtmA6FBmUQBhbXoQCoTF8oXUKZ_Ux3GcKBH5QqSkRBOM2qwXfNJm32sz6BpFf20hxYPapzMEMOM3jy11MTvsdHlsR9w-G8BSDyPlxLRZysmWlS2B1kIp3kAKB4jaGp9zubDiVrC7aMqIALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال فوق ستاره تیم ملی اسپانیا برای دومین هفته‌پیاپی بعنوان بهترین باریکن لیگ ملت‌های اروپا انتخاب شد. اسپانیا در دو هفته ابتدایی تونست بادرخشش یامال انگلیس و کرواسی رو شکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30873" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30872">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWH05AX1h6DMdG9s_Cb_8hjE60c0ixGEqPgXnpal6Kp2lc6lbMC2bpb9XRQW_nyNOvIz_xx8SxW1mz3VLEx9E6iyLnFoWRqfXIBEX0cjjCKqp1Z_F9TNqEB7kkKh1hdkcgzgjm-_yso0-dabceQNdPR1Te-srZxwZT_nGFv7_00TlinGUKN3A0CchnJDl7WcuLoAJ8ar4UIi9hHRrfA2iSIN6aPLmOs5LebSkysd8gZP0v-1-mA_ADnSAid0a6W67H1fbpgBEw7KagL24sB8c_q4t-hGND-k5jCKt_HvaapaZjed63ToNenzbR6mApWGBr-3tCLpe1G8qpDBPznstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30872" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30871">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQlh5E9IqppVLlBZLXdwmLakWcQ96wQMnNPqq3TmKqTR2EuGzZqml50PX-e_fBC5gzObaEhYx-4oG9WImm1lK-wvmVdPrUdv8T8jZADVKEDGB3E9RQGxxBTryfdowTLXbp9t8i2CPhxc8Sg385jmVihvf0_01Ybt0_ljq8AgjOdyGV29V6--rQnSKUbjbp_jCysXMLelGd2nHcGHl0rPqOG8KGa2J-xfmL3F9CJRE12BNKzu2I7doosJCzBQPtbHp9x5zIbUnBfgkLWkPM01U70P4EG266nUezM_XlkZYhqhqNFRWTd67X6NBv7uii6lbQcKu5zIubLjzCDaRNgJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30871" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apjGryAQ5uVe8wnJP_eHUfXITu-LoiCVobVwgTkspMH3nlnutn1dIxWN_y6z09s8bv6ucHCdyOnTFUSxXfjAyUvL6wS3LlpAHPGoE941dt2jbD4h3liaDrIv3Syq1XgMC3__TcK8pFZEQAmvtCFMngRq8YnQVvZQE34KEw2QOyYZbo_MzRRxWhCkM5Vmw7uJGUqpyW7CsV2pKB077XHf72pjqXP4npxqGnLfQSpG6PUemmFIIWavoYo73Lgk_r9n0rHHCPCLgpa3wfkruv6YmzlcxtwzBGdf8KTGJ7lceBFVPxomGZvTdoNAAdJxy6KI7XwRqDvM56c1STZI48lIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQOy7K4uY-qn3MqRntQJSNt2OEHYtwL_4d-CQTVU3LJGJh73yzUFA8sg1pzM4EgLdAGwI8kLXJJ0Ln0HIPexiZWJInvBwcpQ4Q3YJUcdVnecmGFUc5b9JI8dgqhkpDOmDamPsXKvp4DT_WhsVIlwsdn_kv4JoRz9IGy_qwEJb2aM_Jq2Gf_Xd0GA-f50X6_hHQHBIyqVw66X4RQUto4wW6ci8r_HbEIieVXeby_wq9w5SJ9euQvSAQwbAjN9Y9Zwa0om6t-L8C_B0uQ2pbrjjgsCP7llRPY5IUBzz-Vv8HMwn_oZgx4kS9Lcv87bJbSYCsThtCOF11AKbhaBuli_aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تعطیلی مطلق استقلالِ سهراب بختیاری زاده درفیفادی؛ ۱۷ تیم بازی‌کردند استقلال تمرین کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30869" target="_blank">📅 22:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30868">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=myiT6ZPnu6w3BW2noRXXS5knhTey0W964eFpWzbYT7tlmCXSOjnzfAJqq6JgksJkwqlEIIY91mvk2g68bKFSyToB5z04-geBmduBhlDpdoKS3YDqkqGWuBJTdzp2MnZiZ82sqfFhKRlhm33kSFfkiMmEZzIyA-gwwL0n7TIgzmhUuAPxi_q_IghxAyvyKQ1WURnaMuIbbI1wTFsN3BGxSFpYFWj18FXDNrwGHrnrLeTomGOvPI5Pj33UMRnbaAYpAHIXvB0UdwyMo9Fql2DF7Ux9Njx0XRKGI0ObIEAyLVX0XSv1WxiL0j-X6dicBybwq12nMo6fTNT3X5CSAr7JrpuDvP_sJxoJOj1CTfvRI3TAwo4LZA1rx3AYjQQYY4Q3xRrIzuzquRGuqJ3d92ebXVkzR-MO-kT_WpISHyaGzSl4acZw02hhqnlnhwAHpTi84DZLaiNA1HQYCot-0JKUChEaSRbJDNeZDdcO-_IwAwuuVSJXNrg0pVMBOKc6qRO24OX3tXUcSJz1UUWU6EMO9lQg0zXAJ6wbKS_N5hV6HAvrywXLgVEGp2mVGuQftx4kXSuBwHEWt_za2SgEagLIIyZLwf_IK1QcRGvlV8MeV4ajIq_jXMPuWKAQoKdJ0vtjopGn00TZShlo1U0x0EjtvP9aNGUOrrImZDzTpZt19c4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=myiT6ZPnu6w3BW2noRXXS5knhTey0W964eFpWzbYT7tlmCXSOjnzfAJqq6JgksJkwqlEIIY91mvk2g68bKFSyToB5z04-geBmduBhlDpdoKS3YDqkqGWuBJTdzp2MnZiZ82sqfFhKRlhm33kSFfkiMmEZzIyA-gwwL0n7TIgzmhUuAPxi_q_IghxAyvyKQ1WURnaMuIbbI1wTFsN3BGxSFpYFWj18FXDNrwGHrnrLeTomGOvPI5Pj33UMRnbaAYpAHIXvB0UdwyMo9Fql2DF7Ux9Njx0XRKGI0ObIEAyLVX0XSv1WxiL0j-X6dicBybwq12nMo6fTNT3X5CSAr7JrpuDvP_sJxoJOj1CTfvRI3TAwo4LZA1rx3AYjQQYY4Q3xRrIzuzquRGuqJ3d92ebXVkzR-MO-kT_WpISHyaGzSl4acZw02hhqnlnhwAHpTi84DZLaiNA1HQYCot-0JKUChEaSRbJDNeZDdcO-_IwAwuuVSJXNrg0pVMBOKc6qRO24OX3tXUcSJz1UUWU6EMO9lQg0zXAJ6wbKS_N5hV6HAvrywXLgVEGp2mVGuQftx4kXSuBwHEWt_za2SgEagLIIyZLwf_IK1QcRGvlV8MeV4ajIq_jXMPuWKAQoKdJ0vtjopGn00TZShlo1U0x0EjtvP9aNGUOrrImZDzTpZt19c4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ صحبت‌های جنجالی و عجیب و غریب حسن‌روشن‌پیشکسوت‌آبی‌ها درباره ریکاردو ساپینتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30868" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dePiuO0AcT8HOl61way1MsdutXRDAgikclIC-wiC-TC5w7zrVIsyDqJkl6YDdqn_dOZEX7qn5eUlMVrYGbLa6BQ7lY1Q0gJC3bioDXzmzR27EGc19z1kVUjdf90VUiTDUrqkRNdex-gVKYyYTG9LZ6O37T4MMaJdsG1gstVaGLmSFOqT1vXAeP4dADmVuEdtENrtYJ_2oTN7XzgyVitRaxqh3Jlew8KNI2wjj0yelqj_f4A8MY6C_tukOdFX_wBnRQSXjEdSsoSZ6M9HyEQSKarC_U3GXH7sTwIl_Dzd9bG4ClurFQEOHtRhLEeBoWau7ZYBPZTsAKADCK-3nNyNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30867" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30866">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWXRucFK_S2Y0CSRYklkqBRZfZRSt3Kd8omhaADwloT6uSt08WXRka-JpAXMRo_Ry3C1lsB9O9x7KGPoGO_1CXLE3tYEWSSdGb170eqf0RSsdFjxAr44gAwDa7_3EIAuall6DlPnvY7ajb6pmCbzt9d2KsrUvjx_Rm42weh5wZtrdaOljFiD3lOkNKuz3uptC9PV2uXCBasqDwkeANLWmHNL_u7t-bLiPFchNVgBRN04v06jnuTdS3bJJ9UNqlkco21rIri8zf057AKC0fU8oPFjZozlI2DDmSoe2kHcl4wtVD7wiub0BWhgH9JMFQS4tqrDydCN0_0a-oRYpYxKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30866" target="_blank">📅 22:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30865">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJIjR8DtktUepmy_XUoMvEBN31xQaEDY03AXeIMC3Nqr3Oh-Ogv7ANuSr1OLEJW4jWQAxFbSXR8LXlQAs2NgPtZMZz7rFTQhU4Hf4l8NQhT47wk5FJWrBlKT2ApkYsFpIBXliiiupbCf05VgShHIWMB4n0iL430rZXHRU8DqcpZoGPxbEmt_BK8anMTqYXC0Nf2yr082bAs64k2aH02Wb26jaxWvq2493bc7ImQhfNpBk1iNHzmrGf0n9JHdN8lJqIaVz7nz-3pvnm7eaxupIh6Qjht7KfyA__5PUWiRvjaV7dv3XzLB_1qZq7Vh9wGzzfKcK2xaASSXjYtZ9Skhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به‌احتمال‌زیاد رقابت‌های این فصل جام حذفی بانام یادواره شهدای میناب برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30865" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30864">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0w2dcaRotsHZ9T-vnWz5eyeOVOAUVukmy9vdpGBtESiPvELcLY0VznKCacU-UnbI53fsP-CPHL4OoOznFgqnFVresC5dccYivpNhg3hTaXmC13FibgN692fR-RaoYBEw_Sa6yELOqC3ev7VPM7xRvLoejooItdTNK9UcUsn7EoBSISzQqcCc59Epq4-17MsWFYdcAi2N6_q2sqoW8zFo3DxeOeSxVht_ybvX_zBe2kECtcC4yxcCyJXAqATbnZid-bWd3QJKAIB9N0agVIA0-1J5LD52oiyQOUHA-3_8iNh94zR5vIXNhckiWlr7hN29oyJD0cTDgyYjPImgJqhgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
#تکمیلی؛ درصورتی که حکم نهایی منجر به محکومیت منچستر سینی بشود؛ ارلینگ هالند، انزو فرناندز، رایان‌چرکی، دوناروما و دوکو بازیکنان‌مهم این تیم از جمع شاگردان انزو مارسکا جدا میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30864" target="_blank">📅 21:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30863">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s35ZfaxacP2bhzredafk8Tpj1Olq2H2yBNkn7sxPtByXpCeARM52XlwDhSAPta2OIw2d2s9fFGMCByLYgWg_HRXfIr29UeSGyzk98K8DqKX9RqsgktUjdKqEwU9G1FKxhyPXwjHs6O43Cc5mcEsDcbJBnIh6Hhd-qbTPg8DD1TViS2y0PdcHG6mRcjHiKGHiF_JyQ1tRmfmIXwGQovQ5k4hfg6BRbtJBpe7FeXWJ3N5tSPbSzB51Ad1EwOBIS-eNR3qisYjWbZBrTZlbecNTQIpDRaPifM5U_AaVlEVpln3gtC_FLnUHhnLcq-u6Gt-43CV_PFw3YufIu5N3M6UroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین و خفن ترین ترکیب منتخب تاریخ فوتبال از نگاه دنی کارواخال کاپیتان سابق تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30863" target="_blank">📅 20:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30862">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw_hw1cqPJsy2PP9LTBocbbC4YHErOp8KXGHKiBBuiD4NQynSxXZ7lm-YKPIpz2BLmH4MGlYtpWOap2erL8ZAxiSRjwkQughulZbAOg4p73lyHwlsBiC44GIsOyM7H3YEtBb52pSqYqVtta-G3t1Us-zJJ7f1WpgQCKEe9is3e40nR8Qp0cW9Tem483YlU1BlSMHy-E0y-b3pm8nOgknc2k0xVa8vSqoBW3rKmnnl56RlClaEsYXfTU1BhGzK_cu-eJRiWjFoLJGVn5q3IRFZXM-EzjowvqZK_zpu7n3800un4zVeifjvnIJB7bFPXkwIa7LS5EbF74deL5zIHM1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30862" target="_blank">📅 20:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30861">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg_69NKyVAINgwfeRJJWTRGhNXhjbDmyvu8H0-bACD-MV4qlq-pPI-DIApfqcmOGWezIUos57Xo0vtoXgdq9nsOLBDM5YNmklWGMRLm0QhSKwKrRTt91Nueb16i1S1ipoT0c0__aM7pvcchxQJG6hFTiAzFq_KWua1rfOSWwcZ75oL7wo6T0FmkraJaboTCTaY40tHYru9qlH8U2khNN6AEUPiEvGP4awDuqT-PWD7QpgaPheBdVEIKQJD9AD-U3Qtled6_Sj2O01_odSf5ftqKSGM8Eu8BTK8ZTEeUAA4FsIRa3tgoz_a5BiS-tQsGQJU5axdjuqvcJAzW_lt15Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30861" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30860">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grvGT7dbuUFOiiatpjQiAqrHbAn6DKCyRa30cFk1b0SifM4KsJ79sK19PTDNgQCq5eWEMVQbnIMGb7eHMN4kamNOFxB5O0tOWX0XAOhoXvwTz3sDNNYvt4eRtttGFaqv6YfX0JkENd9VPBuWc9_WBnordmdleSKooYLKyi4hpWeuoHMjz8oJEAwaGr8D-L7qXVgT08g-yT9EiKNAUZfs9B4OKIfleJ7-o_lX4_BBJKMckR8QgSiOon2HJneET-KmXvFqEAMqE6tKp5ibRvjXAEdZlFQ1Mnrc9Yxn4O-vHFWAyrH-o7DlBpM3IH-JRJoI4CNUzD3w4DkWfQViarYzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30860" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=fxUbLTbbDFQXxJQkm0Kmn3L43FkeGpRFOTuwNHxoF0-9vqcQICqkTiEvf51zJ3a4aZTuv02dzfvTqS29yErAqDwtBBkuTpVCJnBREOeMmPc1oz7ATqp-Be33_qCzQYwuDisPDhMelQeOoEJoBmng0TLYKFbqCccB0751d6pfyjEO4-VB7w6xw1dHIprPy-tF_X80tcwmYDAYrtQ0-MExE73SPr9i8OBAmZH-bGsxsIgKRIvEVXCpxGuxcFmA-hj54QGGatAyrrwFPGaeITDR4t3jbz0-P204woLzATgaeSuVbeXYRTgqSUpf66jRmM-3g-JriZ49Mwzv6jIYwwitcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=fxUbLTbbDFQXxJQkm0Kmn3L43FkeGpRFOTuwNHxoF0-9vqcQICqkTiEvf51zJ3a4aZTuv02dzfvTqS29yErAqDwtBBkuTpVCJnBREOeMmPc1oz7ATqp-Be33_qCzQYwuDisPDhMelQeOoEJoBmng0TLYKFbqCccB0751d6pfyjEO4-VB7w6xw1dHIprPy-tF_X80tcwmYDAYrtQ0-MExE73SPr9i8OBAmZH-bGsxsIgKRIvEVXCpxGuxcFmA-hj54QGGatAyrrwFPGaeITDR4t3jbz0-P204woLzATgaeSuVbeXYRTgqSUpf66jRmM-3g-JriZ49Mwzv6jIYwwitcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسن روشن پیشکسوت باشگاه استقلال: ریکاردو ساپینتو تو اردوی کیش هر شب دختر میاورد تو هتل و ترتیبشون رومیداد. تو سعادت آباد هم خونه گرفته بود مکان کرده بود. بعد از تمرینات میاورد تو خونه و شب رو تا خودِ صبح با اونا سر میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30858" target="_blank">📅 19:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTu0tAvaARUzkBZcOiMdKelHIutnRKmH6L0TB698_lHsBaEj4MPQ0ZO5IDxe6_NVlPTKCHsUa9L_9qCUEaKMzomUmn7rpG9yEiSt6nZ8_hzQVx0WPSdT1vSYWXjAqvTAOfI9uTcFhbZjeFFmMrW9ce2PaUYmVBq4EuhEyV6H9UMnt0LV4vDPbGZ9vbzmNRwDbmHV1lmqBUK8uPN3Wt1dW4AhUTWMA2O_Su5bQHcEAzF7lcnnPmQW6URxGZ64m5_CQMb8sNNMxv0sF6nshmz0KONADsykpEJfQza0pMV6_fylrZZCeLf6nSQqAhVVZA0ofVsr4Goou5K5rwwC9Ed59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30857" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFcSD2lCyPVoiuTER3-fiSukSsRw-S7KA8iewf2Y2orYHb94JOxndUKuyyWqt_KC458QlTQ_AZnXz9ZiGCX4UjA5XdrXKPmUqnW23BhgFcDxohL0tMWrtb4TfNWe9zghxptABa-sbb0N4ENf-VtXvgJ7iGxKA9_qZIMHOqunnkVqUygonU6-nr7tny5LD4elfgtZk6mcXB4YjX-O_Dh_1YMWn3pHx-W-8y43sYfy0VixOTwEacYwAdUCiEj_VBQXY7MW4kErbgZVDWeaKjQgEwsJOLI48K7VNHzxPfFYznl8jgIILhI_y8Xr3YPTrohgx5HNpAxrxLFLjNGK2LgMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رضایت‌نامه ابوالفضل‌رزاق‌پور و یوسف مزرعه رو هم300میلیاردتومان خواهد بود که باشگاه فولاد خوزستان درنیم‌فصل با فروش این دو این رقم برگ ریزون و سنگین رو به جیب خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30856" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2DqSfA507iYFmVsQRnOzCDeGzu0BIRJTsqYTmQAcNFdefOIBPOMmr9bKid9BEqq4TzgdDYGC3icSLUJF83KO8lhoVdR2ScSaGkkLSvQNzkFu50T0lY2Jg8H8BmjrjnLpjGMNMvbybZlJpljUMGDAaA1OQabNWRmr60tA7tO3y58aQZC_zGuwzVpClAOSQc2nbLQpVUi1zT5lcePP89DyCjwrFAc6ITsujswtKGFwe485adPLIzwehu7rdO53g5GNsunHRvo3T0kqm9cJisxkt0ADLvMKNiNkqroI0OdxlLoFBk656Nbzv044wyARC-zx6XvgXPBRUSunvETSH5xOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
هانگ کانگ در شمال نروژ، با جمعیت 2484 نفر، جایی که خیلی سرده و یک زمین فوتبال زیبا داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30855" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWZ6Yzk8uow8Vt67Fpw63JNTgsVWGQV9o7SFmWoUiaoVaL8X7Uvfv88Feud33ImC-ITLEYLI4O9jO4KKRENRP1KXS9f3VxlKA-NjaHicqNdbLw3GU6fQxWKjhDISGBue5myo1VI1GkbbnyDRYw4Bk0pYAxek-8Eu9WBDqMqXLBKkFdqL6No4VK9cPKkviblvI5vw_k43kf1t65W47XuJa4fq9gsHVW_bM0NnUuEhqjUrB8gKzktwxrL4y2NGoPawRm4vLYDEH-1ywdj8DPcU_dhJerUP1Da7RUzfOEcOUTrkLvpw5UELkbE5YqPbC71jCUg_qofzg8jN2b_4wGB_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30854" target="_blank">📅 17:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVZ17Fjeo4ryLZGvRwJ058HTG7GjbRaRGgKqF7XZrrTtPGtoQmWiNp7IblkcjWloKTVF7OvjLCNJH7beTvSIfkOdJqltlLkeUfA6Rj6xZnDzkVLgvekpubkUvqASaOh3-iA7m_bfyJ8AaOwK29Cb6kVgKcL6jjYpbZQyjpEzEVf8gnhLnQ8_QkYZENVu39v1J2W7J92d0B50tHqysTFip4tdY8bwLl0PT7BRGj2LTPpGDn2wRhqLZhsG9GtO4TP9d2_K0CRI4AnkhYKzN2Dwi1RPerxUeYH82PT27LAW6qPvSaXgpAPOEhTh_WdeAH7ojOrV16-_mEsr0wBzaerw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30853" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2miiTCpq7H8A3c5c2C4Zhe63eU8jED_MBDK9lfgiHiNh4ndIavO4qMMGVYwMNUOe8K2sAPXDb9ibd6hztAbQuUXJwpoZh23a9OrnX_hUazJqoMWHezY4vmvOKRtJL0iGwpjbg1tqXWBWeIb5o70X7saJ4pHZu8jk3NpH_eFTz-4poNHxRY5D2tp5Ecm9wu2_6Jbq5PAa3QsIISQ2W4_Z5acA0AH8B4ksC2IVVwCFV6JBYtUV1lk1ZLSR909mUj1ZLNRde5PR_TATldF80t2yD_2xC0uRHFMqXEsvy3SK6noO4znqUYuFdrjdBVpeW9P3XRMLSLZOjWhvlThKTyjHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌مولر درباره‌بازی‌معروف ۷-۱ برابر برزیل:
بین دونیمه تورختکن‌ما به هم نگاه میکردیم میگفتیم چی شد اصلا؟ یواخیم لو بهمون گفت نیمه‌دوم کارای عجیب و غریب نکنین. نه برگردون نه دریبلای اضافی نه هیچی. باید به حریف احترام زیادی بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30852" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSy3IxueOQgsh7VBm_ZH5_wnzYNoMKhDrgqWHjU-N6EAT_f_Ve9h6IzTTH6UTDOn7aHGUy9Cznav_Y9s4GSHbtErbabPHS1Q8k3BxFRoT-M_WkAG0bcpr8DsLxG3dsPwAfqfuIQi06XYm5hqpMjU-UKiOYlEHe3Rso3x5ou6PknAQ50XiT1EXI18EORxq9mPZXU_bZY2AkJKc_QqAiG8wWESrfWs7e85iiPyGI1RwREZG8Yyz13gCcdJSt7BN3vQLVECeYog9EGcFIMT8LPjB_mV7AMmF_fFI22xkR1ZvKQvrAes0YLJeFPGyGQf2p8J0FX3vrcrfPkAvtJY80iiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی که گفته میشد خورخه ژسوس در پایان بازی‌امشب‌برابر دانمارک درباره کریس رونالدو خواهد گفت و از او بابت‌ این‌همه‌سال حضور دراین تیم تشکر خواهد کرد اما او از هر سوالی راجب‌ این فوق ستاره پرتغالی طفره میره و جوابی به خبرنگاران نمیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30851" target="_blank">📅 16:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELRZzQqV2YFan02uM42TaDWpVMAJHSTSsMPKILbzwgsUa_jv-lMOTXbrHZeddO1IZePqK5xqxDTQCPa4KODkMnK68VYRO1Vr1ZrvkN9pqhFWlhC6KHwJMOoiT7AuKb8BIDPSZ5KPaRJIYWhXYq5Bf0-zBXPQe9aqKOwknJhmSJonwopE3c9pEmNy6VWUT5FtLNak6MkJm_eF1fcX3-rU6QKDZ_OOj27zB_ipUxgm_0GlSuW88VapVZnQJiU7-dyLqq3IMiCp6X5SgFoV-tcQOE1NWWgtDmc7K3alBG_LYLtTTrOyoEIB7YFblHcRg--BEjOJbSIh9TBkVtEzAjv45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت‌ جدید ایلان‌ماسک:
اینستاگرام فقط واسه دختراست اگه‌پسرید بایداینستاگرامتون رو پاک کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30850" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4smjeO8emmbjtDB_1WYOf51L5osTfDDz1ngA4jOELsfEx5yRvaMgGizDZLxMDKfmeIQi0k7CvUZz6XM12XqpyT0HfjyCPbBXE8xvkTl4PZYAq_9EBGVSYB2Yud80t-QIMd7d4p2h5a8WUudV-c08TDzXfGBvJYSWsTeiIT5Kto9oRJgrIq6aner3VcIcU9qmzu1kj0gpqqb_LodiYTtJLJKzez8PL8wotMbfUCi0PvMm2MiJ_1QmVx0OwoDlwPbGGViEa5Z__9YcG5Rx_gSi9OL57v8bMu4GubVeWBUooCk9vOWbv_j1lyw3z-g5dyFW0BMis2TVV2IS2tA-WDceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30849" target="_blank">📅 15:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30848">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAH1-Kx2HHu3Wi0TX0nsV1HQxebYuy_Be1L3zfBqt-uArrIZxcJPJWj7DmXsiTMbwp_-hpR5B8a5TbRUwBSM2iEliGd-HSSfUDmHStYioA_mEwy8KlZZOW_xJJa-R0QB6UIH97-yMB35cr1aO2LPgc4AJZynF_ezQ4GPuAFScvTGVNsuRd-NtIbVrtL_MHRb--oDAFQsmixr2qWN-92Mo6UauQkQa7GfQSQSUI4gvqxurTItijxwt_8xumR9HNtVlWUlV8m5-zIY1kffze7taVrRQ515g-Np1KMRMULqdWviw0bEAe10FzZbhFNzT1n8F_K8b8fOn7ehJi9dQulV9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇭
روزنامه AS: باشگاه‌رئال‌مادرید گرگور کوبل دروازه‌بان 28 ساله تیم بورسیا دورتموند رو به ژوزه مورینیو برای جانشینی تیبو کورتوا پیشنهاد داده‌اند. درصورتیه ژوزه نظرش مثبت باشد فلورنتینو پرز با دروازه‌بان سوئیسی دورتموند قرارداد امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30848" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30847">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piSA9KinMzGmRkicqTRjtDAuNPPKzjcOkimD0i0GE2eyulzJc1JNrOKr31ruxuXWiYr_V7lTYUUsQTP2Vkfhpb8a2-t_ernH5tlrmeQ9AI4gecigvUd_3rPz6FMN3loYeABiEzJJZD7hJpp2WjsRbbrnbxuylbaLrDIBBWOMayg-9gPK8rmwGgYuNrT9cXY74qFv-3RdGcfKwkyH9P-5OhnCf_h0_ThJhfMsQkvmhXuBr-PSnp040O9Q4KGQSHiVr02Y6_xNoKc3-50-VZk2gSW82Bgb3dl2OlgY_asZ7v6KIdpCELDEU94QbfCvetuqTB67VNG3YxhP5ij1CnH9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دانیال ایری مدافع‌میانی پرسپولیس به دلیل مصدومیت از ناحیه‌کشاله ران در بازی اخیر تیم ملی امید سه هفته دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30847" target="_blank">📅 15:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30846">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNGRkJH1FI-5VbvHIKg5cGN4d1taNwnD4P5gWcN7SqW8T4mOzu9GO4uEwb1NEWCfJb4UaUefptwJwQRWwjyerl7tNJJlnFqAJaS0ELeIeVEJprN0FAY8Rk4iafIQjbFc7OANgg0xcKYcMWf5etyizKmPgx1BpjgVBlCLbXyaZ72vFTojU5m1Qcp_RQ4pJYtL1w6CPew4sS0Vr8sq5buKW8QhGFDikNm3bke9Y2mPXrV1pDop2_lVQT3hdiXBv4_lB_8iVJ5tWB3rcz_rvYaa16z2moKLANMtTlbEd0hQMgBqZBh-rqdk1q0zjJeOpxZKJoFiRFWtdXbz7TrLv5rpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30846" target="_blank">📅 14:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30845">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7tQ2WUgAiNhc4L_7hoWj4uAWYgly73iL7kIGatzgf7LcQgiCKT16hq9nfjk7yuOvhupc11AzNB7TWicOBfPg_6YarWxWhzmOeO9xJAJhbvPWm7OMZ5HB4wg0KU1afWsinnIS6eXv_HGl5T4c0K8PPLmnbfrjjYRmdc8Gucvq95LVGhfmatbzUWK415sspZepC-dfIMcfOQ2qBImVt1ASPmbf8mXFYT1TCbb0XZtCtc1zBtgVIG-RGsd6jDeK-SUQWwKDNvhybR-jc257O_qswr4rtZXI1jlzz2X-U8dMlGCZXzt17bhLqIlIR1Pe1rrGaSps86LVIodKfBe79hNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه پرسپولیس؛ دانیال ایری مدافع جوان سرخ‌ها در اردوی تیم امید دچار مصدومیت از ناحیه کشاله ران شده و چند هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30845" target="_blank">📅 14:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8RQmtGVBGEKGUiyGTkTxnjk2SURBrkSnoDwvG0de0-d4nrA8mF_4BqgmIfmLabtYcOyRltrR0Kqg_OwciHUXSySEmy5ozJi5td2EEffAf59YbUAJs4_CmUkGlgO-IWgVIc_haV_IXTMaWZe0WweizCqMcw2Sp4H2bj_7-m-VQjwq9QlWPhsbpQF7QFnIJkWY5UoqMZnb4AHmGbEKksOZaq_uhz7sYjufvCmUh5q12Q0H_XHMRjBVW5ZetjamFgu81nQHe3Oovr9YNv1VLnYdrg8GfNUsJuqXFZztHNZ8C5ihoIXj91KhIjSjcwK7xTkB6cOs0Lz1vy154Z7jJjQUeXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8RQmtGVBGEKGUiyGTkTxnjk2SURBrkSnoDwvG0de0-d4nrA8mF_4BqgmIfmLabtYcOyRltrR0Kqg_OwciHUXSySEmy5ozJi5td2EEffAf59YbUAJs4_CmUkGlgO-IWgVIc_haV_IXTMaWZe0WweizCqMcw2Sp4H2bj_7-m-VQjwq9QlWPhsbpQF7QFnIJkWY5UoqMZnb4AHmGbEKksOZaq_uhz7sYjufvCmUh5q12Q0H_XHMRjBVW5ZetjamFgu81nQHe3Oovr9YNv1VLnYdrg8GfNUsJuqXFZztHNZ8C5ihoIXj91KhIjSjcwK7xTkB6cOs0Lz1vy154Z7jJjQUeXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30844" target="_blank">📅 14:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8qwERxnqndJ2UveXefe8AYJf_bmIJS3PnajSxYkisH3Iv4MU3qVS6xx567nmRFZFqkrl7E3B51ntreA0yZ7idSD0xzdcR3kEmhfZOHyJ77aI-vKbXutJroW_1_suwJq1ALT-Y8LLMI4zzFnQoEvjeL6aStDILRhMDXsT3HFjpXIilIA1Mbuqena_KA9Fv6LzGDCq902DlIrpU0oXcIKnWWOad9W3vsIx2K31y9j47opYCT8up7JllsC-FoEE9GUCAvKKA4RB5K_uAuf4JerQqCnu05e9zQ9O0i0E3slV8axCbGqbN2YFiXycWC49W_OXxsm77Ppes5lsC3Sp9-Qng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ‌امروزمدل‌های‌مختلف‌ کنسول پلی‌استیشن 5؛ قیمت PS5 Pro درعرض‌تنها کمتر از یک سال از 40 میلیون تومان به 315 میلیون تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30843" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRD7diAq95B5jyRvDkKaDQBFI1Rb-Nu3PrQRm-3fbln8kY9qwtIBXDp0TUpW3g-McxhzeOQmpev_xFnGZEbhziEUEy2Mv9p9oxZ5CWTBsaOzjXgl6ziUtP4PY13JyzKsnIs1CoKjjmAIyttT_0iaYTsMILpYFRgQzMzppc5S0-2yLhrx0JEfN70kNT5MGC8URj7EygdJDl6glQqOzIr4M9t8O-kt90DIB-iTgsHBsbzfau28iI4f5Y5tNHDXv8JKNGfI8B65YkaYPEFdQlEEgT-g2pnJpKCmJrTGR3F27uktXTuLggbdXN9MNXqV2YphbNZGypa9P3GxkD2lw8BP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو:
پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم. از این پیروزی خوشحالم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30842" target="_blank">📅 13:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAJCSovz7sjjhSCHvvyza2doEC56ZV_jKXtbL0qxhaWZt8Ke17fWJCfKznaTmLXTTZIpo2Sa5xJ__MXF_nfCxPAKqv12W21zpMuZ8xtN146QSLJg0PHC98diB4v2Nii1Mhanf9vXDv6niKAsL1jot1A1vBItaFsb-jaGXhgO3ARlDDbWwDW9ha3U_wqY6ABf9k0unWePPNBJ8ESpYB4owIgvC4mphH64K-Pytidxr7gXvBeYcRfrmMWMHwAmdZDxOSP3B7mjGd6eXzCPq-ivi7KDRqUZPbwY6430HWk7llz9O3AQlGa6DJIl4Ru35UvNwT1WEkapHesoiIKg7n2o0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین‌شماره‌هفت،هشت، نُه و ده تاریخ مستطیل سبز با اختلاف بسیار زیاد این چهار نفر هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30841" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2IxpSJxwLfLBJxCH-AQWJ8DyDnhTvAf6bt-vZ1SqUjriiusE02siSZm4gIDh8ndyzRuhM7FcEthq7r0_H0J3jlR358pGzeEjZ2zM9cQN2blo3uDW891kB1mVV_d0FMGWkfK769PT07yPRLZ416gFOA2MZpZISW0puH7Ah-v37-0X3oE4bvEKuVnjVlIVsy-5rK3EIhS7vy4vKTwV5TRJPU9k97Ui1P82Ep8CnlhydW6O9mtrrVS-n2pnqcwdN2j5zHxvyEuFv5QbLTXHUmyo2YqH-kX1KbI4Rzua-Uh0jm5cDcZgFOny4yF2yEc79irsFBxUAeZ7iIWmRJRz-zU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لیونل مسی، کریم بنزما، نیمار جونیور، کیلیان امباپه و وینیسیوس جونیور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30840" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30838">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s75hnftR_MwRQ_-t6Na5kPK8cfdjGKXDs5fBQoEoAU9a42VbGdDBxgP9uSCiGykPysAk1ToOrrkO55fTJAEo0nZ_1bgExtVfV9AO5i2os6I2LFXjy69Q83uYwAwCFrY6DsSfIYwbGVnPExcXgWpbRqOj3AqseRs1p5mbP4JHbQx_zjolVGAAakHyFQfqG_SzZ_FQkrghifoqwNrEZTBrf7U3cVhgpzy7vpm4suafRVDaOeozd89sGY2j-Qbe_MB-FT2Lu9MfYBQbQ3BDtR2bhHGy4JLdLVb0AVDN__pYCagY8E_aYWaMWtUqCfrQCgI3WvD1uBJcZ7PywVGy1_1JIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه بیلد: سران بایرن مونیخ از موندن مایکل اولیسه دراین تیم مطمئن نیستن به همین خاطر دارن تلاش میکنن که فلورین ویرتز ستاره آلمانی لیورپول رو جذب کنند و جانشین اولیسه در این تیم بکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30838" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30837">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNHgYqchiJ2nOeZR9AeQH_uBwPCYC7OiRFOg7tybEtWIut8yOH-3YTilvP3LY4VyRi6gwkVOC8S1KEWGoT3a1B9tZMApX-lMpl53Sb2OTI7Tq1cg2nVf2gm3heKtwLKElIEPTQwXA-vmM2jpKM8xYfNrXfeSM7imYzs0b5yRUoGktdbxY2-pnk1wNQwGT4NfoGZcwW_LxYOgW_lgyTT-clMyidfh0jw4t-iPYa2TlzVFdmRvVh_xF_UdneY-Wn_QvON8iZ_DmsOncCmxuSSmckHlrTPcTn-tMz-qcj5XmhZRbcAi5J-doBxurLn_IpAoYXi_gFxUQUW1_FpQ0RFejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30837" target="_blank">📅 12:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30836">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=bl3sjM0tiLG-hhuw9QI50rAv0_MYGT9u5hDp3q2BbSYoUJM6XnjWGRQ0n_gbtUVuem7i95vmawp9GXjRnnb9zExMZmX_x_wgAsYPY2jZKnCKgPHnFn4fd1Dmi2zszDa1Ia2KQQ0iwwuerh9CPJ5IaJWANXvzUpG_0NpLLIwEupoUNUUL37Q-pRec6gYYpVT4Brety02CFSOKpYn2CxW1nojhaD33YC9mxyGohBcpe8j6aqJtS6ouPA04e3uks8KAULaOYUdqMWOUxhedixlnYh8vBKnTEpHI3UtqwCEFIbB0HmwzsvF4OuUUqInxYHKcicW2XOVsnk5FhYIVL_NSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=bl3sjM0tiLG-hhuw9QI50rAv0_MYGT9u5hDp3q2BbSYoUJM6XnjWGRQ0n_gbtUVuem7i95vmawp9GXjRnnb9zExMZmX_x_wgAsYPY2jZKnCKgPHnFn4fd1Dmi2zszDa1Ia2KQQ0iwwuerh9CPJ5IaJWANXvzUpG_0NpLLIwEupoUNUUL37Q-pRec6gYYpVT4Brety02CFSOKpYn2CxW1nojhaD33YC9mxyGohBcpe8j6aqJtS6ouPA04e3uks8KAULaOYUdqMWOUxhedixlnYh8vBKnTEpHI3UtqwCEFIbB0HmwzsvF4OuUUqInxYHKcicW2XOVsnk5FhYIVL_NSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طوریکه‌قراره‌علیرضابیرانوند دروازه‌بان ملی پوش تراکتور بعداز اتمام‌معافیت‌اش به خدمت سربازی بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30836" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30835">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30835" target="_blank">📅 11:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=QYN4jgKHJMLvqlgPMY0pqWIvkGaX_CfHzqwV7n8OvOJj75w5T8zK7uHpwFnrqhRNPdADbDnStB0_9qzFzfiftMJkplnFZ2SOU07fjNXwwzwhW6tt2aL2Q8p0QNJxI9DJ4F1kPF32VZ3JgqUCuHxwgwCsaWy0U8nEMWZ-qg1fpdiT9itf278Z2DJaPx7T0l9t8hzTZbjGiMBG4yHe5u7tHrzs0J5RqqzbAVvvm2hG2-ECZXNYyCzi7OSOV3irg34nqHu4vm3xDzGqjRFOgDCareN9Ol38ixHqO4Dqd2vyLVzJ21ulZuI9rL0-AEDAma4cwyJ0jj2_QeL7LRZT6sXhWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=QYN4jgKHJMLvqlgPMY0pqWIvkGaX_CfHzqwV7n8OvOJj75w5T8zK7uHpwFnrqhRNPdADbDnStB0_9qzFzfiftMJkplnFZ2SOU07fjNXwwzwhW6tt2aL2Q8p0QNJxI9DJ4F1kPF32VZ3JgqUCuHxwgwCsaWy0U8nEMWZ-qg1fpdiT9itf278Z2DJaPx7T0l9t8hzTZbjGiMBG4yHe5u7tHrzs0J5RqqzbAVvvm2hG2-ECZXNYyCzi7OSOV3irg34nqHu4vm3xDzGqjRFOgDCareN9Ol38ixHqO4Dqd2vyLVzJ21ulZuI9rL0-AEDAma4cwyJ0jj2_QeL7LRZT6sXhWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30834" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30833">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usWXPUSdflKuMm3EfyKqDAvfCsfu3UlCJQL7KkBn9q3qDpownRtoZi4x2s8CLxkk667a0FsS2xnJe81MSSGSwtGDC9q3Gn_7teocWuU9foXF_lIEdawoJA4Cs5XLigWOnJ0vV57tTmIg7tiw_MJdf5thLBP5mIgnlDR4DGuP9LHTjtOF62OQnvbQsDt6TMK0g8Du-fudNMdY60D8R3AgnmMOKHu8m6bbwaDONlUda5THE3urf3kHcypzp2gS8uNS4MCkWf_rZjbC26aB4IadqB1w8o20T3tEA48y4HQSgJopIGAkrSIQ_PAmFSu6JTsGPYBCSfP_4jWaVVAJQdGIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
👤
#تکمیلی؛ مدیرعامل باشگاه ماخاچ قلعه روسیه رسما مبلغ فروش محمد جواد حسین نژاد در نیم‌فصل رو به رسانه‌ها اعلام کرد: یک میلیون دلار با 15 درصد از انتقال بعدی محمد جواد حسین نژاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30833" target="_blank">📅 09:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30831">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPW2sQOnTAIYM4UovDYjv8wcQ3BPezhWMWLLew_XgU_SkhOlNWHEPiw4LEpdYIPJYlHjwjqwnOB882dNovBA5vZhatSQ_ZoaAwsQWzb0w6oRiVWoFSyPVNvc2LL_vdHJGk30lhFxXRQUKVDe9iACiERY0JA6xxgHE18kpdrByv5K8cpNBNluvrt6g8cOY3hwKz3cIoK2vEG0lOFlx0V4l2J8pjoPxfmCT3WY5V4UUjCKqDfAUaMNnRYaol36WqH9J5AF26sLezdqQpLnoWCerWLbumBq-GjxY2tDhTRkBJl5IXpxp-CKXwjqUdmNJikXn0NgT3Wdg4yAUHu_u0PtF3n8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPW2sQOnTAIYM4UovDYjv8wcQ3BPezhWMWLLew_XgU_SkhOlNWHEPiw4LEpdYIPJYlHjwjqwnOB882dNovBA5vZhatSQ_ZoaAwsQWzb0w6oRiVWoFSyPVNvc2LL_vdHJGk30lhFxXRQUKVDe9iACiERY0JA6xxgHE18kpdrByv5K8cpNBNluvrt6g8cOY3hwKz3cIoK2vEG0lOFlx0V4l2J8pjoPxfmCT3WY5V4UUjCKqDfAUaMNnRYaol36WqH9J5AF26sLezdqQpLnoWCerWLbumBq-GjxY2tDhTRkBJl5IXpxp-CKXwjqUdmNJikXn0NgT3Wdg4yAUHu_u0PtF3n8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30831" target="_blank">📅 09:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30830">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7fJwubJt5LdIdI6tA9azli4o78a5OgiD78MHrG5wc_Tq9tuf3R9tueks5uHQxV1Si4MTaxpSfLHbfyeNLQI-G2JmCTwLhqgqsRa5-7EmAvBf6iOqdFsGmqqt5xWFv12o80Ydrwzncx_EtOnTudO3dpvyPOYe3LqCQ3xro0Xt-skQT7bdDUFWJ7Ru9KWjSoVpGd4IFoESC9-Rc4vYuEdQnbS51eTMlidt6jXZ9tAQwsdcdr_4Sc8465N62dG-oiiDaIWoryHtB4hiYDDKPcyf_APV1vMGRQ_JXtwYDhhbZqlVRtvFrspOy7eYekZWYtqxz0f9wKyvi6e3WoafSkYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30830" target="_blank">📅 09:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30829">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtt1lkELwChJkVqZQwmEg-PqjFw6nJu-VXuS36RBk2mlCmod-FQlnuWHdmDxChVuzW_SH7YYJIFQO6HTZv37yPYLKobekvj7ipxjUn1FLTziGvs_lvzk-SexBpXylVVLndmaKcosqx4GaYyP0yfGQR_EF4V7C-uOqCQirdzPKTw9h1ds4dxBjFzLiaQSw8T7-vkRfgXbcoCgEPyGEautja0IWTyPIjY0a3h1zzRWdz02Hjvq4w3DigPgm3op8mJ3O51eDSam-36DCyCnktmxcMqCyN9YVjHWaL16cJXPfgqh7FYrAczbL2-C9tGi4aay3sMZsh9leIHWZ7ASIWlR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30829" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET6fhduQtRK5mKIKuQJ9GT7SrvZJtzhE5avET3g2vW6m1EVXlj526q8f4BlOI8rbNUMJjGRUdP1RTx3bgKPV6ET__NOgdd6lUXUqaLdEv8lI2A2CE7hXxZkTDcpoOSpgOgUZGEhO0_mJ9sEsDxH4l7dNLOn-grXrK_UB84ARewjqldoc8f50KH7OBFX0eBo5IyEBdsh-1kBDK2zX8xeNFVhwMaO9MQGYYq1BAOtTT0c7ZmfgkdpgE6X8jWofVk5k0cCQqiBHUa91QqdZVrhI1-NUoAuIeczMU2S6xyykiz_oUVUIDG0H91INlllnZOxi-demAuXV4l9z9wf3japVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/30827" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klRY3c7sbC1jtAkZycEz6Pj1KwvrN9yNFg806nbqABILt0ZP8HSx5lXtj1kAZap__Wzc481Sgl5BVAnzsjEi8N6vp1U4my1rCJ8jJNCIemYz9gv4CxPdWqs1sJeHJNIhvkq8L7RmfGKQZn2PMhgm3T2azN4PfS_WpGp1a7FkaEJE3uYFrTBkVo1FLqs4qVdk7S5NDHfdw6kqApL1cl5QLTBAklUn7ay48UpHFExxbsh3c_Tm1tVJWvhRfRYjlQrHyCGUn1SUx_tQK43XE3PqLYIvnrpf3lTdGDaehJxbx90HU1nRg7qCpNsV2-ljF8_aIGE4-_ZWvrDeYBrRDbsxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
از اولین طعم برد ژرمن‌ها باکلوپ تا سومین برد پیاپی شاگردان ژرژ ژسوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30826" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLWQf2haCjPeCnBlJK5e3Djw6mlmC3ix9ucvrfVdoFBbltNFMKQRomSKf_oGNPD9NhAx5y1qNe2-38CPdh1RvX91RBCY1m8CVhjKAHBz2o38DkrKrvi3zyDDWC049jzm5JvYtrPePpK7XfUDweTj8ng_SQpdF95Clegp_SE5Rcu1SNw1SRlJWZCYHaPi9_9N9x9P1wZbFqv-HLSm5ydjr5kNDOQ_T41Ooo_YNvzxJ-dpncKgpdTR5TRwcMuNdXk3kQZTlOB60KTd2BE6MVX5nyWMnEu-8vTm2GSLtqQ1RJp8_r_u58uxumW4iWn3VvCc5BVvEjiCBtGSarKm3s6Z8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رکورداران بیشترین تعداد گل زده در بازی‌ های ملی؛ کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30824" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3EsEE9456-tWhdkDps5f-9DbrZ39osNHKv9NzqNcCcG6YlwL1O8GPtIYaFmi7uc5ZWr2rl3PmBo-Aye0CULRC5MUB9_-CSP_Q-b6nHZEb2k4253SjPctxgZ-iRJh6S8Y1Tx7bgG7UDrhtuLQdjoCoj2zY8JEW_ZNwW7P0uHpfNeQGf_tuBys86ft0nbAWVTVC9IBF7tV_NzpSUZpOuVkvbDmUNdowolWQiYrF-wasG9guVm4S24JEj_3lHMZdsvuejoaLZ4r2AjcA3ErVzgt2_opWAaKxprYaSt8q-lvjpe8uq4r1wRD-IFfFiZ7V1Ae4I7MjYOvwMHSp-VbEcnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ابوالفضل رزاق‌پور و یوسف مزرعه دو ستاره 29 و 21 ساله تیم فولاد خوزستان به احتمال قریب به یقین در پنجره نیم‌فصل به ترتیب راهی دو باشگاه پرسپولیس و استقلال خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30823" target="_blank">📅 00:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlI6XnK024DUhHVSa51Dac6R_Kcy8EVOfRq7-jP79HnQUeDDTd2LxPpzkSuZM0sPJwiJ93xNX_lCb6hkEdi0U3n-HllyJhxTd8xP1coNxbDODoqULyBCGUrHR7iWq4n61-yyocbiqmJ9SFWMd85DwGlUnqdrMRNkmdpQ5STo10K6_scro2xtGY3S9fMHW3YHrMdaJ3HskTj9tPvi99tU4_KqtpKwEoWDgg3XWDlPfZFqzxYadlDpeCoUHrwYsOZkqmrXe_dwaYyEcLCObMRh_Wlz5J1qrHXzeNG8M5XCxv2kjC3MsnleY7X-ykPag3SpgfuW_jwkECqOeFNg5s0Jgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ برخلاف پیش فصل؛ حمید مطهری موافقتش رابافروش‌ابوالفضل رزاق پور به پرسپولیس در نیم‌فصل بادریافت 150 میلیارد تومان به مدیریت فولاد اعلام کرده. بدین ترتیب با پرداخت این رقم از سوی بانک شهر رزاق پور پرسپولیسی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30822" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGodLUC3McCYR23vjZKCHvMKZPF6QBkDvGdiFq6U6UNXVJRiIyctk7hQ80WjYu3PMFuE_LIorQGEhsYKd0FDKKK5yXqm4F9QPIWs9Glh5owp0aNxlQj-q4bUvrweLXHbothDMGPoGGwiwQfETGmp_9ASA5w-aECrcnqFdRm11JrbNDE1o9sxemOvk5Itt_czfQWKMTKJsA70dr6I4jvrL3ayLYxEqa4Z5E29_xmXuNyKU1ZWJ_VtKr77E_iihkDnloBBykLRr6fFFySr-MYPjU06AZ5az0yvNI_sEyFrJOShSVFKrHzKe2EVCbANVuUhhsTI0eHLkovasoWOKM16Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30821" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebSKE-oe2XmVGxYxMyZjE0u0QZNHzeEi0EQ6zQ2QFEtWyghJezdtL9nGy3Cun-ilFErPj6L3CNZy01dVNslUe2NoWq4Gvg7O1o9_Mc6Wytb_z-xB7SXImXyCnU3rq4jF0cyIZLU5It3j0QHEo1jta3X33dL2n8auPnvzB39jYaE6p-AoN3ENSJJGVmX8LOU-0AGmuvcxygYpJzcSsdsKd3bI5AF6vttA6y0OVYjNJAsz8lSk6VjCqZenP4R8zYuyiW6WD83P8F43wWgx5z5ZbsNm6RNwelIbSDl9BDaDM2SHMeXJuxx0g2pdk-LtIP3NZxDjcRk_HSskV0M0catpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛طبق‌اخبار دریافتی پرشیانا؛ باشگاه استاندارد لیژ و دنیس اکرت برای جدایی توافقی در ژانویه به توافق‌رسیده‌اند و این بازیکن درنیم‌فصل به احتمال‌فراوان بعنوان بازیکن آزاد به لیگ برتر خواهد آمد. استقلال مقصد احتمالی این بازیکن خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30820" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AObuhapV3ygnB3xGKUVLpCTDBUhbnR562s__f8bWODJ5cC8X5RoJHxoXlL-RsgyX9P4tj-Lyu-WEpi_7SwZp-3wjPALJqGGVuvozLKtdNnmuMnxhFjD3eCtBmi8lgs3VqqLZYO95p3y57aH-PVucVDjXCCQCUNQNusd7nXPC0XOAvsi4crEMmIIoeVr9Kp9HNdAKiv3Iv8Vlfn4AO2g-wJExzf2d5aWi7wP2FJDhfJSvugXjwezWZ1JZfyKeTz7h6iv9T904G5DF8DxDWa_4LFoPixTuYsYKZmurx3iv0bzTOoxYR4bRyEeoc6KHKjufYHh5V8HAsGcYLpABBaPeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30819" target="_blank">📅 22:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30818">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeXlDUIrJgnajWB-Z8tMJkPkMXAL2Q2zDC7malgrFto_NTSPqAPFjsgLTeohET3PKiF6xgqI_ta_OPYVHhQEPdOGpOBBOcMhqHKym5q6KI1KIHkwfkitD1Q4S5kyUhgiwF6SUAxiEei19WeZalmzd9TyRAyv4JS5BZ1Hf4d2_EyO2_fBpJrZUptdJOHm3O_Fw2d58DiHGWXcs7bjvjkwZV89K0E8a4ulrAkmatBqoBN9WlfFj5DuQojdeqVDMx-Xx0EuXVIAReLIpDK7r-9cGfAn_Q3vK4mfdkHfD2malpCbjyHUSZjmD1rpiO4wFHCnAIviibVHjhuFAEuXsMeyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک 146 گل کریس رونالدو در بازی‌های ملی برای تیم‌ ملی پرتغال به همراه تیم‌های ملی که بیشترین‌تعدادگل‌رو ازCR7دریافت کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30818" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30817">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkbfUzJRMLS2bNFBE8Iaf1IxWHh22S_q0NJrUAEjXtgbakqDv6_VwoduuoXS3cgVg0aeFFpg_1prWNJm9NRV2jsuKm2c1QR1j2XNkdQEp5zW1BanTCgEEXnGb6ZDlGEtM-se5ObDVjIVEXU38-zKgAFv-OPc9BsklAKkydhDNnwy2-vzRyEotKkOIvQL9yPE7fakqMlu8SKhEJ8t-JWmrtL8KfK0F8hnSk9PKva_ekKM6Np1cqooAlRxZPrwfYMSeMUFrExXuvsdQR1PFpG-Npb9iEiB1b1eTJQvMkpPmOk5zDhC194j40PBHiBRmziNlrfoF3RAEEVaKC9K0hcz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30817" target="_blank">📅 22:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30816">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QteGbH9uepvdh_cthD7VnVztKXwvOEW1ixn41wE_ryAy4zsvAp5MyinL_qwWyRjw-NEEPLOh2voXhiyKujVz9jbcPkoSzcAwm5c7WhcxjJ8z6TDARUwspU1ewV8NF6vvGvtceWTD_0xd3CGXjlOlh339ubbev2KDWGSttIiALiUc2-Mt2E0WhuoKOcgd86vI7paef61OHWGxsRZdgiE8YfKdeYc_BWbSPbsvyFtqjJZ7XBJP3oHjaya2URU-z0TGb5fLp_7j9BrMIPWbcll9MvDVo5i791ZKm2_4peTWT73-jH0LkjNWb8qiMNCsQNXpEXBiV-lT2_7m3YNwoBPd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30816" target="_blank">📅 21:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30815">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sovWixqhtpnDZ72Sl-Y3tlfo6X3Hyd1pNBpwpCI6i46_U43YmoWG0NwZb6tH7um8mc3jXSDTWpPOM3AcnqXpCj-T_-bI1qnPzH6yjj8-OYias8lIiISIZnUsP54Zi-F2hHoQ_6Egc4DKocgTzct67Wh9kKVpICDEdpdJ0451Bvl49Mleb57z3XCU6_ILXIc2dI2ID6IxMECSsQKJFrLNdIKxb-SPUysUUdaKki7bW-_Ygekkh5dbXbYWM98zrc8i-jvBxwnyvEqlmIRLFsUwj4Fo370KLJ1vP3WZQC0Nfz-6eS5LGAoAS_V-naBi45P2fJrtk6yL6ZVqRjLoyXE-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
در فاصله 48 ساعت بعد از خرید سهام باشگاه آلمریا اسپانیا توسط رونالدو تعداد فالورهای باشگاه رشد چشمگیری داشته و از 500K به 3M رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30815" target="_blank">📅 21:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30814">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBH33yUMLrxkgNHUhZdZl_7b9W81BgZ6SIlstUziR84WBeFmu0aZBCmMUtv41BoSeLkrbh8pdeogIBt-6XaZWERJUcdIIv0YTi9g-zy9enUM4msCRhjKTSlbTy4RaUNUKuNNtTzr0nXWcFuPHZrs7OWFyakpo-NEGC8zu3eFTyaAuw8dORtpjAO5YawbOMyYTA85lIllQpawe806tOXZ37XyyBwedk39a6sfXlMbE2sm-lbMN2l-IGYmGORKiFhG_8Od3MtnhB2qUXGbrzg6JHYU-QA3VOfoFrmLwF7SQFaQZtvd5QHRonpw7zoA8K_m279yW1zgoAJSmGvG0Xd-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولیویه ژیرو:
روزی‌که من به میلان رسیدم زلاتان اومد پیشم و باهام‌دست و داد انتظار داشتم خوشامد بگه ولی نخستین‌جمله‌‌ای که گفت: خوشحالم اینجایی ولی شهر میلان یه پادشاه داره اونم منم فهمیدی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30814" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93919f9336.mp4?token=L3ddlJM_jdZDO8NvMzsvpSFlO1BIhbH2pnOeDeMIeCKp8WpymCOr9IuXQURws_aU9BFsm3rSx9Hc4HN9mqqOohIBHZqsYzQnNR0-2ZQm9GVD1WdOPZTYc7ePMy-vtdHykE2i8lgOrjoAz3btttXdLs9Ka_WPVef-1C2GMujz0Gq58DVtSqN7Jwu2957nf89zM8z0bnUDN0AxlYJGNozpk0jecN1d9sIE31A8Wzq32GHGWXYy_D6w54TT_66UP0ihTOTs2Lyq1rDwVRQ-cml6Uo4IXIf3qTL-wQvy56m-WUmWnJz7GxjRfxCHdeTUJUyQjCWEIzaiNb5P6bOpkPqYyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93919f9336.mp4?token=L3ddlJM_jdZDO8NvMzsvpSFlO1BIhbH2pnOeDeMIeCKp8WpymCOr9IuXQURws_aU9BFsm3rSx9Hc4HN9mqqOohIBHZqsYzQnNR0-2ZQm9GVD1WdOPZTYc7ePMy-vtdHykE2i8lgOrjoAz3btttXdLs9Ka_WPVef-1C2GMujz0Gq58DVtSqN7Jwu2957nf89zM8z0bnUDN0AxlYJGNozpk0jecN1d9sIE31A8Wzq32GHGWXYy_D6w54TT_66UP0ihTOTs2Lyq1rDwVRQ-cml6Uo4IXIf3qTL-wQvy56m-WUmWnJz7GxjRfxCHdeTUJUyQjCWEIzaiNb5P6bOpkPqYyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌پسره‌امیرمحمد‌خواننده سنی نردن گوردوم رو بردن تلویزیون ترکیه تااینجااوکی. بهش میگن بخونه، اینم میخونه. اول همه تشویقش میکنن ولی آخرش بهش میخندن. پسر متوقف شو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30813" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObJozVlV9V58jCe146o51sh5-hXcGDBvngcPlm-3f_KmmFMkxbwzH9LSe-4Tf_PZT20QXMPD8wnFIIKaX16u7kpELOIrvWFtDCSFoAjE98xLC30DOUBfZfZZJ3HI5WMwtdgyhx8Tzv9C_gEnV_2Cr-nCgt-4uhMq9F3L5ziCRmHCN2gWUku_SzLiYmpY51iuovlB9xSt5-qvlyCTf0F5fbdr2e9TA2pcU-LYltm_AyvJ0AI7s4NQ6OWExLo7OxNN2oREV4gIxji-25-Ib96SOw8NGM9PLuqNiQLOevv5HfYdS-Xd6ZIizu8aEcOx-rlnF_luTNcZDWMLgcRnEHT6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQrIaJxakD0-yggQkwrV6R2cPdcbzy8y2_niJ70PCSVMfpXyRNc1eMOr9rB_ZO6wkr1P3BLAM55potxf__b0o_39yNOoa7Z0__rgiFDrmsjYqraWF4QlRh1lW1aMMdSRh2RMlmmPbTqwlWx0VF08uMqiPQ9XfGL3Drj1D7NWzp662L65ulReS1GB2IhM5z-DAyPYUo5PUsrRCEmPPpGsh0z9qVZwJbzujg8Oz-bf7EQXA9OBbgmOaTfHRCO3IsyjpKhficEIR50Hb2RwIk_H2nK1PBxSdAGyo-H7ZNKqTopBJ2BQjv9CTgTd2fcqKkim_sfHhg5MzNpHRM-zQjTNzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30811" target="_blank">📅 20:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBs72k7HhL2-igDPN_5sZZksN3thnHyLTPP00dzBir32S6IiM6SD7ldc110Ro5e8La2y4hdhQYPSdt1mZlAJ0o9sptT7UFDrOw9T6LynqiWg5FiXbpp_YAWBRilqBKzbY9LrZOFLhSvhmjGUz0scjw-NoGffZLlXiemICPbEwngXAJ9e8SRDSr9lpqnZJw1rhHAOV_xFOc8D3OvXi7XHnVTQWnCsmTpEUH2-yunfERN-4kOKqs6A6Pp9DU7HDBwR9RB854uOCCLQbzH0O6nfw-4_rUjeGHDZn2qUazg2VXXe86RAC0LKwLY0aK4X-byBRIoQMUX7-cT04rjWr3J5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال ستاره 19 ساله تیم ملی اسپانیا که شب‌گذشته‌نمایش‌درخشانی مقابل انگلیس بعنوان بهترین‌بازیکن‌هفته‌اول لیگ‌ملت‌های‌اروپا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30810" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr6-kJE35crdBWQcPyHHD_BlRioAhv49HsXK6zQhlKDrxzzi6W3xKu72Ll4qswd7OsTXXqnHbc8aF7DqCRNzR-cbeqQ878pEyxcBLfgweVKMO1oWE6qDH6cY3x3Ma03DObp6ikUhJrHHb4uRfj_boZY5qpWcTDMsjMvkdrUd2OwR1W7qbe7rO11UI9TJt8paFxeaeBpxEYK5-GktE3fx13ZDwPFd8CWq46_LTZZU0zBmuu9ImmJoL3BHMqZFfK03D7lRC_qbGpmQW8ADLgBQ2euxtY8xhaYMMRTU17SebZ7ekwfYVc5Cbt8rvFOuB_D5ebKnNvOwKeS0qlYML32qkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نگاهی به‌شماره هفت‌های تیم ملی پرتغال از سال 2002 تاکنون؛ رافائل لیائو وارث جدید شماره CR7.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30809" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrfWT6q4gMZmWfd9PNH0namOHH5u4pHFziixR7iCsqz43bTm-HtKc88zcSo3dwZc-nlzWIDlG155obPF7hjDw8UsTYl4Ardq1TxkCoBoj5wqGKO-k_PaJPFSc3Z7J4hQNWGM3_OR_8fDFJuk5ArlAw7bc6u1eReXW77EAwKedW9NgA02mye0I8FnMZcETbGEn9MbZhwrhZt-suwUVTMna9GlcZ0l8y_Lr_XqzDCvTo8AFQeC3Ch9Dzg0eL579M2JePMe-qaUSogn5-OmLQgOzhAzZmshKqQCNK1upqlMjg0Q_ES4Ek4MuePhZ3zFAWl8MO9GA2UKD7sSOabginSGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30808" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30807">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8H0QSJFeyGhJP2OFQWlgJtKzBmaHsbqHh0V5XRv4SHf5hKiBigbmkF0Aw_IQteC4v7hhOoSVp5Wtp2zBztDYsvsrvCw6t6ZIjVPDFOdgP3oPaNsU_uvJCFo3MXWiIyHJ5yvep_IwDSzj3emy1zTuS3zSZExpoYvsIQ550aD4xdbJqFpZ8mOqF-ngDvGbtlzYBYuYAkA28iQTIJc2-0JRaIlkhza-SK3SSMK2EyOWfJ6Bb2FyS48winL90B2AByNvIJeKubm9o5Yg_Sbb4Flxrbfn5weSwtG04GloeMpt5TVhes_1sFMw1TXEiPIGGvFNz1H7Br34O0x_kOTtYz2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
نقره‌سنگ‌‌نوردی‌ناگویا بر گردن رضا علیپور؛ رضا علیپور در فینال فوق العاده حساس سنگ‌ نوردی بازی‌ های آسیایی ۲۰۲۶ آیچی-ناگویا با ثبت زمان ۵.۳۶ به مدال نقره بازی‌های آسیایی ناگویا دست یافت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30807" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30806">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhVwZ7mGAZnMqD9SQOawjES8hevx4IbHJID4X_wqtlRT-BLZeJLJL2vAPQsYrg9IRggACarKgUstxdAqCujkY_Hym6Q_X32H-EU0ksiNIdzH7rzB7JYlW5YmmP0PnoEmYGHxS5gcdcvycQ1QyjcNTyuktvmuNjpC9dwQ-a8OiBMwK6VVefGcRwIYDPK2NFr3fBFFpO4cepr06W6yllHgiBIaRmrhBUqba_WqzanuBQuKhH-I6FSElCbE0hLPI0D25HsJse84aWibKev-90NjtF5Mc-e8GcCayLeBPLw8Usgeve53XCp9yEyN8OTWcN59Z-n-lOiydmGLHpsbcaaNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فران‌‌تورس‌‌ستاره26سالهPSG
: باخدافظی مسی و رونالدو خیلی ناراحت شدم، ولی طرفدارای فوتبال باید با خداحافظی بزرگان فوتبال کنار بیان چون یه روزی هم قراره من از دنیای فوتبال خدافظی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30806" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vl7UwhNYPIL5ELQhZZnqd3DpOw49vwI6b-I0ZPqcr8RC6yenxz5hy1rC67CLtPP146fYxIZ6gtPK5bKQi5CBPzmo6D4eZTjXdFACSFoXzi5hKCh-aeHbGbcv7WRhT3QY4Um3MEM6lGq5ID3gE3Vhg2u-bo3Edl0pTHKeKVJk_g6VQ2yJRlKZlJ-ACDVaNQCpb6fkP3ff3po6xOKolhGTpcHA1Wt6Y9S262AC0K98zu47rikOsHicHMUeFgwxmx07N2_KWlM8znmDq2hoHxqftj9RBHI5Xr8Ill9PG2bzkvGK0bRkA__dydo-OSbLtGbMVCrU2G6NJ4d8U7gAA2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30805" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjOlE4gYaUSr2qv7-x_ou15tabRasFtvHDrW-X5Phjwih4Ol-DGyGBwbOBTxa4Q_hSDAwBozEcao_to6O7ggWRhTVWXPd6bpglsH_NGmeNkwcog0uHh3ozzAvSeY1g3Z2Je0q_KA_mk0MroaUYR0X52xRMkijz-rC78E9nZW8GG_ESEapvs3ZJcNY5Oi8v75P5_Sc1lI6VZcOvgbsrqmLmW10VoGSkzJGClCOUiywg0FNuYkOlkYu7H08XYhJogCeQQLB_GN2cO-R7HLPXbtGtbXGilNj_7nO_hnkUFFx8_QGHnTAKVOiy_BI_3zNCXiie1JkUcA5KAojE_3pvD67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30804" target="_blank">📅 18:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt9hyhDSBGdcpAM6wzZjD4Cbv_pPteCTWSoN8PA1jbfr0KWlArs7R9J4z6y4hgVX1D9uT05byhmR6xHob1hhafGLdEYxl0Ca5TFi1nstDPKYzquKnzRX31TvfteNuL6bQxenj1C85bY5LQ1f15QTo495FsvSF480-Arr6uNzZn_-D9ZYGB5ZNBStVB7x1v5xGycXTu9KlAyjBF74SoDiaKZNWiEatOgzHngNLQUjTkR5cOIDl-PjAt_JlVgNdhqd2MnRL6Fj-Fu-56GWgN8E8KNp8uQXPX7BZi4LizKqGBc8HOtjiB8yLTr0HV1-CB9HoQhwMOOFDR9kZDFO-1R7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30803" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCXPvjI76dtGlwIhkDbbQ_x7CsFUtycP7C7UXsW4-8g5Wk9BAXB-2Ql8bpHO4GSJ7upNHXe6ZwJ7nhxFoyE6LZfxVwdD8FNoYrHOAJlnh22Bk2C12kcE5SOpR9MW33USZ-Eq4pZpcnLrKJExWyLVne8BUhIAgww0-YhwkvFxJ2-kOawrkBGh8zZ5TH5LMlnEWJmP1YAPE6hk8QNzAxzQbf2YZ0xkpMvxQPGDk0COMnqsQx38INGPz6V87sPcCBRT_EgnjXU6IWnxfNQGdXQjfqY9XH4_kLWUR_RLgP61c2qZJxFpS_1VLqJifYOdZsAq5J0TdRrjG9LW3qnx41vDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30802" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇵🇹
🇵🇹
نایب رئیس فدراسیون پرتغال اعلام کرد که کریس رونالدو دیگر به تیم ملی باز نخواهد گشت‌. رونالدو بعد از جام جهانی میخواست از دنیای بازی‌های ملی خدافظی کنه اما فدراسیون بخاطر قرارداد تپل‌های اسپانسرها از او خواست که تا رقابت‌های یورو 2028 در تیم ملی بمونه.…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30801" target="_blank">📅 17:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZPDnZz4cRAVjWQ1UN2q__pIXFnoC-I1lyVcnQGIKMWzDpE1IhaSPEnTdGyjaeiEGJwA4Uev5Ha753fQq6O1TIwprEL37gRBybGuD8LCQ8eAhyuFw_UYCJOxMnE6PFxdlqXllliSM-fFXisMDm7nVK00A0sH_iN-EiVD3dt8s_h0LR-2ZHSjUwGE0eRbEjSUfB4e6UWSRVeL6A8p5liA-vSOV-beI0IeTKzAF6YGfjmysspgPpmMghE4ZNECkYdvKIK1JEKj321pM6ysuNEKi4ObO1j0XxySOwigfpNraxHpPo-Onj4kgXr_CytDtqA4YeN5ncaAX9MYsLKTUm5XNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی بعد از آهنگ خوندن برای کودکان میناب و مصاحبه‌زنش‌بامجید واشقانی رسما به ایران برگشت. جالبه چندروزپیش که خبرش رو کار کردیم تکذیب کرد گفت برنامه‌ای برای بازگشت ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30800" target="_blank">📅 17:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPkLhi6gyiQ6zFErEpl-1PseU2g7g3rBVecCVKDCqFC_6pTFOuWkGupSM7ZRD3ugeHRxcgO3rC9NYIMyJFfNudENze0L2qPpOReDoOehtgFqYzG2O6KZFrSKWQsit-ifvZZeppILZ7xYiQuLKn8cxSnm7yI9o5ifKiUf19HWWJGAYaxlohFt4AjfI0_RiAw8Qm3jikkp2MB1Utl0MklUDacc3_YNHNSmSDHOSg4PIx1py1aVEi6NP4cEbxNUwY8r4NwcEMtf1Yy6wt0XcWXit9bbQogWLeeB37xKntQk9JBs61lndZn1GNWNrcTGMTbIEKRWdMIr6hX61dFSybaRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30799" target="_blank">📅 17:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANEpAAjhp-9TxRYtkoKi3qPwk-C92wD2Cx08zv7_J-Q802-i02p3OYOGcgGtK_x1Yjo41WxpZWCJhgNVrCMwxo0uuQqirPn90vF1NCwMR6FtH_AEBD63swHZVvp1wTIfFtTy2t-JS5Wg49eyTtt6Ntf-HRAeYnEBVE7aZT-0lU7aS_IZiDS22zADjT50o_r_54tLGL70_IeFv5906L2BXJlhew3cAGNPUfMsrBvFJHf6rvi5xpIbxPaLuX3Z_5Puk2PucBO5P3u2g92b-tx4_EspX6MwAi8fDJoHzuP0a-gr_uYgX4grJzb-C25vBmYGbaSiei1dHf5W281iCcp7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=KhZzb17-Af6yi1KSzaISJirC9MsFrLb2_0mV5t0ZQKd_TUVddpYbvQCgMPJIDLu7bv_CzG4Cus9xMqyoeZiQDl__yIIMXKh9F1MDwTqdMm25T99RzFcMB7YbI_AnIykUtBySCMnZriUJQA8f2_w03fLqhrzgIvg2Pc377xGCN6hydUxCLjvCoFzr5cKyJF9ZCMfivbBVOrBfZ8U4jYATePcsdk9h3EICJau7kjfyoObimW7W3nBJ07aIxkn-8Mwk7_GVwvIrlnfk0HIyWsM9eOGpvfZUlN-woyRkAO04kFsUOt4sh0XKwJXOt8gWHwa3W0E31WbmQ55zUrNSzHm-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=KhZzb17-Af6yi1KSzaISJirC9MsFrLb2_0mV5t0ZQKd_TUVddpYbvQCgMPJIDLu7bv_CzG4Cus9xMqyoeZiQDl__yIIMXKh9F1MDwTqdMm25T99RzFcMB7YbI_AnIykUtBySCMnZriUJQA8f2_w03fLqhrzgIvg2Pc377xGCN6hydUxCLjvCoFzr5cKyJF9ZCMfivbBVOrBfZ8U4jYATePcsdk9h3EICJau7kjfyoObimW7W3nBJ07aIxkn-8Mwk7_GVwvIrlnfk0HIyWsM9eOGpvfZUlN-woyRkAO04kFsUOt4sh0XKwJXOt8gWHwa3W0E31WbmQ55zUrNSzHm-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30797" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEnQScbtPsWzDx_mYs5--3j4OUAncohK6wrLpLLnkbZMjXZK9iehXHelQiziZ137IjafCnEc-oC_EqhmYrtavIMNP3eiGaWitOJbTTO445qHMHKwOjr_It_W-XhFahXbJcGEZzV3r6N9SRy52P4kjpIJMFJOeeZDBeJR5156s-C7NgmNKvXpkLTTqPwu_zgTaFDodalF2dMxFmAyjvudZVxvj7Km2CyVOf5ByrgZSZKaA1kWn4Fi34NSv78Vq9P-m6MPf_hRkCAGxqS35J3dXW9RC7NhQsA9y-_37SGv4cPzfUOS-Gw1bPBI-Rk8XYPx4CQRCxsTqXthUxn-KTkeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30796" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkK-QH5fPNF6sG-oEm51d5gukfw3zbbuVOb3StEps7mxtMVq7C1oXzv7FYT09Q0B6hxGJvaPQBzV35kErkK1slSfmlGEMX5aPfGJJB8-6xcO6jhbxe_ueiPpWHOZbXtMb0rqvzgXiLiQtyef7zIiYNSjx_JT6QBYlACLoHsgFlIP6UkOX-13azjrldzsFTb8vb4AdPDYaCJBjUqSs29prWUlNby9vomHFKQQZ-CAbRJQP0w6LtgDniFl-q_9U3gcySyyw7lUg3UVVzTKAhOzLPck_P7HxKIb70tUEZL_KpHPlbfoy2NmoaSgfQAxUN5-K7gyMlWakMgz4KGIUfcw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30795" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz8oLqjtc3juIZq_Dqy_8M2nIVq84Q_87ExRWWVIe-aT1xrcJcyK4li8iFypGoAnopywXDB7N6WgYmqq8yOPzv9PL6Xt4q-4X9OZQiGb6xzA-HYDH5jRnj_xGhp_qVUHUYRpOxSQ7hTl_2WWnlVHZcjv_DWSUa_LAJ9rLkyN9W77bpRqqxHyZ4kFq5wTGf-AfPIv_5bchwCknySHhg_7-BBj2qS41SEG5iMITV60TujkzbB2OWMZ6M3AspJgOecqVH84nXIkH4p3c2kn-DnUN2RlyV8tgTv2iOYoj7wHYvd9EWJoteWmPmUBXjHba_VZTXdENmkW-3Vs-h3kbiOwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال‌پرتغال؛ بعد از 20 سال که شماره هفت این تیم برتن کریس رونالدو اسطوره تاریخ‌فوتبال‌بود به رافائل لیائو وینگر این تیم رسید. خیلی خیلی بی معرفتی شد در حق کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30794" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=OPzY_YH0u9fPtgv1YGGL_Nups_jfJPc-uGxTeGg4KmsOkclXtN_GLkzNPAWxsXCoNFfHpErmWloGlcVWeYafd8lVsYArlg-kFEBibZAHhgb1PHZaSd_arooOj1hHCR2Qkk02lXZ-CXu_E0A22BWPTvS3On3CaxzX7tV7WkcW7fmJXIFOce0gpw0K_S7ChikUo4QeDFwuGZU29pDLok3szKJARx_GLkuKithz3TG5ubw3VQDawj4M8uhgYwrwvfvnkDBgQ2QePy_ItliF7bkSMQ2nFqPwUEpNKA_glVlO0ZnFTa4H_LiDg19OgSHf7x_pZ1MWwMe2cbZV3eDXG6THKL6JqdBViUliUwBYcMEqhpdmjMmmk1Z1iHo23RfMszil2wSv9h5NpyPcN6RTyzYifZesw-1mQSJMdxfFCP3J_WTOmf6aahkvQrNSyyjacL62F-0zKTENKA4_wLuxQnUxk-Fz6gxUEyeTOMcduDwaNobvvJ-En5TvTca_E7CP75d-SuUd_cw9qF8WRQ51Wx7ANOGrF1qJV7XSnNrUa_6a3mV6iSdu2vA2yxhPGZPtOPG70AnkewMfB-94_TNioEsKqQN8MDyDtEXjR_KtEASdznFKkyXhXZwL029uBeZOtXPVnMuclG8u9qGKLHKFCH7OwM3qpaVpQFM86rZB9zIHE7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=OPzY_YH0u9fPtgv1YGGL_Nups_jfJPc-uGxTeGg4KmsOkclXtN_GLkzNPAWxsXCoNFfHpErmWloGlcVWeYafd8lVsYArlg-kFEBibZAHhgb1PHZaSd_arooOj1hHCR2Qkk02lXZ-CXu_E0A22BWPTvS3On3CaxzX7tV7WkcW7fmJXIFOce0gpw0K_S7ChikUo4QeDFwuGZU29pDLok3szKJARx_GLkuKithz3TG5ubw3VQDawj4M8uhgYwrwvfvnkDBgQ2QePy_ItliF7bkSMQ2nFqPwUEpNKA_glVlO0ZnFTa4H_LiDg19OgSHf7x_pZ1MWwMe2cbZV3eDXG6THKL6JqdBViUliUwBYcMEqhpdmjMmmk1Z1iHo23RfMszil2wSv9h5NpyPcN6RTyzYifZesw-1mQSJMdxfFCP3J_WTOmf6aahkvQrNSyyjacL62F-0zKTENKA4_wLuxQnUxk-Fz6gxUEyeTOMcduDwaNobvvJ-En5TvTca_E7CP75d-SuUd_cw9qF8WRQ51Wx7ANOGrF1qJV7XSnNrUa_6a3mV6iSdu2vA2yxhPGZPtOPG70AnkewMfB-94_TNioEsKqQN8MDyDtEXjR_KtEASdznFKkyXhXZwL029uBeZOtXPVnMuclG8u9qGKLHKFCH7OwM3qpaVpQFM86rZB9zIHE7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری معنادار رضا علیپور اسطوره سنگ نوردی ایران: باخودم بستم که. گفتم رضا: ساطور میکشم اون شکمت رو که اگه بخواد کباب مالیدن بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30793" target="_blank">📅 15:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1wArU7-VzMiukRDPVNUgwFvqe7gtzDryEu6fY4FcP4VaafsoI3DOVCMgEHJzalmhcqYQa50DTuN6TbtZrCUBGWfzHFxjh46S-m06Ft78Q7u9VqGtmGeDqrTj0FdjW5Bd3DVWY6bvTX14eAzWYiEW71KsQu8QwgHIcP7Pbdg6OPy9mqUgIrC2Q3Iyp2efegj0VtnCR2e2ipTz6iN9UZrn-p8xDIIqEgSvm0LbFyb6_vDB8e5DBBplhPqKeKR57k7ZeiFA2O2EDtD-Shineem4vco6oV5ZFPyqj4ppvu5rIQ2plCTJIOLUk6GIekfkRXzfyTR2sBZz7t7VEnibOFfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
با خدافظی غریبانه و تلخ کریس رونالدو از تیم ملی پرتغال؛ بلافاصله کادر فنی این تیم شماره 7 پرتغالی هارو به رافائل لیائو ستاره گالاتاسرای دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30792" target="_blank">📅 14:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30791">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SR56UWn5JK2k8O4WGbUvFb7GvGB8r-J2T5aIWShsACTVabbWcqP1l5Xp0T0fEIwYcIOdT7pERo1vMa3THwnr886FPMGvSzYLPMiihTmcl9hGEVFzyABNNSNCt8gXa497RB5swIGNs8uM5rV1o16oh_xb0vhmmhSRx-xotodfy552g1xqhAfs50HDVV5idSl39w1CbsCOqZbVWoHNQ1oij5GTiJWe97NNESJp2cukUOOnV17JMZ-yDY0MTTESUClbSeaGpz3qZVBwGEa1OiMGBAQvwZ-Uas_6SLR5y9Zyz-qo6-WEHQFRtRCbXL4C9vVb5vfdcdKryollPJlsi6hXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام باشگاه رئال مادرید؛ امباپه تنها دو هفته دور از میادین خواهدبود و بااتمام فیفادی به تمرینات شاگردان مورینیو اضافه خواهد شد. بدین ترتیب این فوق ستاره فرانسوی مشکلی برای دیدار حساس روز سوم آبان با بارسلونا در الکلاسیکو نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30791" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30790">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMlYpH2tk264miuE4R2dsoeGTvXVU6n6bahjYOCFIDwrhld-PgnDSZkmbFXXRu3_nuu5vyqk5QtZei7YQEyxeBy3wotA04LdLSM82vnEuoce6hfOs6PJ_YzmKiF_6fpg3W1YelZKC3ZNQ9Q7klTSZcsPJT35LdoJ2AgVRvvbvQ1Z-e-iSTgF-Kik3zXq9gaNi3LIfE1jT0TgM8nViigufxyFOgf6HmJ8KL1_jXWxsxwk28DtBqZ7MZtcvE0_httsr9TM_gx_XHfI1rtSx5__wXAbwKustGzb5ILttE_r4DTSgnoXabN8z_nGWpNN4ecZI0cDelC-wM-IHXtlJ5q6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30790" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30789">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKPoSAXZVH9pEGdFhCLkG_wPA3tMT7dwFY83I3-XsDgXRzPiWVUtt5X01NABQ2Lu4YCh4RjZ0DAxHOD0BLAVcuy_e-Vvsepk6SJHE8R4spjjNIJHA9rKpbdfojc-oNCMKwDBOFzYcZZ_cJj-FmCjljvxCEMaX-BS2_G9CMCFA5vJyDNekdRFoIVSUVQRCS_4lfXQvAbqwDb4aUwUVR0P-Ss0shFtDjsy7hD4f5Wm1otGcK8M6a0WO9pkshsysJa7P4k-V-6aP01k5fT-1i9A72GY1RvAPZD9kZZojhR48HIhwRRE-KtboW00ZNqdoMHjJZo2IvYK8_PAhIbBYVPKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایرانِ امیر قلعه نویی
🆚
ایران کارلوس کی‌روش در تقابل های خود با تیم ملی ازبکستان رو ببیینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30789" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
