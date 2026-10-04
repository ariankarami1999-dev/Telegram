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
<img src="https://cdn4.telesco.pe/file/Z5P0Rgbq6jBZCK3Y3sNxSfo0pwNkRda6IAY61ySDJd2Oomd3KaMMbvalNPD1_liIuTZYsSkk0P8zSQbwWlip0RwXSJ_3XJ5B_q0YiHVlxXhLKXstFxmptKrhIYAm9O52AWsxZmElfXXKaoMu1Ph1kWVjy2jve_n-J7Y7e5fI83ujI2a5_Y-SjXXhwg99HhJdB4Ivs4GJ88a4UabL0biuBJpvSTbFgx4ErrzY0s7LYIQhfpW8RZ8Li8ueSFu0JYeIi3484mFT5uJE7HyKhfEyMgjgV_8A3N7hxTAQl-Tv4aPrFW7YIkKIJqh7vCNC5S32YzglLZDHaDWy_xT9CRWXHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 09:36:27</div>
<hr>

<div class="tg-post" id="msg-150851">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رئیس‌جمهور الجزایر: برای هرگونه میانجی‌گری در موضوع تنگه هرمز آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/150851" target="_blank">📅 09:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150850">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کویت با صدور ۶ فرمان جداگانه، تابعیت ۴۱۵ نفر را لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/150850" target="_blank">📅 09:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150849">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل‌ شده در شوشتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/150849" target="_blank">📅 09:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150847">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پولیتیکو: ترامپ از مداخله نظامی در جنگ عربستان با یمن اجتناب کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/150847" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150846">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a30f759b.mp4?token=Bh_d0Pe2Zf9_1HGUeafEb6xXLr0L8FVM7z9PzhvKMcdM7gcWj0LfO7pAkqnbjWqtYeQoGQlb7TCNWViopohAqQA9mFMso1eiH5WMbFkSH_-ktuXP9ieiK83aYbolw4MdtOT_FA-bLvcsjlHYf3PSUKpnpxdS17RLWr31is9R0kSu3B9vWmkpcnh80psAf8lDj7KAOxTZTXJ4xXdzlMfrxPw-cZG0F_2BjxrN9Tq4h-DTwbPgIwvM9uOrdFNfJo2O6kbIbdLcPkdilznJjiLOCWzsu2guczUuZgOt6paVn6zb7r9P1VlD3i2AudD9wRv4W7KUT1dpCt0v119fhxpn4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a30f759b.mp4?token=Bh_d0Pe2Zf9_1HGUeafEb6xXLr0L8FVM7z9PzhvKMcdM7gcWj0LfO7pAkqnbjWqtYeQoGQlb7TCNWViopohAqQA9mFMso1eiH5WMbFkSH_-ktuXP9ieiK83aYbolw4MdtOT_FA-bLvcsjlHYf3PSUKpnpxdS17RLWr31is9R0kSu3B9vWmkpcnh80psAf8lDj7KAOxTZTXJ4xXdzlMfrxPw-cZG0F_2BjxrN9Tq4h-DTwbPgIwvM9uOrdFNfJo2O6kbIbdLcPkdilznJjiLOCWzsu2guczUuZgOt6paVn6zb7r9P1VlD3i2AudD9wRv4W7KUT1dpCt0v119fhxpn4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان عصر دیروز در دریاچه چیتگر و گیرکردن گردشگران در قایق ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150846" target="_blank">📅 09:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150845">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRAOGEKYmhaJOhXJGi5KF1XtmVeJUU9GhyzkhAkvkmmU9JCJWybQFgBZiDhdCyn-WplMRF_VlF5c5s_vwqGCpYQz6HGoOpjLM5Honpr-ZzBzAoJ7gT-0_wGRt4S1u7kZjRoI6iFHT9OpqzGDB8B3yys6Dnsq6YBEYJ24nJXn2mpVBBenWdWO7VN6HoSGxTTeg37V2ys_oT74hLrDP58ZkCjhYDan2xNzBzgKoOYlmbtwe0F3Xd3atN6Vkw55v1feJsOBSPcOKMKf1bB49MhxG5_zhx7_uzQ9K9DNHQGZkQRAsiFqv74a9rr4QgfElQPPRgNPz0AttcQKsBvrb0CkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نجومی و عجیب کوییک
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150845" target="_blank">📅 09:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150844">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08259e56d.mp4?token=D6bcL9_pPGhmP7ytU5AsxFLm0vkqkYKeD45qKLCzIDKCDLHHt1Wg3VyqwlySPY9qBN33ohyX_csdykffTrlz7__UJ1Cp0mD-Z6JNLcUL5DIXVzVmFml4pIr6g2_o-Jd9pJpC1c_p6ju9k6EeahQl7rzBCfExd8SOkQYdG3A3XfX9Ob7IdR04YSjEL-O9Mufrw5SU3zby29Z9XvVypte6kWXR8Tm2XC4MZJzA3Zg_1DioluIYF-1IzO4x2ryjrhZLJQWuYFZkr9LqD9Cvlqukj3mepi5jrbzIM6hx63RjzdRtZQVMqVSgb05fvb5cmYREywZolqgpq-ArDwi-_DefEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08259e56d.mp4?token=D6bcL9_pPGhmP7ytU5AsxFLm0vkqkYKeD45qKLCzIDKCDLHHt1Wg3VyqwlySPY9qBN33ohyX_csdykffTrlz7__UJ1Cp0mD-Z6JNLcUL5DIXVzVmFml4pIr6g2_o-Jd9pJpC1c_p6ju9k6EeahQl7rzBCfExd8SOkQYdG3A3XfX9Ob7IdR04YSjEL-O9Mufrw5SU3zby29Z9XvVypte6kWXR8Tm2XC4MZJzA3Zg_1DioluIYF-1IzO4x2ryjrhZLJQWuYFZkr9LqD9Cvlqukj3mepi5jrbzIM6hx63RjzdRtZQVMqVSgb05fvb5cmYREywZolqgpq-ArDwi-_DefEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض دانش‌آموزان در فرانسه به درگیری کشیده شد
🔴
اعتراض‌های دانش‌آموزی که از چند دبیرستان در منطقه پاریس آغاز شده بود، به شهرهای مختلف فرانسه گسترش یافته و با مسدود کردن مدارس، آتش‌سوزی و درگیری با پلیس همراه شده است.
🔴
وزارت کشور فرانسه اعلام کرده در جریان اعتراضات اول اکتبر،  نفر بازداشت و بیش از ۳۰۰ پلیس و ژاندارم زخمی شدند. همچنین صدها دبیرستان با تعطیلی یا اختلال در فعالیت روبه‌رو شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/150844" target="_blank">📅 08:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150843">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
الجزیره: میانجی قطری مجموعه‌ای از پیشنهادها را برای نزدیک کردن مواضع دو طرف مطرح کرده است/ تهران در حال بررسی این پیشنهادها در شورای عالی امنیت ملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/150843" target="_blank">📅 08:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3459b87732.mp4?token=m3ptSV5OdUBP8T-gt4HaG4zLwHpvpkwhVYZrxwMFvRRLYIpLv0iGSxbgKH15-XfUBEKJr8CLsTNuBVoMKYUoKLfmZ38m1M2Fhm-Ow0HFZ7NuQghGuVSj12zrpsC7w-oBU_zkuPDOZiPB0J2avJkY_V3VTcBcMmiHRVuRZ7Ybj2JlmDoWN1AfsZfSFj5I-h4WaF1RYcDeamel3u3pDXX-GEEHUkA9shqxD_w9KXyvzWw2EaOVmNhhrxeXzYkLV0hnlqGJigtTUE9GZFn6BB4dvdddd4XJ7m0RIBMwflCvIwME0LqgjkWlDaVGumDrx_xBVzw_Kw7V0kHqt5pqQ8SOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3459b87732.mp4?token=m3ptSV5OdUBP8T-gt4HaG4zLwHpvpkwhVYZrxwMFvRRLYIpLv0iGSxbgKH15-XfUBEKJr8CLsTNuBVoMKYUoKLfmZ38m1M2Fhm-Ow0HFZ7NuQghGuVSj12zrpsC7w-oBU_zkuPDOZiPB0J2avJkY_V3VTcBcMmiHRVuRZ7Ybj2JlmDoWN1AfsZfSFj5I-h4WaF1RYcDeamel3u3pDXX-GEEHUkA9shqxD_w9KXyvzWw2EaOVmNhhrxeXzYkLV0hnlqGJigtTUE9GZFn6BB4dvdddd4XJ7m0RIBMwflCvIwME0LqgjkWlDaVGumDrx_xBVzw_Kw7V0kHqt5pqQ8SOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کره شمالی: من ارتباط بسیار خوبی با کیم جونگ اون، رهبر کره شمالی، دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوب باشد.
🔴
اما این تفاوت را در نظر بگیرید: ایران هرگز موشک هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150842" target="_blank">📅 08:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد یکی دیگر از اعضای یگان‌های پرتاب موشک جنبش جهاد اسلامی فلسطین را کشته است؛ این فرد از اعضای گردان شجاعیه، وابسته به تیپ شهر غزه جهاد اسلامی، بوده است.
🔴
ارتش اسرائیل همچنین اعلام کرد فرمانده یک هسته موشک‌های ضدزره جهاد اسلامی در شهر غزه را نیز کشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/150841" target="_blank">📅 07:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXm16B1Mv04oFz2nWcMqKdhoRmgj7u-ZwFtSQiQmBmzSx_KrET79FtIdTXX9M-L8dNroly3cxWnNIHGgyXlGk7vFcpAeGcP8ivUNntuk4aVeegHtqZH8wtfW4ZeFzAX9FP7ye1FkNzvvZ9LjdobGpnRSO7EP8K8QG-NbtG04rbgebWwcSwLrJoY8RnW6YMrN51sbsNvnGVNwmLPSEdIrrtXXTTr4-1i1TZDd_2sKy07cXd-kq90qL75GIcPqrmY0CWnySVPiLR-iNMCMpbPLT-eIMeWRcgcJyXto8GlAx5luHYDhAD85Qb_CFLoUEG9_EmcNbCFR9Ha8Jg_0JdXJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیر ارتباطات کاخ سفید، روز شنبه با انتشار پیامی در اکس نوشت: «حرف منفی‌باف‌ها را باور نکنید. عملیات طرد اقتصادی در حال در هم کوبیدن رهبران ایران است، در حالی که آمریکا در حال پیروزی است.» استیون چونگ با تاکید بر اثربخشی فشارهای همه‌جانبه علیه تهران افزود: «جریان نفت از تنگه هرمز همچنان برقرار است، صادرات نفت ایران به دلیل محاصره موفق ایالات متحده به‌طور کامل متوقف شده و تورم اقتصاد ایران را فلج کرده است.» چونگ گزارش بلومبرگ مبنی بر تورم نزدیک به ۹۰ درصدی، استقرار ناو هواپیمابر و تفنگداران جدید آمریکایی در منطقه و مهار صادرات نفت خام ایران را بازنشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/150840" target="_blank">📅 07:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس ابری ProNet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVKJu4dqajY6bCYQLwUnMckNkcAenP55X3ZYG7EW5QPX3v48cv8qGwSRhVP57QAypbhRf-wLANf5w7gDeNjoJTrB8yaX14U-tf40WNinGI6AGvmui1RT5Dia_LEGK0Cg6xJk58jke1Y-2kjKIXaejUHzoctHQ_r6-UpBBNcVFzh81BSR3DZfxCOefshowOxPk45NFPSV-WoQUp33amxcZwPHk4eJcgYEr1epwUkFfUVCt4zZL-PSpdJFflOIGGVHZFOtE68-3NZmF4_Ek4GXAhz49aIsIq2kSLZBHDAYSB1r7nHGEMUwg-eHc1_8dnVCwxPnzVQiRJ1gizuTYl4hKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین فیلترشکن پرداخت به ازای مصرف ایران
🌎
پرلوکیشن‌ترین سرویس ایران
🌎
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
🔴
دسترسی 75 سرور با خرید یک اشتراک
🔵
قوی‌ترین تیم پشتیبانی 24 ساعته
🔴
مناسب برای تمامی اپراتورها
🔵
سرورهای ترافیک نیم‌بها
🔴
سرورهای ویژه زمان اختلال و محدودیت
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دریافت مستقیم اکانت تست
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
🟢
مینی اپ حرفه‌ای مدیریت اکانت‌ها
🟢
اشتراک فیلیمو فیلم‌نت رایگان
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/150839" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150838">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-ZCTVqUkzqmPK2SxX8e1-MnK5kimVgPbwebnICcTjB30-lNfuPpB_dDDxhPAhkoI0sAVkfwWOUpnUinZtgtFW2r3dv21Nig-BO8pclhng_-gInhq8vK-I0ugg2F6RixvmcMzHxlVCxVNlixCVUdi8cebyMoyke47E1e_t0jVnelfsxHcPtPPKgVAUGLRsdzClmjQfSPNVFmqhbFWmeJd9cZ4UQfWp5q4-BY5uhWqb0NMLHQ8Revx0QA3qShfXKDXoTCuvHSraj7YTdyD4gu-ckU-akZTuEDY7MIsNIHysboSkyIA4f0NZBURPLs3lLjvSRuLZOlNEOi3amPcUF9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ضرب الاجل ترامپ به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/150838" target="_blank">📅 01:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150837">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJyC-UR19e_QxkzN_0RKTGym9lVw06ioAIgITDzC7A0pS1-o-ejyYOlA-en2qiC_4FAf4BB-NYcGVe8zPRzKiYNm_Xg8EAYW5m-eOwuHpZqS0-3G4i-2GM8vZeV_nJ21-5LwDqwpO0et0V-hpSAtcStck7fCXXKLyjOhInOe545qU4vSby0BAFtQgXlTJL8OVwgvm12SKcIoR8OOrMi4S7T9RAPJjGVwBEW9VDv7PkkHKfob7AYauamq7Tgn02gms6FLhcYEblui2s5Cgi1U8aBTTeVVt9cJ51C2fbS2xUJAeWAZRzJLShPkRZX8xjz9PiI6qzEjSkJNUSQEjkeyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام‌های اماراتی تأیید کردند که کمک‌خلبان عمانی با استفاده از تبر اضطراری کابین خلبان به خلبان اصلی حمله کرده است.
🔴
این تبر در مواقع اضطراری و وقوع سانحه برای خروج از کابین خلبان استفاده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150837" target="_blank">📅 01:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/150836" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150835">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f7807e352.mp4?token=GGfXjzGu7LJoN9QgzSxdPONgCr70IKkGg8qqMxCWvWI0wZBsx8_xrKbN-5bF6LUwt66fabCvdUF72sWUhulW9buWdcKVQvS8p1UoeUw8DSx-wUXGBp5mLzZSB_ok6Qvhur-wZ8AV6nC6B5M4g2pWSnnOBqL8rQEBTyjlgexCF0x11sWEPh80Bq92Qi2AjQmgTKMQGjL67Yqc0L72O4lU0jsLu9CASU6GIvPeVm_6sLixaSPB8JDHKn0mqqfqs211LzZ4Rh2wzNw4XcdDLrU5vNomNfqQpHJRcsHtmYJLLm6slKaB76N0Y8XoLID7ZI0TbPbmBQIKnt34gTFWmo85dA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f7807e352.mp4?token=GGfXjzGu7LJoN9QgzSxdPONgCr70IKkGg8qqMxCWvWI0wZBsx8_xrKbN-5bF6LUwt66fabCvdUF72sWUhulW9buWdcKVQvS8p1UoeUw8DSx-wUXGBp5mLzZSB_ok6Qvhur-wZ8AV6nC6B5M4g2pWSnnOBqL8rQEBTyjlgexCF0x11sWEPh80Bq92Qi2AjQmgTKMQGjL67Yqc0L72O4lU0jsLu9CASU6GIvPeVm_6sLixaSPB8JDHKn0mqqfqs211LzZ4Rh2wzNw4XcdDLrU5vNomNfqQpHJRcsHtmYJLLm6slKaB76N0Y8XoLID7ZI0TbPbmBQIKnt34gTFWmo85dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید کیز، مشاور سابق نتانیاهو گفته بود جمهوری اسلامی، ۲ هفته و ۳ روز و ۶ ساعت و ۱۴ دقیقه دیگه سقوط می‌کنه!
🔴
الان این تایمی که داده بود تموم شد و جمهوری اسلامی سقوط نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/150835" target="_blank">📅 01:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKLDvLYOLJJ0HOBBmA4FIIdZkk9XIQVELzcOOBFrEHMHSoMSR_Czug4tuhMjH2Lv6IArDYPp8DF5eRuvOtH-BEhm46HtAHc1M56ohDAZ8sl7-35aOZ958xsfYD1UX5FR-LRarSMFrH3_uThsW4FFEP7Vo2LQT6INLwplqIEg8OfwSeLpzGfxXt4rNyDX7GR4_dJNOsQmU-qCCSTiVKNiojBYwaLHWHKrBEVZMKbFKpbaiAyVZGpwWAOcaIDCCLMwOGyjLLeGQyuQXEscqYBMsSED8ow4gVPuzMyfPSOq2-vsKKzhk4F4MInZFctssxaPdtkjslfD38CiAo5F9TUG-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار کلاهبرداری
‼️
🔴
دوستان تبلیغاتی که پایین کانال نمایش داده میشه و غالبا کریپتو و سیگنال هستن، تماما کلاهبردارن و تحت هیچ عنوان توجه نکنید
🔴
این تبلیغات در پایین کانال توسط تلگرام منتشر میشه و از دست ما خارج هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/150834" target="_blank">📅 00:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSYPQ_Q6NgCYyhaWoBfNKlpIjElW7zhOaoRKpf23a0xiDF8srIcq1tyHehXNoQHMRx_0aEo1W5s8PjRLP4q4Mvjhr7f9760kgMeplbwjbDRkbgPOM7lZSx8tQyZr9bEw5ClQvE5W2B6RmjFh7PlPspV9gKs0T0S_wiJb4P3re63VDI3FVhLmyRkDQRgQIijsJpkxV9y1JS09soWH3PoWuLA2wf0Wlt5k5fErsklEI2scI48rvMj5V_0hcgZVTkzO3BtIOy7Oi5YoAsvlv9xox071ev38YNuycfe_zA2_3K21BGkOoAOAFoyI8g47h7TYI7Eq_CtRc2Cez8FXaRKAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های اسرائیل: مجدد به آسمان تهران خواهیم آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/150833" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150832">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: ایران بسیاری از برنامه های تسلیحات هسته ای خود را رها کرده است و من درباره آنها تصمیم خواهم گرفت‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150832" target="_blank">📅 00:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: ایران بسیاری از برنامه های تسلیحات هسته ای خود را رها کرده است و من درباره آنها تصمیم خواهم گرفت‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150831" target="_blank">📅 00:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYXjDXRK5o3p53AJS0XtLFpMn2iwtXrEFvq6Pn7luXXnzWLYGBSFpqIInKkCn8WJXh8IDRnLUOQOyfZ0iCRIBq4VfA_eYmcZlWXKBCN17WNr-P6Goj8MYx03mCSk-8DjiArQRaVlj_6ZTRe9JKgMWiCahkGddVybYOJZ24sOzjHpGK-ZmuLEHX41nXIwws7Ow4gbt2CruyniwKKfLtMFSMCViqyAthFAnCLyrxyTuxfTXsbANPFvCU3IR1x81Ze8VEjpte2s0ujQ55bUjo3Sas6XXJaEozF_AswXrp8Qveb-B7h16vF9ZKcUzpuA4fBPEGfnYvli21UDs28B4Iv1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین: کمک در راه است
🔴
روسیه اعلام کرد آماده میانجی گری بین ایران و آمریکا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/150830" target="_blank">📅 00:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKovJvpN6xMlHWwxNaICw4Cc_6VBThzJ48biB2xKpDqD2NobC7RURpuYDRmFrhaiwtMpJFxm9cVftaPVXidShTbAGhgJwmFpOI7B1edqTwcQqiO8VZsYo6ORdfYRI3uh9HOlYQ8MY0SbfgQSl2d9JVg-S18w-D2IoAXLrsjh2AqwVAh-AzRognFzOga2Cp5Jb9PjoIFKtuSUc48ipIG8K0Pw8aM6RCEM3c-LE9-63hwg1bLfJQjnVQiflfGVNCtcDNmZ6UFQvOzfZz7qmzv739DLAHZEkUCKz-2VrIeichfiFjFM6n9zmwEQEOBI8XO-THSzTpiJaRSTQ0z4xEd-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هر کد ملی، یک فرصت چرخش!
گردونه صراف رو بچرخون؛ ببین جایزه‌ت طلاست، دلاره یا یه هدیه دیگه
👀
شانس‌تو امتحان کن
👇
https://r.saraf.app/s/agrd348</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/150829" target="_blank">📅 00:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150828">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qGUpDtVy95UwI2CEw-o0J1qiyUNC230z5WIolQWMaHz42NYabvoiRwh6teyLP1XO1LbXR-yDGmwgsFp_yAYTkRVBgxO8JpkpCGQapbZnOeTxEfaz2j5OPJH2kSPRLTvD8mF1Mzyi7iiJtV0vrcrjU4vMm4yEDdDjkqqvgO2tM_w1A3By82UkXdHpsok1W2t-TACDtoKjrqm8oYFYVy9uHHTiFKaFR0gsNaKBtf9JqT-JNd4GkjcAQMGeJncyOHO_BzQI2Lu9o1CP7OPpLKRWzKZ1tyuUurazeBrUJrm3AOZrSEV8biw-EVUYIqa-6NipdgiyrgHP6c0XijqDxogzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میلی گلد طلای هنگفت این هموطن رو بالاکشیده و تسویه نکرده!
👈
صدای این جوون مظلوم باشیم و نذاریم حقش پایمال بشه.
💔
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/150828" target="_blank">📅 00:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150827">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7ef4f1f2.mp4?token=Tpuyd8ePBuNFmgk-6-7VaEktPmYNviqihnFUZDHzmyrvAczutnZB52I7hpQKhu-7COThVo5HvqB3zi4a9rxjNF_tduBuhKkLIusxIRyfD7LjO7IQE-A6noFn_Yl8CLD4xUXT38uloAzgLLFQcrkZMmKf8eLR0J7nJojmrGgVI-UwOjiy4aEpIvst5H3r3btAfRGW76wWCk0UJ2YPJUyHFjgzSNHUl7GzaFXLXOedFxkJRb5NBAuMFuS-nc4tSB076_4KnVNK_pht2bmO17Mc6Q6Rf5-sIN3jcHdYZRFJgzUgLGXyPBaUKtmJEhvpvvn1V7bU0wiGFk5SGclrNZLdfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7ef4f1f2.mp4?token=Tpuyd8ePBuNFmgk-6-7VaEktPmYNviqihnFUZDHzmyrvAczutnZB52I7hpQKhu-7COThVo5HvqB3zi4a9rxjNF_tduBuhKkLIusxIRyfD7LjO7IQE-A6noFn_Yl8CLD4xUXT38uloAzgLLFQcrkZMmKf8eLR0J7nJojmrGgVI-UwOjiy4aEpIvst5H3r3btAfRGW76wWCk0UJ2YPJUyHFjgzSNHUl7GzaFXLXOedFxkJRb5NBAuMFuS-nc4tSB076_4KnVNK_pht2bmO17Mc6Q6Rf5-sIN3jcHdYZRFJgzUgLGXyPBaUKtmJEhvpvvn1V7bU0wiGFk5SGclrNZLdfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر مشهدی به خاطر فیلم گرفتن از مزاحمت خیابانی احضار شد
🔴
چند سال پیش یه دختر تو مشهد با یه دوربین مخفی نشون داد چه مزاحمت‌هایی تو خیابون داره. جالب اینجاست که دادسرا به جای مزاحم‌ها، خود دختر رو احضار کرد که چرا این فیلم رو ساخته و پخش کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/150827" target="_blank">📅 00:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
هگست گفته هر فرصتی بود برای مذاکرات دادیم!حالا باید تکليف جنگ رو مشخص کنیم.
🔴
ایران تو این هفته بارها سمت کشتی ها تو هرمز موشک زده.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150826" target="_blank">📅 00:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ویدیویی از سیل امروز عظیمیه کرج
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/150825" target="_blank">📅 00:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پزشکیان: رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/150824" target="_blank">📅 23:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150823">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">😐
پزشکیان:
آمریکا تو جنگ اقتصادی شکست خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/150823" target="_blank">📅 23:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150822">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پزشکیان: رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150822" target="_blank">📅 23:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150821">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7hztO8DgsxagkaROEJ-vN-qBhZyjiRw73FRbpKQHVn6hhdD_KpYOgTfGfXByDTd59Bep75lmlqtj0_z5OS5JchlHtggDRQD44K0i44-Kq-vGP_QAYfMWZU9PkYfBvhN9D4mr8Y1BZ9Pn4mWJXOVaVS_XbgUfNuZV9VtSBHussr9l7EFVB6Ps9rDe9n18UGCGl4NpYi3yr9pml62DNoOynYoOU9ypVEH0D77aEoUfvNWAKXmpXyqRNoU3dCHGZBNhryrNCrT0TNZWf4XxKpq3S9J5ww0ERrLLJLJaxeFZockZ9FXlMZ-TD9LnQdzqu9V1Cj_wOj2yMzdKpQwegYhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت‌های نظامی آمریکا در نزدیکی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150821" target="_blank">📅 23:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150820">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرگزاری فرانسه (AFP): نیروهای آتش‌نشانی در تلاش هستند آتش‌سوزی در یکی از تأسیسات شرکت آرامکو در ریاض را مهار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/150820" target="_blank">📅 23:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150819">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b362cc0206.mp4?token=KVHN2sPO_rDY0X1yYvQnBnuMaObl3zCxwE5wzXMo-uh8qsMifSkBQVq_kqTGNE7llF1NW8IUr_Bpwqjmu1KduyrWdTODdTcReWCydQ6lY61nvv_ezNUEcaKjiOLwjC3oZ976MqMQ_0MlJA1itejV6_M_oMHWNUBuMq81UDDCR_Rx9hyIRfALjaaYNYnA8Uu4NYzBcWKSLIpw3xRl_jL-7SlFKgXdg20iuo25RiEl7sj5g7s4Y818Yby262DGpTP-_tevk0W3L-9CVvdRBOfgP_NhI4Ijb4XaugGB_riltjoDtGzEhpDYjDBhq3i-yCwrYARVdu3Vh61FM732GkHhqjviOc4iq0KXWdXpomV9O0SsiJwaYB4hIvwM6R8dKF5YUGA1mj8xf0vGGqd6NwVxwGX7ATCU3UTMxCjVdbm_fEMhF85clH9hwUvEwDS3gqB-r5_cbGyK8c6SxVSVLCen2IC39_bCynz6Ayq5liyDMgpzlasCgpOwZOynb4pKdHclJKRs3qAvP5dGw-SIWsAz7mTOcdrP9WDAamjqlIuZ3Z1AoDwrhkoW6mt2DHgjO-Xdoik5aCxr1Dqaw3zW4G5C_r0g605Ed7X-s7X33mQ5barrfTKiKT9qVGVeNZOmMFIOOWN6Y7Y1_bz89pqOftC_mu1cUdmIrjA3OxWs337Cdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b362cc0206.mp4?token=KVHN2sPO_rDY0X1yYvQnBnuMaObl3zCxwE5wzXMo-uh8qsMifSkBQVq_kqTGNE7llF1NW8IUr_Bpwqjmu1KduyrWdTODdTcReWCydQ6lY61nvv_ezNUEcaKjiOLwjC3oZ976MqMQ_0MlJA1itejV6_M_oMHWNUBuMq81UDDCR_Rx9hyIRfALjaaYNYnA8Uu4NYzBcWKSLIpw3xRl_jL-7SlFKgXdg20iuo25RiEl7sj5g7s4Y818Yby262DGpTP-_tevk0W3L-9CVvdRBOfgP_NhI4Ijb4XaugGB_riltjoDtGzEhpDYjDBhq3i-yCwrYARVdu3Vh61FM732GkHhqjviOc4iq0KXWdXpomV9O0SsiJwaYB4hIvwM6R8dKF5YUGA1mj8xf0vGGqd6NwVxwGX7ATCU3UTMxCjVdbm_fEMhF85clH9hwUvEwDS3gqB-r5_cbGyK8c6SxVSVLCen2IC39_bCynz6Ayq5liyDMgpzlasCgpOwZOynb4pKdHclJKRs3qAvP5dGw-SIWsAz7mTOcdrP9WDAamjqlIuZ3Z1AoDwrhkoW6mt2DHgjO-Xdoik5aCxr1Dqaw3zW4G5C_r0g605Ed7X-s7X33mQ5barrfTKiKT9qVGVeNZOmMFIOOWN6Y7Y1_bz89pqOftC_mu1cUdmIrjA3OxWs337Cdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: چین دیگه بهمون تصاویر ماهواره‌ای نمیده و بهمون گفته اول برید مشکلتون با آمریکا رو حل کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/150819" target="_blank">📅 23:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150818">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyZgqGPL_NTdP9sOVvBUPzTQPGMh0A47xokJ3GGx2pcx3NwC9ivgPJndYzOBzGKDdA5TmDmBM3xgF8dRQFks7EJ4VDHkeUzn060X_JTFxnLxhazbbOjfHyyTDSiviJN65FMHhEEluw15Hknm6pzVeEKketU3lv3EAXhGJJzfqCh8LOAsRmVSIfVTlWmo6qxRzQh8uiUs3XGJuvFnXBwKrsPyOHD-CvG30fQOaGBEt9uNbhLkW2WQg15nJMFeql_1lxIRlOJgSLyMSAdC_mHwCTHnp87zYsXwXVbPMSZyGlGSbHVZ0FqCbKRXX6k4BlS8gidyGMflc0u87IBe_mHXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروازها در فرودگاه ریاض به طور همزمان با فعال‌سازی سامانه‌های پدافند هوایی متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/150818" target="_blank">📅 23:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">پول و خانواده،هنوز هم حرف اول رو تو کنکور میزنه!
●
سارینا واحدی ، رتبه 4 تجربی
شغل پدر : متخصص پاتولوژی
شغل مادر : دندانپزشک
مدرسه : تیزهوشان
●
اوستا نوشیروان‌پور ، رتبه 10 ریاضی
شغل پدر : پزشک
شغل مادر : داروساز
مدرسه : تیزهوشان
●
اشکان کریمی ، رتبه 1 ریاضی
شغل پدر : پزشک
شغل مادر : پزشک
مدرسه : تیزهوشان
●
آرش محمدی، رتبه 1 تجربی
شغل پدر: دامپزشک
تحصیلات مادر: لیسانس روانشناسی
مدرسه : تیزهوشان
●
پوریا زارعی، رتبه 3 انسانی
شغل پدر: استاد دانشگاه
شغل مادر: دبیر فیزیک
مدرسه: شاهد ولیعصر
●
امیرافراز دهقانی تفتی، رتبه 7 ریاضی
شغل پدر: پزشک عمومی
شغل مادر: کارمند بانک
مدرسه : تیزهوشان
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/150817" target="_blank">📅 23:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150815">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مدودوف، معاون شورای امنیت روسیه: آمادگی داریم میانجی پایان جنگ بین ایران و آمریکا باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/150815" target="_blank">📅 23:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150813">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:چند تن از دیپلمات‌های ایرانی از ایالات متحده اخراج شدند، زیرا از دستور ترک کشور خودداری کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/150813" target="_blank">📅 23:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150812">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhtWTwkIgqwW_o9y7K4A0kVJIU0UIWVaoa0rpQlDlxJR2wzb7BVYYEDcY75WSZNXIBbPlxflZtRfc61IakBz_LvSXKjEQuZQyZYzctFXWsofPY1p5GoeKSo9CLnrgyvgVJ97o436wVrazdRMjL0__CD3hNeTos396seVlstHtMxyXLwOqd0zhCQ8XYeg6UstbGQ4ZZaYZaBreCxXMJeY9GxQQFdedUkbQPuIPhDiN5jdefiIlCmFJ_DR-hExNUP-tD1YwY6Z2GAXe9DukjTdn64bBk0yxVqPwpT4B_A0-YBTqyav62PBOaFzSf8eIotNCOs5rpXogxd9SXBJcN4sEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: اهداف دشمن تو جنگ اقتصادی محقق نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/150812" target="_blank">📅 23:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150811">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
از وقتی مجتبی خامنه‌ای رهبر شده دلار 100 هزار تومن افزایش پیدا کرده.
🔴
دلار 17 اسفند 1404: 166 هزار تومن
🔴
دلار 11 مهر 1405: 266 هزار تومن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/150811" target="_blank">📅 22:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150810">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
یحیی سریع: تأسیسات آرامکو در ریاض را با پهپاد و موشک هدف گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/150810" target="_blank">📅 22:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150809">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb1679cd5.mp4?token=Eh04pdDKkqJ7DnIAgMepv0_wTr2LslM-lSjPk8k7-FD7KFca-mhI2YdCOwUBia1fBRj1W5sVsXYgpicHjeW63muWLxHka4oaK5HJM5EbRRzNDQwm93aCqXN2B6F0NYxiG-GpXgjDabE_aMy8aG1t0bZDnNM5MxTbRn5y5V9E8yeMVcGXYnLNQEG364YuAnykm36Gbh-u-1WLVhjUj-_JeFhBAmwjc2dIeUUV2b8gyLui5ycdfSftgALEh58iw824NSzivPaQnQtMSQBZsIBmq3KIgn7hiOagrpTIEuCIlvGsdFekbeoy5Z-CxCroezvGeDOhf2TT91wj-Hcc_eXpzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb1679cd5.mp4?token=Eh04pdDKkqJ7DnIAgMepv0_wTr2LslM-lSjPk8k7-FD7KFca-mhI2YdCOwUBia1fBRj1W5sVsXYgpicHjeW63muWLxHka4oaK5HJM5EbRRzNDQwm93aCqXN2B6F0NYxiG-GpXgjDabE_aMy8aG1t0bZDnNM5MxTbRn5y5V9E8yeMVcGXYnLNQEG364YuAnykm36Gbh-u-1WLVhjUj-_JeFhBAmwjc2dIeUUV2b8gyLui5ycdfSftgALEh58iw824NSzivPaQnQtMSQBZsIBmq3KIgn7hiOagrpTIEuCIlvGsdFekbeoy5Z-CxCroezvGeDOhf2TT91wj-Hcc_eXpzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: ترامپ همه فرصت‌های مذاکره را در اختیار ایران گذاشته است
🔴
پیت هگست، وزیر دفاع آمریکا، در پاسخ به پرسشی درباره امکان دستیابی به راه‌حل نظامی در جنگ با ایران گفت این بحران «می‌تواند به شیوه‌های مختلفی حل‌وفصل شود».
🔴
هگست مدعی شد دونالد ترامپ «تمام فرصت‌های ممکن» را برای دستیابی به توافق از طریق مذاکره در اختیار ایران قرار داده است و در عین حال به توان نظامی آمریکا و شدت حملات این کشور اشاره کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/150809" target="_blank">📅 22:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150808">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا، درباره ایران: «پیام بسیار ساده است: ایران هرگز، هرگز و هرگز سلاح هسته‌ای نخواهد داشت.
🔴
رئیس‌جمهور ترامپ مصمم است اطمینان حاصل کند که ایران به سلاح هسته‌ای دست پیدا نکند؛ و چنین چیزی اتفاق نخواهد افتاد.
🔴
اگر آنها بخواهند این موضوع را جدی نگیرند و تصور کنند که او منظورش را جدی نمی‌گوید، این به ضرر خودشان خواهد بود.
🔴
اکنون زمان تصمیم‌گیری ایران است تا آن‌طور که باید، این موضوع را کنار بگذارد؛ بدون آنکه اهرم فشاری در اختیار داشته باشد. در غیر این صورت، ممکن است این مسئله به روش سخت‌تری حل‌وفصل شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/150808" target="_blank">📅 22:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150807">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا، درباره ایران و تنگه هرمز: «وقتی ایران نیروی دریایی ندارد، قایق‌های تندرو ندارد و نیروی هوایی هم ندارد، کنترل تنگه هرمز برایش بسیار دشوار است.
🔴
ما آسیب بسیار سنگینی به توانایی ایران برای رصد و شناسایی تنگه هرمز وارد کرده‌ایم.
🔴
ما در هر دو بُعد نامتقارن و متعارف، تنگه هرمز را تحت کنترل و تسلط خود داریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/150807" target="_blank">📅 22:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150806">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا، درباره ایران: «ما می‌توانیم محاصره را تا هر زمانی که لازم باشد ادامه دهیم. باور کنید، در صورت نیاز می‌توانیم آن را متناسب با شرایط تغییر دهیم؛ می‌دانم که این خبر خوبی برای ایران نیست و گزینه‌های این کشور را محدود می‌کند.
🔴
ایران هرگز سلاح هسته‌ای نخواهد داشت و ما برای اطمینان از این موضوع، هر اقدامی را که لازم باشد انجام خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150806" target="_blank">📅 22:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150805">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5076f215b2.mp4?token=haE-Gl0D8OBkBZmCbSeOExnR9DbIP-OTjGEwzz0YdAMiZEzWWaAQwM9jIc46NMtixqXAslKWsXCzoQEhfkIqGr_mTKRZYFpuDAPb4cvoLSlYjTupu0gmGuzDrdfF7BFuV7gT59BcfjGlKq4kegXHRcuh6ojqJrEiuLmfCXxMkWvxPU9e_xmcZcOf1b93MX5UadmUsWcCDmRKk5o6-NjTm8JMiAa796XmeUDjdIIXvehUBfiEd2S9g7WS33ybB_59N43bprwIdcJVAeHWRMti_QjgfUZS4mq7Qr0c4oiIm3dcsVQuPUQNIcabx6tmKZSLitLKtHiC1Kweqe3S4AqVAKj6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5076f215b2.mp4?token=haE-Gl0D8OBkBZmCbSeOExnR9DbIP-OTjGEwzz0YdAMiZEzWWaAQwM9jIc46NMtixqXAslKWsXCzoQEhfkIqGr_mTKRZYFpuDAPb4cvoLSlYjTupu0gmGuzDrdfF7BFuV7gT59BcfjGlKq4kegXHRcuh6ojqJrEiuLmfCXxMkWvxPU9e_xmcZcOf1b93MX5UadmUsWcCDmRKk5o6-NjTm8JMiAa796XmeUDjdIIXvehUBfiEd2S9g7WS33ybB_59N43bprwIdcJVAeHWRMti_QjgfUZS4mq7Qr0c4oiIm3dcsVQuPUQNIcabx6tmKZSLitLKtHiC1Kweqe3S4AqVAKj6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا هیچ شواهدی نمی‌بینید که ایران در حال حاضر تلاش می‌کند توان موشکی و پرتابگرهای خود را بازسازی کند؟»
🔴
پیت هگست «آنها تلاش خواهند کرد توانمندی‌های خود را بازسازی کنند. آنها یک دولت تروریستی هستند، بنابراین همیشه تلاش خواهند کرد این توانمندی‌ها را بازسازی کنند.
🔴
وقتی کشوری به اندازه‌ای که آنها نابود و تضعیف شده‌اند، آسیب دیده باشد، بازسازی آن فرآیندی بسیار کند و طاقت‌فرسا خواهد بود و ما این موضوع را می‌بینیم و از آن آگاه هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/150805" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150804">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فووووری/تحلیل عجیب نوستراداموس ایرانی از جنگ
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/150804" target="_blank">📅 22:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150803">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e0be606b.mp4?token=jDhaaiozRrvqgvYKYZTko595gqRzbeNJ9AkLgDXSG4jC5oJ1-dWiUB0B9bJ8YQYU0yjzPG-DNfxvBAMI-vvK4bTn-vbkkw2KUm9nN-cNUUzR-bqVX7ftUmGM1h2FS5o_RpgHN_SPju0mbG6jYC1DJHtRiJlx6lf7mrEvAnB4yOpfqaIGfEfLphXWyqM9y05gsmyE_U8A1LKRlkMJKXwPflxXZljKrfx539Am8N0EuCpR4B7Fsp-6pbyd_GDc-Dt42BvMg74rPzuiBm9m-xIAsnai_MEl-ZIA-WC9ExQf6HVM0fRNQVCczrDoY68RncAqJpzzxkaGXgHnjYPt2Lcmvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e0be606b.mp4?token=jDhaaiozRrvqgvYKYZTko595gqRzbeNJ9AkLgDXSG4jC5oJ1-dWiUB0B9bJ8YQYU0yjzPG-DNfxvBAMI-vvK4bTn-vbkkw2KUm9nN-cNUUzR-bqVX7ftUmGM1h2FS5o_RpgHN_SPju0mbG6jYC1DJHtRiJlx6lf7mrEvAnB4yOpfqaIGfEfLphXWyqM9y05gsmyE_U8A1LKRlkMJKXwPflxXZljKrfx539Am8N0EuCpR4B7Fsp-6pbyd_GDc-Dt42BvMg74rPzuiBm9m-xIAsnai_MEl-ZIA-WC9ExQf6HVM0fRNQVCczrDoY68RncAqJpzzxkaGXgHnjYPt2Lcmvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا، درباره ایران: «ما می‌توانیم محاصره را تا هر زمانی که لازم باشد ادامه دهیم. باور کنید، در صورت نیاز می‌توانیم آن را متناسب با شرایط تغییر دهیم؛ می‌دانم که این خبر خوبی برای ایران نیست و گزینه‌های این کشور را محدود می‌کند.
🔴
ایران هرگز سلاح هسته‌ای نخواهد داشت و ما برای اطمینان از این موضوع، هر اقدامی را که لازم باشد انجام خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/150803" target="_blank">📅 22:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150802">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c9b1a92e.mp4?token=iAVKGaqZA3JjCR9dt66wq1Bj3GL6vYamsXAD3ZgaXBm58lvzDDbcOLBPlAPRmhdYW_2e-gHeHQP5SPWhnzU_5TWRL4NlcKe6APuvIfnPbJLOC_DpQaNY9rVjwbkwRdcgLcj_PFvDyVkvs58PlPfzEiL8Wl8-Z-vkOoui_dfZ55kAvvxxHs1sD2NjOwRNVchuqQPOtISMMvaIf1ofcUWzafLr1SC2jTy5gFwXcZuaH-X-Sqs46INRecquo3PmnzozWlyqvevYlQAIw0qQbTUHdzlW44We68aKSlrdbOrmEADSk-sZX1QMbaAdm6h6MbNuGTDuiPzBc080OugkoVhFKlwZ_k_cHvGFMgSgx6Zu7yoQl44Tsx3WSvTbBTB-eOs1ozFCdXSj57tfr6Nf86qsVy1lPkO4yPHB92MFb1QKBIl2etfLbMXctXEtUzHxEje5NwhPeMpOd8eJi5iXuLWi-BghfxxANs5U4fZYpRv4_f__wvf6Nkt--vqmi64T8_LPfQxCY7Nslzw52D0X0PWT1i1tOm5GAhZbzaDDDnGpxl3GPzNYYoToORRs1YgLHc8ICCf7ke7GOzBXTqCeSyj7A6FKN4A0AIX4nbgMaArA91k3xRFL7dYqGMGyWEbKE2Hs4Ekvd2G9LdbCUvOBz700YHmdADzwKnc7yCsgi838TJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c9b1a92e.mp4?token=iAVKGaqZA3JjCR9dt66wq1Bj3GL6vYamsXAD3ZgaXBm58lvzDDbcOLBPlAPRmhdYW_2e-gHeHQP5SPWhnzU_5TWRL4NlcKe6APuvIfnPbJLOC_DpQaNY9rVjwbkwRdcgLcj_PFvDyVkvs58PlPfzEiL8Wl8-Z-vkOoui_dfZ55kAvvxxHs1sD2NjOwRNVchuqQPOtISMMvaIf1ofcUWzafLr1SC2jTy5gFwXcZuaH-X-Sqs46INRecquo3PmnzozWlyqvevYlQAIw0qQbTUHdzlW44We68aKSlrdbOrmEADSk-sZX1QMbaAdm6h6MbNuGTDuiPzBc080OugkoVhFKlwZ_k_cHvGFMgSgx6Zu7yoQl44Tsx3WSvTbBTB-eOs1ozFCdXSj57tfr6Nf86qsVy1lPkO4yPHB92MFb1QKBIl2etfLbMXctXEtUzHxEje5NwhPeMpOd8eJi5iXuLWi-BghfxxANs5U4fZYpRv4_f__wvf6Nkt--vqmi64T8_LPfQxCY7Nslzw52D0X0PWT1i1tOm5GAhZbzaDDDnGpxl3GPzNYYoToORRs1YgLHc8ICCf7ke7GOzBXTqCeSyj7A6FKN4A0AIX4nbgMaArA91k3xRFL7dYqGMGyWEbKE2Hs4Ekvd2G9LdbCUvOBz700YHmdADzwKnc7yCsgi838TJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا شما معتقدید که جنگ ایران می‌تواند راه‌حل نظامی داشته باشد؟
🔴
پیت هگست: خوب، می‌توان آن را به چندین روش حل کرد. رئیس‌جمهور ترامپ به ایران هر فرصتی داده است که آن را پشت میز مذاکره انجام دهد.
🔴
اما از نظر نظامی، ما بارها و بارها تشریح کرده‌ایم که حملات ما چقدر ویرانگر بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150802" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150801">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3782fef625.mp4?token=sXedFJj2w0AfEdzXjiVRgg9nmSJ3V92obIKRmvRU8dXen226Iwgaic3hlUDgpagn2Z3HOiOC8SLtLucKAXV6r9YiBaO8_C9gP3Rh4UmaF2Jj-rBwX2bmW2LmNNk5Q6Hkqp47TSqJa08nsPf_l8Ypm5lfx8UmdzOSvT6rAkw43zc8lVopqwqMWfh539JCkelV7wZSMKbXXVSYc5-ouZd3sBSrFyEdJQmwAExugsXFtest0_kDIr0Cm6OkLexLNQkWcKpOe6fjFLKp8iiT9roNdlxSnapBnbeGmG4tXPLC0aTnSQ6lduEjD_3ToVddHO4m-9b3w7IHqWCX3njbHvrunw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3782fef625.mp4?token=sXedFJj2w0AfEdzXjiVRgg9nmSJ3V92obIKRmvRU8dXen226Iwgaic3hlUDgpagn2Z3HOiOC8SLtLucKAXV6r9YiBaO8_C9gP3Rh4UmaF2Jj-rBwX2bmW2LmNNk5Q6Hkqp47TSqJa08nsPf_l8Ypm5lfx8UmdzOSvT6rAkw43zc8lVopqwqMWfh539JCkelV7wZSMKbXXVSYc5-ouZd3sBSrFyEdJQmwAExugsXFtest0_kDIr0Cm6OkLexLNQkWcKpOe6fjFLKp8iiT9roNdlxSnapBnbeGmG4tXPLC0aTnSQ6lduEjD_3ToVddHO4m-9b3w7IHqWCX3njbHvrunw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا «یواس‌اس تئودور روزولت» جایگزین یکی از آن دو ناو هواپیمابر می‌شود، یا قرار است سه ناو هواپیمابر در منطقه سنتکام مستقر شوند؟
🔴
پیت هگست: سؤال بجایی است، اما هرگز به آن پاسخ نمی‌دهم. رئیس‌جمهور ترامپ گزینه‌هایی خواهد داشت؛ بگذارید این‌طور بگوییم، و من در همین‌جا رهایش می‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/150801" target="_blank">📅 22:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150800">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوووری /  اکونومیست: نشانه‌های نظامی از احتمال آغاز حملات در ۷۲ ساعت آینده حکایت دارد!
🔴
اکونومیست با اشاره به داده‌های ردیابی پروازها از تجمع کم‌سابقه هواپیماهای سوخت‌رسان در پایگاه العدید و اعزام هواپیماها و یگان‌های جستجو و نجات رزمی به شرق منطقه خبر داده است.
🔴
بر اساس این گزارش، هواپیماهای شنود و جنگ الکترونیک آمریکا نیز فعالیت گسترده‌ای در منطقه دارند.
🔴
تحلیلگران نظامی مورد استناد این گزارش، این آرایش نیروها را نشانهٔ آمادگی برای آغاز احتمالی حملات در آیندهٔ نزدیک ارزیابی کرده‌اند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150800" target="_blank">📅 22:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150799">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: شرایط کنونی از دشوارترین مقاطع کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/150799" target="_blank">📅 22:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150798">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=NKlkNsSDEcsXaxW3A3632nOwqHoC0kZBxn3huTOJAojoD0Q8ojBHM0EtAaZ0VrrxGp_zTBEmiH6XbKKfOEq6Z9_EZZF8C0npUXHqm1Bc9vkxbMJYboYTcUhP-Wn894Ftxy43h68rSoCCgB4kw8g_e6qAHcobwoyrjbOYWwLLv4FkSNwgmgtfUo-o2nM1gmWJwAS4lOjY6XSjeIg7hTfpPj6hKp1kWLa14KaRO6BPKlEJneZcu3ocMUlRlrsR4WFdgG85tT2Lp7ST1iutN_oMsMjbW5GGbeSbOM1pgHGy_mAY9YgdWFHmXnFqz1xM7f6iqs7TGJ3Ns-QG5W559XmQew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=NKlkNsSDEcsXaxW3A3632nOwqHoC0kZBxn3huTOJAojoD0Q8ojBHM0EtAaZ0VrrxGp_zTBEmiH6XbKKfOEq6Z9_EZZF8C0npUXHqm1Bc9vkxbMJYboYTcUhP-Wn894Ftxy43h68rSoCCgB4kw8g_e6qAHcobwoyrjbOYWwLLv4FkSNwgmgtfUo-o2nM1gmWJwAS4lOjY6XSjeIg7hTfpPj6hKp1kWLa14KaRO6BPKlEJneZcu3ocMUlRlrsR4WFdgG85tT2Lp7ST1iutN_oMsMjbW5GGbeSbOM1pgHGy_mAY9YgdWFHmXnFqz1xM7f6iqs7TGJ3Ns-QG5W559XmQew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظۀ اصابت صاعقه به برج میلاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/150798" target="_blank">📅 22:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150797">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d87e3e7c.mp4?token=Q71MzatinEVhAY3AVD-D78gFTsmgRmY2yjwGdE7COEbnmjGxxLzG6WC1ih06xSUbpQozt4yCQ82Ui0Z1lNzx-ABgtKTPOdB2LY-r9AvQ2rMc3P1qJuFzxgiy7WsztXaHxpJsFx4wZvU2xGhBXajBgoYM5jyoOyi4NQIY_efEBEbH4iHhzzt-Pz5r1vQEKrVldzgh_c7qXuwn7Pf3DF00CRXQvymXesp1NT0kFmra3Tj8U8xDDPXn9eqUQSJFaSdxkTQQIdof6fYDJDYaLBEGYCHmotzH85qJCiOuDhVFWsLGdcQQo7bdxlislvK_If82JmnaW-7OZuf-K4hIIyd06Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d87e3e7c.mp4?token=Q71MzatinEVhAY3AVD-D78gFTsmgRmY2yjwGdE7COEbnmjGxxLzG6WC1ih06xSUbpQozt4yCQ82Ui0Z1lNzx-ABgtKTPOdB2LY-r9AvQ2rMc3P1qJuFzxgiy7WsztXaHxpJsFx4wZvU2xGhBXajBgoYM5jyoOyi4NQIY_efEBEbH4iHhzzt-Pz5r1vQEKrVldzgh_c7qXuwn7Pf3DF00CRXQvymXesp1NT0kFmra3Tj8U8xDDPXn9eqUQSJFaSdxkTQQIdof6fYDJDYaLBEGYCHmotzH85qJCiOuDhVFWsLGdcQQo7bdxlislvK_If82JmnaW-7OZuf-K4hIIyd06Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آبگرفتگی شدید کمربندی لواسان هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/150797" target="_blank">📅 22:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150796">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCXyyDcgOYiHi-VUiF1-MhK5V5Tm3ktYscej1m3JXQKsCcFHBC1A8XI5obl0bkHiJBjuMZJDDG7MhHKcCfYNKt8Yf2xD2YLkwlE6GjuDxHUPmKLfxp_B2fWtEGNIcjvYK0zheaRBhpZ4u8rDDTvoA5Hw4etQmIHuMrm5qaS0chUcZL_qoFrTEaYqYX1mI8cnMekZ8UALOykjDFUCBrlV4do2hxVUrBpaZTmSwS54rYMu5vUG-DygewH1nHnlHXdVf6141XI35yyZurBDJcPOxVkOR4JT1t3xG0IkEQnQP4VGgM5sq2nNbJnnBWAlfugOYkYknEpDizeQor1138A-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ۲۴ ساعت گذشته، ۱۲۲ فروند هواپیمای نظامی در این منطقه شناسایی شده‌اند. از این تعداد، ۱۰ فروند هواپیمای ترابری بودند که از خارج وارد شده‌اند، که شامل ۶ فروند آمریکایی، ۳ فروند فرانسوی و یک فروند نامشخص است. همچنین، ۳۰ فروند هواپیمای ترابری نظامی منطقه‌ای، ۴۲ فروند هواپیمای سوخت‌رسان و ۱۰ فروند هواپیمای جاسوسی نیز مشاهده شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/150796" target="_blank">📅 21:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150795">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
برگزاری تظاهرات در استانبول ترکیه در اعتراض به ممنوعیت حجاب در مدارس جمهوری آذربایجان و روابط نزدیک الهام علی اف با اسرائیل
🔴
معترضان علی اف را خائن خوانده و خواستار برکناری او شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/150795" target="_blank">📅 21:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SwspjVaniL-BCEtgs1CWEAtv90A-GjoOA8JVCFx92Ein0-kYP06oZjE7xncr_RueJBYJqi8Jnt1WVr397Dytbdn-W2pfthn02Wnk8BJjHL_aZIGaUm3BCDPDhvJWDfLDvNizti5Lsp6C_cmPVCjsv8oaigPy6gnkfZbNaXYCq5eH4Y5h6zDKdMAsBcGM_L7meMT7jxwtWHfJj4vof5a4Xna_xlyPz5dWx_ngcd4Asah1olf8KR-4INx-IeHhtIKoJ8Tc-LO4XZIHBObqp0CIDpWAvrNJvh2T1X8sLMlg1QtgREI_oT0W_Gkv8TkcWJ0_iL6jyCo3huCPEKtvtZ_vGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/150794" target="_blank">📅 21:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
حوثی‌ها هشدار فوری‌ای به شهروندان و ساکنان عربستان دادند و از آن‌ها خواستند از نقاط کلیدی شهر دور بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/150793" target="_blank">📅 21:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyamBzgJRc4sDKr6DqVWoC-FiAjxBJ5vNYUoWpjSGD3_TpggsvxQzxuPBSye1EHnrSyS9dS5qjkuq-riHmWaPAD-CnM4VOCzmENoite4yjHSMXzXYEs2n_0nBHR9NIdW3d7c4_bZPamYWrcgP5S9GiWoZVWL1OQNjD_TcpGSy_mZXXU6m5Pk6GbQKEGJqFsavWF9bUlUyC4VlUEDrfcsPiwgR2GiM-pg_jRp-e-W9Zpc3nx2O9GPAJXCIhcMxEHjG0pfXhqY3nDo_nyODjhVRSqyAomsIyQS7CY2YwJm3whtzq1EgkXfbb1jO7U-6oz0gu3UvbrS4KuEBcRfCJ5P2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن‌پست: ارتش آمریکا در حال آماده‌سازی برای افزایش گسترده حضور نظامی در خاورمیانه است. طبق این گزارش، در صورت اجرای این طرح، نزدیک به ۲۰ هزار نیروی نظامی، تا ۱۵۰ جنگنده و چندین ناوشکن مجهز به موشک وارد منطقه می‌شن
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/150792" target="_blank">📅 21:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
محسن رضایی: معادلات نبرد رو موشک ها و تاکتیک های ما مشخص میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/150791" target="_blank">📅 21:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
تلگراف: خاورمیانه در آستانه دور جدید درگیری نظامی گسترده است.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/150790" target="_blank">📅 21:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edaa986fe9.mp4?token=A9qXvZuPoGxbZeFGIoPcNwIDbncldSNAMp3tPW__4i0aLfJT-F9cf7KvgLh0q4ULs5XOjvuv2jk-9Ww11f37dx-B77HBytPcf9Ytgo_2m66wQXy9WvKZOFJ_ifl-VtzQOXNIDs7VcpffSj9R5FHduTmVxcx69HgIw4kwswR8eHaSFWp5WZbNNgJ-bxNo8B5ggRysuacvIMWs5_S08vTrTuFc7nxS3R1CZxFGkInC2bWqKAXD-vJHJw-fjmNlJiXLBpPcETy0_PZ9RdhiAEbO-e5zC5IXj6GbOufeVNtwfq1ETS4uxJm6bLP0TxE4v9NeDM2NAs8xB9SbGj7AO-AxiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edaa986fe9.mp4?token=A9qXvZuPoGxbZeFGIoPcNwIDbncldSNAMp3tPW__4i0aLfJT-F9cf7KvgLh0q4ULs5XOjvuv2jk-9Ww11f37dx-B77HBytPcf9Ytgo_2m66wQXy9WvKZOFJ_ifl-VtzQOXNIDs7VcpffSj9R5FHduTmVxcx69HgIw4kwswR8eHaSFWp5WZbNNgJ-bxNo8B5ggRysuacvIMWs5_S08vTrTuFc7nxS3R1CZxFGkInC2bWqKAXD-vJHJw-fjmNlJiXLBpPcETy0_PZ9RdhiAEbO-e5zC5IXj6GbOufeVNtwfq1ETS4uxJm6bLP0TxE4v9NeDM2NAs8xB9SbGj7AO-AxiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پای رپر ها هم به تجمعات شبانه باز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/150789" target="_blank">📅 21:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkb5ktSW9dFhwNKwhVJ2ZO0TuuU-c2gag56lAELl4ih78S0CQ2sHLDVGyDbrRDs947jgeHMy1isLNCcnVfBESWBdwjhAM1Ta8wlYrek-qRg2bfsazxRtXmeKWxIkZ0hNUW3j1N1tjKEAHBFueeGfkDMXwex_OGKCXpYp05Ba6G6rRSp4IkT-D0v-FKRDpJD6aeh8YkFfFrn6uqZc4db6hdASNQA-o7uoCBA50ksIVb_GPM6Qt9f-H5auob2me_gOqYwFD6SamgTuD0t3_wo7dTwHCJhdQ3EjotWHQXW7yH6ycJ7aZgOV1cbnH23GEnqMOR8lUkjf2RYulelORpe24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز
:
مقامات بریتانیایی و آمریکایی معتقدند که افرادی که در نزدیکی پایگاه هوایی RAF Fairford دستگیر شدند، با یک عملیات مورد حمایت ایران مرتبط بودند که یا به سپاه پاسداران انقلاب اسلامی یا یک مرکز فرماندهی نظامی جداگانه در تهران مربوط می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/150788" target="_blank">📅 21:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OeYSEW6f7HDjf1BoX4AAQbnKjk4MIYmz2wDXW-umo0FGrEhrRUFTbFpDCZaS3CddXhk6l-qJnASEA0zOhlgk_TDjPnVRxIMVGAn6aUXb4iq2ngqRHNg3BhJlXMwq8WJJWiHcjGPIWfKl9EdIhoXU-LlDSGJzshCJy_JVRd5I0KOIpqWnBGSpUzgkRnZ1i4L1RqTf8_q8BlCDUk7UBJuPTcbqWWAE6kH7iRAKLN_sbDTG4tBM0pUiiVMjiuYJzHwNYCImReBl4BuiKVkh-EQmqxzBRSXVkcwoNIHDaDdH4TKmQbT9HEu3ULhCU9gbC5ZrqHaLxpX71UveqtQ_xK0nwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری یو‌اس‌ان‌آی گزارش داد که ناو هواپیمابر کلاس نیمیتز، به نام یو اس اس دواایت دی. آیزنهاور.، به بندر بازگشته است تا بازرسی‌هایی از سیستم‌های پرتاب و فرود هواپیماهای آن انجام شود. این اقدام پس از حادثه‌ای صورت می‌گیرد که منجر به از دست رفتن یک هواپیمای جنگ الکترونیک EA-18G Growler و مجروح شدن چهار ملوان نیروی دریایی ایالات متحده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/150787" target="_blank">📅 21:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پولیتیکو: ترامپ با حملات هوایی مجدد علیه حوثی‌ها مخالفت کرده، علی‌رغم درخواست عربستان برای حمایت بیشتر. او معتقد است حوثی‌ها نمی‌خواهند بجنگند و آتش‌بس فعلی را حفظ می‌کند. حوثی‌ها همچنان نیروی نظامی قابل‌توجهی با پشتوانه ایران هستند.
🔴
مقامات آمریکایی درباره تداوم حملات اختلاف‌نظر دارند و از درگیری گسترده‌تر هشدار می‌دهند. واشنگتن فرستاده ویژه‌ای برای مدیریت بحران عربستان و حوثی‌ها منصوب نکرده و تعامل دیپلماتیک با این گروه دشوار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/150786" target="_blank">📅 20:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwIZ_lmrc5uUy34kgupx3ZdPyiI96gjMcG0Xd3u3R7U8kwpnLAToiOD0Tgy8g2OhyvqdEmSq4XeV6ML6Ls6eQe4vxbUluMf1R9B0WtgJzu1Ll3yYht9HZbsxY_ljyVUaC6YXaNLq70n1fEbEsdJR8bNfqOkkkaszv6lDCObFEq6kbHga4jml6su2JDVWYGsemXGbCIqv1zI9YM6NJyLOao5C2j6wjO1QSX_wQcLcQkn5Y0Byj_XKyvKvAiN1BV6x0gH0vM4vv9XY7DR-jz9tZP83cLnJqiaKu2CQHve37UkHxJ1oefDaQmShHGW2Uygmk5wKbr9nyOUPa-QOLdYfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس، ابراهیم عزیزی:
🔴
از افغانستان بیرون شدند.
🔴
از عراق فرار کردند.
🔴
بعدی: اخراج کامل از غرب آسیا.
🔴
این روز را علامت بگذارید؛ نزدیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/150785" target="_blank">📅 20:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150784">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQRp6krYhFVsP2HIQCK9VemcrbV9Fx2PgmKhatUWoekCCaZ2WARs1HZjIzH9lNZe7sJmJyLcPpgxIV5NGpKdDoxDBq37UgNIKXyztGeuu-GGXqjy8mJcr6nX8ipxO3mGSUjoOPToZQJalmmS-QwCyP5oJKhPNT_29GSatMfUtufw8HCg9fia059Zy3B07Xs5yvZU9BmmynQ_4hHs7lOpaxTbU43a2DUqYXitdEH65J5P_S_qBk-FGyM5teT0x4WR3c2Xx4QYL8IKwu3FZ2Hv0Mowgm-Xlu4Sj3t0NUgBtvkAxovfyLNj-I8-mTWv4ICQQlZPmwrIagHVG3VP4s2VWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوشته های سردر اتاق رتبه ۱۳ کنکور ریاضی ۱۴۰۵: دوست دخترم مادر شد من هنوز کنکوریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/150784" target="_blank">📅 20:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150783">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG5iC57JI41O3FQUUawanaNZpOxpFT15Cpgk8GD1wKQX7me33-zcgObIdl1Fr0wOL6c6Ne9hsWtETAoHquBonOvN3CaScnkcqa38R2yLqRq4NRCJ_DIzUKfghxpdtqM-Dp02PRQdDN8Oxut0PpO_DprGfIF7BEITM-_Ccufz_UrS7wmBo01Bt-VNRRmlI8FV10sqKEVAk2xDfKXCa-jb_FHsJH5jglIStWgzhcgCOgsIX3WQ4MjQmDS-toDWvxnvva1ExJMnVOKRAdvAEK1quvE14IlOJNFekOnRfiPeeRtzC5OrJqlxU_3NJ7xGZbsvfODygLZr-1XLygaygqkqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابناک: گلشیفته فراهانی قصد داره به‌زودی به ایران برگرده و اقدامات اداری لازم برای این موضوع هم انجام شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/150783" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150782">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
زن بیژن مرتضوی: تو مجازی فحش میدید تو واقعیت دنبال عکس و امضا
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/150782" target="_blank">📅 20:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150781">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzL1n8qqX88bcUlPEVYV7xmfDaxsmN97L8AjyXjWpwkpGlYwkdS9gicLRq_UIpqHxMfHV4DNSwz22skkGAcbD-Ljlc955O38TKDY0vf6Ba6V328PDmWWPjoaEhYC4eecKLXZxbyx1X-PXeD4cpNU_a7yZtTnwtiPji_PzVkt5zeuSsnb-5-qlof3YGslaChEaz-KyROQsD8C2MQUIZzLqWoiAr0qiXzjbqWkpxO96jLGECE4qOjVNGrCCnoVy_A0TXLH9anVeTL5DOQOrOs95JkBVkrobv07EYGV5k_arkm73zxcIzHBmKbdjttn1Nr8K9IAmEBvHplSe9GHFTTlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به خاطر اعتراضات داخل فرانسه، اوضاع اینترنتمون بدتر از چند روز قبل شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/150781" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150780">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b387287a.mp4?token=suBsdIQbqlsJRY5KN1yWEvPvlTdcfuyF6pGuexLDiMk1NVdnkA3ozLK1mVKIOYislkIrdiIEMXdAr5dBqgYBHL-_X-8y02nnhbNuqKCgCQbUmd7ZwXCaw3486F2CwwD38K9Nol5R7U9l-kTB2Q0AdM9d2pLVVzkm3TJK4UNl72p0NRc2V8alRWmWIHXfmPrCgMWm9lV7HGcEB_NR654CmNp1R_1lFlO9vw6pgl6ixYytW9Yea4QbdpSAW4mLHVrIQpLCOXGxmAWIUiH4crriHJxTSGKQk4R9ZTthybHmS469rc3SlPpyOPAQ1OzbyN7h9MYZM9tmAD7DPgLJG7XIxT_KeWmnUKtZ6ws_3sfkROTqmiNDPRuoUyregtf8DHdYiOUu_LbsauG4atmd-67FsRodkMWyRT_JM5LfBER9fgt8gxqNs2QgamsqUy9vP80Gfhjw6N0BjFRys83PovUn3IHLu2Y1lWrcP-nejHy8oAJjEV_tHf9GJd8bnKaPIDCcRHYlb9aCC9_4Ti3RgIOtnBETCFnB2XQNOEYG-m-ylpcJcIPdEIRLWAOqRhdl6ZXSMvNswoNz3KLOZ67tSIXXWg2jwlim5uRT9X4hxSv00_NqiQWRtkiWndyfjECEDtU7ZOkMzNQ8Uvje3_xVySe2XDcYe4mhcMJPw7KQS26xGMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b387287a.mp4?token=suBsdIQbqlsJRY5KN1yWEvPvlTdcfuyF6pGuexLDiMk1NVdnkA3ozLK1mVKIOYislkIrdiIEMXdAr5dBqgYBHL-_X-8y02nnhbNuqKCgCQbUmd7ZwXCaw3486F2CwwD38K9Nol5R7U9l-kTB2Q0AdM9d2pLVVzkm3TJK4UNl72p0NRc2V8alRWmWIHXfmPrCgMWm9lV7HGcEB_NR654CmNp1R_1lFlO9vw6pgl6ixYytW9Yea4QbdpSAW4mLHVrIQpLCOXGxmAWIUiH4crriHJxTSGKQk4R9ZTthybHmS469rc3SlPpyOPAQ1OzbyN7h9MYZM9tmAD7DPgLJG7XIxT_KeWmnUKtZ6ws_3sfkROTqmiNDPRuoUyregtf8DHdYiOUu_LbsauG4atmd-67FsRodkMWyRT_JM5LfBER9fgt8gxqNs2QgamsqUy9vP80Gfhjw6N0BjFRys83PovUn3IHLu2Y1lWrcP-nejHy8oAJjEV_tHf9GJd8bnKaPIDCcRHYlb9aCC9_4Ti3RgIOtnBETCFnB2XQNOEYG-m-ylpcJcIPdEIRLWAOqRhdl6ZXSMvNswoNz3KLOZ67tSIXXWg2jwlim5uRT9X4hxSv00_NqiQWRtkiWndyfjECEDtU7ZOkMzNQ8Uvje3_xVySe2XDcYe4mhcMJPw7KQS26xGMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ:
ما جوانان آمریکایی را داشته‌ایم که گفته‌اند: «من را برای جنگ با کلاه‌قرمزی‌ها بفرست. من را برای جنگ با کمونیست‌ها بفرست. من را برای جنگ با نازی‌ها بفرست. من را برای جنگ با اسلام‌گرایان بفرست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/150780" target="_blank">📅 19:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150779">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278c1d4127.mp4?token=KKXzt6wsQfjYFylyvAg70qJl7aqqE1eyghGgCnQ6NO7KmPAIv5C62khRwDa_FYOCU6_zQqXMbp7PIoUCOoTatmuB16l9dNVBL-dTiRYena01ilcgHBcBktTmOsHRs6pGgsuFljXFExxx4PqG358Z8HeMF6XC9qAxXu8Dm0ULj7Uyv2SmHttij0gamaSz3N5Sq3N0jFbxvC8nYMP160ly2iDnvhsDxvA-Zn6eNJDjpl3E7jNxRXLTmd6pAfo8nZDzmWDrVm7TNwxMKA-mgT7H_MrmWr2-AkvEMxs6IcrXAOEmCH86N9FwwvLPVR8y30QCSAWfxLpe5Appn-hVHU1EgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278c1d4127.mp4?token=KKXzt6wsQfjYFylyvAg70qJl7aqqE1eyghGgCnQ6NO7KmPAIv5C62khRwDa_FYOCU6_zQqXMbp7PIoUCOoTatmuB16l9dNVBL-dTiRYena01ilcgHBcBktTmOsHRs6pGgsuFljXFExxx4PqG358Z8HeMF6XC9qAxXu8Dm0ULj7Uyv2SmHttij0gamaSz3N5Sq3N0jFbxvC8nYMP160ly2iDnvhsDxvA-Zn6eNJDjpl3E7jNxRXLTmd6pAfo8nZDzmWDrVm7TNwxMKA-mgT7H_MrmWr2-AkvEMxs6IcrXAOEmCH86N9FwwvLPVR8y30QCSAWfxLpe5Appn-hVHU1EgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ، درباره جمهوري اسلامي ایران:
امروز نفت بیشتری از تنگه هرمز عبور می‌کند تا قبل از شروع درگیری، زیرا خلبانان باورنکردنی کنترل فضای هوایی را در دست دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/150779" target="_blank">📅 19:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150778">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=Epkc4n0qSLyrzi4w7Xh_Opl0jxvM4WvPuEoawBHrwekr1N3yphoWIX1vdF4eUymnk4c7brBreh-ijcJ532Hf3Gfmm48XQChvpdunz_TOTe17qiIXDSKNgLRL66l169Z33UqOaD4K1jEhHv30OeAAIy5PilAi-1POJFwqGmjd0l8NbXWfKSR-_RpXxASQdf-2-54cOpPkTF08yqozVdJCzE0zMljiIeWqANudhosEuBTQrT_HYd3VPpg1A-ruZrCeD0Mum_a0Fi72bDJZpVnM-5FBNtEUUUYSNVa8AQ8UE2H5gD_7R9F-iECoUZTEDQnRxueRUrrhn5DTNBVtgdNNkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=Epkc4n0qSLyrzi4w7Xh_Opl0jxvM4WvPuEoawBHrwekr1N3yphoWIX1vdF4eUymnk4c7brBreh-ijcJ532Hf3Gfmm48XQChvpdunz_TOTe17qiIXDSKNgLRL66l169Z33UqOaD4K1jEhHv30OeAAIy5PilAi-1POJFwqGmjd0l8NbXWfKSR-_RpXxASQdf-2-54cOpPkTF08yqozVdJCzE0zMljiIeWqANudhosEuBTQrT_HYd3VPpg1A-ruZrCeD0Mum_a0Fi72bDJZpVnM-5FBNtEUUUYSNVa8AQ8UE2H5gD_7R9F-iECoUZTEDQnRxueRUrrhn5DTNBVtgdNNkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ:
میزان زیادی از اطلاعات نادرست، اطلاعات غلط و پروپاگاندا عمدی درباره ناو هواپیمابر یواس‌اس آبراهام لینکلن وجود داشت، اما ۸۰ درصد از گروه ضربه‌ای این ناو برای تمدید خدمت ثبت‌نام کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/150778" target="_blank">📅 19:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150777">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih4nlecVwhbY2oEM71PrKhhUGjJtt7IZOuPAr3uTzihynXhlt03gHWxW2PJlfvBa8f5rCBU6qweqfhOvh9WV1tGfI16u6PeMxF_pd5ObCBArg6t0x4J2_CIgehLT_xtX5Kt6p2voF7P-QTXAjY7K59o_4AlpQJJp4zXjMjgCAzOOLmcIAVEFowaDFaVsSyiU3D1_5WZWJ-N-32NLOa8GXEnJgbE0iLnPYPUv3QFnu0961Yk7vPOHBB_48JGVkvLCIPNrUOgDWwGNGdS-I66aLpiJsINb7JTDOvGYtwCcDunGep4awsZaT6zc643tIdbLqnU9bNl7D8mSR7uRMYAioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطهرنیا، تحلیلگر سیاسی: وقتی عراقچی میگه ما برای «جنگ آخرالزمانی» آماده‌ایم، یعنی ترامپ در پیام‌هایی که برای ایران فرستاده، تهدید به چنین جنگی کرده و ما باید خودمون رو برای اون آماده کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/150777" target="_blank">📅 19:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150776">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
کشور ما تحت رهبری جمهوری‌خواهان به‌خوبی پیش می‌رود که تنها من می‌توانم این قول را به شما بدهم:
اگر جمهوری‌خواهان در مجلس نمایندگان و سنا پیروز شوند، من به تمام شهروندان بالغ ایالات متحده آمریکا، ۵٬۰۰۰ دلار می‌دهم.
جمهوری‌خواهان می‌توانند این کار را انجام دهند، اما دموکرات‌ها نمی‌توانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/150776" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150775">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔥
کپی‌ترید پرریسک راه‌اندازی شد  برای دوستانی که ریسک‌پذیری بالاتری دارند، کپی‌ترید پرریسک  را اضافه کردیم.
📊
عملکرد این کپی‌ترید دقیقاً مشابه همان حساب ۳۰,۰۰۰ دلاری است که هر روز عملکردش را به شما نمایش می‌دهیم.
🚀
این پلن با ریسک بالاتر فعالیت می‌کند و…</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150775" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150774">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
به گزارش نیروهای دفاعی اسرائیل (IDF)، دیروز دست کم هشت سرباز اسرائیلی به طور جزئی مجروح شدند، زمانی که دو خودروی نظامی در نزدیکی روستای "راب الثلثین" در جنوب لبنان با یکدیگر برخورد کردند.
🔴
شش سرباز به بیمارستان منتقل شدند، در حالی که ارتش اعلام کرد که شرایط مربوط به این حادثه در حال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/150774" target="_blank">📅 19:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150773">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
حمله موشکی بالستیک عربستان سعودی به زیرساخت‌های مخابراتی در منطقه مجز، واقع در استان صعده، در شمال غربی یمن که تحت کنترل جنبش حوثی‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/150773" target="_blank">📅 18:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150772">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8afbd943.mp4?token=livMNXlaBZ3EZP7Q0GqAs-6LfhC4s_5uJneuIpysPegGqpyxjI6aX__tvZOEhyDKyDvZ1PK0OYvH44FR6dBO3UYypoeyuwQgrxJKQX2Q3Hduv_6cnhb4sCiRWsmqqXy7X2HEHRmkjeVYChbiMbCXZn-U6M-v_qvoeYI1lMcJq5-mvIFpMiNAmVcdz46E5ba4K2X16jqzndm1na8EXwiZSneidLYGs4GkFuIaCA5jZ5Ax5Y7d_sKowV1rCd5Mkqr3wSWYA9o6ahFQZwlYR1-KKaBT6KMz26FUGnI9oRQdFk42EvNicooFKJISpL78mldJNGqIxTBtLxXxFngFLw0BsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8afbd943.mp4?token=livMNXlaBZ3EZP7Q0GqAs-6LfhC4s_5uJneuIpysPegGqpyxjI6aX__tvZOEhyDKyDvZ1PK0OYvH44FR6dBO3UYypoeyuwQgrxJKQX2Q3Hduv_6cnhb4sCiRWsmqqXy7X2HEHRmkjeVYChbiMbCXZn-U6M-v_qvoeYI1lMcJq5-mvIFpMiNAmVcdz46E5ba4K2X16jqzndm1na8EXwiZSneidLYGs4GkFuIaCA5jZ5Ax5Y7d_sKowV1rCd5Mkqr3wSWYA9o6ahFQZwlYR1-KKaBT6KMz26FUGnI9oRQdFk42EvNicooFKJISpL78mldJNGqIxTBtLxXxFngFLw0BsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری نزدیک از آتش‌سوزی گسترده در پالایشگاه سعودی آرامکو در ریاض، حومه جنوبی شهر ریاض، در مرکز عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/150772" target="_blank">📅 18:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150771">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
از دقایقی پیش به دستور بانک مرکزی،
نمایش نمودار قیمت تتر، دلار آنلاین در صرافی‌ها متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/150771" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150770">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2JbUSKfbJ0mFx_aI_9zJmg3f9xwls3-ATlEDpA-BsF58BKhsFjnlbuLU9P12ZK_OcQQpmXrp1Edo-gyZmqnruVAYmTr65Ahs1L2uRn81hjnPzwuWksn8RnFN6zhpqhS3NKELVdvbYIYecISKgvyTIPQ7HqE-B8uNd_U9Zpdm-A_binTXDxc94Yv1nqGCR9f6MfOQ6i_F8UfaMhLOFLOt2KbnC7mY_tty6Ffx22J2U0vWQ_OMZomJKY5j4k37YdvGCvatlLttDl92Q1h-P2bYTaZExE5JlnwEsM4eJ1RsEAsCz1O5iLg9ydQ6ds1QH2dptpiS9LeEifk8D4lgpSo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: به طور خاص روزانه بیش از ۱۸ میلیون بشکه نفت از تنگه هرمز عبور میکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/150770" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150769">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b3e7c6b.mp4?token=Rerl2J-cs-ox7vhcJO8-zqKSlCZoiiU1JDUFBtbQc_O1coOCR-bg1V-jzZk9ysuw6vCj8avOWZp5QVpZq8CIAKAEBtOBWOWHPsVo3HxTZu1sVASiQal0AmZ0a-7l6RD1S2tz00lNyfVpqoCgFQISCsrcalM7_D3VrVWpHJE-gV7IKMwHa7BF_Y8uj-W7ircJkiaJvWA_TInfRW5rKXi6BIuoEgUqhM-LvSQ7CK7dcj-WHR5j6qr1v9ELO2_poB4Z_zoO-meVWwQPCD2R7T92nPs8Si-EDWrf_dN6P4zr5Kw37cuKkPAJtKa_KZMSHtparaGMTu3PyWWXLysSlkVTlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b3e7c6b.mp4?token=Rerl2J-cs-ox7vhcJO8-zqKSlCZoiiU1JDUFBtbQc_O1coOCR-bg1V-jzZk9ysuw6vCj8avOWZp5QVpZq8CIAKAEBtOBWOWHPsVo3HxTZu1sVASiQal0AmZ0a-7l6RD1S2tz00lNyfVpqoCgFQISCsrcalM7_D3VrVWpHJE-gV7IKMwHa7BF_Y8uj-W7ircJkiaJvWA_TInfRW5rKXi6BIuoEgUqhM-LvSQ7CK7dcj-WHR5j6qr1v9ELO2_poB4Z_zoO-meVWwQPCD2R7T92nPs8Si-EDWrf_dN6P4zr5Kw37cuKkPAJtKa_KZMSHtparaGMTu3PyWWXLysSlkVTlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الهام علی‌اف، رئیس‌جمهوری آذربایجان، گفت: «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/150769" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150768">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
تلگراف: خاورمیانه در آستانه دور جدید درگیری نظامی گسترده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/150768" target="_blank">📅 18:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150767">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حزام الاسد، عضو دفتر سیاسی انصارلله یمن، در واکنش به تحولات اخیر گفت: «تشدید در برابر تشدید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/150767" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150766">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ec018bef.mp4?token=SXc8Ezf3AU3rzn3wEl0lTJh7bNuYbVNUHhv1cwmoKvJS4nyzA7j_gSA9MCSQQtS_Dafoqnm7IpcBylBnqu6gHgFwFirKKQBdQG__VNcUfNdkKp0Ojts8xQMj8qm9p5xcwp2QKfXfG85eYCd5hihERq1jivtayViylIbko8MwbVnBVDJhtyrMVfPPLDkfFC0BIXnmxfY9iiKhAkSf7MToApPDngr7HdQgtjFJM7umW6S8NEgHajNpzgfD9W4JTyoa_aFX2eglcHg5sT1LcfF32DY1me7sQFrnNxH1gtVcay15KIXX8MDMYoogGWzm0jKcWIZQdQSHSty-XqC6YcYloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ec018bef.mp4?token=SXc8Ezf3AU3rzn3wEl0lTJh7bNuYbVNUHhv1cwmoKvJS4nyzA7j_gSA9MCSQQtS_Dafoqnm7IpcBylBnqu6gHgFwFirKKQBdQG__VNcUfNdkKp0Ojts8xQMj8qm9p5xcwp2QKfXfG85eYCd5hihERq1jivtayViylIbko8MwbVnBVDJhtyrMVfPPLDkfFC0BIXnmxfY9iiKhAkSf7MToApPDngr7HdQgtjFJM7umW6S8NEgHajNpzgfD9W4JTyoa_aFX2eglcHg5sT1LcfF32DY1me7sQFrnNxH1gtVcay15KIXX8MDMYoogGWzm0jKcWIZQdQSHSty-XqC6YcYloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی پویش جانفدا: در میان ثبت‌نام‌کنندگان افرادی هستن که اقامت آمریکا دارن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150766" target="_blank">📅 18:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150765">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
زن بیژن مرتضوی: تو مجازی به اقا بیژن فحش میدید ولی تو واقعیت دنبال عکس و امضا هستید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150765" target="_blank">📅 17:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150764">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
قطعی برق در اثر طوفان شدید در قم
🔴
بر اثر وقوع طوفان همراه با باد شدید و گردوخاک در سطح استان قم، تعدادی از فیدرهای شبکه توزیع برق از مدار خارج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/150764" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150763">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=o2Ec8jwgC5GTrGeM8LSvmjLfSFYqpHUzx9HSGE4UQIDBIF66x5B1MpuFwtohrUCPUTd2ZJsfkzx0NITZU9cwl9BNRn416Byq6w3mJAL2gNNc0OtL7oBTzmS5N7koMtD9UELX1klZ5aXoX7t41eQ7Yc4GVJ09umY8rW2XZgY0gW0ytQ3CwkTAFCluSWRtw509AjVBL0fvTqDnvPKPFMe7Hb9euMw4d-dpxxjh6igw_Tz7uHgsh9QLhpVZC1llO5IZKwwxLgM19Bkf8NOY3sfGOmmkwcYhj9OpcvDztmqN2D2drXygqf7JAb3gPO0w4y0DHkDezwfKASH2jFPmqjHBN6pNntKitze4LnG3ouYEyK0EmW0Lr3luvoqJZJvHUeO905Asyhq1O2gVNPdAdKVTFl1LA_zIZF5WO6IHFShD_PkekmrTdYkTY1jt77elSBHOUDWDh10hqBalUldyJPxrq7Q7sTmxBGvYZLz-0l2yGfFspJGj1lPMT6CzW2R0UfVJZzVnlP8JY-pUOo2cMpwad4dDKfPXCA8clYOi_Ck_iZttW2Eyrla5pSaCnyCQtRoc06AjxmSVdvkIyXUWFinwTKDOQp-r4cI9PnP1eRvSvqvwj1Gu_zXRpBLyLut3AL7pykIgG7QZEd58-VnSS2EvldFvcPR25-OcHjs2t8QBHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d34c7efd.mp4?token=o2Ec8jwgC5GTrGeM8LSvmjLfSFYqpHUzx9HSGE4UQIDBIF66x5B1MpuFwtohrUCPUTd2ZJsfkzx0NITZU9cwl9BNRn416Byq6w3mJAL2gNNc0OtL7oBTzmS5N7koMtD9UELX1klZ5aXoX7t41eQ7Yc4GVJ09umY8rW2XZgY0gW0ytQ3CwkTAFCluSWRtw509AjVBL0fvTqDnvPKPFMe7Hb9euMw4d-dpxxjh6igw_Tz7uHgsh9QLhpVZC1llO5IZKwwxLgM19Bkf8NOY3sfGOmmkwcYhj9OpcvDztmqN2D2drXygqf7JAb3gPO0w4y0DHkDezwfKASH2jFPmqjHBN6pNntKitze4LnG3ouYEyK0EmW0Lr3luvoqJZJvHUeO905Asyhq1O2gVNPdAdKVTFl1LA_zIZF5WO6IHFShD_PkekmrTdYkTY1jt77elSBHOUDWDh10hqBalUldyJPxrq7Q7sTmxBGvYZLz-0l2yGfFspJGj1lPMT6CzW2R0UfVJZzVnlP8JY-pUOo2cMpwad4dDKfPXCA8clYOi_Ck_iZttW2Eyrla5pSaCnyCQtRoc06AjxmSVdvkIyXUWFinwTKDOQp-r4cI9PnP1eRvSvqvwj1Gu_zXRpBLyLut3AL7pykIgG7QZEd58-VnSS2EvldFvcPR25-OcHjs2t8QBHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون؛ بارش شدید باران در برخی مناطق تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/150763" target="_blank">📅 17:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150762">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ: معمولاً در انتخابات میان‌دوره‌ای عملکرد خوبی ندارید و نمی‌دانم چرا
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/150762" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150761">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
مهر: شنیده شدن صدای انفجار در جزیره قشم از سوی دریا
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/150761" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150760">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی ترور دو تن از فرماندهان سامانه موشکی حماس در دو حمله جداگانه روز گذشته در غزه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/150760" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150759">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترکی الفیصل، رئیس پیشین دستگاه اطلاعاتی عربستان: یمن، تنگه هرمز، بازدارندگی آمریکا و جاه‌طلبی‌های هسته‌ای ایران در حال تغییر محاسبات امنیتی عربستان هستند
🔴
خویشتنداری دیگر قابل ادامه نیست
🔴
چین وظیفه دارد همان نقشی را ایفا کند که هنگام توافق عربستان و ایران ایفا کرد؛ باید منتظر بمانیم و ببینیم پکن چه کاری انجام خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/150759" target="_blank">📅 17:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150758">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گزارش‌های اولیه از سرنگونی یک فروند پهپاد آمریکایی در نزدیکی سواحل ایران حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/150758" target="_blank">📅 17:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150757">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95b509824.mp4?token=LNcm0I5si0K-9RvPMmntHLv8tCCj0IEV_uzCY4Nf_-rNMYuP045BS34U9SQtSXnaNwTxLGI6j4vRPNfUKGPjL0acOoNE0UweBGYv6y2sgu_jeyI-kwzFeVAwo7bx6FvZCKmJoU1NT1lZYejBg2gDyA7asKtrg6iJHz6-Z3EuwpYIGFLxQZCl1gtpskHKeoMo1ca_bYAgsP55eXMiEzZIZHeVIFtnGzrieTErB2UbJOyHuBhBz0gXePnlpMjhZ3Gu-yzturKFmlcJLGCKvv2o588cOs-SGDkGV2oNxGzvRw9Ju456CmMNVV5zdTom48hGJ-wZ1NWhz7WEKYH_C-_gIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95b509824.mp4?token=LNcm0I5si0K-9RvPMmntHLv8tCCj0IEV_uzCY4Nf_-rNMYuP045BS34U9SQtSXnaNwTxLGI6j4vRPNfUKGPjL0acOoNE0UweBGYv6y2sgu_jeyI-kwzFeVAwo7bx6FvZCKmJoU1NT1lZYejBg2gDyA7asKtrg6iJHz6-Z3EuwpYIGFLxQZCl1gtpskHKeoMo1ca_bYAgsP55eXMiEzZIZHeVIFtnGzrieTErB2UbJOyHuBhBz0gXePnlpMjhZ3Gu-yzturKFmlcJLGCKvv2o588cOs-SGDkGV2oNxGzvRw9Ju456CmMNVV5zdTom48hGJ-wZ1NWhz7WEKYH_C-_gIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای از فعال‌سازی سامانه‌های پدافند هوایی در جزیره قشم ایران برای مقابله با یک پهپاد امریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/150757" target="_blank">📅 17:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150756">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnhiLRrUTlioAugmkjuuzYTC8Li4l2hF9fbGJFxhV8FLl-KP9goysceUabZb_2zMiHJs5JC9Rc0cqEcYbY169ibiAcxCnfpkB6EbntUavF_SiCtHTZiTJFirrqOxI_xxtgBaI6LaNH925BGiVE2rBghIzvWDe1uzNfEeSb1QTHRCBAHgXzzhXOAxEwurNaUB1ZYl2baW65NgI4LQ1NeFlMaRBAZvjWxexkTo3_yI0QlQ21_N-zA6wBIzM85h5_-Pe8QB3LwklQiKBUbnNg7NVGV-LSLNP3q7WH7A2neKt_T9Bwc4ear0YUsQvWWCURPpWRmuXXfg6VDJCAMmiESTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌های اولیه از سرنگونی یک فروند پهپاد آمریکایی در نزدیکی سواحل ایران حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/150756" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150755">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا در حال تقویت گسترده نیروهای خود در خاورمیانه و ارسال سامانه‌های پدافندی به کشورهای عربی برای احتمال ازسرگیری جنگ ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/150755" target="_blank">📅 16:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150754">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/k4oZCBWMbm0lpfhsCLULDXr4Y5O730MGWBHF6XHYlL11gbnSk4i9l64VEt8bwFjd71VsB8gUu79CrOccZdCnxfab91afAuxeTw0zKu75Q6zZ6uWl_E1K8_HdaBs4noErXM_TvgJU17KTwJFO5Vci4Wo7xHYKq2Q2xUnCnqfLqnGCq3Aj37GHp7SxjHFWwFlJJvdZphZC5jdBcQF3EwS96D3UH8ddaFfqeTl098WPl6iypfsTlDwBFrhlgkxKdVC7xJ-E13nZG9gqsYIF7k7Qw2RVcJFXJUwpT8I68c2xXRKspo4m9bICj2zB4LK6lkHQNCY-ifHqla-eunCgzUYZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی ایالات متحده ارتباط خود را با یک هواپیمای امدادی که شش نفر را از جزیره ناکات به سمت بوستون حمل می‌کرد، از دست داد. این هواپیما در حال پرواز از برمودا به بوستون بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/150754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
منابع عربی: وقوع چندین انفجار جدید در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/150753" target="_blank">📅 16:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی سپاه اعلام کرد که سپاه موشک های بالستیکی ساخته که میتونه اهداف متحرک (مثل ناو هواپیمابر) رو مثل آب خوردن مورد هدف قرار بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/150752" target="_blank">📅 16:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwXe5ldBKEYHyRcXmFGbHByZxzj8hhcpF39rZ2yRyIRyRLb_4p9Hj66DaOlur52CsDyLbaqOCjw2ENrho2GYWbVpSlI0TDT0_cSiLbHdSx7PHefA6StW5FvGH9nyD6HpFgAub8pcD1ypL_lvYzg9J2Vvxv1V4SG2330CQJsTc553jIPDe8NK3uC5h_XsDN6XttiulLd91W-yHI7AhW_K_2iclXZLE5R8M3qAT2oNcHY2NK9Pz8mMbO-kAwQw8DII1tB7sJ0KTg0Yru9OjmTcVMOd-Jerww9D4-IW1PaPJ-VTEJ_PHsuvWtNbpdR5cinkiksfOV5jZnfLPBN5hW2SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادامه آتش‌سوزی در ریاض عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150751" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150750">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به خبرگزاری Axios: ما ایران را به شکلی بی‌سابقه منزوی می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/150750" target="_blank">📅 16:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری /
رویترز: جنگی که ترامپ بارها وعده پایان سریعش را داده بود، ناو دوم آمریکا را هم به هرمز کشاند
🔴
رویترز: ناو جورج واشنگتن به‌طور غیرمنتظره از ژاپن اعزام شده و مأموریتش پایان مشخصی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/150749" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
