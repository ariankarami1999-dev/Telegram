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
<img src="https://cdn4.telesco.pe/file/oBfpaES4Axe1wKKIuW-qD39uKRjJoMVBkG0crslmv7S20c83jdKWBETEnIWK2w3JTU4ZXWte0Z0YbV5nDvmT8lEBHhN_xfEZQoYey4fXK4Kis3n4iQSF9LOEzpAIL47xoKfY3Wo1_EUAcCMyV7hbJst0bD7S5XU3LftORxUW707zWrnEGXR7Xt4iRrU5q7gq0S6UcHGGDCNO8iFA4osiU9aOPvs-1cNwYe7o3eZOJTmfpJ9jbeeY7VnUmgLSGum4lrF5kwkx_OgQaqSx58FotRqSebp__Hqkj99zxQqoz-Mom4UPgHFQcJcLe6hv38QDRvXOblbjRnl9Moy7OUI2Tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 14:05:40</div>
<hr>

<div class="tg-post" id="msg-15784">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسرائیل هیوم: به ارتش اسرائیل هیچ دستوری مبنی بر عقب‌نشینی داده نشده
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/15784" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15783">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مخالفت شدید چین با اقدامات آمریکا علیه کوبا
وزارت خارجه چین بیان کرد: چین همواره با تحریم‌های یکجانبه غیرقانونی که هیچ پایه و اساسی در قوانین بین‌المللی ندارند، مخالفت کرده است.
پکن از واشنگتن می خواهد تا فوراً به تحریم کوبا و هر نوع اجبار یا فشار پایان دهد. ما حمایت بی‌دریغ خود را از کوبا در جستجوی مسیر توسعه سوسیالیستی متناسب با شرایط ملی آن مجدداً تأیید می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/15783" target="_blank">📅 13:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15782">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">moamelegari-trump(@withyashar).pdf</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/withyashar/15782" target="_blank">📅 13:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15781">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رویترز
:
اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
@withyashar</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/15781" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15780">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سی‌ان‌ان: متحدان ترامپ در کشورهای حاشیه خلیج فارس بیم دارند که توافق او با ایران سرآغاز تحولی فاجعه‌بار باشد
@withyashar</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/withyashar/15780" target="_blank">📅 12:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15779">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/withyashar/15779" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15778">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است. برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت. @withyashar</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/withyashar/15778" target="_blank">📅 12:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15777">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=pzK1MOhGUHWfcNiLKdz2nymKQyBlLwV-bzEdDdKmxGt3wFr8h0ou3DufcuNzj96xuGpTI4H-tfSFMS23STQO6c16reMO7aeYE7jWH2TZuTxgw8WDIsKAUn_G-zYzuy-xJB88B0qGGVKxUomIrPMghICo4DPPXeoGasRu_yRyrad5Dq-WKirGUFB6k167n7wxS4FmW1UZHZ3VmYPIk5h6RZTPJkyw4c4kXNd66OFjB72PKCb84wcpcEsy5TzeRxv8z-m3g6vWn6P8uTs1frzg3IqOmz0BhY1EbVo9_dONHuxIup8tZHV2hBYnHoAJjiq5x7D4XjefFvZYXX-4Owc1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=pzK1MOhGUHWfcNiLKdz2nymKQyBlLwV-bzEdDdKmxGt3wFr8h0ou3DufcuNzj96xuGpTI4H-tfSFMS23STQO6c16reMO7aeYE7jWH2TZuTxgw8WDIsKAUn_G-zYzuy-xJB88B0qGGVKxUomIrPMghICo4DPPXeoGasRu_yRyrad5Dq-WKirGUFB6k167n7wxS4FmW1UZHZ3VmYPIk5h6RZTPJkyw4c4kXNd66OFjB72PKCb84wcpcEsy5TzeRxv8z-m3g6vWn6P8uTs1frzg3IqOmz0BhY1EbVo9_dONHuxIup8tZHV2hBYnHoAJjiq5x7D4XjefFvZYXX-4Owc1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است.
برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت.
@withyashar</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/15777" target="_blank">📅 12:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15776">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/withyashar/15776" target="_blank">📅 12:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15775">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وال استریت ژورنال:
ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
@withyashar</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/15775" target="_blank">📅 11:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15774">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/15774" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15773">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi4HMwKQzSb-aSmAEcK461mJj26FAzYcVv4KatemMzl7TK5RK5jiiqeT-iza2Jt4i581R5JlfdbJF1uVz4VTxSpF5Wz4jWQj9ox1KhPpAG1PF4kgWXuswelUiazyse1ci9dhd7fmbLEpOVXVmnpVEUbvf3RDSiFOs7QIVkqprAIkfdISB-4FeJu9Qd_7l-NgNYnbYMuaQcMMaFU8ykaCbw2u9wsS-7d0UJREzx6OtbRgNW40qdeVPRJWCDciF0VeLIDxi3h0dIDDhTGy-tzoGWLmDCe7seYk6CRLUhADtYZmeHD50WoNjyDV3rN5ByOCJYXMvxZq7MvzsAfvHFVNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد! رئیس جمهور دونالد جی ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/15773" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15772">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2960b1463d.mp4?token=fA8O7E-jqbkdJTzmeLWlSf3JPRHm8n46nikD2O5Lr6HT5Uirpw7eZuukjTNQwXcyS9LEpPYgbT_bI7RQZ_dg6nmMOewTVNyARBVJhrI8gP-qce3aAQ2H3OyUQF80DDb9l4twAwp_IFWHeJQ0eqE9ON_yThHiXx4TkeeGLL513_d4frXKxnJ4vMYc7aEU60hGKq-IHlqsuwsr_ZTBiyH8dcXJG7rrtpq0F9mHsz6KGhsBMnrNTl5Ogyd-w3B0cOB7HWUs_NFwpr0byzrgR-8-3P8xlRrQkkT6wa55OF15urFWW0IW9zgCtNhxWMf6CTmvC-gyIaQaH9gHWFQK0JNcHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2960b1463d.mp4?token=fA8O7E-jqbkdJTzmeLWlSf3JPRHm8n46nikD2O5Lr6HT5Uirpw7eZuukjTNQwXcyS9LEpPYgbT_bI7RQZ_dg6nmMOewTVNyARBVJhrI8gP-qce3aAQ2H3OyUQF80DDb9l4twAwp_IFWHeJQ0eqE9ON_yThHiXx4TkeeGLL513_d4frXKxnJ4vMYc7aEU60hGKq-IHlqsuwsr_ZTBiyH8dcXJG7rrtpq0F9mHsz6KGhsBMnrNTl5Ogyd-w3B0cOB7HWUs_NFwpr0byzrgR-8-3P8xlRrQkkT6wa55OF15urFWW0IW9zgCtNhxWMf6CTmvC-gyIaQaH9gHWFQK0JNcHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در دو جنگ جهانی پیروز شدیم، فاشیسم و ​​کمونیسم را شکست دادیم.
ما باید دوباره این کار را انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/withyashar/15772" target="_blank">📅 11:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15771">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">«قطعنامه اختیارات جنگی ایران» متوقف شد
‏ سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
‏ جمهوری‌خواهان و ترامپ استدلال کرده بودند، تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
‎
@withyashar</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/15771" target="_blank">📅 10:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15770">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ درباره ایران: هفته گذشته، ما یک توافق تاریخی برای پایان دادن به درگیری با ایران امضا کردیم، تنگه هرمز را کاملاً باز کردیم و کاری را انجام دادیم که هیچ رئیس‌جمهوری قبلاً نتوانسته بود انجام دهد.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/15770" target="_blank">📅 10:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15769">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSYvjgdPrITMpTFe059zp_BsYJzx-KOatIQkj5xv6gZwtz0yLxNzZKnrnmii1ro4ktV0Wfwk_gEbPtUDQllrYvtzn3RwOdcxx9QV_QLYBF1J41mKThUUgMyshqYqyNWpl3jz9ma3Awuzh5x14jeX0LEPh7Y8zwqY8qEiwRjz59dEVmnVFoKznPjj6M1sf_JPo5muyMNM-we2Nt_AwCqQnZ4DCuyhzt3cj5KzH3pdp4qTVOmdFZj8u7SVI8d0xzT0Mt9VLOTWDpSTUqvXBJqJsE3os5LYeB7hSFAxfHopJ0WZQ1kR5Yev8ux86RUIXbHTfI4gnZIyIsgALN60OuS8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌ تروث : دو زلزله بزرگ که به تازگی مردم بزرگ ونزوئلا را لرزاندند، هر دو در مقیاس وسیع بوده و تعداد زیادی کشته به جا گذاشته‌اند. ایالات متحده آماده، مایل و قادر به کمک است! من به تمام نهادهای دولتی دستور داده‌ام که برای اقدام سریع آماده باشند. ما در کنار دوستان جدید و بزرگ خود خواهیم بود. گزارش‌های اولیه خوب نیستند.
@withyashar</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/15769" target="_blank">📅 09:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15768">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هشدار سونامی در ونزوئلا، بعد از زمین‌لرزه۷ ریشتری، ویدیو منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزه شدید نشان می‌دهد. @withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/15768" target="_blank">📅 02:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15767">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061be29e3.mp4?token=St5-TYbh84rxZG8672_66A-btFe_jd-K12jSkaRS08a1-Amt2oM2eA7WmKQuaqUkMd2za-Aufp3wV29akOmdHkteoGD2-SDuFpnrtegQ1aM4yQG5rZ3mcMJGIFJAruS4o0HicRHlzPxa7VNc9F7lAazJk8oCEyIrEsOBeDrp6VuQvXaT7hiGjS2cw8GlR22Mmdk4m9dhM-7TfqZ7zinKJEJAmu9gI_vYNmSyCUTLscKbsJgurDlOIKFbDnPZ6rCEtEJtNGp1meJYhhoGsPcnvvXAFXgVcQCz0cMTrwMScgNV3HNCQpZjRe1wnVrG5MpS7y7VjgRa1-pXQoYruDs3Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061be29e3.mp4?token=St5-TYbh84rxZG8672_66A-btFe_jd-K12jSkaRS08a1-Amt2oM2eA7WmKQuaqUkMd2za-Aufp3wV29akOmdHkteoGD2-SDuFpnrtegQ1aM4yQG5rZ3mcMJGIFJAruS4o0HicRHlzPxa7VNc9F7lAazJk8oCEyIrEsOBeDrp6VuQvXaT7hiGjS2cw8GlR22Mmdk4m9dhM-7TfqZ7zinKJEJAmu9gI_vYNmSyCUTLscKbsJgurDlOIKFbDnPZ6rCEtEJtNGp1meJYhhoGsPcnvvXAFXgVcQCz0cMTrwMScgNV3HNCQpZjRe1wnVrG5MpS7y7VjgRa1-pXQoYruDs3Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هشدار سونامی در ونزوئلا، بعد از زمین‌لرزه۷ ریشتری، ویدیو منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزه شدید نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15767" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15766">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده شدن مردم منتشر کرده است.
‏گفته می‌شود بابا وانگا، پیشگوی مشهور بلغاری هم، وقوع یک تهاجم فضایی در جریان یک رویداد بزرگ ورزشی را پیش‌بینی کرده بود.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15766" target="_blank">📅 01:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15765">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">طارمی و الهویی دوباره در مرز آمریکا «معطل شدند»
ایرنا از معطلی کاروان تیم ملی پس از ورود به خاک آمریکا از مرز مکزیک خبر داده و نوشته مانند دو سفر قبلی، روند عبور مهدی طارمی و سعید الهویی، توسط ماموران مرزبانی طول کشیده است.
دیدار با مصر در سیاتل (ایالت واشنگتن) که مرز شمال غربی آمریکا با کانادا است برگزار می‌شود.
تیم ملی برای صعود مستقیم به دور حذفی باید مصر را شکست دهد اما با تساوی مقابل این تیم هم می‌تواند به صعود به عنوان تیم دوم یا سوم باقی امیدوار بماند.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/15765" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15764">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZp_qDKZme7YPra3wyz_cz8ufqVYdEg83lwE7dB0pdH-IVS_LCxMQxfH9-qKcS2kkB670beaqBuQd_ZHeVg2uWVX9_ZS5GJcqOTiJ_dAK_cC0t9y2GbMGipe5udn0pK6n2aURCGdKHWk0AGyuPtJDVT4sPMG3zZQIFECFvbjscaGSFiOPE0rEi3OtO0ri2tj4z7Y1uycIJOT3k8ekQ4xSE9b1lprzSFxlzyCYGE0DC8Vt6FwBPHzAhMsHU0f7L1-BRze-vOW_RDJ1AqnOcf7BJqrN_65aFuYLqcsMXT1wI-i2ZFnLRk9duS1zAbYPx5Fs44mAZpa7P7JreY1eEcVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر «آبراهام لینکلن (CVN-72)» نیروی دریایی آمریکا در تصاویر ماهواره‌ای در فاصله ۱۴۰+ کیلومتری بندر چابهار ایران مشاهده شد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15764" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15763">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فاکس‌نیوز : ترامپ به دنبال تأمین ۶۷۲ میلیون دلار برای حذف مواد هسته‌ای ایرانی است
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/15763" target="_blank">📅 23:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15762">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزارت امور خارجه ایران: واشینگتن باید از تفسیرهای متناقض با مفاد یادداشت تفاهم بپرهیزد.
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/15762" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15761">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارشهای زیاددددد از صدای انفجار دوباره  در بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15761" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15760">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/15760" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15759">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جنجال در ایتالیا پس از افشاگری درباره همکاری پنهان در جنگ علیه ایران پولیتیکو: افشاگری مارک روته، دبیر کل ناتو در خصوص استفاده آمریکا از پایگاه‌های ایتالیا در جنگ علیه ایران واکنش تند گوئیدو کروستو، وزیر دفاع ایتالیا را در پی داشت.  گوئیدو کروستو گفت: تنها…</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15759" target="_blank">📅 22:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15758">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جنجال در ایتالیا پس از افشاگری درباره همکاری پنهان در جنگ علیه ایران
پولیتیکو: افشاگری مارک روته، دبیر کل ناتو در خصوص استفاده آمریکا از پایگاه‌های ایتالیا در جنگ علیه ایران واکنش تند گوئیدو کروستو، وزیر دفاع ایتالیا را در پی داشت.
گوئیدو کروستو گفت: تنها پروازهای مطابق با معاهدات مجاز بوده‌اند؛ پیام روته کاملا اشتباه است.
احزاب مخالف در ایتالیا از این توضیحات قانع نشدند. آنجلو بونلی، نماینده سبزها گفت: ملونی به ایتالیایی‌ها و پارلمان دروغ گفت. ملونی باید فورا روشن کند چه اتفاقی افتاده و به پارلمان گزارش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15758" target="_blank">📅 22:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15757">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فردا فرمانده ستاد فرماندهی مرکزی ایالات متحده(سنتکام( به اسرائیل خواهد رسید
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/15757" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15756">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نعیم قاسم ، رهبر حزب الله ، اعتراف کرد که یک گروهک تروریستی نمی تواند ارتش اسرائیل را در رویارویی مستقیم نظامی شکست دهد
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15756" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15755">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/15755" target="_blank">📅 22:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15754">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتَهمتَن</strong></div>
<div class="tg-text">داش تو ویست گفتی بوست کنیم؟</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/15754" target="_blank">📅 22:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15753">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/15753" target="_blank">📅 22:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15752">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/15752" target="_blank">📅 22:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15751">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAdam Fazaei</strong></div>
<div class="tg-text">یاشار جان ایموجی فقط جاوید شاه دیگه نیست ؟</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/15751" target="_blank">📅 22:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15750">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromf</strong></div>
<div class="tg-text">سلام
داداش
بجز اخبار یه چیزی هم خودت بگو
مرسی
دلتنگ صدات شدیم
😂</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/15750" target="_blank">📅 22:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15749">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بندر عباس صدای ذرت مکزیکی‌ میاد
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/15749" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15748">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وال‌استریت ژورنال؛ ترامپ اقدامات جسورانه علیه ایران انجام داد که هیچ رئیس‌جمهوری پیش از او جرأت انجامشان را نداشت، اما در نهایت به همان نقطه‌ای رسید که دیگران هم در آن قرار داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/15748" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15747">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال 14 اسرائیل:اسرائیل در حال آماده‌سازی برای احتمال حمله دوباره به حوثی‌های یمن است
@withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/15747" target="_blank">📅 22:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15746">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78282e8e68.mp4?token=DwNgZU_wANU-Mzm191tR8r9qT60EvfqbRQA5JTQqTHze3k00y5g-beRHhcJd1R-JrUOjZHWuk0HRqee8tw6As_Fp_zAmlF87baRwKNFeMvhlrU7Z-hkO5xky3EWlDt1u6yc1yl6--MzHpjtBgOlmKUe3zLKzYTcD-Uby2gXFLtQmS7HIYd57wlWRMJDfQsvrgD2qx3pEQWEGrMUDyvljGftxfnLwuKZLkbopPV3XtE8PQTbSpesP-_OYsOjQWLsOlEFxMabRncpzGAfBfSD14tEMJOyPvcUjMeO32nvPvzuGLVPBfiitrLGgo2TFu8vhRJGYEmI9T-dHx2ka_rZG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78282e8e68.mp4?token=DwNgZU_wANU-Mzm191tR8r9qT60EvfqbRQA5JTQqTHze3k00y5g-beRHhcJd1R-JrUOjZHWuk0HRqee8tw6As_Fp_zAmlF87baRwKNFeMvhlrU7Z-hkO5xky3EWlDt1u6yc1yl6--MzHpjtBgOlmKUe3zLKzYTcD-Uby2gXFLtQmS7HIYd57wlWRMJDfQsvrgD2qx3pEQWEGrMUDyvljGftxfnLwuKZLkbopPV3XtE8PQTbSpesP-_OYsOjQWLsOlEFxMabRncpzGAfBfSD14tEMJOyPvcUjMeO32nvPvzuGLVPBfiitrLGgo2TFu8vhRJGYEmI9T-dHx2ka_rZG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه کان اسرائیل : آمریکایی‌ها در حال ترک فرودگاه بن‌گوریون هستند
ایالات متحده ۲۸ فروند هواپیمای سوخت‌رسان را تخلیه کرده و اسرائیل نیز به‌دلیل نگرانی از اختلال در پروازهای غیرنظامی در طول تابستان، اسرائیل خواستار تخلیه حدود ۲۰ هواپیمای دیگر شده است.
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/15746" target="_blank">📅 21:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15745">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام ندهید. در غیر این صورت مسئولیت با شماست و توسط حرص و طمع خود شما انجام گرفته. به این مسئله دقت کنید و
فقط از تحلیلها و مطالب آموزشی افراد استفاده کنید
. هیچ پکج یا هیچ پرداختی به هیچ بی ناموسی انجام ندهید.
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
از توجه شما به این مطلب سپاسگزارم، یاشار</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/15745" target="_blank">📅 21:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15744">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">1$ / Tether = 167,000 Toman
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/15744" target="_blank">📅 21:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15743">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر انرژی آمریکا مدعی شد: بازگشت جریان نفت به حالت عادی به دلیل مین‌های ایران به تأخیر افتاده است
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/15743" target="_blank">📅 21:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15742">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یدیعوت آحارونوت: فرمانده سنتکام به زودی وارد اسرائیل می‌شود و با وزیر جنگ و رئیس ستاد ارتش دیدار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/15742" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15741">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c79bdeee0.mp4?token=bxHQK5DAR4LA6fieuGbIy1Xgswsg-Ieyqj-b35JY0d-523DkxMRnQ1KTVoNWvZaRmc2eJ336Lo9x3ShDd9q-S6HmLdo_g8giGeMiPmgtRRHW9EDZEsNWTXWgCPTU16I4R5TFpoZDb-8K0aNxZkWEZj3EZVXbPbuU7u5eRCtm6O2GXJth4pcNE_st4eUog_sWtWbOPiQ3RtR5UXbcoHuj34Q-s9EMmnQrons0BBHEGTgSiXh0Dozatbzl44nIzGKR7twkC7iaeBC5vFYrA4F7vFc3E7ZQ8m68pwbo2sHtG1AkWJKsiFAcCsQ-0Hq56BI30xVgJWi_FWTa0QabVsVV0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c79bdeee0.mp4?token=bxHQK5DAR4LA6fieuGbIy1Xgswsg-Ieyqj-b35JY0d-523DkxMRnQ1KTVoNWvZaRmc2eJ336Lo9x3ShDd9q-S6HmLdo_g8giGeMiPmgtRRHW9EDZEsNWTXWgCPTU16I4R5TFpoZDb-8K0aNxZkWEZj3EZVXbPbuU7u5eRCtm6O2GXJth4pcNE_st4eUog_sWtWbOPiQ3RtR5UXbcoHuj34Q-s9EMmnQrons0BBHEGTgSiXh0Dozatbzl44nIzGKR7twkC7iaeBC5vFYrA4F7vFc3E7ZQ8m68pwbo2sHtG1AkWJKsiFAcCsQ-0Hq56BI30xVgJWi_FWTa0QabVsVV0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگ داره خیلی خوب پیش میره. همون‌طور که می‌دونید، ما داریم با اختلاف زیاد می‌بریم. ایرانم داره امتیازهای خیلی بزرگی میده. ببینیم آخرش چی میشه، ولی واقعاً اوضاع خیلی، خیلی، خیلی قدرتمند پیش رفته.
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/15741" target="_blank">📅 21:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15740">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روزنامه تلگراف به‌نقل از منابع نزدیک به ترامپ مدعی شد که رئیس‌جمهور آمریکا احتمالاً
پس از انتخابات میان‌دوره‌ای کنگره، توافق فعلی با ایران را کنار می‌گذارد و به‌دنبال توافقی جدید خواهد رفت.
به‌گفته این منابع، ترامپ برای مهار فشارهای اقتصادی و حفظ موقعیت جمهوری‌خواهان در انتخابات، به توافق کنونی با ایران نیاز داشته است , بازگشایی تنگه هرمز و دستیابی به تفاهم با تهران، نگرانی بخشی از جمهوری‌خواهان را کاهش داده است.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/15740" target="_blank">📅 21:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15739">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آکسیوس: اولین دور مذاکرات اسرائیل و لبنان در واشنگتن بدون نتیجه پایان یافت و گفت‌وگوها در فضایی به شدت پرتنش برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/15739" target="_blank">📅 20:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15738">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:ایران تاکنون 500 میلیون دلار مواد غذایی آمریکایی خریداری کرده است.   @withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/15738" target="_blank">📅 20:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15737">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ:ایران تاکنون 500 میلیون دلار مواد غذایی آمریکایی خریداری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/15737" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15736">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxbFYJAmTj0YtJfCvjrCMSzwVq5eNOwkBup4T7j7XDT9MEFeXhUj2nrqdpWVVjsxYV3T79LrFKbWgkgqeT_ujfL_0FZdn1aWkr75U49xK6ovzCkO9NK-W_znLOtpnNFe1-mPL7URVCJ4HLziQttp5H7DkJuIRdI791eqg4nF1WnIRU0S8y-3ZssEUHRfk7wFXQo40a9BPZT6wgCwih2_x2mut9j54Q1hM01rFJMATTaUOCQUunvTvWMOyuIlx4egEGUy43UQY10Nk8xmMBDhWHO3_JFWgEsybKaKSTDTefaUuTTSiuCjtUMXxXWxmgQycqjb1XwCAGJGdKc-5ntlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیت‌کوین به زیر ۶۰٬۰۰۰ دلار سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/15736" target="_blank">📅 20:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15735">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مرحله دوم مذاکرات فنی ایران و آمریکا ۸ تیر برگزار می‌شود
وزیر خارجه آمریکا دقایقی پیش در اظهاراتی گفت که مذاکرات فنی ایران و آمریکا، روز ۲۹ ژوئن / ۸ تیر در سوئیس برگزار می‌شود. پیش از این نیز وزارت خارجه پاکستان اعلام کرد که مذاکرات ایران و آمریکا هفته آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/15735" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15734">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58bddbc88.mp4?token=TmWRyfhMrZKZjh_Apn7Ip7wX9PCJrrUUA58PvvvXXMZwKkpZM-14NOkcL5IfIFVuQF5jf0vhXLcDXcEK7X-Kc7Wi5G07VHZ-LIiPojJHmBB0B8CNyfBf09sH4WxVUCKVRbV_9El36L1wlh_liGpTDss0Jht6LYXwFTTfve1eMiPSWERvr_dEbQO8gQh154GJBxkr0rVPfd8qOfPmTG-Vxx7b7QKGlhaNmRzv2Qm4ggcJI9Y14C4Qfrda1rWMAcNe3rbS60q2Tp4VmzZNKrX0CqaW_5TVRGceMucjeiFv5N1weCFl-bg0NZv476R2qUIeMEY69r6BohMgPUrXwMCLOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58bddbc88.mp4?token=TmWRyfhMrZKZjh_Apn7Ip7wX9PCJrrUUA58PvvvXXMZwKkpZM-14NOkcL5IfIFVuQF5jf0vhXLcDXcEK7X-Kc7Wi5G07VHZ-LIiPojJHmBB0B8CNyfBf09sH4WxVUCKVRbV_9El36L1wlh_liGpTDss0Jht6LYXwFTTfve1eMiPSWERvr_dEbQO8gQh154GJBxkr0rVPfd8qOfPmTG-Vxx7b7QKGlhaNmRzv2Qm4ggcJI9Y14C4Qfrda1rWMAcNe3rbS60q2Tp4VmzZNKrX0CqaW_5TVRGceMucjeiFv5N1weCFl-bg0NZv476R2qUIeMEY69r6BohMgPUrXwMCLOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : من بیشتر دوران بزرگسالی‌ام را به جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای اختصاص دادم.
آماده نبودم اجازه دهم زنجیره‌ای از هزاران سال تاریخ یهودی به خاطر دستیابی این آیات‌الله‌ها به سلاح‌های هسته‌ای شکسته شود.
به همین دلیل بیشتر دوران بزرگسالی‌ام را به این هدف اختصاص دادم همچنین به عنوان نخست‌وزیر
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/15734" target="_blank">📅 19:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15733">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ارتش اسرائیل: یکی دیگر از تروریست‌های حماس که در قتل عام ۷ اکتبر به اسرائیل نفوذ کرده بود، از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/15733" target="_blank">📅 19:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15732">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال 13 اسرائیل:
نتانیاهو امشب یک جلسه امنیتی درباره لبنان و سوریه برگزار خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15732" target="_blank">📅 19:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو: از ترامپ اجازه‌ای برای حمله به ایران درخواست نکرده‌ام بلکه تنها آن را به او ابلاغ کردم.
ماموریت ما در لبنان هنوز پایان نیافته است.
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/15731" target="_blank">📅 18:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/832f75f201.mp4?token=e0avm56Og5XrTszOxtxV3Xdz0ccFEC4hugfFnZWz5adTVm1ppNqw79qi-VFjJQwuN_bXs9KaxhqgVOJste0nbIpnP9eFZUPU-fmBCXc1MunfZU2wK71Ns7zKI3WiHsBR7N7LB2rjRKINkoSRUxjDEjKm7ll4cLqq25MWwT-mtKTtrynlWx7ATOlka390MtpTFVwsOME6UB9dCQEKjLWQ_P_iH-ANNfmqb0BZSxMPJpVNJLI6bxTGr39QpmizC3Blox4QhYLXr_93UR0CPMtXrpy3HxjObaG0r6czL8rC5hOs96w4EpCuANn7-bOqQ9JGsGYGH1xelpLxzfq9CemUnD6WgoSm3Ia37Qxri3x9yh0xByE2tnDXaQg_wl9rlIElV8NrfSR3B-U3CJv_b9T7PBwoFmAO9Pb5rvEJBsvc6TsOlIiXGwGQHGmCPBDXnsgfZ7sJ1CYBN59yZHGYV9J883Ou650QStHMUdxwfYHdMat0U0BXnLyjvb6NWcDPmfDZwC-wIa8JliMxxGRummuSxQpxYDffI2DsCzHhjPmifHBuiifX_CYjKxxjh99LSI6dYyhXU8mg8d6OBuy5PHNyEwsjm24wDajE_rzivbL2Ol_DNcGubsSBMYOqZ48CUyFBbgE9fn8KlspK3NL0vqPCxtwFvXCqIEht-MBEfOZARs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/832f75f201.mp4?token=e0avm56Og5XrTszOxtxV3Xdz0ccFEC4hugfFnZWz5adTVm1ppNqw79qi-VFjJQwuN_bXs9KaxhqgVOJste0nbIpnP9eFZUPU-fmBCXc1MunfZU2wK71Ns7zKI3WiHsBR7N7LB2rjRKINkoSRUxjDEjKm7ll4cLqq25MWwT-mtKTtrynlWx7ATOlka390MtpTFVwsOME6UB9dCQEKjLWQ_P_iH-ANNfmqb0BZSxMPJpVNJLI6bxTGr39QpmizC3Blox4QhYLXr_93UR0CPMtXrpy3HxjObaG0r6czL8rC5hOs96w4EpCuANn7-bOqQ9JGsGYGH1xelpLxzfq9CemUnD6WgoSm3Ia37Qxri3x9yh0xByE2tnDXaQg_wl9rlIElV8NrfSR3B-U3CJv_b9T7PBwoFmAO9Pb5rvEJBsvc6TsOlIiXGwGQHGmCPBDXnsgfZ7sJ1CYBN59yZHGYV9J883Ou650QStHMUdxwfYHdMat0U0BXnLyjvb6NWcDPmfDZwC-wIa8JliMxxGRummuSxQpxYDffI2DsCzHhjPmifHBuiifX_CYjKxxjh99LSI6dYyhXU8mg8d6OBuy5PHNyEwsjm24wDajE_rzivbL2Ol_DNcGubsSBMYOqZ48CUyFBbgE9fn8KlspK3NL0vqPCxtwFvXCqIEht-MBEfOZARs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، بسنت : سلطه دلار خیلی مهمه
همه کارهایی که ترامپ داره انجام می‌ده، دلار رو دوباره محور تجارت جهانی می‌کنه
تو ونزوئلا و حتی مذاکرات با ایران هم می‌بینیم که معاملات قراره با دلار انجام بشه
درکل، همه این اقدامات جایگاه دلار رو دوباره تقویت می‌کنه
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/15730" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ به فاکس‌نیوز اعلام کرد که قرار است به بازرسان اجازه داده شود تا مکان‌هایی که اورانیوم ایران در آنجا نگهداری می‌شود، بازدید کنند. از سوی دیگر، ایران قصد دارد در اولویت اول، کالاهای آمریکایی به ارزش حدود ۵۰۰ میلیون دلار خریداری نماید. هیچ عجله‌ای برای ورود بازرسان وجود ندارد و تیم آمریکایی قرار است همراه با بازرسان آژانس برای یافتن اورانیوم غنی‌شده اعزام شوند.
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/15729" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
ترامپ: هیچ عجله‌ای برای دسترسی به این مواد وجود ندارد، زیرا پس از عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/15728" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15727">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ در تروث : شهردار ممدانی با حمایت سه کمونیست تمام‌عیار به پیروزی رسید و رسانه‌های جعلی هم با سروصدای زیاد و به‌صورت یکپارچه برایش کف زدند. تبریک آقای شهردار!
من دیشب ۱۶ برد از ۱۶ داشتم و به انتخاب میهن‌پرستان فوق‌العاده آمریکایی کمک کردم، اما رسانه‌ها حتی یک کلمه هم درباره‌اش نمی‌گویند.
در دو سال گذشته، حمایت و تأیید من باعث ۲۵۹ پیروزی در انتخابات مقدماتی شده و تقریباً هیچ شکستی نداشته است، با این حال هیچ توجهی از سوی رسانه‌ها دریافت نکرده‌ام!
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/15727" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6227a74ce9.mp4?token=YqOobuRMV23SPN090bL65JqnkT0rV6scDFd18jpWnt1BNrGzDYJ2BwfxcutR3BCdnXmFuBtC9NJZwPdb_7J39Ayq4TsZETukPSS82Hi4EOu3BWyrs7eFshVkR5VEzu4ipU8AiT8hl4mfOY6hnBFNGHwywzWnP5EGiPnvYBCQXwMhLc_KOuL0WYjTDUF3JGjIwXuVB3eO_et1DHpOzxzMgXqciaKz83y2uMRqVvkX2cANFc1Xr4sOp2zAp45eqlGWACiRwmFYekDfx8jWmtSlIb14EUgWbYmdcvHoDqZiM3FfJt3gUXuiGxM-m3JBtg0P10axDQdsWrCbEa5vljvnwRQsgnMx_BtSvUbreRXRt6pxGtMKN4hvPhI2T0yHYvyxa9vWU7-vrJwj2eMo7r5U8EeDT54zoM4mViLP1i_NRqo8O-OIALplaPTQBbd7HMRzyJqcb-e5q_yrS4GUQA5u4qALNh-h4v9BOqq4pDw9nQ9ogK1RPKXCcmunHisqiZlwmu8dVGMVYKWhV7wNkTj6MwGPjkDx05r0gjrzsAje3cFm-D69JGhaecrIvCduiLmmRdrg6cTwVkOwXcsqq70qwkRC_AB_IduNVbX1walTUpwj9k2otkjGQV9y4F2icfPs3_AzPED3HfTGsNnME4m0wpweAd2dEPZ1WBdLxUIlLtE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6227a74ce9.mp4?token=YqOobuRMV23SPN090bL65JqnkT0rV6scDFd18jpWnt1BNrGzDYJ2BwfxcutR3BCdnXmFuBtC9NJZwPdb_7J39Ayq4TsZETukPSS82Hi4EOu3BWyrs7eFshVkR5VEzu4ipU8AiT8hl4mfOY6hnBFNGHwywzWnP5EGiPnvYBCQXwMhLc_KOuL0WYjTDUF3JGjIwXuVB3eO_et1DHpOzxzMgXqciaKz83y2uMRqVvkX2cANFc1Xr4sOp2zAp45eqlGWACiRwmFYekDfx8jWmtSlIb14EUgWbYmdcvHoDqZiM3FfJt3gUXuiGxM-m3JBtg0P10axDQdsWrCbEa5vljvnwRQsgnMx_BtSvUbreRXRt6pxGtMKN4hvPhI2T0yHYvyxa9vWU7-vrJwj2eMo7r5U8EeDT54zoM4mViLP1i_NRqo8O-OIALplaPTQBbd7HMRzyJqcb-e5q_yrS4GUQA5u4qALNh-h4v9BOqq4pDw9nQ9ogK1RPKXCcmunHisqiZlwmu8dVGMVYKWhV7wNkTj6MwGPjkDx05r0gjrzsAje3cFm-D69JGhaecrIvCduiLmmRdrg6cTwVkOwXcsqq70qwkRC_AB_IduNVbX1walTUpwj9k2otkjGQV9y4F2icfPs3_AzPED3HfTGsNnME4m0wpweAd2dEPZ1WBdLxUIlLtE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشد دارایی ونس و هگس در طی سالها
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/15726" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13a4e4286.mp4?token=Wk9OqOrP-OKDbdH-YGR4hxJS54m6ihlE3YzJKcFnfKnGygK8shd-Rl4vYhNjGoskT8i2Ch75pP8OfMTcFOip-JKcYQvMXOlo3H-tdyI4j04VGdDVEcJGTBFpAbGX-Fer4BpEtu_i7AUxzaJNU7WNs5_VBWvA-9QPauusbROvp0Y7akTPKfw3pJoXesLtudzLSPvSEUKGTBGrkn4dTt6F3zIAH4zKSqBV8K1QWq9-EBYwy5fF4cba4ackjPD8-2JT2_cbNJAdhdyFGou5J6vcBGnEqzyjelUUlfPsyECv_wbw4tkXRkb9hc6jif7e8iNOXYRwwSiQ2e_pqWqqn8xUUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13a4e4286.mp4?token=Wk9OqOrP-OKDbdH-YGR4hxJS54m6ihlE3YzJKcFnfKnGygK8shd-Rl4vYhNjGoskT8i2Ch75pP8OfMTcFOip-JKcYQvMXOlo3H-tdyI4j04VGdDVEcJGTBFpAbGX-Fer4BpEtu_i7AUxzaJNU7WNs5_VBWvA-9QPauusbROvp0Y7akTPKfw3pJoXesLtudzLSPvSEUKGTBGrkn4dTt6F3zIAH4zKSqBV8K1QWq9-EBYwy5fF4cba4ackjPD8-2JT2_cbNJAdhdyFGou5J6vcBGnEqzyjelUUlfPsyECv_wbw4tkXRkb9hc6jif7e8iNOXYRwwSiQ2e_pqWqqn8xUUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری دولتی لبنان گزارش داد:
یک پهپاد اسرائیلی خودرویی را در نزدیکی شهرک کفررمان در جنوب لبنان هدف قرار داد و دو نفر کشته شدند.
پیش‌تر نیز سخنگوی ارتش اسرائیل اعلام کرد نیروهای ارتش دو عضو مسلح حزب‌الله را که تهدیدی برای نیروهای اسرائیلی در منطقه علی‌الطاهر در جنوب لبنان بودند، هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/15725" target="_blank">📅 17:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قیمت اونس طلا به زیر ۴ هزار دلار رسید؛ آیا سقوط ۱۵۰۰ دلاری از اوج تاریخی ادامه خواهد داشت؟
قیمت نقدی طلا روز چهارشنبه ۲۴ ژوئن (سوم تیر ۱۴۰۵) تحت تاثیر رشد ارزش دلار آمریکا و افزایش انتظارات مبنی بر تداوم بالا ماندن نرخ‌های بهره در این کشور، برای نخستین بار از ماه نوامبر ۲۰۲۵ میلادی، از مرز روانی ۴ هزار دلار در هر اونس پایین‌تر آمد.
تقویت ارزش دلار آمریکا باعث شد تا خرید شمش طلا که بر مبنای دلار قیمت‌گذاری می‌شود، برای دارندگان سایر ارزها گران‌تر تمام شود.
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/15724" target="_blank">📅 17:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5b8c6375.mp4?token=V_utoAAJXRR8BcN-nUF8fMzXpm5mhO0DgTyTd0FC7In5ng7eeKRQyePcJ-nlnOkOdxvZDSfcJnlGfnbUzams-HvnmHtw2TqAd3ZDbDGMGNZED6hpGCYTEPGO0y0JNlI4lwA_muETQdKjw1ZaaRuCawZMTEmq9dFEzRWeHbKm0l3DyvsPPjViaw4zhbfeHgpWu0lhv1h56TErNL1i1fPP_CvriAwDCxArpcuD9ask4D3LnPFSRwm87K9QvQwnoGMkyBmPZMNviwzFZiZ0HAC2klwhGnQRP1aodR8Tb8bGBtev0cbj5p6xdUqJOufXwr8UI4gomtOYfV_PcBvno1wvDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5b8c6375.mp4?token=V_utoAAJXRR8BcN-nUF8fMzXpm5mhO0DgTyTd0FC7In5ng7eeKRQyePcJ-nlnOkOdxvZDSfcJnlGfnbUzams-HvnmHtw2TqAd3ZDbDGMGNZED6hpGCYTEPGO0y0JNlI4lwA_muETQdKjw1ZaaRuCawZMTEmq9dFEzRWeHbKm0l3DyvsPPjViaw4zhbfeHgpWu0lhv1h56TErNL1i1fPP_CvriAwDCxArpcuD9ask4D3LnPFSRwm87K9QvQwnoGMkyBmPZMNviwzFZiZ0HAC2klwhGnQRP1aodR8Tb8bGBtev0cbj5p6xdUqJOufXwr8UI4gomtOYfV_PcBvno1wvDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، برای دومین مرحله از تور خاورمیانه خود به کویت رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/15723" target="_blank">📅 17:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15722">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سنتکام: «نیروهای فرماندهی مرکزی ایالات متحده در تاریخ ۱۹ ژوئن یک حمله هوایی در شمال‌غرب سوریه انجام دادند که به کشته شدن یکی از رهبران ارشد داعش منجر شد.
در این حمله دقیق، علی حسین العلوی کشته شد. این عملیات بخشی از تلاش‌های مستمر آمریکا برای مختل کردن و از بین بردن عناصر تروریستی است که در پی حمله به شهروندان آمریکایی در خارج از کشور یا خاک ایالات متحده هستند.
نیروهای سنتکام همچنان در همکاری با شرکای منطقه‌ای به عملیات خود ادامه می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/15722" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15721">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا به سی‌ان‌بی‌سی:
هر پولی که رژیم تهران دریافت کند، متعلق به ایرانی‌هاست.
نسبت بسیار زیادی از پول برای خرید غذا و داروی آمریکایی استفاده خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/15721" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15720">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فاکس‌نیوز گزارش میدهد : پرزیدنت ترامپ روز شلوغی را در واشنگتن دی سی آغاز می‌کند و آماده می‌شود تا به کنگره برود، جایی که طبق گزارش‌ها قرار است با جمهوری‌خواهان سنا در مورد قانون متوقف شده «نجات آمریکا» ملاقات کند.
در طول اقامتش در کنگره، قرار است قانون «جاده قرن بیست و یکم به سوی مسکن» را نیز امضا کند.
همه این اتفاقات پیش از جلسه کاخ سفید بین ترامپ و مارک روته، دبیرکل ناتو، در اواخر امروز رخ می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/15720" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15719">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOkTvpOmW2yfCSJ4Vu8u-2t6Rl2WN_Fmov5JtC-kwdKxLiZra_b3zY6DGG9wnS2vOYl_Rag91lXVvUEk4-Guzx2Xm6Dj4m-7R2GGTTgteJaoX2TnfI2wKlbBAGCnim9Kt8za4GoEHibaYYEVUtOYGjpQS1QIpKGeIVWrUUok-APOZ1fCC-8MhjjQRN4TAN-mHgbC1cSzI5tupC1ynuhSVQyGfNHgRvoRBbfykwSa4xlbgaFf_mIRtlnU4w14nUHXJkUPEY5ZN-3yeTtiaJRh1e8vpvWUyzKDroAFfHIAf1F2z4He4R0USRqbEGUujqsfsjB6YRBom4hi0JsvzZh5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث : «ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دردسرساز رسانه‌های جعلی، هیچ‌گونه عوارض، هزینه بیمه یا هیچ نوع هزینه دیگری از کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌کند. اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت.
همچنین، هیچ پولی از سوی آمریکا به ایران پرداخت نشده و هیچ بخشی از دارایی‌های ایران نیز مستقیماً در اختیار این کشور قرار نگرفته است. ما بخشی از دارایی‌های ایران را که همچنان کاملاً تحت کنترل ماست، برای پرداخت به کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا از آن برای خرید ذرت، گندم، سویا و سایر محصولات استفاده شود.
ایران به‌شدت به مواد غذایی نیاز دارد و ما این اقلام را منحصراً از ایالات متحده برای آن‌ها تأمین خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم.»
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15719" target="_blank">📅 15:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15718">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP1ViGyz6l6qKvp-TNI4eIL6SBCa9OvaeqB5uyOE8YdO6b7JqB2eRH005mi_0y9ffF9tznooslrvPRK6wZmZrGSGyBqaTzfM4mFWsu139MSDQTq7yqTXTClxsXpQygT49On2hRdKFllyJi1N3v5FgGaEOXzwPiWSlVHXes6vNXkARuKllVWqUUEJxJ_AozzKiGCqeYCmH4-tkQVceXNw2j3vBXHlnih3KXTblOC8m6_Ec_dOK0AL38aiFGAUoW7SD0hMb1vxHN0NGacHPLbpzf5C9zdDVGV9Jo7jAH6U4HBbqPZjmkNdw4733No0NKpHQcEh9Ot9P3FAQDyrw3_cWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن پالیسی:
توافق ایران زمینه درگیری‌های بیشتری را فراهم می‌کند
!
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/15718" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15717">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">با اعلام راکستار،قیمت بازی GTA6 مشخص شد.
نسخه Standard:
80 دلار، معادل 12 میلیون تومن.
نسخه Ultimate Edition:
100 دلار، معادل 16 میلیون تومن.
@withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/15717" target="_blank">📅 14:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15716">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حسین پاک، خبرنگار مستقر در لبنان: در نقض آتش‌بس دیروز اسرائیل در لبنان، ۳ شهید داشته‌ایم
دشمن درحال برنامه‌ریزی بلندمت جهت اشغال منطقه طیبه است.
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/15716" target="_blank">📅 14:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15715">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قالیباف در باکو: تفاهم‌نامه امضاشده برای پایان جنگ «اعلام شکست آمریکا» است
او در بیستمین کنفرانس اتحادیه مجالس کشورهای عضو سازمان همکاری اسلامی (PUIC) در باکو گفت: «تفاهم‌نامه ‌اسلام‌آباد نه نتیجه فشارو اجبار، بلکه حاصل مقاومت و اقتدار ملت شجاع ایران بود... یادداشت تفاهم اسلام‌آباد تبدیل به اعلامیه شکست آمریکا شد.»
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/15715" target="_blank">📅 14:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15714">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">غضنفری، نماینده تهران : امیدواریم قالیباف سر عقل بیاد و مجلس رو باز کنه.
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/15714" target="_blank">📅 14:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15713">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">معاون وزیرخارجه خطاب به ترامپ:
نمی توانید با هیاهوی رسانه ای، سیاست "راه بینداز و جا بینداز" را پیش ببرید.
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/15713" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15712">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ee6905e4.mp4?token=QsahxeSLi92VY3Ua4DCrjiuzC5xZskETHiHscS8gwdr6QrcnMA4XOkcP9xDbUDCfXSWeDfKIsr2tipdMdmFV9WY4QelY_sWy1oEF6PVfGmXd78wVO-m1OXVglR7h96ZpQKPjG4rCFX-lkBjFVX7C50z77BbreN0ByuukGFdbVVQ9btIKCJSKtYJZs7q6rlOtLiTa9P9Io5pvmiBdD0CfexStV-xiNZjgb-WnkVzhX7FRMXo1ybWBU5oL6kY61KDcJZLDVdiQu9N6zhakI1ZyJKZWSoNB1L5JVKsJZWQaBAhjCkEUTU2nSVrEZbJQsrlRIwxZdJMf9naGM9K145zKVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ee6905e4.mp4?token=QsahxeSLi92VY3Ua4DCrjiuzC5xZskETHiHscS8gwdr6QrcnMA4XOkcP9xDbUDCfXSWeDfKIsr2tipdMdmFV9WY4QelY_sWy1oEF6PVfGmXd78wVO-m1OXVglR7h96ZpQKPjG4rCFX-lkBjFVX7C50z77BbreN0ByuukGFdbVVQ9btIKCJSKtYJZs7q6rlOtLiTa9P9Io5pvmiBdD0CfexStV-xiNZjgb-WnkVzhX7FRMXo1ybWBU5oL6kY61KDcJZLDVdiQu9N6zhakI1ZyJKZWSoNB1L5JVKsJZWQaBAhjCkEUTU2nSVrEZbJQsrlRIwxZdJMf9naGM9K145zKVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک سنگین در‌ جاده شمال
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/15712" target="_blank">📅 13:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15711">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/15711" target="_blank">📅 13:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15710">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پایان شهادت نتانیاهو در پرونده فساد مالی
بنیامین نتانیاهو پس از ۹۸ جلسه استماع در ۱۸ ماه گذشته، دفاعیات خود را در پرونده اتهامات فساد و رشوه به پایان رساند و با اشاره به شرایط سال‌های اخیر، گفت که «۱۰ سال جهنمی» را تحمل کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15710" target="_blank">📅 13:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15709">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وقوع تیراندازی درپایتخت ترکیه،آنکارا رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند. @withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15709" target="_blank">📅 13:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15708">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وقوع تیراندازی درپایتخت ترکیه،آنکارا
رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/15708" target="_blank">📅 12:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15707">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اختلال بانک‌های کشور برطرف شد
با اعلام شرکت خدمات انفورماتیک، اختلال خدمات کارت محور بانک‌های کشور برطرف شد.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15707" target="_blank">📅 12:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15706">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آژانس ایمنی هوانوردی اروپا به شرکت‌های هواپیمایی توصیه کرد همچنان از پرواز در حریم هوایی ایران خودداری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15706" target="_blank">📅 12:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15705">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رویترز: قراردادهای آتی نفت خام برنت به ۷۵.۷۴ دلار کاهش یافت که پایین‌ترین سطح آن از ۲۷ فوریه گذشته است
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/15705" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15704">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPydIC7f2xIgGwwL-oThSMIhqbVRvB111WijjNb5Td-IHBGWKV2GXunPtdGPf-ThrluRVEAh9OKlD7tKQs6vxXfpxVuPbXYgpsl6o6GRBLi6uTjT98XVQkAVVj_Zf2rhIIZPNNobnlKIs7rdTkTUNtgHDMjKzz8rg7pJ0-LU0gZalZqwfDreDQvcwPJEd7Z8XZVIEgjK9Zf_f7Y9bLBaGytqQeagOkTKGWu80KsmUu6tSNYQPiJyYE2kEe11Kr41u7_fvKzXi0HJeuzBAb0R_p2SmORyeLGCkcI40wdhfw-nIW0dgn_ToCoo2TUKgzcJZz8do1ZECQKn5LVpFzIeYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در تروث ‌: ایران رو کاملاً تحت فشار گذاشته بودم؛ در آستانه عقب‌نشینی بود، حاضر بود تقریباً هر چیزی که ما می‌خواستیم رو قبول کنه و واسه اولین بار تو چند دهه گذشته، احترام فوق‌العاده‌ای برای آمریکا و رئیس‌جمهورش، یعنی من، قائل شده بود.
ولی سنای آمریکا تصمیم گرفت تو بدترین زمان ممکن، یه رأی‌گیری بی‌معنی درباره قانون اختیارات جنگی (War Powers Act) برگزار کنه؛ رأی‌گیری‌ای که به بزرگ‌ترین حامی تروریسم تو جهان این پیام رو میده که آمریکا از کاری که من با اونا می‌کنم، راضی نیست و باید متوقفش کنم.
با این کار، عملاً به دشمن کمک کردن و دلگرمی دادن.
این سناتورها فقط کار من رو سخت‌تر کردن، ولی به هر شکلی که شده، کار رو به سرانجام می‌رسونم؛ چون من همیشه کارها رو به نتیجه می‌رسونم!
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/15704" target="_blank">📅 11:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15703">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هم اکنون دلار در تهران به صورت ناگهانی از 165هزار تومان عبور کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/15703" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15702">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGk7XFH_R7MfH33HsEOcxHN9HjUJs51TMeG16HcyYljoLHOICP5p5Qx-uYTM6ELg6Jc1MUDuEm_VZl6_JpOHBCgeXaDJcX0B9VAyB2ky5ZWdqNukAUNgQcvVIn6QbgBQ7Jq-Ot3-WbP-GnZzLpdqJryCAWk_zxva3zeCE_99yEgiLsKLFiNO8ZW1cTfdxSAKrqLPqesLsP3ZZrnTBAI_xLSRB5Cregk3kndC2Pzkvo86X9LD3HIFSWNW1ooyWGpmpwks9Ce_wIXpUA8dA9hUPp5YLn2Vp5RQx6X1hHv0VHyJm9YUoVOVWAq55grZnwvssdL8SwXh9OAELYeoVCOgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هگست:  اولین آزمایش سامانه پدافندی جدید «گنبد طلایی»، با موفقیت انجام شد @withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15702" target="_blank">📅 11:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15701">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هگست:  اولین آزمایش سامانه پدافندی جدید «گنبد طلایی»، با موفقیت انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/15701" target="_blank">📅 11:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15700">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پاکستان: مذاکرات فنی میان آمریکا و ایران هفته آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/15700" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15699">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RotWpQOnLMXDVOoR5uDNLX3gZpaZLDX-mrPsWW48gqobAK0c0E3lFK2nsDdI0hVvME0GsyWGMAQm8KLRlFHdIczQU7dt_JylNzd_xWMFadS5GFBKZpQ2kjlqhTsBwvMC6JwzHHf3ZtXHgFGwGLXBikieFxUMmAfR9NPavp0v7YDK5oU3MJv_ZC3gyEnKOlUMAFC4WWPeqx9LMyXeBSO-0s9iKQhIBu8mPuAc1XdW5MBAoZyJVyRSZ1AJzU-TgXuZaISM1lbEt_A4rjekZp_7uruXP9eWu7mrGZpicFPbCVC5MLEsbIPiLa1cZ37Wo59qYOHV-oo2kL7E0NufVotq6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین بروزرسانی از استقرار ناوهای نیروی دریایی آمریکا:
در منطقه سنتکام، دو ناوگروه لینکلن و بوش به همراه ناو آبی‌ـ‌خاکی تریپولی همچنان در منطقه حضور دارند و بخش عمده توان رزمی دریایی آمریکا را تشکیل می‌دهند.
دست‌کم ۱۷ فروند ناوشکن از کلاس آرلی برک نیز در دریای عرب، دریای سرخ و شرق مدیترانه حضور دارند که توان قابل توجهی در اختیار نیروی دریایی آمریکا قرار می‌دهند.
در غرب اقیانوس آرام، ناو هواپیمابر واشینگتن نخستین گشت عملیاتی خود در سال ۲۰۲۶ را در دریای فیلیپین آغاز کرده و ناو آبی‌ـ‌خاکی باکسر نیز در دریای چین جنوبی مشغول فعالیت است.
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15699" target="_blank">📅 10:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: از تأسیسات هسته‌ای ایران بازرسی خواهیم کرد
ما معتقدیم که بازرسی از تأسیسات هسته‌ای ایران در اسرع وقت بهترین گزینه است
اولویت اصلی ما مشخص کردن محل ذخایر اورانیوم غنی‌شده با خلوص بالای ایران است.
ما از محل اورانیوم غنی‌شده با خلوص بالا اطلاع داریم، اما مهم است که ایران ما را از آن مطلع کند.
به زودی با ایران برای تعیین تاریخ بازرسی‌ها و جزئیات مربوطه مذاکره خواهیم کرد
آژانس ما بازرسی را انجام خواهد داد و این به تهران بستگی دارد که واشنگتن یا ناظران دیگر را دعوت کند.
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15698" target="_blank">📅 10:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15697" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca023fa4e.mp4?token=b-Kw47JyBxtpzxUX9VwR91rJh76vcCNI23mutWYemXEwO9Y5G9sSJUL79ciupKqhTl8P5kS4OicAlwiYnWbx1M6s2QuesJo8NAO1FgP3ya9a3yEKhI-QENWJwa1IoE0Qm7PzOdeinPFlxwOGzsi7ogAILKL5VjHkuopnIXtT-6cESOLIs5lDFHn5YWcj5qbmwspv9Y_4A3We_i75Pb4bTQiME2AJ74GyzvIDFYuyTw0YUrR2L-_O1deXs4nIA6lNLdjAVh9jU0pBXUqyco9-s521GjGjdjmuEmSBBi_LmRmgyIKVjsqRKqCTu6D5lhsivOy3oCS7sgpdwAputUfctg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca023fa4e.mp4?token=b-Kw47JyBxtpzxUX9VwR91rJh76vcCNI23mutWYemXEwO9Y5G9sSJUL79ciupKqhTl8P5kS4OicAlwiYnWbx1M6s2QuesJo8NAO1FgP3ya9a3yEKhI-QENWJwa1IoE0Qm7PzOdeinPFlxwOGzsi7ogAILKL5VjHkuopnIXtT-6cESOLIs5lDFHn5YWcj5qbmwspv9Y_4A3We_i75Pb4bTQiME2AJ74GyzvIDFYuyTw0YUrR2L-_O1deXs4nIA6lNLdjAVh9jU0pBXUqyco9-s521GjGjdjmuEmSBBi_LmRmgyIKVjsqRKqCTu6D5lhsivOy3oCS7sgpdwAputUfctg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ که توی پیجش قرار داده و مضمونش بر اینه که هیچوقت نمیزارم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15696" target="_blank">📅 10:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaP1vIJtyrBvCqY3aJzqExvW_iCRl1oiXpqbi5-v4QP3Z7P9ENdVDcMkLS7NdVTLzfzxQXKXYmkuHCkeTixnOVeTqP5_IZG2Tg2EdhzakaoT5_TAlp6L87V3Rc0JSgzZ6vrde4qQ79TgNeaHG_vj20teRi8fqkW9QGinXhnIEnSVnVxSYQ9vHJcA3OGxdX20_Kl-ZNKTfiYTDUJ9zj4PyJCDUyryos5KFSdi7PJGAgkaW0rS15vr59gCv2szZ8vGEHFeXdKtNPGU936-XCdh6ETDd55MJXPGmZ87Isnse10MbGH9roZcc5Qlpvt1PpiA6XiIMhnSY32EokQpA2MUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۳۰ نفتکش حامل نفت خام ایران که دستگاه‌های فرستنده و گیرنده AIS آنها فعال است!
اکنون به سمت آسیا، چین، ژاپن و کره جنوبی در حرکت هستند و بیش از ۵۰ میلیون بشکه نفت حمل می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/15695" target="_blank">📅 01:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ‌ در‌ پنسیلوانیا:  ایران قلدر خاورمیانه بود.
ما باید این مسیر را انجام می دادیم. باید به ایران می رفتیم.
شما نمی توانید اجازه دهید که خاورمیانه و سپس ما را منفجر کنند، اگر این امکان پذیر باشد. ما قبلاً آنها را می گرفتیم، اما آنها اسرائیل را منفجر می کردند. آنها می توانستند کل خاورمیانه را منفجر کنند.
به توافق صلح تاریخی با ایران دست یافتیم
ایران عالی بوده است. اگر ایرانیان هوشمند باشند، منطقی خواهند بود؛ در غیر این صورت، مجبور خواهیم شد کار را به پایان برسانیم که احتمالاً کمتر از یک هفته طول می‌کشد.
اما فکر می‌کنم همه چیز برای آن‌ها خوب خواهد شد. آن‌ها کاری که باید انجام دهند را انجام خواهند داد زیرا ما می‌خواهیم این کار انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/15694" target="_blank">📅 23:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سنای آمریکا به پایان جنگ با ایران رأی داد  سنای آمریکا تصویب کرد که ادامه عملیات نظامی علیه ایران مستلزم کسب مجوز کنگره است. @withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15693" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سنای آمریکا به پایان جنگ با ایران رأی داد
سنای آمریکا تصویب کرد که ادامه عملیات نظامی علیه ایران مستلزم کسب مجوز کنگره است.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15692" target="_blank">📅 23:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۴ اسرائیل نقل قول‌های اختصاصی از احمد وحیدی، فرمانده سپاه پاسداران، خطاب به مقامات ارشد رژیم را منتشر کرد.
1 «ما رئیس جمهور ترامپ را به زانو درآوردیم. ما به آنچه می‌خواستیم رسیدیم. طبق معمول، غرب احمق فکر می‌کند که در عوض چیزی از ما دریافت می‌کند، که البته هرگز اتفاق نخواهد افتاد.»
2 «هدف ما در حال حاضر این است که آمریکایی‌ها را در تنگنا قرار دهیم. هرگونه تخلف، هر چقدر هم کوچک، به ما اجازه می‌دهد که تهدید به بستن تنگه هرمز کنیم و ترامپ و مردمش با هر چیزی موافقت خواهند کرد.»
3 «ترامپ فکر می‌کند پولی را که به ما می‌دهد صرف خرید کالاهای آمریکایی خواهیم کرد. این هرگز در طول عمر ما اتفاق نخواهد افتاد.»
4 «حالا باید به آمریکایی‌ها بفهمانیم که اسرائیل بازیگر بد خاورمیانه است. هدف این است.»
5 «از هیچ چیز دست نکشید. تهدید کنید. و در صورت لزوم، از مذاکرات کناره‌گیری کنید.»
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15691" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نخست‌وزیر پاکستان: هفته آینده با مجتبی خامنه‌ای در ایران دیدار خواهم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15690" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15689">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15689" target="_blank">📅 22:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15688">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام ندهید. در غیر این صورت مسئولیت با شماست و توسط حرص و طمع خود شما انجام گرفته. به این مسئله دقت کنید و
فقط از تحلیلها و مطالب آموزشی افراد استفاده کنید
. هیچ پکج یا هیچ پرداختی به هیچ بی ناموسی انجام ندهید.
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
از توجه شما به این مطلب سپاسگزارم، یاشار</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/15688" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15686">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lo0dIQkxPfhAdW1cDeZV6edhZnjA_b_ZoRqikrsliSoGVu2d_rxorbOW_kMwzM0YtfIniXDxhkWjJ5aTdRfkHNjuOSE1DT8hdT17PmDpr6tqZ0-dw9PvTJbayo5xMr2_1whMhUxEGL9cudDBUVTRXOQH1mrMSGhojW2ITF2uURzbLpA5WLZIJsqsmRs7lrIf331ny-yLSz_sPVsvJ8C2zWwcCqtZR-pSoozEWvngcRnTFqadhBoklFv9pRrepZl1EWkrzYEW1sa1qS9x__PRCeURjPP6CSGOvSfYkQpryemFUreeUf2Z4chu0vIQVcoCZ7eA4zts15506ofzlGSrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل با انتشار نقشه تونل کشف شده جدید حزب الله نوشت:
حزب‌الله با حمایت مالی جمهوری اسلامی طی سال‌ها(صدها میلیون دلار) شبکه گسترده‌ای از تونل‌ها، انبارهای تسلیحاتی، سایت‌های موشکی و مراکز فرماندهی در جنوب لبنان ایجاد کرده ، هدف این زیرساخت‌ها حمله به اسرائیل بوده
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15686" target="_blank">📅 22:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7644ffed31.mp4?token=lq8iPQa8cF46H69UCvVnbAC8QGrStVI5nzo-Xj_BL0wGF7w_Uy1JP9p64lv8DmetBdrEa6qYDj3pwjgPfiEiKAewdNladVCPKGRM52OC107FnS_5Ib4g92rNd7NlIU9eyzEYueipouhfj0Hk1TxctUCiUOccNd3rhhQQdhMIJT7QZBr1GYHRBFUR9kGtHgr-B0_xX4GmVidIlJLwrKtK9Dp2TD2HuT_JNT_MWm6P7dk9EkhMO0bg5AbpOwaD4bd2DXqC2D61dyLuFQuYWRAbsVrXTjDo-0p7z0EqRQ08tEhIQMSqwyARccKm0RMbAZ6MG7GitiU8Tv-uXJi2lSTO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7644ffed31.mp4?token=lq8iPQa8cF46H69UCvVnbAC8QGrStVI5nzo-Xj_BL0wGF7w_Uy1JP9p64lv8DmetBdrEa6qYDj3pwjgPfiEiKAewdNladVCPKGRM52OC107FnS_5Ib4g92rNd7NlIU9eyzEYueipouhfj0Hk1TxctUCiUOccNd3rhhQQdhMIJT7QZBr1GYHRBFUR9kGtHgr-B0_xX4GmVidIlJLwrKtK9Dp2TD2HuT_JNT_MWm6P7dk9EkhMO0bg5AbpOwaD4bd2DXqC2D61dyLuFQuYWRAbsVrXTjDo-0p7z0EqRQ08tEhIQMSqwyARccKm0RMbAZ6MG7GitiU8Tv-uXJi2lSTO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک یه ویدیو از محرم پست کرده
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/15685" target="_blank">📅 22:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15684">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQaDao4wlgJifyJ-oLHXkYfViGVka5sljv2fe_Ly3EPpdhACJPkOdkp63pWgDpgQ6qiwcpw8ARz5MMwYCKYrbYTM-Ear0agH686-DZJy88-xvAbdURtksax0Wo1l2Z8P3PGTU7rJL1O6w1auNp13cWx3xWZmtVK9Iq7ZR_nhKioDgbuH7SVE7QvN-dhAl4nefctSW5MZeXe6hi0l8ZstBY4GSVByo-1u7IukOWDMKoEFbBxZC-gcBx1mYuYYFezWiQ7kqrgZeRu6l3qKXX-elWapvmnApzwnWTf-kqO8WH1qQ3lQIcJ8_cbnOYr9BSfwM_OEOXY_7veMtizE93O4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبینا محمدعلی‌پورثانی پس از ۱۰ روز پیدا شد
سیدامیر احمدی، دادستان عمومی و انقلاب بهارستان:
مبینا محمدعلی‌پورثانی، دختر ۱۹ ساله ساکن نسیم‌شهر، پس از ۱۰ روز بی‌خبری پیدا شد.
این دختر پس از پیگیری‌های قضایی و اقدامات انجام‌شده، پیدا شده و در سلامت کامل به سر می‌برد.
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/15684" target="_blank">📅 21:44 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
