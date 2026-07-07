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
<img src="https://cdn4.telesco.pe/file/osdWt1GLC7NyW_x5VFgBwooyo6rUnF4bJBGE1lSt8yaqkk6BKtJolol1lI9i1kG7WeTmX8XWljmYa-KpL3jSyaNLhhuh5CmDIFMJwOHf-gD_A2r0ZprT7MEiRCGtX6KVubnCivqRF4xpLOI0nFBtVVu5F7_1NYAf36t1E14Xed-7-uyyTD9CLVtFjwHYMnOMgU3vqi3nPutrGcxPpcoKAffnIzn2Lu93C_kyJiu6ro5bNQm6J0n1rCF9guBQOQrHYE1XHxWJI4UdMCnm2jLnP8-X2b_vEORvuaVG06XtwoOPWdYW10UAXRf923PCYBK6M-EftC36TwPbqKerLh7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 23:52:11</div>
<hr>

<div class="tg-post" id="msg-16689">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش ها از فعالیت گسترده ارتباطات رادیویی نظامی در سراسر خلیج فارس و تنگه هرمز.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/withyashar/16689" target="_blank">📅 23:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16688">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رضایی:  دوستانی که مخالف مذاکره هستند صبر کنند؛ خود آمریکایی‌ها این مذاکرات را ازبین می‌برند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/withyashar/16688" target="_blank">📅 23:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16687">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرصت ۱۰ روزه آمریکا به مشتریان نفتی ایران
در مجوز جدید وزارت خزانه‌داری آمریکا به طرف‌ها اجازه داده ظرف حداکثر ۱۰ روز به تمامی‌معاملاتی که قبلا فروش تحویل و فروش نفت خام، محصولات پتروشیمی‌و فراورده‌های نفتی با منشا ایرانی را مجاز می‌کرد پایان دهند.
در مجوز جدید همچنین تأکید شده است که ایالات متحده آمریکا از امروز (۷ ژوئیه ۲۰۲۶) هیچ‌گونه معامله جدید از جمله خرید یا بارگیری نفت خام، محصولات پتروشیمی‌ یا فرآورده‌های نفتی با منشا ایرانی را مجاز نمی‌شمارد
@withyashar</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/16687" target="_blank">📅 23:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16686">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیروی هوایی اسرائیل برای مشارکت برای حمله به ایران اعلام آمادگی کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/withyashar/16686" target="_blank">📅 23:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16685">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75ced6192.mp4?token=QYemZObaQLy-ySS67wP3LgDIE8I5O4WDTbxuwWi2U4aElTo3DIVq4U7jOLLkOxAHWP5ntOHyI7EioaoZ7iRMvxP3-WzMQw_2TNEqoo8FJ5CmxHx2BmBn1V_ERxsaxB57WKOtkhW0FugZntwssJQgzCKg57_ZC7ZYVj9oeC84M6uSZpJTxwhMW83WYheLYCFRk8An_WKI8pXyp9ZA9emLkHX7GIbzPOxMT-79ZGwQ3FJtKQpLVGsuZA0NjcgZbBD2g2OF32Te3IWqnAQ_iV1nKs-WnIXMnbDE6dpuKOtyMyqI2DdG8gsJ6rdmURF0qCiYSNYjyl6stI4BbuRHsvgxrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75ced6192.mp4?token=QYemZObaQLy-ySS67wP3LgDIE8I5O4WDTbxuwWi2U4aElTo3DIVq4U7jOLLkOxAHWP5ntOHyI7EioaoZ7iRMvxP3-WzMQw_2TNEqoo8FJ5CmxHx2BmBn1V_ERxsaxB57WKOtkhW0FugZntwssJQgzCKg57_ZC7ZYVj9oeC84M6uSZpJTxwhMW83WYheLYCFRk8An_WKI8pXyp9ZA9emLkHX7GIbzPOxMT-79ZGwQ3FJtKQpLVGsuZA0NjcgZbBD2g2OF32Te3IWqnAQ_iV1nKs-WnIXMnbDE6dpuKOtyMyqI2DdG8gsJ6rdmURF0qCiYSNYjyl6stI4BbuRHsvgxrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی: آمریکا به دنبال عبور دادن ناوهای خودش از تنگه هرمز است
آمریکا در عمل زیر تفاهم می‌زند.
@withyashar</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/withyashar/16685" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16684">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دستگاه های اخلال گر GPS در سراسر خلیج فارس و تنگه هرمز فعال شدند  حتی تا کیش‌ کاملا در سیگنال قرمز فرورفته
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/withyashar/16684" target="_blank">📅 23:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16683">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری آکسیوس : آمریکا امشب در جواب نقض تفاهم نامه توسط ایران و حمله به کشتی های باری،حمله ی گسترده ای انجام میده.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/16683" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16682">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بعد از ۳۷ سال و دو ماه از آخرین سفر خارجی علی خامنه‌ای که در تاریخ ۱۹ اردیبهشت ۱۳۶۸ (۹ مه ۱۹۸۹ میلادی) به کشور چین انجام شد، در زمانی که وی در دوران ریاست‌جمهوری خود بود… و همان طور که نشان دادم با پرواز بوینگ ۷۷۷ ماهان در همین لحظه لشش از ایران خارج شد و…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/16682" target="_blank">📅 22:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16681">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4d715020.mp4?token=MzeBzCp9FoTNwq6TevzPRTH4_ghOWSWpC9iLWG7tHBpfkT0S4duF2otiXdYMKofVfUaU9Jh1RsBjGiiUweU7UsD45ZuZq89JeggjbSBln9Qv8NvtWw1NPEGmgvxVxSA3yQXmurnHasGbnqsjcQw-wJEeGd3G30K6ZxPhFWw6F0v-uitB4087orqsnWKn8mllph_RjqfvtLmXiGQiWnApIsaY_HmIFqAvJp1TIfK9G9lUjuGfMaIDEpsGQhm54AX27XRffAeRZZReXqp6vOZpcVgNbMqJNvtjLDj58YemzLP6GUd1QWzd2wCd8D2edXyJCjIJ8PwkQ0Y18aTtmKAwkwRRS3p-aFq383egHhEVgupQL7tPKurjikIUI29OdLU-RcW0EYmSkgvBM5bd9koIeiAu9LQ5Hdxj1v_NDwoHNSlbgvBnK8vts8mxU9G59sCAj5NUliKU2xMJfPXZ9vqNDVwTcsLeipgUifCLFUg-X4t_B4eRa08TUjDOQXyosk8ZKnBXd-gP1SGa9w--RhHWPmOYK-k73QInts1oHA_aWTdIirSLhEaRC4F3NjxhIn-SlWbCDH4jvaVudsLicsxnf6MZ06YYd3UfhigzLRjVkI7ud06X3eY9TzYtJJFht5EbgncMv0lArQ4_HlQG6icR85h56M3T7VId_iRSokmRwRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4d715020.mp4?token=MzeBzCp9FoTNwq6TevzPRTH4_ghOWSWpC9iLWG7tHBpfkT0S4duF2otiXdYMKofVfUaU9Jh1RsBjGiiUweU7UsD45ZuZq89JeggjbSBln9Qv8NvtWw1NPEGmgvxVxSA3yQXmurnHasGbnqsjcQw-wJEeGd3G30K6ZxPhFWw6F0v-uitB4087orqsnWKn8mllph_RjqfvtLmXiGQiWnApIsaY_HmIFqAvJp1TIfK9G9lUjuGfMaIDEpsGQhm54AX27XRffAeRZZReXqp6vOZpcVgNbMqJNvtjLDj58YemzLP6GUd1QWzd2wCd8D2edXyJCjIJ8PwkQ0Y18aTtmKAwkwRRS3p-aFq383egHhEVgupQL7tPKurjikIUI29OdLU-RcW0EYmSkgvBM5bd9koIeiAu9LQ5Hdxj1v_NDwoHNSlbgvBnK8vts8mxU9G59sCAj5NUliKU2xMJfPXZ9vqNDVwTcsLeipgUifCLFUg-X4t_B4eRa08TUjDOQXyosk8ZKnBXd-gP1SGa9w--RhHWPmOYK-k73QInts1oHA_aWTdIirSLhEaRC4F3NjxhIn-SlWbCDH4jvaVudsLicsxnf6MZ06YYd3UfhigzLRjVkI7ud06X3eY9TzYtJJFht5EbgncMv0lArQ4_HlQG6icR85h56M3T7VId_iRSokmRwRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۳۷ سال و دو ماه از آخرین سفر خارجی علی خامنه‌ای که در تاریخ ۱۹ اردیبهشت ۱۳۶۸ (۹ مه ۱۹۸۹ میلادی) به کشور چین انجام شد، در زمانی که وی در دوران ریاست‌جمهوری خود بود… و همان طور که نشان دادم با پرواز بوینگ ۷۷۷ ماهان در همین لحظه لشش از ایران خارج شد و به نجف رسید
@withyashar</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/16681" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16680">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری وای نت وابسته به ناتنیاهو از قول
یک مقام رسمی آمریکایی: آمریکا مجوز فروش نفت ایران را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/16680" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16679">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/16679" target="_blank">📅 22:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16678">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رسانه های عبری : به تازگی، شناورهای نیروی دریایی ترکیه به تمرینات نیروی دریایی اسرائیل در دریای مدیترانه نزدیک شده بودند، مانع از پیشرفت آن شدند و به گزارش‌ها، تلاش کردند نیروها را به سمت درگیری سوق دهند.
بر اساس گزارش "اسرائیل الیوم"، با دستور فرماندهی، شناورهای اسرائیلی مسیر خود را تغییر دادند و از رویارویی مستقیم با نیروی دریایی ترکیه اجتناب کردند.
@withyashar</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/16678" target="_blank">📅 22:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16677">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022cfc7780.mp4?token=Ndn1rWW46GVeSSOR5d1340Y41QIwWqSWpMjw2I_BW_jovkqp_wokNXayHNCMwXS-5izeSelIBGfPbhh6T-iLep0YmitBnr7razqKvbrnk-e_WiGPQMEf5aREFqNuLUPjtACJjflglzwzHONoWt6q8fCLA7DlCqiC5aW711hDjhUoXhxcqYputeHKtHxi9W3efi5G76BAHZTXNCosIym_tO87Atjnk3A7XdTScawg5qqDyKQbFwUyuWVvR3Iej9JbTCn5DbjRNuccfdZUTFU9Gw3e5gEdp1ayPHBpKdCxDltNe-y87uDybrvaTDHP9INYcJt4w0bkqu70pFbWdeAqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022cfc7780.mp4?token=Ndn1rWW46GVeSSOR5d1340Y41QIwWqSWpMjw2I_BW_jovkqp_wokNXayHNCMwXS-5izeSelIBGfPbhh6T-iLep0YmitBnr7razqKvbrnk-e_WiGPQMEf5aREFqNuLUPjtACJjflglzwzHONoWt6q8fCLA7DlCqiC5aW711hDjhUoXhxcqYputeHKtHxi9W3efi5G76BAHZTXNCosIym_tO87Atjnk3A7XdTScawg5qqDyKQbFwUyuWVvR3Iej9JbTCn5DbjRNuccfdZUTFU9Gw3e5gEdp1ayPHBpKdCxDltNe-y87uDybrvaTDHP9INYcJt4w0bkqu70pFbWdeAqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین
تصویر از خودروی
ن
ع
ش
کش که فردا قرار است در عراق تابوت خامنه ای را حمل کند
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/16677" target="_blank">📅 22:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16676">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">طبق گزارش ها یک نفتکش بزرگ دیگر  نیز مورد اصابت موشک در تنگه هرمز قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/16676" target="_blank">📅 22:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16675">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قطر معاون سفیر ایران را احضار کرد
دولت قطر در پی حمله به یک نفتکش قطری در تنگه هرمز، معاون سفیر ایران در دوحه را احضار کرد.
بر اساس این گزارش، قطر از تهران خواسته است فوراً به تمامی اقداماتی که امنیت منطقه و آزادی کشتیرانی را تهدید می‌کند، پایان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/16675" target="_blank">📅 22:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16674">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/16674" target="_blank">📅 22:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16673">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">داریم به این لحظه نزدیک میشیم. گفتم از الان داشته باشین، سیو کنین، چون اون موقع ممکنه اینترنتتون قطع باشه و نفهمین چی شده.
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/16673" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16672">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آرژانتین ۳-۲ زد جلو</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/16672" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16671">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کامبک سنگین آرژانتیتثن ۲-۲</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/16671" target="_blank">📅 21:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16670">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصر دوباره گل زد ( این دیگه درسته ) ۲ بر هیچ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/16670" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16669">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک مسئول ترکیه‌ای به شبکه الجزیره گفت: رئیس‌جمهور ترکیه، اردوغان و ترامپ، مسائل مربوط به إيران را مورد بحث قرار دادند و بر لزوم یافتن یک راه حل قابل قبول برای جنگ و باز شدن تنگه هرمز تاکید کردند.
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/16669" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16668">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/16668" target="_blank">📅 21:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16667">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مصر گل دوم رو هم زد</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/16667" target="_blank">📅 20:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16666">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/16666" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16665">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو درباره ایران: توافقی بشه چه نشه  من هیچ‌وقت اجازه نمی‌دم ایران به سلاح هسته‌ای برسه، این دقیقاً همون موضع ترامپه
نتانیاهو : اردوغان فقط مشکلش با اسرائیل نیست , حتی یونان (که عضو ناتوه) رو هم تهدید کرده به نابودی
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/16665" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16664">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو به سی‌ان‌ان: به رئیس جمهور ترامپ توضیح دادم که فروش جنگنده‌های اف ۳۵ به ترکیه توازن قوا در خاورمیانه را برهم می‌زند.
ترکیه جاه‌طلبی‌های متجاوزانه‌ای دارد و نیرویی حامی صلح و ثبات نیست.
اگر ترکیه هواپیماهای اف ۳۵ را دریافت کند، اقدامات متخاصمانه‌ای صورت خواهد گرفت
نتانیاهو : هنوز خیلی زود است در مورد آینده ایران صحبت کنم.
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/16664" target="_blank">📅 20:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16663">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv81Dnl8cWvqGZzZPGBS60zl2HNX2Z3dQh8HToE5LikyYaAebAlXI5eqhyRu_xFrFA2eWlhWXBxdacHpdpA5wA69lBitf-As_lqjT_VF1iKf-RrS0KFQd9qs18Q8dz9AldFYIB2DHyh0EgtXJlmWAph9kBKc1nLnqMevF26WV3_p7u9xQjNDvAOLJL7SYJQQiwn8LdkzXbUWre-jyiGcdRCih2wQ5AQ7i3DNNboK8tW3gwx2oWfwN2cSp5kGc2fXIotrc6QFOydm_IGpK1KjgseY9MLPWRql5PZVtwq93unCMkyS_ySohanCq69zmpNkDAgamNPY9_xAteP0sd0BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : هواپیمای بوینگ ۷۷۷ ماهان حامل جنازه خامنه ای تا دقایقی دیگر وارد نجف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/16663" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16662">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hcip43WDUljTPrqaIlt1t8cC5dz9xiMJR-UOJKb2ZSpy4_sq87_FyQZYA_AH4I_xoCsgz3bbAN96Olf-JHmphS1lbZ1ArbUKg4itOQfyfzL_gzqxXJ4YchB7psXjpaMl0e1xawAbgT8_GoGTaWG_3oQrMPklbZo0mN67d559E2IuQjDdSD3XCSZeLNqy4W8oCS5Tfnx-dg5xfvb-xPGa0LZByCPLOZZajXV_NGG0kPvdIPYi_R64ya-_nwwzbcuUi5FrbIWDY2EH_E1SxEHYzI0ATDQW1dcAo4dDbblg4HdOOIzdBJNYCrS6mYxeu0CsqxvaYQR6HlgjmedmSP5tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گروه تندرو ناشناس برگه‌ای روی ماشین و خانه قائم پناه، معاون پزشکیان چسبوندن و به حذف فیزیکی تهدید کردن
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/16662" target="_blank">📅 20:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16661">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مصر‌ ۱ هیچ جلو هست مسی هم همین الان پنالتی رو خراب کرد ! شخمی‌ترین جام جهانی تاریخه !</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/16661" target="_blank">📅 19:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16660">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بلومبرگ:ایران به سازمان بین‌المللی دریانوردی اطلاع داده است که بر تنگه هرمز تسلط دارد.
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/16660" target="_blank">📅 19:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16659">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مقام ارشد آمریکایی:ایران با شلیک موشک ها به سمت تنگه هرمز،یادداشت تفاهم نامه با آمریکا را نقض کرده است. @withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/16659" target="_blank">📅 19:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16658">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مقام ارشد آمریکایی:ایران با شلیک موشک ها به سمت تنگه هرمز،یادداشت تفاهم نامه با آمریکا را نقض کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/16658" target="_blank">📅 19:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16657">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ecd9127e.mp4?token=LU_ZUJJU-29oDej8uoegnaC_Yrn07PgHm3NQJub9qOzEMqhqu9_so6tO43qVBxx4czxTgDK97jCu_aGpOVDtAOjDWNSkJKXZLhKRKhmnvN10uJvXbQLKKyViL3gsFgQAu9-fYli8XippnLOvX_MT0s_himJGqfsM8cu0j50vbmesEsNym370AGr9_PpLHruGTCDNU4nbjjf957HcNrMfyi3EkKb6PoZEgtGfn4jkr-F5o0lmH-n1hp4jNQd4V5rZNh3ra-lIXQ9g6kvHObKwXSDIb7namalfYbzqAex-jeNKlLKEbfrUnmIXUL0H4zThijYFs4Zu1rgzLLnvaI2nzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ecd9127e.mp4?token=LU_ZUJJU-29oDej8uoegnaC_Yrn07PgHm3NQJub9qOzEMqhqu9_so6tO43qVBxx4czxTgDK97jCu_aGpOVDtAOjDWNSkJKXZLhKRKhmnvN10uJvXbQLKKyViL3gsFgQAu9-fYli8XippnLOvX_MT0s_himJGqfsM8cu0j50vbmesEsNym370AGr9_PpLHruGTCDNU4nbjjf957HcNrMfyi3EkKb6PoZEgtGfn4jkr-F5o0lmH-n1hp4jNQd4V5rZNh3ra-lIXQ9g6kvHObKwXSDIb7namalfYbzqAex-jeNKlLKEbfrUnmIXUL0H4zThijYFs4Zu1rgzLLnvaI2nzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکل زبون وا کرد
😩
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/16657" target="_blank">📅 19:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16655">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b528ebf23a.mp4?token=ksnFPAuyXHnoRgyk0mjU3FKqG8WSbB8Oi4LwkG_Hzceq5pBo373NupCL_YTTZH2Jwt_qb0N2tDpGdsfmYfFmYWPY4gPvM0xFNiPcUZ6uORwBPYLtX2GTTr1X4Utveh48qIzzhpVIhptEKz-dOrVtvNsFpWk0rnaxf974KCAick07RfKWpzCbfmXUCCRrBZFGmCe1Mn0oh584jSQ9pjA2Q5EAJAdvnZxbsl-1Vu0XKgPUf3lX_lp5WQrZKdbHuxZtYV_xAYTvSnWR7frN5I_W3vYh_ntBOWUr3Wn41K2pgXMAFOLJUat_tfEgpwkD49FnWgSHm-4CX9Xg-BhL7EO3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b528ebf23a.mp4?token=ksnFPAuyXHnoRgyk0mjU3FKqG8WSbB8Oi4LwkG_Hzceq5pBo373NupCL_YTTZH2Jwt_qb0N2tDpGdsfmYfFmYWPY4gPvM0xFNiPcUZ6uORwBPYLtX2GTTr1X4Utveh48qIzzhpVIhptEKz-dOrVtvNsFpWk0rnaxf974KCAick07RfKWpzCbfmXUCCRrBZFGmCe1Mn0oh584jSQ9pjA2Q5EAJAdvnZxbsl-1Vu0XKgPUf3lX_lp5WQrZKdbHuxZtYV_xAYTvSnWR7frN5I_W3vYh_ntBOWUr3Wn41K2pgXMAFOLJUat_tfEgpwkD49FnWgSHm-4CX9Xg-BhL7EO3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جایزه موش طلایی سیرک هم به این تاپاله میرسه
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/16655" target="_blank">📅 19:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16654">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شبکه ان‌بی‌سی به نقل از یک مسئول آمریکایی: ایران شب گذشته دو کشتی را با دو موشک که مسافتی کوتاه را با سرعت بالا طی کردند، مورد حمله قرار داد.
@withyashar
اتاق جنگ با یاشار : دو تا هم  الان زد ، پس امشب دکل سیریک و برای بار ۴۸ ام میزنند
🤒
🚨
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/16654" target="_blank">📅 19:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16653">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl-2ZtBDHaVPPZJDMrB-F9rINXPNFY0EgQ3X_3VIC3aln78inpYtCB-_5iJcMOuYRThfwFWM8-lfu1qMyIuoZM78tSKnWTuNFRLa6GksLbuaMKOgHVQ8hPErhaxXxV4sL7X04D0NHlAmQXG5x-gUmR30O01nXWhlS69Njxp-A7sfrAu8CLnTb5DoBSkrsxMrOswm3oU_uFl0xO3Ky6NbaIs4QxiHkOhQdBy8cGv8z-YeWauor067IBsAyHDcrHhrUDIapXGmBxod-3KZBY-ASkO5ESsZwUGa7Vs6zX_Tn0hFEb80Bq9L9sKHvvVHWQlbDkVGQraOO2qdgpRhZzQ9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اینم یکی از کشتیایی که دیشب بهش حمله شده، به وضوح نشتی سوختش مشخصه، قبلا خیلی گفتم ۳پا میخواد بخش جنوبی هرمز(مسیر عمان) رو باطل کنه و به طبع تمام ترافیک رو بکشه بخش شمالی برای ایران، اینجوری نبض هرمز هم دستشه
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/16653" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16652">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk2Gu3R9KGfh8rO9qFTBYQHLoPDfi-qFoV8OMu5GugNEjyZsGOENb9I2KZh5kBLA6SoWvgxEP5okXzQuQ2vo3-Xor0-EKhlfXNiBHE3PEYZPgcZ2LbadQPdDfE32em-oPjzUCcDkISMW5CRbVxJ416-eGJvVg2c4haI4To9doUYjjEaHxefINHR1gzDWVxniuRwL6Qw7bPytjkCfUqnjnWSiZ8vieD2Tg0KOQ8ip4d-hAyVgV6GgvslWkIPXHj81Kd2R6e5kntYsNYoFfrB2TszZhxmWIXCdjzG2xEFNleghJ4sPt25ibDcA3DPCAny8rM9kbv9Y0LilRgS5rzkmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله دیگر به یک نفتکش در تنگه
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از اصابت یک پهپاد ناشناس به یک نفتکش خبر داد.
این نفتکش هدف حمله یک پهپاد با هویت نامشخص قرار گرفته که منجر به ایجاد خسارات  در بدنه کشتی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/16652" target="_blank">📅 17:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16651">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک مقام ناتو به الجزیره گفت: رهبران این ائتلاف، در نشست خود که فردا چهارشنبه برگزار می‌شود، به موضوع تنگه هرمز و آزادی کشتیرانی خواهند پرداخت.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/16651" target="_blank">📅 17:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16650">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گروه فرانسوی "مهاجرین" که از جولانی حمایت می‌کند، مسئولیت انفجارات در نزدیکی کاروان مکرون در دمشق را بر عهده گرفت
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/16650" target="_blank">📅 17:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16649">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">درگیری مرزی طالبان و ارتش پاکستان
منابع محلی در ولایت ننگرهار اعلام کردند میان نیروهای طالبان و ارتش پاکستان در نقاط مرزی شهرستان دوربابا تبادل آتش صورت گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/16649" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16648">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqqvLLdlNLXU0r-rhyruydF3Ri8e39Q7k6rp9JRbHWoxmJTfhkB8Lq-QcKKfQJMBAk_X2JKtXddUXzrwQBfa5F6CKxX8_bG81ZO94QkarLu4CLF52x84_SXjXTiYURKIhohqK-o6EaKQCSlbFPGewsvK49TP5TvL75iDPGTC7qfZrs1w-o1jzSHFI5Q1DaqLMw8WdCUcoBsF-frH9caVNJgeDze5niSUDbhw9zcIvzi-Q2yWCGSb2V4m9g9iBnLnssN4w_nKvpxMjDtONjgQXZPQCnPS0Hj6rLJPMfaNMp4Jio_mvnnq69qs6K6OnLi6rgYQ7vKEXMrMf7TmHMtTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات دریایی تجارت بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفت‌کش در حال عبور از تنگه هرمز دریافت کرده است.
این نفت‌کش مورد اصابت یک پرتابه ناشناس قرار گرفته و به نظر می‌رسد آسیب‌های ساختاری به آن وارد شده باشد.
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/16648" target="_blank">📅 17:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16647">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/16647" target="_blank">📅 17:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16646">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دبیرکل ناتو: بدون اروپا، آمریکا نمی‌توانست به ایران حمله کند
رومانی بزرگترین فرودگاه‌های تجاری خود را بست تا به هواپیما‌های آمریکایی اجازه برخاست و فرود دهد
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/16646" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16645">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: ترکیه به خاطر من درگیر جنگ با ایران نشد و نمی‌خواهد شاهد دستیابی ایران به سلاح هسته‌ای باشد
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/16645" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16644">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بدل موشتبی خامنه ای خودش دهن باز‌ کرد !
این ویدیو رو پرت کنین تو صورت عرزشی ها !
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/16644" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16643">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ به ناتو : کاری که تو ایران انجام دادیم، اصلاً به کمک هیچ‌کس احتیاج نداشت
حتی خودم هم کمکی نمی‌خواستم. البته قبل از اینکه برم، گفتن کنارمون هستن
ما هم تریلیون‌ها دلار خرج ناتو کردیم؛ برای چی
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/16643" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16642">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور، آیا قصد دارید جنگنده‌های اف-۳۵ را به ترکیه بفروشید و محدودیت‌های قانونی آن چه می‌شود؟
ترامپ: ما قرار است تصمیمی بگیریم. فکر می‌کنم خیلی‌ها - می‌توانم بگویم، خیلی از افرادی که همین جا نشسته‌اند - بگویند چرا این کار را نکنیم؟
ما رابطه بهتری با ترکیه داریم و ترکیه از بسیاری جهات بسیار وفادارتر از سایر کشورهایی بوده است که فکر می‌کنیم وفادار خواهند بود.
و مطمئناً چیزی است که ما در نظر خواهیم گرفت - بله
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/16642" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16641">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قطر: ایران مسئول حمله به نفتکش ماست
ما ایران را مسئول قانونی این تجاوز و خسارات احتمالی ناشی از آن می‌دانیم.
هدف قرار دادن نفت‌کش قطری هنگام عبور از تنگه هرمز، تجاوزی مردود به امنیت کشتیرانی است.
ما از ایران می‌خواهیم اقدامات‌هایی را که به امنیت منطقه آسیب می‌زند یا کشتیرانی را تهدید می‌کند، فوراً متوقف کند.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/16641" target="_blank">📅 16:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16640">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رویترز: نفتکش حامل گاز قطر که در تنگه هرمز هدف قرار گرفته، به دلیل آتش‌سوزی در اتاق موتور، در معرض انفجار است
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/16640" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16639">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOf3-V2lCIBsOCBUZH-jHIZ5wa-CR_gWAHcXKxiE1utrbTsl1TiBw7hqaAEIMH35WK-Qiy78K9nAq_oosX9GLZpbttZkQ6n6MdX4SLXpOBbZvnKoPK01Zv7Nt-IIbgMV_ay5mhXsrUHa3GXg5aKwJmSVRcJX0NJSeX8EVwoxS-RaD83x2rqFNVTq7Wxf5peY-_Ch72rcw_UReYkYpWic0YTpWPPS4LeohgIXbbHmBmbD2OZFJIJt__CP_eRnJOnHX06jyLmJzNALOt8J7lf1xZYVhTO5npXz8YSikLHmXG1sQNvq9gtnuIyvFUnmGEffZULAAYxiSrD63BFoOO9ozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : کارخانه تویوتا از مکزیک به ایالات متحده (تگزاس!) منتقل می‌شود. یک معامله بسیار بزرگ. تعرفه‌ها در حال اجرا هستند!
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/16639" target="_blank">📅 16:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16638">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ارتش اسرائیل و شاباک : ارتش دیروز در شمال نوار غزه به دو پایگاه تروریستی حمله کرد ابتدا، احمد یحیی ابراهیم بتش، فرمانده یک گروه نفوذی در سازمان تروریستی حماس و در یک عملیات دیگر  جنوب نوار غزه، حمواده ابودقه، فرمانده یک واحد اطلاعاتی نظامی در این سازمان را به هلاکت رساند.
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/16638" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16637">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هم اکنون از سیریک صدای دعوا در تنگه شنیده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/16637" target="_blank">📅 16:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16636">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bfc7d0dc6.mp4?token=V6TOHo6EsB8NX33aCZgJpwpgPq0oX4AmELLGcXPAEPrT4FsSELrd6lagX0ZWSv2gY7MOYAOGvPqDi3s5_IA_LP6GOpC7G5kTDFlo9C5giCm_7x3CjycTBX4F6wdc_e4Qw2nFiBOGhYv-9149i5k4-eg0pjh1VjcllMd36Q69aUtMINbPsyzO7G9I_L1ipOC4-VXsefWVzekqfqJ1l5SdEVtUFXz_TAaAunMtbXDVZwCL8i3gv5H39txGTLcWHyWg0MoACwQ4RM2B1ysiEvdhjPimerKDXPKEwGLM3BYM-YnHFgT9Y9hz_x9yMoAQNKebopqrmz4XLavbN9bizWl06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب سنگ به سوی وزیر امورخارجه ، عراقچی که با چند متر اختلاف به ماشین کنار وی میخوره
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/16636" target="_blank">📅 15:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16635">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f08747f0.mp4?token=i9lo8TUrUTxeJ7589qXVr3J7Rr6nDF2EehHIQu55-Ee1w-y8CSGDFrP8UW2arQeTkF-m-YK9WktSgljEeeL3i1J19XA1h1_mPSvvmNZYFl8Sci1BXT8flZklfau54KbJ--XC88Uzzj4N89VcYKXKrjdiETYmkicHYqUea7Ogr8MYfrNb580vg7egpj3AwAVXNYGfgY1rSXoWA1hnhKAO6c4VRyG7Pz4CQIQNmrBv-PqQDnfpe59uer3BUumsOuOTYPZHnP7FRWCR-55cUe54rIRa9sOjV2GNFAS1erSGHT5HAmm5cGYa9W7zyEOgMFy80R0yTuxp0PGpu6VgDcQa3TqRQsJ6DiVnUozoiNM0oDvyLlKgXORiu9TnF8Y_e0nF0bmuVd-1Rsh_8AFe3tCxbAYcHhUspz8qtM6YvT4UNjGi82qjc7rY9V2LwHydrMslh16qjuPgjGaHzFN5BzGIw1TD931W_-IYng5Xfif9AlfcbW79vuwZmKNqjQmFvI7ZaeAAlpJVB25lb8pPY--UWgSaOiOfblFMyHCZTdYzlRpKiKdj2XjFWDRaMmv5Rv4vJkoJLjT0VJP1Y1vkozMQGpSd4MfnGivSTs_KcoeWBrcLjTRaIxJ_mhgsUCtGpsW_X5cECNVwV-XfMtCevkiKDqqW9D4ghwF7KPEiAbqj87o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال اردوغان از ترامپ در فرودگاه آنکارا، همینطور حضور سربازان ناتو با یونیفرم جنگ جهانی دوم.
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/16635" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16634">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">علیرضا فغانی کاندید قضاوت فینال جام جهانی 2026 شد.
@withyashar
🏆
😍
💥</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/16634" target="_blank">📅 15:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16633">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedf1332c.mp4?token=Y0lJ5K3F7T9LChcfpAhwOaeedV3KCGxRGjAvtslSj5vI9cAXYBEcmWHjlDgAk4Zp_uUAbxf1N4cI21ezN6w-JA99M3BQIyBr_aEggVmGwUmWFRysWyDOkoOJSlZyOYdc7w1Og0OC6Z7I9aAcjZe6HZ1sEvoSWT5bR1uk5ccrrK6v_2g0xmH0x8IRhx_uYeqfNoK3sz7iOSBQOE2f_Bo_FB79ld0M-GYR0yiiwrrP23cDmMs__yVW28YDkZgNQmL7Vfh6NYBl6S8SVkZLASSuWDMUxiak7I6BMsKIMUup787fskyEvIbYHVLFG_5XQchGo--iJ2tbn8KRxwy_RPaREg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان در فرودگاه از ترامپ استقبال کرد
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/16633" target="_blank">📅 14:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16632">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.  اما امروز، خوشبختانه، با همه امکانات موجود،…</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/16632" target="_blank">📅 14:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16631">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a9d31515.mp4?token=VzfvcFOQsT4nN308uZ_NhZ0aLSFvucOgknHr71lDWqdflluxaRfu5SMYjjpVgmMx0bzF-KUOJsh9t7i8sOUbba2SqVBbmQ2qPEtc9Yadi3cw4S3PLZ7dOjj9irx6lgFq6rlhyFP7voOolM5kh8DtEyXYGaBg2RaasFsBkdmcB3gjNk-Q7XNEhkrw8koDR43uptX9-y8ZUjurKfn2MUvkDjSjPEb_zDhU4H5Hpdv_B_oIy6e3PIE-A87-3ErWloxprDV6jWkhwPdllba8vhVrUElZSYZ26AIEApvrnyefXWO0czt3d8KbnDPAQjAXggof0k-KJ3S-QfQKG8xISbHP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سال ۱۹۷۵، زمانی که رضاشاه به همراه همسرش به ترکیه آمد، همسر فاروق کوروتورک، رئیس‌جمهور وقت ترکیه، سرویس کامل اتاق خواب خانه شخصی خود را به کاخ چانکایا برای ایشان منتقل کرد، چون در آنجا امکانات مناسبی وجود نداشتیم.
اما امروز، خوشبختانه، با همه امکانات موجود، از تمام رؤسای کشورها به بهترین و امن‌ترین شکل ممکن پذیرایی می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/16631" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16630">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/16630" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16629">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=FhufI7rDe4KGy9jiA2i98HOZk1hjdSodt947WQACrjwKpyQPN1dxyShaHQwt98yrj-l8r8-yDKnZv2LYjCDxzDJsPYOXpVQyzKRd3sim6_sV9fRpTaYnhoIFrpjfFmaJs0K_8rPIP41Emm8wvFsz00aMQ669S5QeTsKn60U1ZPXpNgUgMY7ReAiwxJ4dhmhCB-LTZ2sBkS5XpNpUNYHthrw5DMXsxIuUtUGeFB9D7ljCkb_bV9_7-hNqxNFVEmFEO52qZKZCrVTKXPU046iWWzioxXA12gJdOXQbodSM704A9c_9blTDeiLzo9XXbA_ysikyqZVbHNpp0vDSV1UMOXgCNWNN2qNwoSFOgdPx3KdTBejUbzuPlLrttkDn0U58gCaYc9_bIugYsLfGDjq_muLrYOwOnlyfSJDT9kzZJmXoUW-h7agwiDjoPFAmpozTeV1lACAtyjx70zpWpS5kte03vO3QAeTMW2RpVhNmHoJCrMnExAMPe-79P0nyDyXS3JQ0NExg5kYF_iHWRiLF8AUhh5VUShl0fQVsGD2lyx6s5KW58t5ibk_8pVAE4ey2QXX77gl4svnIoXcq-CxkWx2B8gLgZ1Fk4uGykStz6qkrgz9k9novhkvwOh0fUKDXl7w-c1KB08JeAh3akrAq0Oxwh5yDiOD4y7GLs0BScYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3acaa8f.mp4?token=FhufI7rDe4KGy9jiA2i98HOZk1hjdSodt947WQACrjwKpyQPN1dxyShaHQwt98yrj-l8r8-yDKnZv2LYjCDxzDJsPYOXpVQyzKRd3sim6_sV9fRpTaYnhoIFrpjfFmaJs0K_8rPIP41Emm8wvFsz00aMQ669S5QeTsKn60U1ZPXpNgUgMY7ReAiwxJ4dhmhCB-LTZ2sBkS5XpNpUNYHthrw5DMXsxIuUtUGeFB9D7ljCkb_bV9_7-hNqxNFVEmFEO52qZKZCrVTKXPU046iWWzioxXA12gJdOXQbodSM704A9c_9blTDeiLzo9XXbA_ysikyqZVbHNpp0vDSV1UMOXgCNWNN2qNwoSFOgdPx3KdTBejUbzuPlLrttkDn0U58gCaYc9_bIugYsLfGDjq_muLrYOwOnlyfSJDT9kzZJmXoUW-h7agwiDjoPFAmpozTeV1lACAtyjx70zpWpS5kte03vO3QAeTMW2RpVhNmHoJCrMnExAMPe-79P0nyDyXS3JQ0NExg5kYF_iHWRiLF8AUhh5VUShl0fQVsGD2lyx6s5KW58t5ibk_8pVAE4ey2QXX77gl4svnIoXcq-CxkWx2B8gLgZ1Fk4uGykStz6qkrgz9k9novhkvwOh0fUKDXl7w-c1KB08JeAh3akrAq0Oxwh5yDiOD4y7GLs0BScYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ همکنون در آنکارا به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16629" target="_blank">📅 14:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16628">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/16628" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16627">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ7ifgJwnfVggHDzuGrwCtfTBIRHRseHYALbntKxnGDxdjfpti0YqA6ZH6gMzteZjls7haUnJ___PKyglNM3Z9kug88f1bWP21LA8O6CXifaeTA7nxK1u5bF3En6sjrETOBuGXNaQydouTaz-zxQHVJAPlybol6HJKcFAYmaEf9E67Gnsbt4Jyo8oj_dhZRTq6OjxpuZbVKq4CahdE4zlX2y58fIIyTVmKwMMMK6T6ZwWor-TJyM_e5oCZNjjk0V7lDbuvmlTTQw0YfIgXVzrsYWxyhyd6d7OnRChLl_9zoEPGskgpRqjWDziU3S3X_LHULPRFfIyleyD_oEVXAkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با هواپیمای ایرفورس وان جدید هم اکنون در حال ورود به آسمان استانبول است و حدود چهل دقیقه دیگر در فرودگاه آنکارا به زمین مینشیند.
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16627" target="_blank">📅 13:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16626">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">منابع امنیت دریایی: یک نفتکش نفت خام با پرچم عربستان سعودی در نزدیکی تنگه هرمز در نزدیکی عمان آسیب دید، پس از آنکه یک نفتکش LNG در همان منطقه مورد اصابت قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/16626" target="_blank">📅 13:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16625">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfVLnW7NAwiGyT79VHbsUTxo_iUfVUG-T19k13EW6Iz4U0eBY2aIM9n-cKOCf6cMESGRY3f7aKE_F-BQAzi7jUfzmEjwhRyQUCNNB_vr0XqezeRLefX9LXAB8i3JtwzmkKe49xL30B-NVA31p04QRPbkXd_MEs3q6qmNuZq6ROQlD1upzDkM8SzohFHxRDegENXQ4SVjLQ4R4kNiOeHsqLt38qbySIbiyQeQKrLICGvMWobUsC56pP-SqPJzBUzYN6k5S-532Fv-La5yYkdd2n_p7E0YoocEFz55aDHkJ62Z9wP6CQXq5M_RBE5izYrm0m3BBkX6pRaR6wOveOZqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا هر وقت این کامیون عجیب و ماجرای تابوتهای یخچالدار را میبینیم ، یاد فیلم «سرباز جهانی» محصول سال ۱۹۹۲ می افتم که داستان دو سرباز آمریکایی را روایت می‌کند که در جنگ ویتنام کشته می‌شوند، اما اجسادشان در قالب یک پروژه فوق‌محرمانه ارتش بازسازی شده و به سربازانی با توانایی‌های فرا انسانی تبدیل می‌شوند. این نیروها با یک کامیون بسیار پیشرفته و مجهز جابه‌جا می‌شوند که درون آن محفظه‌های سرمایشی یخی ویژه قرار دارد و سربازان هنگام نداشتن مأموریت در آن‌ها به حالت ریکاوری نگهداری می‌شوند چون گرما ضعف این پروژه بود.
امیدوارم موشتبی خامنه ای‌ رو هیچوقت نبینیم و زنده نشه
😂
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/16625" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7801177f00.mp4?token=o2Mm8k3tbLEtRW2wsM0bnQihkectOsfUhrUuC2TOjBe6QiGzlhbglgi0SYbDmX70Wc0AL_veIKqlnSQLWq_cSIZzzm61m_y_xNlaXWZ9lfa_3oiA-e8dT-OVa7wNbLQg5siqI86IQxxX8e2QSDcZGNNk4nlw7jA5gCp7y-GZkpTKO6sAI843ppuFpEmN_2-Uz4bMn108jVU0TZqIP7EJ1TTM2Y21CgNhZZXNM9a3K08RMNP__oWt8AyCkq5OkUMAK9_2Hb0R21A2I_I98UoKuPa-5-5D4pSLd4fTZsNBYrALeMP5kGqdJhnSNzyZm5ZA7I2Tpq2RTGbPTFarsAgUpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات بالاخره تپه علی الطاهر در جنوب لبنان توسط ارتش اسرائیل فتح شد
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/16623" target="_blank">📅 12:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0122a2f81d.mp4?token=NHeMmQ9Ytv5kKTYRdRQ_OLvPLNhJlfI_3lYUypLGsR0UUL-ntkklOTy5yFSdOkhL_HVt_69DheuVxJwt9cLzPxJz70EYxAt0vwueTC6t30MhZjm3Gqsfp7QtKRKAKlMwlGltsplHPV8Tw0OQFPT90FWt9CFEIowM87QZ65zNv56eGFnAigElbSkJyymGJtQQIR27Nik-HXgDvgJogeXfslhbs-uipJJ0b6TO26mMqx_S2RPuaIhN5EM0Vi6TXefRxNWQyrxZQCDaJgSrnkndVf5zCSTklxyklsVo6NspAzgwSKIbWo_av7gLKgyJL5et74PA0m9-HcFthunK5KhquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم مثل تهران دیدن جمعیت کمه
در مسیر فیلم خورش خوب نیست کامیون ضریحی جنازه ها رو از وسط راه اصلی خارج کردن و از یه مسیر فرعی بردن
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/16622" target="_blank">📅 12:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مقام ارشد آمریکایی به آکسیوس:
ایالات متحده با حملاتی علیه اهداف ایرانی،انتقام حمله به نفتکش ها در تنگه هرمز را خواهد گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16621" target="_blank">📅 12:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=A9gtdLoR6h9-sf5Am3ZTcYO9Yh6hDoyDosrIU0FtWSi25aRTy3TZ9i1XZcjX93FoMW1z9g9s8ECevP9OOeUduDiXx7-NKvDGaYvW3cztjuWfNW8hN0AuMrW7vAh7hUZz3sjSY6VQj_MsZo3EwspCv4TJLrxMxq8y8-inTz7ZhqmXw_6HHPcS3cOLaTZ_ExJQhsKv1N3NIVSpXj4O6nkPUlB3mbwgFh8PYquJYtbB_E3QQ6Ro58orTsONvwoDIm3asNBAU7RfVdM9wyz33s7cdwcPBMCPqzDdRvnQgWiufaZvZcQNzpCbL-BIdLP--7o3AFcPvc-tApUJ1qABciOKSocVYm4qna24nhP7Z7BToPwdWMadNMfphyTI08FU2LtezkgX350U2wHIIiXqyOl7H8Is-85IeudcGmJ9VkAz5KPXwQ2X1HI9i2IAGjewYBVr9erNb6ZXU-NUe8Nr4O4Dpl8aE1_gaByaXpgoP55LloAwRJimLcecNN6qU4n5Cu1tkuO0apTElBHuBEo7Bt3jjb-8Rhe7TK2KP9w7vmOYzv4bAUHfH6epbnexQtJi8zSfEo3oa3VItwSgyXLcwfmJW3sWqgQd4fQ9pPPKMS6sCfWtvKYn6Ypcr_NwrA3RLkuQMI-hesG3hr6UGpT-lygNIluNAP-fIZOsBOz4rY6CcBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7de57d9.mp4?token=A9gtdLoR6h9-sf5Am3ZTcYO9Yh6hDoyDosrIU0FtWSi25aRTy3TZ9i1XZcjX93FoMW1z9g9s8ECevP9OOeUduDiXx7-NKvDGaYvW3cztjuWfNW8hN0AuMrW7vAh7hUZz3sjSY6VQj_MsZo3EwspCv4TJLrxMxq8y8-inTz7ZhqmXw_6HHPcS3cOLaTZ_ExJQhsKv1N3NIVSpXj4O6nkPUlB3mbwgFh8PYquJYtbB_E3QQ6Ro58orTsONvwoDIm3asNBAU7RfVdM9wyz33s7cdwcPBMCPqzDdRvnQgWiufaZvZcQNzpCbL-BIdLP--7o3AFcPvc-tApUJ1qABciOKSocVYm4qna24nhP7Z7BToPwdWMadNMfphyTI08FU2LtezkgX350U2wHIIiXqyOl7H8Is-85IeudcGmJ9VkAz5KPXwQ2X1HI9i2IAGjewYBVr9erNb6ZXU-NUe8Nr4O4Dpl8aE1_gaByaXpgoP55LloAwRJimLcecNN6qU4n5Cu1tkuO0apTElBHuBEo7Bt3jjb-8Rhe7TK2KP9w7vmOYzv4bAUHfH6epbnexQtJi8zSfEo3oa3VItwSgyXLcwfmJW3sWqgQd4fQ9pPPKMS6sCfWtvKYn6Ypcr_NwrA3RLkuQMI-hesG3hr6UGpT-lygNIluNAP-fIZOsBOz4rY6CcBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه ۱۴ اسرائیل، درباره مجتبی خامنه‌ای : اون هنوز زنده‌ست
- از مخفیگاهش بیرون نمیاد و می‌ترسه، اما تو دورِ بعدی درگیری‌، یه بمب اسرائیلی به سراغش میاد
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/16620" target="_blank">📅 12:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید @withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/16619" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به ادعای رسانه ها دولت مصر با یک تصمیم سیاسی، تمام برنامه‌های سالگرد درگذشت محمدرضا شاه پهلوی شاهنشاه فقید ایران را که همه ساله در مسجد الرفاعی برگزار می‌شد لغو کرده است.
‏همچنین گزارش شد که از سوی مقام‌های مصری به وزارت خارجه این کشور ابلاغ شده اجازه ورود چهره سرشناس مخالف حکومت ایران به قاهره داده نشود.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/16618" target="_blank">📅 11:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: کنگره باید بودجه ۳۵۰ میلیارد دلاری دفاعی را تصویب کند
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16617" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شبکه الخدث عربستان سعودی گزارش می‌دهد که رئیس‌جمهور ماکرون، ربع ساعت قبل از وقوع انفجار، هتلی را که در دمشق اقامت داشت، ترک کرده است.
در سوریه‌ نیز گزارش شده است که رئیس‌جمهور احمد الشرع، دقایقی پیش از رئیس‌جمهور ماکرون در کاخ ریاست‌جمهوری در دمشق استقبال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/16616" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=BOa7WU9yOYT0O1qpUH-GM5rruzz6bNW6wxjq_FD6jBdbN-2ZfEWdOWD-SRrfssHzHrMCixWDe9J3B64lOuZ23ogs30Dn7QMELcvlvg3RS7OI2k3eYSW0qNyxOPSE3fNQdS-afje0KHBAnpczXrIWCEbNYJkvv6EeIwPyjeUXJrgdz6tVfqjJm-sDInyqqVaSDAbVu3lkLfnQiX7kgRPW27IkDjANswZs9EN2Ru1_3cx3H15FALkuEYxTipqJuWqc0oh4i2ZbwzQcuLed9IzP3fo-WaOujNY6Gl7jY-BIx1SQXuBCt_onrxuXW84zzLczM87TyRyu5xUHCt7xYY5BNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=BOa7WU9yOYT0O1qpUH-GM5rruzz6bNW6wxjq_FD6jBdbN-2ZfEWdOWD-SRrfssHzHrMCixWDe9J3B64lOuZ23ogs30Dn7QMELcvlvg3RS7OI2k3eYSW0qNyxOPSE3fNQdS-afje0KHBAnpczXrIWCEbNYJkvv6EeIwPyjeUXJrgdz6tVfqjJm-sDInyqqVaSDAbVu3lkLfnQiX7kgRPW27IkDjANswZs9EN2Ru1_3cx3H15FALkuEYxTipqJuWqc0oh4i2ZbwzQcuLed9IzP3fo-WaOujNY6Gl7jY-BIx1SQXuBCt_onrxuXW84zzLczM87TyRyu5xUHCt7xYY5BNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تصاویر ماهواره‌ای رویترز از تهران در بهترین ارزیابی حدود چند صد هزار نفر را نشان میدهد
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/16615" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=mL3_Jcp1WSLQsADGCgWPVEXmUa7UMxaKQr-r0hreWbJQZY-_Dygw2zhXcPRkj0KlC-hNTND2jFpTpTlWmpC4v8zRCgNBIT0Hu678li37i10FLE-F9ZQrVaPm5A2Mla9lEknf9cRuImTAqf8CPdS4EV-UZbmEty-JobdzHMQrdDj8m1lxfBngfN_LBXFfEHeLgBxALrqIYJwiZm7J5T8G2ocyhyx4mCTz7PTH88uol7s9-Bp8vpPU97d8wP7i06K39jsAfGYryEspwI_fXaALm2uD5VsRHX2JUEZjsCKlgYXS06hyQE-iYvmsg7D6_FCgX12eIiHEbkpNPdnjqVbrFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=mL3_Jcp1WSLQsADGCgWPVEXmUa7UMxaKQr-r0hreWbJQZY-_Dygw2zhXcPRkj0KlC-hNTND2jFpTpTlWmpC4v8zRCgNBIT0Hu678li37i10FLE-F9ZQrVaPm5A2Mla9lEknf9cRuImTAqf8CPdS4EV-UZbmEty-JobdzHMQrdDj8m1lxfBngfN_LBXFfEHeLgBxALrqIYJwiZm7J5T8G2ocyhyx4mCTz7PTH88uol7s9-Bp8vpPU97d8wP7i06K39jsAfGYryEspwI_fXaALm2uD5VsRHX2JUEZjsCKlgYXS06hyQE-iYvmsg7D6_FCgX12eIiHEbkpNPdnjqVbrFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند انفجار در دمشق، در نزدیکی هتلی که رئیس‌جمهور فرانسه، ماکرون، در آن اقامت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/16614" target="_blank">📅 11:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک منبع امنیتی ارشد لبنانی امروز به روزنامه "ال-جوماهوریه" لبنان گفت:
"ما در صحنه، هیچ اقدامی از سوی اسرائیل ندیدیم که نشان‌دهنده عقب‌نشینی از مناطق مشخص شده در توافق‌نامه باشد. برعکس، شاهد تشدید عمدی تنش‌ها هستیم."
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16613" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز به نقل از یک منبع امنیتی: انفجاری با استفاده از تعدادی مواد منفجره در نزدیکی هتلی که ماکرون در آن اقامت دارد، در دمشق رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16612" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صداوسیما : نفتکش هدف‌گرفته‌شده در تنگه هرمز پس از نادیده گرفتن هشدارهای مکرر مورد اصابت قرار گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/16611" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=maTR5hagpupdvh3f-jmE457CI_nNLRs4khGA4L85Z5Gc8GLNylzGY9hLUfd1wCGop3w0LXYvMRpl9Ko2M1tKPw3HzTXLRuhMRa4yzRiiPsMsRSdmUOhL3rfw29W9af5Cq-AEKFvTtEA9Dc_ZTtu4z-KrHeVxtjJG7DMMX-SGYQpkcEGHDrlzzVMLNcUww1aYxd_GgOGl9efUeYgqAZj8OVaRTpvv-fsueYcpgoGbzn6ycsZ_jKgPrpIeUP_ba-fqML8g_CMizGUtGAnuos9cd_NF-9Veb-6hKR43kbTUuUGQiyc_XnvLuxKosKDIoGB4P-iZyDltT45EMfECSgHEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=maTR5hagpupdvh3f-jmE457CI_nNLRs4khGA4L85Z5Gc8GLNylzGY9hLUfd1wCGop3w0LXYvMRpl9Ko2M1tKPw3HzTXLRuhMRa4yzRiiPsMsRSdmUOhL3rfw29W9af5Cq-AEKFvTtEA9Dc_ZTtu4z-KrHeVxtjJG7DMMX-SGYQpkcEGHDrlzzVMLNcUww1aYxd_GgOGl9efUeYgqAZj8OVaRTpvv-fsueYcpgoGbzn6ycsZ_jKgPrpIeUP_ba-fqML8g_CMizGUtGAnuos9cd_NF-9Veb-6hKR43kbTUuUGQiyc_XnvLuxKosKDIoGB4P-iZyDltT45EMfECSgHEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره ای از ۶ ژوئیه دیروز ، چند هزار نفر را نشان می‌دهد که در نزدیکی برج آزادی در تهران، ایران، برای مراسم تشییع، جمع شده‌اند که کاملا برخلاف ادعا های میلیونی رژیم است
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16610" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLPWhzoMioBoB4NPTr6tGreOaDagAsFQJb-zvOmssPcH8ef4lxlDfZM_sxxHPWF82ko9hjXdqdOjedUmmplJ2872i37DXRz09lVeShFrnQCxN5akCWqgIPxe9WLlfcHhunPXUJbzl2pn9nG-07C90-m6CJFCPR5-ARHDPYwCl3fXQ3_wFzrn2AuG1a0ovP0n05GCqYdWxtTEeG8bwzLfhKpTkiZF6H7I-RtnLOgst07Usx4xtUjcShSrMtt3ymoveMhIAq1OewSBfW1REl6vG09B9ql2WsrpAJdj1CZTqw4cnXUFNND-gGGhe0n0uhSpVtNMTYeILqlh1JKxjDrYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدل ایست نیوز : تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/16609" target="_blank">📅 10:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2fzw95P39VgQJQXjAM8K4LNAvREUSDFB9FsofFbw05ct3aNp31GRS6B8zGRYfORNXpZp1d4jTorztH8L1TTcthBPhBETjVZjMBobo3557Q3cSZL8CnUehY8ox1SWDL0ZH1d-objxXaBjAE-PhVTk8wMuoiOUc5V05_oJvNY3esBKzgmNra6t_dxCpDoD6yIcTNRiTjmxj_yd4xjZsUX70tgFqz8Qp1Vpv6_riwZFr7oiREg9nynOjn8nHWTzVUvGJrIuZuaPYyULqznZ_Hrg5SPuqFCruQ20791UyKcEy14Nwxg4tBBnLwl6d7oqeM4X4lQ6E7JhzIIyOa4RhObHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/16608" target="_blank">📅 10:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی به ترامپ: به امضای خود پایبند باشید
تا زمانی که تهدید‌ها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/16607" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به وب‌سایت والا گفت:
حماس هیچ قصدی برای خلع سلاح شدن، تسلیم کردن سلاح‌های خود، یا تخریب تونل‌ها ندارد.
استعفای دولت حماس یک اقدام نمادین است که با هدف نشان دادن تغییر به واشنگتن و شورای صلح انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/16606" target="_blank">📅 09:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/16605" target="_blank">📅 09:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkywbSMvQS03iTYXWZzzhwNJFSaFMiI0MrT_aDTikEp0oHX93LPvTt8Ioz2ld-By8oBKJeQUPTnxfX1zoCWC2OCsgYB91d0qYvkUrtNOrC8H3xUjsqQ9GL89mzmjvt-FPtUB3KQmsNHjM5iF1-WYIV66XBB0DWCIktFOg8CZvPe_A3L2_QtEBdqKk-DJrox_NjnBzUgzGm_ruk94QviJ9_LHNSkhjyrG--H-NIuMU4GqfQ6CyjxB20hh5ZdDXagQNbOJ2icRfTpSA4A5VOTBVVzETnxbHvdzkkr44ZRrPQVsQzBJ_aSPzy_z9t8Z8NDo77J2Sx2ckYr6kdhcZM5qMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
گفته شده نفتکش مذکور حامل گاز صادراتی قطر بوده است
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16604" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=cffJrO0IAoIfJ-menLeC_N7Bm5b30ZD12JpdvzdIVeilduZSzoecaW5rF7BAcTA4ZsmfV-WxUGk11YXfcY_m2XoqMXCIlCrOk5OpDIqqqJQR4L2Pctp0T6UpU1_Ealxqd2xOdwGxAlK1979L5rjkjcJcIfxliOygdp-u6FiFp14s55gX1iYhXi18Tk5OL3It7FTTNEbwFPT8mqp-3lpFajzd_hMm3D9sjot23-fJQU5-lGVJwyFm2HJnEU6MWRva6OTgII2ymD6aYmVS2SOT3tNA1-ZPASC4A2U5qMG1MLTlVHoEmbOHso6a_XwOWwomlvPiZ0D7lFoaDPi8mpUw4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=cffJrO0IAoIfJ-menLeC_N7Bm5b30ZD12JpdvzdIVeilduZSzoecaW5rF7BAcTA4ZsmfV-WxUGk11YXfcY_m2XoqMXCIlCrOk5OpDIqqqJQR4L2Pctp0T6UpU1_Ealxqd2xOdwGxAlK1979L5rjkjcJcIfxliOygdp-u6FiFp14s55gX1iYhXi18Tk5OL3It7FTTNEbwFPT8mqp-3lpFajzd_hMm3D9sjot23-fJQU5-lGVJwyFm2HJnEU6MWRva6OTgII2ymD6aYmVS2SOT3tNA1-ZPASC4A2U5qMG1MLTlVHoEmbOHso6a_XwOWwomlvPiZ0D7lFoaDPi8mpUw4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوایی که ما تنفس میکنیم سیاسی هستش !
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16603" target="_blank">📅 02:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=oqnCQ5LdBtxqQ7gtk01P4AbU889mwy2F0UHiphnhlbSv-IjZB-UtQ8EP0QOFPVG5zF7RfWYY5m0vNhR4RiPQrJelpS59ZzdyCcDmwpgo9uEY8Hlnylb7t602-lpic1PoCwT7zE8hMdbo5I6PC6aqKMAQIQKTt_qSQTwVEmxWhiUDDnl9ucpOWIc3xwszBnSXn_t-Zyb4V6w-7hREjBzpY9hcgtjd8kQBGWqqOfqgJXA0JGNzKhsVx6HrYOg2Gbs9yw-IP89z3mhDzVfI2VITkyW96ryLgum7OiRLSc93gLZkf3hAgyxJLVo1SrCzZmHN_9gAxTOA7DNTSrm_126r6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=oqnCQ5LdBtxqQ7gtk01P4AbU889mwy2F0UHiphnhlbSv-IjZB-UtQ8EP0QOFPVG5zF7RfWYY5m0vNhR4RiPQrJelpS59ZzdyCcDmwpgo9uEY8Hlnylb7t602-lpic1PoCwT7zE8hMdbo5I6PC6aqKMAQIQKTt_qSQTwVEmxWhiUDDnl9ucpOWIc3xwszBnSXn_t-Zyb4V6w-7hREjBzpY9hcgtjd8kQBGWqqOfqgJXA0JGNzKhsVx6HrYOg2Gbs9yw-IP89z3mhDzVfI2VITkyW96ryLgum7OiRLSc93gLZkf3hAgyxJLVo1SrCzZmHN_9gAxTOA7DNTSrm_126r6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع جنازه انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16602" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7n2HMaV6juZ03lWCCVlThHitvBFoJ0JQQMnKghPnG6N5JK2ZaHqYCwF6ErWBiARwYRY5rAHZCSuUcTCp3nnGab8i3SXL1sortL33yV89XZj4zzyujgKy5sISWA3bnpY3hbwi-4kXV94mic1_l7ekXzNtVrBkMe5LMIn0sGH6y_Gy2l2tX7kVLbbLE_ghJK8apFGxSYEJICyP58B7KkSqNc71f1SXBNUN1nJD5SQH-iFeRieGkz0uta_fHVj99b8eCSNotc7ctipHlUecICi0NeU7Lt4CIetOGRnvNv0o89lHrGl_A7bXq5NuPIgN-595Nb_IIf7BD6Tp_3H-nSypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16601" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر امور خارجه آلمان:
ایران باید تمام هزینه عملیات‌های بین‌المللی برای پاک‌سازی تنگه‌هرمز از مین‌های دریایی را پرداخت کند
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16600" target="_blank">📅 01:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c696b52038.mp4?token=MJOii75SAR-uxbhr81aAh0Hke_A_GV8fzVnbDNhKPUb4hR8gkq4dfmjAZOdENikyQBbSVKA5yRxcrFn1zQ0HbvIQsFZblBK0dRkYjwFcxvO_xdVvQra8qBh7YY3TIGCRnlbpG-i4hw8OMowb01v1XisD3ci3z5h0MS7QaEFCEeevid5cBVi2d1Pq9DrF76jL4Cg_ZzbXVoCC_TmIH11U9OxeCShUBHb-FTtBGLdATbuingmL0hj0GKUMcJharyllRIfxp1fP7knBPe0Y5cPodD4m2jkVA2EGQbmUjXPSOkRwQgWPUHnaqO7U5F03UG0U-4vu_KaS-cnxYyVUsweGZZzMAYE3D1V895l7Vqba5E9onhpqrP-t9TLzPEA0ahlGzuH3l33MKBfnayWydeIe-n0UWqucZxVWM09S054CqN3efQkw-wWuJYBom9hxcbS4rGCd_rqJ4ISuNdwHFtdE71dciRn89WHXdwOIuve_399kr6W2RRhWzWUu_pl0YmjE2onZxY3cfqZrUFOzCwp3xzSl2MyZw3kSuuwwDnvNYMd1IhQ9X1D1O1oHjSGFW9gdvws-yXTfuSixJT_dkCETmp1OcDLxJwjQoPJXnlydl64-kElYUmGhYCwgInbM_afGAxwJL8ZIlvMAIhtQ3bhTbN-e17UtF_X6bG9eY8mQXE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c696b52038.mp4?token=MJOii75SAR-uxbhr81aAh0Hke_A_GV8fzVnbDNhKPUb4hR8gkq4dfmjAZOdENikyQBbSVKA5yRxcrFn1zQ0HbvIQsFZblBK0dRkYjwFcxvO_xdVvQra8qBh7YY3TIGCRnlbpG-i4hw8OMowb01v1XisD3ci3z5h0MS7QaEFCEeevid5cBVi2d1Pq9DrF76jL4Cg_ZzbXVoCC_TmIH11U9OxeCShUBHb-FTtBGLdATbuingmL0hj0GKUMcJharyllRIfxp1fP7knBPe0Y5cPodD4m2jkVA2EGQbmUjXPSOkRwQgWPUHnaqO7U5F03UG0U-4vu_KaS-cnxYyVUsweGZZzMAYE3D1V895l7Vqba5E9onhpqrP-t9TLzPEA0ahlGzuH3l33MKBfnayWydeIe-n0UWqucZxVWM09S054CqN3efQkw-wWuJYBom9hxcbS4rGCd_rqJ4ISuNdwHFtdE71dciRn89WHXdwOIuve_399kr6W2RRhWzWUu_pl0YmjE2onZxY3cfqZrUFOzCwp3xzSl2MyZw3kSuuwwDnvNYMd1IhQ9X1D1O1oHjSGFW9gdvws-yXTfuSixJT_dkCETmp1OcDLxJwjQoPJXnlydl64-kElYUmGhYCwgInbM_afGAxwJL8ZIlvMAIhtQ3bhTbN-e17UtF_X6bG9eY8mQXE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو لوئیز نازاریو دلیما</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16599" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16598" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from~‌🇭🇦‌‌🇦🇳‌~,</strong></div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16597" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی : کیپ‌ورد آرژانتین رو حذف میکنه، من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود! @withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16596" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3CGhiFeZr9C-uoJb7cTuuowrjbohLAX3pPOnzhZtJ-UeOtfAwfK5B6pyAvtEaKOxZom-NBuZjtU7u-b7DWaUx40La3gewfhpwIFq9mJZ5wgdZM8yFDSi6OEhDMPdrImiASmFbLS6552snUCpHrysHneOtwAFerkCxmhG0eeMq8Km8A9gQKB-NmrL2AMTQw3h4t2TCmVK9nTZGZZ-xMbRkyPdvvMFv1-Y02AM4VZ5aFIgSf-fSDQsijdKCsuD8hcJJYVWT8BmCMoucrHuP6vvKlnW7fUhGJTNf1mdwZhHeLr0nZqVQVyISooQVFi0imee-_WSrBdQbz8K4nzcG1pqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ پاسدار صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@withyashar
🚨
🚨
🚨
🚨
سربازان گمنام حضرت موسی بد فرمون دادن</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16595" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آکسیوس : نتانیاهو در تماس تلفنی با ترامپ؛
- خواسته که به اردوغان «تذکر جدی بده» یا «جلوی رفتارش رو بگیره»
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16594" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است. @withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16593" target="_blank">📅 00:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">استان هایی که تاکنون سه شنبه ١۶ تیر را تعطیل اعلام کرده‌اند:
استان تهران
استان قم
استان سمنان
استان خوزستان
استان مازندران
استان اصفهان(شهرستان های آران و بیدگل و کاشان)
استان یزد
استان مرکزی
استان بوشهر
استان لرستان
استان هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/16592" target="_blank">📅 23:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیوید کیس مشاور نتانیاهو:
بمباران مراسم ؟
شوخی میکنید؟
صدها مامور موساد توی اون مراسمه!
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16590" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=tP9HcnukBYMpsfbNhTzYTrlUD_6YMusphMKLzNwTsK_l7U0NkN0E-OqAAvEdp8fS7eY25czfvErcHuP-h9q2YqZysIeW5g6NBwb3yD7_09rsMI4BUmbDBSbFtJ5s680m-UnqV8tjsS4xNwre6h6VdnFjTfHtJZm2GCz20OGhTyNpiwuCIUwvltFiMR0whx75ZYmFq56BPhviQanMaAc1SMrupeacua8AIhROxUrgK7Y9DwO9tq1RlOG6SLXQwOCuQNAnSA-KfUuoYes-Qq4gIQeI89EAEZjRVrOVZVxLThhTLqAcl0GCPa_Wzje3PUtg1YI32PWgVEiDp14W7NZFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=tP9HcnukBYMpsfbNhTzYTrlUD_6YMusphMKLzNwTsK_l7U0NkN0E-OqAAvEdp8fS7eY25czfvErcHuP-h9q2YqZysIeW5g6NBwb3yD7_09rsMI4BUmbDBSbFtJ5s680m-UnqV8tjsS4xNwre6h6VdnFjTfHtJZm2GCz20OGhTyNpiwuCIUwvltFiMR0whx75ZYmFq56BPhviQanMaAc1SMrupeacua8AIhROxUrgK7Y9DwO9tq1RlOG6SLXQwOCuQNAnSA-KfUuoYes-Qq4gIQeI89EAEZjRVrOVZVxLThhTLqAcl0GCPa_Wzje3PUtg1YI32PWgVEiDp14W7NZFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16589" target="_blank">📅 22:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم. @withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16588" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=eZ2D6Mnnnwd5wiHbnViU5gZbnT3srPBfLeh1ytePaFSCGz_GLm0YJoRzpL5HyCUdTCIPJTS9pZUSQKV6LDvV_sSee2PheYFqz4_Aj6npY9rK49toTk0ip7JkHXUl8t4qPaIPPdqmYcVaoEsW2UeUXKFbZ6usg7u76hqdHJd4yS_Cn6lISQKTcMQgfWu18-7pGRrQJJPQoEhDD-RaCrZF1zwTgoiosuHcl7jWLlABUaBiG5EmZi0wsec5xqkKEEfKmuoT19MDjJD1om6FaIAgPugdt8L0HUSACDS6Zwb94nQk5qB5VDfOsdB_EkEULbBn11cMtIl-38VkzvO89ZMfQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=eZ2D6Mnnnwd5wiHbnViU5gZbnT3srPBfLeh1ytePaFSCGz_GLm0YJoRzpL5HyCUdTCIPJTS9pZUSQKV6LDvV_sSee2PheYFqz4_Aj6npY9rK49toTk0ip7JkHXUl8t4qPaIPPdqmYcVaoEsW2UeUXKFbZ6usg7u76hqdHJd4yS_Cn6lISQKTcMQgfWu18-7pGRrQJJPQoEhDD-RaCrZF1zwTgoiosuHcl7jWLlABUaBiG5EmZi0wsec5xqkKEEfKmuoT19MDjJD1om6FaIAgPugdt8L0HUSACDS6Zwb94nQk5qB5VDfOsdB_EkEULbBn11cMtIl-38VkzvO89ZMfQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون با عینک آفتابی معروفش که ترامپ مسخرش میکنه وارد سوریه شد
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16587" target="_blank">📅 21:25 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
