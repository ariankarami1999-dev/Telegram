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
<img src="https://cdn4.telesco.pe/file/a2To2rU4OGHu5F6psTQpCCJB3kR6F_d95r6UGIGyyOUj7tZooyO9L6A_THi6SsNirkOQKny-dssVH85FGyZDJusGL3rMlMNdvWT6t6VvU6fXalziRvILgwWlEKscEIdrDk3-nPtakxIkwduXXtfuvr_KuNfGMe7CmbrLZlksOWx1lysnddaMalrf5_6J8NFpYzxWtb1Mlig0wqtj8GKXYTQaM7xPbP0G_4BMn7e25J9aE0QIk2R_S938MJJPmIPehrytzU5aXHXufXYtOlAanVjkOFyQkcknNZ5qByTTHaFShSWkOpFeI-8czzsKjJ-j3arn3vctNLEz5eEBYskVxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 14:08:44</div>
<hr>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BMKZk7d4TR23meNbWRX1PGkNu2Mn9teJhV2hIIhgRKy1SYX3rYHnGJAe8gGLd8D-PtWThWt7VYClK57lxResftgq0XPtbYAL56vh_8i4GGHrZ7vk8jjA2rUykCAgxcHGOepVtRIBP1_AiCyL2QWAh5RUq-gz76N9Ndey5V3ubO5EskhcL07BziIP2yR5LeDRGNyBaCzLtY-WCf5mKaFPfxjjjm6MuKqHWf2uTCUwTD16N2PKWvztZIOSq7HKJWcB3ap0DVc5AfCgq7ymGNbcbJLKYgFlYuTVmrLWccrNTcyYjrVRnu5bzy8Q9reFPl7XebH7z-qOncChdI-sImZ6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=BMKZk7d4TR23meNbWRX1PGkNu2Mn9teJhV2hIIhgRKy1SYX3rYHnGJAe8gGLd8D-PtWThWt7VYClK57lxResftgq0XPtbYAL56vh_8i4GGHrZ7vk8jjA2rUykCAgxcHGOepVtRIBP1_AiCyL2QWAh5RUq-gz76N9Ndey5V3ubO5EskhcL07BziIP2yR5LeDRGNyBaCzLtY-WCf5mKaFPfxjjjm6MuKqHWf2uTCUwTD16N2PKWvztZIOSq7HKJWcB3ap0DVc5AfCgq7ymGNbcbJLKYgFlYuTVmrLWccrNTcyYjrVRnu5bzy8Q9reFPl7XebH7z-qOncChdI-sImZ6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdWJgw0PLVMOxf50UHNevQWUOdCA1CdoPX_0z9iz-k6WtSxMwBr-aofRD7f9ll804XH6DaZJ1ELPMlMpuhOQnPKs8JyErM6SWhuaCnSujCteOBMVuvkNkNqsxjOXPXySGGOdgs5Wed63LZG86_J18AVtM37nK8R9JL2eln5jndKb_Z2F0Mk6GRCcGBIBmjQI3MHl6PmdvkwKaEc1wqoPtN2NrIi7CnCROH_ihPKlNdTdlLFiPa-EfnTyD2FmHRdh3vsEarEd2154QrYQ6vziE-pVQ7MiObpIamq4JpHZvvkfnLFujZqg-RUS6KcumrSZuy2CxkqlN2y7LDvTImj9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=KeLG4nrvOcrqw-ecUqQOZjSOFgxI5lJUni0cj1I4CP_UmpVt6El2b4Vn5tlOU31g3IOrk0-Z1D97UPEpNklg-SHmFK6ffKyH6yeZikVerP727AvhcXT3H_Rzrhjt3aDOJrWQrXOUU_uTABlVCDUTfmU0WZ16YoDv5GwjB403ZpdvA4qBKYr0CHXbb4AOkeiDt7W10XBJtYLrlq6yKpnplbDPed3A25hY_4wtEZLLCvATOsZTMHJ1mw9I4bBu3Al9cDGz8CbHpWsyJ1-L6Lt_S9mxwk8NRLezuwltOpeIopju7RKYAx7qGxJmxvKsH1BLnygm4M_Z-f7KMSIpnJehi4EroRuWm019d0RI5KVYJ8zkTnauORUvWhE3jsZt6U3dag6wVozCG1SkHLbOwVvktRSWMZQ1CtEcwA2qQfVOuenpO0VNN3iOT2NIiWwA2k88zywPdaOew_zzPpxfx4xWQt3ZeQ35Y2TlX03zqu2uh3bRU86xKa5mRW7o2i8VuUamuXIucXM5u252JvoVGB9WupXSWZsTf1Vhtj9NfVwygQ0lw-O1GSp9L5Za6be25TK00b9gdIblzB_LWSysxnagzjyI0e2_WNsWxWyIInOl03JXnCbJOpZvh1H1xREiUia1rkNRscZmbSLcQRiYbVl_B9RdGspN1nLKsC8VCBLIlu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=KeLG4nrvOcrqw-ecUqQOZjSOFgxI5lJUni0cj1I4CP_UmpVt6El2b4Vn5tlOU31g3IOrk0-Z1D97UPEpNklg-SHmFK6ffKyH6yeZikVerP727AvhcXT3H_Rzrhjt3aDOJrWQrXOUU_uTABlVCDUTfmU0WZ16YoDv5GwjB403ZpdvA4qBKYr0CHXbb4AOkeiDt7W10XBJtYLrlq6yKpnplbDPed3A25hY_4wtEZLLCvATOsZTMHJ1mw9I4bBu3Al9cDGz8CbHpWsyJ1-L6Lt_S9mxwk8NRLezuwltOpeIopju7RKYAx7qGxJmxvKsH1BLnygm4M_Z-f7KMSIpnJehi4EroRuWm019d0RI5KVYJ8zkTnauORUvWhE3jsZt6U3dag6wVozCG1SkHLbOwVvktRSWMZQ1CtEcwA2qQfVOuenpO0VNN3iOT2NIiWwA2k88zywPdaOew_zzPpxfx4xWQt3ZeQ35Y2TlX03zqu2uh3bRU86xKa5mRW7o2i8VuUamuXIucXM5u252JvoVGB9WupXSWZsTf1Vhtj9NfVwygQ0lw-O1GSp9L5Za6be25TK00b9gdIblzB_LWSysxnagzjyI0e2_WNsWxWyIInOl03JXnCbJOpZvh1H1xREiUia1rkNRscZmbSLcQRiYbVl_B9RdGspN1nLKsC8VCBLIlu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=gQaoAYWVaDThIrFT6v0SMdZMNkx4TA3jclUzJzT9SgLoVyYvzuBAs6Gqhy-_N1k277GGoVX_IbMcnKXIi2CDlrcALulHj5YDfNCoc5xEiJmSd-oCVl67n9jjSyZmYi0GvVBmGcUzDtZOUCBay9OlrZL-K82Y7uepqgS64LBzJHQ9T2STfxdAwJyXZOvWXqob52USmf2qIcnLulhQS5Nx2tPylu74o9IGWjepVmiuJHO9Dm0DqB6uePJagxSEdy8Tpqe3kmyGHlbVpYfzZvIFNgyCM44qLm0sepNM26eUD5tGSKyO_EX3uoUX02PkJRi-qDv_EmDegjDMFWulTVmJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=GXFlQQbFMPL99OuKitmuYM7_gpOlEx2qvvIZ7PIOj8YGh4HIcm7Qf9a69gzckHFe2P6Rybhsfz85WWpn_UYp4cVW7Rl9b56DHYLZDncL0Faokm3P68zdXk2GDl8lju5GUM8ZYPRXODiqbeJojQDpsoS49r5oL07Gu3sQ_kciZ96BimKoCZnS-ciA_qz1mF_86f_hO-Jcorra3AJ8-nsM2eRkUGgFB2pjk_giCybNORsGxvGwwGxWkoiG1hpTKxYs__RiD87pTTElgON6_LsxkvLS1nohQtEmgs4QwKdwG5uS9_n6RIKT5PPvOgpRaX8uecZdxrTHU7CpjWftT5smiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0U_EV03l6hN6fSBEloHRSMdXvt-AQDCrioxAxL4daN53gLeS-G7IFuIYwMoYav9-xYxxZ8R0sedGTqwv0UFQF70JII-VgEczb2WO78y2luNQF-gXaJlpsJKT-EgQzhHLg64ATmrbTb6ZjTAB0f0nqgiJWFliHaxon2Q1WooQ0fuXxqZawswNYwktM-TNXowcq8t4w8WABfe7V76bob581Kp0Ptut1kVh4zljFIQS_YZJngZ4mg1vEJGmiU3FKnnzM5LesiOR6Y3EIhmBll4IwvzqweOgWXWBDEyXHXJJYDCN2wJGCZFh6OAJV9Vgy1rhuXzEf9JkeG3xHRRYhMk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=rd13S5pp3Kce2cy9fpX1B_3zEhMs-C1kBcIzJxS1W10WbsOI4Zl5yMm6F_yeys6DbAZEWPTSeHC5tQZj208lKrKKqpufGoLsElX9B44vrWhqGk_2emnFfS1GGMgXrNpIKkOP4CA0Do1etuFX_ITx412w9AeVaNzJEkEKCuEYOibKHDvYJggvv18-gu78UagO_75uaTEVCABDih44ovev7qxpfBNLdXktrjvNFLfLKv5AAi3ZSoiruio6xY1VtxnvTGdSFbxwqs0B1ZW1V8dqhlvHo8CE5uxYGm48SfztDYa5QdB8XbXUIKunTFMFOmh4OxNKB-QZrEohR_8lqFrS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYCu8XrF-1WqfnO07o-fr9OaKRkYH1w8FqQMzfE9ZZDlMdXe3zyxME8VlPcIdomEPmFYv6E6wgnaYe7qNwZ1AyBqGhZuogz80itTU6NtXBkS0y3gAjYL9gwZ55u7zFKCD9SOlrEVg1hYxeeZexZNr89hUAV9Ifaeqa2MaFh0Q6F_h8Cp-J3H_r2I_g6ZwkFRUt1kWI6L1SKqFJAv_IbJMHdEt9vwTzRYkyv6bY55NmmA_mcih6bOVpyK58g9LTH4SEY_vNrImKx_28PZV2h7RRdQsvVwPblwpLzBdEeugkG3pRXNeHeyQ1oHW1hZBvzV8IVIABR6U_YGDiHuKssflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=tfnr8iEAbRWO9GfT1g7y8Rs-07Suzc8Vs2HzBlf-976hUKdkcpDQfiBxlwTlt3a-NiNBfNIz6ATLAM5jWm8JaesTXoScKuEtD6TVIPhW_GjZcNfcbJ6Xn-xPhoZ99dms1cEyF7WTyYPOw925smhbVg5bw40eqNbG28u_0vw65O2JX-9g-apoCKn4KBGLmnIgOFDWqMqFwXQjMK3fB58zm4ydRkrPYmzwp-07_7jCdNBTmaaRfhHtMS6gMjqTm3Y1jrRCIcWs_mfyo1y6gmAScqlQ6En5qXyVHcvHipc06Lyo09lqc8R9VA6UyqOd0XzbFY5wmkeN9uG_EeYjcIqryQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=tfnr8iEAbRWO9GfT1g7y8Rs-07Suzc8Vs2HzBlf-976hUKdkcpDQfiBxlwTlt3a-NiNBfNIz6ATLAM5jWm8JaesTXoScKuEtD6TVIPhW_GjZcNfcbJ6Xn-xPhoZ99dms1cEyF7WTyYPOw925smhbVg5bw40eqNbG28u_0vw65O2JX-9g-apoCKn4KBGLmnIgOFDWqMqFwXQjMK3fB58zm4ydRkrPYmzwp-07_7jCdNBTmaaRfhHtMS6gMjqTm3Y1jrRCIcWs_mfyo1y6gmAScqlQ6En5qXyVHcvHipc06Lyo09lqc8R9VA6UyqOd0XzbFY5wmkeN9uG_EeYjcIqryQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocUvZInmXSgxOFR_PkkilUcR6lyDAdV74ZT8NWKgyv1oIgBPLnO_rDXZkuKDAxp4IFbybmmZj22RdK5ILR-kfn97u2bAGkbDZ1RcjdrjgVsMu4mb1eC9Y8_sctIdIhKeDUJdBiEV26gvb0eGq0E5VM1a8jE05TFg-zm4bhFH8F0VtD_fvtQVEZa0A6Fwx0KH8QkXtpbheu3-bZtskLP8O4SJnqgJfZH27xXhOFIDd9YtOCpNHfuEw8cE9J9c5qnFjpAF8S_Iu-HB7VRQoZPQ_0fV_Hx6PpXSTEhGZTnFMcWWRNWNizB18L5VMJ86wZqPPRfOlenrWrUI3w0mESdJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=NQ6Qiy1Bhdewspuscq4b1vDu1heNLjed5DCLGlv3RmIBk2BVoIizo_g-g39BtMKOzzGXSwMk37BdN-5JrtXxfC8XjUtp0pnDvC5ZQXxJLUoZKu7j6wlr3cUld672B_QpUZ_RAx9hc4sKK3e51j_el4RUPuA0oOD7U0rMyge6NhMzcXoKdAhmnKNuOs1jMboMtomQ-rPE09opj6dXBgbmpyeqC3bKxplCvqa_HLf2g_PniT3UUmw4sxWN_flEZhtZCT3XijMDwn9ASn1ke6aKp-VHmpLeWqs0CaWgr_laWxi5DIhEZ7PUdyzosuFCVE9ptP3tRlZSa0H51oMTWaMahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=NQ6Qiy1Bhdewspuscq4b1vDu1heNLjed5DCLGlv3RmIBk2BVoIizo_g-g39BtMKOzzGXSwMk37BdN-5JrtXxfC8XjUtp0pnDvC5ZQXxJLUoZKu7j6wlr3cUld672B_QpUZ_RAx9hc4sKK3e51j_el4RUPuA0oOD7U0rMyge6NhMzcXoKdAhmnKNuOs1jMboMtomQ-rPE09opj6dXBgbmpyeqC3bKxplCvqa_HLf2g_PniT3UUmw4sxWN_flEZhtZCT3XijMDwn9ASn1ke6aKp-VHmpLeWqs0CaWgr_laWxi5DIhEZ7PUdyzosuFCVE9ptP3tRlZSa0H51oMTWaMahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=lXXlwF25D4vSFSxBkC4LuszImi6PbkkRp_acZbSUSbROnMXQ8NmzZVcc5kc_l2f8GszCBG6LDLj3AU06zbae1o3xxCniTQ59Wnz-s4mRZVg8xyBtwAVhIxzKt0LZ7NcgFfbv2c56J_NEkqHT9akcucR_9P8AZG2hde3i4rNONn2Bce9mKXUIMsALQmjwmCofff0mo9nwORImES4xvHGKf5pCDbkmi7A-PvEWZp3A8z2QJEky2ttPEnl-BrGCXX5TEClwJkWQUmaRCbVDS0Ii8WqQiv-1bMDvwdazh34etFigWMg_gLBknuweeCHdmHVTp90COwFD7g8y8MiUQXttgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=lXXlwF25D4vSFSxBkC4LuszImi6PbkkRp_acZbSUSbROnMXQ8NmzZVcc5kc_l2f8GszCBG6LDLj3AU06zbae1o3xxCniTQ59Wnz-s4mRZVg8xyBtwAVhIxzKt0LZ7NcgFfbv2c56J_NEkqHT9akcucR_9P8AZG2hde3i4rNONn2Bce9mKXUIMsALQmjwmCofff0mo9nwORImES4xvHGKf5pCDbkmi7A-PvEWZp3A8z2QJEky2ttPEnl-BrGCXX5TEClwJkWQUmaRCbVDS0Ii8WqQiv-1bMDvwdazh34etFigWMg_gLBknuweeCHdmHVTp90COwFD7g8y8MiUQXttgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiBKy1Q0TRHANsufzTEmKh4ZQa3pEDqfIFZyvbxEq0R3NyTBzs-d-Q5WzXvQGrQTItR_DqfAim_bZcYdmjf02eiwzgii3o9t46E3RCPOIxos5XCCFoL6akBZEdhjhD4eJNB5dNVl3wWPNhLTcl9TCFb-Aa9XOKffh2mAWFm9ax3U-9HsQMFH4bCLz_KOaSN0vW5WeXcMdPGG2xgbJEEZJMux8aGViewbLb8Lh6KDZR1gg10qlteBFTzGYociTA1kRK7KX3qE_EEQrv-G8HzR4-_UU1eVD0ezojSm6v0cJCRjshAi3QfsTyeqUIDJ79zq9q1i3ceL5xlKbjkhCSC7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa32sKePsq7gLL1aPGBKfKZlBJwNDD49Lfy6FrAkS4GmIa0DLCJJDsONyccLgSofPPcuN-4-iHoe30KL7p4yEilF8gH6JlZ4zDk3XG2UkkfLla-2mKyEUaqaII2SifzakgYZOP3pLPOJ-NLSKtF904N94Ijj_WcYbLsVL_uVauklOdGDvgnQAcwTO2sffLDgDcTgobYo3q1G85WdUlGDJF9KKB6wHn3HqJXUo7TI4mcP_VIygRGbNYDpuMJKtML4QikEEhtbZvw_pQFyN7wVgStZRWqf4O_P3cD6lsA27SFjfd95EUWAm4mYKBQ_ZxiZRvJYSlRQfBy_yB2jediJEJnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=odTYSqMApeFPY7Ws3LYwEdDtCr4PAKpc1WF1v41-WwRQj1NXA8Mawe5r73_NVLAA-ZigfSxih1AzPsgWKZ3wV-Jer8RxRTaYiWCzoqCEE-CPfYExgiAu8607-nRwlUUMl0QjSs-Iie3V4kXOr4ZTGE6ZOJJQBXEvbN5ptDZy1o5-Nv3caKCdEPT1OZFkr4wWjao8NjA9M4raaS-SrrCqyvdHvwjMu4ulWkfw18RHTMraOIjLHqbjQLEGURy8gF2JFXjEbw6GBubCwF6_s_Mx5qZw9cmuE9ApKhe1tImAqvx_DCPwA7NXWDaQ-3lKfUo75XCR3igaax7aAZVP820Oa32sKePsq7gLL1aPGBKfKZlBJwNDD49Lfy6FrAkS4GmIa0DLCJJDsONyccLgSofPPcuN-4-iHoe30KL7p4yEilF8gH6JlZ4zDk3XG2UkkfLla-2mKyEUaqaII2SifzakgYZOP3pLPOJ-NLSKtF904N94Ijj_WcYbLsVL_uVauklOdGDvgnQAcwTO2sffLDgDcTgobYo3q1G85WdUlGDJF9KKB6wHn3HqJXUo7TI4mcP_VIygRGbNYDpuMJKtML4QikEEhtbZvw_pQFyN7wVgStZRWqf4O_P3cD6lsA27SFjfd95EUWAm4mYKBQ_ZxiZRvJYSlRQfBy_yB2jediJEJnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=OSC2d6TMY9bVnsYVoHTWa-X9an6-EHfvx6CiEO1e2VQPnteGyXm3lE0Fq_n49CvFbpSG5Zq_7Wds7iZ34aW1A50U7Kpvc2PzNcxPuVQ-VJ8J0juVQLj1yogKjgdayA_Nrs6Z_CWBfKGrQLaT9gFiWAq--m4zyIb1H96GfYvHRbF2eTzqvUj7D0t4V-MuTQpu-5b9lS626yEM1oDkq9sGYZJlrGh6JjlWQ7UCAQaENw4GK_FHK5zh3XuBJ5XiFTrcLWRB-I06rSz5sSl0rf6hL2s_WwR2a5EVxsubYaDV9JOEvlehFqxHORlDfU0IQStqgKHMAEsmxm0iImocFCS3Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=OSC2d6TMY9bVnsYVoHTWa-X9an6-EHfvx6CiEO1e2VQPnteGyXm3lE0Fq_n49CvFbpSG5Zq_7Wds7iZ34aW1A50U7Kpvc2PzNcxPuVQ-VJ8J0juVQLj1yogKjgdayA_Nrs6Z_CWBfKGrQLaT9gFiWAq--m4zyIb1H96GfYvHRbF2eTzqvUj7D0t4V-MuTQpu-5b9lS626yEM1oDkq9sGYZJlrGh6JjlWQ7UCAQaENw4GK_FHK5zh3XuBJ5XiFTrcLWRB-I06rSz5sSl0rf6hL2s_WwR2a5EVxsubYaDV9JOEvlehFqxHORlDfU0IQStqgKHMAEsmxm0iImocFCS3Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=ZamPiwXbfK9qVdHX1Pi0W_pbdpoQ_YIKQTJP5WdYKNjBwq5td4BRdpN3KIqtd1ziqA00_V2MaceLpa1mAlo7tUZR_1Pa07kcCFCndZa2TEdOOgh0YwOAo9MCSrsNb_ypEu_NuY1jrtafQyC9NFsNamUSuQZhgjivHvlekNyRYxiBNkHke2vavb8XSukjnvqkINtRFOiYpgtx7QYePYvkuHSp2YMcVqe4LC6--ld2zI0aN_um7sYlSyE-Kx0NZ0rIwP39SGL_gkOt2ROumlNgQvnw_1jkF5tfu2n1q9uQtPflMedT3HH5L4f316pTScMBISjdEHphOlBk0UrxbPTwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=ZamPiwXbfK9qVdHX1Pi0W_pbdpoQ_YIKQTJP5WdYKNjBwq5td4BRdpN3KIqtd1ziqA00_V2MaceLpa1mAlo7tUZR_1Pa07kcCFCndZa2TEdOOgh0YwOAo9MCSrsNb_ypEu_NuY1jrtafQyC9NFsNamUSuQZhgjivHvlekNyRYxiBNkHke2vavb8XSukjnvqkINtRFOiYpgtx7QYePYvkuHSp2YMcVqe4LC6--ld2zI0aN_um7sYlSyE-Kx0NZ0rIwP39SGL_gkOt2ROumlNgQvnw_1jkF5tfu2n1q9uQtPflMedT3HH5L4f316pTScMBISjdEHphOlBk0UrxbPTwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZoqXA0AsNtcLHYROAmpbsFTJ5M2ZCgqCah9YlaZr0Na8bUah0IugagHlU2X1kA721iscpz-VQ9ZCQ5QT3B-QBXfBQSp74hASe8lt060nb1CXdpNWye0C6GF-cwQSXt99GcW8NCjKS0zziAFJ5nya73Nwxm9oaTwLqKOK-fNRKEk76TwQnWsRR7cAyVYJV_ScAf1vHfCrHl1EYV3vZELqNlFKuxcYGAiULfABHtn8qkSRs3ZFA6Dg8uhQhg_VeCqHrKcyHKi09EwyFsxwuua-hpwDIeE7OVnTWFBk14cfVhBV3vsikOnJfLi5ZZCbp88us-RW1y5R0TTaxnyNS06uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=Vmaxi51IxZXwfGWqjrEfRF6m36RiYJVpdMi398VqdLfQDqm0y0t-B2en7clDUyejlKisdclp9R93WGcL-viRXvpdpb3sHoAj6OGzh0FeVtUWoedqDnqB6o-zKPOZUZP2qj4c9CL0FGIVse82PhD1eOo2-pqQrlYynoyKKUPVSl4Z4sJO8s3ybKgJirfqjgaSQdPcmxmnOOnOY3He_H3_9Q0DPMi_qMjeZlU40GIkhQLpEpyLHOFbARf7BbVf9b1ZS6r8fckZt9WGZSZwL39rw9kdYc993baDh8L-i4UzvFq2IP-RLCaLNHUgodgQ-3JelEYFKPx5F8MPduCGIMasMmmgNJAarMuWZNuxyPkRwByIcmnSIS1cbNVTMvWNVLrinuROuAoS-UVAIej__gnY01dq2c9D69IF5oUPLjnR6lG8iGoc9JKyQy00OHT56-zVo0Oh3QFbaxukVLvtCBwd3RqBDdLlSmpzgwiwcFpMLedNycnUlwQdynHj6Kx3tFqLLhK4GoM1EHjPqNPweY1LRIPeH8q7KPfJFFir08jsLkvTcAIt2sib6qYtGK7shUGzDvWsSytz5vOXxJqHumi8Aqcx-5FWtKCjqOHJXm6LVjCC3vV_PzCpvpTAGAnrq3HzH6nyngVyac8065D0-tszANVUV6wExj0s6Bem418hJsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=Vmaxi51IxZXwfGWqjrEfRF6m36RiYJVpdMi398VqdLfQDqm0y0t-B2en7clDUyejlKisdclp9R93WGcL-viRXvpdpb3sHoAj6OGzh0FeVtUWoedqDnqB6o-zKPOZUZP2qj4c9CL0FGIVse82PhD1eOo2-pqQrlYynoyKKUPVSl4Z4sJO8s3ybKgJirfqjgaSQdPcmxmnOOnOY3He_H3_9Q0DPMi_qMjeZlU40GIkhQLpEpyLHOFbARf7BbVf9b1ZS6r8fckZt9WGZSZwL39rw9kdYc993baDh8L-i4UzvFq2IP-RLCaLNHUgodgQ-3JelEYFKPx5F8MPduCGIMasMmmgNJAarMuWZNuxyPkRwByIcmnSIS1cbNVTMvWNVLrinuROuAoS-UVAIej__gnY01dq2c9D69IF5oUPLjnR6lG8iGoc9JKyQy00OHT56-zVo0Oh3QFbaxukVLvtCBwd3RqBDdLlSmpzgwiwcFpMLedNycnUlwQdynHj6Kx3tFqLLhK4GoM1EHjPqNPweY1LRIPeH8q7KPfJFFir08jsLkvTcAIt2sib6qYtGK7shUGzDvWsSytz5vOXxJqHumi8Aqcx-5FWtKCjqOHJXm6LVjCC3vV_PzCpvpTAGAnrq3HzH6nyngVyac8065D0-tszANVUV6wExj0s6Bem418hJsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3q3XE8AlrompvY_hYgaNv2B70r5ue6QI_1BPb9ADSGWtyA0tnBex5BsfUNLzgVi_ztE4Mr6UomiuAiys0_Bzw2DqdMO1k1OU7a6NC3hvG6pgXCc3BecRL6uSEji8LfcSmrkv44K8-hpqjXmPpIJARplnlNFA_MpAMoeohpiYvsWvbavrF3yHZHj8CEj61Hh-LzjEbdJIrotlOcb-39NhaeydWPagAUi046SJr6o03Q7IgTN0rtMIkUVfoWwb2bX96soVi7VzOAveXsEEt_hFLGaXl_XWYP27l8LWV1SFuqRk1XwPKmZnPKNnDoPcwCJ0Bzl34Zk2GKMvrmUd_uKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=IvX6LVgLWvqFAwdaSjOSrE2Y7csFP2IqW_9RP5HRlZ-D-VEnC2TaMuFhrfYaBFgoocqIA188KWNI7QBdqdPAvAw9Dj3c6SxXXV74cx5ASwiN8wUTCIZvd-jN5fAqY-ihuB5X3SpL9KbZ2fBELOI-X5GhkM6ywevDcTyWFxKweu2W_76V9--ztO0lCF9qpuCJYbZAwh5RAYyDYpl2Vs2-oTlAG6brEpVSDZn7XmZiE9BUDCzYEKnrq_b-6L-TLUxUNwRR-rvU8Sw0ZKhfW5naBjoED9UtB9swVsNRCtZYnbzCx421VOjdXrv4uD1qoE8NFRTX6lgHGdye3y3IoqDFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=IvX6LVgLWvqFAwdaSjOSrE2Y7csFP2IqW_9RP5HRlZ-D-VEnC2TaMuFhrfYaBFgoocqIA188KWNI7QBdqdPAvAw9Dj3c6SxXXV74cx5ASwiN8wUTCIZvd-jN5fAqY-ihuB5X3SpL9KbZ2fBELOI-X5GhkM6ywevDcTyWFxKweu2W_76V9--ztO0lCF9qpuCJYbZAwh5RAYyDYpl2Vs2-oTlAG6brEpVSDZn7XmZiE9BUDCzYEKnrq_b-6L-TLUxUNwRR-rvU8Sw0ZKhfW5naBjoED9UtB9swVsNRCtZYnbzCx421VOjdXrv4uD1qoE8NFRTX6lgHGdye3y3IoqDFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzCZBLa-TVB85hIhfPcVIybMnTkHbWHJGOT5J1e8Bf_LlIdIqD9IEYOEVo-1rv2aInab7wNYHBZpqUCao0yJQk19LsNPNcPvojfSALnU8LPzA5D2o3xJkAa4b19Y7kAz1c8Z3iQeQGGSjoDNNv5Vjtm6HOGne3tZveAjOLZjUCwXySogr75Z37lbAHGJHgwzJAulsXDqJoLAnOWWK0T7lU72r4_L5ip-Lour8Ri_wc-YdrRe_UMwzTTN4sMbljIWQ_9ypF6R92ocGRx7W0RfEMrrmxT27NNKmFky8CeCCf50dBTZ_-Jl3-EWPMgruqTMpIF3AAELwmWExU3hQJIfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXUkRFveijuExYDT-F44dpCj1c7iEALqZUHTxX_TB-kf8Wies39wNuYaosZS765di6SlOEoFboYntKdnF_bSi4bgopC8f-h9x4v5PhZe6HeFdAVxeJ5ZKJA1eCOF45pt_YpiDAIZRxPBnvEaTKCM2MFgh09HrELcJ4pgaTq-lHdNw56-U5JZsLb0c52Cj8400sGXsMLTjjMyg43iGwBbnZg29CmWymbYcJElQPgnqwe1VY0Ix11MXAh9CgkKLxcIBD20OTjkE6F6h_giBJW8cep2aRxO_3DvMF214NwIChcmNnHynhcrFnjL8oakMopoxMGWDc-bxbs7d1mZBFfQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_JFc2e0ZOlcHy9cDcyD6GMGRUvkwvEm1924_Ru3GKnV4Ks-nY1b3AEArVzBL0Cpsq5QB4NJrnd_1fTDVvMkClUwvuNYRx3agdAtti2aubDER6jdV2t3rV9x38GaJZV7RAChiY9QHZy1IBORPjqEMUKNnHhsmLmGGbCDU3n9N0okuU4wJaqCFnx3FbZMBx2qJzbe_nQsTc6EhP1RShUzFxM0IcNVpZrBqlDuUiw-st-KlIAgdGiJd2Re1NhSDKpg7nCPxbHTCRf1gbv21dsdQqK9W-iVFK1Q_8ErdXx1_ciGeiSNYcBk0xAfH7v5hcEM6anfESzcvtAjp6_aHQdX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=Q6ps0hw698st4rsgEzhhX54MMNIe21GyjSLDGzkFkw4PKBiLsC1kbNpJKaoTXtxYQIga_e7d29D2ybPBLABzsHrFF2tRHDhGHX6TDRYohjmFIxfBJKOV5CRkpLx3OOItsE_1DXYGxu0qmXhT0ZlileGGxn2HxfB35d0MwVwt-cJhRCFZ35WuXYW4PEl7bAxSLc-QEe5VgSMUY-2tA3JH3x9-tBbjidkCTwg1kW1BFOl2AZ77dmfpsc3YILy4-goZXXKLBJg2xB3ecmxpLJBY9BjyeNEtpSTQvzEziviQNeBcmAKe1qa2Zq2y4PXZyhmJH9I2YVb8YU3FzvPKiCMKgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=Q6ps0hw698st4rsgEzhhX54MMNIe21GyjSLDGzkFkw4PKBiLsC1kbNpJKaoTXtxYQIga_e7d29D2ybPBLABzsHrFF2tRHDhGHX6TDRYohjmFIxfBJKOV5CRkpLx3OOItsE_1DXYGxu0qmXhT0ZlileGGxn2HxfB35d0MwVwt-cJhRCFZ35WuXYW4PEl7bAxSLc-QEe5VgSMUY-2tA3JH3x9-tBbjidkCTwg1kW1BFOl2AZ77dmfpsc3YILy4-goZXXKLBJg2xB3ecmxpLJBY9BjyeNEtpSTQvzEziviQNeBcmAKe1qa2Zq2y4PXZyhmJH9I2YVb8YU3FzvPKiCMKgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=bP4ywxWaAyuiA6jDIFXEFYYa1sjyiBptMZkGfjqxxh-vATtSHKvorNy214NAGBuC2cAwav1EzXXXQ8pJm7VYJYatT9QtuJjMRAokv8tsEa90Clvt8nt_EDoWrFLgRZ3kyJQyujk5Qzo5X9VTtSPlqJVdZX9BokRGjtMoLygDfb6Wbr8pcympyfKjeNIc92s91IGMLj-Mwmhr1nMaBTDv6Z2hNgyp2N-QxUyjxt-y1vwVAVmqZ2nKBh66S1jPj3CwnK5hutxZTjzLavAPTsHR0Hkvlc7TtuMRy6ZHdyN9W8nmDObi55xW-xWWW3O6vaBQly2A7syni3xIKLzfCrasXYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=bP4ywxWaAyuiA6jDIFXEFYYa1sjyiBptMZkGfjqxxh-vATtSHKvorNy214NAGBuC2cAwav1EzXXXQ8pJm7VYJYatT9QtuJjMRAokv8tsEa90Clvt8nt_EDoWrFLgRZ3kyJQyujk5Qzo5X9VTtSPlqJVdZX9BokRGjtMoLygDfb6Wbr8pcympyfKjeNIc92s91IGMLj-Mwmhr1nMaBTDv6Z2hNgyp2N-QxUyjxt-y1vwVAVmqZ2nKBh66S1jPj3CwnK5hutxZTjzLavAPTsHR0Hkvlc7TtuMRy6ZHdyN9W8nmDObi55xW-xWWW3O6vaBQly2A7syni3xIKLzfCrasXYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9q1cNqkmnbn1NsjC5NoSCO586wBxIPFf352ljh_HKQO_er3DuMfy9x7kSf60uz-2JF2bRPyYQbyv3Lg-KrC9iRY39UvDHSPcYcEN4qbf6-jFjYntOthObpmD5Eu1vc7-SHyZMEOpOaiqex8BnWX5QTM5JZ0yF-rjlNohIObsBLDDniBzRmD6aX9AsrVbCw-GxbRUxnzqC3QsrEYwoTwlMFDU-KTmKU_Ff7JUpmTgBxW9eS0u-ijBmrt7tq0sim1UZEAc_jF3fe-2naD9QsvlvCMnvFUGYDmrd8_cjLeSLu2XGLC8gNzfqKu_pt4EDKOuJ2jmasr8Oulp7QZm3KA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd4iCgDSxMMw1bmHSG1Br8PNpGpBJJ90_a17mbVEcfRMgiGnOFp07Xx7712Qq597qSSqCLnGFJk3bpBVcv_kGDwuLTiU0QNQYLY5uC_wa8aPjbNknPmtAaAFJQBTj3xCk200PQSrizKuCyFN47MuW7ptGz4zHLIQrX4SONtSz8hkHiCjBZvtvrGBMpIcbNvursj7X9KSHXkrShTpA9-dzngWPXEhG_yFceNUsWlJmunOb1NkDGUqlkTclOGJUTBZG2GGe_Y5XkjOvhZJBZl-HuDA85OqiH449kJjph2CjZ9-yBgMy3T7VcywCl_TVMoOiTrPkNcRid5PQQssTCf2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=F3eGlFYiFuATzGzxCzb0U1rzU1spRy3LbRsNx0ecA02TzZVgwJSoXzDRO5uUb8Cyo-io7jEkS6W_yNyuYzTbs02QPQTo1_HhgCU_VxMxjDEaigD1suQ9ZoA87sMNrZJgrE0NAGc6HJ9z-tH_3fCUVYOP3CLjceOWxnA_Wq5PLDzbBjMvWKQK2e2s3XBgDZI8Ewz5vaaDwgQgV9TUzGW2KqplVLyHqSxayjUjftcGShZPpaPHlvSXkRa8kHr9cclN6ZaSGfaKDAEACvri4y1f0fS2o94D84Io-dxW0I9D1x-tmH6Iy1-roztAkaO8YIf_r_SuEYxcCqxu_oD6oX5uhqMC5hZTU5OwHvAv3Lz3gCRkeCKB1aUOZwnXo5dn0IO2fQzdFHqWdtLTQohLEvorVmQfRKAHIH2W12DnDaHc_gU27s3hpnwfx6LrXK33y0ndf8y5CKJ7Il-x7cCg0SFCOGNr7BTSd7abS1LN1Cu10YFC7UNNore43JrUOXFrZcG4SrzY0ZQdKXkaf-IXiZlE6yw0qlanZY102TOwm6tlU9CsjfX_QVNnG71s-HwDJu16ZAr-TGVQExn_6sPW273XRLqj0tcxZuuF5OryezXOQGledehEZj-2wBlCWlNzBMeXpw_42Jxt63VYjelpwtciTCWoKq89gQoHpZmdsdaeCw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=F3eGlFYiFuATzGzxCzb0U1rzU1spRy3LbRsNx0ecA02TzZVgwJSoXzDRO5uUb8Cyo-io7jEkS6W_yNyuYzTbs02QPQTo1_HhgCU_VxMxjDEaigD1suQ9ZoA87sMNrZJgrE0NAGc6HJ9z-tH_3fCUVYOP3CLjceOWxnA_Wq5PLDzbBjMvWKQK2e2s3XBgDZI8Ewz5vaaDwgQgV9TUzGW2KqplVLyHqSxayjUjftcGShZPpaPHlvSXkRa8kHr9cclN6ZaSGfaKDAEACvri4y1f0fS2o94D84Io-dxW0I9D1x-tmH6Iy1-roztAkaO8YIf_r_SuEYxcCqxu_oD6oX5uhqMC5hZTU5OwHvAv3Lz3gCRkeCKB1aUOZwnXo5dn0IO2fQzdFHqWdtLTQohLEvorVmQfRKAHIH2W12DnDaHc_gU27s3hpnwfx6LrXK33y0ndf8y5CKJ7Il-x7cCg0SFCOGNr7BTSd7abS1LN1Cu10YFC7UNNore43JrUOXFrZcG4SrzY0ZQdKXkaf-IXiZlE6yw0qlanZY102TOwm6tlU9CsjfX_QVNnG71s-HwDJu16ZAr-TGVQExn_6sPW273XRLqj0tcxZuuF5OryezXOQGledehEZj-2wBlCWlNzBMeXpw_42Jxt63VYjelpwtciTCWoKq89gQoHpZmdsdaeCw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx6oRjxBjlLWdfLBFrmdguX4ux5Wqtji9xxgTJXPxqSkG0nDdRKM_P6lUUVMW3xvOls2yI1xnO_fH0_uVu7eLfFqtLu0ad1lhhowWpvFr0VKFyloxTdBhYUs3bEItMFv5eFuK4GYQTHQpT-eLX3wXmqgbMb-B5lfsCPTYOp725JCpbqplnyZs2Bn4f6wj5YWP9tKqe-L69hsgzk9HAQkWl1tmYcnB7rxm1bgVVwltQOvHC3UJH95WeJ3x165QZDHqzo1QK3FkfPmUEue5pVDDaeQ2kBZePCG5Afj-8iWd3yfITpKel1G3h-0FzFCLxpVaOo_6WgKxxLdq4mD1h_FMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcBq2a8AuG6Wf31SqgR2pn7y3vZsnATtRFVKUTEIKToNSYcnwa63S3gfemyQvGj7BoKF8C85Eu2ytfRUZUA1NAQjnzDqWCOSUW0AR0Sro16zAXcL-P3PhJS2MMRX4_P1zR8hagDSUQdmnfg_-OK72hB1_CTXBAfJpKiTq0ivZ3mfJE3-u1T9udpwR4bd0778JiOFC62VPn2_WmFvRn1X4A9cMvtCjVPIa_y5nW4m4q-gskmP2lwapkqo6q6A463QWDSXWLU4GsTL78uguwK3uS-NOcLK3bY_mw-A3PWNldNu8H7Y465zH65jh4UVcAeazwmuSOH4zltMb86nuXvf1tOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcBq2a8AuG6Wf31SqgR2pn7y3vZsnATtRFVKUTEIKToNSYcnwa63S3gfemyQvGj7BoKF8C85Eu2ytfRUZUA1NAQjnzDqWCOSUW0AR0Sro16zAXcL-P3PhJS2MMRX4_P1zR8hagDSUQdmnfg_-OK72hB1_CTXBAfJpKiTq0ivZ3mfJE3-u1T9udpwR4bd0778JiOFC62VPn2_WmFvRn1X4A9cMvtCjVPIa_y5nW4m4q-gskmP2lwapkqo6q6A463QWDSXWLU4GsTL78uguwK3uS-NOcLK3bY_mw-A3PWNldNu8H7Y465zH65jh4UVcAeazwmuSOH4zltMb86nuXvf1tOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=b862EW7YoHseqX2j-C1LhH_ae81dltMiT4IgmPPkbt7fuw7Jmv-4X2Q6cqJI5yJHT_zwGzw8Xc5Zk9dTzPUjaTBnfIOikbMkpqKLv9WGNm5cAwy4dc3K20UseP1UAzCQaMhN0oIoIY5kpFDO-aQGXO26G-27XY6gVEATnOY06naw4yA22Do00mBh_m61l8H_GL-6iBIQn02PwSxxJzP8ZVf2SVw75q4kU7zAaKQuQhoH_shnXYuPeSfECjD8VWrLqiOz5LX3jo6t43sG7sV9yIY8Bz7XIdSFrwYaXWNPwJ9vow_j8_NeV3XB2EeI5LvsOIoagnmfHW9LX_8fwzh6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=b862EW7YoHseqX2j-C1LhH_ae81dltMiT4IgmPPkbt7fuw7Jmv-4X2Q6cqJI5yJHT_zwGzw8Xc5Zk9dTzPUjaTBnfIOikbMkpqKLv9WGNm5cAwy4dc3K20UseP1UAzCQaMhN0oIoIY5kpFDO-aQGXO26G-27XY6gVEATnOY06naw4yA22Do00mBh_m61l8H_GL-6iBIQn02PwSxxJzP8ZVf2SVw75q4kU7zAaKQuQhoH_shnXYuPeSfECjD8VWrLqiOz5LX3jo6t43sG7sV9yIY8Bz7XIdSFrwYaXWNPwJ9vow_j8_NeV3XB2EeI5LvsOIoagnmfHW9LX_8fwzh6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=E8UR726cJYskkFDGgwmNYlDWINKx9pKgEC0uSq3nbef8VzWiiUvMEnQQ9_thApIvt9IL-I5labtTz6aDUZskzd4i-Ilw1i1OtAqX-cmIjXp-PS-5nLvfIv0k5YV6ScvQtKOg6LkU1A95r7pYmYpFua048sngxyYXZME_xAeD8B8XrAaXqBLfmcbTfDMSwbV47pWqfoS4gtQWAJM8yHAizOGBleTPZ-y4yQWACqLGFgFLr9_sW8GKxt6u-DgtBeoU5_s-Z--O8xhl9NNeeqTdVd1GVMKG0MF0mbsdxvOTngo8WoD60SREiSQumjBLdUX9GhUB7Ug_b6cu3tkm6Fbj7i7jSC4-KRQi7FDV-w6nSlowP1Y9CmPoyXcOYddngU3rZLxqMKs2nCthatTJTce8bKhVYKGTjrLWMgn6qu3253hZg6FjbRZs7VV4fVm5YkqP0YEZEmyF2N17sQENWaDX0Kz1mJLMM5zwI4uS3it2MyNY_msgzkiqIyNOL79JSZjURS4eMwKWJmFeLduQsULfgPUWejDPh0KgJnEy01DbJ5CkPbeSaC6icoIJHnImPwRQCKTtQHLS2lAnGhSSqzu2wJTiQwmHfgaCl3rtHnmyTfmmsZCgPRpTOnxnDG8jwNavU12wkSvaedO-e7VCBrHl6USoDpvUrBpZtJfANIvIFMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=E8UR726cJYskkFDGgwmNYlDWINKx9pKgEC0uSq3nbef8VzWiiUvMEnQQ9_thApIvt9IL-I5labtTz6aDUZskzd4i-Ilw1i1OtAqX-cmIjXp-PS-5nLvfIv0k5YV6ScvQtKOg6LkU1A95r7pYmYpFua048sngxyYXZME_xAeD8B8XrAaXqBLfmcbTfDMSwbV47pWqfoS4gtQWAJM8yHAizOGBleTPZ-y4yQWACqLGFgFLr9_sW8GKxt6u-DgtBeoU5_s-Z--O8xhl9NNeeqTdVd1GVMKG0MF0mbsdxvOTngo8WoD60SREiSQumjBLdUX9GhUB7Ug_b6cu3tkm6Fbj7i7jSC4-KRQi7FDV-w6nSlowP1Y9CmPoyXcOYddngU3rZLxqMKs2nCthatTJTce8bKhVYKGTjrLWMgn6qu3253hZg6FjbRZs7VV4fVm5YkqP0YEZEmyF2N17sQENWaDX0Kz1mJLMM5zwI4uS3it2MyNY_msgzkiqIyNOL79JSZjURS4eMwKWJmFeLduQsULfgPUWejDPh0KgJnEy01DbJ5CkPbeSaC6icoIJHnImPwRQCKTtQHLS2lAnGhSSqzu2wJTiQwmHfgaCl3rtHnmyTfmmsZCgPRpTOnxnDG8jwNavU12wkSvaedO-e7VCBrHl6USoDpvUrBpZtJfANIvIFMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN9SJPeSvZGQ3aicVCcseLlUygGx_v9jJk5o7wupgfTYvWcq0jLMdxfVAOkPCU_hkC6sd0LXHWuHjkQVFZLAS8z5zHQlHLeGnb_IOHzpjQQI1ha1TSlReYx254v0n7mk7bkEke8J-eXI_oshS1hVSS92qKAjs2AIjBqAQtQPH0WV6P8XZhVcyCrkZc-9FhbB3djTjVEcwqTGGALh6zIzYqz73j9LRTQtvuTnBXKbUcIWCMbZqDy-P4XBNWVeeOjq6TFHA9qNURj4p5A7DOiQJwhXKkJFsoL0jFxyAlk7mndtimenUMIQ__NClIXZr7es-EKX8nENq62mnX4xplaDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNtPBGOPwXMfBl4xmUG5CJVwuIyKtp6XJrwOl-GC2F9OtOlz0Q0q1vTvKYzye-zGMq8wXbgwnSeGviluIYigtIYziEh3d4-dsw9H30KsEyogAbHhE6xH2wEmBMQZpcTf9THI2u6ByMrKU4gfEFS10_gexu3OeTLa-EGQ_2MEKt7xSDoycKrsm-uOAp2Vskcf1JWdHr3O_EhXm4PDrWOrOfR9_Sz8AkQ2Uo55CSvmt9bXUpN3y_70rvaULpVtgs-k6-Io6cdv1b8Y4tHjZOzFkM37x_WMBoiRJF8Xpx5yLhlyVPbCBNoCY28Lz9sFpoaDW_TSmSJOp93xD1_tPE-G0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=e_zFXHO-AgWahVS8AVS3ZfnykgzdWKMgx9n7FRdrcUB0-jpDzp0JzpnMQKTE5ktB9i958d_ANSblOVLJ64tpzmB9xoM3g25w-xnUedD16F5YDxWJ6Kh21r-JH9IyujnZQV9m_mjeFuiRiJRXE_iro09lqkUseXCzNaodqvpTMDpHcbFGkDBqGk8ENRdKNvhCza-_dBfTzEOHsxczfozKBbWTavcFNIjoo1SAgkUJYggfYJFPB7lXOIThLdJYuQflvURKT8GHWVkxiCBM_z0ANqJXCShz_s4JqfFldl1UVl4L4JkqD3kiz7y4b8p5-gQ22GibubRwMrRh4v4PSs0Zyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=e_zFXHO-AgWahVS8AVS3ZfnykgzdWKMgx9n7FRdrcUB0-jpDzp0JzpnMQKTE5ktB9i958d_ANSblOVLJ64tpzmB9xoM3g25w-xnUedD16F5YDxWJ6Kh21r-JH9IyujnZQV9m_mjeFuiRiJRXE_iro09lqkUseXCzNaodqvpTMDpHcbFGkDBqGk8ENRdKNvhCza-_dBfTzEOHsxczfozKBbWTavcFNIjoo1SAgkUJYggfYJFPB7lXOIThLdJYuQflvURKT8GHWVkxiCBM_z0ANqJXCShz_s4JqfFldl1UVl4L4JkqD3kiz7y4b8p5-gQ22GibubRwMrRh4v4PSs0Zyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=HR3Q4oJfZFL4BmH63BFeQdKLW0_djTmedDOTtZCXUgGsvRIxYtwwF93js6xHNedqDClA_ICLKoAYE36jmTaY-y_rTCqFX60jY8gDUrHw8wGqhQH9tKd0ca0MV4ulJwWkLC8hEx0MU_L8D5kciGqtXujI4Bnhvr8O07EP-xIa1LVM6LseoCogW9EUGS0eQa5Hr-EEZHA8v-KPAj_tcpIyEmL36s1bydUJ66WsqboyeIPsb7DQQ8nyO860I-fOeM5oswBl2FF4X9wEJn0U0_g6k0HINpPIkUkgIU1Uvag0qChWUHqHSvASgU8gsRq_AHL3OW2QAV_VHi_GeLH7YJ8UMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=HR3Q4oJfZFL4BmH63BFeQdKLW0_djTmedDOTtZCXUgGsvRIxYtwwF93js6xHNedqDClA_ICLKoAYE36jmTaY-y_rTCqFX60jY8gDUrHw8wGqhQH9tKd0ca0MV4ulJwWkLC8hEx0MU_L8D5kciGqtXujI4Bnhvr8O07EP-xIa1LVM6LseoCogW9EUGS0eQa5Hr-EEZHA8v-KPAj_tcpIyEmL36s1bydUJ66WsqboyeIPsb7DQQ8nyO860I-fOeM5oswBl2FF4X9wEJn0U0_g6k0HINpPIkUkgIU1Uvag0qChWUHqHSvASgU8gsRq_AHL3OW2QAV_VHi_GeLH7YJ8UMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=uRW2McHfbWQDNTDh-z0xzokD_y8hc11AZ2Th33KUzfn8Q2NScUzmOM-UPfyXG6YwIN-8mVMUHmQ-j1bajJf_oZmVSiLcsF79hRuXYpaXnuvP7USbb49I8IG73mQmU3m__KcnIRIxCgQb-3GvYRaDhsQJ-Cf3PAdP2XMeLQRxmsPieTNdAtEkn_DQZsUm5OsJR9n5Ckjj_FfJyOtIVENtjYLK4N-EuGCLTeIXUHZin9uMIk_y_3U0TuYYMylRsBcfS66Opbz6qSW_FpeD-HqIxNYVaIXyA__ykfpsJfgxtYMqaSTpYjN0BRGmGIMAkZ1o7VNUhTwXBZDgilwaGfNV6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=uRW2McHfbWQDNTDh-z0xzokD_y8hc11AZ2Th33KUzfn8Q2NScUzmOM-UPfyXG6YwIN-8mVMUHmQ-j1bajJf_oZmVSiLcsF79hRuXYpaXnuvP7USbb49I8IG73mQmU3m__KcnIRIxCgQb-3GvYRaDhsQJ-Cf3PAdP2XMeLQRxmsPieTNdAtEkn_DQZsUm5OsJR9n5Ckjj_FfJyOtIVENtjYLK4N-EuGCLTeIXUHZin9uMIk_y_3U0TuYYMylRsBcfS66Opbz6qSW_FpeD-HqIxNYVaIXyA__ykfpsJfgxtYMqaSTpYjN0BRGmGIMAkZ1o7VNUhTwXBZDgilwaGfNV6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=Z7vokQPRki8maAFpfoK5cTQf4BGjOXSZHwTJA1RUNyHlDS87uFPAxC9jIl9fEn_KOCbiCXF3y6AWiFOHWp8IozKG6bP9B0E8ftsQUoW5L9-VAAzwM6SnSumeM9hXMUe7NrSv5yyZuIEVe7CeM0qUHBOszPHvpebLA-akRysGRE2kP02ayQWRALo0tmLFHu7_CfzdRRINLC-lnTnd6B8gu2HT37cuNug5Joi_qGVdGKvWph7u_44qgdB-QfNogOlWldrGvRutDl0vCshCjdhu5IJWdG2IVATwHA7Lbe5PiZ3sWprdJyIfegnIICwcfF2dwmby_ipWAdvYrp0vj1XxPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=Z7vokQPRki8maAFpfoK5cTQf4BGjOXSZHwTJA1RUNyHlDS87uFPAxC9jIl9fEn_KOCbiCXF3y6AWiFOHWp8IozKG6bP9B0E8ftsQUoW5L9-VAAzwM6SnSumeM9hXMUe7NrSv5yyZuIEVe7CeM0qUHBOszPHvpebLA-akRysGRE2kP02ayQWRALo0tmLFHu7_CfzdRRINLC-lnTnd6B8gu2HT37cuNug5Joi_qGVdGKvWph7u_44qgdB-QfNogOlWldrGvRutDl0vCshCjdhu5IJWdG2IVATwHA7Lbe5PiZ3sWprdJyIfegnIICwcfF2dwmby_ipWAdvYrp0vj1XxPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz89J-lq3JRFvQqfkDzrkMRNAURW-CY5wOak6FkAaktp1VfzK3kgOtHbs3yfFtsiglUDHqDMEj89qzaSOQIu_qY6P6TXsNzO-IQ9LCx8qvaPBAdJWsiFRSy-YFSqQiQ_oOwMwW1F9npslgDCkXYG-5H0niHJDzSw-iuB1hEicEimjEoFuE1w_74kCM3mQLzcwcUva-1EQztNeCKhcm6i7ShAf7mCIdNYt5HRYS2YZtx0357tTANsx4oGAK3s7pCm0HXiDEKdtxAquxw7cbdNDPmnt9ioy-IooQrHcWUnbNy4wB2HukfQPC3mFb7-qeepSMkNzehlajexH_KCSCpYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-MJOiPqpIs9J7b-dpK_xr_E3MoXuzUTH1DoWO0fZhmK3C1Plm_MaUa-H_px168BmxxTxsxdL1V4IKjpyw0ed75dnbaWgv5Uy3EE_NofNpnndR3uqg7oPWpvYjfry32-UWpgU9Tq_qnsAaz6_B7vN6UczypeDKEtalyJU_bS3ATfneyzmsUCgzJ4tVlb-199ca1vN-YtuKDO1fEeFsCklf5bX40sdiKiShpr79TGCDWi1xOWLgXwG23TJAELSUagxlr1ATnaBZpxDQOYcyq1IrJEeswg9QWJ2H6t_DAgWNQZjt1sWKgncTx1OcqI-QrhaWpcG9i6CRa5wMMyMV1WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=vhwPlxwGYeLbjaPbkl4Eo0KqHETZQccK5O4EVRadYNTvZhIF-6WZMI8YrYQeEEk_1j1PoyWMleiwk8-S_95XxAy0XvTzl7NIzG3jCdRZRSgJo23xCWKb_zWWTR-f093g8wPm95QKqeBPcU4JkdtJhAFvWzlvhPN-0qUiu8u9CHnszebN3O-rZyGzzLmNlpTrc53loE7eGkjJzAnOuKCUe9MH2Olw85_quoujuiAqLFUiM0wRYduL1puFnh1GzeC03vrPjDLjue166dGs2qBAB6YNpTbs9fEdS03IJKVemWvMSktkrhDcuGGcL1PS6GVK6fKNV1cO3iaxeNnB9_TtQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=vhwPlxwGYeLbjaPbkl4Eo0KqHETZQccK5O4EVRadYNTvZhIF-6WZMI8YrYQeEEk_1j1PoyWMleiwk8-S_95XxAy0XvTzl7NIzG3jCdRZRSgJo23xCWKb_zWWTR-f093g8wPm95QKqeBPcU4JkdtJhAFvWzlvhPN-0qUiu8u9CHnszebN3O-rZyGzzLmNlpTrc53loE7eGkjJzAnOuKCUe9MH2Olw85_quoujuiAqLFUiM0wRYduL1puFnh1GzeC03vrPjDLjue166dGs2qBAB6YNpTbs9fEdS03IJKVemWvMSktkrhDcuGGcL1PS6GVK6fKNV1cO3iaxeNnB9_TtQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=rz3PpcaEooIS2vNCxRuFJ0p0NRVadiB45wRqG_g7O1jhzzKPhXufUKDMOejth9MspZdAW0J7sjtYzlHmr_Z1U4ZVkRHbJqP7a6yVT64R4iPpORlhacrmU5g4QodbVlPsyb76QhK6tzZlhMfdorJyUvr3pA3K3YoO4Ns3sLeHlyD1RyEcuGpfcI9a2oIwZ4PR_-_b9PA9YDGi2wKWEVSTI5KFTDqRvvS3yfZ0s7gyMOw_oUeM8tjvR-yTIVZj23iyytsgZbEnTDDJLky1fSZe64nvqatxWWmayi6pTsE1QasJ7RDIxjApljiZkGTkyiaSGrxpsgtw8DL5R8cZ9XwJepunm-4THjHoBPQIaDTHbRspT6XR03qvrSkVKCrglQxmqb5Ji3obzNHQ--pvpFO-0jJDn0Ymy_5rfWHogV7dEDvy8TdPn-rd8pnLe85bHX4ezta95NDI58TpWwCXpHt-PwMYM2dq8qXmStXUhRXzLY0GQdqng5lwMaQYfEjINqsSxjT35V-Gc6DF5HpofO4jghdxZfdJrrYQY7RUQDfHNPvVXmbzKyFYvlp51EfRgOKBPizVU04BZeedDr1dXJO6L9_B-yHMJH8zGdI7IAcMtJxwbrNbIvzzUiQAJ5RHbLzOwCYnb_fC7CKUa4iiMjHFSkNjtU2TvUBX1vo6UqUXuQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=rz3PpcaEooIS2vNCxRuFJ0p0NRVadiB45wRqG_g7O1jhzzKPhXufUKDMOejth9MspZdAW0J7sjtYzlHmr_Z1U4ZVkRHbJqP7a6yVT64R4iPpORlhacrmU5g4QodbVlPsyb76QhK6tzZlhMfdorJyUvr3pA3K3YoO4Ns3sLeHlyD1RyEcuGpfcI9a2oIwZ4PR_-_b9PA9YDGi2wKWEVSTI5KFTDqRvvS3yfZ0s7gyMOw_oUeM8tjvR-yTIVZj23iyytsgZbEnTDDJLky1fSZe64nvqatxWWmayi6pTsE1QasJ7RDIxjApljiZkGTkyiaSGrxpsgtw8DL5R8cZ9XwJepunm-4THjHoBPQIaDTHbRspT6XR03qvrSkVKCrglQxmqb5Ji3obzNHQ--pvpFO-0jJDn0Ymy_5rfWHogV7dEDvy8TdPn-rd8pnLe85bHX4ezta95NDI58TpWwCXpHt-PwMYM2dq8qXmStXUhRXzLY0GQdqng5lwMaQYfEjINqsSxjT35V-Gc6DF5HpofO4jghdxZfdJrrYQY7RUQDfHNPvVXmbzKyFYvlp51EfRgOKBPizVU04BZeedDr1dXJO6L9_B-yHMJH8zGdI7IAcMtJxwbrNbIvzzUiQAJ5RHbLzOwCYnb_fC7CKUa4iiMjHFSkNjtU2TvUBX1vo6UqUXuQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=Vx3P3RhXBOkJcncHq3VcbBiy9T3OxarOcVeOz3qQNB44Q9LgaUBVowOaY9oWmv904T000pzhYQbYs8QjjI2eY66falu2S7xX0cJk1WyLN1MRaYTyJARTMWlR4wMW9U5DBPVRvG2MXoVE9x_02M3rPp-zVdF52yOJFerlJObcnnzC6Pk8MekN0unbM6Tkg-B7xa0QQwPVIAaPigWqGkeq3OruNvRIK4bHl3LBQWluLa09ojeXagnGEEF-YQ9ERygxskJ-zjKfUM3bvrJR7af62yYKZry7hqnBzcyujUf28xCqEEt__D9GfKfylDTA8SUotqiuftqQGWkkQ5zKQr7izA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=Vx3P3RhXBOkJcncHq3VcbBiy9T3OxarOcVeOz3qQNB44Q9LgaUBVowOaY9oWmv904T000pzhYQbYs8QjjI2eY66falu2S7xX0cJk1WyLN1MRaYTyJARTMWlR4wMW9U5DBPVRvG2MXoVE9x_02M3rPp-zVdF52yOJFerlJObcnnzC6Pk8MekN0unbM6Tkg-B7xa0QQwPVIAaPigWqGkeq3OruNvRIK4bHl3LBQWluLa09ojeXagnGEEF-YQ9ERygxskJ-zjKfUM3bvrJR7af62yYKZry7hqnBzcyujUf28xCqEEt__D9GfKfylDTA8SUotqiuftqQGWkkQ5zKQr7izA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKjUCjXBs8q92fmtIQJE9-OGjV53ldpUeV-fy57b5bLJ4GIdgLc90XXy8B4exnv4YKWqiM32ss3AEWaUDpz5omyhZEZrNjin8BvCc9WokBsuryA2CkQLkiJMadkuAFuBKG8SAzgyaFUAU4aQcUYqYwUObb-pw12CE5EfvGVQU4COIs1PXSbnujFRwz9AofvpBX8DSouy6CKIkhGLd_VZBEYp_JurUnNHGX5i6Q1sFLo72HLwUeZeUH4Y7SNVoHjO5DFF4x8gKYvWO2pDpdCPgPYu-haDh6aBSB-1kZ96nieiPaLK6zm3t0JeYV0Es7GW8-fquYSTJMYP0mXsKKfDKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVdhAkdaVdzmzPi61-IGjZllk8P5AAJZmtZhUx0gxxm65OqgmgUNRUMJHlLzDAXH1Pjfke-XWYMk8Erdu1x8jvowegnPJkSUWLvBUDxcaF21-vE5Q5t_r2Fcirg-BO6AJwu5EdyzWBTFbH-2UeFw7lhJwTruszO8AI6WgCUibM5vS0oD90-2K79zLU1Xc1reh7iUNpwAQZMRGDsl1fY23q5H8KTphftvf8H7-lREPGrTuWQj8MX9ex545bSeUPMOA7WqPNJYY16tAysyKiOqkfr6pXxNs531gGqvms_D7XU_tI1qlBNPkWT1sxAh97oPBhLjE4DVhxKgcZkU6dmctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=kc14tfgWcreCD-SytMSM5yWty3twwb2i9PG7YWYJgKlHvunASbcxrXInAqrcdakfTX-Hs5QsrLlEhPFaPXvOBBCA--NSL7Xj1MizrgPs3WDHr1YW4W3H5JOkVGq6-sDoLGq4HqPE-2Sc77HqKrMoTJCQEL3IHiK52MEdX-ipVMaWeXTjiW3ualrdvQjtqEFkir2mQKQwj7CWnjFElEViO3sIwcnnTVCOjhK4GeERDh8gf5YhrstQqzO7-RCIvuOB3LfZfmieJQUool5Jvb9ebcJJjnuMzF_Ob6hi2Vapveh-lWwS_UKH0dZOKIo3GjqWjmKrQiS_8HekHT_JqgFSlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=kc14tfgWcreCD-SytMSM5yWty3twwb2i9PG7YWYJgKlHvunASbcxrXInAqrcdakfTX-Hs5QsrLlEhPFaPXvOBBCA--NSL7Xj1MizrgPs3WDHr1YW4W3H5JOkVGq6-sDoLGq4HqPE-2Sc77HqKrMoTJCQEL3IHiK52MEdX-ipVMaWeXTjiW3ualrdvQjtqEFkir2mQKQwj7CWnjFElEViO3sIwcnnTVCOjhK4GeERDh8gf5YhrstQqzO7-RCIvuOB3LfZfmieJQUool5Jvb9ebcJJjnuMzF_Ob6hi2Vapveh-lWwS_UKH0dZOKIo3GjqWjmKrQiS_8HekHT_JqgFSlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye01RVriT_KmjrDD59XKdKtNxH_iuA2SIONIEIEebEbWsZpY7PpotnHo4oFEg9dC7_l80tq-9LoiNGzom2lPo2WiIpKx-I6qUJ4A6QKClu1ExeLPs_3YjsmyFUVrjkEgxsEnzOgZRDbzokgjEwFHJ7uoX8GqK1TxwULxIf7PcfiGblsKJ781CHly5b4hvccx_hZysY9Hfp26Mre7y0WzRkT6TVkx6tVL1dNnTZY2tzH69ofJ7j7Z-2hHK4KrH9Xc0li2zGKSOdKv0yt9DjTBaO8Chsof2MWYTt4dXZR1DWxz5qJTFPm73zGQqxuIU21BZyEisbwT803042FDynsbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqWV4MltyDR_oCEu1fv3BfgLbqyk8ky-8QxWApUtEADqcfXT4mHe1BKDmruvXrLrykQqCBbogSZo99vzmhkdGAHmq08ZW0s4hR4PREPGz7PbCY4YVzi8IvDFMmD0hi8p-KA_npFuPbHGIehArtO7E7hydkMpE3s5gpsdhuECOHOx_Is0kbvbEH7Yzc07vsDUYvTG62y-GVWdAi3YjboMgdyQcLqMQfqktaJwVII-BdjCPSmBi__axXYkVYotgoSl_ncA5S7W0N2Q2EjGC6djbitHwQMlRBaYAjSSJXKDm7YhZj4-e5f5SLPUzFmMibJwDGQQ-X5w0U1Shio2kpWB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=iPloeib8-D1abP2oCgk-XtNxha6MLpQz2uqhtdi85eyH6Ca-qwt-u2lLAKOxiXVLXwh9IuzOX1edgCiRbBpm0hkCheJ0Gs-fKCZYNDh5jqugScUv05ieAASbbi9hwIAe0Z643drZpBBW6OttlLNsNuI9uhsAASXmQiS-eEKn_qYbUuNY9BmLOezxYjVD54M_Sj_gPFFgUvogynPXIW0iBB1bya1lkYy__lJn5KHwfvpapV8Dwn56cmGcVfqp4g8ELd3iaJq7ywIYxu-1Zeb2rF5UKHlIe4LtyGS8LwyWCFNgf90a2sl1rDMzkVI8vzMht-rjOY7C4itq1_4BbqHcgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=iPloeib8-D1abP2oCgk-XtNxha6MLpQz2uqhtdi85eyH6Ca-qwt-u2lLAKOxiXVLXwh9IuzOX1edgCiRbBpm0hkCheJ0Gs-fKCZYNDh5jqugScUv05ieAASbbi9hwIAe0Z643drZpBBW6OttlLNsNuI9uhsAASXmQiS-eEKn_qYbUuNY9BmLOezxYjVD54M_Sj_gPFFgUvogynPXIW0iBB1bya1lkYy__lJn5KHwfvpapV8Dwn56cmGcVfqp4g8ELd3iaJq7ywIYxu-1Zeb2rF5UKHlIe4LtyGS8LwyWCFNgf90a2sl1rDMzkVI8vzMht-rjOY7C4itq1_4BbqHcgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVl4qPPV5HauP2hY2FCEQTi_vc-oZegO066WkSdo7Fe76T_g1OMGzf79htSVhEMpwL4bAZN8eaU5vEzJnKNEV2bZ2g72nFeImbGVjM0MY7K-D8NoKK3yKjupCJr8rfpbl8Hy1Fzn3qPFZcsJfx7xC6boBUS0XHqyLsv61o5Z73aBcY3yGV1KbplAEOI496HYp_e1CSwsGBCQgNO4Zsj4FAdyXfzk2W7dGhA363ebMjKWOpBGJxfdSJP-YWxXMOOQIXQhMTxQG8pZtEojlsdwW13DnxhEtsYeypplrx978K1LeuAEQVkrelI0_hmI5x2orF6ASaP4dDdz-p1dqEiYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BITzO0Z13hJ1czuRueTxgBeubdgWRTUIH4Yr7fAwCXtWoDeWp80jFagNNLgR0ZiX1SfPgeLucT9AxytuXciCRN4AbzYOBsL_yZzaV1kStbFy5bk5XXS6titERCvbkwAZBoqm2KAEjyB-o-2NffkDQbvGjteqPN0hMzgasLn62mHYn7JlX8KSOePyyRIq2Z-vKpDSgU6Z1UFwuksN4k6hcs9omtPTtBW1rOgJ2lD2OFdrfuT74KSoekhR6SFKS2TNtKwnfSyHbdhLoX088H0O_gYenl71R6501v0xSVizEMRHSAv_5smoSqoaXk0eSKJKKmLomdXrsOY6ewifievC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=UKayNpmWQoG1kDgF19CZspC97sGD6PXSVO-nD7C6CSZHYRJ4PIdWAEEYZVbgzg2j3Q4SDlGrr6FycNCJTe5TEd6kpUOqjtARTbgMQIOU8nb4mrupQLa6S7fNlxCWUS8efZL0EysibkNN1rZXoQv5h8gAW6ZzjEg2bUvBmh29yzEnE2JRo5Q9K8CToxO8WHgLETfQrXHqKxM9UcN_K4V7lkjxBo1gKlOg6H53H2UlwwHHcoFaoKtIh0ODK4CT1LKEzy97AIl_F2U-TJALhijTDcf4NWeQmfjHl8H2N3Q8sr3td48AipKPBzkeOKL1U8cfaGV3Mks8OlIeZE6Gy_6v7Sgnh5hxbYhenQOAPy1iZnekyAiu9uB6lHJMCf_B5UtOlBI6D6mOcjIdxpWYqxgSnQ6IK6PyaelmQio57fDs8-W8VSJqjTX3F_SY8AANR0giBs8Z2OgsI4BrEcunsKS3Cfp0ja3YQ7sCPc4fg_EPErI5yposKpV44M1IIX9F_hNF9OD7XSyaMxDLgum2p1YDEGGXuf-h6uK9IcS2BWJ4IIAwHUexRtlCmi4xeG_f6BsmYEgfiBbae3Q-dBQueRPW0dQVm2Kkkox7UsPc4P6n4qeG-7GZw_vpluw1GmUI1oinKLb2Reyqs3AjIKyYOpEfVyQO3Wz8kV-DH5wTVl774BE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=UKayNpmWQoG1kDgF19CZspC97sGD6PXSVO-nD7C6CSZHYRJ4PIdWAEEYZVbgzg2j3Q4SDlGrr6FycNCJTe5TEd6kpUOqjtARTbgMQIOU8nb4mrupQLa6S7fNlxCWUS8efZL0EysibkNN1rZXoQv5h8gAW6ZzjEg2bUvBmh29yzEnE2JRo5Q9K8CToxO8WHgLETfQrXHqKxM9UcN_K4V7lkjxBo1gKlOg6H53H2UlwwHHcoFaoKtIh0ODK4CT1LKEzy97AIl_F2U-TJALhijTDcf4NWeQmfjHl8H2N3Q8sr3td48AipKPBzkeOKL1U8cfaGV3Mks8OlIeZE6Gy_6v7Sgnh5hxbYhenQOAPy1iZnekyAiu9uB6lHJMCf_B5UtOlBI6D6mOcjIdxpWYqxgSnQ6IK6PyaelmQio57fDs8-W8VSJqjTX3F_SY8AANR0giBs8Z2OgsI4BrEcunsKS3Cfp0ja3YQ7sCPc4fg_EPErI5yposKpV44M1IIX9F_hNF9OD7XSyaMxDLgum2p1YDEGGXuf-h6uK9IcS2BWJ4IIAwHUexRtlCmi4xeG_f6BsmYEgfiBbae3Q-dBQueRPW0dQVm2Kkkox7UsPc4P6n4qeG-7GZw_vpluw1GmUI1oinKLb2Reyqs3AjIKyYOpEfVyQO3Wz8kV-DH5wTVl774BE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoHo7nsI6IkHVWX3CD4JmVi0JjgUnzCcfOWDsevL6Vu6an_IaXprebXeRNGWDGCoqlXZuWF9tUQ_OSEM1QYQ8ol7ZcHMqcvxw_E81NB2chla-W1St8u1OVg_XYEXYUggZ4AF6Vq_fEwH99DfjVFnQtcG0gvA3mb4_ezQ3M4to6Alw6KA2sSJZOVksulaAJJXzEZKKgi36Q8Xozz-Pd_5XtCG9flMXHDjg22VtVNxQvPCiOqOqpv-jWdxjM61OX3nnAthraB-A6dvMYtKr1ab1sZ6oZMlgu9jSlf1kJ-e-Gxv32b22wvTkAVEQe7YvWtVd5WdlQGi7BsU7dQ5bMWRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EbvFQ8-I3kRkwaJgk9fJSr6DEbJe3N_RuszUuDTnE4Eq9UUnEslUVjzCk2IB_YymtJ3d863CswE5yVrzXkJzUa2QIE5kR5tEoQ59HN8FpKs8JhQxF1yZOqszAeHkk2keUpFWYWLc-OGLq1UmLn_NtQCkxa4sA5jVqc4DBKyAg7M5zjgAU6IeD_u3i8bt5zo4RibEeL-b8jddzBXyeMEhkEl-958-eskf4l8MEiE3BLT1B0nGCYOI3l1M3Of_k92zYvy7BVoYfXKjG00YsMUnShV94_scQUXTLWO0sqJRtTFAUzCIwblNLJtcWshMikq-KptTBpmFJW8YGBDyAUcxG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EbvFQ8-I3kRkwaJgk9fJSr6DEbJe3N_RuszUuDTnE4Eq9UUnEslUVjzCk2IB_YymtJ3d863CswE5yVrzXkJzUa2QIE5kR5tEoQ59HN8FpKs8JhQxF1yZOqszAeHkk2keUpFWYWLc-OGLq1UmLn_NtQCkxa4sA5jVqc4DBKyAg7M5zjgAU6IeD_u3i8bt5zo4RibEeL-b8jddzBXyeMEhkEl-958-eskf4l8MEiE3BLT1B0nGCYOI3l1M3Of_k92zYvy7BVoYfXKjG00YsMUnShV94_scQUXTLWO0sqJRtTFAUzCIwblNLJtcWshMikq-KptTBpmFJW8YGBDyAUcxG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=ikUT8zs2-oLYYKuFWejHzEx3un07AUMrroCtQLMbvVEOQs4YFpgUhdX5XN7bc_SYicFUYR7V7y7Ixn_fuXK44W4ttWv0pAYQ2XAthBzB9Miu7Jbza19bcn659x-MTmLSKLHvGa-EukHQoRHPqO06SuBiaEiA6tyjEYkataOIy0Cy82yldTuh_be8CMZid2RaCjMpqhip9OHUkZu_RMOQoolcYKJXC6uNxnYP34fztMz7rkO7fm_T5-cZe61jHVGuC8Gk9su0WZ4GRISvtUlANvp7qtyB98E6W91X2USw9jLNCxEYHbspkRh49iuDfN9nWRmFaKGxqFF75GuheaMhHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=ikUT8zs2-oLYYKuFWejHzEx3un07AUMrroCtQLMbvVEOQs4YFpgUhdX5XN7bc_SYicFUYR7V7y7Ixn_fuXK44W4ttWv0pAYQ2XAthBzB9Miu7Jbza19bcn659x-MTmLSKLHvGa-EukHQoRHPqO06SuBiaEiA6tyjEYkataOIy0Cy82yldTuh_be8CMZid2RaCjMpqhip9OHUkZu_RMOQoolcYKJXC6uNxnYP34fztMz7rkO7fm_T5-cZe61jHVGuC8Gk9su0WZ4GRISvtUlANvp7qtyB98E6W91X2USw9jLNCxEYHbspkRh49iuDfN9nWRmFaKGxqFF75GuheaMhHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfr5pS4-RWS1dGOOcxBPi09W9bi4drUl9Y5I-lMIH3kx0v_7S7jLuaZVncwYR_Zz6dgpS1cvK-WAqXxovFS6Kfpr6SmdXv1oBY5bs549ltGEX4zcgBGIWVL_GFMt5GJ9FFGXvuHsF4mlg96uMvFjmucb26qEvP7iXHF-iHguhCgSHopKzPyHdW7MDdzmR_xc9WFvNkhBKLb2X_DR9footX2xQy1wO2XDMOvNu2tieRNsotWGRR2cuafysHPEQxrGIAHR67MWBzjnTE2uBPQZ3YsYNZo9h2sHcumUTnc3yWOVYTV4cqsQltY7Z8bBEB3cICk8gahzdoZJJoBxw_VLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=ftpryMqGwqXLxrVsxTGJrjmZLDH14fJk5js4BPG4bvG2ZkeJQyjgShBWmGXwL8KTW5SruQKTLGaCnEDX8jVVgrn2q7lPm1auMFmj5rusiUH9ioJaPpTrKRIA1v3CogqrmCEZZOuYcrFjjvFndPwyqBV6S1huTtJW_hjkU8k6igUosAtQQd1z2FtZ4rcftd2YuYmVEZhUd78zis6VgRPS-YV_nW68TN1FKlMkOddht0hqT4j7hJsIessKITEp51jnHp2VOJuJ9hjpIh3TOeRICp0T3I3apqJywrGG5Y7GarRSGd2Yr5QdpP4X49lSlfGBSl4TND9QpY6r6Ex8wLuZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=ftpryMqGwqXLxrVsxTGJrjmZLDH14fJk5js4BPG4bvG2ZkeJQyjgShBWmGXwL8KTW5SruQKTLGaCnEDX8jVVgrn2q7lPm1auMFmj5rusiUH9ioJaPpTrKRIA1v3CogqrmCEZZOuYcrFjjvFndPwyqBV6S1huTtJW_hjkU8k6igUosAtQQd1z2FtZ4rcftd2YuYmVEZhUd78zis6VgRPS-YV_nW68TN1FKlMkOddht0hqT4j7hJsIessKITEp51jnHp2VOJuJ9hjpIh3TOeRICp0T3I3apqJywrGG5Y7GarRSGd2Yr5QdpP4X49lSlfGBSl4TND9QpY6r6Ex8wLuZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
