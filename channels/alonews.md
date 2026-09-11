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
<img src="https://cdn4.telesco.pe/file/CzkjVa6VyTe59Ds_gIgwgwN8Udr1tguE2C38FUVeLAl3eM77rBwC9jSvlSnBZeY21cj-jeKASVcd1wzT10UVHfw2dCSQSOgpTMIkqIUXjaZIemVAshxTJmn054mIuI9UJ4Qmq-Ru-jpZeW3r7oCo85M7liR0meUnNexH9ak2piffYKmn94OvX93Q3qaNkYlKVQpC0WiFA-AKmy6FhaDjDHnAfvR1Tjpn1Kne9qpZ1Lq4hDkwtKtKd2SqHtu5d9W7Fnm2PqBQ9y6qnHtr7kh0VAy3xWdVcuhRNAleDVWiu5MkW4yfjZ4Yl4d7ldSD8-C4vaH2AJZxVnj6GU25dz4P0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 927K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 04:46:05</div>
<hr>

<div class="tg-post" id="msg-146793">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: اگر ایران سلاح هسته‌ای داشت، اسرائیل و خاورمیانه را نابود می‌کرد و شهرهای آمریکا را هدف قرار می‌داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/146793" target="_blank">📅 03:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146792">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ: دیشب ۲۲ قایق سپاه رو زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/146792" target="_blank">📅 03:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146791">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ: بعد انتخابات جنگ رو تموم میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/146791" target="_blank">📅 03:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146789">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: چگونه ایران می‌تواند موشک‌ها را پرتاب کند، در حالی که ما آن‌ها را نابود کرده‌ایم؟
🔴
ترامپ: آن‌ها همیشه می‌توانند موشک‌ها را پرتاب کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم دارند. البته ما آن‌ها را سرنگون کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/146789" target="_blank">📅 02:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146788">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=kgkv7iEEwaXThp_JqKk7V_IihFp3GsJzIptUcWxcozUVamPe4z2MqWvfIF9AU63uroO4IrvPqdkAUGwWioHhMEeNBdZyxuK1TLANkw9DLvXKQG5Xy5I2g07qvOg6ZimPiT5hlfkK6tSfMX9xsdS_2KF3TevLCb2mYT80GgG5sU0vdEO7J-mGKRMkKzZ-31zIZxsm-fVqYTjpu-J581D91Um5ITfpYijS7hQI6Y6VjSkTE08tRb6lPHg_0ZoA92ex23YH-XKpoWeZq7IAWVW3HSADowgRocxps65Q4rA_AEpl8NIWnplPLkmtER5Nckqg8ef6am2gMSUAksCMMLIp3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=kgkv7iEEwaXThp_JqKk7V_IihFp3GsJzIptUcWxcozUVamPe4z2MqWvfIF9AU63uroO4IrvPqdkAUGwWioHhMEeNBdZyxuK1TLANkw9DLvXKQG5Xy5I2g07qvOg6ZimPiT5hlfkK6tSfMX9xsdS_2KF3TevLCb2mYT80GgG5sU0vdEO7J-mGKRMkKzZ-31zIZxsm-fVqYTjpu-J581D91Um5ITfpYijS7hQI6Y6VjSkTE08tRb6lPHg_0ZoA92ex23YH-XKpoWeZq7IAWVW3HSADowgRocxps65Q4rA_AEpl8NIWnplPLkmtER5Nckqg8ef6am2gMSUAksCMMLIp3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: چگونه ایران می‌تواند موشک‌ها را پرتاب کند، در حالی که ما آن‌ها را نابود کرده‌ایم؟
🔴
ترامپ: آن‌ها همیشه می‌توانند موشک‌ها را پرتاب کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم دارند. البته ما آن‌ها را سرنگون کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/146788" target="_blank">📅 02:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146787">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: روز دوشنبه یک بانک بزرگ را تحریم خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/146787" target="_blank">📅 02:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146786">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnHIUaRP2rt97L2CazTKNZ1gmTQmpY5FJIXae63XZKXvFt4pwfvqampxnAJrl3nuJs_t64xYBcwgAPTHv4DLUIpugAJebwn2BDoei72eC0tW10_tqDV5-MnLT6iDEVS6wFi3vQZkhwd95_yYmrk4rkSj_pdOjupnOUr41ZXrzIbXd47nVtuV3DhJztLD2U1HAbmuUPAo2bCXocdk2F9Qh_e-ju1hLTXgfnqJpYr82-KX6Y8tkH3W3GHfCxBMK-akE0Pt21HKxp3vA1JEPfmPkFMTDEhkSTBAA_0wJH5JzWvb7rpGUQfMWwT7gia2QHDWVodv18Tf5u53xi8DwlNffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میثم مطیعی، مداح: مردم ایران فقط همینایی هستن که شب‌ها تو تجمعات هستن
🔴
پ.ن: منظورش اینه همین اندک زن‌ها و پیرمرد‌هایی هستن که میان شب نشینی شبانه به صرف چایی و شیرینی و.... تا حوصلشون سر نره خونه، مردم ایرانن
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/146786" target="_blank">📅 01:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146785">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
حقوق ثابت نماینده‌های مجلس ۵۰درصد افزایش یافت و مزایای جانبی نیز افزایش پیدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146785" target="_blank">📅 01:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146784">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
جنگ نزدیکه
‼️
نفت 110دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/146784" target="_blank">📅 01:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146783">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1771681df.mp4?token=QFOm2bchVt-cJTagwOrhA-lR350FCH32T7UPUOL-MJ3XR0wsFBYxi_m5h-4_UaYRo3Xn64B6mcq_7kSaOjdUmqJWoX4TSbuM1YrdJjeqFaqWzZ-F8OyHu6KpzWQCtuRj_eIwQ8Y4Py09chjwRrmUMEM7Y8f-SQ18aUIcqaggb6hIZvf2IB3lH98F3hDBDz640PY0OL3VV07pNuqWMIBxOCZWpuUw2jbksOvZWV34vCawpF3q25dmcn3DzE_RC9iuFgvwPFB91au5pvz4fdrw5eSdaKa7ILIXudOioibgiItSGjxmcjqk7JRCd5_KbmuB05Ax60PHaqa8oDcdZhgfWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1771681df.mp4?token=QFOm2bchVt-cJTagwOrhA-lR350FCH32T7UPUOL-MJ3XR0wsFBYxi_m5h-4_UaYRo3Xn64B6mcq_7kSaOjdUmqJWoX4TSbuM1YrdJjeqFaqWzZ-F8OyHu6KpzWQCtuRj_eIwQ8Y4Py09chjwRrmUMEM7Y8f-SQ18aUIcqaggb6hIZvf2IB3lH98F3hDBDz640PY0OL3VV07pNuqWMIBxOCZWpuUw2jbksOvZWV34vCawpF3q25dmcn3DzE_RC9iuFgvwPFB91au5pvz4fdrw5eSdaKa7ILIXudOioibgiItSGjxmcjqk7JRCd5_KbmuB05Ax60PHaqa8oDcdZhgfWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری که تنگه هرمز بسته شد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146783" target="_blank">📅 01:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146782">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab0f48a8.mp4?token=v2mD0ekO2-m9jH6wLADEWyiOox8lxKxOpKkNm9k2JTb4gcQ3lUl05pDEqqpYXFYzvIB8bNWvwcTSjHT3YmUhFEdKKKwUQw9aH7iitcJ4E2vdiitng7ciOt6n3hDpxk53p-is5H3r9k4cwqXf6O-Obd6cydYZXFYhjXRdLO1kb3KToJHsyLuyKusiNGVnuZttbjgEiaeBNEXJ-LUdjat8765KuuPfzmStANJbi3hgIgu425X6JaJiWzJTqDegUXT4MyVQYNkM3Jt21Dge09X9FBCQRwBLLhJUxXkcW-Gkc9Fekx44_ONtExRubYqSuwf2DlZLwYwP3ypzyLEWDtq4HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab0f48a8.mp4?token=v2mD0ekO2-m9jH6wLADEWyiOox8lxKxOpKkNm9k2JTb4gcQ3lUl05pDEqqpYXFYzvIB8bNWvwcTSjHT3YmUhFEdKKKwUQw9aH7iitcJ4E2vdiitng7ciOt6n3hDpxk53p-is5H3r9k4cwqXf6O-Obd6cydYZXFYhjXRdLO1kb3KToJHsyLuyKusiNGVnuZttbjgEiaeBNEXJ-LUdjat8765KuuPfzmStANJbi3hgIgu425X6JaJiWzJTqDegUXT4MyVQYNkM3Jt21Dge09X9FBCQRwBLLhJUxXkcW-Gkc9Fekx44_ONtExRubYqSuwf2DlZLwYwP3ypzyLEWDtq4HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یمن موشک شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/146782" target="_blank">📅 00:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146781">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
هم اکنون پرواز جنگنده‌های نیروی هوایی ایالات متحده بر فراز آسمان بغداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146781" target="_blank">📅 00:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146780">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
لحظه انفجار تونل های حزب الله از نزدیک
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146780" target="_blank">📅 00:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146779">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
فارس: قیمت گازوئیل تو آمریکا از ۶ دلار رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/146779" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146778">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
امواج مدیا: انتشار گسترده فیلم‌های هالیوودی از مجموعه تونل‌های حزب‌الله که امشب توسط اسرائیل تخریب شد،قابل توجه است.
🔴
یک احتمال این است که این فیلم برای ارائه به ترامپ - احتمالاً توسط هگزت - به عنوان بخشی از استدلال برای تشدید بیشتر تنش‌ها،از جمله حمله به «کوه کلنگ» در ایران، در نظر گرفته شده است. اتکای ترامپ به جلسات توجیهی ویدیویی در طول جنگ و ترجیح او برای نمایش بسیار مشهود نیروی نظامی، به خوبی مستند شده است.
🔴
زمان‌بندی نیز قابل توجه است. حملات اسرائیل همزمان با ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل متحد، در لحظه‌ای که دولت ترامپ به نتایج ملموس از کمپین فشار تشدید شده خود علیه تهران نیاز دارد، رخ می‌دهد.این ترکیب می‌تواند انگیزه‌هایی برای تشدید بیشتر تنش‌ها ایجاد کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/146778" target="_blank">📅 00:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146777">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رسانه‌های آمریکایی گزارش داده‌اند واشنگتن علاوه بر پشتیبانی اطلاعاتی و هدف‌گیری جغرافیایی حملات علیه حوثی‌ها، یک سامانه هدف‌گیری میدانی و بلادرنگ مشابه سیستم «ماون» پنتاگون در اختیار عربستان سعودی قرار داده است.
🔴
با این حال، در ارتش آمریکا نسبت به مشارکت بیش از حد نزدیک در بمباران‌های تحت رهبری عربستان، به‌ویژه در صورت بروز تلفات غیرنظامی، نگرانی و احتیاط جدی وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/146777" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146776">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
خبرفوری و مهم
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/146776" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146775">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی از هدف قرار گرفتن ۲ فروند کشتی در تنگه هرمز خبر می دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/146775" target="_blank">📅 00:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146774">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نتانیاهو: امشب، بزرگترین پایگاه ایرانی خارج از ایران را نابود کردیم. این پایگاه، تونل‌های علی الطاهر در لبنان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/146774" target="_blank">📅 00:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146773">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jZ6qOhJwERUBGkSqLTwzwbX4Z4rM9el5TPANxKCpYHC6k3nTO1SQch4CE7ZqJB3VcBF7acjhgpGcHM5YUBGztBtx-8ym-7jHX3ET-xsfWJvO7DSF9ZYb8H_SW1oHvRhQHBDqN_g6kOUaVackjYSCpuxawYktdzCWwiTkaFvK20u78NNMBr4nAxago7CKhdThEostVBqcrRicGk1-e6WIBA0dJGgwLAhCUs9b6RET6Fg31l7zSvdl2Psn8QBKOTRvXPpELT9MptOmnlvaDo0LPbS7VWdSBy3W4AlMx113046TDFL0gHQID4hKzDXumFTC9FBI_wmPuK9RKwdjcGyhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: ونس ترامپ را دور زد؛ مستقیم از فرماندهان ارتش آمریکا ارزیابی از جنگ گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/146773" target="_blank">📅 00:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146772">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
روزنامه یدیعوت آحارونوت در گزارشی اعلام کرد که ارتش اسرائیل خود را برای مقابله با پاسخ احتمالی و واکنش حزب‌الله لبنان آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/146772" target="_blank">📅 23:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا در چارچوب «عملیات طرد اقتصادی» ۱۴ فرد و ۵ نهاد رو تحریم کرد. این تحریم‌ها شبکه‌های پشتیبان کتائب حزب‌الله، حزب‌الله لبنان، تدارکات نیروی قدس سپاه و شبکه‌های دور زدن تحریم‌ها رو هدف گرفته.
🔴
دفتر کنترل دارایی‌های خارجی آمریکا همچنین از توافقی به ارزش یک میلیون و ۴۲۷ هزار و ۲۳۰ دلار خبر داده و اعلام کرده رد کردن بیشتر درخواست‌های در انتظار برای مجوزهای اختصاصی مرتبط با ایران رو آغاز کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/146771" target="_blank">📅 23:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35cc518a6a.mp4?token=Wf7EXmPA3HyfEbwK1ZOw3QvDBNP3klBybqpVZhqrv38q0Nb_4rkauyH_gJyUMxByaRtQfrWMxB0Ao1vFoEs3LU3JEgpEUx01gnmyKmYMlbSdPIjSCavnVSvT01jKLkXuI4vHDIgoU2E4kwbohova2o08_APhT-PHa-ACzkn_WlWrE_NVmgW9gJZ3MI7f7SIp1w47v6W26Rrd_W_nDEPygpwLeUXSIjpH7FrX4cUoBYN2Q9uTCn-ythboSM6gnztp-S0ibysOzE2F4VWMhBi5bY_nNX0CySDZI8XyYrWRbSQM3vHZ83ZrqveTRlVoAJlc_Bqih2zWu3a0sQ_LC6JkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35cc518a6a.mp4?token=Wf7EXmPA3HyfEbwK1ZOw3QvDBNP3klBybqpVZhqrv38q0Nb_4rkauyH_gJyUMxByaRtQfrWMxB0Ao1vFoEs3LU3JEgpEUx01gnmyKmYMlbSdPIjSCavnVSvT01jKLkXuI4vHDIgoU2E4kwbohova2o08_APhT-PHa-ACzkn_WlWrE_NVmgW9gJZ3MI7f7SIp1w47v6W26Rrd_W_nDEPygpwLeUXSIjpH7FrX4cUoBYN2Q9uTCn-ythboSM6gnztp-S0ibysOzE2F4VWMhBi5bY_nNX0CySDZI8XyYrWRbSQM3vHZ83ZrqveTRlVoAJlc_Bqih2zWu3a0sQ_LC6JkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: وقتی افرادی را می‌بینم که مدال افتخار کنگره را دریافت کرده‌اند، کسانی که هنوز زنده هستند... بسیاری از آن‌ها فوت کرده‌اند. آن‌ها در جنگ جان خود را از دست دادند.
🔴
نکته‌ی مثبت در مورد مدال افتخار ریاست جمهوری این است که افراد معمولاً از سلامتی خوبی برخوردارند. آن‌ها این مدال را دریافت می‌کنند زیرا در ورزش‌ها پیروز شده‌اند. اما آن‌ها مجبور نیستند مورد اصابت گلوله قرار بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146770" target="_blank">📅 23:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15fee3e724.mp4?token=ZEl2sxYv2VUaNhzpmd8JVEJnkmNcJDHSeVDtnMGGQLJXPc0FWOJFdG7aotqAE6Li7w4yTBu2oFNXdxRolULwJO14RJA7-C4QPO_hQiBUCPFyWBd5RuE2lhvfp_A4t0EjQN_9LAxXL5UjaMSC8qWqcBedODhpQ8U7NnenjJxfs6LrH9O8sZQJUVvg8_-y_1lJkdZGOCLU7hDmp6ObRmG_ipE8qjDFjr2cBA3T9VWU-l4fglOJK0EV1MyusO8Cmusy6j4zeb9JDUSt2Oj2soapxcb2Cpgnou5EcnirVIjk-iGWDiqXdra9wYiHJ5ciitXxcs7EpIvjDF1Fy6T7LJrlUTyCmWjw_wHdxLR1MF5asx0BXFKg1724OrntonpE_XjmNYZNviFv81My-4Az8ejNmClOSe0gfsPWmbtWgmVaXx4FoGLSZsIvjb2VQXsiKPVRqxaNWCrkU_3-bnYMbwIhXK0TyC0ITOhLxrOlm6QhLT5lwS9eE63F8xjyEsKMAtSnN3uW_3XN5Sun2jsx4lOretq0ZPNpUjP8-LlPLdPkzBdPIvi3bNJzbHKtlnGhPqsTn_EuiQLAxibLpfRAYV2RLAKIklCOwg6lIyC0JwiXG7l5-iX9ZGOZ-NTz366qtlze6CxyOZlC3swK0AI_15CzVRP6xV6S08nuWfRtytO1eRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15fee3e724.mp4?token=ZEl2sxYv2VUaNhzpmd8JVEJnkmNcJDHSeVDtnMGGQLJXPc0FWOJFdG7aotqAE6Li7w4yTBu2oFNXdxRolULwJO14RJA7-C4QPO_hQiBUCPFyWBd5RuE2lhvfp_A4t0EjQN_9LAxXL5UjaMSC8qWqcBedODhpQ8U7NnenjJxfs6LrH9O8sZQJUVvg8_-y_1lJkdZGOCLU7hDmp6ObRmG_ipE8qjDFjr2cBA3T9VWU-l4fglOJK0EV1MyusO8Cmusy6j4zeb9JDUSt2Oj2soapxcb2Cpgnou5EcnirVIjk-iGWDiqXdra9wYiHJ5ciitXxcs7EpIvjDF1Fy6T7LJrlUTyCmWjw_wHdxLR1MF5asx0BXFKg1724OrntonpE_XjmNYZNviFv81My-4Az8ejNmClOSe0gfsPWmbtWgmVaXx4FoGLSZsIvjb2VQXsiKPVRqxaNWCrkU_3-bnYMbwIhXK0TyC0ITOhLxrOlm6QhLT5lwS9eE63F8xjyEsKMAtSnN3uW_3XN5Sun2jsx4lOretq0ZPNpUjP8-LlPLdPkzBdPIvi3bNJzbHKtlnGhPqsTn_EuiQLAxibLpfRAYV2RLAKIklCOwg6lIyC0JwiXG7l5-iX9ZGOZ-NTz366qtlze6CxyOZlC3swK0AI_15CzVRP6xV6S08nuWfRtytO1eRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من شخصاً دوست دارم مدال افتخار کنگره را دریافت کنم، و من درباره آن مطالعه کرده‌ام و قصد دارم آن را به خودم اهدا کنم، هیچ مشکلی در این باره ندارم، اما اجازه ندارم این کار را انجام دهم. باور می‌کنید؟
🔴
تنها کاری که اجازه ندارم انجام دهم این است که آن را به خودم بدهم.
🔴
من فقط شوخی می‌کنم. در واقع، من شوخی نمی‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/146769" target="_blank">📅 23:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6844b8766.mp4?token=gzUsQi9WAop-js0cLXDv0fLOr7LdERFJMmfnVDb5KcDunIvb5pB9e8IZfMP31KhA35N0n31BLYhDBHWUnWOksmC6c0aGWsL1gfOV7S7cgMDPzx4xpveDqdPDM9779WBgqfUkcVK5HkLsUUUTmf36V5Cn7xVHvOpXdXLR8SOe7ipjBJFcbd_TLbgq_fWEGBMDN5BHMrG1Gx7rgMZbGy1joRwEf1V0kDmRRpP39cnGdq4y3KNv6aPN9NAG5SymBBYm5mOzCeTmyChffxhqEnx2aLxu6-ea_zg7W4acXqmbqy5xkXVDIg5bPjGxI-KoFnp7nA-VpokSQ3NKv7Xm3w9iAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6844b8766.mp4?token=gzUsQi9WAop-js0cLXDv0fLOr7LdERFJMmfnVDb5KcDunIvb5pB9e8IZfMP31KhA35N0n31BLYhDBHWUnWOksmC6c0aGWsL1gfOV7S7cgMDPzx4xpveDqdPDM9779WBgqfUkcVK5HkLsUUUTmf36V5Cn7xVHvOpXdXLR8SOe7ipjBJFcbd_TLbgq_fWEGBMDN5BHMrG1Gx7rgMZbGy1joRwEf1V0kDmRRpP39cnGdq4y3KNv6aPN9NAG5SymBBYm5mOzCeTmyChffxhqEnx2aLxu6-ea_zg7W4acXqmbqy5xkXVDIg5bPjGxI-KoFnp7nA-VpokSQ3NKv7Xm3w9iAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انفجار تونل های حزب الله از نزدیک
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/146768" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
خداداد عزیزی : فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/146766" target="_blank">📅 23:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
صداسیما: بهترین برنج بازار الان کیلویی ۴۷۰ تومنه، گرون نخرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/146765" target="_blank">📅 23:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سی‌ان‌ان: بیش از ۱۰۰ مشاور نظامی آمریکا برای پشتیبانی از عملیات عربستان علیه یمن در این کشور مستقر شده‌اند؛ این نیروها در زمینه اطلاعات و هدف‌گیری به افسران سعودی کمک می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/146764" target="_blank">📅 23:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7cc27edd4.mp4?token=Acbc-rOg0VjwGShRRT4xZrIF6bzxxaNFlK3KHZP03ZjtY2fxPsOBrs4fq91o3BRjl4W2cVeT-1h6ISEDWD4gajlcA8--8uPWLx9Nj4xBt5QyHaOR1Gv-ZmQkIvnYbGiO8iUSwLI3cTfraCW5k_--6hZhEggty9H26TQ7oQT61IO_w8KomdmRiEJvlZZbX5e7vx9w7EqckmjqnH9wYS4nZ8UrzxD6H2XBLS0UhqJM7yrC1A75DmhVKsHbenl73v90mbLhJ1p6WSEweNlef170qgiILVixNiguuXGpdsfbIfXlFS_5JSWb_ewx-25QzgEXxpfZ5dpo-PNp44fWO632mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7cc27edd4.mp4?token=Acbc-rOg0VjwGShRRT4xZrIF6bzxxaNFlK3KHZP03ZjtY2fxPsOBrs4fq91o3BRjl4W2cVeT-1h6ISEDWD4gajlcA8--8uPWLx9Nj4xBt5QyHaOR1Gv-ZmQkIvnYbGiO8iUSwLI3cTfraCW5k_--6hZhEggty9H26TQ7oQT61IO_w8KomdmRiEJvlZZbX5e7vx9w7EqckmjqnH9wYS4nZ8UrzxD6H2XBLS0UhqJM7yrC1A75DmhVKsHbenl73v90mbLhJ1p6WSEweNlef170qgiILVixNiguuXGpdsfbIfXlFS_5JSWb_ewx-25QzgEXxpfZ5dpo-PNp44fWO632mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک دوربین امنیتی، لرزش خانه‌ها را در نتیجه انفجار  در تپه علی الطاهر ثبت کرده
🔴
زمین لرزه ناشی از انفجار علی الطاهر تا ۴/۱ ریشتر گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/146763" target="_blank">📅 23:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFU99nK50dsCKl8VPix52Y03yk2_hK7AB2eZRGVqh6j1j2Q02BvxXYNQaYdCTKxPea1YqaMAZ4O8dqDLMb4zIo62mQK-toXNaj7f7OgxBSdPsI_dnWP0hMZQsfFvqcWOqCgfYr--aUe5GsfKjvf8eo0OqkyIgCQ4ZnBk0cIarwxNiZKTwjG0BCSIJzY13y9DOvTjTc8eqBaxcimtYquDD11omQolFZClFiSWCVbOTSiZxX2TzztgKwcKRJ64C-MFnMlsmNSw-tutPmIHDqO1SWq4gDBXWxXz-rj9RzECaURtc7UbgF2Z25tXoikRMqjZWjsFOtSDV_uknyyQqQGd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: مردم شجاع یمن، با اذن خداوند متعال، قطعاً پیروز خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/146762" target="_blank">📅 22:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d08c935a.mp4?token=o1EMCadw9ZdW7Q4tw0IHj_kxCn7uFjtF-Y304d2FJLXQW79-DBAIqJfIEk92MmpX15dLJkKF-OmwcpC7DyO2thtammsWYc4b8dmE24gvaqsi2T_uSW4iQz5ofBTPi0eN__TpX-d_ElAxDTTr6s2v1155GMpC0qqo5a3XJagFfmMcLgH6RxqrKgHlW25YdFXvEPrD-fYZvedY8n76eP1o3dhZk9Ajwyu2gBxgox2NIEdR7SZLGoTtXzMOzgl3Y4gEflwgUfUX85kg3-wsPHUwtI7X9t4NAiHtie0dzMiXppYNvkiQZuB3RSFUcNcHmKgXyXm9huvqNb2sd4TYOZF3QTPVRMitGVtY44IvHpKCBVPfah6iwfTr4vhonhyAQpqT9wv8tBx0AzkHs17r8uGhZTV71d_JNrxSrGWlW7gpLre4N6mRZZSsD6HjRSbAAcNFJKDoAxmXJC5av-6YOVEzMQxFMzTNZX3nWda_BdNVYPczdcdUNr6ieI_vWsayTZg_o_IVUpgIuxknmMS5C-ki43PvsPbXhueV-xy7xiJA2T2wldEAJfvXFSAfiXdTa48Rbgl1bh_zXEBJkUgTkPS0IxuKt3UzyLxBuDzMswclJB0C_gfe4MZfACHzb75t0R3Mcpd8I3Vz7FoiWYCBRzTvuezPnTMvLe-SBba9d8x-SE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d08c935a.mp4?token=o1EMCadw9ZdW7Q4tw0IHj_kxCn7uFjtF-Y304d2FJLXQW79-DBAIqJfIEk92MmpX15dLJkKF-OmwcpC7DyO2thtammsWYc4b8dmE24gvaqsi2T_uSW4iQz5ofBTPi0eN__TpX-d_ElAxDTTr6s2v1155GMpC0qqo5a3XJagFfmMcLgH6RxqrKgHlW25YdFXvEPrD-fYZvedY8n76eP1o3dhZk9Ajwyu2gBxgox2NIEdR7SZLGoTtXzMOzgl3Y4gEflwgUfUX85kg3-wsPHUwtI7X9t4NAiHtie0dzMiXppYNvkiQZuB3RSFUcNcHmKgXyXm9huvqNb2sd4TYOZF3QTPVRMitGVtY44IvHpKCBVPfah6iwfTr4vhonhyAQpqT9wv8tBx0AzkHs17r8uGhZTV71d_JNrxSrGWlW7gpLre4N6mRZZSsD6HjRSbAAcNFJKDoAxmXJC5av-6YOVEzMQxFMzTNZX3nWda_BdNVYPczdcdUNr6ieI_vWsayTZg_o_IVUpgIuxknmMS5C-ki43PvsPbXhueV-xy7xiJA2T2wldEAJfvXFSAfiXdTa48Rbgl1bh_zXEBJkUgTkPS0IxuKt3UzyLxBuDzMswclJB0C_gfe4MZfACHzb75t0R3Mcpd8I3Vz7FoiWYCBRzTvuezPnTMvLe-SBba9d8x-SE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : بسیار خوشحالم که اعلام شد پرو به طرح "سپر قاره آمریکا" خواهد پیوست.
🔴
این طرح در برابر چه تهدیداتی است؟ این طرح در برابر تهدیدهایی است که حاکمیت کشورهای مستقل را به خطر می‌اندازد.
🔴
این طرح در برابر گروه‌های جنایی فراملی است که در بسیاری از موارد، پول بیشتری و تجهیزات نظامی بهتری نسبت به دولت دارند.
🔴
این موضوع غیرقابل قبول است و تنها راه برای شکست دادن آن، مقابله قاطعانه با آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/146761" target="_blank">📅 22:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb51f27a7.mp4?token=ftujAaBrkBEoAZJUuaBeRvPJ-fmKulZF9jegTa3TkuV438o09_YDx0u-scMZqyShd01LdIg2O2-02IQ9gDSoI4M_bG4ljvasXTQ3toNzsBUYiBSbJHHhFByKgQIv_4oRj6aP9STiKO6kNvCaXQMQyxULgQoIaGJ-ESrbNt4uzCvyqMP4Kufa7PZ0myQZ6p_qhbX_8sjTaKQcxvFOsFhfWPePvGhOrVzOqkyz3mKMwM8zFC88X6GJN9dS90Jt6NlRrKvSgD6nTWlI0BNexIuoNjGNVpHVbBlug4hFJ_dFDuq8b1LyMheV9MIe7GFg7SFApxZuA0RUqfnZ7NyZWkKZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb51f27a7.mp4?token=ftujAaBrkBEoAZJUuaBeRvPJ-fmKulZF9jegTa3TkuV438o09_YDx0u-scMZqyShd01LdIg2O2-02IQ9gDSoI4M_bG4ljvasXTQ3toNzsBUYiBSbJHHhFByKgQIv_4oRj6aP9STiKO6kNvCaXQMQyxULgQoIaGJ-ESrbNt4uzCvyqMP4Kufa7PZ0myQZ6p_qhbX_8sjTaKQcxvFOsFhfWPePvGhOrVzOqkyz3mKMwM8zFC88X6GJN9dS90Jt6NlRrKvSgD6nTWlI0BNexIuoNjGNVpHVbBlug4hFJ_dFDuq8b1LyMheV9MIe7GFg7SFApxZuA0RUqfnZ7NyZWkKZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : او ژنتیک فوق‌العاده‌ای دارد، خونش عالی است.
🔴
من طرفدار بزرگ خون هستم. من به خون باور دارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/146760" target="_blank">📅 22:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
عراقچی در تماس تلفنی با وزیر خارجۀ عربستان، دربارۀ آخرین تحولات منطقه گفت‌وگو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/146759" target="_blank">📅 22:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا از اعمال تحریم‌های جدید مرتبط با ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/146758" target="_blank">📅 22:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرده است که بیش از ۱۱۰۰ تن مواد منفجره برای تخریب زیرساخت‌های تونل‌های واقع در زیر منطقه "علی طاهر" در جنوب لبنان استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/146757" target="_blank">📅 22:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB3vvhKMP3Hd8gI5Ex081YcPcr52f98mlz37QrblTvfikLUh71L8u9DhN-x1AmJ9w8sdRlc5IaEpwrtl5D-xs-LX1zOMFMSYQx6CH6mcw9QC9znbTBkCdkPypHavm4fV5jfRpr2dm9nm97MQ7QBzh-fvObIM_q-V11GrSYnmw-GoWKN7tLpJ-yKpmUPpOUdGhe5RrFuDAYgNwwJTGGU3Itelh9kesDoeP3c4Qu7fE0UpM4QHCxoYO_ItOGmEoQXbqBh_Jiu3PwM7VhhkL8HpHd9-4OJsWp4p_FIWkRuAXdoDDANZtWcI3rceBw63XUq9qP0aVdD3yJLSRpx197m3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مصطفی نجفی: به نظر می رسد حمله سنگینی علیه تاسیسات هسته ای در پیش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/146756" target="_blank">📅 22:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/نتانیاهو: نیروهای ما عملیات خود را در تپه علی الطاهر در جنوب لبنان آغاز کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/146755" target="_blank">📅 22:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69ef09a20.mp4?token=eHdhy4a1WE7b5UQ3alT4c4bZr_-sndzumWrO_GcbFS-01-qbh5tQrKi6o_bT-l784E9IHU4-flvLnV8c55cCGhQKHbSrKBEtrVCGuFSpGhTqMhqEWyz1RqM4qcwWsNK5vW_YJ0jTdl0FmrWxBn9JnNQRi1xuo0QTSO6ZOZ-IKN2IDploAodMDK_OfweiiRfvXU3OrzXSBGtamWqleEYe0e-U4H2QJqXugradb5DA7YlejErzgeIwp0-T6HJdcENxRwWdbY9tT7-J-0wnnUT46iHIDIJosvui-AEpSpIGdKEIarwWGnn35sEyPDDrXgkPuQnnDw0Fhubaqfba_TKRVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69ef09a20.mp4?token=eHdhy4a1WE7b5UQ3alT4c4bZr_-sndzumWrO_GcbFS-01-qbh5tQrKi6o_bT-l784E9IHU4-flvLnV8c55cCGhQKHbSrKBEtrVCGuFSpGhTqMhqEWyz1RqM4qcwWsNK5vW_YJ0jTdl0FmrWxBn9JnNQRi1xuo0QTSO6ZOZ-IKN2IDploAodMDK_OfweiiRfvXU3OrzXSBGtamWqleEYe0e-U4H2QJqXugradb5DA7YlejErzgeIwp0-T6HJdcENxRwWdbY9tT7-J-0wnnUT46iHIDIJosvui-AEpSpIGdKEIarwWGnn35sEyPDDrXgkPuQnnDw0Fhubaqfba_TKRVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرده است که بیش از ۱۱۰۰ تن مواد منفجره برای تخریب زیرساخت‌های تونل‌های واقع در زیر منطقه "علی طاهر" در جنوب لبنان استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/146754" target="_blank">📅 22:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146752">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=BwWFcZ8Jly5W0geahYfUQySWN6jR2Uys7Ack5MLYrouL9zzNp8sZkFO4Hq55jqkppr7_rNMY_VMHL3y7_CYmUA6fEFRlhGMEdpwmmlKlzCVSc9k7Q3yXADfpj0B0LzteE9NoqQdSwzs80Sx8CPC8-Mos9EJEngNvLf_DAs8wZeVvZd6rcHxSa7EkUQ9mRU--AfwUSdv0b2muXqOcGf3KE0rQhvv7bnJj42vF97BAvjE2M0ec0_hufpAg_6KqxtleQlpo-d8R0dMM-jqUlMKne-swRFxTUBZ6y4To2wtTdtp8XyDIpWdhIK4tv8NQOiuxd-YsYwg_gwmonQQ-429_vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=BwWFcZ8Jly5W0geahYfUQySWN6jR2Uys7Ack5MLYrouL9zzNp8sZkFO4Hq55jqkppr7_rNMY_VMHL3y7_CYmUA6fEFRlhGMEdpwmmlKlzCVSc9k7Q3yXADfpj0B0LzteE9NoqQdSwzs80Sx8CPC8-Mos9EJEngNvLf_DAs8wZeVvZd6rcHxSa7EkUQ9mRU--AfwUSdv0b2muXqOcGf3KE0rQhvv7bnJj42vF97BAvjE2M0ec0_hufpAg_6KqxtleQlpo-d8R0dMM-jqUlMKne-swRFxTUBZ6y4To2wtTdtp8XyDIpWdhIK4tv8NQOiuxd-YsYwg_gwmonQQ-429_vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / تصاویری نشان می‌دهد که نیروهای اسرائیلی چند لحظه پیش تونل‌های زیر کوه "علی الطاهر" در جنوب لبنان را منفجر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/146752" target="_blank">📅 21:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146751">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پزشکیان فردا به هند می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/146751" target="_blank">📅 21:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146750">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری بیا اینجا بهت میگه دلار و طلا رو کی بخری و بفروشی
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/146750" target="_blank">📅 21:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146749">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-bprtzMkeCIj3QYPU9SmwnYWp_Qh4cGDTZY9gCwqr7niuiWZHcNAYGKZb1YgjLV95n-785ZA09dZF2RtmxorMAF0vJ-K1atkimpcNCTxpRVAO26xGLrdHlnK9RHxPXWH9Hr4dczfypZ1hDfhCyKDld3HL6mZ6QI9ZEqujOuSBpVQRRqmwqQtPkRdl6tpSsPY-oUAQV1POqUx7MAR3Keqn0Ro21myVAgEYoWhK-EWLlso_kLWd-WCmigjjSl7oue00lE_ryfocI0ogz7r1Twm3fu7LyISbIqgPu1mXnUYEh6AFlHEw8dNHt6ffyTL6IiV2ffdCxzMBxkBxTaI1kcQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجید شاکری (مشاور سابق اقتصادی قالیباف): فروش نفت ایران رکورد سال قبل و همچنین کشورهای همسایه را زده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/146749" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146748">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
در آستانه بیست‌وپنجمین سالگرد حملات 11 سپتامبر، 2977 پهپاد نورافکن شامگاه چهارشنبه بر فراز بندر نیویورک به پرواز درآمده و با شکل‌گیری تدریجی در آسمان و نمایش نور تصویری از برج‌های دوقلوی مرکز تجارت جهانی را در خاطره‌ها بازسازی کردند.
🔴
هر نور نمادی از یکی از قربانیان حملات سال 2001 بود.
🔴
در حملات 11 سپتامبر 2001، 2977 نفر از 90 کشور جان خود را از دست دادند. از این میان 2753 نفر در نیویورک، 184 نفر در پنتاگون و 40 نفر در پرواز شماره 93 کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/146748" target="_blank">📅 21:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر نیرو: در حال حاضر اتصال شبکه برق ایران به کشور‌های پاکستان، افغانستان، ترکمنستان، آذربایجان، ارمنستان، ترکیه و عراق با موفقیت برقرار شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/146747" target="_blank">📅 21:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146746">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/ترامپ به نیوزنیشن:
اتش بس با این رژیم برای من تمام شده انها آشغال و تفاله هستند
🔴
پایان رژیم ایران نزدیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/146746" target="_blank">📅 21:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فیلد مارشال رضایی:  اقدامات سیاسی و مخرب آژانس بین‌المللی انرژی اتمی، کشورها را به‌سمت خروج از NPT سوق خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/146745" target="_blank">📅 21:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
آخرین قیمت نفت: ۱۰۷.۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/146744" target="_blank">📅 21:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=nQ-xSUQwlPqwK7C8jT6T7sMP8imqORy26pkIvzvBFaJq3PBhb_3Re7A9HhgvMdvMtYzPiOGkbE_aJ-z9AXsxZwAKqXoTWPZKGdnLRGaSG96ER-G01xU19sCtkNeC3on2MjBiNRCyMeNTaS5R6nx3tWvyvKFF04-8RpsUDEhZNZYYXo2YHDoCIsCJiqpFodIcwS8alDYxRYSAtnEmiA4YCWjeKUCDiVUSUal1zTftk8v7msnSJZoY7lc_uFB84OYombws3wo6hGXGGjukzKYvejSt4b8xpQAzO7d1P0PVFYmwFP6Ey1dzrnC0ei530jvDBgAtk_iC4qHhYP9osv902w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=nQ-xSUQwlPqwK7C8jT6T7sMP8imqORy26pkIvzvBFaJq3PBhb_3Re7A9HhgvMdvMtYzPiOGkbE_aJ-z9AXsxZwAKqXoTWPZKGdnLRGaSG96ER-G01xU19sCtkNeC3on2MjBiNRCyMeNTaS5R6nx3tWvyvKFF04-8RpsUDEhZNZYYXo2YHDoCIsCJiqpFodIcwS8alDYxRYSAtnEmiA4YCWjeKUCDiVUSUal1zTftk8v7msnSJZoY7lc_uFB84OYombws3wo6hGXGGjukzKYvejSt4b8xpQAzO7d1P0PVFYmwFP6Ey1dzrnC0ei530jvDBgAtk_iC4qHhYP9osv902w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: رئیس‌جمهور ترامپ امشب اعلام کرد که ایران در حال تسلیح مجدد خود با سلاح‌های هسته‌ای است. این درست است.
🔴
پس از آنکه توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را ویران کردیم، دوباره در حال تلاش هستند.
🔴
من اینجا، در کنار دیوار غربی، پیش از ریش هاشانا به شما اطمینان می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران سلاح هسته‌ای نخواهد داشت.
🔴
همزمان، ما به محور ایران ضربه می‌زنیم؛ نه تنها به شدت در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات بوفورت را ویران کردیم و اکنون با ارتفاعات علی طاهر در حال مقابله هستیم.
🔴
چیزهای بیشتری در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/146743" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز: ایران و چین با یک سازوکار پنهان تحریم‌ها را دور می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/146742" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) تصاویری را منتشر کرد که بقایای یک پهپاد شناسایی و رزمی ساخت عربستان سعودی را نشان می‌دهد که امروز صبح بر فراز استان حجه سرنگون شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/146741" target="_blank">📅 20:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه تلویزیونی ۱۳ اسرائیل گفت: ایران در حال برنامه‌ریزی برای یک "حمله بزرگ" است که اسرائیل را نیز در بر می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/146740" target="_blank">📅 20:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: هیچ هواپیمای نظامی آمریکایی در حمله ایران به پایگاه هوایی در اردن آسیب ندیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/146739" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سپاه: تنگۀ هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/146738" target="_blank">📅 20:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
جابه‌جایی بالگردهای آسیب دیده آمریکایی در اردن
🔴
فیلمی از چهار بالگرد آسیب‌دیده بلک هاوک که از پایگاه هوایی موقر السلطی منتقل می‌شوند، در اردن در حال پخش است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/146737" target="_blank">📅 20:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIL8qlb4L4IhwQud_V6MftcOdBJZd2fOA_vbXbMEWWPAs9M9JFBc_w0Zb0_bmanvmRqVpgNwKSRefVNGhwoPFtvZ5RclNRT7Bn-MoHg8acMJKeJ072OI4zuDUeMA1Q9Ohr-84w37O_KoP5xUE6RzroIxYjWvaJYSIXlmlfWnoDyPsR80jvfJmsHu-1uUHzFUHXdeq7-Y0YCnDHN1IXzNiUxnajamdYYAVgctY3475_46smh4bg5QNR3o6Xyh_wlbIhnui1BR9_0BEyyksf0St6zHEBKtHHhQKBD2hha0jQqPvCr0nJ1SDEaLdmgiJ7NAQK3iit-E0-YOMOQ0A-Dd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c03d5ceb.mp4?token=aCsrPC6Ru5TgWV1FAkIdrlNjgHguVLRVv0yyZfn8CJbNzU6eBBrvPq3VvaTthAZW0O_JoShODvj_bGpcR7yB09qsc3xBAUTBAjYotq5Jbt8x6r46COZcBecLa4ALeYqDkHqpXm32REuNo-C8RGp0iSG-heMa8Heu-bYI0-T1R0ORePF16zwTOEq6f6lQlMQkFpqk3p6WMRGvg1NUy_WiTvgv4moVdB4VLaLpGaEsmB3csbRgdh2Zy0eWOMXcZeR1GtTH1czjggVBqxts0nhwl6hmUT2Pi9jZxIFpwtc6q8TJ2b-_1Yuuu7cx8UCKVlS_dPre_K2aWZsXxS4R76MxKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c03d5ceb.mp4?token=aCsrPC6Ru5TgWV1FAkIdrlNjgHguVLRVv0yyZfn8CJbNzU6eBBrvPq3VvaTthAZW0O_JoShODvj_bGpcR7yB09qsc3xBAUTBAjYotq5Jbt8x6r46COZcBecLa4ALeYqDkHqpXm32REuNo-C8RGp0iSG-heMa8Heu-bYI0-T1R0ORePF16zwTOEq6f6lQlMQkFpqk3p6WMRGvg1NUy_WiTvgv4moVdB4VLaLpGaEsmB3csbRgdh2Zy0eWOMXcZeR1GtTH1czjggVBqxts0nhwl6hmUT2Pi9jZxIFpwtc6q8TJ2b-_1Yuuu7cx8UCKVlS_dPre_K2aWZsXxS4R76MxKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از انهدام شمپاد ارتش آمریکا در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146735" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رمضانی، مدیر توزیع نیرو: مردم کرسی بخرن، شاید به قطعی گاز بخوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/146734" target="_blank">📅 20:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGYKuuBT2rvfBxaO4I6D1IVWvJLiDY1Lw-QrFR1Bi8fVkWrYcpe_IjPUlcyFG4j0cgI-BGj8kRDFKjMywJIKSgDP2RCwsFSzpQkP3pOzXQI5npoL4KK_2uo3oLxXvGmyqAClNRI9A1iar7RvfMn8LwHh3NY1gCdugRq1lN-RVqPgWyWv5Am3eR6g-tEtZ_cgIhMW_3fK704JHsjLPnCiDxj4ewHkT7JBszV7Zlo6zlxmzEYBgCXNawXaENFkEFrOeLk4dh25JlTvL4M8Y1Lljb80LzyNHuAozsmv_RdUxAJx2Oc9xs4QT7MrGCY7VaIbGEpfvqju0wBzNe6M_aYAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل به تونلی در شهر حاریس در لبنان حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/146733" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وال‌استریت ژورنال: جنگ با ایران ممکن است تا پایان دوره ترامپ ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/146732" target="_blank">📅 20:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران بار دیگر تولید موشک‌های بالستیک را از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/146731" target="_blank">📅 20:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نفت ۱۰۷ دلار هم رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/146730" target="_blank">📅 20:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e2184c3e.mp4?token=a66_Cw_CF3mPNta7g0YEclmlMtstQ11-n9XyH0nTf8rt1pRD9PdDand1jpID9AogjNSXcM1_mEEBBQzeRL6YAiJ1wq6h8uTu8lGq9I-ROMxV5dAw_BeQDuIuwoWrmWpFMQ0ITOccJFK34osl5EjRZCAarLPz9EClZF-eVJrJRrl7YwrIDm4lsEqivYKXxpWGqxSNS2nrZAbNoeuT_jUO_gFx54EZOpAZ5omOr8r-N2SEBaWL6mvCf_QhJFiz4drTS8rjFHXeZBc2b0A4vVcJduwYYXlQmVXqJBZOk6ETffrKWvYTuMsdeM5uyQ_bnBj187hpxSFJlx-_j9E0pQIGsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e2184c3e.mp4?token=a66_Cw_CF3mPNta7g0YEclmlMtstQ11-n9XyH0nTf8rt1pRD9PdDand1jpID9AogjNSXcM1_mEEBBQzeRL6YAiJ1wq6h8uTu8lGq9I-ROMxV5dAw_BeQDuIuwoWrmWpFMQ0ITOccJFK34osl5EjRZCAarLPz9EClZF-eVJrJRrl7YwrIDm4lsEqivYKXxpWGqxSNS2nrZAbNoeuT_jUO_gFx54EZOpAZ5omOr8r-N2SEBaWL6mvCf_QhJFiz4drTS8rjFHXeZBc2b0A4vVcJduwYYXlQmVXqJBZOk6ETffrKWvYTuMsdeM5uyQ_bnBj187hpxSFJlx-_j9E0pQIGsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جنگنده F-15J ژاپنی پس از بروز یک مشکل فنی، در پایگاه هوایی ناهای واقع در جزیره اوکیناوا فرود اضطراری انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/146729" target="_blank">📅 20:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/146728" target="_blank">📅 19:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
کاظمی: نمیزاریم دشمن مدارس رو غیر حضوری کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/146727" target="_blank">📅 19:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که نیروی هوایی سلطنتی عربستان سعودی در ۲۴ ساعت گذشته، ۶۴ حمله هوایی را در مناطق تایز، حدیده، مریب و الجوف انجام داده است. در این حملات از جنگنده‌های F-15 و تایفون استفاده شده که از پایگاه‌های هوایی شاه فهد و شاه خالد عملیات خود را آغاز کرده‌اند.
🔴
آنها همچنین اعلام کردند که نیروهایشان یک گروه از جنگنده‌های سعودی را در آسمان تایز با استفاده از موشک‌های پدافند هوایی تولید داخل رهگیری کرده و مجبور به عقب‌نشینی آن‌ها کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/146726" target="_blank">📅 19:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای آمریکایی مسیر ۹۷ کشتی تجاری را برای اعمال محاصره بنادر ایران تغییر داده‌اند، در حالی که به بیش از ۵۰ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/146725" target="_blank">📅 19:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBPh5uIH_skxMiNl3jDTSRBe3P6juJRMY08TWOH3zTK2RY6Kq1Bd05y9v3dbMwm0GZjve09r-nrjPgkKhZGdGQVLoQKW8dee-HBzvf4V11QNePTdKl5N8EcnHAah4twYPc7CJd_fYP_pb_5u79ZSRrDTHHGlrEn0T4SArgxmsMA1RjKkigeLuALscv00C9C-FeNcm8BRHlfwYns2ZIdWHWQtNeYoBIOToTOZbEICk1I1kTyOX28zza94GOthv-WU7LVPMZR7eox8ChfJ7uC9oaUo25rSJ2Fp3oFARjJ7s7k-vxTnzPa7w78PQduTRK5JzcT_zIFMMm_PnCWyGkhSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به 106 دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/146724" target="_blank">📅 19:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6QXIecbH_DdEDYegfMH9V1S_1JtbQUgyuaU0ftpHAZRNccdNGxz3SKJmc1Gkjn6D-gy6859zXXvzLfEwBF1ogJUpWe-5J0U8mE5qLO3b3IrKRpp0uFmWq-_8lT5IUx8VZSA2RJ9sxlGBrmhWW7_ZRjK6pqqhN8sPmd_6jdtNdfuPBpGQGGRZ1QSWrd9rekCAUHluXoYiVbEiDh7Qgjxgm11yuU7uVEbbeDseZ1NaD3ZSPVyMvzGHJ3iW8C2nj7r6G1fNYdu2zcPbebwdO6bQFBDA2JrvHdw7mq3j0iczN7EXANmtVJJi419JqQkYxAebGykfUyulnY4GPU-5xVDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه سعودی الحدث نیز اعتراف کرد جزیره استراتژیک پریم به کنترل انصارالله درآمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/146723" target="_blank">📅 19:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزارت دفاع: به زودی گوشه‌ای از کوه‌ یخ صنایع دفاعی ایران را می‌بینید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/146722" target="_blank">📅 19:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
هیلاری کلینتون درباره اسرائیل:
من اسرائیل را دوست دارم و از دولت و سیاست‌های نتانیاهو متنفرم. من آمریکا را دوست دارم و از دولت و سیاست‌های ترامپ متنفرم...
🔴
این خبر تکان‌دهنده در رسانه‌های اسرائیلی منتشر شد، جایی که نتانیاهو به طور مستقیم از سوی محمد بن زاید آل نهیان از امارات متحده عربی تماس گرفته شده بود و به او هشدار داده شده بود که حماس در حال برنامه‌ریزی برای انجام عملیاتی است [چند روز قبل از ۷ اکتبر]. و یا او به این هشدار توجه نکرد، یا می‌خواست ببیند که آن‌ها چه برنامه‌ای دارند تا بعداً بتواند به شدت واکنش نشان دهد و این امر موقعیت او را تقویت کند.
🔴
این یک شکست در رهبری بود.
🔴
اگر مردم اسرائیل بخواهند دوباره به این [دولت] رای دهند، به نظر من ایالات متحده باید موضع بسیار قاطعی اتخاذ کند. من فکر می‌کنم که می‌توانیم با یک دولت جدید همکاری کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146721" target="_blank">📅 19:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146720">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نماینده چین در شورای امنیت: درگیری در خاورمیانه باید از طریق گفت‌وگو متوقف شود.
🔴
باید به اجرای تفاهم‌نامه میان واشنگتن و تهران بازگشت
🔴
ایالات متحده باید استفاده از زور را متوقف کرده و به مسیر دیپلماسی با ایران بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/146720" target="_blank">📅 19:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146719">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/55de3b7b3f.mp4?token=LfgpN_A478OnRXj_gwkaV7KqCiLsFKhTiBQQTMTxtaHM-ZspOP3a15tXuZrDTfzIiZ0A2NAYj4vXWNZXp-J7K6iJFkpGrFwakM-D-ImPMcgoqgBtkdO-dLbJtgOziAM5Wba-1ssilP8sImaeqbMCtn5izmEL8D-e0xwljuSXOEmPW5ugRxjrHsuEhsJiuEsHxxg4eMvRekiB8xFGtOrGB0kEPM-2RFNPQLU2vXLP6Gf5Xp-KmCJkiun35n2Ys3Nx7Lhs-gN-XEFgoftXXTHI-yJjuj1hlKhmX7GAh7B_pCtFtxOhstoBKHuuvzaCW05suj7lK6nqxxHVayR30REeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/55de3b7b3f.mp4?token=LfgpN_A478OnRXj_gwkaV7KqCiLsFKhTiBQQTMTxtaHM-ZspOP3a15tXuZrDTfzIiZ0A2NAYj4vXWNZXp-J7K6iJFkpGrFwakM-D-ImPMcgoqgBtkdO-dLbJtgOziAM5Wba-1ssilP8sImaeqbMCtn5izmEL8D-e0xwljuSXOEmPW5ugRxjrHsuEhsJiuEsHxxg4eMvRekiB8xFGtOrGB0kEPM-2RFNPQLU2vXLP6Gf5Xp-KmCJkiun35n2Ys3Nx7Lhs-gN-XEFgoftXXTHI-yJjuj1hlKhmX7GAh7B_pCtFtxOhstoBKHuuvzaCW05suj7lK6nqxxHVayR30REeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده دانمارک در نشست شورای امنیت سازمان ملل با موضوع ایران: ایران باید به‌طور کامل از قطعنامه‌های شورای امنیت تبعیت کند، از حمله به کشورهای منطقه خودداری کرده و از هر اقدامی که آزادی کشتیرانی را تضعیف می‌کند، پرهیز کند.
🔴
وضعیت تنگه هرمز تنها یک چالش منطقه‌ای نیست، بلکه مسیرهای حیاتی جهانی را نیز تحت تأثیر قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/146719" target="_blank">📅 19:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابعی گزارش داد، از آنجایی که جنگ علیه ایران توانایی قطر را در تأمین گاز مشتریانش به شدت محدود کرده است، دوحه در حال مذاکره برای عقد قراردادهای بلندمدت خرید گاز طبیعی مایع از تأمین‌کنندگان آمریکایی است
🔴
طبق گزارش این رسانه آمریکایی، شرکت دولتی «قطر انرژی» به دریافت محموله از پایانه‌های صادراتی فعال و در حال ساخت آمریکا علاقه‌مند است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/146718" target="_blank">📅 18:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8527590cc0.mp4?token=Gg1SmN-G_fHN-sDPwwyy6HXaxQEmkS3qria4vfGZ6g22feJ7DZ0J2g4xOci4bpzrBV5SqRln7bUro8SPbiQhv4Uk7MMazy6QCiriIEC0Vm0kAfKXu1g6qe_Odw-2t-wIysaN6SmYSt-LqYpbbnm6LmyXIkkl2snfM7rEwfTR5BnUVK-02VTKdx-fqHDUypajF34tfybmXXLjV0OTH-Tt0tMkwmqSJlMQQbg9sW4csCkJ4pmQg1LbSdEu1lth_Ilgfodc2O5FMcpk-jtTvzD1JuUOc8Nvv2aFiNP48oIxODm_3tkMZSUs0Yll8X_B6W7K02DCukd2r4klitU91Pk1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8527590cc0.mp4?token=Gg1SmN-G_fHN-sDPwwyy6HXaxQEmkS3qria4vfGZ6g22feJ7DZ0J2g4xOci4bpzrBV5SqRln7bUro8SPbiQhv4Uk7MMazy6QCiriIEC0Vm0kAfKXu1g6qe_Odw-2t-wIysaN6SmYSt-LqYpbbnm6LmyXIkkl2snfM7rEwfTR5BnUVK-02VTKdx-fqHDUypajF34tfybmXXLjV0OTH-Tt0tMkwmqSJlMQQbg9sW4csCkJ4pmQg1LbSdEu1lth_Ilgfodc2O5FMcpk-jtTvzD1JuUOc8Nvv2aFiNP48oIxODm_3tkMZSUs0Yll8X_B6W7K02DCukd2r4klitU91Pk1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیلاری کلینتون: ما باید به خطرات بالقوه خود توجه کنیم، به ویژه به این که شی جین‌پینگ چه فکری می‌کند: می‌دانید، "آنها دیگر نمی‌توانند از کسی محافظت کنند، زیرا توانایی دفاع از خود را ندارند. شاید بتوانیم تایوان را وادار کنیم که به سادگی تسلیم شود، زیرا هیچ حمایتی وجود نخواهد داشت."
🔴
منظورم این است که اگر به نقشه جهان نگاه کنید، وضعیت برای ایالات متحده مناسب نیست، و من معتقدم که این تا حد زیادی به دلیل تصمیمات بسیار اشتباهی است که توسط این دولت گرفته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/146717" target="_blank">📅 18:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146716">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نماینده پاکستان: دیپلماسی و گفت‌وگو باید اصول راهنما برای حل موضوع هسته‌ای ایران باقی بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/146716" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
روسیه در شورای امنیت: اجازه بازگشت تحریم‌ها علیه ایران را نخواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/146715" target="_blank">📅 18:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146714">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e130fadb40.mp4?token=A6Va2rVY-_wYU1m3KU0hx99S4i38roG4RE4iRePLZDQq5vAGHcq8ZrdDhPXkXYWdm8DAbLfyJpf1NUTru2W06YIRCcl3fI5sgT9VF14BnaTC_UYIVfXPPiSK4fXoe8T_f_PlWG_8cMnYCilJCu7p8Mw-JjYh5e11tTEXM0WSDBxqtLBhlqzPhVkfFeWM0AlCE8Qe6lh6YCcBiodXMf7M3eeWZIqcFYLc_43xZ3CHwasZjIOxEQVycTrU3dCmv6oSrz2A6OfmFN8rpZEPhryVZPdhpha5T-VFAsuGBHz12Q3A5Nl8k7_W4Jp01eBJ5g3LbhqvGw_jjCitwTq30nWjVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e130fadb40.mp4?token=A6Va2rVY-_wYU1m3KU0hx99S4i38roG4RE4iRePLZDQq5vAGHcq8ZrdDhPXkXYWdm8DAbLfyJpf1NUTru2W06YIRCcl3fI5sgT9VF14BnaTC_UYIVfXPPiSK4fXoe8T_f_PlWG_8cMnYCilJCu7p8Mw-JjYh5e11tTEXM0WSDBxqtLBhlqzPhVkfFeWM0AlCE8Qe6lh6YCcBiodXMf7M3eeWZIqcFYLc_43xZ3CHwasZjIOxEQVycTrU3dCmv6oSrz2A6OfmFN8rpZEPhryVZPdhpha5T-VFAsuGBHz12Q3A5Nl8k7_W4Jp01eBJ5g3LbhqvGw_jjCitwTq30nWjVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای ائتلاف "جنوب غول" همچنان دسترسی به شهر عدن را مسدود کرده‌اند و نیروهای مورد حمایت عربستان سعودی را در جاده‌ها به دام انداخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/146714" target="_blank">📅 18:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
الحدث: روسیه و چین مخالفت خود را با بررسی تحریم‌های ایران در شورای امنیت اعلام کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/146713" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دبیرکل ناتو: مین‌روبی در تنگۀ هرمز به ما مربوط نمی‌شود
🔴
موضوع مین‌روبی در تنگه به قلمروی ناتو مربوط نمی‌شود. البته ما آنچه درحال وقوع است را زیر نظر داریم و کشورهای عضو ناتو از نزدیک با یکدیگر هماهنگ هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/146712" target="_blank">📅 18:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
تسنیم: تنگه باب‌المندب به تسخیر رزمندگان یمن درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/146711" target="_blank">📅 18:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146710">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نماینده بریتانیا در شورای امنیت: برنامه هسته‌ای ایران منبع نگرانی و تهدیدی برای امنیت بین‌المللی است. ایران تشدید تنش را انتخاب کرده، برنامه هسته‌ای خود را گسترش داده و بیش از 400 کیلوگرم اورانیوم در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/146710" target="_blank">📅 18:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146709">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npKPVLgZVbplRBqOP4-1yaXM0q20_c7MkD4_vHT07sEyK6A4wTV0Xmxic_R3frC25ptNoee5gdbmVBmHrnE8v13ODXR4mCGKGmNbn-8EI8FXf6q98HSeKlk7UEOTSa_JXPGylYghBPTIVdEfKF8Nm4F3weSeGIzFml9PMioHcsu4gAAleNAuDe7o2h6A9sv9p9te5eV3-IKAQY60FB9SNit051VoVCxPql4qn1E6Z4KlzbryYwsHqI_7mndcpX7n8n1lu50QXkflNz0-8Jrqz-Na4BJRDv52pdmN_f71TP1vw_Ue7CyIKaMf9xA4QOKUTg6TlDbfdIxw36z0pTCnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدیدترین تصویر از جنتی که امروز منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/146709" target="_blank">📅 18:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146708">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نماینده بریتانیا در شورای امنیت: ایران با آژانس بین‌المللی انرژی اتمی همکاری نکرده است.
🔴
نماینده یونان در شوراى امنيت: از ایران می‌خواهیم در مورد برنامه هسته‌ای خود با آژانس بین‌المللی انرژی اتمی همکاری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/146708" target="_blank">📅 18:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146707">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d44c8477f.mp4?token=E2gX5Z6thcRVqPHswh-czuHc86s6PETd86VD3s70fMODlnWrzlbWhSIwDk-Ga4ZWKfFJz_1PU_u82sWLXbdxA8cf9G04Nel_1buwRA8VLybvV3_nS_sAAUeTMBDc-W2cOfev3rpS3MavB10VAxrzJs96GCiYOC5IR6sAiCTSadL3xQUD9Top78R0_wUmpRz6Uz0yLWcWMa9L7YkDpVYXpC4GTIxKUfPU3LIG42D2SrefBXvD-OnfD2mDEANOqOq9vvIhGsQxccqMkmdLtDQW70P6XEAnkPB64XMo1DiEZUsYzxPeoE0kaZIc7gN7-5F3WPsWJrOBlKZF5pyY3cXyTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d44c8477f.mp4?token=E2gX5Z6thcRVqPHswh-czuHc86s6PETd86VD3s70fMODlnWrzlbWhSIwDk-Ga4ZWKfFJz_1PU_u82sWLXbdxA8cf9G04Nel_1buwRA8VLybvV3_nS_sAAUeTMBDc-W2cOfev3rpS3MavB10VAxrzJs96GCiYOC5IR6sAiCTSadL3xQUD9Top78R0_wUmpRz6Uz0yLWcWMa9L7YkDpVYXpC4GTIxKUfPU3LIG42D2SrefBXvD-OnfD2mDEANOqOq9vvIhGsQxccqMkmdLtDQW70P6XEAnkPB64XMo1DiEZUsYzxPeoE0kaZIc7gN7-5F3WPsWJrOBlKZF5pyY3cXyTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده بحرین در نشست شورای امنیت سازمان ملل با موضوع ایران: حملات اخیر ایران به ما و کشورهای منطقه نشان‌دهنده عدم پایبندی این کشور به قوانین و حقوق بین‌الملل است و باید در برابر آن ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/146707" target="_blank">📅 18:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146706">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f588e43d4.mp4?token=rfkQ_REuzLxxcfDWZ1HwQsUz7_kBecd2ouWdn34mwPU1BplPAzm-tdzGg8CkEth5pP3HzPpcqog3MsysmTxFzPJQk652pDaeveSMr2hXJxMJ6CZuVM04hX09CGFGtUMmJXjkJKJGR5pz0jBTCiKs9XcZNxPZeg6K8hrxg-0MtyTZCZHoYq4ie2gnFxoTNBysiCjFNeIFg4YxonakvzwV9QWAjX9jtqYSgDrR2DAD-L9GNsg17Z_RgLtCTleNkNeC6-wuAieUlgiakOBcWM0GpPrMwX-Rcx2SQJff7kyXEcnTIdrMusH5AoQtD072ObmpiCLjdEhMYD34Uh8peB0usQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f588e43d4.mp4?token=rfkQ_REuzLxxcfDWZ1HwQsUz7_kBecd2ouWdn34mwPU1BplPAzm-tdzGg8CkEth5pP3HzPpcqog3MsysmTxFzPJQk652pDaeveSMr2hXJxMJ6CZuVM04hX09CGFGtUMmJXjkJKJGR5pz0jBTCiKs9XcZNxPZeg6K8hrxg-0MtyTZCZHoYq4ie2gnFxoTNBysiCjFNeIFg4YxonakvzwV9QWAjX9jtqYSgDrR2DAD-L9GNsg17Z_RgLtCTleNkNeC6-wuAieUlgiakOBcWM0GpPrMwX-Rcx2SQJff7kyXEcnTIdrMusH5AoQtD072ObmpiCLjdEhMYD34Uh8peB0usQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔴
11 تایید
🔴
2 مخالف (روسیه و چین)
🔴
2 ممتنع
🔴
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس قطعنامه نبود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/146706" target="_blank">📅 18:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نماینده آمریکا در نشست شورای امنیت سازمان ملل با موضوع ایران: ایالات متحده قویاً اظهارات چین و روسیه را رد می‌کند و از مواضع بریتانیا حمایت می‌کند.
🔴
سال گذشته این شورا تصمیم گرفت قطعنامه‌های تحریمی علیه ایران را بازگرداند و روند اجرای این تحریم‌ها را از…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/146705" target="_blank">📅 18:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146704">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20260b4433.mp4?token=R8GM554jVi8hf_wk3bG4uNd07sHvoPB-Xuxm2tgy5T6cPEowhBLcwTVeUGDbrkJ-ERg2E7QuRt0-fUeSiZYx8lPIevpPYdoRlTPrkuaMsofwmmpNIpq7Z2auyclbOh7ZPL-cVHdymMUk1gnSUAwLEzSg9uXPLpmLxZi-ePxD_txknvKFPJFFN84MGqAHCqg2-5J4DkRH-YhSORyorNX-2Q5RhXOfDXwPa1BkP5AIWQuQJ5dZL69DPnbOFjgrTOgBLhZ_r4xCSd2Q-sHwfyipYSRBRs07geFSplF3t6R6_taAhl6aXb4fIkXgHsQ95097iZRqk0kIqxwIQ9Unc-1tVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20260b4433.mp4?token=R8GM554jVi8hf_wk3bG4uNd07sHvoPB-Xuxm2tgy5T6cPEowhBLcwTVeUGDbrkJ-ERg2E7QuRt0-fUeSiZYx8lPIevpPYdoRlTPrkuaMsofwmmpNIpq7Z2auyclbOh7ZPL-cVHdymMUk1gnSUAwLEzSg9uXPLpmLxZi-ePxD_txknvKFPJFFN84MGqAHCqg2-5J4DkRH-YhSORyorNX-2Q5RhXOfDXwPa1BkP5AIWQuQJ5dZL69DPnbOFjgrTOgBLhZ_r4xCSd2Q-sHwfyipYSRBRs07geFSplF3t6R6_taAhl6aXb4fIkXgHsQ95097iZRqk0kIqxwIQ9Unc-1tVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده آمریکا در نشست شورای امنیت سازمان ملل با موضوع ایران: ایالات متحده قویاً اظهارات چین و روسیه را رد می‌کند و از مواضع بریتانیا حمایت می‌کند.
🔴
سال گذشته این شورا تصمیم گرفت قطعنامه‌های تحریمی علیه ایران را بازگرداند و روند اجرای این تحریم‌ها را از سر بگیرد.
🔴
امروز باید گزارش ۹۰ روزه ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است.
🔴
روسیه و چین می‌خواهند قطعنامه‌ها را نادیده بگیرند و با وتو کردن آنها از ایران دفاع کنند؛ آنها در حال نادیده گرفتن اصول بنیادی سازمان ملل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/146704" target="_blank">📅 18:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146703">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7af20ea1.mp4?token=KCkyFlVnq_mY_t4tozq9vpklCuT6oZjNM_nSbo9B6B5itDVZ9Z8ZZ_5Lzu7uYoBVyBwGYgu81TKzNrKQO6ByH9W3ipEpTFnr4iWBaiSDHaisl6GN0eiO9EbiBAXP8rhcxbRQkCoAH0i1S-hwlmjJl-jqQhuuyo4Yj9nO5ezUuETd0vqWA9SKySxYusfmbtRVm96PJ-J2Alfk4w-PkJel2uqDkubKBPyF4jIinDq_tJZjFVtNMRcOZ5Q2IJS-DdWsWcMomHn05DUdb20-aovbM8bZ6U2D-ovp9Qqb9LI7ftxWPNxYpOp6mwY3viKSeniUnNc1-JxA7G8oUo1C0tT3UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7af20ea1.mp4?token=KCkyFlVnq_mY_t4tozq9vpklCuT6oZjNM_nSbo9B6B5itDVZ9Z8ZZ_5Lzu7uYoBVyBwGYgu81TKzNrKQO6ByH9W3ipEpTFnr4iWBaiSDHaisl6GN0eiO9EbiBAXP8rhcxbRQkCoAH0i1S-hwlmjJl-jqQhuuyo4Yj9nO5ezUuETd0vqWA9SKySxYusfmbtRVm96PJ-J2Alfk4w-PkJel2uqDkubKBPyF4jIinDq_tJZjFVtNMRcOZ5Q2IJS-DdWsWcMomHn05DUdb20-aovbM8bZ6U2D-ovp9Qqb9LI7ftxWPNxYpOp6mwY3viKSeniUnNc1-JxA7G8oUo1C0tT3UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیلاری کلینتون درباره ایران
:
ما کسانی هستیم که ایران را تقویت می‌کنیم. آیا ما از آنچه در ۲۵ سال گذشته انجام داده‌ایم، هیچ چیز آموخته‌ایم؟
🔴
و من فکر می‌کنم ایران، نه فقط با تشویق بلکه با کمک هر دو چین و روسیه، بازی بسیار هوشمندانه‌ای برای کاهش توانایی ما در دفاع از خود و متحدانمان انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/146703" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
اسکات بسنت: ایران در حال حاضر به‌دلیل محاصره دونالد ترامپ و تحریم‌های فلج‌کننده خزانه داری آمریکا با پیامدهای سنگینی مواجه است
🔴
آمریکا کنترل کامل تنگه هرمز را در دست دارد، صادرات نفت ایران رو به کاهش است، صف‌های طولانی مقابل جایگاه‌های سوخت شکل گرفته و اوضاع هر روز بدتر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146702" target="_blank">📅 18:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
هم اکنون جلسه شورای امنیت سازمان ملل درباره برنامه هسته‌ای ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/146701" target="_blank">📅 17:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
👈
طرق گزارش مسافران: فرودگاه‌های ترکیه پذیرش محموله و باری که مقصد نهایی‌اش ایران اعلام شده را متوقف کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/146700" target="_blank">📅 17:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146699">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گروسی: نمی‌دانیم در کوه کلنگ چه می‌گذرد
🔴
مدیرکل آژانس بین‌المللی انرژی اتمی می‌گه از طریق تصاویر ماهواره‌ای فعالیت‌های هسته‌ای کوه کلنگ گزلا رو زیر نظر دارن، اما نمی‌دونن دقیقاً چه خبره.
🔴
از طریق تصاویر ماهواره‌ای فعالیت‌های هسته‌ای کوه کلنگ‌گزلا رو زیر نظر داریم ولی نمی‌دونیم چه چیزی داره رخ میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/146699" target="_blank">📅 17:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146698">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری/بلومبرگ:
آژانس انرژی اتمی وجود فعالیت هسته ای در سایت کوه کلنگ ایران را تأیید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/146698" target="_blank">📅 17:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146697">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع نظامی دولتی: حوثی‌های یمن به جزایر حنیش بزرگ و کوچک در دریای سرخ رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/146697" target="_blank">📅 17:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146696">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رئیس سابق سازمان جاسوسی بریتانیا:
فکر میکنم وضعیت کنونی با ایران چند ماه دیگر نیز ادامه یابد، اما فشارهای اقتصادی از مقطعی به بعد، آثار خود را بر ایران نشان خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/146696" target="_blank">📅 17:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146695">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فرماندهی جبهه داخلی اسرائیل: از سال نو لذت ببرید، اما برای هرگونه تشدید ناگهانی و غیرمنتظره وضعیت، آماده بمانید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146695" target="_blank">📅 16:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146694">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
در حال حاضر ۶ فروند هواپیمای سوخت‌رسان و یک فروند P-8A Poseidon در منطقه در حال پرواز هستند. شمار اعلام‌شده هواپیماهای سوخت‌رسان، شامل هواپیماهایی که در حال بازگشت از مأموریت‌های خود هستند نمی‌شود.
🔴
۵ فروند از هواپیماهای سوخت‌رسان متعلق به اسرائیل و یک فروند متعلق به قطر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/146694" target="_blank">📅 16:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146693">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1738045bd1.mp4?token=DibXEfzTI893zU1G1fEWn_Rrk4nAYCzw-YabQkrFXBxFpJv2cA4X-rnuLLCINMG-QTW8JnqWQ5dR2umhU95un1Vx3JXwpfOrD1OmgdOaOyJ2HNJ0WyBjYh0grPLMaoK9kGy9ceKGnpSmAJJOTo_hn1Rk42acBecochZCnRvPnsF7q-Az_FcVxRqph3aDLW_cGndqlGYkSceGYub_HS9Lct3CGkRTX_azvWeruXBC9B2IoKi7XemK0NqTgYbfnmMbQNGCVeOU0WtPNop2Sw3p5MNl2AVw42jldaZjsH9PmIPD5eSUZ2XC_yn1JllfILmCHi8Wi-0uwa059TLKCAjAaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1738045bd1.mp4?token=DibXEfzTI893zU1G1fEWn_Rrk4nAYCzw-YabQkrFXBxFpJv2cA4X-rnuLLCINMG-QTW8JnqWQ5dR2umhU95un1Vx3JXwpfOrD1OmgdOaOyJ2HNJ0WyBjYh0grPLMaoK9kGy9ceKGnpSmAJJOTo_hn1Rk42acBecochZCnRvPnsF7q-Az_FcVxRqph3aDLW_cGndqlGYkSceGYub_HS9Lct3CGkRTX_azvWeruXBC9B2IoKi7XemK0NqTgYbfnmMbQNGCVeOU0WtPNop2Sw3p5MNl2AVw42jldaZjsH9PmIPD5eSUZ2XC_yn1JllfILmCHi8Wi-0uwa059TLKCAjAaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها، پس از تصرف بندر المخا، تجهیزات نظامی متعلق به عربستان سعودی و امارات متحده عربی را به غنیمت گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/146693" target="_blank">📅 16:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146692">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69e8c3e218.mp4?token=j7DHdKBFlqsgGzuRiLh_3OdpIl7ymTd-oa7nvsjdnQzyC7ceB0DlLma47bjjzzuydK5etSg4YjzncxpKwE9_GSS0KRxDFHpWlaA4qCOSFAatTIMlfWKTYaf0T-1MW6SevmEZmvWdFLFgF5Yz2UdpPkdaJGpntY-M5lkDAjriwU07IAd58z5xjfdViNd_2egagGHQ3Wvvg-jRPD97Xn_YyCYNoW5pstDdVDXMDLmKqWYVHXfW-A7jeoi4lU9ezFDAe9gV6i8Dq4UnMzZI0GToU9PXP8mC1sqcyLLo0Za--4MoeJp9170LutgE-Mrwwh-LzrDvseadYw9XuFwJNUCc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69e8c3e218.mp4?token=j7DHdKBFlqsgGzuRiLh_3OdpIl7ymTd-oa7nvsjdnQzyC7ceB0DlLma47bjjzzuydK5etSg4YjzncxpKwE9_GSS0KRxDFHpWlaA4qCOSFAatTIMlfWKTYaf0T-1MW6SevmEZmvWdFLFgF5Yz2UdpPkdaJGpntY-M5lkDAjriwU07IAd58z5xjfdViNd_2egagGHQ3Wvvg-jRPD97Xn_YyCYNoW5pstDdVDXMDLmKqWYVHXfW-A7jeoi4lU9ezFDAe9gV6i8Dq4UnMzZI0GToU9PXP8mC1sqcyLLo0Za--4MoeJp9170LutgE-Mrwwh-LzrDvseadYw9XuFwJNUCc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو مربوط به آتیش گرفتن موتور یه پیک هست و یکی اون وسط داره بلندبلند شماره کارت پیک موتوری رو می‌خونه و مردم گوشی به‌دست دارن شماره رو می‌زنن که بهش کمک کنند موتور جدید بخره
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/146692" target="_blank">📅 16:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146691">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
آیا پاییز و زمستان قطعی برق خواهیم داشت؟
🔴
وزیر نیرو: از الان نمیشه پیش‌بینی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/146691" target="_blank">📅 16:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146690">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbO0QA1r1iG5uLhUiXSee39HNQn0QRXu8cxAnOw5x5lcM6yXZkJnijoUgC7SxTHdTuxzQa1B8fMKtAQAMYNuMY2df-Ioq3FKhJxl1EzOq97OrBHm7Dc6ZqUrJSGferI2p_CKFKI0gOFRPb8iq9SMkNMqj2CTSe6n4srf0-JO6E_sj2M_8EF8-5Mt471WfwYuSudFhmqNcmw19cUGpXCxVeN19CXw7LmHKznT4CIWmCoewlmR_PCJB9r_CXvq5x5A_QeVd8YvBOQhry_wF7_riXaNmqPvsUfRoq9GtAgNYmQDNyqxHr5qyNshWcOWA2tGoDp4QqfLvFaeIygsaYSZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه حمله هوایی اسرائیل
نبطیه الفوقا
در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/146690" target="_blank">📅 16:13 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
