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
<img src="https://cdn4.telesco.pe/file/piD4lcIqYLobH8lH4Y7HkE_clKNZ6ybcG2Y1CwbQjhNN05YyuJN6If-r9CxZsi5V5_VmQqCgi-CV3pmOA0bCibVZ0H2hctQMHBAEHafqb0q2srCP0HzYinBh4SWyxmkt0WGbawyRKo1R1TjawOwKvxFyOhoQ8M-cGkWpFG2E9fsMm8JouzJoc4mmnbhxK9wEiWVQk4-fW7FpffzPGPc0oQsLH0JHbQL3vS2OGJR9llZdWAd_oos1Bp4eAUFtfL2PRKGGMOlUp2IlW4UrdhngFe_J54wGbEp4q-svt_InxqBGqah_VDUFx1ila9l9nqC-vWMMHpjyyxSNzfzYu2012Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-72477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مذاکرات ایران و آمریکا بدجور گره خورده، آمریکا به دنبال اینه که مستقیماً بره سراغ مسائل هسته‌ای، ولی ایران همچنان رو تنگه گیر کرده، این در حالیه که آمریکا می‌گه تنگه بازه و ما مذاکراتی در مورد تنگه و رفع محاصره انجام نمی‌دیم  بنظرم یه دور جنگ و ترور رو در…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/news_hut/72477" target="_blank">📅 18:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه #hjAly</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/news_hut/72476" target="_blank">📅 18:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">معمولاً تو اسرائیل وقتی نخست وزیرِ وقت بخواد تصمیم مهمی بگیره، رهبرِ حزب مخالفش رو هم به یک جلسه امنیتی دعوت می‌کنه، و امروز نتانیاهو از لاپید، رهبر اپوزیسیونِ حزب خودش دعوت کرده به جلسه بیاد؛ احتمالاً این جلسه امنیتی در مورد ایرانه
#hjAly</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/news_hut/72475" target="_blank">📅 18:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ برای بار هزارم:
ایران به سلاح هسته‌ای دست نخواهد یافت و آن‌ها در وضعیت بسیار بسیار بدی قرار دارند و به‌شدت در حال شکست خوردن هستند. این ماجرا خیلی زود به پایان خواهد رسید.
این وضعیت خیلی خیلی زود تمام خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت.
قیمت نفت درست همان‌طور که قبلاً بود، به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/news_hut/72474" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
در سال‌های پیشِ رو، وقتی تاریخ کشورمان را می‌نویسند، خواهند گفت که ماجرای ایران یکی از مهم‌ترین کارهایی بود که ما انجام دادیم.
در واقع، این یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/news_hut/72473" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: «اخبار جعلی» را فراموش کنید. حالا می‌خواهم آن‌ها را «اخبار مصنوعی» بنامم. از این عنوان خوشم می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/news_hut/72472" target="_blank">📅 18:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfnz4HNhCjmpCOQ3YDYodkdKKaSPx6cmFT4vIpXLBQIPbHANjAoKv4z99SaQ6wZo9ljVlN7eiyoYnnURAyQ9-HEiaPWSAKGKg9ssluGR8WjCMA5-1QN6rr9yqfpUXozB4iam7k8dB_FMni15bQSx6tcpD0iaFc5r1FVFZgqj3I1DDASCmM8ohuujdDLOi3GNXdNvk-8EXhorhE49vmDdkp8kUapbtvNmbJ4qGIy67vZrk9jSa9ZslCrTy3p6Ch5EJUGpdDyhZXVAk0b_nxPQEHGL-ijJSuW8xWSJvkRx3FordrXAOTKiwlQqoAUtKj4ZGsxc83AYwTc1ZtdzfJSeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا در حال اعزام ۶فروند جنگنده اف-۱۶ به خاورمیانه!
@News_Hut</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/news_hut/72471" target="_blank">📅 17:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=Iq5-XhIunpSXenUYOogNYzok9MWeRTsDSd4w2kIDMYbjXL9QOa5r0VsVmR6cJjkSmqeS_bJM0XBZDUN_R0aYdYOPXVY5IZ-iEr6O-QHTPLG_7pPL_w15ApqOLg85024eJVskA1pjAd51Iy5zBeFQKklVePZwb7WeePm-z5lXUzpW0yqIKHmZuKAIDj_66tHAvNleMftVIbsRNz73W2UyvoipOkca7EguHDzD4_sF8f5O0T4T19EPNBqyrrBz6GqsYXqFB9oiMyxDmI7UczfHx_ELulTprEvxQRCzQ7HIk0ABjCwQBV1lGsHRaAZDyuc9r4DbwhrOEZG0DLsQLXKXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89765f99e7.mp4?token=Iq5-XhIunpSXenUYOogNYzok9MWeRTsDSd4w2kIDMYbjXL9QOa5r0VsVmR6cJjkSmqeS_bJM0XBZDUN_R0aYdYOPXVY5IZ-iEr6O-QHTPLG_7pPL_w15ApqOLg85024eJVskA1pjAd51Iy5zBeFQKklVePZwb7WeePm-z5lXUzpW0yqIKHmZuKAIDj_66tHAvNleMftVIbsRNz73W2UyvoipOkca7EguHDzD4_sF8f5O0T4T19EPNBqyrrBz6GqsYXqFB9oiMyxDmI7UczfHx_ELulTprEvxQRCzQ7HIk0ABjCwQBV1lGsHRaAZDyuc9r4DbwhrOEZG0DLsQLXKXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌های غیررسمی میلی گلد دفتر رسمیش رو جمع کرده و دیگه پاسخگوی ملت نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/news_hut/72469" target="_blank">📅 17:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72468">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=vF7dys553mADbG9R95g86UT59vO0vj4kNgnYV9VlKcdsmTWAL-nULPrWLg7H4y_yB27-v_bRUKty5Y_sfixpI08Lj9z5b7YYNyPbhftyETkljKUfLaAIKmlgsBIbia2SL_hwE49nWuohKta_xJE4OZl2t6-B7seGNpBUVmqTGksOO_tATAosDC2Iok7wLIeH9G65WSXNscTQUJ8WwJFstcubgN-0tuDh0Sv1lreE5J-Wei1Mq0iKffMDALUI92tpwJzaMi0eaxCQJmMRIh_fr1aL3rrx8WuOCC7ajEjWKvmBQQJawxfhga6Xcb9bZ_2TfsjdRJLGxP2A6IrIgI5A1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=vF7dys553mADbG9R95g86UT59vO0vj4kNgnYV9VlKcdsmTWAL-nULPrWLg7H4y_yB27-v_bRUKty5Y_sfixpI08Lj9z5b7YYNyPbhftyETkljKUfLaAIKmlgsBIbia2SL_hwE49nWuohKta_xJE4OZl2t6-B7seGNpBUVmqTGksOO_tATAosDC2Iok7wLIeH9G65WSXNscTQUJ8WwJFstcubgN-0tuDh0Sv1lreE5J-Wei1Mq0iKffMDALUI92tpwJzaMi0eaxCQJmMRIh_fr1aL3rrx8WuOCC7ajEjWKvmBQQJawxfhga6Xcb9bZ_2TfsjdRJLGxP2A6IrIgI5A1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور:
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/72468" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72467">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
نشست نتانیاهو در ابوظبی گسترش یافت و نمایندگان ۱۰ کشور را در بر گرفت:
امارات متحده عربی، اسرائیل، عربستان سعودی، ایالات متحده، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر.
ابتدا دیدار دوجانبه میان نتانیاهو و «محمد بن زاید» (MBZ) برگزار شد و سپس سایر مقامات به آن پیوستند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72467" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=nZeOONta0P0JJsLWF2qBAef1XKO8uVHPOwrj6E6K5Tv3z9RaNKSvVsjy0FhIICOa1d2lA7MK25uFXSJaqo2AFQEaweadPOqSwN8sfD8gHOziWgbptHvJ_yLxkxLbQAJzuM1w6CfeBCJcV7UQyhrWWzHBzps6kSGLgrnUvgQ3wWD7GADwyhABQdH-KZw2T0gg7dRdaB7Qrk7_U3FQFkiGzR763MWgvj4dwfVdioh2Rey9eHJiD_gAIrOIhOdsR-B6vh03JTP0vvu3prAo5FM64SdB-vNm1pwVJtqwL6uuGfntWN0cn59f9qdypcc7CKBjxDi2Lfj6TFY2e6cZA5DYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4e41635.mp4?token=nZeOONta0P0JJsLWF2qBAef1XKO8uVHPOwrj6E6K5Tv3z9RaNKSvVsjy0FhIICOa1d2lA7MK25uFXSJaqo2AFQEaweadPOqSwN8sfD8gHOziWgbptHvJ_yLxkxLbQAJzuM1w6CfeBCJcV7UQyhrWWzHBzps6kSGLgrnUvgQ3wWD7GADwyhABQdH-KZw2T0gg7dRdaB7Qrk7_U3FQFkiGzR763MWgvj4dwfVdioh2Rey9eHJiD_gAIrOIhOdsR-B6vh03JTP0vvu3prAo5FM64SdB-vNm1pwVJtqwL6uuGfntWN0cn59f9qdypcc7CKBjxDi2Lfj6TFY2e6cZA5DYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل:
جزایر تنب بزرگ، تنب کوچک و ابوموسی در خلیج فارس، جزایری متعلق به امارات متحده عربی هستند که تحت اشغال ایران قرار دارند.
ما تداوم اشغال این سه جزیره توسط ایران را به‌طور کامل رد می‌کنیم.
هرگونه تلاشی برای جلوه دادن این موضوع به عنوان یک مسئله داخلی ایران، تغییری در این واقعیت ایجاد نمی‌کند که این‌ها سرزمین‌های اشغال‌شده هستند و نباید تحت حاکمیت ایران باشند.
+کص ننت:)
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/72466" target="_blank">📅 16:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72465">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=c_4snMCXl2FpKqR7oEJA7dWTJuR_UNCJveZOgRNXZkURQG25eC-64QVHSRzzGi6N7N2UgroPp5Y17SaYPKZws2sBeK0ZGYNTUkv2B0OOyMm7Y54Za0goT-AtHmTSWjMcEW4AMQ9wGCcf5NKc1pZBoX3JUjnV8pDjPC_pw0gsuNDvAyNLSPkJ7ciEjpZggKdy_iMZ7OX09tuNago9ryhxmsYf2cVMZBgRfMuF-XmbulaKYkyB2Z6cNEFGBNnnj_PJFXuunrVZ2buyNNa6EPsbI8F-HiyDS8T05o15umYb-eDep7nMXmxMCjFJdpNSD0NEJ5mWqFCM9ovYj-8NoIXJ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8551b8a147.mp4?token=c_4snMCXl2FpKqR7oEJA7dWTJuR_UNCJveZOgRNXZkURQG25eC-64QVHSRzzGi6N7N2UgroPp5Y17SaYPKZws2sBeK0ZGYNTUkv2B0OOyMm7Y54Za0goT-AtHmTSWjMcEW4AMQ9wGCcf5NKc1pZBoX3JUjnV8pDjPC_pw0gsuNDvAyNLSPkJ7ciEjpZggKdy_iMZ7OX09tuNago9ryhxmsYf2cVMZBgRfMuF-XmbulaKYkyB2Z6cNEFGBNnnj_PJFXuunrVZ2buyNNa6EPsbI8F-HiyDS8T05o15umYb-eDep7nMXmxMCjFJdpNSD0NEJ5mWqFCM9ovYj-8NoIXJ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیروهای رژیم در یکی از هنرستان‌های دخترانه شهر اندیشه برای تشییع نمادین علی خامنه‌ای!
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72465" target="_blank">📅 16:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72464">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=QM8McatS3rDN9EGn-v7qxjtjbmReEhVtykkH6wOz3k6cUWMPNXkGqYfD-vfuP16secMhQihjNfy1wXG_j6lRzGaRzDqPiDVI3Pqg3ii69huGhKBMmypyTB129aP2FOmqS-B4he3cY14jnG6a6_xedw1Cn2FtKREQRP16BuHy-_SPllYSWFuAmodX2NApZxvWo5qC6JpkGbmLVXJyFJ4_huqVZxRbbxC6MbMN-w6-miXoAqyX7bcINxRgj3nRKZeHzW8IBhRJAjZa20pRGRl71RFT0woVD6VaKMM2OZT0NBabe6Jk08KeNXeMX-01BfU9mxavJEKrLu66VCxIPaTlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb8d0412d.mp4?token=QM8McatS3rDN9EGn-v7qxjtjbmReEhVtykkH6wOz3k6cUWMPNXkGqYfD-vfuP16secMhQihjNfy1wXG_j6lRzGaRzDqPiDVI3Pqg3ii69huGhKBMmypyTB129aP2FOmqS-B4he3cY14jnG6a6_xedw1Cn2FtKREQRP16BuHy-_SPllYSWFuAmodX2NApZxvWo5qC6JpkGbmLVXJyFJ4_huqVZxRbbxC6MbMN-w6-miXoAqyX7bcINxRgj3nRKZeHzW8IBhRJAjZa20pRGRl71RFT0woVD6VaKMM2OZT0NBabe6Jk08KeNXeMX-01BfU9mxavJEKrLu66VCxIPaTlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درد و دل یک معلم منطقه سیستان و بلوچستان را بشنوید که هر میز ۴ نفر دانش‌آموز نشسته و درس دادن برای معلم بسیار مشکل است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/72464" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72463">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک فروند هواپیمای بوئینگ ۷۳۷ متعلق به شرکت هواپیمایی ایرانی «کاسپین» در فرودگاه استانبول، به دلیل بدهی ۳ میلیون یورویی به شرکت خدمات هوانوردی ترکیه‌ای «ACM Temsil Gozetim» توقیف شد.
این هواپیما در حال آماده‌سازی برای پرواز به ایران بود که مأموران اجرای حکم قضایی وارد عمل شدند؛ آن‌ها ضمن دستور پیاده شدن مسافران، هواپیما را بر اساس حکم توقیف در فرودگاه نگه داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72463" target="_blank">📅 15:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72462">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Io6GrYKMafaz1dRVgU915fyYiaSN1AWzE39VeoM2VQvOajn2w6Hq4QiKGhHuXH4DYTrN48kJ0CBednpS-f6gTXoQfO2NOsAGieQiYMUjENgrNSl_wCR_ZoWNcYYqrStMPd07jibFaXrKrFxyCtrkDGwZ4QRaeuKDX-poWuMBtUD7t1cXQnIdXqtv9-qgTD81-bngepAGJ0PSZ94F5Pe2MTDMRUIqy9aPb4xHa8YG1gV9M5tcf1coWKDKXUQQ5TqBXURFypBQoBUjdAxlEd64NDAJ76McNfGlgE2ynaobiIVEmS5ZCbNkkuLxHjKXCnTDE_rhz1WOAMYSwr_PVCuQqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26341dd428.mp4?token=phRraKGcejL3bVY9ToIv2EcRZ5bas-fwfwJ7FJRyzTahCc-l4k8h8L-Xjnk5VLS-IXxyTLwiG1gM-rwAFfHxERSZE9laUMKo_Sk5UBClxQX7zivUxVh4UC97FGdEVx-L3hgPZ4I7XzEWGUCU-3IOaKKN8HuBBRJiHDjyY04zK5P_iVLzB-3j1o1MBJzClpvooFqF_gvL3Xzevmt0wL_ovSERFM4uKuq2rBCJJYE8AjYxKtaO3wC2abeLpMkZUmgx2WldRea3M9ez8Lx0aBtE-1c-ldRtc1__6X6h3jpJhHmZnu4nxBXWuggeqWi9x17OgOERWpPfXZ88N2id1aYu0Io6GrYKMafaz1dRVgU915fyYiaSN1AWzE39VeoM2VQvOajn2w6Hq4QiKGhHuXH4DYTrN48kJ0CBednpS-f6gTXoQfO2NOsAGieQiYMUjENgrNSl_wCR_ZoWNcYYqrStMPd07jibFaXrKrFxyCtrkDGwZ4QRaeuKDX-poWuMBtUD7t1cXQnIdXqtv9-qgTD81-bngepAGJ0PSZ94F5Pe2MTDMRUIqy9aPb4xHa8YG1gV9M5tcf1coWKDKXUQQ5TqBXURFypBQoBUjdAxlEd64NDAJ76McNfGlgE2ynaobiIVEmS5ZCbNkkuLxHjKXCnTDE_rhz1WOAMYSwr_PVCuQqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر منتشرشده حملات پهپادهای مولتی روتور FPV نیروهای اوکراینی به سربازان و مواضع ارتش روسیه را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72462" target="_blank">📅 14:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72461">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=WPgIJWhM_TbFnCI3P4SKYTZH7w1lb-oPmFXwkjXmCpR5D0hm7i_rByUnT9_RhrO5OJfAFGN1Jjl5vRYtk47-BZ59NH1xCglfE1ZL-flZp6sfDmksrIeY_RnJDxFQLxDyTzPfUQdCY6uHQPrxPYHkrTxUm-DI-x_q2R8e31ORKn9Uewmr962mfT4k7RQKnUhAc5fD047-OgbicbyH9SPuwnoBfehmTDm_xSKbAIMKpPvsOtVZyR4vG0Mfwkynwcktue9UJ8gbL7EvCZ6YqpPDRIA31gZaT2bKw8O2QXBfzUMV0xbbHXpUR3CN-NLHN578nF0qK4NYUL5_leRqbRCAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311fdab4f1.mp4?token=WPgIJWhM_TbFnCI3P4SKYTZH7w1lb-oPmFXwkjXmCpR5D0hm7i_rByUnT9_RhrO5OJfAFGN1Jjl5vRYtk47-BZ59NH1xCglfE1ZL-flZp6sfDmksrIeY_RnJDxFQLxDyTzPfUQdCY6uHQPrxPYHkrTxUm-DI-x_q2R8e31ORKn9Uewmr962mfT4k7RQKnUhAc5fD047-OgbicbyH9SPuwnoBfehmTDm_xSKbAIMKpPvsOtVZyR4vG0Mfwkynwcktue9UJ8gbL7EvCZ6YqpPDRIA31gZaT2bKw8O2QXBfzUMV0xbbHXpUR3CN-NLHN578nF0qK4NYUL5_leRqbRCAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در آن شب او یک ایران زخم خورده را به دوش کشید.
به یاد جاویدنام حمید مهدوی، آتش نشانی که خودشو فدا کرد تا معترضین رو نجات بده و در نهایت با شلیک گلوله، ۱۸ دی ماه به قتل رسید.
۷مهر روز آتش نشان بر حمید مهدوی ها فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72461" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72460">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=aImdU-DVT49vSOCbwy-2UK2WcSlByDwqkXCYs9pWX97Zspg_9-ODP_DjWww6DMUs0-BQw5F9keRlyO2ftCChweAbAPICLUHjbLhP-Jcf9zobJERGVbMAR-_b8xMdEO4F5wzQemqPdCD__wadeqvO2oJ7XaTcr27u6opvblXMniDnuy_LgpwPiScrOdwZan_3lBFXD1zhH1xRZqcIMgQr_pPA5PhNGEI6fPrUUG6DUXakNsKZnwqm4zH944VO4umRkxBzfg6wGhdR61X5aK7x0ZmJ41dBo_O4Tcxp1OBLay8buhtQHnXvhMCiY86166MyInxWoTZw3zHCZ58JLYICkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d05cdce3e.mp4?token=aImdU-DVT49vSOCbwy-2UK2WcSlByDwqkXCYs9pWX97Zspg_9-ODP_DjWww6DMUs0-BQw5F9keRlyO2ftCChweAbAPICLUHjbLhP-Jcf9zobJERGVbMAR-_b8xMdEO4F5wzQemqPdCD__wadeqvO2oJ7XaTcr27u6opvblXMniDnuy_LgpwPiScrOdwZan_3lBFXD1zhH1xRZqcIMgQr_pPA5PhNGEI6fPrUUG6DUXakNsKZnwqm4zH944VO4umRkxBzfg6wGhdR61X5aK7x0ZmJ41dBo_O4Tcxp1OBLay8buhtQHnXvhMCiY86166MyInxWoTZw3zHCZ58JLYICkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
افزایش ۳۰۰ هزار تومانی کالابرگ، پول یه پفک هم نمی‌شه.
سخنگوی دولت:
قطعا کالابرگ برای خرید پفک داده نمی‌شه!
+بیناموس مردم با سیصد تومن بیشتر چه چیزی میتونن بخرن؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72460" target="_blank">📅 13:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72459">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلار ۲۵۰ تومن
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72459" target="_blank">📅 13:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72458">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=iJ5NwnyWfCOqCNpI-Scbw5jUGuaoGWBcAGU9uQKW8RUsBukXogr7Ej4kz32oI7RUSdWZ9ofBzuW-qSsCfFth-9MMh0bxVp0KDTY_Dsb1PQNtTLiXSe3grZ5doPbPOepOpwIJmgUViPBW95wmMJQyyqqMtm7tZoKvtII7t089t7brKTDnLUm32TwyEC5JB-o0IeMMjw0Ono0ZkgV_tUmVqSRTEq8VTMaJmXriCJe5T4N1MyS19f6rToBQD6kYitSSYtU4AfKrAFCvGhFNaDBtI1kmyAho8oj2LDPXMZ5zCRD9Wdq0ZB-DD8yj6YhRrbQev0aoECcrQ8ZyBgJ3aGRYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a114556ee1.mp4?token=iJ5NwnyWfCOqCNpI-Scbw5jUGuaoGWBcAGU9uQKW8RUsBukXogr7Ej4kz32oI7RUSdWZ9ofBzuW-qSsCfFth-9MMh0bxVp0KDTY_Dsb1PQNtTLiXSe3grZ5doPbPOepOpwIJmgUViPBW95wmMJQyyqqMtm7tZoKvtII7t089t7brKTDnLUm32TwyEC5JB-o0IeMMjw0Ono0ZkgV_tUmVqSRTEq8VTMaJmXriCJe5T4N1MyS19f6rToBQD6kYitSSYtU4AfKrAFCvGhFNaDBtI1kmyAho8oj2LDPXMZ5zCRD9Wdq0ZB-DD8yj6YhRrbQev0aoECcrQ8ZyBgJ3aGRYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت : خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
خبرنگار : به به خوش خبر باشید دست شما درد نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72458" target="_blank">📅 13:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72457">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1910edd949.mp4?token=cfbtNozK6rAcQekhYTbzQefxzuHKDYBJv98Yf5DOIeYufwDQtxkgfwQUy7DljBsGpGezQtwPcobOsxqM7CH2oakHcsLqi8MX2bpgzZqE1Jhc018FFGiROViAxNhLnSBgXvsQtzt-QnAOocd-gE89zPM2-xff3_yJkGotAU9gObvcFEhb7hcCC_Wu8M3yx1yPA6itbM1urOap5pUCTDnQVzos7NuhCOrO-BAtSoB-u8UGtwbkvXZJUPzxDj7nNU147lu9iwO5O1mOYKOy9iWiCv1Ft0X2mJY1HYXEkO3nQ-5mgKnXvHOxM_Dtx0DhBIGMA6oWgjDx1hvtyzJ-SQLujQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1910edd949.mp4?token=cfbtNozK6rAcQekhYTbzQefxzuHKDYBJv98Yf5DOIeYufwDQtxkgfwQUy7DljBsGpGezQtwPcobOsxqM7CH2oakHcsLqi8MX2bpgzZqE1Jhc018FFGiROViAxNhLnSBgXvsQtzt-QnAOocd-gE89zPM2-xff3_yJkGotAU9gObvcFEhb7hcCC_Wu8M3yx1yPA6itbM1urOap5pUCTDnQVzos7NuhCOrO-BAtSoB-u8UGtwbkvXZJUPzxDj7nNU147lu9iwO5O1mOYKOy9iWiCv1Ft0X2mJY1HYXEkO3nQ-5mgKnXvHOxM_Dtx0DhBIGMA6oWgjDx1hvtyzJ-SQLujQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار افراد از پنجره‌های ساختمان در حال سوختن آکادمی علوم کی‌یف، پس از اصابت پهپاد جت‌سوز روسی به آن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72457" target="_blank">📅 12:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72456">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=DQSGRWS5hOVq6ssSC1KzxAgpmjx2bxHynjrUa9DhUdJEalGS37pAlvGXttcjinS3GbPQnL73hYhIwzyBP7VryGlHnLZH_FNv5P4BQIrq8snLlaXP8othOsfdT0UPRe1q4uY3eCM90s3VSeEMoKPSF-nv2HsjXf3BySWgPYVLqBtxXR8JK4VYZBDk28_QqLts30yOsaqXLp8HvrbH4s0TTG95OIZY0qCFXHBNo-3EQvVWD0AAyC3Jx9gSS5qSTJwfgrG7ZhucegW0lLkXe4dzvXDy2YyQEKqe4JchYluEDycLsLK8cVxwansrrcI7odIMngsdaZCHUp49FBOWTqQ6zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=DQSGRWS5hOVq6ssSC1KzxAgpmjx2bxHynjrUa9DhUdJEalGS37pAlvGXttcjinS3GbPQnL73hYhIwzyBP7VryGlHnLZH_FNv5P4BQIrq8snLlaXP8othOsfdT0UPRe1q4uY3eCM90s3VSeEMoKPSF-nv2HsjXf3BySWgPYVLqBtxXR8JK4VYZBDk28_QqLts30yOsaqXLp8HvrbH4s0TTG95OIZY0qCFXHBNo-3EQvVWD0AAyC3Jx9gSS5qSTJwfgrG7ZhucegW0lLkXe4dzvXDy2YyQEKqe4JchYluEDycLsLK8cVxwansrrcI7odIMngsdaZCHUp49FBOWTqQ6zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط ۷ سال گذشته! وقتی همه می‌خندیدند که این ربات‌ها چقدر دست‌وپاچلفتی بودند. با نگاهی به اینکه مدل‌های هوش مصنوعی در همین مدت چقدر پیشرفت کرده‌اند، واقعا کنجکاویم تا ببینیم ربات‌ها تا کجا پیش خواهند رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72456" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72455">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmp0KF6zo9TlRsVdsq7vu57Zy3oMgaquohJBX-QeqVYGvLfXyp37mTnd6lO1AoJOoF_S5FiQ_CKxhFqLKyiy73ZztkSQL9KcWBOSHUqJVfp99z4sZpA09H-raxlgOT3YYCXK6edgT8HgZmqiDoNtJH7omlyRlgaviFAPSI6hU75GXkSAZ0104BSvXrWe4HkYRAyGTQ9v87_Zix47NfQa_Hh5-w8VHj2wI1JqrBRCM4gWxdmed68nuGG_FD1bJJVMwFqQuRWfT_lFvCCew5bpY9Tv5AxopVo5TwYBu4X7C59B3RplwAzAwV_9EVRFJX_FXwz1yuDfuUinbxwqjH-4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
قوه قضائیه جمهوری اسلامی: رای پرونده ترور قاسم‌سلیمانی صادر شده و بر این اساس دولت آمریکا موظف به پرداخت ۴۸ میلیارد دلار است!
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72455" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72454">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72454" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72454" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72453">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFoY0CXx_-e6CUtBlvm6HJRmQJdJoHORZx9ADWw_K2aA6XQkFt1pgEXe_29m7WNvaAWTLD9Mz_ihTXRQu0gQp1jTi6D1OTnpa0CnTdL2U9Kk3q7Z5RAVGSIfNxBDDsa9WGvAhgqn48i0qWHJoJAn0gbIzWv72m0rwZ2DCLLoLoAF6RTIKTM4Cj4g35UrouVnVAsGeTuCzO9JqR0LCj1GotHcJCX1VPNDJ_PoGn0nGluT0JWUxC0dLNBx-6ZdYS-FUcQ_e_tW2NAA-18sTQMWjxM-YI8NrkfOK-h8z220_MlmEdedEdwUHuZYDyy80pIzRP4fI8KoKQHsRC17PQsNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72453" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72452">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دلار ۲۸ تومن شد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72452" target="_blank">📅 11:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72451">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e130021.mp4?token=tF1hiazSuripnNVbeD05_4Jk4wE1AUPNlvW0eFD5XDU7iATSdnfYMy-kjR7FTVDwqO6z3BynGThOS0F0qaHfwvOYFO-aF5kQjqfMcmX59rl2cWsfr0PmcH96KRxgjmOuqk_R2Racs8iOoDojPOFvO8eyaxHaJqtyvcUs3omsIUD5Kj3EjSKuyQt23Mk1Pf7PBwvAXyQXkQfAAWqnOGIIPUO2ZjMheAlO5zBXIoDuC6-YzTlM8vT5RCXstY5vHJJUKNVKMC3jLREHIfC8rU4nTvuWJnrbTboy4wC2vR3F8uFul9Obx1ef7AJEXo9mSeyI1n1W2lctKNnYfOE9A23aPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e130021.mp4?token=tF1hiazSuripnNVbeD05_4Jk4wE1AUPNlvW0eFD5XDU7iATSdnfYMy-kjR7FTVDwqO6z3BynGThOS0F0qaHfwvOYFO-aF5kQjqfMcmX59rl2cWsfr0PmcH96KRxgjmOuqk_R2Racs8iOoDojPOFvO8eyaxHaJqtyvcUs3omsIUD5Kj3EjSKuyQt23Mk1Pf7PBwvAXyQXkQfAAWqnOGIIPUO2ZjMheAlO5zBXIoDuC6-YzTlM8vT5RCXstY5vHJJUKNVKMC3jLREHIfC8rU4nTvuWJnrbTboy4wC2vR3F8uFul9Obx1ef7AJEXo9mSeyI1n1W2lctKNnYfOE9A23aPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنندج؛ ضرب و جرح شدید سه نوجوان توسط ماموران انتظامی
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72451" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=MyrSEcHza9PSEbvpHn7WV_Fe6I_bSXui-Hi_AN5mRb5gsKYzBjdDX9AvmunHlYAInqeEGSEc_BYNbyOfzYVMKcL8Wd2PdJgJ2A6Y9ZFlOHH0nUJrTaXPfGFXFDDlH3hd1sqoRPw9BqaGGQLV-5WiTMZtKci8XkDJYt_jC38Xx_MAhUpIRNf7gLH16NUA_8ky4Z4kVlojVhDvKZen_LDfTPvBkD-OiNQDbw6OytQBo-zQ82unVNMo9ZKnMT7Y6mlvLudDakHcZ1V0plrXceHlgraKJMcUuNf2a2NylumkhrNtd167a_tSgqZlUgvMlqwJasrZjbSLKkTuwCCAQ22N5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=MyrSEcHza9PSEbvpHn7WV_Fe6I_bSXui-Hi_AN5mRb5gsKYzBjdDX9AvmunHlYAInqeEGSEc_BYNbyOfzYVMKcL8Wd2PdJgJ2A6Y9ZFlOHH0nUJrTaXPfGFXFDDlH3hd1sqoRPw9BqaGGQLV-5WiTMZtKci8XkDJYt_jC38Xx_MAhUpIRNf7gLH16NUA_8ky4Z4kVlojVhDvKZen_LDfTPvBkD-OiNQDbw6OytQBo-zQ82unVNMo9ZKnMT7Y6mlvLudDakHcZ1V0plrXceHlgraKJMcUuNf2a2NylumkhrNtd167a_tSgqZlUgvMlqwJasrZjbSLKkTuwCCAQ22N5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک سگ که بر اثر صدای انفجارها وحشت‌زده شده بود، در جریان حملات روسیه در اوکراین ضبط شد:
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72450" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72449">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=M5PSG9yIBhMsvoJOU6XDNZ71N45EMdszhpuSoJvgf_8gdMQhVyyartrH-LvFoJ6E3y3RySNIeEh7v2LYb3Y1KiJFXlDT6pxA_KbNfIRK1_TxIRKwzgbZgUpbSymcKh3OlbehmrGIxliaOoqCBFqzYJ1bUGk58Lk2E5f_vinEH4lXY5oy3XeWBB7WY9Pp5lOcT6EQjHvXH8jxJBACQd04IlEru8KdDO57kIqinmHG0RC2JCZ7uS9TEcSJd148b2jJ59T2c8u_pJqqTMpUoz6BE1aYhtUNichobFATi05tbmuziUtjWkIAmT12zfNAGm4l93GfcTsYFAEXwsT0JGf-t2Rjbh44SNNO3Dv6o1jV5kZg_cCFewjvwjnASOH8H1Kx4gWnLphQZBHhUYiTkx2P4Kn20fKuvs-SKJQm5b0yPhzjrt3gFN9sDIXJUfNL2M8vQG_r-vZZ9I-GBvSQJu08BYzAJXE25OeCglXcxx4_qdftHO4jHMVQsv-St4OQN1DY99WzdO_ZmOlc6PcvSTo3Z1PRxHb_wPzjJwj_Fnn-oAV8c71ooCPdiKLljgJGUAvlDJSB9bQTCwx92lG8xDr35XefInxVXe0UIsYLPAzr1tqNsJsUYeooCWxi26SA3mSZj22-ME4KYwciAmg1mxHd8XhO4b1pjsNsr7XQrZIlh34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=M5PSG9yIBhMsvoJOU6XDNZ71N45EMdszhpuSoJvgf_8gdMQhVyyartrH-LvFoJ6E3y3RySNIeEh7v2LYb3Y1KiJFXlDT6pxA_KbNfIRK1_TxIRKwzgbZgUpbSymcKh3OlbehmrGIxliaOoqCBFqzYJ1bUGk58Lk2E5f_vinEH4lXY5oy3XeWBB7WY9Pp5lOcT6EQjHvXH8jxJBACQd04IlEru8KdDO57kIqinmHG0RC2JCZ7uS9TEcSJd148b2jJ59T2c8u_pJqqTMpUoz6BE1aYhtUNichobFATi05tbmuziUtjWkIAmT12zfNAGm4l93GfcTsYFAEXwsT0JGf-t2Rjbh44SNNO3Dv6o1jV5kZg_cCFewjvwjnASOH8H1Kx4gWnLphQZBHhUYiTkx2P4Kn20fKuvs-SKJQm5b0yPhzjrt3gFN9sDIXJUfNL2M8vQG_r-vZZ9I-GBvSQJu08BYzAJXE25OeCglXcxx4_qdftHO4jHMVQsv-St4OQN1DY99WzdO_ZmOlc6PcvSTo3Z1PRxHb_wPzjJwj_Fnn-oAV8c71ooCPdiKLljgJGUAvlDJSB9bQTCwx92lG8xDr35XefInxVXe0UIsYLPAzr1tqNsJsUYeooCWxi26SA3mSZj22-ME4KYwciAmg1mxHd8XhO4b1pjsNsr7XQrZIlh34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه امیرحسین قیاسی با پسری که رتبه ۹۲ کنکور شد ولی معتقد بود ریده و پشت کنکور موند!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72449" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72448">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvkX-Don22xBCwUJIh0RPD9Nv3p1mSwaMigFYdHhuPEQHOFeyU6qpwg0KgEU6qxgICQboHkVQbtLWiTEyvzONv3oQa1583IMyERe8n5_bVlWMwdzrwz293WYg8rf7cIzmqnjW2CUIy1gw0-YRhOkMo_jsmQz37nyu5z9uzVqtN4ffiekvI-AeShFIL_pylU0mj-PJ3BY6G3mHlIDE1j8uDXGFJyWK-gbSpv7ZwVeFTKPX4aMbt0Zv3o9hb4u9MXoQ2WIczjUqK3vhBDKuuIAefCxdtkBhq8SoSifzxs34rgm02BjoCd4O8xp1MLc1OL2dynlHRRzb-43V0TUG7Q2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛به گزارش شبکه خبری «کان»، سفر روز یکشنبه بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به امارات متحده عربی که در اصل برای هفته گذشته برنامه‌ریزی شده بود، در آخرین لحظات و پس از اعلام عدم امکان دیدار با رئیس‌جمهور امارات (محمد بن زاید) از سوی مقامات این کشور، به تعویق افتاده بود.
مقامات ارشد چندین کشور حوزه خلیج فارس، از جمله نمایندگان کشورهایی که روابط رسمی با اسرائیل ندارند، در گفتگوهایی با نتانیاهو که بر موضوع ایران متمرکز بود، شرکت کردند. نشست منطقه‌ای مشابهی نیز در جریان سفر قبلی نتانیاهو به امارات در ماه مارس (هم‌زمان با تنش‌ها و درگیری‌های مرتبط با ایران) برگزار شده بود.
هم‌زمان با سفر نتانیاهو، هواپیماهای مرتبط با نیروهای حفتر در لیبی، مراکش، قطر و امارات در ابوظبی حضور داشتند؛ از جمله یک هواپیمای دولتی امارات که از مبدأ ریاض وارد شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72448" target="_blank">📅 09:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2070144954.mp4?token=uoed3p2z2QrlNt70-8SnCa0VI5W7de6BPSM-HjkJGzrMYPyiMzqD1pEJfJ2WmpYkJuuCLX07xGqUiVN9e4cW4qZPEV1fax_Ph4aC6ketHlMb5Fd2bNG-Ehs1Q5AzIIR76_d0_JyUFDSS0feFtHwY75oI9whvLlmOjzyT1Big2NX8zzwnWW5lOJXQNov0yCoL5yOfeq9weoHxlL_OrDilMIjgW9HL7Ks41btaZtgwFcOZ8D813FH1JzLNAvhC8mCJ3V-HmUpyp9UKD4a_TH2jfcmtkAmzMNm2temV0__-60NiWzGRm9kHd34fAsx8mNlyNh6LQbUGXZmTj9XFVKR8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2070144954.mp4?token=uoed3p2z2QrlNt70-8SnCa0VI5W7de6BPSM-HjkJGzrMYPyiMzqD1pEJfJ2WmpYkJuuCLX07xGqUiVN9e4cW4qZPEV1fax_Ph4aC6ketHlMb5Fd2bNG-Ehs1Q5AzIIR76_d0_JyUFDSS0feFtHwY75oI9whvLlmOjzyT1Big2NX8zzwnWW5lOJXQNov0yCoL5yOfeq9weoHxlL_OrDilMIjgW9HL7Ks41btaZtgwFcOZ8D813FH1JzLNAvhC8mCJ3V-HmUpyp9UKD4a_TH2jfcmtkAmzMNm2temV0__-60NiWzGRm9kHd34fAsx8mNlyNh6LQbUGXZmTj9XFVKR8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو به‌تازگی در برابر دیدگان میلیون‌ها نفر فاش کرد که باراک حسین اوباما به تأمین مالی رژیم تروریستی ایران و مرگ هزاران نفر کمک کرده است.
«در مورد هر دلاری که ایران در اختیار دارد، کاری که آن‌ها طی ۳۰ سال گذشته انجام داده‌اند این بوده که هر زمان پولی به دست آورده‌اند — چه در جریان لغو تحریم‌ها توسط اوباما، چه از طریق فروش نفت و گاز و غیره — آن پول را صرف ساخت بیمارستان برای مردم خود نکرده‌اند.»
«آن‌ها این پول را صرف دو کار می‌کنند: ساخت سلاح برای خودشان و صدور انقلاب!»
«آن‌ها این پول را صرف تأمین مالی حزب‌الله می‌کنند. صرف تأمین مالی حماس می‌کنند. صرف تأمین مالی شبه‌نظامیان شیعه در عراق می‌کنند. بله، این‌گونه آن را خرج می‌کنند. آن‌ها این پول را برای حمایت از تروریسم و توطئه‌های ترور در سراسر جهان به کار می‌گیرند!»
«[ما] مانع دسترسی آن‌ها به پولی می‌شویم که قرار است برای کشتن آمریکایی‌ها استفاده کنند.»
اوباما پول نقد و لغو تحریم‌ها را برای ایران فرستاد و آیت‌الله‌ها آن را به موشک و تروریسم تبدیل کردند.
رئیس‌جمهور ترامپ دقیقاً برعکس عمل کرد و جریان پول را قطع نمود و...
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72447" target="_blank">📅 09:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72446">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=KST8wMGGynLPDrlymE6LEWJrkEWMx7vxApQvazxMYPHKAHOzPlG_I8PFm6UrZyDE7Kp39yQwHBdEfRaDWztGy1fDcBSFwXHSOBhxIfLVZeHancUIhwjRACNzbuTlPw632TVOEUdkIXCJRiCuda9Lkr_aIIciD8KvAnf9ga6SokrBipFr1PYxxvL3d0cRy-KB4FWZDcLPJpiD7EtS_1qjX5oM7XRimYIYvOIUfw8fYPVtHSRbJ4FULoMa3qxBH4kbzf2kaLqw6oFrMrKGpIoul-0L3OEs6MPjYC3FEIkx8vbPZD2RcuLZNc_O3NI6MiY-JsGE-axSrKIBfxWGhGllQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=KST8wMGGynLPDrlymE6LEWJrkEWMx7vxApQvazxMYPHKAHOzPlG_I8PFm6UrZyDE7Kp39yQwHBdEfRaDWztGy1fDcBSFwXHSOBhxIfLVZeHancUIhwjRACNzbuTlPw632TVOEUdkIXCJRiCuda9Lkr_aIIciD8KvAnf9ga6SokrBipFr1PYxxvL3d0cRy-KB4FWZDcLPJpiD7EtS_1qjX5oM7XRimYIYvOIUfw8fYPVtHSRbJ4FULoMa3qxBH4kbzf2kaLqw6oFrMrKGpIoul-0L3OEs6MPjYC3FEIkx8vbPZD2RcuLZNc_O3NI6MiY-JsGE-axSrKIBfxWGhGllQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
مشکل اصلی در مورد ایران، «انقلاب» است؛ نه آن مقامات دولتی کت‌وشلوارپوشی که در برنامه (Meet the Press) شبکه ان‌بی‌سی ظاهر می‌شوند و در رسانه‌های آمریکا بی‌هیچ دردسری تریبون رایگان در اختیار می‌گیرند!
«بحث ما درباره آن‌ها نیست؛ کسانی که در ایران حرف آخر را می‌زنند، روحانیون شیعه تندرویی هستند که دیدگاهی آخرالزمانی نسبت به آینده دارند.»
«آن‌ها معتقدند که رسالت مذهبی‌شان این است که آغازگر وقایع پایان جهان و آخرالزمان باشند.
این واقعیت است؛ این هدفِ اعلام‌شدۀ انقلاب آن‌هاست. چنین افرادی هرگز نباید به سلاح هسته‌ای دست پیدا کنند، چرا که از آن برای باج‌گیری از جهان و کشتار مردم استفاده خواهند کرد. این ریسکی غیرقابل‌قبول است.»
ترامپ دارد کار درستی برای جهان انجام می‌دهد. او اکنون به دنبال کسب پیروزی کامل بر ایران است، زیرا این تنها راه چاره است!
بانک‌های مرتبط با ایران در حال تعطیلی هستند، ترامپ عقب‌نشینی نمی‌کند و ایران قادر به صادرات نفت نیست.
اوضاع کاملاً علیه آن‌هاست. هرگز نباید سلاح هسته‌ای داشته باشند!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72446" target="_blank">📅 09:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72445">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=WveYKojzOEZvI0lfABEFwI-mkbRZ0FAWO-scA-JGZ16-Mo3xfvp2FO5a_a_76ofuCFxjLFiOD1i1D-8a7_SOM-i5JKV3gWAZ36PoNKQa_dSedn52u4DKkW7wNZQOaWlsqLQrmZoXCpLTglXLRSFvh6S_QWBtFSjY8c-iEKbD-D69Jh9WWcO_4HDf3clIoVVkwV9gohC89_eH5WZngTciqU590j1OX4RSolUkck45b2k2ByX7EohC7QzwLpCvWrT055u2t02c249BW2gEi2vK_KrJsMONMIQa4bDJt-X_ncPxKnfPwYnjTNLmf3uGZwloiPbnlfDCI7xAtloSqTRqiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=WveYKojzOEZvI0lfABEFwI-mkbRZ0FAWO-scA-JGZ16-Mo3xfvp2FO5a_a_76ofuCFxjLFiOD1i1D-8a7_SOM-i5JKV3gWAZ36PoNKQa_dSedn52u4DKkW7wNZQOaWlsqLQrmZoXCpLTglXLRSFvh6S_QWBtFSjY8c-iEKbD-D69Jh9WWcO_4HDf3clIoVVkwV9gohC89_eH5WZngTciqU590j1OX4RSolUkck45b2k2ByX7EohC7QzwLpCvWrT055u2t02c249BW2gEi2vK_KrJsMONMIQa4bDJt-X_ncPxKnfPwYnjTNLmf3uGZwloiPbnlfDCI7xAtloSqTRqiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
اگر رئیس‌جمهور ترامپ اجازه می‌داد ایران به سلاح هسته‌ای دست یابد، نه تنها همه او را مقصر می‌دانستند، بلکه ایران کنترل کامل تنگه هرمز را در دست می‌گرفت.
درحال حاضر تقریباً همان‌قدر نفت که پیش از این مناقشه جریان داشت، از تنگه‌ها عبور می‌کند؛ به استثنای نفت ایران.
«آن‌ها می‌توانستند تنگه‌ها را کنترل کنند، حق عبور (عوارض) تعیین نمایند و تصمیم بگیرند که چه کسی در این سیاره انرژی دریافت کند و چه کسی نکند. اگر آن‌ها سلاح هسته‌ای داشتند، دقیقاً همین کارها را می‌کردند.»
«اگر ایران سلاح هسته‌ای داشت که می‌توانست با آن همسایگان و جهان را تهدید کند، هیچ‌کس نمی‌توانست در مورد تنگه‌ها کاری انجام دهد.»
«۵ سال دیگر، همه می‌گفتند: "باورم نمی‌شود که اجازه دادند ایران در پناه یک سپر متعارف، برنامه تسلیحات هسته‌ای خود را بسازد و توسعه دهد!" وحالا شاهد حضور یک کره شمالی دیگر در خاورمیانه بودیم. ما در آستانه چنین وضعیتی بودیم! این همان چیزی است که رئیس‌جمهور مانع وقوع آن شد.»
«وبدتر اینکه، صحبت از رژیمی است که در جریان آن به اصطلاح انقلاب، ده‌ها و شاید صدها هزار نفراز مردم خود را قتل‌عام کرده است!».
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72445" target="_blank">📅 09:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72444" target="_blank">📅 06:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72443">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72443" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72442">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72442" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72441">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RstxSG-41j--rSzJAvjhKSfhCEwFPFyvMcZHnCKyzeZxNjdROiOXIftchTItSRuOa9_fMFJ3zJ8IvzUN8-1wY2g15xNah1vgZ6qLokchaIS0e5boNSOrIuvrNHnOTEl2Ty7cB-zBHuq1FNO9x7pUL1GE_OX1hqslVKJ7hq9zEjRlpzjDJNdxyXw0kPySh6O2tOplmiacZIZHZDKFOgUawwPTozHCbe-8wDL1PDe9Sd9iv7D0r2zEH-K5uUTtNJb-zFMrmxOcpccMHPfEovtdPpy21GJtIq4GoZEgc0lJa3tVkwCZRSVa9oDUcRWsIBKh1nYEHNEn0ryX9QlyEG1V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72441" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72440">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmbD8W06FwRDFmOxsqomkfBSx4udSWJQbpmGHiwIt_XrawxrntJDy7XzjWG2G9s0d_nrqKeQuD6NrxC4TYSQJviyGt5nVkRZua-UEiN5rFcZtISlyT-FdBv31TsNuq0f9zQoIHWRdlbXSda8fsNMYkHp94wK8Q8uQ3yQ_ynkeSrysLrdPDGY1C0lAj6RKa5Lzxk7oWcPv2hF4iD1bUfHNKe--p7rc3G8slplR3Ya58U_0ScAWagdQ2bhcjqndd4OlAjEznD1krMWgtgs61Pwv-S3LqJIAbVUo7O99jtiLULb_M5C5MGCjzwHvVkbxDHHQVdgctLQsZ5mYiMCq8DmzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر نتانیاهو:
نتانیاهو و همسرش دیروز به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، از این کشور دیدار کردند.
در این سفر، رئیس شورای امنیت ملی، رئیس موساد، منشی نظامی و مشاور سیاست خارجی، نتانیاهو را همراهی می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72440" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72439">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نقشه‌های گوگل تصاویر ماهواره‌ای پیش‌فرض خود برای غزه را به تصاویر ژانویه-فوریه ۲۰۲۶ به‌روزرسانی کردند و مقیاس تخریب را بلافاصله برای هر کسی که برنامه را باز می‌کند، قابل مشاهده ساختند.
کاشی‌های ۲۰۲۶، بلوک‌های مسکونی متراکم در رفح و خان یونس را نشان می‌دهند که به مزارع آوار خاکستری تبدیل شده‌اند، منطقه بیمارستان الشفا به شدت تغییر یافته است و اردوگاه‌های چادری عظیم در زمین‌های باز باقی مانده قرار دارند.
آخرین آمار UNOSAT: ۲۰۱,۲۹۰ سازه آسیب‌دیده (۸۲٪ از کل ساختمان‌ها)، ۱۳۴,۴۲۲ سازه تخریب شده.
این تصاویر حدود ۲۳۵ کیلومتر مربع را با وضوح حدود ۱۳ سانتی‌متر پوشش می‌دهند - به اندازه‌ای واضح که می‌توان دیوارهای جداگانه و خوشه‌های چادر را مشاهده کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72439" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72438">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=FUd63xP07BfwZzRkfKNRov_DN1eJC8BWa0ZA1C8y6bWGYr9VHkavF3W8hh6EMZjVMw-20A0hj58REEMexkCCcUtd68pEXbLhHuFUAVis2P4KEGziIyDp3tQSRnBcw6bfnGDUuclrSUEujLR0wujC71BwRQ1gs1QTnWdWCnXG0UYmSf_I5RgXjEycS1EjJpUURocCWDN3frNtI1M394ffR2Cvja6bK-Hwg5YlzKqNjiiczhVU5Pge0lYGhgPCbBqX1SuCR_O_wUpNfzLN3HXQ5qJ7_nGR1zMo-bKE0LusE5bhC1yz6-kBoADWe393UhrJbdzly--XnMuiEcwpfN3YVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=FUd63xP07BfwZzRkfKNRov_DN1eJC8BWa0ZA1C8y6bWGYr9VHkavF3W8hh6EMZjVMw-20A0hj58REEMexkCCcUtd68pEXbLhHuFUAVis2P4KEGziIyDp3tQSRnBcw6bfnGDUuclrSUEujLR0wujC71BwRQ1gs1QTnWdWCnXG0UYmSf_I5RgXjEycS1EjJpUURocCWDN3frNtI1M394ffR2Cvja6bK-Hwg5YlzKqNjiiczhVU5Pge0lYGhgPCbBqX1SuCR_O_wUpNfzLN3HXQ5qJ7_nGR1zMo-bKE0LusE5bhC1yz6-kBoADWe393UhrJbdzly--XnMuiEcwpfN3YVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیوانه‌اند. هیچ شکی در آن نیست. آدم‌های بسیار دیوانه‌ای هستند.
من همیشه به آن‌ها می‌گویم: «شما دیوانه‌اید، رفیق.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72438" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72437">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=Lq3zWxP_C8mxFgkn_R7cfmIPZMjdAKQ8ZutPUKirWrVpXaeVgFc_nvuCSDG0Mw3xMNNLp_Mowm5TPoZuRjUVPui5aUfSEFj0F9bq_sybExX0hUbsXzKna5NlOmHjzPAXG1wjmMh9BZ6nh4wPqPGtU_uOQtod2QpH6KpcscOqkdHcAS9fiX6QF9K1P0A29c0BOJAwbf-zKUeCjAs-D08PR5vyx8R2hsPVqyDZBuISom0Aj3uFuudfwIkdcZrtoXIDAc39EDQDxbcvtade6jDA2iG-myhMafWh7PHl5HR1Uuk5SSFSckrh6pxe39N3saoFLkFpMgnH7HqrnoPseYzY4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=Lq3zWxP_C8mxFgkn_R7cfmIPZMjdAKQ8ZutPUKirWrVpXaeVgFc_nvuCSDG0Mw3xMNNLp_Mowm5TPoZuRjUVPui5aUfSEFj0F9bq_sybExX0hUbsXzKna5NlOmHjzPAXG1wjmMh9BZ6nh4wPqPGtU_uOQtod2QpH6KpcscOqkdHcAS9fiX6QF9K1P0A29c0BOJAwbf-zKUeCjAs-D08PR5vyx8R2hsPVqyDZBuISom0Aj3uFuudfwIkdcZrtoXIDAc39EDQDxbcvtade6jDA2iG-myhMafWh7PHl5HR1Uuk5SSFSckrh6pxe39N3saoFLkFpMgnH7HqrnoPseYzY4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند.
من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم.
بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این کار اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72437" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72436">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=S1kamNoTt8QAUzbxKjprl_1lgJsPe1qkkKS4LUl_WEapLcpnicxApIOvzbAc-7hmaPVPhrC0CvbqaqNnl-90urbcHYCk-A6kM6XPE-AmhalXSQvPSfSyer6LlZE2AlPDipXlNx67Sj4oG8OyWJxJKH-3XU4Tj_5-y8J5Z01bmgs9UudfXKYXb1mIDlo8b87Sq31NgzqcW5p8JaJyO9ziSv9_Od-KLbFbaWtmklVYeAMDOTZvPpBVIR6CaX7NZ0le0N_j8jSBBQPcO0OgrWqSV13nL7AZNXUyUT7oC1n2KL8TNA0i76gMLSUEMNFD87HsC3wgP-nYHlVXs2Nzldd5FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=S1kamNoTt8QAUzbxKjprl_1lgJsPe1qkkKS4LUl_WEapLcpnicxApIOvzbAc-7hmaPVPhrC0CvbqaqNnl-90urbcHYCk-A6kM6XPE-AmhalXSQvPSfSyer6LlZE2AlPDipXlNx67Sj4oG8OyWJxJKH-3XU4Tj_5-y8J5Z01bmgs9UudfXKYXb1mIDlo8b87Sq31NgzqcW5p8JaJyO9ziSv9_Od-KLbFbaWtmklVYeAMDOTZvPpBVIR6CaX7NZ0le0N_j8jSBBQPcO0OgrWqSV13nL7AZNXUyUT7oC1n2KL8TNA0i76gMLSUEMNFD87HsC3wgP-nYHlVXs2Nzldd5FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رویداد پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) به ایران ارتباطی دارد؟
ترامپ: ممکن است مرتبط باشد، اما باید بگویم از اینکه آن‌ها را آزاد کردند، تعجب کردم. من چنین کاری نمی‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72436" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72435">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=jRp7eEAAL6LJ2UrVmu7RkuWq5P7NJWz0qy4SMfva0rXPIRQ11fEcmcQgfzGaveyiZ_91LDRQ_HBqZGsjORNdvT_rgKNafMvMYnlZPhLhv1peWOsdgNHB8gifg-tLtBO08cPMlCFsuYxduhDbz0j4hmD8XotfCP89puQ5Y0PiYKFVeRXehicrhv_laBoYqrowsjcXXkb_Bptsb1YMeL8zeVrHMTUNvA6E7Du390Vx3xR0DqkKQe3224PXd-8G2XsA01wfoulabBhmMIvMdpbPYoONPHNSkaPKAcQ3SK65msvUV9xmiUCJctuLngEqxpoCcD60gPnF1WbFoSWTqikBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=jRp7eEAAL6LJ2UrVmu7RkuWq5P7NJWz0qy4SMfva0rXPIRQ11fEcmcQgfzGaveyiZ_91LDRQ_HBqZGsjORNdvT_rgKNafMvMYnlZPhLhv1peWOsdgNHB8gifg-tLtBO08cPMlCFsuYxduhDbz0j4hmD8XotfCP89puQ5Y0PiYKFVeRXehicrhv_laBoYqrowsjcXXkb_Bptsb1YMeL8zeVrHMTUNvA6E7Du390Vx3xR0DqkKQe3224PXd-8G2XsA01wfoulabBhmMIvMdpbPYoONPHNSkaPKAcQ3SK65msvUV9xmiUCJctuLngEqxpoCcD60gPnF1WbFoSWTqikBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما خیلی زود در آن جنگ پیروز خواهیم شد. ماجرا تمام می‌شود و قیمت بنزین به‌شدت سقوط خواهد کرد.
هیچ‌کس دیگری نمی‌توانست چنین کاری انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72435" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72434">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323953406a.mp4?token=vUaJQLEbnxG2aepi1_p87HD_3Y4yzeXgBy3i11Rg9iaTN7GUX6fla38SnfYsMW4sFOvxWAGhIdQBQpSna6Wzm2ufqs0fduHYiK4LxrDXeaBsKphZzUAU1OKdI2_ioS79n82eL4OzukpJt_ZHT7JqJiDZZ2wm43JmY0k2GzonyA5k7d_TK7nUx0Zwsqd4QWITAvvrh3GGpflxM50y_b-QhmkV5sC0h6HHTkLJoFAqqL1dOjeJ8oLrUIRo4K0x4lqfY6z_pjFoq9ldRKrnkIbgGQHepkjQ4MdPO-Y_V-MG2yf_LO45MVnAiN6J7_EYDQHyEvPOmamQgyQe-GKXBXJ22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323953406a.mp4?token=vUaJQLEbnxG2aepi1_p87HD_3Y4yzeXgBy3i11Rg9iaTN7GUX6fla38SnfYsMW4sFOvxWAGhIdQBQpSna6Wzm2ufqs0fduHYiK4LxrDXeaBsKphZzUAU1OKdI2_ioS79n82eL4OzukpJt_ZHT7JqJiDZZ2wm43JmY0k2GzonyA5k7d_TK7nUx0Zwsqd4QWITAvvrh3GGpflxM50y_b-QhmkV5sC0h6HHTkLJoFAqqL1dOjeJ8oLrUIRo4K0x4lqfY6z_pjFoq9ldRKrnkIbgGQHepkjQ4MdPO-Y_V-MG2yf_LO45MVnAiN6J7_EYDQHyEvPOmamQgyQe-GKXBXJ22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر جمهوری‌خواهان کنترل مجلس نمایندگان و سنا را به دست بگیرند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند چنین کاری کنند، چون هیچ درآمدی ندارند و ما را به سمت رکود اقتصادی سوق خواهند داد؛ آن‌ها پولی در بساط نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72434" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72433">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979f299405.mp4?token=TdmIjjTYyzrgcxpl6ZlnML4tMclgx4bbN54Xmtqw1iEMHNh7nQg8pnEv-c6KPQlG2GlaWUjo208PWZQzpKwL_QODm-PW_6GryOd2JFJVlw67dLlEBYA9kOLLCemyOKhIIqiWaXUw_H9eaYci-eNRgatIaLyFabrGyEZpXpwaTlRkwK7oD4ggy_kBrF7M2rHWIDqt2UnwDeHbJ6LG8VXUQnhICAlmVwGxHhcPHkqq-pkQvyfr2Wr84Y0iRHjAy-_9-0TCP0IYQ4Q9_2VQOTvYuJVe9yRZ9bEH-7cqEXMjBEOwZ3L0D4eTY3bdJmTtlyVHLfGNvTEoHG9YybR6ZqYmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979f299405.mp4?token=TdmIjjTYyzrgcxpl6ZlnML4tMclgx4bbN54Xmtqw1iEMHNh7nQg8pnEv-c6KPQlG2GlaWUjo208PWZQzpKwL_QODm-PW_6GryOd2JFJVlw67dLlEBYA9kOLLCemyOKhIIqiWaXUw_H9eaYci-eNRgatIaLyFabrGyEZpXpwaTlRkwK7oD4ggy_kBrF7M2rHWIDqt2UnwDeHbJ6LG8VXUQnhICAlmVwGxHhcPHkqq-pkQvyfr2Wr84Y0iRHjAy-_9-0TCP0IYQ4Q9_2VQOTvYuJVe9yRZ9bEH-7cqEXMjBEOwZ3L0D4eTY3bdJmTtlyVHLfGNvTEoHG9YybR6ZqYmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یستنیتیاساتتیاایایایایایایایتبتیتیایتتیتیابتیتبتیتبتیتیتنین</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72433" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72432">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8-3v-Ufx4-N6ZRVxQ6lPBywPgMLi7JnYQLOnkbj28e3ZO9iZZCp9jJuiv4eToUXDF44vYcEq_WfVuTRSdh3Joiq-q0rH0gSQJXAvwnQf53WJ-7UPyf7f0hFTPZ_esC3yoiSJqV67m1TUypy_dgeh_b9a2bKxD0IYtX5RXwAZFA1S_wxll9ePdcqo7IOtCk2mr113y1XzgTSCTTyDp5C44P24Hrl6DX7Q6YB_pY15ScumKk82g6uQlx0vi-XKZz3kV5AzaVUvFm9xQzhNgktraUts9eTukdbR7KolVKMguE6yn9qHB-JyYUFAuQopGcOn9BRPBPhvsZqmSzKNOOFiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«عملیات طرد اقتصادی» باعث شده است ارزش ریال به پایین‌ترین حد تاریخی خود برسد.
ما به تضعیف توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72432" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72431">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX_dxsLKKycyVDohhss43jeMd2GBEfNC1jV2-m11NcJKJqAbBVMLgV__OWHSlPxOrRZRqF_kKm21WNT829mkuCt4b_q6g_Eoc8nKmqzQfnIDm3rSULntaE_PNp8wATvsCCIzf8dhpKBUTpe5yQ7AcPB-5OLECuVY4MCkLE_Dl1bTishotK2DJDOhmpk4y7CkuhbsFGA344mlEjNxn8cuu0XRlsJnMP90jKs1MOQSpcKm2uQjL0WjA_JeM4N6i8Qt-q4e06R9Fl2-BQ4WjnGYq_Wh1fLgBK4doZPSeoS5rgPISrq0HveFjcoBWcZhVygMk5IjGt8xsUGTTpGA9J1_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع آمریکاییِ دخیل در مذاکرات با ایران به العربیه گفت: احتمال دستیابی به توافق بسیار ناچیز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72431" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72430">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW4pjTtOR9wnRSUxxvwEf6VNBvHE7NpGDlgl1uOp-y1fb3gbxp2eJd7JQ7tjoLmI3fGF_iL_w2bXWnGh2oY0zZz7aGlYPo4HPHh-b-GeP6kigw2gZ-PjH2TCRtnFei29siTiO9mg8p_V4gqk9P7sZ_HtBIFuAOAF0CwF7G7UwdWQDKDUWGC75SMohuvOptVo-JcCo3YEZbLQfN2k5eRAabG9DFvEbhtLS6FkUPBiWRgQeVkq-tmN6LKqG-Vr-3fBUpQAZ492s0s7N0UV0O39pCFJxW7JRJo5BLY9vpURyLrmuyg7Ckvo9L9k1DajQjCFF78tpgBQ5aK6GFBzN51uaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72430" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72429">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=eCBPH9mc0jpL8fJC8-DFDKWJbZnIaO2IAGB8wICE8z1uL7O7Hdf_W9ARxMqFEP1UQ1u-AK2QzsHGYM_W5HaKqfAOT5V_urOIWV1EczDYE_l8eOKUGPlOU3L1mTSIXs-ipDUu8Sj5mrBwDWcCnbjRMskkS1kVc7wmlse1kovECRC5jAhAOC-vY0-OdBtRSXCqFOURIHnSaSK0y6j42sWsJ0pamc3WBXkPkvIjOuIgRY0JC1zMVZ0JbcTu8aCmwgpdF4xDL4oNtAZJ_33yb9zkTKfxMSyokAcFd6TUy6-itIdUtkKtZb15im3JCnLbR5Dg1skZEsYJDzQaAy-KWjR6WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=eCBPH9mc0jpL8fJC8-DFDKWJbZnIaO2IAGB8wICE8z1uL7O7Hdf_W9ARxMqFEP1UQ1u-AK2QzsHGYM_W5HaKqfAOT5V_urOIWV1EczDYE_l8eOKUGPlOU3L1mTSIXs-ipDUu8Sj5mrBwDWcCnbjRMskkS1kVc7wmlse1kovECRC5jAhAOC-vY0-OdBtRSXCqFOURIHnSaSK0y6j42sWsJ0pamc3WBXkPkvIjOuIgRY0JC1zMVZ0JbcTu8aCmwgpdF4xDL4oNtAZJ_33yb9zkTKfxMSyokAcFd6TUy6-itIdUtkKtZb15im3JCnLbR5Dg1skZEsYJDzQaAy-KWjR6WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ساعتی پیش سرمایه دارای میلی گلد ریختن تو شرکت میلی گلد و رسما دارن مسولین شرکتو کتک میزنن و هر چی میبینن خرد میکنن و فقط صدای عربده و ناله از توی میلی گلد شنیده میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72429" target="_blank">📅 20:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:
رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72427" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سرعت آپلود بین‌الملل رو انقدر آوردن پایین که عملا دیگه نمی‌شه چیزیو تو تلگرام آپلود کرد!
#hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72426" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72425">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQReQM0g-8We49z6OQ--ahCNZYOWIsDNfuQXfS3qE7t02vWoqvogw-3tTYMK0F47F4uXf2o1-6bf4ov4R6sEZ2_1euYQs_jBRZ14z4SICOcoenM3m3cJcA67ZuK_Dd0jpT0KiR4x5gTrG8Unhbbh28rwr9Ow5Xv687sysnNkLyqnePbeEsBj9h1lVXKNMPRkzwqoLj5_xeb_hVTom0f8oqiBaiC_i348kO6o7Wn2MZhVGotTRRMEiO0sMPU4eVXWnKAytP9DcQJp8Ypm9IBCoA20y8zVDtcfxr8xmvS5YE8KUIjoogjCeFG9TUGhZuGnZkfWugtjNhnTTcQbTndUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهریه بین عرزشیا
❌️
مذاکره بر سر تنگه هرمز
✅️
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72425" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72424">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دونالد ترامپ امروز دوشنبه ۲۸ سپتامبر ۲۰۲۶ ساعت ۲ بعدازظهر به وقت شرق آمریکا (ET) در دفتر بیضی‌شکل یک «اعلامیه» (Announcement) خواهد داشت و خبرنگاران کاخ سفید نیز در آن حضور دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72424" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72423">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COJYghPei77SN3cb8BpBWkped29p3sIUvFQymcWi472tOvwoyLNiz3nc83Udg56-Kq1iNEbscv1PDnXG0gW4j3MvWceUR2gBksL0E1GzuFViO4TfcXtlXu5VfSmvOqYp2c16cotQy92R8dpjR4Y4DEIh5njHhRvyP-7WKfEZuor-00Xeyj3hJLIjwtmcHE6uVJ4NdFgZ6ropnIaIEaEpXvT0BWnP6eCEV-PErAFSwgJsyXThCOejivBBX-CBWdNgazyF1PlhwxzDT5UICcrhTxmbi4yMEhYKO4HVz8qzc29Ixd2mPHuGoNbniDsbvZbjDokYFxu9EOD5EqoZiKWiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی به زندان اوین تحویل داده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72423" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#مهم
:چندین فروند جنگنده F-22 Raptor طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی «لنگلی» (Langley) برخاسته‌اند. (1)
علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی ایالات متحده نیز در آسمان هستند که احتمالاً وظیفه پشتیبانی از انتقال این جنگنده‌های رپتور به خاورمیانه را بر عهده دارند (2):
- GOLD21: KC-46A (شماره ثبت: 17-46034)
- GOLD22: KC-46A (شماره ثبت: 16-46021)
- GOLD31: KC-46A (شماره ثبت: 18-46051)
@News_Hut
| AirAssets</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72421" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72420" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72420" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRI7UnmD05tRHYgY9FfWT8Wb4jFzH7_mGf0AIhxqgKhDA6_m8ANpxCSTNrIVy7ER0L6-bvRi4AhQVRrPOa3YQjztlD9wdruafr8uXqNRiOLKXSA_xt8wuQixho5ngyIS4D_hrPYE2vahkguM8ATxaW9j41_FT8XJ1njcc3MTjsoJRfbo55cM6SbvxR8afCrSx8DqPlXjVD19eC80attr2cB0o5Mq-95sEuAHan2mMWkv65GxGd4p1C1AiheYmmfgVYuWfP0GCuN4aVKZKqR5U-fILfwP38xQhPEklgeKGeHYlarVCSLVtHzXIGY0BoObEYtkyHFT8nKsxv6m_HWjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72419" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=fBzTqsdskjcY6WWveMhM_vaAkAyILXjke2woMlT3h5jCHPgn6-nxEboxauoYQetHSPe3LIky6bdZ93Z97j47h9mjxYF8RTOcdZ2jvzCieRzu19YKvGsdIb4t0FsF1nFvY5-SOLXHwfd7l7N9E_R4qMHvwOCdMw0aFkDvsPrWkmk9h90wt2iuqvkrBIjUMk_4KLu7cwv5j7YXEn4MG9WkpB0NTMy7HFK8rUE3kgPO7HIBnPhX4yEpWLUmqPqscz0G5ZR8oeU5aEz3iuLLuyTPMZJN1Fz33BcO_XDfT15gPT96Ov3T89VQGGpxjpJCmbyb5WXdjftI_zK51CfCQpOjew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=fBzTqsdskjcY6WWveMhM_vaAkAyILXjke2woMlT3h5jCHPgn6-nxEboxauoYQetHSPe3LIky6bdZ93Z97j47h9mjxYF8RTOcdZ2jvzCieRzu19YKvGsdIb4t0FsF1nFvY5-SOLXHwfd7l7N9E_R4qMHvwOCdMw0aFkDvsPrWkmk9h90wt2iuqvkrBIjUMk_4KLu7cwv5j7YXEn4MG9WkpB0NTMy7HFK8rUE3kgPO7HIBnPhX4yEpWLUmqPqscz0G5ZR8oeU5aEz3iuLLuyTPMZJN1Fz33BcO_XDfT15gPT96Ov3T89VQGGpxjpJCmbyb5WXdjftI_zK51CfCQpOjew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردادن شعار«تا آخوند کفن نشود این وطن، وطن نشود»در اعتراضات امروز دانشجویان دانشگاه علامه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72418" target="_blank">📅 17:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=eqJTkoLoTPrVajnm35PykdU2T2CtDKoQTvKpb11LOttM1pNZzwjGpaeAMWivh_38ReLG0JX--yiY8B2ggaeQdjvknI8Xr9mxrMYJH5MpzAgdUdbHBClG6nHQqkQa-Nl738Iot8UcaUIba3kOJ5GemNkwZqHehj_eJCfBH0-ScQWQLfdcNEIrof2e7cuWKuLwBvXXx-w0nJB1V2sweiTPEmIkho8oTQ3XVQ6Kc6ub4sQEIH4HHbf3sCII_ZE-qc1Y-DR3OVREYilGKfcW6QyoIQfUobvleEyIFaUSq0UyayaUxbdz4eGTphbY1GionWx_UF9rb10_O-A6R-MZ_iDyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=eqJTkoLoTPrVajnm35PykdU2T2CtDKoQTvKpb11LOttM1pNZzwjGpaeAMWivh_38ReLG0JX--yiY8B2ggaeQdjvknI8Xr9mxrMYJH5MpzAgdUdbHBClG6nHQqkQa-Nl738Iot8UcaUIba3kOJ5GemNkwZqHehj_eJCfBH0-ScQWQLfdcNEIrof2e7cuWKuLwBvXXx-w0nJB1V2sweiTPEmIkho8oTQ3XVQ6Kc6ub4sQEIH4HHbf3sCII_ZE-qc1Y-DR3OVREYilGKfcW6QyoIQfUobvleEyIFaUSq0UyayaUxbdz4eGTphbY1GionWx_UF9rb10_O-A6R-MZ_iDyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛گزارش‌ها از شروع اعتراضات در دانشگاه علامه تهران حکایت دارد؛اعتراض علیه حکومت، گرانی و...
جمهوری دروغی نمیخوایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72414" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72413">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=U_s4UOV3Og3MRaegEHAiB_C_FsUGmJJu_YgXm7A8GDU1176MCH2E36bidJchS2S48hjOT3D59k1kQtbehrW6c8bt9RkuwvN-CvK6I4TwLOmUqiQOPuzuivz9rDeo6f719VY39bdN93ilN78NnA2_UHluLfWvPQViQkEtqqKgj9-sVjz5eliM4Ws2fGbAVJLKE0YgToVUMx87pqvEFFtxEU4KN7NUltuCgKc9i5FhbcpD6_m5olFKPauUeEsuHDIaqIimxtqj-TKaL74qR00YfmDSdBqjRMuV5SrMg39BE-e9ahFXYnM9Z5BJx6u6NJBRBPxwsvpXmLZ0rTFA40Ag4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=U_s4UOV3Og3MRaegEHAiB_C_FsUGmJJu_YgXm7A8GDU1176MCH2E36bidJchS2S48hjOT3D59k1kQtbehrW6c8bt9RkuwvN-CvK6I4TwLOmUqiQOPuzuivz9rDeo6f719VY39bdN93ilN78NnA2_UHluLfWvPQViQkEtqqKgj9-sVjz5eliM4Ws2fGbAVJLKE0YgToVUMx87pqvEFFtxEU4KN7NUltuCgKc9i5FhbcpD6_m5olFKPauUeEsuHDIaqIimxtqj-TKaL74qR00YfmDSdBqjRMuV5SrMg39BE-e9ahFXYnM9Z5BJx6u6NJBRBPxwsvpXmLZ0rTFA40Ag4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی هیچ چیز سر جای خودش نیست. مهندسی نفت از امیرکبیر، رتبه ۱۰۶۵ کارشناسی، رتبه ۱۵ ارشد، ببینید شغلش چیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72413" target="_blank">📅 17:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72412">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=bAXZ0yeXHmiPksaheAVUY3ug1tQh3xxTcXSWOIG3bYZ54rGo--YGOHxmbaUmD0obquVDG5KmE41A6mHI25ksgBgxE0MNjasGsIY94lBIDgj7Ykb5E8BSaWdtqCHieqm1hoXcbwoGosF_2_XeQYNCcmGzaGst6ksLyEn2Lw-NUYxvrAuyF5HAiL2b9SotlYtbyjfkJIVA5oPVQy8q0H6Aaa0L2i9sIZKCJkrqPby0DfRQQ0APlUlxf4GAAsTQHOVgmE-KAKXAxJXFJCGjoQ_DkdM8DBjo45t2ilWH6SB9xD0LM0FiuU9TOYPDUZCRlkVe7U0y0GAeQtJGOqh6ag8zwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=bAXZ0yeXHmiPksaheAVUY3ug1tQh3xxTcXSWOIG3bYZ54rGo--YGOHxmbaUmD0obquVDG5KmE41A6mHI25ksgBgxE0MNjasGsIY94lBIDgj7Ykb5E8BSaWdtqCHieqm1hoXcbwoGosF_2_XeQYNCcmGzaGst6ksLyEn2Lw-NUYxvrAuyF5HAiL2b9SotlYtbyjfkJIVA5oPVQy8q0H6Aaa0L2i9sIZKCJkrqPby0DfRQQ0APlUlxf4GAAsTQHOVgmE-KAKXAxJXFJCGjoQ_DkdM8DBjo45t2ilWH6SB9xD0LM0FiuU9TOYPDUZCRlkVe7U0y0GAeQtJGOqh6ag8zwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه: تحقیقات با هدف یافتن «کشتی نوح» در محوطه‌ای نزدیک به کوه آرارات آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72412" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72411">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=c91BLHRTVmdYGpayDdajM0NxJPv3oaLAhGfLeolmDQraywRZit3z_4Vg1GJaWVqXaClepY0aUTGweEq8kGkwmEiipoSmUT3g9WbM-FHCbcwt1Q0W5S_0Y4HnrC89gIX1x7SG8K28RuBYoCd3nu22DISr0WUGAvWkWNmzy-TWk_bSFkuPm4rS0vXEy9yxzQv46-BaIq7cv2hlU90OTVIR9Bq9n0W5jTj0EAVbL8jBsaEXfo0PnyWgoF0Pk7MxvZ8E_HM_dNKNZ85UOfqkszNjxLTYts9EBkPAg6P8TtPYYy4_vvzB3XEALiFU3HtTnyysNgPAS6m-oIDKWAzJ586GiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=c91BLHRTVmdYGpayDdajM0NxJPv3oaLAhGfLeolmDQraywRZit3z_4Vg1GJaWVqXaClepY0aUTGweEq8kGkwmEiipoSmUT3g9WbM-FHCbcwt1Q0W5S_0Y4HnrC89gIX1x7SG8K28RuBYoCd3nu22DISr0WUGAvWkWNmzy-TWk_bSFkuPm4rS0vXEy9yxzQv46-BaIq7cv2hlU90OTVIR9Bq9n0W5jTj0EAVbL8jBsaEXfo0PnyWgoF0Pk7MxvZ8E_HM_dNKNZ85UOfqkszNjxLTYts9EBkPAg6P8TtPYYy4_vvzB3XEALiFU3HtTnyysNgPAS6m-oIDKWAzJ586GiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، اعلام کرده است که در پی صدور حکم ۱۰ ماه حبس تعزیری، خود را برای اجرای حکم معرفی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72411" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=nklTRXSjhnLhQFyHHM-XpdXqeREYuBiTQKm1JmKGhk-aJduyUnRQdzwp3c7IvojimJBymFMfX2sM8gkb9M5hay-HUt8JQLtS4O9AOVTpsBqz2mrhFgpQuECQOJev1KmX0KEwT9UizjFsYav3VL8u79gdxF4lgnkE1Z5mAq8-rKd_9a6c-kn5r0UwLxPW96gh-ydAYkPW48E7SGNTXJUbJb7PQNNFODPDtfXnqE640PjMu0FRaXrPoTt03r0XGQrrtsOrjJOPhAfzRbx-ZcP1Mwna4HWyfMnDusikaf1p3rx-HeQROUXWFNZJntEMNDJWEaSqW57_zPZWCatkFy25HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=nklTRXSjhnLhQFyHHM-XpdXqeREYuBiTQKm1JmKGhk-aJduyUnRQdzwp3c7IvojimJBymFMfX2sM8gkb9M5hay-HUt8JQLtS4O9AOVTpsBqz2mrhFgpQuECQOJev1KmX0KEwT9UizjFsYav3VL8u79gdxF4lgnkE1Z5mAq8-rKd_9a6c-kn5r0UwLxPW96gh-ydAYkPW48E7SGNTXJUbJb7PQNNFODPDtfXnqE640PjMu0FRaXrPoTt03r0XGQrrtsOrjJOPhAfzRbx-ZcP1Mwna4HWyfMnDusikaf1p3rx-HeQROUXWFNZJntEMNDJWEaSqW57_zPZWCatkFy25HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:چرا هیچ نشانه ‌ای که ثابت کنه رهبر ج ا زنده اس، منتشر نشده؟
عباس: به دلایل امنیتی!
مجری: خب چرا یه ویدیو ازش نمیاد بیرون؟!
عباس: به دلایل امنیتی! شواهد زیادی وجود داره که نشون میده آمریکایی‌ها ایشون رو تهدید میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72410" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=W8vIBpI5RArD6evmQGmXwdhY0MN3Ud3Y6PUNjCWxD2y2D0z5MY-IhmE15fX_Aung5_MQW8yBY70j0o5ztlzHKCq0xfCopL8LWt2WimUQ0o9dqT8i-_-X_KNDFqdmry0FieY2AdLE6q6oF9VytljTMM08Gx4uFCWdgKHlNmwFnBBtf9rq1rxSOpYljkGnDOHerJZheOQhcDucsq2KY37BCp4q0BE3lXDf1BCSBeatxndFfVki9FoBBQs13o0TtE8l2JtpjzuB_CTBerEwVX8Bcbxj5CRQv0pNAMrqws7_COk9w1o2EpkO6EY1gLNqNqKryEenWMKklVpqGeBsLH60sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=W8vIBpI5RArD6evmQGmXwdhY0MN3Ud3Y6PUNjCWxD2y2D0z5MY-IhmE15fX_Aung5_MQW8yBY70j0o5ztlzHKCq0xfCopL8LWt2WimUQ0o9dqT8i-_-X_KNDFqdmry0FieY2AdLE6q6oF9VytljTMM08Gx4uFCWdgKHlNmwFnBBtf9rq1rxSOpYljkGnDOHerJZheOQhcDucsq2KY37BCp4q0BE3lXDf1BCSBeatxndFfVki9FoBBQs13o0TtE8l2JtpjzuB_CTBerEwVX8Bcbxj5CRQv0pNAMrqws7_COk9w1o2EpkO6EY1gLNqNqKryEenWMKklVpqGeBsLH60sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان درباره استخاره روز اول مهر :
قرآن رو باز کردم دیدم خدا میگه بازم باید صبر کنید؛
«وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ ۖ وَاصْبِرُوا ۚ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ»
از خدا و پیامبرش اطاعت کنید و با هم دعوا و اختلاف نکنید چون سست و ضعیف می شوید و قدرت و هیبت تان از بین میرود. صبر و پایداری کنید، چون خدا با صابران است.
اینا خیال می‌کردن بد اومده بابا خیلی خوب اومده که...
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72409" target="_blank">📅 15:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72408">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مجتبی خامنه‌ای:براساس محاسبات الهی، ایران قدرت اول جهان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72408" target="_blank">📅 14:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72407">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=surQAfiOZz522g8JDLQS0WOd4iMyg-3PFL_fWQmNmbuc2pKB2Mp5-MSOs64ctgomphlO2SdPUlAYsTeqfvYSmN6pf8cz8-7KWqUlsb07dtNdVu-05k-KrdX3X5DyU9Wzl829NUTFA16IERaGRD_ZaKXOfh1613da7eurtX2D9dYfmgTuo_zBYoFBn0N2qC1n45dtDmJMoK-849RaAH5U85acrVoJ0rA_36H898-5WGsYp2LX6nO-vU2wysEWSNYQKH8Wyuaoyq1mOBDWQW3RRQiSh_uWWJ5lswk3bgrS19yZbxdYyncfOXvGUJhvGKiavgWhrHFwAx4a6qN7UeYAOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=surQAfiOZz522g8JDLQS0WOd4iMyg-3PFL_fWQmNmbuc2pKB2Mp5-MSOs64ctgomphlO2SdPUlAYsTeqfvYSmN6pf8cz8-7KWqUlsb07dtNdVu-05k-KrdX3X5DyU9Wzl829NUTFA16IERaGRD_ZaKXOfh1613da7eurtX2D9dYfmgTuo_zBYoFBn0N2qC1n45dtDmJMoK-849RaAH5U85acrVoJ0rA_36H898-5WGsYp2LX6nO-vU2wysEWSNYQKH8Wyuaoyq1mOBDWQW3RRQiSh_uWWJ5lswk3bgrS19yZbxdYyncfOXvGUJhvGKiavgWhrHFwAx4a6qN7UeYAOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر داشتن با ذوق توی جاده میرفتن سفر که یه گوسفند یدفعه برعکس اومد و باعث این تصادف وحشتناک شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72407" target="_blank">📅 14:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72406">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72406" target="_blank">📅 13:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72405">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFtCjReYexTX5uQlden4fHES9TqaO6WJJcor1Du85ajKOhwXUNbCfWhAEdAylb1ExRYhJksgsEtbz9zZ9KfR6eZ_sYkaH_IKPpBBcIdDLAJsYP0IWcMmvCWHAu-o70ZelttZEZy8rSykOZ5v2ybzqIrPiJXUqBykJ9iOj789o3d5mLb-4Q2FWtRvjPmUMk8x-Stc4T3U5dE2wIXJnk9NG0NRxXjmhLZ-lSTWCA1XrP0Z_5MHaQr8q3yCVXm-7d_i3-HftJjB6kwxI9M1my0BG3ZtvdqaYzAfKhmw76qlAGQekE_g5ifnvVFSK1j5EteNgkHQs8DdOVFUYntvIqhB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواشناسی:موج رطوبتی از شمال آفریقا در حال حرکت به سمت خاورمیانه و ایران است و می‌تواند زمینه‌ساز افزایش بارش در بخش‌هایی از کشور شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72405" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72404">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=mPiDmt9Odqy9KtvlLbj4gVhihSGSPRVRK7zWlcClzzPnJJXC-SQwV7dgxz_dXYqDL2iObZzcKMpAoCAE1nUyFXLBkDxy1MzXTr58O8yCrYoAf8HydIgupcuy9Mf3QE_Idp-8LBd19PhXg-s0Bl4olythD8VflHNN7wjG36fnITNrCKlynbtACjnmGqVu4CA-jvVqSt7mbuE9Yhgh6uNIP-ocJmcddA05VquI9NTmow-2ktcGNGx2ramUAJzM990apWMjjfdg8NdGOQwIWhPOp-us_U0Wi_IyCt49ULgJREKOUi_ssLbroOyupCQqaNw5q43MK71Jl3XDHc4vHmq56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=mPiDmt9Odqy9KtvlLbj4gVhihSGSPRVRK7zWlcClzzPnJJXC-SQwV7dgxz_dXYqDL2iObZzcKMpAoCAE1nUyFXLBkDxy1MzXTr58O8yCrYoAf8HydIgupcuy9Mf3QE_Idp-8LBd19PhXg-s0Bl4olythD8VflHNN7wjG36fnITNrCKlynbtACjnmGqVu4CA-jvVqSt7mbuE9Yhgh6uNIP-ocJmcddA05VquI9NTmow-2ktcGNGx2ramUAJzM990apWMjjfdg8NdGOQwIWhPOp-us_U0Wi_IyCt49ULgJREKOUi_ssLbroOyupCQqaNw5q43MK71Jl3XDHc4vHmq56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر نظامی وابسته به حکومت:
یادتون باشه تو جنگ ۱۲ روزه میگفتن هی F35 زدیم ولی در واقع ماکت اونارو میزدیم
این جنگنده ها از طریق الکترومغناطیس یه شبح بعد عبورش می‌ساختن
ما داشتیم پاد های F35 رو میزدیم یعنی امواج های رادیویی اونو خلاصه بگم هوا رو میزدیم
در نتیجه هیچی نزدیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72404" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72403">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72403" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72403" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72402">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI3N7P5uqAP__AHP9GkKZla4VyqCMaM0TALopP-BUEJvnyvW7-bxM16fg_7bDRYjg8CxX7tyzTkVrl5kNZfLtPRDz5B2-UvASDKGrzoBnviyZNQYsYEAU16NJ-lFnhAx5yEa5-XHdQYmKRFCpTkxjM7ORehZn_qbtv_m0egklf5Sf2IXC1plb8Eh3Rn-3vr99aPazVx5T1VFrD66F4m1MI4L4sgZaPsZCcDKN4PY70qrHxMPMMMu4-cT1ClW7q5EQx3-Ws3a4s_rU29IEK4sS_VjeZFIKso6s8r-0n5u9McBFP9wVJNBT9jJIeuO4iV32hgckKs0on47_XWJlnLiHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72402" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72401">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql8bVVDp3AWp4lfGsdOfhvZ-dgt9YfrYwHp6bcvcTEuk_-D0jhkUXdClm5SmEt3GTF8jTI_RUmBqbB0f7J-LAm_cBRgUGGZ8f-arCqSvRLUlVrPYwNEy3Q_2nuYtBZNnLQKNRtkNsq_l0OGheUKOnB-0VwdXlm65Hk0s2qMfHKpCA7bkjAyjU5MSMm4hkUOS2zBvYK3xnxreqvewfLmFrSR21MeYMa4ot0l2hVZAz5WIFf3ZwwTu_TjZqYotGFgVnP72jYQWYE-3aEeadITKBykenNeUcurJlSX9TmBzcXKSgTs_wf8oEgt_FKD1sxu04OMecXsZ2BtLua1OvRBI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی، فعال رسانه‌ای :
همه‌ی شرایط منطقه شبیه به بهمنِ ۱۴۰۴ است!
یعنی چند هفته قبل از حمله ۹ اسفند...
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72401" target="_blank">📅 12:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72400">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72400" target="_blank">📅 12:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72399">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=XJ_OkI4yOdZW0uDt3s1A0kw7BnJkAXvcDIEFPNmpFUyjxTOPf9bSczuy89PqdzEqw8his9iC5meqDSJeDDbZ3KszWSl6wOSGRjIBnnEa6C-TrFVS89Wc5YNC8_WnIapOJyLx3Ge24mPRMNrEZhy94Z54JjKvJHL5NDOjE3A8Jt-4VhceGUVhJy6Jr5TZsONjDgtBzkefo8iHuk-K7nTs6GBRXS5x4AdjzQPtSAxv-Yv_C-Q5AjYYlI5RgQMP2UE-SszRhqxvRkaBnkQtR99LRGOfXYwaBZ0-WzqkD3WCKvcSQ5oW9mxCZGHq77gItaOduK_FXlfsXIsF1fESEmN0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=XJ_OkI4yOdZW0uDt3s1A0kw7BnJkAXvcDIEFPNmpFUyjxTOPf9bSczuy89PqdzEqw8his9iC5meqDSJeDDbZ3KszWSl6wOSGRjIBnnEa6C-TrFVS89Wc5YNC8_WnIapOJyLx3Ge24mPRMNrEZhy94Z54JjKvJHL5NDOjE3A8Jt-4VhceGUVhJy6Jr5TZsONjDgtBzkefo8iHuk-K7nTs6GBRXS5x4AdjzQPtSAxv-Yv_C-Q5AjYYlI5RgQMP2UE-SszRhqxvRkaBnkQtR99LRGOfXYwaBZ0-WzqkD3WCKvcSQ5oW9mxCZGHq77gItaOduK_FXlfsXIsF1fESEmN0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلما، ماده‌یوزپلنگ هفت‌ساله ایرانی، چهار توله‌اش را به‌دنیا آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72399" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72398">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پرزیدنت ترامپ:
به‌جز نفت — که [قیمت آن] پایین‌تر از دوران دولت بایدن است — و این واقعیت که دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم چون [آن‌ها] از بین رفته‌اند، قیمت همه چیز در حال کاهش است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72398" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72397">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=maFMbk39ahqRl-MxngDdWn-avHGKHqBru5eKvQd6DUxUhZ6dg5b_Ts4ohoQsya9BRQqvK3ZCmYGTIKJRS9lg2UWTp-79F0LpFhdTJ6fFDpel52riNyDHuEcn-RigfYaF6Prjz2xJFkJnQ17VQsbAOpfnX5yc3JGwbJX06ZUNzbdy1sdw1LwMXAKZ7ggLN3L4FO8VzBhjIoMux5eL2fBOqk6rnXZ8107Nno06pnX6IeOl6ONKADytDISFSWbrBttuSC4OoUlk-aXgm0mbDZuPmDou--iCSGUYvNzGAhnNNHnaspO5buH7AZd7wBqaADHJtbLdkSrcfX5EmFyE4o7bOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=maFMbk39ahqRl-MxngDdWn-avHGKHqBru5eKvQd6DUxUhZ6dg5b_Ts4ohoQsya9BRQqvK3ZCmYGTIKJRS9lg2UWTp-79F0LpFhdTJ6fFDpel52riNyDHuEcn-RigfYaF6Prjz2xJFkJnQ17VQsbAOpfnX5yc3JGwbJX06ZUNzbdy1sdw1LwMXAKZ7ggLN3L4FO8VzBhjIoMux5eL2fBOqk6rnXZ8107Nno06pnX6IeOl6ONKADytDISFSWbrBttuSC4OoUlk-aXgm0mbDZuPmDou--iCSGUYvNzGAhnNNHnaspO5buH7AZd7wBqaADHJtbLdkSrcfX5EmFyE4o7bOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
در مقابل محاصره هوایی، می‌ توانیم بین پروازهای غرب و شرق کره زمین دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72397" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72396">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=ZQhIwCR-EcMFztuIJdMCWfI3z2b5LiafHJvVr8ZS4A9BwK58PPcZjxFHkT5EaBLhJh4smyvI2azTrqq7lWZBGzcqkDjF8fEpxzY_RnN2P4juHzTyyuLdgqpqwnScy_yASYQbVcAt1mdpC4IuVJAdBT8_Q_fn9gOrT4x_2PJsnuiEZj0IX1hmpHHR708YJh6smL3rvBR3u_N0iZZsVjxf4mNoofH2-SdRPIVoi9FbG-dgzwC4XFPlOlSg6zvJYn20wwtIrhutCQp07zeUrbD4OGGn_D62GWQbs7qc0XFZrOfR-QEjV4I3DYqIDfaXcuKTkwAE_jDRl9geAUZSfl2igw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=ZQhIwCR-EcMFztuIJdMCWfI3z2b5LiafHJvVr8ZS4A9BwK58PPcZjxFHkT5EaBLhJh4smyvI2azTrqq7lWZBGzcqkDjF8fEpxzY_RnN2P4juHzTyyuLdgqpqwnScy_yASYQbVcAt1mdpC4IuVJAdBT8_Q_fn9gOrT4x_2PJsnuiEZj0IX1hmpHHR708YJh6smL3rvBR3u_N0iZZsVjxf4mNoofH2-SdRPIVoi9FbG-dgzwC4XFPlOlSg6zvJYn20wwtIrhutCQp07zeUrbD4OGGn_D62GWQbs7qc0XFZrOfR-QEjV4I3DYqIDfaXcuKTkwAE_jDRl9geAUZSfl2igw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:ما هرگز به مردم خودمون حمله نمی‌کنیم
ویدئویی از شلیک مداوم از روی کلانتری به سمت مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72396" target="_blank">📅 10:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72395">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=hdi2hf5cquF3sLxVIYV-FxZ3vwmsdNpHTgQl0VHWlUO7kAV1e6JycS9_exiT8DVBjpDhFNu69U_tDaMZHnBvnEUfDt_QDmXKZ7pMFU1fIhVVIqbtAKcijbMJE5Yc1rq_NdaPC60EZqOSg0GX9NdZCTeIi_oCK3By7O90ZfcdyckveCnTvwMSoI04vlvLTMT4Usjx_W4JsK-3qck8wFglTOn33AUlTc3h0LuGa9f6L5gn5ZdZgcYkEseybY0Ka1pYL8jeActg_9gcBx_VkGvUhm0my1Vdd78E1BCfCt5wPZ9kxdU2ZDVkNWECdREYgB9c4oaCSrN8RYtxhbXiZFUCmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=hdi2hf5cquF3sLxVIYV-FxZ3vwmsdNpHTgQl0VHWlUO7kAV1e6JycS9_exiT8DVBjpDhFNu69U_tDaMZHnBvnEUfDt_QDmXKZ7pMFU1fIhVVIqbtAKcijbMJE5Yc1rq_NdaPC60EZqOSg0GX9NdZCTeIi_oCK3By7O90ZfcdyckveCnTvwMSoI04vlvLTMT4Usjx_W4JsK-3qck8wFglTOn33AUlTc3h0LuGa9f6L5gn5ZdZgcYkEseybY0Ka1pYL8jeActg_9gcBx_VkGvUhm0my1Vdd78E1BCfCt5wPZ9kxdU2ZDVkNWECdREYgB9c4oaCSrN8RYtxhbXiZFUCmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد تو سطح نیویورک دارن خطر ایران هسته ای رو نشون میدن ، این میتونه آماده سازی افکار عمومی رو برای شروع یه جنگ بزرگ باشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72395" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72393">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=Pl3AlfFDJr__UTYA_XrtUixax63_nkuv4bFhsFzC_bZsL1OVjz4MWowIpYx8byuxSFKM_QY2LAJD4EJqwCQIEzvZofBQdgnglW-Cm85raw9p9xg9RWGdJ6Ka3mgLsFWLOGh2jqDnj2_4U9paoYUPdBqaTidfhEdQDZJfPiRsIqs5uGjH8ZdRXcluZgyMgx1k3ugV7MUHwwD6EnoHI4bl3aaH-2WYpXvErq4Y4OfySuwVbhnZ9lZtoEX1tV_p6Vle9XYDDty1GxEdhuNuPhnD5kYTrKhw9zkQ4o-Vnk3o0JJr2OnjCIRmETrnainBeJHtgxS6HkC_6q5VzD56XW4Dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=Pl3AlfFDJr__UTYA_XrtUixax63_nkuv4bFhsFzC_bZsL1OVjz4MWowIpYx8byuxSFKM_QY2LAJD4EJqwCQIEzvZofBQdgnglW-Cm85raw9p9xg9RWGdJ6Ka3mgLsFWLOGh2jqDnj2_4U9paoYUPdBqaTidfhEdQDZJfPiRsIqs5uGjH8ZdRXcluZgyMgx1k3ugV7MUHwwD6EnoHI4bl3aaH-2WYpXvErq4Y4OfySuwVbhnZ9lZtoEX1tV_p6Vle9XYDDty1GxEdhuNuPhnD5kYTrKhw9zkQ4o-Vnk3o0JJr2OnjCIRmETrnainBeJHtgxS6HkC_6q5VzD56XW4Dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ناو هواپیمابر «یو‌اس‌اس تئودور روزولت» (CVN-71) از کلاس نیمیتز، در چارچوب استقرار برنامه‌ریزی‌شده نیروی دریایی آمریکا در حال حرکت به سمت خاورمیانه است. این ناو پیش‌تر از سن‌دیگو خارج شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72393" target="_blank">📅 06:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72392">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72392" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72392" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72391">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hilx__xigc_xYZTLqW90t9lni3QIR6NdUIrZD4lKrdggLjPAdvr0utcFK8MEDc7H1k8gZmgj27pXVuy3hO7IY0oZ9b0-yqJpEv2t09XdRn4S7rtCJkUvT2KFeKobtKipVczaeL61M0Dm1HQ0P1eASXOzrNrPC80pMB53E9CbXliyVTxmZaNQcPYW6PHpIZVpk3Qd5kIpnM1b6IvHkziqLiLOE6oW_N9YGUksjj7k2IEqVKEgxR7U4ptmALdRRGcqmb1o6TIDIbsPVDf33yLkG4gLZJZoV5mgCtEr9iGlAOspDtTKKN9IX4R-4VpuB0DV0rQVOFHEj6NsIIOxJ6OcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72391" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72390">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b361018705.mp4?token=LbzhmpzQVjOkyKPvf2vPt65V_PBsUeA7kC1eEfCoKub9El3SleAb6NFXWaJrrYXQGvn8IXJ5f4vaQus5Yxrow_l1MfKCToPdYFd-duO3UrTx2PbQIlQ1F4BsKjdYgcD_9_kB6eywhPinKMJ4-Q6agW0B3zn0FeqR-GxkpRE9VAKSWE252AyeFMrmoJcA92P3BvAakb5AMcfQW-ytF1fW7mj_g2ueDUg8W9S_jh-YUy5W48aSKWFE0zGyhRuGtwFceZWv136EMMzk1a_JtWmmJOGy-UpfkuMW-mXPpj6pZc9wW_RdAoEDLsg5ovX-VJeL8JJ_sQhEEihqCjU8KLAqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b361018705.mp4?token=LbzhmpzQVjOkyKPvf2vPt65V_PBsUeA7kC1eEfCoKub9El3SleAb6NFXWaJrrYXQGvn8IXJ5f4vaQus5Yxrow_l1MfKCToPdYFd-duO3UrTx2PbQIlQ1F4BsKjdYgcD_9_kB6eywhPinKMJ4-Q6agW0B3zn0FeqR-GxkpRE9VAKSWE252AyeFMrmoJcA92P3BvAakb5AMcfQW-ytF1fW7mj_g2ueDUg8W9S_jh-YUy5W48aSKWFE0zGyhRuGtwFceZWv136EMMzk1a_JtWmmJOGy-UpfkuMW-mXPpj6pZc9wW_RdAoEDLsg5ovX-VJeL8JJ_sQhEEihqCjU8KLAqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای همچنان برای شما مطرح است؟
ترامپ:
نمی‌خواهم چنین حرفی بزنم. یعنی، ممکن است [چنین اتفاقی بیفتد]، اما صرفاً نمی‌خواهم آن را به زبان بیاورم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72390" target="_blank">📅 01:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72389">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e157d195.mp4?token=S_JvL-lHoaJ5OgL5jeW7tdybn1WyOBB00V21Hk48mBHckoVfPU6xWyz4hwQdLnjmfgpjQkMtiqUTGAv_lb_mwkEP8EeoC2tWJQ7txX_4af--VnKFIwGPg5JjVLxtnswL4039ibS4ILTXJl1H0heQBvLzOPSTFV73_VV3FcubzqaV6XLKMviwV8kZHtta3aFe7Yp0MacgPlxpHSpAoVSMyopMYoz3C0e7mGQKVb3m_Xcw9ilacUPrbji2hmoB62d94yfy4UrTAZBbD8CmOMXUIKIZWxwHswYv-M1ASEMlsrrrbJASn80U3SATMTrfui-9-OTpc_EVXr8QHK2h3UjXiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e157d195.mp4?token=S_JvL-lHoaJ5OgL5jeW7tdybn1WyOBB00V21Hk48mBHckoVfPU6xWyz4hwQdLnjmfgpjQkMtiqUTGAv_lb_mwkEP8EeoC2tWJQ7txX_4af--VnKFIwGPg5JjVLxtnswL4039ibS4ILTXJl1H0heQBvLzOPSTFV73_VV3FcubzqaV6XLKMviwV8kZHtta3aFe7Yp0MacgPlxpHSpAoVSMyopMYoz3C0e7mGQKVb3m_Xcw9ilacUPrbji2hmoB62d94yfy4UrTAZBbD8CmOMXUIKIZWxwHswYv-M1ASEMlsrrrbJASn80U3SATMTrfui-9-OTpc_EVXr8QHK2h3UjXiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا فکر می‌کنید ما در این جنگ [با ایران]، از طریق جنگ اقتصادی که وزارت خزانه‌داری به راه انداخته یا با حملات نظامی پیروز خواهیم شد؟
ترامپ:
فکر می‌کنم هر دو. به نظرم از هر دو طریق پیروز می‌شویم. از منظر نظامی که عملاً پیروز شده‌ایم، اما این بدان معنا نیست که آن اقدامات را متوقف کرده‌ایم.
ولی قطعاً داریم با اقتدار کامل در آن پیروز می‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72389" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72388">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3da141396.mp4?token=B5lUkKkkcK7s7uU9TDuQrx8VY9VyIfPVzvvf0ix79xBV1cqpmD1SKlsdAHnQFz4a1vAQvP4f3yg5reU3pI0RSqal0uOpmWBn1rLizpWjxsvB_atefNKHgnlWWFS1moDQng6q0foQGqN09YHRWkLXDG0oX-xdaMGkiE9MEAIXxCtQX3u80ohkeOCsfFlG525jzLN5M_BS3TY-eO3n2omTsxSc2o1CEZD0cO-G4ew0jnFkxJwpmP87XNk-ir8kWaorqhbsufRWAH9Wk1umMyUw0RgPx6BVHG2aOnMoCUXc0l5JSYns205_FByo-wKGD94XnXAI1UYwuZUCGv0V5FO1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3da141396.mp4?token=B5lUkKkkcK7s7uU9TDuQrx8VY9VyIfPVzvvf0ix79xBV1cqpmD1SKlsdAHnQFz4a1vAQvP4f3yg5reU3pI0RSqal0uOpmWBn1rLizpWjxsvB_atefNKHgnlWWFS1moDQng6q0foQGqN09YHRWkLXDG0oX-xdaMGkiE9MEAIXxCtQX3u80ohkeOCsfFlG525jzLN5M_BS3TY-eO3n2omTsxSc2o1CEZD0cO-G4ew0jnFkxJwpmP87XNk-ir8kWaorqhbsufRWAH9Wk1umMyUw0RgPx6BVHG2aOnMoCUXc0l5JSYns205_FByo-wKGD94XnXAI1UYwuZUCGv0V5FO1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به گمانم آنچه رخ خواهد داد این است که ما خیلی زود در این جنگ پیروز خواهیم شد؛ و به محض پیروزی، قیمت نفت کاهش می‌یابد و به شدت افت می‌کند تا به سطحی برسد که پیش از جنگ بود.
و نکته کلیدی این است که ایران به سلاح هسته‌ای دست نخواهد یافت. این کلیدِ ماجراست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72388" target="_blank">📅 01:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72387">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91575662ab.mp4?token=qrTkQw6aJWvNGvdckim9G1EPiEU3mRN9p_mVpC_TuGiYt_gXjyIN3ZulEHzpiuAxlZE156HheJ40Wb5feFzRSlItq4QINMOYlg9Qm204OPZgYOFDPySVeKokaA10Xtjaxtvka9X-WdmvcPPdRxUnBpZGLsQo1l_qTv0MaPL6NkmQwYfM24gOAXnt8QcqrxZ84cxIGUK8XzYLHN7v8-Zi9GPDN4QHqI8d2BW_QVqCTmMR1nw3zeGuy9Uw9R9gUQ_gu69EOuuGHJE7P85RoDQaWmLrxUsw8XL9vpnmAd_S8bG8PM1R-hl6ExZ83YbhOJU-DeXimlGkVT6h11LI-t3bfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91575662ab.mp4?token=qrTkQw6aJWvNGvdckim9G1EPiEU3mRN9p_mVpC_TuGiYt_gXjyIN3ZulEHzpiuAxlZE156HheJ40Wb5feFzRSlItq4QINMOYlg9Qm204OPZgYOFDPySVeKokaA10Xtjaxtvka9X-WdmvcPPdRxUnBpZGLsQo1l_qTv0MaPL6NkmQwYfM24gOAXnt8QcqrxZ84cxIGUK8XzYLHN7v8-Zi9GPDN4QHqI8d2BW_QVqCTmMR1nw3zeGuy9Uw9R9gUQ_gu69EOuuGHJE7P85RoDQaWmLrxUsw8XL9vpnmAd_S8bG8PM1R-hl6ExZ83YbhOJU-DeXimlGkVT6h11LI-t3bfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو سالگرد ترور نصرالله رو با انتشار چنین کلیپی به مردم اسرائیل تبریک‌گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72387" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72386">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-YX_HQLaNXs19yKLuytXZIvVbU-f3GJv3Lc3qMqyss0YrPk6FUlMclKJ1VnSjNSeRFGAqVxxwC4_fIN_yer_ly0dTDEMHPFywmAAV6T76w7mnVmri3tjaioy9FjMyg7gIy7I6KnROco7hEtH26XrL8gycTRHe8UV4VrnMVKnfTImP-hsfWFNmrZA77dkA3immA3rFlmv-mTtCvti8TISpKyAm7ubQ5NKadRPFzguCVTbCV2_uCs4eMvOfG7Bpt21PXJ1gz7VZe32wT2iVDtBWzk_zXQ2X5wLtGiewcz5u0ep8vBC7aFvW_5arIpsOtmxSdOV0XeujHJ9PDF9n9tUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، امروز سفری محرمانه به ابوظبی داشت و با محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
نتانیاهو صبح امروز با یک جت اختصاصی سفر کرد و بخش عمده‌ای از روز را در امارات گذراند.
محور اصلی این دیدار، ایران بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72386" target="_blank">📅 23:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72385">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CThdBT-f9mKq_fLAdEhnKBZM1b9Y_h1V3wgMXEVyW_NrNhXOQllnA3GYiHE6E4DrpiCG4hQEmdFELy5sSyZ2fl59at56oVlgcfHi7i1WzG4ERlg-skAjpFi_hWDeD-OrAmChs8MdUyNm6cJneD79fpPbo8nCP3ozPBt5rqTFhp0VctabLh3zkMAhdm0KbsL_N8M_XtUSbqkkZvDwNbsdOWyA6jdbqg1sSslbf79ZdTScdE2YSCA5hDfibeYXBIRP8O_ghoEw-kNGP01Zgt30mnWJIQ2u-EBklVevHu8-Jy78PjGh5mPAZDAs7AUTXkJos5aWqWibRJfkc67jJ5_Sdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق‌ترین و مفهومی‌ترین عکسی که میتونین ببینین:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72385" target="_blank">📅 23:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72384">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الکساندر ووچیچ، رئیس‌جمهور صربستان، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72384" target="_blank">📅 22:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72383">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72383" target="_blank">📅 21:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72382">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=IYMothV4nwCqHoiq3o4_HDyZoJ_gaK2Y0SlyX7EVPI0Gk64AS-_GlK6jlcyQFiZw7MKbOxn5vjs0z4nPrgmIj7Us9DBnynHOtc8WBV5RU_5USIgxLVrbI_AiZOJ_Ge4qT6zq-vAG8CTzDoPIz3G3YBCIhtFc80ajmd2oiJW7_umZ7F1raw9KuV1NFFPvwtVf1Oro884lNSUGRvJFcr7RcG7dtvbCcHE5X3NZGSRduKsT8rP3-aNOw-vZ-syxV1R3nJW10fy-CQ8WLzzpRJQg-EW5Fb_zmciQVsoJ2q6GaEaUOGqqBUSHk2BsAwXT6bhrb1GdzrqdgY1r_7gkgWRYNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=IYMothV4nwCqHoiq3o4_HDyZoJ_gaK2Y0SlyX7EVPI0Gk64AS-_GlK6jlcyQFiZw7MKbOxn5vjs0z4nPrgmIj7Us9DBnynHOtc8WBV5RU_5USIgxLVrbI_AiZOJ_Ge4qT6zq-vAG8CTzDoPIz3G3YBCIhtFc80ajmd2oiJW7_umZ7F1raw9KuV1NFFPvwtVf1Oro884lNSUGRvJFcr7RcG7dtvbCcHE5X3NZGSRduKsT8rP3-aNOw-vZ-syxV1R3nJW10fy-CQ8WLzzpRJQg-EW5Fb_zmciQVsoJ2q6GaEaUOGqqBUSHk2BsAwXT6bhrb1GdzrqdgY1r_7gkgWRYNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم یه حماسه‌سازی دیگه از مسعود :
🎙
مجری شبکه فاکس نیوز:
آیا شما اورانیوم غنی سازی شده 60 درصد رو تحویل میدین؟
مسعود پزشکیان: بلهههه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72382" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72381">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=d4c_NKa0UXds5FEgRNObsxK6GklS5BsydEU7nd7OFmvLADXYHIu9PpPzXFVmhztW8zHRU00R_caIuvu4-s8n5mA1OaapANuZz1B0B277b20lntywBFh53Q22ZWW_VUR4D7GkPSUOaKCd2q9LjSx9k1eEDn9FaRWpMnzmcDS5GBPr5-cfxEeLSyBvtV5P91oT4OdmUlpuCzoXpLDyFbucw9rQEbm_97xvSX1I450k5MhGU35XvFHfGT0X3kjN3uteH4Iyp69-fCnpFAO1hzq4IGNvCgoAiIKreQb1xjpRp-ehMq72Y5cKygYuEkJqXUrX518pXe7gHQzZSeRycVgkKybhvAax1uFlDteWuKltxQ2n3Kcz2xGSXPxPOQnWFYGxmq8aiE81acU65rs-7wyOaoA2UnRa0eu_TfNK70aU3aAVhVbcKaswJdwY0b9mvEUbivfzSdkn8HIL4YB9LYBQzApQkDpd45DCiMQWxtHcu5FMtMcDJ8S52H6f9lbxboWIISwMbs00nmukuuNGJtCEE94VU71xA3a6AqVhR5qm4bl8Iupkg-PYa0jHOzMIzFPZmus_bYp_eMeV6chwn8ij6yzgb2ZqvyGL7AQ_2xbkwRS-uQpmxSiJJabDLI4AtIVWEv7Oxrtec2oz9v_upiY97soiIKLKsKtMpkLmG017FjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=d4c_NKa0UXds5FEgRNObsxK6GklS5BsydEU7nd7OFmvLADXYHIu9PpPzXFVmhztW8zHRU00R_caIuvu4-s8n5mA1OaapANuZz1B0B277b20lntywBFh53Q22ZWW_VUR4D7GkPSUOaKCd2q9LjSx9k1eEDn9FaRWpMnzmcDS5GBPr5-cfxEeLSyBvtV5P91oT4OdmUlpuCzoXpLDyFbucw9rQEbm_97xvSX1I450k5MhGU35XvFHfGT0X3kjN3uteH4Iyp69-fCnpFAO1hzq4IGNvCgoAiIKreQb1xjpRp-ehMq72Y5cKygYuEkJqXUrX518pXe7gHQzZSeRycVgkKybhvAax1uFlDteWuKltxQ2n3Kcz2xGSXPxPOQnWFYGxmq8aiE81acU65rs-7wyOaoA2UnRa0eu_TfNK70aU3aAVhVbcKaswJdwY0b9mvEUbivfzSdkn8HIL4YB9LYBQzApQkDpd45DCiMQWxtHcu5FMtMcDJ8S52H6f9lbxboWIISwMbs00nmukuuNGJtCEE94VU71xA3a6AqVhR5qm4bl8Iupkg-PYa0jHOzMIzFPZmus_bYp_eMeV6chwn8ij6yzgb2ZqvyGL7AQ_2xbkwRS-uQpmxSiJJabDLI4AtIVWEv7Oxrtec2oz9v_upiY97soiIKLKsKtMpkLmG017FjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:
رئیس‌جمهورایران این هفته اظهار داشت که ایران هرگز به دنبال سلاح هسته‌ای نبوده است؛ با این حال، ایران اورانیوم را تا سطح ۶۰ درصد غنی‌سازی کرده که این میزان ۲۰ برابرِ درصدِ غنی‌سازیِ مورد نیاز برای تولید برق است. چرا ایران به ذخیره‌ای ازاورانیوم با غنای ۶۰ درصد نیاز دارد؟
عباس عراقچی:
اولاً، غنی‌سازی تا سطح ۶۰ درصد غیرقانونی نیست و همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد؛ ما این کار را برای اهداف مشخصی، از جمله مصارف پزشکی و دیگر مقاصد، انجام داده‌ایم. با این حال، ما پیشنهادی برای تعیین تکلیف مواد غنی‌شده تا سطح ۶۰ درصد در سال‌های ۲۰۲۵ و ۲۰۲۶ ارائه کرده‌ایم؛ موضوعی که اگر آن‌ها حسن نیت و عزم واقعی خود را برای صلح ثابت کنند، قابل بررسی است. پیشنهاد ما این است که مسائل پیچیده‌تر به مراحل بعدی موکول شوند و در این مرحله بر اعتمادسازی تمرکز کنیم. به همین دلیل، ما این طرح هفت‌روزه را بر اساس تفاهمی‌که در گذشته با صاحب‌نظران آمریکایی داشتیم، ارائه کردیم. نخستین گام این است که دارایی‌های ما که به‌طور غیرقانونی مسدود شده‌اند، آزاد شوند؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72381" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72380">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صدای انفجاری از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72380" target="_blank">📅 20:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72379">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJKBAeOJ4UqERMkadPZl3zdSkDHIGYgHXQ51HJAIT7NRG0dpUO2EJdE-SVgOtaNNBDkpD3n0Ajxt9DCyb_MdQL4nf6FCRpRQyOH7eNmDFANoBdZ90WQ6K6LQA5FE1dbh9R31ffz-tFYcfqS4DHOD55nC0MU1TVYoIgl9WIuJs85qoES9wMZXYiTcRxzfmtTj3ncZxO3nfhx6N2X6oWLNeOTLzYcrjXyFZ6_qFE-OLdKKW8VQK8RZBDtSHLTrSZdbhmebRIharhBabD1QMx0WifgQtTQxzd83UkOi7L4G5c0ieu3hSjVUd0qJaj0qhpCtx5z0h__ospYy44C8oTTo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آوش به نقل از اداره حقوقی مجلس: حمید رسایی به ده ماه زندان محکوم شد
آوش:
این پرونده که دوبخش دارد مربوط به سال ۱۴۰۲ و زمانی است که حمید رسایی هنوز نماینده مجلس نبود.
حمید رسایی که از حکم شعبه دوم دادگاه ویژه روحانیت تهران، برای عذرخواهی نسبت به انتشار مطالب خلاف واقع درباره مجلس شورای اسلامی امتناع کرده، با حکم قاضی برای تحمل ۱۰ ماه حبس تعزیری به اجرای احکام احضار شده است.
بخش اول پرونده مربوط به انتشار مطلبی با تیتر «دستکاری قالیباف در اسناد مجلس» در صفحه اول نشریه «۹ دی» است، و بخش دوم مربوط به انتشار کلیپی تصویری در کانال تلگرامی متهم که رسایی در آن از تعبیر «دیکتاتور پارلمانی» برای باقر قالیباف می‌کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72379" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72375">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lm9za5NApmGPGLRkzx32mKH56q6V5_TXYtmm2JppJ0UpgnYvolG8XsYJhLxP1Yn6B_e3nuXHLzkbQtOkO1RKqKrAzWZ4QCRNJ5xO3RQ_qwdc-Vx2Zyk0z8KDoyU1Na6tbmTp0GsYbrgcDaxO9KBiNs5gFnudH4VwdPmh1TGUAVsUoFVmLNfS1avaRiMG4rdagAo-pWp3nDOUfAxmA5VzTIKQml7UAVR0K7tVCn6iGT9wV7ULrIHeZGvh_nKs59VTEcT0DlcKBQuSCP4JjYipPpYFBkEDbr8hovD4-Prl1te9GZxUKJPopJzom6hdOTUy03CxdFL2p98xgVASFj7pvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuEKxPqSAVTe0Y2XDc2HlCQoVHI3ZpYGDVbt8WROpHnWO7e1dct8nWm4C-LA0RYwQmJbVHc-3PQBvnWpNiHhTTCi1aQNUqyIYBbPtni8qOsWPUYRgGJ28lL6nB7H_VOBg6J5sBxIeZPCYQWOcc1WVtPAGB_Y2Wd1DlavxmDv5xuGCkOmLb2crDII8dO0bJV8B-AEnLQDxzxeCRwDIJh-RXdmk9l8ynM0wrSbq1zWPDyW5lnobTVX0ltzqtqc7BccWjSjGDJw2kvJtZOla5ArxTinsfr8OsLX7ZELrOfg-pMLMAqFrRfQMlEhDDHMjCgQFJygBOoMCaQ_gUd5xL9zFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=d4R0KND9XEKAYbgzhkK-Mu9mB88vH5uZZMIewiQ7obs3h4ZnfjoCNJWKZqjfaP-lpIOnAgSDEcPtEZUeagFcKiduQZmAuXiz99INsIuKCoa46nnusPjo7yglz5zY0g-Cgw3DTR_DvkFmSPtccr9hckdwondiZdJsIMgFTkGHex96BlbsdoGbIWpd5_zqqUGYelTk2V4paaa7YOzjnysY3i8wc8tIISyjKuW7mI-4-5MkKxUFY-9FnIn-mghvl6XeErBWKL3KAmW-4vVsC1k1CNTWPzKEAQwJ4HuV7Uy4dlFKAc1aaOtOndWdaR38mylrS7e0g0fzjuLz4NLh65I--03xr04zF_PuoNT6sFR_eNn5cvFZMs7qux1tJHjZMtSakShAg30OUEjv5DTVt62GXsyoqT35ZD9cDdPRau5xDF1GOjLW6-DD9Q2ahd61Qn8mOG7do2u_J4VRjCAtSpqu57vH1Nnegz2aj3Adu_BnUaOHQYODdkCxAPpQS4tblYUvDAP3fNjPKfINvG3OQYQFaq4M4h4pNvmpmlHjVIjiGBB7rCFr9tNTAs9zWejTHoUpPqx5cVmtFZMkhFr8F_4blEe64rY-BqZtgxp7I1v2QYtpxbRFhaYqNpMU97TTaNfp2oQi2rSCZolUowm1If472jGRIj-dtz8wdtwyR1zX06U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=d4R0KND9XEKAYbgzhkK-Mu9mB88vH5uZZMIewiQ7obs3h4ZnfjoCNJWKZqjfaP-lpIOnAgSDEcPtEZUeagFcKiduQZmAuXiz99INsIuKCoa46nnusPjo7yglz5zY0g-Cgw3DTR_DvkFmSPtccr9hckdwondiZdJsIMgFTkGHex96BlbsdoGbIWpd5_zqqUGYelTk2V4paaa7YOzjnysY3i8wc8tIISyjKuW7mI-4-5MkKxUFY-9FnIn-mghvl6XeErBWKL3KAmW-4vVsC1k1CNTWPzKEAQwJ4HuV7Uy4dlFKAc1aaOtOndWdaR38mylrS7e0g0fzjuLz4NLh65I--03xr04zF_PuoNT6sFR_eNn5cvFZMs7qux1tJHjZMtSakShAg30OUEjv5DTVt62GXsyoqT35ZD9cDdPRau5xDF1GOjLW6-DD9Q2ahd61Qn8mOG7do2u_J4VRjCAtSpqu57vH1Nnegz2aj3Adu_BnUaOHQYODdkCxAPpQS4tblYUvDAP3fNjPKfINvG3OQYQFaq4M4h4pNvmpmlHjVIjiGBB7rCFr9tNTAs9zWejTHoUpPqx5cVmtFZMkhFr8F_4blEe64rY-BqZtgxp7I1v2QYtpxbRFhaYqNpMU97TTaNfp2oQi2rSCZolUowm1If472jGRIj-dtz8wdtwyR1zX06U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ساعات اولیه ۲۷ سپتامبر ۲۰۲۶، ساکنان از سه وسیله نقلیه مشکوک که به سمت پایگاه نیروی هوایی سلطنتی فیرفورد در حرکت بودند، خبر دادند.
یک توطئه تروریستی برای انفجار پایگاه نیروی هوایی سلطنتی فیرفورد وجود داشت.
پنج مرد در منطقه ویلفورد به ظن ارتکاب جرائم تحت قانون مواد منفجره دستگیر شدند.
پایگاه نیروی هوایی سلطنتی توسط بمب‌افکن‌های آمریکایی برای حمله به ایران استفاده می‌شود.
پلیس مبارزه با تروریسم در حال بررسی این موضوع است که آیا ایران پشت یک توطئه بمب‌گذاری مشکوک با هدف قرار دادن یک پایگاه نیروی هوایی سلطنتی مورد استفاده نیروهای آمریکایی بوده است یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72375" target="_blank">📅 19:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nHOiCIvaFQPeb8UfzLNqjGk14St_QrjaIUPQAnCYDet2FYILaYipkCTkzjEWOIX2NxFLYp8ytZX-7Bu8UpLLblQqmHsveI2U-3HEawSfnEs0vofHSgfibpQD-spn6mqA3WMflaU_PugOUqtXhFonGdy5GzIto5xV8RUohhIkWQhWsEQ32m-VkgIxxcGSAx4wTXBaNOJCp9L8LalHXFwidiTNoVXVpAl0PIVyBlCkU2AYMFSq--rhx7X4hiVflaIHmF-dX0smpgC09cCdUXNhODGi56LoFQ_6dfOel9isR5PFYEvt0Cxp-C_15ThOOSwOM58iHvQQqFQzn84LKTDn98g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nHOiCIvaFQPeb8UfzLNqjGk14St_QrjaIUPQAnCYDet2FYILaYipkCTkzjEWOIX2NxFLYp8ytZX-7Bu8UpLLblQqmHsveI2U-3HEawSfnEs0vofHSgfibpQD-spn6mqA3WMflaU_PugOUqtXhFonGdy5GzIto5xV8RUohhIkWQhWsEQ32m-VkgIxxcGSAx4wTXBaNOJCp9L8LalHXFwidiTNoVXVpAl0PIVyBlCkU2AYMFSq--rhx7X4hiVflaIHmF-dX0smpgC09cCdUXNhODGi56LoFQ_6dfOel9isR5PFYEvt0Cxp-C_15ThOOSwOM58iHvQQqFQzn84LKTDn98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
ایرانی‌ها می‌گویند که تنگه‌ها را ظرف ۷ روز باز خواهند کرد؛ [در حالی که] تنگه‌ها باز هستند.
ما اکنون به‌طور میانگین روزانه ۱۵ تا ۲۲ میلیون بشکه [نفت] صادر می‌کنیم.
نتیجه این است: ایالات متحده بیش از ۱ میلیارد بشکه صادر کرده، و ایران صفر.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72374" target="_blank">📅 19:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b7065503.mp4?token=CmSHW1kuPcMGXWwAmAZzhKzo_y8M1C6QMDFwR4iB0HUbXTt4ecyBHHNdS5tEmWapaT-BqWLVDegs5pPXPrFVP8isvXM66QMpu_cA_C-uXad8DxaqVKgCzK_tK48cq2r-iQkrzLTAspMvIN6KpP1i2OqwQnabBaI3hudg3e7hRO8Yy1W9UESqHsvD1FztnRTTCPSfHYDtsGDQKVMtMSrec837GnMnw6rlOULnrJ_31p6ETbambv1QAM5wwyDCV_BTBdjg6hxpJIGkbhgZIuGF35lrJEr_MGXAYNltI0b7eBuZXXrfWNt0KjeOibdBU0p0a0XNKJodnciBdWf4SzNgBoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b7065503.mp4?token=CmSHW1kuPcMGXWwAmAZzhKzo_y8M1C6QMDFwR4iB0HUbXTt4ecyBHHNdS5tEmWapaT-BqWLVDegs5pPXPrFVP8isvXM66QMpu_cA_C-uXad8DxaqVKgCzK_tK48cq2r-iQkrzLTAspMvIN6KpP1i2OqwQnabBaI3hudg3e7hRO8Yy1W9UESqHsvD1FztnRTTCPSfHYDtsGDQKVMtMSrec837GnMnw6rlOULnrJ_31p6ETbambv1QAM5wwyDCV_BTBdjg6hxpJIGkbhgZIuGF35lrJEr_MGXAYNltI0b7eBuZXXrfWNt0KjeOibdBU0p0a0XNKJodnciBdWf4SzNgBoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی مانده است. ایران دیگر چیزی برای معاوضه یا دادوستد نخواهد داشت.
احتمالاً ظرف دو هفته آینده، آن‌ها آخرین محموله‌های نفت خود را به چین تحویل خواهند داد و پس از آن، دیگر چیزی در اختیار نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72373" target="_blank">📅 18:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO61tQ8lUHOrdizKnSo1rGAWtXQatD9cficzTHB0XWtlPmAkylekzPavCyFHXgf63Zc1D_-DR3R7miU8gbUPq0JKuKpFPzmxGMbKxOWvNwmnV06E8SrozlsbkOL-BdaOFkqURicF4hPZelwOx4_Z2zRghanjkoG121cCmX1ad9hRoJAZrzv4bwWilLJ4xeqaUTg62_kLNMz5my5JD1M2M1dp20LjG-v54gxXhXDg_4saMVDxbzPTZurpSP0gvQto45Ej0QZ3pgwkMuwZUMzsUzgZJ0XZpqXLCZHl8GEx7slpZWXXAd6d6UFF9hk1dRLoJ5hk5UyO-iOgb1-JFp-lXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به «اکسیوس» گفت که با وجود رد پیشنهاد ایران، انتظار دارد در هفته جاری مذاکرات بیشتری میان آمریکا و ایران انجام شود:
آن‌ها خواهان توافق هستند، اما این آن توافقی نیست که من می‌خواهم. آن‌ها در بازی خود زیاده‌روی کردند.
ترامپ در پاسخ به پرسشی درباره ازسرگیری حملات:
همواره به آن فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72372" target="_blank">📅 18:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72371">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=SQZAc37X4rsnto6ulhfZLFHTDc21q087_L391C3-SJiSyoOEaoHu9jul6lPoEIded1wpTVoBoDPk_T8JTgG09msmOBOsmKYfdpnc60K34WJonQ5ebddGyOuhysM7kzQf6sCl3exbEb3_jhFJ4hHyKnFCZUR-Ad5Y3lxOasuR7RRhxQg1JQOzNRGUFcRJ3hZbNYIPHKo9wcQzSjJfkqubZ36hUX6RfjlwLBZJfo0DzC4fhHJFT7-NiTDqCc7T4oD5NP-qOGxAWSRGbO-B7qlE6GbRnH14Lu1_HCGmNxsZlAXZe8JN_Le1LqwyRZxb5FVk5IUnU6kikiI2nhyRy5QvYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=SQZAc37X4rsnto6ulhfZLFHTDc21q087_L391C3-SJiSyoOEaoHu9jul6lPoEIded1wpTVoBoDPk_T8JTgG09msmOBOsmKYfdpnc60K34WJonQ5ebddGyOuhysM7kzQf6sCl3exbEb3_jhFJ4hHyKnFCZUR-Ad5Y3lxOasuR7RRhxQg1JQOzNRGUFcRJ3hZbNYIPHKo9wcQzSjJfkqubZ36hUX6RfjlwLBZJfo0DzC4fhHJFT7-NiTDqCc7T4oD5NP-qOGxAWSRGbO-B7qlE6GbRnH14Lu1_HCGmNxsZlAXZe8JN_Le1LqwyRZxb5FVk5IUnU6kikiI2nhyRy5QvYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
ما همان‌قدر که برای مذاکره آمادگی داریم، برای رویارویی با هر چالشی نیز آماده‌ایم.
ما در برابر هرگونه تجاوزی علیه خود قاطعانه می‌ایستیم، حتی اگر کار به جنگی آخرالزمانی بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72371" target="_blank">📅 18:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72370">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حملات اخیر پهپادهای جت‌سوز روسی «گران-۴/۵» (Geran-4/5)، یازده مرکز داده اوکراین را هدف قرار داده است که شامل ۱۰ مرکز در کی‌یف و یک مرکز در دنیپرو می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72370" target="_blank">📅 18:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72369">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=ALVUv6hAog79KqxAE-30KBA5uJx4sv_pM8aF5Q20YAEgNcsXylAKsxd0RPSOl3SLtmtcEM_EcWyHMjA4mbMs0GAjBFYE9xGmmlXA1mugf5dmS8aUhvyDMsQJQlSE3rZpFH1sScvUdQ-gIisKqZjqMDX5WoBPb0otdri9cmp3IlKhA1aJkjQj-tMAPTbKJQbFreRe6zEcXooxVNf_xMelCfSETup1C1cvk4UB-iUFJzQWIiR_YGx4XMPfV6pxOOM69kKqwtOz17dvH-olSnJvvowplJ1TY0Adi8PE2XJcktdEQsz6wR0Btsb1bhssVLGbOYYZ0FpTOen4u4IhYH1_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=ALVUv6hAog79KqxAE-30KBA5uJx4sv_pM8aF5Q20YAEgNcsXylAKsxd0RPSOl3SLtmtcEM_EcWyHMjA4mbMs0GAjBFYE9xGmmlXA1mugf5dmS8aUhvyDMsQJQlSE3rZpFH1sScvUdQ-gIisKqZjqMDX5WoBPb0otdri9cmp3IlKhA1aJkjQj-tMAPTbKJQbFreRe6zEcXooxVNf_xMelCfSETup1C1cvk4UB-iUFJzQWIiR_YGx4XMPfV6pxOOM69kKqwtOz17dvH-olSnJvvowplJ1TY0Adi8PE2XJcktdEQsz6wR0Btsb1bhssVLGbOYYZ0FpTOen4u4IhYH1_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جعفرقائم پناه؛ معاون اجرایی پزشکیان:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگه به پایگاه‌ آمریکا تو کشور شما حمله نکنیم بلکه مستقیماً به خود کاخ سفید موشک بزنیم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72369" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72368">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72368" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
