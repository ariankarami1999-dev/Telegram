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
<img src="https://cdn4.telesco.pe/file/NaYTvHoa1w6nI-dbIMTPVjIzvNm5vDMpCuDMz_WRBW68T39iSlpjl2a3ayDPAHH5ORIKwvxBitZFEDa75kZkItA6fNfZmN0PFptp5s0FC36l-nlwbUf8TaWbUuazLq3k2zLeqrqQlEY4aBAV4hlq8qYwA_GTB27vcisPR4nzPTJtVPiKuZq80Mzv3q-8gLj4gCVRr6yI1UDRDRBnIs5ODs5RdKm44GKAtUgYepsCbhi1yQh_e1q6iY3MEyHlEL9oblcYApEWamZH19YQVYqP6cdtxKirnYQLNwlc63dSa_dgMjDu8lKot96VoI0tjae610L-HybiZiz_yfmpS7ZLRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 18:41:18</div>
<hr>

<div class="tg-post" id="msg-130349">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: از کشتی‌ها می‌خواهیم که با پیمودن مسیرهای غیرمجاز برای عبور از تنگه هرمز، خطر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/130349" target="_blank">📅 18:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130348">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
عمان به متحدان اروپایی هشدار داد که ممکن است نیاز باشد هزینه‌های کشتی برای عبور از تنگه هرمز را پرداخت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/130348" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130347">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
روس اتم: متخصصان در هفته‌های آینده به نیروگاه هسته‌ای بوشهر بازخواهند گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/130347" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130346">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=JMjREAO0_vWokp1_DWyPRhtJAjWI_tQgttjRGmdr--pQLn4U_h7-zilgSkHJeLMq2KPYLrS_jqAaTDBSp18qw0eMfesimBVqdRS0lz-SVKB3NNuF7QQDLq9Ozyo5RmM8L9aG2tMOMBVkq_qGx05Wqcu4RN6DNvWSr47edbrb56-FhV55bQ_3Blr7mxrlnelzWNNKZQ1PFw7dV-cD2XGKcxSAoh6aZKc2tvvq1XyPxDXX7YlUabP-UzmD8WDD0p972coXEjGJinf1DSHaZ1pyToWYCexEsm5C94adPsn3dkUIZD_edT4ozJ5vE-xVsx9aZ5b9BnCEwWRMkez6gvTWHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=JMjREAO0_vWokp1_DWyPRhtJAjWI_tQgttjRGmdr--pQLn4U_h7-zilgSkHJeLMq2KPYLrS_jqAaTDBSp18qw0eMfesimBVqdRS0lz-SVKB3NNuF7QQDLq9Ozyo5RmM8L9aG2tMOMBVkq_qGx05Wqcu4RN6DNvWSr47edbrb56-FhV55bQ_3Blr7mxrlnelzWNNKZQ1PFw7dV-cD2XGKcxSAoh6aZKc2tvvq1XyPxDXX7YlUabP-UzmD8WDD0p972coXEjGJinf1DSHaZ1pyToWYCexEsm5C94adPsn3dkUIZD_edT4ozJ5vE-xVsx9aZ5b9BnCEwWRMkez6gvTWHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌کمانی و برگزاری مراسم حمایت از جامعه LGBTQ در ورزشگاه سیاتل
:
ما اینجا برای فوتبال هستیم، نه مسائل دیگر. تمرکز ما بر روی مسابقه و کسب موفقیت است. درباره موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
@AloSport</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/130346" target="_blank">📅 18:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130345">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130345" target="_blank">📅 18:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130344">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwdmNYLYPFdWvWd_1tt5R2Hl_-rvVRsjWZS6IKA8Y1KE0qwdgm_EYyAeJaam-48jfq3DFhLGKQrIdWLHP9IYwOSnKoAZjtVm-iPJOxGxi2pgUDSfSYahCQ00xlPKH7TjLPuhwAtpPoMIa9uhlL4SzhVE4J8B8HgSpGeawd07pDTtrRTHzEgYWNT3E5U5CT_2GRK47yawNSTslbYmmAdCHwlclhgPlTgdx5r6xx5YqwWSsFquQqWKh5Ya-n1jmnsk8B9zAuIAh3Is9ChsDdOf3ElT25gY9EiZHnPG3gBtEStebqdln_OaIFVloc6cJNbdtsJ7Jl77PoqslMIqTJwYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان به همه مشاغل علاقه داره به‌جز ریاست‌جمهوری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/130344" target="_blank">📅 17:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130343">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
۲۲ خدمه ایرانی نفتکش توقیف شده توسط آمریکا، در کراچی تحویل سرکنسولگری ایران شدند
🔴
۲۲ خدمه ایرانی یک نفتکش که توسط ایالات متحده در آب‌های بین‌المللی به طور غیرقانونی توقیف شده بود، با پیگیری های سفارت جمهوری اسلامی ایران و اقدامات تسهیل گرانه دولت پاکستان، امروز به نماینده سرکنسولگری جمهوری اسلامی ایران در بندر کراچی تحویل شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/130343" target="_blank">📅 17:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130342">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نعیم قاسم، دبیر کل حزب‌الله:
«ما در کنار ایران خواهیم ایستاد و می‌خواهیم متحد باشیم زیرا مشخص شده است که قدرت شما، همراه با قدرت رزمندگان مقاومت در میدان، به ایجاد تعادل مناسب برای شکست اسرائیل و اخراج آن از سرزمین ما کمک می‌کند».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/130342" target="_blank">📅 17:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130341">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دعوا سر نذری تو همدان
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130341" target="_blank">📅 17:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی:
همسایگان جنوبی باید پاسخگو باشند: چرا خودشان برخلاف اصل همسایگی خوب و قواعد بنیادین حقوق بین‌الملل، به تجاوز علیه همسایه مسلمان خود دست زده‌اند و اجازه داده‌اند از خاکشان علیه ایران استفاده شود یا موشک‌هایی از آنجا پرتاب شود؟
و چرا چشم بر مسابقه مخرب تسلیحاتی و خرید و انباشت صدها میلیارد دلار انواع سلاح‌های پیشرفته که هیچ توجیه دفاعی ندارد، می‌بندند؟
و چرا تجاوزات مکرر رژیم صهیونیستی به کشورهای منطقه و اشغال سرزمین‌های فلسطینی، لبنانی و سوری را نادیده می‌گیرند؟
چرا در برابر زرادخانه هسته‌ای اسرائیل که خارج از نظارت‌های بین‌المللی است سکوت می‌کنند، در حالی که توان دفاعی متعارف کشوری که بارها تهدید و حمله از سوی کشورهای همسایه را تجربه کرده، به عنوان «تهدید» معرفی می‌شود؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130340" target="_blank">📅 17:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130339">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8be098ed9.mp4?token=qdflj8Dy5x44rRuxz66sl3WsjtNnyvV6JiwuZihy96Z5-FiSYEFIqBjM-LvNAlYHGzjyQ-sC_CGv7XE_OY63cwmw_-WpgSLB1bDPYPIJUgfGgV1AE94c5ZZN5P9MxEwS8EGkwxfwwcPATtRwNuoN8nieQ-QucygOlCSfHG3svwkG8bkKQGcq63MdXN3mgZM_rAyVdN0nkgKyhI-JdYCK8Vf-FYO_A4PVz-3GyVL5jnBocBPic1lXdlsz8m432fq0ItSPkM08idTu-FuCjhctR0Kv-bI-Bfj7KcCt_zKxHe9lj0TOR6gcbMm8iZGAmJR5DUy4q-H0uOv4q-b441X54w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8be098ed9.mp4?token=qdflj8Dy5x44rRuxz66sl3WsjtNnyvV6JiwuZihy96Z5-FiSYEFIqBjM-LvNAlYHGzjyQ-sC_CGv7XE_OY63cwmw_-WpgSLB1bDPYPIJUgfGgV1AE94c5ZZN5P9MxEwS8EGkwxfwwcPATtRwNuoN8nieQ-QucygOlCSfHG3svwkG8bkKQGcq63MdXN3mgZM_rAyVdN0nkgKyhI-JdYCK8Vf-FYO_A4PVz-3GyVL5jnBocBPic1lXdlsz8m432fq0ItSPkM08idTu-FuCjhctR0Kv-bI-Bfj7KcCt_zKxHe9lj0TOR6gcbMm8iZGAmJR5DUy4q-H0uOv4q-b441X54w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوروش احمدی: اگر توافق نشود، ترامپ به سمت محاصره می‌رود، نه جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130339" target="_blank">📅 17:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130338">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130338" target="_blank">📅 17:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130337">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130337" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESkIfoLUtO5zKbXFH_4ynWatLtMsAdj5IB8HbOijX2XjEiicTRqWxok0NSiG4WvxEZZErSGVxdoJSPTTiQc90hrwjwTG9Yx0_uoa7ojDVq6sRKmB6adsSxs0ahjWN1QTFYuRXUGftk3J_SowWxlGZ4vFQB_mqsJ46g4rGqTl46eW154UVzQPjVBNyfXtIGixr-ADF0SgXILQMUuN0W_ZC3aflG4qqnSgamPiBoLNdI_ezoYRd_bSjI1oS7_XzcbvMR3QQWYK52MLkB1-EgWhr_VynFLZhe4pPeKE0qTBsAyapi_7v0nfQr4VIi2WFP8N_YxVHcD4aUkw4YX23U4pAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدارهای حمله موشکی در امارات متحده عربی فعال شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130336" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
العربیه: دور بعدی مذاکرات آمریکا و ایران در ۲۸ و ۲۹ ژوئن در بورگنشتوک برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130335" target="_blank">📅 16:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a208c87a.mp4?token=kuNSzJn73GUvRDzItgvueAUxh1nfuEXgPOtrGIb7F5jIAZuI1MK1Z_O2_WQclXt6kELlFfNLh9AEzwpSfR4XucNiIal0jtFfpQoxWV0Bionl9EfC-hI7jV-LERD2-rR0wJoTa0yrKEIWvtaH9bKdWKpXssXsW9ZSqXNWfCcEdjPdiyoOum-UZPNlGsC0u5-cegnpPVNuL7WrdHO8L8x1DYFC3TPfPSzKDHb4E_ddj5EArquoFjNbSTt7tCQley24vamlpbidUDlK3KdDOfgPkp6XSBseKoXPX6UNZsFZmrte8JzBcyrRQNDiGDbRMbmT9v-Ku7A1uCYOt7mZ0XX6eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a208c87a.mp4?token=kuNSzJn73GUvRDzItgvueAUxh1nfuEXgPOtrGIb7F5jIAZuI1MK1Z_O2_WQclXt6kELlFfNLh9AEzwpSfR4XucNiIal0jtFfpQoxWV0Bionl9EfC-hI7jV-LERD2-rR0wJoTa0yrKEIWvtaH9bKdWKpXssXsW9ZSqXNWfCcEdjPdiyoOum-UZPNlGsC0u5-cegnpPVNuL7WrdHO8L8x1DYFC3TPfPSzKDHb4E_ddj5EArquoFjNbSTt7tCQley24vamlpbidUDlK3KdDOfgPkp6XSBseKoXPX6UNZsFZmrte8JzBcyrRQNDiGDbRMbmT9v-Ku7A1uCYOt7mZ0XX6eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این سکانس مختار دقیقا برا این روزهای جلسات دورن نظام ایران ساخته شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130334" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554e768468.mp4?token=XZvarDJKSDZF7n_BPmobNt1TeXaXY3PAmzDfbS6OImbGQKB6_ZMMEQ610Q5XvVuDZeSVJ9dbC2yhiXTRA0Ka6GbSh5X_Y1U4HZEKMVfGk0hSGrZayN9Ui47lG6XX_dLvtTcqF5IhDSJ3qCCufVzXw1fBt-0gWw_SQGHQAPMHKgt1kWuYiYmj0g_z7jVahHGd3m7zaU3WI8fFtNAUG-6sHj0ua504pxIQnJCc_pUWMG2pa0jeu4Kc7dxEjA6YN1OTocNQ57LrWHUaKXs6zb-XAQqLhY9BLJJKPi_FOGfTmyFbb3NkEqIPdbzEUqAFRb0oabv_E14PeP5cSPqTnb1asQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554e768468.mp4?token=XZvarDJKSDZF7n_BPmobNt1TeXaXY3PAmzDfbS6OImbGQKB6_ZMMEQ610Q5XvVuDZeSVJ9dbC2yhiXTRA0Ka6GbSh5X_Y1U4HZEKMVfGk0hSGrZayN9Ui47lG6XX_dLvtTcqF5IhDSJ3qCCufVzXw1fBt-0gWw_SQGHQAPMHKgt1kWuYiYmj0g_z7jVahHGd3m7zaU3WI8fFtNAUG-6sHj0ua504pxIQnJCc_pUWMG2pa0jeu4Kc7dxEjA6YN1OTocNQ57LrWHUaKXs6zb-XAQqLhY9BLJJKPi_FOGfTmyFbb3NkEqIPdbzEUqAFRb0oabv_E14PeP5cSPqTnb1asQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقلیت کم عقل در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130333" target="_blank">📅 16:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv9Qbw6yMnKRjrnlGJ_0pkZ0BCk0iPLzfuenfSZw5S9Ix5a742_pyGixOt-gG4L1LRuLatJN6L43hpl3oBjhPTEL4KML7SD-PbI9hUm_7vyNpgXdh3r71guxg4EotPcaZafFiWmPzgpmxkdmtfsJfeLaJHjZ1VlRRzBzW66Lj7RI0lWiXgAodDGiX5ZM0dTFP2QlBdXo1_OHyrS2eQUGxBtRX_3u2fpmMo5s20GEMdYrH-ruQUez2Y7jNuQiXh66S7rtBqDYtV0Z7HB18CJn2AHZDNttw3vhyjNdPPoiM4ttZ8bU4ZxphMPXGVXTm2D2H7KNQD6dOOL0hyKaVTBzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش وزیر دفاع اسراییل به سخنان سردار قاآنی: اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباهی خواهد بود که تاکنون مرتکب شده است.
🔴
نه هرمز و نه شلیک به غیرنظامیان در اینجا به او کمک نخواهد کرد. هیچ چیزی ما را متوقف نخواهد کرد.
🔴
نیروهای ما آماده‌اند تا کار را تمام کنند.
🔴
وی در انتهای توییت، پزشکیان، قالیباف و عراقچی را تگ کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130332" target="_blank">📅 16:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkTAjy9CKjy_DUszSCx53fSeLtx7t31IRWHdOVUUwSafzjdgmU6AQhjuTMro-vIXR2V2OevIrWVt3N1x_dGjVRL6kROuJCsx1hs3lkY6r6SNIlAu17ICgf6VcZmkqYxPzWTjYjpWK742XEi3qi0ZEQbZlmgaQK6lSiXSmP00SGO6et8dwA-K_wbPWdv6t79bx8lx1xLLbv0mKz11hBvHaKj-ABf4QxQom6qTLCVUZNGcBIL_cNER7VKtmcVXljnezxQbl7oSdxNr9bWoJeT9BwZeyTos3th5aiF8qEwDzn8xv8kbY0zOs1uFmZdZ-4kd4ASashLJZW445vhRDDdwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOhKwUB3M6hSKZonk-w-HTbUW5AzVR5dOvgCS_QjaMPUOv2Zk61YOunycYB0hrCRj_i2R9EGZl0xkjF9SrK-FosMpsYBjhfAKygymGYFV4plm8VjS0RjULbMT2FEqicBwwYZU9VF5rSs3R6w73OLbKVKTYDWIa5gD97qka8K9TPDNjzD9txIizUKe19NWjIqwWiDc4HpYWUg4nh7iAjjjUgC6bMGqURa8XsErRlxKAfww_f4CvF6W7vgjWi8aX161uhla6tM7aLezS0G0d_fKDFBaK9JFBF2kmu9ZylV3vA12ZrzzDKLfBEYMh9xR_X0XXIuYvslCuIvYGVnGKZw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=PZ6iqmxdQBjL_4xoPhvxijCEJ8pKrqbbxde_qqGZrzjyzdEsfTBkRZ9KxDcOiuhAbx2Z2i4h9piBswGUnVeE6jU2RcgqZlVe5bBvttNk8k1qJkT5Ub5TmhYNzJg8-boXPEnqiv2cU_0GdY2A92UZh8V1UsTLi5eVuXDZY4MpmgXTlwrlDATJICf8mSJfpeTUGZLntY0e-O5gLenM1tx6DNYdl-HNCUNDOy6uIxF1uw3fXwNKS7gBsfzgk3dZGVSj7_DiPqy9ocwnfe8Z5AwFeSHt8RlV8C5ri5SkAXXK55t252sMoB1BL1RItSvvQQ9zO3zQJfssRRR-8kUAJ_-ILA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=PZ6iqmxdQBjL_4xoPhvxijCEJ8pKrqbbxde_qqGZrzjyzdEsfTBkRZ9KxDcOiuhAbx2Z2i4h9piBswGUnVeE6jU2RcgqZlVe5bBvttNk8k1qJkT5Ub5TmhYNzJg8-boXPEnqiv2cU_0GdY2A92UZh8V1UsTLi5eVuXDZY4MpmgXTlwrlDATJICf8mSJfpeTUGZLntY0e-O5gLenM1tx6DNYdl-HNCUNDOy6uIxF1uw3fXwNKS7gBsfzgk3dZGVSj7_DiPqy9ocwnfe8Z5AwFeSHt8RlV8C5ri5SkAXXK55t252sMoB1BL1RItSvvQQ9zO3zQJfssRRR-8kUAJ_-ILA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
🔴
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
🔴
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
🔴
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
🔴
شمار تلفات هنوز مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130329" target="_blank">📅 16:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130327">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9KsudorPoSM-JdC9319HZYImXA1G0pILXnoxj3TXrLTKFh2OrZYC2kPR63bAb5NiNVXBM0T0io1XlljBQizcUhVKqYJ6eZ_UoIbT-RtkFIQ_ZWcQbAzlrhcp0FcehAuNN0mV7sJFN_nlKFS7hniZfUVBNyxKUJXVvNpbc_YXCdITLu0r28UR7Tow3rI_qXO22YlknPYY3es7PfamOPNNAt4wC0nr-Un01SbOcWqtN_gUcsMxEk_OtmV96nd3COPVn4_qGTthX78RzMizRKNbj_9wRcUNb-FE27vvBVdSvnkEcJbOwo-qVvCCr02GO_aU7q6x4l4wJ4nB6MuVD2FmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازی ایران و مصر که به عنوان مسابقه «افتخار همجنسگرایان» نامگذاری شده؛ فیفا اجازه داده فردا همه با نماد و پرچم رنگین کمان
🏳️‍🌈
بیان ورزشگاه و معلوم نیست صداوسیما چطور میخواد بازی رو پخش کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130327" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130326">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=FIVnxc69AUCo16QHIT-ubrKd1cxzmqPDN0D6iPnWn5AIIYLgLVJrkgpr_HK2R3Y8_PCRbfsi02v36JMjif-ZdwnNSLsAj2yEzQmSjVACi9OoCPS2iwaiuA5262s0rLHaYcDS2hwGOnh4yrPcermgBPyU_GFITOxXf28FcYSSYbivHs5mRt-vL4-tQHGsmRae6j0aXbnXfG2ry-5RaM-IOvmD9-WyePIsHm5J8NfRzZPxYKC3iqB1v3Uk5ej5eUz5TlwXqXlzi3_z8pkvoKov3TbSHlubCgk576sgD5eogfNTKPRXJ5yOqwRLX7jvHxW4gha_PVl52uBcVAaYMetyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3a84c436.mp4?token=FIVnxc69AUCo16QHIT-ubrKd1cxzmqPDN0D6iPnWn5AIIYLgLVJrkgpr_HK2R3Y8_PCRbfsi02v36JMjif-ZdwnNSLsAj2yEzQmSjVACi9OoCPS2iwaiuA5262s0rLHaYcDS2hwGOnh4yrPcermgBPyU_GFITOxXf28FcYSSYbivHs5mRt-vL4-tQHGsmRae6j0aXbnXfG2ry-5RaM-IOvmD9-WyePIsHm5J8NfRzZPxYKC3iqB1v3Uk5ej5eUz5TlwXqXlzi3_z8pkvoKov3TbSHlubCgk576sgD5eogfNTKPRXJ5yOqwRLX7jvHxW4gha_PVl52uBcVAaYMetyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده تا از مزایای عدم توافق و مقاومت و بدبختی بگه
🔴
نون این جریان تو بدبختی مردمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130326" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130325">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
مهار آتش‌سوزی در پتروشیمی کارون
🔴
روابط عمومی پتروشیمی کارون از مهار آتش‌سوزی امروز در این شرکت خبر داد و گفت: این آتش سوزی تلفات جانی نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/130325" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130324">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ایتمار بن گویر وزیر امنیت داخلی اسرائیل به کانال 7 گفت: آتش‌بس در لبنان نمی‌تواند پایدار باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/130324" target="_blank">📅 15:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130323">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
هم اکنون، هشدار تخلیه ارتش اسرائیل برای شهر منصوری در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/130323" target="_blank">📅 15:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130322">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فارس: مذاکرات بر سر بحث هسته‌ای برای بعد از حاصل شدن توافق نهاییه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/130322" target="_blank">📅 15:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130321">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955a11f8e7.mp4?token=MT67oYDsz1A1Jsl7X5_4bai6SAhl51c3XsHbRmiI5ZXpOwhUHoCn22N8KwexdBb15bqCCCyNGgYR6O0JhFsmYaCpl6AOg7aRLIzsihaF5XsjVZIUtOQoo0ytp7NR_4ElHCxY78z0rn8OkAWT8nqmja8-pOK7htLY3-nViZ2hsyI1b4OpsHqZZzAPdUgHERVHvBdI0NhmzBgoD99Tceq86_WKxVqtm0Nsf-ZdG18LP3Oz_gsHyQwD02PDO3rOctOAIrHKquyhYLLEZvnrcv9XjHiBD63mGyFYdtmP9l5yTtLpfFEX1Zg1MNylpRaVtkP7ncBSoM7LlyBn5vadPqsHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955a11f8e7.mp4?token=MT67oYDsz1A1Jsl7X5_4bai6SAhl51c3XsHbRmiI5ZXpOwhUHoCn22N8KwexdBb15bqCCCyNGgYR6O0JhFsmYaCpl6AOg7aRLIzsihaF5XsjVZIUtOQoo0ytp7NR_4ElHCxY78z0rn8OkAWT8nqmja8-pOK7htLY3-nViZ2hsyI1b4OpsHqZZzAPdUgHERVHvBdI0NhmzBgoD99Tceq86_WKxVqtm0Nsf-ZdG18LP3Oz_gsHyQwD02PDO3rOctOAIrHKquyhYLLEZvnrcv9XjHiBD63mGyFYdtmP9l5yTtLpfFEX1Zg1MNylpRaVtkP7ncBSoM7LlyBn5vadPqsHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی سپاه: عبور از تنگه هرمز فقط از مسیرهای اعلامی ایران ممکن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/130321" target="_blank">📅 14:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130320">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d81ff4ef1.mp4?token=bjc4NjpMm9qYenhPQc5aLLH47bUuWpI7q35c6PrHCgLYdN9CST2mxS5k3VFmEl_M8HFCjAxzOTfb9IqACihdjJfkRlt3VYeQh6sfoPXzZu9aKwlCf1m7X0gizaZ0rVeeZi4rbM9At-r7vGCB6oUi8LBrEABxKtEr7Y0CRqLE7wxWF-J6WXXphOwANlDsDa4ZioMcVukgqcosAa7QBbtx0xvyPF571xpE80mwpwgDjgV_cDZWllilLKa_EqgzDtHxhDvW-KXCML6jEYRmjOjFPc9G_F8b1oIDcW8Cb8mTj-z_IcwBy3I7mARQV_Zaixtx5Pxcgw0Og1cJ1QGrMJZBCmbboCk0jx_Gdz9RXRwwWX_Lr4sgywbqyxdLJVIOE6Eygg8z6gSr7oJV02P5ru6Ds7BhEVWf6OEmvnPY3RSLAp7_qjmMhLzaeD0TmTVb-U3QsXCvpk3W3tAsNmMBrzXA9Ujn8uY3RuMSCBNO3dkkNeES0JMWOotWrVStJ9peyGM1GZOwfxZhQC09uJYe5yDuhZvzPpd9oX9A4S4KWyWgxe4Oi90GtJPswvBgBp_5lM3L5H-Z4omrpOAXbW2s8YAyYZ8Ja56yawpW1aYJ_LdK9XDtyIB2s4dQNu2Br766u4Idz9dBhMZj5Bv4oyi6VGaJq40dZ_jpSCLqpRPieHGZ7AE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d81ff4ef1.mp4?token=bjc4NjpMm9qYenhPQc5aLLH47bUuWpI7q35c6PrHCgLYdN9CST2mxS5k3VFmEl_M8HFCjAxzOTfb9IqACihdjJfkRlt3VYeQh6sfoPXzZu9aKwlCf1m7X0gizaZ0rVeeZi4rbM9At-r7vGCB6oUi8LBrEABxKtEr7Y0CRqLE7wxWF-J6WXXphOwANlDsDa4ZioMcVukgqcosAa7QBbtx0xvyPF571xpE80mwpwgDjgV_cDZWllilLKa_EqgzDtHxhDvW-KXCML6jEYRmjOjFPc9G_F8b1oIDcW8Cb8mTj-z_IcwBy3I7mARQV_Zaixtx5Pxcgw0Og1cJ1QGrMJZBCmbboCk0jx_Gdz9RXRwwWX_Lr4sgywbqyxdLJVIOE6Eygg8z6gSr7oJV02P5ru6Ds7BhEVWf6OEmvnPY3RSLAp7_qjmMhLzaeD0TmTVb-U3QsXCvpk3W3tAsNmMBrzXA9Ujn8uY3RuMSCBNO3dkkNeES0JMWOotWrVStJ9peyGM1GZOwfxZhQC09uJYe5yDuhZvzPpd9oX9A4S4KWyWgxe4Oi90GtJPswvBgBp_5lM3L5H-Z4omrpOAXbW2s8YAyYZ8Ja56yawpW1aYJ_LdK9XDtyIB2s4dQNu2Br766u4Idz9dBhMZj5Bv4oyi6VGaJq40dZ_jpSCLqpRPieHGZ7AE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه ۳: این تیم پیر دفاعی، ابزار بازی جسورانه با مصر را ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/130320" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130319">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V05oyUP-t3j-gStrFqT_D0RhOTzWtyI2yIRc_ZEdV-AREmVvO2jOV4OCtKuTzUS131-MQXUbdnA5XPpja8jBZ7NJJQzQaGcBmOsztLmh0CsrRf5a1XTrKxi_PGeZHes2-wT3iufUxCqG7v3Uqy7oQfp5JHwHop9NbprjSQCeCMsujDrNT0bnqyoIA-w9yHKBN39RFQNAF8coe-ulLCszSVyf2RZ8V0EeU2YTY7vbAjhXqKx2pivCxoox_Yu_LDX6S0a37qQG1RanLPetaA67os75LizaglL_y7jXRchTIplMpXj7UduTrOFOsliE6qVZlys8siLH5Lq_fShZWmUboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آغاز پروازهای فرودگاه کیش پس از ۴ ماه وقفه
🔴
پروازهای فرودگاه کیش پس از چهار ماه وقفه با ورود نخستین گروه از مسافران و گردشگران در سال ۱۴۰۵ از مسیر هوایی به این جزیره آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/130319" target="_blank">📅 14:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130318">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل:
در طول این هفته ، بیش از ۱۰ ترور در غزه؛ ۶ حمله در جنوب لبنان؛ بیش از ۱۰۰ بازداشت در کرانه باختری داشته ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/130318" target="_blank">📅 14:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130316">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSrNgRpgQl9SlJFl5H2FAhL-BXPXUqbomTK-Zr94kx3YdQWG9Dup_vipnV169mjzrHDNvJeTs2Wfv_uNhXFD0zbbRynEVAGpkcOP1JnvnFBlde-x21J6U81zquebGyneff_nSTk6SjY-DHDUGx7gddrX1P8CUZwz8fT8BsJq-cnWmhCF6oCtBxZXJJ4V3yrQgMmYJpDkaQHRfHezqoq9fEJRr0OEfiG3VUO74Oj6uIuJKl-o-1DZAV8JgQyN5oH_7Sk289XoSYevzg_C6dmbziWDeqXj6t2WchSKVmcm6_JO0YNwyQZO9tgkLAFOhdurznEmuVtWorMdti2OjP_g3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس شِلتر:
مذاکره‌کنندگان وصل به شبکه یهود هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/130316" target="_blank">📅 14:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52da7df95b.mp4?token=O83G5KsPAamuItBWM0UaVKXeLEvVXeIbiQEIWO14qNFNFYziIwFKFrMQO9OOfDVrLd-RpyavfLV3QtfNk32aSbliOgA0xACUbCFQ8IF3PIx021j9FQttH5XBeE3KViOZheEMm8GGiulFsTInzYftBC-2dmapvXYFlsh04YQVp33boezZi-1dAV9D6TSMSNPdzhBILPBRsu-7xp3V5Il4zoBAhEIz5r_1nighNOLvK0ryHgF2Fn38f3NB-uzzG9LwDm90BNMhyKZ8EMetnN6ZFpmVu8SUKNgZ4TVYGj9AH7g9XnrUzW7w_Ujlkto26FvdhW4HISiSOjurUoEAj3Kc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52da7df95b.mp4?token=O83G5KsPAamuItBWM0UaVKXeLEvVXeIbiQEIWO14qNFNFYziIwFKFrMQO9OOfDVrLd-RpyavfLV3QtfNk32aSbliOgA0xACUbCFQ8IF3PIx021j9FQttH5XBeE3KViOZheEMm8GGiulFsTInzYftBC-2dmapvXYFlsh04YQVp33boezZi-1dAV9D6TSMSNPdzhBILPBRsu-7xp3V5Il4zoBAhEIz5r_1nighNOLvK0ryHgF2Fn38f3NB-uzzG9LwDm90BNMhyKZ8EMetnN6ZFpmVu8SUKNgZ4TVYGj9AH7g9XnrUzW7w_Ujlkto26FvdhW4HISiSOjurUoEAj3Kc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم وایرال شده از صف نذری تو الهیه تهران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/130314" target="_blank">📅 14:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130313">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4fae070c.mp4?token=SkAc9JARKJ-kJuMeLOgTsp45qDufeAXe8gyMome6vqrU_WySEJ4ZgfktjBm1uR7HWAxahAUUNWnzfP2VdAenMFfEauupRzVeEBXxtETTq6O-7V2JD9cZGCrkTDId5YNgFhoI06vGA-YFMk_pcSGx30JSk4bcLx9dRionjn-1nC0NGH0qS2OLdMSqg3OWy56gGXot3BK1wjpZ9tuIhBgn9tJVnsXQceMo16RmOsgRg2OYsZtxrR9tNCcP29Qb02LY75iGqmZ3HrUaV3oC7eVduUpLCmwdqr3FiacUeleXnOio9LT6yQKOVidz8xzUPwB7toTjSCOF5NuUBOt-9eIZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4fae070c.mp4?token=SkAc9JARKJ-kJuMeLOgTsp45qDufeAXe8gyMome6vqrU_WySEJ4ZgfktjBm1uR7HWAxahAUUNWnzfP2VdAenMFfEauupRzVeEBXxtETTq6O-7V2JD9cZGCrkTDId5YNgFhoI06vGA-YFMk_pcSGx30JSk4bcLx9dRionjn-1nC0NGH0qS2OLdMSqg3OWy56gGXot3BK1wjpZ9tuIhBgn9tJVnsXQceMo16RmOsgRg2OYsZtxrR9tNCcP29Qb02LY75iGqmZ3HrUaV3oC7eVduUpLCmwdqr3FiacUeleXnOio9LT6yQKOVidz8xzUPwB7toTjSCOF5NuUBOt-9eIZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن رحیم‌پور ازغدی: تُف بر روزگاری که رهبر ما را شهید کردند و ما از صلح با آمریکا حرف بزنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130313" target="_blank">📅 14:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فارس: درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/130312" target="_blank">📅 13:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td5w0i6mXR3I3XlY6IQZnpswh_3mH5aWdgjCtqNzsj_4lpWM684iCnek6dkcSBBALssbyaZBthWDyLsEaRHRUAMP-aR9FkwrELYE3bm5G2dCYIAlQ9bVsSu8pVZwOLoq3aL-DfFgOYH_EcBN5u3C0usOxvm999i5GQli_KvPw9PN-lYYH4qqG6mcPzFbP-6uLjtFTXgkyp93ftEwaaUVSLHcuA_nw5hFklhsImbSDwWfUZKEjh8Mm2aIcRL0kdxpt7VM3DilxwYyXBUW3sYb7z9govViCUVTIG8w00fEv2Vn8kLB64u0OsHhh2TA_uOhFwTvG7UbMjM1l4cfxOyhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
ما یه بازار جدید داریم که داره شکل می گیره و اسمش کشور دوست داشتنی ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/130311" target="_blank">📅 13:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO7wpqCLsEte4KfuMUExYgHP62Hl1UbZagm5nfCTUVG5jopjTYmbMq36RQnz2-GUOczeFiRF30ziduo9w3DaDSypfnJPwZ4F60kqcTzYe3FUN70vSGuRs7AQAYQ5Plv-MtiP5fxUFMtETP51b-9N3ny6GUMOy_C6F7W-DbysZsW5vTa89aW6qRk-kSsa7_l4GveKFOBVPQJCW54PfFTdd4yh_DsxuGxgDV6X-mFzNNs1eQ2r7bcySQqjCqBNgeTzVZxhFQLF9CuxsVTRkB0MQKDT07k5Uf5rON6nR_rcBQWIV1d3Z18nNjXI5mzgglSgIOmdoChxe4GXHMjhCcrbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: امام حسین هم روز عاشورا رفت با عمر سعد مذاکره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/130310" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=Kg35v6ywghDE_kwNMEul_s8Y7-vubLcR6a_EHEeVB5MrwdCU44-6soYkeQX5-XEHQaycFFFXyV3g75pAZI7HJ07dP98wSx48JfI-yJ6_TIqFDulJBIRVOETGRnACSUF77p-vWiMI-9OlA0Wu2mf1D0A3MsRb1BMv7VZK-NVqVTu_hgMnJCg-WQRTKq0hMTXwptcafNaXIMlgHKOvFdqMkaqaDGsI-rsqxMkX2raG7TmWNHkPF2uXeSGPfkJWOeJL5JmYVC6XI0IdlXzykH0TjTr-_uL8gZzWs9TaIIjbrUpAOwesv_tQfVwoc03prW3ysR-tCRTTimTjgfFgWLTh8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=Kg35v6ywghDE_kwNMEul_s8Y7-vubLcR6a_EHEeVB5MrwdCU44-6soYkeQX5-XEHQaycFFFXyV3g75pAZI7HJ07dP98wSx48JfI-yJ6_TIqFDulJBIRVOETGRnACSUF77p-vWiMI-9OlA0Wu2mf1D0A3MsRb1BMv7VZK-NVqVTu_hgMnJCg-WQRTKq0hMTXwptcafNaXIMlgHKOvFdqMkaqaDGsI-rsqxMkX2raG7TmWNHkPF2uXeSGPfkJWOeJL5JmYVC6XI0IdlXzykH0TjTr-_uL8gZzWs9TaIIjbrUpAOwesv_tQfVwoc03prW3ysR-tCRTTimTjgfFgWLTh8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسم محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130309" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130308">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
حزب‌الله: با تفاهم ایران و آمریکا، ما به یک پیروزی بزرگ رسیدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/130308" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130307">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh8c7Q2Js99enYX5dd93_2L235xob4WFZeovi1UVGHkpXcy_xkeZYqWhnTBCI6pfsi8dkLAk5tXXxHnBr2_czsZ_Iu3Ifgxz9j2ucGV3Y47enPkSipzxY3IgCT-enQez8mm4240dUEQ9Uwmvage5Ak_8sL42bhrDFF0Wq1AV5NK5fwXVX48maXNqu2BqwNKeg53jLbkudO068WPUhyZHDeSeY8kI2trhipkTNgg7TDXuK2ssmpLhoUWYsDDKOk664acsMVcQs-j6O03o33stBI35znWEyVSs3x7_3NXgbqnFs43zKD-HFPYICH3g2wGsALnwOqlRT1RSrQpdgKPdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۳ عبری به نقل از یک افسر ارشد اسرائیل: فروش جنگنده‌های اف-۳۵ توسط واشنگتن به ترکیه، آزادی عمل نیروی هوایی اسرائیل در خاورمیانه را تهدید خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130307" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130306">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/130306" target="_blank">📅 13:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130305">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=Bi6Q6dhfCvKx-c05tJIxAZBbSzcjRPSah88e0SOg-fdC80kJtLInzMONL720yr1DU1xOfhu9baZJo7kSNlgVMFi4Noj-cZ1aXQlcqu3v0qGOYcXL7e6AtVtkxYAEqvIUIKfbRnXwJwusSvvZJW1gsXUGF9wL9WXxuIzBh2RkKwIDlOvSOrlGvtya2JlO-hjUIoV_U94wWwIpqhCwA98X7jaOhZ3oUivnBlz6fog-hcgof1zp8V95__lsA9ZrOWm9l6c8seLwvLuiz5aX-sYiv4noArQBh_uHWT9g7ZUTK49XAYQJoxOfAkJXoJERo3N-NQMYD71yOC8BCI3j5Krv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=Bi6Q6dhfCvKx-c05tJIxAZBbSzcjRPSah88e0SOg-fdC80kJtLInzMONL720yr1DU1xOfhu9baZJo7kSNlgVMFi4Noj-cZ1aXQlcqu3v0qGOYcXL7e6AtVtkxYAEqvIUIKfbRnXwJwusSvvZJW1gsXUGF9wL9WXxuIzBh2RkKwIDlOvSOrlGvtya2JlO-hjUIoV_U94wWwIpqhCwA98X7jaOhZ3oUivnBlz6fog-hcgof1zp8V95__lsA9ZrOWm9l6c8seLwvLuiz5aX-sYiv4noArQBh_uHWT9g7ZUTK49XAYQJoxOfAkJXoJERo3N-NQMYD71yOC8BCI3j5Krv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130305" target="_blank">📅 13:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIFTUzq6LDictYI2iae1OyxlDffoJ79MtEyOkfwhL7aKIggo5PIMSfVANkSEnCZdhAaqNquXYUhmXA9MZ3s6Yx_7-dZulbCEEuzqZacLmCbdvconkw-oq400yH-FAg7bkpFIeviknEi5Ptkc-MDBGSNVsT6FlI7kVbkS4_7s24RxL7pRd4XwvRvzhl1muNu7ScGYRx8f9orgFa-obIZMbwYK0RP6A3pRxyuyjzvcNtLE_TqfVGJbeaUt-5-NArYZIQsm1D94I5Y18jj06WP78sHqIQ6Y9tk6XBK0UnRlNA1maD8z4UefqU9fi1T-XApezY5aFOFHCsjolAIX28IEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAYidsAlDF6XIv8vbtUj37NKpwoY8nmKE7dw20SPCllxw0mulWt71CkPLJBeh4WW3Ova8p9o0U7y-ou9es6WMJ8z-ds-9ShP7EzFC8OpfhbhJMCiXZmhysdLPKvf8ThrX3Mm63iIenA1wwnhGX8_IRCp6pHc-Csg_db_t87sOUBmNvwHzfE_SAVLRZrnDsHJSUsYLEWmicTMX1B-a4lT0mbTJmqnsO8rKUdLWWD9ywUEQadxHtwEu8WmUUTEcVWkVOVNzCKzzL6INHVHWD2ib6cqFPEeK5D2lSncAuVEODZLVsD3AT_4MWzkbsxP4wrD5dk1gbDT2v984yKmtDZweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oIPOgr-bjG1Tmwmi9QDtHkfcFIhSzK5RqfUtYa2fcwNhPFL50fKjevydCUM5hsPPNFEC6kmqFRxxCTqZw0UPff5jkNs2IkkmgMj9qWSnOJwX7bDp0YV__32DLftfzRMF9ruTY-tl4PVp216Rt0xU1K_i_UEQiq1Ohg4_E2-iuzk8AUW_grzoDgiyvEhGQ1wkJu77KkuQ53pni4d7uzrtoFcZP-UvitdfdPU96astSUcUWxEtJ8wc0Xj8N66KWzTWQK9WS60fyObyaCMAmh3iiNLyiUrF01Hwod36dndoaWGU2fOekVIxxlFDaGonM8ukbsfhQ-blWPU62c4zjAcMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a25pcOGrmew_Prsd01rHY5MD61n24LsATmrTM2k4G3Rf-hfJcoHvPHLOWhXqWnwRHGIMxM3hHvxdDWM72CsxLwtYOvoaoNmlL_fyoRIrJSzm0jRVRSflFunbIhmaxLhf-mcp_rl2RV-9ezQipfJHuQF01pjK46iYYeCV03obsY2b2An7yA0on5Yk06lCsgqyrx5L7B2gYAqTtlOMAq6jw67t5JrchKrT0ahbgksN-sHPnkw6GmBrYeSChcolMP7kVmZdvAiIREE_7fcEuLVAOcLmFhq1rr2l5aQa8h1q838s2XMW129zLZpoF2aDdi2FaX_vAY_VUjBz3YrwPBwnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqGRiRmdLNIfpwcQFUtf12GMcGyqOBvUsxjXrb9uLDmNvp1CnGyybnCHJKLxey2JG4kc3C_H19pY3ZhnQFxAJ6rNWsHbasQbJDep-PEdbShbhdnohxMc7SVP_Ap9-BHbKrW1qddf4l3BgDDjzaoUo03uKzjl1ZzlS10k7kSLLKmleRXm1DoNYZNH133BTBIWLGysD_ojug9uNaBR1RuKiF7FYlPMfCPSIeowdyGHN_S_gNsFFtsxRbKiOY0JpMncqDIEPEeZ4VgXNp_bdROJdKAgDBs1dvPktDLwqhco5-hPDHqDrzFwKb1orCa26Zzgldf2BDe7uIzCcKXLpXaE4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید ماهواره‌ای از خسارت های سنگین حملات ایران به پایگاه پشتیبانی دریایی آمریکا در بحرین
🔴
در این حملات، ساختمان فرماندهی پایگاه، دست‌کم ۱۲ ساختمان دیگر و همچنین دو پایانه ارتباطات ماهواره‌ای به‌شدت آسیب دیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/130300" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/130299" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
طبس گرم‌ترین نقطهٔ جهان شد
🔴
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130298" target="_blank">📅 12:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb6nqcc6Urv7XlZDHpmcy7DeAuQFlrmbslb--Z13cS43iRRtMYR5iv1Aq-YMXGjFtnBsIqiHIgLa32JK6IooGAOeeYhdUEdjmp5U1RlLAsW-5x8I0k-ufWJhTlaQxDxLz-qj4axfvm2vdO0WwIu99DhP3-7ZOp7mzM6T9ulBI3b_0zGl8fZB6PE4EZ7tH_-G_eVmO2cbKzV5CJq2Zuy7E10jm6sGbgNEU5Y32texm1g-xYT8cdcykURQfCA2YjMyMgq7XvFcMm4IYi70ZAi-S_sq1vIK-VJ6qqoZCuB5U7fBVCgJKgUf1H7YzvjTzBFOFnzo3VJGRbnWZbdNOqiieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده مختاری، خبرنگار: سال گذشته بانک مرکزی رکورد ۱۵ ساله چاپ پول را شکست
🔴
پ.ن: چاپ پول، یکی از اصلی‌ترین دلایل تورم در حالی به اوج خود رسیده که کشور ما در ماه‌های ابتدایی سال گرفتار جنگ و محاصره دریایی هم بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130297" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عراق شایعه خروج احتمالی از اوپک را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/130296" target="_blank">📅 12:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=aSkhuVqdYf9-ea2a4m0ETE46LeaUqSgkZzK0UYwTCAl0FES2FA7WVepIsBTfrNhaPVt8p8vJdliOHDR0qxWloXfHVEH9U9ccz2V-pzRz9F7MOZwcxSmZDVQzdGnab95hEM8YAuofKTJw_PSy3t-cDxOBC3ES05mEE608gYhKcke3pZd2Q1sYM_6ibeRJkuNdMQaQOGKTkfHqeAhZNeDzh5YocmIEV1HIBXNCeP2hCysVRFiLJwVc-tSmXeJxw8tcm8NhYD6BNnYsmK-fiuULEnv07KH4prpawL8s0UB9xpEN9mMYIRI98iDH8xsrkuXnALoN6vRUDfcI6FJq9a8irA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=aSkhuVqdYf9-ea2a4m0ETE46LeaUqSgkZzK0UYwTCAl0FES2FA7WVepIsBTfrNhaPVt8p8vJdliOHDR0qxWloXfHVEH9U9ccz2V-pzRz9F7MOZwcxSmZDVQzdGnab95hEM8YAuofKTJw_PSy3t-cDxOBC3ES05mEE608gYhKcke3pZd2Q1sYM_6ibeRJkuNdMQaQOGKTkfHqeAhZNeDzh5YocmIEV1HIBXNCeP2hCysVRFiLJwVc-tSmXeJxw8tcm8NhYD6BNnYsmK-fiuULEnv07KH4prpawL8s0UB9xpEN9mMYIRI98iDH8xsrkuXnALoN6vRUDfcI6FJq9a8irA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر ، جبرائیلی: اگه قراره با آمریکا ببندیم؛ ظریف رو ببریم
🔴
یه بچه و بساز بفروش و پاساژدار رو به مذاکرات فرستاده‌ایم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130295" target="_blank">📅 11:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWhUvMHY3zrNAfUAJsjYXZLw5sDq6wDfJs1s75LHojxN3_aH51g5NEKsXlEbVwD_g8UL2Z9Gw7PWolF1gcWZT9Xl8KmMe-hp_ydVwuzMU3geOPluCnDaxz3w9-6n26MxVGfvcUWAxnUBuTB9eGDu6hV9LyldjN8IjElT0zprxPp2qL0uOo4-Lwpq1ghzV_ILJ6lI_xsr4LSH3dbfwwgftyHnmaXa5fmGKCZkzu7i8NvXmUvISaJVq7ttf5-KdfRS6_KTuBpKb9TWWIGlYh2EfJJ_4rfyyiYqHze0C7WKNdJFuQRFitZQFV7A9ymKg5300tPbcAUF2crR97xrNbTlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: امام حسین سیدالشهدا شیعیان بود و امام خامنه‌ای سید و سالار کشته‌شدگان انقلاب اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130294" target="_blank">📅 11:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAe2j0ILxVMs81b8jXxDH-Ha46OuOi8cqBqGjiW7eIsTmr6C-rPameF82WhZtJZYfPSA1rIFUH4Nhavlq2Rdb3jBj8fTOseC71_whcBuSGekKtureeQsWm2CPIm3DXntCuuaZz33KQimTdMs_29skkStDKrmCoNNPopGwYZ9TNljJ6ds2hVH_qOrosofy2s9dUaotXgQQjfY3ZyxpkhFcGpumtEfIalFK63R6M2d-l1sZeuLMCs88tHUG9MfxxfjwASWL8cV8VkgCb5p-ajtBQ4G5WNOjcRsaYq3BV6y3NgeWqPKuBXhjH-gmBjEpUScaXVTukCDMuKW2dw982NYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ زلزله بزرگ در نقاط مختلف جهان طی ۳۶ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/130293" target="_blank">📅 11:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا اعلام کرد مذاکرات غیرمستقیم میان لبنان و اسرائیل که قرار بود روز گذشته در دور پنجم خود پایان یابد، برای چهارمین روز طی روز جمعه تمدید شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130292" target="_blank">📅 11:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/130291" target="_blank">📅 11:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بلومبرگ، با استناد به داده‌های ردیابی کشتی‌ها: ترافیک کشتیرانی در تنگه هرمز روز جمعه در هر ۲ جهت ادامه یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/130290" target="_blank">📅 11:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مذاکرات لبنان و اسرائیل در واشنگتن باز هم تمدید شد
🔴
این مذاکرات که پنجمین دور گفت‌وگوهای مستقیم لبنان و اسرائیل در آمریکا است، قرار بود روز پنج‌شنبه در سومین روز خود به پایان برسد، اما اختلافات همچنان باقی است؛ به خصوص در خصوص نحوه عقب‌نشینی ارتش اشغالگر از جنوب لبنان که تل‌آویو همچنان بر ادامه اشغال این منطقه اصرار دارد.
🔴
هیئت‌های مذاکره‌کننده لبنان و اسرائیل امروز (جمعه) نیز نشست‌های خود را از سر خواهند گرفت تا به ادعای این مقام آمریکایی به توافق دست یابند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/130289" target="_blank">📅 10:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌: تحرکات و حضور هواپیماهای نظامی ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
🔴
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/130288" target="_blank">📅 10:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1VZf-18TGPgrRU1lqHO7uAJ2ux4SOACPWDIwMQDg4QefrX6t1qDaDUM9MHwegzQAqojKhm_NyB5n6KioncVJEuzhSrAqIpLRQQDBsm4dHEkVgih1hi6gsdC8jbGB2xeqvbWLFIVR-Z2RihwmyFJ0FQr0yr0v_cZv-Qeu3qiphR1WbOxOp3DSWOoK0cACt1OBIKK0d3gJTP-GBi0hpmNE0KQvTslNoTCSjMQNWbs0yA3YlUeSDGUdwMiqG5Mj7lx-lC_QCCdx5Y0oFftW42MjFlyWPwcJGc3wJ6VxJrKwpeIq3NcFEYyupSHlvOiM1XPQGtxAZqX4XoV7vSJN0iTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان پیداش شد: مذاکره‌کنندگان برای هفته بعد قرار مذاکره گذاشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/130287" target="_blank">📅 10:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCb4d0t5rPYJejUaReA4EZne6pz8UmpnCx3dXHZHsRdhSi3BEqwv_552s6niqr5R7DpmvYb0Z0Z_fip297HguwGhsitDm_kbGmLxj5lrpANFObnI2_MNOmPy-NVJEAJVM3Wvy3yPmamj1rmjOK_8CBHvWA6q8pPm2F0LlXccOS3ZD7sELE9iZJLWoRLNp92G7PLFbQWDjDfI4yQKg5g_-iPhF7vveNB9yd33JLnowbW5uRYsOrBJtUCLvUx6SPpGGZvcRYK_BvGAdzdJY3GrIqc9khnY4NnzAGuDh2Jcs1SPAhS6JIPWbd-jrQDUYGOKBteYA3_cus-_PaZuA222ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAGzTg_QFJGzmHVr8qdpzDlG0c6vDItGL-4UnJDxInbenwldQ5nBKPANlOOs3VTD4N_WK_uNouVjEmurrXvd6ScA2-jrwHBh0IAryk4d4Fg30n7yrlrSMnHeq5ViXI0EeldYLtoq8CjnzQmRFi1W6t8sQ-2PJ5YyhKfDEjFHYBV9RmTkIZsmetYO2qzJUHwY8aVWt58pNw82_DeG4NlBypLg1NlQQBA-dRPXET31X09sIo-PQxH7m3-d3X-RKNSiaJjKAyhpw7XqzAOuDCEObmh5HgV1m07p4LclI9RBZS1iQSxffHd5lEqx_fr8XG24oLzt5xyr-JsmDFDrANgfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ki_DQ5RTN3C65P3qKHuA1tKvp_E8f2MbF4MFcQxaZLAtilY21PYnY0bvhSiV8N9yPeaDeYsvICpE9MPEirgCY4G1Lq4gBfEcNG4GxLjIe96C7bSLdLbNfoUWdo7FKGXH-jYCsBwKgBr3YBODjxUuxvFyaYG0F-AKsvffwRN1fIUq58682zb5rAdX1jbV-TJcJ7o0zNaQoAKB1ko5DJrmoKNFeK4Cva0qcPEscxos1elDCxFZQ8i97PUjuZ1-HqlL1_-4g4D81766C3ZUn7wku6rKKvHbxiSgfvVmtXkFCwdRM37LCry2kEl2Zx08eiXACcLMKuE91vYI0tOrlcvCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHeGVN7pSAqp5wEaZQMs80s1qfxW1G66OaNl8xAUvXOTPc5nE-Etx-MQYamqwzKRsmRo6OcummNXvFeF7xKTnBxj0zseHQfdxIDYisuM201iZ1c1jNT3zCqMZ6UKsW7688NprgoSGUzQ8h66n13c66pCuBrvhAKgQBsIqQNLZSzQ47ZJqXbWaECH099FKPMzcHwQ2jx5MuEyyA5_HK6rYVM9J-JK5PVJ5-MCgmmNky6Bs3lSAGsh4SWLWTHukbWO4vCSQ5hPr0xzWl8zd1HCACuuaSegZbQUHaI6rHbmOBTV8yM3HOylKM9AEN5tV83AU4-orFK-UlliHNND9EiZGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون، رهبر کره شمالی، بر آزمایش‌های جدید پرتابگرهای چندگانه موشک، کلاهک‌های موشک بالستیک تاکتیکی و سامانه‌های توپخانه‌ای با برد افزایش‌یافته نظارت کرد و بر لزوم تقویت قابلیت‌های تهاجمی «مرگبار و مخرب» کره شمالی علیه دشمنانش تأکید کرد.
این آزمایش‌ها شامل یک پرتابگر چندگانه ۲۴ لوله‌ای ۲۴۰ میلی‌متری ارتقا یافته با سیستم هدایت دقیق خودکار و برد تا ۹۰ کیلومتر، کلاهک‌های ویژه ماموریت برای موشک‌های بالستیک تاکتیکی طراحی شده برای وارد کردن «خسارت مهلک» به فرودگاه‌ها، بنادر و زیرساخت‌های برق و گلوله‌های با برد افزایش‌یافته ۶۵ کیلومتری برای یک هویتزر خودکششی ۱۵۵ میلی‌متری بود.
کیم گفت که این آزمایش‌ها پیشرفت در چارچوب طرح نوسازی نظامی پنج ساله کره شمالی را نشان می‌دهد و «تغییری در وضعیت آتش در مرز جنوبی» ایجاد خواهد کرد.
او افزود که سیاست دفاع از خود پیونگ یانگ نه تنها با هدف تقویت توان دفاعی، بلکه با هدف ارتقای «وضعیت تهاجمی مرگبار و مخرب» آن نیز هست، به طوری که «هیچ دشمنی جرات رویارویی» با این کشور را نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/130283" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل به نقل از سفیرش در سازمان ملل گزارش داد که طرف لبنانی اظهاراتی قاطعانه مطرح کرده
🔴
وی افزود: «هنوز به مرحله صدور بیانیه نرسیده‌ایم، اما درباره مسائل اساسی گفت‌وگوهایی در جریان است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/130282" target="_blank">📅 10:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIvjeoERDeb2eLjymFJ3Xap4OJz6m3yjS-v07_DRfb7G8jJq9-4ig0CYJsoR0MVOMVB0a2NRLUrmdERbKA4BfRA1T9HktbJjpPXyY7TwHYCH6fvwHf6VTrXmc-mFGfpCSHL_bWmdtDtY_kRPYZ4fcs1rGyd_J8xHnu0iZEZLpUuW_e0B92igp1Q7h3kHAbLRl4o7Gci8FW2tz6JfaBC73ek8ErUHV4Mx9Mxys8QEh-2jdXeEMDSwI4dzIGcFXN0tOXiJtysspHCA3U5FXa79Dta_650MfeN1-abSiHAqQQXz22PdCBZwi4sNWlNRrLwN8HcKrExjGDgqusLiyQGvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_zxB-l69uWgloqYe-EM_QdM1izQXVekuvctz20haWYLIb4cdWN1q1fXcfLDUK5ahIrPLtDmCpEarlJQSujBYghbaTS8SjnJananP0kp_tlo3fk1egoKNyEaMRWizw7_PR1wRWKYxk0mHhamjOpjcAopJu5E4cqb469RLpB0TkHFbhyF1_ASJk0Wsu8Ftk96LcarZhP3U-ku_Z7G5ZATX8txhB6Yhg9ze5Q0EgaVBOP_gRCR85jo1XpIjID3Fss4ysmuX1uFaHjiYqHFdqokkuQCrzHiNLPZMyGZRTq0d1SuO3Viuzi5MYEBnluJspIKoAp6D6L9Q-yHMd4N4MIeGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bc2eaf0b.mp4?token=nQbSN4ynV2jJMif_0zVNr4uwFaaQniz2G21L6wfStxkZ-ow7Ak-leZIcA3EJVA88S65oOioO6h15fQWZvZlm2xlVKudS8TOd80kkYlCDMa4Xw1-W-84347dVAL1UQZ9HY51CS_o-FacSmIHu_518Diy44CmUmtTLPlhdu-84SassFst5pmc7xEYlVmTlU7kCp7wliJl6jpsdBEuVGVWNeICjl-s9E3-GTF50XkJaI0RxrQ5mm9m1iAUIZHOehD2BdUbXR8eildIcmwCLzgVw_lSdJaSlGS6x95ysKcXKhkfIGDMPvz36w5jwPhlvKDNb9oL3nYRRqE7VjVSn4HPfzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bc2eaf0b.mp4?token=nQbSN4ynV2jJMif_0zVNr4uwFaaQniz2G21L6wfStxkZ-ow7Ak-leZIcA3EJVA88S65oOioO6h15fQWZvZlm2xlVKudS8TOd80kkYlCDMa4Xw1-W-84347dVAL1UQZ9HY51CS_o-FacSmIHu_518Diy44CmUmtTLPlhdu-84SassFst5pmc7xEYlVmTlU7kCp7wliJl6jpsdBEuVGVWNeICjl-s9E3-GTF50XkJaI0RxrQ5mm9m1iAUIZHOehD2BdUbXR8eildIcmwCLzgVw_lSdJaSlGS6x95ysKcXKhkfIGDMPvz36w5jwPhlvKDNb9oL3nYRRqE7VjVSn4HPfzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی صبح زود امروز به ناحیه النبطیه الفوقا در جنوب لبنان هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130279" target="_blank">📅 10:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130278">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وال استریت ژورنال مدعی شد:
حمله ایران به کشتی باری در سواحل عمان، آزمایش توافق ترامپ برای بازگشایی تنگه هرمز بوده است.
🔴
به گفته دو مقام ارشد آمریکایی، سپاه پاسداران انقلاب اسلامی ایران روز پنجشنبه در تنگه هرمز به یک کشتی باری با پرچم سنگاپور حمله کرد و توافق امضا شده هفته گذشته بین ایالات متحده و ایران برای پایان دادن به درگیری و بازگشایی این خط حیاتی کشتیرانی را آزمایش کرد.
🔴
این حمله تنها ساعتی پس از هشدار ایران به کشتی‌ها مبنی بر عدم استفاده از مسیرهای تأییدنشده از سوی این کشور انجام شد.پس از حمله به کشتی سنگاپوری که از مسیر تعیین شده از سوی عمان عبور می کرد، چهار نفتکش دیگر که در این مسیر حرکت می کردند، بازگشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/130278" target="_blank">📅 09:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130277">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-dbG15YwFHxAquzBTh81uUB3zbNE0qQ6l7zb551akNLYBzXaf2xjoGTiYklB7oe3rWJkjpqheVgGbZ2oa6jPjOBNbxcyITyq_8xrFWXMqGoI_xMN9QGCytjO0RaimcJT5elj8Jf2J3zMcW9ylcQ2xGDbDImVOh_cUeTIF_EbjMv1rIbT69biXOWwF1BeshjOysJ_Zj8yAfZosdlPIP9kxl7-aTFx4aDFfxPHBiau1SLx-9Hkarz4xFMrAy8vJdC19DRApGgopooqnt9-0nSnGGH6vJFGluDydtvSX8MAkosFM7QyoPKcaPRJp2pJgtr5EF-PqUrjHx_dMnJVvXoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز ۴ زمین لرزه مرز بین عراق و ایران رو لرزوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/130277" target="_blank">📅 09:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
بهای نفت برنت با کاهش ۱.۷۴ درصدی به ۷۴.۱۹ دلار و نفت خام وست‌تگزاس اینترمدیت (WTI) با افت ۱.۹۶ درصدی به ۷۰.۵۱ دلار در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/130276" target="_blank">📅 09:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130275">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR0mMZo9fP7ceMN6I1tr669nF3d48nb-h2p3eCmiG43-UiU0PinB_3JkVfqVsKzR-OMmFRl4OPDtevjlvyAbjfNApbNfh10fKdXyUvpri-TydXUL8_Hk7pVEZBTQi_WpyUygXJAqg-F6Osk44LwUnAiKGcd6DfD5Vh9Sh7o0yDfWRRBwNLgHI81g9Nqa5eXUGObkQm9jUZuwzJeG3vdQYJ4Znb2JU1IX1LznM8Kjkg3zT-j9_3TEaiT_HV3w0Kqr5O1UfN5d89IF11LNr-fnuOjbw1YoIweCz_LZ0KVxZ3emyLq--11zeen2s4Nr_uAga-AgNoN1ud0C7SqQ1YXPCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر امور خارجه آمریکا در امور شرق آسیا:واشنگتن، علیرغم اعتراضات چین، مرتبا کشتی‌های جنگی خود را به آب‌های مورد مناقشه در منطقه آسیا-اقیانوسیه می‌فرستد تا «از آزادی ناوبری دفاع کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/130275" target="_blank">📅 09:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130274">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نخستین پرواز دیروز پنج‌شنبه ۵ تیر از مبدأ تهران در ساعت ۸:۰۵ صبح در فرودگاه بین‌المللی کیش به زمین نشست و ورود گردشگران به جزیره به‌صورت رسمی آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130274" target="_blank">📅 09:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130273">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmBatqXPOm3txMEdFyMN6VD11IGxivqhEw5Vfo8znolAprJ1YrVb9vHA7FELy0Ypc28HuoxHnAy2ftPDCFauBF082FvXvpD9KxE-ob9f89sYfCBoXyhHoOZvkt9R1DPyFTOdyRmcJljy1dt75NwZkA1jsxsZlBdBAPi6inrKdZWbJ6z96a8XhqnYJQQWmMdb0Q0RqT6xEPen-P84EaGqFgcd5OAeCb8IFwb3whmyl4Q6OSb7atBEUPNagTOTLGz-38PB6t3yHixC1WtKM6AzrjWZwWUiQSQlktygXriYWyu1kpKVS9oTjBzsDpusvrDulj5qVJhsWcbbe-2suK8cfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله شدید اسرائیل به نبطیه/ در ساعات اخیر چندین حمله به جنوب لبنان ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130273" target="_blank">📅 09:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130272">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل: به هیچ وجه قصد خروج از لبنان را نداریم، حتی اگر ترامپ درخواست کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/130272" target="_blank">📅 09:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130271">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
افزایش کشته‌های زلزله ونزوئلا به ۲۳۵ نفر
🔴
سازمان زمین‌شناسی ایالات متحده:
فاجعه احتمالا گسترده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/130271" target="_blank">📅 09:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130270">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6157f55c.mp4?token=SBSqz7Yxx2IV46Lymo0HIHQI5UsOLuowZYj2b3jqhWWRjSdVOrDm2CWNbcZ0MDC-mAAnqFceMud2XgvwtDHbWrEgD6ozOkCkPi9c0_AxK6VY3T0pgo_aDCf3XE0N_8wxtyruTvr4NF4S7DSkzJFy9lP0nJQhu1CnkZrevcgPHKksJrXy8H52S4hftnIh6jRhJUECUkE3YBhOn9_xJIBxHI1ax4M65BppRecT0sjPzLHru5_BO58KV4bItX8Wl4csSQ4S5nbl2b81UgAy9IrjbT3TBoROG5hd5hG62ynGcWLQiS5n_0MbEBAGclVLXyvibHDPycOC3XjrOhYAZpfLZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6157f55c.mp4?token=SBSqz7Yxx2IV46Lymo0HIHQI5UsOLuowZYj2b3jqhWWRjSdVOrDm2CWNbcZ0MDC-mAAnqFceMud2XgvwtDHbWrEgD6ozOkCkPi9c0_AxK6VY3T0pgo_aDCf3XE0N_8wxtyruTvr4NF4S7DSkzJFy9lP0nJQhu1CnkZrevcgPHKksJrXy8H52S4hftnIh6jRhJUECUkE3YBhOn9_xJIBxHI1ax4M65BppRecT0sjPzLHru5_BO58KV4bItX8Wl4csSQ4S5nbl2b81UgAy9IrjbT3TBoROG5hd5hG62ynGcWLQiS5n_0MbEBAGclVLXyvibHDPycOC3XjrOhYAZpfLZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از زلزله ۷ ریشتری ژاپن، امروز صبح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/130270" target="_blank">📅 09:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130269">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
استیون میلر، معاون رئیس کارکنان کاخ سفید: ایالات متحده در مسیر بستن کامل پرونده پناهندگی قرار دارد و پذیرش تمامی اتباع خارجی را که به دنبال یافتن پناهگاهی در آمریکا هستند، به‌طور کامل متوقف می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/130269" target="_blank">📅 09:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130268">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bc8bdc23.mp4?token=DoVQDpacnpedqvjq8AySohfk4D8lCGLallGuT5mXUwWWVwpbPE9SjCqe7K4t4id7-SNmpP7pUlyIIoVqRf5IAFUwlVdGD1MigtzrQYdhAWQza-4d2cE4t5FAgpy3sgChn2G_0TXrMpZayTiHVnflBwxPIzqmFpsGtT7zPrgC0A1a5jxrVkbiheVEh3IdfhJ14C_Rh5QGU2mWJnLYr5IIY6l25xfdnwJt29nhKwrnNy5Yf8c_8fc7coStlwjk3O4oURz2HHrRv4SggkObCqBYoefNGBKOfYLzm0NIqBZPx0AOPlm9N_wEFe52Qmf2eqEonGcRyi_5hq9vnPEsCgegIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bc8bdc23.mp4?token=DoVQDpacnpedqvjq8AySohfk4D8lCGLallGuT5mXUwWWVwpbPE9SjCqe7K4t4id7-SNmpP7pUlyIIoVqRf5IAFUwlVdGD1MigtzrQYdhAWQza-4d2cE4t5FAgpy3sgChn2G_0TXrMpZayTiHVnflBwxPIzqmFpsGtT7zPrgC0A1a5jxrVkbiheVEh3IdfhJ14C_Rh5QGU2mWJnLYr5IIY6l25xfdnwJt29nhKwrnNy5Yf8c_8fc7coStlwjk3O4oURz2HHrRv4SggkObCqBYoefNGBKOfYLzm0NIqBZPx0AOPlm9N_wEFe52Qmf2eqEonGcRyi_5hq9vnPEsCgegIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ونزوئلا: ما ونزوئلا را در کمتر از یک روز تصرف کردیم و نفت در حال جریان است و ما با آن‌ها بسیار خوب کنار می‌آییم.
🔴
ما می‌خواهیم به آن‌ها کمک کنیم — آن‌ها دیشب زلزله‌ای عظیم داشتند که در مورد آن خواندید، مانند یک زلزله عظیم در کاراکاس. ما می‌خواهیم به آن‌ها کمک کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/130268" target="_blank">📅 09:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130267">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گروسی: معتقدیم که مواد هسته‌ای از زمان آخرین بازرسی که در سال ۲۰۲۵ انجام دادیم، منتقل نشده‌اند، اما لازم است این موضوع را به‌طور قطعی راستی‌آزمایی کنیم
🔴
جزئیات فعالیت‌های ما در ایران و ترکیب کمیته هماهنگی ویژه مربوط به روند بازرسی، در جریان مذاکرات مشخص خواهد شد
🔴
آماده‌ایم تا فعالیت‌های فنی خود را در ایران پیش ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/130267" target="_blank">📅 08:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130266">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: ایران کشور زیبای دوست داشتنی و بازار جدید برای آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/130266" target="_blank">📅 08:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130265">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHBFv4CYaj3kWSdUJek0K5klG1DEq7KztXxUtyNZkLybi3uOIQHXNiqsMX4AKTpCs5uBQoeiW8CgdrByGelyvLxTtHkm0hn9vN3jGOUoFmTHfFPeuTO1Sl2X0AhLNzjSaLA4XdHKOZa4tXramWu89NJmW-3-h1q6Tx_ad7vSOMO58i_FxbJk6aMGl2TX-R0Ayyy6wWNcKajwDnuntd-flQMRTHvnOv2s5vGCtoJ1_RpyJKuj2nj9Uv0Uyfb6I0Aek2o0Or3ZMrWTTTf2RUR1EHgwa2REzScYokyIcLmEJuL7P5fyhlzKCUKEu9hxhSDBVZIDZ5j_J2qgicux3vpW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا اعلام کرد
تماشاگران می‌توانند در دیدار تیم‌های ملی ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶ که روز جمعه پنجم تیرماه در سیاتل برگزار می‌شود، پرچم‌های رنگین‌کمان را به ورزشگاه وارد کنند.
به گزارش رویترز، این مسابقه هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود و کمیته محلی برگزاری جام جهانی در سیاتل آن را «بازی افتخار» (Pride Match) نام‌گذاری کرده است. ایران و مصر پس از قرعه‌کشی مسابقات با این عنوان مخالفت کرده بودند همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای تاکید کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه را دارند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود در دیدار ایران و مصر که از سوی کمیته محلی جام جهانی در سیاتل با عنوان «بازی افتخار» (Pride Match) معرفی شده است، از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی جلوگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/130265" target="_blank">📅 08:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130264">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24211a974.mp4?token=QWzIPbFaQEoyNBlPA6-JmM_wGWU2hdi-H_aSQYesPrF9GpcpXggSYjNv5fojY800KAfYyncTzfhhUzZ2CTjryafNQeQR4EBrXE77ldh8DLJjydF1BH7ipXEMAgTd8HZeQinZAFBEyD6tzYv5iH7MvrFrdgl4ntXtU5gZCUAVtivDrXsK0SUzj7tstaWAmEC6DI6HMFsUBXKLeIa5iuLjyKpcFlg3arCwqVEnLa3EsRWoDpBWBKp7-m_VDOJk5inukDsCfvVDU5SGbqVB4bYKAZFYie0esOwgVs6siAsiYeupjNqGpOzkCn0CffWQl3m0Hf_0D7aXLcG_bmKRTXEmuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24211a974.mp4?token=QWzIPbFaQEoyNBlPA6-JmM_wGWU2hdi-H_aSQYesPrF9GpcpXggSYjNv5fojY800KAfYyncTzfhhUzZ2CTjryafNQeQR4EBrXE77ldh8DLJjydF1BH7ipXEMAgTd8HZeQinZAFBEyD6tzYv5iH7MvrFrdgl4ntXtU5gZCUAVtivDrXsK0SUzj7tstaWAmEC6DI6HMFsUBXKLeIa5iuLjyKpcFlg3arCwqVEnLa3EsRWoDpBWBKp7-m_VDOJk5inukDsCfvVDU5SGbqVB4bYKAZFYie0esOwgVs6siAsiYeupjNqGpOzkCn0CffWQl3m0Hf_0D7aXLcG_bmKRTXEmuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رجزخوانی وحید جلیلی برای ترامپ
#گنده_گوز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130264" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130263">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: باید علیه ایران اقدام میکردیم چون داشتن سلاح هستهای به معنای نابودی اسرائیل و خاورمیانه و به خطر انداختن جهان است‌‌
🔴
اگر ایران سلاح هستهای داشت ، ظرف یک ساعت اول از آن استفاده میکرد و ما هرگز اجازه نخواهیم داد که این اتفاق بیفتد‌‌
🔴
ایران سلاح هسته ای نخواهد داشت و به آن موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/130263" target="_blank">📅 02:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130262">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: ایران خیلی می خواهد با ما توافق کند و فکر می کنم احتمالا با آنها توافق خواهیم کرد‌‌
🔴
ضربه بسیار سنگینی به ایران زدیم و اکنون از موضع قدرت مطلق با آنها مذاکره میکنیم‌‌
🔴
قیمت نفت به شدت و به طور قابل توجهی در حال کاهش است و کاهش قیمت نفت با کاهش قیمت تمام محصولات دیگر همراه است‌‌
🔴
تنگه هرمز باز است و دیروز شاهد خروج 19 میلیون بشکه نفت بود که بالاترین رقم در تاریخ آن است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/130262" target="_blank">📅 02:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130261">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: 159 کشتی ایرانی را کاملا غرق کردیم و همه در قعر دریا هستند‌‌
🔴
تنها در یک هفته و نیم ارتش ، فرماندهی ، هواپیما و نیروی دریایی ایران را 100 درصد نابود کردیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/130261" target="_blank">📅 02:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130260">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: روند خرید محصولات کشاورزی برای ایران خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
🔴
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/130260" target="_blank">📅 02:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566bfa2ebb.mp4?token=ttge2ya0-V-S1TNdBy2-yqlGzXV0xsG99vxvbJwM5Q4HVbyPkkFZ-ZaxGODcHhH6tA04N18ZaWhPeJhHT5GPSpC5bQ9NG_eE68mSFEvDyJ13q0yEEAHMlyiiRIW6hVHY4mkF1ziQRQT6gAy_Rh5yAuh2d3OLipLltOZmM1mUCqry3MRMPrWy-sB2udtHzgf9Joi7pZkNbq7ChHue2ydh0Pgh30OyekB6qY6KZZl9bMANV2TJta6WONyTJ-jBAp48XDHqpQ6Rro0-owHrPelcUPisqkEA4mjr9JE9d7TYVkGT5X-PrfYBA-ZW0bKo0jsUBMJe1K4jxDEFQ6MPlmPOtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566bfa2ebb.mp4?token=ttge2ya0-V-S1TNdBy2-yqlGzXV0xsG99vxvbJwM5Q4HVbyPkkFZ-ZaxGODcHhH6tA04N18ZaWhPeJhHT5GPSpC5bQ9NG_eE68mSFEvDyJ13q0yEEAHMlyiiRIW6hVHY4mkF1ziQRQT6gAy_Rh5yAuh2d3OLipLltOZmM1mUCqry3MRMPrWy-sB2udtHzgf9Joi7pZkNbq7ChHue2ydh0Pgh30OyekB6qY6KZZl9bMANV2TJta6WONyTJ-jBAp48XDHqpQ6Rro0-owHrPelcUPisqkEA4mjr9JE9d7TYVkGT5X-PrfYBA-ZW0bKo0jsUBMJe1K4jxDEFQ6MPlmPOtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف امشب با روسری در هیئت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/130259" target="_blank">📅 02:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
جی‌دی ونس در مورد جمهوری اسلامی ایران:
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/130258" target="_blank">📅 01:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130255">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g00boAXpizaf6QTHf3-yp64THi5_5u3m5wblTQC4ExOrgw8i18VeWVBeJURXQR3yOUl1CgvstziPBR0d8exhQehlva5pUmAj245wFrdlZWncwdzTeWw3sTfzXBAXshvRG-sGOkkuP-otpUZQWsZJdo6OamCw_wv786aqtJDWZMXs5JigBnmYrHswiY93DQpPpHL3lDWuWHkT1i9tEHsiE6mhlxhgXaZaR-Smll90fxEYgIFp4pW0Qe1SPSdTBT5RgdJ6DJbBnreThWbIpq-4YFYioQYqb-8fmMjGHOYuR2iGkGYROJPHYBy8LRzD3-DNHPlN5KBV7AZkyBmFiAhv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3r6zYvkOr2jM8IWyjkQS3OZvPba0B9wBVZIxHOXoQWVZk-S-ykEdiCZcmCNL2XBMnk2HhwmHgA3NHK0TDhonccP8xRxTajxQLUfQ4DnRny4vqzJuKcnmZglQvcskaWHd_eImgoQqa_A-wuoabQv2CWB5ad3YwerjMqRrAmr6_zUeb4uU8zbHOIRtNBSqG4AhhsYPg7YCAe64kZuqNFg-cbR_lWmDigu45yBiD89P3_pg8pSumX_oCPvzfeETF3WXpUOlZDspO9PTFkbOjx05FXtyWKYAVlAQGgMHd43u14NUCDJKSYtFyvAfuWUzKMZG6kie2QyQNBAnTDkWJOOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHaG1qsItFKVzOukhdSEGBQ76sL_kLL3KbrWqdvhdgBZP2O6DKNwNsDrarNYKyLA1dGIelITCyyuLQKgW8jTvK6HsJJWuVDYeFhU0uVFnwNzRVd-yoDwySIVGxQ4G7CJ5A6mDeVhn4TLjHxAOoU-0XJwOqiWPMlftXejZQlAdISiKTZ7bOPhLhS6JdC1FATAIpqvH6v1PI3pqyoCvRGZaGdgUkkDNnv_7V8iYdp1BeKm91EhYthDsoqwC62sDuhDxSD_guARdyTB24unzGNAOGFBdV0TAMqZyqQEF3iHXMCAa_icJOPZkfS8qMfnVEjqMAkAHWGR3dUT7t7cCfd56A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شهباز شریف هم نتونست مانع بیل زدن پایان ناپذیر پزشکیان برای کاشتن درخت تو اسلام آباد بشه
🔴
شهباز هی میگه نمادین هست ولش کن اما مسعود ول نمیکنه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/130255" target="_blank">📅 01:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130254">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e31799d4.mp4?token=L6yQMIUZExDPZeenNJ71xOUD4B44L1lnpIRu9zRPbdRM_zSDE5x3fyhwD56qPATbAmyL5tVloLEYZqjZmcKwUcxvZBY9zhKNVECn-hzA6kikxeEYjiAbJHewzHU6uVKyouoD9Lczv79Dm8fWCYju912vzE5vDqg9Pqteazr60GREVNLfcVmciA1Y6D45Fi0kbxnm3Bpnog0rdifw3yyc5KdoAiy7OG7a7R1p8N8EdZasN5np9XtSb-OybpW6cPhTtXO0V9ZuXC3GD7BCw1o9dVVQax7YV3RFzb1HNRjo1jVImvs5JTCyh0HgHvcMfdyKkFYIOorMx8wvLfckC5tYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e31799d4.mp4?token=L6yQMIUZExDPZeenNJ71xOUD4B44L1lnpIRu9zRPbdRM_zSDE5x3fyhwD56qPATbAmyL5tVloLEYZqjZmcKwUcxvZBY9zhKNVECn-hzA6kikxeEYjiAbJHewzHU6uVKyouoD9Lczv79Dm8fWCYju912vzE5vDqg9Pqteazr60GREVNLfcVmciA1Y6D45Fi0kbxnm3Bpnog0rdifw3yyc5KdoAiy7OG7a7R1p8N8EdZasN5np9XtSb-OybpW6cPhTtXO0V9ZuXC3GD7BCw1o9dVVQax7YV3RFzb1HNRjo1jVImvs5JTCyh0HgHvcMfdyKkFYIOorMx8wvLfckC5tYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یک مداح دوزاری دیگر به پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/130254" target="_blank">📅 00:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzAD0fV4Toe6pturDJUHrqbB5bp96HKNDuObN_zfWDuLinjPhtalNZNGE-2ekcv707Tx_SPNeM74aLjJUQnh_J7DovosWCc5W9-vudPzvPkwpZ6n6tyTn3YAusxas3a9gcNjBfgbxK6bUk_bQ_Hxd4x9tCph9o62GS-E9z6RFbf80hNf2Fa7RCwdekcpo6q2WvoI5Rv3EuTs3UcdTTiU2W6gTd04SadDVgd71QZ30kHaIBF7DL6VKjUfmFYyFIKXQvqM2HbxPCVF3CGhkDUZeO5FI8HV-z0NCtSx8x_7eiwU8gNPTgtwf2mCWsAdgjSV3j4GpRjtURUk3OW1ISrNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما برداشته یه آخوند که تنها رزرومه‌اش افتتاح شلتر(خونه صیغه یابی) هست رو هر شب میاره راجع به مذاکرات نظر کارشناسی بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/130253" target="_blank">📅 00:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130252">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b6026c629.mp4?token=h9dqGKm88-pLWPh5x5ULB811EYAcCa9J8rvKF49icoIWxNSf4gjvQA5lJVmJSvdW2TnVi4HWJAHzIbhsK_o_gJt59CymB74Puyy5NerrXlUezX5Hqm3deyqI0fdvyjs-L9hyOG_hAxpY9jYnhDRjrh_Z5GEplT81AkPlsxjmWkvunN5rJ9Bvz1ww-1Nvd7l6vPC7W1OCUf19V4n0ac7JWcw7sgNDdCwzX0Mpwox96JW-Fm0X1f7XBagPINzvbWpJ2Sqn6Th5eBfAAmXsh2F6DWx_ns03oD4KuWMGdyaGqEMi_XWCcKDdxGMc1Z7T07Zn_f7mOq_WjACd9pfvCz1ZGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b6026c629.mp4?token=h9dqGKm88-pLWPh5x5ULB811EYAcCa9J8rvKF49icoIWxNSf4gjvQA5lJVmJSvdW2TnVi4HWJAHzIbhsK_o_gJt59CymB74Puyy5NerrXlUezX5Hqm3deyqI0fdvyjs-L9hyOG_hAxpY9jYnhDRjrh_Z5GEplT81AkPlsxjmWkvunN5rJ9Bvz1ww-1Nvd7l6vPC7W1OCUf19V4n0ac7JWcw7sgNDdCwzX0Mpwox96JW-Fm0X1f7XBagPINzvbWpJ2Sqn6Th5eBfAAmXsh2F6DWx_ns03oD4KuWMGdyaGqEMi_XWCcKDdxGMc1Z7T07Zn_f7mOq_WjACd9pfvCz1ZGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از رهگیری موشک‌های بالستیک اسکندر روسی بر فراز کیف توسط موشک‌های پاتریوت در جریان حمله دیروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/130252" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130251">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c21bf1806.mp4?token=lq-_VyXrRHPr0P5BhjYMH0L4KtQ9N1yiaBoprwD_6lDmy0oTCjsxfl5eWGd4rNxjCFNC-effclpfrrLFmYOpjCFoJ75ZwdfCjxCcEPQQ6ETqv5vXw0PDgYgXjepoHp94DM4wW7gzP8QIxJwpMT89zwVBz8BoCFi8SPIXUEgXmP1c-_-a3tDWnn9FoigKH0Nx0IX2KjOQ2V66v_krH2ZRThZba81I7KAfj5BcxZZlQW0n264vP9hCHP9EKhUy5pjPFZRcyu4_ctCbB1zkMMyIUwxlK9xR1YGJghRJJExVlARaGtp1_pGRivuHP-jDjJS-Hm1HllgF3A_g6FfQunMB5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c21bf1806.mp4?token=lq-_VyXrRHPr0P5BhjYMH0L4KtQ9N1yiaBoprwD_6lDmy0oTCjsxfl5eWGd4rNxjCFNC-effclpfrrLFmYOpjCFoJ75ZwdfCjxCcEPQQ6ETqv5vXw0PDgYgXjepoHp94DM4wW7gzP8QIxJwpMT89zwVBz8BoCFi8SPIXUEgXmP1c-_-a3tDWnn9FoigKH0Nx0IX2KjOQ2V66v_krH2ZRThZba81I7KAfj5BcxZZlQW0n264vP9hCHP9EKhUy5pjPFZRcyu4_ctCbB1zkMMyIUwxlK9xR1YGJghRJJExVlARaGtp1_pGRivuHP-jDjJS-Hm1HllgF3A_g6FfQunMB5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحید اشتری: واقعیت اینه شکست خوردیم و تسلیم شدیم و توان انتقام نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/130251" target="_blank">📅 00:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130249">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaKz_5QCRoEe63XLR7VeECLxcBQWgKVbgdEu9AlYe5-3u7k1Bd5_NpfDvyXJArpWQEHC8rxKjLlmdTQhlrTDH65jPVJlvnvv5v3mfwQcS5CuAwHQ2ZrTYO-nc5_WeSQnwSEeUF0DSkdP712yrNa99bbopwWpYTBcz-hGCHBsuAAkR5ElQ47kljlpmgCc5t_OjK6vTnwjUWbWEOhkMmVvOpePs15RHYTFWDDv7yeir0O87Cm6s-cZpws3VH-WVPlXx7LFIgOYQa-advy5-TlD2zgsH8_D7yE_yIwTNHJKzvWiIYx5oDc_hQuOrgS17e2jncjAbBYUV6lj3nN7_NZn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOW0TtLIg67JFw-z_cb3TeXbtvMUTl3g-uDsCiKtUIg-DnCJCqK98u2ZM8TxeX__z0-GOIFGAMvkQR_brv9bFxChn8rBxHehmyC4FspXkDAf-FMNxJB5lvCeOnEdfCzEhMWYZjlea-1trx3ZDZOCi7C7gQX5xRZtc8tsf0af1lKstX2ToAfEB28CsgP3J14h0AJ1W8Rn6Ou5ZzEYnEZNGmLWYgAyAJT82JqVlnLr8CkbSjPny2abWb7ztXu2iHIs66S0SAQvDAE0oIFFRJneHGVo8eW6NtoKnhsh_4TNkkRlEAn56mhjwLjvkiGaiE3uUUU5r3Di-5KcwF-M_orktA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
محاکمه شیخ "احمد بدرالدین حسون" روحانی و مفتی سوریه در زمان دولت بشار اسد در دمشق شروع شد. او متهم به حمایت و توجیه سرکوب مخالفان بشار اسد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/130249" target="_blank">📅 23:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130248">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
شبکه المنار گزارش داد که توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/130248" target="_blank">📅 23:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130246">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOJ_dz2CJgZfHzo_tNbddJMFFGaxa8sCl1pElBgf23MKoaDebtEbD_p5Ci5yCSfmSer1AGu4ey-ebYl6A57hvsGRBenIV2NMmW1IDDAboiFjXRLQrjb6yEpB7xpiuYjf6HzO-g4pNRVbxv2eEPX-OR2X831VWGnxXIBGDLu3tKi926VaJ_vDPfHT4W4pupedS-9BzouvXGHSc68CslfKmxv8OMZX1xQVhCKKxVkG_2oo36BVxTAQ-rovsswKD7kazsb7S9HBS5yh56w-v38YSOcsi4Ue0Gq7U3ypFy6IBFV0EmtYouKZInFVzW30jQWQQtzuY1ZSrDEC7z05nLjGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
آقای جدید گفت برید مذاکره کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/130246" target="_blank">📅 23:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130245">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ارتش اسرائیل: ۶ عضو حزب‌الله رو در جنوب لبنان ترور کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/130245" target="_blank">📅 23:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0081f0c6.mp4?token=oM_wsuugI_roOZJvrdCmOBkhtgL0JaEVqHQBv5ZqBMJjUYa8bgqidUlTYJ9LvmIncho9l-5RlSRIExGTIdkUhVEJFTyv9JdQlphdfNopOuwsibr2puSoK2Eb64rNJEkcLWX1w1nmPydRHW4B3uNyl9_v97jsqgk1mO_TXPjmYC4kvy8YXcuCf5g1wypKQ61gTHOlGDM4eM6Hr0jOHz9YrmBkzVWvcHvZ59FMuXtGXovvh-6HqQ05lKpFVzaRJdsvYXuM6UO6dfnA5xbb7htsmjP0aTIoj703gBpwVcpAQ28Oi1jFgxkzP5KDDRveV2aWO4hxepD0fMk__LEcNGo82Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0081f0c6.mp4?token=oM_wsuugI_roOZJvrdCmOBkhtgL0JaEVqHQBv5ZqBMJjUYa8bgqidUlTYJ9LvmIncho9l-5RlSRIExGTIdkUhVEJFTyv9JdQlphdfNopOuwsibr2puSoK2Eb64rNJEkcLWX1w1nmPydRHW4B3uNyl9_v97jsqgk1mO_TXPjmYC4kvy8YXcuCf5g1wypKQ61gTHOlGDM4eM6Hr0jOHz9YrmBkzVWvcHvZ59FMuXtGXovvh-6HqQ05lKpFVzaRJdsvYXuM6UO6dfnA5xbb7htsmjP0aTIoj703gBpwVcpAQ28Oi1jFgxkzP5KDDRveV2aWO4hxepD0fMk__LEcNGo82Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته از ناتو: این بهار، با مهندسان جوان و بااستعداد در شرکت ASELSAN، بزرگ‌ترین شرکت الکترونیک دفاعی ترکیه صحبت کردم.
🔴
آن‌ها انقلاب صنعتی دفاعی ترکیه را هدایت می‌کنند که به نفع هر عضو اتحاد ما خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/130244" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49014d9e0b.mp4?token=kfXO9rZU1c6tdn2nHSKJac_bVCnkdtgsDznWaigaaiC5oSpgFeHWtE2Lfz-qKpgFGZa2E6AQYzzFV4OPf9U4OrLl4NGufQu6RLbVQjRtlvB0IkgfCsHVRCdSRctr5rgka-YAAVYvnTa3_4R1jNaX6EPCpwnEOrUDsE4k882ZuJRcxXBUbcgpFOW_JmqvRD4rH153dTzY-Gz8wJkxny8hR3o3HaW9OmoEJfNlmuMfc5k5H1LSprA8jFGtGUAhn_CLsTMfYKKtSXtrRtd9BER8AOdzT7d3GUF4W57Oidp4FV99BVseg4FTpsagt92Eks77izHrV3xT5Stffu52MEPz4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49014d9e0b.mp4?token=kfXO9rZU1c6tdn2nHSKJac_bVCnkdtgsDznWaigaaiC5oSpgFeHWtE2Lfz-qKpgFGZa2E6AQYzzFV4OPf9U4OrLl4NGufQu6RLbVQjRtlvB0IkgfCsHVRCdSRctr5rgka-YAAVYvnTa3_4R1jNaX6EPCpwnEOrUDsE4k882ZuJRcxXBUbcgpFOW_JmqvRD4rH153dTzY-Gz8wJkxny8hR3o3HaW9OmoEJfNlmuMfc5k5H1LSprA8jFGtGUAhn_CLsTMfYKKtSXtrRtd9BER8AOdzT7d3GUF4W57Oidp4FV99BVseg4FTpsagt92Eks77izHrV3xT5Stffu52MEPz4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هزینه تجربه کردن GTA VI در ایران، در اقتصادی ترین حالت ممکن: پلی استیشن 5 اسلیم 1 ترا - 112.000 میلیون تومان
🔴
تلویزیون سام 32 اینچ - 26.300 میلیون تومان
🔴
اکانت آلتیمیت GTAVI ظرفیت سوم - 5.500 میلیون تومان
🔴
جمعا 143.800 میلیون تومان
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/130243" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130242">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRIiuxT1uA1Zu8PetsI5rxUGLM7TyLDe7nbu0nvkvJi17dKyLkIBkr8WWL78IJGu245jEMQ_h8PelL5uMZLEnSqrLhBA7oxJiQ1uH5bh52h_UzyXMxPqJkS2rdbfskcp1ENZaCZ98xMCEpXZEmPZfr4y-fIZvexPV7f_-u0WxF_BMdfCDfWID2KjJJmUyUyZdhhq_VlwTC4Rgq6T5BlpPY5eleDzRQIpuuBs9drSJ4SKV9icRUGpC8GL9aXZe0MBEqkgWt2F4URBkxTNdmfwvWzXu962afIawEpvNZhd5_x6X2i9PsJxKd3ppZ06EEJheGUA3D9ynejPcM_fz0lSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/130242" target="_blank">📅 23:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130241">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brxPl0bkKSDjgIwEuKX3vf6ZE-LhAgIuhHix97dKBJIg5ufhRN5nxeSNn2lFOFL6dL_pRlMitQ1swmbnLUwSgJtBkKX3twK0AcoMYK0FIrXX4XlPYqeCZ3Pl6qqryhp119MHkMwd0XJA7-QYN4ajfdKCN34qxDZldj_a4_vmpXMqMFPulWqY6tzNaxb2V1-vKI4Y0rLnQUvcN-0SNmjDhl19ncqmVeqYk3TCQNjffgY2kNe1n2sLyEBbhHT2mDUvKAkgJXFt_o0oRzsgrMZRBJadashKek723L0BSGOwCoC0Jqt7cuHfBznrIudamVLSwGx1LMdqgw2qoKJ3eI9Row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو سالی که برای پزشکیان یک عمر گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/130241" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130240">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092b312727.mp4?token=LjSX0SxFR-oT17Ns5LYELCaJS_uKPnmWOerKIE8CO8hZ6hsiStaJiMpGqLiW5eYigEI26xkZs0mk0OcKTi8VQ2uXk8vPjvt4Z01cczMyNcFRPXrXN3Dc1kAe7ptQ9IwI4V3tg-B8yempMluOo7KOS1XJ-OxtlU6OxQmB52549MFd0lSswHrjku28sERuJtJiITlUk9hvOSairDYa_KEUTLusZ84ttoCNq5tbZL6dxrT-8rOr_YtNcRKvv_OCjDzPyoIvqmol8TnsxO3fmlnxNQz3z60gM1ZQyBdlCRfKlN1UoN8VwPbI9HAQ-wC0XGeU_V6_4duxUqVY1MlsmBMEHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092b312727.mp4?token=LjSX0SxFR-oT17Ns5LYELCaJS_uKPnmWOerKIE8CO8hZ6hsiStaJiMpGqLiW5eYigEI26xkZs0mk0OcKTi8VQ2uXk8vPjvt4Z01cczMyNcFRPXrXN3Dc1kAe7ptQ9IwI4V3tg-B8yempMluOo7KOS1XJ-OxtlU6OxQmB52549MFd0lSswHrjku28sERuJtJiITlUk9hvOSairDYa_KEUTLusZ84ttoCNq5tbZL6dxrT-8rOr_YtNcRKvv_OCjDzPyoIvqmol8TnsxO3fmlnxNQz3z60gM1ZQyBdlCRfKlN1UoN8VwPbI9HAQ-wC0XGeU_V6_4duxUqVY1MlsmBMEHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف در سفر خارجی با هیئت مذاکره‌کننده بدون نقاب حاضر شد اما شب عاشورا در هیئت «ریحانه نبی» با نقاب حضور یافت.
🤔
کجا احساس امنیت دارد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/130240" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
چین رسما اینترنت 10G رو راه‌اندازی کرده؛ فناوری جدیدی که سرعت دانلود و آپلود رو چندین برابر می‌کنه و می‌تونه یه فیلم کامل با کیفیت بالا رو تو چند ثانیه دانلود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/130239" target="_blank">📅 23:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130238">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
عراق پس از بحران مالی شدید مرتبط با اختلالات صادرات در تنگه هرمز، هشدار داده که اگر گروه صادرکنندگان نفت سهمیه تولید خود را به طور قابل توجهی افزایش ندهند، ممکن است اوپک را ترک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/130238" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130237">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/130237" target="_blank">📅 22:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltMvHMuZL1_wk2iA3P9z73Ldaaq_0nW0kOf9xpS3zUhqUW_i_7p9PdQn7uTJvd-MZj8KuuHv-51M7CU2ltU7SRTQt14YnvfmcGMnHp4tvy2fqt1nwBCT5ksQU2RIPL1-6WMjk2KuTmkQATryg68y6WbIjVS7tAoYmLRnLFxOHrDlMmdZfIO1SILOZBfcOg8VH5Nw4nDbYUknefrmDmNhSNQVe47Ix32dLAgkOsgTiooDIjea123IR3Db1LL4Y4O2FbRy2boEOR77jds5VLDWusOKfjfyP1p10ceU5FjT7xt9x8BhTwwsm2J9b_mblHfsy1pGJR50SgnOcP6Dbb5MXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/130236" target="_blank">📅 22:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taQv4HLP3a3YjLZVbNnyUbTQ9TlUyIFF1O1j_zXq5wwFdD292244H_HNHR_sK_Aj9DgtvV4uUT7FCFZ1siGU6GiE6V1hD-fQUgSkWHAPVjEhPFshQJ8lIumpgWaj_jQUSHG88JutHhaOlM7yb980UXfJS3iik8SPfl_SVWhRwlvqcXKiOzogf46S1J6cgNidC_iUYPfP4d8XbvhYqE3Wzwvh-iKiZlIvx_03ZxnOcjoYBwfl31cbpqnutzvewhp9roCJs47cVweHO-UaaHqiNR2r3xlFD3B_q68ove1Q-V0JEbXP68sSh0GapleIWj6WOJDqndIw7BrNzl_uIcDdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت تنگه هرمز: تبعات عبور از مسیرهای غیرمجاز با خودتان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130235" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ملونی در مورد ایران: ایتالیا در درگیری با ایران شرکت نکرد.
🔴
در واقع، اگر در درگیری با ایران شرکت کرده بودیم، توضیح دادن ناامیدی مکرر ابراز شده توسط رئیس‌جمهور آمریکا دشوار بود.
🔴
ما با در اختیار گذاشتن پایگاه‌های خود تنها برای فعالیت‌های لجستیکی و فنی و نه برای عملیات‌های رزمی، به تعهدات خود احترام گذاشتیم.
🔴
و زمانی که درخواست‌هایی مطرح شد که فراتر از آن چارچوب بود—و شما این را می‌دانید زیرا به طور گسترده‌ای گزارش شده است—ما مجوز استفاده از تأسیسات خود را صادر نکردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/130234" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ماریا زاخارووا سخنگوی وزارت خارجه روسیه پنجشنبه گفت، هنگامی که آمریکا و ایران به توافق نهایی برسند، مسکو آمادگی دارد که در توافق بر سر پیش‌نویش قطعنامه شورای امنیت سازمان ملل مشارکت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/130233" target="_blank">📅 22:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروی هوایی یک عامل حزب‌الله را که تهدیدی برای نیروهای ما در ارتفاعات علی طاهر در جنوب لبنان بود، از بین برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/130232" target="_blank">📅 22:14 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
