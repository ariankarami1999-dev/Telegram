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
<img src="https://cdn4.telesco.pe/file/Zc59DGjKvjKPqgoDuwBZ6LUHyvOni_NdBSyfsIGvKDcMmpRaHXMSH1XLzcbSyIbUr4y-bK8hPBOjdB_fmB8gzt2c3usFCZTipSoXR4OMfzTm3iwf-xMcy69PPqEALQomC9QfIS_HBoMO4ikFS1C6966n6vURoqR7XiO2nseGq1kk0RQhZ8ihOs1EVD9ka7SwqoENhZ4rhGQ7VtMLpSgTWazR9zgXWm9jpsgNgepF8O5_vFGUQg2BqzYRXKN1EsnOIzHo1DzOaD6gpfx4bfQTLqEON4XUt8Ezs8f67Pa4ngR1g4Ab-e8sIhZuQ2slBJlS0theIccWK305kfcBjYQVJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 01:41:10</div>
<hr>

<div class="tg-post" id="msg-459838">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a820bfc659.mp4?token=AkIglIyKx_v96cvaetnfEwMVqBrs1YignukLOxN56sebAO8ifSu5IXpwO6tMun_8jw3XwkBpzAQtt7IkzjByI5GwYlnJzOT3zL0-5vicj1XJcGe3pf3kUDLdhx72jMNWkftme5D-VidV5CMYEHRBgcGnxZshS0BmZLS7E8yTx8HIOi5uoPETH1LTzHRpiRIx4sPa_IpI2UXWsXwdZHayyFKM0V0A6VC23xUU7lUHay2Lkj-XW4xVYhB2LB_m0YNTlEhfxMx81Rn07X8Lyq2tEc1OMphu6csTwvrLvWciO6eS-1t-6HJjm_6P2bkUV-pHp4fbxftEfnNrVjpvyUp3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a820bfc659.mp4?token=AkIglIyKx_v96cvaetnfEwMVqBrs1YignukLOxN56sebAO8ifSu5IXpwO6tMun_8jw3XwkBpzAQtt7IkzjByI5GwYlnJzOT3zL0-5vicj1XJcGe3pf3kUDLdhx72jMNWkftme5D-VidV5CMYEHRBgcGnxZshS0BmZLS7E8yTx8HIOi5uoPETH1LTzHRpiRIx4sPa_IpI2UXWsXwdZHayyFKM0V0A6VC23xUU7lUHay2Lkj-XW4xVYhB2LB_m0YNTlEhfxMx81Rn07X8Lyq2tEc1OMphu6csTwvrLvWciO6eS-1t-6HJjm_6P2bkUV-pHp4fbxftEfnNrVjpvyUp3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما به انتقام خون کودکانمان حساس‌تریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 967 · <a href="https://t.me/farsna/459838" target="_blank">📅 01:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459837">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تداوم حملات صهیونیست‌ها به جنوب لبنان
🔹
المیادین: ارتش اشغالگر رژیم صهیونیستی بمباران بزرگی را در شهرک کفر تبنیت در منطقۀ نبطیه انجام داد.
@Farsna</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/459837" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2NqtFXaV_Xib1tZFfxtpphs5Kxqesc2bn8pyBAaFxnWTF3T2wWpR5mx1ipAAWNUeKScawi3PTCIKeaqYAELS908LBHS7jz0sZxJLmzfkBul4jPYpEq3YPTX8RHpmX9UInIAJywQZkID90yI56bKqsTmeJctCvpq92CwFduT31wKWvHnt7_el0PT_rxvKCYLsdILfWTgBw3xyS2ZdaGalYuV4KQuYO1N3R0pVDXxJtyo2D8GzPnL6Q5KKKAfGbyDT0K8hz9uR-aAG4ooGbAguwoS-bZTr7lYQwpQsCK6SDORAO-ng-aSk4GaCnDYJP61bbwJOGZ8txZ9BGL0CmDzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصیحت زاهد
🔹
محمد بن منکدر، از عابدان مدینه، امام باقر(ع) را در هوای گرم تابستان درحال کار کشاورزی دید.
🔹
او با خود گفت که چرا امامی با این مقام خود را برای دنیا به زحمت می‌اندازد؟ تصمیم گرفت برای امر به معروف و نصیحت، نزد امام برود.
🔹
محمد به امام نزدیک شد، سلام کرد و گفت: «اگر در این حالت مرگ به سراغ شما بیاید، چه پاسخ خواهید داد؟»
🔹
امام باقر(ع) دست از کار کشیدند و فرمودند: «اگر مرگ در این حال به سراغ من بیاید، درحال اطاعت از خدا مرا یافته است؛ زیرا کار می‌کنم تا محتاج دست مردم و امثال تو نباشم. از مرگ زمانی باید ترسید که انسان درحال معصیت و گناه باشد.»
🔹
محمد بن منکدر با شنیدن این سخن متوجه اشتباه خود شد و اعتراف کرد که می‌خواسته امام را پند دهد، اما خودش پند گرفته است.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/459836" target="_blank">📅 00:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5199508d6.mp4?token=G1Emqv9M48yOFWfmv5kQKeBRCGo7S7PfxBGe-V2cvmDEnhs-q57mPVWi4AsL_U0tKzKkrLMR1YXkM7PlkIvwDI9IAAc25dj7L118ZoicAOedhQoxhoLcM92KFPavUSmMW5NuH4-LEH4Fmm1L6QDvy60GyBfAdH4ES5UdON4EhmhR3yBcbTj_y0cCK-DxylemX9dKzt1IqlwMJtnTAlX3oj4YVcp3bUskwiw1GlnkSSGxm8B7SVumpjEWbsjtLITYE_KRUQ51F-gjZV2-9AuqqUqIScD7afmimlBKwNHdQO48THgGJWzfd5RKVvqtYHquSicH7iSRiczOJqXBtO-qcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5199508d6.mp4?token=G1Emqv9M48yOFWfmv5kQKeBRCGo7S7PfxBGe-V2cvmDEnhs-q57mPVWi4AsL_U0tKzKkrLMR1YXkM7PlkIvwDI9IAAc25dj7L118ZoicAOedhQoxhoLcM92KFPavUSmMW5NuH4-LEH4Fmm1L6QDvy60GyBfAdH4ES5UdON4EhmhR3yBcbTj_y0cCK-DxylemX9dKzt1IqlwMJtnTAlX3oj4YVcp3bUskwiw1GlnkSSGxm8B7SVumpjEWbsjtLITYE_KRUQ51F-gjZV2-9AuqqUqIScD7afmimlBKwNHdQO48THgGJWzfd5RKVvqtYHquSicH7iSRiczOJqXBtO-qcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوجوان پیشوایی: ترامپ، حریفت منم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/459835" target="_blank">📅 00:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e5acd944.mp4?token=ohaxrMN9tP5jQ_JB1P8aXdNo8hGy6HihHTuRI5wyK3nOkqslzpbJr_kSiRtRSTivyhCJtTH1Wa1UbtDFw04zTRCF7CkTd_etPBYRtwkKZDuBcZJqMvTkS6IXw-0hZ4HBndaqFfZP7b7PgDIW1unFuNlByu0uP5JHdVgVS0ADr5p2AWj3rAzvMr-WqyOa5PZKf_pNrGTX8lWaqT3P7PBW-zhpVbLGdcKzDFYF7AfEa3tenEQQni7qEIjUKEHSvFA_fzlloADGnK8lfE6e8hCNjdmHJXmJoihCLYdZa1Ren_8Ikn64K_3X7epRgb_dx0DQGE7IdrsiOoD0hvIz_U6aQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e5acd944.mp4?token=ohaxrMN9tP5jQ_JB1P8aXdNo8hGy6HihHTuRI5wyK3nOkqslzpbJr_kSiRtRSTivyhCJtTH1Wa1UbtDFw04zTRCF7CkTd_etPBYRtwkKZDuBcZJqMvTkS6IXw-0hZ4HBndaqFfZP7b7PgDIW1unFuNlByu0uP5JHdVgVS0ADr5p2AWj3rAzvMr-WqyOa5PZKf_pNrGTX8lWaqT3P7PBW-zhpVbLGdcKzDFYF7AfEa3tenEQQni7qEIjUKEHSvFA_fzlloADGnK8lfE6e8hCNjdmHJXmJoihCLYdZa1Ren_8Ikn64K_3X7epRgb_dx0DQGE7IdrsiOoD0hvIz_U6aQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم نیشابور ۱۸۶ شب پای ایران ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/459834" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZTVQA-5zQ_y4X5zvByU2AOhFGH2LoDVcdSbFBDJcEGQapafESMM_1yrXkEzTNachYcDOqdnMVYWjLM7w__FZRD42uXbf5yDsbHfB9wY4G4QqCeFpAhpo4octsgZ2wvyd6SabfdLt5kAJxLw50q4mEiEapkd7z39uYjXAaWFXOjKU7o-jioVH2efboRHlvVHgzL4MZMVtqjCp1yRjuj-jBYwL_oLMIfMAYG1KhB8BB8_IfWgeAA_6gf-_iMTwFn56ozUzB3_xL7NPC_Fe49Sov04d8z-Y2URD7RY0tc0WrwPATHIuTgEkTKlFlkUWIiHfZmhgeW6OjvjjBhYs2m5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راز پنهان پشت تاریخ‌های دونفره!
🔹
دردنیای پرمشغلهٔ امروز که همه درگیر کارهای روزمره، استرس‌ها و تکنولوژی هستند، اختصاص‌دادن بخشی از حافظه (و زمان) به یک تاریخ خاص، نشان‌دهنده این است که شما عمداً برای «رابطه» فضا باز کرده‌اید. این کار به طرف مقابل حس امنیت و دیده‌شدن می‌دهد.
🔹
هر تاریخ مهم، در واقع یک «نقطه عطف» است. یادآوری این تاریخ‌ها فقط مرور تقویم نیست؛ بلکه فرصتی است تا زوجین در کنار هم بنشینند و بگویند: «یادت هست آن روز چقدر هیجان داشتیم؟» یا «چقدر مسیر را با هم خوب طی کردیم؟».
🔹
زندگی مشترک به‌مرور زمان ممکن است به سمت یکنواختی برود. مناسبت‌ها و یادآوری تاریخ‌ها، مانند «وقفه» یا «نقطه تنفس» عمل می‌کنند. این روزها به رابطه هیجان تزریق می‌کنند، فضای رمانتیک را بازسازی می‌کنند و به‌نوعی به رابطه «رنگ و لعاب» می‌دهند.
🔹
عدم توجه به مناسبت‌ها، گاهی (نه همیشه) به مرور زمان این تصور را ایجاد می‌کند که رابطه برای فرد «عادی» یا «کم‌اهمیت» شده است. این «بی‌تفاوتیِ ظاهری» می‌تواند منشأ سوءتفاهم‌های بزرگ باشد.
🔹
کیفیت مهم‌تر از کمیت است: لازم نیست حتماً هدیه‌های گران‌قیمت یا جشن‌های بزرگ بگیرید. گاهی یک یادداشت ساده، یک شام دونفره یا حتی یک پیام صمیمانه که بگوید «یادم هست آن روز چقدر برایم خاص بود»، بسیار اثرگذارتر است.
🔹
اگر شریک عاطفی شما تاریخ‌ها را فراموش می‌کند، فوراً آن را به‌حساب «عدم دوست‌داشتن» نگذارید. گاهی مدل ذهنی افراد متفاوت است. به‌جای سرزنش، می‌توانید با هم توافق کنید که این تاریخ‌ها برایتان مهم هستند و از او بخواهید در این مسیر به شما کمک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/459833" target="_blank">📅 23:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459832">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfEJMpRxjrXyqybkNclKccSCOW1wPOl_Cq8u87hLzm96H5R5T1g7rfk07U8q2DqIOdFQQw4YyGIjqI4HiGSMgP-TyFmFI7MwYmLsdF8BHC8s6CtlSkA-IoBEvaNVNq8bJ-mq7kWdDQMN5sK9LnsCJMSiVtNpBEw7CqFB5PU0vI8CRd8KAoIoKrY3cxwQjQdCxrwDTLiD92Ne3ZRUow8yFRzF8_nZS7IZXuE8euNScrRDeihd8Mq-QmUAZW_r1bYTFoWKJD4R6o3TjYJ7Ye7p7M45Ty9Pbw24OQsgM_7qDwOH7YF0yPR3HSyeKRHw9BRacRr9ueJSaahFT1HfKEBZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریل ترکیه بدون ایران به قفقاز برگشت
🔹
ترکیه بازسازی خط ریلی منتهی به مرز ارمنستان را آغاز کرده؛ مسیری که پس از ۳ دهه قطع ارتباط، بار دیگر قفقاز را به آناتولی متصل می‌کند و مکمل کریدورهای میانی و زنگزور است.
🔹
پس از فروپاشی شوروی، ارمنستان و آذربایجان بر سر منطقهٔ قره‌باغ دچار اختلاف شدند. در سال ۱۹۹۳، نیروهای ارمنی کنترل منطقه کلبجر در خاک آذربایجان را به دست گرفتند و ترکیه که در این درگیری‌ها از باکو حمایت می‌کرد، مرزهای خود را با ارمنستان به طور کامل بست.
🔹
در نتیجه، ارتباطات مستقیم جاده‌ای و ریلی میان ۲ کشور که تا ژوئیه ۱۹۹۳ از طریق خط ریلی گیومری-قارص برقرار بود، به کلی قطع شد.
🔹
اکنون پس از کنترل کامل قره‌باغ توسط آذربایجان در سال ۲۰۲۳، ۲ کشور به دنبال احیای این اتصال ریلی از طریق مسیر گیومری-آخوریک-آکیاکا-قارص هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/459832" target="_blank">📅 23:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459831">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9616ce036c.mp4?token=mWe8p4HQE8lJEbL-bANxS131xd4J4jeNMAGO5CO6YXePNp2oaxYd_NhmPvp3gdwg2PC1HiD4qBWeKg2zShKv_4058asgp7oZJpIvOHXgTvTanLZZC9--pF-HcOTTSApMnifp6wZhXZD21QdytanxH82y8TrjuSSXwhg-4gqZrjjILyFWpndvdNWqeQsDB3oY_hhgH8MSdstFHdtoIG2Tn1wM0S2VCRjzNUEKOWEpHqqvk7juah4afJB3ID_WV9eGvmqAItOVNhX5D1iotIV0ixs8wbHcOkUdsRsPPQKAddBK-IQJfpL5TOM3JR07afy1I-iaNJBkqu4b5DOvbv_UIYlSXCDD5sFUKNqCD_X-_c_aOrBIuF3ikol3_bqVFR2OQEjWSUan7I8tq2gFI3sa0vHTrQCulKQkGlqeBuA27BR2nYOTl7VlUUTJPhihGQON7zNGKAvhgF4GMYPAmD09xSzb2LnoHbJUfS6xxyR5KOsiNBSfIrx6sxKiYMiFx_YmCxLoQqYiwp588uholQSLz6IVRXE07Gf0p85ffkNjCDpHM8rsLAnlnSHKAP9x8yNdupvyBHKL_KQFhAPgcYylXcMS9DHXiB2yOT5ZSrJw3ho1WKmJ6Ai57l8g8EyTflXgYa2sgSDSVd2_cdrLozUyYYYSu00o1k_mvWINGCsQjJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9616ce036c.mp4?token=mWe8p4HQE8lJEbL-bANxS131xd4J4jeNMAGO5CO6YXePNp2oaxYd_NhmPvp3gdwg2PC1HiD4qBWeKg2zShKv_4058asgp7oZJpIvOHXgTvTanLZZC9--pF-HcOTTSApMnifp6wZhXZD21QdytanxH82y8TrjuSSXwhg-4gqZrjjILyFWpndvdNWqeQsDB3oY_hhgH8MSdstFHdtoIG2Tn1wM0S2VCRjzNUEKOWEpHqqvk7juah4afJB3ID_WV9eGvmqAItOVNhX5D1iotIV0ixs8wbHcOkUdsRsPPQKAddBK-IQJfpL5TOM3JR07afy1I-iaNJBkqu4b5DOvbv_UIYlSXCDD5sFUKNqCD_X-_c_aOrBIuF3ikol3_bqVFR2OQEjWSUan7I8tq2gFI3sa0vHTrQCulKQkGlqeBuA27BR2nYOTl7VlUUTJPhihGQON7zNGKAvhgF4GMYPAmD09xSzb2LnoHbJUfS6xxyR5KOsiNBSfIrx6sxKiYMiFx_YmCxLoQqYiwp588uholQSLz6IVRXE07Gf0p85ffkNjCDpHM8rsLAnlnSHKAP9x8yNdupvyBHKL_KQFhAPgcYylXcMS9DHXiB2yOT5ZSrJw3ho1WKmJ6Ai57l8g8EyTflXgYa2sgSDSVd2_cdrLozUyYYYSu00o1k_mvWINGCsQjJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با پیکر ۶ شهید حملهٔ دشمن آمریکایی در آغاجری خوزستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/459831" target="_blank">📅 23:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459827">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc00a2101.mp4?token=At99CeqYjovAJp_PyTWYsjvGoG6QPkB2EJDwuxODeN7gPWSUpWHBm-d3U1M4I-hQdoX9gVI5UToOHGsWvwz3nhkosyp53gOOzkBlhsQ1Bze1OnXi3cfwir_jwY16Zbc8q_kEdambVW4yrhk6lhtcIXJsQXs1ehZJfKLlcuZ1mEq4H_kji_McfBVsHpU0aodXS2MF0wfGpv24aa2yx-jMolebNkn1rY9nC-nnYPxNr5WSW4ClrdEbbBZ0SFi5C35MixzYlAnNwvbioDM_lLzofOArhYmxfCS-Lrdk6qSil734Cc6BZ96JHjFjeNRp-bTkzZQdw1KTqJ46KqwPs89zgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc00a2101.mp4?token=At99CeqYjovAJp_PyTWYsjvGoG6QPkB2EJDwuxODeN7gPWSUpWHBm-d3U1M4I-hQdoX9gVI5UToOHGsWvwz3nhkosyp53gOOzkBlhsQ1Bze1OnXi3cfwir_jwY16Zbc8q_kEdambVW4yrhk6lhtcIXJsQXs1ehZJfKLlcuZ1mEq4H_kji_McfBVsHpU0aodXS2MF0wfGpv24aa2yx-jMolebNkn1rY9nC-nnYPxNr5WSW4ClrdEbbBZ0SFi5C35MixzYlAnNwvbioDM_lLzofOArhYmxfCS-Lrdk6qSil734Cc6BZ96JHjFjeNRp-bTkzZQdw1KTqJ46KqwPs89zgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیشب حملهٔ سنگینی به ایران کردیم و آماده‌ایم در صورت نیاز، حملهٔ دیگری را هم انجام دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/459827" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a925bb7627.mp4?token=mVy1fPEbAeqMQJqpgbNM08-Bt-MXZqNl1_k5tt5c74HVP2595tmug4MqA8YKkR67-RyNNlmTP3YKEmgSL95h6erFmZemtChdBeXPpiZ5cRjgauAb29v2D7Jc7QQ6LhxyKmo_Onf78kk9p3f8iY3FM1E_QXo2of2MSLtWoUFcF6PmxjkFgnQjXuX7iXetZZ5UOtCH5TTLRczrUWcHK0sQ4gqh-cmaZizyV7ww7omUVWV7eR79rlNX86tLGAULNs24LJTh0uMIUXHs-hInmXWvlAZo8io8I-eDW6zlMq3R4a9Nmb97YAUhEswMObPAFbyfIP2CT4f1TvM7dlo4p0tAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a925bb7627.mp4?token=mVy1fPEbAeqMQJqpgbNM08-Bt-MXZqNl1_k5tt5c74HVP2595tmug4MqA8YKkR67-RyNNlmTP3YKEmgSL95h6erFmZemtChdBeXPpiZ5cRjgauAb29v2D7Jc7QQ6LhxyKmo_Onf78kk9p3f8iY3FM1E_QXo2of2MSLtWoUFcF6PmxjkFgnQjXuX7iXetZZ5UOtCH5TTLRczrUWcHK0sQ4gqh-cmaZizyV7ww7omUVWV7eR79rlNX86tLGAULNs24LJTh0uMIUXHs-hInmXWvlAZo8io8I-eDW6zlMq3R4a9Nmb97YAUhEswMObPAFbyfIP2CT4f1TvM7dlo4p0tAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره جالب نجم‌الدین شریعتی از پیام ویژه‌ای که باید به سردار سید مجید موسوی منتقل می‌کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/459826" target="_blank">📅 23:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459825">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎥
۱۸۶ شب خروش حافظان تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/459825" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرود اضطراریِ هواپیمای وزیر آمریکایی
🔹
سی‌بی‌اس نیوز: یک هواپیمای گارد ساحلی که حامل مارکوین مولین، وزیر امنیت داخلی آمریکا، و دیگر مقامات ارشد این وزارتخانه بود، بعدازظهر چهارشنبه پس از کار افتادن یکی از موتورهایش در حومهٔ واشنگتن دی.سی. فرود اضطراری کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/459824" target="_blank">📅 23:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d7dc5cb.mp4?token=aTWCnUfSfkFHAjOKS798NRX3f8y0QxJ7m4xLCpCOID8rCVbKfLt6qGajKRpWEMP8c0CtfTnJxnFcMP51_x056zQHLaVawasaTwL3_XXJI6tu-sVfFwlWOR9xM9E4USm6vnE3ZKNHpV8R9J4B208wCsQ8bj6evxq-VI85WmlYESIbJSkvlG8GFmG9XoIrL6_JaY5C_IlN0UNaxbO8SzHKrS8ErZNaemkwjFVXzYuufALzWTzoMvHcpIx1vsAo7D6IMVGGzxuBHpWeSMHrboeL_cXE9GW_tZmQ_uMUJSy0hgND8sFWI1M53aW--fQs8IZo-jmf7Bc5T2DVlYnJWArDcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d7dc5cb.mp4?token=aTWCnUfSfkFHAjOKS798NRX3f8y0QxJ7m4xLCpCOID8rCVbKfLt6qGajKRpWEMP8c0CtfTnJxnFcMP51_x056zQHLaVawasaTwL3_XXJI6tu-sVfFwlWOR9xM9E4USm6vnE3ZKNHpV8R9J4B208wCsQ8bj6evxq-VI85WmlYESIbJSkvlG8GFmG9XoIrL6_JaY5C_IlN0UNaxbO8SzHKrS8ErZNaemkwjFVXzYuufALzWTzoMvHcpIx1vsAo7D6IMVGGzxuBHpWeSMHrboeL_cXE9GW_tZmQ_uMUJSy0hgND8sFWI1M53aW--fQs8IZo-jmf7Bc5T2DVlYnJWArDcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها درحال ساخت موشکی بودند که مین‌ریزی می‌کند
🔹
تا به‌حال شنیده بودید کسی موشکی بسازد که مین رها کند؟ من که هرگز چنین چیزی نشنیده بودم. اما آن‌ها داشتند همین کار را می‌کردند. @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/459823" target="_blank">📅 23:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e02b4187.mp4?token=o23qNWGvB94cvCYS9w1LBYCDJbvzQNLnV0rVRJUeSqMWOjB_l3V34NuXbgeV0G8jBSz0a9vBIl8KT19ghPexrxqqJnsVgUBvci4DaZBslCiFQyPBq-ROkJg4yBsyHUvZ2RRwJkbAptpCUHF_HsWq_qBh0rQ4ghHf2taWRmYs8mYfWeoeN6lgbrLuG6Tagfqpv75nPD5lkk_FaTZcgs2sS1-1DChf7PcmWbsC_pJBvUWyxyURXRppfbHQCpGtWe8-7305aevfdEVIlrP6COt8vfc5WTP1GdBt3QBcurb2wxK6hzsuMO85RKgemUUdFuHJ5lXmZRlNevDxdcXa-HcATA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e02b4187.mp4?token=o23qNWGvB94cvCYS9w1LBYCDJbvzQNLnV0rVRJUeSqMWOjB_l3V34NuXbgeV0G8jBSz0a9vBIl8KT19ghPexrxqqJnsVgUBvci4DaZBslCiFQyPBq-ROkJg4yBsyHUvZ2RRwJkbAptpCUHF_HsWq_qBh0rQ4ghHf2taWRmYs8mYfWeoeN6lgbrLuG6Tagfqpv75nPD5lkk_FaTZcgs2sS1-1DChf7PcmWbsC_pJBvUWyxyURXRppfbHQCpGtWe8-7305aevfdEVIlrP6COt8vfc5WTP1GdBt3QBcurb2wxK6hzsuMO85RKgemUUdFuHJ5lXmZRlNevDxdcXa-HcATA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش شهرکرد در شب ۱۸۶: نه سازش نه تسلیم، نبرد با اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/459822" target="_blank">📅 23:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seLYu0qFV1BLLi5XvlL427eDodBqgDwZhzix47KpPfYP3GkWyLYrCmRBJQG0no2IGwyP1bQhHtVVCl5EgQVAbRclYbNB1SVIdCqIPbHYk8F060JOF4-crvPfOznnpJrn0o0j0EPVpYnPdqskKjOhms8MYYjMwncBw8jrvGQUhg6NRQI-Utrd9_MvVToff-U_t3wHF0ql9Wvhn02nfgqZ7jYUeFMtMzVEidbEPpR2GoZpIdycbdtywOFO1L2Qhn_lnmA9z9w583zcG9-AOFPIX9UEouy3cepWbjht6dDik5EXH83wDRs2xiL6d7u1k0X2qKi85yVZbvct1uIeos_ObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰ شکایت جدید، سازندهٔ چت‌جی‌پی‌تی را غافلگیر کرد
🔹
تک‌کرانچ:  اپن‌ای‌آی با موج تازه‌ای از پرونده‌های قضایی مرتبط با حادثه تیراندازی در تامبلر ریج کانادا روبه‌رو شده است.
🔹
یک شرکت حقوقی که پیش‌تر از طرف قربانیان و خانواده‌های آنان ۷ شکایت علیه اپن‌ای‌آی مطرح کرده بود، این هفته ۳۰ شکایت دیگر را در دادگاهی در کالیفرنیا ثبت کرده است.
🔹
ریشهٔ پرونده‌ها به حادثه‌ای در ۱۰ فوریه ۲۰۲۶ در شهر تامبلر ریج در استان بریتیش کلمبیا بازمی‌گردد. در این حادثه، مهاجم پس از کشتن اعضایی از خانواده خود به مدرسه متوسطه تامبلر ریج رفت و در آنجا چندین نفر را کشت و ده‌ها نفر دیگر را مجروح کرد.
🔹
بر اساس گزارش‌هایی که پیش‌تر منتشر شده بود، کارکنان اپن‌ای‌آی در جریان بررسی فعالیت‌های حساب کاربری مهاجم درباره برخی گفت‌وگوهای او با چت‌جی‌پی‌تی ابراز نگرانی کرده بودند.
🔹
طبق ادعاهای مطرح‌شده در پرونده، برخی کارکنان تیم‌های بررسی تهدید اپن‌ای‌آی خواستار اطلاع‌رسانی به پلیس کانادا شده بودند، اما در نهایت شرکت تصمیم گرفت با مقام‌های کانادایی تماس نگیرد و حساب کاربری را غیرفعال کند.
🔹
شاکیان ادعا کرده‌اند تصمیم برای تماس نگرفتن با پلیس تحت نظارت او گرفته شده و مدعی شده‌اند که تیم اطلاعات و تحقیقات شرکت در ساختار سازمانی زیرمجموعه او قرار داشته است.
🔹
گسترش این پرونده‌ها در حالی اتفاق می‌افتد که اپن‌ای‌آی هم‌زمان با مجموعه دیگری از انتقادها و پرونده‌های حقوقی درباره ایمنی محصولات هوش مصنوعی خود مواجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/459821" target="_blank">📅 23:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459820">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d24269d2c.mp4?token=TF3enNheEu_AdVXqRwwhQ2HK9eylNFiiCWyZsH4qQVdSu-7pbSq7LOrj80wTO3UXpfpWZURNaEmzIBvIkx1aeCjsAV-w3lF9WttrNWjY4cO-Hb9Y1CbXKjoUvDxfzr4r6ZpNraNdrXGOzuyzeFPvOkzrOW6sQrsGSqbSfFctcrzNR28s1HpfzwJrnsQ4q5O7L6ncvzf4bkNiCDV1pneSDNtekG7ofe_Hi9XgI_m_14rDEXfkXMQkJVJBLb5dFpk-6oyfgJgXo8v3jiMG3F5CrFeVxZMv9sSqtVMaqlldan_fzisMQd-317tNG3zK0gH6Icyn5t1HXQzKps5U_XxPhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d24269d2c.mp4?token=TF3enNheEu_AdVXqRwwhQ2HK9eylNFiiCWyZsH4qQVdSu-7pbSq7LOrj80wTO3UXpfpWZURNaEmzIBvIkx1aeCjsAV-w3lF9WttrNWjY4cO-Hb9Y1CbXKjoUvDxfzr4r6ZpNraNdrXGOzuyzeFPvOkzrOW6sQrsGSqbSfFctcrzNR28s1HpfzwJrnsQ4q5O7L6ncvzf4bkNiCDV1pneSDNtekG7ofe_Hi9XgI_m_14rDEXfkXMQkJVJBLb5dFpk-6oyfgJgXo8v3jiMG3F5CrFeVxZMv9sSqtVMaqlldan_fzisMQd-317tNG3zK0gH6Icyn5t1HXQzKps5U_XxPhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارتار: استقلال روی اوت‌دستی کار کرده بود و روی همان هم به گل رسید
⚽️
هم ما و هم استقلال می‌توانستیم برنده باشیم. از مسئولین اصفهان برای میزبانی و از داور برای قضاوت خوب تشکر می‌کنم.
⚽️
حسرت می‌خورم که ۳ امتیاز را از دست دادیم. استقلال روی تاکتیک اوت دستی…</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/459820" target="_blank">📅 23:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459819">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فرمانداری سیریک: صدای انفجارهای احتمالی امشب در محدودۀ بندر کوهستک، مربوط به خنثی‌سازی مهمات عمل‌نکرده دشمن آمریکایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/459819" target="_blank">📅 23:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459818">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2863167ab2.mp4?token=v31lNcKSRkuYwDgkPYhdctWQ4Vi-vgXjcXFj60o7Z2jms-rOZ0AUKKsI-c-dxrGQAPWHItITpafC7VMKkKY3LGY8OCVY9iF18RNOvF49rboF15tiT1AV8-YSYEr-PkjyGf4EGuQ0yx8oeVb7scQPmoUgKts9d44vYSQm_B5Cb3m8DFuRr69WWBH24d1m7VFyjmkPSOP7Yr6hJcW4Bklpkzci9IU-6RsHIMr4-ObF2ujZiYaoudblNhcA4uhQENjEuTHnx1E2BnJ8JPPUTEWyUwxW0HpcsaN1F2ube0C-otanwHTf4C7RE9gbxHPl-Oq1axUP8zx4Ue6mqjTUT3Z0BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2863167ab2.mp4?token=v31lNcKSRkuYwDgkPYhdctWQ4Vi-vgXjcXFj60o7Z2jms-rOZ0AUKKsI-c-dxrGQAPWHItITpafC7VMKkKY3LGY8OCVY9iF18RNOvF49rboF15tiT1AV8-YSYEr-PkjyGf4EGuQ0yx8oeVb7scQPmoUgKts9d44vYSQm_B5Cb3m8DFuRr69WWBH24d1m7VFyjmkPSOP7Yr6hJcW4Bklpkzci9IU-6RsHIMr4-ObF2ujZiYaoudblNhcA4uhQENjEuTHnx1E2BnJ8JPPUTEWyUwxW0HpcsaN1F2ube0C-otanwHTf4C7RE9gbxHPl-Oq1axUP8zx4Ue6mqjTUT3Z0BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها درحال ساخت موشکی بودند که مین‌ریزی می‌کند
🔹
تا به‌حال شنیده بودید کسی موشکی بسازد که مین رها کند؟ من که هرگز چنین چیزی نشنیده بودم. اما آن‌ها داشتند همین کار را می‌کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/459818" target="_blank">📅 23:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459817">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4970a1d1d.mp4?token=gBazwFgl6aAxrXiEDXRHkaSZoLAf5iMJL5uJrVmuNlnknQZATsl2_p5XyzA_LF4nhcEHmT4E-VxjA4LePm6KKuheWjJP_5fmZuhOq2MPhQk8dLzOAMZNOKLJkOqMTo8h0cesCbR9jZT8jkfFd5WHZo9e-WFRLf3Yk1GsiuLhfiFua_JBn6R7t-W89kSa9Y7CCW3Nko8e0Wukexb8RYwWFS0q2eYyWHnvTbvFrhq3q__vHun_tz-BkVuGUV7gFv0G7zbdGvtXhWEFv7G12RbD3UNFIZ1cHZZdG4J2OCe29EUH4ztnNV1gSBubPhzEzieow1ibqUZVzFxUUh55wLUIIYe2F1qi_PyL1mYDtqFAItJacq6Dmkgz8SzKPGma4xSCr6fYP4WILm_rXrqlTYxrtF0esbjpkG-iVZ_MV_Fe7BPLqbE3MNpJ0-_dCb_DbiaLSLqMpdKfFWgri8ezFihPbczZwRft2PKwqASTxPtOnfEl9FkDKC-xYOiKPXsPBUvq_yh7EfA32O9Pafxbfw7LzoESa5N_WRL5SEyRhMLd-mPjOubpfJAWuH5CLE1pznbCNfQBY6ix7q3rMNHuEAxPsrY99nQORAmiRUhCpS69BF80dM3ukkXjU6G0zEdmwJBicoS0WSgh8rllUqY033unKe2eMITq3CwZSPZVC7biPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4970a1d1d.mp4?token=gBazwFgl6aAxrXiEDXRHkaSZoLAf5iMJL5uJrVmuNlnknQZATsl2_p5XyzA_LF4nhcEHmT4E-VxjA4LePm6KKuheWjJP_5fmZuhOq2MPhQk8dLzOAMZNOKLJkOqMTo8h0cesCbR9jZT8jkfFd5WHZo9e-WFRLf3Yk1GsiuLhfiFua_JBn6R7t-W89kSa9Y7CCW3Nko8e0Wukexb8RYwWFS0q2eYyWHnvTbvFrhq3q__vHun_tz-BkVuGUV7gFv0G7zbdGvtXhWEFv7G12RbD3UNFIZ1cHZZdG4J2OCe29EUH4ztnNV1gSBubPhzEzieow1ibqUZVzFxUUh55wLUIIYe2F1qi_PyL1mYDtqFAItJacq6Dmkgz8SzKPGma4xSCr6fYP4WILm_rXrqlTYxrtF0esbjpkG-iVZ_MV_Fe7BPLqbE3MNpJ0-_dCb_DbiaLSLqMpdKfFWgri8ezFihPbczZwRft2PKwqASTxPtOnfEl9FkDKC-xYOiKPXsPBUvq_yh7EfA32O9Pafxbfw7LzoESa5N_WRL5SEyRhMLd-mPjOubpfJAWuH5CLE1pznbCNfQBY6ix7q3rMNHuEAxPsrY99nQORAmiRUhCpS69BF80dM3ukkXjU6G0zEdmwJBicoS0WSgh8rllUqY033unKe2eMITq3CwZSPZVC7biPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لاشه‌ٔ متلاشی‌شده‌ٔ «ام‌کیو ۹» زیر پای رزمندگان خمین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/459817" target="_blank">📅 23:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459813">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg_PSiwujl0jcLd6SIYhUhagASMacBGYXFWLshQET6ZZKFejDBQfjSba5Rhqrmx-s5JEztNNQ2-O6DQqD4fN9LnS_yEOZ6EpYBnTVbcgi_LY4XA82GBhsGs9vmdfAxf_-QC2CEEIhrigYIkj149p9nV4oQAZ_NZlD6kfTVPvq_KeJApJTh29HJlPQptShLDw3lxngGFIeAHyD8hkjHv2CCBVeWcZHepwe6axjmaMZiDjAjR8BlOLgF7Hj3RTR9CrO5F6VaL2PFImP9Sb7dv3x7J-G01OkKbHcqxoGc4yX_tivR1YeDY08C2Yhwwqe2g3aYsFCLi7dDc-0K3cAOooCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3rhdd6osyKaGOOUvmka8du8hrtvbVhMfvzYaGz2mAo6wIlU-w6QZiuYJRSko2ksWwqe_trGRfRoXKJ1zTq3kQKmqjDlayqdWk_iPL92pSmpl2jxEWvBcOWdazk06cJyfGThl8JIfGvx2Xh_bsz4oYVSRmYF_afv1GSckpHe6aGdX0HSZyYQHmfXuKU60m5e2LwSb2mAEGOTc4Hf4oEWq4xXMR2ZPHk4DrUpZMVA3Nsh8V08Z5AkAhi8NHgkQRmo-aU34Nsv20aYnfigoVIY1LFzrm-NqWhep_NydxY4ajJbK-2CEg9MUvgfAhy9MxguGeQ0Jtl_7NYcPTl7GHmITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miMgB_DWTx1PU5qtm0xkBboJfLxwRLn6V3qqDNBhtNAZSgFC9KEmHtg-oxyE3J4ybGY7n63iM10hDHBxq05U8oc7yrEFr2mzFf_xxTF1_EQ9ToAXTXlqGmJQYVWAya3acXoGriqvLU3RfmXDuemTll6P20bMIZxC4wf4h84uWL28YKpN8okpTUapStCxfyrjN-05DIKZO2uC9xTZC9viy5AmA-iJw3G4Rfji9F45Hp0eb8pPuOTqXUiE5R9seNvJvJTSh2o9uLYQCnmjQzITpAFgvNWdy9vkjBrtIj9mxhgu0ClU-j_WT7Ho_k1VKtcUcXL9ZpnTr0WKsELlpMbHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IyFzI7V_XFaWPaZ0-emvnCpeW9VAcy2ZCDFIcgbyLWCOr1NaOPltU4j9fY482T1AnesyGgGdN1NoDEDLWEX8kJ9eHT7PhoF3vq63f_4fvxNmCjcXK5DbhJrpGrI-ZNYtvJRNbb1EJT3XpJbfuhjDtc2mT23OiEE8dTlogzAL8b225bzLglTnN5krHn45bk1Y-LHlB_6p7D3brsoqMdjyNnhB-24ILMa-5f4qXwkGp41mUKgntxy7uyYD1_melGJqZgsHnla82uWalMWVfHajPbyN3XmqCyU-2Uh8N6b8goj87A9bgsEsIlwNXC9cIurVzKXLI5bkMdhq7k4fCPXcrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بقایای موشکی که دیشب عروسی سیریک را به خاک‌وخون کشید  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/459813" target="_blank">📅 22:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459812">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036d5b9fb4.mp4?token=dO7uh-KJY_zsbyi5IgLYZnVS302ibzmTFK7E16lB68ce3OTuNh6GnlvuKW4ue5dmU0u9J03fveS_y_p7r6NSZQz33ViXEG5-LB1GO-3l_ktwAJFTYtyyjAx9JMd0ZQkfClFtXa5QMUkcG9uibpWUPcCtRYLoB0MCxVHiTTpK__EJwXSpiA_T54sItjEIf4XcpMVWdc6zurO3RTE25L2cqtHTpAoH_XHXOPljYoUdfQToO9UwvSKgIk80210Bk7JAOq0xlP284sZpCOSrvAZWdyKxECwpSEbsIjGFNO3HogKzdRdJNZ9joPZN54ERY-ud81Ck8nhxjGuJbOjKoAh4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036d5b9fb4.mp4?token=dO7uh-KJY_zsbyi5IgLYZnVS302ibzmTFK7E16lB68ce3OTuNh6GnlvuKW4ue5dmU0u9J03fveS_y_p7r6NSZQz33ViXEG5-LB1GO-3l_ktwAJFTYtyyjAx9JMd0ZQkfClFtXa5QMUkcG9uibpWUPcCtRYLoB0MCxVHiTTpK__EJwXSpiA_T54sItjEIf4XcpMVWdc6zurO3RTE25L2cqtHTpAoH_XHXOPljYoUdfQToO9UwvSKgIk80210Bk7JAOq0xlP284sZpCOSrvAZWdyKxECwpSEbsIjGFNO3HogKzdRdJNZ9joPZN54ERY-ud81Ck8nhxjGuJbOjKoAh4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارتار: برای برد آمده بودیم نه تساوی
⚽️
اگر مربیان شجاع باشند، بازیکنان هم از آنها یاد می‌گیرند؛ امسال تیم‌مان فوق‌العاده است و برای قهرمانی می‌جنگیم. @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/459812" target="_blank">📅 22:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459811">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ad3b2cbe.mp4?token=qmtCCHQVtwy5XJn9km_Y2Et4bvooYIRgT3T_AjjDxMXYx4Um1NNcJIu6Ut1mgvk3vLzDMSXge5K20aDYWzrOIZ2854ZJ20GfRoYBeGyglMuuBzVe6dwEeSewODuRwlywjmTF3jeqPN9lRqi8ILaXGjBW-K_fzPn7nGCpjcrWhcT8LJ-RhRAk8D5fcS7tRS24nnYgYHvXwx7XTHf5kktHGcrIKte9-UciS4lpDQfKOiyrQLD5DYqFbUiEUoTN7r7CMCl_eEArJj7ATNCN_2vbdNTqkHv-dIs2fbZlmnzMqKsVZ0r0S6Zql9B-Zhq3r302MNy6DtLLgEStixDCaXBUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ad3b2cbe.mp4?token=qmtCCHQVtwy5XJn9km_Y2Et4bvooYIRgT3T_AjjDxMXYx4Um1NNcJIu6Ut1mgvk3vLzDMSXge5K20aDYWzrOIZ2854ZJ20GfRoYBeGyglMuuBzVe6dwEeSewODuRwlywjmTF3jeqPN9lRqi8ILaXGjBW-K_fzPn7nGCpjcrWhcT8LJ-RhRAk8D5fcS7tRS24nnYgYHvXwx7XTHf5kktHGcrIKte9-UciS4lpDQfKOiyrQLD5DYqFbUiEUoTN7r7CMCl_eEArJj7ATNCN_2vbdNTqkHv-dIs2fbZlmnzMqKsVZ0r0S6Zql9B-Zhq3r302MNy6DtLLgEStixDCaXBUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات صهیونیست‌ها به جنوب لبنان ادامه دارد
🔹
شبکه المنار: ارتش رژیم صهیونیستی اطراف ارتفاعات راهبردی علی‌الطاهر را هدف حملات هوایی و توپخانه‌ای قرار داد.
🔹
همچنین جنگنده‌های این رژیم بار دیگر شهرک النبطیه الفوقا و شهرک حاریص در جنوب لبنان را بمباران کردند.
🔹
ارتش تروریستی اسرائیل، عملیات انفجار و تخریب جدیدی هم در شهرک حولا و بیت لیف انجام داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/459811" target="_blank">📅 22:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459810">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تشییع شهدای مظلوم عروسی کوهستک فردا برگزار می‌شود
🔹
روابط‌عمومی سپاه هرمزگان: مراسم تشییع پیکر مطهر شهدای مظلوم مراسم عروسی کوهستک که در جریان جنایت رژیم آمریکا به شهادت رسیدند، پنجشنبه برگزار می‌شود.
🔹
مکان: شهر کوهستک، از بلوار ورودی شهر تا گلزار مطهر شهدا…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/459810" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459809">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a99e356a4.mp4?token=Ro5O0vVrtolatoQBv2FI9gjOcflNfbtnXaGDUTbKw-4fLvOWAd7XPWw8MsAo2jBZgQVxEl5HyT1HbCWQZdrK4_YfvkRsN-nSzqEQGwjeMcvz8W1ENBubnI8gn05DeyNbQHy5w5OzlHbBV_ivsSi_l79TnZ8qN3yEdwisjAYYwzXR5hXnGdenSP3kOkZv6razzduaW6UT3YlhvOIDdvitOGbLO9TbMrW1hVNd53FV74OtsPjUrmIEup3c0LWkbee3JOspYrLQaAbXmtCiek3j1JOJdilMLy8N1udwObaFGLgoqn4YshmpCkgjcFoqTTiJexJyXL9wg_gYYUTZhUkEnB_6choZTBZ7PCjm-mpeM785X9zauakfem42C9joFHtwRb6L6Y8S1TKkSNGrqBhUlm_x2iN8sz-UTnK-YOtOiwrk96CkQLTVGHez2GUbXcW95JAyDJ09gxt78BQhfqJsoLjmS0_tyaMRMA_w9PW4OUDelXXjOfw54RdeAuGeR4Q-XjknZUWS4bQMTkXohgxO1AlKjT5iTp0Mkxtnoe35XBlF3PIbtbfcdiz3MfylyclsQAMd4kPbt0MO7HyuLol2yrfL4PRKpsFF-TEiDt1B_S9zRjZjOxXNz8horcV332im7qf6Mgb_MHXuTpiycL-iRBj6-WyksqBJlhHKQ3kojbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a99e356a4.mp4?token=Ro5O0vVrtolatoQBv2FI9gjOcflNfbtnXaGDUTbKw-4fLvOWAd7XPWw8MsAo2jBZgQVxEl5HyT1HbCWQZdrK4_YfvkRsN-nSzqEQGwjeMcvz8W1ENBubnI8gn05DeyNbQHy5w5OzlHbBV_ivsSi_l79TnZ8qN3yEdwisjAYYwzXR5hXnGdenSP3kOkZv6razzduaW6UT3YlhvOIDdvitOGbLO9TbMrW1hVNd53FV74OtsPjUrmIEup3c0LWkbee3JOspYrLQaAbXmtCiek3j1JOJdilMLy8N1udwObaFGLgoqn4YshmpCkgjcFoqTTiJexJyXL9wg_gYYUTZhUkEnB_6choZTBZ7PCjm-mpeM785X9zauakfem42C9joFHtwRb6L6Y8S1TKkSNGrqBhUlm_x2iN8sz-UTnK-YOtOiwrk96CkQLTVGHez2GUbXcW95JAyDJ09gxt78BQhfqJsoLjmS0_tyaMRMA_w9PW4OUDelXXjOfw54RdeAuGeR4Q-XjknZUWS4bQMTkXohgxO1AlKjT5iTp0Mkxtnoe35XBlF3PIbtbfcdiz3MfylyclsQAMd4kPbt0MO7HyuLol2yrfL4PRKpsFF-TEiDt1B_S9zRjZjOxXNz8horcV332im7qf6Mgb_MHXuTpiycL-iRBj6-WyksqBJlhHKQ3kojbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراغه پای عهد ایستاد؛ مطالبهٔ پاسخ قاطع به دشمن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/459809" target="_blank">📅 22:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459808">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ebad354f.mp4?token=v0W2zsgUkCHzIxJgRFY5Yov0gMa-hZ1XtHoQ9Z08cbzAEuUFAa_2nfk0lHHU-0QsMaUlSpSb-rdzo6GLtze1tPdpq9zKDNAcbqOA0kHT8gBC_FqeJtEkckin-5v0V4xiNzrFx1NmM74yV2i3ylh0LQhau3udavkueZkR1cMhQYB-F9tbV25RBVvguPImksy_Egdzvqp6q_BrqOUjx58Bo62iyJdlIFf9KhIgsVjEV0GcJOYqTI34rHzaLFPFr3o5Q0Sc7H71yTJ0yw8mPESMBuDwLpe_i6SAhFJ1uKoATyldfa8aYEE81IUHoO-IJt6pFqSOsYR3Un4aDADfbEMpTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ebad354f.mp4?token=v0W2zsgUkCHzIxJgRFY5Yov0gMa-hZ1XtHoQ9Z08cbzAEuUFAa_2nfk0lHHU-0QsMaUlSpSb-rdzo6GLtze1tPdpq9zKDNAcbqOA0kHT8gBC_FqeJtEkckin-5v0V4xiNzrFx1NmM74yV2i3ylh0LQhau3udavkueZkR1cMhQYB-F9tbV25RBVvguPImksy_Egdzvqp6q_BrqOUjx58Bo62iyJdlIFf9KhIgsVjEV0GcJOYqTI34rHzaLFPFr3o5Q0Sc7H71yTJ0yw8mPESMBuDwLpe_i6SAhFJ1uKoATyldfa8aYEE81IUHoO-IJt6pFqSOsYR3Un4aDADfbEMpTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنشنال این‌بار ناخواسته راست گفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/459808" target="_blank">📅 22:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459807">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎥
احترام نظامی سنندجی ها در ۱۸۶ شب ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/459807" target="_blank">📅 22:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459806">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
روایت مردم پاکدشت از ۶ ماه ایستادگی در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/459806" target="_blank">📅 22:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7651c4643.mp4?token=sZxnXyfxAfS0epy-6Z50-LC1R0MsJZXKL4UdWojEiK4Fva-wB20cAm9YYsGVGcnCdwu2Ky5gnx7bBHTeEy4iHS7Ok3Snx3Nm845Sb1eeBkQ1e-ee0ypxCrHajymCso_zbBJgPukr2GxCLzODT8onM3zXfpSVe5Ik8jZoU0l7rDGLnDad88vm3FvqLpW0w-fvtB-s5Z4VQMWT0XZ-SkbmJWbhpLdfiH4FlGiYVc6XveculvlUNr_WQeJTtekP-h1wsVitU5uYVJWWbTDHR1Pplqj10ELKU5Mi87zd0xzQ_0pqJKSosYLy3geZ168uaCfU90tpxh9aeVoyVZeHrpx-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7651c4643.mp4?token=sZxnXyfxAfS0epy-6Z50-LC1R0MsJZXKL4UdWojEiK4Fva-wB20cAm9YYsGVGcnCdwu2Ky5gnx7bBHTeEy4iHS7Ok3Snx3Nm845Sb1eeBkQ1e-ee0ypxCrHajymCso_zbBJgPukr2GxCLzODT8onM3zXfpSVe5Ik8jZoU0l7rDGLnDad88vm3FvqLpW0w-fvtB-s5Z4VQMWT0XZ-SkbmJWbhpLdfiH4FlGiYVc6XveculvlUNr_WQeJTtekP-h1wsVitU5uYVJWWbTDHR1Pplqj10ELKU5Mi87zd0xzQ_0pqJKSosYLy3geZ168uaCfU90tpxh9aeVoyVZeHrpx-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار ژنرال‌های آمریکا به ترامپ: توان ایران را دست‌کم نگیرید
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/459805" target="_blank">📅 22:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b593798c4.mp4?token=d41VcrlVkUZLwwCXU8-n2tkS5pmC9yM9aNJ37OsScMFV-pZvudhoXyQwlgtfZ0FyeHOKHaD2V5Hi9QODUSMxd6ylfbFBCCqJ29perUfDp7P5zQWEVZraRyH_vTrdk__o5fNqS2ZnVWM6WsdM5pAs0tVQ7CWr3rBoeFxGWK_4HRpHrlIcJvyyuOWeJyT2K-RMacdKeFMWg-qx9nqgoGmWFj-kl2EGJo5K5tn77ji4KGAfYCARZ_sely1XNnxaKhm2SWyZ3_wIaQIehyw_s2YJK55D2Ph0r3F6hXah63nhl-DzI5hrrumNtNFpHGEBxRwUvN5VQ7MCTp51i82kdOmCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b593798c4.mp4?token=d41VcrlVkUZLwwCXU8-n2tkS5pmC9yM9aNJ37OsScMFV-pZvudhoXyQwlgtfZ0FyeHOKHaD2V5Hi9QODUSMxd6ylfbFBCCqJ29perUfDp7P5zQWEVZraRyH_vTrdk__o5fNqS2ZnVWM6WsdM5pAs0tVQ7CWr3rBoeFxGWK_4HRpHrlIcJvyyuOWeJyT2K-RMacdKeFMWg-qx9nqgoGmWFj-kl2EGJo5K5tn77ji4KGAfYCARZ_sely1XNnxaKhm2SWyZ3_wIaQIehyw_s2YJK55D2Ph0r3F6hXah63nhl-DzI5hrrumNtNFpHGEBxRwUvN5VQ7MCTp51i82kdOmCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ربات کینه‌جو انتقام گرفت
🔹
یک ویدیوی عجیب از یک فروشگاه در روسیه منتشر شده که در آن، واکنش غیرمنتظره یک ربات انسان‌نما پس از رویارویی با یک مشتری، حسابی خبرساز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/459804" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459803">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
از وقتی در
اهواز
دستگاه تصفیه آب نصب کرده‌ایم، هم مصرف برق بیشتر شده و هم هدررفت آب داریم. برای تهیه یک کلمن آب خنک، باید حدود دو کلمن آب تصفیه‌شده به فاضلاب ریخته شود تا آب تصفیه شود. لطفاً مسئولان درباره این میزان
هدررفت آب و راهکار کاهش آن
چاره‌ای بیندیشند.
🔹
من یک کشاورز از دادین سفلی شهرستان کازرون هستم.
برق چاه کشاورزی
ما از ساعت ۱۰ تا ۵:۳۰ قطع می‌شود و دو ساعت هم خاموشی کلی منطقه‌ای داریم؛ در مجموع روزانه حدود ۱۱ ساعت و نیم برق نداریم. باغ‌های مرکبات ما در دمای ۴۰ درجه و به ‌دلیل کم‌آبی در حال خشک‌شدن هستند و صدای ما هم به جایی نمی‌رسد. لطفاً به داد کشاورزان برسید.
🔸
بنده ساکن نسیم‌شهر، شهرک نور، خیابان جانبازان هستم. لطفاً به مسئولان
رایتل و همراه‌اول
اطلاع دهید که این شهرک به هیچ عنوان اینترنت و آنتن مناسب ندارد. حتی برای کارت‌به‌کارت کردن باید تا سر خیابان برویم تا اینترنت داشته باشیم و در بسیاری از مواقع هم در دسترس نیستیم.
🔹
در شهرستان رابر هنوز حتی یک مرحله واگذاری زمین در
طرح مسکن ملی حمایتی
انجام نشده است. به داد شهرستان رابر برسید؛ تا کی مردم شهرستان‌ها باید تاوان عملکرد ضعیف مدیران شهرستانی را بدهند؟ از دولت درخواست داریم نظارت و کنترل جدی بر عملکرد مدیران شهرستان‌ها، به‌ویژه نماینده ارشد دولت در شهرستان داشته باشد.
🔹
چرا هیچ ‌کس جلوی
افزایش قیمت خودرو در شرکت‌های ایران‌خودرو و سایپا
را نمی‌گیرد؟ چرا نظارتی وجود ندارد؟ مدیران این دو شرکت هر زمان که بخواهند قیمت‌ها را افزایش می‌دهند. مردم چه گناهی دارند؟ در شرایطی که همه باید به یکدیگر کمک کنیم تا کشورمان مثل همیشه سربلند و پیروز باشد چرا این دو شرکت از شرایط موجود سوءاستفاده می‌کنند؟
🔹
یک دختر معلول شدید دارم و خودم هم معلول خفیف هستم. چرا دولت
قانون ماده ۲۷ برای معلولان شدید
بالای ۱۸ سالِ بیکار را که سال‌هاست در مجلس تصویب شده، اجرا نمی‌کند؟ با این فشار اقتصادی و تورم به معلولین که قشر آسیب پذیر جامعه هستند هم برسید.
🔹
در
اسلامشهر
به‌دلیل سرقت کابل‌های تلفن، ماه‌هاست تلفن‌های ثابت قطع شده و
مخابرات
نیز پاسخ‌گو نیست. اینترنت ثابت هم به همین دلیل قطع است و مردم ناچارند از اینترنت گوشی استفاده کنند که آن هم مشکلات و هزینه‌های خود را دارد.
🔹
کارخانه
واگن‌سازی زرند کرمان
(پلور سبز) دو ماه است حقوق کارگران را پرداخت نکرده و هر ماه به بهانه‌های مختلف پرداخت حقوق به تأخیر می‌افتد. از طرفی اعلام ورشکستگی شده و طلبکاران برای مصادره اموال مراجعه کرده‌اند. حدود ۲۰۰ نفر در این مجموعه مشغول به کار هستند. خواهشمندیم صدای ما کارگران را به گوش مسئولان مربوطه برسانید.
🔹
شهرداری منطقه ۲ کرمان
در خصوص آسفالت ‌کردن کوچه‌ها، کاملاً سلیقه‌ای با ارباب‌رجوع برخورد می‌کند و متأسفانه فریاد ما در کرمان به گوش کسی نمی‌رسد.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/459803" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxLzfan_x4kR7kpb2ieoqGZKwR9YHrSjzPtvjfupjYDkUbcaMaPqFoCMDTGg4F5XRjUdHw3tNucQlqmTQT5SnTr8ltk-o14YDyvPAue3mqMDErLJypb6pH3BZd8-gRmmCn2eXkkhOeZ-KHcP4KJdtJ_ZxToBeT3UUuF8Z_g7AN81QAuvAsKvhr_ODZzTSledfGCLl2zIRqvEkl-AaSAtCmyKqtpxeTEOA80mXMGA_TiVs1TtuFO1jErkwLvlFLJ2_wYuZyV2PBuvqLAbXap92L_KaW9zo-uVS7fLOfJwhk9zpMyhIobC9Q8gwf8B1H6eErLJDVcDbygFm4yYW4jBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xc-epM9Ts8yMOvVnV5twNw9IWgqg0tNUl5yJDZAT81eFQFp26I78TZaYTuk6mhhtb2atcU0h980BiGuWWU5sNvfiHuEzjAr67QvJ0gHikb7DuyrtsRfxTWDJv8cCOgkX-oKHBehPRZyL9UXBHQjE5wOb-xEE1J6XKdEiUXMslhKC-BqjM_63jpckrnfwNpoJi4X14ALxbxiPsfUxrrD2GI8ELX_tHnRuDrSzy1d4HfFyKYUr_6WMq3aI69yVmANYeCEt0mf0Suo1B2jbJB5-LYXn4-ouSsYF0pfbcFyiknyPXXOhRIra9reUiAwpONni8I9PPxYgvMphU4eVUNjeAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
نهاد مدیریت خلیج‌فارس: فهرست شناورهای متخلف بروز شد
🔹
برخی از این موارد با اطلاعات داوطلبانۀ مردم به‌دست آمده است.
@Fasrna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/459801" target="_blank">📅 22:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwXHFMCtGTefrarzMUR3vDgBXPd64B53DGyYxXaqTqeBwjfp-ehMq4wr9aJcrEMSf0vSlaWek5Bg4qWUnSKFTbh6hbX2RMgDxuHBZx8S3QUjhZ1aKYra9lJ5kIb5NagvDioZA1uT04qGLSdI2WRY1abLBuN_SuwO3mYkIpQhmc07acc-1X6A0v0FKcpVMWlmUxgEqcBxGuMR8RGwOZFUg2n9UJ-uaxDXQ463lEZA_q60xbl93MMB28IZJiWKgZmT7MkBPMpiG2T5ldlEUMbiKPhDFS5fmAEsDSMevgvDPr94wfPK7-PkOiaek0wRIX_nvUjnYDTv6-TisWiQA7MtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط جدید ارتباطی با صندوق بیمهٔ حوادث ساختمان راه اندازی شد
🔹
مدیر روابط عمومی صندوق بیمهٔ حوادث طبیعی ساختمان: از این پس بیمه‌شدگان می‌توانند با شماره‌گیری ۵۲۱۴۴، ضمن دریافت پاسخ و راهنمایی‌های لازم، روند پیگیری پرونده‌های خسارت خود را با کارشناسان ذی‌ربط دنبال کنند و از آخرین وضعیت پرونده خود مطلع شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/459800" target="_blank">📅 21:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5076db8a.mp4?token=UmgwXHGWYcvBTRNBAVCvJMkF7lNQ1mSjCHDMac2-9YGQQgHm5l22qvSbhLDWoCKnXXLGWjKQWsooFJQjkx68l22pDpAZfbPXkAoOOzxvbb2-eJxyypWkI4toBv6jrZ0KYGldkpfUZ7NX7dZLfwpMXE3AQ4UNd8MbCVQeISnGR3AlGBubrDoqPokS_S2UzRpxsA_7P-nEG6Xv8grArf83PpMl-1LnIbwh31Ds78UNuCSq98vlo7S_Llk3YU_-UAK7G9I12XKf_wt72HIKZs6awjl9ejI-tHmjsMcOzDeTGkcuwoZ_sKN0g1uVre8W9oPtk_LDcy7IdUSWtqUoKBGqEJkh-NjadhckVxXZPLQgRqybzkdZjY5aGy9fb-txqhlM4VNe32cQNFe361cnq8tQRYyrNXBOmNQXUDcqONm2TdfFnRhm3RtHNe8NyJMf9fiHPoQdMlRhIpuyBf0bB9mHa7ZuNsagRIEBjmcjsTSHExbVfpL4_yjfKpxnQALNq5mg8Swjq8ibDBspgqV0YFIpfoqd-_BgCPAp1Rbvgnp1o3d_WDG2ZDyc3YGK392QGhpdbVbY3OkApzxywKEAxIrRp--OUeEEVb9UQjD6zbefBjWZssfu3xzxmMb6vDWwWJ5kUVxWk1HUC2n1-Zajcg_euPW-HO0MbSd-YZopvK2zm8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5076db8a.mp4?token=UmgwXHGWYcvBTRNBAVCvJMkF7lNQ1mSjCHDMac2-9YGQQgHm5l22qvSbhLDWoCKnXXLGWjKQWsooFJQjkx68l22pDpAZfbPXkAoOOzxvbb2-eJxyypWkI4toBv6jrZ0KYGldkpfUZ7NX7dZLfwpMXE3AQ4UNd8MbCVQeISnGR3AlGBubrDoqPokS_S2UzRpxsA_7P-nEG6Xv8grArf83PpMl-1LnIbwh31Ds78UNuCSq98vlo7S_Llk3YU_-UAK7G9I12XKf_wt72HIKZs6awjl9ejI-tHmjsMcOzDeTGkcuwoZ_sKN0g1uVre8W9oPtk_LDcy7IdUSWtqUoKBGqEJkh-NjadhckVxXZPLQgRqybzkdZjY5aGy9fb-txqhlM4VNe32cQNFe361cnq8tQRYyrNXBOmNQXUDcqONm2TdfFnRhm3RtHNe8NyJMf9fiHPoQdMlRhIpuyBf0bB9mHa7ZuNsagRIEBjmcjsTSHExbVfpL4_yjfKpxnQALNq5mg8Swjq8ibDBspgqV0YFIpfoqd-_BgCPAp1Rbvgnp1o3d_WDG2ZDyc3YGK392QGhpdbVbY3OkApzxywKEAxIrRp--OUeEEVb9UQjD6zbefBjWZssfu3xzxmMb6vDWwWJ5kUVxWk1HUC2n1-Zajcg_euPW-HO0MbSd-YZopvK2zm8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش خبرنگار شبکهٔ سه از قشم: احتمال دارد تعداد شهدای حملهٔ دیشب آمریکا به یک مراسم عروسی افزایش پیدا کند
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/459799" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbe705fb9.mp4?token=Vopm46pZLa_MDbBPMJ5BZwB6siWCqfG8uvN1QnjR1mNDuJXfudEqEo7WMAdnbzckmbF5uw0xoAowAYm_WBSO90D7L2SUfmBKE7EeiDD1BDOWnmoHmtmL86oPjK2eN71WNTbuX1RKL6UP4sm2bXJHrkGDw4vtdmU6UDA5Ohs0NMMmNbklppTpNDhO0c9k8OsTNqlltzK4n51A2xBgD0AmKNHvVKngB3bigZ-XiGYXPmDbnHl866UzsYWcLKIhh4x-lMiVDDSoWCSzrTjvif7PiJG7oV3EgaMtLgCJenGcAP0niwfEZOetdOn7BpQuJo6-eNQib5NgddpcAcClHHYhJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbe705fb9.mp4?token=Vopm46pZLa_MDbBPMJ5BZwB6siWCqfG8uvN1QnjR1mNDuJXfudEqEo7WMAdnbzckmbF5uw0xoAowAYm_WBSO90D7L2SUfmBKE7EeiDD1BDOWnmoHmtmL86oPjK2eN71WNTbuX1RKL6UP4sm2bXJHrkGDw4vtdmU6UDA5Ohs0NMMmNbklppTpNDhO0c9k8OsTNqlltzK4n51A2xBgD0AmKNHvVKngB3bigZ-XiGYXPmDbnHl866UzsYWcLKIhh4x-lMiVDDSoWCSzrTjvif7PiJG7oV3EgaMtLgCJenGcAP0niwfEZOetdOn7BpQuJo6-eNQib5NgddpcAcClHHYhJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ، تحریم، کودتا؛ آمریکا دوباره نسخهٔ شکست‌خورده‌اش را کلید زد
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/459798" target="_blank">📅 21:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459797">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767fce29d6.mp4?token=jLJOMtRPUhRf7KnkSBsqJtSekChxFfZ05IfSCyQRbyI56UDRTxg7KNUxQhSbdWRctjnp1AqGepWDNJCPr9JCbTaeYVftaNzq-FK-MQClxmVNecRMwOZvAlNPQFbTGJ2PUBJJ8NQuR5VIfn1-tM8MXshQKhei4Z4Te0d7Gr9JixS9027pO1E0rQoTnxcxjPKlfGmMeh3cnhw8Ukv6REzKw_I9VjT5cbkBtGiFERzyVH85HI-IJe_XGEAr4fizSHk0Pwbr9eLSNBQaXaqblxN8oyS_A0S0HYiVO3ewB49Z5A1sWO-EfPtMs9FYxB8gIcGut_Utf82hGiU3Fb81M2Ddvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767fce29d6.mp4?token=jLJOMtRPUhRf7KnkSBsqJtSekChxFfZ05IfSCyQRbyI56UDRTxg7KNUxQhSbdWRctjnp1AqGepWDNJCPr9JCbTaeYVftaNzq-FK-MQClxmVNecRMwOZvAlNPQFbTGJ2PUBJJ8NQuR5VIfn1-tM8MXshQKhei4Z4Te0d7Gr9JixS9027pO1E0rQoTnxcxjPKlfGmMeh3cnhw8Ukv6REzKw_I9VjT5cbkBtGiFERzyVH85HI-IJe_XGEAr4fizSHk0Pwbr9eLSNBQaXaqblxN8oyS_A0S0HYiVO3ewB49Z5A1sWO-EfPtMs9FYxB8gIcGut_Utf82hGiU3Fb81M2Ddvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تارتار: استقلال روی اوت‌دستی کار کرده بود و روی همان هم به گل رسید
⚽️
هم ما و هم استقلال می‌توانستیم برنده باشیم. از مسئولین اصفهان برای میزبانی و از داور برای قضاوت خوب تشکر می‌کنم.
⚽️
حسرت می‌خورم که ۳ امتیاز را از دست دادیم. استقلال روی تاکتیک اوت دستی…</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/459797" target="_blank">📅 21:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459796">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0826c8057f.mp4?token=I1OrAsNdFO6taPkvgYGOc7KI1iRr4dWAbDaK2JEjLvh-ABfk2Bj--z2Sz7hg4vLxr6RgQQxLxUuiAquIHzwAag3fbgcMuyuSCkFhUKo3dAHs67_nQe7KoLHtE_FJO4uF1vQz_hokhiBqV9eWiwiAb76z0DwrcrZILMhm53IK7ki9WDjGUUseY-0kaR-PYftI2s2yUgJdPpKraekGUdKWbT5TF-9EFZtFuMOBOK8ng4g96Os5pxUW2HU-Q_XEo2LE6RI_3k3MxfZAo_XLkIS97-HCbts001BFuWUdRwlIYp5EHf-Ma4lZPKDPD7jucDS-XTSzGHdRBD1fg5uLQYY_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0826c8057f.mp4?token=I1OrAsNdFO6taPkvgYGOc7KI1iRr4dWAbDaK2JEjLvh-ABfk2Bj--z2Sz7hg4vLxr6RgQQxLxUuiAquIHzwAag3fbgcMuyuSCkFhUKo3dAHs67_nQe7KoLHtE_FJO4uF1vQz_hokhiBqV9eWiwiAb76z0DwrcrZILMhm53IK7ki9WDjGUUseY-0kaR-PYftI2s2yUgJdPpKraekGUdKWbT5TF-9EFZtFuMOBOK8ng4g96Os5pxUW2HU-Q_XEo2LE6RI_3k3MxfZAo_XLkIS97-HCbts001BFuWUdRwlIYp5EHf-Ma4lZPKDPD7jucDS-XTSzGHdRBD1fg5uLQYY_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند درصد دربی‌های جهان مساوی می‌شود؟
🔹
اختلاف چشمگیر نرخ تساوی‌ها در شهرآورد تهران با سایر دربی‌های دنیا. @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/459796" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459795">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQfRltv6i7zqe-bb6cCBNPFtRxdD1Vgzi-mQQLlSVQu2ClCoOYMMFyiZ9INVIT4ZWKzLlPI8kUuMgFBL0lmpI_eyQ6A6InjCJR2cgE0SzfgrDxo-umx8SjJayGqpaS_jgvfyojknjjDsWsVWOxV0sRNBR7vpoTmnB1VgSqRvaEF4wsCwo713_9Rmga-bzEIQdaom7QyxP8l5T7nPaFy30QTph5_DVeVfgcRvVyNc6g6_t2YpuwgG5YFjmnSkul02giR-ru-LYM-ZQXajeqIVdKYayBALXKoVeedMlUdMhDLvo0wlgsDzGHg7-5VMSiwDpvXSIB2pCO6C_yZWXWbxsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو، وزیر خارجه آمریکا: یادداشت تفاهم با ایران دیگر وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/459795" target="_blank">📅 21:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459794">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ec4730608.mp4?token=uv7-Mjy2gZ83ni3AsjJfb_sGpKiM6QVz-7VfMrrgni5YUZpLeiyM3NRcmAWPs4j599-D_vdZzuZxn3Yd2n7Iy7E9l98kPxRCwN8kZu9SU3fBQsylKZu8jgo2Z5cDEB4LzBOVAqr3YxqUHmiuHFxs2MdNlt7ZWL1VMBshugD8_rvg5KGIBvjgLOK6w65aH1QqAgPONAC-MeRpSYfD3RQlaf1i6437t9V8FXvqPhv7j5uR2Mn-80pwCDn-bqqlVJvCj5wNtHxA_9jmC6uu279G6Re4j5_a5fjb7uOa2uDyEJAwTsYEP8ooyVVL6oTcuxjRWfLsV0Za2b5zSjtTCOK1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ec4730608.mp4?token=uv7-Mjy2gZ83ni3AsjJfb_sGpKiM6QVz-7VfMrrgni5YUZpLeiyM3NRcmAWPs4j599-D_vdZzuZxn3Yd2n7Iy7E9l98kPxRCwN8kZu9SU3fBQsylKZu8jgo2Z5cDEB4LzBOVAqr3YxqUHmiuHFxs2MdNlt7ZWL1VMBshugD8_rvg5KGIBvjgLOK6w65aH1QqAgPONAC-MeRpSYfD3RQlaf1i6437t9V8FXvqPhv7j5uR2Mn-80pwCDn-bqqlVJvCj5wNtHxA_9jmC6uu279G6Re4j5_a5fjb7uOa2uDyEJAwTsYEP8ooyVVL6oTcuxjRWfLsV0Za2b5zSjtTCOK1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دربی تهران در اصفهان با تقسیم امتیازات تمام شد
⚽️
استقلال ۱ - ۱ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/459794" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459793">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c689a1f03.mp4?token=jTNbdw5eQdpHSaJODsLoDOA_xfAf7KIm7Liy4EiztEYLlHsxgJX4uKsHRVRPEBTsJa-nCQ-rhfaJsRA3GH3M6DbXe6Qto_TC-XSM6-8bSb3Z41mT_74gUNV253nhhP9Y4nARF45ots8_-iISLUNquEmNZGIcNlGugk5k18NmqOZDH6lyxb0KIEW_tYMc6AZJgWC4OeyuHtwAl84l_Do-cd0Fbzzs9HnF8osUrUWHsTjxhKb_DBa52kfsL_if_XYLdH0_Oa_B-PhZY_4Vq7O9KUGI9IkfmpJUh_VRt7k638tTaFp3nol0DhwhRdCkpgdX4esJFWvGhNgwM-88AU_hGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c689a1f03.mp4?token=jTNbdw5eQdpHSaJODsLoDOA_xfAf7KIm7Liy4EiztEYLlHsxgJX4uKsHRVRPEBTsJa-nCQ-rhfaJsRA3GH3M6DbXe6Qto_TC-XSM6-8bSb3Z41mT_74gUNV253nhhP9Y4nARF45ots8_-iISLUNquEmNZGIcNlGugk5k18NmqOZDH6lyxb0KIEW_tYMc6AZJgWC4OeyuHtwAl84l_Do-cd0Fbzzs9HnF8osUrUWHsTjxhKb_DBa52kfsL_if_XYLdH0_Oa_B-PhZY_4Vq7O9KUGI9IkfmpJUh_VRt7k638tTaFp3nol0DhwhRdCkpgdX4esJFWvGhNgwM-88AU_hGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحریم از آمریکا؛ پاسخ از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/459793" target="_blank">📅 21:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459792">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-PAbX-DDA9qQaDpf-ptFGqeyGgjn7ia2l4yeKL7pQn0-ommfYWA4el9ODYI2fKMNY50toOoI4PpcT-t7eXj3miZ4mxgellyJoMM8RC07BatkFF2OQeabWXUWoBoeRd1e0uaV6F9K9_FfJv61qlc96XM3yDw5DVG4-N-ZVm1om_Y3LtNUfiVDfrUvSiJbwUeRb7lP8zYqZv1V8F4qwgrYDhi47p1U-tW30RdCNW6P61mtyaIwyvNP4VLfMg2neZSmuk-hZgXd-syAknVqOfqYA2891AQa35v4OVPY3OhD355AMbyBiUnt2QL2MbhbPey0KuiFHrFeSUPSmlP5EpSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوت چین به نظم جدید منطقه‌ای در میانۀ تردید درباره ضمانت‌های آمریکا
🔹
رئیس‌جمهور چین از کشورهای خاورمیانه خواست در برابر نفوذ خارجی ایستادگی کنند و درباره بازطراحی نظم امنیتی منطقه گفت‌وگو کنند؛ شی امروز در دیدار با السیسی رئیس‌جمهور مصر این اظهارات را مطرح کرد.
🔹
این سفر، نخستین سفر شی به قاهره در یک دهه گذشته است و در شرایطی انجام می‌شود که پکن تلاش دارد همزمان با ادامه جنگ آمریکا و اسرائیل علیه ایران، نفوذ خود را در منطقه خاورمیانه گسترش دهد.
🔹
اظهارات او همچنین در شرایطی مطرح می‌شود که جنگ اخیر علیه ایران سودمندی تکیه به ضمانت‌های آمریکایی در منطقه غرب آسیا را به شدت زیر سوال برده است.
🔹
در چنین شرایطی، ناظران می‌گویند پیشنهاد شی جین‌پینگ برای تقویت همکاری‌های منطقه‌ای و مخالفت با مداخله خارجی می‌تواند نشانه‌ای از تلاش چین برای ارائه خود به‌عنوان یکی از بازیگران اصلی نظم امنیتی آینده خاورمیانه باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/459792" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwnVmuHHgEgACJHxm9R4rYKxa85GBEzlbe4QYv_1G6DgdiU4SLrX2mOr3hh3BICkYFQS1lX8dFB6nrBbN1g_vu80XBI2xWhIOncFyJqUktG-2x_w5-iDHdr-uhEH4W4rrlr6rbqeGw20cYXtuUogoXBxR1Uawkj_KdrzIBGFAnfVIdnvfUT5RKOIUmem5TcqT-lcly5qfjxpNfwCByiIL3JUAMfOurTpX_t0Dv_e_eSVjMW0IOSLH9Q6Sc08bDuXMrBLwjDPnLhW70jpQa1D91XYJjKkQvAxdo5IIvgcV6Gs6WHRTJHQ7ecsejsPSyMt7Jc4MKjbvWF0s2v5gXQB6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حرکت دیدنی محبی و توپی که بازهم وارد دروازۀ استقلال نشد  @Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/459790" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459788">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8480d409cf.mp4?token=HAgyUkp5AzcSatYV2hCzg9oV4cLxWFCoH-egCZAmQuyrXHeDKeKZ2KF8eozZ59D42SBa9vS4h4CrpRYuzyLxNYyKNJSO-wEJZXxSbwSAmR_WF50iCCDSBxN7NAQdhN_N3Ytqhb8BezajZFfcALBbkA30xeXiv-A2bvfQwGHzyn8Goy-xuWTJ30nOIlU16pigYItA-pgtYOq68SAwwoxgXEwpRNPsMBdHwsKsNzi9PaRpPRzgtr5MTRapK2OEDh_Kj6hj9nWBQTKjZStz10yC4z7laY-Is94eoU2K_n3eIgTjCeKqYqZkURc3uPaH8s69yMGBOp9zaba8EeiessRhxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8480d409cf.mp4?token=HAgyUkp5AzcSatYV2hCzg9oV4cLxWFCoH-egCZAmQuyrXHeDKeKZ2KF8eozZ59D42SBa9vS4h4CrpRYuzyLxNYyKNJSO-wEJZXxSbwSAmR_WF50iCCDSBxN7NAQdhN_N3Ytqhb8BezajZFfcALBbkA30xeXiv-A2bvfQwGHzyn8Goy-xuWTJ30nOIlU16pigYItA-pgtYOq68SAwwoxgXEwpRNPsMBdHwsKsNzi9PaRpPRzgtr5MTRapK2OEDh_Kj6hj9nWBQTKjZStz10yC4z7laY-Is94eoU2K_n3eIgTjCeKqYqZkURc3uPaH8s69yMGBOp9zaba8EeiessRhxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رسانه‌های خارجی از شبی سخت برای پایگاه‌های آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/459788" target="_blank">📅 21:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459787">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f18211e5a.mp4?token=HIySaik5shU-V7bYcvGcqyfNOqK0ApOWfmTWbwS3ju4Gx2JiAzsnlI-o_pOH8ICePrOI0k6Rigi8p6aanccUXGcZEeoJQEjDcg50Jr6As2-YDc4QiK6EcmQAHX7lnwt-YtoQpMWWoPYF2MUVjWksIeVMN6ZfxswxFIjwlckTZ2mIpM527vUR-n3KZoe9W4JFtsvg5oJpo2vvKZscZtPhvs-rLqCppEcl6a-BTx5emTAwP-A_IMNLWXgeqgvyqPUQIHMzgzE_c-jiDAYy9EQ0Mmy1P05Bqe8b4s_GSmJ1J0Uj1ppzRj_VfRtzvQwcD5alFj1dvx-OLWnN_lIb4UTRy5B1DcZh1ZNNgK7sVTG_SKt5nR6DCl1Qod-6rOZvbdv5w6jio2Gp3TL2OxCCrZVVRo8LdlYNhRiOmP1tt7q7ZoKQZqj9ExV2QinwfKqMYMn_-IK4Nh4dmCpv5j8T8AMQRRAgfPW5UJ_pi6luwRki-qo757W_ZFP4vh81bS8ooz2lOhxF26Mfybq_s5V9CQ6jWg70zAzd64Q1en9t9PCjvSkWcsdsY-eWMp7_krGTqlcmkI7dkXNwgBzlnYafS_pCLzXDJp5VVWEjxm_2QTGsRkwhAHdvAoQZIZ0DzL-ePZ0X9vcy3YXlMk6nBaRzg8xqvNZSh7fGRCn5dCaYIiOhu6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f18211e5a.mp4?token=HIySaik5shU-V7bYcvGcqyfNOqK0ApOWfmTWbwS3ju4Gx2JiAzsnlI-o_pOH8ICePrOI0k6Rigi8p6aanccUXGcZEeoJQEjDcg50Jr6As2-YDc4QiK6EcmQAHX7lnwt-YtoQpMWWoPYF2MUVjWksIeVMN6ZfxswxFIjwlckTZ2mIpM527vUR-n3KZoe9W4JFtsvg5oJpo2vvKZscZtPhvs-rLqCppEcl6a-BTx5emTAwP-A_IMNLWXgeqgvyqPUQIHMzgzE_c-jiDAYy9EQ0Mmy1P05Bqe8b4s_GSmJ1J0Uj1ppzRj_VfRtzvQwcD5alFj1dvx-OLWnN_lIb4UTRy5B1DcZh1ZNNgK7sVTG_SKt5nR6DCl1Qod-6rOZvbdv5w6jio2Gp3TL2OxCCrZVVRo8LdlYNhRiOmP1tt7q7ZoKQZqj9ExV2QinwfKqMYMn_-IK4Nh4dmCpv5j8T8AMQRRAgfPW5UJ_pi6luwRki-qo757W_ZFP4vh81bS8ooz2lOhxF26Mfybq_s5V9CQ6jWg70zAzd64Q1en9t9PCjvSkWcsdsY-eWMp7_krGTqlcmkI7dkXNwgBzlnYafS_pCLzXDJp5VVWEjxm_2QTGsRkwhAHdvAoQZIZ0DzL-ePZ0X9vcy3YXlMk6nBaRzg8xqvNZSh7fGRCn5dCaYIiOhu6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مکتب این مردم، مکتب ایستادگی است
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/459787" target="_blank">📅 21:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459786">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7W7YtzYFG9_8i3iFisMf-1ZGW5_w0b5_CLmhc_vhsf1PFUxSDQNP23v82WEXZxHCvU0xH9JJVIa07JBkh-YspmO-Ffyp53gknx_miGXZZdaGAdF3SrII8J0CXNKiGJCtr5Yk_ucZCVmn2XPMtVtg-KHMf77kEncfFL-hj2s0Ut5H7x-Y5qdFOqa0IYZdzMIbePepVGOFAUmxti3CkGsk0XdDvZCSyWfwUWNBq8VFVRI9UBzuDZ-6GBfP4R0xAPPftdyXjH9nbFLilZiPucZGrMqRKj_E7NG_MZamucl8D7b2-6srjSNmfCGJKFnVE448WDX-Q9w_FlhkDcsHMg43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار جدی مقام مستعفی ارتش آمریکا به ترامپ درباره جنگ علیه ایران
🔹
خبرنگار برکینگ‌نیوز گزارش داده معاون وزیر جنگ آمریکا پیش از استعفای خود با ترامپ دیدار کرده تا به او هشدار دهد که جنگ با ایران دستیابی به اهداف سیاست خارجی دولت را غیرممکن کرده است.
🔹
اما ترامپ در واکنش به این هشدار، در تمام مدت دیدار فقط درباره سالن رقصی که در حال ساخت آن است صحبت کرد و این برخورد باعث شد دریسکول استعفا دهد، زیرا به این نتیجه رسیده بود که دولت ترامپ «محکوم به شکست» است.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/459786" target="_blank">📅 21:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459785">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98edf43d2.mp4?token=ekhgtyqAu7SduPBADjFIyPQnf0caooS3mFuZbvrqwZ49hNGO_OKHD5z_PrpiH7nSJg2MX6rcF239K27vysfSMExv91b88SNBoGHnDnKMo42H5LDo2xV4Ld4JRzWdADrT33fJvgRgD_lUnuLMN5LdgSIgRvf0Gkt0l1EW5bUqV9Imo6Pw_67cuH_i00wUru86xZ3avDG6Ejwzvhbx-A4UGhPgunx7FATyPhuL3apkGG_ulB0WwtpTZy5kEXF44ukHmBJkZgIHdKUEfNt8UZjDAs4b05nOyGBkb16OJuggiounMv2C_oYtSw_MoeNPt0pplCZXI1AixItm23DPsLZDow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98edf43d2.mp4?token=ekhgtyqAu7SduPBADjFIyPQnf0caooS3mFuZbvrqwZ49hNGO_OKHD5z_PrpiH7nSJg2MX6rcF239K27vysfSMExv91b88SNBoGHnDnKMo42H5LDo2xV4Ld4JRzWdADrT33fJvgRgD_lUnuLMN5LdgSIgRvf0Gkt0l1EW5bUqV9Imo6Pw_67cuH_i00wUru86xZ3avDG6Ejwzvhbx-A4UGhPgunx7FATyPhuL3apkGG_ulB0WwtpTZy5kEXF44ukHmBJkZgIHdKUEfNt8UZjDAs4b05nOyGBkb16OJuggiounMv2C_oYtSw_MoeNPt0pplCZXI1AixItm23DPsLZDow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت پای چپ علیپور با اختلاف کم از کنار دروازۀ فرعباسی به بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/459785" target="_blank">📅 21:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459784">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b0bce5d.mp4?token=VNkJi_EHPshbC5p2fABpTT7zY38t08QNqCtdosw4hkIjxj0_0xCGL4mlTHQ74XLKPC5Fej_3lfUX6rkI6GYYGAFmtTrBpwa3n-QtE31TydAtfv5PnslCUpakhL63srLtxAXdiU8xkdJ33UjdmtKMe1vPN4rwL3mKsSG0WTGcG2iFYSvxMnj2TEqFPVxabxpxp2O_aLaxsm_UnSl705gOvxT_PZJqxefj11RUN8jxbccQOEbAx54lUmx0-2d7n5MRB_A5eDggyK9K9iTnRdaMFiOb60HNWZRMd6V-oJGsyQTpRqR1wp_SJxAMFum-6_mRMgfeh8ngk8ONS63rYBGMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b0bce5d.mp4?token=VNkJi_EHPshbC5p2fABpTT7zY38t08QNqCtdosw4hkIjxj0_0xCGL4mlTHQ74XLKPC5Fej_3lfUX6rkI6GYYGAFmtTrBpwa3n-QtE31TydAtfv5PnslCUpakhL63srLtxAXdiU8xkdJ33UjdmtKMe1vPN4rwL3mKsSG0WTGcG2iFYSvxMnj2TEqFPVxabxpxp2O_aLaxsm_UnSl705gOvxT_PZJqxefj11RUN8jxbccQOEbAx54lUmx0-2d7n5MRB_A5eDggyK9K9iTnRdaMFiOb60HNWZRMd6V-oJGsyQTpRqR1wp_SJxAMFum-6_mRMgfeh8ngk8ONS63rYBGMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان این‌گونه برای آمریکا تنگ شد و عقب نشست
@Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/459784" target="_blank">📅 21:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459783">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d328fba3.mp4?token=KK8VvtHoTP8uefEcYeMilafWKMKy-uAM6DqPOZlxzV5rCw80sXzfaTcxS6db0y8Bqm1778J5LePdYuMTUSpPfv4tnwMusx9qS0P8A92wKgpPbzgL0JZfsFN1foGkaRcW_omC0VJXJycd8ATbF4cI82uFSSKTbjCu2GxfmYp7H29556B-ITkF7rMMRVqqkx2XDopo-FDt07ESQSvIulJSEb9H-nQO7jV1vMF0CvaWPVwNbCWhW4Ri14EMp71iSR2yBKcdnWt_zMntj-DojY5D8L-lENmwh6V9IK-_YvmQvr7kdsCfVtbhfhPMDKbsdYKz-zO0kIGfRx-AR93lF8456w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d328fba3.mp4?token=KK8VvtHoTP8uefEcYeMilafWKMKy-uAM6DqPOZlxzV5rCw80sXzfaTcxS6db0y8Bqm1778J5LePdYuMTUSpPfv4tnwMusx9qS0P8A92wKgpPbzgL0JZfsFN1foGkaRcW_omC0VJXJycd8ATbF4cI82uFSSKTbjCu2GxfmYp7H29556B-ITkF7rMMRVqqkx2XDopo-FDt07ESQSvIulJSEb9H-nQO7jV1vMF0CvaWPVwNbCWhW4Ri14EMp71iSR2yBKcdnWt_zMntj-DojY5D8L-lENmwh6V9IK-_YvmQvr7kdsCfVtbhfhPMDKbsdYKz-zO0kIGfRx-AR93lF8456w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی استقلال به پرسپولیس توسط آسانی در دقیقۀ ۶۰
⚽️
استقلال ۱ - ۱ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/459783" target="_blank">📅 21:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459782">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQFyPzrBUMfnKa-hl6sRLMmG6Dl0rLcb535Vy36SupPvd1nMRTrXkb-13bZ0gvW1rS8yy0LpDzAQ3bTRy_dT5GorTphtYSaPslDSNnWrCLRrvN0GBhCFNg621a3sAMVsRhSrWJg7MCBmO1764yBc-Gy9ltC4IR78sHzY9ty41Ku6jI4cHhB6JvRoeeOV8xbLgcKHyU7WUtcNd8dPjr668kfNSQVz8_2j4Ozdlm4AHSDK0uSowkm_dfEZ3zjt0zarZZx7YZR6p-p8qDNgpyPepLFMprBEQZCrXdqNbYaTgXdRs0l5F7B7VzMh9eDtNuRHUrPCYfcaw45kqgBEjuEKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل تساوی استقلال به پرسپولیس توسط آسانی در دقیقۀ ۶۰
⚽️
استقلال ۱ - ۱ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/459782" target="_blank">📅 21:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459781">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb0ccd11e.mp4?token=I31Bi5zT_LlkU4_lyo4jKjpUDsyzrOV0iTSoimVz_FVbi2FSKV_A2mpYb5cgp-C4DrJqJ7bfGrdjA2RDng90AHlawudBClGGHWutKVMyznNmrRZp96BNFU02Wy3i5FFX7wkV2Tc47JjQ9P4odVDLRIdSknUIF2DMNLmjsBPkxl7ftU8tB94myL2o_HKJRkcEx7CYC3_2-b0RNOJ2Yjfcwuz5jmSfP4lEP6kShp5AnmmQN8Jo52-KpmqSUe-tG3W0ckPFEmOuBbiWK6eYnJ5nVCcCPAxeDOVJyMtwGnGv3I6kP51TC0BoxffxnsfxcvB5qm4UkTcof4HNHVNo97Mh3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb0ccd11e.mp4?token=I31Bi5zT_LlkU4_lyo4jKjpUDsyzrOV0iTSoimVz_FVbi2FSKV_A2mpYb5cgp-C4DrJqJ7bfGrdjA2RDng90AHlawudBClGGHWutKVMyznNmrRZp96BNFU02Wy3i5FFX7wkV2Tc47JjQ9P4odVDLRIdSknUIF2DMNLmjsBPkxl7ftU8tB94myL2o_HKJRkcEx7CYC3_2-b0RNOJ2Yjfcwuz5jmSfP4lEP6kShp5AnmmQN8Jo52-KpmqSUe-tG3W0ckPFEmOuBbiWK6eYnJ5nVCcCPAxeDOVJyMtwGnGv3I6kP51TC0BoxffxnsfxcvB5qm4UkTcof4HNHVNo97Mh3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ورزش: بیش از ۳۶۰ مکان ورزشی در جنگ مورد اصابت قرار گرفت
🔹
در تهران ۳ مجموعۀ ورزشی در اثر حمله دشمن صد درصد تخریب شدند. @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/459781" target="_blank">📅 21:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459780">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c062f89b1b.mp4?token=duDY7FFzUR4KZAnTdnFOFmWcUcCn7BsymB-qaGncj-A9z-OMcXCNwyf95rmPc9TEPJNR-NLOzGRrQt_EObUdxKQX4RAdDKuBvMGb9Q77H46SVOg6rFR_Stw33RN5H32J05jkzh2Wn5cvloxSt8cagawqJMqQKQ1D576QZto1kZf1FeBwLVD9zNACS0FklAfTZONgDa4iotWHOuHSDctiXsEmYVbD--RvgwnwsEP-8KRfG8oGnIv_e48xtfGTvjXhT_nyzCwuKrnJoc1qp-kMOZvdWtJTaUc2JGsAzIVp0gVqHMBbK-4OQVIEti2bXc9Vxodrkoa6ibl5swSpuMZguQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c062f89b1b.mp4?token=duDY7FFzUR4KZAnTdnFOFmWcUcCn7BsymB-qaGncj-A9z-OMcXCNwyf95rmPc9TEPJNR-NLOzGRrQt_EObUdxKQX4RAdDKuBvMGb9Q77H46SVOg6rFR_Stw33RN5H32J05jkzh2Wn5cvloxSt8cagawqJMqQKQ1D576QZto1kZf1FeBwLVD9zNACS0FklAfTZONgDa4iotWHOuHSDctiXsEmYVbD--RvgwnwsEP-8KRfG8oGnIv_e48xtfGTvjXhT_nyzCwuKrnJoc1qp-kMOZvdWtJTaUc2JGsAzIVp0gVqHMBbK-4OQVIEti2bXc9Vxodrkoa6ibl5swSpuMZguQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت دیدنی بیفوما راهی به دروازۀ آبی‌پوشان نداشت  @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/459780" target="_blank">📅 20:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459778">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e73aa861.mp4?token=DQWYYn8CmeMnGkkGlivPXcrDJA_ei-A9WP4vFo3kM1CgVf0sxSdW4DU6eJjTRMGqzaLJMi2lHWazBDyk4zoOi3fUuG1v_muCuqkyiGBAiPhkp2yhVYFpCkI8Fs--msVB4TDyLZgYHuGk_IH8y1SXPhGQLQRfXY9SPGAm1aFAhyLvWyEPvdCDkMb1uwb9yn6iuQjDnfjwaDvtIlrD4CvV_8sng7Zjay2QDzsfai-BNz-x7dhAIpdAQ4d1uX_l-5GXnMekKWWBhYzCc4ed-xKmO-r_4oQxMgOjrXYi-eONdSy5bXTr1f1psFdXkg5lb1t_9yF-sVfgQe3Cp_BQ5wE52w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e73aa861.mp4?token=DQWYYn8CmeMnGkkGlivPXcrDJA_ei-A9WP4vFo3kM1CgVf0sxSdW4DU6eJjTRMGqzaLJMi2lHWazBDyk4zoOi3fUuG1v_muCuqkyiGBAiPhkp2yhVYFpCkI8Fs--msVB4TDyLZgYHuGk_IH8y1SXPhGQLQRfXY9SPGAm1aFAhyLvWyEPvdCDkMb1uwb9yn6iuQjDnfjwaDvtIlrD4CvV_8sng7Zjay2QDzsfai-BNz-x7dhAIpdAQ4d1uX_l-5GXnMekKWWBhYzCc4ed-xKmO-r_4oQxMgOjrXYi-eONdSy5bXTr1f1psFdXkg5lb1t_9yF-sVfgQe3Cp_BQ5wE52w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربه آسانی به تیر دروازۀ پرسپولیس خورد  @Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/459778" target="_blank">📅 20:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459777">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34076244b1.mp4?token=JYCe9mSTZkUjfKF8MBmvpXJ190cYr96xuZV1x1mWZ2mux8IbXnwNYCH0wnTqtLsulu2gcjV-BPErczqpO1ms_95kbHr_sd4_cUch76YICWLtG8gCmXet21kZCTJZwBQ4KxynpyXmXeI0l9_pFzdgch1fsCp5Du3I4bhgVaK7E6ITTt3ickuEOkRfbx9D0q6uzgJvv_RZtr-B3YNF6loAqj9lrsjq4kPhLOAEwmSFepsdYymKMBaSdlM5U1LmES-wun0IVVEoMywPnttkwYjTHRiAX_CIMU39ZM3lnSptThglBt6bhbNi5b7GJLPIv3jhxnq-1bmEukqm0fgA44RmHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34076244b1.mp4?token=JYCe9mSTZkUjfKF8MBmvpXJ190cYr96xuZV1x1mWZ2mux8IbXnwNYCH0wnTqtLsulu2gcjV-BPErczqpO1ms_95kbHr_sd4_cUch76YICWLtG8gCmXet21kZCTJZwBQ4KxynpyXmXeI0l9_pFzdgch1fsCp5Du3I4bhgVaK7E6ITTt3ickuEOkRfbx9D0q6uzgJvv_RZtr-B3YNF6loAqj9lrsjq4kPhLOAEwmSFepsdYymKMBaSdlM5U1LmES-wun0IVVEoMywPnttkwYjTHRiAX_CIMU39ZM3lnSptThglBt6bhbNi5b7GJLPIv3jhxnq-1bmEukqm0fgA44RmHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربه آسانی به تیر دروازۀ پرسپولیس خورد
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/459777" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459775">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ca56d7e9.mp4?token=BDA-kO-K9rSf74yQAnS-krFo1LY7Y_2DENnQ1lgqN4lBkyqVltY1cw-ZYF3MF0Uh_drOtnk6saQwZlBqheCoPO2hLyMYolLocXghb4EMAC22ghvRFIgw2SsdsoQMt-ZVtx15zfhLdZi5k0bKJp18QYXZvlycb8OylBq42aI_rfoE52Hro01JRQCRdx-eEDgK8VBZ2B9qVudSwC5bD-r_PkSUcPq8x4w1FsRb5WZif_8vX90o4gYgMmP9C1ze1gCIaSoRKElZcaYI74o7R_u65OcaG-357LNV-qWl9f7m1cAOTo83olItFmmtCrpm0ClmrLh022WIqdy3DTJ2BOtSdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ca56d7e9.mp4?token=BDA-kO-K9rSf74yQAnS-krFo1LY7Y_2DENnQ1lgqN4lBkyqVltY1cw-ZYF3MF0Uh_drOtnk6saQwZlBqheCoPO2hLyMYolLocXghb4EMAC22ghvRFIgw2SsdsoQMt-ZVtx15zfhLdZi5k0bKJp18QYXZvlycb8OylBq42aI_rfoE52Hro01JRQCRdx-eEDgK8VBZ2B9qVudSwC5bD-r_PkSUcPq8x4w1FsRb5WZif_8vX90o4gYgMmP9C1ze1gCIaSoRKElZcaYI74o7R_u65OcaG-357LNV-qWl9f7m1cAOTo83olItFmmtCrpm0ClmrLh022WIqdy3DTJ2BOtSdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ موقعیت متوالی برای استقلال که توسط آسانی و قلی‌زاده ازدست رفت  @Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/459775" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2bdd4b133.mp4?token=QB8GzAR5w2H5B4EhVxp1otNBLZSURy1yLBEHRIFKGfO0wrg1An2kBuoXSzqOBc-ekOHkjOEjgj4L4t6Tj7Ee7Vv-Gj7sHkn9NlS9lFV4rZfyW-Bs9_ZQisGYLakq6FwL_9uas3clB6QpMHUbZUvz-yR2l-Lpo2L8ejmEHw-pLXpP1SskNDodRtHJ4NrB6Frkh1Z0TN6o0U2JRbc0dM2pVrkRhwmBkjeFOEc0i9rpJuTE6cJWRnLtCatzOvbezDJ5avaF6yVwnhQPH0Y4kLW3kIJk-_QFkKaZWDOdScSiqJ6LgnaLeYyALJyFkjPhVXtFcgWCCevTe1HhH_RNM0u_6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2bdd4b133.mp4?token=QB8GzAR5w2H5B4EhVxp1otNBLZSURy1yLBEHRIFKGfO0wrg1An2kBuoXSzqOBc-ekOHkjOEjgj4L4t6Tj7Ee7Vv-Gj7sHkn9NlS9lFV4rZfyW-Bs9_ZQisGYLakq6FwL_9uas3clB6QpMHUbZUvz-yR2l-Lpo2L8ejmEHw-pLXpP1SskNDodRtHJ4NrB6Frkh1Z0TN6o0U2JRbc0dM2pVrkRhwmBkjeFOEc0i9rpJuTE6cJWRnLtCatzOvbezDJ5avaF6yVwnhQPH0Y4kLW3kIJk-_QFkKaZWDOdScSiqJ6LgnaLeYyALJyFkjPhVXtFcgWCCevTe1HhH_RNM0u_6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشته‌شدگان دی‌ماه همچنان درحال افزایش‌اند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/459774" target="_blank">📅 20:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459773">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اصلاحات و تمدید مهلت انتخاب‌رشتۀ کارشناسی ارشد ۱۴۰۵
🔹
سازمان سنجش: مهلت انتخاب رشته و ویرایش انتخاب‌ها تا پایان پنجشنبه ۱۲ شهریور تمدید شد.
🔹
داوطلبان می‌توانند رشته‌محل‌های جدید و اصلاحات دفترچه را در سایت سازمان سنجش مشاهده کنند.
🔹
داوطلبانی که پیش‌تر انتخاب رشته کرده‌اند نیز تا ۱۲ شهریور فرصت ویرایش انتخاب‌های خود را دارند.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/459773" target="_blank">📅 20:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459772">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارهای کنترل‌شده از ۱۲ تا ۱۶ شهریور در بوشهر
🔹
فرماندار بوشهر: عملیات انهدام مهمات عمل‌نکرده متعلق به حملات جنایتکارانه آمریکای صهیونی در تاریخ ۱۲ شهریورماه الی ۱۶ شهریورماه از ساعت ۸ صبح الی ۱۲ ظهر در حوالی پایگاه دریایی بوشهر انجام می‌شود.
🔹
انفجارها در این بازه زمانی کنترل‌شده بوده و جای نگرانی برای شهروندان عزیز نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/459772" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459771">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGP1tYcf-HfRAXLOn6WAkMIKAyCwe1epXvPvAPjuSKldj1-3zhSTDXnpgOJFnmmVnj9w2wsBYm98YUopfb6yGp3TVrpHNxfcrqGVZEmfy8cvQ6g2ch7eIYNOJZbsNOEuJuZwvpWU8ioqGSyb0RII_7YWU0z-0Ao14EQr6viCSQsjrmYXBT-qD2Oc7CbP5mCyPibp5VSr38FW23iIthZgPqosKvTN_o4o8gs2xSUKNnLfiRquaydvbWjTwqIL1haoBEnNsMPpaOCMM4JM0i8F22EUwJvWkDFOF-SnC4v1mX25M4JhS8xoGXXGUnDmpefOfwKnmxjZQ57diomJp9DqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دبیرکل نجبای عراق به آمریکا: بعد از ۳۰ سپتامبر، سربازانتان سالم برنمی‌گردند
🔹
شیخ اکرم الکعبی: اگر یک سرباز آمریکایی بعد از  ۳۰ سپتامبر در عراق باقی بماند، اجازه نخواهیم داد سالم به خانه بازگردد و تنها اجساد آن‌ها از عراق خارج می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/459771" target="_blank">📅 20:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459770">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c530dda0e.mp4?token=aXwhI7TccVVH_Ynwx_NWd7MEJ5_pOFU5CWXoclYMtEb8Dt3bMRVrZcETEpRZ9infU_wZwsQetXUryKvg_Cn2TZSUa7SkDssIldLtwh44xMCb7yUEJlDEOO1R3PfZCDeVjGR8bixEKi899Ti5Cz-obg0Bi02-3rkIYx3R_prFgw1Wdb1ZYR5f7yjOgem5xeKKA7WB7TRQLYeF2-YcgOMxLPjsQqh6PN_FsOMYB8TQQBq_l6tW4IemO8wQZw8heQlvA6ojtK8mq1S7xitAd0QHjZqoPLXYkB43ZoQz1ZZN5EB_UvRkwZbl_3eYea5uj5MkifzAQyopZnb2QsA6OfmlUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c530dda0e.mp4?token=aXwhI7TccVVH_Ynwx_NWd7MEJ5_pOFU5CWXoclYMtEb8Dt3bMRVrZcETEpRZ9infU_wZwsQetXUryKvg_Cn2TZSUa7SkDssIldLtwh44xMCb7yUEJlDEOO1R3PfZCDeVjGR8bixEKi899Ti5Cz-obg0Bi02-3rkIYx3R_prFgw1Wdb1ZYR5f7yjOgem5xeKKA7WB7TRQLYeF2-YcgOMxLPjsQqh6PN_FsOMYB8TQQBq_l6tW4IemO8wQZw8heQlvA6ojtK8mq1S7xitAd0QHjZqoPLXYkB43ZoQz1ZZN5EB_UvRkwZbl_3eYea5uj5MkifzAQyopZnb2QsA6OfmlUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیشب اولین‌بار نبود که آمریکا به یک مراسم عروسی حمله کرد؛ آمریکا در این جنایت هم سابقه دارد
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/459770" target="_blank">📅 20:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459769">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تشییع شهدای مظلوم عروسی کوهستک فردا برگزار می‌شود
🔹
روابط‌عمومی سپاه هرمزگان: مراسم تشییع پیکر مطهر شهدای مظلوم مراسم عروسی کوهستک که در جریان جنایت رژیم آمریکا به شهادت رسیدند، پنجشنبه برگزار می‌شود.
🔹
مکان: شهر کوهستک، از بلوار ورودی شهر تا گلزار مطهر شهدا
🔹
زمان: روز پنجشنبه از ساعت ۱۶:۰۰
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/459769" target="_blank">📅 20:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4d5a9b71.mp4?token=auvg8Y0HVaz8xIWXhxOWO9a9KchMIxdalgjpUdAPdw4NOBPXpfMt4OU2-xMWXIk6hVzOi7nfYsv1dy9hVO9qy9oZZduzYERXC_1WNwg3Gh4GVUwt4RRS9IYLG36BVX5xwPqxjCjiW3nJxTfzumxewQhsAAH9Pe4SYr9HBTKH1JjqAYnsj-7gQBDgpaxRyBOmztQYHnrqSE6uw15yUUihGZbg4CgaMmQLF-UGMzID-IsJtD1bQTBIk_Q9Dbvb7Z3kTbvkThQtcQmeBY7o9xTMMEaOUl6xSo9kf3d6GD3ag-cT10T3aylwJfA1MU70V35KBi5LhRcBlAYYWFZCpH_5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4d5a9b71.mp4?token=auvg8Y0HVaz8xIWXhxOWO9a9KchMIxdalgjpUdAPdw4NOBPXpfMt4OU2-xMWXIk6hVzOi7nfYsv1dy9hVO9qy9oZZduzYERXC_1WNwg3Gh4GVUwt4RRS9IYLG36BVX5xwPqxjCjiW3nJxTfzumxewQhsAAH9Pe4SYr9HBTKH1JjqAYnsj-7gQBDgpaxRyBOmztQYHnrqSE6uw15yUUihGZbg4CgaMmQLF-UGMzID-IsJtD1bQTBIk_Q9Dbvb7Z3kTbvkThQtcQmeBY7o9xTMMEaOUl6xSo9kf3d6GD3ag-cT10T3aylwJfA1MU70V35KBi5LhRcBlAYYWFZCpH_5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقلال برای گلزنی چند سانتی‌متر کم آورد  @Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/459768" target="_blank">📅 20:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697477a71e.mp4?token=Vc3E3iduQwFiGp42Sft3s9xKyOWuEOr7b2y1TUqm7Aef-Lsyjogl6KGnNXt48DJcRqfOc3Hg-whDuAIRK4xbhZO_5_uclaKYn1-ceWYTbrjy-BmHmTNZeidAkE-9VqlRn8VUF_cNrIw-V5HVN3kGd6f3auQFeJx5d_f7LX8G5Mkfj5VuegJIlPUTtttPfCYPTac-ubr8DYSUoqyK5UGl1a92Mvw7-9kaDFP9Ob3kmI8djEtV21cVAbXTsF9jsKfE2iPqOppykWOVVm7fDPFLBgH67Sy_yrDBvd2T5yHPcXcoVFvKi3w0qcpRlpbnquR9RZwQ_f9GUK6M_N9z8oIBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697477a71e.mp4?token=Vc3E3iduQwFiGp42Sft3s9xKyOWuEOr7b2y1TUqm7Aef-Lsyjogl6KGnNXt48DJcRqfOc3Hg-whDuAIRK4xbhZO_5_uclaKYn1-ceWYTbrjy-BmHmTNZeidAkE-9VqlRn8VUF_cNrIw-V5HVN3kGd6f3auQFeJx5d_f7LX8G5Mkfj5VuegJIlPUTtttPfCYPTac-ubr8DYSUoqyK5UGl1a92Mvw7-9kaDFP9Ob3kmI8djEtV21cVAbXTsF9jsKfE2iPqOppykWOVVm7fDPFLBgH67Sy_yrDBvd2T5yHPcXcoVFvKi3w0qcpRlpbnquR9RZwQ_f9GUK6M_N9z8oIBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشورماتوف یک گل را برای استقلال خرید  @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/459767" target="_blank">📅 20:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5c1b6a60.mp4?token=W69n1IUuZ_fgP21QywAAKDPfExV5VFzKwAbuGPwpjAZ9Jsb3npyhaETnGZBIKP4kLhTrzVIhwYHghwdbdAB8JAExVnCiq0GHaf5c8lbIcvU2xqFIyuRdXCEu1zGewcYXhbw3G92sAbeSHbVbWgyfYvXGMARRlCThdZsqbCqFgSO_eFPGmDy8iEZCuPZAQwenhHsyOajZtBY84xBGXKrtJ0hwd-drE1ENFp2D0uVVeQQylIPcSOd5Ls4JKnTI71hox070GCcBsQ--kOjFx4mfsaFvxmqUbWrX4Fw24uPqX8v25CwODDuD66KZFnThS88MMrHGVCTBXuvKKry10lKgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5c1b6a60.mp4?token=W69n1IUuZ_fgP21QywAAKDPfExV5VFzKwAbuGPwpjAZ9Jsb3npyhaETnGZBIKP4kLhTrzVIhwYHghwdbdAB8JAExVnCiq0GHaf5c8lbIcvU2xqFIyuRdXCEu1zGewcYXhbw3G92sAbeSHbVbWgyfYvXGMARRlCThdZsqbCqFgSO_eFPGmDy8iEZCuPZAQwenhHsyOajZtBY84xBGXKrtJ0hwd-drE1ENFp2D0uVVeQQylIPcSOd5Ls4JKnTI71hox070GCcBsQ--kOjFx4mfsaFvxmqUbWrX4Fw24uPqX8v25CwODDuD66KZFnThS88MMrHGVCTBXuvKKry10lKgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جدی‌ترین موقعیت بازی برای پرسپولیس توسط علیپور از دست رفت  @Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/459766" target="_blank">📅 20:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcYsOlPKCGC0HA5oz14gAuVrC5ZodKKV3nhwLxYuoXE0FCiRG8R85fs_LzHed-djSgqJrhqG9yFYuh5O_wO1VKCyIzQ4C_CaAkjpSbos9TrsxQANdRUqYoJ1_DpeZsZ_ljaT4PwF7U8Oh-mQW5BU2ex__JivXqGYFEs8vNRTRqqZYeDY-EOIftKtS1Smf8Rx4XhhbsYlHQ1u0Yk0JSEVRokIYLv_SLDICl_Jp9DYgt40qS_aR2HdpTpAg56nmlV8roQHc3SN3spz1jAdk8sT_DmraNe2PjMhFz4ukfDq9VqqAeNHExSaeppGTaMTCG84sjA6aeFsVygcDOnM9MlU3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: نقض کنوانسیون‌های ژنو دیگر یک اصطلاح حقوقی نیست؛ بلکه خونِ ریخته‌شده بر نیمکت‌های مدرسه میناب، خاکسترهای سالن ورزشی لامرد و حجله‌ خونین عروسی در سیریک است.
🔹
حقوق بشر غربی در این ۳ شهر دفن شد. آیا نهادهای بین‌المللی زنده اند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/459765" target="_blank">📅 19:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d0b140366.mp4?token=Z9fuedpa46H1EFn3-RTEhpT6xtiEDKonCjt-6Ex19z8oo1DEJb4eWK73EyJiVmJIAtD9SGBHZ9nrfCNr4nEYIezFvY_0wJQ7ueh8xo7H0zj9E8vn-Cw2IoFpYuZKGKeOcHrjdowHWxydZmRXDOZSOV9Y3i00BnJ2QLqvQo5CLPHWecIB9qpyYgqj0oZM9ck26u3zNl_N0WuqSwAxELJJQm0YnvEY4gN9AU6LmQOKFEZARDiJB1pYC2z_eG1TkiRE1innkrn88ELj_b6JZyAvldr7v2l5qiCqy8hpLEu3Ps4scFG-8ROv_LDRIp62aVb4H6gyIxfC_d3MFVpRYukISg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d0b140366.mp4?token=Z9fuedpa46H1EFn3-RTEhpT6xtiEDKonCjt-6Ex19z8oo1DEJb4eWK73EyJiVmJIAtD9SGBHZ9nrfCNr4nEYIezFvY_0wJQ7ueh8xo7H0zj9E8vn-Cw2IoFpYuZKGKeOcHrjdowHWxydZmRXDOZSOV9Y3i00BnJ2QLqvQo5CLPHWecIB9qpyYgqj0oZM9ck26u3zNl_N0WuqSwAxELJJQm0YnvEY4gN9AU6LmQOKFEZARDiJB1pYC2z_eG1TkiRE1innkrn88ELj_b6JZyAvldr7v2l5qiCqy8hpLEu3Ps4scFG-8ROv_LDRIp62aVb4H6gyIxfC_d3MFVpRYukISg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از دقیقه یک بطری انداختن شروع شد
🔹
طرفداران استقلال هنگام کرنر زدن بیفوما شروع به پرتاب بطری کردند. @Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/459764" target="_blank">📅 19:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ae668010.mp4?token=HaX-Rta1ebrjgdbC1XxtyM1t67iZr9xbt6SBgGnYkQEmBNj-m-0-Y6KBNdsuclfdIZ9ISl7TLhaxKYSDWMcGl87wXXFSKT0NcaeKiCRp0RvwybMjouIBWIXQ4ClBAm6MZS4MaAv-fokJm0-wAkYvkUmKYySAtqH3kHuCYwYJUKbnULKJ29R7pFurjV7QANyou1o1kfXNAblLq04G6SEQE_l0ZAVPIg2O-JufKlkuo-1IlL4mKIcvm6cEb74elqCKUGJCTmxkcdFkoj9tVjanTdXKwsNAEpltyLe5qWU5roGSiaYJSHSPX708eszihx56oNCCsAJCdx-C2gLdLP8OLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ae668010.mp4?token=HaX-Rta1ebrjgdbC1XxtyM1t67iZr9xbt6SBgGnYkQEmBNj-m-0-Y6KBNdsuclfdIZ9ISl7TLhaxKYSDWMcGl87wXXFSKT0NcaeKiCRp0RvwybMjouIBWIXQ4ClBAm6MZS4MaAv-fokJm0-wAkYvkUmKYySAtqH3kHuCYwYJUKbnULKJ29R7pFurjV7QANyou1o1kfXNAblLq04G6SEQE_l0ZAVPIg2O-JufKlkuo-1IlL4mKIcvm6cEb74elqCKUGJCTmxkcdFkoj9tVjanTdXKwsNAEpltyLe5qWU5roGSiaYJSHSPX708eszihx56oNCCsAJCdx-C2gLdLP8OLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
سرخابی‌ها در نصف جهان؛ شور تماشاگران پیش از آغاز شهرآورد  عکس: صادق نیک گستر @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/459763" target="_blank">📅 19:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp4rIH4PuIKhgMhqW_jt8NWWpiWuQ9BrX8lJQDRpHuJFuhro25nudT-HSP24J8qS_7O9ZkJbNMVautm6dxsCPGk5ZHfWphD96jGXBqAs-lMiCKLws-tOoRON6exdOSq7j1NeGN4AUkIV4O8ZB-vuqoQ_cPXXUOnrOZPQ85cbBG2RpFAGQ5k45lgNEeOQKdl-wxjr5h-Ttafxm4uy9xSPvSgBPdZGt9mI0hKHM44o1oUbp_5gaae6xTgqtlhRWbgoc_H8lA4h9UsmPVQowtxWt-s5sYyut9R4oCY9WXqSodN8L7LkZUkf2WvAJCCX99t-yQ1dfw8ojmnA3zwSa9sfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران‌خودرو قیمت خودروهای مشمول اسقاط را افزایش داد
🔹
هنوز ۳ ماه از افزایش قیمت محصولات ایران خودرو نگذشته که قیمت مصرف‌کننده محصولات این شرکت باز هم افزایش یافت.
🔹
خودروهایی که از تاریخ ۲۲ اردیبهشت ۱۴۰۵ به بعد پذیرش شده‌اند، گران می‌شوند و ایران‌خودرو می‌گوید بدون پرداخت مابه‌التفاوت، فاکتور و تخصیص پلاک برای مشتریان انجام نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459762" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0efbe4f9.mp4?token=N6_Ccm2EnB35rrCKgTc-fguKu2mggX-lbTegYoieIg7vPOlB4Ch41XqKFMaAzd1MGQ2S-1md0h-q4XiZNNCNp2r_G2kxZaii0ZkTNNKcRWsLUABy7Gy7HI7g_1vP9Ww4Vx9f9W7BHwUCsEQICVHt8NNMzRbA7Jq_IqbINTWMvnkE1Ep5nzjlfgxacSPiVPktXXOwbuaPJUsnsiWlabIvtg8Jk3yygomOtZk0P6kr-b1T8kljIRlWQRZmtDIc0C6-7q43DeZG8zX4d7qvw5YBJ8WcuEKXC7xUki-hIynfUSo16fqUdmy4buSY-pDih3Zi_eO-IkrpjFbr_nNqJubTew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0efbe4f9.mp4?token=N6_Ccm2EnB35rrCKgTc-fguKu2mggX-lbTegYoieIg7vPOlB4Ch41XqKFMaAzd1MGQ2S-1md0h-q4XiZNNCNp2r_G2kxZaii0ZkTNNKcRWsLUABy7Gy7HI7g_1vP9Ww4Vx9f9W7BHwUCsEQICVHt8NNMzRbA7Jq_IqbINTWMvnkE1Ep5nzjlfgxacSPiVPktXXOwbuaPJUsnsiWlabIvtg8Jk3yygomOtZk0P6kr-b1T8kljIRlWQRZmtDIc0C6-7q43DeZG8zX4d7qvw5YBJ8WcuEKXC7xUki-hIynfUSo16fqUdmy4buSY-pDih3Zi_eO-IkrpjFbr_nNqJubTew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ورزش: بیش از ۳۶۰ مکان ورزشی در جنگ مورد اصابت قرار گرفت
🔹
در تهران ۳ مجموعۀ ورزشی در اثر حمله دشمن صد درصد تخریب شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/459761" target="_blank">📅 19:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u50ErfqUxz9CFNDTAFZwjYXi3H7r1dc0pE02cJSOPGvNCkppweGUsIJVWCkG6_GG8oFpJBQ7r8Hr6J-QTrO-r0YE3kNkRPsXqJjULHJNS5jDv4YIqPB9hSXrlcdD1ZojVp_kWufXQpw2ajIEWsx0xexaXjXGP9aP4sFyc4xYv2ckCLO9KJh7Xs9kFJwmhEiDvPn9qUvZHrvw2FLP3uMx2vgpLGzwXZmnFcy58UZZ70zxErDsIYb00wfzTHoMLIsVi59sSlUek5N1SmLVogqU3shAhZGWbyw_kh2IH4jU7GzarWYVgJPBez0zAIT2zY2MenxCpn0ENlw_LSgbWN5YQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو آبراهام لینکلن در پاتایا پهلو می‌گیرد
🔹
ناو هواپیمابر یواس‌اس آبراهام لینکلن با ۵ هزار ملوان و تفنگدار دریایی که بیش از ۲۰۰ روز را در دریا سپری کرده‌اند، روز چهارشنبه در پاتایای تایلند پهلو می‌گیرد. مقامات محلی ضمن تشدید برخورد با روسپی‌گری، برای جلوگیری…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459760" target="_blank">📅 19:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459753">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXqRrHp3n2rY4j4GT2yUe9THFPzZxn1h_Xtnoy2dsmAQus9VaoXtNW26Tdwzwly0b7Ea08JsOzUchxsDWprRJ3v5-EC2eLEd44cS3aC0v8jLxrjSZzmPWXdoXtuJVi9Xei5v9zuDzO_U-nRMPmp3eSU4KTYYA4haHVkzu2cjMqweZuZn0gAnM5R4dUiTSLcpAg8QAMFIBomjcu6eDWFiBCe7oeF7HQcmN-8IzNLfP_SLPe38BbGifdzEwJ3gyKZd2DXj-vZX-XhuVro4_3jD0ce_bBM2fZkaWY5ulXE72mP0hkvXfoVmgRjIGOawyFGmDLxLVIA3u8I_TsFTfeavpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5ZR-kKbWk2L4J8wgkryVboeHFa9HshVHUu8wgfO7KMRDLbNaZxbKsp3u1m6bjfH_QqCZe8UUgCyHvdsBUWNiRYMdfazClqzEkuKqwflb4x0Lmaz-H-uJDeU1vO-K4PPF66PAvZynWC5-CyJQ8t38E-vPaqoL4v9jNZT8buYydJCcCbWhMMAPzQpI1lZryoRYvWiiRE7tJuGD-ie5usdiEGcF3w1tJGyZeeBqnx0hsgg_e6z9yrTW2s6hck7HDTrolDh3xxwoxs2CPaJjPFi0o9mdmeAb4i3pX1O3zMjvgHzydLpybhfagxr9qOJ-lbKu7i11rVBKp33s5PZPGQEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKsr-r-YHidbs8U1WlFuVjObNmtBoTkr4WLJ3C4tKMTTtBs6NnjkQkEx-sBewnKj8ye3RixiSvNvavCz5qpH5cau_ARwvAlf42O8yEfVtyhJFMuThFJOfVARrssuEtmJQCVT5bGTPUaLkMWVM3d2COl385siUk_k1VbNHupVQvbSH9QkAWzjZeSIlL_S4SdvdzZkHe6RgO9VjZolygcp4yoF1EKkqmXBUI9HrMI0zhS1Xt1Bi7MgBHrWWcVI4n2WEP4nH7LHNH2gruKHYJj3mClJscBvQrndVDMBtgnRVbpGuCckAoGPZVyoMZ9kaJG0zpJ6eeFZBgkPc_oyzSLUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSJaqSAm-nKS_KALhgYzwTIuQAmeQA4SKwaEJuwh2JGtvA0YXO4CKUW3NHLfq8kTp2QocLWkSPqT2fLIY-c1JcJSE_77hN6--NlOAEaWbAY-77RyNEs66UrcPbMWW7F9DSw8ZJTofDY4U1_O4isu8PECtrsQHcUIvlitRw-Uxx7Kl6fDrdLdhRCO15G62bgCCCwZQhdMRQ9inlCIGR2oaZXKWCiT9yVfYLJvZ7B95eB_aHx8PW5JtsFsk66OK6eXW9HiEcljvYM1H7v0LFCoZwomaNQEFJ46tlU0RBxg5Cof-T4PXzGA-qh0-DXjmsdlKx_Kv1Zoc7RtkoHpPPGiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyIDu5JxY0b7Y_qoUs_0a7o9K9mmh6_qtFspQlhGEB4OjF-K0yJE0kxmYwu5bSwsbB70QCqgVUrjHUMVHdkrLxU4HkFBsoI39gbhhSlMfDO9iWokHwLvOJDCrvChRKm4nZPu0kd2N55ExvQZ6KdlFUcgbm-JM9xeZHEhgcrcwdocht4FORrCRuQ-hGe8DMAv_lsStkwT2ScHcgvZ1hSVCZSjBBWZoYr6HKZNA3CwiuNGsm1uFZnq9hMWNrwhqffB0pguA7koq6HvWJb-ojy3hHWPB9Y6ohUJjBXYZlVlwSLHKLEb3QU092Qa4l3wKw2vC7OAVqi9q99rPHzpKht91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juPWxnDhjJaGgPgq0XP5dmKD8NQ1vY48-JcPJ_Yao6KavlcjcKPjORMY_-qkq9ezJb9xLltmYpH9NEGCQ5jrkxJYY43TdRXHPUTHqh_4JWB5W-hJR5zN5vDxi98NeATpz-NxPzG4GsvYHjhnt_15tC01HadkisfgYQFrQuyfO0vmoxWbqtbQZDdi_qf8QlZ0cy42bJhfPq0NV-t09Uvygoe30Fmq27EQvuAuT8KP9dtkAmk0L-OM9D_tuHAnX5Px-ApFKw6S6KJCp1kG7FiCammzH6T8NGkO9I5UHMoe7OzdCaE6nG2T2AQUsraX7MNvJOvX2xLGuQ2IO6PRjIPPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-NlE5jBrD9zT108rjg-wf1XR6JK3PtXI5wcYY7klOEtZCnlp9a5C90Ur3fP0NqVrspWkf9ANx3tnDi4iLMMmv9YS9i4fWl6CDU4dXGDGRqL6kxZstrGmPZCTbxhBpusIk5Ci-2RX3vCf-sm-m6YE65QK2QKk94mDBFwUB8yTEqOfROijN1cKyAFn-AuzYBVCBxFlcIDD0wmZ8qRM3X4MgrPbk2-0vzNCttNh2oRaiqdtWqrNtu4mafbac7FG75Eh5hYyeD2Jala7fRWo9ANUmO3DdHS--4pAupxN9UYdrPhEnUmnuUF_iW_ci3tZcnoxuwq4OnQQ5r0Ia-QvOeQew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سرخابی‌ها در نصف جهان؛ شور تماشاگران پیش از آغاز شهرآورد
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/459753" target="_blank">📅 19:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459752">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuMEieCYAlP4ZwiCj7LDcOZHiU1LkWqiViTEXX9zYh1vYzwISTWA__pPTzC6UDODtLDBb88Df1MTcHILwJQcUnH6ao7vw_V2IVZZgvB3UWVnkka-ECi94iBeX70SuveKdbixkUBLiv-08015df7Koqa157T9_IAeuOUfNSEa0HVYSmAop_guJSBR2vscQtGbrjyObqKp3e_04JFAO4dwEuPpx4-1XYh-kjF7f_jR9wNazwmcuVYRaqoJaxSX9lVvXzY7-9926xjaXHcdFZ6M6CukMGJDE0F4loDfsi9gwG5P_8IlSdnChKpFm4VPiQmtybteR6uBAjzvnYgubwzCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر حاتمی: به هر اقدام دشمن، چندبرابر و با قدرت واکنش نشان خواهیم داد
🔹
فرمانده کل ارتش: دشمن پس از شکست در برابر نیروهای مسلح، بار دیگر تلاش می‌کند با تحریک و تهییج مردم به اهداف خود دست پیدا کند، اما مردم بصیر و انقلابی ایران همانند سال‌های پس از انقلاب، پاسخ این توطئه‌ها را محکم و پشیمان کننده خواهند داد.
🔹
تثبیت پیروزی با قدرت انجام می‌شود و مأموریت ما در این برهه تاریخی، ارتقای آمادگی‌ها در کنار افزایش قدرت است تا پیروزی نهایی به دست آید.
🔹
جمهوری اسلامی ایران پس از این جنگ محکم‌تر و مستحکم‌تر پابرجاست و دنیا نیز پس از جنگ به قدرت واقعی ایران پی برده و با احترام بیشتر  با کشورمان برخورد می‌کند.
🔹
به هر اقدام دشمن، چندبرابر و با قدرت واکنش نشان خواهیم داد تا در محاسبات و معادلات آنان تثبیت شود که جمهوری اسلامی ایران در دفاع از خود و ملت ایران کاملاً مصمم است. این پیام بسیار روشن ما به جهان است.
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/459752" target="_blank">📅 18:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459751">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4Hv4MEWUZIuQOJQzaz-Q4mytyYTX6DVE9AN3gUuik-EuYYJ-iAMuP8gugmhHCjWwbVacjuNSdrS0ejhTI3Uy_xbP07VXY0EvG_TR9AIzcnPkRfvSkSMSEOs0x_V4PxvrvTukYwMxKRxt4n6o66Cxqj5RmVdVkv3O28nmU6BJWaYSYaM-KQzJ6SrHp2yKpwJjzZm4E13QyEVIEdXZrt_krRrd9y5V57n0qCfl7BO6ECW0ywaK7Ze6ag582U7je8F0ZSQubs5E8MnX4GoZZF07uhjQSTjHuau7Ux0fU23kz_q4s0W_NwDDLQE2MbtDgUx22MiElxFqNV0TqSh_J2mGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: در حال طراحی  نظامات متناسب برای صحنه نبردهای احتمالی آینده هستیم
🔹
سردار ابن‌الرضا: این جنگ هم توان دشمن و شیوه‌های عملیاتی او را برای ما روشن کرد و هم محک جدی برای سنجش توانمندی‌های کشور در برابر آخرین سطح فناوری دنیا بود؛ اما مهم‌تر از همه، اعتمادبه‌نفس و باور واقعی و عمیق به «ما می‌توانیم» بود که در این میدان شکل گرفت و تقویت شد.
🔹
یکی از آموزه‌های مهم این جنگ، ضرورت تولید در شرایط سخت، ارتقای مستمر فناوری و تأمین نیازهای میدان در شرایط جنگ بود. نکته مهم آن است که در این جنگ اجازه ندادیم با فرسایش فناورانه مواجه شویم و به این نتیجه رسیدیم که نوآوری باید مستمر و پیوسته و پویا باشد.
🔹
مطالعات و بررسی‌های ما از صحنه نبرد نشان می‌دهد دشمن با بالاترین سطح فناوری با جمهوری اسلامی ایران درگیر شد و این جنگ، از منظر فناورانه، دستاوردها و آموزه‌های مهمی برای کشور به همراه داشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/459751" target="_blank">📅 18:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459744">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpwvoVhoa7XiN1KxCGjW02SlKV8fFopaMff7MsNmsLJ3XNZ2eZZ2v91Woh2AUlb1qJFN8QsIzGf1P3JJCquswFn12Bt3D03PmMRplInLw0GHIrBS-FY1ITrz04Zkf8Ge2qTRY5MjDWTYZjS7f559RhEvRVQQRdBaVE8yGQaJMJEVRKsaUjQsFFB-G2MxT9-WmRsSfaSH219GyLYTHxWwMEeoI29D6z33wfTO_gkS0cs38Tyz9za6TdgNue0f_wpXj3dOfjADjvHj3xIyXsHXimAjEUDFlBYLD82R_t2oFCNfujO_SFOe-_NL19MJwW9mEubjGoHDa_C1CPVvo7m78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrYAyB3vtGPFjrMxATVhpvExcINoLMk6hH9d0EqJksKN1HWh64Tg6Q6ZDGL761ystwRhFut4GpNHY75i6CPJ7vQUOHZz6b5RhzfgTXNzWUDkiwzcW-5FfY-NPQSpOM8uGWbJs-Uxn6lGE1ION49ZClrUGkCKFaEz_67kU0I9VumW9j2maGt4KDZVMVA1w30Nxx9qtqwiRHjppkxaEtb4mEQG1le9bsbpi7_AcaUXSuWkMNIGngdknPscFot-jfZcEP5ftTuaIKUFhYdpgBvrYUA2kc01d0-SMa8xdiJtP5jMqZ6ahNuCpO3nKmMN3sY53U3NmcpmPnTqA1ZgFGVmAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9VQj8JFhoueggZfe-nZ-7UysnPv1w5wL8W1uxNoX7Yo3C55wHFP1AGb15vQsPgjh_-iZUrX94nH8skQXucPz6MRivGUvNy10YRRLus3iMMTgJZd5MVJ13ni8IZoO9YXTpHgwfWFICSm6cGsd8WuWTft0LfZK02wQT6eyy5uGJTvZawjxroR6ATn_vPQNEln7zS2_Px7vXXPFMdV3kzhZ-gWySSdNcGxlGzGOFMDF257fSQfmLRfldxLemxNubvOj0jgDb9MuIXGuCYVZrMAIRaTxpAqSULzphfCig3sg4dcrd6QGde4iuCp19ppXbCLA7AI1146n8FKvzfqfzUWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIVI5AXlEXzKLzugNaDOa3f6cBPBbAw7-las_Zz0j5FKNV1eUXXN4upMHpgQDLSLoUMxnuUTzu7litlt4YH_28ZlkJMhAzgCfl--VqVYc15riaNGF5JS6kS27gC3hdu4y_N40OZ-0HdxNybcgxkXIVnKIkvIxmays2OoXQgMLxCNeQP62LcuyNOJnY3R5jpw4fPrk5taWkVBJqH95wLwSIgsGVi2zmRi8ibwD2_JjKCNbnJChi7DNWrv4HT0oFjaenkPY822nyrrK-Tf3niFmfvG6-jDZFBBUOwQATpnr0bLdc-bZeWg72mNmovmpYrzFIn-HNg3cLPk5DXBGYp7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laYQigRpscAEHygJQzB1p8-ucKznaPtvbW9oUl7FG394dFHJN27iqr1U6ZTjaF8wv1F9cTTAspBg_4sxG0vvHcbhIqNvcrWgArXzxsnpr2wEHeSCqJxlGYBbnAi-wDYyXwuSNmqywtxJ1bbOPLR_6G5Bwy7APzvWDhJCd-nEiB3ZvoMaz9ojYBgrbopQjRt6WKBxkv6wo_GyB8_6bef96ukV6lyscJrSIP7v8xGf69h--hA0Xx80ynRE7oCn6WDHg4XBvHpBk0fFzhqSB7aDq9MDiUjKpHBQPV12aMeWvTjRlINX_n3lKIA0zOUk3CnotqyDbZ-3LsUtOV2vUKDnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghlTXMxWa1pl680OF8qnmVvbf6m3u8dU4sojuSyjq6GPlm8ltww_1dMzxvGVaW9v9JfaX0jLUF7VPzDxIhHr_hZhjc1yrv3qs2HCHKr-ZYgmQW04o5ptRkGQfVVwXImfoU2W7LsVRgtjdVghTEJJhpfJh1gdTjFJTVubg6JkASE1NvPsLBcQPQeAagBxn1HRuKbgRfDNZSZnCGLsmlB5yEDVoYygmVASIJ2vbpi8Ji6NerbqmUyw8LcOVaDdtP7c7f1dTwHMTtyk1PB0mHBMhaV-p2YCcSwNYOro9BFoQ-06hZTbjvo1tdax-goFR1qNOpfqKyzbxOe6FI_LsiQ3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnVhMrRM_abipxsBcf6lxmSgP4CR0Ce14mQTUbs6Q0mNhrt8LgCPEZtrjJ9KgmwlLTQgsgEFerfSjrYwWGn0bUnbCWh-T5GxtUDP5fEf0T4T-JMp8HnC1ayLULOTLjj_hrHMQmaG8DY609Y6AGJvz3WdH6RyJ3ZJAA3DIrLjA2rokbrbmpOVndwF-VIEjjq4Q_Lrn8uOw9YCbqYxytbVA8kGT8Oi470-LIzGuu5O5qWXEOr4WXp1ebMiSxSK2gEgruoW9lGjPmDdkl1fbiTO7xiwAQHk4JGt5urJLi5c33glk28H42MP4LjEwfwxf0BT7iUGHLKI3tI1HlprWAI36A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از جنایت آمریکا در سیریک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/459744" target="_blank">📅 18:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459743">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgfaH6KBxUs-3hQIaDVVB-AJyNEpLiiYuW77jZbH44D3zKngzpuZXKVKIjd8SQwMYwjufin8K6wxZid2bwHhv2rIQ49HwQQhJORQ9vqBqtYT7BJZumWSQxhk75ZtX6YR_hVOUXryP6DHLvlIVJlEvlrDzVCFOsl1N94xHZjyN3SLKueJOVlebgRkyoVeIsyIWxOequnT_lUY6TrzkBng6oQVY-XxFQjKPYdbZoE2NmPC6NtOfpSNZXrP_tLZhlQaDy3UM8z4IZL_KBUnrURcbXFNdPn5PiZnq-9V63m61A5HbAAR3-FMySDvxhhWuXyzL0Ok1RWvn4IHGDkgjQI8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آراز و محمد به دربی نرسیدند
🔹
دوربین موبایلش را تنظیم می‌کند، آهنگ پرسپولیس را می‌گذارد، می‌رود عقب‌ تا کامل در کادر بیفتد و کودکانه می‌رقصد.
🔹
وقتی بچه بودم از یک هفته قبل از دربی قلبم تندتند می‌زد و روزهای تقویم را برای رسیدن به روز موعود خط می‌زدم. حتماً آن‌ها هم این‌طور بودند. محمد و آراز با توپ پلاستیکی دو لایه‌شان، هر شبی می‌خوابیدند، آرزو می‌کردند روزی پیراهن تیم محبوبشان را تن کنند؛ پا به چمن سبز آزادی بگذارند، تور دروازه را بلرزانند و صدای هیاهوی صدهزار نفر را بشنوند که نامشان را فریاد می‌زنند.
🔹
اما این اولین دربی پس از جنگ است. سوت داور که به صدا درمی‌آید، استادیوم غرق در هیاهو می‌شود، اما در اتاق محمد و آراز، پیراهن‌های تا شده‌ روز مسابقه در سکوتی سنگین خاک می‌خورند. این اولین دربی است که دو هوادار تیفوسی سرخابی‌ها روی فرش جلوی تلویزیون ننشسته‌اند تا برای هم کری بخوانند و از هیجان روی هوا بپرند.
🔹
موشک «نقطه‌زن» عموها همه این آرزوها را پرپر کرد. ۹ اسفند، آمریکا نه یک‌بار که دو بار موشک‌هایش مدرسه‌شان را هدف گرفت تا سهم آن‌ها از چمن سبز آزادی، تنها خواب ابدی در خاک سرد باشد.
🔹
امروز سوگوار رؤیاهای ناتمام شماییم. ما از یادتان نمی‌کاهیم. امروز، هر شوت، هر کرنر و هر گلی که زده می‌شود، ما به‌جای شما دست می‌زنیم و بازی را با چشمان شما تماشا می‌کنیم. محمد لقمانی و آراز احمدی‌زاده روی سکوها یا پشت تلویزیون غایب هستید، اما امروز در قلب تمام هواداران نشسته‌اید. برای همیشه.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/459743" target="_blank">📅 18:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459742">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI4uX0p3UTw0aj-TVxycxkE0P_YfqgSRNTekDdEr9vKUNl2TWCOoOp-Ye9Crd3n8_MFzqG1SmI1E7PU5fx41LnTtVDzlU34LnacQxVWV7eScYjlnDnq7chtgfnkEQNvU45jCLVG0tDthmgS8NaJiqYXem-W2FtKWjRCbL3PyOHKBWeYbGyT5ZT9WpQTlIazkfBKF9maBhbLvz0-PajRn7Lou3bivpYTjnrNuSrpg3MxcoQpdsjWbhzg4vTwyrEk9RZGQYL-Tx7vJxF1uVZtM_EM25fnO7OUZbacoEEdPbCdtOuv7z7lYbQx6g_DtzWJWYT2mz0mQdi41GkD3CPrXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توران در انتظار تکمیل دیوار نجات یوزهای ایران
🔹
وقوع تصادفات
در
جاده ترانزیتی تهران ـ مشهد که از حاشیه پارک ملی توران عبور می‌کند، طی یک دهه گذشته جان ۱۳ یوزپلنگ ایرانی را گرفته است؛ آماری که با توجه به شناسایی تنها ۲۷ یوز در کشور، بار دیگر خطر جاده‌ها برای آخرین جمعیت‌های یوز آسیایی جهان را برجسته می‌کند.
🔹
با این حال، مسئولان محیط‌زیست می‌گویند تلفات جاده‌ای یوزپلنگ در محدوده عباس‌آباد ـ میامی، پس از اجرای اقدامات حفاظتی و افزایش پایش‌ها، به صفر رسیده است؛ دستاوردی که هنوز با تکمیل نشدن پروژه ایمن‌سازی جاده، شکننده به نظر می‌رسد‌.
🔹
مدیرکل حفاظت محیط‌زیست استان سمنان گفت: تاکنون ۱۰ کیلومتر از این محور توسط این سازمان فنس‌کشی شده است؛ برای تکمیل بخش باقی‌مانده نیز وزارت راه و شهرسازی تعهداتی دارد که باید عملیاتی شود.
🔸
بر اساس داده‌های موجود، جمعیت شناسایی‌شده یوزپلنگ ایرانی شامل هفت یوز نر، ۶ یوز ماده، ۹ یوز با جنسیت نامعلوم و پنج توله متعلق به «هلیا» است. در چنین شرایطی، هر تلفات جدید می‌تواند تأثیر قابل توجهی بر آینده این گونه در معرض خطر انقراض داشته باشد.
🔗
چالش‌ها و راهکارهای حفاظت از یوزهای ایران را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/459742" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459741">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609ac19eca.mp4?token=HknesCiOIqwtsB6t7QV28ms7QnEUkCZpE7qYn551B_Idc2gPhLMUcrX2oFT3SBujxZURy7VpwjySuNuDjlon7FVFXY09lOK8n8MaztaHBJ_j0VXuVZWtLbqesuPGgiE8jIj4RL_ruxiBKH97x0wA9J17NchKgtp1Pal_fuj7oQGb6xTroZdiZYeGAHVZElGbwAkyIRriUJWnsoWnLEQ6ulKIegotiXDoqehhY1zA75QBp9p_UBH4Et7tsYxM18Sz4BEoGyd9O8EWGdsgze0BEogOeqBrfzMzxFvZ8cE3tsiyDFR9kQzjg4YWe9PHhVs4Lvxh6AoEx015sh-Q0p9vOBFns8l8ziSMHdMDucUKusiFrplbNuv3m9rue8iGMEvDhIJg2HlCYKzEwONzGcp2KR2vBFFfqQjDPtPD3Y2pNBwrSoePn2T0Mg_kPTHE-vmTVt9z-8CvnRnrnHC-jFIHxfqENeFmKQIMLwqbK0puzoytWgnPIz6e8gQ8cluCiJ7TA9daQe_0fjbVbpXc6HNxZ8ygpOIbaB6GRcuzJy_mD7wYhbebLtCwkpjdLToIMytDXDKaLDBD1s8qqyGDKME9WXeYP8y5dCPkhbZhj67PPR5XjA5oSPE4qgzDG_yPb8EHlgRfU5Le4Eb1_U21T7jmS4iFxFBD3iz-afr-Dc3a6I4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609ac19eca.mp4?token=HknesCiOIqwtsB6t7QV28ms7QnEUkCZpE7qYn551B_Idc2gPhLMUcrX2oFT3SBujxZURy7VpwjySuNuDjlon7FVFXY09lOK8n8MaztaHBJ_j0VXuVZWtLbqesuPGgiE8jIj4RL_ruxiBKH97x0wA9J17NchKgtp1Pal_fuj7oQGb6xTroZdiZYeGAHVZElGbwAkyIRriUJWnsoWnLEQ6ulKIegotiXDoqehhY1zA75QBp9p_UBH4Et7tsYxM18Sz4BEoGyd9O8EWGdsgze0BEogOeqBrfzMzxFvZ8cE3tsiyDFR9kQzjg4YWe9PHhVs4Lvxh6AoEx015sh-Q0p9vOBFns8l8ziSMHdMDucUKusiFrplbNuv3m9rue8iGMEvDhIJg2HlCYKzEwONzGcp2KR2vBFFfqQjDPtPD3Y2pNBwrSoePn2T0Mg_kPTHE-vmTVt9z-8CvnRnrnHC-jFIHxfqENeFmKQIMLwqbK0puzoytWgnPIz6e8gQ8cluCiJ7TA9daQe_0fjbVbpXc6HNxZ8ygpOIbaB6GRcuzJy_mD7wYhbebLtCwkpjdLToIMytDXDKaLDBD1s8qqyGDKME9WXeYP8y5dCPkhbZhj67PPR5XjA5oSPE4qgzDG_yPb8EHlgRfU5Le4Eb1_U21T7jmS4iFxFBD3iz-afr-Dc3a6I4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شناورها هنوز برای عبور از تنگۀ هرمز منتظر اجازۀ ایران هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/459741" target="_blank">📅 18:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459738">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c00afafed.mp4?token=X-Oy81lbockYBJ4wuKLXt8lhwClhlfQslYvefjThZgmYpedxYX7xb4izMYpMq_mdAqcNN404ydvYy-SRubjUsSL7WTrldgCl4e_CcuYtFHIiK4gP7EcC71lT6sBoxmZkX2Ajwzw1L7rN5TTZm3BtBwYEN8FCqA9utWgQAWn1uN-X_w_oW6GXXrTjKfHD1xd4X91o58qBhUFMO0yVfW_1V6PuZASFx8a9cdBDasuVzypOScfyVcGxgRubUTzJDSbi5-gii7s6FXN-NZlA_6UJskXmnSLpnZIKB83cUBUKt4ziKLYs9_I7WPyHV4AR0yL3ThtA6X5-v57OE_fBNswKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c00afafed.mp4?token=X-Oy81lbockYBJ4wuKLXt8lhwClhlfQslYvefjThZgmYpedxYX7xb4izMYpMq_mdAqcNN404ydvYy-SRubjUsSL7WTrldgCl4e_CcuYtFHIiK4gP7EcC71lT6sBoxmZkX2Ajwzw1L7rN5TTZm3BtBwYEN8FCqA9utWgQAWn1uN-X_w_oW6GXXrTjKfHD1xd4X91o58qBhUFMO0yVfW_1V6PuZASFx8a9cdBDasuVzypOScfyVcGxgRubUTzJDSbi5-gii7s6FXN-NZlA_6UJskXmnSLpnZIKB83cUBUKt4ziKLYs9_I7WPyHV4AR0yL3ThtA6X5-v57OE_fBNswKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ادامۀ حملات پهپادی ارتش به پایگاه‌های آمریکا در بحرین و امارات
🔹
روابط عمومی ارتش: در سی‌امین مرحله از عملیات صاعقه و در پاسخ به هدف قرار دادن مردم بی‌گناه، از بامداد امروز، ده‌ها فروند  پهپاد انهدامی ارتش، سامانه‌های راداری و محل‌ استقرار نیروهای آمریکا…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/459738" target="_blank">📅 18:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459734">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac67baab97.mp4?token=lvpJHdxIZZ4_ZqfpitPnopCSe5PN0FsELhGk_K8l74FLAt5bpgbUaEJw8a06MSQ9y4fNJmshatgCoiVxU2lgZExVkOy-9Ul7C2lJUSGC7se5kmCGUTMrV_IFBocDlI2Y4CtH7DfpNXGJ-3VmjDpnVKTtDorRxKP-RfXbNFRsXvat_Qe1irMI6R_gHRM8_i4Cy8wbYCsLIuxnyVrUjHA1sUVCvyVNhHiUg4BtXR5xlHhrpncZfzOfayt9vs5f4zbXDgCLTVPKIO-mND9OvG_yYdrc1zgiWy4xr9hw7Tc0pBvjRqSikENu3ADFrEJzqn8YG6Vo4F5Un3BLz0NEe7nX0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac67baab97.mp4?token=lvpJHdxIZZ4_ZqfpitPnopCSe5PN0FsELhGk_K8l74FLAt5bpgbUaEJw8a06MSQ9y4fNJmshatgCoiVxU2lgZExVkOy-9Ul7C2lJUSGC7se5kmCGUTMrV_IFBocDlI2Y4CtH7DfpNXGJ-3VmjDpnVKTtDorRxKP-RfXbNFRsXvat_Qe1irMI6R_gHRM8_i4Cy8wbYCsLIuxnyVrUjHA1sUVCvyVNhHiUg4BtXR5xlHhrpncZfzOfayt9vs5f4zbXDgCLTVPKIO-mND9OvG_yYdrc1zgiWy4xr9hw7Tc0pBvjRqSikENu3ADFrEJzqn8YG6Vo4F5Un3BLz0NEe7nX0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
حملۀ موشکی و پهپادی سپاه به پایگاه‌های آمریکایی در اربیل عراق
🔹
روابط‌عمومی سپاه: رزمندگان شجاع نیروی زمینی سپاه با حملۀ تلفیقی موشکی و پهپادی به پایگاه‌های آمریکایی در اربیل یک مرکز تعمیراتی و انبارهای تجهیزات فنی ارتش تروریست آمریکا را نابود کرده و…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/459734" target="_blank">📅 18:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnLsxed08t69hABREwkzGijfRgCanBxLFuHD580UAukItok3UCo0ai9_STKJwOrV_CfSy6alUC4xdRSKdPDJSu6tm5H7268iq_W7FbohmDft7duY4qcZZsDesU9bUYtNC1_WZgJsUcs_y0R_BW74ZtYMekpBv4PZAiD5tFYtT72sa7EYQhgqjAE7O45rU14gWOdJUC3guk8XgMxOn1CPBkhxGJBropjaSnxmhVxqdYQ8MSUOqcJqPJ0FHTQ-WJhTHId_2WxM_faZ7sX9-PPl8Qxof-hB97IWTHZCjaNOIzEYo_E7B1jSYpi5MuDsaG-h3cBDlYqtLhT_5gohMxp5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف وزیر ترامپ: چین همچنان خریدار نفت ایران است
🔹
وزیروزیر خزانه‌داری آمریکا امروز گفت که چینی‌ها همچنان خریدار نفت ایران هستند.
🔹
پیش‌تر وزارت نفت ایران گزارش داده که در ۴ ماهه اول سال فروش نفت ایران ۱.۵ برابر شده و تزریق ارز نفتی همچنان ادامه دارد. طبق آمار تانکر ترکرز چین اولین خریدار نفت ایران است.
🔹
براساس آمار سازمان برنامه، تا ابتدای مرداد، تحقق ۸۰ درصد از بودجه نفتی ۱۴۰۵ تضمین شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/459732" target="_blank">📅 18:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHxutoCtd4LZQW99gNJEMjL6KxR2jDG0kO0BTfOQNgErV0zkzXSmmWrzy3MtOaPBht_zqBKu82c8ylfmlhcTRRTjJjzZmnZsMKWpY_nSK659q-9PjIb2wIyy_4KUkZ8X3Jer8DRvG41g_ofFfTcjYsH3ZxdqS71HF2o9aVX0701s-4p2GIfRrxKCwdx4ytfe70fWcZZTQ04xYlfMI_vdtdTForxAw_TaDZr3HqLD_KOH6A1S0A-2IUFRQbdpBKTLv5sr04QYSYnORzwS0IFjV8yOTJJonyMSSsxA0aZcFfUjtTr9EXgc03UGSiu8hm2nnOmheo2-N89JecpIfjJDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفیر تاجیکستان در تهران: جنگ مانع تجارت ۶۰۰ میلیون دلاری با ایران نمی‌شود
🔹
نظام الدین زاهدی، سفیر تاجیکستان در تهران: حجم تجارت ایران و تاجیکستان در سال ۲۰۲۵ به ۴۸۵ میلیون دلار رسیده که نسبت به رقم ۵۷ میلیون دلاری سال ۲۰۲۰، رشد چشمگیری را نشان می‌دهد.
🔹
همکاری‌های مالی ایران و تاجیکستان بر پایه‌های محکمی استوار است. ما با تکیه بر زیرساخت‌های موجود و ارادهٔ قوی تاجران دو کشور، باور داریم که تجارت فیمابین نه‌تنها متوقف نمی‌شود، بلکه امسال از مرز ۵۰۰ میلیون دلار عبور کرده و به ۶۰۰ میلیون دلار خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/459731" target="_blank">📅 17:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459730">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_AFdA333fROOmt7tjC3XJ_2wMWGYajjXln4rxvDfJlfxxATA2wGTaDkJnCVw1obBsR0AgWfKd1EOkKdBBipPtdEaRrTX1mUjhefCHR5bfND3j2C6q5YBbzWSKXHrxZKXUquMfr4WnZ9Ae-qjBtdyAKj7_wiJn65o5gmn3J_Rp3SI3LjuIajxQEEbMC8WK_y1Cf8VrUEFygGLhZuPENnW3WwlyaiZgdzWaV3vgbkoHVs6dJcUUm-WyI83RZQSQMiAlQtPtZwD6fwMaFShVLTKvSO5IK_SCd4mKCqh98Iep-PUzPN3wXODi-pAbmzwxmch-E7IH8ZLI-msah440Qz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکهٔ ترامپ بالاخره وارد بازار شد
🔹
فروش سکهٔ یک‌دلاری دونالد ترامپ امروز چهارشنبه شروع خواهد شد؛ عرضهٔ سکهٔ ترامپ در حالی انجام شده که استفاده از تصویر رئیس‌جمهوران زنده روی پول آمریکا سابقه بسیار محدودی دارد.
🔹
در سال ۱۹۲۶ نیز تصویر رئیس‌جمهور وقت آمریکا کالوین کولیج در قالب یک سکه یادبود نیم‌دلاری استفاده شده بود.
🔹
این سکه از ترکیب مس، روی، منگنز و نیکل ساخته شده و ارزش اسمی آن یک دلار است. ضرابخانه فیلادلفیا مسئول ضرب این سکه بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459730" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459729">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLWCd-w5VgLr_C_3zG_8QqkQfOasQQ64-FgmOC-1NnYAfGpulFzpJes2od2gCOe7_01-NTYYGDHph7QPZBfEjsLUEePWxtvMKgEq7lgbrjM9r5yN8X-KGaDIwdu3l-GgTnWGih8LvUX-2hLyeLj5P5c4cdBHrFg_OR0SKREM8jUguPDc1qFc0u2bxWAOslDBWK51ewsrjkV4SkK0wvjWO0Pj_4mhf0VbW-BmF3x43vxMvJ3u-p_15VXMV2W2akbiUQlOWrDXDcJOkoKXV0SoWJqCP_kvwpkFQa8u2oz9bNu4kez7hMWNcylOTXs8mOtz9Dqjrs03joUIhn30HfTXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس دانشگاه آزاد: حمایت از دولت نباید مانع نقد کارشناسی شود
🔹
انسجام ملی، هم در خنثی‌سازی محاسبات دشمن و هم در استمرار کارکردهای حیاتی کشور نقشی تعیین‌کننده دارد.
🔹
در منظومه‌ای که رهبر انقلاب ترسیم کرده‌اند، اتحاد به دفاع متقابل و سپس همکاری در عرصه‌های علم، امنیت، ثروت و پیشرفت منتهی می‌شود.
🔹
هر اقدامی که به شکاف اجتماعی، فرسایش اعتماد عمومی و تضعیف همکاری میان ارکان کشور بینجامد، در نقطهٔ مقابل این ضرورت تاریخی قرار خواهد گرفت.
🔹
نباید به بهانهٔ حمایت، دولت را از ارائهٔ نقدها و تحلیل‌های علمی و کارشناسی محروم کرد؛ دستگاه‌های اجرایی برای موفقیت، بیش‌از هر زمان دیگری به نقد علمی، ارزیابی سیاست‌ها و مشورت نخبگان نیاز دارند.
🔹
البته نباید فراموش کرد که عبور از شرایط کنونی، بدون برخورداری از دولت مقتدر ممکن نیست و از این بابت باید همهٔ تلاش را برای کمک به‌کار بست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/459729" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459728">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIM5WETIxDKfJetoCknhgwgCsaawmC3pHdw9_4d8KJgNijXbQnwqmsylZ4K-UlEhdOPG_jUd_p3QSNzCndrSVsjnquR_hDqcsgkiTPmNIymC1YIofKoudDcPWjwn_FD4iaWlRiA4Kf1tAirvwIah40hUFJrk273SVr4Iiec51VXvx-VoPtpbwNXJoYcCfndbtU_V_ax3cWouaXeQDJ5Sa4cQH_A-Zn2XLfodCdsKiHqnom3-FnY8RJAbmsbQcM7tdZgbPJKS_4_ZS2-fspKLjJjs4OacikERwjZR0qX86FliWzKz0H54QU2_yRNUlJgLT9UggiHCG26zqHuVG64JXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورژانس هرمزگان: ۱۹ مجروح حملهٔ آمریکا به مراسم عروسی سیریک کودکان زیر ۱۰ سال‌ هستند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459728" target="_blank">📅 17:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459727">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e60f2bae.mp4?token=aful99wpzg_Z7GFmExhfRCrCKVwp1Nmkqh768s3DxFaZ2etf7G8DANQ3flTNWqhgOSn5XyoZ3kgQw3Ik6N8iSJhZ1U8EcUJQBXg6BHQ1DlxRYTPbSnmIkmD92_0VIhu2HxPR2KTuLWs9JxB_d6bQax0XY5O_kYG4_9s16GYRSf3a2uFqMg4bDwqLA6lQy_SvKU30WpNRH3mfPqR-Ro2iKavZnfL9ZM9bkrNA7SNlrOLn2KovZl49lVx2X1OdBELcW_894ylpBOqSw4A6dWqjAPDiN03aeVy7jL8o10re-APYtz-5UEErdZySJnUdu57W-tLKaCKhm4HqDCt2qYABUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e60f2bae.mp4?token=aful99wpzg_Z7GFmExhfRCrCKVwp1Nmkqh768s3DxFaZ2etf7G8DANQ3flTNWqhgOSn5XyoZ3kgQw3Ik6N8iSJhZ1U8EcUJQBXg6BHQ1DlxRYTPbSnmIkmD92_0VIhu2HxPR2KTuLWs9JxB_d6bQax0XY5O_kYG4_9s16GYRSf3a2uFqMg4bDwqLA6lQy_SvKU30WpNRH3mfPqR-Ro2iKavZnfL9ZM9bkrNA7SNlrOLn2KovZl49lVx2X1OdBELcW_894ylpBOqSw4A6dWqjAPDiN03aeVy7jL8o10re-APYtz-5UEErdZySJnUdu57W-tLKaCKhm4HqDCt2qYABUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انیمیشن وایرال شده در شبکه‌های اجتماعی از واکنش سرباز آمریکایی به صدای پهپاد شاهد
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/459727" target="_blank">📅 17:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDXyXEkEXojmMPGCy6rYgqHdFS-oQ5YGk_FBZ49otbSrcOtc5R6BxQQLoyWeZjiRMsCQQw9iGDQINwQGxAc2ydA522_x-i5GiWvQR7_3IoyFFggname50nVuhOI28PVfZi467G9d-lyCgH6IvsV9xNAX3TcOkcpG0KkijgpJX3MFNW6Aa1rBKuhSoyCkvVtY5xBRkZ9ApkSw3bfRHw_qov_rvwudkA4eKW55FtxsFS-htMYF4fbvaZpS2Q_WUlvHnKIiZWO8MKiCsH65QZmKVY-6K9N6Z_UW9YSxKkNWMPpN8xndvvrIux2u2jDnlLbmhMyBmf6Hw4qnmM4jrxkBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا دلار ۲۲۰ هزار تومان شد؟
🔹
دلار در بازار آزاد امروز درحالی از ۲۲۰ هزار تومان فراتر رفت که صبح امروز ۲۱۴ هزار تومان قیمت خورده بود.
🔹
بررسی اطلاعات مرکز مبادله نشان می‌دهد، تقاضای واردکنندگان به‌عنوان اصلی‌ترین تقاضای دلار در ایران کاهش یافته و آن‌ها حاضر به خرید ارز با نرخ بالاتر از ۲۰۰ هزار تومان نیستند.
🔹
مسیر افزایش دلار از ۱۸۵ هزارتومان تا رقم امروز از زمان مصاحبهٔ همتی کلید خورد؛ جایی‌که رئیس‌‌بانک مرکزی گفت «درآمد ما از فروش نفت صفر شده است».
🔹
همچنین برخی مقامات غیراقتصادی دولت از جمله معاون اجرایی رئیس‌جمهور هم دیروز با دادن پالس منفی به افکار عمومی گفته بود «دولت به‌دلیل ناترازی بودجه ناچار به چاپ پول است».
🔹
وزارت نفت اما می‌گوید وصول ارز نفتی در ۴ ماههٔ امسال ۱.۵ برابر مدت مشابه سال قبل بوده و به ۷.۵ میلیارد دلار رسیده. در مردادماه هم طبق روند تعیین‌شده ذخایر ارزی بانک‌مرکزی ۱ میلیارد دلار افزایش یافته است.
🔹
انتظارات تورمی به‌دلیل اظهارات منفی معاون اجرایی رئیس‌جمهور و افزایش تنش میان ایران و آمریکا براساس ادعای کارشناسان هم‌اکنون از عوامل رشد نرخ دلار است.
🔹
قدسی، کارشناس اقتصادی، معتقد است انتظارات اگر از سمت رشد نقدینگی پوشش داده نشود، روند افزایش نرخ ارز به سرعت کاهش پیدا خواهد کرد.
🔹
اما کارشناس اقتصادی علی رضایی می‌گوید که مسئله افزایش نرخ دلار نیست، بلکه بانک مرکزی و سران اقتصادی کشور با تشریح اخبار مثبت نباید اجازه اثرگذاری عملیات روانی و شکل‌گیری انتظارات را بدهند.
🔹
هم‌اکنون اطمینان‌دهی به بازار ارز از سوی بانک مرکزی، پشتیبانی از تقاضای واردات و مقابله به هنگام رسانه‌ای با عملیات روانی آمریکا می‌تواند مسیر انتظارات منفی را از بازار جدا کرده و زمین شکل‌گیری آرامش در بازار را مهیا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/459726" target="_blank">📅 17:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmNmnQ3XcNgkJdN_NWmteR3yJkvIikZXfRcb9xsGXyZ-7aZ_q1TlDnzjIp5SxZchMjiA-cpfDCZb2PzX0PlAGN-ymlzEcita635Wc6Lv7r8BUE5Nb-te5GXDo6mg2ub03fPlYLLaKB5PyjFhF5WSeI1acZwBi3aCUxmczGmGse9MaDCq8zADCxY3cF4Yf-kvb9N9x8SE9Ycv36C5izGPZNKP_mfLHMXagSXJ1BNGfjQD2hcOIIaPWfAnKQGDt7e0dZqoQThpLKqK9iWIGAVxL1LIWXLFL-eOnV33GVwPcScTlG5SvPMlRfsO0KbT5n9t6ydV_KiRxbjPTXSIf9tmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جانشین فرمانده سپاه: دشمن باوجود تجهیزات ۱۰ برابری‌اش در برابر تمدن انقلاب اسلامی شکست خورد
🔹
سردار ایزدی: سران نظامی آمریکا که خود را بزرگ‌ترین قدرت نظامی جهان می‌دانند، امروز صراحتاً در برابر راهبردها و صلابت جمهوری اسلامی ابراز استیصال می‌کنند و بافته‌های چندین دهه‌ای آنان برهم خورده است.
🔹
حوزۀ مأموریتی سپاه بسیار گسترده است و این شجرۀ طیبه در عرصه‌های نوین دفاعی قله‌های افتخار را فتح کرده است.
🔹
امروز در زمینه تولید پهپادهای فوق‌پیشرفته و مدرن و توانمندی‌های موشکی، بیش از نیاز دفاعی و چند برابر اهدافی که به دشمن شلیک کردیم تولید داریم و سامانه‌های پدافند نوین کشور هم در اوج اقتدار و پیشرفت به پیش می‌روند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459725" target="_blank">📅 16:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwSlkwZj1sBQKmLYFd8KJPt8fEoLNSFPK-URbdxXBc_ijVfRnuXbt8YF2iYkcawR3IABbEPXp7OCXbAmVoXudFPOXeFm8-gV9c1h8aRkDv5aMX-XhS1ff4JmN19aV04R9gAZ_IAfxqVCSYXiA-tauIPqKyBsXznxNjUlDc6dEPoWZObO9J6kIQNqP6Hb7oaigL5IkVp9FKOoVXyLkYHjJ7gSRavEnMSNnoIyWZQbYZd28K8minLv3DABb_S0A4vbe-f8Lk4btNIPgeH00en_NtD4HPAcpR149C-5AszxEs26VJHNVoke25GvmXC_s6yCQeiCFTfiyPDx4UcLjyyieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: ایران و جبهه مقاومت در یک مسیر جوهری علیه استکبار قرار دارند
🔹
رئیس مجلس در دیدار با مسئول ارتباطات حماس: اساس و‌ جوهره این مبارزات در جنگ حق علیه باطل و در مواجهه با استکبار بود و روح مقاومت طی ۵۰ سال گذشته هر بار با شکل جدیدی در آن متبلور شده است.
🔹
ما مذاکره را نفی نمی کنیم اما مذاکره یک ابزار برای مبارزه است و اگر روزی دست از مبارزه با آمریکا و رژیم صهیونیستی با اشکال مختلف آن برداریم، آن روز، روز شکست است.
🔹
ما در جریان ماده یک تفاهمنامه به پایان جنگ آنها علیه ایران و متحدان ایران در جبهه مقاومت تأکید کردیم؛ در حالی که طرف مقابل در ابتدا در متن ۱۵ ماده ای خود، خواستار توقف کامل فعالیت‌های موشکی، هسته‌ای و مقاومت شده بود.
🔹
مسیر ما باید در یک مسیر جوهری قرار گیرد و باید جبهه مقاومت را برای ادامه جنگ حق علیه حفظ کنیم. امروز حتی دولت‌های دلداده آمریکا در منطقه هم اعتراف می‌کنند این کشور باعث ایجاد ناامنی در منطقه است.
🔹
قالیباف با اشاره به عدم اجرای مفاد تفاهمنامه اسلام آباد از سوی آمریکایی ها بیان کرد: آمریکایی‌ها باید به تعهدات خود عمل کنند تا ما اقدام به بازگشایی تنگه هرمز کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/459724" target="_blank">📅 16:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459723">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a5a3e74f.mp4?token=c6g_aGC7MmkKZmT1MuyShdofAh4f5CTIzdjJaF8_EnCG3_qZ7-LbNoO2LnE7Vb49GxYa6YMs55mdgk-_2kwZlzs-A08kDzS6IzTAl9C5PNfjhRuYZz0gs51YtfYmrJRaeix-PEk_wmVcSndzYMqF0x724LCXTTlDLIBdaMSeaA459M7yU1_1ZRAtLadS9qe2glETMsyw83Lz2H8G7MZGlaXKzR-4k76Pw8ct5iT11oKzlaVDEj1HWX5JrW0k1S9ALZP-6PuPee6P2X2XxMrsk99hY2r5swZaZRlbzOKOXTSmY0zJh98yFdCaCdfuooAxkRjLebCmNIkKysE2w_Q1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a5a3e74f.mp4?token=c6g_aGC7MmkKZmT1MuyShdofAh4f5CTIzdjJaF8_EnCG3_qZ7-LbNoO2LnE7Vb49GxYa6YMs55mdgk-_2kwZlzs-A08kDzS6IzTAl9C5PNfjhRuYZz0gs51YtfYmrJRaeix-PEk_wmVcSndzYMqF0x724LCXTTlDLIBdaMSeaA459M7yU1_1ZRAtLadS9qe2glETMsyw83Lz2H8G7MZGlaXKzR-4k76Pw8ct5iT11oKzlaVDEj1HWX5JrW0k1S9ALZP-6PuPee6P2X2XxMrsk99hY2r5swZaZRlbzOKOXTSmY0zJh98yFdCaCdfuooAxkRjLebCmNIkKysE2w_Q1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک: رژیم صهیونیستی حملات خود به جنوب لبنان و منطقه علی‌الطاهر را با شدت بالا ادامه می‌دهد
🔹
از بمب‌های ممنوعه فسفری تا انفجارهای مهندسی‌شده در روستاهای جنوب رودخانه لیتانی.
🔹
هدف دشمن، اشغال منطقه علی‌الطاهر و ایجاد منطقه‌ای ایزوله با از بین بردن امکان زندگی در این مناطق است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/459723" target="_blank">📅 16:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459722">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9bdxC1AASSIilC3QAjox3l4Fsd1pRmz8uHAOkz2ptKG1_gaXzWaFpjlCd1UOX8_sZOoC1_QALE_AEO0qi9mrI4iRqSxCBjOEVNCbSH7ZHkl1cH-fyhBp54x-GFO5srpIoKmhAj1YOOn36CyiZE7o4xEngXQS2qwHZYsdyloLLZ6zTlZzZ9RdFPWiYa6p9JKXPBtFCAk0XkfIVdXblXXIVLgZlaPFOL6-BPtTlY1qNxdbxYYaF1dUkXY6kiVDEP1Bu_tWmwSv2Q-0D7Apv28OEz9OqfD9Fg4uYdX2GFTXkroToVANKZJiYnfhcC34fbLInonCJob2ulvwVfu78lIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بیانیۀ وزارت خارجه دربارۀ تجاوز نظامی دیشب آمریکا به ایران و پاسخ دفاعی ایران
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459722" target="_blank">📅 16:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eaacd2377.mp4?token=BFR0tCl9ieS4NZJ-rHY1-6lJFzU4OkE8d6wVv1jSUszj5XuSKwRvx9ZFarOhV9_qZpNQhMECLtJ8hTkepuOppW9jkHy251qYXDB7lZbGiNY2yV_Q-FLggxsoittY2M4M-luhjzaLnU6SFNUnaYdXCynbZSUDnjdCcpIgC78jIliHV-ffxkWxuWc1ovMEu4_Wg6w_Xe7DNm7nYHPdsi6tOmbogBf61GiuP5VPjsXXXUlSAqXy1WXTKHeo2FBb2yCtHG8Xopyfvn5cADmEVk0msCAvubSZGAFq9EO653LYJqar7gnYQPYKbv6h0miW5pX0tuVKdpsar6YC9xnwGPJp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eaacd2377.mp4?token=BFR0tCl9ieS4NZJ-rHY1-6lJFzU4OkE8d6wVv1jSUszj5XuSKwRvx9ZFarOhV9_qZpNQhMECLtJ8hTkepuOppW9jkHy251qYXDB7lZbGiNY2yV_Q-FLggxsoittY2M4M-luhjzaLnU6SFNUnaYdXCynbZSUDnjdCcpIgC78jIliHV-ffxkWxuWc1ovMEu4_Wg6w_Xe7DNm7nYHPdsi6tOmbogBf61GiuP5VPjsXXXUlSAqXy1WXTKHeo2FBb2yCtHG8Xopyfvn5cADmEVk0msCAvubSZGAFq9EO653LYJqar7gnYQPYKbv6h0miW5pX0tuVKdpsar6YC9xnwGPJp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ ٣۴ میلیون دلاری تهرانی‌ها
⚽️
شهرآورد ١۰۷ تهران میان استقلال و پرسپولیس امروز طبق ارزش‌گذاری سایت ترانسفر مارکت با ارزش ۳۴ میلیون دلار گران‌ترین بازی این هفته لیگ برتر ایران شناخته شد.
⚽️
پرسپولیس در رده‌بندی ماه گذشته گران‌ترین تیم‌های لیگ ایران در صدر…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459721" target="_blank">📅 16:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
معاون وزیر نفت: ۴۰ درصد ظرفیت آسیب‌دیدۀ پارس‌جنوبی به مدار تولید بازگشت
🔹
آواربرداری پارس‌جنوبی به‌طور کامل انجام شده و فرآیند بازسازی به‌صورت منظم و برنامه‌ریزی‌شده درحال دنبال‌شدن است.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/459719" target="_blank">📅 16:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c35f746cd.mp4?token=NqSqAsqAOysTpUR2dZynQqx4SkMo-OUpl5vRKvdj_FlFFmPZjzLQ-tsuHXq9DehC3XzQofc5fOo_Pb047QiprXhi32bBSaKAhoVcwZjxJp_gvmVFYho_Ur1haWKkdKRbNWOPBe8BsNJI2ntJ7NfCvVBCKPrmXNkFXV9otS488cANxWPvZNkdLCinDmEyPMtVx1zPc61Eyc4iTsBCqP30AjQI4bmafrwcEoXAnldKY4ktbXaPWLqoJNznT2cSRVAd2HWfn4AlxJ9fnftiaxWFjx-uLlc8-C0yxwLaJh2DlW45WTHKfhp4Nsnps2kQxAH19uWnWlMTeSx9zyL7UC0gUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c35f746cd.mp4?token=NqSqAsqAOysTpUR2dZynQqx4SkMo-OUpl5vRKvdj_FlFFmPZjzLQ-tsuHXq9DehC3XzQofc5fOo_Pb047QiprXhi32bBSaKAhoVcwZjxJp_gvmVFYho_Ur1haWKkdKRbNWOPBe8BsNJI2ntJ7NfCvVBCKPrmXNkFXV9otS488cANxWPvZNkdLCinDmEyPMtVx1zPc61Eyc4iTsBCqP30AjQI4bmafrwcEoXAnldKY4ktbXaPWLqoJNznT2cSRVAd2HWfn4AlxJ9fnftiaxWFjx-uLlc8-C0yxwLaJh2DlW45WTHKfhp4Nsnps2kQxAH19uWnWlMTeSx9zyL7UC0gUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین: با تروریست‌ها مذاکره نمی‌کنیم
🔹
رئیس‌جمهور روسیه در واکنش به تهدید همتای اوکراینی به ناامن کردن حریم هوایی روسیه، این اظهارات را «تروریسم دولتی» خواند و به کی‌یف هشدار داد.
🔹
پوتین با بیان این که مقامات کی‌یف همزمان ادعای آمادگی برای مذاکره می‌کنند، گفت که «مذاکره با تروریست‌ها» در کار نیست.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/459718" target="_blank">📅 15:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459717">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/459717" target="_blank">📅 15:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459716">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1iMd170K91LB-whp00iWHVe7NfBS3ErJzWJcOCuGkUP-gHjOSYUS_DzM7fEfJyc02HPN54_fCgAuujPFd7M4IYuP3YwGWtj1z5_YBAmskR8yxzR3EhtbMCA2n5MTyKEm9d1AJ8LY4xN2ToIyWwJtUK_s8PR_264U9X8_-RJAh6KFn4UEo0zZC7FjsPfl1NdvE_sVbDjRS9YPHyZYrlPuz-aYo8k2zZasexAIPRtMPjRyRYXVm4f0A5MKRxbhR0vHiP6MaJImaMTc9vWTgskF76YMuUKtzO-_sMz7itulNiWIoQ23kwSh-w_LGCol9awrsX7U_Sks7dG7IE7fE1how.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی‌دلیگانی: پایگاه‌های آمریکا در اروپا هدف قرار گیرند
🔹
نایب‌رئیس کمیسیون اصل ۹۰ مجلس: در بررسی‌های دقیق و برآوردهای اطلاعاتی، احتمال هرگونه اقدام خصمانه از سوی پایگاه‌های آمریکایی در اروپا مدنظر قرار گیرد و در صورت احراز این احتمال، آن پایگاه‌ها در چارچوب پاسخ متناسب، هدف قرار گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/459716" target="_blank">📅 15:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459715">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2rRvVIJ5shsY76b1RaMpQ4W2pfKidmdalyMP0HLOPubaJkxGfVRegnTOA5E5AiAaXzzO4q34I-rWOxgOBNDewGlxEPTRv4fphA47_hA6Ax4KFGGDexNikKLjIw2YBJwEwxTXUiRR313SbexhuUxsrCB9SDZw-ys0rW1fnNW_HOkqSWwpKipKQmB9BrezbQBtFfUbwTE7KS_IEtVphrD-rENxd92nM-fE0bgEkecAVgOXIfapej9jgcGQAjog-OCIQ4d47hFZjk8zDuzaycqFW85x32-m_Nv-p12EWh_UwIcfiUHcsWYehuOVFrWgTQNVs5wbo80I9FHQ3oP5FPMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس این عدد را گنده‌تر بگوید، برنده است!
🔹
وقتی آمار قربانیان یک حادثه از ۴۰ هزار به ۱۰۰ هزار و حالا به ۳۷۸ هزار نفر(!) می‌رسد، دیگر با یک اختلاف آماری ساده طرف نیستیم.
🔹
عددهایی که هر روز بزرگ‌تر می‌شود، بدون آنکه سند و فهرستی برایشان ارائه شود؛ روایتی که ظاهراً قرار است با تکرار، جای واقعیت را بگیرد.
🔗
ادامهٔ خبر را
اینجا
بخوانید
@farsnart</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/459715" target="_blank">📅 14:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459714">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH7sFy6FyZAyM26jq3gB9DJu1MxPpw4EfmfoLpVfbLYHssSK5qQrZwp_r_MmkAkOZlTNC0HLUa2nQSH86_Y8E0hR0AtzwdDc4HG1WwQmSuZGjwPljPHQklKJyCC0BHjllJgB-3BOEp_pGQOpYUveWY8cMWOy_AStGc6Y5mzGSxmUCPungb1FG6an3_bZUGxFS_k-NJYyd86-oM7vzXG9zrbo4nXrmvHhTzL-98v3wX9pbdGLmgvyIT_RNMmWdYE_8fNmXq0ix-HLOlxvC-NNoUHL8g5oqoDplP6iHfYaD29U0Cj14c_gEOgVoj04dYoJ18F_OHmQbPn6K4f00QCVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: تمام اقدامات آمریکا به تقلید از شیطان و خود آمریکا شیطان بزرگ است
🔹
رئیس‌مجلس در واکنش به حملات شب گذشتۀ آمریکایی‌ها علیه مراکز غیرنظامی به خصوص شهادت جمعی از هموطنان‌مان در یک مراسم عروسی در جزیرۀ سیریک، با یادآوری جنایت این کشور در میناب و لامرد،…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/459714" target="_blank">📅 14:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459713">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd66906547.mp4?token=JYCQpV1RwUJ3coM_DHSU28Z3WcpHyuYIuj3LPjH7rQBTJM90PFSg4flGLQMW1WSjIQh_mh9kCexSPz3BPvuclDhT9pzpT75LV43SMZMrWUdLSeUZm40hLEzA3TPGDxLIDWneXixqY0V11HVnw8YMqKyEsBpxEGV8LMVldDvEKsS1aqmMXSa_J-x8LTT5HWpFkzpjX-uQClXtUk97EyQc_8iyMsk9SWR_cpalH6UuLLVtZpSaOrL0uOtQxLLaLIVA8goAoULpWgLWeY6nCVZfX5tffnuxn9c5MMytaZMjqJIP4NJQXWdA-hn5ETD630cCoSHX_5bJRc2WubJRjUE6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd66906547.mp4?token=JYCQpV1RwUJ3coM_DHSU28Z3WcpHyuYIuj3LPjH7rQBTJM90PFSg4flGLQMW1WSjIQh_mh9kCexSPz3BPvuclDhT9pzpT75LV43SMZMrWUdLSeUZm40hLEzA3TPGDxLIDWneXixqY0V11HVnw8YMqKyEsBpxEGV8LMVldDvEKsS1aqmMXSa_J-x8LTT5HWpFkzpjX-uQClXtUk97EyQc_8iyMsk9SWR_cpalH6UuLLVtZpSaOrL0uOtQxLLaLIVA8goAoULpWgLWeY6nCVZfX5tffnuxn9c5MMytaZMjqJIP4NJQXWdA-hn5ETD630cCoSHX_5bJRc2WubJRjUE6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت نفت با موشک‌های ایران بالا می‌رود
🔹
بازارهای سهام آسیا در معاملات امروز حدود ۲ درصد افت کردند و معاملات آتی شاخص اس‌اندپی آمریکا نیز کاهش یافت.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459713" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459712">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0cc9769f7.mp4?token=Tj_Iw7k5YhHu-POZBfuWPfTbUEDCfyf4mtjxwxcsWL7BRqbic3WA1SucJXHYknAF63PCYACC5yzLX4Hzng-OFOk5_iCQuG0l5TkPzV9hpPM4q1hM_iZOzzlbg8Xg-x12L3CR-XF5wLKJqZ-wy5Swupys3MDErstUYrvFMcjl-vm3ItJDb1cPNaNKrQAprKx5vel3i1Co5gWeklozPjE0wvbV-l2FI57eza6JXNEiMY6JpAIscedslompWqRh04bFX1smQARDTUv9d7suj6Po39_Ry8T4Tq05Kv7U5hj2d0Ui69eq1Gcm_E_9gSv2buh6Qj2iXd2L0G3SmB8tElmbPH8bf4oKgjzwL1rLTw6dL8Ab47xea6jBY23pNP2NZ0OXYlXGdDHqr7RVOMr-leza-AQZpkpVcfxANRFkGeIHOZ_rAlA6pkwT_q6_97TUhbRzQw3km4K0t-7Jw64OgFQUQZweQmn_B4UmFCBjPqPVibCsGR-tXZl2vLl-vTeHsWnK_f4XzJD1PxWlDmaf09fFWA_fRaClBBwskRF_jEOzdZFDFXXGVjN3jrpqabIXIhdaQ-IkZDTd9Z6s1EDkmc7WNp_7eFbuyZt2npdmKYoc1O8gKPQMwej4k9Ad4Em8vYZJZZvXt7WfwWu0a384paDOE4g3xtWi3oDfanOlVY_9rbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0cc9769f7.mp4?token=Tj_Iw7k5YhHu-POZBfuWPfTbUEDCfyf4mtjxwxcsWL7BRqbic3WA1SucJXHYknAF63PCYACC5yzLX4Hzng-OFOk5_iCQuG0l5TkPzV9hpPM4q1hM_iZOzzlbg8Xg-x12L3CR-XF5wLKJqZ-wy5Swupys3MDErstUYrvFMcjl-vm3ItJDb1cPNaNKrQAprKx5vel3i1Co5gWeklozPjE0wvbV-l2FI57eza6JXNEiMY6JpAIscedslompWqRh04bFX1smQARDTUv9d7suj6Po39_Ry8T4Tq05Kv7U5hj2d0Ui69eq1Gcm_E_9gSv2buh6Qj2iXd2L0G3SmB8tElmbPH8bf4oKgjzwL1rLTw6dL8Ab47xea6jBY23pNP2NZ0OXYlXGdDHqr7RVOMr-leza-AQZpkpVcfxANRFkGeIHOZ_rAlA6pkwT_q6_97TUhbRzQw3km4K0t-7Jw64OgFQUQZweQmn_B4UmFCBjPqPVibCsGR-tXZl2vLl-vTeHsWnK_f4XzJD1PxWlDmaf09fFWA_fRaClBBwskRF_jEOzdZFDFXXGVjN3jrpqabIXIhdaQ-IkZDTd9Z6s1EDkmc7WNp_7eFbuyZt2npdmKYoc1O8gKPQMwej4k9Ad4Em8vYZJZZvXt7WfwWu0a384paDOE4g3xtWi3oDfanOlVY_9rbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیاتی از حملات کوبندهٔ ایران در پاسخ به جنایات دشمن آمریکایی  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/459712" target="_blank">📅 14:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459711">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6962b2e4.mp4?token=bADQ9rGak9VWtUt3QKd1EP7WpmD0sL176wNocZjjI7KkUdw12mwXMLyAXhezYObIyjApg5mPhLLzs9WuVnh4E5kxopyi5SnwZyMIdDGNzkEtgamMz5XisBcQFwplPagmwL_6bCnP0d0mfJ6RBZtTCoqhShJzCA0R424UvRr_GtWZiBJY3M7ybTZfpXZxurZXucxp7lz5jnPJrP3JuLLKuGjJY1GRpEASmrAs0HEyl2t6kGIP1HLXBVWTohYEwaLufwtcfR40jUxQ0W2p0E17dsojMtTxMBl0eThiiHXUFATohUxme4xrEy70JwOdSpycmVzrNDMzv32MtRu9_5j_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6962b2e4.mp4?token=bADQ9rGak9VWtUt3QKd1EP7WpmD0sL176wNocZjjI7KkUdw12mwXMLyAXhezYObIyjApg5mPhLLzs9WuVnh4E5kxopyi5SnwZyMIdDGNzkEtgamMz5XisBcQFwplPagmwL_6bCnP0d0mfJ6RBZtTCoqhShJzCA0R424UvRr_GtWZiBJY3M7ybTZfpXZxurZXucxp7lz5jnPJrP3JuLLKuGjJY1GRpEASmrAs0HEyl2t6kGIP1HLXBVWTohYEwaLufwtcfR40jUxQ0W2p0E17dsojMtTxMBl0eThiiHXUFATohUxme4xrEy70JwOdSpycmVzrNDMzv32MtRu9_5j_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاپ گستردهٔ حملات قاطع ایران به مواضع آمریکا در رسانه‌های دنیا
🔹
بسیاری از رسانه‌ها این حملات را واکنشی از موضع قدرت به جنایت اخیر آمریکا دانستند و از برهم‌خوردن محاسبات واشنگتن در جنگ خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/459711" target="_blank">📅 14:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459710">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd22734b47.mp4?token=aqGToMOjDhfAyBCpnzc2OyvQeqICclS_0W4hGOoNuioCCPr8SqtbgT6ICm_RuIgqcAHvjPuMBFMefOVKO3Ty5YkVMebHx_BUdNCQTqMQHKfEveZ6Xe1zaDL7tpFKWwdnDGDsLpeG96-Rt_nfWGRszfsRoUXkESojqXTYKLw5dRRHbQisFgaCvjxWUeVQxCeZjAuMlf6iRcQ8jbMGAIBJHc5r52AeqjRHxY1ijG5Y3AsUrrhu1wl0XP_FZgDDQSkblR5h-DOnWy9Z9WAUR9BC0pg8QPagV1M5aMV2vUZXGjlL-nPQv7BQrHjlNrxzXk6vZzMbuj-qhPF8-UUN6Hb5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd22734b47.mp4?token=aqGToMOjDhfAyBCpnzc2OyvQeqICclS_0W4hGOoNuioCCPr8SqtbgT6ICm_RuIgqcAHvjPuMBFMefOVKO3Ty5YkVMebHx_BUdNCQTqMQHKfEveZ6Xe1zaDL7tpFKWwdnDGDsLpeG96-Rt_nfWGRszfsRoUXkESojqXTYKLw5dRRHbQisFgaCvjxWUeVQxCeZjAuMlf6iRcQ8jbMGAIBJHc5r52AeqjRHxY1ijG5Y3AsUrrhu1wl0XP_FZgDDQSkblR5h-DOnWy9Z9WAUR9BC0pg8QPagV1M5aMV2vUZXGjlL-nPQv7BQrHjlNrxzXk6vZzMbuj-qhPF8-UUN6Hb5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگۀ هرمز همچنان بسته است و کشتی‌های متخلف هدف قرار می‌گیرند
🔹
گزارش خبرنگار شبکه سه از جزیره لارک؛ جزیره‌ای که هدف حمله نیروهای متجاوز آمریکایی قرار گرفت و در پی آن تعدادی از نیروهای نیروی دریایی سپاه پاسداران شهید و زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/459710" target="_blank">📅 14:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459709">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5834dd82d3.mp4?token=tBZ2zJZxsNmZJ0zy7GRxYbxqleBVhUDHuZkml4a1_-6egq8gKDV65ZJE1rlBb_LQw9O772kRwi-fF1gCuDVDa1hBJssWh6QHv6YqdyZ-UdLhNJp2hBnX4MnPzWpVjsMbGj2Ue3vx4zLQIjoLSctC9EUoI4NMpSj9WUm0hRbt6B8ruqlFLHYMXWKyw2pgBaSoBwOs37LSxZWdf_UZMCCd42rZqgCNu7KT8vdRgFknUQzpsYoZA2t122wCe0TUFyjTTe3ntW_KrTUL82x_dE5FpIi3un3o-V3jhWPwYU-MaOMd6UjmOs6RGshQfz7Fd9TE5X7HACEvUjBIuVPWJgm_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5834dd82d3.mp4?token=tBZ2zJZxsNmZJ0zy7GRxYbxqleBVhUDHuZkml4a1_-6egq8gKDV65ZJE1rlBb_LQw9O772kRwi-fF1gCuDVDa1hBJssWh6QHv6YqdyZ-UdLhNJp2hBnX4MnPzWpVjsMbGj2Ue3vx4zLQIjoLSctC9EUoI4NMpSj9WUm0hRbt6B8ruqlFLHYMXWKyw2pgBaSoBwOs37LSxZWdf_UZMCCd42rZqgCNu7KT8vdRgFknUQzpsYoZA2t122wCe0TUFyjTTe3ntW_KrTUL82x_dE5FpIi3un3o-V3jhWPwYU-MaOMd6UjmOs6RGshQfz7Fd9TE5X7HACEvUjBIuVPWJgm_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: ۲ نفتکش متخلف با رفتن روی مین منفجر شدند
🔹
روابط عمومی سپاه پاسداران: مردم قهرمان و مقاوم ایران اسلامی؛ ایستادگی شما در میدان الهام‌بخش ملت‌ها شده و جهان شاهد روند بیداری مردم و تنگ شدن عرصه بر مستکبران جنایتکار است.
🔹
شب گذشته ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/459709" target="_blank">📅 14:12 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
