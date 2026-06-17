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
<img src="https://cdn4.telesco.pe/file/clmfUNAIiZFN6c_UxsrBsPu8z_6scjlgBKSprpmbDi5lXHyvjAu_7f8YX21QA-vU4JxtUx73OaLrF_R9cMRLZo7kKnTwDxa9ZVC9tTyV_09hgGjavAkBOAXqkZkilzlDQ-jw-8SS77noNyWNuaqQdZKFY4yI5sIAvkzQL0UF8wRckI1PHZVvNH0f75ncug-Dy10gKIir5e0EzJsiUfaV1xKNrgj_gWN2hovCK2f1yUyCQXoMN6N6qDkOP-jo4hV2L-Mal_rxmb1IHn8CKJwNNf0Pu131jfvjMdhn3Ruq03sNTyLAATLDRnK_Hzpo05TyX83MtxGq0B0XxALmtlcLAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 01:23:42</div>
<hr>

<div class="tg-post" id="msg-442965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: متن تفاهم به فارسی و انگلیسی امضا شده است
🔹
اگر فقط متن انگلیسی بود ممکن بود در ترجمه دچار مشکلات سلیقه‌ای شویم اما الان طرفین علاوه بر متن انگلیسی، متن فارسی را هم امضا کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 368 · <a href="https://t.me/farsna/442965" target="_blank">📅 01:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: انتقال مواد غنی‌شدۀ هسته‌ای به خارج از کشور برای ما غیرقابل قبول است.
🔹
رقیق‌سازی مواد غنی‌شده گزینۀ جدیدی نیست. الان هم به‌عنوان یک گزینه معرفی شده تا راه را بر گزینه‌های دیگر ببندیم.
@Farsna</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/farsna/442964" target="_blank">📅 01:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: تعهد در برابر تعهد؛ قرار نیست ما تعهدی انجام دهیم اما طرف مقابل از انجام تعهد طفره رود.
🔹
بدون مماشات، اجرای تعهدات طرف مقابل را رصد می‌کنیم. در صورتی تعهدات‌مان را انجام می‌دهیم که طرف مقابل به تعهدش عمل کند.
@Farsna</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/442963" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۳</div>
</div>
<a href="https://t.me/farsna/442962" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۲ – کتاب آه</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/442962" target="_blank">📅 01:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: بعضی آسیب‌هایی که به ایران وارد شد با عدد و رقم حل نمی‌شود. ما برای همیشه نسبت به این جنایات مطالبه‌گر خواهیم ماند.
🔹
از هیچ فرصتی برای مستندسازی و پیگیری و تبیین جنایاتی که علیه ملت ایران اتفاق افتاد نخواهیم گذشت.
🔹
از هر سازوکار و نهاد و فرصت بین‌المللی برای احقاق حق استفاده خواهیم کرد. این‌ها خارج از یادداشت تفاهم است.
@Farsna</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/442961" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442960">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: موضوع تنگۀ هرمز به‌عهدۀ ایران و عمان است. فقط ایران و عمان ۲ دولت ساحلی تنگۀ هرمز هستند.
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/442960" target="_blank">📅 01:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442959">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: ایران در ازای خدمات در تنگۀ هرمز هزینه دریافت خواهد کرد.
🔹
سازوکارهای مدیریت تنگۀ هرمز تا حدود زیادی با عمان بسته شده است.
🔹
تردد ایمن با حفظ حاکمیت جمهوری اسلامی ایران بر تنگۀ هرمز خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/442959" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9D8BuIa0t_MhMEvf9kT5Fxq8s3wr35jZ33VNTYCa5PgAFjFILNaDdcZjMUAeKBNoRJzfoq0mfri_FLjVJt0gF-c6pXNQLKh_SvEV7nh43oVO5c9N-QZXoP6oK2HO3FcxaaGANKw5EmcclMtZDiHivWA3UZneZGfAPsiKhSRF34kEYGo4P1AsaBXH4gDNdRSz9l5o2Go102eVRt9euXR20wQy6TXf660bKuP-KPFuy22ZVAPpAWctauUS6YsUkDQJF7ZH_JsFidOVANJ8rRbx0ZZBrtWzBieSOcTYe4o1jSRRosGK8hXFw3X_crNab60JVXIFPacl_VYCkpSpCGOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن امضای تفاهم‌نامه با ایران را تایید کرد
🔹
دو مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفتند که واشنگتن و تهران، یادداشت تفاهم برای پایان جنگ را به‌شکل دیجیتالی امضا کرده و اکنون اجرایی شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/442958" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442957">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
بقائی: موشک‌های ما برای شلیک شدن هستند، نه برای مذاکره.
🔹
موشک‌های ما اصلاً دوست ندارند که کسی دربارۀ‌شان حرف بزند. دربارۀ توانایی دفاعی ایران در هیچ روندی و با هیچ طرفی صحبت نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/442957" target="_blank">📅 01:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
بقائی: از زمان اجرای تفاهم‌نامه که الان است، ظرف ۶۰ روز دربارۀ موضوع هسته‌ای و تحریم‌ها مذاکره می‌کنیم.
🔹
اگر زودتر مذاکره به نتیجه برسد، بهتر است. ولی با توجه به پیچیدگی موضوع، ۶۰ روز منطقی است و اگر لازم باشد، این زمان تمدید می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/442956" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: در متن تفاهم‌نامه تاکید شده است که فقط منحصراً در موضوع هسته‌ای و رفع تحریم‌ها مذاکره می‌کنیم.‌
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/442955" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: اینکه در این مرحله توافق خاتمۀ جنگ را امضا کرده‌ایم، به این معنا نیست که گذشته را فراموش کرده باشیم و درس‌هایی که به بهای گزاف آموخته‌ایم را از یاد برده باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/442954" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران نشان داد که دوستانش را در هیچ شرایطی تنها نمی‌گذارد.
🔹
برای ما آتش‌بس و خاتمۀ جنگ در لبنان به اندازۀ ایران اهمیت داشت و دارد. در بند اول یادداشت تفاهم، سه بار نام لبنان آمده؛ احترام به تمامیت سرزمینی و حاکمیت ملی لبنان آمده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/442952" target="_blank">📅 00:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
بقائی: متن تفاهم‌نامۀ ایران و آمریکا الان رسماً نهایی شده است؛ چراکه دو طرف آن را امضا کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/442951" target="_blank">📅 00:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_JSiRHnOSxLY47NxTr0QnUK0Ni6kSDO6B-GJWp-fYyzcbrnxnxl5rqBRTCkFJLVdaDL-4_tK2doI3_BsczNAIqJwet5Tz9YhIcS4pfB3QC12164VRydbPFFR_NrQOOI41o224N0jIYxwQPC39URpE6-Nv4RW4AyBjEIuzdT4NPUpkuYoyvPt9RcDRWtBbo-N9xX43ysg5ZYGQB4PGWT_VTE4kdOJxGT--Z1DQv5SbVBk-6TAnFeU7Un1QC1p_vx8jd3MywtXpbbw6HlUKkfS6mgFaME06mJe-W4OjIQWM76GYxCrpAMwzRVdINGhR2tQfWR3bT78UcG0p1vTts0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8LCXNekmh_at0rQyREhv_R-XVFt11XqCV085405zaEmW0eQCh-GqeKOXy1j0LzPIxpC_gOUeKGC8ZmC9V3AgRNUglSHvYAIPyH_XNZOFUECY0loGRB8T0RuEDgtk5BLX8IrhS3ePsqtFhjDKIh-OblNErHOA-gT3cvamXjpKvqj_IEoqzFDvZaVmAVPe8KP6t4iYoROu1kRLLnjrfnON2uMlL4xCC-xAA0tcDUYy8JlMwwMfRhmba2DYqHYct8HTOCid_G3FQuQI6kVy53z5SSAyU8sRWPvJJDxxUT37Lp8noBr__1s5m3CfcUD_gie9SzNfmHsOvr4cLW8KLtVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxKjPgbU-pRp_QLdqaKu25d91ZRFI7ygOgtcJ_Jdae4c-6yCPljgl2m7d9KSW7PVPz5ONPqktCVgei-OMiU-m9OkxPVE2UP9zXFlkhx0H3Y8AJ0QYBrm4rlzcbZDr0uRzJk1OpA8UtxyI6TrTL1R9nwExgdqUHQb9inO1rIotLLkChJKWJBjXwZAIc60_zy-R52q48DA4zZPe70BoosNSjyz7IeaHXOpadmnwn2Lddmr9mzJN8GwQexNAtJbijtmtHuqt5yFED_wb-QwtL5LXI4hQ4XWA-jVoSLKWyaqi_A7wLemhZmnfHD12paSypx1cvy__WLpw-Qgxix8vQ8AiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJMQoNH-5xgYdvTQix13_uN2cYNwwGZkJ3gVNkl39sjF5481Npq4RvVF5sB9rgFlGWcha7jYl2uKgq6-mnF3KZZULQEI5e8B79cZCjRBZZtI2NZyIpo_7qjpmbcpz0tDrpE3iB-7HWl6wPb885LjRMVQvg01QyWNcw96eJtfkg9t6CgXyuVsfQpRvzI8264fEGtLVoxtFl83jzl105NY4YFPCQNDSDMSv4x7iSEdI40CMIKAiuHKDfZbBa-bOwMzHpR3wDu9JhkeH2HfD4eGDHbVjirCpUpGFyUkbuciNE0_gRBnCDxbYAJxd8jqi5Jwho2V3kLbHNbw8Av-SN_fnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۸ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/442947" target="_blank">📅 00:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442937">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s4GsJaGvL_0I5tn8XWeqHQMcxI95tpUSs2vhm0qIpwswx2ZUS8EcrkptA0FRAICCSqCixdbCdnTQDtorDlKq3Ko2C8odSETC2WAHSo6b9A4lsNbU5cBBUOO1pVo2f_of5m8csk3G5Dk1NOkBoLSNlM1Po2tvv611AH45jbgTzSgxO0f7YqegQVldhtv7iwfZ1UtskoA3ZvS3YIQb7SXeFzCQH36okvYb6M16Z-yLDI46SA_YpV0FDFQIUuXyPv3BTvIPT9IDE7D5hGkCC2jVG45EFUMYjs91S_xZRfvvBBAn9BSulG5tSdTBSawOZ32hKdrJ22LJaq-qLUxR3c01Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGZMwx6Uf95rIB7as42sOzqGqksV4QCpN8kOlsEyHr-fTt4t7rvZPwt7dgpPqhOg4KIYF2SvPYk-ytloxqOANt42B66cdRHuhPTqMqGuCBX2BbU489INnhOADIheAqNgZcKlsM3fhm5_BCFwyWWhkNy-ABJbQQj8rQhGwYHrfbm1Jboj10ejZYb7X4JxuBRR7_7ipUEYGKeP_BsnTmTb9zkrhu_-s7e_PHVQ-7MKLcqNSiopiNwP8dO1dpWab-ZTaJASyAhXg_SjHV7itrUH1aR_kCEGAfW9oe73b-iJS5MIjoZ2-7GvCGhmCA3ZlU9oviOrPx1wLVwqXvD2MAMHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxBSIdb9qx3-JaruxkUmc4ZacQSsraYl6wULO07Up9S_mvN9xLu_z5nTfXf5RCUvNwR657P80q1GEIxqS6g6Q4-Una6sMThvQhu4tHzbEdF2gkH-G60oZKblknwErjh5vYH8Seqa80qKr5G2zIv6-jtbCOqbfl1z2sMJSpCUOpa9fGu6QsShhOUz9mnU1xtObYq__zIeiafVveyyO-G9X-gPnp6CX_JBZ-TUX1poocOrCntbUPK0pA3Wt38joExzbuPeIDGVOSZXvAdTEYh7-PyBGRpMpvNCjWDOrSxK70xflRN-RpkFyRzMRuMEvwQbshwclaoTqLkxyMyjOXEuzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GtayXeqs7zPYIiLNTsxWnlBdbJEGoVNJLRGGrhVtifPT_Jpcb4AqBtiICAn0X0WSkXoqAQqwd0tbLHptIXr6sB9qNCNSnM1Kc6e_1juQf02aimMzniR2BzfidMVj_XzTB2DxgAVXD6K4hSn6XkKKYU4CZIwvGFSSjrfwFcckEJHb8iy2Pf8ZNY9gwuUb2qLFe65vcgZG-49XLRt4lQYOcqq2Tz0blPL1qAOahflp4y8xCc9LRTnaD9CHutjPUNVo9jgF3fNN-ns0jOEdoBNdtLzXvXegU42hwg4Qr0bmsPK4X0C4u-fGthbFpxOqnseUhPBzOFUn9B8r3OzNXPClQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cz-AYvxZ-yoX6qNMn0_PBPJVAT_jwLDNQtbzhXdfp1_3hTjNRXAUDTNG-SsBtNaRJbQWhno1V7j1AjPpfIAXWbtlwYXSqs6oKXcAmUBnOPhY2j8vLyE780oe2cx_z1LwwzdnMlTcIp83bc8J-Ud-dhgdSTCCoC8beflo5tGN4jL-W-zdeO-AjbahvM6diXuvY1fkEF7HTzjR1t9zmdlBmpSysfYF_ilvwoPjf0i2y9PyYg-_ypZqqesnZQKbPENtPueW8OBDpBHIN4-bArvJVRG-Qkmwi_IAzyXNPrLBwxNdZV0ul5_rNZj-wdc9LYlaVoLcjsnEFm0HRwgGg2DocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaInSGQnD9zZ8UeLskf09GR-cytk4ow7Fp1fZkJQ0uo-LlV0r-C9ZscfKuYWoLvLyaw3im7JhP16_5pgCz3E4klOJjdAMLzdibVTRmW5H5521rbSN2iiUKf9hcXjCvHFnoOlEH1Bzhc3xw4ht2isGB8TLSnv0H6646YokvL_BQExaO5p_JBl-Evv6bXeWKFNuc44ikqZJXLmunB5dnnGfrJ5f4pA150UaIvji-sprSJE6x-ywXl4uFWaniHo9yzijfGlexxXX__IOQrGlozBiNftu71js36eCfH6951VLsGOu7CzQyZ3Zz4LUAZJVKCkrhd0QL6UOik_UeX5-n8Mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opMPuq-SDHPnLIqIvGfjLqtgnRoamANx8S_8tekp1WX1S7PoDrWFXQG1TpjQ4REykt3O3KtGpIjwK69gm8gtFL5E_I4Ctp2m_B_9LYgsxo0ZXch3mD293r_LvTYTk7ZqXujhbJfl-hfb9ufQOEbEcH48YVhyeQopBFx2_JiUg6K5q8N4-2nuTlUCwE253ChuUCQvclRB0HbN8dHnK13MWLla5uLCurIa07oLYqNzncbJG4r99ElDClJKNbgJPi-w8Iy3sYGrFZuVLQxKN3BZMx26M28RxI82dWQUxFrqKQ9Jbhc_uX9p_V9WIX7lppkxIKCQIHcbBRdGK3GjHoxHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPNdzZsb7hMJt94xdpHMDo5RbyKHn1sUvgSF-bCLOFg0AWejF5byFmeSaKBzygLps7hZEnObslL0h7aXqzo0MLzK--skSDk3XeKPvni40q-r42haGfIQJOewmjKMb0S6pas7UbzOsgvtaNCu7Gh7mgOKygFFxmq8VK5NcAU5_OQ8EYtbvu2c8KezKAx9heSlV9zOSXDgTjdVXvSwxQGtehRytVc63YbYuLQflJjfZZj1Go4fHZYrgfaM52l86r_Ldz4DO32d7jf53KHsG6jgZwYK37G7GRsNASu1BMSd-015WVZ62XWYfaqwiI2PlgAAWNbNeWIlKPktf_VuvdJp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4_4UVelVMtUqNZh4LrFRboyfi_tAUYygog-xk6db689DgANB4Zdrz4a074Y6uzVIOVAt8TrxrtAOUIcVZjb0KJCzBZQ8OAKkUzQoucerD47rlSht_JrRgMtmmigNCAoJhCKKjC0j0OTRxIduLNGRYlJur3zCcTm7FF5I72BJJRPvPnqFYY3XGwRHuVuzPD3DZLtgaz0hxC4mrdXI2QPI7ofEOF4TBViSIFnz_LKmZ4VsrCZjfZ4id5OXE0OERgtoxNMVRMHF-2M8NzpBSyZbGOpJ_cazEglKQ8lY4ArTI0dTBcb-eObi8dcL5PJ-ETAB23JNhUrFvHqzKkyqzyU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ncC5Sgks013cpnYMyk7lGGenwSw-Yd6bCdqmyYMJKb0L2QIl8nWHbAa_n_OQ4NSMJmN7k3UsvUYjhtH6zNl7xdHi8-iNDmo6Ohdump8y-iwtOUJzQP7iDNyCVw4Cz_sPsf3ZvlfgNKMSdUpiHCz87XMtxPHJ9K-OC9i3knEkMP9gImO_P6SyiG0ISL7RKcCsqlpA2WvERMUfNP3Dg3UZXHlregSEOXm292JoZ6HoFkqttb63qKbzqU_sDTrz9JtUMGDcs2rSO9HiVMM3S0j8GAknNuTTyzsZaWNTW9NdYYAoC-WAlzyzGZ8noqEvjCX8ni033WBmrkIVktxiI2Fq0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/442937" target="_blank">📅 00:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442936">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcvSRQeYDCljmsKSlzDJqaIZdTE23fYAE1h2kvF9PT6Jig17eBasj9e9A_a9BwmxceZGi6ogkdr8lHE1i__u3Zx7ulpWR3Oq41p7b-BlfHq9-nq8e9eKiSTYw9OKI2Uy8uUA58qHqryPoxiIIuDIUqSh4-3jZQ2dsggX2vEv5EuNPtD8hMMeDloOh3hjA7j5sYt60vCRql4ZOzf8kOStdNd9LpI135h49Eoan7YI_kNoVMhHEOIkeJn1ev-TYwkdxmIflkWVLxKW_Vmoq9xVCNCIkV1qYUD8sE7TAV1YA_2O-6rJ4EucmEH3vUxs0Qf8KQBig0YH1wAWyCqFiYpPAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ صهیونیست‌ها به جنوب لبنان با بمب‌های ممنوعۀ فسفری
🔹
رسانه‌های لبنانی: ارتش رژیم صهیونیستی ارتفاعات علی‌الطاهر مشرف به شهر النبطیه را با گلوله‌های توپخانه و بمب‌های فسفری مورد حمله قرار داد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/442936" target="_blank">📅 00:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca77291ac8.mp4?token=Lk8cjTEiDn8ayWxHpxDSjp6Pj3LsbWQuOlXJcfJtLxStbcczJCReWwmsLV1eY1oOYhvkTXbT3YVPFsH271b3AlZHSfg5HnVc1PQDYHEpy8ZubzHqcYivHRrMyPEfo8WCszZon_eEuqhNY59tfRy8gSIoeGyS37DLVWPhrgqZF21fD54WHGKo7edD1pxFDQ8NB9n07-dbuUgRHLukzVH73bZgQrF2vuMS7eL9eNF1DvloiIwru7InHpIQfIJ-_KtKnatLdqzt_f_vzTZoZbFkgHrCJi1m8T63ebDbhJFtO0-NAXG9-A8bhYyxkZHfw0bChH10rqqbC7te_2j-y3pVyrZlvdQkL_wVac-mzRb6wDtirbHA4-jqoz-EKcwFfPHKvUXAHAJtUPPhoYnZjCTEsa0qTWXwUH5g4z2ybPla44lCMXNmlsWIf1mNAPxIbWsiCR1UyeAixx5f2LZX3UU9feUc_DW0zI23LfIDOJOG-EzB4CmZRq5pZVb63z4CjDrNY64bSgH_sfgV22Cn_NH9kygl4Uuo0L58sYARAWPUa_KpdtGE6Yjuf4M4Qn-s1vLcwDcxAzYQZWJy10UiFkISho4DziiKM55DTU_1dP05D-ToEPe83rZV2nRE1CBJy2orVMwCZQtVzGgO6N5oYEpj1wwlh-72_EkIuZOl_qEelDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca77291ac8.mp4?token=Lk8cjTEiDn8ayWxHpxDSjp6Pj3LsbWQuOlXJcfJtLxStbcczJCReWwmsLV1eY1oOYhvkTXbT3YVPFsH271b3AlZHSfg5HnVc1PQDYHEpy8ZubzHqcYivHRrMyPEfo8WCszZon_eEuqhNY59tfRy8gSIoeGyS37DLVWPhrgqZF21fD54WHGKo7edD1pxFDQ8NB9n07-dbuUgRHLukzVH73bZgQrF2vuMS7eL9eNF1DvloiIwru7InHpIQfIJ-_KtKnatLdqzt_f_vzTZoZbFkgHrCJi1m8T63ebDbhJFtO0-NAXG9-A8bhYyxkZHfw0bChH10rqqbC7te_2j-y3pVyrZlvdQkL_wVac-mzRb6wDtirbHA4-jqoz-EKcwFfPHKvUXAHAJtUPPhoYnZjCTEsa0qTWXwUH5g4z2ybPla44lCMXNmlsWIf1mNAPxIbWsiCR1UyeAixx5f2LZX3UU9feUc_DW0zI23LfIDOJOG-EzB4CmZRq5pZVb63z4CjDrNY64bSgH_sfgV22Cn_NH9kygl4Uuo0L58sYARAWPUa_KpdtGE6Yjuf4M4Qn-s1vLcwDcxAzYQZWJy10UiFkISho4DziiKM55DTU_1dP05D-ToEPe83rZV2nRE1CBJy2orVMwCZQtVzGgO6N5oYEpj1wwlh-72_EkIuZOl_qEelDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۹ شب اجتماع سرخسی‌ها در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/442935" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">۵ فروند بالگرد تا پایان سال به هلال‌احمر می‌پیوندد
🔹
کولیوند، رئیس جمعیت هلال‌احمر: بالگردهای هلال‌احمر از خارج از کشور خریداری می‌شود، که برای ۵ فروند قرارداد بسته شده و قبل از سال ۱۴۰۶ تحویل داده خواهد شد.
🔹
بالگردها دید در شب بوده و دارای سیستم جدید ناوبری…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/442934" target="_blank">📅 00:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
قالیباف: پرداخت هزینه خدمات عبور از تنگه هرمز در تفاهم‌نامه تثبیت شده است
📌
کشورهای ساحلی تنگه ها در قوانین بین المللی حقوق و وظایفی دارند از جمله این که دیگران باید هزینه خدمات شان را پرداخت کنند.
📌
دشمنان ایران را خدا از احمق ها آفریده و باعث شدند ظرفیت…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/442933" target="_blank">📅 00:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442932">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قالیباف: همه این دستاوردها و منطق قدرتی که امروز از آن سخن می‌گوییم، مرهون مجاهدت‌ها و فداکاری‌های نیروهای مسلح جمهوری اسلامی ایران است
‌
🔸
به همه فرماندهان، رزمندگان و نیروهای مسلح خدا قوت می‌گویم و از تلاش‌ها و ایستادگی آنان صمیمانه قدردانی می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/442932" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442931">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae42f790b0.mp4?token=UZMx0bfD8A5lYaAD0oPkGv-u5UMDTD3-cDxr0EYeWITp1nZ9mfICJHgW89XPQ207OtvV7aGsnLTNLgITPO2zLWqziAZqAEHw7CU9tNEoO65nPgbnUyxkobpsT3IPVuOF0U-Xifv7u0PpjxInqwe9WRrsy6Qf6xuuCMj6x8GY5Xm3_dFnvgvwboKnqSo3R6h_mIfUr8lSow_ol2A3P23MrvbYRWQgmYg9tSwfwgfN3r0gpUsFHlZG8TP0WMcxEnipTJ8zH6icKylUz7Iva6ochxDEdOroURdpVLfLRAOyUHxY8VgtoS9SRh4GEaqovyMEYiAxnu7Ktc0-3McOoTAcIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae42f790b0.mp4?token=UZMx0bfD8A5lYaAD0oPkGv-u5UMDTD3-cDxr0EYeWITp1nZ9mfICJHgW89XPQ207OtvV7aGsnLTNLgITPO2zLWqziAZqAEHw7CU9tNEoO65nPgbnUyxkobpsT3IPVuOF0U-Xifv7u0PpjxInqwe9WRrsy6Qf6xuuCMj6x8GY5Xm3_dFnvgvwboKnqSo3R6h_mIfUr8lSow_ol2A3P23MrvbYRWQgmYg9tSwfwgfN3r0gpUsFHlZG8TP0WMcxEnipTJ8zH6icKylUz7Iva6ochxDEdOroURdpVLfLRAOyUHxY8VgtoS9SRh4GEaqovyMEYiAxnu7Ktc0-3McOoTAcIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در این مدت در میادین در میان مردم عزیز حضور داشتم و در کنار شما بودم، هرچند بسیاری از شما مرا نشناختید
📌
از رهبر معظم انقلاب تشکر می‌کنم که در این مسیر ما را هدایت و رهبری کردند؛ هر جا لازم بود تذکر دادند و هر کجا نیاز به حمایت بود، پشتیبانی کردند.
📌
از مردم عزیز ایران نیز به خاطر صمیمیت، گذشت، انسجام، همراهی و حتی انتقادهای به‌جا و گاه نابه‌جا تشکر می‌کنم. همه این‌ها نشان‌دهنده حساسیت و دغدغه‌مندی مردم نسبت به سرنوشت کشور است.
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/442931" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442930">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4538914626.mp4?token=Re5EPrGOAFQybeFncfKcX27mSoXjR3rlnlondtO7ozgGxRZ-oli-n363hT5jloEc_U-dNgipcWqpo5iVuu6vRQD9UR8I1-DDg7dYSQ2YZRiXtPDYndwNXy4w_-lR7QtdxJK5ZsGSE17LTvprnp9bK2GYOGS8awXyeVeZP8FcohFrVzaSx1AfEh9fv_XmSdKjee6Pj45h1gQ3jKDMFqMqJR0t27btbG9V_l4kVOrnkXfCoB_W0titkWM_m9SxrMmRh7UE3Hce25ZeJSGTWJjVTnd82-Rir5Bj5HdjnakddHeg5DD5XljKWY_5gEwAbTUx5DBcLmacEDKEDMJw65ooXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4538914626.mp4?token=Re5EPrGOAFQybeFncfKcX27mSoXjR3rlnlondtO7ozgGxRZ-oli-n363hT5jloEc_U-dNgipcWqpo5iVuu6vRQD9UR8I1-DDg7dYSQ2YZRiXtPDYndwNXy4w_-lR7QtdxJK5ZsGSE17LTvprnp9bK2GYOGS8awXyeVeZP8FcohFrVzaSx1AfEh9fv_XmSdKjee6Pj45h1gQ3jKDMFqMqJR0t27btbG9V_l4kVOrnkXfCoB_W0titkWM_m9SxrMmRh7UE3Hce25ZeJSGTWJjVTnd82-Rir5Bj5HdjnakddHeg5DD5XljKWY_5gEwAbTUx5DBcLmacEDKEDMJw65ooXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تفاهم‌نامه براساس اصل اقدام در برابر اقدام است
🔸
هرجا آمریکا به تعهدات خود عمل نکند، محال است جمهوری اسلامی ایران به تعهداتش عمل کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/442930" target="_blank">📅 00:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442929">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c28824f9.mp4?token=EM3CYPqJjQt1YnthvrqugrhKw201LGrhNaoGdQqghnKy2J0zruG97CPhxZoDyMEOBgAw6-MP3wBbn1e5TlbZrIiYGHD7iMRtDHJbWSNu5zwzmGg5MWsMqDTgvVnWqhDG-i7-s0UyNkut2KGXhAQCPJkXCDC6l3PWscQbu44TDMXRnGLrx_luiRSVIzflxwJb0oWQwo9fuvWw9xQp-_MldOXSKDmkjhPFS5BJ4KEyPwfggUrywAzOjEXkR_wh14UYIWyO_fPalKMqVvdkm15OPCfZdl6awxlrpif9YiU9YxmjR0wC5d_S6siWKrGCN4kZhnczfXhAhFBGk0z8VDdyKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c28824f9.mp4?token=EM3CYPqJjQt1YnthvrqugrhKw201LGrhNaoGdQqghnKy2J0zruG97CPhxZoDyMEOBgAw6-MP3wBbn1e5TlbZrIiYGHD7iMRtDHJbWSNu5zwzmGg5MWsMqDTgvVnWqhDG-i7-s0UyNkut2KGXhAQCPJkXCDC6l3PWscQbu44TDMXRnGLrx_luiRSVIzflxwJb0oWQwo9fuvWw9xQp-_MldOXSKDmkjhPFS5BJ4KEyPwfggUrywAzOjEXkR_wh14UYIWyO_fPalKMqVvdkm15OPCfZdl6awxlrpif9YiU9YxmjR0wC5d_S6siWKrGCN4kZhnczfXhAhFBGk0z8VDdyKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: به‌خاطر حساسیت‌های حقوقی ساعت‌ها در مورد برخی متون تفاهم‌نامه بحث شده است
📌
برخی دوستان نگران بودند که آیا بعد از ۳۰ روز محاصره رفع خواهد شد؟ اما به لطف خدا طی ۳ روز محاصره لغو شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/442929" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442928">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
قالیباف: در بند ۶ تفاهم‌نامه ۳۰۰ میلیارد دلار برای موضوع بازسازی و توسعه اقتصادی در ایران تعیین شده است
🔹
سازمان ملل حتی یک بیانیه که آمریکا را متجاوز اعلام کند، منتشر نکرد و لذا نمی پذیرند که متجاوز هستند. در دنیایی که قانون جنگل حاکم است ما باید با قدرت…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/442928" target="_blank">📅 00:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442927">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc516a2f7d.mp4?token=hC50XDp2c-Y9HR4FhfqSKJROPU3UiM4BapSKY4V65feuKS1DmqDNQ_E3xTPX7GvYIWFCJkRds_Yc1AH3lHX-3_JFpHvf36VUsKswR1ofHxm4c4w06srRlDvjETdr_lsec_3vEbJ464OJLkl4xo6Z-xeoIlc-LEhA3ZyomziBu9V0iv7ChEH-m_GNb-nixDLHLOspzDCmKKRA48_GHJsJvPfQIO599f9wCp8WugsYi7Pzre2AWxiJ18eeiNvHdgvq5AvYRVGPDpryAdMRdchjFI_7RRgziexQuACQrbb4BK5Yo2GUFFfwaa58ovOPVjYMozUrRFCoVIZ3lhWEhKkE9q-uy5qvM1DlvWG8xH2Z2KmUHS6LVbP8VyJLtzi04ZwIeATMDB_lbNbVyvL5BCjpnp7HoJF-m7tsSbhL34BpuYSOhOuXy3cSYb3DlBQ0P8fV4N_TlFxpMirygDRcBFtWUTLsJljIFYudvVBThdtJx7y0nrXyS0MUgbG3xwl65ib6yHe_wt7hwsXBBGROLmcH2Fj5ksQu2r4okwl9mYvaZ0deAIlbqgXYU_EFEsJ0Nz7OHsrDnzF09FS2_1dEUIoR20-Hnc_GtR2PAaAuJnD08z--fe3oOgem9O6OO4PvXG_ldVN13akHwf7P8Y2F6U9u2Gph6Ff0W5-O-W2nKMZFXp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc516a2f7d.mp4?token=hC50XDp2c-Y9HR4FhfqSKJROPU3UiM4BapSKY4V65feuKS1DmqDNQ_E3xTPX7GvYIWFCJkRds_Yc1AH3lHX-3_JFpHvf36VUsKswR1ofHxm4c4w06srRlDvjETdr_lsec_3vEbJ464OJLkl4xo6Z-xeoIlc-LEhA3ZyomziBu9V0iv7ChEH-m_GNb-nixDLHLOspzDCmKKRA48_GHJsJvPfQIO599f9wCp8WugsYi7Pzre2AWxiJ18eeiNvHdgvq5AvYRVGPDpryAdMRdchjFI_7RRgziexQuACQrbb4BK5Yo2GUFFfwaa58ovOPVjYMozUrRFCoVIZ3lhWEhKkE9q-uy5qvM1DlvWG8xH2Z2KmUHS6LVbP8VyJLtzi04ZwIeATMDB_lbNbVyvL5BCjpnp7HoJF-m7tsSbhL34BpuYSOhOuXy3cSYb3DlBQ0P8fV4N_TlFxpMirygDRcBFtWUTLsJljIFYudvVBThdtJx7y0nrXyS0MUgbG3xwl65ib6yHe_wt7hwsXBBGROLmcH2Fj5ksQu2r4okwl9mYvaZ0deAIlbqgXYU_EFEsJ0Nz7OHsrDnzF09FS2_1dEUIoR20-Hnc_GtR2PAaAuJnD08z--fe3oOgem9O6OO4PvXG_ldVN13akHwf7P8Y2F6U9u2Gph6Ff0W5-O-W2nKMZFXp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در بند ۶ تفاهم‌نامه ۳۰۰ میلیارد دلار برای موضوع بازسازی و توسعه اقتصادی در ایران تعیین شده است
🔹
سازمان ملل حتی یک بیانیه که آمریکا را متجاوز اعلام کند، منتشر نکرد و لذا نمی پذیرند که متجاوز هستند. در دنیایی که قانون جنگل حاکم است ما باید با قدرت خود، مسائل را دنبال کنیم.
📌
البته در تفاهم نامه بند ۶ برای این موضوع آمده که در آن از لفظ بازسازی و توسعه اقتصادی استفاده شده است.
📌
در این بند ۳۰۰ میلیارد دلار تعیین شده تا در ایران سرمایه گذاری شود که بخشی از آن صرف بازسازی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/442927" target="_blank">📅 00:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442926">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f74e37d41.mp4?token=S-MPmVdycc2qR3xisEp1Nz-4ZlYB4bwZUjUodnPb0qUYMtwmbBqtMKke7LKDs1XtwxmzpNNKMFLdXpsmmtS47idx2yVamK5oaaGpu7YrgKuH2aI3R5fX8MVNIx43g1P3CSf8O1p6lpmnzWQhHsaPySu1Qus5i_CeYZl8cd_T4aIrXJozfDqoijjTI9vGA6nsIdGwWg7MIzCSKgyZXkpJmzuMhDHtxrvK2-XDS70a9PA9RvIiXAQPmJjK3warZOmPvORNO4d8KBlhK_Xlj85p4B-UboGB_k8wvSs8hSvYGAIZqTeCjHcFdfu0nERyGvjtJu8USJ_LCg5Fd-YS0oqX3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f74e37d41.mp4?token=S-MPmVdycc2qR3xisEp1Nz-4ZlYB4bwZUjUodnPb0qUYMtwmbBqtMKke7LKDs1XtwxmzpNNKMFLdXpsmmtS47idx2yVamK5oaaGpu7YrgKuH2aI3R5fX8MVNIx43g1P3CSf8O1p6lpmnzWQhHsaPySu1Qus5i_CeYZl8cd_T4aIrXJozfDqoijjTI9vGA6nsIdGwWg7MIzCSKgyZXkpJmzuMhDHtxrvK2-XDS70a9PA9RvIiXAQPmJjK3warZOmPvORNO4d8KBlhK_Xlj85p4B-UboGB_k8wvSs8hSvYGAIZqTeCjHcFdfu0nERyGvjtJu8USJ_LCg5Fd-YS0oqX3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: پرداخت هزینه خدمات عبور از تنگه هرمز در تفاهم‌نامه تثبیت شده است
📌
کشورهای ساحلی تنگه ها در قوانین بین المللی حقوق و وظایفی دارند از جمله این که دیگران باید هزینه خدمات شان را پرداخت کنند.
📌
دشمنان ایران را خدا از احمق ها آفریده و باعث شدند ظرفیت بالقوه ایران در تنگه هرمز بالفعل شود.
📌
ایران در تنگه هرمز حق حاکمیتی دارد و طبیعتا در قبال خدمات، هزینه دریافت خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/442926" target="_blank">📅 00:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442925">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7111ac9d43.mp4?token=ILZiU7PuecHtWJXlrLY-J8qkzI1lFszPbN-wvs350hV04ACumWlOG9In3Jwmjr3VLuRkx1YqLkpdoPXauYvhWAPpshv6JODjU3A1J74ct0QddWboPFpMGPilZnM3Em4hVBL3J6YKrcWYRrWpKE_rxyySt0OP-snh9K-6UoZ4yjbroCsA9U_hbeXK1xfA2oyiD21-COzZ-vOwPQX61JKBD74VNiPaansSRpi74jnDOyLFh6OPnT-eC7nXC5j-ZRURU1uioMEV3AgG9KqKkcVXc87h2rnyL7Y-grp5EjWMEkfU1yCCngSVzt6jLxlzSoD8X1ATFzoADXgOK2QjbGWczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7111ac9d43.mp4?token=ILZiU7PuecHtWJXlrLY-J8qkzI1lFszPbN-wvs350hV04ACumWlOG9In3Jwmjr3VLuRkx1YqLkpdoPXauYvhWAPpshv6JODjU3A1J74ct0QddWboPFpMGPilZnM3Em4hVBL3J6YKrcWYRrWpKE_rxyySt0OP-snh9K-6UoZ4yjbroCsA9U_hbeXK1xfA2oyiD21-COzZ-vOwPQX61JKBD74VNiPaansSRpi74jnDOyLFh6OPnT-eC7nXC5j-ZRURU1uioMEV3AgG9KqKkcVXc87h2rnyL7Y-grp5EjWMEkfU1yCCngSVzt6jLxlzSoD8X1ATFzoADXgOK2QjbGWczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: وظیفه ما اجرای تدابیر رهبر انقلاب در مذاکرات است
📌
ما تدابیری از رهبر معظم انقلاب داریم و وظیفه داریم در این مذاکرات به آن تدابیر جامه عمل بپوشانیم.
📌
موضوعاتی که اکنون مطرح است، پایان جنگ است که اعلام شده و همچنین برداشته شدن محاصره که اتفاق افتاده است.
📌
در وسط جنگ، توییتی منتشر کردم و گفتم تنگه هرمز هرگز به شرایط قبل بازنخواهد گشت و امروز نیز همین‌گونه است.
📌
البته این به آن معنا نیست که ما در تنگه هرمز بخواهیم برخلاف قوانین بین‌المللی و مقررات دریانوردی عمل کنیم؛ هرگز. ما در چارچوب قوانین بین‌المللی عمل می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/442925" target="_blank">📅 00:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442924">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌‌ قالیباف اگر آمریکا به تعهداتش عمل نکند محال است ایران به تعهدش عمل کند
🔹
ما مرحله به مرحله و اقدام در برابر اقدام پیش می‌رویم. @Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/442924" target="_blank">📅 00:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌‌
🔴
قالیباف: ما ۳۰۰ میلیارد دلار سرمایه‌گذاری ازسوی شرکت‌های آمریکایی را در تفاهم‌نامه گذاشتیم که خود خسارات ما را جبران می‌کند  @Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/442922" target="_blank">📅 00:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
قالیباف: هرجا دشمن به تعهداتی که داده عمل نکند شمشیر ما موجود است و با منطق قدرت به او خواهیم فهماند
🔹
من دیپلمات نیستم اما خوب بلد هستم به آمریکا تفهیم کنم که باید چه کار کند. @Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/442921" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
قالیباف: خونخواهی رهبر شهید آزادی قدس است؛ ۱۰۰ نتانیاهو بند کفش امام شهید ما هم نمی‌شود  @Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/442920" target="_blank">📅 23:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48f0dcc90.mp4?token=KYQJb9Q7gUVYANtWMFvDYUkV3B8GMFbEge3T2d3x2_1DUaMlSa7PrlFKpPpthdu61-Co8tKZHiuZ6RPTJ8a_7s_iAB_5HkJWOd6RpfcyLcUye_jxcU0JNksRVMTg4GE8_9AAVnkFsZNQRQW0ndBOT7N2W3yVC-1FKftrLI5gou6Vjyid_3w5l-yo-k6G6_4DfXIoC_OYEfXpVrmhf9NSttDyWr6DNgV5rwPGLaAprrSRfOIllTczyFfOkkhOjpwkG23CGVF9Hq7t_sPdjGWsSRPP1rBdLzO09w0avrIzg4Y2qkrLJ9z0ivKU5VNBwBSKAB5LxMFtpA0VxNeMaNV_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48f0dcc90.mp4?token=KYQJb9Q7gUVYANtWMFvDYUkV3B8GMFbEge3T2d3x2_1DUaMlSa7PrlFKpPpthdu61-Co8tKZHiuZ6RPTJ8a_7s_iAB_5HkJWOd6RpfcyLcUye_jxcU0JNksRVMTg4GE8_9AAVnkFsZNQRQW0ndBOT7N2W3yVC-1FKftrLI5gou6Vjyid_3w5l-yo-k6G6_4DfXIoC_OYEfXpVrmhf9NSttDyWr6DNgV5rwPGLaAprrSRfOIllTczyFfOkkhOjpwkG23CGVF9Hq7t_sPdjGWsSRPP1rBdLzO09w0avrIzg4Y2qkrLJ9z0ivKU5VNBwBSKAB5LxMFtpA0VxNeMaNV_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
قالیباف: مدیریت تنگه هرمز را براساس قوانین بین‌المللی پیش می‌بریم
🔹
براساس این قوانین ما حق داریم هزینۀ خدمات در تنگه هرمز را دریافت کنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/442919" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
قالیباف: بازهم تاکید می‌کنم که تنگه هرمز هرگز به شرایط قبل بازنمی‌گردد.  @Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/442918" target="_blank">📅 23:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
قالیباف: ما دستمان روی ماشه است و اگر دشمن زبان منطق را نفهمد دوباره با زبان قدرت وارد می‌شویم @Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/442917" target="_blank">📅 23:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8762557a67.mp4?token=YWL93IYTy6GOVILwfSQhGzetRG5P0MKXEbRGTvmTiXrBOR8GhCwmuWgsKOhJP10YYNevhLx90YBr5Wor_b_9nwbokKG0pLUakKB_urolUHu9vv6BNkXRTbgtOklADcK2PJk_VhFMN7tLtYHeVh4yNBhBmjqlF3Imzm9DkqwFtm-CjGDdwiD2e-TNKisxm4Jzlwxq4_52DTM367oB6o97ixZFxVLOK8snE_0f3Ea-2x1Lv_DTKq3EDBEVXt3Cqeqx0HtKJshJx3ECah_g_2gL4y7JHIZF0hQrERBKq3r4SeskpNjmTZZfyRVqGKPo-bKoPQdYMvJU2W6kW8NaLomvqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8762557a67.mp4?token=YWL93IYTy6GOVILwfSQhGzetRG5P0MKXEbRGTvmTiXrBOR8GhCwmuWgsKOhJP10YYNevhLx90YBr5Wor_b_9nwbokKG0pLUakKB_urolUHu9vv6BNkXRTbgtOklADcK2PJk_VhFMN7tLtYHeVh4yNBhBmjqlF3Imzm9DkqwFtm-CjGDdwiD2e-TNKisxm4Jzlwxq4_52DTM367oB6o97ixZFxVLOK8snE_0f3Ea-2x1Lv_DTKq3EDBEVXt3Cqeqx0HtKJshJx3ECah_g_2gL4y7JHIZF0hQrERBKq3r4SeskpNjmTZZfyRVqGKPo-bKoPQdYMvJU2W6kW8NaLomvqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: وقتی منطق دشمن قدرت است باید او را ادب کرد ولی وقتی پای میز مذاکره می‌آید با بی اعتمادی با او صحبت کرد
📌
گاهی قدرت ما منطق است و گاهی منطقِ دشمن، قدرت است؛ در چنین شرایطی باید او را ادب کرد. اما وقتی طرف مقابل پای میز می‌نشیند و می‌خواهد گفت‌وگو کند، باید با بی‌اعتمادی، اما با حسن نیت با او صحبت کرد.
📌
دیدید که ترامپ در حالی که طبق تفاهم‌نامه قرار بود رفع محاصره طی ۳۰ روز انجام شود، آن را یک‌شبه اجرایی کرد. همچنین آتش‌بس از ضاحیه به سراسر لبنان گسترش پیدا کرد.
📌
البته ما می‌دانیم که با دشمنی بدعهد و غیرقابل اعتماد مذاکره می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/442916" target="_blank">📅 23:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a47ff9e3.mp4?token=BT2H_vxUpFawQdaGfweG4P65idC1jwyiJKYNQ_zA9mXbSFJbBw_NZs_N3MFiHDaEp5qX0bxSc_RFkHlmRLhCH5TfVtLXJThO-45BUVBvfnea0xZdeKHvnmBP9DoGFgDKUveYXWszChHPAc9dWtdiy-RciKuZZBB7ZGjVc6zd36fa9LTluab8IOPh0ttDxr5M8wT5I5I_vAoh6J0jRg-I2dH2d1s3cWWwP62Xg8zoUa-IYNMBtuDsMPLAw3UYleUPG1MN3Wwy0Mq3yfTQ1ErzgVLEdOfBgr-zsIFwxuOqHSlMGLK2z_XpF2JiwUWYA00Mf73PGBc3gJwTlBOLhC_SM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a47ff9e3.mp4?token=BT2H_vxUpFawQdaGfweG4P65idC1jwyiJKYNQ_zA9mXbSFJbBw_NZs_N3MFiHDaEp5qX0bxSc_RFkHlmRLhCH5TfVtLXJThO-45BUVBvfnea0xZdeKHvnmBP9DoGFgDKUveYXWszChHPAc9dWtdiy-RciKuZZBB7ZGjVc6zd36fa9LTluab8IOPh0ttDxr5M8wT5I5I_vAoh6J0jRg-I2dH2d1s3cWWwP62Xg8zoUa-IYNMBtuDsMPLAw3UYleUPG1MN3Wwy0Mq3yfTQ1ErzgVLEdOfBgr-zsIFwxuOqHSlMGLK2z_XpF2JiwUWYA00Mf73PGBc3gJwTlBOLhC_SM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توضیحات جدید قالیباف در مورد فرآیند مذاکرات اسلام آباد
📌
طی ۲۴ ساعت ۳ دور مذاکرات با متن و ۳ دور مذاکرات سه جانبه با حضور میانجی برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/442915" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
قالیباف: اکنون براساس تفاهم‌نامه، باید ابتدا بندهای ۴، ۵، ۱۰ و ۱۱ و اکنون تأکید می‌کنم بند ۱ نیز در اولویت اجرا قرار گیرد تا پس از آن وارد سایر بندهای تفاهم‌نامه شویم. @Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/442914" target="_blank">📅 23:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌ قالیباف: قبل از مذاکرات اسلام آباد اعلام کردیم موضوع لبنان و آزادسازی پول های بلوکه شده باید محور مذاکرات باشد
📌
ما چیزی به عنوان پیش‌شرط نداشتیم، هرچند ممکن است خواسته‌هایی داشته باشیم. البته به میانجی گفته بودیم که بحث آتش‌بس لبنان و آزادسازی پول‌های بلوکه‌شده،…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/442912" target="_blank">📅 23:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌ قالیباف: من برای پذیرش حضور در تیم مذاکره‌کننده کراهت داشتم
📌
من نه‌تنها داوطلب حضور در تیم مذاکره کننده نبودم بلکه کراهت هم داشتم و قبل از پذیرش مسئولیت مذاکرات من تمام تلاشم را کردم که این مسئولیت به من سپرده نشود.
📌
یکی از دلایل من برای عدم پذیرش این…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/442911" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
قالیباف: در طول جنگ نمایندگان چند کشور اروپایی به ایران آمدند تا از ما خواهش کنند
🔹
همان کشورهای اروپایی که سپاه را در لیست تروریستی گذاشته بودند از مسیرهای زمینی به سختی به ایران آمدند تا با ما صحبت کنند. @Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/442910" target="_blank">📅 23:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">روایت شب آخر مذاکرات
📌
قالیباف: هر جنگی که پیروزی داشته باشد، اگر این نهایتاً منجر به یک سند حقوقی و سیاسی نشود و آن پیروزی‌ها ثبت نشود، آن پیروزی‌ها هیچ منفعتی پیدا نخواهد کرد؛ نه در تاریخ و نه در مزایای آن.
📌
الان ما در جنگ ۴۰ روزه پیروز شدیم، خب دستاوردش…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/442909" target="_blank">📅 23:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0785c208b9.mp4?token=lYygv87iPZq6hj9DXWZUKOOeLkXEZvl3J-vzb2oznZL-pblf0UJKuxZTWsUQWyxIjYnbtU3BHvR-eFNFDVX9Q8QFGN6VlqHPnxPtt4Tp_uCK-YvyXTTBDaw8kB-kfPYM7kwo8ATAYA-F5xBzLKvKKhM_L8Bf37iCBpe68XU50yrwqSuL1ZNqZItKHKPZTYdz4YKcjoRlRVyVAXTQtOTC70vSAcwa1gVmPzwd-QnQCdh_3grc-abJk4eOXgjed3cc6BqWRD0FdeZjafAlvH2p24uiHsQTvqVJ95dr-nCVjFwTDWSzLpLUCm7LBcs7JYTamKDy8r-ibs568MR-f1ezPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0785c208b9.mp4?token=lYygv87iPZq6hj9DXWZUKOOeLkXEZvl3J-vzb2oznZL-pblf0UJKuxZTWsUQWyxIjYnbtU3BHvR-eFNFDVX9Q8QFGN6VlqHPnxPtt4Tp_uCK-YvyXTTBDaw8kB-kfPYM7kwo8ATAYA-F5xBzLKvKKhM_L8Bf37iCBpe68XU50yrwqSuL1ZNqZItKHKPZTYdz4YKcjoRlRVyVAXTQtOTC70vSAcwa1gVmPzwd-QnQCdh_3grc-abJk4eOXgjed3cc6BqWRD0FdeZjafAlvH2p24uiHsQTvqVJ95dr-nCVjFwTDWSzLpLUCm7LBcs7JYTamKDy8r-ibs568MR-f1ezPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: مهم ترین ضمانت برای ما قدرت ایران و انسجام مردم است نه قطعنامه شورای امنیت
📌
بدبینی و بی اعتمادی من به آمریکا از همه بیشتر است. حتی اگر توافق نهایی باشد و آن به تایید قطعنامه شورای امنیت برسد بازهم اصلا قابل اعتماد نیست، تضمین ما قدرت ایران است.
📌
مهم ترین ضمانت اتکا به خداوند، فرهنگ عاشورایی، غیرت ایرانیان و انسجام مردم است.
📌
قدرت ایران باعث شده سه کشور اروپایی که در برجام بدعهدی کردند و سپاه را در فهرست تروریستی قرار دادند و دنبال براندازی نظام جمهوری اسلامی بودند به دنبال مذاکره با ایران برای برداشتن تحریم ها هستند.
📌
سیستم های امنیتی همان کشورهای که سپاه را در فهرست تروریستی گذاشتند،  با التماس خواستار گفت و گو با ما بودند و با ماشین به ایران آمدند تا گفت و گو کنند، ما هم پاسخ دادیم، شما که ما را تروریست نامیدید، اکنون با تروریست ها چه کاری دارید؟
📌
ما حتما باید با عقلانیت حرکت کنیم، شعار قدرت نیست، گرهی که با دست باز می شود را لازم نیست با دندان باز کنیم. اگر دوبار شعار بدهیم ولی قدرت نداشته باشیم یعنی بی اعتباری و کمک به دشمن.
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/442908" target="_blank">📅 23:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41398d99c5.mp4?token=RPzOQGpnKYqQei6tO7mpxXvZJi6D_EgOflsGEdRw_nYTtEF0zIMOzqaj1yGek2_aBCNZo8mTIR0dmp7xyK2inW0MLGSH3d41KBvoMlNFFUVErV4SSoeOrgTt31soRoxrEhaF-lk6J-_CMyEgrmtrxMylverbv7oBIGm5WcUjUw7_yJNfDoCfACCNNXIxX5cIQ9USFrXQ-Fkj0_YznnJP3HyxVVCinZg58KzFfs754v3NG00oZuDx1hTV0cIMdD9o6L-IlCaGtRYEY8clDPw3m45VJwu8N0YZjLKagrkJVlyCkWD-qRtfgpYYYec9_Q22hmOipx7bg5bRRqW3AG6_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41398d99c5.mp4?token=RPzOQGpnKYqQei6tO7mpxXvZJi6D_EgOflsGEdRw_nYTtEF0zIMOzqaj1yGek2_aBCNZo8mTIR0dmp7xyK2inW0MLGSH3d41KBvoMlNFFUVErV4SSoeOrgTt31soRoxrEhaF-lk6J-_CMyEgrmtrxMylverbv7oBIGm5WcUjUw7_yJNfDoCfACCNNXIxX5cIQ9USFrXQ-Fkj0_YznnJP3HyxVVCinZg58KzFfs754v3NG00oZuDx1hTV0cIMdD9o6L-IlCaGtRYEY8clDPw3m45VJwu8N0YZjLKagrkJVlyCkWD-qRtfgpYYYec9_Q22hmOipx7bg5bRRqW3AG6_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ از موضع خود درباره «نابودی برنامه هسته‌ای ایران» فاصله گرفت
🔹
دونالد ترامپ روز چهارشنبه در حاشیهٔ نشست گروه هفت در فرانسه گفت که ایران می‌تواند برنامهٔ هسته‌ای خود را داشته باشد.
🔹
او اظهار داشت: «این موضوع تا حدی دشوار است که وقتی می‌گویید کشوری خواهان انرژی هسته‌ای است، در حالی که سایر کشورهای همسایه آن را دارند، شما به آن کشور اجازه ندهید که برای مقاصدی مثل تولید برق و امثال از آن استفاده کند. این همیشه کمی سخت است. باید کمی عقل سلیم به کار ببرید.»
🔸
پایگاه یاهونیوز نوشته این اظهارات به نظر می‌رسد که چرخشی آشکار از مواضع پیشین ترامپ در طول جنگ باشد. او که ماه‌ها بر این نکته پافشاری می‌کرد که هدف از جنگ، نابودی هرگونه توان هسته‌ای ایران و حذف کامل «غنی‌سازی» است.
🔸
این رسانه نوشته است: «اکنون این پرسش مطرح می‌شود که جمهوری‌خواهان کنگره دربارهٔ این امتیازدهی تازهٔ ترامپ چه خواهند اندیشید. اگر توافق نهایی صلح بین ایران و آمریکا هیچ‌گونه محدودیتی بر برنامهٔ هسته‌ای ایران نداشته باشد، در عمل از توافق برجام (۲۰۱۵) با ایران نیز بدتر خواهد بود.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/442907" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
قالیباف: مهم‌ترین ضمانت برای تفاهم فقط قدرت ماست وگرنه دشمن قابل‌اعتماد نیست
🔹
ترامپ قطعنامه‌ رسمی سازمان ملل را جلوی چشمان همه پاره کرده پس به هیچ وجه قابل‌اعتماد نیست. @Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/442906" target="_blank">📅 23:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
قالیباف: هدف ما تحقق هدف است؛ گاهی این هدف با مذاکره اتفاق می‌افتاد و گاهی با حملهٔ نظامی‌. @Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/442905" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
قالیباف: رئیس مجلس لبنان به من می‌گفت ایران مایهٔ افتخار جهان اسلام شده است. @Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/442904" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🔴
قالیباف: قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
🔹
اگر مذاکره نبود این موضوع اتفاق نمی‌افتاد و اگر موشک نبود حرف‌های من پای میز مذاکره بلوف و خالی‌بندی تلقی می‌شد. @Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/442903" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442902">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
قالیباف: قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
🔹
اگر مذاکره نبود این موضوع اتفاق نمی‌افتاد و اگر موشک نبود حرف‌های من پای میز مذاکره بلوف و خالی‌بندی تلقی می‌شد. @Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/442902" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442901">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌ چرا ایران در روز آخر مذاکره حمله به اراضی اشغالی را متوقف کرد؟
🔹
قالیباف: ما هر آنچه که می‌خواستیم با حمله بگیریم را چندین برابرش را با مذاکره گرفتیم. ساعت ۲ صبح ترامپ آتش‌بس را در کل لبنان داد و با آن ادبیات با نتانیاهو صحبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/442901" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442900">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
قالیباف: فرق مذاکرات الان با دوره‌های قبل در این است که امروز علمِ پیروزیِ میدان، پشتوانه مذاکرات است. @Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/442900" target="_blank">📅 23:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
قالیباف: وقتی خواستیم در جواب حمله به ضاحیه به اراضی اشغالی موشک بزنیم طرف مقابل گفت که نزنید، ما گفتیم حتما می‌زنیم و اگر پاسخ بدهید منطقه را می‌زنیم؛ این فرهنگ غالب بر مذاکرهٔ ما بود. @Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/442898" target="_blank">📅 23:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
قالیباف: وقتی دشمن به ضاحیه حمله کرد من بلافاصله از جلسهٔ بررسی مذاکره بیرون آمدم و توییت زدم که ما پاسخ می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/442897" target="_blank">📅 23:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442895">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
قالیباف: اگر مردم ما در خیابان نبودند ما نمی‌توانستیم با این قدرت در مقابل دشمن حرف بزنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/442895" target="_blank">📅 23:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442894">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
قالیباف: وقتی حرف از مذاکره می‌زنیم شمشیرمان هم آماده است
🔹
وقتی به ضاحیه حمله شد و بلافاصله عملیات نصر را انجام دادیم و اینجا نیروی نظامی این کار را انجام داد و دشمن متوجه شد وقتی حرف از مذاکره می‌زنیم شمشیرمان هم آماده است. @Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/442894" target="_blank">📅 23:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442893">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
🔴
قالیباف: من یک رزمنده‌ام و با فرهنگ رزمندگی کار دیپلماسی را دنبال می‌کنم.  @Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/442893" target="_blank">📅 23:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
قالیباف: در مذاکره وقتی به دشمن اولتیماتوم دادیم، ترامپ توییت زد و به صهیونیست‌ها گفت باید آتش را قطع کنید؛ ما با مذاکره دشمن را وادار کردیم که این اتفاق بیفتد
🔹
بدون شک این به‌خاطر قدرت نظامی ما بود‌. @Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/442892" target="_blank">📅 23:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442891">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
قالیباف: آتش‌بس را دشمن درخواست کرد و دنبال کرد
🔹
بعد از آتش‌بس دیدید که دشمن اقداماتی انجام داد و ما فورا پاسخ دادیم. ۲ ناوچهٔ دشمن که خواستند عبور کنند مورد اصابت قرار گرفتند‌. @Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/442891" target="_blank">📅 23:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442889">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌ قالیباف: در مذاکره‌ای که خود یک شیوه مبارزه باشد وادادگی وجود ندارد
🔹
همچنین در این شیوه «شعارزدگی» هم وجود ندارد زیرا شعارهای توخالی دشمن را جسورتر می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/442889" target="_blank">📅 23:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442888">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌ قالیباف: مذاکرۀ فعلی ما از موضع قدرت است
🔹
من در زمان برجام هم گفته بودم فقط با مذاکره‌ای موافقم که خودش نوعی مبارزه باشد. @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/442888" target="_blank">📅 23:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442887">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
قالیباف: امروز در هر ۴ جبهه میدان مبارزه، میدان دیپلماسی، میدان خیابان و میدان خدمت هرکس دقیقا می‌داند چه کاری باید انجام دهد. @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/442887" target="_blank">📅 23:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
قالیباف: اجازه ندادیم آمریکا و اسرائیل به ۹ هدفی که خودشان از آغاز جنگ مطرح کردند برسند.  @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/442886" target="_blank">📅 23:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
قالیباف: قدرت اول نظامی، سیاسی و اقتصادی دنیا در کنار رژیم صهیونیستی که یک قدرت هسته‌ای با آخرین تکنولوژی‌ها است در مقابل ما قرار گرفتند.
🔹
صحنۀ درگیری این جنگ تاثیرات جهانی داشت و یک موضوع بین‌المللی بود؛ این جنگ رویارویی حق و باطل بود. @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/442885" target="_blank">📅 22:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442884">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
قالیباف: قدرت اول نظامی، سیاسی و اقتصادی دنیا در کنار رژیم صهیونیستی که یک قدرت هسته‌ای با آخرین تکنولوژی‌ها است در مقابل ما قرار گرفتند.
🔹
صحنۀ درگیری این جنگ تاثیرات جهانی داشت و یک موضوع بین‌المللی بود؛ این جنگ رویارویی حق و باطل بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/442884" target="_blank">📅 22:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔸
۱۰. ایالات متحده آمریکا متعهد می‌شود بلافاصله با امضای این یادداشت تفاهم و تا زمان خاتمه تحریم‌ها، اسقاطیه‌های وزارت خزانه‌داری را برای صادرات نفت خام ایران، محصولات پتروشیمی و مشتقات آنها، و تمامی خدمات مرتبط شامل تراکنش‌های بانکی، بیمه‌ها، حمل و نقل و غیره صادر کند.
🔸
۱۱. ایالات متحده آمریکا متعهد می‌شود تا وجوه و دارایی‌های محدود یا مسدود شده جمهوری اسلامی ایران را با اجرای این یادداشت تفاهم به طور کامل برای استفاده در دسترس قرار دهد. ایالات متحده آمریکا و جمهوری اسلامی ایران در مورد روال مربوط به آزادسازی این وجوه در طول مذاکرات، به صورت دوجانبه توافق می‌کنند. این وجوه، چه در حساب اصلی نگهداری شوند و چه منتقل شوند، برای پرداخت به هر ذینفع نهایی که توسط بانک مرکزی جمهوری اسلامی ایران تعیین می‌شود، باید به طور کامل قابل استفاده شوند. ایالات متحده آمریکا متعهد می‌شود که تمامی تاییدیه ها و مجوزهای لازم را در این رابطه صادر کند.
🔸
۱۲. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند تا یک سازوکار اجرایی برای نظارت بر اجرای موفق این یادداشت تفاهم و پایبندی آتی به توافق نهایی تشکیل شود.
🔸
۱۳. پس از امضای این یادداشت تفاهم و منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این یادداشت تفاهم و تداوم اجرای این اقدامات، جمهوری اسلامی ایران و ایالات متحده آمریکا مذاکرات درخصوص توافق نهایی را منحصرا در مورد بقیه بندها آغاز خواهند کرد.
🔸
۱۴. توافق نهایی با یک قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تایید خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442874" target="_blank">📅 22:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
متن یادداشت تفاهم اسلام‌آباد درباره خاتمه جنگ تحمیلی
🔸
۱. جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان، اعلام کرده و تعهد می‌کنند از این پس هیچ جنگ یا هیچ عملیات نظامی علیه یکدیگر آغاز نکنند و از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین کنند. توافق نهایی خاتمه دائمی جنگ در تمامی جبهه‌ها، از جمله در لبنان، و بقیه مفاد این بند را تایید خواهد کرد.
🔸
۲. جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌شوند که به حاکمیت و تمامیت ارضی یکدیگر احترام بگذارند و از مداخله در امور داخلی یکدیگر خودداری کنند.
🔸
۳. جمهوری اسلامی ایران و ایالات متحده آمریکا به انجام مذاکرات و حصول به یک توافق نهایی در مدت حداکثر ۶۰ روز، قابل تمدید با رضایت طرفین، متعهد می‌شوند.
🔸
۴. بلافاصله با امضای این یادداشت تفاهم، ایالات متحده آمریکا شروع به رفع محاصره دریایی خود و هرگونه مزاحمت یا ممانعت علیه جمهوری اسلامی ایران می‌کند، و ظرف ۳۰ روز به محاصره دریایی به طور کامل خاتمه خواهد داد. در طول این مدت، تردد کشتی‌ها متناسب با تعداد ترافیک قبل از جنگ که از سوی جمهوری اسلامی ایران برقرار می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود تا ظرف ۳۰ روز پس از توافق نهایی، نیروهای نظامی خود را از حوزه پیرامونی جمهوری اسلامی ایران خارج کند.
🔸
۵. با امضای این یادداشت تفاهم، جمهوری اسلامی ایران ترتیباتی را با حداکثر تلاش خود برای عبور ایمن کشتی‌های تجاری، بدون هزینه فقط برای ۶۰ روز، از خلیج فارس به دریای عمان و بالعکس، اتخاذ خواهد کرد. تردد کشتی‌های تجاری بلافاصله آغاز، و با توجه به ضرورت رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز برقرار خواهد شد. جمهوری اسلامی ایران با سلطنت عمان برای تعیین اداره آینده و خدمات دریایی در تنگه هرمز، مطابق با حقوق بین الملل قابل اجرا و حقوق حاکمیتی کشورهای ساحلی تنگه هرمز، گفتگو خواهند کرد و با دیگر کشورهای ساحلی خلیج فارس نیز تبادل نظر می‌کنند.
🔸
۶. ایالات متحده آمریکا متعهد می‌شود، با شرکای منطقه‌ای خود، برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران یک برنامه قطعی مورد توافق طرفین را با تامین حداقل ۳۰۰ میلیارد دلار ایجاد کند. سازوکار اجرایی‌سازی این برنامه، به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. تمامی تائیدیه‌ها، اسقاطیه‌ها و مجوزهای مورد نیاز برای تراکنش‌های مالی مربوطه توسط ایالات متحده آمریکا ارائه خواهد شد.
🔸
۷. ایالات متحده آمریکا متعهد می‌شود به تمامی انواع تحریم‌ها علیه جمهوری اسلامی ایران، از جمله قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، و تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه، برابر یک برنامه زمانی مورد توافق به عنوان بخشی از توافق نهایی، خاتمه دهد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوع خاتمه تحریم‌ها که در بالا ذکر شده است اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
🔸
۸. جمهوری اسلامی ایران مجدداً تایید می‌کند که سلاح هسته‌ای تولید یا ابتیاع نخواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت کرده‌اند که وضعیت مواد غنی‌شده ذخیره شده را از طریق یک سازوکار مورد توافق طرفین و مطابق با برنامه زمانی مندرج در بند ۷، حداقل به شیوه رقیق‌سازی در محل، تحت نظارت آژانس بین‌المللی انرژی اتمی، حل و فصل کنند. دو طرف همچنین موافقت می‌کنند تا در مورد موضوع غنی‌سازی، و دیگر موضوعات مورد توافق دو طرف مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران، بر اساس یک چارچوب رضایت‌بخش که در توافق نهایی مورد موافقت قرار خواهد گرفت، بحث کنند. توافق نهایی مفاد این بند را تایید خواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوعات هسته‌ای ذکرشده در بالا اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
🔸
۹. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند که تا زمان توافق نهایی وضعیت موجود را حفظ کنند؛ جمهوری اسلامی ایران وضع موجود را در برنامه هسته‌ای خود حفظ خواهد کرد، و ایالات متحده آمریکا هیچ تحریم‌های جدیدی علیه ایران وضع نخواهد کرد و نیروهای نظامی بیشتری را در منطقه مستقر نخواهد کرد.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442873" target="_blank">📅 22:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EreBmeExbceWHxWp1JcB4ShDbSv7SrAyikcT4tVd6j2i02y_VVWf4YNssXd3hWJ3N7GBVWtIhezMnKE3f0bVzDch-jr5yyHSxvFTpTJg2UTqSfZ5Z3lWoK6QMBF8FFArev2cEkaVEtyCldLaYvnhJqi5BiMWJcT7KGaiGUKhegGm5VTiXWmOzr4iiXBKKIEMYQbiJaNKyAssp7m2OXijcY2qPL44T3NMNHwWvexx6kU4aV1WZLgbwtgpJlg0qoa7_HYHoYFD75vuxzY7ToJBSSDp3jaACtXQprXLjcO9mhbOAPMY-5HcCKJMioUrKLQviKgCSsir6A61HTMujb4Bxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قیمت جدید محصولات ایران‌خودرو اعلام شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/442872" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336bbeb987.mp4?token=hK26v00wPuHu9Uxl0eNo5jlW0S31mnKkcngHFi_jwEvhwn1_ITnTRD8XEhbqmiPvvGl-1I24YIkVrtGNBfkyKM4S1NQ_pgRZDaMprtDL7yjY132EK8FxSoiRLBPiBfIrn1kzM-aQ_bXN9_I2gMfNcrm7p0T2uldVLU10HUeE7-a-9T8qCCk9kMqB3R3iQ0Oqk_Six--nXv-Di16VPeeJJndJWrDAfbKTtVEGruw4a-cVZLHJbcYkAldYMhejmRxye-gsrKGvaAoOnA7Tl2OJAcO8r3gOYyKx2lOtmTMM_8uyOhw-JmpTuPjQQweTlPE-Jy30Nt2TgXcWh6itOqYB2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336bbeb987.mp4?token=hK26v00wPuHu9Uxl0eNo5jlW0S31mnKkcngHFi_jwEvhwn1_ITnTRD8XEhbqmiPvvGl-1I24YIkVrtGNBfkyKM4S1NQ_pgRZDaMprtDL7yjY132EK8FxSoiRLBPiBfIrn1kzM-aQ_bXN9_I2gMfNcrm7p0T2uldVLU10HUeE7-a-9T8qCCk9kMqB3R3iQ0Oqk_Six--nXv-Di16VPeeJJndJWrDAfbKTtVEGruw4a-cVZLHJbcYkAldYMhejmRxye-gsrKGvaAoOnA7Tl2OJAcO8r3gOYyKx2lOtmTMM_8uyOhw-JmpTuPjQQweTlPE-Jy30Nt2TgXcWh6itOqYB2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: امام شهید ما مثل مردم زیر آتش ایستاد و خانه‌اش را ترک نکرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/442871" target="_blank">📅 22:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY2FFhRUjEwS7EDTUso9lhIOaeSxiWzSz2zXKHJJWcULQSXwSWDnlaSaHQ-3O3JD6VxZgIw7ojdri2oqg6SkjqBCsPTaw1wJ9TLtlReHPGNkyH3Wd_qGP9oucKxwSV8kJ9t7_XVUeIQGj-NXL9ThMwIZXvgBLiy1OCneJNngiaizwCqx3Q2daP6kX61z2v5aNHUf9vdYxlskE4pCK9U7misY8mLzt9WVTlHSBce_962CXQ7u0k1nrrUkZg_3WPPDQ_Xw1yYtZQKO1lBwpi-hAYk-uBSGa9M5wf86EwpPKF6Poh3xkaj7qIm91YxX_xmDHFtyc7XPn_cNGsQJlYtTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاران رونالدو همه را ناامید کردند
⚽️
پرتغال ۱ - ۱ کنگو
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/442870" target="_blank">📅 22:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDO4KJ5DQYofcxGow9D34wKM_Lcj7RBbLO8SnbaV-0YLX3XQx8qy8WKYF5aFZNwy4ECUrIE2NBALZ-0tcdWch-7COJbwPZ7xbJKi4DG0uEdcycyMPfODftT_Xwkyhb_cc4P56cSK18bWKihTLpA8Rjivm1Hx-1DmCNuhk_iGPLzBizFjjBr2RFriF9CqXHb3MRfOIXYWY-lVJTM9Y-fBBwDsQedIcbPj8rjvozBiaa9nr6UfxUKNwq9mdl13vc2yFCO_SWh2HYuZwKPj1y_0yOAh9aLEHPACVqpNTMgv9UdAVVtJHK6FT7Tla-F69GBwPw2eu9Z0Zs-NOY5QmCGozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل سایپا: مجوز افزایش قیمت نگرفته‌ایم
🔹
در صورت صدور مجوز افزایش قیمت، موضوع از طریق سامانه کدال به اطلاع خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/442869" target="_blank">📅 22:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
کی دلش اومد با تو بجنگه بابا؟
🔹
نماهنگی از زبان پدر خطاب دختر شهیدش در مدرسه میناب با صدای محمدحسین حدادیان.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/442868" target="_blank">📅 21:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: دربارهٔ اموال مسدودشدهٔ ایران، طرف آمریکایی تعهد داده که موانع را رفع کند.
🔹
بخشی از مذاکرات در این باره انجام شده است. برای ما مهم است که به اموال ملت ایران دسترسی داشته باشیم این که به چه نحوی باشد جزو تعهدات آنان است.
🔹
در این مرحله…</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/442867" target="_blank">📅 21:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تعهد ما این است که در مدت مشخصی، ترافیک دریایی را تنگهٔ هرمز به حالت عادی برگردانیم
🔹
این مربوط به خود ماست و نیازی به مشارکت یا مداخلهٔ طرف‌های دیگر نخواهد بود.
🔹
برای تدوین سازوکار مدیریت تنگهٔ هرمز و خدمات دریایی، ایران و عمان همکاری…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/442866" target="_blank">📅 21:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ادامهٔ اشغالگری رژیم صهیونیستی در لبنان به معنی نقض تفاهم‌ است و تدابیر لازم در مورد آن اتخاذ خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/442865" target="_blank">📅 21:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ایدهٔ امضای از راه دور یادداشت تفاهم اسلام‌آباد توسط روسای جمهور ایران و آمریکا درحال بررسی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/442864" target="_blank">📅 21:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442856">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
منبع آگاه: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس، از مطرح شدن پیشنهاد امضای الکترونیکی متن تفاهم‌نامه میان ایران و آمریکا پیش از سفر هیئت‌ها…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/442856" target="_blank">📅 21:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442855">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
بدون تعارف با خلبانان قهرمان ایران که پایگاه آمریکا در کویت را بمباران کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/442855" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44359a14c.mp4?token=k7eevhoJPSBklGC9uWseGg4wmXaK2tKJ0ydHf62xnT6KmphkZ8tQemco33KWe8qVA8Ycz558jmi7lZaNeYcFP9rw2TuGmbYfNngakLsezuMeWi2uEMVtS86uNNed6O-Eb6JgNlGvqfnCiYXPxwEu5tlZ02HX-HA9eV8H5C9ZnnW-37p7yom0VIpc7jvDnPPAmKToaKUDqL79T8fIjdWvGkhvnjUuyA_wU5lLZTRWkUOqVGgui5fYwAtJ5MxiRjVUDCwm4WR24EQdVvFkdeyVK79dz1iNTgcI-QBI76-isJHo9eQUl7tERA5Gi5vRek1ujfJOKMTrIO34VBxkulkxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44359a14c.mp4?token=k7eevhoJPSBklGC9uWseGg4wmXaK2tKJ0ydHf62xnT6KmphkZ8tQemco33KWe8qVA8Ycz558jmi7lZaNeYcFP9rw2TuGmbYfNngakLsezuMeWi2uEMVtS86uNNed6O-Eb6JgNlGvqfnCiYXPxwEu5tlZ02HX-HA9eV8H5C9ZnnW-37p7yom0VIpc7jvDnPPAmKToaKUDqL79T8fIjdWvGkhvnjUuyA_wU5lLZTRWkUOqVGgui5fYwAtJ5MxiRjVUDCwm4WR24EQdVvFkdeyVK79dz1iNTgcI-QBI76-isJHo9eQUl7tERA5Gi5vRek1ujfJOKMTrIO34VBxkulkxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توجیه ترامپ برای بمباران مدرسهٔ میناب
🔸
خبرنگار: آیا می‌توانید بگویید که کسی را در دولت خود مسئولِ حمله به مدرسه‌ای که در روز اول جنگ منجر به کشته‌شدن بیش از ۱۰۰ کودک شد، خواهید دانست؟
🔹
ترامپ: خیر، اگر خطایی رخ داده باشد، طرح چنین سؤال عجیبی در این مرحله…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/442854" target="_blank">📅 21:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442852">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
منبع آگاه: سفر تیم مذاکره‌کننده به سوئیس تاکنون لغو نشده است
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس، دربارۀ برخی گمانه‌زنی‌ها پیرامون لغو سفر هیئت مذاکره‌کننده به سوئیس اظهار داشت: تا لحظه تنظیم این خبر، سفر هیئت مذاکره‌کننده…</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/442852" target="_blank">📅 21:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442851">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7613f3ae0.mp4?token=gPyPHy79O7jMICRw0qZiAPzMPZLCJVd-RqsR1bLi0Fymy0L_NQvYKqREWXWPrgBwrj3tLsutgFNuIkJxvtDF26-MlLKJYfJZsKtdNlm2AkI30qpvfN0NBpCgmRzX-Fv6Pd4SsPH3WeXr_Z-W0RtRGLaZ9nwEiHt4MlCW6dgMC7WILNnLzHKT7FLWDRqCU5pU0U04T7F1717xYYM2OvCmGcWta6DsqWDHJBBGG8EmyzkT5J76KYQj-wX1ZyZdbmM1G84gPbZFK0BS-Fafd4bxZa7F57i0YPFa5XTYkLryPmHDYIugdicif_gDaNY-U32QOmcTQ4KopmM5V8VkSt5CgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7613f3ae0.mp4?token=gPyPHy79O7jMICRw0qZiAPzMPZLCJVd-RqsR1bLi0Fymy0L_NQvYKqREWXWPrgBwrj3tLsutgFNuIkJxvtDF26-MlLKJYfJZsKtdNlm2AkI30qpvfN0NBpCgmRzX-Fv6Pd4SsPH3WeXr_Z-W0RtRGLaZ9nwEiHt4MlCW6dgMC7WILNnLzHKT7FLWDRqCU5pU0U04T7F1717xYYM2OvCmGcWta6DsqWDHJBBGG8EmyzkT5J76KYQj-wX1ZyZdbmM1G84gPbZFK0BS-Fafd4bxZa7F57i0YPFa5XTYkLryPmHDYIugdicif_gDaNY-U32QOmcTQ4KopmM5V8VkSt5CgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: هیچ‌یک از رهبران گروه ۷، نگرانی خود را بابت نقض احتمالی قوانین بین‌المللی در جریان حمله به ایران ابراز کردند؟
🔹
ترامپ: «خیر. خیر، در واقع کاملاً برعکس؛ آن‌ها احساس می‌کردند که [ایران] بسیار خطرناک است. آن‌ها بسیار آسوده‌خاطر شدند، چون ممکن بود خودشان…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/442851" target="_blank">📅 21:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZdP_KiSXo35DU8CJlQ6miu0lQm-i6AMl9Mx-SCftMN5oAhOI0uDZMKB5vcZ4Xo9GmzcCnINe3Fhjdjldm4uhhY3OSzXaQVHn6comx7hsg_dQKYrZjY7Ce1oV6amM8uoB4vvSL4gh_2OkRXzQh7BVsRRm_hNL2YkFoRnZUx5d6NeuvYESwinPhHeHnq3f2Je5nbnM7C0lvlSJn4zhIHEOMUiZi2y8fNZuF3w0PbD2GBm8GEP1IqxkPc38ghkiadGJNT8ETKnRp7cMblFF-XgikR5atmaitm3owYML4QBWUIXdEdJeVkJ5kXsT0WYU-pSBFs5l1LHta1YLVdyHp-CGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxkiIzqKtvY2NonWc_MP5D1GC9rdGm2NJNV6n-Os8HcNsRiIQJ3hshDbuchdx7f6EqtVbw-5N5dVudT-yDR8lqljPddkG4VdIbtRLiZz5OH-ng6muAP9mUaYdJ2L9D_ZsaKx2w1SKcydnfFZCbM44ISl-bs_TVGoJosVzPEfO95UrZ9_6-gg20l6A9NDdsKoOLTeKiY4-QqL-gChuLct-ORr1X1itiNmf6IbQQ2-QdNf9MgIyXhJR0JEqSrUD2r2OdigXYkkZS4Zgk7XaWI3VA9tYjEGSh7GRMUF_CbjT0iXxeYbeY3baMnqdQYa0p5_iYxvrzgN65CKFzbCZBi8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itFBUEWeoGOhrStJqa2pEiD7_GB0RicZsUx-v55cVPBOSvrPQycpm5kE-ZojX3cIbSt_cVo2KCVBQMhtNq1ZN8uwKUZy14DUseAHqXpuxGDMZW_6aUt7IVv4sza61mBwAi6fIFCUmIyb1_gf7TAm1cXSbjmZz0oOzPXtQzKwXYJqZHwsK_FUgd7DfK5kjrlQW_atQfu_3-Oa1HfD2OY6Pyo0Gy5Nc8qjnhPYjblezE87X6uLge56_Xp4-CVdCVK-9ViCnsekK0-EGL_XKMGpg_w-QXwbKryonytrsTBcxi0TGhdriATY5KCE6jCg0imkZA8hXF7fcP9qX5m-AdAkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy3sKZmQ4TsRTkz8ukG-ZwjOWkCeGq9nIFW38friUDSU3eKrvs8_ROkZiPVBqbQ0cbbnMTHTw2fSEZUsF7al_kLQkkAQFEcanjvgDiOaq3OmBG8-LGdcOVWoVIKa3i8pUD_wp44k2Z86AFW4hg2zoOG32QtjnmX1SqQ1sgmS0Jg-8heh6q4NlAIrm4r-wSpuMcZuWeWy5nX5q3B0hIbN2Gf62vH9m3eWgEK7NXF_LBdp1pQ24I4dXaUU6iDz0EKa0ahEzr_YXg1Bof6E9QLVbktRN8MSbeei3oYb1iXeDjZ1npggxqULA4sGRxm0O08scioIjIrKrQEgqdB4ociwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V89vJwTK02yXAoeB9SgjgBx_GwasUEb6xzxcfqEMc8ow8h919T1pSrvm7jRF5CKq1o2xHLJIzgyABoOBluio28YzSuhsImQvK26LH-o6PLNmj4kdjgvKdPr-Ka08qyOgy5e2TZuTsC-1iuOoAfIvrK2Fpv9mJwoBXqGeEtO8yDiYB6_sApJpZaRgO56oeHkUAK-WUThpWE2pPchnMMPuTGGbSHCD_9Q-s4nPe28Fi6XUIFvi3Vww9xZZMNF_qdjVTvbyB4eydfa9SXWhaxVNqEdfCW_skqaL2BqWXoLswMl4tZEZkRoMxNtW21P5LfInW3pJsI0r5eA4RBQ4Fly_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efhi9IpM_FILUmgDUOn8XJjz8yNw3goV1kOvYdMuvT87-KKLkKutT5wY1uNOB1Gp4m2QWxAgESOhyYWk-dT8VIGTEI1k_D2_Xri_X73zMAaNQVEqDli1RJlBIIp7J4DkGfUJKpCnFde4YpTUxxvWnTDLkrmUAtt3JtPwWNMtFW6V6t1j-lhMnhnS-7XtnWTi7rhQyUitAmRZm1tY4vN6VJMcw5XGHDILEI6Crhsoq1i_VWGfP_ecynu46RPg_OZ5drCVoZcC6fUChgiogQB3y4lweWHMWH7G2Wb022iQ7TtXNiIlGjwTLBMhDlozp6_EPzZPSC8CbLvdo7JjTJE0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MPIpE3Y4enHmtGaQ5bStCAl8jf0RteSgVEOyTSvLFTduLf11gn82T9GDFgcFgXBJesKXgJWco_0poqxv3EDyoZo5Ut6SdbVWUO3fKeezEuuyiu9pnt881_oK84fDzrWynEqSN8k0RcL9KmYZNqILG2S-eLz04dMvMl2HwBfs3V_rSHB5jffhXcw8yxHe_BPMM4M6dfS32lEbQYXmBJiARkdyFFNU9aBUaNZIzqUKEdLbtfGUKSp69-8uKJ0ZjjHo-fwBPIprNhQK1hLpQaOKHaTe_arPcAIQ9T4usOXrcu_DiFvDmSa_jB1oXm-0C0zkLs5k7jj3LSuE6U4dVyZZ2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین ورود نمادین کاروان حسینی به کربلا در مریانج همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/442844" target="_blank">📅 21:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f24d5483.mp4?token=siaw_GDMHuYhMkVcQujsU2n7AbzS5Lq6HGbcqSTs2vaFXmb1rEPy4zLl0zk1ixaRiygO0xGVGJ368Coe_9vPsYZ38xiccJAwU0Wm1m5isdFUuwc-AFiWK1c1_mENLhSz8_YVHIS72_TJ5OH4-BUSWAslM2a352zxTAvMJpmrw4PnKqSK3l3atVjtq2W0XYdLrIDZP7DvZlzdVcAore-jB8LH-7mKjAODqytSgf1LKCrBzzDvs1OUaJOCAeUDVWIE2OyupVEqBGwoT-bVD1cp83QCcZO1Y-4fhR0St4QYNHUGn2Q3NaKMuvQGXGWHiZB-IDshAKtQPuxPRnSRu2UfEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f24d5483.mp4?token=siaw_GDMHuYhMkVcQujsU2n7AbzS5Lq6HGbcqSTs2vaFXmb1rEPy4zLl0zk1ixaRiygO0xGVGJ368Coe_9vPsYZ38xiccJAwU0Wm1m5isdFUuwc-AFiWK1c1_mENLhSz8_YVHIS72_TJ5OH4-BUSWAslM2a352zxTAvMJpmrw4PnKqSK3l3atVjtq2W0XYdLrIDZP7DvZlzdVcAore-jB8LH-7mKjAODqytSgf1LKCrBzzDvs1OUaJOCAeUDVWIE2OyupVEqBGwoT-bVD1cp83QCcZO1Y-4fhR0St4QYNHUGn2Q3NaKMuvQGXGWHiZB-IDshAKtQPuxPRnSRu2UfEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع اهالی منطقۀ شهران تهران در شب ۱۰۹ بعثت مردم
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/442843" target="_blank">📅 21:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqzrwqmN_4zmLNhVQ9TZrVW_xS6GJV-oTXA2zl8_BL7YWy1LrIkHFSUFLJFpYCohr8lMu5EhrfAm99IV7vplU-63zOpqnQyYypQSHtzsclNfqKc93ZrzgVM7_ARuapYKmdTxhEqrO6fdkz3yUmvYSRq7V8rZMZUUn-7gxlST5HGdLkhGHXyqnTsiwyP_1FTwPuSQMobj2F20O-dJKciVBLPqxnsYe_lHD5ZWbLf_3guPkbLx3Iy0b5NDJQi3BJ2qqXPwRPZdOqEmJ25uXOTQwbCUKcL-sze0qRGh5-ZnMqYb3O9TNFVWm_1abEIiqgSg20_3s71Eu0XQXKNv-74QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قیمت جدید محصولات ایران‌خودرو اعلام شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/442842" target="_blank">📅 21:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45cbfb6feb.mp4?token=ginEpy2azCKd3F957xCrWf-tTRGlClg5fz1dk0gZK_gZ2VVXLCnPtxWhcCyj5HtRQeC4pMVcFQmVERlnWDBQ1dDPmryxeqPoOowMv1EuPgk2T0PLp6b5PMJniorHEcZyzdvoDA7g9UzZM311e8WBEwl_8xA8uIlw3zQUPzlAASHiIKQaUi_NwIEqT7C7_j-0FRUo1TgOpuoFv_cL9NyR6Uf9r26x7UrNap4Q7CqyASQMTs6_OEnmVhRDiynZ7ErVI69eJ62_CyLhXl9T18Bun71_mrPyYJBp6x829KD3XiSwiftt8ruP2BezHmEM9wwQjRJKx60uAt6tD0gkqsinBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45cbfb6feb.mp4?token=ginEpy2azCKd3F957xCrWf-tTRGlClg5fz1dk0gZK_gZ2VVXLCnPtxWhcCyj5HtRQeC4pMVcFQmVERlnWDBQ1dDPmryxeqPoOowMv1EuPgk2T0PLp6b5PMJniorHEcZyzdvoDA7g9UzZM311e8WBEwl_8xA8uIlw3zQUPzlAASHiIKQaUi_NwIEqT7C7_j-0FRUo1TgOpuoFv_cL9NyR6Uf9r26x7UrNap4Q7CqyASQMTs6_OEnmVhRDiynZ7ErVI69eJ62_CyLhXl9T18Bun71_mrPyYJBp6x829KD3XiSwiftt8ruP2BezHmEM9wwQjRJKx60uAt6tD0gkqsinBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: هیچ‌یک از رهبران گروه ۷، نگرانی خود را بابت نقض احتمالی قوانین بین‌المللی در جریان حمله به ایران ابراز کردند؟
🔹
ترامپ: «خیر. خیر، در واقع کاملاً برعکس؛ آن‌ها احساس می‌کردند که [ایران] بسیار خطرناک است. آن‌ها بسیار آسوده‌خاطر شدند، چون ممکن بود خودشان…</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/442841" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442839">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfed1494b7.mp4?token=opErP0_774y9BcXqtANmYirM2w1pAwOI-zmPVeT8UHYkYqkAVQnu763TzU1m1dV0PvXSAyG6wo989vT8tWS9WOhKLqRwgjxuWV2LIfvV0eR_c2EbBMYAyCr1uXQCGN2Dbrnc6DO9D4lFABEvgDWMAI8_Rb149f0uFeUV8QqSa4G_DVyBT4JKCVXxIsp0FIl7D_ogjoT1PYcck-278i7BA4pIvefNytDrSya7gKdt98JPDH5u5DG9Gp4KupBCG2wb9SD8EcWbfRPieew4d0RTB_qPzwaujreTYP_OZGvaZ2aY8cx8bRztx8wx6OCzsDD364h-QKp_IkTtR5GjxVmglVd7PJvA0NaD91WdsMRECL6wANgY_y4Tn4ZZo2aDy2QjQoN8xrk4SYMf-xLEuDMPzSuU30tQwcct49HQYYml1GtkQPTTowizeCfwSG_PaT3n3MioetPOAti8UHv01x7KSTRXKvdRTN0VAcWfcWoE3IM7dbSv1CFuCtqI20DevnNd0MyyHOC7R6VwQOzMk3CYBH0nFpqSskgKXVFVaI59PrNSwQjAtaiXdkWBGkOWvGUpshUhGPXkQiwts2Fo4lKDr289ffBWSRIBem9gZQwooavlqkOwm4GC7tIrE4MD76cTNbvBsKgOfKsRhaMMkRt5BXjCN9NDwruIKSlSwcUbul4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfed1494b7.mp4?token=opErP0_774y9BcXqtANmYirM2w1pAwOI-zmPVeT8UHYkYqkAVQnu763TzU1m1dV0PvXSAyG6wo989vT8tWS9WOhKLqRwgjxuWV2LIfvV0eR_c2EbBMYAyCr1uXQCGN2Dbrnc6DO9D4lFABEvgDWMAI8_Rb149f0uFeUV8QqSa4G_DVyBT4JKCVXxIsp0FIl7D_ogjoT1PYcck-278i7BA4pIvefNytDrSya7gKdt98JPDH5u5DG9Gp4KupBCG2wb9SD8EcWbfRPieew4d0RTB_qPzwaujreTYP_OZGvaZ2aY8cx8bRztx8wx6OCzsDD364h-QKp_IkTtR5GjxVmglVd7PJvA0NaD91WdsMRECL6wANgY_y4Tn4ZZo2aDy2QjQoN8xrk4SYMf-xLEuDMPzSuU30tQwcct49HQYYml1GtkQPTTowizeCfwSG_PaT3n3MioetPOAti8UHv01x7KSTRXKvdRTN0VAcWfcWoE3IM7dbSv1CFuCtqI20DevnNd0MyyHOC7R6VwQOzMk3CYBH0nFpqSskgKXVFVaI59PrNSwQjAtaiXdkWBGkOWvGUpshUhGPXkQiwts2Fo4lKDr289ffBWSRIBem9gZQwooavlqkOwm4GC7tIrE4MD76cTNbvBsKgOfKsRhaMMkRt5BXjCN9NDwruIKSlSwcUbul4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مردم به منتقدان: تجمعات، مشق کربلاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/442839" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a2c30169.mp4?token=e9WZhEhdMR4GOVqHzP-ixi53tzrOd-rag6DAopzkHNywjMyo8D1tVvXBEWiYhmb5ZgXdypqco4c5D38o56IxC1POMU56zwIfK4kHWmvKwQ0e369VR2gdlCIYO7Sh_pAgedOWP4kStccNaw5jNabSRiepvPUH6JjaYwI_03pFXoRiMPgUxBO9DcZKSHo2hLqUKqkMzcNJIFIh3M6v4VhnLvZ35c-DJ46ZKNTV235cMDSLqdhfcYzmDBV9bvtnoaKUVjlgSUtodlw3yv9djUGnE0dTiojL6mCxIgLhbLT_TnU_XYXYfHUogrPG23FJgME-jE8GdOjmqv-7GJphEtyKpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a2c30169.mp4?token=e9WZhEhdMR4GOVqHzP-ixi53tzrOd-rag6DAopzkHNywjMyo8D1tVvXBEWiYhmb5ZgXdypqco4c5D38o56IxC1POMU56zwIfK4kHWmvKwQ0e369VR2gdlCIYO7Sh_pAgedOWP4kStccNaw5jNabSRiepvPUH6JjaYwI_03pFXoRiMPgUxBO9DcZKSHo2hLqUKqkMzcNJIFIh3M6v4VhnLvZ35c-DJ46ZKNTV235cMDSLqdhfcYzmDBV9bvtnoaKUVjlgSUtodlw3yv9djUGnE0dTiojL6mCxIgLhbLT_TnU_XYXYfHUogrPG23FJgME-jE8GdOjmqv-7GJphEtyKpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: در ۲ روزِ آخر جنگ بمب‌هایی به ارزش ۲۰۰ میلیون دلار روی ایران ریختیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/442838" target="_blank">📅 20:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3se_wt1slmLjCJmjamI8tsQpmGFc_SsiSN26IsNN194cXCDALkboydqfkn9izcMf2cvgOAbSKEsuSDuluzukrNcFea7bt_9I9v9r16h9Utpvn07yACp5AhgZNzBSPFJGXUSvTD2W4q-d4HFVbzsvnM0YzAW0B9gfAn_Yrn3Dd8m6WdAxxcZN690CDQTU8hxggJ_c6Qur8FRCbWrr33KKFSqFRBJrJ7-bDSNxOIMScPozHk-1f3dRZREce9FADPgBCBTr_JSQang3PxqUu9nB7sELVMVST5nzTKrMQKh1vKe-J3PGHSDLtkNJXoU34Dkn1lGKGCqkvUMcntSy_Z32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر پول ایران را پس ندهیم، هیچ‌کس در دلار سرمایه‌گذاری نخواهد کرد
🔹
ما مقدار زیادی از پول آن‌ها را گرفته‌ایم، پول آن‌ها را از آن‌ها گرفته‌ایم.
🔹
این پول ما نیست، پول آن‌هاست و ما آن را مسدود کردیم.
🔹
در یک مقطع زمانی خاص فکر می‌کنم باید آن را پس بدهیم.
🔹
اگر آن را پس ندهیم، هیچ کس دیگر هرگز در دلار سرمایه‌گذاری نخواهد کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/442836" target="_blank">📅 20:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc8405859.mp4?token=jzmlUgVNsKE_AV5Xkoz_VKV8Do0mFkuSbCi7rOacFpOVKbf-EGKPsy0ipdXIJkg9VwMJDWFn7pH5dj0ahKSUMq1tcM5T8Xfw2XCGxoLOPqvV-mOvBMx7iuHQsSPijxY-NLs2_EIynXqdpz4j7W5vL5LDtc8KxZubMzYTmeA1Q_xve_6eio42UROKl3_dlFcZPa3GdQZmUh7qEx2lqBxaG9TxRILf7BjaJ3QKmTf8rkM5O7heUszvN2zx5lvsWmgi3CbM9foRFQdiQvvecV8PQ6nV1QFXXIGS6Mc-yEDrFqsi4OC7M9ktLvxhUn1y37CupX1IkCAn7vMidSguziRDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc8405859.mp4?token=jzmlUgVNsKE_AV5Xkoz_VKV8Do0mFkuSbCi7rOacFpOVKbf-EGKPsy0ipdXIJkg9VwMJDWFn7pH5dj0ahKSUMq1tcM5T8Xfw2XCGxoLOPqvV-mOvBMx7iuHQsSPijxY-NLs2_EIynXqdpz4j7W5vL5LDtc8KxZubMzYTmeA1Q_xve_6eio42UROKl3_dlFcZPa3GdQZmUh7qEx2lqBxaG9TxRILf7BjaJ3QKmTf8rkM5O7heUszvN2zx5lvsWmgi3CbM9foRFQdiQvvecV8PQ6nV1QFXXIGS6Mc-yEDrFqsi4OC7M9ktLvxhUn1y37CupX1IkCAn7vMidSguziRDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: وقتی [سربازان] جوان‌ آمریکایی را می‌بینید که‌ بدون دست و پا حرکت می‌کنند، یا صورتشان بر اثر انفجار متلاشی شده است، بدانید ۹۵ درصد این موارد کار [قاسم] سلیمانی است
🔹
او همه‌کارهٔ ایران بود و مورد احترام قرار داشت. او یک نابغه بود. از قضا اهل ایران…</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/442835" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj7Uz5nKwXiEX7ThpcowciAtbdCHNRojJT5HpGsE0XaxbptRG0SdwDEWJZCKash27BX86ESlIa72H4no1U3KkaGKbMjU1JDrq7ac-hhfN1uYj7FARFtJaWyAKBku49DyXyZgJK2LkHxW3TM7x1H1LcnMhgO2JRWZaZQrLgwBYvA1kEhtXEv0razY4lYSEuj0rNKdmdkP_tftZII2hTl0KPxdbb-h3nhGhDRI6yysLxefN8wvgK_eUrJluN6jSrxfxJOmmh6WTdvR411m1G3tRyTlfbsXA2bEpXCC8wu1ueoJxpxfaZIVOEM-jQR5aaInr2oORLdB7LzLaL1dSl0fYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس برای مهار گوگل دست به کار شد
🔹
نهاد ناظر رقابت انگلیس مجموعه‌ای از قوانین جدید را برای گوگل اعلام کرد و از این شرکت خواست شفافیت بیشتری درباره نحوه رتبه‌بندی نتایج جست‌وجو ارائه دهد.
🔹
بر اساس این مقررات، گوگل باید نتایج جست‌وجوی غیرتبلیغاتی را بر اساس معیارهای مشخص و عینی رتبه‌بندی کند، اطلاعات بیشتری درباره نحوه عملکرد سیستم رتبه‌بندی خود منتشر کند، فرایندهای شفاف‌تری برای ثبت شکایت در اختیار کسب‌وکارها قرار دهد و همچنین امکان انتقال داده‌های جست‌وجوی کاربران به سرویس‌های ثالث مجاز را فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/442834" target="_blank">📅 20:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442833">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e6db6afa.mp4?token=pi5A6zW56ZMSWFWwmAFNkLlSrLM_gmq8dZWpcH3mT6x6qXD7oGCM3EuXcQNnX6C4NAfHM5S2F09lIf5gIvGudFd943leUl5P9Y70YPj8rkaCDBVgwoQ4drjhmBronFdN8Ile4qP6n0yAEeHCt3L4Ml2DPRSoN6bbTUui_kCLG2V-QBjfV8b9pG5_L-ZbFvbMpVjebBiTjgbky8ObsjvEjRQ99mMfmVAOJNKKJ3VZOVg82SwE52-dpmUei24_sElw1JwVbiBACp-qHi7JJNcJV4X46DXstVCKT5_7Z4wXLdV39NdLVUy7SoDncX7-bMut1YnxoSBAYzTvTaZUl6cbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e6db6afa.mp4?token=pi5A6zW56ZMSWFWwmAFNkLlSrLM_gmq8dZWpcH3mT6x6qXD7oGCM3EuXcQNnX6C4NAfHM5S2F09lIf5gIvGudFd943leUl5P9Y70YPj8rkaCDBVgwoQ4drjhmBronFdN8Ile4qP6n0yAEeHCt3L4Ml2DPRSoN6bbTUui_kCLG2V-QBjfV8b9pG5_L-ZbFvbMpVjebBiTjgbky8ObsjvEjRQ99mMfmVAOJNKKJ3VZOVg82SwE52-dpmUei24_sElw1JwVbiBACp-qHi7JJNcJV4X46DXstVCKT5_7Z4wXLdV39NdLVUy7SoDncX7-bMut1YnxoSBAYzTvTaZUl6cbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج [فارس] کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت:…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/442833" target="_blank">📅 20:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442832">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1c2256de.mp4?token=mNx0iYtgjrNLMrA7CBGFyoyHTRMcdUTUGdGDw5A5cw2v3ZB2FWPsEnyYJhSiP8kNjn__oHSRYrZJN0fnaF6g1jGYLl6-wclAhPu4x3vKnOwRjHePX3bY24T1OpRH5uRCpoPB8qE_SNlXfslwBaJIuOLWl5NQkW-FZq2lCd7s2I4G29RypdYL7oyP3-B3yvXGTtO7ppbLukpjjP8-cSQv6otIdrFw1dPseEKH2U0hXxj-UfiU9TdHYOhrEYyzVd3hM2ieoVRzHdG0oU5mm_hybiWD9khoQkusL0QOEGGrLHRm4Bmm8gxGTSvzjQXQlbvIbtd1fX8gFDpL1StN5du6IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1c2256de.mp4?token=mNx0iYtgjrNLMrA7CBGFyoyHTRMcdUTUGdGDw5A5cw2v3ZB2FWPsEnyYJhSiP8kNjn__oHSRYrZJN0fnaF6g1jGYLl6-wclAhPu4x3vKnOwRjHePX3bY24T1OpRH5uRCpoPB8qE_SNlXfslwBaJIuOLWl5NQkW-FZq2lCd7s2I4G29RypdYL7oyP3-B3yvXGTtO7ppbLukpjjP8-cSQv6otIdrFw1dPseEKH2U0hXxj-UfiU9TdHYOhrEYyzVd3hM2ieoVRzHdG0oU5mm_hybiWD9khoQkusL0QOEGGrLHRm4Bmm8gxGTSvzjQXQlbvIbtd1fX8gFDpL1StN5du6IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج [فارس] کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت:…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/442832" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05235cdc5c.mp4?token=FttkstVUS6y7vSCBPxzzzmzYdPKPGqcxZfYjeQu7bfo2KZGRg7ECdbqZEFq_MlR9kMaoc6i6Cx8qdbdjgr_Bl5GNwOFLQeJYR43PDyWPDmrys7dp_SmV0ct4t0WqdPo9FArtRRGm3nXxGOOIUkwzQKzCYc9izSMcfjqHL7IL8boUEn800o4FlNSt5MOtKk3LT8Aetpy7R4e8LTBmWtKRU2C0F1ziCs8tv-VzISuaxct7myzhh4TvyI27sLRFdYBm8pK3eLP2mvjPmmVw9jmnrF8qYF1Uub-9jCpP-rq0hKysQ_kyENLH13ikb6c92WBGch4LUzumG7n50ZdWKKlltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05235cdc5c.mp4?token=FttkstVUS6y7vSCBPxzzzmzYdPKPGqcxZfYjeQu7bfo2KZGRg7ECdbqZEFq_MlR9kMaoc6i6Cx8qdbdjgr_Bl5GNwOFLQeJYR43PDyWPDmrys7dp_SmV0ct4t0WqdPo9FArtRRGm3nXxGOOIUkwzQKzCYc9izSMcfjqHL7IL8boUEn800o4FlNSt5MOtKk3LT8Aetpy7R4e8LTBmWtKRU2C0F1ziCs8tv-VzISuaxct7myzhh4TvyI27sLRFdYBm8pK3eLP2mvjPmmVw9jmnrF8qYF1Uub-9jCpP-rq0hKysQ_kyENLH13ikb6c92WBGch4LUzumG7n50ZdWKKlltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج [فارس] کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت:…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/442831" target="_blank">📅 20:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442830">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8915264142.mp4?token=CbzwvKihfoxbX_kEOzixHZ-X-AwiF5tVB0z4ax9RjDCyUU-qtJ9ijyImF7sQSWQsHPlJOOR1kfd2aN-dxo4Ts8_5DKq0I0Jd3TPMuZ1mc9Z_P7Thp41oa7zf69TA_T53o-al_gegSVndqX2T4NRsWbjbgkOvJiw8BGPalRwu4zLqVcK4UggFsJd0s0DJ-uB4ThSXl0prUxmCpj0vOXUG-YM3ylmQbmUlaD_q-wy92m8wF0nA-kxQfLPEsrhmsUp4hmJZKU1RLtCGJyGe9LpZU0zzSmYMU5Rsu9AM1oLQE33o2uOkWlXweVVLGlNXdit3sHI51ySsVasF2QuysIKXIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8915264142.mp4?token=CbzwvKihfoxbX_kEOzixHZ-X-AwiF5tVB0z4ax9RjDCyUU-qtJ9ijyImF7sQSWQsHPlJOOR1kfd2aN-dxo4Ts8_5DKq0I0Jd3TPMuZ1mc9Z_P7Thp41oa7zf69TA_T53o-al_gegSVndqX2T4NRsWbjbgkOvJiw8BGPalRwu4zLqVcK4UggFsJd0s0DJ-uB4ThSXl0prUxmCpj0vOXUG-YM3ylmQbmUlaD_q-wy92m8wF0nA-kxQfLPEsrhmsUp4hmJZKU1RLtCGJyGe9LpZU0zzSmYMU5Rsu9AM1oLQE33o2uOkWlXweVVLGlNXdit3sHI51ySsVasF2QuysIKXIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: پل B1 ایران، معادل پل جرج واشنگتن بود و ما بمبارانش کردیم
🔹
مردم از من می‌خواهند که پل‌ها را بمباران کنم. چرا بمباران نکنم؟ من پیش از این هم چنین کاری کرده‌ام؛ چون می‌دانید، آن‌ها زیر یکی از وعده‌های خود زدند و من بزرگ‌ترین پل آن‌ها را بمباران کردم.…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/442830" target="_blank">📅 20:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442829">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4a2d661.mp4?token=C0lkHnJha9Yt28yaw02j83cDm0uoNKFF46hvfH-Bi51xPReBXof3r8m2XODoHVKN-hTZHxwIZWTwIpjLo-cxzNk-CtaOHeXLa_EBzfmeSxxFzF-ahUwEDdOGQT7uS_9kKhZN3mQ2fcWCZasox3lRInoTvYhlOEGjA8QKlFJTQL0arHkCKLngRYbzdVgDpbhr9qUqKwNjjiB4rfUI5W4oEXavkNTGMIaT2h8lZpFJGtzZfrvoz5Q_ce8UtwlcNTHCrLUMq-B9OoHAJPiSMIcPAPhx9aiaUceiY7l3J27IVLQTS1AfqIkUlCmMRHXWE6P0Njc44SYm-qmLsoNTW_WOAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4a2d661.mp4?token=C0lkHnJha9Yt28yaw02j83cDm0uoNKFF46hvfH-Bi51xPReBXof3r8m2XODoHVKN-hTZHxwIZWTwIpjLo-cxzNk-CtaOHeXLa_EBzfmeSxxFzF-ahUwEDdOGQT7uS_9kKhZN3mQ2fcWCZasox3lRInoTvYhlOEGjA8QKlFJTQL0arHkCKLngRYbzdVgDpbhr9qUqKwNjjiB4rfUI5W4oEXavkNTGMIaT2h8lZpFJGtzZfrvoz5Q_ce8UtwlcNTHCrLUMq-B9OoHAJPiSMIcPAPhx9aiaUceiY7l3J27IVLQTS1AfqIkUlCmMRHXWE6P0Njc44SYm-qmLsoNTW_WOAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: با نتانیاهو اختلاف‌نظر کوچکی بر سر لبنان داریم
🔹
او مرد خوبی است و گاهی کمی هیجان‌زده می‌شود. من می‌گویم: «بی‌بی، می‌توانی کمی نرم‌تر برخورد کنی؛ نیازی نیست هربار که فردی از حزب‌الله وارد ساختمانی می‌شود، آن ساختمان را با خاک یکسان کنی.» @Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/442829" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442828">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b66ebd12a.mp4?token=vErD-Gzp7CNmVe7QYF_oi280080KrjCg7YP-n6tP0NPdX6vyUO3G3uQPAEpSMXQbzEZjHsXMnbxr5NVf04Hi8uEmjotxWucNHaNrw2dt3RY2x1S8BEskmpBsRhuHwN7BFp4CeCPyvwHKEZQr0KcTonZOj58FrIgSkSf5DiDxDWIamZzUdykE5c0GhXgi_HqdpGumNUZ4m3cGIKqhVcfVC26fLg3bqsCaV3BjpUHivl2Rc79h-F2CAwBeDBvcx2Sq_10wChzZ9W3hgemfWj_z0lpX61cw7rqYS6URQlk40OlddhU1B7e0NosxX4d4ARhG1hd-mpvrqYwYd1rXy-RYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b66ebd12a.mp4?token=vErD-Gzp7CNmVe7QYF_oi280080KrjCg7YP-n6tP0NPdX6vyUO3G3uQPAEpSMXQbzEZjHsXMnbxr5NVf04Hi8uEmjotxWucNHaNrw2dt3RY2x1S8BEskmpBsRhuHwN7BFp4CeCPyvwHKEZQr0KcTonZOj58FrIgSkSf5DiDxDWIamZzUdykE5c0GhXgi_HqdpGumNUZ4m3cGIKqhVcfVC26fLg3bqsCaV3BjpUHivl2Rc79h-F2CAwBeDBvcx2Sq_10wChzZ9W3hgemfWj_z0lpX61cw7rqYS6URQlk40OlddhU1B7e0NosxX4d4ARhG1hd-mpvrqYwYd1rXy-RYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: با ایران فقط تفاهم‌نامه داریم و اگر موضوع ظرف ۶۰ روز به سرانجام نرسد، ایرادی ندارد؛ ما دوباره به بمباران برمی‌گردیم.
🔹
آن‌ها توافق کرده‌اند که سلاح هسته‌ای نسازند و شما این موضوع را به وضوح در متن توافق‌نامه خواهید دید. @Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/442828" target="_blank">📅 20:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442827">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d944cd88.mp4?token=FZxFpFosyo2W83eowXRh8TrIiEGF6GfzPnqjTJi2VcT908i4TSzyFaWmnZ-vQQDHceCMByHqxgnaUWtsrsGku1-yrQEDFOEOM_lXkNe7gL6zfxIqRtVf9zDSgdo-nA9wB4TguoPVVw1UzjTbgakO4ZHWtkiu9pW6yE7FNkyefZOQ-jDaHwzDY1au348G7gl6t4g8r_RQVTEIgA6lTTO7ze2Ltd5VHki3IfrhTYK4YiH6Smq2d6JzxHtZynoMpDhRSfJuNEkY7kOMbx6FiE4BMv3D4vi8OG3C7EWupHiF0tE-HgPAsx2x2KFnOJ_10hOQ2OBA74ME0VbzKeZtCzFk7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d944cd88.mp4?token=FZxFpFosyo2W83eowXRh8TrIiEGF6GfzPnqjTJi2VcT908i4TSzyFaWmnZ-vQQDHceCMByHqxgnaUWtsrsGku1-yrQEDFOEOM_lXkNe7gL6zfxIqRtVf9zDSgdo-nA9wB4TguoPVVw1UzjTbgakO4ZHWtkiu9pW6yE7FNkyefZOQ-jDaHwzDY1au348G7gl6t4g8r_RQVTEIgA6lTTO7ze2Ltd5VHki3IfrhTYK4YiH6Smq2d6JzxHtZynoMpDhRSfJuNEkY7kOMbx6FiE4BMv3D4vi8OG3C7EWupHiF0tE-HgPAsx2x2KFnOJ_10hOQ2OBA74ME0VbzKeZtCzFk7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی متفاوت از حضور خانوادهٔ شهدای میناب در حرم امام علی (ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/442827" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442826">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77331e7d9f.mp4?token=jGSBTgAyWZmxOz5IdsOx3FTAS0V4IV_6Woo6p44iPsi7VNUMtpOt-KsTzPsat414vYphOxBAi8Lp2jFSWjI5uuWoVbajrBqEb4u5Ubey8sV1gBvWt-S24OLIezdCSEeKgzAmmn99pxcpaANBGBw9wMwrFzagKzpye2eJ-MTKPKZsteCFg92oCDgc14Lh1QVw3KK6gv2rFCTTLyCt7zCdO9Tv2cuHqU3jx6jT7nKpFW8kbgYrkN-_rWbEaAMbwXrOqGNn0ihr_e5VIR3BmttcKc8dFcERIoUNyXvu8K0HOx67D0FtNZY2cgz9g0FoW18zCoYEIPvOWJA2pgC-VxTJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77331e7d9f.mp4?token=jGSBTgAyWZmxOz5IdsOx3FTAS0V4IV_6Woo6p44iPsi7VNUMtpOt-KsTzPsat414vYphOxBAi8Lp2jFSWjI5uuWoVbajrBqEb4u5Ubey8sV1gBvWt-S24OLIezdCSEeKgzAmmn99pxcpaANBGBw9wMwrFzagKzpye2eJ-MTKPKZsteCFg92oCDgc14Lh1QVw3KK6gv2rFCTTLyCt7zCdO9Tv2cuHqU3jx6jT7nKpFW8kbgYrkN-_rWbEaAMbwXrOqGNn0ihr_e5VIR3BmttcKc8dFcERIoUNyXvu8K0HOx67D0FtNZY2cgz9g0FoW18zCoYEIPvOWJA2pgC-VxTJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما فردی به‌نام سلیمانی را از میان برداشتیم. فکر می‌کنید اگر او زنده بود، اتفاقات فعلی [برای ایران] رخ می‌داد؟
🔹
او یک نابغه بود. مردم این را فراموش می‌کنند. من در دورهٔ اول ریاست‌جمهوری‌ام سلیمانی را از میان برداشتم. بدون آن کار، احتمالاً ما در موقعیت…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/442826" target="_blank">📅 19:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442824">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc2d4a638.mp4?token=PuB0rX9s7U-iSTb6X5wU0n9KuunKNM9XVNPbM_G8VpeysqWjuOX5qru2ghbd-q0tv-6wTGWntWiMRpzFd7s_RVflngM23UX7wedTitB-ZAwMsyeQXYjmPeCLiOjfUMk-Z2MqqAi4DxHtu_7Rga40ALzilqc54M3oMcRvzDCobxIlLg68VEBsgNvzJhNEN_SsCpnhA7XUZMqgZ_Kcu1Jr29Mn84zvFc6rZPT3ULmD8-NQHeb1fN7lRbFFztpp57uZ-S_ajmbW1-ZRA_o2yT8z-AsAFpQJQ9NTxkDaOt2VK3aIbDXJ0SmQ9IhGLRpNQuKVMQGNsO8NTBc9sPpT40UKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc2d4a638.mp4?token=PuB0rX9s7U-iSTb6X5wU0n9KuunKNM9XVNPbM_G8VpeysqWjuOX5qru2ghbd-q0tv-6wTGWntWiMRpzFd7s_RVflngM23UX7wedTitB-ZAwMsyeQXYjmPeCLiOjfUMk-Z2MqqAi4DxHtu_7Rga40ALzilqc54M3oMcRvzDCobxIlLg68VEBsgNvzJhNEN_SsCpnhA7XUZMqgZ_Kcu1Jr29Mn84zvFc6rZPT3ULmD8-NQHeb1fN7lRbFFztpp57uZ-S_ajmbW1-ZRA_o2yT8z-AsAFpQJQ9NTxkDaOt2VK3aIbDXJ0SmQ9IhGLRpNQuKVMQGNsO8NTBc9sPpT40UKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما فردی به‌نام سلیمانی را از میان برداشتیم. فکر می‌کنید اگر او زنده بود، اتفاقات فعلی [برای ایران] رخ می‌داد؟
🔹
او یک نابغه بود. مردم این را فراموش می‌کنند. من در دورهٔ اول ریاست‌جمهوری‌ام سلیمانی را از میان برداشتم. بدون آن کار، احتمالاً ما در موقعیت…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/442824" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442823">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d7e262eaf.mp4?token=vedgw3Sljm5YHhMKoF7R7gsGQdqFPwYC9bECELLvDkXQppOGuPCaQ-Evwxe6dl-9G52y3MmxlAMztFIGT4DAEKYFiwOif8EQRFRX1T7gUmhme62ZGShLGl7WCZ-sZucQ9yLiRg14g2xCdQ62HIZo1OE_GhvadAISfm2OoXzkSKl1R3iuT8uV2mki8GdmNtkRGST3uL-ZXmjNvomk9cjmuHxn12virW5rOm1BVY2AHHTgkWmf0I4ig83FV-POs22RR6mRryFJs-lFbruOlzlYLn9lsf3yjBYM7zIpXMHElbZiHM61Pn8Y7bjR1Ls2rY_k8fhMowDtjOtQZDvsLTFCV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d7e262eaf.mp4?token=vedgw3Sljm5YHhMKoF7R7gsGQdqFPwYC9bECELLvDkXQppOGuPCaQ-Evwxe6dl-9G52y3MmxlAMztFIGT4DAEKYFiwOif8EQRFRX1T7gUmhme62ZGShLGl7WCZ-sZucQ9yLiRg14g2xCdQ62HIZo1OE_GhvadAISfm2OoXzkSKl1R3iuT8uV2mki8GdmNtkRGST3uL-ZXmjNvomk9cjmuHxn12virW5rOm1BVY2AHHTgkWmf0I4ig83FV-POs22RR6mRryFJs-lFbruOlzlYLn9lsf3yjBYM7zIpXMHElbZiHM61Pn8Y7bjR1Ls2rY_k8fhMowDtjOtQZDvsLTFCV4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: رابطۀ ایران با چین رابطه یک مشتری یا همتای تجاری نیست بلکه به معنای واقعی کلمه باید شریک باشیم
🔹
نمایندۀ ویژۀ ایران در امور چین: در هر ائتلاف منطقه‌ای که شکل بگیرد، ایران و چین حضور خواهند داشت و من با قدرت در این مسیر حرکت می‌کنم.
🔹
ما صرفاً یک…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/442823" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442822">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دبیرکل حزب‌الله: پیروزی ایران موازنۀ قدرت منطقه را تغییر می‌دهد
🔹
نباید ابعاد جنگی علیه ایران را دست‌کم گرفت؛ زیرا هدف آن نابودی نظام ایران و پایان دادن به زندگی عزتمندانه و مستقل مردم این کشور بود، اما این هدف محقق نشد و روند تحولات تغییر کرد.
🔹
دبیرکل حزب‌الله…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/442822" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
