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
<img src="https://cdn4.telesco.pe/file/Ba70mH17qF5gSeJsIf0rVjuOb9zuzSqTcJ9ZWYCNaJSEbL28_wf6dADtwE6JSe5jaapxqEpYKe_npGHzgc-6CSmhK9OWZIqZKWCj58UMZzQke5sDJf3tQDF6mN97ZBLKPRbig7MYAicGsmOG7uLr93t1zbU0bq8hDXXZpFOSur4tMMmqpePiRq2wybgWFL-ooGizF2FeteTn1rG1zRmwaxnAG6krq2dY12p3yMbPK90KCPqXQi1Mqd9j30sHdz4trlqGdAZGJSh0EQNOCHLWxZiSL01yNnBdPX8KNa3v31AdBYrEvYZ9FvBQ1Oooh-xkSYQw_VbM3XtT4XQkqWZ_ng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 11:38:34</div>
<hr>

<div class="tg-post" id="msg-149485">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">طلا منفجر میشه
💢
تحلیل عجیب
🚨</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/149485" target="_blank">📅 11:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149484">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=owIbhuGXV52z0x7yX3wUuynZINuHuqTI3t4wpSG1GhmTsPT3CmvBMMpb-WVnF8uOh6lWsA7mxKEObxGtxEZIuBEXJjIx-aTvRPEvhOeaTtySISUG4-5MNeahhofklJwGfMf2nkm_qTq2qJmLJlg6xPvM7m-KlVEOumeKXIaUgZE0eJ29UKXzdt_QIi9Nr2W7j0LOQuQE-vdG7BD-SucW8miZP3OLK_PpfJnScJJjcOYMywjhLu9WV8hoh7eh1HNw79DyNIWFbkXmA5-P3sT7wC_etJpTLhpQH-v9sJFlKnH8rDIfBVJibYHlW1eCE1EjYrOEjWmGbRzyE1QquWYT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=owIbhuGXV52z0x7yX3wUuynZINuHuqTI3t4wpSG1GhmTsPT3CmvBMMpb-WVnF8uOh6lWsA7mxKEObxGtxEZIuBEXJjIx-aTvRPEvhOeaTtySISUG4-5MNeahhofklJwGfMf2nkm_qTq2qJmLJlg6xPvM7m-KlVEOumeKXIaUgZE0eJ29UKXzdt_QIi9Nr2W7j0LOQuQE-vdG7BD-SucW8miZP3OLK_PpfJnScJJjcOYMywjhLu9WV8hoh7eh1HNw79DyNIWFbkXmA5-P3sT7wC_etJpTLhpQH-v9sJFlKnH8rDIfBVJibYHlW1eCE1EjYrOEjWmGbRzyE1QquWYT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از برخورد اتوبوس و تریلی حامل میلگرد در محور بیرجند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/149484" target="_blank">📅 11:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
گاردین: عباس عراقچی، وزیر امور خارجه ایران که پیش از پزشکیان به نیویورک رفته بود، قصد دارد تا یکشنبه ۵ مهر در این شهر بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/149483" target="_blank">📅 11:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نشریه CNBC صادرات نفت خام عربستان سعودی با وجود قطعی خط لوله به بالاترین سطح از زمان شروع جنگ ایران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/149482" target="_blank">📅 11:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149481">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کارشناس صداوسیما:آمریکا تو جنگ نشون داد طبل تو خالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149481" target="_blank">📅 11:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149480">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=dBCahm4YcDfLb6qgLd2cahG1JOCBTuAQSnDUuV46UOH4Ebaav6zrvIEh5lT54piCoV-3mtoURXdXA5w6W9v5UIfDZw5Q10CvLusWXbTjQLvh7m2oboW-2dAfH98p4rNZcBHEtuSz5niMAxWIcY97peNbNOCabbzAQCnTGoFFKzkYh6I4J239l-_qCIrOKoY9rprL7eUw77aQE8K3eWRnPK32KOAXpB5JSgNkZst5STljmqwUVsY0yCZaZB5veeUgit9PLTCU6QymfpO_I8CGreUePvQJ9rkodr6-LjAL4siN4UiK8Ang4_o46zTnRsOay9LZX71D6erUM5m-LTABQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=dBCahm4YcDfLb6qgLd2cahG1JOCBTuAQSnDUuV46UOH4Ebaav6zrvIEh5lT54piCoV-3mtoURXdXA5w6W9v5UIfDZw5Q10CvLusWXbTjQLvh7m2oboW-2dAfH98p4rNZcBHEtuSz5niMAxWIcY97peNbNOCabbzAQCnTGoFFKzkYh6I4J239l-_qCIrOKoY9rprL7eUw77aQE8K3eWRnPK32KOAXpB5JSgNkZst5STljmqwUVsY0yCZaZB5veeUgit9PLTCU6QymfpO_I8CGreUePvQJ9rkodr6-LjAL4siN4UiK8Ang4_o46zTnRsOay9LZX71D6erUM5m-LTABQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان در مصاحبه با شبکه سی‌بی‌اس آمریکا: وقتی آمریکا به آنچه تفاهم کردیم، عمل نمی‌کند، مذاکره کردن چه مشکلی را حل می‌کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/149480" target="_blank">📅 11:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00db30387a.mp4?token=l5NplzeXOevMh7iXijICkcV_CH4MVVTmfDipsnIERclUwd0mwkei8LRcoJkfBcnWRNfon1I3DjlqWQRcgpQGBMUnGtJ-2VYCp8e1rwTcqwND5spGlr_jxJy9g3mXeQAvOZkz6k9d6gnTr5UT2lNZ4w5sY7K1ul9lZY3iBUQuFROglZ_pgVGlAoWTlCaqfD3kl1_HIAHgRW1cuEgWJq10j-xm_cfvFJGzd1vDmVKZOAEqCg_X4-uUtpYaqpLjRhZif_8_kDuhYhfb322Pbii68Z9l7SKH_aj8ArnthXKaftatHkGbo3dBVdLWaohwah5kQKIfbJJuMo-3l3amBmsUNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00db30387a.mp4?token=l5NplzeXOevMh7iXijICkcV_CH4MVVTmfDipsnIERclUwd0mwkei8LRcoJkfBcnWRNfon1I3DjlqWQRcgpQGBMUnGtJ-2VYCp8e1rwTcqwND5spGlr_jxJy9g3mXeQAvOZkz6k9d6gnTr5UT2lNZ4w5sY7K1ul9lZY3iBUQuFROglZ_pgVGlAoWTlCaqfD3kl1_HIAHgRW1cuEgWJq10j-xm_cfvFJGzd1vDmVKZOAEqCg_X4-uUtpYaqpLjRhZif_8_kDuhYhfb322Pbii68Z9l7SKH_aj8ArnthXKaftatHkGbo3dBVdLWaohwah5kQKIfbJJuMo-3l3amBmsUNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا: آمریکا و اسرائیل هر کس که دلشان می‌خواهد ترور می‌کنند، بعد می‌گویند او تروریست بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/149479" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149478">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c281dc401f.mp4?token=mDLIKFs3LaTfjxZ2KNAaqJ_J6FFELdZ1wva_G9XxDLt_U6gQzekb7oAqkobs0UoApbqQih1PapusWFDXRw_wMIhm6WhddHTphZFOWAuz25EvqZ2lzrqiVz1cQFeaxLi1kH2XmZbsXSOlf8NAaj4uOOtrsVacIreddqnYBNotNvAjCyznthBy0rOM9bir9onvHeD94GOkKYaRiDGUsnwSSyJu8XWwcf7mF6zehapM_0K35w0DGt3Dl1peyatqPZE5NTd5qk4ykTXB9DhQFoZ42qqp3mP1pOVEcV4FNvcwJa4QYKnJWI2EiZbGOl4nbDLXUZfq5htMDZ9p6JrnlwBTxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c281dc401f.mp4?token=mDLIKFs3LaTfjxZ2KNAaqJ_J6FFELdZ1wva_G9XxDLt_U6gQzekb7oAqkobs0UoApbqQih1PapusWFDXRw_wMIhm6WhddHTphZFOWAuz25EvqZ2lzrqiVz1cQFeaxLi1kH2XmZbsXSOlf8NAaj4uOOtrsVacIreddqnYBNotNvAjCyznthBy0rOM9bir9onvHeD94GOkKYaRiDGUsnwSSyJu8XWwcf7mF6zehapM_0K35w0DGt3Dl1peyatqPZE5NTd5qk4ykTXB9DhQFoZ42qqp3mP1pOVEcV4FNvcwJa4QYKnJWI2EiZbGOl4nbDLXUZfq5htMDZ9p6JrnlwBTxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور در مصاحبه با شبکه سی‌بی‌اس آمریکا
:
هیچ ضمانتی وجود ندارد که آمریکا و اسرائیل دست ترورها بردارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/149478" target="_blank">📅 11:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149477">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بغداد: مذاکره مستقیمی با آمریکا برای مستثنی کردن برخی فرودگاه‌ها از تحریم پروازهای ایران انجام می‌دهیم
🔴
هشدار می دهیم تداوم بحران‌ها، پیچیدگی اوضاع را بیشتر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/149477" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
روزنامه کیهان خطاب به پزشکیان:
چرا گفتی به دنبال ترور ترامپ نیستیم؟
🔴
انتقام از ترامپ یک ماموریت الهی و حتمیه، خون‌خواهی مطالبه ملت ایرانه و ترامپ باید کشته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/149475" target="_blank">📅 10:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149474">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCk-rm8XwdwzairOFdKzX2r1FfcHpp-QLDsPTPbl6dym65LjaJL1RzGVyaj6x9T4v9moO0Y_IWAgbbN7DNFVRpnvyoBlLju2d8wLn3_x0wiLY6d5jA_MP1ue-j2AzMSy4skdQCZ6_yBDIqbNg9gJGEWUMvI0K1Os7-YMs1gQvJO-HJRSp-jVB6pIpwphtjrT0O48eknsjMbpuAycEr2gqabQv858sH6uBVT3z4hnMjxUFhbpXW9-fc8rivdqeLJXyXEOamyC5bTbWuViIWaz4qW6jmP22SsT5YT7x44xq8iB_htZC-PtAq9uS_8zJj6NfvoOK7nRhT-eEOx-7id4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از دیروز هربار اینستا باز کردم سردار بلاگر اومده اکسپلورم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149474" target="_blank">📅 10:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149473">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان به سی بی اس: با رهبرمون ۷ساعت رو زمین نشستیم و حرف زدیم و کاملا سالمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149473" target="_blank">📅 10:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149471">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
توافق احتمالی فقط درباره پرونده هسته‌ای نیست
🔴
در مذاکرات جاری، علاوه بر برنامه هسته‌ای ایران، موضوعاتی مانند بازگشایی تنگه هرمز، محاصره بنادر، صادرات نفت و دارایی‌های مسدودشده ایران نیز از محورهای اصلی اختلاف میان تهران و واشنگتن هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/149471" target="_blank">📅 10:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149470">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اتحادیه اروپا: در نتیجه پیامد‌های جنگ ایران بر بازار‌های نفت و گاز با بحران قیمت انرژی مواجه‌ایم
🔴
اگرچه اکنون آمادگی بیشتری نسبت به زمستان سال ۲۰۲۱ داریم، اما دولت‌ها باید آمادگی‌های خود را برای زمستان پیش‌رو افزایش دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/149470" target="_blank">📅 09:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149469">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7KUMZayGuYHSCOkRVVVG0F1rPzBQKQmg-_Dc5UB6EXBTqmXFAujUQytsXU5Ojgi4fU5AEI0u2JYq4_97w4i6x2dFYO6IGp4_yVIPUonVjXvPXj4NArUmqp96m5tM7bloBvLP-KenjOPFncFdyaQ2iqCPaBLjy91AXMbR7hXBf7RzCS6Vnpbc7WxSUz2M4n3gon6RCbza045UweXI_Ami-bBXxtG9TnVNjLDinDKEvBHNel7dwKvwOjmY_kWxGyx4NDNZfrF6ZVEHl92aczMslAJn2f5TpWZBHt2FjCjOUr6gayh095GFWr3em-59MLEhgKIUdHoqDJ6-DCuv7HMAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: ایران در میدان دیپلماسی فعال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/149469" target="_blank">📅 09:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149468">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وال استریت ژورنال:
🔹
طبق گفته مقامات آمریکایی، ترامپ پیشنهاد ایران مبنی بر آتش‌بس هفت روزه را رد کرده و به مشاوران خود گفته است که انتظار دارد بمباران ایران پس از انتخابات میان‌دوره‌ای ماه نوامبر از سر گرفته شود.
🔹
پیشنهاد ایران به این صورت بود که در ازای لغو…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/149468" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149467">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پنتاگون: شمار نظامیان آمریکایی زخمی در جنگ با ایران به ۸۶۱ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/149467" target="_blank">📅 09:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149466">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olGkCmlw7OrGDdJFD_Vf3CC2Zp5roYKtulqmMuRe8rnQX98nRDLeIMBp1ZOJeE8nME19VxI3cWSirmn0qetreohnLAlgb6pY3s1a0SundR69Ae6rzYhzsYszTQfrqK5yqCYAPc0v7y0iNR3X55amBjZQXqXHCd2oQq6Dz81n-OqXLJ5iL624JHQjPKhrD166OLK0fKRoLygiVc9c_GFQRrbUYzG4r01Nrp-C9jAUkQV3xrso_PdX7V5yAwCDhRz9G3Kp4H3wtOj3tnFQAn1AWsEY_oQNo9KRkFHg8siKFUDXjjazeuP3Fp0XnkV-Q4gYcD0FQnbhqjkcVGrnlGJlEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: تنگه ترامپ!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/149466" target="_blank">📅 09:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149465">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
تریتا پارسی: نتانیاهو ممکن است پیش از انتخابات اسرائیل به ایران حمله کند
🔴
‏یک تحلیلگر اسرائیلی به من گفت که نتانیاهو ممکن است پیش از انتخابات اسرائیل حملاتی علیه ایران انجام دهد؛ به‌ویژه اگر اعداد نظرسنجی‌هایش شروع به افت کند.
🔴
‏ او محاسبه خواهد کرد که این حملات نمی‌تواند ایران را شکست دهد، اما ممکن است رقبای انتخاباتی‌اش را شکست دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149465" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149463">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
علیرضا تقوی نیا، روزنامه نگار وابسته به سپاه: جنگ سوم در خاورمیانه میان ایران و اسرائیل و آمریکا، قطعی و قریب الوقوع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149463" target="_blank">📅 09:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149462">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
توضیحات عراقچی درباره طرح هفت‌روزه بازگشایی تنگه هرمز درصورت پذیرش شروط ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149462" target="_blank">📅 09:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149461">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bec11227.mp4?token=SyX5m6t048dYNQuQqGkxDkb_PBJm0OOUlHVKJKEMX-he2k7BbktcGLV0wsTDXxjAYTyNV2aJ3HOzW4Wo0ZfuCY1ZPkclpOede7vBXlSoZzNaj3IBWihrJPGVwvFCQ747m5zJVx6HKEfjAKSFgbrTKzyS6PAnBwjmSD8igz-j33arf7QG91kZSFTu3YCu8SBNHbjb6pRWUlzxybax0hP8UZeMUKwYdH2ycyhocZzdebkSchR9FupM0A9DBIa5HBeo1UjvQyW43aHYcH2cJ1oOyJbXUc_EK67I2ekkpMNXaJ5nV2bRaU3sP12ZFXsdmJPsiiw9ELj2ntdDSyClOJsTyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bec11227.mp4?token=SyX5m6t048dYNQuQqGkxDkb_PBJm0OOUlHVKJKEMX-he2k7BbktcGLV0wsTDXxjAYTyNV2aJ3HOzW4Wo0ZfuCY1ZPkclpOede7vBXlSoZzNaj3IBWihrJPGVwvFCQ747m5zJVx6HKEfjAKSFgbrTKzyS6PAnBwjmSD8igz-j33arf7QG91kZSFTu3YCu8SBNHbjb6pRWUlzxybax0hP8UZeMUKwYdH2ycyhocZzdebkSchR9FupM0A9DBIa5HBeo1UjvQyW43aHYcH2cJ1oOyJbXUc_EK67I2ekkpMNXaJ5nV2bRaU3sP12ZFXsdmJPsiiw9ELj2ntdDSyClOJsTyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پزشکیان: روند توافق، با پذیرش آمریکا آغاز می‌شود
‏
🔴
مسعود پزشکیان، رئیس‌جمهور ایران، در پاسخ به پرسش CBS درباره زمان دریافت پاسخ آمریکا به پیشنهاد تهران گفت: اگر این پیام به رئیس‌جمهور آمریکا یا افرادی که در مذاکرات دخیل هستند برسد، طبیعتاً از همان روزی که آن را بپذیرند، روند آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/149461" target="_blank">📅 09:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149460">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6e918d01.mp4?token=Arz46opZbHffazlb5VPlsdG0pUKoBGNqI35nuSRnP8M884ol7C0kc6Q03-Qb94GonRTW78YZO0ZdjKGR54atyUxZD51AUtzRQX60pgD53gRwlMiMJN4dUog8qckrOxXMR0NhO9vLq24tcJf-9syJ-zYBuKd9KkqtlGxnbO-YhrYd1LqccGvIbC4VXgreaTNu7kBzeThDNcjPa3LGuLs0YjgZxUOImCyuOdqX-WR9Cf65lf-V29aNQfFP7klCEPZeL-h-Bz8YY037wKQjvE3RkK_lE0lNWEJJ4LqUP0y8nqA2Ae3iKnjdCmLHiZxy6r3UVwgsT-ux6O9DVXwwivvzj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6e918d01.mp4?token=Arz46opZbHffazlb5VPlsdG0pUKoBGNqI35nuSRnP8M884ol7C0kc6Q03-Qb94GonRTW78YZO0ZdjKGR54atyUxZD51AUtzRQX60pgD53gRwlMiMJN4dUog8qckrOxXMR0NhO9vLq24tcJf-9syJ-zYBuKd9KkqtlGxnbO-YhrYd1LqccGvIbC4VXgreaTNu7kBzeThDNcjPa3LGuLs0YjgZxUOImCyuOdqX-WR9Cf65lf-V29aNQfFP7klCEPZeL-h-Bz8YY037wKQjvE3RkK_lE0lNWEJJ4LqUP0y8nqA2Ae3iKnjdCmLHiZxy6r3UVwgsT-ux6O9DVXwwivvzj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پزشکیان: در صورت موافقت آمریکا، به چارچوب توافق اسلام‌آباد بازمی‌گردیم
‏
🔴
مسعود پزشکیان، رئیس‌جمهور ایران، گفت تهران پیش‌تر بر اساس تفاهم‌نامه‌ای که در پاکستان امضا شد، به توافقی دست یافته بود و چارچوب کنونی نیز همان اهداف را دنبال می‌کند.
‏
🔴
به گفته پزشکیان، خواسته‌های مطرح‌شده در آن تفاهم‌نامه اکنون به مراحل مختلف تقسیم شده تا روند توافق به‌صورت مرحله‌ای پیش برود.
‏
🔴
او افزود: اگر آمریکا با حرکت بر اساس این چارچوب موافقت کند، «همه‌چیز به شرایط پیشین بازخواهد گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149460" target="_blank">📅 09:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149459">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d078d7d0.mp4?token=czWAPYlWp0ubpjXcoPg38lC4270Fmc8R3Zs_cPFaM6A7aGVn2v2uG7DSBjlEdmTD4hxzimDdBJYMcfol-ZKfhPfQTizQReG-aWi91KLKo4Zy6UxoA1bwhTTunvHT63QFZuYFKYOszoqWwp8b-Z9C22ZTKv-BLR1xTLBzf7Ul_RNzL09i3K94RTdOWRkYnm_dWXgoj8UpUq1pn23329dbkXLN6TB7GfAX43rvJuwS3GywLSphCRuYsHqOsBug1xy_IANaRyaYtdaYmjFDbl0mdpoELwIdBVD9-BaEKroJb2zrFvvvuLdOedn8vBA5sVO7-GBr-IMa1cqw0n2dIzc-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d078d7d0.mp4?token=czWAPYlWp0ubpjXcoPg38lC4270Fmc8R3Zs_cPFaM6A7aGVn2v2uG7DSBjlEdmTD4hxzimDdBJYMcfol-ZKfhPfQTizQReG-aWi91KLKo4Zy6UxoA1bwhTTunvHT63QFZuYFKYOszoqWwp8b-Z9C22ZTKv-BLR1xTLBzf7Ul_RNzL09i3K94RTdOWRkYnm_dWXgoj8UpUq1pn23329dbkXLN6TB7GfAX43rvJuwS3GywLSphCRuYsHqOsBug1xy_IANaRyaYtdaYmjFDbl0mdpoELwIdBVD9-BaEKroJb2zrFvvvuLdOedn8vBA5sVO7-GBr-IMa1cqw0n2dIzc-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سی‌بی‌اس:
«اگر رئیس‌جمهور ترامپ این پیشنهاد را بپذیرد، آیا می‌توانید تضمین کنید که نیروهای نظامی ایران به آن پایبند خواهند بود؟»
🔴
مسعود پزشکیان: «بدیهی است که به هر تعهدی که بپذیریم، پایبند خواهیم بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/149459" target="_blank">📅 09:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149458">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان به سی‌بی‌اس نیوز: ما به دنبال ساخت هیچ سلاح هسته‌ای نیستیم و به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود به کشور را خواهیم داد.
🔴
تیم ۶ نفره از نهادهای مختلف درباره سیاست خارجه تصمیم می گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/149458" target="_blank">📅 09:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149457">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8kWvPZB1ud-CDx0KZoI49EPtVXIfz7aQ-VUUmmBQvGVNZWrfVqa2lrYWjMBtPxmPiqRMSMhu4EgWWakUG9T3cah8AVGNg68ak_Mec8eRDu-oW5sxCbi4eo9pu8AHaI5DcAhtriPSvmu3wqHIhHqN_LjFa1lMn63XYV8ddCbzbv8gK3pVC1abbBuNxbtEw3BJKZn_iDAPAdcjGLKs86Rs7Yfpaa0vRVMXGLYyqW1dRSsHEY-C0G1drdLQGgcBzvDKdJfxNieTcm9g3d2ogZjP914dxbaplT67YwGWoMleSV2uFjkAPIemQ54jc9-Wk14xyu51GUwfsC3G1DPnmv6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر تند فرهیختگان علیه قلعه‌نویی: ۱۳ سال ناکامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/149457" target="_blank">📅 09:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149456">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8710f402b8.mp4?token=rdg5d9sXufo7d6rrDVFuv2BlvVYDP7QIZiY0Qd8JzMB9YTUMdrN97Y7bn4iGW6S9u3dH0qocgw2YSzDwdmZLRxTxF0i8xmHqRZPc8-OKlVbIpd-_ScNUgrW1UgS_8cKI3TfiBdkidoc3tv8SUxYRCxDRLF5ySodaxS3Qv8W4rwQyCRyX1PD4ymqxiCAWbTa5_eUO7FVqPiGeDKzbjtMB310CXvHDq5upls5KNGy4YUh2zmoa0YrQnVO8oH5xD-RyO_kTiaB4I2bMV5h0qRCN6PktpDvl-I6xP4T7oECitPzfp-YL5pRck-q1t00oAyDsnP9rNf1-GdFoTGGKy-wcqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8710f402b8.mp4?token=rdg5d9sXufo7d6rrDVFuv2BlvVYDP7QIZiY0Qd8JzMB9YTUMdrN97Y7bn4iGW6S9u3dH0qocgw2YSzDwdmZLRxTxF0i8xmHqRZPc8-OKlVbIpd-_ScNUgrW1UgS_8cKI3TfiBdkidoc3tv8SUxYRCxDRLF5ySodaxS3Qv8W4rwQyCRyX1PD4ymqxiCAWbTa5_eUO7FVqPiGeDKzbjtMB310CXvHDq5upls5KNGy4YUh2zmoa0YrQnVO8oH5xD-RyO_kTiaB4I2bMV5h0qRCN6PktpDvl-I6xP4T7oECitPzfp-YL5pRck-q1t00oAyDsnP9rNf1-GdFoTGGKy-wcqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اون دزده که تو مشهد گوشی یه رفتگر رو زده بود دستگیر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/149456" target="_blank">📅 08:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149455">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
الزیدی نخست وزیر عراق ، به اداره امور اقامت و گذرنامه دستور داده که به شهروندان ایرانی در فرودگاه نجف اجازه ورود ندهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/149455" target="_blank">📅 07:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149454">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
بر اساس گزارش شبکه نیوز‌نیشن، مذاکرات غیرمستقیم جاری بین مقامات واشنگتن و تهران در نیویورک، با میانجی‌گری قطر در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/149454" target="_blank">📅 07:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcY86Ugj6lg5zColOjxYhj3hH1RR3pqBL0X7GG8rYoETQBK9yFTJpzk_an4OsgRua6BXMLusecXCVlMIyQi2OEHBZDZe0HSPUCTORBzdjbPtQ6mAcPk2kVuO2hgOLH0aJSimFnP-VN9claivPHLjkvsZLkj4IxVcTwD-8Y2gyaM4lolH_4UShLs-Tp2c9k6eKwNHJmcqb_hSR79WPyLtAAR4iWTY9mAW7VXUju5gFjgUKzwZFUViv6CwCRG5COOTuv88EaZttXpoe8RvuvnNpeiLNA2erWm5yJhl9Fa2zWI1e4_KDzO2NGYlUM02xxzc41-x1Xio5bIBuWmJnNw-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">LIT VPN
نسل جدید فیلترشکن
🔥
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
🔥
فیلیمو
و
فیلم‌نت
و
نماوا
رایگان
‼️
سرویس نامحدود فقط ۱۷۹ تومن
‼️
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کدتخفیف ۲۰٪:
IRAN
🔥
خرید
از ربات:
@
litvpn_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/149453" target="_blank">📅 01:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmAVJMwl1bk7vNm_T3Oypgcskan1Ej00JYwhSxpuu6GE7OkJSfBzkxPskbv8uRARuvi-EdIx9cVa-c5B39gEhUB63eRT7u0OiwH-f5GDzao20k25hMezbNhSCqRqjcKt2I-4FbQDBeTNoavmB4o8Pf1jrnW2iigaN2zUI9upRcHlMWo0DP8K4Z1erYsom38dksyqchqpPzeBtTtHejqe6fPGq_h8oPwgHysyfrGBLw8K-4GNU16HAzuP2GzKoWzhx3eB-pIjktF-XC7w9s96tt7_-wV5Vam_WBxvQVrjiIBMMj2RVdQ6ImenjoCdhnJ3LXsbOOzRh6XNWnfjvLKd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل: عربستان سعودی تمام‌وقت مشغول التماس به اسرائیل برای کمک در برابر حوثی‌هاست.
🔴
اما در نهایت هیئت نمایندگی‌اش هنگام سخنرانی نتانیاهو تو سازمان ملل، جلسه رو ترک میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/149452" target="_blank">📅 01:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
هشدار حمله موشکی در جیزان عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/149451" target="_blank">📅 01:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b4430e11.mp4?token=ueKcViG5IaDwWQr-6sKqizY3z-peZKuqcWcBJihXveULl1TAv_iM7x_O7mQArB9tWbW82GMllyZh9qGE7cuHHvzifXK9xUUR-Xzs2tB0sGLdiAA6iz6kZuRZwkvqzCLn6qxnQ7nrglAP8mGaaqoWWqQBmAsHRSv5fOACitHGT_LOxPtS6FeKbCwt-Sft6rRanw667pC7fxqvdHhkaM9_iLMJCtTl9K4BsUFsnZDT8o4JGJGse2OgZLgXfVdNJ-EyjMdYF6e3-xkJUEF27GLYx1WjE_O7bzlpfJDPe1C0v0blPnjZfUzycV9PWLMwAq_WnjdEFnTrDF678v_TTVhP4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b4430e11.mp4?token=ueKcViG5IaDwWQr-6sKqizY3z-peZKuqcWcBJihXveULl1TAv_iM7x_O7mQArB9tWbW82GMllyZh9qGE7cuHHvzifXK9xUUR-Xzs2tB0sGLdiAA6iz6kZuRZwkvqzCLn6qxnQ7nrglAP8mGaaqoWWqQBmAsHRSv5fOACitHGT_LOxPtS6FeKbCwt-Sft6rRanw667pC7fxqvdHhkaM9_iLMJCtTl9K4BsUFsnZDT8o4JGJGse2OgZLgXfVdNJ-EyjMdYF6e3-xkJUEF27GLYx1WjE_O7bzlpfJDPe1C0v0blPnjZfUzycV9PWLMwAq_WnjdEFnTrDF678v_TTVhP4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی دوست دخترم میگه منو میگیری؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/149450" target="_blank">📅 01:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دقایقی قبل اسرائیل به جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/149449" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💢
توضیحات عراقچی درباره طرح هفت‌روزه بازگشایی تنگه هرمز درصورت پذیرش شروط ایران
💢
مهلت هفت‌روزه از زمانی آغاز می‌شود که ایالات متحده این برنامه را بپذیرد. اگر این اتفاق فردا رخ دهد، اجرای برنامه از همان زمان آغاز خواهد شد.
💢
در صورت انجام اقدامات لازم، معتقدیم…</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/149448" target="_blank">📅 01:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhVmR6ZA_oAmbES_rXGPNy27Z5nubt393Lw0MyfTHvoWzXULJse5DKvqNKkAT0HG8Vhvmn17b5xOCD_xMljMDWvTJXNrgDc2J5X1A9eNL5gMvHvtdWRXQdoH0DLTiM-FtobDBmW7bYeKbM6VnWM980wNFRfiXL8OEgG2DikH_7lUBoe_nGnadFH-ejR4hsHMbPevB__yIrt8a5kEHHXm4Az1fO4TK1krGhhQcC-ZV8HI-cmbf3n6aK-HxmO0Hmzo-PVyr4WlW3O489sQma3At4eHKSQbG2hz3EQIBaTSP3J4EAEn5-rA9jmPA-R1yfJTsT7wrH64TETbUGyINow_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی‌زاده
:
دستاورد سفر نیویورک رئیس‌جمهور و وزیر‌امورخارجه، افزایش احتمال اقدام نظامی علیه ایران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/149447" target="_blank">📅 01:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع امنیتی ایران: خبرسازی رسانه‌های غربی در رابطه با مذاکرات کذب است
🔴
ایران شروط ۷گانه خود را به طرف امریکایی ابلاغ کرد و توپ در زمین آمریکا است.
🔴
دلیل بسته ماندن تنگه هرمز عدم اجرای تعهدات از سوی آمریکایی ها است و همانطور که پیش از این مشخص شده است تنگه هرمز با توییت، خبرسازی رسانه‌های نزدیک به کاخ سفید و فشار هرگز باز نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/149446" target="_blank">📅 00:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=X55XzRkCUnwAEevg7IPb2btjAcWPZ6fcFHjpVCaSm01JfAQyfYjOHjbDxY7XkOFYJSDuUvfhVKSqLja8cW1KWMhNr-UXRY33z7RrygPoLat_1to_0FI5N4bCx0QQb8ZmiWB7izLbaRCE8_tRQgmMi4IXF4etOQ2haQgnwUG88xlrT0Y4abMaR5mJcf3GShoNhYsKeSAIAjP0dF8dxFoGycXIRRJSkR_ZiqJzNUIpjhTgPW55YfIZWYkcrh6eINNOnwWfFGVs798Op3y8C4ppXAuMf0lw0UVpHX7BkE3nbK4FNOHt70xomXjSfNzc9ev07vxyCXZ3p37K4hJ4F82Tmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=X55XzRkCUnwAEevg7IPb2btjAcWPZ6fcFHjpVCaSm01JfAQyfYjOHjbDxY7XkOFYJSDuUvfhVKSqLja8cW1KWMhNr-UXRY33z7RrygPoLat_1to_0FI5N4bCx0QQb8ZmiWB7izLbaRCE8_tRQgmMi4IXF4etOQ2haQgnwUG88xlrT0Y4abMaR5mJcf3GShoNhYsKeSAIAjP0dF8dxFoGycXIRRJSkR_ZiqJzNUIpjhTgPW55YfIZWYkcrh6eINNOnwWfFGVs798Op3y8C4ppXAuMf0lw0UVpHX7BkE3nbK4FNOHt70xomXjSfNzc9ev07vxyCXZ3p37K4hJ4F82Tmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توضیحات عراقچی درباره طرح هفت‌روزه بازگشایی تنگه هرمز درصورت پذیرش شروط ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/149445" target="_blank">📅 00:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE06p_nNLiFrCPJr3Cpcvr6nRsuP4Au8CYvrHHLwRKlrkVnK8R-2V8GUB2dyXmldWi8Rhav_JqfZsPGaDuyNJiO90uGR6kHQWqNNA6M3tXfdBFo_vjvhu1IpH56zBoNUbC16hCvd5OL7UZk74w5uBvxCKFrJ-DlMr0HQCHrXoxma0fF3wxuXRZupEuXXK4jSLsPRhZ1coUUS17tWxRcDoNZuRumqlRIwtkVgbmkUVHlDExVd3nCUSQ5DciiGOoKmwqbJWj9z9FcMKH8rkp1MPNFe0x5bjAYK4nv9ORPfm8Dx5aA9-HtDA_E8r9HRxJq9G6NA3yTWkYqKLeZLqAb74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توافق شد
⁉️
🔴
خوش چشم: جنگ قطعی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/149443" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149442">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پزشکیان: ایران بر بازگشت به تفاهم‌نامه اسلام‌آباد شدیدا تأکید دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/149442" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149441">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عراقچی : ایران یک طرح مشخص و 7 روزه را به ایالات متحده ارائه کرده است. در صورت فراهم شدن شرایط به دور از فشار و تهدید، تنگه هرمز ظرف ۷ روز می‌تواند بازگشایی شود. مهلت ۷ روزه به محض پذیرش طرح پیشنهادی ما از سوی ایالات متحده آغاز می‌شود که این پیام را از طریق قطر منتقل کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/149441" target="_blank">📅 00:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149440">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43bb16d0b.mp4?token=kMoCHqECj9DqW9s-ZyEKDdME2OcCOWNEhlmNw7g5kJwceBP0L61KG4bumbabGzHKJxF1bhnNmVaFPvRThYYjwhMDb4c8DpkGU9GaGW8kOnT0BGGhEiLrLVXAj-zorRjnqF6Qo_MTtj3VkNXBedl0ZqdZRQ-4us7_kn_-2YGuJoR-fC_5KoERMNMIuKno1TMrT1O_g9XE2QypTaOa1eCQqW5VnQ6ay1IMR1e7s7Rn1jDB1x5KFAq6xuFRKuCHQAvwOQkOgBgjmiuCE1O4E-wAS6T9DaQMNg2L9IFITffzZAs7vqk8B3gyxJNg_GszJomv-RhAJaoB2A9DghdTjfkQAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43bb16d0b.mp4?token=kMoCHqECj9DqW9s-ZyEKDdME2OcCOWNEhlmNw7g5kJwceBP0L61KG4bumbabGzHKJxF1bhnNmVaFPvRThYYjwhMDb4c8DpkGU9GaGW8kOnT0BGGhEiLrLVXAj-zorRjnqF6Qo_MTtj3VkNXBedl0ZqdZRQ-4us7_kn_-2YGuJoR-fC_5KoERMNMIuKno1TMrT1O_g9XE2QypTaOa1eCQqW5VnQ6ay1IMR1e7s7Rn1jDB1x5KFAq6xuFRKuCHQAvwOQkOgBgjmiuCE1O4E-wAS6T9DaQMNg2L9IFITffzZAs7vqk8B3gyxJNg_GszJomv-RhAJaoB2A9DghdTjfkQAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری تلویزیون: این جنگ تمام می‌شود آمریکا هم می‌رود ما می‌مانیم و این همسایگان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/149440" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149439">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9373fc68d3.mp4?token=LfCy1vDL4Y_rBihyGG8vUVsP1HITKR_QC9k4D9h8EH7Sl-38fNLllBn9i0pjWTdGjELPu7YDXev65I9rszF61xeEXjT8PdPDG3V64Dmqf2HTb9ZXiwl9rVHfwk_Y1bKlGHVLOvaJuLtBe8b_W-XDGwUSbUTdADILOo9IYt48aob0SxH_zqnWcPAQ-OIdsMoLOploduWI7r1VtXDF-hBhyelA6MFEUCZ87aifRe9fi_440QoXO0IW_XCDXzgeNNwHRJbBGPVS8Qqse3MHi2s14HxKyr3K33FaSi4xuSJDiOv5CGc3hry0fpj7SFPk44kyMVDyuotYuPXIPuvcn_WbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9373fc68d3.mp4?token=LfCy1vDL4Y_rBihyGG8vUVsP1HITKR_QC9k4D9h8EH7Sl-38fNLllBn9i0pjWTdGjELPu7YDXev65I9rszF61xeEXjT8PdPDG3V64Dmqf2HTb9ZXiwl9rVHfwk_Y1bKlGHVLOvaJuLtBe8b_W-XDGwUSbUTdADILOo9IYt48aob0SxH_zqnWcPAQ-OIdsMoLOploduWI7r1VtXDF-hBhyelA6MFEUCZ87aifRe9fi_440QoXO0IW_XCDXzgeNNwHRJbBGPVS8Qqse3MHi2s14HxKyr3K33FaSi4xuSJDiOv5CGc3hry0fpj7SFPk44kyMVDyuotYuPXIPuvcn_WbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجاب استایل‌ها از حموم رفتنشون هم فیلم میزارن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/149439" target="_blank">📅 00:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149438">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/149438" target="_blank">📅 23:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دبیرکل سازمان ملل: ایران به دنبال سلاح هسته‌ای نیست
🔴
آنتونیو گوترش در دیدار با پزشکیان: صدای شما و ایران، صدای صلح و میانه‌روی بوده است.
🔴
بر اساس ارزیابی ها، معتقدم ایران به دنبال دستیابی به سلاح هسته‌ای نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/149437" target="_blank">📅 23:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149435">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سخنگوی سپاه: تا تحقق هفت شرط ایران، دست از تنبیه آمریکا برنمی‌داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/149435" target="_blank">📅 23:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149434">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0beae5d2de.mp4?token=ESam5yOt9YxCmZnBtXN7hD7M5a-1tC6i7OyD1UIYhq3InS2WBFjiDQpmBEJhu-lhb5GE2lx0CSkYz03qUsXOhVqmIPrB883rFltyv0qbSIQNQECCc9cpbkyY16qSvOVTSlbeqS4NlY74IDPVWKC5X1uFpEi_fnGenCCfI8IFpW5RPBly9XPjl-bnAfz5KYDXgxt2AdrCAk8C7r-xnfgHNkUymDS3s8gG0g2nTM5lgrs_BSbJ1VC4FtVDxaoxaAeIMR8Lguz9TESnD9VBp2qzPAdg6PHSTER9YO6MZMPwugxWoB57PERqN32A--qLjYpKhbl071BylHr5ozT0RKAQow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0beae5d2de.mp4?token=ESam5yOt9YxCmZnBtXN7hD7M5a-1tC6i7OyD1UIYhq3InS2WBFjiDQpmBEJhu-lhb5GE2lx0CSkYz03qUsXOhVqmIPrB883rFltyv0qbSIQNQECCc9cpbkyY16qSvOVTSlbeqS4NlY74IDPVWKC5X1uFpEi_fnGenCCfI8IFpW5RPBly9XPjl-bnAfz5KYDXgxt2AdrCAk8C7r-xnfgHNkUymDS3s8gG0g2nTM5lgrs_BSbJ1VC4FtVDxaoxaAeIMR8Lguz9TESnD9VBp2qzPAdg6PHSTER9YO6MZMPwugxWoB57PERqN32A--qLjYpKhbl071BylHr5ozT0RKAQow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عراقچی و وزیر خارجۀ ترکیه در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/149434" target="_blank">📅 23:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149433">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWPFqdJ0PYufeArxJQm1SFy3yaHpHbyVyddf5YYaVfey2GGKalUAxtQMcQBraVucl89u72eiVE4hzCfkiJ5ZFBW-QfJ4aZhYD7Dayi0a39ZztTlY1u9EKOwIGjBKgQU_VqNUApfC0s4lf9z5Ak16Bo4kGTC9WKfGmhW6wnmibtiecdkqli1z7YaqGAJXcouqfT3R4T4eQsHW9_qH7e1sWxRQ843i8fzCPLM_BFTYwmN1rVd2c_JDVOnWeGNsyhxUhMzCebVz03D1EUVnhxrRWMskU2i76wDS7A-mEdlCMNy_DwtjzRLZz7YNm4L9jZ15sDYyn0bMifsTcXXP499q-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تجمع کنندگان شبانه از دولت درخواست کردند که حقوق نمایندگان رو قطع کنید و به حساب رزمندگان واریز کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/149433" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149432">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کریستیانو امانپور، مجری ارشد سی‌ان‌ان:
وزیر خارجه قطر، محمد بن عبدالرحمن آل‌ثانی، به من گفت:
🔴
«ما در چند هفته گذشته تلاش کرده‌ایم تا دیپلماسی میان ایران و آمریکا را دوباره به مسیر اصلی بازگردانیم.»
🔴
او افزود که مذاکرات غیرمستقیم این هفته «پیشرفت‌های مثبتی» داشته است
🔴
«ما واقعاً امیدواریم که دیپلماسی پیروز شود و بتوانیم راه‌حلی پیدا کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/149432" target="_blank">📅 23:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149431">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e658b1bc.mp4?token=DK9rVOY8sNd7PZshZsFzA8d7I74WxPPP4D124RHTX8z86rpYpQgenxqPQgeW8YSU6lxcd1ZrwkSVbRfTmm5woPd-aSJRsP6lkGmCMZGD8kWRx8RmyizgqO8P1dUmM1ksbkJniU-lcVpn52A0V3mkptmkT6rZCtE25vRBHyjy8n8-Roe9JSAIN-7aa4nq5UAAQH3naAUwvpAnIZ2dGkxQe5xhqlzqEdvDTTAOeXcT2IE2w6cH0-gj4erzSXm1f6tr2-cwsAqYLinR3lq-yFra9hoVGKGPXiZ6F5FX_7TOLU-ziEe8GtiX5DoryvytSkR-cW3zGbZEusos8n75GIbWfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e658b1bc.mp4?token=DK9rVOY8sNd7PZshZsFzA8d7I74WxPPP4D124RHTX8z86rpYpQgenxqPQgeW8YSU6lxcd1ZrwkSVbRfTmm5woPd-aSJRsP6lkGmCMZGD8kWRx8RmyizgqO8P1dUmM1ksbkJniU-lcVpn52A0V3mkptmkT6rZCtE25vRBHyjy8n8-Roe9JSAIN-7aa4nq5UAAQH3naAUwvpAnIZ2dGkxQe5xhqlzqEdvDTTAOeXcT2IE2w6cH0-gj4erzSXm1f6tr2-cwsAqYLinR3lq-yFra9hoVGKGPXiZ6F5FX_7TOLU-ziEe8GtiX5DoryvytSkR-cW3zGbZEusos8n75GIbWfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعارهای امروز پیر پاتال‌ها مقابل منزل حسن روحانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/149431" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149430">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ایرنا ، خبر خبرنگار الجزیره درباره اعزام کارشناسان فنی به نیویورک صحت ندارد
‏
🔴
ترکیب هیئت ایرانی تغییری نکرده ‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/149430" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149429">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizz Vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opGAuvB39RBwKG6C3Koh9Xyv5j2bzzm9yS04ghILaawVmUeTMyfAIH6xhzjm-D00TzedhCwEzrPtnKdAvohDWGEdTM80Z-LB-uUVXNeh8aOPWmkH2toJ_EN_Dz7kQT5bpSvXYOQAIZahJNDqCdHm406stGTyDOR_hBIK0uqLI1ze44XczACsgyjGjLF46IEdv8POv69-AqCIlvURjoQ3TqOVCd6O7OBuBn37ADEPyIB1uMuAAukUVFPeWvHqtO8taMAoCPVQtP23cBUh0SqRCmVpJu3NZyxdg4-ImxZ7sZCKU92wAWU00JPbQhT9OLu0KARQNx0OUcGqm2De69f2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
دارای IP ثابت
💥
سرعت بالا و اتصال پایدار
💥
اتصال پایدار حتی در جنگ
💬
تعرفه ها
🔸
سرویس نیمه عزیز
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود نیمه عزیز
▫️
تک کاربر — 180,000 تومان
▫️
دو کاربر — 230,000 تومان
🔸
سرویس عزیز
▫️
10 گیگ — 30,000 تومان
▫️
20 گیگ — 60,000 تومان
▫️
30 گیگ — 90,000 تومان
▫️
50 گیگ — 125,000 تومان
▫️
100 گیگ — 250,000 تومان
🔹
نامحدود عزیز
هفتگی:
▫️
تک کاربر — 129,000 تومان
▫️
دو کاربر — 149,000 تومان
▫️
سه کاربر — 169,000 تومان
ماهانه:
▫️
تک کاربر — 240,000 تومان
▫️
دو کاربر — 360,000 تومان
▫️
سه کاربر — 450,000 تومان
🔸
سرویس اختصاصی
▫️
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 275,000 تومان
▫️
100 گیگ — 500,000 تومان
▫️
200 گیگ — 800,000 تومان</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/149429" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149428">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=Fr7TJqj7EnTrsb0mLhU-PVFEe6MHdV4VdJMz2wi3kZuhgKLfB4TpeE1BdiMvabp9oOUd1_CYBj1DF7wM985h3WMF53f6gQx90KyKgh8Qzv0t8TjegEIR_7aRr2XIvsLIGsSl-KDg1ftoOQDlmCK3RKE5nJQM15xALENf1ueSAqORPtmO2R4fUPkyCAWWZRSbKb9AyodrUEFByqTb5M8dnJ55EW7tcStPubWnaefiEilWiJlBGXMWIhcXUqYFXlMSH4r3QbIYXaPGjisIRPoM7js36KoiNsArAC6hbwnquALve8J3jVyyuezPMiWx0u90XxQ2CvILYZXunXEr6Ugruw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=Fr7TJqj7EnTrsb0mLhU-PVFEe6MHdV4VdJMz2wi3kZuhgKLfB4TpeE1BdiMvabp9oOUd1_CYBj1DF7wM985h3WMF53f6gQx90KyKgh8Qzv0t8TjegEIR_7aRr2XIvsLIGsSl-KDg1ftoOQDlmCK3RKE5nJQM15xALENf1ueSAqORPtmO2R4fUPkyCAWWZRSbKb9AyodrUEFByqTb5M8dnJ55EW7tcStPubWnaefiEilWiJlBGXMWIhcXUqYFXlMSH4r3QbIYXaPGjisIRPoM7js36KoiNsArAC6hbwnquALve8J3jVyyuezPMiWx0u90XxQ2CvILYZXunXEr6Ugruw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مسابقات کبدی بانوان، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش
😂
😭
@AloSport</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/149428" target="_blank">📅 22:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149427">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فارس: ادعای آکسیوس و الجزیره دربارهٔ مذاکرات ایران و آمریکا دروغه و هیچ مذاکره ای نکردیم
✅
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/149427" target="_blank">📅 22:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نخست‌وزیر لبنان: با کشورهای خلیج فارس و اردن در برابر حملات جمهوری اسلامی اعلام همبستگی میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/149426" target="_blank">📅 22:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oghq_40uVJY6fabwUp_phOFWwlvWghaymw992lHzTdqqTYT7vB1WlGmOkTXRInPrfkxyeFUS8YtpaxrQRVsMqw_aTBJzRJhveqiqN85qWqoPSlDQhyT3gR1Ff5H8xbd92NQcF72VP4MspwZZ_RFiqCk6HwaqOKmF9qWjpItzMpmIh1xGkx9BVlZ7UoI2Er9PjsjAxW3ZV0Mh7YqInNxXuQ1vH1YibKqt_afXCyS6Tk6w3zS_F_k4r1urWraB-Gze4gM9VjMzPoCrNe_zFWG1UcI_Rub5IDQGKfPSv5XXF-KTfWrgIHKQDyPqqomsKtEo8fJk055T7pyg5WnDPScpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ایران بر ضرورت بازگشت به تفاهمنامه اسلام‌آباد تأکید دارد
🔴
از موضع مسئولانه جناب آقای شی جین‌پینگ، رئیس‌جمهور محترم جمهوری خلق چین، در حمایت از بازگشت به تفاهم‌نامه اسلام‌آباد و حل‌وفصل اختلافات از مسیر گفت‌وگو و مذاکره قدردانی می‌کنم.
🔴
ایران نیز بر ضرورت بازگشت به این تفاهم، اجرای تعهدات مورد توافق و فراهم‌کردن زمینه برای تداوم مذاکراتی جدی و نتیجه‌محور تأکید دارد.
🔴
اشتراک نظر تهران و پکن در ضرورت احترام به حاکمیت کشورها، کاهش تنش و صیانت از صلح و ثبات منطقه‌ای، مبنایی مهم برای همکاری‌های سازنده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/149425" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گزارش‌های تازه از وقوع انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/149424" target="_blank">📅 22:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyxLvMXEP_k-vwBJvlWbljHqh8ktQgw5aws32aKuqs_DywMmmEyGmaxnGlJHheHgw6pXfY-NEVVDo2cDC_XbTwx4BK758sg9tI-6W0gjRwCUMiTJG_JkVmvIKVCfnjBKssciUA_USukpsa9RNggpLRGwt6HkthKWPqSSjJJs_87ZT6Cbs4xdEEue_IxsoT2QLqEYfG9INyw4Dh0SlQYYWSL8LmwW9kFogCxL9G9VkOFX-KbgLzER3un48KRqL-hB7WfVvOXfa1Ir3DLxrUHMvJPy0NEZPd7esEczMxlFhyziurpZZVjcVPpHSHzVW560hgxPn31VHuxRNWejpsRVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: هیچ پیشرفتی در مذاکرات غیرمستقیم با ترامپ حاصل نشده است؛ منطقه به سمت تشدید تنش‌ها پیش می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/149423" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149422">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر خارجه عراق: با آمریکا درباره مسئله تحریم‌ها گفت‌وگو خواهیم کرد تا امکان ارائه خدمات به پروازهای ایران فراهم شود
🔴
طرف ایرانی را در جریان ممنوعیت پروازها قرار داده‌ایم
✅
@AloNewd</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/149422" target="_blank">📅 22:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149421">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSMyuhq_XItdqP0GjuAtGeCa_YaNhdK2FcbgJcNDN2C9T05NbxGswMhjPswdhHWfyTspVmjAZDF_R4FuB5Lx0eviaxw3Jw9x0bQu-__ol_kAL0ScKy4RNh6nHUlzng5vGb3QThBiTkxPOMoMDNy3eXd7nK4SgaWW5vz9C11n4N1Rhr74lEioyobnstq9gK0W9GURcflcO5Cf4WJeC1tSvs_63FjVZMPXyfuR9vJiBL1c3cthGkfCPOJRQSh8UYpRgRSmCGHRVzSv4NBTQw9_ej7x4iAtBotwxPvAF2wTNpSX17B_2tVj6MmkW9k-U9Xhv6vfXx6zXt298FjHMB1IvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت کلمبیا  را یک گروه تروریستی اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/149421" target="_blank">📅 22:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فارس: ادعای آکسیوس و الجزیره دربارهٔ مذاکرات ایران و آمریکا دروغه و هیچ مذاکره ای نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/149420" target="_blank">📅 22:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف:
به رهبری قاطع و بینش‌مند رئیس‌جمهور دونالد ترامپ، صدها میلیون نفر از جان‌ها در جنوب آسیا نجات یافتند.
🔴
مداخله به‌موقع او در یک نقطه عطف تعیین‌کننده رخ داد، زمانی که دو همسایه دارای سلاح هسته‌ای بر لبه یک جنگ تمام‌عیار ایستاده بودند.
🔴
و چه کسی می‌داند که اگر رئیس‌جمهور ترامپ در این لحظه حیاتی با شفافیت در اندیشه و عمل مداخله نمی‌کرد، چه میزان ویرانگری رخ می‌داد.
🔴
بنابراین باید اطمینان حاصل کنیم که جنوب آسیا هرگز دوباره به آن لبه پرتگاه نرسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/149419" target="_blank">📅 22:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان:
تعهد پایدار ما به صلح همچنین در توافق‌نامه دفاعی مشترک تاریخی مکه میان کشورهای برادر — عربستان سعودی، ترکیه و پاکستان — منعکس شده است.
🔴
این ائتلاف علیه هیچ کشوری نیست
🔴
این یک تعهد جمعی برای دفاع، ثبات و صلح در منطقه است و چیزی بیش از این نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/149418" target="_blank">📅 21:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان:
ما یک‌بار دیگر حمله‌های اخیر و ناپسند حوثی‌ها علیه پادشاهی عربستان سعودی را با قاطع‌ترین لحن محکوم می‌کنیم.
🔴
تلاش برای حمله با پهپاد به شهر مقدس مکه مکرمه، مسلمانان سراسر جهان را خشمگین کرده است.
🔴
هرگونه تهدید علیه امنیت و حرمت حرمین شریفین، خط قرمز ماست که هرگز نباید از آن عبور شود. هیچ مسلمان نمی‌تواند حتی فکر ارتکاب چنین جرمی را در سر بپروراند.
🔴
پاکستان با مردم برادر عربستان سعودی، همان‌طور که در طول تاریخ همیشه بوده‌ایم، در همبستگی کامل ایستاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/149417" target="_blank">📅 21:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف:
پاکستان انتخاب کرد که با سرعت عمل کند. از طریق تلاش‌های هماهنگ، پاکستان با موفقیت واشنگتن و تهران را تحت یک سقف در اسلام‌آباد گرد آورد
🔴
از مذاکرات اسلام‌آباد تا تفاهم‌نامه اسلام‌آباد، گام‌های تاریخی بسیاری برای پایان دادن به این تعارض جدی برداشته شد.
🔴
در اینجا، من از فیلدمارشال عاصم منیر، رئیس نیروهای دفاعی پاکستان و رئیس ستاد ارتش، که تلاش‌های بی‌وقفه او به ایجاد فضای دیپلماسی در شرایط استثنایی دشوار و چالش‌برانگیز کمک کرد، عمیقاً قدردانی می‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/149416" target="_blank">📅 21:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه نیوز‌نیشن گفت که در طول ۴۸ ساعت گذشته، تقریباً ۴۰ میلیون بشکه نفت از تنگه هرمز عبور کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/149415" target="_blank">📅 21:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad11830c5f.mp4?token=Z0ApOViXWTCM_3S198f8L8bsuIKZgVEpxH5JrG3RtBlVKudrrOfC5osrhbHZ4ZVZPH3AizmCEtDwnJEEoXD3RKdZFAro3xq9qDqBt3jIIE2kL-1N8bwfBJK7e8VNIM4thkPaiirXgv8lvgRopzvYgSQ7NS0_UwtkvlxoIPLSrfbiTd_kZkyQZLNYS5FljTDjBLqBdqSWn6nptVNmoSBQbmWMfjkHGPDNKXulE6HIHGNV76D9uKxHGBbH4vAaXKysvhO-2F0mY7lkEggHSs05_IrC5XNog1TTtbVCLRC0IImg3e6WUfrnn8bnopjS_nBjcNF3E4jBzFWPeOpYRBQvhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad11830c5f.mp4?token=Z0ApOViXWTCM_3S198f8L8bsuIKZgVEpxH5JrG3RtBlVKudrrOfC5osrhbHZ4ZVZPH3AizmCEtDwnJEEoXD3RKdZFAro3xq9qDqBt3jIIE2kL-1N8bwfBJK7e8VNIM4thkPaiirXgv8lvgRopzvYgSQ7NS0_UwtkvlxoIPLSrfbiTd_kZkyQZLNYS5FljTDjBLqBdqSWn6nptVNmoSBQbmWMfjkHGPDNKXulE6HIHGNV76D9uKxHGBbH4vAaXKysvhO-2F0mY7lkEggHSs05_IrC5XNog1TTtbVCLRC0IImg3e6WUfrnn8bnopjS_nBjcNF3E4jBzFWPeOpYRBQvhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: تنگه هرمز و تنگه باب‌المندب، شریان‌های اقتصاد جهانی هستند و باید باز بمانند، حامل رونق و پیشرفت باشند، نه خطرات جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/149414" target="_blank">📅 21:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع بلندپایه: بازگشت به تفاهم‌نامه میان آمریکا و ایران امکان‌پذیر است
🔴
پیام‌هایی میان دو طرف درباره بازگشایی تنگه هرمز در مقابل کاهش محاصره و تحریم‌ها منتقل کرده‌ایم.
🔴
تماس‌ها برای تأمین ضمانت‌ها و هماهنگی و تنظیم گام‌های میان آمریکا و ایران در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/149413" target="_blank">📅 21:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نخست‌وزیر و وزیر امور خارجه قطر در گفت‌وگو با CNN: ما دیروز مذاکرات غیرمستقیمی بین تهران و واشنگتن داشتیم و پیشرفت‌هایی حاصل شد.
🔴
ما تمایلی را در هر دو طرف آمریکایی و ایرانی برای پیشرفت در مذاکرات احساس کردیم.
🔴
ما تمام تلاش خود را برای بازگرداندن روند دیپلماتیک به مسیر اصلی انجام داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/149412" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149411">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBx9FrA75TZKrk3UshYHALK8JINLhp0ZOnB8FW81lgjThqqznK_bXPtUhNXYJB0A9606u2tXm0aPGvfG54qr8wo4ctPEK0xSK7KJ8i70VT3Tft4IiPfBGgzTIChaRoqvFQjNXiFWhRhFMwWxm6pexxwFbTeAVVsO6-bf_QucWZ6bpe9HL3UrWFPcKQ0RUwfphnSXLQnlCxS-e9ajgpfBHzK5RkafttDPaP0R_Q7ZEiZf87tYlbb7UW6gBQcnBilLnqKpE-P_Sur0JgotnJLjyKd0V6AlM6W2b91rajFoAjEO6EOEmGAcOuQkvYvOLsfZ6o02Ria1iMV-SShXWwpcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار پزشکیان و دبیرکل سازمان ملل در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/149411" target="_blank">📅 21:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149410">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBpSQqWqmx0nW4CcQr9NQSeANmCaBqLe4lo52Zm9gzTAyhUZ9n2C3n5Rcg6jgA_ggYQ2EggKBIntqdpb1WVPKqXGa4RGAkmp9vYZ4cXyCyCY3W_O-vZS2iPFhxIvnlAkLzNMO8uaPAddwAx0kp5__FaPUKI53Km1ZlyAxyZpXON6AhokFUEen6VKrpBiJwetE4cvkFd8T0DqHw-lcerpI3YBRHKl6TdQlG55zD0TkF7GDe5jZczJD5cZQ5Zpyo7pE-UTu54m0VHSQHjA2hhzr9Ud6diBCLiLUFaPZN7byUgtlCXKKRj0bRdFe3P6pHP2-Tgw2YQ9uDPLDBSETD3gcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان بریتانیا وارد جنگ علیه یمن شده‌اند؛ به‌طوری‌که برای نخستین بار از زمان آغاز جنگ عربستان و یمن، یکی از این هواپیماها بر فراز خاک عربستان سعودی و در نزدیکی مرز یمن دیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/149410" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149409">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T16hM5k_o6_QyaQtYv-CdLQjqnX3-wOKF7XgnWjW8zwQb1lYYNER9lA_c9TcS5iRvABEww832CpyJ1JIhGP-H6B3jYgXP5Sk4kWBUEgsTbk_zCPYT4DMGMtquEBE_S7MTwmp7qJ2XNsOmSi07G_1lKTqxskK27Y-JWpjV8eTiY5u9Og8LyXm5c9iRPjdoQxyiomFM5oGVF3CG6ztXXCg6r06JT3UNyoXvo8ylmXjN3mOAUFNtWYXsr-JVJcaKVmbHJ2nMnia4ulTMCp8BZINEHM8C7QCdkD6tRe6gSrlJ3XzdR51emLkCfUL_VMKj46Ez-LO4mBTydMk_mhIsbF2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از رزمایش موتوری امروز که طبق معمول سردار بلاگر بازهم تو تصویره
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149409" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149408">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucBhmUYg-AVspPFrtSLeP6uw2f0Gv9NTt7ZY2EQdkfA9x4Wxq1XYf3BfaIDIr0wXGbZjtVSOg-8wKmKysDLmef8iSksiLyASR4MECR-MtyyHvxPEHuZMMGesY5eEgYkC0Q6AJwli-wWIV4B5MpGNgmTl3hr86rfcJPJxwZThVKrlZBvhOzm7emhKZ5tey5da7VrcCirTcrGcirOyTclza4NS4n3sXKs41JGhMRQRNMd-8H3c4IDBFICWZturM3nHuZRms-F-5waQNPyP3ejuZOdqUBikz2tL0AJPN6jsarSbPzq_7m-Q1s3wgIfwoVgvUVMUlX3Q7YFf6mSrybzPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: رئیس‌جمهور شی و خانم پنگ همین حالا از واشینگتن دی‌سی خارج شده و در حال حرکت به سمت چین هستند. این نشست نشانی از دوستی، قدرت و موفقیت برای هر دو کشور چین و ایالات متحده آمریکا بود.
🔴
ما در ماه نوامبر در چین و سپس در ماه دسامبر در میامی، فلوریدا، در نشست G20 دوباره با یکدیگر دیدار خواهیم کرد. کارهای زیادی انجام شده و در آینده نیز انجام خواهد شد. من با اشتیاق منتظر نشست بعدی خود با آن‌ها هستم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/149408" target="_blank">📅 21:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149407">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
واشنگتن پست به نقل از مقامات آمریکایی: اسناد محرمانه‌ای که به کنگره ارائه شده، نشان می‌دهد که عربستان سعودی احتمال توسعه یک برنامه تسلیحات هسته‌ای را منتفی نمی‌داند
🔴
این موضوع نگرانی برخی از نمایندگان آمریکایی را در مورد موافقت ترامپ با کمک به آن‌ها در ایجاد یک برنامه هسته‌ای غیرنظامی افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/149407" target="_blank">📅 21:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149406">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر خارجه عراق: ما با هماهنگی آمریکا از طریق تنگه هرمز نفت خود را صادر می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149406" target="_blank">📅 21:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149405">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اکسیوس به نقل از یک منبع مطلع:
قطر و ایران منتظر دریافت پاسخ ترامپ به پیشنهاد ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149405" target="_blank">📅 21:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149404">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bccf790968.mp4?token=Qvg507KCSq_AHGyEYbVSrOzbx6My8_yodCMNFF-TPYCdqFqJxpa0csDWVrB25HF1VcvWUTzDJiWt7C3S2AICQkS2R283gXaAQbtd5trHcz-lE-lWCuJVyDF7TNlxw6kpagLlPkOydP1YlbKf96GmB1Cn14M9l1Gg4Sj96GlmwTOlgU5epSFmCFgrqRtrc4zUMnRx7HpBxXR2Wj6rQmStZjyh97kpGc3OGZpnHnD6f7jbRTG6F-nnc0egJ4tHVMHlEd501tQgnziRSs74ut3ykjY1r4ozp6NZhcJZtj3mji4inh_ZFiHKOja5-rnxoDc1KDlEQ_-N9WFP0qmXA5vRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bccf790968.mp4?token=Qvg507KCSq_AHGyEYbVSrOzbx6My8_yodCMNFF-TPYCdqFqJxpa0csDWVrB25HF1VcvWUTzDJiWt7C3S2AICQkS2R283gXaAQbtd5trHcz-lE-lWCuJVyDF7TNlxw6kpagLlPkOydP1YlbKf96GmB1Cn14M9l1Gg4Sj96GlmwTOlgU5epSFmCFgrqRtrc4zUMnRx7HpBxXR2Wj6rQmStZjyh97kpGc3OGZpnHnD6f7jbRTG6F-nnc0egJ4tHVMHlEd501tQgnziRSs74ut3ykjY1r4ozp6NZhcJZtj3mji4inh_ZFiHKOja5-rnxoDc1KDlEQ_-N9WFP0qmXA5vRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پایان سفر شی به آمریکا
🔴
ترامپ و شی با یکدیگر خداحافظی کردند، چرا که شی بازدید سه روزه خود از ایالات متحده را به پایان رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149404" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149402">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نیویورک تایمز: نتانیاهو از عملیات هفت اکتبر خبر داشت
‏
🔴
نیویورک تایمز گزارش داد که محمد بن زاید (MBZ)، رئیس‌امارات، پیش از ۷ اکتبر به نتانیاهو هشدار داده بود که حماس در حال آماده‌سازی یک حمله بزرگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/149402" target="_blank">📅 20:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149401">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqnnb6SBxpby5et0Qc5nIYlotkZrpMCrtZ3Z3PPlJo5U_6DUMiL5uRzBML23BhWptXWMlNzUjZytkzKs6H22rz1VPROCi0rJu99_2qoAl-YCAgq7LFxMyCkFeFH7ZhyylIzGR4jKjSl5Rff_i8ruZusOwjKntx2vQQ3rCqF0t1uRs-T8-C3Cvxg9Q2z-vJ4QEri65v5JdMVjO1RcprrRbv4wEYIWWbpFZZBK_sASfMDcsiIkGgvtwxq7PnxRx2V2cUGF90cpfVvjjGaQCp0vOE8rMXvAKHQoLnPpT3nwplJ02RKIdI_dt-BFIcklSVb_a-6SnZt5_aWUrAT2NADz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه، گفت که از رابطه شی جین‌پینگ، رئیس‌جمهور چین، با ترامپ حسادت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/149401" target="_blank">📅 20:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149400">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سنتکام: تا کنون مسیر ۱۲۲ کشتی تجاری به سمت ایران را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/149400" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149399">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مقام ارشد ایرانی به رویترز: حتی در صورت پذیرش پیشنهاد تهران درباره هرمز، امتیاز هسته‌ای نمی‌دهیم
🔴
یک مقام ارشد ایرانی به رویترز گفت: «حتی اگر آمریکا پیشنهاد تهران برای بازگشایی تنگه هرمز را بپذیرد، ایران هیچ امتیازی در موضوع هسته‌ای نخواهد داد.»
🔴
این مقام افزود: «تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/149399" target="_blank">📅 20:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149398">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره:
پس از نخستین دیدار میان استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، کارشناسان فنی نیز به مذاکرات در نیویورک پیوسته‌اند.
🔴
اگرچه دولت آمریکا در ابتدا برای هیئت ایرانی روادید صادر نکرده بود، اما این روادیدها به‌سرعت صادر شد و به هیئت ایرانی اجازه داد به مذاکرات ملحق شود
🔴
طرح پیشنهادی ایران برای بازگشایی تنگه هرمز طی هفت روز، در صورت کنار گذاشتن محاصره از سوی آمریکا، در حال بررسی است.
🔴
این طرح نسخه‌ای تسریع‌شده از روند ۶۰ روزه‌ای خواهد بود که پیش‌تر درباره آن گفت‌وگو شده بود و شامل اقدامات فوری برای بازگرداندن دو کشور به مذاکرات مستقیم درباره برنامه هسته‌ای ایران خواهد شد.
🔴
مهم‌ترین مطالبات ایران که در حال حاضر در مذاکرات مطرح است، شامل رفع تحریم‌ها، لغو محدودیت‌های صادرات نفت و دسترسی به منابع مالی بلوکه‌شده ایران است.
🔴
دو طرف همچنین همچنان درباره ترتیبات مربوط به تنگه هرمز گفت‌وگو می‌کنند؛ از جمله این موضوع که آیا ایران و عمان می‌توانند تحت چارچوبی مورد توافق که کشورهای منطقه و آمریکا نیز در آن مشارکت داشته باشند، به نوعی از مدیریت مشترک تنگه بازگردند یا خیر. همچنین ترتیبات مربوط به عبور و مرور کشتی‌های آمریکایی از تنگه نیز در دست بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/149398" target="_blank">📅 20:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149397">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3acdf0c4.mp4?token=vXHg-VA6OWSvAkzv81-6BG9R4TLLkEJpyOOynmarrG18lPmudPsdYq8L3OTMQF_uX8Jo0lzSpUrzD8yjil-hcgNOOws1n0-inPlZvDranAjG0ubI5Z7mNsxWLHrLYltcCTdzguzVp_DdiaeR_TySxvEklPZYzb0tJhEoKXFySXnz87hH8dRk_6kwV6oanLiCIK1NBUtyqvQ52kc3TJyZkcpvvkAY0NFz36aKnJQ-D7xkpb1-GBJTGI8ApKbVwoqUriqfJbwiYm0Zf9UP0EffTjdgIzdkpUywY5zOK6y92ME89fE4ytL8_7p7KVWCy7ZS1HDtZoHMvcxT8Fl0s7pkCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3acdf0c4.mp4?token=vXHg-VA6OWSvAkzv81-6BG9R4TLLkEJpyOOynmarrG18lPmudPsdYq8L3OTMQF_uX8Jo0lzSpUrzD8yjil-hcgNOOws1n0-inPlZvDranAjG0ubI5Z7mNsxWLHrLYltcCTdzguzVp_DdiaeR_TySxvEklPZYzb0tJhEoKXFySXnz87hH8dRk_6kwV6oanLiCIK1NBUtyqvQ52kc3TJyZkcpvvkAY0NFz36aKnJQ-D7xkpb1-GBJTGI8ApKbVwoqUriqfJbwiYm0Zf9UP0EffTjdgIzdkpUywY5zOK6y92ME89fE4ytL8_7p7KVWCy7ZS1HDtZoHMvcxT8Fl0s7pkCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی عجیب قائم پناه معاون پزشکیان از برش دادن کیک ۹۶امین سالگرد تاسیس سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/149397" target="_blank">📅 20:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZ37ABgVsisp1BniNGZebDaon9ABNqGdE5vqitWx3i3Om2JSC_D7gzDAZPQXmQ3g38wmrYZ8FfWWvLBneszEN0-GPo4LdmxpdodV0fX46Y23aHVAb6311rsZ5RKzRU3zDtuTNnScoUoX1v0Jv119xZHMQGyDdgT2y4FJQK-GFTUVToNmv2qrHd6HdbTD4atmOiDeAZCEaeIRBVGPtR4iNRvSF772axkE2L6J7u_H14oWpF35_BLiOGDimrWo9z5BQdlrCG50HFCyetGNjOiEmshAhi24tsnf8VMDj9L0LdrKNoYZW0K7fekkkUuhVBoEg5FsJMATRolKEIvtzKB2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOfD56UIpbo2-wpz80WEPHKrF4nJEFx9mr77NmY2HSKZwaUhzFGpcLHRU2rX5wPzkn-AtAtZlLYhLrLIaHBiC1MdCkkAFHW7O1LEJrIeAKG91jvcBJ3Hz331KlLRf_1IgIGk2-42FyZdUaTp9KggXlXSrHgTxEUv49xJmzWSs1yhMm0BkzWyxTB10nSKsGCltQU7WldV-arQDLv3nKvDrAb01QFllnwvUpzsdIqWuA3CkcooQ8ucxIj0xUaF3Vrkzqdv8T3AlAqf4ldo8xy45L3aZD_fq5C05iZOwjMpR7WHFJ_JxF2d8vniSGxelRgqP_l0xfy3tiuzt1g12CxPMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار فرماندهان ستاد‌های ارتش عربستان، پاکستان و ترکیه در ریاض جهت مقابله با حوثی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/149395" target="_blank">📅 20:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43bbf6157d.mp4?token=RAppoAwCgWYjdffTkgkoYH7lCz1piby-noxHrUnzoJh-TjlprwWXwkXRnNDRp3pxHMjG7u7OqalB5c_i6PnDFa1X9qs-Ie1ukUVL1JJu0ameNRw_jP8TCAVjVsghik79sWkYGv6tmV-9lo8rcRYI4tESsSMu6YWwilzV_f447ckujilUu8St1qJVAyoaLFzdIFIlHe6LiU7aCGDb78o_M0PDVWoH6315317U7G5nalrERbBse2Bilfe-sJzaQCf6tj8UcsM95OyJvW86CJvRSd_XVp9iLLZP25BMJ-MTp6pFhgBXnNMTYZXvnacPDAaJ08pIMuQgHX60QyL1Zl8ONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43bbf6157d.mp4?token=RAppoAwCgWYjdffTkgkoYH7lCz1piby-noxHrUnzoJh-TjlprwWXwkXRnNDRp3pxHMjG7u7OqalB5c_i6PnDFa1X9qs-Ie1ukUVL1JJu0ameNRw_jP8TCAVjVsghik79sWkYGv6tmV-9lo8rcRYI4tESsSMu6YWwilzV_f447ckujilUu8St1qJVAyoaLFzdIFIlHe6LiU7aCGDb78o_M0PDVWoH6315317U7G5nalrERbBse2Bilfe-sJzaQCf6tj8UcsM95OyJvW86CJvRSd_XVp9iLLZP25BMJ-MTp6pFhgBXnNMTYZXvnacPDAaJ08pIMuQgHX60QyL1Zl8ONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار خطاب به ترامپ: آیا درباره جنگ با ایران با رئیس‌جمهور شی گفت‌وگو کردید؟
🔴
ترامپ: بله، صحبت کردیم. فکر می‌کنم قرار است اوضاع خیلی خوب پیش برود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149394" target="_blank">📅 19:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149393">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f22063209.mp4?token=MADq7QiR-bevNMO-GGSCREFcLn7Wga-mzyy1uuQjmo0I1NygUHX2Iy1G_8B8fxE3p3j_xWJNoo6rj4dJx7v0B2UFP-GQ7pCv1ircXwI2Nypq-Fl0VIZdzK4yFbbe28rpMGvQSBFGZ-0TTY9AGnP45nwUZIRsBC0DeLTyHe-vxzY1T7dcgVi2j2x0PK-Jb5vlRNTYztQcbL_OMsstY2HheH2SUAoe4hoA4a3ufBix4Fql4zof5ZFvz7Veoevr98D755zUU7m6FcHiKo-xeeYfpe3oWl0waz3G5E1WHFx1asROlyN8faOEAZUAjJSB_P2zwG5KtxmrRQl_gRlnyVogLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f22063209.mp4?token=MADq7QiR-bevNMO-GGSCREFcLn7Wga-mzyy1uuQjmo0I1NygUHX2Iy1G_8B8fxE3p3j_xWJNoo6rj4dJx7v0B2UFP-GQ7pCv1ircXwI2Nypq-Fl0VIZdzK4yFbbe28rpMGvQSBFGZ-0TTY9AGnP45nwUZIRsBC0DeLTyHe-vxzY1T7dcgVi2j2x0PK-Jb5vlRNTYztQcbL_OMsstY2HheH2SUAoe4hoA4a3ufBix4Fql4zof5ZFvz7Veoevr98D755zUU7m6FcHiKo-xeeYfpe3oWl0waz3G5E1WHFx1asROlyN8faOEAZUAjJSB_P2zwG5KtxmrRQl_gRlnyVogLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازم عجیب اما واقعی
‼️
🔴
عده‌ای بیکار و علاف هم جلوی منزل حسن روحانی تجمع کردن و خواستار محاکمه وی شدن
🔴
این جماعت معلوم نیست از کجا کسب درآمد دارن که هر روز ول میچرخن به یکی گیر میدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/149393" target="_blank">📅 19:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149392">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f93e70ab2e.mp4?token=hEuNQbD_Wg165CiY1rA6xxCn4AXrnsEQJhKGUoqQ3yoBS25t_vsuhLlQjCOOZbEwYzMBmtARm2QYYAspIKQPpkPGsC-jgedFGPCgAceFnQecvUBLQwkCrEUZpZ9hSz4cBHb-3Tb9i9Ucyh0yozzXgn5VCTh1GR_2ulVXwCgWOfcc3H2Cd4YjU9BUAq8qaVF2EquN2Sx1ei60-aYrEQTRSpkU4y1J0CgGredYljQogRx6kR9z_EUxumf0Wl9cB2pZmTGteqOSgQwT1yuhZGK2ScU5yqaFGCGCEcABfWh3QS9AiyO8XkxwfrhXg_ZIfRgB5pK1q2FLD_89VCyR2wbZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f93e70ab2e.mp4?token=hEuNQbD_Wg165CiY1rA6xxCn4AXrnsEQJhKGUoqQ3yoBS25t_vsuhLlQjCOOZbEwYzMBmtARm2QYYAspIKQPpkPGsC-jgedFGPCgAceFnQecvUBLQwkCrEUZpZ9hSz4cBHb-3Tb9i9Ucyh0yozzXgn5VCTh1GR_2ulVXwCgWOfcc3H2Cd4YjU9BUAq8qaVF2EquN2Sx1ei60-aYrEQTRSpkU4y1J0CgGredYljQogRx6kR9z_EUxumf0Wl9cB2pZmTGteqOSgQwT1yuhZGK2ScU5yqaFGCGCEcABfWh3QS9AiyO8XkxwfrhXg_ZIfRgB5pK1q2FLD_89VCyR2wbZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
امروز بسیجی‌ها به یک جوان که پرچم آمریکا رو پیراهنش بود وحشیانه حمله کردن
#بی_شناسنامه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/149392" target="_blank">📅 19:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149391">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2c9f2c38.mp4?token=e8_T6Mhyl4cO_JfYuEwL3s5KBcgrQt1DpVQR0huf7trpoqowlOCvXhEjaW3ulOPLsDjTSvHRFjfd98mmwUKLdFyquWmQk1v6SFAQjrm4p6G9WuNZFwDpxGhrZMuokDLwvicsI4nB6oXKVafj1ksyaTPu_15AZMBwrO2ISVvDdDG5B-TsKSYCecVlr_ZVhmbCxPfSzvcPz7csK1C6fCiQ8CASdIisUTiJWE8AK8u5Ygi-OAepONVnJbwuC8Ps28sSIiMk3L_f6xhceCJVbH7mABomdTZVbZ5VA9HD0FDA57lPpj-3UUuyCy0DK5tpyfHmRadrPSwgNXPnG0kxIf_c-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2c9f2c38.mp4?token=e8_T6Mhyl4cO_JfYuEwL3s5KBcgrQt1DpVQR0huf7trpoqowlOCvXhEjaW3ulOPLsDjTSvHRFjfd98mmwUKLdFyquWmQk1v6SFAQjrm4p6G9WuNZFwDpxGhrZMuokDLwvicsI4nB6oXKVafj1ksyaTPu_15AZMBwrO2ISVvDdDG5B-TsKSYCecVlr_ZVhmbCxPfSzvcPz7csK1C6fCiQ8CASdIisUTiJWE8AK8u5Ygi-OAepONVnJbwuC8Ps28sSIiMk3L_f6xhceCJVbH7mABomdTZVbZ5VA9HD0FDA57lPpj-3UUuyCy0DK5tpyfHmRadrPSwgNXPnG0kxIf_c-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
گسیل ترابری های نظامی ایالات متحده به خاورمیانه جهت امضای توافق
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/149391" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149390">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
جررررررررر
🤣
سفیر اسرائیل رفته استارلینک رو تحویل نماینده ج.ا بده نماینده ج.ا هم عین دخترا قهر کرده و اونور رو نگاه میکنه
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149390" target="_blank">📅 19:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149389">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
👈
رهبر مذهبی عربستان سعودی در بیانیه ای بی سابقه از تمام مردم عربستان خواست برای جنگ با حوثی های یمن آماده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/149389" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL0DO9pizGHh04H0tzAMxb2ugYk_w8-yyrCXbg9L8YtpvuMfIKprTrQb_hrfh1xnmGRUTXC85kipZtJ27mv3iCOzOfCfAYgj3fRnP_NPifpiSxASdUlsv2s7O1qcozaBk7bQg2QqQ4zLyVuoYIxZBYZ4LKVE4D-HXGdpvrrdHp4YwfB82xRiZ9AROYT4MOQTHdWf-uP9_RCLfnek5niT4qhukinbYL4hmpvMTgyBoIR37SP5sQMjdKHCh29eVPnsZmy7Brll8oe3Aec2IPBrVeJpRNAIqz15I5FwreBn3vM1npmtkIzthTTusXxGDLDc29qGoTKQOcKGPI8pLEWYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
دیروز تو تهران 96امین سالگرد تاسیس پادساهی سعودی جشن گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/149388" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149387">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فایننشال تایمز: حوثی‌ها به اروپا تعهد دادند کشتی‌های اروپایی را هدف قرار ندهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/149387" target="_blank">📅 19:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149386">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0d77058e.mp4?token=geu3AX2OMj16XBXP4S_52ZCWSZT1x99UmDiGJOUuO94Pu37r-ZSLDWFC4HqRHRRM3zhAYVvUQAp48-h27IcAjLaP8lcWXd6r14zJWedGKNFnXJ5D4boQpiSPAM7441qyshl8IKJhG3S_rTSktFEiuNUpMarjPW_EqNZOm06DMLJxE30ssk1vCkpu0TnALyLrQrOF3J8SdVeVhLcExJPRsKZr4hmbruBYKCyEuaPR8Q2YDuJAR8sEosefDaUg2G-89kJOvo_o1Jm2TMS5lRghyMBguRH0fgJHhz7DaJSom-qW38o1essPpdZbZ3ff8-nZQf3y-1WJGzrA67f0b2a9gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0d77058e.mp4?token=geu3AX2OMj16XBXP4S_52ZCWSZT1x99UmDiGJOUuO94Pu37r-ZSLDWFC4HqRHRRM3zhAYVvUQAp48-h27IcAjLaP8lcWXd6r14zJWedGKNFnXJ5D4boQpiSPAM7441qyshl8IKJhG3S_rTSktFEiuNUpMarjPW_EqNZOm06DMLJxE30ssk1vCkpu0TnALyLrQrOF3J8SdVeVhLcExJPRsKZr4hmbruBYKCyEuaPR8Q2YDuJAR8sEosefDaUg2G-89kJOvo_o1Jm2TMS5lRghyMBguRH0fgJHhz7DaJSom-qW38o1essPpdZbZ3ff8-nZQf3y-1WJGzrA67f0b2a9gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در دیدار با شی جین‌پینگ: این سفر برای آمریکا و چین بسیار ثمربخش بوده است
🔴
دونالد ترامپ در جریان استقبال از شی جین‌پینگ، رئیس‌جمهور چین، در کاخ سفید گفت: «آمریکا از این سفر بسیار خرسند است و مطمئنم چین نیز بسیار خوشحال است.»
🔴
او افزود: «اتفاقات بزرگی برای هر دو کشور در پیش است؛ این دیدار بسیار ثمربخش بوده است.»
🔴
ترامپ هنگام استقبال از شی جین‌پینگ به پرسش‌های خبرنگاران پاسخ نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/149386" target="_blank">📅 19:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149385">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/149385" target="_blank">📅 18:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149384">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نفت خام برنت ۱۰۶ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/149384" target="_blank">📅 18:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee60910e82.mp4?token=GzSNRy2tcz8tjcDNz8Vn1S3v3avo3SVp6ze5zLH324WZ3xVAmF_OfIXG-dYICu0dnApOR2zwP1lRhOLCR7cU0k1Qj3lWuCK3OeNa3DA5UjldmvJfo1GckK7YNUjCDASAaFqnUlU2V8G4kkYzJjz6rWEFvFOtFtQ8-b8oWy3CW2fy5zCrCz7lHVhFbzotmH3P4WDoeyDfXEIlnxvjMEhTciDkYc7HD3uHVwqlRIgirU72WkL1mTc2TqmeZC5QiZtxs3HqIc4reQS3SylC1T4muNteR2B8IAcp3ATbKCdBM5TO9qgjNbVKaL2g3m1JlKwIOXRyE4pf6wAaOy6V0yHJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee60910e82.mp4?token=GzSNRy2tcz8tjcDNz8Vn1S3v3avo3SVp6ze5zLH324WZ3xVAmF_OfIXG-dYICu0dnApOR2zwP1lRhOLCR7cU0k1Qj3lWuCK3OeNa3DA5UjldmvJfo1GckK7YNUjCDASAaFqnUlU2V8G4kkYzJjz6rWEFvFOtFtQ8-b8oWy3CW2fy5zCrCz7lHVhFbzotmH3P4WDoeyDfXEIlnxvjMEhTciDkYc7HD3uHVwqlRIgirU72WkL1mTc2TqmeZC5QiZtxs3HqIc4reQS3SylC1T4muNteR2B8IAcp3ATbKCdBM5TO9qgjNbVKaL2g3m1JlKwIOXRyE4pf6wAaOy6V0yHJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ و شی در حال چای خوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/149383" target="_blank">📅 18:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149382">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کارشناس نظامی صداوسیما: در روز های اخیر پرواز هواپیماهای جاسوسی و شناسایی آمریکایی اطراف ایران بسیار افزایش پیدا کرده است که نشان دهنده یک حمله قریب‌الوقوع احتمالی به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/149382" target="_blank">📅 18:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiVlBiVwI7d8XI7HCEF4o84DuTrugfZP2krbpHn3T2mPYgUkOgN98yHRkvhvF_t8py0mpEHup8YWrOtOBRAcjQgWXgh8rwLrdQc7Lr03-QACgrNcerB-Nts7vQjmPzo5Kc4WceuXF1mpFvmQvuUy89swOv81zsxmchzzGwf0G8OtbeKMGuaLGaOWotabeNJq1Fa5siBQfAcpQ5LthO1z4yMuwCh00rOcTKBRHzSxxF_C73IsTtYaRnZAPQ2B6NIXu0t1RNa6kKHXDY8S0Ul8VxONhm9oyNzAMZX1u0E9cJWdD2b4YtcniaCnWWRXy1LyTRs3VYweeb-qMQPN4oFZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
عراقچی و پزشکیان باید استیضاح بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/149381" target="_blank">📅 18:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149380">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXefx_HFTDDJDgWKuUOAGUX088qj_L8BkxJoiR87V1XTn6epCbxqTaiMBtX9LbH5GgZAk6Ufbm0-z_99X6EDeRkjL7unuuJN5MdAPv5hw2vBDLDrVYd8VvCVFQIp87wLIYFxKuLc00m_7mxhKbSTXBg6KrlyC7xJilrKTp7wJGqE1-WOvr-Y60eSEBGYrbK5bXqN4GdI9rsemBfqkmQ8fgGh3_j6opyXJETg2byMUjlO01LpoDQI7kRGYLmJJr_lyXlK-E8mYlR2tAp9CtYaVT8_npbkidrfE17xFxHlAzU5q8qOTHlWNGzFWOAhqYJBtbEd4vwMmA1HdgF7ItAfsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:
«محاصره هوایی ایران» (لغو شدن پروازهای ایران به کشورهای همسایه، منطقه و دیگر نقاط دنیا)، پیوستِ «محاصره دریایی» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/149380" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ و همسرش، ملانیا، از رئیس جمهور چین، شی جینپینگ، و همسرش، پنگ لی‌یوان، در کاخ سفید استقبال کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/149379" target="_blank">📅 18:21 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
