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
<img src="https://cdn4.telesco.pe/file/nDNjPIM_DSd-c2uXfSExS60To_frAVbQuVV2HSLR40zzAk3urnJ_EAs4DOzoT13WKpisFyySxKR7fftxlwIARt9ROiV4lMQdi0m-OoI4TU5qlHKv2Nr3sa31yo8FycJqBu72hIbLIJQd2FwDYtVp7T36zJ7yEMXjYipyTqVgur1js1Fex7MeCrxoUhtct1njsqfj-CdOzUgv-fo0OxYUnAECy_uLT5VHyln_05Z0j2386DsShkeZEkKCOAkRxNNrpmDGq0qT9VwWmhXoSzpSalYc5LNVy2QuHgsDEp2NBUHoIWZR7uDTh7gM4lKbCGx2Dfu2E1QFifliRiV3-p_LBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 990K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 22:59:24</div>
<hr>

<div class="tg-post" id="msg-142711">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام‌های آمریکایی: نیروهای ما برای ورود و خروج از تنگه هرمز به منظور انتقال روزانه میلیون‌ها بشکه نفت، کریدوری ایجاد کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/142711" target="_blank">📅 22:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142710">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVZc5CWDq3XzkN9zzGxpPQTkOqfVPXZlezazZNahH0SkDXuag0-U_BCqK6jXKCfX_5jZC3VqypDTlFdj8eYYl5UMAYBWRh9CTlS1TY6biGSy6Yoq9LBbihXMYQvS60ri3OR0jhTqyosMSpyGow3qnmWdCB6XMYaAurS1pcposGdIFZLTseA7u5UrBsemHnwi1fBX4PzglmVaP5A3D89zTgGj8A1KZHAahYF9-zZeHDm8g_iPgUoTzQPm0tqcU4NZMYgT7c9Yhve22EU7ZT935bbV1PzzsPvelqtxEGVH1RBN_LT1_6jjrm_hUjdn-ykpGSwUCMaUkXjZKtruw3V15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی با وزیر امور خارجه موریتانی، در مورد حمایت از فلسطین و مقابله با اسرائیل و توسعه روابط دوجانبه گفت و گو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/alonews/142710" target="_blank">📅 22:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142709">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
همتی: هم‌اکنون صادرت نفت ایران قطع شده و نفتی صادر نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/142709" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142708">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یحیی سریع: نیروهای مسلح ۹ عملیات موشکی و پهپادی علیه تأسیسات نفتی عربستان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/142708" target="_blank">📅 22:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142707">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74ede774bd.mp4?token=fEvBtojaPnc3UkEaQT6-xtHxkmLIHHJ4iVIrzdhEIc8Im4U-B7ekTvJ6mccWWEsqJ8UZnGT3UsKFyMACpyZncC-a2EVpKwUiX56lk5fnmUhXZ8L5XkpoTUkv1cSj2cDfH6NY_5uFe3XHiuJK8Jxq6tJFkrIKC5Q4nojVg13tjzhanoEke7gF64a1sIRpOCcEThRYqQuKwJSMFxpQhpXAl7TEKpz4fCof-mfSNNVD8HyzhjzGpb7mtgjAm4PVHBPtQmofgSLxK64eLKnyb6kz-0bWr6NGCps0iuqY15fAO8V4_3Ro-5ifh4sWsW2MWXQqqDW7A2Vhog-3qcqZ0WaASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74ede774bd.mp4?token=fEvBtojaPnc3UkEaQT6-xtHxkmLIHHJ4iVIrzdhEIc8Im4U-B7ekTvJ6mccWWEsqJ8UZnGT3UsKFyMACpyZncC-a2EVpKwUiX56lk5fnmUhXZ8L5XkpoTUkv1cSj2cDfH6NY_5uFe3XHiuJK8Jxq6tJFkrIKC5Q4nojVg13tjzhanoEke7gF64a1sIRpOCcEThRYqQuKwJSMFxpQhpXAl7TEKpz4fCof-mfSNNVD8HyzhjzGpb7mtgjAm4PVHBPtQmofgSLxK64eLKnyb6kz-0bWr6NGCps0iuqY15fAO8V4_3Ro-5ifh4sWsW2MWXQqqDW7A2Vhog-3qcqZ0WaASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: تا الان پول‌های تعهد شده در تفاهم‌نامه پاکستان آزاد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/142707" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142706">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
بلومبرگ درباره سفیر سابق آمریکا در لهستان:ایران انگیزه‌ی چندانی در کوتاه‌مدت برای بازگشایی تنگه هرمز ندارد. ایران می‌داند که زمان به نفع او است و به همین دلیل، نیازی به ارائه امتیازات فوری ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/142706" target="_blank">📅 22:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142705">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزارت نفت عراق: از ابتداى ماه آگوست تاكنون روزانه بين يك ميليون الى دو ميليون بشكه نفت از تنگه هرمز صادرات داشته ايم
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/142705" target="_blank">📅 22:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142704">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfd0cd9fe.mp4?token=W8vYKFPnmqGppAEtk97q6lOwRcXSIZt2GY2scwPn2thgfOMthvbRfpwDxQ9P52hNnR8pDcc2evNUFa4DpWvYVxSNUnc8K5XYJEPgKqXmWVPYAbAoFOdbrDfDa5_8Tah9jAhoyH-K1SLJSQ7lCSP-YWsMFzt5CZW-IVmsiuag-fgQb86blmFyiWactQxU4mY85Ixb9Wl_yYcmw6jxTotRqqFpJ98jX3nozIiZJWvAUXFauMxjScVqZblMnuj5VrBb_ziOiijE01T4FH5xJ_NWxP7j0c4KXV1Kho8ZEvA9E8YNvF0frl-yy7xwIsOfazJsM-KDmwZLE4z-D6UfR59fBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfd0cd9fe.mp4?token=W8vYKFPnmqGppAEtk97q6lOwRcXSIZt2GY2scwPn2thgfOMthvbRfpwDxQ9P52hNnR8pDcc2evNUFa4DpWvYVxSNUnc8K5XYJEPgKqXmWVPYAbAoFOdbrDfDa5_8Tah9jAhoyH-K1SLJSQ7lCSP-YWsMFzt5CZW-IVmsiuag-fgQb86blmFyiWactQxU4mY85Ixb9Wl_yYcmw6jxTotRqqFpJ98jX3nozIiZJWvAUXFauMxjScVqZblMnuj5VrBb_ziOiijE01T4FH5xJ_NWxP7j0c4KXV1Kho8ZEvA9E8YNvF0frl-yy7xwIsOfazJsM-KDmwZLE4z-D6UfR59fBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: مشکل پول های ما در بانک های عراقی حل شده است و به تدریج بهتر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/142704" target="_blank">📅 22:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142703">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy4trCp7nxptTLROi3LnV6f2WPWffxxypnbaaemA2cAi5kgQkNItAYmfFwc2N27-QDnCH5CyEcAChbda_m0lfOMd7vn_KPoOq9fFxoKkA18w5gSs5rCWYlQ7nCt8j69s3QVuuP6VL5vTbQ4AHUm6FFnLN1vgkpeYfGAIBpv05QRghwkKRoHctxlbkjkDklN0z3gsSHvStB_0YB2NYx1E7HPy0CCHNbvkELX972UQyPY-kcgKgVlv088ENRNJZElrBg3531azIpP0JQprTHQoCfq7Sdy5GHe6_7VL_5cLXVaLmwfr2blLUduf09ack5NFWjlP1ioK0L5-fj10aaGniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما رسما دیگه عکس آیت الله خمینی رو حذف کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142703" target="_blank">📅 22:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142702">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e789ecd273.mp4?token=Qy2OzaoRUUe11rFQtGLYaBZDjjQ45pUG2aRIgx1To6xNSOYr-jsjNx5OswpS25dMhg5FSsV8JtFMGFqRr3V544BrDIywJwQAiWa820Eah50TVIZszawBrlhbH2Rvls2eGefUw8Jc2qsrKniP8GiflOutjrnGVdR6C2-Eeqn3BtEn1IbMmjBVZlzO0a0hea_38cD4MuG_qfFX5qmj0SfY8qMeYqut99oJ1W-DR7652y-V98-zWP6jaj7CmkwVF1-Yx35cBtF7Rxz0cDbKwUUSf1-ORsoy-1xIkYJxkfF4eCo3Q4muDQncd7HK5udbfrrRrBe6BSEdPBGJmw9JH85ZHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e789ecd273.mp4?token=Qy2OzaoRUUe11rFQtGLYaBZDjjQ45pUG2aRIgx1To6xNSOYr-jsjNx5OswpS25dMhg5FSsV8JtFMGFqRr3V544BrDIywJwQAiWa820Eah50TVIZszawBrlhbH2Rvls2eGefUw8Jc2qsrKniP8GiflOutjrnGVdR6C2-Eeqn3BtEn1IbMmjBVZlzO0a0hea_38cD4MuG_qfFX5qmj0SfY8qMeYqut99oJ1W-DR7652y-V98-zWP6jaj7CmkwVF1-Yx35cBtF7Rxz0cDbKwUUSf1-ORsoy-1xIkYJxkfF4eCo3Q4muDQncd7HK5udbfrrRrBe6BSEdPBGJmw9JH85ZHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی اسلامشهر تهران؛ یه مادر و پسر گدا رو گرفتن که فقط تو نیم ساعت ۲ میلیون تومن پول از مردم جمع کرده بودن.
طبق گفته این زن روزی ۱۵ میلیون تومن از مردم گدایی میکردن.
ماهی ۴۵۰ میلیون تومن درآمد داشتن. بهتره بریم‌ گدا شیم.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142702" target="_blank">📅 22:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142701">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/142701" target="_blank">📅 22:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142700">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
زلزله ۴.۲ ریشتری حوالی گیلانغرب را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/142700" target="_blank">📅 22:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142699">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751a5db559.mp4?token=RT3Ru8q2i4dXwoV67WGYtqbWGzO6MpeKMe4WYZFfH3W8JmBqNWmgj5-MwTZmkwkRTHRax-BdEs0jH_D55L0uImwtPMlxzV_9RW5DhjwF6wsiCt9DMyF_9z7KWnGCpL3uneHYNITMCFy4QxcgVsVd65zjH4qI7IaJb_jLx4XnkmAQjObqcavVXuK6PEsNIcZN7L1xU-G7ach_iblsothUKbPQzSWy8DYFC38Qh2gzDVJA_OFH2maqtltgk0DUuUObGD8Ww_OxGq9AqghYLVYC15_BcMURxwtnmf8gJxPTj-qiExMGfYVjGG3dD7Sr0TQwO7zcJ-82nUJaMenOqyqrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751a5db559.mp4?token=RT3Ru8q2i4dXwoV67WGYtqbWGzO6MpeKMe4WYZFfH3W8JmBqNWmgj5-MwTZmkwkRTHRax-BdEs0jH_D55L0uImwtPMlxzV_9RW5DhjwF6wsiCt9DMyF_9z7KWnGCpL3uneHYNITMCFy4QxcgVsVd65zjH4qI7IaJb_jLx4XnkmAQjObqcavVXuK6PEsNIcZN7L1xU-G7ach_iblsothUKbPQzSWy8DYFC38Qh2gzDVJA_OFH2maqtltgk0DUuUObGD8Ww_OxGq9AqghYLVYC15_BcMURxwtnmf8gJxPTj-qiExMGfYVjGG3dD7Sr0TQwO7zcJ-82nUJaMenOqyqrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: تاکنون چیزی از پول‌های بلوکه‌شده در راستای تفاهم‌نامه آزاد نشده ا
ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/142699" target="_blank">📅 22:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142698">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وال استریت ژورنال: دولت ترامپ نگران است عمان به ایران برای رسیدن به توافقی که بیشتر به نفع تهران باشد کمک کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142698" target="_blank">📅 22:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142697">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWJw3Ab83NH0-ACNu_6viE9SX9KI7uCBsmcvXFyjaOJwy8Qf9F9dCJaIvCxap_VkC_bEzglpV_ealdhSzioeIlLbEuvj9gc8SGQr1jhzedQuez6NFQ1QDXvycIMmIq-4a6WB_12Oq9YmVtEJujdOu22bto1h-OO1oTPcFwfcphf0V1f6grFPskFDbiaMqeHr7_xr_2QUj9Vd4_8aR4bXvYYdQBBrOGxQhdmfMY-29gt8xozdoexhhCjSchxzn4CYmANHZm4aWSBYL0_N2MvVmeo7D8W5gxnedrXKyiR99BVlZ-1w3p1FCGhkk9ILO4D32bcUSMP-M9dTMO8kOcgEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت معناداری که قاليباف منتشر کرد
🔴
پ.ن: تنگه قالیباف
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/142697" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142696">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66593eb30b.mp4?token=ID0UR9UDFch_0_kvRDNCSKdUP8kGsPFTOns5B77y-LcHjtWSXyxbUgyTCBvCd4yiPNVlUTaFYe8cQxlN7jIRP03hUa1TLb1vUbxYYMydqqeUT7kUDfQ9SB2CxlCYSxBptV2XTYgtBFFluzdFBggcQe7X1K6Cz582XDVgtyw2-SkVdAXW2ujiAYb0Pq80ikVRucQyxZJDwIE__TRgbrjut4EyXFSkVHjHCbx4TIDAGT2Kg7P2PFmpAJJaODo7GNCpWe1Ky0Lw9e9vSM_QdnM9Wg4Ga6i-uAZb_w2wwcHv3H1ESrsGBpXyBc0_FE_A-Gn-MHqoVip4gLsSqP7jScFdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66593eb30b.mp4?token=ID0UR9UDFch_0_kvRDNCSKdUP8kGsPFTOns5B77y-LcHjtWSXyxbUgyTCBvCd4yiPNVlUTaFYe8cQxlN7jIRP03hUa1TLb1vUbxYYMydqqeUT7kUDfQ9SB2CxlCYSxBptV2XTYgtBFFluzdFBggcQe7X1K6Cz582XDVgtyw2-SkVdAXW2ujiAYb0Pq80ikVRucQyxZJDwIE__TRgbrjut4EyXFSkVHjHCbx4TIDAGT2Kg7P2PFmpAJJaODo7GNCpWe1Ky0Lw9e9vSM_QdnM9Wg4Ga6i-uAZb_w2wwcHv3H1ESrsGBpXyBc0_FE_A-Gn-MHqoVip4gLsSqP7jScFdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین، پالایشگاه نفتی "اوفا" متعلق به روسیه را مورد حمله قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/142696" target="_blank">📅 22:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
عربستان: امنیت دریایی همچنان اولویت اصلی است؛ هرمز و باب‌المندب باید بازگشایی شوند
🔴
همچنان به تلاش‌های خود برای کاهش تنش‌ها و جلوگیری از بازگشت درگیری‌ها ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142695" target="_blank">📅 22:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bfb45f45.mp4?token=b0PaB4-dYVu0qpKtZdfTwQ2i4aVVR6EvKQMCorwKfZaIAv4nPUdf_hyCOkHEJupqSZ-04njGs0fZl1ZHHH7Fikl8fV7e9C6uzEkLuIJ5iQxxOdnEqVHMej3hWl1TIgPUDrrcKUnro49BGozZv18syxrkYw84GV6ve6MbWvXJOT9FICJIz9lmgrikgrpk2Q-xVHFz_S1vDISref1_fZwFHo3an86bI3kIT0VqcAegIcBZm4dBV2SZ7xNisixH5ybd-zm9N691QFuPPRpT6VPIAFMH-NGZmBGNya1infya4vBQAe6rz6W_gPwB0Rp8Yg8sBGTQSQQhoVY7kmz-xiE6vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bfb45f45.mp4?token=b0PaB4-dYVu0qpKtZdfTwQ2i4aVVR6EvKQMCorwKfZaIAv4nPUdf_hyCOkHEJupqSZ-04njGs0fZl1ZHHH7Fikl8fV7e9C6uzEkLuIJ5iQxxOdnEqVHMej3hWl1TIgPUDrrcKUnro49BGozZv18syxrkYw84GV6ve6MbWvXJOT9FICJIz9lmgrikgrpk2Q-xVHFz_S1vDISref1_fZwFHo3an86bI3kIT0VqcAegIcBZm4dBV2SZ7xNisixH5ybd-zm9N691QFuPPRpT6VPIAFMH-NGZmBGNya1infya4vBQAe6rz6W_gPwB0Rp8Yg8sBGTQSQQhoVY7kmz-xiE6vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش همشهری از جنایت هولناک اتباع غیرمجاز در پارک نهج‌البلاغه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/142694" target="_blank">📅 21:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
روزنامه همشهری: اروپایی ها از گرما میمیرن ولی ما گوسفند هامون هم کولر دارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/142693" target="_blank">📅 21:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سنتکام می گوید نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۶۵ فروند شناور تجاری را تغییر مسیر داده، ۳ فروند را از کار انداخته و ۲ فروند را سوار کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142692" target="_blank">📅 21:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyA74iopmOGIqhrFAgOSzO2MyTi4mfzQW1SL2I_3789q6VhjOIUlRqYI4BwqH1W9XucW4pWgPkKdrjh8OG2Rg4JEliSIIUPL7WrUU21mvDKAqesPPBsYuXJCh_8Aw105bW1Pwn8gfpddzJx17YmbvvZW36T1MVv1nLBXQkA334DCaG2UTza2SEDY1ZHCzoP4QnBB1zxiEiBoMTn8Ui-UUjc7wknlYRHYAj7cYtCPzn0lEqQXNWC0uOjkyqTQ4xvBOxHfGzFDIULUTJGWu9WIbPQPMrGPH2h0cm66UgZJrOWwtqHyME85tlVKrNoJ32RUVJeDm59aXlDUCxsW_msduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa62ad9d6.mp4?token=iOgvN6XBt44KQ6PHe2uqVVuSH0BLX6CkeEdf6f7Vh3QK13A3rm_FO_EuZiTxxCkjj8QhKagqbP6wsQgSEwZpE2VaiPdpzV42tZnoA_Akc3p_lRXchTGT2PIuGJph1rn_F4wgo3QD7ZLfcuSKjRGT0SwjlQHgWwpVU7wZ0rHXQ5l5bicoicZrg_xtA0wYzrQxU-6Kz7xHjLUZYfc-1UHEDM9K4Hv_DJWtcxT8n3ovUo8rNfRox8GnCbs0-H21qeOA4WyJTbYqK3dSGXX3ja8TDO_q1XVqexNxKLRyxiX3mvufFWnmsovVKVczJdnxL1xPo-WC8ZAne0WpOk7zbHaymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa62ad9d6.mp4?token=iOgvN6XBt44KQ6PHe2uqVVuSH0BLX6CkeEdf6f7Vh3QK13A3rm_FO_EuZiTxxCkjj8QhKagqbP6wsQgSEwZpE2VaiPdpzV42tZnoA_Akc3p_lRXchTGT2PIuGJph1rn_F4wgo3QD7ZLfcuSKjRGT0SwjlQHgWwpVU7wZ0rHXQ5l5bicoicZrg_xtA0wYzrQxU-6Kz7xHjLUZYfc-1UHEDM9K4Hv_DJWtcxT8n3ovUo8rNfRox8GnCbs0-H21qeOA4WyJTbYqK3dSGXX3ja8TDO_q1XVqexNxKLRyxiX3mvufFWnmsovVKVczJdnxL1xPo-WC8ZAne0WpOk7zbHaymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای ثبت شده امروز حداقل پنج دهانه برخوردی از حمله هوایی دیروز اسرائیل به پایگاه هوایی ابوالظهور در شمال غربی سوریه را نشان می دهد.
🔴
به نظر می رسد سازه ها در بخش جنوب شرقی پایگاه، از جمله آشیانه ها و انبارهای ظاهری، دست نخورده باقی مانده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142689" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عراقچی عصر امروز با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان به صورت تلفنی گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142688" target="_blank">📅 21:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: هیچ سلاح هسته‌ای علیه ایران به کار نخواهم برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/142687" target="_blank">📅 21:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان: مذاکره به معنای تسلیم نیست
🔴
در جهان کنونی که شاهد زورگویی و قلدری برخی قدرت ها هستیم، ملت ایران و نیروهای مسلح با جانفشانی، افتخارآفرینی کردند و دنیا از این پایداری حیرت کرد.
🔴
اگر چنین حمله ای به دیگر کشورها صورت می گرفت، به فروپاشی می‌انجامید.
🔴
کشورهایی مانند چین با رقابت اقتصادی خود را اثبات می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142686" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyTV4M58sAPcwix75D_boIufGx6mBFRyWF1GDFFw1Zc7ZtMqnxz1cjqWayQ4XjOjbKxwaDIiyv5lrLYs_5dmO7cwAaFHkHCKtrTzsi9_W8ES-VELaWHDjpGDcXWeFMvKc96tMYEqjUhz8J974VOh4efMvaUrwvWQG4MHSUEHCNH2X34kXxR6tgEkC2-0L2W0HWUXPwdWZM6mUCI9IaA7iS_uKYr0rilYGv4kboQAOwbh_xlTXGtJy_s7flFmjozDv2GArD6n8D-FqKbxepl95BQ-mz39QE5rBV3__ZwpHiwVJi6uuvzKWDSKrqCOoiQLq4cAz51PScrhYS_-6kZiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل: ۴ فرمانده گردان بیت لاهیا حماس را در غزه کشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142685" target="_blank">📅 21:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh0QvmT88QYcpNH4bwMPIqE5jTroaXRoyvvEsThq9cmt3sWecfXAMY-KkAcqxPdxcbYacEXzouGiZYkR0pT8Fz3kbLsh2YEUEmoi9-4gwmcg7INlPVgROmx6iCSa0CRg501rk6n6lhCn3h8DaJddl_1oqMp0b41ogFzuepdhBLcV-lNFfoN2Ws88QA0U7KQFj06kcBuG5bdEG6g716ltU9xTsmfc-GcqtcAyXyQ_3lxKXuUN2KP4z5Pf91w4NlyYnfF1nNYzBwa4Z7a06CzwljVGrWfYU61y2vbY-v5vR1ZS8N5FO23gq-OyX5TBDzhJxIVIE8if0mQxM8NYhx4n1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت معناداری که قاليباف منتشر کرد
🔴
پ.ن: تنگه قالیباف
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142684" target="_blank">📅 21:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StXnv_6jEZEQdXulNaHc6bSMPTLkiWKB-eta4BC0FnoQP_ZmQvtdj7dImwl9pD9Zk0GtPfNKaUWJ0k-60oeUcx9FGFjm9PYEpRQVccM9y9Mv60K1lIJuf9bugV7wtw_rh933IAl7qESVWUSBRwhdGdxDziu50cD2vpzHY-7tL4kKK1YzrOwqSoCdVoaYht4kTprrqqvotH1av5h1EpLu23y3Ts_61gyqEVuIGZg3yiOagIVzpgPt7GJOfQAStEl6J8NTOC8k6MHbNchMukDqaVvsr6WL-5TIpjGdehTGFeHqb2wzuBBWTJtw54LGZIqXMjut3HQRftMIRElyap-jtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ‌عجیب ارزش بیت‌کوین
🔴
فقط در ۵۰ دقیقه ۴,۴۰۰ دلار جهش کرد و برای اولین بار در بیش از ۲ ماه گذشته به سقف ۶۹,۷۰۰ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142683" target="_blank">📅 21:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نتانیاهو: ما شاهد تلاش ترکیه برای استقرار در سوریه بودیم و به همین دلیل حمله کردیم. این یک پیام بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142682" target="_blank">📅 21:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy6RBW4ylAMpENB0rM0773LZ8jiMk8X1cszkN9iVQMynykIvp3IGvdmg_vktkUakTK2iu1IIRN3JdMAnVdSwMlRaLz8qFL6pwQnUl0GRoaI-tVBBGHms2qzMjf0Ihe9N6l-htg03mVSF6kKBH4HyNvHITm0NYAFBlRh5UOB7ItzwMAGUMR7OG6wgT_W0O46800y2reKkWFspwipncHQvWOd2iCNfkOpyGxu8w7XOi-2fYAIBRfjbZQpJmdJHMLZAT4GaB41Gf0O0IKbD6Zx_BQGQp-rIbOU0HSCHMsYrRuc4L-exftkUObBrbaN7G8lrdqnTZHbZYwqafx6Rjeojwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر کانادا، مارک کارنی، می‌گوید که کانادا «در حال حرکت به سمت یک توافق» با ایالات متحده است که شامل «تضمین بهترین شرایط در هر یک از مهم‌ترین بخش‌های راهبردی کانادا و ارائه اطمینان بیشتر درباره آینده روابط تجاری ما» می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142681" target="_blank">📅 20:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نقض مکرر حریم هوایی یونان از سوی هواپیماهای نظامی ترکیه
🔴
روزنامه کاثیمرینی: مقامات یونانی اعلام کردند که ۴ هواپیمای ترکیه ۱۲ بار حریم هوایی یونان و ۶ بار منطقه اطلاعات پرواز (FIR) آتن را نقض کردند.
🔴
این نقض‌ها در مناطق شمال شرقی، مرکزی و جنوب شرقی دریای اژه ثبت شده‌اند.
🔴
یک فروند هواپیمای گشت دریایی سی‌ان۲۳۵ ترکیه مسئول ۶ مورد از این نقض‌ها بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142680" target="_blank">📅 20:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU45FTj3hDLQ2RauiTEB1TGqsu4AM9kVzIHbMQ3BSSNohjJth5eNp5OYg4Tzz3jshmYhCcC0EC3wjzLujY5yuM60cWGsw_bl43ke-6P0oTOkZHFQodLf3NkoFttxLnRCVKPot41YDDgzu6qCI6pmiYto6B6ShYXipkiSakwS9E1esaJrKLSTjtSJHBYe912g3SahTkIHVUg2u4I9p8OJgu6WoId60S4D6_oI4zuUBzsdBSgtiGoaeOVd_I5HvcNET7qJeJtXWHUUwlE1GjzUXv3pMYV7CpGMNqEiHwOpusxvFTzJkFB3qf_kZ4Rvf0GqBydkeBNZhoQnBWRVUOZDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های رهگیری کشتی‌ها نشان می‌دهد نفتکش LPG «مایتی نویگیتور» که از سوی آمریکا به دلیل حمل محموله‌های LPG با منشأ ایران تحریم شده است، پس از بازگشت از سنگاپور از تنگه هرمز عبور کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142679" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گلف‌هاوس: کشورهای خلیج فارس از پایان جنگ به شکلی که ایران را قدرتمندتر یا تهاجمی‌تر باقی بگذارد جلوگیری خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142678" target="_blank">📅 20:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نتانیاهو: ما شاهد تلاش ترکیه برای استقرار در سوریه بودیم و به همین دلیل حمله کردیم. این یک پیام بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142677" target="_blank">📅 20:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خارجه قطر: نخست‌وزیر و وزیر خارجه این کشور با وزیر خارجه عربستان سعودی در ریاض درباره تلاش‌ها برای کاهش تنش گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142676" target="_blank">📅 20:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80174ee807.mp4?token=mXGZPz5YC4ZHGupB8ssvoLaea8dOQFZT3tqgrycehRKh3OLUPonteqBzdwBzssYg50VWrzMoQ7ZpgsAzSerfSQm8wSeRouMKDXAY1SZzAr3sMdttEEud2u5wor8Wxx9KiWt_E9YejLjPbLi6IMlgr0ulJ-LW3dk-cgnyy7pFwqPAO0wsxFX4xcgugM9gSvaZvrl2vnwewTaSGSI-ZSfGBPoirEXVg5614wU6Xzr-hj3xjFszyGnDJcdOyHReRXHgFPPBA1m6Yd-dAkeCBOj_zMX-QqYiFN_BgonhkWU1WRhq9fyBMlb0xLbo18a8hLWaTR4MJ1QaB8zJBCe-r74ecg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80174ee807.mp4?token=mXGZPz5YC4ZHGupB8ssvoLaea8dOQFZT3tqgrycehRKh3OLUPonteqBzdwBzssYg50VWrzMoQ7ZpgsAzSerfSQm8wSeRouMKDXAY1SZzAr3sMdttEEud2u5wor8Wxx9KiWt_E9YejLjPbLi6IMlgr0ulJ-LW3dk-cgnyy7pFwqPAO0wsxFX4xcgugM9gSvaZvrl2vnwewTaSGSI-ZSfGBPoirEXVg5614wU6Xzr-hj3xjFszyGnDJcdOyHReRXHgFPPBA1m6Yd-dAkeCBOj_zMX-QqYiFN_BgonhkWU1WRhq9fyBMlb0xLbo18a8hLWaTR4MJ1QaB8zJBCe-r74ecg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از لپ‌تاپ دوربین‌دار شیائومی با قابلیت‌های عجیب!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142675" target="_blank">📅 20:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
به گزارش خبرگزاری آفپ، بیش از ۷٬۳۰۰ مرگ اضافی در فرانسه در طول گرماهای شدید این تابستان ثبت شده است.
🔴
فرانسه از اواسط ژوئن، رکورد ۵۲ روزه شرایط موج گرما را تجربه کرده است که بالاترین تعداد ثبت شده از زمانی است که پایش ملی در سال ۱۹۴۷ آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142674" target="_blank">📅 20:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8faf3df15d.mp4?token=m5tSRE5s9vL0-jejAqEs36TbJFqWe6pPhkDG0qF59tVjqO-Qb_RkCWMSbZO7vOZWXnRl0ycX31kcIyE7G2wcGMJU-PdX-iHTDPcoWl367uvxdV_xRtZyWsp9Y1MyBJcOkeQzy7IVJ1Gi07plKQh1khj9bS2rFFVMf_JufJ-bEGqJuhz4lGGZgSFRfp_KSi_9z6fHja3zvQ92SwE9-P9xjsxPFUv8z78NZ-UgypnokN2Zr6mbOwyQVeb5BqpA5BNfPb4j-0erqzimk1qNZX7qd4D33iA3ox-eVFcJxw8TnPxw_5dboE073mJhJRYYma8ivaLuyu2kH3h8RBdDOCpQYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8faf3df15d.mp4?token=m5tSRE5s9vL0-jejAqEs36TbJFqWe6pPhkDG0qF59tVjqO-Qb_RkCWMSbZO7vOZWXnRl0ycX31kcIyE7G2wcGMJU-PdX-iHTDPcoWl367uvxdV_xRtZyWsp9Y1MyBJcOkeQzy7IVJ1Gi07plKQh1khj9bS2rFFVMf_JufJ-bEGqJuhz4lGGZgSFRfp_KSi_9z6fHja3zvQ92SwE9-P9xjsxPFUv8z78NZ-UgypnokN2Zr6mbOwyQVeb5BqpA5BNfPb4j-0erqzimk1qNZX7qd4D33iA3ox-eVFcJxw8TnPxw_5dboE073mJhJRYYma8ivaLuyu2kH3h8RBdDOCpQYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیدمحمد خاتمی: با بستن اینترنت کار درست نمی‌شود
🔴
فقط میل به استارلینک و خرید وی‌پی‌ان زیاد می‌شود
🔴
امیدوارم آقای پزشکیان با شجاعت و صراحتی که دارد این مسأله که جزء وعده‌های ایشان بوده را هم حل بکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/142673" target="_blank">📅 20:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2119b5365.mp4?token=grZxG43pNq7b6ypTwuSKamn7buSVziTxLTu8jfRmD7zhrC2P9joFRtIyxZ4lniVXGs02KKDuQ6TQaORuYFIMvKFosLsj_dqlEx_5zikYWaDPUx8y8h599Jrwh65uzCsSBSOPgFDvvpNDv64jyBm4q1AwmrnIyTR6bAyHBtuDbJHOR8ahCIIsieapVB43RbVXCitkkGz22A2R5qceM9vV5PhWqSXhmjCB2XsGHdXIySJxjgzuZlkiK8rDQpD6QdiMwwJXwx7gsKREkOR_XiTIfzRfKqpY17Z4Fr4Aimkx7p2qbE774Ttp9kjWWrAfnRHu9k_yJ3DWPJChpuZgWv3m0qJfun-eHyO7mBZ1KFYgJNzAmN-DmkaYsvTOKF22uRYetfT20m6S26v3hQbcqf8gY-NV75v03iYa4Iwry846hlt6W0Wr3wxAOwaTS2-iJoYf2iP2j-gdre-Xz9gBxkZWidwG9weiVIY6spaaIzQVJbfllc4Y8YwI9kJAtyEQfYG14oL2zLufr6V9ENyhmL45eVkCdPXBZA-wgerLl5bF-NOiuoJzXruWjZHD6WBYNSrRjKcfHB5rqmk7daoIwArOOtMRhd_xA9ZRGkHw7T8MwnXzmxr9JU9BrPIWw12sfAW3cuIW90AHSawbBpcvBpQocadh7QmyX7279hUU1CgCbdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2119b5365.mp4?token=grZxG43pNq7b6ypTwuSKamn7buSVziTxLTu8jfRmD7zhrC2P9joFRtIyxZ4lniVXGs02KKDuQ6TQaORuYFIMvKFosLsj_dqlEx_5zikYWaDPUx8y8h599Jrwh65uzCsSBSOPgFDvvpNDv64jyBm4q1AwmrnIyTR6bAyHBtuDbJHOR8ahCIIsieapVB43RbVXCitkkGz22A2R5qceM9vV5PhWqSXhmjCB2XsGHdXIySJxjgzuZlkiK8rDQpD6QdiMwwJXwx7gsKREkOR_XiTIfzRfKqpY17Z4Fr4Aimkx7p2qbE774Ttp9kjWWrAfnRHu9k_yJ3DWPJChpuZgWv3m0qJfun-eHyO7mBZ1KFYgJNzAmN-DmkaYsvTOKF22uRYetfT20m6S26v3hQbcqf8gY-NV75v03iYa4Iwry846hlt6W0Wr3wxAOwaTS2-iJoYf2iP2j-gdre-Xz9gBxkZWidwG9weiVIY6spaaIzQVJbfllc4Y8YwI9kJAtyEQfYG14oL2zLufr6V9ENyhmL45eVkCdPXBZA-wgerLl5bF-NOiuoJzXruWjZHD6WBYNSrRjKcfHB5rqmk7daoIwArOOtMRhd_xA9ZRGkHw7T8MwnXzmxr9JU9BrPIWw12sfAW3cuIW90AHSawbBpcvBpQocadh7QmyX7279hUU1CgCbdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل، ایال زمیر، از خاک سوریه که در اختیار اسرائیل است، بازدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142672" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpnH97Ri8GwhVPGbBwi2K89CY-HcNJH_rrOCvjafHWRcPMolRlOfeH986C56IGRDZGwN366SnQrbn4TBLuwad0IgJ8aatEE46pckeUf5nDaEGMThCcDd1DVenfRVo6I-JZmA6vl0TRw61qMrkC9xAHAdSQ0DT5dl2p2YlsPZ9nt5D-PrdL6Fj3AlmVoZireSo1q81ebzDy2LY71NcEqtF1lf7at7HF1ZGo-yESn25Zz06kgGdTHb12-m3e9hnMIGSGXknsAJZTq0_4zqe8nXhdQ-nTrdTnVrmtxQ76hMH9Hc65SlNuu9xTj0FUSEem-1wdCmXgE4JQqggm_-Rhk_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهش ۴۴۰۰ دلاری بیت‌کوین در کمتر از یک ساعت
🔴
بیت‌کوین تنها در حدود ۵۰ دقیقه، ۴۴۰۰ دلار افزایش قیمت را تجربه کرد و برای نخستین‌بار طی بیش از دو ماه، سطح ۶۹ هزار و ۷۰۰ دلار را لمس کرد.
🔴
همزمان با این جهش، در مدت یک ساعت بیش از یک میلیارد دلار از موقعیت‌های معاملاتی شورت لیکوئید شد؛ موجی از تسویه اجباری که به شتاب رشد بازار دامن زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142671" target="_blank">📅 19:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rY9M0k1TO002bkru_lxRau545doTmxbiD65csnatX_Qko9I6dl4XKFUrmUOddq3P0W2Frj7ZSECX3uNv1gGnV-KG7bFdHFWZq97DD5Mh98B9nTbEufTjLzNq0nKR_fEVtStfArh-z-Pw0WryNb8do0jwEg6e2dWNeRmeA_FjuHnc9oeyLaz1Pvig1Naqs8dIZU36j9rORfNbSnzkRZgLvOnVDuUKErV6Ar18A6lMUkrbQdMDsO0zbIvDmjyg_oY_N5Wfq3bBV4EUElBAXJX_uUTMVVZ1v3VC-v2w_uonBi85NgLMW37K8l_4Ivk9CFOIDCz42x4FfglN_lyTdh44MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه عبری: ترامپ دستور توقف مذاکرات با ایران و حرکت به سمت راهبرد «خفه‌سازی تدریجی» را صادر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142670" target="_blank">📅 19:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142669">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قالیباف در دیدار با آمیدی، رئیس‌جمهور عراق: آمریکایی‌ها در حال حاضر در دوره استیصال به سر می‌برند
🔴
رئیس جمهور عراق: موقعیت نه جنگ و نه صلح میان ایران و آمریکا باید به پایان برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142669" target="_blank">📅 19:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مصوبه مجلس: ۲ تا ۵ سال زندان برای برگزاری، دوره ها، کلاسها کارگاه‌ها و همایش‌ آموزشی حضوری یا مجازی در ایران، بدون اخذ مجوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142668" target="_blank">📅 19:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
افزایش شدید قیمت طلا
‼️
پیش بینی قیمت طلا در روزهای آتی
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142667" target="_blank">📅 19:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142666">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
انگلیس فهرست جدیدی از تحریم‌هایی علیه اشخاص و نهادهای ایرانی وضع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142666" target="_blank">📅 19:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مصوبه مجلس: ۶ ماه تا ۲ سال زندان یا جریمه ۸۰ میلیونی برای مصاحبه ایرانیان با رسانه‌ها یا انسان‌رسانه‌های تحت مدیریت کارگزاران مرتبط با دولت متخاصم یا دولت خارجی که هدف تأثیرگذاری مخرب دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142665" target="_blank">📅 19:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142664">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
جزئیات نسخه جدید مصوبه مجلس: هر تبعه ایرانی که اقدام به اخذ هر نوع اقامت دائم در کشور دیگر نماید، از اشتغال در تمامی مشاغل و سمت های دولتی و عمومی، محروم خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142664" target="_blank">📅 19:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: مردم دارند جایگزینی برای تنگه هرمز پیدا می‌کنند. می‌دانید جایگزین‌ها چیست: تگزاس، آلاسکا، لوئیزیانا.
🔴
مردم برای نفت دارند به آمریکا می‌آیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142663" target="_blank">📅 19:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرنگار: آیا انتظار دارید که در اواخر امسال با کیم جونگ اون، رهبر کره شمالی، ملاقات کنید؟
🔴
ترامپ: بله، من با او ملاقات خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142662" target="_blank">📅 19:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731f523fc8.mp4?token=LRwoc5UiA1Ab8QFmtWRBXSN4C7wGUjwOkEqyiO9RCcB11e3d2dTQPOiRLVrv6ALoz90qgBr11Xq4QcedyED7Npc-jupnVS2u3hnOujvTMPy2RGRIFFv0R-u-TWvVzt29TbIXOnhTGNo7o-M7t-jlWADrqgH1MsHcvBXPQpXKPT5f_eL43ODeHgtTi3TjRztQD7Imo3w3BYcgpV81Vc9ecvGA0OkjXcrk0k8Dn8Bmc0QULTI0hs78fv9FKyaMIkW622cJfl_e3q3DwhHYPDPHxJCMqjMjV0XT0mW5PmFfkeTBagoBOklmz4SzFqsGrPPiP8EkF96PtVoLrh7ebuC2ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731f523fc8.mp4?token=LRwoc5UiA1Ab8QFmtWRBXSN4C7wGUjwOkEqyiO9RCcB11e3d2dTQPOiRLVrv6ALoz90qgBr11Xq4QcedyED7Npc-jupnVS2u3hnOujvTMPy2RGRIFFv0R-u-TWvVzt29TbIXOnhTGNo7o-M7t-jlWADrqgH1MsHcvBXPQpXKPT5f_eL43ODeHgtTi3TjRztQD7Imo3w3BYcgpV81Vc9ecvGA0OkjXcrk0k8Dn8Bmc0QULTI0hs78fv9FKyaMIkW622cJfl_e3q3DwhHYPDPHxJCMqjMjV0XT0mW5PmFfkeTBagoBOklmz4SzFqsGrPPiP8EkF96PtVoLrh7ebuC2ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
آیا انتظار دارید که در اواخر امسال با کیم جونگ اون، رهبر کره شمالی، ملاقات کنید؟
🔴
ترامپ
:
بله، من با او ملاقات خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142661" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1fc2e4d0.mp4?token=MDq5hCYBj5fvzBZ-kXvq9k1W4VEZaUckjKDrjEDKnXCv79y3Dd5q40WDy06EbDgaH7y0u8Q_liFPBbhNW-jUJiGQrzjiEMgJv0lZoE0KPtMuJlLnRof4mCG2AYET0PDdimtFlQqWByawK870LcXL8o1kFDwfWr15ihRipW8J--N1cDcuPzDEx_xacsdSm6sDVdQFCDlxU5dCbCLucLeZHNRcAit0qeccuBbOdKxejVtGffHesloIEge13IMUBgsCvUyvGwe4h2_FfY_04mTl12Zyq1tBhlkoorGvZx7NIqhK61GZxTA3gCGVfxspfZJhIQa1-0WaL2H62hSxMm5FLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1fc2e4d0.mp4?token=MDq5hCYBj5fvzBZ-kXvq9k1W4VEZaUckjKDrjEDKnXCv79y3Dd5q40WDy06EbDgaH7y0u8Q_liFPBbhNW-jUJiGQrzjiEMgJv0lZoE0KPtMuJlLnRof4mCG2AYET0PDdimtFlQqWByawK870LcXL8o1kFDwfWr15ihRipW8J--N1cDcuPzDEx_xacsdSm6sDVdQFCDlxU5dCbCLucLeZHNRcAit0qeccuBbOdKxejVtGffHesloIEge13IMUBgsCvUyvGwe4h2_FfY_04mTl12Zyq1tBhlkoorGvZx7NIqhK61GZxTA3gCGVfxspfZJhIQa1-0WaL2H62hSxMm5FLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره‌ تنگه هرمز: ما کنترل کامل و بی‌چون و چرا را بر تنگه هرمز در اختیار داریم.
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142660" target="_blank">📅 19:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c617cffdea.mp4?token=NDRxmspeN2pYtv2s3s2hpsvNsXr-Tvtdx4GHy8qJAMsC5y8iGPVWHTpgPk93sdCLxHLd3HT1RTwkJKO7MH85NO9XV_alsaVoGXFCnQJJd7pLRVZQVwmUvtGh6LCsa4GM9dDzTbMn86DHI3OMorlVc-n6XilWF3BGwH9mfcrKrLivEZN5dbKmiSbpoZDVgIP1FyI8LNcxLxrwKuFHTm2yW_hpWNIS1zWcJJ7GDH799xOLYilDDWM2DPqc1Peeq7tZrymPWrJDM70h6Ae7lPvbFDi7d9omVRLxuNbsqR5hZh2AtggnSr7dRK5m0tjg3_Qf88pAVrmCkZuc1tV4s-1p_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c617cffdea.mp4?token=NDRxmspeN2pYtv2s3s2hpsvNsXr-Tvtdx4GHy8qJAMsC5y8iGPVWHTpgPk93sdCLxHLd3HT1RTwkJKO7MH85NO9XV_alsaVoGXFCnQJJd7pLRVZQVwmUvtGh6LCsa4GM9dDzTbMn86DHI3OMorlVc-n6XilWF3BGwH9mfcrKrLivEZN5dbKmiSbpoZDVgIP1FyI8LNcxLxrwKuFHTm2yW_hpWNIS1zWcJJ7GDH799xOLYilDDWM2DPqc1Peeq7tZrymPWrJDM70h6Ae7lPvbFDi7d9omVRLxuNbsqR5hZh2AtggnSr7dRK5m0tjg3_Qf88pAVrmCkZuc1tV4s-1p_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: شاید در مقطعی مذاکرات با ایران را از سر بگیریم
🔴
خبرنگاری از دونالد ترامپ پرسید آیا مذاکرات با ایران را از سر خواهد گرفت؟
🔴
ترامپ پاسخ داد: «شاید در مقطعی این اتفاق بیفتد، اما در حال حاضر شرایط بسیار خوب است. با این حال، شاید در آینده مذاکرات را از سر بگیریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142659" target="_blank">📅 19:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a870d896a1.mp4?token=b6r9hz1Imq50kFoa66uC8tcVbmeEK5hTL2Z9N-Tcl8D2eHwsyI6ZNiJSMDhcqKaAccegg3JdQL4TFjQ6VmpOhpBfdsXnD9gsQrGwKh9QV2t9K5cYrEFHOFOj8Rt1KbZP0d49UQjZ7Ly4C4eHknSzYwtddKi40MMVx-hpddbKbzntjACMztRaeeyX192bd_yvLiqkUVg39ovACrQMgytefrHhZ-u_-JvZrG54QVmUtR55NlaVXFL8aMVLkKS2ljD3XYm8HKH_Ez711-VXjdFKluNkCN6gjUlXaJiunqm7Mb2WxW3l9mqyr6kMSUMKSMspAQBmzWkq6U6maOrITPI464i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a870d896a1.mp4?token=b6r9hz1Imq50kFoa66uC8tcVbmeEK5hTL2Z9N-Tcl8D2eHwsyI6ZNiJSMDhcqKaAccegg3JdQL4TFjQ6VmpOhpBfdsXnD9gsQrGwKh9QV2t9K5cYrEFHOFOj8Rt1KbZP0d49UQjZ7Ly4C4eHknSzYwtddKi40MMVx-hpddbKbzntjACMztRaeeyX192bd_yvLiqkUVg39ovACrQMgytefrHhZ-u_-JvZrG54QVmUtR55NlaVXFL8aMVLkKS2ljD3XYm8HKH_Ez711-VXjdFKluNkCN6gjUlXaJiunqm7Mb2WxW3l9mqyr6kMSUMKSMspAQBmzWkq6U6maOrITPI464i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: حجم زیادی نفت در حال انتقال است
🔴
دونالد ترامپ درباره ایران گفت: «شرایط قرار نیست بی‌نقص باشد، اما حجم بسیار زیادی نفت در حال خارج شدن است؛ واقعاً حجم زیادی است.»
🔴
او افزود: «مردم از این میزان شگفت‌زده شده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142658" target="_blank">📅 19:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f803e8a6.mp4?token=lwx0d3PvpW_1rN7JFauNSdNHvrQ2F4dBD0sTS3GW2UctpmlVDVVv9cm5J4pCSt8Nw47mxJXosD-v9ug_eoPuHljfKMZNy6OtbpDcNHrd827ZLpr78WOofIshNMKAC7fC7wOm8oBvv0fAGuNRZ9nZJozhechmrQioMcQucUiFFZyiPbC9Z5ftlI9E4FsShFexOry73Tiw4G9Llzsc1oZ2fNDwICwOtuqnjMXZm7Qc1d4aAtGB_DLFB7-igUDBtUo3uCe-CQLjBqgMsSkUBy-LolRdv9tLnZW7vuxreoHr85KkwJwrUUTHU0JPehphtb2S94inNAXYWb2EgtWVx-OdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f803e8a6.mp4?token=lwx0d3PvpW_1rN7JFauNSdNHvrQ2F4dBD0sTS3GW2UctpmlVDVVv9cm5J4pCSt8Nw47mxJXosD-v9ug_eoPuHljfKMZNy6OtbpDcNHrd827ZLpr78WOofIshNMKAC7fC7wOm8oBvv0fAGuNRZ9nZJozhechmrQioMcQucUiFFZyiPbC9Z5ftlI9E4FsShFexOry73Tiw4G9Llzsc1oZ2fNDwICwOtuqnjMXZm7Qc1d4aAtGB_DLFB7-igUDBtUo3uCe-CQLjBqgMsSkUBy-LolRdv9tLnZW7vuxreoHr85KkwJwrUUTHU0JPehphtb2S94inNAXYWb2EgtWVx-OdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون استفاده‌اش می‌کرد.
🔴
ما اجازه نمی‌دهیم از آن استفاده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142657" target="_blank">📅 19:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142656">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سخنگوی نیرو‌های مسلح یمن (حوثی ها) : از ۲۰ ژوئیه، ۸ نفتکش عربستان را هدف قرار داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142656" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67623992c1.mp4?token=mlEDLBymK1DifwXS9Ezu2CHTlek6apJA0CcZzisJUP4sev7o8YejKwzjjdYVWbEe5YxgBI8DSRmx1w_DxpHD198IoAufpC4O8hsBF-VCC5zji6AKCorcra7gjsI4jVSLwowZPMvamC_VoMwqpZeJS3wnWfIUovs9A022DyKhkKWuoL8oAm0B_WjIEslvHqz5noH5KKPs3QXxnCInrWB6Nal8E03CuiFAmusbvNJWHRLpLlh30UxAt7bZTgXsbBqPQHOV9VxHWQqOwUY4UQoiX3fk4PkNnt_Xgn3vvL5z6JCwF0n3rHYHzeX53hzthk3rNgZu5L-bL8VlgJcUHakxBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67623992c1.mp4?token=mlEDLBymK1DifwXS9Ezu2CHTlek6apJA0CcZzisJUP4sev7o8YejKwzjjdYVWbEe5YxgBI8DSRmx1w_DxpHD198IoAufpC4O8hsBF-VCC5zji6AKCorcra7gjsI4jVSLwowZPMvamC_VoMwqpZeJS3wnWfIUovs9A022DyKhkKWuoL8oAm0B_WjIEslvHqz5noH5KKPs3QXxnCInrWB6Nal8E03CuiFAmusbvNJWHRLpLlh30UxAt7bZTgXsbBqPQHOV9VxHWQqOwUY4UQoiX3fk4PkNnt_Xgn3vvL5z6JCwF0n3rHYHzeX53hzthk3rNgZu5L-bL8VlgJcUHakxBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره پروژه سالن رقص: تصور نمی‌کنم دیوان عالی علیه ما رأی دهد
🔴
خبرنگاری از دونالد ترامپ پرسید: «اگر دیوان عالی علیه پروژه سالن رقص شما رأی دهد، چه خواهید کرد؟»
🔴
ترامپ پاسخ داد: «امیدواریم چنین اتفاقی نیفتد. نمی‌توانم تصور کنم که چنین اتفاقی رخ دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142655" target="_blank">📅 19:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8ffe259f.mp4?token=SM4tF8B90v89RHORZEd1NiEhhrczZhBihAaIL4remQifloJ_W3cQyDX-T9Eu8fagQmP0omAgva_c76evXdZoj1jG4-b3GEMjgeh0MpC3aGddxae9oMbywbs8DCz9xMZ6shnPbQqSW_SuDSU_m2AAClsCcdHxc0BHDuHTso4sstxE01BebEjJgDXxXrnfCbBhKfuOftjjTqtig43CPigeFJZ1pESYTPhVWRfmzDbwVEyqsoz4o2gCxzEH2vwCCyR2Ty9YtlPpjLvp7b3ZROMk5d1cepM5G03l0zLIfG3V0W0BOchymNPnKfHDHEaKGyCscgTN-P10jyuG6zDRjIe2zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8ffe259f.mp4?token=SM4tF8B90v89RHORZEd1NiEhhrczZhBihAaIL4remQifloJ_W3cQyDX-T9Eu8fagQmP0omAgva_c76evXdZoj1jG4-b3GEMjgeh0MpC3aGddxae9oMbywbs8DCz9xMZ6shnPbQqSW_SuDSU_m2AAClsCcdHxc0BHDuHTso4sstxE01BebEjJgDXxXrnfCbBhKfuOftjjTqtig43CPigeFJZ1pESYTPhVWRfmzDbwVEyqsoz4o2gCxzEH2vwCCyR2Ty9YtlPpjLvp7b3ZROMk5d1cepM5G03l0zLIfG3V0W0BOchymNPnKfHDHEaKGyCscgTN-P10jyuG6zDRjIe2zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من در چین بودم. آن‌ها اتاق بزرگ دارند.
🔴
آن‌ها اتاقی فوق‌العاده دارند.
🔴
این (سالن باله کاخ سفید) از همه بهتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142654" target="_blank">📅 18:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f77c6fe5.mp4?token=fQNE_3uYjkCpqTqnO4uKX8l_W3mPY96-0Rcvf_56o51VTIXX_bKoc5coc4ocMpeZPBxFBSYvsJ4QV1hjsqDIVgEDFiHUxNHG11kk9MvOck-5T1Awz4sBaytgJaX3FZyuNsxdEDKAUbK0tN6otqnKzU9A5tyycCKOjVN4pvFoHaFxdwuIshDC-x4m_WxEon0kWzo_WiggK0xFPTAgk_AvKX7i34gXsL6AnUUPjYproq38IEGQfLIcPND_GPAu7R6pkWDlbH9gV2l0rkWF4a7IF600e4mdEsxZcuVyZ2nhsPIM5_dnZ1p1PQnhyocl4GlviiTcQ4iNSwSYzWSyeZ4d54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f77c6fe5.mp4?token=fQNE_3uYjkCpqTqnO4uKX8l_W3mPY96-0Rcvf_56o51VTIXX_bKoc5coc4ocMpeZPBxFBSYvsJ4QV1hjsqDIVgEDFiHUxNHG11kk9MvOck-5T1Awz4sBaytgJaX3FZyuNsxdEDKAUbK0tN6otqnKzU9A5tyycCKOjVN4pvFoHaFxdwuIshDC-x4m_WxEon0kWzo_WiggK0xFPTAgk_AvKX7i34gXsL6AnUUPjYproq38IEGQfLIcPND_GPAu7R6pkWDlbH9gV2l0rkWF4a7IF600e4mdEsxZcuVyZ2nhsPIM5_dnZ1p1PQnhyocl4GlviiTcQ4iNSwSYzWSyeZ4d54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
برنامه شما در صورتی که دادگاه عالی علیه پروژه سالن بال شما رأی دهد، چیست؟
🔴
ترامپ
:
امیدواریم این اتفاق نیفتد. من نمی‌توانم تصور کنم که این اتفاق بیفتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142653" target="_blank">📅 18:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e129e6b9.mp4?token=h5-vRsMoaqx2MI2FTH8qARgR47hUbX-G_zTbbvuom6d4ZAd7tBKdASu3aVXsFY5mVSzIU8ntF496iMMfSDAyCZLqAGUKyRCc6iM9Nw1l_6h4AQtW4xwxWzMNZe_KdSMW7GIe7dR4DeaqzpUGyXKD2MsGtLAmJPBj8QeT3WE-n-P8oU_bABcxF21Z2ShTmw6gJOJhX2r94k323nXrFHpQilWfBcBKO9eOpXJSHBguli7ug-OdDa8_2yDfQEKnVQE7JFaOWD6iDzVvpaxscPvIVKxtpiW6-S6CNvEIvQKkPSIPgM2Ph5RY4v1E0RxuTZvsZJskk-OfvJ6Mutwg9hGBYjtQHF4FnhQQAnFNMgS0mMtmjH9zTSs3nZdrBNJEsKwLg4mxl_4QNrLko2FMvcMcfVhLlRg45QER3bMKADeHjMCV92YK7UwaAi5X1hN4L8n1Myid6XAwjdLmphHGmLG3wfurjqW4dVS28EsxzsnBCqZw_uxCgS8rgZmkhDlY42JV4-GnFQViBphaEGOuybiPomONOnNwAg_vnK6lrZ6IVUxpTsdug5W6655siTP3xyXppC7OXjJwooJrWqYRsA871j1AuyWKadCLoAe0mJerQ5eSSgzqgcoCFX6FgwuRcq7sc3bY19dCPX2gEamG_VfmYoIykmjFhcfFNBU1d3z8JKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e129e6b9.mp4?token=h5-vRsMoaqx2MI2FTH8qARgR47hUbX-G_zTbbvuom6d4ZAd7tBKdASu3aVXsFY5mVSzIU8ntF496iMMfSDAyCZLqAGUKyRCc6iM9Nw1l_6h4AQtW4xwxWzMNZe_KdSMW7GIe7dR4DeaqzpUGyXKD2MsGtLAmJPBj8QeT3WE-n-P8oU_bABcxF21Z2ShTmw6gJOJhX2r94k323nXrFHpQilWfBcBKO9eOpXJSHBguli7ug-OdDa8_2yDfQEKnVQE7JFaOWD6iDzVvpaxscPvIVKxtpiW6-S6CNvEIvQKkPSIPgM2Ph5RY4v1E0RxuTZvsZJskk-OfvJ6Mutwg9hGBYjtQHF4FnhQQAnFNMgS0mMtmjH9zTSs3nZdrBNJEsKwLg4mxl_4QNrLko2FMvcMcfVhLlRg45QER3bMKADeHjMCV92YK7UwaAi5X1hN4L8n1Myid6XAwjdLmphHGmLG3wfurjqW4dVS28EsxzsnBCqZw_uxCgS8rgZmkhDlY42JV4-GnFQViBphaEGOuybiPomONOnNwAg_vnK6lrZ6IVUxpTsdug5W6655siTP3xyXppC7OXjJwooJrWqYRsA871j1AuyWKadCLoAe0mJerQ5eSSgzqgcoCFX6FgwuRcq7sc3bY19dCPX2gEamG_VfmYoIykmjFhcfFNBU1d3z8JKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در کاخ سفید: اسکاتس میراکل-گرو یک شرکت عالی است. آن‌ها در واقع به کمپین من کمک کردند، باید صادق باشم. شما آن را متوجه خواهید شد.
🔴
فکر می‌کنم بزرگ‌ترین شرکت چمن در جهان باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142652" target="_blank">📅 18:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134287961a.mp4?token=OEZZOFA1COOhkXKyeHJrkXsnLfiv50guICZZ10VIZkgnmg8UHepcrSvzo_LsmzoNUpE9-_j1UDrIi3SlaWiLx-IOepqmVLnMrDVQC65t4jMv8PxJKdeYTpGPFahJRuwm04XbojE45Y45hKj4aefF6xRcZolO8LpE6s6tcg1pPO4BU79lyGsXz8hs75F2RkaO76NxS0OGPL5FtagcNZ-61eJv8j2wKKrUXzHvmD9p7XgXmZ4IeZGxz4sxQww-SNahi33CesV8WePPibtFT1PFTauayuhZJ1IyxCc6KQFXWIR3W8PUaIyPkq9NABYp5IyPPQNoNPRxPoXVRQerHW9dVhrDF1Gytv9-Nbm4QTLP4X7w7XDfdhCltqKX7XBQQKwCUVBZHQO28Mr-WqwYDZovr4sA3S2TX1ivAP1cfrkcLgLHLFN5Qs3PzIOWduiiPNy6-7TwRn0I2UPmv359SA6Xm9vr-tmXjAlsW8TV8iEJdIq1268KV_IhBHUZTEXzR6-JGgBVPMrQFfyYtTUqJlq6hpG_j2fxMMC2tvZcKy5icvp5G_0BFsUbxI41l2qO-gKwPQiOneiUwAiYhW38ydXDqyKaicoDzFNAOhfnQHEo5Ws_OgpXsY1c_EnrNmZYwvJidl_hWPwtQEmliPKf4rW90lv2Z2IOPmrDrmX3SdPmfsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134287961a.mp4?token=OEZZOFA1COOhkXKyeHJrkXsnLfiv50guICZZ10VIZkgnmg8UHepcrSvzo_LsmzoNUpE9-_j1UDrIi3SlaWiLx-IOepqmVLnMrDVQC65t4jMv8PxJKdeYTpGPFahJRuwm04XbojE45Y45hKj4aefF6xRcZolO8LpE6s6tcg1pPO4BU79lyGsXz8hs75F2RkaO76NxS0OGPL5FtagcNZ-61eJv8j2wKKrUXzHvmD9p7XgXmZ4IeZGxz4sxQww-SNahi33CesV8WePPibtFT1PFTauayuhZJ1IyxCc6KQFXWIR3W8PUaIyPkq9NABYp5IyPPQNoNPRxPoXVRQerHW9dVhrDF1Gytv9-Nbm4QTLP4X7w7XDfdhCltqKX7XBQQKwCUVBZHQO28Mr-WqwYDZovr4sA3S2TX1ivAP1cfrkcLgLHLFN5Qs3PzIOWduiiPNy6-7TwRn0I2UPmv359SA6Xm9vr-tmXjAlsW8TV8iEJdIq1268KV_IhBHUZTEXzR6-JGgBVPMrQFfyYtTUqJlq6hpG_j2fxMMC2tvZcKy5icvp5G_0BFsUbxI41l2qO-gKwPQiOneiUwAiYhW38ydXDqyKaicoDzFNAOhfnQHEo5Ws_OgpXsY1c_EnrNmZYwvJidl_hWPwtQEmliPKf4rW90lv2Z2IOPmrDrmX3SdPmfsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در کاخ سفید: به مدت ۵۰ سال، یا حتی بیشتر، می‌خواستند یک هلی‌پورت داشته باشند، اما کسی نمی‌دانست چگونه باید آن را پیاده‌سازی کند.
🔴
ما در حال ساخت یک هلی‌پورت عالی هستیم. این هلی‌پورت توسط شرکت سیکورسکی، شرکت سازنده هلی‌کوپترها، اهدا شده است، زیرا ما هلی‌کوپترهایی داریم که حتی نمی‌توانند اینجا فرود بیایند. آن‌ها هلی‌کوپترهای کاملاً جدیدی دارند که مدت زیادی پیش خریداری شده، ساخته شده و اخیراً رسیده‌اند.
🔴
آن‌ها نمی‌توانستند روی چمن فرود بیایند، زیرا قدرت موتورهای آن‌ها آنقدر زیاد است که چمن‌ها پاره می‌شوند. آن‌ها امتحان کردند و چمن‌ها واقعاً در همه جا پخش و پلا شدند.
🔴
هزینه آن توسط شرکتی که هلی‌کوپترها را می‌سازد پرداخت شد. ما پولی برای آن پرداخت نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142651" target="_blank">📅 18:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23b388398.mp4?token=eZ63gZ4ZXh2uux2SYqr3AY50UluKqTZiZs7nBk830tSLYpKdyIWa5nplrTkqAMhz_0JmfWpfIc_7k3ESAtJlK5HERmZ_QghhIj0dr-lV32PAbaMmi5vc3-Qen0gPg81eqHcofzBHJkH6viQ-ZRI-z2hup0gUYPreVkiNvVJNnpOikYJitoh_jXemL_QurlIOQILX44Gh_7kDVCLXiov0htBZHIRYLCxc21WSZytcsPzOU6Wu6viBJKfI7G1CIdN9Otnx7rJN06c-F1qjEeZDz-7ZqoXSaj0Ujcj18GSEBexCpY9hvwzpe9SFUf_eCmITt0o1AawjwVA3ytO9M_KMXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23b388398.mp4?token=eZ63gZ4ZXh2uux2SYqr3AY50UluKqTZiZs7nBk830tSLYpKdyIWa5nplrTkqAMhz_0JmfWpfIc_7k3ESAtJlK5HERmZ_QghhIj0dr-lV32PAbaMmi5vc3-Qen0gPg81eqHcofzBHJkH6viQ-ZRI-z2hup0gUYPreVkiNvVJNnpOikYJitoh_jXemL_QurlIOQILX44Gh_7kDVCLXiov0htBZHIRYLCxc21WSZytcsPzOU6Wu6viBJKfI7G1CIdN9Otnx7rJN06c-F1qjEeZDz-7ZqoXSaj0Ujcj18GSEBexCpY9hvwzpe9SFUf_eCmITt0o1AawjwVA3ytO9M_KMXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما زمین کاملاً جدیدی را روی آن ریختیم. مواد مغذی زیادی برای چمن وجود دارد.
🔴
اگر شما چمن باشید، بسیار خوشحال خواهید بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142650" target="_blank">📅 18:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
آمریکا در حال حاضر حدود ۵۰ درصد از کل تولیدات نفت ونزوئلا را دریافت می کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142649" target="_blank">📅 18:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gj6FLo5YafvFij3IM8lp0KgcLkk5pQQnpgcg7M7jpRhR8t9FzPRi54VcnsE-pnMZcAGu3fTCpZsEarmW8DXoPikBgPk3Xi4DDDA2LJDjp-rUtaa56ceQVZ1Ysx13qmw_QeKNbbj8o2-n5GQbH6zyrmYQ7YNv5D2-OFF-IcOCcf1eEZ49F0FQ24c0JqxWPptvoxIMVFOBFB_mFrV0ub_zMsIKVCpDZBs7_XOdzsdIkGU2-2T95LHZv5mGmM3quqzGmbaIz1b95f0KfI5g0ac-8r7ZJVuEiFzXmYR74KyOUZ3zWCStaKWDAs1p_OqySfLJcaM8BGZ7-ArUKskwSrrDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من به کوری میلز، نماینده کنگره از فلوریدا و دوست من، گفتم که از رقابت کناره‌گیری کند، اما او گوش نداد. او فکر می‌کرد می‌تواند برنده شود، پس چه کسی می‌تواند او را سرزنش کند؟
🔴
ما اکنون یک نامزد عالی به نام رایان الیج داریم که به جای او در رقابت است! رایان نماینده همه چیزهای MAGA است و توسط همه مورد احترام قرار دارد. او حمایت کامل و مطلق من را دارد!
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142648" target="_blank">📅 18:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142647">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل: گزینه جنگ تمام‌عیار علیه ایران، یک گزینه مطرح‌شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142647" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142646">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
معاون توسعۀ محیط کسب‌وکار وزارت صمت: با پیگیری‌های وزارتخانه، محدودیت برق در اکثر شهرک‌های صنعتی به حداکثر یک روز کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142646" target="_blank">📅 18:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142645">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ppFdtsmic_FsoaDKt8U0-SdSTkOR80nUxpR4g8EIr9T-SJtyTAbfiYW5j9wanBaiKAWRPmEOYKhRsgL-wkmkZXDlpWcpJ0_sjaToOvXGoaX8PLaGOtfbrYXHlfdoWDtmumFua6vNBJkN125Plc7qXIMpSSwhUnNAQo8gfU-EAS-zn5fE05n2J4DFpte6kkBLyE2NL_9kjab3OsZAZ1UbJmdN-rfTzXCUbbzrRMz1dQfsSGVPmlLtyp6MkK8qcGyQIiBe-3W5-o_SM0JRT-UGV15iB9xLknipD5y3gJZKoOa9rM5gok8tV_fvnkLRyQyYSXuEird0XihrT8D6xOCZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتیجه واکس سرطان موفقیت آمیز بود / سهام مدرنا 150 درصد جهش یافت
🔴
برای اولین بار یک واکسن سرطان در مراحل نهایی آزمایش موفق عمل کرده است. در یک روز ارزش دارایی سهامداران خود را دو برابر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142645" target="_blank">📅 18:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142644">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ارتش اسرائیل: در کمتر از نیم ساعت، دو فرمانده حماس را در غزه مورد هدف قرار دادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142644" target="_blank">📅 18:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0G7RvjT-SLzJZq5Oaq3vFYqXKM-Og12FjN25kInnqA9oTENvsoYAmHrnRqv_TxqxwwWup56eiektZftOTaQBxxkeG8Rby1yvDbSIS-51AeRDY2yN94JXSEIGf1BId1ivMKNUJagqY2rzGiRAJCT50gxlLuPINZmhy1GHoLE1L4CM6HCNcKi6VIYdd0_Jnj5PPxC7Ok85ZrQ1cE0xACgdJtcy-cyGkinl2sUKs6tDcfGOinE8pLN0VBEthZ4N9GEYoRKLq4GPbQFRqtxP2pcTjz6vMMhDUwZmU4kLbw5z-FfSdZoAN5CpbyMbcfNAjf5Prn38-ju_p9v2lwAP30sww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
رسمی؛ دربی قراره تو ورزشگاه نقش جهان اصفهان برگزار شه؛ 11 شهریور ساعت
19:30
@AloSport</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142643" target="_blank">📅 18:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkEhCMcFk_aLXnZx6YpMpEHveNn4IeyCtDyf-H-5pI3KgkY0GmaauAhIoxAZmhDWVuYPJuIRxTWvTnLMFySgDlNSQfbCGL4OLKlDs5rQ2Y6uzeVEh-utTp-TCarbHLl-uC-O7w7LANRun7QjNTzS-lAoR6qesO1YtoG7wNMIkMMpnNTWivQvJUPmc-yF05C-bwCkMIq33w1SVyZMCZNZjo0_4bxESxzBtFLRXVJZ1JUrQXgG5uzqDTMOawwDTfYdo42yenKZk5iKE7noNanDQNh0XkDMfBmEH4Bc-Q1qNWLAhu2NHeh6TDbSuOxnMN5djJTPOOkNWnMOdp8CNn1ysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خاتمی: مردم گرسنه هستن ولی کمبودی تو زندگیشون ندارن
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/142642" target="_blank">📅 18:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142641">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گویا در تهران بزودی از خانه‌های ۲۵متری رونمایی خواهد شد تا شرایط ازدواج جوانان راحت تر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142641" target="_blank">📅 17:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142640">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5214028bd8.mp4?token=F_RqjM-xxYVRLMXpLobD3y1q50-pzrmDXv4V__Pgbh2BXVjBnSIb21dzFda2_Ae_rAgnseQht7iYdxOxgJyhHAw2GHoPrl0B-BeG0Yq-MJlySJlPcep4huuglxVJnLhY4_1QgszbtCATPeNPZlI67WyCI7w-xdhC3TTQ-Zp_L9Sv8IZSytaD_-CirxWWjfZsksGv7QbWQ8FK8EVyXKaoiyzNSKkzo-6B8xqDFnYX60S78ArBshoSH4fWGx5qWKES1If2pOWJsnQGRRlFyaK3WhA1IZ1kDZ9P4iz9UsPQ0KCWgoBy7NBB-pX6RjMA4YAEeBtzzbsU_QKoajJfKxj-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5214028bd8.mp4?token=F_RqjM-xxYVRLMXpLobD3y1q50-pzrmDXv4V__Pgbh2BXVjBnSIb21dzFda2_Ae_rAgnseQht7iYdxOxgJyhHAw2GHoPrl0B-BeG0Yq-MJlySJlPcep4huuglxVJnLhY4_1QgszbtCATPeNPZlI67WyCI7w-xdhC3TTQ-Zp_L9Sv8IZSytaD_-CirxWWjfZsksGv7QbWQ8FK8EVyXKaoiyzNSKkzo-6B8xqDFnYX60S78ArBshoSH4fWGx5qWKES1If2pOWJsnQGRRlFyaK3WhA1IZ1kDZ9P4iz9UsPQ0KCWgoBy7NBB-pX6RjMA4YAEeBtzzbsU_QKoajJfKxj-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این سکانس فیلم آژانس شیشه‌ای دقیقا برای این روزهای ماست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142640" target="_blank">📅 17:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142639">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
افزایش شدید قیمت طلا
‼️
پیش بینی قیمت طلا در روزهای آتی
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142639" target="_blank">📅 17:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142638">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پولیتیکو: ایران و آمریکا وارد فاز صبر و انتظار شده‌اند؛ هر یک منتظرند تاب‌آوری دیگری زودتر تمام شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142638" target="_blank">📅 17:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142637">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
قالیباف:
آمریکا به دنبال خروج آبرومندانه از منطقه‌ست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/142637" target="_blank">📅 16:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142636">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یحیی فست از حوثی‌های یمن (انصارالله) اعلام کرد که سه اصل اصلی بازدارندگی علیه عربستان سعودی را برقرار کرده‌اند:
«محاصره در برابر محاصره»، هدف قرار دادن استقرارهای نظامی سعودی در هر کجا که مستقر شوند، و پاسخ به نقض‌های قلمرو و فضای هوایی یمن.
از ۲۰ ژوئیه تا ۱۹ اوت، حوثی‌ها می‌گویند که هشت تانکر نفتی سعودی را هدف قرار داده‌اند — پنج مورد در دریای سرخ و سه مورد در خلیج عدن و دریای عرب — در حالی که ۴۸ کشتی دیگر را مجبور به بازگشت کرده‌اند.
آن‌ها همچنین از نه عملیات علیه اهداف در ينبع، نجران، جیزان، ابها و شرق عربستان سعودی در پاسخ به حملات بر فرودگاه صانعا، بندر حدهیده و نقض‌های فضای هوایی گزارش می‌دهند.
۱۴ عملیات دیگر استقرارهای نظامی، تجهیزات و کشتی‌های حمل‌ونقل نظامی سعودی را هدف قرار داد. حوثی‌ها می‌گویند این حملات منجر به صدها کشته و زخمی، تخریب تجهیزات و انبارها، غرق شدن یا آتش گرفتن دو کشتی فرود نظامی و تخریب بیش از ۱۰ قایق نظامی شده است.
این گروه هشدار داد که هرگونه تشدید گسترده‌تر از سوی عربستان با «پاسخ جامع» مواجه خواهد شد، در حالی که پایان محاصره، پرداخت حقوق و خروج نیروهای خارجی از یمن را مطالبه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142636" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142635">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La6byw_mwXFfRrwHHcJGPZT0FWZWUFHIEf4plbeVAXGpcHmZ2WOt0u0HaDNC3nEMBdIrjke22mTBJIrydcRbhq4G-ukXRDTEU8lCmOmtR-U1x6UtRIzYXm5ATUAIB8KlIaGgkeDnUGhSdoUI1IVaEvL-E5TKCKWHGFkHxnOsd8fGMtVDh3lrWfvzh4fumOiD8vRRXdOOSsE5SOPfVi1NbG2cNvrzQYTEzAYiM86Pt3eqloxYKcgBPhgM8z8d7ZZz2XoLQFw-e2Yg06dpy5NYhjimsxSH8qDR0VL9i14T_33Wn_CZKV-a_zeBn_gDys_g7tkKd8Sjm9zxFz3oMuyPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: کاخ سفید همچنان در حال ارسال پیام به تهران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142635" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142634">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk2qMGIUMEaLHucUBcmd8kKymefIZ8dXonaPj8oukH7K2RjpPlWUAgPuXDJ5ThEB2_nYUtHvgGKBstVl5ioTBY-wr7u6gUpsw2gURY1ZwkdjPR6G63--f61ktAKa6SVu57Xjq6WuGgGBpcaXXpUYGT-UnXSUlLY5Erc4SYDrlAurtZdbwRRaf32FR2MtUWUCFqK21rog5kUb0l398YuN37mhW2k5yspPZCArLpY6ccZR-brbheUNNFHYZKdwDPWCt7uHihEAaD3n4nkwnQ48iJCp5_MkspggKjVT46xVm1i-wUZ6vn_T8e6PhBDExhHbaJf-EfSlcfkw2Ixxzv8RZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت با طرح «مقابله با نفوذ» به علت مغایرت با قانون اساسی و حقوق شهروندی، مخالفت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142634" target="_blank">📅 16:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142633">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXCNu31v1pegqLzQ9Sn9bQfByvDaDcp5sgyTPrB5XTY_2eXwh7JiyjP31Sx422XVgnVELvcLhzdz7KKPbU5a7BNthDz6W0nG4goU3zaOghc7Rc9Hp3nRnrnjAYy6PH4a5-Usxsh0FbOlnedsWQhCk9pCaj8Yl2qkdCuYKC06Oxxq1d7CSgfIL9bhvpSAubidiI-e-B6aCAWB0dkpCQ5RKmdmnBmLYmRP1om73k8Zsw9JMSrexZkoeUvtq-4rjSGDfdCRGgtUTdmYdi1WCLf1Yg02NAbC81f-ZSIjIQgPzIOs2eIBhVLNth5tetfduepaB5JPgSNGKWFoE1gHME5hIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش رسانه های حقوق بشری
«آذر یاهو» به دلیل گذاشتن استیکر خوشحالی برای مرگ آیت الله خامنه ای و همچنین کامنت گذاشتن برای نتانیاهو؛ به ۳ سال زندان محکوم شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/142633" target="_blank">📅 16:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142632">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF4G_Q4G5sxAT8z4pKmK_k5OoilBMJKp0XnBlBMGMiuWUBefKT-UdJqFek1T4GVYN1P7cSzBw8RD_b0PflmaWv34ja33Lj7c7YlDgn5yqRyIZLS9xDDid2FaxWaBd-7mVqvLo6Ns9Yaq4OVSQY_nlMw8Ss9YOhtzMfwP-jasK3A5qAptv34VPPseAAsrp1DDevRgPCqRGPDg5-BZGto_mVg1bHomwnF6SCpwrfWbA3R4adLRfsM0BoBKs9shoe-1PUeBJjAlo65JdvvXn6TIHUM8tJOXB7yuont-acKHyI75n2X3TDk-z0_mkMg-tkAUX3IyoYpbxhIMgBfiAXnFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: باید آب‌های فلوریدا رو با مین‌های هوشمند مین‌گذاری کنیم، اینکار میتونه حواس آمریکا رو پرت کنه و ارتش آمریکا محبور بشه بخشی‌از توان نظامیش رو به آمریکا برگردونه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142632" target="_blank">📅 16:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142631">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb1f98eb1.mp4?token=v65YONjNUFSkQgqc3WC5Xm0eZuPYk-8A1y2uUCqxKN2s2lYUpEAr8j_L3OgRYD-7h0yKDjeB00y7fbcsHwm-WAKq-UfWR21VEcX6mqJ0Akx5-veuLa6fQplbqnc5YQhhojnwci-I7eZvwwIWpnhJprQcSZnG5hvM72uouQqI2j-M-ezsAcy8jtdJtg73tQMsNMeeyp8BUe4gF4TqpJLndrEYREPablHw_Dpj58fG3x-Ee9IxBDb1kDj8Qc2rKn64ybb6_jpkYMpbzce4Z4bWjm1C9GsmjD2Wg3TWHy7iZ5POlfIFRa-dTZHtoNWl33hX76T-BMCmAal9brETApULIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb1f98eb1.mp4?token=v65YONjNUFSkQgqc3WC5Xm0eZuPYk-8A1y2uUCqxKN2s2lYUpEAr8j_L3OgRYD-7h0yKDjeB00y7fbcsHwm-WAKq-UfWR21VEcX6mqJ0Akx5-veuLa6fQplbqnc5YQhhojnwci-I7eZvwwIWpnhJprQcSZnG5hvM72uouQqI2j-M-ezsAcy8jtdJtg73tQMsNMeeyp8BUe4gF4TqpJLndrEYREPablHw_Dpj58fG3x-Ee9IxBDb1kDj8Qc2rKn64ybb6_jpkYMpbzce4Z4bWjm1C9GsmjD2Wg3TWHy7iZ5POlfIFRa-dTZHtoNWl33hX76T-BMCmAal9brETApULIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظفریان، معاون مرکز پژوهش‌ها: ادعای کسری روزانه ۱۵ تا ۲۰ میلیون لیتر بنزین غلط است.
🔴
با افزایش تولید بنزین از ابتدای سال تقریبا در مرداد ۲ تا ۳ میلیون لیتر در روز کسری داشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142631" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142630">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اردوغان: جنگ ایران و آمریکا راه‌حل نظامی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142630" target="_blank">📅 15:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142628">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCciRPifQ4-wSrYgZhE6Z-HkBH9QuV78tmE0AKogRuq5vdJNPE-arj_N5tXxIXRftuoV-TUoKttPCW1ikZ9lfNJ4RysVc6J0IUqKY_0nUKH_5-GkIAxIKiZG_5kjt4A9Xagxj-jFIJTcT_SvRVEw-4G1aG1sfwItyj2v9RuPhI8jbvbfCwsP2_9Utr7ZW722x_cnpBrn9700mg4aFX4PnGaxKINA8OTNognLx-bs6U5OXB6bI4CKBmEJspEW21o-ozpOVuN4_-U1-XR1QbK7p2XY6WKdBUSSBwaO0XvKq1SSUYhrvTZV9mcLsaPG4iZxgcM59GhjXFGvFpBA4XKI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل: تنگه، تنگه
😈
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142628" target="_blank">📅 15:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142627">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6fb20727.mp4?token=TDvE_nNpNqviUOTBUi1JkGnKUGFuS-qIRevir8ZRLq_YdWGWXzlm56jlJQVBoEOpFUtZUVQmZXJ_-ZBAPPRhDY_s41BUg3brf71THVpEY38qlzCrV7HwwDl4fTedSatDryhsBbsmDCCIc2DF0JhP35uE9uqeqhGDMq_WaeuVwdgJoiATJxZiZN48Lw_Kn9xeblBVi9ArCzdY-NsI4EvqTDSvLVBdtubFDP-B4LEDL7oURrkjXlPn0brEWBcSrGJOyyagP2G6lIc_sm4x2KJKRIQSwSygxMWvjwYuGNAW8wOyO9xOIux2yCwsVj4DBAaNtfoEmaBwANgoo144PWbh4Xfa3UNboXtemS7HRbHa9mRkMpXzx-jG3iKj3DyWdfQFq6J9ma6QKyLdQ7xorz8STNY97xgICj_Dryx8uEBfq-6NZnDI_9nE4E5uL47Gfy36JzTCf7N4DBd70BB0g7oHNDch2wnal2gtWv8uhtwycdJ5WUR9jWxyn_n2wLYzykKCfDuZxEawkovX9S0mE9jFE8L6m2RjECfefDwjYL9gRjYigJm45lcNPyGEr0gNBav5UogL4Inu5vby33VtsIQoVJZtxunKoaNwQJ76mgYy6R8Cw2ekq7cpmvn3_3uy9dUWP6HDWu-Yvw4Fxpj7Dzp4ttXrsAukHjBIoWpl5tSuDwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6fb20727.mp4?token=TDvE_nNpNqviUOTBUi1JkGnKUGFuS-qIRevir8ZRLq_YdWGWXzlm56jlJQVBoEOpFUtZUVQmZXJ_-ZBAPPRhDY_s41BUg3brf71THVpEY38qlzCrV7HwwDl4fTedSatDryhsBbsmDCCIc2DF0JhP35uE9uqeqhGDMq_WaeuVwdgJoiATJxZiZN48Lw_Kn9xeblBVi9ArCzdY-NsI4EvqTDSvLVBdtubFDP-B4LEDL7oURrkjXlPn0brEWBcSrGJOyyagP2G6lIc_sm4x2KJKRIQSwSygxMWvjwYuGNAW8wOyO9xOIux2yCwsVj4DBAaNtfoEmaBwANgoo144PWbh4Xfa3UNboXtemS7HRbHa9mRkMpXzx-jG3iKj3DyWdfQFq6J9ma6QKyLdQ7xorz8STNY97xgICj_Dryx8uEBfq-6NZnDI_9nE4E5uL47Gfy36JzTCf7N4DBd70BB0g7oHNDch2wnal2gtWv8uhtwycdJ5WUR9jWxyn_n2wLYzykKCfDuZxEawkovX9S0mE9jFE8L6m2RjECfefDwjYL9gRjYigJm45lcNPyGEr0gNBav5UogL4Inu5vby33VtsIQoVJZtxunKoaNwQJ76mgYy6R8Cw2ekq7cpmvn3_3uy9dUWP6HDWu-Yvw4Fxpj7Dzp4ttXrsAukHjBIoWpl5tSuDwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران: اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.
🔴
هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال خواهند شد.
🔴
در دولت بعدی، ما این سیاست "مجازات" را به طور کامل اجرا خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142627" target="_blank">📅 15:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142626">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
۳۷ تا نماینده مجلس برای حجاب، به پزشکیان تذکر فرستادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142626" target="_blank">📅 15:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142625">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzKx8M131OiVV5vBSxlxbE9YN0vajtrE9FdXFzWvI_-4es8JiLGdmaWfEHQA1Mtmn8nSUW6Q_IdDV0QAxfFmETr_PmIPOIQ4V2Xmphpa5xHAoqtLM0PtVKJVHqr0gvAhrG49p_xAbkpqf3ehkgJDnDjGWGXZO85N0k4LOUq48QYz8d0JT1J57ugwxMF9w3mcHvBq5F7GGAE9NxMsOi23AG0HNNmT8EZmZqCiAA8sWVqvRc0nZgOexM91LRbybEkxsgB7lf-0J_NoDo-21P99oxLECXBXFEkYCJAFGRC8MITcS8j0p-OKPy5srMMrCwOOUdLVX9JeoaDnwAt-aA6new.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو شهروند کشته شدند و دیگران مجروح شدند پس از انفجار یک بقایای جنگی در شهر میفدون، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142625" target="_blank">📅 15:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وال استریت ژورنال: حملات اخیر ایران در تنگه هرمز، روشی را که امارات برای حفظ صادرات و تولید نفت خود به کار گرفته، تهدید می‌کند
🔴
در این روش که «سفرهای شاتل» نامیده می‌شود، نفت خام و فرآورده‌های نفتی از داخل خلیج فارس به کشتی‌هایی منتقل می‌شوند که در خارج از منطقه منتظر هستند تا محموله را به بازارهای جهانی منتقل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142624" target="_blank">📅 15:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش ترکیه در تماس تلفنی با دن کین، رئیس ستاد مشترک ارتش آمریکا، درباره روابط نظامی دوجانبه و تحولات خاورمیانه گفت‌وگو کرده است.
🔴
جزئیات بیشتری از محورهای این تماس منتشر نشده، اما گفت‌وگوی مستقیم فرماندهان ارشد نظامی دو کشور در شرایط پرتنش منطقه، قابل‌توجه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142623" target="_blank">📅 15:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
جمهوری آذربایجان، دادخواستی رسمی علیه شبکه خبری سی‌ان‌ان (CNN) در یک دادگاه آمریکایی، به دلیل گزارشی از این شبکه که ادعا می‌کرد نیروهای اسرائیلی در جریان جنگ، در داخل خاک جمهوری آذربایجان علیه ایران فعالیت داشته‌اند، تقدیم کرده است.
🔴
جمهوری آذربایجان این گزارش را به طور رسمی تکذیب کرده و اعلام کرده است که اجازه نمی‌دهد هیچ کشوری از خاک خود برای فعالیت‌های نظامی یا اطلاعاتی علیه ایران استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142622" target="_blank">📅 15:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4wI4lhipb9D7qRWcmg92Q3UhX4YKgjDQ_2-sSe3SW-vxXLiw5xMI2voT1BjrrDlMoGnafnsB-ueATZmqZK3FixEYkEzfajhFQFkm2-Dco5EUQJjJze0mloeDKxRB7ZWQI7jcxoQFKDyJuynlKqjDoBC_N1i0JoXNK3S9mSXStCiC2GWZnRopHkoQTrDcRkKqAS28nSQt3xRO9hYDpfzWrJwqqlT0SV3s_3LTqvSkYLS_1AaubE0I6iDegYJz4aPe7N1z6hFsL6B08HwNu5G0gXLsCZfC9V3GiEA9vx7QmEUeIoUAc4prbdN1tphPm8oH6Xp-JemEyl_QJJtNK4sjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: کاخ سفید همچنان در حال ارسال پیام به تهران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142621" target="_blank">📅 15:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رئیس مجلس عراق از قالیباف خواست تا اجازه عبور نفتکش های عراقی از تنگه هرمز را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142620" target="_blank">📅 14:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پروازهای فلای‌دبی و ایرعربیا بر فراز فضای هوایی ایران از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142619" target="_blank">📅 14:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142618">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPxNg-vnuMRJuk2elq5_EicOJcrhuNipf1yEC2qoc_nEQKOPzcyV-jLnydWcsgKXkZL2IWY5rSD-RZUmFpmwwENTKF6n3uOPBMZt0Wtdwu1_3KzR-Iq5FjF3lvT821kI6ZZzLaeH2I2ryre1E-6aXaB1S-8w1wDNVzoHoapRV9b74jUsQAjwz-62YizdSb83g_tHczC5Wpmm3fKTKSEgSdcK0uo9UR-zBhdqylpUh0zBxEAoT3ydVgfTHo6JN3z-HilEmIKz9i1RiHM7yN0JwvUnSEZ4MIfeAu7rADAMoQ3Ka38fijigwHPMYoQEFe7fIpPjv7RmGWrHNzMV2FqkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسما از سوی فرانسه اعلام شد: اخراج دو کارمند سفارت ایران در فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142618" target="_blank">📅 14:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142617">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9t1lBSyiFPDHw85LEj6pecYHM5t1N9_G0j9eeHMC23ZSLc6w34WDqozWJet3j2IOaPdRRfvGqTwHr8bdYU3hdx0fPmE5bFZ8HvH2P0HwbrC5m3bRBOA9kUzuG9vk_J9szxJkIEzNq9V-i7dCWH-kJZqadH1FpYvwg5KmxKbxOi6ek1ZFW68ZGfNz0B1XfePacj5X0LaJCi5UByjodwMjqJ99-3G7ZQawrGS_Mys_cX2FdN7PjNZzXVZS2G82k7uGPwBM3fF7mU6mKcAL4_FOpo96oGG3-ev42r-Qh7h8q982c6ArAxqk_erW3T_p0BmpgV6nC778_J6PsydI5vJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس : لباس‌های ترامپ هنوز بوی غذای هواپیما می‌دهد، اما ادعا می‌کند که تنگه هرمز را تصرف کرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142617" target="_blank">📅 14:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت سعودی آرامکو به دست‌کم سه پالایشگاه اروپایی اطلاع داده است که در ماه آینده، تمام حجم نفت خام تعیین‌شده در قراردادهای آنها را تأمین خواهد کرد.
🔴
این تصمیم به معنای ادامه تحویل کامل محموله‌های قراردادی نفت عربستان به مشتریان اروپایی در ماه آینده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142616" target="_blank">📅 14:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اسرائیل به هیات صلح اطلاع داد که قصد ادامه دادن حملات به حماس در غزه را دارد و فعلا حملات را قرار نیست متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142615" target="_blank">📅 14:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142614">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abb069838.mp4?token=UKEqwo0pQc1Ekqa4UoctUPnnqYFeXoFa_7W3YhqHHpIZiBVU9NXLbxzxmPtsoWT8P8FdXBDYm_dwy8sZBOJonp_r44e0YQm0pA6BZHzOO0h1Tha-JqfIOGsW-x9pANvUh4sA74ZyRThhJdDRNJ1bkLMv8ysmjRxVPeEzYB1_7Zi84lh27HxA1Dq4KxkPQsU33-uvMuIxwCENXQNxQvQGUez3pEgx-aEvsAfrPyLALvogCGY5yTLhHYPJzolm_gW2mTQvk3ybfLJUXuihZTeYnvX2W9FaYIuHVjTMIEwbDq8FvMfzm9eVbnY_JX8q7zqO9pFJ_vHysUzzIG2IsT9Urg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abb069838.mp4?token=UKEqwo0pQc1Ekqa4UoctUPnnqYFeXoFa_7W3YhqHHpIZiBVU9NXLbxzxmPtsoWT8P8FdXBDYm_dwy8sZBOJonp_r44e0YQm0pA6BZHzOO0h1Tha-JqfIOGsW-x9pANvUh4sA74ZyRThhJdDRNJ1bkLMv8ysmjRxVPeEzYB1_7Zi84lh27HxA1Dq4KxkPQsU33-uvMuIxwCENXQNxQvQGUez3pEgx-aEvsAfrPyLALvogCGY5yTLhHYPJzolm_gW2mTQvk3ybfLJUXuihZTeYnvX2W9FaYIuHVjTMIEwbDq8FvMfzm9eVbnY_JX8q7zqO9pFJ_vHysUzzIG2IsT9Urg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب تو تبریز ۱ پسره مزاحم دختر میشده و کسبه هم گرفتنش انداختن تو سطل زباله
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/142614" target="_blank">📅 14:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142612">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a77ace1c.mp4?token=dFKZe7uEUqLTMbZldRwl6jmSCUVyAjaANcBfu8nMEuuHrFfDfTsCAojOidtJlj1KPyMfg3eGCINCwCW1DW9zH_8tHPDvqpZs2bV_-Dlv9EjGTWuU5823rRPEpMtGYAzABbZ2wTwQvxZbzGV-dHwZGJIJF3RQac1Yh8GIQydQoTdKkLSOlj1_qKzJv8FLDx_dK1OgALj-rfWfxE-ftdWatCiEmiimNoDKXncu1U3w92hSn0jgWFQF5uoaLxXgoIUzMbBrbj1tIsfWB3F3jmkmH1Ml-iNERtjJEQ3AjuuZqOHsi5Qo_cKu6tJrI32mjNsOabcoCNtyofUh77Vj0q9Qmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a77ace1c.mp4?token=dFKZe7uEUqLTMbZldRwl6jmSCUVyAjaANcBfu8nMEuuHrFfDfTsCAojOidtJlj1KPyMfg3eGCINCwCW1DW9zH_8tHPDvqpZs2bV_-Dlv9EjGTWuU5823rRPEpMtGYAzABbZ2wTwQvxZbzGV-dHwZGJIJF3RQac1Yh8GIQydQoTdKkLSOlj1_qKzJv8FLDx_dK1OgALj-rfWfxE-ftdWatCiEmiimNoDKXncu1U3w92hSn0jgWFQF5uoaLxXgoIUzMbBrbj1tIsfWB3F3jmkmH1Ml-iNERtjJEQ3AjuuZqOHsi5Qo_cKu6tJrI32mjNsOabcoCNtyofUh77Vj0q9Qmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی ریزش یک معدن طلای سنتی در منطقه زامبوی در شرق کامرون، نزدیک مرز جمهوری آفریقای مرکزی، دست‌کم ۱۰۷ نفر جان خود را از دست داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142612" target="_blank">📅 14:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142611">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpY2v-P9NrCdeydTMr3ZZMzSYMm5-KklqKhSzyX8bk0z4POF39xwz0v6Vm9M7Rq71ky854_id7THQFQnZ7_6xGYHTbhmi0JX90VgNDF9wU8vzYGhBlqM1vg-qDWjZsoBNIYX04wOWFYAgyqpVvoPmyEC96ekxWoezmBlt8mBQWmo3gedjgLaXqzRTivWqcusdloqLOExWLOgUH61mc7NCtW2u-8PNAN1vDiHCxSiZIkIDpyNgC8VugmhMDhk6VtfeouG2q7PPFlu66kdWi9erszdE4WhkBOXKkayvYkpoYzmKHRQfgN4YiLK6EFDpP_TQDWJZ3Cpdx7Ww0GM5ZzhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گیدون سائر، وزیر امور خارجه اسرائیل: بیل کلینتون اگر تصمیم درست در مورد کره شمالی در دهه ۹۰ میگرفت، این کشور الان بمب هسته‌ای نداشت. اون موقع تصمیم بود که به کره شمالی حمله کنند، اما در نهایت این حمله را انجام ندادند و این کشور تبدیل به یک قدرت هسته‌ای شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142611" target="_blank">📅 14:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
اداره کل هواشناسی استان تهران نسبت به بارش باران در نیمه شمالی و وزش باد شدید در نیمه جنوبی استان همچنین کاهش دما به‌طور میانگین بین ۳ تا ۵ درجه سلسیوس هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142610" target="_blank">📅 13:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142609">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شرکت توانیر اعلام کرد: در پی آتش‌سوزی در پست برق شهرقدس که ناشی از فشار و افزایش بار مصرفی رخ داد، بخشی از شبکه برق منطقه دچار اختلال و خاموشی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142609" target="_blank">📅 13:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/httlNNnQMh5k8Mv_EDCII_2DeajqmXDvvPO1bNmRUUBdPr-56tdGT8QlkLHAZrxa3VLzYLrRbPlYffyGC1iKlAGy-cxh13Ceszn4LRwj6NiuGq3c3RWjCs5G8KsQh2xauInOz4WAM-hLgBBFNREiaN9OUmc6a61uQ_uK4vCDX5BKZh2W8ThNH4ahadmsm73ZQYB1Ou-CJP0wdPiBAeRs27kQVAz0yeEEGgFD193j0K7CiCAb8k-mbXlQRadpdMqbvXFK7257F0ZvSlkKoJwaRgX95aFIhizXaRagpVkuODbcYSXI0tZxrGZtAMXL6EhsSZGvrH5u2_WvUDj0LhKGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران در هند، در پاسخ به پست ترامپ که تنگه هرمز را جزو قلمرو آمریکا خوانده بود، کالیفرنیا را جزو خاک ایران اعلام کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142608" target="_blank">📅 13:45 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
