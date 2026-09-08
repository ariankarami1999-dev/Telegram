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
<img src="https://cdn4.telesco.pe/file/PvYZJF6_lG48crPabzVY03ab2gZcegIEUR9H7JAYXvU6XTGpqwfNqRDH785Y0y215X2klCtzRwDYmguNEgXASB4zEd-SFYet2Rx5tiXLOjsZSbu70iAsSlY3KeWT5cAonlDS0gMO-24vNuZBYdofTwzV6Y3G37cpJNQk5KrIntKM2j_mZJJBOty6bFYLOHmkWsqxlkRtbQrbZTMj3-VOdzr8BZ3pn2nJFB41JpZReKDWhB-8-31EbmojADQRoptUVSO1qWoHLQ-Xm8ucJjwqdvMjsoK72dOMLc8l8kKNj-OgGfM6CD9kLYmpNB_agMumdLYTIR7r5WGkYCglSOfaqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 926K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-146315">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دلیل رسمی کم شدن سرعت اینترنت ایران در ساعات اخیر اعلام شد
🔴
اکبری، معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:  کندی اینترنت ناشی از قطعی فیبرنوری در ارمنستان است و تیم‌های فنی در حال پیگیری و رفع این مشکل هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/146315" target="_blank">📅 21:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146314">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9191d8e017.mp4?token=tcEoQjZXkSgwrSUdLhaFKwRMEkgVXPyNmSViItUPIqQ_x_K---U4qBxjm189cwgVbksQJ99bcnlZA4Qw0nmjfQm7K4dSU7fLT691PAiiBmX6y6b-D6PhFasf0t4Y4uQ3Xut7ujhl2RzAacTLfIcolUYTZCxW-FWyHMdYgb68AswATBbOt0mvr2UCtIthmLEgLEqf5rR49VT7cyK09QjeUfmU_dlDH1OuLFGIbSfMC9kDIh1yQT_FA26mUfah4HTvDRd94yip5BcXplJn2RNYBK_JHafE_f5Ez_3XS7yKdNNSTnrOGE7F6cwrhDR2BiIqsO1rzFs62eIRKBDXRpifng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9191d8e017.mp4?token=tcEoQjZXkSgwrSUdLhaFKwRMEkgVXPyNmSViItUPIqQ_x_K---U4qBxjm189cwgVbksQJ99bcnlZA4Qw0nmjfQm7K4dSU7fLT691PAiiBmX6y6b-D6PhFasf0t4Y4uQ3Xut7ujhl2RzAacTLfIcolUYTZCxW-FWyHMdYgb68AswATBbOt0mvr2UCtIthmLEgLEqf5rR49VT7cyK09QjeUfmU_dlDH1OuLFGIbSfMC9kDIh1yQT_FA26mUfah4HTvDRd94yip5BcXplJn2RNYBK_JHafE_f5Ez_3XS7yKdNNSTnrOGE7F6cwrhDR2BiIqsO1rzFs62eIRKBDXRpifng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی طباطبایی معاون دفتر ارتباطات رئیس جمهور: ما هیچ وسیله نداریم جلو آمریکا استفاده کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/146314" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146313">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سخنگوی کرملین: از تردد آزادانه کشتی‌های تجاری در تنگه هرمز حمایت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/146313" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146312">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
دولت بریتانیا در چارچوب بسته جدید تحریم‌ها علیه ایران، فرود هواپیماهای ایرانی در این کشور را ممنوع کرده است؛ مگر در مواردی که معافیت مشخصی صادر شود.
🔴
این محدودیت بخشی از مجموعه گسترده‌تری از تحریم‌های مالی، تجاری و کشتیرانی علیه ایران است.
🔴
لندن پیش‌تر در سال ۲۰۲۴ توافق خدمات هوایی دوجانبه با ایران را لغو کرده بود؛ اما مقررات جدید، ممنوعیت را به‌صورت گسترده‌تر برای هواپیماهای ایرانی تثبیت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/146312" target="_blank">📅 21:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146311">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPFzcXaqD-77hvAVjFKFpvmcmZiiNavCmm038P61RQMRq5jjF92U2WwtC9-mMOHAOd_h2C5LPvWe0b7EHFIbBxG68Knod76FNQddD2Z5nkEnXsSh8tK0Jy0i0A0-Cuw4Z53ly1RZaqgcI_Q4LKhv0KPQBs85znxu-rgNkYZkYcAf4fe4yt3FJqoxo1KKNVhA8fBUHK-s8NIIMxOcidqmFgVJuVEmij86jgUESbyI23S9X-gfUdrt1Y7x3zopQtOj8EvaoExtyydRkWRfawtL__9EsvWSmi1dC5L8P9fMpMxAfv4HLm2ke_T3wC5G9lxqtjYL-fS5gNO99JyMDzWoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل چند لحظه پیش حملات هوایی را بر نبطیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/146311" target="_blank">📅 21:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146310">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd277</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/146310" target="_blank">📅 21:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146309">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu9z8IGe5OxDzr6TOB8fWrXYQwIZNIp1JaZ78FLj2qZh7DpaHLSE6Cq43K0jHEPSMLDu1A7dDcisAht1eD0Cw5rZhplAPwcQDqOO0rZWIsZzO8rO5w9klxn-AJa0N08XyH7gdLyPZj9H4x6PN2Oz2t1KebQ28Kq9IumohORoHXoqkETEQgWL1TW7fJ6X8vFXo2KZaY1r9zRTQioC7WwRgXGZnyebBN2hETZEVS4b4jZOv5m8LZvlNlujyh3gYW_jUTQ3BPecQrSX8e2ashk56VnxItLVvPkaqUvZUU7qC5qvnMPx-mZ4_D43kGv6Ew8QuM1OSj746Yn-ASEHMoJq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل
:
گزارش‌های رسانه‌ای نادرست است. هیچ هشدار از سوی امارات متحده عربی به نخست‌وزیر قبل از ۷ اکتبر داده نشد.
🔴
اگر اطلاعات مرتبطی وجود داشت، از طریق کانال‌های اطلاعاتی بین دو کشور منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/146309" target="_blank">📅 20:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146308">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI3ye_Ef7MSxN66lGuYD8N-fVsGOtWLXlCAFbvAQRv9-3VHn2-EMfxgevwfpv_WNLp7e9pPzZRofZoe9cLrZoPo9nryWjEO9fU1nfDct6gTvyDfBwNSlpjZIUJrzukvXbWC98XZ_134On5Rq7LyXNm9aUtEYoAiFcgcmvyaTtw3VlXxEs8QBs_wqDmzpg5nPY6GyedttXV79eTOSTw9aSIxdrCdZRMO2CCHI5McIi-R3p7nkLH1OTQpRLZV0UrX5UVlN0oe833XZaLoocm6dFowYjsnAOH1eNsdlS1w3PhoioGHwk1d-Ug__XPtcLnzsdYxQUgh5Q_aDhbRL9rddig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت اپل، فردا از آیفون ۱۸ رونمایی می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/146308" target="_blank">📅 20:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146307">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anGznIZQFr9YtmEbml1iuB-XrIHPSSRzNINfZjCZW4rSfp7pkxJpsHzGlW3aRXIRpfd4miFAUn2wwm0EHLXU3kR9SjtojQAbWD-RmR_rTUrOcJLh_c9KRRzVLnYNqmqHZS7yBdSAksnA8bE2_lbkXe4SvuqbCcoJo9dOS6cZGutVhKGE9k6WBWbEIinBAE_Kd4zkx_eqy9m6FazqHRjoO9rSGbvPfTYF5c0NqYyoBlDPZbTxZ_6rhohkaVD-7C88-63NOAfTtmiNK00g4OwEDhrhUPO-CKOWknnQqBYh5XPLY4Wv4eysMyBRlgwUUlj5kH-HsIe6guivh01xVfJDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارها در نجران، عربستان سعودی قطع شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/146307" target="_blank">📅 20:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146306">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
عربستان سعودی: سامانه هشدار زودهنگام در منطقه جازان فعال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/146306" target="_blank">📅 20:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146305">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0dd43b40.mp4?token=AWs8VLWP2th2ydcBm_PyqU3b96NrjCUsEJWDGDPesWmsOEaeW4wJ7w3N51IOhdrJvsHqzEect2X2GhLoQtbQHMNquZ8_X_BS4EZZfe8OAQ6xZP_rg79sMLgJHmCt6PczqcN55IRtDq2S_EzSbFdX4Fz71V_w7n7dJA2nogVPXnvepO05jS2Pst0RbOKWjJW2GaiMFIura5E619_RxV5kmG7rF-yPsftqxbU5vAtWdbwk8fUs12fX6tDPf73Q98Z6cTRpIxWpGzyRUlbar0Ld_jmz1bwe5edMrsECGcjlRhNm5pEIcFwiz30zx4vM7BXAT6P9QWqxvuLnga99AWCcZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0dd43b40.mp4?token=AWs8VLWP2th2ydcBm_PyqU3b96NrjCUsEJWDGDPesWmsOEaeW4wJ7w3N51IOhdrJvsHqzEect2X2GhLoQtbQHMNquZ8_X_BS4EZZfe8OAQ6xZP_rg79sMLgJHmCt6PczqcN55IRtDq2S_EzSbFdX4Fz71V_w7n7dJA2nogVPXnvepO05jS2Pst0RbOKWjJW2GaiMFIura5E619_RxV5kmG7rF-yPsftqxbU5vAtWdbwk8fUs12fX6tDPf73Q98Z6cTRpIxWpGzyRUlbar0Ld_jmz1bwe5edMrsECGcjlRhNm5pEIcFwiz30zx4vM7BXAT6P9QWqxvuLnga99AWCcZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت درباره مراکز داده:
ما باید داستان واقعی مراکز داده را برای جوامع توضیح دهیم.
🔴
همچنین باید اذعان کنیم که در این زمینه تبلیغات سیاسی زیادی از سوی چین وجود دارد و این اعتراض‌کنندگانی که در مناطق روستایی ظاهر می‌شوند، نتیجه یک خیزش خودجوش و ارگانیک از سوی جامعه نبوده است.
🔴
این اعتراضات بسیار منظم و سازمان‌یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146305" target="_blank">📅 20:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146304">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae902a64.mp4?token=f5CpqnV93PJ5IgEhLZOmi2554BtNOtevrIGqlq1NX3WUzo4n5M0Bt-TgSxJ6bWNQpylCyOrDThj5ypZyPkTb0dHqm_7Yxqt8QCIWrGG5Z7RJtPAuR4zyjzKgMiSx3yNjloaXfXwQy9TJstyg5spOrF9OB6hcdAwmqt4nr7mWekI3ckG1Jv_dzfozGwoSPwoZug1IOAqtV0fxBg3p_KbiZ0JmhBuI47WTCd_gnSi2JKseYc8qeaHWkibmierek8cpRcvRT3KvtHBsIgQsb337mWytc7lIsROjgmPOuylmL8jHhJeZzR_sSAlcMb3ibR1fuN34VxmeZx4x6ApFWBE4qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae902a64.mp4?token=f5CpqnV93PJ5IgEhLZOmi2554BtNOtevrIGqlq1NX3WUzo4n5M0Bt-TgSxJ6bWNQpylCyOrDThj5ypZyPkTb0dHqm_7Yxqt8QCIWrGG5Z7RJtPAuR4zyjzKgMiSx3yNjloaXfXwQy9TJstyg5spOrF9OB6hcdAwmqt4nr7mWekI3ckG1Jv_dzfozGwoSPwoZug1IOAqtV0fxBg3p_KbiZ0JmhBuI47WTCd_gnSi2JKseYc8qeaHWkibmierek8cpRcvRT3KvtHBsIgQsb337mWytc7lIsROjgmPOuylmL8jHhJeZzR_sSAlcMb3ibR1fuN34VxmeZx4x6ApFWBE4qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت می‌گوید اگر چین در رقابت هوش مصنوعی با آمریکا پیروز شود، گنبد آهنین «اهمیتی نخواهد داشت»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146304" target="_blank">📅 20:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146303">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac0931e227.mp4?token=g6vzSKQ-_RZmSV2eqJpnqsoJzpSoZdr0_JCLkGof4OQNkkSntw_SlcOEYqGv82NfKKitYy64oAN9SSrI9kYi1YNjBn0mp1rZRxNr2oJMmjWQLpq40_oOJnKvjT8xQLa9eLH2B7kNK2wEbCa7tqFIH7w51meqCJ41M4aDWN7SgZR-yDPXUHP-O-EWm6hccwsqU1dx_S9pXP9_vwCy8ar_NCJRRe40bYGmVVy4TQ0oSpixtL1coWFXsgLvZ2jGu3A_zZ_oahH5IFeHZmMz1S-TbIXizM9ZI7VZthfj4VkmzcfDYbQAVQl5ParxAKZHjbvWjKzKHgYfgPxFLIB_Q6Whbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac0931e227.mp4?token=g6vzSKQ-_RZmSV2eqJpnqsoJzpSoZdr0_JCLkGof4OQNkkSntw_SlcOEYqGv82NfKKitYy64oAN9SSrI9kYi1YNjBn0mp1rZRxNr2oJMmjWQLpq40_oOJnKvjT8xQLa9eLH2B7kNK2wEbCa7tqFIH7w51meqCJ41M4aDWN7SgZR-yDPXUHP-O-EWm6hccwsqU1dx_S9pXP9_vwCy8ar_NCJRRe40bYGmVVy4TQ0oSpixtL1coWFXsgLvZ2jGu3A_zZ_oahH5IFeHZmMz1S-TbIXizM9ZI7VZthfj4VkmzcfDYbQAVQl5ParxAKZHjbvWjKzKHgYfgPxFLIB_Q6Whbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بِسنت
:
هنگامی که اتحاد جماهیر شوروی فروپاشید، اقتصاد لهستان و اوکراین هم‌اندازه بود. اکنون اقتصاد لهستان سه برابر بزرگ‌تر است.
🔴
اگر اوکراین بتواند اقتصاد خود را به‌درستی مدیریت کند، این می‌تواند بازدارنده بزرگی برای روس‌ها باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146303" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146302">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007c3cad6a.mp4?token=G1PWLC7y_pDUa-IkAvqslpu7R2mhnGMkovE653Do5lGMKlM3kyPGh8Dvju3yLjHpO9nHbaZnsvXkEfjIbZHFnV2Y5dpwmKCN5dRUGwVlvKGTYFXnmeHCPuZ1FotRQelRy1kme4qPwk-z4jKfO7iHerR3db4tGA0_UNI3mNKBe4U_5rnOVfoPFVhl1TieY-ipzJu0qSybFcmA88alSs6sw9-8ZquB6dIHJCIPd4V5XJvg_AL1Gq4b4gg4F1V7ptvcMEYleknwIpbFH0ZHPAcLtMz7yYfgbzmWbgV9sIH7PiNsv2afEl7oBiYym3hY4zvvHdCCzrMaGGKiADK73RCiBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007c3cad6a.mp4?token=G1PWLC7y_pDUa-IkAvqslpu7R2mhnGMkovE653Do5lGMKlM3kyPGh8Dvju3yLjHpO9nHbaZnsvXkEfjIbZHFnV2Y5dpwmKCN5dRUGwVlvKGTYFXnmeHCPuZ1FotRQelRy1kme4qPwk-z4jKfO7iHerR3db4tGA0_UNI3mNKBe4U_5rnOVfoPFVhl1TieY-ipzJu0qSybFcmA88alSs6sw9-8ZquB6dIHJCIPd4V5XJvg_AL1Gq4b4gg4F1V7ptvcMEYleknwIpbFH0ZHPAcLtMz7yYfgbzmWbgV9sIH7PiNsv2afEl7oBiYym3hY4zvvHdCCzrMaGGKiADK73RCiBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بِسنت درباره اوکراین: آنچه روس‌ها در حال انجام دادن برای اوکراین هستند، یکی از بدترین چیزهایی است که در طول عمرم دیده‌ام.
🔴
اما اگر صحبت نکنید، نمی‌توانید جلوی آن را بگیرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146302" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146301">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d29fdee52.mp4?token=GGjmNHmzlrxvXEDecbjBEfkHwwQAYrJ7szVsFAIrgmsXCxAWk9i7JABmHNX2H83enoW9L1Nt5UqFwljSjO-i3l63JKOrTY3G1TF6RkSs--Jiz6A5xGa_HpNvdSw-QwojC9fbDRV1GfjFKckgKix1A_WzJibYl2syGA9FTpDgQCz_N4YAfofP6MQtD0YHh79WhAs_xJpg70UZlSB-YrE4QRFEBDc-qmIrvbI89wh1TKs_xpvbnlAIBCQICQ7xuwk9Tx0REcPhyxy_E-Zh5vE9VmXiedh7TahTbDJKblXcJ6C2iVH_XBQszQ1MxftP854MDdTyYb2GJMzB9Hpgizi6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d29fdee52.mp4?token=GGjmNHmzlrxvXEDecbjBEfkHwwQAYrJ7szVsFAIrgmsXCxAWk9i7JABmHNX2H83enoW9L1Nt5UqFwljSjO-i3l63JKOrTY3G1TF6RkSs--Jiz6A5xGa_HpNvdSw-QwojC9fbDRV1GfjFKckgKix1A_WzJibYl2syGA9FTpDgQCz_N4YAfofP6MQtD0YHh79WhAs_xJpg70UZlSB-YrE4QRFEBDc-qmIrvbI89wh1TKs_xpvbnlAIBCQICQ7xuwk9Tx0REcPhyxy_E-Zh5vE9VmXiedh7TahTbDJKblXcJ6C2iVH_XBQszQ1MxftP854MDdTyYb2GJMzB9Hpgizi6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بِسنت وزیر خزانه‌داری ایالات متحده آمریکا درباره مقامات جمهوری اسلامی:
مارِ ایرانی، یعنی رهبری، هنوز نمی‌دانند که مرده‌اند، اما مرده‌اند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/146301" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146300">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192ff7f923.mp4?token=kWQAk9aLHIQ99ehLohIRqaGBr4U9iyOfiO1qA6SZJvfDsipSD0e9symKhxEiV0U4T62U1QwPwe3wpMhE3W5yA8UcUJ_oYl4GbCietl-UTNPNOiX0Rva5GooPKY-pWNUQHiCYQ0va0ne_q14-aNbcyV2ryHaMG1dpSHNucTaBCNB_DtEGh09liHhaNPQwFOuGhG4w_5nxt-Rr09NRZb7kj3A7nXLwZo6EKtHFQQ9n9F8R5HYmO8gE_pp6vOi-dwoUsMktnaJShO7u6z_FBMJjMgGk4PNURNuuE9boMue_VUZMz6jRPb035piI8yQKokmndTFxfzF3jKlD7JskX_CbOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192ff7f923.mp4?token=kWQAk9aLHIQ99ehLohIRqaGBr4U9iyOfiO1qA6SZJvfDsipSD0e9symKhxEiV0U4T62U1QwPwe3wpMhE3W5yA8UcUJ_oYl4GbCietl-UTNPNOiX0Rva5GooPKY-pWNUQHiCYQ0va0ne_q14-aNbcyV2ryHaMG1dpSHNucTaBCNB_DtEGh09liHhaNPQwFOuGhG4w_5nxt-Rr09NRZb7kj3A7nXLwZo6EKtHFQQ9n9F8R5HYmO8gE_pp6vOi-dwoUsMktnaJShO7u6z_FBMJjMgGk4PNURNuuE9boMue_VUZMz6jRPb035piI8yQKokmndTFxfzF3jKlD7JskX_CbOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده:
ما فکر می‌کردیم مهم است که هیئت روسیه در اجلاس G20 حضور داشته باشد.
🔴
زیرا اگر قرار است صحبت نکنید، چگونه می‌توانید این جنگ وحشتناک را حل کنید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/146300" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146299">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/711062d2d3.mp4?token=ZoIOsWUFaIkfR4-d5oY_Mv3gd5wgK43kEvlNd5j9b3jwS9ae5I7odHZpulrbCmMTpepeY2aCUvZnms9Jlwe2TvoDldmdwUReWBD4971qGfjbY_wdNYrxrDpoSc0P4B2_9yKyuLuOeLtRMSZRPoavN1AWk8GWbtHPJ4Ng8e4C-fCUa1uK2Mz92dx1bb5EK6zzyZAJbhsBfaFsTJX47_PHd60Xoq2qRWn1O-1U2-sWeziBc2GT5TuTb4D9T0i51739Tlh35Ooz13aOiWUbHgWvDa4lODBfe9E29DqU5WhY8Psg_CrDH8_Zfao36mMnF1Rhxgm6-M09dNkQNph0DZ0DNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/711062d2d3.mp4?token=ZoIOsWUFaIkfR4-d5oY_Mv3gd5wgK43kEvlNd5j9b3jwS9ae5I7odHZpulrbCmMTpepeY2aCUvZnms9Jlwe2TvoDldmdwUReWBD4971qGfjbY_wdNYrxrDpoSc0P4B2_9yKyuLuOeLtRMSZRPoavN1AWk8GWbtHPJ4Ng8e4C-fCUa1uK2Mz92dx1bb5EK6zzyZAJbhsBfaFsTJX47_PHd60Xoq2qRWn1O-1U2-sWeziBc2GT5TuTb4D9T0i51739Tlh35Ooz13aOiWUbHgWvDa4lODBfe9E29DqU5WhY8Psg_CrDH8_Zfao36mMnF1Rhxgm6-M09dNkQNph0DZ0DNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد سیلی که تو رشت اومد، مردم دارن با قایق رفت و امد میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/146299" target="_blank">📅 20:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146298">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ece98dfc.mp4?token=NTTKpqLtgdzyII8ZigPdsRyhim6wJLWuOi-mAX1s9cqxrxEVl2sTI0xRQ3dE66YRbl9H7IsxMSBBYxMNt5KmXAOOSVCAovz1Izs1dPUy9bfU51n6tDQi2u8AENT40vX0omXcGvGUeiwpSN4p37UwHCp8wW4gx7fFfUcVxEtVt7MZWkcXnGxP8tGfwIFzDoup6TQ9bNccmYkoXGE_7-g4oa50VE3ReV2GUYQAYRqdZp0VYoGMty0XxKTFKEn_CEo-_46MrEM10DGbXzLHwIa85mstSpxGyjm1NaPff9o9Atf1yR3FSpq28gpgvhYWBZ75udUKkEBGFzjdv0UUtE-PPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ece98dfc.mp4?token=NTTKpqLtgdzyII8ZigPdsRyhim6wJLWuOi-mAX1s9cqxrxEVl2sTI0xRQ3dE66YRbl9H7IsxMSBBYxMNt5KmXAOOSVCAovz1Izs1dPUy9bfU51n6tDQi2u8AENT40vX0omXcGvGUeiwpSN4p37UwHCp8wW4gx7fFfUcVxEtVt7MZWkcXnGxP8tGfwIFzDoup6TQ9bNccmYkoXGE_7-g4oa50VE3ReV2GUYQAYRqdZp0VYoGMty0XxKTFKEn_CEo-_46MrEM10DGbXzLHwIa85mstSpxGyjm1NaPff9o9Atf1yR3FSpq28gpgvhYWBZ75udUKkEBGFzjdv0UUtE-PPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس‌جمهور
:
تفاهم‌نامه‌ای با این قوت و افتخارآمیز در ۲۰۰ سال گذشته نداشتیم/ در هیچ جای تفاهم‌نامه مصالح ایران نقض نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/146298" target="_blank">📅 20:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146297">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
الحدث: ابو علی العیانی، فرمانده واحد واکنش سریع حوثی ها در خط مقدم البره در پی درگیری‌های سنگین در جبهه الوازعیه در استان تعز به همراه چند تن از سربازانش تسلیم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/146297" target="_blank">📅 20:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146296">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پوتین و ترامپ با یکدیگر تلفنی صحبت کردند.
🔴
کاخ کرملین: پوتین و ترامپ در مورد نتایج دیدارهای ویتکاف و کوشنر به مسکو و کی‌یف تبادل نظر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/146296" target="_blank">📅 19:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146295">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWbfyyj_5B_peVlOqkj7LeY0TH1_kZQms7ZnWOr1cLL_YG62I6HpAmqmOPgcNVl_edpxm9jasTHvYUvtPXbmtGdEZf6j2iaAd3Ik3WSBk9tCfbB5vnXvODE6SUdRbJ2jMnz3KugPGvUuyFL540JhmciQ_LHlF6FZxIDo4VlIGIk9TzZz-zuObwAXr7b4R4hZxqf87D_dbRYdz7cPWTtnFA1AHHPIOJ2P3iJuyOnw6ovyTS_5SKgxGAuHsMaLd6swPa9yb7F-L02hxVp1AhUUpCI6-2xhmWNzXQqANFAOFPZ7ZMB5PFGqsQo0HL4cB2ag_nt-wE2p7XbL5Q_d5TT8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت یمن
‼️
🔴
از همه طرف به حوثی‌ها حمله شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146295" target="_blank">📅 19:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146294">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX5xKYu4yy43OeRLz1ATciMYEhlOTC9ZGm0MX08IIq7uJp33jrStkur95z79WE9W5u779VGO4g3B__MsaoqJrbPK4I3UjF8dq4eDEc5o_kFtio-LH3I_o-WCLIQ0uZklJoCnj0Yub-HRxSdf2siTlLrHz36Y3F-UlQlhczrYUqIxx89UoGPlk5NebVIW7Chy29Mnd1OJfl0D38Z2rn_na0ndZ5gnPwfm3NVIMr52iqlrQYakBWMb6x8Tmb6rIBpRt2uWZXmr-LJYp_plGtto_sRWNNLbgWyp_nMSzBkQ6pHs1vv8wyeitgiViP5friss3XaZzP04HhDMwEkvGZp4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان:
دوست داشتم تو المپیا امسال مدال طلا میگرفتم و اونو به رهبرمون تقدیم میکردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146294" target="_blank">📅 19:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146293">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فهرست کامل این ۲۷ شرکت هوایی به شرح زیر است:  • هواپیمایی شیراز (Air Shiraz) • آسا جت (Asa Jet Airline) • هواپیمایی آتا (Ata Airlines) • گروه هوانوردی اطلس (Atlas Aviation Group) • هواپیمایی آوا (Ava Airlines) • هواپیمایی چابهار (Chabahar Airlines) • هواپیمایی…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/146293" target="_blank">📅 19:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146292">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/146292" target="_blank">📅 19:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146291">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
آمریکا ۲۸ شرکت هواپیمایی ایرانی را تحریم کرد؛ دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا سه‌شنبه ۱۷ شهریور، ۲۸ شرکت هواپیمایی ایرانی، ۷ شرکت مرتبط با بخش هوانوردی و یک تبعه مصری ساکن امارات را به فهرست تحریم‌ها اضافه کرد. از جمله شرکت‌های تحریم‌شده…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146291" target="_blank">📅 19:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146290">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آمریکا ۲۸ شرکت هواپیمایی ایرانی را تحریم کرد
؛ دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا سه‌شنبه ۱۷ شهریور،
۲۸ شرکت هواپیمایی ایرانی، ۷ شرکت مرتبط با بخش هوانوردی و یک تبعه مصری ساکن امارات
را به فهرست تحریم‌ها اضافه کرد. از جمله شرکت‌های تحریم‌شده
آتا، چابهار، ایران‌ایرتور، آسمان، کیش، کارون، قشم، سپهران، تابان، زاگرس، وارش و فلای‌پرشیا
هستند. همچنین چند شرکت در
امارات، بریتانیا، ترکیه، مالزی و قزاقستان
به دلیل ارتباط با ماهان‌ایر یا شبکه‌های مرتبط با آن تحریم شدند. آمریکا همچنین
مجوز عمومی G-1 ایران برای صادرات مجدد موقت برخی هواپیماهای غیرنظامی به ایران را تعلیق کرد
و هم‌زمان مجوزهای جدیدی برای پایان دادن به برخی معاملات مرتبط با هوانوردی غیرنظامی صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146290" target="_blank">📅 19:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146289">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8653206654.mp4?token=dSOoyAQSFMGuGgOENu5GhaeffFNk-kL4kyegr8CBnakg_d_sQTRn9pdh6ungjdwAWn12OfToiS9gxZCcQ8xHf5PunBTtA59eFlrc0DqRAx1Wi-BDYY_-pR6IbW2J2L4wR5y9oTZtVjHk_iyPWibWZSgYU8CdqHkPONa1lYKUppIh405ZrmYnFOKAbyc4aIJJd7lUgHYsrNiSJ5NjAZEOta7l1HWYFqJWA3M8Npd4QgEQubzd6u_eO3SSpfyfOOEhievruhcy1v8eFi26QA3DKDL28BCBgJJ1xAk9HcoNDJYfcqyblXmXy4-_9323wFdaT8lBfuwBA_fDzvXgkCIHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8653206654.mp4?token=dSOoyAQSFMGuGgOENu5GhaeffFNk-kL4kyegr8CBnakg_d_sQTRn9pdh6ungjdwAWn12OfToiS9gxZCcQ8xHf5PunBTtA59eFlrc0DqRAx1Wi-BDYY_-pR6IbW2J2L4wR5y9oTZtVjHk_iyPWibWZSgYU8CdqHkPONa1lYKUppIh405ZrmYnFOKAbyc4aIJJd7lUgHYsrNiSJ5NjAZEOta7l1HWYFqJWA3M8Npd4QgEQubzd6u_eO3SSpfyfOOEhievruhcy1v8eFi26QA3DKDL28BCBgJJ1xAk9HcoNDJYfcqyblXmXy4-_9323wFdaT8lBfuwBA_fDzvXgkCIHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افسر آمریکایی از دو روز اختفا در کوهستان های ایران می‌گوید
🔴
افسر نیروی هوایی آمریکا که پس از سرنگونی هواپیمایش بر فراز ایران در فروردین‌ماه دو روز زنده ماند، برای نخستین‌بار در برنامه «۶۰ دقیقه» درباره این حادثه صحبت می‌کند. این مصاحبه یکشنبه منتشر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146289" target="_blank">📅 18:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146288">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ee16bd882.mp4?token=gEIB-vF5P2_QSAAOFotCzYEo42yChExT0OQWjqYMgLfjcFgu53MSlt0r1WlBWSpb-mz_B4bDZCGpRgirWosP5QhFK5De3jSWrTYPAMfmWgfQNMFw2Xq8b5wOAkJnlwfHQdZgEQuzlE4kCFOPvUw5q0Le_YHtZnShURvYiytEt1-eHbC7P__DBerwCIcmAxHan3lFdZvkNo60LCK7JrUV5kRUCcLUV5dz4_jPT6tMk_dMvfhmWGPN8IfW7NVoRNmggXAE91qtcZp5KWgcjnqOST5yzixv9guFGJsgLjxp45qproGwyWSBFEUU46Cf7j2tZw9G9ag2BGKBlDDQ99sh0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ee16bd882.mp4?token=gEIB-vF5P2_QSAAOFotCzYEo42yChExT0OQWjqYMgLfjcFgu53MSlt0r1WlBWSpb-mz_B4bDZCGpRgirWosP5QhFK5De3jSWrTYPAMfmWgfQNMFw2Xq8b5wOAkJnlwfHQdZgEQuzlE4kCFOPvUw5q0Le_YHtZnShURvYiytEt1-eHbC7P__DBerwCIcmAxHan3lFdZvkNo60LCK7JrUV5kRUCcLUV5dz4_jPT6tMk_dMvfhmWGPN8IfW7NVoRNmggXAE91qtcZp5KWgcjnqOST5yzixv9guFGJsgLjxp45qproGwyWSBFEUU46Cf7j2tZw9G9ag2BGKBlDDQ99sh0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز طالبان تو اصفهان علیه بی‌ حجابی تظاهرات رو شروع کردن و خواستار بازگشت گشت ارشاد و اجرای قانون اجباری حفظ حجاب شدن!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146288" target="_blank">📅 18:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146287">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: ایران دیگر هیچ شانسی برای دستیابی به سلاح هسته‌ای ندارد و تحریم‌ها علیه آن مؤثر بوده و نتایجی فراتر از انتظارات به همراه داشته است.
🔴
ما الان داریم می‌جنگیم چون ایران می‌خواست سلاح هسته‌ای داشته باشد و خیلی به دستیابی به آن نزدیک بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146287" target="_blank">📅 18:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم: یک زیردریایی هوشمند و پیشرفته بدون سرنشین آمریکایی رو زدیم و عکساشو بزودی منتشر میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146286" target="_blank">📅 18:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146285">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=uZ1HqkmApS1tP6cjbDWiiVobrmPRskmKo3s331f4GaQFz0UnEvf7LDLVCw5t8F0js_jh1LhRuuOYRcIvPk_IN9Z9V8-b3Jqc7V6TRBae8wPDee5EbknJsqoHHR1SUxNAXFl3JTZc1w3-u08sCTo98abwawm0_PHbNZRxOdLDTjrLs4ySrslNMsaDRNeCDovO2U3Ty4iOfJuDieNFC0n-78l5uyuS_qNk9CUtF2JI3xsJ0vXF5aH0iCy2nUSRRjc9ra1ii75a-lLknm3SCbGw185GJbIl8tVXdY9DCWc4p_3Ml0ByxL8PewkjyiCs5EoACVt3GE0cJ3WY0KpWMp6f9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=uZ1HqkmApS1tP6cjbDWiiVobrmPRskmKo3s331f4GaQFz0UnEvf7LDLVCw5t8F0js_jh1LhRuuOYRcIvPk_IN9Z9V8-b3Jqc7V6TRBae8wPDee5EbknJsqoHHR1SUxNAXFl3JTZc1w3-u08sCTo98abwawm0_PHbNZRxOdLDTjrLs4ySrslNMsaDRNeCDovO2U3Ty4iOfJuDieNFC0n-78l5uyuS_qNk9CUtF2JI3xsJ0vXF5aH0iCy2nUSRRjc9ra1ii75a-lLknm3SCbGw185GJbIl8tVXdY9DCWc4p_3Ml0ByxL8PewkjyiCs5EoACVt3GE0cJ3WY0KpWMp6f9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 230,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146285" target="_blank">📅 18:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146284">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">بی ارزش ترین پول دنیا رو داریم، ولی همونم نداریم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146284" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146283">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774ddeaaa1.mp4?token=KO0JcoZ6raandMQUxFIacxXmAigtyQavys6DFKt07RoP9HGc-OaYOCIGknlalto8UPWwH8mjbG-_nIHFlMvRxoXh34URYLhcnAefFz40HBNFI__MsBJRz11k_04xmIzrfj9nrNDdQWjv1_mbMLZw2lGcTaAmGUF6N1OXZdxs1sXzmpA2TKEqeUiJsvKA7e8hPcTRZhLETyhTzMuGoQbWyRTz0voiZtnEjspXKddH3XvfrX2DtG4DTdrH2AZrwyjEIibdvNhxXQUio6RDbwGVFPm5ADTKYdehAaM8pcl_R94S4sTPpa_K1hPLuEED1wUfyIjhG8pcMnTUo9FcdBX1tJ_EmqI2G1uTogb0cKIQIKthKWjeffFKdufXRpyKV4QNKsvDcWRfLXWK6WWF-OI7R2owkG8a5JADp5SOjq_FlJTncZA8_0yYfIIcUxuGSC0W96z-qdI26w6IkFkV1Trj8mZ-SH2wDpIVHysgYJ78BKyaWe8Jelc7cdiRYqayjgY3RZ-y9OGfZ0BOAkOwWOtf_4DhAEB4RrAWupbPTSJJlv8-Z6QDvAdSYCvCYYaQRXB2qgTMUSZJBt9AJq7fMc1nFfjLq6UcIa3nlYo_1biuqSzXqXwmxPljwIJN29YQakbz-QvBJrSRDrPbdMlWoEWYIAcPhQMMWcSsNpSKm0XImhs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774ddeaaa1.mp4?token=KO0JcoZ6raandMQUxFIacxXmAigtyQavys6DFKt07RoP9HGc-OaYOCIGknlalto8UPWwH8mjbG-_nIHFlMvRxoXh34URYLhcnAefFz40HBNFI__MsBJRz11k_04xmIzrfj9nrNDdQWjv1_mbMLZw2lGcTaAmGUF6N1OXZdxs1sXzmpA2TKEqeUiJsvKA7e8hPcTRZhLETyhTzMuGoQbWyRTz0voiZtnEjspXKddH3XvfrX2DtG4DTdrH2AZrwyjEIibdvNhxXQUio6RDbwGVFPm5ADTKYdehAaM8pcl_R94S4sTPpa_K1hPLuEED1wUfyIjhG8pcMnTUo9FcdBX1tJ_EmqI2G1uTogb0cKIQIKthKWjeffFKdufXRpyKV4QNKsvDcWRfLXWK6WWF-OI7R2owkG8a5JADp5SOjq_FlJTncZA8_0yYfIIcUxuGSC0W96z-qdI26w6IkFkV1Trj8mZ-SH2wDpIVHysgYJ78BKyaWe8Jelc7cdiRYqayjgY3RZ-y9OGfZ0BOAkOwWOtf_4DhAEB4RrAWupbPTSJJlv8-Z6QDvAdSYCvCYYaQRXB2qgTMUSZJBt9AJq7fMc1nFfjLq6UcIa3nlYo_1biuqSzXqXwmxPljwIJN29YQakbz-QvBJrSRDrPbdMlWoEWYIAcPhQMMWcSsNpSKm0XImhs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آواره خیابونی: اگر به ناموس حسن روحانی تجاوز شود از همسایه‌ها رفراندوم می‌کند که به متجاوز جواب بدهیم یا نه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146283" target="_blank">📅 17:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146282">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
انفجار در اطراف تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146282" target="_blank">📅 17:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v8-ZTxh2wOncf8nlVmWykceJZoSXmWvqlrMiMtEMp62lFpRe0ue5FZFoLyQbQgaXHVC5xVJU3xuokqeDab3Ii1Htxtvey0RzswanoFsdDODDWxOvlNrUOhHF1F6gILX0_OZSmHKosEb-Pq0fd5wSiJ_A9TVlJdm3XAhfLHpdu2OBNGDUmCwCGBYzwSZ9RlWclQwPfu3Vr0kp-31LeQMZOaWFkox6CPSyyKnMmdRHADJvpcsfdagF_C1-yS2E_1FsDZw5G9zooAAf0klJMYoDvvmsEJX7g6Mh4esRioMAv8oYxE6hD5kVqViP428Q_bbdZRz1m0kYAhoph4IJjxxdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ed3Mc4oiKQeOe-fx7h2G_Aj_LoPFF_WP7qsJX9ik6lFRbxURcXtIgLR4sxRM8CJqrHlP98CmmZt3n2M0WM4OWonkv3vg0HB-C5aixnbO4gLo9_uJ85CpPphDOqxUa0ocnx-xCmfbu6VCjER9JVfB8FeQw0IHYpwaDeWDSVUeobsNgFcFDI7DAoYJZjo-eoVXadJhUBdU-EOFStTo1bZ71pVuMRvem5k16tZGwqn3hdVPQtNN3B6YjsI6Atj_Ol7L8Ql-Ftu2I1_CPsUgn9QZWO5263ITPlujX-5iT5T-v8XzaOJOpBehSVB7q9Fia_G-lxndE248umLZ3LDkOt-ywA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بندر رجایی قبل و بعد از محاصره دریایی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146280" target="_blank">📅 17:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146278">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=R45Eg36aPRHukpxGYdBgq7gBHxWwbsoRkjnYUDihCOermW-_9GFM5AsEK3c9SePMWwM_zk-6D-GHEutk1OyxejMHLgNK2U0Yf6hwZ3qUNlFqGPmrgph11t0BORqdXtLaBglOQeJx-FzaRS9bXa51CVGOkZsXGVjGYKGDvWUbtPPIzzsXpD-jwzgYcukksyu5sj9WnVG900huRzk-Gmzcxv05zfrp2VcwLTIP8LKD80ecLLzUA9tNS-6QdfwEJ-WJ6m1JfqJ1I_Q6L3j53CWGZ3s6zKCttptHDblCt5DIYBXLQmktMaDZHVI7SmhCWjMp9DyBSSs-Pq_WM_3X04BJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7708c5f418.mp4?token=R45Eg36aPRHukpxGYdBgq7gBHxWwbsoRkjnYUDihCOermW-_9GFM5AsEK3c9SePMWwM_zk-6D-GHEutk1OyxejMHLgNK2U0Yf6hwZ3qUNlFqGPmrgph11t0BORqdXtLaBglOQeJx-FzaRS9bXa51CVGOkZsXGVjGYKGDvWUbtPPIzzsXpD-jwzgYcukksyu5sj9WnVG900huRzk-Gmzcxv05zfrp2VcwLTIP8LKD80ecLLzUA9tNS-6QdfwEJ-WJ6m1JfqJ1I_Q6L3j53CWGZ3s6zKCttptHDblCt5DIYBXLQmktMaDZHVI7SmhCWjMp9DyBSSs-Pq_WM_3X04BJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خسارت سیل به ۷۷۲ واحد مسکونی در مازندران
🔴
مدیریت بحران مازندران: در برخی نقاط مازندران بیش‌از ۲۲۰ میلی‌متر بارندگی ثبت شده است.
🔴
تاکنون ۷۷۲ واحد مسکونی درپی بارش‌های سیل‌آسا خسارت دیده‌اند که بیشترین آسیب در ساری گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146278" target="_blank">📅 17:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146277">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnF0H7K9f1JjFqtx9_ZS3toVSRgSb0zFwv3f-9Qok07zk1HfP0Prt15EtV6HOrlig-FoMv8VT0pNOVz67ss-j0BBRVG5NOo9iICQotrqvoGb0d3IqCPsa6B0ZoYaYHqy9nP9ODuwzu8Pc8yNi7ilfy3dgNSfMtfx--LIkr1KbwgnVuiGmaczVelVHZEhZnBrbcxJ4yO9gwKvGy5JSktQai1VDFwEirK5jjtkRymbiK3CZ-IXIitCwl4junIrws60bscP6GKmfxEZHJiEkp63kXG4ITYfpFKB8SEzPPapAjg5VRJFh6PwVbyh8SQ43ksF75C5VrmfXbV0s-JXIJdj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رومانی به دلیل خطر سقوط اشیاء از فضای هوایی، وضعیت هشدار جدی اعلام کرده است و از ساکنان مناطق تحت تأثیر خواسته است که فوراً به پناهگاه‌های امن پناه ببرند.
🔴
این در حالی است که یک پهپاد روسی وارد فضای هوایی مولداوی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146277" target="_blank">📅 17:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146276">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3G60_akgeqqSgoFDd8A9sz7Z208zhX_2r_JXp-dJxW7qH5pMS3sZM-jJQklr6VCiWdcACyCVNta3vgGJ50EtoLajm3EWDCAFx2VqSOLgzwn2FlpMtgdJGVJqZ8T_FhKMBMWKur43HxRT0jqUVFxzgnr-lGLCn_JmRJgRsdAvlcsT_uyMLdVaKKXSNhyr7Vo9RFsp0xQn5Tkk0fgtFZJh7HP2jjYzdpS0wfa2SlBIcUaagWicUTkkYd0ELklI2endEXOS3ogqMQPp4-mNI9Msm_LvoSp5noTSrdquwp4ku2wIe0d5jiGza3R6MibbVWDlZ4XkHKiGmStj68SYkr_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاربر بریتانیایی: نیروی هوایی بریتانیا اخیراً برای دفاع از اسرائیل در برابر حملات ایران به آسمان رفت؛ خلبانان ما جان خود را به خطر انداختند
🔴
اسرائیلی‌ها چطور از ما تشکر می‌کنند؟ با اعلام اینکه جزایر فالکلند متعلق به آرژانتین هستند. عوضی‌ها!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146276" target="_blank">📅 17:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146275">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بلومبرگ: نخست‌وزیر جدید بریتانیا با استفاده از پایگاه‌های خودش توسط آمریکایی‌ها برای جنگ با جمهوری اسلامی مشکلی نداره و این موضوع رو تأیید کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146275" target="_blank">📅 17:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146274">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کانال 12 اسرائیل: هواپیماهای تانکر سوخت‌رسان آمریکایی شروع به بازگشت به فرودگاه تل‌آویو کرده‌اند، چندین هواپیمای سوخت رسان آمریکایی امروز مجدداً وارد اسرائیل شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146274" target="_blank">📅 17:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146273">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f71160ed.mp4?token=STJMXct3bwktC_ceTPkQ0X4uVhBFWOUqA5itCKcR_7BzN426CwzwoAdEK_izKl7MztI1-89pLDnzGDZLqiBouyZU-UcWqA1erIKN3AjWiEY5SX4-4y2vAixPU9cZnkFFFG9SCAFNmAdj7vRyiJuO4mWyxeT8KPTz8XMuhUFLyO5fdGmI2cG4WhjZpaB1C_h446O3QlxGAZtAlk5OFLHE1efDUtwr4kCOuRi7jXAKw-aNhBEsxiKoyQ9FkSqJaOHkchtistiZeiXyqaBjkit0MkOvdB7K-5oMpclibCTQQDCfuRvvHuC3nykxQK6jiaZ56JtFCORtChLfry6HVyckGxAyRwtoeT64kLQBTj8pbfb1tOaOtuky_10dUgCSwmIS8wXYuCfDu3or0E8Blx3rYFpkN1slH7jhec0dX-IhVI6IDkMETkazZX6crzLG8v_oQwkSsjgk2jv73ZUO___3xLgqWxM0zJoyH1uP3EX0mtQWVIbdUDiHJ6tGmLy_X09il_pfkQ_UxdP51MN-Sj4dYU9CnUsh85iu0wLJw84Wd29LZLixZ41_f04naEnJyQSrpNAQnve86sBfCWpLAG1uQxfR2eyRC0Zq2gvOgIBQ8ziZOLbGAxXxJNB9mjM4b-z6fJSkU0A5S3Yx9KSreGB6mujMF3vW8UfeGeIXn9TTD6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f71160ed.mp4?token=STJMXct3bwktC_ceTPkQ0X4uVhBFWOUqA5itCKcR_7BzN426CwzwoAdEK_izKl7MztI1-89pLDnzGDZLqiBouyZU-UcWqA1erIKN3AjWiEY5SX4-4y2vAixPU9cZnkFFFG9SCAFNmAdj7vRyiJuO4mWyxeT8KPTz8XMuhUFLyO5fdGmI2cG4WhjZpaB1C_h446O3QlxGAZtAlk5OFLHE1efDUtwr4kCOuRi7jXAKw-aNhBEsxiKoyQ9FkSqJaOHkchtistiZeiXyqaBjkit0MkOvdB7K-5oMpclibCTQQDCfuRvvHuC3nykxQK6jiaZ56JtFCORtChLfry6HVyckGxAyRwtoeT64kLQBTj8pbfb1tOaOtuky_10dUgCSwmIS8wXYuCfDu3or0E8Blx3rYFpkN1slH7jhec0dX-IhVI6IDkMETkazZX6crzLG8v_oQwkSsjgk2jv73ZUO___3xLgqWxM0zJoyH1uP3EX0mtQWVIbdUDiHJ6tGmLy_X09il_pfkQ_UxdP51MN-Sj4dYU9CnUsh85iu0wLJw84Wd29LZLixZ41_f04naEnJyQSrpNAQnve86sBfCWpLAG1uQxfR2eyRC0Zq2gvOgIBQ8ziZOLbGAxXxJNB9mjM4b-z6fJSkU0A5S3Yx9KSreGB6mujMF3vW8UfeGeIXn9TTD6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اد میلیبند، وزیر خارجه بریتانیا: من به یهودی بودنم افتخار می‌کنم و در حمایت از کشور اسرائیل ثابت‌قدم هستم.
🔴
هیچ تناقضی بین این موضوع و حمایت من از کشور فلسطین وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146273" target="_blank">📅 17:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146272">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c103c3be2.mp4?token=VBi2DGhOd73SVv2lpOriPZ73Vyk1FYCLwYVQEvE00PpCnddPA3n02rhkUVJtgvmznz1ySuZFlbrynsVkzxnL-__p4wfgp-CXK0j5DN_tRsFKQVp1dm0PUTo3pqvdCv3koTQ1ngqyte3DoYah7-uulqC80D8oggSH7cdyGeYuCBdNiCYJX-sm3n2dq-INTgA8R73c34I3y7O2pvRzUa6f2gdMTr023WRmZdvam1gJRyY1LGVMo3AxSChGx8XhS9VrhpedWdkXRLjfwIouDuEKVME2cbHRnDT5wVHJFANnw3-FO7y1FMIp0vzBfHn6-_NDKb31ujEDZOXXFVgRk8TaIr3Ob5L5pluh2FTGfZ-dJ5ZBjNOjllcNedGYvurWxoBMTuz9241jolaoToy1JNhxvxYudyI9w8dznmMQeJuWDjv0omeefFGWZzfAsqZjj7eqKxiBXcnkWG11JoMuADeeM4h_lrvpTJOpAuOPW-kQ1oVH3H-BrpRWs8O8LnxVo9kpfuEtTfI0RRrQm7Yvjqp2k0R4TOe703ClMjIhFUGrqGvlrdUx5rMSWgOEqttIsZoz8ZaBNA5zKy0uQdADNTDwHzUSBb9kmo1Id3ICEFIgsRN4CJjQQhwwwWHjpqeSwF_PBezcg8VdgPs1bfCqZaieiH08bnVAv60nil_8OM3KZK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c103c3be2.mp4?token=VBi2DGhOd73SVv2lpOriPZ73Vyk1FYCLwYVQEvE00PpCnddPA3n02rhkUVJtgvmznz1ySuZFlbrynsVkzxnL-__p4wfgp-CXK0j5DN_tRsFKQVp1dm0PUTo3pqvdCv3koTQ1ngqyte3DoYah7-uulqC80D8oggSH7cdyGeYuCBdNiCYJX-sm3n2dq-INTgA8R73c34I3y7O2pvRzUa6f2gdMTr023WRmZdvam1gJRyY1LGVMo3AxSChGx8XhS9VrhpedWdkXRLjfwIouDuEKVME2cbHRnDT5wVHJFANnw3-FO7y1FMIp0vzBfHn6-_NDKb31ujEDZOXXFVgRk8TaIr3Ob5L5pluh2FTGfZ-dJ5ZBjNOjllcNedGYvurWxoBMTuz9241jolaoToy1JNhxvxYudyI9w8dznmMQeJuWDjv0omeefFGWZzfAsqZjj7eqKxiBXcnkWG11JoMuADeeM4h_lrvpTJOpAuOPW-kQ1oVH3H-BrpRWs8O8LnxVo9kpfuEtTfI0RRrQm7Yvjqp2k0R4TOe703ClMjIhFUGrqGvlrdUx5rMSWgOEqttIsZoz8ZaBNA5zKy0uQdADNTDwHzUSBb9kmo1Id3ICEFIgsRN4CJjQQhwwwWHjpqeSwF_PBezcg8VdgPs1bfCqZaieiH08bnVAv60nil_8OM3KZK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میلیبند: اختلاف ما با مردم اسرائیل نیست؛ ما با مردم اسرائیل روابطی محکم و پایدار داریم.
🔴
اختلاف ما با عملکرد دولت اسرائیله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146272" target="_blank">📅 17:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146271">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80a6fae71.mp4?token=RjojotJ4ZFKjZR-PSn5zI2HKbtjOBvYmJNCzS8hryv5aLlQFXDaJrC-5Ux9ujAvb90I397fjwflJ9IrzBQiUh_1wQdPI8lCr457mFloRqMnGBbE4qzGe-bCZ4kjmeKYxvhj4I5X3R_OO7u_rqlIVXrklglyJKF8J_s8IaQ1Le9XrBsz5sm04leJX5Td5bY0yy6eWFOlUpRqkx1UdHnQ9gF9d6o7F-rH6Ry-0-2_4lgvsOjLLRIjGkFkOHmYclYxV97YmVrU9dC4lbuyETL9m8cpMQXpIfN4HO4l_t_Tc-wcj8BMNGF0gcfZR_GoTcTuVtRXF3rts5jyO0UD8Nmn294xiPtqsUqAGpyKV6CN0-KwDrwCw90K554a3pGiNd7C86wMzMGTqeMu_yKG5uA-Mysno7-bxDYpx-WzJXEYwBxJTnxoDz8NFWtDnLk4Fjk0zbtRz_8mKVYyvfYEg366qqR-vYK1B6uFGe-mibkG7vIm9mL1sk8zt2aLDmswu7ykdsvw0u2mCs5Nv-wVef29YHLYz5mmwpkDOU0puBXLBiKSJG1ZUrpalWjr5UsR-zwH8bS7ql7gyvlamQPDDzLZk9wcPqTou2qaSnDcVw7yqEC7lNbtKXNgYxMqKJMRfBx1yb13sANohhJM2Wie9dI0xHlVPX29_MeV7wx71ja7nOLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80a6fae71.mp4?token=RjojotJ4ZFKjZR-PSn5zI2HKbtjOBvYmJNCzS8hryv5aLlQFXDaJrC-5Ux9ujAvb90I397fjwflJ9IrzBQiUh_1wQdPI8lCr457mFloRqMnGBbE4qzGe-bCZ4kjmeKYxvhj4I5X3R_OO7u_rqlIVXrklglyJKF8J_s8IaQ1Le9XrBsz5sm04leJX5Td5bY0yy6eWFOlUpRqkx1UdHnQ9gF9d6o7F-rH6Ry-0-2_4lgvsOjLLRIjGkFkOHmYclYxV97YmVrU9dC4lbuyETL9m8cpMQXpIfN4HO4l_t_Tc-wcj8BMNGF0gcfZR_GoTcTuVtRXF3rts5jyO0UD8Nmn294xiPtqsUqAGpyKV6CN0-KwDrwCw90K554a3pGiNd7C86wMzMGTqeMu_yKG5uA-Mysno7-bxDYpx-WzJXEYwBxJTnxoDz8NFWtDnLk4Fjk0zbtRz_8mKVYyvfYEg366qqR-vYK1B6uFGe-mibkG7vIm9mL1sk8zt2aLDmswu7ykdsvw0u2mCs5Nv-wVef29YHLYz5mmwpkDOU0puBXLBiKSJG1ZUrpalWjr5UsR-zwH8bS7ql7gyvlamQPDDzLZk9wcPqTou2qaSnDcVw7yqEC7lNbtKXNgYxMqKJMRfBx1yb13sANohhJM2Wie9dI0xHlVPX29_MeV7wx71ja7nOLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه عربستان سعودی:
حوثی‌ها همواره ترجیح می‌دهند منافع محدود خود را بر منافع مردم یمن و خود یمن مقدم کنند.
🔴
آن‌ها به دنبال توسل به خشونت و زور در یک تلاش ناامیدانه برای دستیابی به اهداف خود و خدمت به منافع شخصی خود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146271" target="_blank">📅 16:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146270">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=cKZsnYSzuYhMLP7CxSv_G-x0m2U5iUbtnC_Mu9n6_dovTH0QJBVpbxvWs2eRQEUFJUtxfZxwOiX91z1etCnKj08UjoV6yEEi73qvdQtPZ_WZz3QLrYRSRPmHyvbvB5NcVkXq4EYX9GbtGT0aCJhicDKwk9CPwR5f4SjFs3ugkdyfn44Y2fcwf5O1tkK4gUpAEWyPCIWhym7Iz_qzeNcNrFX9NMq4VlnFVbrDKfsu8F5RxZw3Gm2HsmAcQv3-SUEwHy2skR-PA9TVl6SdgZUz5Bv0QbDWwxoCIpLfrJYZw18P3-f3g02nZsaTyoUncXl3I4e3eW3bzseIJeUUY9a3QS_opcZJFoCAk2nkwgMo5g5wAulO9eFdoowo8Bg93obxeQmk1E7A12Ki7DZv5SnoFTyH24cyU-Jn_MywTkJ43g_NBcwyqVYnaufKKL66gIc7iy9or2bJbnCxPkcwdgD3HVnpDZuOYeWKZxgd1bgwnEFi4vpRdvTA8sRXcbLuguHRh4g_hfgNkL7V8NezR-aiVaa5FV-k1M4824NBo4Ybaw-s8zIJanDly-xbBThashYBwJjiKbAviODY-7cy4dQbGFCwTmLHdEw05kdyMt6ctmzOf7lc09ERlk-Xo2q2U9lrc300uww0xN2kB6rhxrNekLLoPNRE4PaeV45gnbTcWVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=cKZsnYSzuYhMLP7CxSv_G-x0m2U5iUbtnC_Mu9n6_dovTH0QJBVpbxvWs2eRQEUFJUtxfZxwOiX91z1etCnKj08UjoV6yEEi73qvdQtPZ_WZz3QLrYRSRPmHyvbvB5NcVkXq4EYX9GbtGT0aCJhicDKwk9CPwR5f4SjFs3ugkdyfn44Y2fcwf5O1tkK4gUpAEWyPCIWhym7Iz_qzeNcNrFX9NMq4VlnFVbrDKfsu8F5RxZw3Gm2HsmAcQv3-SUEwHy2skR-PA9TVl6SdgZUz5Bv0QbDWwxoCIpLfrJYZw18P3-f3g02nZsaTyoUncXl3I4e3eW3bzseIJeUUY9a3QS_opcZJFoCAk2nkwgMo5g5wAulO9eFdoowo8Bg93obxeQmk1E7A12Ki7DZv5SnoFTyH24cyU-Jn_MywTkJ43g_NBcwyqVYnaufKKL66gIc7iy9or2bJbnCxPkcwdgD3HVnpDZuOYeWKZxgd1bgwnEFi4vpRdvTA8sRXcbLuguHRh4g_hfgNkL7V8NezR-aiVaa5FV-k1M4824NBo4Ybaw-s8zIJanDly-xbBThashYBwJjiKbAviODY-7cy4dQbGFCwTmLHdEw05kdyMt6ctmzOf7lc09ERlk-Xo2q2U9lrc300uww0xN2kB6rhxrNekLLoPNRE4PaeV45gnbTcWVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / اد میلیبند، وزیر خارجه بریتانیا:
ما در هماهنگی با اتحادیه اروپا و آمریکا، تحریم‌های اقتصادی گسترده‌ای رو علیه ایران دوباره اعمال می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146270" target="_blank">📅 16:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146269">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ایران: آژانس در برابر حملات به تأسیسات هسته‌ای نمی‌تواند بی‌مسئولیت باشد
🔴
هیئت نمایندگی ایران در نشست شورای حکام اعلام کرد امنیت هسته‌ای زمانی معنا دارد که در برابر حملات غیرقانونی به تأسیسات هسته‌ای صلح‌آمیز و تحت بازرسی نیز اقدام مؤثر صورت گیرد.
🔴
در این بیانیه آمده است اگر آژانس توان یا اراده کافی برای رسیدگی به پیامدهای امنیتی چنین حملاتی نداشته باشد، اعتماد کشورهای عضو به عملکرد و اثربخشی آن زیر سؤال می‌رود.
🔴
ایران همچنین نسبت به نقض محرمانگی و افشای اطلاعات حساس هشدار داده و تأکید کرده آژانس در قبال سوءاستفاده از این اطلاعات برای اقدامات خرابکارانه، مسئولیت قانونی روشنی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146269" target="_blank">📅 16:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGRDYFtys1ZH8vSPD9Ah9B_Y1kB6vKLrwn96muJ-diQqY2jmLyCugeJ3l_yoSOhb-_-h9w_TdzrGzMGaqzq06eorDB5kgz0md1mp61YGBQVxcebWKBFZAxTTWEbHL5I_HBUkqFlfe3iCi-n-Lx4ksOjhwPzsKAR7ERqtGNhuhksziWVHdVHK9m9uiakVShIT2uMKa0EwyqH6cu-o-RAlarBwEkMnfVzsAaBwpIG_zRrOEON9MrHFl2Rfphe4UD49MjEqkac3uBmj7XK-6JWV0IV05OoZF-2NiCMRm42OHAPLrgpFsQi40EHcSXOEFWDLFpt8hM6OMzvOry9yg-md5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ug7oxUl6zLWeE35HkS1i1uOD9zX3x8n08KZeXREDl9e4dd-jQH894te1tS_4jHpvKtFSxPFjiotMW1QEvFr_-TQFPVEJAyNVzcReP1SmNsYB90Ys4lDS9-hDmVbwELVnuKEBfoqOmmXkKNuIwHp2z5Zv0h2sk1XpQgkD6OtnbR-FoUVzngfHdkOhTzi18_osVRJNy8GRa3H0kfUI6tLGmXK33QZMFhCgCkURYLoSfvVd0TZD8z6IxnH2dZlh-msURWdUzAVLQ3E2iPiWpGe-GXl_97Lk9HVaxvVToryCtj_mteHLycBmfaX08CJH43YjNAOeZuvnqID5kaNmKo8QiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از آثار حملات یمن به پایگاه هوایی خمیس مشیط عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146267" target="_blank">📅 16:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146266">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تحریم اسرائیل توسط بریتانیا
🔴
وزیر امور خارجه بریتانیا: واردات محصولات از شهرک‌های اسرائیلی را ممنوع خواهیم کرد.
🔴
ما شرکت‌ها و افرادی را که خدمات ساخت و ساز و تأمین مالی ارائه می‌دهند که به گسترش شهرک‌سازی‌ها کمک می‌کند، تحریم خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146266" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146265">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اوه اوه تهران چه رعد برقی زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146265" target="_blank">📅 16:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146264">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxBkbUjiWrgnAONqWnnvDuFK8HkmmG0RbJHJ2AmNWf9QVe3CtcIKNX-AMu0DMppz2pRSKHwQ6MJBe7cHUUoUYOVu4ElAlrvLgUV03iPEbBGO8jJ06peTjZxbEyMOmao6DDGledAo_jZ9kOCMvvKnrUDZZjBN9SD1ecvijwcrkgWhI_BYOnRW2zIuaANfojrmafzZOZQHS86rzQCmlWfU8S11daMuJZetllGxiad9-bS2b7askZ3ZhM2m9-Hm7_HcCHHCpAzqHwejT5e-PFSvSmwS_XYzcY3XqarDjJgnyX_rOq7hFOQJxWc_k_S2mbxczkwIr2qYgpc5IKm87dgGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز
:
تیم کوچکی از پژوهشگران شرکت امنیتی آمریکایی
Calif
با استفاده از مدل‌های هوش مصنوعی، یک
کرم رایانه‌ای
ساخته‌اند که می‌تواند در عرض چند ساعت، صدها میلیون حساب
WeChat
را بدون نیاز به کلیک یا لمس کاربر، در معرض نفوذ قرار دهد.
🔴
این بدافزار که WeWorm نام دارد، نخستین کرم شناخته‌شده
«بدون کلیک» (Zero-Click)
توصیف شده که می‌تواند به‌صورت خودکار در هر دو سیستم‌عامل
iOS و Android
منتشر شود.
🔴
بر اساس این گزارش، WeWorm از سیستم اعتماد مخاطبان در WeChat سوءاستفاده کرده و با برقراری تماس، می‌تواند حساب کاربر را چه تماس پاسخ داده شود و چه بدون پاسخ بماند، به خطر بیندازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146264" target="_blank">📅 16:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146263">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رکنا: دیروز تو کرج یه مرد ۶۴ ساله که تازه داشت رانندگی یاد میگرفت، با خودروی‌ آموزش رانندگی داشت تمرین میکرد که ی پسر ۲۳ ساله که راننده پژو ۲۰۶ بوده بخاطر آروم رانندگی کردنش عصبانی میشه و میپیچه جلوش، پیادش میکنه هلش میده و پیرمرده میخوره زمین سرش به جدول میخوره و در دم فوت میکنه و به قتل میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146263" target="_blank">📅 16:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146262">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d730932bb.mp4?token=VaH4GTPvrLRujpsluE5wNxacuX15v0RYA3ckiH4trI_LxI-a44AkYIDvIPw7CnTt2HpFH8anN7s8DG2Yx3pDg6yxkh06IGuQNHHbGE1ZbDt0fIiKnZ8RPNFYkKxeR8Ckd3cK0may0iF0-lFCGUGr5nQHA8e2VNrFxmxEUH2ngmicpokJ8d4NX98Tl3PQQJBf3Hl2N6MmvHg0zJbxVQo4N9rzlzp1PPlYmv9ilK6UT3UavUupam5IV9aRWyIrfkSLeQ4lXVwxyvKaYQbAkcXgVeWbmsVaiLfktSlyDQpQTQ39uMGiVxPNXWpRJ5avj357U4Z2vaqLJmVB7t133HOAxZnT2yTsstBtHwIEenh1dI2Hd4826rXGhJTv2_D3otPXWhDzMhswhkTGFKN-r3ocBLy-r6_l8-ZStbxbUcfOlOcU7DUOOH9FVN4swtGlGdwRSPrZLdYYUzjiXFztdrcMv_5XDgKQNbRpJnT5E3LAPGE3lhKT2gGcv2deQNz1txghMuDfbTGRD3ZAYiY_KqWXduWxz01lR_x8dF4iPLMPGOB5WUtN9QrIOVn3HsV7xnhJxpWUdbb9XNCIjcgBg1U2fyz-s506RRZnEsGmY5hf4M2fEHOJkILajW2THvFh_8iTZGsnSX3yRQanZq_8fXnh4y2L2QIS2pJkvT-ZN4irei8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d730932bb.mp4?token=VaH4GTPvrLRujpsluE5wNxacuX15v0RYA3ckiH4trI_LxI-a44AkYIDvIPw7CnTt2HpFH8anN7s8DG2Yx3pDg6yxkh06IGuQNHHbGE1ZbDt0fIiKnZ8RPNFYkKxeR8Ckd3cK0may0iF0-lFCGUGr5nQHA8e2VNrFxmxEUH2ngmicpokJ8d4NX98Tl3PQQJBf3Hl2N6MmvHg0zJbxVQo4N9rzlzp1PPlYmv9ilK6UT3UavUupam5IV9aRWyIrfkSLeQ4lXVwxyvKaYQbAkcXgVeWbmsVaiLfktSlyDQpQTQ39uMGiVxPNXWpRJ5avj357U4Z2vaqLJmVB7t133HOAxZnT2yTsstBtHwIEenh1dI2Hd4826rXGhJTv2_D3otPXWhDzMhswhkTGFKN-r3ocBLy-r6_l8-ZStbxbUcfOlOcU7DUOOH9FVN4swtGlGdwRSPrZLdYYUzjiXFztdrcMv_5XDgKQNbRpJnT5E3LAPGE3lhKT2gGcv2deQNz1txghMuDfbTGRD3ZAYiY_KqWXduWxz01lR_x8dF4iPLMPGOB5WUtN9QrIOVn3HsV7xnhJxpWUdbb9XNCIjcgBg1U2fyz-s506RRZnEsGmY5hf4M2fEHOJkILajW2THvFh_8iTZGsnSX3yRQanZq_8fXnh4y2L2QIS2pJkvT-ZN4irei8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع میلیونی مخالفان مذاکرات در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146262" target="_blank">📅 16:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146261">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
الحدث:
نیروهای تحت حمایت عربستان سعودی از شمال استان الجوف، یمن در مرز با عربستان پیشروی زمینی را آغاز کردند و به سوی الحزم، پایتخت استان الجوف حرکت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146261" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146260">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/کره جنوبی: به تنگه هرمز نیرو اعزام می‌کنیم
‌
🔴
همچنین یک تیم تحقیقاتی برای ارزیابی وضعیت در تنگه هرمز اعزام خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146260" target="_blank">📅 16:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146259">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سپاه : یک پهپاد MQ-1 بر فراز تنگه هرمز منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146259" target="_blank">📅 16:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146257">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e6929357.mp4?token=D6w9obxwHCziHOKEZv-LEUyDEp9p5cmW4KZ052eCQtnmrPWE1rWg2oBAceuZu4kemZMfhsYCOcPJIElep6F8pWQypTILkxv474A2omE3cFwkKylJQsYF0YCOF1BmvKFDgVVaesNqmKpqzGiROA8eJn-A3emHNj3iVcFSKNhrAikO0Jl-qxAAwclkrrA5U879OF0yZ0Ct96PDrR8t73nWDdGZGb7Iuk9zFJL9B-_fH_86i_UTjPRuF4_stVQF3jjBiCXzokTkL0zlwfZKIGDFoo32vG6gylxgeUZMBOzJrJCik8-Pt6qnIHn1ddBvourW-e0E9HNOSYdJuyQvjxR3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e6929357.mp4?token=D6w9obxwHCziHOKEZv-LEUyDEp9p5cmW4KZ052eCQtnmrPWE1rWg2oBAceuZu4kemZMfhsYCOcPJIElep6F8pWQypTILkxv474A2omE3cFwkKylJQsYF0YCOF1BmvKFDgVVaesNqmKpqzGiROA8eJn-A3emHNj3iVcFSKNhrAikO0Jl-qxAAwclkrrA5U879OF0yZ0Ct96PDrR8t73nWDdGZGb7Iuk9zFJL9B-_fH_86i_UTjPRuF4_stVQF3jjBiCXzokTkL0zlwfZKIGDFoo32vG6gylxgeUZMBOzJrJCik8-Pt6qnIHn1ddBvourW-e0E9HNOSYdJuyQvjxR3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای یمنی در بازار "ایتمه" در منطقه الجوف، پس از پاکسازی آن از نیروهای وفادار به عربستان سعودی، مستقر شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146257" target="_blank">📅 16:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146256">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e7b82147.mp4?token=jS5Op3eZKhWUXsTNmz3VWXXkZ05GeqaRj50wBFdxXbPPiZ28S-C0hOtcS83ro6itPVgJIdScV5ZBk5nSOZ1FvJtS_4HNWD959Ku8xzNfM_lm8HZzOgMRrX7480JKs5eDHY5InukF1FwymWwW8gJb0YVYoPksLGXalaj8eCYUhobJmybIngElXTASfm6F1NtYsc40ieyfJka5jBCBjnDtZ53uzIRAsfwJu5RDS5WMVXxvG7zkgysSFQnhDwgA6PgkI2WN3siFlDLv73Zv7wNjsSZV2o8OCChTZoviIFS1Okd6t_4xBG9LqbTaX42dYpMPx-mh4FYiwRtS7DaInTjpTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e7b82147.mp4?token=jS5Op3eZKhWUXsTNmz3VWXXkZ05GeqaRj50wBFdxXbPPiZ28S-C0hOtcS83ro6itPVgJIdScV5ZBk5nSOZ1FvJtS_4HNWD959Ku8xzNfM_lm8HZzOgMRrX7480JKs5eDHY5InukF1FwymWwW8gJb0YVYoPksLGXalaj8eCYUhobJmybIngElXTASfm6F1NtYsc40ieyfJka5jBCBjnDtZ53uzIRAsfwJu5RDS5WMVXxvG7zkgysSFQnhDwgA6PgkI2WN3siFlDLv73Zv7wNjsSZV2o8OCChTZoviIFS1Okd6t_4xBG9LqbTaX42dYpMPx-mh4FYiwRtS7DaInTjpTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان:ما حملات حوثی‌ها علیه عربستان سعودی را به شدت محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146256" target="_blank">📅 16:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146255">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: نشانه‌ای از اینکه پایان درگیری میان ایران و آمریکا قابل مشاهده باشد، نیست
🔴
کشور‌های حاشیه خلیج فارس نمی‌توانند اختلاف خود با ایران را دائمی تلقی کنند و به هم‌زیستی با این کشور ادامه می‌دهند
🔴
ایران باید بداند در کنار همسایگانی قرار دارد که دشمن نیستند
🔴
تنگه هرمز با وجود ظهور مسیر‌های جایگزین، همچنان برای اقتصاد جهانی حیاتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146255" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f30d079b.mp4?token=SIyKO5izO6aajOHo4U9AImHDuHmGfc3aKX8HM2cuEAY3BEP_pWkJ60Anybcrn_3FSEq2lvgDdZZFccrrGvZ-Xc0BB3eW6GA1Hqgf8pepS0S0XBcUpAGXX9WjePUypGeMd7cl_UAOQ_Zux9ZjpyP0I76eReeUZ8g_0Q0rwnShZExQYIyejyJ17EDuzYOcyVwisw_oyRWQKRfgwI4NVc25exyvADsu95EjeHHmbAlQ43-7Sb3exlMV8c-YntEjm9-xSMB6BzPcgnRkC1GsRBaViG9FThaM61u-TdzwfvOqTTvS37lVV1GCV_bTkFXcDSMaKsEIp5PtqGsz9mPSYadCvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f30d079b.mp4?token=SIyKO5izO6aajOHo4U9AImHDuHmGfc3aKX8HM2cuEAY3BEP_pWkJ60Anybcrn_3FSEq2lvgDdZZFccrrGvZ-Xc0BB3eW6GA1Hqgf8pepS0S0XBcUpAGXX9WjePUypGeMd7cl_UAOQ_Zux9ZjpyP0I76eReeUZ8g_0Q0rwnShZExQYIyejyJ17EDuzYOcyVwisw_oyRWQKRfgwI4NVc25exyvADsu95EjeHHmbAlQ43-7Sb3exlMV8c-YntEjm9-xSMB6BzPcgnRkC1GsRBaViG9FThaM61u-TdzwfvOqTTvS37lVV1GCV_bTkFXcDSMaKsEIp5PtqGsz9mPSYadCvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاکر بوری بلاگر بخاطر این ویدیو که سراسر حقیقت بود اما چون اون‌نماینده مجلس خوشش نیومده بود به ۱۴ماه زندان محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146254" target="_blank">📅 15:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
جا نمونین ازش لینکش
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146253" target="_blank">📅 15:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نماینده‌میناب: مردم باشرف جنوب حاضرن با قایق خودشون برن به جنگ دشمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146252" target="_blank">📅 15:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146249">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLWybyGNUdQNS2x20mCghZ7Fu6qgjFZDauVC2UvuYgTucgtoVFr6nxRHzvKKnc064oXTelddSVphCW1mdQ8dynEpppTddhFDcCkkpZnBnDvG2a9Zpjv0yX8iElPEDPve6y1B0Pe_GvrBDPZsdu2D02_gCTSXr4C4dYousSVBy7yg4ZpdMrTc_w6AvhZEjUm7nd8muYMhvzIi8PkyavMJHtJzZhF_gkQmAtUPFynxTg3MDokDJvbcFOvV4zGy-knBJ9Ix8vF4kOlVEC5CSGU08myQCdzESoSayQMb2rkr1uaBE2w2DffYcZKAlrDySOZT09wKerHIKMvYR3q2jVrkyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419a009651.mp4?token=B22ESzny4uneoTjGFoFpXQVXSEFnsI1WNKybG7Q1guqlnluFXP3wBS2oOqscsphK9Ld1nlKioXgLynmUAdmOiu6xA-97vuOy0BRnDQS7UuVa7BJpkvyznKImhPaIr96dg_jRKHfUoNkV3U_MMy6OtxvcNA4TlwD5bKDY90aN_uHlGRXgtH953Kd_-XJSM0Olte3VB-4_XMOeaOWVe717GEIo2GKrSwBMEQiBJjh4tpRWGw39uTKfb_2RmodbhA2ISMqIPO15Qbr4tGi2vhCElGjKjavPbHYX2pvJ3hjGuWXEeSSeDAKt1-OQjzlJz2z-L3NHndChRKMV2ps8CYdqQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419a009651.mp4?token=B22ESzny4uneoTjGFoFpXQVXSEFnsI1WNKybG7Q1guqlnluFXP3wBS2oOqscsphK9Ld1nlKioXgLynmUAdmOiu6xA-97vuOy0BRnDQS7UuVa7BJpkvyznKImhPaIr96dg_jRKHfUoNkV3U_MMy6OtxvcNA4TlwD5bKDY90aN_uHlGRXgtH953Kd_-XJSM0Olte3VB-4_XMOeaOWVe717GEIo2GKrSwBMEQiBJjh4tpRWGw39uTKfb_2RmodbhA2ISMqIPO15Qbr4tGi2vhCElGjKjavPbHYX2pvJ3hjGuWXEeSSeDAKt1-OQjzlJz2z-L3NHndChRKMV2ps8CYdqQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های وابسته به انصارالله مدعی شده‌اند که نیروهای این گروه بازار
الیتَمه
در محور
الحزم
در استان الجوف در شمال یمن را بازپس گرفته‌اند.
🔴
با این حال، ویدئوهای منتشرشده
و این ادعاها قابل راستی‌آزمایی نیستند و مشخص نیست تصاویر مربوط به زمان اخیر هستند یا قدیمی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146249" target="_blank">📅 15:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146248">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">ارزشی خیلی جالبه!
میگن اینجا دموکراسی حاکمه، بعدش میگن رهبرمون هرچی بگه همونه و اگه کسی حرف از دموکراسی بزنه(اشاره به روحانی) بهش میگن خائن وطن فروش مزدور عامل موساد کافر حربی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146248" target="_blank">📅 15:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146247">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
صداوسیما: هزینه افزایش نرخ بنزین صرف بهبود کیفیت زندگی مردم خواهد شد
🤣
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146247" target="_blank">📅 15:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146246">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqyMBn1_3FjNeTrGFhUUyEINKGZvjScBi16AXBPFpn7zsqRiLTcwIe6rEpBayiYBvYi-UKqrP_YlS5qIaDj1vsTlHdvZr7SRor7hHejkNpugE4FFQCSSW9zyGr38LdMVTbC4bja-HOqNVi1wZE-Su2HkJ8G6DdKjyZ77Do2DOvSRgqmO72dMeANdsTOjXFJRwjV1zuw0btXkxGhhenJwkECRZYnds8DwZatrOYctEgxECOYoBjgrpMd5zj-DQXubHX6dvZXWdSz4eA7ehwdKDNnMPIDXh7VwFfMpFMHUCvdyE9QJ85RiSNgBi-_U0d86xooZ7tzcmM6It9A1I54DYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیکه کاربران فضای مجازی به پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146246" target="_blank">📅 15:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146245">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa2a2a7ee.mp4?token=G3ezOsstSzAoifoYkf1Tg-CLFAtazS7rHxaVx8lXAHp-w3NGQCHWZNFHzJxq4FZ4yHTTsjaKWJ4q6ogTHi_6gpfQEHxqnjQd6A_xEQKK2jqzyxPuyf21dCKbyzO6BKdEBg9uAkrE0mnJUhxIAPPVCqqfMkoC476R-BOCb3zQd9oXGrYQGAYaGTnHQtsK0tiB2SZ4DgdD5cYvMKZDoJzBX09z3oVNoUED48vyx7Zm0dCHN4ohyOGFFYHY_96KE5d_-7jtD0Bt148aSgO5LWgmvRiAp2ngLJB8dnDxQbo5eNbydyGF3rZxacOpo3CEhELuhxcW5axQiX0qiyxgbBbbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa2a2a7ee.mp4?token=G3ezOsstSzAoifoYkf1Tg-CLFAtazS7rHxaVx8lXAHp-w3NGQCHWZNFHzJxq4FZ4yHTTsjaKWJ4q6ogTHi_6gpfQEHxqnjQd6A_xEQKK2jqzyxPuyf21dCKbyzO6BKdEBg9uAkrE0mnJUhxIAPPVCqqfMkoC476R-BOCb3zQd9oXGrYQGAYaGTnHQtsK0tiB2SZ4DgdD5cYvMKZDoJzBX09z3oVNoUED48vyx7Zm0dCHN4ohyOGFFYHY_96KE5d_-7jtD0Bt148aSgO5LWgmvRiAp2ngLJB8dnDxQbo5eNbydyGF3rZxacOpo3CEhELuhxcW5axQiX0qiyxgbBbbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نسل جدید با دستور همراه نمی‌شود؛ باید با او گفت‌وگو کرد
🔴
نمی‌شود صرفاً دستور بدهیم و انتظار داشته باشیم نسل جدید از ما تبعیت کند
🔴
تحول در نظام تربیتی نیازمند نگاه آینده‌نگر و متناسب با اقتضائات نسل جدید است.
🔴
حل مسائل جامعه نیازمند تقویت گفت‌وگو…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146245" target="_blank">📅 15:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146244">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پزشکیان: نسل جدید با دستور همراه نمی‌شود؛ باید با او گفت‌وگو کرد
🔴
نمی‌شود صرفاً دستور بدهیم و انتظار داشته باشیم نسل جدید از ما تبعیت کند
🔴
تحول در نظام تربیتی نیازمند نگاه آینده‌نگر و متناسب با اقتضائات نسل جدید است.
🔴
حل مسائل جامعه نیازمند تقویت گفت‌وگو و فعال‌سازی ظرفیت‌های مردمی در بستر مسجد و محله است.
🔴
آنچه امروز در جامعه مشاهده می‌کنیم، برونداد نظام تربیتی ماست.
🔴
در مقاطعی امکان مداخله تربیتی از دوران کودکی و نوجوانی وجود داشت اما از این ظرفیت به اندازه کافی استفاده نشد.
🔴
اکنون با پیامدهایی مواجهیم که اصلاح آنها به سادگی امکان‌پذیر نیست.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146244" target="_blank">📅 15:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146243">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سی‌ان‌ان: خسارت ایران به پایگاه‌های آمریکا «سنگین و قابل‌توجه» بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146243" target="_blank">📅 15:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146242">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ساعاتی پیش عبدالرووف اسحاقی، فرمانده بسیج پارود تو سیستان بلوچستان ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146242" target="_blank">📅 15:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146241">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2f0be2c9.mp4?token=mTmutf483bC31vujzT13eTvKJ5qwyHFIeEU3IsNdmJElptzuMm2L2ECl634ts5qeTPo7cKSYIfXEDfChkux49fRyDt3FpeSIwwZyrWTA1EMs9Ufuy98KeyLvid8AYnnmXcPMxdi5LS5bz-nOO7zOzGBkarUVuMTThjBpePRrjwBKY594oiQDOA2tiazDceoxXdkuupizlkKZVu_9aQFfw2Efmr2-8kCAyNP6JF51359NJH0Dfq32bAYA3ydVs5ZXPh1SNjQwEQvS7DbBRP7MHk7y4QumZAv4ctZdi2w4OipN0h_Lo6gwVYcDeZLpkK3uUsUU9RDnAnPcB-VFVw_pEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2f0be2c9.mp4?token=mTmutf483bC31vujzT13eTvKJ5qwyHFIeEU3IsNdmJElptzuMm2L2ECl634ts5qeTPo7cKSYIfXEDfChkux49fRyDt3FpeSIwwZyrWTA1EMs9Ufuy98KeyLvid8AYnnmXcPMxdi5LS5bz-nOO7zOzGBkarUVuMTThjBpePRrjwBKY594oiQDOA2tiazDceoxXdkuupizlkKZVu_9aQFfw2Efmr2-8kCAyNP6JF51359NJH0Dfq32bAYA3ydVs5ZXPh1SNjQwEQvS7DbBRP7MHk7y4QumZAv4ctZdi2w4OipN0h_Lo6gwVYcDeZLpkK3uUsUU9RDnAnPcB-VFVw_pEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی مخاطبان از وضعیت ساری
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146241" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146240">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59092702df.mp4?token=mFZZcLtldNHnhsbhSTgi1U1Ycd6AdU6d1Fx4HximoWLDbVykDEWSYWc50LNteernTeYgih1VXOWdPnJSZzwWKRh3dwoceb5pGDKX-NkgjECc1ZlnNrpohlQN2vEymcSulAUcFauiI4f7WsPmPtLY99V0lB5rlybnQDg8Uaq4Lr5uy9sgsnW5IOZCkn6hAQ-OJFN-NxjLJWy4M7pJoe5iKc_tF1oBGDCkn8wSTmhAuq_g3s8iBgH8UAJ8gpFdxjT20JKS9p-XoHyVctKIwGZERRfvFbWIInp1VVBqZiBQ2jQPzw2xMH1AlwhZLJZreKrOBo0ffAOzzb5oVOQHDDMlhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59092702df.mp4?token=mFZZcLtldNHnhsbhSTgi1U1Ycd6AdU6d1Fx4HximoWLDbVykDEWSYWc50LNteernTeYgih1VXOWdPnJSZzwWKRh3dwoceb5pGDKX-NkgjECc1ZlnNrpohlQN2vEymcSulAUcFauiI4f7WsPmPtLY99V0lB5rlybnQDg8Uaq4Lr5uy9sgsnW5IOZCkn6hAQ-OJFN-NxjLJWy4M7pJoe5iKc_tF1oBGDCkn8wSTmhAuq_g3s8iBgH8UAJ8gpFdxjT20JKS9p-XoHyVctKIwGZERRfvFbWIInp1VVBqZiBQ2jQPzw2xMH1AlwhZLJZreKrOBo0ffAOzzb5oVOQHDDMlhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه عربستان سعودی:حوثی‌ها با تحریکات خود، عواقب ناخوشایندی را برای خود به وجود می‌آورند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146240" target="_blank">📅 15:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146239">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
انگلیس یه قانون جدید تصویب کرد که فشار اقتصادی به ایران رو چندین برابر  تشدید کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146239" target="_blank">📅 15:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146238">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سرگئی لاوروف، وزیر امور خارجه روسیه، درباره حملات انصارالله (حوثی‌ها) به عربستان سعودی: «ما معتقدیم که این حملات نتیجه معکوس خواهد داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146238" target="_blank">📅 14:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146237">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146237" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbjv8K-NrSBnztOu299qWG_tLAa7b0OqaaLKJM8Ww7zafiEBWwe0og5nVUqIZSEmM_2ZkZkRcWX6LYm0qeYJUKwPkXOv1-gd8guOw81gN683fs8IytcqLy6AtSlIBFN1IWtwvs56zmruqG7nrExIy-6tn-5sUO46ranlw1qPHbCBxIxo11MPeuw6OhiNfKEwaHPFPe2xtsBCRETYm7XHGBRVGt_fWiHr9FDsipO3bM3aAl0-h6O-CZ7bGsq0XpnFYkCLje9-Og5M40JiUHduPu-w_SWOtat67Rnot5D4ztkNGNnBsTvts3UE1MW_ZbBqQvrvPG6HdzBLGf-6Oiv0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdBavXHMlxAIAxYCOrVRhOaTRCvYiC4rUET8udtHJ3ys7JY8pp7n42NK-VDcHJ8xLIV9QEVty8TKs2Pd6L1ej1nihnCQonst82B1jy9POfWBhkE8q3pG9a3PYnUSK8b134HHgmhyJ3GomEHlTGzuLOxSuA_Z-6-hRx5SfxX9XVzbG_PnKeksCmEbjMOQ_b54TioSwj3dGF1PCZNyCueS7e7jFpSUlkQj1LF_EznegjVDWaYva5NnpG4siCcfIo3SDAThSehvsuPUTbAI-uwkhEuvMC1sf2Z1vffTlt5briL6Bc4s0twwpSwHPMHAs02_BWpsZ-xTCh4bBcHHJAB98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TeXw0dWPXg_1sXMGYzjsfQD85NXlVNR4-8KDVsOYIo7Zd7A0KZpfoH8diMJAODjmBj7a-sCWoyIJ238P0Tcm1xJr0UVGUE6AWZV4YK1STNBLnrEWyU3mvw4oOk01khWrYACseydu_2qIKNC_7XdM5DIFI7N1LY5KXWBQuHiwGRlQbM47cl_L7kiDYRqmGfqYgDxTM1FR2ydb5SiP5fchRtrbKCD8exAjrBX9wLeR548li3RbZbEkFo3_hrnffwZn7w2-cKmGZ_m9QN39vTBgCo6On8lJIYJhTvHtzNB4ZDTUItyrKWEgXNvW2bidB59L3_rESEBVfrm1Exw0WDLwXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41eec3ec50.mp4?token=DowvJT0nJFRtnlb6fmTgahv2GA1XVd-ZaxBUR-Waj9YE1Pha7TIqrinXH4ZAHRpFzFIT2mHSyGDf_gBNjb1dMYpDCfOil2hHy1TXpqoPTcbbWmW-MBzRF-nfkXaVLT1EObqPVzFPsvY0zXbfby-j5DOBzx-MTv1hEwTzb9JX0n2NQ_JX1opqTroVfBKo1sVGgeKrTyltEN7zOE3lS2tb4f4aK70V75jKWemjBL2ASyujiSOK6u2YcJ70nEslJQkuKFKyUCY3efdy1wd22nA8ohoJP5qHZ5wvYewbveIWrMxsppY8CNuAlmTP1-c1hRV8wtdAUuj6cxy8fBhlJKK2Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41eec3ec50.mp4?token=DowvJT0nJFRtnlb6fmTgahv2GA1XVd-ZaxBUR-Waj9YE1Pha7TIqrinXH4ZAHRpFzFIT2mHSyGDf_gBNjb1dMYpDCfOil2hHy1TXpqoPTcbbWmW-MBzRF-nfkXaVLT1EObqPVzFPsvY0zXbfby-j5DOBzx-MTv1hEwTzb9JX0n2NQ_JX1opqTroVfBKo1sVGgeKrTyltEN7zOE3lS2tb4f4aK70V75jKWemjBL2ASyujiSOK6u2YcJ70nEslJQkuKFKyUCY3efdy1wd22nA8ohoJP5qHZ5wvYewbveIWrMxsppY8CNuAlmTP1-c1hRV8wtdAUuj6cxy8fBhlJKK2Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات شدید اسرائیل به مناطقی از غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146233" target="_blank">📅 14:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزرای خارجه چین و قطر درباره آزادی کشتیرانی در هرمز گفت‌وگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146232" target="_blank">📅 14:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
قطعی بیش از ۱۰ ساعته برق و آب در چمستان / نگرانی مردم از خسارت به مواد غذایی و داروها
🔴
پس از بارندگی شدید و سیلاب در مازندران، برق برخی مناطق شمال برای بیش از ۱۰ ساعت قطع شده است.
🔴
بر اساس گزارش‌های دریافتی از منطقه چمستان، ادامه قطعی برق باعث اختلال در تأمین آب نیز شده و نگرانی مردم درباره خراب شدن مواد غذایی و داروهای نیازمند نگهداری در یخچال را افزایش داده است.
🔴
شهروندان خواستار رسیدگی فوری و اعلام زمان دقیق وصل شدن برق و آب هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146231" target="_blank">📅 14:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8ae66168.mp4?token=ZIewSvL1FpQZFoENpmyT1_ht2AvfskqRXJyErtg7d3xVbjGap4k8RqxlIG3v49tibrAq6seb9sMnzfrJz6HtCoTelFZ1FSeh2hdMkO9S4RxjC6-gmTVjo1RCmVVwjkV4IwyQKmqiy-RR4l8-xTxGsYEMSL-9aDGicVk68C4R75WWpDmWhWzWxhG_Og7Ng3fUyir4sU6M9lrg3tay0BnoKDq2gcwsGLCvDZFajOns4mNqvteFxG0iXFaXpIbagn01hT3sjPw6XBWpa_Wr48lreKdNJm4uf0NxWw1gFOeijCogevPyaDyRrYzleGvYVBJflraD5tQiUa-rCi5_3tgbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8ae66168.mp4?token=ZIewSvL1FpQZFoENpmyT1_ht2AvfskqRXJyErtg7d3xVbjGap4k8RqxlIG3v49tibrAq6seb9sMnzfrJz6HtCoTelFZ1FSeh2hdMkO9S4RxjC6-gmTVjo1RCmVVwjkV4IwyQKmqiy-RR4l8-xTxGsYEMSL-9aDGicVk68C4R75WWpDmWhWzWxhG_Og7Ng3fUyir4sU6M9lrg3tay0BnoKDq2gcwsGLCvDZFajOns4mNqvteFxG0iXFaXpIbagn01hT3sjPw6XBWpa_Wr48lreKdNJm4uf0NxWw1gFOeijCogevPyaDyRrYzleGvYVBJflraD5tQiUa-rCi5_3tgbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آبگرفتگی شدید معابر در بابل به علت بارش شدید باران
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146230" target="_blank">📅 14:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMoJVxTWw_shAegGh774u0zJ2lh6hDphAr9eNIFFvzJJyN3rb_SG_5xnM1o9DXN4Q_eXmHOQ0DZ9ce03N4MwBspXQPhkOvtZtttk2dOxPo1tOIa3GNQ8LrPYVdpt2hrB7J1UF3yC6_ZKmerrzilEK02NKJeGpJrU5ugNDHzWAhzxhVDSb03t40NPOc6xMzfvs6HO5PDYbuGGbNgnwkq9e0TFgfrJTMflmXoBoQRzBIiUKH25jgN6lkg_l-68uCPEOa9JGpEYt6AVa78sfW28fMw2-VSp3R1etC9uhdFsV_Dlra7Eazd-0n5bv0fBh2w9Pa6cFgLZrvGAHZUA5sT45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیشروی گسترده نیروهای یمنی از چهار محور به سمت مرکز استان الجوف
🔴
نیروهای مسلح دولت یمن با حمایت و پشتیبانی نیروهای قبایل، عملیات پیشروی خود را از چهار محور در استان الجوف آغاز کرده و هم‌اکنون به شهر «الحَزم»، مرکز این استان در شمال یمن، بسیار نزدیک شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146229" target="_blank">📅 14:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146228">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: باز شدن تنگه هرمز از اهمیت فوق‌العاده‌ای برای همه کشورهای منطقه برخوردار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146228" target="_blank">📅 14:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146227">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رسانه روس: شروط جدید ایران به آمریکا منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146227" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146226">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
قیمت نفت خام برنت در بازارهای بین‌المللی معاملات آتی، تا ساعت ۰۸:۰۰ به وقت گرینویچ، به ۹۹ دلار در هر بشکه رسید؛ افزایشی شدید که پس از حملات حوثی ها به عربستان سعودی رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146226" target="_blank">📅 14:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146225">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی ریاست‌جمهوری روسیه: برای عادی‌سازی روابط ایران و امارات آماده هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146225" target="_blank">📅 13:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146224">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeJcgqWDutX4dacGhy_8Z-fUGukKto1zKNdYm9cYUWdfeSvpH6D9GTdRSdCCuT2E-b3vi95oONwOSzg0D_ueajghIcm3XscoR3Htv_FCvObcARQI_xjjzYWI-QdPLsE0Puogiy9xXqVyb00RjDnwbCO4qlJOZ1REx8wj8iQDy8HQuQ2ke-rkfo8tqd9X7mpedqt5knJ9--bSZv348ZO8Dar665ZOlp_jEnsco8XiM5e7ai39ht0vu8MfnawZocU7y-n-RvYoDEKDggvoDfDqqKDJU7T_j4_uomzy7Xha3LBZP-EaSHRhL9frAdKcUG6AAXEWNMofas75Y_OBrKdijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قوه قضاییه: محمدباقر خرازی در بازداشت به‌سر می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146224" target="_blank">📅 13:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های استان بوشهر: پرواز در مسیر بوشهر به دبی از بیستم شهریور راه‌اندازی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146223" target="_blank">📅 13:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146222">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0pnQ6cKZT1O9PDmWvJwmKybYHIzhGky85dxp_9Pppq5cjyzS3i9wYn8rm2bstFzsvV3ipBpzzKGM67agjo-rQHuTldezycXMU0HK_Z99J7Z9C4i223Vzl-e50K8FApx6syWy24I5ESWed-a7osrebKEpnzQt_DTUrVUmcaZvaImMIbr4Kj4xNxFOB31OvPLFIr3-c_68Eor0GQIHJcFI9QOpPl-KX4cyR09hsFnQGLolhdVLcpNgZrkizv_afVwIMz3wSZNdRLnmJBK0wT000IqkDq32bgWhokEPQph0SXjsh469p6F9Fvz-BAcZVQ_OoeuR9wXhEHQut-mSMIQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت جدید پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146222" target="_blank">📅 13:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146221">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس: خودروهای نوشماره و وارداتی طبق روال قبل سهمیه‌های خود را دارند و برای آنها محدودیتی در نظر گرفته نشده ولی باید هزینه نرخ سوم را بپردازند.
🔴
در مناطق آزاد، نرخ سوم برای خودروهای وارداتی اعمال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146221" target="_blank">📅 13:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146220">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
زلنسکی: «به نظر من، ما همچنین در حال حرکت به سمت مذاکرات سه‌جانبه هستیم.
🔴
نشست سه‌جانبه بعدی می‌تواند در امارات، سوئیس، ترکیه یا کشور دیگری برگزار شود.
🔴
ما در این کشورها تجربه برگزاری مذاکرات را داریم و از سوی چند کشور نیز دعوت‌نامه دریافت کرده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146220" target="_blank">📅 13:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146219">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMKExOXSYGOcNvZx-pcti9-MvPfnjbG_nOTzllrq0VjrNygTZJvWtBVTyT6Q38FSN3AmY7ZIHHT_8qsSiEVTOh1aYgprSoHSyzAxxnl--eZ7LJRa3lBTviNA3Wx5_9iNz6e1_D0gr0Umrfb9pHcczOu3iAb-KkV7AsGDX6Y3d01aCtkFfrvKer1UnD4qAyINr-5aIgS4M_FMz5jsClcGFDoDJmdLEINEn4QAkdSjGf-ATsDOJuQLNNBV2VYujxRzLl35ZJhFUhRlop31zj60-VhI_0ynemmyraPrIvBAmQ4YrGLxDsUbf9PcUH5c5emMENN2IJHStmaZuEP05Jw5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزرای خارجه روسیه و عربستان درباره ایران و تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146219" target="_blank">📅 13:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146218">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee5639fcf.mp4?token=BopV1ozswToXBzgEiu0atUfKgpThSSbfHaP1DWxC3Mx8Z6iY5XLoTnsU_pSUBhZ051mka2vFZSHwi5MfvHbosnPm3jCW9N7-sK3bmnWs5Zs7-Nc7aDoh-n2IDs_XwH3rJcVM005RjFq7ZsClnSRfyu0JVsV7ajurwIRRwozrpGcWf4ioVMpEEiKiDwFhauFgwT1so9F10U59CRSph5A0vv8iDEXpneqAHqp10YZ6LJgrXACuYqRQ4YiN6aYVkVpEaVJ-HFy__0ZCP4656OPJoWLkvghS8uL1IvWduC3ZPMwZiv8w6xu2_nQuHXX5T78vCbOfP3BPR3HdvU7j1l-s1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee5639fcf.mp4?token=BopV1ozswToXBzgEiu0atUfKgpThSSbfHaP1DWxC3Mx8Z6iY5XLoTnsU_pSUBhZ051mka2vFZSHwi5MfvHbosnPm3jCW9N7-sK3bmnWs5Zs7-Nc7aDoh-n2IDs_XwH3rJcVM005RjFq7ZsClnSRfyu0JVsV7ajurwIRRwozrpGcWf4ioVMpEEiKiDwFhauFgwT1so9F10U59CRSph5A0vv8iDEXpneqAHqp10YZ6LJgrXACuYqRQ4YiN6aYVkVpEaVJ-HFy__0ZCP4656OPJoWLkvghS8uL1IvWduC3ZPMwZiv8w6xu2_nQuHXX5T78vCbOfP3BPR3HdvU7j1l-s1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: «ما به بسته‌های موشک‌های بالستیک از آمریکا نیاز داریم.
🔴
آنها به‌طور دقیق شنیدند که به چه چیزهایی و در چه زمانی نیاز داریم
.
🔴
من روی دیدار با دونالد ترامپ در ۲۰ سپتامبر حساب می‌کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/146218" target="_blank">📅 13:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146217">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82015a4d76.mp4?token=V4bxoSUttI4kqxGKUe1uJnBjo4JRP4lyxH6GybqvQA_sjHrBUkJrc9LKnclOdhzjsGysVqBaIiiwM87qWoZs5YhzPx_p-ofBf-HZx5N-4vdOINqbt6PZziS4PakCP2an7-hcR9M8BllONY7xN9fjArmtFeueC7l_PhJ6EJmRDuFvPpgOIpP2_ib-zVuzE1maORyU9jyl33qB_BgBm8iLhUVw4kXMxnrTofnt-t-jEOqbdxmY5cd28c2WI-c6_IboOEPii_Ulw5OomBuCt_opYsnjmo5CTjlr-PCkv-CrmUioq22QyoV6AkUe5GhqM00GreAKmC6k7LAIRKgXmptnzYHyn7usd3Kh6W1TJRMqDpp3EE1KsWfFJcHVOD71am3A2PD753UBZQry55uA77Sy4qTiCBv3_R06d6DKOvujfbP5FPcpB1KszUQH6VJiH_kVGrrSyFhnaok8LIN97uunG5iZ-ZoutOhTOx_2aJLI9SALln6_boimdBBgKsxZtG3kAa_KOLkNXmTi7xJi8gAR_89R7c9KYyGtAmqs05AiPFhN1bsBy_bHKbJvtwu6JBS161k7Epm-TGYc_8fugcQdYSi2tiac_X_Rpzi-M8sJ4-76EsU3C0tJ44gVAYxA1z447OZPyuusuhKRNTNTLM1KPUSuRoyYPJr0fuHRXxb7gdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82015a4d76.mp4?token=V4bxoSUttI4kqxGKUe1uJnBjo4JRP4lyxH6GybqvQA_sjHrBUkJrc9LKnclOdhzjsGysVqBaIiiwM87qWoZs5YhzPx_p-ofBf-HZx5N-4vdOINqbt6PZziS4PakCP2an7-hcR9M8BllONY7xN9fjArmtFeueC7l_PhJ6EJmRDuFvPpgOIpP2_ib-zVuzE1maORyU9jyl33qB_BgBm8iLhUVw4kXMxnrTofnt-t-jEOqbdxmY5cd28c2WI-c6_IboOEPii_Ulw5OomBuCt_opYsnjmo5CTjlr-PCkv-CrmUioq22QyoV6AkUe5GhqM00GreAKmC6k7LAIRKgXmptnzYHyn7usd3Kh6W1TJRMqDpp3EE1KsWfFJcHVOD71am3A2PD753UBZQry55uA77Sy4qTiCBv3_R06d6DKOvujfbP5FPcpB1KszUQH6VJiH_kVGrrSyFhnaok8LIN97uunG5iZ-ZoutOhTOx_2aJLI9SALln6_boimdBBgKsxZtG3kAa_KOLkNXmTi7xJi8gAR_89R7c9KYyGtAmqs05AiPFhN1bsBy_bHKbJvtwu6JBS161k7Epm-TGYc_8fugcQdYSi2tiac_X_Rpzi-M8sJ4-76EsU3C0tJ44gVAYxA1z447OZPyuusuhKRNTNTLM1KPUSuRoyYPJr0fuHRXxb7gdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
«اگر بریتانیا واقعاً به دنبال برخورد با مسائلی است که آنها را نادرست می‌داند، پس تحریم‌ها علیه کره شمالی، چین و روسیه کجاست؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146217" target="_blank">📅 12:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146216">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=q6pZ9JctxLW9ndVivsj0-um6ERGcz-XcKke9lumk8lh-aTz_Oxu51p3I6XiJoXD20FFg9-AD3H9nzlDx3H18Y0DbpxTX5RYmXqj0djBP5xAaGlX0nNa42lbac3uhssVItjHbEgz1fjeyZEKW_bGdYyDBXSOF1vOUCjfSVndiIoAWwK6bUifi8V1YRsTZCZ6zYy3nGTFWEp-BPQHtYO8GocmEEaf3h1qaCyGpVMefVFZy9pWt1NqQ_Sn5EWn9-YCUTKxAom0XAQkG-o9BJAnvUN1-skYWATkbeLXVZAZq94g89mV8S-43zuEMW35nLKBUz8gi_CWrCNq2JnC2oU9BEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=q6pZ9JctxLW9ndVivsj0-um6ERGcz-XcKke9lumk8lh-aTz_Oxu51p3I6XiJoXD20FFg9-AD3H9nzlDx3H18Y0DbpxTX5RYmXqj0djBP5xAaGlX0nNa42lbac3uhssVItjHbEgz1fjeyZEKW_bGdYyDBXSOF1vOUCjfSVndiIoAWwK6bUifi8V1YRsTZCZ6zYy3nGTFWEp-BPQHtYO8GocmEEaf3h1qaCyGpVMefVFZy9pWt1NqQ_Sn5EWn9-YCUTKxAom0XAQkG-o9BJAnvUN1-skYWATkbeLXVZAZq94g89mV8S-43zuEMW35nLKBUz8gi_CWrCNq2JnC2oU9BEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر منتشر شده در رسانه‌‌ها از انفجار در تاسیسات آرامکو در پی حملات حوثی های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146216" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146215">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرگزاری رسمی بحرین: پادشاهی بحرین حملات مجدد حوثی‌ها به غیرنظامیان و تأسیسات حیاتی در عربستان را به شدت محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146215" target="_blank">📅 12:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146214">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نماینده مجلس لرستان: کشور با اعتراضی روبه‌رو نیست و مشکلات معیشتی در حد گرانی‌های جزئی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146214" target="_blank">📅 12:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146213">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
عارف، معاون اول پزشکیان: حتی قیمت سوم بنزین با نرخ ۱۰ هزار تومن هم فاصله زیادی با هزینه واقعی واردات داره؛ هزینه واردات هر لیتر بنزین برای دولت بیش از ۷۰ هزار تومنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146213" target="_blank">📅 12:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146212">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de408d162.mp4?token=X3MzDNDEkiXMeVlEqIcLnfO93hQM_JnKHHhVqrOViinWT38EnyKbVNzCYhCpJ_jtrwycs-KiRYpOGKRIQCuQGw7dcdFCcYZIQW0eYgdlMTrGQ_jCwyBxBNz-VfNZEdhUmh2mvapb7sV8_biFzUNi0W3MaE4Ekf_TuBD1fGysYDnV2L5aNPBYazv2U_dlUsI8oiC9ekRRs-OAgf4ePcvhwmRNCWY3DXXLQxvVIMYbq1NbW28eBNxfuEDkhhJ48GbVShLxexajJP4cNFKjWNNRM1PGO1CfiLE1ucAGtBSbd7nuKR7SvbmSMNCiKB1-AMCwIgFq30ily1n-G2yDzDPMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de408d162.mp4?token=X3MzDNDEkiXMeVlEqIcLnfO93hQM_JnKHHhVqrOViinWT38EnyKbVNzCYhCpJ_jtrwycs-KiRYpOGKRIQCuQGw7dcdFCcYZIQW0eYgdlMTrGQ_jCwyBxBNz-VfNZEdhUmh2mvapb7sV8_biFzUNi0W3MaE4Ekf_TuBD1fGysYDnV2L5aNPBYazv2U_dlUsI8oiC9ekRRs-OAgf4ePcvhwmRNCWY3DXXLQxvVIMYbq1NbW28eBNxfuEDkhhJ48GbVShLxexajJP4cNFKjWNNRM1PGO1CfiLE1ucAGtBSbd7nuKR7SvbmSMNCiKB1-AMCwIgFq30ily1n-G2yDzDPMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجرانی: قیمت بنزین سهمیه‌ای افزایشی نخواهد داشت و فعلاً همان ۱۰ هزار تومان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146212" target="_blank">📅 12:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146211">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پیروزی AfD در آلمان؛ فرانسه نگران تکرار تاریخ در قلب اروپاست
🔴
پیروزی تاریخی راست‌گرایان در انتخابات زاکسن-آنهالت، تنها آلمان را با یک تحول سیاسی کم‌سابقه روبه‌رو نکرده، بلکه در فرانسه نیز زنگ‌های خطر را به صدا درآورده و آن‌ها نگران تکرار تاریخ در قلب اروپا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146211" target="_blank">📅 12:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146210">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نشست فصلی شورای حکام از امروز در حضور نمایندگان ۳۵ کشور، با محوریت ایران برگزار می شود
🔴
آمریکا و سه کشور اروپایی در این نشست چند روزه به دنبال ارائه قطعنامه‌ای برای ارسال پرونده هسته ای ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات منع گسترش سلاح‌های هسته‌ای هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146210" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146209">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
زلنسکی: آمریکا به‌دنبال کاهش تنش روسیه و اوکراین در زمستان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146209" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146208">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqAvkhxbhKBOMcLdjtLT6CBnNRYqG4E7gXcz-MSDgm82cjYgcsKQleXfIm62ja3uq4N_Outfrou29S0ycE3reT_8hZDzMVt_4KdViIZgjqTchbqh1Kgwc2G0OJUOkKkBYWHVY7WjJJ6XJWo_LGJI9mudA5duGCjIRDU457_IsHhsTQA8ACSn03Hct4VKeRJ9JPQuVS66P1mS5AZV6VJ2Z7M11yhvhMcHjoYmvrUcVliuRv9TwNaJ1AxCzB35fELEn-E1JfyFUslTfkzZ7rGQus_XuKzrs3WzBQQL1zXCT-Re3RCXIXofXfT8Z4SbIaI_mvETgWWwRBoOP8p5fSRjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146208" target="_blank">📅 11:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146207">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که ده‌ها موشک بالستیک و پهپاد را در طول شب به تأسیسات شرکت آرامکو در شهرهای ابها، نجران، شهر اقتصادی و نیز شهر جیزان، و همچنین پایگاه هوایی خمیس مشیت در جنوب عربستان سعودی شلیک کرده‌اند.
🔴
حوثی‌ها مدعی شدند که این حملات "آسیب‌های جدی" وارد کرده و هشدار دادند که حملات بیشتر عربستان، "حملات قوی‌تر و گسترده‌تری" را به دنبال خواهد داشت.
🔴
این گروه اعلام کرد که این حملات، انتقام حملات هوایی عربستان به مناطق مأرب، البیضا، الحدیده، تعز و الجوف در سه روز گذشته (121 حمله هوایی) بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146207" target="_blank">📅 11:39 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
