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
<img src="https://cdn4.telesco.pe/file/DGuTU-AmW67wLSqyIDJBbm3N1Yt4345HJCPahSokEtGFL2nxz_nFxcuQXC-snOYwJGdCjrU_2dX7F7EJQn2RrftnuCmwwQcY6MwdD2d5mekoj-XLSw2oUVVxpteKCXj5HPLVI2inDzVXggJ0RFHHTS5jEaZkimS5TUxizHP1AQ6Pvza9kXKvJSN601ICXyzY6JsJ2I_GYDRbRxm2cqARdVcKb4W61OmWgBfWavYEb6RZ7J8adOIjw--tY6MAyBW3fuKS_9LokFTky5YjEQ2sg6poWWpaHrjql-ctA1DARqhB_kmloUNF1pYWTtDky2rErLtEZh-zqB0qT5ptF0b3dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 19:44:47</div>
<hr>

<div class="tg-post" id="msg-136736">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
روزنامه عبری زبان «یدیعوت آحارانوت» به نقل از منابعی گزارش داد دور بعدی مذاکرات بین لبنان و اسراییل طی ماه میلادی آینده و در سطح سفرای دو طرف برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/136736" target="_blank">📅 19:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136735">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
لحظاتی پیش سفارت آمریکا در اسرائیل یک هشدار امنیتی برای شهروندان آمریکایی در اسرائیل به دلیل تنش قریب الوقوع در منطقه صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/136735" target="_blank">📅 19:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136734">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رویترز: چهار نفتکش روز چهارشنبه پس از تهدیدات انصارلله یمن مسیر خود را در دریای سرخ تغییر دادند
🔴
کشتی‌های مرتبط با اسرائیل، ایالات متحده و عربستان در معرض ریسک بالاتری برای حمله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/alonews/136734" target="_blank">📅 19:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136733">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35436f215c.mp4?token=dka8ocur8suCL53mnWF8daUuMitiYS61lxGj87rRJtWiSqHuI-HJyz-aSChQ1qX5I5oMpVw3j4ol3ACGgqipKku8rLRBekynWGotDDq68FUHI3VxKvGmF9MWjZBJorxMQKxhQnXXc46LytASPHrukaIF4FtB2uZt25wAL9TW6TVa-S-eyEIcJSyZTr_jpxgMkCUTaQ0EhU5JjTiZpAGPTSVmSj8FkgTh4o683PfvaRG1-k3NGk98VaiChrzl6ngiZ_sb-dxo5a3z3Cllhw_TR329mZpsmjNYVRoeMvy1MQQcAhNVACOmEScia0siAE8CvoupYlPHPrKHQ6jqY_ZtVDNucaoK5749RlxWci-HTWHRb37RCsETg9reTqWBwu3WhHPCkOFJjYUcdHyuS80hdHIZnWcSZYfioCdLQ--Gb0doWTpgzq8QTlpfpLOeHKyJ9CJOKs5HfWPPN-tAAfzL332N3VXRijUUB7csq7zvc5ZbEiuX8JyyvD-46EVlrLSYqyOnkB1xIMSWTfZpB_6l6G7jH7FTNDbU6B3sGGzQxEAlabyA5KlxsYbVRBLAvVb_0A_BxBmfdINuErBDVjhievFzSsNneDqqqjJrLriXxe-Pmoion-AmjSjrr2fGmKm9XxlE7HA2-FQR26DscEENxrGInw3_l5hST_MfIaEIQHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35436f215c.mp4?token=dka8ocur8suCL53mnWF8daUuMitiYS61lxGj87rRJtWiSqHuI-HJyz-aSChQ1qX5I5oMpVw3j4ol3ACGgqipKku8rLRBekynWGotDDq68FUHI3VxKvGmF9MWjZBJorxMQKxhQnXXc46LytASPHrukaIF4FtB2uZt25wAL9TW6TVa-S-eyEIcJSyZTr_jpxgMkCUTaQ0EhU5JjTiZpAGPTSVmSj8FkgTh4o683PfvaRG1-k3NGk98VaiChrzl6ngiZ_sb-dxo5a3z3Cllhw_TR329mZpsmjNYVRoeMvy1MQQcAhNVACOmEScia0siAE8CvoupYlPHPrKHQ6jqY_ZtVDNucaoK5749RlxWci-HTWHRb37RCsETg9reTqWBwu3WhHPCkOFJjYUcdHyuS80hdHIZnWcSZYfioCdLQ--Gb0doWTpgzq8QTlpfpLOeHKyJ9CJOKs5HfWPPN-tAAfzL332N3VXRijUUB7csq7zvc5ZbEiuX8JyyvD-46EVlrLSYqyOnkB1xIMSWTfZpB_6l6G7jH7FTNDbU6B3sGGzQxEAlabyA5KlxsYbVRBLAvVb_0A_BxBmfdINuErBDVjhievFzSsNneDqqqjJrLriXxe-Pmoion-AmjSjrr2fGmKm9XxlE7HA2-FQR26DscEENxrGInw3_l5hST_MfIaEIQHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: تهدید نابودی را عقب راندیم و به دستاوردهای عظیمی رسیدیم.
🔴
به یاری خدا، جاودانگی اسرائیل را تضمین خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/alonews/136733" target="_blank">📅 19:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136732">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
اسرائیل هیوم به نقل از رسانه‌های آمریکایی مدعی شد احتمالا «بنیامین نتانیاهو» در هفته آتی با سفر به آمریکا با دونالد ترامپ دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/136732" target="_blank">📅 19:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136731">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
منابع خبری از تداوم نقض آتش بس از سوی اسرائیل و حملات توپخانه ای و هوایی به جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/alonews/136731" target="_blank">📅 19:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136730">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر خارجه عربستان: ثبات پایدار از طریق قدرت نظامی قابل‌ دستیابی نیست. ثبات از طریق راه‌حل‌های دیپلماتیک پایدار که به ریشه‌های بحران‌ها می‌پردازه، حاصل میشه. به‌جای تن دادن به تنش‌زدایی موقت، باید راه‌حل‌های سیاسی دائمی یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/136730" target="_blank">📅 19:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136729">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/136729" target="_blank">📅 19:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136728">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نخست‌وزیر عراق علی الزیدی:
ما اجازه نمی‌دهیم عراق به یک دولت شکست‌خورده تبدیل شود و دولت ما متعهد به مبارزه با فساد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/136728" target="_blank">📅 19:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136727">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر خارجه روسیه : ارسال سلاح به ایران را رد میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/136727" target="_blank">📅 19:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136726">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ca8e4ec9c.mp4?token=E-X7Xwk75H6_L2lDCYIcT2PYRjwxpO8kbNsigfeLs5AdKPrkDuFnHABBKCE8GbnKRmOaIjqPxF0a9T3t6BkE0ivD9q50ZrP-Xml7t5yvmLY4npDhUovXiBysKBhw51AC4aj0DZbsgw8jFNcS0VhxvAif20eI2-ownJRGWYUCDEYCc9rMCDVLyrMLoTwqibYFw7pnxZpUxrS5PkCZA0b4KqN05SzZYvoq7JpTEgQN1EqX64C4s77T41sOzFi0smH1EqJKpZpqO9vT8SA5XgaJyl6ASPLOBkMGzCfoUmn1ly9DNbKe88OEAh2KIhKUuyC-6G0VXgozJaS8ogHGQdnbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ca8e4ec9c.mp4?token=E-X7Xwk75H6_L2lDCYIcT2PYRjwxpO8kbNsigfeLs5AdKPrkDuFnHABBKCE8GbnKRmOaIjqPxF0a9T3t6BkE0ivD9q50ZrP-Xml7t5yvmLY4npDhUovXiBysKBhw51AC4aj0DZbsgw8jFNcS0VhxvAif20eI2-ownJRGWYUCDEYCc9rMCDVLyrMLoTwqibYFw7pnxZpUxrS5PkCZA0b4KqN05SzZYvoq7JpTEgQN1EqX64C4s77T41sOzFi0smH1EqJKpZpqO9vT8SA5XgaJyl6ASPLOBkMGzCfoUmn1ly9DNbKe88OEAh2KIhKUuyC-6G0VXgozJaS8ogHGQdnbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت خطاب به کارگر لنج:
من به دستور رئیس‌جمهور به جنوب کشور سفر کردم و اومدم به همه کسایی که دارن تلاش میکنند خدا قوت بگم و ارادتمندم.
🔴
کارگر لنج: باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/136726" target="_blank">📅 19:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136725">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lObhwrrvR9ypxmMIZdi6mAvgpWtzr58lmveYtQRr95-Yv6W86ctY97Yq0IpdQahs1R44BRFPSaZwPPZzIb4iLrSFZ_l9UdeS45cNnYFMp7iQ31_piY723V6FN1lEV4GoWtiInEKRhzfZPo0NNtIo1rJzY7diqW3oYYTGAjFZ08h7edjPCexRKe_bz1iu3_2SCwTKBW9fjvIMAWBbQOYjrEGod0tx_djLHx9tWQmG9h0r35Be054jb52Z6MnayMJZ0DoLd3vveZlPk8FoFxthxnyWwAm5-kqQXqOtz_8JsYd62T_WuzQ96ZLg4qo_ZMjxbYMLeZgGkxz0xHJ1iKEGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت گاز طبیعی اروپا همچنان در حال افزایش است و به بالاترین سطح خود از آغاز جنگ رسیده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/136725" target="_blank">📅 19:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136724">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ در واکنش به حرفای ممدانی درباره بازداشت نتانیاهو : آمریکا به هیچ عنوان و به هیچ صورت ممکن نتانیاهو را بازداشت نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/136724" target="_blank">📅 19:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136723">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
منوچهر متکی، نماینده تهران:
قرار بود قطر ۱۲ میلیارد دلار از ۲۴ میلیارد دلار منابع ایران را آزاد کند و حتی اعلام کرد ۶ میلیارد دلار خود را بعداً پس می‌گیرد، اما آمریکا وارد شد و گفت یک سنت هم نباید پرداخت شود؛ تا امروز هم این پول پرداخت نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/136723" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136722">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رویترز: شرکت هواپیمایی کی‌ال‌ام هلند اعلام کرد تعلیق پروازهای به دبی در امارات و ریاض و دمام در عربستان را تا ۶ سپتامبر تمدید خواهد کرد.
🔴
این اقدام به دلیل وضعیت بحرانی در غرب آسیا اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/136722" target="_blank">📅 19:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136721">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
اختلال در متا (اینستاگرام، فیس‌بوک، واتس‌اپ)
🔴
درحال حاضر اختلالی از سمت شبکه‌های اجتماعی اینستاگرام، فیس‌بوک و واتس‌اپ وجود دارد.
🔴
این مشکل به صورت سراسری است و کاربران ایرانی هم شامل این اختلال هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/136721" target="_blank">📅 19:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136720">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پوتین: می‌خواهم بار دیگر تأکید کنم. مشکلاتی که در بازار سوخت ایجاد می‌شود، بدون تردید موقتی است و بر پویایی عمومی اقتصاد روسیه تأثیر نخواهد گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/136720" target="_blank">📅 19:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136719">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سی‌جی‌تی‌ان: تصاویر ماهواره‌ای نشان می‌دهند که هیچ هواپیمای آمریکایی در پایگاه هوایی العدید در قطر حضور ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/136719" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136718">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBt77Y9a79N9f-fioVwERLm-CwnqAWMHCu6aAaVuDVWst6NGA40O64MtJbmT3m75E88Vv_gmpHB1t9IkhO97NTJT761ZoBMLnzDItB_oaImDBtFxKvIBfxyYcd0NYrxzlU26mjb9Dg6RNRBJiTLjeuko20Tu5ZDABzrhfTrqujZ3BT65gTi6gTDiLYvHxJ7jEyGaj-TjTfbSw2OhmEg-bbcaRREzpWdX02gJT6Hok7jgB3D-s_sAEItvbmqrQI_EWbjS59O0I4s45t2WlxCTXdf0K2rAqnSEsh_d44KaccdERzjDgGDNsRBPN1yrghuBJ7Lc4QAUTAP_oUz28PSuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دستور پزشکیان برای رسیدگی به موضوع فیلتر شدن سایت عادل فردوسی پور
🔴
در جلسه امروز هیئت دولت، وزیر ارتباطات و فناوری اطلاعات گزارشی از حادثه اخیر مربوط به دو سایت «عادل فردوسی‌پور» و اقدامات انجام‌شده ارائه کرد و چندصدایی در حوزه فضای مجازی را همچنان از مشکلات اساسی کشور برشمرد. پزشکیان رئیس‌جمهور در این خصوص دستور پیگیری جدی موضوع و جلوگیری از بروز مسایل بدون هماهنگی را صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/136718" target="_blank">📅 18:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136717">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2801c386a4.mp4?token=D53BC1AyEsEktOyDT9jGRS1M_fUbCNHXTLaF56rUO9otcLEsnhN1uVaCZci3-j1nHWhW_cVSAd2JQAON9dNTkLVPp1SvU5oM6Va1oZ_XwFoih9SOX9xQZqUrhEz8P4dr1HFgAgg8639JRQyxAz1U4gtJb1jgTfr--otF65kKM0oFNcfVnapukPwC9y5lHhR3sRcVIrW1ZctaT-NktvH3z4e5oMh01TVr0hXprC-viMFaL1_WnHqyZSId6cqoQ0WG9Zx_fyN-LafyB8J7dWXiHhZ65_HubIEj4qZv9K1zSLp8HvUtXipDQOsFwhJnywu6rQIveFkAVS-Ti7bAOmzMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2801c386a4.mp4?token=D53BC1AyEsEktOyDT9jGRS1M_fUbCNHXTLaF56rUO9otcLEsnhN1uVaCZci3-j1nHWhW_cVSAd2JQAON9dNTkLVPp1SvU5oM6Va1oZ_XwFoih9SOX9xQZqUrhEz8P4dr1HFgAgg8639JRQyxAz1U4gtJb1jgTfr--otF65kKM0oFNcfVnapukPwC9y5lHhR3sRcVIrW1ZctaT-NktvH3z4e5oMh01TVr0hXprC-viMFaL1_WnHqyZSId6cqoQ0WG9Zx_fyN-LafyB8J7dWXiHhZ65_HubIEj4qZv9K1zSLp8HvUtXipDQOsFwhJnywu6rQIveFkAVS-Ti7bAOmzMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: بخش‌های کلیدی اقتصاد روسیه علیرغم تلاش‌های خارجی برای بی‌ثبات کردن وضعیت در بخش انرژی و سایر حوزه‌ها، باثبات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/136717" target="_blank">📅 18:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136716">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اکسیوس: شرط اصلی ترامپ برای برقراری آتش‌بس این است که ایران حملات علیه کشتی‌ها را متوقف کند و تنگه هرمز را دوباره برای کشتیرانی باز کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/136716" target="_blank">📅 18:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2371f68421.mp4?token=mvzj26OqhNxdOQRgcYAdNZK_8BOoTiD7abeusSACRGCUAZfcKcrJ-Tz95zOU9qxx9a-146R5T8H2_ptuowKPZ0moxKH5Mq23JmlqIOFv1QYEm2qSDoAkvUysCMTz3TBzebGV9ucG8FamguS0GBbC2yeCfGd_cs5b-dp3O-gjySxoYdYtjTqxxN65WjJkc4eVxWcUq5-EAhd__WsXkneDNswEJAwQU6SOiyfRPPsH4UMw_YPyV2BD8d4QYsiRo5_hnPMozu2_i_1HQGgR0jWeypZNR-9A8gsoVGJjA7BF5weGOLd19LisxszMH8Cg_MmNGGSZ8w5njZvaNmHKQJFtkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2371f68421.mp4?token=mvzj26OqhNxdOQRgcYAdNZK_8BOoTiD7abeusSACRGCUAZfcKcrJ-Tz95zOU9qxx9a-146R5T8H2_ptuowKPZ0moxKH5Mq23JmlqIOFv1QYEm2qSDoAkvUysCMTz3TBzebGV9ucG8FamguS0GBbC2yeCfGd_cs5b-dp3O-gjySxoYdYtjTqxxN65WjJkc4eVxWcUq5-EAhd__WsXkneDNswEJAwQU6SOiyfRPPsH4UMw_YPyV2BD8d4QYsiRo5_hnPMozu2_i_1HQGgR0jWeypZNR-9A8gsoVGJjA7BF5weGOLd19LisxszMH8Cg_MmNGGSZ8w5njZvaNmHKQJFtkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که نشان می‌دهد بعد از شلیک موشک از ایران، سربازان آمریکایی پنج دقیقه وقت دارند در محفظه های که برای آنها طراحی شده است پناه بگیرند، این محفظه های به دور از هم طراحی شده تا تعداد تلفات به حداقل برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/136715" target="_blank">📅 18:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هشدار سفارت آمریکا در اردن؛ بیرون از خانه ناامن است
🔴
شهروندان آمریکا باید دستورالعمل‌ها از جمله آژیرها و دیگر هشدارها را دنبال کنند.
🔴
آن‌ها باید به وبگاه‌های مرکز ملی امنیت و مدیریت بحران برای راهنمایی‌های ایمنی عمومی، از جمله توضیحات آژیرهای اضطراری در اردن مراجعه کنند.
🔴
از شرکت در تجمعات بزرگ اجتناب ورزند. از تمام مناطقی که پلیس در آن‌ها حضوردارد، دوری کنند.رسانه‌های محلی را دنبال کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/136714" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / آکسیوس: ترامپ در آستانه اتخاذ تصمیمی سرنوشت‌ساز قرار گرفته: پذیرش آتش‌بس جدید با ایران یا آغاز یک عملیات نظامی گسترده و مشترک با اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/136713" target="_blank">📅 18:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
شرکت اسلان ترکیه قرارداد جدیدی با وزارت دفاع بوسنی و هرزگوین برای تأمین سامانه‌های ضدپهپاد امضا کرد.
🔴
این سفر همچنین شامل دیدارهایی با مقامات ارشد دولتی برای بررسی گسترش همکاری‌های صنعتی و دفاعی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/136712" target="_blank">📅 18:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136710">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44376769e1.mp4?token=pkCC4fcWaPo2q7lb55UavUmfX95Qq5xHeVOUSWDu4laEE7HTUNky1s7KtXKF2H9pQBEopI6YS_pG8VfsUcqgLd67Ma2tNLXfw26YEOSDg0P7W6xKRalRwUo7p_SXuxEuPQPY7qoAmulbz3OVuzC7QiFcpAHZFDCzjIBkMGIJAJUrkVfjNLpJNwVoFRTnGip1YMsX3RsOs1dHOiMp_U4HzzxaqISFQEVP0iVsmMWZw-rfekheZUt2WubWq2JD8ZvkOK3BvPxPuiBRjtgIw7rjb2GW_b4PQqwJrLaBUmSz5Dj2igTpYTKm8VdW3Y8p9FExJtWca1ntFbcqQVFBKBQOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44376769e1.mp4?token=pkCC4fcWaPo2q7lb55UavUmfX95Qq5xHeVOUSWDu4laEE7HTUNky1s7KtXKF2H9pQBEopI6YS_pG8VfsUcqgLd67Ma2tNLXfw26YEOSDg0P7W6xKRalRwUo7p_SXuxEuPQPY7qoAmulbz3OVuzC7QiFcpAHZFDCzjIBkMGIJAJUrkVfjNLpJNwVoFRTnGip1YMsX3RsOs1dHOiMp_U4HzzxaqISFQEVP0iVsmMWZw-rfekheZUt2WubWq2JD8ZvkOK3BvPxPuiBRjtgIw7rjb2GW_b4PQqwJrLaBUmSz5Dj2igTpYTKm8VdW3Y8p9FExJtWca1ntFbcqQVFBKBQOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که هواپیماهای نظامی آمریکایی در حال ترک پایگاه هوایی فیصل در اردن هستند. این اتفاق پس از حمله امروز ایران رخ داد که در آن حداقل یک انبار هواپیما آسیب دید.
🔴
چندین فروند هواپیمای ترابری C-130، به همراه چندین جنگنده و هلیکوپتر، دیگر در این پایگاه حضور ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/136710" target="_blank">📅 18:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136709">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9eYpkgfA6Ypl4rrjwwwG158st-OBR9orcU0B0S9p1sFKJ3uWwj9habP8LbHDEP53d7YuS-GH_gHG2cWhZOjNED0kURb0vadnN7ZuU7TqN63iYizQlUFFeXeXONMp_ToY5CnJ3Nzl-_MbaePQsAcA8UOPhPw6Ozi-vCdoPFf0NfRZh8uB8TagAij_7Y-NLZuVkY3x2_A5Bghc27SYVNprqZ48zFgYeFlxJD5MtECHkdhpgFJheg4oXsnzYTsoziLGzUL8X8HRCQKSqt851brrV5GcBU7XOd7Iyg1ox7-d1I_cf9hhOAvpIMysAGZSDDsPQ9k2L4q0L1caI6NqNc2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای MV-۲۲B Osprey متعلق به نیروی دریایی آمریکا در فرودگاه مسا در ایالت آریزونا دچار آتش سوزی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/136709" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136708">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خبرنگار: آیا ایالات متحده تلاش می‌کند تا سوریه را به درگیری با حزب‌الله بکشاند؟
🔴
روبیو: ما به سوریه توصیه کرده‌ایم که بر چالش‌های داخلی خود تمرکز کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/136708" target="_blank">📅 18:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136707">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نیویورک‌تایمز: اگر انصارالله یمن از تردد کشتی‌های عربستانی از طریق دریای سرخ جلوگیری کند، حدود ۴ درصد از عرضه نفت جهان از بازار حذف می‌شود
🔴
خط لوله سومد در مصر و کانال سوئز نیز به عنوان مسیرهای جایگزین، محدودیت‌های قابل توجهی دارند؛ زیرا نفتکش‌های بسیار بزرگ قادر به عبور از کانال سوئز نیستند، ظرفیت سومد کافی نیست و در صورت استفاده از مسیر مدیترانه، زمان رسیدن محموله‌ها حدود چهار هفته افزایش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/136707" target="_blank">📅 18:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136706">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApLLLgwyGqH7QgKHufuDyY3jPh5WAl5oALaMvMJldLOdHoTSpchMrTswUuACsdrwNXC_oXfXkqDLG6kK5WHyxb5-NAv5eyMPbVGCxRY2LqfxzKsL80oQxOcW41uH3n4FSguqNytBxBrOoQet33ZkAeS9OZYldkIjj3OEF-t7DNGb8AvgsCSdLW0jIWewpblm6Fdx9p0Czyl8wWui2uzcbivxmwirPlAj-G80Vt1ZRrg7Z0f9z26ZxnA4oB1cUM4ZS-4A8AShpKV9WxlFmbQSVnK_-qSsYJ_jAsXslIRAvC3idk3jXpkLOuHmgcgIHS5BMxiaBcWgKnT9YFWNTg3KTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمیخای چیکلی، وزیر امور مهاجران اسرائیل: ما باید برای جنگ با ترکیه آماده شویم.
🔴
احتمال تماس مستقیم با ارتش ترکیه در دریا وجود دارد. این یک سناریوی غیرممکن نیست؛ این اتفاق می‌تواند فردا صبح به وقوع بپیوندد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136706" target="_blank">📅 18:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136705">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81cf502373.mp4?token=I8mSpddhLqz8q-tZAsyZA3wZgA0iBb03oLfPn9uHhXs2NFkOGD4Kx0_5aOGZq7t7kxbSWWTbS7bA838kXxr0UVjjSIzWtnr92D-gaZh3cUY6noYeEWIb6LuNSp7Jix02EPNlpqvM_KbTZa9aXtV05VWhs8UkWUJu7kdwycH2F3X6MN-GoTO6IKG8cvnGtVpdzxX66MYVBpZKVq912IGayKTZ1ee4tVjstqVGlxN0zYUCKY_XQB0CB3Ph2hThqbTI0c7wCEw3N9mxmPJErV106WJzOTKPR5KB4A4DsLjc6s5dKxP23q5fN_l97P6Bugws-5PVxTq-1BEqnRL5nzuORQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81cf502373.mp4?token=I8mSpddhLqz8q-tZAsyZA3wZgA0iBb03oLfPn9uHhXs2NFkOGD4Kx0_5aOGZq7t7kxbSWWTbS7bA838kXxr0UVjjSIzWtnr92D-gaZh3cUY6noYeEWIb6LuNSp7Jix02EPNlpqvM_KbTZa9aXtV05VWhs8UkWUJu7kdwycH2F3X6MN-GoTO6IKG8cvnGtVpdzxX66MYVBpZKVq912IGayKTZ1ee4tVjstqVGlxN0zYUCKY_XQB0CB3Ph2hThqbTI0c7wCEw3N9mxmPJErV106WJzOTKPR5KB4A4DsLjc6s5dKxP23q5fN_l97P6Bugws-5PVxTq-1BEqnRL5nzuORQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: چین با اقدامات ایران در تنگه‌ها موافق نیست
🔴
مارکو روبیو درباره ایران گفت: «فکر می‌کنم چینی‌ها ــ و البته بهتر است خودشان در این‌باره اظهار نظر کنند ــ طرفدار اقداماتی که ایران در تنگه‌ها در پیش گرفته، نیستند.»
او افزود: «چین به‌صورت علنی اعلام کرده که با دریافت عوارض یا هرگونه محدودیت بر آزادی کشتیرانی در تنگه‌ها مخالف است.»
روبیو در پایان ابراز امیدواری کرد که پکن همچنان بر همین موضع باقی بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136705" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136704">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4239c52d4.mp4?token=tyscZWZ1hj5zHITVrEU3Omo15fk6_EOigO8lNuKr4bgDu9R8MK_m11SdV2cQTdha53SHpAKKOGtuvfmvaZl2dUJdT_p6p1XLGj7ZVOH2JHHiwEfcz51t3HOZmqRb9fPIO-dHox-k4doH8o9SlQNTPbl2k8NHs-C2wlgJCMz7CwwXa7MNEYovLr1JmjuUDzzEmgBb7IllwYW-ZGERjl-UI1dUpGVY5vgH_OH-ANLQlCYh7-QBuWnkwpQOpo5XV4ZemTsotQSf_vH_DtX1_Q4adxdaAg57ucWwM051F6Cg5KBHlMlgQKrKiOqUawfEKIHRVbeMD6p7lfTHI6vdNhx7ymJOUXQv1CqpI2RKTCeJN_W3EP4zJJhMxi5srlW_VEf3QPyhqLmER9aWvO0OGJqBc1uvy2Vqxx7R9nED_4zokAh1euCf_mS2O0-_UYYM4TOHd4WPJtxVWWUFolUzTzjzWzML-vhSQaeCK6vO2rhiBOw1q-y5P4hsBrkBmT1yTlOwIKytt9Wfj1QFeAFXpkXtJndcz2On3vKSFJIo0pu1GUh9QdjrLpJBG-Y8RVWrRzLErgAuUDWQQIo6heAkkkJAe7Pa4u7ulcQT8nMddwxmrWsnB-BobQ7bxwq9L-FNXaPhZZpwBHqRWzkYmYPGIdNdk3gaUO7KCatATlLX8qZozVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4239c52d4.mp4?token=tyscZWZ1hj5zHITVrEU3Omo15fk6_EOigO8lNuKr4bgDu9R8MK_m11SdV2cQTdha53SHpAKKOGtuvfmvaZl2dUJdT_p6p1XLGj7ZVOH2JHHiwEfcz51t3HOZmqRb9fPIO-dHox-k4doH8o9SlQNTPbl2k8NHs-C2wlgJCMz7CwwXa7MNEYovLr1JmjuUDzzEmgBb7IllwYW-ZGERjl-UI1dUpGVY5vgH_OH-ANLQlCYh7-QBuWnkwpQOpo5XV4ZemTsotQSf_vH_DtX1_Q4adxdaAg57ucWwM051F6Cg5KBHlMlgQKrKiOqUawfEKIHRVbeMD6p7lfTHI6vdNhx7ymJOUXQv1CqpI2RKTCeJN_W3EP4zJJhMxi5srlW_VEf3QPyhqLmER9aWvO0OGJqBc1uvy2Vqxx7R9nED_4zokAh1euCf_mS2O0-_UYYM4TOHd4WPJtxVWWUFolUzTzjzWzML-vhSQaeCK6vO2rhiBOw1q-y5P4hsBrkBmT1yTlOwIKytt9Wfj1QFeAFXpkXtJndcz2On3vKSFJIo0pu1GUh9QdjrLpJBG-Y8RVWrRzLErgAuUDWQQIo6heAkkkJAe7Pa4u7ulcQT8nMddwxmrWsnB-BobQ7bxwq9L-FNXaPhZZpwBHqRWzkYmYPGIdNdk3gaUO7KCatATlLX8qZozVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: اقدامات چین مسیر درگیری آمریکا با ایران را تغییر نداده است
🔴
در پاسخ به پرسش خبرنگاری درباره احتمال ارائه اطلاعات هدف‌گیری از سوی چین و روسیه به ایران و تلفات سنگین نیروهای آمریکایی در حملات اخیر، مارکو روبیو گفت حضور در هر منطقه جنگی با خطرات اجتناب‌ناپذیری همراه است.
🔴
او افزود: «این حملات در واقع نشان می‌دهد ایران طی ۲۰ سال گذشته منابع مالی خود را در چه حوزه‌ای سرمایه‌گذاری کرده است.»
روبیو همچنین تأکید کرد: «هیچ‌یک از اقدامات چین، مسیر تحولاتی را که در درگیری‌های آمریکا با ایران شاهد هستیم، تغییر نداده است.»
🔴
وی ادامه داد که چین در برخی موارد حتی همکاری‌هایی نیز داشته و از انجام اقداماتی که امکان انجام آن‌ها را داشته، خودداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136704" target="_blank">📅 17:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136703">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
قیمت نفت برای اولین بار در شش هفته گذشته از مرز ۹۵ دلار به ازای هر بشکه عبور کرد، زیرا افزایش تنش‌ها در خاورمیانه نگرانی‌ها را در مورد احتمال اختلال در عرضه جهانی نفت خام افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136703" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136702">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
یک منبع نظامی به تسنیم: هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/136702" target="_blank">📅 17:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136701">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3168e57cc1.mp4?token=c83CbN5Viq3j9vVMfJ0r14ufvkfCY6IZueEobwmYCQiH8dNv1Ju7IunukUo93ZrbZL8SBbCyz2tkwOHi66uZvHKrawZpld23lsKxjn522hFbC2Ti47qOIOe75KoqSznsvpOam1DqwAigqpKue6xzLq-9aDnreVbPKJ6rS5pbHXY2C0MJutHLUf_YPfx3wYE2_XHiieACJl4rGXgqcrYxjWNX2VZCAQsQIPh7qjL4ES9PMm2byXTO1A0brLY12S9d2TtOB2WwgxSS9g23LjumJCkwXfE_VpyleY7RagNDvM-4UyGw3r1RKcgS4HFCa0KzaBrEuxlZPj2qpCSNEnx9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3168e57cc1.mp4?token=c83CbN5Viq3j9vVMfJ0r14ufvkfCY6IZueEobwmYCQiH8dNv1Ju7IunukUo93ZrbZL8SBbCyz2tkwOHi66uZvHKrawZpld23lsKxjn522hFbC2Ti47qOIOe75KoqSznsvpOam1DqwAigqpKue6xzLq-9aDnreVbPKJ6rS5pbHXY2C0MJutHLUf_YPfx3wYE2_XHiieACJl4rGXgqcrYxjWNX2VZCAQsQIPh7qjL4ES9PMm2byXTO1A0brLY12S9d2TtOB2WwgxSS9g23LjumJCkwXfE_VpyleY7RagNDvM-4UyGw3r1RKcgS4HFCa0KzaBrEuxlZPj2qpCSNEnx9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: امروز به خانواده‌های آسیب‌دیده چه خواهید گفت؟
🔴
ترامپ: فقط این را می‌گویم: «ما شما را دوست داریم؛ ما فرزند شما را دوست داریم.» تنها کاری که می‌توانید انجام دهید این است که تمام وجودتان را در این پیام قرار دهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136701" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136700">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / بلغارستان بااستقرارسوخت‌رسان‌های آمریکا در خاکش موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136700" target="_blank">📅 17:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136696">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9eeec050.mp4?token=ryCFV-Fjki4-66o80mWiLaeZfF0JoiecqWFLLCfu7IRJG2F4dS89kR1SilxYDPFvBsYwh866FARlMf_lralL-PdIdIcxo315bluVq5BfrdTcZ-w0kzjKk3GhCxdXJUDDiGYVKB984vLZWITuCp9fXf7Ues4oEHgiungHuLx30_xfeijRIyK92CKsMLrBvNdg7i4F9aa7ycV7kB0pscMaRImR_iz2kMTqeJDqtXuQYIFtVahtMOvZh0vEcm9jd9GRyzhWd6BGXjXmri23iheHMWLeobtX9m-f6ds87rqz9T0dSybVxeNlybaqvVy6TOwDTeEZ9hKg0FQVsJaRlS8iig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9eeec050.mp4?token=ryCFV-Fjki4-66o80mWiLaeZfF0JoiecqWFLLCfu7IRJG2F4dS89kR1SilxYDPFvBsYwh866FARlMf_lralL-PdIdIcxo315bluVq5BfrdTcZ-w0kzjKk3GhCxdXJUDDiGYVKB984vLZWITuCp9fXf7Ues4oEHgiungHuLx30_xfeijRIyK92CKsMLrBvNdg7i4F9aa7ycV7kB0pscMaRImR_iz2kMTqeJDqtXuQYIFtVahtMOvZh0vEcm9jd9GRyzhWd6BGXjXmri23iheHMWLeobtX9m-f6ds87rqz9T0dSybVxeNlybaqvVy6TOwDTeEZ9hKg0FQVsJaRlS8iig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری بین گروه تروریستی JNIM و سازمان تروریستی IS-Sahel دیروز در منطقه گوسی، در شمال مالی، رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/136696" target="_blank">📅 17:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136695">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec324d8d1.mp4?token=U6E2Ot0kDoQZ3qDgV16TNikZmATh_B_xdAlshwQEyZGHsSYA4I8OVw3Yl0o24cVTEAA2VwnFIBFu7PXHSSC9lNtXk2PC87YYPF_MhcT7_tcaumBPDZZWENPHTQnu0QzxsMnvyeQDtoO3jKDms8wWBm0PNgqZYey4uPdNlWquaPNuXSPOop23iJjvhyfgH2XEXmhhukOC-ZNhay0FcvKshVLaJGpztPpMOxazdwdOmoQw1zMErW6CeEaviik9k8wtUVt9liL2L_921EZQ-ib4APmW7PO1VFHIpCZ3c-A6lOIrOXbI4G8aASoz1Q4bElh8D7F1iY47RPxIuSt4RvxIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec324d8d1.mp4?token=U6E2Ot0kDoQZ3qDgV16TNikZmATh_B_xdAlshwQEyZGHsSYA4I8OVw3Yl0o24cVTEAA2VwnFIBFu7PXHSSC9lNtXk2PC87YYPF_MhcT7_tcaumBPDZZWENPHTQnu0QzxsMnvyeQDtoO3jKDms8wWBm0PNgqZYey4uPdNlWquaPNuXSPOop23iJjvhyfgH2XEXmhhukOC-ZNhay0FcvKshVLaJGpztPpMOxazdwdOmoQw1zMErW6CeEaviik9k8wtUVt9liL2L_921EZQ-ib4APmW7PO1VFHIpCZ3c-A6lOIrOXbI4G8aASoz1Q4bElh8D7F1iY47RPxIuSt4RvxIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: آمریکایی‌ها مخالف جنگ نیستند.
🔴
آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند.
🔴
هیچ‌کس نمی‌خواهد ایران سلاح هسته‌ای داشته باشد.
🔴
آیا شما می‌خواهید ایران سلاح هسته‌ای داشته باشد؟ فکر می‌کنید این خوب است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/136695" target="_blank">📅 17:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=XDCaE97PkyF1l875s6H-0KyKC0_pOPi2RhCaBmLS9-GsXVtr5awbycLroU3JTCEEWRW2U8U191kJ3USyV3CzbGkiEI1VoZt3plto-R0Dah2uaY6aV_iMFcZbLAmCjez_QXO-HPPyFXZksK4MO0CENuAVMDzx7YY3BsVj4cT_ZCu1Hkt4pGzhU8ZUzrpQ7s_2WIs6FchDIA_eUgoBVo25wVghzOR6tROV8_BOdpS55FV-kQ_AA99PnzoeXeeEkEcEkfsONPtDA6XjCNbByVsCk2K8_nTE61K-T2rlaHXSKIti1Hky5wjmr64i_Fk8wcYE3jFyTw-QPN5nMx7EZ9aQGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=XDCaE97PkyF1l875s6H-0KyKC0_pOPi2RhCaBmLS9-GsXVtr5awbycLroU3JTCEEWRW2U8U191kJ3USyV3CzbGkiEI1VoZt3plto-R0Dah2uaY6aV_iMFcZbLAmCjez_QXO-HPPyFXZksK4MO0CENuAVMDzx7YY3BsVj4cT_ZCu1Hkt4pGzhU8ZUzrpQ7s_2WIs6FchDIA_eUgoBVo25wVghzOR6tROV8_BOdpS55FV-kQ_AA99PnzoeXeeEkEcEkfsONPtDA6XjCNbByVsCk2K8_nTE61K-T2rlaHXSKIti1Hky5wjmr64i_Fk8wcYE3jFyTw-QPN5nMx7EZ9aQGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها بهای سنگینی خواهند پرداخت. آنها در حال نابودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136694" target="_blank">📅 17:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136693">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb67cefff9.mp4?token=pB8mvJMP7VPVoytURA763xnznT51cYPcwHvmAivtVXx8aD97aO96TL1KBKTuIuaS9plU9lAMR1hz-uwhgEZ1TbSRJ-pXQlKy-g8C-eTXu0QOCx6e012NrtfUMADbzOZ4PzMIjwyivyFJvgyncY4uP6tiOMrmDFzEDIz-HgvfuMkz3QKth5cqL5xjBvnUQ8G3RxJhgrK1G58Xu5iC8O5bA5lSD-PSH_OwmGeG93Yx_88Up0Tsgm2oZEDNVaiTefnJh0vLvOZbz8la8vNpsLSJeW3rATt1KmtgP7ixcuSJ6EeFF2gznp0-woqJ8FB9crjNRKXXER-ah3MndTpqPdtr7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb67cefff9.mp4?token=pB8mvJMP7VPVoytURA763xnznT51cYPcwHvmAivtVXx8aD97aO96TL1KBKTuIuaS9plU9lAMR1hz-uwhgEZ1TbSRJ-pXQlKy-g8C-eTXu0QOCx6e012NrtfUMADbzOZ4PzMIjwyivyFJvgyncY4uP6tiOMrmDFzEDIz-HgvfuMkz3QKth5cqL5xjBvnUQ8G3RxJhgrK1G58Xu5iC8O5bA5lSD-PSH_OwmGeG93Yx_88Up0Tsgm2oZEDNVaiTefnJh0vLvOZbz8la8vNpsLSJeW3rATt1KmtgP7ixcuSJ6EeFF2gznp0-woqJ8FB9crjNRKXXER-ah3MndTpqPdtr7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره سربازان آمریکایی که در حمله موشکی اخیر ایران کشته شدند:
آنها واقعاً قهرمانان بزرگی هستند. همه آنها به صراحت گفتند: "ما نباید اجازه دهیم که ایران سلاح هسته‌ای داشته باشد." آنها به سلاح هسته‌ای دست نخواهند یافت.
🔴
ما به آنها ادای احترام خواهیم کرد. برای من، این یکی از سخت‌ترین کارهایی است که یک رئیس جمهور باید انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136693" target="_blank">📅 17:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136692">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-Az32lvruAOt6BlS7jzTsoF8pFFLaMnMLF6EOGVUgkOe1svhTB8dVzcPywCJvbVYeqjHyYDQcpKHMPW_6Sxbh6vOjUJlUcWFE1npTKRXrXVZYxF4V6IXxd6xMntPunH-cQTSac9QNOtMUhCAl7F57zxSQ2FkcmP8AN9aeOUo1CuEegILKgar-A6Hek9FJNMEoZoC_Th68RMU9a5WYUKCUtkOSa5dXCHVo4Gj7qyT8jtejJ3dyosorQS0WBjXFm2zFKtRu8cakREZiGGxmJhxc3VDYvTjuyL98R7rvAS1Ul4gkvnPOcbd0Khk8tYY_nydTRC7aImvg6tRZcKQX6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس: کاخ سفید و دفتر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، در حال بررسی امکان برگزاری نشستی بین رئیس‌جمهور ترامپ و نتانیاهو در کاخ سفید در هفته آینده هستند، اما تا کنون هیچ جلسه‌ای برنامه‌ریزی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136692" target="_blank">📅 17:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOcIbld239oPw-JgbzvRYchXKAKMoVzAbTrUSRHAeqDX8i73pM5qDYAsDHwmRJwS1YJHSGSSiQL0qJox20E7LpyQ8q9X_Mb-qfe4leRLIQaoD89nFP_SZ0MKzfs5u33eOjWHWRTKx1Ry5KKyxZj-TpjJTo3Fn0rrgoSdG4KWJSImsnzZVXc33BsUYx_3SGpwJyjvQYzfRH8cYPfzfnj0PGwCkYS4Nya5i_LPos5WBq5pdtSli0neET_a4_Hbc9iQFsZsCO3UAZvtuqzMbu7vkb6dWYn_MMbQBM7Vy0K06N4syQ8UCAzcGLdHFJnk2G6meovwYCDpeBdVywMhMbsTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec16b7119.mp4?token=lguKxTjFVb1zHejT1_yzU6WPI7sKomEmXDr3jaHuitEt6dCxZ_fVDl2K_BdUZwyavH2YwVgMMuMLaAxy54n-OoBLq87MNKnKA_MFMbMWHiTw-RlV1WaJjjovRm5-wuWFetXnLeb61PVq54aG_gnzTy9xOJqpdH-865nqTAwsQwVSAGVpBk9XcCfSFJtpJugMldTjJdteghwuGLxLLfEiDqZkctYnIm03PwF81vlYp4sg96zdTckWwRR8N0p2Olk-P9W9USPruvdYgwdUz_V5yDY-PG-XDG32gWtEzB2pThMYNYWitHZjG3uotwqcoS2hnT-ktlhYLQeBOlPuIBVaPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec16b7119.mp4?token=lguKxTjFVb1zHejT1_yzU6WPI7sKomEmXDr3jaHuitEt6dCxZ_fVDl2K_BdUZwyavH2YwVgMMuMLaAxy54n-OoBLq87MNKnKA_MFMbMWHiTw-RlV1WaJjjovRm5-wuWFetXnLeb61PVq54aG_gnzTy9xOJqpdH-865nqTAwsQwVSAGVpBk9XcCfSFJtpJugMldTjJdteghwuGLxLLfEiDqZkctYnIm03PwF81vlYp4sg96zdTckWwRR8N0p2Olk-P9W9USPruvdYgwdUz_V5yDY-PG-XDG32gWtEzB2pThMYNYWitHZjG3uotwqcoS2hnT-ktlhYLQeBOlPuIBVaPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیف سطلی هم با قیمت ۱۰۰۰ یورو (۲۰۰ میلیون تومن) مُد شد.
اگه پول ندارید بخرید میتونید به جاش همون سطل رو دستتون بگیرید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/136690" target="_blank">📅 17:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136688">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KievP3gmRvfZze3nu8aY0bUvAvLHm2jqhF2CfI-GhzzP4oYp4waSG452diSuptNWYlq4t6IOBdKqjfXGEylC1QZYFRhqVkRPxXUVS0Q55mUWX0XybbUnSz-QUiWZsdT6cXrXxQk2_XHwL-CqI_eTNKMdSnTrFWNqUHVv5BIVKLSSVOSRoZvwKbjnf211ufHApNRtFkSJgFbzfmIgy12V7iowGQI_54lARVkhS-ReOiqOFdRkspWw5wXDuznPxZAU6blSwqwJccHfijp402UNa4KqEBmMPnHZP9MOvzkvjOtV0YVf3LjlbNI27s0fCBq73RdutJNw7uDjZFGiboMUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
۶ ماه طول کشید تا تونستم دوباره اینجا قدم بذارم.
🔴
جاویدنام
#غزل_جانقربان
تک فرزند ١۵ ساله و هنرجوی کامپیوتر ، ١٩ دی ماه به همراه پدرو مادرش دراعتراضات شرکت کرده بود، که نزدیک زاینده رود با شلیک سه گلوله وحوش رژیم اشغالگر جمهوری اسلامی کشته شد.
🤔
حرام زاده های حکومتی که دم از وطن و دین میزنن، قاتلین هم وطنان ما بودن و هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136688" target="_blank">📅 17:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136687">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
عون: لبنان تنها زمانی می‌تواند امن باشد که یک کشور با یک ارتش باشد
🔴
خلع سلاح حزب‌الله تنها در صورتی امکان‌پذیر است که اسرائیل عقب نشینی کند، ارتش لبنان کنترل کامل و انحصاری این کشور را در دست بگیرد و برنامه بازسازی تحت مدیریت دولت اجرا شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/136687" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136686">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
به گزارش مرکز اطلاعات دریایی مشترک، حوثی‌های یمن (انصارالله) آمادگی‌های لازم برای حمله به کشتی‌های تجاری در نزدیکی تنگه باب‌المندب را به پایان رسانده‌اند.
🔴
حوثی‌ها موشک‌ها و پهپادها را در نزدیکی این آبراه استراتژیک مستقر کرده‌اند تا برای حملات احتمالی به کشتی‌ها آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/136686" target="_blank">📅 17:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136685">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اکسیوس : حمله به تهران احتمالا می‌تونه؛ واکنش گسترده‌تر ایران رو با دنبال داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/136685" target="_blank">📅 17:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136684">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین: امروز حملات دوربرد ما اهداف مهمی را در مناطق کراسنودار و استاوروپول روسیه با موفقیت درهم کوبید.
🔴
در پهنهٔ دریای سیاه و دریای آزوف هم یک نفت‌کش و ۴ کشتی باری از «ناوگان سایه» روسیه هدف قرار گرفتند.
🔴
ما آتش جنگ را به خانهٔ اصلی‌اش یعنی خاک روسیه بازمی‌گردانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136684" target="_blank">📅 17:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136683">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNK5y5DDfetsBE654lKnrwyH28_RSYimjkyojcjDYcRvjkvq1WmuLp5Se2Ygd835egFat-FpyX4fmqWCZAcqvoturfk8sqUxusG_0h7D6jmoFoPNykxVRdJr1TLg9tzgPcblK_4hjvBi2oh_FiD7X4g4CQb_sdizB-ltUgrC7JWUTPfEf9puXNqLVy3PsDUleRWREKvIKG7jgAD4gaDcXxnAXZfA2AF2_3slSNhpB4m7vXET50FWVnxU7yDDLE3mYHNWIdScWQLS4h2UI9U70bqtgGNOj0QOp0zIfQh4oUfmzPkvzPXYqp-LXLORTai-qyX5i0uK3tEQZjHU1RbGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: به نظر می‌رسد ایران هر ایده‌ای را که شامل یک جدول زمانی برای آتش‌بس باشد، رد می‌کند و هرگونه مذاکره‌ای باید مبتنی بر بازگشت به اجرای یادداشت تفاهم باشد.
🔴
تهران معتقد است که مهلت‌های آتش‌بس صرفاً دوره‌هایی برای تجدید قوا و بازگشت به جنگ هستند و نمی‌خواهد در این چرخه گرفتار شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136683" target="_blank">📅 17:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136682">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
معاون امنیتی استانداری چهارمحال و بختیاری: در حملات دیشب آمریکا، نقاطی از شهرستان کیار مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136682" target="_blank">📅 17:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136681">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رسانه‌ عبری: ترکیه در صورت ورود نیروهای کُرد به جنگ، از ایران حمایت خواهد کرد
🔴
برخی مقامات ارشد اسرائیلی ادعا کردند ترکیه تهدید کرده در صورتی که نیروهای کُرد به عنوان بخشی از یک طرح زمینی تهیه شده توسط موساد، وارد خاک ایران شوند، از ایران پشتیبانی هوایی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136681" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136678">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFqg7_JIGaOTGr71gSxUKZxzaGs0j5i08gKLu60okzBViBd7plgSWu2cLCgrSJuSSBimQ_5Of_diiRc2NbkXXb1XYBiq5edxr6KORLcVajcr3q1EIweEgT4ugIXcCSpFhnZ-M-h63_DIiwO0hWkkivC4Yyy1f10-tMoWXZ1qgkAziELsXVHTCEd2mR312v0Ux8qADCPxS7p_DoCUyrZ29I6cYaOxDQt3cBvk1H3bApTwgfALDNhvsY_w-sxtC3t6eq_YwL_rJI3hJt8SA4FLcm2Mcx8JsIxhMtDXYYgsPb_k9ajuvXEd3Mxfgg3N2IN-Xvegyd4Pab1vmgaXZToHQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d8d194b1.mp4?token=gIWZIAK0kIhWxftnaPmSlXttFljMfygYo_PAhR3Dodm-MrCSqpBn80IrK9tE3OUTEfQ1iLSrXBZ9CgH1vzbJjbrate6FEkQQC9ZZcUppkYEs4S19mN3DzDeDmMk-4Us43Z7xrve8iwjv-b63LMbQ2pqdpMkVM1qTHpskFuVzuepmCpzDdZffedXxfcN61A2JMKTKaXcniEUDqLJJPSNkRUtSiUNs0wn1pgenAWFj92O43QzTQiOSx-ATm9RHoasaGA027dnJhXD6EQG1J9THtvu2dbD5TYm4VcMBtL0cNvsW2G3thXFVWA6IoSblIyAaomvBLlYYCSdOoK-GowgNbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d8d194b1.mp4?token=gIWZIAK0kIhWxftnaPmSlXttFljMfygYo_PAhR3Dodm-MrCSqpBn80IrK9tE3OUTEfQ1iLSrXBZ9CgH1vzbJjbrate6FEkQQC9ZZcUppkYEs4S19mN3DzDeDmMk-4Us43Z7xrve8iwjv-b63LMbQ2pqdpMkVM1qTHpskFuVzuepmCpzDdZffedXxfcN61A2JMKTKaXcniEUDqLJJPSNkRUtSiUNs0wn1pgenAWFj92O43QzTQiOSx-ATm9RHoasaGA027dnJhXD6EQG1J9THtvu2dbD5TYm4VcMBtL0cNvsW2G3thXFVWA6IoSblIyAaomvBLlYYCSdOoK-GowgNbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای تأیید می‌کنند که در جریان آخرین حملات ایران، یک آشیانه هواپیما در پایگاه هوایی ملک فیصل در اردن هدف قرار گرفته است.
🔴
پیش‌تر ایران اعلام کرده بود که این حمله، آشیانه تعمیر و نگهداری جنگنده‌های F-15 نیروی هوایی آمریکا را هدف قرار داده، چند فروند پهپاد MQ-9 Reaper را که در آن نگهداری می‌شدند منهدم کرده، به چند بالگرد آسیب رسانده و همچنین تلفات انسانی برای نیروهای آمریکایی به همراه داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136678" target="_blank">📅 17:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136677">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlLgx5E4ys1uKuEGZWYwp41wguy0sFtd_JUwMNHRTQm7FB4JIqgwtChbC3C4Vqs4l3tgGZz7SBiaTCiskALi_LdHDWY_883UZwPAZXOSYD_l5N-AjXx2EXC7zrRmsF9tbFs-aFxyxOb5ZEcm6Y12j0fAWWcCndYwf2xeO2rRAJWVJEvpytY543WPk2hfLPNntoftNm_jeWS86sTKZOL-lDnQRfzeP1k2-7HvmtrMAy59wnjPdbzELEGNJSOXY7OClS9fBFMbg0Z242ADhtMow-Ql9e1ig73QDJ7QZVIzGIN0pZPnaPoMopuiaBpJqy-k8DjyeTZC_zW16Fw8YPGCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، خطاب به ترامپ : وقتشه کویت، قطر، عربستان، بحرین، امارات و احتمالاً عمان رو تخلیه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136677" target="_blank">📅 17:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136676">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پهپادهای اوکراینی در ۲۴ ساعت گذشته، ۱۳ شناور را در دریای سیاه مورد هدف قرار دادند، که شامل ۱ تانکر، ۱۰ کشتی باری و ۲ یدک‌کش است.
🔴
نیروهای سامان‌های بدون سرنشین اوکراین اعلام کردند که بین ۶ جولای و ۲۲ جولای، ۱۹۶ شناور روسی را مورد هدف قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136676" target="_blank">📅 16:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136675">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1UVBcVtvMhIBUA92UBFm_u2kO7WkGNt-kfD8UIE5lS6yaLy3FHyO6dLO4cTwYT1JExZmMHVeDaNcHjL2LCQjJt8nhUsf-416k92-JUH6e5msjCdVPRCaOgSjIIA_o209gndj5dzFiqW_5-Y1W2e57hif-5nSc-9TjahySuDHma3l35m7WCVdhDCZWDHjPnjECi7Fz5krK6PUiZNxKj22NFfeBMdl4pclC4nZeF3sd_THy7HEFEEvrZ_WnM_wvers2hQqPFt9P4T6YtDkJwMKzyH3GYfK05sYaV0cZUqdKSiTBtPpTW8Ec9TVtFAy-PYEz2nNGEbP8u24IXEF5FEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هوتن قلعه نویی: بابام افتخار بزرگی برای ایران به ارمغان آورده و ۱۴۰میلیارد پاداش عددی نیست که الکی بزرگش کردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136675" target="_blank">📅 16:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136674">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواسته است به دلیل افزایش تهدیدها و خشونت‌ها ، در شهرهای تل‌آویو، یافا و هرتزلیا احتیاط بیشتری به عمل آورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136674" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136673">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پاکستان اقدامات یمن علیه عربستان را به شدت محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136673" target="_blank">📅 16:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136672">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
انتقاد تند رضا رشیدپور به امیر قلعه‌نویی: ملت از دشمن خارجی بکشند یا از برخی دوست نماهای داخلی که خودشان را مرکز حقیقت می‌دانند و دیگران را وطن فروش.
🔴
عراقچی درست می‌گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136672" target="_blank">📅 16:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136671">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / ترامپ: «از این لحظه به بعد، هر زمان که ایران به یک کشتی در تنگه هرمز شلیک کند، چه با موشک، راکت، پهپاد یا هر وسیله و سلاح دیگری، ایالات متحده یک پل یا نیروگاه برق را بمباران و نابود خواهد کرد؛ از جمله پل‌ها یا نیروگاه‌هایی که در نزدیکی پایتخت یا در داخل شهر تهران قرار دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136671" target="_blank">📅 16:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136670">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnMk34xLkw85oLF7WEWMeqfDbCIGbkGiu5zadQXCCdRUZFhjRTI1KCIk1qoE_hBfRpLNYEyC1NXAPLgY_14ocykyVi2qlZcxnAAah8bnJ9eTXdPtlMLpZhDTM1WsYKD3HiirXnbHgU-3iE1NaGpAgfcwRgrIdO2TDfk6U6mp4gF8TdBuqvkTts3s_pyOIPL6A8Ch8Upg_Xi54MMdOWdfARLfvq4dcGmtqwJPsOf6HJ6NZP2dh0rMdr18e2dqhsK6-1etsOyejytgWzu8Ia3nFJZ9005_jbpbdNLpT10vD8ft060TKqRmBWoAQxqbLyVTT_ZgSDl8tevRmnTw3i6cGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ  : عازم پایگاه نیروی هوایی Dover برای ادای احترام به قهرمانانمان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136670" target="_blank">📅 16:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136669">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گروسی: ایران به سرعت دسترسی به مراکز هسته‌ای ایران را برای بازرسان تسهیل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136669" target="_blank">📅 16:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136668">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: پاکستان میانجی اصلی ما در مذاکرات با آمریکاست !
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136668" target="_blank">📅 16:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136667">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شرکت بزرگ کشتیرانی دانمارکی، مارسک، به دلیل افزایش حملات روسیه به زیرساخت‌های بندری، به طور موقت خدمات خود را در بنادر دریای سیاه اوکراین متوقف کرده است.
🔴
تا اطلاع بعدی، کشتی‌ها به جای آن به بندر رومانیایی کنستانتسا تغییر مسیر خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136667" target="_blank">📅 16:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136666">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت بهداشت ایران اعلام کرده است که از تاریخ ۲۷ ژوئن، در حملات ایالات متحده به نقاط مختلف کشور، ۵۳ نفر کشته و ۵۹۲ نفر مجروح شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136666" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDCNOiSRjoQQK4lc0OBm7vE5-NEr_eEE4GLJxgxFQZv9PKGNNwNR2En-dO6Y9x0okH9cwSVy6F37UJI93b3K_V0nER4DWBSk34NNmZITnVxNnyBv4F8778Qhak0L6uLu7LGvERgMFhyDV3W_2vKH5tzhITT3ip0JwfXMxcPCw7js9_Bmd99HImv7nELI6zZhjg7K4Wnbh3fj8a2n7NAFs012wvoBrN8jvtkqkIzDqQQPx5gOhk17oPyXCw5WlPx7BKFV7LDcjrCep0oI096UbNnbsOQoNnnJorWI1ZqpciYMasyDMe17kUJcv1Qsy-V1oQ30W5dAK6-64K-fE4tl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrEEcwrJW6kJPPNz6eWpvh-0hcFsk8WqwgX_pEDOjLCIXfJ185m7uFQY8gfyLXVFTQYYOSHlm_-CRJ2mOEsqn2CE6y-lj3z21n5k_OL9GfnlRQ-nbvkwR0Z1svJFE-xyQfmYtI7p7CzbjY1QFymBBlY4N4KRA6VPSdHAwDiuFK23n3MERhVclTc-0F12RUc2lyqUjMNz4OG9rLfY_Yn3z10tN4Z3n8FYVvz9HWfdEs-9fFNSyUkSzgYVy1Tt-ZgpsnyxfWCaOnOe27X8FrDO8BAI7R2RX8IzRsaeVnCx082d7QYuRGNGb5c3U7uALgT4IFrKvQsS6CVV0jMO8cPUHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ed108863.mp4?token=bcF_vCy_5p-K1dMuMVJGm46q1AQvERUZCZdWIzsIDObbFEd8yDZVgEkRI3C2PA0wZvCNLyTrIK20JJGHH338yxX-xE9ob6CosmJd10Lpef2pZTUvSitEniF95vbiQ5PfDrMvIqhzdCGNqCqv6J4hqziLlXDp_qYrXL1orLb0Bnf1DBaVKeWRxU21qhgRADpgiDAXErdPSvE3lEG2aLdcbt3n8-6rUae12lehr_wXmTloRKJGKVY7uqDS4VNrFIeyafzVa7KdCJ9o6-eUzaYy95K4ZDOyCB3lPeinecusTCPOosqcpQjcwgKGoiLr-XGgTa6f3UBQLsau190QMPj4cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ed108863.mp4?token=bcF_vCy_5p-K1dMuMVJGm46q1AQvERUZCZdWIzsIDObbFEd8yDZVgEkRI3C2PA0wZvCNLyTrIK20JJGHH338yxX-xE9ob6CosmJd10Lpef2pZTUvSitEniF95vbiQ5PfDrMvIqhzdCGNqCqv6J4hqziLlXDp_qYrXL1orLb0Bnf1DBaVKeWRxU21qhgRADpgiDAXErdPSvE3lEG2aLdcbt3n8-6rUae12lehr_wXmTloRKJGKVY7uqDS4VNrFIeyafzVa7KdCJ9o6-eUzaYy95K4ZDOyCB3lPeinecusTCPOosqcpQjcwgKGoiLr-XGgTa6f3UBQLsau190QMPj4cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد از بررسی ها و آزمایشات DNA  امروز قطعات پیکر تعدادی از دانش آموزان مدرسه  میناب روی دستای مردم این شهر به خاک سپرده شد
🔴
همچنان اثری از ماکان نصیری تو قطعات شناسایی شده نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136662" target="_blank">📅 15:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/ رسانه های داخلی: دستور مقامات ارشد سپاه برای گسترش دامنه درگیری در غرب آسیا صادر شده و ضربات در ساعات آینده به مناطق غیرمنتظره خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136661" target="_blank">📅 15:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136660">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فیصل بن فرحان، وزیر خارجه عربستان:
ثبات پایدار از طریق قدرت نظامی قابل‌دستیابی نیست
🔴
ثبات از طریق راه‌حل‌های دیپلماتیک پایدار که به ریشه‌های بحران‌ها می‌پردازند، حاصل می‌شود
🔴
به‌جای تن دادن به تنش‌زدایی موقت، باید راه‌حل‌های سیاسی دائمی یافت شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/136660" target="_blank">📅 15:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136659">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سازمان ایمنی هوانوردی اتحادیه اروپا:
توصیه می‌کنیم تا تاریخ 31 آگوست 2026، از پرواز در فضای هوایی اردن خودداری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136659" target="_blank">📅 15:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136658">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYztYSwc5U73GKWRAjfS9bz7SmpFpxTfSB2euP2PSU3_06lWOKLi2Be62wML7QPrmM_7lTYwBPs_oxbiItp-m0BP5UwXL1yQjWrUJHRxjblfP6I_QalBMlQ65c8-1aXFR58HDaV98y96I_ws7Vj5GNn_1mCT_DDcKY1yCqkxKIoMWyUs5Acav8MoEPlalUy-ZbXdgwAi2ZNyFxKS5EtjYwgDPDW4X3jiO6wqoZqBG4FZrnjFBsoDO82fuwYBrwxTnXRzc1ajA41oIVytGd3phBttEbKTYsqCBkKKZHTXOkfOdvEmHQQ2KuanNUEsM7mWRCa23OmxdMxKn_eAKIto8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت هواپیمایی خلیج فرود در فرودگاه ملک فهد را به تعویق انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136658" target="_blank">📅 15:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136657">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رویترز: پاکستان پس از اینکه در میانجی‌گری مذاکرات آمریکا و ایران نقش داشت، از واشنگتن درخواست تسهیلات ۱۰ میلیارد دلاری کرد تا ذخایر ارزی خود را تقویت کند
🔴
اسلام‌آباد امیدوار است که نقش دیپلماتیک خود را به پیوند‌های اقتصادی قوی‌تری با ایالات متحده تبدیل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136657" target="_blank">📅 15:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
تلویزیون بحرین: سامانه‌های پدافند هوایی در حال مقابله با حملات هوایی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136656" target="_blank">📅 15:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136655">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
هدف حملات پایگاه آمریکا در شهر الدمام در شرق عربستان بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/136655" target="_blank">📅 15:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136654">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
تسنیم: دقایقی قبل آمریکا جزیره لارک را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/136654" target="_blank">📅 15:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136653">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
آژیر خطر در الدمام، عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/136653" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136652">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزارت کشور بحرین: آژیرهای هشدار به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136652" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136651">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری/ دفاع مدنی عربستان سعودی: آژیر هشدار در شهر الدمام برای هشدار درباره وجود یک خطر به صدا درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136651" target="_blank">📅 15:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136650">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری/ دفاع مدنی عربستان سعودی:
آژیر هشدار در شهر الدمام برای هشدار درباره وجود یک خطر به صدا درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136650" target="_blank">📅 15:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136649">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/ هم اکنون حمله به بحرین و فعال شدن آژیر های خطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136649" target="_blank">📅 15:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136648">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری/ هم اکنون حمله به بحرین و فعال شدن آژیر های خطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/136648" target="_blank">📅 15:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136647">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تمرکز آمریکا بر کوه کلنگ که هیچ فعالیت هسته‌ای در آن وجود ندارد، چیزی جز بهانه‌جویی برای تخریب و ویرانگری نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/136647" target="_blank">📅 15:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136646">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گروسی: نمی‌دانم بازرسان چه زمانی به ایران باز می‌گردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/136646" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136645">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/سپاه: اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136645" target="_blank">📅 14:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136644">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
داده‌های سایت ناوبری کپلر: دیروز دو نفتکش وارد تنگه هرمز شدند و دو نفتکش دیگر از این تنگه خارج شدند که یکی از آن‌ها نفتکش گاز از ایران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136644" target="_blank">📅 14:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136643">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رویترز:امروز، چهارشنبه، ۴ کشتی مسیر خود را در دریای سرخ تغییر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136643" target="_blank">📅 14:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136642">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMtWRpUX1cn8kN_SFuJbfUj2k_WIO4U6p6MP1Vlu-Alx5h4S7_XHnHI1r3Xyep4W47u9HFFadTYZ8nFYpyVzrssS-qZoblwGrBpjGbeI_O7e_hO8_2nZhTUfiY1eXtrIV0nmrr5RyNLgGEA8g65quJvsbV3YGkQUepEW6cH_MOpZ7VW8QXCgIQrw0fZFWPMJT4vIdMnW91QfT65d6m-VE9KxU7eE9F_zJnOvXjUT7Z-b5regA174ccUoxCeXh383m5PRAuLQm3hWMyyfo4SVrYPjmAwtlK9kCIV_GvTtejJdu-Qb_W8_Q6_n9rWfzW9jVcpixFB42jrmFYlIQPC7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسماعیل بقائی: حملات و تهدیدات مکرر آمریکا علیه تاسیسات هسته‌ای صلح‌آمیز ایران، نه تنها نقض آشکار اصول اساسی منشور سازمان ملل، حقوق بین‌الملل و قطعنامه‌های مربوطه هیئت مدیره آژانس بین‌المللی انرژی اتمی، کنفرانس عمومی و شورای امنیت سازمان ملل متحد را تشکیل می‌دهند، بلکه خصومت عمیق آمریکا را نسبت به پیشرفت علمی و توسعه فناوری ایران نیز آشکار می‌سازد.
🔴
فعالیت‌های هسته‌ای ایران به طور کامل به آژانس بین‌المللی انرژی اتمی اعلام شده است، مطابق با تعهدات مربوط به تضمین‌های لازم. تمرکز وسواسی واشنگتن بر منطقه کولانگ کوه (کوه کلنگ) که هیچ فعالیت هسته‌ای در آنجا انجام نمی‌شود، چیزی جز یک بهانه ساختگی برای تهاجم، تخریب و خرابکاری نیست.
🔴
ضمناً، مدیرکل آژانس بین‌المللی انرژی اتمی، که کاندیدای تصدی پست دبیرکل سازمان ملل متحد نیز هست، کجاست؟
🔴
مردم ایران با اراده و اتحاد کامل، آماده‌اند تا با تمام قدرت، هرگونه اقدام خصمانه آمریکا یا نقض حاکمیت و امنیت ملی کشورشان را پاسخ دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/136642" target="_blank">📅 14:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136641">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
👈
وال استریت ژورنال: با وجود ماه‌ها حملات آمریکا و اسرائیل، ایران نشان داده است که هنوز نیروی موشکی توانمندی دارد.
🔴
حمله موشکی اخیر به پایگاه هوایی آمریکا در اردن که منجر به کشته شدن سه نظامی آمریکایی شد، نشان می‌دهد که تهران دسترسی به سایت‌های موشکی زیرزمینی را بازیابی کرده و همچنان به پرتاب موشک‌های بالستیک پیشرفته، از جمله خیبرشکن، ادامه می‌دهد.
🔴
تحلیلگران نظامی می‌گویند ایران پایگاه‌های آسیب‌دیده را تعمیر کرده، ذخایر موشکی قابل توجهی را حفظ کرده و توانایی خود را برای به چالش کشیدن دفاع هوایی ایالات متحده بهبود بخشیده است.
🔴
در حالی که مقامات آمریکایی می‌گویند قابلیت‌های موشکی ایران به شدت تضعیف شده است، حملات اخیر نشان می‌دهد که تهدید همچنان قابل توجه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136641" target="_blank">📅 14:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136640">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آنتونیو تاجانی، وزیر امور خارجه ایتالیا، اعلام کرد که ایتالیا میزبان دور جدیدی از مذاکرات بین اسرائیل و لبنان در تاریخ ۴ آگوست خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136640" target="_blank">📅 14:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136639">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03508862dc.mp4?token=VHl423Jm1lKvdrvpKfEVTqgh3Jtg4b1w24aApTzCc87DEOyUVrTARbvpFRpScGPwVQNafbmlu_LKVcvFIojZmezeMgz24BEBlOmFY08Gqcsc3mDpgqPyoTTIZLlkTj26fllax6MBSBCjD6Onb2JTRtNJ-niICVaE7BCAcdqmmDGkoZMZsdoMf-4mrYR-fPUK-yk56j1kIS-p-P84Tl4fGNtoX23AkVZxJpyfhTCXGYWeYhvhM4pBcH2V6lLD8LpvHu3EBRkLvxyr0n0fxHKhcLrDSmy2MrHQBsWTDHybVbLHAqUpYS-528AOVf1Jol6MAYl2c1v32zmDD_cuCcP94UhTZjS4rohjskDO-BZVQ2zCnW2SdWMUv3ZTQfFJWK-E_BDWEh_NLQPqqktgKLMOs0dkdW4bjFJ1LQ5S0hqYA69ILnqBU8Iaccl7n0LR4i1vilzSQzvHY_OBHaXNyov03w7Zd1YojLFd1_m9RqqiFb1QIyeAKXdsi3fk64T8SNXgPZerJQ6Rl1KIsf5a0tmXoCznpWKNVgIXjQeQHauNY3KXBwtaQIPZ_bfgvXCvxVU8R1lNQOPFUX8m90FTqNQGQuVlTJWq01KL14LpggnJDul7KH8l46z8GRD50tc5AKPRMK_uScS2p_LDe6li2ryVgXc93u0k0G1PlDm_t0HwqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03508862dc.mp4?token=VHl423Jm1lKvdrvpKfEVTqgh3Jtg4b1w24aApTzCc87DEOyUVrTARbvpFRpScGPwVQNafbmlu_LKVcvFIojZmezeMgz24BEBlOmFY08Gqcsc3mDpgqPyoTTIZLlkTj26fllax6MBSBCjD6Onb2JTRtNJ-niICVaE7BCAcdqmmDGkoZMZsdoMf-4mrYR-fPUK-yk56j1kIS-p-P84Tl4fGNtoX23AkVZxJpyfhTCXGYWeYhvhM4pBcH2V6lLD8LpvHu3EBRkLvxyr0n0fxHKhcLrDSmy2MrHQBsWTDHybVbLHAqUpYS-528AOVf1Jol6MAYl2c1v32zmDD_cuCcP94UhTZjS4rohjskDO-BZVQ2zCnW2SdWMUv3ZTQfFJWK-E_BDWEh_NLQPqqktgKLMOs0dkdW4bjFJ1LQ5S0hqYA69ILnqBU8Iaccl7n0LR4i1vilzSQzvHY_OBHaXNyov03w7Zd1YojLFd1_m9RqqiFb1QIyeAKXdsi3fk64T8SNXgPZerJQ6Rl1KIsf5a0tmXoCznpWKNVgIXjQeQHauNY3KXBwtaQIPZ_bfgvXCvxVU8R1lNQOPFUX8m90FTqNQGQuVlTJWq01KL14LpggnJDul7KH8l46z8GRD50tc5AKPRMK_uScS2p_LDe6li2ryVgXc93u0k0G1PlDm_t0HwqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده، و وانگ یی، وزیر امور خارجه چین، در حاشیه اجلاس آسه آن‌‌ با یکدیگر دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136639" target="_blank">📅 14:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136638">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e2cd52ad.mp4?token=cStNF7TBKZFPhEI6oZOyDwXq81WQ9oWwrPCE0W11fFoATu80M1OTNlLzpPaU0nsBgtMfKpxub9B5CpLJeNfJ9GuHmj7TRS1u311UlB5aWwPbpQHI1HvdUmwQxUIpjQtI-3TGnVzPIi3164k0msCztQPPmglVUBe4NqkK2onXGyKk1RHv5cXLpSFAz4DQQskbtkdbeLzxLYP7pXML8wyWGDsBYJg0TPxu3I5hqTT3EZLv9SfXyvJ7mDL8W9BnQHTSU7Ld-0Ts607sCjzGMYN9kE-Slu8ZR7Jfgxa92sr_pRzXl0ZoeVsDTZ_XNcXG1jm8-c61LOacv1Bjmv3z_DVj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e2cd52ad.mp4?token=cStNF7TBKZFPhEI6oZOyDwXq81WQ9oWwrPCE0W11fFoATu80M1OTNlLzpPaU0nsBgtMfKpxub9B5CpLJeNfJ9GuHmj7TRS1u311UlB5aWwPbpQHI1HvdUmwQxUIpjQtI-3TGnVzPIi3164k0msCztQPPmglVUBe4NqkK2onXGyKk1RHv5cXLpSFAz4DQQskbtkdbeLzxLYP7pXML8wyWGDsBYJg0TPxu3I5hqTT3EZLv9SfXyvJ7mDL8W9BnQHTSU7Ld-0Ts607sCjzGMYN9kE-Slu8ZR7Jfgxa92sr_pRzXl0ZoeVsDTZ_XNcXG1jm8-c61LOacv1Bjmv3z_DVj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی اوکراین به مرکز توزیع شرکت تجارت الکترونیک وایلدبریز کراسنودار روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136638" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136637">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1516e3b0.mp4?token=KOvLxFm66ZH2OG3_8TSWy5E_FOTCrgkvS9CU8OCPU2DbJK-DGIL_2ZTmB1z09cAZelx-4f-EMDDqg1Mzby8bduUEbyPwIxC2Fjk846hvx9HE_L13J_x5ntR8EKjyy1jS8-WA87KHvdGZtyR6D4k7Yb9iSiZ3FF1m9lKzf2UBU3lH_cXBAo6rGhm4rW-0UR8r8KTa6ZsBDqWmTvuY1ERuWUJrkmuHf7aS3Rxo5LnUhcBMjYBfVtdIIRWm1Zkm8oVU5nrX3pU9J6pzhPwKQa24zOwTCVuv8kbeGcGODPR5jSfyNUV2YSdJoIsCVkUHmm96ntXwwHtAe1v5ApoWLiGveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1516e3b0.mp4?token=KOvLxFm66ZH2OG3_8TSWy5E_FOTCrgkvS9CU8OCPU2DbJK-DGIL_2ZTmB1z09cAZelx-4f-EMDDqg1Mzby8bduUEbyPwIxC2Fjk846hvx9HE_L13J_x5ntR8EKjyy1jS8-WA87KHvdGZtyR6D4k7Yb9iSiZ3FF1m9lKzf2UBU3lH_cXBAo6rGhm4rW-0UR8r8KTa6ZsBDqWmTvuY1ERuWUJrkmuHf7aS3Rxo5LnUhcBMjYBfVtdIIRWm1Zkm8oVU5nrX3pU9J6pzhPwKQa24zOwTCVuv8kbeGcGODPR5jSfyNUV2YSdJoIsCVkUHmm96ntXwwHtAe1v5ApoWLiGveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتسب به حمله ساعتی پیش آمریکا به سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136637" target="_blank">📅 14:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136636">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شاهزاده محمد بن سلمان، ولی‌عهد سعودی در یک گفت‌وگوی تلفنی با شیخ مشعل الصباح، امیر کویت، بر همبستگی و حمایت کامل پادشاهی عربی سعودی از کشور کویت تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136636" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136635">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
مارکو روبیو، در مورد محاصره دریایی بنادر عربستان سعودی توسط انصارالله:
حوثی‌ها در گذشته نیز تهدیدی برای حمل و نقل جهانی محسوب می‌شدند. این یک تهدید جدید نیست. ما در طول هفته گذشته چندین بار با مقامات سعودی در مورد این تهدید گفتگو کرده‌ایم.
🔴
ایران در این میان نقش دارد. ایران عامل ایجاد مشکل است.
🔴
آنها تصمیم گرفتند پروازهای مستقیم از تهران به یمن را آغاز کنند و عناصر سپاه پاسداران انقلاب اسلامی و دیگران را به این کشور بفرستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136635" target="_blank">📅 14:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136634">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سازمان ایمنی هوانوردی اتحادیه اروپا: توصیه می‌کنیم تا تاریخ 31 آگوست 2026، از پرواز در فضای هوایی اردن خودداری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136634" target="_blank">📅 14:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136633">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزارت بهداشت ونزوئلا: سه نفر در ایالت «آنسوآتگی» در  ونزوئلا بر اثر ابتلا به هانتاویروس جان باخته‌اند.
🔴
آمار رسمی نشان می‌دهد که سه بیمار در آنسوآتگی دچار وضعیتی شدند که منجر به آسیب قابل توجه ریه شد و سپس در بیمارستان درگذشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136633" target="_blank">📅 14:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136632">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b71bc601.mp4?token=g9mXL9BEljKD7vdaHwUqatbS3jBASLhoAwkLqHDl4ogFPAK00o463hEPlkZZQDmKrdnmgTecCawbVeToWzFPsFKNYzuuGgMLNA161qxLVpeFbZGq-QyocBjivYFQ0NcBNA_VG0dRAaqCJY1TFAVB0oryUYPhWuExxJ4JcHYp1mlYGD8jljhAoVGv6M0B5oou8gcT4vNQU6ga5YqaO3Lw4yK2E7UwoGxVjYg7dmzmzVyJFrHCvHEQSB1CFgx9kgdUuctFm2Mn3vAZ8Hb8HiVSXe20jnE10CEyJjFdQx2ujXzxzXIUDH6vkm8E_PD4pvknGEbeU9U5n7774lMhCNNJ8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b71bc601.mp4?token=g9mXL9BEljKD7vdaHwUqatbS3jBASLhoAwkLqHDl4ogFPAK00o463hEPlkZZQDmKrdnmgTecCawbVeToWzFPsFKNYzuuGgMLNA161qxLVpeFbZGq-QyocBjivYFQ0NcBNA_VG0dRAaqCJY1TFAVB0oryUYPhWuExxJ4JcHYp1mlYGD8jljhAoVGv6M0B5oou8gcT4vNQU6ga5YqaO3Lw4yK2E7UwoGxVjYg7dmzmzVyJFrHCvHEQSB1CFgx9kgdUuctFm2Mn3vAZ8Hb8HiVSXe20jnE10CEyJjFdQx2ujXzxzXIUDH6vkm8E_PD4pvknGEbeU9U5n7774lMhCNNJ8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا این توافق‌نامه، ذاتاً دارای نقص نیست، زیرا در بند ۵، اذعان شده است که ایران در تنگه هرمز قدرت دارد؟
🔴
روبیو: فکر نمی‌کنم که این توافق‌نامه دقیقاً این را بیان کرده باشد. این توافق‌نامه به آنها حق پرتاب موشک به سمت کشتی‌های تجاری را نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136632" target="_blank">📅 14:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136631">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مارکو روبیو: ما نسبت به کارایی مذاکرات بدبین هستیم، زیرا طرف ایرانی به تعهدات خود پایبند نبوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136631" target="_blank">📅 14:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136630">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر خارجه روسیه: تداوم درگیری به نفع هیچکس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136630" target="_blank">📅 13:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136629">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edfc958cd.mp4?token=TArTnOHkSoRL_QIEaBPS1V1zLrni6KIn3mvs152psto3e4h6n7LIk7kZ_feOYbk-ordHusFZCIY6kQLtEPlMfukKnThH-zeZZV5YF0eySDyxyPAzegR8igz6EOoIt3VGHEu4rHYrR4LPu8s14jChf_2FCOWmd0fJ-mmtf6ZVbtaFOYEe73w8igCeV4b0kx76H_YK_HoBtHa7xR7u6DTbe0wQFJC5ds6d1LZXt_L-mgd1Vf3cbFZ70l6K79OO1aO54H848FrzmHjp4AUT3_WZKIqwHutNwIvPTGtRhEl_mX4RD_AQD-rjj-oMZxvq5qckNNyDDCSp4U9QBUg77ZJJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edfc958cd.mp4?token=TArTnOHkSoRL_QIEaBPS1V1zLrni6KIn3mvs152psto3e4h6n7LIk7kZ_feOYbk-ordHusFZCIY6kQLtEPlMfukKnThH-zeZZV5YF0eySDyxyPAzegR8igz6EOoIt3VGHEu4rHYrR4LPu8s14jChf_2FCOWmd0fJ-mmtf6ZVbtaFOYEe73w8igCeV4b0kx76H_YK_HoBtHa7xR7u6DTbe0wQFJC5ds6d1LZXt_L-mgd1Vf3cbFZ70l6K79OO1aO54H848FrzmHjp4AUT3_WZKIqwHutNwIvPTGtRhEl_mX4RD_AQD-rjj-oMZxvq5qckNNyDDCSp4U9QBUg77ZJJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: رژیم کوبا سال‌هاست که در تلاش برای بی‌ثبات کردن منطقه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/136629" target="_blank">📅 13:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136628">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سخنگوی دولت عراق: الزیدی فردا پنجشنبه به ایران سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136628" target="_blank">📅 13:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136627">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
روبیو : چین صراحتاً با هرگونه محدودیت در حمل‌ونقل دریایی از طریق آبراه‌های بین‌المللی مخالفه؛ این موضع چین اهمیت زیادی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136627" target="_blank">📅 13:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136626">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
روبیو : حوثی‌ها، حزب‌الله، شبه‌نظامیان عراق و حماس
🔴
این‌ها گروه‌هایی هستن که ایران پولش رو صرف حمایت ازشون می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136626" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
