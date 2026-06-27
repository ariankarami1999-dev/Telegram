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
<img src="https://cdn4.telesco.pe/file/U3MfJiXJ6lyJ-mSvlAvGo1gTMsKafdfL3tuwCJ7tC-VfMv-0FYjL9mKoUssHD-f-3MuCsn4NpqaVjPueQshbAEk-Yusl9nt3V1fZxUk829e79LlE4n9rLyRtSnVuqkfg5B-5pb3ckDpVHxZmY5xCSHlGHB3qp3MgU_vpLuIH78fEt0GsJOM1dLOTvwo6rgI4MEf4q6bnBbNDbCahq61vvAsRUmTal4jdluFOZOCsMB1q4Q1WXcxMNOgdE9rartWPTf_Lctklo_p1EPwC_SVl4XD1dXmR50zZPLWLzcp4x5K6NDr1tHdY62clUBFrIq-87QNByfkggNtxY3YwQGhhyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 06:13:10</div>
<hr>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrO7cSrShcbA7oEVSGy5OWRjzxGLCxF-edMDWKn1RPt9HA9KJVM3fXvMWYGyOQsPlN68UOuZ0g8AHCZgyZ7L3BWLKZtMlLzsQSY1x0O0QdGP7qSCPQLv0GaI9GUDiVk0GA1dmY-QquKn3M2ufhxBj6mgV7dTo_P12UOu8c6qVOv6_vBlLp0jPzhbm7XZCQh1DPPQ7kSRx7BqnELKKgbLNgcJHjiavAahFoarTXpMkfnAlxY3UENbDS0V1bja6AbgWFiYB539GxTZ0SpjFhldfLt2L2yEb19ChY_es5VRk8i1QiKevT7Ghc24Xg_jMvOSAxlKKD6nFUghENAHiByVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=ZlsvbDClqvN_jrciemggC96xQ3ivTs219Hanke4olGno-WXNGEkHYv4kGcFMr-Y04ucP8cSGTr-_s1eIEIVSg7G-INKl2Ss1HOy3JK4vXV6VsUT2yHdO_m3eh46aadH9Eycdlr_GMcrzgJaES9LJM67OGOl99BEcmy5MKwkbA3dW_4TgnCrtSTle54p-gSDd0TLT6pCnsjd2DKl6IElc0BWoKmRhgAXgFMArPpb1-EM5sETpFjxmLBXFhXIuxgfsKP7rFgFF-gEiuBgn8BwD75q3Jr0M1mJ5fsrsm8yPt0lqopGw98CLG83C-2ZEXKOVS9CHjUPXl9kcGbu-Yyyxaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=ZlsvbDClqvN_jrciemggC96xQ3ivTs219Hanke4olGno-WXNGEkHYv4kGcFMr-Y04ucP8cSGTr-_s1eIEIVSg7G-INKl2Ss1HOy3JK4vXV6VsUT2yHdO_m3eh46aadH9Eycdlr_GMcrzgJaES9LJM67OGOl99BEcmy5MKwkbA3dW_4TgnCrtSTle54p-gSDd0TLT6pCnsjd2DKl6IElc0BWoKmRhgAXgFMArPpb1-EM5sETpFjxmLBXFhXIuxgfsKP7rFgFF-gEiuBgn8BwD75q3Jr0M1mJ5fsrsm8yPt0lqopGw98CLG83C-2ZEXKOVS9CHjUPXl9kcGbu-Yyyxaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6bycQ0H_-bQHyYXuerZVIJXGJPtf5k8WsGXCSgJHv49PhG4nmXW-iQu-VJCQd7kWV55iEoHQ0ZOChaxQNIVrTDcT--J8rDU55g_m26OMG_NMnIZpPd0f6iFRIYFHk1nhbD4p8gvzjIjALxeOz3IOea9vWUXvSrv6ZeDqWRxgCcmcWD1rM8_Iz5Vsla0ptPnx77bdiM0EkQ-flrpXVVYi0HCEmtenVkLCLPkeQxFy3QSW0F96Jw7YioerOXieHpnIekFPoqu2AwO902ThPjSxMerVsP40LwQyS5TY0Q2LN_-f6eQZJKXTU804dKwVekKZ_IwRG4Ibo8HGvTu62LO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=j_anMZe4xYmoKy7QSkaAWb0ci3chYBWUunVSY3erLkX4CzoeQJ0WbZUqUFQ924StGLxuwyCqjIRaSNFqusy1Uds445x0kxq-Fcm-v6HHkM3Bx7xU6ZphtjRMPNbRzAUMlN9jylmaP4-Lppymkqa2evQ3n3hTnODPlJ_q7sRCOcxXNaMhDTt-GfgPGawMRhcTYBUIqQC6V_jk80jOzadCv0HcE8DuUNRevjK2hsicPSMx0mIoku_S9dwAyGKwVS4CbwnvWK6PI602QqfcEzkno5RZa5YjA44BTzxTT0as0sJQJXh1dh6KB93IgtSR55-hm5Ojo9PKmlBjj0HmX1F-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=j_anMZe4xYmoKy7QSkaAWb0ci3chYBWUunVSY3erLkX4CzoeQJ0WbZUqUFQ924StGLxuwyCqjIRaSNFqusy1Uds445x0kxq-Fcm-v6HHkM3Bx7xU6ZphtjRMPNbRzAUMlN9jylmaP4-Lppymkqa2evQ3n3hTnODPlJ_q7sRCOcxXNaMhDTt-GfgPGawMRhcTYBUIqQC6V_jk80jOzadCv0HcE8DuUNRevjK2hsicPSMx0mIoku_S9dwAyGKwVS4CbwnvWK6PI602QqfcEzkno5RZa5YjA44BTzxTT0as0sJQJXh1dh6KB93IgtSR55-hm5Ojo9PKmlBjj0HmX1F-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkiGCAYrMkEcIiEKerwXI8yjSyj2J_fmpcZhuFpg18dKLC8aRWNPupQyzQBC94UtZ0i-FT4WLgPW_ikcb2awnNCecJHV8fRKP3e36VNEcFmrli29iVY7CFsQ5s32ulgiJ9nEO71uQRh_GWAcWkVzIbseopNmFHlJf4Lygu_xGxoqMj3FELFHzeoVdFDezSNew66jdm8Ub0-0TpMG1VtIyenIfdXXl1BVSUI4QVPX9UMkvq5giNL-xhXNbzk_SPZeOQvXddNfajOkmVxY35CMnoVvOq2NKAQXyqS7MzJ4FJxsFh0lGPQ9Pgd3nLewM8mpDdggUk7vFLYR78Zn9vD8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=vwVEsuMDWl_TBj2XDd5a1luIc2BlpDxic1z206h5DEucN9kgK3XqenJAEAZUpcKOkq4yZRcpyGriIAxZGLjOQzSIhtqoZBn7GMEIUN0w_wJfQrlYlPHwzZBLJ0wZdeQB_34lAyYEjZhWmzEA6UNvdpLDHJOq5x-0lvzmlPU1IRET4eGeA8-E-gYgVSVBwnvPBNxs6lGT2ef7V2av-Z9bohovNJ79wbcPFU831wf15baGRSoq0tIT7f1C71xKOlUIQiJX-inZcMkFxTQjAwV3xiafXtvIxKXfnnSZW81xy1WhGBnfQsth0bTH4OOiST_IUaVYPwoqBy0OmI_72mYkTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=vwVEsuMDWl_TBj2XDd5a1luIc2BlpDxic1z206h5DEucN9kgK3XqenJAEAZUpcKOkq4yZRcpyGriIAxZGLjOQzSIhtqoZBn7GMEIUN0w_wJfQrlYlPHwzZBLJ0wZdeQB_34lAyYEjZhWmzEA6UNvdpLDHJOq5x-0lvzmlPU1IRET4eGeA8-E-gYgVSVBwnvPBNxs6lGT2ef7V2av-Z9bohovNJ79wbcPFU831wf15baGRSoq0tIT7f1C71xKOlUIQiJX-inZcMkFxTQjAwV3xiafXtvIxKXfnnSZW81xy1WhGBnfQsth0bTH4OOiST_IUaVYPwoqBy0OmI_72mYkTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=DaEZlypaPVr5zaVOzbZ_Cw8CB7pe38pICsGHou1xVTRm4IHagHLNhMH5Zh0_v4x010uEEEKCbGDAHKpwBG0MVCdL6U5_qOB5Gyk4J3Ke8979r25sFnzhlAbR9j8cifEaLkwkJHAUQKAglOp_d8Ya0WVEwHkry_eZ48t-l9G2EebTiv-5WfkZp3EtniUkueZ6OYdz85FWSEj-5sHq9cuVyC417OoHeFfbmYF6QLdVW9nUzX3MzXSX4XgNfWyYIOSr3RAcD18UHHmG94Qmwa78vl0kuo8r_J01gEKbxixu3Pg1P8dq4dwdI8MI5-T5-LrcxvlxFZRp1vNztBINiAl3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=DaEZlypaPVr5zaVOzbZ_Cw8CB7pe38pICsGHou1xVTRm4IHagHLNhMH5Zh0_v4x010uEEEKCbGDAHKpwBG0MVCdL6U5_qOB5Gyk4J3Ke8979r25sFnzhlAbR9j8cifEaLkwkJHAUQKAglOp_d8Ya0WVEwHkry_eZ48t-l9G2EebTiv-5WfkZp3EtniUkueZ6OYdz85FWSEj-5sHq9cuVyC417OoHeFfbmYF6QLdVW9nUzX3MzXSX4XgNfWyYIOSr3RAcD18UHHmG94Qmwa78vl0kuo8r_J01gEKbxixu3Pg1P8dq4dwdI8MI5-T5-LrcxvlxFZRp1vNztBINiAl3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Uc-UD93Eyf8x3S8Yzj46Ohk46_61VT2VLQF2oVCw6RsDtPRYqhBxeg6pbpx_e9hjb0ps_Zts8OCL2UZwt-x1xcZ3zZNfiz7MPqIGCjONmBi_Qq_n5dWvST8NM3yzxH0S7ReD9R2CU_oAihZQVm6gwxgyzsdd14vuqnIRouuWkGwUX23ZGcXsKbdH9SopxbI3GiAWPUaKwJ4hWeiV1K5ChhRehnsTzFTpL5ryLQdMRgpGoEXaOdbACqoM3kxs_HwYpO3cHSGJWmAo8UCXDekWDCsgjSJq_wOQ_ZjX3kjomusAF9SeIJVfF5UrL-pbsKo-8l88DMjHBNLrFFIN8Fqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=UbhHhM8lYtnHNbCzwKzK6uCsxDhHb7NVeC4Yeuq7zoDWCUMLuBYr9N7r_EkrNKKAQJWZ5F_zYYl4KeWxRFf6muYo-pIz0e8tU_rhBF42OV5bXQKCqx6J2FCfzkob55jZn5VZu-OrxzTuv9EJdhSW3_Ny0LaMwHW5ae_mGw-VDioW9RMPVryc8Ytnobq-l1C6T4Aid5uZR-KKsqBp8ZsKk2LQtBJohDxhltXLQ2bFOuaqk72KGVshpXxFKtAZBN2mEwfeK7NGdA8NUoSl-nP7oFQgB1s30yf4ViodKfHHKw0PQjdfXKIEfewy2sf9udKzXXeFIiKumN07jcsesZVt9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=UbhHhM8lYtnHNbCzwKzK6uCsxDhHb7NVeC4Yeuq7zoDWCUMLuBYr9N7r_EkrNKKAQJWZ5F_zYYl4KeWxRFf6muYo-pIz0e8tU_rhBF42OV5bXQKCqx6J2FCfzkob55jZn5VZu-OrxzTuv9EJdhSW3_Ny0LaMwHW5ae_mGw-VDioW9RMPVryc8Ytnobq-l1C6T4Aid5uZR-KKsqBp8ZsKk2LQtBJohDxhltXLQ2bFOuaqk72KGVshpXxFKtAZBN2mEwfeK7NGdA8NUoSl-nP7oFQgB1s30yf4ViodKfHHKw0PQjdfXKIEfewy2sf9udKzXXeFIiKumN07jcsesZVt9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU1RBzQTBUbidDg2yMXAf_nMJck74b_xjwLmAP8MihLGmDwuJfXa7DeC9FybPRzttvU_7STN7_lKrj5HfP5B2ut2PHL2fi47qQL9Bq8BmqLSB8MX0LQZt1rqCYjh6dEbbyKkYBPbKBbRqbAOCKGOsF4XrMNi4JdXW76mTM3PNUM20VWI6MgNsgI_lhFyPLnkDdTCDYSMk7iQZijCKA0Zd8cIMzK2fQya-iEAg4Qu9u3cxZ3xQD38i6Suci1_7nKVMA3ix9wnB0JeZ_me7-5dmEqKulYDu493hkjAKheWG6tbEYm8XU0c87XXrQb6qz43Wf2_xhuzHYx1wPjFpNIQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=q0Y2mkVuajJXQLghNY-3QjU5zTJRomKrXiR4hAJ54I3XXZPFv-VsMN_bOLyIXaB3js1hk-5ORxJwXcw-0xl7g7TYVFb64IXEA2EDE6QpBPZV8-dLTJVwZDZXFZ8xeofJgvzCUtPp-nB5agbl1os7YSn0WFIG1YsmTmKvJFDN6-4vO4VPUk_fH1UwUlJ5rTAB97sDssuEpTrzEgrBU0RyUv3xmNISgrkxNF78vFz_pfXkXh3uZRatWizx4cq_5EOzcshXmlEA5e1rHIjY9B_TqMPamkYcHIF6Lqth9HCJL1GarLEpDkpw005kdXHUUTh3eVi_X6GLUtDythEaYhnaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=q0Y2mkVuajJXQLghNY-3QjU5zTJRomKrXiR4hAJ54I3XXZPFv-VsMN_bOLyIXaB3js1hk-5ORxJwXcw-0xl7g7TYVFb64IXEA2EDE6QpBPZV8-dLTJVwZDZXFZ8xeofJgvzCUtPp-nB5agbl1os7YSn0WFIG1YsmTmKvJFDN6-4vO4VPUk_fH1UwUlJ5rTAB97sDssuEpTrzEgrBU0RyUv3xmNISgrkxNF78vFz_pfXkXh3uZRatWizx4cq_5EOzcshXmlEA5e1rHIjY9B_TqMPamkYcHIF6Lqth9HCJL1GarLEpDkpw005kdXHUUTh3eVi_X6GLUtDythEaYhnaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMbU3vzuDXvf5urw_4PfR-LOW4cQqHFWwCuZF9DCCxbpU9uFC-19MFjn7lTK8XXK0-UtHaxdXD-4XfLc79o_aQQkIaL-UyyTJefeWXqmxD1EyK56G6tZGJkPfKRHkIetetVbrmRv2DfMLKaPZVtJoDcr0tjIa1iA85bYscSauDcZ_gVIQ_0CcVIJkVuwnJmdcdPa00Nt_chS2CVYX-yFnATzbgGgRbWS35QlpoO1-szE8V8NkmIbyT4maIlveTtn-DySgNj7Lcbzjr80znWwNpFN6rZ7Z9rnZ8cuziX3y2nHkmIzm1pg8APYAT1ND673c8qBUYURMUMQAcY4gr6ChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG-5sqZX1xQBmZW5c3NWWez7I749Bp0nnvfe30Prm4GleJehkcM6oPeUHhoLeM27sHa4g9pNOrDKt4CyjG0Ft5SvdJcnpUKSWQtgb63mcEDYGnrsd6RjFvY2U8iIK3SUTD-BQELaY4-cHq8wnvoRCZ9etkYCTF0eDnEy-kRIowWOWav_UkeJNCfU7Sm5PN6GYAvjSV4sUfLC6Zx1lBhpsiEml_gyIk8QFddUOKIyzbXMVz4AF4XL048NSe3MueZbL5zVBM2keDLXhO-jybmwJrEZ86eoGcG5S23zLeTt0UpxqnVJ0jRKgtgSxfJlaSaI7ESe5hV6T6lj0EfSa8TeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsHKqb_La8m_yyO26AyQT6qASjMDPTr8_5eT-qtWr5WpFsdyE87azjqgXTAyZwsHgjpP4jIzN1SHCFCEvs1LUU2hpmZ5Wf18j03q-Y-MFtjl8n4cCyZ-CStrGXZs-Epacj7bd6eQpr0ar8-7023tYYx5S6TbacozT0jn2_uF5pOvw7Mj6_3KEl5KLQhwVOqKVOBusi2rkEND4gGbF8Qrko8RNZPVclWolU0BNkiCst9sxoP5BT0177BsivmWF8ThHlTc81Px6yxMCaqqsM70gjbww8o_Fb4wv1NZV62tsIjTwklc31zH3SVFSCiD88l9qij8S3gNVm9XkCy8RWtUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC5ZRQdOHVYFW6-raQ7qbkHYmgLrtVsDhur_vZGBjpii03a74u84a7BDTwyST3nLpqBEanB-AhUmMOj8AG6OXw58UttWDLsm3sDErD_l57t0SkOAlHXj8mk3XiTeLTaM18ZGSqfYLlde6yBDZVCdZ7F-QBJ3UwXk8a8d2gNZQltqHPy_EJ_3O20IG62TfX7HEtdr1AKMz90l5DyIqMSveEbhaQ6-UxYCb-iq5mm3f-3djA6x0BR4SvTmx81Xer5ElWwH3nApZijhVhTHc9enQVKSvGJ0plXHYghFf-qmUo_b6BRkLsF8CSvgQxUouKpAIvp7FtIvlBRJMeSvU3faiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jisNc-GuII3jgAhWpUFfEh8_DkmhJpAbVbNipvktTQPIMAGqKrsWTuoQpMX5cpxdAtQHguCkHWDcBXeZ3PdY9xI1DsafwKSvpzUBCNnAMP7kk4t6fHFBuw47VPVOw9D0ezIawTbIzlwT0vFBHBBKHxYLjS0uGDxp-l--z5zNuP9-U4-bIBg7WMX0f6mUvNNsH6pPCH5XCIEkUuqQGo-fHNDzsaEUnY3gnb8-86aAuMjhPPNjUkR6TGZT5qR4QIHo7ADouJUDoyG5eBn9G6jxFPqFzfN-CBYPXXsqScvd8kifQe5lgZVOzA2SCrIBVx8G1Z9bF0j1Bxxvbaj_d8ca9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1yqSKDWR0Bv6ahAGlnWbRraAdHbTvkN_2842ibZPmSPE-06xgLfhpSxPY8hLHSFYnQYbzIxONNs5dsTmIrQ5esuEwNVycaLKgouKI9A6IpmNEPFzCLe2MW1XnVYY69kceI3B0I6aWNbNHS5tXnDRTQfFEBPHUYudvbqderK7WaRE0kkPrBSXQbid4MyTZihOwaK6SnnVxmvQmK-PY2hVEQ621bJ4CJwcDfqEr8d9SiqzXTcI20JgfqMSS7i885qe0DHyEfN8OM3dwtyBARgxWWHEpvJ67F1W57__8LKNi7Eb3CdvF58MN0cx2LVI1RIKzqOoS8PS2ODKoy4GWcX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYBRVtc_ofzWPFR4BTiR-rJwZcjIuU-eBXaVTO5I1cFhFZM49PNXO0UG9izG2sZpLZaQCOaZSNiXF4LB7NzOSW7DIG130sq_DPELtbsRyy_pQBnlkC7GESPJcBGwog0S0vJG5jvC8pwo-SAxaWsFGvAbvmc0ebJ3HGWjDAuw_gFUI072PTqNPArs0Q1ISRkkjasZhJEtpci9XebvHM858yMkatiqSpzafWbNZ5TIcSTln-o3uxa79mN935l80WF6wxj27giVqJO61FGtvHkeM7DXGgH3rE7IhjeL1Pz1cvYfgVtsdt9H6UIJXUg243q4e9yUHBal00NRUr7pMtEdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1OWhfM8N0SaZAh-Y5yeieVZjEdV3q65BCJIFksxXudlwziIFfTtAtfTRCh4c7U3BiXrPUYr8sfnuBNBaq2T5OeMeqDSLXM0vTbbshy93x_IKDiPJHfGFVMrxfOv2CnKJZYcd8S5aI3WbnBy1wjdC2XhuLO2WWwEjDz1qJ2IybUjrZNX7VZ6YjRc5Ae0TpRUxg5Yn7YV4EymSVg-se2SXlM9I5ymBW2w0bmmgxQ9iUZtJHD54VxXYOpljofOI04_BVoannKeyHgqtdBAJ9hMkzXjtjnOL91nhgV3sdx-Yfq2CU-nE7qR17k0Rk46slMBD7r9EQGZ3tRV2NR3nsofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5BhspcJvWsUHX1l_ZSYx4BLbOVS6NIKr1ZiUlW-0WrO697-hC_lJ-kpoKxfLSTVwjNOb0ik0kv_Ww3wN34HHUpC-OQ4KchX8LX8UzRbc-22AiW6Bh0BpXI1c0d25PVLjd8ObxX5aZoFyHsQc9aog595GIsCCEdzn7dGlbKrPxgI0L-6DS5AK8qI8X7RXR1-RGPHT5obwGalHPNNN-noqKQ5EvRTnFIhPxAgqR0PrTdjwXVcXht2R5JK-simj_R_EDkVafF6GOYIjgAyeBOIKkNG7jAdJynwVR4dH9tGMo_sWQLxWw6DQfwx__NyknA5UnevSAj0A4mU_MINzdII7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3zO2oKfXJ-fEiVMpWDXugkY72dmBbcNReNvbG79Y4uyc6RMPDeUviPVQaFJQBfa9hmfL52Hj7ea_vbMs6ozTzO_dzfdzci5UR1fWJK4ETDvvJ0npnusiZ1L0PjrZpidZH92rKkebdgpuK98N1OJujIvo1rCEROUSxEFFdIXuDoNMgJOYI3uNWuKSC1Fes1l56Di7W-aZSeOLM-6D_1FrqgISi_0lZpMBgFJnNB8rB0PmNsPXlHw0yQz7YsjWMSLgTRZc3hMzcTNIYeicskdwXP8mP3L5eVD1mNlWgE1IOUN4AMygwkCZQzgSI004U5iUuYNrh90QFeXDBd9GdrPug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=SkKEvnqzppPGYocJopTE1efTmVJfAR_OOx0ZhgKXPOlr3nFhuQ3MBOHaPKnNdz9KVKy4QiKD_KJEwfwQ4p9QzdsAgwK1slcp5Fpu8_UlTb2Mf6_a068uqGudflNOir9hBdZm5acb5G7EKEL0hmUcEeNNgQi91zjJ1EPKEgDhV_SuU6Ty7Ih5g8t3rbDpipIZef1WrxE8Rw5gS93MUqkxDvK8E4Fm02L_-Gn80ZDW-c5JZ4AOXFkD45GhgBgGdI31HrbS30QVtXwYkD28MiGJ13W5w0728_H9WKEuRWzEk9_tVLEWJ2XmunjYtSeAXU3m7jIYEscdBBtWP755SvqaGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=SkKEvnqzppPGYocJopTE1efTmVJfAR_OOx0ZhgKXPOlr3nFhuQ3MBOHaPKnNdz9KVKy4QiKD_KJEwfwQ4p9QzdsAgwK1slcp5Fpu8_UlTb2Mf6_a068uqGudflNOir9hBdZm5acb5G7EKEL0hmUcEeNNgQi91zjJ1EPKEgDhV_SuU6Ty7Ih5g8t3rbDpipIZef1WrxE8Rw5gS93MUqkxDvK8E4Fm02L_-Gn80ZDW-c5JZ4AOXFkD45GhgBgGdI31HrbS30QVtXwYkD28MiGJ13W5w0728_H9WKEuRWzEk9_tVLEWJ2XmunjYtSeAXU3m7jIYEscdBBtWP755SvqaGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzAlNAuqqwSgXqo8NvmErGWn7enByHW8GRYhiXiKN-CS_a7OpbXtNvNyWBELH_und9x2t9cokX2yvYW7Yvkem9F2vconDE--oCR3eWK6u8CfR2AkJVXmmZGvL2910oOL-bQO0WEhjFP_KqDxrygyUN6KwWDDsdYcBO2LDWFXM33Aurf1u7vuvnVtWfADO1if9bj4GyKRatj3e87rxpFyk9UIQZJKONf4A3THfNahMwuCuQHCLck3lmPVyKjHceAcGjzCxAD8d3GpX7krns8nKSJhA6jH7ltD3PqVi0imRp4QDYbfYuKoUw3mMm8T5pC2CEgVGT1Qlib04rvIJwEe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=DcwtL8FSBd5SOddOrh65SX8J6WkuLCsnkcHGwHQdGQAkaf2HtlTnB1aMEDXDi7vEJBeMVfk2H9gIhVqhWKTNrMEGCk5Ctl5AU0ew5EjzwGANZCbLi8zIvMZuCG0Pk9j-wtYUYRHwLRvHcMdPsKJxT9i7om-XiyIz6Dk8zzl79Kxn_WGyFNwQmLCvZlLxMhpZnrlJZV6-vDVgI5htUFra5XmBTULj-bt8IVbTeHISZTuSMFb2Tle5_Ri32trNB_02Obi5Ry5P_tc4DF_v73IRGx3-IWFXmmN7r3E_2VGxlPKAKkwr2oudq9RmPgJYYuzwdFlxYpX55Bd_Djf-segz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=DcwtL8FSBd5SOddOrh65SX8J6WkuLCsnkcHGwHQdGQAkaf2HtlTnB1aMEDXDi7vEJBeMVfk2H9gIhVqhWKTNrMEGCk5Ctl5AU0ew5EjzwGANZCbLi8zIvMZuCG0Pk9j-wtYUYRHwLRvHcMdPsKJxT9i7om-XiyIz6Dk8zzl79Kxn_WGyFNwQmLCvZlLxMhpZnrlJZV6-vDVgI5htUFra5XmBTULj-bt8IVbTeHISZTuSMFb2Tle5_Ri32trNB_02Obi5Ry5P_tc4DF_v73IRGx3-IWFXmmN7r3E_2VGxlPKAKkwr2oudq9RmPgJYYuzwdFlxYpX55Bd_Djf-segz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=pxiFAN8cwWtbMRTqhBvCcAfQZd_pzWsnMiVwHhZmcU_w1fq9EPKjULoaBGRoOaMePbH5QeF7XNQCU2P3BY2Mvg-Jeu2cf0ENPpJBDBzhZOi12ZCoROUG50k0aybB_xCxLLgP34aynjk4Y3_mRc36Qi9RgeI8Y2llLTprrCFyJjTv4Nz-oHpBNqIpMx5NPpOeSYIrC2gpCeTtvCI9bAiBr_BB_3QSMkozBwqLOnb__J35ZcYZuYuvqPegecvBfFv0780-h8f-tJu4nShuFN8tYxdQufbPLXYlBPR5lxQr9eAG4HjvGiRqIk_fVxvsaThoVthJXjCUntXR6_OoY6NcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=pxiFAN8cwWtbMRTqhBvCcAfQZd_pzWsnMiVwHhZmcU_w1fq9EPKjULoaBGRoOaMePbH5QeF7XNQCU2P3BY2Mvg-Jeu2cf0ENPpJBDBzhZOi12ZCoROUG50k0aybB_xCxLLgP34aynjk4Y3_mRc36Qi9RgeI8Y2llLTprrCFyJjTv4Nz-oHpBNqIpMx5NPpOeSYIrC2gpCeTtvCI9bAiBr_BB_3QSMkozBwqLOnb__J35ZcYZuYuvqPegecvBfFv0780-h8f-tJu4nShuFN8tYxdQufbPLXYlBPR5lxQr9eAG4HjvGiRqIk_fVxvsaThoVthJXjCUntXR6_OoY6NcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y73wSNy3qj0gtSE6ZcnalFuZl7sdV2H_jurV5ILpUF59Llfpih46m_x6qNTTzYLjaNqI3MMgDNcDgrHmZKhwPZ-1mA5_ZPTlh7AckrcaKpedGRD1Fsg_tE7Q1cGkZE30T5kqSQvALKe61WuJHMnbi3nUZawj7IWOXhq49Nl1PhgdXd9Ph4iaKLfTM8eoAEPpjXHBIsj9DqlYYgZmidZ0XwQBzF08BfwI0B80LmF80fHLQbMknaHyPWnhAHHxIQXKKdHdMB26q1uHsRF1YSwulW7dNR6MvsR36ERW_B6uTSb8p3iwKAFQ7VEIXgo8Q6pPT8SlaMgM4iP1Gpvi9K6KVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlYKvXcpx9Utnvx0hq3ftMymGIWxO_v6KNic31lK-A2YvERf4M8WjXGH1CXRZw5xdBZObA5ZKsPeAeRNz7cQIHQSRYyvjU-Z9weld-LEOfHQbDEg0aA3_fsMplpJ_9RUEuKfsUNDPDh9_sZP6xgelN-EPAioyivNbKaq_SNiNfS0E0o3ZE07Vk9h4mdTBa2NrlsDeSDyYVQzFe1V64amlnVfX1rqDzF9emghd55rEs0CWJteaiyEbOiEEciEEF0gWOC7m4AjNd5uMS0yIRW-ygeX470nPR_JuMYpLY9cH8CNXycI4Vp-ehFrj1I3K1A1Ti9jPCkiUeimMEJ-8WsR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqtWFRuh4BTN0Z-Wqr3pU-QPrUISnzI5PhA3AQH9NmeP9VbZTnJSEIfzw36tlS51FeJ8UQ-q230RFlkxnp7tIG6IhmYz0sJimycPlppZUqGs4c2-cChWIyNqIhWi0wnM93eC5eP9J5608kSYE0YZh1Gs7G-tHKoELJlxCMrY3L2N85odxLqzsC4eI2_aQ0fIHoq0He7EXAcVXNNvx7NR1i7QvKhuIBdU5B_StF7Ppu7Am9OT8EW67E8nOgjccUHyIcYJ0iOz4oeL-TQBaWlj1oalcsQQLndhbzsxwlgUHn_4PvQAUWt5bfc_E0GPls9Rwdl69ghsODDlPwEww5WHGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ucCTgh3LVIJi1NMvytBy5nawrMKBQaUkhryqDAC01kPu859zo26u0SP4-LxAz3Ij7NI8DeK3u70DQAAoqzKe4ub5h3UhlrPxMXxLKNJtfW_HEpmdiQON8V4u61Fam8sS-xR-arhO0ofO5XT0z43PpISY6GTr_drPA_S_5E4gcrUO5fea8yyHwp8s8wAJoGNAWFYAao8G-0kWLwC_C2VWJutr4KosrHAVoD0N0hG4sdvN9bmcSghWvgJcxCwem7FLHBUWaE8U8ysYPGvTw-Tjv_pv_PbX9JB0jFqLeVfskb05THo1Nrp7qscR1xDcLo3741oOD0GmgssyYI-U26b15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ucCTgh3LVIJi1NMvytBy5nawrMKBQaUkhryqDAC01kPu859zo26u0SP4-LxAz3Ij7NI8DeK3u70DQAAoqzKe4ub5h3UhlrPxMXxLKNJtfW_HEpmdiQON8V4u61Fam8sS-xR-arhO0ofO5XT0z43PpISY6GTr_drPA_S_5E4gcrUO5fea8yyHwp8s8wAJoGNAWFYAao8G-0kWLwC_C2VWJutr4KosrHAVoD0N0hG4sdvN9bmcSghWvgJcxCwem7FLHBUWaE8U8ysYPGvTw-Tjv_pv_PbX9JB0jFqLeVfskb05THo1Nrp7qscR1xDcLo3741oOD0GmgssyYI-U26b15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c046_dadHsQqq5JS4ASedRzxcSZy2q-vNKDH6aRm_6BAkkuLw_DicIRpVeD9z1IREAHv4EHL1dDkp9fddH5WdZUDB5fQu4hyfpaq8rG6cufm033WmsHbFzFLml8bWTQD7DZBbAy7FgT0vFJh7QUOdM_zAnewAwMTjPgPfWdEPszRSMvNY0jezVXbqBYvTUfnrlqHO11zmvUhdQ7PRF2iqpOksVyylWjs3RVDhR3PZ-PvIPfSX0cJompRJyAW_waFfBGpmsAdYmj1wXkRLvAAfFOCqcUIg-bwcy5dNhIrtvqJgCnQKGfd4tcaMyNtyi1xFlvpfEQjBUinm5W4MeNHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=Xt32rYwSObWs3GW1P51MQcfaTqtS0STS5JizaF0BFIYwHxY9E9152UzI4GTwnMv0KflGDHsaNcuMlPsxaHCefMx2njLwSMVVVdIFnnxDlNh7TnF_AFeVtmKYxM51hUuXXOZoOzeXIiEYb3omAN9vK0b4I2K1oqCfgXDYGMjjgpWRmzmji3DSBH6prM8_xO23hT4_-lHcTwFfqU-sxgtFrfJkYxvXiJX5TQ7u4DYyJOZeDEVUqeIfOFV_wnsxASJetk4XEZNQ4cKpFzmiu7RRgXqZnu-8Wl5LcvbTI0ED4TIsfULfzfv-DOiW_NLU3R_v7F_Lq6vWcKUUrgr3tVXHSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=Xt32rYwSObWs3GW1P51MQcfaTqtS0STS5JizaF0BFIYwHxY9E9152UzI4GTwnMv0KflGDHsaNcuMlPsxaHCefMx2njLwSMVVVdIFnnxDlNh7TnF_AFeVtmKYxM51hUuXXOZoOzeXIiEYb3omAN9vK0b4I2K1oqCfgXDYGMjjgpWRmzmji3DSBH6prM8_xO23hT4_-lHcTwFfqU-sxgtFrfJkYxvXiJX5TQ7u4DYyJOZeDEVUqeIfOFV_wnsxASJetk4XEZNQ4cKpFzmiu7RRgXqZnu-8Wl5LcvbTI0ED4TIsfULfzfv-DOiW_NLU3R_v7F_Lq6vWcKUUrgr3tVXHSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=k7aueevpsP-NzGIGg7bff1cRVp3Fs8E8Kg5tPjY8Gt2cPffh3quB-Ir3LYGjoY0RpNoO3Q3GcsX_MXQdhWHpanpKwZuCxU6M-JVKhdETsJeOOHgKOg-i4jeT5RTN-YfRAvfO2qR5P3PuiwXiOAYfnBAtKhXhWDJ03ljFUlI8H_49M8ntu9gMICwhU3_PiDqKJOLii--uzO_83ZtECy73Wnc80Df1-0VVzXTLmU4pyPqD8fK8N2c-NcA3OoafnLpVq1EM8i6nuAImFLjyUs0UUlmyVhXQJQ995hRIT-cn_5d_uxRbcp4tPetUNf0bkL2ttK47UtX2XI7IcW7RJckzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=k7aueevpsP-NzGIGg7bff1cRVp3Fs8E8Kg5tPjY8Gt2cPffh3quB-Ir3LYGjoY0RpNoO3Q3GcsX_MXQdhWHpanpKwZuCxU6M-JVKhdETsJeOOHgKOg-i4jeT5RTN-YfRAvfO2qR5P3PuiwXiOAYfnBAtKhXhWDJ03ljFUlI8H_49M8ntu9gMICwhU3_PiDqKJOLii--uzO_83ZtECy73Wnc80Df1-0VVzXTLmU4pyPqD8fK8N2c-NcA3OoafnLpVq1EM8i6nuAImFLjyUs0UUlmyVhXQJQ995hRIT-cn_5d_uxRbcp4tPetUNf0bkL2ttK47UtX2XI7IcW7RJckzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=a-Ba72ryLxW9l9ddIXQnmDn0Elyu08JVs2oXcKllvk4een3jot2ihSgbL_AURtHSrTkXQNISFPrzOahLD8Yy5XS0cGAAy9VqprYkzmEYE0J5mLk1liTmDcDolX2U-Rg7Yd_5aRvS7W-ZAs2UxHpaF1-QgrpKvRCaVo0NZvtF_jwC4R5FtK-kQVWpxrD-9dB7Ohx-SFmV9jWlP0m9kkujS7FOa6ibQYtLUkmtlzCVFWobSCoPo7UwIvb6FGsisrUmlSGUNcc6JkVCPuuBw3dedit1_arfYthTmtzi2pduiJW7NGCDdleAJTQLMUSXBsZs_TIzUfVid4h6bmy0MaTRwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=a-Ba72ryLxW9l9ddIXQnmDn0Elyu08JVs2oXcKllvk4een3jot2ihSgbL_AURtHSrTkXQNISFPrzOahLD8Yy5XS0cGAAy9VqprYkzmEYE0J5mLk1liTmDcDolX2U-Rg7Yd_5aRvS7W-ZAs2UxHpaF1-QgrpKvRCaVo0NZvtF_jwC4R5FtK-kQVWpxrD-9dB7Ohx-SFmV9jWlP0m9kkujS7FOa6ibQYtLUkmtlzCVFWobSCoPo7UwIvb6FGsisrUmlSGUNcc6JkVCPuuBw3dedit1_arfYthTmtzi2pduiJW7NGCDdleAJTQLMUSXBsZs_TIzUfVid4h6bmy0MaTRwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPQUC0SIln-GBvTVmri-YP94KUOkabvqvb0Z3-Skzj6gWt_tCbYWMeobfqOVnZHS0SCd0Pu9VeltPDouQv_p6uBHRTrBeHg7rZys-7mGW77Zu7m88QMmDDbGJSp7Ey4Qoj87Yoi7LfXI1fkQQElC1E5Aj2hDizMnABaTukk19rVYC_6vdMBmgPbcJy9FIPeUa4tdnB68LlB1gwuJgPPiPcdUvGqGC0P-uvxscH8YJQFE2fbt5JSoKYHfOZuXUqJAdPmSjpibTzvvF0vSM4Qw6nOWzZkYT_xlz1HWS4KybqAtVpAHLxl6b8d3F2xKYE3i7rcdM4zgWqLFF7srFYQq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OErZ6O-Dl70n6b8KG9lEu-DQLIyjsafbwZrOJBYYykNUOcD32G06c_bSsuJfz2ZCoeOpLkuUnuy37yxlFO4utc6bhxiElp31H_j2KBF1zXxGZ1_EFfaKcrUZ6rDT5FmSL-Uz_TBScrvLNBj1nPDKSCaq8v-5-h-bVEOdTdKUQ_lfB2CyqrXPoiuep0BiJ7kWlqORBo1m8XScHdSurM9OsqpSLL94L8E0q-FLfwipt56zg9GEno8xky42mlFjxb2vIp2lLF9oNWYu_24tTwWOBCJttKfRI2rkQi9gNRUZ8hjNa8Q5ISOhpxQyOmYim55gb8d5w1MT4YVWMFoiWsPPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FecEaS7euOuUNyapSvw2zaI52XJOJtx6kV1OS2AbN6qn0JQHLVO6i4SaAVXt-d4QLBUUJbzMDWefDNlwvD9SHofhsk-UgLXK-68j8yEmr3swAxDkjffTSRwer7ZFCxFAD6Z0R7jaZ2KzfPLySVzbkAq0JuRF9yw_5yLfKBOkY8ZsHPrLm7i0b0ujOtWzQKgsl-ODbyJ4eCk_hgog9u2Jepnq7_o4rriQ2xm9GPR2V1nMcrQA2ovFscrBE5Iw4p9mUc6sdRU-CoAjluxDrt0oM9hWAnuFyMV5KtTIz2n2u-j3jL9ygiROucc2XRnb3KiREWbgYAO7ktshGpEHtdlFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1cSMehYYSvTiAdXKiVY8fzRTIhOxs2zpRzRa-UwEbNfRtK4PeHosXKOK_5C0oOYfq6FzOHcl4q25UichwUugDdujrvWBnAiev-OLRylRSAfPBFdfECEMr_OO79bElxtM1O6YBOT1CP9jVnq3Q-ZjPmM2xhc0eQmGy0dvQU8llCILUhKmG2xwfaOe0fJZnCOuBJLyswL7XxeZK6_SCZohZso3gS6AAu0ktNaASBcPLFDbtOLRT1T3VHT3hwAyDyRtqzEeYMhwQGp6g9xNAUFT2rjGfM2bDAMK02mbWpmnCZNeUM3wz-v3PfYMIptU24kMOr6DR7aeq-WopX-IeHnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=NdgmjlbEGL30NBgc0MaDjnYTcxC9zSR-eUCzb6sxOkle8LtKpDK9FOtLWekE59lsq6_sQiKtpM5MgBKrYioKM1Jjd18dQNG96wBpNSKh1vTFrFSXcihYDoeQwkOE6TcMh9cHdKF02RKLc8SV2kqmBcSOZby7_-7-feFeM-csxAitHw1MekzcyfLiXkLLPugN0vq5J9wnYcZ5C8Xk0pN9TRr_oiZTfSBQ_EnXGYqZV3rbYZCrPEXZuir0sidkGYu17o5YTpASgI6Lh3pviqmTiMLlzYdHUUaWVR82G6Qxr05mp3Vc9SjKdo_la3ClbAfBtIuKCLX2KSoXqkCIcdkB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=NdgmjlbEGL30NBgc0MaDjnYTcxC9zSR-eUCzb6sxOkle8LtKpDK9FOtLWekE59lsq6_sQiKtpM5MgBKrYioKM1Jjd18dQNG96wBpNSKh1vTFrFSXcihYDoeQwkOE6TcMh9cHdKF02RKLc8SV2kqmBcSOZby7_-7-feFeM-csxAitHw1MekzcyfLiXkLLPugN0vq5J9wnYcZ5C8Xk0pN9TRr_oiZTfSBQ_EnXGYqZV3rbYZCrPEXZuir0sidkGYu17o5YTpASgI6Lh3pviqmTiMLlzYdHUUaWVR82G6Qxr05mp3Vc9SjKdo_la3ClbAfBtIuKCLX2KSoXqkCIcdkB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=lt4dTll9Q-BnVSbH2MsHTEw2lZ_35Vz8UhhYSnGv9O6hr5B0qzzUz66MefiAUdL6I7RcU602e2Z0E1FHcm2-rP7dEJ1U3je_82SqkuDD9CR8uabIqyJpmov83_MeuJ8W2YT3ftW9uvbX_RAHw4bOtuYnSUcRWhNkwQOEsSg2NDqOGkvrx9cR7uivMbF4RQwZ7Q-ffhztK98J-jjctyCjmx8Y0mNt1Ty-WrKVeNMZMIIu6cSXbdtDY80WL2tbf1wvM4MwB4rKts9LCaHi6-HP_XlrkKiUBS2KlOu5s1wAptHm9pBnbUkIRVPo0yzSCr896LHQR8ip8bKZdfbh-RRQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=lt4dTll9Q-BnVSbH2MsHTEw2lZ_35Vz8UhhYSnGv9O6hr5B0qzzUz66MefiAUdL6I7RcU602e2Z0E1FHcm2-rP7dEJ1U3je_82SqkuDD9CR8uabIqyJpmov83_MeuJ8W2YT3ftW9uvbX_RAHw4bOtuYnSUcRWhNkwQOEsSg2NDqOGkvrx9cR7uivMbF4RQwZ7Q-ffhztK98J-jjctyCjmx8Y0mNt1Ty-WrKVeNMZMIIu6cSXbdtDY80WL2tbf1wvM4MwB4rKts9LCaHi6-HP_XlrkKiUBS2KlOu5s1wAptHm9pBnbUkIRVPo0yzSCr896LHQR8ip8bKZdfbh-RRQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=rmPerBn07cH1jDxixERyYKbsXPtvqFXegJt64gpLrKuzvfDKXk39AUF0y238_Y9AbiScvUy70cNqmEgdy5Zc2h9CuEZjrgjrRY3tiFnhUfHN9Ggr-r2n5uo9BkEkXbqMmKeIfjsAcfI20VNr9PR65LS8QTISaakKFnF8xMMI0tjLEzv7QwE3k8MKl4rgPD7TVjRUCZbmcLteL9FPgqixGL2OgOFYjCWAfPl0KUhg3TYsOA90Us0cg82VTFnIELS917r1GHiatE-UNY3aGGt58DOPfz9OmPLFNPmL8AtpcSSr_VdnDTtaYmTVWZiZxWwP4xf96ukZ68HhC7V7IdT3IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=rmPerBn07cH1jDxixERyYKbsXPtvqFXegJt64gpLrKuzvfDKXk39AUF0y238_Y9AbiScvUy70cNqmEgdy5Zc2h9CuEZjrgjrRY3tiFnhUfHN9Ggr-r2n5uo9BkEkXbqMmKeIfjsAcfI20VNr9PR65LS8QTISaakKFnF8xMMI0tjLEzv7QwE3k8MKl4rgPD7TVjRUCZbmcLteL9FPgqixGL2OgOFYjCWAfPl0KUhg3TYsOA90Us0cg82VTFnIELS917r1GHiatE-UNY3aGGt58DOPfz9OmPLFNPmL8AtpcSSr_VdnDTtaYmTVWZiZxWwP4xf96ukZ68HhC7V7IdT3IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5Rs1bcjokMDRDj6MRUK2lQjOzsgtaoq5ikcx8JFByozojN1susoYwps8n46xZ6lrt-t2traX3vrtAb2BWH_k9xw2eqeLz6X75qEyH8g4gxW6zf7kWnODxDsOV2Xnszu4_XzobTah2AQ7SzrREYhVsNW_KtVULXFa0dcgsQuHxc8_LziLhx9aO9m55DC4jUVTrhG_n4CUFHgGTzPvR2M4Bi9_7p8imLSspg2xCG2DnHJfpyTEzblAgRARi4D71TsaSj6-1F7bvTQnhZWStQt_ewrLDiyfUYty9jRDADzTkD1pRs2kfJRWgbgWcz9XwqXuwueELHQcfi2DahZ2cmWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=mwA3yr-1s998Gzz_BVP7y-5rDayea_-4fCiEFA1J6Xs-Jl516KCD0Y6zbFv2qbhf1Ot2GsEcEmYls5FLA7LIu1AlHFEUZ-Fcf1f4dKZSBhwR49rq_rfd8Q_N981I8W1ehMA0Pf5mKPrtQ7F6DcB-RyZWlMiHGSWkkr1TbI3KIabkv1aqH0puLb9y9uD50ScP3kS6ypJ5xUToRzf1b6f2RHR61RNpZAw9f6Tc6RU7V_GXpL1Lnak9z_JS3QlyZhnd1xjXlQXRbDtZ_F7HaipgtYo9sjyuUpKKbu8r7TRnO6RBY3CU1u9tgH-0YgLA7tYHQoouT_cr1xgzemNlQDhogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=mwA3yr-1s998Gzz_BVP7y-5rDayea_-4fCiEFA1J6Xs-Jl516KCD0Y6zbFv2qbhf1Ot2GsEcEmYls5FLA7LIu1AlHFEUZ-Fcf1f4dKZSBhwR49rq_rfd8Q_N981I8W1ehMA0Pf5mKPrtQ7F6DcB-RyZWlMiHGSWkkr1TbI3KIabkv1aqH0puLb9y9uD50ScP3kS6ypJ5xUToRzf1b6f2RHR61RNpZAw9f6Tc6RU7V_GXpL1Lnak9z_JS3QlyZhnd1xjXlQXRbDtZ_F7HaipgtYo9sjyuUpKKbu8r7TRnO6RBY3CU1u9tgH-0YgLA7tYHQoouT_cr1xgzemNlQDhogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=dVUWqW4ghKHKA-jv1UeFv1AuZQPhwJEX00JH1Bv-z-ifAb5CJNX5xH09A22AHGSxD4ls1AekFf54WoMpqTeqstO3x60FDFh6JM6Hbn5S73S5AJCWOmzb09-lIhSkPiALC7pnjZf1qCeFiZTraqOanKRVswubRS2F8eUZ4B7hbYjs-mFk8GDUpBwIzG48cTMmRTb9BwAzCOM-N5icnXxzG8mhKJyFOtSYf5Ll40gOcKaVNqZ_cYD23EWU-dg8pauPyBFR3XAjQ5l4GE_dUsRJ9DMaqmoxdb_cW_yC6DycRzGTogaMiWcMkXSrQUN_o8TPVfnPHNNcvKSAvJT0z19Sjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=dVUWqW4ghKHKA-jv1UeFv1AuZQPhwJEX00JH1Bv-z-ifAb5CJNX5xH09A22AHGSxD4ls1AekFf54WoMpqTeqstO3x60FDFh6JM6Hbn5S73S5AJCWOmzb09-lIhSkPiALC7pnjZf1qCeFiZTraqOanKRVswubRS2F8eUZ4B7hbYjs-mFk8GDUpBwIzG48cTMmRTb9BwAzCOM-N5icnXxzG8mhKJyFOtSYf5Ll40gOcKaVNqZ_cYD23EWU-dg8pauPyBFR3XAjQ5l4GE_dUsRJ9DMaqmoxdb_cW_yC6DycRzGTogaMiWcMkXSrQUN_o8TPVfnPHNNcvKSAvJT0z19Sjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lssjUuJ53q21quDs6O-Hi3715cTz9dN2bTJLbDOf9ACv7N63Ik6NbChiX7NBe3NIy-I7WuQhS2JQIKiDo15ReYo9MSj5QrWpBRxIl8Jlzlf6M8WYVUXo87elRpxyuZL1olSe2F_nWucoMEeqdPV81ESKNRmFQKX-6jpM9E0WX1fkxmwEwlQZBz9upjj22hrHZCEXCkHPUFla1y4AefXamRLD6pDIVDhV-rJw-ANwmDlyGq9Zliae8u0fFHxPi15VnUt-rSkau9ODvX3FvGqPkGa6D1vJsfjyKM8xCtscJw4gBoj9QnCVjhUPEifWu_tkfh3fxSo4ij68ZtQtCwnJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=TrK-Hp-XURlWkZUEbpZ-iA_JcfUYa0AbY5FBF52bTjKYbRLN20ArdO5ZsSWrqTh5bI12DoZfspMcKAmxrgzWeLRR3s-7kIOg-s2Tk9AkF1V8CTGhD0422O91-QUvfR9TaYua9l35UeARmTuyBfg3oeq1j6dlIhVmN2uoifhzLsf-R6L9MwGBqU6X-KFryG2B9vCtm2tb9l-ail_j8F3jsS1TJo5WQ5ln1emwFoe-X_eIHrc7-2FP_Cxo1IJXmnJY9VfxNEwfIzv5O6Mcgub8kKRtIL7jyHeOMtCa95j0WtegXD0D-0wd9dHsJySnMUx5KmI0N7a9ppGn_2wvuSDxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=TrK-Hp-XURlWkZUEbpZ-iA_JcfUYa0AbY5FBF52bTjKYbRLN20ArdO5ZsSWrqTh5bI12DoZfspMcKAmxrgzWeLRR3s-7kIOg-s2Tk9AkF1V8CTGhD0422O91-QUvfR9TaYua9l35UeARmTuyBfg3oeq1j6dlIhVmN2uoifhzLsf-R6L9MwGBqU6X-KFryG2B9vCtm2tb9l-ail_j8F3jsS1TJo5WQ5ln1emwFoe-X_eIHrc7-2FP_Cxo1IJXmnJY9VfxNEwfIzv5O6Mcgub8kKRtIL7jyHeOMtCa95j0WtegXD0D-0wd9dHsJySnMUx5KmI0N7a9ppGn_2wvuSDxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJYZKCkVqi_JqgMKNoi2M8Nft0s6zz9nCNN8Vhhg9HY2Y6udCuNz3Eot63QGXQ0QrO6rbr7Z70dO8tFrcZoxXgv8gaI6hLzD2Q7C_w1P42fZbBI1VklnctF2Rsu22c22jGcsu5zdnR6A_jaRXbXMXSrQkyKaETDHsMSFzVKhD8LVxDbuN8BBUQorBWgSjrDMze6ntD35xlIxNeay5C7KOhU6k18i_9mm2BsigfyEFFyK2bRHEx7OrS34CcWnFIhtc4mAGqq01Nr2fZg2Ur1c21edTZG4l9M0ilakimJ1PCY9o4rt76bqcwrFvj_w0QiTlSGQo-Lbvg4qsg-tsYi-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCq-WY8rMhK2l5jjU0FF3IcZL5hONbuCJHrKHASLZ20u69L3uelUcwykQiJBqNuNnYNaEP-qQBlgqxvAzjVQHbHfC5M6QnMjthxHY4BUHm0Lmag-GH87GGrPL2zdyT76ChMI3boQEO32Pk_78_G29V7SHk18TnVbOPanU84-7lw0QSThGYjp3jQD956oZOqtW9oVExZENocW9QHPl8Vbo_UCsWzwzKV5nW64L2SIQjbQGiMRqd2wQdy1mpFUAdSdzx_ebHDAd0DVZ3zGrfWszOw6tIvz-9q9kYv264tcOQt6wXlTNXA2_5Xw0rCQBvptoPD7CBNjap2V6k-Wqd0-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=lYArhL286VtXPFzN6eAsFJyfHCutbmOf_eb8FJ_QLf3yrY1eAnG0NJ_lSQ82fiRAiuUwxypSw2E58h21ibqJlfq1GMq3B1swc8UQzi_wZEz2-DFmOvd24G-o9fdXCRNKMzDDKWPHDsLkHGjt7VqVuhWX73JcUOZYkWEKMGqSYAKCo8JK_x9AHgm8RX0x9T_-dqjxprJcqXWFYBqYV6rdP0hpsJK8JmgcBHVB20c6ezMqOyRM5e3nIVGN3IPA5A8DN2BpuF0O_2ClZTQwd_DTKpLm8Lmf5DX5wqqbvLMc2450Fmx6umjF2en6T2Rpv5nwzPUg7loBu6QKIKE_SOj_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=lYArhL286VtXPFzN6eAsFJyfHCutbmOf_eb8FJ_QLf3yrY1eAnG0NJ_lSQ82fiRAiuUwxypSw2E58h21ibqJlfq1GMq3B1swc8UQzi_wZEz2-DFmOvd24G-o9fdXCRNKMzDDKWPHDsLkHGjt7VqVuhWX73JcUOZYkWEKMGqSYAKCo8JK_x9AHgm8RX0x9T_-dqjxprJcqXWFYBqYV6rdP0hpsJK8JmgcBHVB20c6ezMqOyRM5e3nIVGN3IPA5A8DN2BpuF0O_2ClZTQwd_DTKpLm8Lmf5DX5wqqbvLMc2450Fmx6umjF2en6T2Rpv5nwzPUg7loBu6QKIKE_SOj_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=oJCF1zcriVb_KuQRiCS3HU9bzC8etDVCiryQy1kOYUo7F20DHYL6LT4oh_YLNHuW6GFs-jhV9zF5VmBFP5Krc-hb8r4BIpxk5eCQLF5K6gCZd-d3iWj113GtiD78RV3_e7oq_gD2wlC-ghRrcqi8a5O2rG8gMV33O9foNVivNMCSHDtP4MYHfGNHJ0qCpryjoEu7wN7gjHnBeGbQrLfPGc-Iy1oF709FXZP5n3D3AiveQQZjOhaLfg-3bvWk4dqGDI_qRi6b2twffpeAwb2a4lrpjd1XexZW_0QjX0qIHwzDQ_Gfqppdh1dYTOBbzbyhmkU40ivbijQ4JFlyf6Tdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=oJCF1zcriVb_KuQRiCS3HU9bzC8etDVCiryQy1kOYUo7F20DHYL6LT4oh_YLNHuW6GFs-jhV9zF5VmBFP5Krc-hb8r4BIpxk5eCQLF5K6gCZd-d3iWj113GtiD78RV3_e7oq_gD2wlC-ghRrcqi8a5O2rG8gMV33O9foNVivNMCSHDtP4MYHfGNHJ0qCpryjoEu7wN7gjHnBeGbQrLfPGc-Iy1oF709FXZP5n3D3AiveQQZjOhaLfg-3bvWk4dqGDI_qRi6b2twffpeAwb2a4lrpjd1XexZW_0QjX0qIHwzDQ_Gfqppdh1dYTOBbzbyhmkU40ivbijQ4JFlyf6Tdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOF_5V-fwoVN3jdAIWgb4X9-OADbgw4_lI651JHG1q-qrBOvitXv8uPFxo9ho98C5oji81CoVr2mgu4jzxNshQXhDw-1CGWwfm4t5b4ULzgTndfdABlNUaIWWhqty8SDbq_6JUhizpz4K6pQzQwbGi8HK9mKCEhrZIwBiAUeScNO6ToEm4rdb0yuswskJ73kiXiciwHoCWtxIHkHX-ssMhqfQD6rdZtYf9gP3hNYxhsZFe9ZK-FSDujc_k00nzX1qVJ1SvTNAXol1rmDpR0KdlIqvMxNdVz7HPkAaWf8kugcK63Bj1LEnMs0KXP4GSikbbNGy51Rn3KDPWl6F2hizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/admFXkLBe06AyPIf_4dv47dTXv6ZrqgfruThSUspmRqwEUF6Nxfpr-RTHPJ_GPLYwwk9PSNgN0ZUIiq87KrOocvWeYpRyX9hFLkyVE6Hx_NSHh-qlFuPbeEWx6yklNlABDacYcw0YeWHFzldJ0ZeQOfV0DxHlhdO2JqBzT03upujwFYcdeF0TckihGv0lJglPlwsOgPyfNF9u2yYJya8unNc1uZtYMukAJkly7POpBAJ0unMmoYSFlLQxMPQUBO0CVNVsvNzwzRqGDbrpin1gcgKbNzBe0nACA6B_UYIoFLKVxTG-pGZBWMhTSPszu0ALcYSWlKTPzsOlrtQUAP6qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=avpgADsqDnHokU28c5EO32BMzhBWXIxQgcF0uk5NpWOBEUh2Od7pfQKuZsgZ5E-09J7O3njSqlAinIIEs4xqAbDCsD_7Iolq88bZxnushiUCdl9RIi7DkSnkQB7KYttLtnH3gl_b_yxdrWAjsmm9EdXNtDAwAkMAFCRsa3l7tVukwfaA9THBz7taBrq2AdGEUTAj0UJQhxJBlz42pBHuQ69_NZD4b3cF572B9NY5hBNsG7ipUeR7A-qXTBh_Ox36xmo7mP9F0BLsjccNWPlbIs5FOPRFDvms_sA2GvII3hDZBSGpMkRRU3UXqK8JcTVylG9Ho7kibC6MmXtJlZsl9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=avpgADsqDnHokU28c5EO32BMzhBWXIxQgcF0uk5NpWOBEUh2Od7pfQKuZsgZ5E-09J7O3njSqlAinIIEs4xqAbDCsD_7Iolq88bZxnushiUCdl9RIi7DkSnkQB7KYttLtnH3gl_b_yxdrWAjsmm9EdXNtDAwAkMAFCRsa3l7tVukwfaA9THBz7taBrq2AdGEUTAj0UJQhxJBlz42pBHuQ69_NZD4b3cF572B9NY5hBNsG7ipUeR7A-qXTBh_Ox36xmo7mP9F0BLsjccNWPlbIs5FOPRFDvms_sA2GvII3hDZBSGpMkRRU3UXqK8JcTVylG9Ho7kibC6MmXtJlZsl9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=vXrILSAGmYa2q-_2T5VWoit6gw5I9IpjQBQXQhAo6HNtDIjEd3lCiigE3WpR_yPP5_P8jkR7U903eqJwIpROQCIJuz6C9PIDBMENyQMbcIoP4epZ2ms60oxIRB8vE_yDnkYQpy7wJDoY9jtStEpzIe8tmg4IFdCrFjDDbSS9MmVHNigKQG5fLSzuoDdeJjMh7Nxuo9XUSZommOK4ku7cel0paYnZxmPLGQYzfI1Z_Nfs3efaRpKaNB-KtPYk8OK7Sjfc4giie76-BryWQD8Ce-PZYHPdMHvgW9mXGeq2EJsAkrsYSOqZ1LW4zo0UWec9QLyvUSahtKuZWPkC7BH9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=vXrILSAGmYa2q-_2T5VWoit6gw5I9IpjQBQXQhAo6HNtDIjEd3lCiigE3WpR_yPP5_P8jkR7U903eqJwIpROQCIJuz6C9PIDBMENyQMbcIoP4epZ2ms60oxIRB8vE_yDnkYQpy7wJDoY9jtStEpzIe8tmg4IFdCrFjDDbSS9MmVHNigKQG5fLSzuoDdeJjMh7Nxuo9XUSZommOK4ku7cel0paYnZxmPLGQYzfI1Z_Nfs3efaRpKaNB-KtPYk8OK7Sjfc4giie76-BryWQD8Ce-PZYHPdMHvgW9mXGeq2EJsAkrsYSOqZ1LW4zo0UWec9QLyvUSahtKuZWPkC7BH9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=LAx0hlsINzAWpoEKwyqhGiBRWQEyqkYFypI8znorhJ5DDJblbCsgD_1kNWAU8s9BRwyn033eRcr4a57Y823LHB8FvnlGGrTMp-kPdJe4fC2dw9Fsc8QyAdzF3vBbc0yVg_wIUew7o0Jmn2-xxv2Gm3DAcvobQNiPa5QVwXIJcELmK5tQbBKYKFgxU0xlTc6LYE-Bc_B5uUuFO18q3KOm9gw-pwciJurQNxeEHYzm5sQATtsWzc0p11HhW2GCeUB-U5OoGUqJNcsWxzjaqcVA19T_aPX_qbcmK-K7L0xaYTsdE11uGhAP3QabUm2638dhRNTesS5-6_QxQ2QyYv7lBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=LAx0hlsINzAWpoEKwyqhGiBRWQEyqkYFypI8znorhJ5DDJblbCsgD_1kNWAU8s9BRwyn033eRcr4a57Y823LHB8FvnlGGrTMp-kPdJe4fC2dw9Fsc8QyAdzF3vBbc0yVg_wIUew7o0Jmn2-xxv2Gm3DAcvobQNiPa5QVwXIJcELmK5tQbBKYKFgxU0xlTc6LYE-Bc_B5uUuFO18q3KOm9gw-pwciJurQNxeEHYzm5sQATtsWzc0p11HhW2GCeUB-U5OoGUqJNcsWxzjaqcVA19T_aPX_qbcmK-K7L0xaYTsdE11uGhAP3QabUm2638dhRNTesS5-6_QxQ2QyYv7lBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=DOIPWhOJCnDcHHItPs0G3pSPncwxn3n_wwbqDVK5YuT13LuJMAdmD1XbXuGSe_ZsmyoG1jS7vBuWtNGV7ZW6Ejm-PrxfPTt4p65fmfhdKj1mUvJLFJlsWK_4TDcpBF_XiLOuDWIox51PvUHI9FOpUT0CnqvF_LMbasprtYGT8hX25Qp4fIPiZ9QdBhSJp8pxDR9jjQsGZ5lGYmDBkgj0LlnoFUl9CZ_iAvlojzhyJU9ZvKksgla-NROaNOm7TWsVR2Lu1-tsG75GrKcuNGBzhcncQ8IC9Z7J71JOOGYLQ-I8f9NcEbwIR0V4zZvG13DNLVQrrHm3l-JqNkZfZvD3eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=DOIPWhOJCnDcHHItPs0G3pSPncwxn3n_wwbqDVK5YuT13LuJMAdmD1XbXuGSe_ZsmyoG1jS7vBuWtNGV7ZW6Ejm-PrxfPTt4p65fmfhdKj1mUvJLFJlsWK_4TDcpBF_XiLOuDWIox51PvUHI9FOpUT0CnqvF_LMbasprtYGT8hX25Qp4fIPiZ9QdBhSJp8pxDR9jjQsGZ5lGYmDBkgj0LlnoFUl9CZ_iAvlojzhyJU9ZvKksgla-NROaNOm7TWsVR2Lu1-tsG75GrKcuNGBzhcncQ8IC9Z7J71JOOGYLQ-I8f9NcEbwIR0V4zZvG13DNLVQrrHm3l-JqNkZfZvD3eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDnSq9UbCrIlMTpZYSB-xTbcYLA34Scyr05E0c_2uux7wEfyejy-auZVjNpZNzZO8PHYca9mFhl9RM3WqD1zy4McdXZN3g5DBImDf4xcdjSLVbHxu_cFmZNgQD47Sd4AGjNdqTu3fxePeDmXQRSW2pow1VGLjlLLi1k4Udcpz_wd6sIKAr0Elr2Vk5viLsZa1RWEiLGNJIqrTE078V82JnAki-0hKkhOMigPO-9YzG84D2LLRiQ4llWlGjpKsOd-qME5s7eMXMdCJHIuPGuyGDB6nR9rQadsJOK2ikg7i1nIcT4BhmN0LGUoeYZ0FayKnZzZWDNYoQif3e5mgdVnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=nj9tOBnMxSj23EDVi3s-GqAMNwMNs-Fp38xR3tiOvvyWobVYv6EJCPz-25qoPR5uLfAfB_zk_hm9vEbzX7kdW7IP4C1jmjuHTmj9LJRdzohdIHP2_bI6huU7IiSgzjYHpS6XVTcreOip80qWzBTE0Us14IZLIuz6nG-lGyWOkIdzZEQCfLqOwng2ZISEBjV-rnKJU4CFy-Cr4Qm0mRUxLp8P61wn0rwq7_cvBrOWj2UleWUy4p54tUO16SXOuJV9EcVPmRWc8ZOMCOuqGN1Ni6cccl_hlpYJryclnZIyN8r7h-okq4bnej2_9XPygE2N6kuKsToEc5qwj7Wctseet4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=nj9tOBnMxSj23EDVi3s-GqAMNwMNs-Fp38xR3tiOvvyWobVYv6EJCPz-25qoPR5uLfAfB_zk_hm9vEbzX7kdW7IP4C1jmjuHTmj9LJRdzohdIHP2_bI6huU7IiSgzjYHpS6XVTcreOip80qWzBTE0Us14IZLIuz6nG-lGyWOkIdzZEQCfLqOwng2ZISEBjV-rnKJU4CFy-Cr4Qm0mRUxLp8P61wn0rwq7_cvBrOWj2UleWUy4p54tUO16SXOuJV9EcVPmRWc8ZOMCOuqGN1Ni6cccl_hlpYJryclnZIyN8r7h-okq4bnej2_9XPygE2N6kuKsToEc5qwj7Wctseet4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwgAh0DKKAkzU0LqBGE3wA5kBKJU2luy4UzrwMKekIfdB97jw2QtA6Gwo4gLxb3LMsIXi-5FbO5nyFNkpeGRe22rZliYfSvuvM6lUZKBED7L8-I_5ONbZjTdlfckNoO4T__-Y9pZfZ2RJJEbSQIPWfzCJJ29y8lgcwUXvYLAzRsSguXA5zU7f_NzfCBaz-g38YND0lq0ayGpwxFEH5mBMrUDOdkF3-FvOijvFouyqOOEo1HbKbGcutvDHVh7glZ86eXVz60xCmeubceRE808Z_rA8XifY1JRLlsBjRmowRnvTXgeOLnmR16z2v7mhN-iRyTFNLxY68i_LS3CrpyBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=CawozJjeLTDHZVXZnItfJtgWxYiouZ4Otb0tI9mY44NaMnUsuITIOuqfF1Fta6_eas-d6Nn8t9NJm6XJihfFiIwT2fMROnBZvX0jnDijdILSN7HGug_ViROIOZJzPDFXK0WbxKaWPjAqHyQQXub7wyo2g_J5CPKE9YhNWnRtfk7ND0jxQPfqLzWbQzmu0hLJ6ruCiFNR5ou2CS1wwSThL9AOKDD4FWp0FnsLO3eoM0ZrqemkqosLFz8_KkfOaBAKdlyMmwEc7p9-IfSGzrI6TjMdaro798A1ajRvgB_ZwF2y8bYeEBQpy9R5nxXDrRxpuOqsB9-ZxFLMxCH_2LZysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=CawozJjeLTDHZVXZnItfJtgWxYiouZ4Otb0tI9mY44NaMnUsuITIOuqfF1Fta6_eas-d6Nn8t9NJm6XJihfFiIwT2fMROnBZvX0jnDijdILSN7HGug_ViROIOZJzPDFXK0WbxKaWPjAqHyQQXub7wyo2g_J5CPKE9YhNWnRtfk7ND0jxQPfqLzWbQzmu0hLJ6ruCiFNR5ou2CS1wwSThL9AOKDD4FWp0FnsLO3eoM0ZrqemkqosLFz8_KkfOaBAKdlyMmwEc7p9-IfSGzrI6TjMdaro798A1ajRvgB_ZwF2y8bYeEBQpy9R5nxXDrRxpuOqsB9-ZxFLMxCH_2LZysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhzW0ENT_awROf98Upa753Mf6fYjuMLUOstIV6OLHiofPKxBpFfsewqltnlRGYVB3BtSNW5C37NA82LVJO8WQUxHiAgq1Y5PiHbIGKG67-MgTkIvdwCwRkQOujp4MZrqOS78QXEuYD8pPbfUws4rvYOvd9fc9Ffd1WNhaLHVqUcAeNVycUtbaww6M9lx6-UVu4MBDZeJbqj767FrtqI8_71Au-OK8B01ZOrxwNIkbcKfIGAxiDGnbHP944OG2D-ICyfGTITQMSnA9-fq-9Crx5oYgrYn7uj4_I3CWahkij0VyH-2evKArgwIh0dZJQUCcHc7FQANzA49SygEszL4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=n_vttJF6fR2LHPsZmMcqgo5u0eF4uBxtlxcH0uElwuI4SNdV45Qds0MbjNFQrSIZChDpmqUUOFYNlOhF6EDzNThtTZm6dxa3i52NbNEJckBiv-vv22CYMg0hJhLB6riV0X7CP3r20qbyQ-hMw1NFx70sqol_3dEpD8W7gHq0eWqGmFnE5E7pdIpaL8H_CcNzAk9x0iybgN6YUueZgUkQvVusE0Ioo1M1ps5Ijmx3v9TGwjes_mhVFHXOkElOl89AWQDMt-pMQhO7U5wKBbTXz_w8VKUW0ernqckqw7MEi2F5I5IlKkfUtis7LO-iiYRO1WsXrmr7ifFu3TqAPdBysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=n_vttJF6fR2LHPsZmMcqgo5u0eF4uBxtlxcH0uElwuI4SNdV45Qds0MbjNFQrSIZChDpmqUUOFYNlOhF6EDzNThtTZm6dxa3i52NbNEJckBiv-vv22CYMg0hJhLB6riV0X7CP3r20qbyQ-hMw1NFx70sqol_3dEpD8W7gHq0eWqGmFnE5E7pdIpaL8H_CcNzAk9x0iybgN6YUueZgUkQvVusE0Ioo1M1ps5Ijmx3v9TGwjes_mhVFHXOkElOl89AWQDMt-pMQhO7U5wKBbTXz_w8VKUW0ernqckqw7MEi2F5I5IlKkfUtis7LO-iiYRO1WsXrmr7ifFu3TqAPdBysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFyuqFboQ52pWNmcpX1dyl-oN82Du4-JdcUeCjkE0OIQWLq7M4s23ivFQb2E9Xc2R1IrzPNpqGF_ghlUzJ4F3JdfaCkfiRqyF-oi2bqZSICDtDcDPMdXGzo40Arw51Fqmc0Z4MGoxQiGW7NnkDzqXVKAFSzMg37BgBb7SYTilvsNytQ7eI46KH52d2j2NHDyRLRdJXrQ1ky4Ipx2SoB4JPL4R77BRyCfJ6BRdPBMrGAMW5qh2T0J4K3uzYc42KxFlvx-X14Ae6BVWbQhtsf8KAGsnGrk6xwxLulw2_IsRsNLk0gjIk2KEvvdomRHj8sj1G-8kHYRjTkVvH0j-R905g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=dTPcjgKd4KNMLXhuQMlrweBa-9DWNnBW2q15Qqn6WJH_QsHWAPbBZTU9DBhjYLTXQztOmJfjGl_ijqJdeSk5YrUMl5SS7AWRK1Vq9uKg4CNGgGgL5o2ST_xNFqG_BrO7QEC9KXz-HCxgrUzX79WyB1PWyLBlk-_7bvZMR-rp2WhHVM3OwM6dQlSmyLL3r5o7Y33DhOZyqhT_bHIEe5SafyoHogbGXWQZ7eIWbOg-LIzepiAl0KgHFSQY6BBwLC04ksWVuzGNhR7qxJaEBJWI7Dvvnd9LnhWrzBoUGF8qL62f_pC30GVzz0dMabGMx_fG7aSoH6mlgMB42b1IsKNFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=dTPcjgKd4KNMLXhuQMlrweBa-9DWNnBW2q15Qqn6WJH_QsHWAPbBZTU9DBhjYLTXQztOmJfjGl_ijqJdeSk5YrUMl5SS7AWRK1Vq9uKg4CNGgGgL5o2ST_xNFqG_BrO7QEC9KXz-HCxgrUzX79WyB1PWyLBlk-_7bvZMR-rp2WhHVM3OwM6dQlSmyLL3r5o7Y33DhOZyqhT_bHIEe5SafyoHogbGXWQZ7eIWbOg-LIzepiAl0KgHFSQY6BBwLC04ksWVuzGNhR7qxJaEBJWI7Dvvnd9LnhWrzBoUGF8qL62f_pC30GVzz0dMabGMx_fG7aSoH6mlgMB42b1IsKNFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=MsXNJaWQic1bA8XWbnm3tKPu50afr6XcrxR8p52o0alOU5T9444CmD9B70p3eRGzfwgQrjZw4KpPtHnXdLANhZpq74BbEnTyT_3HxQljQaBqnnfWyTgbNButzwjKhPfx3R31HsCgTu22ierADLRoHgyLZxLwm34hxKLz7sC0-uha98vl40HH5H9YVGrYQYITj5RrxWG0QHpK22cz_P-cZgLAg_weDHS_E7NmECMCfgeQg7Wf482C4EygOuauvfW1HK0nc2gRwEWzKCddHZXx-PavfmVS9HH5k6kSM9ixv0uHPs8jsfUeiDJWTRYKIU5LUYJMB2dyLncG9b0IbS-6eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=MsXNJaWQic1bA8XWbnm3tKPu50afr6XcrxR8p52o0alOU5T9444CmD9B70p3eRGzfwgQrjZw4KpPtHnXdLANhZpq74BbEnTyT_3HxQljQaBqnnfWyTgbNButzwjKhPfx3R31HsCgTu22ierADLRoHgyLZxLwm34hxKLz7sC0-uha98vl40HH5H9YVGrYQYITj5RrxWG0QHpK22cz_P-cZgLAg_weDHS_E7NmECMCfgeQg7Wf482C4EygOuauvfW1HK0nc2gRwEWzKCddHZXx-PavfmVS9HH5k6kSM9ixv0uHPs8jsfUeiDJWTRYKIU5LUYJMB2dyLncG9b0IbS-6eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH9y34yYMkbRzhDBJLc-lsgpws_ZAFT3kBKa2GtXK3Czo3XTRhE4zLT51MwOHqGgDjz7a8zIj1DaJzKO3Gxu5Z97aamBroJDs05DoT5KtfEEZsUX0dcHw3oWXrAB9yGqgwCqT2oSIeoB5NEe_nf9sl06uiK3wDBHqwBmz5D-p4tOb5_A_AZMm6Ck54xcIvZBi1TzEYOOpVxYulKmJ-HgEhuvkTZPrFmBvB9xFWeQcMwlUMiHoTBCZJnsui1BIV11cspKyZlwNAqPvlmC2j6rciQxB-BJNuOoiR7tO_5_JU1ba6fhQ-c3SAzitzCD4yHavjv4xV8shHTMHqPQDv_Dig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=IqG1dGt-LFqR26M8w9_rYfYEWmHMVzWgpKZ1F03cl2YttKwG6T7KIumxAJzRILb4AGFwN8c17Fr3nfeL-xgSLIlzrQXXNB5X22lpCkWgVQ7XZmsUnUzoNZE1JQryEPhmkGN2ojK9A_UsHLSBsVLxy7xnrG4ZRMeosM9D6lEtI_RIqgKx4EJcVpF00EmY5efPnG5lT3VI2SOkiaeepOIysmD9QJkRSW7x57nEDbFq-xxc6OU-AF4TSXbykT5fKQdpRH4MNnGBDLzjOoGigTJhlj_AVHVSdm2IiYbXSZclGDYqEA0PxTTOy-CHSF8lipDOhU1fSdt3HYB7oEZ99v2xWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=IqG1dGt-LFqR26M8w9_rYfYEWmHMVzWgpKZ1F03cl2YttKwG6T7KIumxAJzRILb4AGFwN8c17Fr3nfeL-xgSLIlzrQXXNB5X22lpCkWgVQ7XZmsUnUzoNZE1JQryEPhmkGN2ojK9A_UsHLSBsVLxy7xnrG4ZRMeosM9D6lEtI_RIqgKx4EJcVpF00EmY5efPnG5lT3VI2SOkiaeepOIysmD9QJkRSW7x57nEDbFq-xxc6OU-AF4TSXbykT5fKQdpRH4MNnGBDLzjOoGigTJhlj_AVHVSdm2IiYbXSZclGDYqEA0PxTTOy-CHSF8lipDOhU1fSdt3HYB7oEZ99v2xWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=H1WF63kzFXMH7Zuch4R6tET6PXpvmuphmqTtteqyhg8VLMfdKaU8b4_0dVJ3Ilbn7_yp83TWmyg36dY9HoLI4UTZcJs8_gpbBp-rcZMp6JqrsRn6o_DCWujg66cIIFx_lwi8yvzJOUJW_f-np6WnewIGz678wK2E51j56Fq7i1NfkSZDCg-DiC7zR2lhPsw_QdOJwol9GEsEHjkj5OVJNlsKmsIaQAcScojD-lcUkJqtGt-AXaDFjrc7T5H_StUuWZ0znLdsM62IWMBsXBV6UOF5RI2E6gwlVaK3yjfuO0A1S2g18GsKLhntTWEKZGI13a_6JzqHoQgquqcJpY9DDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=H1WF63kzFXMH7Zuch4R6tET6PXpvmuphmqTtteqyhg8VLMfdKaU8b4_0dVJ3Ilbn7_yp83TWmyg36dY9HoLI4UTZcJs8_gpbBp-rcZMp6JqrsRn6o_DCWujg66cIIFx_lwi8yvzJOUJW_f-np6WnewIGz678wK2E51j56Fq7i1NfkSZDCg-DiC7zR2lhPsw_QdOJwol9GEsEHjkj5OVJNlsKmsIaQAcScojD-lcUkJqtGt-AXaDFjrc7T5H_StUuWZ0znLdsM62IWMBsXBV6UOF5RI2E6gwlVaK3yjfuO0A1S2g18GsKLhntTWEKZGI13a_6JzqHoQgquqcJpY9DDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=EUzlUxWV6tB0FHK9g7p7A6peRTj-5AyYsuzwgfg7JlVVmOdaOkuh9oQdo6B7DugCkRFrwzc8Wb9vl9ZYJoxgB-LinsRjsLmGueDBLeYih0AKTXkfJPd8CrTi56mfeJNKq3t8AXpxH3JcDcfDxYBWgUWhd-cWskFBFhyvSqPivwCXxCFAGmq8cdihDpU_s-IgWhs7XIE8w39ZrokTuSLPIBvqfl0zNCMvE8CKxQT5YGEi0O49iyeqtxiwCEF_vHOopFF8piVYU6n3RI2T5r_EsjJ1z-wOw69LlwnWVraXTEoUSZ06IiIb3phT5-nma31PFAy52hiAJzrzDdyrC2PUFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=EUzlUxWV6tB0FHK9g7p7A6peRTj-5AyYsuzwgfg7JlVVmOdaOkuh9oQdo6B7DugCkRFrwzc8Wb9vl9ZYJoxgB-LinsRjsLmGueDBLeYih0AKTXkfJPd8CrTi56mfeJNKq3t8AXpxH3JcDcfDxYBWgUWhd-cWskFBFhyvSqPivwCXxCFAGmq8cdihDpU_s-IgWhs7XIE8w39ZrokTuSLPIBvqfl0zNCMvE8CKxQT5YGEi0O49iyeqtxiwCEF_vHOopFF8piVYU6n3RI2T5r_EsjJ1z-wOw69LlwnWVraXTEoUSZ06IiIb3phT5-nma31PFAy52hiAJzrzDdyrC2PUFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=jfbw3YzJD1dPPH9bcZjb2J7RxiF2oPTp897XNi5Qc_BJ79WN1tNuXd-tlY0N3F1DX39rNtP-B5iQy0Dco6bgg8A6rBR88BfHN4bFnYo7CUslVSJ_McDDroGvY0_sa5La20e2rz2WEJ27UUnniNEaI7n5ZefrVscte4049CYTQXEzCltkc4rJiBCUFej1lnAuQ_IeP8KbW0zohSbtWxm2dJ-tSflj57KPrMbkFhefgmzTxIr2Txr74z3YyVQYTaXrHUsGDxaFFM-blw919ai56nt8rG_jh89vTM8cN6QlEWHYZPhkJ-oY3IaajN1mQkDHNMuv2BzMGBouRkyN_oVcGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=jfbw3YzJD1dPPH9bcZjb2J7RxiF2oPTp897XNi5Qc_BJ79WN1tNuXd-tlY0N3F1DX39rNtP-B5iQy0Dco6bgg8A6rBR88BfHN4bFnYo7CUslVSJ_McDDroGvY0_sa5La20e2rz2WEJ27UUnniNEaI7n5ZefrVscte4049CYTQXEzCltkc4rJiBCUFej1lnAuQ_IeP8KbW0zohSbtWxm2dJ-tSflj57KPrMbkFhefgmzTxIr2Txr74z3YyVQYTaXrHUsGDxaFFM-blw919ai56nt8rG_jh89vTM8cN6QlEWHYZPhkJ-oY3IaajN1mQkDHNMuv2BzMGBouRkyN_oVcGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=jktdt67ttJeJg2ZQ5PQo_-2kG_IGhC8mcJX4BiRAdb3e_JbIixpbO0KHdksRDn2JOewW5C3Qo2By_HMH7nRTmeoB4PTtVhdYzIzf4lCUiwszx0wRhOMOjq8iNmGm6sBpdFuF8P3TJzc-9ar0h5T3THLZI_VFLHyAMTh9ciYVWTQ1g1aKtJrewuX3b_nAiw8gTRBGFun5ZWlVwS73R1tTQjNc1P1yPfedGXMkzgDAghmFbaE4-TIPjHjvz0QSm0LXMXCm9eXWH-Y1C-0Z3SqL3sSqdBr2RJ6I6m-PBjHYlaPajgfxfTBg8ZbcretqL2i1_DpE7YAlGmHSBi-tCuOb7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=jktdt67ttJeJg2ZQ5PQo_-2kG_IGhC8mcJX4BiRAdb3e_JbIixpbO0KHdksRDn2JOewW5C3Qo2By_HMH7nRTmeoB4PTtVhdYzIzf4lCUiwszx0wRhOMOjq8iNmGm6sBpdFuF8P3TJzc-9ar0h5T3THLZI_VFLHyAMTh9ciYVWTQ1g1aKtJrewuX3b_nAiw8gTRBGFun5ZWlVwS73R1tTQjNc1P1yPfedGXMkzgDAghmFbaE4-TIPjHjvz0QSm0LXMXCm9eXWH-Y1C-0Z3SqL3sSqdBr2RJ6I6m-PBjHYlaPajgfxfTBg8ZbcretqL2i1_DpE7YAlGmHSBi-tCuOb7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=VnneqgLjQOms1cxrfHBDq7G9Zfxxi2fzYe1ItVKiA7sHf5csgiRmUF9EP3GKS2BZrIHos9TEZGwmPBamPcsz1v59g8FYQP7Dq7g-7VzO5I-Bp350cD-u3AfMdSq3J1s2MPp7tgGC2wVV2xyfC3KyOeEAKfVtnIfkNU3BFJ5Dgkq3UxJZlQ1oZ5VLSTknwPG-v-0oovZHAeMCYdHG6osc8oDcK1SfRGVFQQ1t8LfZWaIqaEVYffzFWgN9X4USlQtg4p8J48J2hTCQHeMMY4aS1GkfIZX68HVAX_sRS4MLhnuo6BbGa4qTNsGLn02COcPdvPPqulgcCSds7TT6koNMxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=VnneqgLjQOms1cxrfHBDq7G9Zfxxi2fzYe1ItVKiA7sHf5csgiRmUF9EP3GKS2BZrIHos9TEZGwmPBamPcsz1v59g8FYQP7Dq7g-7VzO5I-Bp350cD-u3AfMdSq3J1s2MPp7tgGC2wVV2xyfC3KyOeEAKfVtnIfkNU3BFJ5Dgkq3UxJZlQ1oZ5VLSTknwPG-v-0oovZHAeMCYdHG6osc8oDcK1SfRGVFQQ1t8LfZWaIqaEVYffzFWgN9X4USlQtg4p8J48J2hTCQHeMMY4aS1GkfIZX68HVAX_sRS4MLhnuo6BbGa4qTNsGLn02COcPdvPPqulgcCSds7TT6koNMxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghrOpEMd-Kf4v8Vp3rFm9HQjhtZAvazv-YZHkMJx-1-hXNx_dMK24OWOF-P9Lgn39pEsa_dj8VF_eSFNo2rz4fUPkgNlqAyKT8PB_-F5R5-vUW8tpUj1k_lB-3CNJ01xhoVuVCMcYpvjeO0F_EgL4HrxiLVFqnkMXBFCf2UUyIdZrhOv-9hzTCBOC6nMXFcdbgO84A70g8Zkre5dYqB35LsO5hAc4Lom43SxFGSpCqdORU0fM8dc5oFy1spKfn2lun0f3jwy7c7EfU7l-F084bCKNLlPjjMJLGFMzkXN59BhAFyXeD16o02uCtE3Z4aMRB1O4ykL6AtdZrg8a-o5vVKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghrOpEMd-Kf4v8Vp3rFm9HQjhtZAvazv-YZHkMJx-1-hXNx_dMK24OWOF-P9Lgn39pEsa_dj8VF_eSFNo2rz4fUPkgNlqAyKT8PB_-F5R5-vUW8tpUj1k_lB-3CNJ01xhoVuVCMcYpvjeO0F_EgL4HrxiLVFqnkMXBFCf2UUyIdZrhOv-9hzTCBOC6nMXFcdbgO84A70g8Zkre5dYqB35LsO5hAc4Lom43SxFGSpCqdORU0fM8dc5oFy1spKfn2lun0f3jwy7c7EfU7l-F084bCKNLlPjjMJLGFMzkXN59BhAFyXeD16o02uCtE3Z4aMRB1O4ykL6AtdZrg8a-o5vVKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=b8bwww_B9JHpGrJLg-eWwcHIrcvLIWsL2r-NgLKXJhafjLubD6db2MCZVPAiioyz4U35oMLlw5l2tOzbbK9_V0ueHKUJ796OBMTD0AaFfsi6N-jOGlzElV_yZZS3tMYU8i02-14mwqy0XlHQmJiLYaRmDSrjwjiWck2QLnHhMLWdeDFpkEdGJSgv0gIhk-Ia7C2wuhQPcZOJTs1b2jOU7fA-2ITEJA2btiRuknvaJQqpsNm7EIOEw6djgfKpFiaBmee3TzZmT6tqQD4v5qflZP_DxesHTeAeAbYut3VBrR-_QdfIbYj3tF-V01qy3_Nm4NormvgUzfqdzrcVJ9unqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=b8bwww_B9JHpGrJLg-eWwcHIrcvLIWsL2r-NgLKXJhafjLubD6db2MCZVPAiioyz4U35oMLlw5l2tOzbbK9_V0ueHKUJ796OBMTD0AaFfsi6N-jOGlzElV_yZZS3tMYU8i02-14mwqy0XlHQmJiLYaRmDSrjwjiWck2QLnHhMLWdeDFpkEdGJSgv0gIhk-Ia7C2wuhQPcZOJTs1b2jOU7fA-2ITEJA2btiRuknvaJQqpsNm7EIOEw6djgfKpFiaBmee3TzZmT6tqQD4v5qflZP_DxesHTeAeAbYut3VBrR-_QdfIbYj3tF-V01qy3_Nm4NormvgUzfqdzrcVJ9unqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCNg6lomeJjhsbyBk4A__fAZRI__UT3wbs44A9JnwmAC2W1WVm94v7wyeENZa4hHekaOt13BDYEL0qMFW95cmZiKGFSvY0hPOVugqmcU9926eT5-L9nxh2ZyXBsPOet2d_oyjyp2n2ujpPQ1iEKo40pWQWRD8czDir1u14kY3zGGTyz3fwCFSV6Q-DlfsYndJf0l1avfFjEHdp7wJ3hsR8CWfhNPVewbaxmBDu51oZ2j910cSyu9-CMGQEKXEPcDL9mY95fADl-cV8GQn-N9NFcN1007UdfoFUSDk0mpSUhYh19XR-_P9l2Kxrd4HxXCwt-Ub8VSIxxYD30ki2sxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AVvKJaI0YJDjmgnTXIiSTAQTcceWTXbcNRlmqUdHxyNy6sKBzV-Xd7iTalZ8JR5QJKXi6o1m4NpnXfH4GjonzHFd5Yuyh3wrqqV4SZnDEOQmJVxhWRzaEnBje604u_6tnmtk370kEk6Qw2TG7IUmQuHhJ5S0HSXCH20zvhDCdQHqNRpNw9Aqnhy0KfBy0XYmpBXh4GHc3m35QbA11J2G4H3p3uEZ78noFTIMYoX3FPUDHtBYodjAdGJIKY9Uom6v_yg20FbOFK7ckl7JtUudG1bAVQ-bhBBfisyWp0nYtdcOFOrXGeX4lF2nsKieOU6m14hmz0E3EGoYDp1kaRTdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
