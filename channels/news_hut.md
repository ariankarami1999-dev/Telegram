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
<img src="https://cdn4.telesco.pe/file/R5Ywu0DohZXruQ0yJzGH9O4PAuy9CIvbhT3YBBvSfE2_fsCg-y9CUt53rVbP6LKvptjdAZAnMfIB3aQr4r1emi59zIW-MhztpHfUyxe6s8wEtElw8SJG-7JKAZo_fWzVkDa-gzmdwnoWYNoi0kC51Pm8wit_XlcffCcWsy7P7X6hCPRKCd4d8RkAQpom2rn5m518q30l_AC8ghqMQjvasECczkvCuS4iO-F6HAfGJKER3qGr08MwM32Hb1HGzTDid2z6dWWIsKYm6flHbcnf-YAQJ67SInMI2UfrxsGIHyyck4c4M1d0_YSzTIvVhRIcFct42HbbV1sUVc8HMujfpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 107K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 23:14:42</div>
<hr>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=DxzIw9wcFfUSjCn-FKljniA1a_wxDTeKprcD1cVRqrs6JXTyBRXzaP3ug3XHO-yZQQCNJshoyukRqhQDkb8p3vmRpRAsbepSYTLUXxcy11w4SnXZgUJ7zSVw98Q8JYDw98zRiw_WmJhBCC7H1rAD9ah-S9tnw6tE0BHWv0GDDPW8NAGJ7yzfCHPAIqI84TBtUGHNMOOkOioh_5Tk9JwWGofEE2Vs77eSj5OJTYG-Gf_qA37qNSdustnXBrFe8WRhJFt8BBUtEoz-8bO4_gaUccq-iiFVH2SujlXA8lXuU0eUmmADkoCzRYHnYv_fh6xT96dpkFmgzNnbS3Svkphozw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=DxzIw9wcFfUSjCn-FKljniA1a_wxDTeKprcD1cVRqrs6JXTyBRXzaP3ug3XHO-yZQQCNJshoyukRqhQDkb8p3vmRpRAsbepSYTLUXxcy11w4SnXZgUJ7zSVw98Q8JYDw98zRiw_WmJhBCC7H1rAD9ah-S9tnw6tE0BHWv0GDDPW8NAGJ7yzfCHPAIqI84TBtUGHNMOOkOioh_5Tk9JwWGofEE2Vs77eSj5OJTYG-Gf_qA37qNSdustnXBrFe8WRhJFt8BBUtEoz-8bO4_gaUccq-iiFVH2SujlXA8lXuU0eUmmADkoCzRYHnYv_fh6xT96dpkFmgzNnbS3Svkphozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=kGE5ckojkGscB4XWsPw-FpY_u_6lMor6-BmqWF6E9utAoaKvLd6HY2ho4EwZv3Sea8tpcizDtV09-jgcKgabgJv6YLKahiQXYzGBJy8RfJGkVghfSl9IiszlXjcyuAbpXenszkZTGuBb_-wlhzMHuef7m9kI0vqV0kQ8S4okV7Sldym7Q8bqAsMYqos_KvXJdJPymFmGT6hnaHMY5-H4W6XKbUAJXEE7Rs49AmbaS3Nj08ownaIg9zNZ7Jl2V_y9711bVcFkHwHUJXEHDjp0tW2fS676L5f55fyFnzVId1S2scvVJ9KeoaEA3eyYBpx_JRtwF1K9Iysh8DraMZ-Thw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=kGE5ckojkGscB4XWsPw-FpY_u_6lMor6-BmqWF6E9utAoaKvLd6HY2ho4EwZv3Sea8tpcizDtV09-jgcKgabgJv6YLKahiQXYzGBJy8RfJGkVghfSl9IiszlXjcyuAbpXenszkZTGuBb_-wlhzMHuef7m9kI0vqV0kQ8S4okV7Sldym7Q8bqAsMYqos_KvXJdJPymFmGT6hnaHMY5-H4W6XKbUAJXEE7Rs49AmbaS3Nj08ownaIg9zNZ7Jl2V_y9711bVcFkHwHUJXEHDjp0tW2fS676L5f55fyFnzVId1S2scvVJ9KeoaEA3eyYBpx_JRtwF1K9Iysh8DraMZ-Thw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71685">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/61894edf33.mp4?token=A1J2p_XF-SJeyqNFFHXZ5B_WMrVqrzp7OcGHkA8N3thuk6e3-KnQytW9KzHKp6JsR9f2NzqA05AgawmUkJnzxZ-uVcWuwQxfkkjfV32MIN2_IsCs-EOqdBh5rvgxWBtQelhU9qc8SMDwV8Ot25hsASsi61C8k76vi3mmmzxomEVxBaUahIg3UMxmdGDUoF2E-4tQvlnu2S6RYwBgpeOwUhMOkaBNhVp_Pg74a8D8e7JAc1KqgEoWaJURysNkw9sEiHjEaNyDxtg5WcrhMLZH2Ff-0GpNYHuDsly-HcOIbmhyQG-46UhpmEvVSgYOsmlnhtDQPpCHQyn9qceTi1yOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/61894edf33.mp4?token=A1J2p_XF-SJeyqNFFHXZ5B_WMrVqrzp7OcGHkA8N3thuk6e3-KnQytW9KzHKp6JsR9f2NzqA05AgawmUkJnzxZ-uVcWuwQxfkkjfV32MIN2_IsCs-EOqdBh5rvgxWBtQelhU9qc8SMDwV8Ot25hsASsi61C8k76vi3mmmzxomEVxBaUahIg3UMxmdGDUoF2E-4tQvlnu2S6RYwBgpeOwUhMOkaBNhVp_Pg74a8D8e7JAc1KqgEoWaJURysNkw9sEiHjEaNyDxtg5WcrhMLZH2Ff-0GpNYHuDsly-HcOIbmhyQG-46UhpmEvVSgYOsmlnhtDQPpCHQyn9qceTi1yOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، هواپیمای تهاجمی A-10C Thunderbolt II نیروی هوایی ایالات متحده، مواضع داعش را در نزدیکی «جبل‌العمور» در شرق استان حمص (مرکز سوریه) هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71685" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71684">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1QdwUeNvTTaRd3l3W-AxIG5ONgTFoAAR_xEPvclStGG6YgNdKClYSJ8-xJqNLF8e4hvfPKIB2ZEHrzxYeJnFuhYxH9LX4Mu9o4TPxDe9qbxpW2LpAjkUyAH_8rcWnygumXkttijTPA_D5s-7Xjy-lrXgCYnP3dWownPIYOPuZqPKxLiQ5GVEeCvws40JjfjH7TRry8dIsZMijmBMQJKggPtYrJcB6epoha0YKTLcLCC5nEsiU6UI0gRcbB8nHIyK-OsohJaPhytGDDonrm37beHT59l1vkJd6r6TA-t1tz4VuiwBirr_9dieGknVXNg0lgwm9PYNL2hWomvCw2t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست:
دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از انواع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است؛ این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود که هزینه آن از محل پول مالیات‌دهندگان آمریکایی تأمین می‌گردد.
این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
این قرارداد برای تصویب به کنگره ارجاع می‌شود و می‌تواند آزمونی برای دموکرات‌ها باشد؛ چرا که در ماه ژوئیه، بیش از ۱۰۰ نماینده دموکرات مجلس نمایندگان به کاهش کمک‌ها به اسرائیل رأی داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71684" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71683">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=YWVDJPkUdkbI1-FNut-9vghZJYcvmIyhgFX3sv8gJFhnnvAwUP9KYKqsQrfMZzFoErVyHTu1oPsH3WHncyktcyp3AnRm5OehlxLTZ2dZwpH8fcwsTbuBCqii-nTdOkn4kj5cxCQfCfCVVWA2_fNV546oQGS1y4w3j9SKjn7R1AkVe-HSr5WToetLedE2ARanfdkDAGheuuz4cm5heW3jFhBNI98kz--c1NNQkoaVqWazuh5KfPwGnTSjVTQl8ouLG_nHZuSgWCL4bksg5S_NnLB-qOl-Hor2F4ziCokF8DYarONutkGRzm2jLJxcLQyksKzurNDn7lNZuPcxntwBBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=YWVDJPkUdkbI1-FNut-9vghZJYcvmIyhgFX3sv8gJFhnnvAwUP9KYKqsQrfMZzFoErVyHTu1oPsH3WHncyktcyp3AnRm5OehlxLTZ2dZwpH8fcwsTbuBCqii-nTdOkn4kj5cxCQfCfCVVWA2_fNV546oQGS1y4w3j9SKjn7R1AkVe-HSr5WToetLedE2ARanfdkDAGheuuz4cm5heW3jFhBNI98kz--c1NNQkoaVqWazuh5KfPwGnTSjVTQl8ouLG_nHZuSgWCL4bksg5S_NnLB-qOl-Hor2F4ziCokF8DYarONutkGRzm2jLJxcLQyksKzurNDn7lNZuPcxntwBBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از نفتکش «ال‌گایا» (EL GAIA) پس از اصابت به آن در بخش جنوبی تنگه هرمز منتشر کرد.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که ایران ماه گذشته با موشک و در پایان هفته جاری نیز با پهپاد به این نفتکش حمله کرده است؛
در مقابل، ایران مدعی است که این شناور پس از ورود به «منطقه ممنوعه» در بخش جنوبی تنگه، با یک مین دریایی برخورد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/71683" target="_blank">📅 20:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbKAAWY07A0k3HPbI7Ge3exU-lxhjPjeUeqPv8SskLIR4oZVw4bK3qswcHXzufopv6DxOZuy7vBTUBHRaBlZ6LbtjQORVqyurUD-DOOzoGzVEdVNZUGYkyzNFov2R05XMILqk8t8lEFMAWpVjkvLnM9VDzPUgXIguX9upRoa1lOmG3y9FU2P1IMXfuNd8caJjtQS4uRFwbwXUCweCRFtmsJvC8s46j66RZA0UDwBLd57IXHnnWIqe8qCeDHplFjj9glORTUeDzmX17IijD2lsSXTllfeb12_F-d4-Q6_mvdewOY0pqIlW6a8JgbukN3txVBI5Fwk75eHVOk-e7Jg5lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbKAAWY07A0k3HPbI7Ge3exU-lxhjPjeUeqPv8SskLIR4oZVw4bK3qswcHXzufopv6DxOZuy7vBTUBHRaBlZ6LbtjQORVqyurUD-DOOzoGzVEdVNZUGYkyzNFov2R05XMILqk8t8lEFMAWpVjkvLnM9VDzPUgXIguX9upRoa1lOmG3y9FU2P1IMXfuNd8caJjtQS4uRFwbwXUCweCRFtmsJvC8s46j66RZA0UDwBLd57IXHnnWIqe8qCeDHplFjj9glORTUeDzmX17IijD2lsSXTllfeb12_F-d4-Q6_mvdewOY0pqIlW6a8JgbukN3txVBI5Fwk75eHVOk-e7Jg5lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=ekkFnccnzeMli2rfOysqx3Zva1OoJCiqNFhaldWO8ioEi6FURRzBZN7b3-cV8lwgr1cwUw_VKTTEpliermRjfyNzV_stlZlpLaNGAD-rzMp8kOHrjWQF-HGGOIEfR_g57bNgFmmUY-EQGDgC89-7MReOXvptp2wx_qzV0YEC1-XQ7nqSej-P5rwZSsstJL823BRVqKdwowDI6HUtLz3Pg8-mr-s67ZPQv9TCEjKl-VofHGQdSgJtDw0oFWYlAm1zsMZYA5vypKyp2a7VwKEV3KybW_1Yi-hKUTsY4MA1-iM0IfgOjhMhPoxwyJKY1PfwUpr_ujyHuRI-Y26TP_eFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=ekkFnccnzeMli2rfOysqx3Zva1OoJCiqNFhaldWO8ioEi6FURRzBZN7b3-cV8lwgr1cwUw_VKTTEpliermRjfyNzV_stlZlpLaNGAD-rzMp8kOHrjWQF-HGGOIEfR_g57bNgFmmUY-EQGDgC89-7MReOXvptp2wx_qzV0YEC1-XQ7nqSej-P5rwZSsstJL823BRVqKdwowDI6HUtLz3Pg8-mr-s67ZPQv9TCEjKl-VofHGQdSgJtDw0oFWYlAm1zsMZYA5vypKyp2a7VwKEV3KybW_1Yi-hKUTsY4MA1-iM0IfgOjhMhPoxwyJKY1PfwUpr_ujyHuRI-Y26TP_eFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=dq_SlCtrwzOnbZxUSB8-kPNKTiK7G3eJvyaNA2KXDTZ8NpcnbL5Y50Dbx4hkJjmP7Zl5hdm_IlrmUMjIsoYSmXgzihjpBHgx7lsS72QQY2oXjQ72pNQVbPeTqBjfY9b-jqNP580Pg6WWFR7rWQgc6wphCFbD9vFKowE12hdE_F-W6qRA2O7b2duzcxGgt5_EfjGAa-ZBfd-7TyMo_CZnePPZDfRCpqjNpYsCBM2QJDJ49OO1rfWaYH6Iy2IEvD2_BGczAQRsx3jrKTNLB7_GER9hRryhSpDrSWHqK3U6vgUKCjyvtYGBm5hcibdg1TI0nkTmXA7dwomPhdHDb47u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=dq_SlCtrwzOnbZxUSB8-kPNKTiK7G3eJvyaNA2KXDTZ8NpcnbL5Y50Dbx4hkJjmP7Zl5hdm_IlrmUMjIsoYSmXgzihjpBHgx7lsS72QQY2oXjQ72pNQVbPeTqBjfY9b-jqNP580Pg6WWFR7rWQgc6wphCFbD9vFKowE12hdE_F-W6qRA2O7b2duzcxGgt5_EfjGAa-ZBfd-7TyMo_CZnePPZDfRCpqjNpYsCBM2QJDJ49OO1rfWaYH6Iy2IEvD2_BGczAQRsx3jrKTNLB7_GER9hRryhSpDrSWHqK3U6vgUKCjyvtYGBm5hcibdg1TI0nkTmXA7dwomPhdHDb47u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crMEWfHuMyOHXrfUtnN81NGw5j9cc6FzdekykFE8CaKEfBx-fOXUyPKmsxrPlh6Wxu1SO6D7TwGwAJ4NGTus-dSFZwNfSYXq2Wje8UiubCX4_i02UOGM7ZCTrcEevJTQgqs6SUmDf4HQPxCeZKFg1RPSXXdJNynghfLw116kPVswdTBdm4pAIema9czlF98Eu6s9o3g7A_AGwGWjmvM1BnB3ShLRYVTNpXbYobEpkBbjoYRyBvvPJQFwRExHmfIW7re7Zxnq_OD8Y_fpQQ1aihg6eFXoO9gz9cJHPN4nJeLE-Sx_SZg6beKrcodVYWTRVtYYM99v_p4gR6n2O9rUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=ZhwmMuxNIs8f28Pv_vuZbiwfuoIQ-7Hcd6fZLsANNWV75tZ-lqpJXDUOrW1x48O8l3uq4Mw0d25SG45RrU1oXgXLvso6BGqHCq7mKEEuW-WqxRULfStpu1h4orwm5mxOsJvcSdnbs1K8sjwfOetDjUHo_wSxnhvY70sZpnStlkvLNkyKhoqPQjbezpFIrUmqbS-CLsJVha_88oLM9EbiVjBxO-tjWDNBBPEiPsRAyz-vOHiml7pkcpLg7xPejydI5aeG_uktdLW_RVuJeunvKh3g2M_rKs0TbIidZtvDfkynfer4TA305e6qYhZ3iqw0_IfyECj-v5_IDTXE6JVZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=ZhwmMuxNIs8f28Pv_vuZbiwfuoIQ-7Hcd6fZLsANNWV75tZ-lqpJXDUOrW1x48O8l3uq4Mw0d25SG45RrU1oXgXLvso6BGqHCq7mKEEuW-WqxRULfStpu1h4orwm5mxOsJvcSdnbs1K8sjwfOetDjUHo_wSxnhvY70sZpnStlkvLNkyKhoqPQjbezpFIrUmqbS-CLsJVha_88oLM9EbiVjBxO-tjWDNBBPEiPsRAyz-vOHiml7pkcpLg7xPejydI5aeG_uktdLW_RVuJeunvKh3g2M_rKs0TbIidZtvDfkynfer4TA305e6qYhZ3iqw0_IfyECj-v5_IDTXE6JVZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAkNQmCT4ANharl8wCrNIyeR3ZXziJ__c5YCKiTIgaoikeLnUE-kXTEOcWIsraZV4XVNBr7vJi3dMXt8QDKRuZr3L1UyZBkhiUuT50L0s6lp4temXTEukvVJlg5AVacpAVD9mlbptzjxLEJNmxwZR3Z43dOyQJiBqpiFHv1twCl5wgfHpK6FY0WdEi3J8SAjukbxWgjccKdAGuGou0m_Bu3ZA3G_htIs2ZzO3cCgsl1H2rvBxi-jmaaDJhKR21DsefQ2gI3QQoxF43IYVolkFF3x07ko1He9HweWW53wVY78FNRx2e5tL-REM5McIs7IYm2Cf84jQL0ZWWOb6-qT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=ip7hYvmURuGxFaJU-GwLNcKUAb0roSU1IWvm6GaY1hfWRNSbsY8RFUYSPhfB2eHZ1WCxs9Tol1pCsPLuAIOQnUkN8YkcP9YI3jyt6ljjM_9eFvE283TKd0LsfOVPch7zRmoHSh-uf6MApXCZtGIQk0299RPBk9_tely6bdmQyDY9J-S6rrjpCmsasWdvOt6mh2m9lpOIm4TIZuc4fmsyHmHP8XRYSX9VCHdP-ODbNk9zuvliJcDbXVQnuAGzvkdHd6qO5pH8jSqi-xOj6Ki_fmSIMSdGRfaAk16u6ABfCULQRcpVDIVtBi1h2y5yEX4kv2XHrLPx8narIjt97b2P8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=ip7hYvmURuGxFaJU-GwLNcKUAb0roSU1IWvm6GaY1hfWRNSbsY8RFUYSPhfB2eHZ1WCxs9Tol1pCsPLuAIOQnUkN8YkcP9YI3jyt6ljjM_9eFvE283TKd0LsfOVPch7zRmoHSh-uf6MApXCZtGIQk0299RPBk9_tely6bdmQyDY9J-S6rrjpCmsasWdvOt6mh2m9lpOIm4TIZuc4fmsyHmHP8XRYSX9VCHdP-ODbNk9zuvliJcDbXVQnuAGzvkdHd6qO5pH8jSqi-xOj6Ki_fmSIMSdGRfaAk16u6ABfCULQRcpVDIVtBi1h2y5yEX4kv2XHrLPx8narIjt97b2P8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=sMVlULXfSiGxf5YD8DqHByav7aHyngq6B4szgeb5cg8C5rPAqt8o-r9-VistBpYzKQXVY5y3rgyMj1aVeJ0uJlg6Mm0NIt9ncjze47bUyYKx7rHu8lIwthjexR86zVYcbZ8zdjQ2Em4OhEYxbXnkHqQOmuujIgNKD-wRHUu_gkoBk9oS8l5Dw5GwutVi2lQl0nRPgGDHCaD_pEcfFbcXe5wCt-SZWHBf4Zd4RZjtO0PqAoAhHweCE7KNCuN4UO1yqsnMrGKwoojr0oQ7eY1DyNrvFRQZN2kaxPdr1xQFB3lZ-Q_hNw-EZ-nL4COJSE9-1lGjEYpFOJIvcg6GdrRl_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=sMVlULXfSiGxf5YD8DqHByav7aHyngq6B4szgeb5cg8C5rPAqt8o-r9-VistBpYzKQXVY5y3rgyMj1aVeJ0uJlg6Mm0NIt9ncjze47bUyYKx7rHu8lIwthjexR86zVYcbZ8zdjQ2Em4OhEYxbXnkHqQOmuujIgNKD-wRHUu_gkoBk9oS8l5Dw5GwutVi2lQl0nRPgGDHCaD_pEcfFbcXe5wCt-SZWHBf4Zd4RZjtO0PqAoAhHweCE7KNCuN4UO1yqsnMrGKwoojr0oQ7eY1DyNrvFRQZN2kaxPdr1xQFB3lZ-Q_hNw-EZ-nL4COJSE9-1lGjEYpFOJIvcg6GdrRl_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=AU7qe3XrZunjlX5bRnW_hjE6_KqiXRil0xuqneQBSxgbB-OJGmF4p2a_PYp2aYNqKLsxWngYX6RZTmEuUSNq8orRRYxpmA3VPnaHo7Q-UXGS2wjpy5hYMKlxNPuZcBxd493nkINXS1yrvnmE4dI24V7ADNET8s_XVg_g2yiqfAEmev-d2snk5nEM8eE3jg-q7YpmCWZM5DoUGtlwVvoMrI81auJNanuLQBD93xAdKrTxBJhVH1r2R69N3HyWp9GWQvkegSs0fK22SLHAt-bkuBZ3UNc3zvq9130kfN4UKaBTU4Obg8YKCbV4CALEJhbiKrXwLGb6xsxRdHlJI6Q7tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=AU7qe3XrZunjlX5bRnW_hjE6_KqiXRil0xuqneQBSxgbB-OJGmF4p2a_PYp2aYNqKLsxWngYX6RZTmEuUSNq8orRRYxpmA3VPnaHo7Q-UXGS2wjpy5hYMKlxNPuZcBxd493nkINXS1yrvnmE4dI24V7ADNET8s_XVg_g2yiqfAEmev-d2snk5nEM8eE3jg-q7YpmCWZM5DoUGtlwVvoMrI81auJNanuLQBD93xAdKrTxBJhVH1r2R69N3HyWp9GWQvkegSs0fK22SLHAt-bkuBZ3UNc3zvq9130kfN4UKaBTU4Obg8YKCbV4CALEJhbiKrXwLGb6xsxRdHlJI6Q7tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=I3ko91kt1zMYZVdHDZabnWM9I-XJ2R3J4ilLY5VN_yvXZL3nkAkfEmeAZeOvUmB_oAJ7e4M10Wwonwli_Jqy2b0quZM1krwAUQvkNUyT9NL4GMFXnRahpCawD9vnknhiRXNroy-w4gqQm2qdpID2k80sprUUjdZW1su4PP0w8hg3g9ytRa02AwLoGQYLzy34psHdZ0vNywfd_aX8DRO_ordLk1-2MN0R9pbF8AiXG5MnU68HB4tcB7sA-y9Nclx8q1y4pnRWyc4i56icY6mlj-0QumgkG2AfuaRnH-F7_ixLE9fUx96CnUFBuMfS-CRdE6n_bECNkTyzvevsZyUBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=I3ko91kt1zMYZVdHDZabnWM9I-XJ2R3J4ilLY5VN_yvXZL3nkAkfEmeAZeOvUmB_oAJ7e4M10Wwonwli_Jqy2b0quZM1krwAUQvkNUyT9NL4GMFXnRahpCawD9vnknhiRXNroy-w4gqQm2qdpID2k80sprUUjdZW1su4PP0w8hg3g9ytRa02AwLoGQYLzy34psHdZ0vNywfd_aX8DRO_ordLk1-2MN0R9pbF8AiXG5MnU68HB4tcB7sA-y9Nclx8q1y4pnRWyc4i56icY6mlj-0QumgkG2AfuaRnH-F7_ixLE9fUx96CnUFBuMfS-CRdE6n_bECNkTyzvevsZyUBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71669">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=o7ZfIASwl0ZECb3I2i4WvV9lcCrTRmNWDU1jJDyfNIcCimUWP9NBNIjXheZIgHHL9d8fvRMCVR-_yjKaELghGHim7wIFpgt-OjYz_LBJgZhvvRPSXabhYXPTi1X_sIeuMAbYI3FHSTaUMF2UwnPHMA-ccmVtlhKcnoHgEtDIdVsyxudvGD9o7QQYr1DXlOO3447BZzy9j4Q9XIuADJTIaIYZnuAUFP6lnaaR7OgPbHyiuKVkcPClhqfmNRmtUBrZKK2mA07qTCM3yi4ezErF9T5uWKDOAJiU4xznjoAydLDX9jaofb_Mkg2ty4aq5uf1zV414Wj1zlSRmB4jHbtAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=o7ZfIASwl0ZECb3I2i4WvV9lcCrTRmNWDU1jJDyfNIcCimUWP9NBNIjXheZIgHHL9d8fvRMCVR-_yjKaELghGHim7wIFpgt-OjYz_LBJgZhvvRPSXabhYXPTi1X_sIeuMAbYI3FHSTaUMF2UwnPHMA-ccmVtlhKcnoHgEtDIdVsyxudvGD9o7QQYr1DXlOO3447BZzy9j4Q9XIuADJTIaIYZnuAUFP6lnaaR7OgPbHyiuKVkcPClhqfmNRmtUBrZKK2mA07qTCM3yi4ezErF9T5uWKDOAJiU4xznjoAydLDX9jaofb_Mkg2ty4aq5uf1zV414Wj1zlSRmB4jHbtAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر زنِ مجتبی خامنه‌ای:
مجتبی خامنه‌ای با همسرش سریال " فرار از زندان " رو مفصل نشستن دیدن و درباره اتفاقاتی که داخل سریال افتاده بود هم صحبت میکردن.
یه بار تو یه جمعی گوشی یکی زنگ خورد، من گفتم این چه آهنگیه دیگه؟ که یهو مجتبی گفتش این آهنگِ یکی از فیلم‌های کریستوفر نولانه دیگه، چطوری نمیشناسیش؟
‌
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71669" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71668">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hizZnXTmJ3TpkH-MsNYy6bwmkbpfGq5WCPQwAvHQ1IdDO66IzVty6I0d7XKBzka5G5AcJodh5s-oqbtovn2fPc7wtIhdRxIuQBgOdhLGaSh8tcT9DpobEwP6ahMfTFLKQ2hRh3wvNHyMtytRP9QyvSjNLlMZaZBZZXRimHeNI6w48f5DW7JUKrfjov-QUw3bLwzYzo0H9rQKi0aNK3A1RpCdPTI1QavR6so4BebY4_gaTj26PSW58C4iJ4-6GYnUJzrIWzv1X0KGGy4d9gnFhD0g3TwcLoI6d4gaGYc7CV0MmAsoUmyL4NiPxe12aAnwl3C9PBguY-8fR5R13srDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی:
«نشست عمان» با حضور کشورهای خلیج فارس برای تثبیتِ مسیر تنگه هرمز، با نقش‌آفرینیِ جدیِ آمریکا و برخی از کشورهای حوزه خلیج فارس فعلا لغو شد
عربستان» به بهانه اصابت خط لوله‌اش و درخواستی که از پاکستانی‌ها داشته تا ایران را راضی کنند که به انصارلله بگوید از فتوحاتِ جدید عقب نشینی کند، «بحرین» بابتِ ناراحتی از جنگ رمضان و پرتابه‌‌های متعددی که بخاطر میزبانی از زیرساخت‌های نظامیِ آمریکا در خاکِ کشورش دریافت کرده و «امارات» هم بابتِ اُفت جایگاش در آینده‌‌ی منطقه در صورتی که مسیر جدید تنگه تثبیت شود، در نشستِ مهمِ عمان شرکت نکرده و کارشکنی کردند!
ولی بازیگرِ اصلیِ لغوِ این نشست، آمریکاست!
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71668" target="_blank">📅 13:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71667">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حملات موشکی/پهبادی حوثی های یمن به مکه، طائف و جده عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71667" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71666">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTMmgLqweKFXh4V8TDByf0C3ghpnaYO3yoQlU-EB57QNISxUXtB2zj6VVlOii3i4KjzDHOqUeG9rD4xRyE-k6GG1ZkgciTzr3qVkSiEuIIHCrxlQl081Sopirj0JEx-6L8xC4zgDF6K-Z1_2fWt0acuwKG6B2eVW88vKtvq1fqplqXgnmpj3ssCFC7zbNw5_54SClVwu0mXF_03PIAF0pFTH5LsCTsSAtebNStgv3I1xarRtP7TPJ1Pe-oepCegOCgnVV3N4nnCRqgxQT88LSd-BvzmOkU8JsnGr9Yl9HsUEaj-0WrJeomwxw7L9oPCb8RP5yWLRNu0n39HSZ6724A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) :
گزارشی با تأخیر زمانی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع موثق گزارش داده است که شناوری مورد اصابت یک پرتابه ناشناس قرار گرفته است.
هیچ‌گونه خسارت یا پیامد زیست‌محیطی گزارش نشده و مقامات در حال بررسی موضوع هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71666" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71665">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=pArkhTMapF2y-Bjb6PdgWHU9RNcmhcVu-2ZmYRVmPIlawipYCN_0GYtWO8NOEWSoMxtpOMU11Wn5qKCawzWEqMiAgzcAzyCmVLTg8EYGEa5MA-2OMbz1a81zAsC4Q8h_jqR8dpkPAU06glmvHzh0LUi3HUYFbAf5IjMFvSAviXWSS0Jw9WJp2Pr-ir3Al1CAQK_LHMHhbXxDl6XwjpT2nkmXd35ffCceNcQz3udjwjST48dHIovs_TUZrsKxOZ73XZxuJzxVNA7Ib7sinILjJTG50-w_2nT5FzvFV9cpAx1u9HXHCOe-Jp6DU4pppAku9zyV-IThuD-rgqQrzymdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=pArkhTMapF2y-Bjb6PdgWHU9RNcmhcVu-2ZmYRVmPIlawipYCN_0GYtWO8NOEWSoMxtpOMU11Wn5qKCawzWEqMiAgzcAzyCmVLTg8EYGEa5MA-2OMbz1a81zAsC4Q8h_jqR8dpkPAU06glmvHzh0LUi3HUYFbAf5IjMFvSAviXWSS0Jw9WJp2Pr-ir3Al1CAQK_LHMHhbXxDl6XwjpT2nkmXd35ffCceNcQz3udjwjST48dHIovs_TUZrsKxOZ73XZxuJzxVNA7Ib7sinILjJTG50-w_2nT5FzvFV9cpAx1u9HXHCOe-Jp6DU4pppAku9zyV-IThuD-rgqQrzymdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبه ناو سپاه با عنوان «رودکی» که در جنگ ۴۰ روزه منهدم شد در حال غرق شدن است. این کشتی تجاری بود اما به نظامی تغییر کاربری داد و گفته شد هلی‌کوپتربر است اما هدف حمله قرار گرفت و نابود شد.
در جریان جنگ ۴۰ روزه تقریبا تمام شبه ناوهای سـ.ـپاه و ارتش از بین رفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71665" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71664">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71664" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71663">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvU14PhTcthUwSwA4yy-3VWggmBmELpZU6jtEyVSUm65EvWH3jLslntFY22OcxKcLaEMMIR7Ay3Hw6lCAnt9GYC4i6z3bZXb68OY8hHEDOuEqMYtOK-zDXkJRi3OclDapcgPa7BwtmkY5r7Dh_77Fgp7BMDa2p-iXPcCLEX0KU6TNN9mqdLJANy-Vwz86z9jO8yPiADVzzICOmKjom0XTN1GgFOTo0BAkbFMBAu-Q1vQX4PREx3fB68DU-acxLvU1bayi2RU6g-9VUM_45DB05hbDkkjSODJ3Hk6VQUxdcidXjRwPktJR4xB1Lol0gAGozQTfUv6Y-AHWQR_RE8NBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71663" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71662">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FT9UxbGmOFFF6HRBCFSyUrBQiDOFdVa8p7eujWaP0zHhwziMedVV2Kj68dLTEqL2OwT1Jge-fURVa3S-t7oXMyVuuo0IyCAZ2AThrkdhOZRXv2BDtjip0pQZ9d9fkJXZXZPNvUydDmR07MshhsqF-ghCiL8Wg1M1cciGhqBjXOCNeOLT81EeGc6d2buJzwLQnk60Vnzy5YCcRUt0_Q3soeK8fcUJhDS3AAD9CQeve7iufYuJXIflpvx37YsvkRAI3UA_QyPE6FFEkklfYh7BDtc-ShOsj0l5JZCJWpGPE3Uz6PXHp0AeRayITALhbKyOzVo2g6gcYhAhCJe_3hXDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71662" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71661">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=MsmvV8clz14we2K0XWH7XZAB_QC4lBU0B2axfos8qxsfK6M0SmDa1OezZYHOfWLQFgNg5adk0rVkm4n2cupKqkJ4ja-zcJuQ8AaS80bR3GN5-5J36zzRU3dvKiaFAm1ACzmzhBQGzQh8chMg3ifHj8xGD-F1g2FkKHqC1Mcis77dvWpWxS3TQNZ83L-Awur2UgmBkdsp2NA1DC1VShHV_Pjt5Zyj7K3qks0cIghxmrSu3u0ydSa0fOvYB2AV1vtQ5pMrFxHKzYcn4KwZtj5HisoCFJbsjJVMenBTL8m8U3oXOBxDV6gmI0GgDx204dn7w-uduQ0ky-Lq3xIgZhpW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=MsmvV8clz14we2K0XWH7XZAB_QC4lBU0B2axfos8qxsfK6M0SmDa1OezZYHOfWLQFgNg5adk0rVkm4n2cupKqkJ4ja-zcJuQ8AaS80bR3GN5-5J36zzRU3dvKiaFAm1ACzmzhBQGzQh8chMg3ifHj8xGD-F1g2FkKHqC1Mcis77dvWpWxS3TQNZ83L-Awur2UgmBkdsp2NA1DC1VShHV_Pjt5Zyj7K3qks0cIghxmrSu3u0ydSa0fOvYB2AV1vtQ5pMrFxHKzYcn4KwZtj5HisoCFJbsjJVMenBTL8m8U3oXOBxDV6gmI0GgDx204dn7w-uduQ0ky-Lq3xIgZhpW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: آیا قرار است همه ما تا ۱۰ سال دیگر بمیریم یا نه؟ موضوع بحث همین است.
ایلان ماسک: خب، متأسفم که باید این را بگویم، اما همه ما خواهیم مرد.
مجری: می‌شود یک بازه زمانی مشخص کنید؟
ایلان ماسک: بله، نرخ مرگ‌ومیر همچنان ثابت و ۱۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71661" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎙
صحبت های این خانم درباره سگش:
خرج ماهانه سگم حدود سیصد/چهارصد میلیون تومنه
😳
روتین روزانش صبح حدوداً ساعت ۱۰ بیدار می‌شه، یعنی صبح همه رو بیدار می‌کنه. بعد تا ساعت یازده که می‌شه، یه مربی شخصی داره که میاد می‌بردش یه جا مثل فضای باشگاه.
بعد هم که ساعت سه و چهار غذاشون رو می‌خوره. پوستش حساسه و یه سری شامپوهای خاص داره که ما همیشه می‌زنیم.
شب‌ها من یه دور پیاده‌روی می‌برمش و بعد هم شامشون رو خودم می‌دم.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71659" target="_blank">📅 11:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=U5Cf3bttInFollQLRlPgawmke740xKZRZNCuaTn_HcSNX2kpJo94wJCClsThAR7fhYUbIwaOk-tnWua3B1XmXqlJS3aaV5CR3JnLpNOXDXFtJhGmH3WVrKEaBll1D61PzSJ1tLyvZqdl0FK3FpKBnU09hsJ2IJoRIU1pNhV-ja7Jp-BMkW-Iy9Ul2-DFhvaunowIVc00Aee2PH9s1lOGFsCnM3dfdNuMfjAZGGPMbsaqLmweGMWYfKx-VP5LLrDuDVDuZsJzq0qt-zINCS3BtewFCeOG_-hm8fK01qu0hT9XbZp73woCIbjqGpvOcPYTOinfPameKK65GOXx1rW1jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=U5Cf3bttInFollQLRlPgawmke740xKZRZNCuaTn_HcSNX2kpJo94wJCClsThAR7fhYUbIwaOk-tnWua3B1XmXqlJS3aaV5CR3JnLpNOXDXFtJhGmH3WVrKEaBll1D61PzSJ1tLyvZqdl0FK3FpKBnU09hsJ2IJoRIU1pNhV-ja7Jp-BMkW-Iy9Ul2-DFhvaunowIVc00Aee2PH9s1lOGFsCnM3dfdNuMfjAZGGPMbsaqLmweGMWYfKx-VP5LLrDuDVDuZsJzq0qt-zINCS3BtewFCeOG_-hm8fK01qu0hT9XbZp73woCIbjqGpvOcPYTOinfPameKK65GOXx1rW1jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب علیه روحانی در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71658" target="_blank">📅 11:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوباره آمار مبتلایان به کرونا تو کشور داره می‌ره بالا، خیلی مراقبت کنید
من خودمم دو روزه به شکل عجیبی گلو دردم
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71657" target="_blank">📅 10:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840407be05.mp4?token=LQfz4lvZN9mIcNIadPFhcJEP15PA86OnRF9rapaPiF6Rzd4JvgXrkOO-7LnO5MdzPHks5PYNJ1AUtesnrX2f3LStSqsH_2qJP-wQ4YiBSv9ajrv3paYwWlS4MkX01ui9jexOwrWcYuDCwoF3GvX9PZdBDsQMLZRTGFf8hHwahmu7RvEiOrfaBC4YRbH4kpylRFPWGlaHyDMq6dIcE58iKiYy1PRG-idKegSA3vaMQEEAapXb5X9OC_AupAEucHrf44E1sfUDI5JULnfJhgJKHKAN-gF4kxHK0Cuxw6h-AxpFrndFU5Bmf61sgpg5wrL081bYx8tfZI408NULBdCevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840407be05.mp4?token=LQfz4lvZN9mIcNIadPFhcJEP15PA86OnRF9rapaPiF6Rzd4JvgXrkOO-7LnO5MdzPHks5PYNJ1AUtesnrX2f3LStSqsH_2qJP-wQ4YiBSv9ajrv3paYwWlS4MkX01ui9jexOwrWcYuDCwoF3GvX9PZdBDsQMLZRTGFf8hHwahmu7RvEiOrfaBC4YRbH4kpylRFPWGlaHyDMq6dIcE58iKiYy1PRG-idKegSA3vaMQEEAapXb5X9OC_AupAEucHrf44E1sfUDI5JULnfJhgJKHKAN-gF4kxHK0Cuxw6h-AxpFrndFU5Bmf61sgpg5wrL081bYx8tfZI408NULBdCevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار شده 240 تومن؛
همون لحظه صداوسیما:
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71656" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71653">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=AMc4MXCdCeLWqn8-9plkZyPfo2eY9YtVDiM0UVHO4RM6ooVy-Rhgywfpo-I0Ax9F_Yq3X70DYIQsMgpmviw3K8Hc1rfie-8OGBAzk-hAq1jj7wKlJ77biODBkMSnqlue1oKyrAaOCw4iTQtGClKpUsBkZc6USh9ggZPCvM8eaNfreZJTgJ8phZhixZiFk73V8-kIayQhnyhBuh-2i9-LVvK3ojNkFFYuZ-jZ1t4IZign0yI4XejWNEoArXpRhvSpllB0aH27NT1suJ8bRFW4yz5dmpcsAOPmnjmBAsrjspiTGfViMJ6FVBHEmKrRB48bhs0VIYqNPzMs1pwVW_53jaOD2YtR-7ZPKUYvc5_WKTlTvMuPWsSzkoEStIG16mFlYY59jwxPfde5N0XPefvWcKl8s_mMXZmXlUEyTG0HFjFmJAUgvYjy1EacpPf__bro4wonVlgNudEF2KWkc16lhxuyUEbDF9Eblm9iFyajOxJca3WOPWGErkVo4CG9OHdXhA_LTXmB4DlddRfYjh7T5ASHsK2B7ZJT0o9hUbyUHcV26I3SCzEx9SFsBjK-nQ1UlW6S6OAegWmvucZw_Bpwst2JjbeW2dWnIicNWCO1k7c29Y2NLrZHa8rZYLw8GwGJBPl5jRt_I7JO_RkDL46Va-emPLc2NzQoWIPuhHuC3TU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=AMc4MXCdCeLWqn8-9plkZyPfo2eY9YtVDiM0UVHO4RM6ooVy-Rhgywfpo-I0Ax9F_Yq3X70DYIQsMgpmviw3K8Hc1rfie-8OGBAzk-hAq1jj7wKlJ77biODBkMSnqlue1oKyrAaOCw4iTQtGClKpUsBkZc6USh9ggZPCvM8eaNfreZJTgJ8phZhixZiFk73V8-kIayQhnyhBuh-2i9-LVvK3ojNkFFYuZ-jZ1t4IZign0yI4XejWNEoArXpRhvSpllB0aH27NT1suJ8bRFW4yz5dmpcsAOPmnjmBAsrjspiTGfViMJ6FVBHEmKrRB48bhs0VIYqNPzMs1pwVW_53jaOD2YtR-7ZPKUYvc5_WKTlTvMuPWsSzkoEStIG16mFlYY59jwxPfde5N0XPefvWcKl8s_mMXZmXlUEyTG0HFjFmJAUgvYjy1EacpPf__bro4wonVlgNudEF2KWkc16lhxuyUEbDF9Eblm9iFyajOxJca3WOPWGErkVo4CG9OHdXhA_LTXmB4DlddRfYjh7T5ASHsK2B7ZJT0o9hUbyUHcV26I3SCzEx9SFsBjK-nQ1UlW6S6OAegWmvucZw_Bpwst2JjbeW2dWnIicNWCO1k7c29Y2NLrZHa8rZYLw8GwGJBPl5jRt_I7JO_RkDL46Va-emPLc2NzQoWIPuhHuC3TU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوهای این خانم معلم برزیلی مهربان و زحمتکش بخاطر سبک خاص تدریسش حسابی وایرال شده:
تو یکی از ویدیوهاش که حسابی هم وایرال شده به یه دانش آموز فوت فتیشش که درسشو خوب بلد بوده به عنوان جایزه اجازه داده پاهاشو لیس بزنه…
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71653" target="_blank">📅 10:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71652">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=QVprRuCgxlDct2uqBWJJChImY2fYMD21mGMUIXA3WKf414lpMFE4zchr4aux9cI4u7x696oRblaEWSMoE4RVh0SYSGWeLyZThO_12W0Hyk9AEM18jVYYGbYDnjCFjeRr6qyAOMZjbe-NcTtV01Y__9F-tyos3UmeKtFG3MXRttaf7Wzwpc5ZPjgeGAm0RihnyDE2bXBvFs6NiUrV2BMC0LcAVD8By13cdBQSQSvyQwYdCDMWEjP-QHjrFVrL7YPgy9EvQeRopI-Van2zJsSqGHLLOpB8A2qhqjQ97klnmPvx3wK6ZkV7bhv69NHNSF8Eh8Pf5ro-88q9HU1VFRS0AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=QVprRuCgxlDct2uqBWJJChImY2fYMD21mGMUIXA3WKf414lpMFE4zchr4aux9cI4u7x696oRblaEWSMoE4RVh0SYSGWeLyZThO_12W0Hyk9AEM18jVYYGbYDnjCFjeRr6qyAOMZjbe-NcTtV01Y__9F-tyos3UmeKtFG3MXRttaf7Wzwpc5ZPjgeGAm0RihnyDE2bXBvFs6NiUrV2BMC0LcAVD8By13cdBQSQSvyQwYdCDMWEjP-QHjrFVrL7YPgy9EvQeRopI-Van2zJsSqGHLLOpB8A2qhqjQ97klnmPvx3wK6ZkV7bhv69NHNSF8Eh8Pf5ro-88q9HU1VFRS0AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش‌چشم، کارشناس صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی موندن که سیستمش چیه. موشکی که بدون نیاز به ماهواره، ناو در حال حرکت رو پیدا میکنه و دنبالش میره.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71652" target="_blank">📅 09:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71651">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168229fd60.mp4?token=JajxvmGGkCSqxPYOaKLF_QOtLhYnf5dYv2QiOjEPMKD2TqdxioXUtym6BPooQUyiuAy2UY-t6AmnokKlhGuKsxTs4X1lJPrVHvr2EHZqnN64T9c081d1q1mL28NRKqxdzdq1qHmltsdX8JkoSo5fwTcLcAk-6RZLBs5TBQDyTwl-VcfK0IUyr5eEyZUKc2YiLxigqwKEFQQrqK_gdTMd8R2PZT4tFM6p0QkJz8y__6ipU4ccJp6x2m72jqe85M6Xd-CHRgIL5d2NFXtJtKQjEevyrm_jUbw2x2sWsR51kTOvRq3hfP5pSz1HpJyuwa8YneDRr0505KfczdWnPp_G8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168229fd60.mp4?token=JajxvmGGkCSqxPYOaKLF_QOtLhYnf5dYv2QiOjEPMKD2TqdxioXUtym6BPooQUyiuAy2UY-t6AmnokKlhGuKsxTs4X1lJPrVHvr2EHZqnN64T9c081d1q1mL28NRKqxdzdq1qHmltsdX8JkoSo5fwTcLcAk-6RZLBs5TBQDyTwl-VcfK0IUyr5eEyZUKc2YiLxigqwKEFQQrqK_gdTMd8R2PZT4tFM6p0QkJz8y__6ipU4ccJp6x2m72jqe85M6Xd-CHRgIL5d2NFXtJtKQjEevyrm_jUbw2x2sWsR51kTOvRq3hfP5pSz1HpJyuwa8YneDRr0505KfczdWnPp_G8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواب رییس کمیسیون امنیت ملی به روحانی:
اون روزایی که تصمیمات غلط میگرفتن اون زمان دنبال رفراندوم نبودن بلکه دنبال حاشیه بودن
اکثریت مجلس خواستار برخورد قانونی با روحانی هستیم و این تقاضا رو ارسال کردیم
قرار نیست یکی تو گذشته مقامی داشته الان از عدل الهی و کشوری مصونیت داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71651" target="_blank">📅 09:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71650">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71650" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71649">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0jDSmw3T03usGSjOL5uL5MXBgIMZu2B4KznWCqw820l9B7AxAiXpODuQLPS1c5PSfTA89OFY9Ks3zy-R3CI3NxpdFGlkxNZ26Pe-ZcUbr00BqgPBkUZ04BNPl3sTXuNS_TlnJXwf-RwSyb14SuAZQ-bsvQGPVnCHVci-E9HzwW5MFV5FGryvvR80usES8UrSWBqF07UQStqYppU07pprbDMmjTPuSWUcDeYPFfKt_SO8cPB2Zmdf432gD3q5AlcRuocDegUtQ1kPDf4ugyBckwpOEdnKijX1BVVP0wquBADDmjXTQqnKKWVwd3Skh4bSA0tg0_u3C1TDLiHKGEYxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71649" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71648">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=InxptZBaXpxcszRDbS3AAA2WyMrB3nuABHqVCuY2_p9-Nq8K7aH2WdiYwOOXLfqSlimP77VrKeonGClq2PxJxrlf09656jyh8Z6oz4qPK1MHFWoSEmK_NdsMp6IFJdWCM2dGDSj3mtOE9B014WaDPnBmGd7QqCrzSMXkmbRPT_sQp64Dzm4dI67Ykfq_ywIvd1_tR3rIKMZS43ivxIxY2xxIPM0_ZtlRESJ9LEzjsGmGIMI9xu1iypdy0rA2_B4343DVi5gblWimbJrhicoI1t4QXrCxqfGTMxOysjdOmyn4bZ0s2rRCEDrKZEyWQ-XJwXxeSBEv_yO5jcGRldXTbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=InxptZBaXpxcszRDbS3AAA2WyMrB3nuABHqVCuY2_p9-Nq8K7aH2WdiYwOOXLfqSlimP77VrKeonGClq2PxJxrlf09656jyh8Z6oz4qPK1MHFWoSEmK_NdsMp6IFJdWCM2dGDSj3mtOE9B014WaDPnBmGd7QqCrzSMXkmbRPT_sQp64Dzm4dI67Ykfq_ywIvd1_tR3rIKMZS43ivxIxY2xxIPM0_ZtlRESJ9LEzjsGmGIMI9xu1iypdy0rA2_B4343DVi5gblWimbJrhicoI1t4QXrCxqfGTMxOysjdOmyn4bZ0s2rRCEDrKZEyWQ-XJwXxeSBEv_yO5jcGRldXTbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل یک عملیات ترور علیه یک فرمانده حماس در غزه انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71648" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71647">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3D_mGOTMAd6OYgGUNceJA-gfd79ZV-gO0OckN8p8MSO_lawfzei3IS7a2miv_eT7Vi-RxfyM7eLHP_f-h6mW4HivsFYLgDKc7G7_Vsq5shdiPhk0U7rTYcTduP9qP3e1mdSh123UoczRf6U3ZrneEhkL05bLc_ohm7w8QACnGP_03wJElSAcNNj0stnO5QsPzHTyFhrbjysbf7w_6-NzqH8MEROzctLTY5NnTZyUGg_rkfc_g4ULsw5FHZsz4PfPkUg26_3otiTVraqJuFbkRYyX5XJJZxNPwiYF7K4yCN5Ep0mTvEqwNbngBXdxJoD44zaAxLcijexrqLDmYqMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم». معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در‌راه است را نخواهد گرفت.
تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71647" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71646">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس.
تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71646" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71645">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itiUeTnsu8Jpb10RE4Bvb3H9ZCLhouTwXCfOiJMOOlBY3OlEFmfTj5MRvPY8uDGpq0W1VvfPeN7kpmEZknCKbEStpm93foMsSN1oZ77rb6Y5G_iW4TqJP2V3-LqcSUHb273ylFTAK5O54eSe9kdvtXLgWiGxTi2N8pPNEbGAeJxaRuI4689z1YtWyyTx1bfE2EyCGaNwHcUgXjJJH6X3svaH_a8fhnl8XoOnPaB3na4HKQg76k-HjJS6DUEjnVOECBw18d2FaMJpLnkUBLL-2bC9KXOcUakFHmWv7HYMUWfCtotG1Yk3SLpcHwmEOlMm9Dx_wz7q1sZcZK_FoHuszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ماه گذشته، نفتکش «ال‌گایا» با پرچم پاناما هدف اصابت موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، در حالی که این کشتی در آب‌های ساحلی عمان لنگر انداخته بود، ایران بار دیگر با استفاده از پهپاد به آن حمله کرد.
این نفتکش هم‌اکنون توسط یکی از شرکای منطقه‌ای در حال یدک‌کشی است. ادعای کذب سپاه پاسداران، نمونه‌ای دیگر از دروغ‌پردازی‌ها و تلاش‌های این نهاد برای ارعاب و ایجاد مانع در مسیر تردد کشتی‌های تجاری در این تنگه(هرمز) است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71645" target="_blank">📅 23:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71644">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیروز در بروجرد گروهی از معتادا در اعتراض به شرایط بد کمپ از اونجا فرار کردن و با این کار انعطاف و آمادگی بدنی بالای خودشونو نشون دادن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71644" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71643">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71643" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71642">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71642" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71641">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSnwu3rXMIBfm43vb_buTUmt8liyqnF1rJOc1hoFNgnK2sKY5ee26hJJUgbaxpcqmvfFXlfKCF1fMbj8J60M9v9Cjt-ATScSSlN5BhugthQ-WbUUH7aBS5DMoLVXzedo-8JKXKQWmvTjgIvZAba0kma3ac4KxwL6xwlYshre4KMAhdB3BglcF33S-8w91fq_RCKsi8DbKkmT8d-6OYiIOBAGRMXCsCkh4iJrXmX1ppx7ndSqVJW3854UgLwoGvsfa_e5LShIUUNMVhwd4K8lcIPqaJFneil0WGgTHcb8cyKcDl-LIpSpIXcCo3icU3PHLSxAgYPNmvO6-2xlEe1v9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
نفت‌کش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در جنوب تنگه هرمز، با یک مین دریایی برخورد کرده است.
تلاش‌ها برای مهار آتش بی‌نتیجه ماند و تمام بدنه نفت‌کش در شعله‌های آتش می‌سوزد.
سپاه پاسداران اعلام کرد که پیش‌تر درباره خطرات این مسیر غیرقانونی هشدار داده بود و تأکید کرد که تنگه هرمز «همچنان بسته و تحت کنترل هوشمند ماست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71641" target="_blank">📅 22:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71640">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=veJZh9t3ginHKJ8oxJo2FwtgmrFqkONb3w3BkGRRE7I8E37ANAvaAcOVIqoGG6iXXWIJYIY-ExMLzKn2a-erkoM8Igad2LvkidkDjFy1cylSHfD7XOl3A3GLKw_7xLsPeL2d18BxqeElCPEv4ddw8i8SvL0i-VqoFuOoJKSA91JkqYj2fG9xtl6yr2AHyjsPCWEBC7TqAOYQvATfIxhag2-RquAqboR4lp6DdSzvpLQIMcA606LzlN2DaUvVdOiYbvBqWzBf_bLntm2zHETlQlJvAvs7iMRlwdtrf8OWSzUeqNWT1lNEPpHgmXDZZryHUfV75xReu8i9c1aBEvjGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=veJZh9t3ginHKJ8oxJo2FwtgmrFqkONb3w3BkGRRE7I8E37ANAvaAcOVIqoGG6iXXWIJYIY-ExMLzKn2a-erkoM8Igad2LvkidkDjFy1cylSHfD7XOl3A3GLKw_7xLsPeL2d18BxqeElCPEv4ddw8i8SvL0i-VqoFuOoJKSA91JkqYj2fG9xtl6yr2AHyjsPCWEBC7TqAOYQvATfIxhag2-RquAqboR4lp6DdSzvpLQIMcA606LzlN2DaUvVdOiYbvBqWzBf_bLntm2zHETlQlJvAvs7iMRlwdtrf8OWSzUeqNWT1lNEPpHgmXDZZryHUfV75xReu8i9c1aBEvjGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره سرگرمی های روزمره :
سودوکو بازی نکنید اعدادی که کنار هم قرار میگیرن یه رمزه یه چیز نهفته رو آزاد میکنه
فضای سیاه سفید تخته و شطرنج هم شدیدا جذب کننده اجنه هستش
🎙
مجری:
اونوقت بگو هیچی بازی نکنیم دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71640" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k5jd39p67Gv8XiMbs6rJQz2aRTSeXWYkrz9v31QP7oVTlNLDY2qqmViaCekTdLZ4Xv1FFKCJRZH9SyetXRoQ8iD6SLZ3MPXVV5GQT1pb0EaIy-K3mAVCIswUiJ1NwwmfmcPdAPm9zjWr_VAn3bBUZZwTM0GekB5oXHUEej17s7QrbWv-tQEly7tRI-F_c5hLvX8_Bg8QHIfQLutB0f-y3DuJcZfuscaMrv0Pw_NO2HPW729WTMaCzcFCqpIpDXLMHecSKY4yulls6grCZetooqCdZV_a_r_sEe0WpR-jEOQx5-LwUVycrhgcTEoQFTPiQ1u9RXhO94Ks2T6VIBIEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SZkT1Q48gRV77sgGSBwqajNQsmMsPMEiESyRNb7szkvKOQ3fKZm9t55CHS9uvNrzjyx5duUD4zP-MU3abVAJu_foGXeBGozDboBL_O_6Dba8Nb2TDQoNvVCLtLdQJce1Qz1slnpE-DOh3zv4wADfkU_4Eu1DZhp34XOMabyUUgvcPHNxKJZdpTF0D262Z6qu8hCAGbytofWqMG94PSOXGS2MkHoKuv0ibFKL_CIbh8WAqviZG96bZPwFKImCc8Lh6GDOeuYUkNap6e7f4QQ7bDuyt4wn318ULzqert5uYPNRhLIRceIuCd5JNAxww7tPOhmfA-CnX3iK6jk364Nphw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامکی که داره برای مردم ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71636" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9266483.mp4?token=icTwfwnq7GTcJmcb-B8018c6NF7C2ZmBDHhrB-1M0pDq4X3AxdH04x02yq16vd6kWlDRihdyFG9hX7UXdSaw_tn5HwDZB4T1ew60cqPdOPCVp1HrIH9DnXOY28zoYY5U2TQroF3OQ2VD51T8rwAWjpvCguabIiUgQIO2YEB7V72ek8yedBB8IlA1U7MH3JZ1ZAy_XOB6QNrID_UB8xEgu1tKr8Ha_ekIi2bOd5DtmKXbXL3hfEtocnN-UbC3oFyifJsFOHGUwqHTuEJktyB70t6kgsZkF-_0JqJrInZsZ9yibjrFr6menq3tWdbZGcFWZL7iknExfpXQEanPZkNAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9266483.mp4?token=icTwfwnq7GTcJmcb-B8018c6NF7C2ZmBDHhrB-1M0pDq4X3AxdH04x02yq16vd6kWlDRihdyFG9hX7UXdSaw_tn5HwDZB4T1ew60cqPdOPCVp1HrIH9DnXOY28zoYY5U2TQroF3OQ2VD51T8rwAWjpvCguabIiUgQIO2YEB7V72ek8yedBB8IlA1U7MH3JZ1ZAy_XOB6QNrID_UB8xEgu1tKr8Ha_ekIi2bOd5DtmKXbXL3hfEtocnN-UbC3oFyifJsFOHGUwqHTuEJktyB70t6kgsZkF-_0JqJrInZsZ9yibjrFr6menq3tWdbZGcFWZL7iknExfpXQEanPZkNAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
سیاست ما روشن است: ما به نابودی زیرساخت‌های تروریستی در «منطقه امنیتی» لبنان و رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد.
به دشمنانمان می‌گویم: اگر تا به حال درس نگرفته‌اید و تصمیم دارید دوباره به ما حمله کنید، ضربات سنگین‌تری متحمل خواهید شد.
هنوز کارهای ناتمامی باقی مانده است و به یاری خداوند، آن‌ها را به سرانجام خواهیم رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71635" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71634">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-4ia36pfDiU08XNdxtCBMLJ1jK_mfvyGynHohV65_cFSiM43txwVxLyyn8vGZaRJK3OMyC7tFVGHq44tkb7aRAkaQCy_iF4rJxtqscbkeLKPzHDk5jidKtL6qT4nqvH7LcXGZewdTiC6vVzUL4TLoBNwEnB1J8FbCi1tVDhl-u4QzOsL2zYWi97JUDN_D3W2W6xLvWDx_NZfVDpqGVyTeR6rZ7ehe0Sf_ctm31PC5oWLYKKicfmGJT6X4hJu8dKrGTVQcPblFznsdIt06_-BsfqPncWyGO9hPQl_sKiLqaYiZyLMtTHFyJvOr-rH1NfIINmZj5ZIsjbDaItXCAxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری «عملیات طرد اقتصادی» (Operation Economic Outcast) را با هدف قطع تمامی شریان‌های حیاتی مالی رژیم ایران و حامیان آن آغاز کرده است. به همین دلیل، من فراخوان جدیدی صادر کردم تا افشاگران اطلاعات خود را درباره کسانی که اقدامات تروریستی ایران را تسهیل می‌کنند، ارائه دهند.
خطاب به هر کسی در سراسر جهان که اطلاعاتی درباره این شریان‌های مالی دارد: این فرصت شماست. اگر اطلاعاتی قابل‌استفاده برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ فارغ از اینکه کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، اطلاع دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71634" target="_blank">📅 21:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHAZXITBkfSjZXU9vfXjjAe5_bWvYVBwpSY_X-MaGuw13PlHC4ZwS6LRrPqtN0JyfJsl3hDRcMyMWAGrqELUGbBbNYWIuUx8b9DvNSiHKMdgJn2wjuIZ8bWXqzUXQh-jzIKs6NPv3f1ehsdpSiBvkCA9OmGu0L4UOc9vjb-iNXL4UL7QmrjqBUFlmPtpBFla7QaWCzf7M4dudRFS3RgTE6xX15kEksLnnvM7Bd1aX901WOOif-7BCPA4LlUtTKp6gG619fWW6UDoYz-1Ban9O89emO2djJU_vbzJXvIkpifEP-9QQj_Mf4oBblBHP8TQ5kFtgZFDKy35AAxnOj2vEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
نفت در حال عبور از تنگه هرمز است.
کشورهای جهان — که هیچ‌گونه کمکی به ما نکرده‌اند — باید پس از پایان یافتن این غائله و فتنه‌انگیزیِ ساختگی، هزینه‌های ایالات متحده آمریکا را جبران کنند؛ و قطعاً چنین خواهند کرد.
ما این کار را بسیار بیشتر به خاطر دیگران انجام می‌دهیم تا به خاطر خودمان، و نسل‌هاست که چنین رویه‌ای داشته‌ایم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71633" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqz7TzyH7WcSp3Gs5E7LAF65vmtq2APopyuQWYplavVWGzDFuACxyyPcPPU8jLvZGmTJAKAMWj3VT8dcjgYKZPVA98fs-tDgJ8EfNuKF43gxS2OsttAfpNGhHmDDKCq01s1cPWXTsKLBixfzjeI-86QDYTCLW8CG_7zhhOsnTc6grGbQP8pcSMdeR4PPyODFKfjeheBVPr1UEjAuID9neJmfD45uJ_EsBjah_Qh-nXVIjxwCFb_QpHdR2_EBmQbKcdh9CiqWQRwYhqgiUAWlAx2wOU8IPDnCcgViBZSoj5BERLzBBZKwoxBg6Ula_mIdEVjnUw-WoXz2zl99-kzF5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
امیدوارم همه متوجه باشند که افزایش قیمت‌ها در سراسر آمریکا ناشی از عملکرد «جو بایدنِ خواب‌آلود» و دولت او بوده است، نه «ترامپ».
حتی قیمت نفت در دوران بایدن بالاتر از سطح فعلی بود، حال آنکه ما مانع از دستیابی ایران به سلاح هسته‌ای شده بودیم!
به‌جز نفت که فعلاً وضعیتی متفاوت دارد، قیمت‌ها به‌شدت در حال کاهش هستند؛ قیمت نفت نیز به‌محض پایان یافتن درگیری نظامی با ایران — که زمان زیادی هم تا آن نمانده — به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71632" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-l6RLb9KSPpgw1bW4uS2PgiUMAQ460aix5QoF9FuCik5sJxHKPPl14CR0kcJSMpp81n2FecQ1MN79Rosbk0KDzk-17DJblWDp4i_LFfbLK04OUIpqYWPijGwNmwkOwrodC9R-VwNlmh2qP9jQfP9tQ2Di81MQMMhuGqG--P_i4mtQuokdJ-RGk0bA5AEqlRwTsBkWHPqWNXYni1MCzeIZVk9mSS1S1E2-EFMp1U1v8xzZg99YH45D-41Miz8_BPtzfjikEXVRQngVJU6HZH8KPVyzLmuwtstT5JO4ipW2sId3HkU_Ektgw4JNE7ai1DppxDEdxqJFsHKLgsRE66bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
من به تازگی گزارشی دریافت کرده‌ام مبنی بر اینکه ایالات متحده بیش از هر زمان دیگری در تاریخ خود، سلاح‌های نفیس و ویژه تولید می‌کند.
این سلاح‌ها روزانه به نیروهای ما در خاورمیانه و فراتر از آن تحویل داده می‌شوند. کارخانه‌های شرکت دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند و همزمان به طور متوسط هر کدام ۴ تا ۵ کارخانه جدید در مقیاس بزرگ می‌سازند!
تمرکز اصلی این تولید بر روی پاتریوت‌ها، سیستم‌های THAAD، تاماهاوک‌ها و سایر سیستم‌های موشکی استاندارد بوده است که ما در حال حاضر تعداد زیادی از آنها را در انبار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71631" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
تسنیم:
ایران بارها اعلام کرده است که به دنبال مذاکره برای رسیدن به توافقی با دولت ایالات متحده نیست.
ترامپ همچنان ادعاهای نادرستی درباره توافقی با ایران مطرح می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71630" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  «ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد. این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71629" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THBZcuztfbSZQvmOFGfaoWvjc2yRp3gGe-o7vjI8jM6PTAIfnKNIsg1gLJIhi5MKBWMlSQcJpBe8b_PgGnBx5R2X2NvSSEJOc1dSvj6_1iun_kR9X1m09Ds2v7aWDlNP7AxB1MFF9UrpDkgNkLPO451_Q6sM9ZMMVg6cnRncan7nBQRTk0OaccP_3dJ7JcigpugSKG0qKT0IOxRGjhwn-uy6TJBvT-3S-lWwibGP-QC6k_gPNj2ynpYiRC9LjmQ5-JNMIZC8e7gRtb4X81d4ugtS0M84pD15zU2SmGmj8sEveBDiIj0WklO_CVzKi1o8ZNHU4eTin0NfXno9bI3vBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد.
این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71628" target="_blank">📅 19:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=hloZfamgnA-_qcnECzVS1cWyg07pPAiA4ylnI771ZwKguSOyza05jWUCTvXi6APPNLquehXEL2vXk490cnVbgv4kEcjE_UI0pakm4meokmjtWIThxFdIrwbq2hl-1kqn61aFzTc-1RImO_cN4ymTWadZ9FCbhl_mlXgg-blPLiUe4ha6ZVEEj45Omc1b5rpjATltWyujuF02QPeTh6JqvR5b83O3b_8Mf7_w0-VjsUVX6gaaQD4UJ8e3sXXCZodnlyiqjocy27N-M_TyequinEtVdA35csc7sckh861hcrG5rH3nGmOp8fry4NGRnSZq1T044-DHi_Z5q3cw1TVpzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=hloZfamgnA-_qcnECzVS1cWyg07pPAiA4ylnI771ZwKguSOyza05jWUCTvXi6APPNLquehXEL2vXk490cnVbgv4kEcjE_UI0pakm4meokmjtWIThxFdIrwbq2hl-1kqn61aFzTc-1RImO_cN4ymTWadZ9FCbhl_mlXgg-blPLiUe4ha6ZVEEj45Omc1b5rpjATltWyujuF02QPeTh6JqvR5b83O3b_8Mf7_w0-VjsUVX6gaaQD4UJ8e3sXXCZodnlyiqjocy27N-M_TyequinEtVdA35csc7sckh861hcrG5rH3nGmOp8fry4NGRnSZq1T044-DHi_Z5q3cw1TVpzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ رفته ایرلند و چپای ایرلند هم برای اعتراض این حرکتو زدن؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71627" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71626" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcATzFE6ibuzLFmecqeWebVVfCadEKlmRUGG7LbqVcsCgPAWAXwqFN4ASBlGDV-3xYrco3RuEsEdemtliixaviaHoMwbmRMnpl89yhZsKwt-FsZ7xxHt6IDfqXDUSENc1ZDBJJUiF98RWVnyI4z_DqdmsZm6F7DcE4E7P0nkM6mehedCfjNUAS7-dUXVgZcKAPp2EnQ5oFEDYWW5KCkadecnYQ0qsNG45N3Hk_DuqXm4NhJPSZNTY6fA7FwwCrt8BStEbDEKspZTpB_oh4NWS8KIIvuA_GdRlXl0-cZF7lcfqke4a-gVZi_9uykmGoFg4J5D79sa_YBRo2PM6IkxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شب بزرگ فوتبال آسیا !
نبرد هیجان انگیز
⚽️
السد
🆚
استقلال
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل دو تیم باهم:
⚽️
السد: ۲ برد، ۳ تساوی و ۱۰ گل زده
⚽️
استقلال: ۳ تساوی، ۲ شکست و ۶ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71625" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCHSNPTQdAdmTh5UiDFltKezqgVcS70ftkz1ule1WIYRUD1UL21XM4-5KMKOFMqOzvGWp7eNuOA1JtszERGEHDrixCIUaNZKKfXdT2SmGZ8-QQaKH7oJd_y2E2RG2vZKaAA6ol6WTZZurcMi3D2LxmWRWfZB-KZBRZJA7Cb0ztDbFiaWqFjTktEugWeZUUG2PdGR2fULEeqgbXWQBrWiXOrSVllkrNknTBor9to8u-gsc6CEWJ3EnJwDGrFLDGgBUwDYwiFdahVsJWwZqJ-kcDXh75Q6372sgR3T63zqgplWI514iMzdaT5QEAxJPAmcjo3abyni9tsqysrorrICuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
اوکراین موافقت کرده است که به تأسیسات انرژی روسیه حمله نکند؛ روسیه نیز متعهد شده است که همین کار را انجام دهد!
افزایش قیمت جهانی گازوئیل عمدتاً ناشی از جنگ روسیه و اوکراین است، نه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71624" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
دقایقی پیش چندین انفجار سنگین در چابهار سیستان و بلوچستان رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71623" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
ویدیویی از عملیات نجات افسر تسلیحات ملقب به "براوو Bravo"(زیرنویس فارسی)
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71622" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnGwOU5m98yTne4886RoXEg1NAfynfHRhhqlM9QKxy-8Fm_E2zBhZzd6SRYv7hgHsYv4_dneGbWoz3ZMo8nxdy62hxz9VvVTFZmNW2iK85USfeV_W18PfoPGfSeRQo_aVNdmNaWUYC4J1d0yxUo1AIfaHpgaCvjY8QZSJs0g6BBH9F-2yEwNvLFMfmTJP_itlq7LYMaGvR4Oz2-jpa2kVVBXN8-BV2T1X_I1ktG7jQ5Pv-zbvZC_nmjkOL5UjwvmOgBAwtVVAaI7Sn49CywHWNjUXlKPZnGfeOoFtDa-xFD6pTY4TROC-mMVqJYU3PJ-Dv92PypcjlT82ltt9tiBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو هفته آینده برای سخنرانی در مجمع عمومی سازمان ملل در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71621" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=nOSdgzurLygVXvC-LrW37zkqaZiCZ3jsexVS-hdf4EM9H9hy2_lcqLPfHZ377_KV6WTJzvLdIwIbXo95ilMvEtsXKlga1hvJEaSX4aiZvCxS0giWFiDIq8_urKQ-uiw9byCAt-L00Z-K0IKDlptzQaHNevXa3rruT2p8W8IA8JhJRNL_XSHiXxZZLs2w0vQbD-Z4xTTrb3N6DqFxsa8wRREF1rjxLv_3DmFO2Y5gY6UsVU8lU-2EKSlqMe4nqUGo4UX-DmZHOPKP8-YKd8Zzod6vBZ-S1FxT1VX_EjEy5gvfFKr7X_XAK7RbtgQzH-AlT9ciAGLbiuGY6ICTT4xNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=nOSdgzurLygVXvC-LrW37zkqaZiCZ3jsexVS-hdf4EM9H9hy2_lcqLPfHZ377_KV6WTJzvLdIwIbXo95ilMvEtsXKlga1hvJEaSX4aiZvCxS0giWFiDIq8_urKQ-uiw9byCAt-L00Z-K0IKDlptzQaHNevXa3rruT2p8W8IA8JhJRNL_XSHiXxZZLs2w0vQbD-Z4xTTrb3N6DqFxsa8wRREF1rjxLv_3DmFO2Y5gY6UsVU8lU-2EKSlqMe4nqUGo4UX-DmZHOPKP8-YKd8Zzod6vBZ-S1FxT1VX_EjEy5gvfFKr7X_XAK7RbtgQzH-AlT9ciAGLbiuGY6ICTT4xNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک پهپاد روسی «گران» (Geran) در بخشی از جاده در شهر «پاولوگراد» که مملو از خودروهای غیرنظامیان بود، سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71620" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=lq_IpqkOss5SokCPUKPqDRrc0_bCDbB1u7ljr869xAc_eDEEhGK77ZqsOMAAFfY_lYNpe94A765EnS2D0Q0gomK4bHs28bg4hvSnwBnLo4MpnsvKzc9TDYzfalCmzUTEE__UrnozLNkwBb-lYQk5X08Oa-opFlXRpTzVJfySTwX0kwyOr73hVkb1kOt69DilY8pDD12d25m-vdZonsV_fNWCxK9syoQN4M6tzKWmWF4pWjEBdxGx824OI1O73ndha5Yx8xgL25aoiN8Rx-ruwAN--GhxAjg_wbI2wAQKcUOihUlkldPhUcf6LbvP2WJLCOYBZpokdQhwn1P6WEARKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=lq_IpqkOss5SokCPUKPqDRrc0_bCDbB1u7ljr869xAc_eDEEhGK77ZqsOMAAFfY_lYNpe94A765EnS2D0Q0gomK4bHs28bg4hvSnwBnLo4MpnsvKzc9TDYzfalCmzUTEE__UrnozLNkwBb-lYQk5X08Oa-opFlXRpTzVJfySTwX0kwyOr73hVkb1kOt69DilY8pDD12d25m-vdZonsV_fNWCxK9syoQN4M6tzKWmWF4pWjEBdxGx824OI1O73ndha5Yx8xgL25aoiN8Rx-ruwAN--GhxAjg_wbI2wAQKcUOihUlkldPhUcf6LbvP2WJLCOYBZpokdQhwn1P6WEARKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگزاری این کنسرت خیابونی مختلط توی کیش باعث شده صدای طرفداران حکومت در بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71619" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71618">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=FIpki75eYUsNjasyBMjE9RTkptcRTXPmjixnICU8U4re4KxUPDi_odhkF8KP-CIvAN7C9yrf_E0mUVw_6dvINUc8ZwH5rGoRrBkWl-ylYn5VikqC9tV1DtwoA2m1YOqLeYrQ7N6v1O53FTOZk4ajFULwV6QL0PThbbiLQq6B2yTUN5gbLyCiG84uJI1F1tsx2kckiEWDBN80HUfCiJnoqUUVNTPxeJ147bBrXWMzYTiUDGQKDREg39MOxSmu0TYHBUQxNXF03E7H6Cz2CWe3OOfyq3LjqKXcCQR1-b081bB4kL0LFJjXE4CQa8vuKdoTJN01eiMQa5KGQc4ztINBeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=FIpki75eYUsNjasyBMjE9RTkptcRTXPmjixnICU8U4re4KxUPDi_odhkF8KP-CIvAN7C9yrf_E0mUVw_6dvINUc8ZwH5rGoRrBkWl-ylYn5VikqC9tV1DtwoA2m1YOqLeYrQ7N6v1O53FTOZk4ajFULwV6QL0PThbbiLQq6B2yTUN5gbLyCiG84uJI1F1tsx2kckiEWDBN80HUfCiJnoqUUVNTPxeJ147bBrXWMzYTiUDGQKDREg39MOxSmu0TYHBUQxNXF03E7H6Cz2CWe3OOfyq3LjqKXcCQR1-b081bB4kL0LFJjXE4CQa8vuKdoTJN01eiMQa5KGQc4ztINBeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و بی‌بی ترسیدن نکنید اقا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71618" target="_blank">📅 16:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71617">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=biQPzpwCfRJqz-Ymcl3aetE9sqjBtAVSeo1YWNsv8dY6ALNWwazD4kFuSpHdu_HtQwPwDGjmPv1LYJLzALXNzALvTSsZCkYVW-BJ5V-08UnhNzW8DdYfFA0tVAsaZrj02R2VIA7fE_pWOc8JtRW-frz3rhPTc6jAyqDx4HBjAnsDu1z_FneX9JmNzliXJDefkw3YYUi0JMNITWhrZBZchtznGSyCQEbaTuQ03Eo3ip4qs4a_c4AK82_1KqnUrN4B56QVDxYEXwTe_Hmp2MGhwL4a35vTZvRcZs8_iLxoy4Yklsiy74lsfgMEGlMjC3u7hA4ifalkruLinsC-BWzZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=biQPzpwCfRJqz-Ymcl3aetE9sqjBtAVSeo1YWNsv8dY6ALNWwazD4kFuSpHdu_HtQwPwDGjmPv1LYJLzALXNzALvTSsZCkYVW-BJ5V-08UnhNzW8DdYfFA0tVAsaZrj02R2VIA7fE_pWOc8JtRW-frz3rhPTc6jAyqDx4HBjAnsDu1z_FneX9JmNzliXJDefkw3YYUi0JMNITWhrZBZchtznGSyCQEbaTuQ03Eo3ip4qs4a_c4AK82_1KqnUrN4B56QVDxYEXwTe_Hmp2MGhwL4a35vTZvRcZs8_iLxoy4Yklsiy74lsfgMEGlMjC3u7hA4ifalkruLinsC-BWzZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سرقت آیفون ۱۷ پرو ، در کسری از ثانیه در کافه ای در اندرزگو تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71617" target="_blank">📅 15:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71616">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=u8SkT3G3qEhK1AC1AXpPp2t14lH1LsdCOFClKbWnkkMv_0d6A82BbEpgWHhaNgb55YzRyKrfwMsiCVgcXmZA_aCAJbdC6KycUd5s8fVCKxFdGHZRv7SIEFAx_xSY3dIR5MkKvwDvPucJyEaVtpB2fVNQ1t23fF-nNjNV1WOGow4lVEpMnbvG0RjNtKjg8vy4RPqFQvFOsqu0NM-Ezv7UHWJ2uRN2n6klEK7sUMf-T0pWWA_HwNbzwI55yRjN9hzUsFghosZS_5vB51v3AYr1P_876gipAQgdnhgszR0oCSvVAiqSw9AKz-W8GEoeJFIyaZFOVPRBnCrZhVg6LVgaAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=u8SkT3G3qEhK1AC1AXpPp2t14lH1LsdCOFClKbWnkkMv_0d6A82BbEpgWHhaNgb55YzRyKrfwMsiCVgcXmZA_aCAJbdC6KycUd5s8fVCKxFdGHZRv7SIEFAx_xSY3dIR5MkKvwDvPucJyEaVtpB2fVNQ1t23fF-nNjNV1WOGow4lVEpMnbvG0RjNtKjg8vy4RPqFQvFOsqu0NM-Ezv7UHWJ2uRN2n6klEK7sUMf-T0pWWA_HwNbzwI55yRjN9hzUsFghosZS_5vB51v3AYr1P_876gipAQgdnhgszR0oCSvVAiqSw9AKz-W8GEoeJFIyaZFOVPRBnCrZhVg6LVgaAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
در ۴۵ روز گذشته، ۹ آتشفشان فوران کرده؛ انگار در جهان، یک تغییر بزرگ در جریانه
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71616" target="_blank">📅 15:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71615">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=W5-whnsO8uFscfFV2aqMSCz2fzE6bY41p9z0jXTdIqzZflHPMn891O3XWNXTbFugrDTtKiKYE6qvwZFw3bdSZCz_JlKipKa4Dq6e-nydjZadNqLgBCtWVC6hHp2WLfrXlq7ZYBtpLcc3sau-WLdOX38CAj7RcdVhEvmsUmJnwqJ_dRcT9hpkO3WAZrSe0uZpc6PP8ci-NjCvkxRNsUc_Jb336a0QmlVZBWfTzNR0NyoPUNMpQhqBxCwhQ4yC_-pprwjTk_qfTXl8GbG7D0YzSgoA3wqJciIUjukhJFGYDnSX-aHAymUTb8VMKuQZuobmJ9eQhzAGWWI1jXN9BkGdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=W5-whnsO8uFscfFV2aqMSCz2fzE6bY41p9z0jXTdIqzZflHPMn891O3XWNXTbFugrDTtKiKYE6qvwZFw3bdSZCz_JlKipKa4Dq6e-nydjZadNqLgBCtWVC6hHp2WLfrXlq7ZYBtpLcc3sau-WLdOX38CAj7RcdVhEvmsUmJnwqJ_dRcT9hpkO3WAZrSe0uZpc6PP8ci-NjCvkxRNsUc_Jb336a0QmlVZBWfTzNR0NyoPUNMpQhqBxCwhQ4yC_-pprwjTk_qfTXl8GbG7D0YzSgoA3wqJciIUjukhJFGYDnSX-aHAymUTb8VMKuQZuobmJ9eQhzAGWWI1jXN9BkGdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
ما امروز از قبل از جنگ هم آماده‌تریم!
تو حوزه مرزبانی، انتظامی و خدماتی آماده‌تریم.
با امنیت مردم شوخی نداریم، ما شرایط‌مون جنگیه، اگه وطن‌فروشی به دعوت دشمن بخواد ناامنی ایجاد بکنه، ما اون رو مثل دشمن می‌بینیم و باهاشون برخوردی رو می‌کنیم که دارن با دشمن برخورد میکنن.
دشمن میخواست چهارشنبه آخر سال 1404، همون مدل دیِ 1404 رو راه بندازه ولی حضور مردم تو صحنه، متوقفش کرد.
مردم ما فریب دشمن رو نمیخورن، 30 میلیون جان‌فدا داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71615" target="_blank">📅 14:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71614">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnolN9qOV4hyEhNBOA1thcfy-LMqfd6oHp6yT7D9maN8Qpbl9MUpxDiwxSfSxUg79pP0vVLtrnrDTujufwPQ2cuHSBofMovu6eSPluDi-_JEmDetQouvto0A3g8MBuTXIQzWcAovo2VzZuHaIxM76a0ReEY1_GXeu5SQVqO-yKv_Seu8xzOHJ7I0LpsfqT6IHkLM_TYk2kEaUtUo9QZPFhmGjIlORmFk1ZUPRGPNF2Vxe-fnk48u4Uw061htMZLiKgE-etRRqHWdY-lSn7SKp4bZYxsZr8AAHopHn6O9bGmQYrVucJBRAdl9neG3aNqmff3BvyLsC3KRJ_P-7G3mwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🇮🇷
🇺🇸
بلومبرگ:
پس از آنکه اتریش تحت فشار دولت ترامپ از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به این کشور جلوگیری کرد، حضور او در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منتفی شد.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند؛ اکنون احتمال دارد نماینده‌ای دیگر از ایران در اواخر هفته به جای او سخنرانی نماید.
انتظار می‌رود کریس رایت، وزیر انرژی آمریکا، در این کنفرانس ضمن تأکید بر اینکه «ایران هرگز نباید به سلاح هسته‌ای دست یابد یا آن را تولید کند»، خواستار همکاری کامل ایران با آژانس و دسترسی بازرسان آن شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71614" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71613">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=uTbZKPrRw7bDPgboAJo7MypMdU92ph74sKRQwV7Vna3cI0F0TZwRRgc_XfMypm9zKhu4PqOfwSVfSUsN0etRRjbNiMTn-jp8uI1yCejaHlv1FgXvAyJuGG98NctPGTczqt3KEHStTyYAs9S4XgTWgc8g_Gt9gdRWqQwwsA4V9fATuyxv2oJ4vxjsS6MXQGo50_IKjOTlLZtHgY5NKcVYh0fK6Z33MDMvBuBlL6NflxVCNWvzxxVrTwsx1s24d6j4SdbmiQ-AyQ5uizZNKJIGfPx8j1oUsWvDz0Y4KTn6jFCuxqPFIyWzZGQC5-pgP15hacb3PTh4LmXaXw8eu7CbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=uTbZKPrRw7bDPgboAJo7MypMdU92ph74sKRQwV7Vna3cI0F0TZwRRgc_XfMypm9zKhu4PqOfwSVfSUsN0etRRjbNiMTn-jp8uI1yCejaHlv1FgXvAyJuGG98NctPGTczqt3KEHStTyYAs9S4XgTWgc8g_Gt9gdRWqQwwsA4V9fATuyxv2oJ4vxjsS6MXQGo50_IKjOTlLZtHgY5NKcVYh0fK6Z33MDMvBuBlL6NflxVCNWvzxxVrTwsx1s24d6j4SdbmiQ-AyQ5uizZNKJIGfPx8j1oUsWvDz0Y4KTn6jFCuxqPFIyWzZGQC5-pgP15hacb3PTh4LmXaXw8eu7CbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇳
سخنگوی وزارت امور خارجه هند در جریان سخنرانی مسعود پزشکیان در اجلاس بریکس در دهلی نو، با خوردن یک‌نفسِ یک ظرف آجیل — شامل خوردن، لیسیدن انگشتان و برداشتن دوباره از ظرف تا زمانی که کارکنان تشریفات آن را گرفتند خبرساز شد
😏
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71613" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567356c89d.mp4?token=P4ur9fNHI3Y8WQm7zeJqhzD5xlDUwjJN51jjJ7Pj3b_Yb2c7vZRY5hEfbjRohlvNTt-0STjpgcdS8d8TeWIb_r0CNqj8JxTv68NOh4VKJBRJJXDQPez-feXNwp7h93bczBTsbUxKRa-REV5XfLtpDwrDyr3JShTKP0wZIXTCKBnpapPfeTmmSH0aeCnUWj_E2yVNhhV4r2w2OJBHtYPwV-cvfdfksYY5-Fn1ohzjm4j9e9Fjs9XpcbdfM13lG4IW2WI6FocgQ577MGlHoQwOWqwdssEP8-b-SPs6IJGIef-5Lt72NH8lcT_pcBlMSpXVEY7DctAbJrS0lLAHfb5bOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567356c89d.mp4?token=P4ur9fNHI3Y8WQm7zeJqhzD5xlDUwjJN51jjJ7Pj3b_Yb2c7vZRY5hEfbjRohlvNTt-0STjpgcdS8d8TeWIb_r0CNqj8JxTv68NOh4VKJBRJJXDQPez-feXNwp7h93bczBTsbUxKRa-REV5XfLtpDwrDyr3JShTKP0wZIXTCKBnpapPfeTmmSH0aeCnUWj_E2yVNhhV4r2w2OJBHtYPwV-cvfdfksYY5-Fn1ohzjm4j9e9Fjs9XpcbdfM13lG4IW2WI6FocgQ577MGlHoQwOWqwdssEP8-b-SPs6IJGIef-5Lt72NH8lcT_pcBlMSpXVEY7DctAbJrS0lLAHfb5bOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
توافق میان ایران و عمان حاصل هفته‌ها مذاکرات فشرده است و حقوق حاکمیتی هر دو کشور را به‌طور کامل محترم می‌شمارد.
از کشورهای همسایه انتظار می‌رود اختلافات گذشته را کنار بگذارند، برای تقویت امنیت منطقه‌ای گفتگو کنند و نفوذ بازیگران مخرب فرامنطقه‌ای را محدود سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71612" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CCOqRgBzlHefh4PnOkdCLg3_BJiQFs39rk4S2yMRvVOOeRr9OEkeopO_sHAoyBmXHSoYEcWL9vQ5-KLlnvji2hnxu2gRANXL4-9iXQo0Lg2W3n7xbNt8RsFovkSlK6posH8spxxIJHSq1I1L-y7Otx4h4Xz-nqbt0XtZrd5ytoDBfSz0AAJAgbxMsD7PMg-ZY76DQn38XDTeEPr4Rn1EGcY9sgHRFRgLKUtwo8BTG05E8qMXuBnT0pToLyDE63JN3fpXhzMTBRgjDaenObiHLhf4c4Sx1v-30hNzbU08aGuG06CpMaKnPOPIiwVLMgEdyqKLDA5xDyN9gmFPjvxoHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه دختر شماره یه پسرو که روش کراش داشته داده رفیقش، و رفیقش تو نیم ساعت این اطلاعات رو از پسره درآورده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71611" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71610" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlwG25UnIKCZHpSaX54OWxFbC9nuLyLTnZ7mD5KnEYizJD15QYTTJ85d3z7OMNuS5xPttlNHw3Y0rjDiS52CvqpyIwyCFEabce8LQ9N3UW-15vOSorIErxhNsRP8e-wcTCkW1LalI4ZiGhDS_ABcAjJGLiTYw6CcMTvLvUIRRbo_v8_nlSXBcoTyTaBUfN-ST6jPhw4NegwfB27hFpEQ9-Otfium7J5kXNVJALBKl19kv8AAxiS2pJ0i6-BnzmOaslpsDwRvsdYSoZSVoeCoRQYxiJ_wHA9u4JuMG4NtLxA3BoeTjvYlcAqRxyRmwBI_mY-qtd6-ftHscZzddS7xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71609" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71608">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001bfae793.mp4?token=t9Yiohu8p_GlUuUw84K-HJoF8DWgeA4bnBsu8LjmZfoDr5AkQ1voLT0KJqD1Z7RjX-44nF4Xr0g2OLQTWUHimyVqztkKbeZwku_Zfo0JJ65Fa5jT10nPs7k0Azqi1vInxZuoRUoNYDjnamY1qavWog_dqUu40zNw_36D1QssqC-sRWTtXa_bvF1G7PCd3eZ8zZnPhxDkd2NRU_zErwNn8KSWKvnh1g-6xbMHOoLC0dbGQfmcvMnT-1HKGbW0TlC1nKr8HFSlqXGiI6ScqDEjO67uhDD7eCl9gpT3zfPeSa-dh0BVHjfsNrEIWOEnVzHkXIlJeYiqu9jNRgWlUh9X6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001bfae793.mp4?token=t9Yiohu8p_GlUuUw84K-HJoF8DWgeA4bnBsu8LjmZfoDr5AkQ1voLT0KJqD1Z7RjX-44nF4Xr0g2OLQTWUHimyVqztkKbeZwku_Zfo0JJ65Fa5jT10nPs7k0Azqi1vInxZuoRUoNYDjnamY1qavWog_dqUu40zNw_36D1QssqC-sRWTtXa_bvF1G7PCd3eZ8zZnPhxDkd2NRU_zErwNn8KSWKvnh1g-6xbMHOoLC0dbGQfmcvMnT-1HKGbW0TlC1nKr8HFSlqXGiI6ScqDEjO67uhDD7eCl9gpT3zfPeSa-dh0BVHjfsNrEIWOEnVzHkXIlJeYiqu9jNRgWlUh9X6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
مجری صداوسیما:
اصلا نگران نباشید اوستاد خوش‌چشم مجدد توی برنامه ها شرکت خواهند کرد و انقد پیام ندید و مارو نوازش نکنید که چرا اوستاد چند وقته نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71608" target="_blank">📅 12:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=gRJ3sJ0ylOWA3qZJgZrRRJl_DPQ1_1lK68OnL4zWX3WpS3Nw6KI3hREb6K17pryWdwexA3W7lc5y43TGBamjAYZ0JJX96HqDsOvlurEqC49az5eZlf6cLP9d-fJL1GPzJUwzD0pfT7czMT1uJW62Q9sAjcU2eI8U8u-WK6z8J5oIKrRvzRzAfIlOH-5TbrP5cBgRMzUeXwBnGnd3NEsOsvE-45hIg5Olzol92UZT03RAD3_68K9O8lUfDS93wVemBPlSLCuh2IrhwOxZpfV-JT2qvkesvTCwMx_Izb5_XnKIuGwigX3KP8YUYYCg6mZpA9fTZvQ0PxXqqlmbir7D4gJ2UyuqvEJZrGou47ATD68HBLlee6IbQctIBHSI5AvpJ31FNTkH0Xn28rW0utsi23SprSQhPRpETkEFtOB7EmdXW41wMzwYfbAssmDFiFgBkn9_ISMkBwaYieqenhcSRJ0-i5mYSVnm2SyFg-I60QEFUuO7bM8xd-8tf0f1Po1Rsp1A28cGd1J67eFNApc8LT5Fuc6ShUb1NTISEb1o1hy4M5OjdoVAPgJtPSqi3ZRV-nt7iLYPqCkmUbPW551t-L5P9U9FzH6E4dKbC8cpf9K8v14OTTqQIql_t5QihSB61QzyvaT5xyD4mfaGuLCXUDOmOctrECImyrakMUzSdgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=gRJ3sJ0ylOWA3qZJgZrRRJl_DPQ1_1lK68OnL4zWX3WpS3Nw6KI3hREb6K17pryWdwexA3W7lc5y43TGBamjAYZ0JJX96HqDsOvlurEqC49az5eZlf6cLP9d-fJL1GPzJUwzD0pfT7czMT1uJW62Q9sAjcU2eI8U8u-WK6z8J5oIKrRvzRzAfIlOH-5TbrP5cBgRMzUeXwBnGnd3NEsOsvE-45hIg5Olzol92UZT03RAD3_68K9O8lUfDS93wVemBPlSLCuh2IrhwOxZpfV-JT2qvkesvTCwMx_Izb5_XnKIuGwigX3KP8YUYYCg6mZpA9fTZvQ0PxXqqlmbir7D4gJ2UyuqvEJZrGou47ATD68HBLlee6IbQctIBHSI5AvpJ31FNTkH0Xn28rW0utsi23SprSQhPRpETkEFtOB7EmdXW41wMzwYfbAssmDFiFgBkn9_ISMkBwaYieqenhcSRJ0-i5mYSVnm2SyFg-I60QEFUuO7bM8xd-8tf0f1Po1Rsp1A28cGd1J67eFNApc8LT5Fuc6ShUb1NTISEb1o1hy4M5OjdoVAPgJtPSqi3ZRV-nt7iLYPqCkmUbPW551t-L5P9U9FzH6E4dKbC8cpf9K8v14OTTqQIql_t5QihSB61QzyvaT5xyD4mfaGuLCXUDOmOctrECImyrakMUzSdgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ℹ️
باز و بسته کردن (مونتاژ و دمونتاژ) کلاشنیکف AK-74 توسط این بانوی روس
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71607" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
اگه نیسان کشنده ندیده بودی
این ویدیو رو ببین تا ببینی همچی توی ایران ممکنه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71606" target="_blank">📅 10:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=TtifFkmrX8cJY7bD_iflnxJcVmbS8aSdeRLuO4pv_klisyktuhNgLiMRBfmuw6u9PJ63f-JlrGXgYor6ohLXlFBB6iMy77obESdGTq5c1_N3pqGV2Q4AbUXactwaJ0pUmB2LkQMuke59n7jr4L8896qRN5lbFJ5QqulUTIDaDn4apBN6dk40juEpKNGI_QGJzTOLHUXdDL6dexyOCxqFtlSSxRLG7s769oZ2nk6huQHdKUhdKWJtCXJOCfIkEE1idxx97-7xARUp8Ydo88zMygheVrlwwkaXFx6PNxa9_HB262LxLKSR3lchhaMdpdo2GMhzvIgP-narLWWyBzL19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=TtifFkmrX8cJY7bD_iflnxJcVmbS8aSdeRLuO4pv_klisyktuhNgLiMRBfmuw6u9PJ63f-JlrGXgYor6ohLXlFBB6iMy77obESdGTq5c1_N3pqGV2Q4AbUXactwaJ0pUmB2LkQMuke59n7jr4L8896qRN5lbFJ5QqulUTIDaDn4apBN6dk40juEpKNGI_QGJzTOLHUXdDL6dexyOCxqFtlSSxRLG7s769oZ2nk6huQHdKUhdKWJtCXJOCfIkEE1idxx97-7xARUp8Ydo88zMygheVrlwwkaXFx6PNxa9_HB262LxLKSR3lchhaMdpdo2GMhzvIgP-narLWWyBzL19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست سلاح جنگی بر روی شتر توسط یک عرب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71605" target="_blank">📅 10:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=XoAUgeAInDroAxIbDVx6euSRZztZS92PnsAEWvB9kBGb0Ou9IQnUudLXM95oLh4EjSwXBz1uT-QEyQ6oxJMa-iar1x__ORpdI7rmBLPYlZIXDHKAQsXmkhFgswrTEMRSuL7ReHdv_ZOsJdX2UKmEjoHtxNSzuBSVP2wPJ6wE-Z7R24BK6L9-GO_GRa8DNrxKcw_IfMI06MWRQKoGJ3USR9VKgV-gIuDnhHjyMYqw6PBXukgEz08jxKvY1ytVYZnGSGqtS98lGg1tbrx0XvYou4w0kBwI6BgpF3lhzDCgtwFiWy7th6oX1by-qrZOvKwl49-S7rafaiepZTEXVeK13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=XoAUgeAInDroAxIbDVx6euSRZztZS92PnsAEWvB9kBGb0Ou9IQnUudLXM95oLh4EjSwXBz1uT-QEyQ6oxJMa-iar1x__ORpdI7rmBLPYlZIXDHKAQsXmkhFgswrTEMRSuL7ReHdv_ZOsJdX2UKmEjoHtxNSzuBSVP2wPJ6wE-Z7R24BK6L9-GO_GRa8DNrxKcw_IfMI06MWRQKoGJ3USR9VKgV-gIuDnhHjyMYqw6PBXukgEz08jxKvY1ytVYZnGSGqtS98lGg1tbrx0XvYou4w0kBwI6BgpF3lhzDCgtwFiWy7th6oX1by-qrZOvKwl49-S7rafaiepZTEXVeK13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
زنده یاد مانوک خدابخشیان:
تنها برگ برنده دونالد ترامپ این است که پرونده رژیم جمهوری اسلامی بسته شود. این بزرگترین پیروزی است، درست مثل فروپاشی شوروی؛ این را فراموش نکنید.
چرا او باید وارد جنگی شود که سال‌ها طول بکشد و دوباره در باتلاق خاورمیانه بماند؟
هدف این است که از خاورمیانه بیرون بیاید.
شما به اصطلاح آن دکه جمهوری اسلامی را ببندید، همان‌طوری که دکه کمونیسم بسته شد و همه فرو ریختند، تمام این‌ها هم فرو خواهند ریخت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71604" target="_blank">📅 10:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71603" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
یه ایرانی رفته توی تجمعات حامیان فلسطین توی خارج و بهشون میگه <<کص ننت فلسطین>> یعنی فلسطین رو دوس دارم
😂
اونا هم بدون اینکه معنیشو بدونن دارن تکرار میکنن
در ادامه میگه فلسطین رو از حماس آزاد کنید
در آخرم شعار جاویدشاه رو سر میده
👑
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71602" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
@News_Hut
|Cataphract1</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71601" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
⭕️
تصاویر تازه‌منتشرشده‌ای که توسط برنامه «۶۰ دقیقه» (60 Minutes) پخش شد، عملیات نجات دو افسر نیروی هوایی ایالات متحده را نشان می‌دهد؛ افسرانی که با نام‌های عملیاتی «آلفا» و «براوو» شناخته می‌شوند و جت جنگنده F-15E آن‌ها در ماه آوریل بر فراز ایران سرنگون شده بود.
این دو نفر در حالی که نیروهای ایرانی در جستجوی آن‌ها بودند، در منطقه‌ای کوهستانی در جنوب اصفهان و با فاصله‌ای حدود پنج مایل از یکدیگر فرود آمدند. در این گزارش همچنین تصاویری از حمله به نیروهای ایرانی به نمایش درآمد.
آلفا» هشت ساعت پس از خروج اضطراری (اجکت) از هواپیما، طی یک عملیات پرخطر در روز که با مشارکت ۲۱ فروند هواپیمای آمریکایی انجام شد، نجات یافت.
«براوو» حدود دو روز در پشت خطوط دشمن باقی ماند. او با وجود شکستگی کمر و سایر جراحات ناشی از فرود سخت (به‌دلیل نقص در چتر نجات)، از یک خط‌الرأس کوهستانی به ارتفاع ۷۰۰۰ پا بالا رفت تا اینکه دو تن از نیروهای ویژه امداد و نجات نیروی هوایی به او رسیدند و وی را به بالگرد آمریکایی منتقل کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71600" target="_blank">📅 07:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71599" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71599" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejgt3q2vf79kg4PEqxhVKUov9GAbseNDiNc2yBXJ8CJ-Og6D8lXVbibw9GTZWS8KF0NIeOKgc50a0bRL0gggHt-MoKbzoi2y-v4KNGmcskDTozajp_HsOxD_jV8vGdx1Snf6W6mKADiT3yhuHclMli4pKB0XkfXL1kIih6kRORuAt1geqli1mQHlNWx23Jyv-fykF1twwY3jSZI1uDXwKndlz5giSqvDjnYsu9iyYHGL55OcbCWoFlAKOQKpHHSagQdw8sMsQZku5sjt1md0XNcWiIYWPOOQjw00Rs8j19TggdmXGOGGQU3uf8YeJO2u1dKu8pLVECyfMvuDY_X1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71598" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=A_8MBtHYd2gVNhqpkCcwTJTzfwalqPktPc8XmwMc2TFbVKjFT7jabSPrBD6tw9qYpVQx3_DA7gueKKudHGpo3qgJolMKg11lpWkOioA7SfyeWYPAkWVuATkG8DVIAFyCAbgGRvKGRYm3g7oMx_EKRORKJ2tzYfdsB3cy45LyHwOzJ1SZ1NFyRiKW1Dak5V2zDoc_cAfTyve-jsPQXXyIogFTVPvYPebz1SjvR8xVAtzZJbKcYEHNrab49ccNH0qOixWYmlWEAbEmcWL52YPGfkE9nBdCJp3MKK83iVazGoSdoCX_gfSgMyEXEJTMUK2ztz5-ECiLhE5QlwtjArE6og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=A_8MBtHYd2gVNhqpkCcwTJTzfwalqPktPc8XmwMc2TFbVKjFT7jabSPrBD6tw9qYpVQx3_DA7gueKKudHGpo3qgJolMKg11lpWkOioA7SfyeWYPAkWVuATkG8DVIAFyCAbgGRvKGRYm3g7oMx_EKRORKJ2tzYfdsB3cy45LyHwOzJ1SZ1NFyRiKW1Dak5V2zDoc_cAfTyve-jsPQXXyIogFTVPvYPebz1SjvR8xVAtzZJbKcYEHNrab49ccNH0qOixWYmlWEAbEmcWL52YPGfkE9nBdCJp3MKK83iVazGoSdoCX_gfSgMyEXEJTMUK2ztz5-ECiLhE5QlwtjArE6og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سپاه به طرف تنگه هرمز موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71597" target="_blank">📅 01:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hml5Y4ATPFFIJkrZ9YFmyhDyd9Ihf1mMK5fO00mFgjlXw9i8eMLkmo39_rJe_Siekc0eUgXer1lV9iiqcomhdqBPTbU0CoOfSKYDfIKPm19z_wJNb1UU9db116h3Tv3NCg4YjjG_pWXjVPXgCn-WvUefoV6nWBxuRmYU2bHkcUpyhkf5QP4DPEcga1Kipm_5EWh9I1lSabIKZ57xdAMxr5WMfA9EOufrUloL10Du__WoniwlRA3hE4cU0pc-LOaqHGpTD52liqkpjbU__BasaetEMD9r4D1uwj0NxW9mU8oR_qCLkkON7xlhaSujvp5hENjdMyDjYOoFy5KqrMA9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
❌
🇮🇷
🇴🇲
باراک راوید:
یک مقام حوزه خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در طرح پیشنهادی عمان و ایران در خصوص تنگه هرمز ارائه کرده است؛
زیرا نگران بود که عبارات پیشنهادی عملاً منجر به ایجاد وضعیت موجود جدیدی در این تنگه شود که برای این کشور یا سایر کشورهای عضو شورای همکاری خلیج فارس قابل قبول نباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71596" target="_blank">📅 01:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=m6TV6h9kDLa5f0v4DMeCUW5gQuJqkaxtXUvpgjzOZg3Olt5QdY9sxrO_IJxg5rIsXhKF0TZzds-ysYuMmTNECK34GtGZWZJ2mT6ga3chcXjZ3dp05ygeCJ0Op2LviFyMtY-cI65nAPmchQbdQo85Ld7YLarBMjBbtBxVc44kc-VU2U0_CdQ4gnRlLu1EjgbvHyQ9d_72yD_Y-s_A1-4PL0mmPnkWynm8XIQaYkpK1A_68gCzOaRvK97_NIiIRFzypWy87Ukj4O5EuNScCgof9DcdFtZrS1-lFbn9x7jcRkpnnqElY6VEIwCYLW0CDf-i3EoE8XJIKsvliMuRPXjrYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=m6TV6h9kDLa5f0v4DMeCUW5gQuJqkaxtXUvpgjzOZg3Olt5QdY9sxrO_IJxg5rIsXhKF0TZzds-ysYuMmTNECK34GtGZWZJ2mT6ga3chcXjZ3dp05ygeCJ0Op2LviFyMtY-cI65nAPmchQbdQo85Ld7YLarBMjBbtBxVc44kc-VU2U0_CdQ4gnRlLu1EjgbvHyQ9d_72yD_Y-s_A1-4PL0mmPnkWynm8XIQaYkpK1A_68gCzOaRvK97_NIiIRFzypWy87Ukj4O5EuNScCgof9DcdFtZrS1-lFbn9x7jcRkpnnqElY6VEIwCYLW0CDf-i3EoE8XJIKsvliMuRPXjrYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
ایران می‌گوید دیشب به یکی از شناورهایش حمله شده است. آیا کار آمریکا بود؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71595" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm2iwQnWfdpmr0QHX5AtInvwBt2emwf3mt-3U9dsyw8kbqVzMepQ5S1wc6yaATeY_Y1tK0znER8NLu4x17ckzIlG4lClcKktoCxHCupqMB-Nl3EmgRwPjt2tlS-_kF4YVphdMut8JBmbv7e-O1LZdiospH9b7EvpcHJsIufIHAsB-aTLCTFEnDnb8-xRuMhfpXW2qCOQx7Did5epR5fTQYD-9SkIhDzfNhNMwdtq1I-kjVFLgWER9v34En8VQ0OFc-EpsfVqiLiGXTfFJ249HZxH4apaj8ik8GUlDGyJ2wD3fFZspbNeK7Pseh3OKQ3ZdqVvd1WGb1D5oyc7kEBi3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇴🇲
بدر‌البوسعیدی وزیر خارجه عمان:
در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاد.
ما همچنان به ترویج گفت‌وگویی که حامی ثبات و همکاری پایدار در منطقه ما باشد، متعهد هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71594" target="_blank">📅 00:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
⭕️
نشستی که قرار بود فردا در عمان میان ایران و کشورهای حوزه خلیج فارس درباره تنگه هرمز برگزار شود، به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71593" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_WBQHh4ead2Sj-sTU3u-KVZ2eUOTQKoTGVfDvab_hHnhyJ8TIvryup4f8ZIRNqVwP5Vnq5TnslGkJDtN5I8009gtGW3paDELoWIKnxs4LsjGBCGdw-7rrI-jLmQ82SQ4bAFktfUJa2Uewps4svjD2XJ4Tv2ksTJ2ag3Vi0ipWPdgixTukTl1slZyo2VtNcbb1rgPloOgeYamWbcchvFOyKDCKZcuAb-KJedK4iN8WRuJ3t9X6h5r49EYSI79MQuYPBwowWAyJdxLAS9qfx0Tp-ESdNF0LZPCfiqH-FMNKnk07QJPkVbYyxKIeHpvmsLnHNuWCtlt7qCuQsccBVUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های عجیب پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71592" target="_blank">📅 00:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=TGUJM4U8Dnbb9DIBvq4lOjj2KyPpmBgwjZ6_NdVzEIbhsCWCK5Fz_OitXVxuXRQSY8e5dT4sn7R3sGIYA_rEuCV1aMRon88s5XB6yKSROuhV4i_LfwSBxwavMEpUe4xejB57Ofuir0NzTW3SIhzbuXJW3ISzQDvzWBW6oWbDftcfh71K4gSUFqrMUvjnfsbVALRSkmZmwF7NX3HqY8rGfvzY3oxJFO9puVOLjU3aORd3tiUUIh3x3YftZa7RL2W6DWXd00HAWA1cH-ccFnfjG0fw0q4UNG4AGyHRE82ZzdqPDq5SUXhg3GBHc5rMA98KzhovtjqvKU-YC81yVs3mmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=TGUJM4U8Dnbb9DIBvq4lOjj2KyPpmBgwjZ6_NdVzEIbhsCWCK5Fz_OitXVxuXRQSY8e5dT4sn7R3sGIYA_rEuCV1aMRon88s5XB6yKSROuhV4i_LfwSBxwavMEpUe4xejB57Ofuir0NzTW3SIhzbuXJW3ISzQDvzWBW6oWbDftcfh71K4gSUFqrMUvjnfsbVALRSkmZmwF7NX3HqY8rGfvzY3oxJFO9puVOLjU3aORd3tiUUIh3x3YftZa7RL2W6DWXd00HAWA1cH-ccFnfjG0fw0q4UNG4AGyHRE82ZzdqPDq5SUXhg3GBHc5rMA98KzhovtjqvKU-YC81yVs3mmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو تبلیغاتی بانو سیدنی سویینی برای novig
😟
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71591" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMIW4i3ihfBhLtLb0qE_2tDFV661gtiRyhoj3XogHsEWMMSkE48_5cZe-oW2RDrIbCRmQIX0vLEoXCdCvv6RiBo0fXmh16A62rF8rSXdQlkA7BSna0lQkqI2jPBwCmRN_2g2oFlPSDjioPZI9bY-qGzMrpu8RJf-UV-8EWUjlqjMowC1w9mYZQl30GgGgJOttpXOvwVkLZSjce4ISUiW0gx-3oSSwGtD2WM7VyICsyKkOi9qLJGda_Wxuzrf31TvUaVsuSJR2KLlPq2jyYi9BHRMsMYXMT70EzLNwbo8EISrjL6nFt-DLOPgHLET3bopEIBdPtjnkkcLD46wi9VUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇺🇸
نیویورک‌تایمز:
مقامات ایرانی می‌گویند که رهبری این کشور طی هفته‌های اخیر بر سر دو راهبرد برای شکستن بن‌بست با ایالات متحده دچار اختلاف نظر بوده است: بازگشت به مذاکرات یا تشدید درگیری‌ها.
بر اساس طرح تشدید تنش، ایران حملات خود به اهداف آمریکایی - از جمله شناورهای نیروی دریایی و نیروهای نظامی ایالات متحده - را افزایش می‌دهد و هم‌زمان تلاش می‌کند با بالا بردن قیمت جهانی نفت، طرف مقابل را وادار به پایان دادن به محاصره دریایی کند؛ محاصره‌ای که تجارت ایران را فلج کرده و صادرات نفت این کشور را به صفر رسانده است.
ژنرال‌های تندرو، از جمله سرتیپ سید مجید موسوی (فرمانده نیروی هوافضای سپاه پاسداران)، طرح جنگی مفصلی را به شورای عالی امنیت ملی ارائه کردند. این طرح خواستار آن بود که ایران و گروه‌های هم‌پیمانش - به‌ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق - دامنه حملات خود علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را گسترش دهند.
مسعود پزشکیان، رئیس‌جمهور، و محمدباقر قالیباف، رئیس مجلس، با این طرح مخالفت کردند و هشدار دادند که اجرای آن می‌تواند ایران را به جنگی بسیار گسترده‌تر بکشاند، موجب حملات هوایی سنگین‌تر آمریکا شود و بحران اقتصادی کشور را عمیق‌تر سازد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71590" target="_blank">📅 23:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=dpUWI33BWSx-bvisgaXYUWxK7xmBoMPZZo9J0u5VK9KZmgjjmLv9fmNgadepWPgWbPkYSpYucjuQJ9cZ8j2Ao-yFkDXmhaMidb1lnaMkUpVen871aSWq7TZrXfi9EfaZCMDmXwnF2_gDsHw41Ky8qE_5vl7Q2NIs7vtK4nITRHCkEUFO-i19DiAuSoZPCJzDJDVVkGu7G7QMXC3dBFzrOUhSaSH8LMqMBn_ljDIwRDc4akHiUKC1qZjNnhJkoaMK2rvdQe8ipvhV9hqBU48_4TdtnpchgHCw-buDhnyCECyindOh_HeAO3E4lz-fQLTF96xMXtmbv1D7CrC25qKKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=dpUWI33BWSx-bvisgaXYUWxK7xmBoMPZZo9J0u5VK9KZmgjjmLv9fmNgadepWPgWbPkYSpYucjuQJ9cZ8j2Ao-yFkDXmhaMidb1lnaMkUpVen871aSWq7TZrXfi9EfaZCMDmXwnF2_gDsHw41Ky8qE_5vl7Q2NIs7vtK4nITRHCkEUFO-i19DiAuSoZPCJzDJDVVkGu7G7QMXC3dBFzrOUhSaSH8LMqMBn_ljDIwRDc4akHiUKC1qZjNnhJkoaMK2rvdQe8ipvhV9hqBU48_4TdtnpchgHCw-buDhnyCECyindOh_HeAO3E4lz-fQLTF96xMXtmbv1D7CrC25qKKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کشتی که امروز صبح در نزدیکی جزیره قشم در جنوب ایران مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71589" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=eEWhSHIe6l54K2_whvgUwOK2ZRfgBFpU8y5qnOVKQJD1HXg1ihuirDqBuNXCs2tep_MIKOtbt0yoEUi571lKaJXCzs9YQZxOYcusjxlRiV3_zLbmrj9zZ3Ix5EjJvvSnu-F6Nw15jpN_aK_95tt8vvEt0vSV_Er4DKmRVMb4FgD4sJDweU0pLb3-tA1yTIMP79r-8utnq6Yx3-rih6QL0EKi04N7eu0Zdx8BfhbXpPj_ewnXoLNfBQqkCyCYkLeF30224Z38zYGpNmTgWdd0G1V1ztIGw9TgyAH-MLeXZD2s_uHsLPrVvTjLbH4XSexG9JVQfEs87vrI4Y1KvMvkgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=eEWhSHIe6l54K2_whvgUwOK2ZRfgBFpU8y5qnOVKQJD1HXg1ihuirDqBuNXCs2tep_MIKOtbt0yoEUi571lKaJXCzs9YQZxOYcusjxlRiV3_zLbmrj9zZ3Ix5EjJvvSnu-F6Nw15jpN_aK_95tt8vvEt0vSV_Er4DKmRVMb4FgD4sJDweU0pLb3-tA1yTIMP79r-8utnq6Yx3-rih6QL0EKi04N7eu0Zdx8BfhbXpPj_ewnXoLNfBQqkCyCYkLeF30224Z38zYGpNmTgWdd0G1V1ztIGw9TgyAH-MLeXZD2s_uHsLPrVvTjLbH4XSexG9JVQfEs87vrI4Y1KvMvkgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
زهران ممدانی شهردار نیویورک :
قربانی اصلی حمله ۱۱ سپتامبر عمه‌ی من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71588" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mClVDJxEGufSX9JQW1fTyEWdpMqsSX__ULoHTQjKf_641LyrdtSrVDQb9FsvKewCxnLUR15s2K-qKp5uKStQ_DphuBHCE218JXh07Ri4uSCdk7rkLMrvNPkrM2YisbMD6ib1EiZJ1sp9LONoRtbyHaMz_3fzrQV3yTXeUXrFEcQ1bzJKtYc5exil2uwXI1H__JPqRa007IDROW0HT1MNK62SctFSGNkfGS7_5cR54Rse0yC2HweYga0NQvnmC8YUcWh3KiTwMN0N5iQ0ycR-AN4Q0swEhzaQWkrT8BSmNuRsv24p_BLr0HG4RmEu7gLYFpI7WtZXySz5Dagcze3FnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
🎮
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومان رسیده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71587" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=NSPj6-fis90HjdN2PI1tsubCcE2uS7_I9ox2ku7uR9dvojseZkP7KsiN-ewthyyu4pj7LUXWw9XskIpsSWY2aNonfztNfL-_vkMY3M6jld9uX7w96JKY0wj3SgXqQkFJBo8CAOuSOYkaMlPk9yoGTsITwYugnKOcbxo6y7DIX1SQdaT4-V6toxjgy1dfgV5UtW6lW54IvJ2xKpvmjolnpMGU_GM9FuZzPSlNCwhc72MG_fc_52fS5EQeDBWF-COZ-iISvUQ9Rcz2CMJH4OnM-iViP9Kz3TicsSSDdnlOiU3j9xOEtrQwIcU33IlvtrKMquZJKCSYgRZtBwR5i588xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=NSPj6-fis90HjdN2PI1tsubCcE2uS7_I9ox2ku7uR9dvojseZkP7KsiN-ewthyyu4pj7LUXWw9XskIpsSWY2aNonfztNfL-_vkMY3M6jld9uX7w96JKY0wj3SgXqQkFJBo8CAOuSOYkaMlPk9yoGTsITwYugnKOcbxo6y7DIX1SQdaT4-V6toxjgy1dfgV5UtW6lW54IvJ2xKpvmjolnpMGU_GM9FuZzPSlNCwhc72MG_fc_52fS5EQeDBWF-COZ-iISvUQ9Rcz2CMJH4OnM-iViP9Kz3TicsSSDdnlOiU3j9xOEtrQwIcU33IlvtrKMquZJKCSYgRZtBwR5i588xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مدیر سامانۀ هوشمند سوخت:
خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71586" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
اطلاعیه قرارگاه جانفدا:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71585" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=iCqdi8Hbuv-sxJT9Cf_zGrxtlb_H77LGtFvlW2xunLsieNm5nZ5rZd8gCUv7CjlnlYWetXZFDohQOJt55oUjnWd519bsGER6MNxXyAS5m3LUiUe5Hpc-kzTCUkdFp1FHUNTsWzyWMhqctM8m1_3K77zPrV3QLFVSdaw5_zvysRrpValYx6VhF0cQp_tQuQUdwXO9LmHYsyl4GJqCtzcI8tzDrlGh3o-wtWD5dGLtxz-HfaempB8qc0gR18x6dPpvuaFqMNFQWyQl7ZeIwY0zd1N61eH5LbJrduicEv_pog5ilavT2g2XHvis8ldKStSXJkprwAdx4CJbdeZQ3t0u5xMvY8R3ywAieDdh8GbxGAhLgWqnFVUd-ACi3as09LtCyeo1ZuCvbyyeRxsVCWN-RDLTsbPkgCrRwJgq4A5W-TP_PGz_b2qBe3DNJbedS_m-fANAkkXncgv9Et9IRDgpepTR8t2oHE_L7zlp3z8Hw6y45a8-w8XzVcD2LSDjM06ehowHhqkCo69lk734oM4aKAA3pwryWQYKhOb2HXfG5qm84vmBzGf7MscE8MQWi_GJNQue9xQbJ8s2B8Jfyvo_AJnzpc-CSxQzpDN4eq6VqpybVyckX4QshljUih0LCjCv8sk71rIJ-OnfrylzZ4tM0OOgbTVbZEfRI5h_wO0zf50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=iCqdi8Hbuv-sxJT9Cf_zGrxtlb_H77LGtFvlW2xunLsieNm5nZ5rZd8gCUv7CjlnlYWetXZFDohQOJt55oUjnWd519bsGER6MNxXyAS5m3LUiUe5Hpc-kzTCUkdFp1FHUNTsWzyWMhqctM8m1_3K77zPrV3QLFVSdaw5_zvysRrpValYx6VhF0cQp_tQuQUdwXO9LmHYsyl4GJqCtzcI8tzDrlGh3o-wtWD5dGLtxz-HfaempB8qc0gR18x6dPpvuaFqMNFQWyQl7ZeIwY0zd1N61eH5LbJrduicEv_pog5ilavT2g2XHvis8ldKStSXJkprwAdx4CJbdeZQ3t0u5xMvY8R3ywAieDdh8GbxGAhLgWqnFVUd-ACi3as09LtCyeo1ZuCvbyyeRxsVCWN-RDLTsbPkgCrRwJgq4A5W-TP_PGz_b2qBe3DNJbedS_m-fANAkkXncgv9Et9IRDgpepTR8t2oHE_L7zlp3z8Hw6y45a8-w8XzVcD2LSDjM06ehowHhqkCo69lk734oM4aKAA3pwryWQYKhOb2HXfG5qm84vmBzGf7MscE8MQWi_GJNQue9xQbJ8s2B8Jfyvo_AJnzpc-CSxQzpDN4eq6VqpybVyckX4QshljUih0LCjCv8sk71rIJ-OnfrylzZ4tM0OOgbTVbZEfRI5h_wO0zf50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی آموزشی برای دخترای موتور‌سوار چنل که قطعا بکارشون میاد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71584" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
