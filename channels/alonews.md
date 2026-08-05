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
<img src="https://cdn4.telesco.pe/file/NRcG1nHmLvSRZ06H0EvY-TIVHVVxUU0Pozw3pu5oYSiQsfevKNE2OBVNSUyMy2mi2A870O77_Z8_tWL6QlzRlxdmvZe4YqPR0OLQdKW3GyzwF9wbYTpgYtCcFQIrlXycgscYqRvu9KiJx0kp9R_sUoDr9MDNRiNTx13-veqMito807GYQUAxc4TfaOXpb1tkEgP5ungTV5g34jnJp6DjHaSc_JvMAsuruHUcrWY9V9-6i8wE8-KoLSGdiUx9CUJMzeHW-njyWbnjjIZa-0SbN7fS8L-_tQNRvlhQdBXW6ZPaokZblfYsSptyJwPyG2ibPUpNiuIsapyuGvrYxHWuFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 985K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 08:27:26</div>
<hr>

<div class="tg-post" id="msg-139930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سنتکام:
مسیر جنوبی از تنگه هرمز همچنان برای کلیه کشتی‌های تجاری که قصد عبور از این آبراه بین‌المللی را دارند، باز و آزاد است. در طول سه ماه گذشته، نیروهای آمریکایی به بیش از ۱۰۰۰ فروند کشتی در عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند،
علی‌رغم اقدامات تحریک‌آمیز و غیرضروری ایران، و این عبورها همچنان امروز نیز ادامه دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/139930" target="_blank">📅 03:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مهلت ترامپ تموم شد و الان میاد میگه بخاطر تماس طالبان، به ایران یه فرصت دگ میدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139929" target="_blank">📅 03:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
گزارشات اولیه تایید نشده از رسانه های آمریکایی از بررسی وجود دست سازمان اطلاعاتی ایران در ترور ناموفق ترامپ توسط FBi آمریکا پلیس فدرال در حال بررسی این موضوع است و هنوز تایید نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/139928" target="_blank">📅 03:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یه کشتی تو تنگه موشک خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/139927" target="_blank">📅 03:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139926">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvPRB5DVJzZkzFqm0sPjYn7hc5TgZxxuPJ9USJOOdgUaMj0gMSZbCS4Xlujc0brBZ1v8CgPj1RSWNR-2kEABmBAqSLJCf17_oE64GdTFFLnsFwSovCkAY4AQ46Q6vsfqPay4hAzlho-zQPDuvGRKbqog7QcjuwoXfu_6-HNJRYsYEExX765dvNYBYbBQPPUnKrCp9wlEdsQ3b1ST1pSrjHiAhwHOfZSdp6CTR3sGx23-lhF0fjk79a5yb9wlYc7iVlQCTgUql8HAJNKZNj7PdwC-Lodqv0e4UlT4L0rqNSm5gThOS-dcgvEnYHGFx0M3fokQbjM0KAofAiCPh7y9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون دوبای
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/139926" target="_blank">📅 03:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAajKLwFCgbIP_YOFXghgfF1LQ3o7onQ8_TMCWGnnAjxipjj8lRK235ytHeU-NtMF461NadqkVF--D3507FOIm52Uk5eIwg1eT_ndqyAILaphBxQMrWUdLojXtVK6Utlb1kopVlr2Qrg6PReqiGCttFsVLdfDnYNlkXQmrav_6a7wqs1ki53qZ8apHOWr2lS3k1rao4ULZn0dYULMBOUULKSgJLGvEFgRtIQngKSxMm_9G42YG6hb2NCjqrs8aFk7NqfsuQz8qG-bGJs1Ac8AnaWZ1OEQ9MLyOLUPemowtPJVhcB5OAEATaCQPx3zdhIUEN5vOcNX6rVje5Px0rNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون های دود در دبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/139925" target="_blank">📅 03:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139924">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrHWvTaRWVgegaDdy1_g0mdXc4cf2QQ_nMTNPLgNwaxzxvhgHUNBYj8QO1nEOOhEGEW10nMy5shQECsZvM2iJIu0iV4lXl99ERaQUuBvy9Te8r9cY1x0GUP14cua_PsikKR4jLr02AMUy1gyz5e38BA1M0xW4iZ7KP2aeMtXmsDP7ciBKHQTqfk3dwe8qDngKMXRb2uFnmpOxAs5vdj1Yci5hhPGrJQZCKTs94Fj8cy4xei2O8Keef5-FdKWt5KeVDl4c5172H0PPvIR1dPmhYMUSW-77byfPMpa-KsndKfuWoPWH_uzqWe77eBrn_5PVr9JQStYnS-xotrcCTBjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارشات از انفجار کپسول گاز در دبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/139924" target="_blank">📅 03:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فاکس‌نیوز
:
یک فرد مسلح در زمین گلف ترامپ نشنال بازداشت شده است.
او متهم است که اقدامات امنیتی پیش از سفر ترامپ به این محل را زیر نظر داشته است.
پس از بازرسی خانه‌اش، مأموران موارد زیر را کشف کردند:
یک تفنگ با تغییرات غیرقانونی، خشاب‌های با ظرفیت بالا، جلیقه ضدگلوله،
و دفترچه‌ای حاوی نوشته‌های نگران‌کننده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/139923" target="_blank">📅 02:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سوءقصد به ترامپ ناکام ماند
زن مسلح با تفنگ AR، جلیقه ضدگلوله و مهمات بازداشت شد.
رسانه‌های آمریکایی گزارش می‌دهند مقامات انتظامی یک زن مسلح به نام «جینین جان تیل» ۳۸ ساله را در زمین گلف ملی ترامپ بازداشت کرده‌اند.
این زن ادعا کرده بود که برای نظارت بر آمادگی‌های امنیتی پیش از حضور رئیس‌جمهور ترامپ در محل حضور داشته است.
پلیس اعلام کرد در بازرسی از منزل او یک تفنگ AR که به‌طور غیرقانونی تغییر داده شده، جلیقه ضدگلوله، چندین خشاب پر، مقادیر زیادی مهمات و دفترچه‌هایی حاوی «اظهارات نگران‌کننده» کشف شده است.
مقام‌های آمریکایی در حال بررسی انگیزه و احتمال ارتباط این پرونده با تهدید علیه ترامپ هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/139922" target="_blank">📅 02:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139921">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مجری صداسیما: مردم میگن حاضریم کل زندگیمون رو بدیم اما انتقام اقا گرفته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139921" target="_blank">📅 02:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPUN77XciA8EJesLC5Up1KclRL7gyYWdPVSbYGDKseYyRNRD1jsZIo5z0b8GCJdiYlZfaGW9vUYbcmMqnXS2h_w2bisNtvN-76TIeNRlyw5zjC4dZxlMkqXtxkGoJJpixP1mwnW4vCiNARsL_LgUJpfBliwbrxW1H2ptilbQT-zXMaMhrOeiKfLL07w9EIhkowPOkoeo6yrKtNdyla4WWsw9cbFeDKZN5wtCnQ7UoeJxwaRYWlI4ICQZKRUbq3L8ACNU51_4__nAlPcjR3Nlap3AD9unz4ylYhHoyGKLKoz5UZpQL-quJxIARTbRgl71XdTKNPWfEugidE2VY19nbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSbA0-pNhAce2KmNkpArbKmEwPK2GLIYMEwX4GKfEdAJwBN1iIBKDOp5gZgJ4J23thYPBXTp_7RD5TNpJmS-ZI5mRrNuAnedWSqVQF9_bXOAcRAh1TUQUTVYCiVesTt68F8sbkz-3X11Yj5wo9RN9wXyX6juVO_1Ri3iLlzi3i421BzxVwDEkHl6gVUvE9e_nyH6VSYQ7IABRhkn9DHx3-oIAKIOt2cN1jLlTfshdwEG69gVCq1knbZpkoBxc51wZRlDyThOfPSIBzjWKWcatgzIiRWFt-7mJ6ks89UMLuy7-o-q8Q7W3RODmY8cmJLkXjdUWwfyPjPzGgSIawt2GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=mz_hNQMBuxgRlhEt8xrPf0R_CXoc9xbmHwepWmR5UFPd5eOd_d4xRkI-fbLHysK51Q_z6lQNGqAwtI_h0tw259x6iUJ5srATc6QfNYc8IcnVp3QMp_a76PgCFwdLK4gCAZAZNWjIYpKdwPfeJFya3K9EWxSdMeD8ZRIYBMo4_Z8Tcu5Gxqz9r2rbN11ybs9EsUDcWNrdTxCjCmD702nFs_ZbwimLUog9B-OLZpu3QFDvIjqyb-UxyWXZSEiLfWHtIK6TuLicsk21o_k8oXrHLRjemOe5zd-qDE8CzHPRihJs2SS0nvlZmLyJ9PW5xZEz6WLjM4kx3YSFNKrQpyM2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=mz_hNQMBuxgRlhEt8xrPf0R_CXoc9xbmHwepWmR5UFPd5eOd_d4xRkI-fbLHysK51Q_z6lQNGqAwtI_h0tw259x6iUJ5srATc6QfNYc8IcnVp3QMp_a76PgCFwdLK4gCAZAZNWjIYpKdwPfeJFya3K9EWxSdMeD8ZRIYBMo4_Z8Tcu5Gxqz9r2rbN11ybs9EsUDcWNrdTxCjCmD702nFs_ZbwimLUog9B-OLZpu3QFDvIjqyb-UxyWXZSEiLfWHtIK6TuLicsk21o_k8oXrHLRjemOe5zd-qDE8CzHPRihJs2SS0nvlZmLyJ9PW5xZEz6WLjM4kx3YSFNKrQpyM2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات بسیار شدید و بی سابقه موشکی روسیه به کی‌یف اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/139918" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNmFw_CKOEkzSdFDazXP8onT6ZXHQxlYnUP3jEAFlwKtylEo0noVinM3ocCZ91pOBJQJJ0jNaNBJzTxyz6gIBi6hVz-f7hN4sUfS9XHveVesup8ge0He1pgkiHkq36gPXmOX-cJxGTYVGCbJ80ZK3R5n8Cs86aLbyFVgzkIEMBJ5epkaSkNcZp0Q5dWDkW7sw5k-MzjUAcslW_Kd6LbESGo-77lZHhOoo2fP6sPlLGyyK2mizE0CSfnq-PU_vehGO8IsSvG1oJx1qvjBCiG_vjXW41DeTTRdWBUcAXoqqWxMPZ4mrQ5NqNLUnMH4UkaFX9BwonTT0lDIl7nfE9ajcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست، وزیر جنگ آمریکا، خطاب به CNN، درباره کمبود ذخایر موشکی
:
اون خبرتون حقیقت نداره، خجالت بکشید شرم بر شما
ما باید خیلی بیشتر از این رسانه‌های جعلی بدمون بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/139917" target="_blank">📅 01:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش آمریکا اعلام کرد طی سه ماه گذشته، حدود هزار کشتی با کمک نیروهای این کشور از تنگه هرمز عبور کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/139916" target="_blank">📅 01:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرنگار المیادین در اسلام‌آباد به نقل از منابع اعلام کرد که در حال آماده‌سازی یک یادداشت تفاهم دوم هستیم که به عنوان پیوست به یادداشت تفاهم اول خواهد بود و تنها به تنگه هرمز محدود می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/139915" target="_blank">📅 01:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
مهلت ۴۸ساعته ترامپ، ۲ساعت دیگه تموم میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/139914" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b407081b1d.mp4?token=Iw7sZoGO9S2U7fOYDDgXlrMEMejGOtbarsuGPq-zNc8WTcyng9x9FM5oOHW914MUVaEp57QLRbQQ2DfMO6t50mKMSoDFPFEM-4fNkk0vwalAjDS6lf3X1KzyplOtPfEfdkvY2w_dxLKjoxHmyd6rN2X0NnT9ccojCXmONKIef_gSsTBEXkRBuswo5aSx0bsDi3yFf8ge87PnSP0JfdsrNdIRON-cJ3d8gg-HYqEwPRa5GHRvlT9GOsMDVFQsz1cVe8HBbKkSkdLqIPOkdtYk3ChmdosWFUurZBI1CIboMIZdpJW9-2sJ1puhvPicMFJyErgCdm0b83iu3eAyWDOyzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b407081b1d.mp4?token=Iw7sZoGO9S2U7fOYDDgXlrMEMejGOtbarsuGPq-zNc8WTcyng9x9FM5oOHW914MUVaEp57QLRbQQ2DfMO6t50mKMSoDFPFEM-4fNkk0vwalAjDS6lf3X1KzyplOtPfEfdkvY2w_dxLKjoxHmyd6rN2X0NnT9ccojCXmONKIef_gSsTBEXkRBuswo5aSx0bsDi3yFf8ge87PnSP0JfdsrNdIRON-cJ3d8gg-HYqEwPRa5GHRvlT9GOsMDVFQsz1cVe8HBbKkSkdLqIPOkdtYk3ChmdosWFUurZBI1CIboMIZdpJW9-2sJ1puhvPicMFJyErgCdm0b83iu3eAyWDOyzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری هندی تلوزیون: باید تا ابد با کل دنیا بجنگیم
🔴
پ.ن: خاک بر سر مملکتی که یه هندی بشه تصمیم گیرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/139913" target="_blank">📅 00:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ:
بازار سهام به بالاترین رکورد خود رسیده است زیرا سرمایه‌گذاران متوجه شده‌اند که آمریکا در حال برنده شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/139912" target="_blank">📅 00:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از دو منبع
:
ارتش آمریکا نزدیک به ۸۰ درصد از موشک‌های رهگیر سامانه تاد (THAAD) و حدود ۵۰ درصد از موشک‌های رهگیر سامانه پاتریوت (Patriot) را استفاده کرده است.
🔴
کشورهای حوزه خلیج فارس نسبت به کمبود سامانه‌های دفاع هوایی ابراز نگرانی کرده‌اند؛ مسئله‌ای که بر توانایی آن‌ها برای مقابله با پاسخ‌های ایران تأثیر می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/139911" target="_blank">📅 00:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f44155df6.mp4?token=lAzk6kP994FWEI_6Drk7NkPLRqQa2HwmfUAxHspEQQN_0OhFWec3NijUXIj0cFUBQya9Grhi_-25ty1eyCYuE4HtO30mM24NhVolrMn96boPO5JV6uBn18fkf9V6szmJRWhSUmkVTPeofBxxhka1JUjB2aAoBdJKnfuBM6LBBdHY6B-b86qy8tWqxCYDfrHOOE0h6kyEC7HGdI0YoH_jFLl194-yA-RseRlT82LTCT2E_D5jRpJNp2Pp-bQFQX3XUsI-xVuW8YWD_6R1B90jhsVUsVNGUhQOYn2mWTgVy0dYuR0yiP13RnNuVwkFxlSkB_NftXUq8b11mQSXi_cw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f44155df6.mp4?token=lAzk6kP994FWEI_6Drk7NkPLRqQa2HwmfUAxHspEQQN_0OhFWec3NijUXIj0cFUBQya9Grhi_-25ty1eyCYuE4HtO30mM24NhVolrMn96boPO5JV6uBn18fkf9V6szmJRWhSUmkVTPeofBxxhka1JUjB2aAoBdJKnfuBM6LBBdHY6B-b86qy8tWqxCYDfrHOOE0h6kyEC7HGdI0YoH_jFLl194-yA-RseRlT82LTCT2E_D5jRpJNp2Pp-bQFQX3XUsI-xVuW8YWD_6R1B90jhsVUsVNGUhQOYn2mWTgVy0dYuR0yiP13RnNuVwkFxlSkB_NftXUq8b11mQSXi_cw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چه بر سر این مردم داره میاد
😔
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/139910" target="_blank">📅 00:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwTmaUig-nv6fcOkNsQuRwmR6opDtKgEameo6WyS0dchYSpsu5BMUGiFX9pdrEmBION9kyCU0FaomksPhS7i3YerYJqXQLUxX977xJUqOyCuzCHWZQ8TRuXV7zDJ2OR6rwOOo66KumHInVmW5lxQMhkUYdygcJMt3GO_gwRf79ndQewPmaaDBYsxRoFExNuYCgBmAOJIM1vKdO31-1MK8m-ICJQ7UClpAzwyQjzcPfrYqpcv56rKsVMX3nVVyIq058qylwHJTj06Hh009ryYm98KjaPfKQHuH_YXdZCaRWlBPh2le2vjDsQHoSO8udXawuwQni7kp3OsxNso31iWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tefuq-7570Sb9-y6ssCHyi-uI0GcYWHlGuaJek1Cpwf93ZIf9BweHnFS9fpU1WOZn-EkPut-mF74lKjW8dFtYD7N5vEiV4G1algeA795Qm7aLe2tXJNU5Ba3HMKvFwnt2wrayKkYBVZLFiasWXZSu_03W6AXPdQBFVQLvE0XqEQgOwDtY8hHOmkfon4eP5DdcoV8VrvT1ZzqIhhSKYOkxuGNZYANpgXSXag1eOpHL4jU2MAVImvWYVaYtnabxRhoag2xROaNM72pQm5vqI4Yw-rYansjQ8sdWqMpP0QamtWA8TlbgHgvPmZaC76Vbr6-hptLMjuRLl7ZVUoltdPL_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مراد ویسی؛ تحلیلگر:
ایران سال ۱۳۹۷ امضا کرد که سهمش از دریای خزر فقط ۱۱ درصد باشه و‌ بقیش رو‌ فروخت. اینو به مردم نگفتن و الانم میخوان دزدکی توی مجلس تصویبش کنن.
سهم ایران از همه کشورا کمتر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/139908" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCX71MfGE4wfQMEKgttJZitSNs0-oez3m2N04ovkZs_Z2QztQ00FwOW0d0g7YHq8AA3-N7VYXnxH9tROSEyLM63sPEGDCroNcwq3fWsAybxvGPpcis6PK8r7Ig9h-wGlAPbh5tHD8L3U5Pe0KXObXdq1lb9tIF7TfXp1EvZgd3r2aCcVUc3dv4XFCFaPtSynpNrCvF3Pwu-tA9VOSNp36-7HBBjq2FthNtT-1aiwWFn-uxrc8O8EDKah_yEngc6Vf5Gq4TblvsL9xb66AclW7o7jybqXy8E1WDga_pihOXDhhQCR9xvs4jV_l4E67zxxODNw91JsdfiYEsV8PkdqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اوکراین پهپاد‌هایی رو به سمت روسیه فرستاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/139907" target="_blank">📅 00:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت خارجه  آمریکا اعلام کرد که ویزای یک دیپلمات ارشد برزیلی را که در واشنگتن بوده، لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139906" target="_blank">📅 23:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139905">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شورای اسلامی: تجمعات شبانه تا پایان صفر برگذار میشه و بعدش رهبری دربارش تصمیم میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/139905" target="_blank">📅 23:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139904">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
به گزارش شبکه المیادین، ارتش اسرائیل اقدام به یک انفجار شدید در شهرک حداثا در بخش بنت جبیل استان نبطیه در جنوب لبنان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/139904" target="_blank">📅 23:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt7gLK6xZTAGkniRY_qTLRSYhplZpjSpMlHRyLXesO7nNjjFigxoTpLS9uuZ0MhzS7pM6Il11fHw657faab2ZdB1crAGeeNjQe3G4n-jj5cCiFdLGOOUeKIBs3xXUKcR30V9tielv53EbrJUI9OsDf-FrCU6j_JlrfOizp69Eh2C088m6XDhcnrBES4zRPPmKTsU8oKSqHc9b3eSFgSBQp73ixFn4IiVGIZvX9-P96bQjdrVr50Hxw9V3sSBl3aHCEpnOgMynpqAanopABXdAtLELuT6HXyhvJ3PATtggzAA3bBeNzRXmFVhhPIMp6gLsOicilKTVHXnVP1wpWiMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتیجه نظر‌سنجی کانال 14 عبری از انتخابات اکتبر ( مهرماه) اسرائیل
🔴
احزاب راست افراطی و راست میانه‌رو به رهبری حزب لیکود: 61 رای
🔴
احزاب چپ محافظه‌کار و چپ افراطی به رهبری ایزنکوت:  48 رای
🔴
احزاب راست و چپ عربی: 10 رای
🔴
با توجه به این نظر‌سنجی و در صورت تثبیت آن با توجه به ائتلاف راست‌ها با اعراب مجددا احزاب متحد با لیکود(نتانیاهو) اکثریت کنست را به دست می‌آورند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/139903" target="_blank">📅 23:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت ملی اسرائیل، پس از رد شدن ایده بردن کروکودیل به زندان ها ، توسط دستگاه قضایی اسرائیل، از این دستگاه انتقاد کرد و گفت در انتخابات پیش‌ رو، در صورت برنده شدن، این اصلاحات را در مورد زندان ها پیگیری خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/139902" target="_blank">📅 23:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قیمت نفت خام برنت با ۵.۲۶ درصد کاهش به ۷۹.۳۶ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/139901" target="_blank">📅 23:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اسرائیل شهر حدثه در جنوب لبنان را بمباران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/139900" target="_blank">📅 23:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
تلگراف: ایران در حال بررسی ایجاد یک «صندوق داوطلبانه» توسط کشورهای خلیج فارس و برخی از اعضای اروپایی برای پوشش ناوبری، حفاظت از محیط زیست، جستجو و نجات و سایر خدمات در تنگه هرمز است.
🔴
این طرح که مورد حمایت عمان است، از چارچوب تنگه مالاکا مبنی بر درخواست از کشتی‌ها برای پرداخت سهم داوطلبانه الگوبرداری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/139899" target="_blank">📅 23:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7805dff906.mp4?token=LIe6ty5C3FYQlav0yIA3Ky5g6GtYjfLLNwlHeZsh5AZaLt4aUeRtZzzee08Vvu7mfHJ_Fqt9xI3ZP16VlmbBFWbXWaS4UrxnMDq1FnPQbpjLU1IlzP6RggZGe1uVasOdBBIQe9Gtg1yTglZCxAMwblTp1DFhuQOnF8EdmEqORQtOQugbHelMj__1vdMPsQ6w4Mnii-Z-K1-CqUFWpkMcSdDWFREATi8N4gB7QC5vKOi0yICL1eYuA9_X46C1RxEtBIo96CqWmQfoYeRC3H1V-kMX1ETATgSpDscujxs0ltQzWwKhm3tz4vzKsii-Wjd3Q70kjpZEVONnpozL8PC-LrfpERWCYJ0ozdL1oROEctI6_4aQWfVY71oK01OOfV0b7ZWzeMVNTqBcQWd-TP-V3slPUN4udio3CdvQYJPsM2yOUqmQWUm5w7RoRpwf8r4HLJKDY0UHYjTZIIW8jV5Kwv_1ukqvdvvF9oO-8kyui1a7Iks6uLo6ayYEuJidGP9i_AMmAKnV31WbV6t5EmNN3iWnoHdTiU8gZvCa5zp9gLe9sQPZt6UnOW-oTyWh7ObhzBTZQu0T8Ya4QY1iSGkd-t1gfl02BdNEC0i3xgfimf71doRjdDy6pE5AZqLyUibRxwR7NIfbU-NtlDsaFBRCnK5u3mgis9ceq08mlyOlWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7805dff906.mp4?token=LIe6ty5C3FYQlav0yIA3Ky5g6GtYjfLLNwlHeZsh5AZaLt4aUeRtZzzee08Vvu7mfHJ_Fqt9xI3ZP16VlmbBFWbXWaS4UrxnMDq1FnPQbpjLU1IlzP6RggZGe1uVasOdBBIQe9Gtg1yTglZCxAMwblTp1DFhuQOnF8EdmEqORQtOQugbHelMj__1vdMPsQ6w4Mnii-Z-K1-CqUFWpkMcSdDWFREATi8N4gB7QC5vKOi0yICL1eYuA9_X46C1RxEtBIo96CqWmQfoYeRC3H1V-kMX1ETATgSpDscujxs0ltQzWwKhm3tz4vzKsii-Wjd3Q70kjpZEVONnpozL8PC-LrfpERWCYJ0ozdL1oROEctI6_4aQWfVY71oK01OOfV0b7ZWzeMVNTqBcQWd-TP-V3slPUN4udio3CdvQYJPsM2yOUqmQWUm5w7RoRpwf8r4HLJKDY0UHYjTZIIW8jV5Kwv_1ukqvdvvF9oO-8kyui1a7Iks6uLo6ayYEuJidGP9i_AMmAKnV31WbV6t5EmNN3iWnoHdTiU8gZvCa5zp9gLe9sQPZt6UnOW-oTyWh7ObhzBTZQu0T8Ya4QY1iSGkd-t1gfl02BdNEC0i3xgfimf71doRjdDy6pE5AZqLyUibRxwR7NIfbU-NtlDsaFBRCnK5u3mgis9ceq08mlyOlWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ چندی پیش، به سمت لس‌آنجلس رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/139898" target="_blank">📅 23:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7PijcCGQ41LLwk5k9rAnmKYs8gH9B8astoKWzl1H_kvAxXOhBIDWB7lcfVDGplrTd8r-TqlO4pAYNZQkeB-6_2XdzR9vNLgbxnBLkqA3SNZ-M49m_AXlntv0t2Oos7fyfqn4MmOcMNrBL8T5a3O8oNCk5qL1xK_f0WMz1PiCz2cbFjcXrktF3KpzZDbmO9BP2IUI9ygxmO14J2Crsq6GP2Y-ikMg7HFzCgjoItJYnXT0aL1TNh7ATLNVSiQ72W6pJsiz6rO5HprLggTLwy0dfFNxT9YKcNo3nJ1rXaZFpZuGqnQJ71RrQTTYc6MpjDYgdqzDNedVUR89UUCM1QMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی یه حرکت غافلگیرانه اپلیکیشن بله وارد اپ استور شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/139897" target="_blank">📅 22:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت‌وگو با شبکه الجزیره ادعا کرد:
🔴
ترامپ همه ابزارهای قدرت را در اختیار دارد.
🔴
هرگونه مسیر موقت در تنگه هرمز بدون مانع، مجوز، تأییدیه یا دریافت هزینه خواهد بود.
🔴
تنگه هرمز یک آبراه بین‌المللی است و هیچ طرفی بر مسیرهای آن یا توانایی عبور از این گذرگاه کنترل ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/139896" target="_blank">📅 22:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نتانیاهو: ترامپ معتقد است که می‌شود غزه را عاری از سلاح کرد. تا خلع سلاح شدن حماس از خطوط استقرار در نوار غزه خارج نخواهیم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/139895" target="_blank">📅 22:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فرماندهی مرکزی ارتش آمریکا (سنتکام)  با انتشار بیانیه‌ای اعلام کرد ناو آبی‌خاکی باکسر(Boxer LHD 4) در چارچوب حمایت از محاصره دریایی علیه ایران در منطقه فعالیت می‌کند.
🔴
سنتکام همچنین اعلام کرد تا تاریخ ۱۳ مردادماه ، نیروهای آمریکایی ۴۵ کشتی تجاری را که قصد عبور از این مسیر را داشتند دستور تغییر مسیر داده است، دو کشتی را از کار انداخته و دو مورد دیگر را نیز مورد بازرسی قرار داده‌اند.
🔴
این اقدامات در راستای اجرای سیاست‌های ایالات متحده برای کنترل تردد دریایی و افزایش فشار بر ایران در منطقه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/139894" target="_blank">📅 22:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
المیادین به نقل از رسانه‌های پاکستانی: محمد باقر قالیباف، در دهم آگوست [۱۹ مرداد]  به پاکستان سفر می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/139893" target="_blank">📅 22:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvZJgcUGT4C3fnutglwKPo_d4FNW_3_6a1CqzTW-FbJ44B2QlwphG4vw3m7QAWdUgrgs1e9ugyKmlCT2ccpBgiZ_P7ifNjT1j57ZzZYQFeZkhISVslaeCU7X-lbZ0Ie76h8UAnPI3T_Qo9YmpGZMohtF-Efu_hsdgv2mt954RKFEFCRqA7fXOJ6B8-86hzyw6yrl-8dDab556LPUeK418E-mCtirsNOemk8M3gQ03s7ttrRe_nNvSh4eICMH4Lw2U7MPSgtR5Fuev-43O4TSv4HuBK5lBIqIUmxfewGh0cj52iQaapowPQ6jpswzsl4xx88R0fieBYBYpF0qZzpy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تناقض رفتاری بسیجیان
‼️
🔴
بسیجیان دانشگاه شریف که قبلاً به دلیل اختلاط در سلف دانشگاه اعتراض داشتند، اکنون در مراسم اربعین با خوابیدن مردان و زنان در کنار هم مشکلی ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/139892" target="_blank">📅 22:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
الجزیره : گزارش‌ها مبنی بر اینکه ایران به عنوان بخشی از یک توافق احتمالی، ترافیک تنگه هرمز را کنترل می‌کند، نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/139891" target="_blank">📅 22:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
خبرگزاری فارس به نقل از یک منبع نزدیک به تیم مذاکره کننده ایرانی: تهران تنها در مورد ترتیبات آتی برای مدیریت تنگه هرمز با سلطان نشین عمان مذاکره می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/139890" target="_blank">📅 22:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت و گو با الجزیره : گزارش‌ها مبنی بر اینکه ایران به عنوان بخشی از یک توافق احتمالی، ترافیک تنگه هرمز را کنترل می‌کند، نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/139889" target="_blank">📅 22:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e43f241f.mp4?token=m5J-bkBZcrqzz53m7NKesOkm1VV0VSfJ1J-aVaZODu9YRJjKh-vPPgN5MqXqxsziCAi7dCy6jMYogF35u41QvTWAZQ3vEVScZmO2XOHbd5x4_GIi4jbJ5ki5N9RCKbjIJdHICoHQnLnpZ2PWEL6XiFwx2DY_Md7uHyGk7bDqHP3c3ek4JHwB9gbXcysdY6dlRg0xWeioGZcBYw4_Vx2JaRdhx4I5Pe4KjUhm5Nt77vmUnv8zjl5XhjspK8rNpB6yt_Kxzv9uhDN45uWzopZ1lPbjNiLzWy-b4TLc-wjv3XBB6ziVnIiJ_oijq_eHN6xIDz35wP1cXkTdpz1sOP4Ukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e43f241f.mp4?token=m5J-bkBZcrqzz53m7NKesOkm1VV0VSfJ1J-aVaZODu9YRJjKh-vPPgN5MqXqxsziCAi7dCy6jMYogF35u41QvTWAZQ3vEVScZmO2XOHbd5x4_GIi4jbJ5ki5N9RCKbjIJdHICoHQnLnpZ2PWEL6XiFwx2DY_Md7uHyGk7bDqHP3c3ek4JHwB9gbXcysdY6dlRg0xWeioGZcBYw4_Vx2JaRdhx4I5Pe4KjUhm5Nt77vmUnv8zjl5XhjspK8rNpB6yt_Kxzv9uhDN45uWzopZ1lPbjNiLzWy-b4TLc-wjv3XBB6ziVnIiJ_oijq_eHN6xIDz35wP1cXkTdpz1sOP4Ukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ناصر هادیان، استاد برجسته روابط بین‌الملل: اگر از این مرحله عبور کنیم، ایران در شرایطی قرار خواهد گرفت که شاید در  سال قبل تا حالا سابقه نداشته
🔴
نسل ما نتایجش را نخواهد دید ولی نسل شما این نتایج را خواهند، دید یعنی کشوری پر رونق، توسعه یافته و قدرتمند
🔴
این محقق می شود اما به دو شرط؛ یک توافق انجام شود و دوم شعور متعارف به خرج دهیم، یعنی عقل زیاد هم نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/139888" target="_blank">📅 21:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
دیوان امیری قطر: امیر قطر در تماس تلفنی که از سوی رئیس‌جمهور آمریکا دریافت کرد، درباره تلاش‌ها برای کاهش تنش میان واشنگتن و تهران گفت‌وگو و رایزنی کرد.
🔴
امیر قطر در گفت‌وگو با ترامپ، تلاش‌ها برای نزدیک کردن دیدگاه‌های واشنگتن و تهران با هدف تقویت روند دستیابی به یک راه‌حل و توافق را بررسی کرد.
🔴
امیر قطر بر اهمیت گفت‌وگو، بهره‌گیری از راهکارهای دیپلماتیک و پایبندی همه طرف‌ها به مفاد یادداشت تفاهم تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/139887" target="_blank">📅 21:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139886">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سپاه هرمزگان: از فردا به مدت ۷۲ ساعت، انفجارهای کنترل‌شده برای امحای مهمات عمل‌نکرده در اطراف بندرعباس انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/139886" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139885">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73386ecd9d.mp4?token=XklO8gEiarSlsmHWA-6HqaInlUohlDetAbZ46gcefnwnqxkzrIMqlttWSJnBYbUxbCM7BMA4YP7r2CLkPYwqamK--dKW-sNucwL_bPlXf9n7tiulF5MdWTyuC0GforOXlHitu2rmkFjO5t_1pw8h0-x4mmhfgVVSE9y-m-dzuma8ZOI1yveJx0VaC6ZjYxNHgkevkGSjfVweEYJ_x-9gY1viJvqW2H2bILsWJDPlJcx7wyb8alS1qH-BFQx2PovuH8rfYaB1xzuvTdZ8bkZtIa7at4RUutxszn_hmd9z3yfptcUcLjU3xWPZE63cQ1r-gsy1eqTBlQ2lsojXmootpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73386ecd9d.mp4?token=XklO8gEiarSlsmHWA-6HqaInlUohlDetAbZ46gcefnwnqxkzrIMqlttWSJnBYbUxbCM7BMA4YP7r2CLkPYwqamK--dKW-sNucwL_bPlXf9n7tiulF5MdWTyuC0GforOXlHitu2rmkFjO5t_1pw8h0-x4mmhfgVVSE9y-m-dzuma8ZOI1yveJx0VaC6ZjYxNHgkevkGSjfVweEYJ_x-9gY1viJvqW2H2bILsWJDPlJcx7wyb8alS1qH-BFQx2PovuH8rfYaB1xzuvTdZ8bkZtIa7at4RUutxszn_hmd9z3yfptcUcLjU3xWPZE63cQ1r-gsy1eqTBlQ2lsojXmootpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز روس توی دونتسک لخت خوابیده بود و داشت افتاب میگرفت که ......
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/139885" target="_blank">📅 21:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139884">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ipJvIYXm6KqDK0ZwPbZn90UY0lIsc9f0_j1KvdfN6bCtUXI57pr4P6VGdzZEQOqqsnaCiA4rW-C4xPHHKwLj5Gr2-kIJq5FrKTDNhthadZfp8ct6qg2Gyg13jC6lh9SG0OO2XWUZm26UUd_JFbz4pz7ZuBz0rSq8WHYjGUsKStOXvouRr0aRZCC8O4prRsVnzxOklba_AYQ1FEKjwsonqR-XvpGwVsk7jm7TWQVyNkf_2bBobruLxbBeW3Os4fs5-wuRzET_D5IVg-GyNLkl_K2f7asX9ngb2Ep5v7phg5rZGPoOMYThh5ro5uoLLxG4Jp0PfjZXkbOowBomdrixOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهای نفت برنت با افت ۴.۷ درصدی به ۷۹.۸۷ دلار در هر بشکه رسید. همزمان بازده اوراق خزانه‌داری ۱۰ ساله آمریکا نیز از ۴.۷۰ درصد در روز دوشنبه به ۴.۶۴ درصد کاهش یافت.
🔴
به گفته تحلیلگران، در حال حاضر اخبار و گمانه‌زنی‌ها درباره احتمال توافق با جمهوری اسلامی مهم‌ترین عامل تأثیرگذار بر بازارهاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/139884" target="_blank">📅 21:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139883">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
۱۸ نفر بر اثر انفجار در شهرک شمس آباد مصدوم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/139883" target="_blank">📅 21:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وال استریت ژورنال: به گفته یک مقام ارشد، ایالات متحده و دولت‌های منطقه درخواست ایران برای دریافت هزینه را رد کردند و در عوض خواستار تضمین‌هایی شدند مبنی بر اینکه نیروهای نیابتی ایران به قلمرو آن‌ها حمله نکرده یا آن را تهدید نکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/139882" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رویترز
:
منابع آگاه می‌گویند دولت ترامپ در حال تدوین طرحی برای ممنوعیت استفاده از تجهیزات چینی در مراکز داده (دیتاسنترها) است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/139881" target="_blank">📅 21:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139880">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: ساعات حساسی در پیش است که ممکن است چندان طولانی نشود (شاید حداکثر برآورد، فردا باشد) تا وضعیت تنگه هرمز و هرگونه توافق احتمالی مشخص شود.
🔴
این موضوع مستلزم آن است که واشنگتن در محاصره دریایی و تحریم‌های نفتی تجدیدنظر کند؛ اقدامی که ممکن است انجام شود.
🔴
این مسیر راه را برای بازگشت به تفاهم‌نامه و مذاکرات هموار می‌کند؛ و شاید به برگزاری یک نشست در آینده نزدیک یا تمدید اجرای تفاهم‌نامه منجر شود، زیرا این تفاهم‌نامه در ۱۷ اوت منقضی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/139880" target="_blank">📅 20:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: مذاکرات بین اسرائیل و لبنان در رم تا ۶ آگوست ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/139879" target="_blank">📅 20:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: اسرائیل مستقیماً از دولت آمریکا درباره روند دیپلماتیک با ایران به‌روزرسانی دریافت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/139878" target="_blank">📅 20:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فاکس نیوز: یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/139877" target="_blank">📅 20:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر حمل و نقل هند:  کشتی باری هندی به نام "فایزه نورع لییا" در نزدیکی آب‌های یمن مورد اصابت یک پرتابه قرار گرفته است که منجر به واژگونی و غرق شدن این کشتی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/139876" target="_blank">📅 20:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز: ایالات متحده در جریان جنگ با ایران تقریباً از تمام موشک‌های تهاجمی دقیق خود استفاده کرده است. ذخایر موشک‌های ضدتانک و موشک‌های تهاجمی هدایت‌شونده و دقیق این کشور تقریباً به سطحی بسیار پایین رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/139875" target="_blank">📅 20:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه : مذاکرات تا الان تو سطح فنی و سیاسی مثبت ارزیابی شده
🔴
ایران با عمان در حال کار برای تنظیم سازوکارهای مدیریت تردد کشتی‌ها تو این آبراه مهم هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/139874" target="_blank">📅 20:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a445c24fe6.mov?token=GbZuWXnYjBaBx9C4npR-jkyBZgSYn6Jbq7NZzMrRkk5o8_ElvDvY5oi1yLyDFryyP9F1GQZsjU4tUK0RqZcunLxwbrHwH33KYXrIjyxlPz1hADAq6H8-DQpB0sToqjDMXL7DaBN814h2qiYxng0457gujm822RDaACjDwaWxpVduJ7L-uS90PqRUh-BsGTcNtynKD26GcY0d1_UpxSqF2S8ktRDswJbULGOdRCB7ZvmSYTyGH9H5AHM6JwGxWN5tbo1v7P3gOs3Z2L3zgiRI5w0rgV0QyBkb56d9FNGfcsxu7NZp2-6Zd0v_ZZ4akLG5jJrOsE4pmS-89X8yOpXAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a445c24fe6.mov?token=GbZuWXnYjBaBx9C4npR-jkyBZgSYn6Jbq7NZzMrRkk5o8_ElvDvY5oi1yLyDFryyP9F1GQZsjU4tUK0RqZcunLxwbrHwH33KYXrIjyxlPz1hADAq6H8-DQpB0sToqjDMXL7DaBN814h2qiYxng0457gujm822RDaACjDwaWxpVduJ7L-uS90PqRUh-BsGTcNtynKD26GcY0d1_UpxSqF2S8ktRDswJbULGOdRCB7ZvmSYTyGH9H5AHM6JwGxWN5tbo1v7P3gOs3Z2L3zgiRI5w0rgV0QyBkb56d9FNGfcsxu7NZp2-6Zd0v_ZZ4akLG5jJrOsE4pmS-89X8yOpXAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک سرباز چترباز روس در جریان جشن روز نیروهای چترباز در نزدیکی مسکو جان خود را از دست داد، زیرا چترش باز نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/139873" target="_blank">📅 20:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c2f667a2.mp4?token=k12cr7rbleiMpa1hSlaX0C2aaZzcBs5BSYkQIg4on5YFVPqWucXtJuyIGbmllfSxBg_3uecyshwAcO9bFkTkammejetFDOOMShUXohNdAaUuAuUOrx0_fVFbDnAdhtPCF32GjDKF0v7SRqkJs9rrPAj4KGEmZUftnA2cV39fqmJ18YribfZoGdP6q0Ct-QdNuYz5_KIdUR8-WasWemtooOBPTVUyT2f1Q50IeExSl6UzQkyQ4H9GIsGF6wczQlaUdMqTcAFVERT_iYsR5d0bnIhqCp28osHg5tsbEJ-kOpk3EjW-vuMPTtF1NqcVIpRlFkKC0V_rkdPhgCoMlI2d8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c2f667a2.mp4?token=k12cr7rbleiMpa1hSlaX0C2aaZzcBs5BSYkQIg4on5YFVPqWucXtJuyIGbmllfSxBg_3uecyshwAcO9bFkTkammejetFDOOMShUXohNdAaUuAuUOrx0_fVFbDnAdhtPCF32GjDKF0v7SRqkJs9rrPAj4KGEmZUftnA2cV39fqmJ18YribfZoGdP6q0Ct-QdNuYz5_KIdUR8-WasWemtooOBPTVUyT2f1Q50IeExSl6UzQkyQ4H9GIsGF6wczQlaUdMqTcAFVERT_iYsR5d0bnIhqCp28osHg5tsbEJ-kOpk3EjW-vuMPTtF1NqcVIpRlFkKC0V_rkdPhgCoMlI2d8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از یه خانم که ازش مصاحبه میگیرن: هوش مصنوعی ایرانی بهتر از امریکاییه، اصلا مگه آمریکاییا سواد دارن که بخوان هوش مصنوعی درست کنن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/139872" target="_blank">📅 19:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه :
مذاکرات تا الان تو سطح فنی و سیاسی مثبت ارزیابی شده
🔴
ایران با عمان در حال کار برای تنظیم سازوکارهای مدیریت تردد کشتی‌ها تو این آبراه مهم هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/139871" target="_blank">📅 19:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فارس: از زمان اعلام آتش بس در غزه، اسرائیل ۴۰۰۰ بار آتش بس رو نقض کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/139870" target="_blank">📅 19:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بلومبرگ: ایران بارها به طور علنی اعلام کرده است که اجازه نخواهد داد کشورهای خارجی در عملیات پاکسازی مین در این منطقه حیاتی که مرکز حمل و نقل نفت و گاز مایع است، شرکت کنند.
🔴
با این حال، در جلسات خصوصی در هفته‌های اخیر، تهران موضع خود را تعدیل کرده است. این موضوع توسط دیپلمات‌هایی که با شرایط این گفتگوها آشنا هستند و به شرط ناشناس ماندن صحبت کرده‌اند، فاش شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/139869" target="_blank">📅 19:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دو زمین‌لرزه ۳.۹ و ۳.۵ ریشتری هرمزگان را لرزاند
🔴
نخستین زمین‌لرزه ساعت ۱۶:۱۰:۱۴ امروز حوالی سردشت و دومین زمین‌لرزه نیز ساعت ۱۶:۲۲:۱۶ در مرز جزیره قشم، خلیج فارس و جنگل‌های حرا، حوالی لافت در استان هرمزگان رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/139868" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فرماندار ری: آتش‌سوزی در شهرک صنعتی شمس‌آباد اطفا شده و آتش‌نشانان در حال لکه‌گیری هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/139867" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139866">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک مقام ارشد ایرانی:
رسیدن به توافقی با عمان در مورد تنگه هرمز، در صورت توقف دخالت‌های آمریکا، امکان‌پذیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139866" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
انتشار گفت‌وگوی مهم پزشکیان با مردم عقب افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/139865" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یک نفتکش هندی در جنوب یمن هدف شهپاد قرار گرفت و در اثر انفجار غرق شد.
خدمه کشتی توسط گشت دریایی یمن ( مخالف حوثی ها ) بدون جراحت نجات یافتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/139864" target="_blank">📅 19:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6wWO974Pry9q7BszH10DrGqNJT3aaxtf9pVFHwowYPS4IKjCfy50yAMqIEv2DCPd__de2EGA7-DkyslreQoYp-hmhmLvg6Igj5IpA-EpplltFOU_0a6eylbYrqyBWv25o8Zwu9DcYZbyehzJHHKFO036MDI_JwfzhqdonWI3b93QDqkmMODYT4c7WIqjxeDnMV0RI3HUm5XDvYO19_Ndeo3F6RGfC4MgLXwDvj_y9r57ufV-gklbbDS_6mP4NncL7euSkVsAUZymiE77BUJnz5Hf3E5tZOe2NBYCIRBRbJN1DX21WyVw2_-83EfASGynBc4wMHZ-U6yA-FqK2tkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاتریک وینتور، دبیر دیپلماسی گاردین:
‏ به نظر می‌رسد عمان، تحت فشار آمریکا، اروپا و عربستان سعودی، در حال پذیرش مسیری برای بازگشایی تنگه هرمز است که تا حد زیادی با ابتکار ایران طراحی شده است.
🔴
‏ بر اساس این پیشنهاد، مسیر عبور کشتی‌ها به گونه‌ای خواهد بود که ایران همچنان کنترل غالب را بر آن داشته باشد و کشتی‌ها هنگام ورود به تنگه از آب‌های تحت کنترل ایران عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/139863" target="_blank">📅 19:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLgZypHaugXaEG6xUKi0V2C64kvXDSd5hmsSX8VmYk_211YF8U-g7arpzAEiFBUp6tVqTvTZs9WculUxOgsqXaSHI6RXdapW5-mZMKhJU2WEOmTZN9y0ERYkduyLz25SR5qP4QiH6Bm0f55fY8rFMcw4rVk6CWsYAhldcCq9A2LeG8F1m-MtElpF55YQBV0lvTJ2KpVmKSdCQcD8U9O-F0AEQL6eUdDUhpXKetqHMgzGdS721z8UqZp_X__zJfnzUj9LTwXg9lrrQYgEnk3RkewB0pARbZHAvzecFqOaZq5wEvbPnq8fLljyt5N7ByqIXQdlk1ynp5g6LLb-vTfb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشور رو هواست همزمان عباس تو کربلا:
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/139862" target="_blank">📅 18:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ارتش عربی سوریه دستور تجهیز کامل تمام نیروها با مهمات جنگی و افزایش آمادگی رزمی به بالاترین سطح را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/139861" target="_blank">📅 18:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D54dOlYS6hMLlWK-KjYTUCXFGVC_uADCWcVY2GBdoNgFdoXIIeJVaghdJHGwa_aqrPbfJHisjm0WGBDbc6f10L94FJt2dG30xzaScyB23WbQiSGL9saxtdCYOJPlEEiG4NVVokCIlMsve2wGfZpqMPU557v1aQozHd1cSsSSyl829_BuyTRfW88Rt33J0rdG1U8wm1EiPpy7SeB1Ehlyt3Tu_AC1C977mUVl9yAypXiYNSNx75c-sKdozx96PTuh0yzOIho3mG2ZSf-hQaIi9CmhfilPqXIDFzWdT_7nRsQEx1Zo3hf2wQn7W6MUr8Y4DVoMP2SLnfpzJtvaZ3mMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: "توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران در مورد خلع سلاح هسته‌ای و تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/139860" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: افتخار من بود که از سناتور دارلین گراهام نوردونه (خواهر لیندزی گراهام بزرگ و فقید!)، از ایالت فوق‌العاده کارولینای جنوبی، در دفتر بیضی شکل استقبال کنم.
🔴
ما مدت‌هاست که یکدیگر را می‌شناسیم - او فردی فوق‌العاده و یک وطن‌پرست واقعی آمریکایی است. لیندزی یکی از بزرگترین انسان‌ها و سناتورهایی بود که من تا به حال شناخته‌ام، و خواهرش عشق عمیق او به کشورمان و ایالت کارولینای جنوبی را به ارث برده است.
🔴
در جریان دیدارش، از دارلین خواستم، به خاطر کشورمان، در انتخابات مقدماتی ویژه جمهوری‌خواهان در روز سه‌شنبه، ۱۱ اوت ۲۰۲۶ نامزد شود. او پذیرفت، چرا که هیچ‌کس بهتر از او برای گرامیداشت میراث برادر عزیزش، لیندزی، وجود ندارد.
🔴
دارلین، که از خانواده‌ای کاملاً فوق‌العاده می‌آید، در تمام زندگی‌اش یک برنده بوده است، و از حمایت کامل و تمام من در انتخابات ویژه سنای آمریکا در کارولینای جنوبی برخوردار است - او هرگز شما را ناامید نخواهد کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/139859" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139858">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
بسنت: همین حالا تعداد زیادی کشتی درحال عبور از تنگه هرمز هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/139858" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139857">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqTCrNhvkd9-exFaUdrHT_svDpS-HiJUfFx9NMFA_ccPZYqGnzU1jytnN1FLFni_9tvyf_dNdwHgbhONl8_jrnUA8pyBAYfObKVdmpn-36PqXDq8Uj-3oVxKB4OUsidaQwvdkGuQ5BHgZ6CPO0pUf8ybHGY5gjLoD5864oEj__KoTfwd5mYy3mzkihhZzi6GQEC1AgJaqZ3UScogzZicdYqMvIqtsHePUS4wD0msTCRFBTf7JW-dx-j7KMFBK9sXxKEvgLQ003sNBsfpcgeuXumNJE8ZqmF4u9UTxG5EbtwN6WQG2nFVTAGFvuTHVep37OunH0BA-B9LyXTzq4cmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووری
/
بهرام یوسفی فعال اقتصادی نزدیک به دولت مدعی شد توافق ایران و عمان برای  بازگشایی  تنگه هرمز حاصل شده و احتمالا ساعات آتی خبر بازگشایی تنگه هرمز از سمت مقامات  ای عمانی اعلام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/139857" target="_blank">📅 18:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139856">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: فرماندهی ارتش طی ۴۸ ساعت گذشته سیاست حمله به غزه را به شدت تشدید کرده و اکنون هر عملیات هدف‌گیری نیازمند تأیید شخص رئیس ستاد، زمیر، است.
🔴
سخنگوی ارتش اسرائیل هنوز در این باره اظهارنظری نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/139856" target="_blank">📅 18:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KMjspa2OZkILfe0dqIKCmT9JTL6Zh0M4fss9qTtAEALa-qj6XIQYzMV3KWnB0Uv8RSuirGZfcbRMby2Tj5Y5RVIWRS7Z-0ankvB_QEtz1hTZ72lH0PDMMbP50xNZQlvMIopPKWvZf2hww4oX9f0WLVLXvFHNl5ejH9AYvNaw8oJ5jknbOeDezzhYMiUQ_fzoefoXUZuysA112Kl74LqZEufv1D-KY43QxaFqK3qt9-qUSqFzsF6ALQAoOUF0gb2zJIk7hJr_3UJ42f0JqgpilgE3sFD0DcpnSlJQDfnnfM6YwXQE7l2uS8RtIefCKsYh-CUYKsDUMOXRJ7JcyDMbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K1vNuK547ohzTmXJWRNK2wzFi_yNHHZrPheZcSShxKjlOjYmdSiPKOEWr98zNpWhO8dZRkQp8A1WzstR9eBE0SREtumhG5UtWizrr7ewb-kTkLnuVAAURvGOY8RmyUauCVx52Xpmly_4jIAK52HxWKJQn4i_HRVndtxbzZSXx7exogBDVfUHuvArasFWLrSDpKl5ewKo9h6upZpZCdzJ0sxXdB14fJYHtifgrZZUNLgvHuOmmWeoik1xohxeCANzcILaebqroZZXmt_CZ74gszTk0ejiuCjR6LlGzgrPORy1CvXGA1_U3QQVURFT4YcheNP5eDjiUWIZJOc6OWq4dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b73abb732.mp4?token=UjZoQ68veQwhzPSdRTPb7EtA1R2ieh7Kyvlc6ZZhTCPj677OcAaMg_i1H4o3shr9kwYUg0TXm-mS-T5Ng2Zo31-QGP9VkI8y1j2hKcRbxU-XIj-vfHHfsT1wN02Mpsb4YS_nbRw2xblLtE_7VhIddDOMnO-tKBIQ1REGsSEwai5bC4pD6UHy2XMbpuzfB3gNfuB7UB9eBxZL80IxpbniCXGsOjaHRVCBMDTaXSh65ElYoo4XgnvuOGa6UIJ-rXtC4SAqOgHYQuQrwc5Vma1JivAwWKRWC4tT5ob4g36aHjTbrsSU99PhtnixB4kATGdDsIlgz0jHep3ltA7hU6VsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b73abb732.mp4?token=UjZoQ68veQwhzPSdRTPb7EtA1R2ieh7Kyvlc6ZZhTCPj677OcAaMg_i1H4o3shr9kwYUg0TXm-mS-T5Ng2Zo31-QGP9VkI8y1j2hKcRbxU-XIj-vfHHfsT1wN02Mpsb4YS_nbRw2xblLtE_7VhIddDOMnO-tKBIQ1REGsSEwai5bC4pD6UHy2XMbpuzfB3gNfuB7UB9eBxZL80IxpbniCXGsOjaHRVCBMDTaXSh65ElYoo4XgnvuOGa6UIJ-rXtC4SAqOgHYQuQrwc5Vma1JivAwWKRWC4tT5ob4g36aHjTbrsSU99PhtnixB4kATGdDsIlgz0jHep3ltA7hU6VsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز 13 ام مرداد، تولد جهان پهلوان، جاویدنام مسعود ذات پروره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/139853" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نشریه بلومبرگ گزارش داد عربستان سعودی از طریق میانجی‌های عمانی در حال گفتگو با انصارالله یمن درباره برقراری آتش‌بس و کاهش تنش‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/139852" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptQKZ_82uXNaxHRVTW5L6qw_I9GgrgcAYxvQ5yce9n-uWXWeao8uqlkb7PcZWzPCi3QJQ82ZQG3GIAU7_Q4AZFiGw60F-e5rUIZVC-EGTecy6Hu63YSQui4x1b9b85MvP6EKMuUqr-_4kbL2P_DUvTuWPegrgbpYjGodspmR41esSa5bJtA8TV0S5JP3K1aDHI4pG77iXWXyMLQxgI0XQEISMZOfFZWYsmjrvm2E90hL0-8lPxY4biFxg9Vo8RMaCRi-iwb_BoFOhC6Ida2UsubmIdFuFRrTaTnYa5ueGQUX9L08wcRgSIRgYdf1iYcust3xbLl7EYTkHHsqKcycJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
توییت ضرغامی درباره جنتی
🔴
خودت استعفا بده و به نظام خدمت کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/139851" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
به گزارش فارن پالیسی، گسترش سریع تولیدات صنایع دفاعی در روسیه باعث شده است شمار زیادی از نیروهای کار از بخش‌های غیرنظامی به صنایع نظامی منتقل شوند.
🔴
این روند رقابت برای جذب نیروی کار را در شرایطی که روسیه از پیش نیز با کمبود نیروی انسانی مواجه بود، تشدید کرده و فشار بیشتری بر بخش‌های غیرنظامی اقتصاد وارد آورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/139850" target="_blank">📅 17:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
روبیو : روابط آمریکا و پاراگوئه هر روز قوی‌تر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/139849" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
روبیو : تو مذاکرات برای بازگشایی تنگه پیشرفت‌هایی داشتیم، اما هنوز به توافق نهایی نرسیدیم
🔴
امیدواریم خیلی زود به توافق برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/139848" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
روبیو: اعلام توافق با ایران در مورد تنگه هرمز می‌تواند خیلی زود انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/139847" target="_blank">📅 17:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139846">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
العربیه: بیانیه مشترک عمان و ایران درباره هرمز، طی چند ساعت آینده اعلام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/139846" target="_blank">📅 17:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3aBfOEISWOO4CncoEDWEHEdrDzViXwD1X8ntXMUhr17JipbE3HEBcLfzb6DIlPHZdaIfT4Mtd1QQcUBq6UUST1cPzzkKc-lxfBJdMtHcVYSp4-dleo-k-HqoeRIOiP2zryggxJm2bQad20yXhpfl_xMqPJ-YklmNej9fziaW2fEjXSPvma6i2jtO3EoYSFr-7JrWnDuD_J_fEj9cO3INcefPXmBdcEhwGDzRw9jeC7Yhl3Tpo6FW13kSyJsAZuLM6sPooUMd6PW-MhOgm8x8mPHvBA2iRdDha4dC_7Nalabm7IA4zv4XkGv3wf-P6M5KBzXwoQPqyryKZjHYpaVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFxzx5MKGLaHX468am9pHm6_8Lye_RQJKis90o_sPvYahRnCh0-H7QNsHasZJnN2JJY6I7-XsCBau8lJqJ8dKU5ywj9U-DaSpk8504__cdve1D-vWy5KDRLVIM1KxOy58a7c22x9vPJm42SzkGQy9VY9uZQKyWAH9-nlbChYU3aHGcQ57by1zk9fngW3WZppei50D3oorQ2bLF2GrWZXwTnSpgsoj_3yE8eKm8jsCKjWOGY-YjCgzNdRiaEuUlrI_w3BrhoDnNtaGR3VEjaMZHh40WKVs_Nm-t5WrFDEhyZ48F3hpy4Og2LaNusZrKntIw_JzcIbUfFjHLun8O2mPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هواپیمای آمریکایی امروز از پایگاه هوایی اوسان در کره جنوبی به سمت پایگاه هوایی عیسی در بحرین به پرواز درآمد که احتمالاً به دلیل کمبود موشک‌های پدافند هوایی در بحرین، محموله‌ای از این موشک‌ها را حمل می‌کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/139844" target="_blank">📅 17:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
الجزیره : اعلام توافق برای بازگشایی کامل تنگه، ممکنه تا چند ساعت دیگه یا نهایتاً فردا انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/139843" target="_blank">📅 17:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یک منبع مطلع به العربیه: احتمالاً طی ساعات آینده یا فردا، جزئیات مربوط به بازگشایی کامل تنگه هرمز اعلام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/139842" target="_blank">📅 17:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
شرکت تسلیحاتی «فایر پوینت» اوکراین با بیش از ۱۲ شرکت دفاعی اروپایی برای تأمین رادار، سامانه‌های هدایت و دیگر تجهیزات مورد نیاز پروژه دفاع موشکی «فریا» توافق‌نامه امضا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/139841" target="_blank">📅 17:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_exWetlnRXFBDs7HIPkWQymQsCnYXrPcuWN9idWlPUx94wfN9Xi8uT1AelS-rBUilzzFzONCQP89nq3H1AxfuyKB2WsLPFX-huwXqQcsVTm1XYUW63uRgQbeVSu57ey7PBoF7LtikOmpzmD9t-w_5I9Yslm1PUOd7OmagitrReFGfcSp-5neiE2T0Pe8ET8L5R3oOdN3146et6UaEBwyjPzTBBUy_E33OFCiUCTNDBU8BQRn6fULq7LM07IvOhHtVjuPf2bOA2V8u_uIVWw8IeFH8ug0-HvGnJOC8b5An3RWIhFlMa3m-F0GTZpSf9L6cQ-8bbQ9CC7Qgou374wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایوان: همکاری نظامی با آمریکا فراتر از تصور است!
🔴
مقام‌های تایوانی از گسترش همکاری‌های دفاعی با ایالات متحده خبر داده‌اند؛ همکاری‌هایی که علاوه بر فروش تسلیحات، آموزش‌ها و تبادلات نظامی گسترده‌ای را نیز در بر می‌گیرد و بخش زیادی از آن تاکنون به‌صورت علنی مطرح نشده بود. این موضع‌گیری در عین حال پیامی به چین تلقی می‌شود که نشان می‌دهد روابط نظامی میان واشنگتن و تایپه همچنان در حال تقویت است.
🔴
به نوشته وال‌استریت ژورنال، «ولینگتون کو» وزیر دفاع تایوان تأکید کرده است که سطح همکاری با آمریکا «بسیار نزدیک‌تر از آن چیزی است که تصور می‌کنید». به گفته او، این همکاری‌ها تنها به تأمین تجهیزات نظامی محدود نیست و نیروهای تایوانی از طریق تعامل با ارتش آمریکا، تجربیات عملیاتی و رزمی ارزشمندی نیز کسب می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/139840" target="_blank">📅 16:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUX2S9Y9qnAylkEeVcwTz9KQF5P1GeAVUYNt7dmY9lXsy_4ROCF4qiFaycf73E8wKrfIguNb3E34PsVIDv4clC6LlV7aG5aitxdi5R7W0my6jk00ymihz4bnx8Kji3udyT0kQz1OWD3EPut_kHXo5YzMyaeIbQEqNlMvRPy3zqEfPQQSytHVD3n0kppnzk24l_sdyjlGJg0RL2GvJ2ifUufyjRcIygCbem4GFKbWcld_3bOMm0qNJbvjsI9DFuB630ZVtFLXmgsMFUI0gi6iezZaOuuUplkbtaVfKIn0VDpEad9R5aY4FxEnmh_LYQPWkbi8vBOOyLusITWEQ_7KQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط نفت برنت به ۸۰ دلار پس از مصاحبه تلویزیونی وزیر خزانه‌داری آمریکا و اعلام احتمال دستیابی به توافقی جدید برای بازگشایی تنگه هرمز تا فردا
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/139839" target="_blank">📅 16:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
شش نفتکش غول‌پیکر سعودی، خالی از محموله، مسیر باب‌المندب را تغییر داده و از جنوب اقیانوس هند به سمت آفریقا حرکت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/139837" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رسانه‌های انگلیس: آتش گرفتن قایق حامل ۱۶۰ مهاجر در کانال «مانش»
🔴
رسانه‌های انگلیس امروز (سه‌شنبه) اعلام کردند یک قایق حامل ۱۶۰ مهاجر هنگام تلاش برای عبور از کانال مانش دچار آتش‌سوزی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/139836" target="_blank">📅 16:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ویدئویی از عملیات جنگنده F-22 همراه سوخت‌رسان آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/139835" target="_blank">📅 16:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روزنامه Izvestia: آمریکا داره با سردر‌گم کردن تهران زمینه رو برای یک حمله غافلگیرانه فراهم میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/139834" target="_blank">📅 16:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
امارات متحده عربی ورود همه شناورهای ایرانی، از جمله کشتی‌ها و لنج‌ها، را به بنادر خود ممنوع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/139833" target="_blank">📅 16:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA8wYEzk3EQGA4dM0iXUqhhvd8UC67UulAqD09KAXxJUb3h-2EN1M39rWMHjRLFO5SN2XtfRli-0hz3alHqjGvpgQXcKpgxB03hCu_kyXQKJjU_lST6IPJu3bJ5FW838Yh3Mkozzr_BmoUAZBCm3JqH0PzqG-07qypmDHLBl81uGd1Ib3HyDKUjDKatB1b-_orXs_fc9nVP2Ry6lhGQdZugMq8vEEJpY8hS9UpIi9hOV-dvLa8UhqX_7FRCa2yUP7s8LTE3HhGrZDnYJl6xAzKanvujw2OFm3konuKTFyZTbUWqtNSqVkuyPIMxP_H4FsLtC5qqpXZ-d2reDSPluIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن عباسی:
سال 73 با امکانات متروی تهران، در جزایر و سواحل جنوب تونل زدیم
🔴
زیرِ جزایر و سواحل، تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/139832" target="_blank">📅 16:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EguU5f4xO3oA2CR96wrFjprjK8inu5HWMTHW3vO4w0Tbs13tDqg19geZ-tElnho0S_mD5DqpBuz3jduU1HfEzYYUgTvEI5-lpdXI4D5RgWhX8PSrZE9Ue8AImHQCUWl7q04m9i_oQBuGAvqiGz4NDi90Fkepe_l8VXohEbw2z0jY4UuMrjVpDMnJc6YVGpvYzGpvDw7LBrlpJPfvUj4-K9PZ2mWtXy6fmQu7-ZjX5Kq3Gw_3XWeUm0uj99et80noH62JYLNGHkISksqyBP8nKHn-Q1DXyRwgcDfEBOJBdqn9RN_1Iz5eBFuVJbXgG1kbdgs_EXwKiAvVOE4xG47Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : وقتی با رضا پهلوی حرف میزنی، میفهمی بیشتر از سیاست به فوتبال، غذا و عکاسی علاقه داره
کاملاً مشخصه که او ویژگی‌ های لازم برای رهبری را ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/139831" target="_blank">📅 16:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvnTrOJMFXIEvIX1IeJZXD4l4j0WgmZV36N42RlVAhEl_drd4XNmgJoDCfoEhE_BC_rMZUcbP8dfLfzPS0pcDLMnaxwhRtvH0Do3eKGxujVXVW50lpXBMgzMjT1Xe3hK3yp9p-REi5xMsm4yyUdlxNLCub4hCRUe1RdQLJh-LnOGGz2SjjNjTMt0yANhsCe7loMgynKSzlh5ILWbgMixlYdO-hVGr7M9B0Msf5kdIN15CP1dO3DvNR_x3FNuGTznPiigCDZC1_m1DGoGPQw7CEmgFOF_RAYrYJS_tNRodUhWVluAUmnJ6eGExrX-v4sF5AfLeczoOCZhowhDDUT3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۸ نفر بر اثر انفجار در شهرک شمس آباد مصدوم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/139830" target="_blank">📅 16:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df5d5b7fb.mp4?token=d7J44QaOG2dubPBKteDNEG-k03ZkK9CVkMf47ITIx7PjG9cfHD1AcSRg0kC_1Hn1JDpJgvqHyjcDPKnfinaqwlliHjtTQGY_XY88_NC-c3LpZ3Rg_jW_7uKLmPYP4ADEnRtasYeq3iTV8tzX6WXmALuqxBv7Y_7dmKWWS2dfECEHD3PfSywyPB0gRTZKz6XGMEXcrbC63CP8Ae-XvUw-GUvgmWOQ1rj-dBZ6iOyqnmnd6a_1rQc6BxvYO19DgZsAh91LF5cGbFlhsLqlfzd2XOs8QxBHD6y9svz_mACIcwJIMb5TlLO1ZgiTbWV2ExMecw6Dkydew5JavieDcKLAjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df5d5b7fb.mp4?token=d7J44QaOG2dubPBKteDNEG-k03ZkK9CVkMf47ITIx7PjG9cfHD1AcSRg0kC_1Hn1JDpJgvqHyjcDPKnfinaqwlliHjtTQGY_XY88_NC-c3LpZ3Rg_jW_7uKLmPYP4ADEnRtasYeq3iTV8tzX6WXmALuqxBv7Y_7dmKWWS2dfECEHD3PfSywyPB0gRTZKz6XGMEXcrbC63CP8Ae-XvUw-GUvgmWOQ1rj-dBZ6iOyqnmnd6a_1rQc6BxvYO19DgZsAh91LF5cGbFlhsLqlfzd2XOs8QxBHD6y9svz_mACIcwJIMb5TlLO1ZgiTbWV2ExMecw6Dkydew5JavieDcKLAjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
توریست ایرانی پاشده رفته کوبا و زیبایی های کمونیسم رو به عینه تجربه کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/139828" target="_blank">📅 15:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کاهش نفت و افزایش اونس طلا بعد از مصاحبه وزیر خزانه داری آمریکا
🔴
ریزش 5 درصدی نفت برنت به زیر 80 دلار.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/139827" target="_blank">📅 15:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا، در مصاحبه با شبکه CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/139826" target="_blank">📅 15:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/139825" target="_blank">📅 15:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-C1o7NS2DGod1JnlyMuX2Zl2pTvIIqh0fdcVB5CornlIFSNrrPKofL7v5iHD86XZK44sZ1MVT11qw1YcoPhsPCOIC-CHG1BSC8OPvpCfSWW-WrDE7Zs0sbuZFpJ82HC6F8x3LhXRH9D7WiaL9VigKqOFaZzZ0T2s35fucrmMit7TUJEZ-1H1ZEzUbvRYRywMQk-gP6o4gnQm48e9JaTMNFzXuER3SbX9KImmHraqsHEAHNLHaw63XP5oSGr07px_N-8KcxsTyEbKkvEN2-0wlLF8vEyy2W6kfS5R11D3pfluMuHAe32P3gdudON9x-x49LGekUNNAUwQ3VTCaOhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
العربیه تصویری از کشتی هدف قرار گرفته در تنگه هرمز منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/139824" target="_blank">📅 15:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139823">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmBfulaU83JCCnnhN-QSe36wSxIPSNRLCgOl2xv54oofO9PxGrYHKLzqLt0ItHdhFULgS8XqE7i_NFIFHygkLNoPumZ_AMF36wjX-9ReLy0t62TLClighECslwzqsZitCxmMdpEg3zj10ppygmAaZJwqCorVxXr2uSsOQ34Vy6CEjEAivGyU_ZvsSCBMGR9r7_ISFHmAGTT6626x_VPyiF33YKsbys8U6GrjhY8JfczbzSHNS5zekeLS3LITic0sM19yaQ9BPBHfwXUKssxdSh6SA28JshM8iAhqPjy4aX_ANqG3hjOi1aq6Z6vRE-AdCYvdhx0-FEuzrXwsL7Ej5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: ترامپ تا سه شنبه به جمهوری اسلامی فرصت مذاکره داده و باید تنگه هرمز رو باز بکنن
در صورت باز نشدن تنگه هرمز ایران با حملاتی ویرانگر مواجه خواهد شد
✅
‎
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/139823" target="_blank">📅 15:04 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
