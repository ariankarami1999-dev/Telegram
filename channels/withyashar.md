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
<img src="https://cdn4.telesco.pe/file/Sh_oQ_zrKPH5aEEo_UHIkHmH4ohkX1KR4MgYFCYvn9QlX2PzCYPFnD-d4MYSKlo7ZtpWkjqFnbK54kWzJIGARLUdef5dkc1zBOhNl-1dEi9SWtogSSxxpDYbUrnn_C6Y8qwMG1d8Auofk5yJawccRL29wVE0zGv9qyC3_6hfWBgaMkoH-TGadSadhCVWHiuwJhAKuAvFMVkxs5xqfkF2lM9AyiK7QN1fnOKY3mGG0LKITp9gKq5FOG4btqrwhRpDC0VE9keN-QkilQ351WFaKDAtQ2F1Ern5snhIU0Tz6Apv9bacXS3OP73D_kK9wt_GhAKpqTR0z4Xwl0QBu69vvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 333K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 20:12:33</div>
<hr>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اتاق جنگ با یاشار : در سیزن ۹ اپیزود ۵ کارتون سیپسون ها پخش در سال ۱۹۹۷ پیشبینی شده فینال یک جام جهانی بین مکزیک و پرتقال برگزار خواهد شد ! همه نظرشون اینه که این پیشبینی برای همین جام جهانی است !
@withyashar</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/withyashar/16276" target="_blank">📅 19:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
@withyashar</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/withyashar/16275" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">واشنگتن پست : وزارت جنگ آمریکا در حال آماده‌سازی برای اعزام نیروهای زمینی آمریکا به لبنان است.
@withyashar</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/withyashar/16274" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره. @withyashar ( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/16273" target="_blank">📅 18:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عراق به گروه‌های مسلح طرفدار ایران دستور داد تا ۳۰ سپتامبر خلع سلاح شوند
دولت عراق به گروه‌های مسلح طرفدار ایران دستور داده است تا ۳۰ سپتامبر، همزمان با پایان ماموریت ائتلاف ضد داعش به رهبری ایالات متحده، به طور کامل خلع سلاح شوند.
@withyashar</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/withyashar/16272" target="_blank">📅 18:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7LL49XieWZcJH3Lvq9_YsVVYhrlOiHG5WTKfXUPYnHoCuwFrrZgQc3BHLujpteVXnXAwmxNzKMRKnhuFFcahNdb93ODuXaX2_NRfMw-_8MKegfZP3bhgFPK0L3TpKmNOoXxMwRNrtNkq0--og2u9ECY1aBVMUdw6chX1Yr9tZUx5AdURevxD2jy6erXXeXbfma6Rx8bo1TW6sP2Bw2SJdz_3mO25xTu2_SC-CnOoOr6dzCiQ-MO-1ssxxQJ3ADMNKTq_MTCksYX0CeOw-EEssSB0L8QhgMEc19jWjWWqmNYsXR-xoKpX3Yll3JoLXgpCFvCs6-k5Nxd9z2U4Ahtr2p8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7LL49XieWZcJH3Lvq9_YsVVYhrlOiHG5WTKfXUPYnHoCuwFrrZgQc3BHLujpteVXnXAwmxNzKMRKnhuFFcahNdb93ODuXaX2_NRfMw-_8MKegfZP3bhgFPK0L3TpKmNOoXxMwRNrtNkq0--og2u9ECY1aBVMUdw6chX1Yr9tZUx5AdURevxD2jy6erXXeXbfma6Rx8bo1TW6sP2Bw2SJdz_3mO25xTu2_SC-CnOoOr6dzCiQ-MO-1ssxxQJ3ADMNKTq_MTCksYX0CeOw-EEssSB0L8QhgMEc19jWjWWqmNYsXR-xoKpX3Yll3JoLXgpCFvCs6-k5Nxd9z2U4Ahtr2p8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : «لوفت‌وافه» وارد میشود
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/16271" target="_blank">📅 17:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">«جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/16270" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جی دی ونس: ترامپ به ما گفت با توافق با ایران فعلا تنگه هرمز رو باز کنیم و ذخایر انرژی جهان رو فول کنیم تا بعد ببینیم چی میشه‌.
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/16269" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16268">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=dn2RzTg16pHWG8_henJd6CKEmWWljV1Ha8jYF-H8W6rivX6sYYbF3qHPPKougcP1qhl2WZHK-hZDCaAvWdvXpmL8F0UQ8YWMYJhLBqETLsbxjOAyg_iGJyrMuyPG-sqhs48mBiwPgOPy6uvlZ7SLiilBhHPVj12w4S4_0xJOdp8Lknu1IJVwTd8mu8RSzJmsCXihuqnwarWOtXCy6pt_4r6x8SNRzGWGS8qXexs0V78YJGuxFK7Vee0lrtxoEPBfcpP2PoZdOMdnWnEgLl4mWY947_YRDrIYn8n6GPP1iDQtR-sOF-pDfV95eMbl4GdWkx6EETuyHFp0fork1DgTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=dn2RzTg16pHWG8_henJd6CKEmWWljV1Ha8jYF-H8W6rivX6sYYbF3qHPPKougcP1qhl2WZHK-hZDCaAvWdvXpmL8F0UQ8YWMYJhLBqETLsbxjOAyg_iGJyrMuyPG-sqhs48mBiwPgOPy6uvlZ7SLiilBhHPVj12w4S4_0xJOdp8Lknu1IJVwTd8mu8RSzJmsCXihuqnwarWOtXCy6pt_4r6x8SNRzGWGS8qXexs0V78YJGuxFK7Vee0lrtxoEPBfcpP2PoZdOMdnWnEgLl4mWY947_YRDrIYn8n6GPP1iDQtR-sOF-pDfV95eMbl4GdWkx6EETuyHFp0fork1DgTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: منتقدان شما می‌گویند که از ریاست‌جمهوری سود می‌برید.
ترامپ: من سود می‌برم چون بازار بورس در حال رشد است. همه‌ی ما داریم سود می‌بریم.
وضعیت حساب بازنشستگی 401(k) شما چطور است؟ ۸۵ درصد رشد کرده. «متشکرم، رئیس‌جمهور ترامپ!»
من سود می‌برم چون پول زیادی دارم.
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/16268" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ درباره ایران:
ما سه شب آنها را به شدت هدف قرار دادیم، اما اکنون رابطه ما بسیار خوب است.
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/16267" target="_blank">📅 16:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وال‌استریت ژورنال: یک کشمکش قدرت در داخل تهران، مذاکرات صلح آمریکا و ایران را به خطر انداخته است
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/16266" target="_blank">📅 15:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پوتین: به دلیل کمبود گسترده سوخت در روسیه،صادرات هرگونه سوخت ممنوع می‌شود،قابل توجه است که ایران از روسیه بنزین وارد می‌کند و صادرات سوخت به ایران نیز متوقف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/16265" target="_blank">📅 14:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">غریب‌آبادی‌(کاظم دست کج)در راس هیئتی متشکل از وزارت خارجه، بانک مرکزی و وزارت کشاورزی به قطر سفر کرده است، صبح امروز با شیخ «محمد بن عبدالرحمن آل ثانی» وزیر امور خارجه دولت قطر، دیدار و گفت‌وگو کرد
پس از این دیدار،
نشست سه جانبه مذاکره کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای یادداشت تفاهم برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/16264" target="_blank">📅 14:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16263">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/untiPDhkPz02LTDniS_l06qPZe-mudXRRT2wusS48C3ELyfyiLaF01_K_pZvkNVOeXtI6CT-psYWfilJFR2l6vPoPNjaxSEI6tOujOGH-hfG_wCx0Z06k3U2DzUtgnuuvJJAzK65CidSIB2r64vikd6EsN7qO0qsi-DGf_BKWegwBKrhqBMNLExcYsCdmPMOYne7BwKO2uXcqgM9iHfC7WAGPMIC1vbcgnGtmkijC53kblkHM-tGj1SDnKYHIiB5EXBh4_HbJ0fQrf0uCuH9BD0erfQxg88kTyFzuraiQ_eSBOnpzGgxbR7ZYzFSyyJakDuKvIFHJYHp_GygiwaK1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این بین، جمهوری اسلامی هم بیکار ننشسته، یک هواپیمای ایلیوشین روسی تجهیزات را دیشب به تهران آورده و اکنون در حال برگشت است این در حالی است که خبرگزاری‌های عبری امروز صبح گفته بودند که ترامپ در پی یک حمله تمام عیار است
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16263" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16262">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8M-QQsEkXfGNBBM8-P6t1ogKbU2nU0-D5HsNDQ6WURD9bQTcW0R57H7yNTdWZz6ctiuK-k0ObyXafZF6AuHF2zt13Vr1rIoYzdeADg6Fypr8k34QdNvH2KYyyG-XFX2aWLSxlYPH7VAWW6D_ebp2Ta6pgu-ePJg7Tuu8G5Q4OzpqzvvgvZvLqMAmtJTEOzRVSczi3YmZblzyumNkmc0DX5nJU-LZlhthm9cHhqb99ij7YTg9rUGwx5YmddnwkbuLK8oyxPjpnyN6UFnMcKU3y1J_pNAswxY7SJNAtCZL-h2SrbsTTUNcOz4s8VrlWJZ9anOrGtO82bG2fINM_Z0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا جهانی دوباره پایین زده و اومد زیر ۴۰۰۰ دلار
دلیل اصلیش اینه که پیش‌بینی‌ها از افزایش نرخ بهره آمریکا دوباره بالا رفته
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/16262" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16261">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr76KORnnL18JKTeGHziyjGkimCmzANHwCwDGXc2rffFPyOEXz-mJe4EnSExkO_Jiq0jteqtYXNZIuUH9drOIOE7AZ_WV499ZEaHQZLreTnmJdfSpkoUqwZxMDrBrJ8BiUNl7FKVS2GlZDLZgYsMudObid8l2e-wCIaMLRIPhzK4rPUu43t2T-5dJTHNGezINhGQEhJJAQFqTvQCBMNi-LpK95LbH8ERNcWBhuw0s9myW7ShEj06vJA3j1monxsXaRD4-S6RwMsGAv93md-6soOLg5Pp6iKnl_1FHnqooGHnlRbxRaxiusvLWXOqAcRL5zrXITdOXh2kxe9UQ6ceWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق داده‌های CryptoQuant، موجودی نهنگ‌های بیت‌کوین بزرگ‌ترین جهش تاریخش رو ثبت کرده و تا الان بیشتر از ۲۷۰ هزار بیت‌کوین (حدود ۱۶ میلیارد دلار) حوالی قیمت ۵۹ هزار دلار خریداری شده
و
در حال جمع کردن بیت‌کوین هستن
این به معنی رشد فوری قیمت نیست، اما ، نشونه مثبتی برای روند میان‌مدت و بلندمدت بازار محسوب میشه
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16261" target="_blank">📅 13:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=NeqiYFaWDHNXl9h43f4vk77D6PI1vXIZH2oeq-1XYtZNMwaFnQMNLe-_vgpalGvwhQSn66DPwGpX15R-XWDKyQj7QGLdHhZ5eQqVAcUMyG3nMq1Bpkf5-Oa4kFVHsImKc4IkEd_659FY35lu5nXbKXeJ5Te_N8ozEiUKQCumOX4YQ8BqPv7tts-aA9njaWhOaRk0M4Yf-deRHIi9a3Y0NuYlqKAqU0Of4QMtmqGlMaRxuRJHaFxehRkTriYyd7fDpUA2JJkxGEXNKFOPK3imSwBidJrQEG6xQ5yXx_1ufbs-OtwOKP7SQfo6Eb_QZIxU-rb6VlfSc2JGRIgsgFBMc7D7RnR4HqH0XV80MF_g8sui6wnAGF8N4yWrP7KYWdxmO-6StG1sBMnI5zHnK7MTLEk7n0q5ZLBkvbA-5TvuydvwceQHEHWBFsx7QATtWTWNKfwpIqE75srpbVzrJ3tA3-azpGm-yJ64FFi7BkdP831tcXVmVsqA1ISWMwPJJ5OpTcNIUmBcp8axrUuORmIaLsQCknF69l7H2LqeRxp333Gil_B2a-QiR_dmX4jgzGtNZSdSQ-cNnGlPr38gi_kPN7ynhvo7Fnkxzkr5EfHAkuDxIwXlpTyuwcjX_bZltxcI44or8uMiPbdpB3NmxdPaoxMqE7Cbqh9OBcpUes6ICwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=NeqiYFaWDHNXl9h43f4vk77D6PI1vXIZH2oeq-1XYtZNMwaFnQMNLe-_vgpalGvwhQSn66DPwGpX15R-XWDKyQj7QGLdHhZ5eQqVAcUMyG3nMq1Bpkf5-Oa4kFVHsImKc4IkEd_659FY35lu5nXbKXeJ5Te_N8ozEiUKQCumOX4YQ8BqPv7tts-aA9njaWhOaRk0M4Yf-deRHIi9a3Y0NuYlqKAqU0Of4QMtmqGlMaRxuRJHaFxehRkTriYyd7fDpUA2JJkxGEXNKFOPK3imSwBidJrQEG6xQ5yXx_1ufbs-OtwOKP7SQfo6Eb_QZIxU-rb6VlfSc2JGRIgsgFBMc7D7RnR4HqH0XV80MF_g8sui6wnAGF8N4yWrP7KYWdxmO-6StG1sBMnI5zHnK7MTLEk7n0q5ZLBkvbA-5TvuydvwceQHEHWBFsx7QATtWTWNKfwpIqE75srpbVzrJ3tA3-azpGm-yJ64FFi7BkdP831tcXVmVsqA1ISWMwPJJ5OpTcNIUmBcp8axrUuORmIaLsQCknF69l7H2LqeRxp333Gil_B2a-QiR_dmX4jgzGtNZSdSQ-cNnGlPr38gi_kPN7ynhvo7Fnkxzkr5EfHAkuDxIwXlpTyuwcjX_bZltxcI44or8uMiPbdpB3NmxdPaoxMqE7Cbqh9OBcpUes6ICwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکورت و جابجایی دیدنی بی بی نتانیاهو
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/16260" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkqxtZRrSy9--sKJr8DMW-p1IjgYgRlTw6I49APJEk_-YyWPAoPFb45INX_i0cKWx7KVnzRjn-4OHPfY8YP1GqzeBb5f-T6O6yfpynxtLyHP7VXUBiG2YfHg2VTkfX9b0JGwUoSKA7rmGV8xbP8bCIlAm1fJQr1m0aPv6pKVvYebpPMXcTqXkF66WA43v9iMDdw4zA_1Ti7utnfnZ9CN_4L1q9p5FRJmCzz6BMVQ4Iipnei6ZfBSSPI541SCBuOJHup-8GLz1x-NIbMBaGbkUf-9wRYw6cs6iuLMU80Z9g5PIGDQ9p1LyFrhHX808ovQGTKVPogzucdNtugETOnyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خدمات دریایی انگلیس:
یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/16259" target="_blank">📅 12:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز: مذاکرات فنی غیر مستقیم ایران و آمریکا، در دوحه با حضور مذاکره‌کنندگان ارشد و تیم‌های تخصصی در حال برگزاری است
ویتکاف و کوشنر، چارچوب و مبانی این مذاکرات را پایه‌گذاری کردند
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/16258" target="_blank">📅 12:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال ۱۴ اسرائیل : رئیس جمهور ترامپ برنامه‌های عملیات نظامی گسترده علیه ایران را متوقف کرده است تا مذاکرات دیپلماتیک با هدف محدود کردن برنامه هسته‌ای این کشور را در اولویت قرار دهد در‌ عوض از حملات تلافی‌جویانه هدفمند برای حفظ اهرم فشار استفاده می‌کند تا از بی‌ثباتی منطقه‌ای جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/16257" target="_blank">📅 12:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فارس : استان هرمزگان بیشترین آسیب را از آلودگی نفتی ناشی از حمله آمریکا متحمل شده است. این آلودگی بخش‌هایی از سواحل بندرعباس، قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی و تنب‌بزرگ را در بر گرفته و تاکنون بیش از ۲۵۰ کیلومتر از خط ساحلی این استان تحت تأثیر قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/16256" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">1$ Tether = 175,000 Toman
📈
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/16255" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIPnEhYv6wPYzlyleIXGlbFfGVgRiBuNU1R43W1l_R0MYgEQB-2LltZalrOJ5FrPfYbL-GrjPzNPIwRlbSqrrKfOSpTiHfQUys9HvRuKy90JgZZdsBhd_-Qfg9KpwZyWIMu1iQeQY_lwi_rZ94JW4VIcTmQwYhHPiwQ6JfxeIr1MHq48bJ9nDVP46ROVFKYThKZLGCd5tera60Q3Iiic-1RMyYM1X3cda_Eirb4WILL_4NzuVrSh_wuykJs9muAhRhqVd6vRGpUpyLhAzRn5S6dCcNWSzcsl94miTItgszAlFINdcreoLuJ-g6hE9SeAPecsD5Xlg7sPtIIbD2HjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون شیراز نابودسازی از پیش اعلام شده مهمات عمل نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/16254" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlX5Wf-q4bWnaQiTQaiHHEGYOx4fef8wkkJqSOlEGttdn8ffAh1gMaLtlGEdRU_bprThW60R-PDKD2_b5ISa26-CO75P_NFhxQl05ndre3d6GCWZX_eGcAg9g1NpGNt-pqM8fbrdxZ8P2_RAaJdroMMgsxjWLgFqcNkNMkof9Vx07JPdJRl_dh11JEF6GjXQg97-HISXjClyA7gyMeaY-MDnZ38M76nWQuNpz5mU0JwF5AdAoEoSqv-gNGhGnA8bDOo8YNU8hJm5VXUwwcfAWCwLZiFKINSYy1dybOrIx-XpYIau-PsU8gSEq7KFA-jVfqe6vtob6rdnOCaaReLleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند کشتی باری که از مسیری غیر از مسیر تعیین شده ایران در تنگه هرمز، تردد می‌کرد به علت خطای ناوبری و آبخور، به گل نشست
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/16253" target="_blank">📅 11:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرگزاری های رژیم :
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌ کشی و با پارچه پوشیده شده است.
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ ازاین‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد.
@withyashar
یاشار : امام رضا هم جواب کرد
😂</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/16252" target="_blank">📅 11:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سخنگوی ارتش فرانسه: ناو هواپیمابر «شارل دوگل» در خلیج عدن مستقر شد
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16251" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شرکت‌کنندگان مراسم تشییع از ساعت ۶ صبح روز ۱۲ تیر تا یک ساعت پس از تدفین، بیمه شدند
@withyashar
سه‌شنبه ۱۶ تیر نیز تهران تعطیل شد</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16250" target="_blank">📅 10:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16249" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وال‌استریت ژورنال: عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16248" target="_blank">📅 09:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات آمریکایی:
ترامپ در حال بحث درباره احتمال تجدید حملات نظامی گسترده به ایران با وزیر جنگ و رئیس ستاد مشترک ارتش است ، اما تصمیم گرفته است که مذاکرات دیپلماتیک را در حال حاضر ادامه دهد.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16247" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=m0nrO3qxzHL_jMUGjvOvZMIFAOp_0ndmq5zD4OvhNULxXMICNZjxJzqJNcCM0v3lJWXw1ZwwmtxPM0IsIqRxAb7y-JOsY0_4eOQYMwOGuC2NKecMPBzwlE8Y6aTI5XVHet_e2XMOYgdWUnFz-V2KEJGxOw0vD4RbaL9tP-t4EnFRlhsUucU8DcbEzTnIzZaK3KSnIBDCszFXtLto9qnc_95OW4znHQecXO1INrH4ZEx1JLuzwC6qDAN2qKD5NIPU1flYrd2Y5ZKc0YvFgmWweyfmETy0rbm3pvFbJ2D2pwMT6YQ_g6_ED8XyLf5RR9ndxJSDSycmE9YbtMqCnA80kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=m0nrO3qxzHL_jMUGjvOvZMIFAOp_0ndmq5zD4OvhNULxXMICNZjxJzqJNcCM0v3lJWXw1ZwwmtxPM0IsIqRxAb7y-JOsY0_4eOQYMwOGuC2NKecMPBzwlE8Y6aTI5XVHet_e2XMOYgdWUnFz-V2KEJGxOw0vD4RbaL9tP-t4EnFRlhsUucU8DcbEzTnIzZaK3KSnIBDCszFXtLto9qnc_95OW4znHQecXO1INrH4ZEx1JLuzwC6qDAN2qKD5NIPU1flYrd2Y5ZKc0YvFgmWweyfmETy0rbm3pvFbJ2D2pwMT6YQ_g6_ED8XyLf5RR9ndxJSDSycmE9YbtMqCnA80kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها) , سپاه پاسداران که بیضه های این ارتش هم نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16246" target="_blank">📅 02:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رویترز : مقام‌های فرانسوی تجمع بزرگ شورای ملی مقاومت ایران (مستقر در پاریس) را پس از آن ممنوع کردند که نهادهای امنیتی نسبت به افزایش تهدید از سوی فعالان سلطنت‌طلب رقیب هشدار دادند.
پلیس پاریس این تجمع را که قرار بود در ۲۰ ژوئن برگزار شود، تنها چند ساعت پیش از آغاز لغو کرد و دلیل آن را فضای به‌شدت متشنج داخلی و بین‌المللی و خطر بروز خشونت اعلام کرد.
تجمع‌های پیشین شورای ملی مقاومت ایران، که توسط بازوی سیاسی سازمان مجاهدین خلق ایران سازماندهی می‌شود و شرکت‌کنندگانی از سراسر اروپا و جهان را جذب می‌کند، معمولاً بدون حادثه برگزار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16245" target="_blank">📅 02:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUE7J5vGNMoNgUuQZJdPFopx4cNTfSBXLt335BtwLhjrjw9ui9ZBeItsxKiFNRmZy6f70yzvx6WLFbfa4gAdFa_RZoqAoracPq-aVGDipqKM-xZo0Yl5nSMsUBiByq8Az7dvspBq9tHtTjc-ehkREK9SgfmxbITd-Y7FY4__GlSIZlSZPcCgehX8PPNSsVpkLlq_KA9OCPd4-oGRcCMckdYlsmoAdGOGt_RdgIrP0naV_OpVkAs59X-hOqou-5GIyMQspnN0LtLyc-9OSEHMS14F1Ww0MZG1vJFwk1PBdBsX5WVkS4kSuCcFVRXZ9erFHpSy1sQ59AcThDBXJWqJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است.
از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد تهران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16244" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو:
حزب‌الله چیزی شبیه به «پنتاگون» را در زیر زمین احداث کرده است
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16243" target="_blank">📅 01:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shoNSEWJI5dwcaK9uxhdv3B0Jv9CRjlw_yXuqI1TvZg4SgXZIIO7RU92OSEka5WY4IDWD_wK3adem6YRLenZh2EW6Q0zvG8-R51fOD63u5ntKH7ehHGEosDtgM9MZQAHnwq7lFPApOfhcJg8vr9ODlkrkii7IioqmfXSUpBlN5UCF-lEgz_0DY8FFSLy1BVRymqZDhyxuBD_5OTBBu40OLmTyGmBw0qE0yhH-hnWdO7SUXTxtt-zJiA0jDTmsEHShYLOyz8R2ADXy2C21ZA4PectFy_naa-8e8q2ynqzXp82XPM73xI_SkEokjFX4U6dWWiC0HE8N6PXQEECx9DLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد ! ۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه  یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا…</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16242" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسانه رسمی قالیباف بعد از اینکه صداوسیما مصاحبه‌ رو قطع کرد، اعلام کرد بخشیهایی که پخش نشد درباره این موضوعات بوده؛
پاسخ به ادعای بازرسی آژانس از سایت‌های ایران.
جزئیات پیگیری آزاد شدن پول‌های بلوکه‌شده ایران.
توضیح درباره اعتبار 300 میلیارد دلاری برای بازسازی که تو متن تفاهم اومده.
پاسخ به ادعاها و حرف‌های ترامپ.
توضیح درباره پیام راهبردی رهبر جمهوری اسلامی تو 28 خرداد.
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/16241" target="_blank">📅 01:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0q-hZcTcWkr8ykfj78naAn6KI6ZRqw3rPNArtWgw-iRboZSK9E_4PWGoEQn_AsSBv-PmWDOYFGB2vJ1_dMOSfSfSCmA-iPI7E6fZalS-KdPoeKO89_E77oN61qMye9r3cwmkOzOCU5mzLJo8RSiui82Yl3gd3lVmqscHXK7Cgy1JJE_02mZsn7kLBbY67xK5ZmVzTAWQEtoyujY4_1xKeCBezMmJpfKbmApwGy95xL1ZHHC2jvNXiUaD15BL3XphHGASrOm8qQ9Cwt3y_qY6PAhkS1HdegvljFG_hHQY5C4cbqVCQ6i_BobSlGIKzp4pLgjBirS20i1ez7HJqah2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663206797.mp4?token=VDYr500ziZN-VECMbsg_2mvzbLzTyJuxYRcB5UYgy5fCnwXA6t4AC38bY1bbRqbuZohXUD0Dm4RDLhv40giYyuvCbh3uzTVeLQF-qdox6Qw1nTitbogb23Um6hrPMdc31R2uPlmVViR9zoni3VjrEBRzEbfxpuIwB1i4JiaxlNaULsuohMNtcvrUOBrhWn2kpjr1r9_xCYtf5z7R5mdxKUEGCA9ShZ94bG5kY04Er3_rsW22SLcQ3YZaZtPacSk0Fd4DqtQzSm71BJvSAVHyW77tFS_eVsIHuZUNAOVEOk2LEZ1V6wBxpXkcZB6LMsHW1-I1TinsM-PLP_xwEfiMqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663206797.mp4?token=VDYr500ziZN-VECMbsg_2mvzbLzTyJuxYRcB5UYgy5fCnwXA6t4AC38bY1bbRqbuZohXUD0Dm4RDLhv40giYyuvCbh3uzTVeLQF-qdox6Qw1nTitbogb23Um6hrPMdc31R2uPlmVViR9zoni3VjrEBRzEbfxpuIwB1i4JiaxlNaULsuohMNtcvrUOBrhWn2kpjr1r9_xCYtf5z7R5mdxKUEGCA9ShZ94bG5kY04Er3_rsW22SLcQ3YZaZtPacSk0Fd4DqtQzSm71BJvSAVHyW77tFS_eVsIHuZUNAOVEOk2LEZ1V6wBxpXkcZB6LMsHW1-I1TinsM-PLP_xwEfiMqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای افغان به مناطقی در بلوچستان پاکستان حمله کردند و درگیری‌های مرزی آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16239" target="_blank">📅 01:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unJKlWMunXBfv7fwbZaKFofgrpjOGxMR93KY50yHW8VeSeACtRTWGw2kCd2sjto4d6Bl27fpJ55c78sZGbUkXT33FI1HiGaGZAeaHFWyS9ho7T_8wB5G2vgAQyUJYb8FgKTwLuGXcWGfQQQ4Esi5GaiH6XGbpiYu0cDnybPJve3B0V1xgfToke6vjlv1jVwXYYZvDCmRQquYdvIrJStKqUIPFIq_MbrVPUjrl-pLW0TORlx42gxYIz4s44z9qigxWmqTOkm9qMxiJOuYl5-_BOAP1dpSlETvZuJTQhHdN0PxHJRx2SF2QngsG2HXLvYHkw2LBKepAzznTVPqrCZJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان‌های کامیونی پر از تابوت جدید از تروریست‌های حزب‌الله که توسط اسرائیل نابود شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16238" target="_blank">📅 00:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال استریت ژورنال: سپاه پاسداران این پیام را به واسطه‌های قطری منتقل کرد که اگر تضمینی مبنی بر کنترل انحصاری تنگه هرمز توسط ایران دریافت نکنند و اگر ایالات متحده و کشورهای غربی از برنامه‌های خود برای دریانوردی از مسیر جنوبی در این تنگه در نزدیکی سواحل عمان دست نکشند، دوباره تنگه هرمز را خواهند بست.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16237" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaGZy5au2zooT0tRirK4ROQyyMkRhcGk_XcAsgBVOKVeD8AyxHyGD-l56uovYXtq7wOAeZ9QVAyPhU66HV7pKDYP3qh_zD1r1kSw-m8ScVBbIrTzY3_co14EM-xhyyuIhbfwxrdZBKLy96BAXbLO-N8AvXyNW88QL6AalZvmIfvahUpfAQmmR1TYScTEao9aFkz6_-mcmFTcFRuviwpNsYU1MXgaxp_iE-cqcGvExNfREQR0yZuGc5WAkTOVtEJ_ulYYGQJei716ndKtRDDqNDL9paIh_RfcZu0CujYHhdSYqhU-D84Pb6PI-zBRuxlzXS24OVE4RSRg-UiztNOVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین لرزه ای به بزرگی ۶.۲ ریشتر خلیج کالیفرنیا در سواحل مکزیک را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16236" target="_blank">📅 00:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جی‌دی ونس: ایرانی ها یه تاکتیک عجیب برای مذاکره دارن. توی رسانه ها میگن مذاکره نمیکنیم ولی وقتی به ما زنگ میزنن برای مذاکره خواهش میکنن. خب این یعنی چی؟!
ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16235" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اتاق جنگ با یاشار : چک افسری ! این ویدیو نکات ریز مهمی داره حتما دقت کنید! https://www.instagram.com/reel/DaOSvJUxDdL/?igsh=aGRkbWQyN2ozeTNs  کلیک کنید و کار های اداریشو انجام بدید</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16234" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16233" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره.
@withyashar
( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16232" target="_blank">📅 23:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQroocdJePHdY8EEdYWpJHBk4tTx_BhG0aYLY0n4VH8jwrRbxH3znSyg44-_EuNtaW9lhwVlW-6vWiut7XCsLiJz9JVSSTLbbDfXv2aO9vLMwmN6osFgpM_rY_bUvro87LUmm5qdIQKsc3VvoH6aBkDld-BMdtONUIyYqkkXaHxxdMN14HPCF4T8of9_BQDHSHrIqkabudBm2C9cCbbCxsd4B2ta2f3p0tHEwRELrkW4ux5DJ79-vh64v-FaGbBAMM5RR3xOh5Zm2ilvBOSFEQawyecOE4hPYdVJwwCSVSJCtGkfW3mX5M0apOYeeQk3ipcRSBOedk_mrSvMepLHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16231" target="_blank">📅 23:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=YmEWQTyTSpFUjOmInO9Mgjfkx4eLmhXFZj8kPjSkbXjxK6rWZB3KTr-ecZIAuM7Tlijd5E_p55p4qLp3Wn2TFgtOdBWHR84-b_D760vXqf08xhk1sjswhtqenc3f9UFkKUFSVRSoc-TP2tVeBVt_R8_I6ya3AhrFw3oNZ0C4eoSVPm2QGxQ91IUNtdLGFluFjuKAY2-vdtH-QIxJI4pYmtcPal0PCuXcMyhY9j3k13dZHpq7mxzBgeSebwrBbqF_D7oGULwN7VtaTnTaeB3SBV9hYmSZcAgi9pUaxfayHR4ZMJCDrEATHBe9wCpisxJ4XywWAixP34YfO_0jQHeHJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=YmEWQTyTSpFUjOmInO9Mgjfkx4eLmhXFZj8kPjSkbXjxK6rWZB3KTr-ecZIAuM7Tlijd5E_p55p4qLp3Wn2TFgtOdBWHR84-b_D760vXqf08xhk1sjswhtqenc3f9UFkKUFSVRSoc-TP2tVeBVt_R8_I6ya3AhrFw3oNZ0C4eoSVPm2QGxQ91IUNtdLGFluFjuKAY2-vdtH-QIxJI4pYmtcPal0PCuXcMyhY9j3k13dZHpq7mxzBgeSebwrBbqF_D7oGULwN7VtaTnTaeB3SBV9hYmSZcAgi9pUaxfayHR4ZMJCDrEATHBe9wCpisxJ4XywWAixP34YfO_0jQHeHJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16230" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16229" target="_blank">📅 23:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سی‌ان‌ان: آمریکا و کشورهای خلیج فارس نهادها و مقامات مالی حزب‌الله رو تحریم کردن.
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16228" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaBCDJ2RhjKxD5j6_eki0afviRl6wrST6jnNBbGIKmUHj00kRNiuHjBn3oxD2r5QJNrvM_mFsISmpld8WMa6t3lXpCogIU5OtUWQsEH6xpVv8efC6JECyfiRlWhzUNAcbewa3IH_30pkUyXF9BUU-m701dp33WYqd-pcz2jSjLCZ9VmxFKIP_3-glLM6Uhb647zzzAWW9ZlfvKSPjDkjwUtl4Y4mAvw-Ok1AXT1wULgjYg6nsTqEDWwNMhXblUBD2ebmP25c-fNDNlKSSTCYbvQy_oq6BjK-Ne22y0JbqgLvwXSw45BRpD8JxUTr1Hx2k_fca519VBjrGEBz3eszcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تابوت های آماده شده برای خامنه ای و خانواده اش
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16227" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔸
فرمانده سپاه تهران : خودروی حمل اجزای خامنه ای به شکل ضریح حرم امام رضا طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16226" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ در تروث : مایلم به رئیس جمهور شی و کشور بزرگ چین به خاطر پیروزی بزرگشان در قانون شهروندی از طریق تولد تبریک بگویم!
@withyashar
یاشار: ترامپ در آغاز دوره جدیدش فرمان اجرایی‌ای امضا کرد که می‌خواست اعطای خودکار شهروندی به بعضی نوزادان متولد آمریکا را محدود کند(پدر خودش با همین قانون آمریکایی شد چون پدر بزرگش آلمانی بود)، اما دادگاه‌های فدرال دوباره آن را متوقف کردند الانم  عصبی شده داره به چین تبریک میگه
😂</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16225" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16224">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو در خط مقدم جنوب لبنان:
«حزب الله زمانی قوی‌ترین ستون محور منطقه‌ای ایران بود، با تقریباً ۱۵۰ هزار راکت و موشک که به سمت اسرائیل نشانه رفته بود. امروز، تنها حدود ۸ درصد باقی مانده است. اگر تهدیدی برای امنیت یا سربازان خود شناسایی کردید، فوراً اقدام کنید. منتظر نمانید.»
پیام ما به ایران و حزب الله ساده است: شما اینجا جایی ندارید. آینده لبنان باید توسط لبنان و اسرائیل تعیین شود، نه توسط تهران یا نیروهای نیابتی آن. هدف ما امنیت و رفاه پایدار برای هر دو طرف مرز است.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16224" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر خزانه داری آمریکا : فقط چین نفت ایران را خرید
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16223" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد @withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16222" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16221" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=tysw2ZzR3HOJ1lwx46BImTaLdNWiENWphhUC_BOWXHGGKHch2W-QUB3Dha2grgHkOb7GNMMf0XQ0KoB-DjUaoks_4EC9GLHO0B8WUtxt__y1FrgPT_Y5hMfp299jPAgU1BaDVww77ooF9jtQif9v8ET46c2kkmCra2lUAVrIbxAKr-wx4-lyZfKdtRQ-MY8mH5zUMKN6GHXh7Oofo2Uv2WyHOjXF-ZcTKpYFeheXG38lKQ0bfYTZacpQd02UyhFjNiRW9DoOZYoqR2xl7uAHiDcx0h_nES49Ek9EqtI5UTmrx_ZR0WZEGJnansQAvnbi1qb4HKaRcOk3AAyceEWgNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=tysw2ZzR3HOJ1lwx46BImTaLdNWiENWphhUC_BOWXHGGKHch2W-QUB3Dha2grgHkOb7GNMMf0XQ0KoB-DjUaoks_4EC9GLHO0B8WUtxt__y1FrgPT_Y5hMfp299jPAgU1BaDVww77ooF9jtQif9v8ET46c2kkmCra2lUAVrIbxAKr-wx4-lyZfKdtRQ-MY8mH5zUMKN6GHXh7Oofo2Uv2WyHOjXF-ZcTKpYFeheXG38lKQ0bfYTZacpQd02UyhFjNiRW9DoOZYoqR2xl7uAHiDcx0h_nES49Ek9EqtI5UTmrx_ZR0WZEGJnansQAvnbi1qb4HKaRcOk3AAyceEWgNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل از رهبران حماس مرگ مجتبی خامنه ای را لو داد
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16220" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خالد مشعل از رهبران حماس: مجتبی خامنه ای کشته شده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16217" target="_blank">📅 19:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو: اسرائیل و لبنان دو کشور دارای حاکمیت هستند و حزب‌الله باید از بین برود.
هدف از مناطق امنیتی در جنوب لبنان دور ساختن خطر از شمال اسرائیل است. ظرف هفته‌های اخیر 9000 عضو مسلح حزب‌الله حذف شدند.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16216" target="_blank">📅 19:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svbC4-cVPTjHY6KPUWCxz_4fQKeBCU4dKPyhy18zJRKakcsoO0fNV-4GFuFtWVHGckDKMejD1nkBnOK9boePcEjbTZ-Xjaj0e55yZU-GVV3QXg1BWSt89VlrN8PRy7w_wSGNMdwIb5U3noo7dlcok8dXsy9CS5C_GrsLjq15PpkT1EF7kl03JZ6cpIaI_i74lPgFdJA8uYENmEOZ6SxLT54qkaiTkJBDF0wIu15SFHNNYNAav0NVQ9Pht3XbF23WLOfzzv5Fq2wTY5Q0c9bGa4msF6J8l7MvAxpNRx5QY4QqvwiRLQkoNn6vBTyWVsInCOwnE4cf1cgJHaG-DaIBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: اولین آیفون تاشوی اپل هم معرفی می‌شود
iPhone ULTRA
اپل احتمالاً در ۸ سپتامبر ۲۰۲۶ از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و نخستین آیفون تاشوی خود رونمایی خواهد کرد. به گفته مارک گورمن از بلومبرگ، این تاریخ محتمل‌ترین زمان برگزاری رویداد معرفی محصولات جدید اپل است و در صورت تغییر، مراسم ممکن است یک روز بعد برگزار شود.
آیفون تاشوی اپل، که به‌طور غیررسمی
«آیفون اولترا» نامیده می‌شود، گران‌ترین گوشی تاریخ این شرکت باشد.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16215" target="_blank">📅 18:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK9_tvWT_wwd8El7C6kqjN_lB9Wvbq2hG-uiRuS3VSB1vNq8UYpr3LPtF6Bbnn1N1beLaSoWh-KjaHkUiF41vxQDiOUxEJUC9ejLvd2D6hMkZzCNW2S3DUk0Ccs2bMo4csC7cAbg7ZGPQ-phY9KwTzlstzVbbQnOuV2rQbuhAh6sq58Z_SLpvWORfzT0I4iJy-O5dXQ_sUFkdR6-r77A2swqT-VOHUSlSpiezrwZBRt-lcdpACCKbVlXwi_qEv4cUL2mQyjBh5Tsa8rXfS34n3FWIM-vcCzOVp0iM8RAoDiQmNw2BGwWavHlEkfSvX4xwU89O2g0FHGWzcp5CjNcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
@withyashar
یاشار : منظورش مردان تغییر جنسیت داده هست</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16214" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16213">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crUvPLcjfknhnVMWEJET2_y1HlttQxm744Wro6L3gwez9hJylKqOUoFFQVRYv8u5LPvuirBvzsoX-CSLfJyiVuDdQvP5pj7Vvrbm8UweWAhKyE2EkfK3_0tIPm9h56ITg7t20T0j51sxgdoo8xv3dG_bXr6wdEWkwdjyHgdqfHw4qYGNVL-K_e9Y4cde0az0nvx21Vkw1ia8W9ughRPb1l0DK06N3KPUOQRw4lScZnNxgEdOqZIYF4bQP44kjuIBOKZZaoKDr_YiGq7uMNZ0ctwVWYiS7IE9EDQTWE45DWFJIkrR8k8cZ4Sthhc2Y30fzDvQEXGFAS5sYYu5gLwZ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16213" target="_blank">📅 18:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه‌های عبری : «پلیس و سرویس امنیت عمومی اسرائیل (شین بت) یک شهروند آمریکایی را به ظن جاسوسی برای ایران دستگیر کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16212" target="_blank">📅 18:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لقب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16211" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وای نت عبری : یک هواپیمای مسافربری شرکت هواپیمایی الکترا ایرویز که با نام تجاری لات به سمت اسرائیل در حرکت بود، پس از آنکه دو جت جنگنده نیروی هوایی به سمت آن شلیک کردند، در هوا چرخید. طبق گزارش‌ها، خلبان دکمه‌ای را فشار داده که هشدار ربودن هواپیما را می‌داد. این هواپیما از ورشو پرواز کرد و در آسمان ترکیه نسبت به ربودن هواپیما هشدار داد. پس از آن، بر فراز قبرس پرواز کرد و پس از عدم دریافت اجازه فرود در قبرس، برگشت و مسیر خود را تغییر داد. مقامات ارشد صنعت هوانوردی این حادثه را بسیار غیرمعمول و خطرناک می‌دانند و تحقیقات فوری در این زمینه آغاز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16210" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آتاانتیک : اسناد منتشرشده نشان می‌دهد با وجود هشدار قبلی ترامپ درباره عدم استفاده از سیگنال پس از یک افشای جنجالی، مقام‌های ارشد دولت او همچنان از این پیام‌رسان برای هماهنگی‌های حساس استفاده کرده‌اند. طبق اسناد FOIA، دست‌کم ۱۳ گروه گفت‌وگوی سیگنال در نیمه اول ۲۰۲۵ فعال بوده که یکی از آن‌ها با عنوان «Iran/Ukraine Planning» به بحث درباره ایران و اوکراین اختصاص داشته است.
این گروه‌ها با حضور مقام‌های سطح بالا مانند مارکو روبیو (وزیر خارجه)، پیت هگزث (وزیر دفاع) و دن کین (رئیس ستاد مشترک) اداره می‌شدند و برخی چت‌ها دارای حذف خودکار پیام‌ها (۸ ساعت تا یک هفته) بودند؛ موضوعی که نگرانی‌هایی درباره نقض قانون نگهداری اسناد فدرال ایجاد کرده است.
در حالی که کاخ سفید استفاده محدود از سیگنال روی گوشی‌های دولتی را تأیید کرده، این اپ برای تبادل اطلاعات طبقه‌بندی‌شده مجاز نیست. با این حال، وجود چنین گروه‌هایی به‌ویژه درباره ایران نشان می‌دهد این پرونده همچنان در بالاترین سطوح تصمیم‌گیری آمریکا به‌طور فعال در حال بررسی و هماهنگی بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16209" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTl5rOoieshgdBIWjw2nj7uJjWsQaFV3SqUvJhIgvzsasaIdZqOKbKqoJoxzctg6zHzlx1jGeJtBOSUDHBcgtkEHU2sdS5Sw1q3xHRjceksRLf-uN9IjNCwggNP-GC9yATmEp3BLf4VG-N-bWvBYelqIUgxGEu-xDZ13OBhHgms5qhD0XQd2NQVCIiuiQ3KpXn87xp8_cZGLg7sKXbDp6Lac2jFXJshhIfWp-biS0QkiMxiPtrycTNUj0KYnsjLSP5St9T-Jj-OHXfooaWhJzCHWc5nsuK8Z-koRjWQs2f7e_86EE3CPcLqFmWPycxFcPR4cNSTdQKB2pRbYdKtPJfG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTl5rOoieshgdBIWjw2nj7uJjWsQaFV3SqUvJhIgvzsasaIdZqOKbKqoJoxzctg6zHzlx1jGeJtBOSUDHBcgtkEHU2sdS5Sw1q3xHRjceksRLf-uN9IjNCwggNP-GC9yATmEp3BLf4VG-N-bWvBYelqIUgxGEu-xDZ13OBhHgms5qhD0XQd2NQVCIiuiQ3KpXn87xp8_cZGLg7sKXbDp6Lac2jFXJshhIfWp-biS0QkiMxiPtrycTNUj0KYnsjLSP5St9T-Jj-OHXfooaWhJzCHWc5nsuK8Z-koRjWQs2f7e_86EE3CPcLqFmWPycxFcPR4cNSTdQKB2pRbYdKtPJfG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت دفاع اسرائیل و شرکت رافائل در بیانیه‌ای اعلام کردند با توجه به تجربیات دو جنگ اخیر با ایران، سامانه‌های پدافندی گنبد آهنین و پرتوی آهنین را برای مقابله بهتر با پهپاد‌ها،راکت‌ها و موشک‌های کروز ارتقا داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16208" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روزنامه لبنانی المدن گزارش داد:
توافق‌نامه امضاشده میان اسرائیل و لبنان در پایان هفته گذشته به
قطع روابط دیپلماتیک ایران و دولت لبنان منجر شد‌ و عباس عراقچی در پی امضای این توافق‌نامه، سفرش به بیروت را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/16207" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از خبر تشکیل نشدن جلسه جمهوری اسلامی و آمریکا تتر شد ۱۷۲،۵۰۰+ و بیتکوین به زیر ۶۰،۰۰۰$ و همکنون ۵۸،۵۰۰- اومد و نفت برنت +۷۴$ شد
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16206" target="_blank">📅 16:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الحدث: منابع می‌گویند ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16205" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ستاد مراسم دفن خامنه‌ای: مردم برای نزدیک شدن به جنازه علی خامنه‌ای اصرار نکنن.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16204" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:  فردا در دوحه با قطری‌ها «دارایی‌های مسدود شده» مذاکره خواهیم کرد. @withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/16203" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts4bZO19xfocasjztlyxhtYykSl2T4koSX4C_N4wdj9-QkQeEEdVl_lBfcRfPOh-Qns6HvbBwMK-_q9XepS8zKtV6qOaFwx_Jqr43y0BtxBwoh-Dt1vocYeZNDi0CTIje7hdtSY8YqQrH3HrHvGhnWVh74pZFxnl7-_Pv7RG4S3e8aP-FQHevPBSh0wPSEH4toyqaPCHeWGFR84_xPSUxT8Jungw7AFIkAMa44jNmgEFCGM_FTWj6ZdqSY0VPxuauuPZoYpXe_LdlVIQAiuspMR8bD49oCN8S3qrsbovNvJGpOmOKToeVnTUS_vmmS3VM0_g0mED23kdZf9hnPrUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی :
کیپ‌ورد آرژانتین رو حذف میکنه
،
من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16202" target="_blank">📅 15:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی وزارت خارجه:  آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند. @withyashar
😂</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16201" target="_blank">📅 15:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند.
@withyashar
😂</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16200" target="_blank">📅 15:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUApTiNNpRPt76-uHSFUuol-OoOnak_JNXX2OCAoY__HFECpa3xSwBnrf9JDrCucJYX83SJ_cPnvFIOQb7NLDrWZ8dJuD0K190zNrZPJ0L_wrDarZXAizHVP5FJ3CD5YdcYRrPIq-8t9uqFqcaVhertDNAZsSFr7vvrkd4dtFHSvtgyIDp-8NK8TpyY9i_Iv4_AzN2TgHHCnRE2tNY-q-kEWyDxVf7ROXb0LtLoa7FJ-lTtvlZTjqH1wset0e4TAeI1-ijguSGlmtP4Oc3y78kOI6J5PgHVATHkepAVtXt3XX_w0asVpn8mn74hRbO0UotT-rakf3P019s7mGJ_8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر وایرال شده از تعزیه محرم
قیافه بعل یه جوریه که داره میگه خب عاشورا من چه کاره‌ بودم
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16199" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دبیر ستاد تشییع جنازه خامنه‌ای :
مجتبی بخاطر تهدیدات دشمن نمیتونه تو نماز میت پدرش شرکت بکنه و باید مخفی بمونه
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16198" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند  @withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16197" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر : هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16196" target="_blank">📅 14:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMffi9KqQgBxNBtVoUqi45LTNq79b-DEcIdsBqfogt82Daca4Zf9oR73d1RtfzRePE_qdgOQH94cAlIjoiHzb8OG8ZZRvQk3HHtbNcFuyewpupFTF9YaHqmQmLLs9lJukl2XRBnv-2xR5PEoOxr08gGjvQIGcSPF1XuWuiCQ2ZD3AhF3b9XuaXKHR3gvvrTWzq3Qd2-YppfMs8oOJBxvjD2oI9goQSMZ83yfRpS1kCjP63jUCMJFjxpZCQ3GMy7SXbYEABQF6CTAn7Eahux93ZkHCALBQ0xg5xtUTqYApQbTU8yctMPwW5EcWn9GR_NSl0DAZA2DqQtP6kIRoE8cxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی آمریکا موشک ضدکشتی LRASM را با بمب‌افکن پنهانکار B-2 عملیاتی کرده و در رزمایش Valiant Shield 2026 با آن یک شناور آبی‌خاکی بازنشسته را غرق کرده است.
در حالی که B-1B از قبل این موشک را حمل می‌کرد، تلاش برای افزودن آن به B-52 و P-8 ادامه دارد، اما B-2 فعلاً تنها پلتفرم برد بلند پنهانکار برای شلیک آن محسوب می‌شود.
ترکیب برد بلند LRASM با پنهانکاری و سنسورهای B-2، توان حمله دقیق و دورایستا را افزایش داده و تهدیدی جدی‌تر برای ناوگان‌های دریایی، به‌ویژه در اقیانوس آرام، ایجاد می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16195" target="_blank">📅 12:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر امنیت داخلی آمریکا:
پس از حذف ایران از جام جهانی رقصیدم
روزنامه نیویورک تایمز گزارش داد، مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16194" target="_blank">📅 12:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک منبع آگاه غربی:
ممکن است اسرائیل ابتدا در هفته های آینده وارد جنگ با جمهوری اسلامی شود سپس ایالات متحده آمریکا به اسرائیل ملحق خواهد شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16193" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داد که مارکو روبیو، وزیر امور خارجه ایالات متحده، توانسته است دونالد ترامپ را متقاعد کند که اسرائیل باید حضور خود در لبنان را حفظ کرده و علیه ایران اقدام نظامی انجام دهد.
در همین حال، جی‌دی ونس، معاون رئیس‌جمهور، ناچار به عقب‌نشینی از موضع خود شد و در نهایت اعلام کرد که از توافقی که با محوریت اسرائیل شکل گرفته حمایت می‌کند، نه از ابتکار عمل ایالات متحده.
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16192" target="_blank">📅 11:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJb6XI08FlpypvP-eqsbVyvxXW2dRKUaKUJEgkfiZPawNu8n1dCwp8WjfBxFHxCuB64LnoDBt0_yLyuPpvVgnMkWMWV7OuimSrU6rHEWKARA1_ywqu7CWmR2OPKRdvwARbnYc2ZrSMfk8f4Nq6EwWVHZbWiJukwWCozFRz6n33R_t0EZXSTdx_SD_oZZRJoT6wRwtlRrTfrLNKbftkrbU6SdXa41L8sWLP-IEiAQOApGoBzHbpGMoEX63etCn6R4wkLo9FE-MNRAfTv9Xb91lwpIZc9OhRQD175okFy7Undz6TekhakdsUgmG7c-RpWMyFdVZlqWd93K5H7HsBy-sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین تصویر ثبت شده از محمد اکبرزاده قبل از تصادف و مرگش
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16191" target="_blank">📅 11:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWn3jLuPx2VBJh0E5mYdlWPJ_Ty1nOyhaqZcFBQTEF8_2XKZBARKkdd5Zu4iCV4DxQwB7fiVRERTl8sNLFvYJaJxaKEHaduWRxj7QrjwimfoG1uv26_QoB8j2pgmak_tciN5wWSvtO16TKCzZEBfEjSDMuSfMZEblD9dXOU5ax7QLqMe0ZjJ5TcXLcMaTXT7Eu69oKomasitqylKOz0vJ_FyPodshNFcGLckqIvEmEZTOnSoUdUwy9ueAgcaZoe8JJ63cGgHcWtGphuI4LzrIf-2vQabenlekmZTVjcR4-4HX52rozvzQC9D2LjdWtd5QqgpQ43YvzfsJBgdTww7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان انفجار مهیب و برخواستن دود از سمت فرودگاه شیراز
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16190" target="_blank">📅 11:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اسرائیل در حال آماده شدن برای شروع مجدد جنگ تمام‌عیار علیه ایران
بر اساس اطلاعات موجود، اسرائیل در حال آماده‌سازی یک کمپین مستقل برای آغاز دوباره جنگ تمام‌عیار علیه ایران است. این تحرکات نشان می‌دهد تل‌آویو مسیر جداگانه‌ای از آمریکا در پیش گرفته و انتظار می‌رود در آینده بسیار نزدیک وارد فاز عملیاتی جدیدی شود.
در همین حال، فعالیت موساد در داخل ایران به‌طور محسوسی افزایش یافته و شتاب ناگهانی این تحرکات، از تسریع آماده‌سازی‌ها هم‌زمان با عملیات مستقل اسرائیل حکایت دارد. هم‌زمان، انتظار می‌رود در روزهای آینده موارد بیشتری از انفجارهای مرموز، آتش‌سوزی‌های صنعتی و حوادث مشکوک در داخل ایران رخ دهد؛ رخدادهایی که با الگوهای تاریخی خرابکاری و عملیات پنهانی موساد هم‌خوانی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16189" target="_blank">📅 11:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد !
۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه
یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا نزدیکی سریلانکا به نمایش می‌گذارند
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/16188" target="_blank">📅 10:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16186">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=SwEOuLSmlEVit3YEqyj6-2jGTICs7tkxQXnG5gQL8P3hVaHZi2_ppRJxx1qljkmR2_5z-w_MIF18QvkNo0w3oLBNvbV3rCJKarL_yHPZ9em6seu2bauqWK-HtC-57wQKbW_IU-qn2YtvwIMSyzTTQzpNI0_xefktfFsH0vZj2UwfH0leCqnShvoui7vmwpiWlz0JyWGImAaTQmqq18WRLkUO0FsPSK9eS1FBNEt5XliuVeGwpPKCLslhOgBK5K5lrH_VzMcod_9frRAU-52rl8fVY7OoPBwY2uyXDRGMqdhBshx3Pa0M-MohMWQJfoOIJoCC569m6eD-r71cgDTzKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=SwEOuLSmlEVit3YEqyj6-2jGTICs7tkxQXnG5gQL8P3hVaHZi2_ppRJxx1qljkmR2_5z-w_MIF18QvkNo0w3oLBNvbV3rCJKarL_yHPZ9em6seu2bauqWK-HtC-57wQKbW_IU-qn2YtvwIMSyzTTQzpNI0_xefktfFsH0vZj2UwfH0leCqnShvoui7vmwpiWlz0JyWGImAaTQmqq18WRLkUO0FsPSK9eS1FBNEt5XliuVeGwpPKCLslhOgBK5K5lrH_VzMcod_9frRAU-52rl8fVY7OoPBwY2uyXDRGMqdhBshx3Pa0M-MohMWQJfoOIJoCC569m6eD-r71cgDTzKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قنبریان سخنران صداوسیما: اگر ترامپ را قصاص نکنیم رهبر فعلی باید بدون شک تا ابد در مخفیگاه باشد
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16186" target="_blank">📅 10:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16185">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igqMczuk9KS7voUwD7m0s9-ZEfPOaVlwVZz2Bd-CVT2AspKsDK-O5MDpt3mJ4HO73TniPcd6tJ0Zl8YujwgrVHUQVVboEU_xASUE3i9VCS98OtUPgEvXv0aSjcZpijXIkzYKbUnAoAuhVvV8LxJqfckC5VaXNu3r4GOCoR8QOuWOICc3j8_7PDLstQ51-YClN5nhG9cOBqPVnojLqkMfnXnrxbVdcW2g_Vf5XPwt25YxPy5u5YeBqro_g3Gxn927B8mYLBO033M1DDBLNEz7r7CP7V3cVrx6RxyRzG5SwORWOHsCmSovUsmAqP57OZxzTDRvQS1qNrVE7CBJTtk9lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو نیروی سپاه پاوه ترور شدند
روابط عمومی سپاه استان کرمانشاه:
طی اقدامی، افرادی با تیراندازی درب منزل در شامگاه دوشنبه هشتم تیرماه، «برهان کریسانی» و «خالد خالدی‌نیا» دو تن از نیروهای بومی ما را هدف قرار دادند
در‌این عملیات خالد خالدی نیا بهمراه خواهر و خواهر زاده‌اش کشته شد﻿
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16185" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16184">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اسناد محرمانه هک شده مادربرد و تراشه جدید آیفون ۱۸ پرو مکس فاش شدند.
بیش از ۶۳۰ گیگابایت اطلاعات از جزئیات کلیدی آیفون ۱۸ پرو و آیفون ۱۸ پرو مکس اپل به سرقت و فاش شد.
رویترز : فایل‌های حساس شامل فهرست قطعات و تأمین‌کنندگان، و حتی عکس‌هایی از مدل‌های در دست‌توسعه آیفون 18 پرو از طریق نشت داده در شرکت هندی Tata Electronics توسط هکر ها روی دارک‌وب منتشر شد.
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/16184" target="_blank">📅 10:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16183">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حزب‌الله:
قمار سر توافق ننگین بی‌نتیجه است
حسن عزالدین، عضو ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان:
صهیونیست‌ها مکان‌هایی را در به اصطلاح
مناطق آزمایشی
گنجانده‌اند که اصلاً جای پایی در آنجا ندارند مانند شهرک فرون.
دولت لبنان اساساً خودش را فروخته
و به دنبال فروش قدرت لبنان است.
پرونده لبنان همچنان در اولویت ایران قرار دارد
و جمهوری اسلامی ایران این پرونده را به هیچ طرف دیگری واگذار نخواهد کرد. معادله‌ای که تهران ایجاد کرده همچنان پابرجاست و ادامه می‌یابد.
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/16183" target="_blank">📅 09:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16182">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شروع حذف‌های هدفمند؟
دریادار دوم محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، متولد ۱۳۵۰ بود و در زمان سانحه رانندگی و درگذشت(دیروز)،حدود  ۵۵ سال داشت. او تازه سه هفته پیش، در روز دوشنبه ۱۸ خرداد ۱۴۰۵ معادل ۷ ژوئن ۲۰۲۶، در فهرست تحریم‌های اتحادیه اروپا قرار گرفته بود!
وی در ماه‌های اخیر در سخن‌رانی‌ها و مواضع مرتبط با امنیت خلیج فارس و نظارت بر حضور نیروهای خارجی فعال بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16182" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16181">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دیوان عالی آمریکا امروز سه پرونده سرنوشت‌ساز برای دولت ترامپ را تعیین تکلیف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16181" target="_blank">📅 09:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16180">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMKtt7qABd3ELv8_BPWDT4LGwGp8QP17t6HCuLALqGQjI6sLRmfr0zHe-_c4neAv7_eVOzKjcPaDzdLbodfjNeqbqP40rGkIn1oB5Bl1m4Qur3roLeWt7Vb2QQelKYpLBN0EmVimvUdOiaUiDU9jtBbanSyBAIkkWhi_Z59mUyotsl3tAY2A2kkrYj5tcZUwrFQ_gT9SfDBOf8YUjr9kn3OVnShOCeHt_NZpowkTF85LFhuNqyVSO4UWGr7o-8s-96VCcVe8AcUcmj0tObCnIW8cR7Lf4RQeGP2S-1DcQUXyIqDk1TpYNeRllFMFswpP7MldG6x_qrqTqXwzfVfUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید روزنامه همشهری :  انتقام قطعی است
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16180" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16179">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">روبیو: احتمال شکست مذاکرات با ایران وجود دارد
شبکه «ام‌اس ناو» به نقل از منابع مطلع: روبیو در جلسه توجیهی با اعضای کنگره آمریکا، گفت که دولت ترامپ هیچ توهمی ندارد که مذاکرات با ایران آسان خواهد بود.
روبیو به کنگره گفت که احتمال شکست مذاکرات وجود دارد، اما دولت می‌خواهد به مسیر دیپلماتیک فرصتی بدهد.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/16179" target="_blank">📅 09:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16178">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ به شرکت‌های نفتی: «قیمت‌ها را کاهش دهید - وگرنه مشکلات بزرگی پیش خواهد آمد!»
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16178" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16177">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ0bvjrNVr72W3K6ZhreVXNwkj1z_ZiQZRG3PMcOfckDFA_S7xZWrhkj-yFfw_rXzqODci8XqHYe9JS9KS2SnR5OxppSEpZf2lqQZYRgouNxYMKy77o5dlMOWmxgAJWcFxKU3WC5XyRIYVt0ZwprUfB8yuCzIuo-9kNb4PnSMsNq25VP80wIJtqo6WQAQdu757Iq2uYbqmTevtNDLOec-aNEuw1C9anRFIXS86TFjva582TihYK8m3soi-veeOHyHnn-QNWcgyASNnCh1lDezTXUj22TyfMeY2-l8LBmtqU0onN9Ugmkttat9vU2qDxNv41_pT_xDOxZVNEq3v0G5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار هدفمند در موناکو فرانسه
۳ اکراینی نفر زخمی شدند که حال دو نفر از آنها وخیم است.
پلیس در جستجوی مظنون فراری پس از انفجار «هدفمند» در موناکو است که شامل یک وسیله انفجاری جاسازی شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/16177" target="_blank">📅 08:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16176">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حمله مسلحانه به ایست بازرسی پاوه در کرمانشاه باعث کشته شدن 3 سپاهی شده که یکی از این افراد نقش مهمی در قتل عام مردم در سال 401 داشت که به هلاکت رسید
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16176" target="_blank">📅 08:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16175">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتانیاهو : اگر از غزه خارج میشدیم، خامنه‌ای، نصرالله و اسد الان در قدرت بودن.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16175" target="_blank">📅 00:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16174">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Akur_ed3vLFH65vYqQ8I1p8IMjrZDlyjCrTlhJJRPrpSPf8swSSDUIMcOwVWsi5xEWLQNOrYSSLm3cYznavslLP7E7RxZX6TRBs2HAW55Rpl8nBqhW2as0on8hnjdsU9nuY7UO-wqRkyztsTytNtpulNGGe4cON22nAlvs_l1RhUqw_EMoSsqXID_ia50_3Pas3wQApwtnVLMaRDpuy9Bbkx0-0Z0ArR--XXOdo2mwNgh6pjSM85HHbTWprX09IB5mUIeYk44ZwBg_c9htvSyqJzwRLzb7KAgOJrAGyGnJrUVWuieQrXjOogZb8GhEjb3psOmj-KzZ1jKFXgJKHuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات سنگین اسرائیل به مواضع حماس در خان یونس
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16174" target="_blank">📅 00:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16173">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2RlbiIPd45TACcfBuMRzhetRLX0T_o3fOFlllUhDCcjusZbF8vwmFNaoq7oPUq2wfeloD7rFAJ57lkj8NZgoeJz0MmTVqh0-wm6gwh49yZ8QjZCVqtJoIXfuiYpx1iENDBlB87jgDrpw4KkGiaOhpaBlV_WUKJmThwKxCTT6YaYEedLdAmoew9ZXtL1ni-XxoLzAm9wYehtkt9TvJNn687z-Fjx-b38qwWjLLTEpUQA_SdBb4pxKbtsrL0bxbTiOd-rUGfcpO719rwcq_sjiViibaErJb2JND13iFQUpYuUvxEDrNDiDNvWLEiacFREkWvFVBzJ7QAP2qv4ScJc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید باور نکنید ولی؛
امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال
۱ میلیون دلار
پاداش طلب کرده بود و فدراسیون پرداخت کرده
۱میلیون دلار هم بازیکنا و سایر اعضا دریافت کردن
اول یک میلیون دلار (۱۷۰ میلیارد تومن) رو گرفت بعد نشست رو نیمکت.
نتیجه: حذف در مرحله گروهی در آسان ترین گروه.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16173" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
