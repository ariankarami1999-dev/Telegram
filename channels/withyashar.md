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
<img src="https://cdn4.telesco.pe/file/BLNcqQmCNugwWGuhz8fm6pYR0TGtIy63oKNzmI9-CKvyKBCaxHeNZQqxzMczLXRFTO2tTz4PbtSi9fAFql4bseQG5v-I1uEn6nzL_Rc42rGlGYbLozTWhUnSUDVMyzRAryZWWEDe1Ewr_CIoJ6n3sh5S3tFbLgnwwsLOFDfSZtUxk7Xw64-OMr1I8w8FIncv0eWDs6qboVEMFFSUl_MD1sZmA1bTGA70l95uIJcMowtjFyno5xm3AQLo2oMd6EoYZ2K9ITVwXWUeq69z02nFs7Va8H9bINfpcJBtuosxoytxMPCLDO-zNVA-4wEDwsiUz8KWbFXYoE-Hxy3feg-Efg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 22:38:00</div>
<hr>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ از لغو تعرفه‌های ویسکی ایرلندی خبر داد و گفت «همه مدام پیگیر این موضوع بودند»
@WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/23042" target="_blank">📅 22:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/23041" target="_blank">📅 22:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from... ...</strong></div>
<div class="tg-text">درود آقا یاشار. السیسی وجود دارد در داخل رژیم؟ و بنظرتون اگه وجود دارد چه زمانی رو میشود؟</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/23039" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سی‌ان‌ان: عمان پیشنهاد ایران برای دریافت اجباری عوارض را رد کرد و پرداخت‌های داوطلبانه برای ایمنی ناوبری و زیست‌محیطی را پیشنهاد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/23038" target="_blank">📅 21:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5wSFouMHX2qCqp5IQbd_JW0kOW-xpCb1mhTsbCdqg4ebL3d9BCxKdhqTlFADqhIUEgzlrDky2AVrBz5EPXXjhNMP4Nlk8tNZLOoHAC7LXlYiTvNkCsGPrRvPfulDUZwn6GT7jGVcdnP60ztf_AXa0VPh9dxvP7PgLGJNj577VYtpjC_uSu16q9ajlXifCvvCkLs7KyyvT2yGQLEniN8bSBdJw5TR4i9yBOTEzeSyU5JQ_8GNcI8cIrNuFrkNepR4hNm1si5HJVpQqFovPpKY6YkjEhfeuCHsZ2dQ0xqd7cFsjvWEMHMEWN-ZXrKrJvPPeJ8fHKXfnJUW0hX08dOkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون پرتاب سه موشک از یک نخلستان نزدیک سیریک به سمت تنگه هرمز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/23037" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f697ad6f42.mp4?token=k0pyR5cEt8B9fRtChPzTsHa1D0yEhjopNUNOktRXGWwH-ntCEnp4jrfLcCPNEPyQrQ5Rz5n70Hyqg_vkFDd_xetp6pIQmuqKijBpC2nzWByezr6wtZA7db5OPl4sAlozHfwa6OjNYyge-Q1pAjYQrWx7br-l_P4PKJwPLUXCvHEzVBgHK-R2fkZhGXGYaZBkBHWKQsfulFWFRjTaahAH4o-nAXamLzLjv7CQxYQjN2PUy_H38zBmAi4hlYwric_B9xfmN9SOeo7tcrVYmiMgyiZBCK8J4qobvERLayk9gjJOfct0kq0cPi8mHJzjRydYrQ2Wf-P_3IsVlG4HAu2zsxlITykatjS7HDD8mKLlZHIr8PdhH8Urubg2wE8SQgVHtdXaGr0jhmwPDtlwJc5k_ycmAGKfRUBoDWEqREisekhVxw70p66sdpsA_deGxTyQIStKVxFqMLwSU9b1fUYVnVbdhiAi2EVY1IlIFMR0Q9DNWh3kAMGRUR2gyrZ9sM5hKkw-vTI0Gtaw7KLArbxsQKgvzFVyHj0be3ZFSjrvNzUD-h3bX3ZgP48hC_yxZbF3KNxxH7notSH9HKsTZTkst-j1eQxRfPWZMG9Jd864I7nNWsjnO3dfYbPS60mggSzgSGBqwFoml_Jtv9MdjrICL0iGSeyC_xbzzLxqEqQlzLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f697ad6f42.mp4?token=k0pyR5cEt8B9fRtChPzTsHa1D0yEhjopNUNOktRXGWwH-ntCEnp4jrfLcCPNEPyQrQ5Rz5n70Hyqg_vkFDd_xetp6pIQmuqKijBpC2nzWByezr6wtZA7db5OPl4sAlozHfwa6OjNYyge-Q1pAjYQrWx7br-l_P4PKJwPLUXCvHEzVBgHK-R2fkZhGXGYaZBkBHWKQsfulFWFRjTaahAH4o-nAXamLzLjv7CQxYQjN2PUy_H38zBmAi4hlYwric_B9xfmN9SOeo7tcrVYmiMgyiZBCK8J4qobvERLayk9gjJOfct0kq0cPi8mHJzjRydYrQ2Wf-P_3IsVlG4HAu2zsxlITykatjS7HDD8mKLlZHIr8PdhH8Urubg2wE8SQgVHtdXaGr0jhmwPDtlwJc5k_ycmAGKfRUBoDWEqREisekhVxw70p66sdpsA_deGxTyQIStKVxFqMLwSU9b1fUYVnVbdhiAi2EVY1IlIFMR0Q9DNWh3kAMGRUR2gyrZ9sM5hKkw-vTI0Gtaw7KLArbxsQKgvzFVyHj0be3ZFSjrvNzUD-h3bX3ZgP48hC_yxZbF3KNxxH7notSH9HKsTZTkst-j1eQxRfPWZMG9Jd864I7nNWsjnO3dfYbPS60mggSzgSGBqwFoml_Jtv9MdjrICL0iGSeyC_xbzzLxqEqQlzLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@WarRoom</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/23036" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e431617c.mp4?token=CWrwGRRTqw86UPuCJ3b9PC9vtxdz0sjRxcMuFKqCW_VUeTwyNFHwac1znjwgP-WU1dOck0kpj-xlD50H7MNkk0sxG97JS8JVM6DmkS88QmcJ_SfmiZAJvVkILwxpXE9mbOpLlu8SYWBR-Kxva1ZOUVgDXMiyU6uWehP9pC-X59wlkJA-AyqwHJ6hsM3hJEdrb657tETue5XX3XB1UDDKLXHYfZAcqyG0XxU_Lt2HEhHr0L1rC-qYpZ8OxH3ecuf8Mj0z0t8lOUkdF5_5YuX-PZ5qRoTj6OgFk2FGRQhYmpf5I5_pTYwLoQNEQ67YBspUipk-KGyk4cu9ZlkaewjXyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e431617c.mp4?token=CWrwGRRTqw86UPuCJ3b9PC9vtxdz0sjRxcMuFKqCW_VUeTwyNFHwac1znjwgP-WU1dOck0kpj-xlD50H7MNkk0sxG97JS8JVM6DmkS88QmcJ_SfmiZAJvVkILwxpXE9mbOpLlu8SYWBR-Kxva1ZOUVgDXMiyU6uWehP9pC-X59wlkJA-AyqwHJ6hsM3hJEdrb657tETue5XX3XB1UDDKLXHYfZAcqyG0XxU_Lt2HEhHr0L1rC-qYpZ8OxH3ecuf8Mj0z0t8lOUkdF5_5YuX-PZ5qRoTj6OgFk2FGRQhYmpf5I5_pTYwLoQNEQ67YBspUipk-KGyk4cu9ZlkaewjXyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام، می‌گوید هیچ‌گونه نگرانی‌ای بابت کمبود مهمات آمریکا ندارد.
«ما به‌خوبی مسلح و برای هرگونه وضعیت احتمالی آماده هستیم.»
کوپر در پاسخ به این پرسش که آیا نگران تهدیدهای آینده است، گفت: «خیر، نگران نیستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/23035" target="_blank">📅 20:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/23034" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا تنها</strong></div>
<div class="tg-text">سلام .
میشه دلیل اینکه بنده رو از گروه بیرون کردید رو بدونم</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/23033" target="_blank">📅 20:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/23032" target="_blank">📅 20:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قصه قورباغه و دیگ آب جوش
@WarRoom
🐸</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/23031" target="_blank">📅 20:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اطلاعیه رسمی قرارگاه جانفدای کشور:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قرار است به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فوری اعزام شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/23030" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/23029" target="_blank">📅 20:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMalekshahirad</strong></div>
<div class="tg-text">رویا چرا الکی می‌فروشی ب مردم مرد نامومن</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/23027" target="_blank">📅 19:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23026">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فایننشال‌تایمز :
حمله پهپادی روسیه به قطار نزدیک مرز لهستان:
یک پهپاد روسی امروز به
قطار تخلیه‌شده کی‌یف–ورشو
در نزدیکی مرز لهستان اصابت کرد؛ این قطار تنها حدود یک ساعت پس از قطاری حرکت می‌کرد که
بوریس جانسون، نخست‌وزیر پیشین بریتانیا، کارل بیلت، نخست‌وزیر پیشین سوئد و شماری از دیپلمات‌ها و مقام‌های اروپایی
در آن حضور داشتند. قطار حامل مقام‌ها لحظاتی پیش‌تر از منطقه عبور کرده و وارد خاک لهستان شده بود. قطار هدف‌قرارگرفته ۲۰۶ مسافر داشت و پیش از حمله به دلیل هشدار پهپادی تخلیه شده بود؛
در این حمله کسی زخمی نشد
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/23026" target="_blank">📅 19:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba17bf936a.mp4?token=XLz18P7oRmRCOlcdolhwK2gweRZgB70yQfnlSSGjSmy03JjsjzDNtezfNE4xICa7-WQz1uTZBHxihZ_x_YTpY66MeTj_O5DBvUmd1oLlUPW-23zlku-S7T7eyPdd0RTly4_YuA7Wo6GWSZNbIPEfhylDXXPn_lAEgCw6FUkzl1TV7XbUp_mMDRm6gSyVnrOpF6CZPkyVJTHp7XSfA8WlzQLl7--5ilawnAXctxiuIzYeOWwcJF1YePsQxDHSepEK4giaAqI0n8bIjJ-HzExUFSEMPulcF_7XsBIroKNoOzbpIICuAmKMz44dn_CA-ChGzvz99_yBAp6oVOP1ukMYWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba17bf936a.mp4?token=XLz18P7oRmRCOlcdolhwK2gweRZgB70yQfnlSSGjSmy03JjsjzDNtezfNE4xICa7-WQz1uTZBHxihZ_x_YTpY66MeTj_O5DBvUmd1oLlUPW-23zlku-S7T7eyPdd0RTly4_YuA7Wo6GWSZNbIPEfhylDXXPn_lAEgCw6FUkzl1TV7XbUp_mMDRm6gSyVnrOpF6CZPkyVJTHp7XSfA8WlzQLl7--5ilawnAXctxiuIzYeOWwcJF1YePsQxDHSepEK4giaAqI0n8bIjJ-HzExUFSEMPulcF_7XsBIroKNoOzbpIICuAmKMz44dn_CA-ChGzvz99_yBAp6oVOP1ukMYWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/23025" target="_blank">📅 19:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">درصد ٪
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/23024" target="_blank">📅 19:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=eAUPwn8Vzc2reETbixUBIGQUKNxQ43dxIsvEcogoEjvuVDgKcvX4eJBzT0NTuH7e0R2AHIfaV7Zp-l-wnawXYP4h6kmnpRtuhcNQWp5eHOr1TYaMgIxqCGzr86dakpfLtuOd25WCIuistgPB9FY56zAHn3S_OLXJJcYoa-sgc2VMsbmNb_AbFQbocloiCGIUGIXo4iRuWwRweVs6_bB8bl2D1hGI3Cfzl1Jq7Tkdvd1BrGf0tBew0xUWY7Szl-YoOYgfHkipCfyH8VnD5cyIPZpVDhotvjx5Mb76dMjq1LcdeSKZgcP0NRGylQaR-VN1lNV5E2oUIGASplnbBpLjfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=eAUPwn8Vzc2reETbixUBIGQUKNxQ43dxIsvEcogoEjvuVDgKcvX4eJBzT0NTuH7e0R2AHIfaV7Zp-l-wnawXYP4h6kmnpRtuhcNQWp5eHOr1TYaMgIxqCGzr86dakpfLtuOd25WCIuistgPB9FY56zAHn3S_OLXJJcYoa-sgc2VMsbmNb_AbFQbocloiCGIUGIXo4iRuWwRweVs6_bB8bl2D1hGI3Cfzl1Jq7Tkdvd1BrGf0tBew0xUWY7Szl-YoOYgfHkipCfyH8VnD5cyIPZpVDhotvjx5Mb76dMjq1LcdeSKZgcP0NRGylQaR-VN1lNV5E2oUIGASplnbBpLjfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/23023" target="_blank">📅 18:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPo</strong></div>
<div class="tg-text">ما نخواهیم پول نفت مون نره لبنان و فلسطین و نفت مون رو آمریکا بر نداره چیکار کنیم ؟</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/23022" target="_blank">📅 18:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک‌تایمز: تندروهای جمهوری اسلامی در اوایل ژوئیه مخفیانه توافق با آمریکا را با دستور حمله به سه کشتی تجاری در تنگه هرمز در ۷ ژوئیه به شکست کشاندند:
مقام‌های ایرانی به نیویورک‌تایمز گفته‌اند
مسعود پزشکیان، احمد وحیدی و بخش بزرگی از رهبری ایران از این عملیات بی‌اطلاع بودند.
تحقیقات، تصمیم حمله را به جناح تندروی مرتبط با
حسین طائب، روحانی بانفوذ و رئیس سابق اطلاعات سپاه
نسبت داده است؛ این جناح از ابتدا مخالف توافق بود و به فرماندهان میدانی اختیار داده بود بدون تأیید مرکز به کشتی‌هایی که ناقض کنترل ایران بر تنگه می‌دانستند حمله کنند. پس از حملات، پزشکیان با وحیدی تماس گرفت و با لحنی تند خواستار توضیح شد. این اقدام مذاکرات را از مسیر خارج کرد و
حملات مجدد آمریکا در روز بعد
را به دنبال داشت و در ایران نیز کشمکش قدرت، اتهام خیانت و تهدید به استعفای برخی فرماندهان ارشد را رقم زد.
عباس عراقچی
برای کاهش تنش به عمان اعزام شد، اما موفق نشد. هم‌زمان،
نبود
مجتبی خامنه‌ای
بر بحران افزود و مقام‌هایی گفتند حتی پزشکیان درباره اصالت برخی دستورها و پیام‌های منتسب به او تردید کرده است.
طبق گزارش، هم اکنون
جناح تندرو دست بالا را پیدا کرده و به‌جای بازگشت به مذاکرات، خواهان تشدید حملات علیه نیروهای آمریکایی، شناورها و زیرساخت‌های انرژی منطقه شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/23021" target="_blank">📅 18:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/23020" target="_blank">📅 18:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: با ایران به توافق رسیدیم، توافق خیلی خوبی بود، دیگه هیچ سلاح هسته‌ای در کار نخواهد بود. تقریباً همه‌چیز نهایی شده و ما به هر چیزی که می‌خواستیم رسیدیم. مهم‌ترین بخش ماجرا اینه که ایران هیچ سلاح هسته‌ای نه خودش می‌سازه و نه از جایی می‌خره.  ما امروز…</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/23019" target="_blank">📅 17:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/23018" target="_blank">📅 17:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
instagram.com/YasharMotors
🐦
x.com/yasharrapfa
▶️
youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/23017" target="_blank">📅 17:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFatemeh</strong></div>
<div class="tg-text">ی تحلیل کن اقا یاشار</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/23016" target="_blank">📅 17:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMَ reza</strong></div>
<div class="tg-text">چرا موج مکزیکی تموم نمیشه</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/23015" target="_blank">📅 17:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976afe9552.mp4?token=PJWBVsnWwbbAmdcXcS2S8Hpb_3tpOPoyREYdkDK309TjVNudu6CesmDRMjaRoSHY2GSkwRqKnVY0j9seNS40ZJrQjS6Nf1Ie6MPLxD95PckbVls2cxnznvgYo_Pj-AIS6iapY0u4h3AD6w8WWcNzxethRtroElUmYNR8XYlW4AK9InNlYYjqmJGU8XN9F0YH27sEqwaCTGYms5YXEDwXOwUCe2gaJnm0qdVMGTrSWx6qhbYuyodC8LmAIwjCpQouN5iVWLexU-pzxt-kXzN9GCJ4nmd2gfjHTEZMJsze5HpAQkUvT1PdfbjGoqNkPYTAQ4pxB2hLqQZXTOv-GGCLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976afe9552.mp4?token=PJWBVsnWwbbAmdcXcS2S8Hpb_3tpOPoyREYdkDK309TjVNudu6CesmDRMjaRoSHY2GSkwRqKnVY0j9seNS40ZJrQjS6Nf1Ie6MPLxD95PckbVls2cxnznvgYo_Pj-AIS6iapY0u4h3AD6w8WWcNzxethRtroElUmYNR8XYlW4AK9InNlYYjqmJGU8XN9F0YH27sEqwaCTGYms5YXEDwXOwUCe2gaJnm0qdVMGTrSWx6qhbYuyodC8LmAIwjCpQouN5iVWLexU-pzxt-kXzN9GCJ4nmd2gfjHTEZMJsze5HpAQkUvT1PdfbjGoqNkPYTAQ4pxB2hLqQZXTOv-GGCLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ماجرای ایران درست پس از انتخابات میان‌دوره‌ای و شاید حتی پیش از آن به پایان خواهد رسید.
قیمت بنزین به‌شدت سقوط خواهد کرد. من می‌دانستم چه کار می‌کنم؛ چاره‌ای جز انجام آن نداشتم. ایران نباید سلاح هسته‌ای داشته باشد و هرگز هم به آن دست نخواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/23013" target="_blank">📅 17:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5a025761.mp4?token=QX2VJHfDuLXSgHkdvq3PCYdEiRi3Vgzs4kLlOZAck0Vs7JiTWLqFFMrKSNqW61KYkBGwLsVDfnWjRYw_VC-yMiRywAbx9Ghthd4sCD5IaMJp4ylHsaVNtoPzDEZpq3a2xKJhaDq12PG2wydxrof3Exh9r5FXbb7xY85x34xOvSGIBF6qRyDW2ylBUEjfDMBmL6DD8ZXjxn63jXvxybXh-7PRbXz9uW5x1UQ9QvkNCKYFPzY4yGk58u-ch1-lYisKP466W3A9jugbmAhFLEMqkx4ZWGhMwdFuJRqDXWKkJpc_ZE-wKuJdxtopfpzP9tGlvwH8D9CXC2RXR623auFR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5a025761.mp4?token=QX2VJHfDuLXSgHkdvq3PCYdEiRi3Vgzs4kLlOZAck0Vs7JiTWLqFFMrKSNqW61KYkBGwLsVDfnWjRYw_VC-yMiRywAbx9Ghthd4sCD5IaMJp4ylHsaVNtoPzDEZpq3a2xKJhaDq12PG2wydxrof3Exh9r5FXbb7xY85x34xOvSGIBF6qRyDW2ylBUEjfDMBmL6DD8ZXjxn63jXvxybXh-7PRbXz9uW5x1UQ9QvkNCKYFPzY4yGk58u-ch1-lYisKP466W3A9jugbmAhFLEMqkx4ZWGhMwdFuJRqDXWKkJpc_ZE-wKuJdxtopfpzP9tGlvwH8D9CXC2RXR623auFR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران به‌شدت خواهان دستیابی به توافق است. آن‌ها مدام تماس می‌گیرند.
ما باید توافق درستی انجام دهیم. من تن به توافقی که خوب نباشد، نخواهم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/23012" target="_blank">📅 17:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2125e8e92b.mp4?token=YWZjmGx8P1FmXxql6qVz1gdokxWIfbzL_k-eMJ844NFFIj6T-giGSaFXMqOBdY6gU5fHv1z1bqmyi47KoYQ1mDm84mRp98lTHx8d8FdNTgOmL187MEzi9-sQ9sEo3XWM66IZY4mCkeJ4i311rS7uqf5ZIS4zuEIogtj8vI2savKPvmX0Kndb2hfBVoW6x0p3gVhns__HJsw-LwUqKqTMk7YZdcuHhOaWBZK7U0tKfvHD_bopaQ5SOd1wKGg82ae9WnlwYa989YKiwQ3PDZ0ouBJtr-_fVzFnQBLnp6pBYXjzUFrWVG2sDx5-aAjotAAB7rQE9RsZSwAuRk9G6FtzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2125e8e92b.mp4?token=YWZjmGx8P1FmXxql6qVz1gdokxWIfbzL_k-eMJ844NFFIj6T-giGSaFXMqOBdY6gU5fHv1z1bqmyi47KoYQ1mDm84mRp98lTHx8d8FdNTgOmL187MEzi9-sQ9sEo3XWM66IZY4mCkeJ4i311rS7uqf5ZIS4zuEIogtj8vI2savKPvmX0Kndb2hfBVoW6x0p3gVhns__HJsw-LwUqKqTMk7YZdcuHhOaWBZK7U0tKfvHD_bopaQ5SOd1wKGg82ae9WnlwYa989YKiwQ3PDZ0ouBJtr-_fVzFnQBLnp6pBYXjzUFrWVG2sDx5-aAjotAAB7rQE9RsZSwAuRk9G6FtzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ترامپ به نشست دوشنبه ایران و کشورهای خلیج فارس: برایم اهمیتی ندارد
خبرنگار: نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
ترامپ: برایم اهمیتی ندارد. این به خودشان مربوط است. ما در نهایت از آنجا خارج خواهیم شد. مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم! مثل ونزوئلا.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/23011" target="_blank">📅 17:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab990d240.mp4?token=Qxi-Nj1s66enZELoj05xpvpxmeuhfs3zqcQH6mxoEsezlDityQEXn-U0Tw4oU4C-eJn0sSYjo7KoU0eHlJQAOSw7PtT5CE4e9eiGGtIZE41sYu3JGlIuSlZVBN7GQ_xwv1MGp6hLazHzBNxiZqOM4x_JJUlpWhYVgv2isXIFjwp4GeiawpzbZGYG1zWBxIVJq-5FtgakfVWrVqxqCUdBPT_q0jCai9-EOZKRCAQEDv-Qi4_KfSpoQ2958OYa2l1awz97jOF0bOBwNuzV8J6ku3dlDfQuWNUZEs8ry1rkmbAYMTYDlT0y3ntnKWVBFVkVYFXYlBckGE6TjfT7lqr0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab990d240.mp4?token=Qxi-Nj1s66enZELoj05xpvpxmeuhfs3zqcQH6mxoEsezlDityQEXn-U0Tw4oU4C-eJn0sSYjo7KoU0eHlJQAOSw7PtT5CE4e9eiGGtIZE41sYu3JGlIuSlZVBN7GQ_xwv1MGp6hLazHzBNxiZqOM4x_JJUlpWhYVgv2isXIFjwp4GeiawpzbZGYG1zWBxIVJq-5FtgakfVWrVqxqCUdBPT_q0jCai9-EOZKRCAQEDv-Qi4_KfSpoQ2958OYa2l1awz97jOF0bOBwNuzV8J6ku3dlDfQuWNUZEs8ry1rkmbAYMTYDlT0y3ntnKWVBFVkVYFXYlBckGE6TjfT7lqr0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات رئیس‌جمهور ترامپ درباره ایران:
ما در نهایت خارج خواهیم شد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم! مثل ونزوئلا.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/23010" target="_blank">📅 17:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش ۲ انفجار مهیب از تنگه هرمز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/23009" target="_blank">📅 17:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: جنگ با ايران قبل از انتخابات میان‌دوره‌ای یا بلافاصله بعد از آن به پایان خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/23008" target="_blank">📅 16:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ: ایران می‌خواهد به هر قیمتی توافق کند، اما من توافقی را که بی‌نقص نباشد امضا نمی‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/23007" target="_blank">📅 16:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf4511f99.mp4?token=CgSGOfBw3sbvkap17PW_u4BL9dHQCgk333IJW2jgtGcwpiXUJOBlAzi0-BhV0oL25DdgmBBAzNvkxm4vIGQU9wa4VEFycVxONjN96vLxBvqDe1BCbggAJhmEEKyplriEStiZdRLWuIVeKU-0k2cZp8QeWzShn-xYLEU6pC8H1GERanTL-4A3IIzlK2a88jki1N6oXso1DLOHRDlkJOjmgS6X1bLngN0WqYE_QobVpE4m6etE70gkNqlN9b4LSoX9r8MBPIFRchRr7g0xv0UVGRfwoyDU0tnCvINDqzmK72FArc4Y_Wu2lVWwppJwehIS380CdgEKZOdSUpy7uR8RCjS6MWxK-bstOllkmtWinWwFqVfuTSnjfSaNNw-pEPTVVyNOD6zJEpwXqC7oBytA9SveZrmSOCT7OVsiG-XoxNMjajwpzPDgMNymTc7Fmc9xoHQT-V7obQeZuvNMmlr1ZCy8ndSEeTyFMZyzu2CP48v9RvK5dGHAYv1oLjHfCFba58XSCSLDh9CuKlzeFsT9pET8m1sK0HQ6FTnM6OZ0uvo6qidrcn7lBwJekkOXil8MvAaYhFCXBHPGGVCX7rdIil1Yt_kJmYePdWoaUdLqK-2ThLBXfn_l3I4fTEBhd_i3wJLE-6lboTTGSvMk22Uk0GN7FFj_vsuax88_4czXyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf4511f99.mp4?token=CgSGOfBw3sbvkap17PW_u4BL9dHQCgk333IJW2jgtGcwpiXUJOBlAzi0-BhV0oL25DdgmBBAzNvkxm4vIGQU9wa4VEFycVxONjN96vLxBvqDe1BCbggAJhmEEKyplriEStiZdRLWuIVeKU-0k2cZp8QeWzShn-xYLEU6pC8H1GERanTL-4A3IIzlK2a88jki1N6oXso1DLOHRDlkJOjmgS6X1bLngN0WqYE_QobVpE4m6etE70gkNqlN9b4LSoX9r8MBPIFRchRr7g0xv0UVGRfwoyDU0tnCvINDqzmK72FArc4Y_Wu2lVWwppJwehIS380CdgEKZOdSUpy7uR8RCjS6MWxK-bstOllkmtWinWwFqVfuTSnjfSaNNw-pEPTVVyNOD6zJEpwXqC7oBytA9SveZrmSOCT7OVsiG-XoxNMjajwpzPDgMNymTc7Fmc9xoHQT-V7obQeZuvNMmlr1ZCy8ndSEeTyFMZyzu2CP48v9RvK5dGHAYv1oLjHfCFba58XSCSLDh9CuKlzeFsT9pET8m1sK0HQ6FTnM6OZ0uvo6qidrcn7lBwJekkOXil8MvAaYhFCXBHPGGVCX7rdIil1Yt_kJmYePdWoaUdLqK-2ThLBXfn_l3I4fTEBhd_i3wJLE-6lboTTGSvMk22Uk0GN7FFj_vsuax88_4czXyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از کشتی کانتینربر ایرانی که امروز در نزدیکی جزیرۀ هنگام قشم مورد حمله قرار گرفت با یک کشته و ۳ زخمی
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23006" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز: احتمالاً عبدالرضا شهلایی، فرمانده ارشد نیروی قدس سپاه، عملیات حوثی‌ها برای تصرف شهر مخا در ساحل غربی یمن را هدایت کرده است:
منابع نظامی یمنی به رویترز گفته‌اند که بر اساس
شنود ارتباطات و اظهارات نیروهای حوثی اسیرشده
، شهلایی در هدایت عملیات تصرف مخا نقش داشته است. منابع دیپلماتیک نیز به رویترز گفته‌اند که
فرماندهان ارشد سپاه برای هدایت حملات حوثی‌ها علیه عربستان به یمن رفته‌اند
. عبدالرضا شهلایی از فرماندهان ارشد نیروی قدس است که سال‌ها در یمن فعالیت داشته و دولت آمریکا برای اطلاعات منجر به شناسایی شبکه و فعالیت‌های او
تا ۱۵ میلیون دلار جایزه
تعیین کرده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23005" target="_blank">📅 15:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ازسالی : سلام یاشار جان من همسرم راننده ست الان سمت مرز ریمدان (مرز ایران و پاکستان)رفته.میگه اعلام کردن مرز بسته ست. اسمم  نباشه
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23004" target="_blank">📅 14:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فایننشال‌تایمز: ایران از روسیه پهپادهای پیشرفته و گران‌قیمت درخواست کرده است:
به گزارش فایننشال‌تایمز، تهران امسال از مسکو خواسته است
پهپادهای پیشرفته روسی را برای استفاده در جنگ با اسرائیل و آمریکا
در اختیار ایران قرار دهد. به نقل از
مقام‌های امنیتی غربی و یک فرد نزدیک به کرملین
منتشر شده است. درخواست ایران در حالی مطرح شده که همکاری پهپادی دو کشور سال‌هاست در جریان است؛
ایران پس از آغاز جنگ اوکراین، پهپادهای شاهد از جمله شاهد-۱۳۶ را در اختیار روسیه قرار داد
و مسکو بعدها با استفاده از فناوری ایرانی، تولید این پهپادها را در داخل روسیه توسعه داد. حالا با ادامه جنگ، تهران به دنبال دریافت نسل‌های پیشرفته‌تر پهپادهای روسی است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23003" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e14331e2.mp4?token=na-gmsU3d1SO1C_oTfdzLw7vmTBIxG37sZmyRbL4Ktua5ZNU4PTlxxOhMmOwazFDbqlbaBlLSBzq03iJ-QDPIrnHVrndnLTbFRufDrOn-Gy-32Z44XrCN5xwGLE25tIO2u3WeBA691EhPgbIh9BkchccYwN3XiuTCLf4z4CIjUXEewXO3qky1BraE1jdl1906MQXi0QCErmirnvpIEf32n9sKK8TCCkeU3FbUX08dZFZSgJqbOSVaCbIFhi2nbJhJ0XXFZ9tVVXjv1xL1aCzCAg3GDPW4Qx91Ym_PLN-p3G1bJaBQnTFu-z1t3kUoIua5GTym3pTRLe1YIoTiZZs8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e14331e2.mp4?token=na-gmsU3d1SO1C_oTfdzLw7vmTBIxG37sZmyRbL4Ktua5ZNU4PTlxxOhMmOwazFDbqlbaBlLSBzq03iJ-QDPIrnHVrndnLTbFRufDrOn-Gy-32Z44XrCN5xwGLE25tIO2u3WeBA691EhPgbIh9BkchccYwN3XiuTCLf4z4CIjUXEewXO3qky1BraE1jdl1906MQXi0QCErmirnvpIEf32n9sKK8TCCkeU3FbUX08dZFZSgJqbOSVaCbIFhi2nbJhJ0XXFZ9tVVXjv1xL1aCzCAg3GDPW4Qx91Ym_PLN-p3G1bJaBQnTFu-z1t3kUoIua5GTym3pTRLe1YIoTiZZs8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام یاشار جون. ممنون از تمام تلاشی که برای آگاهیه ما می کنی. من همیشه آهنگ پرنده که تو کانال گذاشتی رو برای پسرم پلی می کنم. اونم که خیلی تو موسیقی استعداد داره، یاد گرفته و اجراش می کنه. پسرم ۳/۵ سالشه. این فیلم رو مربیه مهد کودکش ازش گرفته
😂
😂
😂
گفتم برات بفرستم که بدونی از کوچک و بزرگ، همگی دوست داریم
❤️
❤️
❤️
اگر تو کانال گذاشتی، صورتشو محو کن لطفا
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23002" target="_blank">📅 13:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جرد کوشنر، فرستاده ویژه آمریکا: اگر اوکراین تا خط موردنظر پوتین عقب‌نشینی کند، توافق صلح می‌تواند نهایی شود:
کوشنر گفت
موضوع سرزمینی همچنان سخت‌ترین مسئله مذاکرات صلح روسیه و اوکراین است
و ولادیمیر پوتین خطی را که می‌خواهد به آن برسد مشخص کرده است؛ اگر اوکراین با عقب‌نشینی تا آن خط موافقت کند، بخش عمده توافق از قبل آماده خواهد بود، اما
کی‌یف در حال حاضر حاضر به پذیرش این شرط نیست.
کوشنر افزود وضعیت میدانی نیز در تعیین سرنوشت مناطق مورد مناقشه نقش دارد و وظیفه میانجی‌ها یافتن راه‌حلی است که ضمن حفظ اهداف اوکراین، امکان پایان دادن به جنگ را فراهم کند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23001" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کمی پیش گزارش زنده فاکس نیوز از روی ناو جرج واشنگتن و پرواز جنگندهی F-15 و F-35 با دریافت کردن سیگنال تهدید از سوی ایران(پرتاب. موشک/پهپاد) به کشتیهای عبوری. همچنین در ویدیو میبینید که تماما پشت سر مجری موشکها و بمبها قرار دارد و این ناو بیش از اندازه تا دندان…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23000" target="_blank">📅 12:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxEVBLplBuc2umFY2JbbKkd-B7zyAt7Hjlzo_kpsHwFnJFYjPhn4gc1GVvnVDac3n3BYuct0fSATpwghfIKySn3Dfsr7UrLP2W9EmK-qhnnGdfgn9krmOXPmcnBcGLtyvVloqw3v-KwIewBZW0W91WqKinx0W6yVWRp41g-Ejr0_vtO5LzngyGovnQha8w5lGQLhnMTj-ZqxN3ylvfZDSoX1G6BYyEcPVU6AWmEikc1fD32sGVvJSey1EnTw62RbjstkR9t4iPGffinLXKpKt1L4D68eLjzs5WqVklPniEAWg2NRtxsQrXMcRRcI7QqfZo2DNjgskRpy3k3sAGdsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست:
سودا (مرضیه) ابراهیمی شمس‌آبادی
، بلاگر ۳۳ ساله اهل بندرعباس، به اتهام «افساد فی‌الارض»، توهین به خامنه‌ای و فعالیت‌های ضدحکومتی به اعدام محکوم شده است. نیویورک‌پست همچنین به
ترانه رحیمی
، ۲۰ ساله، اشاره کرده که به اعدام محکوم شده و خواهر دوقلویش
رومینا رحیمی
به ۲۵ سال زندان محکوم شده است. این رسانه همچنین به نقل از منابع حقوق‌بشری از اعدام دست‌کم
۲۹ معترض بازداشت‌شده از ماه مارس
خبر داده است,صدایشان باشیم
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22999" target="_blank">📅 12:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الجزیره: هم‌زمانی بحران در تنگه هرمز و باب‌المندب، خلیج فارس را در وضعیت «بین دو فک گازانبر» قرار داده است؛
با ادامه اختلال در هرمز و پیشروی حوثی‌های مورد حمایت ایران در مسیر باب‌المندب، دو مسیر حیاتی انرژی و تجارت هم‌زمان تحت فشار قرار گرفته‌اند. این وضعیت فشار قابل‌توجهی بر کشورهای خلیج فارس، به‌ویژه عربستان، وارد کرده و
واشنگتن در مدیریت درگیری با تهران، بیش از پیش با این چالش روبه‌روست که منافع و امنیت کشورهای خلیج فارس را نیز در نظر بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22998" target="_blank">📅 12:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فاکس‌نیوز: مقام ایرانی می‌گوید ایران تا پذیرش کامل شروطش از سوی آمریکا وارد مذاکره نمی‌شود.
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس ایران، در ایکس نوشت تا زمانی که آمریکا همه شروط ایران را نپذیرد، گفت‌وگو و مذاکره فایده‌ای ندارد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22997" target="_blank">📅 11:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری رژیم ایرنا: دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22996" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3mA9HdmWt6h_NhGcatEloFRbziB3cowr2XOyQKI1lUSqpnpdt167lC9RdOGBLaihxOCS3oEQoSd0BinKy4oyJmx_miQl_9nJiOxA0ZboR5lUx6I_tEyjTLmY4qCkupA7eUa-PuvIHV3FaMJpDApJrEjhQDAsfnZTzdc6fG_jn9cjPqdxh0zkGTCCPfnDVDMJ60ucvFZYGfjrigNSm3Eg2bU82Mh5O0FcxxeHT6t47C6pxNTuy7AQijdwimMeQMmu5wFr04aWReyHLNFBwD5_1JOfRFarrzRDaE4x03K9K_JQLQaJupjxBM_kH735vvfnRzJsOoRLJvmzhW6Va1cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک کشتی هنگام عبور از تنگه هرمز مورد اصابت پرتابه‌ای ناشناس قرار گرفته است. در حال حاضر، اطلاعاتی درباره وضعیت خدمه، میزان خسارات وارده و پیامدهای زیست‌محیطی این حادثه در دست نیست.
در پی حمله گزارش‌شده، آتش‌سوزی در این کشتی رخ داده است. مقامات محلی در محل حادثه حضور دارند و در حال کمک به تخلیه خدمه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22995" target="_blank">📅 11:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdd8f1fc2.mp4?token=oxtDrmvd1ESz2BRX8k9_wmeO8X5WwNMPhz104GzhPj_mjhIOUNMxeLMQ4fyxbGSkn1ZL7L2P8ahquS-vm0KtMARZhn8nU5EfqRXzSIwXrzjWVHUNI6oAzGz94LOyD4Y1jD9HldkBJyzHe484mZSBujA8aNM3k2BSiSdTTYTua0d2XZeryobTJAq4frPgvQvZkmeEmhb_wIhx67P1ScORP4kZr8eYZTgUXsw1UuCd0_xUTNdgfHaKLg6WwBmweYYpnYBX-N2WkL_lL9qGa9LiXAl8zyIFqKidWGJewbbJKXgDW2aiaYa8Cq6IFM0k7k9qr3RupAqO_SWorrAjydjKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdd8f1fc2.mp4?token=oxtDrmvd1ESz2BRX8k9_wmeO8X5WwNMPhz104GzhPj_mjhIOUNMxeLMQ4fyxbGSkn1ZL7L2P8ahquS-vm0KtMARZhn8nU5EfqRXzSIwXrzjWVHUNI6oAzGz94LOyD4Y1jD9HldkBJyzHe484mZSBujA8aNM3k2BSiSdTTYTua0d2XZeryobTJAq4frPgvQvZkmeEmhb_wIhx67P1ScORP4kZr8eYZTgUXsw1UuCd0_xUTNdgfHaKLg6WwBmweYYpnYBX-N2WkL_lL9qGa9LiXAl8zyIFqKidWGJewbbJKXgDW2aiaYa8Cq6IFM0k7k9qr3RupAqO_SWorrAjydjKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمی پیش گزارش زنده فاکس نیوز از روی ناو جرج واشنگتن و پرواز جنگندهی F-15 و F-35 با دریافت کردن سیگنال تهدید از سوی ایران(پرتاب. موشک/پهپاد) به کشتیهای عبوری. همچنین در ویدیو میبینید که تماما پشت سر مجری موشکها و بمبها قرار دارد و این ناو بیش از اندازه تا دندان مسلح به منطقه عملیات آمده.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22994" target="_blank">📅 03:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ارسالی : من امروز پهبادم رو بردم رو کلانتری شهر رستاق تمام کلانتری تخلیه کردن ، الان رفتن تو بانک کشاورزی موندن
😂
😂
😂
اسممو نذار
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22993" target="_blank">📅 02:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانال ۱۳ اسرائیل گزارش داده ارتش این کشور در پی تحولات باب‌المندب، احتمال
شلیک موشک و پهپاد از یمن به سمت اسرائیل
را جدی گرفته و در حال آماده‌سازی برای چنین سناریویی است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22992" target="_blank">📅 02:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad.Rf</strong></div>
<div class="tg-text">سلام یاشار من از اینستا چند روز پیش پیام دادم ندیدی بغل پادگان 02 ارتش رو سه روز پیش زدن من رفیقم سربازه اونجاس گفت با پهپاد پادگان بغلی رو زدن ولی کسی صداشو درنیورد حتی میگف بازرس اومد فرداش ببینه چه خبره دوباره پدافندا شروع کردن کار کردن بازرس فرار کرد</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22991" target="_blank">📅 01:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22990" target="_blank">📅 01:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromممدم✌🏽</strong></div>
<div class="tg-text">یاشار تقریباً ده دقیقه پیش موشک از تو شهر بندرکنگ بلند شد به قدری نزدیک بود کل خیابونا صداش پیچید</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22989" target="_blank">📅 01:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش صدای انفجار بندرعباس
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22988" target="_blank">📅 01:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22987" target="_blank">📅 00:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سی ان ان: پیت هگست، وزیر دفاع آمریکا، برای حضور دو خدمه جنگنده F-15 سرنگون‌شده بر فراز ایران در برنامه«60 Minutes»تحت فشار قرارشان داده است.
به گفته چند منبع آگاه، هر دو نظامی درباره حضور در این مصاحبه نگرانی داشتند و هگست به‌صورت خصوصی با آنها دیدار کرد تا مشخص شود آیا داوطلبانه در برنامه شرکت می‌کنند یا باید با دستور به این کار وادار شوند. در نهایت، یکی از آنها با نام مستعار
«براوو»
با حضور در مصاحبه موافقت کرد، اما نفر دیگر با نام مستعار
«آلفا»
از شرکت در آن خودداری کرد. پنتاگون این گزارش را
«دروغ کامل»
خوانده و گفته تصمیم حضور در مصاحبه کاملاً بر عهده خود این دو نظامی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22986" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزیر خزانه‌داری و دارایی ترکیه به شرکت‌ها و مؤسسات مالی این کشور درباره معاملاتی که ممکن است مشمول تحریم شوند هشدار داده است؛ موضعی که چند روز پس از تحریم یک بانک ترکیه و دو شرکت زیرمجموعه آن به دلیل ارتباط مالی با ایران اعلام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22985" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22984" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارسالی : سلام داداش وقت بخیر
از بندرکنگ امشب با فاصله هر 30 دقیقه دارن یه پهپاد یا موشک میزنن به طرف خلیج فارس تا الان 4یا5 تا زدن
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22983" target="_blank">📅 23:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22982">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارسالی : مرز باشماق هم بسته شد من اربیلم و همسرم رفته ایران الان لب مرز مونده نمیزارن بیان گفتن مرز فعلا بسته س و مونده تا ببینم تکلیف چه میشه
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22982" target="_blank">📅 22:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرنگار الجزیره: نیروهای اسرائیلی وارد منزل همکارمان، علی السمودی، در جنین شدند، خواستار تحویل او شدند و به پسرش حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22981" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک موشک بالستیک حوثی ها در منطقه "جازان" در جنوب غربی عربستان سعودی به یک مسجد اصابت کرد که منجر به زخمی شدن تعدادی از افراد و خسارات جدی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22980" target="_blank">📅 22:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22979" target="_blank">📅 22:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22978" target="_blank">📅 22:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حسین حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22977" target="_blank">📅 22:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وای نت عبری : حملات جدید اسرائیل به جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/22976" target="_blank">📅 22:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22975">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/22975" target="_blank">📅 21:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تصویر ۳ پاسدار کشته شده در سراوان @WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22974" target="_blank">📅 21:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری رژیم ایرنا:
دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد
منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22973" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پرتاب موشک به سمت تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22972" target="_blank">📅 20:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آسوشیتدپرس: نفتکش آسیب‌دیده در خلیج عمان باعث گسترش لکه نفتی شده است.
بر اساس گزارش جدید، آلودگی نفتی ناشی از یک نفتکش که گفته می‌شود توسط نیروهای آمریکایی هدف قرار گرفته، در حال گسترش به مناطق حفاظت‌شده زیست‌محیطی در عمان و ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22971" target="_blank">📅 20:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmsNnrT7GCfhl6IlL1--ZHTmJkvsrWHfBIoLT3qA4cW5YvukftMQQ--t7HAJ1xXz-SHGXvOrQr-wtZTcRdN8RUpSaw4NoPPRdoSh_bbVHNTtu-5R3ybcNfcmolwh4BExuYBHsrPIl4vWgNtGk_j3EH6GDD-5AthuqKzvOT2w6pnh3Pz5N0s56STjDpf2-yKvwHDvSWRsJIeQOJ-0hqmA6f3m43dXJjgYxIecOUZH-w9LYMd2Vf6yUfw24CLjxpkAqG9vZuBZCQ4c7_NbfwYWxZZQkJSJOxgcP---IeGnPI74I_RWQn-iQVesHzy9k2sga-1LgiWPlfEs6WjvAHE2cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22970" target="_blank">📅 20:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22969">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دو مقام ارشد امنیتی عراق به رویترز:
ساعاتی پیش سکو های پرتاب پهپاد در چند نقطه از مرز ایران و عراق کشف شدند،
تا اطلاع ثانوی گذرگاه های مرزی با ایران بسته خواهند بود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22969" target="_blank">📅 19:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-AWvWsgQ32aCQg1TkUiIwWgQjiwL4dzhkAeh_wmRAxnRdZYGK8Il4cXcZyuC762LXK9jtMRKZdsLchR-mkRci532LbkK5Hs5VUt0rw0rGCWuEZ890oShhqAluRhvm6ZxQWJA1KzS7WgNtAa3YEZH4A1MWE3bvDAsyMEH-wPCnAe1n-l-6dY5w-HJVndrOEe7xMFJRFjUn-1fMCNvkwet5NW-tk6Zmi_IDEPjKSLaH1NwEmqpk-Hv-0FlrO4VjYvopJyK3HsM1qZnGN1ezM5-Vt-0ox5JdatMnB1dOp_Zn6mjAG6Jm1_lOFPjeidu0Vu44kSMNo0UevNI4gaHpXdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تانکر نفتی متعلق به چین با نام لیزا که در دریای مکران حضور داشت، تلاش کرد تا از تنگه هرمز توسط کریدور ایران وارد شود، اما سپس مسیر خود را تغییر داد و به عقب بازگشت. مشخصا آمریکا اجازه نداد  @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22968" target="_blank">📅 18:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شبکه فاکس‌نیوز، هم‌زمان با پشتیبانی نیروهای آمریکایی از عملیات‌های ایالات متحده در جریان تنش با ایران، به‌صورت زنده از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که کاملا پر از موشک و مهمات شده است در دریای مکران و نزدیکی تنگه هرمز گزارش می‌دهد. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22967" target="_blank">📅 18:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2884ed587b.mp4?token=hQpl5wozQiBQKxaWxkyU9Ieb7tzlgE-HerpkcOiD9B8kUzlz3zQ0jK5uG21G5j0QwK8rCVM2o08OHSoRT28lEnx23XD5KFIQZw3M16cJ1IaeNxJsN9SYVB5sZdvrVtHjAv0JcIm7MPxJFJGXlbJ9Pvs1LQMWJPR_GzV7a_roxzIfIwRv2xluXXq4e_NiAYrfMJHl9hNMpJt3GZrhxAa1B9_VNLnIRDsJTZraRzWw68Yh-QqokGSAgu-HCdASi5qbUrJD2-zH2pn_EqGYL0aTJpnZHO4qrVvwP45kO03rXLFKx2QlR3UPV0EA9LVpwDutKseRDQCiOA-1HUDzRT-ZXJtZkQlJMI_XitboPV-qwRxnkr4awDhsjKXld6hW3jaZSjgpmCio1JNtCPu0cIQ5dH01IwcTRuYHtdo3tpMRpJqofxEu5K3PqBrPxhwRs-19F78XSMw-7hXnRQOT6pPJufvhbQffzuoQt3pvGqSsOtOV84HV1YjlNCSWcxpAhasAmKAFKxLpLvqgo_bF9pntkGL8lOReTcCKimm78E7vAWkjq4kSLvSOcXb1TVpsqda1rHvJ00KS9r4IrVLetA4pcOA0c4WlrPEhkGt6-tO4dWuTkEky565DEcsWEEorI0LLCP53Ft9gLre-547u3Pq6AMn8cj_ZU4fGmF4yA3JBYy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2884ed587b.mp4?token=hQpl5wozQiBQKxaWxkyU9Ieb7tzlgE-HerpkcOiD9B8kUzlz3zQ0jK5uG21G5j0QwK8rCVM2o08OHSoRT28lEnx23XD5KFIQZw3M16cJ1IaeNxJsN9SYVB5sZdvrVtHjAv0JcIm7MPxJFJGXlbJ9Pvs1LQMWJPR_GzV7a_roxzIfIwRv2xluXXq4e_NiAYrfMJHl9hNMpJt3GZrhxAa1B9_VNLnIRDsJTZraRzWw68Yh-QqokGSAgu-HCdASi5qbUrJD2-zH2pn_EqGYL0aTJpnZHO4qrVvwP45kO03rXLFKx2QlR3UPV0EA9LVpwDutKseRDQCiOA-1HUDzRT-ZXJtZkQlJMI_XitboPV-qwRxnkr4awDhsjKXld6hW3jaZSjgpmCio1JNtCPu0cIQ5dH01IwcTRuYHtdo3tpMRpJqofxEu5K3PqBrPxhwRs-19F78XSMw-7hXnRQOT6pPJufvhbQffzuoQt3pvGqSsOtOV84HV1YjlNCSWcxpAhasAmKAFKxLpLvqgo_bF9pntkGL8lOReTcCKimm78E7vAWkjq4kSLvSOcXb1TVpsqda1rHvJ00KS9r4IrVLetA4pcOA0c4WlrPEhkGt6-tO4dWuTkEky565DEcsWEEorI0LLCP53Ft9gLre-547u3Pq6AMn8cj_ZU4fGmF4yA3JBYy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه فاکس‌نیوز، هم‌زمان با پشتیبانی نیروهای آمریکایی از عملیات‌های ایالات متحده در جریان تنش با ایران، به‌صورت زنده از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» که کاملا پر از موشک و مهمات شده است در دریای مکران و نزدیکی تنگه هرمز گزارش می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22966" target="_blank">📅 18:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoBtta4IgBiNN2KUk4L3SyVUlPcV3zMNXC0Fl2ijlxnj8EJ-G1kbXygAbLlVFXgL7xOKtzd7_z4AuAN10YzxTAiMAhF-bjc8rVjaRtlLQ5YhGA0JTb2GCTppgO2iPBgTEbVGjloZFqRlgkyOtGEza5Uej4fYfd21uU6RtXGhk_uA9rqrsKhFYskjcoayjvlD5W8TIUCoxT4qKUJ3anzOXJMazqceK4WBfx1qCNrfqjwvOmCXySRU2i7iRJsLhBgS_atSZr3XU5-DXnFLTsmAtDIzZ7sOolTjs6NEtNLrgOU-Z6b5CMoteHB0lV-W8yUyp_GPtHZR7a1RLRsXPLffxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVyellcxEIz71Z_w8bEMzlW3Tf8UFX2EupOqnxA1uQqjpT_tF5L-jR9M8PFmCX7krPyoGMamL7MW1j0QWqfnysfRuyWuMbbJALoSJV4xvp5r9t67jxBUC5x1I4KgaOQS0iiZMlxqpjQsgU-EcLV5QzGpIO3QkUTM7-1LM96cFHdUeWu7qmFBcN7y9RTXgNyikSnIG28BcESHsRPwcIdZLLh5KB0Ve-0CGeMbWuI7789P42JSpqZ10ozZeRhjxhH_5CHvs3fNInCubYNFb4lao1Xw2ZWd5K7KV1EzfDg2kbUoMODx2-QzC94Cf_hbgSrtvhCbqvp6MmDjZDdzfSKGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQ1YCqNl6ViTb-lEfJgNL-jaaTBqEeZW6I9GQy3duYxUe20DWrUjiWiqGIHUJePfgW47tgwlHTmDW9f9DJPOtTrr_MNRgc01r0TMDdJ9IxkW03cXbSa5lXIuTNsX9rLSnreRIScjfpWdI9G9gs2bpWBBJLjvcrnAZ3SUH5m_sXRDQWm6z8P0SNP6ZBHqo7nz_SXTJvZkmCphR9tC3CkzF2z_DL2OwkdemUFKuEukIsiEH-F1WUnC-seV2L3G9TvBoC2BffFCdcIyeAj1qT4SjeKycpwle9xVc_NKeOypOAtGyGTM9l5p0OYdvwzo1C1UEtgOJzJx3dQGftugt10MtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgkLdzCYsKFbOAZLLCMe4Z5ZL3TPeBuzg9CEmPRF6FixAmNw7AljA7KcPdgut0OSfYca6itnMsBQWJssL-sApBfvBLzE3HUwqp7njMDyGYDktkNhFBf2unaCx2pzSjTjt-0tufBwHoqQbG_L7INI_mCrQF1dpepH-5rEDq2i82egiqxaerhjEPCIU6uGPu53SWpUMBREX3FfmE1faD5PNwJ0_d1i1WvBerf8ZFLgIzIbhvRgWPpc-5f6Y2bmMnNB3aslaO-wHEbOr4uglrvmHyLSuIkT-L07iceK2k6xL9vDEnawNgFPLuA_9eLiLUIK8_2kQlXGjWyoAody2WWDlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آمادگی برای حمله زمینی احتمالی به ایران
سنتکام : تفنگداران دریایی ایالات متحده بر روی عرشه پروازی ناو
«یو‌اس‌اس پورتلند» (LPD 27)
در حالی که این کشتی در دریای عرب در حال حرکت است، برای عملیات احتمالی تمرین می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22962" target="_blank">📅 18:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز به نقل از یک مقام ارشد ایرانی: نشست روز دوشنبه ایران و کشورهای خلیج فارس در عمان به درخواست و ابتکار عمان برگزار می‌شود، اما انتظار نمی‌رود در این نشست توافقی برای بازگشایی تنگه هرمز امضا شود. به گفته این مقام، ایران همچنان خواهان توافقی است که به تهران اجازه دهد از کشتی‌های عبوری از تنگه هرمز عوارض دریافت کند؛ موضوعی که عمان با آن مخالف است. این نشست قرار است علاوه بر هرمز، درباره مسائل منطقه‌ای نیز گفت‌وگو کند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22961" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزارت خارجه بحرین اعلام کرد که این کشور در نشست وزارتی پیشنهادی درباره وضعیت تنگه هرمز شرکت نخواهد کرد و تا پیش از ازسرگیری روابط دیپلماتیک با ایران، در هیچ نشست جمعی که ایران در آن حضور داشته باشد، طرف نخواهد بود. بحرین همچنین تأکید کرد هرگونه توافق یا ترتیبی درباره کشتیرانی در تنگه هرمز باید بر اساس حقوق بین‌الملل باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22960" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آسوشیتدپرس: یک شهروند ایرانی-آمریکایی از زندان اوین آزاد شد، اما همچنان اجازه خروج از ایران را ندارد.
کامران حکمتی، جواهرفروش ۶۲ ساله نیویورکی، پس از گذراندن حدود نیمی از حکم دو ساله خود آزاد شده، اما مقام‌های ایران همچنان ممنوعیت خروج او از کشور را برقرار کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22959" target="_blank">📅 17:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اتاق جنگ با یاشار:
اگر پرونده ایران در شورای امنیت به رأی‌گیری برسد، باید بین دو حالت فرق بگذاریم: اگر رأی‌گیری درباره
یک قطعنامه معمولی و الزام‌آور
باشد، روسیه یا چین می‌توانند با وتو جلوی تصویب آن را بگیرند. اما اگر رأی‌گیری از نوع
رویه‌ای
باشد، روسیه و چین حق وتو ندارند و نمی‌توانند جلوی ادامه روند را بگیرند. از طرف دیگر،
وتوی روسیه یا چین به معنی پیروزی ایران نیست
؛ اگر بیشتر کشورهای شورای امنیت علیه ایران رأی بدهند و فقط روسیه و چین مخالفت کنند، از نظر سیاسی نشان می‌دهد که اکثریت جامعه بین‌المللی با موضع ایران همراه نیستند و روسیه و چین در اقلیت قرار گرفته‌اند. حتی در برخی موارد روسیه و چین ترجیح داده‌اند
ممتنع
رأی بدهند و قطعنامه بدون وتو تصویب شود. بنابراین یکی از اهداف مهم آمریکا و کشورهای اروپایی می‌تواند این باشد که در صورت رأی‌گیری،
بیشترین تعداد کشورها را پشت موضع خود جمع کنند و روسیه و چین را در اقلیت و حامی یک رژیم تروریست نشان دهند
و آنها را
به اصطلاح در جمع خراب کنند
.؛ حتی اگر این دو کشور در نهایت یک قطعنامه ماهوی را وتو کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22958" target="_blank">📅 17:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSLn4cLuT0TT3f-ha3qhtFPp3zP9sCPAHz73LyVtgk047wZCOUpoSdWVUq3rz-qOI8mxq3uKQmKn9EvrDTeWOOGyX5g8Fhobbj94-QapN83LW5Lm1QaDugx3e6flsyR1oUL7YP4celiErfj-sOeS8FYfshQxPysntyIMM7LNbi3oid2P69LGIOBCBy9tKTPR7KCIbVny3ZZImNtSFTEFZPs8m1J1c9fMC9AfDj-Uyb0P9ofCa_ODapGG6ZnFryk_VVxdQffsKPTdQGd1uNYuoXz2AiheEnbzR7qvsDIHJl0yA_MajxCwHWRpMd4TxQDA48-gXEkL8q-fd2z1BVdzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست:
ایران پیش از حمله موشکی ۱۷ ژوئیه ۲۰۲۶ (۲۶ تیر ۱۴۰۵) به پایگاه هوایی موفق السّلتی در اردن، تصاویر ماهواره‌ای با وضوح بالا از این پایگاه در اختیار داشته است.
این تصاویر که توسط
نهادهای چینی در اختیار ایران قرار گرفته بود، هم پیش از حمله و هم پس از آن برای بررسی وضعیت و خسارات پایگاه استفاده شده است.
مقام‌های آمریکایی نام شرکت‌های چینی را اعلام نکرده و دولت چین را مستقیماً به دخالت متهم نکرده‌اند. در این حمله که منطقه محل اسکان نیروها را هدف قرار داد،
۳ نظامی آمریکایی کشته و ۴ نفر دیگر زخمی شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22957" target="_blank">📅 16:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: اگر ایران سلاح هسته‌ای داشت، ما تماس می‌گرفتیم و می‌گفتیم: "قربان، آیا می‌توانیم با هم ملاقات کنیم؟" ما با آنها بسیار متفاوت برخورد می‌کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22956" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حسین حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است
بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22955" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22954">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d1bb0546.mp4?token=WUIdJuVSgHxrx1ZcLGuMRAjA5behzHP0Uv9f79J-b1Bl4uq-LQvR65tBODruzXuqKGuVEGEM7Um4pHjayfqUbxeRjBipIVad1v96IBV43gMGJltZjwKk8UrtB_xKJoK1TvrrUpfEKnp0s1-BAMq6l5FlZQiapeS-9IcV4jxvlttQ-6XNQ3NjWbQLPr3YVNaKGgZrAZ_fomhHSkKOdvYH8yAQZ6uoms4ieqXpYmcOCC8Rci5jNtPvmwKRshpnxOWnlKaazqM86PBf7B-gPlj8bz9w_zJdk7NSU_SqE7yRSds8LCktbHHgccFa08WB8KAmhJSvxe7I9l7zMwkYO3JBmSJhBBN7HdRGnDFiyFhOAvNcdH_y4Fi3ozsERdIrKMEyKooASrNl75GvSsZ0QOQcEn7PfU4sdov0sE9fOoYYKoaoc-KA6xtpAJkGCcaNLXHXFKajN5JD-xZtXzifW9EMYYSnmQNaitGBpTv4TVjC6Ix3wE1aSRJ5FpgOk20tbkUKwJB37M5fO9u87OBfxPjCbrZ5iirCWR57hYH1mdm2s7QsIXTVUB6hQRxBTAXtQp_HwyGsd8DcQESwaEpapXZev8AmdiNGBhgkfnvOjjB7KvPxo-bCc8e4DsnUcBGr_iTiyXuNthdo6OEQsBZUtLbt-2jHw4So9eUg6G8I9iqhv-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d1bb0546.mp4?token=WUIdJuVSgHxrx1ZcLGuMRAjA5behzHP0Uv9f79J-b1Bl4uq-LQvR65tBODruzXuqKGuVEGEM7Um4pHjayfqUbxeRjBipIVad1v96IBV43gMGJltZjwKk8UrtB_xKJoK1TvrrUpfEKnp0s1-BAMq6l5FlZQiapeS-9IcV4jxvlttQ-6XNQ3NjWbQLPr3YVNaKGgZrAZ_fomhHSkKOdvYH8yAQZ6uoms4ieqXpYmcOCC8Rci5jNtPvmwKRshpnxOWnlKaazqM86PBf7B-gPlj8bz9w_zJdk7NSU_SqE7yRSds8LCktbHHgccFa08WB8KAmhJSvxe7I9l7zMwkYO3JBmSJhBBN7HdRGnDFiyFhOAvNcdH_y4Fi3ozsERdIrKMEyKooASrNl75GvSsZ0QOQcEn7PfU4sdov0sE9fOoYYKoaoc-KA6xtpAJkGCcaNLXHXFKajN5JD-xZtXzifW9EMYYSnmQNaitGBpTv4TVjC6Ix3wE1aSRJ5FpgOk20tbkUKwJB37M5fO9u87OBfxPjCbrZ5iirCWR57hYH1mdm2s7QsIXTVUB6hQRxBTAXtQp_HwyGsd8DcQESwaEpapXZev8AmdiNGBhgkfnvOjjB7KvPxo-bCc8e4DsnUcBGr_iTiyXuNthdo6OEQsBZUtLbt-2jHw4So9eUg6G8I9iqhv-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«ما
تنگه هرمز را در اختیار گرفتیم
. همه مین‌ها را پاکسازی کردیم. من گفتم: «پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟» گفتند: «قربان، این مین‌روب‌ها
زیر آب هستند
. آنها همیشه در زیر آب فعالیت می‌کنند.» گفتم: «چرا این کار را می‌کنید؟» گفتند: «به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه
خصومت و درگیری زیادی وجود دارد
.» به عبارت دیگر، اگر در یک آبراه مین وجود داشته باشد، یعنی افرادی هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
در آنجا دیگر هیچ مینی وجود ندارد، هیچ چیز دیگری هم نیست.
و اگر ببینیم آنها در حال حرکت هستند، خودتان می‌بینید چه اتفاقی می‌افتد.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22954" target="_blank">📅 15:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7fc7dd57.mp4?token=YuvoLPwDYqhiu-dgredIAsKkMdUnieleWTGUvchCuh8ynAkTbdoIRJBkv5wa7BxX2kyMXguUYIq1jEhqZmIe0zmLkDAKfFrfgrxOHceBS48qn5ZLwyl4bEE1w3xRgNEIw5nHpcju_2nsAifwUYzASnzSOxwo1bjUEYvV9b7wL0DTmhj_hwnrV9V-XiFHHvXO0aHqnfcYYCXD73F20Zo6hIiN0XFpvkPCeYPi0Li2BwQixvOFPbDXNtq3IGVouulBnM-OYqiGaV6SZHqwiZdBWGMfwnOpxSmdHc5K0X4K_H4IszWFzNmRljsFJJv51z1iV4CaDsTjXhJn7uiQs5Bzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7fc7dd57.mp4?token=YuvoLPwDYqhiu-dgredIAsKkMdUnieleWTGUvchCuh8ynAkTbdoIRJBkv5wa7BxX2kyMXguUYIq1jEhqZmIe0zmLkDAKfFrfgrxOHceBS48qn5ZLwyl4bEE1w3xRgNEIw5nHpcju_2nsAifwUYzASnzSOxwo1bjUEYvV9b7wL0DTmhj_hwnrV9V-XiFHHvXO0aHqnfcYYCXD73F20Zo6hIiN0XFpvkPCeYPi0Li2BwQixvOFPbDXNtq3IGVouulBnM-OYqiGaV6SZHqwiZdBWGMfwnOpxSmdHc5K0X4K_H4IszWFzNmRljsFJJv51z1iV4CaDsTjXhJn7uiQs5Bzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما یک درگیری نظامی کوتاه داشتیم. آن‌ها می‌گویند: «آیا ممکن است از کلمه «جنگ» استفاده نکنید؟ چون وقتی از کلمه «جنگ» استفاده می‌کنید، موضوع کمی متفاوت می‌شود.»
به نظر من، این یک درگیری نظامی است. ما آن‌ها را به شدت تحت فشار قرار داده‌ایم.
در مورد ونزوئلا، ما آنجا را تحت کنترل خود درآوردیم. ما در آن جنگ پیروز شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22953" target="_blank">📅 15:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وای نت
: کشورهای خاورمیانه، سقوط جمهوری اسلامی را به نفع منطقه می‌دانند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22952" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صداوسیما:  پس از بسته شدن دو پایانه مرزی شلمچه و چذابه به شکل یک طرفه از سوی عراق؛ از ساعاتی پیش مرز چذابه برای فقط خروج اتباع عراقی که قصد بازگشت دارند؛باز شد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22951" target="_blank">📅 14:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آسوشیتدپرس: رئیس‌جمهور لبنان به نباطیه در جنوب لبنان رفت.
جوزف عون در سفری
کم‌سابقه
به جنوب لبنان، در حالی که نگرانی‌ها از حملات مجدد اسرائیل افزایش یافته، از افزایش حضور ارتش لبنان و تلاش دولت برای حفظ ثبات منطقه سخن گفت. این سفر اکنون پس از عملیات اسرائیل در ارتفاعات علی‌الطاهر و ادامه تنش با حزب‌الله انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22950" target="_blank">📅 14:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رویترز: کشورهای بریکس بر سر بیانیه مشترک به توافق رسیدند.
منابع می‌گویند اعضای بریکس در نشست دهلی‌نو بر سر بیانیه‌ای توافق کرده‌اند که
اقدام نظامی یک‌جانبه هر کشوری را محکوم می‌کند
، اما برای جلوگیری از اختلاف، نام هیچ کشوری در آن ذکر نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22949" target="_blank">📅 14:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=aAihV4BqWFj1RVeSAekTDGp0L_2SUE6yLVHRoJd3mcJFtbUDTQs9yQnrDxb3sdjjcqRDu8L_Od6gTaqQ2qByc4ztC1VYmwwHY1-HsAYrak2arO8jh2IVc0U09qH2PIeawL5klpRFdC4AWQSB8DHypMRyhRv0dunqsGtD2gQJCFNOu5DNq1n9SkHCMD8CSds5_E7gVEUkimhrBjBWPNZenDl4XGaNTNK_LrlNoy7hdm0WWQrmbV928QwsdlRbadUjAwYCj-RyuN1PywssozDyiL_G9vCzuJCGRoeZXK_yd6gDXD7ZX2RW4jgfLTsyt60MrY7iE898y3aRvK7fUNDRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=aAihV4BqWFj1RVeSAekTDGp0L_2SUE6yLVHRoJd3mcJFtbUDTQs9yQnrDxb3sdjjcqRDu8L_Od6gTaqQ2qByc4ztC1VYmwwHY1-HsAYrak2arO8jh2IVc0U09qH2PIeawL5klpRFdC4AWQSB8DHypMRyhRv0dunqsGtD2gQJCFNOu5DNq1n9SkHCMD8CSds5_E7gVEUkimhrBjBWPNZenDl4XGaNTNK_LrlNoy7hdm0WWQrmbV928QwsdlRbadUjAwYCj-RyuN1PywssozDyiL_G9vCzuJCGRoeZXK_yd6gDXD7ZX2RW4jgfLTsyt60MrY7iE898y3aRvK7fUNDRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران (ونک) ی غذاخوری افتتاح شده که عرزشی سوز ترین رستوان شده به اسم بی بی که تخصصش  کتلت درست کردنه، حالا ی عده عرزشی فشاری شدن و بهش گیر دادن، میگن تو عمدا اسم غذاخوریتو گذاشتی بی بی و فقط کتلت درست میکنی.
@WarRoom
😂
✌🏼</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22948" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: فکر می‌کنم ایران موشک‌هایی دارد که می‌تواند شهرهای اروپایی را هدف قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22947" target="_blank">📅 14:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22946" target="_blank">📅 13:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=SXWTdj-a-l7HMKAOwPIyVRxME4CiWohJuyis9fHH6VYgJEewzL9UxgJ8aKD52j4yHpvP86_L09uNkgjqG3IvvxqxuoNJPEUVJMlzd9qynmKpRBYsEm-659ZxSQbxNLUItz5GwGprAmWeQvNFXcJv3ioJxJozOiWLInRi4wzYG1CJ-AldPH4kHUqiX3wUzypNJUzCMpXEK7Olw2Ty50ij-aXCV7KoDnD8Ua9opT5bwTa8JZJ91OgZUBlq9neX3pSDSeAVesnChzCSnTxVbQ3rQzVcwA4cUkOu6mQIOWKi11QQuDJ24db9QVZzaROdm4anJAyQxSgfCjhHpJWnMmkmAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=SXWTdj-a-l7HMKAOwPIyVRxME4CiWohJuyis9fHH6VYgJEewzL9UxgJ8aKD52j4yHpvP86_L09uNkgjqG3IvvxqxuoNJPEUVJMlzd9qynmKpRBYsEm-659ZxSQbxNLUItz5GwGprAmWeQvNFXcJv3ioJxJozOiWLInRi4wzYG1CJ-AldPH4kHUqiX3wUzypNJUzCMpXEK7Olw2Ty50ij-aXCV7KoDnD8Ua9opT5bwTa8JZJ91OgZUBlq9neX3pSDSeAVesnChzCSnTxVbQ3rQzVcwA4cUkOu6mQIOWKi11QQuDJ24db9QVZzaROdm4anJAyQxSgfCjhHpJWnMmkmAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران: ما با قدرت بسیار زیادی تنگه هرمز را کنترل می‌کنیم. هیچ‌کس انتظار نداشت چنین اتفاقی بیفتد.
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22945" target="_blank">📅 13:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=mUDdsKkFNeorQtkevsQyZWxVA-q5EyL--3nbbHfLtbztr0vam7AwOL-vX6JZnJfdzZ4atST5jr2tG6WEHgpuTVq6T0A5A7NN1224ux_X2jUzpJSJfNx46f9xcZdylcUbHcVA13iwNJ7Q8akwnif__Al7-FC-7vSvm73Wg486BaM8VD2xj5EMQAQbpLIx0CujzU370lhsybLJuAKMk6EIaFZdZBxgpTtJDHKfQ-fnRZ-7JLVZXnzbjRZN74jxQuyAcOp1QRUoq-Hc8wijgqGXHvu9vMwC_SMm8hrQ5AG4aN5KF0UnYE6-HVyh1WGsCmPxpWKwUY1vv4AtYfyTA2PlVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=mUDdsKkFNeorQtkevsQyZWxVA-q5EyL--3nbbHfLtbztr0vam7AwOL-vX6JZnJfdzZ4atST5jr2tG6WEHgpuTVq6T0A5A7NN1224ux_X2jUzpJSJfNx46f9xcZdylcUbHcVA13iwNJ7Q8akwnif__Al7-FC-7vSvm73Wg486BaM8VD2xj5EMQAQbpLIx0CujzU370lhsybLJuAKMk6EIaFZdZBxgpTtJDHKfQ-fnRZ-7JLVZXnzbjRZN74jxQuyAcOp1QRUoq-Hc8wijgqGXHvu9vMwC_SMm8hrQ5AG4aN5KF0UnYE6-HVyh1WGsCmPxpWKwUY1vv4AtYfyTA2PlVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جنگ در ایران چه زمانی پایان می‌یابد؟
ترامپ: فکر می‌کنم خیلی زود؛ احتمالاً درست پس از انتخابات میان‌دوره‌ای.
آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا انتخابات را پیچیده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22944" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=IxsTVe7Jch8O4eG5yyrf_giDHgq2ioFJUdumVvIaQars-vhkTSbg27AYXprYuGaJEo5qi7iSuaXwaGWNpjnECfWzKj9-Hyxw9OQO-FTN5Tpp_YgrscCZFHuxgnB13Oug2wJSadeAUmrxv-WGY_3aEhqkKR9yVsc73u47Jpy1VnsfDlK2QZA6PSNxd0LrhhXSohjDts7mFRcKl7F5pNP94svKPMbVKs6yrO9va5Mrd-fMJMbk3Zyy-G63CDYs67ca1ZuT28liXkhjEEatl0whAGZb8rdlrv8EBKlX1GwRWqIjloErMDNuLtSuTAORhYqImMjmfXN7z0rSGZnBlm5ZDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=IxsTVe7Jch8O4eG5yyrf_giDHgq2ioFJUdumVvIaQars-vhkTSbg27AYXprYuGaJEo5qi7iSuaXwaGWNpjnECfWzKj9-Hyxw9OQO-FTN5Tpp_YgrscCZFHuxgnB13Oug2wJSadeAUmrxv-WGY_3aEhqkKR9yVsc73u47Jpy1VnsfDlK2QZA6PSNxd0LrhhXSohjDts7mFRcKl7F5pNP94svKPMbVKs6yrO9va5Mrd-fMJMbk3Zyy-G63CDYs67ca1ZuT28liXkhjEEatl0whAGZb8rdlrv8EBKlX1GwRWqIjloErMDNuLtSuTAORhYqImMjmfXN7z0rSGZnBlm5ZDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا
ایران
مسئول حمله به خط لوله نفتی شرق-غرب عربستان است؟
ترامپ: فکر می‌کنم آنها هستند، احتمالاً آنها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22943" target="_blank">📅 13:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ در مورد حمله به خط لوله نفت سعودی: حوثی‌ها نمی‌خواهند با ما وارد جنگ شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22942" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: ما آتش را در غزه خاموش کردیم و روند صلح را در آنجا تسهیل خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22941" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دونالد ترامپ در مورد حمله به خط لوله انتقال نفت در عربستان سعودی: به احتمال زیاد، ایران مسئول این حمله است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22940" target="_blank">📅 13:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">.:
سلام یاشار جان من ساعت ۱۲ فردوسی بودم
دلار ۲۴۲ معامله میشد
اقتصاد مملکت داره منفجر میشه
خدا به مردم رحم کنه با این گرونی ها</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22939" target="_blank">📅 13:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ : اوضاع در ایران برایمان بسیار خوب است
همه چیز  به آرامی حل خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22938" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=ugbtjDk4L2Jbr6UYv8rSWImU9JzBig32UQz6UWJ-eHB8IzMA8wBdWkQ2Sq7eAeQ-h-7Ua74rpQL5c-Y52Kbq4G8TspyH-indz1qfAqI1b-nBoGlymqq1gJMALywQDkwjcimrigtTYYRECTsTSQEtWVrbu9QNTJ8YICmviTclZCLvKeDC0XTI1Bgz61l5xBSzuevcZvHO52fPylBEt5AxwB3gfzbbtc2mkNWtygAexSfXYvO_S2-6KRv8zWmtxokuYV4Jk-nSQVW04kY_z2ApsUCVSM4Jsu-gDuxEnGR18q7ayx8PP62NcLkONo9qQwIXe_hOgK901QF_q1qPkly53Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=ugbtjDk4L2Jbr6UYv8rSWImU9JzBig32UQz6UWJ-eHB8IzMA8wBdWkQ2Sq7eAeQ-h-7Ua74rpQL5c-Y52Kbq4G8TspyH-indz1qfAqI1b-nBoGlymqq1gJMALywQDkwjcimrigtTYYRECTsTSQEtWVrbu9QNTJ8YICmviTclZCLvKeDC0XTI1Bgz61l5xBSzuevcZvHO52fPylBEt5AxwB3gfzbbtc2mkNWtygAexSfXYvO_S2-6KRv8zWmtxokuYV4Jk-nSQVW04kY_z2ApsUCVSM4Jsu-gDuxEnGR18q7ayx8PP62NcLkONo9qQwIXe_hOgK901QF_q1qPkly53Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22937" target="_blank">📅 13:13 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
