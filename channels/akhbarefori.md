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
<img src="https://cdn4.telesco.pe/file/aGa7Uuia01jEtuYV7xOPdB6eiKQG4hZUonMIbsCV6dRXUKGSxpTaezX8-Xop-JP-X6khihyd1mOmivul6FHBI-B1hJFcd95wgbWg1e1pQezBRvJIq5Qsm9tM3U178-tWc8lob7juy3qnvacn0psVOF8-vZ47ujyJ97kqFRYN_Qx1uCd9aeSfw3fHdTP_xY4RrIV6W0yhoXZAwq8Fq0ua11eSrFrYvG39gAtrnk-Ef-8sebNyv_ptckRLtDEPe30GISO9HGs_BsCdiep00hfh8TY2sK3KQ6d1zLYqc-6xlA6_LDBBmJzhayoHsR1LQByqDJ0Uu-dDaAXhLdlc6i7UVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 02:24:45</div>
<hr>

<div class="tg-post" id="msg-674674">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وال استریت ژورنال: اسرائیل از سرعت بالای بازسازی در ایران غافلگیر شده است
روزنامه وال استریت ژورنال:
🔹
ایران بنا بر گفته مقام‌های اسرائیلی و غربی و همچنین بررسی تصاویر ماهواره‌ای، در مدت کوتاهی توانسته است زیرساخت‌هایی را که طی ماه‌های اخیر در جریان کارزار بمباران آمریکا و اسرائیل آسیب دیده بودند، بازسازی کند؛ از پایگاه‌های موشکی مستقر در اعماق کوه‌ها گرفته تا پل‌ها، بنادر و تأسیسات تولیدی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/674674" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674673">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
عراقچی: توافق بر رهبری تحمیل نشد
🔹
هرجا رهبری اصرار داشتند؛ ما پذیرفتیم و هرجا رهبری بعد از توضیحات ما، متن را اصلاح کردند، ما مسیر جدید را جایگزین کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/674673" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674672">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
المیادین از حمله مقاومت عراق به مقر نیروی زمینی کویت خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/674672" target="_blank">📅 02:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674671">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
عراقچی: توافق با آمریکا بهترین توافق ممکن بود
🔹
اما وفاق ملی درباره آن شکل نگرفت
🔹
مردم کف میدان را با دروغ ناامید کردند و گاهی فکر می‌کنم اسرائیل در چنین روندی نفوذ دارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/674671" target="_blank">📅 02:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674670">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
عراقچی: دولت رئیسی توافق کرد که با ۶ میلیارد دلار تنها کالای بشردوستانه خریداری کند
🔹
سال‌هاست که برخی کالاهای اساسی را از شرکت‌های آمریکایی می‌خریم و جدید نیست.
🔹
صدا و سیما هیچ کدام از مصاحبه‌های مهم من را پخش نکرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/674670" target="_blank">📅 02:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674669">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5526e06d52.mp4?token=LlPcwi0NkWCUfZ_l0vB3IEgBJ1e6OrojynjA001kgOmOd4CgUoDFJ0fnlcwvaQ3Q2AMMT-vO93z6sRCYrhk23RxettBF0EtAFU6IeQWnz9p8avMTnpuXVrzWQvNHyXJSOg73aG8cYsbseGsxCsGvxDNU6lT-dELY1pEciYVRZ_BmGRckNeB6-myVkr20wK_2USm4Hjhnt-XpWTf9tJOMU-Rxqk3YIOzLYulx9y8IS2NJYZV6hUCGZGzEhbjpCuudRXlN-sAamstO2Q60PQj1HwOxCiceTf4QBM4q9cLF5ou9SkjxHJ18QJsVXhcbQ1EdIyQKjJRjEhWx-sGI5RV7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5526e06d52.mp4?token=LlPcwi0NkWCUfZ_l0vB3IEgBJ1e6OrojynjA001kgOmOd4CgUoDFJ0fnlcwvaQ3Q2AMMT-vO93z6sRCYrhk23RxettBF0EtAFU6IeQWnz9p8avMTnpuXVrzWQvNHyXJSOg73aG8cYsbseGsxCsGvxDNU6lT-dELY1pEciYVRZ_BmGRckNeB6-myVkr20wK_2USm4Hjhnt-XpWTf9tJOMU-Rxqk3YIOzLYulx9y8IS2NJYZV6hUCGZGzEhbjpCuudRXlN-sAamstO2Q60PQj1HwOxCiceTf4QBM4q9cLF5ou9SkjxHJ18QJsVXhcbQ1EdIyQKjJRjEhWx-sGI5RV7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تردد روان زائرین امام حسین(ع) از مرز مهران
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/674669" target="_blank">📅 02:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674668">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
رسانه‌های عربی: در تصاویر به‌نظر می‌رسد یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، درحال سقوط است @AkhbareFori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/674668" target="_blank">📅 02:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674667">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
المیادین از حمله مقاومت عراق به مقر نیروی زمینی کویت خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/674667" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674666">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=P7_rrIg6Lkp9V4c2K3SLom-UdVaZILctkugW3ix_aVZOQMPUQNsItThkJFOiOi6ySAcv9WeoUbc26vGvUXoGTqvMV2QAmwSngUEf3-B7Uw5jBPZG0IzjWcybLdLLSLvVaXc2LWkq3fp9sugBFz6GvsqhPdIST-Ud8GJZuA_62hDJjuS35jgjI_tKECi92nGGqsi8sElEpFD4pdhdAg0pvyqa7g_rrye4FY3EhNw1y9Nx1bJXpVBxa9GB4K3Nvba-VCGxJIqSTeGFyK46xWsiaS0bxZniAG5fUgGOUgisbjEPHMApNQbAxawACTZJ_fvapdRHqZhqbB3KentH8iuEwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=P7_rrIg6Lkp9V4c2K3SLom-UdVaZILctkugW3ix_aVZOQMPUQNsItThkJFOiOi6ySAcv9WeoUbc26vGvUXoGTqvMV2QAmwSngUEf3-B7Uw5jBPZG0IzjWcybLdLLSLvVaXc2LWkq3fp9sugBFz6GvsqhPdIST-Ud8GJZuA_62hDJjuS35jgjI_tKECi92nGGqsi8sElEpFD4pdhdAg0pvyqa7g_rrye4FY3EhNw1y9Nx1bJXpVBxa9GB4K3Nvba-VCGxJIqSTeGFyK46xWsiaS0bxZniAG5fUgGOUgisbjEPHMApNQbAxawACTZJ_fvapdRHqZhqbB3KentH8iuEwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: در تصاویر به‌نظر می‌رسد یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، درحال سقوط است
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/674666" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674665">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkYquZy4w38TIjfZywm5VWJnOWEl5NtE3SKRS9gy_cwB_6qhU0yuIdBjSO0d8P2ly_x3pNeJz5mIPIuLH5dEDdKtgOWMpadZybvmGSAKdquUEKXDiGO5Pu9Ph0F58HwiiyqnwKoRFzU__yknuI-fk3AdHiH-xkRRE_yUd1Lrr5PabhY0060m_QNH6TSeha8WI2srY8cST1twH_dFkunYH0Jdrl17y3sK2hUfBdt6zCqScrqye0aYuiMGG79VPW53MKSUXAx0AgqBfxhnCSg2bdYambTO0mwwjBx8JNyx7x1FAOVtvAll0yPKpyEnoYFO7KPkBmW89wHU6S7GezIRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک زرد:  تا اطلاع ثانوی، از این پس، هر گونه خسارت وارده به کشتی‌ها، محموله‌ها، یا هر آنچه که مرتبط با آنهاست، از پول‌های ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد/ این خسارات ممکن است بسیار قابل‌توجه باشند، اما با این حال، این کار منصفانه و عادلانه است
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/674665" target="_blank">📅 01:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674664">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
نگرانی اسرائیل از سرعت ایران در بازسازی زیرساخت‌های آسیب‌دیده
وال‌استریت‌ژورنال:
🔹
سرعت چشمگیر ایران در ترمیم سریع پایگاه‌های موشکی، پل‌ها و مراکز تولیدی آسیب‌دیده از حملات آمریکا و اسرائیل، مقامات صهیونیست را غافلگیر کرده است.
🔹
این بازسازی‌های سریع که در تصاویر ماهواره‌ای مشهود است، ادعای سران آمریکا و اسرائیل درباره «وارد کردن ضربات ویرانگر» به توان زیرساختی ایران را به چالش کشیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/674664" target="_blank">📅 01:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674663">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75012b9b40.mp4?token=TyMF66aeMZYBq2C3SPGK6jE62QtfyEERvnEI62mN4x5fxoScihW4629HIOB8ERqpO3xXsvGyBxetPAYL56hPA4MjlLSMf2yJFZHu9Rf9AUjqVR2C85DNE2VIMDSH34a70Yped1FCIVTJi9IqYv-FTPvsuXzudBU_rsvdbo9lV8r_pqhI6nO5znwaQ_MkO90UDN4B9VELvbS-WCwKAgYjU1wmHFGXC1Q6hjbmGVoxrjivWpOPc7nTA6pkWUJYgXe8BGW3nQRDx5d2n3ggMQtX5uvGet-xxRfS2eeI-BlXYq3x8P9gLdQgfAb7WntCP7dQvMNC0YAwFZ9sCjRFMFur6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75012b9b40.mp4?token=TyMF66aeMZYBq2C3SPGK6jE62QtfyEERvnEI62mN4x5fxoScihW4629HIOB8ERqpO3xXsvGyBxetPAYL56hPA4MjlLSMf2yJFZHu9Rf9AUjqVR2C85DNE2VIMDSH34a70Yped1FCIVTJi9IqYv-FTPvsuXzudBU_rsvdbo9lV8r_pqhI6nO5znwaQ_MkO90UDN4B9VELvbS-WCwKAgYjU1wmHFGXC1Q6hjbmGVoxrjivWpOPc7nTA6pkWUJYgXe8BGW3nQRDx5d2n3ggMQtX5uvGet-xxRfS2eeI-BlXYq3x8P9gLdQgfAb7WntCP7dQvMNC0YAwFZ9sCjRFMFur6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اى كسانى كه ايمان آورده‏ايد، اگر خدا را يارى كنيد، شما را يارى مى‏كند و پاهايتان را استوار مى‏كند».</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/674663" target="_blank">📅 01:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674662">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله به مقر فرماندهی نیروی زمینی کویت
المیادین:
🔹
گروه‌های مقاومت در واکنش به حمله به گذرگاه شلمچه، به ساختمان فرماندهی نیروی زمینی کویت حمله کردند که منجر به خسارات سنگین شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/674662" target="_blank">📅 01:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674661">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تحریم‌های ایران به لایحه تحریم‌های روسیه افزوده می‌شود
جان تون، رهبر اکثریت سنا:
🔹
در پی درخواست دونالد ترامپ، توافق بر سر افزودن بندهای تحریمی ایران به لایحه دوجانبه تحریم‌های روسیه در سنا نزدیک است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/674661" target="_blank">📅 01:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674660">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c423ce9cbd.mp4?token=QzGKMXbiSvrXIJum_OWsA7loNJXUmGNIHS9A73Iutc3aFIHqEy26i3OCKAdgyzmopIjGuRlH89ES7QTe9DODGWVoVD-Wf_sFtpkODiAE3QmcRxbFsMNqoVF4lMvvH6kvjk7c9Iwir_FoX_sKPJIYlJIqDrXzDtug4l0ghNHyu3V2dmogm_QJ3hszqDxLInJact8h_7JIXTW1FNM2XjsyNGfgKAw90H6NgUfi0h9px6lLqPJRYcadHCQ0wjcPnci9yMjF0OWRULOou0C7mlKDxdYTdB2HJ7yYgEZeNxQIjkC39tkSnSZDgzIjdHmmVWMCryrIo0k-vgw9oM5chtvk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c423ce9cbd.mp4?token=QzGKMXbiSvrXIJum_OWsA7loNJXUmGNIHS9A73Iutc3aFIHqEy26i3OCKAdgyzmopIjGuRlH89ES7QTe9DODGWVoVD-Wf_sFtpkODiAE3QmcRxbFsMNqoVF4lMvvH6kvjk7c9Iwir_FoX_sKPJIYlJIqDrXzDtug4l0ghNHyu3V2dmogm_QJ3hszqDxLInJact8h_7JIXTW1FNM2XjsyNGfgKAw90H6NgUfi0h9px6lLqPJRYcadHCQ0wjcPnci9yMjF0OWRULOou0C7mlKDxdYTdB2HJ7yYgEZeNxQIjkC39tkSnSZDgzIjdHmmVWMCryrIo0k-vgw9oM5chtvk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ‌زرد: نفت ونزوئلا حق مسلم ماست
🔹
ما به لطف ونزوئلا پول زیادی به‌دست می‌آوریم. حق مسلم ماست که این را داشته باشیم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/674660" target="_blank">📅 01:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674659">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار ها در کویت به قدری زیاد است که در قسمت های مرز کویت و عراق هم شنیده می شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/674659" target="_blank">📅 01:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674658">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عبور موشک‌های ایرانی از پدافند آمریکا در اردن
نیویورک‌پست:
🔹
در حمله‌ای که در روز چهارشنبه اتفاق افتاده موشک‌های ایرانی با عبور از پدافند آمریکا، به انبار تسلیحاتی در نزدیکی همان پایگاهی که سه نظامی آمریکایی در آن کشته شده بودند اصابت کرد.
🔹
این حمله پس از ایجاد انفجار، باعث شکل‌گیری یک «ابر قارچی‌شکل» شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/674658" target="_blank">📅 01:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674657">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQF0ckhRDWLJ4mEIJbyG0JwddLI4-arw3SRSIzRn6sL_B3KqqAbLjjK0VoNbermbaXAgjPwjJMqxlfJ-UtP_HaqrUcyqzSBX0_lGpWJsLstj8zO-qzwpJ60pCdgfoGtVo8IhWqYfW9YNnm61-xLBKQjM4N4c7FaMYziW6xqvW1ttlh7ZGFUdLmMnl_Z2V0gBPR_09ZOD96IgoUTnbDlkbxB6H3yieYAX-IU2eFIp5pNanGdlmYoihZrIGJJB9RSb4Dkux1OV2fBzwGxEE8CQ4ztFeZAECEp9JmGoWycrZJtgk2APRu7o5p9FjCxVlWLmGe1YASVMREYe-l8pVdjDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام موشک آمریکایی در آسمان کهنوج کرمان
فرماندۀ سپاه کهنوج:
🔹
یک فروند موشک تاواهاک آمریکایی در آسمان این شهرستان رهگیری و منهدم شد.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/674657" target="_blank">📅 00:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار ها در کویت به قدری زیاد است که در قسمت های مرز کویت و عراق هم شنیده می شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/674656" target="_blank">📅 00:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
انتقال ۱۲ نظامی مجروح آمریکایی به آلمان
🔹
نیویورک‌تایمز از انتقال ۱۲ مجروح حملات اخیر به آلمان خبر داد؛
این خبرگزاری مدعی شد که مجموع مجروحان از ابتدای ژوئیه به ۱۰۰ تن (۵۰ مورد در اردن) رسیده که اکثر آنان بهبود یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/674655" target="_blank">📅 00:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674654">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اقدام معنادار قالیباف در ديدار با الزیدی
🔹
ادای احترام نخست وزیر عراق به رهبر شهیدانقلاب و شهیدان سلیمانی و ابومهدی مهندس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/674654" target="_blank">📅 00:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عضو انصارالله: عربستان برای رهایی از تبعات محاصره یمن باید غرامت بدهد.
🔹
۱۰ سرباز آمریکایی مجروح از حملات ایران به آلمان منتقل شدند/ پنتاگون جراحات را خفیف گفته بود.
🔹
دادگستری اصفهان شایعه اجرای حکم اعدام ۲ متهم را تکذیب کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/674653" target="_blank">📅 00:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
منوچهر متکی، نماینده مجلس: نامه‌های احضاریه ترامپ و نتانیاهو به کاخ سفید رفته است
🔹
آنجا امضا گرفته و از طریق کانال بین‌المللی به قوه قضاییه برگشته است.
🔹
اگر در دادگاه حاضر نشوند؛ حکم غیابی قصاص برای ترامپ صادر خواهد شد؛ صدور حکم، تنظیمات آنها را به هم خواهد زد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674652" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMe1E8rkdMIKyzmO4ejC6WfY0GiYn6Vq8lzmJlYvpfXup0qdlk5S6owXvOCE2miuxLQrgaq7r2ayYJPFyufE6V2uqLOoUkoV2VhLH6hMB35D5StQOV72QrRweeUKFSOanJUdUEEzMwjeHZ3Q7miR26RtruhrRoSOOO8mX0w1tSIq38Q9VglJZBjccExkLEtYSNjRjx5TWBin4wQEMrb-Uox0xvap59HWoqNaFV_UkU-0r3sXJp62haU3TUC22pxedOLywfEKCQdfaaspnsana01XKxlrRvYwPrXXbqFS_4Z5Itwu5SgocgtJFn6VISJuH-8YAK-6JjHxBa8Umc2Z5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJhHtWMG-UhLcfAtdELzR0dPzg5jM0NufD0ZJduQjvhJ7ahsVR5nnlQ1DRO9-hfEgvAAGtswzNebOZniLdWAxOp8HRlhVuwKTy0hqgxpW_OcEkaFTe_fkdz8h_qXDJ5lITXrv8dpbqpBB52YiMrBFTKSRYlQKjYB-MFdL-czKq_cME0gvUGJzfXPrjTIBNUC4Nr_u9m7Dr8UEAMd5vHUYQqRgJNsUa4YfPZ7P91SouYCNdmxsPJ8BFsxUpf5aWnXSC4pKW4stmcuCs8VJguTgV2eWlsnT9svkZB2ny46bIwszICUA5PvquW_nVzzvU2gHEL0R5uukXj_gdSqI4GK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOSeJelfUjXvFJSZZi5kXsTgRGo4aVvMKtAF9X7ObvffIuS0-7QxMD80NGtoYhvZ7if17Dn8x8Q2m0SC1HZnoXDnKrl8BzLdKaxtMsFO0UD9XWqgrORcWjxiJh8jNodHNUbAy9VR_M6_TnDVtHr_tMkpr6BQp1WZpH3j4O58t9zzy6S5bLp-fO7y83bKU5F34rsScOz_zpQ6xKZp6H4F74F_Trxm8crYK-ZVMCE7t-OZyYCrB1FkblUWE8XeOBjXs5UFkmS4ui5yIiSIfKfpxDYfvnw39WBrEXpYJZ_gIRGeNoYjrpSDsU8VOGrHCS4vHODYgTbeBWkvTnoswkzijg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به جنوب لبنان
🔹
رژیم صهیونیستی نقاطی از جنوب لبنان را هدف حملات هوایی قرار داد./جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674649" target="_blank">📅 00:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم
🔹
ساعت ۲۳:۵۰ دو فروند موشک در جریان حمله دشمن آمریکایی به محدوده روستای مسن در جزیره قشم اصابت کرد.
🔹
براساس اطلاعات اولیه، این حمله در محدوده روستای مسن رخ داده و دستگاه‌های مسئول در حال بررسی ابعاد حادثه و ارزیابی خسارات احتمالی هستند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674648" target="_blank">📅 00:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIpd2FRPgG6FdAbbf8NPy5DhxxNX8oqwwSyj1vQdLKh87AOqkA_6Y0q040pSbe6WPCNU7YemyCXmiEiKZFNve7MSFkHDujWqnDoIWLrNWqvUfhbfz9DysEQpNeJVJcEgT81OTBzMTXMsizeTAGF6ekYzoWmiDE27USh_KTbb8jjwDTqHtVMSXSNtfqiZI-Uf84SS10V60MuQ40AiK8uysnZLCFI6gByqfseIluYAHwnIBAK6EfqbN2z1eV_20ueO6dyxXhUsgTg-31x4B7cpG0aE05rgClvXjVauUh8eys6Zo1dhTwdkOcsHjb-Q1RfDqhjF4OpHrW7yUf_yyBNhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/674647" target="_blank">📅 00:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
خوک هار: درصورت ادامه محاصره دریایی توسط انصارالله، ایران و یمن مجازات نظامی سختی در پیش دارند  ترامپ:
🔹
یک سال پیش، ایالات متحده آمریکا به شدت به حوثی‌ها به دلیل دخالتشان در تجارت و بازرگانی از طریق هدف قرار دادن کشتی‌ها، حمله کرد. از آن زمان و در طول درگیری…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/674646" target="_blank">📅 23:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewdOsZyF3R2DFSLHAYfWFc0Vn94F2Jat7PtSDlTlCWcq3gtIxG08rnWIYHQeF5gZeZouZDj3BDfRrg7zzpJyoksVf02gSKcV6aKhoZKXMjm4gfzsFZ8H2jR_PSgQ6YjpE_FUdYCwjyTSFA2SdtJo8FzqAMejo5hVpZf5I558IakizkzktrTLtxhkHPdXzc3Oj7CZq8fPVndiMeiBpU-wAEec1KOr2mFTmn-TlNyZAYNOyDAw8HPl9-MVyLpq89iL283WA7ScxcZ6TUtFIWcghG8Od0Uj4VSBNMPn_y07Tou05fwnrHIOgJ_CcT4mmQYP0ixvqWlVhH8ZulkSqRWQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایگاه آمریکایی علی‌السالم در کویت یکی از اصلی‌ترین پایگاه‌های ارتش تروریستی آمریکا هدف حملات موشکی و پهپادی ایران قرار گرفت
🔹
ارتش کویت ادعای مقابله پدافند هوایی (آمریکایی) با این حملات را مطرح کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/674645" target="_blank">📅 23:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArydlgHu2-6Bc0JRdVWee2YCwirc5u9YNZ--9Ude5B411NMl4GpnK_cZ1PU42TLzf6FATutm9OWqcliChiFVqd1_JuuoRNePWXIaz8R96Vm7oTP2320TgX68NZkvrOFERhSFDoRzPPQ_XCURaDkLbqpKp-hVPekmWn6skd9Rx_F4gZz_k3XcL3c0HKhGr8RMFve80Aj8bp49cR9V55LxqJxsVRBs-b0zEjHIrJU_fXu64qHy1sZERjASGjvTvzoWeAzNLbWpT64FHZBsUJzJLqwkFeLzRS2j4VxHLe_ryy5f9vtq6Hb_TLkpFn14kU0Hm3SPhwqyzPQks35ktMbVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش آمریکا موشک‌های پاتریوت قدیمی می‌خرد
🔹
ارتش آمریکا برای اولین بار پس از چند دهه، موشک‌های پاتریوت PAC-2 را خریداری کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/674644" target="_blank">📅 23:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">🎦
سفر از آگاهی شروع میشه
🔹
قبل از آغاز سفر اربعین، از آخرین وضعیت جاده‌ها باخبر شو. ترافیک، انسداد مسیرها، محدودیت‌های تردد و حوادث جاده‌ای را در
سامانه ۱۴۱
به‌صورت لحظه‌ای دنبال کن تا با آگاهی بیشتر، بهترین تصمیم را برای سفرت بگیری.
🔹
کافیه وارد
سایت یا برنامه کاربردی ۱۴۱
بشی و از بخش
«اخبار»
، آخرین اطلاعات جاده‌ها را به‌صورت متنی و صوتی مشاهده کنی.
🔹
برای اینکه از وضعیت لحظه‌ای جاده باخبر بشی، بیا ۱۴۱
#اربعین
#سامانه_۱۴۱
#بیا_۱۴۱
#وضعیت_جاده
#سفر_ایمن
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/674643" target="_blank">📅 23:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا بداند اگر جنگ را آغاز کند، گستره جنگ فرامنطقه‌ای خواهد بود!
🔹
وعده پوشش هوایی آمریکا برای عبور از تنگه هرمز اعتماد کشورها را جلب نکرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/674642" target="_blank">📅 23:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674641">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
فیلیپ گوردون، دستیار ویژه اوباما: جنگ با ایران جز شکست فاجعه‌ای ندارد؛ تنها راه، امتیاز اقتصادی به ایران در ازای پایان جنگ و بازگشایی تنگه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/674641" target="_blank">📅 23:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674640">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
این مرد مرموز اطلاعات کوه کلنگ را به آمریکا داد
👇
khabarfoori.com/fa/tiny/news-3232486
🔹
سرگیجه آمریکا از دقت حملات ایران | ماجرای ادعای کمک روسیه به ایران در انهدام پایگاه‌های سیا چیست؟
👇
khabarfoori.com/fa/tiny/news-3232561
🔹
جزایر قشم و لارک در التهاب؛ شنیده شدن صدای انفجارهای پیاپی در مناطق ساحلی هرمزگان
👇
khabarfoori.com/fa/tiny/news-3232597
🔹
کارشناس فوتبال به قتل رسید و جسدش به آتش کشیده شد
khabarfoori.com/fa/tiny/news-3232401
🔹
درگیری لفظی امیرحسین ثابتی و شهریاری نماینده مجلس درباره تنگ هرمز
👇
khabarfoori.com/fa/tiny/news-3232520
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/674640" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674639">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🔹
منابع عربی از شنیده‌شدن صدای چندین انفجار شدید در کویت خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/674639" target="_blank">📅 23:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674638">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c92cef2e.mp4?token=Ux9qsP3W7v2M4Fg4_DfdN9mDwfYPQ89m3TwoyjEihAftRFmRXPGMtNwWCYsc0Qp_Eq7DvufaBGwMasf-KPZqEQAXOGaZXuJZv6_zVT27IRWIlc-g2NNS5XaBlDjc8h9SLXmShZP6fycR8_A1gCKUDQ0uItBAMPB3gcNLbn4davC_rz7novxAyDsddsh_AOJtU_eIIom3f_FWOS6x7hPLhxuPv90Fh_D13tauRy4wDh7DyBUYRvw2i6F9AvLJcK3Zgo75nyJ72gkLZBThjr8hl4Xeqg-NwUh222N3yEo1Gye5c8Sjxt_mEKQS3YsP5xaRWbko1vwTkrDUnFqOwYdorwRu__Fml-MBefN7Ef58--dy7zPZp-0fPSMsWqJ8P0iDXWBcpEAw6uLEUpUJ8yuCjTVV54vRF8Sqbd-l2uq1ordqiVdRqCdBAZLLBEEUor4-r9bKugS4mR58oDQT_HsYmgBdWwSP4Cemv6V4pabK0VArfxyYvxruiYGQ9eFOJXnrWc-jQavZMkceT9OP6UpaXLVrH9k7F5Ei6ZBWBICna3l7ggWmFt3GgaM_ArZjxRrYgYCImZWwTFwC6JjT7Ut_4-8xs3gGC7ERUtuNqWebnTtqqE8KNzWQVO14Oh_k3E9MM3xv1kqRYO5gvvi5otT12_H9fonTq0eSrvRa_yl7lVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c92cef2e.mp4?token=Ux9qsP3W7v2M4Fg4_DfdN9mDwfYPQ89m3TwoyjEihAftRFmRXPGMtNwWCYsc0Qp_Eq7DvufaBGwMasf-KPZqEQAXOGaZXuJZv6_zVT27IRWIlc-g2NNS5XaBlDjc8h9SLXmShZP6fycR8_A1gCKUDQ0uItBAMPB3gcNLbn4davC_rz7novxAyDsddsh_AOJtU_eIIom3f_FWOS6x7hPLhxuPv90Fh_D13tauRy4wDh7DyBUYRvw2i6F9AvLJcK3Zgo75nyJ72gkLZBThjr8hl4Xeqg-NwUh222N3yEo1Gye5c8Sjxt_mEKQS3YsP5xaRWbko1vwTkrDUnFqOwYdorwRu__Fml-MBefN7Ef58--dy7zPZp-0fPSMsWqJ8P0iDXWBcpEAw6uLEUpUJ8yuCjTVV54vRF8Sqbd-l2uq1ordqiVdRqCdBAZLLBEEUor4-r9bKugS4mR58oDQT_HsYmgBdWwSP4Cemv6V4pabK0VArfxyYvxruiYGQ9eFOJXnrWc-jQavZMkceT9OP6UpaXLVrH9k7F5Ei6ZBWBICna3l7ggWmFt3GgaM_ArZjxRrYgYCImZWwTFwC6JjT7Ut_4-8xs3gGC7ERUtuNqWebnTtqqE8KNzWQVO14Oh_k3E9MM3xv1kqRYO5gvvi5otT12_H9fonTq0eSrvRa_yl7lVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر آزادی‌خواهان جهان: خلیج‌فارس خانه ماست  خلیج‌فارس، جای حضور ملت بزرگ ایرانی است #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/674638" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674637">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🔹
منابع عربی از شنیده‌شدن صدای چندین انفجار شدید در کویت خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/674637" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674636">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtGPv_zZrslBBUF1bm5lsvHDnTC-K-6fNBejUIDC6CRCVhVQs_o4IykoZ4Lv9MJzeXW6qQDgJXDRZm3mtkLYtTW3SSYOu5dQw_9-0BXiEkfuqUJYMwkzk09VQNQlgwsYMyPyq4uRzZr91Huq0HEEB0cjTtjLmFpwLS0emWJl-YV-nwijVjlJkO078poP1a7NhzBVAfXZgYOXgfikqdH5wmMjLmjqk5IGmedd5n8DfDQBynbE1XnYP1RU6t3f5fv6rXfWyWdbmJJF6L8JFR1z25LfibU4NaC4HEcxIpslEKALzbMz-20s0b_bf9OWoFFMQRcOkJYcn8CgRisfVT7zrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه دوپهلوی عراقچی به مارک روبیو که مدعی شده بود سیاست آمریکا «سر در برابر چشم» است!
🔹
عناصر وابسته به اسرائیل در دولت آمریکا سر خود را در خاک دفن می‌کنند (اشاره به یک ضرب المثل انگلیسی)
🔹
آنها چشم بر واقعیت‌های میدانی بسته‌اند و گویا تنها دغدغه‌شان انتخابات ۲۰۲۸ است.
🔹
تجاوز بی‌خردانه‌ای که این افراد تبلیغ و تشویق می‌کنند، تنها یک نتیجه خواهد داشت: رئیس‌جمهور آمریکا اگر دنبال معامله است، باید بهای سنگین‌تری بپردازد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/674636" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674635">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
المیادین: ساختمان فرماندهی نیروی زمینی در کویت هدف حمله گروه‌های مقاومت قرار گرفت
🔹
این حمله در پاسخ به هدف‌گیری غیرنظامیان ایرانی و عراقی در گذرگاه مرزی شلمچه توسط نیروهای مستقر در این مقر انجام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/674635" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674634">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: نیروهای مسلح آماده هستند تا به دشمن ضربات کوبنده وارد کنند
🔹
خطای محاسباتی آمریکا با پاسخ پشیمان‌کننده ایران مواجه می‌شود؛ دشمن قادر به تحقق اهدافش نخواهد بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/674634" target="_blank">📅 22:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674633">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
۶۲۹ مصدوم و ۵۵ شهید در پی حملات هوایی آمریکا از ۶ تیر تا اول مردادماه
کرمانپور، رئیس مرکز روابط عمومی و اطلاع رسانی وزارت بهداشت، درمان و آموزش پزشکی:
🔹
بین مصدومان ۴۶ زن و ۲۴ کودک و نوجوان زیر ۱۸ سال و در میان شهدا ۶ زن و ۳ کودک و نوجوان زیر ۱۸ سال دیده می‌شوند.
🔹
تاکنون ۵۲ عمل جراحی انجام و ۳۶ نفر همچنان بستری‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674633" target="_blank">📅 22:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674632">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
نقل قول فرمانده موشکی نیروی دریایی سپاه توسط رئیس کمیسیون امنیت ملی مجلس: ذخیره موشک و پهپادی چند برابری برای رویارویی با آمریکا در اختیار داریم
🔹
طرح قانونی تامین امنیت تنگه هرمز هفته آینده در کمیسیون مجلس بررسی خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674632" target="_blank">📅 22:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674631">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72b80e2f0.mp4?token=lhXoe1rBVNIjahn0JrJu0g_1ah49DxKAlDeyaGY-Y8GhIDO8p1EyKzPraq29xWpwwSozFtyChTTV00a4G9j_3EwS6SU-2B_9QNTr-We1lJBz_BCrWAomDEzhBghYVEBWyLnUmsnAtoZQeT1H8yDoYMFfT6V1UwaifkOI-7ABajkarxi1ZOyrgSzz_dWLZyPChHpwvhXn8AmLZngHeDX3_9fzGxgy2U5A69ErFnLiKHYNkWxYdAXVEjbLTWK2bGLELmdIFkqbccyFjYyjYwaYUHzW7jP4xbmuJnXhLDQLYmPT6lFhpE8g5vlDMyf7Eu88eKcFUB-N4kzs4RHDlPc_hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72b80e2f0.mp4?token=lhXoe1rBVNIjahn0JrJu0g_1ah49DxKAlDeyaGY-Y8GhIDO8p1EyKzPraq29xWpwwSozFtyChTTV00a4G9j_3EwS6SU-2B_9QNTr-We1lJBz_BCrWAomDEzhBghYVEBWyLnUmsnAtoZQeT1H8yDoYMFfT6V1UwaifkOI-7ABajkarxi1ZOyrgSzz_dWLZyPChHpwvhXn8AmLZngHeDX3_9fzGxgy2U5A69ErFnLiKHYNkWxYdAXVEjbLTWK2bGLELmdIFkqbccyFjYyjYwaYUHzW7jP4xbmuJnXhLDQLYmPT6lFhpE8g5vlDMyf7Eu88eKcFUB-N4kzs4RHDlPc_hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد مدعی است که جنگ با ایران، بهتر از چیزی که انتظار داشت پیش می‌رود
ترامپ با اشاره به تجربه آمریکا در ویتنام و افغانستان، مدعی شد:
🔹
جنگ با ایران بهتر از آنچه انتظار میرفت پیش میرود. وی تلفات اخیر آمریکا در منطقه را تنها ۱۸ نفر در دو جنگ اعلام کرد، در حالی که شمار کشته‌شدگان ویتنام را حدود ۲۰۰ هزار نفر خواند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674631" target="_blank">📅 22:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674630">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32816f983.mp4?token=o5hPSuxCFeZD5SZsUsmr609DCzADSZFgu_2J-5Ha8xcv3C2wrwBIjWgYkWjkz-OG_Nf5gFtasRHZhhxhVYVgMFLepMI97SVbsogCMMj_mS-_NEyjHBxttaqqrKH1K7tRbO7sw0m9OX2R9idOzDqLRmsYRjopqVAe-UejkJ2kDWhW3XRJ8k9lGxsnRVfxIex1te8Xnbi-tSMzTt2uFUxdIxLAXR7crJaekndbVoYuBAHklFKbxPGIEQPC0e5onsG52cuzrFxuT69TSzFdvDDKY3kDCadTifH8dHXyED0x4G8XPfDAvJj4Gixado7G8qYv465qMu00HCRIB6kBPxpNYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32816f983.mp4?token=o5hPSuxCFeZD5SZsUsmr609DCzADSZFgu_2J-5Ha8xcv3C2wrwBIjWgYkWjkz-OG_Nf5gFtasRHZhhxhVYVgMFLepMI97SVbsogCMMj_mS-_NEyjHBxttaqqrKH1K7tRbO7sw0m9OX2R9idOzDqLRmsYRjopqVAe-UejkJ2kDWhW3XRJ8k9lGxsnRVfxIex1te8Xnbi-tSMzTt2uFUxdIxLAXR7crJaekndbVoYuBAHklFKbxPGIEQPC0e5onsG52cuzrFxuT69TSzFdvDDKY3kDCadTifH8dHXyED0x4G8XPfDAvJj4Gixado7G8qYv465qMu00HCRIB6kBPxpNYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: ایران دیگر ارتش ندارد، ولی از نیروهای هوشمند و ماهر برخوردار است، اما هنوز سطح مشخصی از توانایی ها را حفظ کرده است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/674630" target="_blank">📅 22:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674629">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49efae757f.mp4?token=M4VrbeD9VXEA_HUNal49od7Vvq5x-obTfrPbTQTybfNWnDhChOJwxd-Xa2ZTgkUkzZ_LK1AZgnTbq1oaQMsqIZ1hYqEym5pbhiwb2hlSJag4x-NO2ynpnS_3SDp4uptn6Ix41Vi-hrLKO7Uz0abRh9zdsvZ-LN0i3uB6f3EMZppawfqoJHfkWw38lgMU1617ei88zrY-v6IHh8lDEXDuPcpaG85GLRF1RKuMszNbGFqztwYabLy0nlzxAP9rEZHEeHWHD42O5RVcwvVUdmrL2GOugHjPoHvek88QidEIS0k41ZBNerA1peiQybOXqZBm9UP_RjhWkp9lUtUmmX3Pgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49efae757f.mp4?token=M4VrbeD9VXEA_HUNal49od7Vvq5x-obTfrPbTQTybfNWnDhChOJwxd-Xa2ZTgkUkzZ_LK1AZgnTbq1oaQMsqIZ1hYqEym5pbhiwb2hlSJag4x-NO2ynpnS_3SDp4uptn6Ix41Vi-hrLKO7Uz0abRh9zdsvZ-LN0i3uB6f3EMZppawfqoJHfkWw38lgMU1617ei88zrY-v6IHh8lDEXDuPcpaG85GLRF1RKuMszNbGFqztwYabLy0nlzxAP9rEZHEeHWHD42O5RVcwvVUdmrL2GOugHjPoHvek88QidEIS0k41ZBNerA1peiQybOXqZBm9UP_RjhWkp9lUtUmmX3Pgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقل قول فرمانده موشکی نیروی دریایی سپاه توسط رئیس کمیسیون امنیت ملی مجلس: ذخیره موشک و پهپادی چند برابری برای رویارویی با آمریکا در اختیار داریم
🔹
طرح قانونی تامین امنیت تنگه هرمز هفته آینده در کمیسیون مجلس بررسی خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/674629" target="_blank">📅 22:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674628">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6b19c90e.mp4?token=KBg2mpO-u9ntNB-8zfOInFdHg3D-LgsI8ySDj3veO3VAzniYIrfF0gf0l_QIZlYSv9ojtaKWLL_eHDa74AKgA_VIszsOys0Hezk3wLN9NTJMLWdAxt9NzYQAOKa_vHjkK6PYg9lqniBgWNGikJHSQTn5fQXci3jJcVy2w7P7S9-TBwY4PWK6GszCZVH7LrLAwa33EQnzYRjJKMZDsxgCU1CBDMnKgNY_1Z5aVcBlbldbOQZMnnY9CRd6HoMQ7dXuuLMJ3KXuXmN6EwicI50PhAhngBWoD4nt3wceVO9y_cSRZoL0U5zf8wrFR3pjRZcUp5VYrz9n7kW1Ow7UzqIuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6b19c90e.mp4?token=KBg2mpO-u9ntNB-8zfOInFdHg3D-LgsI8ySDj3veO3VAzniYIrfF0gf0l_QIZlYSv9ojtaKWLL_eHDa74AKgA_VIszsOys0Hezk3wLN9NTJMLWdAxt9NzYQAOKa_vHjkK6PYg9lqniBgWNGikJHSQTn5fQXci3jJcVy2w7P7S9-TBwY4PWK6GszCZVH7LrLAwa33EQnzYRjJKMZDsxgCU1CBDMnKgNY_1Z5aVcBlbldbOQZMnnY9CRd6HoMQ7dXuuLMJ3KXuXmN6EwicI50PhAhngBWoD4nt3wceVO9y_cSRZoL0U5zf8wrFR3pjRZcUp5VYrz9n7kW1Ow7UzqIuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، با همه‌ ما، ایران است
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/674628" target="_blank">📅 22:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674627">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
المیادین: ادعای حمله ایران به نیروگاه کویت، فریبی صهیونیستی است
یک منبع عالی امنیتی سیاسی به المیادین:
🔹
اخبار حمله ایران به نیروگاه کویت را تکذیب و آن را فریبی صهیونیستی از نوع «پرچم دروغین» خواند که هیچ ارتباطی با اقدامات نظامی ایران ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/674627" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674626">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBK0liesWZJn3aI1U7jo3Vub7BgesxFvLtkhZX492QcgbCb--2RI2Fv8AqdKeYLRiCpKaVbek0Rms_E8hI068XveXe292mZgqhCyFn36u2PCJbUKPJtF8LxNttVOifI9DUsoS8gFyvO6RATTHUi_cCwiY1-bYoJWcxIHHbgmUr1aebJBUHfZ0n-vCvcI-1oK2DXnhSaKsMxu0UTb157_VUXGwaK1C2Wawb5K5UL_nvWTLq8UL9vpPdyJ01HplxWiTGrXmxW7mF6kiKQKySbTg4GZKK58LPAhqc9FT0v7xYdJGFZ885Lo8GEpjy9gUTdfkfgZHhKMRGbKhuVlMv0OEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی وارد قرقیزستان شد
🔹
وزیر امور خارجه پنجشنبه شب در راس هیئتی سیاسی به منظور شرکت در نشست شورای وزیران سازمان همکاری شانگهای وارد «چولپون‌آتا»، قرقیزستان شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/674626" target="_blank">📅 22:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674625">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49efae757f.mp4?token=PO0E1rDBLPMvNM_z76AHkaPQDR72E8rAciK0_VbL5t-SWBRZoOPnwPyJXoJvw72xMBNWx8FXA3Xp0dRsWFEZ4XUeHvKMkfiryPnpR9DvgVEPqbETsIvYxW-U6VjSXcWi4__VSmBrUvlM4UVeP1Z5dzQXTpck3uoZty7rre099_w25MD3ymQHoMVKk-nZOZZkRSYNeXFYFr2zqoNzs1vJlaGnErNQVqKqlYwcXRk9ncq-zQlQYLmQnSSMJUWK8t50z3v5SPMzVcSVSqah6M4vzgiUxIP8mcZsF2fMopQwQsPjKxJcHMINcKdzvZK1CixZcR46_ohHHb7aFpe_qyMyhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49efae757f.mp4?token=PO0E1rDBLPMvNM_z76AHkaPQDR72E8rAciK0_VbL5t-SWBRZoOPnwPyJXoJvw72xMBNWx8FXA3Xp0dRsWFEZ4XUeHvKMkfiryPnpR9DvgVEPqbETsIvYxW-U6VjSXcWi4__VSmBrUvlM4UVeP1Z5dzQXTpck3uoZty7rre099_w25MD3ymQHoMVKk-nZOZZkRSYNeXFYFr2zqoNzs1vJlaGnErNQVqKqlYwcXRk9ncq-zQlQYLmQnSSMJUWK8t50z3v5SPMzVcSVSqah6M4vzgiUxIP8mcZsF2fMopQwQsPjKxJcHMINcKdzvZK1CixZcR46_ohHHb7aFpe_qyMyhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقل قول فرمانده موشکی نیروی دریایی سپاه توسط رئیس کمیسیون امنیت ملی مجلس: ذخیره موشک و پهپادی چند برابری برای رویارویی با آمریکا در اختیار داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/674625" target="_blank">📅 22:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674623">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jqj70bATku9t_65XrEjogLVJAgJRMb6HXUDRG09WLYP5JxBig5NIaEivFEVFT0HhzAX-8mPAScY178devy2rO53MxF88TJCUnVnKUmSxOLK5Dj6CL-uRV8hAeFNjeKKaCVsnMfY1iZiHwP4qJbUINMcRSrxdHF5Ev4rEd_E-V39qh41_j3-ZE_4PyhsPqRXpsoyJWRhz6pqVENZAs3BnnBVjpC3JxFQM90ogC3Xu8GwANwwtpcTHbORlHO6MTS1Z55l4EvECWPO08F5t_eq6UUgD0AkqHKuKKIpmbKilL4-y6itOqsLI-KNWufdt_-JyEVec1zaZMzsKwu8l3EcfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjdFsOIyYpjoOegi5OZMtna49NA9zNo16RFFC8Jv6sUnSz6N9b0MEgJ3wnbcDvzTEhRALk_U4t2gg_IZw7fji9YxsVibpWH3cCqgalfhCwJQJM08-UUJJUr1WfFsy_-RH7ZwW0kMhlShQrjI07N3v2e7Gxk2xnyVFBGTADlpfrOPHyKl5xsEfcDnblYzIFT5BP-r5sK3uOI7yJJQ9DAaGIV-ut-m0UFeZmidMdQ4GBEhh-UpqiYKrfUW3WfCR2Sd2Te8AuvEJ2Ak44LeaKuYCdzcYlw_Lu4rS_7MCxGAT5JIrwznebQ3MhU69_W1SZFY02h9MIOM4L9LuyPPn0vAEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اقدام معنادار قالیباف در ديدار با الزیدی
🔹
ادای احترام نخست وزیر عراق به رهبر شهیدانقلاب و شهیدان سلیمانی و ابومهدی مهندس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/674623" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674622">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تکذیب شایعه انفجار در شیراز‌
🔹
امروز هیچ اصابت جدیدی (تا ساعت ۲۲:۱۰ امشب) گزارش نشده است
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/674622" target="_blank">📅 22:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674621">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6112fd8a66.mp4?token=lvHONfMFubtxbIECE5xVdhFyG-zHR-4wTbKJ3ODxqFqNEQr_F_DNEGMZ-YBjjtu4cuNrdeeWabKpLBGVPXvPrv64d6LzEfTsHYAVfMZCOqzyUKMIkywgJ7ccLTjjmFOohr7R0aTfYjmZpqGkQvof3805bQT0JAkG4t3SzD74_JHSLUEPEKD5qQJZLZmD3KOu80cgI5odvd0kXFL1F0gQU7kv4wEwKT6AlTqHyKNQ92_FrgZazd7Fc-m3hD1o4yC3pK8L-s5tl_ZPH58fXtja12Ds7MH4XTSNusafASiEALiM7x00NOi8dXs55E7lz9vG9XwQQAuHJzqJWaQZRhET3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6112fd8a66.mp4?token=lvHONfMFubtxbIECE5xVdhFyG-zHR-4wTbKJ3ODxqFqNEQr_F_DNEGMZ-YBjjtu4cuNrdeeWabKpLBGVPXvPrv64d6LzEfTsHYAVfMZCOqzyUKMIkywgJ7ccLTjjmFOohr7R0aTfYjmZpqGkQvof3805bQT0JAkG4t3SzD74_JHSLUEPEKD5qQJZLZmD3KOu80cgI5odvd0kXFL1F0gQU7kv4wEwKT6AlTqHyKNQ92_FrgZazd7Fc-m3hD1o4yC3pK8L-s5tl_ZPH58fXtja12Ds7MH4XTSNusafASiEALiM7x00NOi8dXs55E7lz9vG9XwQQAuHJzqJWaQZRhET3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی جدید شیطان زرد پس از ناکامی از نابودی توان هسته‌ای ایران
🔹
رئیس دولت تروریستی آمریکا در جدیدترین مهمل گویی خود علیه ایران مدعی شده است که تهران خواهان توافق است، اما من معتقدم هنوز زمان آن نرسیده است و آن‌ها باید ضربات بیشتری متحمل شوند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/674621" target="_blank">📅 22:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674620">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1130431a.mov?token=ACsIIhLADMMHE70vumvozMjL9hlV8QW2-6GlnyPnxf3WrrUdgxaItfg14aLFTL2hBLkyJbjoJ38gGQzmvqcAMbkzpXiIbzSEOz0Iko0mwPHNwnGDDyzd0j9faSYXVFUE6P6St6uLIhDqDirmBmm_ObXEavlQ9mxJTsEDKntrAiYP3xwZ0usJYvfY-GJJonK_ZShoV_B1kJn6wlrB0GmoyWXImxRCkEcrKIv7TJGnilllHbrMJVztwQbKRSAEGsEQH4ffvbeSC5A6ZNrLOho4dpO-AU9ZaE6fV8AOG51iJyPhcH4MLjDzEEi2V0Ehsl_O1M84vme7q-1eYJmJcZ-s0rmDclkeb16Y5Jx_Kxqz3iHSNf7xoOlnBUxV-nEH7yUrmYrL6_fnwL9xn4AupPyncTx0H4_Of24wapNh5I7vK0crIXCQByJ5hvbknzyAQZSA0IdYS6t5DthLE29w2XdoGWxIe3bdhw1TZY-2plUOy-iVAOshKdx3WDAsezOnGtoUQMtoVU_hvnepdeodiDrV9d1twOSxq2ejzAGWJl9SNbr3Z_MGdWaVx7c5B9Tui5mKWaJzJmsocn2KE3KNFxm09vu6T12MZva0sleBOqJyfKOowq1-VVzR0aJja8EGT5YnVHrsAxOUOPOq0Pg2iCPGmDNr08jOvk5ZdSQrEhyRbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1130431a.mov?token=ACsIIhLADMMHE70vumvozMjL9hlV8QW2-6GlnyPnxf3WrrUdgxaItfg14aLFTL2hBLkyJbjoJ38gGQzmvqcAMbkzpXiIbzSEOz0Iko0mwPHNwnGDDyzd0j9faSYXVFUE6P6St6uLIhDqDirmBmm_ObXEavlQ9mxJTsEDKntrAiYP3xwZ0usJYvfY-GJJonK_ZShoV_B1kJn6wlrB0GmoyWXImxRCkEcrKIv7TJGnilllHbrMJVztwQbKRSAEGsEQH4ffvbeSC5A6ZNrLOho4dpO-AU9ZaE6fV8AOG51iJyPhcH4MLjDzEEi2V0Ehsl_O1M84vme7q-1eYJmJcZ-s0rmDclkeb16Y5Jx_Kxqz3iHSNf7xoOlnBUxV-nEH7yUrmYrL6_fnwL9xn4AupPyncTx0H4_Of24wapNh5I7vK0crIXCQByJ5hvbknzyAQZSA0IdYS6t5DthLE29w2XdoGWxIe3bdhw1TZY-2plUOy-iVAOshKdx3WDAsezOnGtoUQMtoVU_hvnepdeodiDrV9d1twOSxq2ejzAGWJl9SNbr3Z_MGdWaVx7c5B9Tui5mKWaJzJmsocn2KE3KNFxm09vu6T12MZva0sleBOqJyfKOowq1-VVzR0aJja8EGT5YnVHrsAxOUOPOq0Pg2iCPGmDNr08jOvk5ZdSQrEhyRbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی وارد قرقیزستان شد
🔹
وزیر امور خارجه پنجشنبه شب در راس هیئتی سیاسی به منظور شرکت در نشست شورای وزیران سازمان همکاری شانگهای وارد «چولپون‌آتا»، قرقیزستان شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/674620" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674619">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
مهدی محمدی، مشاور رئیس مجلس: ممکن است در ساعات آینده سطح تنش بالا رود
🔹
در آستانه شدت پیدا کردن تهدید هستیم.
🔹
هیچ ایده مذاکراتی وجود ندارد.
🔹
آمریکا فهمیده نمی‌تواند تنگه هرمز را باز کند.
🔹
می‌خواستند بر دستگاه محاسباتی مردم و مسئولان در ایران اثر بگذارند.
🔹
برای رویارویی بزرگ آماده‌ایم. باید درس آخر به دشمن داده شود.
🔹
دشمن با چیزهایی روبه‌رو خواهد شد که در طول تاریخ در هیچ جنگی دیده نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/674619" target="_blank">📅 22:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674617">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRubecs5uZo8e0HH_0OzgAuXFEQBrjTAlbnxUYmS0J0rJTolGn-QVGkFNdPTZ4CsSc4PBtoEUxxVqdJq3_LxhkDsLbiZ0FgJDWAqf9iD-CzIUtJEoKINO4zMFdTPpbmaBR-X27kfRPSl5mJxJGaPQ2cn9dLigpJPnGnmHwTOEID0J5JtuUaN1MlWD_mKCHmjv3ANd9QJ-4B07XguCev8Lskm53fGwZYqWunucxWRRXCiCPmOX0Gw0wrXwmZLpucCrGJxuH1ZWgsHuM6j_-JmgwtfoMGAh8A2w6rKVNvUqedkfTgFh-ew4HtO2Wj5AvVTm-uaczWvsYe6GDim1l_FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از منظر امام علی (ع) امر به معروف و نهی از منکر صحیح چه ویژگی‌هایی دارد؟
🔹
امیرالمؤمنین (ع) امر به معروف را تقویت مؤمنان و نهی از منکر را خواری کافران دانسته و این دو را اساس و برترین اعمال دینی می‌خوانند. امام صادق (ع) نیز با تذکرِ عملی و دعوت به تقوا در…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/674617" target="_blank">📅 22:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674616">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
فوری/ یکی از پایانه‌های مرزی کویت هدف ضربات نیروهای مقاومت در منطقه قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/674616" target="_blank">📅 22:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674615">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
بغداد: جنگ ایران ۴۵ میلیارد دلار برای عراق هزینه داشته است
الحره:
🔹
مشاور مالی نخست‌وزیر عراق، مظهر محمد صالح، تخمین زد که جنگ ایران بین ۴۰ تا ۴۵ میلیارد دلار برای عراق هزینه داشته است که ناشی از کاهش شدید صادرات نفت است.
🔹
پیش از جنگ،  عراق روزانه حدود ۳.۳ میلیون بشکه نفت خام صادر می‌کرد که حالا به کمتر از ۱۰ درصد سطح عادی خود کاهش یافته است
🔹
نفت برای عراق سالانه حدود ۸۸ میلیارد دلار درآمد ایجاد می‌کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/674615" target="_blank">📅 22:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674614">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD_0y4yYfEvhj7wcFw_U1431mePuc16nJjMbXSyXWQURX6Nu5c3cS7pXjrUScJfWSexfzSmIbWd6EOsXnGEzm2QS4zlumB9zwGvTr0Rh7hio-qX-2xmT7VdQ6sBNaE1WmdGLHk1i3BoI9QeuQD05V4eH-Pvmk4YRDu2uTnmIBjGbGKoUNtJF6qGTIy-2ly-gUv0pMJmbyOTz1hHkdVgLaciDmIZKTG_mQjtuOnNNEWGTP4UJhb9wFru3jver08KRRENReZLus2T4c8Ct2ErlwTNq7dPsmzPgQgm2el3zZoQt7jBQeaLdyTu_vLgJCVfEy5VC8j8fmMmXB26on5zfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت ۱۰۰ دلاری شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/674614" target="_blank">📅 22:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674613">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlL7dis18CdSv9V-RogVB5HYPutyOL40mJ2fjeW11i5cr1EW_RUHqr876cQRrPi6A49_Es5vEc9JNA8Z1hux0c1Fhelj-qSwb5cEs_EBbst2lTQYyZRF0EmCvuA8-uqlbng-Ka7pdTVf2nchP6dfJDc7nFzmT3ooHbutHxG5nOXb86pCQGZqrBPHPDbL16_RMYUA6q5cLbwhO0Cb9xickoYdUAX677QYlwcHQn2FmdA4QsnV7FKZQfbLSNxNsopDJFwU5PRl3Z_UBDoFojoqHGeNFg2hVz_B4pFKv-Z6xJxR9O_2hGQJMEak7fchJd6lonp2g6Ur-lN-vZeVMUKWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به یک منزل مسکونی در غزه
🔹
جنگنده‌های رژیم صهیونیستی در تازه‌ترین جنایت خود در نوار غزه، یک واحد مسکونی را در اردوگاه «البریج» هدف قرار داده و آن را به طور کامل تخریب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/674613" target="_blank">📅 22:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674612">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579db9bec.mp4?token=Qo7T2naSZjU4GO2K5jSRdP2r54UJFMZf8i0t4saBdAdtsggT5AvfXEEYoSYadNey6RqOLw35OpI4m0mMt62gKk0PMpeA8BMDTnxhXoCoa-nmZVdRNg_0zqE3bHDmKWRg6bh4WIbeEAcnmFhMYIXEFRMpR4uUpi7bHb7ceIl1PkGuNY0KCwqU1BfWEDChPMlBf0Q3Fj0wiYdhZvEDNAdmegMz1FhWGKORwOGCHF8-AalXpVVBybPve02kmUalUKGImfvvkk1VUtDVE1cBSnfuT6gJC8lSimn8gdIuI_Coa7YZ8v_sb2r5nSNsNU7An0tfDo8aq5wLk13xmmXw15gSTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579db9bec.mp4?token=Qo7T2naSZjU4GO2K5jSRdP2r54UJFMZf8i0t4saBdAdtsggT5AvfXEEYoSYadNey6RqOLw35OpI4m0mMt62gKk0PMpeA8BMDTnxhXoCoa-nmZVdRNg_0zqE3bHDmKWRg6bh4WIbeEAcnmFhMYIXEFRMpR4uUpi7bHb7ceIl1PkGuNY0KCwqU1BfWEDChPMlBf0Q3Fj0wiYdhZvEDNAdmegMz1FhWGKORwOGCHF8-AalXpVVBybPve02kmUalUKGImfvvkk1VUtDVE1cBSnfuT6gJC8lSimn8gdIuI_Coa7YZ8v_sb2r5nSNsNU7An0tfDo8aq5wLk13xmmXw15gSTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیبی در سایت پرتاب موشک هیمارس در کویت شناسایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/674612" target="_blank">📅 22:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674611">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
فوری/ یکی از پایانه‌های مرزی کویت هدف ضربات نیروهای مقاومت در منطقه قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/674611" target="_blank">📅 21:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674610">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
زمین‌گیر شدن ناوگان آمریکایی ارتش چک پس از یک سقوط مرگبار
🔹
یک فروند هلیکوپتر نظامی «UH-۱Y Venom» ارتش جمهوری چک در پایگاه هوایی «نامیشت ناد اوسلاوو» دچار سانحه شد و سقوط کرد.
🔹
در این حادثه که حوالی ظهر امروز رخ داد، یک نظامی جان باخت و چهار نفر دیگر مجروح شدند که بلافاصله به بیمارستان منتقل شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/674610" target="_blank">📅 21:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674608">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWQle3bBH6x7cy26-EKEJVpI9gQ3Ikm0vb2OTbMiG49wb_x850mKgtX2CKTZhHiG0_Okyh7w2kL2vzVkma5nyL-9HHhAdJ31R0egmy3ug4RaV0kOHZH14x_88B6M9oGEYvCYOgvzPwvmdC8RELMvdIRhUp7IqIn1gr1nkbFYgMt86wkAGcwO4nNJ0Z4E49ZfJv6ElR3gLw-d8GwQNyR8rKiL_P28kbtEp90ISA3J2n4UuxMToN_hiCVRUXCB29rHPfatk6izVhyeKwKGCf7RUxTzakrXxSkRTGFkeKrbSymECyN35Vpp187hgc5oLS9cVuR_hd3P3OLSpnktpz8IZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOdgZa5BYwfbzsKjw8oOz0PYMP2zs1Gs1s_E3nwFDbmhq_Il8XaJbDJGZG7DspY8kOHt3Nuv7BRyUeaVSI0zadxW75ICUSE1aOcvyw1Ob5-0cmZ6nks5311qV1_GWT-upGPgWUU0mW8ACIyV6eYeiB3pIX83D9jXbuds969VQz9rCKW1mNoj61hSHs4tEy9Y_UKxi3_yVds-c52Yk-DyiJCq5b8t3ExwcPULVhgyXfPuECRsTWAkLFQ66a5ANZrKxG4-JJE898tOGib9ubTQBsYXRxAmmHGuCvvDv2Gfu-W4-_JFKh_T7bpfFQJ1bIrysGqTfYxIEJY8C1zkKt5h0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از انهدام سرورهای آمازون در بحرین با سرجنگی نفوذکننده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/674608" target="_blank">📅 21:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای «سقوط مشهد» در حوادث دی‌ ۱۴۰۴ تکذیب شد
دادستان مرکز خراسان رضوی:
🔹
در آن ایام، اغتشاشگران با اقدامات خود موجب تخریب، احراق و بروز جنایاتی در سطح شهر شدند، اما به‌ هیچ‌ عنوان موفق به تصرف اماکن دولتی و مراکز مهم و حساس نشدند.
🔹
بنابراین، طرح موضوع سقوط شهر، ادعایی بی‌اساس و در راستای اظهارات ترامپ جنایتکار است.
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/674606" target="_blank">📅 21:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcUmRGKjmGUorLRqXmRtTbM8Z4gFsIDM3J97sw9ne1vaWYh7lbYvdTPCmYfKIg25u76HDkeFjEK9zKfFwej1VM8Z3dqFSmhwjl5zcGcztQOqxnOzI5r422zcl571re-uAnzu12cs-0tdjgcje-2u5Lfcd1EiCee8zxAfklLePx6ecBx4-n5zQX1xeMNUWgggSqtG-ECC01YWQx2g2EgSw70lN80rriq5clawYZfbk6RsMA5ruHs3oq5xuorFvUREewtadvxz9gfcF5irN1w6-Zkj7dTkmArsWmcCr51tlllU7qnEnfTF2ySRMAbmuHo5uzDR2nFbLt-7Y3pikLCTiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک احتمال برای جنگ سوم/ اسرائیل دوباره سناریوی ترور را تکرار می‌کند؟
🔹
یک گزینه محتمل، ورود آمریکا به همراه اسرائیل به جنگ با ایران است. این بدین معنی است که جنگ ۴۰ روزه از سرگرفته خواهد شد. اگر این اتفاق بیفتد، احتمالا شاهد همان نقشه ای باشیم که اسرائیلی ها در جنگ ۱۲ روزه و ۴۰ روزه کشیدند: ترور گسترده مقامات.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3231841</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/674605" target="_blank">📅 21:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674604">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46c12035b.mp4?token=L2aKZB2lvF12DIK43oqh2xnVC3TWiMZSOGvWU1o9d1pG1-oczDdNQj1oJ9pg31wYNsbckKkImuxDe2DdvFKTfT9Kr4dgujsTGPq1Spk2IFg7Zve5mZr4dC95HLbqNtJOeyXEIEKSuHYQ4Pv3bBthMISbk05vSn7jTFyk1pCtqc4oo5cpbTlOS0pQCaGeOfRNVsJhUDChnjosRNiy_KGnaJ7Xz6MGMVIpo7HfjYJzzrQYd_cwA1E4Wuoyirc8sQjJesrPB6PUDiFGZ9bnhp-4qaxfO72XvpOTHoZF7ICvaU1_nbZC_r3V8eregtQAowWp79JkfpUAW4Hg03RBG1zFig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46c12035b.mp4?token=L2aKZB2lvF12DIK43oqh2xnVC3TWiMZSOGvWU1o9d1pG1-oczDdNQj1oJ9pg31wYNsbckKkImuxDe2DdvFKTfT9Kr4dgujsTGPq1Spk2IFg7Zve5mZr4dC95HLbqNtJOeyXEIEKSuHYQ4Pv3bBthMISbk05vSn7jTFyk1pCtqc4oo5cpbTlOS0pQCaGeOfRNVsJhUDChnjosRNiy_KGnaJ7Xz6MGMVIpo7HfjYJzzrQYd_cwA1E4Wuoyirc8sQjJesrPB6PUDiFGZ9bnhp-4qaxfO72XvpOTHoZF7ICvaU1_nbZC_r3V8eregtQAowWp79JkfpUAW4Hg03RBG1zFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل از قابلیت ورود به حساب کاربری با ضبط ویدیو سلفی پرده برداشت
🔹
گوگل روش جدیدی برای ورود به حساب کاربری معرفی کرده که در صورت فراموشی رمز عبور و نبود دسترسی به روش‌های معمول بازیابی رمز، از ویدیوی سلفی برای احراز هویت استفاده می‌کند. این ویدیو با تصاویر قبلی کاربر مقایسه می‌شود و در صورت تطابق، امکان ورود فراهم خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/674604" target="_blank">📅 21:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وقتی عشق به نوزاد، امید بازگشت را زنده نگه داشت
🔹
00:12:30 آگاهی نسبت به مرگم و تمایل به شنیدن صدای مادر
🔹
00:25:40 نگاه نامحرم و فریادهای بی‌صدای من
🔹
00:37:10 درک خوشحالی خانمی از نزدیکانم با ظاهر مهربان از مرگ من
🔹
00:46:05 تلاوت آیت‌الکرسی توسط روح برای فرد در حال احتضار
🔹
00:55:40 توسل و درخواست مادری کردن در حق من از حضرت زهرا(س)
🔹
00:59:50 هزینه در مراسم اهل بیت حتی در شرایط سخت
🔹
01:07:10 تغییرات رفتاری محسوس تجربه‌گر بعد از تجربه از دید اطرافیان
🔹
قسمت دهم (مادرانه)، فصل پنجم
🔹
#تجربه‌گر
: زهرا قدیری‌فر
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/674603" target="_blank">📅 21:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674602">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
فرانسه دیپلمات‌هایش را از تهران خارج کرد
🔹
پس از انتشار اخباری مبنی‌بر تعطیلی سفارت انگلیس، منابع خبری گزارش کردند که فرانسه نیز به‌ دلیل نگرانی از تنش‌های اخیر، سفارت خود را در تهران تخلیه کرده است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/674602" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674601">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تداوم سانسور رسانه‌ای؛ تل‌آویو فعالیت شبکه الجزیره را دوباره ممنوع کرد
🔹
رژیم صهیونیستی در ادامه سیاست‌های محدودکننده خود علیه رسانه‌ها، بار دیگر از تمدید ممنوعیت فعالیت دفتر شبکه الجزیره در قدس خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674601" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674600">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6caabfd38.mp4?token=l50n9-L80N2hhsh41dGjyfHZoR6cVgL6kdvmIGcEGiu5bdxCzSCb6mqGovPteu7ytUWWyNqIO0Tg2Ecjp9WDLGUHvtktFADGbjKJp1MO2_30gbCL0aPbrVRAfFsQCzik75r3X1n_0MEvA_iJ1htG332UpRFsQ8FGQLIAb9HDe78xMtipCioKeqEu3t0swYmVFC25TeCFZbu5FLMf8GFeCGGWHKrm0s2UFYY9tnadNbYfMo_4z2_DHSW7CeFKHkUg6sAi2hawi9Eja7mlNLLkn1O9nky9qhBDtkqUQyRV-rHm0__IB4kKMQEpuyEYTwCrmbnl59zQ3aoVG1YCBv6X7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6caabfd38.mp4?token=l50n9-L80N2hhsh41dGjyfHZoR6cVgL6kdvmIGcEGiu5bdxCzSCb6mqGovPteu7ytUWWyNqIO0Tg2Ecjp9WDLGUHvtktFADGbjKJp1MO2_30gbCL0aPbrVRAfFsQCzik75r3X1n_0MEvA_iJ1htG332UpRFsQ8FGQLIAb9HDe78xMtipCioKeqEu3t0swYmVFC25TeCFZbu5FLMf8GFeCGGWHKrm0s2UFYY9tnadNbYfMo_4z2_DHSW7CeFKHkUg6sAi2hawi9Eja7mlNLLkn1O9nky9qhBDtkqUQyRV-rHm0__IB4kKMQEpuyEYTwCrmbnl59zQ3aoVG1YCBv6X7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار گسترده زندانیان از زندانی در کلمبیا
🔹
منابع خبری گزارش دادند که در پی وقوع شورش در زندان «لاورا والنسیا» در شهر پوپایان کلمبیا، بیش از ۳۰ زندانی با ایجاد هرج و مرج موفق به فرار شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/674600" target="_blank">📅 21:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674599">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df788729a.mp4?token=bDXcoRB2gdeyABGBxgxVGiAzs_prxelP5JuY1vroEFRohoKrFaRhWXJIZiIkI49FLbQ0UEha7xWIDmZ88kDACVB_40zcTw4joxa7pP1LNVZeaqfMkU1mJjRPU2Dq7yTsXtKrKMhjnCVvc9wrYV0yMM0XLhO4x4RiLrV_1H8yxYSZzbjkHJ3AnA1XZT0e5ExFra6WRDohka31VUZkjgt09xaTnAHhLchYW583K09J6ncdgwF14ldK_Gj5M6pVv18ed-Yypi3Ij7kIvSIENAkcK1AAHbj7vD8QTB-uCLmN7WcfHgL0SQpTzk_cPKFqRaqf9g7zVPSZmO7hy2GrycwscQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df788729a.mp4?token=bDXcoRB2gdeyABGBxgxVGiAzs_prxelP5JuY1vroEFRohoKrFaRhWXJIZiIkI49FLbQ0UEha7xWIDmZ88kDACVB_40zcTw4joxa7pP1LNVZeaqfMkU1mJjRPU2Dq7yTsXtKrKMhjnCVvc9wrYV0yMM0XLhO4x4RiLrV_1H8yxYSZzbjkHJ3AnA1XZT0e5ExFra6WRDohka31VUZkjgt09xaTnAHhLchYW583K09J6ncdgwF14ldK_Gj5M6pVv18ed-Yypi3Ij7kIvSIENAkcK1AAHbj7vD8QTB-uCLmN7WcfHgL0SQpTzk_cPKFqRaqf9g7zVPSZmO7hy2GrycwscQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند جذاب آشپزی که غذا رو نجات میده
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/674599" target="_blank">📅 21:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674598">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ایلان ماسک: هوش مصنوعی تا پنج سال دیگر از مجموع هوش انسان فراتر می‌رود
ایلان ماسک:
🔹
به گمان من، هوش مصنوعی تا حدود پنج سال آینده از مجموع هوش انسان فراتر خواهد رفت. تا پنج سال دیگر، تقریباً هیچ کاری وجود نخواهد داشت که هوش مصنوعی نتواند بهتر از انسان انجام دهد.
🔹
شاید تنها چیزی که هوش مصنوعی نتواند بهتر از انسان انجام دهد، انسان بودن باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/674598" target="_blank">📅 21:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674597">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14baf46281.mp4?token=ib7lDcUU6IzcllazExOJ9KKV7hDOp2nxZ2mlh_eDEnFKfuEzMC7R2Lj6z98ONFvWqJ72LwUMU2U5zuweMU83WEn30ABAtbX_GW4FhZCDhxPCWhecDlalok8rlgqPJVbEFE_ybEoOBXONDZSVRkeVCvpLlF61olQJxgOHA4pK2fg2frw78PmPWPdodlb6qmi7keJkZCmULb9_prs6IyRMISW4OJtCwyc1xNG5Hg9m4ejMKbFRNPVEunLla4VkmdOuSv3dlvC_cT1RrRUguLdhtvBMOlE0okD16ZPTef1MbSJOdGio9tG2rjwG4yNmTe05-SdJirr7w4Sz75tUt3pE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14baf46281.mp4?token=ib7lDcUU6IzcllazExOJ9KKV7hDOp2nxZ2mlh_eDEnFKfuEzMC7R2Lj6z98ONFvWqJ72LwUMU2U5zuweMU83WEn30ABAtbX_GW4FhZCDhxPCWhecDlalok8rlgqPJVbEFE_ybEoOBXONDZSVRkeVCvpLlF61olQJxgOHA4pK2fg2frw78PmPWPdodlb6qmi7keJkZCmULb9_prs6IyRMISW4OJtCwyc1xNG5Hg9m4ejMKbFRNPVEunLla4VkmdOuSv3dlvC_cT1RrRUguLdhtvBMOlE0okD16ZPTef1MbSJOdGio9tG2rjwG4yNmTe05-SdJirr7w4Sz75tUt3pE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: لاتاری (۱۳۹۶)
🔹
ژانر: درام اجتماعی، معمایی، هیجان‌انگیز
🔹
خلاصه: اگر دنبال فیلمی هستید که تا مدت‌ها ذهنتان را رها نکند، «لاتاری» را ببینید. این فیلم با روایتی پرکشش، از یک عشق ساده آغاز می‌شود اما خیلی زود به ماجرایی تلخ درباره رؤیاهای بربادرفته،…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/674597" target="_blank">📅 21:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674596">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5wCBWcHeia3uctc5vbRioh9T7HT756cq09RXbRo_WCtqUeg67U0y744ezVeGRA3wLQKappJFKEWjWCSEZuvhUSQiNp6idEeJJRU0W0ZPsgtitALGY2MARCk4ihR2zABwh0NiXtgdraXsvq--G8Wxx6Z-EB8BauwuMzVzJnHFdIQB18yF4BRgDk71la9ncnhfdtheCo5AbMa0vBPwWC_25O9KW0xrGFrT7eRaIpeHaifIv0-YWSZepsdvck9fyLkLOZT43jQY_9tHyWCjVOlfvGPR1xJKPxwXXvPZQ_9g_mZSBDoznWY603xi5nT7g9QbrlJjx-ZpvR_pPvwGKj6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪙
حقوقت رو گرم‌گرم طلا کن!
این ماه هم مثل هر ماه، قبل از شروع خرج‌ها سهم پس‌اندازت رو بردار
و حقوقت رو بدون کارمزد در ملّی‌گلد طلا کن.
تا ۵ مرداد با واردکردن کد زیر، می‌تونی از ملّی‌گلد بدون کارمزد طلا بخری:
🎁
کد تخفیف کارمزد: d-mor05
در ملّی‌گلد می‌تونی:
✅
طلای آب‌شده رو بدون اجرت و مالیات بخری
✅
۲۴ ساعته و آنلاین معامله کنی
✅
از ۱ سوت طلا بخری
✅
هر زمان خواستی، داراییت رو بفروشی یا فیزیکی تحویل بگیری
📲
همین حالا وارد حساب ملّی‌گلدت شو بدون کارمزد طلا بخر.
🟢
ملّی‌گلد؛ پلتفرم امن خریدوفروش آنلاین طلا و نقره</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/674596" target="_blank">📅 21:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674595">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWMYx8CDSo4MR8TrqsZRbi2VOVyU2dDF0KjssRR6JQipdMgpo7ZaviOLO1l8lxVdjfeHtmM0zjy2R61JuMUk5JqFRK3Mpp2S55JWaN2r4RrYRlP5nCJHVXsnhaRyp1bJuOpMQVmCa88k0uxe1CzOC3-FpUZW3N_Y-EJ_u30_NVz9czkhVWW6SSPWf8SBhLJmNVziLx_5xJhjLpoaEe1a0_qhlxMhrEWGX1jRNJwaKmqYcDd3Z2IA_W9D4XNk-N_CgNlYK9GrTvuwlqKqjIfXtoJhp9PUJeDmSXJYBoY5TF-zBrV9zplt8I28qA3qr8ewM-nas7fS0oa-Ar71jl_t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتکش ایرانی از خط دزدی دریایی آمریکا عبور کرد
🔹
یک‌ نفتکش منتسب به ناوگان ایران دقایقی پیش با نادیده‌گرفتن محاصرهٔ ادعایی آمریکا از آب‌های آزاد وارد دریای عمان شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/674595" target="_blank">📅 20:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674594">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec0d59648.mp4?token=WizhOfkRMO4s_Rw44CGiVV-iWRaqHjEYXiUrvbg8E6Sg94oQOHG4_rQBiN7zq_Jr1gcn7M06w8LzKKDdjeVGl5TVV_YmRjUFBRVQklIAbqCyl-jOQoKno2-6EW3kQDz369yY7-Z17stRs-w-Gf5buGbuFPZxNYs685Nc0Wbw98qY49kT6I0LNYQzmiN3P0qJgQyooRHMW457bvHQAFdIq32DCN8MgrNP7gHY8zewHtD7F9pzBVkzSZzHh8SuiNQ4dgycPNy4TWSnrvpPz8oeqz4jIXQL-zFkVzlqftdNy8PcdpS2zFwfezb20sOkxAoTIyphnNMXzk4YT4qtKgS6Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec0d59648.mp4?token=WizhOfkRMO4s_Rw44CGiVV-iWRaqHjEYXiUrvbg8E6Sg94oQOHG4_rQBiN7zq_Jr1gcn7M06w8LzKKDdjeVGl5TVV_YmRjUFBRVQklIAbqCyl-jOQoKno2-6EW3kQDz369yY7-Z17stRs-w-Gf5buGbuFPZxNYs685Nc0Wbw98qY49kT6I0LNYQzmiN3P0qJgQyooRHMW457bvHQAFdIq32DCN8MgrNP7gHY8zewHtD7F9pzBVkzSZzHh8SuiNQ4dgycPNy4TWSnrvpPz8oeqz4jIXQL-zFkVzlqftdNy8PcdpS2zFwfezb20sOkxAoTIyphnNMXzk4YT4qtKgS6Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لهجه زیبای بچه‌های عراقی و نگرانی آنان از شرایط ایران و رهبر انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674594" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674593" target="_blank">📅 20:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
اطلاعیه اداره کل آموزش و پرورش استان هرمزگان درباره برگزاری آزمون‌های نهایی پایه یازدهم روز شنبه سوم مردادماه
🔹
تمامی امتحانات نهایی پایه یازدهم در تمامی رشته‌ها، در روز شنبه مورخ ۱۴۰۵/۰۵/۰۳ طبق برنامه قبلی و در تمامی حوزه‌های امتحانی سراسر استان هرمزگان برگزار خواهد شد.
🔹
از روز یکشنبه مورخ ۱۴۰۵/۰۵/۰۴، تمامی امتحانات نهایی پایه دوازدهم نیز طبق جدول زمان‌بندی اعلام شده برگزار می‌گردد.
🔹
زمان برگزاری آزمون‌های تعویقی، متعاقباً از طریق پورتال رسمی اداره کل آموزش و پرورش استان هرمزگان و رسانه‌های معتبر اطلاع‌رسانی خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/674592" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تسنیم: تکذیب هرگونه اصابت جدید در جزیره لارک/ صدای انفجارها از سمت تنگه هرمز است
‌
🔹
برخلاف برخی شایعات منتشرشده در فضای مجازی، تا این لحظه هیچ‌گونه اصابت یا وقوع انفجار در جزیره لارک گزارش نشده و اخبار منتشر شده در این خصوص صحت ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/674591" target="_blank">📅 20:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674590">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
برخی منابع عربی از آتش‌سوزی در بزرگترین نیروگاه برق کویت در پی اصابت یک پرتابه خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/674590" target="_blank">📅 20:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674589">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85bb97986.mp4?token=sLiq965TUTzADmGIg-Cp_vHzWbaYr6e3Q6jklJ5zL0HqNFUkN1GgZKBz1tvyHmavg3vWWvC8ytHWxkEuM2aYJqba8dYQg3TPoMFe4-CRefUiQhXzsCfA7PuRSDZnjvmDiKEhrERihKRr21zCkCTvHYigjTSGdONy0mb5p8WJzmmpNS0-lHNtwmPKssWQlFnL7ZBkfJ2YgKUma_050HVgdat7-WdJaFIY-N3-UOlOEM1wqOYueq-1pk8daxm9fXhrd9wLTkw0mdPbBXLtt0ssolbxQ-Y2SgE0bvt_zV03EhfL5XnQo8yNDJzUZRhHvTwX1ITNzIUUwULd3MtEmxYDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85bb97986.mp4?token=sLiq965TUTzADmGIg-Cp_vHzWbaYr6e3Q6jklJ5zL0HqNFUkN1GgZKBz1tvyHmavg3vWWvC8ytHWxkEuM2aYJqba8dYQg3TPoMFe4-CRefUiQhXzsCfA7PuRSDZnjvmDiKEhrERihKRr21zCkCTvHYigjTSGdONy0mb5p8WJzmmpNS0-lHNtwmPKssWQlFnL7ZBkfJ2YgKUma_050HVgdat7-WdJaFIY-N3-UOlOEM1wqOYueq-1pk8daxm9fXhrd9wLTkw0mdPbBXLtt0ssolbxQ-Y2SgE0bvt_zV03EhfL5XnQo8yNDJzUZRhHvTwX1ITNzIUUwULd3MtEmxYDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در بزرگترین نیروگاه برق کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/674589" target="_blank">📅 20:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674588">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP4JxMS3j3pmu0huC0M-GKj9TXlHqPf7cRK0cu9WvfkPJ8a3Oh2gSpSV9Nmzu5fe6JkCBivQtyDF8Z5Jo7vfchDBMtp_fWwzOy6perkYENmODzw7jZgGDLve0viS4pEtpL9fEe8EQ_zKAhFId9Npw1wNF8X1eLff1YasljWZHP0o8fLI7Dc1LMhXmfo6b89YS1wPPqg3U1CbODHItAE2oz6zRYkab7pCJRlP9tOtWOAGXR1dZ1qEcN5s7K964ZC2byhGmTN2GoLYf6UaNMrlXQwGJdvRrs_Jd7FSYa6knrAVgkIgars5_GRQiOUSIlg-XSV_pzoNwUHGjFkMjDQ5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: پاسخ ایران به حملات زیرساختی، تصاعدی و شدید خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674588" target="_blank">📅 20:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674587">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
شکست خوک نجس در کنگره؛ قطعنامه محدودیت جنگ با ایران تصویب شد
🔹
مجلس نمایندگان آمریکا با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف، طرحی را برای محدود کردن اختیارات ترامپ در ادامهٔ اقدام نظامی علیه ایران بدون تأیید کنگره به تصویب رساند
🔹
چهار تن از جمهوری‌خواهان…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/674587" target="_blank">📅 20:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674586">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54f2d248df.mp4?token=ixGjZBWpEtvBIolZKtGj3i9bz0I-d6tFatA90aKbimlJLzkjJNbYoXcyvAEOz4HsAwG8Dq5oyrDEWO5TLg1qFePpCeepRgmZFCVu6bdzilTFaSFE1GYsPQV7Uq0AfccgPxQ_b7pupru5HDknGMY7DMsnJiC1FIL0d0TTGYqd6wT0SMIoVybbBkYGGGLa5AegriA3cBgd12AP2OggLhxZGLDLbUy8O0sRViM25-CUACP4pGhAT6X72fWrOFtEnFFvJZmB1k4s2kjSJ6H3VNNHsCs49Tw3mJVB7PRAh5M9T8ApLH0M4p0Ffz3FqFAAZL1n60wi_7jzHJ5YnuoWMo5ozpG7xVKtmBi7SmcJhQSz70U7tbDvrdgAt9jtFRy3mCHQnJ3RVFxfMtUWa0JADHEbH0P5QH0AdfKB6veEPOpCIx_xByEUb2FKIuC7pyhXKbBk-O9nrJySLVb9dPh3c6lo5zp2jGTTbw5aMR3Q5tTYqUWz6bikGcA8UUe_J9_z-Uy9UA9Jcub-Ur8ohHSCBR1vZqU5ohwtUkq7t9T6othk7hfXgaVZozQ8vo2ENYi35yT4ZMlxWKezluR2Lpezbqsa42j-Rsnovcve-B6TaRZRldGavhRFMtb4mzvRncZaVNQIuKCl2HTDqKtO7gguJZvigV6f-TPvVgYXxBzU8S-2x50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54f2d248df.mp4?token=ixGjZBWpEtvBIolZKtGj3i9bz0I-d6tFatA90aKbimlJLzkjJNbYoXcyvAEOz4HsAwG8Dq5oyrDEWO5TLg1qFePpCeepRgmZFCVu6bdzilTFaSFE1GYsPQV7Uq0AfccgPxQ_b7pupru5HDknGMY7DMsnJiC1FIL0d0TTGYqd6wT0SMIoVybbBkYGGGLa5AegriA3cBgd12AP2OggLhxZGLDLbUy8O0sRViM25-CUACP4pGhAT6X72fWrOFtEnFFvJZmB1k4s2kjSJ6H3VNNHsCs49Tw3mJVB7PRAh5M9T8ApLH0M4p0Ffz3FqFAAZL1n60wi_7jzHJ5YnuoWMo5ozpG7xVKtmBi7SmcJhQSz70U7tbDvrdgAt9jtFRy3mCHQnJ3RVFxfMtUWa0JADHEbH0P5QH0AdfKB6veEPOpCIx_xByEUb2FKIuC7pyhXKbBk-O9nrJySLVb9dPh3c6lo5zp2jGTTbw5aMR3Q5tTYqUWz6bikGcA8UUe_J9_z-Uy9UA9Jcub-Ur8ohHSCBR1vZqU5ohwtUkq7t9T6othk7hfXgaVZozQ8vo2ENYi35yT4ZMlxWKezluR2Lpezbqsa42j-Rsnovcve-B6TaRZRldGavhRFMtb4mzvRncZaVNQIuKCl2HTDqKtO7gguJZvigV6f-TPvVgYXxBzU8S-2x50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وطن؛ خط قرمز ما
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/674586" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEJrwB0H8-JbVGR0bYo8cGyjkbel2mRmJQMFUxqq6C1cMb-7_4YPCrFSLYUTsiwChyPqJrZx_kTPfHYYIJHgjWxau5nh5e0uNzlI2QDls1ni8UMZMRXxXuBBIApRYeUK_VyCE3ag_H5x3vi-RqCrPJ3GoWX3zFNLMjB6h5xSb1BspQCUCfwDnKmJor9TQqOJ4pGOLOldz1r0A1G5-QQPN-756HEaANMBPapA0j67InLZRN0qBsHsSY7jS722lzzzbH46dxmpnWA6r_emstCQ-hvufB9B5hES00vPThMkrA7IFwO-_XkpvhVz-3-Ut_1y6H7ch61vCRGai7buRSt7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/674584" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وقوع انفجار در کویت
🔹
گزارش‌ها از وقوع انفجار در کویت حکایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/674583" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674581">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzLWV5JM8jeUTaebiUvxXa2NVZ41N-l4x_VvsfXpuR748OWNwF8BsvXiXb3o3p_5RA-qTWu371ymL8qLOyeo8ACXs2U4j-1Tn4rJ9bVW-k-XmS1w17dq2JMRq1KvIv7VCF9LM1eGfBJwD7yR1RgSuy-4QTlJnVPB8j4i3r8EoIRwEaD_u-oOdqw41o4iNl-gdlQIEunzKSqL1qM72ipH1tk77mx5DXX907QbSQvKqF8ELeTMbL-eloMiMQIUQIc7grrqVRFcZDQF7W-o6_P2zWCFVRp-_ne02SyWr0zb2TxbikNO_cQZSUEkj8WGT3GBDrhFoq2NCrAMmTbpRqU_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLyQoB7cWsVoVfTj3_9ebY_f39-OT1jeGzuY_qGnquWA2Cf8JY8r7a0-DiZrCB789Tsk28aWqgpbEnNUZfNLKj0SKrxQX0ylxQTS54jRXys6-x8rkZZnmVHhjSmkW75BOPdQmqmywZhmAqraj4LIuq4h5sQ_4P5BkeCDu1KvtHReOwCqUVuzfwF9MMPKn5Gm9qZzlXSzjSxS9Ou9ojmC7Drtzdu0w0YRBxBnm1Iup80VqhS11L0j8L4fLJRlPvy7rmY73xuWOYu9eCul3fgvNlpwY4lLc4iobb4Qt8blUmMVDER8d7tz2-QbZUexZIPRl0bThoyFIl4WxN1maENwwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کتابی برای آنان که به عشق‌شان نرسیدند
🔹
«شب‌های روشن» از ماندگارترین آثار داستایفسکی، روایت مردی تنهاست که در چهار شب، عشق، امید، انتظار و شکست را یک‌جا تجربه می‌کند. رمانی کوتاه اما عمیق که با نثری شاعرانه، حسرت عشق‌های ناتمام و رؤیاهای دست‌نیافتنی را چنان روایت می‌کند که تا مدت‌ها از ذهن و قلبتان بیرون نمی‌رود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/674581" target="_blank">📅 20:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674580">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8fa936d0.mp4?token=kQA1mAuDQqcFh37EoiM0KfJdAEnMPuy1bsOlbz0hGvP42dxDqvNZSW45iupWwFJ0fgPR2Mky_lR-aPK7tS7NWSJh1bXY3Msn977h_47oHcmojBYUYDviP1bxU7yNo0ub5KwUXhQNLEKF9gV5EYzeHGdbL90celEjAm0ND9WOG7UM3mF-RFAcpc8WYKRo46EcrTe1K98FJI71CfK_oao23evL_ws_Tzhl4tfENvf6DGFsFHOjdyAQKgPaS_HzxrGYUnLM-31m1SEF_lrhTc60rAkAWkwxlT-mpm_EgWpE4AYlnSZSyKrNRaS8uw2NEdPJ7UXLRpJUl0G9WdB3z9KA0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8fa936d0.mp4?token=kQA1mAuDQqcFh37EoiM0KfJdAEnMPuy1bsOlbz0hGvP42dxDqvNZSW45iupWwFJ0fgPR2Mky_lR-aPK7tS7NWSJh1bXY3Msn977h_47oHcmojBYUYDviP1bxU7yNo0ub5KwUXhQNLEKF9gV5EYzeHGdbL90celEjAm0ND9WOG7UM3mF-RFAcpc8WYKRo46EcrTe1K98FJI71CfK_oao23evL_ws_Tzhl4tfENvf6DGFsFHOjdyAQKgPaS_HzxrGYUnLM-31m1SEF_lrhTc60rAkAWkwxlT-mpm_EgWpE4AYlnSZSyKrNRaS8uw2NEdPJ7UXLRpJUl0G9WdB3z9KA0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیویت: برنامه هسته‌ای عربستان در خدمت منافع آمریکا خواهد بود
🔹
سوال خبرنگار: «چرا عربستان سعودی به یک توافق هسته‌ای غیرنظامی دست می‌یابد اما ایران چنین حقی را ندارد؟»
🔹
سخنگوی کاخ سفید: این توافق به شرکت‌های آمریکایی قدرت دسترسی را می‌دهد، موضوعی که درنهایت به سود صنعت و منافع آمریکا است، این بدیهی است که برای ترامپ اهمیت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/674580" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7Cu0h6hpdDi3INaOH3PdnZVxp9KqT4srUA_fTSWPpZnBYbKXTgiN5lQDDlA362dI9_7te_Z1noZ5fSH-vq1V1q7lk7OslUXAdhetXfWIcfIF8mYAQ9Tg1xchhc3QyJlau2LsdkOL9MwqRdwXCfWNKL_gqK3Jh5TBhz02riNzKKM2SYx1bukKqBVJyTFiko4tzOrdeHuNP0CmaD31WMNFgu-evHgqmM1ZaxoFWYza8ODK_B9cZPeu_kPI_lBmmefg1X3oHlkUHNEgkd_BeAYy8wgJCqYoTrZu4kfWaXA26SU84SIyPTY-IAjaSRZpAggy_2VY5Xkb5oyzUGbGS6OQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر قرار باشه یک خرید رو به فال نیک بگیری...  ۱۳ صفر میتونه  همون روز باشه
🥰
حالا چه بهتر که شرایط خرید فوق العاده ای داشته باشی ..‌
💎
طلای اقتصادی با اجرت از ۳٪
🏦
بانک طلا؛ خرید از ۵ میلیون تومان، بدون سود و اجرت
🔄
تعویض طلای سالم با محاسبه عیار ۷۵۰
👰
مرجع سرویس عروس از ۱۰ تا ۶۰ گرم
📲
جدیدترین مدل‌ها داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/674579" target="_blank">📅 20:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674578">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
منابع عبری: فردا ظهر جلسه امنیتی محدود در دفتر بنیامین نتانیاهو برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/674578" target="_blank">📅 19:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674577">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
وزارت دفاع آلمان در تازه‌ترین تصمیم نظامی خود، از برنامه این کشور برای خارج کردن دو فروند از کشتی‌های جنگی‌اش از منطقه دریای سرخ خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/674577" target="_blank">📅 19:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674576">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
صرفه‌جویی امروز ما مساوی با آسایش مردم جنوب
🔹
این روزها گرمای شدید، فشار زیادی به شبکه برق استان‌های جنوبی وارد کرده است. هر کدام از ما می‌توانیم با یک تغییر کوچک، سهمی در کاهش این فشار داشته باشیم.
🔹
خاموش کردن وسایل پرمصرف غیرضروری، تنظیم دمای کولر روی ۲۵ درجه یا بیشتر، کمک می‌کند برق پایدارتر به خانه‌های مردم جنوب برسد.
🔹
این ویدئو را ببینید، منتشر کنید و دیگران را هم به این قرار همدلی دعوت کنید.
👆
دو ساعت صرفه‌جویی، یعنی آسایش یک خانواده در جنوب...
#صرفه_جویی_برای_مردم_جنوب
#قرار_همدلی
#همدلی_با_جنوب
#۲۵_درجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/674576" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674575">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffeaff223.mp4?token=HEkxiqw7wllQHvL-X8pMgrSPYQp4Nm9hoGi9BXei6nYBPrplZV5gKpvA9JYtrfqbc5Eggt0MfBKa1RBpmiI9gI-WbKCHifkk4qAjTmHW2SPV8ayFZugsXEVBUkl0_MIMtVW7l18jUpvnJ31pZXC2x6E7JPlOonDfwQ1FYFC-mYpbxkJECOpQ5CYtCoiAKp0cjP8SAisNRxGeENo18XTHgRCPIQZQTXWs1dhQqXlg5ueutKNBuhLWOJ7mLuIyAvFe6ioM_47jJGAQKRlXbUB3Ig7cEnAOnGy2iDYqW4BSY9M7muIQFpQ-bcNIsleUq1LtipbS28q0XOlRDhru98TGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffeaff223.mp4?token=HEkxiqw7wllQHvL-X8pMgrSPYQp4Nm9hoGi9BXei6nYBPrplZV5gKpvA9JYtrfqbc5Eggt0MfBKa1RBpmiI9gI-WbKCHifkk4qAjTmHW2SPV8ayFZugsXEVBUkl0_MIMtVW7l18jUpvnJ31pZXC2x6E7JPlOonDfwQ1FYFC-mYpbxkJECOpQ5CYtCoiAKp0cjP8SAisNRxGeENo18XTHgRCPIQZQTXWs1dhQqXlg5ueutKNBuhLWOJ7mLuIyAvFe6ioM_47jJGAQKRlXbUB3Ig7cEnAOnGy2iDYqW4BSY9M7muIQFpQ-bcNIsleUq1LtipbS28q0XOlRDhru98TGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌کس خوک نجس را در فینال جام‌جهانی نمی‌خواست
رهبر دموکرات‌های مجلس نمایندگان:
🔹
او بعد از فینال جام‌جهانی خودش را رسوا کرد. او شبیه پیرمردی در باشگاهی بود که هیچ‌کس نمی‌خواست با او باشند و او تنها کسی بود که نمی‌توانست این را بفهمد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/674575" target="_blank">📅 19:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674574">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
هشدار وزارت خارجه آمریکا به اتباع خود در خاورمیانه: برای لغو پروازها آماده باشید
🔹
وزارت امور خارجه دولت تروریستی آمریکا با صدور یک اطلاعیه فوری، از تمامی شهروندان آمریکایی ساکن در منطقه خاورمیانه خواست تا برای شرایط اضطراری، از جمله اختلال در رفت‌وآمد هوایی، آمادگی کامل داشته باشند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/674574" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674572">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دولت درخواست دائمی‌ کردن تسهیلات گمرکی دوران جنگ را داد
جعفر قادری، نایب‌رئیس دوم کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
در جریان جنگ ۴۰ روزه، گمرک مجوزهایی از شورای عالی امنیت ملی دریافت کرد که با اقداماتی نظیر ترخیص بدون ثبت‌ سفارش و انتقال بررسی‌های استاندارد به گمرکات مقصد، سرعت تجارت را به‌شدت افزایش داد.
🔹
اکنون با پایان اعتبار این مجوزها، دولت لایحه‌ای برای دائمی‌کردن آن‌ها تدوین کرده است. استدلال ما این است که وقتی این تسهیلات در شرایط سخت جنگ گره‌گشا بود و مشکلی ایجاد نکرد، چرا در ایام عادی اجرا نشود؟
@TV_Fori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/674572" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674571">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
وقوع انفجار در کویت
🔹
گزارش‌ها از وقوع انفجار در کویت حکایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/674571" target="_blank">📅 19:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674570">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تسهیلات ١٠ و ۵٠ میلیارد تومانی بانک صنعت و معدن برای واحد‌های صنعتی و معدنی
محمود شایان، مدیرعامل بانک صنعت و معدن در حاشیه آیین امضای تفاهمنامه سه‌جانبه میان بانک صنعت و معدن، سازمان صنایع کوچک و شهرک‌های صنعتی ایران و صندوق توسعه صنایع دریایی:
🔹
با امضای این تفاهمنامه ،امکان بازسازی و بازگشت سریع واحدهای آسیب‌دیده به چرخه تولید با ارائه تسهیلات ویژه فراهم شد. تسهیلات غیرحضوری نوبان صنعتی تا سقف ۱۰ میلیارد تومان برای سرمایه در گردش واحد‌های صنعتی اختصاص یافت.
🔹
برای نخستین بار در نظام بانکی تسهیلات ۵۰ میلیارد تومانی جهت خرید ماشین‌آلات دست‌دوم به فعالان حوزه معدن پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/674570" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674569">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما از شنیده شدن صدای انفجار در سوزای قشم خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/674569" target="_blank">📅 19:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674568">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بلوف جدید خوک زرد: در آستانه تصمیم برای حمله‌ای بی‌سابقه علیه ایران هستم
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در گفتگو با شبکه ۱۲ تلویزیون رژیم صهیونیستی، مدعی شد در حال اتخاذ تصمیم برای اجرای یک عملیات نظامی گسترده علیه ایران است. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/674568" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674567">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ab091516.mp4?token=eJzREIlX2uqnP11NiA3udFvGAeL1mqeEqMKN9eyp78px4qS8uXTcxLBynYwkUp8-CXFYYaUdFfr3ma7R9YyyNLdsA_GC30oPUPA8O-zv1sUPD-2vMBH3B1GnsdfuvGxq5PaPzmAOVBa_Pbok8hv2qvaPgUJvsgDELWKTbdojBXBxY9KIW1fH_KEyRztF3V3tQjar79JmzgIAGsjiOC-eaOesI5Hm_8UIiMbmN8OB7Njxp18E3VyAt2_0mj04eFjnKlTyEASGKyjMQW8l_u25dbJiN0xVbvF1yvK4u0JsM2PvZs2jHN5D_ZWGZgjwkciBNYMHE3RznIH4azk9aGZJdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ab091516.mp4?token=eJzREIlX2uqnP11NiA3udFvGAeL1mqeEqMKN9eyp78px4qS8uXTcxLBynYwkUp8-CXFYYaUdFfr3ma7R9YyyNLdsA_GC30oPUPA8O-zv1sUPD-2vMBH3B1GnsdfuvGxq5PaPzmAOVBa_Pbok8hv2qvaPgUJvsgDELWKTbdojBXBxY9KIW1fH_KEyRztF3V3tQjar79JmzgIAGsjiOC-eaOesI5Hm_8UIiMbmN8OB7Njxp18E3VyAt2_0mj04eFjnKlTyEASGKyjMQW8l_u25dbJiN0xVbvF1yvK4u0JsM2PvZs2jHN5D_ZWGZgjwkciBNYMHE3RznIH4azk9aGZJdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: برای پرداخت کالابرگ منابع را تامین کرده‌ایم
رئیس کل بانک مرکزی:
🔹
در صورت افزایش درآمد نفتی منابع بیشتری در اختیار سازمان برنامه و وزارت رفاه برای افزایش کالابرگ قرار می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/674567" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674566">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
بلوف جدید خوک زرد: در آستانه تصمیم برای حمله‌ای بی‌سابقه علیه ایران هستم
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در گفتگو با شبکه ۱۲ تلویزیون رژیم صهیونیستی، مدعی شد در حال اتخاذ تصمیم برای اجرای یک عملیات نظامی گسترده علیه ایران است.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/674566" target="_blank">📅 19:01 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
