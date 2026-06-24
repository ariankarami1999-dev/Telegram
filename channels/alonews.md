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
<img src="https://cdn4.telesco.pe/file/tdn0nNdQz1I-CRPn6gpL4ftYOHYtPunv4G84ObMTusyPIA4YKEfQs2t_CkkPj_bDR8O9lPJcotI3hyY219t-45s64ebtXNg2AbSICPhrp9E4lZfvz0hGPTDpcj-0mbriKuzbtvzlHoyA17VTchsYLFNA1kjh6kIgWk9SAP5y6-CC39pLAk6mUwEssv-ln6JqaTIcW7hw7mYEfYCSfm7of37GOErcym20yquEQHiRzkupaJUq8Z6InLkjz9vjjSHjDkQyXQn8_d61c31-GskcUv7n2Mm31dyhScHtppgiJRda2fQtiK4rm-UMzp7HPEA2PZe2FO0psAl7kELalLz-Eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 945K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 15:47:36</div>
<hr>

<div class="tg-post" id="msg-130002">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtntOif9EOaXLJL6PKYCRbb7rGaU10-ks1v94mqqBKl3B5vXyTSpg3HnxcsH2OKlIdqPdLMpAKhLqYcezXyLwwtM7AhOtJYFjmGv9q0LO4iz7Q4dKMEIq9pbNlOdZFH68B6YCtE_Pj_JKc3IfhsPj7RdhBHfJMJFqKE_-gZyhh8GvhugmNJs0PLJjKPW77G-GNwOPfU7I-UdPXLrF9URFOVOSA6-I8xhMg22ecTc_pemWmy8OHbYAcTmTkgizVxp-mdnBFx-hXXFyEEUNg0jirOh0rmg6dth1k6AMD5s7l0vLkRszoDtgKZP4_6M8CV-JaGk8EkbkhNm4Ow07tBNaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه پست گذاشته و از خودش بابت اینکه اجازه نداده ایران به سلاح هسته ای دست پیدا کنه تشکر کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/130002" target="_blank">📅 15:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130001">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5SQ61CNNRIhRMmnwgLxdl_oGaChJX8Na4To2ankEAbAEkT5puTzF9ObjAoikG3sYDs2w3PY2IXlrUICuI4Calx0CAqktk-hkFFKWcmXvkUV5JNIAynwpf1AdEkI7Cexg5a0wfnsSlkyY6hM1Oigy3rNWDlcYtDVsmH1UMyoDkKDHrGwm3KsE7hNOfZiIaPfmYd0JUUzEq3CQeh3RVlNx3kczP-r76Qg_nKmWo6yNKTMomJUkmph6E-TeJrDeKrTsiOKCBL13XYJ_DKSWvZjG8m_tfwOaEBnTN7zfNGmwjwjbjK4FntQgUmRqFWZOZiLEL26lHGBnSF37YZiP4YXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار قالیباف و الهام علی‌اف در باکو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/alonews/130001" target="_blank">📅 15:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130000">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر خارجه اسرائیل: مذاکرات جاری در واشینگتن میان اسرائیل و لبنان تاریخی و بسیار حائز اهمیت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/130000" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129999">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB3s8XmuhTsj95JVFdFYdYY_MaBevLyJcevE-1v2L-CLNtBVMmiAKN23_wJlUV2FKQfHUzTGMN1nCmG8TbyXhc5ymvL-vW9G_D2ipwvo2b97p1oJEit38Qnv98dADR84E4GQGk3bfzd1-akmdTnCSzAxBupWpzJHy7kSW6OGFC-sUWJH2M5-o8f7-PrgehIEUpkMC8fPTWyB4lRPsTugKnc_gzfyut-aMOVv4toPUroS-6-5GHtZpJEkfvJ5XrPp_zXfmCi_bMLPomHrPmr6Ih7mtWQezbp4b-jDV-4G2hj7YSmOJKt-EXtgaJHRy1s-qBR4UatNKrjfKM9UlSbMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران به آمریکا اطلاع داده است که برخلاف گزارش‌های دروغین اخبار جعلی، «هیچ عوارض گمرکی، هیچ حق بیمه و هیچ پرداخت دیگری از هر نوعی توسط ایران برای عبور کشتی‌ها از تنگه هرمز درخواست یا دریافت نمی‌شود»
🔴
اگر این اطلاعات نادرست باشد، مذاکرات فوراً متوقف…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/129999" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129998">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCIq6cAJ3h6XLKsuiDf8SBWgW-9MPUBz0h6qWUkF-wGbFbMcOpAX-VTMIUasWWbtbULECa4xRTsFjM6IuD_QacMhEUrGZFYJaYSpm8eqVkCcfsFKnuqWtgTIpJX3UPsTv3jrc_JgzZGym5JxMOTY6PGooUsCPZcwntlIMAXobBvwyCrzDAcBcq-XwZtkx0sC237t_iSn_NwfIJfMxjc1_GbA0Np0ixuHdejV4AvJQOguYhcofqEiW5gNaVuBv3QBt_g52dYIaEXUkpBBCjAyRwXIwYk3hztQLzEYcWyaV9WHAh90XfpM5Obl4AQ_TqgikLzNRqg8-AKk7YwE3WRq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
: ایران به آمریکا اطلاع داده است که برخلاف گزارش‌های دروغین اخبار جعلی، «هیچ عوارض گمرکی، هیچ حق بیمه و هیچ پرداخت دیگری از هر نوعی توسط ایران برای عبور کشتی‌ها از تنگه هرمز درخواست یا دریافت نمی‌شود»
🔴
اگر این اطلاعات نادرست باشد، مذاکرات فوراً متوقف خواهد شد! علاوه بر این، هیچ پولی به ایران منتقل نشده و هیچ منابعی از صندوق‌های آنها توسط آمریکا آزاد نشده است
🔴
ما بخشی از پول آنها را که کاملاً تحت کنترل ماست، به کشاورزان و دامداران خود اختصاص خواهیم داد تا ذرت، گندم، سویا و سایر مواد غذایی را خریداری کنند
🔴
ایران به شدت به غذا نیاز دارد و ما آن را صرفاً از ایالات متحده برای آنها خریداری خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/129998" target="_blank">📅 15:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129997">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XVVxMsd4TvWHnJjtfL3XJdzQIKlNRPtzdL-CnO-Ka01gHQe_oyts6gizuzdelgXtoPh47r4PxpFklXIuzzcwoiWdtJ-HNRWPUu3UAQ6fLbiliBZH6LjSi4CPJUltKjIX_4EPrIpdTEdG2q2tahNjXTowXhbAX24wwRZ26RVaePtFgjX2wqaX2Mqe9RPoQW1cZ7hf7VWb7fXgo6Q9FYF577HSOJTFcLlk54MYurSp8EMSQG9jRiaPBtXSGdqhMjrdGt-12Cec9s83yV-m0NlCoHTA9A6_c4ic9FdF6CNrU-6uTkULoH9SnO3ABg2FtTAy8IZXoiAaUa3nfLiE_e9Wyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مصاحبه وزیر میراث فرهنگی با خبرنگار اسپانیایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/129997" target="_blank">📅 15:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129996">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=rXBcpbkAM_HpbCEdtgcDDGhv2JgDfFr5W2W7pCh3SAaytXjCPykqQYSOFnrpDeVbaYbMkH2s4kP99GwpESK7GKRYQI7Cm8kE2qyDooTs7008MaocYHJxUhhY4hWInFok5xjK1hkj3DaW-Yn0E9xJxtmEhUDfIeK_8N-ouywe_aevM7TrNUdmhWsL3l38QH1IcWIC73P-g3zjeB9hWopuqiMKPBqoegL6azldp2Gm79yvYfFn4QMARO6-pPHZFVlRu5Ju2mGRyT7qNmfdP4eXORpgtVzvXdIx3KU0ZNF9Q4ZPv6KzBF7wjCqtJoRRACesOTbAxbNbWxx5UIWefSCxAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=rXBcpbkAM_HpbCEdtgcDDGhv2JgDfFr5W2W7pCh3SAaytXjCPykqQYSOFnrpDeVbaYbMkH2s4kP99GwpESK7GKRYQI7Cm8kE2qyDooTs7008MaocYHJxUhhY4hWInFok5xjK1hkj3DaW-Yn0E9xJxtmEhUDfIeK_8N-ouywe_aevM7TrNUdmhWsL3l38QH1IcWIC73P-g3zjeB9hWopuqiMKPBqoegL6azldp2Gm79yvYfFn4QMARO6-pPHZFVlRu5Ju2mGRyT7qNmfdP4eXORpgtVzvXdIx3KU0ZNF9Q4ZPv6KzBF7wjCqtJoRRACesOTbAxbNbWxx5UIWefSCxAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صداوسیما یه نماهنگِ سرطان پخش کرد؛
بعدش دیدن خیلی کسشر و آبرو بره، کلا گرفتن از آرشیو شبکه سه هم حذفش کردن
😂
😂
😂
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@AloSport</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/129996" target="_blank">📅 14:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsV2wQv3jqIthSyRkIQ4WWGJvrX0AKNVu2orpY6hfGL3uTbpjWoD9r2zlJxybyH5jELXGGxQ0klWhuezb5urLZE6P7rGJlsY36rVFfdQ3sS9WD7jaNbDIsY8l38ZEVI-kyxyWJU8u8vKCyo5BcDl8op_n18TA-hEgdGqWJ3i6ScBY3j8kdXYhk53s7vHFs4EMa7I7RlxZz67J2IJlhGxxlNmYGyBlNTl8FvODmx5tkTAJJqpLGqQ9IdrwIA9146CSVfsRdGc3F8p7XndWRBLPkjl_XLBjWowMqoPe1tDX8yRjkIl8J2atqmcbEaz1JTm5B1hl03cLOIVHA0kaCmVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن پالیسی:
توافق ایران زمینه درگیری‌های بیشتری را فراهم می‌کند
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129995" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129994">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/obbGf4LdyKfn-WCsT8tTbDJKi_iaOdGNaeK7OVhwG7JKgk29sC1R1wwTLEtZEs8EmLSGtACx1AUFB3M8K1wGPeBmKlfv_yKPLMJDOhD5uO_nItgWJgFznpRl14zTWBbojoTE3hfSykFCrUD9uuwwz3GxslugkYCrocqTg-pgYiOjwPgjJoao9ux3-zfn7hUm_4jKVnbmXnyEYhppc8xe9xNu-kX1b0eiX-MeSUrqUEuEMWQt912KDYRkZRo_Nxv72LF-DC2qhOsSbNfntQzAvBnMOamG6uMl4-cDQVBRIgtbyHJYry_6V4tJ3s6PZUD36dPYANwV2WsRHJxd7NVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا ایران ۱۰ فروند هواپیمای مسافربری بوئینگ ۷۷۷ به صورت دسته دوم از عربستان خریداری کرده
🔴
تصویر ماهواره‌ای ادعایی از اولین فروند تحویلی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129994" target="_blank">📅 14:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل:
حتی اگر واشنگتن از ما بخواهد، از جنوب لبنان عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/129993" target="_blank">📅 14:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5cIIoMrZ_vRciF2zaWeG19nmvd4P0k5uGGprShWnix29u5lZ__F47-3sBiz7LKzU7fZ4C3opIPhVnAyr7FzW78NKzIiMXFxopslcG5KCvO_B3txYJoE27mv9mXqNEKFuQv9JD0URId8oTPAwjXD5GeJzdhWM_rKvA4VbU_Gz9AVyCI8NqgasxkTelGtSwwZQ_2VRnGp6WMnxBCsvFcz3axmeBSkECHB71IkHYNr7lPiaVakQqe9KC9sb1L35LUqU7V3ds24EVNWd7najZReL_Vbu3-W-vEw5TUxwQeUIkLsqXRi8QmZi46mRV-I2CB4Ids-1VLSzQq3qpOdOlA8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: برنامه‌ای برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد‏
معاون وزارت امور خارجه:
🔴
در سوییس هیچ نشستی با گروسی، علیرغم درخواست وی، برگزار نشد.
🔴
هیچ برنامه ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته ای وجود ندارد.
🔴
این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم ها و... بررسی و تعیین تکلیف خواهند شد.
🔴
نمی توانید با هیاهوی رسانه ای، سیاست "راه بینداز و جا بینداز" را پیش ببرید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/129992" target="_blank">📅 14:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129991">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
دلار با افزایش قیمت به ۱۶۵۰۰۰ تومن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129991" target="_blank">📅 13:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129990">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی پوتین: سلاح‌های هسته‌ای تنها چیزی هستند که از جهان در برابر یک جنگ جهانی محافظت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129990" target="_blank">📅 13:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129989">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وقوع تیراندازی در آنکارا
🔴
رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129989" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129988">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ایسنا: اختلال خدمات کارت محور بانک‌های کشور برطرف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129988" target="_blank">📅 13:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129987">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEzDjrbnZJWvCikv61RBIzRIgheBd39K8lEYCPr2GzZOcgK4Mx6MoVmhJn7a-M36SdLtN1GNXHKkotESf33by29s3p3G981JYNdeAxixWg3OzhW4QGnOtCLyki2VSU6pCYErqtJPnl_Z_npWfPL8VFX7KzebQwmaD2ncqWnfqSAtNEG2vbbJrPtr2i6s-P5nw9hFt7hi84J6VLSStso8_X2yAR0rksNdWSEXHhRX2yyCStL12T1-J5a28aJQiGXdHKecFoCCLnX59kQ0ubYRqKyAqpURqRkvy_ccx2JNJ3araRnhCFTx_rHojAuVq5RMe_wELsFhKhqLQKer0rDiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایید 4 سال زندان برای دو ورزشکار ایرانی در کره جنوبی به دلیل تجاوز
🔴
دادگاه عالی شهر دائگو در کره جنوبی با رد درخواست تجدیدنظر، حکم چهار سال حبس دو عضو کاروان دوومیدانی ایران را که پیش‌تر در پرونده تعرض جنسی محکوم شده بودند، تأیید کرد و به این ترتیب، رأی صادرشده جنبه قطعی پیدا کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129987" target="_blank">📅 13:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129986">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxyqjfw1WMcJj0UZ8KwVm4iucLz0Mw9H1k0j3ApAy9-PqUr7hjddgodvICHXD2oDFF8VbVYucKU4ij2rbGAT3MkbcT1jVBLRL6qUos098r2EXZo5Vd3IHsI2V3Pl2QAQpbGjP42pH98dmdgbHnyb0yAsYhlzDL_RhZc77h_vT83erSyn9fki6hA4l022g-Iz8mHnMH5kZ3DEwBspBbrFUFrd7E_o6ooSepCSShlmaqGVSmm4IhrNxfE3EXwp0rw8PfHbITKDPlvdYIAV_DI5fH7JSJeCd0jjnGRCUweL5mVYPVuyxrK2rf6JLbGm5Mr8_Y12omXmSEfC1KSRE6HlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تاسوعا رو تسلیت عرض میکنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129986" target="_blank">📅 12:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129985">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=ELXRowjNXGRmTeBp3sOnTzDTQP81jenA-3092MPXrsRua1EvlCjfxt-cpTuJGBW3DKYDM8rsWmxXJWgWfaefr1DyfbQt8TWulbqLtFjf9cqj4NNg9HjGLpOZyqtc6Qx_WnbiHEjkXv5ap6p33DK5LJEoxv_BKXsE97S6AkIFu_1lMcj2suzwEVdzQj91z-vRCJf1ARWaJLjda0VE9n9bH33PkYbCkAADZ6kVpBfwBspG-9eRyM0Iw9CN4QXAQYl6bCxKNe3vsensf0J-eVGt3ok51QX4bLNtDLsx9QiLLFNBoihBm4FJRe5kixkGznGbRCTnqiSh6vmqtWYStxfVPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=ELXRowjNXGRmTeBp3sOnTzDTQP81jenA-3092MPXrsRua1EvlCjfxt-cpTuJGBW3DKYDM8rsWmxXJWgWfaefr1DyfbQt8TWulbqLtFjf9cqj4NNg9HjGLpOZyqtc6Qx_WnbiHEjkXv5ap6p33DK5LJEoxv_BKXsE97S6AkIFu_1lMcj2suzwEVdzQj91z-vRCJf1ARWaJLjda0VE9n9bH33PkYbCkAADZ6kVpBfwBspG-9eRyM0Iw9CN4QXAQYl6bCxKNe3vsensf0J-eVGt3ok51QX4bLNtDLsx9QiLLFNBoihBm4FJRe5kixkGznGbRCTnqiSh6vmqtWYStxfVPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
🔴
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129985" target="_blank">📅 12:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129984">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بعضیا هیئت عزاداری سیدالشهدا رو به میتینگ سیاسی تبدیل کردن تا به امیال خودشون برسن
تف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129984" target="_blank">📅 12:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129983">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa3359d12.mp4?token=Ej0OCupmPJit31zpYqyB9qlY5XhqKWIAFiMyRv2wS7nXj2NLL_5hido3YWTp-Irk_Ew4--6lrzzXqrEFeWUzCAJijXuDe-iDjz1h-o-uI7geCL-dN10psQgmqT1HdSskalFLLB_52h5eCGf1J-bk_GLCX_FSuHaV_Tn8cOAd4i_BhA5oMjwsF2nhHfMnmRZ7r25-Atr76_wrwVXWH_viA9Rvvd8HLMPv3lrYfRz2Qkisz79faPtayRZqxJwblTWPZAnHhrAv4FeFF1Y-tjEBgJYNmrpQi2U1SFfeJ3fgV2KGWwvE8VmTepYXaEJPthN2pXqb_tyJOH2BjtolJxNsDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa3359d12.mp4?token=Ej0OCupmPJit31zpYqyB9qlY5XhqKWIAFiMyRv2wS7nXj2NLL_5hido3YWTp-Irk_Ew4--6lrzzXqrEFeWUzCAJijXuDe-iDjz1h-o-uI7geCL-dN10psQgmqT1HdSskalFLLB_52h5eCGf1J-bk_GLCX_FSuHaV_Tn8cOAd4i_BhA5oMjwsF2nhHfMnmRZ7r25-Atr76_wrwVXWH_viA9Rvvd8HLMPv3lrYfRz2Qkisz79faPtayRZqxJwblTWPZAnHhrAv4FeFF1Y-tjEBgJYNmrpQi2U1SFfeJ3fgV2KGWwvE8VmTepYXaEJPthN2pXqb_tyJOH2BjtolJxNsDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بند دوم تفاهم‌نامه نقض شد
🔴
شعار مرگ بر آمریکا در حسینه زنجان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129983" target="_blank">📅 12:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129982">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اینم یه عزاداری زیبای دیگه
از خون جوانان وطن لاله دمیده
🥀
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129982" target="_blank">📅 12:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be27f0a22.mp4?token=Md3jPnRC4IxwVF48fI7fua_omfWQ8VNG5wJVQENEMJEYxwgY4jxrybW4dJpDmATudvVYkUxbhnAfmp7rNepGGdLKx-fm2DMCicNAleZ4Rskj-mgaf2zH6xKMqCB6Y7XDK_0eN0nphbZJHsSQs70qiJhPFhs5i0xFdWnNJM3fK5vPUyrMXvXZCqIafgi70Qxvyzimn102NWNXqerrVYXFIWZu0tssHVMED5PiGZBfJPbaNqDzIv24Sp4FFw-bIovPOI_s3ZROzX6VwoOhu_wfpGM8MHBUlTsdhykuOXy6Fe7ypi02QLwIcieSN-dZmpc-vQhWdUSteskz08SxEU5l0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be27f0a22.mp4?token=Md3jPnRC4IxwVF48fI7fua_omfWQ8VNG5wJVQENEMJEYxwgY4jxrybW4dJpDmATudvVYkUxbhnAfmp7rNepGGdLKx-fm2DMCicNAleZ4Rskj-mgaf2zH6xKMqCB6Y7XDK_0eN0nphbZJHsSQs70qiJhPFhs5i0xFdWnNJM3fK5vPUyrMXvXZCqIafgi70Qxvyzimn102NWNXqerrVYXFIWZu0tssHVMED5PiGZBfJPbaNqDzIv24Sp4FFw-bIovPOI_s3ZROzX6VwoOhu_wfpGM8MHBUlTsdhykuOXy6Fe7ypi02QLwIcieSN-dZmpc-vQhWdUSteskz08SxEU5l0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زیباترین عزاداری این روزها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129981" target="_blank">📅 12:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اروپا به شرکت‌های هواپیمایی توصیه کرد همچنان از پرواز در حریم هوایی ایران خودداری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129980" target="_blank">📅 12:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رئیس جمهور لبنان: مذاکرات  اسرائیل و لبنان در واشنگتن در حال انجام است و جدا از آنچه در جلسات سوئیس بین ایالات متحده و ایران منتشر شد، می‌باشد.
🔴
تلاش برای تثبیت آتش‌بس در جنوب در حال انجام است و پس از آن نیروهای اسرائیلی عقب‌نشینی خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129979" target="_blank">📅 12:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رویترز: قراردادهای آتی نفت خام برنت به ۷۵.۷۴ دلار کاهش یافت که پایین‌ترین سطح آن از ۲۷ فوریه گذشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129978" target="_blank">📅 12:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129977">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
الجزیره: برای شبی دیگر در لبنان، خبر چندانی از تبادل درگیری‌های نظامی وجود نداشته
🔴
به نظر می‌رسد که آتش‌بس همچنان برقرار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129977" target="_blank">📅 11:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4FPr96n0a0QyaVRLW1dsQ5K0QpGBDiCHtesYCbT2zMMx0UhD6EVOOLtgCdzCYM__d1Ad6ENKqkLkCdH863ZZl0KjG86qYhTAuX2sgNjOuSc-yL3rPiLNFIYCAnFAkuIRHEa4aH9SWdKEknRzHhKoXaVyvDAGuJP5pOoaPrFlzrlSoTay255FSslD3T1UswPIUYynkvNm2_Pq1w3-lycSKuY9YdE842DHdwEAqgq8mKQxEbTB-VNn2X4z4nVwkdtS-g4MnnFjJNcecRcp_vFHmIXPA4iNcrNqVC3o1cazU8U-KMeBNEcXbcyQYs_REeAFJY0IDQ-_mDftvcVjyTXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخابره کد اضطراری توسط سوخت‌رسان آمریکایی در آسمان امارات
🔴
یک فروند هواپیمای سوخت‌رسان KC-135R ارتش آمریکا که از فرودگاه بن‌گوریون در اراضی اشغالی برخاسته بود،، در حین پرواز بر فراز امارات و تنگه هرمز، کد اضطراری ۷۷۰۰ را مخابره کرد. این سوخت‌رسان سپس تغییر مسیر داده و  به تل‌آویو بازگشت.
🔴
ارسال این کد به معنای وجود یک وضعیت اضطراری و فوری است که نیاز به فرود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129976" target="_blank">📅 11:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad6aa88dd9.mp4?token=kHMST9j6RH40WlDEEiC-2yRj58AHEtGRDiVEUEHrybX7AW7U8y4ab1I6HXO-ytldfFdiKUfijf1txszZaUvgl5EvWdH2rIqiYlfTNLEdTYKKCGjJENJm3GbycuYxVetbvl8GSyt_KgqkRygA_MCO6hk3UAsO_OydMlONsAi45t7J-jRWZLoFqQ_WsxCtSwZcpOv8O-QzYwlTkfKM8p1tcO2nk_1C0pAmNEAbGU0wzxjlpG_Y_N1KIG5xSr0dMZfZJ9gv_S1K54AuwK0VO7WjsS0h3DOFO4lUmpCDO0zKvvkrkQZxcuFLIE_u9bRA4tVY-GJxFIxdnxW5eW-PGbzrMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad6aa88dd9.mp4?token=kHMST9j6RH40WlDEEiC-2yRj58AHEtGRDiVEUEHrybX7AW7U8y4ab1I6HXO-ytldfFdiKUfijf1txszZaUvgl5EvWdH2rIqiYlfTNLEdTYKKCGjJENJm3GbycuYxVetbvl8GSyt_KgqkRygA_MCO6hk3UAsO_OydMlONsAi45t7J-jRWZLoFqQ_WsxCtSwZcpOv8O-QzYwlTkfKM8p1tcO2nk_1C0pAmNEAbGU0wzxjlpG_Y_N1KIG5xSr0dMZfZJ9gv_S1K54AuwK0VO7WjsS0h3DOFO4lUmpCDO0zKvvkrkQZxcuFLIE_u9bRA4tVY-GJxFIxdnxW5eW-PGbzrMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: تفاهم اسلام آباد حاصل مقاومت و اقتدار ملت شجاع ایران بود
🔴
این یادداشت تبدیل به اعلامیه شکست آمریکا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129975" target="_blank">📅 11:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قالیباف: همسایگی صرفاً یک واقعیت جغرافیایی نیست؛ بلکه یک مسئولیت هم هست.
🔴
هیچ سیاستی که بر پایه حذف، تضعیف یا  بی‌ثبات‌سازی همسایگان طراحی شود، در نهایت به ثبات پایدار برای هیچ طرفی منجر نخواهد شد.
🔴
درمیانه جنگ اخیر نیز بر اساس نظر رهبر معظم انقلاب اعلام کرده بودم ایران با نهایت علاقمندی به همه کشورهای اسلامی خصوصا کشورهای‌منطقه، بویژه کشورهای ‌حاشیه ‌خلیج‌ فارس اعلام می‌کند که آماده توافق های امنیتی است که با همکاری های اقتصادی پایدار شود و سرزمین های اسلامی برای تمام سرمایه گذاران، امن شده و دربرابر دشمنان مشترک خود ایمن شود.
🔴
جمهوری اسلامی ایران دست برادری و همکاری خود را به سوی همه کشورهای اسلامی دراز می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129974" target="_blank">📅 11:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
قالیباف: امنیت منطقه باید توسط کشورهای منطقه تامین شود / هیچ کشوری امنیت خود را در ناامنی دیگران نخواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129973" target="_blank">📅 11:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قالیباف: ایران از صلح استقبال می‌کند؛ صلحی که بر پایه حقوق ملت‌ها، احترام متقابل، تعهدات متوازن و منافع مشروع باشد.
🔴
بر همین مبنا معتقدیم دفاع مقتدرانه، انسجام ملی و دیپلماسی، سه رکن مکمل یکدیگرند و تلفیق هوشمندانه آن‌ها، تضمین‌کننده امنیت و ثبات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129972" target="_blank">📅 11:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
قالیباف:  ایران آمادگی دارد با همه کشورهای اسلامی، بر اساس اصول احترام متقابل، عدم مداخله در امور داخلی، حسن همجواری و منافع مشترک، همکاری‌های خود را گسترش دهد.
🔴
ایران از هر ابتکار عملی برای شکل‌گیری سازوکارهای مشترک اقتصادی، تجاری، مالی، علمی و امنیتی جمعی حمایت کامل می‌کند.
🔴
ما در سخت‌ترین وپیچیده‌ترین شرایط، دوستان و شرکای راهبردی خود را تنها نگذاشته‌ایم.
🔴
برای ما، آتش‌بس در لبنان به اندازه آتش‌بس در ایران و در ادامه، خاتمه جنگ در لبنان به اندازه خاتمه جنگ در ایران اهمیت داشته و دارد و باور داریم که ثبات واقتدار در هر نقطه ازجهان اسلام، به تقویت عاملیت، عزت و ثبات در کل امت اسلامی منجر خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/129971" target="_blank">📅 11:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: مذاکرات فنی در سطح کارشناسی هفته آینده با میانجیگری پاکستان و قطر از سر گرفته خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129970" target="_blank">📅 10:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان: در حال برقراری ارتباط با دو طرف آمریکایی و ایرانی برای اجرای مؤثر تفاهم‌نامه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/129969" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129968">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8-yHVQnWRmnklYeLlqmw5NRPjY8Af1YFPAyZDjwj9lkNsnJCs9UrrqoyuluLWYq3oZBc7cJjb0L-lHwxq8kvv6OjayTtNRFunEuyDrKQTaS-fmsr5GX1SCDVGSCUKEh6IEZCv3uEtpnVGZ78BTFHAbk--HJres9-keGH2ZNRa02CvPQAoNjl72AKX9JeEwYEtjG-z1Fq4kaoplNF3P3e6Wuen1bQ4E71SoyoF9D_VDAvn5nJ8Eet_wLgKx89QBrgYE_oCxOM0GSLBM7dz75i62Z97e7Z4786gARS8mAtsBY22XhkpMY19U2YMum73MeHLvK61fRkBrH8e8Zaqtv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر ارتباطات: نسبت دادن اختلالات اخیر بانکی به بازگشایی اینترنت بین‌الملل ادعایی غیرکارشناسانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/129968" target="_blank">📅 10:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129967">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: از تأسیسات هسته‌ای ایران بازرسی خواهیم کرد
🔴
ما معتقدیم که بازرسی از تأسیسات هسته‌ای ایران در اسرع وقت بهترین گزینه است
🔴
اولویت اصلی ما مشخص کردن محل ذخایر اورانیوم غنی‌شده با خلوص بالای ایران است.
🔴
ما از محل اورانیوم غنی‌شده با خلوص بالا اطلاع داریم، اما مهم است که ایران ما را از آن مطلع کند.
🔴
به زودی با ایران برای تعیین تاریخ بازرسی‌ها و جزئیات مربوطه مذاکره خواهیم کرد
🔴
آژانس ما بازرسی را انجام خواهد داد و این به تهران بستگی دارد که واشنگتن یا ناظران دیگر را دعوت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129967" target="_blank">📅 10:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129966">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBwa4sI9Vj7OvsrdUplXZC0wmO184XSCEruTESI7Q_46T517H27ySVNd8GO65m4fPykMTL016Ei8IeETDA4qEB8HgY1AtKZHt0c18wxr_Gw4823Nw3UHKCR40mipOSZNcM9plzt3f8W7BEjhFGY8y1uG33S1zdhQOVa8eqjPvEs1tezaj3NHBkz9yjtE4wWsCCH9mLGu7KDLQHgPCri2n-DvgulFQJ1Ru-APg7z4dAycOmp2Vos7zqaPHj3KKTXkbxfxjwWRq6DuKZQpXsV_JThroHBKAJ8xlTzDxpudmOR7knybcYrPC0JkznAYsNOBsM96xIKRsljE9bumhiFcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: آمریکای زیبا هرگز یک کشور کمونیستی نخواهد شد!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129966" target="_blank">📅 10:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129965">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: همه از نتانیاهو خسته شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/129965" target="_blank">📅 10:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129964">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aacf80584.mp4?token=Dz2CLJzi5-5TIInAvFMD60Vo61XrpnqxGYPUCefNtSwlg6BLMHfIPt9yinIVYxgS7xn-dcA6DIC52L0gNmGyMw9v-NTmRWwFdzX7QsOTJM92emqj9oLxSErgKDbEprkdGVFihgw-0_t3p0Chyk2cHihitd9Bp-P77bCYUsAgDOyxupQdjQSbewZbAhmWm9c50DN3Zt5HPQKMN4i1tS2ECbGJDalNuR49WMcR-bp7Kz3xjjkv5tpJaag6L7Wc1F_bpX0C0MwaEForKXpVmimO1knXTFX3eFpRx4iO8ZVcL3_ZWotCn0_9kF50I4X4q9QQh2uETFh-bZqoYrgSAkmp8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aacf80584.mp4?token=Dz2CLJzi5-5TIInAvFMD60Vo61XrpnqxGYPUCefNtSwlg6BLMHfIPt9yinIVYxgS7xn-dcA6DIC52L0gNmGyMw9v-NTmRWwFdzX7QsOTJM92emqj9oLxSErgKDbEprkdGVFihgw-0_t3p0Chyk2cHihitd9Bp-P77bCYUsAgDOyxupQdjQSbewZbAhmWm9c50DN3Zt5HPQKMN4i1tS2ECbGJDalNuR49WMcR-bp7Kz3xjjkv5tpJaag6L7Wc1F_bpX0C0MwaEForKXpVmimO1knXTFX3eFpRx4iO8ZVcL3_ZWotCn0_9kF50I4X4q9QQh2uETFh-bZqoYrgSAkmp8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ که توی پیجش قرار داده و مضمونش بر اینه که هیچوقت نمیزارم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/129964" target="_blank">📅 10:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129963">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وال استریت ژورنال :  اسرائیل با فشارهای آمریکا برای خروج نیروهایش از جنوب لبنان روبه‌رو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129963" target="_blank">📅 10:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129962">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قالیباف: بعد از جنگ اخیر، شرایط منطقه متفاوت شده و باید با نگاه دیگری آن را دید
🔴
در گذشته برداشت برخی کشور‌ها این بود که نیرو‌ها و کشور‌هایی که از هزاران کیلومتر دورتر وارد شده‌اند، می‌توانند امنیت منطقه را برقرار کنند، اما بعد از جنگ اخیر مشخص شد که نمی‌توانند و خود از عوامل ضد امنیتی هستند
🔴
باید از این نگاه جدید در منطقه استفاده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/129962" target="_blank">📅 09:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129961">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نخست‌وزیر قطر: ضرورت ایجاد یک خط ارتباطی میان تهران و واشنگتن در دوران پاک‌سازی مین‌ها در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/129961" target="_blank">📅 09:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129960">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نخست وزیر قطر به فایننشال تایمز:
مذاکرات سوئیس (ايران - آمریکا) زمینه را برای مذاکرات دائمی حل و فصل بحران فراهم کرد و کار تازه آغاز شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/129960" target="_blank">📅 09:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129959">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE1sQPtFg_5pmZRENTlup6RQ4-uIielyNcbIDhWH6P2zZAvkSSs2mAOz-3JCeckvgsPdquCKTifTQ7Z9GVhf_VYg1I4oAJkPmeniw4FoFVQ__wFUG94an-qKIT8M2J_afgB9a8c3x-Z-RzUhIbmapEbqtvqSLu9ydyz4FwBntSg7VtfWSsB-u345f6Vi_0IX1lfkNux-lMeJyXdjDdC3JnvRJdLa_XajB6g0kW0nnsshimu19V6ny9ycqbv98UnEdziLX_HjSHrRt6BnpEYbSV3-W58yx9lTY0W_q7caJzChgS7ofCNUxTOkFjjP-9hsKcni0mBtbj-y4nUeeeeURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد ترامپ از پمپ بنزین های آمریکا: قیمت را با کاهش بهای نفت پایین نمی آورند
🔴
ترامپ در شبکه اجتماعی اش نوشت:
شرکت‌های بزرگ نفتی قیمت‌های خود در پمپ بنزین ها را به اندازه کاهش شدید قیمت‌هایی که برای نفت می‌پردازند، پایین نمی‌آورند.
🔴
این قیمت‌ها مثل سنگ سقوط می‌کنند! به عبارت دیگر، مشتریان «سوءاستفاده» می‌شوند.
🔴
من به وزارت دادگستری دستور داده‌ام فوراً به این موضوع رسیدگی کند. قیمت بنزین باید خیلی سریع‌تر از چیزی که من می‌بینم کاهش یابد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129959" target="_blank">📅 09:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f466cb2cd.mp4?token=gXwu7weUH6a5RsqpHbzzostTgBKQFKkPBtbiXV_8fZmuKWJhlsM1VzKIp43mQa-AXjzoM7S5M3JI9VxqwWHSJJYckARoA0TQdEbEsRI4X6zbg8lJ22XkV2oxwyFueN1ouvK-O1jy-MRUnvsbynBkW7ZGBZGcREfEOlauT-yN_7tK_jxEi6ObhCRF_M4SRgrMwZGcGSDpn-UytNntTtACQIaMb5aZ4f5Tzm_TVTvl8nnxskt5szGS76MOKQbxC1u0lW9BXEaEJkzBTGKg7LqWA4H2q4VHJ-yeFLbqpQlgJBGjNPJX_aOWNGjfxWacbXiSqec-IRkOTYk96hR38XrU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f466cb2cd.mp4?token=gXwu7weUH6a5RsqpHbzzostTgBKQFKkPBtbiXV_8fZmuKWJhlsM1VzKIp43mQa-AXjzoM7S5M3JI9VxqwWHSJJYckARoA0TQdEbEsRI4X6zbg8lJ22XkV2oxwyFueN1ouvK-O1jy-MRUnvsbynBkW7ZGBZGcREfEOlauT-yN_7tK_jxEi6ObhCRF_M4SRgrMwZGcGSDpn-UytNntTtACQIaMb5aZ4f5Tzm_TVTvl8nnxskt5szGS76MOKQbxC1u0lW9BXEaEJkzBTGKg7LqWA4H2q4VHJ-yeFLbqpQlgJBGjNPJX_aOWNGjfxWacbXiSqec-IRkOTYk96hR38XrU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: همسرم به من می‌گوید لطفا نرقص، اما من عاشق رقصیدن هستم
🔴
رئیس‌جمهور آمریکا در ادامه گفت: همسر بسیار شیک‌پوش من به من می‌گوید؛ عزیزم، لطفا نرقص! این در شأن ریاست جمهوری نیست. اما من می‌گویم مردم عاشق رقصیدن من هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129958" target="_blank">📅 09:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129957">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اکونومیست: نتانیاهو در نهایت مجبور است با توافق تهران- واشنگتن کنار بیاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/129957" target="_blank">📅 09:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129956">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffgfMjY5v91gznCc_mt6NBetDqHzecwwY1ndgpu7gAEz5KwgGVaSUUtOaC-rEFvr4oiDkkN1VyRGlwpNLi1fyRqIB93tQFkcjHADPn04p7ktea5ttcfR1-F9FAISFv1Wu1kv6BguzbdGoIPX3MN8k804piulEown2QAae5GUWF3KSlYNQqB29qkwpg4ILJxBwOjOZ8mix63x43kuHfkJth-pZn-bIUZEkd3kBksGWdRkOUhcFsGekFXAAq6buyoCB8p56juYztZcmGqNzSHv4UCT-55hResR1kZ6WAnhPYAkLQ3vW6LaNXk3-M8AieLfirPFJIa8qeq_E8Xt9aYxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش سناتور برنی سندرز به تصویب قطعنامه غیر الزام‌آور اختیارات جنگی در مجلس سنا: کنگره بالاخره کاری را که باید ماه‌ها پیش انجام می‌داد، انجام داد: به درخواست از ترامپ برای پایان دادن به جنگ با ایران رأی داد.
🔴
قانون اساسی واضح است: روسای جمهور نمی‌توانند به طور یکجانبه ما را به جنگ بکشانند. این مسئولیت کنگره است.
🔴
زمان آن فرا رسیده است که کنگره سرانجام مسئولیت خود را بپذیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/129956" target="_blank">📅 09:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نخست‌وزیر قطر: امکان سرمایه گذاری کشورهای خلیج فارس در ایران طبق بند ۶ تفاهم نامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/129955" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129954">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مهر : اختلال خدمات کارت‌محور بانک‌ها رفع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129954" target="_blank">📅 09:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129953">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
لبنان و اسرائیل امروز هم مذاکره می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129953" target="_blank">📅 09:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129952">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
لوفت‌هانزا: تمایل شرکت‌های هواپیمایی زیر مجموعه‌ ما به ازسرگیری پروازها به ایران
🔴
بررسی و برنامه‌ریزی برای گنجاندن این پروازها در برنامه زمستانه این شرکت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/129952" target="_blank">📅 08:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129951">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dae873392.mp4?token=Zsh41EFoK2XKimtzKxrSIlHIx1LuIUrvPc338QQmtEivG7-DmNLL4zLxbZTUY4hq9cJjXFbjpxoqLEb8rpj7786gkx7IO9JbPw5KIMEgR2gUvJcTMytT66CAhhKpafgHwDdxBSPuKSQuZb8oido78-F2CyqEsSRnQ5LBkFcfh2GyiHvXqFlT750qqOBi8rzUUUgbdp7BG0XewazGy5dxjp0RpiGfLyI1u3wqyxJ_zH5rJMlDBFsCEev6Vcf5-24wbUBIFbLRajzk_sXEoQp-8G0RoohpYWtuN56J3e3SE8zPmsXUo_srOaU5GIXqoLVGThT1JmSKIzst9myWllgxeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dae873392.mp4?token=Zsh41EFoK2XKimtzKxrSIlHIx1LuIUrvPc338QQmtEivG7-DmNLL4zLxbZTUY4hq9cJjXFbjpxoqLEb8rpj7786gkx7IO9JbPw5KIMEgR2gUvJcTMytT66CAhhKpafgHwDdxBSPuKSQuZb8oido78-F2CyqEsSRnQ5LBkFcfh2GyiHvXqFlT750qqOBi8rzUUUgbdp7BG0XewazGy5dxjp0RpiGfLyI1u3wqyxJ_zH5rJMlDBFsCEev6Vcf5-24wbUBIFbLRajzk_sXEoQp-8G0RoohpYWtuN56J3e3SE8zPmsXUo_srOaU5GIXqoLVGThT1JmSKIzst9myWllgxeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از کیروفسکه، کریمه، در میان حملات پهپادی اوکراین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/129951" target="_blank">📅 08:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129950">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gi5kKl31dCKZoYD3fTBelg5-qnXZGA3DigTtQIC_9zDDFQ2UIWKpjdTLJvPEoS4brWpJX9wIn2ZT1jKB6CqTi-GiOJBAhkX1onZI61ScWgpRvjMCRKkbk4Lg2wZ9MyvracuCUFuWdoqfPXEvbx2-WX9kqVj4cDxw3DjVrryyTFrLjh9gi_yqcmutj6mDplf-uiD2anfZ551aDshgQv7cKMDxVrhcGIRCJOenxzz4MTHpZYqmWqKdK1-7ZC4xU7Qqfx_lWaCx-C0zsfeIuzpZp4i8Jn0y3FEBaI29q3KDzMt90a4Ci8SLJQIF1XpdEyVucKKQtFU2d2MzS4v662rmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده، تحریم‌های اضافی علیه «گروه مدیریت کسب‌وکار اس.آ.»، یک کنسرسیوم تجاری متعلق به نیروهای مسلح انقلابی که اکثریت تجارت کوبا را کنترل می‌کند، اعلام کرد؛ به‌طور خاص بخش‌های این کنسرسیوم که در بهره‌برداری از ذخایر معدنی و فلزی کوبا و بخش‌های مسئول انتقال دارایی‌های مالی و فیزیکی نقش دارند، تحریم شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129950" target="_blank">📅 08:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129949">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leqgJbPf_8aTzIuOPn22jyKPfy2ZZKl224h7thAnleXN-kU9q4tOG3nHpJQWTFmYzfwlykMt_EuJMJfxHKOaFohsnY_PkfgyeEPZo9B6ebWgAqPImHU-qeaKpjgh-eSTlMIeqon8ff__3APUR2v6rZRmsTo5RfnzQs0AX6MGlSRkHwW-2GNr833SZgQG-GBGyBij5c5s_v0QPf3-deelVs-DsyoyY3nQM9svX8RWLpaAVyQ2pzpX1k8f2GG8QDgz8S1CvDGDeaiiNwhx06oywejDdwH0ZhhvKLkBavDMzS5sLAvVyDeDxCTYGUsCG_3GWspbGMRpxBwY9TcjOI3HFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ترامپ به تصمیم سنای آمریکا/سناتورها کار مرا دشوارتر کرده‌اند، اما من به هر شکلی که باشد آن را به سرانجام می‌رسانم
🔴
ترامپ: من ایران را کاملاً در تنگنا قرار داده بودم؛ در آستانه تسلیم بود، حاضر بود تقریباً هر چیزی به ما بدهد و برای نخستین بار در دهه‌های اخیر، احترام زیادی برای ایالات متحده و رئیس‌جمهورش، یعنی من، قائل شده بود.
🔴
اما سنای آمریکا تصمیم گرفت در زمانی نامناسب و بی‌معنا درباره قانون اختیارات جنگی رأی‌گیری کند؛ اقدامی که به بزرگ‌ترین حامی تروریسم در جهان این پیام را داد که ایالات متحده از کاری که من با آن‌ها انجام می‌دهم راضی نیست و باید متوقف شوم، و به این ترتیب به دشمن کمک و دلگرمی داد.
🔴
چهار جمهوری‌خواه بازنده همراه با دموکرات‌ها رأی دادند و ایران از افراد من پرسید: «همه این‌ها چه معنایی دارد؟»
🔴
این سناتورها کار مرا دشوارتر کرده‌اند، اما من به هر شکلی که باشد آن را به سرانجام می‌رسانم، چون همیشه کار را به نتیجه می‌رسانم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129949" target="_blank">📅 08:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVpg0d8Bf_vswZwfqiQTgwdetXgVj1M9OUxKZuwkkBCHPvPGok-lchckjQVmQqMqnZkMFFS36lFfhFJHcBLgSJf0-q4iq2qlTh6cX8HzO4CVRM9nVU0NY4S1g5e00l0SasjmAbYmiY11OLNeMXXxD5PopOOs8e6vP6uuBWsdMGEI1SHykDP0xLj6LEQH5bjLkqQ1KtJn_7D2p717z7wzdqIM3AtrBlFrF5JwYwuHptfN10aIvEY4x0lYxKv3jPfvlv7ccXNk5vnZ1HnQcYv0OGR0pPIoDTbsGmvV2y7NEi1YFvfBfunag4WUdfOaxqnnsDr9LP9-9zztmpdtAovQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم جونگ اون، رئیس کره شمالی، اعلام کرد که برنامه تجهیز ناوگان دریایی این کشور به تسلیحات هسته‌ای مطابق برنامه‌ریزی‌های انجام‌شده در حال پیشرفت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129948" target="_blank">📅 08:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129947">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYQ65aeVhdiIMmMjiyC5pIHAbgeBpYptu6108rro3D3wqapZMlT73r1rmIrGGO6ite1jDhkeKBW066LBKgcbWVsLaYdGAhVE7GcI2B48rugDJlRkXbF8u9L-RVTLbNb1zuB4sfP0m8GPf0gbBqX1Rl1zfwTt9mkWfiYwtNdfiU42Nj3p3CRmVc-dLXtY-hzyCnCv3hnqkenx9uX7oFnC333cTBn4yQ2nsO9G4N5u3DOdY-ArA7dHfePACd4yiuWAKvNDWjyGeSDHBJOC4dO0acnzbhJ_E3YpiqqRQ4RDXFOHoVDJAm6Py5D9StZrzQi7Dfp_D3Bf9I0bSO37iDcadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آای هیمتی:
اگه ذرت و سویا آمریکایی کیفیت خوبی داشته باشه، چرا که نه! میخریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/129947" target="_blank">📅 08:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129946">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYGFqV-BwVtvdWJnAzmZd2Vxc8ROPBkBWuhm2nb2AQZOJ_jyrYA6FI1XID1ko08877V4dqA8vS0QPVvq1NaqwJMizgN5Tgx2aqKbjnsSWjdARDg3bibURDvqraodZrNjvj7STBRjFYO-_L00Y4R8wRBvK-kECvY21rS0SBtDzhOOG23aZMD_BSAl-SGt5k3Nav4wUJ0LXIXrhxNHWWk3xWOUK6QsqizpDDmloUYC2XGqSZsvAc-SAhXCXY80udTKR4THWrY3hrOO355zSxeLGx1Z073--ODDts5GLADECgX1pvcwetONBFRYKlu4yeMZhqPJ1bJ3J--ikMhA4F71tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری دنیا جهانبخت از حضور در مراسم عزاداری.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/129946" target="_blank">📅 08:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129943">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRKmZ_Dyq5QRAuqXVXblMI0-i9miE-_HRtjjsRoCPX3Xj-JRH675fSMeAgoSA2SYJ28GPC3IhlBp67vEHK73AcUksF68PppabuHsMFPFoXmMJGKIkRu2XOgjhrBu9wPPPfB9Jl0jIy8I0QPOvroZj21QQ6RPMCLORaNYitF_LQlSxWeJyw_8fuBgdqJV_uhBdx602qEPB1xvHOQq0KGeLO7TpK5cYiuXLtPtn7PRX1V-0dmKDTemQp93dSCSR6V2v1UMo9c64o-hHsFwGiuIE2ddYStzPENUaq1ZnOBh3GK5wvP6jZN46Z0Wdo2PEyO9TG_IdXaduWldYPuougWcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZ4DmibRI48ckwPgCod3THnkZI-6ZcBft-0YqW2AANfzdD8TLG85LGpfYri6EU84Zt8fILveSFgtcbWONRorBb49MnNLoBZJMQN0jEPDFLgHvSyciDg__abtuEcKCUgARkaSucbZfCBOaQOrjznHpHTEdF7N2PMldHua-gydzCTzqyTG55PslojRYrD9ol_Qgk_y_vwJe0aUJBcQNr8zIQ8iS8L9sBGaRHCZ-BCYa3Vcshnu2wqVCyZc4Q_QhRKQ9qqs1Dl_zfjhE7j5nRSqgK79PfEsOs8FhpSRE8Zf6wfZYp0dsEKT1i0zJTLtbzVN4sfyz_TjH_XnS-0X10wRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_HEyIaEPJIDGlbIyTMB8dycbbf425TbqmarrXlbiVXENK1Mk2x2BsyXQbLTYbdbbCHOLp4GAliSPO3DLjXHLFzkM3dqaDe2sm8MPRdDaqvnaOFuyo_nsiXG8_t1bLGVGdlQeXU7R0kPywsKIj1KnxHRmmuQf6rcnl9lYyZSoqKxHj-SnxXuITC35WuuFgiGh4_1ODCBzvJFBeA6HjJv_MvXbiFMT46oEUwFDOQpMekLaHHcj_XZ8Shu8WJlFVuAVsRnUvlLhBbsXF_S0jcuJhuq6FF_xWgor14zYIiZ1NzqsFQh_sjTHJkjIJAUiYyn4qnQ_YjU2F2A1xDGGVufRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل به چادری تو غزه حملهِ هوایی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/129943" target="_blank">📅 01:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129942">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXX8NnpLa7vPo6tuAauBSKZueU1u8he95jlIXui4I1n7YW8-J8QYpO7Z2zq06ex0pbw8xiqSTYvUB1NRR7qqMKEwY8W5-0CCdMDn1vEk4qydg6yEMyENlsvFsjbmkFAzFR4mE26UjejNRCwtwK4kC4snOn0DL4mxtRCeyhCBTbLS03kgSD0feJS5U1NH5McBM03hcEf44dNvinFTMlUfudo6dqQfif8L9JLN8zsAcKF8luxRMtuq0b1P25Xn2klCmwYcI9_gLL7_awSAUYTRYlNygucTc_ReD-tU883QgseRT1qCpe6cFngbBnYCZm0ejY0EgwBATzSjy0CB2mTUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: این روزا همه چیز عجیب شده...
🔴
اون جایی که باید بسته باشه، بازه.
🔴
اون جایی که باید باز باشه، بسته‌ست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/129942" target="_blank">📅 01:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129941">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فرماندهی سایبری کشور:  اختلال ایجادشده در سامانه‌های کارت‌محور برخی بانک‌ها ناشی از یک حمله سایبری هدفمند به زیرساخت‌های مرتبط بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/129941" target="_blank">📅 00:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129940">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375b61eb9b.mp4?token=UZmG0YHPJTCEsOChTXohrVhjeimG5Dbq1G_SPEeRsbhyrNN3cYUFoU-2AJ0RrGmv261r8Byf8Dd7XgW9BQbA5J1RbVrIiyLgl-r7elYI2Jjtfq_vptcUM6eVTAekhDxfzUoaVxR9l40A43PATim3xcZcC1e6CYqR5_cyTovjQa9NR8aIvBcXPNy512ufzo7D6de70ocBzdl2PNxVuFUw0LmQbIqzM05vraJx3J31b7KR0t9E6eZUs0DDxSnMCuumxil2vCMyepdZzApb84m9yaOXz17_fmosZHp7vmo6f5O1forOdqxHzt1_kFK3sgkfCuSBUvt9Hb7CXaBMXgUYug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375b61eb9b.mp4?token=UZmG0YHPJTCEsOChTXohrVhjeimG5Dbq1G_SPEeRsbhyrNN3cYUFoU-2AJ0RrGmv261r8Byf8Dd7XgW9BQbA5J1RbVrIiyLgl-r7elYI2Jjtfq_vptcUM6eVTAekhDxfzUoaVxR9l40A43PATim3xcZcC1e6CYqR5_cyTovjQa9NR8aIvBcXPNy512ufzo7D6de70ocBzdl2PNxVuFUw0LmQbIqzM05vraJx3J31b7KR0t9E6eZUs0DDxSnMCuumxil2vCMyepdZzApb84m9yaOXz17_fmosZHp7vmo6f5O1forOdqxHzt1_kFK3sgkfCuSBUvt9Hb7CXaBMXgUYug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهباز شریف هم نتونست مانع بیل زدن پایان ناپذیر پزشکیان برای کاشتن درخت تو اسلام آباد بشه
🔴
شهباز هی میگه نمادین هست ولش کن اما مسعود ول نمیکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/129940" target="_blank">📅 00:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129939">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کانالای ایتا: ممکنه نهاده‌های دامی آمریکایی آلوده باشه و مردم مریض بشن
🔴
پ.ن: احتمالا ارزشیون جزو دام و طیور هستن که نگرانن
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/129939" target="_blank">📅 00:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129938">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ7b_TMKpccAsoCLXDH7OR8HRXJJXsnvX32bhbpU9jdboThsTlB30OQ5XXg-442ZUT0RNlLsh2nsa0abW2uJVVhTAxgVAlYKVhL3oeeLJNap7UlBfhyLACrCeXGAKveFUh0DjE4QnxXIEuFk9ss1dEMeKdTgR2hFFIEl4Zd-YnWnyCSfYFEkyKmRqCrGF7UkbSNchkvWsmEOC0pJH4_9285W6lz_vclUxe4U2q57_tJLwui77cfidki3vkcCTtrqi-qmd0IFMGAU2of54QDjgk9qzitR7JEi77UNJxOaTRzAg9dK9zoIae2oO36V0rWJNsNki2f_AO1sI_GZ8Yayyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تقریبا 320 تا پهباد به سمت روسیه پرتاب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/129938" target="_blank">📅 00:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129937">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
امیر پوردستان رئیس مرکز تحقیقات راهبردی ارتش: چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/129937" target="_blank">📅 00:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129936">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: به توافق صلح تاریخی با ایران دست یافتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/129936" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129935">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c0d36b14a.mp4?token=U_o-JCr6L7zhBDS4Yw7tZL17f-HD3zUf7rTY_6pNo8xgCIQ-jOrPPvxk03772kKJCgoQ74lHdnzfyEDJDCX8t_Pw2I8oG1gkqUmViNNIaAAldl_Aan71h_G9PfiEd4ZNT-bLQ3UM1tLjovRAPfcpY4GQT1WIb9V8bAGQOba2GqDhYuoHdlbNFjKy1sBOFZ_nRo6zMSivKdpeGo_c9t1Vi-iln874vfZeTfnUMq2PNJU-woPi0WYDBTFHjXayhIzHhh0qX4brvz8NBcVnYK5zLabRM52_PGedrKGhApMynYcU3kmdUlMTvDdfi7b51zJqmItWg2rIbn3Zerq3UcGPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c0d36b14a.mp4?token=U_o-JCr6L7zhBDS4Yw7tZL17f-HD3zUf7rTY_6pNo8xgCIQ-jOrPPvxk03772kKJCgoQ74lHdnzfyEDJDCX8t_Pw2I8oG1gkqUmViNNIaAAldl_Aan71h_G9PfiEd4ZNT-bLQ3UM1tLjovRAPfcpY4GQT1WIb9V8bAGQOba2GqDhYuoHdlbNFjKy1sBOFZ_nRo6zMSivKdpeGo_c9t1Vi-iln874vfZeTfnUMq2PNJU-woPi0WYDBTFHjXayhIzHhh0qX4brvz8NBcVnYK5zLabRM52_PGedrKGhApMynYcU3kmdUlMTvDdfi7b51zJqmItWg2rIbn3Zerq3UcGPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ دوباره تهدید کرد
🔴
می‌توانیم کار ایران را کمتر از یک هفته تمام کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/129935" target="_blank">📅 23:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129934">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d170582e.mp4?token=L6uPnctWnFl8iJnacgOkGA-nR36KNIiqOJjqBfI57Ud0YlaOjDcI2rGe9P8uAO-Mn6ia-NI0xmxFV381Fl92IsJu32-RMRUsde8w0qEucL-vTL15hH7cuPT_4L_16qxCed0bWcIb0Twvb1Gys7ftLH07SBXdtRLK38JoCrO4VNEnoVKJAhjYAIW_i37IpqcMxhm1yx69gXH1QqYsQjJHI5E_r7beKCAGep-qDaJm4JfgZY697_7Vy5h74f16W9gsT1jMp3oencIHu908xIL2hGGyr4ZnoMuLa_sjkJVPF_PiBPNGT26oNwsGS-JK4s2NsSVkKJOpTWJ2BBWND4fWM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d170582e.mp4?token=L6uPnctWnFl8iJnacgOkGA-nR36KNIiqOJjqBfI57Ud0YlaOjDcI2rGe9P8uAO-Mn6ia-NI0xmxFV381Fl92IsJu32-RMRUsde8w0qEucL-vTL15hH7cuPT_4L_16qxCed0bWcIb0Twvb1Gys7ftLH07SBXdtRLK38JoCrO4VNEnoVKJAhjYAIW_i37IpqcMxhm1yx69gXH1QqYsQjJHI5E_r7beKCAGep-qDaJm4JfgZY697_7Vy5h74f16W9gsT1jMp3oencIHu908xIL2hGGyr4ZnoMuLa_sjkJVPF_PiBPNGT26oNwsGS-JK4s2NsSVkKJOpTWJ2BBWND4fWM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ پیشنهاد می‌کند که ونزوئلا باید در آمار تولید نفت ایالات متحده گنجانده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/129934" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129933">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
فرماندهی سایبری کشور: اختلال ایجادشده در سامانه‌های کارت‌محور برخی بانک‌ها از جمله بانک‌های ملی، صادرات و تجارت ناشی از یک حمله سایبری هدفمند به زیرساخت‌های مرتبط بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/129933" target="_blank">📅 23:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129932">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا: ما باید سیاست خارجی را به عمقی که سیاست خارجی به آن نیاز دارد، برگردانیم.
🔴
نظرم را درباره رئیس‌جمهور ایالات متحده عوض نمی‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/129932" target="_blank">📅 23:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129931">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری / سنای آمريکا طرحي را تصويب کرد که به دنبال مسدود کردن اقدام نظامي عليه ايران است مگر اينکه رئيس‌جمهور ترامپ مجوز کنگره را دريافت کند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/129931" target="_blank">📅 23:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129930">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: ایران عالی بوده است. اگر ایرانیان هوشمند باشند، منطقی خواهند بود؛ در غیر این صورت، مجبور خواهیم شد کار را به پایان برسانیم که احتمالاً کمتر از یک هفته طول می‌کشد.
🔴
اما فکر می‌کنم همه چیز برای آن‌ها خوب خواهد شد. آن‌ها کاری که باید انجام دهند را انجام خواهند داد زیرا ما می‌خواهیم این کار انجام شود
✅
@AloNews
خبر جنگ
﻿</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/129930" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129929">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ : ایران با ونزوئلا خیلی فرق داره و نگاه و ایدئولوژی متفاوتی داره
🔴
در کل هم طرز فکر و باورهای مسلمان‌ها با کاتولیک‌ها یه سری تفاوت‌های اساسی داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/129929" target="_blank">📅 23:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری / سنای آمريکا طرحي را تصويب کرد که به دنبال مسدود کردن اقدام نظامي عليه ايران است مگر اينکه رئيس‌جمهور ترامپ مجوز کنگره را دريافت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/129928" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dc387a22.mp4?token=R7TFb6y5UxvBbc4fVm-XE2J9U7yYeAhkBh3yl1NO_iV8wIiXdztZeW5JqZBxxny4_cnP_Qen0QZZHSG9bY-i8sg00Sso5x4dpmvKCzHGPKEIq30sQZT7053JEOmAK65V8RXD8JSaPuUsYFnaHs-IqaaWa7XASxlFJnOHqVy8B7lrmhYvCVC0pnMpJ_62Rnv3Fye4MVetdi-veQCtcw50emiSyRmpTU0_-J0GAUiwCA3_SStY8j6p8HzeveAWhULZcnuJhkpnJ9ZGB5PzWpDoitgMArtIqB5GvOOgyLPLJShtPaBv6KybqF_Nf9WRXyZ3Las8E46bkAvx04Sh9w5W6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dc387a22.mp4?token=R7TFb6y5UxvBbc4fVm-XE2J9U7yYeAhkBh3yl1NO_iV8wIiXdztZeW5JqZBxxny4_cnP_Qen0QZZHSG9bY-i8sg00Sso5x4dpmvKCzHGPKEIq30sQZT7053JEOmAK65V8RXD8JSaPuUsYFnaHs-IqaaWa7XASxlFJnOHqVy8B7lrmhYvCVC0pnMpJ_62Rnv3Fye4MVetdi-veQCtcw50emiSyRmpTU0_-J0GAUiwCA3_SStY8j6p8HzeveAWhULZcnuJhkpnJ9ZGB5PzWpDoitgMArtIqB5GvOOgyLPLJShtPaBv6KybqF_Nf9WRXyZ3Las8E46bkAvx04Sh9w5W6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در پنسیلوانیا
:
«کدومو بیشتر دوست دارین، جو خواب‌آلود یا جو فاسد؟ آماده‌این؟»
🔴
جو خواب‌آلود! تشویق حضار
🔴
جو فاسد! تشویق بلندتر حضار
🔴
«متعجب شدم. من خودم "جو خواب‌آلود" رو بیشتر دوست دارم، ولی ظاهراً "جو فاسد" برنده شد. البته هر دوشون خوبن!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/129927" target="_blank">📅 23:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129926">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15aaa27354.mp4?token=ty0sdSnAu1LljXkCN20iEhd2sTAPhVReU4GJ9IIP4dP7kRmsQV5Q9hP6rjWpI89N-UiK0GxNy70_XM45dEKc4g9vjxTd32B5Vk3IZBGIwxzINsL65WYzLJbcRvHMojWzN03UHlISB4JNJhsOJDYmOPIrOLQBbQy9JFe90Ed6sVS1wYGLHt4JXokl2ja14pya3_0HM78mvoDrSLQiDdge1aM8Za3BCyV4Oi-CXf06pXcb2c3tffheyCPXX2NsQvOwTMYde-GCjfWTWnAORwjDZLgUbxkoS8D7LibS6j-4UXER_owBEAeamRzlCT1fADhva0QAUhzbe82mxV46X6h1Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15aaa27354.mp4?token=ty0sdSnAu1LljXkCN20iEhd2sTAPhVReU4GJ9IIP4dP7kRmsQV5Q9hP6rjWpI89N-UiK0GxNy70_XM45dEKc4g9vjxTd32B5Vk3IZBGIwxzINsL65WYzLJbcRvHMojWzN03UHlISB4JNJhsOJDYmOPIrOLQBbQy9JFe90Ed6sVS1wYGLHt4JXokl2ja14pya3_0HM78mvoDrSLQiDdge1aM8Za3BCyV4Oi-CXf06pXcb2c3tffheyCPXX2NsQvOwTMYde-GCjfWTWnAORwjDZLgUbxkoS8D7LibS6j-4UXER_owBEAeamRzlCT1fADhva0QAUhzbe82mxV46X6h1Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسحاق دار، وزیر خارجه پاکستان در مصاحبه با شبکه العربیه: براساس برداشت من نباید هیچ هزینه‌ای در مورد تنگه‌هرمز وجود داشته باشد، فرقی هم نمی‌کند چه اسمی داشته باشد و وضعیت پیش از ۲۸ فوریه باید احیا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/129926" target="_blank">📅 23:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129925">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ در پنسیلوانیا: ایران قلدر خاورمیانه بود.
🔴
و اکنون ما ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون سامانه‌های پدافند هوایی، بدون توان موشکی و بدون برنامه هسته‌ای ترک می‌کنیم.
🔴
ما در تلاشیم تا توافقی عادلانه را به نتیجه برسانیم.
🔴
ما باید این مسیر را انجام می دادیم. باید به ایران می رفتیم.
🔴
شما نمی توانید اجازه دهید که خاورمیانه و سپس ما را منفجر کنند، اگر این امکان پذیر باشد. ما قبلاً آنها را می گرفتیم، اما آنها اسرائیل را منفجر می کردند. آنها می توانستند کل خاورمیانه را منفجر کنند.
🔴
آیا می خواهید اقتصاد بدی را ببینید؟ این یک اقتصاد بد است. پس به یاد داشته باشید که نفت ما در میانه این درگیری کمتر از جو بایدن خواب آلود بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/129925" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129924">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد و این بزرگ‌ترین مقدار نفت عبوری در تاریخ این تنگه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/129924" target="_blank">📅 22:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452666b6dd.mp4?token=D8L7ODFdhi9H9MLysxfMa49tfGc3PwWzevOyfbczVQuXZ6ut7n6TWwpY4aEGl_v01M3NPM7kstBWJ69AXwW27PAlyvBI3GKufzVWtYrTbwWHmoEwhlP-dYeNs1N4URwdKNxiCcMAI3y70OjEs0buNxTp4n0ZqJfKMBTsuGt9fYmtcSA6vlzK-V8i0yikbKD8A_43pykYHi09QG1L9_-b2AaOuLxf9zn0yf40PVJpEn8HA0coQTsgpGkkfmpL_MStw6EsAwPASjLcg3LGWu9pmF9Fy4Wf6VL8LMowehsMaOvlF9wlnXLkbYpyTGiH3jcYh6-x-aJg9XkVvYzcmDnKwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452666b6dd.mp4?token=D8L7ODFdhi9H9MLysxfMa49tfGc3PwWzevOyfbczVQuXZ6ut7n6TWwpY4aEGl_v01M3NPM7kstBWJ69AXwW27PAlyvBI3GKufzVWtYrTbwWHmoEwhlP-dYeNs1N4URwdKNxiCcMAI3y70OjEs0buNxTp4n0ZqJfKMBTsuGt9fYmtcSA6vlzK-V8i0yikbKD8A_43pykYHi09QG1L9_-b2AaOuLxf9zn0yf40PVJpEn8HA0coQTsgpGkkfmpL_MStw6EsAwPASjLcg3LGWu9pmF9Fy4Wf6VL8LMowehsMaOvlF9wlnXLkbYpyTGiH3jcYh6-x-aJg9XkVvYzcmDnKwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما می‌توانیم هر وقت خواستیم بر فراز تهران پرواز کنیم و هیچ‌کس نمی‌تواند کاری با ما داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/129923" target="_blank">📅 22:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
پوتین: احتمال بروز درگیری در مناطق مختلف جهان در حال افزایش است
🔴
کشور‌های غربی آشکارا اعلام می‌کنند که برای جنگ با روسیه آماده می‌شوند؛ آن‌ها هنوز به مرحله وارد کردن ضربه مستقیم به روسیه نرسیده‌اند، زیرا می‌دانند که مسکو پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/129922" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129921">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پزشکیان اسلام‌آباد را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/129921" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129920">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYu8O9TicZY2lQVbSyeBZttk3xtrZvgTjzjRs9jSuqeVdWMJHEx0m0WfnIyca3gakAoPBfZ-eX9Xo60N6wgssNw3ThM3-DpE7srt2VA4tLjnlhareveUplnoEW-2wlCkOSv88P0dsHpxjkw6YXHpXxdOMmgeBMEuv-Qlm84l_ZQelksZJkOGGfTOAv61cJg6dO9MxTlG6e8QlVzcFBcKFMMH7l1o1hZja20lTIQSuu9iAGCfLrlHnFI4xjANmMF1R01uB_PuFfDGZEdoId9uVTMuM0f1fyyNj2EGjNq4Jw5tzE5Qk8rBnBRY2jyPXMKTeT1GH8WTf8zm2BxD2820NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک خیلی منطقی و یهویی اومده یه ویدیو از محرم پست کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/129920" target="_blank">📅 22:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129919">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3245b245a.mp4?token=H1B24dpMMK7S3Bq53VcwtRI_8Sj3EMOk4soGkCUefZ7dRthyJdflaobg29KkjfumUX7ucqq_STUx5h-bJHaCqHJb4xqlXxV4IUqIYFvX-i2L5xsoUZ1g1CXARkWn95il3Rxi9_eNY10vli2OXf06x7SWMhr0YgeqGYzDCbQIPFMK3wosAIVP1_K4h7i2YAdOvsCqh06n13eL-vKmXOjX2h-CQREV7y5RM-oq8INVDaDpMlFgB96-9xGVaL0HFfcCAg9Hr_drrif965w79yzw-Zmb5Esel0LdzZ3OfjnbZ0sSosi4x1rFtJBOeb64TTk8kLu9-7c1U7Y4mE0NfEU0ZlN1K37Q-d46mlxo4dXhFfO7colsbpdx_M3AKvvoT7ckROKn1D-JeynsS5rn-fNbCXDWzE3E-0uXVRiTdvSUJvkohLnNzchId__VeURRddOxpkgUyKx6kna5_ZM38vMq4XgBHclUBguOs4gZvItOAWU1w_uIFU8j75RVDnoyJFL2HwECrT21oPMT2r72NvuyGZNceddf75BiDWxrCXakOvO9zD2VSi2wiKNMkMockyB1NvJyXBGSFO11VrMWRM5k6pEHRzPEXFjSm0a40hPqgbY74EtTactbl04uj9Q1ePN_pJblaSjLdLPlr4XkT8jlshFMfbq8wvtpDmb6DjtxgLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3245b245a.mp4?token=H1B24dpMMK7S3Bq53VcwtRI_8Sj3EMOk4soGkCUefZ7dRthyJdflaobg29KkjfumUX7ucqq_STUx5h-bJHaCqHJb4xqlXxV4IUqIYFvX-i2L5xsoUZ1g1CXARkWn95il3Rxi9_eNY10vli2OXf06x7SWMhr0YgeqGYzDCbQIPFMK3wosAIVP1_K4h7i2YAdOvsCqh06n13eL-vKmXOjX2h-CQREV7y5RM-oq8INVDaDpMlFgB96-9xGVaL0HFfcCAg9Hr_drrif965w79yzw-Zmb5Esel0LdzZ3OfjnbZ0sSosi4x1rFtJBOeb64TTk8kLu9-7c1U7Y4mE0NfEU0ZlN1K37Q-d46mlxo4dXhFfO7colsbpdx_M3AKvvoT7ckROKn1D-JeynsS5rn-fNbCXDWzE3E-0uXVRiTdvSUJvkohLnNzchId__VeURRddOxpkgUyKx6kna5_ZM38vMq4XgBHclUBguOs4gZvItOAWU1w_uIFU8j75RVDnoyJFL2HwECrT21oPMT2r72NvuyGZNceddf75BiDWxrCXakOvO9zD2VSi2wiKNMkMockyB1NvJyXBGSFO11VrMWRM5k6pEHRzPEXFjSm0a40hPqgbY74EtTactbl04uj9Q1ePN_pJblaSjLdLPlr4XkT8jlshFMfbq8wvtpDmb6DjtxgLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا، ملونی: ما نمی‌توانیم اجازه دهیم که رژیم آیت‌الله‌ها به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ویژه با توجه به اینکه آن‌ها از پیش — و به‌وضوح نشان داده‌اند که — موشک‌های برد بلند در اختیار دارند.
🔴
و من فقط درباره ایالات متحده، یا کشورهای نزدیک‌تر به مرزهای ایران، یا اسرائیل صحبت نمی‌کنم.
🔴
ما نمی‌توانیم اجازه دهیم. ما توان پرداخت هزینه آن را نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/129919" target="_blank">📅 22:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129918">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عضو رسانه‌ای تیم مذاکره‌کننده: هیچ بازرسی از تاسیسات هسته‌ای آسیب‌دیده انجام نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129918" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نخست‌وزیر ایتالیا: اگر اجازه دهیم ایران در تنگه هرمز عوارض بگیرد، وارد دنیایی خواهیم شد که هر مسیر تجاری استراتژیک به یک سلاح تبدیل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/129917" target="_blank">📅 21:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129916">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4723480403.mp4?token=RJ5oBf3itnwDXpuho3vIG77nvQ5vGgagNO30YQ4HcBYaL3p_Zj24P4xdyWTtnk6Uh4oOG58cjhrvNPktYnY6NvetcPb2eSyXaOe-AFnY8i6ZTcWnLxs9LVKnik0LvZzdfxIn7icGv76pHhtb6ILV53ky-I9xUdcxNmiM1ZT_94oSvxhIGWaz7cd1hl5ahP2R3ZyeM6leuQ7cOBWQKQidRyJlLYK-RrWkWAMpZiYx8GoX-dj2uq9hPKjwoP3Ffijt8JhHUMBX0HE7vFq_iM0zV9pAZsPgif3Q8L3XFJ5WuzpxIczTlY_hteNYxhDlrTCGgtSWZ808cXOECtbO3dybeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4723480403.mp4?token=RJ5oBf3itnwDXpuho3vIG77nvQ5vGgagNO30YQ4HcBYaL3p_Zj24P4xdyWTtnk6Uh4oOG58cjhrvNPktYnY6NvetcPb2eSyXaOe-AFnY8i6ZTcWnLxs9LVKnik0LvZzdfxIn7icGv76pHhtb6ILV53ky-I9xUdcxNmiM1ZT_94oSvxhIGWaz7cd1hl5ahP2R3ZyeM6leuQ7cOBWQKQidRyJlLYK-RrWkWAMpZiYx8GoX-dj2uq9hPKjwoP3Ffijt8JhHUMBX0HE7vFq_iM0zV9pAZsPgif3Q8L3XFJ5WuzpxIczTlY_hteNYxhDlrTCGgtSWZ808cXOECtbO3dybeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی این روزا میری بیرون
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/129916" target="_blank">📅 21:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129915">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ریس کل بانک مرکزی: در مذاکرات با آمریکا دو تصمیم مهم در ارتباط با بخش اقتصادی این تفاهم‌نامه داشتیم
🔴
یکی مربوط به آزادسازی منابع مسدود شده ما بود که در تفاهم‌نامه آمده بود و در جریان مذاکرات به تدریج آزاد می‌شود.
🔴
قرار بود ۱۲ میلیارد آن ابتدای کار آزاد شود و بقیه منابع در جریان مذاکرات.
🔴
با توجه به آن که در جریان مذاکرات ۱۴۰۲ موافقتنامه ای بین ایران و آمریکا امضا شده بود، ما مبنا را آن قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/129915" target="_blank">📅 21:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129914">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7PWjRen-Gb48KzC1PzuHvhnrqpwyguPkSQZpBInSeH7eljPJagNZdissDEHYef5dVf7qVZL1Jg2t4dCSPUe8120Y6UN3cOtPsrOG8gYDC2ao07iOHeWfyzigRYxx9sdxDoNZVOPW9BpfIvNx-WQGfrMOn3RRZz9BxBzgtUhvt04-bnLVjH1OLpWbmMzOZAWvcmXjH-ln5c673jUpdn0Iy-ng8Sa9BBUiIdlx4-aon1c2ETc3oP5pZHD68daop_LlShol15r2Aajto0AymQxVm-cTuH7IiBBjYg3B4c6rpvgAWQ000wTWcCux5yE0g2603o1uwW7-zz_4o24whMWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش آکسیوس، تیم ملی فوتبال اجازه دارد دو روز پیش از دیدار بعدی خود در جام جهانی، به ایالات متحده سفر کند.
🔴
تیم ملی برای دیدار سوم خود در سیاتل (۲۶ ژوئن / ۵ تیر) مقابل مصر، می‌تواند دو روز زودتر وارد آمریکا شود. با این حال، تیم همچنان باید در همان روز پایان مسابقه، کشور را ترک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/129914" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06aba58df.mp4?token=s_J7qpQzcisQh_WbJM6jfumqKiXxB02XbaE9G2Fbb2ufY7u1Wg73wEghmY368WJjEBDR0fbOQDuwqS_pjLFo3afvMnXGm8AwEiqWGBBYAHDH439bjOTxwnlicXQWr9inQruvtmb4tf2lX_9NfA6KUNdrKrX5-bJeWXSGvC7ESDB1Z8Zve2f0uzrTQz4XmjsnKGUSBMmnmsLXIm5OncT1ZU5qOuG-B9vOgkhyo2JwY6US-4C7TUuxLkxosXJCOXZkVPRKB2CFISodcv6UQKIbtgr9J94aI2IVZpJliJYLePwTWQYFwv9TKIYQLq3FMK1Z0YcSzbCBQykfI80sNLo4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06aba58df.mp4?token=s_J7qpQzcisQh_WbJM6jfumqKiXxB02XbaE9G2Fbb2ufY7u1Wg73wEghmY368WJjEBDR0fbOQDuwqS_pjLFo3afvMnXGm8AwEiqWGBBYAHDH439bjOTxwnlicXQWr9inQruvtmb4tf2lX_9NfA6KUNdrKrX5-bJeWXSGvC7ESDB1Z8Zve2f0uzrTQz4XmjsnKGUSBMmnmsLXIm5OncT1ZU5qOuG-B9vOgkhyo2JwY6US-4C7TUuxLkxosXJCOXZkVPRKB2CFISodcv6UQKIbtgr9J94aI2IVZpJliJYLePwTWQYFwv9TKIYQLq3FMK1Z0YcSzbCBQykfI80sNLo4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهباز شریف: برنامه موشکی ایران هرگز بر سر میز مذاکرات نبوده و در تفاهم‌نامه نیز ذکر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/129913" target="_blank">📅 21:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نخستین بیمار تب کریمه کنگو در اردبیل شناسایی شد
🔴
معاون بهداشتی دانشگاه علوم پزشکی استان اردبیل گفت: نخستین بیمار قطعی تب خونریزی دهنده کریمه کنگو در استان طی سال ۱۴۰۵ شناسایی و تحت درمان قرار گرفت.
🔴
سعید صادقیه اهری به ایرنا، ایرنا اظهار کرد: این بیمار، زن ۴۶ ساله‌ای است که با سابقه گزش کنه شناسایی و بستری شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/129912" target="_blank">📅 21:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjPlBAcMipW4cM4DgFhiZhOOF20v-bNvDvmw8NV3ZcqnmMdGf7bebWYSHxMmtOHCg9jVdZo_Rnh3WNIbp5w03G-_qsVz16g0KdC4QLHVVueadd7tdU_8vL27ruIv22Uz4NylNgcwuz3y8jKcTjSgRQoCzXnq9aoSax5gC9rOur0U_2LqkH24gZaVx39vMSg1vlRBF3vzZw52PcPJuJ1WPGUmFB1DrpNIywO5CodXjETERuziEpOF_oywidL_oIw7JAHRfFfOjYwdlwoRdK5FJGEUWQx5RFMJ7WEmV7-53sVc7QwfQvCQKeuWkB_C77so4aQkKa8PZ8sKA1lZ2XFWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه اسرائیل : حزب‌الله با حمایت مالی جمهوری اسلامی طی سال‌ها(صدها میلیون دلار) شبکه گسترده‌ای از تونل‌ها، انبارهای تسلیحاتی، سایت‌های موشکی و مراکز فرماندهی در جنوب لبنان ایجاد کرده.
🔴
هدف این زیرساخت‌ها حمله به اسرائیل بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/129911" target="_blank">📅 21:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: اوضاع در لبنان خوب پیش خواهد رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/129910" target="_blank">📅 21:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ : ما داریم یه توافق فوق‌العاده با ایران می‌سازیم؛ داریم توافقی می‌سازیم که کشورمون و دنیا رو امن نگه می‌داره
🔴
چون اجازه نمی‌دیم ایران سلاح هسته‌ای داشته باشه، و اونا اینو می‌دونن، و باهاش موافقن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129909" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
خبرنگار : بازرسان آژانس کی قراره برن داخل ایران؟
🔴
ترامپ : هر وقت زمانش مناسب باشه، عجله‌ای نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129908" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرنگار: شما در حال صحبت با رانندگان کامیون هستید. رانندگان کامیون در معرض خطر بالای از دست دادن شغل خود به دست هوش مصنوعی هستند...
🔴
پرزیدنت ترامپ: آن‌ها نیستند. شما نمی‌توانید شغلی پیدا کنید. ما بالاترین آمار شغلی در تاریخ این کشور را داریم.
🔴
ما آنقدر شغل داریم که در دسترس خواهند بود و بزرگترین مشکل، جذب افراد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/129907" target="_blank">📅 21:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها تو این چندساله گدا و گشنه شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/129906" target="_blank">📅 21:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129905">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: مهمترین چیز الان این است که ایران هرگز سلاح هسته‌ای نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129905" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129904">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: هرکس که از توافق با ایران انتقاد کرده، باید آگاه و توجیه شود، حتی اگر از دوستان من باشد.
🔴
آنها مشکل گرسنگی دارند. آنها مشکل غذا دارند. آنها مشکل دارو دارند/تورم آنها ۳۰۰٪ است. آنها مشکلات زیادی دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/129904" target="_blank">📅 21:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129903">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3dc624529.mp4?token=Ua0atBoOohT2d4EVPJM8r6vDCaly0XkHf6vcVxFAg_9Jr0BUgfXQo7tSLdLWXzGr3YA6VdKsmXvq9U9nAGS8nrj0yPDJB_CRZnWpjw3ygAyCDIg3AHqR0hwOrsTI8hfYOJiUMh2vOhhpAtPRzoEhPzuYXoW6bMcK7xcyWq6dL8lfbePXxbujX1eOtMgZMPhb7vBSQebekqtlevoaPxmMrTXNhjctHQmPgmls5VX4LOHvrbCZpmUMe0vrx7ojXNB8t7EHXYzn76gol1cK7Y-w1VoSbap4dzthpT9X0YWJlLQaNEKrrgjo38RgrYl8rYcUfj2iHu2qqU0OFPBNudFFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3dc624529.mp4?token=Ua0atBoOohT2d4EVPJM8r6vDCaly0XkHf6vcVxFAg_9Jr0BUgfXQo7tSLdLWXzGr3YA6VdKsmXvq9U9nAGS8nrj0yPDJB_CRZnWpjw3ygAyCDIg3AHqR0hwOrsTI8hfYOJiUMh2vOhhpAtPRzoEhPzuYXoW6bMcK7xcyWq6dL8lfbePXxbujX1eOtMgZMPhb7vBSQebekqtlevoaPxmMrTXNhjctHQmPgmls5VX4LOHvrbCZpmUMe0vrx7ojXNB8t7EHXYzn76gol1cK7Y-w1VoSbap4dzthpT9X0YWJlLQaNEKrrgjo38RgrYl8rYcUfj2iHu2qqU0OFPBNudFFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران با بازرسی‌های کامل موافقت کرده؛ اگر غیر این بود مذاکرات را لغو می‌کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/129903" target="_blank">📅 20:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129902">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66355597a0.mp4?token=lum2PTxcGtCCVx9DbfBc26ew9y5vHnMtL_3YNF7IvuT7dU98JjUaqGvWi9UQYhu8uu_n_LQgKghE8J2_RMU97yamqMCFP2O50d3786liThEqzfGF-0IpOg1UMKQ-I05leFEdQmzGqWcUUWK4PksFglFx2FxYHktvXktgfxdBaZjC1K7RND7N4KmF6Z1gsXqUl1uTzb750Y4cNCcEYnRhsR1VlBLsVCQqrYIA4D4M-t3_MjJXoWZ5kQfmB0DSaEarr4MRiJEVyRwbiygIe5X34p88yWBwvpaXEab7uEy2xZszVimsgLbhXuliToevdUHScfdDu-8xEZmPJNQ_wXbaEm0he9tzRFI-fz0u9YCAKTFsJ1qJ7hXMzQyFUF82lJ8asiZdl0Iejg2ZkY5iQ343J09tbocz95jc6Hk-n6pxh4lBDKvyINdJpqZBlDOENaBnlNXWHTeH-37pELASDrapORKOdXxLFk3_WxKf3aoN2DgbOQ9FcxNZfZgk8wuDd7Q4Ourhaf_iegvUGIaOFlJUx2li5mjZrlgYb4HNkZcS4qVffucGi0vh5aOQmw3X4VYVjWomz6X_Zivzel6EODbijofTt111vGIpHz09_JcZoyO9y4R3dC0Av2OkOy7mfIrK7cKH5DyYLU81Xy6nMlfrMuy3XZ-_sNB9xnOqvdT-IPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66355597a0.mp4?token=lum2PTxcGtCCVx9DbfBc26ew9y5vHnMtL_3YNF7IvuT7dU98JjUaqGvWi9UQYhu8uu_n_LQgKghE8J2_RMU97yamqMCFP2O50d3786liThEqzfGF-0IpOg1UMKQ-I05leFEdQmzGqWcUUWK4PksFglFx2FxYHktvXktgfxdBaZjC1K7RND7N4KmF6Z1gsXqUl1uTzb750Y4cNCcEYnRhsR1VlBLsVCQqrYIA4D4M-t3_MjJXoWZ5kQfmB0DSaEarr4MRiJEVyRwbiygIe5X34p88yWBwvpaXEab7uEy2xZszVimsgLbhXuliToevdUHScfdDu-8xEZmPJNQ_wXbaEm0he9tzRFI-fz0u9YCAKTFsJ1qJ7hXMzQyFUF82lJ8asiZdl0Iejg2ZkY5iQ343J09tbocz95jc6Hk-n6pxh4lBDKvyINdJpqZBlDOENaBnlNXWHTeH-37pELASDrapORKOdXxLFk3_WxKf3aoN2DgbOQ9FcxNZfZgk8wuDd7Q4Ourhaf_iegvUGIaOFlJUx2li5mjZrlgYb4HNkZcS4qVffucGi0vh5aOQmw3X4VYVjWomz6X_Zivzel6EODbijofTt111vGIpHz09_JcZoyO9y4R3dC0Av2OkOy7mfIrK7cKH5DyYLU81Xy6nMlfrMuy3XZ-_sNB9xnOqvdT-IPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: مسئله لبنان جدا از ایران است زیرا لبنان کشوری مستقل با دولت خود است.
🔴
ما قصد داریم با دولت لبنان مذاکره و با آن برخورد کنیم
🔴
آینده لبنان متعلق به مردم لبنان از طریق دولت منتخب و مستقل آن‌هاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129902" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه امریکا، می‌گوید پولی از جیب مالیات‌دهندگان آمریکایی به ایران نخواهد رفت
🔴
این سرمایه‌گذاری‌ها در ایران از سوی کشورهای دیگر خواهد بود، در صورتی که ایران رفتار خوبی داشته باشد.
🔴
آن فرصت‌ها می‌توانند شامل سرمایه‌گذاری‌ها... سرمایه‌گذاری مستقیم خارجی باشند. این پول دولتِ ما نخواهد بود. این موضوع به پیشرفتی بستگی دارد که در زمینهٔ مجموعه‌ای از دیگر مسائل امنیتی حاصل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/129901" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
