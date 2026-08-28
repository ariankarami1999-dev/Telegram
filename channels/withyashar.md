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
<img src="https://cdn4.telesco.pe/file/mon6z4Tw1Kd2xTiRtlkn-koiRDrd2enpKo9z3vIgfA6tG1DO8RBmXIt31rCqrzay6LFx--5u6khrx-R3FzOSDAIIKR66IO6fxKiqYmeR9iiRCYwRrZCOD6M56IU2y7oEocTVYlLtnVR_Xv3hOrQsACHAY9wOzkMS0c3gvQYsI5xEaQwFsm1u3eUpJ5oD0XCOenal3OfC66fpxIx4AvbHRptAB6i8uPDc8SB4iY1W9lwIDEhi4BUji-FGQvm70VeWyylVQY-Qz_gNNRPbORApaGuFoTn0GE0e5x17JwwcqKslpG96Kd9aoihY--cST40_63eQb5wiKvX6NoBfUwMPyw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 440K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-21642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دبیرکل سازمان بین‌المللی دریانوردی:
حدود ۶ هزار دریانورد در ۴۰۰ کشتی همچنان در تنگه هرمز گرفتار هستند
@WarRoom</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/withyashar/21642" target="_blank">📅 16:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21641">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhTF8G3jWzCoQfun_ISV43DSMfIyNutvKjjXR7kUqbiszJ8QLJEZYqO2RrSPRMC0xiugk4dhS3ze8RXCom35v0DZeVMPDuLH2MdXJ3ATIrBUmMwonQCwNesGt1VEVuzJj1taCqofKvw2leaxZ370srqYJCNFQuIa-jCQeZLsf0WGiBx6VjaPCreuz1hUgctBH3A_2f96Z7C1jYa7rVqu27fSXoB8MpPovMQ70TN1mHNWwZscHDXlPHDEzK0h8B-WeoyVMWhwTdGKc9g6D1bAltZQVx8xDI8di9MV0Fm7UeXzAbdFtGNKY4KkPmZ4VkrTI2z9Ed1ajnY02X-ddK52Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیگه از اون آدم مهربون خبری نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/21641" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21640">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مستند و مصاحبه جنجالی کامل تلویزیون إسرائيل با یک نیروی ایرانی ویژه در موساد با نام مستعار آرش در داخل ایران ( در این مستند صحنه ها بازسازی شده اند ) که در طول جنگ۱۲ روزه نقش مهمی را در انهدام سایت های پدافندی جمهوری‌اسلامی ایفا کرده بود.
با زیر نویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/21640" target="_blank">📅 15:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21639">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxf6FU5PjGXMIhgSKxd5jdFirK6v7N4xo67zZxuhKGSl-AtUN1YHxdPtDDWblPDwm9JF-IIGWgOxAo_LLoCbPoXXAVzvuxox00AISXl4EOuKR6kOieWqqRaJWq28t1UTJC3aNVNIGrkARSgXF1mCSxz-R7Xamg2KOn6RxYQz4ea8_3Vs7xQavRSIBGo5bAhpdprnmNyVcKSHZij1mHHhupYApmqC0bVLBMJ4uBBr0KVvttU3eJfPnzoULiThbH602bs4J9dNetIvG0hZ0-flsQ5Ls64_P9tsDDiHzX9D_G_8fy4eFJmhRyCkbEYcVgG2CZv5SguDnzmAw636Yuib5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد @WarRoom</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/21639" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21638">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=gvoOJwQpn9HtsjNjgt70lvNqtzYB-xEWkebE0zhWAAA0H9uQmcN0lYdJmkmo9xzeAyQ6eov7GenK92r1ZLoWMe0AqFxtIcxmpt9AAIemvLiw_RGg8FhCDesyL9wFEkWeuMmA351uwMKyGKSNCg04wcBQV4K9f5flgW8cd7z6LxoakMMiB4PE69wN6zfxj59YyHQOYmIS5f6YU5zWPEBlh3dsU5FwGE6HnZXClnYjnQZT0j5k5KQc9BTz9KqIuF8OvrFdBMZ0IzQ-yYNEDeY-6TkvW2UvUl5bkrpif5PJgd7s0P7HgBQCu2IyDDKb7Vucqv-dS_XPgnmyJc0tuV8d4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b72f483d.mp4?token=gvoOJwQpn9HtsjNjgt70lvNqtzYB-xEWkebE0zhWAAA0H9uQmcN0lYdJmkmo9xzeAyQ6eov7GenK92r1ZLoWMe0AqFxtIcxmpt9AAIemvLiw_RGg8FhCDesyL9wFEkWeuMmA351uwMKyGKSNCg04wcBQV4K9f5flgW8cd7z6LxoakMMiB4PE69wN6zfxj59YyHQOYmIS5f6YU5zWPEBlh3dsU5FwGE6HnZXClnYjnQZT0j5k5KQc9BTz9KqIuF8OvrFdBMZ0IzQ-yYNEDeY-6TkvW2UvUl5bkrpif5PJgd7s0P7HgBQCu2IyDDKb7Vucqv-dS_XPgnmyJc0tuV8d4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگر ایران سلاح‌های هسته‌ای در اختیار داشته باشد، این پایان اسرائیل و پایان مردم یهود خواهد بود. و مهم نیست که چراغ قرمز باشد، چراغ سبز باشد یا چراغ آبی؛ من به رنگ چراغ اهمیتی نمی‌دهم. این برای من مهم نیست. ما باید این کار را انجام دهیم، زیرا در غیر این صورت نابود خواهیم شد. ما دیگر اینجا نخواهیم بود
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/21638" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21637">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175422b47.mp4?token=Torc6LTpQm0t7_PfX0-jMs_f9pRpRv_QFIRm2R4IymWZaHjzQTIug_uX20XqA1DAhq5Ea_RLanWPEaKYqjjSHy5Wqr4jIdyz1NHX9HqOyLUKiZduygG67EKS74e5iunI_XezP97pMzMp1M02WsquOEbYhEHodOqKaM0tmb1U9LpD2Ge_0h5JrW0ZsO2wdEBT8jqAVfyIAtBS7pKZtI7I5FSplL9Ks-gqsdr-fqpr7v2FHspXeVAf8q6iPkPXjaOViGTgQl04bmaDSaBP9y_qYZfkoP713IkeZjHQMWkfHvAn8aRSVNPMAkWIqp8_HpK7XTtF3bcoWgsfl3q8P2dODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175422b47.mp4?token=Torc6LTpQm0t7_PfX0-jMs_f9pRpRv_QFIRm2R4IymWZaHjzQTIug_uX20XqA1DAhq5Ea_RLanWPEaKYqjjSHy5Wqr4jIdyz1NHX9HqOyLUKiZduygG67EKS74e5iunI_XezP97pMzMp1M02WsquOEbYhEHodOqKaM0tmb1U9LpD2Ge_0h5JrW0ZsO2wdEBT8jqAVfyIAtBS7pKZtI7I5FSplL9Ks-gqsdr-fqpr7v2FHspXeVAf8q6iPkPXjaOViGTgQl04bmaDSaBP9y_qYZfkoP713IkeZjHQMWkfHvAn8aRSVNPMAkWIqp8_HpK7XTtF3bcoWgsfl3q8P2dODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری که ادعا می‌شود برای بندر کنگ و لنگه امروز صبح هست.
@WarRoom</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/21637" target="_blank">📅 15:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21636">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=KAF2_qcC14MgYyidt2l_2fqB-MNIMtSAW3hbHywSb7-k6frgjEy6VDftm2gQr8p4EZNvAi30fnQCW8oYCs-trbKM4Ze4gxAQ_rObDZrqfA2f9Xc0VKcpR3LQ_19LEbfWs7Pju4UpnVKGRSHmfUZisuq5HTGIAevQeW7Tyuh2ctdoktX0b4QcgFI27ER58FmPnPTwyD0kurGvcuTWPAqfkYt0PEOVWpfZBbPSyHJcOB0tYQgiAErRuMlBc2SZyV8l0tNmGxKQi5P-9ylMISe32fYSSfJkOl3_ZerbDu0anSFqk7QL4V-PgtNpFu5XTVJz4jQfBRKsfpDqJcwFLVR4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2bad7297.mp4?token=KAF2_qcC14MgYyidt2l_2fqB-MNIMtSAW3hbHywSb7-k6frgjEy6VDftm2gQr8p4EZNvAi30fnQCW8oYCs-trbKM4Ze4gxAQ_rObDZrqfA2f9Xc0VKcpR3LQ_19LEbfWs7Pju4UpnVKGRSHmfUZisuq5HTGIAevQeW7Tyuh2ctdoktX0b4QcgFI27ER58FmPnPTwyD0kurGvcuTWPAqfkYt0PEOVWpfZBbPSyHJcOB0tYQgiAErRuMlBc2SZyV8l0tNmGxKQi5P-9ylMISe32fYSSfJkOl3_ZerbDu0anSFqk7QL4V-PgtNpFu5XTVJz4jQfBRKsfpDqJcwFLVR4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دید بان اتاق جنگ : من با یه صدای لرزیدن شیشه اتاقم بیدار شدم دوباره خوابیدم  ، بعد نیم ساعت رفتم دم پنجره یهو چشمم به این افتاد
@WarRoom</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/21636" target="_blank">📅 14:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21635">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آکسیوس گزارش داد روزانه حدود
۲۰ تا ۳۰ نفتکش
از مسیر تحت حفاظت آمریکا در تنگه هرمز عبور می‌کنند و حدود
۹ تا ۱۰ میلیون بشکه نفت
جابه‌جا می‌شود؛ نزدیک به نیمی از صادرات پیش از جنگ. امارات، بحرین و کویت به این مسیر پیوسته‌اند و عربستان و قطر نیز ممکن است به آن ملحق شوند. آمریکا قصد دارد با
افزایش عرض کانال اصلی کشتیرانی تا اواسط سپتامبر
، امکان عبور حداقل
۵۰ کشتی در هر شب
را فراهم کند و در نهایت
۶۰ تا ۷۰ درصد صادرات نفت پیش از جنگ
را احیا کند. آکسیوس همچنین گزارش داد حدود ۲ درصد کشتی‌های عبوری ماه گذشته مورد اصابت قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/21635" target="_blank">📅 14:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21634">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=fbMf6C16gphaUy_QxLCKqzLqZhGSEEbrwM_epXMQ_ANnuEjYL9jakDjnh45mNMN0-76PeVFlBefFmQC-UzIT-FnvFWUvImqGm8lNV17H1hsSfmQb25ot-5HHSsTe3YPA_FUK5mWPUadOxO--pUJHS0YUw-ZeN2buOWoDbozroa4KbbSOTyguO3xaJxjQkAho9t273pjgpnitDD3yodRVTOvfnknXMRWGcDuV-NTQoHph9jOn2KIJP4zwGRHvIqww34vgaoa0Ukjcu4lt2nciumxVPqP9Qb-gK_EqdTY0vK5DG23Q-oMIbzkUOkVLcx0vvr7pMXQizbsbrDmpRXhk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ed644e27.mp4?token=fbMf6C16gphaUy_QxLCKqzLqZhGSEEbrwM_epXMQ_ANnuEjYL9jakDjnh45mNMN0-76PeVFlBefFmQC-UzIT-FnvFWUvImqGm8lNV17H1hsSfmQb25ot-5HHSsTe3YPA_FUK5mWPUadOxO--pUJHS0YUw-ZeN2buOWoDbozroa4KbbSOTyguO3xaJxjQkAho9t273pjgpnitDD3yodRVTOvfnknXMRWGcDuV-NTQoHph9jOn2KIJP4zwGRHvIqww34vgaoa0Ukjcu4lt2nciumxVPqP9Qb-gK_EqdTY0vK5DG23Q-oMIbzkUOkVLcx0vvr7pMXQizbsbrDmpRXhk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف پمپ بنزین پشت زندان رجایی کرج , ساعت ۲ ظهر امروز جمعه
@WarRoom</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/21634" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21633">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیویورک پست: پسر ترامپ، زندگی منزوی را سپری می‌کند، در حالی که با تهدیدات از سوی ایران و تلاش‌های برای ترور پدرش روبرو است. او به شدت تحت تأثیر ترور چارلی کرک، فعال محافظه‌کار نزدیک به او، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/21633" target="_blank">📅 14:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21632">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پروفسور جان مرشایمر، استاد علوم سیاسی دانشگاه شیکاگو : وقتی فشار اقتصادی یک کشور را تا مرز فروپاشی می‌برد، معمولاً آن کشور تسلیم نمی‌شود، بلکه برای بقا واکنش نشان می‌دهد و دست به حمله می‌زند. مرشایمر با اشاره به حمله ژاپن به پرل هاربر در سال ۱۹۴۱ گفت فشار اقتصادی شدید آمریکا علیه ژاپن و قطع دسترسی این کشور به نفت، در نهایت به واکنش نظامی ژاپن منجر شد.
او درباره ایران نیز گفت اگر تهران احساس کند بقایش در خطر است، به آمریکا و متحدانش پاسخ می دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/21632" target="_blank">📅 13:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21631">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آکسیوس گزارش داد آمریکا در نبرد بر سر تنگه هرمز به‌تدریج دست بالا را پیدا کرده است. بر اساس این گزارش، نیروهای آمریکایی با هدایت و حفاظت از کشتی‌های تجاری، عبور نفتکش‌ها از مسیر جنوبی تنگه را دوباره برقرار کرده‌اند و مقام‌های آمریکایی می‌گویند کنترل عملی این مسیر اکنون در اختیار آنهاست. اگرچه حجم تردد و صادرات نفت هنوز به سطح پیش از جنگ نرسیده، اما نفوذ ایران بر رفت‌وآمد دریایی در هرمز نسبت به ماه‌های گذشته کاهش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/21631" target="_blank">📅 13:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21630">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزارت امور خارجه رژیم :
تمام کشورها موظف هستند از اعمال تحریم‌های یک‌جانبه توسط ایالات متحده خودداری کنند، و تحریم‌های اقتصادی ایالات متحده علیه ایران غیرقانونی و فاقد هرگونه مبنا هستند.
@WarRoom
یاشار : بابا شما که قوی هستین چرا ترسیدین ، تحریم هم که برکته
🥴</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/21630" target="_blank">📅 13:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21629">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ در مصاحبه با شبکه 12 اسرائیل: این موضوع «تنگه» هنوز باز است.
واکنش ایران بسیار ملایم بوده است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم، این تمام ماجراست. بقیه چیزها مهم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/21629" target="_blank">📅 13:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21628">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ : قطر در ادامه اختلالات ناشی از بحران تنگه هرمز، وضعیت «قوه قاهره»(حفاظت حقوقی و قراردادی در شرایط اضطراری) برای تحویل گاز طبیعی مایع (LNG) به مشتریان آسیایی و اروپایی را تمدید کرده است. این تصمیم به‌دلیل ادامه محدودیت‌ها و ناامنی در تردد کشتی‌ها از تنگه هرمز اتخاذ شده و بازگشت صادرات گاز قطر به سطح عادی را به تأخیر می‌اندازد. قطر پیش از جنگ یکی از بزرگ‌ترین صادرکنندگان LNG جهان بود و اختلال در صادرات آن، فشار بیشتری بر بازار جهانی گاز، به‌ویژه در آستانه فصل زمستان، وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/21628" target="_blank">📅 12:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21627">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش‌ها از سوریه: نیروهای ارتش اسرائیل (IDF) با آتش سنگین به منطقه تپه بت‌ال‌ورده، نزدیک به شهر بیت‌جان در مناطق روستایی غربی دمشق، شلیک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/21627" target="_blank">📅 12:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21626">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نرخ دلار ۲۰۱،۵۰۰ تومان
دلار کف بازار  ۲۰۰-۲۰۵ هزار تومان
تتر ۲۰۰،۰۰۰ تومان
بیتکوین ۷۹،۷۸۰ $
انس جهانی طلا ۴،۶۰۹ $
نفت برنت  ۸۸،۰۸$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/21626" target="_blank">📅 12:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21625">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فری استایل یاس به همراه من (یاشار رپفا)
۲۰ سال پیش و زمانه همچنان بی رحم است…
@WarRoom
@RapFA
✅</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/21625" target="_blank">📅 11:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21624">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJKuyaKKm2ECl8JLXLXv4ZswEv3WYLd02eSqtU4gG3wFD_JBxDjPd4Echu6mT4KiMDrP33EgOF0lzsTAIjynwf7uxYIZizopLtgUgKK181Voxcu_uVsy_U3njTbxdEyn2a3G9pPL2WnHw4_5D6ZvSJITMRIwD7PuoGl01Df2ctoQiZZaHydPdGeeVnyFrDyWZFcVU_QVPm7zRnUQk_N8h_WQDKY4idtWDRYyTViDVvI_N_atWymVGnCSTKHXnzNq4SUEiWzSOZfOI3mnT9JJNebIQK7WgWCBCGs1xvi6bWX4J98y7ANMjspyGWxqXq9-9B1ysSwoq7QSoDJkFDwFHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از دیدبان اتاق جنگ : کاری با دست خط ندارم سطح سواد عرزشی جماعت که برای ۹۰ میلیون نسخه میپیچن (اسرائیل)
@WarRoom</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/21624" target="_blank">📅 11:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21623">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آغاز واریز سود سهام عدالت:
سبد ۴۵۲ هزار تومانی: ۴۴۳ هزار تومان(۲.۲۰$)
سبد ۵۳۲ هزار تومانی: ۵۲۱ هزار تومان(۲.۵۹$)
سبد یک میلیون تومانی: ۹۸۱ هزار تومان(۴.۸۷$)
@WarRoom</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/21623" target="_blank">📅 11:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21622">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRZJkZ2dlHJO9KLaWlgqIrohC7OaBZPHjsWBplZwMhJjKuaE52WMC0U69vcVyyCveI12horjTcbjZlbx3SdKdUTTnmJQLlOD1LrbC2l81tb-4OnPEMyhrFFb2ZSU7BgbqONIZROkYVYOm2hPG-me3YVIueiwGFxQK6P5Otf3TpFx-5xgxru8m_voZ-DaotLUdJpnXy0DWl2LxWa9g_QgQc8ZrJHQg2PXOLGyBupJeSIJ4iWizsIkDlHi7fDL8UkUa4kEocPrxNHP-3X37us4dTixHko2V92gvV_5RLO-rBV680f5s6O00DLcyJZPadDjHr_JPvmQQWRPegWgXRZlMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث دوباره:  تنگه هرمز در حال حاضر قلمرو جدید آمریکاست
@WarRoom</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/21622" target="_blank">📅 11:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21621">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2JFqjzuzLVJ08JbnHozuGZhQY6lVvnTxphPfOZ2MSXzi2F4siniqZg2sKPmwUFIx7BHsIJME5PU7hPgKRDXLD8PpxeiW8i-003w6k-3TF8SAm2mVtpt5jO7OmZyflycxmizqjsrszFdTl-eY4mzOZOLDPw9W0fjBAF1aK3IhgRM_m0eh2Eaq1Gc4IbsjEY1brm54-InsEExMPfRBZ5r_uYT2b_oI3u5xmPYEkA9f9og6O9-BRu3vePA1ngQe-EqYfDx7stX5XRjYzTi-Ue7GRUn37PQ9rXuCKdHSaDFrrtDfiEOIWsrJ0sOp8Z7L-PkfzTqE0tNlzizSZMt5qnx7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هارالد پنجم، پادشاه نروژ و مسن‌ترین پادشاهِ در حال سلطنت اروپا، در ۸۹سالگی در بیمارستان دانشگاهی اسلو درگذشت. کاخ سلطنتی اعلام کرد او صبح امروز جمعه ۲۸ اوت، ساعت ۶:۳۵ به وقت محلی، درگذشت. هارالد از ۱۹۹۱ پادشاه نروژ بود و بیش از ۳۵ سال بر این کشور سلطنت کرد. او به‌دلیل کم‌خونی همولیتیک تحت درمان بود و پس از ابتلا به یک عفونت باکتریایی در خون، وضعیتش به‌شدت وخیم شد. پسرش، ولیعهد هاکون ۵۳ ساله، اکنون پادشاه جدید نروژ شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/21621" target="_blank">📅 10:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21620">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام)، مدعی شد نیروهای آمریکایی از زمان آغاز محاصره بنادر ایران، عبور حدود
۱٬۵۰۰ کشتی تجاری
و انتقال
۷۵۰ میلیون بشکه نفت خام
از تنگه هرمز را تسهیل کرده‌اند، در حالی که به گفته او، ایران اجازه صادرات حتی یک بشکه نفت خام را نداشته است.
کوپر همچنین مدعی شد هیچ کشتی ایرانی بدون اجازه سنتکام وارد یا از بنادر ایران خارج نشده و تنها در موارد بشردوستانه اجازه تردد داده شده است. به گفته او، تاکنون حدود
۷۵ کشتی تغییر مسیر داده شده
و
۳ کشتی
از زمان آغاز محاصره بنادر ایران از کار انداخته شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/21620" target="_blank">📅 10:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21619">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«محاصره و عملیات “
طرد اقتصادی
” اقتصاد ایران در حال فروپاشی l را درهم خواهد شکست. آمریکا طی ۱۴ روز گذشته با مدیریت خود
۱۳۰ میلیون بشکه نفت
را هدایت و منتقل کرده است.
ایران: صفر.
@WarRoom</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/21619" target="_blank">📅 10:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBbsOde8YfX-6QLMnQU4IFKe--uZzEdm98zg1fQvxpZf2oAChUfnf9cKuhkUQv53mOJMq2oPohiUrcEnbksIn81oHdbKF3YyRb6ThrrSpnS3CQl-rk4Y2GufPvvJEkihUl8zfS38ke1a8S1EdRbiGt2U0BXPvqjCnd_36_SGvZXxnz1Mjremr6L3M5qGX1pau2oxvtDhll3V37q4jiB3nBYRbL01dx0y4jBrLOG_ulLpQZyHh3M2ujQY9Ls9Qot73mJLp-E1InlUX0k3YEt7WX_optfmaeq7d6okLtmz7PRgBG5k5miETgZg4Wc6REsBwOAy-ZrQiFfCpzV810KIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ با انتقاد شدید از گزارش جاناتان هانت، خبرنگار فاکس‌نیوز، آن را «بسیار نادرست» خواند و گفت: «من نمی‌خواهم با ایران دیدار کنم؛ آنها هستند که می‌خواهند و برای توافق التماس می‌کنند.» به نظر می‌رسد این یک سوءتفاهم باشد چون هانت در گزارش خود گفته بود مذاکرات مستقیم میان آمریکا و ایران فعلاً در جریان نیست و دولت ترامپ به‌جای مذاکره، در حال تشدید فشار اقتصادی و تحریم‌هاست؛ هم‌زمان کشورهای عربی، از جمله قطر، برای گرفتن امتیاز از تهران تلاش می‌کنند. ترامپ در ادامه از برت بایر، مجری فاکس‌نیوز، خواست «زیردستان بی‌کفایت خود را سر و سامان دهد». بایر نیز در واکنش گفت هانت «خبرنگاری عالی» است و تأکید کرد فاکس‌نیوز اصلاً نگفته ترامپ خواهان دیدار با ایران است، بلکه برعکس، در گزارش به صراحت گفته شده بود ترامپ نمی‌خواهد دیداری انجام شود و مذاکراتی در جریان نیس
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/21618" target="_blank">📅 10:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سازمان عملیات دریایی بریتانیا بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد. @WarRoom</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/21617" target="_blank">📅 09:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFzQ-xEm3Bu7gbjox0xA9hQYD87c5vjeUehVHl3yHyzg26sR_eyr1kuwSme-EB52WXTOz70X76P34hdxG4qIMxKJUjrUw52_asT1lHuZj1PaCbHIBzv5R8x0rAz7O5YE982893a8gJYMcmiZWj7sDsZqNYumgWFagl7GfdA7tjKw7fyhzgwhL55eLoWWwu2vTVMV30r3zZSPVUDiKCkWJk9kRYFsuVtMpLcUa1JyBW4urYOGTMzrwTNpeeOnNAZ4aygAjeUPtxdnvuesyp19rNZJTYJVxRauEwoJ6paENzMOXj-mCHEzwfIr_rbTZggI2blnJM2C66qAR4u0cfl15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران کشوری رو به فروپاشی است
@WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/21616" target="_blank">📅 09:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBynbyirFY1AoG73xLL927CsKHfp_YpEtASuLIdPfbGmChnyY4BEYolCPXkuzPTe2s4IQC9jlBGkfAuEUbXFhb9mzKxYRWHVLYDGhKg_fcwQHWB4ETqMQBi9aj7kMH8gUDIz8KryP_t_RfZoE23ooaCkkWP7wehgKJ-izxS4W4XEoucgSLwMr8lVLlDGwVMdARUOyhYm_tpWIp4MTqMw9Wu-yctYe4j84a_XApqHyw7g4fmItgI_By18m1Bmq4hG_IbHRXgoP7nhShY0OhZPX2XK_1CsoOB47Mzoj4dT-yiQ_JCprm3pnbC-wLUo3hp4Qo1f9Ltiq3V3D9sDRE_wVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ سوخترسان آمریکایی و ۲ پهپاد در خلیج فارس در حال مأموریت هستند ، بعد از مدتها این حجم مشاهده میشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21615" target="_blank">📅 00:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=OPzw2Z6mzmtGotxljioGPvA3jWhRHTUDSzWRwVdk9ZM3pVg86yED2T7qxEKKVPuTAMZGdeGYpAIHh2zLxCrOK-rgvWOqptiDb-hpi_Hjt0uYdPYs-hmsEOQa_N-ZGEyo_Byfo9NINqhoTmm_393yHdyqXlKmMPwGRMgUoC1Q_U4uSWCMk38SNny_JHrg2tRDWCbHpBxeaIPpXUlLwzDBJH9n0NH6DLyHr3E9YpF_84nmdnjVe4Rhc4MPr8ELF1t2rTHsGsai4P1ehRhBUpFo6IyvKDFoc63UXydPljHprK2qUiKZFVk5UnWdQiVfK7Db0TZAG3d8mwmNaMEIqksZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6860a3c4.mp4?token=OPzw2Z6mzmtGotxljioGPvA3jWhRHTUDSzWRwVdk9ZM3pVg86yED2T7qxEKKVPuTAMZGdeGYpAIHh2zLxCrOK-rgvWOqptiDb-hpi_Hjt0uYdPYs-hmsEOQa_N-ZGEyo_Byfo9NINqhoTmm_393yHdyqXlKmMPwGRMgUoC1Q_U4uSWCMk38SNny_JHrg2tRDWCbHpBxeaIPpXUlLwzDBJH9n0NH6DLyHr3E9YpF_84nmdnjVe4Rhc4MPr8ELF1t2rTHsGsai4P1ehRhBUpFo6IyvKDFoc63UXydPljHprK2qUiKZFVk5UnWdQiVfK7Db0TZAG3d8mwmNaMEIqksZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : هر کسی میخواد برقش قطع نشه میتونه از بورس برق با قیمت آزاد خریداری کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21614" target="_blank">📅 23:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">محسن کج بند رضایی، دبیر شورای امنیت ملی، ادعای وجود توطئه ایران برای ترور پسر دونالد ترامپ را «دروغی بزرگ» دانست و گفت این ادعا ساخته بنیامین نتانیاهو برای فریب و ترساندن رئیس‌جمهور آمریکا است. او مدعی شد نتانیاهو با انتشار گزارش‌های جعلی درباره «توطئه ترور ترامپ» او را ترسانده و بر تصمیم‌گیری‌هایش اثر گذاشته است. رضایی افزود: «اگر تصمیمی بگیریم، هیچ‌چیز مانع اجرای آن نخواهد شد؛ اما این گزارش‌ها صرفاً یاوه‌گویی‌های نتانیاهو هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21613" target="_blank">📅 23:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دیوید بارنیا، رئیس پیشین سازمان اطلاعات خارجی اسرائیل «موساد»، می‌گوید جمهوری اسلامی در نهایت در اثر ترکیبی از فشارهای اقتصادی، عملیات علیه حکومت، و اعتراضات مردم ایران سقوط خواهد کرد، و تحریم‌ها به تنهایی برای رسیدن به این هدف کافی نیستند.
@WarRoom
🚨
🚨
🚨
حتما چنل رو دنبال کرده
🤣
🙌🏾</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21612" target="_blank">📅 22:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21610">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش پرتاب موشک زد کشتی از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21610" target="_blank">📅 21:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21609">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داده است که دونالد ترامپ با بازگشت به چارچوب اولیه توافق ژوئن با ایران مخالفت کرده و ترجیح می‌دهد با تشدید فشار اقتصادی و تحریم‌ها، تهران را به دادن امتیاز وادار کند. در مقابل، ایران تأکید دارد که بازگشایی تنگه هرمز باید بر اساس همان چارچوب ژوئن انجام شود؛ چارچوبی که شامل کاهش تحریم‌ها و محدود شدن فشارهای آمریکا بود. پاکستان، عمان و قطر نیز برای میانجیگری و نزدیک کردن دو طرف تلاش کرده‌اند، اما مذاکرات تاکنون پیشرفت چندانی نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21609" target="_blank">📅 21:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به شوخی می‌گوید:
ما یک خلیج(مکزیک که شد آمریکا) داریم. ما یک دریاچه(انتاریو که شد آمریکا) داریم. حالا چیزی که نیاز داریم یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا اقیانوس آرام را تغییر دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21608" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21607">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرنگار: با کدام رهبران در مورد قطع روابط با ایران صحبت کرده‌اید؟
ترامپ: چیز زیادی برای صحبت وجود ندارد. ما نمی‌خواهیم با آنها صحبت کنیم. تنگه هرمز باز است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21607" target="_blank">📅 21:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21606">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: ایران در وضعیت بسیار دشواری قرار دارد و نمی‌تواند حقوق سربازان خود را پرداخت کند.
اقداماتی که ما در مورد ایران انجام می‌دهیم، به این معنا نیست که ما از گزینه نظامی چشم‌پوشی کرده‌ایم.
ما نمی‌خواهیم با ایران صحبت کنیم و قصد نداریم جلسه‌ای با آن برگزار کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21606" target="_blank">📅 21:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21605">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شرکت روکِتسان ترکیه موشک کروز «چاکیر» را با موفقیت از یک پرتابگر زمینی آزمایش کرد
. این آزمایش نشان داد چاکیر علاوه بر پهپاد و دیگر سکوها، قابلیت شلیک از خودروهای زمینی را نیز دارد و می‌تواند اهداف زمینی و دریایی را با جستجوگر تصویربرداری مادون‌قرمز هدف قرار دهد. برد این موشک بیش از ۱۵۰ کیلومتر اعلام شده است.
جنرال یاشار گولر، وزیر دفاع ملی ترکیه،
نیز درباره تسلیحات جدید روکِتسان گفته است: «ما این سلاح‌ها را عمدتاً برای بازدارندگی می‌خواهیم، اما اگر استفاده از آنها لازم باشد، ترکیه بدون تردید از آنها استفاده خواهد کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/21605" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: هیچ نگرانی‌ای از حمله روسیه به ناتو ندارم
دونالد ترامپ در گفت‌وگو با آکسیوس گفت که «اصلاً نگران» حمله احتمالی روسیه به کشورهای عضو ناتو نیست و تأکید کرد: «هیچ مشکلی وجود ندارد.» او همچنین گزارش‌ها درباره سفر محرمانه جان رتکلیف، رئیس سیا، به مسکو برای هشدار به روسیه درباره حمله به اعضای ناتو را رد کرد و گفت این سفر «یک کار معمول» بوده و «هیچ پیامی در کار نبوده و هیچ چیز غیرعادی‌ای» رخ نداده است. با این حال، گزارش‌هایی از جمله گزارش وال‌استریت ژورنال و CBS مدعی‌اند که رتکلیف در مسکو به روسیه درباره حمله به ناتو هشدار داده است؛ موضوعی که تاکنون از سوی مقام‌های آمریکایی یا روسی به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/21604" target="_blank">📅 20:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رئیس سابق موساد اسرائیل:
اجتناب از یک جنگ دیگر با ایران غیرممکن است
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/21603" target="_blank">📅 20:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏ انفجار در اربیل عراق , منابع عراقی از حملات پهپادی به گروه های کورد در منطقه سوران در اربیل خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/21602" target="_blank">📅 20:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob8_svB0pyG-THsAB-TV6TnBwBwC8KOmCpOU80O9ZSDsic03vI2eo7SBoje40cmazUEZCPkOkvF1Oeg1slbDEX8q8RIA6jIEm9GO-W8ufFxdckDkLcWX2c3gKIw1FDYhS0bmfnLjw9NFCE_fcpHVe6DzroP4vFk8i5TKAN7nKup15eniuaIRyr85j6wcPkyBUYmfTFMnb1Vda14_RZMi0OYqm3UGZ3zz7NdcHN4Gu_8es-z4KV2MO1Ou7erFgWmzg8t_G846KFAcWMGaskJgOWIWotVYQJyS6kX8_VBY4f3TVApY5Bo0TyTs6-RygZ_SJ0rtLPApHICpbmIgu0S1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امبر اولر، ۴۱ ساله و دختر شایسته میشیگان، امشب در مسابقه میس آمریکا ۲۰۲۶ در میامی روی صحنه می‌رود. اما تنها پنج سال پیش حدود ۱۳۶ کیلوگرم وزن داشت و پزشکش به او هشدار داده بود که در مسیر یک «مرگ زودهنگام» قرار دارد. پس از این هشدار و تجربه‌ای تحقیرآمیز در یک پارک ترامپولین، تصمیم گرفت زندگی‌اش را تغییر دهد. او طی بیش از سه سال با رژیم غذایی و ورزش حدود ۱۷۰ پوند، معادل ۷۷ کیلوگرم، وزن کم کرد و در سال ۲۰۲۴ وارد دنیای مسابقات زیبایی شد. اولر که مادر سه فرزند است، امسال به‌عنوان میس میشیگان آمریکا انتخاب شد و اکنون در میان ۵۱ شرکت‌کننده میس آمریکا ۲۰۲۶ قرار دارد؛ و در ۴۱ سالگی مسن‌ترین شرکت‌کننده این دوره است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21601" target="_blank">📅 19:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مقام آمریکایی به فاکس نیوز:
توافق ایران و عمان برای ما اهمیتی ندارد؛ فشار اقتصادی را ادامه خواهیم داد و مذاکره‌ای با ایران نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/21600" target="_blank">📅 19:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر انرژی آمریکا: به ایرانی‌ها گفتیم می‌توانند با همکاری با ما، فقط برای تولید برق انرژی هسته‌ای داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/21599" target="_blank">📅 18:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ارتش اسرائیل: دیروز، یک فرمانده از شاخه نظامی حماس را در حمله به منطقه خان یونس به هلاکت رساندیم.
همکنون نیز ارتش اسرائیل در حال حملات هوایی به جنوب لبنان می باشد
@WarRoom</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/21598" target="_blank">📅 18:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxBsTMkpjAjbS2ayD5R_9bMdRUlYwpGFS4xv5Wq1Qass4iPaOPAcrOdQ6uie2v5yha_wnJKNrLahLtEkh5EmCdQOtvT3G3i_N9FcF_lMZwDtKjhibv1Cm27aJUqeGvP0tdbiK7JltSuarcjKiAUYb1djWhoaU2W_kHwtBDBrl69Mm_qPHtQUsWLJJceVesZnr4UtYiR7Mxlxu9ZnC3S5UC3koHrFcR2oo2RsQzi8ILn_E09xeQq2GYbkyR8WHp7chfDKai3horACVfnxab0e-SvmjfeetrnL1wZWUtlnsvPVUhXyciZMdS48CKTQXok_b0CDti_FRZBwR6gdvnmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای جنگ الکترونیک E/A 18G نیروی دریایی ایالات متحده در حالی که ایالات متحده همچنان به اعمال محاصره علیه ایران ادامه می‌دهد، بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند. تا ۲۷ آگوست، نیروهای سنتکام ۷۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/21597" target="_blank">📅 18:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21fec76a7.mp4?token=c5OaOfmqYjVE4HNukE4urUA1Ca3xRCI1cbgxHrihaZrJjFG-lS6PTWRlNlnvok2F0y8cXzjsrN0o3zJfHH4IlkKr17rvh1duwmtRyOwbnGMpEL2tyUILlnXQZNuJBAPN1Va3SKrWLYy20HazajoN3ktJMvOOlehW5LEKPIOCeONf6m2EEEICW5pj5GGHr7U0ZNsYWXnyyq-51nS0bceJwmQXTkzOeyYk-DmIVfSBgjOfop9QWlLNYdkHc4ELmHQMx8knZjUzDo5UvEEzErOK7uvT4fn0FTbZwAo6q9wnvl28TJZ61BnWwDTLwYvVpSTleD0PqhOoj9sbH2gnV7RCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21fec76a7.mp4?token=c5OaOfmqYjVE4HNukE4urUA1Ca3xRCI1cbgxHrihaZrJjFG-lS6PTWRlNlnvok2F0y8cXzjsrN0o3zJfHH4IlkKr17rvh1duwmtRyOwbnGMpEL2tyUILlnXQZNuJBAPN1Va3SKrWLYy20HazajoN3ktJMvOOlehW5LEKPIOCeONf6m2EEEICW5pj5GGHr7U0ZNsYWXnyyq-51nS0bceJwmQXTkzOeyYk-DmIVfSBgjOfop9QWlLNYdkHc4ELmHQMx8knZjUzDo5UvEEzErOK7uvT4fn0FTbZwAo6q9wnvl28TJZ61BnWwDTLwYvVpSTleD0PqhOoj9sbH2gnV7RCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو در ویدئویی از پیش ضبط شده مدعی شد که هنگام پخش این ویدیو او در ایران یا در پرواز ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/21596" target="_blank">📅 17:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏یسرائیل کاتس، وزیر دفاع اسرائیل، در جریان ارزیابی امنیتی با ارتش اعلام کرد: «مهلتی که تعیین کرده بودیم به پایان رسیده است. از این پس هرگونه پرتاب بالن یا بادبادک از غزه به سوی شهرک‌های جنوب اسرائیل با پاسخ سخت روبه‌رو خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/21595" target="_blank">📅 17:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">معاون وزیر نفت ایران: حدود ۴۰ درصد از ظرفیت آسیب‌دیده میدان گازی پارس جنوبی به تولید بازگشته است
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/21594" target="_blank">📅 16:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">@WarRoom
losing my religion</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/21593" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع آگاه گزارش داد که هدف از سفر جان راتکلیف، رئیس سازمان سیا، به مسکو در روز سه‌شنبه، هشدار دادن به روسیه  بود که از حمله به ناتو و کمک به ایران خودداری کند. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21592" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30ac12425.mp4?token=p-J20Sntq6c5YPvVqabxzHpA16JVEdOaQjF5EvJ6JiMextg01bN2BoF4eN_4SPDD8HPcyDNLQ-gTYeI27OXjDsNDOhTELO1avt9d4kazTYPbpIcPCW5AQv09FmOsF_rx1g-s7QHaEYzqpUYTnsjQaU3vMfYIDNzvIK3weiydRe2m-mtRltRDjoaKwHgxsRXRxIw-uw24Zzcg7Sg19Fo2Ec_i0K01ef3qd3StFwBSAtZqf3FVnb-xSi9HlROEDphUukkNKTzCmXr9hlV8bIrStpHAsDsh71A8Ton8GaQVi_hLl7w9n78M0s9d9VAkAvTpOkbJA7or-f-pL79AzhNLXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30ac12425.mp4?token=p-J20Sntq6c5YPvVqabxzHpA16JVEdOaQjF5EvJ6JiMextg01bN2BoF4eN_4SPDD8HPcyDNLQ-gTYeI27OXjDsNDOhTELO1avt9d4kazTYPbpIcPCW5AQv09FmOsF_rx1g-s7QHaEYzqpUYTnsjQaU3vMfYIDNzvIK3weiydRe2m-mtRltRDjoaKwHgxsRXRxIw-uw24Zzcg7Sg19Fo2Ec_i0K01ef3qd3StFwBSAtZqf3FVnb-xSi9HlROEDphUukkNKTzCmXr9hlV8bIrStpHAsDsh71A8Ton8GaQVi_hLl7w9n78M0s9d9VAkAvTpOkbJA7or-f-pL79AzhNLXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21591" target="_blank">📅 15:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شیخ محمد بن عبدالرحمن آل ثانی، نخست وزیر و وزیر امور خارجه قطر، امروز در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، دیدار و گفتگو کرد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21590" target="_blank">📅 15:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21589">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آتلانتیک : کاخ سفید به‌جای تشدید عملیات نظامی، به سمت تحریم‌ها و فشار اقتصادی بیشتر علیه ایران رفته تا هم فشار بر تهران حفظ شود و هم جنگ به موضوع اصلی انتخابات میان‌دوره‌ای تبدیل نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21589" target="_blank">📅 14:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21588">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">روزنامه نیویورک‌تایمز گزارش داده است که عربستان سعودی در پی هفته‌ها حمله حوثی‌ها به اهداف سعودی، خود را برای احتمال آغاز دور تازه‌ای از جنگ در یمن آماده می‌کند. بر اساس این گزارش، حملات متقابل میان حوثی‌ها و نیروهای مورد حمایت عربستان شدت گرفته و خطر تبدیل‌شدن تنش‌ها به یک درگیری تمام‌عیار افزایش یافته است. ریاض در حال تقویت مواضع دفاعی و نیروهای یمنی متحد خود است و در صورت ادامه حملات، احتمال اقدام نظامی گسترده‌تر علیه حوثی‌ها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21588" target="_blank">📅 14:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21587">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKaG2Wwn-IOtU2af-5_DvtPTtp6krhyrHWaqzLP6TJA1LtJq1WOW02q9poDCP74xdHv2E4JgA5ST_W1zn6lgQhZVBmUjP6flT_piIzkPM7MsklFQEBlSJsh5YYocOy2FW5AbgjIfOBMaKyPxdtx8vLZzPKH0D0IR1NTXidbQ9s9X0z_GRDkfYH69QoOELFD-KdlwqKDwumj0A3gZQODKYzrWcqLsYuVoSMEBHBvuOrC6ace0ijCDyqn40NrmmONpK-Luxfvhoy_zTkxXPnd5uD16P6gDQZ5gKWeO9m1XukeRBYzzpgmdjy4ICKE0u67Bg83Ou_dSfdtPW1ak1S0UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون گزارش آتشسوزی بزرگ در پادگان سنندج
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21587" target="_blank">📅 12:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21586">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Bitcoin = 80,080$
🚀
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/21586" target="_blank">📅 12:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21585">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار: آیا می‌توان گفت که در حال حاضر حملات نظامی علیه ایران متوقف شده‌اند؟  پیت هگست: نه. اگر لازم باشد از حملات نظامی استفاده کنیم، این کار را انجام خواهیم داد. اگر ایران آن‌قدر احمق باشد که زیاده‌روی کند یا با ارتش آمریکا درگیر شود، ما هر کاری را که لازم…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21585" target="_blank">📅 12:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21584">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به گزارش MS NOW، یک ملوان ۱۹ ساله نیروی دریایی آمریکا از خدمه ناو هواپیمابر «آبراهام لینکلن» در ۳ اوت ۲۰۲۶ به دریا پرید؛ همسر ۱۹ ساله‌اش هم این اقدام را تلاشی برای خودکشی عنوان کرده است.
او پس از حدود یک ساعت در آب نجات یافت و حدود پنج روز در مرکز پزشکی نیروی دریایی سن‌دیگو تحت مراقبت بود. همسرش می‌گوید او پس از تولد دخترشان در فوریه، چند بار درخواست
مرخصی پدری
کرده بود که رد شد و پیش از حادثه نیز درباره وضعیت روحی خود با فرماندهی و کادر پزشکی ناو صحبت کرده بود. به گفته او، پس از حادثه مراقبت‌های سلامت روان محدودی دریافت کرد و پیش از نخستین جلسه درمانی، دستور بازگشت به خدمت گرفت. اکنون این ملوان با
اقدامات انضباطی نیروی دریایی
روبه‌روست و طبق اسناد اتهامی، به
تمارض (Malingering)
و
غیبت بدون اجازه
متهم شده است. نام او به دلیل حفظ حریم خصوصی منتشر نشده است. این زوج یک
پسر سه‌ساله و یک دختر نوزاد
دارند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21584" target="_blank">📅 12:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21583">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه ویس های دیروزم رو گوش کرده باشین ، خودتون صحبت های همه را میشنوید بعد تصمیم میگیرید به هر حال ،ما در راه شخص شخصه، فقط شخص خود شاهزاده ادامه میدیم و با اطراف کاری ‌نداریم و این بحث اینجا به پایان میرسد و تحقیق و تصمیم بیشتر با شما است
🙌🏾
اتحاد باید حفظ شود و رمز اصلی است همچنین انتقاد هم اگر محترمانه و درست بیان شود نیز باید شنیده و پاسخ داده شود
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/21583" target="_blank">📅 12:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21582">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ایرج مصداقی مشاور شاهزاده رضا پهلوی: علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره. حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی…</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21582" target="_blank">📅 12:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21581">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ایرج مصداقی مشاور شاهزاده رضا پهلوی:
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره.
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/21581" target="_blank">📅 11:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21580">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اتاق جنگ با یاشار : به نظر من علی کریمی باشرف است و جنگی ، ‌ابتدا باید با چهره خودش برگردد و این موضوع روشن شود ، افراد سمی دورش را عوض کند ، بعد بهترین فرد برای بخش جمع کردن کمک مالی برای مردم و کسانی که اعتصاب انجام میدهند باشد و این روند را مدیریت کند و از پتانسیل بالایش استفاده درست بشود باید در پست درست قرار بگیرد و بازی کند همچنین نیاز به همکاری بیشتر شاهزاده با ایشان هم هست و نباید ترد شود ، ولی باز میگم باید با چهره خودش برگردد اول
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/21580" target="_blank">📅 11:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21579">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">علی کریمی : ‏از اين لحظه به بعد؛ از هيچ شخص يا حزب سياسى حمايت نميكنم. در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد. این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.به اميد آزادى ايران و مردم نازنينش
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/21579" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21578">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یاسمین پهلوی : آدم‌هایی هستند که برای یک روز جنگیده‌اند، آنها خوبند. آدم‌هایی هستند که برای یک سال جنگیده‌اند، آنها بهترند. آدم‌هایی هستند که برای چندین سال جنگیده‌اند، آنها خیلی خوبند و آدم‌هایی هستند که تمام زندگیشان جنگیده‌اند، آنها اصیل‌ترین هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/21578" target="_blank">📅 11:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21577">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تحلیل الجزیره : توافق زمانی شکل می‌گیرد که ایران و آمریکا به اصل «امتیاز در برابر امتیاز» برسند؛ یعنی هر دو طرف چیزی بدهند و در مقابل، چیزی مشخص به دست آورند.
در غیر این صورت با پافشاری مانند تکرار شکست‌ها و بن‌بست‌های مذاکرات قبلی ، احتمال جنگ وجود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/21577" target="_blank">📅 11:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21576">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت : چندین پیمانکار در حال انجام عملیات بازسازی و نوسازی مخازن خارک هستند. بازسازی اسکله‌ها و مخازن و همچنین پروژه‌هایی که از قبل تعریف شده‌اند، بدون وقفه در حال انجام است و هیچ‌کدام از کارهای جاری متوقف نشده است. در حال حاضر برخی پروژه‌ها حدود ۲۰ و برخی حدود ۳۰ درصد پیشرفت دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/21576" target="_blank">📅 11:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21575">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0A2bs37imgRI_Jp4tVLbUlINPd-ReE2DFNYmWQ4Vj2DolwJgrCztvQ8defE7PF9Ou9oWMx5I2D72DEPfebLy56GXhSpjQ9W3iGhet9T23TbeAeaAQzY1iTybLXiXkWjArgfrARE5wmiBjtB_JKqzkjxZhHtHTfUk-IJOFD6_D_731ttFIkac9h7qjJIp24sipLKjfJPEgt2alcby4Kf-8BJv6I22mMzLPSpO4gPIDqJgZO7fPbtCkiCRstNvgJypYe-9Kj3PJSUhzE-_GV9nKDsoxlBT9_cNoEJfs0oS1mZEl8lVjt51e9B_dViGLXmfBF4zZz8wi6WXwxHFLpT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : همین الان قلعه حسن خان بغل ساختمان مربوط به دانشگاه که در جنگ قبلی مورد هدف قرار گرفته بود
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/21575" target="_blank">📅 11:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21574">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی کاخ سفید در واکنش به سفر وزیر خارجه قطر به ایران اعلام کرد که هیچ مذاکره‌ای با تهران در حال انجام یا برنامه‌ریزی‌شده نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/21574" target="_blank">📅 10:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21573">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a3060c7b.mp4?token=C2yARsq1ex6Ws9SJZqRceV57NboQVZkUJdK1cG2Oyyn3Gm-cr-xM2u_gg8vkGxxOZEEEllKANIWSceTpIu7v5QO_xbK6XX0aIVCsM5XWTnImq3lItEi56zv8BG8WpFIVUawnH6MFGkWKFOl7dw6u8ITMjfKaq-RSJZionlJ1CAGU7gQ7_I66g6IYLwSVZjyrfcl4xr4-hJswn796DwYzKLCEobdt9M6hwXAz0Y-isDBSdpwD4olebidjmaugFYiJbFokjrQdwXp3T6pgWxCOLeAdacSgx8q0k7fTkg0n4CwDIqJg0KSMB1_nQ2vpJB1jl-0eRqP-cHqnP8RT0x7c3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a3060c7b.mp4?token=C2yARsq1ex6Ws9SJZqRceV57NboQVZkUJdK1cG2Oyyn3Gm-cr-xM2u_gg8vkGxxOZEEEllKANIWSceTpIu7v5QO_xbK6XX0aIVCsM5XWTnImq3lItEi56zv8BG8WpFIVUawnH6MFGkWKFOl7dw6u8ITMjfKaq-RSJZionlJ1CAGU7gQ7_I66g6IYLwSVZjyrfcl4xr4-hJswn796DwYzKLCEobdt9M6hwXAz0Y-isDBSdpwD4olebidjmaugFYiJbFokjrQdwXp3T6pgWxCOLeAdacSgx8q0k7fTkg0n4CwDIqJg0KSMB1_nQ2vpJB1jl-0eRqP-cHqnP8RT0x7c3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بحران گازوئیل؛ صف‌های کیلومتری و سرگردانی رانندگان کامیون
‏گزارش‌ها از تشدید کمبود گازوئیل در جایگاه‌های سوخت و اختلال جدی در ناوگان ترابری جاده‌ای حکایت دارد؛ رانندگان کامیون در شماری از استان‌ها ناچارند برای دریافت سهمیه پایه سوخت ساعت‌ها و حتی روزها در صف‌های طولانی بمانند. کاهش سهمیه‌ها از سوی وزارت نفت رژیم جمهوری اسلامی، معیشت رانندگان و روند حمل و توزیع کالاهای اساسی را تحت فشار قرار داده و نگرانی‌ها درباره گسترش اختلال در حمل‌ونقل جاده‌ای را افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/21573" target="_blank">📅 10:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21572">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مؤسسه نیروی دریایی آمریکا USNI : گزارش داده است که ناو هواپیمابر تئودور روزولت CVN71 و ناوگروه رزمی آن در هفته‌های آینده از سن‌دیگو حرکت کرده و برای استقراری بیش از هفت‌ماهه در خاورمیانه آماده می‌شوند. فرمانده ناو نیز خدمه را برای مأموریتی حدود هشت‌ماهه آماده کرده است. این ناوگروه قرار است به حوزه فرماندهی مرکزی آمریکا اعزام شده و جایگزین ناو «جورج واشنگتن» شود؛ اقدامی که در ادامه حضور طولانی‌مدت ناوهای هواپیمابر آمریکا در منطقه و هم‌زمان با ادامه درگیری با ایران انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21572" target="_blank">📅 09:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf_0vpdXW-eHNJUZztN22w2n-5exrWAwc4TDuTRQNk8OOy_mZ05lbsdc4kTPsPDseJZ8igFrXkk-mCsD9xX8A4DR7bBvsh_gWZwK5EpTw1Dop-kswCHbC3oCrPqt4sM6iZLzEpkLr52Eq5RBN9SYg-HZwJ5czz24Cmq7pMG_CdxmXyOAWvpyBYfM1XUAdsczgrprnT6wWhZeHLkInAXHxPOu-RijVnRfoSxy0Kw909tFpWc7ADpfN8_71sbfpkF9Mieg7RzXCTFiG46UMl4OEdiYRVD6PWfhAe0YQmcdtBqcmTc9dY5UKym6QjkNzErR2RjAC9ljJJKZeLfB0_sJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات دریایی بریتانیا بامداد پنجشنبه گفت که یک نفتکش در آب‌های نزدیک منطقه «الخصاب» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفته که باعث آتش‌سوزی در آن شد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21571" target="_blank">📅 09:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع آگاه گزارش داد که هدف از سفر جان راتکلیف، رئیس سازمان سیا، به مسکو در روز سه‌شنبه، هشدار دادن به روسیه  بود که از حمله به ناتو و کمک به ایران خودداری کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21570" target="_blank">📅 03:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21569">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVoMpQWD2XIV73URKw9ZQXAayU3Q5KZYOY8XeGgwk7CJgJ0nrHK17aXpBTOHWZ3mJE88P4Det-Uj6YSpVRXnnisW20iNHxatW98DpwaHpt1MPXW9noxc6Ycc1JhjkhBWn7nlWSvWxSWkAueOJC6ejVfzl4g5-CoVfcC9xtSxG-6KKWX8BMCNcxJOlC4oE2Df925udnFndzFeCOOlUsWg4w0Y_NcXYUqedVloxX03oeYIMEpI6f-mqU7rzkSFbcJuTSLt6jvI-413L9Z1SjTh_VK-C6FlP53-0OXrJmtHbNPKosQ5leSXjtviZ3nVg1FYsFfHDf8AZOJY2rxaWyc5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیونه خونست! صفحه اول روزنامه نوبنیاد امروز
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21569" target="_blank">📅 03:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21568">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">در منطق دیکتاتور مردم دو دسته‌اند: آنهایی که باید گول بخورند و آنهایی که باید گلوله بخورند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21568" target="_blank">📅 01:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21567">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بلومبرگ: وزارت دادگستری آمریکا در حال احیای «دادگاه غنائم جنگی» است تا بتواند نفتکش‌های ایران را به‌عنوان غنیمت ارتش مصادره کند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21567" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21566">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تنگه دعواااا شد
🚨
🚨
🚨
🚨
پرتاب چند موشک از سیریک و صدای انفجار از تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21566" target="_blank">📅 00:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21564">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21922cc89d.mp4?token=n3RDsZJhcjc8Np2vl93K2dYGkQskcBnLlsARCCV0xW4Dw94ifRvJjwy4MKNIx9SYPNNLj0Wf1u3PW6NXCZ0iOzcNb-N6GUsoa-cp3hngFDojKFlZBotY1dxsGNpidDavF6h1zQfVlzbzNvpA_QUt3KhtOVtY2XSd6kZQVU0nggCEIcb_Tns87sfe06hSRsO4emYA06rnL5NjcmiC6Q-s6K9C_TUa8Wnx54nCS4HIt8bdrwoQ_KjJJiR-pkot3bwLB1LHsl_ARHeNvlPNx4Qi-N4XnYSnuokRtQYOdJp3Nvl1SA7YyVPVaVVYkoIR_ZzS8cHG_l_QJnMLf36rXP1I03boYTGzzJMd1eZT8OmBXLq7242l99yWVhgsL1XcSJ6yl9Mg68oe7GU4YVzKy2nbGZumEmhvrc00-iyn1JfJ33P25p6eTLQnDjZySkc2z6MNHmkv1fGYW9Retw8aTIilSCCDRJFMyYHIwe_lPlWJSl5wGX-t7LVa8X2fifDzeAtp5nijzG8WwTn_Z28od9jVLg0tVmaEGp4YCsmcEL3XpnTr9qogBtZV0DRgz82DQdRmimmB2xOsAhUo3wGhEtfElSHDIqVe9wdx1TLxXtrNEB44jcbVdZony7vEsbf7JhYsWr4lnFeeVnaIOujzltyjVIqrmAD775bioSVe-yRPB00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21922cc89d.mp4?token=n3RDsZJhcjc8Np2vl93K2dYGkQskcBnLlsARCCV0xW4Dw94ifRvJjwy4MKNIx9SYPNNLj0Wf1u3PW6NXCZ0iOzcNb-N6GUsoa-cp3hngFDojKFlZBotY1dxsGNpidDavF6h1zQfVlzbzNvpA_QUt3KhtOVtY2XSd6kZQVU0nggCEIcb_Tns87sfe06hSRsO4emYA06rnL5NjcmiC6Q-s6K9C_TUa8Wnx54nCS4HIt8bdrwoQ_KjJJiR-pkot3bwLB1LHsl_ARHeNvlPNx4Qi-N4XnYSnuokRtQYOdJp3Nvl1SA7YyVPVaVVYkoIR_ZzS8cHG_l_QJnMLf36rXP1I03boYTGzzJMd1eZT8OmBXLq7242l99yWVhgsL1XcSJ6yl9Mg68oe7GU4YVzKy2nbGZumEmhvrc00-iyn1JfJ33P25p6eTLQnDjZySkc2z6MNHmkv1fGYW9Retw8aTIilSCCDRJFMyYHIwe_lPlWJSl5wGX-t7LVa8X2fifDzeAtp5nijzG8WwTn_Z28od9jVLg0tVmaEGp4YCsmcEL3XpnTr9qogBtZV0DRgz82DQdRmimmB2xOsAhUo3wGhEtfElSHDIqVe9wdx1TLxXtrNEB44jcbVdZony7vEsbf7JhYsWr4lnFeeVnaIOujzltyjVIqrmAD775bioSVe-yRPB00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏وزیر انرژی ایالات متحده، رایت: در صورت شکست بازرسی‌ها و مذاکرات آژانس بین‌المللی انرژی اتمی، زیرساخت‌های هسته‌ای و صنعتی در ایران به صورت نظامی نابود خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21564" target="_blank">📅 00:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21563">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23dd6e08b2.mp4?token=d5p16PXZgYBOWMJsiN5yyk4DRJVS1HZa_6rfx84-zWrRKlMYN4CkBP3u8ohDJN2084y-73xmLf_YCva8tjwor1xvme-KByNwv2np3SVwW535RtFNlrkm0GtLFyYIpvSO-0rjJa5wH9SH1nT5NnoEuBDbJJZ7pk-hnom4vsy_1x685wtBwMgTiTJ2M0iMDeyJaZrSBquU0qY0xcHFzOM1kOlZv3GqWe4Tv5XOfMznhUwXAdg8KfY3ieT-ySfY6IAeCThGgTahN0qZe3YCvdEYrStnlSKKds8vXLSWnHX5sO8Du6mjg8u-YdCxAAnEMddcYrM8DCTD2TsnceqUbpOfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23dd6e08b2.mp4?token=d5p16PXZgYBOWMJsiN5yyk4DRJVS1HZa_6rfx84-zWrRKlMYN4CkBP3u8ohDJN2084y-73xmLf_YCva8tjwor1xvme-KByNwv2np3SVwW535RtFNlrkm0GtLFyYIpvSO-0rjJa5wH9SH1nT5NnoEuBDbJJZ7pk-hnom4vsy_1x685wtBwMgTiTJ2M0iMDeyJaZrSBquU0qY0xcHFzOM1kOlZv3GqWe4Tv5XOfMznhUwXAdg8KfY3ieT-ySfY6IAeCThGgTahN0qZe3YCvdEYrStnlSKKds8vXLSWnHX5sO8Du6mjg8u-YdCxAAnEMddcYrM8DCTD2TsnceqUbpOfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : سگ‌های نظامی در کنار نیروهای آمریکایی در سراسر خاورمیانه خدمت می‌کنند و ماموریت‌های حیاتی متنوعی را انجام می‌دهند. این جنگجویان چهارپا، هم‌تیمی‌های قابل اعتمادی در کمک به محافظت از نیروهای نظامی آمریکایی در برابر تهدیدات هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21563" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21562" target="_blank">📅 23:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">@WarRoom
Ai</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21561" target="_blank">📅 23:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi ...</strong></div>
<div class="tg-text">درود یاشار جان بنظرت الان رو چه حرفه ای تمرکز کنم و یادش بگیرم که در ایران آینده بتونم کمک بزرگی رو انجام بدم</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21560" target="_blank">📅 23:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21559">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">@WarRoom
Final Battle</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21559" target="_blank">📅 23:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21558">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaha</strong></div>
<div class="tg-text">جنگ قبل انتخابات هست یا بعد ؟
بنظرت خودت؟ و با تحلیل و دیتا هایی که الان هست
❤️
🔥</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21558" target="_blank">📅 23:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21557">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21557" target="_blank">📅 22:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21556">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
نخست‌وزیر و وزیر خارجه فردا برای بررسی تنش‌زدایی و فراهم کردن زمینه‌های گفت‌وگو به تهران می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21556" target="_blank">📅 22:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21555">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیدبان اتاق جنگ با تاخیر : درود من چند وقت بود میخواستم یه چیزی رو بگم ولی شک داشتم بگم یا نه  من ……….. این قسمت پیام  حاوی مشخصات دقیق فرستنده پیام بود و سانسور شد ……  برج مراقبت مهراباد یه تعدادی ادم بودن خیلی مذهبی و عرزشی بودن جوری که انگشت نما بودن  اینا…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21555" target="_blank">📅 21:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21554">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دیدبان اتاق جنگ با تاخیر : درود من چند وقت بود میخواستم یه چیزی رو بگم ولی شک داشتم بگم یا نه
من ……….. این قسمت پیام  حاوی مشخصات دقیق فرستنده پیام بود و سانسور شد ……
برج مراقبت مهراباد یه تعدادی ادم بودن خیلی مذهبی و عرزشی بودن جوری که انگشت نما بودن
اینا چون رادار نداشتن تو جنگ میومدن با بقیه ی برجای غرب کشور با عرزشیاشون هماهنگ میکردن که جنگنده اومد خبر بدن
میگفت ما ۹ اسفند یه ربع زودتر خبر دادیم که جنگنده و موشک دیدیم اگه میخواستن رهبرو پیاده و با پای خودش ببرن بیرون از بیت یا ببرن پناهگاه تو یه ربع میتونستن ولی اینکارو نکردن و گذاشتن بمیره حتی مدرک و اثباتم داشت که زنگ زده بود پدافتد و حفاظت بیت  میگفت حتی از زمان جنگ ۱۲ روزه رابطمونم خیلی خوب بوده با بیت چون خبر میدادیم بهمون اطمینان داشتن
و خب این یعنی ممکنه باقر قالیباف رهبرو با لابی و کودتا قربانی کرده باشه؟
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21554" target="_blank">📅 21:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21553">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال 13: رئیس ستاد ارتش در دو روز گذشته توصیه کرده است که تعداد عملیات ترور هدفمند در غزه افزایش یابد، به عنوان پاسخی به "پرتاب هواپیماهای کاغذی"
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21553" target="_blank">📅 20:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21552">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرگزاری تروریستی فارس : یک نفتکش هند هنگام عبور از تنگه هرمز توقیف شد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21552" target="_blank">📅 20:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21551">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTu6I6zs40pbo0nvzQbBVbsaNRSliwApPPIGwvsTtH3BJWJaOhjT1ckeeRnvEp9KaKy28va8lvC30XZiOoBn3wEc3kuQTqS2DwUcVF-DV7o__RNHjiJ8-8R6WU7q1BPZpVL84ZtolanAL9UkBMqG_mSELaURswthp9rRAu4-IaiH_5WY8ZE5C7dzh9PheO2MdU05nG_EEe3qMO8IoXBwIZUqVVVLIJQFUbZzevu2KsRE99cxTmVzc5BmgiMhPbuD0F2ygVphOUIoubWjvMyklxOLGFpCBzAHKVCFKBNBIfBIXz7i9a2pvCiwdT2J7JLL1H4iI2VhOAf18Y3ZdHM0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در سال ۱۹۶۴، در دوران تحصیل در آکادمی نظامی نیویورک، در کنار پدرش «فرد ترامپ» و مادرش «مری آن ترامپ». ترامپ در سال آخر تحصیل به درجه «کاپیتان دانش‌آموزی» و شمشیر افتخاری دریافت کرد و همچنین فرماندهی گروهان A را بر عهده داشت. این تصویر مربوط به دوران فارغ‌التحصیلی او از آکادمی نظامی نیویورک است؛ یونیفرم او لباس تشریفاتی یک دانش‌آموز نظامی است، نه یونیفرم ارتش آمریکا.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21551" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRk5HrcMvoug32FQCfF9_fAsRdDp8ZvpSjwyLny2mxMyLhfB6O-OOkTYM1BUTstsoZwHn9yQc15A6DaURCccxFoY76ZOU5CYb1Tbi_yALitMIFBX3rbng2PPPSC9WDLFGMOoVTOaVMMDtMTXr5W4h-6cHnds2BisdDyGz1JcDw105SYpA5zoBcHM9f-Mp6DuSIWOUi8d3bB5msv385ybreOdzRdBr0mEzrLd85xnV4Q3wUk-sYjbMdiwm7Ynt4bRlrUWL2kK7OgUrHiv-IS2GeWpc9PKac8QUQ1k7u9jMstbGQnAcA-EbKIJOUS4jCLy6Z8XCXE31ui3agQKU6SDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث مدعی است امسال کار رو جمع میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21550" target="_blank">📅 20:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21549">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWV1sq43SEaJSV7m2zD9N_pUU0goOgN_2YBgCXuCRLcsGcZQLMi_fXZ3FNCRxGB1kz15BasHoQRfoRj4JBm9we25ZWSXPeoqaOJa3We5vaCe5zOSk12xah9cGVpUL-pygbzICjV-X9auDf9rXHv06RyhhvlXe7T_uds7kTx_4NbUrRh2m6SCWqVS2NKD1c8BRy1XxB1ESDLK08x7cvHu4A4g0HeWQiZFyMn5x3tYRRlBH-_SlBOGGQD3oO9dGabA3MiO7FR6HGGSf5gNCbZRU0qrhpRbESV4xwF9ROztV-GHQJWSiUjL7Jmv7mIHPXRdE_uVq1ewxmVk9J1PfIo7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث پست عکسی از خودش و پدر مادرش را بازنشر داد که در کپشن آن نوشته شده : والدینی که دنیا را نجات دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21549" target="_blank">📅 19:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21548">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کانال ۱۴ به نقل از آتلانتیک
:
منابع داخلی ایران به این نشریه گفته‌اند که
مجتبی خامنه‌ای، جانشین تعیین‌شده پدرش، یا از نظر بالینی مرده است یا در وضعیت نباتی به سر می‌برد
؛ موضوعی که پرسش‌های جدی درباره اینکه در حال حاضر چه کسی عملاً ایران را اداره می‌کند، ایجاد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21548" target="_blank">📅 19:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21547">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ در گفت‌وگو با الجزیره
گفت او گفت برای ازسرگیری مذاکرات با ایران «عجله‌ای ندارد» و برای انجام مذاکرات نیز «هیچ جدول زمانی مشخصی» تعیین نکرده است
همچنین گفت «ایران با مردم خودش بسیار بدرفتاری می‌کند. آنها تعداد بسیار زیادی از معترضان را می‌کشند.»
من شنیده‌ام تورم آنها ۹۰ درصد است، ولی من فکر می‌کنم تورم آنها در حقیقت ۳۰۰ درصد است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21547" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21546">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2699b93394.mp4?token=R331-Z2Xd8KLEZUlVjH9wR37lkixYt-2L-0LKjNYDtzWzg_hcyUH5mjrUhhk3sXouk6nXIKv-P07E8WL0_Z3UFd1BOzy_wJmdu9jz5K5MPBgxWRhwjMFX_H_o9DEJw6b9sQoloNGA75dc8i-v1W_JliUKE2tcLFNBESKAJmvjM6aNM5kammdbH6A4uiAiDAJSiozwf_ykCCho2bCdGAkImtHyVP3Q7Vcuj7wXKf5oJ-f8myzW7YXl1ewantUv-MKItD3gI8EOnfQptpkogj6nMil5zMqqkNJUUp9TrVourR09fDcIuFK4MGq-vDWgPleE2ljAeYZXGHHb-xqQaOopg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2699b93394.mp4?token=R331-Z2Xd8KLEZUlVjH9wR37lkixYt-2L-0LKjNYDtzWzg_hcyUH5mjrUhhk3sXouk6nXIKv-P07E8WL0_Z3UFd1BOzy_wJmdu9jz5K5MPBgxWRhwjMFX_H_o9DEJw6b9sQoloNGA75dc8i-v1W_JliUKE2tcLFNBESKAJmvjM6aNM5kammdbH6A4uiAiDAJSiozwf_ykCCho2bCdGAkImtHyVP3Q7Vcuj7wXKf5oJ-f8myzW7YXl1ewantUv-MKItD3gI8EOnfQptpkogj6nMil5zMqqkNJUUp9TrVourR09fDcIuFK4MGq-vDWgPleE2ljAeYZXGHHb-xqQaOopg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: وقتی افرادی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.
اما اکنون این احتمال وجود دارد(اعتراضات)زیرا آنها (رژیم)بسیار ضعیف شده‌اند... بسیاری از سربازان آنها حقوق دریافت نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21546" target="_blank">📅 17:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21545">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbraham</strong></div>
<div class="tg-text">یاشار جان درود و ارادت
نمیدونم این پیام رو میبینی یا گم میشه لابه‌لای پیام های دوستان
فقط میخواستم بگم دمت گرم که توی این شرایط سخت و پیچیده که این بیشرفها برای ماها درست کردن تو پیشمون بودی و همیشه توی شرایط بحرانی بیشترین انرژی رو برامون میفرستی خدایش دیروز نشسته بودم توی پارک محلمون و به همه چی فکر میکردم ولی هیچ وقت به خ کشی اصلا فکر نکردم چون ماها حقمون این نیست که بخوایم بخاطر یه مشت چاغال بیشرف که بویی از انسانیت نبردن زندگی خودمون تموم کنیم
به هرحال همه ماها یه روزی می‌میریم ولی حداقل با شرافت بمیریم ن بخاطر این پیشرفا
پاینده باد ایران و ایرانی
❤️</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21545" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21544">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehzad</strong></div>
<div class="tg-text">سلام یاشار جان عرض ادب
من تو کرونا پدر و مادرم رو تو یه تایم ۱۷ روزه از دست دادم و الان تنها ترینم
حرفات کاملا درسته ولی نمیدونم اگر شما ، مثل من ۳ ماه فقط سیب زمینی و نون لواش میخوردی بازم میتونستی اینجوری حرف بزنی یا نه.
برادر اوضاع خراب تر از چیزیه که میشنوی
منم دارم بین خود….. و ادامه دادن میجنگم</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/21544" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21543">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به گزارش خبرگزاری کم اعتبار مهر، ایران و روسیه قراردادی ۲۵ میلیارد دلاری برای ساخت نیروگاه‌های هسته‌ای جدید امضا کرده‌اند. انتظار می‌رود مسعود پزشکیان، رئیس جمهور ایران، و ولادیمیر پوتین، رئیس جمهور روسیه، هفته آینده در قرقیزستان دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/21543" target="_blank">📅 17:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21542">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/492b9e7ef3.mp4?token=vg14oYsdtMibEIdieIAalJqMiAKv-JuohxM4RzZpK0gKFESEPog4E8biOoqs4gbCZFpkTzFj1_VH5nMMT6FhoUAW15WVyirSZj2dokm1ElvKQAqKRNPVoQ17PqilT2CvC4BehAzJRdTfB41eB9AdUhOF6TriXBTljexEWuTc3E4yeRezfDxQmHchhTQljsP2eyXXvEuF8nkfcFFJKCY3HhH3ItM_j7llORqkSidUQ7dAaVaGedquV759qnMWm5pt9fXvCNtb38VjwMKXOHKrUu7xkKNyGI9prSCxtt3cm415vaj5fUxCgXNoMLZD1GFksqMWG1iMOrFojEWhiCTwwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/492b9e7ef3.mp4?token=vg14oYsdtMibEIdieIAalJqMiAKv-JuohxM4RzZpK0gKFESEPog4E8biOoqs4gbCZFpkTzFj1_VH5nMMT6FhoUAW15WVyirSZj2dokm1ElvKQAqKRNPVoQ17PqilT2CvC4BehAzJRdTfB41eB9AdUhOF6TriXBTljexEWuTc3E4yeRezfDxQmHchhTQljsP2eyXXvEuF8nkfcFFJKCY3HhH3ItM_j7llORqkSidUQ7dAaVaGedquV759qnMWm5pt9fXvCNtb38VjwMKXOHKrUu7xkKNyGI9prSCxtt3cm415vaj5fUxCgXNoMLZD1GFksqMWG1iMOrFojEWhiCTwwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
«ما مین‌ها را پاکسازی کردیم. اما تنگه [هرمز] باز است؛ تنگه در حال فعالیت است و کشتی‌ها از آن عبور می‌کنند.
بله، هر از گاهی ممکن است یک پهپاد یا یک موشک یا چیزی شبیه آن شلیک شود، اما تنگه کاملاً در حال فعالیت است.
حجم زیادی نفت در حال عبور است.
دیروز ۱۰ میلیون بشکه [نفت عبور کرد].»
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/21542" target="_blank">📅 17:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21541">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ درباره ایران:
این گروه حاکمان ، آن‌طور که باید، گروه چندان شرافتمندی نیستند؛ این را به شما می‌گویم.
ما خیلی زود در ایران به یک پیروزی بزرگ دست پیدا خواهیم کرد.
ما واقعاً، حقیقتاً، از همان ابتدا ایران را کاملاً تحت سلطه خودمان داشته‌ایم.
من قطعاً با اجرای قوانین شریعت مخالفت خواهم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/21541" target="_blank">📅 17:05 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
