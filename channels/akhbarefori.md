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
<img src="https://cdn4.telesco.pe/file/gmu0VEvnl7kkk6B3DNeqq3ZS-pldL5X1bIP7IpaMYvIuGHesme0UIMMNKxWBvnHo0VS_gDXoNGZt8PuR7wIdo-zNGnb8FBqQH-tOmqyeXzKkVHZgImNnHMbMGdvrVDMf2MS15TLYCDYfhQdY-ZFnqjZbwE71FJMg3hk0Grg_sTIIOl2uqOXHSAIA-1ai4yg2QiuC9u_hqnvIFb9i_u_2P13ju8RMktUp3Arg2N1dGg9uQUgMjYH_lkvHRLOGU5AEZcXLrg4D7K-xaijVA5his3rrIR_UwXB5lAW0oV9aRhhH6iZk4XQiHnfJw91B0kGgOAe0wpKJYTlNa0bJlclluA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 02:24:00</div>
<hr>

<div class="tg-post" id="msg-667172">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIIfDpukWI00pKc3O9oDOGcKIuo43RuZSP-sTqgXdbloRG_TTN21M0Uv0tIDJWYlHgqGL2SdoWvJ4rrfhmET_4Hrs-jbvjLwvkpuKYNc9XM2C8QBcee4OOPSc_Ljk8G4svVX0OxQt4HUAi-s6rBznWNoKMEB0HC6-YKFqp4I8fQTic_n6kFVrcpRF_GTuGtwEG1Ah8a8DUDDFE-g6gKYkO5cOW9A86lFNzMapDRSmB5A7qEbvR5WgyZK9s8adkrdBR0t6WyJYOncd-YRCbJLx6iUWbOYdQIa4eHQa6MDcP4YTxYq_MTq2bb7DnANvAipuBtq22jW1ny7z1nVcHMWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
بسیاری از صاحبان کسب‌وکار فکر می‌کنند...
🤔
🔹
همین که محصولاتشان را داخل دیجی‌کالا، ترب، اسنپ‌شاپ یا سایر مارکت‌پلیس‌ها قرار دهند، فروش شروع می‌شود.
🔹
اما حقیقت این است...
حضور در مارکت‌پلیس، پایان مسیر نیست؛
آغاز رقابت
است.
فروش چند برابری در سایت های ایرانی کلیک کنید
فروش چند برابری در سایت های ایرانی کلیک کنید
فروش چند برابری در سایت های ایرانی کلیک کنید
فروش چند برابری در سایت های ایرانی کلیک کنید</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/akhbarefori/667172" target="_blank">📅 01:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667171">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjfXaj4zASIebPP1lLQNB5Q604lDgNQ_cJw-gyJ3QvyAilWp5MOCfAdkarGLqzZhjrWIzINFpXvSSQS0ZhMwRrYJ9D-ozlsjVdUg8smDHExcSuoluGj91ZxfNaddOg_a7JULMePr6CNiIKgj3NWG1hlRKPZU3CnzWJRdZCliY5Xth4Xeyi0Yb8W7z4xwgmE0zm5fAf8iD2lmqkL-PEU6_gTXOCx3JHAik7BOQEdKnlzbbvu7UPgorrcGwehfU6WFllla5f8-hkkwdz1XoWlhC055wTfs8oUn3-Y6vlc3F5NOMVTmcPZCiPPbSB4raEAYsp-AKL-CxlzdP_WTRQ4hQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/akhbarefori/667171" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667170">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7930bc7d2.mp4?token=DIbwIC88xFB6X6cEvRJ6yh1hoXkajh8l71ZkbF5qAFymPgLo_8XnpVSGp0zMCTnUM2aJct5s3IT5UsOKZFL5XV4g4IBgJoFzd8szRA3HNCmvI5fjfxTG2kqFA9djbn78WL9gSH4_D-T1AZeAhYzyAzvynfoy3w8AhoedUbsC14iQW5ox-Y9OuCtmeoFTs-Z6gY6hX7amzxZ-CqPeG6WemGFB-1Mcj1OhucHVXbcXOrIy1myrWfcfZEsGPjNgUILQgakxGjbsiX8EDPKB-lwEvvAqbXEn6M1wIENFSicf0L4sHkBqGjW8Fud1lT-nyshFf9OjFil_FcZLofWWkjQ7VENUh27aLMJjDxwhQAvgV4tb6Vuo6_K4tEt-kG6v0HMUMTeYoQrMRL0pxoWJ66pFUlu4hpiq8QAdKT4oQ484A3dd3iYm3DvpP5F4Akx-pvsxrIhvStuxneMQNLhONkm97u7K2z4-BMoVdaSgs7CoPSArlbfh-1GaWXUtQlZhcocYHKe4oHPjiOvJbcY44cJKcRS9B6p_bHRwraCOb9tr57DNXpjkWvJHWUwGlLPJkx-cIFj1FgYL0lbaUaTbLfk-QtHCP9LUSZFlZ930oIOpomwJwxBfvd5Mm2yDVA_8DxFIOPbNmKPJToT3-MPePKwamd7aI2-IyIIEHNKWZ6IB_Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7930bc7d2.mp4?token=DIbwIC88xFB6X6cEvRJ6yh1hoXkajh8l71ZkbF5qAFymPgLo_8XnpVSGp0zMCTnUM2aJct5s3IT5UsOKZFL5XV4g4IBgJoFzd8szRA3HNCmvI5fjfxTG2kqFA9djbn78WL9gSH4_D-T1AZeAhYzyAzvynfoy3w8AhoedUbsC14iQW5ox-Y9OuCtmeoFTs-Z6gY6hX7amzxZ-CqPeG6WemGFB-1Mcj1OhucHVXbcXOrIy1myrWfcfZEsGPjNgUILQgakxGjbsiX8EDPKB-lwEvvAqbXEn6M1wIENFSicf0L4sHkBqGjW8Fud1lT-nyshFf9OjFil_FcZLofWWkjQ7VENUh27aLMJjDxwhQAvgV4tb6Vuo6_K4tEt-kG6v0HMUMTeYoQrMRL0pxoWJ66pFUlu4hpiq8QAdKT4oQ484A3dd3iYm3DvpP5F4Akx-pvsxrIhvStuxneMQNLhONkm97u7K2z4-BMoVdaSgs7CoPSArlbfh-1GaWXUtQlZhcocYHKe4oHPjiOvJbcY44cJKcRS9B6p_bHRwraCOb9tr57DNXpjkWvJHWUwGlLPJkx-cIFj1FgYL0lbaUaTbLfk-QtHCP9LUSZFlZ930oIOpomwJwxBfvd5Mm2yDVA_8DxFIOPbNmKPJToT3-MPePKwamd7aI2-IyIIEHNKWZ6IB_Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استانداری کربلا: هزاران موکب در خلال مراسم تشییع مستقر خواهند شد
🔹
شورای استانداری کربلا اعلام کرد که در جریان تشییع رهبر شهید انقلاب قرار است هزاران موکب در مسیر تشییع برپا شود.
🔹
بزرگان شهر تأکید دارند که این رویداد باید در شأن و جایگاه رهبر شهید برگزار شود و تمامی آمادگی‌ها با بالاترین سطح از نظم، هماهنگی و کیفیت اجرایی انجام گیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/667170" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667169">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c23eb2f.mp4?token=g-D4H5_mqDS2LxnDzeymtorTEPuq0icViHMojNXPdGzWH7vC33d20CVS7RL3sntRtxPq6ztlCRy2VnrYHmGh3rESsaQOCc-9MpOcvHmxuDDmc_Gb9U-9aB38rYyWSZJpqTY9onjWH7yEKSNRh0Gh55rz8X1nBn4uAynTcOQNK8eBX7QEXARAyj8lmCu1xPH8yAPOLzjMH9ImOcwCJo6goZefi-rCm-pSV5B6e17JTTitu1JKTI2WBzvusQeAhWA9NM3fi3UksLhK9U5k10eHpLuK6uhqv2KXMIAjSTNmq8Jn-sdfkOnRkJ2fD4RiUCSwMBfdWEQf2UGnwUkVm1DbVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c23eb2f.mp4?token=g-D4H5_mqDS2LxnDzeymtorTEPuq0icViHMojNXPdGzWH7vC33d20CVS7RL3sntRtxPq6ztlCRy2VnrYHmGh3rESsaQOCc-9MpOcvHmxuDDmc_Gb9U-9aB38rYyWSZJpqTY9onjWH7yEKSNRh0Gh55rz8X1nBn4uAynTcOQNK8eBX7QEXARAyj8lmCu1xPH8yAPOLzjMH9ImOcwCJo6goZefi-rCm-pSV5B6e17JTTitu1JKTI2WBzvusQeAhWA9NM3fi3UksLhK9U5k10eHpLuK6uhqv2KXMIAjSTNmq8Jn-sdfkOnRkJ2fD4RiUCSwMBfdWEQf2UGnwUkVm1DbVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود ده‌ها صهیونیست به خاک سوریه در میانۀ سکوت الجولانی
🔹
حدود ۷۰ شهرک‌نشین صهیونیست تلاش کردند از منطقه جبل‌الشیخ وارد خاک سوریه شوند که این اقدام به تنش و آشوب در منطقه منجر شد.
🔹
ارتش اسرائیل اعلام کرد این افراد بازداشت و برای طی مراحل قانونی به پلیس تحویل داده شده‌اند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667169" target="_blank">📅 00:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de64ccc53.mp4?token=a1k4l1oPBYWZmP-k-XUssITPHw4hXU1OJVqA7L4jsHPobCx89BZtrrlAZRiQH47bvlxMz-VyC7Y87ykPHCOearpuAFXRchaEh3HVR-8nebodStJUbPLQU8NzXaYJPttaGw_rOwO8sWOE12ek7rjGbb2Epejog2puDKJxBOwRi-K_wLnQdKY9RyfNwokdE3D3-CLD-0fySPLhcRC0H7UZqin6sm7KNAOCU6oDSq0o2vPPv3gfajBYNsL2UhGpKO2hg6d-bbZ4cGtVGVBEZnIYiDgcdzERTte3Z0TQYi5b5XKkmUOx8tPA2o7dohp6ZKW0C4pQ69c17I8RqKHzLfSJfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de64ccc53.mp4?token=a1k4l1oPBYWZmP-k-XUssITPHw4hXU1OJVqA7L4jsHPobCx89BZtrrlAZRiQH47bvlxMz-VyC7Y87ykPHCOearpuAFXRchaEh3HVR-8nebodStJUbPLQU8NzXaYJPttaGw_rOwO8sWOE12ek7rjGbb2Epejog2puDKJxBOwRi-K_wLnQdKY9RyfNwokdE3D3-CLD-0fySPLhcRC0H7UZqin6sm7KNAOCU6oDSq0o2vPPv3gfajBYNsL2UhGpKO2hg6d-bbZ4cGtVGVBEZnIYiDgcdzERTte3Z0TQYi5b5XKkmUOx8tPA2o7dohp6ZKW0C4pQ69c17I8RqKHzLfSJfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریستیانو رونالدو تایید کرد: این آخرین جام جهانی من خواهد بود!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/667167" target="_blank">📅 00:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1509a3e0e7.mp4?token=BBKWhujuWziXMqThAC8c30GS5elzEP6uzTQTY60ixcqnXRgIwmm9yjoWX5EGhXywNkdkj1YnyWMLcZQOGJ8z4iq_B5V4xNGRVF46JWCHkzm3x7gAW1uWGPbNKmKFtmC323_513vx3v6L-u6BfbjbIGb4TL18q2NWA77VuQEN5vE5MnLe1Ol5Hl1kwGXxS2BVfyXb6XkvJ6vZXHgbo2ydykaiDXDprjLow_iKXWIp1Sbw5fEwtVBfrQw83Dt9_Ir8lpVfnCdMokH6NO-rXe5XwdpPp4iOIx_V-98g88XqgXSnWcW7e2yroZNA2cVxho5uCS40Wow0zgHSc0w3gITVEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1509a3e0e7.mp4?token=BBKWhujuWziXMqThAC8c30GS5elzEP6uzTQTY60ixcqnXRgIwmm9yjoWX5EGhXywNkdkj1YnyWMLcZQOGJ8z4iq_B5V4xNGRVF46JWCHkzm3x7gAW1uWGPbNKmKFtmC323_513vx3v6L-u6BfbjbIGb4TL18q2NWA77VuQEN5vE5MnLe1Ol5Hl1kwGXxS2BVfyXb6XkvJ6vZXHgbo2ydykaiDXDprjLow_iKXWIp1Sbw5fEwtVBfrQw83Dt9_Ir8lpVfnCdMokH6NO-rXe5XwdpPp4iOIx_V-98g88XqgXSnWcW7e2yroZNA2cVxho5uCS40Wow0zgHSc0w3gITVEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه تشییع پیکر رهبر شهید در عراق
🔹
مراسم سه‌شنبه شب در عراق آغاز می‌شود؛ دولت عراق میزبانی رسمی را بر عهده دارد.
🔹
صبح چهارشنبه، ساعت ۶، بدرقه و تشییع مردمی در نجف شروع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/667166" target="_blank">📅 00:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
نتانیاهو: ما غیر از آمریکا متحدان دیگری هم داریم
🔹
نخست‌وزیر رژیم صهیونیستی به سخنان جی دی ونس، معاون رئیس‌جمهور آمریکا که گفته بود واشنگتن تنها متحد اسرائیل است پاسخ داد.
🔹
ما دوستان دیگری هم داریم «مثلا کشور کوچکی به نام هند که ۱.۴ میلیارد نفر در آن زندگی می‌کنند.»
🔹
برخی از کارشناسان معتقدند شکاف‌های ظاهری میان رژیم اسرائیل و آمریکا بخشی از جنگ زرگری دو طرف برای پیشبرد سیاست‌های مشترک آنها است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/667165" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احمدی، نماینده مجلس: بیش از ۳۰۰ خبرنگار خارجی عظمت تشییع رهبر شهید را به جهان مخابره می‌کنند
علی احمدی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
حضور بیش از ۳۰۰ خبرنگار خارجی، بازتاب‌دهنده شکوه مراسم تشییع رهبر شهید در جهان است.
🔹
این مراسم یک «قیام ملی» و نماد همبستگی مردم ایران است و برخی روایت‌های رسانه‌های خارجی نتوانسته از عظمت آن بکاهد.
🔹
برخی رسانه‌های خارجی با تعابیر تحقیرآمیز درباره تشییع در عراق تلاش کردند از شکوه آن بکاهند، اما حضور پرشور شیعیان عراق و تمهیدات امنیتی حشدالشعبی، امنیت کامل مراسم را تضمین کرده است.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/667164" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
شهرک‌های مسیحی‌نشین لبنان ادعاهای نتانیاهو را تکذیب کردند
🔹
شهردار شهرک رمیش، اظهارات بنیامین نتانیاهو درباره درخواست برخی شهرک‌های مسیحی جنوب لبنان برای پیوستن به اسرائیل را به‌طور کامل تکذیب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/667163" target="_blank">📅 00:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712f858aea.mp4?token=duynfYm7zT_tH2OWh2D4l8YmvLIdsAl_AHsZJeCzXzy7QqO17ipHCSrl-oQuUIr4Op0jDVeynQ4RqtUh62JcwuL45b90lTeE-0vRAKJ7zPKB_OHWCGnzARjB9m_Pz6OIgMdmsSQZqlVCy8DNS6pYbK_S0K46uldjNqe9cvr70pbdW32FcWLmaKDmgzl6lQMDAogzMpGy9TBbc8MvI3QOFeZL7iwMK0RXpZCJKaPxCrOjlQZEMej1p5h1IJCVhGUsNx4N6g6OrfOvejzzFqlCz8WgpQJ7D2mtJar0b3aM27YZ0HX1yvaFwq7y1MXedbobM4nWb9NWKxfOqUtHj7gPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712f858aea.mp4?token=duynfYm7zT_tH2OWh2D4l8YmvLIdsAl_AHsZJeCzXzy7QqO17ipHCSrl-oQuUIr4Op0jDVeynQ4RqtUh62JcwuL45b90lTeE-0vRAKJ7zPKB_OHWCGnzARjB9m_Pz6OIgMdmsSQZqlVCy8DNS6pYbK_S0K46uldjNqe9cvr70pbdW32FcWLmaKDmgzl6lQMDAogzMpGy9TBbc8MvI3QOFeZL7iwMK0RXpZCJKaPxCrOjlQZEMej1p5h1IJCVhGUsNx4N6g6OrfOvejzzFqlCz8WgpQJ7D2mtJar0b3aM27YZ0HX1yvaFwq7y1MXedbobM4nWb9NWKxfOqUtHj7gPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شنیدنی کمیل خجسته، برادرزاده همسر رهبر شهید از اهمیت دادن رهبر شهید انقلاب به نماز اول وقت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/667162" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5v-3KWaVi2QBR6DxJZZdW8aQG4SyjsGwUn7AwgX93sWwRjsabtAzniqYsC5lp92xztaUFKWZkkl2Tib-uEq0guJGYlKh_0LmdSMaJ6h5xRQhdthldUCk0Tdb_MaHM2alsQTr7DathpqIo34WD-Fg3wVDwS4KP2mz1M3qPQK3M75YB06k-AV5nDMAiVT2Xj1QyqR1N_PY9YNnzOjCPU8X3IrGStNMYWSHJQuCHs0jN8TO0IpebcG6Q0fnq9vTYG5KrxThzML6b3WzywMVUO0rAgF8EMLWNo_jLFnjATGPehG9wW5jiAO2nvn_4aHZAUCqDvC0Dq-Sb-ogQmdtiOzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/667161" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ترامپ از فیفا به خاطر بخشش کارت قرمز بازیکن آمریکا تشکر کرد! #جام_تایم۲۶  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/667160" target="_blank">📅 00:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
حضور فرزندان رهبر شهید انقلاب در مصلی تهران پیش از اقامه نماز بر پیکر ایشان
👇
khabarfoori.com/fa/tiny/news-3227938
🔹
نخستین تصاویر از بوئینگ‌های ۷۷۷ عربستان که به‌ تازگی وارد ایران شده‌اند
👇
khabarfoori.com/fa/tiny/news-3227986
🔹
پدر شهید ۱۴ ماهه بیت رهبری کیست؟
👇
khabarfoori.com/fa/tiny/news-3228074
🔹
شرط رهبر در جلسه خواستگاری از دخترش؛ شرطی که شهید باقری کنی با جان پذیرفت
👇
khabarfoori.com/fa/tiny/news-3228078
🔹
عروسی تیلور سوئیفت روی روان ترامپ | جدال رسانه‌ای بالا گرفت
👇
khabarfoori.com/fa/tiny/news-3227857
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/667159" target="_blank">📅 23:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef0be33eb3.mp4?token=qFb-wP_zK859djjhMDfantqGjBzDXQJ9Ks4twKcyZPvrUeh68Avs8pu8tuNusCIxQbYB8uioReHNUBm-Rby2DfO9tktVGl8Zqf8tW3QcbDRzE_biSKVy2VgCvTHHqwr_feGVfa4q5PiRTaJTnx4SVLC2zE1c9eN97WZAj7Tg6TMSXZ7eRpBqk7pUx6P3vPMIg9qC3kbkubH7W7K1xyDd8PjQgxz_ok3b1DYH9b7X8ioSCmZMKuyP3Ec9B3dg5atVAE72g1st9Eml9M-tiH9tBt7afvn66t9T4h-xrrQXklyjQJIt7FtpL7D7Z1_7c0mNE3wpD2hIRA-54qTlsm8QTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef0be33eb3.mp4?token=qFb-wP_zK859djjhMDfantqGjBzDXQJ9Ks4twKcyZPvrUeh68Avs8pu8tuNusCIxQbYB8uioReHNUBm-Rby2DfO9tktVGl8Zqf8tW3QcbDRzE_biSKVy2VgCvTHHqwr_feGVfa4q5PiRTaJTnx4SVLC2zE1c9eN97WZAj7Tg6TMSXZ7eRpBqk7pUx6P3vPMIg9qC3kbkubH7W7K1xyDd8PjQgxz_ok3b1DYH9b7X8ioSCmZMKuyP3Ec9B3dg5atVAE72g1st9Eml9M-tiH9tBt7afvn66t9T4h-xrrQXklyjQJIt7FtpL7D7Z1_7c0mNE3wpD2hIRA-54qTlsm8QTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان: اگر حال‌وهوای امروز و دیروز عاطفی‌تر بود، فردا حماسی‌تر خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/667158" target="_blank">📅 23:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f653a1574a.mp4?token=n3L8kclby5DIJVI9CXcn-GmM7WDG-5iLgCM2Gy10gMls_l7tpAfyqCY0VrTd_VQxZuZNQMokNYuCpzrDjy7sz0_zRgFhJb2NfxmgBifLo5KJnnxE9QNQz0I7kpAoJhRxxtByD2kcFj3rC0-wPfe6yEJd5CtXTkYe5Sgu_rYUl13qVibA_zwR3rcpC93H7mAkUDYMnN5okQFQvnj8zUWIfUPe4b9wv0a7_y5psMB0WNN7UPw0WH8cbDVjvNTpw8FOrIRW_wOVfhF97Dtb2ihRpeNOdio6wIc9vpdDFWtCCUqJmyhl9MIrozxAXLJMEnRTO4Ji3LJQeVpHlISCfPuOBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f653a1574a.mp4?token=n3L8kclby5DIJVI9CXcn-GmM7WDG-5iLgCM2Gy10gMls_l7tpAfyqCY0VrTd_VQxZuZNQMokNYuCpzrDjy7sz0_zRgFhJb2NfxmgBifLo5KJnnxE9QNQz0I7kpAoJhRxxtByD2kcFj3rC0-wPfe6yEJd5CtXTkYe5Sgu_rYUl13qVibA_zwR3rcpC93H7mAkUDYMnN5okQFQvnj8zUWIfUPe4b9wv0a7_y5psMB0WNN7UPw0WH8cbDVjvNTpw8FOrIRW_wOVfhF97Dtb2ihRpeNOdio6wIc9vpdDFWtCCUqJmyhl9MIrozxAXLJMEnRTO4Ji3LJQeVpHlISCfPuOBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آستانه سفر دونالد ترامپ به ترکیه برای شرکت در نشست ناتو، گروهی از فعالان ترکیه‌ای با نصب بنری بر روی پل هالیچ در استانبول، خطاب به شهروندان نوشتند: «کودکانتان را پنهان کنید؛ ترامپ در راه است.
»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667157" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43b7d7fa8c.mp4?token=tmS6lrjVCOYIcIzOFPPysnXd8mH8kraofYIs1ugIqExw9rWjcDtiBLzDhX3PXSdXFnpG69FGAkj0PDmF-KEYhRMmrcD2h164W2Bf7Vp_0RC16IJUDZqpwCJdwHYrfztFt0pEMUIgPtby0bp7xxOID12xpWeyY7DxK9fqla1Qp1kyY3S81infx-FBH2HMz9y4bIFRmnUUxjkCoDxSSXLNPQxpN7TYu5Eu7k3MSsZ7_ISKWasa6jJ37hkp1GTpvOkA-i_yYefyrkXRTN5l3aBgr8rNZ6iwoswlSV1PKS4dAkva1MEH9FWqacnIBA6xs37EvvkYRExn0WffFSqUwX6IFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43b7d7fa8c.mp4?token=tmS6lrjVCOYIcIzOFPPysnXd8mH8kraofYIs1ugIqExw9rWjcDtiBLzDhX3PXSdXFnpG69FGAkj0PDmF-KEYhRMmrcD2h164W2Bf7Vp_0RC16IJUDZqpwCJdwHYrfztFt0pEMUIgPtby0bp7xxOID12xpWeyY7DxK9fqla1Qp1kyY3S81infx-FBH2HMz9y4bIFRmnUUxjkCoDxSSXLNPQxpN7TYu5Eu7k3MSsZ7_ISKWasa6jJ37hkp1GTpvOkA-i_yYefyrkXRTN5l3aBgr8rNZ6iwoswlSV1PKS4dAkva1MEH9FWqacnIBA6xs37EvvkYRExn0WffFSqUwX6IFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر دفتر شبکه الجزیره: مراسم گسترده تشییع رهبر شهید ایران پیام محبوبیت مردمی جمهوری اسلامی را به دنیا مخابره کرد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/667156" target="_blank">📅 23:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667155">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2881a783.mp4?token=k6xpp2cNi2ibIVOg04Xth41B9VSGGC6xX1MmG4C4k4vVEdhIaWfO9O8T_Ztum56e-2ccZeltzwJ0nACK2oqFNYZdXL5xvPGD7BcrCUUlRVX8weH7VK7CEW4Sfr4tZ4ps7Nh80Yedqcfu8tVpc2rwWJcEOHvZRhlVgggRpiBFGMZgT44w3HB3Gvq0qklM1m6s6JGCGsH7O9hACsrd6cLHDtV5T7jkrxDxeSdpd25pJny2UEMvdqY_RGUNQYRitzKu6rNrbjSAhv8vKUrR3DftA5RdkGK9dLcmF2HfGrg648joU1h3izSGzNVwkWcrT58eDwgUf5_nMaf8qzLjz05lkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2881a783.mp4?token=k6xpp2cNi2ibIVOg04Xth41B9VSGGC6xX1MmG4C4k4vVEdhIaWfO9O8T_Ztum56e-2ccZeltzwJ0nACK2oqFNYZdXL5xvPGD7BcrCUUlRVX8weH7VK7CEW4Sfr4tZ4ps7Nh80Yedqcfu8tVpc2rwWJcEOHvZRhlVgggRpiBFGMZgT44w3HB3Gvq0qklM1m6s6JGCGsH7O9hACsrd6cLHDtV5T7jkrxDxeSdpd25pJny2UEMvdqY_RGUNQYRitzKu6rNrbjSAhv8vKUrR3DftA5RdkGK9dLcmF2HfGrg648joU1h3izSGzNVwkWcrT58eDwgUf5_nMaf8qzLjz05lkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت علیرضا دبیر از دیدار با رهبر شهید انقلاب پس از کسب قهرمانی در مسابقات المپیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/667155" target="_blank">📅 23:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667154">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121998aac7.mp4?token=MTA561ewsNKe6MntV6Ej8N_KvuYMoKl6IMiqBHk8cXS1GNHPPtt4_88P1_WiH1dgeCGQyw1DOEIaxlLUOlgDGvMdk_ohoysJlltAjrzwKGByUfuYGv3Q7k-7U6KGPlefv5Y9tXCwPEk5NJvP6GsfTUBSwxKwaz5Jc89ylePLkGNrO4zI4Yd73Uzy4EYZWQ_SDGNPzhNPbRdMbHB2EflkkYJGSGemfUDmZ8CR_zpkHtX46Vj1oX3_ScADy1-oi_funMnI7xZoaR9NkE01Q-zFOJtXqqwkRhVi6fkVqVz1fvFwZAQnsoL7WedTgGH0Bs48T8iZEhH950MxgMoPEkGBgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121998aac7.mp4?token=MTA561ewsNKe6MntV6Ej8N_KvuYMoKl6IMiqBHk8cXS1GNHPPtt4_88P1_WiH1dgeCGQyw1DOEIaxlLUOlgDGvMdk_ohoysJlltAjrzwKGByUfuYGv3Q7k-7U6KGPlefv5Y9tXCwPEk5NJvP6GsfTUBSwxKwaz5Jc89ylePLkGNrO4zI4Yd73Uzy4EYZWQ_SDGNPzhNPbRdMbHB2EflkkYJGSGemfUDmZ8CR_zpkHtX46Vj1oX3_ScADy1-oi_funMnI7xZoaR9NkE01Q-zFOJtXqqwkRhVi6fkVqVz1fvFwZAQnsoL7WedTgGH0Bs48T8iZEhH950MxgMoPEkGBgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آماده‌سازی جایگاه ویژه اقامه نماز بر پیکر «آقای شهید ایران» در مسجد مقدس جمکران
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/667154" target="_blank">📅 23:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667153">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کانال ۱۳ اسرائیل: نتانیاهو در حال حاضر درباره خروج از برخی نقاط در جنوب لبنان مشورت‌های امنیتی برگزار می‌کند.
🔹
زلنسکی: طبق اطلاعات به دست آمده، روسیه در حال آماده‌سازی یک حمله گسترده دیگر است.
🔹
برخورد قطار با ۲ عابر در جوارم سوادکوه/ یک زن جان باخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/667153" target="_blank">📅 23:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667152">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مالکی: ثبت جهانی مراسم تشییع باید توسط دستگاه دیپلماسی پیگیری شود
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
حضور بیش از یکصد هیئت خارجی در مراسم تشییع رهبر شهید و استقبال بی‌نظیر مردم نشان از انسجام ملی و جایگاه ویژه ایران در منطقه دارد، بسیاری از مهمانان خارجی از گستردگی و نظم مراسم شگفت‌زده شدند.
🔹
ثبت جهانی این رویداد تاریخی باید از سوی دستگاه‌های دیپلماسی و فرهنگی پیگیری شود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/667152" target="_blank">📅 23:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J50Hfyyu0F4XKDgefEXYU7Ty0RSRql3fDLyv3bMtAsDZyFEZOCIN_mOKTQTbMqJa_qHye0th3a_OpCD14Hl79xVZx3tVc4dfQweolpMCND4ttTvw54cLpx82ynuWG6L2hT3ikOQ5gN_BMS-jw10Qfokueg85V30oHKvQ8i0KVwm3oxbOnLsNAdbVjkyO4YOQKfk8cQQBWCBj0L0yKYN_on6NrYRMMUsb5ui1V5BpChZSaSSw-TGmI93wtylX1mpELdNUtqzEvXIfsTFBQ9vnnYv9n_KmfdzCh-lpLFLqApIpwSooSCCuZeM_rgYg1dDMGgxU2fRjQVrWkSNbYuw4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارلوس کی‌روش از تیم ملی غنا اخراج شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/667151" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d850eb03dc.mp4?token=Wos90CHeLBQbk0tSWsxgzQqeT4AR4X-k2kDRJroPdgckDrZG-HOaEE2Bt-KAHmsxHpNx3W6FpqwEpWUMaCI1j9crKgZh-G2u-OtpJMlCqGc2GaUUosMVNk30S5pQrIdPh5Jd_f60zBRcbUn-H95UZXZxmYowfOwHk-LO3ILy0mGT8_SNEPaAZ1jtnwgVcljFY6BGiIBfTWz5yZQjDesCUOi_-d8f43ht8-C2yWPdWWWSNwMDz4v23R3d4JsJoXGl0Jdm8Ll7SAWBK1KH6ZHcdN7eqzvGmCQm3u7VkfcwW2krvp5j8763tYV1cgRxDUfkv5ncF0aCRfmUvBgFChE6jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d850eb03dc.mp4?token=Wos90CHeLBQbk0tSWsxgzQqeT4AR4X-k2kDRJroPdgckDrZG-HOaEE2Bt-KAHmsxHpNx3W6FpqwEpWUMaCI1j9crKgZh-G2u-OtpJMlCqGc2GaUUosMVNk30S5pQrIdPh5Jd_f60zBRcbUn-H95UZXZxmYowfOwHk-LO3ILy0mGT8_SNEPaAZ1jtnwgVcljFY6BGiIBfTWz5yZQjDesCUOi_-d8f43ht8-C2yWPdWWWSNwMDz4v23R3d4JsJoXGl0Jdm8Ll7SAWBK1KH6ZHcdN7eqzvGmCQm3u7VkfcwW2krvp5j8763tYV1cgRxDUfkv5ncF0aCRfmUvBgFChE6jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصول اولیه برای ثبت تصویر ماندگار از تشییع
🎥
جهت فیلم‌برداری را درست انتخاب کن.
🔍
از زوم دیجیتال استفاده نکن.
🚶
اگر امکانش هست، به سوژه نزدیک‌تر شو تا کیفیت تصویر حفظ شود.
🤝
موقع فیلم‌برداری، گوشی را تا جای ممکن ثابت نگه دار.
📷
تمیز کردن لنز دوربین
همین چند نکته ساده، تفاوت بین یک قاب معمولی و یک تصویر ماندگار را رقم می‌زند.
✨
تو فقط لحظه‌ها را ثبت نکن؛ کاری کن هر بار که دوباره دیده می‌شوند، همان حس را زنده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/667150" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667149">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2451fa3d0.mp4?token=ACnistwovfI9NLlHRFNRCTw_7L6MCpqB7N8shtm1T03_AWmQ0bxNByh-cUc32kz7U7ctJ8ajAR4n_lsHIj1HVupjMDf5Gp4-bVs5Pocn7F1DfEUacFCmAaedXSNiyIgBQBVuPc1WNigRycfRcfAFN_ldbyIWGyxS5oZEx1uTPIq5yrhKNGB7xaTihb77Zp3dDFl9VsuR9aClbvRjhBNiUcuKcvRDSmzBZD_NuI2COnsAGpSRpaBj-PmYWa51_gfn3HAcaLO-eTSkmf94GtGlFd4Dt5v7H02u4GsVNDGwD9_GFEYJOSdTfALJinuLJTNi3E1GukTpiJGNimUYm2QjQAZcngkvOsYGm8DSbEkddez9JOPKWQ_GymfAgKj8elVwHTpcENq-lWaYPbOpq4c-6kZtx2uAs3EMi3oO9wNSl6Gu9-ZbFKizSGqiOU4BILFCd085QzxK72lPIsES4NZQsrigpB0_N92O__FIbxbtSdoDWRF9I5N_a5XfuoT4yQTsw4oLoBXASzT9q_hHbUseK3XKdb5aZl3ibI38AB_eSBMAGmrzO3FERFWi2m3ctgaI7Vx9e86SG2EbDULTy68wCW5LhzNfZpBWOCVRjN4MvAs2adkXcol7iPLZUpU1pfGzk9LHUwdCOnb5nVm9suGNEX-hLjFmr1pnXJ-8Xi4mRN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2451fa3d0.mp4?token=ACnistwovfI9NLlHRFNRCTw_7L6MCpqB7N8shtm1T03_AWmQ0bxNByh-cUc32kz7U7ctJ8ajAR4n_lsHIj1HVupjMDf5Gp4-bVs5Pocn7F1DfEUacFCmAaedXSNiyIgBQBVuPc1WNigRycfRcfAFN_ldbyIWGyxS5oZEx1uTPIq5yrhKNGB7xaTihb77Zp3dDFl9VsuR9aClbvRjhBNiUcuKcvRDSmzBZD_NuI2COnsAGpSRpaBj-PmYWa51_gfn3HAcaLO-eTSkmf94GtGlFd4Dt5v7H02u4GsVNDGwD9_GFEYJOSdTfALJinuLJTNi3E1GukTpiJGNimUYm2QjQAZcngkvOsYGm8DSbEkddez9JOPKWQ_GymfAgKj8elVwHTpcENq-lWaYPbOpq4c-6kZtx2uAs3EMi3oO9wNSl6Gu9-ZbFKizSGqiOU4BILFCd085QzxK72lPIsES4NZQsrigpB0_N92O__FIbxbtSdoDWRF9I5N_a5XfuoT4yQTsw4oLoBXASzT9q_hHbUseK3XKdb5aZl3ibI38AB_eSBMAGmrzO3FERFWi2m3ctgaI7Vx9e86SG2EbDULTy68wCW5LhzNfZpBWOCVRjN4MvAs2adkXcol7iPLZUpU1pfGzk9LHUwdCOnb5nVm9suGNEX-hLjFmr1pnXJ-8Xi4mRN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر کرجی خطاب به رهبر شهید: قول می‌دهم تا پای جان پای ایران و انقلاب بمانم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/667149" target="_blank">📅 23:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667148">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ba4e6e6d.mp4?token=k-FHVMPOkulo1fIw2h7GygSpYSpoA7Wcu1Fxvj2ibucvGRB0LL9IKS-SKFbcNyd9qiOlkvniZ9d1TqV-W7Kq6ApehMQG6emeexLhORnh9d8ouxROBNuP_KW4WPVcMTXfJfhz18G-W5sjGGqab3rxUHrEDdd1Z3UF5HAXUJ5aJvGn8D_nXRHIz7CoFqTnazS0iVfwJInHgnIEew1UFZa-MHuEOsIQsmxxPG2a37SuJLcfWNWAsBy272aB2mWMh1uJYKEx4gVViFm2_YKroiVxg9zMnC5mi3DGQsfgOGIU3YPyTngxuHENCj3I-pj6YJcOD8QMa7j4foTN0OEqCUV7Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ba4e6e6d.mp4?token=k-FHVMPOkulo1fIw2h7GygSpYSpoA7Wcu1Fxvj2ibucvGRB0LL9IKS-SKFbcNyd9qiOlkvniZ9d1TqV-W7Kq6ApehMQG6emeexLhORnh9d8ouxROBNuP_KW4WPVcMTXfJfhz18G-W5sjGGqab3rxUHrEDdd1Z3UF5HAXUJ5aJvGn8D_nXRHIz7CoFqTnazS0iVfwJInHgnIEew1UFZa-MHuEOsIQsmxxPG2a37SuJLcfWNWAsBy272aB2mWMh1uJYKEx4gVViFm2_YKroiVxg9zMnC5mi3DGQsfgOGIU3YPyTngxuHENCj3I-pj6YJcOD8QMa7j4foTN0OEqCUV7Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام میرهاشم حسینی: مسئولان در صورت تکرار تهدیدهای دشمن، پاسخی محکم به آن‌ها بدهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/667148" target="_blank">📅 23:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667147">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429d9e230a.mp4?token=GTFgqmZ8pjNp6Gfw2wAICdvzgB79QDHzyVfyUAziiDBFGcQ3UMvmykHjsgoEjQ0c4YhFGw9Bk_e_8SWA_1BZ1fgSl-_I2C5ucZQSNiVyR0bqc0wbXlE6viOTtHuAxonKPhkisxMdJd8HRVxDkeSmNzcSYnxl8xs2Vk9FFAj4-6Y6R4JQbB50jFA7l1POiLG2cAGdlV9G3dVJRUZIbsTkWHySQbuGBoqGX7Q6LeI43FdPuV6RkE4uLJ0cEoBhf4gL57TDnf81-8lRiGcwMr3PwY-SgZBg0USf0KK81TG3EYyCxddIkVsJNDMG7IPx1O9pnR_6ykfNwzOpSLL-0s8Vhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429d9e230a.mp4?token=GTFgqmZ8pjNp6Gfw2wAICdvzgB79QDHzyVfyUAziiDBFGcQ3UMvmykHjsgoEjQ0c4YhFGw9Bk_e_8SWA_1BZ1fgSl-_I2C5ucZQSNiVyR0bqc0wbXlE6viOTtHuAxonKPhkisxMdJd8HRVxDkeSmNzcSYnxl8xs2Vk9FFAj4-6Y6R4JQbB50jFA7l1POiLG2cAGdlV9G3dVJRUZIbsTkWHySQbuGBoqGX7Q6LeI43FdPuV6RkE4uLJ0cEoBhf4gL57TDnf81-8lRiGcwMr3PwY-SgZBg0USf0KK81TG3EYyCxddIkVsJNDMG7IPx1O9pnR_6ykfNwzOpSLL-0s8Vhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
️
به نظرت این میز کار کیه؟!
🔹
خیلی دوست دارم با چنین کسی ملاقات کنم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/667147" target="_blank">📅 23:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667146">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خوزستان سه‌شنبه تعطیل شد
🔹
به دستور استاندار خوزستان با توجه به موج بازگشت تشییع‌کنندگان پیکر رهبر شهید از تهران و قم، سه‌شنبه ۱۷ تیر استان خوزستان تعطیل اعلام شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/667146" target="_blank">📅 23:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667145">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d26df7cb5.mp4?token=jW-8ypI384t52HhU3wKIXAgtc0o87HRDYMU0DqwcwRLjeE83aL9pc8_dB0OoVba3bSkJDuO8Nkdq2L9JS6m8HgSjXSjd5sBsD4L1LN_XjM7MOXaEstRr_gkAhi19oBsQ-_tmONjvTObNSQ2QUWjdi0jZmp-MC9UNAqfnM7tEHstNHCxf4MEJdQKRte69QwJN6UkCknpOF1-aIq5Ql3wKK-8jKg12926FYQwJmESSDKdEwgrFUfAe6DTNaWspDiIRCo35mqBNqO0yiv8IuoifBRRuWaMeT1MQTOsfm_GiHeMVhYIJnuf_eP1PWBDhiUYrQ_vBCuMgmi4M91F78SD9IYjox7H4RaVMhEKsUb5EGj6lCyelu43Zpz9S_oqzl5UuMKpRL4Au8FT33qy7nPTAjUm6URjoWKIvGEQegrbBCcxIpanV_z5riyEkUxcGolsaLZzGKMZMkh4zBHjmLXPxaf90RdnpSx295LrKVgYrkLkWnUHTHOODKtIM58b_AoD3WOKOv8Lif7lAXFLHSKX90ShjHz_4jDQcExNYhjpDDEWm1CSblujF9Bzy-HIJUvZrAjwltPhk-Q4q2q2kzKMmATFPXSLpeLwCBfAl-YjFLlRudOa5ERme8DV2KF34HD_qgBMlJ6Rgf0qw_FcfevfeDn08u6twLtDzTk9VUL8OSHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d26df7cb5.mp4?token=jW-8ypI384t52HhU3wKIXAgtc0o87HRDYMU0DqwcwRLjeE83aL9pc8_dB0OoVba3bSkJDuO8Nkdq2L9JS6m8HgSjXSjd5sBsD4L1LN_XjM7MOXaEstRr_gkAhi19oBsQ-_tmONjvTObNSQ2QUWjdi0jZmp-MC9UNAqfnM7tEHstNHCxf4MEJdQKRte69QwJN6UkCknpOF1-aIq5Ql3wKK-8jKg12926FYQwJmESSDKdEwgrFUfAe6DTNaWspDiIRCo35mqBNqO0yiv8IuoifBRRuWaMeT1MQTOsfm_GiHeMVhYIJnuf_eP1PWBDhiUYrQ_vBCuMgmi4M91F78SD9IYjox7H4RaVMhEKsUb5EGj6lCyelu43Zpz9S_oqzl5UuMKpRL4Au8FT33qy7nPTAjUm6URjoWKIvGEQegrbBCcxIpanV_z5riyEkUxcGolsaLZzGKMZMkh4zBHjmLXPxaf90RdnpSx295LrKVgYrkLkWnUHTHOODKtIM58b_AoD3WOKOv8Lif7lAXFLHSKX90ShjHz_4jDQcExNYhjpDDEWm1CSblujF9Bzy-HIJUvZrAjwltPhk-Q4q2q2kzKMmATFPXSLpeLwCBfAl-YjFLlRudOa5ERme8DV2KF34HD_qgBMlJ6Rgf0qw_FcfevfeDn08u6twLtDzTk9VUL8OSHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: آقا انتقامت را می‌گیریم بغضی که در سینه داریم، تبدیل به خشم می‌شود، خشمی که باعث نابودی آمریکا و اسرائیل خواهد شد
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/667145" target="_blank">📅 23:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667144">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2984b64fa.mp4?token=S_eUBWXbJ0o_50E0-gm9VPI96ExNciN5uTW60E59K2cT5p7sh74jne5C6yBRzANBTIICAjfHB0DJ4kHT1zoN4gSiYIPkzNmjcVOZvsMU_QPB7Z9OmbmLy-JHB7S-KJwGZRetveQcvgqaB3t3kCQK1PuqeCpv9Xm2wRKkWeQxm4JecWUXCYYlXCvYZvQroQ4EItdTSD57Zk3Rfgv665tUoYThYaCL-TYAJ5PY8cQFIgUUI-uogfQbRJuT9xMw6dHiizv8-vQA_P2aH_5_13BzSmJT_kusJ86gT4GkLNu-otNuxe3t08y6Vm6onslMKoTzA5pDpbtJU6c3L3eXZnyZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2984b64fa.mp4?token=S_eUBWXbJ0o_50E0-gm9VPI96ExNciN5uTW60E59K2cT5p7sh74jne5C6yBRzANBTIICAjfHB0DJ4kHT1zoN4gSiYIPkzNmjcVOZvsMU_QPB7Z9OmbmLy-JHB7S-KJwGZRetveQcvgqaB3t3kCQK1PuqeCpv9Xm2wRKkWeQxm4JecWUXCYYlXCvYZvQroQ4EItdTSD57Zk3Rfgv665tUoYThYaCL-TYAJ5PY8cQFIgUUI-uogfQbRJuT9xMw6dHiizv8-vQA_P2aH_5_13BzSmJT_kusJ86gT4GkLNu-otNuxe3t08y6Vm6onslMKoTzA5pDpbtJU6c3L3eXZnyZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیین وداع با پیکر رهبر شهید در دو روز و در مصلای تهران تمام شد و مردم برای مراسم تشییع در پنج شهر تهران، قم، نجف، کربلا و مشهد آماده می‌شوند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667144" target="_blank">📅 23:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667143">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=OIe_nX3h9dZ4ljcukn80wvlzciMIlmkB1EVF3b6nAwNEnlSVKa47qTJOu-OFGdHS8_oTfjn1xnH9u5Y9LqAo1Us_axxcYwyLEyaXn7Tng1KX2aLvv8nLQB56jSlm1lLHcYy552fnBCQoOo5D7QfFSOyjlhe_XujhpH5fsbPlzgYpRJEdv6wNSTY3_XcbvGc6__SW7vJugYP4ZPaLmpegYuCGozI106-DTO2tDyy9-HougmoRCuiSqujORdCGfmGqSS25WA3k5mvPaSw8xqJYyzHkN7ctKyTLQRYnAXbG9tKjH2oDoZKViD19nPJA4nwiUMrD8ImVdqJFO6JqsPDOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=OIe_nX3h9dZ4ljcukn80wvlzciMIlmkB1EVF3b6nAwNEnlSVKa47qTJOu-OFGdHS8_oTfjn1xnH9u5Y9LqAo1Us_axxcYwyLEyaXn7Tng1KX2aLvv8nLQB56jSlm1lLHcYy552fnBCQoOo5D7QfFSOyjlhe_XujhpH5fsbPlzgYpRJEdv6wNSTY3_XcbvGc6__SW7vJugYP4ZPaLmpegYuCGozI106-DTO2tDyy9-HougmoRCuiSqujORdCGfmGqSS25WA3k5mvPaSw8xqJYyzHkN7ctKyTLQRYnAXbG9tKjH2oDoZKViD19nPJA4nwiUMrD8ImVdqJFO6JqsPDOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران: خدمات ۲۴ ساعته مترو و حدود ۴ هزار اتوبوس جهت تسهیل رفت‌وآمد مردم در مراسم تشییع رهبر شهید فراهم شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/667143" target="_blank">📅 22:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667142">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTkMh-KbjwOjbQIp2cpXH6Qh8gMUhamfgnLPbPMkdEE96xTKf-uHu1sYvXUgEO9Xc4v3yBSYv5eofv93kgMntTSMfwf9JStYaICgEYOzIoXdGXI5fVCeMhGbT-3X-Yi1R_wpSKXeX2GTsOrbWsAwuiZZLnwDDZWQ0HreNa78UdmeznXtUntPfK6iqVmjrvgn4nfaYA4kbBHyXffsgs2zwXBpTW-PsTH5M-xNNvBqOEICS7hmGXCZk3dQ1fqkCCPZwpCROKPLZokalikhQ5J1-4X_zG1M-q63RZHUt_Nj42nORWh-ZamiHBxIRgKfupOoCii75gFD4OCPYJxaZCealQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: خونخواهی امام شهید، آزادی قدس است
🔹
رئیس مجلس در دیدار با رئیس شورای رهبری حماس تأکید کرد دیپلماسی باید با تکیه بر توان دفاعی، دستاوردهای میدان را حفظ کند؛ وی با رد به رسمیت شناختن اسرائیل، تصریح کرد که حمایت از جبهه مقاومت ادامه دارد.
🔹
درویش…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/667142" target="_blank">📅 22:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667141">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رئیس اورژانس کشور: بیش از ۲۲ هزار نفر از خدمات درمانی مراسم وداع با رهبر شهید استفاده کردند
سعید میعادفر، رئیس اورژانس کشور در
#گفتگو
با خبرفوری:
🔹
تا ساعت ۱۶ امروز، ۲۲۶۴۴ نفر از خدمات درمانی استفاده کردند؛ ۲۰۳۳۱ نفر خدمات سرپایی دریافت کردند و ۹۵ نفر به مراکز درمانی اعزام شدند (۸۴ نفر زمینی، ۵ نفر هوایی و ۶ نفر با مترو).
🔹
در ۸ بیمارستان صحرایی، ۱۷۱۱۸ مراجعه سرپایی ثبت شد؛ ۵۰ نفر به مراکز درمانی منتقل شدند، ۳۵۸۸ نفر به‌دلیل ضعف عمومی و گرمازدگی سرم‌تراپی شدند و ۲۷ نفر جراحی محدود سرپایی انجام دادند.
🔹
عمده موارد ناشی از ضعف و گرمازدگی بود؛ تا این لحظه مورد فوتی گزارش نشده و ۳ مورد احیای قلبی‌ریوی (CPR) موفق نیز انجام شده است.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/667141" target="_blank">📅 22:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667140">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aab6bfc91.mp4?token=rbICBQBLIkIgx6In0QSgsnNt-YI1ScpxoCpdxZNVujnhWXZfhYUJA_CcAalz0-NbWt50K7OGKy9MjxDa2IdQW28z4KcxbJEbAG6L7lvIuXcOVN5oGPeRC2UpRxgXXmO_Xld125GEEldHtjXlAvduKPwTz1YjT2hTeg02AbDpfdFGDS154ZLhqtO0oUzLIYqpCE4KhqvxtNn5iBaUWUm9oMMDTMls6Q-sTaZ8d8btV3-Lw_RCA2-dhXocRh8gobrhcwQsXZmZqBq20f1fRBzzemG4sPJX4Uj52cjxB81tSu0iXEI7BYvSFJE0uWxQyd0QMjviHUMLoic2zZNmNVBEyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aab6bfc91.mp4?token=rbICBQBLIkIgx6In0QSgsnNt-YI1ScpxoCpdxZNVujnhWXZfhYUJA_CcAalz0-NbWt50K7OGKy9MjxDa2IdQW28z4KcxbJEbAG6L7lvIuXcOVN5oGPeRC2UpRxgXXmO_Xld125GEEldHtjXlAvduKPwTz1YjT2hTeg02AbDpfdFGDS154ZLhqtO0oUzLIYqpCE4KhqvxtNn5iBaUWUm9oMMDTMls6Q-sTaZ8d8btV3-Lw_RCA2-dhXocRh8gobrhcwQsXZmZqBq20f1fRBzzemG4sPJX4Uj52cjxB81tSu0iXEI7BYvSFJE0uWxQyd0QMjviHUMLoic2zZNmNVBEyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مرگبار کامیون حامی نیترات آمونیوم در مغولستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/667140" target="_blank">📅 22:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667139">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad1acec64.mp4?token=ki8nAtgmer4vZvXf4-zrrI4KCVexK4DFI1sEHa2R-AcylvlWppTx-_nKvkngiCMGG_yqbZyEDPhixOeOEP8gu-k2GSocV5hq4x9NXSGGCO2x_flxpiTRPWvhoqUWubPgCVNL_CzXKvETTvF0rwLzpXSuqXNNv-rrBBvWJNLmQIh8fRtxPcE805_PHgFRx9nHc2VSEJKNB7SYAGAh81Jv12YlNLwv516uGyV3W_cOJD8MmX5oUp2SIkDgveHguHi7WqZRMmW6Gx5B6ll1TNXo-gDLFjtUjdddQqJRGJXNXSmTwl92DoHgD1jH9v6FJPV4SnFHYrv40UtjY9n-f3VGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad1acec64.mp4?token=ki8nAtgmer4vZvXf4-zrrI4KCVexK4DFI1sEHa2R-AcylvlWppTx-_nKvkngiCMGG_yqbZyEDPhixOeOEP8gu-k2GSocV5hq4x9NXSGGCO2x_flxpiTRPWvhoqUWubPgCVNL_CzXKvETTvF0rwLzpXSuqXNNv-rrBBvWJNLmQIh8fRtxPcE805_PHgFRx9nHc2VSEJKNB7SYAGAh81Jv12YlNLwv516uGyV3W_cOJD8MmX5oUp2SIkDgveHguHi7WqZRMmW6Gx5B6ll1TNXo-gDLFjtUjdddQqJRGJXNXSmTwl92DoHgD1jH9v6FJPV4SnFHYrv40UtjY9n-f3VGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقایق پایانی مراسم وداع و خداحافظی جانسوز مردم با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/667139" target="_blank">📅 22:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667138">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=YHVdUTkcy32MSpJhxew6PFYXuOvlR4J8t-RMecv1eUQtcPxgXA5RZOVghYKcCKE-l1gIZmH6rVucJBhy9FAYgI4ybPLbdd8X27B4ntOEs1t_KZkClbhFY2L9N6Ba7G-cMuVSX_8im107X9hlI4LtXS-cVSOEKk_Qd5yFnD04z8TaXyFIkoM3y7YRn7lhBh1fDstqZ9jEk3-wn8bml1tapDtT43c9-_UWBju7lbWynXfrcE71OuqgUY8NXr0eMNx6VRsIr9rVc1TAm_y4A2x4bX7z7KrIU2IUWmP5rKwEARnm4EcEcHwM1BfdgEvHob7q7RaDozKiFE_He7tMPsX02A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=YHVdUTkcy32MSpJhxew6PFYXuOvlR4J8t-RMecv1eUQtcPxgXA5RZOVghYKcCKE-l1gIZmH6rVucJBhy9FAYgI4ybPLbdd8X27B4ntOEs1t_KZkClbhFY2L9N6Ba7G-cMuVSX_8im107X9hlI4LtXS-cVSOEKk_Qd5yFnD04z8TaXyFIkoM3y7YRn7lhBh1fDstqZ9jEk3-wn8bml1tapDtT43c9-_UWBju7lbWynXfrcE71OuqgUY8NXr0eMNx6VRsIr9rVc1TAm_y4A2x4bX7z7KrIU2IUWmP5rKwEARnm4EcEcHwM1BfdgEvHob7q7RaDozKiFE_He7tMPsX02A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران: حضور میلیونی مردم در روزهای اخیر، نشان‌دهنده دو پیام روشن است؛ نخست، وحدت و انسجام ملی و دوم، تجدید بیعت ملت ایران با آیت‌الله سید مجتبی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/667138" target="_blank">📅 22:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667137">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc53a66083.mp4?token=SWy-yxBYS_-M_5qAnHjHoej7WEkwoi0dn9ItpvAm1sfU9W--K4SWpvwdOXL3E6e7mC7Z8-KnUsrABxtUg5A11FlQgTvYUVRCt_KwYFeZRL_71ziNtxaBlAn_Yi5QqfLX6IqBM3G6ZoKmRjJTZUwU0BU7VGGw198BgR8Y82db4MljF_iQGXGiDsNkHM9gLkiTZV4DoHc2yQZVz6N0AULlLULDb36APmwdE-BxMwwLk6VkqhxDB3GrIzrmTgI2PDAzkrSOx0E4_XdH4HrwD2oQAVt16uOmWjH16wZDuq9Kxi4yKHucD8CEhZ-hI3DOIGDP9hQ4Tb38m1qHH9vpO8o5CFRVnontnu9ccSsu7cO3PToNu9-NBgxWmwt032leA69I52IIhgVmx_-64veRvhRc8V76rLUNsiP1X8HOSdrvWVOjbFRvjJ2eFwqD5IiE_tThjSr4p4qhIcB1Q8_9DdG7FSnYaWVW9Te8jBCisJelb87DqYtARCA6KhNBjpPI00I5J5icmWMbpAKNPiPWNDUK0Eq0RD2DyQYVTvYB4wIgnS1uAV4CsM4q7sOZXzk4k9JF9GmSrPqbvZqleRTQkA4rVJezfXZKjDIxZzuiSgKZ7g-e8NLE22owVyGwyHkQsYUQMlsXTXXwKgtXyFGMgkiw3IqbFx77t-2KlDqSZfv2MtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc53a66083.mp4?token=SWy-yxBYS_-M_5qAnHjHoej7WEkwoi0dn9ItpvAm1sfU9W--K4SWpvwdOXL3E6e7mC7Z8-KnUsrABxtUg5A11FlQgTvYUVRCt_KwYFeZRL_71ziNtxaBlAn_Yi5QqfLX6IqBM3G6ZoKmRjJTZUwU0BU7VGGw198BgR8Y82db4MljF_iQGXGiDsNkHM9gLkiTZV4DoHc2yQZVz6N0AULlLULDb36APmwdE-BxMwwLk6VkqhxDB3GrIzrmTgI2PDAzkrSOx0E4_XdH4HrwD2oQAVt16uOmWjH16wZDuq9Kxi4yKHucD8CEhZ-hI3DOIGDP9hQ4Tb38m1qHH9vpO8o5CFRVnontnu9ccSsu7cO3PToNu9-NBgxWmwt032leA69I52IIhgVmx_-64veRvhRc8V76rLUNsiP1X8HOSdrvWVOjbFRvjJ2eFwqD5IiE_tThjSr4p4qhIcB1Q8_9DdG7FSnYaWVW9Te8jBCisJelb87DqYtARCA6KhNBjpPI00I5J5icmWMbpAKNPiPWNDUK0Eq0RD2DyQYVTvYB4wIgnS1uAV4CsM4q7sOZXzk4k9JF9GmSrPqbvZqleRTQkA4rVJezfXZKjDIxZzuiSgKZ7g-e8NLE22owVyGwyHkQsYUQMlsXTXXwKgtXyFGMgkiw3IqbFx77t-2KlDqSZfv2MtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاموش شدن چراغ‌های مصلای تهران و آخرین لحظات وداع امشب، با روضهٔ حضرت سیدالشهدا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/667137" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667136">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ویدیو حشد الشعبی درباره تشییع پیکر مطهر رهبر شهید انقلاب؛ برای خداوند بپاخیزید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/667136" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667135">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
درخواست رئیس ستاد تشییع تهران از مردم برای پایان مراسم وداع در مصلای تهران
فرمانده سپاه تهران:
🔹
با توجه به لزوم آماده‌سازی شرایط برای برگزاری هرچه باشکوه‌تر مراسم تشییع قائد شهید از مردم عزیز تقاضا می‌کنیم ضمن همکاری با خادمان خود به مراسم وداع در مصلی پایان داده و اجازه دهند تا فرصت کافی برای آماده‌سازی مراسم تشییع آماده شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/667135" target="_blank">📅 22:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667134">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02553b7c3e.mp4?token=HE1-gDV5_6PI5xddjOvoQ8-3QH6C_rY0QcoZ-dKhQDyQm2WZLOVSuOQvV1WEBHBbXVLgOvGzVBxJhkZtn-i3C68-G0pG8pBySsDWiX_6Nc1Bq96dgv-VxQ_YR1SBsEH24qFA_ZMTqYMXmBx_IvDkLleyJQnYQAGnt7CJhfp2rJYsnwZQeCyRim_NgGsSq1LKfiyoPzSbNY05KqvxL-U6vvIUY5NeGCj6WPesZ8aquLsYwX3fgCdl8yaOJU0nx3Vm43Gvgh-u3Q5nASV7AtaIXN2Tn7IlhVKdmnzv0A9FTjt4YazkI6Ue6UMBoYnIhXPzkKH74-RLWp2UUrsrVVFym2w5KVzPV9LpNcMexZAch0EZBSy6Z_dAL_-QpGgmFFyKr-H1E0uDrCzkdKCr8U9DWJ9xIzcaN9pKcqxQhmm6KaFQXWvR-LVN3v1_EHouQt4CE0ho8TCA36TPNiLvGcLF6WU569hxkao2jlscmhXuGEjqlYqrhTYEm_VstkQ_w73_-YcfAKYnBzKnBw0mxGffjkX_odAQ9UJkwJYbTNUz50hJcFSWa3VlHbkJdjWPhtOxx3fwJr9X4SZsj0Jx61XlIIrbi_OsUDTAvdb_Td1GW6DRgeuLgO0mkKBs-D9w6cpUEEo4a2cQZCVRHNVBXy9L1riNYvnQ-lHoht-ia16JiYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02553b7c3e.mp4?token=HE1-gDV5_6PI5xddjOvoQ8-3QH6C_rY0QcoZ-dKhQDyQm2WZLOVSuOQvV1WEBHBbXVLgOvGzVBxJhkZtn-i3C68-G0pG8pBySsDWiX_6Nc1Bq96dgv-VxQ_YR1SBsEH24qFA_ZMTqYMXmBx_IvDkLleyJQnYQAGnt7CJhfp2rJYsnwZQeCyRim_NgGsSq1LKfiyoPzSbNY05KqvxL-U6vvIUY5NeGCj6WPesZ8aquLsYwX3fgCdl8yaOJU0nx3Vm43Gvgh-u3Q5nASV7AtaIXN2Tn7IlhVKdmnzv0A9FTjt4YazkI6Ue6UMBoYnIhXPzkKH74-RLWp2UUrsrVVFym2w5KVzPV9LpNcMexZAch0EZBSy6Z_dAL_-QpGgmFFyKr-H1E0uDrCzkdKCr8U9DWJ9xIzcaN9pKcqxQhmm6KaFQXWvR-LVN3v1_EHouQt4CE0ho8TCA36TPNiLvGcLF6WU569hxkao2jlscmhXuGEjqlYqrhTYEm_VstkQ_w73_-YcfAKYnBzKnBw0mxGffjkX_odAQ9UJkwJYbTNUz50hJcFSWa3VlHbkJdjWPhtOxx3fwJr9X4SZsj0Jx61XlIIrbi_OsUDTAvdb_Td1GW6DRgeuLgO0mkKBs-D9w6cpUEEo4a2cQZCVRHNVBXy9L1riNYvnQ-lHoht-ia16JiYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرده‌ها بسته شد و پیکر رهبر شهید انقلاب صحنه وداع را ترک کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/667134" target="_blank">📅 22:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667133">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تعطیلی روز شهادت رهبری و تشییع در تقویم ملی/ سیاوشی: ثبت تشییع رهبری در گینس در دستور کار قرار خواهد گرفت
اسماعیل سیاوشی، دبیر کمیسیون فرهنگی مجلس در
#گفتگو
با خبرفوری:
🔹
روز شهادت امام شهید در نه اسفند یا روز تدفین یا هر دو به عنوان روز تعطیل در تقویم ملی ثبت خواهد شد و این موضوع در حال بررسی در شورای انقلاب فرهنگی است.
🔹
قرار بود که مراسم تشییع علاوه‌ بر کشور عراق، در کشور پاکستان نیز برگزار شود ولی به‌ دلیل برخی مصلحت‌ها صرفا در کشور عراق برگزار خواهد شد‌.
🔹
در هفته‌ای که صحن علنی مجلس تشکیل خواهد شد، ثبت این تشییع باشکوه در گینس در دستور کار قرار خواهد گرفت.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/667133" target="_blank">📅 22:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667132">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9295861970.mp4?token=otzezvGHGonPn2bUmqM9ICxB-iSkwcf0k3zwVIutGLgjO9uCfFyRQQWRl7c-tznYpMKE1roy6_tVVp0krmTxJ0Es1FPG--m5FrLN8BjU6AGdxW9Jl1d87aqWSQ9rIjiPht0Y-c7lew5wuyjQygBANQYV2Vznu_1dsbUJ8XLYn_hycEqsi8Vxz2l47lHv_dI-4pwk-7_dlCtJRgwaSzRAghZRkNi-c6Tb5RxnReDH9C8_yTmIRj2mUdiKzyt1wie6Wlw8ZZD39Zg69HpIzCGa-b8Ztn2axhWO3VT62cCnEuWVDSexYQWj_EqKwnF8TRqjjkNaz7LDhq8zTIUBMzX2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9295861970.mp4?token=otzezvGHGonPn2bUmqM9ICxB-iSkwcf0k3zwVIutGLgjO9uCfFyRQQWRl7c-tznYpMKE1roy6_tVVp0krmTxJ0Es1FPG--m5FrLN8BjU6AGdxW9Jl1d87aqWSQ9rIjiPht0Y-c7lew5wuyjQygBANQYV2Vznu_1dsbUJ8XLYn_hycEqsi8Vxz2l47lHv_dI-4pwk-7_dlCtJRgwaSzRAghZRkNi-c6Tb5RxnReDH9C8_yTmIRj2mUdiKzyt1wie6Wlw8ZZD39Zg69HpIzCGa-b8Ztn2axhWO3VT62cCnEuWVDSexYQWj_EqKwnF8TRqjjkNaz7LDhq8zTIUBMzX2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام رحیمیان: تنها مسئولی که بدون وقت قبلی می‌توانستند خدمت امام راحل بیایند، رهبر شهید بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/667132" target="_blank">📅 22:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667122">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf6YoVQk6FfUNG9Xk0vAo4qtkUkeV3YAq73sZOiKLzxdrBU2Ym_Q-Kf0hvSDNB-Jyw8oCBYj19kkS5CdkyY2A33Ibv7MBfG661Pz2PRFTz1xnr-4jOVydS_Vl-FiRtY99-nieKikR4SWMl7CoXuZuBhqkS0-tSmi1atlUeWM6md38aMCcLqTlo7KYAsjyxYL4KFUVGZabpZuTd-Z99IwjIr23MwMdTzNtL1on_I9UFq0-PNGdPz-lWbbirgre10pK_SGIx-hTPWZRW63zKvQA2b9KWe0kusEdwdXqyovwsSyOcto7LcNqUNk8v5qRqRfGzwUfGtZFzjlBEcwedPRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmPO5Um6d2PHpFx6DQJ_vWbAjGXoqFpCEjspJJhn93NOu76y-Erx5h2R2__EswzjVo5MpLVgBx7xDWmAoF9AtuR8UWR1uVVhEk00e6SXgepgyG_uSHdikPUuOcg6w0unvu1Sz4A-2PfGs_csPSWdpKbX4W06LBICbRaU_osq85qo5ObhLtCFsD72L5gELrnvOeDIiset2BwurUZl3YO7AIx7TKngig76AtfEVGEO7g0QES2dyTydgSFoQWacZA0YwLoBJlVV5dcL8-jVaKXdisg_w6f5ouFW7MHZuMUAHA-LzzSaCTvbo2cMkZzLIKk0_-yLSSrRA3StiRxET0K90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRSIEQCY6NdWlrdLuS8rCau_VLo_XF8lN8GdDG7p1tRLPm1NIV4A3T0QZIHqMHiCuqKOU5f3ePgkmQWZjAdO6OMNqxq0rc-KM1cPGbsX6VnwofBQkTAtwr96F1Hz8Pir7iner-RNKHpeNzLq-ZT5N3vTY_G07c6OxCMP_EDXXNTIvjzLdYZBE0bHZ85C-BI3XOL0ySVRmGgdNvuc3oQzE9IDkMUHt3nneppvaGpAGV2e62Tpz-O08oBCB21-3Qy1ET3qT0tU-b1By4jQHFsDUNbyYDQQvGn7byu6CjH0xuqtzIsIlZpRY54jsQmrNMCbEy1ZmOiuR-L06sikZcdHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMkLji38lxzj3DDJRk59A6eZCufEpdTAQv5scVsHBhEEszq2o_1BJoeDX0bIG1uCEoeS8nFU5P3gd4dX8jUAM8Vx9oxoqhEP7zIFVk9Y1lvHm-GiztY81oAgnNC7ZhtH1hz3Z0DhwGsVZofOBZdByv8iE4xhA6nSa55A1QdxfBVjT_ABIGHZlsPeDvRYLWqwahjucul6Ry2z11KP-L068fPfywKThgxVxYuz0fAVWdKeCBZlTPFWfr3f6NXqZ8vFkAgc4UWLIiGG_vZfBjPlAiWJLxtwA9lzTfBRliUyyMPvROjvM6ucJScVSx1X5CoDqNZE8F-uNMERsg4ZqqRzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_yzThXuUO9rX9FaTM2AMCdcBAyu42KPKuBl3AJvxryi-ZUfH3CEDVDCWtFBFUY0f8ln3J8CDgT1LlNiM3QQfxVlcPiKcB4CLr8rxRqR5s3XObvpK9VKur6iV67IaYmPULb_GKSfQKweiXMj93MXaKB0EqTQYlpOWd7gUSQ7UkV1-y_dpBXl4JBJ7dqW6511UMvNMMQQmGbx8rfa_tai8sK2bQBwJBQXqb7M_F9ax-BpuC_wkjn0TGEYtRsEg4jETFTgJE2o15DX140OPZimsNf6yheaU5zY-pFTEDMdAHa7GoufYbq87sk1pe493vRFj2PToFVrmdzBtzvv6X9VjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSsiwEaVSAyUec6ui2mWZ1SKqDiK0LFHSkXMNBgwKhXjTSB0GzoI9uX1SbAtr_KGhOJDq3EWMpo2SsITSTCx5afUstwzhnLtmsdIzydQY9QUbP5SBTvkvBgg-zMi35suR8J8tUZdDCQZsgaU-KwzcpOsIUpOR7uS2uvSTRnxDHUEAdybSMan1F3sRe92-CiCNVcOLcGJ2BQVMhns9hwjIsuG7EZvjvGv1mXddGnSCVobCad18h_Fgc4uc1b1apzvNXEPVg6kCASA190-1XLRI-DRpT-R9l_xZKhhL0IsheCL_aKDIlyKsGg0xhCZ4VfN5yC7uwGo1odfluvCY8Ur6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJEc0hbEowqh-kUoYOhWgYCSqLIB28FCd9yCtSjj8cKPQl2Z5VsiCzNU_4st3ZFaUVJli3OY9pdgnELGJyg10LBfzJFYgr3glcyUmioBKIoxaPAA56bGkTBxafCHbMRBy2cJtdf8rkNCiaHa99xHEFeAX3_QsoPh-W6PjpiMHWwYramqQ-jSuM4hCHVUlPHgHEWmIOFPSRWfD9qRnFdvPcnmzCZXZ1bO0uxXLJYXDlWOd2retkMTBdc0SQGtv-2ISi481BZ4ilj17ZqlIDcef5Qn-I4XSmhSljuIW4uyEvLbDXTgn6DloQx-DRv5gxRFCZ4PZxrYyutJMJoA9BS7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbeCsoJNGEL4P7Tho_pwvBuj64-mZ6JAR9wumB9NP2Jk35CrdsFl3M2v-rP7xZhQmobolLuurgY5NH-UFdLKMfYnzoydz4l3EtxVwV6rSFt4p67BilhpK3i_d4HKsaXRjD-5iCBXMyFlHEjojNLz7po8gvYQV9Do5m6fq5hbe0syC9UIaUobm1kJDgts725E3B1YGgQGYCIWzt6einbVP7UwPDdsUdJvYQjrOLeDTJ2rOFsRLhTI1CQAZ7EJKtMvX4us1OaGxz2zx7800_VPAH017Ht3yl-S32XVcU90Jnh5z8sAO-EP3qAEYvUNqmELMfjCsfPttkIftL3y_z82aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFW1Xwk0YEqCMcF3q-BK4GlrlRO0RlH8mTqCLlHbIMxUkG9pNlG7IHicYsUUf6MM6AhRAcCCon_XYKInIGHlSXEdJ5aE1c2J7n2cS4v1tUY0pNmXymagRlNLlp81C_1fNC9tYy7YO9Lq3R3gT168tvueuYUA8_5xlwiQw6xAp7R0TqjVQUFEe9R7Hnr311UEJQJdXaGnVYcieniDaqyRPPEok9aSPVnzNsRua-KvOiqPdcaedO9uAx-FQXGeygQKVzEci690lKP98FzZWD3KSBIkr4bk3jjSoqmp4N7HOD1cW-Ez3WNUFTlDR6gW8ji9EBG_15wA9MZgNKHjvLywBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5c5ok9snbTsop4qd9Y2XNvzanlMSw8MZWYZlCTmZm8o9hgxv5PTbovJJOdU_gOv4Gf0KLEemsAEsfDERiF2wCZrbfwCS9PI2vMUzeP1nG2Jf-yAtQx1Pd7Se6-Vdgt16eDJM3BZtm-Af6QrZ4mdW-HrAzNTwanOchwtTvyXCK3noBI146_wA_eI7l5igwhzv1sTAD0wjU_mVrOQkwxSlT4IoPkvnUlze3gYqHrAue1UojsTc61kou4fx0ZRFAO82AD6ByImCO_l4O6S87rP43utSnrCcJhQvjvDJT8JS3Ovi6AvSJLm5tzBnUVwf6fQu1Klz4xV08LRN-gMfbji3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از آخرین قاب‌های وداع
🔹
عکاس: زهرا دمیرچی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/667122" target="_blank">📅 22:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elzqj789zpZ_BcfQmVwB5634ABlatec7q1ll6_kN0AiG7tSPaQREQLmUVvmMwFWqwtmr5_mcIXbOJDZpCZeCyJHSuaSfRafE6mzSfF2RW8LhhDrxE-Zda7mbImxIsKYFrU4dKU1i3p4K__PSp8T0MmRlahVRxKsosSBGugRYxPPHpFfCNDFSOVllLZez9Ll_ivcQVxQx_yPHiCdlSmvnyzCp8jFa4neYVv47_pQepcjbfw1ZButzCTm0bPcegezh7jmyDbeMjIZvKhk5dAYUmhFJwylQo5JIDL_vA_qn0tDDeMp7aM3rmXdzHjgiYlin8i68AkZ4z72JQFM1EjKxgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت نوجوان ۱۶ ساله فلسطینی در اردوگاه قلندیا
🔹
وزارت بهداشت فلسطین از شهادت «ولید ابوسنینه»، نوجوان ۱۶ ساله، بر اثر تیراندازی مستقیم نظامیان اسرائیلی در اردوگاه قلندیا در شمال قدس خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/667120" target="_blank">📅 22:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB-g01J3o0U5_smbmIAntynJ5Q6MCWpTPrGL-rv0kFR253NyG7SwVkVTPV0agXJOyP1sLS8RnkdWrEmm7bi1hMgVQ_uUqDR_Qw0UoxDcvKCjpTI634Ev__7kUFEfFlN3FlMZyvMgirN1z5u-Cm_BmFOJ3SXBlGYskerkUJEGdlvQTLzglxsCzW5T9kf1-XnsOwEGfcUVftcuS7phd4QMAmtyhEw5UT7X88xdd4I9jnpATSBGf7uu1sT24sT44PJFRVHY3U25qs0gaDOmIQGBfud1qyfzOJID5GJYAgFEiS26UgvWlEut73C10sD5ab3VbG5nQ2MgBOw6Rj5C_uAX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/667119" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTX_zlrJ7ieHjG6uM09oVrVkm9T-iqydRjIq89P5IS95ct_wIP0AxWe8PVPoq9ultzTo8SZj38FrULOAgf2eZuO-pngYS0OY9MH1GZsO0k3e5H2Wm3eTpcJAKB71ukEXQWehCmBxL7Ybj4vk6mkDbqsmpngASbX3I6v7-7DU1wP-rnRPci9VrZ71J8jlgjFgPguO5Jq8o994YmLZkix-HX02lGLrXrt9Rc1Ul0TCsd4n23H_a-knnJO4rgWlf332D6BUe-TYIPamLSFk1BweQ5-qTEIpYy9TUqBE0GSvdFMXN6z0aMv99yfIpNrqcm0YEkYPkoUWZ7sCS6ybX1dGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه فرزندان، عروس ها و دامادهای رهبر شهید انقلاب را بشناسید
🔹
رهبر شهید انقلاب دارای ۴ پسر و ۲ دختر بودند: سید مصطفی، سید مجتبی، سید مسعود، سید میثم، سیده بشری و سیده هدی. حضور سه پسر رهبر شهید در مراسم امروز وداع با پیکر او بهانه‌ای برای مرور زندگی آنها شد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3228099</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/667118" target="_blank">📅 22:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259b338fe8.mp4?token=jqYv-170fm3JGGarPq4fXrjakL17pSm24TKiA4Nxv5s8F5J0-52sKORqA_ss0ieQ5kmgnq7NgsUuwTguMbRgElusYnqVlgfnsNxSyLAw4dX4NiLi56Uuqzxpg7DIl4unM2U1-LqfK1oWcoNsXqpv3NLYq_cp6SiUL9rCAyU0S1Ryz42jktBGbSlQPUmg9JiWvnY_AS9Bm-dfr_6E1MpJMroMOEkVzBDoPBK8va-vLZPiN0MuOFb6bpHixW9sRsHikuo-pG_COi17e9x_ixoJQZbA-ph43VQc3fixdBRiGLFqqGoBrdhICQ4uOShs6T2YwlEkxQBtnC0hiAXRUy1jEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259b338fe8.mp4?token=jqYv-170fm3JGGarPq4fXrjakL17pSm24TKiA4Nxv5s8F5J0-52sKORqA_ss0ieQ5kmgnq7NgsUuwTguMbRgElusYnqVlgfnsNxSyLAw4dX4NiLi56Uuqzxpg7DIl4unM2U1-LqfK1oWcoNsXqpv3NLYq_cp6SiUL9rCAyU0S1Ryz42jktBGbSlQPUmg9JiWvnY_AS9Bm-dfr_6E1MpJMroMOEkVzBDoPBK8va-vLZPiN0MuOFb6bpHixW9sRsHikuo-pG_COi17e9x_ixoJQZbA-ph43VQc3fixdBRiGLFqqGoBrdhICQ4uOShs6T2YwlEkxQBtnC0hiAXRUy1jEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات برنامه اقامه نماز و تشییع رهبر شهید در شهر تهران از زبان استاندار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/667117" target="_blank">📅 22:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سی‌ان‌ان: تهران مهیای بزرگترین مراسم تشییع
🔹
سی‌ان‌ان تهران را در حال آماده‌سازی برای برگزاری بزرگترین مراسم تشییع توصیف کرد؛ با وجود گرمای شدید، میلیون‌ها نفر برای وداع حضور یافته‌اند و آمار مسافران مترو تهران به ۱.۳ میلیون نفر رسیده است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/667116" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cd5a04c8.mp4?token=h4BzrqxtgW86UDHWnINFPWX9Ouavq9qJ5mx28s1IxhXinEMSYAr2-ExNGhbAhHP1-Dm0Vh_43LZ9Po7MFucCAEDBwICgadLDqnGL5qvlq_Ml7PgOG1wucmSV7fj3w9IkJEHEJKWkRnp5vxtzRgLHX9JOhB7Nri5lfpbGKFthImP21ATjrowr-bAHmo7yhApraqwlUfFV9C3efJ5ay6jveksm94r-oLaypfkVpNFTL1echytBXd806yMFQtS1N1k1nRFSgq2AQPY0w_HUhEErbJ_rGp2D5-Bf_nc08bDpdx1OLR7gx2z_ieZVwAIDXfCYFcnj1rCP4gs3cXXwef_2pC_lcmCySPoeZg9gMqN7f_v5jBJ7Y6ejwJ5mkuwah0dtgkWu3yHHF815lUhCFVaDCY32QvEE_EqFBUr5_uMmhLQzt5AZhK9X0P3HHPVRz7l3W0Ib6_-rdev36Fvg7Gwa3IJ_3SA7J0B9tDCs2T-UQqFr6yxY0tcX5Ro2toiebkjRGI6dWX6-k_WPp5iiwB9kZZPlWYy0z7xuJ0hV1bY_j5Sw4Xi7rTH9tOp-S_lYYcPyKXm9oChoM1mVcEkfdQqNKiejYCTcq4Y9N-1pij6xGvMgbfW3RUFNUIxzkqp1FBw-8y8eIBAgpE90TT5i1qtHULSwrGwx4vEBpTpiV_9IzoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cd5a04c8.mp4?token=h4BzrqxtgW86UDHWnINFPWX9Ouavq9qJ5mx28s1IxhXinEMSYAr2-ExNGhbAhHP1-Dm0Vh_43LZ9Po7MFucCAEDBwICgadLDqnGL5qvlq_Ml7PgOG1wucmSV7fj3w9IkJEHEJKWkRnp5vxtzRgLHX9JOhB7Nri5lfpbGKFthImP21ATjrowr-bAHmo7yhApraqwlUfFV9C3efJ5ay6jveksm94r-oLaypfkVpNFTL1echytBXd806yMFQtS1N1k1nRFSgq2AQPY0w_HUhEErbJ_rGp2D5-Bf_nc08bDpdx1OLR7gx2z_ieZVwAIDXfCYFcnj1rCP4gs3cXXwef_2pC_lcmCySPoeZg9gMqN7f_v5jBJ7Y6ejwJ5mkuwah0dtgkWu3yHHF815lUhCFVaDCY32QvEE_EqFBUr5_uMmhLQzt5AZhK9X0P3HHPVRz7l3W0Ib6_-rdev36Fvg7Gwa3IJ_3SA7J0B9tDCs2T-UQqFr6yxY0tcX5Ro2toiebkjRGI6dWX6-k_WPp5iiwB9kZZPlWYy0z7xuJ0hV1bY_j5Sw4Xi7rTH9tOp-S_lYYcPyKXm9oChoM1mVcEkfdQqNKiejYCTcq4Y9N-1pij6xGvMgbfW3RUFNUIxzkqp1FBw-8y8eIBAgpE90TT5i1qtHULSwrGwx4vEBpTpiV_9IzoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب عزاداری خودجوش نظامیان ایرانی در CNN-News18
🔹
شبکه CNN-News18 با انتشار گزارشی تصویری، عزاداری خودجوش نظامیان ارتش ایران در حاشیه مراسم وداع با رهبر شهید را مورد توجه ویژه قرار داد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/667115" target="_blank">📅 21:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
توقف دو روزه سامانه‌های «ساتنا» و «چکاوک»
بانک مرکزی:
🔹
سامانه‌های ساتنا و چکاوک در روزهای یکشنبه و دوشنبه (۱۴ و ۱۵ تیر) در دسترس نیستند.
🔹
خدمات کارت‌به‌کارت (سحاب) و پرداخت لحظه‌ای (پل) همچنان به‌صورت ۲۴ ساعته فعال خواهند بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/667114" target="_blank">📅 21:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a9c5b3a3.mp4?token=jvigH2jGa7WTlUuOCIxzo08j66ZpMf7yj-dTgRj0HL4NvO4UG6W43I057OxRg0MMsIOcGpAEug0pU6-lD6eMBI8LBWRIPc5QpEkbaolKVTp2ib03-7dH3946NjkuJdMT6eiaQeheZdNM-IFk5wSuJlbncCWJxQ9bdw76Oqz58cz5WS8jBkH92MkuVXSzeEhOZKRFAdbB1GDFcuSdLInKqcTiJYKhKNK23f7MpcUhM-3s1KZY7ct5iXec0tz3_aJK9GVSj30EQw8qpnjabVg_Hw5P7V59vOavAbx6TQeCES-E2XQje14YBCXkOG4FKd4NHnKTdrGGZIhXF1lIPirx6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a9c5b3a3.mp4?token=jvigH2jGa7WTlUuOCIxzo08j66ZpMf7yj-dTgRj0HL4NvO4UG6W43I057OxRg0MMsIOcGpAEug0pU6-lD6eMBI8LBWRIPc5QpEkbaolKVTp2ib03-7dH3946NjkuJdMT6eiaQeheZdNM-IFk5wSuJlbncCWJxQ9bdw76Oqz58cz5WS8jBkH92MkuVXSzeEhOZKRFAdbB1GDFcuSdLInKqcTiJYKhKNK23f7MpcUhM-3s1KZY7ct5iXec0tz3_aJK9GVSj30EQw8qpnjabVg_Hw5P7V59vOavAbx6TQeCES-E2XQje14YBCXkOG4FKd4NHnKTdrGGZIhXF1lIPirx6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیتی که تاب خداحافظی از رهبر شهید را ندارد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/667113" target="_blank">📅 21:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024795ab39.mp4?token=Py9kxumtzNCGIKmLhjbbVtUPhJceW0bS-S9FdFuLJxF04lSgFIgRroMtwEM7qrz3Tse_tjgAMcFZjWRw_VDtYbXmooL0JZf0j1RcieMrnHVPm25dz7aluhGatQIr0QjIYZZzNE6EvBkBjAh_MSTx5bNJ4WKfHxBR52yQIZ0_-eoYwCwWUDXQGtP3uAURpQrou3QzLS3Rb6VdWHShkFkRRNdh0z-uJh0gQgXYAvwUVNYlvz0HsP6psDP-bQrNwVlAmuzcjus9hmc4WIRKuAfYKMUaOKDCHkJu0omSpHz8CLyUmyieX0nVwISa65ntowzrjH2FfmBBh_bQGmToE8-WkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024795ab39.mp4?token=Py9kxumtzNCGIKmLhjbbVtUPhJceW0bS-S9FdFuLJxF04lSgFIgRroMtwEM7qrz3Tse_tjgAMcFZjWRw_VDtYbXmooL0JZf0j1RcieMrnHVPm25dz7aluhGatQIr0QjIYZZzNE6EvBkBjAh_MSTx5bNJ4WKfHxBR52yQIZ0_-eoYwCwWUDXQGtP3uAURpQrou3QzLS3Rb6VdWHShkFkRRNdh0z-uJh0gQgXYAvwUVNYlvz0HsP6psDP-bQrNwVlAmuzcjus9hmc4WIRKuAfYKMUaOKDCHkJu0omSpHz8CLyUmyieX0nVwISa65ntowzrjH2FfmBBh_bQGmToE8-WkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سازمان آتش‌نشانی: در صحن ۵۷ هزار مترمربعی مصلی، سامانه‌های مه‌پاش برای کاهش گرما و رفاه زائران راه‌اندازی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/667112" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
♦️
پایان مراسم وداع با رهبر شهید در مصلی در ساعت ۲۲
🔹
به‌منظور آماده‌سازی مقدمات برای مراسم تشییع فردا، مراسم وداع که هم‌اکنون در مصلی درحال برگزاری است در ساعت ۲۲ به پایان می‌رسد و زمان پایان آن دوباره تمدید نخواهد شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/667111" target="_blank">📅 21:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3fc9fe1b8.mp4?token=b32cS3V2Lu4CVESIxYLjiMPqevnpQvfRz1ZYEiqeIfAQZLO_vJzfHdtoIAzvzxaEnoBRh0z45YxDv4vChh74_uO_TcsHvGmiJVKN0HZEQEhrbJGOzrP4eM1KYCqLauOyR7S25ttIZa4VYwp4jzA_fT6YAhV0NSJJGl6XXlYqaBfBHjCV6iXg8vvj-96caP_r8d7z0nT_GNdACJDjv9kU9WgTvQBiuw6Yai1fqcuZhcP9iupjtTKbqxedYxgfjN2eePN9GEcGXzVIeePGn_R7WSGGsZvYMFIThIn-Jyj5wNRxpAIgPoAbmxruSwbtDsyAAlUpSD53j4YXkpvmV9qjtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3fc9fe1b8.mp4?token=b32cS3V2Lu4CVESIxYLjiMPqevnpQvfRz1ZYEiqeIfAQZLO_vJzfHdtoIAzvzxaEnoBRh0z45YxDv4vChh74_uO_TcsHvGmiJVKN0HZEQEhrbJGOzrP4eM1KYCqLauOyR7S25ttIZa4VYwp4jzA_fT6YAhV0NSJJGl6XXlYqaBfBHjCV6iXg8vvj-96caP_r8d7z0nT_GNdACJDjv9kU9WgTvQBiuw6Yai1fqcuZhcP9iupjtTKbqxedYxgfjN2eePN9GEcGXzVIeePGn_R7WSGGsZvYMFIThIn-Jyj5wNRxpAIgPoAbmxruSwbtDsyAAlUpSD53j4YXkpvmV9qjtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به رسم همیشه که در دیدارها کف دستمون حرفمون رو می‌نوشتیم که شاید ببینی و بخونی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/667110" target="_blank">📅 21:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c400f5c86.mp4?token=DNQA7LqYDWVBhusJ5BzSuqyGjRt98LKfZhYnuBmVcf1apptkxLvjkIvUkt7kfz6voEBaZSetCaPRTM4XrtMmQhW6x8pmpBpccFdNvW5xJEFwO-ewfwHeAARszJE5zCKs79Ophnf8twvOBuPsZ1w6ayAscEBxZ4x2-ctbqbPU6XckqktqJI2ytsLmmMeB4ozwvz4K7dR-wJwfd_D2LOAup-CQGOC8QXJNtFgbx5VaV_9nfZVfFwgqfAKm22tolg3rmTRvP4tAm9cqlnfzs_rdbJB-dRftb0W9Dox31NBZHppEQAdqxF-X9AzuStwWzSV4YGQRsMTVJosGY5CPAB6tGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c400f5c86.mp4?token=DNQA7LqYDWVBhusJ5BzSuqyGjRt98LKfZhYnuBmVcf1apptkxLvjkIvUkt7kfz6voEBaZSetCaPRTM4XrtMmQhW6x8pmpBpccFdNvW5xJEFwO-ewfwHeAARszJE5zCKs79Ophnf8twvOBuPsZ1w6ayAscEBxZ4x2-ctbqbPU6XckqktqJI2ytsLmmMeB4ozwvz4K7dR-wJwfd_D2LOAup-CQGOC8QXJNtFgbx5VaV_9nfZVfFwgqfAKm22tolg3rmTRvP4tAm9cqlnfzs_rdbJB-dRftb0W9Dox31NBZHppEQAdqxF-X9AzuStwWzSV4YGQRsMTVJosGY5CPAB6tGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر محمدرضا کلانتر معتمدی، پزشک رهبر شهید: رهبر شهید زمان جیره‌بندی حاضر نبودند بیش از جیرۀ همگانی استفاده بکنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/667109" target="_blank">📅 21:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NItlnBB_zSADIwZcRJ6hFd8VL9_1eqKmBM3HXineBrY-ZpFpCowizCb0H8Fsog9IYCucK3-9qmP5lmNDgCA1aektmM6m0inW58M0tLA6DteQgLzg6ShHU_JI8pHzuoGeh1waW4_a2DNiZqeLj3t3VBj1FzLLos1h0xsamzlEJG6yVRbtIdQkF5gKKOpipfRmg-4Lq-XRFol36abZuoRESTPaYVJC_HGBw01L0DVIVCsZ5NEqWjWXK1681-cECcbMKnilb9-qUStl-6ffIt9CFKbToiWes6aZh6m3RWb6hgS025AEVx-zMatynhIf-k8zbH59bLTf4ZUxk7LC1_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اللهم انا لا نعلم منه الا خیرا
🔹
مردم عزادار و سوگوار ایران امروز با حضوری گسترده و آکنده از اندوه، در آیین اقامه نماز بر پیکر رهبر شهید و عزیز امت شرکت کردند. این مراسم در فضایی سرشار از معنویت، وحدت و وفاداری برگزار شد و حاضران با اقامه نماز، ضمن وداع با این شخصیت برجسته، بار دیگر بر آرمان‌ها و مسیر او تأکید کردند. حضور پرشور اقشار مختلف مردم، جلوه‌ای از همبستگی ملی و احترام عمیق به مقام شهید را به نمایش گذاشت و این آیین را به یکی از ماندگارترین صحنه‌های بدرقه رهبر شهید در حافظه تاریخی کشور تبدیل کرد.
🔹
هفتصدونودودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/667108" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
قالیباف: آمادگی برای جنگ، شرط مذاکره قدرتمند است
رئیس مجلس:
🔹
تا زمانی که برای جنگ و شهادت آماده نباشیم، دیپلماسی قدرتمندی نخواهیم داشت؛ چرا که دشمنان با کوچک‌ترین نشانه‌ای از سستی، به جنگ روی می‌آورند.
🔹
وی همچنین بر لزوم همکاری کشورهای اسلامی برای خروج از سیطره آمریکا و اسرائیل جهت تأمین امنیت و اقتصاد منطقه تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667107" target="_blank">📅 21:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس از حضور ۱۰ میلیون نفر در نماز رهبر شهید انقلاب خبر داد
جواد حسینی‌کیا، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تاکنون در تاریخ اسلام سابقه نداشته است که ده میلیون نفر همزمان در یکجا نماز برگزار کنند و این بزرگترین نماز جماعت تاریخ است.
🔹
به دنبال ثبت رسمی تشییع رهبر انقلاب در تقویم رسمی هستیم که با باز شدن مجلس پیگیر این موضوع خواهیم بود.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667106" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnQjLeM-4QsLOxpFmEE3glWBnsRLHKFPdBjGq4_UoTYEPCeZ9UTdHjlVtX4CXg-yZxYAcE_zAMixb7RmwR6O5CfoCFE7TrPYWw6zhQfMNEPCPFpWWJd3M3RuRWPm8GNy62pv860o_TmQCHMPeP94ApNsQwo0TcQuA1qGHe1rKro8VVFUyXrdNvZXo2ci_tA4Wmi9irzrfk6-3z00uGrROi2V7YvpWesFMuDn-rhfMxAPKBAZtlc3ZagxyeEl2uhC-AfOrbylGDFpJYhEhDgMG8RHi-Z1b-IGCWj_xoieCLp4jX1c-daS6rtWd7MloTVbI4767Sqy5lmRxti7KsX-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
پویش ملی «آخرین دیدار»
🔻
جهت ثبتِ تاریخی وداع با رهبر شهیدمان، از کلیه علاقمندان دعوت می‌شود روایت‌های خود (عکس، فیلم و دلنوشته) را به شناسه زیر ارسال نمایند.
📬
شناسه ارسال آثار:
@akharindidar_admin
🎁
هدایا: شرکت در قرعه‌کشی ۲۰۰ جایزه نقدی + بازنشر آثار منتخب در صفحات رسمی پویش.
🇮🇷
آخرین دیدار در بدرقه آقای شهید ایران
@akharindidar_ir</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667103" target="_blank">📅 21:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
فراخوان مقاومت عراق برای تشییع رهبر شهید
🔹
ابو الاء الولائی با دعوت از مردم عراق برای حضور در مراسم تشییع، آن را ادای دینی اخلاقی به حامی همیشگی ملت‌های منطقه دانست؛ وی تأکید کرد گام برداشتن در این مراسم، پیمودن مسیر تمامی شهدای راه حق است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/667102" target="_blank">📅 21:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667092">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7HrCaDp0EfkSoyc9Mlb7oRLueh1eWnvo8ErYHlTioZgP9H1drdOl_kW3Yo16l2wh_khQjoNxXdR5UovNi4ND7m79gniKi5p2iwArtZMQRaKdbxoa-ACfT6aZWWO8RwH7vjWjvaL63lJP_ZAZvL7p19su-DKm-ARCmQQTVXXepEIhiUtTMg4Vxg73SNl7T16_AFhI7MAyAwugpUrdV5Oq2hlRUKvg2JPDc4olLW4NICj6I7iKx3ael44hQ0Xq0V6wdhLMcM_rGa7mBOCMCxg_KA9SS7WrDxKotwt83xhRlqRucT0UID9MJbZXRaWU5GYRMQEVWfST0t6YAOB7SkRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dv6xms9hTsFp6S7gLMyQZlEo04KGmQkZXgPNEsvPkw7c0gPo4iCa59fXvI-YAnd8fsZd2SGYgk1nqG99qXpf2B0NILocoiWyssvWl0o5OXFwg17haeiAftHT8SvnEFMMHana-HKPGUau93kcJP8SoA3eOR2iEftnkuClAsnDsFq7akP00DJgNRTDTZZ8Rd7FUSBuc7VMVq8uxvfyZiivN5gQiUUjzSOjLDaD0GpOikr9OD9zgjF0aCQplz3U1o8vcBzlVpuGzGfHnQD1uRBVLYQkBZiozeJ0KC5oZ47QgnbmjsFtUJXfSFbN7Dapa10opecVGcERrZDrtvlw-tN9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YESQLgquApgR5Nous6mr9m-Q1gHhqZqNSvu6osc8t8iKEdJ7_BCSZyuVc8ClkMOzkQYnVoYAojyrq7a2HDdxpOLIvuuw77aD1bSjK5G1-HY8wf8MTKNNcVKMOFlNRVO9kB4SLxG247w1VSVy9gz1xZJK6k911C4OQEaT4_r4KYsuNOO1WLO-hvxPPMZ5XMRgAD2HYHHuTj9mtNrGYxQpMLNGXJTB9XqqCE9tVd0QFofzjKnfNrZ_BQzx4xbOWxoeVqgOu8ikmZW4ZBD8YTCCnpUR24jzbBc2WH9JqSAdv3B6G2k3FCf0dwo7JoEE5AY0TSyTD5YZH5uJSdlaLI2z2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OA4eiEI7KkJaiNMaViJ0H08H_EzyGch0fntl3bbZrDAZTHvZ-TLrq_ccm6NfQqYOVQcqg9fjWasaILKGxYHTEzAXrwGxCtg9z7u-Zr76RbxfZrBz6g_y1XyS7GN4M-0EenGuEwvdj2E3j9VTcal0r535C5JV5lDG0TjOzJpzYaPuGG2w8S4H9L1f31p6FJXNrZEzdAQNvJxeuHIUr-QE3Qkety-nhE0uD4DhFlKFv1egrOL19SrJghYo_STCn4A303o1KS7jeEHP00WB2nVByOGjpZkVbORF88dobdf2MK7YG37NCu376AzKWoWMn3IlToaUnnKwGIU-WciRSDR7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzwXcI3-7wzAvk7qN1NCs8dnb5i6MHweBGyEA6stCH0X6XdWAT3j43UVbN0ZJxaTLIUrp9ACVtg3E-JKM0Eo94pAXJKd78NqwrTk095NhErIT_SMVRja8juCd43L1KHtGj7Hyiy5IRAblnADZpaW2A6mFXw6r-8ngqUGZeVT-vW13AfOjjvpPyMZVcFn0UuSBP0RZdkGSRv2trlazjwVL5t-uyhWb-EE42SFPM7j_OSNwX3-wIlg3PKqn6z9BGINBatlOHlNegXUsanesx2ApVgpJRulZ6fEh7Ec1BjSAIa7CydlnGpn19rX_GPmXsiMB1SsnGF7ds6pg1bnPleSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCQ1q8tXzPKshW9BrwjQhVLARZiyemsnErU-EoxWQv__bAyLCx5ALE5RFUiU_UbNGWmonxqkFsrgCVwINzwIMfMmkwuMS2gFuqF7wazyzFaAEsEIBFZGGJSQEx1XMZTsg7A9x-vzAb0KmbuPPVZr2S6OQet-tuueMoupkCaE2vSNpG7VITIMqJ-2N1jdA0BtNyjrc2_2LeYGpP36yYuZ0vemL2vG4qLtCey8dH6_M8YpwV-23JyZK0n347PzZHrxwoHCqBGbJnx6VEw9fqZ8-H4vtrUXAUSWi_lvkynkJgd6GWw-wfkUF0iHVBZUSm0Hk9HgrDuGu3NcvTIJpCSgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxjy7Xvo2uf550qR_ZqQw8xdh7bt7TuTAP7UlcZPCHwfYCMKKqaLHcmlAKUlpF0gZ88G2zpGz-EGfEMD6yJKLYFacw4l7eDLOO85M2yUi9uiGEk6J_sXHwdKYRRhpi2nlDAEdZlEe_zswi_n0A-O9Pm3ooYYcEmIgmqQgicZVp8xQbktjDLtbao4enfp3euyX-kl-8rjfY5BTJNk15b__Z02TNprZCBLzPpAiponoDWuAhvS_lK6yJ6idQv8AJoCEjkdf6WiP_IsIe0I_8xeqOBq_o_97TDjfkS0PX6XX5dxb2c3w3scIzPNs0gg8SfV590FNE61MWxrAVoHM-nO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMmDXwbrEN4VAk1KMAVfzHp3uQJ0aPERbNOAHjYQ1eF7F-5_w37gx6cKXRxZkmC18_EFA3HEFkfE2pp8l4bNL-MoDl63OXAj0z5ZfsKBkxQDPeNZBPS6OFt7dYvM9YPfvILmLUfOiP4PfC-GtLQiO0Zu56Np0zduKBSe3HKtDx9aio_bTkNpetPBPHUbZOfWftuPDvP7OKhAN77AxoGIGVVt7Az6oGpua2nk7ZQd9GuDS-8OYSDK_47N2vpxHMMuQtU_Tvtoil4c0YQ-KDACxs-m0VNHw085uPJO5Gf044B37hYPk7-lXaiiWabKszn9J39zQJ5EYj2kTslO3inCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWfAkacIAdto6vw9CJrows7PM1fchVbtERt2aui-AJC3Vrx4H_DA5fqKCtzvsB5PctCaGOYk62mcgjf9eSpMOOuC2r7U6nMjNCTDnWGCFfZvuH5xWkDPD2O6LFhOeNrJ9rXLhM7soPTLRdQ0fxXeunK1lv-49BQEIxi94SyvBWC3YxUSFEsDOyiBNNL8xKgS2mdPZ8OgZAT5My_-10oRdtsRTV7uwCUk5VqxNqQZ-m6VvAyjdLLgROnH5GUrG53vkX4To86HNlSCcW8SvwWt5VXTifIEKRZMp7us4BLiLdKliER_ntwaXLHH3mzvhR-m9Q7YgOy4TRCpYnqGyYDDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cj1tH7KDW04IhzTk--6pe_bj05m15-mOBXVagGoHsSGH3D3dN6Xm0S4wMHmQkaFqZ1PeEFvuKP57hVqkSTz9OoDMDEv8fMhvpfXplNDwRrjVliaoiqWTpVhJyiJEHO9T1SaT1EVYosXtO3u5b5sGBkz1Z-T1QLJHLpveE3d9LgXpfxxwB2N-idNeMvIhAmtnUezT5q8dxaFc37W_2NO1jRDH35JL3Zi8oz93DfdnYZAr6pC_ocDh1Fe1GTugpnvtzVoL86pp4N8P_PLwTgO86l60yPBHKTaNziXngoFRhVTeGXhmFbWLRmP_NLaIjZM--4-zVCicdteWFZxTCCIp9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از دومین روز مراسم وداع با رهبر شهید
🔹
عکاس: فهیمه فرخی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/667092" target="_blank">📅 21:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667091">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WewQLNVlWE_o1h7klW89EuMF-s2iO07F8fvalUHwgY2J-M9Fy6i92syDqyRwGWwxAsxKrbFq88GhsBOEVzVXv-JkTcEOeYnqWRtKtY8J5Ev8G2z5Z48pPNj-q27i753NcDg0hLlTbes2wJRJFrBDEwlVDZmT9l6pY_johoFE8etv-ZCOp8-DTbLhQ5VtCulHIW6Yb1NfebTN0P4vDJ0DwGl1cvgoudJnRvX9LjtCVsMtOsLuKgSaLA9odmM3ejYNTt9U4c7o17D9Gnw0v0d5z4AK9T32ZO6FeRXZL7mPbypUJHQRKUTEiHgnH6-XGxz_0i46TkJd_Ve4OvGgudDe4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی مستند: روایت رهبری
🔹
«روایت رهبری» مستندی است که با انتشار تصاویر آرشیوی کمتر دیده‌شده، روند انتخاب حضرت آیت‌الله خامنه‌ای به رهبری انقلاب را بازگو می‌کند. این اثر با بررسی جلسات تاریخی مجلس خبرگان، استعفای آیت‌الله منتظری، نقش امام خمینی(ره) و مبانی…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/667091" target="_blank">📅 21:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667090">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAIRRxuDovesg__AQ-tcl0ZarHanp3fSdbpigkovRlN3gDpwnZT8o-bkHgYfKE_kVkmWLOEuN38MdBi2t7tUt7RFI3bwLKe3UNMNR118TLjs33abbNmve_faaZrqS6cwjgVyRUNW7mh6wIJcr-ieRD_qoy98TxMNnHzY9DR8Crj46tJuwdGVJ0yBZC4EqP-_4cD2AODqFVbkCyoUYH0YHrjAIZA6yN2DGEqQN8KqDrowSTvTwEaNoxmokdHq2H01EOpZe0TvqnopdY-Ird1rXr-SutJNraRMNM_CoV_0M9jpf9OUDsk63LFffhiUz2a3cWoaGq1pXMbU9h5phWhwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از فیفا به خاطر بخشش کارت قرمز بازیکن آمریکا تشکر کرد!
#جام_تایم۲۶
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/667090" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667089">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
زائر خوزستانی مصلای تهران خطاب به رهبر شهید: شما همه‌چیز تمام بودید و با اسم شهید نام‌تان کامل‌تر شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/667089" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667088">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b921d180d.mp4?token=vqMquJsn5grQVW3crd4zyRSpjEny_zsCDz6Bz0-il2uu1n-CnWzh-aK-GOAJvEvettV7LfVbnoP8GvGNooCYWE70TLzIAw6hBF2eZKAGxSEBwo_muDDUiHxm5arltIjEoZtCzJ8YwtLnOZEe4RDLPhyf6kPmYXkq08zIIbabxztxndxSSGAZntYQwOj1xn-rBb0ySVoEdMGzM6sYig1r_Bf0C8sQvH_zjHlxALwhaB63sLeYLRnDzuOGoKM9kE0rHB0dKKll8nSsafzg5q_Tc_BprtVjyJ_5QPKdiVzmDJTQSgtpn164E1ntP1x7YOkBpmKt1qB-6E9m7XXzvkLNFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b921d180d.mp4?token=vqMquJsn5grQVW3crd4zyRSpjEny_zsCDz6Bz0-il2uu1n-CnWzh-aK-GOAJvEvettV7LfVbnoP8GvGNooCYWE70TLzIAw6hBF2eZKAGxSEBwo_muDDUiHxm5arltIjEoZtCzJ8YwtLnOZEe4RDLPhyf6kPmYXkq08zIIbabxztxndxSSGAZntYQwOj1xn-rBb0ySVoEdMGzM6sYig1r_Bf0C8sQvH_zjHlxALwhaB63sLeYLRnDzuOGoKM9kE0rHB0dKKll8nSsafzg5q_Tc_BprtVjyJ_5QPKdiVzmDJTQSgtpn164E1ntP1x7YOkBpmKt1qB-6E9m7XXzvkLNFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: همۀ خسارتمان را می‌گیریم و جنایتکاران را رها نمی‌کنیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/667088" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667087">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
زائر لبنانی مراسم وداع با قائد شهید: برادرانم در راه مبارزه با  رژیم صهیونی شهید شدند؛ من هم گوش به فرمان رهبرم
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/667087" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c44794ffef.mp4?token=CPYaRwWbMp5YlSm4kv6sVgsT9Cm43XUIqtW5GtIM1KbZFwtTsAiIUH0kJIPBnD4Fk9RPk3c5lE-i6ie9Kdxa39baalGSar9yp5hfyDmXoQKJ4Wmq3lrKznuOYmQw57eN41lwH7Z2TZ25yRi_7CjCjkA5s-8n35W-I1NHAENj2-Ve3oyjBARvT1QGcL46s9szT6437T4kQv_wa4S4th9PElnHeOJKlrMnkbyowzAeE16RN9177qPPq-tVotPWAarmsvHgvrEgmo5GlovD0Pk9Sy9dJk6orTksXxoRwVUUtnYQznbkDka4a97bZ2_UD7Mu33dErKNkiZk8ZUBQEo3aQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c44794ffef.mp4?token=CPYaRwWbMp5YlSm4kv6sVgsT9Cm43XUIqtW5GtIM1KbZFwtTsAiIUH0kJIPBnD4Fk9RPk3c5lE-i6ie9Kdxa39baalGSar9yp5hfyDmXoQKJ4Wmq3lrKznuOYmQw57eN41lwH7Z2TZ25yRi_7CjCjkA5s-8n35W-I1NHAENj2-Ve3oyjBARvT1QGcL46s9szT6437T4kQv_wa4S4th9PElnHeOJKlrMnkbyowzAeE16RN9177qPPq-tVotPWAarmsvHgvrEgmo5GlovD0Pk9Sy9dJk6orTksXxoRwVUUtnYQznbkDka4a97bZ2_UD7Mu33dErKNkiZk8ZUBQEo3aQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در مجتمع تجاری در خیابان الظلالِ بغداد
🔹
به گفته برخی رسانه‌های عراقی چند کارگر در داخل ساختمان‌ها گیر افتاده‌اند و تلاش برای نجات آنها ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667085" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
از شکار بی‌رحمانه تا تحول بزرگ؛ تجربه نزدیک به مرگ یک شکارچی
🔹
00:07:00 در شکار به هیچ موجودی رحم نمی‌کردم
🔹
00:19:00 علت گریه نوزاد در هنگام متولد شدن
🔹
00:21:50 معتقد نبودن به نماز و گوش دادن به موسیقی شاد در روز عاشورا
🔹
00:29:00 رؤیت افراد جهنمی با بدن انسانی اما چهره حیوانی
🔹
00:34:00 مذمت شکار در دین برای تفریح
🔹
00:35:50 تغییرات رفتاری محسوس بعد از تجربه نزدیک به مرگ
🔹
00:44:00 متوسل شدن همسر به امام رضا(ع) در میان قطع امید شدن پزشکان
🔹
00:50:20 تطابق رؤیت‌های روح در حالت کما با واقعیت در بیمارستان
🔹
قسمت بیست‌وهشتم (شکار)، فصل چهارم
🔹
#تجربه‌گر
: محسن حسنوند
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/667084" target="_blank">📅 20:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667083">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
محسنی اژه‌ای: در برابر قاتلان آمریکایی و صهیونیستی کوتاه نمی‌آییم
🔹
محسنی اژه‌ای با تأکید بر حمایت ایران از هرگونه قیام علیه ظالمان، تصریح کرد که ایران در میدان دیپلماسی نیز رویکردی آفندی و مطالبه‌گر خواهد داشت.
🔹
وی با اشاره به روحیه شهادت‌طلبانه ملت ایران افزود: «مردم ما عزادارند، اما ماتم‌زده نیستند.»
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/667083" target="_blank">📅 20:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_BNYgIK8Z6WIAGN1D420uey2jxMFzuxvtNvntkGo4tKx0zwku6MmPHWFTNCwY5riQNcDIciD9FWsayFAz5RydAUjz3tLaZBtFMJjkN3Qfapt9yzy1P7WGnFQqO2ESb9PpCNn60hXsjxIA7Cuf34hWQdZNNaETVrj9MEZvS5Hp3Z2D4H0XbixfMkRrgAE7YCTkq2hNr3ENdD-5LuOW4s_z69KkD88T6Oiz_BYhjQs7H2XZhu6EVFrSxEagB34sN8tt7BBJuDHqngO8gxRvFx_XGTmkFQ4aY11AfobsURlpdqVNRSlGHhfOz0hJoz1q1fOunSfrpum-PFM9m90l5CGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jk3nrxqQ9742KpYIlkiCmNQvUFCJ-UkejFq1obTvZxutPROZjLIyj_QDpRt1-X38kzjB9lkPXAe0x92DAmcbHfBbQs52DXwzs2Razp0PZyujjZDo_6CFxfaPPytoqOV4GCjfJ7sTmOk_gKMtHv7lDkARYrVEHuNhLCDK3Ox5DKFls1wygF-iUbzdXSTJBjzhlOzLkyJAQzCA6hwtng3WexmnqnreOmY7emHsmwyPILkUBB6D5d3YdvNhgeNCoACqmIkKvogmmk-ToTl0GhbeDp-ijxPeDpQsMYtrAUIqTsB3sPHZW1u8IOPJpbZ7aWsk8bOR46fpu907xrjQsh1vKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aL9-gteGjMURqgRqgPmIMYU846Vj7x1UPujB4vOOj0zEp6BAFipBlVgofTJSPcJJrkh8OBTgL4ROjPES-yWSOYn0r7nEOXKWrvb4a4LDIRreh6HwsPfEe5e8qcHe5JIGwfYmH7OUs2c-niAdfhbWNKX0Mdb3-KAnRuV-pKSlOfzTYU5s_pBChsAAHIOPnksXHEu9zqdNzLl6fzQ5DW2OkN_2jhBSFPr68vAmYhIvdyaE8FeQbcruNUp6048ocWquLwb3yRtRj_GqWmX6XJ0MJDA4DqqFsKlG6jRTBeg6bHJ3E_rpHMSrUh2vWBSGImuS4QkahHJlgTjG5CxgMqHwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTJsV0BH6BNoXpmqzOQ2PKa1tM0vJZTg_S6geHk2z9edq7p3t1EmqJQ7ECwWpI9Do39HCU8BQ1SyZmlwJnlw_R2jFdS6OuCGSU2Di6EMSTRz9uanAB7eLc62tj27qCxvwz4Z2joFYXkKaZ2z11x-nrLmfcBWA1fqSrSFvefBvaa2l5G_XaMR3zRQfELxcYjYYEyzv7Ztq8jSooq9GIw8FKdd4Hz40OBEKPAS1pqgPH8llDpEAhuk_x2RZj0RWF8Dlp60guhRS2j0KULd99Vk5_r2TRGZ77jRhztcb7mxg4GBbW5Ywl7ZuM5Bp3EfQo8AR8i9ILVkQbmfKOrKBqZYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcRc3kbm_McYUi9USLmW4NUcoNV0CarBFxgP2dZ-T-ixgPKplNfNaZO_9BuJ23MGEikelbRIlR6PtCdiWN3OjWVyz5e64kX-qRqR_A2xf9mgkLj2HO3fyO9JeSfiDE8O3T2WrQRvWkq-CN-VSbhEn9O6L39hFTedyMp1LEOXgN12ZdSgAuHwhaWSczvVQtcnhgV7CSXSHZFeMnR74VVT-uQQ7e7k0MuUwQyhW9SYS-NSki6Brz4GJjyqWDMmjq9n5K2kcJoT7AXKug3C2B2YsK0BEsYqwsQ0ejGlc6CrrnKsdBOoeE7AGXZDO4K4naVEBgcMnlq2eirPkuSUzdNANw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم وداع با پیکر رهبر شهید در مصلای تهران
🔹
عکاس: محمد اکبرپور
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/667078" target="_blank">📅 20:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7582d67ba.mp4?token=aJGeaSGNvQQpFt3xWrtdsxUDrpSFoL8lnw2lgfgL5Ko3JvrA_yFg7vG7mIZn8u8SZhuWS5XPQ7F8crODa9REgOYb2_i2LvxcIysvg7PciY8MewPDCwNIpSA7Am9MwutvS8HvdPypTGmHqvpBN6jxkBh5KJfdJH2OXmvdMvVDriEqcvsr3I2DWkFOH45jKRGcTV7arJAThNrusQu9LICbVrONy8Dy401Kit7t4soFknnSKaIZuAiTDIC32LnbYYmY1k0or5A_cS9ajhEKjGxTeVt6xWJMpcmg_Ncwu4PtpRkgUwBqFARuuIFLzZRyORJbLqN94sTnyAelau-ArPd_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7582d67ba.mp4?token=aJGeaSGNvQQpFt3xWrtdsxUDrpSFoL8lnw2lgfgL5Ko3JvrA_yFg7vG7mIZn8u8SZhuWS5XPQ7F8crODa9REgOYb2_i2LvxcIysvg7PciY8MewPDCwNIpSA7Am9MwutvS8HvdPypTGmHqvpBN6jxkBh5KJfdJH2OXmvdMvVDriEqcvsr3I2DWkFOH45jKRGcTV7arJAThNrusQu9LICbVrONy8Dy401Kit7t4soFknnSKaIZuAiTDIC32LnbYYmY1k0or5A_cS9ajhEKjGxTeVt6xWJMpcmg_Ncwu4PtpRkgUwBqFARuuIFLzZRyORJbLqN94sTnyAelau-ArPd_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متروی مصلی مملو از جمعیت است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/667077" target="_blank">📅 20:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667076">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci4o36cVBJdLNEqiLnYvT4B1r-QmlWIjSJSBs8SZVW-yEffMMudpuyNZsDV_Z-ko5wC4F1eajInuo4E82fga5No7xbhccW3Qrk-Jfng9tyTz1Cv2oM0p3ZNb-__Bw6klRC8Wqo22ccqptEK3V9Avhp1VjiXGKvtX7Bzaibsnd-VhicaLDIF5PTjLDyoFzxuvGI2OwjgbhsXkrHoXBviU7Y3sQCoeQRTAsq4_9WDC9WkzG9nAYBe75KNVWiQ6jvhatmFfQFUVynt-9wcC7AxYMN4hG43MhwN0XGqJUhSmpM_LcAkEr9UhvfBGYgNh0dnmn8q2eqSd_h3-LmKEUbqCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد دانشگاه شیکاگو: ایران؛ قدرت نوظهور منطقه
رابرت ای. پاپ، استاد علوم سیاسی:
🔹
وحدت میلیونی مردم در وداع با رهبر شهید نتیجه اقدامات خصمانه ترامپ است؛ ایران اکنون قدرت نوظهور منطقه است و به‌سادگی از تنگه هرمز عقب‌نشینی نخواهد کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/667076" target="_blank">📅 20:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667075">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17080c3f19.mp4?token=ODKnY10TN5XzvZw75yNbs0S8Hj9o13y7yFxnfFOTiLVPfoNdfCZ4HlWMZFMhdk7GZGK-PHDl3EwWWpj8VCKkS6DQz5gWPqNmzHCs5fUBZEpAXUz0bdoPQq5QM6vFCSJGK0Vm7EbD5DUxn8DHDPu6yq-DX1Lqdl-jcjMPWbU7Byb0XcEIN2lrTObljL_vpEdEJPdssHdwW80rFP_NNH9U7DgAWTCSDDHVAPeMjkiaJUYsxOHIEM--wxJbzKiBKB4fk2ijQeqzsTNV0mV6eVt1E1CfSiL7ODWh61YCW30QCVA9ecSQgMe9dq5l3QCNtSpdUwVHREd8VT0hQaPmgQj_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17080c3f19.mp4?token=ODKnY10TN5XzvZw75yNbs0S8Hj9o13y7yFxnfFOTiLVPfoNdfCZ4HlWMZFMhdk7GZGK-PHDl3EwWWpj8VCKkS6DQz5gWPqNmzHCs5fUBZEpAXUz0bdoPQq5QM6vFCSJGK0Vm7EbD5DUxn8DHDPu6yq-DX1Lqdl-jcjMPWbU7Byb0XcEIN2lrTObljL_vpEdEJPdssHdwW80rFP_NNH9U7DgAWTCSDDHVAPeMjkiaJUYsxOHIEM--wxJbzKiBKB4fk2ijQeqzsTNV0mV6eVt1E1CfSiL7ODWh61YCW30QCVA9ecSQgMe9dq5l3QCNtSpdUwVHREd8VT0hQaPmgQj_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید آخرین غروبی که تهران میزبان آقای شهیدمان است...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/667075" target="_blank">📅 20:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667069">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-yVQBRKnDZ2dTnr2AMxLisAPbpcRQf43XGlNqSdqkqxuBUAmX5TmTC1dC3tCToxcUmnebxaMbLXSBQIAT5_SaAVucAAHUbAL8pE-wFFR93za95hecIPw70_x1cHFH1g7spLc2BLm9eJvEhO5-eU5Y53-IpfeRRIpaN6J7QBtHv1uPOlqvfjlecLYi-RLiyP3pEqfG4zMRh9EzKS8kUeX8o-8iU15svE06won0uMOdPePwP63NQ5CJiIJLmpqXcVgAVj9ovVIcNnBq8YbrOqIKVMXOqfYpfa1AnZrr-jk6FDP72b96IGxctSUBOAhd7iEWwvjZDBsvYiMzD2CtJw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQIQoz2a2uCR0twqTOtJJWGs5r7MoA73pxaMAgRk-WtYQFgUpVg4rw3_aVk89mwjiq1SygmZdT2qfYe1f-F4chzXGrAwEhj7PcLwQPtFPht-ZaSlf6Ntb7qfD45p1H51r6moPHOYE4l9a2_rKVFGZQjsuaLIkbfwYCpEenOWYYHs-7HKg_WA7fOrv3Sm3WyH_4ues_5tWBf8KgseEziZzhRg989Rpz7ceBkn_kFtoJTTKVd4xfBBA9eVPDRH9R4MOKwIpylFooTA8JC6o_mm8dVeTi1BfSxQ9iC6fEa_btEScHakh_lydjRYpX_vxmH5X61jgswolT843842NMaa2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEwoTtr_Ep35gjpOcOn3wAF7olJQGRf6uaRd1WWr1XxyhBtyKsXE9p3E702YrJlZVcTV4cixANDN7HCpae3xQFJAOgowmvdCJbo2pFe4xk7j3bmG0ULI4LqA5Mbn-rES4ghl1HObsMZIxMBDJVoAqlT2tvscizlsixil8gS17XkeHDH7NdHMWOdpofIyv154xA3pjLpVKOV7-FN4-bSpqJKo29aFbqE-Jk4q-Dq40wMq9wdUvdRThoTClxBF1MJFBqykoWjQ421HWSnnExYo8-cTil-AuSeRb0BfexMg-TK3EBh1spdGhyfKq6A0QtH6Gs-sjlic7us7ALQgKhg48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2PQvUssRZZgoSumdVH9Gh5IGAyDPdrRQJY0dpMAUuLEQVguDm68uYLY_F6wBCOU0FBOKNlh3to973V_cVaNhF_yJ6CWvZ0LgWFyBe5mptD13rZjFgj5VG6IA2ysAXKru4OvZFQt1zJn0AOBX2ZVQGgslAOciA8EbBEj0NhkTdGrUbuYC8L4kc6q4aMx6yVKWPypbbzLVYMkaeUJq-pM0QceQtpw6XF--VKVezyOiq23EroRPeiWWXtpTFoTY5sRtdGGa-GHoqRZ2TCz-VgTppregucbIGuMosKWh8nX0H7x6yU8eDY-HUWomVze5ixUEw1knVTRRR5r0bz2g9Q1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsjwYdXnfIkLY_itaWqE63DJ58Smjl8g2vFfe7eeT5mDJuy0aR_vdWMzr696GxvopWjUlNh5lqNwgJIxzXRcschzRnRyP7jZU1k_u1gsJZz_x9ZL6oMOxK-ejljKo_r6Fu4Lxu--2iwdgAczFXI5MtpttYIUw2q1pSijGyubM5H7HihjfU6qgxM86DTu0XuKf6ussZrZkOXKPN-NSuFjoWTCeuMeb8jyuytZ43nbg_bIZXqIJP1LNybIHRjsmgz7GUGdTetJoTV8JnhKFb1H_hXx7oVOu0v-zNOsyy9W-feqIhqTcNk9LAObsYj6hUELV-84iH60CLrZR96EptbYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J337SwnUtKY-pY5Ju4OaW21N__daxoQ8ff9oens7eHOtP_KexwXjtIoCuFpVf2ADo3Acf7pl0-a7uDH4Fx-gJpjEsN_zxvsaNfNtapnpcWpK0Vy-gw4tvE0K1PnGjgt0YnZ1_5SlOBTGx19FKUC1Wlo9CdsncKa4aiK7_0cz_zVl_4bo4n75aE-PrGPaekRI6_kJwSXZl24GPNFu79FCqbJauU2b1EwZg6ecKKj3F8UYUjdLeWB5SJF_84O5iTV8f5RPAUq8CeWwz9PGxt5gY-BbKnCbSiUxLijkbJjyslR-0KIkrqr-hURRSU1NIcfUsRZdkbplvcUOaHxcwuyANw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مچ‌بند سرخ
🔹
قاب‌هایی از حضور مردم با مچ‌بند سرخ؛ نمادی از عهد، وفاداری و خون‌خواهی امام شهید و نایب صاحب‌الزمان(عج).
🔹
این روایت همچنان ادامه دارد...
🔸
شما هم تصاویر خود با مچ‌بند سرخ را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/667069" target="_blank">📅 20:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667068">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏆
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/667068" target="_blank">📅 20:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667067">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4732a72aac.mp4?token=mOCjbLV8cUC1XKMpdAuDm76SJhFgR1Cyq2ptAaNrz-T52h8trVPg3IYa614iqqyWie38q-JOLh58J9M1SXmt-0UWOpP-EbUMj_IGSbK5yodtpDdAOZXXFQd9IdWPwGGLBVlaf2-yk47ZcEUxw68IzycNoQ4GNfW6QE_7TEck9fJ_mJq3y21lqd_86rBm3p-GgX2f1DSJEZHLYaV143L2gdD9u_rce69N9mD8tzySanPNX2snaTu2Z9Jy0LGDDKlJxcfGidVPC0xZ0skmhxdB6Cp4FENH6XbCVHHpDUWmji9P2E4aCIDd6RW3dCVE5Q7YBGZCPqmp9lo7uAtM4IuHXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4732a72aac.mp4?token=mOCjbLV8cUC1XKMpdAuDm76SJhFgR1Cyq2ptAaNrz-T52h8trVPg3IYa614iqqyWie38q-JOLh58J9M1SXmt-0UWOpP-EbUMj_IGSbK5yodtpDdAOZXXFQd9IdWPwGGLBVlaf2-yk47ZcEUxw68IzycNoQ4GNfW6QE_7TEck9fJ_mJq3y21lqd_86rBm3p-GgX2f1DSJEZHLYaV143L2gdD9u_rce69N9mD8tzySanPNX2snaTu2Z9Jy0LGDDKlJxcfGidVPC0xZ0skmhxdB6Cp4FENH6XbCVHHpDUWmji9P2E4aCIDd6RW3dCVE5Q7YBGZCPqmp9lo7uAtM4IuHXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیمایی در رودخانه ایست در نیویورک سقوط کرد
🔹
پلیس اعلام کرد که سرنشینان این هواپیما نجات یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/667067" target="_blank">📅 20:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667066">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3Gnpe-HNzGFJnWYkyyvXMe4fUnulJUokffeRhUWHLpHpjyTMNMg1yq1fNyT2dXFo4D6sxoLH4-eBbrPE6iC3qBq77Fq9sAGH8OeaFFvfH5YzClRNCaaYYOLj_vcsePnCCG0G0_M4vYxOZoJUuluu2HAr4ygyIY3RvIifeND0gWqxN6vDXOye27EOW2iLsT8kkqOT7OtWJktKcGENrj-QMrGwOmhiToRJzoZqnFa7qLM-lqgElITLmwKHKZwP7hUoZ3zmwL3JZtnC6XOYpsUyv3gplLuyahZNXZRQRS1xtQ36ezzwAdJQGowU6WPkcTAm-g9nC_wCf7pS8-RQV49bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ننگا بما اگر که ز خونت گذر کنیم!
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/667066" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667065">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b8123ee.mp4?token=QJKfR3lLVyf_02ijbHQUE3uvDUKe1YLMJW_MnhZjr4Zy28VulInLiDI9eqhZxasSSGky048VLqkphoPQNAjP9sw0UIrBdbXcW7R_DMXa2n-IFslvDlXfLZzh-4JYsREankTMBGfcuY5I0udqkAdEc_1h2Yq6ZyuDsqo3Qj9jKkSTtDGUluCxSv55jQD1PaWdrZyJV6rY4-KccCoF9Qd3wtO9CQf0AdYN8LeSBiU5XvVsUODxnSN0-vO5OlGZKEAvw0WirymbqgwQC8PYWaSKwH3rNMet4JnHjs7_l-DfqwoQzX8_gSN68C0zwvswH_1Aqp7oKoKVc0c47K23n6x8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b8123ee.mp4?token=QJKfR3lLVyf_02ijbHQUE3uvDUKe1YLMJW_MnhZjr4Zy28VulInLiDI9eqhZxasSSGky048VLqkphoPQNAjP9sw0UIrBdbXcW7R_DMXa2n-IFslvDlXfLZzh-4JYsREankTMBGfcuY5I0udqkAdEc_1h2Yq6ZyuDsqo3Qj9jKkSTtDGUluCxSv55jQD1PaWdrZyJV6rY4-KccCoF9Qd3wtO9CQf0AdYN8LeSBiU5XvVsUODxnSN0-vO5OlGZKEAvw0WirymbqgwQC8PYWaSKwH3rNMet4JnHjs7_l-DfqwoQzX8_gSN68C0zwvswH_1Aqp7oKoKVc0c47K23n6x8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین اذان مغرب در مصلای امام‌خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/667065" target="_blank">📅 20:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667064">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
تعلیق پروازهای تجاری فرودگاه نجف
فرودگاه بین‌المللی نجف:
🔹
تمامی پروازهای تجاری به دلایل عملیاتی، تا صبح پنجشنبه به حالت تعلیق درآمده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/667064" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667063">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42afbb9eec.mp4?token=kp-87sg3l-008eI0NW9t6bI8iu30XC139io9rXE3ipMTbtit-qk1MGJrTyy8TsEmq5EqT-FcB3zgr7IjDkOBVB0Cxcg_GoldQyl5qwjhLZ2x8buN2FVWK_YgKU96eHC3vCwBcgnpOS1Mnsy_XnaCfWmKZbEg1iH48D7jJx5TBYhM0B2J3peJ1s25v9cgHq4F8E2eqo_j4pY5S2Y3LzYPttXl0n4aKsJ9JfJXrigtWff2xV2Bqj6rj32X-aGkcLMjJJvwOJ3pofhH4zUpftyyTLvOIeTnwOOe30CFpz8K6TcZxKqkXfiVqO9OEUS27J7JiUluyA1Glg6NAcBBniw10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42afbb9eec.mp4?token=kp-87sg3l-008eI0NW9t6bI8iu30XC139io9rXE3ipMTbtit-qk1MGJrTyy8TsEmq5EqT-FcB3zgr7IjDkOBVB0Cxcg_GoldQyl5qwjhLZ2x8buN2FVWK_YgKU96eHC3vCwBcgnpOS1Mnsy_XnaCfWmKZbEg1iH48D7jJx5TBYhM0B2J3peJ1s25v9cgHq4F8E2eqo_j4pY5S2Y3LzYPttXl0n4aKsJ9JfJXrigtWff2xV2Bqj6rj32X-aGkcLMjJJvwOJ3pofhH4zUpftyyTLvOIeTnwOOe30CFpz8K6TcZxKqkXfiVqO9OEUS27J7JiUluyA1Glg6NAcBBniw10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
او به آرزوی‌اش رسید/ زائر رهبر‌ شهید: خوشحالم که رهبر شهید به آرزوی خود رسید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/667063" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667062">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
بانگ طوفانی یا حسین (علیه‌السلام) در کنار پیکر مطهر رهبر شهید انقلاب اسلامی در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/667062" target="_blank">📅 20:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667061">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SopNyixTHtQ7gZUUhaBJ45WI1Eo8p9QsBZs5ESbrKtbVwzoKaXZf_cvKNsUCYbgW7Iq_bwDQtVprMluK4dmTY3wEykcdFH33c4DXkWgwvbHPFJej-A3v8HsjwUM_xvuELKTZerVWEMyliloS2kg6M-hPCr5BGvTvg8EHgj_NSczH-c-beOGmEsfw59QMY-fCxTTPKHALOes0Ie160vrik2LJmypDGYVIxnvDkLnmf1oQ_qFYlF31L6MrXGHahi16DNL4u4SauS3lsVfTdGB_9g_2T0Uy9NC7J1t1Ija-npxa3fxKPr4QZVfcVG7O0DNoXpgSbR14eED74ph2OEyo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید مدیرعامل از موکب‌های خدمت‌رسانی؛ نوراللهی:
#بیمه_البرز
تمام‌قد، پشتیبان زائران است.
مدیرعامل
#بیمه_البرز
در جریان بازدید از موکب‌های این شرکت در پایتخت، بر ضرورت ارائه خدمات در کوتاه‌ترین زمان ممکن تاکید کرد. در همین راستا و با دستور وی، علاوه بر استقرار شبانه‌روزی تیم‌های تخصصی ارزیابی و پرداخت خسارت خودرو در تمامی محورهای مواصلاتی منتهی به تهران، اعضای ستاد ویژه برگزاری این مراسم نیز جهت ساماندهی فرآیند خدمت‌رسانی منصوب شدند.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5056</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/667061" target="_blank">📅 20:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667060">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csgLazkl2uIkSb4nsYt9BWl8xBPugzz5MJ9Th4YF4cw2464weq5Zi_n_m2pouKleyZe99l78G9avNSkNgFJWnRX9vceyKNraiLN1H30cTeTnfbisq8pfBjpUHlM3qU8awZfnoTQklzMa_wKguhu3EGFiDkK4vkgagRnbM5Y2ufVrSTXxXJRK65B7DielTVvwp2PgL961kWUpu57sT6jEtow0edO5c0EEgmp4eCnezIepf6n6HlVa-Wu09fmdSx7YGBdo7g_jeYGCg5kHMg4xFdZn5TnEEIJgI96eIvapKcfE7v3k5Z4aXoe_Bhuxt6b6aq4A02kflocRna5Gd8onRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور رئیس‌کل بیمه مرکزی: صنعت بیمه در آیین وداع و تشییع رهبر شهید انقلاب، تمام‌قد پای کار آمده است.
ذاکر تیموری، مشاور سیاست‌گذاری رسانه‌ای رئیس‌کل بیمه مرکزی با تأکید بر اینکه خدمات ارائه‌شده صنعت بیمه، تنها گامی کوچک برای ادای دین به غیرت بی‌نظیر مردم و ایستادگیِ رهبری شهید است گفت: خدمات‌رسانی صنعت بیمه تنها به برپایی موکب‌های متعدد، پذیرایی شبانه‌روزی و اقدامات فرهنگی محدود نمی‌شود؛ بلکه در کنار پوشش بیمه‌ای تمام شرکت‌کنندگان در قالب کنسرسیوم، تیم‌های متعدد ارزیابی و پرداخت خسارت نیز در سراسر محورهای مواصلاتی منتهی به تهران مستقر شده‌اند تا این صنعت بار دیگر تمام‌قد پشتیبان رفاه و آرامش ملت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/667060" target="_blank">📅 20:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667059">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پیکر رهبر شهید از جمکران تا حرم حضرت معصومه(س) تشییع می‌شود
دبیر ستاد ملی آیین تشییع و وداع با رهبر شهید:
🔹
پیکرهای قائد اُمت و خانواده ایشان، پس از اقامه نماز در مسجد جمکران، از این مکان تا حرم حضرت معصومه(س) تشییع خواهد شد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/667059" target="_blank">📅 19:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667058">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKounasJ7oEJ1Vbb-uJ9bj4aiPEUCXKHoC20GHz6IiZMAPvy86D_pHJZiKGqIvQe6Us_SQipjqCE_-GEnYDn7TeZwymYiPMk7ztPPjlfM0aKDUOX3ra72pDX5lCQ9QSHLRQCOH9JU7UDQYakL173i8Q21Pm1gSX44HuAsSxCwW87ytB32UVJBP-z1yL-OC0rZ_fyVCFwwj-I1Uylfq3OcpB-w925QA5bkrLu-7l--im69Vj50-sWrB3j2i2ENq1hA12iAzoroT5n3yqw_R2WocQ02iYy2W_tFdSuqeBGLxXjPdzrnfAQzjz6nN44AfgefSjQ5K3ftj7P4eg_DxUZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
بنری در مراسم مصلی خطاب به ترامپ: «خواهیم دید چه خواهد شد.»
‎
#هزینه_خواهید_داد
‎
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/667058" target="_blank">📅 19:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667057">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syfPQDR3BKhsy_XS00SlsUyKRU3Aov7o9-BY-8jsqBonO5pDT3RO-GrI0c1FCEWRaCFeOMGMxpKz9le16FseAdPrEfKshTLEuSRS_-efIb07dmcvqLpp5ryDNrISRtcvXrfIjvYtxM7o1Yk24k6Q0JVL5Jte3nZEib3y8SflyPR-WhMp0mGV3-ZOZzmiu2ZD8_2samE39FFWZ_JZ1DSLvPRhUQMXLXKpc4I79YkN_WD9T6QYlwkDcrMtBJJ4mrV_nfOIdBWqqiyVCwXXek8rF2kW7bZrUbBG4O8AwNnp41RvkvqolpQO0IKu5oK_yyGJ0vLZJ86varmmizY9pCil9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۵)
🔹
اگر نتوانستید به تهران، قم یا مشهد بروید می‌توانید با اکانت خود در شبکه های اجتماعی در این بدرقه شرکت کنید، چطور؟ در جریان تولید محتوای بین‌المللی اثر بگذارید. کافی است عکس، نماد یا جمله ای که از رهبر شهید دد خانه خود و اطرافیان هست را در شبکه های اجتماعی پست کنید. از کپشن انگلیسی و عربی هم فراموش نکنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/667057" target="_blank">📅 19:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667056">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c0ca481a.mp4?token=CL-XziB5NO0MaX9zeqeV-ixn-oY4qvFB1W3evzgBRvfWSdQ32l0uSpTISweXHInIIyN9NjeDwJgiZa5zbuYmQpbSBVh-k7YxLNKZQZlmsP9yuQPE0rQVoR_DLGJv9DbSO8pdzSYiz5ZVm1R3F5Kdx1mF36G9NGo92oWCcrVxKHSnNAFb85z417Go8sW9eRxKU6WnOBo_xs-TguIvIWOWHrNGBDZi5xVKfFVQhuR3B2RiMhHEu47ioRyT4W-BWs_nzekOGc_Hkylx_qNuhkYhvSNMqGVhrav8eRSrb1BS_gJev4PI4D-vSV5vuq8fLbQUVcZE9a9gu32ZONIFroWYKxuAeT8kfHG8ZVFwLy8jdXwQx_w7sKRYYNvGdvdE0WtqmZRskPNtARiceHrOEe7-QJtHDPgE2Womyph7g3ZpZU_h3lAKmgxoKRC3tdFo-TlRk9ebOU72STiv-Zfe3_XwZEeB41ILHzvnZO8bToOH_1JuM2qPqhqr3IjXjMuyUr7hufju79ZyAVC--nl5fz_doib3FvMwn7ObuI0jBxU7f1liGqp-enFTQ2g3CEPDwvYDjb9cr-G3mx9h5ghcr4_mvuL2s2SKHJCvKKkuTX4N7YSmDaMTxvU3dWDVXnRN_tfbLvfsL9t4qWXgO24NtpJRnHN5Ep5dXDtKCVhxdrDrcGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c0ca481a.mp4?token=CL-XziB5NO0MaX9zeqeV-ixn-oY4qvFB1W3evzgBRvfWSdQ32l0uSpTISweXHInIIyN9NjeDwJgiZa5zbuYmQpbSBVh-k7YxLNKZQZlmsP9yuQPE0rQVoR_DLGJv9DbSO8pdzSYiz5ZVm1R3F5Kdx1mF36G9NGo92oWCcrVxKHSnNAFb85z417Go8sW9eRxKU6WnOBo_xs-TguIvIWOWHrNGBDZi5xVKfFVQhuR3B2RiMhHEu47ioRyT4W-BWs_nzekOGc_Hkylx_qNuhkYhvSNMqGVhrav8eRSrb1BS_gJev4PI4D-vSV5vuq8fLbQUVcZE9a9gu32ZONIFroWYKxuAeT8kfHG8ZVFwLy8jdXwQx_w7sKRYYNvGdvdE0WtqmZRskPNtARiceHrOEe7-QJtHDPgE2Womyph7g3ZpZU_h3lAKmgxoKRC3tdFo-TlRk9ebOU72STiv-Zfe3_XwZEeB41ILHzvnZO8bToOH_1JuM2qPqhqr3IjXjMuyUr7hufju79ZyAVC--nl5fz_doib3FvMwn7ObuI0jBxU7f1liGqp-enFTQ2g3CEPDwvYDjb9cr-G3mx9h5ghcr4_mvuL2s2SKHJCvKKkuTX4N7YSmDaMTxvU3dWDVXnRN_tfbLvfsL9t4qWXgO24NtpJRnHN5Ep5dXDtKCVhxdrDrcGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت زائر مهاجر از محدودیت‌های عزاداری برای رهبر شهید انقلاب در اروپا
زائر رهبر شهید در گفتگو با خبرفوری:
🔹
من آلمان بودم وقتی خبر شهادت رهبری را شنیدم؛ نمی توانستیم آنجا عزاداری کنیم، داشتن تصویر رهبر شهید جرم است در المان.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/667056" target="_blank">📅 19:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667055">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
نتانیاهو: با ترامپ بر سر چشم‌اندازها توافق داریم  نتانیاهو در گفتگو با فاکس‌نیوز:
🔹
شکافی در رابطه با ترامپ وجود ندارد و هر دو رهبر در راستای منافع کشور خود عمل می‌کنند.
🔹
اگرچه ممکن است اختلافاتی داشته باشند، اما همواره آن‌ها را با صراحت و باز بودن مورد…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/667055" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667053">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcPA8bHpHVnrvxsbxynKgW3o_MhWMxliqykOIcwo-nDpCbtn_vip0kHoTyzQp1vCktc8j-M0mTjgCUzGywVXohuxlekbzWDCE7UpMR127n8yI3Uytj174E55a1-PlpUpTW9xAROdNf-2RDs-6pZv8Pb_e7i9cs_VncsT24BO83_9TWRZMw_iQLAUueklVROrdJDnhK_0oHsdbM-cTT73fvOdkXJyvQrYK3E3kIYq116-hRQODAh82R9j_5VjInxSUVHcIBTqEUfv8etWJfAxTTIV9m9TKCBitydkggPsfQ8stXpsQd7PgF6VnJo2Ry7Od7D-7T6KVR02jdwxVgDLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyuH3tEoKYo5BN7OoGo3ZEM05Ao0ciGMT6Rau2EZNlivg41zaS6KqywI-w_dgk4oHCyTx0t6Hddg1im686_UF_9_Ww2tXEo1aVDaytX4QF_--2uIl6pbL2zArk_k4SEa80dngtIgBLdia-dlbqcuCeaod_nEvc1gfiXqTR50xUx1i0u9w-SG9Cz7s8JL_yEuOcfeLNihJdcxZ_UTLEza-_EL0lX9ogO8d1RvIzQOrEAqc0fZIAURqDd0qIqUQYbqDK0pCPgN6IvEfJC5IrLRVQPgB6RH_aDhdw4pXZq3teTIfZIPwa89mGgCWbGFaW645C0vNzugswrHcT18ZiAr3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت زندگی رهبر شهید از تولد تا انقلاب اسلامی
🔹
«شرح اسم» روایتی مستند از زندگی رهبر  شهید انقلاب  از کودکی تا سال ۱۳۵۷ است. این کتاب با تکیه بر اسناد، خاطرات و روایت‌های نزدیکان، مسیر شکل‌گیری شخصیت، مبارزات سیاسی، زندگی خانوادگی و فعالیت‌های فرهنگی ایشان را به تصویری منسجم و خواندنی تبدیل کرده است.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/667053" target="_blank">📅 19:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667052">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700dbb08b4.mp4?token=cKQDMilTBhFZboZvJLG1KabQufMOzKn0RQq92t7ySuuoMOFIIFquvZMfo8KSVGybqLMtJvE_4jhXj7cDzPMrzdsumxj2QGRvyuFepKISUpoArbfIlu1wEf6Ij0IB4oOKY4Qfvk20oXN8hdwE6pzrDq5Q7tLm8QzEm3ALNyxRzhGuqZL5qAuBdf06efl_gJVSbFhwzrvTegNIGWwBTDAsdjSb9CoB3deeceSxY0oaKg7XQfystDmRWeb4kp48RNLlbgRLF_ce0sewvs-g4vlqb8P6k60mGHxo3K0dsV8HDt4VNjTeK-7f0BNSH0vzy5TrylNv3LsL59qkR19m9uGmUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700dbb08b4.mp4?token=cKQDMilTBhFZboZvJLG1KabQufMOzKn0RQq92t7ySuuoMOFIIFquvZMfo8KSVGybqLMtJvE_4jhXj7cDzPMrzdsumxj2QGRvyuFepKISUpoArbfIlu1wEf6Ij0IB4oOKY4Qfvk20oXN8hdwE6pzrDq5Q7tLm8QzEm3ALNyxRzhGuqZL5qAuBdf06efl_gJVSbFhwzrvTegNIGWwBTDAsdjSb9CoB3deeceSxY0oaKg7XQfystDmRWeb4kp48RNLlbgRLF_ce0sewvs-g4vlqb8P6k60mGHxo3K0dsV8HDt4VNjTeK-7f0BNSH0vzy5TrylNv3LsL59qkR19m9uGmUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرگی زاگربلنی، اسقف اعظم کلیسای ارتدوکس قرقیزستان: رهبر شهید مانند پدر امت بود و با چشمانم دیدم که ملت رهبری را مانند پدر خود بدرقه می‌کنند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/667052" target="_blank">📅 19:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667051">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1351a483e7.mp4?token=e7N3K_K1xwXw2xSAKgolt0vT2ktjWswimEpWxvHtZ-G0mVTzbLIBu2N0gmdpUV8he4shaoRow8cw3JWmk_VHhLPKAqI1mZKrkQuIJSG9lhbim2TUPBim9l0U3qqEXuW33nufpiMhhHpoowXNBNkqOVDJxpscV6soDULtr6DZSVOSeWjiE27HlpCKrnZ49HgH8U7JZBhMQua74YX41TrRMRJYcoyqRM_jc1ogqJjDBt1uvjskOoHrJWEeKEGb60TNE29A8nXlHum_yiBH24TEWLFt7-8a4PY_lkRpxrdQu2NwO6jgzZBcwk_E5H_Yer32V0WlMj0ecaPQcusFnRDPxmB4-gLgg1NZa8Oa3gEdKtkk_3p3hU6A-VV7AFdo6tw2Pocj9rA9SbHh9V-zJAB6Y6cA6bXcp_WU--OHDge7oO5IOkfLl_B1mVr3R5bhN9NVGt6VNTRsKs4IJd9UAR7vStQU6sIObrA4Tivh6FXiuPZbid81NlpRHOIMfmxv-Y18S7MpkHGBUDLAOuhQpZ6eJqOrc0MK8Cs4h_nPkfaC_InDYtDPxh76aqxJmVsIj-jfXPDHpo7vDMdCWAhV9FFX3zgjKMGJdBK1ULyXeDbetgtvZVPjzW5ykqDnZSSpZxrFNNVXE0DW2QEE1dRYg396lN2qRp8fRwrxS3aITmjlKfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1351a483e7.mp4?token=e7N3K_K1xwXw2xSAKgolt0vT2ktjWswimEpWxvHtZ-G0mVTzbLIBu2N0gmdpUV8he4shaoRow8cw3JWmk_VHhLPKAqI1mZKrkQuIJSG9lhbim2TUPBim9l0U3qqEXuW33nufpiMhhHpoowXNBNkqOVDJxpscV6soDULtr6DZSVOSeWjiE27HlpCKrnZ49HgH8U7JZBhMQua74YX41TrRMRJYcoyqRM_jc1ogqJjDBt1uvjskOoHrJWEeKEGb60TNE29A8nXlHum_yiBH24TEWLFt7-8a4PY_lkRpxrdQu2NwO6jgzZBcwk_E5H_Yer32V0WlMj0ecaPQcusFnRDPxmB4-gLgg1NZa8Oa3gEdKtkk_3p3hU6A-VV7AFdo6tw2Pocj9rA9SbHh9V-zJAB6Y6cA6bXcp_WU--OHDge7oO5IOkfLl_B1mVr3R5bhN9NVGt6VNTRsKs4IJd9UAR7vStQU6sIObrA4Tivh6FXiuPZbid81NlpRHOIMfmxv-Y18S7MpkHGBUDLAOuhQpZ6eJqOrc0MK8Cs4h_nPkfaC_InDYtDPxh76aqxJmVsIj-jfXPDHpo7vDMdCWAhV9FFX3zgjKMGJdBK1ULyXeDbetgtvZVPjzW5ykqDnZSSpZxrFNNVXE0DW2QEE1dRYg396lN2qRp8fRwrxS3aITmjlKfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر‌شهید در گفتگو با خبرفوری: وقتی خبر شهادت رهبرانقلاب را شنیدم خُرد شدم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/667051" target="_blank">📅 19:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667050">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhgeZ8aTbFN8m-ZaVOy2GHI2hvKIqJNBL0IlcIC5pd3uDDTc6BgVOe9X6s94on44BvVDNVX3ta1xfxJyFyjB8MWmp8JtNWg3XrovpcYNEPqAPYQIPyGSv08tUJG98Wt5pyYGSpEcW2vrAZ0vmWps3XSEWxHayj5-5mdV0ebg-o1OT2GHj5D0VWGl0CTIXpny5faSwCssKoYMVVl_E6P_H0Iwj0eymQKiYSphTU3UJTEVtMyD70yzIJkvtN4fik_OqSYLSvw2uogddU7ejRai0SVmdvLVxOKebKzArpNoi8UBWb7NoRRrXpzI5jXIzKSGjvZywabNxFh1d3p_aueYuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر خبرگزاری آسوشیتدپرس از مراسم روز یکشنبه در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/667050" target="_blank">📅 19:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667049">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f306a56e29.mp4?token=WMqfR_-QqJAWv249KDugO1zaQaPG1uVyBHC330yXId8NS4s5oGUoo2J_yCY4rAiqLshzl8CKXuv0FBRuJX6soIUuVXX0nbyRJmCvCFVeAkq0tc0Qnz9HzutU3VZyz7vo2SFPho0yA26KYD-iCwWtN8Mt2INi7b8qBJVf0kMKtJpKjIaSHysfeGgoPuZPR3Q4gy1lSa2WOMisP-AZyxLuhBHzlfAAsQmbDLtOZ3KyB6Fi4QGQsTW5TnDGQed7qKSXP0hE6pOpaAJli32vs3rpAtUzIY3StHvwVOLlbKcVp-Be0CxlrCvtVrb4_1c6-vVGMXVZ51y565OhBAXtOeCtyqXlWQRXUdTHXp3L2xYV2NfbetVCUTvr6ZVbCQRBspF3owbLqOYmBLPiG2oepuM2fyU841K1riTQ4wJB0hW7m-GS-ssqvWpII_bxdKBr2WeAb-uOuXF1la38hvztZMk0_xjbRbZbr2BzjZdy_gLKwXWatXDhDB3GaqgDqWxAbso-4Z8GoV-XwqKTtNikbQSnZ_X6FKgkcT88dLAMrljTJGfJAZIHWkDQKRUehYluKaXdlE365BRV-lWAkv6ken1KSl9TFtLaMa3RY3aku75QaiKnqs3YVKzqaOort3aW_6jeAephjciRzc9kD4E5KQQCDNtRnDFRYZ5tpq8OtMdkYII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f306a56e29.mp4?token=WMqfR_-QqJAWv249KDugO1zaQaPG1uVyBHC330yXId8NS4s5oGUoo2J_yCY4rAiqLshzl8CKXuv0FBRuJX6soIUuVXX0nbyRJmCvCFVeAkq0tc0Qnz9HzutU3VZyz7vo2SFPho0yA26KYD-iCwWtN8Mt2INi7b8qBJVf0kMKtJpKjIaSHysfeGgoPuZPR3Q4gy1lSa2WOMisP-AZyxLuhBHzlfAAsQmbDLtOZ3KyB6Fi4QGQsTW5TnDGQed7qKSXP0hE6pOpaAJli32vs3rpAtUzIY3StHvwVOLlbKcVp-Be0CxlrCvtVrb4_1c6-vVGMXVZ51y565OhBAXtOeCtyqXlWQRXUdTHXp3L2xYV2NfbetVCUTvr6ZVbCQRBspF3owbLqOYmBLPiG2oepuM2fyU841K1riTQ4wJB0hW7m-GS-ssqvWpII_bxdKBr2WeAb-uOuXF1la38hvztZMk0_xjbRbZbr2BzjZdy_gLKwXWatXDhDB3GaqgDqWxAbso-4Z8GoV-XwqKTtNikbQSnZ_X6FKgkcT88dLAMrljTJGfJAZIHWkDQKRUehYluKaXdlE365BRV-lWAkv6ken1KSl9TFtLaMa3RY3aku75QaiKnqs3YVKzqaOort3aW_6jeAephjciRzc9kD4E5KQQCDNtRnDFRYZ5tpq8OtMdkYII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مصلای امام خمینی(ره) در روزهای وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/667049" target="_blank">📅 19:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594503be2b.mp4?token=RKGFYAs2VfYsbQ_utd5RuLd9ZgG7OQHU0LzFBU1BA3uL5fR7TBzNoqYuiDcFe-vJ82tuRmTPT9feFJp5O10eW4kQlouwCTgRg3qnWTjqA1u3VjU2Lhdz6Id4G08p7-7oum7MlNNyJ7kBgYFBxAESC09XLGwxK96SHi7ZXWBCCJqWzDYxNsftjW2R8RbQgxMPqIa_qmwH5Ttbzd1jXFvpnQIrMZDq9VaOfepEO62DVlhMDDU1zKgOItDclRBeoi2zBT3HTkIpCSri6GdLBUcblmHwGyw4sQUWXQJH5PYe3utluW01lPBXCYQ0gc1BHUKZjvFCRKMOeP9UQg4riVKq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594503be2b.mp4?token=RKGFYAs2VfYsbQ_utd5RuLd9ZgG7OQHU0LzFBU1BA3uL5fR7TBzNoqYuiDcFe-vJ82tuRmTPT9feFJp5O10eW4kQlouwCTgRg3qnWTjqA1u3VjU2Lhdz6Id4G08p7-7oum7MlNNyJ7kBgYFBxAESC09XLGwxK96SHi7ZXWBCCJqWzDYxNsftjW2R8RbQgxMPqIa_qmwH5Ttbzd1jXFvpnQIrMZDq9VaOfepEO62DVlhMDDU1zKgOItDclRBeoi2zBT3HTkIpCSri6GdLBUcblmHwGyw4sQUWXQJH5PYe3utluW01lPBXCYQ0gc1BHUKZjvFCRKMOeP9UQg4riVKq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری شبکه سه: ملت ایران تا زمانی که نفس می‌کشد، میناب را فراموش نخواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/667048" target="_blank">📅 19:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
برنامه وداع در مصلی به دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667046" target="_blank">📅 19:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEDAAT-JEQ_mwCwRf8p20bsmYpgxpU4FzknnxKL32w7kTZP3H-ahQ7qwxri1oLkVmhyC0tI-DviMsXt76Iwy0dRF5KeyUa9kFrxo_N8kDPR9c6wNytGwiuVyfhkm6Zq3mYGh_iJHr6NWiPM4KoLySC6Vb_M-biqVlzVqBdNO-f4dQn83z4MqJxY-qKYrN5cLi_3_neoqLgVw3b1etjm2sNd2e60oLZ_wm8nkx5qic7Hw2KNqHlCE3ChnYRjYxZPZZWVig-WreaAUw5-5ukbPEBKu4DyvQHypzOT6D9lgVU977E9LxYLNGMqbcEzASJosZmYwahyss8ydTDWmYxnT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: فردا جهان شاهد حماسه‌ای از جنس عقلانیت انقلابی خواهد بود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/667045" target="_blank">📅 19:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2069e9781.mp4?token=brRzr9p02YQgoLM51nNzF03ci5qqMWyn2fZU0YZUeYJFzNxBu6oA0gtsnl4mwqDZASFAydkavA-UXJPsUKLEbfiOrp87PLshtTZQ-CspmfGmYlhqKrizf-a_ebgaVd8Ba0KjnxQIYdR9KXoqMC2tlRbLCmq43SPRG2tcV-3UQR5KmT8eaVXOsYD6Kzaw_AlxH8Ys9EhPF3uL5DHAe3CbrZMdwa-viHXwYReGME0scBSui_Sn1Kd-iV4lXApRhS9mpFTNLoPQeIVDbVeBjiDwaHAySe7N5av1Y1cMGu0uZGbM2fUMQB8R3ZcjpOUeuQwZmqwLiYND2gHvt7jJdN2g0hs33gHO7Mb0LZ6wIROf3rT8r4zncExEelccmz-9bjBFhGVolCoiLVAn-bSYF4tLTKsl-FZXD0CCTAeqhsF96heWhtEJCfWjPxe3FoJmeZf34RNvZzoQh9qzVHIXP3SlGKDfXIC1-Rozgj8jqWeZk85bpeWsG3fHpdnF3gm9Sjs7z29MKLvxMiX9fe5lKT98b7L6xkhdsUp_y2AH1w36a9DpkCdZ7yHXgltGcLKfkeefaGLvC0Z56Gvz4f8rpgK8plZlBehrhBO4cHv8fLPSzvsTqq00drLN9maMgkYB-Iih3dmdiO27TlLiq7_ypDGsNkN_DRnUaQx6HDDie9aWi0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2069e9781.mp4?token=brRzr9p02YQgoLM51nNzF03ci5qqMWyn2fZU0YZUeYJFzNxBu6oA0gtsnl4mwqDZASFAydkavA-UXJPsUKLEbfiOrp87PLshtTZQ-CspmfGmYlhqKrizf-a_ebgaVd8Ba0KjnxQIYdR9KXoqMC2tlRbLCmq43SPRG2tcV-3UQR5KmT8eaVXOsYD6Kzaw_AlxH8Ys9EhPF3uL5DHAe3CbrZMdwa-viHXwYReGME0scBSui_Sn1Kd-iV4lXApRhS9mpFTNLoPQeIVDbVeBjiDwaHAySe7N5av1Y1cMGu0uZGbM2fUMQB8R3ZcjpOUeuQwZmqwLiYND2gHvt7jJdN2g0hs33gHO7Mb0LZ6wIROf3rT8r4zncExEelccmz-9bjBFhGVolCoiLVAn-bSYF4tLTKsl-FZXD0CCTAeqhsF96heWhtEJCfWjPxe3FoJmeZf34RNvZzoQh9qzVHIXP3SlGKDfXIC1-Rozgj8jqWeZk85bpeWsG3fHpdnF3gm9Sjs7z29MKLvxMiX9fe5lKT98b7L6xkhdsUp_y2AH1w36a9DpkCdZ7yHXgltGcLKfkeefaGLvC0Z56Gvz4f8rpgK8plZlBehrhBO4cHv8fLPSzvsTqq00drLN9maMgkYB-Iih3dmdiO27TlLiq7_ypDGsNkN_DRnUaQx6HDDie9aWi0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقایق پایانی وداع با امام مجاهد شهید و ازدحام جمعیت در صحن مصلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/667044" target="_blank">📅 19:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5PvhyA-O-jGnW4BVrEo02RTO-6CEVLU-u2y258eH3r2R8oL4Oi0XHLsFYY44iBlsGrEPLxWzks2t9M4zuSNlWK7OyiNE_qatp9qw4bWxN1bmdyQRdcyt0BSIPRmqL2HMRb-2gBtBHOHnIEU8CKyJjOTfh7frET2zqMdtgsc_zvZEOmLXI9m_tNd-SRKClBKgOSY6Zj11B3qCpOPLC1btQ4urypyxN8zZOjXVW799OHEwEhNirBs3sfRAMuyIq6EvEW_-yv23Td9QnV7ibXKa4M3AS1KqDSZjINtRyYtzofZic45aWjN4mmiQEzf_2If-dKblpRQSTrImj2zGpO1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در موکب خدمات رسانه ای همراه اول صورت گرفت؛ راه اندازی استودیوی تولید محتوای هوشمند برای خبرنگاران
🔹
همزمان با برگزاری مراسم وداع با رهبر شهید انقلاب، موکب خدمات رسانه‌ای همراه اول با هدف حمایت از خبرنگاران، عکاسان، مستندسازان و فعالان فضای مجازی، امکانات تخصصی سخت‌افزاری و نرم‌افزاری خود را برای تولید و انتشار محتوای حرفه‌ای، در اختیار اهالی رسانه قرار داده است.
🔹
در این موکب، فعالان رسانه‌ای می‌توانند با بهره‌گیری از تجهیزات پیشرفته تدوین، اینترنت پرسرعت و مجموعه‌ای از ابزارهای تخصصی هوش مصنوعی، ویدئوهای خبری، گزارش‌های تصویری، پادکست‌های صوتی و سایر تولیدات رسانه‌ای خود را در کوتاه‌ترین زمان ممکن تدوین، پردازش و منتشر کنند.
🔹
این خدمات با هدف افزایش سرعت، کیفیت و دقت در پوشش رسانه‌ای مراسم و تسهیل فعالیت خبرنگاران و تولیدکنندگان محتوا ارائه شده و امکان استفاده از قابلیت‌های نوین هوش مصنوعی برای ویرایش تصویر، بهبود کیفیت صدا، تولید زیرنویس، خلاصه‌سازی و سایر خدمات تخصصی را نیز فراهم کرده است.
🔹
از تمامی خبرنگاران، تصویربرداران، مستندسازان، فعالان شبکه‌های اجتماعی و تولیدکنندگان محتوا دعوت می‌شود برای بهره‌مندی از این خدمات، با همکاران موکب خدمات رسانه‌ای همراه اول، هماهنگی لازم را به عمل آورند تا ضمن استفاده از ظرفیت‌های فنی و تخصصی موکب، تولیدات رسانه‌ای خود را با کیفیتی بالاتر و در سریع‌ترین زمان منتشر کنند.
🔹
موکب خدمات رسانه ای همراه اول، در خیابان آزادی تقاطع آذربایجان، با مجموعه ای از خدمات و پشتیبانی های تخصصی، در خدمت اهالی رسانه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667043" target="_blank">📅 19:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قالیباف: صلح در لبنان جز از مسیر ایران ممکن نیست
قالیباف در دیدار با هیئت حزب‌الله:
🔹
برقراری صلح در منطقه تنها از مسیر ایران می‌گذرد و دیپلماسی ایران همواره با آمادگی دفاعی و روحیه رزمندگی همراه است.
🔹
محمد فنیش نیز تصریح کرد که توقف جنگ و پایان نهایی آن در لبنان، نتیجه‌ی دخالت جمهوری اسلامی و الزام آمریکا به اجرای توافقات است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667042" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMsKiKG_gGH_1T1HFnhcAa-ro5B9cuzKHjjuzSvQveKqaPAqqyY9dBNzSueuPBo0NxEm7ISQYSOy7E7XkhndQYiqhAYWmDaDw8QTcRIEHycjOkssoFyzBrr8A3LbrBGpcfh4GESSIHXEvNA_ZJGGHzcpSsD-5fwMgd0f7UTIAge9oHEnewp12e03l8Z6hjju0d8_neP5jebwX5uKojKQNIwECWOQ-zKKzbPYsVOb2tE_f-9xoWrk0nKjSeStQNk40TYrKa1vBB-5mqWwShQy_yzkE_1XMPgCJbZkLGqlj9N00JFFaUX1BaVbpHYlPFcG8gB8k5yZwaC0kmZq86GPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌ی قضائیه منصوب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/667041" target="_blank">📅 19:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjyFG80fyTqbVkyoQEq_d6qzpcvgKia5difrLom0VbFgP7iULRzQqWQqabh9msAK0djaellfblFAiPU-ParI5ijL5IgUK9MsZEBMsrOufU3SRPQnuvoRG_-IbmsyirNWekgKjvntCBPoh2Xlm0QyTd3O_gr9jta_GRFHaRu2J9cG91pYj7nIZ7ZMmJhwiDkREtxhRj32Y1un7AnZ5wzQZY3sGQiBy-IrAWkKT8a-gtQv4_ILor-FOkxPPESOLDaOPkOxWV7MhK3n9k4IiIjeSc56g5Ei-BLXTslLR00lAn0O4C4uH6ymqVgRzQgrJDLtlqgZ5T6ovNHO6AWWtdALrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دنیا بداند انتقام قطعی است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/667040" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZ6tXyWHaLoyr2BB3tvh2KE4aVnQLf9wAOnuG72fmgFgjM-tJUJJs2bLWHcDiaQ1f3iLQDEWC_1ErxlHbk4hDpl7NeNuAtTLKDJwTa2bpRMIMB7QK8hP4I6XXEAcilu-8BFVgZYLI9qWmH26V0Y8HltGgztk0Wn4W0K7uToBF7x4Mxb3uwxuHEWKqTeXxmiX7aPvqy996uCIQzbzHDlF3lpMWal0pRdhSIh6TpVjEU_h4NKQvqvj7I1CezX_pT9bVPlLCW7RfWFlUplo3V5HG7r3wRi4hwJ2UZBYzIYHIBucpQ-hEyk889tuAIvdVFzstIYUKiNRFqvPsLfutF5T8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667039" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
