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
<img src="https://cdn4.telesco.pe/file/Mqp4b6MVJutlKUoaHv3Sd5VFu9uSE30R2iJsqVub6gWTOZ42nClqmjnCKG-ohFdRxFLL75yY2PEIhHyVtGAugG9fBrP3id2j-i2libHd3TWahGb5uJKacBODhbAgcl0NM0PyT8_UEgmR_jva7nw8_-4HxcaO1R9U2mlJaFEDdXeeZ8H2Fc0BKE3pNEuPhZD7LlcFvtDz9_qDJX2T0_-8JYfHY6dBcrR9oGW-ia9t4oL1hzOfsTiLlZBF4__POWilEeGmvxXhCGIFMLgFM4JutPqX5NW5WwVRtiRX2z_PM49yxhY5ucBD0O8MGPPAnaU5GhoEU5RN1dQHySaR8FyHzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 955K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
<hr>

<div class="tg-post" id="msg-129548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
جی دی ونس، معاون ترامپ: پیشرفت قابل توجهی در ساعات اخیر حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/129548" target="_blank">📅 16:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129547">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ونس : همه رهبران بزرگ دنیا اینجان
چون ایشون به ما قدرت داده که راه‌حل دیپلماتیک برای کلی از مسائل مهمی پیدا کنیم که برای مردم آمریکا مهمه
🔴
ولی فکر می‌کنم برای کل دنیا هم مهمه دولت باز ما حرکت می‌کنه و برنامه هسته‌ای ایران رو ادامه می‌ده
🔴
همه این کارها از قبل انجام شده
🔴
سؤال الان اینه که چقدر بیشتر می‌تونیم با هم انجام بدیم؟
🔴
می‌تونیم ورق رو برگردونیم؟ می‌تونیم تغییر کنیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/129547" target="_blank">📅 16:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQWr_yjCB096OYvr6txnVKsQwlBfAM0dJ8-mRGaxnM-8OTX37h46TnTs2-SO0ZXJ0wE-w-_mY_QfgYJkOZhPW3ob8SnE9aNDMiXB8YfoJdOgJzukYUtDdAp9fTp6WG_jhmp7U3JCZ4jxMpdaiJDzbPnezFojPX6XKwT4_26mZn-uXm4p1ohiNZJJXTLFpPlsCNK74icD-plpzqi6NT93fBYOEQlj7OjgnZKxLyTNAkccUNk9t-go007yFiBv8G2-0GeDbvY2XjAHR7kdNy-Lsl2PzlM4sQtE9FWYI0PoQjX2nXB5u-dX_rZZJE2aBFhDlCCPqCPJyVqcmuciAIqy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت تتر همزمان با شروع مذاکرات مستقیم ایران و آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/129546" target="_blank">📅 16:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ایلان ماسک : هوش مصنوعی داره جای و شغل آدما رو میگیره، واسه همین دولت باید مستقیم به حساب مردم پول بریزه تا اقتصاد فرو نپاشه و تبعات هوش مصنوعی جبران شه. حالا با تولید ارزون و انبوه توسط هوش مصنوعی و رباتیک، تورم کاهش پیدا میکنه و حتی ممکنه دچار تورم منفی بشیم، پس دولت هم چاره‌ای نداره جز اینکه بین مردم پول پخش کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/129545" target="_blank">📅 16:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از دیپلمات آگاه از مذاکرات: میانجی‌گران ابتدا درباره سازوکاری برای نظارت بر نقض‌ها و حفظ صلح در لبنان بحث می‌کنند
🔴
در مورد اعزام هیئت ایرانی به سوئیس، مقامات قطری به ایران گفتند که اگر هیئتی اعزام نکند، عملاً به نتانیاهو «حق وتو بر جنگ» را داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/129544" target="_blank">📅 16:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش تازه دیلی میل به بررسی احتمال تغییر رویکرد روسیه در جنگ اوکراین و بحث‌های مرتبط با استفاده احتمالی از سلاح‌های هسته‌ای توسط مسکو می‌پردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/129543" target="_blank">📅 16:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مصر، ترکیه، عربستان سعودی و پاکستان بیانیه‌ای مشترک صادر کردند.
🔴
در بیانیه مشترک وزیران امور خارجه مصر، ترکیه، عربستان سعودی و پاکستان آمده است: بر اهمیت دستیابی سریع به پایان مرحله بعدی مذاکرات تأکید می‌کنیم.
🔴
تأکید می‌کنیم که تلاش‌ها باید نگرانی‌ها و ملاحظات کشورهای منطقه را در نظر بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/129542" target="_blank">📅 15:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وب‌سایت «زتیو» به نقل از منابع آگاه: ترامپ به شدت از نتانیاهو عصبانی است؛ او گفته که دولت اسرائیل سعی دارد او را فریب دهد تا دوباره جنگی تمام عیار با ایران راه بیندازد
🔴
رئیس‌جمهور آمریکا به شدت در این باره فحش می‌دهد.
🔴
در حال حاضر، او قطعاً از اسرائیلی‌ها بیشتر از ایرانی‌ها عصبانی است
🔴
حملات مداوم اخیر به لبنان، ترامپ را بیش از پیش به سمت مخالف فشارهای تل‌آویو سوق داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/129541" target="_blank">📅 15:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emQtrb9-JwCnuYW_qqIp5YY_F4pCOKd_gqdKROQKFBlYwTODh4HzVTYXCztVTbE7do_ZvthA1u7OSZs5D3APhwLE5ORjNnlIJhm5waGzenEkVTMZ1rm8oKwVaRO8EjZFukYN8EH9oMpv0eV3NhuGLeaZ_YD8dQo57Ls-YeStWcfy9yXbX9TUozu9mAJcSPZtPOakZsgyBnMI-oxfZ_0n7sONyllnFzvjX3eusSpTQXsk5w20MvL2hJcrklDJUSLPr7cGzJLUzQ1xk9uNHbnMPqJO5J3XOI4wrzgE6S3Wh76L1Rk7MQbv0rhhByqqfr1TfI2pwiO_x6zDjpQYi7FvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ روز پدر را با تبلیغ دولت خود تبریک گفت: روز پدر مبارک! کشور ما عالی عمل می‌کند. تعداد مشاغل و بازار سهام رکورد زده، بهترین اقتصاد تاریخ! بزرگترین ارتش جهان، تا به امروز. ما در همه جبهه‌ها پیروز می‌شویم، پیروزی‌ای که هرگز سابقه نداشته است. خدا همه شما را حفظ کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129540" target="_blank">📅 15:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
امارات به عنوان اولین کشور عربی، استفاده از شبکه‌های اجتماعی رو برای افراد زیر 15 سال ممنوع کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129539" target="_blank">📅 15:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=h5Mk7o3qluMmrIWNK2ND_TOcOYk0kiOPa05ybAf2YAH1WH_30yoBgn33wQUG7LVJiR1w6nfYyRjw8d3o-DzIDUE2RUZFvhEpdo3k8KRmJwmtnIWIt5jK-2DascvR7dkEQ_-P8wl7htArv-XApBLM4hDYgHuYXxcPQTezXwffO0bWWLGlzANwgbgDWz4ftSj-6mhlWvAd0YhCu_81402HsSVfeyTOO6nq0Qj_uuPSdvB5NFxTRUMj_lYTSgvIY5EDv-VbcNSG8oZnUhCK6Am-vzo-gB4WNPXH_tO1BoWpEHUwtG6CUZFICEo1-RS3pCp8R5wkyywqlNmSsE9iSsmjTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=h5Mk7o3qluMmrIWNK2ND_TOcOYk0kiOPa05ybAf2YAH1WH_30yoBgn33wQUG7LVJiR1w6nfYyRjw8d3o-DzIDUE2RUZFvhEpdo3k8KRmJwmtnIWIt5jK-2DascvR7dkEQ_-P8wl7htArv-XApBLM4hDYgHuYXxcPQTezXwffO0bWWLGlzANwgbgDWz4ftSj-6mhlWvAd0YhCu_81402HsSVfeyTOO6nq0Qj_uuPSdvB5NFxTRUMj_lYTSgvIY5EDv-VbcNSG8oZnUhCK6Am-vzo-gB4WNPXH_tO1BoWpEHUwtG6CUZFICEo1-RS3pCp8R5wkyywqlNmSsE9iSsmjTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت فعلی در سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/129537" target="_blank">📅 15:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129536">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2df66b5d.mp4?token=JQRfsbKWlfoIpzOYhh1I3ffF-fxjCLsIYH24OjSuFhgBO1nTKloQlVh8i15Nutskcb2Ist_VUsiB7kWa_ccv_ioMVRlIMgLJF-EEamBJUiVLHcCwsf_xRUJT3z3u2VFJl_4NRKM22z1m0vFmcqG2vonFkd5jgmk7_BHnMUBlJz7remN4G7TKHMi1A0SG4E1EKIGcpwGVkBU5ipjhEBAcE96V-Di94YGm0d8hxrhBQl5FuqD7ukIObQcjvOVmx3gLrOADB0s8S9l_L2c-Ddf8Vw4aQQ7Auz_ktN1xZOSJQdm7ta2ixLgelg6x1I7trErM8-VX-kobdMIOpJzpVhN3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2df66b5d.mp4?token=JQRfsbKWlfoIpzOYhh1I3ffF-fxjCLsIYH24OjSuFhgBO1nTKloQlVh8i15Nutskcb2Ist_VUsiB7kWa_ccv_ioMVRlIMgLJF-EEamBJUiVLHcCwsf_xRUJT3z3u2VFJl_4NRKM22z1m0vFmcqG2vonFkd5jgmk7_BHnMUBlJz7remN4G7TKHMi1A0SG4E1EKIGcpwGVkBU5ipjhEBAcE96V-Di94YGm0d8hxrhBQl5FuqD7ukIObQcjvOVmx3gLrOADB0s8S9l_L2c-Ddf8Vw4aQQ7Auz_ktN1xZOSJQdm7ta2ixLgelg6x1I7trErM8-VX-kobdMIOpJzpVhN3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شوک در حزب‌الله
گزارش‌ها حاکی از آن است که محاصره ستاد کل حزب‌الله در جنوب لبنان و در ارتفاعات «تپه علی طاهر» در حومه نبطیه، باعث بهت و سردرگمی در میان نیروهای این گروه شده است.
بر اساس این ادعاها، نیروهای ارتش اسرائیل موفق شده‌اند به یک مرکز فرماندهی زیرزمینی و ستاد اصلی حزب‌الله در جنوب لبنان، که گفته می‌شود با حمایت جمهوری اسلامی ساخته شده، نفوذ کرده و آن را تحت کنترل بگیرند.
این محل پیش‌تر در دوران حیات سید حسن نصرالله به‌عنوان یکی از پایگاه‌های مهم معرفی شده بود و در همان زمان نیز موضوع رونمایی از موشک «عماد ۴» مطرح شده بود.
در ادامه این گزارش‌ها ادعا می‌شود احتمال گرفتار شدن صدها نیروی حزب‌الله در این مقر وجود دارد و گفته شده ممکن است تعدادی کشته یا بازداشت شده باشند. همچنین اخبار تاییدنشده‌ای از بازداشت حدود ۳۰ نفر و انتقال آن‌ها برای بازجویی منتشر شده است.
حزب‌الله در تاریخ ۱۸ آگوست ۲۰۲۴ از شهر موشکی «عماد ۴» رونمایی کرده بود؛ اقدامی که در آن زمان به‌عنوان نمایش قدرت و پیام بازدارنده علیه اسرائیل مطرح شد.
در حال حاضر نیروهای اسرائیلی در حال پیشروی زمینی در این منطقه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129536" target="_blank">📅 15:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129535">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
گویا علی الاصول راجع به مسائل هسته‌ای هم مذاکره خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129535" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129534">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: آمریکا درخواست انتقال ذخایر هسته‌ای ایران را مطرح کرد و ما به راه‌حلی با عنوان «کاهش سطح غنی‌سازی» رسیدیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/129534" target="_blank">📅 15:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtg-0jfbL9xdh_w-V4ngVrrnNy5ml_DLjlm4UW8n9Wa9s14EMFsN_qY9mHbIG1YvHiUq-3IpI340O_xPeRVyNt2n7nDN1jmu5N5lJUKdGBAxbJEICRumO2roxC6OLk7NoXXQd_046vzNaRDhTE17AWerNIBQZq3_NzS68C1uBCcfSd-C5F_1N16jo3wSNzXM9kc2RywJf1-ZdRbbrMenrfGJE_71_1l6vH01L2B1U7IObha1pebsoN_RQ6aAXx6preJLN192iRNHkjns-s4T_6p5Y9qB9lhzTjwVEXqcfw6oTmZz3cTsSzf135IDwIVSEpep1dyxyeUBVWvcGiChXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون سوئیس، جمع پایدار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/129533" target="_blank">📅 15:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129532">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW_tw_LAnWZ88mAXBnJV1KhEFx_1XOmoxO1lVNAp0FJnaqn3sH9Jmo716EF4ep55d3DKdm6uSupDgaGjtmagIk7-n9jx3icd2hnaO7Rx1NToobuJp9CmyTlT4f1mGTOXCsQqhu3i-GKhzYau-k7zuAQm3oonWmn4F-wnuCqUIgA3-Pb4EiERmuVRovPyWgT3F8KN3g_qxb5AwKXk1jMxNNlPaMNxKh3Tehbxv8UTWpCGqMN2qvmgLfH6TTQesgSPbzNXFkxH8ltTV7fI8OM_deEyDpgKhFww92Dj_5NI8ctggexJ0l-0oT6ZgSn4jCLxWiwmAH1HBikZOAzggP3TUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت عالی سد کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/129532" target="_blank">📅 15:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129531">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزیر خارجه پاکستان به الحدث:
🔴
ما موفق شدیم آمریکا و ایران را به گفت‌وگو ترغیب کنیم و به آتش‌بس دست یابیم.
🔴
ما توانستیم آمریکا و ایران را برای نخستین بار پس از ۴۷ سال پای میز مذاکره بنشانیم.
🔴
ما در هماهنگی با شرکا و متحدان خود این میانجی‌گری را به نتیجه رساندیم.
🔴
جنگ میان آمریکا و ایران فاجعه‌بار بود و تأثیرات منفی شدیدی بر اقتصاد (منطقه و جهان) داشته است.
🔴
سه تیم فنی در مذاکرات بین آمریکا و ایران مشارکت دارند.
🔴
کمیته‌های فنی در حال بحث دربارهٔ پرونده هسته‌ای، دارایی‌های مسدودشده ایران و موضوع لبنان هستند.
🔴
در طول دورهٔ ۶۰ روزه، هیچ گونه عوارض عبوری در تنگه هرمز اعمال نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/129531" target="_blank">📅 15:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129530">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
برگزاری نشست سه جانبه ایران، امریکا و قطر با موضوع لبنان و اموال بلوکه شده
🔴
نشست سه جانبه ایران، امریکا و قطر با موضوع آتش بس فراگیر در لبنان و اموال بلوکه شده ایران هم اکنون در محل مذاکرات در حال برگزاری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/129530" target="_blank">📅 14:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129529">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار صداو سیما: یک دور رفت و برگشت پیام با واسطه پاکستان بین دو‌طرف انجام شده یک دیدار هم با هیئت قطری برگزار شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129529" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129528">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
اسرائیل کاتز، وزیر دفاع اسرائیل، اعلام کرد که ارتش اسرائیل (IDF) همچنان برای مقابله با تهدیدات در لبنان آزادی عمل کامل دارد؛ این اظهارات پس از پاسخ گسترده اسرائیل به آخرین حمله حزب‌الله مطرح شد.
🔴
او تأکید کرد که نیروهای اسرائیلی در منطقه امنیتی واقع در امتداد مرز باقی خواهند ماند و اسرائیل از جنوب لبنان عقب‌نشینی نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129528" target="_blank">📅 14:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129527">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBInMfR6k1-1n_UrEehJtTDjJNUfkUdow6ZjHsZE8EH2WP-qARJygd_skIYESpYnC8dDzaVhWvK5dNcv9YWG6hKXhiSMFiPSomso-FHY7Vyvak7xLCEMqivQgCEhfimNxscMt-YMZQkB40JGQdaG0b2uVf2tB-2HOBv8fTmgcXMaDk0_Xtbe9weHxgih_IuQEoRscxPqR3y9LSq4IiH1mP0zmkvlOBSOJVtRh-vkImiAm3adAZZsW98WDyJIfLgxCsTmJbzSKGrtPKQn3CrL-CCW1HQasvPpDl-swIbVDWNwscctDMAbZNfXKNCqm9d8nuMIMfwNtDODtJPXLnZVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی:ایران مصمم است روند اجرای تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129527" target="_blank">📅 14:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129526">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
پزشکیان: ادامه جنگ به نفع هیچ فرد یا گروهی نیست
رئیس جمهور:
🔴
ادامه جنگ به نفع هیچ فرد یا گروهی نیست. بر اساس همه تحقیقاتی که در جهان انجام شده است، هر جنگی موجب اختلال در رشد، توسعه اقتصادی و اجتماعی و افزایش فقر و بیکاری می‌شود.
🔴
این سخن به معنای ترس از جنگ نیست. ارتش، سپاه، نیروهای هوافضا و مردم ما نشان دادند که با قدرت در برابر تجاوز ایستادگی می‌کنند و اگر جنگ ادامه پیدا می‌کرد، با قدرت می‌ماندند و مقاومت می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129526" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129525">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrjnvKteWIN3RYTWBwInNWKjzUfK9mEJ2zRfH4F4J0ETIDMliGDXgCpACDx_mrl1403DY7ffKtmMJKkRCOG8XyrVx_-GwslkIeVwnehRoYmHoZv2FJUTy6oHbLNzjd2w4us7wiPOumD3Q6g793VBK6H6E99nII32L3RBRB1ux6fPReI3VgrPKOTtoAgHqZWOomgxgd61M2xge0O_-sTXpv89tgNWTYFXtPZsOaPHCdaNs8TTpbP0FgjiRmz9QfVbVXmFcprmx_7QsIGT0WBsEGwj53pSDnLx37YiiRr_V8kxyKraRhqFwh3OwJ5ieKU652S4oc3Yxt0BETSvKq-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام ایگنازیو کاسیس وزیر امور خارجه سوئیس پس از دیدار با عراقچی
🔴
جناب عراقچی به سوئیس خوش آمدید.
🔴
در نشست دریاچه لوسرن، ما چارچوبی برای گفت‌وگو و تبادل نظر فراهم می‌کنیم.
🔴
در شرایطی دشوار و پیچیده، رابطه مبتنی بر اعتماد میان سوئیس و ایران، که در مأموریت ما به عنوان حافظ منافع نیز بازتاب یافته است، همچنان در خدمت دیپلماسی و در راستای صلح و امنیت در خاورمیانه قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129525" target="_blank">📅 14:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129524">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان: در شورای‌عالی امنیت ملی تقریباً همه اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد
🔴
مقام معظم رهبری به دولت اختیار داده‌اند تا این مسیر را دنبال کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129524" target="_blank">📅 14:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129523">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4776c5951.mp4?token=cuLlRRlXyHUdJV3AYuhsBgJaJOWmRcZL4bRfEkjdAQ0vjlJX2bEfG0Abwx-wSHIrqzqBcq8PgUzGQTFJTtU_d9L-rdqAZJKAtGGRr75MThztxkLYRkXx4j2ai-FmOI9nB68yZR5udKyA0SE3n2lYK97laP8ocQgcnAI4OxAI2_Rxic5d9yw3w3FKSmQsI_B0iI5s9_UVnQrOU0sc2vs66l9E1Z2iFWJF66H_rG9uw8krESupAfTvK-t1Izx-msAm--C9w2uoJCE3oh52xqO4AZYYceUvaXuuSZWA6yEkJyfdMmOt3sCTGD7UW4nr5I7wCNfIlXChIVSc03x_sIQbIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4776c5951.mp4?token=cuLlRRlXyHUdJV3AYuhsBgJaJOWmRcZL4bRfEkjdAQ0vjlJX2bEfG0Abwx-wSHIrqzqBcq8PgUzGQTFJTtU_d9L-rdqAZJKAtGGRr75MThztxkLYRkXx4j2ai-FmOI9nB68yZR5udKyA0SE3n2lYK97laP8ocQgcnAI4OxAI2_Rxic5d9yw3w3FKSmQsI_B0iI5s9_UVnQrOU0sc2vs66l9E1Z2iFWJF66H_rG9uw8krESupAfTvK-t1Izx-msAm--C9w2uoJCE3oh52xqO4AZYYceUvaXuuSZWA6yEkJyfdMmOt3sCTGD7UW4nr5I7wCNfIlXChIVSc03x_sIQbIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار تیم مذاکره کننده آمریکا با شهباز شریف
🔴
تیم مذاکره کننده آمریکایی به ریاست ونس امروز در جریان مذاکرات چهارجانبه ایران و آمریکا با مشارکت کشورهای میانجی، با شهباز شریف، نخست وزیر پاکستان دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129523" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129522">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o590J0qTLJfN9oJDk5POoL-YW9dJXTtgQJ5NvQO3Z8xfCMETU98NcrhTaBvMh76Wxs7nd2lYKqH0skt01KFwmv67kO7xVNYpcIG7a2UzJf56FOL2DTAkBMKpo_p1LE-I3QFgFgUjvlYeyuREKX-djaoTzUYWetkB2sEwB-AekUqOGXnKkD1FQpTZvVY_pmtTW4rrlRlHXEROs1BJ6vDPw34jHMz_eOxGdtr8O0guwu77kZwgXRRgOiODyNBGN6iWjaH4ZHe9sr4yTrAsdI934sRggredMEQnb8R3h6eW8NfCGSwCzodKS9aFzzV0b8_p9AmtNXV7srsCZTVY61aFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیر کل آژانس بین‌المللی انرژی اتمی گروسی گفت که با وزیر امور خارجه سوئیس کاسیس در بویگن‌اشتوک دیدار کرد.
🔴
«در این لحظه حساس، مهم است که به دیپلماسی هر فرصتی برای موفقیت داده شود.»
🔴
گروسی همچنین از حمایت طولانی‌مدت سوئیس از آژانس بین‌المللی انرژی اتمی و تعهد آن به دیپلماسی تشکر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129522" target="_blank">📅 13:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129521">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پزشکیان: دوران محاصره دریایی یک بشکه نفت هم صادر نکردیم البته طی دو روز گذشته ۱۶ میلیون بشکه نفت صادر کرده ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129521" target="_blank">📅 13:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129520">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129520" target="_blank">📅 13:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129519">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68daaf45ba.mp4?token=oshJPjd0OPh6mK1QFQ1_szVPXkLMtUN9CmwH2DtgHD5juk3ZsfFqtQvek8B7BR9szSaQjv6bYdKxah2Ukuz0v3a7RFPsExH5p1KEJqWyBIntcXTTTpivjLob4FdL4ocvLmjyuDipnFUt8W4QzMWxJLr8RxBVJCUuwmTRtislh8mFsGHhTJrq9peSC2oQ8AINgBj7m-nu3U6xFYIOo-Ws1CDekEcJwCFMl17nYM8TiSqq7fX5CWDlMP_mSqza3DRhPpnBvCHsjgyYh0PpVW34YcJHb3RfdnEOQ1rMPoknsZ3ES_jI66pYYZ6X4Gshl9g_aqdK9SzVhJrHiqkE6ZZ7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68daaf45ba.mp4?token=oshJPjd0OPh6mK1QFQ1_szVPXkLMtUN9CmwH2DtgHD5juk3ZsfFqtQvek8B7BR9szSaQjv6bYdKxah2Ukuz0v3a7RFPsExH5p1KEJqWyBIntcXTTTpivjLob4FdL4ocvLmjyuDipnFUt8W4QzMWxJLr8RxBVJCUuwmTRtislh8mFsGHhTJrq9peSC2oQ8AINgBj7m-nu3U6xFYIOo-Ws1CDekEcJwCFMl17nYM8TiSqq7fX5CWDlMP_mSqza3DRhPpnBvCHsjgyYh0PpVW34YcJHb3RfdnEOQ1rMPoknsZ3ES_jI66pYYZ6X4Gshl9g_aqdK9SzVhJrHiqkE6ZZ7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف، معاون پزشکیان : دنبال جنگ نیستیم
🔴
ولی اگه کسی بخواد شاخ بشه و جنگ رو تحمیل کنه، جوابش رو جوری می‌دیم که یادش نره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129519" target="_blank">📅 13:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129518">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZe-4TiOQ2e-TxMsUWMiIGqD6EVfabbBmLti_IDgJGsojgG_hjqMq5g8f6_zQN_ANCwC7eTuupoiWQ4NeWxgFikQ9j-uO-HLLRapFxVo5LC-jjK9noXsSiseUqY4M6conSTg3YDtPExXl7xKSMeDC-qXynovMPUVQP6NlGLzkkgOJsfDzf4Rj6ZTWwtXnQ2QObyxc1M-bpSmOyXmpiI7cWXEPmJHUHzfM5zvTfzftJ--qwOqGVL90cIB_43Oj9xTSjStNHbGYQgM1T8ZMRYcldcCUbFX6u2W360ubvYGLuwT3jpqLTpGjhNBE7lwMU4yxCpU8syV-T25Ui9QrnYPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با وجود اعلام توقف گران‌فروشی اپراتورها در طرح اینترنت پرو، ایرانسل همچنان هر گیگ اینترنت پرو را با قیمت ۴۰ هزار تومان عرضه می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129518" target="_blank">📅 12:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129517">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kiq3d45H-g9kBbEGOf8SgDmqMgIYX0Mte5kZdA6XdmU5XJTIwsntf9c68v4GUE13VF_9WyRRVcqkouQEPJORptCP2XpBYH51p4xao0Ar1zSVDQppMnwjBCqljJ4vAuqYp_zzIg92-AjEBFJawINyLo7KugnVsi4vki398DPU43fA4SZrgHKP1417uA-A2amv07IeYm1ZflR9vTXEhe4PEkkcTuQyGReyapc3bJOcSa29obRZImIjbdYcSJCcPksXmaecfaQIVJrF4llgJee6fnUitHJeKSuNKhNY7nmUZHERuGyZzVxgJkKh2Z8NuZJnLmSYTt6XKV8CdlUcbG_h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار رسمی اعلام شده از وضعیت پتروشیمی‌های کشور که پس از حمله اسرائیل شاهد حدودا ۸۷ درصد کاهش تولید نسبت به سال گذشته بوده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129517" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129516">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSn88XApNGJ4uxiocdBok4w8-Hx_T--EnBa5OXE1QRQaZt54aqQxt95a8NVYpuJDtUYnfEgQiHBDki1Z71a434_Iyauu9AMiIJkW6Tpx9MIdD6WpnqNFbcWQBwET-NoYBRzSovJ8OflbgTRerx2bXpn5rOdD-44UhXnfJT-NVM8JD0DjuijToiRMQCdz1E4VfYsJoMITRYIzZRHNYlPW968BQgdrodAzQ78NBoyI0AKx1nStZI1wMRGhJmS3jAwFLeXf6BF55ymRboPNInjJ0DABA4NQYqN2R1lmfkMR2TrCU1syj--PnZEW91MVIrwVUwzPfJeCsLHe6P4qKgWC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : قراره ۶ میلیارد دلار از پول‌های بلوکه‌ شده ایران برگرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/129516" target="_blank">📅 12:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056df7a897.mov?token=R6R25U-UBqnkBKOJtAiQTaVYtHEypAfZkTO_54xRfkslRXsZuzvFfIT7J0vMXwQB2DSCo9iNFwcw2_aHeJmLFkqajC7SacKis3W_PehtUzeimV3dUsHBiLjNM1NYIH5TshQMPATFARQXOec8GadiH1M0OZy0O_6xUKiZ3ejdNSxAgSR47DsAAiJnRYBSNg3V9wJ9fWFEXCWK_1quRkJh0HbH2k9tNSSJWucydEFwKFVPyU4HK6rC01VhFEW6pJxn7wPB82RfC4qZs7XAViTNcbw9onh82_CeZT0hLnpSzfKByDNsqQ2TCyR8USuhtwB3nY3j7FC5JlOXLtTEi1SOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056df7a897.mov?token=R6R25U-UBqnkBKOJtAiQTaVYtHEypAfZkTO_54xRfkslRXsZuzvFfIT7J0vMXwQB2DSCo9iNFwcw2_aHeJmLFkqajC7SacKis3W_PehtUzeimV3dUsHBiLjNM1NYIH5TshQMPATFARQXOec8GadiH1M0OZy0O_6xUKiZ3ejdNSxAgSR47DsAAiJnRYBSNg3V9wJ9fWFEXCWK_1quRkJh0HbH2k9tNSSJWucydEFwKFVPyU4HK6rC01VhFEW6pJxn7wPB82RfC4qZs7XAViTNcbw9onh82_CeZT0hLnpSzfKByDNsqQ2TCyR8USuhtwB3nY3j7FC5JlOXLtTEi1SOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیات جمهوری اسلامی عازم ساختمان محل مذاکرات شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/129515" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129514">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9S3zJ5qGoN2mLBo0bLBBzZYwa_INHg4dPzjLkzSNXczPHtJmDL-ciZGcCCChcN6m8ej8Qf1okmdkGvVAN_u4ZGeKm3Ed3bXCZ6Z-WwSqOFvHb-4Fa8x7Ue3HDsNfYpjz8dIShyd-cQ7Cu9kDjOWe6cIUL6nyZd8Tv_3RmKxIH2maXnNjxDjILcYDqnCwg6hXFShV-xEWEt-qgUNMAqJmENxanTaiWnU5-4B3zD7maVo3diD6NsBRSoOdTRRxDtp_zCVdHLVV6zM546nQKJ653zMtNai6bFPvmxBpfmL3zwI5dbrpcRxIzDzO8SG5wIE4V7J_UMowDyMckrFPyQ3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمایی از محل مذاکرات در بورگن‌اشتوک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/129514" target="_blank">📅 12:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129513">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
هیات جمهوری اسلامی ایران عازم ساختمان محل مذاکرات شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/129513" target="_blank">📅 12:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129512">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
برای اطمینان از اجرای یادداشت تفاهم به صورت مستمر از طریق میانجی‌ها تبادل پیام می‌کنیم
🔴
در جلسه بعد از ظهر، هیئت‌های نمایندگان هر ۴ کشور در یک اتاق حضور خواهند داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/129512" target="_blank">📅 11:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129511">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران: قرار است یک جلسه یک روزه داشته باشیم
🔴
برنامه‌ریزی به این صورت است که صبح دیدار دوجانبه با هیئت ‌های قطری و پاکستانی به عنوان میانجی‌های این روند خواهیم داشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/129511" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129510">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فارس به نقل از یک منبع نظامی: تنگۀ هرمز همچنان بسته است و نیروی دریایی سپاه نیز تا اطلاع ثانوی هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/129510" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129509">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
قرار است یک جلسه یک روزه داشته باشیم
🔴
برنامه‌ریزی به این صورت است که صبح دیدار دوجانبه با هیئت ‌های قطری و پاکستانی به عنوان میانجی‌های این روند خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/129509" target="_blank">📅 11:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129508">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اسکای نیوز عربی : پیش از شروع مذاکرات ایران وآمریکا، جلسه‌ای بین هیئت‌های ایرانی و سوئیسی در اقامتگاه بورگن‌اشتوک سوئیس برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/129508" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129507">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
حمله بن‌گویر به ترامپ: باید بدانیم چگونه به رئیس‌جمهور بگوییم «نه»؛ توقف آتش‌بس یک اشتباه بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/129507" target="_blank">📅 11:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129506">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد.
🔴
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔴
۶ میلیارد دلار پول ما در قطر برخواهد گشت
🔴
نتانیاهو اولین ناراضی از مذاکرات است.
🔴
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم.
🔴
این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/129506" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129505">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عراقچی و وزیر خارجه سوئیس در بورگن‌اشتوک دیدار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/129505" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129504">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
پزشکیان: به‌زودی مبلغ کالابرگ را افزایش میدهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129504" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129503">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک منبع مطلع به ای ۲۴ نیوز:  یکی از اولین خواسته‌های آمریکایی‌ها در مسئله هسته‌ای - اجازه دادن به بازرسان آژانس بین‌المللی انرژی اتمی برای بازدید از سایت‌های هسته‌ای در ایران به منظور بررسی وضعیت به‌روز شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129503" target="_blank">📅 11:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129502">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر نفت: پس از توافق، کشور بزرگ‌ترین سکوی سرمایه‌گذاری خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129502" target="_blank">📅 11:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129501">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تنگه هرمز هنوز به صلح نرسیده است؛ با وجود اعلام صلح، بیش از ۵۰۰ کشتی همچنان در دو سوی تنگه هرمز در انتظارند و بازگشت به شرایط عادی زمان‌بر خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129501" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129500">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سی‌ان‌ان‌: در جنگ علیه ایران، قدرت نظامی آمریکا آن‌گونه که واشنگتن تصور می‌کرد، قاطع و تعیین کننده ظاهر نشد
🔴
در چین برخی صراحتاً گفته‌اند که پکن از این جنگ سود برده
🔴
این درگیری بر برداشت جهانی از چین، تأثیر گذاشته
🔴
جنگ مذکور قدرت بازدارندگی کلی آمریکا در موضوع تایوان را به طور قابل توجهی کاهش داده
🔴
بسیاری معتقد هستند که پکن در بهار امسال، تهران را به سمت مذاکرات با واشنگتن سوق داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129500" target="_blank">📅 11:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129499">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / المیادین نخستین نشست رسمی در سوئیس ساعت ۱۶ به وقت تهران برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129499" target="_blank">📅 10:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1EuP3nqA2bZEpZMgjoQfquMO1d-wxnFNqKFZWHM9eb6tGelJAuR2XKNrwIBW3-BEgZVl_amx2_GMhsej6_mZ4AYwzWfYrgIcMkJv7KTt75tdDnZhI0dGfm9KnyZ486Y7l2IfUooGx-APk-TEV_nogUHbOilcpElt6IzIOvUGs6itOOQbHLzGyZ2aTieTVCEuogAe3XvQBPSMHeMNnkLhXVAweRUWZg1RpymcQxafZ0YHDYMXiLO7_vOni_9sgU6vbxxb6sU-SMwefemVqjGVJLn7Hn88cvB9I5tbRAakjOZtGFElYeu9imL2PPcVlVMJt7tll7ww7EGz7u1rxQ4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHqbxv99Kgst0z_NDRO75nzMj8RScq3ACh8sK9Ja9EWmUo7aW-41Yn7_vA7LcfasaO3UagkwYCBt5rquUwJGAXEOUQKELLfc3hh8WQGe3Ucx7gEmSPyB2N73eLaPyKVLfl1jfA-USDPNdAfyRtZpxwPNcdRyxNXuhPopluNjH4yXstK9Lo8a0fCjyvJ37VIT7jOBw74uHkOVhgCzIpyYT9p7UCpbKMWC1UWJIpvR-Ss3t8mVcMEecUpDSNvJh-QhHsgYr8z1ZpvOX7JasIZ2hsw8roD7pHlsKGm-xkiBydx6yc3xK6fDoDqvj3TO1FqD5JW2jTqwcsx_btlzlQBI9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پرادو ۲۰۲۵ در امارات ۵۰ هزار دلاره در ایران ۴۳ میلیارد تومان ، حتی اگر دلار رو ۱۸۰ هزار تومان درنظر بگیریم و ضرب در ۴ بکنیم هم به قیمت ۳۸ الی ۴۳ میلیاردی این خودرو در ایران نمیرسیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129497" target="_blank">📅 10:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6knQXqsG7tV8jVjMiyHDRs2PI_C0eO9lhE1MfCxrTflUbkKipH10DcQsdeB9G-PGdnXjAEYQLiiTSSZJ_sFJMORAuUWPE34j59qe6_WwWkye4yJtxihUw53hCHLd_QDgpNxjpvFmJr9rCJg7m_LqeJmIxW5VpzhY8BhCoUfG7cSJFMrFt3Oleg2Q9WaF0njDo6KKTHuTGCBAWSIHKwXh_F7kdJmVIIJ1Y0Weoexokj9N0Prt_dUIP4W-9lo2OhruXLypX0Dzy7bdGrgZrG9BoskeKTGRVYDpW5b02WpmOQVeUYKbc0W3AVgJJuqnitgh1GVBmeMk9A3LtxfIYjKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrxjDcBIWg_oq54VEmT9qNVlWDw49NyH6kdL2mjH20_dO346COTywOWzPgTuZklSeUaB7TBJjyABPWRGluRexDsRo8bOVWZvSPbsgyr9bBxQwbaPdWHfCyqKxYvRbDGYdOe2wDczhiRUkN-v7sa-IssGB_ELqHenEQ1OEBHdbvGGsS0MBDAHaPcYK_AKiq28Og6Oy8XHdp_zQUJ85RSxBWPzQcN4XqMlfUXtxmZMgPc28ITo_XZm6gy5MRVk8lURu9p3GwdrKRf0d4WwGIm_2y2B4gPLxeWT_w73UT9BocPNtZktRkFd4769xCCJT3iDkCPxcGg-AgDEIMfef-fljg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از ورود هیأت ایرانی به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129495" target="_blank">📅 10:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در دزفول
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129494" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: شاید اگر توافق با ایران حاصل نشود، برای عبور از تنگه هرمز تعرفه وضع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129493" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw4e8aOt4y63Ol5cYdd2JM5wGsOou8hyn0mFEZd01yJF68zMWH6dBT6BoekIK5QTz2lH4bVWBkJLRGA6x0jMyuQ7W5ueteyIMK1B2jhGVMrf0iUabgP-WzTe_bkBXWoIvywlrIrmDSRFb3hMPAgkL6Y_kAplPzOWlUaZ2LjQKU8f9VE6PYKk34LWE5jpGATyDTX8ZL_mFxQTlsX2q0CdjLDySfxe-5y1SKtfg0QOYA96rik4N3i-SAIkOqAdp2iwP8NkuhzAD9e8stQjoTsLhVtOjb4wYYkT0omcy1BEasvVAGl4RN1e6CaDX_FhwiDxapSqK1WuU752qtL7cfh2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: هرگونه خوش‌بینی مورد سوء‌استفادهٔ دشمن قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129492" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
الجزیره: شکاف در روابط ترامپ و نتانیاهو به اوج خود رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129491" target="_blank">📅 10:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
خبرنگار الجزیره در نزدیکی اقامتگاه بورگن‌‌اشتوک سوئیس : ظهر امروز به وقت محلی قرار‌است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129490" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سی‌بی‌اس به نقل از یک دیپلمات شرکت کننده در مذاکرات سوئیس: ادغام پرونده آتش‌بس لبنان در مذاکره با ایران، یک تحول راهبردی برای دولت ترامپ به شمار می‌رود
🔴
دولت آمریکا از راهبرد جدا نگه داشتن منازعات مختلف در خاورمیانه، دست کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129489" target="_blank">📅 10:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Y7_AD99Xqg5AWTwFwd2J5mo7MKvaMCtXNq1d9CQpJAZh0yIMBM7Wr7iwadhmVumadewmVwi1hdvlPoN2OiCygOj5k5NOf_jYg8oUQPqIXfTvJ0sjDAsE0gubCYfZEdfixAMv2aoz_C4ki-uU8pyi9F43x7IlP3YlrTmJXeAfc2IvIKvPQaxtcqq-_cb8plvjV054MG_z7S4BcDcQ0gF4AP2plLvLtTJjudRFTrO51vY0Y17JAh0h-4SDAdt04RJsuh0t8YlstQG0mcLAG088cxLkKPuyRK1lqMw5l7YJy4XnnTSiVfhRPAR926c_aT8apQXWPH3BJXHY3hhTaO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترمینال سوخت کرچ که توسط روسیه اشغال شده بود، صبح امروز با حملات پهپادی اوکراین منهدم شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129488" target="_blank">📅 10:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/129487" target="_blank">📅 09:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129486" target="_blank">📅 09:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع دیپلماتیک: پرونده لبنان نخستین موضوع در نشست اضطراری خواهد بود که به مذاکرات سوئیس افزوده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129485" target="_blank">📅 09:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193ac2578c.mp4?token=Owld_K1ZeG4v3qbD5np5LHDlHi8GmauVwy7ivRDMlw_rWMtPLg3JcbrVRE5ixbnB8cLfxn1Tn5xlQdx05NU6BFaEncd5eLtW4TeJQbh-eKYP9xGNh4YZ6ugdPU8c6MzAIjV6CEUltTI1bKVwpgpI0_aj0v36zqLqZP0aS9PC1qGv_7gPVP-otBPoo16ZKKR2oicSnAw2h2XiuVnfZJfg4d5zc3x0jTtA97e0iOhmFTfyFYnqHYWdiP1oHylTRysjE2uY1rGRpV7lTzoEmbball-6C5OtsQFsSspDfAj4BUcU2hWFpA389HpdZdYkJ8n5gvM9uYWLPRs74MS3v6C8tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193ac2578c.mp4?token=Owld_K1ZeG4v3qbD5np5LHDlHi8GmauVwy7ivRDMlw_rWMtPLg3JcbrVRE5ixbnB8cLfxn1Tn5xlQdx05NU6BFaEncd5eLtW4TeJQbh-eKYP9xGNh4YZ6ugdPU8c6MzAIjV6CEUltTI1bKVwpgpI0_aj0v36zqLqZP0aS9PC1qGv_7gPVP-otBPoo16ZKKR2oicSnAw2h2XiuVnfZJfg4d5zc3x0jTtA97e0iOhmFTfyFYnqHYWdiP1oHylTRysjE2uY1rGRpV7lTzoEmbball-6C5OtsQFsSspDfAj4BUcU2hWFpA389HpdZdYkJ8n5gvM9uYWLPRs74MS3v6C8tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به مداحی که می‌خواست با تیغ، حلقومش رو ببُره:
🔴
خو فحش بدن؛ هر چی بیشتر بدن، خدا از گناه‌های من بیشتر کم می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129484" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
به گزارش روزنامه بریتانیایی "آبزرور"، نخست‌وزیر بریتانیا، کی‌یر استارمر، انتظار می‌رود دوشنبه آینده از سمت خود استعفا دهد و قصد کناره‌گیری دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/129483" target="_blank">📅 09:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o0PT_2kU5awM62vadW-x8m51hhu_tfCdLD5oi2ae6K6PHBMxSN9QRZ6kv5Pi9NgTvlOh2_cu85l8tJRU2_FiG5cta4RNbVCcq0THdYz7NCH-MNj0Rn0phU5svh8lEa2PVmyEm1SrKKK3HhkcsLzUpLgY8SM3gAtVky1oF_AYnmiaXmUBLze-RIPKqDQChSH_AgkXi1IGDw4i0-gkrgujVt25HM_LP1LxNbl31Tiwi34_91TQjED0uHadGHiX2F1GYT0G6jcX1hCrISo3w9G9uSFsBSbt0qOh8Vf9421HBdSgah6ddHMPouQ8eOuuHvtRQXTtDuqjx2v2aZCHwpN7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیر قلعه‌نویی با انتشار این تصویر به شایعات درمورد ساعتش خاتمه داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129482" target="_blank">📅 09:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: آمریکا پیشنهاد داد، ایران تنها برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/129481" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک دیپلمات:
یک نشست اضطراری درباره لبنان به مذاکرات ایران و آمریکا در سوئیس اضافه شده؛ این موضوع نخستین دستور کاری است که مورد بررسی قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129480" target="_blank">📅 09:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJabPvb1pFkiWwqyp0KF0cfFVTbhBmwCSGoPirIxi5K70ymtml0DbffUw7yqtz7e8Mm1QkRXFLIpSZaYYOLoy0FjMuNVZUgSWyhqoVrS8-KGRyKF8lPBAQFKFborpLzBL1Vlv-yo2CUHCv51FycRlP9t56SJTNxr1L1-tOn0KfAJbckbRMWs36uu9xDnVhgawrnvrbgXqVXyeptVeRS46RXqb0cPG0BrqviXR5HdZ-UhfyqY1j6vydmWnxzRroVzF03QYbXsM95Uj-Wbvt2iaBic9bNpqxtUQXa9sB-zWrq1_AsCoOuixTMxLpabeG10TaKagO14SdTkbUTDgqjBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/129479" target="_blank">📅 08:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رادیوی اسرائیل: کشته شدن ۶ سرباز از جمله یک افسر ارشد و مجروح شدن بیش از ۲۰ نفر در حملات حزب الله در لبنان از پنجشنبه گذشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129478" target="_blank">📅 08:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
خبرنگار الحدث: ونس، معاون رئیس‌جمهور آمریکا برای شرکت در مذاکرات با ایران وارد سوئیس شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/129477" target="_blank">📅 08:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I93FA1-IW-RrWQWA2luuBnnM633xHp-H3EnoQaN5aazk0WFLg7i-8p9_1ICOUe9yGcpoTvZHZCmmz4c71H7dJukJO1fBDCXu5tOO1IRzhjsxtQhzHDAGRi1_6S94QYATDX3j3W4esiQSwy3ZdJt1oGiQdgU69_nm_Y0m-82D9fbECL-3WBBzAAeiehVBUkAfEQpZiDl52XMLvzMnSaAPgUw4RdF9SsJfrdRNS03LiDlysw3zeLQdEPDWkpH9bpQ7b5DLAeV-jEBZMpoZ9SLT5YZM7UEdOfkznCXZcJtbggNLg6Tix7f8xHHl8vbTxU-YUs775x6yMQe4umLvEbHDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز شنبه، با انتشار تصویری اعلام کرد که یک جنگنده پنهان‌کار F-35 نیروی هوایی آمریکا بر فراز خاورمیانه توسط یک تانکر سوخت‌رسان «کی‌سی-۱۳۵ استراتوتانکر» (KC-135 Stratotanker) سوخت‌گیری کرده است. سنتکام تاکید کرد که نیروهای آمریکایی به گشت‌زنی‌های مداوم خود در آسمان منطقه ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/129476" target="_blank">📅 08:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd6e8762e.mp4?token=N4CNkdQegReNyXo8SyiQlVwZSD2zVAZjMkIWuZZNEJcE3ju0hw4gkpDnRy3-O1wj2R0SXJsG8zhRR9l55-wJNMx5CzYnQE1gmoB3qn2jY9fY-4mQpLuKF9g-fXMOxVZWTjcw-zVrHOy9nIvmVabYykq_KoinssHhKAZbcwqLtpL7njo6qlTXdmXMK0lhAxoMnduvlJo3iyQJ2crO8hU03iJ1NPB83D-CSjvf88-AKli1AyiDrEq0YbEOaB3oRpevAzwkRDgU3O4Jb5awZCZEh9a8-LOMhuKXBikio7WDLge8Lg4SgK94pZQ8c9TfzTWyqV1WQqbYGtxLc555hS-C4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd6e8762e.mp4?token=N4CNkdQegReNyXo8SyiQlVwZSD2zVAZjMkIWuZZNEJcE3ju0hw4gkpDnRy3-O1wj2R0SXJsG8zhRR9l55-wJNMx5CzYnQE1gmoB3qn2jY9fY-4mQpLuKF9g-fXMOxVZWTjcw-zVrHOy9nIvmVabYykq_KoinssHhKAZbcwqLtpL7njo6qlTXdmXMK0lhAxoMnduvlJo3iyQJ2crO8hU03iJ1NPB83D-CSjvf88-AKli1AyiDrEq0YbEOaB3oRpevAzwkRDgU3O4Jb5awZCZEh9a8-LOMhuKXBikio7WDLge8Lg4SgK94pZQ8c9TfzTWyqV1WQqbYGtxLc555hS-C4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چند ساعت پیش عباس خوش قدم (سید عباس عراقچی) رسید زوریخِ سوئیس، الانم این شهر طوفان شدیدی شده و کلی درخت افتاده روی مردم و مصدوم زیاد داشته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/129475" target="_blank">📅 02:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23c2d0b89.mp4?token=TBsslZLbfmF1wbOXyeaJYozvH_EYgN1P0xDfV2tq1CLqiXR_l4YqLjq-mshVesDTV7Iw_mKTirHVoODxCBxwmxAtF3841ZYjELSRJb3wFKS_StC0W_z26kYS8ldP9NCMyziGOvWZCIsXE_FiuNrpjarCnSRSLaX7m-RSNTxvvujSzvX_3vL2MYGjOJ9nfn6Wzf4CkJTLSeQhqZc3JCuCckbyrp3a4jvtCD8yWboilml6WFMed6hdFM38YVf3PIGv8NN0E5264P15IfdQayn7NLhu0XFx-7ptoRajO1jjEks2FHiMiwCyF24_XzDJcGyawiuoH3pBGJNPlT9QNdE3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23c2d0b89.mp4?token=TBsslZLbfmF1wbOXyeaJYozvH_EYgN1P0xDfV2tq1CLqiXR_l4YqLjq-mshVesDTV7Iw_mKTirHVoODxCBxwmxAtF3841ZYjELSRJb3wFKS_StC0W_z26kYS8ldP9NCMyziGOvWZCIsXE_FiuNrpjarCnSRSLaX7m-RSNTxvvujSzvX_3vL2MYGjOJ9nfn6Wzf4CkJTLSeQhqZc3JCuCckbyrp3a4jvtCD8yWboilml6WFMed6hdFM38YVf3PIGv8NN0E5264P15IfdQayn7NLhu0XFx-7ptoRajO1jjEks2FHiMiwCyF24_XzDJcGyawiuoH3pBGJNPlT9QNdE3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری تیلیوزیون: باید فرودگاه مهرآباد رو ببندیم تا هی نرن مذاکره کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/129474" target="_blank">📅 01:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مراد ویسی: نباید به ترامپ دل میبستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/129473" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qI7rzzWeN7abjxu9EOVhXDakr26DZtjsZCiupAobag8uezbheJwpNjNE-WoIqZf-ATNoSs-3Jc39rbW7NLWAzUwf_I_T-1V4CIaisiqBzJH_1gF7tP5WVavdY3VQYoZbX76k_A6_MFsHYsnjGMyd2qLc7Qk_G8FKbPU6xsNbSPCX-nvBCX3GcYZrSO1_mFqXX14KaKj7QST11NwMKRKANQQUneY8PK1QBvlyjWS2rIw8LaW54xUC-cojZ5utNwW7RMMhfaU0vXryQUiN9fxOhEidFTqaSkfLVcqXLxORmb7h3QmqXQYnyJguCSfpJNmqTEfKYWv5CSrqW3rRUgKa0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHQUeEqnuR8GtjlwUUkw7yEPcN_asuqID-BJVpbf4lZ3aTDhdzCXz5_4y2ReM3tg08Vz5aSNuKgUQVnfcYDox345oWWYjJ5mHZgvcb9-Osw7Q68BO4d-cJPOjr6p7fe1nef0Hc27pzgnUro1Vxbh7yVikqLYxARYn-9eHOXDpa7tUHZRI4BgNsp5H0aTJWTcGrBb4W1pqmRcag2uCMWEQDzzXsnX1bca1NnlPNsZ-GosYwTbKhUgOu5UWeyTZe4GrhOmqYpNiSSbKVnlqn9lLsMdG_dnYnHXP20DdyvMJS3p0grZxybeQ9F9Aryx4q4GgVGj2EfaYspWwNIsKHJMeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی با پرچم استقلال تو استادیوم داره بازی آلمان - ساحل عاج رو نگاه میکنه!
@AloSport</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/129471" target="_blank">📅 01:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8f4b679b.mp4?token=eRP9duuBuAPCuF_-72MArxqKTt5-BYNMrIbzA7RfF4CemyANyiodxrned5jkvbktu3GvURhR7B9UoNUz0kkL-_M6RgQrTsLAGMoJJWWX2vIH5Puh8QzW5TATMypoLGKorPnSAmJO6EcCXkt_mpZ-RB6ocTHjPnkTTN-Y_9CSnBC5EMfwKEQYduRPg-rDKBLt8c9mX8epJXq7mtk4qEpV7MWJZFnHbm1Gi8M-XGzsjcz8YLFy50-uYwotEkrS-a4wYGfaC-eNmdav1pHlT74Q1WRAbmp3EmzrYhRJWIgGxz1lPMU4cv3BbDEKf_v8z0jaS9DspO73F2IUEjbEM2sdvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8f4b679b.mp4?token=eRP9duuBuAPCuF_-72MArxqKTt5-BYNMrIbzA7RfF4CemyANyiodxrned5jkvbktu3GvURhR7B9UoNUz0kkL-_M6RgQrTsLAGMoJJWWX2vIH5Puh8QzW5TATMypoLGKorPnSAmJO6EcCXkt_mpZ-RB6ocTHjPnkTTN-Y_9CSnBC5EMfwKEQYduRPg-rDKBLt8c9mX8epJXq7mtk4qEpV7MWJZFnHbm1Gi8M-XGzsjcz8YLFy50-uYwotEkrS-a4wYGfaC-eNmdav1pHlT74Q1WRAbmp3EmzrYhRJWIgGxz1lPMU4cv3BbDEKf_v8z0jaS9DspO73F2IUEjbEM2sdvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشخوری عجیب ایرانخودرو
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/129470" target="_blank">📅 01:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPNsUL6ToRmDOXWLcMPMkim1edqmObdrJSg9YHAHJ35yKQh1vIa1GWUqb9F9p7KgIyEJ6F2w-yCSPMgmzW6Le18OMTlrwPQvLRkAHD98sKx9jPfXxFppJbvSgaN0Kgf4xQShwvhWQ33shVe10bc-0bnPUYInJWkvDm_04vgfunTmfrJ6mPLlq3DkEhEZQfjQgNDIsxiABt6Zzqf6ERTiFSScxypDWBVREEIxN5v7DYeKFtVEzl9PAS3IAlcwaxFu6VwXDXsjDrCYUuFt4titKqqCq8B96LSL5nsP-gJdNST8-E8ovOuf_ZVn7y7OyhR-VBz99PJKOQuor6FtuBMYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : آقای نبویان اشتباهی نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/129469" target="_blank">📅 00:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
علی زینی‌وند ، سخنگوی وزارت کشور :
به همه کسایی که توی مراسم تشییع و تدفین علی خامنه‌ای شرکت کنن بیمه رایگان تعلق میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/129468" target="_blank">📅 00:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8FCW9PBeFNbcCaCaAujekZrabwS1rKA1GOYlf2F6TkhuvXrQhKl68O2dIxZeqhjNgDloCGVq0W8Ll3a1xO5PIusGb8DXlnZSRaZQYV0zlKvo-bQT3RIXud7JJ5Dd4n53Tlzq6KV_9VnVvvhrSMcmKQqzGIEQQa_zdQ9LIZ5VZqSRjr2hgW9F87wXHyiZYfBbH_ItTy09r3l0GN9wJ1a-AvWE9X8-GryfDW4zWktaZM_JVzKo4MUQV2IrGCAyraBH84oTT9AJDL8CKorSL5CymX2YNF3xZURxQDwHSSjDekLDJlWr0USefUIws8ICMs5nyZ3CsVx4EUvzpJnA0rFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف بعد ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/129467" target="_blank">📅 00:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQp4Xg1V_Ef37IODDxVxqHpjGh6ucOmrJ5dvJTvBp2O3Ii2xOK3bB-4h3EpwS9QEZxsES9YeSGqTAv-WXIS7gBfkjdmUw1J4z1D5_MjxSgYSMkLzGoa1jEYO5FCc3R_KQOR6qYlvYLLfz6APlRyoPDBRvqlQsLeR2uk6atpNwseZY22PK2-C87dEWkxe_CWFS86r0WpJdPpFzTFbPXakeDAhQ7gMX3H5sJn_IjN7u_WgrfDRyqqkaoSIQdoYc-_qrKyEV15przMTV7e-vHJwaR8yOnQEX49L3Jjem1irXc8gZ4SYGMj5IKFyQtBgJtcq-Ec65HqWji7DnoOFEo4ILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط ساعت رولکس امیر نیوکاسل در مکزیک دزدیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/129466" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68aa7787ac.mp4?token=pJHaBj2fQw8qCHKM6A_oo-a15aPhza-DsfvWIMTgAxsx4q9QpJiyvdurDJlua9fk-_tBI1w4QFMFEIv2W-VO_J0ZFuub-zoWXJle7THjnG4Cnq_KwjzOxP26Suuvmm2ieM6YhmtWVzTY4cwSJKxdqp8uW5BLpC2-xjc2hRr4HwMDJqPxGjuR0d8D39ynhlY0TDyaZs6q1s4Ds3O9tXqRIsTOT-grN2jaMuN2SV8G9a3Qmc4IVY2wnxBQnI5-ptoToHtzJ2g5ZucQOhPVvmy3qq4kSlis4xb7OkWRMPG7PdPe2zYTLiEF0DUHPeeHZRJYxUAxGvSjTYoz-iEopbKwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68aa7787ac.mp4?token=pJHaBj2fQw8qCHKM6A_oo-a15aPhza-DsfvWIMTgAxsx4q9QpJiyvdurDJlua9fk-_tBI1w4QFMFEIv2W-VO_J0ZFuub-zoWXJle7THjnG4Cnq_KwjzOxP26Suuvmm2ieM6YhmtWVzTY4cwSJKxdqp8uW5BLpC2-xjc2hRr4HwMDJqPxGjuR0d8D39ynhlY0TDyaZs6q1s4Ds3O9tXqRIsTOT-grN2jaMuN2SV8G9a3Qmc4IVY2wnxBQnI5-ptoToHtzJ2g5ZucQOhPVvmy3qq4kSlis4xb7OkWRMPG7PdPe2zYTLiEF0DUHPeeHZRJYxUAxGvSjTYoz-iEopbKwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس :
«من مشتاقانه منتظر شروع مذاکرات فنی با ایرانی‌ها، پاکستانی‌ها و قطری‌ها هستم...»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/129465" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f204fb86d.mp4?token=E_tMpAI4qTtVfKhdKMzG433792yIKNvQSRfMrmrg1D5KwXzprDOQHJKHSI2PZdE69oFxJJuXU8KHW4HvqVx0FbxOF5EMpGqlgYUmhMFqBMxT1oytmirJqqRQ3UyCLml8dKIPmbCMe99zBH5UIXs5Fi0DJ3lX4GjtUOQI7sVIlrFm-P7PZKa4G4KqSCdkKV7Ja1AXzGTDp_nbEvAcmmJLcbsIkalhXyzWrbbqBSeqV6aw7lnIHHgf0You5smER4JgoyQWF5bQTkTgpNf7pQcipzuyqfI712APL7JQyiq60KL8ui3tXNpbwnp-0SbOY7dcBRyA1isflOKKRR6PCY3t-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f204fb86d.mp4?token=E_tMpAI4qTtVfKhdKMzG433792yIKNvQSRfMrmrg1D5KwXzprDOQHJKHSI2PZdE69oFxJJuXU8KHW4HvqVx0FbxOF5EMpGqlgYUmhMFqBMxT1oytmirJqqRQ3UyCLml8dKIPmbCMe99zBH5UIXs5Fi0DJ3lX4GjtUOQI7sVIlrFm-P7PZKa4G4KqSCdkKV7Ja1AXzGTDp_nbEvAcmmJLcbsIkalhXyzWrbbqBSeqV6aw7lnIHHgf0You5smER4JgoyQWF5bQTkTgpNf7pQcipzuyqfI712APL7JQyiq60KL8ui3tXNpbwnp-0SbOY7dcBRyA1isflOKKRR6PCY3t-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از راهی شدن جی‌دی ونس به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/129464" target="_blank">📅 00:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
همه رفتن سوئیس فقط آقامجتبی مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/129463" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyX1mIaur6ymSqT9fZ_BYVRK5-aCTWOJWnasmFB5TbNB_2NFfAxeiLNvvysvLmoLdBj1Osf79dv83L9pcRkiz7_nP8ZrYuCO662DD79APS6f83puRAa75ijQl_748Wh-9CIeHVD4xgPsjH1sqUjOudsanoAYlrZqkxcHGd47jCwonG9-aH509G0qMSy8dAHfiEvKkkbnMMi8ikcEcDX1RpeNeOqq8Ci-yV50ffkDPEjs6U3yOQJfl0mDso-JEO-IfC5GEGpaNXFu43-pyeyjTvGWMNMrnHJwrhUvUJvFpYCHtI63Y3UpCmNNZsgqb4KnMWG2QbuGbHB59HlQu8g1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا بعد از اظهارات ضد امنیت ملی توسط نبویان، تنگه وی هم اکنون درحال باز شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/129462" target="_blank">📅 00:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9096e084.mp4?token=pV7QGc7xLU1uCbNxBtUt9OZSO7pWQIna-7jNTD6FSAs6f7Ipd34aA-2jLdgNuQibdbuid4fkf4ZMXHEa5o_ej4uq1ouc6QiptGWDMjc7FDF8D_SkjMbZlpSKMv1Q67xCvdSzQCfjIQ63Ku2LTef9FWbXxtmluAuke08zYHeyb-ak33uwwIoYC1rPoaA6kfzXvYO7TklTZoCyecq-RskES_mvSy9wghKuaXAsNxnbz55a2eYVGKQPcMUAADdyj2SYKw7co6IaQ4pJc_BQHQiWfSpww3eeurMzODKip94QObHI_bef2q7xfh_3vpn77A1fud1FY1ZBsL_Lp7KidmnJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9096e084.mp4?token=pV7QGc7xLU1uCbNxBtUt9OZSO7pWQIna-7jNTD6FSAs6f7Ipd34aA-2jLdgNuQibdbuid4fkf4ZMXHEa5o_ej4uq1ouc6QiptGWDMjc7FDF8D_SkjMbZlpSKMv1Q67xCvdSzQCfjIQ63Ku2LTef9FWbXxtmluAuke08zYHeyb-ak33uwwIoYC1rPoaA6kfzXvYO7TklTZoCyecq-RskES_mvSy9wghKuaXAsNxnbz55a2eYVGKQPcMUAADdyj2SYKw7co6IaQ4pJc_BQHQiWfSpww3eeurMzODKip94QObHI_bef2q7xfh_3vpn77A1fud1FY1ZBsL_Lp7KidmnJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ورود تیم مذاکره کننده ایرانی به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/129461" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ونس هنگام عزیمت به سوئیس: امیدواریم در مسئلهٔ آتش‌بس در لبنان پیشرفت حاصل کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/129460" target="_blank">📅 00:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
هیئت مذاکره کننده ایران وارد زوریخ سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/129459" target="_blank">📅 00:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / جی‌دی ونس، معاون رئیس جمهور آمریکا برای پیوستن به مذاکرات بل ایران ، واشنگتن را به مقصد سوئیس ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/129458" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/ بی‌بی‌سی‌: کیر استارمز نخست وزیر بریتانیا دوشنبه استعفا میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/129457" target="_blank">📅 23:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
حسین پاک، خبرنگار مستقر در لبنان: ساعاتی قبل عملیات نظامی از سوی اسرائیل متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/129456" target="_blank">📅 23:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
خبرنگار العربیه: کارشناسانی در سفر ونس به سوئیس او را همراهی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/129455" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
محمد مرندی: ایران آماده است تا برای لبنان از توافق چشم‌پوشی کند، زیرا از متحدان خود دست نمی‌کشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/129454" target="_blank">📅 23:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-RGfhe_4Ve6QsojnC1GPdkFdbG5om9jUBQfEbeJtfS2GQH-3UDYsh5y9vMigKQ97P2u0ogwD2XK6TPrJ8kr8mmy6dDEmNMBPUPwF1RBfVLSdXyvpprEGy_7YT6cIo4n7BW2zMyKsZXCNiDe2b5eYoD5sFID7Q78BQeI22rhlJJYrW309u-T3B8K8hWsqgvOzehJSEdDfLPQKnJ3vUiBn--1QPes54SufWghgxCHYQqiB8yTEx_ZxbMbr9MRMqRFyhx2pk8kY4Aj3D5F_lwShskSmnE5h79ZTno2pa2HwbK89FqylFOhnECfP22J35DQbpSe5Si16LZWwtcgH9Utbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو تیم مذاکره، خطاب به پست ترامپ : هزنیه‌ای وجود داره، این قطعیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/129453" target="_blank">📅 23:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ونس: ما به مذاکرات ایران فرصتی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/129452" target="_blank">📅 23:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
هواپیمایی حامل هیئت ایرانی به سوئیس رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/129450" target="_blank">📅 23:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: تصمیم به آتش‌بس در لبنان بعد از فشار شدید آمریکا بر اسرائیل گرفته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/129449" target="_blank">📅 23:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/129448" target="_blank">📅 23:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رسانه اسرائیلی آی ۲۴: پشت در‌های بسته در اورشلیم، انتقادات تندی متوجه ترامپ و تیم مذاکره‌کنندهٔ او بر سر رویکردشان به ایران و حزب‌الله شده
🔴
نگرانی در اورشلیم این است که ایران قصد دارد از هر توافقی برای بازسازی اقتصاد و توانایی‌های نظامی خود استفاده کند، در حالی که امتیازی اساسی در برنامهٔ هسته‌ای‌اش ارائه نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/129447" target="_blank">📅 23:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOBlCHOPQKkTyMOZIkFi9K2npA8wrTaZb0PHdLYcjsPAlSivsq0vjZrsRuIeFNdIRymEJuZioLWdiZucRerJpe0UUa7_3btS04lLCy9op9jZUEqrF1On_4MX-aYsgFiiIsQ0zqp222Gnth3GYyHW-wU-4B3kcykI6pDaa-GlAkry8Wm9JLs2KVoiWlMdOSAKyLzja2auPKRJF4NIv-EZjUgZD4JQBpaXZ0fjfeXpCQNnVYaaglrPGBmGIJCq9lulhga23jRYetI1OyKO2exTD0bm53VgChWqaNniNoV-JrvbLsDTRb9zeedYgLYD2GAjJEnMkgfHSPsnQvJVGRnPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: در تنگه هرمز در طول ۶۰ روز دوره آتش‌بس، عوارض گمرکی وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز عوارض گمرکی اعمال نخواهد شد، مگر اینکه توسط ایالات متحده آمریکا و برای آنها، در صورتی که معامله به پایان نرسد، به عنوان خدماتی به عنوان فرشته نگهبان برای کشورهای خاورمیانه به منظور جبران هزینه‌های گذشته، حال و آینده اعمال شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/129446" target="_blank">📅 22:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کانال ۱۲ عبری: آمریکا در مذاکرات فردا به دنبال دستیابی به توافقی برای بازگشت بازرسان آژانس به ایران است
🔴
در صورت موافقت تهران با بازرسی آژانس از سایت‌های هسته‌ای، آمریکا چند میلیارد دلار از اموال بلوکه‌شده ایران در قطر را آزاد می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/129445" target="_blank">📅 22:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الجزیره: شکاف فزاینده بین ایالات متحده و اسرائیل این هفته به اوج خود رسید.
🔴
مقالاتی در نشریات مهم اسرائیلی منتشر شد که ترامپ را متهم می‌کرد که پس از امضای تفاهم‌نامه با ایران، اسرائیل را به ایران واگذار کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/129444" target="_blank">📅 22:37 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
