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
<img src="https://cdn4.telesco.pe/file/PH5jacSICzZKzBiPDv2r0mlDQ_Y_904WdWPvpCREQnv073_t-ocS4bMwqbqjvecaYtxToqbU5usJHXP3Le0nythdvwkQUwdFrH5k2UvsRq-mqaDWiDL-CdOq3CWVkJ2kSdqBrJe9NGc_wsky-GA_B3yq-RiSpjYcrOkxZM-AMzg5ZVVgi-ulG_MKjD1RP7veQen3JNrPN-0PN_piGvxa8TzXwA8_ZcbSAr8ZJa0ryjr_P6Jjtt7aXXN76_z5jEwysvnRF4cb56DHh0Dno61WrA4c79PzW21OaYu5vJLFsXCyKg1aPw_G01hpgVV5hzo2ZwmWz6uHaNrpBKNP9hyAxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=iat0vwfu4gqFJv2-gHCyJlWZq7e91NlNJxljrnBNIrreuTw6WYOtc0FU2rBsqb0Qz-_r-6zhlGcRgYom8YdDftqOjA_pgHpjtXOsf0rMApX1vzOMjFc7LlpqgAGR7lhywAA_OgV_nymE4n7uKmgJgR5xz9UCxybzhByNk6-mAgS4hhofVRR70Hn_37PxPBifGTORHcFpU3L2NZJumBJuoIcbS1JqTXLIfUAPogKigUTOFO-9lwwWcJeLH6MIA3AHJUaXin9GeUovGpWQV5jPI--wlthuStbHiJktBmoaQgVdbhmvsOgwbyPRtjm8mWflkLLmYvT66fadFSYtKaEzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=iat0vwfu4gqFJv2-gHCyJlWZq7e91NlNJxljrnBNIrreuTw6WYOtc0FU2rBsqb0Qz-_r-6zhlGcRgYom8YdDftqOjA_pgHpjtXOsf0rMApX1vzOMjFc7LlpqgAGR7lhywAA_OgV_nymE4n7uKmgJgR5xz9UCxybzhByNk6-mAgS4hhofVRR70Hn_37PxPBifGTORHcFpU3L2NZJumBJuoIcbS1JqTXLIfUAPogKigUTOFO-9lwwWcJeLH6MIA3AHJUaXin9GeUovGpWQV5jPI--wlthuStbHiJktBmoaQgVdbhmvsOgwbyPRtjm8mWflkLLmYvT66fadFSYtKaEzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=nd6ShmUtgWq_vZ69tHA6q0wu2hAL5QOYNKJW2redoWs9zuIm7e6DUSc9rM_zTVpFQ9oxHYLLx-CzCtKxTTfadjFrs-SRBKWXSaTURaLLX3mAECENYkvjGbzRCZ1zeEsJ-va03JTSw6xTULrCVT6_MSRNa2_oJY8w6RfA8HAaSGOnlTSRDEv9LRTkZ1VoipNrOtZdQ8XAhbvh18WQ_RcBjjmK0EYP0bYElWLnonZhldmaoERnw47jcmp9xi4TADIP36EVkDvDbMRMlU3L094Djh-kj1JVatkHK5UYPz33lP8363vri5ur6SChRssBS2fo-Tadwbxe7UqRrtnWixmRXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=nd6ShmUtgWq_vZ69tHA6q0wu2hAL5QOYNKJW2redoWs9zuIm7e6DUSc9rM_zTVpFQ9oxHYLLx-CzCtKxTTfadjFrs-SRBKWXSaTURaLLX3mAECENYkvjGbzRCZ1zeEsJ-va03JTSw6xTULrCVT6_MSRNa2_oJY8w6RfA8HAaSGOnlTSRDEv9LRTkZ1VoipNrOtZdQ8XAhbvh18WQ_RcBjjmK0EYP0bYElWLnonZhldmaoERnw47jcmp9xi4TADIP36EVkDvDbMRMlU3L094Djh-kj1JVatkHK5UYPz33lP8363vri5ur6SChRssBS2fo-Tadwbxe7UqRrtnWixmRXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=PxsbEvaFISn2JyUC7juY3d2ir6Ch2mo4-C05wwyUe4owBORotnUyFWgDqKF1sYj-vPIaOz6nMRMt0nxEY_LBrniRZKQRc8J1T4s5_tQ4kLG4xHgdHbPOvJGtPbK0CqaMLA7PPBCNJD8UhyKwqFS6aTOliMTCd9aoJAKXDhvTI_6sq_UfKWMdUp9m1z7bkJOzAfdliRFmGD2Ti61n7Rvw_PkPCOYjlt3YePeq_t7qn9HODF-32_WkAKvUvdgk6-vi6CoWTmsr0HADo7zmU4ji7Ou71F3XxL372p82L81HaKa6HWONEH0r3FZJwKsUOo15thHchDOxph0PTVrO8Pyz4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=PxsbEvaFISn2JyUC7juY3d2ir6Ch2mo4-C05wwyUe4owBORotnUyFWgDqKF1sYj-vPIaOz6nMRMt0nxEY_LBrniRZKQRc8J1T4s5_tQ4kLG4xHgdHbPOvJGtPbK0CqaMLA7PPBCNJD8UhyKwqFS6aTOliMTCd9aoJAKXDhvTI_6sq_UfKWMdUp9m1z7bkJOzAfdliRFmGD2Ti61n7Rvw_PkPCOYjlt3YePeq_t7qn9HODF-32_WkAKvUvdgk6-vi6CoWTmsr0HADo7zmU4ji7Ou71F3XxL372p82L81HaKa6HWONEH0r3FZJwKsUOo15thHchDOxph0PTVrO8Pyz4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=dLu2aQC54dwBeQw0FS1mDV5SnvV3IAByulZO12_dGoQ_wImUPS-JAappoI6BUznmgxGOxjF9LohuSCa2Zk_QaYrxu9_Xu3jXDmkjsvYlx6TvyaPbLhpggr7gL_YJN9oSHwC70b08EXZGPzyf8_pt8p1HgzSDRBkdB6rSoxvtLuPPrO1dSaqhllRDoR_bb8MxWhZqaATrynoKpS2ZyDHMX6q327smBcU7c2atCsI7HiMNsvC6AiMS9hEa2b_ASWwNCcvWJ-iaB4uFcxBr8e6J8l9udu56amkNcakGReUOj1rDWYL5j7F35iA1FGFG_ofbX1vfyYO3Wg9U7-W6W8KPtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=dLu2aQC54dwBeQw0FS1mDV5SnvV3IAByulZO12_dGoQ_wImUPS-JAappoI6BUznmgxGOxjF9LohuSCa2Zk_QaYrxu9_Xu3jXDmkjsvYlx6TvyaPbLhpggr7gL_YJN9oSHwC70b08EXZGPzyf8_pt8p1HgzSDRBkdB6rSoxvtLuPPrO1dSaqhllRDoR_bb8MxWhZqaATrynoKpS2ZyDHMX6q327smBcU7c2atCsI7HiMNsvC6AiMS9hEa2b_ASWwNCcvWJ-iaB4uFcxBr8e6J8l9udu56amkNcakGReUOj1rDWYL5j7F35iA1FGFG_ofbX1vfyYO3Wg9U7-W6W8KPtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=S92OCLHwMxB6R2tnTg8Q49YulMAAVZl8vw2bnBzAOJNXu0mkrl6uA67fW9po1YTrqV51hLh2slszWMv0rNlAZoMxUtM9wKb7SyPWK8Fnv3v7NUABcBj2Ofjrv4Eny_9RvZCDGs_-YoXyAhznVOl2JTUFKPpD1c19IFKax5gCqR8WP1cXW6GIPfu4_g-EqrZBQZOUp6-lvvnO6wxVvecpZ5wyfwsy7aAV5TKEmdcmYsT-OPdOsDHTVVIKgUZI6cDLujRBZnrf8QISDr6b718jP0bVOwloFm7dfvd2FJdPWqCS0PNJ-scE1Uqp2sQtxS53a4u3qO86_br2T-5_sWtjVWDOswl4r6BVIKI-6IZ_BWPZBhUMuk5i9URVftKxoyuNm0ttyYj9XLIpR94jm2zQ-CrKLiLk5FPi-EQ2oLHr5_QH5U-jLyJ9fvJdqW9JFVTyJVcoUWewrO0FAnCbQn6HCxFDgw-HxIZ1K0Spho5AmXCxn3zrryqYpFAhO0YZ_Ab4aPjcrQxA-ctO-YhE9VkrmgPHA4yyndZVrTCUbLS7clJRzCvDfTlQ46gJAfpCUTWU7MgEgMrdevUUPLbwB1zZLXZfjrCO3CEVA2H1MhavYeSzPmc0byRgtUC0TB42nwZnwDfnlkF6BUQbi0w-Sk4C3GZjrv_aySSILahIIRJcj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=S92OCLHwMxB6R2tnTg8Q49YulMAAVZl8vw2bnBzAOJNXu0mkrl6uA67fW9po1YTrqV51hLh2slszWMv0rNlAZoMxUtM9wKb7SyPWK8Fnv3v7NUABcBj2Ofjrv4Eny_9RvZCDGs_-YoXyAhznVOl2JTUFKPpD1c19IFKax5gCqR8WP1cXW6GIPfu4_g-EqrZBQZOUp6-lvvnO6wxVvecpZ5wyfwsy7aAV5TKEmdcmYsT-OPdOsDHTVVIKgUZI6cDLujRBZnrf8QISDr6b718jP0bVOwloFm7dfvd2FJdPWqCS0PNJ-scE1Uqp2sQtxS53a4u3qO86_br2T-5_sWtjVWDOswl4r6BVIKI-6IZ_BWPZBhUMuk5i9URVftKxoyuNm0ttyYj9XLIpR94jm2zQ-CrKLiLk5FPi-EQ2oLHr5_QH5U-jLyJ9fvJdqW9JFVTyJVcoUWewrO0FAnCbQn6HCxFDgw-HxIZ1K0Spho5AmXCxn3zrryqYpFAhO0YZ_Ab4aPjcrQxA-ctO-YhE9VkrmgPHA4yyndZVrTCUbLS7clJRzCvDfTlQ46gJAfpCUTWU7MgEgMrdevUUPLbwB1zZLXZfjrCO3CEVA2H1MhavYeSzPmc0byRgtUC0TB42nwZnwDfnlkF6BUQbi0w-Sk4C3GZjrv_aySSILahIIRJcj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=OxhTy1yM9PlKiDhnzTWom3lWc068kx-p56_CfUlEKmPBtj3HUhoUl2yQAAYT1-716ocisQOMLU3ftaODZL8sNTa1y34h3UWWrNfhS8qKzmEZBUYN8LQ4GddIJYFokrzVz4SLy-Y02mo8s2DGfExKS75BQTpZVFrKLVJsAQGqCvDJtNk6i5IOVF04Gmi4ZWnT6oSzokHb6up12RPOE0HIVf9_S9HlX7-t8h0omPhrmxRObBrXPyHS6Y6cQ_B5XF3tpCBpv8LltC8Kc69V4GobH-Ld8q_P3SEjAIH2W_ut7WD5ZdCTfFLNrlyio7eJVgL1LSFVQLmx0EGxMNoEqR6WcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=OxhTy1yM9PlKiDhnzTWom3lWc068kx-p56_CfUlEKmPBtj3HUhoUl2yQAAYT1-716ocisQOMLU3ftaODZL8sNTa1y34h3UWWrNfhS8qKzmEZBUYN8LQ4GddIJYFokrzVz4SLy-Y02mo8s2DGfExKS75BQTpZVFrKLVJsAQGqCvDJtNk6i5IOVF04Gmi4ZWnT6oSzokHb6up12RPOE0HIVf9_S9HlX7-t8h0omPhrmxRObBrXPyHS6Y6cQ_B5XF3tpCBpv8LltC8Kc69V4GobH-Ld8q_P3SEjAIH2W_ut7WD5ZdCTfFLNrlyio7eJVgL1LSFVQLmx0EGxMNoEqR6WcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuFbG4LEMTV5Ft0VVrnOYLVNOfu_6E2Wyb0lo5V12h5BoMwBA8-hJ7kaytIxAOkhKgn2vWzrt9L2AaZpFNprfz6Z7Tllsy2lBt3EuzlHMcvJ_7v09oCEN0b94WiPNw1xDNSfz-YkKRpaqZhKLIYvYnwq9OvczM_YPsp2JkZ-y9ID3QZiEuHf9gUY0TqDIf3mCVbOnjENjCwb7s3fBsE4H9jdufL5P2i732vPy7Ba7LPtz3TqRbd6TjuVfNbgPJ6cwN1IYCVwISjZXJC1eKCvGpxqAPc0WhpUsskErBVV9gdrQWblC_91NiAEeBVh_mDkZ1LaJaDoFVPdVpUS7Z0LhRB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuFbG4LEMTV5Ft0VVrnOYLVNOfu_6E2Wyb0lo5V12h5BoMwBA8-hJ7kaytIxAOkhKgn2vWzrt9L2AaZpFNprfz6Z7Tllsy2lBt3EuzlHMcvJ_7v09oCEN0b94WiPNw1xDNSfz-YkKRpaqZhKLIYvYnwq9OvczM_YPsp2JkZ-y9ID3QZiEuHf9gUY0TqDIf3mCVbOnjENjCwb7s3fBsE4H9jdufL5P2i732vPy7Ba7LPtz3TqRbd6TjuVfNbgPJ6cwN1IYCVwISjZXJC1eKCvGpxqAPc0WhpUsskErBVV9gdrQWblC_91NiAEeBVh_mDkZ1LaJaDoFVPdVpUS7Z0LhRB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیزر دوم فصل اول سریال هری پاتر که از کریسمس 2027 قراره پخش بشه
@News_Hut</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/news_hut/71099" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71098">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71098" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/news_hut/71098" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71097">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvr6oMgslXUb7XxTkOscCaffFxsqKavV9H9wls7uNKlo-7_e_T13Yiq3sY22CtuhYSFUGr56M8laV3o6c3xemmrKtVQPrV8Yc80wD3s9S-m7o_edBW0w1YEo_g0jW1UK1TNakgj9bPpXaJJGeJZV-dBg8JedPxkx6AhTcUxHcp-8iOxKFKmVbN2I2EYtXUsYTvVTmWMruixCWUzpmzPRAXYe2a_ld6d1gVDEd6aeS8DBjnVCqO8QE5-q1ym2RqI5RYUyaPFh5IzWpHfRSlSqGVL6mhnqBJrW1Ol-ttecKjbNB3W5uKE_HkLAcIJpRaKfdcF0FCwalJ107BL8vdjPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/71097" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71096">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">〰️
سنت‌کام:
بیش از ۲۶۰۰ تفنگدار دریایی و سرباز نیروی دریایی آمریکا، بر روی ناو جنگی USS Boxer (LHD 4) مستقر هستند و این ناو جنگی در حال حاضر در خاورمیانه در حال انجام ماموریت است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71096" target="_blank">📅 17:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=HoY2VmkIu7bG-56WzyeG92oSLVvbPgvoKiw6eziJT6tub2ly-QPG9k7mHrho3DyznwPS7zLfEQSZnoolaM5arn9LGNih7vzD_d49jFc3QHM8Rb8mgrOEbOiLmyMcyaUt0P-8zznu09h4MwCt-wtDoSNA0N21LQH5S6yOq5BrxVhNqelx0d1kmgFq1raE_hwt3BtKKoLqC2Cj0zCxLdaV8qfSQB2aeLJMfa0k6psXzSYG5c9coi1Ah8CaWxmId1Rt76lJkSkKCjpS3lefW4QlbNL3kJlclKP5iSv7XDUQZiGcISGB-jZwPu6BxnIT3SBRkxXrhO0-AZEHvViWJnN7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=HoY2VmkIu7bG-56WzyeG92oSLVvbPgvoKiw6eziJT6tub2ly-QPG9k7mHrho3DyznwPS7zLfEQSZnoolaM5arn9LGNih7vzD_d49jFc3QHM8Rb8mgrOEbOiLmyMcyaUt0P-8zznu09h4MwCt-wtDoSNA0N21LQH5S6yOq5BrxVhNqelx0d1kmgFq1raE_hwt3BtKKoLqC2Cj0zCxLdaV8qfSQB2aeLJMfa0k6psXzSYG5c9coi1Ah8CaWxmId1Rt76lJkSkKCjpS3lefW4QlbNL3kJlclKP5iSv7XDUQZiGcISGB-jZwPu6BxnIT3SBRkxXrhO0-AZEHvViWJnN7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=ZljWjFMjZJgEB1fKBQqhh7qJjfScYvg1j0WJYWj9pDimo2XaWRoH5Hk0rgm9RFX6z7u_cDWGxuPUJYihTIfIC5gU_rmNpQQJUyA6yhAIYy9PxJSeQYrKv_zwl8l6q0bs2pmgHniqp6goDy9zSPb5YB2Mu447wMuCWsETuI1ngC1dzW90KtHryLnJITtG3M-EKRwRx9f-XAQ3DQsjZLXA3uMUEHsUOe80ZRq9TbRwpOuy6c5h0YBA0FT5xzukZr52SD7syV0ItzgLGEkX0ZPabhDsuXI6Us1X0lgXV4zRDFJIuz7jk14LSRkWh0hyJfRSrrrDLBVEAbwu_uJXQUpmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=ZljWjFMjZJgEB1fKBQqhh7qJjfScYvg1j0WJYWj9pDimo2XaWRoH5Hk0rgm9RFX6z7u_cDWGxuPUJYihTIfIC5gU_rmNpQQJUyA6yhAIYy9PxJSeQYrKv_zwl8l6q0bs2pmgHniqp6goDy9zSPb5YB2Mu447wMuCWsETuI1ngC1dzW90KtHryLnJITtG3M-EKRwRx9f-XAQ3DQsjZLXA3uMUEHsUOe80ZRq9TbRwpOuy6c5h0YBA0FT5xzukZr52SD7syV0ItzgLGEkX0ZPabhDsuXI6Us1X0lgXV4zRDFJIuz7jk14LSRkWh0hyJfRSrrrDLBVEAbwu_uJXQUpmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=m3JaoJQg5pj53Jl9vuL-S9_ZuZgnDO6i09BqBP6K5aaOYej5ejNDl3fHhbOkLv2TkEpR--1W4o7F0yEbu1qkGiG1sqYXUZZaOFZQI1VfZFRDQX0rykG1A7ls4UKsABppU7N0R2lU46lYOahtzwo3VxV4ASut-p0yG4_MTKtCtBi8iyHNX4owoa8eVd4q2TMspD5QGlvaAg1odwrbKVRNIpGGZSirovD-UnE6gz4MBE09Y6FVKTrTTwvvapVsPGd2fboHd3C56yeV60BrLMr8z0jXUjEUznbqEuB3AreRn2DQPe8yd2esP7f6bDCtspNuH289s3EmQn4RzN628kgSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=m3JaoJQg5pj53Jl9vuL-S9_ZuZgnDO6i09BqBP6K5aaOYej5ejNDl3fHhbOkLv2TkEpR--1W4o7F0yEbu1qkGiG1sqYXUZZaOFZQI1VfZFRDQX0rykG1A7ls4UKsABppU7N0R2lU46lYOahtzwo3VxV4ASut-p0yG4_MTKtCtBi8iyHNX4owoa8eVd4q2TMspD5QGlvaAg1odwrbKVRNIpGGZSirovD-UnE6gz4MBE09Y6FVKTrTTwvvapVsPGd2fboHd3C56yeV60BrLMr8z0jXUjEUznbqEuB3AreRn2DQPe8yd2esP7f6bDCtspNuH289s3EmQn4RzN628kgSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71092">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=Zto5xFimVJtZRFIH3Jo07xOAktW3e839kBIz_TrKSvYv9uIWC4rTObIEPSiYznpqR8OaIpcLGmO3am3smgmq1gZntfLpPT-RS0VeWeg4O6H4vVaO-ek-MF-VFAK4tlYsZiBgoi2puLC68AHXvfeuWpZ8Oa-lfKKhmiFZraFn1zAaX78rMtRvWwyNjQLC7f4ndTBxgbdwizDNsvMFUCcVKC5VrpgwEZ5qItJHjJI3WdgApVl1cPSmvrzqb61qkv2KktyS3RwBgJh1DxL8rl4qBtmXBpX5iobqOSvhBpMRpU66fPqUAsaLfzIxYl83-IfzTbPKleoey8ayvcq5o9GOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=Zto5xFimVJtZRFIH3Jo07xOAktW3e839kBIz_TrKSvYv9uIWC4rTObIEPSiYznpqR8OaIpcLGmO3am3smgmq1gZntfLpPT-RS0VeWeg4O6H4vVaO-ek-MF-VFAK4tlYsZiBgoi2puLC68AHXvfeuWpZ8Oa-lfKKhmiFZraFn1zAaX78rMtRvWwyNjQLC7f4ndTBxgbdwizDNsvMFUCcVKC5VrpgwEZ5qItJHjJI3WdgApVl1cPSmvrzqb61qkv2KktyS3RwBgJh1DxL8rl4qBtmXBpX5iobqOSvhBpMRpU66fPqUAsaLfzIxYl83-IfzTbPKleoey8ayvcq5o9GOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
فک کردین اومدم از قیمت دلار آه و ناله کنم؟ نه اومدم پاره‌اش کنم!
رزق و روزی دست خداست نه آمریکا، دلار قیمتش عوض شده، خدای ما که عوض نشده.
قیمت دلار هر چقدرم بشه، باز روزی مارو خدا می‌رسونه، منم اعتراض دارم ولی ناامیدی تزریق نمی کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71092" target="_blank">📅 15:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=Mcqm1BY8A87LAm3G3VfkJJxUu7rhFnHYZlLcOJDxtQYbMfLTxuS7FAtbBAmcNhZX-Xo8Nec0kTAkNwPaD2RgTB-riL5Y0KG_MDak9pBwLWmL7Hg4TceB9ofJHGWd0Uq4nYIF4xqOv7fx-_w0ijbcM3iti7b-obUZxHcPRlC8hVK1TjxgBBa0-ZkKx3bCmvIjCNSRIpR0JuVl8M166zk96PDGarjpmlc6JcEu4goRDimeVvVvsMBNtp_JvYg4GEeIxrcoYNaV5d69QMIqf5BhwtNH2YS5j9GAL9Ikg7T2ZColY7Megp37lvW9nzTT2N-lge-i23jzNQb9BOGSG6ep8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=Mcqm1BY8A87LAm3G3VfkJJxUu7rhFnHYZlLcOJDxtQYbMfLTxuS7FAtbBAmcNhZX-Xo8Nec0kTAkNwPaD2RgTB-riL5Y0KG_MDak9pBwLWmL7Hg4TceB9ofJHGWd0Uq4nYIF4xqOv7fx-_w0ijbcM3iti7b-obUZxHcPRlC8hVK1TjxgBBa0-ZkKx3bCmvIjCNSRIpR0JuVl8M166zk96PDGarjpmlc6JcEu4goRDimeVvVvsMBNtp_JvYg4GEeIxrcoYNaV5d69QMIqf5BhwtNH2YS5j9GAL9Ikg7T2ZColY7Megp37lvW9nzTT2N-lge-i23jzNQb9BOGSG6ep8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
🇰🇼
روز گذشته، یک پهپاد انتحاری که توسط ارتش جمهوری اسلامی پرتاب شده بود، یکی از واحدهای برج مسکونی الدیره در شهر کویت را هدف قرار داد. این اصابت باعث آتش‌ سوزی و تخریب کامل آن واحد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71091" target="_blank">📅 14:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71090">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=aSr_drfDtyuX4YbN1fewDea1kIx1Nko6BD_rT4GCN6Fw5B_FviBkvWHCR7kcWg9HkCuxp-DlYEdUWWNFZTUuerIAycrmD_2Z0k5l_mBTyxEyPZUXgUPOLTBGbQGxOhkszlPrh7c6xEXVK9UcE32SNXjKJF5buZcjMfuy3a3nT2uigQb-BU7akKqbaA7H4c-K3BNKrjqYCxsMCX2qIb-hJe0kIZMn8aklDFckJWKVYu2u_xeOOiXdtsK1ni6T46c_VhRNWekyEZlThqyqi53c3T2dtSLJRXAkMlRzK3pw6q_1QLQEt4vhUxExxgfd5nmyAGHCw4R_eltR0moAVX10Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=aSr_drfDtyuX4YbN1fewDea1kIx1Nko6BD_rT4GCN6Fw5B_FviBkvWHCR7kcWg9HkCuxp-DlYEdUWWNFZTUuerIAycrmD_2Z0k5l_mBTyxEyPZUXgUPOLTBGbQGxOhkszlPrh7c6xEXVK9UcE32SNXjKJF5buZcjMfuy3a3nT2uigQb-BU7akKqbaA7H4c-K3BNKrjqYCxsMCX2qIb-hJe0kIZMn8aklDFckJWKVYu2u_xeOOiXdtsK1ni6T46c_VhRNWekyEZlThqyqi53c3T2dtSLJRXAkMlRzK3pw6q_1QLQEt4vhUxExxgfd5nmyAGHCw4R_eltR0moAVX10Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
🇦🇪
با افزایش تحریم‌های آمریکا تجار و بازرگانان می‌گویند امارات از بارگیری لنج‌های ایرانی خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71090" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71089">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=b0x04bmp4m8Z1eqhqZYkbUaNml6Mxl55jzZrCyRt1RP_pjgnPSUxZ9bNM4w9MDzC8AfSHyb4TniEjAxJbmTMxRrKRI7xFaGLhNHdTcfrl3WSGUYA-yM7y47Bx4jPxg77gazXhMJxpft1fzV0ihH8eV_V54tG3xpt1vghQnnorvv9qOJW6n3u806fofjt1ROfqSxLx1xy1Xhuzwmde8Sdl0sUQ-GmRBvwoGceiod6i02jHAxeHvRTGpV0cPqaxo5qOPy7DJU7ew2vfva8qiAA2IT3r1cMrglc1nBraQ7ehdnu52N98WguVDA5kXv9Hr_-Bpe1WNDwy_6qxGILHIX1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=b0x04bmp4m8Z1eqhqZYkbUaNml6Mxl55jzZrCyRt1RP_pjgnPSUxZ9bNM4w9MDzC8AfSHyb4TniEjAxJbmTMxRrKRI7xFaGLhNHdTcfrl3WSGUYA-yM7y47Bx4jPxg77gazXhMJxpft1fzV0ihH8eV_V54tG3xpt1vghQnnorvv9qOJW6n3u806fofjt1ROfqSxLx1xy1Xhuzwmde8Sdl0sUQ-GmRBvwoGceiod6i02jHAxeHvRTGpV0cPqaxo5qOPy7DJU7ew2vfva8qiAA2IT3r1cMrglc1nBraQ7ehdnu52N98WguVDA5kXv9Hr_-Bpe1WNDwy_6qxGILHIX1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
🚂
برخورد قطار با یک کامیون در گذرگاه راه‌آهن در گدانسک لهستان.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71089" target="_blank">📅 13:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71088">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=jLYEMFsMuse95PU43lQhJctRszPYbIeAJIq5wzj9_hzZwriRA5-K1Gx6xXjrlzKB6f66QpLpIccWqM7N7nZLgkh5TDPWTmW8hmOK4sxOb4eLDcpl0TwAPktqLmjSHrUev_5I1TlikQFfyc3iYkx3t7FR_J0Oy9mVIV-KcBGljXFpMOgwnWj33vHQPJ4i3qT1HnIf0s-Xc5cxQFUCL7cpXNdChdqe3gTNIyFzqoD_VVl_i7JgHL-GMG9N5R-eJ9U8Sat-w4_vWBBZg4fsr5vdG1bV0s_OEJaYsNv7Dj8aBG9cqa5dq6jv-rIq9a2AAmKeQ75d01l8FT8JB-AGgWwVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=jLYEMFsMuse95PU43lQhJctRszPYbIeAJIq5wzj9_hzZwriRA5-K1Gx6xXjrlzKB6f66QpLpIccWqM7N7nZLgkh5TDPWTmW8hmOK4sxOb4eLDcpl0TwAPktqLmjSHrUev_5I1TlikQFfyc3iYkx3t7FR_J0Oy9mVIV-KcBGljXFpMOgwnWj33vHQPJ4i3qT1HnIf0s-Xc5cxQFUCL7cpXNdChdqe3gTNIyFzqoD_VVl_i7JgHL-GMG9N5R-eJ9U8Sat-w4_vWBBZg4fsr5vdG1bV0s_OEJaYsNv7Dj8aBG9cqa5dq6jv-rIq9a2AAmKeQ75d01l8FT8JB-AGgWwVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با رفیقش رفته دور دور الهیه و به یه دختره شماره دادن،
و حالا اولین پیامی که دختره براشون فرستاده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71088" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71087">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71087" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFwY3ftK1H_R5d8xSc3Em0s24auOwrNDq44QapJ4zHZLw-7HyECbXB-uSMWFZUNL89kgf5kvWgE6Baa7xLXv9POBRHXK0pSs6OABLgpM10mIgDjDJ2r5vjA025Jx0qSJy-3TX-KZJt2LTE79MgOVmcHw5xQW9g_thncOywjYCBK7rz_EZ6nZnxipfH-VdZaCOkr1kH1uuJZPsTLOKFwDNrvh6jc6E8SKVfYbqQoTxcjy6rdeJRxPDhrm3E1HRsjSJBB54_RU4qo6H8FaLMz5Ew7mhHRZ1o_x1hvnZvBwDuaODP1xhk5bu0nXRmX0jkIlx2HpHv_Dc8OWe0iaARy9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71086" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4843999275.mp4?token=Gr902Y1AKpgY9KOgzrW_FnCMx-KMjftGOzSCy-8ih2RD36mS5RrmOpd896T4H_9yfKApowpKHnoVTpVmzWAxg9RhVcotW5qUlfhOcqaa6XUh7Kqt0qtmkxXLfojVkshlNIh08niaEFo5R7aG3IHmRJUyEBtjztBGbYyh1X-yrPkzJz5Lyh4JCKHrRh2H5TvFbaCLPFjR2mz9UAwiRqcJ84jReG9QbqI67qx1fXGmWXskeg-nteIhO0VPZQ33hwHTnXpj2dKBq0uiYN_SzdbKLLzHUiQ0KLODUWzW9ZP5XiZlFmpvVKA8ZdlYrvr3pZQBbfNGQVYdJPxu6FI-v2mpuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4843999275.mp4?token=Gr902Y1AKpgY9KOgzrW_FnCMx-KMjftGOzSCy-8ih2RD36mS5RrmOpd896T4H_9yfKApowpKHnoVTpVmzWAxg9RhVcotW5qUlfhOcqaa6XUh7Kqt0qtmkxXLfojVkshlNIh08niaEFo5R7aG3IHmRJUyEBtjztBGbYyh1X-yrPkzJz5Lyh4JCKHrRh2H5TvFbaCLPFjR2mz9UAwiRqcJ84jReG9QbqI67qx1fXGmWXskeg-nteIhO0VPZQ33hwHTnXpj2dKBq0uiYN_SzdbKLLzHUiQ0KLODUWzW9ZP5XiZlFmpvVKA8ZdlYrvr3pZQBbfNGQVYdJPxu6FI-v2mpuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پرزیدنت ترامپ در رسانه‌های اجتماعی پرسید: «مردم ایران کی قیام می‌کنند و می‌جنگند؟» آیا دولت در حال بررسی مسلح کردن یا ارائه، سایر حمایت‌های مستقیم از مخالفان ایرانی است؟
🇺🇸
ونس:
ها ها ها... مگر پیتر دوسی امروز صبح این سوال را در فاکس نیوز نپرسید؟
سوال خیلی خوبی است.
و چیزی که رئیس جمهور گفت(درجواب به این سوال) دقیقاً همان چیزی است که من می‌خواهم بگویم.
قرار نیست درمورد این سوال صحبت کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71085" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQ6y9Co5kf_pkFfLMf4KyGoOs3JGbh0YGo1vR3IRHG1w8X8cRXvXtkcQQITt-vjDYwLMYZjuLHgQ90Z6Aea3_OghsZWGeFIYoWt_o1jSNVTncfBturrfabeUKhVCtdH6kA3u3rFFI5uS9rdk4o3zco4IEz0R6GODRqnM5bIxLAYYbIDpwCIXvwLDipn2tjFya9TwNIJYUD7mJjfnYy2Sr0MunHzCnq1wuMgrC0BmNYfUvzfsH9aJgteZ4cAycqq_nebOnuXuvtWGxorA8qfiY1G6_LEkLKUb0oe49sFfh0WHMLPDM0opPpQ_dZGxmMpd2SxCFa29LfCoAoanM1yY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی با این پست به شدت میسوزه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71084" target="_blank">📅 12:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=n4IQYkMJFhjFZmo5TQP8lhyqnxA_k3tWVihR46gJX-6hVWwJJ6RJ-yT_V8m8XwB1vDLty_vjDtGYkcS3XcpRCcJR_EjtS8CrsZa6PQV93CNCnKmn-XzUdxjXkKxb0HknpSjwN89kprOFt654jwdGd5yB8TWmHuevbJ57NRSeVlNJid1fPnqUTyracfOP2vGjsB7sBz2886bnqAGWy3Ao6PnkjwZut29fqc-qiHIcxFWmHl06Or2PhgK3Py8-pUb90rW6UIEGhGB2AIsOZyJG5UjzdDE6K3d68rfhngepVMnlGrhr_yIie5jDoEoRDDnsLUxKhVgRyU62usw-Qo4XNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=n4IQYkMJFhjFZmo5TQP8lhyqnxA_k3tWVihR46gJX-6hVWwJJ6RJ-yT_V8m8XwB1vDLty_vjDtGYkcS3XcpRCcJR_EjtS8CrsZa6PQV93CNCnKmn-XzUdxjXkKxb0HknpSjwN89kprOFt654jwdGd5yB8TWmHuevbJ57NRSeVlNJid1fPnqUTyracfOP2vGjsB7sBz2886bnqAGWy3Ao6PnkjwZut29fqc-qiHIcxFWmHl06Or2PhgK3Py8-pUb90rW6UIEGhGB2AIsOZyJG5UjzdDE6K3d68rfhngepVMnlGrhr_yIie5jDoEoRDDnsLUxKhVgRyU62usw-Qo4XNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از طرفدار حکومت
🎙
خبرنگار:
از قیمت دلار خبر داری ؟
🇮🇷
طرفدار حکومت:
بله شده 200 و خورده ای
🎙
خبرنگار:
با این قیمت پس چرا اومدی اجتماعات ؟
🇮🇷
طرفدار حکومت:
دیگه باید قدرت تفکیک داشته باشید تو ذهنتون و قیمت دلار یه چیزه و بیرون اومدن یه چیز
اصلا اگه امنیت ما نباشه شما میتونید راجب قیمت دلار فکر بکنید؟ نه نمیتونید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71083" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71082">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⏺
ویدیو وایرال شده از اعتراض یه زن کارتون خواب:
به عنوان یک کارتون خواب که 20 ساله دارم این زندگی تجربه میکنم!
شما مسئولین که مردان خدا هستید شما دیگه چرا؟
تو دانشگاه رشته حقوق خوندم
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71082" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71081">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=FaaPxyaAk3FRBRUI2o3kXWTYxiDrqwXV1UJMuzLxXXrfqpazC31wm1CLUHI2Mhn3gnpgDTqx0SMriF5I0t18AXb7pQltpuZAU1MxNmWzooTpNTSbMigkOMCvzaydg8TqbsKz9urgx_6sxAF8bS7uaonoIWX2IfSt7ZUFvNd-wAmrkFh12JqHtZNRCPOu-U1bK86wlfA8IByF-G6RxUWijxR-MWRrJEV-yycdSauzDi9hW1eRoYkOpZ27zM77NfqH1HZrSXXd9R3VukiD3LHriCvcM2_oSnOnQhpQuT_58HtwE6bpcmwKf4odOfgs58tS9Evk_KJRHpCpuGLlDt1N5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=FaaPxyaAk3FRBRUI2o3kXWTYxiDrqwXV1UJMuzLxXXrfqpazC31wm1CLUHI2Mhn3gnpgDTqx0SMriF5I0t18AXb7pQltpuZAU1MxNmWzooTpNTSbMigkOMCvzaydg8TqbsKz9urgx_6sxAF8bS7uaonoIWX2IfSt7ZUFvNd-wAmrkFh12JqHtZNRCPOu-U1bK86wlfA8IByF-G6RxUWijxR-MWRrJEV-yycdSauzDi9hW1eRoYkOpZ27zM77NfqH1HZrSXXd9R3VukiD3LHriCvcM2_oSnOnQhpQuT_58HtwE6bpcmwKf4odOfgs58tS9Evk_KJRHpCpuGLlDt1N5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسره دوست دخترشو برده تو کوچه پس کوچه ها بهش رانندگی یاد بده
آخرش هردو غافلگیر شدن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71081" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71078">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=YyoVO1P2GtH24jESJVaaIy_eP9tnr3CWrCOWCDK9PuzaZebUFpInYS5VGe6PgAe6IbySFK4eFRYDP2hd4q-vOf3QKMM-JD9sBBpP_GTYphCLsB9cctUv7Hm2sRW3wzS_kiqyeIudzFBXVKXn7H2Kzzk7LzLURewQe6p5CjwrVxP5V1qPsk4zeTO7UH0KY-CHYtKuXD-o-ufQx0rjQeHXRSBvmQ-8qZSROzvVGC0CuVCmhKRlHpeAKTAIo-ekGCcGYJkU8WaF2K72ul00gdYpZLqxVhvV7xkfuBZjbN5YJhlDm-_e2YsFt8SUAZ5wH5CXxj2T820Wxs3o50m5tK_N-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=YyoVO1P2GtH24jESJVaaIy_eP9tnr3CWrCOWCDK9PuzaZebUFpInYS5VGe6PgAe6IbySFK4eFRYDP2hd4q-vOf3QKMM-JD9sBBpP_GTYphCLsB9cctUv7Hm2sRW3wzS_kiqyeIudzFBXVKXn7H2Kzzk7LzLURewQe6p5CjwrVxP5V1qPsk4zeTO7UH0KY-CHYtKuXD-o-ufQx0rjQeHXRSBvmQ-8qZSROzvVGC0CuVCmhKRlHpeAKTAIo-ekGCcGYJkU8WaF2K72ul00gdYpZLqxVhvV7xkfuBZjbN5YJhlDm-_e2YsFt8SUAZ5wH5CXxj2T820Wxs3o50m5tK_N-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی دزفول چند تا دزد میرن توی یه خونه مجهز به وسایل ضد سرقت و 3 کیلو طلایی که توی اون خونه بوده و قاحب‌خونه قصد داشته باهاش طلا فروشی بزنه رو میدزدن!
صاحب خونه شب قبلش توی اینستاگرام گفته بوده که میخواد طلا فروشی راه بندازه که این حرفا رسیده به گوش دزدا ؛
فردای همون روزی که این حرف رو زده وقتی صاحب خونه خانومش که باردار بوده رو وقتی میبره بیرون یه هوایی بخوره دزدا میریزن تو خونه و طلا ها رو میبرن.
حالا صاحب خونه گفته که هرکسی هر سرنخی از این دزدا داشته باشه و بهم بده ، 10 میلیارد تومن بهش پاداش میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71078" target="_blank">📅 10:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71077">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0def551e36.mp4?token=V6RnHP5wpked8QWEnvRCkCkkA8FBcHianBdLu53zX3gZS5woaP0WQmAsEPRyN_zvLiAupQMctJAO6vYTAVCKBD6r_EXsRoEUJolCpa4hBvp7ksiPC3BpvJuXLHdGRybJv8_ksSVuxI8Btp46jKUjKDb1iKCqKkaiNuN3Wz8IzTp9KcMaMshkAJGjDs7JC6I4fu4OTFleG1MCoG3le5EbasPNKUmyphcrkBw0YlN_-ktaMcvvPpxPg2f4dSqWimRaO3FQ5feWkiJj4ZkJLtaBVToul3xU22ApOvnrD5wbIdgNLU5KDhyIe2Gg3c4GaD8SrZgfe0OSio7OoGjFq5BhHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0def551e36.mp4?token=V6RnHP5wpked8QWEnvRCkCkkA8FBcHianBdLu53zX3gZS5woaP0WQmAsEPRyN_zvLiAupQMctJAO6vYTAVCKBD6r_EXsRoEUJolCpa4hBvp7ksiPC3BpvJuXLHdGRybJv8_ksSVuxI8Btp46jKUjKDb1iKCqKkaiNuN3Wz8IzTp9KcMaMshkAJGjDs7JC6I4fu4OTFleG1MCoG3le5EbasPNKUmyphcrkBw0YlN_-ktaMcvvPpxPg2f4dSqWimRaO3FQ5feWkiJj4ZkJLtaBVToul3xU22ApOvnrD5wbIdgNLU5KDhyIe2Gg3c4GaD8SrZgfe0OSio7OoGjFq5BhHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه دختره داشت تو قزوين واسه خودش قدم میزد؛
که یهو یه پیرمرده خواست مزاحمش بشه ولی بعد که فهمید طرف پسر نیست، عذرخواهی کرد و رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71077" target="_blank">📅 10:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71076">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=CByrzygJ4u5E7SiR6f-o36EE0OqYiK2wwHfwif7aXmG-O4J2EXTiCl1D4SCuO3bHm3669w4oxBhxxKvN8HwOKYEn3sCnbKr3EPEfHUyEccXqmZSDEFlFexA9NhqlgXC2EhnxMH8WiNF5i1LfF2wn5pCuI7OSCrwCSBEz7pOagz0rH7_CIN_kN6IGNuBAFt_iu1hGqqs7bDP3TRQwDOm_aLS1dpzaSyKMby8DVnwUBYJUYSB9owuTVdI3FJbgU8wuUVHVNwAc8YaDxOOGWN3hqGN2HKi7PA3bOo6X41R4LoqoZqHt84z5dSMUsFhNwy72-dFZVjfoJeplFi11S9xykA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=CByrzygJ4u5E7SiR6f-o36EE0OqYiK2wwHfwif7aXmG-O4J2EXTiCl1D4SCuO3bHm3669w4oxBhxxKvN8HwOKYEn3sCnbKr3EPEfHUyEccXqmZSDEFlFexA9NhqlgXC2EhnxMH8WiNF5i1LfF2wn5pCuI7OSCrwCSBEz7pOagz0rH7_CIN_kN6IGNuBAFt_iu1hGqqs7bDP3TRQwDOm_aLS1dpzaSyKMby8DVnwUBYJUYSB9owuTVdI3FJbgU8wuUVHVNwAc8YaDxOOGWN3hqGN2HKi7PA3bOo6X41R4LoqoZqHt84z5dSMUsFhNwy72-dFZVjfoJeplFi11S9xykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه دستگیری یه قاتل فراری در ایرانه
:
قاتل با چاقو مامورا رو میزنه و داشت فرار میکرد که یکی از مامورا عین راموس تکل زد و طرف افتاد.
بعدش یکی دیگه از مامورا ویلچر برداشت و میکوبید تو سر و بدن قاتل تا بیفته زمین، هر لحظه این فیلم عجیب‌تر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71076" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71075">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L229KRy5cpPbotHr68bBeJhKkdJbdTUq4uO4EiPuU21HrKC1Qgae9C1Nrj3J5tbt8_Nh34dO_JVx_g9LD-doX8GzfkA5EJuBuQqsoW6U-ukMRWic5gZx-Trby7NtagwhwSH2D4L60a0y0iYAcZf4O3FCt0vhJyNskQic1zRpUHLpXpREGuNrl6nYSeekaIC-RA-dzFUIwJulHH4b2RfWjok9-iIwvELHsa6xtOdV78hJVeunvJorAu2QpHt9IBWgOuxnb2VSNWZ0rZktBLLrF843uYEXqBadNQVOG6IJE883jC1fu9HO41qnTv4zFrvns9EAqh4IO4sUjA4pFplROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
اتحادیه اروپا رسماً به «عملیات طرد اقتصادی» (Operation Economic Outcast) پیوسته است و ما از موضع قاطع و زودهنگام آن‌ها قدردانی می‌کنیم.
ایالات متحده در کنار متحدان خود قاطعانه ایستاده است تا اطمینان حاصل کند که رژیم جنایتکار ایران نمی‌تواند از سیستم مالی جهانی برای تأمین مالی جاه‌طلبی‌های هسته‌ای، برنامه‌های تسلیحاتی و نیروهای نیابتی تروریستی خود بهره‌برداری کند.
جهان پیام روشنی به رژیم ایران می‌فرستد: ما تا زمانی که آخرین شریان حیاتی مالی باقی‌مانده قطع نشود، از تلاش دست نخواهیم کشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71075" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71074">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71074" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71073">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuGU0xv4iee-utA3CjLyCILacar9pXg4B-rTPLdwq-41eU7JvhcyrhRv6GI52IkeD3NBzN3JnMqXMPvbZXBS4J1-pP4TCOslgSTnoLGv6TdopciNdP545fGfh4SjAer176mwTMwh1rBrPVjA1neRp4ZSfnqkhRLhQ1Z7INkRmzw0mHV-FyKVBTdgepgi4vBG99LDwZTbNssuU5awj75_J7PoIUCrTQx4dJtRihbru3F5kKHV7ebmKDH3pBC35SPz7iyPoLNTvjA3NKwbe_4Cd8WVgRgqxhCOZd-3yPpi0A-OEF7NGtpm9aSwKHrWxmQFhlHCuFxeXm7v7oh81eM2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71073" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71072">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇷
نایا:ایران چندین موشک به سمت کشتی ها در تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71072" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71071">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c46c090035.mp4?token=LSJero3CKIeNm5fA_N95-6dvX4d9GkbTeIS-DU45VBdtXTHBOiXH04KLF9gYb6yoeAjPlZvXNJpx-jFZeGUWiiIV7j3NXaAh9CwDNDJV-ILLmXS6mmU1DP9dPE_cOAv25iORShAFGqZBbZgolyIaMY_HkhTJA2RSKxhbeBN7Fw2-13olhog70FQi123YEmIP51dd-5cE5SaUVqjdctCE5ywpI_IisIQzfsO9tmqrEvPg4pF9xgahIL4YCb4xb99GdoRQZ5DcL6chTDeC8BzOFHY-qdj2Tr-vDWT6nr5LH6iEHuN4Sy8DkB9-xujvHhmSLjDIkIN7Teik_BCGhrpKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c46c090035.mp4?token=LSJero3CKIeNm5fA_N95-6dvX4d9GkbTeIS-DU45VBdtXTHBOiXH04KLF9gYb6yoeAjPlZvXNJpx-jFZeGUWiiIV7j3NXaAh9CwDNDJV-ILLmXS6mmU1DP9dPE_cOAv25iORShAFGqZBbZgolyIaMY_HkhTJA2RSKxhbeBN7Fw2-13olhog70FQi123YEmIP51dd-5cE5SaUVqjdctCE5ywpI_IisIQzfsO9tmqrEvPg4pF9xgahIL4YCb4xb99GdoRQZ5DcL6chTDeC8BzOFHY-qdj2Tr-vDWT6nr5LH6iEHuN4Sy8DkB9-xujvHhmSLjDIkIN7Teik_BCGhrpKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پورمحمدی:
انسداد تنگه هرمز، برنامه‌ریزی شهید پاکپور بود.
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود.
شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71071" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71070">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46300e7107.mp4?token=cZm6DIdrnwEiiQttWi5390cFNTMjU7hUVnblRHwTqK7xph8FKd8kbtwi4nRjYaPzPjMFnIFqghYQqWq6647re4dwJuXt8uyxEtllUuBdprWxmiEbFzdIReJ_ejkXWNz_sTqRjAKhfMOfnt-R8PzEJstoNe_5imwnDv-mdQL9990j3rBYFxYAvAhpsHwoY1XkXqVe0rMaNXBBJ41X39zv62ZaMEXyq03uHFbsiorGHNjFulLjTthiu7B-OXiGOzT6CpeibgGG0-R3hw_SEbTaDWnlctgpRjrUpLJbv_hDWhPLDBP5yEqOznK2bE1Lxwkt08CpVtwiNiWatDWISCjvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46300e7107.mp4?token=cZm6DIdrnwEiiQttWi5390cFNTMjU7hUVnblRHwTqK7xph8FKd8kbtwi4nRjYaPzPjMFnIFqghYQqWq6647re4dwJuXt8uyxEtllUuBdprWxmiEbFzdIReJ_ejkXWNz_sTqRjAKhfMOfnt-R8PzEJstoNe_5imwnDv-mdQL9990j3rBYFxYAvAhpsHwoY1XkXqVe0rMaNXBBJ41X39zv62ZaMEXyq03uHFbsiorGHNjFulLjTthiu7B-OXiGOzT6CpeibgGG0-R3hw_SEbTaDWnlctgpRjrUpLJbv_hDWhPLDBP5yEqOznK2bE1Lxwkt08CpVtwiNiWatDWISCjvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چندشب پیش تو شیراز یه دعوای عجیب رخ داد؛
دوتا دختر با ماشین میزنن به ماشینِ دوتا پسر؛ بعد گفتن ما مقصر نيستيم و داشتن فرار میکردن!
پسرها هم گفتن چون بی‌ادبی کردی، باید بمونی خسارت بدی، بخاطر همین پریدن رو کاپوت ماشینِ دختره که فرار نکنه!
این وسط یه پیرمرده هم خیلی بی‌دلیل از دختره کتک خورد...
تهشم دختره گفت دیگه این موضوع واسم مهم نیست چون زنگ زدم شوهرم سروان شهریزی، الان میاد کون همه‌تون رو پاره میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71070" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71069">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876466a913.mp4?token=ZT8ApHwRyvtfU29pJoW3FuZGmHWHMKrxR0ufYqlq3T2Kx3hUBFVstJF3nwwR5QVZHOtHkKjoc9R_IEkpdkWtvkxsVP-b9WiVnbgfgqCf9ZqzT4GjQdGL05Y72pWgArZJEgipV5t5VrDkHX7tzxHDd-NCkPKBNWTSQasdOCYrIhUi4uFoe0u-nzkH6M6Vkje7wFqpo081u67IjJiEonUuSRA3I4YiBoZ3sSU0B1g7sw8DepWqWkVjEfKkOvCwk4vxzBPqJa3LUJzei1MLlRDTGSahQTlwGxjmLIuMSz-zbqdIrHsLRiyhD2KmvGhtRtkTgTY6crS07xOjW6L7Hl4hvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876466a913.mp4?token=ZT8ApHwRyvtfU29pJoW3FuZGmHWHMKrxR0ufYqlq3T2Kx3hUBFVstJF3nwwR5QVZHOtHkKjoc9R_IEkpdkWtvkxsVP-b9WiVnbgfgqCf9ZqzT4GjQdGL05Y72pWgArZJEgipV5t5VrDkHX7tzxHDd-NCkPKBNWTSQasdOCYrIhUi4uFoe0u-nzkH6M6Vkje7wFqpo081u67IjJiEonUuSRA3I4YiBoZ3sSU0B1g7sw8DepWqWkVjEfKkOvCwk4vxzBPqJa3LUJzei1MLlRDTGSahQTlwGxjmLIuMSz-zbqdIrHsLRiyhD2KmvGhtRtkTgTY6crS07xOjW6L7Hl4hvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق گفته خانم دکتر؛ دیگه خوردن واژن خانم‌ها نه تنها دیگه نباید باعث خجالت شما بشه بلکه پر ازخاصیت و فواید زیادیه که تاحالا درجریان نبودیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71069" target="_blank">📅 23:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYJSeRUVM7xx6lwcnNceBB6ma-suY0s9-ZAlPMfTnnBRf51XG0gAwSAysjgEkEAIDRtbgpGFN-BfTchmkCloVKhuUEQz4y2qWa9Xay6dJl-6aVNcOjMKNXAGxuWlPHyPywUA-q-c6Ixy1jTBgYgCerYzUH8S2qAodrfx_wp63VN_zXj_aqsGtaasX2HPbtp_pqA0TJEU-3EP8kGVmdc4Q1mlX9nmflw6I0eOLfRibOXxPhxhFrBKHS-b7rxmhGqbpWrdAVTbF3IMw6PHvIBpQRlch40fuYttFNsNDV-M6nFuKlqj3KG2VcnRgV7hatY10G3BMqy-sr8FWGKJwjNKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیبافِ:
قهرمان، محکم‌تر «شورت» (Short) کن؛ طوری که انگار آینده‌ی شغلی‌ات به آن بستگی دارد (چون واقعاً هم همین‌طور است).
یا اینکه سطح ذخایر را به زیر «منطقه خطر» برسان و فرو ریختنِ آن حفره‌های عظیم (و البته نابودیِ شغل خودت) را تماشا کن.
یا هم به درگاه خدایانِ نمکِ «برایان ماوند» (Bryan Mound) دعا کن.
دنیا که از همین حالا بساط پاپ‌کورنش را آماده کرده است :)
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71068" target="_blank">📅 22:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71067">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=PpOSKbTYi3Y-vbvE9AwqpYnXsB3uTyOBasQ0J8z0SL8gUYIdPyJXhF2E0OwzI8V70h48B3OPV0M4Wqr6nADQLtfD_bCXA3IKleewEahHW12dyS0lamf-cFY268XSxONYkQyIVNXf4zh8i1xIvkGdXiMutp7t8fsh3H-QVKFAYM4tln9QnLN9QSKFf6VwxP-RVfVDdG5GrL1iJclBfk0gm8XJM2luLIoHq0bYeQnI0BzKdk-1zggr-h1U2K2gW6cXCWUNkp0pHXHwuJtqdNyNz3peD_GtzrTueWYU4yra3okGG_vJiwuUXaE8NJ0thRpcogFFY7u_ltWI3Rxi9wY8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=PpOSKbTYi3Y-vbvE9AwqpYnXsB3uTyOBasQ0J8z0SL8gUYIdPyJXhF2E0OwzI8V70h48B3OPV0M4Wqr6nADQLtfD_bCXA3IKleewEahHW12dyS0lamf-cFY268XSxONYkQyIVNXf4zh8i1xIvkGdXiMutp7t8fsh3H-QVKFAYM4tln9QnLN9QSKFf6VwxP-RVfVDdG5GrL1iJclBfk0gm8XJM2luLIoHq0bYeQnI0BzKdk-1zggr-h1U2K2gW6cXCWUNkp0pHXHwuJtqdNyNz3peD_GtzrTueWYU4yra3okGG_vJiwuUXaE8NJ0thRpcogFFY7u_ltWI3Rxi9wY8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ارتش اسرائیل تپه علی طاهر در جنوب لبنان را فتح کرد و کنترل آن را در دست گرفت.
ارتش اسرائیل پاکسازی دو مسیر تونل زیرزمینی حزب‌الله در رشته‌کوه علی طاهر در جنوب لبنان را به پایان رسانده و در تلاش برای خنثی‌سازی آنهاست.
لشکر ۳۶ کنترل عملیاتی رشته‌کوه را در بالا و پایین زمین به دست گرفت و آن را از وجود شبه‌نظامیان پاکسازی کرد. برخی کشته و برخی دیگر فرار کردند. خنثی‌سازی زیرساخت‌های پاکسازی‌شده در حال انجام است.
در داخل، نیروها مراکز فرماندهی، اتاق‌های تسلیحات، اتاق‌های ژنراتور، محل‌های زندگی، دوش‌ها و یک آشپزخانه را یافتند -- که به شبه‌نظامیان اجازه می‌داد عملیات جنگی را انجام دهند و برای مدت طولانی در زیر زمین بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71067" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71066">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWKrALVaXLGcJ82N5Ca4MeGhx9bfxSLsBJCt3Y-EVilINnYmahIZxN3PSpPiHHPo2AgdUD00XPawXSFn-FPux8d_ufbexh6T5JvEtLeRrmvj3mCUxAUU3yDSQKnQsnl78xr9_bZgWDuVVZqkzSYdQ1Zj5uuJZbbcGhUjlRreYQZ6m8SnBeuOVXEmsa1yHqlkJxuQA7SkCdzV5qdQz0LUIdaC8jpgwMH0WFDzbxT2eRzBFSHLpJzknHzur8cdzLqu7BKYopAEv0DG3CX1ug1NXxvDMYpEAD4lT4yN1tmKEoNFQ7u6FLCTdFb9te_yYeaBQdb2-SrjKR3fPqYkfTHA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71066" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71065">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LJABt9C9zrrhWjmdqI22WwBHG6Ul2BKwC-gGz6sQAA6iYdL3EwlfDpwEzOHpHApoPGQdgEJUw1Ox8yPNlTO3HPKrKL-kQG8RMEwpKhp1tttHW1rMDgknBpIOsvJzci7hM6KNfSlyuggCtD2qIQYiEfv9yWdU5PdXM_JJTG0Rtfza81mbTqnJh2rgMLAkr1s_VQ98mYRaAME00JaBcV6HFlcj-rEJht1de1oP1uYYsdX_tX7jO8VvtCG_Jzs3u2IO4jWaFNMDAwHkfxFoi9gLcv2AJ0YRPOvFx7odMr_Z65v0aSiNBycLU8PGDpFnu5xh6Yk9rNVjnnml1qe8mfMjHis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LJABt9C9zrrhWjmdqI22WwBHG6Ul2BKwC-gGz6sQAA6iYdL3EwlfDpwEzOHpHApoPGQdgEJUw1Ox8yPNlTO3HPKrKL-kQG8RMEwpKhp1tttHW1rMDgknBpIOsvJzci7hM6KNfSlyuggCtD2qIQYiEfv9yWdU5PdXM_JJTG0Rtfza81mbTqnJh2rgMLAkr1s_VQ98mYRaAME00JaBcV6HFlcj-rEJht1de1oP1uYYsdX_tX7jO8VvtCG_Jzs3u2IO4jWaFNMDAwHkfxFoi9gLcv2AJ0YRPOvFx7odMr_Z65v0aSiNBycLU8PGDpFnu5xh6Yk9rNVjnnml1qe8mfMjHis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ترامپ هم اومد به بازار
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71065" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71064">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=Y1vLo2VzdIIOd-xy4fJHPnZHnZKx53MIO7mBdA6-SaacCDj7xvbpnTVqe6mnYYSbcfis6aHRwaOPg2SQ4yMfu3K91ObHVeGCu2VifpvwKTUjTxP5C9l3j9OpUt5vkwvGpJbcHl2JduWRi6ST5F-YFsQWwYRXeCTPFqnkXD-EjfD2GxfnTU56Cv2PfE1d6Ky7LiX32oibJg7q9jIMqFYQMBHmrlmOM8PUSj88imqiF7SXHUMTs7HGakub1Ttn2oE-KxsxgzIEueo85iybrA9OIpmBgRrOvuSQFJkpJuTCJtrDnLy-2EdCPJdPwh8Jhwfl6BF1-YcyWLQMdsRgqH8Mrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=Y1vLo2VzdIIOd-xy4fJHPnZHnZKx53MIO7mBdA6-SaacCDj7xvbpnTVqe6mnYYSbcfis6aHRwaOPg2SQ4yMfu3K91ObHVeGCu2VifpvwKTUjTxP5C9l3j9OpUt5vkwvGpJbcHl2JduWRi6ST5F-YFsQWwYRXeCTPFqnkXD-EjfD2GxfnTU56Cv2PfE1d6Ky7LiX32oibJg7q9jIMqFYQMBHmrlmOM8PUSj88imqiF7SXHUMTs7HGakub1Ttn2oE-KxsxgzIEueo85iybrA9OIpmBgRrOvuSQFJkpJuTCJtrDnLy-2EdCPJdPwh8Jhwfl6BF1-YcyWLQMdsRgqH8Mrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
رقص عجیب «حسن حسین خانی» مداح نزدیک به حکومت  در حالی عجیب  و  با شلوارک! تو یک  ویلا با آهنگ شماعی زاده
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71064" target="_blank">📅 20:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71063">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=XK3ISrV0oA1j5CnC4uqezWhFqN7qaE-JncEHu2YCbLSfAyYF85zyJHlwfhmWzKQYQCXyXiTMGbe_Z9EfV5ajRdAXvBbXhEf3Rf-oLBDVurYcjPYP9-Hs3GiLF7qTGjZGHrkJOgG954lknDJYN_3IcoP1K73vDWKZ559BIoqSlREH3d11rJJUNCLRv_XgP3aQZZd8EDKr9qlo9W0CvgFEWxXbwUoRJKnbxBvggETPaMu84X769aZgdGq5oP_qxSh2XwKIl7bhDvW_kfwwPIggmUSMLMuAwgwxwaV-MzchouqQaPYka5KcfOE-fwgFpCqwGXOLV-hlnMQ8bfwqTIY60Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=XK3ISrV0oA1j5CnC4uqezWhFqN7qaE-JncEHu2YCbLSfAyYF85zyJHlwfhmWzKQYQCXyXiTMGbe_Z9EfV5ajRdAXvBbXhEf3Rf-oLBDVurYcjPYP9-Hs3GiLF7qTGjZGHrkJOgG954lknDJYN_3IcoP1K73vDWKZ559BIoqSlREH3d11rJJUNCLRv_XgP3aQZZd8EDKr9qlo9W0CvgFEWxXbwUoRJKnbxBvggETPaMu84X769aZgdGq5oP_qxSh2XwKIl7bhDvW_kfwwPIggmUSMLMuAwgwxwaV-MzchouqQaPYka5KcfOE-fwgFpCqwGXOLV-hlnMQ8bfwqTIY60Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
من به توانایی‌مان برای از میان برداشتنِ یک‌بار برای همیشهٔ این تهدید ــ یعنی سرنگونی این رژیم ــ اطمینان کامل دارم.
این همان مأموریت اصلی است که همچنان پیشِ رو داریم، اما به تحقق آن نزدیک شده‌ایم. این کار غیرممکن نیست؛ بلکه کاملاً دست‌یافتنی است.
آن‌ها بی‌دلیل از حمله به ما پرهیز نمی‌کنند؛ آن‌ها به همه حمله می‌کنند، جز ما. آن‌ها از قدرت ما، توان بازوی ما و عزم راسخ ما آگاهند.
من خطاب به دشمنانمان به‌طور کلی می‌گویم: با ما درنیفتید. اگر درسی گرفته‌اید، بدانید که نباید با ما دربیفتید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71063" target="_blank">📅 19:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71062">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
شلیک موشک/پهباد از سیریک به سمت کشتی ها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71062" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71061">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdLcw1PewVc8Yf7hzDvJ_fQuWueAjFW4UmW5VjJ-dIAVAZ7NDL_ag2xp3S6xe8zn-qexbfpdqHU1mZDnSk5f_3ExmjMXp5RszIL3VN93QdYbVtBcoGmtUNx0d-EwDbTlemHSBXJx2sBZ04qiHcS5u8TM2ffwsMPrPYBt5g5RKOdCEQehzYAqfKyqeJgn_JNyWx_tnIxu0jYUlUIJSyZ8q8w4yJTGS9C69KUgDZ0yU3YuM0dkY9l7lGOEN42lf8V_xFMz2EPjDF0XNRhoeyOAWLMSQPUQHNesG8btd1A2pda-fxvDEstc3DEMUSq9zaLbyeNmJLHq9xzBsqnQ6cKAiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
برای آن مشتی خائنِ پست‌فطرت که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید بگویم که ما ذخایر تقریباً نامحدودی از مهمات با کیفیت متوسط تا عالی در اختیار داریم؛ بسیار فراتر از آنچه ممکن است برای این عملیات یا هر جنگ احتمالی دیگری (که وقوع آن بسیار بعید است!) نیاز داشته باشیم.
علاوه بر این، ما در حال تولید مهمات با حجمی بی‌سابقه هستیم. ما در حال انباشت و آماده‌سازی برای مقابله با هرگونه وضعیت پیش‌بینی‌نشده‌ای هستیم که ممکن است رخ دهد.
ما این مهمات را برای خودمان — یعنی ایالات متحده — نگه می‌داریم و فعلاً به دیگران نمی‌فروشیم، هرچند فروش به متحدان به‌زودی از سر گرفته خواهد شد.
همچنین، لازم است بدانید که دولت بایدن حجم بسیار بیشتری از مهمات را — بدون دریافت هیچ‌گونه هزینه‌ای — به اوکراین واگذار کرد، که این مقدار بسیار فراتر از مهماتی است که ما در ایران به کار گرفته‌ایم.
صدها میلیارد دلار کمک رایگان به اوکراین و ناتو اعطا شد؛ هزینه‌هایی که اگر از اروپایی‌ها خواسته می‌شد، خودشان آن را می‌پرداختند.
با این حال، ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71061" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71060">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=th_Gs5pS63hpsthhAbX8_JQW3tU_w0qW80zcJIXjY7HVSnKjuNRMWAOSyzTmILpZ_I8LsK9aJ6ddXWEXrY0ZlsIo6CptM4Jv1932cIOWn9qe3Dtu4xaDWQ7_euAxG8j1Ux5hwoDzGhRz7O-q8U_KYNgV3cBem-odbIBp5o7o0TAgpdV6p0L5skOjZfrwaJAZVv7oxhveeMabIWhVibhhsQB5RBzWj6x4z96_PRcs1NAtEh0FSSh3THfJrim5TjRKjtlxhGPJEQ8E8ipa1PFHhEKwRUTZBYpZXAdbep6yZfYYbn8p4eiYUtM3OQztV6RJ9GJ8v-S8M_MpzOWTvSvOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=th_Gs5pS63hpsthhAbX8_JQW3tU_w0qW80zcJIXjY7HVSnKjuNRMWAOSyzTmILpZ_I8LsK9aJ6ddXWEXrY0ZlsIo6CptM4Jv1932cIOWn9qe3Dtu4xaDWQ7_euAxG8j1Ux5hwoDzGhRz7O-q8U_KYNgV3cBem-odbIBp5o7o0TAgpdV6p0L5skOjZfrwaJAZVv7oxhveeMabIWhVibhhsQB5RBzWj6x4z96_PRcs1NAtEh0FSSh3THfJrim5TjRKjtlxhGPJEQ8E8ipa1PFHhEKwRUTZBYpZXAdbep6yZfYYbn8p4eiYUtM3OQztV6RJ9GJ8v-S8M_MpzOWTvSvOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
کسانی که دوستتان دارند، شما را فردی خوش‌برخورد، شوخ‌طبع، سخاوتمند و بذله‌گو می‌دانند؛ اما دیگران می‌گویند که شما سخت‌گیر، متکبر، مغرور و حتی بی‌رحم هستید. به نظر شما، کدام‌یک از این توصیفات درست است و کدام نادرست؟
❤️
شاهنشاه آریامهر:
بی‌رحم؟ گمان نمی‌کنم.
متکبر؟ قطعاً نه.
مغرور؟ شاید کمی. اما در مورد کشورم—و آنچه به دست آمده است
نمی‌توانم شخصاً دچار غرور شوم، چرا که انسانی مؤمن هستم. من عمیقاً به خدا ایمان دارم و اهل عرفانم؛ پس چگونه ممکن است مغرور باشم؟
انسان در پیشگاه ذات ازلی، هیچ است؛ مطلقاً هیچ؛ گویی اصلاً وجود ندارد.
البته با نگاهی به دستاوردهای این کشور، قطعاً دلیلی برای احساس غرور و سربلندی وجود دارد.
اما بی‌رحمی؟ این ویژگی من نیست؛ این نهادهای حکومتی هستند که باید عمل کنند.
وظیفه آن‌هاست که کسانی را که قصد آسیب رساندن به این کشور را دارند شناسایی و خنثی کنند. اگر نام این کار بی‌رحمی است... خب، در آن صورت باید بپذیریم که در این مورد با هم اختلاف‌نظر داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71060" target="_blank">📅 18:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71059">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e330a05.mp4?token=potLpEj7YMVF2GAg4nnh0AAJB9xpY0lD7uqu2wlYWbuNDnBoC3EYnKSFRaSbEGpxPV_K6i8ckBsKn2X3hFxy6eN0woTAa2hGPD05x5nl8YDxCJBUKAhq60oeRDZeB6zORbiTizPQeJThbxaXu3Bm7Jj4XwcqFRZu0qQGxsHjyvyKGDHdmSZAhSouY6EYYhlbH2y-ffyzt3R3artSEBVyXcJS1_Xcx75cdDuKPQyOeUgc3hyxEbMlTmo_Mrhf7oe93d8lUYEj0uZC1w8ns5v1Q8O_enxXhC7z4gbv_3wDJjv4bFviPLd_uqzpk9udD4jJXFNlDVX_jQmxEUqkhwfIxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e330a05.mp4?token=potLpEj7YMVF2GAg4nnh0AAJB9xpY0lD7uqu2wlYWbuNDnBoC3EYnKSFRaSbEGpxPV_K6i8ckBsKn2X3hFxy6eN0woTAa2hGPD05x5nl8YDxCJBUKAhq60oeRDZeB6zORbiTizPQeJThbxaXu3Bm7Jj4XwcqFRZu0qQGxsHjyvyKGDHdmSZAhSouY6EYYhlbH2y-ffyzt3R3artSEBVyXcJS1_Xcx75cdDuKPQyOeUgc3hyxEbMlTmo_Mrhf7oe93d8lUYEj0uZC1w8ns5v1Q8O_enxXhC7z4gbv_3wDJjv4bFviPLd_uqzpk9udD4jJXFNlDVX_jQmxEUqkhwfIxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های این پسر درباره‌ی اونایی که میگن کسایی که ریش ندارن کونی هستن رو با هم ببینیم:
کدوم مادرجنده‌ای اینو باب کرده که هر کی که ریش‌وسیبیل نمیذاره، کونه؟
شما برو فیلم سوپرا رو نگاه کن، عمو جانی کونش هم یدونه مو نداره، چه برسه به صورتش.
ریشو کسایی میذارن که ترس از کون‌شون دارن، اونایی که عقده دارن و بچگی کون‌شون گذاشن، ریش میذارن.
خیلیا ریش دارن ولی صد مرتبه از کونیا بدتر هستن
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71059" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71058">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71058" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71057">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWSOD8J9gge-A-Hymg7zoSDRm7YJcP148oT_DyWC1OuU5RDM1zAUtQolPDmdZjtKUNrnE5tfTHTFo35sqBGqlJBJK3r9GVkn774r1NvcccOHvl6PgSwZbiWhNk91xno0DJBQdkKGTsQT67Ii6_xEdaqHs3hGcEvzS4N2A7yOEkQlhOaYDdDeeT9fpIQHL-0gThpJCfvBSFmQSt7o_cVvgd_S1JklndqXVdJ8-TU-2QRf3tZrRNe7ebvrP9aG8gqqBSjKRpwlPpaD6oiymbZHAZk5yb5njHnhRqxw0VrvC3GLjWH-ZAYc6TfOYXRoR_ea5OdikxYX6EQyh_pEXVG-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71057" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71055">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSc4Z4q7718yg1Kw7s2mZnDgCiXER_M9KjVSXR2ppNrR4kR2oj5XrG1fLTYT5fQclan9l3UEDfFwoKUN6KbBwBUwjrXxGggyFUEB6CkmfQ_ClygP0bjgcwu7IMz5aMYFkM8LxbNc9dQ61xaJADTnjt1-M_Wq1MkXt4l-RqlYIJ1wg4Z3RjtyEKMFug1gbq0i_imqS4nEJymESL74BEl80oTFZNawrwYMrj5JkePsYw4srgdQlfaHk7k5n7EPBTX3rqOfgoWfxwvknGYvp1yYgZAQr_IpCx9pp1tiAx2F86I4XPznZ1-_f-dcjH9P2opRbR10ANUI6gBVD4UfmfusVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
🙂
پست جدید تلگرام در پلتفرم ایکس:
حس و حال بامزه‌ای دارم، شاید بعداً عکس‌های نودم رو منتشر کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71055" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71054">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_f526ww5iq2iSbVzFao6VrCt1q7AiX5y8Rd_gktGzq47M6z2uYME9-HG1-Xb1RIfe4cVb19mcSPmKH9Zzfwbi_CESsrh1BPeicpm_ClYELjUYTFe8N6UBSVnJGErNGFN-nJyURnuNqo0L8o7o31dIdyrnkTlYxzk1JSkWNH1vjCUOxUyNheSL0JvRwM-u5pmyg1Z69pFYDRq5AS6xuL5KjoYTrtPHV5aLhq9DSB-KnD9R3B4rNC0ufeltu37Tny6oHaMzC0xPtW3kMlAnHOhLOYHJpvC79ikCHX139iziZGALYfYp6G6dGXFSDCVe86KP3RLqk178spIN4mKMX_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جمهوری اسلامی کشته شدن سه خلبان نظامی در حملات آمریکا در دو شب گذشته را تأیید کرد.
اسامی: مجتبی باقری و حامد اوکاتی (خلبانان هوانیروز/هواپیمایی نیروی دریایی) و حسین مهدویان (خلبان نیروی هوایی).
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71054" target="_blank">📅 16:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71053">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=Htx1A80X7AsZxa5wtV3GIr3j_iRKyuJC6UyMZ18k3CpswxskyFjC5adLABB_gzfUy98lKS1XvUh2NLWAuSlcHUKWKsQgGKjJHNSKFrMIY_B6OPoc8ch2b-Widqt6HlQMirA6r7rYbTTplJ08y08YvaHPraM3lO35G4agkIBwo9mAelXa5RZfHyU1KWYcHBUTlo14WI-3HDotrKltWMqXW0CqgiU8xMrbPMHjVnNYpknIisBxsyGgySb5pbQlpdXflwvfDWr4H2H4ynyHSSnnp_WP7JlvU2LdsZkkfNMCBMJTTnm80phEpj-k11FFdVmORXK9y9KIs_BO7Opq2UF7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=Htx1A80X7AsZxa5wtV3GIr3j_iRKyuJC6UyMZ18k3CpswxskyFjC5adLABB_gzfUy98lKS1XvUh2NLWAuSlcHUKWKsQgGKjJHNSKFrMIY_B6OPoc8ch2b-Widqt6HlQMirA6r7rYbTTplJ08y08YvaHPraM3lO35G4agkIBwo9mAelXa5RZfHyU1KWYcHBUTlo14WI-3HDotrKltWMqXW0CqgiU8xMrbPMHjVnNYpknIisBxsyGgySb5pbQlpdXflwvfDWr4H2H4ynyHSSnnp_WP7JlvU2LdsZkkfNMCBMJTTnm80phEpj-k11FFdVmORXK9y9KIs_BO7Opq2UF7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو ایتا و روبیکا با انتشار این فیلم نوشتن سامانه پدافند لیزری جدید اومده و همه موشکا و پهپادای آمریکا رو با لیزر زده.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71053" target="_blank">📅 16:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=V_zEx3t502k9xVOOSuj2GWNnE3fjOifl3TBNW5D2AZL7r3poefNesn0kga4MRfcOqfKJTosGoQhe8TKS4NaeheoUxUE0-dYAV2ZlNOvX-p7J9m13FTt8GUpx4BNa3dverd1jdjnwAJQ5fuUQt7QzA8eCYL52FOcvD-mph7AnIx7xFi7YHRcRn9glihxQLgYIayxpeijKjB86HiR3w3H87pqtia95g1-KtcgYcRhVySVUKrJGpCwTjYz206sitly2RvoA0oX5bLnjJ4UUv57Q9S2XPCdzUySt0fZVGF7v2L2J-wc-s51PF0IeNol8mdUtO0JqS0pRq8dr2SCwmU2LQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=V_zEx3t502k9xVOOSuj2GWNnE3fjOifl3TBNW5D2AZL7r3poefNesn0kga4MRfcOqfKJTosGoQhe8TKS4NaeheoUxUE0-dYAV2ZlNOvX-p7J9m13FTt8GUpx4BNa3dverd1jdjnwAJQ5fuUQt7QzA8eCYL52FOcvD-mph7AnIx7xFi7YHRcRn9glihxQLgYIayxpeijKjB86HiR3w3H87pqtia95g1-KtcgYcRhVySVUKrJGpCwTjYz206sitly2RvoA0oX5bLnjJ4UUv57Q9S2XPCdzUySt0fZVGF7v2L2J-wc-s51PF0IeNol8mdUtO0JqS0pRq8dr2SCwmU2LQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ از یه دختره که سر سفره عقد، آقای داماد رو سورپرایز کرد و گفت من مهریه نمی‌خوام و فقط 14 شاخه گل بنویسید
؛
هیچی دیگه پسره دیروز طلاقش داد و اونم با 14 شاخه گل رز طبیعی قرمز  یک جلد قرآن برگشت خونه باباش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71051" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01429c982d.mp4?token=t6MgLx7837Qsu3LrYFktbZRkdHvRXiWIg9KJJmKhWt6IDmgdoIWYhU9WE2vXtjosJJz_uYcTfqraWY3D1eO3jOJSo7fmu6tRzO_TeGBNmYQVshRgi8k-5ngfcbWAD3OXpV116frkx11lu1LY_M0YnhAawVTH_h70d5grkse5ymT7KLLYuLvtYmme38oZzrfCXZY4tw7mjW4k4f5d4pHEfN3GIrtE3TTF4SZ_0_rK4p69axJqWCIhHYygvnLTwfdc-AXSbX0rDPYQsRbkxnzV3_iEqLcpmkqQK8QgDXtzWBAHVKBnjbD5sHf4EMSUt2akgDhGITREoRjJwqM8seV4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01429c982d.mp4?token=t6MgLx7837Qsu3LrYFktbZRkdHvRXiWIg9KJJmKhWt6IDmgdoIWYhU9WE2vXtjosJJz_uYcTfqraWY3D1eO3jOJSo7fmu6tRzO_TeGBNmYQVshRgi8k-5ngfcbWAD3OXpV116frkx11lu1LY_M0YnhAawVTH_h70d5grkse5ymT7KLLYuLvtYmme38oZzrfCXZY4tw7mjW4k4f5d4pHEfN3GIrtE3TTF4SZ_0_rK4p69axJqWCIhHYygvnLTwfdc-AXSbX0rDPYQsRbkxnzV3_iEqLcpmkqQK8QgDXtzWBAHVKBnjbD5sHf4EMSUt2akgDhGITREoRjJwqM8seV4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز، اولین ایونت مد و فشن توی تبریز برگزار شد و حسابی غوغا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71049" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=d_hSHx4fz9GUFpLoxIS2moGdT5sfCCA5ICwrvcG3sVOLvflgRH3z-m2DF-g_nXVKCYoen6EaUd9kXVaQxzIMftFMu7Rs40nXMF1mIfn_hCGA-2uj-5DPqqNKDejvL2fR9unbJqivpPHAIIeDUt3BdkTOfYcfAAMJ2bzxqkXuAVMih0ep-Q8kM5Df1DcIjDv1T4S2_3yEKkrRW6h1a3wNEivRrXq-7RptoA2EjwhhUjU8HQW3MfWel_HvpK7OrV99ctERp-4T9N-l8RLcc_RI2GpFOXu3zJAQMF4YaJFMgYrdSdx7wKpceBga7Vi8zsoAzCmOlzpqaMsFelv5GpAJiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=d_hSHx4fz9GUFpLoxIS2moGdT5sfCCA5ICwrvcG3sVOLvflgRH3z-m2DF-g_nXVKCYoen6EaUd9kXVaQxzIMftFMu7Rs40nXMF1mIfn_hCGA-2uj-5DPqqNKDejvL2fR9unbJqivpPHAIIeDUt3BdkTOfYcfAAMJ2bzxqkXuAVMih0ep-Q8kM5Df1DcIjDv1T4S2_3yEKkrRW6h1a3wNEivRrXq-7RptoA2EjwhhUjU8HQW3MfWel_HvpK7OrV99ctERp-4T9N-l8RLcc_RI2GpFOXu3zJAQMF4YaJFMgYrdSdx7wKpceBga7Vi8zsoAzCmOlzpqaMsFelv5GpAJiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ در مورد پسرای زیر ۳۵ سال که موهاشون سفید شده، در حال وایرال شدنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71048" target="_blank">📅 15:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK8jPnd21VGkWv9HToIAOUiZizKDndtxTLOz9MTZoa3OWnOeC3UsLOptuf3yw-8WLK5HlywanqHqCCAlwn_07YJ8JdYmmG0ffs3TMZ9o9BuPmSJSpEzCbtrc7TiLz0mrSYgGLvXkhOxAeQcs11HZ5KPJcU7j1_Q_J8aC_LMnmGFzeRKPpMWMA_rgcr5hGuHLgCBTc1Qu_qnuHDjFoP7cCJh1vX7PICmafSSJJ3d7zzUMkeJYmHKO4EE9kIIUL3MjmstEe4zCO36g1-ClMc55Pn-rlakf-8Tq4T62K7T343tBEt5k67Bw15XVyMPEGBgJ4ur-eA-QQ5Ge1QvT5o8O2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خبرگزاری میزان وابسته به قوه قضاییه، روز پنجشنبه ۱۲ شهریور ماه اعلام کرد حکم پرونده صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، در دیوان عالی کشور تایید شده و او به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری، مصادره کلیه اموال منقول و غیرمنقول و محرومیت از اشتغال به شغل کافه‌داری محکوم شده است.
مرکز رسانه قوه قضاییه این پرونده را مرتبط با اعتراضات سراسری ۱۸ و ۱۹ دی سال گذشته دانسته و مدعی شده است که متهم در «تحریک اعتراضات و ورود خسارت به اماکن و اموال عمومی در استان قم» نقش داشته است.
صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، کارآفرین و نیکوکار ایرانی است. محمدعلی و صادق ساعدی‌نیا در جریان انقلاب ملی ایرانیان در دی ماه گذشته دستگیر و اموال هزاران میلیاردی آنان مصادره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71047" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:  اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت. ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71046" target="_blank">📅 13:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=fxoxXNsabstYlG15a48kW42aFANM70ZlZPaDNFgwLEbZlUN5vL1OQN7RCqwFcEB3VErqPYsdjRxjfGAZsLKdIi-ealkGwF2KwxglsKcDcxs62g_q3AvJuRHTNwogpr4Cr2llhFhI-4EMaE_HPBIhMjt-fHwgnbqjSbVB9DOkX6rdZ1lIM_IzxsEBOiE_MFxd79B2Yz7hSVlJsY9SaS7csvI54CDLYursPHGRmVNpJn9MmVDRG2qwjKNCtTH405693nTAHava4h1MTjqzGOVN8Viktb1k0X11U_4cfgGiPs3jU5mhKgEF3wNQUCTCj7qI0EuX7HRr8OYPXDiUPQLetg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=fxoxXNsabstYlG15a48kW42aFANM70ZlZPaDNFgwLEbZlUN5vL1OQN7RCqwFcEB3VErqPYsdjRxjfGAZsLKdIi-ealkGwF2KwxglsKcDcxs62g_q3AvJuRHTNwogpr4Cr2llhFhI-4EMaE_HPBIhMjt-fHwgnbqjSbVB9DOkX6rdZ1lIM_IzxsEBOiE_MFxd79B2Yz7hSVlJsY9SaS7csvI54CDLYursPHGRmVNpJn9MmVDRG2qwjKNCtTH405693nTAHava4h1MTjqzGOVN8Viktb1k0X11U_4cfgGiPs3jU5mhKgEF3wNQUCTCj7qI0EuX7HRr8OYPXDiUPQLetg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت.
ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران را به اعماق دوران حجر و تاریکی بازخواهیم گرداند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71045" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=BvNDXMlt6SQNYPRnqARfvj74WgJsOzHGYSWceQt0G8wM4YQ55Lh3edH1UPEECjTq2ko5P4EJ-X-q37rYr_anGEjzyIBSdbC6YMlaZnSV1JCNw23W3yqKlbXLiDrlJlzvUez692695qfgllxR8IqeBqQV33qoXuE1l8lKe7KCv4M-5OeQSkrJUNQofDC5MNWVqnrwF2JMTiIPB74itdrAKug_4IYrkiQpitbsxNR01WfLxft3eXhc5NyKgoGnqK1-3aE9z1dG40IBtUIajB_UV_XoNk3sF4ERfzXJUFMo3GB4GzafXSUORyAj521VhS3-yiAPGaZhgN9zvlq_1cdf7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=BvNDXMlt6SQNYPRnqARfvj74WgJsOzHGYSWceQt0G8wM4YQ55Lh3edH1UPEECjTq2ko5P4EJ-X-q37rYr_anGEjzyIBSdbC6YMlaZnSV1JCNw23W3yqKlbXLiDrlJlzvUez692695qfgllxR8IqeBqQV33qoXuE1l8lKe7KCv4M-5OeQSkrJUNQofDC5MNWVqnrwF2JMTiIPB74itdrAKug_4IYrkiQpitbsxNR01WfLxft3eXhc5NyKgoGnqK1-3aE9z1dG40IBtUIajB_UV_XoNk3sF4ERfzXJUFMo3GB4GzafXSUORyAj521VhS3-yiAPGaZhgN9zvlq_1cdf7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
جنگنده میگ-۲۹ام‌یو۱ اوکراینی یک موشک اس۸۰۰۰ «باندرول» روسی را در ارتفاع پایین با یک موشک آر-۶۰ منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71044" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=mxfDgpRDjbsEBIXsyl1zPrm_Zoqv7JWnlx_xvzgv1XV336ZTJ0J9meENXmi6IG4-ytn_JQUGeoLEKP3-9A9o0kMO9GyVBVxqzU9WLtJZCfI5ee7RGHguzg5GHLG2Dnni3eNK39SZJJMwRI8fVaqtphYq6AY8rAkozT3WdOL3PRsUYpNcrKNjND6a8ICb3abNqAwJRjVPJGf2ykr-JdrXtfPttbWe9Njml_YV_k-Bjo08issAXdEuBXGz5BxB1vPq1IeE8MJvIB6j6N1H_EiS-S38KdcPpjeKoj28cf0tyRW2lSD6nuQdzkEXjHFKbhs7hElUY4H2bPjDZ9XOVfLtWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=mxfDgpRDjbsEBIXsyl1zPrm_Zoqv7JWnlx_xvzgv1XV336ZTJ0J9meENXmi6IG4-ytn_JQUGeoLEKP3-9A9o0kMO9GyVBVxqzU9WLtJZCfI5ee7RGHguzg5GHLG2Dnni3eNK39SZJJMwRI8fVaqtphYq6AY8rAkozT3WdOL3PRsUYpNcrKNjND6a8ICb3abNqAwJRjVPJGf2ykr-JdrXtfPttbWe9Njml_YV_k-Bjo08issAXdEuBXGz5BxB1vPq1IeE8MJvIB6j6N1H_EiS-S38KdcPpjeKoj28cf0tyRW2lSD6nuQdzkEXjHFKbhs7hElUY4H2bPjDZ9XOVfLtWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
روابط عمومی ارتش:
در ادامه سلسله عملیات‌های صاعقه و در مرحله سی و یکم،  در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش جمهوری اسلامی ایران، «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمد الجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71043" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71042" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgY7L1xnNgrXnwokp-4ApVgCC58SgBUKlTcMtRATl8YMqq39Jx3xrGD0JuyxXitRVeIPVVWakwo0ZiwQ8whAEFFvalGlNAS_mDP72ZeT2o00bKmKaMv-qjteaZK5YBPwWF3jlBUf9TDV27x27SvHqCzmQQfB2TFUB0rtF7Pt5YSrztES247ox_3Y9l4EIh0x4u0mNAcKUesUrG6QBPI48IK_JNny1hSaaSPqj6vIw9mP0SsVf5zl_d3uCrocjBRSFGU-PHlgZDZUGdgAXljkWEiRvAzGZDV7BbSdsoD9a0PkDsNElb7k4kw6cLA0ulLvpccpB3-9G1kdydhMhMnPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71041" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=YyotY7L0M2tCr4J48tNzzE2vMYF-RQYqItr4Fy5fRMPUkowcZ0xrF1HOL7WCZyBjYxPk0vMYBjqHK-SsY7ClBrjUTAfM-GMJce59iReLXX8OnBE_4rpUomNdg5ivONgN8c9zixrrujQ4GIhpmQuplsfArl-GG_Ey72S-bO5J0YXt-OEdXY1cHcnMrV5JL97Cn7By6mPiZK7YjX3qbplC1oFA3qw9hNWChcoLW9ARYm1BOuAlDmQk9EQCeIgIaBZUYtffTPlMe-2Vrk4ErN6wMXW2xD_kDsMaPNjIjSKPEEMy_-SL8s-e-390oMM4ku-CBZPccJDU_zUoilYythtYIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=YyotY7L0M2tCr4J48tNzzE2vMYF-RQYqItr4Fy5fRMPUkowcZ0xrF1HOL7WCZyBjYxPk0vMYBjqHK-SsY7ClBrjUTAfM-GMJce59iReLXX8OnBE_4rpUomNdg5ivONgN8c9zixrrujQ4GIhpmQuplsfArl-GG_Ey72S-bO5J0YXt-OEdXY1cHcnMrV5JL97Cn7By6mPiZK7YjX3qbplC1oFA3qw9hNWChcoLW9ARYm1BOuAlDmQk9EQCeIgIaBZUYtffTPlMe-2Vrk4ErN6wMXW2xD_kDsMaPNjIjSKPEEMy_-SL8s-e-390oMM4ku-CBZPccJDU_zUoilYythtYIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تو میدون تایمز نیویورکِ آمریکا، یه خانمِ چاقو بدست بعد از اینکه یه مرد و یه زن رو از ناحیه شکم زخمی کرد، بعد از اخطارِ پلیس‌ها به سمتشون حمله‌ور شد و به این شکل بهش شلیک کردن و کشتنش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71040" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=EnYNrWlJxYmg8xYjMPnz9DYGrynPxyHXQrg2VmzzH4cZUGco9dy2ljxuwjcwbWwpO-mXIe64bsPOjdsR2e_Rf0y6MSyCHHwOsCUxX_-tOuxd15NRA3rC9qRvWMgQQ4gv81T8Slxrz2X7PfdixYq_153PN8SvRJyFXYRR_DYMvyJpTmgZLWFFocVhL66Wjc4wctdPdQatzGYE9ZTLBlmp-gtIZ0P3wf7rPbCE2fsVTj_EhJEdmEAg_9MQkY-WmTOfwrBjqZ4A305-nhelY7zER-QjRlpEqx-sbRxT68CFUKQriuxK-fqTMPhJk1Ne-KBoRKI_fxgM5GWASXKU7CsINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=EnYNrWlJxYmg8xYjMPnz9DYGrynPxyHXQrg2VmzzH4cZUGco9dy2ljxuwjcwbWwpO-mXIe64bsPOjdsR2e_Rf0y6MSyCHHwOsCUxX_-tOuxd15NRA3rC9qRvWMgQQ4gv81T8Slxrz2X7PfdixYq_153PN8SvRJyFXYRR_DYMvyJpTmgZLWFFocVhL66Wjc4wctdPdQatzGYE9ZTLBlmp-gtIZ0P3wf7rPbCE2fsVTj_EhJEdmEAg_9MQkY-WmTOfwrBjqZ4A305-nhelY7zER-QjRlpEqx-sbRxT68CFUKQriuxK-fqTMPhJk1Ne-KBoRKI_fxgM5GWASXKU7CsINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سایپا تو ماشینی جدیدی که زده ماشین با اینکه راه نمیره ولی براش کیلومتر حساب میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71039" target="_blank">📅 12:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2qwcm1r9ssq5u5sjifQnsNqzQpSFI3Ik9qyMwijqEIFgpPQp_zgAF7BddhD1GSclwi8TQtzg4ep5s7qFHcBD8PY42ONcaFBF1p8Be425AbFzvissg6hXznPspdT-PhPFIn9eOgvLCpPGBDiEJsSiUpGYTPMY_-lMHwNQnj67CSYXFtXzlH2LNs5Qg9KNGliyjL5wuu_oQqOR8T7pnrNR7OHFU6iMnq6oy2k70nsnKUf12WatP5pvQUMOCiQ2_OM_mmMfOPsw3EN062LHXjM0XkQpVSJKQbsEREaoJ0N5CvfBIVUUohlq1ntahy546NVdaxjBkLa6QXZf0k-XGIg9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس:استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته در ساردینیا با شیخ طحنون بن زاید آل نهیان، مشاور امنیت ملی امارات متحده عربی، درباره ایران دیدار و گفتگو کرد.
این دو مقام درباره گام‌های احتمالی آتی بحث و تبادل نظر کردند؛ چرا که دولت ترامپ در پی بازگشایی تنگه هرمز و هم‌زمان افزایش فشار اقتصادی بر تهران است.
امارات نقش کلیدی در تلاش‌های تحت رهبری آمریکا برای عبور نفت‌کش‌ها از این تنگه ایفا کرده و در راهبرد تحریمی واشنگتن، کشوری مهم محسوب می‌شود.
مقامات اماراتی به دولت آمریکا اعلام کرده‌اند که هرگونه کارزار مؤثر فشار اقتصادی باید شامل تمامی کشورهای عمده‌ای باشد که همچنان به تجارت با ایران ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71038" target="_blank">📅 11:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71037">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به بندر سوچی در روسیه حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71037" target="_blank">📅 10:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77017317.mp4?token=A0rf5xo2pMB6Skh1qTJn3vr_tsOzpHa9nJhP23g9778hGzo3pXHieGwjOMEn29Zw6gff09YHUGYR9flYRExShAz_errw3djVEqrbNBjmh91DPfJLD2aPyCOwraODs-Vt00Dy1o0_HmHKadkInDdLemqgCHyuaUh21gdTgpkiAF7_bT-SwwJK024Fa1rFDRC2oAjdPSf_nMs-sQP3GIx57k3968tUfk8vDjLcszN70Y6mbrpQ79RQrm00J1KWfHbPk0G0wX_E4_YkV8H2g-TV_KivOtiGPWpMhKWAYN5RUsZQc1juXQe8o7VcdsRsQSKfxXOGCJxxdbFkgGPJLbCrVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77017317.mp4?token=A0rf5xo2pMB6Skh1qTJn3vr_tsOzpHa9nJhP23g9778hGzo3pXHieGwjOMEn29Zw6gff09YHUGYR9flYRExShAz_errw3djVEqrbNBjmh91DPfJLD2aPyCOwraODs-Vt00Dy1o0_HmHKadkInDdLemqgCHyuaUh21gdTgpkiAF7_bT-SwwJK024Fa1rFDRC2oAjdPSf_nMs-sQP3GIx57k3968tUfk8vDjLcszN70Y6mbrpQ79RQrm00J1KWfHbPk0G0wX_E4_YkV8H2g-TV_KivOtiGPWpMhKWAYN5RUsZQc1juXQe8o7VcdsRsQSKfxXOGCJxxdbFkgGPJLbCrVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی وایرال شده از پسری که چالش گرفت که تو خیابونای شهر از مردم درخواست پول کنه(نفری ۱۰۰تومن) و اکثرا قبول کردن و در آخر هم پولی که جمع شد رو رفت به نیازمندا کمک کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71036" target="_blank">📅 10:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71035">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=sCS9iWCyXxAGJeqO_eJVAlwCg9O4Obrcf9D-gT6ZL3IatowUmC3Ngm8OTg_ew1d6YUoXvrlxHj-BNI07X9R7MgTebNS4o9PLUCS6HkeAwqqouB_FGy4yXadJaDYZb4VDlrYKUF4slwto3GEwUo1ZtNu1X5ujFAK3NpEl4rMUVe4wcnHzaCzVTD5GqPiH1FWn8FfjomhiAwO5AMGDGwJM532aOQBRx0SAygQmP8G1nuUHNV-U2TWMnvpgpYXGrnfP-pYGBVqNYkHlpcvSK_80GcF1IN3_lxGpLO3nTZX3mT_lQ83JjJgTKQW0-VKcrJ8b72f_bvtnH1sqM208PHKouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=sCS9iWCyXxAGJeqO_eJVAlwCg9O4Obrcf9D-gT6ZL3IatowUmC3Ngm8OTg_ew1d6YUoXvrlxHj-BNI07X9R7MgTebNS4o9PLUCS6HkeAwqqouB_FGy4yXadJaDYZb4VDlrYKUF4slwto3GEwUo1ZtNu1X5ujFAK3NpEl4rMUVe4wcnHzaCzVTD5GqPiH1FWn8FfjomhiAwO5AMGDGwJM532aOQBRx0SAygQmP8G1nuUHNV-U2TWMnvpgpYXGrnfP-pYGBVqNYkHlpcvSK_80GcF1IN3_lxGpLO3nTZX3mT_lQ83JjJgTKQW0-VKcrJ8b72f_bvtnH1sqM208PHKouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ویدئو جدید از پرواز هواپیمای HC-130 Combat King II آمریکا در ارتفاع پایین در عمق کشور به دنبال خلبان آمریکایی جنگنده F-15E
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71035" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71034">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=HGZ4EQnidUa-IPRaosj18KkrQmR0RwwGDdK8k2o6A7-OMjbRypiXVdVwtZsEB6oA-LLlUgaRyy07oDqstfqkKimdt_FqlJd2lDXXjliNQ7_4szxVk8jDWvnaH2XueuPkTRjLeSPqVZF_QgQGinkGlLjm8rJA6OQ5WgRX24fTmOtwQAdnhuLENmfp3nnJG-Kz7on2RCQ65k765G6gPgJCrt5k88ttguz_KXjT-U_QmK_as6IkZuLXq9iVaQ27Laut9QSoHREkv3QQOgC-MhLXB3sjCcMXLler1OmxjD9za8NmFbf9vhdyz2jQc5z5umCsnouWs3riAs7HKXK5tfyiVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=HGZ4EQnidUa-IPRaosj18KkrQmR0RwwGDdK8k2o6A7-OMjbRypiXVdVwtZsEB6oA-LLlUgaRyy07oDqstfqkKimdt_FqlJd2lDXXjliNQ7_4szxVk8jDWvnaH2XueuPkTRjLeSPqVZF_QgQGinkGlLjm8rJA6OQ5WgRX24fTmOtwQAdnhuLENmfp3nnJG-Kz7on2RCQ65k765G6gPgJCrt5k88ttguz_KXjT-U_QmK_as6IkZuLXq9iVaQ27Laut9QSoHREkv3QQOgC-MhLXB3sjCcMXLler1OmxjD9za8NmFbf9vhdyz2jQc5z5umCsnouWs3riAs7HKXK5tfyiVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71034" target="_blank">📅 09:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71033">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=MX7Bc0S-LybSu5ey1II6YbM3s0IEewCPfO3qbVxOElRzh0ksPCWDZ6qsBtdTmQd6KsB5OwAyHxCqkKmRN5tmIGaKZIyrIiV5CtMbosReLN5iFa_MzUAfK-T5kY1_fDXSlmPAKJOFatpfaq5g93Ty5I9CZlFnyNf0ivKXHAOPv_XG2fURrcepdEBiIyvWW2nNWIHZatfFnQLYG5tsBxlTLYZf7MIl_HVdJiDz05doRW_0nmaVlzGt5h6Tk9t3_Ap8eDVEQZ-8QU2tczfPLUGBjRPP9nupI8_aPgrXPN1cZUMPTjkRBc6f1SF0-PUGwrXBe3jkofX2MjnzTexNYKfZGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=MX7Bc0S-LybSu5ey1II6YbM3s0IEewCPfO3qbVxOElRzh0ksPCWDZ6qsBtdTmQd6KsB5OwAyHxCqkKmRN5tmIGaKZIyrIiV5CtMbosReLN5iFa_MzUAfK-T5kY1_fDXSlmPAKJOFatpfaq5g93Ty5I9CZlFnyNf0ivKXHAOPv_XG2fURrcepdEBiIyvWW2nNWIHZatfFnQLYG5tsBxlTLYZf7MIl_HVdJiDz05doRW_0nmaVlzGt5h6Tk9t3_Ap8eDVEQZ-8QU2tczfPLUGBjRPP9nupI8_aPgrXPN1cZUMPTjkRBc6f1SF0-PUGwrXBe3jkofX2MjnzTexNYKfZGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح عباس حیدرزاده مداح درباره‌ی وضعیت مجتبی خامنه‌ای :
تولیت آستان قدس رضوی گفت که شب دفن رهبر؛ مجتبی خامنه ای ساعت ۱۲ شب اومد حرم برای دفن پدرش و تا ۷ صبح اونجا بوده.
وضعیت جسمانی ایشون هم عالیه، هم از لحاظ ظاهری و هم از لحاظ جسمی؛ حتی مسئولین هم پشت سر ایشون نماز خوندن.
همچنین ایشون نیم ساعت کنار قبر پدرش دو زانو نشسته بودن و گریه میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71033" target="_blank">📅 09:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71032">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71032" target="_blank">📅 01:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71031">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bykYG7sgZ-zfMVtAqeTawTOM2xsrNXZDftNzs2fApJLN_sgjlBgvCtM1Uw-2PR09NyZ2z6hBYK-PTfc7GhqOHyXg7KsEpfhtOkujL7xWMQHWE1a1_6CbIaAs8ysaS_3FA07timABbaDsbi0uKypRKc1Or4HEc0rDNb3AeqAb9PdFpsFsrayVPt6cgxTPaZNlAoQSL7t-YMJaZ-6BJluviLRq0w1kdsPnnKZvaFHsrGm8uYU6DqkJyEyIaTlc3UWTkwRGItQZAMKXTBViJ15DwDW7thE2nVHvvDEz41bNUIhHV29Fbhms467R5xXFfkwBVWCQOa2nJFgw2yVhTXANLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71031" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71030">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71030" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71029">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=Tjw2dEPSoEe3HMV2a8SfeU-unKxQABNV1BE3B5_Eee_VbQXLBoVqiQdwKveilexWuZG7na5XKJ3_tP-fE9A2J8NCQqrFpdOBh-3QcgkqA6npX-rQZpOlQrWbqtyzOi1q2B_hHNxka4v2eb5srmJDh3Ptl_nSHh8ydMAcUoJM86sYJ1GPUDnRj5ZqGA9vuOKWvThZQgdc-DWOLXOowGlxV2N-SoZLk0dRjjKGDzmlrMzPTQgbnQ1uPASkrdLBqeuLgHcl9g9vyTr6qIB4Xegj28wXECeL0LwneMoafAJhxpuDMeC8KcQ4M4NkLgFRtLFwYHiqeKzhZnj0PrOIOxkhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=Tjw2dEPSoEe3HMV2a8SfeU-unKxQABNV1BE3B5_Eee_VbQXLBoVqiQdwKveilexWuZG7na5XKJ3_tP-fE9A2J8NCQqrFpdOBh-3QcgkqA6npX-rQZpOlQrWbqtyzOi1q2B_hHNxka4v2eb5srmJDh3Ptl_nSHh8ydMAcUoJM86sYJ1GPUDnRj5ZqGA9vuOKWvThZQgdc-DWOLXOowGlxV2N-SoZLk0dRjjKGDzmlrMzPTQgbnQ1uPASkrdLBqeuLgHcl9g9vyTr6qIB4Xegj28wXECeL0LwneMoafAJhxpuDMeC8KcQ4M4NkLgFRtLFwYHiqeKzhZnj0PrOIOxkhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇹🇭
ناو آبراهام لینکلن تو پاتایا - تایلند پهلو گرفت و ملوانان و اعضای این ناو برای یه استراحت  کوتاه مدت پیاده شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71029" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=ohjkF1BovsEfHDPZBCYtlJlehbjHzptkFEE7oFtpwDSW7K7DA2-fIJDz7dHOFLySkVR2A8filpFeSKC8eKovkVbfIBV3WPZuVfNV_cUFylyoRaZ4XDhHtk7ts690fj3eS6_W7uLDdD0QfcQajKiFDsplUnicjdHDqEJ8vHgrnpgzmAuN-J5-l7Z8VkOgPH5S1R6m4UR-PhN7IveCtPeJTt7z8HJFQgTeaSRPTEdECGVXDE5v-BxP0bGiYLqyLzPhXn3NiimP1yck4gp8fiRIBv-eCYMmUO_NAPJ5-Q7dq_sh95So9KSkvVMo8zOKIaoBQRClyUXQogQ74LKPZijA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=ohjkF1BovsEfHDPZBCYtlJlehbjHzptkFEE7oFtpwDSW7K7DA2-fIJDz7dHOFLySkVR2A8filpFeSKC8eKovkVbfIBV3WPZuVfNV_cUFylyoRaZ4XDhHtk7ts690fj3eS6_W7uLDdD0QfcQajKiFDsplUnicjdHDqEJ8vHgrnpgzmAuN-J5-l7Z8VkOgPH5S1R6m4UR-PhN7IveCtPeJTt7z8HJFQgTeaSRPTEdECGVXDE5v-BxP0bGiYLqyLzPhXn3NiimP1yck4gp8fiRIBv-eCYMmUO_NAPJ5-Q7dq_sh95So9KSkvVMo8zOKIaoBQRClyUXQogQ74LKPZijA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
ملت ما با قدرت جلوشون ایستاد و اگه بخوان این مسیر رو ادامه بدن، بازم با قدرت مقابلشون می‌ایسته.
ما تو اون تفاهم‌نامه چیزی بیشتر از حقوق کشورمون نخواستیم و الان هم فقط دنبال همون حقوق هستیم.
ما همچنان به تفاهم‌نامه‌ای که امضا کردیم پایبندیم. اگه آمریکا هم به همون تفاهم‌نامه برگرده، ما هم طبق همون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71027">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=cnieOy1TU7_7Ce0mhF0iEzfOZW0Pc-p5QofaQ-1SB2ZVmeL6r1rtUgp5gX_tpri_SeJ6BFY7a25ZMJBOY-CKZNJQp7U6Gt9rNeIE_Klsn13tqooToNVV5cZfu_LS6mk5OafwTPpfc8TpTGmmG_SzTkXRXk_5SOCDdVVm5lRx8udRcBUzgdesRssvc-0WtarVgTv5yjXBHwZypI5VEm2DWoByDJdgEEzMxBLHw1a6j3012qzUJjyrItsG1FI7yInYCIiFDoLLiJYFYZIRY5M2uQ51JY59r_utqmerC8DDAvmX2n1F25-j2hHU5ixCBZwahMRTY6bTmjXi4DT3bFBaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180c2bccea.mp4?token=cnieOy1TU7_7Ce0mhF0iEzfOZW0Pc-p5QofaQ-1SB2ZVmeL6r1rtUgp5gX_tpri_SeJ6BFY7a25ZMJBOY-CKZNJQp7U6Gt9rNeIE_Klsn13tqooToNVV5cZfu_LS6mk5OafwTPpfc8TpTGmmG_SzTkXRXk_5SOCDdVVm5lRx8udRcBUzgdesRssvc-0WtarVgTv5yjXBHwZypI5VEm2DWoByDJdgEEzMxBLHw1a6j3012qzUJjyrItsG1FI7yInYCIiFDoLLiJYFYZIRY5M2uQ51JY59r_utqmerC8DDAvmX2n1F25-j2hHU5ixCBZwahMRTY6bTmjXi4DT3bFBaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره انتخابات:
من تحت تأثیر انتخابات نیستم. خودم نامزد انتخابات نیستم؛ حزب من در انتخابات حضور دارد.
به گمانم حزبم به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71027" target="_blank">📅 22:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71026">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=R6_KwVx3lZQ_4bVwK_D68u0HU2OYZpMTcdKBgXohYAGLfe9TpGOiE8ZRpU9K6Rad8bQJ5UTNg7yHW7JMEFmGPyE2EmnkuZbnx1VOzkiWOXISJRNSsWXWVSLO1xAXlVZwkSoMhER4S_9FkHoLNCK2KoCafTuWMIMSi8BO6OC9AR4O3-9uw81GZg5x1jP8iWEmhu4FeN3uz0qGyfkmn_HaZ82edcN7fxIkBXlW8EeC7bCxOw6Pl2baSmkWIY3UhcyYJ3XSqEMM9g4LPA892xGH9rPx09dEAXOdxElSO81BjEHZMEM920CSTyfTdMtCt2D7tNWAPvXy2HnRuBtbd6Hiew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f1ce3ca7.mp4?token=R6_KwVx3lZQ_4bVwK_D68u0HU2OYZpMTcdKBgXohYAGLfe9TpGOiE8ZRpU9K6Rad8bQJ5UTNg7yHW7JMEFmGPyE2EmnkuZbnx1VOzkiWOXISJRNSsWXWVSLO1xAXlVZwkSoMhER4S_9FkHoLNCK2KoCafTuWMIMSi8BO6OC9AR4O3-9uw81GZg5x1jP8iWEmhu4FeN3uz0qGyfkmn_HaZ82edcN7fxIkBXlW8EeC7bCxOw6Pl2baSmkWIY3UhcyYJ3XSqEMM9g4LPA892xGH9rPx09dEAXOdxElSO81BjEHZMEM920CSTyfTdMtCt2D7tNWAPvXy2HnRuBtbd6Hiew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
دیشب حمله بسیار سنگینی صورت گرفت و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71026" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=NTVAZ3fYx-6yuaeoMOWJYcz_jlgzZQrQ5_JFzHuztfDB2nJ-8DZ3hdQ8CsdTHK5n_ktIe3SPttD1UX6yh_HdM-0Ip6nXHw_YXRuCrhSOMqklcrs2Gvc3lPMOdaRlaLaKovmmVdVV4yw5io_VhFHlcVPX76kty5cxuDc16OePZI7XDLzc4KzAl5iFGr9ccMKM17ylx6DeiuXfx12iuoH_5pVTAohGgM0dPDy_osxQEeNkfXT6o59BVgGNN578Puw1ELQtEIFzv4LvzME460xJbcnoyUXogE5_z8Dvi7XhYwxRvWe_SWbrL3uEB30nTsJ2oNEvzVvuc8xk-Dd5YZVdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a230c24bdf.mp4?token=NTVAZ3fYx-6yuaeoMOWJYcz_jlgzZQrQ5_JFzHuztfDB2nJ-8DZ3hdQ8CsdTHK5n_ktIe3SPttD1UX6yh_HdM-0Ip6nXHw_YXRuCrhSOMqklcrs2Gvc3lPMOdaRlaLaKovmmVdVV4yw5io_VhFHlcVPX76kty5cxuDc16OePZI7XDLzc4KzAl5iFGr9ccMKM17ylx6DeiuXfx12iuoH_5pVTAohGgM0dPDy_osxQEeNkfXT6o59BVgGNN578Puw1ELQtEIFzv4LvzME460xJbcnoyUXogE5_z8Dvi7XhYwxRvWe_SWbrL3uEB30nTsJ2oNEvzVvuc8xk-Dd5YZVdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
یک ضربه کوچک بود، اما دیشب ضربه بسیار سختی به آن‌ها زدیم.
ما تمام تجهیزات جدیدی را که سعی داشتند در امتداد تنگه هرمز مستقر کنند، از بین بردیم؛ تجهیزاتی که برخی جنبه تدافعی و برخی جنبه تهاجمی داشتند.
آن‌ها تلاش می‌کردند موقعیت کشتی‌ها را رصد کنند — چون همان‌طور که می‌دانید، قادر به دیدن کشتی‌ها نیستند؛
ما تعداد زیادی از کشتی‌هایشان را نابود کرده‌ایم
آن‌ها نمی‌توانند کشتی‌ها را ببینند چون راداری در اختیار ندارند؛ چرا که ما رادارهایشان را منهدم کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71025" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=ZAdW5JFtQ650RKHlvON0DuQzFK09jjapJyo22EfUgX0zv71wqZiWxp1t3z3l0UH9igzKzqGvYj2JNe89oieGeKBWurIU-V3il4LbrYenF8g_ukOIyVi61mdqEtRsdFk_4CZf6LY_tN3u-0xdHGQmKNEJ7ZWY2jgIUW1LeT8juH4pvd4K_5U-k-MqQJCnJlrkl8NPCgDYZI_KTNQ62tO4lQWkX_koocQde4GwVW5rViAu8gHEtjgR5YqzwniKmN7x-dNXt1glX-Fk033bAm-VIKsw65oagrd0aHy2BHdMtTHmQsZr6TW4xYHxAQIBqHY6DRPh4oSQSexHREkfCteTUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991fb05c67.mp4?token=ZAdW5JFtQ650RKHlvON0DuQzFK09jjapJyo22EfUgX0zv71wqZiWxp1t3z3l0UH9igzKzqGvYj2JNe89oieGeKBWurIU-V3il4LbrYenF8g_ukOIyVi61mdqEtRsdFk_4CZf6LY_tN3u-0xdHGQmKNEJ7ZWY2jgIUW1LeT8juH4pvd4K_5U-k-MqQJCnJlrkl8NPCgDYZI_KTNQ62tO4lQWkX_koocQde4GwVW5rViAu8gHEtjgR5YqzwniKmN7x-dNXt1glX-Fk033bAm-VIKsw65oagrd0aHy2BHdMtTHmQsZr6TW4xYHxAQIBqHY6DRPh4oSQSexHREkfCteTUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ما هر کاری که آن‌ها انجام می‌دهند را می‌بینیم.
آن‌ها حتی نمی‌توانند به دستشویی بروند بدون اینکه ما متوجه شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71024" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71023">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/504db2064f.mp4?token=F-d8SKAGMv0yUC7ZkezN9OaPK8Oj09bRTpRjs-f89ETLzsojzPNwHyLcwjBgUql14UJCDm6GqTPI0ktpqLxrpi7katpovBcauo__9Knf_qwZm72LHbC0FU6jOD3egO_oxGS2uOqsqsRq-qVgmfipuEP8qChbCGotMC3n71CtuuIjtkPU4wc9PQTObAivbni7rmA1uuJnfF2bHZ6R_WKgQ61LiCag4rAKKsGADXKUQl9z4gVrTvaGW0TjUOuyDkuq_o4kIH3rZdAFqUetVTSigq26tZcWlWv9zbzmXsgWX6yIE3LXPPg6Teh3pHgBr8MDRBLVOd7evLq-zoZ5mOiw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/504db2064f.mp4?token=F-d8SKAGMv0yUC7ZkezN9OaPK8Oj09bRTpRjs-f89ETLzsojzPNwHyLcwjBgUql14UJCDm6GqTPI0ktpqLxrpi7katpovBcauo__9Knf_qwZm72LHbC0FU6jOD3egO_oxGS2uOqsqsRq-qVgmfipuEP8qChbCGotMC3n71CtuuIjtkPU4wc9PQTObAivbni7rmA1uuJnfF2bHZ6R_WKgQ61LiCag4rAKKsGADXKUQl9z4gVrTvaGW0TjUOuyDkuq_o4kIH3rZdAFqUetVTSigq26tZcWlWv9zbzmXsgWX6yIE3LXPPg6Teh3pHgBr8MDRBLVOd7evLq-zoZ5mOiw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
بیشتر مردم نمی‌توانند به این شکل آدم‌های خودشان را بکشند.
بیشتر مردم سعی می‌کنند منطقی رفتار کنند، گفتگو می‌کنند و بعد شاید کار به سرنگونی بکشد.
اما در ایران، آن‌ها مردم را می‌کشند.
وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند؛ درست وسط پیشانی‌شان شلیک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71023" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71022">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=ffKTcw6JDDEQ1QpZOBVXNj7gIowsRp5BWQlOsz1UWQW8QEmzREb0pGdZyG0K6c4DtSnYo0pfReVDiwpt30hWM6h8nI3suyYhvL5PCL70cAq6FCf_YXs9hIF7XppqwteSwF7Kxdw6NvRefz3iIk4Pm712A0v67LvWjv5wbF6hYP05T5BMSSPRuf---ZOZkQyhnptpXdUMXIy8vMRELvNyLnTObDw7rVBDZrX6bHHvhZPvMlGPVbM7Lq2T7yShKjQ7sN38I9S7F1wbHGhoAM90chtsmFn-zqsqdkEGDbVpbghWOqsZgkxYveEaqsffCW5IfDpcHFmTaZv1Ivt4ZLeCHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319507bcf.mp4?token=ffKTcw6JDDEQ1QpZOBVXNj7gIowsRp5BWQlOsz1UWQW8QEmzREb0pGdZyG0K6c4DtSnYo0pfReVDiwpt30hWM6h8nI3suyYhvL5PCL70cAq6FCf_YXs9hIF7XppqwteSwF7Kxdw6NvRefz3iIk4Pm712A0v67LvWjv5wbF6hYP05T5BMSSPRuf---ZOZkQyhnptpXdUMXIy8vMRELvNyLnTObDw7rVBDZrX6bHHvhZPvMlGPVbM7Lq2T7yShKjQ7sN38I9S7F1wbHGhoAM90chtsmFn-zqsqdkEGDbVpbghWOqsZgkxYveEaqsffCW5IfDpcHFmTaZv1Ivt4ZLeCHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
تا سه ماه پیش، پنجاه‌ودو هزار نفر از معترضان کشته شده بودند؛ می‌توانید چنین چیزی را تصور کنید؟
و حالا شنیده‌ام که احتمالاً بیست تا بیست‌وپنج هزار نفر دیگر هم به این آمار اضافه شده است؛
یعنی شمار معترضان کشته‌شده به حدود شصت‌وپنج هزار نفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71022" target="_blank">📅 21:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71021">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=aU8UTpmPMEZyuxQCndvEmL7fAd0XYibIBa6wMZ8tSXci2flxyv2MXlELdUGv79mkrD7eYkCKybsTm16tUteeGN1vaYX4brHlUsMW-7ELvJqXNjb6X7uRf3Ro2FRNwgNc24oiGaoaQfaYP2k0QnX1cOXdrrnbMto2Dimy0ra672wf18YskWL7vY8EMIimaAVesszEXsFELVU3PKYPYA0VznOLM9yWU-t6XR3cZ_eiE_Cb5b9RJCO0_Z70wQbELGeo6lSwcE_IJrmdnxCUhcsi4QZ3nQPY1fA9yExhBvm9sQzassK1pAl2cI9wtOLcnzob1Xz5P2kAWybnIaqOPwIVvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e478b4b0.mp4?token=aU8UTpmPMEZyuxQCndvEmL7fAd0XYibIBa6wMZ8tSXci2flxyv2MXlELdUGv79mkrD7eYkCKybsTm16tUteeGN1vaYX4brHlUsMW-7ELvJqXNjb6X7uRf3Ro2FRNwgNc24oiGaoaQfaYP2k0QnX1cOXdrrnbMto2Dimy0ra672wf18YskWL7vY8EMIimaAVesszEXsFELVU3PKYPYA0VznOLM9yWU-t6XR3cZ_eiE_Cb5b9RJCO0_Z70wQbELGeo6lSwcE_IJrmdnxCUhcsi4QZ3nQPY1fA9yExhBvm9sQzassK1pAl2cI9wtOLcnzob1Xz5P2kAWybnIaqOPwIVvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما امروز در «تروث سوشال» (Truth Social) نوشتید: «مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟» خب... اگر... اگر این چیزی است که شما می‌خواهید، آیا سیا (CIA) را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
⏺
🇺🇸
ترامپ:
خب، پیتر، من نمی‌خواهم چنین چیزی به شما بگویم. خیلی دوست دارم این را به شما بگویم، اما... اما گفتنش مناسب نیست.
ولی... منظورم این است که من وضعیت دشوار آن‌ها را درک می‌کنم؛ آن‌ها هدف شلیک گلوله قرار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71021" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71020">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):   گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.   @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71020" target="_blank">📅 21:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71019">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=GrwSy0BW1qIayNiOVFBQUolvlOS2R9yQcUmOWzGwTK_2sWvGr42XKo_gU8_o_XMe945uJ6LsOsU7NSe7lt9icwwDR93-Dt3k3Gyl8-3u6mkCKpO1inTZY8X6u2_fxUctIvyokCQtn_I0VGIYjMrfqfjYXSv7j4o8E5X3Fd-Tlidlsr5aFmFqNtdecSdPgSx4qq129-NxOxX2NPP0scewmNuWDmeoow9rgdOOrwOBVa3JgcTvce_e0vsEVNllNfguwMtSn4EiFOPVoo1m_qFrweTtwaisQzug8SjwERs8hwxdqDX7Wius3zmh_DryVutqmbjc7V36ie5VUETj52dq9p33NEsWfyyZrIMcfz87eRsa6TmxZOWT95JyeiiwZAjzI8-UprhY742bCBkB_6kLrPVt0BJGKccvDo61QTDaUDBuSy2CLHIqY4-xUnTl-kvc6PPvTzHMYe84eoKHXoZmqsriHUWWIA8psyeJ9o-3WsuyuzLBgxs7LTB2T4IHIVJtIjryJVkG6NTFtv-JNzJWZ4rr1TkWrRe9Oxw1I88rIaJHT7Qbu-5qZVYC1zI8oGHfG9FWZuVlSBapjWgY5zRgSTdsjyJtbACsvZeWQqltg6xuV8MW3V6EHj-WQBAZ6UEJFe2GELqnnv7vZuOendq4Zeet4PjklxQJ65dbgB_vXBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edb01b99f.mp4?token=GrwSy0BW1qIayNiOVFBQUolvlOS2R9yQcUmOWzGwTK_2sWvGr42XKo_gU8_o_XMe945uJ6LsOsU7NSe7lt9icwwDR93-Dt3k3Gyl8-3u6mkCKpO1inTZY8X6u2_fxUctIvyokCQtn_I0VGIYjMrfqfjYXSv7j4o8E5X3Fd-Tlidlsr5aFmFqNtdecSdPgSx4qq129-NxOxX2NPP0scewmNuWDmeoow9rgdOOrwOBVa3JgcTvce_e0vsEVNllNfguwMtSn4EiFOPVoo1m_qFrweTtwaisQzug8SjwERs8hwxdqDX7Wius3zmh_DryVutqmbjc7V36ie5VUETj52dq9p33NEsWfyyZrIMcfz87eRsa6TmxZOWT95JyeiiwZAjzI8-UprhY742bCBkB_6kLrPVt0BJGKccvDo61QTDaUDBuSy2CLHIqY4-xUnTl-kvc6PPvTzHMYe84eoKHXoZmqsriHUWWIA8psyeJ9o-3WsuyuzLBgxs7LTB2T4IHIVJtIjryJVkG6NTFtv-JNzJWZ4rr1TkWrRe9Oxw1I88rIaJHT7Qbu-5qZVYC1zI8oGHfG9FWZuVlSBapjWgY5zRgSTdsjyJtbACsvZeWQqltg6xuV8MW3V6EHj-WQBAZ6UEJFe2GELqnnv7vZuOendq4Zeet4PjklxQJ65dbgB_vXBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:ما رژیم ایران را سرنگون خواهیم کرد.
ما این رژیم را شکست خواهیم داد.
🎙
مجری؛
«شکست» چه معنایی دارد؟ آیا سقوط خواهد کرد؟
🇮🇱
نتانیاهو:
سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این رژیم به هر حال در آستانه فروپاشی است.
🎙
مجری:
آیا رئیس موساد، رون گوفمن، برای سرنگونی رژیم ایران تلاش می‌کند؟
🇮🇱
نتانیاهو:
تمام نهادهای ما، تحت هدایت من، برای سرنگونی این رژیم و شکست دادن آن تلاش می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71019" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71018">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=MPPbqwPFWntoJryCKhNAY9HQ9MxN8CY5ce6lFsx655NwH-qRa1imIzqnzmAodfBanB98xRwX0GnVvxPGo2NmU1Nhbt2bLnmopgI_AzvpZNquKKhKty3KSvdwblY8nTtTp1izTBvo_AWhxHCw29eOJXbN_ZEFIxu7CQsZ8LPyi8umdGxgYYmY7uo5g--THDDDCHQY7eXnQy9VUZ5PwS9aLaxuMgU49xznM4ODKkB9EgZBYnzMDj4Tlt3Jl7giIJahe5mDpD6ibpB6Et0kf7_dltbSWbfLvJI74SNm8NsNPkazAjbKo_wb_i-h7ScjsGIdD_kmtKxGtoLg1bCoXgJJXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5723b906.mp4?token=MPPbqwPFWntoJryCKhNAY9HQ9MxN8CY5ce6lFsx655NwH-qRa1imIzqnzmAodfBanB98xRwX0GnVvxPGo2NmU1Nhbt2bLnmopgI_AzvpZNquKKhKty3KSvdwblY8nTtTp1izTBvo_AWhxHCw29eOJXbN_ZEFIxu7CQsZ8LPyi8umdGxgYYmY7uo5g--THDDDCHQY7eXnQy9VUZ5PwS9aLaxuMgU49xznM4ODKkB9EgZBYnzMDj4Tlt3Jl7giIJahe5mDpD6ibpB6Et0kf7_dltbSWbfLvJI74SNm8NsNPkazAjbKo_wb_i-h7ScjsGIdD_kmtKxGtoLg1bCoXgJJXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از دیدار محسن نامجو با مجتبی خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71018" target="_blank">📅 20:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkoTV1EW9RgjRxxNGdF6pUwbGdyUc4ubYsNYq2_5s8zwsH9NYGdKMzxfksl_d60iN6iH12Vy2ohM2qVq1SwmT_GKSZ7JjZfjj8uAGiQ9mSJWqiqOCEBKTpaiTVbRViS1RGpBWVrgwjYOhU5excYgRRufrfnXj-f7gxQR327mUuPgPwht37U4eBGVsjlgSAqE4z4OkReNGbZlEiV-D381wPKH0J1kQ8eXNWiaihlTPm5V1-D5aJYBrcYRJifDdxJ-Um55sp7st4R94JMwbpRSJbk-ADdyIyPOFnXL5pD_T6fzTrCYyKm592EwD6swhIaADNrIu7x1F006dWbOucpf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odRxkiiZQJlWjH6jcSBMalbWAJeFhlirYCGSqpmnwJ8vnwT01samS6Ub-iW19uWiOLfbTDk5UPHhHXLZ5hia4QUNL1v7Qo_lDnnqRa-4h-uKVuKoUuHdFnx8XucuiAVB7s1b8rBc1ZvW9zTXdFuhIsYEhYdndlb_OuGrcEPtUMojAP7C8nK01VDB1c5-232frQqtTavM4yX_k6-IUH7aHdscnQEzbUvRpAXrK1C141kl3yiWYzTa3DCpuweMCM77g6opsFOVes-or3T8sU3Thr22zcY-ewlOMzEkJBOtGBf-hMGlN8-Wm6IZ5wiwbVFrumr01Ph8KoskUybukcdpIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e8023466.mp4?token=bvLBjNACPxBbt4W2SqP-ZHU2wCqzlqYlP-fsR_lUMxgCkeGggp5eYEKv7I5FeyMXlqoQeQBpN8FoSEW9qziK7TGu8_f7AJzqWlGgGAn-Y122sU4F2Pu3EPIEBsByaA6yVgTbzH2eQeAXVdlpIR4S7B_0m5YeN_Lk314t6ME_NdOGtQYxsfV3BV0dtQn7N90WaqfosNIAHVfTxbkWKmCR7lTEYWah-XGM9c5k-pyHkdQKiflCBkl-25bTbTZcLQ8Pbr58bVG4SAKmohVyL0ClErzt8VGaTx2yL2rWwH2YNVPtfUWxTFOCM6J5BnWqarSzEAriDqoU6rhX5h2JVpOJXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e8023466.mp4?token=bvLBjNACPxBbt4W2SqP-ZHU2wCqzlqYlP-fsR_lUMxgCkeGggp5eYEKv7I5FeyMXlqoQeQBpN8FoSEW9qziK7TGu8_f7AJzqWlGgGAn-Y122sU4F2Pu3EPIEBsByaA6yVgTbzH2eQeAXVdlpIR4S7B_0m5YeN_Lk314t6ME_NdOGtQYxsfV3BV0dtQn7N90WaqfosNIAHVfTxbkWKmCR7lTEYWah-XGM9c5k-pyHkdQKiflCBkl-25bTbTZcLQ8Pbr58bVG4SAKmohVyL0ClErzt8VGaTx2yL2rWwH2YNVPtfUWxTFOCM6J5BnWqarSzEAriDqoU6rhX5h2JVpOJXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حملات جنگنده های اسرائیلی به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=qfUl4hvEfDXdlzNpvyRp2kdX3QZa6LNo0V-EMLeuWzgop6Er8DA49y6N3zbpmGVYoCzBxbti5LpXqrCu2z81TYpyp2Dj8CQqtSdwSvZhD-rkiWuY5tk-9qPwYcKxkFdLGpIMNoUoDDZU2_ac7e_GpY4a3WunDP4WcLzfG4MeiHoj9zIYFwHQbsjKgPbWiOyLIYyg9ZwlyhTILZi7nX54ao_1hWiOkjQXuSCX-3SOTb6NQgfNSX-E5mRjqx_tD-rUPKqJyWz-PCTy6cZV522o4cTzGBlB_6S3OmTIwB5SGLHCURvD4GYQ-wddTrm73AnFq59ooJvgY2QRo9XMZ3CKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=qfUl4hvEfDXdlzNpvyRp2kdX3QZa6LNo0V-EMLeuWzgop6Er8DA49y6N3zbpmGVYoCzBxbti5LpXqrCu2z81TYpyp2Dj8CQqtSdwSvZhD-rkiWuY5tk-9qPwYcKxkFdLGpIMNoUoDDZU2_ac7e_GpY4a3WunDP4WcLzfG4MeiHoj9zIYFwHQbsjKgPbWiOyLIYyg9ZwlyhTILZi7nX54ao_1hWiOkjQXuSCX-3SOTb6NQgfNSX-E5mRjqx_tD-rUPKqJyWz-PCTy6cZV522o4cTzGBlB_6S3OmTIwB5SGLHCURvD4GYQ-wddTrm73AnFq59ooJvgY2QRo9XMZ3CKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLg_nCW0rNz3jkps6tg_PdsGUsIxTz9DZxLy4aF0VBZN7ZVfMjfQEyTZx3N3IkyZWwiEQFR90eKwuqazE83VikwGnPZWqil5pedXsKXPBz9LSOqxRMAhFqlDnLZ0MtHrzRouHwJCkcICKcAAW3YnvkCm1yPADt2ucI2FBNV4NbmdEarvAl-riY_FHKNDm1IjDq9v-OnoshRKj31w2G0JhsiWuDc8oHCYRWJkdDzk-dSCIV8ixdcQIXH1D3IRMqZp_9upSUIx2wiMCQB5HgK4WwE663LYpHXik2osPPt01vYkMY3KaB1z1b4oT-EaKl9ahQfFHZsHV0erx0isZpuC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=GN89B102jPgg4_K6mtisXHUgyvdu2o9kbJgd4l8bYstXnDJrxvs5ZldICY3jh_j5Xh8GO0G9jwEZelFzXGm8N4FVbcRgGNDwyWQeoM2FNyeVbFBXUnI7LhVYs95cst_dkA8RyEh0VxS1XaXJZZ2xgVM3a_4pH7iidTBPef22hojE2yZoznNsyMHrFymGk5VFxWcVurcsTkqzJTfTyMylslG0gAjmtKA7GVg_tZfExLVNuuigt8FBs4MvJ5OJj43SRylR9B4FgorIbxJ0TqSd7nB8XTO3JXdllXWogbP5D-wxAp-Yl6javKWHoYXCJTfjVpbYYjG1s_sBEZR30OMwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=GN89B102jPgg4_K6mtisXHUgyvdu2o9kbJgd4l8bYstXnDJrxvs5ZldICY3jh_j5Xh8GO0G9jwEZelFzXGm8N4FVbcRgGNDwyWQeoM2FNyeVbFBXUnI7LhVYs95cst_dkA8RyEh0VxS1XaXJZZ2xgVM3a_4pH7iidTBPef22hojE2yZoznNsyMHrFymGk5VFxWcVurcsTkqzJTfTyMylslG0gAjmtKA7GVg_tZfExLVNuuigt8FBs4MvJ5OJj43SRylR9B4FgorIbxJ0TqSd7nB8XTO3JXdllXWogbP5D-wxAp-Yl6javKWHoYXCJTfjVpbYYjG1s_sBEZR30OMwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71008">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=qjtlRJS8955-87Jzv8Bp7QvoqClB8cTHKK0XcPwvFXYLObfK6wO2b5C0lJC-VRBzcq_QkBhvJ50LH-4H98cdYk37KT424QnAs4J1qRieWU5tdBhRsAtL9k53eybvvvYYAzD-agsqecyrR9Lgg1RPjKPoAllgL5FSAGnVGrOJJnbTQ4_83H5NIek1Tij-hJLCTXo19lYkGSyag8e4b4zxqpYxN9_JiY-3W6QFLqNIKpCZtuzTRPe9f__kwNAldCdp_EoLbRDAsXZaid-XX0OYG9etMkxy546a8Kt5f1YF46zwxtLj0s9QPIB252balordrPwQfARTBWYfxPd5hVKlYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=qjtlRJS8955-87Jzv8Bp7QvoqClB8cTHKK0XcPwvFXYLObfK6wO2b5C0lJC-VRBzcq_QkBhvJ50LH-4H98cdYk37KT424QnAs4J1qRieWU5tdBhRsAtL9k53eybvvvYYAzD-agsqecyrR9Lgg1RPjKPoAllgL5FSAGnVGrOJJnbTQ4_83H5NIek1Tij-hJLCTXo19lYkGSyag8e4b4zxqpYxN9_JiY-3W6QFLqNIKpCZtuzTRPe9f__kwNAldCdp_EoLbRDAsXZaid-XX0OYG9etMkxy546a8Kt5f1YF46zwxtLj0s9QPIB252balordrPwQfARTBWYfxPd5hVKlYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇧🇭
لحظه اصابت پهپاد شاهد-۱۳۶  به مقر ناوگان پنجم نیروی دریایی آمریکا در منامه، بحرین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71008" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71007">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZTtSTupWoKJqypb8QfPyRCVZLTCqJasunGupkkOLvI2e51d5OUipNcTrNt_u-mwjVinYQ4XFCE8dZhv0f3QgSYSr1oMyMq-PCDTKUr1iBQ3Kypu_ZV-b4YOx0ptzkVFOQBV9kaEWxaAgpVWXI_MREXSYPOoqUomwNVN-gcnYqDMGQ18DQG9njxOBv16g3GIt5cr83ELBR0IgG4xeehnkg6Mf35DiE5dwC2V-N-Kdi9kSjTKqAvbEUMSGyrd7bqEmovkPOsXTGeflDWhnpDC_hb5EZ4Zghd3FtcQ4yOnPiH_nGXuUTG9LIaUUzKEsKkLzdbFvDv2nys57J9aPMLKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه:
ایالات متحده به هدف قرار دادن ایران به دلیل حملات به کشتی‌ها ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71007" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71006">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71006" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71005">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taI6Oy8VAyLaj3_b9_v13uhR5pqTMcRkGrPRY6uR3HVYMSmYmOG7aEULjKARh00PON7AMqbNdapFtCldIr_I7jxM9j3Ht1783EC1tNV8y8dzQgfo8RoY0Hv2ibt4f48bLDv6TpvFlqNnPf0fem2ReNdsOSUG21lU_W3TulPpSCHSoHtQTyD423DQOcFeuBAEklcPapoVuatIS5kNMEjPjzVxQ11vBeArM3eDwft3x9Nx8LWegdwDlMpFWq8kZFC3SZs3H2SrMGQVe9x3t-Ai0PBRW064e_slE6BySl95c5U3uWaWBAieaC6yqwY6_NQGNbMrZjxDLUsIJYSWDceQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71005" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71004">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26734edca1.mp4?token=S8NgbyKtBcrvWIRmegNtRZMUQXW_Nxwt_fHiS4nu1LJFpL3nmobys6MRv6TDpWTWko3jMr8IhhbygINstguPhU8TMAuMjiCZ8VvLStTzAnV1HUs9GVlcJ1HQlEOgw3wbPMEM8lctCTIWmeAFlwfdRXnBGEGgOUjLs9POAEmKen0zryL1SchE0r9sZVXszsSczy57YoEuMCdaCQVNyMsi94WE-CBnD6EZjxUcKKImX8_t2yeCxQyE-TtAvL9g3NxPM39MOg3Svko_4pAcT5cgCdtlmeGF1GskT3w9l-2bptM-PFxTGVF03V486hpRzpUYX8B42xM1wOsNQZa7wGCMQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26734edca1.mp4?token=S8NgbyKtBcrvWIRmegNtRZMUQXW_Nxwt_fHiS4nu1LJFpL3nmobys6MRv6TDpWTWko3jMr8IhhbygINstguPhU8TMAuMjiCZ8VvLStTzAnV1HUs9GVlcJ1HQlEOgw3wbPMEM8lctCTIWmeAFlwfdRXnBGEGgOUjLs9POAEmKen0zryL1SchE0r9sZVXszsSczy57YoEuMCdaCQVNyMsi94WE-CBnD6EZjxUcKKImX8_t2yeCxQyE-TtAvL9g3NxPM39MOg3Svko_4pAcT5cgCdtlmeGF1GskT3w9l-2bptM-PFxTGVF03V486hpRzpUYX8B42xM1wOsNQZa7wGCMQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
اینترنشنال:
⁉️
🇺🇸
🇮🇱
از شهروندان پرسیدیم پاسخ شما به پرسش ترامپ درباره زمان قیام مردم ایران چیست؟
یک شهروند با ارسال پیام صوتی به ایران‌اینترنشنال خطاب به دونالد ترامپ می‌گوید: «چه تضمینی وجود دارد که ما بیرون بیاییم و تو بعدش مذاکره نکنی؟ ترامپ، کار را به نتانیاهو بسپار که او بلد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71004" target="_blank">📅 18:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71003">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=fOLji0fE_kWVkfDP_27E48xwlM7pYhyi51zRqY2Yla-eqBE5_RJONvsfEyeVrjTzIxa9o5hqeune289raZ3ZIAQJWeEGFAHK6KwiuL_FqUl2ToRaQItvhZFKSx-D27tvLeGpc4oNVjm47KawN1uLYp78Ho3jVQACF_-r08lTCaHYKiiw74Ujnb7ua-Cj6UOeYXT4MlxY-f27t_FlRIMB_omsw-n1GzVdNQo9VYzurzuffAJLhNr3TUeQNcGABXTIpcZy6jJOt4hJH9ALETu3wZMuBIfO04XIPjmXjeUlB-jeZS315h0nFIMDP2How6cY0h-NfmTnbyPP_OYZ4Zj2ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=fOLji0fE_kWVkfDP_27E48xwlM7pYhyi51zRqY2Yla-eqBE5_RJONvsfEyeVrjTzIxa9o5hqeune289raZ3ZIAQJWeEGFAHK6KwiuL_FqUl2ToRaQItvhZFKSx-D27tvLeGpc4oNVjm47KawN1uLYp78Ho3jVQACF_-r08lTCaHYKiiw74Ujnb7ua-Cj6UOeYXT4MlxY-f27t_FlRIMB_omsw-n1GzVdNQo9VYzurzuffAJLhNr3TUeQNcGABXTIpcZy6jJOt4hJH9ALETu3wZMuBIfO04XIPjmXjeUlB-jeZS315h0nFIMDP2How6cY0h-NfmTnbyPP_OYZ4Zj2ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فردوسی پور:تاج و دوستاش نزدیک ۲۰ میلیارد از پول بیت المال رو گذاشتن تو جیبشون.
چند وقت پیش تیم ملی جوانان ایران واسه برگزاری یه اردو قبل بازی‌های آسیایی، به ترکیه سفر می‌کنه.
تو آنکارا، هزینه هتل‌شون طبق سند خودِ فدراسیون، 116,160 یورو شده.
بعد برنامه ۳۶۰ زنگ زده به همون هتل گفتن که قیمت‌ها اصلا این نیست و انگار مسئولین فدراسیون قیمت‌ها رو الکی بالا بردن! و هزینه ای که کردن چیزی حدود ۳۶ هزار یورو بوده.
خلاصه تاج شیرین نزدیک ۷۰ هزار یورو کرده تو جیب خودش و دوستاش
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71003" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71002">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=i-Qm8MoLZxVVjLUYKY16vX9DNw_HKE-vkxZ5zdgCpcy6zvBzR8hQL0AWoZyMLJG4LZtIjGAd_2ElKx0L22rMMR9DYwGDDhcyLSyd0pPQZGE3PtdljzD82AKNYMs8TBcMdKhmcvoDi3586aWAJzyV0DkEYnJCtkVY3oU6o8xxaH1oUdUAscRKEmT7Bk4puVbbEaW2TfZ8fF47_Pv9I05fu2OICF98HNM1XrfNATx1VYOm6HJdvO7vbTr5RB8zf3ltPm1zvPCZJg-NVilns6IpKFKJDD4D2hVWUcMBzooa8yweDTG22T54KgJbTCmg0qkm-B8zVUVJXnD_ipRDmBjjR0CEVGWKrJpqPOs3ABlP2A47kvYFajRvktwJb5gmQfCLQgykm8NDjT4ilDP4svgC-zfDGk6YMtPzyvi-MxUv39uABEGBEmmjDxQOe4N5hmkZwOsOtVu9sjt9jZw3jBSmRtlHG-SlHqU1gwGA3JRyoMUMbVH-BBIuv1OsKrbJUX8n65NtWJ_SuAhRnKaJfholXgI96mBV3pX81b6JbrKCu2m9NlbJRJ4uTUMPcfL8KBUQKHXUu-DAfHsecH3RcwJ9fefbjJ0EbmwUughZFTnSx-QeHjQ2lPlKeTVOnr-T3RwW0cAxU0CHnARyJwEG8YUlSlfCHZBL4TyYuM6zCIyAHNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=i-Qm8MoLZxVVjLUYKY16vX9DNw_HKE-vkxZ5zdgCpcy6zvBzR8hQL0AWoZyMLJG4LZtIjGAd_2ElKx0L22rMMR9DYwGDDhcyLSyd0pPQZGE3PtdljzD82AKNYMs8TBcMdKhmcvoDi3586aWAJzyV0DkEYnJCtkVY3oU6o8xxaH1oUdUAscRKEmT7Bk4puVbbEaW2TfZ8fF47_Pv9I05fu2OICF98HNM1XrfNATx1VYOm6HJdvO7vbTr5RB8zf3ltPm1zvPCZJg-NVilns6IpKFKJDD4D2hVWUcMBzooa8yweDTG22T54KgJbTCmg0qkm-B8zVUVJXnD_ipRDmBjjR0CEVGWKrJpqPOs3ABlP2A47kvYFajRvktwJb5gmQfCLQgykm8NDjT4ilDP4svgC-zfDGk6YMtPzyvi-MxUv39uABEGBEmmjDxQOe4N5hmkZwOsOtVu9sjt9jZw3jBSmRtlHG-SlHqU1gwGA3JRyoMUMbVH-BBIuv1OsKrbJUX8n65NtWJ_SuAhRnKaJfholXgI96mBV3pX81b6JbrKCu2m9NlbJRJ4uTUMPcfL8KBUQKHXUu-DAfHsecH3RcwJ9fefbjJ0EbmwUughZFTnSx-QeHjQ2lPlKeTVOnr-T3RwW0cAxU0CHnARyJwEG8YUlSlfCHZBL4TyYuM6zCIyAHNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طراح ارشد موتور (بمب‌افکنB1-Lancer) متولد سیرجانه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71002" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71001">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618f407212.mp4?token=rQOIiqzMI-bElqfr7hcWGkHj9oUWKgbecenyI_dDqQku9825nY8TQya33Y1Nx8rkc8xrM1I6H3XwzB0KyYzsfPXgBwrAep-GYFUeWQaPDMNLXQwFnwql7kp3hDfjttGL2qnmrgxSHWS5NdMkd3RPclyTtIWO28ViHZeA5n054JqNxtlkiW53L2zcmK5ZEJo7WVEWSuEPpL5RKS7LmauRwz_Ibm0ePkuCcyNzHhTR3gafDSyAO0-ZY0Hzwb3ZDo1p3YLwPPDsZPNnnQUccxRfFHi67KV8PxIbIRX8zsAYEKma-IxcA2Ac0hqPM8MsspP8G12oYOg10WIfbC62pG8GUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618f407212.mp4?token=rQOIiqzMI-bElqfr7hcWGkHj9oUWKgbecenyI_dDqQku9825nY8TQya33Y1Nx8rkc8xrM1I6H3XwzB0KyYzsfPXgBwrAep-GYFUeWQaPDMNLXQwFnwql7kp3hDfjttGL2qnmrgxSHWS5NdMkd3RPclyTtIWO28ViHZeA5n054JqNxtlkiW53L2zcmK5ZEJo7WVEWSuEPpL5RKS7LmauRwz_Ibm0ePkuCcyNzHhTR3gafDSyAO0-ZY0Hzwb3ZDo1p3YLwPPDsZPNnnQUccxRfFHi67KV8PxIbIRX8zsAYEKma-IxcA2Ac0hqPM8MsspP8G12oYOg10WIfbC62pG8GUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بررسی قیمت چند داروی پرمصرف از شهریور ۱۴۰۴ تا شهریور ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71001" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71000">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=lcl8RJFiPdjDnsS6QxiDqegvKLejlKo9HNx3foVW5S7fZYgslZi5Awe3xmXIEum6EmaLIaNszb448lsuYoqOgZNcG_PmiYb0KRfjq6aTDJk2uoarkUjwmXcsNu8KY0jVPH1zM9eh-8wx4qt1JQkjpFpPEEnH_g106KLPKYgyGZ3b8QVve3-8ENh_2GRyqSf2BuuZji1BvPK3xVal5dngCdk820TefFKxazR8kVwZchr7QJbfh1tbwXgNSxfLtOomckgWV8HAt7eVuSNFKC3mTeqA-z8m48lrflKAz5rb-V8O_MGARnMKyoIs8PEPUUxgdNHTjz1sijoCt0hCG6E1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=lcl8RJFiPdjDnsS6QxiDqegvKLejlKo9HNx3foVW5S7fZYgslZi5Awe3xmXIEum6EmaLIaNszb448lsuYoqOgZNcG_PmiYb0KRfjq6aTDJk2uoarkUjwmXcsNu8KY0jVPH1zM9eh-8wx4qt1JQkjpFpPEEnH_g106KLPKYgyGZ3b8QVve3-8ENh_2GRyqSf2BuuZji1BvPK3xVal5dngCdk820TefFKxazR8kVwZchr7QJbfh1tbwXgNSxfLtOomckgWV8HAt7eVuSNFKC3mTeqA-z8m48lrflKAz5rb-V8O_MGARnMKyoIs8PEPUUxgdNHTjz1sijoCt0hCG6E1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرت زدن وزیر ورزش و معاون وزیر خارجه و تمیز کردن دندان توسط وزیر خارجه هنگام سخنرانی پزشکیان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71000" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
