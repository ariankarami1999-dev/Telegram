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
<img src="https://cdn4.telesco.pe/file/Y_jSktuvsFhV0Kx2gy3l4stVQEtXuc8U1nJmK_n39L0iiCM6OkECDfhbjd8duQfzEutHONwagdvlGRaIVy6Kyb7PZcARhiQuPTUoIgc8ntH3_Sc9xA6f_zhlkZk0ginDi8HgcccLT595iRDylLUbQpuhUh9GNHF_hpNmRK6JOkpryD91GH6-OdgvxXh2iAcg5gSrPOfe-7zoG1Ku70mapjApS84Z6VmjI49rgtvVClX_AUvAYTiVL0GNPwKDI5JZ-8A9lRIgvpJWuigcuOlgZOmL4Hh1JnT9Ue9N-oM0aUq60uH5d6XLlXh8tTYxVa8x0vcnlV1jNutsYPOkaEk6vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 14:32:04</div>
<hr>

<div class="tg-post" id="msg-125519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سفیر چین در تهران: همه طرف ها باید به حقوق مشروع ایران در تنگه هرمز احترام بگذارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/125519" target="_blank">📅 14:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5580004caa.mp4?token=rLT6CKVHCdt7rS9tf40vZ7yVyL2Fl0Ucl9tEjjmkak9te3-4xqOOOxSNM-N-Sy0XdaOSykrHhOzH9Xtk5S3EojTVqYNWyx7hOzrkPbsqSatUHykBKW35O3XiEOmvsuIUnrTcJyzlPmd032ulP3LNNlp7ljCPi9NPm1APso0CBfBFevEIXDd_VpQqLkBDdIWZrXp3unL3rmNPm6rboG6UMc__fbHVDl1LDBAp6jGNLntizO8Qn38AYIojBl8kkbjsWaEK2Vv0bGMEsudykv63pnlK-w960HKvKsoHqilxXrqWPo4VoWT7lxzu9ehv3r-tnRjjlrN57QyrpisMvt4xDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5580004caa.mp4?token=rLT6CKVHCdt7rS9tf40vZ7yVyL2Fl0Ucl9tEjjmkak9te3-4xqOOOxSNM-N-Sy0XdaOSykrHhOzH9Xtk5S3EojTVqYNWyx7hOzrkPbsqSatUHykBKW35O3XiEOmvsuIUnrTcJyzlPmd032ulP3LNNlp7ljCPi9NPm1APso0CBfBFevEIXDd_VpQqLkBDdIWZrXp3unL3rmNPm6rboG6UMc__fbHVDl1LDBAp6jGNLntizO8Qn38AYIojBl8kkbjsWaEK2Vv0bGMEsudykv63pnlK-w960HKvKsoHqilxXrqWPo4VoWT7lxzu9ehv3r-tnRjjlrN57QyrpisMvt4xDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی از احتمال بارش باران، رعدوبرق و تگرگ در نوار شمالی کشور خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/125518" target="_blank">📅 14:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/125517" target="_blank">📅 14:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
غریب آبادی: موضوع رفع تحریم‌ها و مباحث مرتبط با مسائل هسته‌ای در مرحله دوم مذاکرات قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/125516" target="_blank">📅 14:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / الجزیره: وزیر کشور پاکستان در سفر به ایران حامل پیامی برای رهبر ایران خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/125515" target="_blank">📅 14:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجارهای کنترل شده در بندرعباس به مدت چهار روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/125514" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxomYn7VVHEnudxlmqsn_n2pNgpHFHuDUKTrcSdt3jGvTQ5MCcJIyYb1OJBRiMFBxrE2F-o429U1bKcpenscHV9cCtcwbelwjQ9tvLtdbxu-TgydarfTlf0ub1AvzYGC47PHSmBvbGOu4LUQS_7b7epOotxzVVkwnmfL6QVYRn1MyIWd2eTOisjRno_B4FpDoQ0qFEVFpwCrqs6QHzl-QoLndEp90WgvUZmxWccbqcO2KasafFjA4z6isQvdxRkckEQEn9_tBthtnjZMt-d2DiTncWnkDzBzpegUd8tvMfXCMxjaD6xqZj-6ZBU1taN0MqVBN8JLwTNWsPF0ZMChFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: نواف سلام، نخست وزیر لبنان با اشاره به اینکه مشکلات مردم جنوب، مشکلات تمام لبنانی ها است، خاطرنشان کرد تا زمانی که این منطقه در معرض تهدید باشد، کشور در ثبات نخواهد بود و دولت از حق لبنان در دفاع از حاکمیت و امنیت خود کوتاه نمی‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/125513" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125512">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دبیر انجمن صنفی شرکت‌های حمل‌ونقل ریلی مسافری: ۳۰ درصد قطعات یدکی قطار وارداتی است و دستمزد نیز حدود ۵۸ درصد بالا رفته که افزایش هزینه‌ها را به دنبال دارد. قیمت بلیت قطار در همه مسیرها ۲۱ درصد افزایش داشته و از فردا اعمال می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/125512" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125509">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999b104f0a.mp4?token=TYUG3K290Yq7GMWouQ3cpeb7OQ9tiiB6MkUlu4KSKQ2u7qR99F4DNVyCjrGTBh5okPJBfdh-tc1tNWckrJMuPqazMRU92-vewARFhcnzpluomz9Vl7qZ5_0cDGynjIWtoCEL9KRJ2iqAtn4BI_Q6EE3AWrO64kDplr2cLgiZgt9AF4-Tu1J_Tqvu30JkqTSgQemUpfeCwXCNvvyIFSx7AmnsypXTDzmQUuIvTZnjNzg8465iESB2ID1IweYNij4dSu57vh-4zycgnLzHDs6sSl_k7vWce0_tA69xHHfHOJ1rqmHq8VT0QzgGWxZWOOAabi5_774QoismcZ_7C8RKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999b104f0a.mp4?token=TYUG3K290Yq7GMWouQ3cpeb7OQ9tiiB6MkUlu4KSKQ2u7qR99F4DNVyCjrGTBh5okPJBfdh-tc1tNWckrJMuPqazMRU92-vewARFhcnzpluomz9Vl7qZ5_0cDGynjIWtoCEL9KRJ2iqAtn4BI_Q6EE3AWrO64kDplr2cLgiZgt9AF4-Tu1J_Tqvu30JkqTSgQemUpfeCwXCNvvyIFSx7AmnsypXTDzmQUuIvTZnjNzg8465iESB2ID1IweYNij4dSu57vh-4zycgnLzHDs6sSl_k7vWce0_tA69xHHfHOJ1rqmHq8VT0QzgGWxZWOOAabi5_774QoismcZ_7C8RKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز هم در سراسر کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن و حتی جمعیت از سه شنبه هم بیشتره.
«خسرو پناه حیا کن، کنکوریو رها کن»
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/125509" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125508">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ697uIi4ilC2JYfY6EVdlZZqn2QrLuXvTrP5Y0jv-CpcjbDGYzYzcIxvffxv6PkN62pPxlO-f-rNgBKWyONZJLhq-nlHMQL0SrvxeVdryxX8TtMMEtahp1ijt6FWsQVNX5cl59J5vYbpj2mSsFu0p0L1FTEQ9Rjk7tcXXBmWblfMc20R9HYU_wLaBP2okjJyWKlAopKkF3FQdRr8yvmFIRPusqrEkhpOdEoxHYQ5Mq83WNEdICAxHdM6vsDY6PvnGAsg3IKjrGEF95EGN-BGyWTDliyhViSRTSnD2_vGNzTnYjPwGUUbNSXch-bqi0bTJruhytcYNPAG9t7W4BreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داخل امارات یه منطقه ای هست که جزو عمانه و داخل اون منطقه یه منطقه دیگه هست که برای اماراته!
🔴
خاورمیانه همینقدر عجیب غریبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/125508" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125507">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c6f0cb3e.mp4?token=vFy9rk8o0z8yUxgUDwopDOIebRQXuiG7oCBPb5VXyY_xv2NooSuUeILn8Vqr6sLjVU6kR9yuIT-8snY3Nqa_IcYv1xZ-28DGmyEMQnYCa5e8qRv9Ei_oBMrH8yaBPk4iMNMay-0KeRLDZ5SMlU0ebWC3UWxlJ-uFiAVSI2c4gQOnesORqaGtIY8M8HBuxJVP_Wft66ywDKF6DAFkI_EVH3VlZRCew953ztvwOMzk2fdtQ8p-oaVXaraDCi_XwRxC-3Zvw-FoOAu3QH_WeHEq2h9EzPwzrreuxL-WmwnpSdf-5S7NMI39bqqMamZS1L3o5OBibNkEUGQJJxdlul7EXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c6f0cb3e.mp4?token=vFy9rk8o0z8yUxgUDwopDOIebRQXuiG7oCBPb5VXyY_xv2NooSuUeILn8Vqr6sLjVU6kR9yuIT-8snY3Nqa_IcYv1xZ-28DGmyEMQnYCa5e8qRv9Ei_oBMrH8yaBPk4iMNMay-0KeRLDZ5SMlU0ebWC3UWxlJ-uFiAVSI2c4gQOnesORqaGtIY8M8HBuxJVP_Wft66ywDKF6DAFkI_EVH3VlZRCew953ztvwOMzk2fdtQ8p-oaVXaraDCi_XwRxC-3Zvw-FoOAu3QH_WeHEq2h9EzPwzrreuxL-WmwnpSdf-5S7NMI39bqqMamZS1L3o5OBibNkEUGQJJxdlul7EXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
«هویت ایرانی» ما بر روح و‌جان ما حک شده! غیر قابل نابودی است!
🔴
ایران بر همه چیز الویت داره.
🤔
قابل توجه عرزشی حرام زاده که از تخم عرب های سوسمار خور عربستانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125507" target="_blank">📅 14:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125506">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=ojM8QB905N1YAKuM27PDIalD_TqwsCx3zWGwAEw4MWCSyq83_9cSUzSNuIHlyiipnBQSRcDcYjsnhThuLuoq2gJTKH-_TlSZKieGKLbThBkQ30LFc2klH75pbaHsUM3kYwFA9-G_db3nlhy-exyaKhVsDm_zXMseofTxWCI7SJK-plMaYLVk4DJWvod_g6nfLmpI9vL0zZvMT4wqYiYar2qJBz8A297e6Bb0HzN9zFr2AwBsQPZ6pIOY_oMbHhXBnpNsriwfmxoHdsGr2IhjdeVieAXENJGvGm1KpUi8aEtM8zvjJkpVnfeK3te7WFK08wsXOlNnkrW207lWcvH74w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=ojM8QB905N1YAKuM27PDIalD_TqwsCx3zWGwAEw4MWCSyq83_9cSUzSNuIHlyiipnBQSRcDcYjsnhThuLuoq2gJTKH-_TlSZKieGKLbThBkQ30LFc2klH75pbaHsUM3kYwFA9-G_db3nlhy-exyaKhVsDm_zXMseofTxWCI7SJK-plMaYLVk4DJWvod_g6nfLmpI9vL0zZvMT4wqYiYar2qJBz8A297e6Bb0HzN9zFr2AwBsQPZ6pIOY_oMbHhXBnpNsriwfmxoHdsGr2IhjdeVieAXENJGvGm1KpUi8aEtM8zvjJkpVnfeK3te7WFK08wsXOlNnkrW207lWcvH74w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: مرکز ناوگان پنجم دریای آمریکا مورد اصابت موشک قرار گرفت؛ نه ببخشید اشتباه شد؛ صدای انفجار در جزیره خارک شنیده شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125506" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125505">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy2fJHcdtrmdCdpkJDn-GuqgBO4b2M_vIx8aPdcBuckOzMrSLDtrpIG7Ur-Pi_PWvRij1FXxoEnXCmZNXD-A9uDKBA9TkhrAKh2HooIyy2sgmyz7t_43cyt7uEUBSL9a7JkAxwqVGX6rd6GWsDZGsn0l5awmeFjBf3P1phZek7goBYnQSj3lTOJXdkr2aWsSPzOTSv8QkAEyzGICuTXqz9mDlgnvSEdnRzxs1zGEZ9p0sDjoGOjBF8ZDswDqCnslztwf2By8jDZuHQ09a7ZehyN0YrbaJtX420j4Ru_PN4C5eGUu1dPOBkYunWjB2P-MS4lJYmT8HQZwbtasW0laKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز پیش گروهی از اتحادیه معلمان مکزیک، ساختمان آموزش پرورش در مکزیکوسیتی را تصرف کردن و خواهان افزایش حقوق شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125505" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125504">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که نیروهای ما بر منطقه «شوچنکو» در اطراف خارکیف تسلط پیدا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125504" target="_blank">📅 14:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125503">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فارس: ۴۱۷ میلیون متر مکعب آب از افغانستان راهی شمال سیستان و بلوچستان شد؛ یعنی کمتر از نصف حقابه ایران که در سال‌های نرمال آبی پرداخت می‌شود
🔴
فارس نوشت: افغانستان یکی از پرباران‌ترین دوره‌های خود در قرن اخیر را پشت سر می‌گذارد اما تاکنون تنها نیمی از حقابه ایران از رودخانه هیرمند پرداخت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125503" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125502">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بحرین: ما مورد حمله ۳ موشک و چندین پهپاد قرار گرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/125502" target="_blank">📅 13:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125501">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وال استریت ژورنال: دادن پول به ایران برای ترامپ خیلی سخت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125501" target="_blank">📅 13:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125500">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: امتحانات پایه‌های یازدهم و دوازدهم نهایی و حضوری برگزار می‌شود
🔴
کاظمی: تلاش می‌کنیم امتحانات از ۱۳ تیر آغاز شود.
🔴
همه ملاحظات لازم برای کاهش نگرانی دانش آموزان و خانواده‌ها رعایت می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125500" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125498">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1v7b6y2yPML-tCXGPsl194EHvJHnkVbidjoOBhX8eT-mLrwgMCoMJLdzzSEHHwJLXM2-vaJZgvUY4IA8PtpGz-NJlGQibHEyMDLlXmntbG19nAlQiOufr1a0xzYtthvKzWPrgrBse7U_zFgzuic70kNJpxW7MF4LtSKjXllwVv5mMdx2U9U184f76i29SeV8Nbls6hVSEA89bkOAxpeaBfwyBonBOoMRcTMjDCR5h1NkkoZhVGuvA4kX-0uzuFmMgZQyXuJPO2AhLhQdV4xwMpqd2MH2L1EesXv93qXAenrk7q5Yu3WMD3IaBDMQOsQN6cDSYNYdtioOqbNmZl7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFwNCLn5PA6RJPiVtTmjWnentoQTBQRyRxtA1sXjgXnD0dT234fMnW70th-MmGTqG84RRZpp2jkOeQh2IHdAkjZRSb-CoV5b6Elfpex8vfLnKgmB_6ZZxcmioiwY4RiaZYVMfkCD4dIRDrCFUzt0DpkaYP-ExAop9ILaJmOGmL4fUjxdMXqNVfZQcapL2fhHcV9LddrBYW80rXG_zYd4V_wXEMjC9DwhXnpmxYGs1rcbdXlJFLJj7SH3LEZ6--1TSyXBIf3o2jQ39rwzwqzYUYZ6a8J3QVVgmT9GR8KnElOv1TW46JIlaRd5bIq7ThWq9AVEdNvKo0Up90ihyefxzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش سوزی منتسب به اطراف پایگاه هوایی استان شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125498" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125497">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/125497" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125496">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125496" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125495">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت امور خارجه کویت : ما حملات مکرر ایران، که آخرین مورد آن امروز صبح رخ داد و نادیده گرفتن خواسته‌های بین‌المللی برای توقف تجاوز بود را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125495" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125494">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
العربیه : پیام‌های بین آمریکا و ایران از طریق عراقچی و ویتکوف منتقل می‌شود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125494" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125493">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1GSHD7co7eSYRIfA76y3LieS4X01GXh0JvEA3n1qUD-yAdGN03DimiPPtt7rWN8BJu-8rhCsnJOy7uUikRgaVtASaLz9tzKk082mNbrJAfVkzMZ3lxyOCQsml5Ps-NFL62eb6B5gDkTldRoWfHsNolSiEFrHjyiZ3nzls3kTSifNZc5TvzUG7lurlcz-w-ARuH9_PIGsqpOUEN8hXkfRykpQhiZk729P-hnzXvYFhQ7uKY5Qoew9TvhPxIaOvppkKMW__8bza7W4q6UFZIPi02ZxfCW6GbXLzKehZ9eM6s6QgqXDF17FiEWFKvOwyg8OnvbzTtQBs-ZFUId5oAekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه
:
پیام‌های بین آمریکا و ایران از طریق عراقچی و ویتکوف منتقل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125493" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125492">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">⚽️
🇺🇸
یک مقام آمریکایی در گفتگو با رسانه اتلتیک گفت:
🔻
ویزای ساعتی بازیکنان ایران و اعضای ضروری کادر فنی این تیم صادر شده است ولی ویزای افرادی که هیچ ارتباطی با ورزش ندارند برای آمریکا صادر نخواهد شد.
🇮🇷
اسامی افراد تیم فوتبال ایران که ایالت متحده آمریکا درخواست ویزایشان را رد کرده:
مهدی تاج - رئیس فدراسیون
مهدی محمدنبی - مدیر تیم
محسن معتمدکیا - مدیررسانه
مهدی خراطی - مدیراجرایی
مسعود اردشیر - عضو اجرایی
مهدی ملک آباد - رئیس حراست
سروش سلماسی- آنالیزور
مهرپویا اسدی - آنالیزور
رضا جاودان- تدارکات
حامد افضلی - بین الملل
سیامک قلیچ‌خانی - رسانه
امید جمالی - رئیس بین‌الملل
🔻
تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
@AloSport</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125492" target="_blank">📅 13:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125491">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سازمان میادین میوه و تره بار شهرداری تهران: قیمت مرغ تازه در میادین و بازارهای میوه و تره بار، بسته‌بندی کیسه‌ای( پوشش کیسه نایلونی) کیلویی ۳۵۰ هزار تومان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125491" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125490">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">😍
قبل خرید، رایگان تست کن  ما کیفیتو با حرف ثابت نمیکنیم
😉
با تست رایگان ثابت میکنیم
🔥
@Netaazaadbot  @NetAazaadBOT
🚀
VPN پرسرعت و پایدار
📩
برای دریافت تست داخل کانال عضو شو
😍</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/125490" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125489">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOMzujEEtMxmaO4KOFySX-ktPQNmqLI7rPuWnDMdawyzFlDuCy-hD-ynqrPfBUcMnJ0jHNhRnw3u2TMn0ug93JFWn60zKveBDnSlRmQygYKM23w9qu-ev_Q9F4L-fmBPjsMh7Zr_JBvU5ARzO4VGOEC0R-7-qQoB_yreIOqE_PqSHqToExF7hOXJhNAwTceXFWtLBKVe-cnzu3zF65DOAbLxRxfRhJYsCWN5PbpBTrSFRBsI6r6OW7sF7rJg_Pm4joyYY135WB2Ky6YXee-95tNa26sgodpwXQKFqmCUD61O0RPWpmmTZgdj23304wWayRsBbYSDKYoBQPPHbClW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
قبل خرید، رایگان تست کن
ما کیفیتو با حرف ثابت نمیکنیم
😉
با تست رایگان ثابت میکنیم
🔥
@Netaazaadbot
@NetAazaadBOT
🚀
VPN پرسرعت و پایدار
📩
برای دریافت تست داخل کانال عضو شو
😍</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/125489" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125488">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ژوزف عون، رئیس‌جمهور لبنان: هدف قرار دادن یک گشتی از ارتش ما توسط اسرائیل، نقض حاکمیت علیرغم تلاش‌های ما در مذاکرات واشنگتن برای توقف تجاوزات است.
🔴
از جامعه بین‌المللی می‌خواهیم مسئولیت خود را انجام دهد و به تجاوزات اسرائیل پایان داده و احترام به قوانین بین‌المللی را تضمین کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125488" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpSeacoCo2MIC_oTgb6K3S7qqmjjrzCFc1B2KNHx_fMbNse1S77FTXLUJ7wj2XFYCMhCCsbNjdAEiMAF3_ikBV8tLzNMWFuMYS3ZeumLEh8IBBNWsy9jjkwVT3nrRs6XrDfixWmUMCJVnjpAieIqRzOtE-3y9bhBTndi_4DYHIOpDfXtrssGpJlHA6l6n_RciiB5FdTMGrxNzG8eZIdZ4OHO6Mw0UswqJIVkcjkGas4J0UFk4eoFqnh8xUjLFqMHmFfX57gR0Nij5PdtBc1jKCpd035K2OcaSuIXVChODsutZm-EwxXbY9ffD8856NuFKSBQExasKsEGcuxlLqoXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxDDiQWj5_KWow59Sugj_gHPz6_rcrBlcyJZYhHGEa68zgNFkELZ-0KdszJDHQT3mxv3FbNoS80vwXivPocY_fJ0PAwWESQ8spUifFHu3uZ-zM3L808WYR9HfGHHIVi9u1rrjsKxIAAyUPuaYL2wWFG73Uo8vXBAItATe4TER4cW3IqGQfa6F482LLvdCB-9k3l_8Ptmkx9gCDWnJ4Vloa4jh8SEZqu0s_6AydyuEfHGMKCgHuoYBdy2PC1RRNkCNVSdeLr8Y_b3VoQ7gArMtSDd1L3lDNO5LX-sdQOCLnFXGyiDTqJEpIbLzuDQ-60LSEidfD-0fGUgu4bBiVd9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpuPeOMPq3fg3AhXVUcqUn1mu2iLKRtPvJ7n7nW6H4o7VBOX5oxjOtnQyZCbRUrYWbjbMk3vdvpV4n_4GQi_ATW2s0dh5wjOplRG6KLbUhLYVfZZC9efjUnEmhftOngTbenDw4hgvjX6TOpnTwqAo0bGenBq059smvldMu33fndLa-Or38hSDRt59pnSwwiv9YU5DxOlA5lkxpuG9YP7ybL3pk8qRyzHbsDhYp2tB0-nzc_plHT5tXXo_5y1W768SHkfa7hkYhubQilCKicKD4rsNCBC3qGvrNWJtzHKRBQzXsuxXTY9dM5Q6qeHZ5LH64NPeZgGEd01IjxNsYwaWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125485" target="_blank">📅 12:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125484">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نواف سلام، نخست‌وزیر لبنان: قلب‌های ما با جنوب است و دولت شما از حق لبنان در حاکمیت و امنیت خود دست نخواهد کشید.
🔴
درود بر تمام روستاهای جنوب و به آنان می‌گویم که رنج شما، رنج همه ماست.
🔴
تا زمانی که جنوب تهدید می‌شود، ثباتی در لبنان وجود نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125484" target="_blank">📅 12:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125483">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
غریب آبادی: آژانس نمی‌تواند از ایران هزینه سیاسی ناامنی ایجادشده توسط متجاوزان را بخواهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125483" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125482">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJG1MH6AVQeB3vDTmZTaWLX5xH5ZBiA2cZgbslpQKZ7OfH1TgvhU9mMJGCxlJ5eghBBYGeYWmnjkspmrAuvDxM9BSI9Yw0hg5GxGzfurvjlcjrvn1pjeFKD9DSyTfuWS9FjO1T9MGygE9rCYQkN-x4NDyE__CIr04kkBon5JiKsRbwjrTMmrdxP0A7Ys1nSYSTWnf8ScBaI0_9mPJ_Brlb62ZiD_XaMZfTE6Ejr1IBnd2RJQgnJlYwVvQFeCbm7Z5570oYsSrhEfQRz7hojCaxOiCK0ROhUGxJZ639nY86pbpawPYOcMU5HIRYJCOnFENHf6x0smGNBsbsY8QpqHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که به تازگی در فضای مجازی منتشر شده است/دادخواست مطالبه ۴۱۴ سکه مهریه دو روز بعد از ثبت ازدواج توسط زوجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125482" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125481">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asIuvXUVtRhZ80Ny1LMdfdWS7HkoaQZVIgiqnD-sL5oPRpGgnIARJoPdniLg4VnhBpwKbGngt9OoNNqyvDRUe7oOctR9uvbX1T5eWaCbmuSI1cpnSggO6muWioZSSyKlBHnXcU30bL2O4BRBYGy3LwKCfw-SB6K2TN80yMfdqurA5Mq8dr5jhflkqB2cxXEyqC3qS99tpjfTzgqC5ETuWmzGHCKKby8ZwTbzsJUr154Gmqb8Kq2tG5asSGv6tI3pL2ssYzyrNHxFr1v7gR_5uB4639sTkq53KmfZp_JvF8DG8fosgHewKdBTJQySrPv5njytkOVR-Ah4so7zVv-eDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشکل جایگزینی پهپادهای منهدم شده آمریکا در جنگ علیه ایران
🔴
ناوگان MQ-9 نیروی هوایی از 165 فروند در آغاز سال 2026 به حدود 135 فروند در حال حاضر کاهش یافته است. طبق اعلام فرمانده سنتکام، این پهپاد در جنگ اخیر علیه ایران شاکله اصلی حملات علیه ایران بوده و بیش از 4 هزار عملیات شناسایی و رزمی انجام داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/125481" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125480">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PML-ui516RdBYhw71cP9omzIQLuGOqIRxyhuZDwPBzeawTugXceAtjPaeV8jZFLE8sCzUdbYkYCNJfKxKPoFL5vekLdBxicXi9s-Ib2u0n8f-hZzvOaBo8TQ1CZ_xazTVEKrq0p_bzaaY5V-3RR45t6g6G8ZkY8EQGfMTDLV3k8AVubBdP-TGUTc4jpNcXh71VjCvuAirPGKYTFSBN_x_80qearAaV1AnM8_81qzXd0-AS9UTzXBX-5cag6yDnMQeYUADM0cIaWaoUOma_1TnGbN87DLwTbsvbBHtjshHJNefxPnxThw-EIS4dSL3nf5zROeyT9Gyjhw3_GkTKJNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۳۲ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با رشد ۳۲ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۳۹۱ هزار واحد رسید.
🔴
شاخص کل (هم وزن): ۱۱ هزار واحد مثبت
🔴
ارزش معاملات: ۲۰۷۵۰۰ میلیارد تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/125480" target="_blank">📅 12:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125479">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082a0108d0.mp4?token=m1mAwVaX3VoO6qnlqttHg7lCWJBUZdQGid7hul5CiGs4wE70_y8a74ySsf_VPmexDvKhsfFSDRn8L2XyuZ2MakZwCk1RhwTEdxYhWIbGFPYLcc0vw-IXVnSJsw80DPLVeRUAH4crnqaCt90BiKKOJecaIdXLFGVdUpEdCLS5vJw3w2O8bORG1_WjwOOZoy4p_rHuq3GLbSkxLUtUYERi4aKh_vVtfota8nRkmF3HCpQcuSZQMeLWANQ42gfzDd9_qMCazfh-y4YGFHUx_c_pdncdYZWB_mdtKGMsQ4nW5Us2rF3iCfhWoAQ2haN1zZCFbgVzhICBHX05jY_HTURLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082a0108d0.mp4?token=m1mAwVaX3VoO6qnlqttHg7lCWJBUZdQGid7hul5CiGs4wE70_y8a74ySsf_VPmexDvKhsfFSDRn8L2XyuZ2MakZwCk1RhwTEdxYhWIbGFPYLcc0vw-IXVnSJsw80DPLVeRUAH4crnqaCt90BiKKOJecaIdXLFGVdUpEdCLS5vJw3w2O8bORG1_WjwOOZoy4p_rHuq3GLbSkxLUtUYERi4aKh_vVtfota8nRkmF3HCpQcuSZQMeLWANQ42gfzDd9_qMCazfh-y4YGFHUx_c_pdncdYZWB_mdtKGMsQ4nW5Us2rF3iCfhWoAQ2haN1zZCFbgVzhICBHX05jY_HTURLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پیش بینی های درست تاریخ
🔴
نسل 57 چون زندگیشون تامین بود و نگران آیندشون نبودن ،دنبال یکی میگشتن که بگه بعد مرگتون من بهشت براتون می‌سازم.
🤔
یه مشت حرام زاده سکان کشور رو گرفتن که به این روز افتادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125479" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125478">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر خارجه ایران :
آژانس اگه روی بعضی سایت‌های هسته‌ای نظارت نداره، به‌خاطر حملات نظامیه، نه اینکه ایران همکاری نکرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125478" target="_blank">📅 12:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125477">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfNt_0hlczSSyxx3lRhFxfmzFa8mZSQz6igTWrrIV6z2izIARiqNZrWxhD9dZIhAPLGBa5uuezy1OdP-ngIaPuzz1juwxpOQsc1d3qMbVBfnL6GE6l9E5uKJL6kAUq7u8lFMKZWsyi8OTSVk6vfFAc2Jvpqsds9DAw3zi3uZ0PilcIbtL4tFAYuKyZcFeJux7EwUlI4Sv8Nw4FDH-CRLRXNeilvFb1afLsiNDw9h5GlEaYlgKdAkvjdGFn8bQrzXqTccZFDuG-W0soHcnEo1ariwFCm2xV7d5rJcIH1HvSalqKmqqyWB32zdDsWQN6ySNc8EZECHRr4hh4bLOqumYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل یک سرتیپ ارتش لبنان و دیگر پرسنل را در حمله‌ای ترور در جاده خاردالی-نبطیه هدف قرار داده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125477" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125476">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125476" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125475">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
لاوروف، وزیر خارجه روسیه: روسیه ناگزیر حقوق روس‌زبانان در اوکراین را احیا خواهد کرد.
🔴
این یک پیش‌شرط برای راه‌حلی بلندمدت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125475" target="_blank">📅 12:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125474">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گروسی: ایران نسبت به ما تعهداتی دارد و باید دسترسی‌های لازم برای بازرسی‌های ما را فراهم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125474" target="_blank">📅 12:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125473">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f714df4f8.mp4?token=PfK8UXjXH2-PuSuzxEXrrOf_ZgTjue0ENdJn-4hQkEjr_bQW3XT-OB6ghBMnRcURr6-dx6Gx37oE3DSk0E9XVb87VLcwLQd91YDIrLWiD1gcHSv6mjbwJejLxAWQ0rzVRM30LH4VT4RAbb1ifnFsMYrUQO5LjENHrowZkdy9lXZD9O1TqTMycON3qqeXRllXdfgNe2uI00nNBAWmhussja5RSF6YPrDIDn8c2qm1ZF6sDARSBiEzMIVhJ9sz1Qr35JGSnF-Nc_4kge2OUhRBYCeNaiVKw8QSDewd5mZjo-qvEF3rZSsgXKpinm-WqZvcmF04g3CmQLNrFPlSOgS7wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f714df4f8.mp4?token=PfK8UXjXH2-PuSuzxEXrrOf_ZgTjue0ENdJn-4hQkEjr_bQW3XT-OB6ghBMnRcURr6-dx6Gx37oE3DSk0E9XVb87VLcwLQd91YDIrLWiD1gcHSv6mjbwJejLxAWQ0rzVRM30LH4VT4RAbb1ifnFsMYrUQO5LjENHrowZkdy9lXZD9O1TqTMycON3qqeXRllXdfgNe2uI00nNBAWmhussja5RSF6YPrDIDn8c2qm1ZF6sDARSBiEzMIVhJ9sz1Qr35JGSnF-Nc_4kge2OUhRBYCeNaiVKw8QSDewd5mZjo-qvEF3rZSsgXKpinm-WqZvcmF04g3CmQLNrFPlSOgS7wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ هوایی اسرائیل به شهر
السکسیا
تو جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125473" target="_blank">📅 12:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125472">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
زلنسکی: این جنگ باید پایان یابد. اما رهبر روسیه می‌خواهد به جنگ ادامه دهد.
🔴
شب گذشته، پهپادهای ما حدود ۱۰۰۰ کیلومتر را تا منطقه سنت پترزبورگ پیمودند و انبارهای دریایی دشمن و پایگاه کرونشتات را هدف گرفتند.
🔴
قدرت ضربتی دوربرد ما همچنین حدود ۵۰۰ کیلومتر از منطقه کراسنودار را پوشش داد و یک انبار نفت را مورد اصابت قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125472" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125469">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=DaR_YauX4xcztQW7nmatgQMtF8uyD7AVjrurq6QvPjZrh1E8uhW-7bNrZj3r_AWSHZNLvfZuzvRO3rgd70vtoNZYsQ-v1cBXwBBD67RdWpgE5sbilW70TrvTbRjwWWMsSA1X1FKzbLIZ1Wru4WCM4xUTIVZX4b_ppsnfZ7M2_UE0cf1d6J6Mk2xM8Mie4iMlmBwDryMgRozGes6Fe1ij6NHgzvoMzgvCliAx3cvPixcxMLg1G7dnS5oxlGqANOi_r2vQfecVvDak3uoHdVjVNWcl19YzpdZZqsIMmBGySJ3UU13oAvL_ez5RUuNPPFXCxzTCoFXDtqM0CpnK-h4s9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=DaR_YauX4xcztQW7nmatgQMtF8uyD7AVjrurq6QvPjZrh1E8uhW-7bNrZj3r_AWSHZNLvfZuzvRO3rgd70vtoNZYsQ-v1cBXwBBD67RdWpgE5sbilW70TrvTbRjwWWMsSA1X1FKzbLIZ1Wru4WCM4xUTIVZX4b_ppsnfZ7M2_UE0cf1d6J6Mk2xM8Mie4iMlmBwDryMgRozGes6Fe1ij6NHgzvoMzgvCliAx3cvPixcxMLg1G7dnS5oxlGqANOi_r2vQfecVvDak3uoHdVjVNWcl19YzpdZZqsIMmBGySJ3UU13oAvL_ez5RUuNPPFXCxzTCoFXDtqM0CpnK-h4s9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
🔴
«خسرو پناه حیا کن، کنکوریو رها کن»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125469" target="_blank">📅 12:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125468">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYyMWk7GBJWmkJsMP-9KoC4xwEGEILAfWXIMsDNa0yPAz-sNBHLpD3KNEBTFs3HxWIatL9wlGsCeDejBwoDz-46pnROLd9fuGG5T2QyOesFO-GEmYef_tlhRgF16Kn9JuNMLd9PLr-z4KcDlI5Sipu-owu82qQz_j48VfXh0x4vB1qe4YGh0EyM1ZaQ4rzUiW9Vlx802BXpZGd9EILnYESHSwevqNkwvQ1EUQ-UAiJrmZhDbyBzJW1J2vBICLMV9krW3KJRoFFFRPdJePZCQ5Op5RIta4kZxdLRiNEF810CYaVlwAlbfCfs5XWPM-PvyyHDDlHhXxmPsqRz-67Sh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تریتا پارسی: به بازیکنان جام جهانی ایران ویزای ورود به ایالات متحده اعطا شده است. اما آنها شب را در ایالات متحده نخواهند ماند
🔴
آنها در مکزیک مستقر خواهند شد و سپس برای هر بازی به آنجا پرواز خواهند کرد.
🔴
این بدان معناست که آنها باید در همان روز بازی از طریق اداره مهاجرت ایالات متحده از مرز عبور کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125468" target="_blank">📅 12:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125467">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
معاون وزیر بهداشت: بخاطر قطعی اینترنت یک رتبه علمی در جهان نزول کردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125467" target="_blank">📅 11:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125466">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmL_qYbC4V2fNX5dsrjTYzkyPjadMR5Y_PoHVnVzBlOjb_YNeg1RU7cwbHcMIZ4eBAUlgfxM6Qu0CxU2bfkGoKMfCfW4oBNmEoAROiw-FAi0r70-ONx4ypSofrP5oi-9_zH5D7H2MMDTJovPIGqDixPE2E8PJ_nC-azfk9nFD1Na8_QJVoz4h755QvzBnILE-z16w86Sz0hLo86WdQs6IfRecmAwyB_KY0fN6FMcjWjcvtbeMyRaSVPIHWwrdku9mDw63Xf4qeaeYoo80BMRSynDPtR71LAsXRbxcA1RujA5I9KBtpCBb74W6va7VneYV3PvJ1xpQiGl1XdyO3CJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت مردم پاکستان داره قطع میشه بدلیل اعتراضات مردمی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125466" target="_blank">📅 11:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125465">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق تاکید کرد که ایران پیشتر اعلام کرده که عراق از محدودیت‌های عبور از تنگه هرمز مستثنی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125465" target="_blank">📅 11:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125464">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری کویت:
از سرگیری ناوبری هوایی پس از تعطیلی موقت دو ساعته.
🔴
تغییر مسیر ۱۱ پرواز به منظور حفظ ایمنی مسافران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125464" target="_blank">📅 11:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125463">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تهدید جدی تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125463" target="_blank">📅 11:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125462">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ادعای آسوشیتدپرس به نقل از مقامات آمریکایی:درخواست ویزای برخی از اعضای تیم ملی ایران به دلیل ارائه «اطلاعات گمراه‌کننده» رد شده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125462" target="_blank">📅 11:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125461">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رویترز به نقل از وزیر انرژی آمریکا: کاهش قیمت بنزین در گروی توافق با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125461" target="_blank">📅 11:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125460">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
الجزیره: ارتش لبنان اعلام کرده است که چندین سرباز، از جمله یک افسر ارشد، در حمله‌ای اسرائیلی به یک خودروی نظامی در نزدیکی نبطیه در جنوب لبنان امروز صبح ترور شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125460" target="_blank">📅 11:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
انفجارهای کنترل‌شده در جنوب اصفهان و بهارستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125459" target="_blank">📅 11:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_i1TH5MJ617Sl3ITIYqExaRa_jcyhfscDYGIr_9r4qOvEJ2BiHfvSufPOHNZU1k-Kv-KNN7-VvJFECBsCyKx6aEYDgUtJgPDIp-5EHXIxk-G7dEL52qJRWFMvjIcwecLSEJC4ylRDA8m2zUGavmjS3pZxDnnSNxhVuZVp5OCt-HS1Unct9ndciaUDOIBXEceaiJ8poGT8dQxD-erHblU8xYZAEBFnqeIKFQPXWWBarJbbh1dpM7Z_d-swiq4cwlBEiviCa6MpgjAHTy6SwPLvT7PgVLIMPmWkvdU3GJtSyj8eHTxf74baXP_26t0IxPijbHEM-v1GEP3eyhKHz6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت بورس مملکت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125458" target="_blank">📅 10:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125454">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SADz6sfRQinaeSLvSLV4Ha8y-sPv_0py5nQ4Q1qUbyBXVWkHAd0-pDC1eWTjcKpVr1y55rUneSjQUGZ-nMUysQmsFee2kvNyAbHGHCvxBrjU5HBQBxYsyijWJe12lb3lIyLi-lUsaMqHLNGe4p1X8sJCE52yMyCD9naN_CnWBbuCPEjbbdzliWPgyYJ3fuJDa_lOyYFp4H9LpcTArqiktrtUfsG4z3NTnIi1DG7soeUOpoaHX_hB_57GOV9PLuAkEKlat49cQ6oY6frinTT9zpdBxWRNTpJVIxFlpcFMEdHiHd7yeih9ZCQqsCMVjZw3pL08NLtCmqHhxDp-UVOaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gT8_5uALH_YayelNSiSejJxrjghFIq_PBNCiTtriC8OVRm3J2CKcH1F2SZwwF5Hnwc2iqd7edj69Z1-e6soDGGbxZa4OH1FhVz-TVZAmtiogOXaGcoiJB3mJRK-r4wfvQJVx4DgtGizrLhWCngAsYqCyJzH1rQCQqAt_t6ZZnFYvXmXy03maRP9qC7uF4nKPrXuInIDx-LH5n97d8ylhte2FaMopqV_1buwv8a4D_WIiwSPX4Fm8TLG9wnNqizcSsS1VRdZcbbPVAl56to3GsGVovZ3S8f0LKhpCy7EykhvEe-RJMJyuxaLShJ0kVrMHtqZPKv4XUXAUZKPsVKWZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PexPr0RFRAlN5KNXp1_12Yyhxvx-nP6QhetS08Z4qejz4Zyf-veqSyXlsxxBgRmNTcXYH81DbztKKJ6JxM5i1tu0gn7a9XCiEND68DgP4k0B8gHwua40QcgzrSgp8j35vZML1UsTS3-jbOS-ReJfhmKDfK57lGDx-kFEFV9GmRz9NWYUfmWSdcchcZavSdziu0J2k73NNKp252wtTkmXYokyrCogi8JLtjN7tbMeHnAiUxSpNGMgPgI-czcGJFDAsnFs9UMy8Tr778JhjUwqEGlJOO0Obd7eTrGXZSg96eG7PBAJ8Ztb60rnFlRYEaHGDbdwujCqNDr7vnh70DZtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-8sqdclMylQVVapfxRlFr4DKPW3SnE9IrCvwuSKBC6K2j8ELfwBFlkL_Gd5yzoBMLGMc2zy8Q59sFl5dMCq0nik6chdWWvJouJRqLgF4e1ZedeOdOdJfrDH2g9FIBXbvae3HpT4DBDud4z55XuOxRbqwibqsjCvXcjAkx1DvDe8Dbk6ct-c6oqz35-FSTsvqgUC2YxFZzcabS-YBXjtJBOYpFwK0b8whIIxf-Af4sqiJoUuy5Tgy1_TMz2ThlTpBCw2zHeuNPG8QsYYxi0Zvd7EsoTUcVPTnTQG1fpAGTtMhndSX5J9FCvqaA5_uFGE9G9Ous5Sa-umrWhAXjmsww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار فرمانده سنتکام با مقامات ارشد بحرین، قطر، کویت و اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125454" target="_blank">📅 10:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125453">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYUVkjRkQ3HOswY7DSx2nwseiQzQw8pIXzWi8S1tUDIlp_HCczzRd3McWZ-GaBckonzX-EKOP-zRngg4ggmcV4Qao31NWDwjzHxU2e8cbJ-KoVTwHyATQRg0chJICHIrkf14EsXnbMgIfiD0w3lgT2i8fLY0Ln-luySQtObG4ee-hNRyCS_WV2zZmWejMYVpnZHig_TbklgnLsDdB5STe50L2SFCTX3iQmLDbMf59rnGvTJmIVZ60aV7wcbhb4adrBqnzgW2-ypx4qHpmyuFg-DJndmwNeeiQpueMEZRkI28xqjAd63oJO6UeUEtfMVP4SGe0_HMv0ermRu5YQpg-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بحرین حملات موشکی اخیر ایران علیه بحرین و کویت را محکوم کرد و اعلام نمود که هفت موشک بالستیک که به سمت این دو کشور شلیک شده بودند، با موفقیت رهگیری شدند.
🔴
بحرین از ایران خواست تا حملات خود را متوقف کند، تنگه هرمز را باز کند، در پاکسازی مین‌های دریایی همکاری نماید و عبور ایمن کشتی‌های تجاری را تضمین کند، و هشدار داد که برای دفاع از حاکمیت و امنیت خود، تمام اقدامات لازم را انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125453" target="_blank">📅 10:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125452">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkEeN2iF0I7GOMFHbd5G1BFnb5OrCGrc39MGfYNzQ9fe8XurrO47GhDjGB3U-DbTHnRBoppeFQTOm1EiuXeDdWjeAx1PjNOANri16V_xIOZ32XP03dTyHUP7yDxqfeNeRvVyLrXrhy2_lzE_eIwyr6jXeTXOcVQ07li5sPwMgrlHMMc0q8yu73fu1hggyiRnry7di8jmk0mXb2-ni_Gv4aRVctLL0XQPpPpibWypEFGOScBcW7EUUXyJJ5dWXv97pVUhGULZbzUUC1Vbg5BDMbJCQ8y6XIHunFwK7c2NVrtsRapM_nnJKlvrqzxU1hSdB_FOe-pE0CdcZzbZCZFOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس اتحادیه تعاونی‌های مسافری: با ابلاغ شورای عالی ترابری قیمت بلیت اتوبوس‌های برون شهری از امروز رسما ۲۱ درصد افزایش یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125452" target="_blank">📅 10:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125451">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سازمان اورژانس: روزانه ۶۰۰ تماس مزاحمت برای اورژانس داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125451" target="_blank">📅 10:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125450">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سنتکام: ۷ موشک بالستیک ایران به سمت کویت و بحرین شلیک شد
🔴
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد ایران هفت موشک بالستیک به سمت کویت و بحرین شلیک کرده است.
🔴
بر اساس ادعای سنتکام، شش موشک توسط سامانه‌های دفاعی رهگیری و منهدم شده و موشک هفتم نیز به هدف مورد نظر خود نرسیده است. سنتکام همچنین اعلام کرد هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125450" target="_blank">📅 10:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125449">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N4REkdOJr7Uk5Zyj6jmy6GCVtBv7-EUK7_qTvS0ODtwr6K1Z2fVxivoGiKvnbB3xU3qUWbNfXu5dmPjVliPalgjvXb5L1TULdrQs3NNUi7nk1x5ewHxYlVhWaUnSIswNb_fBwdoHf6pWtnoh-n5o2aZC_oqCOx-KVkQrV4uozSyeY4NZVYnw7PfKKXF0qcq9rEJLwQ-75NJ19stxbirw0NlvopVXUWyTdiBvJr5iz5QM5mlUr-6KwjmCr7F5Pmo1Wca78l5BP8Kg5XDbgrOdMBSQPxBoOxXmmtSkkrIEk-s8wkPlX4j5CXSrYBOgNiYE2EcSfWffClOpD5INM2cr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل یک سرتیپ ارتش لبنان و دیگر پرسنل را در حمله‌ای ترور در جاده خاردالی-نبطیه هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125449" target="_blank">📅 10:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125448">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سفر رئیس سنتکام به بحرین، قطر، کویت و اردن
🔴
در حالی که پاسخ ایران به نقض آتش‌بس توسط آمریکا ادامه دارد، رئیس سنتکام «برد کوپر» با مقامات بحرین، قطر، کویت و اردن دیدار کرد.
🔴
فرماندهی مرکزی آمریکا در غرب آسیا در بیانیه خود اشاره دقیقی به زمان این سفر نکرد.
🔴
فرماندهی مرکزی آمریکا در غرب آسیا گفت: او (فرمانده سنتکام) همچنین با اعضای نیروهای مسلح ایالات متحده که در این منطقه مستقر بودند، دیدار و از (این) نیروهای استثنایی تقدیر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125448" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125447">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgJni9F25_6lfsRAEhdfpmf100xpf2i_GKNvoTKoqQxqFfzbWCUUlfoXZK_0IlRF5ZZqfKNKcizJrK4sJSePImlk0qeMCbXKrgWkRsoy-omzvs6C3iXBcJNmVjQUlRWOPKxW1gPxbbhbA1IPcVBuezFusXHPBFF6wdB4zRDclGeP7jocuFm7PKEcT04HI17S2Z0dg4M5x_9t07lqg5Yslz22x38pmat8f0E9-vbK-c7GxSqg7zzQ7oVvaX_kML0Qu-nOrtLSaj8PU0JT4GTG-dgX3sM2RUAa86kgjnaAaUI5syvMygmLD-yUyzDDkVONFHennqJICM8PY4NNx1LoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی میفدون-زوآت در جنوب لبنان را هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125447" target="_blank">📅 10:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125446">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پولیتیکو: آمریکا به دلیل کاهش ذخایر موشکی در جنگ با ایران، توافق تاماهاوک با آلمان را لغو می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125446" target="_blank">📅 10:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125445">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd9a25e0f.mov?token=hkCWN9OdaGDTfoMLHOvqPxcLpFe6T9ckhPBEUUKJQFfQ2ajarndHYQUaWugyhshrSR-o7CmNL-7QHVs5WNWcautoSBaQmj4C1QPvioo_e6iCUgm4qWdfRGg8HsDkrUMFFmHqVH_SFmQwVu6wNl9CDzK6KrEcDRpSceMCiCjqrKr0M4V9n7s-u0o4MFLv4gzwkayEGgS9QXJTUf6QXHflZrZX6THUS2-a-vqLScZ_mwl8JVgvNI-VP4fBMmhiSRdEON0YLqjdW3sp3BpXJ50PmCNI0lmvZkKVlcnRrGQPHB3LSw8s-h_QoFcLeNum71w3ir5bS3HQ06GZrtsNtOs_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd9a25e0f.mov?token=hkCWN9OdaGDTfoMLHOvqPxcLpFe6T9ckhPBEUUKJQFfQ2ajarndHYQUaWugyhshrSR-o7CmNL-7QHVs5WNWcautoSBaQmj4C1QPvioo_e6iCUgm4qWdfRGg8HsDkrUMFFmHqVH_SFmQwVu6wNl9CDzK6KrEcDRpSceMCiCjqrKr0M4V9n7s-u0o4MFLv4gzwkayEGgS9QXJTUf6QXHflZrZX6THUS2-a-vqLScZ_mwl8JVgvNI-VP4fBMmhiSRdEON0YLqjdW3sp3BpXJ50PmCNI0lmvZkKVlcnRrGQPHB3LSw8s-h_QoFcLeNum71w3ir5bS3HQ06GZrtsNtOs_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دورهمی و میتینگ تینیجرهای تهرانی برای حمایت از تیم ملی در اکباتان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125445" target="_blank">📅 09:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125444">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b7b5a89e.mp4?token=pVWMjzXlxICoWiOnQPI9Q5WHn4P-IWnnHc9ESbxP0GOmgApBvEmOu6tiuXFWkYlOi8xdGSvD7-5DorzVEv5UaMliv2iBUy9shS8eeWBOkStzJ3zPdjxRB-w_RDWqXMiIfl7oci5xftZcVymbHSW97VWIkS4rdIKcO4_qeVK5uNNSsJvqAX7_qrX6rRbNMiHOazLQTdbneYt74MirdU2_Z8-UutNhLeQLls412XH3_NrSK-AAKThiS1BwyAVTwPnnH4YuavahEUbSvikG7fBN18WplvYiA7a6ZTqmZyke6QUj1sqpbzWez6WIepiZ8WT_OhDTxxPOBIjY0hYicOg3Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b7b5a89e.mp4?token=pVWMjzXlxICoWiOnQPI9Q5WHn4P-IWnnHc9ESbxP0GOmgApBvEmOu6tiuXFWkYlOi8xdGSvD7-5DorzVEv5UaMliv2iBUy9shS8eeWBOkStzJ3zPdjxRB-w_RDWqXMiIfl7oci5xftZcVymbHSW97VWIkS4rdIKcO4_qeVK5uNNSsJvqAX7_qrX6rRbNMiHOazLQTdbneYt74MirdU2_Z8-UutNhLeQLls412XH3_NrSK-AAKThiS1BwyAVTwPnnH4YuavahEUbSvikG7fBN18WplvYiA7a6ZTqmZyke6QUj1sqpbzWez6WIepiZ8WT_OhDTxxPOBIjY0hYicOg3Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فلاحت پیشه: امثال ثابتی حاضرند ایران غزه شود ولی توافقی با آمریکا امضا نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125444" target="_blank">📅 09:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125443">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ در گفتگو با ان‌بی‌سی: رهبران ایران هنوز برای پایان دادن به جنگ جاری با ایالات متحده به توافق نرسیده‌اند زیرا آن‌ها «قوی» و «مغرور» هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125443" target="_blank">📅 09:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125442">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sELUtwEpxFgIVh_Y9vRsQKT-hrqYofBYeU5O6hZiGFegX3OnaMvMtJ4ZbK0kbQjFjT1WBpXiaed7xe4SYUNp-KDXQ7PhkiU7YXRS-Hb5IneVx-xy6PNzUqA8lEl-Q5qGv1K5OtAACkn0hhsu1jPLUDvAFBMEwYu4LGEtLrZ3yT2j_pbCwBQ63naHGpe6syRuI8CnUmyTXp185a4v9412T30cmZmRQn08wANtxKu7jXYdPCn7g2eXrZWYiCklCpoLWq7G3i4VROU6hHlCHivB5P1OK5VTjmXn8yHk1pgaE6CvtBXru_9dXsAJXhJrF_epe0MC91QgnfZmillRytd-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاسمین انصاری، نماینده کنگره آمریکا: دونالد ترامپ امروز در دفتر بیضی کاخ سفید، چند بار به خواب رفت، دوباره.
🔴
به همین دلیل من خواستار اجرای متمم ۲۵ قانون اساسی شده‌ام، و ده‌ها نفر از همکارانم هم همین کار را کرده‌اند. ترامپ بیمار است و باید از سمت خود برکنار شود، این یک بحران امنیت ملی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125442" target="_blank">📅 09:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125441">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=KrQy3rqa5RgXUItyL87_1xWHlDUueAEIGbU-l69Hi1QNvic8nsKTO2tne_rcG2eZOS7ua2DJKpgrq2arhSJHr9HLnQkXz1W_NuJHDomxppwVLm-f8orsPAl4YCCsn6l6jfflKP_TQjUgMQCLCg6ALHAl3abf_xDKQOcSOhfrc2jhG-mwcOyJdN_f3kq-V4QOQOrknMp4Ry802-Ri4jtY1-KP8tqZonf0wylU4t7mGNq0F_re2MskGImtgEY1--GEJ0GVzEMyE7XFWRFV4Uj4Tn-YPG2wE1nPkFdiaM9mT9P7LxMmrY6derdBZJy4_ak0aDajp-5Y-SRwE7I0bpn2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=KrQy3rqa5RgXUItyL87_1xWHlDUueAEIGbU-l69Hi1QNvic8nsKTO2tne_rcG2eZOS7ua2DJKpgrq2arhSJHr9HLnQkXz1W_NuJHDomxppwVLm-f8orsPAl4YCCsn6l6jfflKP_TQjUgMQCLCg6ALHAl3abf_xDKQOcSOhfrc2jhG-mwcOyJdN_f3kq-V4QOQOrknMp4Ry802-Ri4jtY1-KP8tqZonf0wylU4t7mGNq0F_re2MskGImtgEY1--GEJ0GVzEMyE7XFWRFV4Uj4Tn-YPG2wE1nPkFdiaM9mT9P7LxMmrY6derdBZJy4_ak0aDajp-5Y-SRwE7I0bpn2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125441" target="_blank">📅 09:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125440">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل در دیدار با رؤسای شهرک‌های شمالی اعلام کرد:‌ «ما طرح‌هایی را برای گسترش عملیات‌های نظامی‌مان در لبنان به سطح سیاسی ارائه داده‌ایم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125440" target="_blank">📅 09:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125439">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پنتاگون سطح تهدید ضدجاسوسی اسرائیل را به بالاترین حد خود افزایش داده است، در حالی که نگرانی‌هایی وجود دارد که اطلاعات اسرائیل تلاش‌های خود را برای جمع‌آوری اطلاعات درباره بحث‌ها و تصمیم‌گیری‌های داخلی دولت ترامپ در مورد درگیری‌ها در خاورمیانه تشدید می‌کند، گزارش NBC News.
🔴
ارزیابی اخیر آژانس اطلاعات دفاعی، توانایی‌های جاسوسی انسانی و جمع‌آوری اطلاعات فنی اسرائیل را در سطح «بحرانی» ارزیابی کرده و به چندین حادثه اشاره کرده است که نگرانی‌ها را افزایش داده‌اند.
🔴
در حالی که اشتراک‌گذاری اطلاعات بین دو کشور بدون تغییر باقی مانده است، مقامات گفته‌اند که انتظار می‌رود کارکنان آمریکایی هنگام سفر به اسرائیل یا ملاقات با همتایان اسرائیلی احتیاط‌های بیشتری را رعایت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125439" target="_blank">📅 09:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125438">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfITrN0Z2z-JD_iNuHQyiKZgryosdQrFvoYEVSWHylMPdyktokqnDgHHS4wZxsdQv8KckUTOZmhMLtnqjiVfLDtNDE8zTHpDLTZVBPdMc5AtDrfeiHYDMyuNXW0cmcFp4gOBZfNe-a_BAwGQd2KI87Ym8P_8Ce0zXiw52gOHCHthR64z6_vDg7989lImiqfiEGeX7czAEgrmrjGy01afV-KuVpAxM6MimhPtjUEqqb_xYIv9_GKnB-eIz0IM9raSL3kmsHSCJ03Ef64SFsvtSz2By-HpN8elM1alCix2rkPS0MuywaLLdeAg_mF6QC_0zKlZKq7qNwYTGfF0E3XOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش فروش بلیت‌ قطارهای مسافری برای بازه زمانی ۱۷ تا ۳۱ خرداد، از ساعت ۸:۳۰ امروز (شنبه، ۱۶ خرداد) آغاز شد.
🔴
پیش فروش بلیت در همه محورها از ساعت ۸:۳۰ تا ۱۱ صبح روز شنبه (۱۶ خرداد ماه) از طریق سکوهای مجاز فروش اینترنتی بلیت آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125438" target="_blank">📅 09:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125437">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYwxEWb-q5-v6jZpOL04532mLwCxCwxqco-oxZeNBPH8So2KwD29RvRzd6KDCvXg50Mmihf2h47HAPyRCSPQQGgS2tmwGtyRzXsX6fEUJoedwVNmVadkSAV11s0rS7pJAsheX4M9f6WSoxRBT6QEnX_XAiRDDEJ4FFKSf8-kWgP3TyjHrocpBJnAJ3ZmlUOiqGma8pmuTMyhUyqpOSrj6Ur-Idpi4qCvM_mWFBsjXfcBccn4MZ87Xsv7x8YURFqDGxzzO9YdABg4BWZiyOaqbR-SUTvS4dIxI9fDNN5jYIAoF8zYTmbv1bLhmjJAHJlaM_g-oBD-WKxiD5afqwzsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی به رئیس‌جمهور لبنان؛لبنان را از دست دشمن واقعی خود نجات دهید
🔴
براساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی‌ها را آواره کرده و کشور او را روزانه بمباران می‌کند.
🔴
اگر لبنان برای ایران ابزار چانه‌زنی بود، ما مدت ها پیش به توافق رسیده بودیم.
🔴
لبنان را از دست دشمن واقعی خود نجات دهید، آقای رئیس‌جمهور!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125437" target="_blank">📅 09:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پوتین: روسیه هیچ سلاحی به ایران تحویل نداده و تهران نیز درخواستی برای آن نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125436" target="_blank">📅 08:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125434">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoLeAyT69_66TGJ3PZJRZWTnnU4cwhUOc_ah4Z4IaL6ko44lBz6yVqvRalleCj6TD3W_cYANMUhzKXgNgBUtmd83EEFNkZmLijW5PLphVfM1_4p7cwv44Tr1tgBREKxa5ajsrM44001DFRzBXkTnqXqjSVC2AKpZnDhOQwXJQCdCi7UWue5kFuVib5fXdElhIL43S9PFSAu3yn87tNmFJVZCmb8F48GZyoNv9PrU6i2XXhAhB1xDs74hXu7_iK25lzGSBYrskACHV-QT_Li56gSNnpZnoydpruWgfuKSPmZmLjnQLb-ukYmB6y_29z1-p0z60RQT8xXfD0lknJJO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDMru-5FxYiKh4_BP8KXtlHDNhIYtF5MGttI2WRU47NhZFrxSu4BJVyOEaATV-84BShUXShJuHK1gQjhwotEYH4G5DDWN0Xl171K1R3i5rW79IFb73MCiyDbevma-twZeyqWalcTPVe_Sz5k0qKg2QZPyPMo9171XR2gUxoyKMuk9Kfr1kfbensc4zJ1BSgIWPq018Yd8MS5B2S6MD_FQWJg499tkLdu6mLXqyQFIDSiYYUGYTY59eJ0jebS61CZskt5psCNf7p_7KWriFEmH3H-6zmiZgvrW5tRQ975bczMXAJAViUuGSxuHtFQCaqM11sAs-a-S0QD9SHUpKPIhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون و دخترش (جانشین آیندش) در آزمایش‌های دریایی ناوشکن کانگ گون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125434" target="_blank">📅 08:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125433">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شبکه ان‌بی‌سی به نقل از مقامات آمریکایی گزارش داد که نگرانی‌هایی در داخل پنتاگون نسبت به تلاش‌های اسرائیل برای نظارت بر مقامات ارشد ایالات متحده وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125433" target="_blank">📅 08:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125432">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
چهار مقام ارشد آمریکایی به نیویورک‌تایمز اعلام کرده‌اند که درخواست ویزای تمام ۲۶ بازیکن تیم ملی ایران برای حضور در جام جهانی ۲۰۲۶ پذیرفته شده است.
🔴
بیش از ۱۲ نفر از اعضای کادر پشتیبانی (از جمله مربیان، آنالیزورها، پزشکان و فیزیوتراپ‌ها) و همچنین مقامات فدراسیون فوتبال ایران که قرار بود تیم را همراهی کنند، ویزایشان رد شده‌ است.
🔴
مهدی تاج رئیس فدراسیون فوتبال ایران موفق به دریافت ویزا نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125432" target="_blank">📅 08:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125431">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzkLKHV7ZSjKI7TFQ4coZrZ6vA56D0Q25irP-ZfoK0ikIK8wHApouRKPvZftn5PooAY6NEjFVAcTGv4rb51qQkjkH_HlzAQiLZtOiuH9fbGH7ae9tTEfVcRPvNpYzCQhSeGKpCjspEOwNtUTSNK3lCwQmnIQ4nLfYDn0qvAsOBkYt-bsU7h6-2zxPUbsaFp4vTm5PzIyuU81dBh-jzYeyYRYj67OAlcY98GYsmtgD4lkl4HCw-AtJb-fynusxJp0_YeJI0ZkPRzWQT2JZyrt7On5TS2aMHFJJebMcDzB16etPXIxUNdmnjZvjzafwg9TXI9uZ0YLT3oElKyMbcrGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از حملات ایران به پایگاه آمریکایی‌ها در کویت، ستون دود در این پایگاه مشاهده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125431" target="_blank">📅 08:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سنتکام: نیروهای سنتکام چهار پهپاد حمله یک‌طرفه ایرانی را که به سمت تنگه هرمز پرتاب شده بودند، سرنگون کردند. این پهپادهای حمله تهدید فوری برای ترافیک دریایی منطقه ایجاد می‌کردند. نیروهای آمریکایی سپس سایت‌های رادار نظارت ساحلی ایرانی در گوروک و جزیره قشم را برای دفاع در برابر حملات بیشتر هدف قرار دادند.
🔴
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به حملات بی‌دلیل ایران در دفاع از خود آماده‌اند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/125430" target="_blank">📅 08:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125429">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کیهان: دولت پزشکیان بخاطر استقامتی که در جنگ نشان داده، دولتی پرافتخار است / محبوبیت پزشکیان بیشتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/125429" target="_blank">📅 08:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125428">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6jIhpbLG1iA1O_0BuqI5JOe_WTipQK-V7pt8T0EDW64r51trF3Eu163QGYaMeO937nQbR23ZKepbZV_PMid7ZMXKr1Ot0neoA4afHnTuC044_NxkaDM_-QAG050a2-fGK8Ghs3TJczfUv7_EvZyToanfUYAhQCUH_hTh6sO-2xYkilVMMV9_-3FosvzXNm5uPnurlQ5oAd2XXFORsaKAUR02cTSLopL7lfvAPyvJRCZLFEg1UWs5STv2SpZOpwkkiTTs3MIiaeOVInWiUpAJYSDOtYuL1dQhiBpFCU3l8FAmQzxUHvS_Qsc3JdlFlxxxaWx_dgrl19yCQYqcKvr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی بی اس: تا الان هیچ کشتی‌ای توی تنگه هرمز به خاطر پهپادهایی که ایران فرستاده آسیب ندیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/125428" target="_blank">📅 07:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125427">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=YO1cm3OPdyvMgICNJDsQXwIS5UOQWRQ6NuwYj1PyJCnkmkP09rGX-cowj4ompLCH2Ybo35bR657W0ZUigyjbFg1K3WilIbRExcRKLh148eXt0Ou-HPWpUrM1f_k_C_VOW732W86WEBJ-78C_AoCHf9zyLD1Ym7FoZZw02CchxMWqWzraATK3bTolzSPzh5oHWMJ0qzzkTFhYlw4-YB8BN2HJ8FD6ruiFSRBc6QVzV1R_6gB3Jmo6nh3AAY1aRKJmi5Oo7N8zlVl_PUw6bd7uQC2ej0JbsB9ZUGk9MpO1z0uJybHTKdg6cuxaqDIqn6n01Q398QuNf1iB0dQ77WKMog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6388d22ab.mp4?token=YO1cm3OPdyvMgICNJDsQXwIS5UOQWRQ6NuwYj1PyJCnkmkP09rGX-cowj4ompLCH2Ybo35bR657W0ZUigyjbFg1K3WilIbRExcRKLh148eXt0Ou-HPWpUrM1f_k_C_VOW732W86WEBJ-78C_AoCHf9zyLD1Ym7FoZZw02CchxMWqWzraATK3bTolzSPzh5oHWMJ0qzzkTFhYlw4-YB8BN2HJ8FD6ruiFSRBc6QVzV1R_6gB3Jmo6nh3AAY1aRKJmi5Oo7N8zlVl_PUw6bd7uQC2ej0JbsB9ZUGk9MpO1z0uJybHTKdg6cuxaqDIqn6n01Q398QuNf1iB0dQ77WKMog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پخش دیشب برنامه «خیابون انقلاب» بخاطر این حرفا لغو شد.
ما اسرائیل رو تهدید کردیم اگه کوچیک ترین خطایی کنه میزنیمش، الان لبنان رو با خاک یکسان کرده و ما هیچ کاری نمی کنیم.
ما همش الکی تهدید میکنیم اگه فلان کارو کنن مام فلان کارو میکنیم، خب چیشد پس؟ یه بار به دشمن نشون بدین که ترسو نیستین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/125427" target="_blank">📅 07:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125426">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نیروهای آمریکایی از هدف قرار دادن سایت‌های رادار نظارتی ساحلی ایران در قشم خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/125426" target="_blank">📅 06:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125425">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUhEqiyG25yBCk0Jb6m0U-TpxiUfSFeAvUxvCplNHyephN9J67qcIllwLszGQ2e1_2NVaA2HJVvPZ3YkaTiGVk3xEYE--XStWzxn-lxVvQjMAmTykWxLplOzh_u0WUbhE02eP_K3QDwSkvsmTASfdAqqvvSZyWDaa_78Tya3qchMHc7YrjfvHhZuI6gedy6nseDwxIl5mPh2xDmY5LrIcTb9V9cBo_vClQ04MiU4GHt3YQPUuPdLk2vp0vIKDleuqfFEeQyCBMFZla1SoN7ug-ImmCKApXlHdJwZtBxFV68wRhK4_QIZm8-ckcexE9ppFLEj6cgE2lImlX8cj2Zwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">​
🔼
کسب درآمد از فروش  VPN
هنوزم ممکنه!
درآمد چندتا از نماینده‌ها رو ببین
👀
پنل نمایندگی وی‌پی‌ان گذربان، سریع‌ترین و
راحت‌ترین راه برای پول درآوردنه
✔️
​
🤑
چرا پنل نمایندگی گذربان؟
🚀
سرعت و کیفیت بی‌نظیر
⚙️
پنل مدیریتی حرفه‌ای
💵
سود عالی
⭐️
بدون ریسک
​فرصت رو از دست نده و کلمه «الو» رو بفرست
👇
@GozarBanAdmin
@GozarBanAdmin
@GozarBanAdmin</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/125425" target="_blank">📅 01:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125424">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ به ان بی سی: خیلی از مقاماتشون هم مغرورن یه سری کارها هست که هیچ‌وقت فکر نمی‌کردن مجبور بشن انجام بدن
🔴
ولی الان مجبور شدن، راه دیگه‌ای ندارن و این قضیه زمان می‌بره
🔴
داریم درباره ۴۷ سال حرف می‌زنیم که هر کاری خواستن انجام دادن
🔴
توافق اوباما با ایران خیلی بد بود و از قبل هم عملاً تاریخش تموم شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/125424" target="_blank">📅 01:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125423">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ به NBC : وضعیت برای اونا واقعاً سخته
🔴
یه جورایی استقلال زیادی هم دارن، ولی سال‌ها با یه رهبری ضعیف و بی‌اثر از طرف آمریکا و بعضی کشورهای دیگه طرف بودن؛
🔴
طوری که عملاً گذاشتن هر کاری دلشون خواست بکنن.
🔴
من فکر می‌کنم خودشون هم الان باورشون نمی‌شه به اینجا رسیدن؛ جایی که عملاً خیلی ضعیف شدن
🔴
این موضوع باید خیلی وقت پیش حل می‌شد
🔴
توسط رئیس‌جمهورهای قبلی یا کشورهای دیگه، لزوماً هم ما نه
🔴
ولی واقعیت اینه که دو بار تا ساخت سلاح هسته‌ای خیلی نزدیک شده بودن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/125423" target="_blank">📅 01:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125422">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ به شبکه ان بی سی: رهبران ایران چاره ای جز رسیدن به توافق ندارند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/125422" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125421">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb22b3119.mp4?token=a5AuyzsNBGpJToA45sj3loWSR2TXesdianYJOmjZA3frKgDb-rUeitzMZYniP8XeULGL_D7-oV-oJqL_1S88l450liMycVlRiAfFgs_HezI6gxjpYtDhaZrgi9ltfutHkPXYYiYjFU_iIl-We6VzpU_DvQfUl5LXnfkZQwVMPLENHdHXyQ5GcWTvTq0-WnhcQ4iIbll1m_WmWc2x9NYC6-eMV9lDL0H1xkzqNUdBm7sqFsNtjvApVf76euJk267M1JGK_bWSsxjkaxrNNjSbsH2pAho49is7_GbtLr1_Il79ZWKcTlY03Jtv-4vjfa2sGAABkDNnBmyeLzoE7OJ2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb22b3119.mp4?token=a5AuyzsNBGpJToA45sj3loWSR2TXesdianYJOmjZA3frKgDb-rUeitzMZYniP8XeULGL_D7-oV-oJqL_1S88l450liMycVlRiAfFgs_HezI6gxjpYtDhaZrgi9ltfutHkPXYYiYjFU_iIl-We6VzpU_DvQfUl5LXnfkZQwVMPLENHdHXyQ5GcWTvTq0-WnhcQ4iIbll1m_WmWc2x9NYC6-eMV9lDL0H1xkzqNUdBm7sqFsNtjvApVf76euJk267M1JGK_bWSsxjkaxrNNjSbsH2pAho49is7_GbtLr1_Il79ZWKcTlY03Jtv-4vjfa2sGAABkDNnBmyeLzoE7OJ2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله تروریستی به یک پاسگاه پلیس در منامه بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/125421" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125420">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/125420" target="_blank">📅 01:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125419">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پرواز جنگنده‌‌ها تو جنوب عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/125419" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125417">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: ما خیلی سریع از ایران خارج خواهیم شد و نتیجه آن، به هر شکل، بسیار قوی خواهد بود؛ چه از طریق یک تکه کاغذ (توافق) و چه از راهی بسیار سخت‌تر. شاید حتی راه بسیار سخت‌تر، آسان‌تر هم باشد.
🔴
اما ما از این مسئله عبور خواهیم کرد و قیمت کود شیمیایی شما به‌شدت کاهش خواهد یافت، درست همان‌طور که چهار ماه پیش بود. قیمت کود شیمیایی اکنون هم کاهش یافته است.
🔴
قیمت انرژی، نفت و گاز نیز همگی به‌طور قابل‌توجهی پایین خواهند آمد. و صادقانه بگویم، من تصور می‌کردم قیمت‌ها بسیار بیشتر از این افزایش پیدا کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/125417" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125415">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: محاصره دریایی که در حال حاضر علیه ایران اعمال کرده‌ایم، باورنکردنی است و جهان پیش از این هرگز مشابه آن را به چشم ندیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/125415" target="_blank">📅 00:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125414">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7514cef466.mp4?token=cE_0nhpcbmOq_ZKIlZiT0CDPOIC7E_ry-rscy8ZJE75N1lCuyW7D-g4pWQeWfqiuAOE-zJ1NCE8WAtkldf-wszV8F_7gu7Jm_aol_nU-SKi2a7E5KBGNhaGcX9FdDruu5yExaNm0b44SL2yDLxNKT5snY-uHbtwa-4OZz3Oqw4mFwhjnbLKSda09jp8ffOCDYM0oPUSBTSrayGf49yKxy9nLK_6WK7OnpKNnI4SUkTKcYBs3UXh8IgeqytNrj0bv9cEGXskox1tZtGCH0lUsZyXPJXQg6qX5k2aHFZEGwrHS16EAgSzrIqUOSUV4BEgVEKsZAZAWrKdBQb4xADKoqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7514cef466.mp4?token=cE_0nhpcbmOq_ZKIlZiT0CDPOIC7E_ry-rscy8ZJE75N1lCuyW7D-g4pWQeWfqiuAOE-zJ1NCE8WAtkldf-wszV8F_7gu7Jm_aol_nU-SKi2a7E5KBGNhaGcX9FdDruu5yExaNm0b44SL2yDLxNKT5snY-uHbtwa-4OZz3Oqw4mFwhjnbLKSda09jp8ffOCDYM0oPUSBTSrayGf49yKxy9nLK_6WK7OnpKNnI4SUkTKcYBs3UXh8IgeqytNrj0bv9cEGXskox1tZtGCH0lUsZyXPJXQg6qX5k2aHFZEGwrHS16EAgSzrIqUOSUV4BEgVEKsZAZAWrKdBQb4xADKoqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : این دیگه خیلی جنگ حساب نمی‌شه
- یه درگیری نظامیه، بیشتر شبیه تمرین می‌مونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/125414" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125413">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: ما به هر نحوی که شده، تا حد زیادی مسئله ایران را حل کرده‌ایم.
🔴
ما باید یک سلاح هسته‌ای بسیار توانمند را خنثی می‌کردیم و اجازه ظهور کشوری با حضور گسترده هسته‌ای را نمی‌دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/125413" target="_blank">📅 00:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125412">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/صدای انفجار در جزیره خارگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/125412" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125411">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX2NwzzpGwlBhQnwsUuckcVYstLFnT9-RH1OgogJb1zuqTx0SgnQPt9HMthNScgnToqQ72nwnfNssbbklNVq8ZRZy4NqoEFDmGZq06M-MPVxWifrLlNGebX_GUpjmPX17_Et5Y8P6RctQtLk5gJmjPX_DJ_e6komwUUJmKVSgsXeTr2CrDUYHrBRZ2M2-y8DjtJk2aUbHt7K5VKKk1dymyWR2THPDDvnziDZI5QZzKnTBfnp1FK03S7yVvK_drCb090TefZ773FwuNdoImnpYO2rmls9FAMebEpYyKvXzMYN7xst9cW9EvQek7LvSFAuHFJNIEjPiBL0r4nn5WiUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی جمعه 15 خرداد اعلام کرد که یک حادثه جدی در جریان عملیات مین‌روبی در نزدیکی نیروگاه اتمی زاپوریژیا در جنوب شرقی اوکراین رخ داده که بر اثر آن تعدادی از نیروهای ارتش روسیه زخمی شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/125411" target="_blank">📅 00:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125410">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNddW4oVBVrroyJZKCXnusw0eRRHkye9wtNamWrz-puZQDIVAfPkcLnaOZn0pblcWxYMIuga5NoeJWnjplnBz8PEFx-iDs4dK9xJV5UCSge0ZeyfaeIBCsARPYHko-5_ujX8KXZCnfONw8-XixwRtJmywx8Ehrg9uMZ-Icus1scRk3aqddtS3l6Gcd_3Xe7eAdzVyYLnWhUeELpaBoB6THJLBq3TvOQ8ruPQCxT3JRdaACObjAaZaP8JB7D715SsYWX2Vt8b9aJWN9xfnwD1S_QXGqCU2ZPGrV9nMV5yy7rdRDNs3xZGZNKzsQkTrC1baMtU47TaPr352DAqBTMlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی طارمی: اگه تو جام جهانی گل بزنم، اونو به آقا مجتبی تقدیم میکنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/125410" target="_blank">📅 00:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125406">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exeD6ZItcQJlFL6X37NGTtIVSGB522TyGrp0D5mpbQad6657dYANy58dYvlAQlc81Y9SIvHIYzl7a91lkuGK8ScXG-x2aTqWoHoqcWl7my3IfRsCi16A4MeoA1sRLp5gqeUYEemd8nkxeeZA_MXhDpH7DeSFhyhZkwhyH6sn-aIzuAZ9zKbibDTiB-PHLE7ozrOtuU_qyzl46gSzX-B4t25k6pj_iWMl1HJ_kTUc4hZSigUyjZAr4_HGKnaMh7F368Q4W_d8MYdgbvV44zJ9DH1HkE9r9tlpt0LSNBdRmu7fagsztFd5u3IKPvCtfk6Gp8A18Q8cHpMhyhinAioHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvpO94rgwjiP_W8kih6eT1yC-GoeaJkbZ0oGygyH6ChREWurtsFuSbf-kmFocxdGz_6BkZbWQD36NRQ3XBYvEqhukCraODQOxb5abFvaeoFOvxelH9K5ns0cDKXEJn6CcSo4cu2EELaw06RIjYJPGvv8J8vPjy5fM-YhetjBQh_uTEG-E5Vr3rx2BzUafamMDpvCYxwVZKrVtQZr_gJkq4Y9C6Xl4Fob6PU0MvIYI-qmfGMvjvwsMMPWh6ae_-cDBwONk_NBrSlaq1lTHkL0SRGr13poR7Y7JaznpxM83kqk_99cOig9MMyVYBCNftEygEJFRNe8NRQxMDgSvRUiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAhfNy9MJmMOe995eg9wK_mQoIfj7VZKcM1JYaNRfioKB5Q1pfzDh341smNJSlcJvHIJnhsJL89lffrIhlBylK94FCkQPkj5BBx1WHffZdVbE8vkdLUnihBTMAXMeWXt1_d373Wk19d7QIhUM211LKvgWWpDfLhGlIxxeOnwZFiwpj5HhJC6DcqPzF0aphh3vGY7zS1lRdD8I-iE-ulVERqrYRLa9oZ5c_FLmj2szXlilVy07a7rQ4V91EPGgVKmTbMY3c7fyBwDa8uTahvxEv4M8nGUHYlPXfBcigV8Jne223C3ltlUn326M3BaxeEweqxdKkNdnynQffVCfs1c_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDyAmo4XTJn8laRRjlt2qKig6W0soECBNccd4IvrG9JUaiBYlBj9NupQsftgGIhODzIMx3CgJwTil7O0ocKYwlgaq-s_1qUFyrmOLpWdaJ9yOTDXLVifbN7A3Dv7YkZ4Hv6eYMSpUP65vC1r7DZUWb8WSRtFuj64rhGTDsAE_WaktenThFWO-vpHEwCvuwBhhFdks6YtlGqdQ_0spLk3hZqo8r9zPloi_5kP11fs-1PqBCFT37z0B7Wv8nXD7H2QU_dwWtGz9QjIUb0tJA-ZuCswy3_03G31_-UT_Z38fwIzyTcrJdc-pVmsJJOTzFyC5LPydwJuOwiT4F_MeOY3fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صدف طاهریان، مدل معروفِ خارج‌نشین، امروز با یه استوری رسما اعلام کرد که به ایران برگشته
🔴
وی اعلام کرد منقلب شده و انقلابی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/125406" target="_blank">📅 00:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125405">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a13944d664.mp4?token=RG9WFnvKpETgo4jdi2_gnmwFL7UNhYQqhkC8IT-G8JwJTtso5NtY-Ck2JAVGYtO7uyk8zhTZWIPi-ZjM_0WlQ-4khiYj7nt6bfZTPyIYyN6TTGdl2FTsfAcsqq0haVGovO0p0u_5eIirkOSg0fsABuWcZ2Y-b5BcoGVGe97mWPd9v9jAKk4IEhOcqQrP46rfB1fTEExzu4pnqJrlf6-Qa_580AqzoGX5oY_LMSGWud0wwkJ2K_ErAcX9jgwV_PAieXseBtfff6sbisU-3eqzNG14jHyVhn95-ibpyMoNDo-NVk8NjgGLX_k7Vuoz2YAg1DLrWHv7s-HxuPXxWlGVaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a13944d664.mp4?token=RG9WFnvKpETgo4jdi2_gnmwFL7UNhYQqhkC8IT-G8JwJTtso5NtY-Ck2JAVGYtO7uyk8zhTZWIPi-ZjM_0WlQ-4khiYj7nt6bfZTPyIYyN6TTGdl2FTsfAcsqq0haVGovO0p0u_5eIirkOSg0fsABuWcZ2Y-b5BcoGVGe97mWPd9v9jAKk4IEhOcqQrP46rfB1fTEExzu4pnqJrlf6-Qa_580AqzoGX5oY_LMSGWud0wwkJ2K_ErAcX9jgwV_PAieXseBtfff6sbisU-3eqzNG14jHyVhn95-ibpyMoNDo-NVk8NjgGLX_k7Vuoz2YAg1DLrWHv7s-HxuPXxWlGVaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه فیلمبرداری از جنگنده نسل 6 F-47 آمریکا، این جنگنده هیچ حرارتی از خود بروز نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/125405" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125404">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: در حال بررسی امکان ارسال سلاح به تایوان هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/125404" target="_blank">📅 23:53 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
