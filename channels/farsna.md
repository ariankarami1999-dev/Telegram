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
<img src="https://cdn4.telesco.pe/file/U3aLflqBG6NJyk7q4Vg-PRRqaGwhBzWGwAynLeJHYFY9Kw3iEffaHLjBQbid81CsF7SFK8N2_EREOAPaTRBrwk6yuae6gJ8WmTiQC2HRZz4eCLNAA1KCf0KZDxe3rJ-_RTXQO57AHJ7lf-JPGHzR5desY-6g-h9fu5gWXYq4p029jBNT9oJbsSzsmM0IWHIBHJ_c7fax5WQm-azkknRZWY_ZNCihxadIdLpHqIDahZ76gPnpNylNMPAUhpSf2x81ed4rYkYOgKLd9rlVBj76ZMthsjrCW2vJ9h6DzrU-2QpssMmP6Pyiwf8gYzkJJlGNusvcGneDfP-MqRp4mkLeWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-459542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تکذیب حملات دشمن به «جم»، «کنگان» و «لنگرود»
🔹
شبکه‌های اجتماعی از وقوع انفجار در ۳ شهرستان «جم»، «کنگان» و «لنگرود» خبر دادند که مقام‌های استانی اصابت هرگونه پرتابه و حمله دشمن آمریکایی را به این نقاط تکذیب کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/farsna/459542" target="_blank">📅 22:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
🔹
استانداری هرمزگان: دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان یک منطقهٔ مسکونی در کوهستک را مورد حمله قرار داد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/459541" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e810f08972.mp4?token=uVUbGxhM_GgwUGAZWSNt62mzMI2wBt-ckiBzezAs7h6pgJEeAV3SDrqcoueaBIhwU7CgbSyqy1nHUtKc0qN5KUhN6V2i6A23BTTqe3Yjww7gF8XBwqiu4jQjlvZItSU1nT3fCSEqhMYxbGCZS8bm5uQDcC9LiV2bWfKIrJl-XNrSNB6N_VA3Ub9NfcxnXSNQvtSXvZZ-jnZaEZGot3YGU3GUutI-V7Ci07N2tSxYs2aGDe0sYBJJsuZBt9iE9nRW7Ka9wLVPratHuIID-Gi-KVJw0xnyfpKwOrcf5sDIwDTvM0xCXAnowStmIycdLjaSp3l2G5Mhr9t-ohL9cje1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e810f08972.mp4?token=uVUbGxhM_GgwUGAZWSNt62mzMI2wBt-ckiBzezAs7h6pgJEeAV3SDrqcoueaBIhwU7CgbSyqy1nHUtKc0qN5KUhN6V2i6A23BTTqe3Yjww7gF8XBwqiu4jQjlvZItSU1nT3fCSEqhMYxbGCZS8bm5uQDcC9LiV2bWfKIrJl-XNrSNB6N_VA3Ub9NfcxnXSNQvtSXvZZ-jnZaEZGot3YGU3GUutI-V7Ci07N2tSxYs2aGDe0sYBJJsuZBt9iE9nRW7Ka9wLVPratHuIID-Gi-KVJw0xnyfpKwOrcf5sDIwDTvM0xCXAnowStmIycdLjaSp3l2G5Mhr9t-ohL9cje1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۸۵ مردم کرمان با رنگ‎وبوی جهاد و حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/459540" target="_blank">📅 22:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459539">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اصابت پرتابۀ دشمن به محدوده خارج از باند فرودگاه جیرفت
🔹
معاون امنیتی و انتظامی استاندار کرمان از اصابت یک پرتابۀ دشمن آمریکایی به محدوده خارج از باند فرودگاه جیرفت خبر داد.
🔸
این حمله هیچ‌گونه خسارت جانی به دنبال نداشت و به باند و ساختمان‌های فرودگاه آسیبی وارد نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/459539" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459538">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/459538" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
🔹
استانداری هرمزگان: دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان یک منطقهٔ مسکونی در کوهستک را مورد حمله قرار داد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/459536" target="_blank">📅 22:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqYuC_o0h1b2fFD8gTDSMPb6qVdCKVm0iaWTO-TGEMYusTnnlSrmI2Lv9zuof_DONY8YChnE47HoUZq_G7bw5kBaLxZH9mzW9LUtztEZqZf6BIu0sCsERBmLw4RbW34J0ahzceKvxCIoT2QedqGToysEAry_jjTxKopbdiz81Lv6YDoy1H3HP83QkMMY0DMlwxzd_nLoZ7WPLcHOgO4EcH79Si9SuSGZ3uJiDI4MKeekeOW3DKfO19COgpSJAy-M1X_9m90mKcWF4-b683TEcsAslxzwpHG_zEc23iPFSR0QeuI5xL7JVpKeDhCZSrnZyseGZJS7eianBx6OlSPl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویب دریافت هزینه خدمات از کشتی‌های عبوری تنگۀ هرمز در کمیسیون امنیت ملی
🔹
سخنگوی کمیسیون امنیت ملی: بر اساس ماده ۳ طرح اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز، در قبال خدماتی از جمله خدمات دریانوردی، محیط‌زیستی، سوخت‌رسانی در شرایط خاص، بیمه‌ای، ایمنی…</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/459535" target="_blank">📅 22:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623c890cf8.mp4?token=cxLjYV_fJbwrg2eJ--fBut_n0dO7JCWXcWDHAHKlg7XttwMVjTN8Qy95phDdyRxdDOEYewudPKDVQ_nz6spVZNAkeRaxF2ZFoFFAFUmoeEP_8rDP0wGwXH1Z9tJz9ZVmBqfJJzFjNAU5Es7EpMaSv8Zv37Icy6u4WiJr8C2emoj5-SdiYQ_KkMFVsEOT7zi9v-p2Ax8d3YkGMLrV-g2xCJfW5sXPsHDJV9ix58mVqxMlFE89DK_6HqnBVPoFyBkxNNYIRqIiZH2VEJjhM4yGpI-OM2B_FUQBSBk5dvKePcWR4MlFEOqAsdIowkBMIfIBsGAgKOMn7cRh-QIAxajGaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623c890cf8.mp4?token=cxLjYV_fJbwrg2eJ--fBut_n0dO7JCWXcWDHAHKlg7XttwMVjTN8Qy95phDdyRxdDOEYewudPKDVQ_nz6spVZNAkeRaxF2ZFoFFAFUmoeEP_8rDP0wGwXH1Z9tJz9ZVmBqfJJzFjNAU5Es7EpMaSv8Zv37Icy6u4WiJr8C2emoj5-SdiYQ_KkMFVsEOT7zi9v-p2Ax8d3YkGMLrV-g2xCJfW5sXPsHDJV9ix58mVqxMlFE89DK_6HqnBVPoFyBkxNNYIRqIiZH2VEJjhM4yGpI-OM2B_FUQBSBk5dvKePcWR4MlFEOqAsdIowkBMIfIBsGAgKOMn7cRh-QIAxajGaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان در شب ۱۸۵ هنوز با حضور مردم روشن است
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/459534" target="_blank">📅 22:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در عسلویه
🔹
فرماندار عسلویه از شنیده‌شدن صدای انفجار در این شهرستان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459533" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3xVs2nf2lIaNgXVGwG3nLDpv5HytRmQjY1a5sLfp23XnD-8ruSj1XlPG4BTsgPD2UKEkset5pIT32_n-79tRGxQIvEv96Glj9EAbZ5uRDUl0fI8egYJSZdhqrSPeYEsPjbtrlznuMoGdIUlZAe54cBsPMrrYcWLqlC3souqAa8H8tRAjkLi9xdQLysGEWCt7_wLFIs8Iy9DKEh8STobYK0pwkG8lKo9hgY4_pqHCY87CyPN5WOObAvYYgTFmH9K4BOvYLM47X6rVmrbgbHD8fs5hX0LTA6f-UPcnBzBuGiUHwhxpSkepixlTovyxCauTluUGv29DshKhwoxh1Hacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل سپاه: هماهنگی پدافند هوایی ارتش و سپاه معادلات دشمن را برهم می‌زند
🔹
سرلشکر وحیدی در پیامی به سرتیپ الهامی، فرماندۀ پدافند ارتش: هماهنگی کم‌نظیر بین نیروی پدافند هوایی ارتش و سپاه و شبکه‌سازی یکپارچه، به‌روزرسانی مستمر فناوری‌ها و اتکا بر توان جوانان دانش‌بنیان ایرانی می‌تواند معادلات دشمن را بیش از پیش بر هم زند و بازدارندگی اطمینان‌بخشی را برای کشور ایجاد نماید.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459532" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
شلیک موشک‌های ایرانی به‌سمت مواضع دشمن
📝
مشاهدات میدانی خبرنگاران فارس از شلیک موشک‌ و پهپادهای ایرانی به‌سمت مواضع دشمن حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459531" target="_blank">📅 21:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175cd3fff.mp4?token=jS-z_A-auWEt1XWUEwwxRpPN9lboVJ5xwfCAX7dys8QSexSpmjQGYffzEcTTIEuJN46HNWJPe6Y799kOqACX13kf_zSjVNjLTKcEJxqtSWvfEMLUgRpvxLSaxMs2ifxdwY-kYETDHYOdL9hlYTTW5tNU0wb5OUgBznTukPm97C6JGH6SxLfq23xWOiFSHsxbzdLzkmk8KB1mBzWLlnGw28woLL0a9At9GReGkxBaSkqAM__LegS-rFQt_kyzLrRcPWjxalCQjHV4xzIbU8esDCoCNP8IYuVSIR0HtI7QV15Tfs6rvwVji5xhgy2O6dM_TDYzj8zoFwAZWw-zshzzcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175cd3fff.mp4?token=jS-z_A-auWEt1XWUEwwxRpPN9lboVJ5xwfCAX7dys8QSexSpmjQGYffzEcTTIEuJN46HNWJPe6Y799kOqACX13kf_zSjVNjLTKcEJxqtSWvfEMLUgRpvxLSaxMs2ifxdwY-kYETDHYOdL9hlYTTW5tNU0wb5OUgBznTukPm97C6JGH6SxLfq23xWOiFSHsxbzdLzkmk8KB1mBzWLlnGw28woLL0a9At9GReGkxBaSkqAM__LegS-rFQt_kyzLrRcPWjxalCQjHV4xzIbU8esDCoCNP8IYuVSIR0HtI7QV15Tfs6rvwVji5xhgy2O6dM_TDYzj8zoFwAZWw-zshzzcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: کسانی که تا ۳ شهریور به اماکن اعلام‌شده مراجعه و محل زندگی‌شان را اعلام نکردند، تا پایان شهریور فرصت دارند برای اعلام محل زندگی خود اقدام کنند تا کالابرگ به آن‌ها تعلق بگیرد
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/459530" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6888c2e65.mp4?token=J5uxHPL2fwGtDk6yDtjyNY2kZ44VwAsLcSqV-vm4X0PI2xA9K6cztv8Ig8R-myyluG5UteA3LhmTQ6v1oveBnFGGKpqVexBdisPvvW5XU0CrFepsZklAFeeGG8ZZwyuk2vo8iKQ7c9QLOcE5rE21tTfvnKlRv1FQDfq_wui_Asa2_eMAPaSeWlpjtx7CXx1CRK50uT-Qc3NKyUO7gkXOz5lEFgfWJ8WqhZ3jLvwrG45E9E0DyKwBRFZB11Ij8B0AlV7PbC5uOAo2dIkkfvGhOxvEU4Om3gCguf72iaGqi_PeUOJpq_Hk1a3j-O8kCltesJVMNCVRESQbkitrZXTHL59-0uQQuXPLD0OMVU1CLHZ5ABQDXphkmbFACVxB3Gg8UqsQQCrollPvvLPVFX8p1ntcwen1RabSyFKSzRnhs7GZ1Y220lLaRqAs2DgbUwE5vq6mUmjhmv6Xc3eEps78p-vAP7CIV1H6Zx2QbvID8CjbPkTGdMTRxoeeZAFQOcIDb2UMDhHFqQCVT7Rr3s93BaMpQYHg7pvlmLn7DYrH9TNXHjSYoN2W8Bs4jTWsl6yg3yp5qizxFuZusXKg2RjklH_DhQ6slxrMlRcUIsuzRJJKLXuyAGe-xXDIEvlhoDk0Tq-WLbqKSRXCu0M5mWECWbQzMUP-nw7sz0FLn7DWj0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6888c2e65.mp4?token=J5uxHPL2fwGtDk6yDtjyNY2kZ44VwAsLcSqV-vm4X0PI2xA9K6cztv8Ig8R-myyluG5UteA3LhmTQ6v1oveBnFGGKpqVexBdisPvvW5XU0CrFepsZklAFeeGG8ZZwyuk2vo8iKQ7c9QLOcE5rE21tTfvnKlRv1FQDfq_wui_Asa2_eMAPaSeWlpjtx7CXx1CRK50uT-Qc3NKyUO7gkXOz5lEFgfWJ8WqhZ3jLvwrG45E9E0DyKwBRFZB11Ij8B0AlV7PbC5uOAo2dIkkfvGhOxvEU4Om3gCguf72iaGqi_PeUOJpq_Hk1a3j-O8kCltesJVMNCVRESQbkitrZXTHL59-0uQQuXPLD0OMVU1CLHZ5ABQDXphkmbFACVxB3Gg8UqsQQCrollPvvLPVFX8p1ntcwen1RabSyFKSzRnhs7GZ1Y220lLaRqAs2DgbUwE5vq6mUmjhmv6Xc3eEps78p-vAP7CIV1H6Zx2QbvID8CjbPkTGdMTRxoeeZAFQOcIDb2UMDhHFqQCVT7Rr3s93BaMpQYHg7pvlmLn7DYrH9TNXHjSYoN2W8Bs4jTWsl6yg3yp5qizxFuZusXKg2RjklH_DhQ6slxrMlRcUIsuzRJJKLXuyAGe-xXDIEvlhoDk0Tq-WLbqKSRXCu0M5mWECWbQzMUP-nw7sz0FLn7DWj0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیاط شهیدی که سند دروغگویی منافقین است
🔹
منافقین مدتی است تلاش می‌کنند با فعالیت‌های خود در فضای مجازی و کانال‌های ماهواره‌ای، چهره‌ای جدید از این تشکیلات تروریستی ترسیم کنند.
🔹
در راستای همین پروژه آن‌ها به‌تازگی مدعی شده‌اند که «مجاهدین» هیچ‌یک از مردم عادی ایران را نکشته‌اند!
🔹
اما هزاران خانواده ایرانی، سند زنده جنایت‌های منافقین‌اند؛ خانواده‌هایی که پس از دهه‌ها، داغ عزیزانشان هنوز سرد نشده است.
🔹
شهید حاجی‌هاشم، خیاطی که در نماز جمعه تهران هدف ترور منافقین قرار گرفت، یکی از همین مردم عادی بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/459529" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317136bcd7.mp4?token=jiQG6kT1pz2E0stLsnD2caACq4Fbyc-JDxReYLy8Pa5Rw4wUcD48VIip1-AF9Qs1jkOrHSn6y1zO8PvgoUdnp4wZ1zaUhuMp7uYp-yChn81fpfD4WsE2GSYMzWpbjPwfsgJl3nHlr1ftJvwQsIIQjmqd_HEC_yEZEsUWyrPiQXHLYfYf3y1nYfii5GI9e-HpTHgT1BsKDsat4EWHdHZFhAN2SNhccaph09XQawcgZxLHuVZ-0XCgEFwgWYwKXDX54VY2GJVMa5Jx2AeKaN4Jbwaazz4ojmRTUEKfO1VC6rzEH4BjI_iXugmn1Us78l5No9BWZNr5sinYcL4WpR4I7le7VTeKC36oftCIJYeBJHAJPQnMijIGKLcbMeezM79kQFjEsVcfcBxx7odE4Tep6ROa48fyZzbq5vymR1Ecz1kYnNOb5Uz1-VcsUyaDMrnNNsjdoj47Y16WhJNIifm5tMRbRXWtP2fg5IRINjTXo3JQP0ucCxvqGGATFsAOdKrxg5yZqrnd0Ow-XGDy-xdOFyj09pYg7IhnPaUXul5N1IdFaxB_m15dMSiejUKRf0-MxlqNpCYkRQNceE4wHkdbnECF2Wcj3he9OpTv8DO4KIiIR9rfKM-OWk8NDn49E7fIJa0EcengqpFHAJdwVJM_359dJYddXErlBXYeX60-hbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317136bcd7.mp4?token=jiQG6kT1pz2E0stLsnD2caACq4Fbyc-JDxReYLy8Pa5Rw4wUcD48VIip1-AF9Qs1jkOrHSn6y1zO8PvgoUdnp4wZ1zaUhuMp7uYp-yChn81fpfD4WsE2GSYMzWpbjPwfsgJl3nHlr1ftJvwQsIIQjmqd_HEC_yEZEsUWyrPiQXHLYfYf3y1nYfii5GI9e-HpTHgT1BsKDsat4EWHdHZFhAN2SNhccaph09XQawcgZxLHuVZ-0XCgEFwgWYwKXDX54VY2GJVMa5Jx2AeKaN4Jbwaazz4ojmRTUEKfO1VC6rzEH4BjI_iXugmn1Us78l5No9BWZNr5sinYcL4WpR4I7le7VTeKC36oftCIJYeBJHAJPQnMijIGKLcbMeezM79kQFjEsVcfcBxx7odE4Tep6ROa48fyZzbq5vymR1Ecz1kYnNOb5Uz1-VcsUyaDMrnNNsjdoj47Y16WhJNIifm5tMRbRXWtP2fg5IRINjTXo3JQP0ucCxvqGGATFsAOdKrxg5yZqrnd0Ow-XGDy-xdOFyj09pYg7IhnPaUXul5N1IdFaxB_m15dMSiejUKRf0-MxlqNpCYkRQNceE4wHkdbnECF2Wcj3he9OpTv8DO4KIiIR9rfKM-OWk8NDn49E7fIJa0EcengqpFHAJdwVJM_359dJYddXErlBXYeX60-hbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع مردم انقلابی بندرعباس در شب ۱۸۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459528" target="_blank">📅 21:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d871010fbb.mp4?token=ljKh09rfqUEztgLOY46uTTP1_G2BEhSYBFgE0RsXhdGcDvINufWM3n5CKsQnwU0op-YlCik87QQcSJpIs5AXS_tFHtELcdMsc138mkSXMGr67rylveQRk1jPPA1f3lxpVLCDK-hDjy8X0axteSDenRrbQAlSCYIpaKJ0adJHJPnwZVl2NHWaG_lWbKXZJvVOtKn2JVkQ4SnnSTdZMgUpmv4q35QVYlr-Z-42gUo-KMrWImYrseA_a9boibuHf4Wb-OEzx5K9c9cMxzPFHixreINuZFZviAqMPzBKFWyUCLAVbbf5EO8b06KIeqPzM8ye1G9pxi0GIF1yjjoZR4zhJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d871010fbb.mp4?token=ljKh09rfqUEztgLOY46uTTP1_G2BEhSYBFgE0RsXhdGcDvINufWM3n5CKsQnwU0op-YlCik87QQcSJpIs5AXS_tFHtELcdMsc138mkSXMGr67rylveQRk1jPPA1f3lxpVLCDK-hDjy8X0axteSDenRrbQAlSCYIpaKJ0adJHJPnwZVl2NHWaG_lWbKXZJvVOtKn2JVkQ4SnnSTdZMgUpmv4q35QVYlr-Z-42gUo-KMrWImYrseA_a9boibuHf4Wb-OEzx5K9c9cMxzPFHixreINuZFZviAqMPzBKFWyUCLAVbbf5EO8b06KIeqPzM8ye1G9pxi0GIF1yjjoZR4zhJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر آنچه امشب در هرمزگان گذشت
🔹
اژدهایی، خبرنگار: در حملات امشب تاکنون کسی آسیب ندیده و زیرساخت‌ها نیز سالم هستند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459527" target="_blank">📅 21:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459524">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi1mP8QUBpOiQf45EXW5oaTL6cpoL-0iwxEumBoG64v-OiLyYNKQvJ1QVxfrBONdzbrqEkeGBd2mDVr2zyhVFe1f9FQaQp5G5vLo-2BcSKDzYbnzAeUGt3wnZurIQmX0Y56KtSkw-T2i2-YzFKRsRnJh2NOArW3u0LVXKkv9_WhJkaZsnIff590PeSPkAwg7_hudI46IpRkfWU_Yb9J5YkcbGTyVMPo9hIS-w3s9smmwbvU3cCqAMMhHCaffR9-Wz2z_mGNeNuQYJB6s9O98p-k0ClzrEsrLUEpaJ4c4SCIp3q3qv--AzhTAG9RPxN4xREqYG1mRyzZ87Ul7Mg3S0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد کل نیروهای مسلح
:
هزینۀ سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔹
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا: در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان‌وبلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده‌ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
🔹
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
🔹
بارها اعلام نموده‌ایم و اراده کرده‌ایم که تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه‌های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/459524" target="_blank">📅 21:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459523">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoEysM59kNH_-SxUl8ymUoHwJvEBpVSP27XHtSoc0gtoHb-ZPyTrMjyObcTQleCXIM89RL1GIjKjwCt-vHReRxv6C9C73q_xLNvLpv8fLd9X4wxwRDoKYVcgqw9tExB1uFF6kwcxwTsKG06y1b5gF_cTViPFa39Z3Fa-8EvShZwMDcTs-MgqXNnPatGd5soDH-UA5jk1rkpnHtuH7g5MgyDDnmuxPR20ihHJvIHU0KT_OV748tBx7G21C6cnoyQsmWW306BF9CdSiEqA9ICAiqI2HT_JJYAuEc1mtqFUi0ShrV8-mgALRyBrbYGIbFtSe-UEMCLJnAyzZsqyrUlGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی سپاه: تنبیه سختی در انتظار متجاوزان است
🔸
آمریکا از حملات جدید خود پشیمان خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/459523" target="_blank">📅 21:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459522">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
سازمان تروریستی سنتکام اعلام کرد به اهدافی در ایران حمله کرده است. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459522" target="_blank">📅 21:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459521">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYIUJEaWi9svgAabqjLBKzYz3XPj9CJBOuT3Fg6IvoX2UBrYGFX_gB_PHT2kqYTRJ3A8hyJvPH5yxD8ou7rU0kwR-lxYrklOzW0ukVw95-vmXz-Chvr76UKjAAGSaKpENxnO_jWpnd834i0LmaKy1L9n-dlneRSWiP-Vl8BLiMR-5TlLl7Yg5FQw8ER8Rzn6FtO9NDtSR-3QLMQz09q9m9NGgR2CQWWOCU1r8nFY6IN6CzX9PY3phhMRlfi8H9cR1mWnk6gIqdpwudFHDqNet4d80k8j2QtNr_mEN5AgFtZRVenUreHPbfxFxUb2ntZ_NnBsM4eclQpuMOVozwwj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سفارت آمریکا در قطر: آمریکایی‌های حاضر در خاورمیانه نسبت به خطرات آماده باشند
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459521" target="_blank">📅 21:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459520">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ca5b4f63.mp4?token=mYPewlBuEzTemUqOI2eXCWJO33Zcchb_CrPWNvO9mC-5yeKtDKKZKYLny4Qi9fe8ICDwiH-xVSNcnfn9E0xTuU-yKHBeecqbgUdPOHR9Lf0Nr_5CgzOowMnGPy2gTbp51-7BMVbIGhe7EQmb1MYXKfBPMauf1WGvciagu0jt_ZFFmcTGvCnTZM2A5AC3aQYE8JdoN3K4D4bThWuEkY0S_gDywXk1AqR5DRiv2ZylUV9HoTRk-mES4CaAxfr672ArIvKTSDka-abKJHQb7dmr5X5Hv0jJm1i6PKLH8ibjvp-hqcfsKrUffEsVd3PjlMK1itvP-mWgM219AaEus7_OQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ca5b4f63.mp4?token=mYPewlBuEzTemUqOI2eXCWJO33Zcchb_CrPWNvO9mC-5yeKtDKKZKYLny4Qi9fe8ICDwiH-xVSNcnfn9E0xTuU-yKHBeecqbgUdPOHR9Lf0Nr_5CgzOowMnGPy2gTbp51-7BMVbIGhe7EQmb1MYXKfBPMauf1WGvciagu0jt_ZFFmcTGvCnTZM2A5AC3aQYE8JdoN3K4D4bThWuEkY0S_gDywXk1AqR5DRiv2ZylUV9HoTRk-mES4CaAxfr672ArIvKTSDka-abKJHQb7dmr5X5Hv0jJm1i6PKLH8ibjvp-hqcfsKrUffEsVd3PjlMK1itvP-mWgM219AaEus7_OQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل توانیر: تا اواسط شهریور حتما خاموشی‌ها تمام خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459520" target="_blank">📅 20:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459519">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9bd0f58f0.mp4?token=Fk-Edc5XkvI86JWgY1V3vw1-5LEoqha2dAOCw4j4sedCGBAIbAA1RaJakuGw2OdGCU7saYCHVOlshXRKAYxQNRPxiCgyRQMl0nwSlArJy3nfUCVF8ifjfXNIg9N4uQ9v7fYqzHZJ5CF4oTnTaVn7URL-3gm2QGN3VYqU4J8iufowbn5O97YGge-CtRCQqJRHNojm75neVsY1IfC4FP1ObKGGMCLd7zDtHZBWFMsa9E69HuDSpo8ElsCkHqxrWBNkHaL3emM-Q2az1B7N9-OS4yw0GfNpUdT9BeHNaWDlVlp-XauR5mci65YSv46P5jnOm5ATa53-YGq2twJcY28MyVR9PNMo7RzFobU35Zhy9HZs6hz1e4aBkVJahImpXawWGEjWP5-qcLaXnOVFLeqD7dTRHPaOX6EbCd7EYrAg09j0H8I162N9vV_kf9E4RQn7lWjXrOI8iMUisqGiO1GFhYGYcvYdjFltPZWUfgpapvNgUdsSvhBLvdO6ZEETA5ZVXvQkoR1p4azm3bZChbWu31kVc3XXfHLeDEjQra-Ore7Bu-lVJRUOU_-QsXfpUFNyhaJ2EwFZpskou-Q-JemMdH_1yKOw1SxxpPT-mNFsdowimI0je5rxsOry6zXm_tqKB5KhU3MZqN3d8GVqEF_G4lBoToTAX6Z1szdmREfXAf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9bd0f58f0.mp4?token=Fk-Edc5XkvI86JWgY1V3vw1-5LEoqha2dAOCw4j4sedCGBAIbAA1RaJakuGw2OdGCU7saYCHVOlshXRKAYxQNRPxiCgyRQMl0nwSlArJy3nfUCVF8ifjfXNIg9N4uQ9v7fYqzHZJ5CF4oTnTaVn7URL-3gm2QGN3VYqU4J8iufowbn5O97YGge-CtRCQqJRHNojm75neVsY1IfC4FP1ObKGGMCLd7zDtHZBWFMsa9E69HuDSpo8ElsCkHqxrWBNkHaL3emM-Q2az1B7N9-OS4yw0GfNpUdT9BeHNaWDlVlp-XauR5mci65YSv46P5jnOm5ATa53-YGq2twJcY28MyVR9PNMo7RzFobU35Zhy9HZs6hz1e4aBkVJahImpXawWGEjWP5-qcLaXnOVFLeqD7dTRHPaOX6EbCd7EYrAg09j0H8I162N9vV_kf9E4RQn7lWjXrOI8iMUisqGiO1GFhYGYcvYdjFltPZWUfgpapvNgUdsSvhBLvdO6ZEETA5ZVXvQkoR1p4azm3bZChbWu31kVc3XXfHLeDEjQra-Ore7Bu-lVJRUOU_-QsXfpUFNyhaJ2EwFZpskou-Q-JemMdH_1yKOw1SxxpPT-mNFsdowimI0je5rxsOry6zXm_tqKB5KhU3MZqN3d8GVqEF_G4lBoToTAX6Z1szdmREfXAf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌هایی که هرشب به رنگ ایران درمی‌آیند
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/459519" target="_blank">📅 20:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459518">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bb4d009a.mp4?token=EKHX2o_L5imOCV2vpVafSU5TtAmhvdz8ghDpr026qNos-E6SXFrlhvsWkZrqMyV3LBF1n9EXbRdB_l_gl1JB1xHmQIMDVKEEqGXDD1aXfr79jZq8g7u_oYpEbQ1erhp_ysEnrBEkgyILm2NcxUSY2KmCb8cNk0tePRYkIcVOv8TeOfszT4HGv4IkyZt_ldwD3Nq0ud62XTjlWlqePeNep3aI_EK6YjPk--UJI_Yd3rWXaqOw7mimAzGcSCMOEir04_g2US3xetI2_7fBFr09J2n4V0wh8tXNOOOV0vOGslN5LhEduIwgC41NY6LAiiTHNES70a2jXBqQstci0RiXXDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bb4d009a.mp4?token=EKHX2o_L5imOCV2vpVafSU5TtAmhvdz8ghDpr026qNos-E6SXFrlhvsWkZrqMyV3LBF1n9EXbRdB_l_gl1JB1xHmQIMDVKEEqGXDD1aXfr79jZq8g7u_oYpEbQ1erhp_ysEnrBEkgyILm2NcxUSY2KmCb8cNk0tePRYkIcVOv8TeOfszT4HGv4IkyZt_ldwD3Nq0ud62XTjlWlqePeNep3aI_EK6YjPk--UJI_Yd3rWXaqOw7mimAzGcSCMOEir04_g2US3xetI2_7fBFr09J2n4V0wh8tXNOOOV0vOGslN5LhEduIwgC41NY6LAiiTHNES70a2jXBqQstci0RiXXDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهداف مورد اصابت در نبرد هرمز؛ چه نقاطی زده شدند؟
🔸
نخستین تصاویر هوایی از هواگردهای منهدم شدهٔ آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459518" target="_blank">📅 20:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459517">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4e101624.mp4?token=mgVkFZs8DSxdefAfl_YTTJEGOqG6MwV02hSIQzIfMPq2nSltGjmHGtSp16JVWjHXetHIW9ilJRPp1fG9xQavrXn9C9DHNZpcr9QKbaUyM8ZpTdhGyHOaohh9UaXyovN_WGGvcGMBNUgiTRmxYFw1Vol9Ad287rsq18v3mhdGkFXioD5WSNLgjfqJR1cMT2Y5iLl3s2wS-qmYheOiX0w8QQMomO7TJJiQ1Qz9a0drUr7DJFrOSwcM80-21pFpYYiwJQZDyTQee7ph9zGUcyQ-txHaqMpNMFRpBqNapgOOgQ7woXvT5V2KaRlQGtwphsRhDr1gijT3Ol7AiHQDAQFpwG9zFiUDz9NSQbOjZQOyG1DOnN530iDmNm_iQ-mOh9Eru-_xCewM_e2GTjHqPIxWFrY_KMuASqZ8DjUvs9Hn6dBxq5S2G7GhqreMNSzQZnCBQ_55PbwlXRv4XoH-VApFH0Iuh-t8HDR2jGPLNMtq8E1Ryh8R8DxJabf0YqhUBaoV6D9pmt0MTnep9BynkMt-bL9RkbatlXU-AcBM-HzCJc9rjjthCRZ-GgUErRR6SZ5-pLxR1C3vLRbSfWL87ph_74fmqI9ApoIIThPWKafA3UQhKSE4uKExyUt2cltEnqgrvdBpmRFAkFiIxEWhJFFfmEV0dfV6l6-8X7sjEpzjWBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4e101624.mp4?token=mgVkFZs8DSxdefAfl_YTTJEGOqG6MwV02hSIQzIfMPq2nSltGjmHGtSp16JVWjHXetHIW9ilJRPp1fG9xQavrXn9C9DHNZpcr9QKbaUyM8ZpTdhGyHOaohh9UaXyovN_WGGvcGMBNUgiTRmxYFw1Vol9Ad287rsq18v3mhdGkFXioD5WSNLgjfqJR1cMT2Y5iLl3s2wS-qmYheOiX0w8QQMomO7TJJiQ1Qz9a0drUr7DJFrOSwcM80-21pFpYYiwJQZDyTQee7ph9zGUcyQ-txHaqMpNMFRpBqNapgOOgQ7woXvT5V2KaRlQGtwphsRhDr1gijT3Ol7AiHQDAQFpwG9zFiUDz9NSQbOjZQOyG1DOnN530iDmNm_iQ-mOh9Eru-_xCewM_e2GTjHqPIxWFrY_KMuASqZ8DjUvs9Hn6dBxq5S2G7GhqreMNSzQZnCBQ_55PbwlXRv4XoH-VApFH0Iuh-t8HDR2jGPLNMtq8E1Ryh8R8DxJabf0YqhUBaoV6D9pmt0MTnep9BynkMt-bL9RkbatlXU-AcBM-HzCJc9rjjthCRZ-GgUErRR6SZ5-pLxR1C3vLRbSfWL87ph_74fmqI9ApoIIThPWKafA3UQhKSE4uKExyUt2cltEnqgrvdBpmRFAkFiIxEWhJFFfmEV0dfV6l6-8X7sjEpzjWBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌چه در سفر پزشکیان به قرقیزستان گذشت
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459517" target="_blank">📅 20:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr46aAa6MWHcnFZqe4nluTjP_qIxU286hEDANGCk8ccnzQXqcoPlc0fSdGRe6fJK7CYuhBTPYMIfHqfVyekuw-qabfO356GSRqyM03vnSdxSvoU487b3CymvzM89xeffPLgAcMHT3kjZlkd95pvLDM2nSR9TkTsLs4gs15Iz46ibUDLR3ME3B6fjOXGxUho1pmhlbeLH5OzWzdLmFojBjUGmxts0cu1-YXqF4DvaWCC7PdIEAZWUxsPISPg5yZjtngkSDCABO4O25UgxEHPHPolUHI6vq9f7aDAgw1C-vaYjQt0WbxE-13LbilXpfToF4ipaNOB9N0x_qA9CeamJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پوستر فدراسیون فوتبال برای شهرآورد فردا با استفاده از هوش‌مصنوعی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459514" target="_blank">📅 20:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618cba8f6d.mp4?token=uGQYsVZ37f3R9x_oFmr5GbBx67n8WPiZvNifwbsAMUVtpBvJLAj5-3_yq4XAbdvKjXlErKyPXJVouLic7FCHBcmk_wJKaL2G5bysAm8y3YtwYFSs1jtEFAsIA16bPmsIBoUOXaFH0wGM4AFSXatRNv3slhuYV44UiP1bDZqvsoAUBm3sI67q0gBCddyoetpKBrKFSGMF83AKztLAHyKoredHgOdQNKyyCSMQPYzgLIV9po5bobOwfkzO37w-vJI0f0wTvV0netfC4fmbM_Ot1q2oX8Kr5RULv3g8hWEMJBye2TQHidOReMR3fP4prtNjemBuEhY6xwxfHEdHyHS8fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618cba8f6d.mp4?token=uGQYsVZ37f3R9x_oFmr5GbBx67n8WPiZvNifwbsAMUVtpBvJLAj5-3_yq4XAbdvKjXlErKyPXJVouLic7FCHBcmk_wJKaL2G5bysAm8y3YtwYFSs1jtEFAsIA16bPmsIBoUOXaFH0wGM4AFSXatRNv3slhuYV44UiP1bDZqvsoAUBm3sI67q0gBCddyoetpKBrKFSGMF83AKztLAHyKoredHgOdQNKyyCSMQPYzgLIV9po5bobOwfkzO37w-vJI0f0wTvV0netfC4fmbM_Ot1q2oX8Kr5RULv3g8hWEMJBye2TQHidOReMR3fP4prtNjemBuEhY6xwxfHEdHyHS8fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلایی که ترامپ از آن می‌ترسید، سرش آمد
🔹
جیمی کارتر، رئیس‌جمهور ۴ دهه پیش آمریکا بود که ترامپ با تمسخر ضعف‌هایش، برای خود در انتخابات رای می‌خرید و می‌گفت که نمی‌خواهد شبیه او باشد. دو ضعف بزرگ کارتر که در تاریخ آمریکا از آن یاد می‌شود، عبارت‌اند از: «شکست…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459513" target="_blank">📅 20:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">طرح تعطیلی پنجشنبه‌ها به صحن مجلس بازمی‌گردد
🔹
جعفری‌آذر، نمایندۀ تبریز: اصلاحیۀ کاهش ساعت کار هفتگی به ۴۲.۵ ساعت و تعطیلی پنجشنبه‌ها با رفع ابهامات در کمیسیون اجتماعی، برای رأی‌گیری به صحن علنی مجلس بازمی‌گردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459512" target="_blank">📅 20:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNUoQzBq8zf9vY17UUwWoVtnR7FAGRwQ8QpCjfnYoCd8L6EsS9Af2aZ0OZuL98YLlvLF_yOn8SnollM-OU2fhEFFGB2i_-kgR6DRhCd0J01zJ5q3fvg_KzOv3uAXft1ZthgV_1O-dpY0UilYrDnLC5RKMFH-ylrN_WGQ_I391O18O750qaNCkdyG0ca6L5IXXG4A-hRoEiEinK-ItA_3XWY1ZeyAF4AO6u43YTD2iTfUwRPTkM91AXSctfLpRjnOmYbrjPE0jNivwUrvFFnNca7JTMyb-dZYLSOBLp_FPiZyqhT5DlfyL05X2kezx2SR7gDd3YtZaMBDsYxd4GTqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ خرابکارانه در نیروگاه آلمانی
🔹
یک تأسیسات مهم انتقال برق در نزدیکی نیروگاه زغال‌سنگی «ژانش‌والده» در جنوب ایالت براندنبورگ آلمان، امروز هدف یک حملهٔ خرابکارانه قرار گرفت.
🔹
در همین حال، گزارش یک روزنامه آلمانی از منابع امنیتی و صنعتی حاکی است که تأسیسات مذکور چند بار هدف قرار گرفته و مهاجمان از سازه‌هایی شبیه راکت‌های دست‌ساز حامل مواد منفجره استفاده کرده‌اند.
🔹
حمله‌ای که به گفتهٔ منابع رسانه‌ای و امنیتی، هدف آن ایجاد اختلال در شبکهٔ برق و احتمالاً رقم‌زدن یک خاموشی گسترده در منطقه بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/459511" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
شنیده‌شدن صدای انفجار در مناطقی از بندرعباس، سیریک و قشم
🔹
هنوز محل دقیق و منشا انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459510" target="_blank">📅 20:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459509">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhILu41FzcNrK5rgFb_2BqF8LeuW3p7wc6Yk8ibbcf8YTjE7mSxH6Bty2HJSym6Bm1o2N-7KY0NEefvh0t7oPFOQGk--cPDK_R8TvHJmF_Qic4vvL08dIgvhf3vmgbwKS0e5lXuneQf2OpAGJPmZ6h_nMMOTMe2esCsuwNITSx3QK1KQEAgU-Gq0ENSaiWa4vTjmZnNFIUo3MH2uffj-oBixdBAxawSFiSkGnZRP1U7vQi9uGdbBQK6833NXn5Ex5TtHyvElZQlxWLs5i4tx2gCzsc-DSmyfrwwUbWUeko84kF8FbTnwgMWBrJ2wTg-oxhL2lSBKqdzxZJPAT__uLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قیمت نفت از ۹۴ دلار عبور کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/459509" target="_blank">📅 20:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
شنیده‌شدن صدای انفجار در کنارک و چابهار
🔹
دقایقی قبل مردم در کنارک و چابهار صدای چند انفجار شنیدند.
📝
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/459508" target="_blank">📅 20:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
معاون استاندار هرمزگان: تا این لحظه هیچ‌گونه اصابتی در استان هرمزگان تایید نشده است.
🔸
از دقایقی پیش برخی رسانه‌ها از شنیده‌شدن صدای انفجار در نقاطی از استان هرمزگان خبر داده‎‌اند. @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/459507" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb0V2M7JGGAF98ii4lH4fAvY0V1Qu8iJr6t36OQ7tSu6TRYos2nX3igDdo8AKiLHSRXIvGlj0DbAi8Q4LAIrHpIJ-sY8hZ2MAewQBSvGI8HP6QP7AmHtLMtt8f2R5w270_kPS5nZ59e-dqywa-amjqAr2_0vrHONChLV0JXWaAJeqYP74qHsANBWi_DIdS3cfB5VfwD7tByl576_Suo5fPIZniGNHbuJoakPuRGgKhQcebB-Ky-4J9MU1x9YcXFwh7GwotIAkl4h0AE8fxyzDYidAR0LlGl5WO7m_cObdEMK5_hklL99jTTfG_FmdmAzO-SDfW3V-9WyX8T4s3hBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرایی اصرار حزب‌الله به حفظ یک تپه
🔹
فشارها برای خروج حزب‌الله از ارتفاعات علی‌الطاهر افزایش یافته است؛ اما این جنبش معتقد است تحویل این موضع به ارتش لبنان، به الگویی تبدیل خواهد شد که ممکن است کل جنوب لبنان را تحت کنترل اسرائیل درآورد.
🔹
حزب‌الله براین‌باور است که اگر قرار باشد علی‌الطاهر در نهایت از دست برود، این اتفاق نباید با یک عقب‌نشینی داوطلبانه رخ دهد. از نگاه این گروه، اگر نیروهایش بدون دریافت تضمین‌های مشخص از منطقه خارج شوند، اسرائیل نه‌تنها از تهدیدهای خود دست نخواهد کشید، بلکه احتمالاً آن را به‌عنوان یک روش موفق برای رسیدن به اهدافش در مناطق دیگر نیز تکرار خواهد کرد.
🔹
تحرکات نظامی اسرائیل در جنوب لبنان نیز این نگرانی را تقویت کرده است. از نگاه حزب‌الله، هدف اسرائیل صرفاً از بین بردن یک «تهدید محلی» در علی الطاهر نیست، و حزب‌الله معتقد است اسرائیل به دنبال ایجاد یک مسیر عملیاتی به سمت نبطیه، اقلیم التفاح و منطقه جبل الریحان است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/459506" target="_blank">📅 19:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
معاون استاندار هرمزگان: تا این لحظه هیچ‌گونه اصابتی در استان هرمزگان تایید نشده است
.
🔸
از دقایقی پیش برخی رسانه‌ها از شنیده‌شدن صدای انفجار در نقاطی از استان هرمزگان خبر داده‎‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459505" target="_blank">📅 19:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51eaa49907.mp4?token=es7ZqPWCLxsVQdkPCYsdxKbcSkglh-UBMtQGDnmDCXBUZYrQO7EiErtiGdwUWiSYXcjiwYxOVpkfav60gIhYlP5iIo5JapK5HmGh22DTw__U4Co5sFbGOxzMLcpdGu1SVhP6Ey3QNbvXvIOAkpC64Cq3F4ZhGCJitXb9kUj3RN16KWJM1T9SL1xf5E4l0zhBJd6Q4fHfELi7M8gcx5gMofYyoXa1D_06jznrymTtmSqwm4m8LHhgx73xHS0yRlLmIumOrFrN9rEIz3bgKS2Wht-OBYzxdu49Ctsy__VROHsmRW0zoxMYkizq0BWqk1QcduTeKG_L9xtYYCuzisr5aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51eaa49907.mp4?token=es7ZqPWCLxsVQdkPCYsdxKbcSkglh-UBMtQGDnmDCXBUZYrQO7EiErtiGdwUWiSYXcjiwYxOVpkfav60gIhYlP5iIo5JapK5HmGh22DTw__U4Co5sFbGOxzMLcpdGu1SVhP6Ey3QNbvXvIOAkpC64Cq3F4ZhGCJitXb9kUj3RN16KWJM1T9SL1xf5E4l0zhBJd6Q4fHfELi7M8gcx5gMofYyoXa1D_06jznrymTtmSqwm4m8LHhgx73xHS0yRlLmIumOrFrN9rEIz3bgKS2Wht-OBYzxdu49Ctsy__VROHsmRW0zoxMYkizq0BWqk1QcduTeKG_L9xtYYCuzisr5aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعد از شهادت فهمیدیم نخبهٔ موشکی است
🔸
گفتگویی با خانواده شهید عرفان کشاورز کیا از نخبگان هوافضا و شهدای جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459504" target="_blank">📅 19:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNqW04PObfo6dLuGssxyEk4iKc4l5Oud--7nJEBhbHY4frUvpPswplH_6tQDGwt8n7xs2m2I6RRPqjeIn5v0JBwHJq2G8sBR0ylL-pXMibuIZTgOXPkPgTCN1ZGd_HkJ5PSDLGjJZodRCkVg2g_ZPqDUJPVvomrCa-KXrZmURLjveMU1k3wOX-tENEFrcjyMaepBT_5xRdC50MpYOOmUwrw4KXryg-RSNs_eNSkZDbLxPI1pTdW_r_90ztZ9QSHp96JEjtnffCCSNajJghMQ4Elcezb_BYPreac0dyEiVBS_GmDPsn5cx7RBRiXZomglKF6yChZyVNLbflm2JXompg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک‌های برنامه جهانی غذا به کرانه باختری، نصف شد
🔹
برنامه جهانی غذا وابسته به سازمان ملل هشدار داد که کاهش بودجه، این سازمان را مجبور کرده تا تعداد افرادی که در کرانه باختری به آنها کمک می‌کند را از ۴۰۰ هزار به ۲۰۰ هزار نفر کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/459503" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4726a8e5c.mp4?token=kj-5k8CjNQbCtCwwkVuvkvBWro_OsfNMqGazvgOl0jc4UkTeoXxX-Fd7KCJHyIIFiACIIQlvFY7Z6-UWVUInxrzpSc1WdTr3urVDOU69oSoZkRsIL0n2aACpRpxTus8k1C3eVeAkLOEMSlbxdOe4VcBnttCEur6PjSBVp9F60WSf4H7cXAJ_wNBXn0QUnGlygZBfNkmfKWBOLQmVIybkf2vIyb45Gtz1v91hV9xRUTH-PRG3tll5bCpsvZ_-KT9-9AKotr_W2okzettpVBH5IcBVdLVp5kOtDWQDPzy19MYzmbtOSGIO2x7qP5BvMz6gQzsbx9NCzGf7dC0RSG5Asw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4726a8e5c.mp4?token=kj-5k8CjNQbCtCwwkVuvkvBWro_OsfNMqGazvgOl0jc4UkTeoXxX-Fd7KCJHyIIFiACIIQlvFY7Z6-UWVUInxrzpSc1WdTr3urVDOU69oSoZkRsIL0n2aACpRpxTus8k1C3eVeAkLOEMSlbxdOe4VcBnttCEur6PjSBVp9F60WSf4H7cXAJ_wNBXn0QUnGlygZBfNkmfKWBOLQmVIybkf2vIyb45Gtz1v91hV9xRUTH-PRG3tll5bCpsvZ_-KT9-9AKotr_W2okzettpVBH5IcBVdLVp5kOtDWQDPzy19MYzmbtOSGIO2x7qP5BvMz6gQzsbx9NCzGf7dC0RSG5Asw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: علی‌رغم فشارهای آمریکا، تمایل کشورهای شانگهای به همکاری اقتصادی با ایران قوی است
🔹
راه‌حل تفاهم اسلام‌آباد ساده است؛ آمریکا باید به تعهدات امضاشده بازگردد تا ایران نیز تعهدات خود را اجرا کند؛ ما پیش از آن اقدامی انجام نمی‌دهیم.   @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/459502" target="_blank">📅 19:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459500">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e51ad29841.mp4?token=lXAnoillbcxRT1zTCEcgYEMfo7vO75G-mU-BA-z4j9xCwlxYRPDz73_bqEoxO6Tfx-YBdb3mtKEnEmF25qug4TnnVjECNqUlQ6j5Z3LyuM7DVqqGqoXnaZKpb3GCWz-FAbTuImZ4qJpshKeoyHH1HKmZCz5TaKAKi1g_8Tc0ZEgpj9icKuyLVoVAKh1u4sxwkog6Oq35NPT5k5s7T6Mv8zo87hEiZ8wVz6TCp3OorYzlQvsA4UQB5QD0OPQI_kOaaPMesyU8Fg5JxI0TWljHaHuj2oNLe7urPBPWNMWz6g_29B3ePoWnztBRa6_ccNj8N5Dybc47eUSaSmHKMCPt4lnl_OUsih9VVgmcKj_TJi4zZE2owmDzCWxb-ljJu2abCRaFZqrx4Ajc72pnniAuwWbSdGPKk9t9tO8v7LUFsJYEXSUkpPhmVeyn3c_GPLV2H64Duer-A75KL7t8wu-ZXnyYzui0DtzpKTO3PMi_1f6WbE_ARz8hW4B375z0pGTRBr7xq_4lp9HdtrYLA3QHcK39lPp4NsY6zGptUL64TDClT_FHsOQdJ39lzb5P5S7z7adk75J23LUoc_JdY62AISFNOaumyqrq0hxfJSf6UVSkoX8DcbqiaDVcPmxtqybZnkrdjhDhai_0omVnq9Wdol6GXc-KJXqhSjaVGYBSeTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e51ad29841.mp4?token=lXAnoillbcxRT1zTCEcgYEMfo7vO75G-mU-BA-z4j9xCwlxYRPDz73_bqEoxO6Tfx-YBdb3mtKEnEmF25qug4TnnVjECNqUlQ6j5Z3LyuM7DVqqGqoXnaZKpb3GCWz-FAbTuImZ4qJpshKeoyHH1HKmZCz5TaKAKi1g_8Tc0ZEgpj9icKuyLVoVAKh1u4sxwkog6Oq35NPT5k5s7T6Mv8zo87hEiZ8wVz6TCp3OorYzlQvsA4UQB5QD0OPQI_kOaaPMesyU8Fg5JxI0TWljHaHuj2oNLe7urPBPWNMWz6g_29B3ePoWnztBRa6_ccNj8N5Dybc47eUSaSmHKMCPt4lnl_OUsih9VVgmcKj_TJi4zZE2owmDzCWxb-ljJu2abCRaFZqrx4Ajc72pnniAuwWbSdGPKk9t9tO8v7LUFsJYEXSUkpPhmVeyn3c_GPLV2H64Duer-A75KL7t8wu-ZXnyYzui0DtzpKTO3PMi_1f6WbE_ARz8hW4B375z0pGTRBr7xq_4lp9HdtrYLA3QHcK39lPp4NsY6zGptUL64TDClT_FHsOQdJ39lzb5P5S7z7adk75J23LUoc_JdY62AISFNOaumyqrq0hxfJSf6UVSkoX8DcbqiaDVcPmxtqybZnkrdjhDhai_0omVnq9Wdol6GXc-KJXqhSjaVGYBSeTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در دیدار با گوترش: سازمان ملل باید در قبال تحولات بین‌المللی نقش‌آفرینی مؤثرتر و کارآمدتری داشته باشد  @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/459500" target="_blank">📅 19:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459499">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f83a10d37.mp4?token=T-K2Dc8PSVBEneByghjZF70znMmjwW3hW8MNKnSR1vRRlbnZxB9UigzsrdXKB7LKHJfaoni7tW8zIyAuumNpyuHUWp4IJRdl7TKfvGD-lrrShf2K8xUXKodYLDX_XIFVL6HSaIxtFeZeoZPKbztXs68NRQ9ZC7tUIqz99VmasxkjG7ksS-484WheWIiXwG36nBG3csQl6CfANNJBUbH3QS0GJyS6YPnzL5Gkt3vC2HcxWfrDoU_dzjzhCyqboNfQHrk4_rQg5rrTx_XKBlgXDp0aExXrncZ4HPKGTQbeWZCR3zcRvLWoEpNK1EzoEMVJTSrPZWvkowLss0NJ9RLtyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f83a10d37.mp4?token=T-K2Dc8PSVBEneByghjZF70znMmjwW3hW8MNKnSR1vRRlbnZxB9UigzsrdXKB7LKHJfaoni7tW8zIyAuumNpyuHUWp4IJRdl7TKfvGD-lrrShf2K8xUXKodYLDX_XIFVL6HSaIxtFeZeoZPKbztXs68NRQ9ZC7tUIqz99VmasxkjG7ksS-484WheWIiXwG36nBG3csQl6CfANNJBUbH3QS0GJyS6YPnzL5Gkt3vC2HcxWfrDoU_dzjzhCyqboNfQHrk4_rQg5rrTx_XKBlgXDp0aExXrncZ4HPKGTQbeWZCR3zcRvLWoEpNK1EzoEMVJTSrPZWvkowLss0NJ9RLtyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در جلسات شانگهای و شانگهای پلاس، بر مقابله با یک‌جانبه‌گرایی غرب تأکید شد  @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/459499" target="_blank">📅 19:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459498">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f99fd37fd.mp4?token=unBqQc0nhGvUvpzTMeoy429yDJXodRkuSlLhJ9-FNSauurBBCl8RCCHLb47ZxdKlTV6uOPQTW3bIy8IlC_YoLnRu4KFSrHBCIS1Xzsen9vFZJOM58xyOQLu_VqmyGjI3ebwa2OMjHwUAES19UJ2YyAugeQvNEAqMcG10qU2P87Qem_yesjq2GhBY0m1vD6MGStvFOJfJUYqbq9ByRhAQehD_wySWfBECC6zt0jcQsYspO3P4T8qUfmf4cIYF7ciFYW6S-bnqg46wQTqISNq3PuAv1KHmLezrbvt4qMQwM4bupIVkRW37njUIiZGhr12s2FOJZE9oSmU47vRw4x7Qmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f99fd37fd.mp4?token=unBqQc0nhGvUvpzTMeoy429yDJXodRkuSlLhJ9-FNSauurBBCl8RCCHLb47ZxdKlTV6uOPQTW3bIy8IlC_YoLnRu4KFSrHBCIS1Xzsen9vFZJOM58xyOQLu_VqmyGjI3ebwa2OMjHwUAES19UJ2YyAugeQvNEAqMcG10qU2P87Qem_yesjq2GhBY0m1vD6MGStvFOJfJUYqbq9ByRhAQehD_wySWfBECC6zt0jcQsYspO3P4T8qUfmf4cIYF7ciFYW6S-bnqg46wQTqISNq3PuAv1KHmLezrbvt4qMQwM4bupIVkRW37njUIiZGhr12s2FOJZE9oSmU47vRw4x7Qmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در جلسات شانگهای و شانگهای پلاس، بر مقابله با یک‌جانبه‌گرایی غرب تأکید شد
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/459498" target="_blank">📅 19:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459497">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdq7llibEPMUmrB3WMcTv4XOI07geEC4eHzpBqYcQiBPjgG_WwUnYTEmNR4OLgjXD5HENYZFzHnH4mML3_ss99PN8ZOhh4y99mZBCPAkDARo5ko4dmmm_1vMC-hqvdaI9gs0UW0N3DH_1YFE0uNHCjE7uvrFL6_MpYhw8Mw4wDNVUk6nPP2bj12QKRbrS_xswnxUhb3me0S_VScAPUXtWepwqO14SZzzx9CPDzorKf5nuYKwolgwYIzszAwiSz37q2uRoCzR7QQ8DXiHSUFP4FDg6GDBUZ_HyL4vMJQ0sJpacvFANa8HPXqS3FpcKkyZsE4KIZN7dR563ylrnlTf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار از پرچم سعودی در تنگهٔ هرمز
🔹
براساس اطلاعات ناوبری دریایی، دست‌کم ۱۰ نفتکش با پرچم عربستان سعودی، پرچم خود را به لیبریا تغییر داده و همزمان نام این کشتی‌ها نیز تغییر کرده است.
🔹
بر اساس این گزارش، این نفتکش‌ها در نزدیکی خورفکان در امارات متوقف شده‌اند و احتمالا در انتظار فرصت مناسب برای حرکت به سمت خلیج فارس و عبور از تنگهٔ هرمز هستند.
🔸
شب گذشته یک نفتکش عربستانی حین گذر از تنگهٔ هرمز هدف ۳ پرتابه قرار گرفت و منفجر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/459497" target="_blank">📅 19:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459496">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c7c15031.mp4?token=C4GFOqQ6PkLBEBv9IWzFJ9_Jxxxkaj7FQK96euc4p5c0tGq9NqzKQsf2AUSZjnCQmJ_4604gQwLF8m-M9CuNju1CvBzZO-ie3knS_DMz_zAsnQ3NieLED0V53VcKzZfPCm3ZWH7DFsHy53cy4iL2jLAb53kG6RYFcPk-jeKEwcer0u-X_Z1NkXx8uOZjhMuAfG7XnRJ7AwfrEx0F9O0nx73Onv1i_09kmjydTl1D37QQHFl7JX0UhiSAZ2dGg2agfIeY8K32C01knc9nCaw62TH7_kuaH7x79i4CgcyP2WKsf67mBYa8j-IjXOfiw7dxOIQV6PgEOWdmNhfdKpTWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c7c15031.mp4?token=C4GFOqQ6PkLBEBv9IWzFJ9_Jxxxkaj7FQK96euc4p5c0tGq9NqzKQsf2AUSZjnCQmJ_4604gQwLF8m-M9CuNju1CvBzZO-ie3knS_DMz_zAsnQ3NieLED0V53VcKzZfPCm3ZWH7DFsHy53cy4iL2jLAb53kG6RYFcPk-jeKEwcer0u-X_Z1NkXx8uOZjhMuAfG7XnRJ7AwfrEx0F9O0nx73Onv1i_09kmjydTl1D37QQHFl7JX0UhiSAZ2dGg2agfIeY8K32C01knc9nCaw62TH7_kuaH7x79i4CgcyP2WKsf67mBYa8j-IjXOfiw7dxOIQV6PgEOWdmNhfdKpTWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان چین صورتی شد
🔹
آسمان شهر «چانگژو» در استان جیانگ‌سو چین برای چند دقیقه به رنگ صورتی و قرمز درخشانی درآمد و منظره‌ای غیرعادی را رقم زد.
🔹
این‌چنین منظره‌ای پیش از این نیز در نقاط مختلف جهان دیده شده و گاهی از آن با عنوان «شفق طوفانی» یاد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/459496" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459495">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d2fe8f5b6.mp4?token=Cyc3EwEo4qWQFIW9WQIj5gMdRF5wcmO1cBJQXWNc8g4mV2I5wNv68EqRPo2-L8XSAmyR9AtW-7i83WQfqw8FdFZECPZpeA7EiV6uymwWc3axcqTytc8vAAEoT5cwkhaYAKuA7T4VpEwlVdrnBd3TfzwT3EffY4A81fniJX12bnHQo3CuFjNvMVh9e-dSpRcZ5jwYKDdUUefYoqyr16JL05UcyCYov9iHGoMvHhyUX9yB_SO3qCSIBDDM6Wt4fJBw7rbN6vVVnoCkS2-m9tXZDRgJxbyZY91lWEr5l5o7L3mnHvHdOuonWcLvIVRt3NkkRQ8oxQC1-bdTmhtFyABEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d2fe8f5b6.mp4?token=Cyc3EwEo4qWQFIW9WQIj5gMdRF5wcmO1cBJQXWNc8g4mV2I5wNv68EqRPo2-L8XSAmyR9AtW-7i83WQfqw8FdFZECPZpeA7EiV6uymwWc3axcqTytc8vAAEoT5cwkhaYAKuA7T4VpEwlVdrnBd3TfzwT3EffY4A81fniJX12bnHQo3CuFjNvMVh9e-dSpRcZ5jwYKDdUUefYoqyr16JL05UcyCYov9iHGoMvHhyUX9yB_SO3qCSIBDDM6Wt4fJBw7rbN6vVVnoCkS2-m9tXZDRgJxbyZY91lWEr5l5o7L3mnHvHdOuonWcLvIVRt3NkkRQ8oxQC1-bdTmhtFyABEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در جلسات شانگهای و شانگهای پلاس، بر مقابله با یک‌جانبه‌گرایی غرب تأکید شد  @Farsna</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/459495" target="_blank">📅 19:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459494">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde26b3ca2.mp4?token=vFNEJXaCus2-Pm4Q_d6UWZ9eANQku3qhIKpVFnVuKf7wSj9smW3jIb2M_4Yt_Zeam8lIr_73q2W72eIvP6ve86ZPCACu8oBPwFrb9x7LIbxTDOnSq1JoAj3pLI_hQ-jslGu4F7fxG57NwJVa5PW4OQcuzbPFj9sNzxl_CB48BMqFdsu2BXITBEYelViihxC_cZ-8MWs1s2Q4LwjkXoUA_9BJ1kSq5i3zHE12gl-eHF559mPGePdEGd4zBOt_1zoiUlcpV_Yrf_xEM30dXaH9W_r-qmL5qD22fch-gAPIUO2aox8bB3MUTkD5LTr01hXcCfQqnkbt6VZtP0IpDs7IaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde26b3ca2.mp4?token=vFNEJXaCus2-Pm4Q_d6UWZ9eANQku3qhIKpVFnVuKf7wSj9smW3jIb2M_4Yt_Zeam8lIr_73q2W72eIvP6ve86ZPCACu8oBPwFrb9x7LIbxTDOnSq1JoAj3pLI_hQ-jslGu4F7fxG57NwJVa5PW4OQcuzbPFj9sNzxl_CB48BMqFdsu2BXITBEYelViihxC_cZ-8MWs1s2Q4LwjkXoUA_9BJ1kSq5i3zHE12gl-eHF559mPGePdEGd4zBOt_1zoiUlcpV_Yrf_xEM30dXaH9W_r-qmL5qD22fch-gAPIUO2aox8bB3MUTkD5LTr01hXcCfQqnkbt6VZtP0IpDs7IaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
عراقچی: بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است
🔹
خوشوقتم که همراه با رئیس‌جمهور دکتر پزشکیان در اجلاس سران سازمان همکاری شانگهای در بیشکک قرقیزستان حضور پیدا کردم.
🔹
در دیدار و گفت‌گوها با مقامات ارشد اوراسیایی، چینی و جنوب آسیایی، بر…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/459494" target="_blank">📅 19:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459493">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0bbbc3995.mp4?token=v9zIepD_esAHpwan0jtW8ck1J2yBszjSanHRqezt3MJ01qJ1i3rAdjnYUgp_szJgnqpjd9KZzlaJXQep460xCb3WTeUAUjVkEFO9qGUUWVSPJ1drR6N0X8Q4hdBDlwY6P-Z9Xay3eyjgxfzWdkqAQXQHl_YjFn1ZsXPMuSFqBKuyNWvFxM5gfHufNmUs1bkXH6SiXg1pmDbKLQNcH6lDaMv9PyAj0F3HWkRfsqCxQ46TJ168tx_6kGuJUZ5JwwIRyqdE2R1oJXPUCppVb3_47SB1Fgqy3TYI7wB-ZUH-lsTQvTztGAB4NocoC7CR7E5LTCAp2jsVojTY5IXCJUfB3nzIGYsBETIN90y030qbCgHRT6QTK7SoQaBMiUU9bbH7g39tpEoteaR_VblBQvbFwa6czFcExHnHjshD9hVhiEWxiYGmfVNNClloeAJv4_XWafrcKCdjvCVXXfgFgZbC3iv1UMc-hN2eGe5mpwAizOQVVQHy3fKT5MNTsxr4VQ7Ve-CVhiIDPzWq7e0bOjOdHSol-lRqX7gxtsbXAvZErn3CMacF70Tz09qGI563UNsfvLHsoA2dCIUJPtZAHyg9qiYuDzO8my4OG0Mlt-vab11tRIWzfOigIiB2l22P4fhncxBqS-xFqLSt5CNpoQIjj8ivOd2ZKzGz72IREQAHvlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0bbbc3995.mp4?token=v9zIepD_esAHpwan0jtW8ck1J2yBszjSanHRqezt3MJ01qJ1i3rAdjnYUgp_szJgnqpjd9KZzlaJXQep460xCb3WTeUAUjVkEFO9qGUUWVSPJ1drR6N0X8Q4hdBDlwY6P-Z9Xay3eyjgxfzWdkqAQXQHl_YjFn1ZsXPMuSFqBKuyNWvFxM5gfHufNmUs1bkXH6SiXg1pmDbKLQNcH6lDaMv9PyAj0F3HWkRfsqCxQ46TJ168tx_6kGuJUZ5JwwIRyqdE2R1oJXPUCppVb3_47SB1Fgqy3TYI7wB-ZUH-lsTQvTztGAB4NocoC7CR7E5LTCAp2jsVojTY5IXCJUfB3nzIGYsBETIN90y030qbCgHRT6QTK7SoQaBMiUU9bbH7g39tpEoteaR_VblBQvbFwa6czFcExHnHjshD9hVhiEWxiYGmfVNNClloeAJv4_XWafrcKCdjvCVXXfgFgZbC3iv1UMc-hN2eGe5mpwAizOQVVQHy3fKT5MNTsxr4VQ7Ve-CVhiIDPzWq7e0bOjOdHSol-lRqX7gxtsbXAvZErn3CMacF70Tz09qGI563UNsfvLHsoA2dCIUJPtZAHyg9qiYuDzO8my4OG0Mlt-vab11tRIWzfOigIiB2l22P4fhncxBqS-xFqLSt5CNpoQIjj8ivOd2ZKzGz72IREQAHvlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هفت روز جنگ، ۱۵ استان را سرکشی کردم
👤
پورمحمدی در بیست‌ودومین قسمت برنامه ماجرای جنگ۲
🔻
قبل از رسیدن به هر استان، به آنها خبر نمی‌دادم تا متوجه شوم واقعاً در استان چه خبر است
.
🔻
در همان وسط جنگ، با استاندارها درباره پروژه‌های توسعه‌ای استان برنامه‌ریزی می‌کردیم.
🌐
@majaraa_media
نسخه کامل و با کیفیت را از
سایت
و
آپارات
ماجرامدیا تماشا کنید.</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/459493" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459492">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJcBv2ZCJLNU_QZxc1YwRh6KgvcFr-Xk6SeswHmrUkoAqc1bwOWkIfnYvIbNwnKQTGaeJcpOAFYM5uccsN2M1VNFJuHhoef6N2DJjsvZTrFI4cFYfUJEBfa7WMFvgNmX-y0ftMH69GADleGJnDv6MGl4xgPMVpjZcQMOqqX2zB395ERaPFCs45NEy3Hx6JS4uHyEK0DI3ZIx0wyXfMhqFCIIWtlaqzZBRLBlun1IvTn9MDw5kQ5lxxiedKGSrgAi2NrftY1YWC0bFd0GyglgAQFoXeS3mFL_ApecvzFh_tKihEP4VIa0HqeOwTqPllkeZUPFqMWkd8Ma7NgUNKQaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم روند مثبت درآمدزایی بانک پارسیان؛ تراز عملیاتی مرداد ماه از4 هزار میلیارد تومان عبورکرد
مجموع درآمدهای عملیاتی این بانک در ماه مرداد به ۱۱ هزار و 360 میلیارد تومان رسید که نسبت به تیرماه (۱۰ هزار و 311 میلیارد تومان) رشدی حدود ۱۰ درصدی را تجربه کرده است.
در بررسی عملکرد پنج ماهه نخست سال ۱۴۰۵ نیز، بانک پارسیان با کسب ۴۴ هزار و 615 میلیارد تومان درآمد عملیاتی و مدیریت هزینه‌ها در سطح ۳۳ هزار و 725 میلیارد تومان، موفق به ثبت تراز عملیاتی مثبت ۱۰ هزار و 890 میلیارد تومان شده است.</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/459492" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459491">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/459491" target="_blank">📅 19:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459490">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-TopaHmxlkZA7siDahiCuM2qip50sCZJOGJHtKYcVmd2SvaQzW9ch-z2slYgoBPGDBVKold8kWpAbvxJfuKGDt4NM1IMDp5zU5__IrCXS71WYTuytf_ZrQNCj9FWW3UTBkzkGbsRAZv1HXwr7D1wQMPLP_Pv7cH4q9VpgJY9wHPdOlamxlC6ggWf5K1OS3ZnCsJFbQoixxEdwuqz2akf9CabhxzrMD7cWcRmKQ9j_8bAfeBEoWDez56Q7F-lHgCk5ifOs-0TcNh_J3RQwz9Jnw_Kyr_4DKJxnwl_YYKxCYREIIobkQkLdzMDAe24OgS6a2JeKY2SHWzRxBOx8T_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است
🔹
خوشوقتم که همراه با رئیس‌جمهور دکتر پزشکیان در اجلاس سران سازمان همکاری شانگهای در بیشکک قرقیزستان حضور پیدا کردم.
🔹
در دیدار و گفت‌گوها با مقامات ارشد اوراسیایی، چینی و جنوب آسیایی، بر دفاع اصولی ایران از حاکمیت و تمامیت ارضی خود و بر ضرورت اتحاد برای مدیریت روند افول یک امپراتوری بیمار تأکید کردم.
🔹
بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است.
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/459490" target="_blank">📅 19:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqa4qpvzAztOFwZWivQmBb5QU5P44HnglD_VkupgJlj8R_bHDd509NF-snZ8_VWGPddInrmjLfumQxPgMQstiyt-DXdPXfoHnodCH7isqqaMX-DFnaoOBiajsKrQZ07664BL6Nq-_kR7e4Z2fc6pRH0T0peTrmEkfmi8iJQ_bjos0uP1QABEdP0D_FTRTIoD9Dhx8rsL3B60NIYsW3dsm3i7OcJAi-1oD5O1JPKmWFjabYZAEeZVoM4XQlIwY_Dv__fRWRYL75jvRstMNrNlIP4R2a-tJW-sZzEHjmiPMTWBl1AXVIFNulS19sANEsX299bnHB-GHoFjGxMWqZMuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با گوترش: سازمان ملل باید در قبال تحولات بین‌المللی نقش‌آفرینی مؤثرتر و کارآمدتری داشته باشد
@Farsna</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/459488" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9aac287a.mp4?token=vMCjq-2CcCw1eDFre9fIDzgYTDS3PNOu7ul7-2esAs-lYgMT1VeYoMGBUAN6n_fhlvVMkDZqo9HkqQzQ6vERIje3wwu3ZUUDbrPmZye2VEH9k06OnEtu_jniUTDfN60QTa_22W_hxAvaIMBI7ssdd0IwuWr7Tez4QtLDfZwlOXBV7zsmSYH6cyFF3zH53EeV6Mt9Vw9Un01_azMgVW5u1gaLK3VmzbkzfL1YqjddD57Ebjzw-1i0fba-4_oD1MTaCuFGME60BAWQY4x6QKOpWQHBZnHkLMsLoRL4SBgaZS71l97yabNMx0lM5jmeEbnUwLvV7KXM6u9FiF2sfk85Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9aac287a.mp4?token=vMCjq-2CcCw1eDFre9fIDzgYTDS3PNOu7ul7-2esAs-lYgMT1VeYoMGBUAN6n_fhlvVMkDZqo9HkqQzQ6vERIje3wwu3ZUUDbrPmZye2VEH9k06OnEtu_jniUTDfN60QTa_22W_hxAvaIMBI7ssdd0IwuWr7Tez4QtLDfZwlOXBV7zsmSYH6cyFF3zH53EeV6Mt9Vw9Un01_azMgVW5u1gaLK3VmzbkzfL1YqjddD57Ebjzw-1i0fba-4_oD1MTaCuFGME60BAWQY4x6QKOpWQHBZnHkLMsLoRL4SBgaZS71l97yabNMx0lM5jmeEbnUwLvV7KXM6u9FiF2sfk85Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: همهٔ اعضای شانگهای بدون استثنا، تجاوز به ایران را محکوم کردند  @Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/459487" target="_blank">📅 18:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e7c1d89b.mp4?token=Zr3YdXSSs2KxqIS8NlXByiwEzFhtU0xhkw3C3oJ1ZVN7F3V7ipbnyVv7kbP5sPPRgzP9-K1EQn6hCOKXShmi9v1pMm62qVD3ta3BCSBODKpbn_V7vb8H5Rbsw6yRoPkArBiONk381N0BCb3aEQE9twigsIJP7ljNlKmP-6UadQeoQKI542KO8yJr-m_ZpzFFXQKsfVlZ3lsbVkaRmpQzReQBNKBIuZY2fc47joOY7bc5ucZiTxN2P19ai-_vCkAvZ8gQOedbSRL_2Wzpu6q5nkIULjIJy1WKdym_e_yyALqPHKu76hb_QgbEzkvQLLKuEShQznKipQ0klsxl1Md4RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e7c1d89b.mp4?token=Zr3YdXSSs2KxqIS8NlXByiwEzFhtU0xhkw3C3oJ1ZVN7F3V7ipbnyVv7kbP5sPPRgzP9-K1EQn6hCOKXShmi9v1pMm62qVD3ta3BCSBODKpbn_V7vb8H5Rbsw6yRoPkArBiONk381N0BCb3aEQE9twigsIJP7ljNlKmP-6UadQeoQKI542KO8yJr-m_ZpzFFXQKsfVlZ3lsbVkaRmpQzReQBNKBIuZY2fc47joOY7bc5ucZiTxN2P19ai-_vCkAvZ8gQOedbSRL_2Wzpu6q5nkIULjIJy1WKdym_e_yyALqPHKu76hb_QgbEzkvQLLKuEShQznKipQ0klsxl1Md4RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس اقتصادی: سیاست قیمتی برای کنترل مصرف بنزین، به دلیل نبود خودروهای کم‌مصرف جایگزین، با شکست مواجه شده است
🔹
محمد‌حسین صبوری، کارشناس اقتصادی: مصرف سوخت ما نسبت به سایر کشورها در سطوح بسیار بالا قرار دارد و بخش عمده‌ای از این موضوع، ناشی از استفاده از خودروهای فرسوده و غیربهینه است.
🔹
با وجود اینکه تکنولوژی‌های جدید وارد شده‌اند، اما بحث اصلی بر سر سیاست‌هایی است که باید در حوزه خودروسازی اجرا می‌شد تا این وضعیت تغییر کند.
🔹
نتیجه این اشتباهات امروز در قالب ۲ چالش بزرگ خود را نشان می‌دهد نخست، وجود انحصار در صنعت خودرو و دوم، افزایش بی‌رویه مصرف سوخت که ۲ یا ۳ دهه است کشور را آزار می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/459486" target="_blank">📅 18:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd4e0f9f7.mp4?token=o0W4list1jI-iYYrlcz4t2qcCFb_IlgQfakgs3_WoJ6gdYc4EEnp90USSoV_HkMpRu2NKmHhjr9OFCIjMAfr1OuZ0wjml7lC-1LClmACs9c9J71iahJHAh0Upgri3bpMQYZzd-sTFFnSOlye2oASR3h0ucbrkQQ9ypeAwXCejvlD74RD1gpb-xmSsaQhfKigZj_e_tHoMmcOnHsF7FpayuhxrBeBDWrcT7E5-cN18L4FIo1DHPKbOxTcg9FzVhpiW24I8jMhIbu_jfkD0iic71BfE0E1QgPhntZpUSwgh0jww-5za_IBJk4P1lnCed4opNfbp0AcFsC4WhQTwz3NHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd4e0f9f7.mp4?token=o0W4list1jI-iYYrlcz4t2qcCFb_IlgQfakgs3_WoJ6gdYc4EEnp90USSoV_HkMpRu2NKmHhjr9OFCIjMAfr1OuZ0wjml7lC-1LClmACs9c9J71iahJHAh0Upgri3bpMQYZzd-sTFFnSOlye2oASR3h0ucbrkQQ9ypeAwXCejvlD74RD1gpb-xmSsaQhfKigZj_e_tHoMmcOnHsF7FpayuhxrBeBDWrcT7E5-cN18L4FIo1DHPKbOxTcg9FzVhpiW24I8jMhIbu_jfkD0iic71BfE0E1QgPhntZpUSwgh0jww-5za_IBJk4P1lnCed4opNfbp0AcFsC4WhQTwz3NHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: همهٔ اعضای شانگهای بدون استثنا، تجاوز به ایران را محکوم کردند
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/459485" target="_blank">📅 18:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSnR2Y-ZjOUKyLL1PHEqP-h6_wT9hdxQECGXj6B6lHYOwx0uLamk4UaVJP8MEUETy0GjWOLFx5_gXvhOtXKedSNtU-xyBEXUmxxBEarQwFiRD1wbVu5dmvxjVOzVdGyi66GhlvRmVCxfas9Nwn-tg7k-VPV_8fasNcVlXexWmV9ZY3ogfdYy8RhXgwrki1f0FX1H58C1m0t3JxVMy4WJ4espOLBPANgYvlTj6dF7jB48NS59lFTaZU1beo9loNRXpZ-CNZ2wx0G_8xom9tu6JZCBzTb2YPpPpMrgs0DX9rXIMiUXOhualgKNXq6Ihcv6HCnWkZGh3Wy-L6qpa8MVPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌ها قانون بانکداری بدون ربا را کنار گذاشته‌اند
🔹
رئیس شورای فقهی بانک مرکزی: نظام بانکی قانون عملیات بانکداری بدون ربا را بوسیده و کنار گذاشته است. به نرخی پول می‌گیرد و به نرخی هم پول می‌دهد.
🔹
بانک باید پول و منابع را به عنوان وکالت از مردم و سپرده‌گذاران بگیرد و به سرمایه‌گذاران بدهد، وقتی سرمایه‌گذاری کردند ببینند سود تحقق یافته چقدر است آن را تقسیم کند سهم خودش را هم بردارد.
🔹
قانون عملیات بانکی بدون ربا سال ۶۲ تصویب شد و چارچوبی را تعیین کرد که در آن بانک به‌جای دریافت و پرداخت بهره، باید منابع سپرده‌گذاران را در قالب عقود اسلامی به فعالیت‌های اقتصادی اختصاص دهد، و قرار بود از سال ۶۳ اجرا شود اما این اتفاق نیفتاد.
🔹
در حال حاضر بانک‌ها برای سپرده‌های یک‌ساله ۲۳ درصد سود پرداخت می‌کنند و برای سپرده‌های کلان، نرخ‌های ترجیحی تا ۴۰ درصد دارند.از طرف دیگر برای پرداخت تسهیلات نیز همین روش را اعمال می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/459484" target="_blank">📅 18:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST6aZF9O3JIrQNqkuFUJTwnkcBdf7slD-2rLKPi1b2f4HMrtHya6w8uYombJscrZGQBd_UastQevHM5HN45hmhCzVc7JvVeIRQpwAzQbP0D_hLywnNUmpWwNKO9GdbGcgF4bpE8pZ-dMmI9dfAfe8K8aObMmrfXnjoPmYoj9y43FJylbOWR5GLoLfuGHOCxfEoNixP37H8V5drsR1AohwPsci3Wo4zyhkXhMocQcQU963NHCUXsMjifoRl4ktY8b2cqkfFmewhEmo9kTDU_MvnaQYqpzydhXLNdaNMF2QuwuQq5kVggJ3f04dXbwJXKR6JINWkxhpvjviEorEzAfGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصوبۀ حمایت از خریداران خودرو باطل شد
🔹
سخنگوی شورای رقابت اعلام کرد دیوان عدالت اداری با رسیدگی به شکایت خودروسازان، مصوبۀ ۴۷۳ شورای رقابت را که برای حمایت از خریداران خودرو در برابر افزایش قیمت تصویب شده بود، باطل کرده است.
🔹
براساس این مصوبه که در سال ۱۴۰۰…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/459483" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25637cbe58.mp4?token=ilqi-I8Ip32vXHO3REoS4P9CaMiej50PWVwetwwYFHFQKbgACTo12YFTdnmemFCd4c3aris-oPvX56tZj_I6tEvEGDixwvRA-AidbmH5uF5rNiRjkS46O3366DDKtISiMXITl-9qTPb3YWjfJftaex3iffQiZJpLqSQMB2GJeQcc9-8J7CcZqJqhx6kMwGvraFmVpIzQTt3s7OVyT2Mao2OkjMj_sCgNTny0_0u_r7o_SYNTHVxxCgAO8kVijrUNxTdkLYGOzFXRxWvmxhbiFJrXXQVjnoG1h-d5CCLxTwGTkZkUZoI5kQJZHau0SHPJAi5sJkkBHFnGBL206IoOKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25637cbe58.mp4?token=ilqi-I8Ip32vXHO3REoS4P9CaMiej50PWVwetwwYFHFQKbgACTo12YFTdnmemFCd4c3aris-oPvX56tZj_I6tEvEGDixwvRA-AidbmH5uF5rNiRjkS46O3366DDKtISiMXITl-9qTPb3YWjfJftaex3iffQiZJpLqSQMB2GJeQcc9-8J7CcZqJqhx6kMwGvraFmVpIzQTt3s7OVyT2Mao2OkjMj_sCgNTny0_0u_r7o_SYNTHVxxCgAO8kVijrUNxTdkLYGOzFXRxWvmxhbiFJrXXQVjnoG1h-d5CCLxTwGTkZkUZoI5kQJZHau0SHPJAi5sJkkBHFnGBL206IoOKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: به ملت بزرگ ایران اطمینان می‌دهم با عنایات الهی، حضور مردم در صحنه و انسجام مسئولان ذیل رهنمودهای رهبر انقلاب، ایران عزیز از این آزمون بزرگ سربلند بیرون خواهد آمد و افتخار عظیمی برای ایران در تاریخ جهان ثبت خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/459482" target="_blank">📅 18:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459480">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/373a1bfd33.mp4?token=VEHl7eXzr-dNbHgQ4fEu4InYjGAk49BvlZN2naCr5HxmZUQKy_AEWzcdjtbmf7TwEp439JaGbavf0S_sKvOF1qqQ4UyK9i_LjNccH1o4udUMGVKsfIBCDq6K0MG8TG-43WIooG-uQXlP4X2W3AnVPvGuvbptNOyOsiIKq9gRR2S52P_2hHYKyh84xmwVlaEoWR7l9rE0zrxP5qtFV6FPrrALIGcyfDLDKek7uH-j6MPMRlVrSyKQaojIPyZ08AhitRDDo0q47ojyd9Ll7pHwHVRDo7wliM041_xEDo9gZIggcm1PG2kXM1Z3hp4Xc4Gl3IG0NwCBl2gZfgmE-ovM5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/373a1bfd33.mp4?token=VEHl7eXzr-dNbHgQ4fEu4InYjGAk49BvlZN2naCr5HxmZUQKy_AEWzcdjtbmf7TwEp439JaGbavf0S_sKvOF1qqQ4UyK9i_LjNccH1o4udUMGVKsfIBCDq6K0MG8TG-43WIooG-uQXlP4X2W3AnVPvGuvbptNOyOsiIKq9gRR2S52P_2hHYKyh84xmwVlaEoWR7l9rE0zrxP5qtFV6FPrrALIGcyfDLDKek7uH-j6MPMRlVrSyKQaojIPyZ08AhitRDDo0q47ojyd9Ll7pHwHVRDo7wliM041_xEDo9gZIggcm1PG2kXM1Z3hp4Xc4Gl3IG0NwCBl2gZfgmE-ovM5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: به دشمن هرگز اجازه نخواهیم داد پا روی شرافت و عزت ما بگذارد
🔹
نقاط ضعف را باید در اندرون خود حل کنیم. با قوی‌بودن است که دشمن را وادار به عقب‌نشینی می‌کنیم.
🔹
همه ما مسئولان باید بسیار مراقب باشیم و خطای محاسباتی نکنیم.
🔹
سخنان حساسیت‌ برانگیزی که باعث شکاف در بدنه جامعه شود یا پدیده‌های اجتماعی که ممکن است مردم را مقابل هم قرار دهد، اساساً نباید بیان شود. باید روی نقاط قوت تأکید کرده و درباره آن‌ها صحبت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/459480" target="_blank">📅 18:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459479">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12429648eb.mp4?token=HwejwZZ1e6GQ4zNA_J5bb371bge_KbV4r8qKKnU-dBq8TeTF2i39P6tUMTr0Blj1s-T_cDM1P9z4onPt11KvUCaQ_weO79konDGsHl3Zv9LPp6ceB3q9M2UWgqwFqsC9RH3XLR4Vc4MjxgXbJY3fGeQnyBxSX30j6ykH_BwC8x2zQ00AmXBGqmxXjrT12vxYStkW7KAgcjleQmubttQyHxJpFbJ65fgku85w_AuAMf3sbN_uO0MwfWf6L8ACdNHuy0RT3-oOd0XT9LjZLJUM9GsmLWbnsAePBHw7clopd3vS4LjLRKMtpprE1nXo_gAnkQj7GC8mUZ56CBn6CA3Qrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12429648eb.mp4?token=HwejwZZ1e6GQ4zNA_J5bb371bge_KbV4r8qKKnU-dBq8TeTF2i39P6tUMTr0Blj1s-T_cDM1P9z4onPt11KvUCaQ_weO79konDGsHl3Zv9LPp6ceB3q9M2UWgqwFqsC9RH3XLR4Vc4MjxgXbJY3fGeQnyBxSX30j6ykH_BwC8x2zQ00AmXBGqmxXjrT12vxYStkW7KAgcjleQmubttQyHxJpFbJ65fgku85w_AuAMf3sbN_uO0MwfWf6L8ACdNHuy0RT3-oOd0XT9LjZLJUM9GsmLWbnsAePBHw7clopd3vS4LjLRKMtpprE1nXo_gAnkQj7GC8mUZ56CBn6CA3Qrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
درخواست یک شهروند از موتورسواران قانون‌گریز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/459479" target="_blank">📅 18:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459478">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399ee501a0.mp4?token=qCkFr2xcoBTfcEAmSzSckiZ7eIxefrL15H_gAwD5mqf2J3KaVrUkH9Dqo0zzLjjuBr30zFMayEbXjT2u2fad-SAXYKJa6Gs_2OX0bumlzehgncRGruQag6rxNEm-MktOFE4l5guPd4W22VhsMuHsdCciGlrRO56pBfrhTSiJQW9Ea2fahktGcCgOE7b_v0I7MLPFRW8rmTw8ccAvcMed1c2Tia-N6VBznyY9rsgqXN5AGVUL4KKROG0bwl_UzyORpA9fRiFgBMmzOGIuTihbGrX_6-W_I5QMLPAzNE5E6jrCLioeqt8P1mLT8iEJd8AJ-Kg7RCnjA4XkZ5dBXtD26A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399ee501a0.mp4?token=qCkFr2xcoBTfcEAmSzSckiZ7eIxefrL15H_gAwD5mqf2J3KaVrUkH9Dqo0zzLjjuBr30zFMayEbXjT2u2fad-SAXYKJa6Gs_2OX0bumlzehgncRGruQag6rxNEm-MktOFE4l5guPd4W22VhsMuHsdCciGlrRO56pBfrhTSiJQW9Ea2fahktGcCgOE7b_v0I7MLPFRW8rmTw8ccAvcMed1c2Tia-N6VBznyY9rsgqXN5AGVUL4KKROG0bwl_UzyORpA9fRiFgBMmzOGIuTihbGrX_6-W_I5QMLPAzNE5E6jrCLioeqt8P1mLT8iEJd8AJ-Kg7RCnjA4XkZ5dBXtD26A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانوی دریانورد هرمزگانی حکایت جالبی دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/459478" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459477">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8952f37e1e.mp4?token=nVqw7LpgE6MjhHueJE-x1nIbk1d5gzgj_GupP3iMeK-HzyiUfyCLaOOCGhzUaijRQ2VUZhWTqB3iE8IZhujeD4ne7hnyJEn-3r9ymZXd7XREdzJreNucruR_OzeXCLPm4W5OntJYF2FpWX7d7SflBE7BX1qv6sFUQKcGdZpRNV_m4PiZz4w_DyzwAOkp88OHpEMHiLN57hcWCxe3PnCqKbCwZaPF_7KklVBzbuBqOIevHrOtjbdXLKo29m4j6X26BtH7-x3bwKLtIt46aRopdfpJdVxzof5lhOjk-bMasUUHcWICWbsc2Jj6gPVQ3DWdRKuvf1F4duMQjGq33JcfwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8952f37e1e.mp4?token=nVqw7LpgE6MjhHueJE-x1nIbk1d5gzgj_GupP3iMeK-HzyiUfyCLaOOCGhzUaijRQ2VUZhWTqB3iE8IZhujeD4ne7hnyJEn-3r9ymZXd7XREdzJreNucruR_OzeXCLPm4W5OntJYF2FpWX7d7SflBE7BX1qv6sFUQKcGdZpRNV_m4PiZz4w_DyzwAOkp88OHpEMHiLN57hcWCxe3PnCqKbCwZaPF_7KklVBzbuBqOIevHrOtjbdXLKo29m4j6X26BtH7-x3bwKLtIt46aRopdfpJdVxzof5lhOjk-bMasUUHcWICWbsc2Jj6gPVQ3DWdRKuvf1F4duMQjGq33JcfwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: از همهٔ سیاسیون در هر طیفی درخواست دارم اختلافات را کنار بگذارند
🔹
نباید فراموش کرد که همین الان نیز در جنگ هستیم. لازمه پیروزی در جنگ، مخصوصاً جنگ ترکیبی، انسجام و وحدت اجتماعی است.
🔹
از همه سیاسیون در هر طیفی و همه افراد خارج از مسئولیت رسمی درخواست دارم اختلافات چند ماه اخیر را کنار بگذاریم و همچون زمان جنگ رمضان، حول محور ولایت متحد شویم.
🔹
برخی دوگانه‌سازی‌های موهوم و برخی اظهارات جنجال‌برانگیز از اضلاع مختلف سیاسی کشور در این ایام اتفاق افتاد که دشمن را به اختلافات داخلی ما به طمع انداخته است.
🔹
پیام رهبر انقلاب، با ذکر جزئیات دقیق، تکلیف همه ما را روشن کرد.
🔹
هرکس از هر طرف بر دوگانه‌هایی که رهبری آن را موهوم دانستند اصرار کند، خلاف شرع بیّن و ضد منافع ملی عمل کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/459477" target="_blank">📅 18:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459476">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1395dd58a0.mp4?token=pKPDbVyA4BVlZ6LsGqhnTgpYtOPdQGuNvafMu10xdZISZEjpBBAXglCqZbu7DUYLqfxO-l_JVzBqk0-rFL2c1Hao3IkNeHzgWpoJBgcepLdpjgSunxAW_tOBqXKazlwQsaoIvbmGwWyZqYzH1LnX5lRhOo2IzojwPxlkq7PjSlCh79OQAEMVuDceXqVE7ZcngV1m0-5COfMdbM7XSHvKWQt4flOV9V9kCZdraBakZctrMsyhwmAJ0krtU6JMvriO1UY8L_gZO8LEkooXy6NyYKvoAE3VEsH-1I9H8d_JCu3QMjXprSGYFN_74xIREm34SUeB0uU66f348p-KA4xZVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1395dd58a0.mp4?token=pKPDbVyA4BVlZ6LsGqhnTgpYtOPdQGuNvafMu10xdZISZEjpBBAXglCqZbu7DUYLqfxO-l_JVzBqk0-rFL2c1Hao3IkNeHzgWpoJBgcepLdpjgSunxAW_tOBqXKazlwQsaoIvbmGwWyZqYzH1LnX5lRhOo2IzojwPxlkq7PjSlCh79OQAEMVuDceXqVE7ZcngV1m0-5COfMdbM7XSHvKWQt4flOV9V9kCZdraBakZctrMsyhwmAJ0krtU6JMvriO1UY8L_gZO8LEkooXy6NyYKvoAE3VEsH-1I9H8d_JCu3QMjXprSGYFN_74xIREm34SUeB0uU66f348p-KA4xZVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آ
غاز پرداخت خسارت مشترکان قطع برق از نیمهٔ مهر
🔹
مدیرکل مدیریت انرژی و امور مشتریان توانیر از ثبت حدود ۱۱ هزار درخواست خسارت مشترکان برق خبر داد و گفت: تاکنون حدود ۳۵۰ میلیارد تومان خسارت پرداخت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/459476" target="_blank">📅 18:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459475">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb23fdfbf5.mp4?token=OEbtyfw99fD6YzEt96IeAFFI9b0ozylWtjUVwJu-pidBso8AN1hVLdNwgMbChpYpHC-Libf8plYv3YXvJF26qsg6L4N0VEAP307C-3nz5STvOM-dBoaMEuRznPyXAaebn37xlqceyd4sEpc6N-YNI1fBxXZTsuCqf3fNly4L-gLQ9dk92KAdCxfW1SRkrkrhPLjwjwP8zwsGmxjRcmwvFt12VfQ_qxo6XJhEhVSymIudgFI4VfS5ED4hfsU9fhY6b-jmeZlDe-jHXrR6EFV4KMF5pDLYn7y_jH4Hs3PJBHwaO8y2YZwu3E89ysDykzFwoPb6-HpoBBkl5MTTHNra1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb23fdfbf5.mp4?token=OEbtyfw99fD6YzEt96IeAFFI9b0ozylWtjUVwJu-pidBso8AN1hVLdNwgMbChpYpHC-Libf8plYv3YXvJF26qsg6L4N0VEAP307C-3nz5STvOM-dBoaMEuRznPyXAaebn37xlqceyd4sEpc6N-YNI1fBxXZTsuCqf3fNly4L-gLQ9dk92KAdCxfW1SRkrkrhPLjwjwP8zwsGmxjRcmwvFt12VfQ_qxo6XJhEhVSymIudgFI4VfS5ED4hfsU9fhY6b-jmeZlDe-jHXrR6EFV4KMF5pDLYn7y_jH4Hs3PJBHwaO8y2YZwu3E89ysDykzFwoPb6-HpoBBkl5MTTHNra1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: انسجام اجتماعی، مهم‌ترین معروف اجتماعی است که باید یکدیگر را به آن توصیه کنیم
🔹
هر اقدامی که اصل انسجام را خدشه‌دار کند، بزرگ‌ترین منکر است.
🔹
انسجام ملی، عامل ارتقای روحیه نیروهای مسلح و شکست دشمن بود.
🔹
بعد از لطف خدا، همت و انسجام مردم پیروزی را نصیب کشور کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/459475" target="_blank">📅 18:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459474">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e496db28.mp4?token=LQe6r_6ZMVeNyaKSyd8c-78zU2FR0JJJp7SjjmkZDXSIwMjfJflMjwCCfeLEnic14-b90mVzrG5TChZY1_vcOpC3cTIicGmxjJMmJpCflYoeaixSEB8T5PVHerGjrLCLguy7YBUFkvMJzhuLT9Exkop4PI-rxxQ2eNeyHDoaz7eGsc3MRCm2I9nZsmXwss92I53T6TZuzffYfJxTkcnwunlFY6N-HPQ5br5xR0eLsbqVsgvsZVJ-eWpTKoLN0brrS0SVu-i9vBXNltHr-HxwNTeVFEKn1h3o9CEUwi-7oiJ37DrBkjxZ2wcEgGg1h5Q_8jqmJzE7Sps6mFNq75DKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e496db28.mp4?token=LQe6r_6ZMVeNyaKSyd8c-78zU2FR0JJJp7SjjmkZDXSIwMjfJflMjwCCfeLEnic14-b90mVzrG5TChZY1_vcOpC3cTIicGmxjJMmJpCflYoeaixSEB8T5PVHerGjrLCLguy7YBUFkvMJzhuLT9Exkop4PI-rxxQ2eNeyHDoaz7eGsc3MRCm2I9nZsmXwss92I53T6TZuzffYfJxTkcnwunlFY6N-HPQ5br5xR0eLsbqVsgvsZVJ-eWpTKoLN0brrS0SVu-i9vBXNltHr-HxwNTeVFEKn1h3o9CEUwi-7oiJ37DrBkjxZ2wcEgGg1h5Q_8jqmJzE7Sps6mFNq75DKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: سیاست جمهوری اسلامی ایران طبق فرمان رهبر انقلاب، تحقق شروط تفاهم‌نامه است
🔹
در مدت اجرای تفاهم‌نامه، محاصره دریایی رفع شد و در لبنان نیز، در حالی که در شرایط سختی بودیم، آتش‌بس پایدار شد، البته این به معنای رخ ندادن اتفاقات کوچک‌تر نیست.
🔹
در همین مدت، بیش از ۸۰ میلیون بشکه نفت صادر کردیم و در واردات کالاهای اساسی نیز اقدامات خوبی انجام دادیم.
🔹
اگر آمریکا به تعهداتش عمل نکند، با زبان قدرت او را مجبور به انجام تعهداتش می‌کنیم.
🔹
تا زمانی که تعهدات آمریکا در تفاهم‌نامه اجرایی نشود تنگه باز نخواهد شد.
🔹
شکست سوم آمریکا در میدان دیپلماسی، اجبار آمریکا به اجرای تعهداتش خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/459474" target="_blank">📅 18:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459473">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd85c2a1.mp4?token=N-X-KuQog_GLXDlwjwzNMSNFYpBfOgmlYui2n4LA1hLRcKeyP6mCP1E8jBi5MjP40CcNzyLVJ2kXPIc0ayI2ZT_m1kx6YelBcoyGPFvSH1ZAnks3B3V3iTUqqvzOkpj3Gut7I7GUUwbu2hlRDPQupg0uaYKKWiaqY-wOS_WhXxsN2aCOjXGsI_w8_cO5uNjqCIWvsRezbdV4blErVa9TszU_zGWoq9FzpP33LRv64mRxt4wZw2ow8V-2A6ViTiKqyai75hmHSVqcOJ1IESa-qU2atEDh7yTZdBU0nO7C7GFzbve2KSRw42DOy3g5evxkFbEVpsDTugVclmgYgxzabauwEVajtp5mKU22c5r0unIb3jct2zelobPqXUXmVLtzJxPZJOnFKn4RvVvnfX915w_rGqMX4l7kJer6YBv97jKZNE_aD993fyl9ohNpLU27BZX0f6lgeZo-ka7bUmS4Sgh9R1bqVYK8aXaZkmxUH8Yy5PYp3AV0Lh-6syuZ75zZqrQJakm3e5S2B8xzq5Q4DByB3yGl0YixHjtP3qTIbDkG4UoBBXUiQzGr9Bck-zGZdCjsNT-QsuVms2qU1ugD1cX6HovRm-L1RLwBPRDsJrTZGvnGQYTegTJY6VYVWf1bdq20rY7EQXRHARaxjrT5noHGxDBSZ4I5JMCWJUZH9p4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd85c2a1.mp4?token=N-X-KuQog_GLXDlwjwzNMSNFYpBfOgmlYui2n4LA1hLRcKeyP6mCP1E8jBi5MjP40CcNzyLVJ2kXPIc0ayI2ZT_m1kx6YelBcoyGPFvSH1ZAnks3B3V3iTUqqvzOkpj3Gut7I7GUUwbu2hlRDPQupg0uaYKKWiaqY-wOS_WhXxsN2aCOjXGsI_w8_cO5uNjqCIWvsRezbdV4blErVa9TszU_zGWoq9FzpP33LRv64mRxt4wZw2ow8V-2A6ViTiKqyai75hmHSVqcOJ1IESa-qU2atEDh7yTZdBU0nO7C7GFzbve2KSRw42DOy3g5evxkFbEVpsDTugVclmgYgxzabauwEVajtp5mKU22c5r0unIb3jct2zelobPqXUXmVLtzJxPZJOnFKn4RvVvnfX915w_rGqMX4l7kJer6YBv97jKZNE_aD993fyl9ohNpLU27BZX0f6lgeZo-ka7bUmS4Sgh9R1bqVYK8aXaZkmxUH8Yy5PYp3AV0Lh-6syuZ75zZqrQJakm3e5S2B8xzq5Q4DByB3yGl0YixHjtP3qTIbDkG4UoBBXUiQzGr9Bck-zGZdCjsNT-QsuVms2qU1ugD1cX6HovRm-L1RLwBPRDsJrTZGvnGQYTegTJY6VYVWf1bdq20rY7EQXRHARaxjrT5noHGxDBSZ4I5JMCWJUZH9p4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: با قدرت، منطق‌مان را بر دشمن تحمیل کنیم و هرگز تسلیم نظامی یا سیاسی نخواهیم شد
🔹
در آغاز گفت‌وگوها، آمریکا یک متن ۱۵ ماده‌ای در خصوص هسته‌ای، موشکی و محور مقاومت ارسال کرد؛ اما امروز وقتی متن ۱۴ ماده‌ای نهایی را نگاه می‌کنید، می‌بینید دشمن از همه آن‌ها عقب‌نشینی و رئیس‌جمهور آمریکا پای این سند را امضا کرد
🔹
چارچوب مذاکراتی را ما تنظیم کردیم و دشمن را وادار کردیم پیروزی‌های میدان را تبدیل به سند سیاسی کنیم.
🔹
اجرای سند به اندازه امضای آن نیز مهم است؛ اما بدانید وقتی سندی امضا نشود، راهی برای اجرای آن نیز نیست.
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/459473" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459472">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51ba267bb.mp4?token=f0p3bT9_lHyYDQaCHyhU0ZI0Umh2MEIkeO9FJNI_bUkKkmWAw6o3E_FnGx7ikS8vwV1dCGcq3XQeZ-JWAM3EIs3uVQ1Ob3BdA-sOuRjIDr4FV-o10kSayuQF3EljeBXWrSwiOK8t_U3QLUKI4bzDXKicGRkDAjO91blMRmNT36KBNkYoCVn7-A6mzRuPDXtDoYqtn3lf_fEJgvb2GbWP9aKIcdRDIpIQmiWkKsoekDqS7WwLCWo-fP2bQwyZK391sbp5ZtaZ-LvkyRvKnuhFbQvPcu3ERYlwtDGhNCg-GAL_guv6_OUEfX1DZvqmo856g-iuzpZHBsVs5UY06Z_aDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51ba267bb.mp4?token=f0p3bT9_lHyYDQaCHyhU0ZI0Umh2MEIkeO9FJNI_bUkKkmWAw6o3E_FnGx7ikS8vwV1dCGcq3XQeZ-JWAM3EIs3uVQ1Ob3BdA-sOuRjIDr4FV-o10kSayuQF3EljeBXWrSwiOK8t_U3QLUKI4bzDXKicGRkDAjO91blMRmNT36KBNkYoCVn7-A6mzRuPDXtDoYqtn3lf_fEJgvb2GbWP9aKIcdRDIpIQmiWkKsoekDqS7WwLCWo-fP2bQwyZK391sbp5ZtaZ-LvkyRvKnuhFbQvPcu3ERYlwtDGhNCg-GAL_guv6_OUEfX1DZvqmo856g-iuzpZHBsVs5UY06Z_aDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان برنامه و بودجه: در جلسهٔ نوروز ۱۴۰۴ رهبر شهید فرمودند اولین اقدام دشمن ترور همین جمع است و برای شهادت آماده باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/459472" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459470">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dafb57407.mp4?token=iGMGxqW3KYhPS0-nbUmVURfUChj_67ZI3vqqTeKfZ16ihi8y8ID_IcOYgF4ndbGybqnrskxQDh660ovsxdbWVzig0d-XdfkgpYeOwsT2Pe86y11fUTiVe33YdHngmBqju5bLxTMvQ2Gq1EHvM2TPDhESzaLnTafEKHPimmB5JtRKDj2guARvtmH46HzgrQ7BH7xQKjJXrpaIFhmouY13pElskfwPuFTMhvLRJCYsMEZ9Df-NSGWZsv-fu6qd4uU0cfhc76dsVBRlRFJfaf27v4ezDq9RppCoBcYZjI3cExhMe8V9XG2lzvHgLuO11bSqUD5S9qsHTQ0ePeF0pelAzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dafb57407.mp4?token=iGMGxqW3KYhPS0-nbUmVURfUChj_67ZI3vqqTeKfZ16ihi8y8ID_IcOYgF4ndbGybqnrskxQDh660ovsxdbWVzig0d-XdfkgpYeOwsT2Pe86y11fUTiVe33YdHngmBqju5bLxTMvQ2Gq1EHvM2TPDhESzaLnTafEKHPimmB5JtRKDj2guARvtmH46HzgrQ7BH7xQKjJXrpaIFhmouY13pElskfwPuFTMhvLRJCYsMEZ9Df-NSGWZsv-fu6qd4uU0cfhc76dsVBRlRFJfaf27v4ezDq9RppCoBcYZjI3cExhMe8V9XG2lzvHgLuO11bSqUD5S9qsHTQ0ePeF0pelAzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: مقصر بخشی از مصرف زیاد بنزین مردم نیستند بلکه مقصر صنعت است
🔹
مسئله بنزین را می‌شود با صرفه‌جویی حل کرد. اصلاحات ضروری باید حتماً با خرد جمعی و همراهی مردم، به‌گونه‌ای باشد که فشار بر روی مردم کمتر شود.
🔹
رضایت مردم اصل اول ماست. هرجا درباره مسائل تصمیم خوب گرفتیم، با مردم صحبت کردیم و آن تصمیم را خوب اجرا کرده‌ایم، مردم همراهی کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/459470" target="_blank">📅 17:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5lE9tgqSTwRCNGcUQqnkJOBS6B_r4YYSyH-kzau8tUnielB9iO0OccHvrczpQlYyUxq2nT5WmxVAH74s0UP5laZMi49iOZQESP-iDn1iNW2OmIDza7zMYG-_fgzktv2W043nfj4FOjeOUm-pWS50hSIoi_LjXw_cs0dhcEtRSEUVvz9ornTEaolw5L979jHoGArGQOI8pK7FxumBs5ksHj_QhQJMIbB2UK3uqR7YS3IXoD9QYjsAG44YIc8jGQjHUPd4Jtlt3lXYD2B7jSyQW7tyEcba70NJQlyXE6aOV8dGYJIDaINt58USdSRJ72-nViE7gbeL2XEWBbNYgltQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سران شانگهای: «قانون جنگل» باید برچیده شود
🔹
سران سازمان همکاری‌های شانگهای در نشست شانگهای پلاس در بیشکک پایتخت قرقیزستان بر نقش سازمان ملل برای حل و فصل بحران‌های جهانی تأکید کردند.
🔹
رئیس‌جمهور روسیه با بیان اینکه ظرفیت‌های سازمان ملل همچنان «استفاده‌نشده» باقی مانده است، اظهار کرد برای افزایش کارآمدی این سازمان باید تلاش بیشتری صورت گیرد. به گفته وی، نهادهای سازمان ملل از جمله شورای امنیت باید نمایندگی گسترده‌تری از کشورهای جنوب و شرق جهان داشته باشند.
🔹
رئیس‌جمهور چین همچنین از اعضای سازمان همکاری شانگهای خواست برای بازگرداندن اعتبار سازمان ملل و بخشیدن حیات تازه به این سازمان با یکدیگر همکاری کنند.
🔹
الکساندر لوکاشنکو، رئیس‌جمهور بلاروس، نیز گفت سازمان همکاری شانگهای می‌تواند در احیای سازمان ملل نقش داشته باشد و این سازمان را بار دیگر به بستری برای حل دشوارترین مشکلات جهانی تبدیل کند، نه ابزاری برای فشار و اعمال اجبار علیه کشورهای مستقل.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/459469" target="_blank">📅 17:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361d2a31cc.mp4?token=VsMBDx1kQRudZzrcR6j3Lw6MOCfUX3rG5g4k0C_FdigZQIHFKgx1cu5Zz6eb6qkcgG9a92D2cH-NPIOs6cRsrBDXFNPsiFvKhcyssUAsEvpwjlPoBakFyrevbD2_fLAOvrIYzq7QiUZYJh-WNxIRrs9SNGSaNpJ6zd-8jMqXyzzm7VbagDGiBsYK8dzL_iDIhYeIu8mnQbiyLUs8mTOWgWG0F0p6bZw7qZ1zOexVf9WNWqlh9hSKExJ98unlj47t_mjN7p6Hw6wnjXswJWaaMiasxiWFE9UU_VUrQJb6TU5tV5ZldKVRGF2kaue60tpI-M8TmIIWGk4xGp0ZB4kyHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361d2a31cc.mp4?token=VsMBDx1kQRudZzrcR6j3Lw6MOCfUX3rG5g4k0C_FdigZQIHFKgx1cu5Zz6eb6qkcgG9a92D2cH-NPIOs6cRsrBDXFNPsiFvKhcyssUAsEvpwjlPoBakFyrevbD2_fLAOvrIYzq7QiUZYJh-WNxIRrs9SNGSaNpJ6zd-8jMqXyzzm7VbagDGiBsYK8dzL_iDIhYeIu8mnQbiyLUs8mTOWgWG0F0p6bZw7qZ1zOexVf9WNWqlh9hSKExJ98unlj47t_mjN7p6Hw6wnjXswJWaaMiasxiWFE9UU_VUrQJb6TU5tV5ZldKVRGF2kaue60tpI-M8TmIIWGk4xGp0ZB4kyHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: دولت و مجلس مصمم به افزایش کالابرگ، مخصوصاً برای دهک‌های ضعیف جامعه هستیم و در اولین فرصت اجرایی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/459468" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e37edd23f.mp4?token=Ug-1Z6d0Lm1cwuP3ftgPAliJDewwTVR6Na-OiD3KLMlZ23gsCX78Rfv2hS0wsm9NP2HTnzshJ_jkUDO_BAZLJVebzDXnOAoFxhPAzGLLwpSQb6JYtJZL-zC2PaxAf5gbXv52vysMTRJvcqvSYGkLW6T4hmWOYnfUo-vu8QW-U8KH5SncSp35ZjObdfI3QteL9t1KzmER6ezvieGcWtlC2MeFFTJyc4-NLcvfdvtMHygGnpq4VJkoqo_WmPegjdXUnaFwObYM3ZYt2cW0R3nXcuaoJxB8s1m-UAagmAdilG6dYGA9b9RTznbkOQ75sixPYQHHgbpDNTaURl3id3Pgzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e37edd23f.mp4?token=Ug-1Z6d0Lm1cwuP3ftgPAliJDewwTVR6Na-OiD3KLMlZ23gsCX78Rfv2hS0wsm9NP2HTnzshJ_jkUDO_BAZLJVebzDXnOAoFxhPAzGLLwpSQb6JYtJZL-zC2PaxAf5gbXv52vysMTRJvcqvSYGkLW6T4hmWOYnfUo-vu8QW-U8KH5SncSp35ZjObdfI3QteL9t1KzmER6ezvieGcWtlC2MeFFTJyc4-NLcvfdvtMHygGnpq4VJkoqo_WmPegjdXUnaFwObYM3ZYt2cW0R3nXcuaoJxB8s1m-UAagmAdilG6dYGA9b9RTznbkOQ75sixPYQHHgbpDNTaURl3id3Pgzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: اگر محاصره را تشدید کنند، حتماً پاسخ نظامی می‌دهیم و همه ضرر خواهند کرد
🔹
اگر دشمن اراده‌اش بر این باشد که ما از خلیج فارس نفت صادر نکنیم، هیچ‌کس نخواهد توانست نفت صادر کند.
🔹
دشمن در حال حاضر در جنگ اقتصادی، بر روی جنبه روانی آن متمرکز شده است.
🔹
بخش زیادی از تحریم‌های اعلامی جدید، قبلاً نیز اعمال می‌شده است.
🔹
محاصره دریایی در قوانین بین‌المللی، یک اقدام نظامی محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/459467" target="_blank">📅 17:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRHUFlXgpbN9sRI-BwuZmy683IOghiYotcRd2gCK-QWOXNyMB2ENEzt4HB_mVuJ70LGnntizVK70TpZWKXKi1wSVfIBpnvLzzICdXDytnSS7QXM1wiIrBWn3I-_-kF2BkttwXpS55oSZbtwa6AZEGJZ3jFtfjE1nB0yX91aE3l3QcK49ghzS5EtIcK81KsZX63CIpRNHtGE2NmnKrISewyk0FIi3fo3fzDQrhBbVmaAIT0KnW9TZF4_ErYPTRR5pR6eRNOwqiNNR3xxztHsZVEflOBEaRXJ1gj5NsMic__fYkqy0PfFr8UwzZQRFwO3v5yvUp9bR3lfhJtMwTWjFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
گسترش پوشش ارتباطی ایرانسل در روستاهای آذربایجان شرقی
🔸
ساکنان سه روستا در شهرستان‌های اهر و هریس آذربایجان شرقی، با بهره‌برداری از دو پروژه ارتباطی، به اینترنت پرسرعت ایرانسل، دسترسی پیدا کردند.
🔸
همزمان با برنامه‌های هفته دولت، پروژه‌های ارتباطی روستایی ایرانسل با حضور استاندار آذربایجان شرقی و معاونان وی، نماینده مردم تبریز، آذرشهر و اسکو در مجلس شورای اسلامی، مدیرکل ICT استان، مدیران استانی، جمعی از خبرنگاران و با حضور آنلاین معاون حقوقی و استان‌های وزارت ارتباطات، در محل اداره کل ارتباطات و فناوری‌اطلاعات آذربایجان شرقی به بهره‌برداری رسید.
🔸
پروژه ارتباطی ایرانسل در روستای یاورکندی با اعتبار ۱۸۱ میلیارد ریال به بهره‌برداری رسید و ۱۱۰ خانوار و ۳۴۱ نفر را به شبکه ارتباطی و اینترنت همراه ایرانسل متصل کرد.
🔸
همچنین سایت ارتباطی ایرانسل در روستای هیق با اعتبار ۱۷۰ میلیارد ریال راه‌اندازی شد و روستاهای هیق و هفدران با ۸۰ خانوار و ۲۶۵ نفر را تحت پوشش شبکه ایرانسل قرار داد.
👈
جزئیات بیشتر:
https://irancell.ir/b/331330/ahar-heris-rural-site-inauguration-1405
@irancellnews</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/459466" target="_blank">📅 17:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVIH4Cygxq-P4kDNPKAJRn9ocQ4H9qjL9Yna0XxYJxR3nUOz5Z6i0byB1jWckel2rNcqCf3FLVpcTogN1v1hPrfwWJoMSuRhRKU__cTy7Zf3uHqgdhQ-KE2UaQw8UVImAHiLOB6ZUkC1JeCWwJ7MYvmV2V_b9ZLQTd3OxkiRmQ8mokGNwyjKeMUDYSGDXKXPr89KRY5v1HETSDGA5dmq5_zfSyvk67Lgimi3jCn3MJc97NZpkaoaeeoZ30lfzXVyGOEbIqbD_lqMNYAl0otOztwmW2q-KRbzKMQw47JD5okjPHfwPwiTViqix8qBqZlFRSClCe784KSq0A1sTuRYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
رونمایی از کارت اعتباری گردشگری ریالی و ارزی بانک رفاه کارگران با حضور وزرای رفاه و‌ میراث فرهنگی
🔹
در راستای رونق صنعت گردشگری و با هدف فراهم‌ کردن امکان دریافت و استفاده سریع از کارت‌های اعتباری گردشگری ریالی و ارزی، بدون نیاز به مراجعه حضوری، سامانه صدور آنی این کارت‌ها، توسط بانک رفاه کارگران رونمایی شد.
🔹
مراسم رونمایی از این سامانه به عنوان نخستین سامانه رسمی صدور کارت‌های مذکور در کشور، با حضور دکتر میدری وزیر تعاون، کار و رفاه اجتماعی، دکتر صالحی ‌امیری وزیر میراث فرهنگی، گردشگری و صنایع دستی، دکتر للـه‌گانی مدیرعامل بانک رفاه در محل این بانک برگزار شد.
🔹
این سامانه در راستای تسهیل پرداخت‌های بین‌المللی و پاسخ به نیاز کاربران برای خریدهای اینترنتی ارزی و ریالی، پرداخت هزینه سرویس‌های آنلاین و استفاده از خدمات جهانی، توسط شرکت دانش رفاه پردیس از شرکت‌های زیرمجموعه این بانک در بستر پلتفرم Payval راه‌اندازی شده است.
🔗
متن کامل خبر
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/459465" target="_blank">📅 17:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/459464" target="_blank">📅 17:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d849a033.mp4?token=Qcz9TFfxx4MNUyhLE51RBdAxCNM_DCGc8mNgI206DJ_cSe2o2PDlWwyP8B5k7V9S4DfK72AleXqcjY8CiqGIW2Y5OihjT_fu5mAhCxJpahybCn-IPgZ4zXwyBMdwLQXwoyFrFYblW82m9yNaJkcJ5eeX1UTP57eCHgAV5WeSD2coL98FQvt2SvLJTw9qDtSm6NPbNlzWRbwIaXINfDuKmsWH8FQ1MJobZN9pP-d53lSY6tozrVD2DzUw1UoVQiB9qEf6M0j3hui44zXSrvObVotRmMkzfQIO1TLsYnHlk2symQ5XiG1Qghdfgji4mY57a_S7cQu16eCIAKmc92V0Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d849a033.mp4?token=Qcz9TFfxx4MNUyhLE51RBdAxCNM_DCGc8mNgI206DJ_cSe2o2PDlWwyP8B5k7V9S4DfK72AleXqcjY8CiqGIW2Y5OihjT_fu5mAhCxJpahybCn-IPgZ4zXwyBMdwLQXwoyFrFYblW82m9yNaJkcJ5eeX1UTP57eCHgAV5WeSD2coL98FQvt2SvLJTw9qDtSm6NPbNlzWRbwIaXINfDuKmsWH8FQ1MJobZN9pP-d53lSY6tozrVD2DzUw1UoVQiB9qEf6M0j3hui44zXSrvObVotRmMkzfQIO1TLsYnHlk2symQ5XiG1Qghdfgji4mY57a_S7cQu16eCIAKmc92V0Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاهدها و وثیقه‌گذارهای حرفه‌ای در قوه قضائیه شناسایی می شوند
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/459463" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82abd9d8a2.mp4?token=rXfJccqkgr88QhNPVqnCxcyL1DStZIunNJ76TlmSFf2J90PuLkrpugK7Oaw0spURmG09dLGDksSpwTmCLS7piE0ParxStkv0ab19ou5LkSSLAFaLz20VdoJGGbHT86cWdTN0vUmBTGTc9dhyCRIgrOM8EZLr_3LbZfSr4tEXR8_nKkwAxGoGC_MONzrMhROmqL-GA4WJkX35f5EM8YPATOBGi9pgy4VGUi3iax1fxzeUZ8To5eRQnNgIJmQEQk9b_YDjBrWrjIY5MkJFr0t6hTvD7Lg4CmIP-Y-7QaXnRTmMQ4K7dwLjk0w87u7_UvG8uFzgCKlmp7h3mZZRmpcahA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82abd9d8a2.mp4?token=rXfJccqkgr88QhNPVqnCxcyL1DStZIunNJ76TlmSFf2J90PuLkrpugK7Oaw0spURmG09dLGDksSpwTmCLS7piE0ParxStkv0ab19ou5LkSSLAFaLz20VdoJGGbHT86cWdTN0vUmBTGTc9dhyCRIgrOM8EZLr_3LbZfSr4tEXR8_nKkwAxGoGC_MONzrMhROmqL-GA4WJkX35f5EM8YPATOBGi9pgy4VGUi3iax1fxzeUZ8To5eRQnNgIJmQEQk9b_YDjBrWrjIY5MkJFr0t6hTvD7Lg4CmIP-Y-7QaXnRTmMQ4K7dwLjk0w87u7_UvG8uFzgCKlmp7h3mZZRmpcahA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: امروز همه، چه مسئولان و چه مردم، باید دقت کنیم در زمین دشمن بازی نکنیم
🔹
مردم در همه صحنه‌ها نشان دادند پیشتاز و پیش‌قراول بودند و دشمن هیچ‌وقت نتوانسته است از مردم ما سوءاستفاده کند.
🔹
باید فرصت سوءاستفاده را از دشمن بگیریم. با برنامه‌ریزی‌های انجام شده و همراهی مردم از این جنگ سخت عبور می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/459462" target="_blank">📅 17:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6df48cd02.mp4?token=LfHvDN36KptRJsqrzgAQRXI3iBv5FiFusgFbyh0p-6rqFko6U2_gkpJgsIbDo21aCxKqWiLExaJPP6LwRLQWYSLqDJi4M1-TkWPHF7bNCDc5DynGcxCR4NVxRsdVEwyIKnJtiVObjL-M-Pvlk93aFsX-LLehgD1UNJb2WZGTCjr3DeI0OpSNMOb7YhVF3PxDIPySkcCUDrUPhue2WBzKP_L3EJPKMyIUCez9JkDwbYyJyuzNe2uGap1lMWxz6FESpVgUuY7PWyAkC7v0esMYiL0CVM0Yo-TEO67ZL5O6f_V02I-O7d3mX1esRZMj7fXXqbDACqKOVsTolf9U_VQkG6FNbtaIAxEzuKTVe1N5tk0m1-zbFRwzP88nlmeQxV2x8jBhzg6F32FjVeTv62mZw09urT3EwD5Zq5LxZWJiX7Tg4B92i8lnDZ9ixH5GoIAOm6EUs2BpFCnX5q1GJJ_JAG9ms65SyWeSxTc4cbQ8EOPTE47Q4_JLf4Pm0q8iFra2C2xuGFEHiDylmL3bsidoDSmgdIWVVqJRW1BfuF31dDKIhGcCaVMSX4e5YdbgRs8flO_fJ6NyBLlVTW4tEE7QDBUvlnYbczclRbK3C7SYrLYfJSoh9UAkW1AFcFQeHw2k9sSAccDmfh82FTsgtjsTK0bo1paQSh86Jox0A3955pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6df48cd02.mp4?token=LfHvDN36KptRJsqrzgAQRXI3iBv5FiFusgFbyh0p-6rqFko6U2_gkpJgsIbDo21aCxKqWiLExaJPP6LwRLQWYSLqDJi4M1-TkWPHF7bNCDc5DynGcxCR4NVxRsdVEwyIKnJtiVObjL-M-Pvlk93aFsX-LLehgD1UNJb2WZGTCjr3DeI0OpSNMOb7YhVF3PxDIPySkcCUDrUPhue2WBzKP_L3EJPKMyIUCez9JkDwbYyJyuzNe2uGap1lMWxz6FESpVgUuY7PWyAkC7v0esMYiL0CVM0Yo-TEO67ZL5O6f_V02I-O7d3mX1esRZMj7fXXqbDACqKOVsTolf9U_VQkG6FNbtaIAxEzuKTVe1N5tk0m1-zbFRwzP88nlmeQxV2x8jBhzg6F32FjVeTv62mZw09urT3EwD5Zq5LxZWJiX7Tg4B92i8lnDZ9ixH5GoIAOm6EUs2BpFCnX5q1GJJ_JAG9ms65SyWeSxTc4cbQ8EOPTE47Q4_JLf4Pm0q8iFra2C2xuGFEHiDylmL3bsidoDSmgdIWVVqJRW1BfuF31dDKIhGcCaVMSX4e5YdbgRs8flO_fJ6NyBLlVTW4tEE7QDBUvlnYbczclRbK3C7SYrLYfJSoh9UAkW1AFcFQeHw2k9sSAccDmfh82FTsgtjsTK0bo1paQSh86Jox0A3955pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند
🔹
نقشۀ دشمن برای همه مسئولان ما روشن است.
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/459461" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459460">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fd2a26f4.mp4?token=WOcLz1FLcxlEQERsnnnRbaeBEIEObo7yCk2OZra426NqSiSqTstcWtn5SebJvs52EpMPEe5kcU4xHNqPUnbel8WyvjqfW2AbO0x4P3XmHffHxqpX9SBLeji3UEMhyzh_JwRva9Ep7CiRNuMQmUGvmMLIC4GPLG7v34EueydHFBf24F3b3P3gtm-TVO8WwX4HVCx8AskzSbD2mYJhLwBplTkK7h1CQ_Gu3grkMgj6NzrjU9pJag-OFFuO4_LDByRYDEKyTWrLavUpwNsBK40T4CK1zAoQkAjCCUXTgyK7m-ViE3eY6RWXwWYraFnGgT0JVeK-4qdroiFMzY9XOOtmZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fd2a26f4.mp4?token=WOcLz1FLcxlEQERsnnnRbaeBEIEObo7yCk2OZra426NqSiSqTstcWtn5SebJvs52EpMPEe5kcU4xHNqPUnbel8WyvjqfW2AbO0x4P3XmHffHxqpX9SBLeji3UEMhyzh_JwRva9Ep7CiRNuMQmUGvmMLIC4GPLG7v34EueydHFBf24F3b3P3gtm-TVO8WwX4HVCx8AskzSbD2mYJhLwBplTkK7h1CQ_Gu3grkMgj6NzrjU9pJag-OFFuO4_LDByRYDEKyTWrLavUpwNsBK40T4CK1zAoQkAjCCUXTgyK7m-ViE3eY6RWXwWYraFnGgT0JVeK-4qdroiFMzY9XOOtmZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: قدرت نظامی ایران در تنگهٔ هرمز حفظ شده و ارتقا پیدا کرده است
🔹
اعمال مدیریت ایرانی بر تنگه، هیچ منافاتی با قوانین بین‌المللی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/459460" target="_blank">📅 17:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459459">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cdaf5608.mp4?token=aux-c5f57C3wYfQ30QyHIHym2KxpFQ9JMVLBKVV4lh56dkRSUEZE0upwIcyuWQ53b4n7ZbbPqRD8cB1VzAVU5bUE6TgU8FQsoHxCcZoCKR6P_J5i300oCrgQbiulUzRt_k6fZ2FO7mIzUZdG5NGgPGyqkz4HzpjGij6iksiFkZKCo3i7P8ae-eIzzqcnvkO1be2_W13A-KbnvmG9ljE6O0EQh7ZAsXPxprXmchIWLRPAbXI_8fV097hE269eHuhCxLkcFrLVLf5kcUcvqaj7MYVl1bY55CRU9B04dWzb0Tve8FSI43AYYaTHOZCMJZuwavhPOPlohAXbIKVMGKY6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cdaf5608.mp4?token=aux-c5f57C3wYfQ30QyHIHym2KxpFQ9JMVLBKVV4lh56dkRSUEZE0upwIcyuWQ53b4n7ZbbPqRD8cB1VzAVU5bUE6TgU8FQsoHxCcZoCKR6P_J5i300oCrgQbiulUzRt_k6fZ2FO7mIzUZdG5NGgPGyqkz4HzpjGij6iksiFkZKCo3i7P8ae-eIzzqcnvkO1be2_W13A-KbnvmG9ljE6O0EQh7ZAsXPxprXmchIWLRPAbXI_8fV097hE269eHuhCxLkcFrLVLf5kcUcvqaj7MYVl1bY55CRU9B04dWzb0Tve8FSI43AYYaTHOZCMJZuwavhPOPlohAXbIKVMGKY6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد
🔹
قبل از جنگ، روزانه حداقل ۱۲۰ کشتی از تنگه هرمز تردد می‌کرد و حتی اگر یک یا ۲ کشتی هم از تنگه عبور کند، به‌هیچ‌عنوان قابل مقایسه با قبل از جنگ نیست.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/459459" target="_blank">📅 17:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a06fa7c6.mp4?token=L-pi8zca8esFsR1BzC0jZDtOflEdGG2QKJfVdXcHJc4B0QkduWwKMLB144c0YWWMahdVv5jv7qEzPUnuErxDwJZy1fBlfDg2Yvzo4gR80WNqH4bfKhnJK8vPB_qzuTg0BDMz1IXuhcfkwC5uw523tLOch6kltqwFeJ3ZXROtu9Qetdb6Z6r8Taz_HjD72L-GXanlW4HNHG1RGVz17tRcl0S7jw_xiRRyKATgkIekT42bmd1ghuNTVyv-gQ5uMDrI37NAEywzrohQSOxtKe3N_A5wkqicQQPnYGGygVUrSCXWTvKEo5SCjJsbOKtGulCo8aA_Hq99Npt08uXOPr7pF2ZQ4MJajvvAr7vpudOsYo4ky04NpFwQRsmyMr5f6keys9tNW_HyrUS8YK92CavsNIk_XyisYLG1lJLOIW_lZStsYeA50pJH1ijMB9n1gtNIvSBatmPCbjWqc36NqfJzZ5ZgEfda6NbJEeeG5qmYOX_E3B6HVOLpyufzDONWYtK-8wjC7UAePZa3kdQt4U7O-vsiTIsnwVRikiAVPiVoM9zHFSscD-t5Acnwz4YDgN4WXk3sWMFyFWFYeW-Tj4ih1aOzKmQIzb8ZJfiCVlqgJO4hnS2CSvTy0kEPu0ewdaeaJ0ZRDeXFp5EoXuTouJQqu9O76EIBurkw1B5aX948dyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a06fa7c6.mp4?token=L-pi8zca8esFsR1BzC0jZDtOflEdGG2QKJfVdXcHJc4B0QkduWwKMLB144c0YWWMahdVv5jv7qEzPUnuErxDwJZy1fBlfDg2Yvzo4gR80WNqH4bfKhnJK8vPB_qzuTg0BDMz1IXuhcfkwC5uw523tLOch6kltqwFeJ3ZXROtu9Qetdb6Z6r8Taz_HjD72L-GXanlW4HNHG1RGVz17tRcl0S7jw_xiRRyKATgkIekT42bmd1ghuNTVyv-gQ5uMDrI37NAEywzrohQSOxtKe3N_A5wkqicQQPnYGGygVUrSCXWTvKEo5SCjJsbOKtGulCo8aA_Hq99Npt08uXOPr7pF2ZQ4MJajvvAr7vpudOsYo4ky04NpFwQRsmyMr5f6keys9tNW_HyrUS8YK92CavsNIk_XyisYLG1lJLOIW_lZStsYeA50pJH1ijMB9n1gtNIvSBatmPCbjWqc36NqfJzZ5ZgEfda6NbJEeeG5qmYOX_E3B6HVOLpyufzDONWYtK-8wjC7UAePZa3kdQt4U7O-vsiTIsnwVRikiAVPiVoM9zHFSscD-t5Acnwz4YDgN4WXk3sWMFyFWFYeW-Tj4ih1aOzKmQIzb8ZJfiCVlqgJO4hnS2CSvTy0kEPu0ewdaeaJ0ZRDeXFp5EoXuTouJQqu9O76EIBurkw1B5aX948dyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: دشمن بداند در دوره‌های بعدی جنگ، هم در بُعد کیفی و هم کمی، مسلط‌تر خواهیم بود
🔹
نیروهای مسلح از هر فرصتی که به آن‌ها بدهیم برای بازسازی توان خود استفاده می‌کنند و حتی ساعت و لحظه‌ها را هم از دست نمی‌دهند.
🔹
امروز ایران بیش از دشمن توانسته توان…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/459457" target="_blank">📅 17:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mG1sdYUFTks3eH-Tnb9DES5sH3N0bN8Bw2SVlW5MtL3ejUnuTARopgWEPmdO87nRJg0u_2BZ034WHkglVexaDJnjmm4WX53pUsme2PQBMhJpy41BSdk01ALRP6QZWmn2SlZLn0qPcfyKM6q3IaETEaOqzDICVjeJV0FYvnYFh4SLqvMTJUbqI7qD0NDjPoHNTHg6YfYijoFX5f7Q9mbg9y6KxIGGTbOF2IMjj8uL5CRVV0RYuLjJDIuUwpVpQ0rreHzkFHF08TekLbYFfD3LmQ4KJlo8_-u0WfsU8a6T_1YqrXU4323B5ixj5wl6VH7u_xoppO29AS4SzQfzeri-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دیدار پزشکیان و پوتین در بیشکک
🔹
در دیدار رئیس‌جمهور ایران و روسیه آخرین وضعیت روابط و مناسبات دوجانبۀ دو کشور بررسی شد و طرفین دربارۀ راه‌های تقویت و گسترش همکاری‌های مشترک در حوزه‌های مختلف گفت‌وگو کردند.  @Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/459456" target="_blank">📅 16:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c051d5e2.mp4?token=JrPYbmqYgQHTf8nVLHdr2Y080Z19Iz0iFUA_yUXkMAgvmf3N2vpfk8RQURrFRkEG3WDiB7kBzHI1gCcevIqbxOfJNk_GdUV57-1rVzS7EosVwi7Vj1m8DZg77i9nFO-edGAEoK3qLBhx0B-Qb8YyGM9c09MZ_iJiXdw5amBuGNWHQZ9WQkkh_wYLj8ZQ5NOMG0lvpk0EJQ5hKK5BYYI9T9he8QCWUxEsWbw8PX7q-A6EiEVoJBezpkhq0p_v_163hBbbcGhiDVSt8otfFdfp9ZxqE5m4GismBsKTk9PTUW7rTpyD5ir8QXdwJ6qlrUyrnRp2YDRyGzewxcxvAlqiEXJFvQx4T27RH6yPOd_3S4wzCm6qQ3QEvIjUd7Z0fo8QOaU-M4Bu-xxEqdbziqMK_Pdhod0xAvCkjuHznSUa8KYuGFbtCi8djJvC0GUEKSyyxHPYjdoaVUVgPF_nyo_QD6Ir4zvA4TtkGi7jFdCP-gFJumrIN9F2rqcDBefNQn6NBgCa6Smy31-JmUhDsD6JgqNs3N1JoFG_WWbXhADiFKFxMYYhvj0KiCnNPXGjFA97PPZmD8jMNy1-RV0rbuK_1xBBVO04kvDR5Kf4HAVXx6idUUP0qmnUWbPGNqw0S_Bd3PRe-PryMtrPovXsQHJnRYujYbBfxqucwcGM46uWdUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c051d5e2.mp4?token=JrPYbmqYgQHTf8nVLHdr2Y080Z19Iz0iFUA_yUXkMAgvmf3N2vpfk8RQURrFRkEG3WDiB7kBzHI1gCcevIqbxOfJNk_GdUV57-1rVzS7EosVwi7Vj1m8DZg77i9nFO-edGAEoK3qLBhx0B-Qb8YyGM9c09MZ_iJiXdw5amBuGNWHQZ9WQkkh_wYLj8ZQ5NOMG0lvpk0EJQ5hKK5BYYI9T9he8QCWUxEsWbw8PX7q-A6EiEVoJBezpkhq0p_v_163hBbbcGhiDVSt8otfFdfp9ZxqE5m4GismBsKTk9PTUW7rTpyD5ir8QXdwJ6qlrUyrnRp2YDRyGzewxcxvAlqiEXJFvQx4T27RH6yPOd_3S4wzCm6qQ3QEvIjUd7Z0fo8QOaU-M4Bu-xxEqdbziqMK_Pdhod0xAvCkjuHznSUa8KYuGFbtCi8djJvC0GUEKSyyxHPYjdoaVUVgPF_nyo_QD6Ir4zvA4TtkGi7jFdCP-gFJumrIN9F2rqcDBefNQn6NBgCa6Smy31-JmUhDsD6JgqNs3N1JoFG_WWbXhADiFKFxMYYhvj0KiCnNPXGjFA97PPZmD8jMNy1-RV0rbuK_1xBBVO04kvDR5Kf4HAVXx6idUUP0qmnUWbPGNqw0S_Bd3PRe-PryMtrPovXsQHJnRYujYbBfxqucwcGM46uWdUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: دشمن بداند در دوره‌های بعدی جنگ، هم در بُعد کیفی و هم کمی، مسلط‌تر خواهیم بود
🔹
نیروهای مسلح از هر فرصتی که به آن‌ها بدهیم برای بازسازی توان خود استفاده می‌کنند و حتی ساعت و لحظه‌ها را هم از دست نمی‌دهند.
🔹
امروز ایران بیش از دشمن توانسته توان نظامی خود را بازسازی کند.
🔹
ضرباتی که بعد از آتش‌بس به پایگاه‌های آمریکا در کشورهای مختلف زده شد، معنای راهبردی داشت.
🔹
میدان را در دست داریم و این دشمن را به این نتیجه رساند که نمی‌تواند جلوی موشک‌های ما را بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/459454" target="_blank">📅 16:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942ac8dee3.mp4?token=rncw7qoZGswcg01cMvpWFACbZAseGMzbCvSG5bkTpF24Yo1BZ8lohcxa5a7_AW6ldjkcAK_Q-v1dEhk2orZYeHpHyTTVpjUcjfL4546slaEs-ZUALsvrisrXOuyHlneRbcmgHYKB83sBVABCa2LrHnW92ElXeVhy6mbVlzSnAQIoeiBJPBBGFVOl1qegYYgmtnJdXBiWw8nERk_YxRYjGzKGRrxH2YoEnIit6Z6a5vqf7iRYjHJvhXgZiwurmSPYw8Ov4m2z7WkfU_fBL30tiM_ifX6Nj5A6bnnWm2OUae1ypDkFWYtzWvlXqn1ACAB2CE5bpU1tqt-e2osuoaKanjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942ac8dee3.mp4?token=rncw7qoZGswcg01cMvpWFACbZAseGMzbCvSG5bkTpF24Yo1BZ8lohcxa5a7_AW6ldjkcAK_Q-v1dEhk2orZYeHpHyTTVpjUcjfL4546slaEs-ZUALsvrisrXOuyHlneRbcmgHYKB83sBVABCa2LrHnW92ElXeVhy6mbVlzSnAQIoeiBJPBBGFVOl1qegYYgmtnJdXBiWw8nERk_YxRYjGzKGRrxH2YoEnIit6Z6a5vqf7iRYjHJvhXgZiwurmSPYw8Ov4m2z7WkfU_fBL30tiM_ifX6Nj5A6bnnWm2OUae1ypDkFWYtzWvlXqn1ACAB2CE5bpU1tqt-e2osuoaKanjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: از فرماندهان شجاع و همه نیروهای مسلح تشکر می‌کنم و در برابرشان سر تعظیم فرود می‌آورم
🔹
گاهی انتقاد برخی فعالان رسانه‌‌ای در مورد فرماندهان نظامی را می‌شنوم و برای مظلومیت آن‌ها افسوس می‌خورم.
🔹
در زمان سکوت میدان، کارخانه‌ها، نیروها و بخش‌های مختلف نظامی درحال استراحت نیستند و همۀ خود را آماده می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/459453" target="_blank">📅 16:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef5fe4842.mp4?token=vTp2xTnSjPXX_qqloYUMjLreXUpl2_G8naW8nOO4fIIyqAvRA1hw5Qgv23yQ0CsF6S84vfDz03zDFxJQKFCmex7M97KN-jD8lMBaFdXWWUAg2lHdqWtbFX8w55LKNg8f3rfMv-Ihdb5SYT-SNR4y8eq8OlrIx3zCVWVDNfBZ3UNWjfYagQ28AXRewbcjlVHMM2TJKJXkpvEVN_b2D3MR4J1soQIws3pZbOnETsJyQXb-U51BOnhcHYCpj9sb4eg74QZt6OflF0THvFBM4Goc5I7sqZuLZV1q_dbcO7-XKS9m-LdWPoNXWha804I1yZFfClrMo27J0GrQbsgFOFen67Q7_yzx4-KXpqQtwR8USqpLrrYyC08yDfP5u0Q1FRHEszh4XU0cHJyLS6RnXfTW47dtk8A5L6zGhQN6PfnBbdIkKN_nYkSACoaVdoydc3IEP_wqhqGo6iXpmUR7PoEFweZW-MFVhFodzjpSbXVk2krGd1Ivtf69wheWcl5Axydy7PdTzFJhPbsw2ACmbASOTMpAjfN-oDMBVECchR5CnR8WLY8eurf3IsdTVv2zGcQQ5NAAw-S9Cv-dfAwKMAJRf_E8q9HUxv0ycr1pYrGfIFJjn0If0OLErfj978Y48EJ8BIS3wHgeCOHrMsiAk7_mYCtn7BL9RAndHL0V_a4HU3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef5fe4842.mp4?token=vTp2xTnSjPXX_qqloYUMjLreXUpl2_G8naW8nOO4fIIyqAvRA1hw5Qgv23yQ0CsF6S84vfDz03zDFxJQKFCmex7M97KN-jD8lMBaFdXWWUAg2lHdqWtbFX8w55LKNg8f3rfMv-Ihdb5SYT-SNR4y8eq8OlrIx3zCVWVDNfBZ3UNWjfYagQ28AXRewbcjlVHMM2TJKJXkpvEVN_b2D3MR4J1soQIws3pZbOnETsJyQXb-U51BOnhcHYCpj9sb4eg74QZt6OflF0THvFBM4Goc5I7sqZuLZV1q_dbcO7-XKS9m-LdWPoNXWha804I1yZFfClrMo27J0GrQbsgFOFen67Q7_yzx4-KXpqQtwR8USqpLrrYyC08yDfP5u0Q1FRHEszh4XU0cHJyLS6RnXfTW47dtk8A5L6zGhQN6PfnBbdIkKN_nYkSACoaVdoydc3IEP_wqhqGo6iXpmUR7PoEFweZW-MFVhFodzjpSbXVk2krGd1Ivtf69wheWcl5Axydy7PdTzFJhPbsw2ACmbASOTMpAjfN-oDMBVECchR5CnR8WLY8eurf3IsdTVv2zGcQQ5NAAw-S9Cv-dfAwKMAJRf_E8q9HUxv0ycr1pYrGfIFJjn0If0OLErfj978Y48EJ8BIS3wHgeCOHrMsiAk7_mYCtn7BL9RAndHL0V_a4HU3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش رگباری باران در روستای اردلان در منطقهٔ سراب آذربایجان‌شرقی
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/459451" target="_blank">📅 16:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedd8d3229.mp4?token=bk3jgTPBWzi1V81zXX1i3lODiUCWOZ2-j1sdBl0FhLtN3hl0ksvir-v8QtqCM5zCYFahR7J4tN3T_05zwRpXGg7DlH0IHQbWc3cxLLJxEttfL6kX7qtNtkozO50BDHhvsAVPeEViDbueeA5gA8lcMpRADLDQWTX80A6OI7myrQlkovaZtt_yhy3nFAY7300cNlFj7NBtZYFX7YTj3p03-ikYkqG_GsXZZyIi0OKxNwD-ZB6AWFT7BG1Lji-qEnb2XzK03B55LI-uxZsZn21A-d08SBFnmJD_5L_sfs0up9xzI0ZtUm_S_BfKNPk4Ht1otH46bHKU3yw-zCYrX_LtKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedd8d3229.mp4?token=bk3jgTPBWzi1V81zXX1i3lODiUCWOZ2-j1sdBl0FhLtN3hl0ksvir-v8QtqCM5zCYFahR7J4tN3T_05zwRpXGg7DlH0IHQbWc3cxLLJxEttfL6kX7qtNtkozO50BDHhvsAVPeEViDbueeA5gA8lcMpRADLDQWTX80A6OI7myrQlkovaZtt_yhy3nFAY7300cNlFj7NBtZYFX7YTj3p03-ikYkqG_GsXZZyIi0OKxNwD-ZB6AWFT7BG1Lji-qEnb2XzK03B55LI-uxZsZn21A-d08SBFnmJD_5L_sfs0up9xzI0ZtUm_S_BfKNPk4Ht1otH46bHKU3yw-zCYrX_LtKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در ۱۵ ماه گذشته، به اندازۀ یک دهه پیشرفت در حوزۀ نظامی داشتیم
🔹
در هر دورۀ جنگ، بهتر از دوره‌های قبل عمل کردیم و جنگیدیم. فرآیندهای بازسازی و تقویت توان نیروهای مسلح در بخش‌های آفندی و پدافندی، به بهترین شکل درحال انجام است‌.
🔹
این اقدامات به دلیل بومی‌بودن فناوری ماست و جوانان ما این کار را انجام می‌دهند و دست نیازی به‌سمت دشمن نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/459450" target="_blank">📅 16:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIT_xl4T6moNL9Q1QJdJCd0K3q9HmkR-POxGyyDuAVs4YmsXU3g0vesFtMAnE589ky4isTaoHiPtB8hUzrkXGpJ0C98O-7rhwYs9srqbkBh9vf5UER3YC287M3ovWLLE4pBpRTSSmWOfY0keEiQi9g-p1KZXD1pzDPEbs0EiLzPrNtOjckUp14-LkPiYrEXzBpqG0fzBxP0PCIAMws52Oc0P5tdQC5om1pbFBkXtBwqGwnSTWWCwT8uXPNEo3ZLQDzcXOXno8Q4MgZR3KY8GpSaC3M7PkRwMu2vKkazD98o-3tDCPYFnCYKxv1fwz0BJOYnoMYuVLrsTJvYPVFPUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آدان در آستانۀ بازگشت به استقلال
⚽️
بسته‌ماندن پنجرۀ نقل‌و‌انتقالاتی استقلال و بازگشت خلیفه به آلومینیوم باعث شده تا باشگاه استقلال دوباره به سراغ دروازه‌بان اسپانیایی فصل گذشتۀ خود برود.
⚽️
طبق شنیده‌ها مذاکرات با آدان مثبت بوده و قرار است مطالبات این بازیکن…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/459449" target="_blank">📅 16:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmvn_0n_4gozkYpdKBfDQLwjPOSVfLgsC_S7ADYSOH_TlQ71CAO7RTu2m9ilruA-aM_LHGZszV3l4xSRBZ39UCccSr0bhZ4SwTGNmh8BNIWPcWVdK4dECA3AM_tVvO0GRO0DtbrTwrYKPxBzESTV2Ic9D_WBAjFTvQ3R5FS2J5kycthERKghVflqJ7ytfSv2NG95GbHg9O2j7r97nlMALRP4xakHuvoVfGjxD2NpQWCIEgGHQF96w_TIQsEkHBG7vElNobtisWUC8D8iVrQLblnBZKPKYFt4zENZED9QAT4gTQIvASms9Hu-dKyUyW8yLmiRchXAO26tc3KnWAQ3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: هر هفته ۱۰۰ مگاوات نیروگاه خورشیدی افتتاح می‌کنیم
🔹
امروز در صنعت برق در وضعیت بسیار خوبی قرار داریم و بیش‌از ۱۰۲ هزار مگاوات ظرفیت نیروگاهی در کشور وجود دارد.
🔹
تا پایان سال، ظرفیت نیروگاه‌های کشور افزایش خواهد یافت و امیدواریم این رقم به‌حدود ۱۲ هزار مگاوات ظرفیت جدید نزدیک شود.
🔹
هر هفته ۱۰۰ مگاوات نیروگاه خورشیدی افتتاح خواهیم کرد و توسعهٔ این نیروگاه‌ها با جدیت در دستور کار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/459448" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRmM-zXoFsx8PXj5tWtnis5AbAtTPrYqJruO46rusdTg6rViGl8sCYjjCnfcie6MBrfXvTgrz4CPy4PMEQU7B7z6HRCFsZkfs3rW_VpAyemTe-0TpdvifH71JSaPu1VXMPchKT2u9Cf57TPQL_h5iuq_TDBz01IOcLH-B64D1HNLZ4osfQrV4kyzK1n91DEK0WJW7RUFnDgfvy6sSvabC3XYHtjjrAae5TK6FAyzPU-gLiK7HGKxQAACWlaB7CzZUoElHv4P2A8Hv-Rv1ldMR8L9eLgczDix9nQkEC23BkrJ9ZoLxvHftwJ7hs-Ymu45pTXLOO2CDp5r6IVJx05OCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط آزاد محبوبیت ترامپ؛ جنگ با ایران، عامل مهم نارضایتی‌ها
🔹
محبوبیت رئیس‌جمهور آمریکا با ادامه‌یافتن جنگ ایران در سراشیبی سقوط قرار گرفته و این بار به پایین‌ترین حد خود، یعنی ۳۲ درصد رسیده است. این در حالی است که دونالد ترامپ خود را جزو بهترین روسای جمهور تاریخ آمریکا معرفی می‌کند.
🔹
براساس نظرسنجی انجام‌شده توسط دانشگاه ماساچوست و مؤسسه یوگاو، قریب به ۶۴ درصد از شرکت‌کنندگان در نظرسنجی، عملکرد ترامپ را تأیید نکرده‌اند. ۵۴ درصد از این رقم را افرادی تشکیل می‌داده‌اند که «به‌شدت» از عملکرد دوسالهٔ رئیس‌جمهور کشورشان ناراضی بوده‌اند.
🔹
بر این اساس، ۶۸ درصد از پاسخ‌دهندگان گفتند که رئیس‌جمهور آمریکا جنگ با ایران را به‌خوبی مدیریت نمی‌کند. تنها ۲۵ درصد از افراد شرکت‌کننده معتقد بودند که این جنگ تا حدودی یا بسیار خوب مدیریت می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/459447" target="_blank">📅 16:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCroZ5OH65vzGu0hkKiM-30DkBQzaxs1QsjojbCsYvFqsbMB8l9eMUoaq0hxlgxrpKO1bACK16rYnHdUcFE_dNdE31BffSsXVqp-EYda0kgzRCLDX94hKX6kUWf4Uta9GPY5Fbg4dpSTAaWsMebjy5UxxkFz5mih-PRliV2RHU4pStIrVYixlwI0qJbQF0KoDbKvTsCznjMEZ_A6gylQkJIMEZxh3LZnai0p-ndizmowKA93OgwhW7wP_zHlPqE73CYSlvS4fpnqwqaoQUdHN16Qew0oDhFBkE-f0Q0BmuM6BssEhSzjAsWrK1Ou_9DvtNfN3pxs6pz_748vc1h4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبض یک میلیاردی گاز برای برخی از تهرانی‌ها
🔹
مدیرعامل شرکت ملی گاز ایران: در برخی نقاط تهران قبض یک میلیارد تومانی صادر شده است.
🔸
زراعتکار، معاون وزیر نفت، پیشتر اعلام کرده بود که از این پس یارانهٔ پنهان مربوط به استخرهای آب گرم ویلاها در زمستان پرداخت نخواهد شد و این مشترکان مشمول اصلاح تعرفه‌های گاز خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/459446" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236434ed71.mp4?token=aRUo4QYvizUzq3dtiBchzosf7dbzVCpAOGd0as5yjF6KZYXbKKMjsW5NYW7GzOusC_fILISgqldVMzktIEw9nh0vcYsBxkTKb6nBj6uxvx5AqWvEuq3g1LrgHGseyEL5l3t73zSYAYE3rVN31gSqME02dyRZaJUoegWP903o21N_cSi0cEvU1lXGnGys7wUBrt6A7OZNDFimwOWsHPLgfa2-gz45hcphiCP5ycF267OhZtPlIxRIOSrhT0jq8SuYkMB7iJa7ktXEynJASbBOrskc9Yaf6kfcxsj4EQScK-iqUcR4Jyp-fM0eG0sxI7SaINMlrRC4GyNuRz6bS4nm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236434ed71.mp4?token=aRUo4QYvizUzq3dtiBchzosf7dbzVCpAOGd0as5yjF6KZYXbKKMjsW5NYW7GzOusC_fILISgqldVMzktIEw9nh0vcYsBxkTKb6nBj6uxvx5AqWvEuq3g1LrgHGseyEL5l3t73zSYAYE3rVN31gSqME02dyRZaJUoegWP903o21N_cSi0cEvU1lXGnGys7wUBrt6A7OZNDFimwOWsHPLgfa2-gz45hcphiCP5ycF267OhZtPlIxRIOSrhT0jq8SuYkMB7iJa7ktXEynJASbBOrskc9Yaf6kfcxsj4EQScK-iqUcR4Jyp-fM0eG0sxI7SaINMlrRC4GyNuRz6bS4nm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان و پوتین در بیشکک
🔹
در دیدار رئیس‌جمهور ایران و روسیه آخرین وضعیت روابط و مناسبات دوجانبۀ دو کشور بررسی شد و طرفین دربارۀ راه‌های تقویت و گسترش همکاری‌های مشترک در حوزه‌های مختلف گفت‌وگو کردند.  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/459445" target="_blank">📅 15:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00444557cc.mp4?token=fK8m93_AnBFHCU55NCJHfbjHc5X0hWcil41Uxv4QZYtloSPVgJzEEsjd6l6ucUFm5Ko4xDN5aOAwq99aiOTQBKlK0E5qGgaEuIusr1koIW_nYv0yCdgf9dx-tRepbrEFmG4kjsOgvlX4lDQ4NiiYxYfnWJohLJHuaHdgYkPEcf2Z_KlOka83NH6TXs57SLMN3EvbklUvUWyVEGr4N02aeurJ_hwwIqAFhI8Bz8Z3v4riNAYE14CWyPEjSUy342LQ2pCoETM1LBg9c5iBKyQajij4gLF0CaCJFOY4_uGk-5IpBBKGEUgQJ5jJqzPO5ZpYtAzR45SvKL2F6dVF_acOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00444557cc.mp4?token=fK8m93_AnBFHCU55NCJHfbjHc5X0hWcil41Uxv4QZYtloSPVgJzEEsjd6l6ucUFm5Ko4xDN5aOAwq99aiOTQBKlK0E5qGgaEuIusr1koIW_nYv0yCdgf9dx-tRepbrEFmG4kjsOgvlX4lDQ4NiiYxYfnWJohLJHuaHdgYkPEcf2Z_KlOka83NH6TXs57SLMN3EvbklUvUWyVEGr4N02aeurJ_hwwIqAFhI8Bz8Z3v4riNAYE14CWyPEjSUy342LQ2pCoETM1LBg9c5iBKyQajij4gLF0CaCJFOY4_uGk-5IpBBKGEUgQJ5jJqzPO5ZpYtAzR45SvKL2F6dVF_acOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا برای راضی‌کردن کشورها به همراهی با جنگ اقتصادی علیه ایران هیچ منطقی ندارد
🔹
هیچ کشوری که اندک ارزشی برای حقوق بین‌الملل و حقوق بشر قائل باشد با آمریکا همراهی نخواهد کرد. ذات اقدامات آمریکا علیه ایران غیرقانونی و غیرانسانی است.…</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/459444" target="_blank">📅 15:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b03b0b9c.mp4?token=XmbgdziCtsz7E-8QzXCpk0wGfcLBoddd0Od-Pe83qXne3hanWddD5tCTonLCeO9DMhtSofiZj8gW4Z0U2oNObpB0puXbWjXCXluKrmuNv4N7WWE_5Yrwt3_nIbDYzZKp02N9rIyFpsi-_U0DDY5EcsK1LtiFPMK6WeNSrRnuYGmYtU2n4qfOhipzkljyq1_aK4p-GxStYFuchANGWP6znTY5z7pr_uRW26TvS1PJN5kJVPosBbGjqLTUtF7kzU38d9062FRy7AGcI0t5MkKPNT9Ew2QDkhvKeG8k6C4OIb-Q38CpIgMywI2Bkrpfn5ZjlwVbtHkA1z0oRoBu8jsgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b03b0b9c.mp4?token=XmbgdziCtsz7E-8QzXCpk0wGfcLBoddd0Od-Pe83qXne3hanWddD5tCTonLCeO9DMhtSofiZj8gW4Z0U2oNObpB0puXbWjXCXluKrmuNv4N7WWE_5Yrwt3_nIbDYzZKp02N9rIyFpsi-_U0DDY5EcsK1LtiFPMK6WeNSrRnuYGmYtU2n4qfOhipzkljyq1_aK4p-GxStYFuchANGWP6znTY5z7pr_uRW26TvS1PJN5kJVPosBbGjqLTUtF7kzU38d9062FRy7AGcI0t5MkKPNT9Ew2QDkhvKeG8k6C4OIb-Q38CpIgMywI2Bkrpfn5ZjlwVbtHkA1z0oRoBu8jsgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا در جنگ با ایران دچار فرسایش شده
🔹
آن‌ها هر بار برای فرار از واقعیت یک دروغ جدید منتشر می‌کنند. افکار عمومی آمریکا از رفتار دولتمردان آمریکایی خسته شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/459443" target="_blank">📅 15:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ffa0cfa1.mp4?token=qS-dxijoNffE7FRBZHhxQvaO2vK6x1868zvT11k7uUxIf0MYUoUvUhefrS1ZTSM_J1Dt8U-b4WsuwnOfTpreb5toHQ6deAXMnn855wJA1966coO3Y0Ui3eTlwYzmtsE6oo9hUBi_KlCfAFy2ESoa2IGW6DLDDv5KIBD7UdKzoLF6jxZMCg76L0MHtepsZQqt4ZVJ9chCpdP0Vv752V1cVqaVggTF_xNmyxhl3WWkGnZwec-hEP8RLTBjPF7AF_pYiEqfBerWrwQOiah-fTnmD86ibh0n6xydJA0WU6kGXIUJXHiT3hXRpaviQJCHk33Q51o3S_A_JGEAc1kV3ojVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ffa0cfa1.mp4?token=qS-dxijoNffE7FRBZHhxQvaO2vK6x1868zvT11k7uUxIf0MYUoUvUhefrS1ZTSM_J1Dt8U-b4WsuwnOfTpreb5toHQ6deAXMnn855wJA1966coO3Y0Ui3eTlwYzmtsE6oo9hUBi_KlCfAFy2ESoa2IGW6DLDDv5KIBD7UdKzoLF6jxZMCg76L0MHtepsZQqt4ZVJ9chCpdP0Vv752V1cVqaVggTF_xNmyxhl3WWkGnZwec-hEP8RLTBjPF7AF_pYiEqfBerWrwQOiah-fTnmD86ibh0n6xydJA0WU6kGXIUJXHiT3hXRpaviQJCHk33Q51o3S_A_JGEAc1kV3ojVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکرهٔ جدیدی با آژانس نداریم
🔹
صحبت‌هایی که دربارهٔ فعالیت‌های هسته‌ای در محل‌های جدید از جمله کوه کلنگ مطرح می‌شود، تحت‌تأثیر سیاست‌های برخی کشورهای عضو این آژانس است. @Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/459442" target="_blank">📅 15:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e569594ee.mp4?token=RgTud1SGsgxBCDXwQL2S6RAzDMjGlIXHFHDvmHkBsRL9M_digqohXO7vQ0JiPnfEasV3FsOqlJDg2Fwo4QN94NfTKsumgdToXqlZsFN_NjhYhh0_5WfrYHVlRY_4sYr3UBEgsuyi0p6-xlpMMqiEvBiHuDUc1jwpi0bPFBdmpPNczQNsxKTSKvqKIxEYrySr7nnW222TPI8g8k1G8w0qm6hwMsoKtavbl0qIioQ7j1EejAn_GXQAaRqbJHYjf4Ql8Ktz64KDGLOzlhY8usyEJTICXw8DUI-ATSnF93YRFr42BAwWFhPmBUdQ14tRzqMK0Bsqy9fF4pOJfT3wFbSu7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e569594ee.mp4?token=RgTud1SGsgxBCDXwQL2S6RAzDMjGlIXHFHDvmHkBsRL9M_digqohXO7vQ0JiPnfEasV3FsOqlJDg2Fwo4QN94NfTKsumgdToXqlZsFN_NjhYhh0_5WfrYHVlRY_4sYr3UBEgsuyi0p6-xlpMMqiEvBiHuDUc1jwpi0bPFBdmpPNczQNsxKTSKvqKIxEYrySr7nnW222TPI8g8k1G8w0qm6hwMsoKtavbl0qIioQ7j1EejAn_GXQAaRqbJHYjf4Ql8Ktz64KDGLOzlhY8usyEJTICXw8DUI-ATSnF93YRFr42BAwWFhPmBUdQ14tRzqMK0Bsqy9fF4pOJfT3wFbSu7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخت ۹۰۰ ساله ارس ملی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/459441" target="_blank">📅 15:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d08d933a1.mp4?token=at2JQhHWn0kPKp2PA6irekm9ZS1wSw9HKQk6SgSJkqCC_MJNz0gwZuSR3nJPwpACKRVwSzB32f-i5z2g3YtY3PsSD5rvHCrQ_wJXJOl_ptdTLfS2U95C_r1D44o-RfQ9EDzc6758Qxe_nDc3CpsVHsxEquZw87T7uGgr0BZu_ouDDmbp7UqPVCdpt0qERPSE-dHf-PTX655xnzqj7-XZdWyIg1PTSPHWROkT1iPDdx3RFtG53eUyjZg50wYyQ3isu1mt66UXxFiEECMV0cO9minnwZXdNjrFo_Et6fEVEHVS08Gf3Sn7wDEIu5BMqyzHB-hcg7hXxmsgjCSdjwuyug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d08d933a1.mp4?token=at2JQhHWn0kPKp2PA6irekm9ZS1wSw9HKQk6SgSJkqCC_MJNz0gwZuSR3nJPwpACKRVwSzB32f-i5z2g3YtY3PsSD5rvHCrQ_wJXJOl_ptdTLfS2U95C_r1D44o-RfQ9EDzc6758Qxe_nDc3CpsVHsxEquZw87T7uGgr0BZu_ouDDmbp7UqPVCdpt0qERPSE-dHf-PTX655xnzqj7-XZdWyIg1PTSPHWROkT1iPDdx3RFtG53eUyjZg50wYyQ3isu1mt66UXxFiEECMV0cO9minnwZXdNjrFo_Et6fEVEHVS08Gf3Sn7wDEIu5BMqyzHB-hcg7hXxmsgjCSdjwuyug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش سخنگوی وزارت خارجه به تحریم آزمون زبان توسط آمریکا: آن‌ها علم، دانش، فناوری و تمدن ایران را هدف گرفته‌اند
🔹
اگر ادعای آمریکا برای نگرانی دربارهٔ موضوع هسته‌ای ایران واقعی است، یک آزمون دانش‌آموزی یا دانشجویی چه ارتباطی با موضوع هسته‌ای دارد؟! @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/459440" target="_blank">📅 15:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc92b272a.mp4?token=EHnUdkwzpWDfPRFoowMOcO7e7z-xllN5Z7DKEjXfiHzarqYaSjQXaqSPGiOygYI6Z0qbZh9p4gMEmvJES8L2RJrbi-ss7yTPxkioPxvS4RpAYZUukib7RL-W_HeRgfVeeRBghuQ55lLxxjTSlCvAuqKxrIA5SdR40mj15fOojUaFSwNkHxl7I5xpfTsz_JGZCG30oxRKPP5HAvFtxTt5p21IwqsfNko6eh4dc-edD1HKaOEuhGBqyIN7uqsepIGKNg9osee6KE4-WUPpvBGmuUul1Gt2JoRZDZNle0bWl0pGzrRGkCtsFm7JGrz5fmWdhEqwhlGQGFS5jfSrdBbm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc92b272a.mp4?token=EHnUdkwzpWDfPRFoowMOcO7e7z-xllN5Z7DKEjXfiHzarqYaSjQXaqSPGiOygYI6Z0qbZh9p4gMEmvJES8L2RJrbi-ss7yTPxkioPxvS4RpAYZUukib7RL-W_HeRgfVeeRBghuQ55lLxxjTSlCvAuqKxrIA5SdR40mj15fOojUaFSwNkHxl7I5xpfTsz_JGZCG30oxRKPP5HAvFtxTt5p21IwqsfNko6eh4dc-edD1HKaOEuhGBqyIN7uqsepIGKNg9osee6KE4-WUPpvBGmuUul1Gt2JoRZDZNle0bWl0pGzrRGkCtsFm7JGrz5fmWdhEqwhlGQGFS5jfSrdBbm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز پزشکیان اولین مهمان اجلاس سران شانگهای بود  @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/459438" target="_blank">📅 15:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfPMwDg8ez_qT2II3-Gqt32zuG02mIYx3LjSDf8ihKiWEDm2NCFMGSaGrC9EWngxTDFGKYdzo4mHZMEouAPE-ZibPQa81rSY9koqAIV_O94QZfbpk_IZG7MO2EgClevaUjDm4XoJpe2qy0KNR21Oim4rxS9sQW8_GQEQCaB5vULGtyyv2Sx_xIkCZXXUfHpfXwOy5MS7hTENPDF_arVWv4goWwtc_OOKH8v6qMZwyakuQC5CQm6WiiR9amSgLzb32BBFjJst37xOwWatX9SMPxZXdiIT4cBj_wfzDEnF3xQtVmm6pQtyrNrGbrN2dA4EKZGcz43CxpqUMSQq8qCaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفتیان رکورد کشوری خود را تکرار
کرد
🔹
در نخستین روز از مسابقات دوومیدانی مردان قهرمانی کشور در شیراز، حسن تفتیان در فینال مادهٔ ۱۰۰ متر با ثبت زمان ۱۰.۰۳ ثانیه رکورد ایران که دست خودش بود را تکرار کرد و قهرمان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/459437" target="_blank">📅 15:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1409465bb9.mp4?token=sYUZsJ-afdyBLsLvP9yADVn1z5tqz-eEWSZE0QPtDCYjK9_WBvaXpP_RR-UknCuN4CxYISLjMzLyEf350GbVzOEWcj-BwCJSLNxboDdKIK9oWGdjdF25i3TndhUdXbDO8HkEKuZwQxyf-mEAZ3w0KDGd6BSXBVMEmeivpeiQWrlWAMXp4C8omOiPBWXm6IRw2ed6LhWq7tfLe4WjLi54pskE-EauWFFDqpjcwlwjw_NFQte82imQGk-b82I0xekmPRXD6UstC3gyffm-ZYb3MZ-z-KKroY_WqqGINtW9RLjfrLl6KEMz-jeCf7D2FYSEoo5octQeyBs1EL_wp7tXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1409465bb9.mp4?token=sYUZsJ-afdyBLsLvP9yADVn1z5tqz-eEWSZE0QPtDCYjK9_WBvaXpP_RR-UknCuN4CxYISLjMzLyEf350GbVzOEWcj-BwCJSLNxboDdKIK9oWGdjdF25i3TndhUdXbDO8HkEKuZwQxyf-mEAZ3w0KDGd6BSXBVMEmeivpeiQWrlWAMXp4C8omOiPBWXm6IRw2ed6LhWq7tfLe4WjLi54pskE-EauWFFDqpjcwlwjw_NFQte82imQGk-b82I0xekmPRXD6UstC3gyffm-ZYb3MZ-z-KKroY_WqqGINtW9RLjfrLl6KEMz-jeCf7D2FYSEoo5octQeyBs1EL_wp7tXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: در تفاهم اسلام‌آباد آمریکا مرتکب نقض تعهدی شد که در بالاترین سطح هیئت حاکمه امضا کرده بود.  @Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/459436" target="_blank">📅 15:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459435">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHsEIbSKCcogIGC7pkoz-a27nWriBFKkVb7vUFqeLhMy-1TjZ39Tu3eIhcQmDEzob4Vis2rRWeD2Fm_S1k4_jmXuctpvj4aTDhQ6_MENUY0XzKzJau3N9fNlP1VGCu8c4ixDt5UD1Fka05hloWKbhC9iP64wSSoh4BGZ8KzfY7oxc_aiYhsJUT9xZrN9ufasuJB7zaxYI-g0hEllW437JwaesiqfKZCbV6yTqQDfRA3g7txcwROo0MUBy_6pwnSR7y3SlkR46ipsYn8irCbEQVQvLu4OzoYmT8gUorSlt5CAYSyom0W839JP8vJF05aoO84b57kc_F2UM477r9pnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: نیازهای نیروی پدافندهوایی را به فناوری و فناوری را به قابلیت دفاعی تبدیل می‌کنیم
🔹
سردار ابن‌الرضا: روز پدافند هوایی، یادآور مجاهدت مردانی است که در خط مقدم دفاع از حریم آسمان ایران اسلامی ایستاده‌اند.
🔹
نیرویی که در جنگ‌های تحمیلی دوم و سوم از نخستین و اصلی‌ترین آماج حملات دشمن بود و رزمندگان آن با ایمان، شجاعت، صلابت و دانش، از امنیت آسمان کشور دفاع کردند.
🔹
آنچه امروز در این نیرو به کار گرفته می‌شود، حاصل پیوند نیاز میدان، دانش نخبگان و توان صنعت دفاعی است؛ زنجیره‌ای که باید با شناخت تهدیدهای جدید، همواره در حال ارتقا و نوآوری باشد.
🔹
صنعت دفاعی کشور خود را موظف می‌داند در کنار رزمندگان پدافند هوایی، نیازهای این نیروی راهبردی را به فناوری و فناوری را به قابلیت دفاعی تبدیل کند و با اتکا به جوانان و متخصصان ایرانی، برای تهدیدهای امروز و فردای کشور آماده باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/459435" target="_blank">📅 15:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459434">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2815123322.mp4?token=OtDAOhTC04wBmKRGurWuTVnDcnKevM1C17MZxqLHfGo9K3fXRivrz3JudOtzwgtZ3L9mKCeNfdkNEoCO1XudnreFSTqSZoLEOSZMprZ7kpCuYIQZ65H-ixKpiq5E5X5e0v-ArkNhUkvvEpGKNTsqKJ8VI4KrOiQz_AKkn1DnAbxwClzyfqLETVZDQ7Xp2yhLJmwVuXqcutuJkw73grUgIKFmR7rN3xBWSBe7UH3H82j-_kpXYp9m7IxipHdr6E_R6JPO8J0X0t5qilgQE326qrPYxldf4_PX2ZRmcV87EcG26fFXP-jeh3VEO5SBTe01N6pQUmpm8d1ltjUkEi-0zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2815123322.mp4?token=OtDAOhTC04wBmKRGurWuTVnDcnKevM1C17MZxqLHfGo9K3fXRivrz3JudOtzwgtZ3L9mKCeNfdkNEoCO1XudnreFSTqSZoLEOSZMprZ7kpCuYIQZ65H-ixKpiq5E5X5e0v-ArkNhUkvvEpGKNTsqKJ8VI4KrOiQz_AKkn1DnAbxwClzyfqLETVZDQ7Xp2yhLJmwVuXqcutuJkw73grUgIKFmR7rN3xBWSBe7UH3H82j-_kpXYp9m7IxipHdr6E_R6JPO8J0X0t5qilgQE326qrPYxldf4_PX2ZRmcV87EcG26fFXP-jeh3VEO5SBTe01N6pQUmpm8d1ltjUkEi-0zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز برداشت انگور پیش‌رس از ۲۸ هزار هکتار باغات تاکستان قزوین
🔹
پیش‌بینی می‌شود امسال بیش‌از ۴۰۰ هزار تُن انگور از این باغات برداشت شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/459434" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459433">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fc73ac55.mp4?token=iD3ozy04D0sOkGT6t6qsHpceT9OA0rLTF9tV-zQ0K4z_XR8eM_G4r8JaZjw4EpPGULowaTfkEMYEsd2x8ttcowekZ_D7xuRb7iyg58URRO-baNcGj82TNzgXPDJWRgvLzMcBD8bkh2C3hYW8DZDRF4ItOfaa7QMIqKWCxusEHbWF05vfMJ9z1VMLy23l1ayX5Ksncf1F6Yx8JVKBL9tQgQ6N-IsUZrROgHaeJZ081IAzp8kQ82BMPMiDJSiTE3XAsNMR42UFgmK2kR_2hoxFNlMZPafy9wS1kMkD0YnxeVi3DfRccTOt5OL_W1320CnmTBIJAn8nsF39Nksyf4z5tTNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fc73ac55.mp4?token=iD3ozy04D0sOkGT6t6qsHpceT9OA0rLTF9tV-zQ0K4z_XR8eM_G4r8JaZjw4EpPGULowaTfkEMYEsd2x8ttcowekZ_D7xuRb7iyg58URRO-baNcGj82TNzgXPDJWRgvLzMcBD8bkh2C3hYW8DZDRF4ItOfaa7QMIqKWCxusEHbWF05vfMJ9z1VMLy23l1ayX5Ksncf1F6Yx8JVKBL9tQgQ6N-IsUZrROgHaeJZ081IAzp8kQ82BMPMiDJSiTE3XAsNMR42UFgmK2kR_2hoxFNlMZPafy9wS1kMkD0YnxeVi3DfRccTOt5OL_W1320CnmTBIJAn8nsF39Nksyf4z5tTNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح‌های جدید دولت در ۸ استان به‌بهره‌بردرای رسید
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/459433" target="_blank">📅 15:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d6ce48f1.mp4?token=SvtqsWwMdSDy72sDXbsBAEs9ZviFto2-3BbuqNyGBgn1U-ds-UeMS-qkCanH1CQEKx2PWpSovb39JnbLVH7Zfg76-aCGwkUx86xivn4C8waL1RN1KJ4V8zxE9ycSiruI-cAVdkmejolJDmSRwEwaRD30A-u95TtodBn24MbzpUkIbGCRURj5neTkHSDPLZW03yreUI767XOWSII7JdWDWjhgC1TkQFAN42L0qOF8rm7RaSk-WxDJmPu_Z04Sc5ojsLAhq_h_m_jz3d_c-jw3WhCPMOq8ZhSx_4rnaWQeSzApCdWnO0IN_-7SWe5Ku-csuCM7cp8Z-VrxmKMaTUfbDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d6ce48f1.mp4?token=SvtqsWwMdSDy72sDXbsBAEs9ZviFto2-3BbuqNyGBgn1U-ds-UeMS-qkCanH1CQEKx2PWpSovb39JnbLVH7Zfg76-aCGwkUx86xivn4C8waL1RN1KJ4V8zxE9ycSiruI-cAVdkmejolJDmSRwEwaRD30A-u95TtodBn24MbzpUkIbGCRURj5neTkHSDPLZW03yreUI767XOWSII7JdWDWjhgC1TkQFAN42L0qOF8rm7RaSk-WxDJmPu_Z04Sc5ojsLAhq_h_m_jz3d_c-jw3WhCPMOq8ZhSx_4rnaWQeSzApCdWnO0IN_-7SWe5Ku-csuCM7cp8Z-VrxmKMaTUfbDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت. @Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/459432" target="_blank">📅 15:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=alFCG_bmlBojoMLdeZ-Xqy9G020xBBZsadFTdzeXn5-VHhyy6TD24l0nfsIWJWabcs4eVZXdRndta8Jy2pRK34aYLB-sW16q4oDGmJXLJKRz290-g8NIK6PniyPuces_jj_3iQX_QIfvHfNGk-Ns7MTcrE2-2MxmBuzaM023MP19THmbk3XaViX8ySwDLL6COHTC9xcRsIEXTLe6JEwT4PYO1Kg7GUOYJwe9NzU3DkgEjDW1Phkh3IpTUV8ARYEhRQpE00Tq9b536xzezWKUWCZNQn7SzWg6miDh2xLBg58iBdkh2DiMPvxibEVfmjGTVaotJHwIGkVhA-FBtS-_ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=alFCG_bmlBojoMLdeZ-Xqy9G020xBBZsadFTdzeXn5-VHhyy6TD24l0nfsIWJWabcs4eVZXdRndta8Jy2pRK34aYLB-sW16q4oDGmJXLJKRz290-g8NIK6PniyPuces_jj_3iQX_QIfvHfNGk-Ns7MTcrE2-2MxmBuzaM023MP19THmbk3XaViX8ySwDLL6COHTC9xcRsIEXTLe6JEwT4PYO1Kg7GUOYJwe9NzU3DkgEjDW1Phkh3IpTUV8ARYEhRQpE00Tq9b536xzezWKUWCZNQn7SzWg6miDh2xLBg58iBdkh2DiMPvxibEVfmjGTVaotJHwIGkVhA-FBtS-_ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/459431" target="_blank">📅 15:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGz8IIKGGNZYz6EfTRjqakZ3uL4-3lNonyz5k0lQf3TYUWuHiW9lef4sOGnndUB-OlV25J69L-EU7HsSoKGE1Q9FeRkAfV-fJ5aqdZRC-4sjDbfVX2ePyZ5T9a6EcfSTHpl6rqSAOFiLONb3-q_U52RpagYEt_9IRaMsHfFE2zOht93THi2FGBs40VtIDXn13xVpjVvhyqlN3R5FndqryXb1dpIiGcGh_oQIDN2x8HyruRlKvP2ZyX5mkd5gJGqyawqzz5unzobI-UVHvnEujOAa7LfNT-qKgJ4E1rIr_osNa3ziKAWPOn_d5aAAtWhhi3-OfWpv-gGhBjTz7WuUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بسیج اساتید دانشگاه آزاد: وزیر علوم با مسئولان حاضر در نشست حاشیه‌ساز برخورد کند
🔹
شورای تبیین مواضع بسیج اساتید دانشگاه آزاد اسلامی در نامه‌ای به وزیر علوم، نسبت به قبح‌شکنی و ترویج هنجارشکنی در نشست مدیران ارشد این وزارتخانه با نمایندگان شوراهای صنفی دانشجویی…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/459430" target="_blank">📅 14:58 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
