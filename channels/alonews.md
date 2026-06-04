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
<img src="https://cdn4.telesco.pe/file/vqNeqp1PZYaEGBUuN1T9TxAN61XYEYIy-kTtLZI6okA7qNo1JNbbUfZd_fRA_W8jnnYl3wTTNuuYRykZK3yREXeDmkg3xweIVurJJKnpi1ZfB__qSNnPhtONemk3xYDTX1RpSBNBuybiQaL3Rlw7vVg1fR8VWqbQP_CDCO_VL1A6suAzfT43VNego_MwYnyk4furXUFqsV4Sha6NorSA2PrTLqvKH1VnCl3WfL9r8esiTacDphK3F4fX_w6g9cByVShI5nO2-G-DKkuMf4qKNkwn8MBBchWdN9mHvjxQelhM6LLvbM2fjr9ysl1HVNnaRb_n1AjAIH5aaeqOq2PS2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 963K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-125032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=f349vRfxNl-pBZ8vOc5XrkZrpkH-uMAkqUpt2J7xa8gdVSFLfrBR74lFK10ln0U6i6CvnHIZnQLedBsK9JaZc4pShzPdSUTcQCJWuSh-jMcNCG84EDu5ATcMyWzrUovHTt-jKQWKSHOAjWCOeJQjhBT5I1ue8UY_SJxixmoh3qp3tgPMDokZ36wGKy0hzM01rycceJwlkMHxZvetp7HviEFHEQx0oDxN7k2Gn-E0Atz5QfBJDENLQ_RJLPZxPzxHZZb5HdPzP9bLkEewzyNSDZWh36Y3SNH-23y5HqYQEZrf8riXl3RFe-LJXorL0diEhS2i56kNfpSq8T81mqwUNzsP6VisQndWvzAjV1atJzW9Tbmj0WE_1MXFA38M4_PdiTgsuMOjr02lLNy0TUgsF34CeeZ8X3ctY1GsciZTOL0c4Hgv66VNP15Nyr1vufZ7acb_oQCpAhhyYOZMwzlRDrgsZ0fIiK7y9hzOv1btf9_AASbhYp6N_QAGCBt51O8ROrBEW0zUp8B6iciotqgccF_wS0TKm9CmzUJ3repO3bv9Nf35fTH98JAf-E6PgfdzC1Va7axXS5oM_sBtu-SuR9V78DHANFArMhIklo-UzfF32his7btab32Rrv2CP9PpW4ACaTtHnWcxDt2m96l6lz_3quWyS7L8ErH_JoUB8QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=f349vRfxNl-pBZ8vOc5XrkZrpkH-uMAkqUpt2J7xa8gdVSFLfrBR74lFK10ln0U6i6CvnHIZnQLedBsK9JaZc4pShzPdSUTcQCJWuSh-jMcNCG84EDu5ATcMyWzrUovHTt-jKQWKSHOAjWCOeJQjhBT5I1ue8UY_SJxixmoh3qp3tgPMDokZ36wGKy0hzM01rycceJwlkMHxZvetp7HviEFHEQx0oDxN7k2Gn-E0Atz5QfBJDENLQ_RJLPZxPzxHZZb5HdPzP9bLkEewzyNSDZWh36Y3SNH-23y5HqYQEZrf8riXl3RFe-LJXorL0diEhS2i56kNfpSq8T81mqwUNzsP6VisQndWvzAjV1atJzW9Tbmj0WE_1MXFA38M4_PdiTgsuMOjr02lLNy0TUgsF34CeeZ8X3ctY1GsciZTOL0c4Hgv66VNP15Nyr1vufZ7acb_oQCpAhhyYOZMwzlRDrgsZ0fIiK7y9hzOv1btf9_AASbhYp6N_QAGCBt51O8ROrBEW0zUp8B6iciotqgccF_wS0TKm9CmzUJ3repO3bv9Nf35fTH98JAf-E6PgfdzC1Va7axXS5oM_sBtu-SuR9V78DHANFArMhIklo-UzfF32his7btab32Rrv2CP9PpW4ACaTtHnWcxDt2m96l6lz_3quWyS7L8ErH_JoUB8QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم جدیدی از حمله هوایی آمریکا و اسرائیل به پل B1 در کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/125032" target="_blank">📅 13:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125031">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل : لبنان و اسرائیل بر سر لزوم توقف کشتار اسرائیلی‌ها توسط حزب‌الله و عقب‌نشینی از جنوب این کشور به توافق رسیده‌اند.
🔴
لبنان و اسرائیل توافق کرده‌اند که ایران هیچ نقشی در تعیین آینده هیچ یک از طرفین ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/125031" target="_blank">📅 13:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125030">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
آموزش و پرورش: اعلام برنامه امتحانات نهایی کذب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125030" target="_blank">📅 13:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125029">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل : کابینه امنیتی اسرائیل امشب جلسه تشکیل میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/125029" target="_blank">📅 13:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125028">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آکسیوس به نقل از دو مقام ارشد آمریکایی: در حالی که ترامپ می‌خواهد جنگ در لبنان را پایان دهد، به نظر می‌رسد نتانیاهو می‌خواهد آن را از سر بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125028" target="_blank">📅 13:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ادعای العربیه: مذاکرات پیرامون دستیابی به توافق برای آزادسازی بخشی از دارایی‌های مسدود شده ایران به مراحل پایانی خود نزدیک شده
🔴
رایزنی‌های فشرده درباره نحوه و سازوکار آزادشدن این دارایی‌ها همچنان ادامه دارد
🔴
اصلی‌ترین گره و مانع کنونی در مسیر مذاکرات، به سازوکار و چگونگی مدیریت و استفاده از این اموال آزاد شده بازمی‌گردد
🔴
پیشنهادی مبنی بر تشکیل یک «صندوق ویژه» جهت واریز و نگهداری دارایی‌های آزاد شده ایران تحت نظارت مشخص، روی میز مذاکره قرار گرفته و در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125027" target="_blank">📅 13:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125024">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDlxd5-QetsSRM43O4Dh8eR4KVw6PmgA_bX1shr9Vr3L30R7nXIzmTY5u0unEUa7GJu_aiFKZgutv7cGf6CP9SW7A7_RPEB7-tHXVe6py6_y6tRiKNbu8xMlHvamRRiKPzPJapQLp6nPQfKBTWMkAmzJdSmXff79m8wW61RkGRbCrYuL2o2lgv7zUBHLPd4ry6DWSy05IjOf_6HqhV20pH-nMfGAKlxQNd0hWtiEyUUaeRXsmbx4WgdXbfSvXSRZvLBeTD6r5RZWLcWI7WPli0InxTZ1eBAY7e63k4zP9PKigJef_kLWIQJc6UL_0K5sbz3pfUl5xjcRqnymow4HFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8KiavCvxTbMEWvtsi-HRJeDkl7ox3TFFe_su1gKYTg4OlJUDnyT8TdWS2oyIqBEQdJZohDzyL8z4SuhHnHiW3p-90uUIWDcY2A8EBBwT1pKETz-mCvlm3xPDYHSleSBEATLaG4SyCgVqByAMPNnQkgDq9tUyYYjCBPaUOfs9eXQrg17hrc5O7vQZJB6n-1khV0TKjUyhWBjbu4gCePA9KMGFsPO15RXOpuklaNhZeCnJCOfAh53e7Ff5wFLhhsDi5Z0bNyWR3E58gvUBUiOVqzzlLGunCHqoRQEwOPKSypx5BcR7js-oFcNF10y5BdzqrK0xtORxZiSkAmIppew1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdXXqbbk0FOoeOUkaH8ub0kA3XtofTQ2-sn4nblswvR5qzx5ncjJn5lfdtKBhg62qrXaxkIrIS7DVmdZa1JAMIj7_o8Frt9tFd7RJM1S4thtcJCQr83wAjMyd54iBKGy_gVh0nynNCrKlJ2hfLJv2V2SysDYMJFEoWsOGxKgEAzudNRTSlNzrX6OSex16ObhBejaIWdlRW8s2jRDp2ts7s8qbbEFupQ6RTqyPJsf30In_U-v5-0hMnAPoI1_RJHQEp592DLaCvGC6nFhS2Q_A0s6xjraT2lwixOSOZ0hiR5I3kII8axbF92UVaVeciucOo_nf6Sp9x01esoZCEVPqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به تبنین و نبطیه الفوقا در جنوب لبنان انجام داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/125024" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125020">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bd8285ce.mp4?token=MsP4i1xDKfa7JlWGh6R5svvM7TIFB9gOqIwGgDugeI1fiWWjptQth_yhktWak54fd-DB88SiHjCX1HOyQqpWoD2lUxpSxz6M2GCegbe7UI6nE08TIcH2NYQ7H0bVHw97TxGbCC0Qu34-IcPGh39ZWXWXxQAWlwsxqRKhU8gwWa0yrs7lUVynzvRDJCCWOqRIOy8jkELX8UJF6-x8ttTC7X8DKfnzIvMGKlmxngVqtqm4SXXaBd1UH_LsFP2bAdopsBTCTTmKwJUNmIngfx_eF3QtQAs8PmCuO2d5qAIVYhU1kUBluXVRY41Z3besJeYZEJyboP5_AEd8QdBySh9vGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bd8285ce.mp4?token=MsP4i1xDKfa7JlWGh6R5svvM7TIFB9gOqIwGgDugeI1fiWWjptQth_yhktWak54fd-DB88SiHjCX1HOyQqpWoD2lUxpSxz6M2GCegbe7UI6nE08TIcH2NYQ7H0bVHw97TxGbCC0Qu34-IcPGh39ZWXWXxQAWlwsxqRKhU8gwWa0yrs7lUVynzvRDJCCWOqRIOy8jkELX8UJF6-x8ttTC7X8DKfnzIvMGKlmxngVqtqm4SXXaBd1UH_LsFP2bAdopsBTCTTmKwJUNmIngfx_eF3QtQAs8PmCuO2d5qAIVYhU1kUBluXVRY41Z3besJeYZEJyboP5_AEd8QdBySh9vGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌ها بین نیروهای دولت فدرال و واحدهای امنیتی وفادار به رئیس‌جمهور حسن شیخ محمود و نخست‌وزیر سابق حسن علی خیر در طول شب در موگادیشو، سومالی ادامه داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125020" target="_blank">📅 13:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125019">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فارس: فعلا آقا رو دفن نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125019" target="_blank">📅 12:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125018">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: نتانیاهو دیروز یک جلسه امنیتی محدود برگزار کرد که در آن ارتش طرحی را برای یک عملیات نظامی گسترده در لبنان ارائه داد.
🔴
در حالی که کاتس و بن گویر از اجرای این عملیات حمایت کردند، نتانیاهو به دلیل فشارهای آمریکایی نسبت به آن محافظه‌کاری نشان داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125018" target="_blank">📅 12:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf769954a5.mp4?token=ajEQD1OXB9AirS1vStlU0VIwLOekEyB8caqrBYBeZX_twY6hufroyPMTZbotpVXmhSJA0XEggZPw5AiNacwaQkbDoSK8Nm19DwK6xpWw_0AA4Xjz90zJcS-_4qk2NUhc4mGIShQ2DQb9lJ3P3szdT26PcObT9OBiel3rIuE1ljs3meEYz5JhxbovlaI_JBaIlDm5HkIR2lYm59vHFShipWYg_IBuDHH0Ixiz-Kj23aiKFDhfwykPDwd3RgwZYHigmIVcB2Df9nwkPD7GwYtwhor1ods3KkCsYf71uNJNGoAtiVJyYslVSJ3eXCUXyo3dtCSro7srTzJeYZIHAPuRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf769954a5.mp4?token=ajEQD1OXB9AirS1vStlU0VIwLOekEyB8caqrBYBeZX_twY6hufroyPMTZbotpVXmhSJA0XEggZPw5AiNacwaQkbDoSK8Nm19DwK6xpWw_0AA4Xjz90zJcS-_4qk2NUhc4mGIShQ2DQb9lJ3P3szdT26PcObT9OBiel3rIuE1ljs3meEYz5JhxbovlaI_JBaIlDm5HkIR2lYm59vHFShipWYg_IBuDHH0Ixiz-Kj23aiKFDhfwykPDwd3RgwZYHigmIVcB2Df9nwkPD7GwYtwhor1ods3KkCsYf71uNJNGoAtiVJyYslVSJ3eXCUXyo3dtCSro7srTzJeYZIHAPuRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان فتترمن: من همیشه به هر چیزی که اسرائیل نیاز داشته باشد، چه نظامی، مالی یا اطلاعاتی، رای خواهم داد.
🔴
می‌دانید، آنها یک معجزه هستند و نمونه‌ای از دموکراسی و ارزش‌هایی هستند که ما در کشورمان و در کل آن منطقه زندگی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125016" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی (IAEA):
آژانس بین‌المللی انرژی اتمی توسط نیروگاه هسته‌ای زاپوریژژیا (ZNPP) مطلع شده است که نیروگاه حرارتی زاپوریژژیا (ZTPP) که سوییچ‌یارد آن به تأمین برق ZNPP کمک می‌کند، امروز صبح تحت حمله سنگینی قرار گرفته است.
🔴
تیم آژانس در ZNPP دود کم‌نوری را از سمت ZTPP مشاهده کرده و صدای فعالیت‌های نظامی را شنیده است.
🔴
فعلاً خط برق هنوز متصل است. کارکنان ZTPP به دلیل حمله در حال پناه‌گیری هستند، طبق اطلاعات موجود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/125015" target="_blank">📅 12:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125012">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBiaM53VIgtU8liz9VZrco4mz-akCZijg_sIMZDfCycWHiz5H6Zi-A_uy2495LDx5wh91ebOSSDaPhISJ_wADxzRj9-Ud7TLHiP-HcoLNmR467IjiATUKrecsgZL_kaskJ0NsjnM4ITUky-P1SFFeYqFwudnSWFohJUhu8kaQDUCLrngxmTvhC6KSGLcVqeiKYQllRBwzXenpBQLTH1VFqRr11USjCcan8Q1t-ZCmrQXE1N2I-3kBLpoR8k4m8oEzKO8hUHPh6QdRa0OsU7MxBWHjsGouW4F4cGS3TmmdhOPaOa00FP2zdxJUammqfVm0Nm1T7lWe1anKry3NtfzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWL0JIPak0KVouGZKR7CV7Oiry9iLi8iq6avF9YQlzuSUNIf5WNTMLg_Z2KqPOiftkyxm_AxqnR6sTqFUMytSD5UsHxtHNND8vdF5JYt6xRf65PIv7O4DCskyZsj5ZxvQw-3y6gxZNYfX_M9aTc0Ol17_z1VLcHK2z5eyvg0YVpHmduuPzNrEyhiLKqoEbQG7XIafE5R4UYGNWQ0Csw13IXw8xcFVkzm-aa3k7wCrece13m4hFPo9sGEJwkZKuUV0iBFvNV9VthPHINSSA02eWzWra0VQk05dB2h6vvY4v-pV0v2dMW5IcVpr9ZfiNIbsU_j-b2i2V7Z0oxpLwic2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1sfOwdarA1ux5tXkQh5Tg2RXsVZ_s_fa4ea7TTYbpBhWDkUN4ErK9bQLoAUM3b5RHNJ5AZaEkbzxfH2pibaoB0gyXE76itOeWOqWkLru3JdtxNXaNZerkNntekstMv09I8UYB-pH14k1Gn32hh_4LZIBIQukoqVZmHyUsT6mxOOjbPOWoYXDY5ADmpW5wlzL3pXVcTTH02AQLvVSedinlear0PEvXiVAoNDMChMa5AypiUZuq6QTnRDI-r8uFX0iRsBPgMPZwDUokWTlTnaOg8Shtn-i121zx-hvKPfBDZeGmbS9j9tl3ByiHJzLkD4zSGAM3DleEHMkya0wALL-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی همچنان جنوب لبنان را بمباران می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125012" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125011">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: پهپادی که حزب‌الله پرتاب کرده بود، لحظاتی پس از پیاده شدن «رافی میلولو» فرمانده فرماندهی شمالی ارتش از خودرویش، در آن خودرو منفجر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125011" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل هشدار تخلیه خود را به همه ساکنان جنوب لبنان مجدداً اعلام کرده و از آنها خواسته‌اند که به شمال رودخانه زهرانی تخلیه کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125010" target="_blank">📅 12:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گویا اسپاتیفای رفع فیلتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125009" target="_blank">📅 12:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شبکه عبری کان: پهپاد حزب‌الله به خودروی فرمانده فرماندهی شمال ارتش اسرائیل اصابت زد
🔴
یک پهپاد حزب‌الله به خودروی فرمانده فرماندهی شمال ارتش در جنوب لبنان اصابت زده است بدون اینکه تلفاتی در پی داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125008" target="_blank">📅 12:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
منبع مطلع به العربیه:  ترامپ به واسطه‌ها اعلام کرده که پیش از امضای توافق، با آزادسازی پول‌ها به ایران مخالف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125007" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/125006" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JCk3UngcX5CaWkWL1yTw7JMuCrYdOdOkobkPS6BvwgDBjNetFAUsnlcAx7dviIa00pEtGj45sGnGBVLFC-rFsRKLkflQpMKX2OlYhtEq2LNVxD2SR0Wkt7toSccQXLfr0EpwsL67ZWwrFzjKuBwH2B-SGolbEoeBiopIFsCVC2Ale5LzQGq8SL22w_DTBgH9W1ME6u5kcgSBHglwicdKPmvYuNREoP0zYS_j_SaK9mS2AS8POccvlgYxbp4mXet_DzNQYFRQvN6Vv5uZTjP_XqEWNyhnJVnV4lIXLk5xd0ob8nuKAgikQjqCYYd68vx6AV-ctyO24J6bYubwx94mbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/alonews/125005" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125004">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep3lO9tn2qhPyjFt7RJSnqqDwYtFfv3c-ic9jyujZMhH-QArlevn4qXesoPd1wHAEnTaFS8yrVSyI6lxTZGeUegFaqKOLUAGKbfF3PACVYJGLau1ccXDA-N-51B8Ft4TjAxWz06qQTTg8kvsvQHuUMKa8cjKWBS1_SPIomCaeQsCemBj_lhbgcUQIrQwb3bXJgIVmJDGYiYjxRPnoG6kJpfZgliyqLf4mahrBrn2ShzHiG1fegE2KpEeCdO4CjPQtsEzdKdO6NQGwOLNINxmiS5iPQ3EliXpIovo20Tj4r9pIDe74-Jk2GCuclo_uEDIkShEDoevXAy23AtOTuynEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از ناوچه Boykiy نیروی دریایی روسیه پس از حمله پهپادی روز گذشته اوکراین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125003">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RepMfjxTo7o6-B4Acpf6x8B6l1PANLWsR7VLtu_PvnLYRpUNU1uKY77hSJZqF3v_wsbS1wq47N61KG46_hiu5V7Jzca2bmGIoQCasupA1KyybnrgBZTPduiMr6Uud34fikM3RkbUQcD3ZhL24X5Zt47lZlar64P_5nRNX1agVK0uFfHTny3irPMDchO4UKZcki4_JuNl3mEeUi_WQ_TeYJOHrUlyS1fCtrtHtNUey8aflzxbNzYZJpkaw3puQUI1nddNOJhAlEnPukGdmjCd9UDt9OsX3IjlHl-OtxGR7jQzs5iR6Ui5Dub-iG0ugQ5hXX8RVA_DvJfFTz0q_InuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: سرهنگ دوم آویخای ادرعی می‌گوید ارتش اسرائیل اولین هشدار تخلیه در جنوب لبنان را از زمان اعلام آتش‌بس توسط ترامپ صادر کرده و تأسیسات حزب‌الله را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125003" target="_blank">📅 12:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125002">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: ترجیح می‌دهم آتش‌بس در لبنان را از «مشکل بزرگ‌تر ایران» جدا کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/125002" target="_blank">📅 11:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125001">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مجتبی خامنه ای :  نظام سلطه پایگاه نظامی به نام «اسرائیل» ایجاد کرد و ایران از موضع خود در قبال «اسرائیل» عقب‌نشینی نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/125001" target="_blank">📅 11:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125000">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jck4OhJvEl5UEOb8z4iAGwEoBHnBwXlw6Ool_3rTiaUpSSoWN8AmfW-4eRTvxwYjzak2-rBWwW1ikImUqS2axdWv6ZdKCnuI8B0wKwDorZ8uWRKkIWq76sVjJcVLl99VYdODlG6UVqlNPfLisImXNQcHYrCQNkaNqQIvm_FQ46FByDCAgNaMiQ1qUgz0ep8eR2lS-q6yyg9Czs9EUMUWoBtgCuekYjyWOWzUzrqjgmE6IYArIjfZHsgvu2M4f3qqpzl97PDGU7BwpxAUuqvNtQO-XFOdrN6GR4oyb9c8_QXmhlv6hZj5j3PmKLwGNl8cTBrONQW8o7xFsGZO-MmE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۴ خرداد؛ سالگرد درگذشت روح‌الله خمینی، بنیان‌گذار جمهوری اسلامی هست
🔴
وی در اولین سخنرانی خود بعد انقلاب گفته بود که شما را به مقام انسانیت میرسانیم
نظرتون؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/125000" target="_blank">📅 11:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124998">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEXP7FeDRS5AUrUegv53KhEmia8H-zK2hH42Eo3s-l67i29Rc7soDk22480uyHhutvTnqNXANtPHdr-37zuWgbhgjUh0dOAxR66jOd_7QX761O3lb5OV-mZiojuysAQlMdHwjrYAKg3VJlbvXOe9QWCQfheAhfKe1Mvg4q7T8OVdVpQ9Q6-FpLEGzIWPw1bPjByp6H-zkZ30qtvFquiGoKTfaF6gyBx-tSu1wdjTb6RRhn5IFpnsMRQyfZSai4a3VaN5ilPxEQvjRBCpCwltKrtSaluMRgn9BHpw0rDoxqV7s-x9S7tu_c7V6PwK5hLbZNbcTe9YjCSSSrdL6lScxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLPvacTIwraQ1RzJXOA0VozRFojmlIMc65Tt5QNnkZzayqrESWwnBf3us-zAN2dVohF2eDNi2ENzsY-IYNCjQy97LpE2pmzOx6dRncsa7ZRvMtOMhbZ2wdzKEhnnw_-z8ZI2_TQ-xNbRNh8We_qIjx-8o3IiXux7R7O9MeiWtcbsT-NmnSnavbwZ1J95va8pGU5PcWzqlX_lxspuZhx_6TAivS2dnTm35LS-eDS-8iXmOCcK70yeZVJxIprNDH6ugobII0TLqSHs1nostEkmOLScCxoJ0yo97GVBsDjnEd9tdsCwheGZJzeKpFgPbcUbx1Pvau4BzHY2b-7lPDgMFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی در سراسر جنوب لبنان ادامه می‌دهند.
🔴
عکس‌ها از زواتر الشرقیه و المنصوریه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/alonews/124998" target="_blank">📅 11:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124997">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8cV_1T1YSmh6t6et1ldKvABSfJxrcJJ6D-gxgE0lzIKgCU04o6FdJg1okyZwk45YVpD0wbi6FuAWE07Qq0wIK3NqSgiYh5R9t9enqTOmcoWj0qotHR6hHvreXV_uy7sdQ5fTMewlMnxXh56z8VXrzA291b5672mYwp3LO8RiQFfdE7D2-EOwoYYxjSpXHBMYgk_zFX1h5fe_vZYiTZ42QvLv-4Z-B2Mql0Ut91WbMoPE3m8kRzVxMW1AdU1cDlkRcpUxlG_WOrGqxCn7T_mf9LBrM8RVao3wjQXKrALSS0Y31eM2cOsw23D_4LwQ1V6fh0bp3KWgff2iNDXqt_G9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل شرکت «ایران تک»، جمشید قمی ۶۳ ساله اهل نیوپورت بیچ، به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران بازداشت شده است.
🔴
نخستین تصاویر مربوط به بازداشت او در آمریکا منتشر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/124997" target="_blank">📅 11:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124996">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: روند مذاکرات میان ایران و آمریکا ادامه دارد.
🔴
هرگونه افشای اطلاعات درباره ایران به آمریکا در سفر اخیر وزیر خارجه پاکستان به واشنگتن صحت ندارد.
🔴
در جریان این گفت‌و‌گو هیچ اطلاعاتی به اشتراک گذاشته نشده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/alonews/124996" target="_blank">📅 11:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124995">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
در ادامه موج بازداشت‌ها در شهرداری و شورای شهر سقز، یکی از اعضای شورا و یک کارمند شهرداری به اتهام فساد مالی دستگیر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124995" target="_blank">📅 11:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124994">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntJ-XtU2n5n5RKbqVjGVTWws-oxYuFM3B5XAY4rSQSK5ykw8hQqc3QBOzj5EVSJlD08inCHM1mYO4KELxzDDxxdG7ABUUee4SUPHzzk9Ep3JsSstZh4oQqgFLfO3g7tnH9Q9h6OSXJdvuVcm97p8GE4mJOtUt2rbzhkeFOnGb3mmRsGPbF8cSoxcPhgGnGCuLgWM0HhQoSV2d3GZoSrdTVl5-v-tkrtWwl59jExSXgWj_vt_tMZdSYfL1v-2wPDvL7WWHpS0uKavlrg8YbtjitvP3_EjpLaA4EoHBT8Rg5i_mDl0q17vAIxUidYZULoeYbhrkdzd8X5lR0jIe7xLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به پزشکیان و قالیباف در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/124994" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124993">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کیم جونگ اون به رسانه‌های دولتی کره شمالی گفت که قصد دارد «نیروهای هسته‌ای کشورمان را با سرعتی تصاعدی تقویت کند» و اینکه آنها ظرفیت خود را برای تولید مواد هسته‌ای با درجه تسلیحاتی در پنج سال گذشته دو برابر کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/124993" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124992">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/124992" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124991">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bedf43656.mp4?token=rqOCrzjRYO3VDV-9N-P8BO-j-y2C3lmSfEc2vT0tgLf-NeECG46Vt1iAZ_73Vvabo3uBBhRVDH7aex3DjYEdYGpmVlfhKZ7QT5B_BtF5XHPrFmRF7rR3nxnHiCdj0tIku08GJb19NSCNbOhjsnE0FZGKpcYYrcRHHjkl8zI920rWj3hQzdYNGjPzxUeZGDeb4WqE6osyicGE0pwRlVi79N4VWWaoUKmQJQsfCadq8lGxMu-6yUU4v_Co_B4OOUsYftw2uwrUYKU4LS85eo0XuDlAUL27kAbCLVo4VFMXyl8o5oHfPOn06TvpyY46UraCpCUCy5xdtBP-7GYLqr3PCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bedf43656.mp4?token=rqOCrzjRYO3VDV-9N-P8BO-j-y2C3lmSfEc2vT0tgLf-NeECG46Vt1iAZ_73Vvabo3uBBhRVDH7aex3DjYEdYGpmVlfhKZ7QT5B_BtF5XHPrFmRF7rR3nxnHiCdj0tIku08GJb19NSCNbOhjsnE0FZGKpcYYrcRHHjkl8zI920rWj3hQzdYNGjPzxUeZGDeb4WqE6osyicGE0pwRlVi79N4VWWaoUKmQJQsfCadq8lGxMu-6yUU4v_Co_B4OOUsYftw2uwrUYKU4LS85eo0XuDlAUL27kAbCLVo4VFMXyl8o5oHfPOn06TvpyY46UraCpCUCy5xdtBP-7GYLqr3PCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از پرواز پهپاد پنهانکار RA-01 اسرائیل در آسمان تهران
🔴
پهپاد RA-01 یک پهپاد شناسایی-رزمی پنهانکار اسرائیلی است که برای ماموریت‌های اطلاعاتی، نظارتی و حمله استفاده می‌شود.
🔴
ویدیو مربوط به زمان جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/124991" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124990">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ارتش اسرائیل می‌گوید درگیری‌ها در جنوب لبنان ادامه دارد و به ساکنان لبنانی هشدار می‌دهد که به سمت جنوب حرکت نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/124990" target="_blank">📅 11:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124989">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q32EbrNelZws6vRNPN_7nGmIMa3CEPXoz3uKRvHsfEkupse7mqYdmxmCy_28piUeIBFW9X_ZXiAQYd2A0uQClsMShPB8XAkWiO_ZIIfH8lJXIet63-S7gIMOY_VskrirhycmBhpzEo9kRBew13_ntMTLbDKN3REFIKxDz13WJKv-GIF1Q13aVyCKrNT6yg4JQvfBpzvX_sgWaaY9mUPqwvjrjVn5sRwYklyrdc6CFReK0nnmPsDDR3d6_uX53Gz5My9TFkNu64NlKI_97UFSiMN-oQK3NIgxJmtC0VwVuoWhGLcWj4AlN4SVft8_-wKm-1GnX-egVk-RD5BWOHQGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/124989" target="_blank">📅 11:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124988">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YSbUeIy2wA95bNBC4jalswvcamQmsyv15-mkEEUbEn6iExknAoQ1rYUO7PRXkfVACG_ygPhmjqmBZqJcLzgY0nB_htKYpVWB02shO5bpwyFsFVL4P8ueAKA69PV1G2Ryen-t7uO4-GiGiO21wQY837yE_JjrZy6gYsxzi2w_b66rmtLpEK4J3aG8SSrJGisZ3zj0W5ILoptU4sTJmK6PmiUub6sAPFAtYxn1PKWU8Xhsxzogeglm5CZDuzQU4m0oXKl-mw_p7mxjsyr1fphQdpPnaCIcMTiSF2ajN8SiQJ5gXfmYCOoak_QKChZgZ6EGeitluX1wQZneas8EH8DtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/124988" target="_blank">📅 11:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124987">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca1e1a949.mp4?token=XYO0dWUyrp6s2o9JY2-_8hYIFLDaZQnOXVUUSDXRePArLs0ZuvrqhTnaDy9VKsoH8q_iMoCk1-xwvBks3m9DRAb8nxqcCbykn8_UvcEK4-USiFWR1fUygDLibRVBQeBDwWIMX-DuG7WT2ku7EBH2KDah6eSLUuWqGzcooKSI6qW8reZwDG71u_FxHFrmOBJYWRwVmE5U0AIe5SCofritYqCLAzMhYYsNAnAyVuHhNz14s2BaLFqCBU7Avfg7Wft9cMIWeUu_7_Jr24h5xtGhOzbqirBF6zOjt-ElSKSMUz55A1Or-iDqiU9SdK9VrTdOUuuL_-1IuEPFFv27hNhcHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca1e1a949.mp4?token=XYO0dWUyrp6s2o9JY2-_8hYIFLDaZQnOXVUUSDXRePArLs0ZuvrqhTnaDy9VKsoH8q_iMoCk1-xwvBks3m9DRAb8nxqcCbykn8_UvcEK4-USiFWR1fUygDLibRVBQeBDwWIMX-DuG7WT2ku7EBH2KDah6eSLUuWqGzcooKSI6qW8reZwDG71u_FxHFrmOBJYWRwVmE5U0AIe5SCofritYqCLAzMhYYsNAnAyVuHhNz14s2BaLFqCBU7Avfg7Wft9cMIWeUu_7_Jr24h5xtGhOzbqirBF6zOjt-ElSKSMUz55A1Or-iDqiU9SdK9VrTdOUuuL_-1IuEPFFv27hNhcHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی جدید از حمله آمریکا/اسرائیل به آزادراه بروجرد - خرم‌آباد در طول جنگ اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/124987" target="_blank">📅 11:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124986">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
هشدار هواشناسی برای مسافران شمال/ رگبار شدید و آبگرفتگی در جاده‌ها؛ باد شدید در شرق اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124986" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124985">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d6e65b18.mp4?token=ZcUbqLnoU-DcX5HjU8uIoGpmAT6qGN89S6vQEqzDoMGbABV3XEiOcomFijh4JxFfSyJPfdr-v1t_BKHHhlaytLNn0DMLSJcZphL-SojNlkOz70vJdiQui-L3LIcvl-EoayUa-3BTHqePDsWsbv0xLHrT90CA78mATVfle1ofH21sRa6VNxvp5v-xcnZLbaZHSFQDxjD924z7dF_f4DpTOwDpN-9dZiRElTd8gdFaqTED1ZEgLzjs9l3qW2nINVR-aJEEF95KJY-HQ16NcSJZLCH_QIFylSzjoNYKgvqyU-B_VnzTm_vO3YmptiXm-nq-eHTJ_keaS64MG6e1iYBdSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d6e65b18.mp4?token=ZcUbqLnoU-DcX5HjU8uIoGpmAT6qGN89S6vQEqzDoMGbABV3XEiOcomFijh4JxFfSyJPfdr-v1t_BKHHhlaytLNn0DMLSJcZphL-SojNlkOz70vJdiQui-L3LIcvl-EoayUa-3BTHqePDsWsbv0xLHrT90CA78mATVfle1ofH21sRa6VNxvp5v-xcnZLbaZHSFQDxjD924z7dF_f4DpTOwDpN-9dZiRElTd8gdFaqTED1ZEgLzjs9l3qW2nINVR-aJEEF95KJY-HQ16NcSJZLCH_QIFylSzjoNYKgvqyU-B_VnzTm_vO3YmptiXm-nq-eHTJ_keaS64MG6e1iYBdSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز گذشته/بدشانسی عروس و داماد سنندجی و تصادف شدید با یک پراید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124985" target="_blank">📅 10:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124984">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: از زمان اعلام آتش‌بس، حزب‌الله ۶موشک به سمت نیروهای ما که در جنوب لبنان فعالیت می‌کنند، شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124984" target="_blank">📅 10:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124983">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGh7OvVex7ZyOSYvVL4JABaTUtgygD2uJbhKqseWuDa__Z_CZVLUWhOKTnlwV3qiZZPGoQvbst9a-ych80xQHF8iClVXjFV3-sgVAMqQTQeKc-NxkUKZPvMERC4iG3rgElrPDLhR2BqNA0klKDBtZunBPEs8nQRlMLqvmnse80A7CpDb2TPUppeIn2xXlUz0GLXvDYRrWBsTxSjNU5w0UUMK15YA_XyVsVW3Aw0HCal7A6ArSEpm2i3mXeRefNdEp49cVt5I7X3qHRxooEsFOa7p6L7koH_loET8WYcjnDoWKVPHi6CG7MqJShQXuxPUaKYcQkczN9k8XVe8Tq-MiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله مجدد اسرائیل به منطقه نبطیه لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124983" target="_blank">📅 10:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124982">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
شهبازی مجری محبوب صدا و سیما: من سالم هستم و خبر تجاوز گروپ به من کاملا کذبه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124982" target="_blank">📅 10:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzmubMZwj0CFOvQQoZAtdo7RLwC0SJSf2OlrlBZjmwTOpGrvL79eaQZ_hBirM9JlUWSWv2A_TX5giYx3Fav8FYr5ikIobv6TsKrTv9nda_yfjuGVTibM1b85w_3otuH76U9SZ6nnwsvnXrb8zEhVIv01j_OFR8OmgBzTgM-4Dh2-4zDKlliQZSaqnDt0HzBzbIiwz64ykTTec-eGHkUh7D7W0WoqcCVXLtNlXSh3bnskoB7rGOW0IA2QXBiB0WCg9LMDtdHjJRfvfSX6FA7GnnGdRh987ahLVxrGh05TcuDjI3sT9TJPD-ZIfYJayycZb19OCdndnnS0orBZkUZylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5SunRXhMzRsHkiiC89PJksLWiM9dfV4BRUrU513m6yDxBTBrCrfz8FIPY9B1McJAb0J3Sv2tinQKBqgWOl_adMshHTsTDCz8_8mkeZAcW9vmnU7wqdCWP0Hj46cU1g19tkBcN8VnRvg_RtmpaChrQTcdfOzs2WnrKV7udDekpVb_KD85i1E9RyQUKrhULGFi2FX0ht-TBU9r2NfB0mUU0WuEAA1-s3edRjuKgwV4pvIGKE_6gdeCEQWMKyFcKEdUkISS4xG1YfPi3y2TJxE-BAFI7eYRWJmbEvK2pvqWf_uKPjA9kZr04Ta3rgOGGt6c-exQyrtdriOLkkh_ZsqyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2724519f2.mp4?token=TF8I_iKwYyAWZrptgaKkAoddzF2eE-fjB8i6yX846a7481JJkaC6xS7o7pRvI7sS37zen8BYeyoOK1rOY4Ld7S2SpPVwIZyq_wKGpwA_s5uJbELjvLN7pyzG_FXOMJEDey4uiNbVILKc0QNtfpMtsi5S8OXLpmX9_NqPPxvU-ND7X1VUEWLrzK3DSdLPxEt_JN5BI9pZYS7hsbOf7Zs9uk8I8tarS6HcLCmG6lKq0iX1GdD-rAUsO92CWyO3cUk2mDRInAXB53irUeEHv8tNxb288Xc8JczbkkxmxkQMXWx40dt71kM_D9UAFTZo3EjeEvHvwzZ88gxaptmMXJvsGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2724519f2.mp4?token=TF8I_iKwYyAWZrptgaKkAoddzF2eE-fjB8i6yX846a7481JJkaC6xS7o7pRvI7sS37zen8BYeyoOK1rOY4Ld7S2SpPVwIZyq_wKGpwA_s5uJbELjvLN7pyzG_FXOMJEDey4uiNbVILKc0QNtfpMtsi5S8OXLpmX9_NqPPxvU-ND7X1VUEWLrzK3DSdLPxEt_JN5BI9pZYS7hsbOf7Zs9uk8I8tarS6HcLCmG6lKq0iX1GdD-rAUsO92CWyO3cUk2mDRInAXB53irUeEHv8tNxb288Xc8JczbkkxmxkQMXWx40dt71kM_D9UAFTZo3EjeEvHvwzZ88gxaptmMXJvsGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صور، جنوب
لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124979" target="_blank">📅 10:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f6a25b81.mp4?token=cvZmV9ZOhNgAEd_n-Tb9PCOtlRD6HzOM-kjox4FFKRXtAnXzjXRnKId91SExY-RLfXoTsDYMPFrlc93KBasKqWdwj6LXN1lwhh7TGiVan6Dcp4Ad_--0J8ZeJhgd11-47GHl6f8AnkspR0ohyWdf6zAVo_d7HdlMKgn-XoOoG_WrJ28WXB9qSf-1nTtmgxDRfWLYlY8abGMCKlcZJUsduhUCZDy58D7ofOpgVU5LW205Bejgy88teOamduXDr0cVOa3w24K7u13TB-zrnGMhEi_JK_uW9tvkLGSuwSHcquWFguVmK6ozQSt3mlcZV5m9BzPF1iBZQHICbcUrmqE5mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f6a25b81.mp4?token=cvZmV9ZOhNgAEd_n-Tb9PCOtlRD6HzOM-kjox4FFKRXtAnXzjXRnKId91SExY-RLfXoTsDYMPFrlc93KBasKqWdwj6LXN1lwhh7TGiVan6Dcp4Ad_--0J8ZeJhgd11-47GHl6f8AnkspR0ohyWdf6zAVo_d7HdlMKgn-XoOoG_WrJ28WXB9qSf-1nTtmgxDRfWLYlY8abGMCKlcZJUsduhUCZDy58D7ofOpgVU5LW205Bejgy88teOamduXDr0cVOa3w24K7u13TB-zrnGMhEi_JK_uW9tvkLGSuwSHcquWFguVmK6ozQSt3mlcZV5m9BzPF1iBZQHICbcUrmqE5mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله به انبار نفت کرج (فردیس) در جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124978" target="_blank">📅 10:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlZp6hXX0_uISizEHy9voqw6U9VcqXNxRH2liXlFOP6kpMg5P-d6DVFnUDl3OzfdjUDStmV8Skno98h8BW6dq3iH6DA2BKxbpF4bnRiF96mMJkypiEvSAUqwQzPGwmD-hEbSLcgY_PVQ4iCvmONJvug248AqhGACiidr4yXbqUMc5x98Bwzgvlo8LMendaSsTcdNcC-3wDi4mnnORvkkGWaQUrdM2qQSYxJYSmNINSnuy-URaAWe5FHDBXntPBOSHGP6lxKFOu5EW8mfua2H6DKlC3gMzQ_FDinPrHjkOIm4VtsEW2qqzzJdb2IWKY0ys5Rsy4_l9PQoucx4s2K49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دموکرات‌ها دوباره شروع کرده‌اند! آن‌ها در تلاش‌اند تا فرماندار کالیفرنیا و شهردار لس‌آنجلس را از دو کاندیدای بزرگ جمهوری‌خواه بدزدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124977" target="_blank">📅 10:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وال استریت ژورنال : ترامپ جمعه گذشته آخرین پیشنهاد ایران را رد کرد و به دستیارانش گفت که ایران باید از قبل امتیازات جدی بدهد، نه در یک دوره طولانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124976" target="_blank">📅 10:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN_dFuE0Y6Ytgx0l0wtHH4nK-yAIYn_SyIhaqgaJ_CS3621V-C4tBo9scuZPuT2zC0wIq7CnHP5W8KQGmuPkqvn2Si6vStzVz5C4WwEJu9jRkWjaS_RffwjBQ9D5VKtRrT7nXuiJEDxVtgt95gRIc4uBisoMJ7A-27bRYS5XZ7ppPXC-cMfs5LZtU4ys-ozyMc0MJD9LG8sMcnqR__6haf5S___hsJLModlu2RntCTG_QybT00N3wRVlOmPZwRtbVHZIXVp-ZmWxknMdDlbKYNgvUdq7XFDeRBTJvto4RUsEsOCT7ly2Tonbn6v2dLQ3F-NnT1K6Kmz1XWRHtzOOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی اسرائیل شهر صور در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124975" target="_blank">📅 10:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwHMAYDOL0BdLTFImzYd5FJgkGNzH69bK-X2dBz0xSxVA-W9w4D0yOagaW-3mj9q6KS4q_huBZGomeaMPbNZgT5zdOUpsiTFLrXrW8urA0PACKNIK9h80D48mO7jZlFKERYTOm-vIa-US-Sql2JZTa_y0FaPCyYhhZ6wYZ0gxQ_x9fwcswxJnM-2zULxAtSIaJRKhJJMhHLLkBGnWGwj26bAWrYhvsix74OL0eEFFMpekWHBp8R_7mLhMZZBlCjqsEbYnMZGoWkimV57UcmsGkCoR8N4ZWu9WGYExgpmju7SA0H9H2O0K6WUWNxgfTqrNo5TwLSII6bFbyJQufbnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا بیشتر از عربستان و روسیه روی هم نفت تولید می‌کند / ایران در رتبه هفتم
🔴
بر اساس آمار سال ۲۰۲۶، آمریکا با تولید روزانه ۱۳.۲۵ میلیون بشکه نفت، بزرگترین تولیدکننده نفت جهان است. این رقم بیشتر از مجموع تولید عربستان (۱۰.۱۱) و روسیه (۱۰.۰۳ میلیون بشکه) می‌باشد.
🔴
ده کشور برتر تولیدکننده نفت در سال ۲۰۲۶ (میلیون بشکه در روز):
🔴
۱. آمریکا: ۱۳.۲۵
🔴
۲. عربستان: ۱۰.۱۱
🔴
۳. روسیه: ۱۰.۰۳
🔴
۴. کانادا: ۵.۰۶
🔴
۵. چین: ۴.۴۲
🔴
۶. عراق: ۴.۳۹
🔴
۷. ایران: ۴.۰۳
🔴
۸. امارات: ۴.۰۱
🔴
۹. برزیل: ۳.۹۵
🔴
۱۰. کویت: ۲.۶۶
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124974" target="_blank">📅 10:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
لیبرمن، وزیر جنگ سابق اسرائیل: آتش‌بس با لبنان چیزی جز مهلتی اضافی برای حزب‌الله نیست تا بتواند دوباره صف‌بندی کند و قدرت خود را تازه بازیابد.
🔴
این آتش‌بس نیست، بلکه بازگشت به همان رویکردی است که ما را به هفتم اکتبر کشاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124973" target="_blank">📅 10:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b489036c24.mp4?token=alme5gjrIhLop5BzwdFYuyuEG3IE2TKWh1DpKLWexL7JYmCPQYwIJxK5e8NiFjL7mcxXVDLRYrIpPZMnPtF6X1qDf5b5ECJjw14oxCMXS41b2SM2hbzePqekS2JCYbMXd7nFsDOC59h1gDAn4d3KhGMqACWRopl3purrZSFASRbK9O0JDtnee42CSBfXDGs82ukQYkhYy54u-dhyCsTxRHXjVosbcn2Vf-uT_GzHUiq-6Y8Gm7h7ralEE-RR2F1Cs0guT3_wivLMXxNqovOZs2PWLm_LXIiWU5jURTij7jRx3iQcBRMgsvFuXbluGf9U16KE_d8_OiM8GbFWen991A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b489036c24.mp4?token=alme5gjrIhLop5BzwdFYuyuEG3IE2TKWh1DpKLWexL7JYmCPQYwIJxK5e8NiFjL7mcxXVDLRYrIpPZMnPtF6X1qDf5b5ECJjw14oxCMXS41b2SM2hbzePqekS2JCYbMXd7nFsDOC59h1gDAn4d3KhGMqACWRopl3purrZSFASRbK9O0JDtnee42CSBfXDGs82ukQYkhYy54u-dhyCsTxRHXjVosbcn2Vf-uT_GzHUiq-6Y8Gm7h7ralEE-RR2F1Cs0guT3_wivLMXxNqovOZs2PWLm_LXIiWU5jURTij7jRx3iQcBRMgsvFuXbluGf9U16KE_d8_OiM8GbFWen991A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی ایالات متحده:
نیروهای آمریکایی به یک قایق مظنون به قاچاق مواد مخدر در شرق اقیانوس آرام حمله کردند و دو «تروریست مواد مخدر» را کشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124972" target="_blank">📅 10:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2ae2072e.mp4?token=FH1ya6Hoztz67nQkSRe48A7OveDC9ru8zzQNXeVy24awWXniezatu_sK-oefb0FgNK9S6ViS227P51Dk6sLlN1mGYMTppFAQUXX4NG9NGpnI9J4QoJnl4_L8gAP3oYB1DCwuOWA4sswN7F-exg9KbpT548_u2OJzz-PbI6a8BvlA9ccMXkBU8s092trhOmCx0KGhvV2qTcF95Amxn5GEoKTgXjeWPadeDb8EROI62xxovSOzuJzqhzBF5XN_9lCKu3Y5dVA1w8_0gclGGgLgLQF0A1UV9TRVtGo_aKgVjeUsimpZGYSkusE7zFSfCGL-O_7YZEGonIbSzB1U-EYtIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2ae2072e.mp4?token=FH1ya6Hoztz67nQkSRe48A7OveDC9ru8zzQNXeVy24awWXniezatu_sK-oefb0FgNK9S6ViS227P51Dk6sLlN1mGYMTppFAQUXX4NG9NGpnI9J4QoJnl4_L8gAP3oYB1DCwuOWA4sswN7F-exg9KbpT548_u2OJzz-PbI6a8BvlA9ccMXkBU8s092trhOmCx0KGhvV2qTcF95Amxn5GEoKTgXjeWPadeDb8EROI62xxovSOzuJzqhzBF5XN_9lCKu3Y5dVA1w8_0gclGGgLgLQF0A1UV9TRVtGo_aKgVjeUsimpZGYSkusE7zFSfCGL-O_7YZEGonIbSzB1U-EYtIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مداحی به زبان چینی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124971" target="_blank">📅 09:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2n4rSzShUWerYea6_kE2IjdMJdqYWfKLWaeOfl3VJ923i9f0HGXB16ZkKH8UdQXwHu7zXktNYGNxixzhWydJeoblOX709DYqKBeM_9l6aHHfzNGWJjv0wqTCAqwSa32v8B-x8ofWedd4ezj6UqRW_e5RObX5bRNY8-NBFwdb_KTUZnOpcuu2qA5HXD7mLAagVsGA8sz3z-3MsK_m0G4-dI2bFbWzptbdxpoV_lH6Qsx1GUnL5Qycfur8_vBXv9PjAYcL1aCsipd2RcBTf9NMd5Lg1LiqRtc7Ijsd2k3Q3920m4vI0FPv0pe0g_fYkGRsMFj85FtGL5icyfW0vmxYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپل برای رونمایی از نسل بعدی سیستم‌ عامل موبایل خود آماده می‌شود. بر اساس اعلام رسمی، iOS 27 کمتر از چهار روز دیگر در WWDC 2026 معرفی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124970" target="_blank">📅 09:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124969">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کاتز: اسرائیل این آزادی عمل را دارد که با حمایت آمریکا در پاسخ به هرگونه آتش‌سوزی به سمت شهرک‌ها یا اسرائیل، به بیروت حمله کند
🔴
حضور ارتش ما در منطقه امنیتی شامل منطقه قلعه بوفورت می‌شود و ساکنان از بازگشت به آنجا منع شده‌اند
🔴
یک منطقه غیرنظامی در جنوب رودخانه لیتانی ایجاد خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124969" target="_blank">📅 09:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124967">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=JGpcVPbqY6IJ6gOy3Aps6Ofv-NIQ9xBGrX_ZHcaMhMPIHUvBbz_gxzi3LCHJ_90Dm23rzpNPhqKksF22DMH0GG6t1bINiBouVyxWLi4RvT5u9uGtfxspvv_huya4_uBL_S65RocTNd-jWO_taxZOxcsCFDMYDPnx-Nx4sbfiLto39pY56lQRcADzmaGLmi8y5eWqjvrz6JIlQZ8K3oMM2aIPZc2rpyE1T5qaAII3ULfOGoJ1wwmtFea3a2fd3eQOy07-qw4WWlVQhRPZklJLCdGkCe5dcD1hfbAdiY17Dkrws-lWD7mkpKLMP1Wk9h6mTwL3-75w0t1jaMFX5CAdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=JGpcVPbqY6IJ6gOy3Aps6Ofv-NIQ9xBGrX_ZHcaMhMPIHUvBbz_gxzi3LCHJ_90Dm23rzpNPhqKksF22DMH0GG6t1bINiBouVyxWLi4RvT5u9uGtfxspvv_huya4_uBL_S65RocTNd-jWO_taxZOxcsCFDMYDPnx-Nx4sbfiLto39pY56lQRcADzmaGLmi8y5eWqjvrz6JIlQZ8K3oMM2aIPZc2rpyE1T5qaAII3ULfOGoJ1wwmtFea3a2fd3eQOy07-qw4WWlVQhRPZklJLCdGkCe5dcD1hfbAdiY17Dkrws-lWD7mkpKLMP1Wk9h6mTwL3-75w0t1jaMFX5CAdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیده شدن دونالد ترامپ در یکی از پارک های شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124967" target="_blank">📅 09:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124966">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124966" target="_blank">📅 09:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124965">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رافائل گروسی» مدیرکل آژانس بین‌المللی انرژی اتمی در سفر به ریاض با «عبدالعزیز بن سلمان» وزیر انرژی عربستان سعودی دیدار و در مورد پیشرفت این کشور در برنامه هسته‌ای غیرنظامی ریاض گفت‌و‌گو کرد.
🔴
گروسی در صفحه شخصی خود در شبکه اجتماعی ایکس نوشت: «برای من مهم است که در عربستان سعودی باشم، زیرا ریاض در حال پیشبرد برنامه هسته‌ای غیرنظامی خود است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124965" target="_blank">📅 09:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124964">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کاهش قیمت نفت با امیدواری به آتش‌بس لبنان و اسرائیل و خوشبینی به پیشرفت مذاکرات ایران و امریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124964" target="_blank">📅 09:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124963">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت امور خارجه فرانسه با انتشار بیانیه‌ای همبستگی کامل پاریس را با کویت و بحرین اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124963" target="_blank">📅 09:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124961">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gtWtXOwjn-pWIWD36xqVZrt6qcrkvYjRzibAcISSSaxpk9uwSv27aXtTtcD8j6qMIy3Kmw-jjO9l42pUMdJQa0sT6jDkPkKTF30St1hh2QbYpiMUZdHf0ub-wCLhSY7cGDhn2gnLz0uv4UcUPOsZm4--L9XSJHdZSKzJChxDXrRoRIvm5i9DjvErHDyq1PyJjYUcPCsVpGFhGBxKtRByVZYq3c8hhdjjtOnDplpY397t-EA2Le4SuT2NubT8OYY3CO-Z4eFGx4DHcQmYbT4Vw0a8rNIvLZ75FQikbiZLyVr2kNZgNmJQTdlqnLu78Ke51B7HJM_i2gRXSzlq5evhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AqsVx4HC5Ggy31NtN9kakhj8d3rVlrT3UxcqhKKBgzAFjcZFn6npHtkuSOIfi6FXEFgBuLTRmzO8cyZVXc5_vfrN8hTfxx5ssfIhrZcJ3dij6B3oNsZtFCtRnhngW-MJ3louNnOT2c_pk2OBYjeXZ8VdFiuB8GtD3kBA0CqBErOWGDNqEbiPblclsBkZW-nAGCkoDZoJn7TyWAW5OfwU1Iam6hRprxDTdAE1b87R6LeE08qfE2UYyRi_5-Cn7Kw8_yJ9CeARA3u46hkiq2V68-62Mtp_35gi7C7fZS9dFJd7uGq_fjxhFvQv1o6IFmMur2AODnmKWQFgCOhdIDsJ4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا به درخواست نماینده تگزاس، واکین کاسترو، برای پاسخ به این سوال که آیا اسرائیل سلاح هسته‌ای دارد یا خیر، پاسخ داد.
🔴
وزارت امور خارجه پاسخ داد: «ما شما را به دولت اسرائیل برای سوالاتتان درباره توانمندی‌های اسرائیل ارجاع می‌دهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124961" target="_blank">📅 09:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124960">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
محمود قماطی، نایب‌رئیس شورای سیاسی حزب‌الله: تمام تلاش‌های آمریکا و اسرائیل با شکست مواجه خواهد شد.
🔴
رویارویی ادامه دارد و مقاومت در برابر تجاوز اسرائیل همچنان پابرجاست.
🔴
آمریکا و اسرائیل هیچ حقی در مورد سلاح‌های مقاومت ندارند، زیرا این یک موضوع داخلی لبنان است که ما در مورد آن توافق داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124960" target="_blank">📅 09:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124959">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بن گویر وزیر امنیت ملی اسرائیل:
آتش بس با لبنان یک اشتباه بزرگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124959" target="_blank">📅 09:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C394ezS25KYoCyzgQpSyFkq5AEQlW9VquyEh3sp8p2EwZEBwi2nweeLOciRpKXKEOZYheA2QM1hMq8CGdsjVBbekFrBoIdb5d1IT11d0dg2eV5J1AwZaHJBkQqUgWlqKx_gO47kyC_h5FZowmV0SW1N8OdZiilx4Xqwq8jI3FkZpJiIHzSfPoDuGG_OelNRcvpUqW46Wg0byC2BYR10DSbQMapMhT7ktN2KeKaMwt2Bl9fkkm1Rj7O_koe52XakRyhiNy7j1dpLLr9D_Mz4kW4ir5iIpPeGwUDx2yx3_l_rErd-QFMkEryb2Vkk6IQbVQkGdk34iiB9UlCuCFpb8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست در مورد مذاکرات ایران و آمریکا: هر دو طرف به آرامی به سمت توافقی حرکت می‌کنند که ممکن است پایدار نباشد. آنها طوری رفتار می‌کنند که انگار این توافق دائمی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124958" target="_blank">📅 09:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbYi6oBeZZ2JgRjpiY1BeHUX3n-5ol-CZg66wEDFDuShym2GTvBPXyddZMdOf5_VSaIxk7o5Q-zcobCOmjQfGbdXqVdLNTPq5-W-bamQayEiZ--ra79Xw3vYXm4xZx4oHNhVK2lBSQgF5sGtr0Xc7F14wJ4nD6QURU3qoReW8a6LUsASGoX0qm-Lzu7CcZ1wE9rnTq5NMqd-o2FU8XbVH_ghhMluivbJbCZSjFQs63NAaS6o_O_z_vBbAP2XcoVdatJBm50lsDN1elZkR0P4CMNwiw9BfWM07QYgH6w2-iBWukOmZ_4Bsst8qD-eJeGQ6KZElj8uyCr3CcgnTedZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز: همزمان با جنگ آمریکا علیه ایران و اختلال در عرضه انرژی، ذخایر نفت آمریکا به پایین‌ترین سطح از ۲۰۰۴ رسید و در صورت بسته ماندن تنگه هرمز، احتمال افزایش قیمت نفت تا ۲۰۰ دلار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124957" target="_blank">📅 09:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124956">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHeuKnXt_1VPmfR_sYwiqHaiEVnINcickdyUdmX3nLH13dMQwtWbtxAs9XB_iEivXkEv8syi3PvU3ckMO82voSOxYAtC0lGN6ILpb21CG2_IOyevD-LAG7WLgYfTfAjALh30suRxYTww9lXQSHvY_7YPXqfgtAKaTT2GDJB2XSpPgObBcUdoAqmnNSrqdlC5Gb5Bw4yqjSDIT7CaEPJJIWa0GtUz9SzX5GKAy5eJGHXm1Xoi9W0HOfh2L0PZ5NeTJTTOCUye-Z7rEsEUs8Dz8kwZLoR4d7Iondy1UkoOddZ9ckjzukeklIkj1wVUGucEFeZdP-xTarsejkzkAisZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین برای اولین بار از ۲۴ فوریه به زیر ۶۳٬۰۰۰ دلار سقوط کرده است
🔴
بیش از ۱.۱ میلیارد دلار موقعیت‌های اهرمی ارز دیجیتال در ۲۴ ساعت گذشته نقد شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124956" target="_blank">📅 09:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T07PDJGb6ceTGiqbW5am_0ajVKftxEuKafkGbthJTTN3Ll7nwT3V79Sw6DqCuDSPpjwGcBLRezhlBjwSKKpubgqiM-j1Nnxz3GiIojEz4pdGQLdonpaJEx-bhREhExt-RYTofLcLnuZDfn_CI7N14NqjgTWg4WSEprYlvu34R53P_yPeEkR5KY5N7dnaVUWvhI5MfM1edZAeWwSCuSjL7TIuPomHatrflZcVUcPwt4tFxQ_wg1HzwNdGFWXBERqXQk9tZDKlVCmykofYy8n2etm_BqSaJID2VHtigGTUnYLtF9IyUWhQxr9QlaRlzk00gs0pql8ASfZopcpx8c34Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: مقامات آمریکایی گفتند حملات مکرر تهران فشار بر ترامپ را افزایش داده و در مورد دوام آتش بس در درازمدت تردید ایجاد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124955" target="_blank">📅 09:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124954">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
معاریو به نقل از یک مقام امنیتی اسرائیلی: ما یک پنجره عملیاتی برای انجام مأموریت در بیروت داشتیم، اما بیانیه نتانیاهو و کاتس آن را بست.
🔴
ما می‌توانیم در صور و صیدا آزادانه عمل کنیم، اما بیروت تابع محدودیت‌ها است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124954" target="_blank">📅 09:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124953">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=sBZrt5VQYWDR3sMl4qeTuGtGZddvM1OvEo9FjF8Du1o4vgQ6KI3hQqAkyPPNjD4ESrfc9aJoR36iFd7AsQdL7Ebna4HmsW-d7_sOMoVlVZQkZdY09ZzIasQWut-PQCOIlvfKvq2cDUXU6ifwsj6INDi75pcvEwy50JJ7czUO71Ry4EhTBD6yxJ9p-aqnirhzy_1tMQgQ8ubb8d5ui1JTEMC4bmgdYwRkbDwTuKNzKy6Zs7DZpTmWWn9ux7PVgIvEnv0Ckn4h2a0FIOYEr8s0jJTtoHT67eMw6fMbi7XhjCh4Dk5urghILYogskxhcujsHK4GJMTRG65sGXH7Ed02OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=sBZrt5VQYWDR3sMl4qeTuGtGZddvM1OvEo9FjF8Du1o4vgQ6KI3hQqAkyPPNjD4ESrfc9aJoR36iFd7AsQdL7Ebna4HmsW-d7_sOMoVlVZQkZdY09ZzIasQWut-PQCOIlvfKvq2cDUXU6ifwsj6INDi75pcvEwy50JJ7czUO71Ry4EhTBD6yxJ9p-aqnirhzy_1tMQgQ8ubb8d5ui1JTEMC4bmgdYwRkbDwTuKNzKy6Zs7DZpTmWWn9ux7PVgIvEnv0Ckn4h2a0FIOYEr8s0jJTtoHT67eMw6fMbi7XhjCh4Dk5urghILYogskxhcujsHK4GJMTRG65sGXH7Ed02OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای با وضوح بالاتر از خسارات وارده به یکی از پناهگاه‌های پهپاد/هواگرد در پایگاه آمریکایی علی‌السالم کویت در پی حملات موشکی سپاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124953" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124952">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlgkAuNQ_lUwvPdsE-M7EVQJrE-OFYrVjP7DIuXmQG21F1F7oynbJfvK9wL9TcjCe_whUFiiUkFgTmL0Jng-bRz7CkEWxSiwOJvxGirLfW_Ln0DOWu_ux8RVeCK99wIlnMsg64Y8-ofrJ0Iho52hNNMpIzaTn5WoXoiEqVUWihpfo7jArspe27KhFwd5qQVXf3B08_9sDNdf7D4YcqiGOowcQiDMdR1kPxoBfUpDmVGqtAYTg4QiCRK1I9_ZTAr-dwwM5HmJrWc_IMRLSifPZdB8ls_aWQ3iTliTYe-sv_YL2Qzkp6XDUEUyedDAxk6F_Yb5683LLVYA423sczZxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲۰۰,۰۰۰,۰۰۰,۰۰۰ دلار از ارزش بازار رمزارزها در ۲۴ ساعت گذشته کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124952" target="_blank">📅 09:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124951">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سی‌ان‌ان گزارش داد ترامپ به مشاوران خود اعلام کرده است هیچ توافقی را که شامل ارائه بودجه مستقیم ایالات متحده به ایران باشد، امضا نخواهد کرد.
🔴
این در حالی است که بحث‌هایی درباره ایجاد صندوقی برای واگذاری میلیاردها دلار به ایران پس از دستیابی به توافق نهایی مطرح شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124951" target="_blank">📅 09:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124950">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
تصاویر مربوط به اصابت پهپاد انتحاری به فرودگاه کویت از دید دوربین‌های مداربسته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/alonews/124950" target="_blank">📅 09:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124949">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a81b6cc9.mp4?token=CIjW3VlmiBLSZroH0-uo4VqRmD41SF4ivLk4gCuk_UA0yztlJwhzDW_9EUn0X-z8uw85U5G5kJEUFJP5WHTs--vPSaZ6GtJHC1nufmpzLvFBZVj1XqSodBgvm_8qrxw0GGgssx7AFMkDd2rmIOfp7XZnjtJGF-s9VBMLGGlbg__nk8GZGIB58etiZxFs-EX5BC-Dauj98k527WEzbWnMY63wl40TPA0SIvTFl8TDhdo18h9pUsXD6R5kejLRbScuRPXgVyd6lxY5GTV3MgbBe3-0jM_jp-GjqAOBpHEK-dXKxVx6XDqAIlr6CXjK_blA328eeEpjyjYb_kPCdwxIiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a81b6cc9.mp4?token=CIjW3VlmiBLSZroH0-uo4VqRmD41SF4ivLk4gCuk_UA0yztlJwhzDW_9EUn0X-z8uw85U5G5kJEUFJP5WHTs--vPSaZ6GtJHC1nufmpzLvFBZVj1XqSodBgvm_8qrxw0GGgssx7AFMkDd2rmIOfp7XZnjtJGF-s9VBMLGGlbg__nk8GZGIB58etiZxFs-EX5BC-Dauj98k527WEzbWnMY63wl40TPA0SIvTFl8TDhdo18h9pUsXD6R5kejLRbScuRPXgVyd6lxY5GTV3MgbBe3-0jM_jp-GjqAOBpHEK-dXKxVx6XDqAIlr6CXjK_blA328eeEpjyjYb_kPCdwxIiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض به حمایت آمریکا از اسرائیل در جلسه استماع وزیر امورخارجه آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/124949" target="_blank">📅 09:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
العربیه: ایران و آمریکا به توافق موقت ۴ مرحله‌ای نزدیک شده‌اند
🔴
از تثبیت آتش‌بس و امنیت در تنگه هرمز تا کاهش محدود تحریم‌ها و سپس بحث غنی‌سازی اورانیوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/124948" target="_blank">📅 09:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124947">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkYFKnZBOI09B_29-IFQ23cUOCbvx6WWay4fowzwQqoSDrYBxFtMX4zlSmuIiPvptfazYt5HaelMyI5Ep3DyHD-6U3SoRKM60pbeaPNVbEyiUmKPNn838P0S5Iq5wX16B_ZD_fWTeflLbsHum5EtpM7dj4HNxEZLwep8Sz6B2fKVouDV6JUq22DZ3A76jmbghviT5CbNZEOvoEp26ISPcTqg392rJJBYZ-_Ff4pOekVhn-Vj83cMRVsVy4RTHlXZMBYOCslk6erK_4WLEX3SRSUdvBj2Hd-bixskinBC8izbQeiHOfGU2_VFIirTYusz1dE2o3aqLDQAtJQHaq0Cpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: کمک امام زمان باعث شد جنگ ۴۰روزه رو ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/124947" target="_blank">📅 07:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124946">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81fe9bbd02.mp4?token=NUorB3T_uoUJW84pFiEYcC-d-Tm3Fyfhlw3gHGdKN9FxIN3NSOP0CVKgG5V_mEQhmfaSQSZkcTokmfaCxM9bNS3iDQ9Ai1E7h78zc8Qt_1QL-lrhzZIJIjMmEX0NtpkBOu51KWBv0T-iXNPiMjtiozDw6We9t_wYDA6MAiJLx0HBLHJJqrI0FpgUHYTI3FDGrXss0XTUaj0Bp-OSaIl1Efrz-TwPwBf3EDGyGdz7jaVIwZzR7mumMwULLOu3AtzfXvVPIHDxXcIQ_UbYej11XcCItJ-BWxA14V7DCo_2LuTl7ppBJ0qcNZEx0rFZftSuVXlUv5YuKiYC74LwVw5vpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81fe9bbd02.mp4?token=NUorB3T_uoUJW84pFiEYcC-d-Tm3Fyfhlw3gHGdKN9FxIN3NSOP0CVKgG5V_mEQhmfaSQSZkcTokmfaCxM9bNS3iDQ9Ai1E7h78zc8Qt_1QL-lrhzZIJIjMmEX0NtpkBOu51KWBv0T-iXNPiMjtiozDw6We9t_wYDA6MAiJLx0HBLHJJqrI0FpgUHYTI3FDGrXss0XTUaj0Bp-OSaIl1Efrz-TwPwBf3EDGyGdz7jaVIwZzR7mumMwULLOu3AtzfXvVPIHDxXcIQ_UbYej11XcCItJ-BWxA14V7DCo_2LuTl7ppBJ0qcNZEx0rFZftSuVXlUv5YuKiYC74LwVw5vpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه برخورد یک پهپاد انتحاری به فرودگاه بین‌المللی کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/124946" target="_blank">📅 07:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124945">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnfOmyVBuFWADmPWlnZRgYdk8yY22QZdzEkZ9F6AXfA3KC8t-wKTyHm8MQNQJIMnEkUoSDQkQs6LwQyBb2szKgrtRi5zOct9tiRoVDnNONbiG60IRXrOKQq-BSeKwchy9gkQ47RsdgRF70cSiD-1n2h2Rz8zGhxL55odqOPx4rTc3mHPdNeVwX2saarxcx1xSO-GW_V01xvHSTrLAp0ZmkwoLCL2k_O616hPVTgpY8IJVA5-dppn52XBlmpaxyeFAYfowRxfggwMnOKENjKErM5ndnthqT2BebI1kA71MJlui5YuytFca0Cp-8v9Cw6MTVsNcqNaI90JzRorw8p8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
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
📈
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/124945" target="_blank">📅 01:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124944">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
🔴
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
🔴
با این حال، این اولین رای موفق…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/124944" target="_blank">📅 01:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124943">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=eWIoljRCFdvogsGgg78wu_2zQ9LJ9eJCsouh6IIWlATyZsml6iJeAMAW5qGfWsnQBYT6TTn9QAN4Muok_zYvF-FAVyAAB9rnBv27MTrRO6EyLxWFvbRyF0kH5qlMCnEOiI_aTfpUtLdnm1VrOpmoxrC2YR-Xuj6OQvzKF5_A0q6mnD32xGJY2xqeL8EXhFb7-qPNjg6M6efuRVSFHCnVv5HSHTHOncfdrfTJJJ37X1nEthmF_E-ehqzauQWOygQVlhDIVtUnSCRq4C6Bpz_1mtQM9NW1f2z91w_sDAZpK4aTlkwClDnpMq5ZmPLHwav522dtG7BpfzoP4GTDXrKYIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=eWIoljRCFdvogsGgg78wu_2zQ9LJ9eJCsouh6IIWlATyZsml6iJeAMAW5qGfWsnQBYT6TTn9QAN4Muok_zYvF-FAVyAAB9rnBv27MTrRO6EyLxWFvbRyF0kH5qlMCnEOiI_aTfpUtLdnm1VrOpmoxrC2YR-Xuj6OQvzKF5_A0q6mnD32xGJY2xqeL8EXhFb7-qPNjg6M6efuRVSFHCnVv5HSHTHOncfdrfTJJJ37X1nEthmF_E-ehqzauQWOygQVlhDIVtUnSCRq4C6Bpz_1mtQM9NW1f2z91w_sDAZpK4aTlkwClDnpMq5ZmPLHwav522dtG7BpfzoP4GTDXrKYIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
🔴
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
🔴
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
🔴
چهار جمهوری‌خواه به نفع آن رای دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/124943" target="_blank">📅 01:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7_xGl3XriRBgqLdzyF5uLWbVV8ZfWUijJGd_IBkvsZ_h1YZtNhn48E58gylGNONO-NPEvHUpimAxK5Q-cktTIQ22o6T2KYPj_JeJL7KVcVA9ujR0LVa6fBOO8OypFFjcu04DEoDm05Bo1DfpJI4QjCSerlyBjbJtte60g6pe_6tlI7OZjbvDHuUveOLr3Hb7lE8Z57hWSAm5aUmKECGHAdAAqciI6qreUXGxBXiCnVqXCiYkaXEK3bOOvAfmY8OQgmhnUb6d_Z0dmjI5HWwsdUiMb8VDOSLXrOm6JbwDFfKI1PEZSkh4tU11kK7wLwoy2g4KH-xTzKcjWxniFFr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
🔴
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
🔴
‏ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/124942" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=E1YfsBl1dYRT-FOzJRGAPUtJpO7Ww7mhJhlSebsoiGf1bpAliVuVz-BileomoJ1xHK5slzQHP9T5qb6Yt0C4p4Wb8rB1KvG4SIspkDyVcbJsmzXlme4OH2q8Z0UH9BdJPgHeWVb_2URFPRu7EEKeCAkOGN5EOuIwkv4MBMRAHeyi-w2do7sfRxo-Y3_LfkiMt3NlHUKwqme2d2prI3bLpoViJdmnxKXHa09xWEVB5dVctmNrhPblMl7H7LsV6Jq2HoFQ6pubq5u2bB9tRF-YTvAz2GJpn6ZqDNiyZKRE-wPhsnGRcX08CudkEr01TR4ug-k7Om_5vyJf8rB4GX2-4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=E1YfsBl1dYRT-FOzJRGAPUtJpO7Ww7mhJhlSebsoiGf1bpAliVuVz-BileomoJ1xHK5slzQHP9T5qb6Yt0C4p4Wb8rB1KvG4SIspkDyVcbJsmzXlme4OH2q8Z0UH9BdJPgHeWVb_2URFPRu7EEKeCAkOGN5EOuIwkv4MBMRAHeyi-w2do7sfRxo-Y3_LfkiMt3NlHUKwqme2d2prI3bLpoViJdmnxKXHa09xWEVB5dVctmNrhPblMl7H7LsV6Jq2HoFQ6pubq5u2bB9tRF-YTvAz2GJpn6ZqDNiyZKRE-wPhsnGRcX08CudkEr01TR4ug-k7Om_5vyJf8rB4GX2-4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌ای آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در ۱فروردین
🔴
موج انفجار رو فقط ببینید
‼️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/124941" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124940">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=VpELlh7SJeZtus8OWdq5aONNHqbutsep-BcMtGgBrYEX6jL9BlxMcTmeTA0ADABkBK3SDC3z20VG01VHfSyGNE4l81S12R8gNlPYz5MOIHZM_wSXDzTyQ4-jdTUFOFgJt6wqTy-IABlgkY8Py0cZOoBOkftmXF9ff3F9dpKiMBvX7JVmu2G5_xniz7-K78R_5EXeI4dgNkE9kp2CTIiRLTLtPuQgNhEtiZV1wXAc3Kuq1wfjqVji66IPo3SQNFk9m9nnbvktIOdx-B1iPN0JMyrvGVicJVHLb64pndB6Bw2Pc2q_Xso_jn2EAtqZ81i33rk_4Ub1lKjhZsgH-UITfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=VpELlh7SJeZtus8OWdq5aONNHqbutsep-BcMtGgBrYEX6jL9BlxMcTmeTA0ADABkBK3SDC3z20VG01VHfSyGNE4l81S12R8gNlPYz5MOIHZM_wSXDzTyQ4-jdTUFOFgJt6wqTy-IABlgkY8Py0cZOoBOkftmXF9ff3F9dpKiMBvX7JVmu2G5_xniz7-K78R_5EXeI4dgNkE9kp2CTIiRLTLtPuQgNhEtiZV1wXAc3Kuq1wfjqVji66IPo3SQNFk9m9nnbvktIOdx-B1iPN0JMyrvGVicJVHLb64pndB6Bw2Pc2q_Xso_jn2EAtqZ81i33rk_4Ub1lKjhZsgH-UITfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهبازی مجری محبوب صدا و سیما: من سالم هستم و خبر تجاوز گروپ به من کاملا کذبه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/124940" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124939">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an7VQgJUC8Noo58sJK16w65UljH10OkxIv-Ipdw7IzJ9FYTcitHFzqkfD7bcSCxUdidvFb13aYfSFXD5tOm070Dh8__GIoxjc-dM06LbwTXMbED7o1edERz0B6gjuMyP2uzprW2thhCu9QPyio_7iVxHliVUlPWizhbMSiJVlasMtIMvwCfBa1t8mK0PRTgSowRCsUqQCF6FF7gPOQItallcTViHpKBUxTCma-058dA9fRgaRIenJ8n6XbRidIUNejNB7xE2_Oz02nf-mMzduDolridPQU9fm_6THQzLmiSxcdjzWCkdSz8EvDCY2g3VeFbrHfgCkilM1kKvNEW2lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهبازی مجری محبوب صدا و سیما: من سالم هستم و خبر تجاوز گروپ به من کاملا کذبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/124939" target="_blank">📅 00:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56e67aaa9.mp4?token=p4254DKcfoKgGBQwa2UKbf-_C7TDyq0u5SZj7C8W-tGQ_ndvtu6boJnJKzGhEfRmf_IQlrYfA-FWvkHI3DU-LutyqshjCyFEnqgk-jo2MiBWiEBHR-5k8W1bWcpmJhsR0S77OIxBbnH_HJIb01PVaKx4CHJhhwIDyt4YWv5fAPa9ZwpHIiqo-osY76N4YksQILJXUt191NblA5rLmrhop3cbPMA4X5ufn8UJU6KYNL8IHcwA98oNh0MNFicYR5h2qkBj59ETwhZmL0X2hpgsdYUM9gABKYhGguTW4vcIZMr1fJ2HdEiwudioIDx7qjW_hlZk34jAzhgxPmAgewWzdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56e67aaa9.mp4?token=p4254DKcfoKgGBQwa2UKbf-_C7TDyq0u5SZj7C8W-tGQ_ndvtu6boJnJKzGhEfRmf_IQlrYfA-FWvkHI3DU-LutyqshjCyFEnqgk-jo2MiBWiEBHR-5k8W1bWcpmJhsR0S77OIxBbnH_HJIb01PVaKx4CHJhhwIDyt4YWv5fAPa9ZwpHIiqo-osY76N4YksQILJXUt191NblA5rLmrhop3cbPMA4X5ufn8UJU6KYNL8IHcwA98oNh0MNFicYR5h2qkBj59ETwhZmL0X2hpgsdYUM9gABKYhGguTW4vcIZMr1fJ2HdEiwudioIDx7qjW_hlZk34jAzhgxPmAgewWzdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمعات شبانه تلفات داد
‼️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/124938" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124937">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/124937" target="_blank">📅 00:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124936">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6d857c4c.mp4?token=soza4Tiz87uOvs0qLsShDAJ5-r4gnBadI4VjAaLKNI3oBTAEouLcbE8qtEbujjU9kMNvdJkp64el6G8Nx5JZ2-TkoFipoX6aa26wIVWWterJr43asaF7ovTwXSIDgSWWhCZdSEHbA_HtRgmdV8pFcjfuiAtZO4PYPLrqYMWT0pg4AwkcmP1uJKk5eKlArvzKvcoI3uwb25cFE7nN0fWkVZ_8KC0P0wP70VrWkMf9NBrb8AkBIxHPcnVJutkCcYxxhjzSE0N6Hcd6QBy6BCawEng1K5HSvWnargcaWw_LLowKQ3Os2BFbXasHafa5GE8qoXhpOaBR_a1g6cY5v0yFCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6d857c4c.mp4?token=soza4Tiz87uOvs0qLsShDAJ5-r4gnBadI4VjAaLKNI3oBTAEouLcbE8qtEbujjU9kMNvdJkp64el6G8Nx5JZ2-TkoFipoX6aa26wIVWWterJr43asaF7ovTwXSIDgSWWhCZdSEHbA_HtRgmdV8pFcjfuiAtZO4PYPLrqYMWT0pg4AwkcmP1uJKk5eKlArvzKvcoI3uwb25cFE7nN0fWkVZ_8KC0P0wP70VrWkMf9NBrb8AkBIxHPcnVJutkCcYxxhjzSE0N6Hcd6QBy6BCawEng1K5HSvWnargcaWw_LLowKQ3Os2BFbXasHafa5GE8qoXhpOaBR_a1g6cY5v0yFCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آلمان برای اولین بار در تاریخ مدرن خود در کسب کرسی شورای امنیت سازمان ملل شکست خورد و تنها ۱۰۴ رای دریافت کرد.
🔴
به جای آن، پرتغال و اتریش انتخاب شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/124936" target="_blank">📅 00:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124935">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
منابع العربیه: پیشرفت‌هایی در مذاکرات لبنان و اسرائیل حاصل شده است، اما هنوز توافق دائمی به دست نیامده است
🔴
اختلاف بر سر سلاح‌های حزب‌الله همچنان مانع اصلی هرگونه توافق بلندمدت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/124935" target="_blank">📅 00:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124934">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ: ما طبق توافقی که با ایران در حال مذاکره است، ذخایر اورانیوم با غنای بالای ایران را دریافت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/124934" target="_blank">📅 00:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124933">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31569798c8.mp4?token=nFG3CMRfVV23D3Z6otSGCGBtfVpm1NgUX8gKm5NEwE9q6c1JaOdTzGW8BOzl8Tl2EWoFeHcQRywZxwlj-4pQgo0rRG0-5NLpEZ7V6brXWSpCf0TPkVDmHTrsEV1CrWTlA7v3Wo7_u6sOOwbU7VmxaRaHgaZGUiihbEi5YszTZVD3pah9cJ0EEDchH_3nIcsEnLOrbtoga0G9caRKE9VcUcPb4e_pACbAMSjGuwZTeOiYCOqP-ioRuGq6_cMGc2daZQdTbpnjYvSR2RqtbCLh0bKWiqkeISsnYvGL0oF-5UhF-To02c42oQhmSCBeaj0GY-m_qctI3u9EdY3zCB4opA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31569798c8.mp4?token=nFG3CMRfVV23D3Z6otSGCGBtfVpm1NgUX8gKm5NEwE9q6c1JaOdTzGW8BOzl8Tl2EWoFeHcQRywZxwlj-4pQgo0rRG0-5NLpEZ7V6brXWSpCf0TPkVDmHTrsEV1CrWTlA7v3Wo7_u6sOOwbU7VmxaRaHgaZGUiihbEi5YszTZVD3pah9cJ0EEDchH_3nIcsEnLOrbtoga0G9caRKE9VcUcPb4e_pACbAMSjGuwZTeOiYCOqP-ioRuGq6_cMGc2daZQdTbpnjYvSR2RqtbCLh0bKWiqkeISsnYvGL0oF-5UhF-To02c42oQhmSCBeaj0GY-m_qctI3u9EdY3zCB4opA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : تنگه هرمز فوراً باز می‌شه وقتی من یادداشت تفاهم رو با ایران امضا کنم
🔴
تنگه هرمز باز خواهد شد، مین‌روب‌هامون اونجاست
🔴
زیر آب هستن، خیلی خوبن، تکنولوژی‌شون فوق‌العاده‌ست
🔴
ما مین‌ها رو جمع کردیم، بیشترش رو پاکسازی کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/124933" target="_blank">📅 00:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49eac4e09.mp4?token=Q5EAQa_9q771TWUENhGx58Wz3tsODwgDjTkPuKORHMYUeS6BAir5zuD0ZA8Um-0HIbisf-UzsX2iIX6Emwf6Btp4uHuTdz-eVi-Fsm-Frj63GiBjOifS_Sphtmk3oazLO9M1mXGpFRwgSVVoSN0_s9DcrU94pkcigSt2Zfxa2UMPeI78spy5sFfx847Nbu5LRStmpO45f5d-VtuxAO5ztPJEKRQcBfD0hGCcKS1HTbjbBj5SjW-WI5kry2epi9faBw_yQCIDhqjgzyp0MM8a3qITl0i4TA-vGAksz2XEXW-F41L2r4nmzl8lZAAsiAfdwxan3SwjF6bkEeGxVjcntw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49eac4e09.mp4?token=Q5EAQa_9q771TWUENhGx58Wz3tsODwgDjTkPuKORHMYUeS6BAir5zuD0ZA8Um-0HIbisf-UzsX2iIX6Emwf6Btp4uHuTdz-eVi-Fsm-Frj63GiBjOifS_Sphtmk3oazLO9M1mXGpFRwgSVVoSN0_s9DcrU94pkcigSt2Zfxa2UMPeI78spy5sFfx847Nbu5LRStmpO45f5d-VtuxAO5ztPJEKRQcBfD0hGCcKS1HTbjbBj5SjW-WI5kry2epi9faBw_yQCIDhqjgzyp0MM8a3qITl0i4TA-vGAksz2XEXW-F41L2r4nmzl8lZAAsiAfdwxan3SwjF6bkEeGxVjcntw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اگه توافق ایران نتیجه بده، شاید مردم بتونن شروع کنن به ساخت آپارتمان‌ها و ساختمان‌های اداری تو ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/124932" target="_blank">📅 00:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124931">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ درمورد ایران: ایران یک مشکل واقعی برای جهان است و نه فقط برای منطقه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/124931" target="_blank">📅 00:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124930">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7717fa1eef.mp4?token=nRvoe0CmRpcCLm-o4o_rwcUr7klo6_Xo-bpumsmTV0qqy_dY2KuCjlcq4_FUomi6ikyTV7t-1dB2omVTYzNyt2PVgC2CQuVzNEdlE2CClJevGVVVZsjQcBiOazkBwWbixWQqwoirrTs6FQ4nnu9U6gaSXHjqv_-3hC4Zpzz0Z7-xem2OzcuJMAZHdEbQGQLguK3VNcVM1GSjYFQylucBHTtFJAVmC2h3W27narJRG4FgAI0PVxVHLaTCzkhwSQUKPVliDp3MPzK_KCxriRnscivxtA262C9c54BVA0tSVgaABM9FG3UUzunoXmmARPYN35zVjGHU8Uslz0eR3esjSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7717fa1eef.mp4?token=nRvoe0CmRpcCLm-o4o_rwcUr7klo6_Xo-bpumsmTV0qqy_dY2KuCjlcq4_FUomi6ikyTV7t-1dB2omVTYzNyt2PVgC2CQuVzNEdlE2CClJevGVVVZsjQcBiOazkBwWbixWQqwoirrTs6FQ4nnu9U6gaSXHjqv_-3hC4Zpzz0Z7-xem2OzcuJMAZHdEbQGQLguK3VNcVM1GSjYFQylucBHTtFJAVmC2h3W27narJRG4FgAI0PVxVHLaTCzkhwSQUKPVliDp3MPzK_KCxriRnscivxtA262C9c54BVA0tSVgaABM9FG3UUzunoXmmARPYN35zVjGHU8Uslz0eR3esjSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:در آن بخش از جهان، آتش‌بس زمانی است که شما به شکلی معتدل‌تر تیراندازی می‌کنید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/124930" target="_blank">📅 00:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124929">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: توافق فعلی، در صورت حصول با ایران، نقطه مقابل توافق قبلی امضا شده توسط اوباما خواهد بود.
🔴
محاصره ایران شاید شدیدترین باشد و نتایج آن بسیار قابل توجه است.
🔴
این توافق مورد انتظار مانع از دستیابی ایران به سلاح هسته‌ای خواهد شد و تنگه هرمز پس از امضا به سرعت بازگشایی خواهد شد
🔴
می‌خواهم موضوع بازگشایی تنگه هرمز را از خصومت‌ها و تحولات جاری در لبنان جدا کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/124929" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124928">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: سی‌ان‌ان یک سازمان بسیار فاسد است، با یک خبرنگار فاسد که درست آنجا ایستاده است. هرگز لبخند نمی‌زند. زنی جوان و زیبا، هرگز لبخند نمی‌زند. من هرگز لبخندی بر صورتش نمی‌بینم. او را می‌بینم که با نفرت در چشمانش ایستاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/124928" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ: آتش‌بس در لبنان با آتش‌بس در سایر نقاط جهان متفاوت است
🔴
اگر توافق کتبی امکان‌پذیر باشد، ما آن را ترجیح می‌دهیم.
🔴
ایران موافقت کرد که ما وارد شویم و اورانیوم غنی‌شده را بیرون بیاوریم اما سپس موافقت نکردند.
🔴
نیروهای ما آماده‌اند، اما بهترین گزینه رسیدن به توافقی با ایران است که بدون کشتن همه، به همان نتیجه برسد.
🔴
ما برای اولین بار با حزب‌الله صحبت کردیم و آنها موافقت کردند که به اسرائیل شلیک نکنند
🔴
ایران علاوه بر اسرائیل، به ۵ کشور در منطقه موشک پرتاب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/124927" target="_blank">📅 00:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها به امضای اسناد نزدیک هستند. اما برای رقص تانگو دو نفر لازم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/124926" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ : شی‌جین پینگ برای چین خوبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124925" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124924">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=KxKm-P8OvTsJ9N61YQ4ojCY7BymYflMITtVQZRcpYwwp4m09jYu_id3YEi09eNQsWJepwD4pjp1Wtg2tEFat4v6vPok4cax3H9R2h-5CyW-rJIRd5MfvscXZcNcYW-FvQyo6RDr-K6OgQwIlNDQvF3um01Z-UbZHJAAn5Kh_x6Sd9pzxX5Dr8H9zlmyM6-0W4q97icz6iqMZUxKk5RTgrW5JZaCMozETKmWTOePA_qX85xSQngwJMDF3fkDs9LTAeFERVoPv0rnuIMt-oYswO0uE91GGnHGhj4ZLETy4bgh8486-po3oxdz1hHZeZKW3Gfx-GsuD9rO5Id8m-KoWNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=KxKm-P8OvTsJ9N61YQ4ojCY7BymYflMITtVQZRcpYwwp4m09jYu_id3YEi09eNQsWJepwD4pjp1Wtg2tEFat4v6vPok4cax3H9R2h-5CyW-rJIRd5MfvscXZcNcYW-FvQyo6RDr-K6OgQwIlNDQvF3um01Z-UbZHJAAn5Kh_x6Sd9pzxX5Dr8H9zlmyM6-0W4q97icz6iqMZUxKk5RTgrW5JZaCMozETKmWTOePA_qX85xSQngwJMDF3fkDs9LTAeFERVoPv0rnuIMt-oYswO0uE91GGnHGhj4ZLETy4bgh8486-po3oxdz1hHZeZKW3Gfx-GsuD9rO5Id8m-KoWNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آتش‌بس رو چطور تعریف می‌کنید؟
🔴
ترامپ : تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/124924" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae195d9e59.mp4?token=eudwsyv2bAmbEzNZTlZ7dY-398AhoMUNVNIWSsoH2rb9DqhfPgjZ5Hra0WRoN-bAKisan7bTPpyySzHQPg3IK0TvplzPVKYClSW_fob3geO-CCq9nCUeyK8uWk1YKknPp1YqLiqQQQwf1PfUal6PQnabW4Wj83AX4fBTLYLIVPwGr3TRSwdOsAawWs4clVJGWJNV-Dhb5DkBon8h6BXCf4QpMC1A8YrN8SPsuBfPO2cLuK1F76k_EDRS_nlo4i8ZzB5-fPCszrT1DclyQuTN8bpjEaB1xnDWTBTnz8PE2rBox3AYH-e5ah43zEuuqGflkP_N2eDkZxqEmax7VLwcEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae195d9e59.mp4?token=eudwsyv2bAmbEzNZTlZ7dY-398AhoMUNVNIWSsoH2rb9DqhfPgjZ5Hra0WRoN-bAKisan7bTPpyySzHQPg3IK0TvplzPVKYClSW_fob3geO-CCq9nCUeyK8uWk1YKknPp1YqLiqQQQwf1PfUal6PQnabW4Wj83AX4fBTLYLIVPwGr3TRSwdOsAawWs4clVJGWJNV-Dhb5DkBon8h6BXCf4QpMC1A8YrN8SPsuBfPO2cLuK1F76k_EDRS_nlo4i8ZzB5-fPCszrT1DclyQuTN8bpjEaB1xnDWTBTnz8PE2rBox3AYH-e5ah43zEuuqGflkP_N2eDkZxqEmax7VLwcEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : با توجه به حملات ایران به کویت، آتش‌بس با ایران هنوز سر جاشه؟
🔴
ترامپ : ببین، برای هر چیزی یه دلیلی هست. ما شب قبلش بهشون حسابی ضربه زدیم، حتی دیشب هم همین کارو کردیم.
🔴
(بقیه حرفاش به خاطر مشکل صدا قطع شد)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/124923" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: ترجیح می‌دهم ایران را نابود نکنم، ما میتوانیم ۲ تا ۳ هفته دیگر ادامه دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/124922" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ: پریشب و دیشب به ایران حمله کردیم، ضربه خیلی محکمی به آنها زدیم
🔴
شنیده‌ام مذاکرات با ایران خیلی خوب پیش می‌رود، اگر توافقی با ایران حاصل شود، می‌تواند آخر هفته انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/124921" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJ5ZfBj_xWSxM0nyw06ntTauAxGD8ybUxm6C6C4Xqqc996Dx7CVHN0helTeqJoUAcaDzdr8N6-MNoqjoW9_9y8TEzizGS6pTPDqekckXqZEnwDeG4YcPsq8yCTL-c5AYC32g57duynDBQdjDUehdy9ol3RkMgXOFuSw_ij1QQI7hRDRZ6DRqEx4fg09REZgXxBtEEhE5jblGe-W5X44vOiFt6hEB77u1xP1MFCH1lLE4TMEvh5wZrhiClv8jD5OvblylM6f_HxihMIsWk9AZqa6sb6Vcdd5DfhpKkVJmXQn7eOr6I24absHntx4HQ-XmPljCp15K9ZT_yReoXuk70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتریوم به زیر 1,800 دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/124920" target="_blank">📅 23:41 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
