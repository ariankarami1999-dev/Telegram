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
<img src="https://cdn4.telesco.pe/file/gu3ReaQ210xuXWBZ65JMG5L_UroZ2TFDjTLLnKhhmpiPvIhQz-KbFtg36yWhT6mkFSxKdrLsQysiXaINAukkcVmuhMdkuTIGWMg4DXwYAuhrT8lgaE2EW1i4aPcvCz069Cz9w8Er5h95hzvrpKHazTEM_Nq9dr3LsPT2sGDdlu2yEh7iHzZnw-fzY7Mc6PGJ7kVAAqsFcZjQB0fr3h9j74Fg0zycHqcC_Rbc8dRjOTjmP2l7ZZolDMiS5D8EO1Sjo6ut57EDT1MTN2_inl0vCiBGwEGLul-VwqoHtNuaFSoVUWnRUhGnTIHxEQAFw09rmGywmnLweQXLUI3MpC37jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 952K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 05:34:28</div>
<hr>

<div class="tg-post" id="msg-124659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDmTBRPi2sP7DjShBZOmrWE2EtSwfCD03OUa6QCR5QA77dlygGwzrB7h10DtfDjvk8vp6_Pevp7rNvg4VRrNiZqKLUVCh4HJ55x_Byd8cpo7nb3zHkkW_nnbf3wfzOSWhchTnuVNXz5sDZVRea9Ann7UcAYW-3NQ2XZT9KUccbXG_b36p-KXy9aXATPSPmBiWlOgOKCL2sLH1Kh2hvnB6JN020b7JPn4_C1ifdwBf0ncQB3VH8liAxSEQRuGkAoN6F1NyYE6jVCPqhbJiVUypm8SLQsHmgt50b-IJLJDPH4YaZSzyC9kCKsyCfhlfodEMzkIGvPcha0awvWcfzefUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124659" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رسانه‌های عربی می‌گویند که حملات موشکی و پهپادی به محل استقرار نظامیان آمریکایی در کویت و بحرین ادامه داشته و آژیرهای هشدار قطع نمی‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/124658" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/655265e96e.mp4?token=h-MYqbHpe333H7g9k1IhvLis6azSvSHgauirgqLb_E-kGz6I6tOMfcx1L0to8g-mC_j4uYABS-UIGOvcoLmm9ZdO33VAc22sPqiO3gbT0Nc_yD6Frh1mJBN_8f814a5aLg76m09I6YXxIV90edyZvJroaTILum2knfznp1m3OU5c83n1IJazgLoQvfdlcp8tciB1pAgoSpJzlcT1DcGHfPL8p2KpcnIa71kROigpHsecAwJAT8Kax4OCRsoprKVfQJQO3AOgYw1zUBMlTTFAH5DBpH78qvZ_3x9s1dzXJa8uTemKYHYUoOtqPXrEw6MD5QY2vLBpdRtkbzOn8GYWkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/655265e96e.mp4?token=h-MYqbHpe333H7g9k1IhvLis6azSvSHgauirgqLb_E-kGz6I6tOMfcx1L0to8g-mC_j4uYABS-UIGOvcoLmm9ZdO33VAc22sPqiO3gbT0Nc_yD6Frh1mJBN_8f814a5aLg76m09I6YXxIV90edyZvJroaTILum2knfznp1m3OU5c83n1IJazgLoQvfdlcp8tciB1pAgoSpJzlcT1DcGHfPL8p2KpcnIa71kROigpHsecAwJAT8Kax4OCRsoprKVfQJQO3AOgYw1zUBMlTTFAH5DBpH78qvZ_3x9s1dzXJa8uTemKYHYUoOtqPXrEw6MD5QY2vLBpdRtkbzOn8GYWkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدای پهپادهای شاهد-۱۳۶ در آسمان بحرین شنیده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/124657" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
جت های اسرائیلی بر فراز بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124656" target="_blank">📅 02:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارش از حملات متداوم سپاه به بحرین؛ کویت و کردستان عراق ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/124655" target="_blank">📅 02:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
تاکنون ۸ انفجار در بحرین گزارش شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/124654" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
آژیر هشدای موشکی در بحرین مجدد به صدا درآمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/124653" target="_blank">📅 02:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfa8aff350.mp4?token=e76Ytlqgiv7oX1Lr8fNhKrcrR9jvQ9SciQD4aKCDAWjuUNUXQqdjfiwAqIiIPhIvMfGzh7p8h4draUFZUOfXKluVhzEYXkP5QdWPQ3uV7jUT4afiYIMpgNrtoGwJpMP05MRLTg0jSVLmVg1VqW9CK3NqKLXPysoMhcyjmBG-AwpAvK3CD0PQq8QFWu1ig_JdaDEDl9jrAPvULzCclA4bHmkaa3RTSs52yG3TdjK2vdioQLLaMIo66TRs418rUqGxtR7puqy3jIGWwBYCup6yl9NW5Su4cSKDxahYaMCU0KIbM3sRBZwtH_HzcO_aMY1U29nHO_OmX40sK4jLsgj7_J_eNN6Vku8t99eeQPqf1YXk1RRSZOWyhhEU-1vCQPAcS2FEZU5r_leMuJ55HDkYTlwnXAh6pDYdESoAuAzcJNm0ebl48GSCb8YmpR24RCyXQWEpe7LL5ifxmnT65MlW2JyKjcQ6qy0cMLpx5fO_nd2gt83VyyguPtKJrknAyT_Llt-NCVuTQRMic5-K77NJLV8MUat91xQz5-mAXXNEx2g_VmeG5HbiNDNEja0EIv2IBYxhfBjdLObBt21LDjJIPTHttT1mSHvpbRYLVp9Xe0Hma_1wjYmu34ioFDdHup6HlJ-tbsl3wG83oArthCRin4loVy2kPTI06znBkjaR004" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfa8aff350.mp4?token=e76Ytlqgiv7oX1Lr8fNhKrcrR9jvQ9SciQD4aKCDAWjuUNUXQqdjfiwAqIiIPhIvMfGzh7p8h4draUFZUOfXKluVhzEYXkP5QdWPQ3uV7jUT4afiYIMpgNrtoGwJpMP05MRLTg0jSVLmVg1VqW9CK3NqKLXPysoMhcyjmBG-AwpAvK3CD0PQq8QFWu1ig_JdaDEDl9jrAPvULzCclA4bHmkaa3RTSs52yG3TdjK2vdioQLLaMIo66TRs418rUqGxtR7puqy3jIGWwBYCup6yl9NW5Su4cSKDxahYaMCU0KIbM3sRBZwtH_HzcO_aMY1U29nHO_OmX40sK4jLsgj7_J_eNN6Vku8t99eeQPqf1YXk1RRSZOWyhhEU-1vCQPAcS2FEZU5r_leMuJ55HDkYTlwnXAh6pDYdESoAuAzcJNm0ebl48GSCb8YmpR24RCyXQWEpe7LL5ifxmnT65MlW2JyKjcQ6qy0cMLpx5fO_nd2gt83VyyguPtKJrknAyT_Llt-NCVuTQRMic5-K77NJLV8MUat91xQz5-mAXXNEx2g_VmeG5HbiNDNEja0EIv2IBYxhfBjdLObBt21LDjJIPTHttT1mSHvpbRYLVp9Xe0Hma_1wjYmu34ioFDdHup6HlJ-tbsl3wG83oArthCRin4loVy2kPTI06znBkjaR004" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله به بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/124652" target="_blank">📅 02:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بیانیه صادر شده از سوی فرماندهی سپاه پاسداران انقلاب اسلامی:
🔴
بسم الله الرحمن الرحیم
﴿قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ﴾
(خداوند بزرگ و بلندمرتبه راست گفته است)
ای فرزندان آزاد امت اسلامی و مردم مقاوم و سربلند ایران:
🔴
در پاسخ به گستاخی و تجاوز آشکاری که نیروهای تروریستی آمریکایی با هدف قرار دادن حاکمیت ملی جمهوری اسلامی ایران در جزیره عزیز "قشم" مرتکب شدند، نیروی هوافضای سپاه پاسداران انقلاب اسلامی، به فضل خدا و یاری او و وفاداری به عهد خود در حفاظت از خاک وطن، با حملات دقیق و متمرکز موشکی، پایگاه‌های نظامی اشغالگران آمریکایی در کشور کویت را هدف قرار داد که منجر به نابودی موفقیت‌آمیز اهداف و شعله‌ور شدن آتش در دژهای متجاوزان شد.
🔴
سپاه پاسداران انقلاب اسلامی ضمن اعلام این پاسخ اولیه برای ضربه زدن دو برابر، هشدار شدیداللحن و قاطعانه‌ای به دولت آمریکا و رأس استکبار جهانی و هر کسی که اجازه استفاده از خاک یا آسمان خود را برای آغاز تجاوز علیه ایران می‌دهد، می‌دهد:
🔴
هر حماقت جدید، تجاوز دیگر یا حرکتی که حتی یک وجب از مرزها و حاکمیت ما را لمس کند، با پاسخی لرزه‌انگیز، خردکننده و قاطع مواجه خواهد شد که از قواعد و مرزهای معمول فراتر خواهد رفت و نیروهای شجاع ما در تبدیل تمام مقرهای متجاوزان و منافعشان در منطقه به خاکستر تردید نخواهند کرد.
🔴
زمان "بزن و فرار کن" به پایان رسیده است و نیروهای ستمگر باید عواقب وخیم نادانی و ماجراجویی‌های بی‌محاسبه خود را بپذیرند.
﴿وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِ اللَّهِ الْعَزِيزِ الْحَكِيمِ﴾
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/124651" target="_blank">📅 02:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
این نخستین تشدید تنش بزرگ از سوی ایران از زمان آتش‌بس است که به‌طور هم‌زمان سه کشور مختلف را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/124650" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/868e61e684.mp4?token=ru27l1WTVWR1BXDQe6D4061m_tYUSV6lbMeyKDz9rBH6kdNLOh_iMcYWZ-_uTKiTiwx_fC6WQq0ejhZ-FlW4QBbi565IRqAVeI9sYLcLKRzSvlBIoVMACTh3T2KCEPpByp8SBEpNwv699CHzK9gqG2inwWtSNqLKSMiVKggzMt4qYrW20MFkcStJw-wOJ9ML1pR1UcYwYSEw6AbHajHY2pUEciKcbmldbOf_9OHWw2l8p1r2p0gTBs2xwXSRU_DTKXJ23lQ1SUHneG5hc3cPFyxxdmktKc1FBDDvieJljIpT_PcattlCKikF5TrDuXQ_Fjg9V8w8jRmzr19Wcioj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/868e61e684.mp4?token=ru27l1WTVWR1BXDQe6D4061m_tYUSV6lbMeyKDz9rBH6kdNLOh_iMcYWZ-_uTKiTiwx_fC6WQq0ejhZ-FlW4QBbi565IRqAVeI9sYLcLKRzSvlBIoVMACTh3T2KCEPpByp8SBEpNwv699CHzK9gqG2inwWtSNqLKSMiVKggzMt4qYrW20MFkcStJw-wOJ9ML1pR1UcYwYSEw6AbHajHY2pUEciKcbmldbOf_9OHWw2l8p1r2p0gTBs2xwXSRU_DTKXJ23lQ1SUHneG5hc3cPFyxxdmktKc1FBDDvieJljIpT_PcattlCKikF5TrDuXQ_Fjg9V8w8jRmzr19Wcioj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان
بحرین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/124649" target="_blank">📅 02:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
حمله موشکی ایران از استان بوشهر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/124648" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سامانه‌های پدافند هوایی در بحرین فعال شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/124647" target="_blank">📅 02:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شلیک موشک به سمت پایگاه‌ آمریکا در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/124646" target="_blank">📅 02:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124645">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KH8zgpqxC99kJ-QRi-8krZJo3J3DfEOmm0-w86CGpB75D1Ifwb_L4PDidXLUTab2989XELssAC33MoBW09ZCWiV4w5Jjc-QPeerK3xKew6zoLthcjWkIh9EWOT8_K2lzZrkTI1mVFV4wLWoEihmPiVY-TYaQZZQo9K1N2P33ZG1EZkDmC9X2OB9t__zhEpqAMu7ylWFym3gBs4mmh213BY7DYhhJNc8DTk-IkznM01XDjDr5Eng4JUkHaO7lqwiDB1xOTpERfdBRFoDs42EomKmFep0a_hyGj4PEaBLxCAE4S0mSWP6MAKVvRM-7fEg1w4Jpeu4UHsQUFsZ8b3YImg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/124645" target="_blank">📅 02:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
تا این لحظه حداقل پنج موشک به سمت کویت شلیک شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/124644" target="_blank">📅 02:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124643">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مهر: یک پرتابه به ساحل ایران برخورد کرد
خبرگزاری مهر گزارش داد یک پرتابه در محدوده ساحلی بین شهر سوزا و روستای ماسان برخورد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/124643" target="_blank">📅 02:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سه انفجار دیگر در کویت گزارش شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/124642" target="_blank">📅 02:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124641">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d3ab2f07.mp4?token=FFFwSbpWUdgjpQ2CFmzu1zNeomRS1Sn6-_IgI_2dDVQoX2v2W5TU7yK1g4wo57qU0NJ6xSSEz1GNH5I_obAIhks3wCGzhATKmy1QHis4pSU1FF2V99mVzbl9FsxMc5_f23hG1HJkVE7t8ydzY20usZMYmcMa3GQGkzNfi9Yvlivr9FnvxGE7lXBCqiiM8fWFRxkyGK80jai1PWc7JHV9Wzrc8BOslI8BuImJVd9kM8MDWQJKpkC_kU0CUhXekxq-LOYL4RdtUIzS4sQXSuRC1IxNNB7SIfxU-fpWWgTE0vWaz_drajPel35WJFqDAEt4rGqatCPW5b-IGMI-dvaXWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d3ab2f07.mp4?token=FFFwSbpWUdgjpQ2CFmzu1zNeomRS1Sn6-_IgI_2dDVQoX2v2W5TU7yK1g4wo57qU0NJ6xSSEz1GNH5I_obAIhks3wCGzhATKmy1QHis4pSU1FF2V99mVzbl9FsxMc5_f23hG1HJkVE7t8ydzY20usZMYmcMa3GQGkzNfi9Yvlivr9FnvxGE7lXBCqiiM8fWFRxkyGK80jai1PWc7JHV9Wzrc8BOslI8BuImJVd9kM8MDWQJKpkC_kU0CUhXekxq-LOYL4RdtUIzS4sQXSuRC1IxNNB7SIfxU-fpWWgTE0vWaz_drajPel35WJFqDAEt4rGqatCPW5b-IGMI-dvaXWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه راننده کویتی از ترس صدای موشک رفت تو بلوار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/124641" target="_blank">📅 02:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124640">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">💢
فووووووووووووووری/همین الان چند جنگنده آمریکایی در مرز ایران درحال پرواز هستن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/124640" target="_blank">📅 02:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124639">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آژیرهای هشدار در کویت بار دیگر فعال شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/124639" target="_blank">📅 02:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اسرائیل هیوم:
سپاه پاسداران به صورت مداوم در حال شلیک پهپاد و موشک به سمت اهدافی در اربیل و کویت است و تاکنون شلیک ۲۰ پرتابه تایید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124637" target="_blank">📅 02:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArnLiLICV4MKJad95HAHx5OwiivRMdw2yo_TC7pjpDUTjyFYeu3Tci5RiTcxDB_Cjglq1fgSQT3aRNt2BsOu6TXLgGm9keFZ6mzP5FpqLnt5n_tm8cuqdkL2VOYX07wi1kMxrwINRbgUzrOEqivTqeknUiRg4JmqPlUN096p0vuampEBf6vBRCDyD-WuNLdHdyCxTrrndrMapLh6JqREYdMDCUVcK3QdxvTXnqLfMMIfGHDA5zKHeiOQW5dcP7WpuKBw1Z2n0X7oPNF8RMR0sZ__cG8PiTXDh5rYSmxkTXOU1JugKL-pVivA3dOCcJ40JhgwI1YhFoUyJIwYs0BrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما صدای انفجار در قشم را تایید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/124636" target="_blank">📅 02:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f746e9b10b.mp4?token=SaN9nx3uLDp1KkLPPgKm6l_wlCcmGLeZrW3zoNCesMdS893lm_uKZ0t9z4ZqNiPKBBPc7Ha5OAkOhP1Ji_r9XYmRv7nNc0kZwUfWpJZh0xi6HpvJQ5meY0VbaO0lpmvCQdw5uelfvUbjWP2Hpfyg7clU0Tikx78FYVVZdPEZ6P94VRUcmQpeYFfRqV6tudKYujQCKoRASiWeow2a1XaDIp_grfl5BN14hBkGqQCKDoeB2cBjdkkPcgNy2jHlaJxU9Hb8B82oFYMwcnAJJqalTKcGE4CCTG17Ew6JWsTqv0oNEefHqWacPANfbfHBNqodl6tjTvonwrNfkOw0vdfZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f746e9b10b.mp4?token=SaN9nx3uLDp1KkLPPgKm6l_wlCcmGLeZrW3zoNCesMdS893lm_uKZ0t9z4ZqNiPKBBPc7Ha5OAkOhP1Ji_r9XYmRv7nNc0kZwUfWpJZh0xi6HpvJQ5meY0VbaO0lpmvCQdw5uelfvUbjWP2Hpfyg7clU0Tikx78FYVVZdPEZ6P94VRUcmQpeYFfRqV6tudKYujQCKoRASiWeow2a1XaDIp_grfl5BN14hBkGqQCKDoeB2cBjdkkPcgNy2jHlaJxU9Hb8B82oFYMwcnAJJqalTKcGE4CCTG17Ew6JWsTqv0oNEefHqWacPANfbfHBNqodl6tjTvonwrNfkOw0vdfZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از تکه‌های موشک‌های رهگیر که تو کویت افتاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124635" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/124634" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پرواز جنگنده های نسل ششم f4 فانتوم ارتش برفراز اهواز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/124632" target="_blank">📅 01:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ec38fee8.mp4?token=iNn0tgTi-c7X_OKaI2KEoTbZ3JubGf80qNN9itHjJZfK97F9gUB0RgJtHtictT4FJztTcE9YE5L8bzfO7Mnp7I3DkfgbMYf7XGkHszX_nD_JXiICq5dxidl9p5QILeixM8WR3BZz7MFW7P5YnPePdtRzhqK5fMuscZCszcOHj0y8aAZji8fi35S_WxeZ7oQM6nbw8r_TxDLWvGpUmzgpBvl23jt927aUc4uezGHlFhvg58I_UZ2kVfaQRjgzIbpSycOMLa8pzhDol1yDlxHijZjD-JL-SwUqTbqeQwyMCzSaZ-xtjJd4E7XSsmvzK8W-czMPV1ODU7F3z6XhAGWRsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ec38fee8.mp4?token=iNn0tgTi-c7X_OKaI2KEoTbZ3JubGf80qNN9itHjJZfK97F9gUB0RgJtHtictT4FJztTcE9YE5L8bzfO7Mnp7I3DkfgbMYf7XGkHszX_nD_JXiICq5dxidl9p5QILeixM8WR3BZz7MFW7P5YnPePdtRzhqK5fMuscZCszcOHj0y8aAZji8fi35S_WxeZ7oQM6nbw8r_TxDLWvGpUmzgpBvl23jt927aUc4uezGHlFhvg58I_UZ2kVfaQRjgzIbpSycOMLa8pzhDol1yDlxHijZjD-JL-SwUqTbqeQwyMCzSaZ-xtjJd4E7XSsmvzK8W-czMPV1ODU7F3z6XhAGWRsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان کویت لحظاتی قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/124631" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⌛️</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/124629" target="_blank">📅 01:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ادعای وب‌سایت عبری حدشوت بتخون:
🔴
نیروهای آمریکایی چندین موشک از خاک کویت به سمت جزیره قشم در ایران شلیک کردند و سپاه پاسداران ایران بلافاصله به مبدا آتش حمله کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/124628" target="_blank">📅 01:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شاهدان عینی از کویت:
🔴
خونه ما سمت سفارت امريكا هست سفارت امريكا هم داشت موشك میخورد صداي انفجار خيلي بلندي بود.
🔴
انفجار های سنگین در منطقه سورا کویت با چشم قابل رویت بود.
🔴
همين الان اژير كويت فعال شد دوباره
٦ تا انفجار خيلي سنگين تا الان
توي اين ٣ ماه اينقد صداش سنگين نبود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124627" target="_blank">📅 01:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6773c885.mp4?token=RGXoGcciO4Cc_8sfnmNqfl9MB5M748ElTea9gq5nnd5NLMt0s_wYbZoi4XVCV-9owcK8Fk5LS37BZhSXLZS5HevGcqMvz2fL6cdA_0l6-E_HoEtn9aSkY1u6hvzHcwwzqHHna7-WDMlf7NRgMFiMsb025hxmHw6wPbedLmjmBNMxIZv3drERR9pn-cWKbTiv7SpEH7HZJjZjoFP2hbo57q4KiYW9hX4L8Oep7b6QKg05SbD5GoaxQWij_sw_L9eiEyDa0ENcgyt2E7fOxuTTIaq0BLLcZXV3YK_I7U2DkX7ci1d8fHL2zVVwlY17DYpXujexr2N-sP2W9Rbe2eCj7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6773c885.mp4?token=RGXoGcciO4Cc_8sfnmNqfl9MB5M748ElTea9gq5nnd5NLMt0s_wYbZoi4XVCV-9owcK8Fk5LS37BZhSXLZS5HevGcqMvz2fL6cdA_0l6-E_HoEtn9aSkY1u6hvzHcwwzqHHna7-WDMlf7NRgMFiMsb025hxmHw6wPbedLmjmBNMxIZv3drERR9pn-cWKbTiv7SpEH7HZJjZjoFP2hbo57q4KiYW9hX4L8Oep7b6QKg05SbD5GoaxQWij_sw_L9eiEyDa0ENcgyt2E7fOxuTTIaq0BLLcZXV3YK_I7U2DkX7ci1d8fHL2zVVwlY17DYpXujexr2N-sP2W9Rbe2eCj7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کویت لحظاتی قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/alonews/124626" target="_blank">📅 01:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124625">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارش العربیه: ایران در یک حمله واحد، هم پایگاه هوایی علی السالم و هم کمپ عریفجان را هدف قرار داد
🔴
ایالات متحده و ایران در روزهای اخیر حملات کوچک مقیاسی را در جزیره قشم و کویت رد و بدل کرده‌اند، اما این حمله بزرگ‌تر بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/124625" target="_blank">📅 01:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124624">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پایگاه عریفجان در جنوب کویت، نیز هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/124624" target="_blank">📅 01:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5101dc61.mp4?token=O54FuY8frFYjehMtWygIFkVPSDwLOmI2x_mYUg0__-14msDdx_cKnMtholal8Q3T8PTA-4Ka-lEh6pDonU5SBZQwQf13BbswoeCDRZbS3B9q7CSLIj3Z0xGtKKwdDHTN9OrxmVJwAsr852al4YBYXvrjG7KCCm_cigQyY9NHdQ9p9_J5Kt9BM0glAWXmWawp_qiTkfqtTcQaVUwhip_UV8mMBIwq2w9tGur4H6syXp5tsuUkGgSti3nV1un8lw-e85eQfcBnihEhIARu7qiYblI7OhZDI1wkXdgW318T6PDjpXxccX-bDoXUmQcwJuMaVyr4J3aSJRJmKWO1Ds7zhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5101dc61.mp4?token=O54FuY8frFYjehMtWygIFkVPSDwLOmI2x_mYUg0__-14msDdx_cKnMtholal8Q3T8PTA-4Ka-lEh6pDonU5SBZQwQf13BbswoeCDRZbS3B9q7CSLIj3Z0xGtKKwdDHTN9OrxmVJwAsr852al4YBYXvrjG7KCCm_cigQyY9NHdQ9p9_J5Kt9BM0glAWXmWawp_qiTkfqtTcQaVUwhip_UV8mMBIwq2w9tGur4H6syXp5tsuUkGgSti3nV1un8lw-e85eQfcBnihEhIARu7qiYblI7OhZDI1wkXdgW318T6PDjpXxccX-bDoXUmQcwJuMaVyr4J3aSJRJmKWO1Ds7zhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوئی از انفجار تو کویت، و فعالیت پدافند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/124622" target="_blank">📅 01:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdtjT9r3jdia20IqAH42NljY9fvc3I4ZAsoRO5rieSo2gBYoYW047LZvYfPV9D7IciilcgH3_kZ8G4a8nTDRjIIAIZfZ_t107unZPVPIt1058jJu5nezcWv749MVjP3WYSJUX7rfxLtI5AuHicclvT9J8deltPHPGtLNPgOZKWIrsBsasF_On4ZlrG66bh50AwYL-qhRcNhE6EJvm_E833i_NEufDHhB9aZtk26or924K7rcAyGumSE3Ugh6hZ2Aj6ngCb_qNN7WYsJ39DZuA96ANyH1pjqmiRIELgu-gvgb-hkdt91ZCXC6ZYATnGIMqk1uMmwrGK1m12Saz2jcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رد شلیک موشک در آسمان شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/124621" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/موشک‌های بالستیک ایران پایگاه هوایی علی‌السالم تو کویت رو زدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/124620" target="_blank">📅 01:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrrdgTPLl6WPnFsFaoDRjhJGHkPvOyetNLDSZ_76CG0dQJmcBKeHc47iauIiP9wt2VZLV5vqmfNJ8sRVuFlY9A6xmQAEUYUdDsDxZ0x83WN3F_L8dLIKcwq5Qx3UQNNe9QIdYMHgVTn5KOZVfbpMpFQwKu_hInVwTXAG4fnB1dIpFVuVkEAA2qF7BgBCbLGEhzznHtI5_6BNgRvTW8U8AufoFdwI7fzK881KU0K0bXnmPHGclToYwyx8ErAsRemuYZeD8wcyyvHTYVGHBQpjmAtB-eaDqOZCL4szEkbG5kbdhXFG-c-n4ZUmsfa3SM7wLxBtqBu09MuiPtc1updq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع کویت :
- پدافند هوایی کویت در حال حاضر داره با حملات موشکی و پهپادیِ دشمن مقابله می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/124619" target="_blank">📅 01:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124618">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
آژیر هشدار و صدای انفجار در کویت
🔴
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/124618" target="_blank">📅 01:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124617">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔴
بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.
🔴
پیگیری‌ها برای کسب اطلاع از ماهیت دقیق این انفجار ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/alonews/124617" target="_blank">📅 01:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124616">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de528efdc.mp4?token=ICsEoFnVFPmb03QZ_6M--bL85O0coU4-sd4wnk8WURtQeOYKNnSi6QFA2lEl2rxz_afV2FGEe7uCbHaLOU6OodVNwGX_bsz3U8ypYpIGcYMZTqhCUPNC0J3dUE5stXdOCeSscezp7nPd-SJ4BpE3x30Wno_cJaSV6oVqerJNs7lp72v-jonehhA4g7IYLJEOH_Epa629tBkEkUgK5v4YS6ciH-CJdD7SWApt22xV_673eCvXsTaBafILwuhsclFNv9JqfUbChTm5O3z0r3Kq4aGwj8JyJhaxSh2-xbBgF-aH2Y7Tuq1CnvS1VzowUldZ0sKgBD5YfoLzJFiNTfLQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de528efdc.mp4?token=ICsEoFnVFPmb03QZ_6M--bL85O0coU4-sd4wnk8WURtQeOYKNnSi6QFA2lEl2rxz_afV2FGEe7uCbHaLOU6OodVNwGX_bsz3U8ypYpIGcYMZTqhCUPNC0J3dUE5stXdOCeSscezp7nPd-SJ4BpE3x30Wno_cJaSV6oVqerJNs7lp72v-jonehhA4g7IYLJEOH_Epa629tBkEkUgK5v4YS6ciH-CJdD7SWApt22xV_673eCvXsTaBafILwuhsclFNv9JqfUbChTm5O3z0r3Kq4aGwj8JyJhaxSh2-xbBgF-aH2Y7Tuq1CnvS1VzowUldZ0sKgBD5YfoLzJFiNTfLQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
امروز نیروهای آمریکایی یک نفتکش بدون بار را که در تلاش برای حرکت به سمت یک بندر ایرانی در خلیج فارس بود، از کار انداختند
🔴
فرماندهی مرکزی ایالات متحده (centcom) اقدامات محاصره‌ای را علیه نفتکش m/t lexie با پرچم بوتسوانا که در حال عبور از آب‌های بین‌المللی به سمت جزیره خارگ بود، اعمال کرد.
🔴
خدمه کشتی هشدارهای مکرر را نادیده گرفتند و چندین بار در طول ۲۴ ساعت از تبعیت از دستورات نیروهای آمریکایی خودداری کردند.
🔴
در نهایت یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/124616" target="_blank">📅 01:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124615">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8t-iZarvpv3H1pEmyTiVbSw0vchfMmnFefKfGSS8cabvEAMG0QcuBl4TlOd6UfCBkQBncrN-pKH7UiD5IzOg5e9czSvdaddm1v9EOsy05usTO-DX5dCVBB3HrNuhpxoz5QOXDwVeoiyh_Ll6jQOVyArBYBL1nuvRGfkY-jf0_DtPW-aKxOVgpF76bM53eBOwLtB5tx6OErlTj0Epv2qyTJJG21ndd6a4Yvwetzp0eU3lROi5rH1w2bxA5L94FdKNrm6ONfYtq7n24s97TToxNphoWE9bq7q48PzAL7E2zxWmWbiRS4xA9kbu4fVQovXlzby7sIP2XtgkkuEzQ8QBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران دومین تیم پیر جام جهانی شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/124615" target="_blank">📅 01:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb87b1576.mp4?token=oGwHzbCPd631nejIMtkg7z4Z65flHZjZrTET_gAN5ozkLo6bHsOK5oKj1_opRcxnDbw0C14EUJ2UC7DXXIDpmNEyoNTeXgPjf9oUHi676CXqIx0JB7FFgkszTlUqv804fXt4QnaA2d2lbVqDHlfKlXxZO92Jyd6IbK5g5WcWU6c-ynaFiQWXnftK7XQHoXXJqIETask654Mg6M2N-JCafuwSec6KxyTRaSKJw7kjf0vFiMorv_3msfBuD60xaqztjUWy0mADZNdnPp0sPGrLEjCIjzOFj8TNgtZ35wG-AIbL4sFFvgnOs29dtBwNU0phHVolBBV0AsstYjVPme2r7BW824ozky4Qbe1bNJjWVXrS7B1PlRdifXz2N8KFW3ZoiyROTyc0oAZab_8RJqpyxjBfuNIF5RXNYOvbU2PCvZLZ9XzuEp-pTCjvGWE48Wjj-b0sW8lMVU60iFz8omvADpnNjjyKKGHikCiv5fyHVfoS2icDsQjHmao9wFpMmLkGuNWkElcFDpTWK47jlR7gAvdW4WnRK8Z4gLqxO_Jzr2CBK3ESN9XZSRQHl4-4arNmzT2VO1YqmK82k6HlrEVGKnXkE5rtcG-jjhc_9L7V_k5Bkc24SVaWjoEmFf50oSrKQpFG9eZkjXtbG7dyRL_BLt5Bdl3WZteu3_-CkiHro4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb87b1576.mp4?token=oGwHzbCPd631nejIMtkg7z4Z65flHZjZrTET_gAN5ozkLo6bHsOK5oKj1_opRcxnDbw0C14EUJ2UC7DXXIDpmNEyoNTeXgPjf9oUHi676CXqIx0JB7FFgkszTlUqv804fXt4QnaA2d2lbVqDHlfKlXxZO92Jyd6IbK5g5WcWU6c-ynaFiQWXnftK7XQHoXXJqIETask654Mg6M2N-JCafuwSec6KxyTRaSKJw7kjf0vFiMorv_3msfBuD60xaqztjUWy0mADZNdnPp0sPGrLEjCIjzOFj8TNgtZ35wG-AIbL4sFFvgnOs29dtBwNU0phHVolBBV0AsstYjVPme2r7BW824ozky4Qbe1bNJjWVXrS7B1PlRdifXz2N8KFW3ZoiyROTyc0oAZab_8RJqpyxjBfuNIF5RXNYOvbU2PCvZLZ9XzuEp-pTCjvGWE48Wjj-b0sW8lMVU60iFz8omvADpnNjjyKKGHikCiv5fyHVfoS2icDsQjHmao9wFpMmLkGuNWkElcFDpTWK47jlR7gAvdW4WnRK8Z4gLqxO_Jzr2CBK3ESN9XZSRQHl4-4arNmzT2VO1YqmK82k6HlrEVGKnXkE5rtcG-jjhc_9L7V_k5Bkc24SVaWjoEmFf50oSrKQpFG9eZkjXtbG7dyRL_BLt5Bdl3WZteu3_-CkiHro4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا پادشاه بریتانیا اسلام رو میراث بریتانیا میدونه؟
جواب رو از آرش اعلایی بشنویم.
🔴
نقش برادران شرلی در پیدایش و رسمی شدن مذهب شیعه در ایران.
🤔
آخوند انگلیسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/alonews/124614" target="_blank">📅 01:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124613">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مقر گروهک‌های تجزیه‌طلب کرد هدف قرار گرفت
🔴
منابع عراقی از انفجار در یک مقر گروهک‌های کرد تجزیه‌طلب در شمال اربیل خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/alonews/124613" target="_blank">📅 01:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQlpLsCDgBs1nmtUmYLH1bW9HXCMPvZPf8hCjlegLsDL-C52IZvYtxYmZaC_MkItNBn86mJVztrW3pVXUujrESjG-8GHde8Rtoi5d3llB8dab-grvT-OuKbKon1bt7VfeMzKKfaobhylOnok30GerYl3ShMcdH5AKu5AL8ymfh8TBQzLT8u7vwTTeYWP8tE7vyICiw0Dl7wzrywfmfwQt8E7cT8xLhVuhlj7777GUpIjMMrVeZz8jADMEO27UI6dyNTi-nxAVTJHe7E9Kt4mp7H1-lB05ygoYUpsPo8vRlMkc8UbAGhzGYBPs-ds4RhpMYhFEV7pSKk0rXXmn1_DMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد ماهواره هایی که شرکت های مختلف جهان در فضا دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/124612" target="_blank">📅 00:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ادعای رسانه بریتانیایی امواج:
یک منبع ارشد سیاسی گفت که هیچ گونه قطعی در ارتباط ایران با آمریکا از طریق واسطه‌ها صورت نگرفته است.
🔴
همزمان، قطر در کنار سایر واسطه‌های منطقه‌ای، به طور فشرده در پشت صحنه کار می‌کند تا از شعله‌ور شدن دوباره جنگ بر سر لبنان جلوگیری کند.
🔴
منابع آگاه عرب و ایرانی گفته‌اند که یکی از نزدیکان نبیه بری، رئیس پارلمان لبنان، به همین منظور در دوحه به سر می‌برد.
🔴
نخست‌وزیر قطر نیز امروز با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، دیدار کرد.
🔴
این تحرکات در مسیرهای موازی اما به هم پیوسته نشان می‌دهد که ممکن است در آستانه یک تحول مهم قرار داشته باشیم.
🔴
با این حال، آنچه بیش از هر اعلامیه‌ای اهمیت خواهد داشت، اجرا و عمل به توافقات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/124611" target="_blank">📅 00:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124610">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=ikbFpJc5Ro3neyelKaVD_Snjwy305MrtzgjkeZmfv9FVm7mSlz01wBJEIRObnIF_Klzo2aC2DL8Bzoq2OOMUEgQ7vUdvXdBJzRKrA_jz9QVHFd5kmQuajmDEN0SYwEhSMr4klqgGdo-BvaHb4hZFor-DT6nDws64mb7QzTKhydxVnfdQ7fYXyyx_9P9wP9bjIag6IKwuHWBcioYwlnhVoYeq0TLwNpEhMp1bbsfIRW8-EpKc-CBSGIaFrFm5kZPTE3zzwgPclAlip1R8ztc8rw42n-DuBMwCsuHLAqhjwxSgdPnakb4yflumc4jw_ubRxlveb29Mw-YmfQ6V5_ppQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=ikbFpJc5Ro3neyelKaVD_Snjwy305MrtzgjkeZmfv9FVm7mSlz01wBJEIRObnIF_Klzo2aC2DL8Bzoq2OOMUEgQ7vUdvXdBJzRKrA_jz9QVHFd5kmQuajmDEN0SYwEhSMr4klqgGdo-BvaHb4hZFor-DT6nDws64mb7QzTKhydxVnfdQ7fYXyyx_9P9wP9bjIag6IKwuHWBcioYwlnhVoYeq0TLwNpEhMp1bbsfIRW8-EpKc-CBSGIaFrFm5kZPTE3zzwgPclAlip1R8ztc8rw42n-DuBMwCsuHLAqhjwxSgdPnakb4yflumc4jw_ubRxlveb29Mw-YmfQ6V5_ppQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا به یک کشتی دیگر شلیک کرد.
🔴
بیانه سنتکام : تامپا، فلوریدا — نیروهای آمریکا [امروز] ۲ ژوئن یک نفتکش بدون بار را که قصد داشت به سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/alonews/124610" target="_blank">📅 00:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124609">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
توماس میسی نماینده کنگره: فقط کافی است کمک‌های خارجی به اسرائیل را به مدت یک ماه قطع کنید، آن وقت آنها بمباران همسایگانشان را متوقف می‌کنند - صلح فوری برقرار می‌شود، تنگه هرمز باز می‌شود، و قیمت بنزین در هر گالن دو دلار پایین می‌آید. اسرائیل بزرگترین دریافت‌کننده کمک‌های مالی از جیب مالیات‌دهندگان آمریکایی بوده و همچنان هم هست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/124609" target="_blank">📅 00:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124608">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b65xi_UwdTOgZfd7K4Jf6Ob4H3pycymK4ND-vtKziodR18i75D__lwiYlx14-4Wn2WHSoumti9Mbk5I7sGBbaLxH47yJmH60GaXfyHyUCG7zNsdjK_5hQYUYzl2bvyGo7GCgiZ57pkVcxrWfO9TaZzJh1DPhnSY5y7RcqgT76aYj1MqJOBp1er9TfdVuZUF2dSGgBcop-0EF7XrDM_llIO1pin72Hl6mOFkGZ6NkSoXnCS_O5NSWzjm5FTvDdtwVPj_lYLudm7kyWJzKSyAR7Nwz1MPDM0BUvnENi-5gbqG_oWUq7gB7_ba54JFI6345bPGX0BIua4MtS37apqLONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری‌ابیانه: نتانیاهو فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد!
🔴
علت جنگ آمریکا علیه ایران این است که نتانیاهو علیه ترامپ آتو دارد و فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد و نتانیاهو این را اهرم فشار علیه ترامپ قرار داده تا هر کاری اسرائیل می‌خواهد، آمریکا انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/124608" target="_blank">📅 00:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124607">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : تیم مذاکره کننده با قدرت ایستاده تا آمریکا به خواسته هایش نرسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/124607" target="_blank">📅 00:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124606">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r93Pp1rHO0Pdo2NmgV1jXH8nTylESfjQlLjtxeNQGfdn0frbOxPDgzf_qeZL-c8_AyAiKSsMRGld_8TkJL9m9cHv_L3GM-HJWGZAhi0qeNs3TpyGQPEnz4PuumNxT44zMfEhiw0z6vqFSBvvAdFiB5KUu4J5RDLeDKTZN8DPuAxI94l1-gTImdrDEPXZON2Dkw0rnNaDEjjx3lACoYKI9watnOruWYTCFKxg0QMUnkgxC4FfRGEmUEhwnNAnXU0e_cypaFWg2lHF5oF1Q-7Tv6qjWEzxjeWCRb5zsomMNeMFwhLKTpE-KEAuQuNQ56IlFhbO0KXhdRQ0STT1MRfqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/124606" target="_blank">📅 00:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124605">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
الحدث: وزارت خزانه‌داری آمریکا اعلام کرد واشنگتن تحریم‌های جدیدی مرتبط با ایران را وضع کرده است که افراد و پلتفرم‌های تبادل ارز دیجیتال را هدف قرار می‌دهد.
✅
@AloNews
خبر</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/124605" target="_blank">📅 00:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124604">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رکورد تورم در ایران از زمان جنگ جهانی دوم تاکنون شکسته شد.
🔴
بر اساس داده‌های بانک مرکزی، نرخ تورم نقطه‌به‌نقطه در اردیبهشت ۱۴۰۵ به ۷۷.۲ درصد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124604" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124603">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHuGkvh33nqmG5tKBDT4kRfgez2oye91NUTi3YQUBPnKlw6kVn9kCOCmf1a5jp8ijiqM1PmGw8MMY2w4HSqty6oRS7Ifh7hJFeUXbeNNXywsTCNe6rfdW_Tiiux5cWlaG-i_d9seB444byZ3UaYVxx784LOVPlH39ArmJGveIeXDCS8frqSnsP-3woWJUAfKwRC-TkNPuY3l9LgEwlq2oZFGlmG9KOihQU9bn4mmNPpLXoxP8kE-V7xjMmf2Pl0vDOEQcILGBG5KDHo9tYxrBjduTE_AeIBOFfWWUBdc6uIiPyQTlAZIvU_LCoDXWEukwmvsC7xJi1O5rW4OTm89OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بررسی ورود سرمایه‌گذاری خصوصی به بخش برق ونزوئلا در مجلس ملی
🔴
مجلس ملی ونزوئلا قرار است اصلاحاتی را مورد بحث و بررسی قرار دهد که در صورت تصویب، مسیر را برای ورود سرمایه‌گذاری خصوصی به بخش برق این کشور هموار می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/124603" target="_blank">📅 23:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124602">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
العربی الجدید: مذاکرات لبنان و اسرائیل در واشنگتن به پایان رسید و قرار است فردا ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/124602" target="_blank">📅 23:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124601">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ریزش 2 هزار تومانی تتر در پی خبر تحریم نوبیتکس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/124601" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124600">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a44b2aef3.mp4?token=NESBo-exC6naaufoYpw_EByKNWaAB9V_CDKSI12oTyHxnGzF0cwgEwONpJgQqV0XaxjWAE-NDwXueyCkDeMKSM8i5VGcnFHYQgfd6RPQ8wyTtyscKjGhlFrushBxpl6YbnXiLWhqvHGqf2lZGfeuBo769W08aIugEA1F-fYFwJpJzukHukNKSjDPG5g4kIJm_N829SJ_EHqPEHPW8H1qzCBA-wo05-k2NX1gOfYcdJLdj_UcfOhLxftM_x3IbtEVz3Hu1yF1q7eYy7bhd2lVxcaAp26jR-7UrTUGFwK9bm4ZsVLkJ8obj-GBaBG3pUHe8STXBdq14T-2_kqTUDA8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a44b2aef3.mp4?token=NESBo-exC6naaufoYpw_EByKNWaAB9V_CDKSI12oTyHxnGzF0cwgEwONpJgQqV0XaxjWAE-NDwXueyCkDeMKSM8i5VGcnFHYQgfd6RPQ8wyTtyscKjGhlFrushBxpl6YbnXiLWhqvHGqf2lZGfeuBo769W08aIugEA1F-fYFwJpJzukHukNKSjDPG5g4kIJm_N829SJ_EHqPEHPW8H1qzCBA-wo05-k2NX1gOfYcdJLdj_UcfOhLxftM_x3IbtEVz3Hu1yF1q7eYy7bhd2lVxcaAp26jR-7UrTUGFwK9bm4ZsVLkJ8obj-GBaBG3pUHe8STXBdq14T-2_kqTUDA8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : تیم مذاکره کننده با قدرت ایستاده تا آمریکا به خواسته هایش نرسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/124600" target="_blank">📅 23:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124599">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فیلترشکن گیگی
8️⃣
هزار تومان
😂
❌
فیلترشکن گیگی 20 تومان دیگه نخر
کف قیمت فیلترشکن
👇
3️⃣
0️⃣
💿
2️⃣
8️⃣
5️⃣
💸
5️⃣
0️⃣
💿
4️⃣
5️⃣
0️⃣
💸
7️⃣
0️⃣
💿
5️⃣
9️⃣
5️⃣
💸
1️⃣
0️⃣
0️⃣
💿
8️⃣
0️⃣
0️⃣
💸
برای خرید پیام بدین
👇
🔤
@MrTh_Vpn
🔤
@MrTh_Vpn
🔤
@MrTh_Vpn</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/124599" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124598">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
میدل ایست آی: مالک برجسته کشتی‌های یونانی حاضر به پرداخت عوارض عبور از تنگه هرمز به ایران است
🔴
غول کشتیرانی یونان و مالک بیش از ۱۵۰ فروند کشتی: این عوارض می‌تواند «خسارات» وارد شده به ایران در اثر جنگ آمریکا و اسرائیل را جبران کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/124598" target="_blank">📅 23:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124597">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941e46de05.mp4?token=ajufrXcLXMwn9mMGyVw6vCVXWXj4-8mAAy10PnebiUg48LBOW95VKwI02kd_nalilAWxPVOw1EdGgeys-8vLIEdvO026LDGLtywp9ZqSjMGaJk0DM2JRp2CYE9tfKxh669c2MwuLuLM4E0o_Hf0BdKJK9czb_d5npsG0c8F1WK8LqwvrZPZKWVEfETdW5Lz7oV3xzel_o6g2F7B7idKMWri1gBbn7F8MW_exgtI2AxuLqB1UsAts3ke2ngnAro_H9Q2BO_7ZZVQRsNBnK703JSjzM7KAkqIug4rMjoGAeybiNlipgHk1wFgNA1LPpMiBJNImFKUJGvBR54bQ80QH7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941e46de05.mp4?token=ajufrXcLXMwn9mMGyVw6vCVXWXj4-8mAAy10PnebiUg48LBOW95VKwI02kd_nalilAWxPVOw1EdGgeys-8vLIEdvO026LDGLtywp9ZqSjMGaJk0DM2JRp2CYE9tfKxh669c2MwuLuLM4E0o_Hf0BdKJK9czb_d5npsG0c8F1WK8LqwvrZPZKWVEfETdW5Lz7oV3xzel_o6g2F7B7idKMWri1gBbn7F8MW_exgtI2AxuLqB1UsAts3ke2ngnAro_H9Q2BO_7ZZVQRsNBnK703JSjzM7KAkqIug4rMjoGAeybiNlipgHk1wFgNA1LPpMiBJNImFKUJGvBR54bQ80QH7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمود قیم، مداح: کوروش اگه سگِ آستان اهل بیت نیست،‌ پس خاک بر تمدن ایران باستان
‼️
🔴
پ.ن: محمود کاش اون شب بابات میرفت داروخونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/124597" target="_blank">📅 23:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124596">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvUmp0mUz4NE5cGJICEFjjKYwlotF9YRoNxPOLYZ4SDSMbZVylbkdITyDnROEDGe55A07HGshevJQ372-JY2YETHhVbsoMX6PRbmBX4OWWOa7eoLOoO7tAqB3Er21SGvfDYpqnlqQZcb2MLm9gW-Y1k3LSwqRouZieCNuKVJXov68DEHDvUOgOhFKp1xdgZCn9Yl54HNwTQJVAE2KnIu4IvCsj9E9uuGn2y4gIJEaPxYPQChPGO4gI43Ua-6QxYosBDdf4bPQ7s1RS0t7XGJOI37UR37Qo3MtrNgPP2h6HEIB-lf8mN6fgCtW_iZHEDysN9dmrnAb9_C0ZbP4RfHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تسلیحات و پیمان ابراهیم؛ پیشی گرفتن فروش سلاح اسرائیل به اعراب نسبت به آمریکا
🔴
آمارهای جدید نشان می‌دهد تحت تأثیر پیمان ابراهیم، میزان فروش تسلیحات اسرائیل به متحدان عرب خود از میزان صادرات نظامی آن به ایالات متحده فراتر رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124596" target="_blank">📅 23:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124595">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
یک سرباز ذخیره ارتش دفاعی اسرائیل (IDF) امروز صبح در جنوب لبنان توسط یک پهپاد انفجاری حزب‌الله به طور متوسط زخمی شد و سه سرباز دیگر نیز به طور سطحی آسیب دیدند، طبق گزارش ارتش دفاعی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/124595" target="_blank">📅 23:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124594">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آمریکا چهار صرافی ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس و 6 فرد مرتبط با اونا رو تحریم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/124594" target="_blank">📅 23:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124593">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
معاون قرارگاه مرکزی خاتم‌الانبیا :
اگه هیچ چیز هم نداشته باشیم، با سنگ به جنگ با آمریکا میریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/124593" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124592">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53317d490.mp4?token=H_1te19m6mWr5pz3P09HlXyJt7N83xpyUdNrB4cKp9ruGZ_RsXd2y9fXZ4qFOe-X2wi36fEMnXwY_cCFDq6c9NG-wNVJpXGTh1Zp0zCHFP1kO8DRi6euub0WZ7q-P70P2rbNk0_0WlwWNRpiQqzoWpn3ejWK2dxwGsRrSaJiUckZMDxrMo8nyQKF1p34GW9iEQTv4UlYhBV8jmuTfa0KfH-PGHztMIBNaBWPK040k5KnclgkHRl8A7Enx4NhXpvik6EWAXmKMawW5YEmvGUj2eH-OVtedDppQ1j3I4_2ZLyTWPAvzvTZk3Xy3P_i0Udd2ubHpkCH1b38CbPm1lG3vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53317d490.mp4?token=H_1te19m6mWr5pz3P09HlXyJt7N83xpyUdNrB4cKp9ruGZ_RsXd2y9fXZ4qFOe-X2wi36fEMnXwY_cCFDq6c9NG-wNVJpXGTh1Zp0zCHFP1kO8DRi6euub0WZ7q-P70P2rbNk0_0WlwWNRpiQqzoWpn3ejWK2dxwGsRrSaJiUckZMDxrMo8nyQKF1p34GW9iEQTv4UlYhBV8jmuTfa0KfH-PGHztMIBNaBWPK040k5KnclgkHRl8A7Enx4NhXpvik6EWAXmKMawW5YEmvGUj2eH-OVtedDppQ1j3I4_2ZLyTWPAvzvTZk3Xy3P_i0Udd2ubHpkCH1b38CbPm1lG3vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز شبانه جنگنده‌های ارتش روی کرج، استان البرز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/124592" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124591">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
طبق گزارشات منتشر شده،مصرف دخانیات تو دخترای ۱۳ تا ۱۵ ساله ایران نسبت به سال ۱۳۹۵ حدود ۱۳۵ درصد افزایش پیدا کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/124591" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مدارک_مالیاتی_موسسه_محسن_سازگارا_۲۰۰۶_تا_۲۰۲۴_.pdf</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/alonews/124588" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@AloNews</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/124588" target="_blank">📅 23:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
در تاریخ ۹ خرداد ۱۴۰۵ (۳۰ می ۲۰۲۶)، محسن سازگارا در اتاق «طرح نو» کلاب‌هاوس حضور داشت. او در پاسخ به یک نقد بی‌پرده، مطالب و ادعاهایی را مطرح کرد. او در صحبت‌هایش صراحتاً ادعا کرد که در تمام طول عمرش، از هیچ فرد، سازمان یا دولتی فاند دریافت نکرده است.
🔴
اما با بررسی هایی که در رسمی‌ترین اسناد مالیاتی ثبت‌شده در ایالات متحده، واقعیت دیگری را نشان می‌دهد که با این ادعای کلاب‌هاوسی در تضاد است:
بر اساس فرم اظهارنامه مالیاتی ۹۹۰ مربوط به «موسسه تحقیقاتی ایران معاصر» (موسسه‌ای که سازگارا خود از سال ۲۰۰۶ رئیس و امضاکننده قانونی آن است)، این سازمان در سال ۲۰۲۴ مبلغ ۲۰۰,۰۰۰ دلار فاند مستقیم از دولت آمریکا دریافت کرده است.
🔴
طبق اطلاعات درج‌شده در صفحه ۹، بخش ۸، خط 1e این سند، این مبلغ ۲۰۰ هزار دلاری به طور رسمی و قانونی تحت عنوان «فاند دولتی» ثبت شده است.
🔴
این سند رسمی که تحت جریمه شهادت دروغ به مراجع قانونی آمریکا تحویل داده شده، ثابت می‌کند که موسسه و فعالیت‌های محسن سازگارابه طور مستقیم از فاند دولتی تأمین مالی شده است. این پست با مرور اسناد رسمی، نقض آشکار ادعای اخیر او در کلاب‌هاوس را اثبات می‌کند.
🤔
محسن سازگار تاسیس کننده سپاه پاسداران و از همراهان اصلی خمینی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124587" target="_blank">📅 23:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
تحریم‌های جدید آمریکا علیه ایران
🔴
وزارت خزانه‌داری آمریکا روز سه‌شنبه اعلام کرد که تحریم‌های جدیدی علیه ایران اعمال کرده است.
🔴
طبق بیانیه دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک)، چهار فرد و چهار نهاد مرتبط با ایران، به فهرست تحریمی آمریکا افزوده شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124586" target="_blank">📅 23:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گزارشاتی از فعالیت جنگنده های ارتش بر فراز کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/124585" target="_blank">📅 23:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh8FVKXAXUqaPPqVJveQ8BKDZuCOHe-IsSmtsf4MnLo_aoAkuvbAW1p1qkwLB4lkKtnVgvkZj1a-S99KBewaDbGErcQAP4cacWByVXrD7Tru23cBtzrob7v0_d9Kdz3JFIKLLFBG92F8wE1p9BBQ2jsPT8esNQEAOQObc-HoL9lGXjwaece4aUtER0KFJnkW4zbrYLSJMikSX0_9ju4jN8iX5E2VEz1jQAPi2HzASa85f8msTNPNG4tGqFnwVILJfxziHBmx8Y8KQMjO89bMKvCvy9k8zHMgE2FYeEzvIVWZeQwRuHFocEpxeQVZDrt1fmennqSxOcOuv8iG-7C6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پائین کانال نمایش داده میشه توسط تلگرامه و دست ما نیست و  کلاهبرداری هست و فریب نخورید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/124584" target="_blank">📅 23:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/124583" target="_blank">📅 23:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c91c418d.mp4?token=BwaEsOBnnIQZFAnNZq9d9GqLOThPnhjbUaBPaIOZaEI0rp9OaFC0g2FzSISi77b3MOhjy_QZ3GDHfY1ssaeCYMMyZj3mINzdh9XTybZDcF0emKpCDRdiGDhu6mPz9zl2F9aVp6BS7d3R4G7BUcz3ludfmuMvSNuzXKuVtFnIqg8mL_N-yqFFtbq7nSEGDeoqm9lTK2-uL60BT3vI3qVl3b9QJvdgXMaYJ3BrRYtBlVs8vxYkcNxlQcoqT9MhAHcIbD89kRN8ejdLTYmVXyVxE7HVPNTExGPc4xuAQX2U748AD84abUPkecR7C3c7ZIrV6aIRhIwRy1z35tcXsUO3eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c91c418d.mp4?token=BwaEsOBnnIQZFAnNZq9d9GqLOThPnhjbUaBPaIOZaEI0rp9OaFC0g2FzSISi77b3MOhjy_QZ3GDHfY1ssaeCYMMyZj3mINzdh9XTybZDcF0emKpCDRdiGDhu6mPz9zl2F9aVp6BS7d3R4G7BUcz3ludfmuMvSNuzXKuVtFnIqg8mL_N-yqFFtbq7nSEGDeoqm9lTK2-uL60BT3vI3qVl3b9QJvdgXMaYJ3BrRYtBlVs8vxYkcNxlQcoqT9MhAHcIbD89kRN8ejdLTYmVXyVxE7HVPNTExGPc4xuAQX2U748AD84abUPkecR7C3c7ZIrV6aIRhIwRy1z35tcXsUO3eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: بگذارید بگویم ونزوئلا امروز آن جایی نیست که ما برای مردم ونزوئلا آرزو داریم.
🔴
اما در مسیری قرار دارد که فکر می‌کنم اگر ادامه یابد، بسیار مثبت است و باید ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/alonews/124582" target="_blank">📅 23:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
بانک مرکزی اروپا اعلام کرده است که طلا جایگزین اوراق قرضه خزانه‌داری آمریکا به عنوان برترین دارایی ذخیره‌ای جهان شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/124581" target="_blank">📅 23:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
الجزیره: ترامپ ترمز نتانیاهو را کشید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/alonews/124580" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
هم اکنون پرواز گسترده پهپاد های اسرائیلی بر فراز بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124579" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7472ed86c9.mp4?token=J8Proaoay-2GMSpeE6_mryo29NbPEdW9Ies-SmTiEgJfxPFwXRBUSr4JPo9JUL3mPAEVvBvuifmIIi8Y7-cNWwcT-MEGCUTWcZJt4J08thX8oAGmWP2DVtB4mKr7L_Dt1RWetKyXR0TSM4Bf-j-lqCdYTFxmT0yqZhVTgjj_I_JvwCmJkxGqCrd-Vkr3ElEY9U2vfsRHC7ZI88Yk2VO1yz0ZnQ63IPe4WR-UWD5hYd89cx4pO8q7rWWvWjf5Kpe_oex9ZMrch7Tx7uxIqeFPp-iLiDV4uHtihxzQ6LHt4mmnjvR0TSN-vSisu6U5oqJolMJs2V9DK0w8hTWWspv2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7472ed86c9.mp4?token=J8Proaoay-2GMSpeE6_mryo29NbPEdW9Ies-SmTiEgJfxPFwXRBUSr4JPo9JUL3mPAEVvBvuifmIIi8Y7-cNWwcT-MEGCUTWcZJt4J08thX8oAGmWP2DVtB4mKr7L_Dt1RWetKyXR0TSM4Bf-j-lqCdYTFxmT0yqZhVTgjj_I_JvwCmJkxGqCrd-Vkr3ElEY9U2vfsRHC7ZI88Yk2VO1yz0ZnQ63IPe4WR-UWD5hYd89cx4pO8q7rWWvWjf5Kpe_oex9ZMrch7Tx7uxIqeFPp-iLiDV4uHtihxzQ6LHt4mmnjvR0TSN-vSisu6U5oqJolMJs2V9DK0w8hTWWspv2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلی اتفاقی علی جوانمردی معروف به علی تجزیه که مدعی آزادی برای مردم ایران هستن، بصورت کاملا خواسته در راستای جمهوری اسلامی که بیش از 47 ساله مردم ایران رو به گروگان گرفته صحبت میکنن.
🤔
حرام زاده های کراواتی رو بهتر بشناسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/124578" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b480a5702.mp4?token=Am6JZrTNsjLxdvJXqwqoNGuqCqCjzw0HHFKw9J2ltiXQEKRjrYHHTfKauNpr6xi9JtA_dAQGY3RtYJUZkBm3AibPqcHRrGm_yW8w9eNHJbVjyCDZbOj930ZZnLbsWWwYccPEVdItQXjrnj5Zj7AYKTIKt9V5w3DB2MuIP4RyoAzs6wr4q9IVq93Ejec3-QF7bfZINLVbUdq4FAv1i3atmhdwrqM3pbFisZXeSYMboLfK6QN4ZVJ_2Z5udt5HbpyA9QVD7TyU-yzXfn1nJJTYMme4weaKdZWgLOb9CUVMWhCLCkxP3kvvSOML8RRMiy3M4Fe8b_V50SciGYz_6hDGIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b480a5702.mp4?token=Am6JZrTNsjLxdvJXqwqoNGuqCqCjzw0HHFKw9J2ltiXQEKRjrYHHTfKauNpr6xi9JtA_dAQGY3RtYJUZkBm3AibPqcHRrGm_yW8w9eNHJbVjyCDZbOj930ZZnLbsWWwYccPEVdItQXjrnj5Zj7AYKTIKt9V5w3DB2MuIP4RyoAzs6wr4q9IVq93Ejec3-QF7bfZINLVbUdq4FAv1i3atmhdwrqM3pbFisZXeSYMboLfK6QN4ZVJ_2Z5udt5HbpyA9QVD7TyU-yzXfn1nJJTYMme4weaKdZWgLOb9CUVMWhCLCkxP3kvvSOML8RRMiy3M4Fe8b_V50SciGYz_6hDGIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو در جلسه استماع کنگره مدعی شد: اکنون ما افرادی را داریم که در آمریکا به‌جرم تلاش برای ترور محکوم شده‌اند و یک نفر هم دیروز دستگیر شد؛ از مأموران ایرانی که درحال توطئه برای ترور رهبران سیاسی، از جمله رئیس‌جمهور آمریکا بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124577" target="_blank">📅 23:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124576">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / روبیو در کنگره مدعی شد یک ایرانی دیروز به اتهام تلاش برای ترور رئیس‌جمهور آمریکا دستگیر شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/124576" target="_blank">📅 22:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124575">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا از اعمال تحریم‌های علیه ایران خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/alonews/124575" target="_blank">📅 22:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjHdVFuxu2S7EI6U6lVw9-gWMm00Jy8BHAlIsJSw55Ti-_7zworU4-KTRfUliKAyAtYzvONHfFfEGeAjkPuFU057J0eRCEx6nuU2RCKNJwhTMaMhY6_IqBpThSB4Nk6TPVRebig3gUA_yWjQCoLhHKIK3_lZW27O63OiOAzgYB6_k46ZqWY3defQlYvGiTZHQO9uhGG2WmXCUAwCJ4s8DzPYX_vUCchRyo3x0FXx20V0p8wUel7yVTTsF_LV_MOXp6j0mHScspG9qXDM2WMPokDjihdLIkB2NlE5QVkvnWybSKQxS3QvFRzSHW1e4OPhsigD0rLwZMt8LlaWIT2Hxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/alonews/124574" target="_blank">📅 22:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124573">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db5c6e8c5.mp4?token=qvtAWRCO3vIi8QdOWBr3fgd73Y9w_vHIBrqhrpcYLhJ-609NpKLU9qMq-9vnpeNqlPY9vFQZSl6iKe3gNbhHzqFDBRQZYmLTF9df4Vm9K7O6bZojSqZeZJpTIphVKjFHGlI-achUriNHBazV92EgaDv28NaxcL0V7ufNyb_NJIIwaa8F2zf03HxaeCQ5YHwsdtk-CfpTv7qBnkoxcdf-NdhF7lwHVUGibDFzmbPEnIqrTN6NOjoQBUS7vbbFlgacloP42TNvIs7E15fnWnT12MnNVv-0RXySDdZQ-d0x1BpGiLrYz23bwfDKXAEWZK-1rrnSupg40NdVA8Ht7ahx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db5c6e8c5.mp4?token=qvtAWRCO3vIi8QdOWBr3fgd73Y9w_vHIBrqhrpcYLhJ-609NpKLU9qMq-9vnpeNqlPY9vFQZSl6iKe3gNbhHzqFDBRQZYmLTF9df4Vm9K7O6bZojSqZeZJpTIphVKjFHGlI-achUriNHBazV92EgaDv28NaxcL0V7ufNyb_NJIIwaa8F2zf03HxaeCQ5YHwsdtk-CfpTv7qBnkoxcdf-NdhF7lwHVUGibDFzmbPEnIqrTN6NOjoQBUS7vbbFlgacloP42TNvIs7E15fnWnT12MnNVv-0RXySDdZQ-d0x1BpGiLrYz23bwfDKXAEWZK-1rrnSupg40NdVA8Ht7ahx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: این گروه‌های تروریستی خشونت‌طلب، مارکسیست، چپ‌گرا و رادیکال که در بسیاری از کشورها فعالیت می‌کنند، برای مثال سال‌ها کلمبیا را بی‌ثبات کرده‌اند و دیگران نیز سرمایه اولیه خود را از کوبا دریافت کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/124573" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124572">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9227ec9400.mp4?token=TKCPr7qybuaoUTL4aQEi0QcIP04UIjdjy5rDg4T2rU6p2xBPl3d7l9uknJXwbdvLZwDZCQu0N85Ey19d3knXRj226r2zEptMqsS7ACkJ6gw_-BdFSvv2TblaesJyZvEAmbRo_TiRkTxwT7kT7QigGkXx63Up4Ug5P56uXPqFXudKkDiD4LoZFWkHFtyRy0V4H_INeTraQkxrdTPJHR2YVNIAnnNz3FT55rMmZ-6tESRIrBT2LtVbfUCgSnRkpw6PeV5zHSTN67BQ_hYZhrr6M_Ab-PiYXNjcZS0I9g8UiH0QEfLqIAxG5bJPf3qrP7jyw7dxePVwX8uXhYwEGG4gxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9227ec9400.mp4?token=TKCPr7qybuaoUTL4aQEi0QcIP04UIjdjy5rDg4T2rU6p2xBPl3d7l9uknJXwbdvLZwDZCQu0N85Ey19d3knXRj226r2zEptMqsS7ACkJ6gw_-BdFSvv2TblaesJyZvEAmbRo_TiRkTxwT7kT7QigGkXx63Up4Ug5P56uXPqFXudKkDiD4LoZFWkHFtyRy0V4H_INeTraQkxrdTPJHR2YVNIAnnNz3FT55rMmZ-6tESRIrBT2LtVbfUCgSnRkpw6PeV5zHSTN67BQ_hYZhrr6M_Ab-PiYXNjcZS0I9g8UiH0QEfLqIAxG5bJPf3qrP7jyw7dxePVwX8uXhYwEGG4gxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو: ما پیشرفت‌های چشمگیری در نحوه ارائه کمک‌های خارجی آمریکا در سراسر جهان داشته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/124572" target="_blank">📅 22:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124571">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گزارش فایننشال تایمز حاکی از آن است که ایالات متحده در نظر دارد دارایی‌های هسته‌ای بیشتری را به کشورهای بیشتری از ناتو در اروپا مستقر کند.
🔴
گفته می‌شود لهستان و چند کشور بالتیک علاقه‌مند به میزبانی پایگاه‌هایی برای هواپیماهای دو منظوره‌ای هستند که قادر به حمل سلاح‌های هسته‌ای هستند.
🔴
انتظار نمی‌رود به زودی توافقی حاصل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124571" target="_blank">📅 22:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124570">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/de870dace2.mp4?token=ZSYmid2yR_cLTBqbo_Ji6jrBmTFYZfD8aqps5bzyhCR2H8XVnhJAJdBHu43u9T0EhdrDGtx27HtgEiqD05Y2I8-L_edUHj8i1HSKQfpwINK_LMBCG1VniMKx3E0S8pNdDcWw3cJysI3uYDrZ9Lltvx_zFytcX01ebJF3aD2UYtXZxEiOaGsZx3Jgpj6BAkvnbdl_G-y9X5mZTZ5PWh-R4OUUDWWsXeuXwTYYc2iz-iCHzrb_ET5ZHD0_qUbE_7wneQnMGQqBOirya9OrLXXbimjYM0ykalxBdAsWsl9Uh5GdJvxW1_REjOPCFZDkaUw_G6qOdwZ7mwIttbD3LxUEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/de870dace2.mp4?token=ZSYmid2yR_cLTBqbo_Ji6jrBmTFYZfD8aqps5bzyhCR2H8XVnhJAJdBHu43u9T0EhdrDGtx27HtgEiqD05Y2I8-L_edUHj8i1HSKQfpwINK_LMBCG1VniMKx3E0S8pNdDcWw3cJysI3uYDrZ9Lltvx_zFytcX01ebJF3aD2UYtXZxEiOaGsZx3Jgpj6BAkvnbdl_G-y9X5mZTZ5PWh-R4OUUDWWsXeuXwTYYc2iz-iCHzrb_ET5ZHD0_qUbE_7wneQnMGQqBOirya9OrLXXbimjYM0ykalxBdAsWsl9Uh5GdJvxW1_REjOPCFZDkaUw_G6qOdwZ7mwIttbD3LxUEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی سازنده جم تیوی و فیلمای ترکی پشماشون از این کلیپ ریخته:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/124570" target="_blank">📅 22:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33ad08024.mp4?token=doBonkx45Wea7SYjkuc58RtYsK2k8dj0rw_XOzKevE3PKJvmMIEuRJHb7N1mfM4aireBklWwlRSbYftjOn8ICgCVRqhli7dzNQEycKDbQ68aOEPBCmyZdohW_FjGzdiZb32SLRHNjyKzYMfuYTKa3F6XvJwKRZzKK02UAeZl48kVyS8B6ETve4ffPUdypZyZqm69spROYcGaGKKgU5boOEvuyEKhOhaXCXSJ-VF6SFJ8u9IctuwfDDgnuF09aI5mkuDJkR816mW-Fn22YeWtq-pV_bsOcy_E21tODBmtnQzVhuUXw-WCeSjaCYjLUC6ZGOBuQTPzrCKTBo4a24c3ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33ad08024.mp4?token=doBonkx45Wea7SYjkuc58RtYsK2k8dj0rw_XOzKevE3PKJvmMIEuRJHb7N1mfM4aireBklWwlRSbYftjOn8ICgCVRqhli7dzNQEycKDbQ68aOEPBCmyZdohW_FjGzdiZb32SLRHNjyKzYMfuYTKa3F6XvJwKRZzKK02UAeZl48kVyS8B6ETve4ffPUdypZyZqm69spROYcGaGKKgU5boOEvuyEKhOhaXCXSJ-VF6SFJ8u9IctuwfDDgnuF09aI5mkuDJkR816mW-Fn22YeWtq-pV_bsOcy_E21tODBmtnQzVhuUXw-WCeSjaCYjLUC6ZGOBuQTPzrCKTBo4a24c3ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در یکی دو روز گذشته کمپین «ایران ارث پدری ماست» رو همگی دیدیم.
🔴
حالا بشنوید از پادشاه بریتانیا در سال ۱۹۹۳: «اسلام میراث ماست!»
🤔
آخوند انگلیسی که میگن همینه که ما تو ایران داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/124569" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eeaf331dd.mp4?token=fk9YItFgGtf_cQKZFpY8HSCR3fKYbFSM1vBzckICpCSjnpv0uXKxKClUZZHA3tfob3xE_91H2PBbqbwOJ4De6gzfFyquPyx5mJ3bNeu9kAz2OQrkCR511L0aJXQYNF8UWFn2oGFrTeyba5j4xXoyVQ-DxH9KmB5MpDCukj5gdXqN58ZcQi8jAhHXv-lUjDAlksO5JpXnt8tke0VblCqWCx-S5DHj_i8ljp70_djFxf5QlWRYHw-waLaDO0xF_VKdOPIB-gU2hEhsfefA6XWTn0kA5JEUAwgrbKhGmyWroOwchn91PzrOB2wVg4vXO6jj2DGiwxCuKeiNDRTTNsfpyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eeaf331dd.mp4?token=fk9YItFgGtf_cQKZFpY8HSCR3fKYbFSM1vBzckICpCSjnpv0uXKxKClUZZHA3tfob3xE_91H2PBbqbwOJ4De6gzfFyquPyx5mJ3bNeu9kAz2OQrkCR511L0aJXQYNF8UWFn2oGFrTeyba5j4xXoyVQ-DxH9KmB5MpDCukj5gdXqN58ZcQi8jAhHXv-lUjDAlksO5JpXnt8tke0VblCqWCx-S5DHj_i8ljp70_djFxf5QlWRYHw-waLaDO0xF_VKdOPIB-gU2hEhsfefA6XWTn0kA5JEUAwgrbKhGmyWroOwchn91PzrOB2wVg4vXO6jj2DGiwxCuKeiNDRTTNsfpyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تئوری‌پردازی فاکس نیوز برای شروع مجدد حملات اسرائیل به لبنان با چراغ سبز ترامپ/ جک کین، ژنرال بازنشسته ارتش آمریکا: دونالد ترامپ هر دو طرف را متوقف کرده است. حداقل به یک توافق شفاهی رسیده‌ایم.
🔴
می‌دانم که اسرائیل به آن توافق پایبند خواهد ماند.
🔴
از ۱۷ آوریل به بعد شواهد زیادی داریم که نشان می‌دهد حزب‌الله چنین نخواهد کرد. و فرض من این است که اگر حزب‌الله مثل گذشته این توافق را نقض کند، رئیس‌جمهور به اسرائیل چراغ سبز نشان می‌دهد تا هر کاری برای دفاع کافی از خود و همچنین انجام عملیات تهاجمی برای از بین بردن این توانایی لازم است، انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/124568" target="_blank">📅 22:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نتانیاهو تا چند دقیقه دیگه یه جلسه امنیتی برگزار میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/124567" target="_blank">📅 22:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گروسی: به دلیل جنگ و هدف قرار گرفتن برنامه هسته‌ای ایران، ارزیابی آژانس تغییر اساسی کرده و بسیاری از فعالیت‌های هسته‌ای ایران اکنون متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/alonews/124566" target="_blank">📅 22:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124565">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrhYKEip1k1BUGWTsGfJ9nvW5KdXshBClUEIosZJk4Sxtj2p6pFUQvE6l35a3jdE6J6-PPYr8ktRWADGiAYZWDHaKtyuLnXrGFDG3WQ3Zo0FMwiWvoVEXaR5lIyWleijZKv0FGH9oQbIWFg42ltIE945SK9deOsu0Buj-29Mnz4ZjEP0E08Z8oJL7m1kVxXYiHTsfeGGg178I78gLr_88ngRGCMRkswKwLbaFqWsrtakvkeB9w4E7iguscHl5nIADrWBRkBPeTAWn9gtY1vwgqnrv79lN1urIsjUEyJ-hhi4joKfxekfVi_wy2paCMaav9AXYsyGBC2P4HlyYmC3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشت نفر کشته و ۴۲ نفر دیگر در مالی روز دوشنبه پس از برخورد یک اتوبوس با مین زمینی در جاده بین باماکو و کایس زخمی شدند، به گزارش رویترز و به نقل از یک مقام اتحادیه حمل و نقل
🔴
انفجار در منطقه‌ای رخ داد که جبهه نجات ملی برای تغییر و اصلاح (JNIM) همراه با جبهه آزادی مالی (FLA) فعالیت می‌کنند.
🔴
هیچ‌کس مسئولیت گذاشتن مین زمینی را بر عهده نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/124565" target="_blank">📅 22:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHB3ipnsPrBg1AjIk5bzMxgn1FA-oZ8zSoe2wJPnnESeQZH8LSFhA0exF0pGJZTu1YlL2dYCPpEnteLgy0WLikCPgViH1juA7p2oSjLAGplx1M7fudarwK8yzC9ol4esVMVm8lIN9I0Y06KqXlS_t3sie7YJY3uOLX6SD56G3-GFsWfdG6-HCLKlmHrbScaxW3b8gO1Cosu3ya43cDI36K82RXqbXtgL5z0s0Nhdtrsim_JtFfeC2hBMgEEe6rV0zS59iq7TDUDmCviKKCD-GNFCfuQf8OD7qgrRzHVdXGoBlYoMar_9WA61zU9t8O9H2-kOqBI87kxRQHyNcdzHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
داشتن فلاویو بولسونارو در دفتر بیضی کاخ سفید بسیار خوشایند بود — جوانی باهوش که کشورش، برزیل، را بسیار دوست دارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/alonews/124564" target="_blank">📅 22:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124563">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر امور اقتصادی و دارایی: تعیین مالیات مقطوع صفر برای بیش از ۹۰ درصد صاحبان مشاغل که در سال گذشته با موفقیت اجرا شد، امسال نیز تداوم خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124563" target="_blank">📅 22:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124562">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
روبیو: امارات و کویت در جنگ علیه ایران فعالانه و جدی با آمریکا همکاری می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/124562" target="_blank">📅 22:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdEzjdlWDZY22lGqgPk4VWRrELa2NvbO96N13g1VNQ3X4t5p6S9E0VN5JLcmFiFFrIkKYQbrKGyiG6w5ozjluV6zHdBY4gzyk3jOxX_y2z_-UEZV5hc22PRjmBB9B69sRGlVeSR89a-_TqR083PRnzVFMFrGCswrn36iof8WQ14Np0DysSfU8x6PRtgM9Us8l4JvBZqvI12EJuGKM3TZwZ-rcYBEkuS4QUtvOvqQc7dbBI6LjdlENsqcn_QU7yi9Rcs2dJP-0HC4vqZuvIeRzgtIm9Xe-ZJmBILJomaqLKhZNZ_oni1LcFYuGVff78eMiXLueYwR2Ll3iJyZ8vHzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو «یو‌اس‌اس باکسر» (USS Boxer) که مدتها قبل به منظور عملیات آبی-خاکی در ایران اعزام شده بود، علی‌رغم انتظارات به دریای جنوبی چین رفت و از منطقه دورتر شد
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/124560" target="_blank">📅 22:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/up-M2F9o3WKWKhGh2Dk7LZdV7OGY4PmxJOdu0-I5WAppSemfnfCEfZwO3Q3edeIl37ybzPTt72plnGgZ6pBIJFZdJVnMghAktEljKZd2-XWedeBnYQg3eEydwPaoJvlel7e6lGsbSzmGIJVLFodRKrWi0ZdOF0Ler_zxc9xUgoTHSjglMivm8Ebfpe3NRP9QCIyhuM_oknnQFrZaHxJ9RmVqAsHd-RGJhuqfv4ottSUpOOHIulnZD7wXFLsi7weI3gu2jpa6ibwabE54xCL9lVI-AzfrI-QkXprdwCx5ovs915P-ssSbrAVmNaNjdgfVsu0OMfk_38--O5gCBDl2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSqPun52NOc90GqkZ4R9ADVIAoaUa3HpfU5JaK2zZbA_YcpA7v1rFAfVANDKJIFfPpu4exw_esfUALBhKLW_f_GIzf6aBAh1pgdl6N36TuxfoPtG1I_8YN_XKQoQtutJb56j7RIPjeHD1LKib2_xX6CFlW_Lz51WYqsCUUEELF1ZjY2t0MCH3aqPCDcv9zs2JrsdehZQqTFJNi6XRlPxpr3yVcUbjEWqPtbwY8Gs3IpHaxOYwdZ32qvoMvlnV4dd_BElDwXjp-A5gmUfMdH_UyCshAd67p3I-LDzn2NX_EU64SEC9EmGnky1eEe8hmaEAA9z5LFFC2ECIghL2GEN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5IJspip1DiQ25nmgPHvK0nU98E_8QqLaoKfUk9n9rjbo51PHB_k2KseHcVrLGPnWsiqilAn9ndRYXgjALu-_ffpPWs37MlhDfeukAx21bpp_QxhgKZBYohTTgKDqvE3uWdC5QYI2WF2lUSDRMFztVJh5gfb4rinVgbjKBIHuh5cZcN3Tiv0eCOVxjCNCoqjO46UCIGYJvgdmjSIhqnqjPUqFtW7PRkFaR2Zn5pGjrxWLRHVgE8a_OaiChBr781IICthYgFkkVrby15-rFxySyg_h-CbgzAYOAolZFVYx7_28NI97ELLVdlpfuNgu9Co6PLTWNEJxpAJa3BFytcRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgYya8dmwNVbynCiRwgmqak-QLcGfN7emjHBfggC3yAF5Pz9rrPXRVbfIhLbOyxcQ82BoDvGXnVil-27yY9Djv0lYohc8qgDTWKLGjoJM0afSd7h-jtAzjdvA6MRIloNSCr2THzlLRp0OiPVLcYl2RZm3DRt4DYeamKsNWORAamK2vMfgOfZT204P7XXwlRRFtNh6f358A5K4ZPABTbs82e3mfwEG-CdxSqFXSsRLu6_wcOaPiVNwKCq6iH06kqERtof2SuuswCttxReekQ787Gk-4MCV6b27vyoT3s7LIEocE-4eqJnHfCkNqy8xdI82ExlYpw7FSy9Rj-HV06Pbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
🔴
تمرین همکاری منطقه‌ای ۲۶ دیروز در قلعه هریسون، مونتانا، با مراسم افتتاحیه و یک دوره موانع آغاز شد.
🔴
همکاری منطقه‌ای بزرگ‌ترین تمرین آموزشی فرماندهی مرکزی با کشورهای آسیای مرکزی و جنوبی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/124556" target="_blank">📅 22:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124553">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zi9-dRzN2YONANQK4o2XlfQUQU-_gawiozOuzJxJ1n3aCYqOTi_2OD8xpuDJWKn3nRY0KR2DHJsYJVYrKIUDNYt8kMyiu9TTok5EJMNMJJ2s7M0Vm2F5SJVNabvoZdrsw6Ifl2u0Plm3FT71IBu1N6jsWgYgt5fjIhm8F1yv9QzDUlHBYU_7C0Z1NjSn08EvYk66V_wmKv-DzMI2W2z96bK5YwJInzudW1-hxYHDYcSyeqwZejGVrc7R9PrHDEpHApuMSbI4ujGIF5_tlIMJ21v6z9PtDea86ol6z_tOj0rzNpeuuCofhX3PF7l8msVifwG5Sfr_QcGM58MvzVj1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miTlXui8kusGjDwpLwAUZMmnH9Jxfl2mDUs2UA52lr1hEmwBuRSh9doQ49F648VDC-KDnQlr1qrH-cs5mRQttz7btR_2V8c6cI-wUYtQA_Uk3Std0Dg3t-sqBl5hnjekBuamww0azc5VacnkjbbN6wp9PjzpQilEUqF2aT4aqTgB0zDBkwBOiFQpa185IAYVkU9SvZ5JTmbTZNMkEERyi4Vf1KVx-x6qcm0ofdWRuGNwcObNHNkWQZTVQ3UrApTlBxPEezPprBHD_XdMDP01mcTyjTceCGKL9hgOo68MfNbmeqhEhk3aWrRHg-LeLo_W53X00lWcujD46HbwIvQOfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823f2337f3.mp4?token=eLr4cLJ69CZYGwP_vKD1xU95t9RfW5FB3DNjdGcd92wlCtud9J7yM3jzrS8BMjd-AuWvsP0QqpZM7VtYazxDkbh6Ff9LACh3_rY2XjkPK1YCeFWf5Pqa71S6YwTTZgwVCJkjVhPWcw1CuKsk6mDaqhU7CsPLok2ygWq5_6-FJciy32tHsg_6H-KBVOWYLcxfHwC_UPAM4KbA_z_8RLT2_f2V97mLuMv7tARs6xOyi-esn1a7EGHnKKPGKaUkxl8yhlkG9Or2eBOnA4oOiQx0dNsPNb-32apRBdpqoant1nNGV9DYH7Sw_Nuz2eJZiajzRa-Zzn2hSzzVDjxQbP9SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823f2337f3.mp4?token=eLr4cLJ69CZYGwP_vKD1xU95t9RfW5FB3DNjdGcd92wlCtud9J7yM3jzrS8BMjd-AuWvsP0QqpZM7VtYazxDkbh6Ff9LACh3_rY2XjkPK1YCeFWf5Pqa71S6YwTTZgwVCJkjVhPWcw1CuKsk6mDaqhU7CsPLok2ygWq5_6-FJciy32tHsg_6H-KBVOWYLcxfHwC_UPAM4KbA_z_8RLT2_f2V97mLuMv7tARs6xOyi-esn1a7EGHnKKPGKaUkxl8yhlkG9Or2eBOnA4oOiQx0dNsPNb-32apRBdpqoant1nNGV9DYH7Sw_Nuz2eJZiajzRa-Zzn2hSzzVDjxQbP9SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
عرزشی‌ها ،عرزشی‌ها را پاره کردند!
🔴
عرزشی ها، عرزشی‌های مخالف مذاکره را کتک زدند و پلاکارد گفته خامنه‌ای را هم پاره کردند.
🔴
چند عرزشی در تجمع شبانه مشهد از لباس شخصی ها کتک خوردن و حالا قرار شده موافق و محالف در میدانهای مختلف جنع بشوند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/124553" target="_blank">📅 22:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124552">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
احتمال وقوع سیلاب در ۱۱ استان کشور
🔴
سازمان مدیریت بحران: احتمال وقوع بارش شدید، سیلاب، تگرگ و صاعقه در ۳ روز آینده در استان‌های آذربایجان شرقی، گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی، سمنان، ارتفاعات تهران، البرز و نیمه شمالی آذربایجان غربی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/124552" target="_blank">📅 22:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124551">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فرهنگستان زبان فارسی: واژه مصوب قدیمی «دوگوشی» برای هدفون دیگر کاربردی نیست؛ پیشنهادهای جدید مانند «نیوشه»، «شنوه» و «آوایار» را بررسی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/124551" target="_blank">📅 22:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124550">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/گزارش ها از درگیری شدید مرزی میان هند و پاکستان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/124550" target="_blank">📅 22:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124549">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و عربستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/124549" target="_blank">📅 21:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124548">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سخنگوی دولت : امتحانات نهایی دانش آموزان و داوطلبان آزاد ۱۳ تا ۲۳ تیرماه آغاز می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/124548" target="_blank">📅 21:56 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
