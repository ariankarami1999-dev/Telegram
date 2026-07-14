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
<img src="https://cdn4.telesco.pe/file/YN5dSGrgn0AFOgOhTqYhjotqu1Shrj9vDoyrF1FbTrIcMiygQk4FA9R-Gz5_oxmnXD_QJjvuKK9q3NjqcLTKw836_PETiz7awpsvsYv2jRjPBezkZFiuKcKcvycZzJt43y2wvwKSdm4V8tV84-PUpuu5FS9RwtNAMVYAppBd6Nsb6mUWXtXMT2c6ihzS4AAOlOYkB1pWW94gYOFhjz1y4yqpHsX7e6QNdEr6lmRfWkd8vZFZzq297_lxVkkwsy5rVpyarQ7gTTXHATa2KJ-7qebidp5hpYBLYfK6SdR7TlsEkJH9OwFlIDOieE1oLQdOffQ-qrH8a1mI5OlhhEYs3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.39M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 03:12:52</div>
<hr>

<div class="tg-post" id="msg-671238">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
خبرگزاری رویترز: دموکرات‌های سنا به دلیل مخالفت با جنگ ایران، لایحه ۱/۵ تریلیون دلاری بودجه دفاعی آمریکا را متوقف کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/671238" target="_blank">📅 03:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25d764910.mp4?token=LRSb1WCDb0ifDZrssz29Ef4rMqvdVSJs3XGljSKSh052I38rz4nZ-x2V_CmGFiVtZvHfj09mDv-9CrD2Od1YqXpaf7mMdG5XiWAgaRE2dUvo1GnTaJnYZ28_uqu8TBU1OxZEU_a6KWMlEJAsn7c9YwKrRW_qMemx_IyhTLF9anE5wpWPk2Axb1h3emhgn_odKWJh7tSFRUMyZmgsEkYjBeHxVRd40JNgd6GzwS1XeubLQ-RujxRG3HbQJaxDpkX1FsiGSwYKdv19nTaauWJf5GtgsiDJxHgVdePWivIqUg4pPXjpYtpLqg17e1ZXeSNIaIxpzMdkn0b0oioRDcKcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25d764910.mp4?token=LRSb1WCDb0ifDZrssz29Ef4rMqvdVSJs3XGljSKSh052I38rz4nZ-x2V_CmGFiVtZvHfj09mDv-9CrD2Od1YqXpaf7mMdG5XiWAgaRE2dUvo1GnTaJnYZ28_uqu8TBU1OxZEU_a6KWMlEJAsn7c9YwKrRW_qMemx_IyhTLF9anE5wpWPk2Axb1h3emhgn_odKWJh7tSFRUMyZmgsEkYjBeHxVRd40JNgd6GzwS1XeubLQ-RujxRG3HbQJaxDpkX1FsiGSwYKdv19nTaauWJf5GtgsiDJxHgVdePWivIqUg4pPXjpYtpLqg17e1ZXeSNIaIxpzMdkn0b0oioRDcKcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شیرجه و اصابت دقیق موشک ایرانی در پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/akhbarefori/671236" target="_blank">📅 03:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یک واحد تولید آب معدنی در اطراف روستایی در بخش موسیان در ایلام هدف ۳ پرتابه دشمن دشمن قرار گرفت
/ ایرنا
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/akhbarefori/671235" target="_blank">📅 02:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2jC0ePusLNN9UZZU8D0pekDL2E_8m777MhaQbrnyuVtWeBOHiw4wSHXos1Nu19juNQD-7T5BWkJG-lxpM_JR9FEPzBWyMLMWQgGcUIlFVo2PkjjkP6NzOo5A5F3VLhXfcmdqm3sDkWTZqp5ysZUQeI7LShy7kSjDx-7QEZZu-6-U5AvQQY_iEHhKTiaMhCq97lhbaPeGq6t6hD86Us4TV61wCRmB3ESRsH1fUK3bGyhnelQwOovAEzH35UXjfUuASDmPw-WvgMwVLgkqxEPgMIpPJU0ul9uxWc_rnT9R-dShpwrz5GYsVP1G184TCHFawmzrElTccPZnizsnvCnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت موشک ایرانی در شمال اردن
🔹
تصویری که رسانه عراقی از اصابت موشک ایرانی به پایگاه تروریست‌های آمریکایی در شمال شرقی اردن منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/akhbarefori/671233" target="_blank">📅 02:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a59ef456c.mp4?token=R_ebk8f7vlkjQZd56m4v-EgRn4xzcZGHiwo9t3lfWJ47KPxQsXyB096CKF0yc1PBgqwzHy3gDmayRcj5eumdq8n-lmLRK7hi8A1ZmwWylqsMtZRXYPR2q-9DkwSEQNmmpn-Xcw5RwRYSQ2ufhNtUANTcOWsgrFFVqmJ1oWl98ARzyp3X1J0zIGielEPkhsf2kijZDqg9C6Sd_SQDc97NP4pWUc4yy5u_1wmvbWAUughWoCpag3zIUwYes-03r7sOmAmLE6138ZmTugXtLspy59wHA86mstdI3B8E4B7AWbWfpRKJTgwPh3ykUbmhoA98alBJlvE_EvnEab9j-P3ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a59ef456c.mp4?token=R_ebk8f7vlkjQZd56m4v-EgRn4xzcZGHiwo9t3lfWJ47KPxQsXyB096CKF0yc1PBgqwzHy3gDmayRcj5eumdq8n-lmLRK7hi8A1ZmwWylqsMtZRXYPR2q-9DkwSEQNmmpn-Xcw5RwRYSQ2ufhNtUANTcOWsgrFFVqmJ1oWl98ARzyp3X1J0zIGielEPkhsf2kijZDqg9C6Sd_SQDc97NP4pWUc4yy5u_1wmvbWAUughWoCpag3zIUwYes-03r7sOmAmLE6138ZmTugXtLspy59wHA86mstdI3B8E4B7AWbWfpRKJTgwPh3ykUbmhoA98alBJlvE_EvnEab9j-P3ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش سامانه پاتریوت در اردن برای مقابله با موشک بالستیک ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/671232" target="_blank">📅 02:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وقوع انفجار در پایگاه‌های آمریکا در اردن
🔹
منابع عربی بامداد چهارشنبه از هدف قرار گرفتن پایگاه‌های محل استقرار نظامیان آمریکایی در اردن توسط موشک‌های ایرانی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/671231" target="_blank">📅 02:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بیانیه سنتکام درباره عملیات‌های ایران علیه پایگاه‌های آمریکا
🔹
«برد کوپر» فرمانده سازمان تروریستی سنتکام بامداد چهارشنبه مدعی شد که ایران طی یک هفته گذشته، به ۷ کشتی تجاری حمله کرده و همچنین تعداد زیادی موشک و پهپاد به سمت پایگاه‌های آمریکا در منطقه شلیک کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/671230" target="_blank">📅 02:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حملۀ آمریکا به دهلران
🔹
دقایقی قبل، یک نقطه در شهرستان دهلران مورد تهاجم و اصابت پرتابه های دشمن آمریکایی قرار گرفت. هنوز از محل دقیق انفجارها و میزان خسارت‌های احتمالی خبری در دست نیست./ فارس
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/671229" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خوک نجس: ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم
🔹
ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند.…</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/671228" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671224">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f4c90a8b.mp4?token=gzFC5C0u7ItP_E0pM3qLhX7imKt2lN4sBnwXpv_fuHeJmTEad7bWT12KxysjEqvJUrZa2D55vwfm_6z6Ah3hHYEBHftuBNmqTe7cMctNfCASGo4n1Rt29xtQ9omkLPGGm8Q5odQHxmaMy_awVsWnmfCk7h8p_upmv3uaFDmXDBeM4tdClqizslFpDoYitWF0RNft21KaWPx7-_-u9QoxdRl5DSIDu_hvPMUEQHDwM-BX80mhNMnI_iweExoZGdk3-f4JxmiVkq2fXl_fhRSXAlZ1lEYKCJC7vfYhzkz4nGI_xNScJcLpam8p8y-3F1E9tvbBLULOUO0TVbgUD8-e0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f4c90a8b.mp4?token=gzFC5C0u7ItP_E0pM3qLhX7imKt2lN4sBnwXpv_fuHeJmTEad7bWT12KxysjEqvJUrZa2D55vwfm_6z6Ah3hHYEBHftuBNmqTe7cMctNfCASGo4n1Rt29xtQ9omkLPGGm8Q5odQHxmaMy_awVsWnmfCk7h8p_upmv3uaFDmXDBeM4tdClqizslFpDoYitWF0RNft21KaWPx7-_-u9QoxdRl5DSIDu_hvPMUEQHDwM-BX80mhNMnI_iweExoZGdk3-f4JxmiVkq2fXl_fhRSXAlZ1lEYKCJC7vfYhzkz4nGI_xNScJcLpam8p8y-3F1E9tvbBLULOUO0TVbgUD8-e0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایران در راه پایگاه‌های آمریکا در سراسر منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/akhbarefori/671224" target="_blank">📅 02:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671223">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آغاز موشک‌باران پایگاه‌های آمریکا در منطقه
🔹
منابع خبری از شلیک موج تازه موشک‌های بالستیک به سمت پایگاه‌های آمریکا در منطقه خبر می‌دهند. در این میان آژیرهای هشدار در اردن به صدا درآمده و پدافند موشکی مستقر در پایگاه‌های آمریکا برای مقابله با موشک‌های ایرانی فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/akhbarefori/671223" target="_blank">📅 02:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671222">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکایی در اردن خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/671222" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671221">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dacf0d7f3.mp4?token=d-fJCjFa8Tz0tvZ3MJ88fun2kVTJptI2unUZD2H01Mt88KOgANTrFE4Z9bTQ-BEKDDpWh4nLuN2d-5YoteuolY4r834j-XRg4Mi2DHX3H1hWMd1zaSeyc_hvSb9vz_wA-wYTWYlhzDcJIYHDcF3e2rFxOu5xVvnPSDteV6d36V79rw4EiI91Af8DGxv2I_OT5GYxAySLnPkBjqFNl7gvDtnbU_qffiDlxyGG3VqDZzt7bGe3HdEAEzuLf1hPwqkrWoTUvKFWXWF2os2Bn3i4jAvbPLwzaAPB01zftYNpByCT9CRUgFu3U6noMYEjlTZRJU1Pql2l136edpPwOR7kUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dacf0d7f3.mp4?token=d-fJCjFa8Tz0tvZ3MJ88fun2kVTJptI2unUZD2H01Mt88KOgANTrFE4Z9bTQ-BEKDDpWh4nLuN2d-5YoteuolY4r834j-XRg4Mi2DHX3H1hWMd1zaSeyc_hvSb9vz_wA-wYTWYlhzDcJIYHDcF3e2rFxOu5xVvnPSDteV6d36V79rw4EiI91Af8DGxv2I_OT5GYxAySLnPkBjqFNl7gvDtnbU_qffiDlxyGG3VqDZzt7bGe3HdEAEzuLf1hPwqkrWoTUvKFWXWF2os2Bn3i4jAvbPLwzaAPB01zftYNpByCT9CRUgFu3U6noMYEjlTZRJU1Pql2l136edpPwOR7kUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به احترام جنوب...
💔
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/671221" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uj9lSbtj1Uq_6DAlYnhfc-MdU9knCRLWN-Ch7plUjk8UCg2JpVJQLsF3z5LMyjuEBz4bgQ6iYPfxPrzQmIrKQBwL3gvkA-GEYyCCeXeYnO7xMEGVokUPcz96JL2ljJR5EOT8Q39zFy4X8AlwN9bcBIYHcwAnbphVGUOw7J-miXnSzMYPD7TapUlW82QK7q_wpA_KixELNMB-CpPSVOgF620-_mi034HfMQzATKHpeRv9wSOHBe2tVI6eEuakf6boEowZNRTLEv3cUiNhleQ4LlgQ8YrIQX6zY3v-2EYZQf6W6yLJ20mE20JtnVr86vJSmtVzENryqcG3K6F9cpQg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5FdoTJ1F3nx_MbIhxEj1asvDSSAeDKOmENY9_qB_wNd6SQjwc4nLV9F7b3L_U5I5rLF6rj36nwXcWig_LHcdXN-bN_LU5jRg7mB-p12Xs8iTJc4DF1auK_xtTirkpHtGDRO9DteLzesvLLzuakAivfkZs0kLpp80WjtWQgw_amnA7qsNGi8-K8wdMpQwdVbxtwXj7ivZ-NW8vmfMn5uMxghlqVCCW8qhcikUVEv1vr5gPejXyf7O6fJaR5ryfsFyXuZv9z9o6DvL2K110VS6UT6HNhLSDPSTZEUXngdV86mGxWKiBXBtwcNnmRBih9UQWt2hklgzfqgig0a7ObL8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری جالب از پزشکیان در مراسم مصلای تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/671219" target="_blank">📅 02:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
شنیده‌ شدن صدای انفجار در کویت
🔹
رسانه‌های عربی بامداد چهارشنبه از وقوع انفجارهای مهیب و متعدد که باعث آتش‌سوزی در یک مرکز حیاتی مهم در کویت شد، خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/671218" target="_blank">📅 02:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0021e2c0f.mp4?token=AC8O7-pL2See3LJfu9GS8ncH3GtwJ2pzznCnM_bouYDc2e5-tO7sJjSDLDAK86JfMftzrRFhd9h5pcwljd0zaa_v0aC9csUBSXRfENuTulye-dPoEDEwgHQKGMBduBmeAL-IRcFgkfgk_LzDmNwG74_2QQWs5ioB-JQN2VCVnNHUh3VzXaVN80O4Y387bVylbVKZ2_FzCizMYdn0b4xQsa7QcENshpa7Z85AATh00CumtvlGV0q_f5n2h7-RM7kreKk5m0TLsB_fzvD9tXLr0qzKvSzln4aKd6qUG5phh_cX871l5xZ1D9nx90BlQYWXRGEj_goFva36n0Rl1-0uCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0021e2c0f.mp4?token=AC8O7-pL2See3LJfu9GS8ncH3GtwJ2pzznCnM_bouYDc2e5-tO7sJjSDLDAK86JfMftzrRFhd9h5pcwljd0zaa_v0aC9csUBSXRfENuTulye-dPoEDEwgHQKGMBduBmeAL-IRcFgkfgk_LzDmNwG74_2QQWs5ioB-JQN2VCVnNHUh3VzXaVN80O4Y387bVylbVKZ2_FzCizMYdn0b4xQsa7QcENshpa7Z85AATh00CumtvlGV0q_f5n2h7-RM7kreKk5m0TLsB_fzvD9tXLr0qzKvSzln4aKd6qUG5phh_cX871l5xZ1D9nx90BlQYWXRGEj_goFva36n0Rl1-0uCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم
🔹
ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/671217" target="_blank">📅 02:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de4c546ec0.mp4?token=TgGkKibkfsg_KKXIhm-7b-eKb48NveSROzBPQ8Pc2OFIB8NcqggfT1Dtjl-nXhNqdMpsd7VHpi1T4JSl7Hqe6La-eUrilCCQdAwPTefbFUUMWjfY_qoyRKM-45NCSMikAKo-8socJjr8EiCHvEBLtejtwn_VD2xNiiJlpuiahT1_zeXRkg0dQhWoW1VXeSc5AodXCWN1ifag1ldJczs3Y6voTTuSfXE09Pna0d6Jb7_IMO4yu88-4LTgrTO91Hsfx0f0xDzD_NdxEagm-9PA42RwiVYY62sc3VBZ_kI-3vbuhH2DTW1pEvr22YH1j0Mp0soZVNt4iWlrAk8z_qzKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de4c546ec0.mp4?token=TgGkKibkfsg_KKXIhm-7b-eKb48NveSROzBPQ8Pc2OFIB8NcqggfT1Dtjl-nXhNqdMpsd7VHpi1T4JSl7Hqe6La-eUrilCCQdAwPTefbFUUMWjfY_qoyRKM-45NCSMikAKo-8socJjr8EiCHvEBLtejtwn_VD2xNiiJlpuiahT1_zeXRkg0dQhWoW1VXeSc5AodXCWN1ifag1ldJczs3Y6voTTuSfXE09Pna0d6Jb7_IMO4yu88-4LTgrTO91Hsfx0f0xDzD_NdxEagm-9PA42RwiVYY62sc3VBZ_kI-3vbuhH2DTW1pEvr22YH1j0Mp0soZVNt4iWlrAk8z_qzKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دروغ ارتش اردن در رهگیری موشک‌های ایرانی؛ موشک‌هایی که به هدف خوردند اما اردنی‌ها نخواستند ببینند
🔹
ارتش اردن امروز اعلام کرده بود ۴ موشک بالستیک ایرانی را که به سمت این کشور پرتاب شده بودند، رهگیری کرده است!
🔹
ویدیو منتشرشده از پایگاه ملک فیصل در جنوب اردن که ظاهرا هدف حمله بوده نشان می‌دهد سامانه پاتریوت مستقر در پایگاه در رهگیری موشک‌ها ناکام بوده و تقریبا همه کلاهک‌ها به هدف اصابت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/671215" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
کاردار ایران در لندن به وزارت خارجه انگلیس‌ فراخوانده شد
🔹
وزارت خارجه انگلیس‌ می‌گوید که در واکنش به آنچه نقش نیروی قدس سپاه پاسداران در هدایت گروه‌های نیابتی برای انجام مجموعه‌ای از حملات در سراسر اروپا خوانده شده، کاردار ایران در لندن را احضار کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/671214" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شنیده‌ شدن صدای انفجار در کویت
🔹
رسانه‌های عربی بامداد چهارشنبه از وقوع انفجارهای مهیب و متعدد که باعث آتش‌سوزی در یک مرکز حیاتی مهم در کویت شد، خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/671213" target="_blank">📅 02:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای شیطان زرد: نمایندگان من یک ساعت پیش با ایرانی‌ها صحبت کردند  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/671212" target="_blank">📅 02:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
فاکس نیوز: ردیاب‌های داده‌های کشتیرانی نشان می‌دهند که روز دوشنبه تنها ۱۰ شناور از تنگه هرمز عبور کردند؛ کمتر از ۱۰ درصد میزان معمول عبور و مرور از این آبراه حیاتی. وقتی می‌گویید تنگه باز است، منظورتان چیست؟
🔹
خوک ها : «اگر مردم بخواهند از آن عبور کنند،…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/671211" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار از حوالی حاجی‌آباد هرمزگان   #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/671210" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شد
🔹
بررسی‌های میدانی نشان می‌دهد که لحظاتی پیش پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شده است. تاکنون اظهار نظر رسمی در این زمینه صورت نگرفته است./ مهر  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/671209" target="_blank">📅 01:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فاکس نیوز: آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
🔹
ادعای خوک نجس: «نه. گاهی اوقات به عملیات زمینی نیاز است.» #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/671208" target="_blank">📅 01:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671207">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
فاکس نیوز: آیا همچنان قصد دارید جزیره خارک را تصرف کنید؟
🔹
ادعای خوک هار: «نمی‌توانم این را به شما بگویم، چون اگر بگویم، کار احمقانه‌ای خواهد بود.» #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/671207" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671206">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اراجیف تکراری شیطان زرد: اگر ایران به میز مذاکره برنگردد، تمام پل‌هایشان را هدف قرار می‌دهیم
🔹
امشب، فردا و پس‌فردا به ایران حمله سختی خواهیم کرد و در مرحله آخر نیروگاه‌ها و پل‌ها را هدف قرار خواهیم داد. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/671206" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671205">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d78523d3.mp4?token=Qs8tNw55TIW5BlAg-JQshn3IqFWupotly1aWX1aVKiZY16u5jpE-CW4c8oVqbX6h2B2iK3vf-w4pNjqtA9jfceQltYu_rbi8XhnC3069uL8ClvI-rXmlavSfwY4jB8K1zJuuvMG_WXltTntJxiw3_3p2nby-HS4F2Tzu_GRCsz5ZbNOHLuIVDpHoODqzUiG5f6OL9PoOuc0LevMt1RmDQSlW_ASSn0S-iDepf4vhDPaKnOfmXC4BhLUbFeu041QeazJ5CbuaPkfVDF9gG3ZIGj1aWrcaQXZ1b8lzbNZ7KDWEs_UmVUF0qti2FBUsrhkGD7Gn15Uc1dC53H3RYoV9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d78523d3.mp4?token=Qs8tNw55TIW5BlAg-JQshn3IqFWupotly1aWX1aVKiZY16u5jpE-CW4c8oVqbX6h2B2iK3vf-w4pNjqtA9jfceQltYu_rbi8XhnC3069uL8ClvI-rXmlavSfwY4jB8K1zJuuvMG_WXltTntJxiw3_3p2nby-HS4F2Tzu_GRCsz5ZbNOHLuIVDpHoODqzUiG5f6OL9PoOuc0LevMt1RmDQSlW_ASSn0S-iDepf4vhDPaKnOfmXC4BhLUbFeu041QeazJ5CbuaPkfVDF9gG3ZIGj1aWrcaQXZ1b8lzbNZ7KDWEs_UmVUF0qti2FBUsrhkGD7Gn15Uc1dC53H3RYoV9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد به فاکس نیوز: حملات به ایران تا زمانی که من بگویم دیگر کافی است، ادامه خواهد داشت/ ضربات بسیار سختی به ایران وارد خواهد شد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/671205" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671204">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
شیطان زرد به فاکس نیوز: حملات به ایران تا زمانی که من بگویم دیگر کافی است، ادامه خواهد داشت/ ضربات بسیار سختی به ایران وارد خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/671204" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671203">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار از حوالی حاجی‌آباد هرمزگان
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/671203" target="_blank">📅 01:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671202">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای آکسیوس درباره درخواست ترامپ از نتانیاهو
🔹
وبگاه «آکسیوس» شامگاه سه‌شنبه به نقل از منابع بی‌نام آمریکایی و صهیونیستی ادعا کرد که رئیس جمهور آمریکا از نخست‌وزیر رژیم صهیونیستی خواسته که نظامیان خود را از خاک لبنان و سوریه خارج کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/671202" target="_blank">📅 01:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671201">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
درگیری و تبادل آتش در تنگه هرمز
استانداری هرمزگان:
🔹
صداهایی که هر از چندگاهی در بندرعباس، شهرستان‌های ساحلی و جزایر خلیج‌فارس شنیده می‌شود مرتبط با درگیری در تنگه هرمز است‌. در حال حاضر درگیری در دریا برقرار است و تبادل آتش وجود دارد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/671201" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671200">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=OWsKXJs6suQc-VLsT4ZSyplSYSbMa6YmnG0sS4uOOiyO3nMhZsK5KCJ1s5MvYaOm3vbFbR85EVEbui4JotD81HXKLR0JHRQHtdvkp_EQRGSzb6pirwoAaWtM-tpURM8PLsYKnFOUv3jZTAeWB9U8UGOzT83ekcYwybUDqFoZqQ8f64kYfTZQUkzNnjhwJW3yDAFh85rO3lxeHrduHXyo6KIoi44gdvTSI9PaOKYB5MbIaMz9l4HOxP6XOc99_oSgE0iIowQJUmVniPa5zs0shOg_9dt09HNBOML9OsJxkAv4snoqmBs6yjYCbY4nVsv5qUwhMwMeG6iwOlH-y_1uLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=OWsKXJs6suQc-VLsT4ZSyplSYSbMa6YmnG0sS4uOOiyO3nMhZsK5KCJ1s5MvYaOm3vbFbR85EVEbui4JotD81HXKLR0JHRQHtdvkp_EQRGSzb6pirwoAaWtM-tpURM8PLsYKnFOUv3jZTAeWB9U8UGOzT83ekcYwybUDqFoZqQ8f64kYfTZQUkzNnjhwJW3yDAFh85rO3lxeHrduHXyo6KIoi44gdvTSI9PaOKYB5MbIaMz9l4HOxP6XOc99_oSgE0iIowQJUmVniPa5zs0shOg_9dt09HNBOML9OsJxkAv4snoqmBs6yjYCbY4nVsv5qUwhMwMeG6iwOlH-y_1uLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناوبان جانباز کنارک: موشک دشمن را دیدیم اما لحظه‌ای عقب نرفتیم
🔹
ناوبان جانباز تهاجم آمریکا به کنارک، در روایت خود از دقایق پیش از اصابت موشک تا آخرین لحظه مأموریت می‌گوید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/671200" target="_blank">📅 01:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671199">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
استاندار هرمزگان برخورد چندین پرتابه به بخش‌های شرقی شهر بندرعباس را رسماً تایید کرده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/671199" target="_blank">📅 01:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671198">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در پهنه دریایی شرق هرمزگان و سیریک
🔹
بامداد چهارشنبه صدای چندین انفجار از مسافتی دور دست در شهرستان سیریک شنیده شده است.
🔹
به نظر می‌رسد صدای انفجارها مربوط به تبادل آتش و وقوع درگیری‌هایی در پهنه آبی خلیج فارس و دریای عمان و همچنین تنگه هرمز است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671198" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671197">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
معاون استانداری کهگیلویه و بویراحمد: هیچ‌گونه صدای انفجار یا فعالیت پدافندی در شهر یاسوج رخ نداده است
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/671197" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671196">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b85d1a2c.mp4?token=jvLQedzk8IYRy5wyJLSgjs7k_hmFH6IVbFV7MBa9bXFtODIpHYDL1P-QknszPex5EGEs7gjIKzb0TTrxGXAq215B3aEOjo43USLdP4XZNdtFoQnSeohhEyWM0rOuJHESvY9Vzyc_V3q7uApLiUUx50wbhawe25P6jgcQ55RaPq_eTXBCVa_nEPxM19_-JMpP4qCpLp47KvGIQGOjtPzR-ya-MpMALqIM40P13_g34w7LPNCPNaFZKQaChdUE7AfaBy3As22_BPJVcnxk4Yol9cCNP73UPMo4EVLipmehjKtyoF3BuiKyXc3Pg8dQils8ppjJ_ItkHZAAI6Gw-j32UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b85d1a2c.mp4?token=jvLQedzk8IYRy5wyJLSgjs7k_hmFH6IVbFV7MBa9bXFtODIpHYDL1P-QknszPex5EGEs7gjIKzb0TTrxGXAq215B3aEOjo43USLdP4XZNdtFoQnSeohhEyWM0rOuJHESvY9Vzyc_V3q7uApLiUUx50wbhawe25P6jgcQ55RaPq_eTXBCVa_nEPxM19_-JMpP4qCpLp47KvGIQGOjtPzR-ya-MpMALqIM40P13_g34w7LPNCPNaFZKQaChdUE7AfaBy3As22_BPJVcnxk4Yol9cCNP73UPMo4EVLipmehjKtyoF3BuiKyXc3Pg8dQils8ppjJ_ItkHZAAI6Gw-j32UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه‌های آمریکا در منطقه آماج هدف حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در مرحله هفتم عملیات صاعقه و در ادامه حملات کوبنده پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه‌های آمریکا در منطقه، ساعتی قبل، محل استقرار جنگنده های اف ۱۸، ساختمان اسکان و سوله بزرگ تجهیزات ارتش تروریستی آمریکا در پایگاه الازرق اردن، هدف حملات پهپادهای انهدامی قرار گرفت.
🔹
ارتش جمهوری اسلامی ایران، تاکنون ۶ مرحله عملیات پهپادی علیه پایگاه‌ها و مراکز ارتش تروریستی آمریکا در منطقه انجام داده و این عملیات تا رسیدن به پیروزی نهایی استمرار خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/671196" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671195">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dko_dgPE0uOaa_0OCNUSzNCRpoN_v5_RJj52KMMfc0qa6LmRCKriU82HoFEUZesGnEOlSY9lEJ35p28ywVK8gayMqTFMXZI6vFdIGsltR-1lrlS1DH7jsN3EqDYQZp4-lwsTwVbjfFFbfkuuLv5szagdFWEajU1DEKQsYnMlbuKuqyWLwZgNIk2gSlq0JzOy1qdPxRBXinwTohvPLO5tCzv1FpF-tE4JZ1SCkPXY-v7J1n6LOz9ggzXvq8oJ-6bGVXfl4vypd5vkIIgwwElzkXV49Bc1Vq2LM2wxf3UDAg7eKJdwcpIeVBG8dCmJEclioEj-PWPHZbRKN940PY58Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا به بهانه صعود اسپانیا به فینال جام جهانی ٢٠٢۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671195" target="_blank">📅 00:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671194">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند. هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند. اخبار تکمیلی متعاقبا اعلام می‌شود.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671194" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671193">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
صدای یک انفجار دیگر در بندرعباس شنیده شد
🔹
چند دقیقه قبل نقطه‌ای دیگر در بندرعباس مورد اصابت قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/671193" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671192">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=nYlS7y2O1M8dZ1qFFrJrDah5l_lHZHmMrlseBmcbzCMhglEQ_lIFZ23IAzgqoWVOo5m5rcrtjQ4HblWJSdXE_f8jDPv21WL7DfGkvE2oALjRe9NRopbxIUD8pRJTzqp6CGLEQ0x5hEe1ORejzo_HOzRrHdqp-nTktvIIYneWPk_KKsrhXwuUgiflK1-xGqN9ceEhm72O62X60CrD0jvfAForxI-Gd70wAp239IKI0eiXiXjrejvTwJlZjlPPBEiixLSwE5wFJXlYUf_immOhmJ8QpLyWYgbK5RygCgZ1XwSESH-SCz-JEHpCq5iwaQKpYMtsSfmLcsFtFVH6RrV67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=nYlS7y2O1M8dZ1qFFrJrDah5l_lHZHmMrlseBmcbzCMhglEQ_lIFZ23IAzgqoWVOo5m5rcrtjQ4HblWJSdXE_f8jDPv21WL7DfGkvE2oALjRe9NRopbxIUD8pRJTzqp6CGLEQ0x5hEe1ORejzo_HOzRrHdqp-nTktvIIYneWPk_KKsrhXwuUgiflK1-xGqN9ceEhm72O62X60CrD0jvfAForxI-Gd70wAp239IKI0eiXiXjrejvTwJlZjlPPBEiixLSwE5wFJXlYUf_immOhmJ8QpLyWYgbK5RygCgZ1XwSESH-SCz-JEHpCq5iwaQKpYMtsSfmLcsFtFVH6RrV67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار طلایی‌نیک: خون‌خواهی رهبر شهید به فراموشی سپرده نخواهد شد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/671192" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671191">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ایرنا: شنیده شدن صدای انفجار در جزیره هنگام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/671191" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671190">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شد
🔹
بررسی‌های میدانی نشان می‌دهد که لحظاتی پیش پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شده است. تاکنون اظهار نظر رسمی در این زمینه صورت نگرفته است./ مهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671190" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671189">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
اصابت پرتابه‌های دشمن آمریکایی به نقاطی در استان هزمرگان
🔹
اصابت پرتابه دشمن آمریکایی در قشم: در ساعت ۱۲:۱۰ نقطه ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
اصابت پرتابه دشمن آمریکایی در بندرعباس: در ساعت ۱۲:۰۵ نقطه‌ای در بندرعباس مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
اصابت پرتابه دشمن آمریکایی در هنگام: در ساعت ۲۴ درست در نیمه‌شب، نقطه‌ای در جزیره هنگام مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
بنا بر اعلام استانداری هرمزگان، در حملات جدید آمریکا به برخی نقاط استان هرمزگان هیچ مصدوم غیر‌نظامی یا خسارت به زیر‌ساخت‌های مسکونی و تجاری گزارش نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671189" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671188">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
خروج نظامیان آمریکایی از عراق تا پایان ماه سپتامبر
🔹
«پیت هگزث» وزیر جنگ آمریکا شامگاه سه‌شنبه در دیدار با «علی الزیدی» نخست‌وزیر عراق گفت که تا تاریخ ۳۰ سپتامبر ۲۰۲۶، تمام نظامیان آمریکایی از عراق خارج خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/671188" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671187">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند. هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند. اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/671187" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671186">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شبکه کان: نتانیاهو، قصد دارد در روزهای آینده به ایالات متحده سفر کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/671186" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz-pxZ8-hlstEExd-szart5slYTHHzKPoUaXthJts8NermZwYiyrpXA_4c7-yjy2WGWxTORkxowJ5UoUEpBBBsZrGOfABFAXR2iq_lRg5IHke9zZFzfqlE3SEphbxvcj2Ds-9mNugg_MwG5RLz6zELVryk0mP5BEOthSnYlKMy399CgmEo4RV6F5N3zx7HHDKE-LmTRGQBvw8FsHhJ947cc_DN-JjehvJ2ow84U_U8jPeqARlJPbQR5LySLKHsEgouWFMfEwu4m4hbAfKKKQyAGBc46TVIe0VuRXMDmbpj-B5ObtFzowiziT4y7XyLHQm0JysvLKoN9UIhnVgLZBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم اسپانیا به فرانسه توسط پدرو پورو
🇪🇸
2️⃣
🏆
0️⃣
🇫🇷
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/671185" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmVkNU-l47LjmLejp5kJQTSC4KuvX5icGs_VDIAfp6AgwqUVeHwuPeX_wyqA6X7_H7pk5FswFnjMwyb-dMp0leDb_pd5lEuBKBVyvcuNP5c2gHJG2xhpMve6yWI_yekSRZIKzXuTOwwhDsdEnau3juHfuzDfD_JXRYe97QlpsfPTTe8gPWH1QGZhhttU_yhXq1lNIzcKSbiN6SHGLagXXij8s-3DxH03pMHjFXsfk_3t0UFeWgG4ADxwoNKXZvtUBZmMoNhY_AEgxV7rdVvZIXG_Dx7wFEStIDpgiAep6TIw9fI_7vKAG0OLukPKmXcZi17PxV6ZnoC4pP5FrDOQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: حمله به پست سرمحیط‌بانی در استان هرمزگان، جدیدترین نمونه از جنایت جنگی آمريکا علیه کیان ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671184" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671183">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ee44b24a.mp4?token=EM-T94YlzqA7ylzY8Lcw1-3K_R-itu9uY0KKafRxJgecWadskj3Oc8p0sp8xdUuh8g4FOLV79d29VGO_239_tAeUl29LRb7xBZ3WC291PW2R1j12fDfLhzeGDT19ED6y_YSdspNRK2J45W6RVXmcJKZu7k4ndE0K_W7fRWBnGm0u-nezazhoVNg06A5YE5UY4LyhVAhzDXOYpf0UeoCsDLbrrkneRfUDIv2r4HCV6lvHKV7vZvGcuTaOOt7gtgEw4RqXhVsNASqX_9nbuhPY4EdoAmoG-pkFyrtWVCAsd6p9LsGL9QizGJoOtWtmIz0b6bw0k-CJ4uei_UlgeMuGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ee44b24a.mp4?token=EM-T94YlzqA7ylzY8Lcw1-3K_R-itu9uY0KKafRxJgecWadskj3Oc8p0sp8xdUuh8g4FOLV79d29VGO_239_tAeUl29LRb7xBZ3WC291PW2R1j12fDfLhzeGDT19ED6y_YSdspNRK2J45W6RVXmcJKZu7k4ndE0K_W7fRWBnGm0u-nezazhoVNg06A5YE5UY4LyhVAhzDXOYpf0UeoCsDLbrrkneRfUDIv2r4HCV6lvHKV7vZvGcuTaOOt7gtgEw4RqXhVsNASqX_9nbuhPY4EdoAmoG-pkFyrtWVCAsd6p9LsGL9QizGJoOtWtmIz0b6bw0k-CJ4uei_UlgeMuGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمو پورنگ وقتی اینارو گفت نمی‌دونست مادرش این برنامه رو هیچوقت نمیبینه...
❤️‍🩹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/671183" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تکذیب شایعات درباره وقوع انفجار در شهرهای استان خوزستان
🔹
در پی انتشار برخی اخبار و شایعات در فضای مجازی، اعلام می‌شود به‌جز چند انفجار در اهواز که پیش‌تر گزارش آن منتشر شده است، تاکنون هیچ گزارش رسمی مبنی بر وقوع انفجار در سایر شهرهای استان خوزستان وجود ندارد و این ادعاها تکذیب می‌شود./ ایرنا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/671182" target="_blank">📅 00:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ستاد استهلال دفتر مقام معظم رهبری: چهارشنبه آخرین روز محرم الاحرام و پنجشنبه ۲۵ تیرماه  آغاز ماه صفر ۱۴۴۸ ﻫ‌.ق خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/671181" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی در قشم
🔹
دقیقه ۱۰ بامداد چهارشنبه نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671180" target="_blank">📅 00:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08b1FxYfoHUOcA3zJYwuxLRB7W2OoBOkOpkNFNMUDd7HKvb3bHRv9zW1aXPdwvkxxqPSrqspWLmjOtVTuz0nalAIOV4Dw43QctTLi-tETXdUS_ejbswr1YtXolbZWZh6lKlNAtJ5XOl57hMNcGTjzqT_hhFsPtQI0PLiN3fgmIT5ri_cs0ctWVI88p-eLLSn6LfFYsDQiq57-ODznjxvGBzTHkXteMHhxXm04_fACiswHvbldsuC55VUobWoKDIHAE2dr2-gDKO9MwhGQMPOvAYC3aKNCt5u6W3NiBSkdzEW3vLcWL0fz24G4HwSXYDKMrGWch42BmiQivPAGxOX8EeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08b1FxYfoHUOcA3zJYwuxLRB7W2OoBOkOpkNFNMUDd7HKvb3bHRv9zW1aXPdwvkxxqPSrqspWLmjOtVTuz0nalAIOV4Dw43QctTLi-tETXdUS_ejbswr1YtXolbZWZh6lKlNAtJ5XOl57hMNcGTjzqT_hhFsPtQI0PLiN3fgmIT5ri_cs0ctWVI88p-eLLSn6LfFYsDQiq57-ODznjxvGBzTHkXteMHhxXm04_fACiswHvbldsuC55VUobWoKDIHAE2dr2-gDKO9MwhGQMPOvAYC3aKNCt5u6W3NiBSkdzEW3vLcWL0fz24G4HwSXYDKMrGWch42BmiQivPAGxOX8EeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده‌ای که کامیونش را وقف برپایی موکب رهبر شهید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/671179" target="_blank">📅 00:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671178">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزارت خارجه: دیگر چیزی تحت عنوان تفاهم‌نامه اسلام‌آباد وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671178" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک برای خرید سمعک جوان معلول
🔸
بیمار نیازمند حمایت جوانی ۲۰ساله است کم شنوا از خانواده نیازمند واهل یک روستای محروم منتظر مهربانی شما عزیزان می باشد
🔸
هزینه خرید سمعک ۱۰۰ میلیون  میباشد امیدوارم با کمک شما عزیزان شنوایی وصدای زندگی به این جوان هدیه دهیم‌.
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید.
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در تنها در کانال تلگرام خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671177" target="_blank">📅 00:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMZ59aXoY8gVJeDou6pJUvqIwr0WEq62r5hGQWgG1nTXTvmhVetsjlWv8nq-NOZR873JZkfRbmlkE10v4zndPLtIWd3_7xhggmGBg4_ahhlQB61VQwccttB82R3EusuRAQIlEE1K6jCvaigZpl148Hi-yeR7F3QoqXdWh-Q3cNdXiioIYPBOfqaMtTUcC8JvVr30HejJjztzE7iTNdCqdSPP4wmsvOq9FtLXU-_WkZae4fwgTYddVhAfztnKAxNIq7BxJagcWxyim70Vb-2LcNgs3on2Sw0t7ao9QXvo1o77Yfzqml-mZuqQW2Jxbc-TFMErHZOUCRAffmniB5OcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/671176" target="_blank">📅 00:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e812ee880.mp4?token=Ffc9lkwBuVuJLaRwe-2xGXzxwk_wln_w_WOhcDDKFOCN9UMA6QmN9tNYD1zo4mfGTXQl-Mu8Jg9QVHJA_6N6gIBkRfvaTtdsVvjaRyVopyPZ18ALDfMUZkb9OyzQpm85yGaOSR3o6vw5RkjGg913MMmUokFfCJVpArwaXkwDdCBm18HLCRrRTC8u3TY27mhuEUXcRA9ZE3nWmhp6W8RBm9MhRXJy01E3sQlgJ8nQkJ4kfxqryHpZsjBvNp4R1M7RSBtRvMbFfoalQm5iuYtXeB3Zo4MH8tchO5OZdh5ps5qLisOpto24S8-qWBmZK8C1331nFyu32ygZcIXAtl-BbRiSFVKru3O2AoNXvCenxzjiNVS47ZOHbo3Jam6COHEqa-eH4kBWLzPm5cVHftbpPnd6NiGyTT5sFxML-NUzZDbpQifx5igvkOPXe6H6km_9CidZUw1mBFEhWZeEQjXa2c7QdWWnWallAgAs0xPlX9AfAr4TnWbQqb60qQdVs7OiT1Jm25m9zVX7XhP3UPv1TyK-HmmoVYsmx0JtKxWJC_TxsjYVfrGjX287sThR3TywU8WXZQBZP3KQe8zFZphAra93PvEjti1x8Rrr62Jo17s4-hn1_Xnir1AMqhbPhQmZIsNYTQlGn1DhUKoBFCuF0Vy2qj8yq57y7YRp6YJ5zG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e812ee880.mp4?token=Ffc9lkwBuVuJLaRwe-2xGXzxwk_wln_w_WOhcDDKFOCN9UMA6QmN9tNYD1zo4mfGTXQl-Mu8Jg9QVHJA_6N6gIBkRfvaTtdsVvjaRyVopyPZ18ALDfMUZkb9OyzQpm85yGaOSR3o6vw5RkjGg913MMmUokFfCJVpArwaXkwDdCBm18HLCRrRTC8u3TY27mhuEUXcRA9ZE3nWmhp6W8RBm9MhRXJy01E3sQlgJ8nQkJ4kfxqryHpZsjBvNp4R1M7RSBtRvMbFfoalQm5iuYtXeB3Zo4MH8tchO5OZdh5ps5qLisOpto24S8-qWBmZK8C1331nFyu32ygZcIXAtl-BbRiSFVKru3O2AoNXvCenxzjiNVS47ZOHbo3Jam6COHEqa-eH4kBWLzPm5cVHftbpPnd6NiGyTT5sFxML-NUzZDbpQifx5igvkOPXe6H6km_9CidZUw1mBFEhWZeEQjXa2c7QdWWnWallAgAs0xPlX9AfAr4TnWbQqb60qQdVs7OiT1Jm25m9zVX7XhP3UPv1TyK-HmmoVYsmx0JtKxWJC_TxsjYVfrGjX287sThR3TywU8WXZQBZP3KQe8zFZphAra93PvEjti1x8Rrr62Jo17s4-hn1_Xnir1AMqhbPhQmZIsNYTQlGn1DhUKoBFCuF0Vy2qj8yq57y7YRp6YJ5zG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر حوزهٔ مقاومت: نباید بگذاریم بمباران هیچ نقطه‌ای از ایران برای دشمن عادی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671175" target="_blank">📅 23:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671174">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
شبکه کان: نتانیاهو، قصد دارد در روزهای آینده به ایالات متحده سفر کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671174" target="_blank">📅 23:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671173">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزارت خارجه: دیگر چیزی تحت عنوان تفاهم‌نامه اسلام‌آباد وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/671173" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671172">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54e28773c.mp4?token=EKS5V4QpFqBZMJpprEvRZXCh4y6irn4aDHwdHKYN5QxAzdhBr5MCoFlNmln4xE_nNUxJXVUSUmJThTVimismxjbFKGpPU03NymQQj1T7HjYmFvuzN-4gKc0KELOarzluSHcnQs_r9rNHFJscvDRKdORnyJzs1z6IAdKNR74xcre2FhXDDnBMAuTrAZZh-Ppp8re9hvAjqKlgLIp2i9Xg68z8ymvBsDb_icyu8NIcMadqyPB8m4jklGk0Sltf81nG0k7V15RAH0cVzp3rAWvwCItYRdyx_Z8Uh-zcyB2XBzNYgNVkcTqpCf1y3klOhpplBTxxni9FQsDOnGhsXXiJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54e28773c.mp4?token=EKS5V4QpFqBZMJpprEvRZXCh4y6irn4aDHwdHKYN5QxAzdhBr5MCoFlNmln4xE_nNUxJXVUSUmJThTVimismxjbFKGpPU03NymQQj1T7HjYmFvuzN-4gKc0KELOarzluSHcnQs_r9rNHFJscvDRKdORnyJzs1z6IAdKNR74xcre2FhXDDnBMAuTrAZZh-Ppp8re9hvAjqKlgLIp2i9Xg68z8ymvBsDb_icyu8NIcMadqyPB8m4jklGk0Sltf81nG0k7V15RAH0cVzp3rAWvwCItYRdyx_Z8Uh-zcyB2XBzNYgNVkcTqpCf1y3klOhpplBTxxni9FQsDOnGhsXXiJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم اسپانیا به فرانسه توسط پدرو پورو
🇪🇸
2️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/671172" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671171">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBhoHUHZjj7g8LEIgd0kFyjRBxfkNnTB8AICaopLFmJ5YEjBLh6yzTFl3tNhP30YFIwPq9yzWM3E_VzMdFdVJaBMrCJSV4EoCmE3IlGgiuom9K3g94iJrB1w5Pjljjj6m8BmAEAZKcblHs_RFnlvxK-mOJnxaJc1SjOZlz7ipWUt8CZOkD9RzBVPmFMdzhAkdCeOKX_tpkAWeOE9m0vbgJHAF6tfcE57aje3iK6yRiqgHhJAbVHGLKLnxalEu8s3nOw2H7qUDVT-_XedbVVJzLpXMgrcDEPgC_Uz-PDeCzbQICAM6CquIkozZJr5arCHK3S5sJZ8x7RpPYYPq50tRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انسان خود رأی، هلاک می‌شود
🔹
امام علی (ع) استبداد به رأی را عامل هلاکت و مشورت را راه بهره‌مندی از خرد دیگران می‌دانند. مشورت، که مورد تأکید قرآن و عقل است، با تجمیع اندیشه‌ها خطا را به حداقل رسانده و نقاط تاریک تصمیمات را روشن می‌کند. خردمند کسی است که…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/671171" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671170">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای سنتکام: محاصره دریایی آمریکا علیه ایران وارد مرحله اجرا شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/671170" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671169">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شنیده شدن ۶ انفجار در قشم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/671169" target="_blank">📅 23:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671168">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تصاویر شلیک پهپادها و موشک‌های خیبرشکن و ذوالفقار در موج سوم عملیات نصر۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/671168" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671167">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای سنتکام: محاصره دریایی آمریکا علیه ایران وارد مرحله اجرا شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/671167" target="_blank">📅 23:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671166">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f525d7e01.mp4?token=Ztwnibb2l2gFHJiE1gwHFNtYJMaTyQ6y-oWCkkj--7rhG0kqS3tBg30r8DC7JCIquWFRzwGrFhwaRQ-RoWuTDmke57JB9_cjVxq1zboiK_iL8qJ7qcgxtgyDs7FtCfh30OQtHqlICN5XXP8HbKo_3GvNwKbxxBR0bDBR05CqlkKPtHBluXD-SlL6vtCZF04PdLr2w10JSLHeU6GFn59CpfjLIoH-KDXoZugW771848euKKMHyvGU1JkCZOy5cPnP2vDNHaQLtr7Hh6y4uH-6Rkug-ETwNYB_jAxTR2uafpCb7-jRjaW36tZg5SC3duqUVzNNE9bLe9RaKM3yrBTOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f525d7e01.mp4?token=Ztwnibb2l2gFHJiE1gwHFNtYJMaTyQ6y-oWCkkj--7rhG0kqS3tBg30r8DC7JCIquWFRzwGrFhwaRQ-RoWuTDmke57JB9_cjVxq1zboiK_iL8qJ7qcgxtgyDs7FtCfh30OQtHqlICN5XXP8HbKo_3GvNwKbxxBR0bDBR05CqlkKPtHBluXD-SlL6vtCZF04PdLr2w10JSLHeU6GFn59CpfjLIoH-KDXoZugW771848euKKMHyvGU1JkCZOy5cPnP2vDNHaQLtr7Hh6y4uH-6Rkug-ETwNYB_jAxTR2uafpCb7-jRjaW36tZg5SC3duqUVzNNE9bLe9RaKM3yrBTOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر حوزهٔ مقاومت: راه درست شکستن محاصره، حمله به خطوط انتقال نفت به دریای سرخ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/671166" target="_blank">📅 23:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALEy2COp7euMnLbM8YYEHSLg4Ry9jXQGd7vIdu0C0S4lDWBgtu-SyERsHjAC3u-JioFNmWXgrwzC1l5QHEDGItt9-ehSp8Arh3TgavO5jADPTAOsDgnhjDwKlHNonHEYaZ6EyAIh08yu3kQ7ZrwE3UwbaTOSm0raalzOn2OznLTnGvFLwaBoqr4g9mEWmAY4I3kb5vkuEEnVaI2qoPeO0W0l43T_SAfZu1rvwgkFpzErfpZGb6aZdZKaikrJbiLy1_l4sMTs4mF-GrxeF5vDGkpm5gLB6tqSI_LYObWz_57QQ4YgnXB1onXqKeCV7MjXYO7y88As77TQ09Tepx7N7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSyFRv9lU7BXSSC0tWoLhEQzycA4v9uU2tMBPTI1Txudw7XdTEZE__mV3MVkWvTA_0V5Iu0DRPgB7oXIKchk6vVnFpv65QjL6aKQ12nXbR2LHpGpAAukzY8npYf9VI2myeNa9A6_5xFWcaroaxX0KiSdwfU4VD7r6ENgHXXXDgOCRAMQmEimBR6xRdenAFilk_psvjUcfBcLRsd8CMUi2hPpmEHxwnjDF3Z0HVyqVGqYevSOFu1rr1q8iVD6p_yobz6kryYW5pc0H86FACg8wRB0GE0KCn0kqr8A3vMtZWljcUO8P22yRUt8GS8cTiP_i5z54jLHkiFx1p5xJg7HZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFBTApKc9KnhVgVIxh011b5fjGbt42YC1-Zl_eCfJEmU06qa_-Qk7Y21uVnomg_MR6tStCX_5FBwojIQ6SFfBsaBeP6oiRLOSzMhyqqBa3YRCbs7P4Rmozed5m5MDHAb1YDR0cZYbORwf-q2VxbZ3FbfUQPvH7TJ9pe_ht3R4THsf2iNsXpru-IvQWTp-MJ5QYgkyjizahaFY8s8KJxMcij85c3_bMlfMUWLnOdxb0pVG4UZWOg8LqJdfNSL4O5UrU9KWuzF8mA-TYdKzeGUpIrCVdwOgvJ6PWw24RSTKfMjFiF6Ed6Kc-z2b9lESVar2WGEM4lTikTxqurB9R2Pmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYJvcP_2Kf7OyPqcPqq4pbkQaWDflzTNQfvl2y-JDGrrzM56Iaz0JLk78q34NEwbHeeG11YRlDXxZOwwbcUA8g9Hrz3nMy-wIznBs98n3xdpyQ7BUHZ97oXZpTkM7K7RzmI47RGILDxvitoVxZ4KU0Q1fzqGcudp5mYPux-eijlFyPfiGrfkXchCBfLlJxVQwQC1AtwheyIymLifDHUXt_HRr9PweGry_V5XpCg7ac93w_z4E2IVVEixePJhvknyHNnx7-txkUalZWcA4Jc0D4ClL594mo_VVOsct_0yl3bw9UXQImDyJ9DV-nzOXEjVWVnm8Y-C6SJfxg3RKgnorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qV20LODvYRxr-Uf3PgeXKf9i4sTQEWiqAUR3MIDExwOgWu6kFj74hdYB_ls2LjThoGkYB1iABPjH_cw17eogz1ZQDpoHDgAOj2dr5RmxxXKGh9DzWosv6662NKTpRV9Pt7Z1MIXFVZ_3rziLVK5bodpJOneXi-QuVzRWA7WGZ_AHdIXw9g6hT97UIdfk4zGnD1nDG5XVaeDhhXrkvlgwgqCJkjbB_zMmqiLNpNUmxBVhw0QoRDfCF0zB3vRnlva2Kn7rDJji5L9kYKQ73NdYUFVsizRiUvoQs6fUVy4xh81S1quOxiGlUEULqmHV94g2M4bxueUTCzbJCjT58RfZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frVY-vdTyAYKI-FQpPAPxrQJ3YBwp0bhQLLJaBDvv-rztAi1NQWEA52Ld2nOzzXTGYQ-iBF9hIff7fAF2VDPWCIJbHdLWJJ1jERTtwIUebQ5pFxSh5Cgf9gCx39dN9NNwmAF4dcbarUURzPsgjKREb1GPq-UQU8two48xiNQb_89NtAbpQ2m54e3Elf09W0nDgq0K9tkHpBWSGKl7p_mHS9LU4Yz-4qzx8n9An8mC-FVWjBTM8L18Dj6fajcY9xOi3hVYxWTQojW5akiDPupZ4D1NhXDgYmvyj0WJ69dWw8qm5fH_1CQm0rEJ9tpUc9Cfgd6fSXnqKgN_KOdE0YCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBLWuXSatzMuMdjWtZoVx5Tvv9KLFOBzxuM9MsW3vECxJ5bjN2duRuSz-28JMng4z7rIu-jGm56_zj5_YcUYHpVDuqwa8JEmCmPfxI_Lfa9Zlt4fWLwVAQ5_XUs0oOlduehiPmCI-LoQLmaA75zJcJvyXOzLdOGWUTiDZLj7jHrTdoDQQ5WHuUS7WvCNpBCUT0O0FqLWSeMG6BFea5hG6eikgdsZ7NNGVWrSVnuvgSFvu-apy-6fajIWYWE7jmLEIzuk4zi6bs_hhhoWXiid5-od2sGvPXt-46eTw0TYln5XuSNjA6TRePo5umQay3H1t5N8IJjFnf6EegtsEQZFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqsB2DtvaraWIrzFYEoRkCBQEIuBFAGGbJObBigsdJNV59bgWv9LonqDi5uazfMGR9Kd78GlL64YNvE_XhbWBpp4XmjUwuxvQAMo_aYOn62zG19vXtr2H9Mvw6wzobuCUsvvHSVoljIVz05HuwOSv4_5BdrnC7q8FZJPEE6bb3yD8icboXnuidCg7i1cDXOrnn74TNiyjXUJ7eXuaiDvcrJ_fV7YcaEuf_4iCD7X_MyJyVdCVa8wN_ImJJ-41FEPJ6q7nZUPA-T7NdPjNcH51LvI-vkTrJVJjiLlH6DYd2DqOA-eHMwsr4hk0coD2zFv2OSRBdzUww0XUVdj1HippQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llVdkKnPb333vC8x7SP3SYNG3px3mgwT9b25QzpBk8UiZLPv6UaT9D1-Zvvi_nbtox5fCaRQW9ArLeEP3h6v9beZ6sw8NfL67eYuqajB680h2SwcT-6NvEFZ702Hh9Z-qpEf17x6IWG9HbRMsLr7yZTtD3LXgdb1IGguGSxS9CWmehGPIjJ95vRzkoJLWG1TgfmwlH-i9-hK0exhEGvQBJ00D5z89jtujSa88rdSS6fkTPfxyiMLsidwHfWDn3GwT6f5yUJcwk9HAHsBVi3heFhP0T62f2wDLbxt97FOojZQ2In5duwDMUlvzjftdjw3INzMJIC18BlNTaY4ZmN3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YH6wXOrLSldcieKFU1bBLSXxo7-2bUsjuUBRDE1_TbYLTjCHybE4YxuqWhqUCbqJbP99oNLOfyjpoahBJT2EKuXfeCZSg9ZZfL46y52Wn8TPc1HKkCAJMfQWMRj0ijmZltzh20QBwpAg1mJJHxJLIcbiubDbF--ls1S2jqYQC71O-0tqrZFsvEdCk4W_Y5S4dV2kMTljZsaCBybjkFowM-F1ZUxb-Ife8jIYW_SmB3E046fk3fVMJWxTzLZj4HrTsDmmwzNcVL2l-QE8jjL9FGxC5FY5H2rRbMoP99K8Xp2sHVQeYyLHwZJLIXkZEdFazS71LSBH0tkvhrdDZ-aCHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منتخبی از پیام‌های ارسالی مخاطبان خبرفوری درباره قطعی برق خارج از جدول زمان‌بندی
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/671156" target="_blank">📅 23:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671155">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار مجدد در اهواز شنیده شد
🔹
در قشم هم صدای چند انفجار شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/671155" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h50hGrKU7esqDEMtSKtnoXHm7aKpmQ000lNjbAVTCK8t5pXIDW5MRoyh7bv0SIeTEOSrE6jUwnaFkAgsw9_X1C4qQ7oIaeSD2C5iopzD4RxVcbY0aerPBaKz_fZPUX21kfp_QIYLW_aHGcHfaS6gp-r3QxUl0n0hcyc9KScu95yY5V7nzFklVskQbiIvddEyWDvFe5dbiNIa0qeCz5jM-4q3ctuGkYBLpmZBT9Y9TaFDAIVUlI6mgTfp5uql4LohtG-LvMmv1xXOXah7bAjYA3hoFmFM3jG0Wb6RJ-JqUu2TtgAZaf1aY-KolxkqEnoNhJVSvMwX6Ygw5kqnbpEp8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا آمریکا می تواند خارک را تصرف کند؟
🔹
حمله به خارک نه از منظر دیپلماسی می تواند مثمر ثمر باشد و نه از منظر میدانی می تواند عملیات پیروزمندانه ای برای آمریکا به حساب بیاید و احتمالا با شکست یانکی ها به پایان برسد.
نظر شما چیست؟ گزارش خبرفوری را بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230409</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/671154" target="_blank">📅 23:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
اعمال تحریم‌های جدید علیه ایران
🔹
وزارت خزانه‌داری آمریکا همزمان با آغاز دوباره محاصره دریایی ایران، تحریم‌های تازه‌ای را علیه بیش از ۵۰ فرد، نهاد و کشتی به بهانه ارتباط با تهران اعمال کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/671153" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
کوه کلنگ که ترامپ تهدید به حمله به آن کرد، کجاست؟ / تاسیسات مرموز ایران در قلب زاگرس
👇
khabarfoori.com/fa/tiny/news-3230219
🔹
ادعای جنجالی یک رسانه اسرائیلی: عربستان به پیمان ابراهیم پیوست
👇
khabarfoori.com/fa/tiny/news-3230163
🔹
آیا آمریکا می تواند خارک را تصرف کند؟
👇
khabarfoori.com/fa/tiny/news-3230409
🔹
احمدی نژاد علنی شد تا نشان دهد در حصر خانگی نیست
👇
khabarfoori.com/fa/tiny/news-3230311
🔹
سید محمد خاتمی: طرفداران جنگ همان راهی را می‌روند که اسرائیل می‌رود
👇
khabarfoori.com/fa/tiny/news-3230351
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/671152" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی در سیریک
استانداری هرمزگان:
🔹
در ساعت ۲۳ نقطه‌ای در حوالی سیریک مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
در حملات جدید آمریکا به حوالی بندرعباس و سیریک هیچ مصدوم  یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/671150" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671149">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تکذیب آسیب به مولدهای برق کیش
مدیرعامل شرکت آب و برق کیش:
🔹
مطالب منتشرشده درباره احتمال آسیب‌دیدگی مولدهای برق ناشی از سوءبرداشت از مباحث یک نشست فنی و داخلی بوده است.
🔹
هم‌اکنون خدمات‌رسانی در حوزه آب و انرژی در جزیره کیش بدون هیچ‌گونه اختلالی و به صورت پایدار در جریان است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671149" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNJ2yjuqtxD8o3onRv65DulX2hoTJ-WE1fx5NV6U0oGJIb5Cr-TWikZNckU63Q9MiWq0AOMhew90g36aYWKBc6BYjy9QX0eBj1N7-epve9nAaXzDNGZ37MJaeN9RYd-ibjh2FQksVlNIWsXulCZWHI_0GHKEP8gKGcj3WjIKEQtwmqlaO3dKesM2GoDYpRxJkXLDo93KpYT3hltNalWOHmjBs2gNP4d-F103Y8jOyxLv9rcvQVNR67HDA3NVtniLZKeOmPMho0mjkb7O6iY3YC_JlwbecTRcArQH3xxgyg431ntGBb6pPoYTnHlYtcPSXfWzJZy2OA1nlZvIco8NDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛞
وقت تعویض لاستیکت نرسیده؟ یا فقط داری ریسک می‌کنی؟
شاید فکر کنی هنوز لاستیکت چند ماه دیگه هم کار می‌کنه...
💡
⚠️
یک ترمز ناگهانی، یک جاده خیس یا یک پیچ ساده، می‌تونه تفاوت بین یک توقف ایمن و یک حادثه رو مشخص کنه.
⚠️
❓
چرا وقتی می‌تونی با هزینه‌ای منطقی، امنیت خودت و خانوادت رو تضمین کنی، ریسک کنی؟
🔴
لاستیک‌های اصل کویر تایر
🔴
سایزهای ۱۶ تا ۱۸
🔴
۵ سال گارانتی
🔴
قیمت رقابتی و مناسب
🔴
خرید حضوری یا ارسال سریع با پیک
📍
تهران، بازار سرچشمه، پاساژ رنگ
📞
فروش: توکلی
09122386439
📱
اینستاگرام:
https://www.instagram.com/youtabnatanz?igsh=b2YwN2E1Z3FicmQ1
📱
کانال تلگرام:
@youtabtire
امروز لاستیکت رو عوض کن؛ چون امنیت، چیزی نیست که بشه به فردا موکولش کرد
.</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/671148" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671147">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آمریکا دور دیگری از حملات به ایران را اعلام کرد
🔹
فرماندهی مرکزی نیروهای آمریکایی موسوم به سنتکام اعلام کرد که ارتش این کشور دور دیگر از تجاوز و حملات به خاک ایران را آغاز کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/671147" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671146">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دقایقی پیش؛ شنیده شدن صدای ۶ انفجار در غرب بندرعباس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/671146" target="_blank">📅 23:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671145">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbioUxmp5tyse7N9-2RP3YqkFErIMwX2hxcG94BvKIwGVQa2lHD513HxDMzga7HjRXbpvJ7p25bcLnE3Kv52m-fCOOJioiwCOUtN5qqBuP5k2tko5tZvtaZqN801kT5CJtGzckYTPK_2Eysyp8QYoRMLDSjvhWTCAnTASo4_tkoX2m1JI_Iu11vDNiSxEMgX_X2MCG6MATfiO4zk3azvTFz6NZP8a_y0kcy3dA_dg3TY5ZfCfYy5lyRW6MdwLq-J7MXzNSiXMrHf49bUJqqxmVUOjkZsRvXTUZrGnetAuXV-P9_Annn8VK8XAEWNQmk3lo-z-9WJQ9xOgcP10lzZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران بزرگ‌ترین حمله به بحرین در طول جنگ را با بیش از ۳۰ موشک علیه دارایی‌های ایالات متحده آغاز کرده است، از جمله موشک خرمشهر حامل کلاهک تسلیحات خوشه‌ای
🔹
انفجارهای مداوم و سنگین دقایقی پیش در سراسر بحرین گزارش شده است، با ساکنان که از لرزش شیشه‌ها خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/671145" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671144">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب.pdf</div>
  <div class="tg-doc-extra">10.4 MB</div>
</div>
<a href="https://t.me/akhbarefori/671144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تاریخ مستطاب آمریکا؛ روایتی متفاوت به زبان طنز از تاریخ یک ابرقدرت
🔹
تاریخ مستطاب آمریکا نوشته دکتر محمدصادق کوشکی، با زبانی طنزآمیز و نگاهی انتقادی، روایت رسمی تاریخ آمریکا را به چالش می‌کشد. این اثر، همراه با کاریکاتورهای مازیار بیژنی و بهره‌گیری از نظر…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/671144" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671142">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-X9jPTBRu5AkSIwubytgzyt3YEbrTIK3Lh4E8dRgpEQNb_Jt2PHMOLKBG-SkziLrHiUu0OR46woWNQZBRapnbCH6PDoi9xqMf04wpLw9Nf5tta9UuFAd7Q2FSd5HknhRsvCrdijU23FJCLi5laaD6RQ87-bWo9rBJWL89LQmD7HGq-UKmawno3C5CfZUy5XgKmzQdWZ2yosJhpL5F64V2H2MVdGQgyQkc8dQBJ84qNqt6vNpHM-_s3JmxGVeETfCV46FCZR4Vo8NybMjs2rid99MHT_BLN5276DkSOUyBrbye5KbJV_rBXBDxqoyr2UQ2rK93y4VmLJeEp55Q0naQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tynl5DyIIcfawj3TQHNR-BfjdsDMXr42s1qW8ixkb8rhDFb_5iUUSz0WXtalrDIOnk2vb65NKjWcYcXQ_eFdJf-CF0vqPZYCDmezSh9ovawFQ3IXeokhv_YKAQ5LrAqW_KX-9KjuvNJoIuEMVBa4k1I6_aI2KJslQFq5m3d466j5NI90DDvKjYh8Iwxx-NjWyzBV7JdrevicTzEdzESjZP5MQWU01aOmXbgl_aEA4AiH45Ni58fm4yHuwv0wlVHfXnk9VWbd9Huc-JQfV5hSbuyz6EZMA-5tEiHyS97oCwMZ74vXKN-1Mhn17zaxKhEYrqO-G0DMdKvIZJplVEsGbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کتابی که نگاه بسیاری را در جهان درباره زندگی برای همیشه عوض کرد
🔹
«شازده کوچولو» فقط یک داستان کودکانه نیست؛ سفری شاعرانه به دنیای عشق، دوستی، تنهایی و معنای واقعی زندگی است. آنتوان دوسنت‌اگزوپری با زبانی ساده؛ اما عمیق، یادمان می‌آورد که آدم‌بزرگ‌ها چگونه…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/671142" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671141">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac602c29f.mp4?token=VAJo3LTCzIEIFfu5F_fO5cPSYgz6pY7H-_Et6y8tzzwkdF3kBa5VF77EWWLF3csX6XmxE2ONfnAc6lUTfqpMcmahdHGAKfWCY_V_8TKWMWOhNPkwdAI4RaNyL0IhkFGShiMkWEIzEZNDulScHHUhdUHbt4Mz1Vqf1y0f02RWlwH_UAtUuWfCCYrCRjpOFOPVAIYqOyDiztWCxxVg-W6jCCzI2vBnqsVlH31FDezpoxsvaO-aCTVxes7pLjxKvRNw7OeNDAIFkPUQHNcYjnXI47DP6yb6Ym2O13zT8-O_FwCdDw5eZnzFVDj2qOcmNlGhujEZKzeF6DHRjHYJrhyZwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac602c29f.mp4?token=VAJo3LTCzIEIFfu5F_fO5cPSYgz6pY7H-_Et6y8tzzwkdF3kBa5VF77EWWLF3csX6XmxE2ONfnAc6lUTfqpMcmahdHGAKfWCY_V_8TKWMWOhNPkwdAI4RaNyL0IhkFGShiMkWEIzEZNDulScHHUhdUHbt4Mz1Vqf1y0f02RWlwH_UAtUuWfCCYrCRjpOFOPVAIYqOyDiztWCxxVg-W6jCCzI2vBnqsVlH31FDezpoxsvaO-aCTVxes7pLjxKvRNw7OeNDAIFkPUQHNcYjnXI47DP6yb6Ym2O13zT8-O_FwCdDw5eZnzFVDj2qOcmNlGhujEZKzeF6DHRjHYJrhyZwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به فرانسه توسط اویارزابال
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671141" target="_blank">📅 22:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671140">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2HAMQKjNvJ066XnKY1wQygvgmmAK6SpcCgQV_ZR3WgXZykJC1JAxnRy6qK2os7bMn8wIpuUC9ftGz2loZCvcXhc5n3JPQUQrrekYHkYg8eSuw9Ovya_Wh0UKBWdCNiQtPJR60fjB5o4Z7ZonJsGUYO4_h-tIbwMcgs7dIQleKVTldqqFTNHMH_XgNqCHnaKfiLt3qnPgh5iIwQ6EhFs8UJs9xWFqM0d3yfXVKLeupRIoBbZAR8bQ-7gm95VT52nbuG07Sv6iNkwAR30yVYpy1t_Gt_8rqxHbuZuXhTKH9Zql9MBoKwrlMH-sMjcXHZeGv8klbdl4DJ0X1pnAMQXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا «آنگ سان سوچی» مُرده است؟ | چهار سال است کسی او را ندیده |‌ راز ناپدید شدن رهبر سابق میانمار
🔹
بیش از سه سال است که آنگ سان سوچی، رهبر سابق میانمار و برنده جایزه صلح نوبل، در انظار عمومی دیده نشده است؛ موضوعی که اکنون به گمانه‌زنی‌های جدی درباره وضعیت سلامتی، محل نگهداری و حتی زنده بودن او دامن زده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230365</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/671140" target="_blank">📅 22:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671139">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d35debec.mp4?token=RxCpVLWCcrfFynGLtyoHLGSVUVsq_u8bnRpkyrjIztO6MFuxuUfJtR47mHfHaVaVdSd_yx9ok2r4thZW0Hv069Kce_OTangVYJ-Utf8eW1vs5BAdA6NLMFqPhy7Ft1Jk4oM_rp98V2Fev3XqkGX16sKomM3OJcPEtLrd6mLUyp7ff1C9jwNYWS8H6jrVHoOasOxDlxkOCXMS2XfyN3R6Owg5yyT093HtbbN4q7FsbTTDyKDmBXdb7_Pajk7l4cTrofeXYgxRMbvwXq5XLJ-1QTzx42RI5J2WzWysYUnzzvo5PEE2NSXuzXGYIoLV3Q4ah3df663mZtMAX99_4Uit0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d35debec.mp4?token=RxCpVLWCcrfFynGLtyoHLGSVUVsq_u8bnRpkyrjIztO6MFuxuUfJtR47mHfHaVaVdSd_yx9ok2r4thZW0Hv069Kce_OTangVYJ-Utf8eW1vs5BAdA6NLMFqPhy7Ft1Jk4oM_rp98V2Fev3XqkGX16sKomM3OJcPEtLrd6mLUyp7ff1C9jwNYWS8H6jrVHoOasOxDlxkOCXMS2XfyN3R6Owg5yyT093HtbbN4q7FsbTTDyKDmBXdb7_Pajk7l4cTrofeXYgxRMbvwXq5XLJ-1QTzx42RI5J2WzWysYUnzzvo5PEE2NSXuzXGYIoLV3Q4ah3df663mZtMAX99_4Uit0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت پهپاد آرش ارتش به صنایع معامیر قطب آلومینیوم بحرین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/671139" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671138">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcrZT3Ws-KOqDgVUH4h1jEDeAhZeN2N4Lx58xOGa_pvwOflW3b64o98RFlV35lNzaHiHrF4kEyUFz9yus7RNmyQjg9I2iZs5BdIGVPNIfsxowvNS4e2CN7aQ_jaKwUYPD_ahoPAXtR3pp9F5YChqeM3Z5c4HCFh-dW8F0Itag0fCGNsKINhqxnvrSfO-VZpiuL2SdCTWEYv0fl7-a9TPyjCwhjJ0otkptgx8DMlr8KV7rx-xrwDXSmk35kpUzD08oyD8mN-iXeaUAuqPJmcilF-qMy4DKWaDQVjXLw13MuIE_dR7VS6-cZ6e1qOxvLvu28X7hoPY4T7Eds-UBAVn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاومت عراق: اگر جنگی علیه ایران آغاز شود، مشارکت نیروهای مقاومت فوری و قاطع خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/671138" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671137">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
منابع غربی: تاکنون به طور تخمینی صدای ۳٠ تا ۶٠ انفجار در بحرین شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/671137" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671136">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Qhy1rDLN416rfOBPbOmhwBq8SEmfLQK38smMPmVIeJ1H9_AYj2A0Td0h0D1ZPSQyfX-j8MuOuWiUWR145pzxGHYqe9i8yEiOiaedVUYxipFtYrr5fiiGT1DlORFzn8t6uLIGm1JTOPX1BAwa5KnhGmzWBFV33an3Ng5mpTKltpPbTAcQab8Gx2ybX1OM9g4gQM2rAHk75kDYiVYoqLRocdDHBfSFIJ536CbhaCX5ItdpmxSIg4G_WESNSNNxqAoe_iFoE-vdguHK_Efh6jdT8A6ynlx3o0Aa8AKhVIBsuJ6wx_Q2Eszpvr-7Je4LrX1l8aImN8Zgsx6CL02FjQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: آمریکا در حال تدارک حمله زمینی بوسیله یک رژیم عربی است، ایران به ارامی برای جنگ بزرگ تدارک دیده است، حمله انجام شود این کشور عربی به پایان میرسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671136" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671135">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5lHZ90LLGEzJx2sHj1dFqahoOG6szaNfUkR__k1OO-4gLjjM0bT0l4KeuH4YpxPx_WoDjcKG-3Oswa7PMwidVbHiG_HksJMjSxy88vf8EQtaEU7CK3OPljaiRM_0vPhpKq6cLjRl4TBPC51MXH4FcU--6NL6E4ZPHN9CnhZbttyZg05WMOtmc_JJByCAnDM6kYuK3zhfXOjHoHdwZVfAg2MyPZSf12ozRGDgXUGv1EfgOJOYci3-BhMcAxhou1P0V4_bxpMNawsPIwxSetzl6jnvXbJspBdh8pl2wlwEdWRlxIxA-nY5bGSn-OkeUfc0z-2oKD-GgBteswSvxue4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو فردا به وزارت صمت می‌رود
🔹
عباس علی‌آبادی، وزیر نیرو، فردا در نشستی مشترک با وزیر صنعت، معدن و تجارت، آخرین وضعیت تأمین برق صنایع و راهکارهای عبور از ناترازی انرژی در بخش تولید را بررسی خواهد کرد.
🔹
علی‌آبادی که پیش‌تر وزیر صنعت، معدن و تجارت بوده و سال‌ها مدیریت یکی از بزرگ‌ترین مجموعه‌های صنعتی کشور را بر عهده داشته است، از ابتدای حضور در وزارت نیرو، تأمین برق پایدار صنایع را در اولویت قرار داده و با وجود محدودیت‌های شبکه، برای افزایش سهم برق بخش تولید تلاش کرده است.
🔹
این رویکرد به گواه گزارش مرکز پژوهش‌های مجلس نیز در عملکرد دولت پزشکیان قابل مشاهده است؛ به‌گونه‌ای که روند تأمین برق صنایع، به‌ویژه در دوره‌های اوج مصرف، نسبت به گذشته بهبود یافته است.
🔹
حضور فردای وزیر نیرو در وزارت صمت نیز در ادامه همین رویکرد ارزیابی می‌شود؛ اقدامی که نشان‌دهنده عزم وزارت نیرو برای تعامل نزدیک‌تر با بخش تولید و یافتن راهکارهای عملی به‌منظور تأمین هرچه پایدارتر برق مورد نیاز صنایع و همچنین سایر بخش‌های مصرف‌کننده از جمله کشاورزی، تجاری و خانگی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/671135" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671134">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">روزهایی که از تاریخ گذشت و ما میان این لحظه های دردناک بوده ایم ..</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/671134" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671133">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3acd02fbe.mp4?token=LTFj4Pm5SyP-Pi--tsl28J7ciBlufJZ2RmTUT9BfNe082QPStYTArHqCIwgCbU4rXnJz6CDhgFp8_bzRTJc9E6Gq8Xp5vxBWYb4c2-SuMWHXcmZcpuwlDr-rgVaX22xZO1KWvtAbkBXENHQ7zL_iyEzzGRAQRwDO2P65jEKXQHKIgKkiEQMuxyxDBSCe124WVIseR--xzHfQOTKJJ5bUgyIqdKgreHUWNFyewuYvZKvsp4nEFtjrvv-rX_cXr7nXQUXfDde1SYUAP3WAaSk002vs6A1DKrYqrF8KEorQiZUXSF-L-PMC39cULPcTmu-E3ivZiFMOCneSP_DNzZCuBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3acd02fbe.mp4?token=LTFj4Pm5SyP-Pi--tsl28J7ciBlufJZ2RmTUT9BfNe082QPStYTArHqCIwgCbU4rXnJz6CDhgFp8_bzRTJc9E6Gq8Xp5vxBWYb4c2-SuMWHXcmZcpuwlDr-rgVaX22xZO1KWvtAbkBXENHQ7zL_iyEzzGRAQRwDO2P65jEKXQHKIgKkiEQMuxyxDBSCe124WVIseR--xzHfQOTKJJ5bUgyIqdKgreHUWNFyewuYvZKvsp4nEFtjrvv-rX_cXr7nXQUXfDde1SYUAP3WAaSk002vs6A1DKrYqrF8KEorQiZUXSF-L-PMC39cULPcTmu-E3ivZiFMOCneSP_DNzZCuBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر قرار بود شخصیت‌های کارتونی زمان ما هم پیر بشن
😢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671133" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671132">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ارتش کویت: یکی از شناورهای نیروی دریایی کویت هدف قرار گرفت که در پی آن، ۴ نفر از نیروهای مسلح کویت مجروح شدند./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/671132" target="_blank">📅 22:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671131">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6f8ce096.mp4?token=lqkdk1XqvGoYJMqrOg9dPTtyAIeyWdTC4GS60lY7Gp0LMwqJjXtFlWvBITHmxi2zGs4hjxERqky56846SzJ5lmEn5BmHx0pYvKLcFP-OhTeTIZOnUSesa7lN3cV8aMz6oHzWTtx-Z6SORwoyqNfTUmvbbS5RoLdMb64JkMm5BbkX7IPwhb0kBD0dhhMQHKsF4H_LuZjz5iNfiq0GAa5vuF4liWvEF6CANrysslZED7Z1bSqA8a68A9MuoFKqRIfGrpqj8q6E-Skh8UjMmTsi3wnT-FTkdk8B9FGC12b1ZNP80cAEzfvgNHzmwr2qtfAZIaiCiY1IzbHPwoe0RxbkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6f8ce096.mp4?token=lqkdk1XqvGoYJMqrOg9dPTtyAIeyWdTC4GS60lY7Gp0LMwqJjXtFlWvBITHmxi2zGs4hjxERqky56846SzJ5lmEn5BmHx0pYvKLcFP-OhTeTIZOnUSesa7lN3cV8aMz6oHzWTtx-Z6SORwoyqNfTUmvbbS5RoLdMb64JkMm5BbkX7IPwhb0kBD0dhhMQHKsF4H_LuZjz5iNfiq0GAa5vuF4liWvEF6CANrysslZED7Z1bSqA8a68A9MuoFKqRIfGrpqj8q6E-Skh8UjMmTsi3wnT-FTkdk8B9FGC12b1ZNP80cAEzfvgNHzmwr2qtfAZIaiCiY1IzbHPwoe0RxbkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار موشک پاتریوت آمریکا به دلیل نقص فنی در آسمان بحرین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671131" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671130">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در اهواز
🔹
دقایقی پیش مردم اهواز صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/671130" target="_blank">📅 22:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671129">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
وقوع چند انفجار مهیب در ریف دمشق
🔹
منابع سوری گزارش دادند این انفجارها در شهر «صحنایا» رخ داده و هنوز علت انفجارها مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/671129" target="_blank">📅 22:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671125">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CE53vqD120IH3ddzYitQnebNK3Rh0yFbi6iwSuhWjX5B4w7DNVB1XhcuYoPF0iMb2V47MsoC-tbKBNWEFNVsACYNr1_O3suOcwUfbfIqhy5jXfd88LrPKqNlbMlxz9xdylYuLZHMdbBIdEPDzGHDI2jUQhfnCJmQlQktXbgJtEB_HM2iBCD5w0FO6FBoiU_c3_VVFuUWcT4Q634HhB9WKy8-PWlIKdGFKFt9muoN29F5yVd6kiuZrZ0lRudb__9Ni-IFVZTpVopCkR2SUTxQYOnnQB9RBgM9t38wzqGToc1SuXaRPwAOZyC2BLmYj0QzVrYqxsNQLakTeBWETYfAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AU6g29IFqToaEAv2AOWdC48H40G0FIe4VZBwypt-0behS-ZSFD4mgIBJUHH2UkyqgotV5G0hp9oa3XVGTUpVSZ_5SfBmwVivWKMUF8JGkbgr_9lyGxJC0HOvgZd7kb6EqsbWFpi8B3-k4L77968zBsWMVnq0OFTnz3DtR83beTd0d_fSqmYd23u-4gm5HrwyPwWESZvUDWmh-zDKaIEHq2x1peabRAVmyhh_20TCA3MpADNw6AsUZCrbu-I4gvwAtaXD-0czF5DU_3rJNSJXO2cn_zmF7QuFtE6Nfq1CEJwZWxsFWeXIas7r_hUbMM8rWDN3N9iIwwhAOkOHbHlyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYUUgu_gc7f2V_987QNTABuXWx2FQrQuZRl7nXQKbkoGr05yMXIHIyaZF4ryNf3R77JqNiwX7ydKIuDNO62GV_TQ-DqnwYs__ADwSZfb7mw0fUgEdgTO9u48h-VDIlZV-QEJgbM-Bv_isz0AWpDuBaazM4LQut0QQ1t6dQdQAyjIcpUyPdyhhwOvJ2Mo8JxtgW58KAkrfhLrQBKeHVM8F3zwm_q2AijRr_G1g7VwC0_71PNeyyHs7FT8DfrfCDkE3VQDYOLqDO-igMYkdjPNh4G1dfboSu06DnqpdyPyzVzL55mph4OxY8B_B3C84IECVAvHsnbmNLgIW43YQ_ZrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gK2NQH3oueU0NTf0P3H3W4psYLdYCMol8sdvuzBe7VIEEYrPW0cM8avBrDpna6ePmsEC1CW0E_h2gQjckraykCZxsDE0flf6yDtJc6vfCN40blL-J9LObp1RJl_fX9jvzgScyWGXKdub7yewL8JQYiDzcumInyZfXzIpOqHuHvo1yUOcnDq6YivqeTGBginCfkTG5jZVdDnm4Qz06Al62bE6UyzRergfEL2FOkRX4rQIQjYH57isMtO60OpOSOlmy5tZvlXgk1p6ItMVpqGyWiKxZElSggcgIt8OKsb_KIZObnveyzJT7_eIJ0j2SuMyrPGbtk3OEVwG0Gwi40O0Zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع پروتئینی هم متنوع هستند با بهره‌گیری از تمام آنها میتوان از سایر مزایا نیز بهره‌مند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671125" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671124">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbaf1ccbd8.mp4?token=KhefnX--Kf81fmjXBJuorTMh49xgKIGO8bzxjNZzR8fQ5ERKoecKY96qzYkV-6qZGSBlva8Hcmzjch8uB9sCpfcdluRKM02fIptSm6U7xmF8m3ZYobJAtJKtRRRtuGdBLmgxRbNgKQZjgUypnOXkWCnYq-2gQk_boh8S5IImXeTIz1yewjwnl6v7pYrz57fovTEBj9phLsGkxh6HFlvRk3IERdL6x38Vkz_CMVLO2yod96nh1OR_usivloZCxLOOXYMfA4J5eSZXvcbCidYdWoVgbyNEx6u6l4YdUSPtC1CzjjAmhH7LmK0WFyjLYWyxzkQOi67Vg7h_I4K4p9DTV3LU1N34J9xFXO_c27BQ0vAdCRH01DAFgV04ouBFToETaUZeffvCXC7YHx8m0tjX7NCM_f864o1_tVv7qdsyzthmnupmnAXbJ2eZZuJB2VRYRsdfLmB70pNQQEDgrGKOEHYbf_U3oQ0643B2ZeEaoqtmQCwv38ZundwExu2YVYW2zlhGlk7D8UHQdDWmFjt6iMoJ_ZwQsmOQIDxg9UigSIrh4TPOylw077yb_1juBsRJRyRFfDW6lw8vNEoFcNRyo2etf4s5jZHpHfAqhHSNCxWZblufHbR_GPFMiuDHWS7KvnDsxC2NjL0c--EFk_vi-FJ7igkC_n9cabAztokIwAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbaf1ccbd8.mp4?token=KhefnX--Kf81fmjXBJuorTMh49xgKIGO8bzxjNZzR8fQ5ERKoecKY96qzYkV-6qZGSBlva8Hcmzjch8uB9sCpfcdluRKM02fIptSm6U7xmF8m3ZYobJAtJKtRRRtuGdBLmgxRbNgKQZjgUypnOXkWCnYq-2gQk_boh8S5IImXeTIz1yewjwnl6v7pYrz57fovTEBj9phLsGkxh6HFlvRk3IERdL6x38Vkz_CMVLO2yod96nh1OR_usivloZCxLOOXYMfA4J5eSZXvcbCidYdWoVgbyNEx6u6l4YdUSPtC1CzjjAmhH7LmK0WFyjLYWyxzkQOi67Vg7h_I4K4p9DTV3LU1N34J9xFXO_c27BQ0vAdCRH01DAFgV04ouBFToETaUZeffvCXC7YHx8m0tjX7NCM_f864o1_tVv7qdsyzthmnupmnAXbJ2eZZuJB2VRYRsdfLmB70pNQQEDgrGKOEHYbf_U3oQ0643B2ZeEaoqtmQCwv38ZundwExu2YVYW2zlhGlk7D8UHQdDWmFjt6iMoJ_ZwQsmOQIDxg9UigSIrh4TPOylw077yb_1juBsRJRyRFfDW6lw8vNEoFcNRyo2etf4s5jZHpHfAqhHSNCxWZblufHbR_GPFMiuDHWS7KvnDsxC2NjL0c--EFk_vi-FJ7igkC_n9cabAztokIwAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با فرزندم که به وطن عِرق ندارد مواجه شوم؟
!
پاسخ مشاور را ببینید
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/671124" target="_blank">📅 22:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671123">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کل سندیکای صنعت برق: خاموشی‌ها فقط به تابستان ختم نمی‌شود و احتمالا به زمستان هم کشیده می‌شود
مهدی مسائلی، دبیر کل سندیکای صنعت برق در
#گفتگو
با خبرفوری:
🔹
با وجود ورود نیروگاه‌های خورشیدی و سیکل ترکیبی، کشور همچنان با دست‌کم ۱۰ هزار مگاوات کسری برق مواجه است.
🔹
دولت برای مدیریت ناترازی برق دو گزینه دارد: محدودیت برق صنایع مانند سال گذشته برای کاهش خاموشی خانگی، یا افزایش خاموشی بخش خانگی با هدف حفظ تولید و فعالیت کارخانه‌ها.
🔹
از ۱۰۰ هزار مگاوات ظرفیت نصب‌شده نیروگاهی، در بهترین شرایط تنها ۷۰ هزار مگاوات قابل تولید است؛ روز گذشته نیز با پیک مصرف ۷۱ هزار مگاواتی، فقط ۶۳ هزار مگاوات برق تأمین شد. به دلیل کمبود سوخت نیروگاه‌ها، احتمال تداوم خاموشی‌ها در زمستان نیز وجود دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/671123" target="_blank">📅 22:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671121">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
معرفی انیمیشن: بچه زرنگ (۱۴۰۱)
🔹
ژانر: انیمیشن، ماجراجویی، خانوادگی
🔹
امتیاز: ۴.۱
🔹
خلاصه: محسن، پسربچه‌ای عاشق ابرقهرمان‌ها، پس از آشنایی با آخرین ببر ایرانی وارد ماجراجویی پرهیجانی می‌شود تا او را از دست شکارچیان نجات دهد. «بچه زرنگ» با ترکیب طنز، هیجان…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/671121" target="_blank">📅 22:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671120">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc203453c9.mp4?token=kPSqzfOOFOpWH-106DdSdRXYH5WbWrhQ0AMGdOT_COKUATGEWic_ncDypvirbigLu2GZ_vd6b-gNyQTaswlM2VRheEulRP2ti9FMcJoC4zG8FAbmfxpUT62SYDhFOi8Q85b0CyblACFaRqcGuhSFe0Biok5vLTR_M4pzQ0Bl0PNYCgcj56nTqC5nInkWA7msuJdgv2DBcBHOHIp72F_62xUzuqDHZXsT_PpU4fF2SA64c517ea1yMZdOpFMnSsbs6Z8h_hl_BN2zdbHBfynO4P0y8rS7Q6XifvbxO-_Qqv3XFfCPoYXfil4Uo-hRnlFDEKCUVIiYa4LNvrALWGtn7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc203453c9.mp4?token=kPSqzfOOFOpWH-106DdSdRXYH5WbWrhQ0AMGdOT_COKUATGEWic_ncDypvirbigLu2GZ_vd6b-gNyQTaswlM2VRheEulRP2ti9FMcJoC4zG8FAbmfxpUT62SYDhFOi8Q85b0CyblACFaRqcGuhSFe0Biok5vLTR_M4pzQ0Bl0PNYCgcj56nTqC5nInkWA7msuJdgv2DBcBHOHIp72F_62xUzuqDHZXsT_PpU4fF2SA64c517ea1yMZdOpFMnSsbs6Z8h_hl_BN2zdbHBfynO4P0y8rS7Q6XifvbxO-_Qqv3XFfCPoYXfil4Uo-hRnlFDEKCUVIiYa4LNvrALWGtn7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون حقوقی وزارت خارجه: آمریکا با بازگرداندن محاصره کاملا تفاهم‌نامه را متلاشی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/671120" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671119">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سپاه: چندین سوله نگهداری تسلیحات، قطعات شناورها و هواگردهای دشمن و رمپ استقرار پهپادهای MQ9  در بحرین هدف موج سوم قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
الَّذِينَ آمَنُوا يُقَاتِلُونَ فِي سَبِيلِ اللَّهِ ۖ وَالَّذِينَ كَفَرُوا يُقَاتِلُونَ فِي سَبِيلِ الطَّاغُوتِ فَقَاتِلُوا أَوْلِيَاءَ الشَّيْطَانِ ۖ إِنَّ كَيْدَ الشَّيْطَانِ كَانَ ضَعِيفًا
🔹
ملت شجاع و بصیر ایران اسلامی؛
رزمندگان غیور نیروی دریایی و هوافضای سپاه در موج سوم عملیات نصر ۲ با رمز مبارک یا زین العابدین علیه السلام و تقدیم به ملت مبعوث شده، طی یک عملیات همزمان موشکی و پهبادی در ساعاتی قبل چندین سوله نگهداری تسلیحات و قطعات شناورها و هواگردهای دشمن در پایگاه شیخ عیسی بحرین را منهدم کردند و همچنین با حمله به رمپ استقرار پهپادهای MQ9 دشمن در پایگاه علی السالم کویت تعدادی پهپاد را منهدم و یا به آنها خسارت وارد کردند.
🔹
این حملات در پاسخ تجاوزات بعد از ظهر امروز ارتش کودک‌کش آمریکا در حمله به تعدادی از ایستگاه‌های ساحلی نیروهای مسلح ما بود.
🔹
مقابله به مثل و تنبیه متجاوز تا وقتی جنایت آمریکا ادامه دارد استمرار خواهد یافت و در صورت تکرار این تعرضات با پاسخ‌های غافلگیر کننده مواجه خواهند شد.
🔹
تا زمانی که شرارت های آمریکا در منطقه وجود دارد یک قطره نفت و گاز از منطقه صادر نخواهد شد و این تجاوزها جز تأخیر در بازگشایی تنگه هرمز نتیجه‌ای نخواهد داشت.
و ماالنصر الا من عندالله العزیز الحکیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/671119" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671118">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سلطه شهرهای خوزستان بر لیست گرم‌ترین‌های جهان؛ ۶ شهر استان در میان ۱۰ نقطه داغ کره زمین
🔹
بستان: با ثبت دمای ۵۱.۶ درجه سانتی‌گراد (رتبه دوم جهان و گرم‌ترین شهر خوزستان)
🔹
اهواز: با ثبت دمای ۵۰.۸ درجه سانتی‌گراد (رتبه سوم جهان)
🔹
امیدیه: با ثبت دمای ۵۰.۵ درجه سانتی‌گراد (رتبه پنجم جهان)
🔹
صفی‌آباد دزفول: با ثبت دمای ۵۰.۵ درجه سانتی‌گراد (رتبه ششم جهان)
🔹
آبادان: با ثبت دمای ۵۰.۲ درجه سانتی‌گراد (رتبه هفتم جهان)
🔹
بندر ماهشهر: با ثبت دمای ۴۹.۴ درجه سانتی‌گراد (رتبه نهم جهان)
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/671118" target="_blank">📅 22:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671117">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvHsrckHWV4d3w3-aFfzcoEKYYPqDE9y2nhHdT0omkcj26yCPgocwoNoZcWcU8VTOw_qtpE-wic8eduXcou38K5udAIZ3gPI2RWpur3wLDJZQTVPF9gGbOAZzwOPzZycRVa5VptGhrHaPZ0HdU9DfnkD0Z569j05wMAQYGf9YdpLvFqnBs_AvhIogPwJ4wqjIbSdU3f8lXHcBx5PP_89lZWx6ABaLB_-67Gi5-5YheHqv3mfUYl3n65ZEoXUFlWkdQnrC9LrU4moaBm7MbCsfBSvS7LBD09tt0UIXQww5zgTtX20Ts3Ou8bsrDh-ev8mDHAnXQNE-gaaD-l1UDGtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارش کارت بانکی با طرح ماه تولد از طریق اپلیلکیشن دیما/ ۳۰ طرح جدید کارت برای مشتریان بانک ملت
‌‌
🔷
بانک ملت امکان انتخاب و سفارش کارت‌های ویژه ماه تولد را را از طریق اپلیکیشن «دیما» فراهم کرده است و مشتریان می‌توانند از بین ۳۰ طرح جدید، کارت ماه تولد خود را انتخاب و درخواست صدور آن را ثبت کنند.
‌
🔷
این مجموعه کارت‌ها شامل ۱۶ طرح عمومی، ۱۲ طرح مرتبط با ماه تولد و ۲ طرح ویژه مشتریان مهان است و بدون نیاز به مراجعه حضوری از طریق شعبه دیجیتال بانک ملت قابل سفارش خواهد بود.
‌
🔷
در بازه برگزاری جشنواره کارت‌های جدید بانک ملت تا پایان شهریورماه، صدور و ارسال کارت برای مشتریان رایگان است، به این صورت که مبلغ کارمزد کسر شده پس از ثبت درخواست، ظرف ۲۴ ساعت به حساب مشتری بازگردانده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671117" target="_blank">📅 22:14 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
