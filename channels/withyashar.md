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
<img src="https://cdn4.telesco.pe/file/KGLweOkIemECS-0TQp20LXRBnaiAcZU23X-6SZkxkslwiU_Tfjw3StoDzbRdHcHxxGueun7KLrT2Y-HFVp8m0edc8-HcZpPzu53UYWooddtKyhTJ3i0uL9zG4pQ6t7Ina2OaAszvdklbqHYAqzfOD_EsuXzgAyBEghe-6WFPDX4eteoW_TQXs--w8F3ZCTo27diQoGm1W4-5cykpbcxZVZw-5UuFUFB8MntJeKWzQloj-zKV9Q7M3eHygbW4XrZ3-gMpeTq-vdHkgY8Su9h0RGvfRhW1dVBRdf8w25cPNEsurX3k3UcVlBmfr0zC3zPFbhMp5UdLsUl6-n88HVVsoQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 286K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 02:45:20</div>
<hr>

<div class="tg-post" id="msg-13328">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حملات جدید به کویت
@withyashar</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/13328" target="_blank">📅 02:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13327">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رژیم جمهوری اسلامی به بحرین حمله  کرد پدافند بحرین فعال شد @withyashar</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/withyashar/13327" target="_blank">📅 02:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13326">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">۳‌پا
اعلام کرد در پاسخ به آنچه «حمله آمریکا به حاکمیت ایران در جزیره قشم» خوانده، پایگاه‌های نظامی آمریکا در کویت را با حملات موشکی هدف قرار داده و این اقدام را «پاسخ اولیه» توصیف کرده است.
در این بیانیه به آمریکا و هر کشوری که خاک یا آسمان خود را برای عملیات علیه ایران در اختیار بگذارد هشدار داده شده که هرگونه اقدام جدید با پاسخی شدیدتر و فراتر از «قواعد متعارف» روبه‌رو خواهد شد.
۳پا همچنین تأکید کرده است که دوران «بزن و فرار کن» پایان یافته و نیروهای آمریکایی و متحدانشان باید منتظر پیامدهای اقدامات خود باشند.
@withyashar</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/13326" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13325">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حمله دوباره جمهوری اسلامی به اقلیم کردستان
@withyashar</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/withyashar/13325" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13324">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مهر: یک موشک به ساحل ایران برخورد کرد
خبرگزاری مهر گزارش داد یک پرتابه در محدوده ساحلی بین شهر سوزا و روستای ماسان برخورد کرده است
@withyashar</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/withyashar/13324" target="_blank">📅 02:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13323">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/withyashar/13323" target="_blank">📅 02:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13322">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCisaMvH6n5H6AL1IIBKXi1ZhzKYWiRUn4YUA1KAqaOwpKW_GbFZKyNTvYdxmyBcJ-wKo2LsmvsSQTl6LH03UnqmQWQq9glPPJNI4jGwPyvj7hJ2TOXdy-4j5JRKQxL6UOFI7-WIs8tzAXupF1YgTGvJ9S9J82WbkpuvRcIjH-LWeaZvNY8MDCi4YadeFzqaKWSNSmSxBr5VlnCCVW_nh9WWi4m5LULBKu6JqyOgNt2VMzREBbgarkrBlLm4xDHI5pG1mjaJXfEmzb15Eu6scihhT_1x5YXdz1ryn-VWl3mHA5b9by2lw_B4LoppB6bvW-Vd2VK_VqcC3FrYstDzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم جمهوری اسلامی به بحرین حمله
کرد
پدافند بحرین فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/withyashar/13322" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13321">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dee78f961.mp4?token=SLmXo8q6qyGXKYj5Lpw7Hx9HhKh-Uw3PU_MLWDagSEDF-9qUpcPm2WkXHodke482iQr5QdhJh2-ifdJFp1HC36Ve5gDbLZA6ewRccjwCrmXG9f6ugr5K-XHoe-uHIXh5rA7B7SLCv79x95xXm2bb9cjxp_ASkR8e46BFT3FAFU1GicliW9EThHThqmdnZkWnG4CRuXRnTsX5e3SikYHCIn0bBbhW-rB5NzVFhRK99qGLUBnLkhuiHg0SA0WYNptcI8_D21UckPyLpCEZOfX-8vac9jozwerBYNYPNJEh8v9nciT50IZOknoIJoAp92o44tazhq4rb7_M-4WrGSev1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dee78f961.mp4?token=SLmXo8q6qyGXKYj5Lpw7Hx9HhKh-Uw3PU_MLWDagSEDF-9qUpcPm2WkXHodke482iQr5QdhJh2-ifdJFp1HC36Ve5gDbLZA6ewRccjwCrmXG9f6ugr5K-XHoe-uHIXh5rA7B7SLCv79x95xXm2bb9cjxp_ASkR8e46BFT3FAFU1GicliW9EThHThqmdnZkWnG4CRuXRnTsX5e3SikYHCIn0bBbhW-rB5NzVFhRK99qGLUBnLkhuiHg0SA0WYNptcI8_D21UckPyLpCEZOfX-8vac9jozwerBYNYPNJEh8v9nciT50IZOknoIJoAp92o44tazhq4rb7_M-4WrGSev1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصادف در خیابان های کویت بر اثر تماشای موشکهای ایران
@withyashar</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/withyashar/13321" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13320">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7e3bcc.mp4?token=E-RGUcNZIQXKCQFA2dwYUHUNPDF05tt1kqI4IBPLj8TgjRR5WidSyjdKtEKkegOfp4-kAweCzZ-Zx2hB6RR30K-kjZKLaLy0uTKZ_hSaqKCUYE4J6sX7OOHju2r-HOxxAZqD7gYH_wxisGGWNVLQZkUPRPJVRJv7HPzdIhSYL8xrNHn8kdWudTJCaUE-yBf53Hf3PTTtXTEb5_732Qyv-Y6G9p4x2EquusdTBSsh5Ih3Tg8xt259nemRnM4l_7vCxU9427bio0qC9m3f7l23-9sCf8ZUvM_8Wi4_qxA6fKIZSTI5VpPw7YEZaOkovtT_7KoPc9Kmn_68DBfbx1qSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7e3bcc.mp4?token=E-RGUcNZIQXKCQFA2dwYUHUNPDF05tt1kqI4IBPLj8TgjRR5WidSyjdKtEKkegOfp4-kAweCzZ-Zx2hB6RR30K-kjZKLaLy0uTKZ_hSaqKCUYE4J6sX7OOHju2r-HOxxAZqD7gYH_wxisGGWNVLQZkUPRPJVRJv7HPzdIhSYL8xrNHn8kdWudTJCaUE-yBf53Hf3PTTtXTEb5_732Qyv-Y6G9p4x2EquusdTBSsh5Ih3Tg8xt259nemRnM4l_7vCxU9427bio0qC9m3f7l23-9sCf8ZUvM_8Wi4_qxA6fKIZSTI5VpPw7YEZaOkovtT_7KoPc9Kmn_68DBfbx1qSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیکه دیگری از لاشه موشک
@withyashar</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/withyashar/13320" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13319">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2918449436.mp4?token=rqBkD7vHvNTdnZtjXwKRMaMuaj9jko91TExe0AcPKIOUvgFZJ1VS64Htm0-sUHMLUEBSTu58YKPbhHHA8QN05Fy7aoqYZHi50QUynpbtMWb4qHPI8ADoxzyqSeyEIHbg6snATvrWtffbgjmiaCLz_wVrO5HFH0J68fXPMp0wkFtaUnLQWdB6A6ZlP3N-nDwrQpfR7fmE3XyKI2_PqUAmJFryKEwwxg_dgPa-atDYoYLxU4-iYgdss6u8FQ8JrhMiqdx0bZaC2phJ1nUNiGL-JBtmgYySVLa3yjbEgZsE-F7cMZojDxCn08s-wswJjy3n26q8SHFEl7CkZQPjBzny3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2918449436.mp4?token=rqBkD7vHvNTdnZtjXwKRMaMuaj9jko91TExe0AcPKIOUvgFZJ1VS64Htm0-sUHMLUEBSTu58YKPbhHHA8QN05Fy7aoqYZHi50QUynpbtMWb4qHPI8ADoxzyqSeyEIHbg6snATvrWtffbgjmiaCLz_wVrO5HFH0J68fXPMp0wkFtaUnLQWdB6A6ZlP3N-nDwrQpfR7fmE3XyKI2_PqUAmJFryKEwwxg_dgPa-atDYoYLxU4-iYgdss6u8FQ8JrhMiqdx0bZaC2phJ1nUNiGL-JBtmgYySVLa3yjbEgZsE-F7cMZojDxCn08s-wswJjy3n26q8SHFEl7CkZQPjBzny3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشه موشک منهدم شده ایرانی‌توسط پدافند امریکایی کویت
@withyashar</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/withyashar/13319" target="_blank">📅 02:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13318">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اینترنت ایران داره به همین سرعت محدود میشه
🚨
😞
@withyashar</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/withyashar/13318" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13317">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9349aaf84.mp4?token=hlLybE-SFsYmsqVX8ZB2M5lunRAR91k8B9Q7kdwI1oUh6VZAe9bGIavrzkEY6DJal1NA5VvhxcwSdz9IYRlRrG19be1jvyUvrlzB1MSIapxBoV5ANk1e28pG36EfA2g96zD8ztGTrDn3rzqm3857py9hcCYnv6SCZ_heMq6LFWa8SBf0XjomICyeYwc-X04S1MdTE01aIOVzlREHxJcM0AUmBDy_IKcGfeoaReGrvzzNvQ-0MzdLKVr2FBjXTxxxrN1njPRLRfeDU1I61DKHXswXe3NqBq_mZHB5T6ue5OCfMsOK_sRtFlR674F-Zy1XZsZCTrASFpLLsNhgsG-Byw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9349aaf84.mp4?token=hlLybE-SFsYmsqVX8ZB2M5lunRAR91k8B9Q7kdwI1oUh6VZAe9bGIavrzkEY6DJal1NA5VvhxcwSdz9IYRlRrG19be1jvyUvrlzB1MSIapxBoV5ANk1e28pG36EfA2g96zD8ztGTrDn3rzqm3857py9hcCYnv6SCZ_heMq6LFWa8SBf0XjomICyeYwc-X04S1MdTE01aIOVzlREHxJcM0AUmBDy_IKcGfeoaReGrvzzNvQ-0MzdLKVr2FBjXTxxxrN1njPRLRfeDU1I61DKHXswXe3NqBq_mZHB5T6ue5OCfMsOK_sRtFlR674F-Zy1XZsZCTrASFpLLsNhgsG-Byw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان کویت کمی‌پیش
@withyashar</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/withyashar/13317" target="_blank">📅 02:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جنگنده‌های اسرائیلی پرواز کردن
@withyashar</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/13315" target="_blank">📅 02:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/13314" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پست جدید از صحبت‌های بسیار زیبای شاهنشاه آریامهر  ارتباط قلبی ما
❤️‍🩹
فرا مرزی شده  https://www.instagram.com/reel/DZGNeRLxq-Y/?igsh=MXQ1dTZmdXk2bGZpdQ==</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/13313" target="_blank">📅 01:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b76b57549.mp4?token=qk3ekT17sw8kpg8ijEd7ve4aWxr66vY9Ds96R7rU39u8tUKah5B3Aa8zGq6aUEiDIM8Qg1xHIczSZWec9t3Hnm6DcybZh6g5m5pcuCpCysTR5tUIAU1iTIQxRFqXfDGlc3cSh0kTtWJG7s5SwNl3W2JyDLJAp4NPk2DnNfbDHEgtgH53Rr7nKbKLsuC6He5g_2C1yNDx3PlY2lSdNjbekg7XfHk0-iEOL3SOHyIRtcT-3ci23YRs7UKJKzpbdjrTGmEZgaS5ZcYLhe6NX991yHSJua85B1xtNJgSWdUbO6rjN2tfcWP6Kh5TvFNWTFxuF9hVPkg_FN5XcUwCVQhP31D_vaQAoPORecTqcBLSTe5aDdpmnDfEn5Vn9yYEe5Tss92PJrtlhi7Qu_4OgP7m0cWj9qfhrabutEtj0PLDlPvtD5usxezNjF3r3p7rMKlXwXVgunhrROdC9mUnAMzkpioRemvyhKQ46aBV7XBNDnvZP6F4z7JXMewCvQ7L1Az60WVqStI5jy9hIla1tlKW1H7MZHAw4zonVX-S9j3zt9fvepxGjyet6J1M_7HjpllS05zydSyJKrDgSmVQvU9HqfApisWaLZgP__9_qfM0mpBYq0cZjRxBVCPYx683bPff8xNMut-YLqfAXZRXhlVAm7SdobfdM0isio7n-9SR62U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b76b57549.mp4?token=qk3ekT17sw8kpg8ijEd7ve4aWxr66vY9Ds96R7rU39u8tUKah5B3Aa8zGq6aUEiDIM8Qg1xHIczSZWec9t3Hnm6DcybZh6g5m5pcuCpCysTR5tUIAU1iTIQxRFqXfDGlc3cSh0kTtWJG7s5SwNl3W2JyDLJAp4NPk2DnNfbDHEgtgH53Rr7nKbKLsuC6He5g_2C1yNDx3PlY2lSdNjbekg7XfHk0-iEOL3SOHyIRtcT-3ci23YRs7UKJKzpbdjrTGmEZgaS5ZcYLhe6NX991yHSJua85B1xtNJgSWdUbO6rjN2tfcWP6Kh5TvFNWTFxuF9hVPkg_FN5XcUwCVQhP31D_vaQAoPORecTqcBLSTe5aDdpmnDfEn5Vn9yYEe5Tss92PJrtlhi7Qu_4OgP7m0cWj9qfhrabutEtj0PLDlPvtD5usxezNjF3r3p7rMKlXwXVgunhrROdC9mUnAMzkpioRemvyhKQ46aBV7XBNDnvZP6F4z7JXMewCvQ7L1Az60WVqStI5jy9hIla1tlKW1H7MZHAw4zonVX-S9j3zt9fvepxGjyet6J1M_7HjpllS05zydSyJKrDgSmVQvU9HqfApisWaLZgP__9_qfM0mpBYq0cZjRxBVCPYx683bPff8xNMut-YLqfAXZRXhlVAm7SdobfdM0isio7n-9SR62U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفع موشک های ایرانی در کویت
@withyashar</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/withyashar/13312" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/withyashar/13311" target="_blank">📅 01:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پایگاه عریفجان در جنوب کویت، نیز هدف قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/withyashar/13310" target="_blank">📅 01:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13309">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/withyashar/13309" target="_blank">📅 01:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13308">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMhdi</strong></div>
<div class="tg-text">یاشار این به معنای شروع جنگ هست بنظرت یا امریکا میخواد بگه نقض نشده</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/withyashar/13308" target="_blank">📅 01:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13307">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVCFvodf5-zn1pcGwHJW082xMPaAQE9MR4DBMEhKEsXr63gmxIP0ysAU11mc5vPeCUW7GPfVj6O_Vch2F9iF3eGLatdbgQNaRfjZUsNdKlPyEddtRSWjYgi4nXbVPG090_JYb0HZJbJhLQgbH3PdOtOFwTQHOYhkDEip55cvBq0lshXtQ238qryeoXJHMrs-XQMeJp62dkQ9MlAWUGLU0VDDg2J5ZJDRiXgaUdOhsAAQDckdADxGijowRDFbs-sepgpqBA_2vly-cfAE1bI5pOoC9qGjOpCKglVmm8KOmbS4izLkdvhO4jEx9P9qmDkTPyYhY-lHDdEbKg-1k3Undw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رد موشکهای بالستیک در آسمان شیراز
@withyashar</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/withyashar/13307" target="_blank">📅 01:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13306">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الان شلیک ۲ موشک از سایت موشکی زین آباد داراب احتمالا به کویت @withyashar</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/withyashar/13306" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13305">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=VIx64vNdZB0jKxgNmYq-3h3VTj7pUEDzMLr6sjZKb4yicS_JUa-zeEJKy5u0YuUdVT5U9nwpXNCZV1M1yIz7Cj6l5UFtjS9QxwQyEB1Empf4359vZyXangsQLod-1UfEmJM5VPsy3Ayjsd5fp3OelQm2RH6BMJ9VycSuHDN6ifR_qiPLEvPBsb9L_AwZWt4GCKNTn--ZOAFfe1nDpAK7jLvWVePBGkylbBazO2AC7oHMSGbO6tz1y_9_yDzWqMZ0s9Ty77iLnZoUPFWExF0akrVy1ipVjeszoBhSl8Q0HvE02XYqa9Ew56Ar4vbo-NsDAwoJVUMEXPh4N03dbN7w2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=VIx64vNdZB0jKxgNmYq-3h3VTj7pUEDzMLr6sjZKb4yicS_JUa-zeEJKy5u0YuUdVT5U9nwpXNCZV1M1yIz7Cj6l5UFtjS9QxwQyEB1Empf4359vZyXangsQLod-1UfEmJM5VPsy3Ayjsd5fp3OelQm2RH6BMJ9VycSuHDN6ifR_qiPLEvPBsb9L_AwZWt4GCKNTn--ZOAFfe1nDpAK7jLvWVePBGkylbBazO2AC7oHMSGbO6tz1y_9_yDzWqMZ0s9Ty77iLnZoUPFWExF0akrVy1ipVjeszoBhSl8Q0HvE02XYqa9Ew56Ar4vbo-NsDAwoJVUMEXPh4N03dbN7w2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/withyashar/13305" target="_blank">📅 01:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13304">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5WkEVMTiHOl19kKB3iHWuC1HnPOqz3oSzJSxNzZy2G-kLEMTJiHanWcOvelIt9HzrW1zVMSGWoq-9rqqouKEVGZPb7bf-Rqni_ebA1zpRqXIZFexKNAVWJTlO7R3y56ymtd7fRPC39AWdIcLs_0kgmawBoTK9eWa7FtM7FdbWeu_wyKQQN1d_9A615CPkimK79E5dddZBX94cg8j3CoHJbVyuJ85HGBUxMZbSo1oGPZGWZ7ZJZ1HTY8NQPO-swD-gGtpqPVxapNej_LzXJEuGnDrIKQtTjU6iZ75TpWvQieorFxQGur9gIWpJpKYW9jduK89fjUBSuFea2QgDHPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کویت تأیید کرد که به موشک‌ها و پهپادهای پرتاب شده از ایران پاسخ می‌دهد
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/13304" target="_blank">📅 01:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آژیر در کویت
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/withyashar/13303" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13302">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAhyptClXx7MFjLOq6gQe9ReAV8VrRBgDqmqUlEp7jWXOTJftK32YqFufLHJAeSyMorJ-WahLN-xYYjlJky2hwU6GMz4mk5K1oN5EstskzwsaB2cjFfcPsDAcwe79_mYP1rqKxGEsED05yowlpCj9KpRDLJUGUA2jX4Tvv6xwddSXDgLYnDtAk6V-qandATHlIiaxO7anN-YjwmJQl-c5Kk3IaPQjb20DOixuYObUna13y-wEAP-9WHg5LS7W7hCGM3XOqak829qboZzRlfw04SU66IDvTYtPa4iJdHblL_0hC0xxos93bVsMzlQsnPHgoMsdHnOglXA4vXiCuoFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان شلیک ۲ موشک از سایت موشکی زین آباد داراب احتمالا به کویت
@withyashar</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/13302" target="_blank">📅 01:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13301">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرگزاری مهر بعد از  ساعتی چک کردن چنل ما گفت : بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
پیگیری‌ها برای کسب اطلاع از ماهیت دقیق این انفجار  ادامه دارد.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/13301" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13300">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خاورمیانه جنگشم مثل آدمیزاد نیست !
@withyashar</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/withyashar/13300" target="_blank">📅 01:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13299">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتاق جنگ با شما : صدای انفجار از سمت دریا نبود
به اون کوهه زدن که پر از مهماته نزدیکمونه قشنگ به چشم دیدیم
@withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/13299" target="_blank">📅 01:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13298">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش انفجار قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/13298" target="_blank">📅 01:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13297">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffea244ab.mp4?token=Tey042Xubos3oorJoRtwPjCSQ9GgXCh0BCS1XWwneQO8mJlc3S2dBRpXWxXhlKj8LA0LAsfRps2Od115S547HQR0_vU24sVhO7rphEH5DGR5FcOT_LPmAjKIpzCPDMfL8AGpgYmqs9D1KhIN-rrTCLzXjQB-SYj1eC5SlgRO9qL7m_soncDet8w68_3-s9PAcbFfqsif_d87z3BLm-fyep3968tJXGPSgzUmxRrP7gEM9CrRKk_ChMHNR_RwFBCMgOnBgVe2Ib1ZocSKnQ21BMTp0awe0Uftue7w-Mw3tDJ_WjvW4XYxVdUCyQuJ1iuBOlBF11Kqi_vUXQWZx0TYBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffea244ab.mp4?token=Tey042Xubos3oorJoRtwPjCSQ9GgXCh0BCS1XWwneQO8mJlc3S2dBRpXWxXhlKj8LA0LAsfRps2Od115S547HQR0_vU24sVhO7rphEH5DGR5FcOT_LPmAjKIpzCPDMfL8AGpgYmqs9D1KhIN-rrTCLzXjQB-SYj1eC5SlgRO9qL7m_soncDet8w68_3-s9PAcbFfqsif_d87z3BLm-fyep3968tJXGPSgzUmxRrP7gEM9CrRKk_ChMHNR_RwFBCMgOnBgVe2Ib1ZocSKnQ21BMTp0awe0Uftue7w-Mw3tDJ_WjvW4XYxVdUCyQuJ1iuBOlBF11Kqi_vUXQWZx0TYBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای ایالات متحده ساعاتی پیش یک نفتکش خالی از محموله را که در حال حرکت به سوی یکی از بنادر ایران در خلیج فارس بود، از کار انداختند.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که اقدامات مربوط به محاصره دریایی را علیه نفتکش
ام/تی لکسی (M/T Lexie)
با پرچم بوتسوانا، در حالی که از آب‌های بین‌المللی به سمت جزیره خارک در حرکت بود، اجرا کرده است.
به گفته سنتکام، خدمه کشتی هشدارهای مکرر را نادیده گرفتند و طی یک دوره ۲۴ ساعته چندین بار از تبعیت از دستورات نیروهای آمریکایی خودداری کردند.
در نهایت، یک هواپیمای آمریکایی با شلیک یک موشک
هلفایر
به اتاق موتور کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شدند
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/13297" target="_blank">📅 00:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13296">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش انفجار قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/13296" target="_blank">📅 00:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13295">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رسانه‌های ترکیه اعلام کردند که ویزای مکزیک کلیه اعضای تیم ملی فوتیال ایران برای سفر صادر و تحویل سفارت ایران در آنکارا شده است.
@withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/13295" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13294">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/13294" target="_blank">📅 00:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13293">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پست جدید از صحبت‌های بسیار زیبای شاهنشاه آریامهر
ارتباط قلبی ما
❤️‍🩹
فرا مرزی شده
https://www.instagram.com/reel/DZGNeRLxq-Y/?igsh=MXQ1dTZmdXk2bGZpdQ==</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/13293" target="_blank">📅 00:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13292">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آمریکا ۴ صرافی بزرگ ایرانی
نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.
@withyashar
این صرافی ها ولت هاشون فلگ بود و از قبلم هر ولتی که با این صرافی ها ارتباط داشت کثیف میشد
اما الان خطر فریز شدن دارایی در صرافی است</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/13292" target="_blank">📅 23:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13291">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">العربی الجدید: مذاکرات لبنان و اسرائیل در واشنگتن به پایان رسید و قرار است فردا ادامه یابد
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/13291" target="_blank">📅 23:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13290">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13290" target="_blank">📅 23:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/13289" target="_blank">📅 23:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/13288" target="_blank">📅 23:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دایرکت باز شد بریم برای پاسخ به سوالات
💥</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13287" target="_blank">📅 22:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کرج صدای پدافند
🚨
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/13286" target="_blank">📅 22:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش ها از درگیری شدید مرزی میان هند و پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/13285" target="_blank">📅 22:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش زیاد شیراز صدای پدافند / انفجار
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/13284" target="_blank">📅 22:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13283" target="_blank">📅 21:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13282">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بریم برای سوال و جواب، هر سوالی دارین توی متن کامل بنویسین و دایرکت کنین، فقط در یک پیام.</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13282" target="_blank">📅 21:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b925d659.mp4?token=UZ_a4h0v53g5DG73ZUvPP00chJ0XkI7AicPOHWiMmUxy7-8GiSEww4uzPNB_xI2f7cd_Hr2B3Yp2Ix6jpHWCRjFYjlaOvtqqynyZKfP89ijVIRjMhHaaUyFfi15Qj3R_r_S_hI6Hxuk9YjUUmxC281NvxKmRZ_0L-ShAdGiJH-Rg9dMT-MLwZnUBUB875JV72xG3pjJZaX_42ZGq3uQNbn1vdH9nkbgWnNaEvSRkk9K5fVNZDSaAxOwF3HMjkYSYoGcC2Ktz1qpAKuO45iF55u2T6NTWiy9nrn4Z2d022zHBPDkb9bBCSZ3_3thrP6rrkYMf86AnRdfCyzBCdpC1Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b925d659.mp4?token=UZ_a4h0v53g5DG73ZUvPP00chJ0XkI7AicPOHWiMmUxy7-8GiSEww4uzPNB_xI2f7cd_Hr2B3Yp2Ix6jpHWCRjFYjlaOvtqqynyZKfP89ijVIRjMhHaaUyFfi15Qj3R_r_S_hI6Hxuk9YjUUmxC281NvxKmRZ_0L-ShAdGiJH-Rg9dMT-MLwZnUBUB875JV72xG3pjJZaX_42ZGq3uQNbn1vdH9nkbgWnNaEvSRkk9K5fVNZDSaAxOwF3HMjkYSYoGcC2Ktz1qpAKuO45iF55u2T6NTWiy9nrn4Z2d022zHBPDkb9bBCSZ3_3thrP6rrkYMf86AnRdfCyzBCdpC1Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: «موساد همچنان در خط مقدم نیزه در نبرد ما علیه تجاوز ایران باقی خواهد ماند.
ما اجازه نخواهیم داد رژیم ایران چرخ تاریخ را به عقب برگرداند. ما اجازه نخواهیم داد به سلاح هسته‌ای دست پیدا کند. ما اجازه نخواهیم داد موجودیت ما را تهدید کند.
این رژیم محکوم به زوال که پایانش فرا خواهد رسید و ما به رسیدن آن به این سرنوشت کمک خواهیم کرد.
این رژیم دیگر باز نخواهد گشت تا ما را با بمب‌های هسته‌ای و هزاران موشک بالستیک مرگبار تهدید کند.
این دستور من است و این مأموریت شماست، رومن.»
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13281" target="_blank">📅 21:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ربطی نداره ناو لینکلن ، بوش و ناو آبی خاکی‌ تریپلی و کلی‌ ناوشکن هستند و کافیه!</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/13280" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادعای شبکه ۱۲ اسرائیل : دستور تخلیه ضاحیه جنوبی بخشی از هماهنگی نتانیاهو و ترامپ برای فشار به ایران تو مذاکرات بوده و نه برای حمله مستقیم به ضاحیه
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/13279" target="_blank">📅 20:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYPB2Nc-NtZm8vgXz1Q63X7IqQhF8fTiOpkxBcsjEcRnQ0oOR_50uBK4lQdn2FibUvUjOi8koHkD-NSMN87UNv0F2dYlfa5DS6do55iPBbqQZZCbWIrbaa1jJfkNvlezRN6ivIeWito24RRz3IukhNiLCmJIqWOufFaKpC4iqJ4l-R-Ezs3gH-f-AASmfqcLV9tJejMni39WeDHY7EiBJSTGvhAHwEmPkQqq1wtCVUJZcsXd2mVRMWjCwgc-M6mHJaCJgOebDSdFK9tIDK3MF4oJ3oGNNsBeZsCDf7nRmUQhFPHDEkUDKI9BIs-9Pqy7vIpqGyEvepkPDGP2uL5OzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :«گزارش‌های فیک‌نیوز که می‌گویند جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز است با هم صحبت نمی‌کنند، کاملاً نادرست و اشتباه است.
گفت‌وگوها میان ما به‌صورت پیوسته ادامه داشته است؛ از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش و امروز.
این گفت‌وگوها به کجا می‌رسد، کسی نمی‌داند؛ اما همان‌طور که به ایران گفتم: “وقت آن رسیده، به هر شکل ممکن، به یک توافق برسید. شما ۴۷ سال است که این کار را ادامه داده‌اید و دیگر نمی‌توان اجازه داد ادامه پیدا کند!”
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13278" target="_blank">📅 20:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b6ab4e43.mp4?token=Jl2-boGcldtZvA24avJ2JcoL4CmMqJvN_H4LE9a8dB4dRBROvckkCiGAeH51oGZq5VQIVl97cPwSSCTUuL1hK7HrX68nb7nbsUn1elFOZhLSe6Z8zG5OJ7X6Z02FbRDY2VoqA5MRX7aLxTNuwi2AcCh2bdaBJe_Cgkm5xEeRqoguALdkrZFQol4PuA8_ZIJQddwibn7Tc5HZRatq_xoNrX6vsn9CETTICuPw8fnpDJGSdVXSr3T9gKlqAjSL2F7UR9FxWggUH3FZa6eGXKlh-AJUo8uu2zbV-gWr2j6kbN4N0e5W1CjaQqlMjBOf0eon6BAkGmfSdZpaK-dAvGu7xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b6ab4e43.mp4?token=Jl2-boGcldtZvA24avJ2JcoL4CmMqJvN_H4LE9a8dB4dRBROvckkCiGAeH51oGZq5VQIVl97cPwSSCTUuL1hK7HrX68nb7nbsUn1elFOZhLSe6Z8zG5OJ7X6Z02FbRDY2VoqA5MRX7aLxTNuwi2AcCh2bdaBJe_Cgkm5xEeRqoguALdkrZFQol4PuA8_ZIJQddwibn7Tc5HZRatq_xoNrX6vsn9CETTICuPw8fnpDJGSdVXSr3T9gKlqAjSL2F7UR9FxWggUH3FZa6eGXKlh-AJUo8uu2zbV-gWr2j6kbN4N0e5W1CjaQqlMjBOf0eon6BAkGmfSdZpaK-dAvGu7xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو ادعای مسلح کردن مخالفین حکومت ایران توسط دولت آمریکا را رد کرد
:
«من از هیچ برنامه‌ای برای مسلح کردن غیرنظامیان در ایران برای سرنگونی دولتشان آگاه نیستم.
منظورم این است که ممکن است کشورهای دیگری این کار را انجام دهند، یا گروه‌های دیگری این کار را انجام دهند، اما مطمئناً دولت ایالات متحده این کار را نمی‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/13277" target="_blank">📅 20:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الان کجاست احمدی نژاد</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/13276" target="_blank">📅 20:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGYM</strong></div>
<div class="tg-text">الان کجاست احمدی نژاد</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/13275" target="_blank">📅 20:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmkfW6y4FsrUgeEwKbbs-cwuRkTNFviVckGdWo5d2SW4yY9QSzgTHOrXVSEy0rIBqFZLk4iDDYYURk2OFfsAOopyt2HA2sD5AB9R7Y2Hm52So9KLwcA3XgBzIsvDvT9PwZBvgOTRaNNT1bbhrku_QK2II7H8MgGlxmnWYHtgEILJFZLeHJhgSI1X1BaCefxaswH2kjzrtneaohy7LwhQV0RVEX80WYetxJjxVAjusc6qoQYudTuyfbBp3EstGjaumEq1SWqTS6nJNzx6ACxY76VGdA_aoZRKG0H6BrPW0db8vWkzeSKALiOCCUY6apzWRq1F8XhHpf_Xm6c16U6oew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ال احمدی نژاد السیسی
🥴
پس بگو این مدت برای چی انقدر ‌رفت بوتاکس کرد و به خودش رسید، قیافه درست کرد.
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/13274" target="_blank">📅 20:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f41232db.mp4?token=JkJsdK8ZPrcUCO1meZ8bpMn2IlKm-8uMgXi6o4WwCHHBq3jaItY_1rf1CuNYjvx9xot0HHI02-kGtubDiDgORoNpP5QQOmxGGyPomoTllp7M2L4OfOnfs3VasXYwFfYuoCUsn87GMOX-SaftUwfVsBMjsYe80tnb1Cd1JzjiUaEPzT4RKHdyjid5iy4tD1eTJwBu9i7jCdhQ40mkhqo_qXFYfrU18jzAW1m9a37s5dicT2sOCHIf4Qfkap6xaOtVaolxvc3XFN7s3E7aBHVYe__TWYg-bxE_fFl-wKhtx1ujo2xPWEjUAd88OxuMqTa8AWP4HsG1nWsSnW92eEK8ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f41232db.mp4?token=JkJsdK8ZPrcUCO1meZ8bpMn2IlKm-8uMgXi6o4WwCHHBq3jaItY_1rf1CuNYjvx9xot0HHI02-kGtubDiDgORoNpP5QQOmxGGyPomoTllp7M2L4OfOnfs3VasXYwFfYuoCUsn87GMOX-SaftUwfVsBMjsYe80tnb1Cd1JzjiUaEPzT4RKHdyjid5iy4tD1eTJwBu9i7jCdhQ40mkhqo_qXFYfrU18jzAW1m9a37s5dicT2sOCHIf4Qfkap6xaOtVaolxvc3XFN7s3E7aBHVYe__TWYg-bxE_fFl-wKhtx1ujo2xPWEjUAd88OxuMqTa8AWP4HsG1nWsSnW92eEK8ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های
تامر هایمن
رئیس سابق
سازمان اطلاعات نظامی اسرائیل (AMAN):
عملیات سری ترامپ و کردها و احمدی‌نژاد !
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/13273" target="_blank">📅 19:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دایرکتاتون انقدر ماه بود که الان میرم اتاق جنگ
💻</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/13272" target="_blank">📅 18:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0a60d360.mp4?token=Bhut3vGH6_Mdjwl7M7C38GjB2_4LDE0521hpILZdhjXXplTLdtutn697noGH64fSpKWAs38BLBuGnpDIeDoW4Y-caKNMozIhc0MvfxfLpNq12B9cfidO-Q9SRQpjjkLiWwZVNJ1pM8QXHSnyPLPgAWYdPVRDk5-7z_jDGk-epqcIFb-cDaCxeA6yhM0YTw_tfWeaRLGTOwYYb7cMqiu37BaDFb0OvTzMDpjFVeLnKCxDlZzSOzaGGB8z8dVySR8cKAQQRv7GkNml6Kn9QbKrpQQT7g95MiSPfOl6Xe0wcLnT_5LKf7X2isp1mu7e4Ia5Rqlbvt0-Mkt98_D9gTCxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0a60d360.mp4?token=Bhut3vGH6_Mdjwl7M7C38GjB2_4LDE0521hpILZdhjXXplTLdtutn697noGH64fSpKWAs38BLBuGnpDIeDoW4Y-caKNMozIhc0MvfxfLpNq12B9cfidO-Q9SRQpjjkLiWwZVNJ1pM8QXHSnyPLPgAWYdPVRDk5-7z_jDGk-epqcIFb-cDaCxeA6yhM0YTw_tfWeaRLGTOwYYb7cMqiu37BaDFb0OvTzMDpjFVeLnKCxDlZzSOzaGGB8z8dVySR8cKAQQRv7GkNml6Kn9QbKrpQQT7g95MiSPfOl6Xe0wcLnT_5LKf7X2isp1mu7e4Ia5Rqlbvt0-Mkt98_D9gTCxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«ما در حال مذاکره هستیم و می‌گویم مذاکره، چون مذاکره با ایران شبیه مذاکره با سوئیس نیست، درست است؟ کاملاً متفاوت است. متأسفانه این مذاکرات نیازمند استفاده از واسطه‌هاست.
اما اکنون با چشم‌اندازی روبه‌رو هستیم که ممکن است امروز، فردا یا هفته آینده به نتیجه برسد؛ اینکه برای نخستین بار، دست‌کم تا جایی که من به خاطر دارم، ایران پذیرفته است درباره بخش‌هایی از برنامه هسته‌ای خود مذاکره کند؛ موضوعاتی که تنها یک ماه پیش، یا حتی یک سال پیش، نه‌تنها حاضر به مذاکره درباره آن‌ها نبود، بلکه اساساً از مطرح کردنشان نیز خودداری می‌کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/13271" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر امور خارجه آمریکا , روبیو : در حال حاضر نیروی دریایی ایران وجود ندارد، بلکه گروهی از قایق‌های تندرو حامل رگبار هستند.
اگر ایران بر بستن تنگه‌ها اصرار کند، ما آنها را برایشان خواهیم بست، و این کاری است که ما از طریق محاصره مؤثر انجام داده‌ایم.
امیدواریم با ایران به توافقی برسیم که منجر به بازگشایی تنگه‌ها شود.
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13270" target="_blank">📅 18:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13268">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک منبع آگاه : خلبان هواپیمای اف-۱۵ آمریکایی که در طول جنگ بر فراز ایران سرنگون شد، همان خلبانی است که هواپیمایش بر فراز کویت در اثر اشتباه پدافند کویت نیز سقوط کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/13268" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13267">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ربطی نداره ناو لینکلن ، بوش و ناو آبی خاکی‌ تریپلی و کلی‌ ناوشکن هستند و کافیه!</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/13267" target="_blank">📅 17:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13266">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli Hb</strong></div>
<div class="tg-text">سلام ی سوال
اگر امریکا میخواد جنگ کنه چرا پس ناو جرالد فورد و باکسر برگردوند؟
این خودش نشونه این نیست که جنگی درکار نیست</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/13266" target="_blank">📅 17:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13265">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صبح بخیر من دقیقا ۲ هفته پیش دیدم و گفتم برگشت ! تازه رسانه ها فهمیدن در این پست مستند شده !
https://www.instagram.com/reel/DYiHl04xutP/?igsh=MWZhNHllczYzNGtvaA==</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/13265" target="_blank">📅 17:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13264">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromkiarash</strong></div>
<div class="tg-text">تروخدا بگو ناو باکسر میگن برگشته دروغه؟</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13264" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13263">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک منبع آگاه به فارس: درحال حاضر تبادل پیامی با آمریکا انجام نمی‌شود
تبادل پیام بین ایران و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشنگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده.  درحالی‌که دیشب ترامپ مدعی شده بود که گفت‌وگوها با ایران با سرعت بالایی در جریان است، این منبع آگاه تصریح کرد که آخرین پیام جمهوری به فارس اسلامی ایران به واشنگتن، پیامی آشکار در خصوص لبنان بود که بازتاب گستردۀ بین‌المللی یافت.
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13263" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13262">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6b42048d.mp4?token=cHMM3CXyjXAk2Bq_e1RKvEA235iFs6LfyuK42IuYCAs_ieSrH6E3YkKkRdJdu_Iq286NcTcINRqBRAC8g64iXkYv-RYifZWIAdBkIhoiwKCMUDm18SnJpISARq31KaQyXdjkCVG-Udz0kBuInBfatGCKj60OdJG2--Yu_kgPM57UEQRmSVUmjXu3ueJEOzGKrQSC4ysqDdMs4tFMwal3_jzo1__uPyOx7yiY9SJZFxYDGtxJxmSNofmtss8oV85lDSHPYACGIP1VYG6Rt23jc1FkizJy0U0x9W7STuTfK6N85oQv98eFv9W-6oNF5M8zeFtnocaZGWjiq8C4EPQYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6b42048d.mp4?token=cHMM3CXyjXAk2Bq_e1RKvEA235iFs6LfyuK42IuYCAs_ieSrH6E3YkKkRdJdu_Iq286NcTcINRqBRAC8g64iXkYv-RYifZWIAdBkIhoiwKCMUDm18SnJpISARq31KaQyXdjkCVG-Udz0kBuInBfatGCKj60OdJG2--Yu_kgPM57UEQRmSVUmjXu3ueJEOzGKrQSC4ysqDdMs4tFMwal3_jzo1__uPyOx7yiY9SJZFxYDGtxJxmSNofmtss8oV85lDSHPYACGIP1VYG6Rt23jc1FkizJy0U0x9W7STuTfK6N85oQv98eFv9W-6oNF5M8zeFtnocaZGWjiq8C4EPQYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آهنگ تابستون کوتاه ورژن عرزشی
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13262" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13261">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">واشنگتن‌پست: مذاکرات ایران و آمریکا در بن‌بست است
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/13261" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13260">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک افسر ارشد ایرانی به CBS گفت که جنگ تازه با آمریکا به نظر «اجتناب‌ناپذیر» می‌آید چون اسرائیل و حزب‌الله به درگیری ادامه می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13260" target="_blank">📅 15:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جناب شاهزاده رضا پهلوی گرامی،   پدر ، این پیام، جمع‌بندی دیدگاه‌ها و پیشنهادهای گروهی از ایرانیان داخل و خارج کشور با هدف تقویت انسجام ملی و ایجاد مسیر عملی برای دوران پیش از گذار است.  عناوین چکیده از هزاران پیغام مردمی به‌صورت خلاصه:  * ضرورت ایجاد ساختار…</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13259" target="_blank">📅 15:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جان بولتون :
ایران باور دارد که می‌تواند از ترامپ بیشتر دوام بیاورد، یعنی صبرش بیشتر از اوست
، چون ترامپ شدیدا نیاز دارد که قیمت نفت را پایین بیاورد.
وقتی کسی سه بار بگوید «برایم مهم نیست»، شاید یعنی واقعاً برایش مهم است.
اگر ترامپ نگران نبود، با نتانیاهو تماس نمی‌گرفت تا در لبنان آتش‌بس برقرار کند.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13258" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13257">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چرا کامنت فقط 3k لایک خورده؟از کانال 280 هزار نفری انتظار بیشتری هست بخدا،به بچه ها بگو یه تکونی بخورن یه خودی نشون بدیم</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13257" target="_blank">📅 14:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13256">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSohrab</strong></div>
<div class="tg-text">چرا کامنت فقط 3k لایک خورده؟از کانال 280 هزار نفری انتظار بیشتری هست بخدا،به بچه ها بگو یه تکونی بخورن یه خودی نشون بدیم</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13256" target="_blank">📅 14:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شبکه اجتماعی لینکدین رفع فیلتر شد
شبکه اجتماعی لینکدین پس از بازگشایی تدریجی اینترنت بین‌الملل، بدون نیاز به فیلترشکن در دسترس کاربران ایرانی قرار گرفت.
صفحه من در لینکدین هم داشته باشید :
https://linkedin.com/in/seyed-yashar-tavakolian-a26a61188</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13255" target="_blank">📅 14:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده بیش از پیش رویکرد بی‌طرفانه عمان در قبال تهران را خصمانه تلقی می‌کند و این کشور را تحت فشار قرار داده است تا با انتخاب یک طرف، روابط دیپلماتیک خود با ایران را قطع کند.
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13254" target="_blank">📅 14:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13253" target="_blank">📅 14:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زیر پست صفحه دوم شاهزاده رضا پهلوی و بانو نور پهلوی کامنت مورد نظر را گذاشتم. نیاز به همیاری شما داریم برای این مرحله از فراخوان. لطفاً کارهای اداری را انجام دهید، طبق برنامه.  https://www.instagram.com/reel/DZFAJOWRays/?igsh=NmVldnV2aW1jaHE3</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/13252" target="_blank">📅 14:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13251">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/13251" target="_blank">📅 13:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برادر … کامنتت پیدا نمیکنم راهی نداره سریع بشه پیداش کرد من چون فالوت ندارم اینستا اگه راهی هست تو چنل بگو</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/13250" target="_blank">📅 13:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from<>CNA<></strong></div>
<div class="tg-text">برادر …
کامنتت پیدا نمیکنم
راهی نداره سریع بشه پیداش کرد من چون فالوت ندارم اینستا
اگه راهی هست تو چنل بگو</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/13249" target="_blank">📅 13:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ایسنا: اپراتورها پول کسانی که اینترنت پرو خریدند را پس نمی‌دهند و فقط می‌شود اینترنت پرو را به اینترنت عادی تغییر داد
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/13248" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جناب شاهزاده رضا پهلوی گرامی،   پدر ، این پیام، جمع‌بندی دیدگاه‌ها و پیشنهادهای گروهی از ایرانیان داخل و خارج کشور با هدف تقویت انسجام ملی و ایجاد مسیر عملی برای دوران پیش از گذار است.  عناوین چکیده از هزاران پیغام مردمی به‌صورت خلاصه:  * ضرورت ایجاد ساختار…</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/13247" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رئیس سابق موساد در مراسم خداحافظی:
اردوغان ترامپ را متقاعد کرد که عملیات نظامی به رهبری کردها را که قرار بود اولین گام در یک طرح گسترده تر علیه رژیم ایران باشد، لغو کند.
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/13246" target="_blank">📅 13:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو: تا زمانی که ما هستیم، نه ایران و نه «همسایگان» آن به سلاح هسته‌ای دست نخواهند یافت.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/13245" target="_blank">📅 13:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ائتلاف «اوپک پلاس» در حال برنامه‌ریزی برای افزایش تولید نفت در ماه ژوئیه است.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13244" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار : دیوید بارنئا، رئیس پیشین موساد، پس از پایان دوره پنج‌ساله خود در ژوئن ۲۰۲۶ سمتش را ترک کرد و استعفا نداد.
پس از او،
رومان گوفمن
، سرلشکر ارتش اسرائیل و دبیر نظامی پیشین نتانیاهو، به ریاست موساد منصوب شد. او از نزدیکان نتانیاهو محسوب می‌شود و در دوره جنگ ایران و اسرائیل در حلقه تصمیم‌گیری‌های امنیتی حضور داشته است. گوفمن برخلاف بسیاری از رؤسای پیشین موساد، سابقه طولانی در این سازمان ندارد و بیشتر از بدنه ارتش به این سمت رسیده است. برخی گزارش‌ها می‌گویند انتخاب او پس از ناکامی برآوردهای اطلاعاتی قبلی درباره امکان سقوط سریع حکومت ایران انجام شد و ممکن است نشانه‌ای از تغییر روش باشد، نه تغییر هدف.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13243" target="_blank">📅 12:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b8efdf64.mp4?token=pUbLXjnE-eCsPssRvqLqUS1H07ZRVt29V3JespzqOx1hxqU0R875i5AUKronopDykl1kD5V5NN6mVGS_77ZHu8HCz-Ro-M8ahMVbifwWu5V-VUNJRNQ9GPGsgBzPlq5XW6a1rdIA0b42XSqAVmCOuCT92oS4s6C7f1YlSGHyCVK3eIxUUyTqzThYlaDZyLHY4g4yd-sN6S1v_AEjpngmbzdUCSWN6JZuNv7retvTqvEH-thh50bxO_zf_8SZlfmkHNV_eh4Xp3PqXFx9YFfudIzVx_PwBzLzt3lqSyOG8KE8Yr1FASABqKkRobv2TXPz-z8k8ZmUjXDmt8JAs84KHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b8efdf64.mp4?token=pUbLXjnE-eCsPssRvqLqUS1H07ZRVt29V3JespzqOx1hxqU0R875i5AUKronopDykl1kD5V5NN6mVGS_77ZHu8HCz-Ro-M8ahMVbifwWu5V-VUNJRNQ9GPGsgBzPlq5XW6a1rdIA0b42XSqAVmCOuCT92oS4s6C7f1YlSGHyCVK3eIxUUyTqzThYlaDZyLHY4g4yd-sN6S1v_AEjpngmbzdUCSWN6JZuNv7retvTqvEH-thh50bxO_zf_8SZlfmkHNV_eh4Xp3PqXFx9YFfudIzVx_PwBzLzt3lqSyOG8KE8Yr1FASABqKkRobv2TXPz-z8k8ZmUjXDmt8JAs84KHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دموکرات‌ها نیروی نیابتی ایران هستند !
برایان مست، نماینده جمهوری‌خواه کنگره
:
"تهدید شماره دو ما، جدا از سپاه پاسداران، دموکرات‌های مجلس نمایندگان هستند. آنها دومین نیروی نیابتی بزرگ ایران هستند!"
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13242" target="_blank">📅 11:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">روابط عمومی۳پا صاحب‌ الزمان استان اصفهان : احتمال شنیده شدن صدای انفجار کنترل شده در محدوده جنوب اصفهان ، بهارستان و اطراف وجود دارد.
این انفجارات امروز سه شنبه ۱۲ خرداد ماه از ساعت ۱۰ صبح تا ۱۸ بعدازظهر انجام می شود و جای هیچ نگرانی برای مردم عزیز نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13241" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سخنگوی ۳پا : برای تمامی سناریوهای احتمالی آمادگی داریم
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/13240" target="_blank">📅 11:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c22e4a8d1.mp4?token=eGvEfAGbwlWs1kkFzEYF0hhaQ4M49wt6yobOtbgajoWKBK2jfBnbh0TxTJ0WDxg4ddw0sy6sv0OhMD1DH3g6zpPtz74l-_J8XgKHYJDfuVh-OfVpyJ7M5IujjG4rHNWjr2shHBIbwEfkQmYO-sDm2FUny42NWCDKTNnLjEBFEeriL9GKj1myNprPX_Csgo11VzM6i8tkAzwBWmPI2-zvIfUhGuaReulTHkyAvgHUoLJ-JNRxZ7qdxU2gi0frOKCYgvgxa4e3RwYZtFZAY8sGIjfBfFm-6Mx-ZxzzBMcUmSI9hlaWGabdkZ88QDYCnA6BR-HP3cVqBJi9qCeMbs43Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c22e4a8d1.mp4?token=eGvEfAGbwlWs1kkFzEYF0hhaQ4M49wt6yobOtbgajoWKBK2jfBnbh0TxTJ0WDxg4ddw0sy6sv0OhMD1DH3g6zpPtz74l-_J8XgKHYJDfuVh-OfVpyJ7M5IujjG4rHNWjr2shHBIbwEfkQmYO-sDm2FUny42NWCDKTNnLjEBFEeriL9GKj1myNprPX_Csgo11VzM6i8tkAzwBWmPI2-zvIfUhGuaReulTHkyAvgHUoLJ-JNRxZ7qdxU2gi0frOKCYgvgxa4e3RwYZtFZAY8sGIjfBfFm-6Mx-ZxzzBMcUmSI9hlaWGabdkZ88QDYCnA6BR-HP3cVqBJi9qCeMbs43Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رئیس موساد بارنیا در مراسم خداحافظی و تحویل پست در حرف آخرش : «تغییر رژیم در ایران یک هدف ممکن و دست‌یافتنی است.»
‏او در مراسم خداحافظی‌اش تاکید کرد که سرنگونی جمهوری اسلامی ماموریتی عملی است که به عزم و اراده نیاز دارد و باید در صدر اولویت‌ها بماند.
‏پیام کاملاً روشن است: تضعیف این رژیم تروریستی کافی نیست. تهدید بلندمدت خاورمیانه تنها زمانی تمام میشود که رژیمی که تامین‌کننده پول، سلاح و هدایت تروریسم در منطقه است، برای همیشه سرنگون شود. ⁦
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13239" target="_blank">📅 10:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13238" target="_blank">📅 10:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13236">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مدیرکل آژانس بین‌المللی انرژی اتمی:
انتقال ذخایر اورانیوم غنی‌شده ایران به خارج از کشور کاری «دشوار است اما غیرممکن نیست».
چنین عملیاتی آسان نیست، چراکه (این ماده) به شکل گاز است، بسیار آلاینده است و عملیات ساده‌ای نیست
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13236" target="_blank">📅 10:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13235">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرگزاری «مهر» به نقل از یک منبع آگاه درباره روند مذاکرات با آمریکا نوشت «متن نهایی همچنان در حال گفت‌وگو در تهران است و هنوز پاسخی ارسال نشده است.»
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13235" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13234">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع : ترامپ نمی‌خواهد قطع رابطه علنی با نتانیاهو رخ دهد
@withyashat</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13234" target="_blank">📅 09:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13233">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMat</strong></div>
<div class="tg-text">داداش خیلی ساده بخام بهت بگم اگر من تو شرایط تو بودم هرگز همچین مسعولیتی رو قبول نمی‌کردم...
چون شما هرکاری هم بکنی ازت ایراد میگیرن در هر صورت ‌
خیلی باید مرام معرفت و دل بزرگی داشته باشی که بیای همچین کاری بکنی
باعث افتخاری
👌</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/13233" target="_blank">📅 09:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13232">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from💎masih💎</strong></div>
<div class="tg-text">سلام یاشار داداشم من به عنوان یک ایرانی و هم وطن بهت افتخار میکنم واقعا الان خیلیا ناامید شدنو هیچکار نمیکنن حتی اونایی که تند تند استوری میذاشتن الان فقط از زندگی خودشون میذارن واقعا اگه این انقلاب شکل‌ بگیره شاهزاده بزرگمون بیاد همه ی ایرانیا مدیون تو هستن
❤️
😘
خیلی دلم میخواد این متنو بذاری چنل و در کل بهت جوری افتخار میکنم که تو زندگیم به هیچکس حتی خودم اینجوری افتخار نکردم
💪
❤️</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13232" target="_blank">📅 09:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الجزيرة: حمله اسرائیل به شهر الغندوریه در منطقه بنت جبیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13231" target="_blank">📅 09:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزیر آموزش‌وپرورش: ‌امتحانات نهایی پس از تأیید مراجع ذی‌صلاح برای فراهم بودن شرایط حضور دانش‌آموزان در حوزه‌های آزمون، برگزار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13230" target="_blank">📅 09:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13229" target="_blank">📅 09:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پست شد اینستاگرام سر‌ساعت  https://www.instagram.com/p/DZDi1pCEfvI/?igsh=MWN3ZWNhdWxqbmk0OA==  لطفاً این پست را استوری کنید و برای تمام افراد مرتبط با شاهزاده رضا پهلوی و شخص خود ایشان و تمامی پیجهای ایشان ارسال کنید.</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/13228" target="_blank">📅 09:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRLSJg_8SHXgfYvjyRhUifl4kLYBZL40avO7J_DZvpUGmrxFsvEzu4awt9g3JI_wC1wYm-qqLZvtYqbwngn43e32n7ToN6racIzy4xeW3kAOpkgaJYKB4Z8emdgZ4IzlCWgf9nZhb-XTzO55t17RGfRdNUeh30n0dMK1ED_vc_hPPfWCFh5agIDpGB-hSHQp5O_FRE9ThupFMcV8ILyHpmV3CQSNyJDax_YJLlS899hvqzlvx6mVkmk1hDXu2UKVddQleQ4IPDS3UfIanAQRcXmEax22iYDWTfQarjMbFrsX0zj8pAMOR4Uywbuwy2aI06Ll39fKJhKVm_MgTzo5Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/13227" target="_blank">📅 09:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13226">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ در تروث : اگر ایران تسلیم شود، بپذیرد که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده است، و نیروی هوایی‌اش دیگر همراه ما نیست، و اگر تمام ارتش آن از تهران خارج شود در حالی که سلاح‌ها را زمین گذاشته و دست‌ها را بالا برده‌اند و هر کدام فریاد می‌زنند…</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/13226" target="_blank">📅 08:31 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
