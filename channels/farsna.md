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
<img src="https://cdn4.telesco.pe/file/S-2EFMzQGVX19sRpBdCmUZrykN_iwFmGpwyhL-A3p-CNqGhunzpvjCOVge9HY0uXpklIxHl03puvd3_XPCKFtgas8vsJMU6rYwN73KY-zEtYYLqw1_rWdlYoajYNyf1OL_HATq0Uo4H9Batpb7YoB6assDn3TcHcwdSI3xI1vzHr5b30QVbS2SaRZe1g1RV4j6ygJqSjQYXSzeiIgOf_oxwPGQfkuLKJzBeFh70mWZiuq__ptvUSNP3CjEghodgqSE0gDVrD2UgLknMdqS4y-2FJGGzqmyqkVg-GbG8W7XhoTmb38k73zpqvj-hehO5uqbJyyJQYm5Fe7tE5X-dZMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-465235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a16f9106b.mp4?token=N1TcmCcjXKAdLrmPjBedYEjxPOk6PYlsB8DvSfcJUP0SxN_z67AsnVNIT1M7rQTCK5565qP-3I4F6VVAnc6Pg8gi-zj08D2_ez3-3L0yn3nSJwU0bFnG97Qbpk3xw3gbr6bMfpuAc1evx5X7DJrOngi7PfxLGmjMQ3kMFt29YUT8o5Qa4R9WWITDbX415G5BT1AR96gQKYBL0bCvH-ZVV0K7wFh2YK6JJE8Ph70UOsJJKD7-5gS4NKqWZY7_XFzoERUkgwqJquIgixOAJc8-gTmt7jpV3l-N08eAcOzl5Z0cyq7gLAXlG5al0O8PIgP0lBNPEz4wHlmGZmWKXEMYVJTuKjcKLdMeS9PSBTr0i9xtPP-gky5LHeNWuNIOPjPQlcU-0T6cTN8gNup5WBUBtz3LOgW0eyqrBdedfTRuIr3H6miHeGx5LTmWLYf59dkZrccfR_5hLlfL_yuqnAG-WKOEA7DnLPQHqm_V29U_XTJlbk3StQcmS7osvobT2jHJBJW9nVgC9kcHVmkQRfSBCsO_25iGNnGjoH-EjZCpdib0nuEyu4k-yOBzxFuaQ1amDMDcT1jzdcD8QaUb1Ch1PddWo3-cZMA9Mduq0-mUOHqk6lTKArgpjUru1LTQjqdp2iLP0KVPQhCN-B4Cb7-evbK-TAECJ9cq_Xjx3MxQUbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a16f9106b.mp4?token=N1TcmCcjXKAdLrmPjBedYEjxPOk6PYlsB8DvSfcJUP0SxN_z67AsnVNIT1M7rQTCK5565qP-3I4F6VVAnc6Pg8gi-zj08D2_ez3-3L0yn3nSJwU0bFnG97Qbpk3xw3gbr6bMfpuAc1evx5X7DJrOngi7PfxLGmjMQ3kMFt29YUT8o5Qa4R9WWITDbX415G5BT1AR96gQKYBL0bCvH-ZVV0K7wFh2YK6JJE8Ph70UOsJJKD7-5gS4NKqWZY7_XFzoERUkgwqJquIgixOAJc8-gTmt7jpV3l-N08eAcOzl5Z0cyq7gLAXlG5al0O8PIgP0lBNPEz4wHlmGZmWKXEMYVJTuKjcKLdMeS9PSBTr0i9xtPP-gky5LHeNWuNIOPjPQlcU-0T6cTN8gNup5WBUBtz3LOgW0eyqrBdedfTRuIr3H6miHeGx5LTmWLYf59dkZrccfR_5hLlfL_yuqnAG-WKOEA7DnLPQHqm_V29U_XTJlbk3StQcmS7osvobT2jHJBJW9nVgC9kcHVmkQRfSBCsO_25iGNnGjoH-EjZCpdib0nuEyu4k-yOBzxFuaQ1amDMDcT1jzdcD8QaUb1Ch1PddWo3-cZMA9Mduq0-mUOHqk6lTKArgpjUru1LTQjqdp2iLP0KVPQhCN-B4Cb7-evbK-TAECJ9cq_Xjx3MxQUbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موتورسواری روی پل عابر!
🔹
تصاویر منتشرشده در فضای مجازی، حرکت عجیب یک موتورسوار در مشهد و استفاده از پل عابر پیاده با موتورسیکلت را نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/farsna/465235" target="_blank">📅 12:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a0a2ddb6.mp4?token=u96_oCFfyRgiE-7BA2mIw1yjKdbNW2tBIfprsvTpFJUsAKi--Trp7x_06Ol8WgUIfvgEzjFLCL0Zee42xo4AgvfdJjr-nqEI6JYqavjFPAQbHiMpGw-ZRx1a5ntIO9L_j11LfCFohFIElv9P3n5oDKStmmLQIzb16lgKcGaiw3a-WQf_HSRjAyLUg0nfTr8czsK_2MaUg0JJSMpJlUR_RFEFgVhWy26O5Cn3gP6n-pIIHzN9STOMiDa8GF_xJi47TVK7RuKMmnHRHSJ3Gtoj-6TRkpYb4vhgG2nEzZuge_SGWJoeVZVdfA8TwAzbW_-KWWIenvJtAlBuzA6_YY8nBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a0a2ddb6.mp4?token=u96_oCFfyRgiE-7BA2mIw1yjKdbNW2tBIfprsvTpFJUsAKi--Trp7x_06Ol8WgUIfvgEzjFLCL0Zee42xo4AgvfdJjr-nqEI6JYqavjFPAQbHiMpGw-ZRx1a5ntIO9L_j11LfCFohFIElv9P3n5oDKStmmLQIzb16lgKcGaiw3a-WQf_HSRjAyLUg0nfTr8czsK_2MaUg0JJSMpJlUR_RFEFgVhWy26O5Cn3gP6n-pIIHzN9STOMiDa8GF_xJi47TVK7RuKMmnHRHSJ3Gtoj-6TRkpYb4vhgG2nEzZuge_SGWJoeVZVdfA8TwAzbW_-KWWIenvJtAlBuzA6_YY8nBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوی تبریزی در رزمایش جان‌فدایان: آمده‌ایم همانطور که رهبر شهید جانش را فدای وطن کرد، جانمان را فدای وطن کنیم و انتقام بگیریم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/465234" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465233">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f862792ca1.mp4?token=iZESuI_4N4gzwsGOIeG0BVj1-Z-QEkh9sJeAuZS4n3PW--X8CzLfWK4wWbnGiEoU30oEv2HOEz88V8SY8FdxVNRQ091VGRKimRYIDIr5wfJUoiewrSPhMiV4r3L8Xdzk9dVgh-hxSN9BN0iSFahY9BhLa9DVmfeA6gpM7fBfOtZv8riz7I7EwPQ7ljiEuRmm_Rc0DrxQ1vYZMGyyup8IjotL1reBm2az7kfA5j_JNg-x6HmoAAwAWbYbEqP0IrzF-OQPbjlpvyBDszgmLEWcVBmWakg_KKMjq8zYsLB9G8wwbQj-wcBxTle5UOc48HqEe-3saH0La0dChmafaiqO2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f862792ca1.mp4?token=iZESuI_4N4gzwsGOIeG0BVj1-Z-QEkh9sJeAuZS4n3PW--X8CzLfWK4wWbnGiEoU30oEv2HOEz88V8SY8FdxVNRQ091VGRKimRYIDIr5wfJUoiewrSPhMiV4r3L8Xdzk9dVgh-hxSN9BN0iSFahY9BhLa9DVmfeA6gpM7fBfOtZv8riz7I7EwPQ7ljiEuRmm_Rc0DrxQ1vYZMGyyup8IjotL1reBm2az7kfA5j_JNg-x6HmoAAwAWbYbEqP0IrzF-OQPbjlpvyBDszgmLEWcVBmWakg_KKMjq8zYsLB9G8wwbQj-wcBxTle5UOc48HqEe-3saH0La0dChmafaiqO2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوی تبریزی در رزمایش جان‌فدایان: آمده‌ایم همانطور که رهبر شهید جانش را فدای وطن کرد، جانمان را فدای وطن کنیم و انتقام بگیریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/465233" target="_blank">📅 11:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c80cd563.mp4?token=JsKOpTq-aiWDtYy8vj3RW6S4333k9rpRptky5C7n1vSD2QiAw7fuIwSNsTjiVhBK1lPuFB3Y9rj-GyZaFOgOBycOo91gvgnvTZRElmDc2PggAHcXjFf-XQRmfs-f-QgJkHz2RTsO6dRMAxs2eg1S5_cmaZrtDiWc5EEao8vlx1RjEQ8JglIP7tgReC6WYvEnlTBrMNWRA9yzG7SxzWQEx_SegQdT5mWPLb1_OzF4_uByspTXmRIyJCjUkhmOiopF2oyba9GvqdhCC8g86onxQllRTkQTkSzc92ZIn_iavwquznTJvlcXIDDuiNi-gNJBHy06VOZcZnqRn0WntNwX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c80cd563.mp4?token=JsKOpTq-aiWDtYy8vj3RW6S4333k9rpRptky5C7n1vSD2QiAw7fuIwSNsTjiVhBK1lPuFB3Y9rj-GyZaFOgOBycOo91gvgnvTZRElmDc2PggAHcXjFf-XQRmfs-f-QgJkHz2RTsO6dRMAxs2eg1S5_cmaZrtDiWc5EEao8vlx1RjEQ8JglIP7tgReC6WYvEnlTBrMNWRA9yzG7SxzWQEx_SegQdT5mWPLb1_OzF4_uByspTXmRIyJCjUkhmOiopF2oyba9GvqdhCC8g86onxQllRTkQTkSzc92ZIn_iavwquznTJvlcXIDDuiNi-gNJBHy06VOZcZnqRn0WntNwX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظی با صف‌های ارزی؛ تجارتِ بی‌واسطه به جریان افتاد.
🔹
مصباح، فعال اقتصادی: پیش‌تر اجبارِ صادرکنندگان به فروش ارز با قیمتی پایین‌تر از بازار، منجر به شکل‌گیری
صف‌های طولانی تخصیص ارز
شده بود. از طرفی تجار نیز برای تامین ارز مورد نیاز خود لَنگ بانک مرکزی بوده و نمی‌توانستند با یکدیگر معامله کنند.
🔹
بانک مرکزی اخیرا
مسیرِ مستقیمِ معامله میان صادرکننده و واردکننده
را هموار نموده است؛ گامی حیاتی که در شرایط فعلی، سرعت چرخه تجارت را افزایش داده است.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/465232" target="_blank">📅 11:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLxr9K52LnvfnTQpdaLAAb7ml8aOfowV-vnJTIDQgU-r5cwsNWqBZF1-IHYz-BBORXF4ZXObym5v9oWty_SwkdragH7QtmW0hgC_HhPVPpla0UoVefZrLbshZSG2YWoWP3YuCRMo43vcZSE6mmaQzOfJ4cWwBu2ZOUTHlFzCkfiLpR1SY7OTOLnuipDCM6HAE3t7GPxoQPsYwn0vgOKwgM58axdim6XbbsbCdphV9JWI2L03jGcqlwZcOsiIWr9w9RU1NUOPMtptcTQeD11YCyCPU43lOHC8I4AKmCtnOrN5aUJcFmLaKinJSAxk6jeALlRhTSL4EXHNZ4_nAZgU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
در شش ماهه نخست سال جاری بانک کشاورزی ۶۷ هزار میلیارد ریال تسهیلات قرض‌الحسنه ازدواج و فرزندآوری پرداخت کرد
🔻
بانک کشاورزی در شش ماهه نخست سال جاری، مبلغ ۶۷ هزار و ۳۸۱ میلیارد ریال تسهیلات قرض‌الحسنه ازدواج و فرزندآوری به متقاضیان واجد شرایط پرداخت کرد.
🔻
شعب این بانک در سراسر کشور با هدف تحکیم بنیان خانواده و حمایت از جوانی جمعیت، از ابتدای سال جاری تا پایان شهریورماه، در مجموع ۵۶ هزار و ۲۶۷ میلیارد ریال تسهیلات قرض‌الحسنه ازدواج و ۱۱ هزار و ۱۱۴ میلیارد ریال تسهیلات قرض‌الحسنه فرزندآوری به متقاضیان واجد شرایط پرداخت کرده‌اند.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/465231" target="_blank">📅 11:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/465230" target="_blank">📅 11:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a502f723d.mp4?token=u-Ai_7im6gF98TX7jXZ9UxCDWl53Z1wDVaN7-xVZPgkY_QMYXo19PTBZREHi-Bx_LzvclYOw5WvS7sBPvF6J8auM5VmuT1-HJnKu0plf3Y6cPjbwQvt-THX2RmHedpESm3X2lZy7vSrXdCSkKDSIQ3jCuu19AL_Czkoykgv140xOzzZdAcpDF4CI9-5zIsGrMBq6OefQNobkXeO_ecuO_NFtdwRqOJifUaWHRoRgV326PalgbG7sf1FIbjQKevK4VNvadrquJUCO9_ZI3rW1CxqxuUmbRXM7vZFLyNpdRBgiOXjWS546jmt3QfHjhmetPwOClioCK9_ouggY9nBJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a502f723d.mp4?token=u-Ai_7im6gF98TX7jXZ9UxCDWl53Z1wDVaN7-xVZPgkY_QMYXo19PTBZREHi-Bx_LzvclYOw5WvS7sBPvF6J8auM5VmuT1-HJnKu0plf3Y6cPjbwQvt-THX2RmHedpESm3X2lZy7vSrXdCSkKDSIQ3jCuu19AL_Czkoykgv140xOzzZdAcpDF4CI9-5zIsGrMBq6OefQNobkXeO_ecuO_NFtdwRqOJifUaWHRoRgV326PalgbG7sf1FIbjQKevK4VNvadrquJUCO9_ZI3rW1CxqxuUmbRXM7vZFLyNpdRBgiOXjWS546jmt3QfHjhmetPwOClioCK9_ouggY9nBJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۱۱۰ هزار جان‌فدا در بندرعباس  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/farsna/465229" target="_blank">📅 11:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1928c304e1.mp4?token=oy9E8RuHsn-f6mw6bi7V9EPc4rVLsXcRsIAT2R_wErtJ6TslqEh2QU9FhC97ywH9DIdKzdzBHw_3_0CTSJO8hwZAJd0jRTHWyUC7TVki2XZbnGd-ANFVo1cFeFh8inGgkSCKVmr93dVBiJCZLQiH48daS0N-2r8Zymor3cNE-bWUF9ShZscWnkY4frwKZf4KgVr218kLmWnQrIMDJnHksPDV0ZzmGDYwa-ow8vbmkPbXk4OXVV5qhg4mLS_ALp4ndn-6bhQmQypBQQ_eiOjdtp6LzRCFL4MsnzG8MTl1TVDpL6D6FduSdsc_C_29aCh7cQ8jC6GexuKBhKc1qitcgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1928c304e1.mp4?token=oy9E8RuHsn-f6mw6bi7V9EPc4rVLsXcRsIAT2R_wErtJ6TslqEh2QU9FhC97ywH9DIdKzdzBHw_3_0CTSJO8hwZAJd0jRTHWyUC7TVki2XZbnGd-ANFVo1cFeFh8inGgkSCKVmr93dVBiJCZLQiH48daS0N-2r8Zymor3cNE-bWUF9ShZscWnkY4frwKZf4KgVr218kLmWnQrIMDJnHksPDV0ZzmGDYwa-ow8vbmkPbXk4OXVV5qhg4mLS_ALp4ndn-6bhQmQypBQQ_eiOjdtp6LzRCFL4MsnzG8MTl1TVDpL6D6FduSdsc_C_29aCh7cQ8jC6GexuKBhKc1qitcgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: در یک کلام؛ ایران به دورانی که دشمن آرزویش را دارد بازنخواهد گشت
🔹
این مقایسه بین روزهای سابق و روزهای حال باز هم قابل بسط و توضیح است، ولی در یک کلام، بنده به‌عنوان خادم مردم عزیز ایران اعلام می‌کنم که آن روزهای سابق که دشمن ما آرزوی بازگشت…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/farsna/465228" target="_blank">📅 11:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465227">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7719ab050d.mp4?token=gnKItAKv3FN8fWCEhFACtftnC0edmbRWbilLxldHDF36A8zhrLp45YQ_gIU_IAbckfosgCvodGN6qO1jn0Y7xd_Tyf2igNsbLKs5ZCJbhXghJcluaETi1G98_sHdqdVEI4ApWwCupLsZ4oT6zuWtwy9uRWr5hE3DtQRG8WEvsbZp-03FLcrGJ5bk1GSAVTaiZneIiUKig8e_olSke_DycbLzQnB3IC0MzmjdyVxSUnzkCRLK1oC42qXHK7I3NgGKJmFztBLB3Wb0uHhR0zXVsay_KgHIso_Py9DOOu_PRyBJOa2hGsBZJklVkz7YcT2_5bUyVPgylwjRfD4PeaiZGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7719ab050d.mp4?token=gnKItAKv3FN8fWCEhFACtftnC0edmbRWbilLxldHDF36A8zhrLp45YQ_gIU_IAbckfosgCvodGN6qO1jn0Y7xd_Tyf2igNsbLKs5ZCJbhXghJcluaETi1G98_sHdqdVEI4ApWwCupLsZ4oT6zuWtwy9uRWr5hE3DtQRG8WEvsbZp-03FLcrGJ5bk1GSAVTaiZneIiUKig8e_olSke_DycbLzQnB3IC0MzmjdyVxSUnzkCRLK1oC42qXHK7I3NgGKJmFztBLB3Wb0uHhR0zXVsay_KgHIso_Py9DOOu_PRyBJOa2hGsBZJklVkz7YcT2_5bUyVPgylwjRfD4PeaiZGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: اگر درگیری‌ها شکل دیگری پیدا کند، ما هم سلاح‌های جدیدی را به میدان خواهیم آورد
🔹
برای دفاع از خودمان، همیشه در حال طراحی سلاح‌های جدید هستیم، سلاح‌های فعلی‌مان را ارتقا می‌دهیم و به تولید انبوه سلاح‌هایی که بتوانیم با آن‌ها از خودمان دفاع کنیم…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/465227" target="_blank">📅 11:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465226">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dedcbeb03.mp4?token=RjJS7YfZ7W1T3Y3uM-5rNzk80kWrpgXXA0nDXEHTdosta6OdIGNAdzqf0Sw8bk-C5ektaad7cgYuslh8SHAlvUrMqUqDrAompxT8RicX-ga71bDqzW_bq0h3Gl2yXvDk63Oxatt9APKB5eznZfnuXlu7UJGWeG5aTR62DYloWIzXqgXQ_414_4R3jERDBS5Ne1oS1dPupUIM-2yPuBRgehOQmIciVEF46qvHAJ-Z5_4DO7uYo0dl1sPcnz4HHcI2pBUQObgb0tpZWGQs2Z8vmmWUkBwoRpKEgfnnN9dEs3ms_9aKp8OcOwDfj9tFnTfmZwZ8u9SgNkOO1Z2G2fYrAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dedcbeb03.mp4?token=RjJS7YfZ7W1T3Y3uM-5rNzk80kWrpgXXA0nDXEHTdosta6OdIGNAdzqf0Sw8bk-C5ektaad7cgYuslh8SHAlvUrMqUqDrAompxT8RicX-ga71bDqzW_bq0h3Gl2yXvDk63Oxatt9APKB5eznZfnuXlu7UJGWeG5aTR62DYloWIzXqgXQ_414_4R3jERDBS5Ne1oS1dPupUIM-2yPuBRgehOQmIciVEF46qvHAJ-Z5_4DO7uYo0dl1sPcnz4HHcI2pBUQObgb0tpZWGQs2Z8vmmWUkBwoRpKEgfnnN9dEs3ms_9aKp8OcOwDfj9tFnTfmZwZ8u9SgNkOO1Z2G2fYrAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار محبی: سپاه را تروریست اعلام کردند چون مانع غارتگری هیئت حاکمۀ آمریکاست
🔹
وقتی که می‌گوییم مرگبر آمریکا یعنی مرگ بر سیاست قتل و غارت و آدم‌کشی؛ مرگ بر افرادی که این افکار را دارند.
🔹
از مردم آمریکا می‌خواهم از حاکمانشان بپرسند که چرا سپاه را تروریست می‌دانند؟…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/465226" target="_blank">📅 11:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a2e48fa4e.mp4?token=BIv_Pi6WeMJoAPV9pjA-7_CV_aWzJPhm2eIaTFO_sD0YpLYM7y1iy0FnybaZDZFTLrawqic6ePi9AoeKpGaeJfFrDBh4_utkWR5bTCftdWC3sRw_M-F4aSk0IJnNskS3eFPlGgjpXh32YsEISib8o66EI-br7XayzYh4bg0UZPaLiEcqAmWt7J0eCD03dcjvDp6LI3b3jQyx4Ytahot91ahQtewbicMZwaC36mqcimkDBcfrIjbBJDzCwdPt7Xk_NgQdnQjBW64AQFEg-ynGPbUqmjkXjzlo4vFe9vEihwULln0nw5AMY145K5mS7X2x5GG_veieiHqk1SnZshTODA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a2e48fa4e.mp4?token=BIv_Pi6WeMJoAPV9pjA-7_CV_aWzJPhm2eIaTFO_sD0YpLYM7y1iy0FnybaZDZFTLrawqic6ePi9AoeKpGaeJfFrDBh4_utkWR5bTCftdWC3sRw_M-F4aSk0IJnNskS3eFPlGgjpXh32YsEISib8o66EI-br7XayzYh4bg0UZPaLiEcqAmWt7J0eCD03dcjvDp6LI3b3jQyx4Ytahot91ahQtewbicMZwaC36mqcimkDBcfrIjbBJDzCwdPt7Xk_NgQdnQjBW64AQFEg-ynGPbUqmjkXjzlo4vFe9vEihwULln0nw5AMY145K5mS7X2x5GG_veieiHqk1SnZshTODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منظور: امسال ۲۵۰۰ همت کسری بودجه پنهان داریم
🔹
رئیس سابق سازمان برنامه‌وبودجه: از حدود ۶۰۰۰ همت منابع پیش‌بینی‌شده در بودجۀ امسال، حداقل ۲۵۰۰ همت کسری وجود دارد و برآورد می‌شود ۳۵ تا ۴۰ درصد منابع بودجه محقق نشود.
🔹
برای بودجه حدود ۱۰۰۰ همت اوراق پیش‌بینی شده، در حالی که این رقم در بودجه ۱۴۰۳ حدود ۲۵۰ همت بوده و طی حدود دو سال حدود ۴ برابر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/465225" target="_blank">📅 10:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b604a918.mp4?token=BKJunaMVA1mICifgrvJ4I1T0ckfvSQHkXaNDPQ7gM-aR6d7j9U-bzTA0jpBLnMBs1EEzDMJnwPEIgpxoZHpk8tHgpfG42-TOILoJeFsYEZzMP0jeNw0v3tdTI4nLTriX9YI_dHdtXnRIhKbg3OO0QKtJCi8G3W2kQleqM4W1WStnk5WEbxUKuQLkAsMM6o5op-ALF-WFjOXbQGsoutNhof3s4h9uPZ-dpr_OMuthEPRN6NOsl6RerXffowuwCmHmKGSJke0G65APW_GufODRDqYzNHq1cNSSzFcA88T63pvrU9ekjIEr7w0riiiXTtiOb9nJ1v4XC3Mfah4vAwBGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b604a918.mp4?token=BKJunaMVA1mICifgrvJ4I1T0ckfvSQHkXaNDPQ7gM-aR6d7j9U-bzTA0jpBLnMBs1EEzDMJnwPEIgpxoZHpk8tHgpfG42-TOILoJeFsYEZzMP0jeNw0v3tdTI4nLTriX9YI_dHdtXnRIhKbg3OO0QKtJCi8G3W2kQleqM4W1WStnk5WEbxUKuQLkAsMM6o5op-ALF-WFjOXbQGsoutNhof3s4h9uPZ-dpr_OMuthEPRN6NOsl6RerXffowuwCmHmKGSJke0G65APW_GufODRDqYzNHq1cNSSzFcA88T63pvrU9ekjIEr7w0riiiXTtiOb9nJ1v4XC3Mfah4vAwBGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاکری: از امروز تا انتخابات آمریکا باید سطح تنش را بالا برد
🔹
مجید شاکری، اقتصاددان: تا زمان انتخابات میان دوره‌ای آمریکا یک گلدن تایم ۳۶ روزه باقی مانده است و جمهوری اسلامی باید سطح تنش را در این ۳۶ روز یا حفظ کند یا بالاتر ببرد.
🔹
تاکید می‌کنم که این افزایش…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/farsna/465224" target="_blank">📅 10:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKDRqt2NyEKDJ29DMWV143qx6uBVPZ2CvJnsjtGl4KpeS15sgaxFQUGn9BT-HaCMXfHjyScR2ZqFp7Tq3EnXOKHtRMXFST7b-tBx7zwttHnQi1JV7I9cavCBnE1vhrJTYjxuSMHg1406nB6-XHOMjg7W7VoR1-LzqgzMfgZarwW4z2oHseykvhdn-BWCpL99dg_KHIQgXhk9zAptsu8FyHsJGMUu9DJT2DhENNDMD-z-XHZB0RSu_7gv7y79ayO7rcxtopAzS5C7hTl29R3WihnSpopI-OzuoAuVMEOPijc-hn_K4Y1rnbh6Q_23bSZI4JICP1sBPAaAfiAdpeKq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سخنگوی سپاه: در نامه به مردم آمریکا حقایق ژئوپولیتیکی را برای آنها روشن کردیم
🔹
ما از مردم آمریکا خواسته‌ایم که این نامه را حداقل یک بار مطالعه کنند. در صورت تمایل به پاسخ، انتقاد یا درخواست توضیحات بیشتر، آمادگی کامل برای مکاتبه داریم و آدرس رسمی جهت این…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/465223" target="_blank">📅 10:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465222">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUsrq8NXP592SVcEhveKrRiBr2wiJOmCXTW1OnxHrdj9JFVEYByzNDUegmJeKXMOuhVxhS40kqXxM1ByXU-gzrsMT0VK8-CBuuk-jyUJZ3Uy1M46oSZpX1X9-B96hl_8ZR73qP1QJdp_QnYxNIodxGtUjjPrxYkhwaeh2li9nkUBUrZ70Q-FO8Mr1jgXSrp_F9_9dDc5d8JdARbLEujDdSPvLi532mvlrcb_hXMnX2nFS-M-7l04GAmq88rntF5jNpSV7zBEsLCZBXDTXFhSxh3yAF-znFYrjgi3fLXgcy5vZ9l7r8zvlWp3BAzNRm2Rf1Ufgus7_sY7BRhZJ4mHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ طرح معیشت شهرداری تهران از امروز آغاز شد
🔹
شهرداری تهران قیمت ۱۲ کالای اساسی از جمله شکر، برنج، قند، روغن و شوینده را برای شهروندان تهران از امروز ثابت نگه می‌دارد و به‌گفتهٔ شهردار تهران، قیمت برخی از کالاها ارزان هم می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/465222" target="_blank">📅 10:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465221">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سخنگوی سپاه: نامۀ خیرخواهانه و دلسوزانه برای مردم آمریکا نوشتیم
🔹
هدف ما از ارسال نامه به مردم آمریکا، فراتر از تبلیغات رسانه‌ای و ایجاد آشنایی با منطق ایران است. این اقدام، یک حرکت تبلیغاتی و کوتاه‌مدت نیست.
🔹
بنیان تشکیل حکومت آمریکا بر مبنای دروغ است. با…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/465221" target="_blank">📅 10:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465220">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MELWtObSV6_ykVVMvvduhqasZIlVaMxtKOgXKMhVCG4j1C4Do3ZjepUZrNSDD8Y98GXScWQ1r5VfbvP21rRZA2DvwiR5nad75I7UpQFQ2l_mmjt1NiERrgxpquS5L-OoN5JhT8lgQ3IWgzn2D-YYxC_6cYzfjJF_O9rdGc48mtRYJ6sfwAVxHyrcGsnLb9rqJe3fZL35oCxeouNd08vn8WRxCppjkFlLgC2c5SE8Lfh_pCBftU8EcP7rMj2PsLSxZyWY_7lYHUeUypNFgoV4BDBhcOnOPd8qcAev5BfDCF_hVxKbKaKJ0ZO94fEJYjepqcxdaLZOalzQjKBErwIdzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سخنگوی سپاه با خبرنگاران خارجی دربارۀ نامۀ مهم سپاه خطاب به مردم آمریکا فردا در تهران برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/465220" target="_blank">📅 10:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0C4Scs-HiVe-Je9Z0vdIL586D-vCE_XDMY-AKy4890CKewjaBUVg_BG56vvrJWH_hdGLZwZzUrxeyWx3Piawz7EXkx0nLjbVVUc3rdbvYriEmZzbX-wJATdPL2T4-P7V9c1JJkqlxaoUhrkXxr7gVmuXwtp2U4nkSKD6IS7NDTvhtC1vEKVHo-1lUbhA-5PEBlj8AXL-i38wfgmqn5mdRLDq6HQ0Z3Yjyr_-Xm7ZcepagXd1NJ8hmeYxgGAMyHtLPxbPziDrMKE_OeMwIDvkFQpx1nCjKrSSpiKsg6wV9b31Hrt3dFKm00L9PEF-d5nHlfTkpnHuMW6Op9maG1VzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندگان از توضیحات خانم وزیر قانع شدند
🔹
در جلسۀ امروز صحن علنی، سوال عبدالجلال ایری در خصوص وضعیت مسکن از وزیر راه‌وشهرسازی مطرح شد که نمایندۀ دهلران قانع نشد و سؤال به رأی گذاشته شد؛ در نهایت نمایندگان از توضیحات فرزانه صادق قانع شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/465219" target="_blank">📅 10:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465218">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c31cedce.mp4?token=IYZpXFUliSKLqMzDAZ7QYcRO1hdV-yjPayelh-YTpDlt9yBVNkZNki2bCpQWZOPx62CX5jHCb1zbh6Bv4pmmEqVw8XKptf4wO1tgtKZZ8_ZVQNwpGPe9xuKeYssuiJVZu5YfetHkkuph1vPdadyat9gNZ4Wi0W8T56LmSqDCphLW-JKMIw3o4UrojXKPXDh6ZctXcgBsGI9K_O93tY0031wOrM0WV5RcsxvAPoytLBnvxlytNq0K3kVVIztG-iQkw0PawEd6FgFr872O_xlMcwWogOIWEerK6b86co42NGegPmBEfU_5ezSQec2_pvCB8CuP54nwtwlPhJb2DsgsNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c31cedce.mp4?token=IYZpXFUliSKLqMzDAZ7QYcRO1hdV-yjPayelh-YTpDlt9yBVNkZNki2bCpQWZOPx62CX5jHCb1zbh6Bv4pmmEqVw8XKptf4wO1tgtKZZ8_ZVQNwpGPe9xuKeYssuiJVZu5YfetHkkuph1vPdadyat9gNZ4Wi0W8T56LmSqDCphLW-JKMIw3o4UrojXKPXDh6ZctXcgBsGI9K_O93tY0031wOrM0WV5RcsxvAPoytLBnvxlytNq0K3kVVIztG-iQkw0PawEd6FgFr872O_xlMcwWogOIWEerK6b86co42NGegPmBEfU_5ezSQec2_pvCB8CuP54nwtwlPhJb2DsgsNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلای نهم برای کاروان ایران
در یک دقیقه ورق را برگرداند
🥇
مجیدوحید بریمانلو در دیدار نهایی وزن ۶۶- کیلوگرم با برتری یک بر صفر مقابل یاسین بوباکالونوف از تاجیکستان به مدال طلا دست یافت و نهمین مدال طلای کاروان ایران را کسب کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/465218" target="_blank">📅 10:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cafd39d87.mp4?token=IlKKOYqfrU013QgGsZ5sj8MSlEzQhFsWoKK6CPW4aGytJTEjW9oquhQ94Rl8bwKaZ2S7GK4OJFnoApkhNUZiJ3Ra3POHyLBXBIVBbhvzM89G0xyiLCC_fSWebP3vIN3qN67vvOEk2iNYx5a6fA78BOEFw2PrYZJo9PTnKZDN1f68NyPSWfLWS2ACp5YgVM4MqUZe-obh55a3NThfLLpDnWMDx2BRXWGeJswHQb0zgOuyczeIOoko5aTwhfIvQIC9uQzKdYz3PpLDcDAhmTqVs8AVydxyv9_Ef3RyPfrBRiQG2zEGo60pyqCbXFIRJHeDtht1GbRRQVGJeu6Yo4aezQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cafd39d87.mp4?token=IlKKOYqfrU013QgGsZ5sj8MSlEzQhFsWoKK6CPW4aGytJTEjW9oquhQ94Rl8bwKaZ2S7GK4OJFnoApkhNUZiJ3Ra3POHyLBXBIVBbhvzM89G0xyiLCC_fSWebP3vIN3qN67vvOEk2iNYx5a6fA78BOEFw2PrYZJo9PTnKZDN1f68NyPSWfLWS2ACp5YgVM4MqUZe-obh55a3NThfLLpDnWMDx2BRXWGeJswHQb0zgOuyczeIOoko5aTwhfIvQIC9uQzKdYz3PpLDcDAhmTqVs8AVydxyv9_Ef3RyPfrBRiQG2zEGo60pyqCbXFIRJHeDtht1GbRRQVGJeu6Yo4aezQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مانتوهای کمیابِ بازار ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/465217" target="_blank">📅 10:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac07bd7731.mp4?token=kUK-ZsIV5jOaE1NJGWYGs2fx4lBSv945tOjnGfQWYYClq5_OfCJf8AgH2Zew2g3Rik6Z3sSxc9GGwifokqaxJvuuQnD-NLh5BsgU6nkotlSLZAgtKEj_7KQJSowxULatDyF276is1QSz6ptWXrz5KWIQliFavSL8ZjagZeQtEpxldl61btUEfza7JyaeeU7b2_yyxEUKwdP9ZLoC9pC_v9w5ZreYWrj5vMWTuAvZzK209gZHaUDDsYvmoVlVm9h17HPkuSBTJX0b08EFFyYgIRnBWKwJpK9T7DNbGju2KtaDViXmMnw2OeCNAPU4HlYqn1gOInqsZEHgSYqfmyIUFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac07bd7731.mp4?token=kUK-ZsIV5jOaE1NJGWYGs2fx4lBSv945tOjnGfQWYYClq5_OfCJf8AgH2Zew2g3Rik6Z3sSxc9GGwifokqaxJvuuQnD-NLh5BsgU6nkotlSLZAgtKEj_7KQJSowxULatDyF276is1QSz6ptWXrz5KWIQliFavSL8ZjagZeQtEpxldl61btUEfza7JyaeeU7b2_yyxEUKwdP9ZLoC9pC_v9w5ZreYWrj5vMWTuAvZzK209gZHaUDDsYvmoVlVm9h17HPkuSBTJX0b08EFFyYgIRnBWKwJpK9T7DNbGju2KtaDViXmMnw2OeCNAPU4HlYqn1gOInqsZEHgSYqfmyIUFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌مجلس: وظیفۀ ما مسئولان، حفاظت بی‌قیدوشرط از معیشت مردم است
🔹
ترمیم قدرت خرید کارگران، کارمندان، بازنشستگان و افزایش اعتبار کالابرگ یک اولویت فوری است.
@Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/465215" target="_blank">📅 10:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd555d2e1.mp4?token=j8Q7_L67Nm1iKmmODZSMHcQ68G_Btt8EyVQxoFlHwsCPhkxTZVaakeD9_EKaxvcOmQqFUGL6nckYrJtLfI_P3OkQtAjfbDzxS1kV4u1F2M3LysZDvgXSsYEEmpqWkyCO6RBxvkzEounnujrHf7WMmVL0wPna4KnGzrhduSYZre07feycmK9bg_Kwgl3thA3hVkG4UrCpnPadP-8L_b72a2-zabzuzS70-2q-m8aYaXHmhyk9pk6cEakUPnyjJHAugP0PJhxYnWa80tundeisau2AMFi9AW0OXr0FrFqTm3rkW2Qz0OSf26fBhv5ZfWp3yC0hJwtB_yJAkEkRSXesRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd555d2e1.mp4?token=j8Q7_L67Nm1iKmmODZSMHcQ68G_Btt8EyVQxoFlHwsCPhkxTZVaakeD9_EKaxvcOmQqFUGL6nckYrJtLfI_P3OkQtAjfbDzxS1kV4u1F2M3LysZDvgXSsYEEmpqWkyCO6RBxvkzEounnujrHf7WMmVL0wPna4KnGzrhduSYZre07feycmK9bg_Kwgl3thA3hVkG4UrCpnPadP-8L_b72a2-zabzuzS70-2q-m8aYaXHmhyk9pk6cEakUPnyjJHAugP0PJhxYnWa80tundeisau2AMFi9AW0OXr0FrFqTm3rkW2Qz0OSf26fBhv5ZfWp3yC0hJwtB_yJAkEkRSXesRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توهین دوبارۀ ترامپ به ایرانی‌ها
🔹
رئیس‌جمهور تروریست آمریکا با تکرار آرزوی خود برای پیروزی سریع در جنگ با ایران، مدعی شد که اگر تهران سلاح هسته‌ای داشت، به اسرائیل، و سپس شهرهای آمریکا حمله می‌کرد.
🔹
ترامپ در ادامۀ ادعاهای بی‌اساس و نخ‌نما‌شده‌اش گفت من جلوی…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/465214" target="_blank">📅 10:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e5f09fee.mp4?token=ZvVDgouTqVMStDbURQiXWfRiSiB8RY7vN89NzRio1s_w6y3p30q0ndPn3o8vSWTOA6qMzlYMptqZvhLvfKzMaATC7eCWR3qFialLZsjxtFJ3U3UnBYRFSjF2ZLA53vUDWZvHoY1i5-CQ5tZutuBOnxe6gNCbGZ9ZaO-e2EvcBqTVPozMqpaDzvqG5bQIK-L9FMzCVIEjqeR9aGrnkEf8nmpXXpUveCOBaiQexz7WYCoVEjtu7p-ywiBC7X7Bt4bMNO9Kofccb3uL6MWWy1reh1cnvbNQ1tYOe-l1FF1RbNRIid88sxBFuJcIhO5yrinzoCvG9LjkASPUSa_zFbvN7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e5f09fee.mp4?token=ZvVDgouTqVMStDbURQiXWfRiSiB8RY7vN89NzRio1s_w6y3p30q0ndPn3o8vSWTOA6qMzlYMptqZvhLvfKzMaATC7eCWR3qFialLZsjxtFJ3U3UnBYRFSjF2ZLA53vUDWZvHoY1i5-CQ5tZutuBOnxe6gNCbGZ9ZaO-e2EvcBqTVPozMqpaDzvqG5bQIK-L9FMzCVIEjqeR9aGrnkEf8nmpXXpUveCOBaiQexz7WYCoVEjtu7p-ywiBC7X7Bt4bMNO9Kofccb3uL6MWWy1reh1cnvbNQ1tYOe-l1FF1RbNRIid88sxBFuJcIhO5yrinzoCvG9LjkASPUSa_zFbvN7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: در یک کلام؛ ایران به دورانی که دشمن آرزویش را دارد بازنخواهد گشت
🔹
این مقایسه بین روزهای سابق و روزهای حال باز هم قابل بسط و توضیح است، ولی در یک کلام، بنده به‌عنوان خادم مردم عزیز ایران اعلام می‌کنم که آن روزهای سابق که دشمن ما آرزوی بازگشت…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/465213" target="_blank">📅 10:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efad563516.mp4?token=R9OtsXlLWiTdi_TEPoG9QJXiEoVcskUOPCizgRsq4lz5o8UiTIt1k2yGaXp3zNqq_Fnll33sXqBL18PLVCAqdcRpOCKbgmyfz9OMGrMZcTjYEKfbFxGcOM2CKhsGQNC613FvC-KLrd7nZJ0Cd37EbqdKDMJkMzroEU5KNiAPslB8VR9ZD5DoClpl9R8Tcz4iWEZQ8FzsXSaEmu97YllTU3w6OYUKnJo3VkIYCI8R3qbaKi24EXztrR6NHe8ENSttL_gcYIDZRzn-g16xdbE-JvvdFNaejtfJN_7_RUGXVsc_u5vDq52YqQnjZBEscni579dUofb6euse8t8ggpx59w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efad563516.mp4?token=R9OtsXlLWiTdi_TEPoG9QJXiEoVcskUOPCizgRsq4lz5o8UiTIt1k2yGaXp3zNqq_Fnll33sXqBL18PLVCAqdcRpOCKbgmyfz9OMGrMZcTjYEKfbFxGcOM2CKhsGQNC613FvC-KLrd7nZJ0Cd37EbqdKDMJkMzroEU5KNiAPslB8VR9ZD5DoClpl9R8Tcz4iWEZQ8FzsXSaEmu97YllTU3w6OYUKnJo3VkIYCI8R3qbaKi24EXztrR6NHe8ENSttL_gcYIDZRzn-g16xdbE-JvvdFNaejtfJN_7_RUGXVsc_u5vDq52YqQnjZBEscni579dUofb6euse8t8ggpx59w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: آمریکا بداند در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت
🔹
رئیس‌جمهور متوهم آمریکا به‌تازگی لفاظی‌هایی دربارۀ تنگۀ هرمز و عبور کشتی‌ها از این تنگه مطرح کرد که تکرار ادعاهای پیشین است و حقیقت این مواضع واهی برای همه شناخته شده است.
🔹
هم آمریکایی‌ها و هم سایر کشورها بدانند: همان‌گونه که قبلا گفته بودیم در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/465212" target="_blank">📅 09:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05caa8272e.mp4?token=FgxJMIBOxCJEbtzcrLVH_mM8lVm6kE-3dXCh3xPt9uxXZb70_IlsibA80AtUcBihoNdTTJBbo-larDt2FsMSiNWoloPCDAAFzcJevfyJBlCMV6f21UFw2PvWHdy8wbQIZhq550TRXjsK7wauYEqeIEODLcBI2Xj9GhcmEEfihnMN-jgvhu9YnnObU1vAXa2mUhyOTQzBwgpPd855FQSYuNvYngGCTNTVy5cAZb4OKfyVm-saPoOzTIhIL6rg4beP9FonSytBPFXj7C1lMsSsI1LVDM5USxdWwXIOE18zh7ygrzO7V4YB0baXrsg8deNydxr83FZFqo0Y7BBpbSEPgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05caa8272e.mp4?token=FgxJMIBOxCJEbtzcrLVH_mM8lVm6kE-3dXCh3xPt9uxXZb70_IlsibA80AtUcBihoNdTTJBbo-larDt2FsMSiNWoloPCDAAFzcJevfyJBlCMV6f21UFw2PvWHdy8wbQIZhq550TRXjsK7wauYEqeIEODLcBI2Xj9GhcmEEfihnMN-jgvhu9YnnObU1vAXa2mUhyOTQzBwgpPd855FQSYuNvYngGCTNTVy5cAZb4OKfyVm-saPoOzTIhIL6rg4beP9FonSytBPFXj7C1lMsSsI1LVDM5USxdWwXIOE18zh7ygrzO7V4YB0baXrsg8deNydxr83FZFqo0Y7BBpbSEPgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌مجلس از شکست حصر آبادان در ۴۸ ساعت
🔹
امروز نیز محاصرۀ دریایی و بستن کریدورهای هوایی با برنامه‌ریزی در حوزه‌های اقتصادی و پاسخ‌های نظامی شکست‌ خواهد خورد.
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/465211" target="_blank">📅 09:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8267e0c2dc.mp4?token=PYQJQPr_zqijurMrxirvhKGPIPiYeghjnMlcC7gLIhsYOw2aknsQUbnrWUiNuN6iBcDR3Z2kP2AxMuoMHRXzBxJWx4TVN9BDffJOkqLPXB8H2jR_U1NcMSuGJc4_Nfn6GfEDxNHCc6pKtT36fJhG_KWnyoJUA42stQbmqM_2i8h-9OB4EszpZJW_TJOcXqcU14gPld8t8GyNwJDD94SnYjmwp_dBKsCjWef2kKLBSiCS4_GRN-CIYs8zsfUVeN-FrgLnDoNOeLUbVtqRU7ol5nrGnoIFZ0erSoUhAcd_alkiPI1GFOJ1idRWPufNqWRPTC-pDMK0ZySrLtolgscfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8267e0c2dc.mp4?token=PYQJQPr_zqijurMrxirvhKGPIPiYeghjnMlcC7gLIhsYOw2aknsQUbnrWUiNuN6iBcDR3Z2kP2AxMuoMHRXzBxJWx4TVN9BDffJOkqLPXB8H2jR_U1NcMSuGJc4_Nfn6GfEDxNHCc6pKtT36fJhG_KWnyoJUA42stQbmqM_2i8h-9OB4EszpZJW_TJOcXqcU14gPld8t8GyNwJDD94SnYjmwp_dBKsCjWef2kKLBSiCS4_GRN-CIYs8zsfUVeN-FrgLnDoNOeLUbVtqRU7ol5nrGnoIFZ0erSoUhAcd_alkiPI1GFOJ1idRWPufNqWRPTC-pDMK0ZySrLtolgscfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: شهید نصرالله حزب‌الله را از یک گروه چریکی به یک نیروی بازدارنده تبدیل کرد
🔹
در دومین سالگرد شهادت شهید سیدحسن نصرالله هستیم. او نه فقط یک فرمانده نظامی یا فقیه دینی، بلکه یک استراتژیست بود که موازنه‌ی قدرت در منطقه را به نفع مستضعفان عالم و نهضت امام خمینی(ره) تغییر داد.
🔹
او حزب‌الله را از یک گروه چریکی به یک نیروی بازدارنده تبدیل کرد که معادلات امنیتی منطقه را باز تعریف نمود. امروز، ساختار مقاومت، با همان انضباط و نگاه راهبردی، تحت هدایت جناب شیخ نعیم قاسم، مسیر خود را سرزنده و با قدرت  ادامه می‌دهد.
🔹
دشمن تصور می‌کرد با حذف فرماندهان، میتواند مقاومت را در لبنان متوقف کند، اما تجربه و نیز تحولات ۲ سال گذشته نشان داد که مقاومت، متکی به فرد نیست؛ بلکه یک ساختار شکل گرفته است که دشمن را در هر سناریویی به بن‌بست کشانده و مستاصل کرده است.
🔹
دشمنان و همۀ مردم دنیا دیدند که خون پاک فرماندهان شهید مقاومت، این جریان را زنده تر و قدرتمند تر نموده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/465210" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465209">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55d0d2b94.mp4?token=ae_tYB6XOEuRuYJoHjGVH06d9YUh9o_nk649lXEoohNeGBckluRqyWP9uMw78Jd22kGZQhR21dKrIl5mCNBd8ucz3RIGPx3kS-ZjP31WxICx7thvcGjTyTqyB1edNuULgnUA3pLDNFKtDIwh12V827UbFpjQT8-GP9K6lUB9Yg5KAGsv2vfFN649DoO8t-IT5TLOhk2u939I4CaoY27o2NYrF4OwH7krRyHZt2tjDjfitEfpp4imZrg8Telhc_nuP5Yn6who96rsstpo1s42_FNXgInfkPm8yu3MlrlVtm8LGb2Gef2KH109sId5gGfbb4yC50WkMWQBHg1PupYYOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55d0d2b94.mp4?token=ae_tYB6XOEuRuYJoHjGVH06d9YUh9o_nk649lXEoohNeGBckluRqyWP9uMw78Jd22kGZQhR21dKrIl5mCNBd8ucz3RIGPx3kS-ZjP31WxICx7thvcGjTyTqyB1edNuULgnUA3pLDNFKtDIwh12V827UbFpjQT8-GP9K6lUB9Yg5KAGsv2vfFN649DoO8t-IT5TLOhk2u939I4CaoY27o2NYrF4OwH7krRyHZt2tjDjfitEfpp4imZrg8Telhc_nuP5Yn6who96rsstpo1s42_FNXgInfkPm8yu3MlrlVtm8LGb2Gef2KH109sId5gGfbb4yC50WkMWQBHg1PupYYOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدردانی رئیس‌مجلس از سربازان جان‌برکف وطن و آتش‌نشانان فداکار که در خط مقدم صیانت از جان و مال مردم ایستاده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/465209" target="_blank">📅 09:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465208">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجار کشتی در تنگه هرمز
🔹
شرکت امنیت دریایی «امبری» اعلام کرد یک کشتی تجاری هنگام عبور از مسیر جنوبی تنگهٔ هرمز، در شمال «خصب» عمان هدف اصابت قرار گرفته و دچار آتش‌سوزی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/465208" target="_blank">📅 09:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465207">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
خبرگزاری رسمی عراق: هواپیمایی عراق پروازهای خود بین نجف و فرودگاه‌های ایران را از سر خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/465207" target="_blank">📅 09:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465206">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lymesHLDQ06Yu5pwxw8kMYZGlIXa197PnOqQiHnvpWm_pX4zKcnSdFw-U__SdH8hptPwTKa53fZNMI0Yae-m3q0wpe0Hvi0jdXEPToz2ESqgYAXhQ3q28eUqXF_IaPEdtcJISEpIaE-I7K9oWEb9krrdKCmzlMysZSchoLu1l1BrYzj4BZTbrolOgUQ0veTT-rQoUyzYsb7_M7GpfaH8vhGZpZQ8kl-DJqgTwCtZVX07Z6NNxIOVNAzG-Or4y97dUV9w8NKfhGggW6CeCZ3oKfjDRf4ZnCaiJ5jpif8XPMDbt5Dtxc_CtZ1LnE3G0KfFZeOxzqKvhRWEzbCOmKo8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای ناو هواپیمابر آمریکا و جراحت ۴ نظامی
🔹
نیروی دریایی آمریکا اعلام کرد ۴ خدمهٔ ناو هواپیمابر «دوایت آیزنهاور» در پی وقوع «یک حادثه در جریان عملیات تعمیر» در نزدیکی سواحل ویرجینیا زخمی شدند.
🔹
مقامات آمریکایی می‌گویند که «این اتفاق حوالی ساعت ۱۸:۱۸ دوشنبه به‌وقت محلی رخ داد و در جریان آن، ۲ خلبان از هواپیمای خود به بیرون پرتاب(اجکت) شدند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/465206" target="_blank">📅 09:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465205">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">۲۷ پاساژ بحرانی تهران در آستانۀ پلمب
🔹
سازمان آتش‌نشانی تهران: بیش از ۹۰ هزار ساختمان ناایمن در تهران شناسایی شده که ۴۷ ساختمان در شرایط بحرانی قرار دارد.
🔹
۲۷ پاساژ بحرانی (خلیج فارس، ساختمان پیروزی، بازارچه سنتی ستارخان، خلیج فارس ۲، مهستان و سرای حاج ولی) روزانه هزاران نفر در آن تردد می‌کنند و ممکن است در کسری از ثانیه بریزند.
🔹
دادستانی اعلام کرده ساختمان‌ها را معرفی کنید کارهای پلمب را انجام می‌دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/465205" target="_blank">📅 09:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465204">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f04ea36e.mp4?token=MfbJ0S2VD71TbA_q7exD07Cg__Jc7Y8wmdHOnisXgZewOsQC1DcTl5VgpO2ujglvIC-lO3dUatUOWv528KGmOTZJhLTyHVJDiDO3dqRL42mLgWrsd2Ehmhx7Qm43W6fiAorge7aq1b-ZJe0yZ3C0EA17QnWpYKWX6DmOUunDEI3SMeUvRrCBQ2DIeN2H2dKgz5d9JL6J0sF1CZpNMC_DTSACH34605fjHGXfMGvSzmDn0VggrckuWdQ0RpEHGiuA07P1Mt_6lQ6UhJUVBo55V7V4eyWEvBjhRg27zXWAqWz_UdT4Pug65VvgpPDSuvWykqjo1fqM0n5-sXB0Zej-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f04ea36e.mp4?token=MfbJ0S2VD71TbA_q7exD07Cg__Jc7Y8wmdHOnisXgZewOsQC1DcTl5VgpO2ujglvIC-lO3dUatUOWv528KGmOTZJhLTyHVJDiDO3dqRL42mLgWrsd2Ehmhx7Qm43W6fiAorge7aq1b-ZJe0yZ3C0EA17QnWpYKWX6DmOUunDEI3SMeUvRrCBQ2DIeN2H2dKgz5d9JL6J0sF1CZpNMC_DTSACH34605fjHGXfMGvSzmDn0VggrckuWdQ0RpEHGiuA07P1Mt_6lQ6UhJUVBo55V7V4eyWEvBjhRg27zXWAqWz_UdT4Pug65VvgpPDSuvWykqjo1fqM0n5-sXB0Zej-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فاطمه برمکی به برنز کوراش بازی‌های آسیایی بسنده کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/465204" target="_blank">📅 08:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465203">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc16f82aaa.mp4?token=r6DgfvQWezcRT7LuDnEERwMDcb_N1i1-ya7QtSNYksnBSan9URHwIvLEN-FYAHrplbSe8_-2u6jfxr7DAO6B7nKRl9FAS8mGfylxqWjDugfrMEaHkTOXAWzUjFxgRrLCAzDC3dpuILCOZex0RMyQ1tcCB5_llfckb9VAJf-8gAET44ISNDW-vEB0pxooq-yOr20KR8jUwSzU-mEQkhZZVhD8fuMK9yHBYLeEJriImRsbp5vIRZltWgEWGyCfOHPbsrHcqPUbieqNL30_t6yvEKg2vtyInU5Ofb5lUapjccCGtpOjBUuKyJO7yZ4gUW84HCokcC6BOCnM7OuvpxRGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc16f82aaa.mp4?token=r6DgfvQWezcRT7LuDnEERwMDcb_N1i1-ya7QtSNYksnBSan9URHwIvLEN-FYAHrplbSe8_-2u6jfxr7DAO6B7nKRl9FAS8mGfylxqWjDugfrMEaHkTOXAWzUjFxgRrLCAzDC3dpuILCOZex0RMyQ1tcCB5_llfckb9VAJf-8gAET44ISNDW-vEB0pxooq-yOr20KR8jUwSzU-mEQkhZZVhD8fuMK9yHBYLeEJriImRsbp5vIRZltWgEWGyCfOHPbsrHcqPUbieqNL30_t6yvEKg2vtyInU5Ofb5lUapjccCGtpOjBUuKyJO7yZ4gUW84HCokcC6BOCnM7OuvpxRGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار نارنجی سیلاب برای شمال کشور
🔹
هواشناسی: روزهای پربارشی در برخی استان‌ها پیش‌رو داریم.
🔹
هشدار سطح نارنجی هواشناسی به‌سبب شدت بارش‌ها برای گیلان، مازندران، گلستان، آذربایجان‌شرقی، غربی و اردبیل صادر شده.
🔹
برای روزهای پایانی هفته، سامانۀ بارش‌زایی از غرب وارد کشور می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/465203" target="_blank">📅 08:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465202">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ce5b3c4c.mp4?token=HId_RtM1UUQQummnWXZtJiBOuRO6uLvNqjkLpOZ96wUA3SynIiJE2LQ0u-Imx7zDy0MN-wWpDwLFwuFDAH2GvgbU1PvEpXQjXWj58Tu-DWZFDeVZIB3DzEQHPiiwYKyETash6UgvzmAjSlGCOkZjXxRH4NSWC3aDr9-jG_5K1BfT2JkyDWVhwZbI6crPm6FBXl7ogmS5K9os_qdE1BVYHZ2fyyq1JYCwbBnbapWldGMry93dsWnvKAPsvTJafAGHKPvPIhp6X8iH_vXVU9zeHtATQgrqaYfTtAcmu4HETdjwO90odxwoyNCRAPEP1Ysh-Y1XSiPKgaQy9rm8S6Zv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ce5b3c4c.mp4?token=HId_RtM1UUQQummnWXZtJiBOuRO6uLvNqjkLpOZ96wUA3SynIiJE2LQ0u-Imx7zDy0MN-wWpDwLFwuFDAH2GvgbU1PvEpXQjXWj58Tu-DWZFDeVZIB3DzEQHPiiwYKyETash6UgvzmAjSlGCOkZjXxRH4NSWC3aDr9-jG_5K1BfT2JkyDWVhwZbI6crPm6FBXl7ogmS5K9os_qdE1BVYHZ2fyyq1JYCwbBnbapWldGMry93dsWnvKAPsvTJafAGHKPvPIhp6X8iH_vXVU9zeHtATQgrqaYfTtAcmu4HETdjwO90odxwoyNCRAPEP1Ysh-Y1XSiPKgaQy9rm8S6Zv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از لحظات کشف پیکر شهید سید حسن نصرالله
🔹
مستند «آن شب» برای نخستین‌بار روایت افرادی را بازگو می‌کند که در جریان جست‌وجو و پیدا کردن پیکر سیدحسن نصرالله حضور داشته‌اند.
📺
مستند کامل را در تلویزیون ببینید:
🔸
امروز ساعت۱۲:۳۰، شبکۀ چهار
🔹
فردا چهارشنبه ساعت ۲۱، شبکۀ مستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/465202" target="_blank">📅 08:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465195">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KisOxsuMJGQ05OkAMD2HysPnnkxkt2X9Is_9T2EUA6hhfxxMmCfifrhTzmmjBsN0rq6Yp5TWaKZDmyW9FtYB9swuBV61rZC1rKCmwQLY0w6bu287zkUwFZ4vcPdVqWwRtg1Plq3or7nd33x7Cw73c7eoScxw3L-QX3bctC8E_ZJdf4ErHr2HQ5FsQKgHyR_eewhfnX4HOhdZ6HZaWHiu2717CFusfHaiQ3B57chQuhPxr50MTZzpj2dZpslQoZ4Eeq_vkuY1HtlUP0hkEI68Xfv9YBjk9tBkGmjXZJ0eNrsyLiuoMP1cYN0Eyl8YeOY3KNgzMIrRXyNC2oNtw0QSjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTKjHrns2aUVP1h0I1eQntQd9iRAo6Abkn6lE2U9G8WUKRi3oyXKPXpUV5FFZ0DuVPZQEZekiTIK2xQPSpd9ifh7TysNi6IfzyLJvzpZETbpZhZrLjydr1Vd6RWGQbMG3t2rNNM8M7ufpOtF8LYgA9KEp_oSSjJmLw3EFur6Jkw2KhInzGR_C9fu6w6ZZZJfEiqgvwoDzA51rJ7TGQuGjwrW1oXvw8htTIH5oV5qqBdKZuYhPxnURh0Bq0-NYzZtD4-7ZzXv5ueaaZlvaikwC_2BuTFR8jehtywz4r6C5MJ_j-Im8RCsi7TCFP9lrpo0h_H8HAxYTwdD69Itaig9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OR9g04gZh4kAF_SR81CbP2O3ENngZkXYAdjWDq1hE9qN64jOU-s_V3hFkHzPsM6XTRToFzTPYZuidQZBMOnEnWf9u1ajqs1ZZn5boKm-VkqnyVz2p134AlWzouRa1cJMdGgbmXguzQPRQVaevTrzor6k6DAP8gfCVauCSzhvach9Vg7ekySwO0iDl7M5AIc2raas5llfp2jvb5GVz2XPeqvpyR_5bHN6cBwm6m6LFhRP8NfG57oADW6WFTyd4OH4DH3aK48IRE5Goe3ikC4mse_K0YitqoDaHb4Z-yYgpv79gEu-0cK9cYdjIqrU6pCB8T2X51gssSVBFJPtbGa2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUDOAQBGM9LHWY-oRKtfauLjlFSao8jw9rqllcoPWUq80UXK5jjMw5aaLxB-UWF4cvClWME2fIBUEwsOEkO-6g5lUvIGO_max2WLX7aPi-4BDTKScnEQy9V6y6QDwzqbpE0EjMpOS1CH00CxSdtJ-TgUIaBeEdvGYNSt6agI33PI_crzAQBb9qjn9HOfcBJg2ujzwzp3TCd3KwDG3wadB-48St_dvPIQLz6vKjXh-m4QowCeXVWYFnZzj32d60eYvuh9DR2b28IyzTnoMfNa5dwxOpEtANqU_i93L4EQZZgchBnothM1ExMSqYgf5vdgg3nalve9biTlmf-kwIRH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZLgieKRIQc8DGQEmNRUgsS9maghGrRlNSuPrsmX0OzezyyJxfZMw1FKX_6djZc6eEAEOlXi_TYfvWClVgGkh1pPJBZSAmfKj7zjm10hihJGfp9N5wEyFIEkg6u_l2k86hij5njIUPOLCanJdnabA9Jr9WayjSpvNd5JQeWH2YVhx309XQ5qQ3gw7qt-Qedlm1OvemMxePW5Uwj0gFeUqpAJKB1kR5wn4EaZr18WD4Eh2Twgu9gW9oLfEhIeFhJ9VObnibqwYaJXgRT_ZHHnEKBtNeNWcO_QIRNDVniWvbegdEmXD5-pO8Q2rNVAeiVLnPhVp6epWts0uaki-sIbvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4OxCdndpLnXlRZ2clfVanaI_PJccF0ZRe_dt_BDAtskZSJlHwjeTumTIDmu9z6gkHUo1QrmJzOTxVK1FZ1GP98RCaW_RWf-D_z8uUMye5644aHwqQfzrj9OTrksm3Osw2ZJjn60XZskB1-7uoXXM_M9Jl9HbImfCDSaY1Om3G4g1_f3pqY6NrwpkdEC7zf0qbL4PqOvhKYoiHOGtuAQ0MgK1mV7jmlKQRyj7OremjkzdL4QJfgHqAxPQWwqNYXdPzIGdCXr9LaXI9aOq_N2rPaMCNjsaS5zK7QfQY4Dnm3BeVP-hyYfbL9XpvXyU1HBUAYXiU_shA3adoogW67vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQQzr3Fw4cU8jgZ6cnQvoyWUNYKTCAs7olfoPgfWhHJNAEZZ34pQ6wrnywTDjM59h8PWHfClQYqkaM3KY2m51oRR4Lb2lLt5lZyzTg-rcryBTT-JfzMxRiEx1y9nq0Y4MpBCfMqfQQw2X3WdKW9MCu5Rm49fBBITsRQXTB4rpIstK3wsJXaz_-QYx1IadUh4vKuLEc0iwfCnEMnPJ1N521hK8CjV9c9aXT6gUVsOdmBRxBTfZ6cBIHrbYCLt-xDKhip0ov_ygcuBFgkjrPq0wINsxR844-N5dmR9GN8KPuW7acNN0VLI6vUNraNk6-Lc1SvXnuiFh-EnR5thvZ-oYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خراطی میراثی زنده در دزفول
عکس :
علی صاحب‌محمدی‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/465195" target="_blank">📅 08:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465194">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39f2d07eb0.mp4?token=QE8JjT4I6CondTwuv3uoXfRoqMtkAFdI8qkK1-rq2ArjjqiEFqcQltI3NvdKTG59FoGiEWxNztaL5LJB9xcC6Ye1-nlrMIGl-_P5F0UlbCEu9VBzK9rQzdcBjk_X4b903TCmBZmFc4DnQ6ykIjQ7zDxqNDMbaviWZmejqs6HU_sYqOhesQkH2hEPuPSHHgdtWg5YJIIdyZ8GeTwsX67ZlUGXXPVUTNRgc3vkyrW9OM-1OdWWf7aF9QOnZQ2baIv2CTjdpa946uLpuJemCvxgldhHW-1ZRWOgfmXKhozOSBJndFEd5ayWHCniMrWkLwBmLhITcLESb_1YsZWx9R2JdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39f2d07eb0.mp4?token=QE8JjT4I6CondTwuv3uoXfRoqMtkAFdI8qkK1-rq2ArjjqiEFqcQltI3NvdKTG59FoGiEWxNztaL5LJB9xcC6Ye1-nlrMIGl-_P5F0UlbCEu9VBzK9rQzdcBjk_X4b903TCmBZmFc4DnQ6ykIjQ7zDxqNDMbaviWZmejqs6HU_sYqOhesQkH2hEPuPSHHgdtWg5YJIIdyZ8GeTwsX67ZlUGXXPVUTNRgc3vkyrW9OM-1OdWWf7aF9QOnZQ2baIv2CTjdpa946uLpuJemCvxgldhHW-1ZRWOgfmXKhozOSBJndFEd5ayWHCniMrWkLwBmLhITcLESb_1YsZWx9R2JdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عینک بزنیم یا نه؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/465194" target="_blank">📅 08:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465193">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پاداش جداگانۀ فدراسیون وزنه‌برداری برای مدال‌آوران ناگویا
🔹
فدراسیون وزنه‌برداری پاداش‌های جداگانه‌ای برای مدال‌آورانش در بازی‌های آسیایی درنظر گرفته است. این پاداش، غیر از پاداش‌هایی است که از طرف وزارت ورزش و کمیتۀ ملی المپیک برای ملی‌پوشان پرداخت می‌شود.
🔸
برای مدال طلا: ۳ میلیارد تومان
🔹
برای مدال نقره: ۱.۵ میلیارد تومان
🔸
برای مدال برنز: ۱ میلیارد تومان
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/465193" target="_blank">📅 08:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465192">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دستگیری سرشبکۀ معاملات کاغذی
🔹
سخنگوی پلیس: سرشبکۀ سابقه‌دار در معاملات فردایی و کاغذی، به‌همراه ۱۰ نفر از مرتبطین دستگیر و ۵ فقره از حساب‌های بانکی اجاره‌ای نیز مسدود گردید.
🔹
بررسی‌های به‌عمل آمده، از گردش مالی ۲۴۰ همتی مجرم رديف اول حکایت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/465192" target="_blank">📅 07:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465191">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۹، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/465191" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465190">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsNkwunlyPEBBJRrrRDbAXxEi3mLexgdSyFvAzndbYLMu8a6rSabpQ_nsYrPwEXGIaQ-RsD_sA-mn4iF8XLbC9hhe4Wg6yxnqZlHevkTbSyTRs4d5SC6KWvXfX4BRCoRjzx-sY7aqRIDU72RdonZHFjm8mwDI_SsYcMbX175BJp1cVEwpAnazkviNPdgl8BbtTg78txa5woUPBUPDKOycOZiI8F6so1sf9hK1VBlITLRJSK_qtnFIIZsh2OaRWSzPygXI7JbllN_f_2_i7IsZMiKIxON3srfMBj0c7fNfbDw3ReDKYSaftiYdKOFcc6mmm2r86dMqoXjaYxDLWAcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال سرانجام به جام لیگ قبلی می‌رسد؟
⚽️
قرار است فدراسیون فوتبال با رای‌گیری بین اعضای هیئت‌رئیسه، تکلیف درخواست استقلال برای دریافت جام لیگ بیست‌وپنجم را مشخص کند.
⚽️
پیش‌بینی از آرای هر کدام از اعضای هیئت‌رئیسه باتوجه به سوابق آن‌ها نشان می‌دهد احتمالا…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/465190" target="_blank">📅 07:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465189">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نمایندۀ ایران در تراپ زنان، از فینال جا ماند
🔹
مرضیه پرورش‌نیا در بخش انفرادی تراپ زنان با کسب ۱۰۸ امتیاز در جایگاه سیزدهم قرار گرفت و تنها با ۲ امتیاز اختلاف از فینال باز ماند.
🔹
فردا او و محمد بیرانوند در تراپ میکس رقابت می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/465189" target="_blank">📅 07:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465188">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صعود دختران پدل‌ ایران به مرحلۀ یک‌ شانزدهم با شکست قطر
🔹
تیم دونفرۀ پدل بانوان ایران با ترکیب صحابه فرد و زهرا کهریزی، با پیروزی مقابل قطر در جریان بازی‌های آسیایی ناگویا ژاپن ۲۰۲۶، جواز حضور در مرحلۀ یک‌شانزدهم نهایی را کسب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/465188" target="_blank">📅 07:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465187">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌ عراقچی: مأموریت ما این بود که شروط خود را به اطلاع طرف آمریکایی و جامعۀ بین‌المللی برسانیم
🔹
شروطی از سمت مقام معظم رهبری وجود دارد و این شروط باید اجرا شود تا تنگۀ هرمز باز شود و مأموریت ما این بود که این شروط را هم به اطلاع طرف آمریکایی برسانیم و هم به…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/465187" target="_blank">📅 07:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465186">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌ ‌عراقچی: مواضع ایران هیچ تغییری نکرده است
🔹
از چندین ساعت قبل ادعاهایی مطرح شده که با قاطعیت عرض می‌کنم که هیچ تغییری در مواضع ایران رخ نداده است.
🔹
شروط ما برای بازگشایی تنگه مشخص است. در خصوص سایر مسائل نیز موضع ما مشخص است.
🔹
درحال حاضر فقط موضوع تنگۀ…</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/465186" target="_blank">📅 07:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
مصاحبۀ عراقچی در پایان سفر به نیویورک
🔸
تلاش کردیم صدای حقانیت و مظلومیت مردم ایران به گوش جهانیان برسد، از منافع مردم ایران دفاع شود و نشان داده شود که ایران همچنان قدرتمند و با اعتمادبه‌نفس در عرصۀ بین‌المللی حضور دارد.
🔸
در ملاقات‌های انجام شده مشهود…</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/465185" target="_blank">📅 07:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465184">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
مصاحبۀ عراقچی در پایان سفر به نیویورک
🔸
تلاش کردیم صدای حقانیت و مظلومیت مردم ایران به گوش جهانیان برسد، از منافع مردم ایران دفاع شود و نشان داده شود که ایران همچنان قدرتمند و با اعتمادبه‌نفس در عرصۀ بین‌المللی حضور دارد.
🔸
در ملاقات‌های انجام شده مشهود بود که جمهوری اسلامی، برخلاف آنچه آمریکا و رژیم صهیونیستی تلاش کردند نشان بدهند، اصلاً منزوی نیست؛ بلکه به‌شدت مورد احترام است.
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/465184" target="_blank">📅 07:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465183">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrFbF-Ttw5kF0pRc9CkGrMyVZsdPQIoDlSoG8eXxaTy9BmKvjEV372AWZeFBbXKL6gu93YylAntuj057Bfixr5nZFvMh7MbA_UAoy6aeFJxQiQCKJxRHVL8UNYJ80giRSgoe_gGLIC-no8QZtPh6SH64JtAzqEET8J0drdxrx5HOXFDy58A1l0NambqpJrYWI_Cb1B9PBeTBeIAd9Ti-ZPn0iNbE3m8IT3B1GKKEeZzPhgtwSK0fKU3fX83FjJrrAuqRElaA762bD7D1gDQF2qGhXYXqUj3nGQVu1mC2IAPd-DJ7bc2uoeh7jPKuka1S-YjpFdlu8kvfXThdb8dY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنوعیت صدور چک رمزدار از ۷ مهر
🔹
بانک‌مرکزی: در راستای حذف چک رمزدار و جایگزینی آن با چک­‌های تضمین شده، صدور چک‌های رمزدار از سه‌شنبه، ۷ مهر ممنوع و همچنین پذیرش (واگذاری) چک‌های رمزدار در سامانه چکاوک از اول دی‌ ممنوع می‌شود.   @Farsna - Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/465183" target="_blank">📅 07:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465182">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG36kOshHfMLu3_8HNeFzIDSJBFInMQgloxB3moaeClT4H0whhq0f2UrTTltPgZzCaI7_9Sh95kdQ_7sv6DbHpSUg_DhC4NIk7Ou6b3cZw41kbkU4GPSEhnuYuV8kejO2xAtq1txMuv657O28Ouc86yGVn6AoeFAgc8zLwaWcS7ahlItnKf7_ZRhPqjoChIsyEbRPu3pQs8od0suPZcCVbeRNiWEMIna9vRX5iu2dbpqsYoNpCes19KgPp2tPZQ9MI7gLj_qLrA1vJjCjtOTbMVd5ay77y7HzklkSlIEvG2kzpQ83vfdBBYkkYi-JbZtrgKTSymt0yC5On1LvCQECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدالی که پس از ۵۲ سال دوباره به ایران رسید
🔹
محمدرضا طیبی در بازی‌های آسیایی ناگویا با ایستادن در جایگاه نخست پرتاب وزنه، طلایی شد تا مدال این ماده پس از ۵۲ سال بار دیگر به ایران بازگردد
🔹
طیبی با پرتاب ۲۰.۸۱ متر، بالاتر از تمام رقبای آسیایی خود ایستاد و علاوه بر کسب مدال طلا، رکورد بازی‌های آسیایی را نیز شکست تا قهرمانی او رنگ و بوی تاریخی پیدا کند.
🔸
آخرین طلای پرتاب وزنۀ ایران در بازی‌های آسیایی به سال ۱۹۷۴ تهران بازمی‌گشت؛ زمانی که زنده‌یاد جلال کشمیری با رکورد ۱۸.۰۴ متر قهرمان این ماده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/465182" target="_blank">📅 06:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465181">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نمایندۀ ایران در تراپ زنان، از فینال جا ماند
🔹
مرضیه پرورش‌نیا در بخش انفرادی تراپ زنان با کسب ۱۰۸ امتیاز در جایگاه سیزدهم قرار گرفت و تنها با ۲ امتیاز اختلاف از فینال باز ماند.
🔹
فردا او و محمد بیرانوند در تراپ میکس رقابت می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/465181" target="_blank">📅 06:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465180">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSaz93dWChihBBcCvBVr6gOgGPn4h-QGf7EZ6gHEeszEEiBBou-Z440JxT0LdxXhNRVRoPXogO2H9SL2LQC1tBD58u1tmRWSWr1UFS-B-r39vNPC-3wwMq8sKaTBBfVH8Q4NPpV_r80CxrznANimd692y0vegIS_X1Vm4wvICsjnd6sfu4BxOWKP9m_Daqkpv0dZrPKzHwW7WdgqKhgpCYarqaXYto-iM9i4wOE7F0X9-w6evw1azP7iW6g-RbjUU4IRy5qSurYXI8kkgQhAGkL5y80OesHx3qkz1hDLnwbd8U2b8TKPJxUSnrrQUyvAtm4IrOX-u_omsZF5W-xKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمل ریلی چین به ایران ۱۰ برابر شد
🔹
ظهوریان، عضو هیئت‌رئیسۀ مجلس از افزایش ۱۰ برابری حمل ریلی کالا از چین به ایران پس از اعمال محاصرۀ دریایی خبر داد و گفت با فعال‌سازی مسیرهای زمینی و ریلی، امکان صادرات روزانه حدود ۴۰۰ هزار بشکه نفت از مسیرهای غیر‌دریایی نیز وجود دارد.
🔹
گفتنی است این رشد با فعال شدن سه مسیر ریلی و افزایش ظرفیت بنادر شمالی ایران رقم خورده است.
🔹
ظهوریان تأکید کرد اگرچه این ظرفیت نمی‌تواند به‌طور کامل جایگزین حمل دریایی شود، اما در شرایط اضطراری می‌تواند به‌عنوان مسیر جایگزین مورد استفاده قرار گیرد و حتی در شرایط عادی نیز به امنیت تجارت خارجی ایران کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/465180" target="_blank">📅 06:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465179">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تیم اسکواش زنان حذف شد
🔹
تیم ملی اسکواش بانوان با نتیجۀ ۳-۰ از هند شکست خورد و حذف شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/465179" target="_blank">📅 05:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465178">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5abdqy0cVyn27hENC6qzpSgVHf9Rk0WCG2gnc9CZtKOORg425PeRId4dxOJJyTgJ1nKPcn0sPTwhqy78_Vsmgfk-y__NC4JRWLtv0nAXy9dWA39DUzuQ-H9y3dhhjXtj-NAJ4qpjNzD3lwnmV0FkKoZ9lJQdQ4HHLYBzs81UMx1pXt4j4JFYplqUK63xFTG9GaQBOlh3j8w-G5ndAkDOD5SQpaeTUFZrbBDeydsf58LGZKkZhRHOqpfP27uGhtzg-S9qGja7ZMi5Vw_VeBo4WZ-G2L2UD5SeP42uiStffYFOu5LhfA75skWUDo3sJEz3gAD5b2A8ulkHxv3hPwZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در والیبال ساحلی میزبان را بردیم و بالا رفتیم
🔹
تیم ملی والیبال ساحلی با ترکیب عباس پورعسگری و علیرضا آقاجانی با شکست ژاپن به جمع ۸ تیم برتر صعود کرد.
🔸
ایران ست اول را ۱۸ بر ۲۱ باخت؛ ست دوم را ۲۱ بر ۱۷ برد و ست سوم را ۱۵ بر ۸ با پیروزی به پایان رساند.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/465178" target="_blank">📅 05:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465177">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049afaff9a.mp4?token=jdqB8Sq4ijO5yp2iXfuUVE3s8wCf3ZJ-tEfj0lTZr9Jeo1j3FktSfSuq8HrJIE2Won8reEDQfOiderzmJimQGc8OgWe6rtRK4lgjleU_FNQEGvExkkB9h1j9VTR5Zti3G-PYPrkUuyt6RNZESdE7uQbNKsVqlg0ZxZn4hrAL8tNlkhVvUKheqv3F2YWvtS9WXIqyUlDadjLckqrjfmGHwoxBgiNx3CPnPf7CIoNSIrnk0iQYoW2ajRpb52ZafBUpOox4s38dB2gOqgWHhmOlaBZ-yG7RXevGALTu8uw2dJUi5IDZsFxgyNAmI9g3ItwhmoeFAfakyhm8iQhULizcOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049afaff9a.mp4?token=jdqB8Sq4ijO5yp2iXfuUVE3s8wCf3ZJ-tEfj0lTZr9Jeo1j3FktSfSuq8HrJIE2Won8reEDQfOiderzmJimQGc8OgWe6rtRK4lgjleU_FNQEGvExkkB9h1j9VTR5Zti3G-PYPrkUuyt6RNZESdE7uQbNKsVqlg0ZxZn4hrAL8tNlkhVvUKheqv3F2YWvtS9WXIqyUlDadjLckqrjfmGHwoxBgiNx3CPnPf7CIoNSIrnk0iQYoW2ajRpb52ZafBUpOox4s38dB2gOqgWHhmOlaBZ-yG7RXevGALTu8uw2dJUi5IDZsFxgyNAmI9g3ItwhmoeFAfakyhm8iQhULizcOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدال برنز برای بانوی وزنه‌بردار ایران
🔹
مهسا بهشتی، دومین وزنه‌بردار زن ایران در این مسابقات، مدال برنز را کسب کرد.
🔹
حریفان او از بحرین، ترکمنستان، مغولستان، ژاپن، چین، قزاقستان و کره جنوبی بودند.
🔹
بهشتی در یک‌ضرب با ۱۱۳ کیلوگرم رتبۀ چهارم را گرفت؛ در دوضرب، تلاش اول با ۱۴۰ کیلوگرم ناموفق بود اما در تلاش دوم با ۱۴۶ کیلوگرم موفق شد. رقیب ترکمنستانی او نتوانست وزنۀ آخر را بلند کند و برنز به بهشتی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/465177" target="_blank">📅 05:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465176">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مدال برنز کوراش‌کار ایران قطعی شد
🔹
در روز سوم رقابت‌های کوراش، فاطمه برمکی در وزن ۸۷+ کیلوگرم، پس از استراحت در دور اول، در یک‌چهارم نهایی با نتیجۀ ۳ بر صفر حریفش از چین تایپه‌ را برد و به نیمه‌نهایی راه یافت.
@Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/465176" target="_blank">📅 05:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465175">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wwq-0isbhYOWRensTCRknkutew5Ky4o7nKuhw5i5ble3oqHWJQKxn-2QmvHedL7E4xDOElmlo1ezSPOGw2Ed6xrfRinQ2N81SAmMSR3cKMV6mZtC9bHHAObV7b5gRdOF6OQa0UjI4LKYyAN8Ek5vuvq6EaHoeljQY5b9IXIjwL7gpapgNePttlr2-QahHtm9ONtH_9iE1A1Y7dcPgwywYoHMYnz3mHgMRbsbF4Ka6WtRmt1fiETCikeFK7F7uS9aayMgWa_sxLunXOuoPeEDE_-VqzBe3jtuAQRpJ_pZNRA_0jc219P6UD7wTF3NGv_xSFuuLvcsROhMRot-dvhSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ غایب بزرگ‌ پرسپولیس در شروع دوبارۀ لیگ
🔹
محمدحسین کنعانی‌زادگان و علی علیپور، دو بازیکن مصدوم پرسپولیس، همچنان در تمرینات گروهی این تیم حضور ندارند و روند درمان و آماده‌سازی خود را به‌صورت اختصاصی دنبال می‌کنند.
🔹
قرار است این دو بازیکن پس از دیدار تدارکاتی پرسپولیس مقابل گل‌گهر سیرجان که روز جمعه برگزار خواهد شد، از هفتۀ آینده تمرینات اختصاصی و کار با توپ را آغاز کنند تا به تدریج به شرایط حضور در تمرینات گروهی برسند.
🔸
سرخپوشان در شروع دوبارۀ مسابقات باید به مصاف نفت آبادان بروند و احتمال غیبت این دو بازیکن در این مسابقه وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/465175" target="_blank">📅 05:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465174">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اطلاعات ۲ میلیون و ۷۶۰ هزار کارمند پنتاگون هک شد
🔹
شبکۀ ای‌بی‌سی‌ نیوز به نقل از یک مقام آمریکایی گزارش داد یک پایگاه دادۀ حساس و جامع دارای اطلاعات ۲ میلیون و ۷۶۰ هزار کارمند پنتاگون هک شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/465174" target="_blank">📅 05:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465173">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a58d04f25.mp4?token=BKwA6mB3SlolFHvhPdpQpHL5GEUuBMFJDvxk6NDJgtcI3GI6fUleF3IbCwb8XMY1Dhb4ooWKG52h9I4fn497AMQoSG4ujy9q2zZEEs_0oDvFOU0i93ugtjQ2veoS_muja46X9INe7CdIkVXNEwTFiJUJH_1QTvPwSXq4rBynvUKcv63xakKKlWUPR2ulY0YVFw5Rsjf0MYtBPaTQt7kLs9_tFPGbCdOb89pObBNHvtKKtiPNhKeYFc0vF8bZB8VcsWBWb1p31j72ObGUBeh_9VV7iDOxUTp4aQ1RlUx9ofQIGNrAzfd9EMTP-n_Gh572muiQcuTjmE8ESZaXuArHNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a58d04f25.mp4?token=BKwA6mB3SlolFHvhPdpQpHL5GEUuBMFJDvxk6NDJgtcI3GI6fUleF3IbCwb8XMY1Dhb4ooWKG52h9I4fn497AMQoSG4ujy9q2zZEEs_0oDvFOU0i93ugtjQ2veoS_muja46X9INe7CdIkVXNEwTFiJUJH_1QTvPwSXq4rBynvUKcv63xakKKlWUPR2ulY0YVFw5Rsjf0MYtBPaTQt7kLs9_tFPGbCdOb89pObBNHvtKKtiPNhKeYFc0vF8bZB8VcsWBWb1p31j72ObGUBeh_9VV7iDOxUTp4aQ1RlUx9ofQIGNrAzfd9EMTP-n_Gh572muiQcuTjmE8ESZaXuArHNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی‌های آسیایی ناگویا
بریمانلو به مرحلۀ یک‌چهارم‌نهایی صعود کرد
🔹
مجید وحید بریمانلو در رقابت‌های کوراش وزن ۶۶- کیلوگرم که با حضور ۱۸ ورزشکار برگزار می‌شود، پس از استراحت در دور نخست، در مرحلۀ یک‌هشتم نهایی با نتیجۀ ۵ بر صفر (یامباش-نصف ضربه فنی) از سد اسلام کامچیبکوف از قرقیزستان عبور کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/465173" target="_blank">📅 05:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465172">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJdAAfNFEBpjIeNVTE_EnR48Z59qPJaDFM8VORJ505gh9dqSKdrg9AWinvaya0zOLz0mAkEMUCYxnSZsd1rZj9wo-z9N6oZptmK9tPe6eqBQG-GXTsM500bQwqTKzzD0hUEdpiZKJIPxtv_uEdzLeJaXtVZ7L0krwrgG4y2NvUBrrdSJzRRwEgY-xV5UxXCB4OVv7KEjUYKcLBYfiSFuu5WXHQaFLRdmVC60XiXspFAmhsahzTKtVE6Bly8sStyHyCVYCRCLIl_GXOqZCEL3xXI3YLB9LjtdFjz8VKtrJBf8aIKMzEZOBu5r8HN3bfE9RNi2cwxX3cblURRJXcKT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی جدی آمریکا از تهدیدهای ایران
🔹
مارکو روبیو وزیر خارجۀ تروریست آمریکا از تهدید جمهوری اسلامی ایران مبنی بر هدف قرار دادن منافع این کشور در سراسر جهان شدیداً ابراز نگرانی کرد.
🔹
روبیو گفت ایران تهدید کرده که به منافع ما در سراسر جهان حمله خواهد کرد و ما این تهدیدها را بسیار جدی می‌گیریم.
🔹
اگر منافع آمریکا مورد حمله قرار گیرد، پیامدهایی خواهد داشت. آنچه آخر هفته در انگلیس اتفاق افتاد، یک تهدید بسیار جدی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/465172" target="_blank">📅 05:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465171">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌ عراقچی خطاب به دبیرکل سازمان ملل: در قبال قانون‌شکنی‌های آمریکا بی‌تفاوت نباشید
🔹
جمهوری اسلامی ایران به‌عنوان یکی از اعضای موسس سازمان ملل، انتظار داشته و دارد که این سازمان و دولت‌های عضو آن در قبال قانون‌شکنی و نقض‌های فاحش منشور از سوی یک عضو دائم شورای…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/465171" target="_blank">📅 04:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465170">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">درخواست گوترش از عراقچی برای ادامۀ مذاکرات
🔹
دبیرکل سازمان ملل در دیدار با عراقچی در نیویورک، خواستار ادامۀ مذاکرات برای دستیابی به صلح شد.
🔹
گوترش از طرفین خواست تا به این تلاش‌ها ادامه دهند و اختلافات باقی‌مانده را از طریق مذاکره برای دستیابی به صلح حل کنند.…</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/465170" target="_blank">📅 04:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465169">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پاداش ۲ فدراسیون واریز شد
🔹
کمیتۀ ملی المپیک دیروز پاداش مدال‌آوران ژیمناستیک و تنیس روی میز بازی‌های آسیایی ناگویا ۲۰۲۶ را واریز کرد.
🔸
در ژیمناستیک، آرمان خدایی و مهدی الفتی با کسب مدال نقره، هر کدام یک میلیارد تومان پاداش دریافت می‌کنند و یک میلیارد تومان نیز سهم کادر فنی است.
🔹
در تنیس روی میز نیز نوشاد عالمیان با کسب مدال برنز انفرادی، ۴۰۰ میلیون تومان پاداش دارد و ۲۰۰ میلیون تومان به کادر فنی اختصاص یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/465169" target="_blank">📅 04:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465168">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شکست پیمانی در گام نخست کوراش
🔹
در رقابت‌های وزن ۸۷+ کیلوگرم بانوان، مریم پیمانی در گام نخست به مصاف حریف مغولستانی رفت و در پایان با نتیجۀ ۵ بر صفر مغلوب حریف خود شد و از دور رقابت‌ها کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/465168" target="_blank">📅 04:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465167">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920a493304.mp4?token=VDvFPhF2z4xH_-1Q0Z1pYdFFuHwWakNbp5HIkycz2HDeoqgpDjG3AIdPbqFmlyhzctO-v1CLoRwBI3BEHP1E_pLlGuR_eff5tm1AtTXE4uj97xUjJd0qwwKEIC40fhNOXZqk4W0NIa_NMnYWc9hwKh6BTCQ-T-Pa3t-jD89PRP9LtyfySQ7T7BYTzSE-tMa2yOF5rRg8-d26v-x0Zkv7-PT1KHOPAU_IqLsC3FD_HqRYlL5lB5A2aaYQVi62VYCKWjc9Nz7pBq8eSVMrzCyrMpOErIENPsalvXHexwNN5fEYoc3Hv3F3KLCTbzwEqo12hYz0f_fSQnHexh6Pe9ZRjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920a493304.mp4?token=VDvFPhF2z4xH_-1Q0Z1pYdFFuHwWakNbp5HIkycz2HDeoqgpDjG3AIdPbqFmlyhzctO-v1CLoRwBI3BEHP1E_pLlGuR_eff5tm1AtTXE4uj97xUjJd0qwwKEIC40fhNOXZqk4W0NIa_NMnYWc9hwKh6BTCQ-T-Pa3t-jD89PRP9LtyfySQ7T7BYTzSE-tMa2yOF5rRg8-d26v-x0Zkv7-PT1KHOPAU_IqLsC3FD_HqRYlL5lB5A2aaYQVi62VYCKWjc9Nz7pBq8eSVMrzCyrMpOErIENPsalvXHexwNN5fEYoc3Hv3F3KLCTbzwEqo12hYz0f_fSQnHexh6Pe9ZRjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کماندار ایرانی از صعود به یک‌چهارم نهایی بازماند
🔹
رضا شبانی، کماندار ایران، در مرحلۀ یک‌هشتم نهایی رقابت‌های ریکرو انفرادی مردان بازی‌های آسیایی آیچی-ناگویا مقابل حریفش از کره‌جنوبی شکست خورد.
🔹
این دیدار با تساوی ۵ بر ۵ به تیر طلایی کشیده شد و در نهایت شبانی با نتیجۀ ۶ بر ۵ مغلوب کماندار کره‌ای شد و از صعود به مرحلۀ یک‌چهارم نهایی بازماند.
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/465167" target="_blank">📅 04:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465166">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7FmtPKlEAV_1g24RZv0AAyry-99T_yV8giPmY26sb2ek4Zrg3flZgEGnxEe2m2Eh2xNDxfWP1wT993de2AkvdR9IP3jiLKGflmvpvT4l8q9yBPkCTzOkIV-23zCqEBMUIVUB9J2swObjpirmvi7nnAfDgETwZ0XDQC0C_cNrM9I-oiMaCnMwJpCW4RxZzdldvjcwuOzWZdj7P8uY9mtxSkIUY_Eg_vwahpBVfE_9lTXXSaLJ9fL3PIkh8DGmkckD7YKweZORnYcIJcKWZfK18H3qU820KkeCci2KG8rAtn2gwGJX9ln2V7MGa5GRQwOW_M2boI_dAg9cdiJ7YR6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست گلشنی‌اصل مقابل کماندار بوتان
🔹
محمدحسین گلشنی‌اصل، نمایندۀ ایران در یک شانزدهم نهایی رقابت‌های ریکرو انفرادی مردان بازی‌های آسیایی ناگویا، مقابل حریف خود از بوتان شکست خورد.
🔹
گلشنی‌اصل در این دیدار با نتیجۀ ۶ بر ۴ مغلوب کماندار بوتان شد و از ادامۀ رقابت‌های انفرادی کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/465166" target="_blank">📅 04:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465165">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnJIHh-bVny_SQSAUTecEw8P3rtzvLE0_GEzRwRdHIincEN6SDLBiKv3V3ShkOdvkRd6FDMdBke4Btm3FhcfaQMc5jYbhwg6-1LJzC11Pa8EwcCrMMlCZn8dgLf_jJ8c8EvhYcz3X5vfGj94QChChSvCzi90IyBJSIWyfqV-vHi3pjXn4UOkSOGKFI1IbPNuBeDvetpk2ruitNMKxkWA3hbWQ_n4zzsM7cCi3FSll0bQXvm8oyrsewCNk7mbXTVecJpY5DPk6ChXltWaVkXloBvglQF6lOxCGWD8dVOndPJQcFK5rTYWdrbbleaDIby_oefEVn9OVJS2co3AyNA9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار روسیه به ناتو دربارۀ احتمال درگیری مستقیم
🔹
سفارت مسکو در بروکسل شامگاه دوشنبه هشدار داد که هرگونه اقدام کشورهای عضو ناتو برای محاصرۀ منطقۀ «کالینینگراد»، خطر درگیری مستقیم با روسیه را در پی دارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/465165" target="_blank">📅 04:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465164">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اختلال دوباره در حریم هوایی عربستان
🔹
رسانه‌های عربی از تعلیق موقت پروازها در فرودگاه بین‌المللی ملک خالد ریاض، در پی حملات نیروهای یمنی خبر داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/465164" target="_blank">📅 04:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/465163" target="_blank">📅 04:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkMa3DhYVfNLrc6VewKQppYbqQ2vd9F7L3ufTJO3njTQ3fM7r9WWGPKMRGhebBYGQQrAXCzC6yh2vhPyG0vPF_5XrfmSqseNl8uyaxzB5udYHJXvUKg9pLT5qvyTtyzWalNB9HnxLeEmv5xh7hJvcs_15b59mLNU51jFtKJ-6rGeSmqJ_2TzUhZMZ5R5Dx-1tzj4u4HGno0a1UvOFfrh-pGW6yPTYBBExp5drXzCNrLRAx-_e6iNyA5kaHfSbLpTt-BPuGxIHOCE50p8TOh0QKqOeRnrBzm9VAN1jw7a7ZzmZmp-m3e2SJHOMko777SncppfX8wwyROYrioNeI0tSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست گوترش از عراقچی برای ادامۀ مذاکرات
🔹
دبیرکل سازمان ملل در دیدار با عراقچی در نیویورک، خواستار ادامۀ مذاکرات برای دستیابی به صلح شد.
🔹
گوترش از طرفین خواست تا به این تلاش‌ها ادامه دهند و اختلافات باقی‌مانده را از طریق مذاکره برای دستیابی به صلح حل کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/465162" target="_blank">📅 03:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-gJXt5S8DCHjpiu6affDWquRO6XWAzPpVFiali7L5pGctbeACbHUZMDWGUWO8DJThrmvsLBrcPLxPo_Cq4JO9dR_5McF6KB5cHx-gScvBCIcduIQinvFvG-2K-cLyqyQPW7oxpttbhoqd_iu7CIm0dt83zEZVxF0xQpi38Dmy4_x2Kw-RXJjaKHeADpPiUQsOw8sC9Xpo97gLxfWe8aYWubmSy4ylu8tYy_aSS2TgL9NI1CrOCf8Iv9ribneWOdR3D9o4SryMigbHgdMpIrmNElP7e3rOBKmKBmxEFYF0NmpzTvnQ91MvrGW1rqAtTsOrMWxJlTYPZuRUbl-PKmjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایزنی وزیر خارجۀ آمریکا با نخست‌وزیر لبنان برای وادار کردن بیروت به سازش
🔹
وزیر خارجۀ آمریکا در دیدار با نخست‌وزیر لبنان که در واشنگتن انجام شد، بر اجرای چارچوب سه‌جانبه با هدف وادار کردن بیروت به سازش با رژیم صهیونیستی تاکید کرد.
🔹
وزارت خارجۀ آمریکا در بیانیه‌ای با اعلام این خبر، گفت روبیو بر تعهد قوی آمریکا برای حمایت از لبنان در اجرای چارچوب سه‌جانبه، که تنها راه برای صلح پایدار بین لبنان و اسرائیل است، تأکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/465161" target="_blank">📅 03:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeZLuayllX5JRRP4-N1kq6TADs04lel5z8e1-BduQgEFQ6M9oUeLX43ZaA6SxUoIl2P_OKJB5n_EtTtDVpz1bIGM_DaTgl2VUEA4ZHGAS3aee9AqK_b1LgC277JBcovSE_Vp-Gb9yOIml2PWtb7-WEmYsvbgebt-6jyF-2NxeosZYOTG5C1xYRUTLPRqNiULqUwS4jz3lRDB9UJhcaNbcLmigc9FzdBu3glurP2mn40dgASmL7LqeXOUFLGvu6EbYpyps80rf1a1UskyX9e1g59Cfz0XharjWTIuqaNK-273iOBA4i7R1V-eokNPLw0vLzDIau5QionTsZQh_ZVFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهین دوبارۀ ترامپ به ایرانی‌ها
🔹
رئیس‌جمهور تروریست آمریکا با تکرار آرزوی خود برای پیروزی سریع در جنگ با ایران، مدعی شد که اگر تهران سلاح هسته‌ای داشت، به اسرائیل، و سپس شهرهای آمریکا حمله می‌کرد.
🔹
ترامپ در ادامۀ ادعاهای بی‌اساس و نخ‌نما‌شده‌اش گفت من جلوی آن اتفاق را گرفتم. اگر می‌خواهید آشوب ببینید، بگذارید آنها یک شهر را با سلاح هسته‌ای نابود کنند.
🔹
وی با توهین مجدد به ایرانی‌ها گفت آن‌ها دیوانه هستند. شکی در آن نیست. همیشه به آن‌ها می‌گویم که شما بسیار دیوانه هستید!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/465160" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brqjOEJG0ioNZPIfvObWf4UUqfRxM6AAHlfbauO4hJ_v-ZrJyEZkDuBaLeXDuevOo32xqwVFWsYM2ow43Dw-hpYII1Nhn54RBh5Bu6fX3c0TpPwaqDWVtwmOtUksCeWatjKRvGH0X16SRarTCL2sAhPPxtKR-H3QwqdLeO2U_M7tDzHi29YDVrQiKPejRGobgsKMOBEFY0lKEJkvMevbbKO3DzsLIK9tV0OW0EJJ5JOC8_JR3dbPuQOAs0iQXusRZktNxvr2Tj_1xhm2i1r6iYH5XCGCGOznqXEdeRmbwpdBa15uJMFBj7etaaF2PRqaVLsQpzPI7Kdxtzd6jOjNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو با دعوت رئیس امارات به این کشور سفر کرده بود
🔸
دفتر نخست‌وزیری رژیم صهیونیستی در بیانیه‌ای گفت که نتانیاهو به دعوت رئیس امارات، به این کشور رفته بود.
🔹
در این بیانیه آمده، این دیدار بر تقویت روابط دوجانبه و چالش‌های منطقه‌ای متمرکز بود. رئیس شورای…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/465159" target="_blank">📅 02:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2d20cccc.mp4?token=TuMAHeStM796Bm179Rbut4mXDoyYVuI6OmK_t5ncDbQmwAdf12oUB8Wy0KpLhfIOuhtI-FrUmR37jwu0gi8TnzmWLxt-JQgkflIaRkOiJ8PgoZJRMJGRH3K626lElxSAbAHjEn6xEoy0mDSmZRBqJI6znODoRH3o608BKk8R6arw8HEFycRtA4hV7mTVUhjE4rRCkONSVOXM__zdCBDK5Xmg1TMxy2svZwcjCT96zw1rht_5lPg_1uo0bgUG2c1ZYhUxb2ZUHOuq8k48h2-GEbugT5tVA_IeP7pTjso37vy0p6DEH8PAs9w14pgMpA6Upn3pvlcCSGflfIVvObwBHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2d20cccc.mp4?token=TuMAHeStM796Bm179Rbut4mXDoyYVuI6OmK_t5ncDbQmwAdf12oUB8Wy0KpLhfIOuhtI-FrUmR37jwu0gi8TnzmWLxt-JQgkflIaRkOiJ8PgoZJRMJGRH3K626lElxSAbAHjEn6xEoy0mDSmZRBqJI6znODoRH3o608BKk8R6arw8HEFycRtA4hV7mTVUhjE4rRCkONSVOXM__zdCBDK5Xmg1TMxy2svZwcjCT96zw1rht_5lPg_1uo0bgUG2c1ZYhUxb2ZUHOuq8k48h2-GEbugT5tVA_IeP7pTjso37vy0p6DEH8PAs9w14pgMpA6Upn3pvlcCSGflfIVvObwBHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی مدعی انفجار یک عامل انتحاری در حلب سوریه شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465158" target="_blank">📅 01:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye_1dScuttBswuvgWCcCUILqmU4qWeii0HdXQGWGS3PNmVGe90C9o9uZfnkcua7yFYxGT0cKBbE6rA76mlcEo_XNnaqC6YSznf3P15auVY6vskYgptmPWjQiVuUlM0ly90e8GJ3_Oy_Gaa2hLb4dkC9amNLkol2120v4QupKT6lsNl4cE_4NXuagj5jRdT1ViX1WMECQBYzjBhMAtO7NCCGV89vpJ0sSh9RAQm3R5dzglG1KB7MPFHyAyu6gjksqQ1eAIAW16tajJmxEL8mxzdmJFGKNNo2kE3KZB3IOo7mG39u-MvomxljkCAHXUb1sL_cQI2gQlhVTKLAisyW0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ گزینه برای سومین بازی تدارکاتی تیم ملی فوتبال
🔹
تیم ملی فوتبال ایران از ساعت ۱۹:۳۰ امروز دومین بازی تدارکاتی خود را پیش از جام ملت‌های ۲۰۲۷ عربستان مقابل روسیه برگزار می‌کند.
🔹
با این وجود طبق اعلام سخنگوی فدراسیون فوتبال، سرپرست فدراسیون در جهت انتخاب سومین حریف شاگردان امیر قلعه‌نویی، به تازگی با فدراسیون ۳ کشور وارد مذاکره شده است.
🔹
قرار است تا ظهر امروز پاسخ نهایی یکی از این ۳ تیم به فدراسیون ارسال شود. محل این بازی احتمالا قطر یا ترکیه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/465157" target="_blank">📅 01:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465156">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvkpYnZ_ZXPGXbSMNVZG_5bvp9SCbesEsPa1KtJtKT2FtX87qK1tEkwSHlZVmUtta_tSxZhWvw7kwMIgWBPkN49K8TAUmgOK5UxxyCGYld5AQm9AyI1UHP7lYZEiwSE_ZtELGIdqDIZ8X3hvoPu9Bw3WfvYEga09mBf4lgXKXtmrIEgoGVuqujYbnojUoYKSHULmE3O9f3YflQKT1T64CL4BxTqVAgOmmSRNxdm0fSY6TJwk_5sivqXUIsnt--_WpQF0EFyT-neUMTpZFe6a3Pq6AOHbcUMCa50dxJ2yHASKL5W7rTGPZUBV4BBgAywdyDeAZgOT5RJRcoNnBEK9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو در سفر به امارات با بن‌زاید دیدار کرد
🔹
شبکه عبری کان: بنیامین نتانیاهو، نخست‌وزیر اسرائیل امروز در بحبوبۀ پرونده افشای هشدار ابوظبی دربارۀ عملیات طوفان الاقصی، سفری به امارات داشته و با محمد بن‌زاید دیدار کرده است. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/465156" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465155">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9RTxNAw0WWvDFrexXqFNOKCt-1c_r16GUHer8htjtlq-JE_pp7gv2mUUhNxrfgvokmo0n70A9VzuzOoE-WYk1U01j7WhdPmMjp0uWDxyAloNEh6z6ozNOHcyyINnqiDwmp_aczewYoWCIryI2naObh2_8XF2RVRKnQiuKgkfdNNvzDrmOCLjecaZI34qJ5CYuWOl8mhgyCIOviulsyTVloWoLo9fmt-L2c4pDmrXhCwtyRA0JMcrlWGABMD4D85UiPEkEK9Tc3_FeucZ9hrH6RVwk_YlEVfUOkxNpU8iBXwxsH0Kt7YUVudLhRsxc57sTLCj0316rlNYoMf_Ef54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس: تا تحقق شروط ایران هیچ اقدام دیگری در مذاکرات نباید انجام شود
🔹
روح‌الله نجابت، نمایندۀ شیراز: ما در مجلس اصرار، تأکید و پافشاری داریم که تا زمانی که شروط جمهوری اسلامی محقق نشده، هیچ اقدام بعدی و دیگری از جانب ما رخ نخواهد داد.
🔹
هرگاه نشانه‌ای از ضعف کشور منعکس شد، دشمن نه‌تنها از اقدامات و خباثت‌های خود دست نکشید، بلکه تهاجم و رفتار تقابلی خود را نیز تشدید کرد.
🔹
پس از این همه جنایت و ظلمی که آمریکا در حق ایران داشته، هر فکر، نگاه و دیدگاهی که تصور کند با کوتاه آمدن می‌توان برای کشور صلح به ارمغان آورد، سخت در اشتباه است.
🔹
آمریکایی‌ها نمی‌توانند با قلدری و حرف‌هایی که بزرگ‌تر از دهانشان است، راه به جایی ببرند. ما سرنوشت، منافع خود و منافع مردم‌مان را خودمان تعیین می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465155" target="_blank">📅 00:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۱</div>
</div>
<a href="https://t.me/farsna/465154" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#روایت_شب
|
سرزمینی که هیچ‌گاه تصورش را نمی‌کنید
قسمت ۱
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465154" target="_blank">📅 00:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk5G-gAKf3HUfUUNqLgyLER8efJeOnx4nkKh4cxzcr9ptOq_zy3qN-9VeBIop1FXXBEjJNAqsbNYZBWTlMByt7brH7TT935HdF_2-96M7NHwWjlIUVo6RA6zw6TjiCT2dcYpIY8eHbcQ0ypWX7JxbLQuGXABs9X2OcH6BdmDRa729n6EMDzNK_l5X7_JvPik92aJX7yg-Hjy1oIAaPFeQmgLsY0jpf37Kt5XjxzQ4bFfq4moYVzrimY2emIT0r3OedRLyKZqNjbXbuF9Kuq6eppq5yb88qNzXfh4kB5vfWNwwNWZRBF6WU69LTFv2yD8mosck7GwxG3wtbUBVBEWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/465153" target="_blank">📅 00:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doEtO3ldut4abs0-vKe4BXrK9zx_NB_6agtEspPu4f0cTPf3jDO-qzMKTuOLqhbB2dZGHHwHhuGlCd8UVmEXGcUuN5Gco4mF4TBmMTumpBQhn-hu1HN5RPiZ8lzGfIADSTvB0Xs-Zz2qlduBVUZT4-Tztom9No49WBeHowRXFnZqZ0HwUijaEFplz4sRe2ZoEJ8RP160JUiUfZ7WL1yUcAVuK6-BVgH4BLTBI7fXpI4tPKrTlZbQebW_u0swZoD7IAiODIPEx5qmtiygNcVOmTI6RErBWJH1G8PYtFU_HG72lhUYVC9H7u0ccLrx8IzTvLstxXSSujIGRS8GkGozzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترفند هوشمندانه برای کشف دزدان خزانه
🔹
روزی جواهر و مروارید فراوانی از خزانهٔ قباد، پادشاه ساسانی، دزدیده شد و هیچ‌کس نتوانست دزد را پیدا کند.
🔹
قباد برای جبران این خسارت و یافتن جواهردزدان، تدبیری اندیشید؛ یکی از شاگردان خزانه‌داری را پنهانی فراخواند و به او دستور داد که کمربند شمشیرِ جواهرنشان را بدون اطلاع بقیه از خزانه خارج کند و در جایی مشخص خاک کند.
🔹
قباد با او قرار گذاشت که: «هرچقدر تو را بازجویی و تهدید کردم، انکار کن و نترس، من هوایت را دارم.» شاگرد دستور را اجرا کرد.
🔹
سپس قباد جشنی برپا کرد و در حضور همه، کمربند شمشیر مرصع را خواست. خزانه‌داران به خزانه دویدند و چون کمربند را نیافتند، باهم درگیر شدند.
🔹
قباد همه را پیش خواند و سراغ کمربند را گرفت. وقتی گفتند گم شده، قباد آن شاگردِ طرفِ قراردادش را متهم کرد و از او کمربند را خواست. شاگرد طبق قرار انکار کرد.
🔹
قباد دستور داد او را پای چوبهٔ دار ببرند تا اعدامش کنند. شاگرد پای دار گفت: «اگر مرا ببخشید، جای کمربند را می‌گویم!» او را نزد قباد آوردند، امان‌نامه گرفت و جای کمربند را نشان داد.
🔹
دزدانِ اصلی خزانه با دیدن این صحنه با خود گفتند: «وقتی پادشاه با هوش و تدبیر خود دزد کمربند را این‌طور دقیق پیدا کرد، حتما دزدیدن جواهرات را هم به‌زودی می‌فهمد؛ پس بهتر است جواهرات را سر جایش برگردانیم!»
🔹
دزدان تمام جواهرات را پنهانی به خزانه بازگرداندند. قباد وقتی دید جواهرات برگشته، آن خزانه‌دارانِ خائن را برکنار کرد و افراد امینی را به‌جایشان گذاشت و با این تدبیر هوشمندانه به هدفش رسید.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465151" target="_blank">📅 00:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8879383c95.mp4?token=JnzPj49ah4VwTKLj08tny6KwaS5hilnlzJvT9Gq1o7iVzhTGXJfTXtwINuEjUhrdvaIijVNkhmYjbDL4FiC-I4TkxEmTepNCdB8zHAc9pQTx2rPPGSarTmtmlL0O2egx8UXsyohTcBrjALt1Ihq-Vrv-3l3bJ96oV5nZG12uO8RnGPv64qGN2R0ehuB1VFVta3qkAg4nSgcHNpDRY-h9iEgyuKUWcWQWCUVdHIz9ZQJo-Ldm7wmSO65n_yhA2HRcVEBFKqf3N5-uZMCybrE6zio0HP5vyH127qtsF-ciemvNjZJoV1QE0V5IjS5VCm_xfH3LyBQx7oANI6Rsk9PSJKvwhgUca_iV6VigVxswwlBADytduKE1YPh5fCYpwFJq88oFRsvV01kJcPrPV-QnP8UQDHJoOy9Vq2vS5VkfSAOl0y4j5tO23C7cfqq40ouv7ragjvSu74OxIrBYkgijwq_VIQpCAVCnqqKRZszV6nZHjW3CRxC9q_fqLV7Bnp5wyIbl0YPVN4lyyxjlShwiRwFwJ_R3v7pI7mS3rdHH77vNTjZXu-zYj_OH5zXuSckXsjd27Cf7fvkqEMWCrLoof7BV_nH171qQdTdWLhXUAIQcFSI90pWxIvPFmP7Xo_w5rwVdzmDnX-ZVp7XEd8a-JwzBfIdRh4uCbTZUQ25FFKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8879383c95.mp4?token=JnzPj49ah4VwTKLj08tny6KwaS5hilnlzJvT9Gq1o7iVzhTGXJfTXtwINuEjUhrdvaIijVNkhmYjbDL4FiC-I4TkxEmTepNCdB8zHAc9pQTx2rPPGSarTmtmlL0O2egx8UXsyohTcBrjALt1Ihq-Vrv-3l3bJ96oV5nZG12uO8RnGPv64qGN2R0ehuB1VFVta3qkAg4nSgcHNpDRY-h9iEgyuKUWcWQWCUVdHIz9ZQJo-Ldm7wmSO65n_yhA2HRcVEBFKqf3N5-uZMCybrE6zio0HP5vyH127qtsF-ciemvNjZJoV1QE0V5IjS5VCm_xfH3LyBQx7oANI6Rsk9PSJKvwhgUca_iV6VigVxswwlBADytduKE1YPh5fCYpwFJq88oFRsvV01kJcPrPV-QnP8UQDHJoOy9Vq2vS5VkfSAOl0y4j5tO23C7cfqq40ouv7ragjvSu74OxIrBYkgijwq_VIQpCAVCnqqKRZszV6nZHjW3CRxC9q_fqLV7Bnp5wyIbl0YPVN4lyyxjlShwiRwFwJ_R3v7pI7mS3rdHH77vNTjZXu-zYj_OH5zXuSckXsjd27Cf7fvkqEMWCrLoof7BV_nH171qQdTdWLhXUAIQcFSI90pWxIvPFmP7Xo_w5rwVdzmDnX-ZVp7XEd8a-JwzBfIdRh4uCbTZUQ25FFKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانباز وطن، پای ضریح امام رضا(ع)
🔹
حسین محمدی، جانباز ایران اسلامی که در روزهای جنگ تحمیلی، پای لانچر، دست و پاهایش را در راه دفاع از سرزمینمان از دست داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/465150" target="_blank">📅 23:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owX4WsqURntvMJiUHlaTOmQQPhaGILl_nQLYODWUTjnMUaOS7O0HmVayuYVbgIRMkBjor2jgxPY_BWrPQu3LG3xXUQ5N6PJb1QHKYUcdj3LRGMEsmi71GXPshp1SaBj7V8kMvEuGHYlCkXCHaWtPdK7hz3sTe9BviCiyVxCI9yac6p15MyG5aaZYGzJsxMvdsHDtSWThgwIG9mWeiLqWF_WWQzdIxKbLWOpkUn9Npxx-Iva0rek4Mr86h79pHcXP8t_gt1D1PdUM1pAnVPje8eLluxxRD0BL5mcuvs4Kvni0jHoB9wdxWKr37Cz5oZq0cqyq2Xe6eM_SpQPQmxFEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق اوراسیا در خدمت بازار روغن
🔹
گمرک ایران بخشی از سهمیهٔ واردات روغن آفتابگردان گلستان را به گیلان منتقل کرد تا محموله‌های روغن در گمرک گیلان معطل نمانند.
🔹
در این جابه‌جایی، سهمیهٔ گلستان از ۱۰ هزار تن به ۲ هزار تن کاهش یافت و ۸ هزار تن از سهمیه باقی‌مانده به گیلان منتقل شد. با این تصمیم، ظرفیت واردات روغن در گیلان از ۱۷۰ هزار تن به ۱۷۸ هزار تن افزایش پیدا کرد.
🔹
هدف این است که واردکنندگان بتوانند محموله‌های خود را با تعرفهٔ ترجیحی تجارت آزاد ایران و اوراسیا ترخیص کنند و واردات روغن با مشکل مواجه نشود.
@Darsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/465149" target="_blank">📅 23:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465148">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ-Mv5Elwjm0wdQkAD3Dk_JrZMUUkcSRIDR4Aw6jUjjfcuHIfW6FRlYymROLDt5jbYa3IsMo-a0LWctVkkDeE9WqceIyVQ6_vGtRLAWz_MJipKLXyeXJ5UmDtSM8kczvnrI5MnhM--y9FP6n7fHsj1Egww6fjLwtPpbpANVg0yS8skV914Vz9YhgKvjDzMgpuvqTXzrKSlFBYloKBxOYzyr_MjTru94nVdaJNVny0u96qIcNTR-c2alrS0KgcYJZUuDCmNNepTKnPXNrjHVbi9OQ1ASX02rEcdBZt5C6myKyR7GsDvuZ0OTPo6_NyFAAtGYZevb-cF51ut9a73UHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کمیسیون امنیت ملی: آمریکایی‌ها قبل از هر مذاکره باید تعهدات خود را اجرا کنند
🔹
سعیدی: تا زمانی که شروط ایران محقق نشود، توافقی در کار نخواهد بود، آمریکا باید ابتدا شروط ایران را بپذیرد و به تعهداتش عمل کند.
🔹
تجربه برجام و مذاکرات اسلام‌آباد نشان داد که نمی‌توان به وعده‌های آمریکا تکیه کرد.
🔹
ایران اهل مذاکره است، اما مذاکره تحت فشار و تهدید را نمی‌پذیرد، گفت‌وگو باید بر پایه احترام متقابل و رعایت مواضع ایران باشد.
🔹
ایران در برابر تهدید و زورگویی کوتاه نخواهد آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/465148" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465147">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8630b43d.mp4?token=FEHLmQsC-e5Fu8VrLwMyodxcgBakTVkK1Gp5Il-_2TMaO7nl888yphjj8J4RbdY4M3pDZkdE-b16Xux673NJqiUX-fCQk0LOrB37xsPtVZ6oAL020kEIDKdrQOOoMVdLyrmr_viNEpVWEvRaBNJYjTonObOsQMR0JeM1B1mGWT7bTt8RTAn-Kce9ImHZLjFryzRDsjWEU7AI-TL7jWDqxwjDU53o9pOOn9dPzKvmietRFC9a7lWPfCi5d0cOeoeFXCJjCdWiFXWDljv3LlGjVzdHZfUIwLcVFFGo0iYGGeL1h8lKZzJqS1E6qA2EBlBVyBl-BErjQ2ELf7950ceQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8630b43d.mp4?token=FEHLmQsC-e5Fu8VrLwMyodxcgBakTVkK1Gp5Il-_2TMaO7nl888yphjj8J4RbdY4M3pDZkdE-b16Xux673NJqiUX-fCQk0LOrB37xsPtVZ6oAL020kEIDKdrQOOoMVdLyrmr_viNEpVWEvRaBNJYjTonObOsQMR0JeM1B1mGWT7bTt8RTAn-Kce9ImHZLjFryzRDsjWEU7AI-TL7jWDqxwjDU53o9pOOn9dPzKvmietRFC9a7lWPfCi5d0cOeoeFXCJjCdWiFXWDljv3LlGjVzdHZfUIwLcVFFGo0iYGGeL1h8lKZzJqS1E6qA2EBlBVyBl-BErjQ2ELf7950ceQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«خادم‌الرضا» عنوانی که آزادکار ایران برای خداحافظی انتخاب کرد
🔹
امیرحسین زارع قهرمانی است که حالا برای پایان مسیرش نه یک رکورد، بلکه یک عنوان را انتخاب کرده است؛ «خادم‌الرضا».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/465147" target="_blank">📅 23:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465146">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8GXudFGTkBKQQ8pSz41PO5PLbBPzyAVTC7WSjnsadYld-P70hrRZkmkA3yd8ZcFPnpja4fDaF2sbtrD0PhLMeXIUi8i8-gOGav284MtS_wO6JKfxhUdInBo4-Ezp6qBPAYwnePUDcUPmVlRnvAN-Acd7LpVb9gUdofkKkE5RZT_SOXQCQ8DMXkxTgSts638RFIIwihSobHUFss19irSH5g0GUyDs4jo_TB3EOXtnA35PYHmgjnUuM7pL4keFOXQN9QjPlVWQQ99BGqxGxRCReLswp02PFeg6GdmewgfEjHaZS1OfisUp6omZ_8btr7IahnVi0C_Ylx5LQ8Rjm08CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی: تا اجرای تعهدات آمریکا در تفاهم اسلام‌آباد، مذاکره‌ای آغاز نمی‌‌شود
🔹
عضو کمیسیون امنیت ملی مجلس: آمریکا باید پیش از آغاز هرگونه مذاکره، به تعهدات خود عمل کند. تا زمانی که ایالات متحده شروط و تعهدات مورد نظر ایران را نپذیرد و اجرا نکند، مذاکره‌ای را آغاز نخواهیم کرد.
🔹
در اسلام‌آباد نیز شاهد بودیم که قرار بود به محض امضای توافق، پول‌های بلوکه‌شده ایران آزاد شود، اما این اتفاق رخ نداد و آمریکا بار دیگر بدعهدی خود را تکرار کرد و نشان داد که نمی‌توان به حرف‌های سیاستمداران آمریکایی اعتماد کرد.
🔹
دیپلمات‌های ایرانی در شرایط فعلی هیچ مجوزی برای انجام مذاکرات دوجانبه یا سه‌جانبه ندارند.
🔹
حتی صحبت از مذاکره هم در شرایط فعلی منطقی نیست چراکه موجب کاهش قیمت نفت و در نتیجه کاهش فشار بر دشمن می‌شود و تاب‌آوری آمریکایی‌ها را برای ادامه فشار و دشمنی با ملت ایران افزایش می‌دهد.
🔹
در شرایطی که ایران با انواع تهدیدها، توهین‌ها و فشارهای آمریکا مواجه است، هرگونه مذاکره پیش از عمل آمریکا به تعهداتش، غیرمنطقی و غیرعقلانی است و با مصوبات و سیاست‌های بالادستی نیز مغایرت دارد.
🔹
انتشار اخبار مربوط به مذاکره عراقچی و ویتکاف باعث نگرانی از شعله‌ورشدن دوباره جنگ شد، چراکه تجربه گذشته نشان داده که هربار پس از مذاکرات عراقچی و ویتکاف، جنگ آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/465146" target="_blank">📅 23:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465145">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8973d873cf.mp4?token=YX8AGrcbhYZG3y8-SnPh3Zzc13d5_YIPRp8734G8wNSaBkxyx4fvHTZtfL0SS8Zls_4qXHqOPvKjQPfdHO8RQ_GbikCYU53LN5PtLzlEDRUj5GXGSEi34BydyRT_Sb6xTbQwSLjYTqKLNhRNq5adAwoghqHRa-YJO8WAP21qhFFAQGDuK_u9oULpx_QGQpls4814qrRWhgt34bkrfX77COO-_JMg58fw4FTgJVh8rzXljk1S9wS-o-NErqRMuyGlebHXBCWi9AKCQtBLJiW3tezLi4WjZ3vbcdhhGD6pOm2JwOc6twV6iqv0renq2nU-klcR1g3rRvWFhrwesVOArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8973d873cf.mp4?token=YX8AGrcbhYZG3y8-SnPh3Zzc13d5_YIPRp8734G8wNSaBkxyx4fvHTZtfL0SS8Zls_4qXHqOPvKjQPfdHO8RQ_GbikCYU53LN5PtLzlEDRUj5GXGSEi34BydyRT_Sb6xTbQwSLjYTqKLNhRNq5adAwoghqHRa-YJO8WAP21qhFFAQGDuK_u9oULpx_QGQpls4814qrRWhgt34bkrfX77COO-_JMg58fw4FTgJVh8rzXljk1S9wS-o-NErqRMuyGlebHXBCWi9AKCQtBLJiW3tezLi4WjZ3vbcdhhGD6pOm2JwOc6twV6iqv0renq2nU-klcR1g3rRvWFhrwesVOArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاریخ‌سازی حافظان سنگر خیابان در الوندِ قزوین ادامه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/465145" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465144">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🎥
۲۱۲ شب پای کار وطن؛ احساس تکلیف کاشمری‌ها تمام‌شدنی نیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/465144" target="_blank">📅 23:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465143">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71c93c333.mp4?token=Ktm3g3c6Cm2hDi31cSWSMz_MOMdHIlz4DEppqJ9SRKpenvLkQswg4L0dDB7moWXZRobPCznTYGvDMOb7GNdRqPAeM00tt3NyyDn955w1najgPjHfDANzETHicPX92rb5jMz4E9-DqHDvy8fgZ0G8BaFnjEztCyjEnva3jF20u796k_YVC_EaEAZGkavy10MkHJOCj4XMHT1i1FFCGWJr_wZnV0faSLQ-vibK3WHEe92v3iudeGIsitncCNdLuDEl1-5o9HD_qU-dnCD4AfUmmn_niYaYxqMvNuGdZFjMlKMLa6jHBw6-mnpdAJwYPEICKwZjD9hJ-5iqcjHnRZi_7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71c93c333.mp4?token=Ktm3g3c6Cm2hDi31cSWSMz_MOMdHIlz4DEppqJ9SRKpenvLkQswg4L0dDB7moWXZRobPCznTYGvDMOb7GNdRqPAeM00tt3NyyDn955w1najgPjHfDANzETHicPX92rb5jMz4E9-DqHDvy8fgZ0G8BaFnjEztCyjEnva3jF20u796k_YVC_EaEAZGkavy10MkHJOCj4XMHT1i1FFCGWJr_wZnV0faSLQ-vibK3WHEe92v3iudeGIsitncCNdLuDEl1-5o9HD_qU-dnCD4AfUmmn_niYaYxqMvNuGdZFjMlKMLa6jHBw6-mnpdAJwYPEICKwZjD9hJ-5iqcjHnRZi_7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضدحال آمریکایی‌ها به زیباکلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/465143" target="_blank">📅 23:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbae476c9a.mp4?token=KbG95ELXsS0uLJsl4ChNLQBhl7F0VxJI4ZU-bts9Z3k4_gTlXE_cTK3HVqccVyUAoSIFANmHX5IEBzFoD4rh9YPFC10vi0EZHNoc6BSsPwYFRisAt6k34srNTu6fpoqEvzzZPtyPTcZTNKDkeimBzavIxBJwQ6LqaZqoasl5f7701szBQCDDPhbrFS8f3Z4c1x1bN9yd3lOdENZdE20pIIBW0-95flUCW_5ab-7eWfQPiQSQeaXz4Jqm0nFAQ0XERS3sbN4e4rB6XRuOb6UJTGPetbEuGH5T45WYI-3U6xFkLFiem-88rcFtFCAuStkSpnqjmlgywkxfjDHMx4VMnn4J3XTZh4kSbr1OQmkxGT6tVIG9KXn8r5bghYefj2vK9UJqL5KL7zbaS8pTXrNkXlcM-VOh2_ylCpFw-gZDIhbYE2IYlRONYt6p15IihL-upSqYbIh-sd7n984_G557cjPk3RAIRy6yBcAqhWNe2bQe1bKr3NWQtpG6syjUP5jGkEuAj6Uv99aM9gX1PSIRhxlC9P2bNxUqiqbzTl8_aKPGKq_XvZdj5flcYb0CoFx0vdXVBVAMYb4WgKmHL_lMJGhwHSUJz0A5nZLBMdztNVhA8uBTxRGJl6S2Wtgz9XXiMUmJQMLxW0eI8hCqEzPlGASQuXhYBGSZ9Bc2b7IFGp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbae476c9a.mp4?token=KbG95ELXsS0uLJsl4ChNLQBhl7F0VxJI4ZU-bts9Z3k4_gTlXE_cTK3HVqccVyUAoSIFANmHX5IEBzFoD4rh9YPFC10vi0EZHNoc6BSsPwYFRisAt6k34srNTu6fpoqEvzzZPtyPTcZTNKDkeimBzavIxBJwQ6LqaZqoasl5f7701szBQCDDPhbrFS8f3Z4c1x1bN9yd3lOdENZdE20pIIBW0-95flUCW_5ab-7eWfQPiQSQeaXz4Jqm0nFAQ0XERS3sbN4e4rB6XRuOb6UJTGPetbEuGH5T45WYI-3U6xFkLFiem-88rcFtFCAuStkSpnqjmlgywkxfjDHMx4VMnn4J3XTZh4kSbr1OQmkxGT6tVIG9KXn8r5bghYefj2vK9UJqL5KL7zbaS8pTXrNkXlcM-VOh2_ylCpFw-gZDIhbYE2IYlRONYt6p15IihL-upSqYbIh-sd7n984_G557cjPk3RAIRy6yBcAqhWNe2bQe1bKr3NWQtpG6syjUP5jGkEuAj6Uv99aM9gX1PSIRhxlC9P2bNxUqiqbzTl8_aKPGKq_XvZdj5flcYb0CoFx0vdXVBVAMYb4WgKmHL_lMJGhwHSUJz0A5nZLBMdztNVhA8uBTxRGJl6S2Wtgz9XXiMUmJQMLxW0eI8hCqEzPlGASQuXhYBGSZ9Bc2b7IFGp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۱۲ میدان‌داری سرخسی‌های خراسان‌رضوی با حضور مهدی سلحشور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/465142" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFl0SwLyzKWb79bqPpbb-I-Zp56l-25QadHoafpgeOBFwPW32NvW-kCr0JdDDWKyxIt4WrZHUkhSKDfdhH_NzfbbHLKmAQq4MeVpa3RzSS6CYAssA6dKBJyKZ2HFygIqnVLcNv-WEjOPOJcqllQO1zi7WH58u9myvrsaywTeEeOV9nfB7_ONSoaxXpG_aDXNNgsfvrHcwjWA588-l6cVwH3OWrLewvAHubM36KWr8y-xq0D9TJjZnEkJf0v6HjRCwA7C_s2iyNsh0jigRDe-L7kMcadhB-s3mTqYXowCsZB8QkaAi6AtwX3EJk8UhxEtY_OEerSKovUZxEZauNy0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس کمیسیون امنیت ملی: پیش از هر مذاکره‌ای، آمریکا باید شروط ایران را بپذیرد
🔹
مقتدایی: اکنون نباید عقربه‌های زمان را به عقب برگردانیم. موضوع هسته‌ای دیگر در کانون یا محور مذاکره نیست، بلکه اکنون تنگه هرمز در محور و کانون قرار دارد.
🔹
آمریکایی‌ها اگر شروط چندگانه ایران را بپذیرند، از این مخمصه خودساخته بیرون خواهند آمد؛ اما اگر نپذیرند، مقاومت ایرانی چون چکشی بر سر دولتمردان آمریکایی فرود خواهد آمد.
🔹
بازگشت به عقب و برگرداندن موضوعات به شرایط پیش از حمله آمریکا، نه عقلانی است و نه منفعت‌زا؛ بلکه می‌تواند آنچه را تاکنون به دست آورده‌ایم نیز تحت‌الشعاع قرار دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/465141" target="_blank">📅 23:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de508afd9d.mp4?token=OyFaCfzURwpM09XsXDOWywt2969K21afU1KTkAOGRmMYmunBRVKwbkJNue8_g2YW98Ky7jAwDcp6REDEHt33AFf-mMEQkU2WOW6p7ueIQQvcw5uV3b3m1I8WirB_NZ_HINPIz3_TVcAmr3wR7RtOWvfEPdPMWT2RFoIEmq7NHFjXB7-ARjgEiHFEe7YXmAgGzxs8biMs5P5p8BwQyuQ9q4421GgYdzOyDc-n22UzYmnD6lQ8n3vhTauTFPT_q7qbOlPxqdBS-i-odAWNSqA7I_1QTKYX5-DYE4_j3wOvErVaj7RJFj2mfhJtQIcnnhBrCt7blwLkl6P4uyAhGnIljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de508afd9d.mp4?token=OyFaCfzURwpM09XsXDOWywt2969K21afU1KTkAOGRmMYmunBRVKwbkJNue8_g2YW98Ky7jAwDcp6REDEHt33AFf-mMEQkU2WOW6p7ueIQQvcw5uV3b3m1I8WirB_NZ_HINPIz3_TVcAmr3wR7RtOWvfEPdPMWT2RFoIEmq7NHFjXB7-ARjgEiHFEe7YXmAgGzxs8biMs5P5p8BwQyuQ9q4421GgYdzOyDc-n22UzYmnD6lQ8n3vhTauTFPT_q7qbOlPxqdBS-i-odAWNSqA7I_1QTKYX5-DYE4_j3wOvErVaj7RJFj2mfhJtQIcnnhBrCt7blwLkl6P4uyAhGnIljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مانتوهایی که به‌سختی در بازار ایران پیدا می‌شوند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/465140" target="_blank">📅 23:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fccd8f7385.mp4?token=JWMyUbfJtcS7e1PpOOqXZ-yxlTYiGRIjBkRnrDZo_DJM1KCnNjd_sJ0Sze82xuXAscAovRlR3zFx9-CWl9b4Ccp1LGAoETGD-fPIC939HTUHHKVFKP-Ml7qgiGmEW4C-NqS2l_xlzHSWtdBWgaNNevXSbNc5nlAAyatsd6J1N9TdQ_SxvExKJZq0gnJ7tgX1RObLtW4-rtvuPx_j8CYkvioHLiN5ZbLxU7NiaXgYzb8aLrnrGA_Z8iRQyXiFYPdjCeQbPRCs_5FiIwflicSweIhaiDAMW_yfTV_5qVyiH86BcJ7LXHM0hT4wb5FGWyvEh3ancvhU85WE4BTVU0LEaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fccd8f7385.mp4?token=JWMyUbfJtcS7e1PpOOqXZ-yxlTYiGRIjBkRnrDZo_DJM1KCnNjd_sJ0Sze82xuXAscAovRlR3zFx9-CWl9b4Ccp1LGAoETGD-fPIC939HTUHHKVFKP-Ml7qgiGmEW4C-NqS2l_xlzHSWtdBWgaNNevXSbNc5nlAAyatsd6J1N9TdQ_SxvExKJZq0gnJ7tgX1RObLtW4-rtvuPx_j8CYkvioHLiN5ZbLxU7NiaXgYzb8aLrnrGA_Z8iRQyXiFYPdjCeQbPRCs_5FiIwflicSweIhaiDAMW_yfTV_5qVyiH86BcJ7LXHM0hT4wb5FGWyvEh3ancvhU85WE4BTVU0LEaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا مردم شهرکرد جانانه پای عهد خود می‌ایستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/465139" target="_blank">📅 23:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTtO7ZBlC6Y3jEgLj3tmcsNV1kSoWs1IkPhZ9QBvilRXh5pfDuHD75wmUI6UyUVl0kYeLYIx7iGX0P1wvU733pysb0ZjekioIIKrmPO73pE5039iDNoVYRinVeFE5VR8Iypr6oFTYRGEwXYPlXBre4jQ6lEMxkvRmCxfIuCuVdj_dpKIzrvODCqj0aikjdASWY_mzlxjLq3dZxMdqqjGO_5BXDXULm_s-I876GQ4GltrSL_893yEXMBZfWFH9P-ViEnmLji9H7IZk5zOGVaAkQG26ujC-Ud_QGT8yJx3Uo8RkSL9SNozV_3DH3LKWKq5XCztpt17Nplnq0woXm3dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروندهٔ غرامت هواپیماهای ایران در انتظار رای لاهه
🔹
رئیس سازمان هواپیمایی کشوری: «در دادگاه لاهه و ایکائو (سازمان هوانوردی بین‌المللی) برای خسارات جنگ شکایت ثبت کردیم. ایکائو حق را به ما داده اما منتظر نتیجهٔ لاهه هستیم.»
🔸
پیشتر وزیر راه‌وشهرسازی گفته بود که حدود ۱۰۰ پرنده ما در جنگ رمضان  آسیب دیدند. ۸ فروند هواپیمای مسافری هم به‌طور کامل منهدم شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/465138" target="_blank">📅 23:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465136">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a090dc8a.mp4?token=gxM05sX9JZceeKjy9lPRn1-CpN3QsVR9Igzv7-MQieKKwBwOb4DUxweG6JzFlecBrm-4fq2DO_UJiFqtc6KWMQ0tH0gmLdLSrpVTSf3Q6e-hCLRTaDskzAgvETDZJG6EBs33b_yOXpBGIlm3SWCkGd37DJ4cOsqM1cAYbkDRhcz0nbMX7Lk6hfdMqOSAKqiSDxM3Yo_FcGvwmSZ7MfNu1y06c1e-AfqJH4O2ce65F3FE22QzoFrjIUgxsEJttxz4mPQ9yRAR7PKL8PW9UiT_erhhVUfYTrIAIIkinmRwnLBpbVeENaszFEmIpfNlDqA7kp9FkMMktbd_w6QbxKh_B5bsPbksOHPQfhEV2H6s3ddH-9Huxp4afOV28l5y6DtaiSY2MMgeuKVO_PEyLIdYmLTaelAG5RMMvPS7L0B_i6qbdnu9LMFAM4cAwkEachr1s0w9RzKXwOxsCbHaeeSuDt1rtKvqCyRQhfkIO_ahBgKDfxJanq-voSSbTUSudZqzeceQGd_CFEwPs9zIX9fwslOtGagpcqCyboplOx7vLAIlhVZr6yqmtOH9hiDKtqShapsLr9Zu7531HqaSdyCyp8j1FH7TGnSpRKVz29dRbyvmZf9BB9IQAHZImQR5tv65IaIZMlz-ZhuGQLn2JwaSFLfCN6zfrGxTs7wrvM49Rmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a090dc8a.mp4?token=gxM05sX9JZceeKjy9lPRn1-CpN3QsVR9Igzv7-MQieKKwBwOb4DUxweG6JzFlecBrm-4fq2DO_UJiFqtc6KWMQ0tH0gmLdLSrpVTSf3Q6e-hCLRTaDskzAgvETDZJG6EBs33b_yOXpBGIlm3SWCkGd37DJ4cOsqM1cAYbkDRhcz0nbMX7Lk6hfdMqOSAKqiSDxM3Yo_FcGvwmSZ7MfNu1y06c1e-AfqJH4O2ce65F3FE22QzoFrjIUgxsEJttxz4mPQ9yRAR7PKL8PW9UiT_erhhVUfYTrIAIIkinmRwnLBpbVeENaszFEmIpfNlDqA7kp9FkMMktbd_w6QbxKh_B5bsPbksOHPQfhEV2H6s3ddH-9Huxp4afOV28l5y6DtaiSY2MMgeuKVO_PEyLIdYmLTaelAG5RMMvPS7L0B_i6qbdnu9LMFAM4cAwkEachr1s0w9RzKXwOxsCbHaeeSuDt1rtKvqCyRQhfkIO_ahBgKDfxJanq-voSSbTUSudZqzeceQGd_CFEwPs9zIX9fwslOtGagpcqCyboplOx7vLAIlhVZr6yqmtOH9hiDKtqShapsLr9Zu7531HqaSdyCyp8j1FH7TGnSpRKVz29dRbyvmZf9BB9IQAHZImQR5tv65IaIZMlz-ZhuGQLn2JwaSFLfCN6zfrGxTs7wrvM49Rmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۲ شب؛ روایت مردمی که خیابان را به میدان ایستادگی تبدیل کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/465136" target="_blank">📅 23:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465135">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در سفر ۶ ساعتهٔ نتانیاهو به امارات چه گذشت
🔹
رسانهٔ صهیونیستی «اسرائیل هیوم» گزارش کرده که سفر دیروز نتانیاهو به امارات ۶ ساعت طول کشیده و در این سفر، رئیس موساد و رئیس شورای امنیت داخلی رژیم صهیونیستی او را همراهی کرده‌اند.
🔹
شبکهٔ‌ صهیونیستی «کان ۱۱» و شبکهٔ…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/465135" target="_blank">📅 23:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465134">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
مقام ایرانی: انعطاف‌پذیری ایران در موضع هسته‌ای نادرست است
🔹
یک مقام آگاه ایرانی به شبکه پرس تی‌وی گفت: «گزارش‌هایی که برخی رسانه‌ها درباره انعطاف‌پذیری ایران در موضع هسته‌ای خود منتشر کرده‌اند، نادرست هستند.»
🔹
این مقام گفت که دولت آمریکا در تنگهٔ هرمز به دام افتاده است و برای منحرف‌کردن توجه از این مشکل، موضوع هسته‌ای را مطرح می‌کند.
🔹
این مقام افزود که موضع ایران در مورد مسئله هسته‌ای تغییر نکرده است و تأکید کرد که هیچ بحثی در این زمینه درحال انجام نیست.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465134" target="_blank">📅 22:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465133">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌همه بازداشت‌شدگان طرح بمب‌گذاری فرفورد، تبعه انگلیس هستند
🔹
پلیس انگلیس اعلام کرد که ۵ مردی که در ارتباط با طرح مشکوک بمب‌گذاری در نزدیکی پایگاه نیروی هوایی سلطنتی فرفورد بازداشت شدند، همگی اهل لندن هستند.
🔸
روز گذشته رسانه‌های انگلیس مدعی شدند پلیس این کشور…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/465133" target="_blank">📅 22:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cde3ac3e9e.mp4?token=fkSuukVPFC5rZdFiYtJN4qj_Mdji-ZEdZb72qontzbMNtmdN-uWv93F-b19aBpYZfnrscjTaYxONljZwFAgbWP3gDOsTutB4nONnjcWq_4IVI87vAan-5P2nQjQLjKK-Gl1FnQeJBtvfPJHp-XAOg4v0dEjYi7SK4h7jHB67grIOQqQqdYvIndX36d8Cfthpxq6nASVZ6NDZOT6OfJ16e_ZQmUWyxgHTO_H0lnXPwfRaecac1J9YtRwqnsb9BZaRCeVjAt-EPMtzJZyh6snTn8QETf4PsDje6wJ9JpCBPG5f40x9bKWFy6bXPvF6kPLn3nAGsZVTymVhcjihsMoGXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cde3ac3e9e.mp4?token=fkSuukVPFC5rZdFiYtJN4qj_Mdji-ZEdZb72qontzbMNtmdN-uWv93F-b19aBpYZfnrscjTaYxONljZwFAgbWP3gDOsTutB4nONnjcWq_4IVI87vAan-5P2nQjQLjKK-Gl1FnQeJBtvfPJHp-XAOg4v0dEjYi7SK4h7jHB67grIOQqQqdYvIndX36d8Cfthpxq6nASVZ6NDZOT6OfJ16e_ZQmUWyxgHTO_H0lnXPwfRaecac1J9YtRwqnsb9BZaRCeVjAt-EPMtzJZyh6snTn8QETf4PsDje6wJ9JpCBPG5f40x9bKWFy6bXPvF6kPLn3nAGsZVTymVhcjihsMoGXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: دشمنان بدانند بحث انتقام ما پابرجاست
🔹
ما باید بالاخره این انتقام را بگیریم؛ در هر جایی یا زمانی. @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/465132" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f11e72571.mp4?token=Cnn7UQtxGxL8y43sY4TpF2a8HzKZ4hJ1uF8qyEz5qFrVvm8amjk-rXVKgMw43RhCbg3yGKtK0N2902qbF_wLlY0QuxaLmaBOERXhbjsadElXIFoQld1n7wtXbta0o67HJI4NDd6i5p4ymy-ksirTZtMuia81U9HZdJ9r5lgig1d4EHebq0lgnZd-DTEXw2FzGz1CSk8-fssK57B4S9Cutzj0j7Gir0PLJqnX-u4BI2WLglLO2Dz12ajpsyPGnm5IrWpuKiTJhBGMXCu2zhTEqXHyhBPpOOxLIKzQ3cVnTwuAVcnjQ_NsmOu7Iqh1_nD0RgvztrQvHyDnWMrRItumbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f11e72571.mp4?token=Cnn7UQtxGxL8y43sY4TpF2a8HzKZ4hJ1uF8qyEz5qFrVvm8amjk-rXVKgMw43RhCbg3yGKtK0N2902qbF_wLlY0QuxaLmaBOERXhbjsadElXIFoQld1n7wtXbta0o67HJI4NDd6i5p4ymy-ksirTZtMuia81U9HZdJ9r5lgig1d4EHebq0lgnZd-DTEXw2FzGz1CSk8-fssK57B4S9Cutzj0j7Gir0PLJqnX-u4BI2WLglLO2Dz12ajpsyPGnm5IrWpuKiTJhBGMXCu2zhTEqXHyhBPpOOxLIKzQ3cVnTwuAVcnjQ_NsmOu7Iqh1_nD0RgvztrQvHyDnWMrRItumbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: هم‌زمان با مصرف سلاح، سلاح تولید می‌کنیم
🔹
هرچقدر موشک و پهپاد شلیک می‌کنم جای آن را به‌سرعت پر می‌کنیم.
🔹
کارخانه تولید پهپاد آرش را زدند اما هنوز درحال تولید است. @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/465131" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465124">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFVMmsuEncGYlkgz-4KJrkgHoHw3JlZ_CWeTbZgnQuJ_1IB1ugUj-dmtVHk2hfIvfs_5UUHxnLdpsvArxrVXfPTVpj0US7YR79FLuShoX_aacLpFP8PBg51JC0oOTp5BG39uG5TROBT641S8ZOo7hJ_lvIAO8xHbPzVh7WpUiNQ75vSRlAgwH53aVBqq0bq3O59_tdADBOH-ZpNyoa1xsS3CS_G8TNsrbCFyjcf00hvjdpdAyTAX2J1HaclBitRVH1uTnmOPVwez1P3qjqvyDyTAMrfzm8xjUu2dqj-yZKQs9SwYVVVLsV1sclWofJHVBSqQu_A1fg2-LFU8_dh8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgzQnmYlK4BT6LzrbDHwvVQnT1E9FGw0E9Lg9K3ec_viNJ0o8-Y2Z86gyKnqeQGby9AanjJ36VVko4XXkPJia0h5145Zc4u5qd6G8PaqnTxj5PHs8NsfLCmDs76HL8WIdNGE2x-sNhc9KUJWRzOmOfh3InI1iJednHnb00kzrpRcteQAAWxlOL94Y-pjPTbzca7NqLXD6eE7iK-YURkoNznmnmTqTDN2pmnfXOAOuHshmwCxu35x-2Bo8ha2eSMCaf5y8QlquEctAIRNqPnQ8ydn70Sp25cOwQDqhDxenZXTtYwQfulMHJOBSsfK7ogIaQ8gbDq5CrpCVXyq8ftvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2D8g7nQTg4Vy9N1WchjC3fMs9nGaEPYmDxEfGaSTopg4APqAsUoLChsBrSjI7DiLlPJ-Rb7OH5JYy16OigBWnTza-j1ausPmhlgnf6--_KZL3FRJIpD5QQAtJA8mLBFJJNgfOXhg6Y5cJ3uUejJmjqUAXE3WmzPw5NAAlmKnR1IVDCqeSUazql2AtDQcGKo-UZ07yLJS4t-cOIjr_UzR32raZKKNxMZzDalVWZed7pDaJouTvPk3_Z2lF2KHWse_fafTLlDoiMt3XSLTEezCw7DDTK4fx__LWZP3dX0YW2Tgn526lH48FgdLTFNNT0gRjIFr-L5vqSvmbwHzMtEFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jV357cnN5AVN2sqiaKBCX8efTdYg09bu_P8a1lVdNTzUj6wSNu7KN-HsZ-qj0KhnRSOJ69CCy2CXmZcHFsetrIG7yReYnMNo53dskv8gHcRINlvdEm4m7ycXyEX1g6oHhX-NW3k6-hdF04THpp-QBiD6QKI02T0wqPSVxiqn2zUi3OBYB51yvJCq1SwAbCHEfzlLMHeFSHKnvmsf-TqljOpW2A0C82AhUm0Or6xTB99xyGFp840huAf9CDdBFJT1vC-9yNT54y3_c5pPMFPRncXeZt0Ztv5ZnTmf2dA0iQRAtmryUmTE94W4ezx4tfjhrRON2Pl7_41vzU8JZFkcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKDAL4cWdnVPhCQG8Hs5eRAxz2WpxrNGP8sLUyVai8rQ0PJp4fDYJTayrJmp4SBN0vP0SBuZi3qits8zVfChdU-yteW1VPy1Up37LudDNwPfIc3CAAQB56Kit2FhBRTDp82MVMVeHoHhOutSzj-1CW81up1xVlUi3mVGfRqzpc7Kfo-D6sF9RXl8z-cICAsK7yDuzCo8xX_ez6eUqe5JiKuKqb_LoyKe8WE3UbnkghTesqmoRqzFFjYUNpewe37ysxK_BR8LygArD4thJL_lyYW1fQdRiwbZjmI-IsoprzrUepIYyW5JT7wxy4eVjx247Eas0GL0fO4oubH9u_0IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmwz1gPt2IrGhTClENwhCJQmwAQtyOXNKH55YDPeRbenlR3p9NI9YOYwJvovl05npUlCoPgKrSrQl8EFL-Wr37emudWKJRP2Rg0NzNWAXW2b7RmZPM6HHHQ3kOVIbbrgeW3P6H9wwWilYIqAlt8r1lBl_ed4TIiPj_j7550bYMZc_dcSm59HRtbEkoWaDPDOp-FAPbYGDIxKHqabvEqgGJcy8R6meXXYRVpHgp_2SFtBaYDxgZfFTQfa1F0I2MNt3ZEE7pzZ9KjFrAz0sUNDamXJ_iFgTuQiSNo64iRi_-3hMCHKci9x3eOjOJ1iRQeTu2WfqwYlP2VXNLnuiOY96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tqs13UzFHRUX3px7MeDYI6lVRlBUhQjDotMjGT1_kUq58AwJ0VLF-XyQfe_dr7C9wfX2IsTCjRgOsDuX6ZEnxUbyH1n3W-GGdGlKuLBD_bwT9bxfEPmO042_ACroaZ10GLywCBP4eHgmaejciQgoDA6vGzFAeMoBKj_lhLwn3ipEzrOm4blvWM7P4u_E6ePQlbqoeIdcd5c-YPULL2cR9-3xmR7rbg5O9BswzS5JDwD1gz73Q9kbdrZo3xDSsGrtmPoJ7Y1zQJWQckJSbfdOWjra3u4JaUufrvnvT1hN4wW3oEmbnu25FXrH7H28DsUYA8HHTiDh1kFvWqEJnJsZ5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زندگی در هرمز جاری است
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/465124" target="_blank">📅 22:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465123">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2e0ab091.mp4?token=iYfe9EGndOJ452m1E-W4w7zQxuGacRQni2v-mcSUYqVI3U54Yz1vCNm_W-9PMlt1d2mIhIvTuDEnqAQmr3FlPrObr3I9ait37hEHnr_lo-zj2NMYhv89XxRgDhhCJ18tu_aCrhwVjxmmOuT27nTjG0IrvY3uTZ6gCXce3Fnu_qdowW_AnKS5naqM6IKdCcdCFRG-LQP939oZA8qHtC362-HjB13iWZU7tfjOfO51yijdIm1GElnVak5_T7bYO9uUhQGzX6951y5BnvMrIwfZeY5vwDZdeYHdn_8VDhXEXmFpTjZ8FBzSKT5vKu1AcGd_aigXfnhOF3W02VPsnEskqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2e0ab091.mp4?token=iYfe9EGndOJ452m1E-W4w7zQxuGacRQni2v-mcSUYqVI3U54Yz1vCNm_W-9PMlt1d2mIhIvTuDEnqAQmr3FlPrObr3I9ait37hEHnr_lo-zj2NMYhv89XxRgDhhCJ18tu_aCrhwVjxmmOuT27nTjG0IrvY3uTZ6gCXce3Fnu_qdowW_AnKS5naqM6IKdCcdCFRG-LQP939oZA8qHtC362-HjB13iWZU7tfjOfO51yijdIm1GElnVak5_T7bYO9uUhQGzX6951y5BnvMrIwfZeY5vwDZdeYHdn_8VDhXEXmFpTjZ8FBzSKT5vKu1AcGd_aigXfnhOF3W02VPsnEskqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرت‌زدن ترامپ این‌بار در جلسۀ کاخ سفید  @Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/465123" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465122">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ReudYK30IXILkZLbs8NjaEHpYXAPRFYPZWB3BIM52jDiVDNlyl3rMkLBS4MvMvGNo7UBQt2_qiZZ6maOxt1kfDxRGA_NfSyGVVtvru7ZSFbBydmdMf3DmHLk-FIHlTcM8nsKPqC2ZXXHrInmXX1NdGvZ_0_0cFxkOAx1rbqgaDLBUXVIk0vpBTcU9nf23uR-NY9vidHFAGF9YSFqqL_QwyQ7CM70pj4fsVHKHYdx5qUo6VHT8Sc4m30Vd-Z5KsQ4OcnbpxeNTNTd_edpw6vCk7Snw-pmi2PZC9ePbWStk2thFds12zUxGk90C29hfm22RvEJ7LIQAAVtLhqYzlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان جنگ بر سر مادرشوهر!
🔹
کشوری، مشاور خانواده می‌گوید: یکی از پرتکرارترین دغدغه‌های زوج‌های جوان، به‌ویژه در سال‌های آغازین پیوند مشترک، تشخیص مرز میان وابستگی ناسالم همسر به خانوادهٔ پدری و احترام و محبت شایسته به والدین است.
اگر همسرتان این ۳ ویژگی را دارد، خیالتان راحت!
🔸
مهارت نه گفتن
🔸
اولویت‌بندی و مسئولیت‌پذیری
🔸
مرزبندی شفاف در عین صمیمیت
🔹
شخصیت سالم در گام اول، خود را در قدرت تصمیم‌گیری مستقل نمایان می‌کند. فردی دارای استقلال شخصیتی است که بتواند در مسائل کلیدی زندگی نظیر انتخاب شغل، محل سکونت و مسائل خرد و کلان، بدون دنباله‌روی کورکورانه یا وابستگی فکری به دیگران، نظر خود را ابراز کند.
🖼
اما هر رسیدگی به والدین را باید وابستگی ناسالم دانست؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/465122" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465121">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89c6541e1.mp4?token=oxnpIIvyaSaaLQi9xBpyFdNAF6182qKEVuhvC-6HzTrLJ4qKOcoTblrfy-0e7INW2soati7gjJHkIZl1KTW8jmy7k-3sX3s_waWHWoN17Vn8x5kR6qx636IuAvFc7gXe_h0ldtk5cQekhrDor1nbVA4OHkV-4h7az3gjJx9r2v9FHk17M4gT6jgLuIj5y9Tj3Otv-51JwBf4VJpHqnguCfNRyKLWgn-KrcmexNE2c4UkPQsX_nRtr8ypKcu0ZJsDhW2_GwtCRsUDQiDoV3G-KszvxBhoE8ISBbTIn_-t6XlUYqopDEYJ4MUTUyNuL0MI-Mh3bfkLr3qOvBWGAuBi6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89c6541e1.mp4?token=oxnpIIvyaSaaLQi9xBpyFdNAF6182qKEVuhvC-6HzTrLJ4qKOcoTblrfy-0e7INW2soati7gjJHkIZl1KTW8jmy7k-3sX3s_waWHWoN17Vn8x5kR6qx636IuAvFc7gXe_h0ldtk5cQekhrDor1nbVA4OHkV-4h7az3gjJx9r2v9FHk17M4gT6jgLuIj5y9Tj3Otv-51JwBf4VJpHqnguCfNRyKLWgn-KrcmexNE2c4UkPQsX_nRtr8ypKcu0ZJsDhW2_GwtCRsUDQiDoV3G-KszvxBhoE8ISBbTIn_-t6XlUYqopDEYJ4MUTUyNuL0MI-Mh3bfkLr3qOvBWGAuBi6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: حاضرم با همین جوانان فعلی به جنگ بروم و حتی نتیجۀ بهتری از دفاع مقدس ۸ ساله بگیرم  @Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/465121" target="_blank">📅 22:39 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
