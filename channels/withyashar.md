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
<img src="https://cdn4.telesco.pe/file/SX3EEjUqyRk0XgPufYLRM0eIJ7yH0Jn2SVJiQkGetc7ixWVP1_DdnyoMoxP4Ctk9apbB1F-fbCqefpHDA80371W-9NKi_zLXXQuiaPgBQhBMQtbjA8z_30Bao8ifhoM1Dc7JwjvBlV-20BL_VZbjeY54JvvrEECnqApiql1eKYtGBiLZfvN8UBZr6OT1GqjHqLuN6RsZB56XESAAMx5UPKnJHY_QD0n4mispqbDvJ7yup2Z_ZIze5l2VrgEVgNDrXvNoxXIA7XBOYh73Zc1p-AoxQvNxFQDUbpFY7x7NKmPLGgee9A0OCmFlhzsEhwol4VmJEKUP1qREjzMSN4wFGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 435K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اتاق جنگ با یاشار : طبق روال تمامی جمعه‌ها از هشت ماه پیش تا کنون، امشب بیداریم و نوشیدنیهای الکلی و غیرالکلی را نوش جان خواهیم کرد.
امروز بیشتر خاص است چون ورود ششمین ماه میلادی شروع جنگ هم است
@WarRoom
💥</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/20154" target="_blank">📅 17:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر خزانۀ آمریکا به فاکس نیوز: محاصره‌ی نظامی و اقتصادی ایران متوقف نخواهد شد و ما در سراسر جهان به دنبال اموال ایران خواهیم رفت.
@WarRoom</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/20153" target="_blank">📅 17:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌  اتفاقی راجع به ایران قرار است بیوفتد @WarRoom</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/20152" target="_blank">📅 17:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌
اتفاقی راجع به ایران قرار است بیوفتد
@WarRoom</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/20151" target="_blank">📅 17:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ در مورد اتفاقات اسپانیا:
واقعاً افتضاحه، ببینید وقتی آدم نادرستی به قدرت برسه چجوری یه کشور رو نابود میکنه. این تصاویر رو بخاطر بسپارید، اگر دموکرات‌ها دوباره به قدرت برسن همین بلا سر آمریکا هم میاد.
@WarRoom</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/20150" target="_blank">📅 16:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ امروز در بحبوحه تشدید تنش‌ها و ادامه جنگ با ایران، جلسه کابینه خود را در کمپ دیوید برگزار میکند. به گزارش رویترز، در این جلسه علاوه بر مسائل سیاست خارجی و جنگ با ایران، پیامدهای اقتصادی درگیری‌ها، به‌ویژه افزایش قیمت بنزین و نگرانی‌های سیاسی جمهوری‌خواهان…</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/20149" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حماس در بیانیه‌ای اعلام کرد با مرحله دوم چارچوب آتش‌بس موافق است، اما تأکید کرد که فقط سلاح‌های سنگین (مانند راکت‌ها و موشک‌های ضدتانک) را تحویل خواهد داد؛ آن هم مشروط به خروج کامل اسرائیل از غزه، تشکیل کشور مستقل فلسطین، بازسازی غزه و پایان همه اشکال تجاوز.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/20148" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDsMhJ3IezPubE3mVigpn-hgYS4mem9oODdRIxEAS187b3tqCOCmlpkopCqq3ZvIQS0fJnd4Q64ecO6NSkLWVAy7CGCBKgGMkJLdCNgpoVizT4wuoM98HhYogswre2UG-6ALnNekjXbi6uTEcdNGDLR88tjyfO2BI-t3R9jG7rRLn9s3x7lul9t6KFZvoMplpqPieVjhKEm7VunlDBNCH6g3-GiYpm8b3oQZBaPNb0wFk52VFjjr_-NzsnVK0yGzRz4NUGlME8SodQAGXavfSoaaCGUi7BY0FwmaRc28zM6SydlqToh1xPWCjwJOqjOtReb0wZ_8n4w-l85tq_-rMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر سند محرمانه افشا شده از تعداد واقعی ثبت نام کنندگان در پویش جانفدا  که 8,311,811 نفر بوده و حدود 2 میلیون نفرشون نظامی و حدود 6 میلیون نفرشون بالای ۵۰ سال و ۸۸۵هزار نفر زیر ۱۲ سال دارند !
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20147" target="_blank">📅 15:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ امروز در بحبوحه تشدید تنش‌ها و ادامه جنگ با ایران، جلسه کابینه خود را در کمپ دیوید برگزار میکند.
به گزارش رویترز، در این جلسه علاوه بر مسائل سیاست خارجی و جنگ با ایران، پیامدهای اقتصادی درگیری‌ها، به‌ویژه افزایش قیمت بنزین و نگرانی‌های سیاسی جمهوری‌خواهان پیش از انتخابات میان‌دوره‌ای آمریکا، مورد توجه قرار گرفته است. این سیزدهمین جلسه کابینه ترامپ در دوره دوم ریاست‌جمهوری اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20146" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزیر دفاع اسرائیل ، یسرائیل کاتس برای بار هزارم : اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20145" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کويت: از بامداد امروز هدف حملات پهپادی ایران قرار گرفته‌ایم , خسارات فقط مادی بوده
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20144" target="_blank">📅 14:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIfNfKgllEcVb5K8V-1UmrqdEU3S8sFelD55nMF0YYXQs9TngoTsIbvo3de-TemA_kdfcT87YTXlWM3i9F8j-NNfisL7jQ2jCSJzUy9mipitIlMKLiitahz7jtbSCFBD6xBLO-OES62pgPHgNt55rf6mmAIRHWjIOrGpJy8PppMaEChMkwNJNY4dYN9t8bpGVCPi0XSkFJAjXJVhDWQAbnGmeYptGhrVcrpG7Uu4hO2h-U9pYtMn89q6Fdr5yO1pGTbVo_8oFeEYmtyO2LSgggsHaxp5-nKemfa4PQI1kTRj5Yn5OoVttL3a8FlfDl-q3jGpPgWklwW2iK_2f7TKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون تنگه‌هرمز یکی از کشتی های هدف قرار گرفته توسط سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20143" target="_blank">📅 14:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd52784122.mp4?token=nlqOmACVsxq3-ZDI9GYS3aMMUP4-YPqx6PSGOYcGe5o8BWEmVGnHx2EDBojepPYiBj7XavgnFruGG3uF50vXWpb03dtjZ6Ps6gUj3CQeRzEMmUSJJi-lacbw1Pqi_MMkcGRdJO5z-ONN78hAOPdKhkfVmkvm_x6VhkRr8-aFqKkXLTzyPaEwg5741wUannT4UajkMXfnLEF1iqw-TwmqJCFoebVVY9bwx-tIZEySOzN-H5sLt4k54eEYNVh7Oni9diWU1EpJsOaeMAB0V4xFgLUvbjPrtNswT6cVALangkf0Sy7Ng0iIuTy10ObHA4paU5f2sLMmv_hLSSUzeoZpqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd52784122.mp4?token=nlqOmACVsxq3-ZDI9GYS3aMMUP4-YPqx6PSGOYcGe5o8BWEmVGnHx2EDBojepPYiBj7XavgnFruGG3uF50vXWpb03dtjZ6Ps6gUj3CQeRzEMmUSJJi-lacbw1Pqi_MMkcGRdJO5z-ONN78hAOPdKhkfVmkvm_x6VhkRr8-aFqKkXLTzyPaEwg5741wUannT4UajkMXfnLEF1iqw-TwmqJCFoebVVY9bwx-tIZEySOzN-H5sLt4k54eEYNVh7Oni9diWU1EpJsOaeMAB0V4xFgLUvbjPrtNswT6cVALangkf0Sy7Ng0iIuTy10ObHA4paU5f2sLMmv_hLSSUzeoZpqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی آتش‌نشانی تهران: دود مشاهده شده در آسمان شرق تهران، مربوط به حریق ضایعات و فضای سبز در محدوده جاجرود است
حریق در دره است و آتش‌نشانان در حال اطفای آن هستند.
@WarRoom
یاشار : چیزی نیست بی بی داره آشغالارو آنیش میزنه تو دره دید نداشته باشه</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20142" target="_blank">📅 13:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085ee0b373.mp4?token=SSJ-AZ-JtkwAUudEHRwVr9yriI0A1VbueKI7WU0LrdVk5LCQEnaux84wbTOjnazdLH3q2mODTLBrEM3fRo5606jBGOOaaFFT_KZvLzaR6JImhAb7wYeL0ZWygIQVFnVXYXvoEsBUFl0irvOXJ-50qUfRujh3tK1kYVdPYNmgNYWCF7ZIIXqlCBLDMUMlWlhOvYRxgI3K-urMCn4t5mIthjBxX8BF3LLPEjFCeBMCmoqMkdqQVJUa94M2pRuia0jF8ren7vKRxj4fH-9IjZv_ugZSCWpM4pdgMOylVxiUOFPTg35j9YYozOrvumQhlpDRrfV9BKExJR1J2da0LlbqiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085ee0b373.mp4?token=SSJ-AZ-JtkwAUudEHRwVr9yriI0A1VbueKI7WU0LrdVk5LCQEnaux84wbTOjnazdLH3q2mODTLBrEM3fRo5606jBGOOaaFFT_KZvLzaR6JImhAb7wYeL0ZWygIQVFnVXYXvoEsBUFl0irvOXJ-50qUfRujh3tK1kYVdPYNmgNYWCF7ZIIXqlCBLDMUMlWlhOvYRxgI3K-urMCn4t5mIthjBxX8BF3LLPEjFCeBMCmoqMkdqQVJUa94M2pRuia0jF8ren7vKRxj4fH-9IjZv_ugZSCWpM4pdgMOylVxiUOFPTg35j9YYozOrvumQhlpDRrfV9BKExJR1J2da0LlbqiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران ستون دود بزرگ سیاه و غلیظ در پشت سد لتیان
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20141" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20140">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">به گزارش تلگراف،
آمریکا و اسرائیل در حال بررسی گزینه‌ای جدید برای افزایش فشار بر ایران هستند که شامل «محاصره زمینی»
پس از ماه‌ها حملات و محاصره دریایی در تضعیف تهران است؛ این طرح بر اعمال فشار به همسایگان ایران از جمله عراق، پاکستان، ترکیه و افغانستان برای بستن یا محدودسازی گذرگاه‌های مرزی و قطع جریان واردات و صادرات تمرکز دارد، به‌طوری‌که به گفته یک مقام اسرائیلی هدف آن است که ایران عملاً از تبادل کالا محروم شود، با این حال ژنرال بازنشسته آمریکایی شان مک‌فارلند این سناریو را «تقریباً غیرممکن» توصیف کرده هرچند معتقد است در صورت اجرا می‌تواند فشار اقتصادی شدیدی وارد کند، ضمن اینکه احتمال دارد طرح مذکور بیشتر جنبه انحرافی داشته باشد تا توجه ایران را از اقدامات واقعی بعدی منحرف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20140" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20139">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1VxMN45SsEPaa_ttIO1xzxsBgDVVvIVtWDNlqXBrMhKnCVVC3wGY5Pm__mA5CrIDXGS392BSSyINfFG2Qgn3hFJCcBHl8s8Rdo6HHXo_I4sjHp5W8L9wkc3_BzUQGlX3aUWHaT1w47Muu0EyfeHvtc7Cbhp4ffdeoPjzOXQMshzffeJkLaEsQeidG-toTGz651iUZvWKpo9eX6FlACAQsTbLN5ZbtxlAGCnJhTbXxs6D7ldY34VDAKTMTdj6M2MuuQzE1XS51JLo13zTpfz2wnQpzWlMqEwz8qUgInlhZjfX5JMdtZTWZE-R8M_oThQM6KOkyLtjYkWZYbGH95B_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر سوخت‌رسان KC-135R نیروی هوایی آمریکا با شماره 8017-63 پس از ماه‌ها سکوت، دوباره فعال شد. این هواپیما در پی برخورد مرگبار مارس ۲۰۲۶ بر فراز مرز عراق با تانکر 0347-60 با شناسه «ZEUS70» آسیب دیده بود.8017-63 که با کال‌ساین «RCH169» وارد منطقه شده و پس از فرود اضطراری در تل‌آویو (LLBG) زمین‌گیر شده بود، اکنون با شناسه جدید «RCH564» سیگنال داده و در فرودگاه بن‌گوریون فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20139" target="_blank">📅 13:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20138">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeetJjc3wTMXNaBH9kuTyWZo6d_1PXntZQX3OUoUc1sJdCFydiB68yCDawCdV-9dcfxBa6vWrBs77cD7Pijg7y5f0OHA4q8G3b3AYHwFPpyAfZjUcbCrL4qBap-gDfEVIC812QejKx_ky41y8W5pteycfMgAG5eKMTawbxAxI9KCTzeuf5UaXmaOU4MKLobeN9z7k9Qho0_TFkhMePPGPQgMTvjM5cDfVzAjIl4eovptui94NLGvi_2lqAAm36MCH0w7H0BfDRW_BWKYxztSm6IdstQp3X3sAf-U9JDF9T826qkGoZfZGvAQsJ8A_NGd8FxukTPo8EaYDUyp9O5c9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اعلیحضرت شاهنشاه محمدرضا پهلوی و انور سادات، رئیس جمهور وقت مصر، هنگام تماشای یک  مانور نظامی در تاریخ 28 تیر 1355 در منطقه علی آباد قم.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20138" target="_blank">📅 13:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20137">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش صدای انفجار در تنگه هرمز @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20137" target="_blank">📅 12:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20136">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حماس بیانیه گروه بین‌المللی صلح غزه رو تأیید و اعلام کرد اسلحه‌ش رو تحویل می‌ده.
این یک شکست بزرگ دیگه برای رژیم در آستانه‌ی دور بعدی حملات تمام‌عیار آمریکا و اسرائیل علیه ج.ا در خاک ایران محسوب می‌شه.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20136" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20135">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/054d20c537.mp4?token=VoZi1cPpRJPXfDQTmQKI57iBdEEMDNbptYSvcyzunsUTa6FsncPZNTr7xrxLE8COL2ZEs3JjLHdnCt3FZol-8FyJhpzTVV0tjnuprfaI7hluL3ka4UmHTYWEhhpJLYXcOQ0hZrE4DIkBWq80Z6rXrbnAS6i5xsnsKaqcB0uyBkNwTznjWuyUmIZye0-GtMIT4kXJqjwdc9z6Ct8xZyFUmBjKQfupAwISxNiCsehP4XlXKkGoUa8UL37ihgZvGajLAC4zhavsKpsKetVbz7ufxa5VCtqPwDUbRjzUjk3SPCN_e0wd-6A8WhyjadkTaif0OXPb8j0ZO-G2KgsK8JE_zjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/054d20c537.mp4?token=VoZi1cPpRJPXfDQTmQKI57iBdEEMDNbptYSvcyzunsUTa6FsncPZNTr7xrxLE8COL2ZEs3JjLHdnCt3FZol-8FyJhpzTVV0tjnuprfaI7hluL3ka4UmHTYWEhhpJLYXcOQ0hZrE4DIkBWq80Z6rXrbnAS6i5xsnsKaqcB0uyBkNwTznjWuyUmIZye0-GtMIT4kXJqjwdc9z6Ct8xZyFUmBjKQfupAwISxNiCsehP4XlXKkGoUa8UL37ihgZvGajLAC4zhavsKpsKetVbz7ufxa5VCtqPwDUbRjzUjk3SPCN_e0wd-6A8WhyjadkTaif0OXPb8j0ZO-G2KgsK8JE_zjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال بدل خامنه‌ای از زائران مراسم تشییع جنازه خامنه‌ای (فکر کنم بیکار شده اومده آبدارچی شده)
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20135" target="_blank">📅 12:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20134">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRvwBkESc0lu6U5f6igAhOx6NMuTS2YUvPuvXrwfaQ62Wm-8iBU28pI4pVea6hGB_jwUtzMNWBYNOtZ14dxTihNQ25V1vhZapstDdL1n0fVITYtXYZ4DWYWa6uShrkBVWWpsQCeLRlyTfda-jHOAjdACBU34YAnOtafZzkCOKj3fkvo5sZWNoIBM0TYfAWRw_ap2qSWplmg3ywZ-95RzcPLxpRLmGQhrbPja0VD6zQMcdhrHCp-drRiNWlwZVPyqzKMuGeRVVIVveGp7sawj1zUuN5cMr6wJTXoqZrtCnPPmRPZmFVaRnfDQN_Jg6BqrR9D7u_QHzAX0e9C8WdlFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه ۱۵ میلیون دلاری جدید وزارت خارجه آمریکا برای اطلاعات درباره شبکه مالی سپاه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20134" target="_blank">📅 12:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش صدای انفجار در تنگه هرمز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20132" target="_blank">📅 12:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رسانه‌های دولتی ایران به‌نقل از یک مقام ارشد گزارش داده‌اند که «با اطمینان صددرصد» حملهٔ قریب‌الوقوع آمریکا به منطقهٔ کوه پیک‌اکس در راه است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20131" target="_blank">📅 12:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">باراک راوید، آکسیوس: به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم تشییع جنازه علی خامنه‌ای، رهبر سابق ایران، به این کشور سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکند و وقت‌کشی کند
یک مقام ارشد آمریکایی ادعا کرد که ایران سعی کرده حماس را متقاعد کند که توافق‌نامه را امضا نکند، اما این گروه ترجیح داده به حرف آنها گوش ندهد
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20130" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce43f3e25d.mp4?token=hm5UR3COdCl44BBYoVGZxpvXZusb5PtEC6DIIpQkFnaxhfhQgdWtyi165pZ4fYJYt_it3WyNEnHUPuWscLtvZTYUfeEPD3hn4EYcyaiN8jK0vJ5DkhLHyWhlvz3UT6xkMHnyu2wrbiZHAGCo7Bxd8zSQJQhUqT9fJGn0KIZUTzMwU-Kw2Gvhk7sbw7F6CaeckFtKLLIF5z879U9DtRDfiihdODOXSEGmxBDcvb4QiAm8zpxt4E2tSHTTSW9GGL1_3w1cLa-8s-2odzv_K7ClYLvPTnWKVshIXCMaItWyXKqG23XBus9HUjMjJRlMiHsd8UCBx4ZQrDaDZ-BPKzj2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce43f3e25d.mp4?token=hm5UR3COdCl44BBYoVGZxpvXZusb5PtEC6DIIpQkFnaxhfhQgdWtyi165pZ4fYJYt_it3WyNEnHUPuWscLtvZTYUfeEPD3hn4EYcyaiN8jK0vJ5DkhLHyWhlvz3UT6xkMHnyu2wrbiZHAGCo7Bxd8zSQJQhUqT9fJGn0KIZUTzMwU-Kw2Gvhk7sbw7F6CaeckFtKLLIF5z879U9DtRDfiihdODOXSEGmxBDcvb4QiAm8zpxt4E2tSHTTSW9GGL1_3w1cLa-8s-2odzv_K7ClYLvPTnWKVshIXCMaItWyXKqG23XBus9HUjMjJRlMiHsd8UCBx4ZQrDaDZ-BPKzj2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پرتاب موشک از یزد !
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20129" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d722b8754d.mp4?token=r0nIKcJSnZnLL4svJXdakAf0COkxCnugS_O9r-cMODwIt3rxiGKHXqoqF5qUedYGHOgw6IUSwlDHjpWdcOlACleuOSpyApYduFN-iaK2NY5zpl7cpq7WS5A1Pv3yZwNS3x4HMTqyIdEsd7EKGW0oiwNggbWSMX-33vYKjXlR8PpRT1hJyrAlLun3MXBOS5ul64EIQj2vglCrKvN1ulRYh3rbpGJ81GlL2gmKN0Xz1vRinoF_cbGxvq8-Kvc1QNiEip9y3kpFE7Dwn6idOivQx1APOamBtP-Y85K3A_Sa8s9yHS5pBmxUCI7x3FZCZYyn8W_zTcwNRRUHfZT1XYatBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d722b8754d.mp4?token=r0nIKcJSnZnLL4svJXdakAf0COkxCnugS_O9r-cMODwIt3rxiGKHXqoqF5qUedYGHOgw6IUSwlDHjpWdcOlACleuOSpyApYduFN-iaK2NY5zpl7cpq7WS5A1Pv3yZwNS3x4HMTqyIdEsd7EKGW0oiwNggbWSMX-33vYKjXlR8PpRT1hJyrAlLun3MXBOS5ul64EIQj2vglCrKvN1ulRYh3rbpGJ81GlL2gmKN0Xz1vRinoF_cbGxvq8-Kvc1QNiEip9y3kpFE7Dwn6idOivQx1APOamBtP-Y85K3A_Sa8s9yHS5pBmxUCI7x3FZCZYyn8W_zTcwNRRUHfZT1XYatBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیور : آیا می‌دانید چند روس در این جنگ کشته شده‌اند؟ آیا تخمینی دارید؟
زلنسکی: کل تلفات روسیه ۱،۶۰۰،۰۰۰ نفر است و حدود ۷۰۰،۰۰۰ نفر کشته شده‌اند. تقریباً.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20128" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20126">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78bd5b2c6.mp4?token=JLUhpzLkD5qfdd2JjKE5G838GaPSaARCCzRtjgn0-2DZef-petReJlFAh51xhtFmW74Prg7dewiMuF0Y6pQcG45YpYB7gLHLNJklTO9d--EZz4DwUEc8ViPoz_Ob_ElsI76JL0OOZss4i5-FctRn512EpMRUDioduqn3BW9M7zknkdHhRK_Kr2qgUoApWE_OyAt8zaQvqwwccWOP-vlGa5wipuQW-pbqxsB36ZxfFIEMvpP7ckd1YJ7Y966rWvjD7T2zUe_UfvkKcwCAei_cEppA6Gou9Pxr6WhH85e3Rwf9UCVZxYyh_24dNMTijAcWGlXsKRYUVjoDofgy1hOTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78bd5b2c6.mp4?token=JLUhpzLkD5qfdd2JjKE5G838GaPSaARCCzRtjgn0-2DZef-petReJlFAh51xhtFmW74Prg7dewiMuF0Y6pQcG45YpYB7gLHLNJklTO9d--EZz4DwUEc8ViPoz_Ob_ElsI76JL0OOZss4i5-FctRn512EpMRUDioduqn3BW9M7zknkdHhRK_Kr2qgUoApWE_OyAt8zaQvqwwccWOP-vlGa5wipuQW-pbqxsB36ZxfFIEMvpP7ckd1YJ7Y966rWvjD7T2zUe_UfvkKcwCAei_cEppA6Gou9Pxr6WhH85e3Rwf9UCVZxYyh_24dNMTijAcWGlXsKRYUVjoDofgy1hOTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور گرفتار وی آر شد !
عادل : من دست بوسی نمیکنم. آخه چرا باید دست یه مسئولی رو توی‌ جمع ببوسم؟! من اگه دست بوس بودم الان داشتم برنامه 90 رو اجرا میکردم.
ما این فیلم رو آهسته کردیم که ببینیم واقعا دست رو بوسیده یا نه. دیگه قضاوت با خود شما که دستشو بوسیده یا اون لحظه به هر دلیل دیگه ای یه لحظه سرشو آورده پایین که شبیه به دست بوسی شده.
نظر شما چیه؟!
دستشو بوسیده؟! یا اتفاقی سرشو‌ اون لحظه آورده پایین!؟
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20126" target="_blank">📅 10:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20125">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بی‌بی‌سی: یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه IRGC، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20125" target="_blank">📅 10:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20124">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک مقام آمریکایی به رویترز گفت که تهران تلاش کرد حماس را از پذیرش توافق خلع سلاح منصرف کند، اما ایالات متحده ادعا می‌کند که بر فشار ایران غلبه کرده است. این مقام آمریکایی افزود که سمت دیگر اگر اسرائیل هم این توافق را رد کند، رئیس جمهور ترامپ ناامید خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20124" target="_blank">📅 09:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20123">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e9526a12.mp4?token=Wdz_Q_gY9umJZfraB6iyl-SCr_FJi6NrKShdQDhwOL1vxxjXJeQhvXqBk4KeN6J4tZShEA92U5BU4ItE_Wg31ECuIE5phpAaRM_vEcCsgJEaHzBXlNgXOzlYyqIQdQtLwMZwY6EPjpT0KSgdsWVguyvf1uMDUzR2k1VBFF1weNXmThtIp-PVljmXHCUCAkHJxmsI1EEmaoNk663JMvV0gxynxZg0-hHT7-8NMCW8o-5qfRK_GiB0d3HxydAQXAv3jLNcbrzK6MmH0w7eydr9emGPztIc5QeqZ3xMv1B4__68GCVam_QQHAhkeFJqcNFliq873tKjd4R6M_Dm-FpcnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e9526a12.mp4?token=Wdz_Q_gY9umJZfraB6iyl-SCr_FJi6NrKShdQDhwOL1vxxjXJeQhvXqBk4KeN6J4tZShEA92U5BU4ItE_Wg31ECuIE5phpAaRM_vEcCsgJEaHzBXlNgXOzlYyqIQdQtLwMZwY6EPjpT0KSgdsWVguyvf1uMDUzR2k1VBFF1weNXmThtIp-PVljmXHCUCAkHJxmsI1EEmaoNk663JMvV0gxynxZg0-hHT7-8NMCW8o-5qfRK_GiB0d3HxydAQXAv3jLNcbrzK6MmH0w7eydr9emGPztIc5QeqZ3xMv1B4__68GCVam_QQHAhkeFJqcNFliq873tKjd4R6M_Dm-FpcnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.  مهم‌ترین درگیری‌ها در شهر توره پاچکو در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد…</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20123" target="_blank">📅 09:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20122">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مقامات اسرائیلی و آمریکایی به اکسیوس : ونس و نتانیاهو عصر سه‌شنبه در یک دیدار دوجانبه در واشنگتن، گفت‌وگوی «مستقیمی» درباره اختلافات خود داشتند
تانیاهو با ونس درباره انتقادات اخیر او از دولت اسرائیل گفت‌وگو کرد
با وجود تنش‌ها، طرفین سعی کرده‌اند روی «همکاری در حوزه‌های مشترک» تأکید کنند تا تصویر هماهنگی استراتژیک بین واشنگتن و تل‌آویو حفظ شود
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20122" target="_blank">📅 09:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20121">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.  مهم‌ترین درگیری‌ها در شهر توره پاچکو در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20121" target="_blank">📅 08:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20120">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ: مطمئن نیستم به اوکراین اجازه تولید موشک‌های پاتریوت را بدهم
این یک سلاح فوق‌العاده است و باید کمی درباره اینکه به چه کسانی مجوز تولید می‌دهیم، احتیاط کنیم
تمرکز اصلی من پایان دادن به جنگ روسیه و اوکراین است؛ کوشنر و ویتکاف، برای نخستین بار طی روز‌های آینده به اوکراین سفر خواهند کرد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20120" target="_blank">📅 08:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMnKWdjoG1RU7mjGgQXUajjypTb-u4bc1ukPeoSn-0MR6uhiZR3rvVA47zMFR9Sp3CkNDUV8PwvXWnJ6E7odvbKk9NjQzWw3BgqJamUYMFqRTWV9lZ5eUj5EdhEpbvW8rgpAqI3Ku2Tvu3wzhLw1u2w0Rbh4lr-5b_2e4ciAxdo5_q9JTR5ku82hp_aGApm4f73pvc-tLIt72PrFe76eEYB7GXikY4E901W9DT1CkkqzQ9VMM7dDfZBnSVWZvpSrOkfXZCSbxFiJjt_Rq-eU8-T8N2AyVsKADF5n4a89fMpOK1mfSXvrWaR4gUZosRxNtrXr74qIZ9StBXmQiyWSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری i24news : ارتش اسرائیل با ۷۰۰ تن مواد منفجره ، شبکه تونل‌های حزب‌الله را در زیر کوه بوفور نابود کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20119" target="_blank">📅 08:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20118">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روزنامه تایمز : سیا و موساد دنبال پیدا کردن مجتبی خامنه‌ای هستن.
گفته میشه رهبر جدید زخمی شده و بالایِ 150 روزه که از هیچ وسیله الکترونیکی استفاده نکرده و احتمالاً تو یه پناهگاه زیرزمینی تو تهران یا اطراف قم مخفی شده. چون ردیابی از طریق شنود و ابزارهای الکترونیکی نتیجه نداده، سرویس‌های اطلاعاتی تمرکزشون ر‌ روی جاسوسیِ انسانی گذاشتن.
طبق ادعای مقام‌های سابق موساد، مجتبی خامنه‌ای پیام‌هاش رو از طریق چندین واسطه و نامه‌های دست‌نویس منتقل می‌کنه؛ پس تنها راه پیدا کردنش، نفوذ به حلقه نزدیکانشه. بعضی منابع اطلاعاتی احتمال میدن سپاه مرگِ مجتبی خامنه‌ای رو مخفی کرده باشه و بعضی دیگه میگن، ممکنه حکومت واسه گمراه کردن بقیه، از بدل استفاده کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20118" target="_blank">📅 04:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20117">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a76d99f52.mp4?token=jTFP3JxF4_PHP8bbqaxT6JQmxy5fJaeoYvs-fv_rP5AgHOheKL_WI_HNf2ngDJr0NmMl_q7HkBgfVLHDMGDNRS8caSrenELhQkH08iYy6iE4cCV118H6gdGl1gsMu6IrwC6DGGUGQvDuMUe0VlWXM_w73_eGHkiRgZUhy3NYn9wV9pxRzhnq4i5NQPl6fmFd-XVUzLmGJ9pFkznkp0A_PTqjZA_zgN2ySBjQjv0w9C6hIhLnAv0tSHL6_3lBhIm6jfG0QCOYskaYaFeN7s-czmLv_3SxpfC4T4ZNQImjE7BFXNf_NbomxhZs6vC1h1IJstKbeLfba4nod9j2iN1ZFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a76d99f52.mp4?token=jTFP3JxF4_PHP8bbqaxT6JQmxy5fJaeoYvs-fv_rP5AgHOheKL_WI_HNf2ngDJr0NmMl_q7HkBgfVLHDMGDNRS8caSrenELhQkH08iYy6iE4cCV118H6gdGl1gsMu6IrwC6DGGUGQvDuMUe0VlWXM_w73_eGHkiRgZUhy3NYn9wV9pxRzhnq4i5NQPl6fmFd-XVUzLmGJ9pFkznkp0A_PTqjZA_zgN2ySBjQjv0w9C6hIhLnAv0tSHL6_3lBhIm6jfG0QCOYskaYaFeN7s-czmLv_3SxpfC4T4ZNQImjE7BFXNf_NbomxhZs6vC1h1IJstKbeLfba4nod9j2iN1ZFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.
مهم‌ترین درگیری‌ها در شهر
توره پاچکو
در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد و به درگیری میان گروه‌های راست افراطی، مهاجران عمدتاً مراکشی و نیروهای پلیس انجامید. در این حوادث چندین نفر بازداشت و تعدادی نیز زخمی شدند.
هم‌زمان، در شهرهای مرزی
سئوتا
و
ملیلیا
در شمال آفریقا، که تحت حاکمیت اسپانیا هستند، تلاش هزاران مهاجر برای ورود به خاک اسپانیا باعث افزایش تدابیر امنیتی و تشدید تنش‌ها شده است
بخش قابل توجهی از مهاجرانی که تلاش می‌کنند وارد
سئوتا
و
ملیلیا
شونداز
مراکش
و برخی کشورهای مسلمان شمال و غرب آفریقا هستند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20117" target="_blank">📅 04:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20116">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1e208199.mp4?token=FJuiitBOEVdnUa9b-EaBYBQLdVV817rcbYjUhZMMM-L-jvZ8eHNvL0KJ9P0aOqYGUL0dEXz7e368HeStLM1_roM3LRCNutbyIWTEYNLnDZt8RlLCXwvjDxqeyALtjnl1orTFp5baNtXvroZ87c395b9wpV__ZEuj4k5kFFOsAgcV058eLCCEG4uiQfB5vV4dRKKB4Mqafbt4lKTCIPgvcj9-Bgm4uu8oHe97eL2Omn5xV5ionAb9d4z_SrlOA57EjtO_5iio0R97ss06JEVWJZa3nk8kp--qLkNV7cMC15z0w4XGz7fVXwZBbGNF4nXkdMNQY74UP2Saf21jFuffbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1e208199.mp4?token=FJuiitBOEVdnUa9b-EaBYBQLdVV817rcbYjUhZMMM-L-jvZ8eHNvL0KJ9P0aOqYGUL0dEXz7e368HeStLM1_roM3LRCNutbyIWTEYNLnDZt8RlLCXwvjDxqeyALtjnl1orTFp5baNtXvroZ87c395b9wpV__ZEuj4k5kFFOsAgcV058eLCCEG4uiQfB5vV4dRKKB4Mqafbt4lKTCIPgvcj9-Bgm4uu8oHe97eL2Omn5xV5ionAb9d4z_SrlOA57EjtO_5iio0R97ss06JEVWJZa3nk8kp--qLkNV7cMC15z0w4XGz7fVXwZBbGNF4nXkdMNQY74UP2Saf21jFuffbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون حملات پهپادی مستمر به پایگاه‌های گروه‌های کورد مخالف رژیم ایران در اربیل
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20116" target="_blank">📅 03:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20115">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apItdsmCotKSsK3mVPQDfFLPCdFIGiOllqk0m_jmHqGZcSQBE_rAu2IsEVgRysPWDUh3_t77idr2HbrPeQ9QeUJUt6oJeaX2LliYALNZshrdExaBBaPM6py6qJjdHwkLt8pw1DJ9jFhuyUm2lr81hVGep7XYmgEQ47PicQwVNASzrhPQuSwsBfh2D294rVmF1YRXRerglH-SJxLXl0oVGk2AylqGeJbCKtK7ANaHQKdwBFxGFaA8L0Qhvjc1cdD_-G-WaPAptWPOKscwZdlZ00J7WkpGSOwMGS6gwj_Jj9AMk3Zqf5oYvpr4gQT8LgOweHEPT1NZsZdAcUFvJkqodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مدعی شد توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه حاصل شده است. به گفته او، این توافق به‌صورت مرحله‌ای اجرا خواهد شد و پس از تکمیل خلع سلاح، نیروهای اسرائیلی از غزه خارج شده و اداره این منطقه به یک دولت جدید فلسطینی با حمایت یک نیروی بین‌المللی و پلیس جدید فلسطینی واگذار می‌شود. ترامپ همچنین از مصر، قطر و ترکیه به‌عنوان میانجی‌های این توافق قدردانی کرد و آن را گامی مهم در جهت صلح و امنیت پایدار دانست.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20115" target="_blank">📅 03:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20114">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ممباقر : حمله تروریستی به منازل مسکونی غیرنظامیان در جزیره قشم، ادامه جنایت در میناب و لامرد است.
امریکایی‌ها عادت کردن که سیلی‌هایی که در میدان نبرد می‌خورن رو با ریختن خون بی‌گناهان جبران کنند؛ تاوان خواهند داد.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20114" target="_blank">📅 00:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mc8FOwNxG-gv5vfXgkrUCBNrRNdrJGSpv254ITx8aFKnX0l1om-5dsXloBTuVlOmbqdTQhmPVQyQpXqHD4CWq9KTsASSXP2qRBEfgKTuS5gxxyCqKAjcuHJJyBwYM3jw2DV8mxrii62cPoZXZw2KAAKCZfF2ndBr9yfp7t8nyTrqnMyc_BZvZF78o5dV82C--sw-fyjOvolC3O8JcPE3K87Nq4i0gpL4Ke5F0ccWA2w2kyyHtFXdH3IH8xxYEEkm_fvTP08Eme-AlCdbLQDpXtopv4xr1hpDPoXkTE3078EUmYgg6c7nT1vPPHVSXgisAq_x9LjLf2F-71PPFPJUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : حوادث ۲۴ ساعت گذشته:
حملات آمریکا به ایران: آبادان، اهواز، شادگان و اروندکنار: شلیک موشک‌های HIMARS؛ کازرون و پراش‌بند در فارس: حمله هوایی بدون گزارش تلفات؛ بوشهر و کیش: گزارش انفجار؛ قشم: حمله به یک خانه و کشته شدن دو ۳ نفر
حملات ایران به پایگاه‌های آمریکایی: پایگاه موافق‌السلتی در اردن: طبق ادعای ایران که آکریکا تکذیب کرده، ۳ فروند F-35 نابود و ۳ فروند دیگر آسیب دیدند و تعدادی از نیروهای آمریکایی کشته شدند؛ پایگاه علی‌السلام در کویت: دو انبار پهپاد و مخازن سوخت هواپیما و هلیکوپترها آسیب دیدند.
در عرصه دریایی: در تنگه هرمز، دو کشتی هنگام عبور با حادثه روبه‌رو شدند؛ در یکی آتش‌سوزی بزرگی رخ داد و هر دو بازگشتند. همچنین یک تانکر LNG قطری برای نخستین بار در سه هفته گذشته از مسیر تأییدشده ایران عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20113" target="_blank">📅 23:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جمهوری اسلامی یک موج جدید از حملات موشک/پهپاد را به بحرین آغاز کرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20112" target="_blank">📅 22:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است.
بسنت، وزیر خزانه‌داری آمریکا :
هر کسی به سپاه یا ماهان‌ایر خدمات مالی، لجستیکی یا تجاری بده، به حفظ یک سازمان تروریستی کمک کرده
ما این افراد و شرکت‌ها رو شناسایی می‌کنیم، معرفی می‌کنیم و دسترسی‌شان رو به سیستم مالی آمریکا قطع می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20111" target="_blank">📅 21:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش رژیم جمهوری اسلامی :
پایگاه شیخ عیسی در بحرین را با پهپاد هدف قرار دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20110" target="_blank">📅 21:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لیست کشورهایی که اعلام کرده‌اند از ائتلاف دریایی عربستان برای حفاظت از کشتیرانی در دریای سرخ حمایت می‌کنند، به گفته عربستان  آن‌ها به این ائتلاف پیوسته‌اند :
کویت، بحرین، قطر، اردن، مصر، یمن، ترکیه، پاکستان، بنگلادش، سودان، جیبوتی، سومالی و نیجریه.
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20109" target="_blank">📅 21:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روند خلع سلاح حماس : ایالات متحده تمایل دارد پیشنهاد حماس مبنی بر تفکیک سلاح‌های سنگین و سبک در فرآیند "غیر مسلح کردن" این سازمان تروریستی را بپذیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20108" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شبکه i24 پیام اسرائیل به آمریکا:
بدون یک اقدام نظامی "معنادار" در ایران، تغییری حاصل نخواهد شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20107" target="_blank">📅 21:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20106">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8772ccba1.mp4?token=Ik5fmdVipf4E56Tz4mTRgCDc5pabCnKP3vd26GEFhg6sAcYyFh_JflXkg1d66JoATgt9fTp_mZM3w74ZwdaMCv-gBIVXB_2HmbWIdoQqLZmV-cSL10gIsDbBln6j8FEBBUIF8G5sDDOgdQowoeB2Y_37Ec_jdzlfnLi_vgFwc-KN_usTxjVYuG-Oq3F5c1YGIY2tjVVRmXOOgyYGE2LcaBel1oLyUa75LV6Yz8sHZi5Gv-L3ZUx-5YAlcEgPmzpzmld2OXdtz6-xgBskafk_YN2ZAkZrWB305v31FuLX_-SIAy8chKxGsF0JVJkLs25rQ1YvVrcFVVg2TsLowZrg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8772ccba1.mp4?token=Ik5fmdVipf4E56Tz4mTRgCDc5pabCnKP3vd26GEFhg6sAcYyFh_JflXkg1d66JoATgt9fTp_mZM3w74ZwdaMCv-gBIVXB_2HmbWIdoQqLZmV-cSL10gIsDbBln6j8FEBBUIF8G5sDDOgdQowoeB2Y_37Ec_jdzlfnLi_vgFwc-KN_usTxjVYuG-Oq3F5c1YGIY2tjVVRmXOOgyYGE2LcaBel1oLyUa75LV6Yz8sHZi5Gv-L3ZUx-5YAlcEgPmzpzmld2OXdtz6-xgBskafk_YN2ZAkZrWB305v31FuLX_-SIAy8chKxGsF0JVJkLs25rQ1YvVrcFVVg2TsLowZrg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنای آمریکا با
۵۰ رأی مخالف
در برابر ۴۹ رأی موافق
طرح محدود کردن اختیارات ترامپ برای اقدام نظامی علیه ایران رو رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20106" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20105">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رویترز به نقل از مقام‌های فدرال و ایالتی آمریکا گزارش داد که بازرسان در حال حاضر احتمال می‌دهند هکرهای مرتبط با ایران مسئول حمله سایبری هماهنگ به سامانه‌های آب شهری در ایالت مینه‌سوتا باشند، اما تأکید کرده‌اند که هنوز به نتیجه‌گیری قطعی نرسیده‌اند و تحقیقات ادامه دارد. به گفته این مقام‌ها، این احتمال نیز وجود دارد که مهاجمان برای افزایش تنش‌ها، خود را به جای هکرهای ایرانی معرفی کرده باشند. در این حمله بیش از ۳۰ سامانه آب شهری هدف قرار گرفت، دست‌کم یک چاه و یک تأسیسات تصفیه آب به‌طور موقت از مدار خارج شد و چندین سامانه نیز به کنترل دستی منتقل شدند، اما مقام‌ها اعلام کردند که کیفیت آب آشامیدنی تحت تأثیر قرار نگرفته و هیچ موردی از آلودگی آب گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20105" target="_blank">📅 20:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو : ممدانی، شهردار نیویورک، ایران و حزب الله و حماس رو حمایت می کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20104" target="_blank">📅 19:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز، با استناد به دو مقام در غرب آسیا، گزارش داد که انصارالله این هفته از خاک عراق و با هماهنگی گروه‌های مسلح عراقی و نظارت از سوی سپاه ، به عربستان سعودی حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20103" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سنتکام ادعای ایران مبنی بر انهدام سه فروند جنگنده رادارگریز اف-۳۵ لایتنینگ ۲ در پایگاه هوایی موفق سالتی، اردن را تکذیب کرد؛ و ادعای رسانه‌های ایرانی مبنی بر اینکه نفتکش ام/تی نورا محاصره آمریکا را شکسته است را نیز رد کرد.
سنتکام همچنین بار دیگر ادعا کرده است که تهدید اصلی برای کشتیرانی تجاری در تنگه هرمز، رژیم ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20102" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش وقوع چندین انفجار در صنعا ، یمن
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20101" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">«فاکس نیوز»: همکنون دولت آمریکا گزینه‌های انجام عملیات نظامی گسترده علیه ایران را به ترامپ ارائه داد.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20100" target="_blank">📅 17:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Bitcoin : 65000$
Tether : 193000T
Brent oil :91.5$
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20099" target="_blank">📅 17:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اواخر شب گذشته، دو فروند بمب‌افکن B-1B Lancer با شناسه‌های LANE90/91 از پایگاه RAF Fairford برای یک مأموریت آموزشی کوتاه بر فراز سواحل جنوب‌غربی بریتانیا به پرواز درآمدند و با پشتیبانی هواپیمای سوخت‌رسان CLEAN71 عملیات را آغاز کردند. این بمب‌افکن‌ها سپس برای تعویض خدمه به فرفورد بازگشتند و حدود ساعت ۰۱:۴۵ بامداد با شناسه‌های HARPO40/41 دوباره به پرواز درآمدند تا با سه فروند هواپیمای سوخت‌رسان CLEAN91، CLEAN92 و CLEAN93 از پایگاه Lajes تمرین سوخت‌گیری هوایی انجام دهند. به نظر می‌رسد این تمرین، شبیه‌سازی سناریوی عدم دسترسی به حریم هوایی فرانسه و پرواز به سمت ایران از مسیر جبل‌الطارق بوده؛ مسیری که پیش‌تر در عملیات Operation Epic Fury نیز استفاده شده بود. این مأموریت حدود ساعت ۰۴:۱۵ بامداد با بازگشت بمب‌افکن‌ها به RAF Fairford و هواپیماهای سوخت‌رسان به Lajes پایان یافت
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20098" target="_blank">📅 16:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9C4rf4U783t8p6dyuuVu5_QMctintZfQBXIeg3_Vl0U-NpV1gHWjLTUKbZd9s4jTHj4rwnNeTp8br6hw-zIMLWVhbdHTygWdvoVCZe-MLErSwprq4o5Uv--Vej1NjFCc8eMIOA_skfdrO5Kxx8-z1CxaqOX3M4eD8YDYvDlms3qFlReAqau2Td40fDo5ez00cP_OsH_yxWLMs1Sa5-Rcw2ShTj-Um5CcGotgZ5ODaf8Wgc3p8ZVRKwAzabbgJaDy36wYX2uPG8bdAwFL2gFsOKl3aX2CQpAXQSnGK5MlwQawvyreKEOBjLjcEIq98RCj_voTN-mwj2ZHu3rKgICMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۳ تا از کثافتهای رسما گی حشدالشعبی که در حمله عربستان کشته شدند (عکس رسمی) همین افراد دی ماه در ایران قتلعام کردند. @WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20097" target="_blank">📅 16:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش کانال ۱۴ : درون کوه کلنگ گزلا - مستحکم‌ترین سایت هسته‌ای ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20096" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اکسیوس : چین با ۴۰ درصد کاهش خرید نفت موجب
جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20095" target="_blank">📅 15:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه زنجان: در حمله موشکی دیشب آمریکا، 3 پاسدار کشته شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20094" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل اسموتریچ:
«غزه بزرگترین زندان جهان است. مردم به زور و برخلاف میلشان در آنجا نگهداری می‌شوند و اجازه خروج ندارند. این یک چیز وحشتناک است. فقط دروازه‌ها را باز کنید و بگذارید غزه‌ای‌ها بروند.»
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20093" target="_blank">📅 15:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خانه ای که در محله مينابي در قشم موشک خورد گزارشات بومی میگن که محله مينابي ها همشون جز بسيج و سپاهن و عادی نیستند ، ویدیو خبرنگار رژیم این گزارش رو تایید میکنه و نشون میده عکس قاسم کتلت هم بر دیوار بوده @WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20092" target="_blank">📅 14:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند و داخلش کنترل پهپاد انجام میدن... هیچکدام از مردم روستا اطلاع…</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20091" target="_blank">📅 14:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خانه ای که در محله مينابي در قشم موشک خورد گزارشات بومی میگن که محله مينابي ها همشون جز بسيج و سپاهن و عادی نیستند ، ویدیو خبرنگار رژیم این گزارش رو تایید میکنه و نشون میده عکس قاسم کتلت هم بر دیوار بوده @WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20090" target="_blank">📅 14:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20088">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اطلاعیه شماره ۵۵ گروه تروریستی سپاه: تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در در پاسخ به حملات آمریکایی در قشم
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20088" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20087">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9ea42418.mp4?token=dKQRnRVio882kOGbNgV_qfZ7ouO7iDQ7Xl-EAWQshgDn5ZojJli5qEFzUDlBaM1rgndHUF7xAWQLAsJjf6IOr3GyRvFq_Xj6ICcX4Wv_XS2hA1xGVCyu3CeDCy1UFbiQbo71EgdGJTJ31mr9Ej_gQV433VXSRCs5SQisMm4iMcG61LcV3KijjGs4PVWRgX3vKJiGzuRnhGQiRNUf295gHoT9W2IlFOmnIauHRbjx_idXf6607tEGuH8r65fbukxYIOxvKMN6FWIL6y8eoSzdZqMuPR6VuKYwD6RHQIF2fFJKXhjEtXEpzxIahHGbxmZXwVxot4jJ5RbGw-rJNRavcnbmpW5Hq4V6RUzrxkBL-GYfItDnG9eErKegTi3tV8XbG-AVebwryWAZe5N6iqkenEybi8ygucWD0uTp5BIJNLlUb_dvD9D0oZniifBkK-Zca_W5OtJt4VOoujePSyDIfkQ6c4pCkMWBA94-3d8f6vGnH5wJbcvivWURWkbX_igZzxo0-zHzOXbRvejFuBLXIDdgMgBNT_LuXFe2AtDQYAdI-kNy1Q66NpxtTFUmM1h_vszs2NZCC1GtBgYdnFPhSZ3nC4lXfx2fA15xGE1BVgvgl9pGSRjyhoCb2R6YspgG4aJTXOx5N4KOpi2Uyw5R7MyK-Q0k7q-8zNpM1K2x-c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9ea42418.mp4?token=dKQRnRVio882kOGbNgV_qfZ7ouO7iDQ7Xl-EAWQshgDn5ZojJli5qEFzUDlBaM1rgndHUF7xAWQLAsJjf6IOr3GyRvFq_Xj6ICcX4Wv_XS2hA1xGVCyu3CeDCy1UFbiQbo71EgdGJTJ31mr9Ej_gQV433VXSRCs5SQisMm4iMcG61LcV3KijjGs4PVWRgX3vKJiGzuRnhGQiRNUf295gHoT9W2IlFOmnIauHRbjx_idXf6607tEGuH8r65fbukxYIOxvKMN6FWIL6y8eoSzdZqMuPR6VuKYwD6RHQIF2fFJKXhjEtXEpzxIahHGbxmZXwVxot4jJ5RbGw-rJNRavcnbmpW5Hq4V6RUzrxkBL-GYfItDnG9eErKegTi3tV8XbG-AVebwryWAZe5N6iqkenEybi8ygucWD0uTp5BIJNLlUb_dvD9D0oZniifBkK-Zca_W5OtJt4VOoujePSyDIfkQ6c4pCkMWBA94-3d8f6vGnH5wJbcvivWURWkbX_igZzxo0-zHzOXbRvejFuBLXIDdgMgBNT_LuXFe2AtDQYAdI-kNy1Q66NpxtTFUmM1h_vszs2NZCC1GtBgYdnFPhSZ3nC4lXfx2fA15xGE1BVgvgl9pGSRjyhoCb2R6YspgG4aJTXOx5N4KOpi2Uyw5R7MyK-Q0k7q-8zNpM1K2x-c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند و داخلش کنترل پهپاد انجام میدن... هیچکدام از مردم روستا اطلاع…</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20087" target="_blank">📅 14:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارشات از آغاز موج جدید حملات پهپادی / موشکی سپاه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20086" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دادستانی اسرائیل علیه یک راننده آمبولانس به نام فارس ابو‌الهیجا کیفرخواست صادر کرده و او را متهم کرده است که به دستور یک عامل اطلاعاتی ایران، اقدام به جمع‌آوری اطلاعات و عکس درباره مقامات بلندپایه اسرائیل کرده است.
بر اساس کیفرخواست:او از محل حضور و تردد اسحاق هرتزوگ فیلم و عکس تهیه کرده است. همچنین مأمور شده بود رفت‌وآمد و محل حضور یوآو گالانت را زیر نظر بگیرد و اطلاعات مربوط به او را جمع‌آوری کند.دادستانی اسرائیل مدعی است که این اطلاعات برای یک رابط یا مأمور وابسته به ایران ارسال می‌شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20085" target="_blank">📅 13:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20084">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرگزاری رویترز در گزارشی ادعا کرد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل طرحی را شامل پیشنهاد ترور هدفمند فرماندهان ارشد سپاه پاسداران و ارتش جمهوری اسلامی ایران به دونالد ترامپ ارائه کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20084" target="_blank">📅 12:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20083">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی:
آخرین خواسته امیرحسین صفری از مادرش پیش از اجرای حکم اعدام این بود که به همه بگه ویدیویی که جمهوری اسلامی از اون منتشر کرده، اعتراف اجباری بوده و اون کسی رو نکشته.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20083" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20082">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرگزاری رژیم : نتانیاهو به ترامپ پیشنهاد داده یه لایه دیگه از رهبران و‌ فرماندهان جمهوری اسلامی رو بزنند.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20082" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20081">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAVEKTzmnmaAOR5kDHMEMAH1kyyV1qaYI7y2NFKTBa-uu3_WhWbiUUm-07GXZhY07j_0Vx6z5UspTZzImiMriAM0aZMBTkPV2nBRXYKzwmYpMPjEeWrD07nISv9NzRmHCVndlDP74V71cHDfAouUZAryKjjtaISf0TBYMA_pYyQjPRUxOUs6vrQMHGglkn91u8csRc_xuny_h12opYqFeaRwOEsCwie_2E7RIduIJ4hCZiWT71asu8fJw6pcK2D1Hg1bovxptc4HldwJinXI7IL_45pvAnKubjqy-xGS3Uj0tZhSAEBJoBjUZmHDc0-EdQnXO8KgiRpQ9f0uQdeLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۳ تا از کثافتهای رسما گی حشدالشعبی که در حمله عربستان کشته شدند (عکس رسمی)
همین افراد دی ماه در ایران قتلعام کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/20081" target="_blank">📅 11:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20080">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نتانیاهو به شبکه ABC:
حماس باید منحل شود و غزه باید از سلاح‌ها پاکسازی شود.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20080" target="_blank">📅 11:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20079">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سپاه: متجاوز همین امروز تنبیه خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20079" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20078">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزارت دفاع کویت : یک ساختمان متعلق به یک شرکت چینی در شمال کویت مورد حمله موشکی ایران قرار گرفته و منجر به کشته شدن یک کارگر و وارد شدن خسارات قابل توجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20078" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20077">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سنتکام : در ساعت ۵:۳۰ صبح پنج‌شنبه ۳۰ ژوئیه به وقت تهران، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) با موفقیت یک موج سنگین از حملات را علیه ایران، در پاسخ به تلاش روز گذشته برای حمله موشکی به نیروهای آمریکایی، به پایان رساندند. دارایی‌ها و تجهیزات سنتکام…</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20077" target="_blank">📅 10:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20076">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو به ای‌بی‌سی: «رژیم ایران همیشه دروغ می‌گوید، تقلب می‌کند و با زمان بازی می‌کند»
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20076" target="_blank">📅 10:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20075">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5647d258de.mp4?token=JMxxEsAKNki9ecA7FvRGn8dxTCBfCBchdlanNC_L1EyaCkYujmb2lu4bGcho1newzue0pWYiYSl5pX4M4o7SulVrXjZd5iRfu6AogJ-kOSIKxXvRHjxsXYEuLleT1ayh4xQ9GF-q59YjqZkn8jTkyJum0l4jd7GagCnNNSZ-xcXHrB7IFm-bYB_PsHyFrGj8m_GzZnrF0uTuGh9aNh9jdIeMhxQ38gt9OupNTOT2owO4KAflj-OHA8N9_IAseWU2nlIXKxLyJ-9NdFK-S536rTi2J2nuvouxrmCgrPANiH1hx4IPlXViMLwGhii-GdgPc1ZcGo5VueBZXuH2lOVovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5647d258de.mp4?token=JMxxEsAKNki9ecA7FvRGn8dxTCBfCBchdlanNC_L1EyaCkYujmb2lu4bGcho1newzue0pWYiYSl5pX4M4o7SulVrXjZd5iRfu6AogJ-kOSIKxXvRHjxsXYEuLleT1ayh4xQ9GF-q59YjqZkn8jTkyJum0l4jd7GagCnNNSZ-xcXHrB7IFm-bYB_PsHyFrGj8m_GzZnrF0uTuGh9aNh9jdIeMhxQ38gt9OupNTOT2owO4KAflj-OHA8N9_IAseWU2nlIXKxLyJ-9NdFK-S536rTi2J2nuvouxrmCgrPANiH1hx4IPlXViMLwGhii-GdgPc1ZcGo5VueBZXuH2lOVovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به ای بی سی: بعد از پایان این جنگ، فکر نمی‌کنم تنگه هرمز اهرم قدرتمندی باشد، زیرا خطوط لوله انرژی را از تنگه به ​​دریای سرخ و از آنجا به اسرائیل و مدیترانه منتقل خواهند کرد.
ما می‌توانیم این گلوگاه را باز کنیم و این کار را خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20075" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20074">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3061f41fa2.mp4?token=spOQP0_LqGgabi5elOrTz6Dko7ecHYOx6akNUCCcnz_RtsLxvg2eN0-Uo_P7xnfZayg1_JTIVCAXlsdxkNOOUxL_YCLQc4_Ma96qrphpX1A5Num9t5a1gOOYP5Kex_6nwo1arXmBzJOTKuebI8eAcpofxOwMlVu8TZWxG-7wuDClPeD2X8Ids7KUsJNa6WZO-EBTZq5IGSL4RhqpI9Ga-DzWXh4JXeO1aZAdgNM-QTBUcGsz9YwS961XgHS9YJ0XZwk2SIw5pKjDw_ttXdA3p89q1woLW9j7lafgwDyGfpxzFalA1Qg5SOePDYZAbLB3F_1St70GufkzcL0VmMLTbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3061f41fa2.mp4?token=spOQP0_LqGgabi5elOrTz6Dko7ecHYOx6akNUCCcnz_RtsLxvg2eN0-Uo_P7xnfZayg1_JTIVCAXlsdxkNOOUxL_YCLQc4_Ma96qrphpX1A5Num9t5a1gOOYP5Kex_6nwo1arXmBzJOTKuebI8eAcpofxOwMlVu8TZWxG-7wuDClPeD2X8Ids7KUsJNa6WZO-EBTZq5IGSL4RhqpI9Ga-DzWXh4JXeO1aZAdgNM-QTBUcGsz9YwS961XgHS9YJ0XZwk2SIw5pKjDw_ttXdA3p89q1woLW9j7lafgwDyGfpxzFalA1Qg5SOePDYZAbLB3F_1St70GufkzcL0VmMLTbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری ای‌بی‌سی نیوز: وقتی در کاخ سفید با ترامپ ملاقات کردید، آیا سعی کردید او را متقاعد کنید که حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک کاریکاتور یا تصویر کارتونی است. این درست نیست.
ما در واقع هر سه احتمال را بررسی کردیم و فکر می‌کنم این کار را به صورت علنی بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20074" target="_blank">📅 10:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20073">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw2OfJDzz3eHkaaRg-D9uOToOixyERZph9_56HEmnwu09l_BLDAI31B48X-wa8O8i5gLJi4AEVn1O1Zmj25eXzXaifVh24hhvXBBQZkarnNac6YaK-BDLplvDLl5YVyYZnTg9joD-RrJ2Nji73_NnnTuixwfQb2FyLyqXuIasjnXaJzoWje_o8a3s0yigpgRn7abXVfO0QgxZnZBYzoB8Jofsd6OGoBkodAXv26SNmDJ3lpqN-CtJWk3JURaACax5KNuGHjj-59foqihvw41alPqWKXgaCgEoT_QBoUCkuiDf_BYXJyhHwtM5l4cguwx0ex9Mp6RMzMxlRvZxv568Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه حملات بامداد ۵شنبه ۸ مرداد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20073" target="_blank">📅 09:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20072">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند
و داخلش کنترل پهپاد انجام میدن...
هیچکدام از مردم روستا اطلاع ندارن که خونه بغلیشون چه خبره فقط میبینن تردد میشه در صورتیکه داخلش سیستم‌های کنترل پهپاد قرار داره
لطفا اگر هم قراره اطلاع رسانی بشه
فوروارد مستقیم نکن یاشار جان
آیدیم به فنا نره
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20072" target="_blank">📅 09:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20071">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">معاون سیاسی امنیتی و اجتماعی استاندار بوشهر از حمله هوایی به اطراف شهرهای بوشهر، جم و خورموج در شب گذشته خبر داد.
در این خصوص تلفات جانی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20071" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20070">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe63b4dfd0.mp4?token=G8bomwLRqnsnrj4aWjq9nWXAq1MncqfsfMrhmJkrx2_umXX9-b6TOiF4eQCUF4jgCNc3xVawzy_DXKsWb9ZLe76mhXrTELlbDzMJiIxa5QE8ZgJ_Hkt9QSppbASWs1CmheUPfFYWkTmYYUXkLKNWTMFS6dBd4vbn1PXxW4yZtwhJUO0Xtkt87Ykg7dD644rg1gGjuav9N79gr8dCCVIr2J3RBTqdfIpzkMwIlTQei_qayNX6WUOi--g2RzASMMEnvYVDAdliBuCHt2glWoHmxHmLa1oeAVfOY7_3GBD-fDaQuyM7lg4o9wKKJVHJ6RbYXaudjaBqM0E-CdQxYbCH6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe63b4dfd0.mp4?token=G8bomwLRqnsnrj4aWjq9nWXAq1MncqfsfMrhmJkrx2_umXX9-b6TOiF4eQCUF4jgCNc3xVawzy_DXKsWb9ZLe76mhXrTELlbDzMJiIxa5QE8ZgJ_Hkt9QSppbASWs1CmheUPfFYWkTmYYUXkLKNWTMFS6dBd4vbn1PXxW4yZtwhJUO0Xtkt87Ykg7dD644rg1gGjuav9N79gr8dCCVIr2J3RBTqdfIpzkMwIlTQei_qayNX6WUOi--g2RzASMMEnvYVDAdliBuCHt2glWoHmxHmLa1oeAVfOY7_3GBD-fDaQuyM7lg4o9wKKJVHJ6RbYXaudjaBqM0E-CdQxYbCH6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خمین
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20070" target="_blank">📅 07:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20067">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIls1bYkpXcURWT9TpCZ4OuOQxXtgXWXh_yg4XeepWMI-K3bkxaz01O-nc9VjpBz6Cf-dFQs3bwmgSh0uCmx9mT_lbTR_YKkPFqh0tA6UcAq38HbkfO0C78ObchPlpPCdCy6R4bbpY5RnFQ-rrLaZ9MAa816kiwuy7C_QgI6b-erSoPKmFC8y-FCBaonpkuVaeHdzYcjunqtzVZ5HfPgGs3qR5OLR74xuU8mGDIiJ9JqRmqSfTwENNLWb6QSWehEOJson4cLCJSVsq52HXW_S5hdfT0dmvPmSnzHn7Aa8oHsx08YVKsamsaULjMg-llIyXgzYKTZ8olmUMoZ8Z16tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g0m9HPm1Q8X9PMS2g6V446hVUBgezyZ-aXLNKNYba7G2AEC6-ePORN27jcRKjYyvjzAUejAGcfepoJmswNcas8BymVNQAk3qzH8G8iJjD-fLeMT4endv4fSWtUYLTakZ_-0SGcGMyVL5FnxcQTypWBUNS2dUNoJIgw7mO0Z4SDIAWDFxP6hMfQsbtKKRJG_Fp4xUXPeGU5daFpMzmW08ZM69Mbnb7PtUs7fBqhDfLWD8XOHvqYvKRXjOkUy62yAZmFGNd4DICQ7OCn5CZZ5rf9uZPmp3tW4yY_VNhyFda74j8pD33ZZg1_lpZGTAtmHaQSg-ISKF_sx54suvlkUX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMK1chxdkImezfzQekKLI1n_eF1MqbsXYUdSmcwzhjdAytiE8NmMp5Et8h3wy_x6lNDt7Ru9oUwVULnCSWYOpxhtLq4gYjFqlnQWwu6FaFyGQm8A4oI0z-o-NPm3-VaLvVAYy0Ff3CpvLeCqpx3xD8g1PuHjA_mF9wmO7RN1exmLlPQngIJE4lLpNBZdmey-UOPVdCwQbdCLcpAlVbOd1P_D75NYLgIkInAcyxPZ7EGFvVw_OZ8EGmluCasnt3ffdQWshDbrjwaJCNCYpzAErIDonmkRy-Mzrlm61cYHleR65bae23qUJZA9_IgjftwH3l2SjrJjeuqYJfPQT5PYPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قشم ( از پارچه های یا حسین به نظر میاد یک پایگاه بوده )
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20067" target="_blank">📅 07:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20066">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739655b0d2.mp4?token=Z-oF-zWcN_GxXIIWeQh2QM2BVfWCvVg_Mlc6mKYnGmUJW_Ee4WPLjOiNst50oK3gIsgTfq-zLfl_8Jrz0wKdBFVF8ZsXiD2yej5MptvLbo__qFMMLJvOSleLBfQr2gvwjl-taG8qqhkOLGagelW963_QRuqvXyG3N_trUk_H4ECnNqNsi0l2_XaSCNMvO1qE-cCRbfP7Qa4oKiA1K9iM2IPUMW2j-VC2ulhEOShKMHELT8ftdpPwyVqWqhPG4K9WlIzHKqTjNSIMdWe_AaBHcGn999KmKAzPuRV2NEfnnTd0ddpwGTloxNCknwldTgkGbzDZQE88pxBvTbCnD9lvWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739655b0d2.mp4?token=Z-oF-zWcN_GxXIIWeQh2QM2BVfWCvVg_Mlc6mKYnGmUJW_Ee4WPLjOiNst50oK3gIsgTfq-zLfl_8Jrz0wKdBFVF8ZsXiD2yej5MptvLbo__qFMMLJvOSleLBfQr2gvwjl-taG8qqhkOLGagelW963_QRuqvXyG3N_trUk_H4ECnNqNsi0l2_XaSCNMvO1qE-cCRbfP7Qa4oKiA1K9iM2IPUMW2j-VC2ulhEOShKMHELT8ftdpPwyVqWqhPG4K9WlIzHKqTjNSIMdWe_AaBHcGn999KmKAzPuRV2NEfnnTd0ddpwGTloxNCknwldTgkGbzDZQE88pxBvTbCnD9lvWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20066" target="_blank">📅 07:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPs1AVePwR9uGuse-2N_VxVE_ViSWOoTiqjI72WqUWUrVhe3Cd0Il5mZdD4If9OiYVpuJK7OiARKlPu-6qRFdve9Js-hk6GPQfZD6kcaDT8VnWvsSSEUQymT2ENsb0Pl9_2c9euct7K2VptjcnTEafLQHIplKEURgzbatSbGXV6LrF3-gZOpBTHjELp2_IU0K4OXwSP05RYQpgc-wJee-_o1Ua4zzNwqoC8d1D-nSwivde0XpRhrwastbMDsDrVFwUktMajNMoMKrvUiOOlK4ITT3vbQ3XdJgy3_U5Bnq1BssglqAg6MuvrQIcV-ZWIcNElmRziJfnhYNOBpBo4toA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0a3za2lzLaz5xlhVUwuz9JmCXUfM8Gh6MWfkrM1Us2gBcfGMFXLslXKsQOB1aqbFVUDDVYegK2zHaPUDZLOw7QW7MO1R3s0ejTiTS6OL-Op5g6g7hEF90yGAjIC-P4teVynRUM6N_cCItH5CL_S3u0xe7dde6jFX3hicBrCooqhPXzEAzAN3-p6YL8POL9LOU_oxNOcwjTRKFyK0p8H28qPXbQGmiB5lXhOc2t4S6y0wHKZtv7iGetYxTBVbxQhdfWKspyQoMIH-Aw_SKGVmWtCyShvI6pvNG0BpS0Wn9FcM8hU7OhqKX0btEcgX1iVAl7rNeH1wyt3uutSbsIjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxD79Vg3BxJ_w5W1jxXbmufqsHfoZmZpvc9lt4_I0MUbof8ABtfYaCdj38Q64XcNsnOxLKfEImUHOsGe9mQ5VV4QGP4yJW7_pt8MI6Z2CQzLQLDOIgCb1CcwDrTny3vlq6ZebSrOdo-0T7nc_-hhiZtUNufV_-ibhZQDnRoWpFEoZRE3fakjUjBebf7o2r5EwdgzyokzkTOzfwh0a1gDW-moDtcuP157JfgewSd7_rUnukgDVdn0e33s890hqpq3QBjchIQQRIqPYx3bIX466ASNG-kNtBypf7Rt7h5O3a7z4r-CTzyM0imMcIwaIli6VzSctuy1GI93K3XdFRbkxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1QigIsfIvfYdtuOfHo6_TYXRL3lVLS8d0IliHB6CiV8JUtKZ21CbOc1KyTulbaOpcRLuFWlF7sKgZTGHyveGth5SqnmK0WX5FcSKcaJlDgCb_IbCTd_qU4VZ5tVtXRtL0zL7J4SfL3LFupUT2CDoko64MOnTTWqNCzKrSz0vmO1NGjXY5LoWgxZ_2E9JZA7InNkin60oRiegINjwr0tKqSju8edraWzcwkBsgCQIjIptl7hgCoVB4ay-fMdMWLJiswkW_2aoE02xLJuNmGjMjc7131cwUDu2xisszmIZnWWrp1Kk4INDuUjO7lFY_C2AfpHUp64YIWO5ygGhmnWAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از یزد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20062" target="_blank">📅 07:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c918aabbfc.mp4?token=UKp__otE9o_I81sR9uqCc4sgWi2nfJmKXujV4Cm8y8soU9ZqfNiLvGKmkYDxzt6D38YUeEGsLigqcw5XQSpBI2QNs2L3ZXcd3i9im_8ZqflnO3SYEcYhA8hFZuZI7p8YCh6_eLx7PFwaADQevoOOjJVYgYpZc2kHga7z0UxmNHN3FoUk-b-M_Dq5OB_n69Q2emVRK3QFxovY0f_A61cJtVEaWhrJv_jd8y6BpOOT_KLWCz5LYOCb7oE_sKPJhmE9377bv2r_wk7oJBOXUNRv4aYqLoWrBFiKiyzSxWEoDlhfLJXY2Jqc4VUhQKtJz8WUtNhXBZWnM_t2ljP0Jxsl7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c918aabbfc.mp4?token=UKp__otE9o_I81sR9uqCc4sgWi2nfJmKXujV4Cm8y8soU9ZqfNiLvGKmkYDxzt6D38YUeEGsLigqcw5XQSpBI2QNs2L3ZXcd3i9im_8ZqflnO3SYEcYhA8hFZuZI7p8YCh6_eLx7PFwaADQevoOOjJVYgYpZc2kHga7z0UxmNHN3FoUk-b-M_Dq5OB_n69Q2emVRK3QFxovY0f_A61cJtVEaWhrJv_jd8y6BpOOT_KLWCz5LYOCb7oE_sKPJhmE9377bv2r_wk7oJBOXUNRv4aYqLoWrBFiKiyzSxWEoDlhfLJXY2Jqc4VUhQKtJz8WUtNhXBZWnM_t2ljP0Jxsl7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریز شبستر دو تا موشک رفت
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20061" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwAmW1napFrisQWzA91leoUAS_z2mK4CUiVvfddY4GHPzBm19DHoqeJ2xRVHYeCHEwW2ISG1Ha_yKRcUeRwghVhcjVphBPf0WeyceeVgSt4e1HvvUEhutKmQkeRZDP3p6o84_yjyN7gkLjvpextoaTH_YeRSyvbT4BzLsrMTFVYbEXZ0LWZWpPSomPB6I_kikYihhyj0IQ9yP3SteGBVWjarnkC5lR9fja94VvW9U28xvzjYpyXEy40upJob7ygHUkflsJjN4IoLmGLQZg2nmVkEeA6dSp3HftKWYz896nc5o-RyLYFtLM8JZB_7xzy1GrtX3i7Pg_BhyrTnx6pZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان پرتاب موشک از خمین
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20060" target="_blank">📅 07:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a4989fd2.mp4?token=kJONEnBVSkIRHAHzIhBgKQZWERINLCJZS8WtkcHTRQb-OUq8hB4HJzfm4-jAVgSjZa0EhKXn0LCC5nDMlcLj-b-Y99KZuS_LvmOvGE6GHSD0OPAuNLCyvTVr7HPQGcyhNcPKq5WeY72bEgTkLRxl2IhqE5o4v-sQjJZQMaqIgd_mwa4pFK4eQCFVvDKZ-dYQkUBb2aqZy4N2exmbeSkjN9KY3YxiQ_h-m97n5xNpghsTWyAPB1EcjltyxWZ0W-yEHkxBJfgahSiOM8hzjCfU4PrIoS_TLLu47QH6Mu77z-_f74U8kTaZ2JeQINWKgFQBWrEDaQHJwxg9MYOMf0KHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a4989fd2.mp4?token=kJONEnBVSkIRHAHzIhBgKQZWERINLCJZS8WtkcHTRQb-OUq8hB4HJzfm4-jAVgSjZa0EhKXn0LCC5nDMlcLj-b-Y99KZuS_LvmOvGE6GHSD0OPAuNLCyvTVr7HPQGcyhNcPKq5WeY72bEgTkLRxl2IhqE5o4v-sQjJZQMaqIgd_mwa4pFK4eQCFVvDKZ-dYQkUBb2aqZy4N2exmbeSkjN9KY3YxiQ_h-m97n5xNpghsTWyAPB1EcjltyxWZ0W-yEHkxBJfgahSiOM8hzjCfU4PrIoS_TLLu47QH6Mu77z-_f74U8kTaZ2JeQINWKgFQBWrEDaQHJwxg9MYOMf0KHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز حدود ۴ صبح
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20059" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7049e361.mp4?token=DPGquReUohgp4YgtjoyW7ues9kCcV-gMTfriY5DnTAJtyzPdws8O_TorgG5bfFcSbjmNrQCpW3dGosMF7yHscoRl7vSahq6pW_Pl0K6hvFZkSZPF9HSh5FVTnDjJ35ecnkd4u-YmLLojcBArmagOuDpRN-VGuuf8nw5aaui3Vvu8fSBgb6xk9r6HvXX9SNuC66y5JLx0LBszqGUly1U_ZzZB3soOcwgxCzf1pxm4vi3gtjsXTjG0d9VRLt8BV7NSGJDMtkGT7kkOm5GV7CF6NzjU98gEvRYcexWYVwKuvlDdrsQEsw2efqVJAFafOVtSjF6wZLvuQHkm3j35Ki5aTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7049e361.mp4?token=DPGquReUohgp4YgtjoyW7ues9kCcV-gMTfriY5DnTAJtyzPdws8O_TorgG5bfFcSbjmNrQCpW3dGosMF7yHscoRl7vSahq6pW_Pl0K6hvFZkSZPF9HSh5FVTnDjJ35ecnkd4u-YmLLojcBArmagOuDpRN-VGuuf8nw5aaui3Vvu8fSBgb6xk9r6HvXX9SNuC66y5JLx0LBszqGUly1U_ZzZB3soOcwgxCzf1pxm4vi3gtjsXTjG0d9VRLt8BV7NSGJDMtkGT7kkOm5GV7CF6NzjU98gEvRYcexWYVwKuvlDdrsQEsw2efqVJAFafOVtSjF6wZLvuQHkm3j35Ki5aTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس ۳:۴۵ بامداد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20058" target="_blank">📅 07:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b11a9cf.mp4?token=MgZy4sQPLYsuPfTCEZQmZa8VfxZVgAP0sKS5rpXcZ-3BkxxnA0qP2sy1taHMK_aWHIRDZkV_2XvjkB-zESSRCaqck29A3aHP2N__brzqModgkMK7_Vz3KHvvDevW0GIM8HOesprEk_BLocmtGCPdV15y1ZItJumA5tbE8Nvon7kqnJgcA07HSQrdOq9KDuXtHePlfBoKOEhrwMU4Aex0sB_A7jstPRoDUscK_5RLzIZfh6ah6A61mw1kqjLRj640d5bBxd83qOVY7OETWMAnyjrCFZlSGHgFbHlrgY2OqeQHfI9BeujdNPZFCyWv6u03aXLlKjwllNncMVR286COTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b11a9cf.mp4?token=MgZy4sQPLYsuPfTCEZQmZa8VfxZVgAP0sKS5rpXcZ-3BkxxnA0qP2sy1taHMK_aWHIRDZkV_2XvjkB-zESSRCaqck29A3aHP2N__brzqModgkMK7_Vz3KHvvDevW0GIM8HOesprEk_BLocmtGCPdV15y1ZItJumA5tbE8Nvon7kqnJgcA07HSQrdOq9KDuXtHePlfBoKOEhrwMU4Aex0sB_A7jstPRoDUscK_5RLzIZfh6ah6A61mw1kqjLRj640d5bBxd83qOVY7OETWMAnyjrCFZlSGHgFbHlrgY2OqeQHfI9BeujdNPZFCyWv6u03aXLlKjwllNncMVR286COTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">4 صبح آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20057" target="_blank">📅 07:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فاکس نیوز : هدف سفر نتانیاهو به امریکا تکرار 9 اسفند و بمباران تمام سایت های هسته ای و موشکی و نیروگاه های رژیم تروریست اسلامی ایران بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20056" target="_blank">📅 06:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmK4Q686pkL0vxE83djbc0WpDZ0J5DG0QpkusEZ7ZfPgwc9px-HfL_-7CeGW0VjyXGcI7aT8gFtxGN4kv59MMOMgCqJ4n06BUkpFUqV_kioQE4RAgU4M7Qdorti4kX7svraCSWxa6PWe0pv0z2CHfOBWjzfO3jdqkxG7sNbzEucI5qQ-gpmM_RGocSnn9TR4pAKWInHH5CS32htcWv4mOUsyOSr3GyGixRQZeeZMSnRu0jEr5L3UU7XmVcIaQ44w_VV7ZAjtokNSqXjDyC0e2ZborddM-WVp1TNcvFfnoR_reUpCDCgBHAwBMrZzcQtVAtnhc75jhFDqrinsjfXQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : ده‌ها موشک ATACMS برد بلند آمریکا از کویت به سمت تأسیسات نظامی در داخل ایران شلیک شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20055" target="_blank">📅 06:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc88dc378.mp4?token=EDSsxlLiD-e772iOBq32KYwPdENdxY1dmohure0psn4jAjQ5MdbW-ZQKccSshkLdfXVgJd8neao1WgSh-2sZrmQMkeld8_8cwfk9xqEDquw3Iy0A2j6w7Nb4OuGpeig4iLS4ZEN9_IdLHSs_i2IVU5TIVd3VI-sCFv6PF1b1pAXlf5Uerj7hDoVkRxPi-o_Qg9SxnqQMIRBWdvX5th_CvbrisCgO09E9CHAYyRGx_F5jxWn4BtOa4BVI8-Jy5D9MLoUL4_J7ECWC5ElJfqEONhwEYognCZzCPgISQMk1D9bEt696_j99cCydSrswRl8ZB4vU-As2EvhBBNV9T5Zc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc88dc378.mp4?token=EDSsxlLiD-e772iOBq32KYwPdENdxY1dmohure0psn4jAjQ5MdbW-ZQKccSshkLdfXVgJd8neao1WgSh-2sZrmQMkeld8_8cwfk9xqEDquw3Iy0A2j6w7Nb4OuGpeig4iLS4ZEN9_IdLHSs_i2IVU5TIVd3VI-sCFv6PF1b1pAXlf5Uerj7hDoVkRxPi-o_Qg9SxnqQMIRBWdvX5th_CvbrisCgO09E9CHAYyRGx_F5jxWn4BtOa4BVI8-Jy5D9MLoUL4_J7ECWC5ElJfqEONhwEYognCZzCPgISQMk1D9bEt696_j99cCydSrswRl8ZB4vU-As2EvhBBNV9T5Zc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اطلاعات سپاه گلستان اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20054" target="_blank">📅 06:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aabd75843.mp4?token=Y71qmLZ7lVZouv5sB5APthkX0gWafvROaG0mbgcGmPXF_Xwdz7qwR1ZpOryH6a7BlTveFo6SYrT0LBOJOEy6I0mUzncRD-q8oOAGKHEtzUVgavCKfgNTzrwXfsBarUQMSngGv6pPSCVsnhFMiGdq-2w0yD1DhHwiTiSFbx8pzWMAnO-Qeof202YAp4POftuRt7uthC5sZwYJUN9-TEZYnPUz71tJC7UVv27nhLfw9zQwMXsACKOuZ4-IBZa2It6iyzS2pCAx0tLxUoe6uKyaADlb4OD49NncFa70FcQif7dSU9QjVa_55ICxU5E0c7SXPhl1sMaZJsJqnV7etOLFoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aabd75843.mp4?token=Y71qmLZ7lVZouv5sB5APthkX0gWafvROaG0mbgcGmPXF_Xwdz7qwR1ZpOryH6a7BlTveFo6SYrT0LBOJOEy6I0mUzncRD-q8oOAGKHEtzUVgavCKfgNTzrwXfsBarUQMSngGv6pPSCVsnhFMiGdq-2w0yD1DhHwiTiSFbx8pzWMAnO-Qeof202YAp4POftuRt7uthC5sZwYJUN9-TEZYnPUz71tJC7UVv27nhLfw9zQwMXsACKOuZ4-IBZa2It6iyzS2pCAx0tLxUoe6uKyaADlb4OD49NncFa70FcQif7dSU9QjVa_55ICxU5E0c7SXPhl1sMaZJsJqnV7etOLFoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در
ساعت ۵:۳۰ صبح پنج‌شنبه ۳۰ ژوئیه به وقت تهران
، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) با موفقیت یک موج سنگین از حملات را علیه ایران، در پاسخ به تلاش روز گذشته برای حمله موشکی به نیروهای آمریکایی، به پایان رساندند.
دارایی‌ها و تجهیزات سنتکام ده‌ها هدف متعلق به سپاه را در ایران هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، سایت‌های دیده‌بانی و دفاع ساحلی، و توانمندی‌های دریایی. هدف از این حملات، کاهش بیشتر تهدیدهای ناشی از ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حوزه خلیج فارس عنوان شده است
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20053" target="_blank">📅 06:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس به نقل از مقام ارشد آمریکایی :
آمریکا هم اکنون در حال انجام حملاتی در ایران هست.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20052" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بوست کم شده داریم لول میایم پایین یه کمک کنیدد بریم بالا استیکر شاه برگرده به دوستاتون که پرکیوم دارن هم بگین
https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20051" target="_blank">📅 02:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش‌ها از شنیده شدن چند انفجار سنگین در نورآباد ممسنی فارس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20050" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، در ماه فوریه تخمین زده بود که کمپین علیه ایران برای دستیابی به اهدافش ممکن است شش هفته یا بیشتر زمان نیاز داشته باشد.
کوپر در ۳۱ مارس ارزیابی کرد که هنوز حدود ۲۰ روز دیگر برای تکمیل عملیات نیاز دارد.
با این حال، سرنگونی یک فروند جنگنده F-15E Strike Eagle آمریکایی در ۳ آوریل بر فراز جنوب غربی ایران، علیرغم نجات موفقیت‌آمیز هر دو خدمه در تصمیم ترامپ برای پیگیری آتش‌بس تنها در چند روز بعد نقش داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20049" target="_blank">📅 02:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش صدای انفجار سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20048" target="_blank">📅 02:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رویترز: انفجارهای شدید و پیاپی، کیف پایتخت اوکراین را به لرزه درآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20047" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
