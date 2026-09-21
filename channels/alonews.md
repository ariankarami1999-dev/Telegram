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
<img src="https://cdn4.telesco.pe/file/ELypT830Th04NhLzYxY2_JTJUZ9oB14yBLKNW6x3fLCrPmHjM69rIO7aoFKKsO9JOvI-omLXAtP2irP80tLDbYXzGomE6MX6OM035hLOl8XxsHKhTksb-DoZd9YwjN9mVf71ci9JgdoWA3YsZP6hFfzZjAAxanDnBMUMN1ZRpxYWNrdaIM6K3ZKwwoiZRRKni6z66ybKYUVdhhs5RijU6OdQTItBSv4tDlRn1ZMwu2yfF10Zw-mMunEaxglU4sJIE30dj2PUjLnkNSMded5L2q5ZY93dRq6-py3QOfEIEC2TN3pCg2q_dPXE_tfCPnkdIfAB6HhFfSGVxf3HFCLiTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 995K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-148546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
تازه‌ترین داده‌های کپلر که رویترز منتشر کرده نشان می‌دهد در هفته منتهی به ۱۳ سپتامبر، ۲۲ نفتکش که بیشتر آن‌ها ابرنفتکش بودند، با مجموع حدود ۴۲ میلیون بشکه نفت خام از تنگه هرمز خارج شدند.
🔴
عربستان و عراق هرکدام حدود ۴۳ درصد از این حجم را به خود اختصاص داده‌اند؛ نشانه‌ای از ادامه جریان صادرات نفت خلیج فارس با وجود اختلال شدید در تردد دریایی منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/148546" target="_blank">📅 14:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
انتقال سهمیه بنزین به کارت بانکی از مهرماه
🔴
سخنگوی کمیسیون انرژی مجلس از اجرای آزمایشی طرح انتقال سهمیه بنزین به کارت بانکی در پنج استان از ابتدای مهرماه خبر داد و گفت این طرح تا پایان سال به‌تدریج در سراسر کشور اجرا می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148545" target="_blank">📅 14:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نیشن: احتمال دور جدید حملات آمریکا و اسرائیل علیه ایران پس از انتخابات کنگره
🔴
نشریه نیشن گزارش داد: شماری از کارشناسان از احتمال آماده‌سازی آمریکا و اسرائیل برای آغاز یک عملیات گسترده دیگر خبر داده‌اند؛ عملیاتی که ممکن است پس از انتخابات میان‌دوره‌ای ایالات متحده آغاز شود
🔴
دولت ترامپ نیز به‌تازگی یک بسته تسلیحاتی ۲.۸ میلیارد دلاری برای اسرائیل تصویب کرده است که شامل ۴۰ هزار بمب می‌شود. طبق گزارش، نیمی از این بمب‌ها از نوع ۲ هزار پوندی هستند
🔴
با این حال، نیشن می‌گوید برخی منتقدان و تحلیلگران تردید دارند که با توجه به کاهش ذخایر تسلیحاتی آمریکا، فشار بر نیروی دریایی و محدودیت‌های مربوط به پشتیبانی پایگاه‌های منطقه‌ای، موج دیگری از بمباران‌های متعارف بتواند دستاورد تعیین‌کننده‌ای ایجاد کند
🔴
نویسنده مقاله سپس همین مسئله را نقطه‌ای می‌داند که بحث درباره گزینه هسته‌ای را، از نگاه او، نگران‌کننده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/148544" target="_blank">📅 14:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
اکنون حملات پهپادی ارتش اوکراین به یک پالایشگاه بزرگ روسیه در فاصله 1300 کیلومتر با مرز اوکراین.
🔴
آتش سوزی گسترده و انفجار های مهیب پالایشگاه را در بر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/148543" target="_blank">📅 14:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دبیر شورای اطلاع‌رسانی دولت: اکنون با مسئله گاز مواجه هستیم
🔴
نیاز به همراهی خوب مردم داریم و در این ارتباط باید رسانه‌ها کار کنن و فرهنگ‌سازی انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/148542" target="_blank">📅 14:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFWp1lzqkh1NaLC5YXBRlP1yRsvvScJTb-0lGvGD7rSKTmSt4M4I3VQEdJIhXbpPuKwwKI0USEf2Xksn_tvolx3akz0vQ6Z4sJTj2bi_rZ7HURMX12l7woOm1l3UriJETEKDHPnnUHgmrWOhlN9AsithgJTHyX1IrQTlRyGhqlGG0TLUcD497fWCI6DfMDQZvNmDybpKxCaC_jYvpvdGK5DfsCkQ8hurNhBp9Y7GxOE6bF3lE-wOqBquAwR3qtXHKEoKpMNCrJdCtYfx03BlFvkCuLlBQADjF1xcgjb4oRKNMnD0orOpWOutZp06FHQkHYhm-X-S5z7oruNXduwXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست سردار آزمون در واکنش به دعوت شدنش به تیم ملی: خوشحالی امروزم مثل اولین‌باری است که دعوت شدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/148541" target="_blank">📅 14:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر کشور پاکستان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/148540" target="_blank">📅 14:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
تایلند صدور ویزا واسه ایرانیارو سخت گیرانه و محدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/148539" target="_blank">📅 13:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع در وزارت کشور پاکستان: محسن نقوی، وزیر کشور عازم پایتخت ایران شده است تا درباره تلاش‌های میانجی‌گرانه و راه‌های پایان دادن به وضعیت بن‌بست گفت‌وگو کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148538" target="_blank">📅 13:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کاخ کرملین: روسیه هیچ اختلاف نظر با کشورهای اروپایی ندارد که بتواند منبع درگیری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148537" target="_blank">📅 13:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpSi3IsmJ9x1t1VbRIXcRKx-KJdj2jHF9qxwXqZ6-dS6ORqcQmVbq4h4isRZZkuWqJIMzVReHrgT8Q20NLfP0U7caI92oGvLJZg12GzcQs3018k91wjYeDyQekRNWmVLL2d3JLwIj2wx0YqQtY_XJ2p5hsUn1jx_jK0awph8d8jNwuE3-oIHUeSMvObs5OwJU5Oz6qzxdlBHfmD4f9qeHGNN28LoizAKPY_6V7wsRlmAQSuJN6ABjBdZBQGZjvflEBChjKSSg3aSrnR0NH8kszQPxQypggeafLEXEUUCgDuGTil4FRuu_Oas7YRU9IXfO5xBl1Q8T25PvyJw6F4nwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شدن ستون دود در شیراز، صدای انفجاری شنیده نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148536" target="_blank">📅 13:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری فرانسه: آمریکا از صدور ویزا برای تیم رسانه‌ای پزشکیان خودداری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148535" target="_blank">📅 13:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نیروی انتظامی تهران: نه تنها مصرف گل جرمه، کِشت و نگهداری از اونم جرم محسوب میشه و مجازات داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148534" target="_blank">📅 13:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fupot13-pS50a5iDfoCRlXuSts-DkYTAN1vXDYYA_0qt_5rU_rQdV7jbteGsC9D84rhrFQ4aGFVmD1sCTUxUNBxqGl0cL7CjsNCp77c0j12X7Ba8kanAEbFkaFHrQkhx6p1d_mb6tOHrTjaewSTHHdnV2r7nii7Y_69dCcMAiVYLbnM27SoIiqBN_UWVayNMdopIo9EiLbO3Q13e1W0Wc0ktNtsdANy6oqClGfVWTYa4GA5naV3WNIwXKteuNWBI7nJj2Qbs82yVqRM_rsy4lQDBSvZjCDFpxNJQLBn5ozPy_ZJv_ODASYxTEYm165jWwMjIKctl4oxdx88F6xOO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از آتش‌سوزی در میدان آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148533" target="_blank">📅 13:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رویترز: قیمت جهانی طلا طی روز دوشنبه کاهش یافت
🔴
هر اونس فلز زرد با ۰.۵ درصد افت قیمت، به ۴۳۵۴.۳۰ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148532" target="_blank">📅 13:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت خارجه فرانسه اعلام کرد: این کشور پس از تعطیلی مرکز زبان در تهران، اقدامات مناسبی را انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/148531" target="_blank">📅 13:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl7lBzMHXBaYOfoFC0PELepNR5r80ZkJw9aLflwuFoiM-5KtKuWa2okzNgMLB1uGYBdQ8lamt9GnhDz_hR2HNd78aU58KUgCEAXL7yig7kMJBa-k_g1nYHJlZhukaYYwBg1JHJMMTGqVyPDVDixAi_Pl5iWijluKuu0X5CG91NbGiuB4cNrTqSAhCzHP-3oiSoML4R4tTw4q2MNOcPLwb4ZswEm3y_UmLgEK6HKo7T85X13JxBl9yt1nxSrp5kMuorQhTj5pkRQrfRBAygPUbS_2KmXbkUUATNRjtR1_nK2ZU_NsKVEGKGVoS1gDV7BDjbk87Hzto-gh9wdYxpeTCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اداره عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که اطلاعاتی درباره حادثه‌ای مربوط به یک کشتی در حال عبور از تنگه هرمز دریافت کرده است
🔴
ظاهراً یک نفت‌کش متخلف قصد داشته با عبور از تنگه از طریق مسیر موسوم به «گذرگاه عمانی» خود را در امان نگه دارد، اما هدف حملات موشکی سپاه قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148530" target="_blank">📅 13:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec220c9e50.mp4?token=gFWMRq61SK96OZpACcvi74QjJPsVUcCrI7j5d9BoGPJqMxO4qx1YdDsgMQTaQFJVuMaLh52opgB0OQNHrmW0-L4U71c2thmFm7HNEfyVsoT8l4IkWn4Z00zEOG3atugtNZ-6Js9mCo_Yi6Q3X_kWLSsre5pV14SDZWP1yE6QzkDX8jthqDFXumHoB5Jbg4g4HZgcWDIVcHD7Wpi8nvjXki9bQcoTrK2dyWbVJulmp8_uy7GLXGqZ5ldv3huJGnWb930FwscY8oDmLZ669Oz7SYhHBhDFy3gs0W_m7XdAWnR8OuJ1WiyiRE63VcK7olRkGmpVjCZT7JNn1Wpo8u08SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec220c9e50.mp4?token=gFWMRq61SK96OZpACcvi74QjJPsVUcCrI7j5d9BoGPJqMxO4qx1YdDsgMQTaQFJVuMaLh52opgB0OQNHrmW0-L4U71c2thmFm7HNEfyVsoT8l4IkWn4Z00zEOG3atugtNZ-6Js9mCo_Yi6Q3X_kWLSsre5pV14SDZWP1yE6QzkDX8jthqDFXumHoB5Jbg4g4HZgcWDIVcHD7Wpi8nvjXki9bQcoTrK2dyWbVJulmp8_uy7GLXGqZ5ldv3huJGnWb930FwscY8oDmLZ669Oz7SYhHBhDFy3gs0W_m7XdAWnR8OuJ1WiyiRE63VcK7olRkGmpVjCZT7JNn1Wpo8u08SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت موبایل یک پاکبان در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148529" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بهرام یوسفی فعال اقتصادی نزدیک به دولت : عباس عراقچی پاسخ ایران به نامه ترامپ را در توقف کوتاه دوحه؛به عبدالرحمن آلی ثانی وزیرخارجه قطر  تحویل داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148528" target="_blank">📅 12:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نخست‌وزیر قطر: از زمان برگزاری جام جهانی دیگر روی آرامش را ندیده‌ام. بعد از آن، هفتم اکتبر اتفاق افتاد و از آن زمان هم هیچ‌کس حاضر نیست به ما فرصتی برای نفس کشیدن بدهد. از همه خواهش می‌کنم که سال ۲۰۲۷ سالی آرام و بدون تنش باشد. لطفاً، ما واقعاً به کمی استراحت نیاز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148527" target="_blank">📅 12:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/867f2a6745.mp4?token=UclvNnkFoWbb4vNYQkeqONbG27b-hvcblsQoShsc182G287DizPqHow2MVwixDfsj95bdJhG8zLiIwCDQ1rGwP84b8IAz_N0DuLvgHlWLM3JjnHnQB0-ICjUtY-YYItuZMCTG3g1FcoPjFMcNHTaA34u2Ip4bs0cNQjVL3Q-_yq5Cemr4pivUUeTeGFFO9yAemo2IOGKQpUf_eY5SGX1bLvONx-DY2ym_dpF0MqQ2sZihapsT6Ba52BNgq8Kqs5gaV4rEspG-9hfDd4HOPbVgGqOvKetsyv-0LMY6QLXljvn8ylBxPqhkhwHYJpt-JuY2mRKJaNd_ZqXHDiC8TXqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/867f2a6745.mp4?token=UclvNnkFoWbb4vNYQkeqONbG27b-hvcblsQoShsc182G287DizPqHow2MVwixDfsj95bdJhG8zLiIwCDQ1rGwP84b8IAz_N0DuLvgHlWLM3JjnHnQB0-ICjUtY-YYItuZMCTG3g1FcoPjFMcNHTaA34u2Ip4bs0cNQjVL3Q-_yq5Cemr4pivUUeTeGFFO9yAemo2IOGKQpUf_eY5SGX1bLvONx-DY2ym_dpF0MqQ2sZihapsT6Ba52BNgq8Kqs5gaV4rEspG-9hfDd4HOPbVgGqOvKetsyv-0LMY6QLXljvn8ylBxPqhkhwHYJpt-JuY2mRKJaNd_ZqXHDiC8TXqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا صبح امروز یک موشک از داخل ایران شلیک شد؛ مقصد آن مشخص نیست و هنوز روشن نشده که این شلیک
آزمایشی
بوده یا به سمت هدف مشخصی انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148526" target="_blank">📅 12:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
جهش غافلگیرکننده بیت کوین به ۸۴ هزار دلار؛ قیمت تومانی سقف جدید زد: حدود ۲۰ میلیارد تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148525" target="_blank">📅 12:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/67d93d944f.mp4?token=FXsfwYxuSaM3zu5aVccxvQmqyGe3W9sGL9ZI9c1eGQlOqHisncMVHfCaZHxQr3E-RmjaLkwEIGHa07_yYt3GfAou7I3GMTblJaNiD4NKBz4bcc_IHYiwINsQ7SlUfCwvKFcjqPWAC4PDUv6ihcPNQKK_GJmOZAUJ9cSW2tgVh-XQO84l8CpT_N0L0AQ2HTAbU0gr0HWKXpWuCPFE1nDPr3ufGRZ7mGkuUIilG66E18g90Kkxyj33wU7oG_gl-uRQ4EoUlLNU7khQAtuzelvxBNTKXV1R_MB7xI4qPB8WU_MXS4CjMqAe3Iqyy1d7w3zokNxp4Lg7t5eOyFFq2x_M3A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/67d93d944f.mp4?token=FXsfwYxuSaM3zu5aVccxvQmqyGe3W9sGL9ZI9c1eGQlOqHisncMVHfCaZHxQr3E-RmjaLkwEIGHa07_yYt3GfAou7I3GMTblJaNiD4NKBz4bcc_IHYiwINsQ7SlUfCwvKFcjqPWAC4PDUv6ihcPNQKK_GJmOZAUJ9cSW2tgVh-XQO84l8CpT_N0L0AQ2HTAbU0gr0HWKXpWuCPFE1nDPr3ufGRZ7mGkuUIilG66E18g90Kkxyj33wU7oG_gl-uRQ4EoUlLNU7khQAtuzelvxBNTKXV1R_MB7xI4qPB8WU_MXS4CjMqAe3Iqyy1d7w3zokNxp4Lg7t5eOyFFq2x_M3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای مجددی در داخل یک انبار مهمات در منطقه
العیس
در حومه استان حلب سوریه رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148524" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💢
قیمت بیتکوین ترکید</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148523" target="_blank">📅 12:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lg0wahOMSzBewHzb-0KBuFLW2xn8CE7JJIesN1dNWknXi-5id4YZgbGQsbbkGSNVre_DGdhdfC8s0FJzf9ZoRE6NskuQEs-jmPfHhd3b_iAu_CUkz2j8QK8Yy_Lfhvp2UvdkWgdCHhJoBAcbuYa4R0u27_H-lYEGG59bJS3qyOorurBXtLoTSjBQ2PwaoGbWPLewst6B70ctu0B0EuzKNNvgcf5-3fdasEBEsE141Nr3O9S_Dn0_TB1zw5hzOb7ev75SX_3y7cwZAWTG6EHvPqFUplM-DVknzEXYVns46HxnuEADfAW9KWNFxdx9NOom7lKc1MebMRTEfY-ZPmUOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUftpSHaQeUgTmUAb2m-eAfgK4NM4q_44wSW57cVL2Fd3aHztEF6iOHBmFqg8H9GThekfVaULpdEbfgpHgZi4sZ6UQLLoJabnyQ160xG13h2sH95RLaiVmuceZuRTAeWpJeFgGOG_RJofGPFFXokn6m7iF5refR7Yj-CeJXyD9ReomLGPcLID1v52HQCca0xf0rr5OXcikqTXqDRjLvSMtXAgEwhp7lOI0_2Hk68fUqY5NLvjIjfJks-EaQw79BQxoSOFkJ5zR13vcQnKl9DmqasePbJWGc34WWD8Is7qgc21awpHlSEi_WKYI6dn6eiz8nrIy7kHzOUSwJZmJr40A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای مدل A330MRTT متعلق به عربستان سعودی و یک پهپاد، پس از انجام ماموریت‌هایی در نزدیکی مرزهای یمن، به پایگاه هوایی ملک فهد در طائف بازگشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148521" target="_blank">📅 12:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148520">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اکسیوس به نقل از منابع: در جریان تماس ترامپ و زلنسکی، رئیس‌جمهور آمریکا بار‌ها از همتای اوکراینی خود خواست حملات به پالایشگاه‌های نفت روسیه را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148520" target="_blank">📅 12:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کارشناس صداسیما: مردم میگن اگه اقتصاد هم در اثر حمله دشمن نابود بشه ذره‌ای دست از نظام و کشور برنمیداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148519" target="_blank">📅 12:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmmZMUGcazTtROENoj1HWbALgg_mC36BYeBh_C0m0ZuKWLkTupuBpAGs1_vWKFv219LSAtgMpYaj6Kwug3xIuSj_eyJSqCnmBJl8lJstfcF088E6OpLg52OpM8aQtVaXo4U4nToLUqEKI9-P3UUJiG1eYDh9kBVABxDWmendo27wlAk9QPm-3BNfX08bWJI2ZHfKnDf7zjxC48nSwPlGWF_ReUpGWYvdYFVZ2yiRpyJgQH-VdTi3p4FplZ81MwCNCAHypcab_8EvMlH5xVQ0D1TMaTtWyF1FCCbUvOgoikLHiXp_Y4j-7SQJuT9M_Qkpt5SYQUXbi-tEvLWBEx2fEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس: ایالات متحده به عنوان بزرگترین تولیدکننده نفت و بنزین جهان هم، قیمت‌های سرسام‌آوری را تجربه می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148518" target="_blank">📅 12:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148517">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی حماس: آمریکا با صادر نکردن روادید، مانع حضور هیئت فلسطینی در نشست مجمع عمومی سازمان ملل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148517" target="_blank">📅 11:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پزشکیان فردا به نیویورک می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148516" target="_blank">📅 11:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نیروهای یمنی(حوثی ها) موشک‌هایی را به سمت مواضع نیروهای همسو با عربستان سعودی شلیک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148515" target="_blank">📅 11:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نخست وزیر قطر: ایالات متحده همیشه متحد استراتژیک ما خواهد بود و این چیزی است که من مدام تکرار می‌کنم.
🔴
ما معتقدیم که اتحاد ما مستحکم است و هیچ چیز نمی‌تواند آن را از بین ببرد
🔴
تجهیزات ما آمریکایی است و ما به آموزش‌های مشترک خود ادامه می‌دهیم
🔴
ما به داشتن رابطه قوی با ایالات متحده و ارتش ایالات متحده ادامه خواهیم داد. و البته، این یک همکاری دو طرفه است. هرگز یک همکاری یک طرفه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148514" target="_blank">📅 11:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سناتور جان کندی در مورد ایران:
فکر می‌کنم حدود شش ماه دیگر از آنجا خارج شویم. بعد از آن نفت ارزان خواهد شد و تورم در آمریکا کاهش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148513" target="_blank">📅 11:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f645472.mp4?token=e2xuK7CVOTOPpHmX9zG2jMeHWf0Kb-K_bukNVJgIqPLYbX4xMH9CwIniJJe38wffkUIN77P16FMJvr8wGYR-nCfXyXXfOPuKUDbnanOUNeD5F1RnrmUaj-be3igB9C8DQpXn2t0Rp4-SgzNpoGJcyPXg72OJtbJklF1_ppRNQGAqpLu7WazdRr9QZs1cLJllD8aY_S_CDLmIco__vubUoEIdjAxDnO3cRwKnzr5Tz5bqre2GKlmFsUkyHH_JknNQ00DqV73K7VQ3wE0yWE-7bb04N3-ZUHFhUTv_zu7_-QmeGF-NPR-Mqz2zXeplmC2KsnTuWVnfh5m9PXjVFfjElA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f645472.mp4?token=e2xuK7CVOTOPpHmX9zG2jMeHWf0Kb-K_bukNVJgIqPLYbX4xMH9CwIniJJe38wffkUIN77P16FMJvr8wGYR-nCfXyXXfOPuKUDbnanOUNeD5F1RnrmUaj-be3igB9C8DQpXn2t0Rp4-SgzNpoGJcyPXg72OJtbJklF1_ppRNQGAqpLu7WazdRr9QZs1cLJllD8aY_S_CDLmIco__vubUoEIdjAxDnO3cRwKnzr5Tz5bqre2GKlmFsUkyHH_JknNQ00DqV73K7VQ3wE0yWE-7bb04N3-ZUHFhUTv_zu7_-QmeGF-NPR-Mqz2zXeplmC2KsnTuWVnfh5m9PXjVFfjElA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جان کیریاکو، تحلیلگر سابق سیا:  اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت!!
🔴
صدها هزار پناهنده افغان در ایران هستند و هرگز تابعیت ایران را نخواهند گرفت.ناامیدند و اسرائیلی‌ها همین افراد را استخدام کرده‌اند.
🔴
این‌طور بود: «در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار. اسرائیل هزاران نفر از این افراد را استخدام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148512" target="_blank">📅 11:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148511" target="_blank">📅 11:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e412d99b5.mp4?token=UtQk13YB4yObJyIdPW2ZfiIazitE1xrqyo2toQGAdqHW3KnJbag-hikl4IfCIo2zkQVfvX45rHo4DnZXdp4BfEiFhmsALjGu8e9Gj0AHsJrXwZOcYTEGOENT8Bud07me5zyCs-fYSa5NFddon2uBALNVc7YkG45d0CGMsmlUr-eAbQvPubC5RSiSLZUeI8yuyAP28OzCws8d__jKVeTKaVqlybJl5RnC6tnENQJha50r8KGgDuAfsZ2Dh4YUb3jpY7qdz5v8FUS1S5gn60nN4ndgfLCxgRs4yhW9dTUqC5C5Iwb53knZMXRoYUjiv7Lvb9PorCmsouFDfXx9raNfMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e412d99b5.mp4?token=UtQk13YB4yObJyIdPW2ZfiIazitE1xrqyo2toQGAdqHW3KnJbag-hikl4IfCIo2zkQVfvX45rHo4DnZXdp4BfEiFhmsALjGu8e9Gj0AHsJrXwZOcYTEGOENT8Bud07me5zyCs-fYSa5NFddon2uBALNVc7YkG45d0CGMsmlUr-eAbQvPubC5RSiSLZUeI8yuyAP28OzCws8d__jKVeTKaVqlybJl5RnC6tnENQJha50r8KGgDuAfsZ2Dh4YUb3jpY7qdz5v8FUS1S5gn60nN4ndgfLCxgRs4yhW9dTUqC5C5Iwb53knZMXRoYUjiv7Lvb9PorCmsouFDfXx9raNfMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما قیمت کوکائین را اعلام کرد!
🔴
کیلویی ده میلیارد تومن!
🔴
پلیس مواد مخدر تهران بزرگ ، یک بار بزرگ کوکایین کلمبیایی را قبل از پخش در پایتخت ، کشف کرد
🔴
این کوکایین‌ها بیش از ۵۵۰ میلیارد تومان ارزش گذاری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148510" target="_blank">📅 11:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یک آخوند عوضی کثافت: با دختر رضا رشیدپور تحریک میشم، رشیدپور قیمت دخترت چنده ببرمش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148509" target="_blank">📅 11:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14f346d3d.mp4?token=gZgfS9KpKQT790r5iLQ84pnG8cPxs3qfT5kPrWNvyIsxLFnTLjZi8LS2-xodEKAP_fgLt58VcJTEFeua15kCXaNzQIYQXUjeHH8ogagSN3BB8XGgt7-rLf9TP_2FE9yvhBpEZgxXSQkZoTArGSgcCy5DQqrH4-TZ3z9Uoa1qjBaMCfPB00C9R7lSbdC35WjPc4yrQbD-uDEnT6kelgs3gWqypGgdA8rWivwXuH9sdFiUu8uMYr27oDw7cY-zqkfSmm9lKZ9wnuDIvQIqKpF3ZvA5sq29ahJ0J541ievK_P6Iko1xSlrLR80RlnBiSljTolZkjKDmbkAysRqofAYjXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14f346d3d.mp4?token=gZgfS9KpKQT790r5iLQ84pnG8cPxs3qfT5kPrWNvyIsxLFnTLjZi8LS2-xodEKAP_fgLt58VcJTEFeua15kCXaNzQIYQXUjeHH8ogagSN3BB8XGgt7-rLf9TP_2FE9yvhBpEZgxXSQkZoTArGSgcCy5DQqrH4-TZ3z9Uoa1qjBaMCfPB00C9R7lSbdC35WjPc4yrQbD-uDEnT6kelgs3gWqypGgdA8rWivwXuH9sdFiUu8uMYr27oDw7cY-zqkfSmm9lKZ9wnuDIvQIqKpF3ZvA5sq29ahJ0J541ievK_P6Iko1xSlrLR80RlnBiSljTolZkjKDmbkAysRqofAYjXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند عوضی کثافت: با دختر رضا رشیدپور تحریک میشم، رشیدپور قیمت دخترت چنده ببرمش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/148508" target="_blank">📅 11:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8VuV3hP-SCHmMhwlw6coQ_Q8Yv-V95WMtnhv_qWcFXem9lw-Vr7aM4Fkcpqv4jMTT-AwdMdWh9T2M-k-4xbzsssfVIop8ruwqFleExmrAqC1Kn3VZuiBNANKQOQd46LKkBofhjZr1y8Bf6waAAYX5DrjsrkQdoIQjBiIS7WBUHLQnTFM-ghDN-UFrRbkR4G5N2TKEc65VqIhYmUpP3hVP63W9pRtJHyKBUmP9Gg4Cs0Rvgg5oJmgtMDu8e1iyJAtjm1UW-RThAWVNZxXWOs4ZZyUes1PxeCa9LQvZ_9mA6CqbFiSajQ9Z6TtP_1ikHqJbb8O-zFjxAT5e8YFvzIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استاد گودرزی: پارسال که نزاشتن پیاده تا آرامگاه کوروش بزرگ برم اما امسال میرم
🔴
هموطن راه در جهان یکیست و آن راه راستیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148507" target="_blank">📅 11:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148506">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c35e79706.mp4?token=iKzIHJDImRvSPidkpcxEzK99eS1ew3X0DfBZUnt4pxKipH0XRDvqFLv7Pd4M1XJbas6zUInbvM5SnvJ7x7Yho2wtxXz7RUQPH__JefrrUS7rcjpCdYVmGVeN8anga3KtCblo3MoTB8nLbn0f8ZKprh1PJhYKZd5KAvvsS7Au7ofGaRSVqvLsbfHKdUUGZeNwN7zAqBFLPVVK6MzpDwTa7WF6lQRktojSZgvJYj_LxI6e9M3_Hu65znFuvPIRprfPA0_kTVLvnItMCktHypQ8XSMGNkSkoDicRDFB6h-vKKTZPNa-1Iy8C4c3wA1JUbfouvfwodofFhMTqA5OITGLvXTDMHP2eMuxGPKk6Os_BW_mM-0tDq_kHV8IsfI68HKybCtOXzJiXKSnPge9uf-7qkMuKlOX4gYNTy0FpUyfwP5sAoe-F4VizAboJvP-phl_LwH_qSCN0cQmjZ-nz0dQI2R6MtqlnjUXnBhQ4Dr87qA9pjNvzqTQtEmHlbcNKXJ6opAoaSdSk0iPCT0YPHEaDEANfn05vLERJjzAZ0nqmq3K_5JX2X6addG4h1Ni-YsxOJUz4j-3RRrc6wgAEXI-NWVXV-zJeApa254pWcOfa9zNLi1A2ebL6CI0zKpVjewMeXZwsdh0dQ6IY9TrgjH05Mn0enPhmvXKtLekyp6aYVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c35e79706.mp4?token=iKzIHJDImRvSPidkpcxEzK99eS1ew3X0DfBZUnt4pxKipH0XRDvqFLv7Pd4M1XJbas6zUInbvM5SnvJ7x7Yho2wtxXz7RUQPH__JefrrUS7rcjpCdYVmGVeN8anga3KtCblo3MoTB8nLbn0f8ZKprh1PJhYKZd5KAvvsS7Au7ofGaRSVqvLsbfHKdUUGZeNwN7zAqBFLPVVK6MzpDwTa7WF6lQRktojSZgvJYj_LxI6e9M3_Hu65znFuvPIRprfPA0_kTVLvnItMCktHypQ8XSMGNkSkoDicRDFB6h-vKKTZPNa-1Iy8C4c3wA1JUbfouvfwodofFhMTqA5OITGLvXTDMHP2eMuxGPKk6Os_BW_mM-0tDq_kHV8IsfI68HKybCtOXzJiXKSnPge9uf-7qkMuKlOX4gYNTy0FpUyfwP5sAoe-F4VizAboJvP-phl_LwH_qSCN0cQmjZ-nz0dQI2R6MtqlnjUXnBhQ4Dr87qA9pjNvzqTQtEmHlbcNKXJ6opAoaSdSk0iPCT0YPHEaDEANfn05vLERJjzAZ0nqmq3K_5JX2X6addG4h1Ni-YsxOJUz4j-3RRrc6wgAEXI-NWVXV-zJeApa254pWcOfa9zNLi1A2ebL6CI0zKpVjewMeXZwsdh0dQ6IY9TrgjH05Mn0enPhmvXKtLekyp6aYVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ مبهم مدیرعامل توانیر به احتمال خاموشی برنامه‌ریزی‌شده در زمستان: امیدواریم بتوانیم مدیریت کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148506" target="_blank">📅 11:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / وزیر کشور پاکستان راهی ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148505" target="_blank">📅 10:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
جورجا ملونی، نخست‌وزیر ایتالیا، از آماده‌سازی لایحه‌ای جدید خبر داد که با هدف ممنوعیت پوشش کامل چهره شامل برقع و روبنده یا نقاب در مدارس و اعمال سقف قانونی برای شمار دانش‌آموزان خارجی در هر کلاس درس تدوین شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148504" target="_blank">📅 10:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA4oSkKn0uFYKm_09Swpoc8gb8pNQBQ3lkVXBpnlNOCKgQ6fUHD-02OMj_gDPOX4G9x_lN0PfHjAbWAZcDKsp6F8lKUcwbDpJ2NDCdYZST6P7-UtL1aMQyPgk2ONdP93l33EJIcAZEbKwbcHl53UHtCfY0a6mH9tBKkyHqqBpBot3YG2yRPJ5B4CedC5vencB8M7BjpmdtJN8P5KGHHvtAp-GI_9MF4voda5rChCwcllG4KFsm_fNRsNNRTThukrNjpR_QyVeZdviC6hdHllAOCZtDnApmV1NdNxAyfDG97hISYVyuG9YvigTW5Sb2fBj-rmu6-Lp0LJwbW8Rub1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: ‏۱۸٬۵۵۲ دستگاه خودرو، به‌عنوان پارت اول از ۱۵۰ هزار تاکسی دات‌وان، بر اساس جدول زیر میان ۳۱ استان کشور توزیع می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148503" target="_blank">📅 10:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رئیس سازمان غذا و دارو: واکسن آنفلوانزا در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148502" target="_blank">📅 10:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات دولت آمریکا گزارش داد که دونالد ترامپ، در خصوص حمله به جنبش انصارالله بسیار مردد بوده و پیش از لغو نهایی این حملات، نظر خود را چندین بار در این باره تغییر داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148501" target="_blank">📅 10:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سخنگوی سپاه: جنگ تمام نشده و ادامه دارد. سپاه پاسداران هم خودش را برای یک جنگ طولانی‌مدت آماده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/148500" target="_blank">📅 10:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7M4A2nSvQ5Me7-QmBq7s9Orhdd82-q3RdCdXBdSoAccDetjmaw1swPXaiO4PSEFBWsHRncYGZyeCEjQEFT_qvnrp419XIv7hPQb7QuJcvHDQFYVv7wpcNwB4fHaOZCKKvCbkSEvvjDLGTVinfLSO6R2q8szxPVTKo_rNWCJvMtzWoj5z0LtPsXqlEnymem2RK0YIz_uudAZL6x2_xCAfH8Oc2JYvjm3g_rBjPTs9McqQPjc9ZUKoqHWcSD5cS-YiISzlEEeR6EP3o1bVF9qaGrag8vwCQAAcMQsRXZ4tYxNIFcOfR_16GKLU6BiNtIcWmsdUS5jd9BA2eV47gWapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر خبرگزاری فارس: درآمد نفتی ایران به ۱۶ میلیارد دلار رسید؛ دست دولت برای حمایت‌های معیشتی بازتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/148499" target="_blank">📅 10:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aquVWMvcf_aXyhhcqhc2uaS5kCCQfD_BgHBDfXSZhuSdS4rSqucDlhwW7O1wHjldk4pbndPo6eWZwn4ZxP1ntUTFcgDLtk8v3UZR13UW08QP5oj3IqkId-BcqCRugc_ZVNGup7NvRiXqFk6rzWKLBhWrOYUzaZTQs1PjaWMlOHqs1Vz4YQuL3D738WwRq9epMMaO1tN1NK6fFYZzC24_2KIeIL036GBGG9xtPoKrb2v0HKkS-BhrczKdqX39oxZiisTMqwSXMwa2VdAWCe2bWZpDEwyIEf0fL487ZrBBWqeAIk8DJOoSawT-_-lthluHASYqTXN3zMI1HE3t12bYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شغال کثیف قاتل ایلیا کوچولو به قصاص و اعدام محکوم شد
🔴
جوان۲۳ساله معروف به «شغال کثیف»با صدور حکمی قاطع ازسوی قضات برجسته شعبه پنجم دادگاه کیفری یک خراسان رضوی به قصاص نفس،اعدام،تحمل۲۰سال زندان و۷۴ضربه شلاق محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148498" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
به عنوان بخشی از تلاش‌ها برای کاهش وابستگی امارات متحده عربی به تنگه هرمز، شرکت راه‌آهن الاتحاد و بندر ابوظبی، یک سرویس حمل و نقل مستقیم بار راه‌اندازی کرده‌اند که ترمینال‌های فجیره را به شهر صنعتی ابوظبی متصل می‌کند
🔴
این مسیر به محموله‌هایی که به فجیره می‌رسند، این امکان را می‌دهد که مستقیماً از طریق راه‌آهن به ابوظبی منتقل شوند، که این امر زمان حمل و نقل بار را کاهش داده و کارایی زنجیره تأمین را بهبود می‌بخشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148497" target="_blank">📅 10:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
معاون امور زنان ریاست‌جمهوری درباره مصوبه اصلاح مهریه: تعداد سکه تعیین شده، مبنای کارشناسی ندارد
🔴
نسبت به این قانون ایرادات متعددی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148496" target="_blank">📅 10:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
آنا پائولینا لونا، نماینده جمهوری‌خواه: مذاکرات درباره ایران مستقیماً میان رؤسای دولت‌ها انجام می‌شود
🔴
بهترین گزینه برای آمریکا، دستیابی به یک توافق برای پایان دادن به جنگ علیه ایران است؛ این موضوع به مذاکرات فشرده با دولت‌هایی نیاز دارد که کانال‌های ارتباطی با تهران دارند
🔴
گفت‌و‌گوهای مورد انتظار ترامپ با رؤسای‌ جمهور چین و روسیه، مسئله جنگ با ایران را هم در بر می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148495" target="_blank">📅 09:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کیهان: اتفاقا همین حالا و وسط جنگ باید موضوع حجاب را جدی گرفت زیرا آیه حجاب در میانه جنگ به پیامبر نازل شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148494" target="_blank">📅 09:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پزشکیان خطاب به دانش‌آموزان:  می‌دانید که شما گوهر هستید!
🔴
من از یک خانوادۀ معمولی به اینجا رسیدم.
🔴
شما اگر ذهن‌‎ و فکرتان این باشد که بهترین شوید حتما می‌شوید. ما تلاش خواهیم کرد که شما بهترین شوید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148493" target="_blank">📅 09:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgFnv6nGpPDEjVv1CrAh7PjoTptNiP6cf5z7CyUUs8ujFqfZJLeOMq2F4m7dQC6075TP6Gkz1sjYNb-P5X9iYlHvkMI-lDciVMFC1aEzwLuoPrfit4Bgqj1O3NKviOA10UnAAx94lXDZhmzULOcc5NtRN7HEM66_AXp4_inQJfe_JYQI3xGE4UZK2_AsGVWlM8ja88iHYUtB7pI1KEaCgIYKmhnumx-USVYmLzvmsynZPGNYswPlPg9AjJPnKJx_dV4UzEToyF8tbVNYzqjVxmGuV1AuQo7UqN_geyg7eWn_QjdicYNI-IYaDSHGHaBW-f8muvDoJtUo-VAJ3DVcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت داده‌پردازی کشتیرانی «کپلر»:  حرکت کشتی‌ها در تنگه هرمز در آغاز هفته کاهش شدیدی را تجربه کرد.
🔴
۱۲ کشتی حامل کالا طی روزهای شنبه و یکشنبه از تنگه هرمز عبور کردند، در حالی که در آغاز هفته گذشته ۳۵ کشتی از این تنگه عبور کرده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148492" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: درِ بازگشت ایران به میز مذاکره همچنان باز است، مشروط بر اینکه این مذاکرات با حسن نیت انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148491" target="_blank">📅 09:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibD9uIHzRzxdypIwYGGrU6e8jpRZ4zKyKp5C8jL2j9q7FhcDzRozSCh8I-GWhSKBBG5QwdYrhcetgZ_CXinqyaZJyciHkU9r1luqp1aNxR53NZOVZcmUcMUMqvQRv_vMOCaF31kpW5YNhyKwuHkSfdP1eFZFEwdC7vfqVLz5M6N1pY8NG2ie4K_Y9WmaUfl6QNP4czsWYlwtMPgbdig4a-mqHLTPBdz4gVXr8hC1PhvBONRTphJ4wEPFJ9mN9Tlp2qfcsV2pM5ZXviMmBL6GX0hhmUZ1Ev0eydoClgnyWjNup9JOZcVpgBwu0Gqb6Eqvyo1DhF4wDba9wGj1V2i2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل منطقه اطراف ارتفاعات علی الطاهر در جنوب لبنان را هدف حمله هوایی قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148490" target="_blank">📅 09:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9LORCYKRvdQdTAd5LS-2ymlFkVaPrH2C-OONapH9UjlwfJrEVA47VCAarTTBFVEBob77n1EWTrZReyLOfbFt8Z6wtlC8bevgmCm1Yrjjmqer7tXH--axCzNq13UPAZJW9Sp6EwzW10egaRVVLKUZ-Vk7cnU3OAILqUjmTbJqdOesdN-jQrJOYA7TgEhwkbipUa36KVE0pMk3RVCohMVodxbE0Y1aWZx1ChKQIeuY-t0KpWfWgQTUqdGR3BEai00PDE1JkoRDZho9qyZEd87HVoUV6JAvQuC1NApRAK397vJP6NmUgWqfSthilw_jhFo7Gg3Sj87H8-7bUtWpl0BPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی پاکستان به شرق افغانستان
🔴
الجزیره به نقل از یک منبع دولتی افغانستان: جنگنده‌های پاکستان به ولایت کنر در شرق افغانستان حمله کردند.
🔴
در نتیجه این حمله شماری کشته و زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148489" target="_blank">📅 08:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سپاه : لحظاتی پیش انهدام یک پهپاد MQ-1 در آسمان تنگۀ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148488" target="_blank">📅 08:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpC2tNIMExLq-3cVICW9OELS7UqH0uA9wq_ZZRVmu3bEfBSA7-Lrebp4cxlwJf_DhcNK1c1-olVPuDSz0S2FT6gurW8gPvuRpHkLyDcNsQ9F1c0kBEb6KxPG0TGWSg5gARkj-eJTBUEkSdDoKyfbzZDtKznhGDvGqqFuVAn_9pT8UV5NYYImsvCI-zc70OCD18RGSQVoCpd3DpFw_7OoKVCZI3e3G4xilpIJyZKr6nXSCSFdB8zC7fP6PhHxm_MH-TsC73jmXrC9xMRXn2yyzrVQRu2PNLZ4vnmUxcfBbG7PrmWtdJWVGz7ftuOgPRKH4yFXH8AQ2GxJzDSiAmDE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: قیمت بنزین و بیشتر کالاها در دوره بایدن بالاتر بود
‏
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، با مقایسه وضعیت قیمت‌ها در دوران ریاست‌جمهوری خود و جو بایدن، مدعی شد قیمت بنزین در دوره بایدن به‌مراتب بالاتر بوده است.
‏
🔴
ترامپ همچنین گفت این تفاوت تنها به سوخت محدود نمی‌شود و به ادعای او، قیمت «تقریباً همه کالاهای دیگر» نیز در دوران بایدن بالاتر از دوره ریاست‌جمهوری او بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148487" target="_blank">📅 08:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148484">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6VmyhU6R6iAx87K2RnpsP7MG_GsKqdYAeFTcBo_RVlL_7-9qlAR9WRW6HlNurQc2oejQcote4xPCAfDveQqAZKhHsXLMyU3h9EL1Kl0UFGFipXXeIE-zMlJzP4xvsQDyBaQ_GXYU9a_4Bqk-6BHUcyDzmS6x-U-GSqHidX8OTFaaCVHlj8JISD4oVWE-79L_hko3fLcOMEDRUxAFv-Ko2ej_4O0U8JL5XQ1uRZ_in8ZcBh5NeaRGGTNz8FRWwWg7DLS0cBaH_1GExw2Lhkggr-gfmlVE6CZXUaxhh_7qsd62klswKt4LKvxrkFGHhebd-EDYSeijn0ML6qck4r9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۱ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/148484" target="_blank">📅 08:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148483">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEBhDSzLdjzaAC4NiEuiwaA7iDCyGG_N9jyiZ25KH8ebqulIzgmNoogL473zbZ076nlCH5mD2yAtsf0ytYwN8MwqLrJsbwO2OjN4BDEs2EJ6X56TMQ_YKNp1IvDm_HO3F4HF-buGqqpcUElIq2etNKMSIFDlolFGIihqFILtdMvQi1_x84Ah9dV0Ysebo6bY2eEMKEXzFJ5eDNOEuFLq03cH-V3LFshMnyLRVW7R3Xx-QOz8MDk-lbNP5PMogjTgoFrN4epFuXEdtgvDt_OiyaNZqlqQtL-NA0vNdBGHwMr-QH2SlCpXB0UdgCNRBX-SLFNzeGW4CMrUUSAbPEKBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تنگه هرمز ظرف دو سال آینده بی‌اهمیت خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/148483" target="_blank">📅 07:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148482">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJCC3gt1fShD66YG112j32FT1OXXp3pmzaiiToa9O5ydVxJNmK07EPhBufkXOoOjNZjxH_IMNrqRCgWKBkwMZ-j2c-_ZGfEovxdni_xL7t5LtPctX15nHVL9v0ynvz5HHUiSLTAd2JyvZsy9fTFvTuqNjXV8YELKNJkM52Md-oacJTv95gz1YS3YSivXal7vZVEWqumaYE1wcauoz431wXvdJbD3qCLAHSqo7CoeIPmMQbf-cQS8ljywP6eiT_4OKJxeDwsLgzhF_9b9USbMCG8S78KPBz_lESKRkGoYFOYDALDPZ28d9JOnwitUWc7ZOBGFo--drUbmhuwz0a7pYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس:
شماری از دستیاران و حامیان مالی سابق
کامالا هریس
معتقدند او ممکن است در نهایت در
انتخابات ریاست‌جمهوری ۲۰۲۸ آمریکا
نامزد نشود.
🔴
آکسیوس با
۸ دستیار و مشاور سابق هریس
گفت‌وگو کرده که
۵ نفر
احتمال نامزدی او را کم دانسته‌اند،
۲ نفر
شرایط را ۵۰-۵۰ ارزیابی کرده‌اند و تنها
یک نفر
انتظار دارد هریس وارد رقابت شود.
🔴
با این حال، هریس هنوز
تصمیم نهایی خود را نگرفته
و همچنان در حمایت از دموکرات‌ها فعالیت می‌کند و با مقام‌های این حزب در آستانه انتخابات میان‌دوره‌ای در ارتباط است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/148482" target="_blank">📅 07:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148481">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsyRwQKPNZKC11DkCLcN8ldfi3jaNgRfh374l3qbRXfPuh2P0o-oPtYkRe2gzCDuLJPDPB6H2AU6ZNHWKrP97bqSkzawC_Q8IPzkf2C6RjUpUq1CuLlIfWpl0W1yFKaGRvWkK1eAUNVvOR30aVw03-zk8fU-rfhP05s2N-02FWKVvquYtdAFD8a8_Z_9gLAJHnmgQCIp81TjIGo33qlNtTf3-0qfUXNGIL1zBExt5PcHGTpgWN4Lg2LB-n5_8PvXUhxyEmVjkon1-8B3TGC3Ubrg-6YQO2Jz0qN8p_iyEP1EDeiInMXmZwjb6jAx-u877CKNrdZuRcwq7z-Xq6OBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/148481" target="_blank">📅 02:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148480">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f25a1f47.mp4?token=RUriKayR-5vtvyErcGjYEH1sDgl-AkERZUE7NKDd3CFYkesFsrw-eX7E843cnKYsdSZfX8eeRxTnahBaOjNKUA7oWHuzyaPCs5m55c5LtH4dhndbao44vLXko5VFtRyRDpdfnjC01ApBJdsTaEX5vwKmAqd3WWEXkNxUcN9MYyHdcbBaCj2llWvUXgnuQ71ewvFEt0mRX6XDVq0fwZAKDJ-AJzaQYarxo-Od4Zc0lTUycL2LDfUgPhv6_br6N91bZp74MbsMsPVYis0n2q2zJV6khF2vxifM7zhcDTi5keKawLQ0Wu2D3u1CsXrNPeDT94hE6lJgQ4vaOiVy89QbGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f25a1f47.mp4?token=RUriKayR-5vtvyErcGjYEH1sDgl-AkERZUE7NKDd3CFYkesFsrw-eX7E843cnKYsdSZfX8eeRxTnahBaOjNKUA7oWHuzyaPCs5m55c5LtH4dhndbao44vLXko5VFtRyRDpdfnjC01ApBJdsTaEX5vwKmAqd3WWEXkNxUcN9MYyHdcbBaCj2llWvUXgnuQ71ewvFEt0mRX6XDVq0fwZAKDJ-AJzaQYarxo-Od4Zc0lTUycL2LDfUgPhv6_br6N91bZp74MbsMsPVYis0n2q2zJV6khF2vxifM7zhcDTi5keKawLQ0Wu2D3u1CsXrNPeDT94hE6lJgQ4vaOiVy89QbGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار انبار مهمات در اطراف حلب، سوریه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/148480" target="_blank">📅 01:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1ac39bc78.mp4?token=t7MeXavsehpkIl3UUaFDMzU6O18jnoH8LjIpcQCZgQ2fZWCjuEJjfHMgeRxosMurpB7c4HnwffwhQyFr9BzfuGNeoyTULx75vXSxt2sT-ssV66pyrzHMWLl1VpsT_5gH4jUzgmjX8aJVpgTNutOqd-UEtZBq0yXUtej6r21I89GHNTMkgzWF-nVqwtJdQ1kjJe4ba_rhOt1UIBwg211aIsd_gWuVCnqZFUKetUzfILqEQSfzqqqk1gFHvawkE9ZPNO7RXriJ7BOOuyAa_1oAlmf4Akc3-Cd1d9gmSDoR5Lnt30jXCvXidYqoC1gRLdZM-VLN-wA_LXgKzQwnNHME4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1ac39bc78.mp4?token=t7MeXavsehpkIl3UUaFDMzU6O18jnoH8LjIpcQCZgQ2fZWCjuEJjfHMgeRxosMurpB7c4HnwffwhQyFr9BzfuGNeoyTULx75vXSxt2sT-ssV66pyrzHMWLl1VpsT_5gH4jUzgmjX8aJVpgTNutOqd-UEtZBq0yXUtej6r21I89GHNTMkgzWF-nVqwtJdQ1kjJe4ba_rhOt1UIBwg211aIsd_gWuVCnqZFUKetUzfILqEQSfzqqqk1gFHvawkE9ZPNO7RXriJ7BOOuyAa_1oAlmf4Akc3-Cd1d9gmSDoR5Lnt30jXCvXidYqoC1gRLdZM-VLN-wA_LXgKzQwnNHME4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو آسمون مشهد هم بشقاب پرنده دیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/alonews/148478" target="_blank">📅 01:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148476">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7acf398c7.mp4?token=hy6UjUj7JPitmwz57jZw30NMLpGm93lQNXr3vm-ui7SdNSCspmQ1dyMFMiJwaOocjSwIlOQs_YulQDaGeNz8yHID-pHGV_aaQN_Wr2NAk4uXKNSARenxazowQuVzgYNsOViEWdcUv1CAptQQStnKINPrueALuOrsYHAgUMqX3QlGK_lQS10Ll7P-y2hl03PVv6x2OhLhkkPVL2xnSEotao6CJzjeoPhm2Mk8bSNSsK-t84L3jsSdcpOlMzC21XSSFby4mKm44iwV3o3LUF2YmDvru9HxLWtU6SeVeYYpcFzn0iXMATYFpGUz6tSlsjUi12oW-qbqxOaovw-rutw_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7acf398c7.mp4?token=hy6UjUj7JPitmwz57jZw30NMLpGm93lQNXr3vm-ui7SdNSCspmQ1dyMFMiJwaOocjSwIlOQs_YulQDaGeNz8yHID-pHGV_aaQN_Wr2NAk4uXKNSARenxazowQuVzgYNsOViEWdcUv1CAptQQStnKINPrueALuOrsYHAgUMqX3QlGK_lQS10Ll7P-y2hl03PVv6x2OhLhkkPVL2xnSEotao6CJzjeoPhm2Mk8bSNSsK-t84L3jsSdcpOlMzC21XSSFby4mKm44iwV3o3LUF2YmDvru9HxLWtU6SeVeYYpcFzn0iXMATYFpGUz6tSlsjUi12oW-qbqxOaovw-rutw_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل در آسمان تهران شی شبیه به بشقاب پرنده دیده شد و بسیاری از مردم گزارش کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/148476" target="_blank">📅 01:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148475">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
هم اکنون فعالیت‌های گسترده سوخت رسان‌های آمریکایی در خاورمیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/148475" target="_blank">📅 01:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148474">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">علی رضا تقوی نیا، روزنامه نگار نزدیک به سپاه:  وضعیت کاملا جنگی به نظر می‌رسد و آماده‌باش صد درصدی به نیروهای مسلح اعلام شده است.</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/148474" target="_blank">📅 01:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148473">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd5cJDI4EpncXKGjdt75dJuomZ2HECkbI6O34expBwZjJ7WQ-wEPFFRpCpY1PSeBoAeFnXy5ZCQGNa1gGsF3P8yfcyZxVAog_3_WHnpKHub1jASjaQ_GK8zOtrKZieHnTnrNXak4N59CBdeajI-F_57atIckJGRSoyuOdYmiUcNa_7Q04RHqIkJ4CC0y3KU7ndGI4DSL7E04rSat5Xug1fZMapW6D-1W22801VRR02LSL5YR30GHMbgoHKPrYB9MT8D9mPhwX3XkLq0gJNOAnvrLkdTyJ7YLNmg4CG_mWSrKYU-Z3NHCCfs3GmqpHEeac2VRBi6JboKL1e5hQu0_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ترامپ:
نیمی از جهان متعلق به ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/alonews/148473" target="_blank">📅 01:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/alonews/148472" target="_blank">📅 01:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148471">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: بزودی همه چیز مشخص خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/148471" target="_blank">📅 01:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148469">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خروج از ان‌پی‌تی منتفی شد
🔴
عضو کمیسیون امنیت ملی مجلس میگه طبق نظر مقامات عالی، ایران از پیمان ان‌پی‌تی خارج نمیشه. این حرف رو در حالی زده که بحث خروج از ان‌پی‌تی مدتی‌ست مطرح شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/148469" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148468">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTP5sSCVL5WwpThypMwTdUehBzJDL6zq7Acau4LdVSnIx_vso4oHsrqZ8l4k-3pwN6Zdb8PVJUhSUHajaEmku4pbmIXY-Z3TDy9R3Bo9qvORb_3HbVNou_vbuC0Y6ytMKxZ7m-2U_yjfg2Imhzxtz4zJgec978Wc4mpadvxHLxUdYYIh4U_-MWWFzYRg6e_rRdobdx9PiB1KiNT88KWglg8g5fQDqyE53mWav420Il0IJnx0yrPFMJlNTnLoVlXw0gJ-6oaSSfi-n1v-6-cE2PUdxFKpU86K7xiB6Y9yONTLDHrg2c3YTvBJP52sK8v-WWPrKUcR_qtW7TD_iOsDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت‌الله شبیری زنجانی درگذشت
🔴
وی جزو مراجع تقلید و در ۹۸سالگی فوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/148468" target="_blank">📅 00:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148467">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-iCK5wmo73kSRvOWcvX45X9tybqXlqw3YdKOsbMJ4Jnd6xzzCdX9hQKMtGBFIKt5nc-jkzlgql4MJ9Fk9EuyPsCXrcdg_Axh-e6PZH9rhGiVpWqBwFf7wDF-3UPDAboGj_7kZyGVgQR4hXR8QKElOCQF0QN8L4NQK01QUSnY1K-hZ1wUDDb22Dwyh5jKaoTLxANVxUD5NBEcc5xawgIDDP-ALutgvUl7NKuOt4XzynrGGIM6P_9HrDrYdLXwA7yQkpmzF89yWD0Cvx-c56_33MB4RyOmkZBo_J-EHbtkSvPGl4rdQWW2wRyS6-OYQAn4tjmewg38WGmxRdQ6knutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط تتلو ۳۹ساله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/148467" target="_blank">📅 00:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148466">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP9iRsrM69k0SNrM4ovGyLRslhry9Pd3iLr0cqKTZHfa1gXsq24GB_-TBtVnKdlSn7BwixeC8DqRQdq0TKJU95yX1VyQ00wcoPEX49AXGLPLSRMqVFx8RGEHJ8oYsQuMQ3_FHE4OnQYDW37kBL_l0g4aV1SWQJj5PXyFjo6NOINLv_elK2mxsrjHudzR4T4w649WJ44wloPqJzzqkSVwOGfCFFBGwzIQGij1UzOjCBFUwFCu686v3hkaC_dgRxuf2XIHWbwLikudUXIrw7vcREufVJJeuJC-izfsnqLDZD7WGtTP1MW67aNHdkVDmgLMjKpVCN9LQPrZ3SOe44VY8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
طولانی شدن جنگ تقصیر پزشکیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/alonews/148466" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148465">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دیشب محسن نامجو که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه
«کیر،
خفه‌شو»
دهنشو بست  [@AloTweet]</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/148465" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
یاشار سلطانی: سپاه، دلال نفت هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/148464" target="_blank">📅 00:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148463">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وال استریت ژورنال: آمریکا تحریم‌های گسترده‌ای علیه دیوان بین‌المللی کیفری وضع می‌کند
🔴
وال استریت ژورنال یکشنبه شب گزارش داد، دولت دونالد ترامپ رئیس جمهور آمریکا قصد دارد تحریم‌های گسترده‌ای را علیه دیوان بین‌المللی کیفری وضع کرده و دسترسی آن به نظام مالی بین‌المللی را قطع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/148463" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148462">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/148462" target="_blank">📅 23:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148461">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/148461" target="_blank">📅 23:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148460">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / گزارش شده است که تجهیزات نظامی و تدارکات لجستیکی ترکیه و پاکستان وارد پایگاه‌های سعودی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/148460" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148459">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر انرژی قطر: اظهارات وزیر خزانه‌داری آمریکا درباره اینکه تنگه هرمز ظرف دو سال آینده بی‌اهمیت خواهد شد، «اشتباه» است
🔴
تنگه فقط برای انتقال نفت و گاز اهمیت ندارد بلکه مسیر مهمی برای انواع تجارت محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/alonews/148459" target="_blank">📅 23:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزارت خارجه فرانسه اعلام کرد: این کشور پس از تعطیلی مرکز زبان در تهران، اقدامات مناسبی را انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/148458" target="_blank">📅 23:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148457">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_jrksX28m8bC-M8ABgVNQEURr938gL88n3UYyssMePVgv6GmO48QPtTRbzUKmT9JIuqZgteJhAJhrkA9xjMMSav-a4G_0qbBRnyXz7oF7hAg6ASjZe2cePVTxiKSxciKeNy6SH3KGOhtLKL28xAtHzOnjgUwPuABULVOL-KQlo_uqIrE55WHVUsD4NewDz3T6UJ1y7XDP0u7-kpW80Fg0BY3WWViQx52FPmPQdQpeLUheEaug7r-TxREdWi8QTl1beHaWP33gU5_EjtJNf1ET3OHcrmknvQoRgHmNnf6FH_gcq06GC7643lY47o0G9jpdByT3ou2m1w3T7zXyHMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / منابع عربی: آسمان اسرائیل به طور کامل کلیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/alonews/148457" target="_blank">📅 23:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6mi6v7hAzSw_xDK8kURc-IGFWnQWDY9a64sWJHMRR4ZGDzR-YmqO0HDMVW0OJDDVh8IEMI9FvkCJmhP9O8Bv-w30T8pIQJ10n7RRUDcrlQRTaFLwO_buIw5bsinjBfXXkYMKjmzDFM1qfQAzdP_c4spqSZA6Oi_IH2AslIIn5Um3XvV-gLlnR2Qdto4f3OxhxVBro-8uKcobe-OSEVs9e31LCy35LzVvMjm3tx-c7CyqYyxou2sAsn9Banm0f_QSPKtBVg_9V0DE3W5V2prUPMrZZtxWW9TQCP01jyRcsfz5cCnhlSx5yXSPEewLgyMf3N1vB2J9Ra3XPEDA_Ltfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلهکی:  تحرکات جدید برای مذاکره از سمتِ آمریکا، بخاطر وضعیتِ بُغرنجِ دولت ترامپ در انتخابات آتی این کشور است؛ «آمریکا اصرار دارد ایران باید تا ۴۵ روز آینده وارد مذاکره شده و همه موارد را توافق کرده و امضا کند»،
🔴
«مباحث هسته‌ای از روز اول مذاکره مورد بحث و بررسی قرار گرفته و روی آن توافق شود»، «تنگه از سوی ایران باز شود» و آمریکا نیز متعهد می‌شود مذاکره تا قبل از برگزاری انتخابات آمریکا به نتیجه برسد!
🔴
دستاوردی هم که آمریکا برای ایران در نظر گرفته، «رفعِ محاصره» و «آغاز نکردنِ جنگ جدید با خسارات زیر ساختیِ بالا»ست که هیچ تضمینی وجود ندارد که بعد از انتخاباتِ آمریکا، مجددا ایران مورد حمله گسترده آمریکا و متحدانش قرار نگیرد!
🔴
باید دید ایران از خطوطِ هسته‌ای _یا به بیان بهتر ۷ شرط برای توافق_ عقب می‌نشیند یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/148456" target="_blank">📅 23:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
هم اکنون پرواز جنگنده های ارتش در آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/148455" target="_blank">📅 23:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTL4Au0FOJD3tQH_98ShrADpiyXZIe2UvMjShHZTmm1w1BExQr7FgEeHjme01tiJTzLQMiikiLND5c61LzWG4Pei9yISxyiLowYT467RI6h7daAC-5VpbIkuyRkfNhZvQSemEJ954TFAvpPiHD7otUmWswk3_BXp8NgH3o5qafiTHZgwq1-KqTvBTpCtrLC-aMUG2copz8yZJHMAqbd6fva9jwJybdEFuHSrjQ9HCDoiaXv401OtehpmjjMgwW_WloK1Xn5cmbRvqLjXyQdvEPh_ixkYJ1ajXApv0mYH0Fe-IBS0sKQw0hTnlO9dLk_EEV2c9MjmH0ZvzweC52UtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت مجازی آمریکا در ایران از تمام شهروندان آمریکایی حاضر در خاورمیانه خواست برای احتمال لغو پروازها و بسته‌شدن حریم‌های هوایی آمادگی داشته باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/148454" target="_blank">📅 23:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرنگار دولت: ادعای ترامپ برای دیدار با پزشکیان آرزوی محال است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/148453" target="_blank">📅 23:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبر لغو پروازهای ایران و عراق از روز سه‌شنبه تکذیب شد
🔴
به گزارش خبرنگار مهر، طی ساعات اخیر اخباری مبنی بر لغو تمام پروازهای هوایی میان فرودگاه‌های عراق و ایران از روز سه‌شنبه در فضای مجازی منتشر شده است.
🔴
در همین راستا، مجید اخوان، سخنگوی سازمان هواپیمایی کشوری، در گفتگو با خبرنگار مهر ضمن تکذیب این خبر اظهار کرد: تاکنون هیچ اعلام رسمی از سوی دولت عراق، وزارت حمل‌ونقل یا مراجع هوانوردی این کشور درباره توقف کامل پروازهای میان ایران و عراق منتشر نشده است.
🔴
وی تاکید کرد: ادعای لغو تمامی پروازهای میان عراق به ایران و بالعکس فاقد تأیید رسمی است و این خبر تکذیب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/148452" target="_blank">📅 23:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
انور قرقاش، مشاور دیپلماتیک رئیس‌جمهور امارات: ارتباط با ایران ادامه خواهد داشت؛ به‌ویژه با مسعود پزشکیان، رئیس‌جمهور ایران
🔴
قرقاش تاکید کرد باز نگه داشتن کانال‌های ارتباطی با ایران می‌تواند به منطقه برای عبور از ماه‌ها درگیری کمک کند.
🔴
او دیدار اخیر ولیعهد ابوظبی با پزشکیان در حاشیه اجلاس بریکس در دهلی‌نو را نشانه اهمیت حضور «صداهای عقلانی» برای بازگرداندن صلح و ثبات دانست.
🔴
این مقام اماراتی در اجلاس رسانه‌ های عربی در دبی گفت: «تا زمانی که خصومت‌ها متوقف نشوند، نمی‌توان آینده را بنا کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/148451" target="_blank">📅 22:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDvp9yr27LruhftOpxTqiKnf43D2w3g0dTBU-MdCqWehxhltDqUzfO9iPQLupBU0T_ytcSdQf9EUUN3gzxU39eM7gSE7r3yHhn2_91XD5RjzICpr1K3hEw3ezlCevNignK7XgGEyhXPfvlfeA6Ei0Y7vNAj7EMYStMjHRcQ70rtMC-SUrLJ-IFDKMQoxs3ecCsXk2SI3HG5RuMM4X2hx9iD8K0_vZnPfns-QjWgV2nsGOPGe0FK_-SwKSPI5oHWAqZfEH5qLWs-vlL7aviIFWJZI3lyRkE6xI9n3g_0BfgN8bszxeFz_Mah4E5Dpdpz_wL8VYIjVGzoS2BRDp7_kgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدعلی ابطحی: اجلاس سازمان ملل جای مذاکره و احقاق حق مردم مظلوم است
🔴
اجلاس سازمان ملل بزرگترین‌ اتفاق سالانه دیپلماسی جهان است.
🔴
از پارسال تا امسال به مردم ایران ستم شد و ملت ایران سرافراز و سربلند باقی ماند، آنجا فقط جای مذاکره و‌گفتگو و احقاق حق مردم مظلوم ایران است.
🔴
گفتگو و به دست آوردن‌ رفاه برای ملت تحت تحریم وحصار اقتصادی حقی است‌که مردم ایران طلب می کنند و‌ دیپلماسی جای حل آن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/148450" target="_blank">📅 22:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
این وسط وزیر کشاورزی به ازبکستان رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/148449" target="_blank">📅 22:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa73_ywftp1lBA9bC9-h4OAu9WciXtrywm3PXtc0qMTSZgTFe2M6s56XkSkstjATNhyR8tr5qtswd6ewbkHhu1uJ4Ghm1RDz8cZ2DaBpYoLewWsYjjjdir9z6r_8sjqjXTlRP40YhGMFFNqai8xfuTUjQ9fFovx5Y9tVXghY74wi1rmWXu37WOCZIfEfbOuIUg2y52yo8bKq-RP_vNk0-2c5No5f4qswaVhyUcLuPbf9m71OHk8_2x3QF_E42k3yeF0xXY9eqEobIlAfm0uwBcrAAHnr6QtJFKE-X2L2Vvufabhm8ICR9gJ1ar6XPIgH7ZO--c9tSkFh91k_eMZfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی از دوحه راهی تهران شد تا یحتمل امشب راهی نیویورک بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/148448" target="_blank">📅 22:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
آذری جهرمی به پزشکیان:
سفر نیویورک را لغو کن و نرو!
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/148447" target="_blank">📅 22:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148445">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvCdTm-Ej6x6f4193VTSx9soC4hTorWtMcQm0xbEK-mgm5eHIheZ2pS1W_xpNOoWKncv4HY362zVRGdPogMe7ecF38bwEnesoupQAsClAA5wQ9OsxQfaCN0JjOf_XXiciavs9FMTcrTj-KVaI-Vzi9un9ORBNH-I7NR0gZ47w2p2xVMrEZAsxaDUL4diJCKUbi34Agb8wWbj97IRxbzaqH5ep-6yb4pVm5hTUal6vOmeeEQyUWy4MtCO5DspLXaHVBt3VXwGT2qiAd_xcPStTh5j0pAHjlL7-cSgT36MGJzG3xMYiMRFzgfO8LSQ5XADDrRiD5vM-BMcR7uvqSguTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsrvwSJ1vbZh1zLt1G4W7XEhDWSV65fSYMlvXkaR0AXhSmQYqbBWwuvM_gm44G9afo2ykl1YDoVHQGh1crUjNspM7jQPOAYlgEpYvElxWuMe3emZj4IKH1lGJe2OhTRbMxByBqsle9xpQAFQI9ggrXAjK1MIZGrf8eBqzvWdjmHQNe8d6HCOj8mcTbHcaI6TDyt8DXwWfxjQQrMPqXKchTvQ5adT1geZ75iBzits8P9NBdHx8xd6RBbvbsaJw646L29eT7TnIWLgnWZzkzy6ndotWCd9jrPMffKBRgGY9OeivJDEJfOB4yCzlE6LJbiXQzR0xW0noN7fP7VpGJMfLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که امروز صبح گرفته شده‌اند، نشان می‌دهند که عربستان سعودی به طور همزمان هفت تانکر بزرگ نفت را در پایانه های رأس تنوره و جوایمه در خلیج فارس (معادل حدود ۱۴ میلیون بشکه نفت خام) در حال بارگیری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/148445" target="_blank">📅 22:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148444">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ولودیمیر زلنسکی رئیس‌جمهور اوکراین:
من تازه با پرزیدنت ترامپ صحبت کردم. این یک گفتگوی مهم بود و توانستیم درباره بسیاری از موضوعات بحث کنیم.
🔴
ما توافق کردیم که در نیویورک دیدار کنیم و این دیدار می‌تواند تغییرات قابل توجهی را به همراه داشته باشد. یک پویایی دیپلماتیک در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/148444" target="_blank">📅 22:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148443">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که جنگنده‌های سعودی در ۲۴ ساعت گذشته، ۲۸ حمله هوایی انجام داده‌اند. این حملات با استفاده از جنگنده‌های F-15 و تایفون از پایگاه‌های هوایی خمیس مشیت و طائف صورت گرفته است
🔴
این حملات مناطق طعز، الجوف و مأرب را هدف قرار داد و در مجموع، تعداد حملات هوایی سعودی‌ها در طول این درگیری به ۷۶۰ مورد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/148443" target="_blank">📅 21:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/148442" target="_blank">📅 21:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/148441" target="_blank">📅 21:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88138fc09e.mp4?token=a5Bku2IuwYROvwVD3MtQpd15B3LQ7CAasvvK1L1v9tQzJPdz6hqHxv7n700Hc3yh7GKDLXXXvX_9Wj8KJ8lC5IGQmbwEl7YD-6gas0o_5n2bj5mf4dR_2BFwhdayXWTt-9M7TXKT6FnhfhixYtP3ycn6l0J6bWCDbNqbM1m776KOjqFVs4pu8Pw20XoO2zzzn7161wVAPn_IHroj3_yb0GwkeSj6Wk9eqftlYpnETOD7GxSM2JgK8fNpvhujk0iM0ApOa7Yd2akBT03jlW7hAZ1wJHKmHKEFXZZDJIXEN2o1ooOqyo416Uq19r1mUmFVUCzqC4IDxmCQtZ3XEHOucA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88138fc09e.mp4?token=a5Bku2IuwYROvwVD3MtQpd15B3LQ7CAasvvK1L1v9tQzJPdz6hqHxv7n700Hc3yh7GKDLXXXvX_9Wj8KJ8lC5IGQmbwEl7YD-6gas0o_5n2bj5mf4dR_2BFwhdayXWTt-9M7TXKT6FnhfhixYtP3ycn6l0J6bWCDbNqbM1m776KOjqFVs4pu8Pw20XoO2zzzn7161wVAPn_IHroj3_yb0GwkeSj6Wk9eqftlYpnETOD7GxSM2JgK8fNpvhujk0iM0ApOa7Yd2akBT03jlW7hAZ1wJHKmHKEFXZZDJIXEN2o1ooOqyo416Uq19r1mUmFVUCzqC4IDxmCQtZ3XEHOucA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بر باعث و بانیش تا قیام قیامت لعنت
#رقص_میله
#رقص_پرچم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/148440" target="_blank">📅 21:43 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
