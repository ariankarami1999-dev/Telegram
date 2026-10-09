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
<img src="https://cdn4.telesco.pe/file/YUoH69Vdj4udi-rPH0tDbJPYDXXM1ahcTRg09dYIwqgYE6tlC8hn1NgyoVjLB4ge8R928UTdVlBiaUNbpgXfdLPg5ThxgTPGXjFMpXamt3AfRdU5VGlVt9gV3qpA5tkKtOHErmVbbOIubJqZq0s5KU9xYRIF0sB7uNJif6q5J-RDJL4SAANK-V7y_gy94Uqi_n2JyeyHnsQrtDpFIdaOUY9x5HeSMHBd_iUt82yOYfVHNnrQnYVDvbYHh3tvOqUG6h_FWBXEfxaOE-iGQ_l3hQv2YzZnjdF6dP5mwse5a3tz-0LNJD7QPdyiupz9UxDBPqPSCvrSce7TPVgr-uSIig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-696965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e3251bb3.mp4?token=iaOs81O4mfsfbiYfXzVUOE0-gnzQg31ODHQFy4t6k_bPtuLHVx5F4yH-7TLH6ULPseyd8fLwY5_BKHyLOu55REJV-9akL9oKBH11IlO7OfBp6Bojd6CH2Mz8F-eluBSzpYSi-nhujhdGI6T2u-YfFY6DhRGOz7s1dGH12D2at42dK7mI3sDVtpOtvajFBuR-TxstP-_KTh8ZJ0R7-KsqYewiUTqArtAIcLkHqz8fVBPy6_T1sX85gnlQgsW-IF1huF3PSF3dELZp364udQcyZwJo8XhlkSNZSF8LbUbBVcDIegVcOsritsMNDqEzzYyzbFVUwk4ilGAv_Z0GLns3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e3251bb3.mp4?token=iaOs81O4mfsfbiYfXzVUOE0-gnzQg31ODHQFy4t6k_bPtuLHVx5F4yH-7TLH6ULPseyd8fLwY5_BKHyLOu55REJV-9akL9oKBH11IlO7OfBp6Bojd6CH2Mz8F-eluBSzpYSi-nhujhdGI6T2u-YfFY6DhRGOz7s1dGH12D2at42dK7mI3sDVtpOtvajFBuR-TxstP-_KTh8ZJ0R7-KsqYewiUTqArtAIcLkHqz8fVBPy6_T1sX85gnlQgsW-IF1huF3PSF3dELZp364udQcyZwJo8XhlkSNZSF8LbUbBVcDIegVcOsritsMNDqEzzYyzbFVUwk4ilGAv_Z0GLns3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم پرسپولیس به صنعت نفت؛ اورونوف در دقیقه ۸۵
🔹
پرسپولیس ۳ - ۱ صنعت نفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/696965" target="_blank">📅 18:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30ab30119.mp4?token=A-XzLxT2TAWL2AvH-OamqfITcEQ5n8k8cm5Mcu1Q9Qvww8Icu9b3BRl8TVLGCrVrpB-WZlWB-snGVta_71QqIhT-9_oSEYEHwvll6bzLkR-lqKjtakrgA4ckkpc_MpwOU6ePvnHNF4DYaPRg6ThPagSr_VqSFgZqePFpOHqFpK5QIEA4xtRvGG6fS5ScapPie-IX5qnsfZU7xMYEMwCBTI2fxC059TB4E1gKNc0iiKkBUe_OxJO3527PP0R1jYNP153Mfwj6_MaiKMgp7-5b-zDXOB2YbODGOrpZMdHwR-7B8c4T309GQSIbOc2PLqCsc6B8ruo4sl_FiHUym7dYJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30ab30119.mp4?token=A-XzLxT2TAWL2AvH-OamqfITcEQ5n8k8cm5Mcu1Q9Qvww8Icu9b3BRl8TVLGCrVrpB-WZlWB-snGVta_71QqIhT-9_oSEYEHwvll6bzLkR-lqKjtakrgA4ckkpc_MpwOU6ePvnHNF4DYaPRg6ThPagSr_VqSFgZqePFpOHqFpK5QIEA4xtRvGG6fS5ScapPie-IX5qnsfZU7xMYEMwCBTI2fxC059TB4E1gKNc0iiKkBUe_OxJO3527PP0R1jYNP153Mfwj6_MaiKMgp7-5b-zDXOB2YbODGOrpZMdHwR-7B8c4T309GQSIbOc2PLqCsc6B8ruo4sl_FiHUym7dYJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلطان شناسایی شد
مدیرکل محیط‌زیست استان تهران:
🔹
یک پلنگ نر در منطقه رودافشان دماوند، با نصب دوربین تله‌ای شناسایی شد و نام «سلطان» برای آن انتخاب شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/696964" target="_blank">📅 18:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: من چوب آزادی‌ای را خوردم که به ناشران دادم/ ممیزی کتاب نباید دست ناشران باشد، چون دنبال منافع خودشان هستند
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
در زمانی که وزیر فرهنگ و ارشاد بودم به ناشران گفتیم ممیزی انتشارات با خود شما باشد و خلاف قانون اساسی عمل نکنید وگرنه با شما برخورد می‌کنیم.
🔹
چند ماه گذشت و این ناشران برای پول درآوردن خیانت کردند.
🔹
کتاب افتضاحی را منتشر کردند که نمایندگان مجلس به من گفتند این کتاب چیست که برای چاپ آن مجوز داده‌اید.
🔹
کتاب را که خواندم تا نیمه های آن که رسیدم حالت تهوع گرفتم.
🔹
به مجلس گفتم حق با شماست و در فاصله کمیسیون و صحن علنی، معاونت و مدیرکلش را برکنار کردم؛ به آنها گفتم هیچگونه اشرافی ندارید به کثافت‌هایی که منتشر می‌شود.
🔹
به نمایندگان گفتم قبل از پاسخ به سوال شما از درگاه خدا استغفار میکنم.
🔹
ما به ممیزی متمرکز برگشتیم و الان هم معتقدم ممیزی صورت بگیرد و نباید آزادی در اختیار ناشر باشد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/akhbarefori/696963" target="_blank">📅 18:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a955c8f2af.mp4?token=CXohBkLgsW-wFVghxOwDsB7uPw_dtncshzQVu5Zn7uD_X62RYY7L8vR9HqmdS6448hQxPmf8ZiEq0VUdp6GtqgNCZA08ofhlEUap-cu-mx0NVKNU6V4yUSOdKN4wnzBtUqRY8CsoibnIbjz8XEj_sd4qJ14SHkO3RZOZeg0J1XUR9YSphc_180Kk3Jrrdme21YX7uPG2lV5I57ypLd5Ep4UFYr85xwraHr2nUe4vKZNbwHAYKk0BLHg5LvGuM7fmL9vmsawf9jBQ1PI8j18kCw8Z9npJ84qubQ1w8sqknaspg6Yn88kYuUoFm69LlYYJoBWDDc0Q5VNzWO-VhTOooQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a955c8f2af.mp4?token=CXohBkLgsW-wFVghxOwDsB7uPw_dtncshzQVu5Zn7uD_X62RYY7L8vR9HqmdS6448hQxPmf8ZiEq0VUdp6GtqgNCZA08ofhlEUap-cu-mx0NVKNU6V4yUSOdKN4wnzBtUqRY8CsoibnIbjz8XEj_sd4qJ14SHkO3RZOZeg0J1XUR9YSphc_180Kk3Jrrdme21YX7uPG2lV5I57ypLd5Ep4UFYr85xwraHr2nUe4vKZNbwHAYKk0BLHg5LvGuM7fmL9vmsawf9jBQ1PI8j18kCw8Z9npJ84qubQ1w8sqknaspg6Yn88kYuUoFm69LlYYJoBWDDc0Q5VNzWO-VhTOooQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی زیبا از حرکت مه بر روی ارتفاعات کوهستان سهند
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/696962" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=rdCpKQ36ikHdvqTbm-tts4cE8ojOcDUaSA1q1f0T8aRHCWNt-ynxSnU5FJaeSKIo_3kX_HCUXObfF_EPxOcGDwTNyZijdxDMzAap3xzPxndzNVLh8RrYyJumSFe7S9r9qB6GAhaXmT_UL9q1E0uIsUCESPHhdjhjegmJhhGPFo7c1WIUfOi2zGei99zkyepDl2YVdwXlgRIaAvuE3iQQ9_bscjODBv6uL8I3wz6dwZy-mUH5fn42GE2RHmR-qE1TK9tk8xegc1eZWpELXy1PVHFX9BjpGRzKSOQ0CCvtcWln_-HkEKhIuvYk5TVqptp7_8PIN4lvZWTf50caqhUDlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4da4e50a3.mp4?token=rdCpKQ36ikHdvqTbm-tts4cE8ojOcDUaSA1q1f0T8aRHCWNt-ynxSnU5FJaeSKIo_3kX_HCUXObfF_EPxOcGDwTNyZijdxDMzAap3xzPxndzNVLh8RrYyJumSFe7S9r9qB6GAhaXmT_UL9q1E0uIsUCESPHhdjhjegmJhhGPFo7c1WIUfOi2zGei99zkyepDl2YVdwXlgRIaAvuE3iQQ9_bscjODBv6uL8I3wz6dwZy-mUH5fn42GE2RHmR-qE1TK9tk8xegc1eZWpELXy1PVHFX9BjpGRzKSOQ0CCvtcWln_-HkEKhIuvYk5TVqptp7_8PIN4lvZWTf50caqhUDlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول صنعت نفت به پرسپولیس؛ دروازه سرخ‌ها با گل باصری باز شد
🔹
پرسپولیس ۲ - ۱ صنعت نفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/696961" target="_blank">📅 18:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696960">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a787cce95.mp4?token=tm6WvC8sGXMMvkcgqoDyd8ROKtDfyGBPpEkGSaNSd_kAdKTzUIL8NerVeaJa-04MTzuCs8gIFLcvQXDlOO_bKJYWlmeeTQRe7FJjxF7CoJBkCiMIBTGLgacbB5WABPLdzO5p_sXOnFkaOti7Hqdy28NvceEg8B_YSSCrgjdl3UEGUtawO-ypqSYji4IJ5aCadnr-_WYAApv7o7wovZpO5A6DIRwkf2CmY3XOVmR8FL4-EIW9yRXBLHyZU34tjrBhAJiYaQRTNaRu8R5GRNVw11qquIkQOrC-I7YLXyyuD1ByHDFW15AS7lmGMflykYAxa8LlRatNG866zsE2sfZhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a787cce95.mp4?token=tm6WvC8sGXMMvkcgqoDyd8ROKtDfyGBPpEkGSaNSd_kAdKTzUIL8NerVeaJa-04MTzuCs8gIFLcvQXDlOO_bKJYWlmeeTQRe7FJjxF7CoJBkCiMIBTGLgacbB5WABPLdzO5p_sXOnFkaOti7Hqdy28NvceEg8B_YSSCrgjdl3UEGUtawO-ypqSYji4IJ5aCadnr-_WYAApv7o7wovZpO5A6DIRwkf2CmY3XOVmR8FL4-EIW9yRXBLHyZU34tjrBhAJiYaQRTNaRu8R5GRNVw11qquIkQOrC-I7YLXyyuD1ByHDFW15AS7lmGMflykYAxa8LlRatNG866zsE2sfZhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی پربازدید از زد و خورد یک معلم و دانش‌آموز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/696960" target="_blank">📅 18:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696959">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=GZGWz4STtzVxYqqbbNL-miZyDDa2730l2XXentt07h-W-4TW0q7QHKtezE-Lb9zlaJS7Wcl1lcBdaQ4N1elwX0bck0KfPlIgw6jV-ButKX2RFGqv1zx3ZqppO4tZKiXCbb1uoKU6-o4ys2hNpJ1PNa9IJfwac5LVgnOstuVOx0CZESp9A6ypB6OurZ6LIkpTWnsr5Vjvc-aNeRxL826jcbmFmKBdGPg7WovQ-hW2x5l9IySwD1O6zjdu7b_wCYE_FOkwWNP4Z4tqbB9mcKTVoH30T2_5jhmTBOLyZVstrWLM0ePeaHUnAxazCEora5OJm-GfdxovFK1gMNq8mzNm7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa65c912b.mp4?token=GZGWz4STtzVxYqqbbNL-miZyDDa2730l2XXentt07h-W-4TW0q7QHKtezE-Lb9zlaJS7Wcl1lcBdaQ4N1elwX0bck0KfPlIgw6jV-ButKX2RFGqv1zx3ZqppO4tZKiXCbb1uoKU6-o4ys2hNpJ1PNa9IJfwac5LVgnOstuVOx0CZESp9A6ypB6OurZ6LIkpTWnsr5Vjvc-aNeRxL826jcbmFmKBdGPg7WovQ-hW2x5l9IySwD1O6zjdu7b_wCYE_FOkwWNP4Z4tqbB9mcKTVoH30T2_5jhmTBOLyZVstrWLM0ePeaHUnAxazCEora5OJm-GfdxovFK1gMNq8mzNm7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به صنعت نفت؛ علی علیپور در دقیقه ۵۳
🔹
پرسپولیس ۲ - ۰ صنعت نفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/696959" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
امام جمعه تهران: پرچم داران فتنه زن، مردگی، بدبختی، ترامپ جنین خوار و نتانیاهوی پلید بودند
🔹
همین ترامپ قمارباز عضو جزیره اپستین و جنین خوار و کودک کش و دوست پلیدش نتانیاهوی پلید در جریان فتنه، پرچم به دست گرفته بودند و به زبان فارسی در آن فتنه پیام و شعار…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/696958" target="_blank">📅 18:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696957">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMIdq1gA_Vi-2oy4TIUxgpYKBjn1uC-ARWikQ3LEAXKFkJFUF9FUQdFVG9Wtf-OlmZNSLYVl3RS9wXMi_o-yqVa4jrFbVJZB37C7vYP-ahb02B2KAfsG-GxfSqjwlhBqQbbkavc7jfhmAwPaZZjbeBsWw3NwjAfO7hNI0ksr3J-N4hN1jmqg2cbnF66OO15Xh0JS0afZ_1Ei-XBr9_jN93zEU3hMf_67ylJYM7tCOB8wGZdcY-UW0ZFPjEZSvdMYHRMfBb5mMVsfl31GFKcH5wXrhVxLERImqCeRjS3YZ2cqE8I8w4tTVCuwXKxwu3JhXIZhjKCcFH6ueRT6-VWyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باز هم دست ترامپ از جایزه صلح کوتاه ماند؛ ناوی پیلای، قاضی‌ای از جنوب آفریقا برنده جایزه صلح نوبل ۲۰۲۶ شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/696957" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: ۱۰ تا ۱۲ خانواده از قبل انقلاب واردکننده خودرو بوده‌اند و نمی‌خواهند این کار را رها کنند/ واردات برایشان سود بیشتری دارد
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
ایران خودرو خصوصی شده است و باید صبر کنیم که چه می‌شود.
🔹
کسانی که در سر تولید داخلی میزنند فقط به فکر منافع خودشان هستند و روی حسن نیت این کار را نمی‌کنند.
🔹
در یکی از کشورهای همسایه ۵ هزار خودروی وارداتی برای کسب جواز‌های لازم معطل مانده بود؛ خودروهایی که ردیف قیمتی هر کدام از آنها ۴۰ هزار دلار بود.
🔹
۵۰ مورد از این خودروها را در اختیار کسانی گذاشتند که میخواهند تصمیم گیری کنند تا راهشان باز شود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/696956" target="_blank">📅 18:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: امارات و عمان در اجرای سیاست انزوای کامل ایران با واشینگتن همکاری می‌کنند
🔹
ما در حال رایزنی با پاکستان و ترکیه برای بستن مسیرهای زمینی ورود و خروج از ایران هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/696955" target="_blank">📅 18:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
هشدار نارنجی بارندگی در ۶ استان کشور
🔹
مدیریت بحران برای روزهای ۱۸ و ۱۹ مهر در گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی و سمنان آماده‌باش اعلام کرد.
🔹
احتمال رگبار شدید، رعدوبرق، وزش باد شدید و گردوخاک وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/696954" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPp2TX5BqDB4kPEdfQ-QaCa65sSAjHib9eg7JEhkwjK4K_s1SqdBDAlZCwE7bcuxHuWbBHoy2OyJ1Z9wnOG4F4GKDLXr6SAG2eInldbN9OamzflsUSCBaR5-ZxD-mpGRFL-uO9Q6O6IXMWGumQwCc-W0FDGrM5uYIFz7EBqESmMhHZuuPCgn1uPOG-AQIqQiOUA2xDGsR7sB87GShVw6f9pM_IUJ56MyfRJENMBvXn7J4a2wIFg1MbpUO8aK_2fnAPKgGhNzR3C28GZ2kVMgGuVps7xjG_NHR_gpud3f_xtVCrre2Poy25y6PwBb0B1lpK0J7iRoLfpbLBtCtTs64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نجات باتری گوشی اندروید؛ با چند تغییر ساده در تنظیمات، شارژدهی گوشی را دو برابر کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696953" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6TC_KQX3jNHxbUub6NwnqxEcWptadM7pBtJ6d3Dkx5G3eJl730okifPKpctkLkXG5VtFCwJaAIZTv8NUaMxV5L34pZsXvG2YwDqpt73lKJkPvKeO38Fen1JpWOodlftsgenlREwxvqCO1GWxIIL6hJBxb-lKdfiuCwGge3MP7985VxAZ6wUflb1AFIjyO4aGgm_a6ckeC5o-hJanl4LFemfCpRa0RNpIxIQv2Cr_hrDpsNhanrbjkjZ06Oek0uuoNt_WfKQ7XiUkHvZoflR75n8KmJk090AzaVdWo6YAoYVjH3UnePMcVwhDPEWTg4wPEn8EUO96NdbSIRw5CVGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/696952" target="_blank">📅 17:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
المیادین: ارتش یمن ارتفاعات مشرف بر شهر «تعز» را آزاد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/696951" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حمله تند میرسلیم در مقابل رانت خودروسازان: بیخود کردید به ایران‌خودرو و سایپا رانت دادید!/ صدردصد با واردات خودرو مخالف هستم
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
ما پول نداریم که بخواهیم خودرو وارد کنیم برای همین صددرصد مخالف این موضوع هستم.
🔹
پنجاه شرکت خودروسازی بیخودی درست شده که تولیدات خارجی را سر هم می‌کنند.
🔹
اولا بیخود کردید که به ایران خودرو و سایپا رانت دادید ثانیا اگر سر مردم کلاه می‌گذاشتند چرا جلویشان را نگرفتید؟
🔹
مردم ایران کم ندارند چرا خودشان زحمت نکشند؟ چرا سر سفره دیگران می‌نشینند؟
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/696950" target="_blank">📅 17:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ترامپ جنایتکار: از همه کشورها می‌خواهم تا از عضویت در دیوان کیفری بین‌المللی کناره‌گیری کنند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/696949" target="_blank">📅 17:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48de063267.mp4?token=lvKylIaH5SMMoKlSr2YgBWJ-tW8ektESbgAxje-1UopvdYZbYmEjUxfZdgZs33OWeuS3ijxLKdnJh63JRynOslobl7xqLvDR9v5ew5qSg5edjgOxXTf0VWAs4NDWZK6JWPM3eJ_EhZxJJUuSG2cshU2T4J3Lt3qhOJ2RE8wtmcgx3U8u2hpl52zrotc7wuykTxZRBqJFaBbXxrG16LZbd2X3ZZA4tmcbudmMCJeObrPwET2dVN3weC6lamfzSV5cZiZol5zVGq3QKI9fEHovLq5pNXZiFrtAK34L9B0t3rf0gGru2kXQ82itj0rwus90cc2CjOjPis4B0ztgT-zQqIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48de063267.mp4?token=lvKylIaH5SMMoKlSr2YgBWJ-tW8ektESbgAxje-1UopvdYZbYmEjUxfZdgZs33OWeuS3ijxLKdnJh63JRynOslobl7xqLvDR9v5ew5qSg5edjgOxXTf0VWAs4NDWZK6JWPM3eJ_EhZxJJUuSG2cshU2T4J3Lt3qhOJ2RE8wtmcgx3U8u2hpl52zrotc7wuykTxZRBqJFaBbXxrG16LZbd2X3ZZA4tmcbudmMCJeObrPwET2dVN3weC6lamfzSV5cZiZol5zVGq3QKI9fEHovLq5pNXZiFrtAK34L9B0t3rf0gGru2kXQ82itj0rwus90cc2CjOjPis4B0ztgT-zQqIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آدم‌هایی که با آن‌ها معاشرت می‌کنید، می‌توانند سقف رشدتان باشند یا سکوی پرتابتان؛ جایی رفت‌وآمد کنید که از شما آدم بزرگ‌تری بسازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/696948" target="_blank">📅 17:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
گزافه‌گویی
ترامپ جنایتکار: نیروهای دریایی ما رهبری تلاش‌ها برای اطمینان از این را بر عهده دارند که ایران به سلاح هسته‌ای دست پیدا نکند و این اتفاق هرگز رخ نخواهد داد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/696947" target="_blank">📅 17:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrGNgEdfUGvT2VqXipGc80ANXIxGHFpjgGxxPdBkrkqE19bBS7FA7pDbGXiUxTxQnCLD6dSfQRWjr5FeH7wdOKk4lP9jzmCaKGQXlMqREKHJ3RERGnqiKCQMMJDvyegIVBVbCQYFtC_SSULsGOliwP0fzsgeX_vSt2Cxk6RUXfRuzM7h1rUURrYSf-CB3dACt3aTZYt8GZ6JvO3wgMOtvacFN7BoG3uLHCBaHZpuwb8kf0LgttXZVWbsPlC51kKspnl6nirtDsDEJB3b_fVbkKp3Heyhbm4ORv5vqktYgu3bhIowS4FVraYkNuwFe3S1iI_1Hpbm2isYL1DJ1DxVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس آمریکا اسیر هرمز
🔹
مطابق آخرین داده‌ها، حدود ۷۰ درصد شرکت‌های بزرگ آمریکایی در ماه گذشته میلادی بازدهی منفی داشته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696946" target="_blank">📅 17:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696945">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b1cf6b09.mp4?token=WZN7b-ddDVZYGuNFURFMgDuP44g5nJU3ja23vbpFUxi-e-HdY5aQYGugc1LlLMYFsFwxMGOK8f3f5ux-ENtqDCHAn9MLQnFfCePjOq_dW8vxAifIaSAbstEZZ3kj8dDnirYBxVl8NmKc1qk7BoLgMJyaT8mP2Uho4a56itm0JMfUph9KvmUZ1aSxG8vQby8mT9Z3ci7ExYFmkn00a3FCT0LOCk037QLsnzaks7peLASc5nOIgC4gdKv_7Mv-sS1kRbrpzWOj5VAJABjt_ryMQEz10b-xOZj5vFtBxrU6AazR_pt1NE5ZdL-RB0eOfCyFQGxHqXgdYyRE9IXqzr9Jew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b1cf6b09.mp4?token=WZN7b-ddDVZYGuNFURFMgDuP44g5nJU3ja23vbpFUxi-e-HdY5aQYGugc1LlLMYFsFwxMGOK8f3f5ux-ENtqDCHAn9MLQnFfCePjOq_dW8vxAifIaSAbstEZZ3kj8dDnirYBxVl8NmKc1qk7BoLgMJyaT8mP2Uho4a56itm0JMfUph9KvmUZ1aSxG8vQby8mT9Z3ci7ExYFmkn00a3FCT0LOCk037QLsnzaks7peLASc5nOIgC4gdKv_7Mv-sS1kRbrpzWOj5VAJABjt_ryMQEz10b-xOZj5vFtBxrU6AazR_pt1NE5ZdL-RB0eOfCyFQGxHqXgdYyRE9IXqzr9Jew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی به لاوروف: سه جزیره ایرانی در قلب من هستند
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696945" target="_blank">📅 17:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696944">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM-9IfxS295Pv0fnOPaxFvHmVJkiQx7QTaFU74irI79c8oZLF3qIQCC0659bTzujXwuti9eNiMzEdTOjMDUiigL717dtYvK0eo0uZVCLd5psvqRaxI_bFWqHY5W0_bswHIvDva1zeVrpDY4ZrFbpwsl5vIIktPg0jZWHA-6O--ujP0zixLi6zNqSxuMxkPbeAesaPM6tsgumTIpIEuXMyCYz_QFgrwDNR6OaR7njbjuzX9Wb-4jUfBz0qive2LdiR4-xKDbJQL1iSxRPm8-ztBSj0b1RwOf0ft5BW0xDZP4Q2naMFhL5fA2L5zdaOrx2c_hVnPZe_RocMT-TQUU0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خانم دکتر افتخاری، معاون فرهنگی اجتماعی نیروی انتظامی استان سیستان و بلوچستان در حمله عناصر گروهک تروریستی به شهادت رسید
🔹
عامل اصلی بمب‌گذاری هنگام فرار کشته شد.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696944" target="_blank">📅 17:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696943">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgmxDw2qX7DW9Imz2FJ86jCDnS4RHN-PuU4q1mFQnl7O24U0-lJv-L7CvWnUaSgP0_Xz-BcGq_9oCnUFoHWkn7e8r988XlUghGpt3wr_fWdYpJBLfLPnesreJne5qmK6hPmHVjmsjh_mH5Ugnnu0gCHgeb8PRM45Ha6sr2tX3Bn3hxVDEnxwLki4PM61DJApcbPow7cJDRF73RDUUY8agJgs0dXxk_RKGKYw7xBPIbPCH1_cSrO6ajAJYn0aXh-TpHZ_9ltqJMKSDcv4jIl4qcrUzUxJIztRhhMLSGW6g-8a0o0W1E8nW3KAuADqLKQ-rMCPsf10qHNnt0rAZnR4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صابرین نیوز: یک منبع آگاه از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای نظامی در سیستان و بلوچستان خبر داد/برخی منابع محلی از شهادت معاونت اجتماعی انتظامی استان در منطقه چشمه زیارت زاهدان خبر می‌دهند  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/696943" target="_blank">📅 17:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696942">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcd6a39dab.mp4?token=fSQ6Iin-t9_d1qMbRwTaTegF985ThRRPnYCIbQbNUbTt0aSBlYH0CSFCdktNpUIbtw1Oj-bfvQaW1wNBx_18sDW-Z9CCL7kuHtmd0KaedCrH6T4O63ZCE9hca0-c0Vv7sHiHatN-JNe7lJUEES9MqEWtmEcLlbBRjev7cBLRHaluegWk6bF9bJ9tor2dT54abD3HDZ3FRt6nuMoGDjCcKwghINnM1Hx4q7gWqVMo4kn7JXnPDIIPRsD3uJ6KagmGNiefA6b5Stl3e0x85vlh-r_0D_labnzU1rFUfp_NyHuFXB8Bt---AslHdqsUjyVflSPWogCGRlt4X5sg4cKFBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcd6a39dab.mp4?token=fSQ6Iin-t9_d1qMbRwTaTegF985ThRRPnYCIbQbNUbTt0aSBlYH0CSFCdktNpUIbtw1Oj-bfvQaW1wNBx_18sDW-Z9CCL7kuHtmd0KaedCrH6T4O63ZCE9hca0-c0Vv7sHiHatN-JNe7lJUEES9MqEWtmEcLlbBRjev7cBLRHaluegWk6bF9bJ9tor2dT54abD3HDZ3FRt6nuMoGDjCcKwghINnM1Hx4q7gWqVMo4kn7JXnPDIIPRsD3uJ6KagmGNiefA6b5Stl3e0x85vlh-r_0D_labnzU1rFUfp_NyHuFXB8Bt---AslHdqsUjyVflSPWogCGRlt4X5sg4cKFBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از بررسی VAR، اعلام پنالتی به سود صنعت نفت رد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696942" target="_blank">📅 17:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696941">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb6cd3c76.mp4?token=r-Z_qHor9WZ9S3Ygypg24RZ-F47D8Y8wspYVwvkPLHJkv8wW9FPrewzMaivawSKjZPFMLArdR_4HHmypFPE4GC3zSlsl1Iu1Bg68HFAweqfLhdXOTZvqMvrenHIDojbNg4MTOFzey41mKw2QxetHFMU43I0NTkqldbB5aJ44FU2k-WRZ2oRHHxeOn3fLMNIy4xZkvYjNW1aYqZGhRoJTFpaOPixdbgmbDio0EKZPE_-9yY34wEOrFPTpaE9U7h-6kVGn1rzZw-VNdaKx0Dz5SIX9Mr6QuTwHKatoKt6TjIuFrv-VbnvOtoEo3abL5DPsnyl3kACJU1Frs2dQDV9Lz6id9e1TKbBBJtfjQwuRz_CQKAdKi0nZCRSoxik6SxI-4xSV38iFzSSiPWgqLTWFGyyGcOBFiRL8dtVPcVYiySbZEN0I17pirqdhdLW_VRko3DoCRznxghzPle9HRyQeqXoZm38tiLmrTyqrC58LMtDrCoBxHrXKO9V1UOSCUM1-7cyzkKz6foCPOsb9zFPNdRtGtysH_BzlQ_x-TmYjf0aRL6FUGn9OsPhjc1Zby2K1AvOZ0zik1NGi7ibMmtWO6lKCW9tRq41MGkbxRQLRCSXj6RY6reAIGaFqKa1uXjSb3a6KzYb19Ti93iO7IJ6WWxQRtYnzncqjOML3gnDNpNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb6cd3c76.mp4?token=r-Z_qHor9WZ9S3Ygypg24RZ-F47D8Y8wspYVwvkPLHJkv8wW9FPrewzMaivawSKjZPFMLArdR_4HHmypFPE4GC3zSlsl1Iu1Bg68HFAweqfLhdXOTZvqMvrenHIDojbNg4MTOFzey41mKw2QxetHFMU43I0NTkqldbB5aJ44FU2k-WRZ2oRHHxeOn3fLMNIy4xZkvYjNW1aYqZGhRoJTFpaOPixdbgmbDio0EKZPE_-9yY34wEOrFPTpaE9U7h-6kVGn1rzZw-VNdaKx0Dz5SIX9Mr6QuTwHKatoKt6TjIuFrv-VbnvOtoEo3abL5DPsnyl3kACJU1Frs2dQDV9Lz6id9e1TKbBBJtfjQwuRz_CQKAdKi0nZCRSoxik6SxI-4xSV38iFzSSiPWgqLTWFGyyGcOBFiRL8dtVPcVYiySbZEN0I17pirqdhdLW_VRko3DoCRznxghzPle9HRyQeqXoZm38tiLmrTyqrC58LMtDrCoBxHrXKO9V1UOSCUM1-7cyzkKz6foCPOsb9zFPNdRtGtysH_BzlQ_x-TmYjf0aRL6FUGn9OsPhjc1Zby2K1AvOZ0zik1NGi7ibMmtWO6lKCW9tRq41MGkbxRQLRCSXj6RY6reAIGaFqKa1uXjSb3a6KzYb19Ti93iO7IJ6WWxQRtYnzncqjOML3gnDNpNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین وسائلی که از گذشته پیدا شده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696941" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696940">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دفاع تمام قد میرسلیم از خودروسازهای داخلی؛ بگذارید ایران خودرو آزاد باشد
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
بگذارید ایران‌خودرو و سایپا کار خودش را بکند.
🔹
به ایران‌خودرو به خاطر دولتی بودن تحمیل می‌کنید کلی آدم استخدام کند درحالیکه دولتی بود.
🔹
بگذارید ایران خودرو آزاد باشد چرا باید ایران خودرو با ۶۰ هزار نفر کار کند.
🔹
برای تولید خودرو قیمت مواد اولیه را به ایران خودرو به قیمت جهانی می‌دهید و می‌خواهید قیمت یارانه‌ای تولید کند و به شما بدهد.
🔹
وقتی واردات انجام شود خودروسازی‌های داخلی اصلاح نمی‌شوند، شما توی سر این‌ها می‌زنید.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/696940" target="_blank">📅 17:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696939">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd4238f6f.mp4?token=PYBbqgIZwfnGtiCzxkvREk_GC5fxTPLBpRWyTffq8gKYIdREXa2RuqFFipfZmnGt64ZGTYS4lsLo3uPO2vZvwcxdPn2XQtFg1mOdMcFkyIbwX0BcPUz3zLzedPugqvXJMNKJddBhjgkVmFCgyZO9GgNGRNxeMDlVtn0BxIxyNRslh7XJ1FgUHZFhmAkgjUaU0CQMoui_xVIHAB5Fr8TepFPCxv0g4zZnRrT1_1zM7VyE-2KzCIFVwLJI5nrUX7o3amaLM1tQD-g-kpdVg47vdrbn9sCQQiJxVmVcIzjoc-7jQ432TOsUxA_o0NR-1QY7E9r9j0V3eowXOkrJzy77QZqmmTxywzBV2iQ8iE9rxegiBJ9Yn2LNTh207Dw63vlYfP6_20JulY9toDIKPlmLoKKnY6Wn_DZ9LmeI2JTdqRGR3px04RXa7mfwdaiCQSqwkDbYuggYQCAtD9xjf6SclAmBcfUTjr6nsogxM0KvIDulXDK-8paiAk8bp7vBO_gJn0b0KXrwjETZjJQcoRrRoRNHo6EOWvFdlgi1hAzfqNYAB1PPs27cxeUSJiAfgdOz8G7zDBSd_GTp05eG6s-xPiwqhAxTVFLKA5VobvfBJjInZB3UyxNIGr2KRBUQFAYDAFuLxD8cg7BKasDTbhCmQJTFp72vvxKQ9fAQ_8QY-6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd4238f6f.mp4?token=PYBbqgIZwfnGtiCzxkvREk_GC5fxTPLBpRWyTffq8gKYIdREXa2RuqFFipfZmnGt64ZGTYS4lsLo3uPO2vZvwcxdPn2XQtFg1mOdMcFkyIbwX0BcPUz3zLzedPugqvXJMNKJddBhjgkVmFCgyZO9GgNGRNxeMDlVtn0BxIxyNRslh7XJ1FgUHZFhmAkgjUaU0CQMoui_xVIHAB5Fr8TepFPCxv0g4zZnRrT1_1zM7VyE-2KzCIFVwLJI5nrUX7o3amaLM1tQD-g-kpdVg47vdrbn9sCQQiJxVmVcIzjoc-7jQ432TOsUxA_o0NR-1QY7E9r9j0V3eowXOkrJzy77QZqmmTxywzBV2iQ8iE9rxegiBJ9Yn2LNTh207Dw63vlYfP6_20JulY9toDIKPlmLoKKnY6Wn_DZ9LmeI2JTdqRGR3px04RXa7mfwdaiCQSqwkDbYuggYQCAtD9xjf6SclAmBcfUTjr6nsogxM0KvIDulXDK-8paiAk8bp7vBO_gJn0b0KXrwjETZjJQcoRrRoRNHo6EOWvFdlgi1hAzfqNYAB1PPs27cxeUSJiAfgdOz8G7zDBSd_GTp05eG6s-xPiwqhAxTVFLKA5VobvfBJjInZB3UyxNIGr2KRBUQFAYDAFuLxD8cg7BKasDTbhCmQJTFp72vvxKQ9fAQ_8QY-6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس توسط بیفوما در دقیقه ۴
پرسپولیس ۱ - ۰ صنعت نفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/696939" target="_blank">📅 17:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696938">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f341ddbe37.mp4?token=ZqZDt4eh1ZvafREpePeZYaDDz8yJEey90CL2ibtzu7vxtfqd2pgYCuJL-5VFnEVVLyHy_6w0DwVmIh_QFNuBCJEQ1ehqPCbnX79ErlSZ6nIJoAsQQCR4AvoQGAdlyckAiX6nmT_AFFjgFQ9qQCxaxv_73bvysS_LGKvHGzWJTSd8AEbVWpGSVRZLD7wu676D4cGQXJ_10s8M9O6-QrqMNzApZUHVwwhNRQSnvIHxOk51Ps-x8paBZkPujEJ7U5GJA1qUIt6WjgZ9kMnYTAmspIESVS7h7KLXQwxiPv9mmCFc3T0QAUW9rvqm91kMshG3Z1Ck0CugVBPbFyqFphPyNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f341ddbe37.mp4?token=ZqZDt4eh1ZvafREpePeZYaDDz8yJEey90CL2ibtzu7vxtfqd2pgYCuJL-5VFnEVVLyHy_6w0DwVmIh_QFNuBCJEQ1ehqPCbnX79ErlSZ6nIJoAsQQCR4AvoQGAdlyckAiX6nmT_AFFjgFQ9qQCxaxv_73bvysS_LGKvHGzWJTSd8AEbVWpGSVRZLD7wu676D4cGQXJ_10s8M9O6-QrqMNzApZUHVwwhNRQSnvIHxOk51Ps-x8paBZkPujEJ7U5GJA1qUIt6WjgZ9kMnYTAmspIESVS7h7KLXQwxiPv9mmCFc3T0QAUW9rvqm91kMshG3Z1Ck0CugVBPbFyqFphPyNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک مرد به طرز شگفت‌انگیزی از یک حمله پهپاد مجهز به موتور جت در منطقه کی‌یف جان سالم به در برد و تنها چند ثانیه قبل از اصابت، از آنجا فرار کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/696938" target="_blank">📅 17:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696937">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-text">متشکریم از شما بینندگان محترم
سریال «بدنام» برای بیش از
۲ میلیارد و ۳۰۰ میلیون دقیقه تماشا
تا امروز و ثبت
پرمخاطب‌ترین سریال فارسی تاریخ شبکه نمایش خانگی
‌
📺
❤️
قسمت آخر سریال «بدنام» همین‌حالا در
#فیلیمو
کارگردان: احسان سجادی حسینی
@filimo</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/696937" target="_blank">📅 17:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696936">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPcZs-Hdfsy9GxaFkAQt9CDRn7rQKmbaAaQAxrX-oF_A_fOlymB6u_f2pc7pUwG4875tP-SPMuQ67fN7oWZepNJFVWYcN4mdLSjIivdkzTCw6NvcD3gpix7SWNpqjU0EU-JjBKa47_rVZFbiUndM_1lVQfmVPFpzPmecsjQkppxNBtoh0YElFAdbJ8z2lgH50AoZMHMYhN58-d3NlCEHhJTi3A0hB_ehwDQzIqVECDW9reKSp3V7rJl6-XqxE0LZz-q86pWKIlwRrxR4070wS9n2DWrnYzp9fv0cFiJlFMrZceEtDj55ncc_4CS4bKhbJ9jaQCIhYudJ8ETd3qlxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی
#بیمه_البرز
از نخستین برات الکترونیک در صنعت بیمه
در گردهمایی مدیران و رؤسای شعب بیمه البرز، از نخستین برات الکترونیک صنعت بیمه به همت بیمه البرز و بانک تجارت رونمایی شد.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5111</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696936" target="_blank">📅 17:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696934">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43ec82752.mp4?token=GvQOnwOdPPOPU4IzTd99agArCEMp8G732ogLBD1WA2FTc21yeWUxYsksWMIc4Kitn-JgEyy2jH5EKskX10xY_qcj-QE9NwGZ_zZoocFmIm5-q4JiVG9MUXn2S75lKv2Uvl8ox6SDfgUNR9DIELQHncQEeWV5CSXUKgAPz0NW4hsQQMNc7smC9dO7oQRximp3eiSVWVDvcqiJT6QxHKi98_qkv03n95yGY3o00y4pXY1JIxXt4VGi1GsRlaslawNt3HrZ9jb_7-5Fkc7i0dJpuKFDfyKB4wQqcqE-FcroZBCfrLRD1776OAymLiUkOf0BH4AJokS8fEnto6z63NT_NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43ec82752.mp4?token=GvQOnwOdPPOPU4IzTd99agArCEMp8G732ogLBD1WA2FTc21yeWUxYsksWMIc4Kitn-JgEyy2jH5EKskX10xY_qcj-QE9NwGZ_zZoocFmIm5-q4JiVG9MUXn2S75lKv2Uvl8ox6SDfgUNR9DIELQHncQEeWV5CSXUKgAPz0NW4hsQQMNc7smC9dO7oQRximp3eiSVWVDvcqiJT6QxHKi98_qkv03n95yGY3o00y4pXY1JIxXt4VGi1GsRlaslawNt3HrZ9jb_7-5Fkc7i0dJpuKFDfyKB4wQqcqE-FcroZBCfrLRD1776OAymLiUkOf0BH4AJokS8fEnto6z63NT_NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریستیانو رونالدو زیر پست لیونل مسی: لئو، سال‌های زیادی برای کشورت جنگیدی و یه میراثی به جا گذاشتی که برای همیشه موندگار می‌ مونه؛ بابت تمام کارهایی که با آرژانتین انجام دادی، نهایت احترام رو برات قائلم. یه بغل گرم رفیق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/696934" target="_blank">📅 16:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696933">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFi9gtP-IJ5conMfDhtk9ULtG5TfVTjExVM9z0mI9TLorMDKfP8uwitHQNBuQEVbHT3JXkOluEern7AxUjNOYpM8X4XvCHUR84diHtNxC8cAL3Hs2MtLGcS1hF68zktU4BrcNd71kbuIFyQJllixmBv39p1UgVDTa5NilFgmLjq4q2B78jkr1Z_lmbzfubiBXx0cPDGqLCpqb0oYCsYNyofwjjwqPt1KEhcIyaJuN5RJYXtxTsta0QuuwrFigoZ4_Hik_z64m6huyoa2CQa_I6hAOoE9HnDIOvJxw3TcHmQFFZjI2G9gFMKHSTk7urjDCtfGzWkyBXOYrvHIWMwe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ کشوری که بیشترین رسانه‌های مخالف در خارج از کشور را دارند!
🔸
ایران با داشتن بیش از ۳۰ کانال تلویزیونی ماهواره‌ای و بیش از ۱۰۰ کانال و صفحه رسانه‌ای بزرگ و میزان دسترسی حدود ۶۵ درصدی، در رتبه نخست این فهرست قرار دارد.
🔸
روسیه با دسترسی حدود ۳۰ درصد و ونزوئلا با حدود ۳۵ درصد دسترسی در رتبه‌های بعدی جای گرفته‌اند؛ همچنین کشورهای چین و کوبا نیز در جایگاه‌های سوم و پنجم قرار دارند.
🔸
در مجموع، فعالیت رسانه‌های خارج‌نشین، شبکه‌های تلویزیونی، رادیویی و پلتفرم‌های دیجیتال تبعیدی، سهم قابل‌توجهی از فضای رسانه‌ای این کشورها را به خود اختصاص داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/696933" target="_blank">📅 16:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696932">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVzQAqKa8Lk66uDYqzoACyOJtm9dCHNFjVSPzrNNCiEv-0LACnZltVe88clH-GlzsFy7u8CXUA7Xr5XqJ1BVwseTNz2gX5hWlKhj28RJMyzO2PyXk70VX-zZ61Jf88ceu4Kko4chEhJi3rVLwDMwbCWjGpLCxUfk6U-AzVZEfJC9rMoQkh4MAeztfxRrn1Y732N4p2F0tJdX5aq-eGo9SdY1h3SgTtIa-A14OG_hF2_03avf8PdQnuCPh0_MSbh7HHdBklM8dzzAF2mJYXsAQ1oluUqn8UCoidaVJ6DiuyO8_k1Jkh1bfjbBuC60ozh4TLJU29a5v3ul-2TQaXhkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل‌مپس قیمت سوخت را در بریتانیا نمایش می‌دهد تا رانندگان بنزین و گازوئیل ارزان‌تر پیدا کنند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/696932" target="_blank">📅 16:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696931">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
صابرین نیوز: یک منبع آگاه از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای نظامی در سیستان و بلوچستان خبر داد/برخی منابع محلی از شهادت معاونت اجتماعی انتظامی استان در منطقه چشمه زیارت زاهدان خبر می‌دهند
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/696931" target="_blank">📅 16:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696930">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpEkUdk_kgfON7pMx4ckb_b7xwaHzNz3mqkRlfXP3BhNm7zDPVv3-2S0gZkWUJ7syDC0KB6kyittxfRonOby4bjbB45uEw74SWPuxDvzR4p7hfCFSAsUzp4j4vIzcItmnPhXEV-Yy9B8wj6My4oYKNbL67IaEeyuEPkdPa1OONdGxSQ6m0QFHUigqgTdknutLe3ntWFC2htIFaFnkEtQeJ2Ni_FkjZ8HWlQsllDZHXWG-Bhm6LXg7HiTc-4hcL3p_mXqZI-Lo-HB6t-0ycF8HgW94yCJZPrQPaOqUzaTfeCSl0pKqDv_qp2m_rX70HWo-zHwzhK2tmgnJmq76smKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیوار مهربانی در یکی از بیمارستان‌های شیراز؛ مهربانی برای نجات جان‌ها
🔹
در این طرح، افراد به‌اندازه توان خود کمک مالی می‌کنند و رسید پرداخت را به دیوار می‌چسبانند تا بیمارانی که برای تأمین هزینه‌های درمانی نیازمندند، از این کمک‌ها استفاده کنند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/696930" target="_blank">📅 16:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696929">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: گزارشی از وقوع یک حادثه در فاصله ۱۳ مایل دریایی در غرب منطقه الجزیره در امارات دریافت شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/696929" target="_blank">📅 16:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696928">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سازمان هواپیمایی پاکستان (پی آی ای) اعلام کرد که تمامی پروازهای خود را به مقصد ریاض پایتخت عربستان به حالت تعلیق درآورده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/696928" target="_blank">📅 16:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696927">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSQE7aeQIf3HF_0F2C0gQfzNjjqf1IsJASaYlkdf8Mc0QrZsUbnvT4GXsiM2CcuQQjYPJ5zQiquSGTR3GaGJpVV-SqbIEEZzJaQGSL8ym4muKdr5GCPJGyIUwinf8fWSOzzEeDY_ENgg0iVDWX7Gw1dA7E0k-WdlWFEzXL7W6e3piu6qtubStWqhyDu8Q19q-vXTCyRJObc-p-hH9YdM-HnF57FfI3l8ucCFiheLmmkfNuwatE7SW0_Xr-CW9maShqZ3UU7MSFKsNBRQ239KgM2izSBunMMyQbCMjmYYBCcWZrSydLTLm0WRmid8byVFUl0_A27zi-aP2AHnynw1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رنگین کمان در آسمان تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/696927" target="_blank">📅 16:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696926">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ad76c3b8.mp4?token=Q5eWf7_49Xz8G1QTzLV5_koHMHOi0ml6-4wgdTvJ9SBPonWV6R3sljihqtfBx0s6jV7373pEN7H_1fQ69HCxKfp2dDauq6iDtWDe43FCf4cvchbEsCFPxbob1I31HiiKdd83Nf_gmq2fcKaTrqMJ3PxgOAH4BpCECHOCKwjv6mSZL9GfiSH-KmT5lxAOFBWrBhLwrN-LiUUmOrYxvPugAwoFQJLKS2BYRBWZpDj6_MU9YkFs6IKww9sNSeY5_GN1VUWf85hNRzVLn5A--IcIe7oMjGGV8Zd3TMc9jUMXXRd5sa_GhYUFFTvvmPFrk5K-bDA8vhmnLXsfY_9vNqOkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ad76c3b8.mp4?token=Q5eWf7_49Xz8G1QTzLV5_koHMHOi0ml6-4wgdTvJ9SBPonWV6R3sljihqtfBx0s6jV7373pEN7H_1fQ69HCxKfp2dDauq6iDtWDe43FCf4cvchbEsCFPxbob1I31HiiKdd83Nf_gmq2fcKaTrqMJ3PxgOAH4BpCECHOCKwjv6mSZL9GfiSH-KmT5lxAOFBWrBhLwrN-LiUUmOrYxvPugAwoFQJLKS2BYRBWZpDj6_MU9YkFs6IKww9sNSeY5_GN1VUWf85hNRzVLn5A--IcIe7oMjGGV8Zd3TMc9jUMXXRd5sa_GhYUFFTvvmPFrk5K-bDA8vhmnLXsfY_9vNqOkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهکار خلاقانه نسل جدید کلاس اولی‌ها برای مشق نوشتن
😂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696926" target="_blank">📅 16:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وقوع چند انفجار در اربیل
🔹
منابع خبری امروز از شنیده شدن صدای چندین انفجار در اربیل خبر دادند؛ هنوز علت انفجارها مشخص نیست./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/696925" target="_blank">📅 16:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d28c230a9.mp4?token=c8BZXXYij-pcsIdjbZoKsMTeVPCA9Xf96E72BsHbbbF-9qNwn2YXrvGQ_j5bPEwuttibCdd0Z2A8TlqxsHD97fHKnjDQ57CfLdXUCRQNtGGyBZzYPghUYGGrgII4tGJnr0kLPIPLztdJqnGeCQqGKgtnCfLz_8H0EOZVZNRUveTuz-Gv-Q8BWdASNnX5IBjT0H72QDmy-sPZSidAGnwoNsFQCkoAiNGowcd2Oq5N-MnJGQ00OGvAyUVqfj_cAiQnibzWGXBI7_8FC7x1Ubqv0dMd-d4Nk6gb3V2gugl7EvTv-zNtqels9oYPfY4FwthfAeJBP7DYdbUib0tUdrJFEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d28c230a9.mp4?token=c8BZXXYij-pcsIdjbZoKsMTeVPCA9Xf96E72BsHbbbF-9qNwn2YXrvGQ_j5bPEwuttibCdd0Z2A8TlqxsHD97fHKnjDQ57CfLdXUCRQNtGGyBZzYPghUYGGrgII4tGJnr0kLPIPLztdJqnGeCQqGKgtnCfLz_8H0EOZVZNRUveTuz-Gv-Q8BWdASNnX5IBjT0H72QDmy-sPZSidAGnwoNsFQCkoAiNGowcd2Oq5N-MnJGQ00OGvAyUVqfj_cAiQnibzWGXBI7_8FC7x1Ubqv0dMd-d4Nk6gb3V2gugl7EvTv-zNtqels9oYPfY4FwthfAeJBP7DYdbUib0tUdrJFEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه هوش مصنوعی متا از شما جاسوسی میکند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/696924" target="_blank">📅 16:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f74a4d50.mp4?token=BcYoBPKWpLe0VCUwg2Y1DjlteTnpxZOYpotAyJ3iF-2Eohl8Y1RKPDWEx4OhAXaEEY4vWp9A7Goz-nWquq6WkDSTRKzqpdm6jKo8uEVrr-FZU8xwdmMT-PXBfAUW8OnGimXJEgSpcuPCICjFo6yzB6LKsfkxLL80b--Jg1QwN-7ofLFTvn2Jb5YprUDx_m4k64SRoE5mkT4QwDr1otn6890pSxth9m67CreqZ8lKJxVY3rLMwkUXOEh4fxfMjdkJtQAcuHazlhhSVqJraWEP9XRBCvfPULqn85ip6tWXXnL9J0B6CYCD1xwBQ27PfQ-txz3gVlvKjwXNXdmd9GVIRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f74a4d50.mp4?token=BcYoBPKWpLe0VCUwg2Y1DjlteTnpxZOYpotAyJ3iF-2Eohl8Y1RKPDWEx4OhAXaEEY4vWp9A7Goz-nWquq6WkDSTRKzqpdm6jKo8uEVrr-FZU8xwdmMT-PXBfAUW8OnGimXJEgSpcuPCICjFo6yzB6LKsfkxLL80b--Jg1QwN-7ofLFTvn2Jb5YprUDx_m4k64SRoE5mkT4QwDr1otn6890pSxth9m67CreqZ8lKJxVY3rLMwkUXOEh4fxfMjdkJtQAcuHazlhhSVqJraWEP9XRBCvfPULqn85ip6tWXXnL9J0B6CYCD1xwBQ27PfQ-txz3gVlvKjwXNXdmd9GVIRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از طوفان شدید شب گذشته _ هفته بازار تهران
@akhbartehran</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/696923" target="_blank">📅 16:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد؛ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/696922" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696921">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد؛ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/696921" target="_blank">📅 16:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtGNNNE8-pW1xeDx69H3onqlUbQp1bA8-wzaiAob0c3mzf1l00bbQc-XuRFooCBOO2ZeikLbo4bvmfycWXkXPClittHBDBbVcAruH6cGh-vAP_83t5_CkUfJtnlAEDN05UE104qkyM28EBMVpTwAQq1lkpGxz0VPw7nJefQ9ye7XYJlr2h-Nh3qGHHuiw4FesogGUev0aPa98a747jDjih6aA3l0CN8sGHX3UV2r0Ri8RGUSC1B3U7_RMjsGjszl5K8dnnsMGcRrL2VTEVydbl0XLruXK64BNP0QH1OdlkvF60uEAzEZZhMOxDfJR74U4IiuBhNlPkR4yRbpWy97sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنده مسابقات عکاسی کمدی از حیات وحش؛ آخوندکی که لم داده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/696920" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696919">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs3h5hJKMg_wz9uHhqeQDCpvXTMDX0mdyNRW5iA3EcW_aQ08HYseFgI3MoacOWMFnmWUoYhnRao_5afOcBZaiOa6fHuXRKnHqoAaXdOZuxSdiRRjrIxottg8oeZ9qrk_gL9WxRAndaZ5BNeKSGQ_Mjs60XBTeRwFEefP44JmOpxHvpKt7-xFvvZPBQ7lzCq7UfHzpUaj6j3nNuRJ5dNDU3KfcVqnIPvm3laIWVhwM12HrnI-P2TsZJp8O_Vr7DFQJ4vYXmIh4znOnVeO7MMii-vKma4AWizubcB4Z1Wsu8TuEne3vC9RQAEO0epjQKZ-mDOPxTuC_hJ9gY_LLJWwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده ورود سربازان پاکستانی به یمن/ شاهد جنگ ریاض - آنکارا- اسلام‌آباد با حوثی‌ها خواهیم بود؟
🔹
چرا عربستان از پاکستان و ترکیه کمک گرفته است؟ آیا ریاض امید دارد با کمک گرفتن از اسلام آباد و آنکارا بتواند مزدوران خود در یمن را پیروز کرده و سبب شکست انصارالله شود؟ به نظر نمی‌رسد هدف عربستان دستیابی به یک هدف میدانی مشخص باشد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251085</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/696919" target="_blank">📅 16:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696918">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFlpjDuGCLnXk6KWERhIEwpsPC1yrgyKpTkoO0D03yZtA7LizOi2eRccGGh3yeB9KKrCsXAIMHMM0fheq2m893msCws_Fbu420pkXrF9AXdi7LIHp2IsAOeLkeUczFOodMFKXeM7r8UdH0BTXfbarAcpywNwD-tFcuxTc1t2LeMDtOcVH7Pk8zWjTveVHT1-ZIRP-XmoV7m_uls-zGYjHxCtk4wYFr_3Ct_wd02ODv-YuYQKca5QNQPrm-4B_CMlx1RWPbnFCWrCBB-la-QNr4C6Dap0yDqVEV8egqBTLuxVfBu3PRE0nhXylsyu9gtPGFIhlMz9oEP6rHaKJ-kQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خانه اربابی در روستاهای شهرستان نکا، مازندران
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/696918" target="_blank">📅 15:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696916">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913cab507d.mov?token=j7PZTkIl3J1BNFdb4nUrKtn5euKCmligZr9fhSUdn6_FLzooPm3MBslgSP-dxeq0cBvwdU4ofNRuIo2BGxfre1HvbAQl_tABD2s_iNp4E3oNvAUuZqFdy4OC1n0SozYmDi05xDU0teyXeWGdJMmKg_TbvGz3IPeOPk_DXDVkx8rnhtYIRo0Fv15y6syzkg-iqReagB4B3l7L_hNjtUz4kOugXuCiuc6BAJLBuGXdI5o9L5wiLSQ9MtAWe3bBy39fJPyCykbRgTQ6dP1SHou3Bd6jhNi-2nWu73ZrOiPSHyRcKHUpne9LKzQ4_42ErLe6MKVbvuuVAmBCBD2uW7NcMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913cab507d.mov?token=j7PZTkIl3J1BNFdb4nUrKtn5euKCmligZr9fhSUdn6_FLzooPm3MBslgSP-dxeq0cBvwdU4ofNRuIo2BGxfre1HvbAQl_tABD2s_iNp4E3oNvAUuZqFdy4OC1n0SozYmDi05xDU0teyXeWGdJMmKg_TbvGz3IPeOPk_DXDVkx8rnhtYIRo0Fv15y6syzkg-iqReagB4B3l7L_hNjtUz4kOugXuCiuc6BAJLBuGXdI5o9L5wiLSQ9MtAWe3bBy39fJPyCykbRgTQ6dP1SHou3Bd6jhNi-2nWu73ZrOiPSHyRcKHUpne9LKzQ4_42ErLe6MKVbvuuVAmBCBD2uW7NcMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز بارش باران در هشتگرد؛ این موج بارشی به سمت کرج و تهران در حرکت است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/696916" target="_blank">📅 15:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696915">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
امام جمعه مشهد: دشمن با برگزاری برنامه‌های مبتذل در شهرها، به دنبال ایجاد رقیب برای تجمعات است
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/696915" target="_blank">📅 15:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
توییت معنادار باراک راوید، خبرنگار آکسیوس
🔹
نگاهی به گذشته: در ژوئن ۲۰۲۵، پیش از عملیات «چکش نیمه‌شب»، کاخ سفید اعلام کرد که ترامپ «ظرف دو هفته» تصمیم خواهد گرفت که آیا آمریکا به جنگ اسرائیل علیه ایران می‌پیوندد یا نه.
🔹
اما زمانی که این اظهارات مطرح شد،…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/696914" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نیمی از واردات کشاورزی ایران در دست دو کشور!
🔹
بیش از نیمی از ارزش واردات محصولات کشاورزی ایران در پنج ماه نخست سال ۱۴۰۵ به روسیه و برزیل اختصاص داشت.
🔹
همچنین چهار قلم روغن نباتی، دانه سویا، کنجاله سویا و ذرت دامی بیش از ۶۱ درصد ارزش واردات را تشکیل دادند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/696913" target="_blank">📅 15:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696911">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200536c161.mp4?token=t6DOIdkb2MaPvQuazXPfdH7zM0Vhw45vTrt9SVTH6dVNsGnIN3AQv1mv9eQu8A7II_6583Tp1mGSLjKGRMK9bQfQj0fXo1dMqNYDrgyyT72iIZLp1z6VEc8QGbh0Hzi-R5xfxHRkiaStri9Waez8bHho1t7mnoPx0MY1Z-u5RAar4qVDdxpSJYRkdQGTYzP6ls06qxBksi-JjjVNNky2Q3MS4akHF1n5D1qhmWcId2NU2wu-qyqiC7ZXw8DyT0fv0_aivkNKL7DVX895Rp8NyQyrWIJKEmINfC_mIWCiRo8btJh7ieL--ANND1gPj2UIjuNSNxaWmtVUEuqPXJKRNVylR5An8Mj15UGQ4QhgN7q1ZGBkYCtsYroPPaPOj2jvD2RUtd_P7RRTh09iW23dkZCWskLJFlFuk0esZjBKKCd4wuG5KF1qiVRce-tPYUUDHr5kQ3CRPh0vCNgdBRhDWD1fef27WQIeFic-s-SixDqSz-uXIszS-9Pi2Ro0lyDyeHFC4MLEqy8aRylUaif3JpMjZznbtsfAUbBzb8Jgzqh7tnubmYe-62OjHs0KjyF1CP7LH5BVV5r5NGtB8IeIPL6spG__I7dnOPwZR5Qcr4NoRyCuj0jcbpavLVn0xfUti2nnvg4OcXQuayfC4fKRAGPUq0ro4I0PULgU_H8HDHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200536c161.mp4?token=t6DOIdkb2MaPvQuazXPfdH7zM0Vhw45vTrt9SVTH6dVNsGnIN3AQv1mv9eQu8A7II_6583Tp1mGSLjKGRMK9bQfQj0fXo1dMqNYDrgyyT72iIZLp1z6VEc8QGbh0Hzi-R5xfxHRkiaStri9Waez8bHho1t7mnoPx0MY1Z-u5RAar4qVDdxpSJYRkdQGTYzP6ls06qxBksi-JjjVNNky2Q3MS4akHF1n5D1qhmWcId2NU2wu-qyqiC7ZXw8DyT0fv0_aivkNKL7DVX895Rp8NyQyrWIJKEmINfC_mIWCiRo8btJh7ieL--ANND1gPj2UIjuNSNxaWmtVUEuqPXJKRNVylR5An8Mj15UGQ4QhgN7q1ZGBkYCtsYroPPaPOj2jvD2RUtd_P7RRTh09iW23dkZCWskLJFlFuk0esZjBKKCd4wuG5KF1qiVRce-tPYUUDHr5kQ3CRPh0vCNgdBRhDWD1fef27WQIeFic-s-SixDqSz-uXIszS-9Pi2Ro0lyDyeHFC4MLEqy8aRylUaif3JpMjZznbtsfAUbBzb8Jgzqh7tnubmYe-62OjHs0KjyF1CP7LH5BVV5r5NGtB8IeIPL6spG__I7dnOPwZR5Qcr4NoRyCuj0jcbpavLVn0xfUti2nnvg4OcXQuayfC4fKRAGPUq0ro4I0PULgU_H8HDHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باز هم دست ترامپ از جایزه صلح کوتاه ماند؛ ناوی پیلای، قاضی‌ای از جنوب آفریقا برنده جایزه صلح نوبل ۲۰۲۶ شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696911" target="_blank">📅 15:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696910">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اینکه می‌گویند خودروهای تولید داخل لگن است و مردم کشته می‌شوند، مغلطه است
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
اینکه کارشناسان می‌گویند بخش اعظم آمارهای جراحت، مصدومیت، فوت و...به خاطر خودرو است ، اشتباه می‌کنند. کدام کشور را سراغ دارید که بنزین‌اش مانند کشور ما مفت است؟
🔹
شما اگر مانند کشورهای دیگر روی سوخت قیمت واقعی گذاشتید، آن موقع توقع داشته باشید که مردم بگویند چون سوخت ارزشمند است پس ما سراغ خریدن خودروی ارزان نمی‌رویم. پیشنهاد برای واردات خودرو را برای خودتان نگه دارید.
🔹
اینکه می‌گویند خودروهای تولید داخل لگن است و مردم کشته می‌شوند، مغلطه است و ربطی ندارد، این اتفاقات صورت می‌گیرد چون بد یا در هوای ناشایست رانندگی می‌کنند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696910" target="_blank">📅 15:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696909">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4164a12584.mp4?token=f614HfBGA5KAhmvCj-_G9szWdVpIIUlZgJ2Ll1jllfK3FLF52Ey4jHxV9wehcJIjchgww9hlxGj9GzY5YShd1Dm7V_UxsANqTeHUGSBUvXvUaWBWKsMDCRGvZkdcTHIfAZrpC9amT2VYrNExos1zss1E79hSw1EGQEreHoLPu1dqVEf-DOqAMVjwEo_lNg3oovQmHaqWEaX-wbFMeYk3wk0A0r3NYlPkA-Gou0J9jkq_tg94362shSK5stLBs6od6eulYJr_qERnT9Kg8n7H89bfYUH_IAagsfpw3xM2EpaQNl9YNzHodq5V0N38heYz3uZa8IWydPrb43Nz5OUbvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4164a12584.mp4?token=f614HfBGA5KAhmvCj-_G9szWdVpIIUlZgJ2Ll1jllfK3FLF52Ey4jHxV9wehcJIjchgww9hlxGj9GzY5YShd1Dm7V_UxsANqTeHUGSBUvXvUaWBWKsMDCRGvZkdcTHIfAZrpC9amT2VYrNExos1zss1E79hSw1EGQEreHoLPu1dqVEf-DOqAMVjwEo_lNg3oovQmHaqWEaX-wbFMeYk3wk0A0r3NYlPkA-Gou0J9jkq_tg94362shSK5stLBs6od6eulYJr_qERnT9Kg8n7H89bfYUH_IAagsfpw3xM2EpaQNl9YNzHodq5V0N38heYz3uZa8IWydPrb43Nz5OUbvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر خونتون مورچه داره فقط کافیه این محلول رو درست کنید بریزی جاهایی که رد مورچه هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/696909" target="_blank">📅 15:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696906">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
قتل همسر ۷۰ ساله به‌دلیل سوءظن به گفت‌وگوی او با مردی دیگر!
🔹
مردی سالخورده صبح امروز با مراجعه به کلانتری مجیدیه به قتل همسرش اعتراف کرد. جسد این زن در خانه کشف شد و بررسی‌های اولیه نشان می‌دهد علت مرگ، خفگی بوده است.
🔹
متهم مدعی شده پس از مشاهده همسرش در حال گفت‌وگو با مردی دیگر، با او درگیر شده و باعث مرگش شده است. او برای ادامه تحقیقات به پلیس آگاهی منتقل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/696906" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696905">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/535068ce0a.mp4?token=d0lg6DYLHIVxVEX51qK7noxDv7Lm5RtVOt8AWBae0HZW4mqxvmdvJaSMZNR0npcyqg8eeHvI9YpuGwyuAj3hAn_eWKCVlcxcJ7nfWMjUeJcmnsDMxczO0c5h3J9earVx4wraD2_SeT9JQcJhSOgn33B5R5wgozKnjM-LrbP4t8dORc5-W7xnOCORs-XMO7x4P2jJCqwkRCMYeP1fBuuMkllkyYoXg_NLbbw3MXRIDZBCVdHz8qtzHwHKe4LQh9qwCdhyA9BiUNzYOnX21RLfGJ5_vPQjpP9UsYNVYVZbenH6k3gb4OgSLrbTpCH1eQ8Op-893mPdw-kCNlCBBOEubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/535068ce0a.mp4?token=d0lg6DYLHIVxVEX51qK7noxDv7Lm5RtVOt8AWBae0HZW4mqxvmdvJaSMZNR0npcyqg8eeHvI9YpuGwyuAj3hAn_eWKCVlcxcJ7nfWMjUeJcmnsDMxczO0c5h3J9earVx4wraD2_SeT9JQcJhSOgn33B5R5wgozKnjM-LrbP4t8dORc5-W7xnOCORs-XMO7x4P2jJCqwkRCMYeP1fBuuMkllkyYoXg_NLbbw3MXRIDZBCVdHz8qtzHwHKe4LQh9qwCdhyA9BiUNzYOnX21RLfGJ5_vPQjpP9UsYNVYVZbenH6k3gb4OgSLrbTpCH1eQ8Op-893mPdw-kCNlCBBOEubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مادری از ایل شاهسون در حال دامداری با کودک خردسال خود در دامنه سبزِ سبلان
🇮🇷
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/696905" target="_blank">📅 14:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: ما قصد داریم به عنوان بخشی از تلاش‌هایمان برای منزوی کردن اقتصادی ایران، تقریباً ۱ میلیارد دلار دارایی ارز دیجیتال را توقیف کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/696904" target="_blank">📅 14:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696903">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
محسن زنگنه، نماینده مجلس خبر از واگذاری بیشتر از ۱۱۰ هکتار از خاکِ ایران به افغانستان برای سرمایه گذاری افغانستانی‌ها داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/696903" target="_blank">📅 14:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696902">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Duq1IWBVZA2BHSt8JhwjB92Taxfr5naJvmyDACsNVJimweeZmFkHojL8nTn69CXg-2UhNPbAxgDtySc_4_bdmpWm6v1MLumXHZTO26OYlO79SVkhtV1K-WQIGn3SVrsVaW8Xju6AECCDoGPDg9eag98CNqBa1WEi-w82OXBlCB_U12gLkJG2qdOLVLylpo-eC8COzCW5b9cUYDpltSh0MPrkkT5IMrg9zL2Uru3hgGngenEFqZSmwCyzuXDKJpUcRZvTZ-CvhRMHo9tIwlcLbE--dihk3xsRrhNIj-I-eCpDrOmc7UEHFeKI5d0zxEfAHtZwF7OSbjjWIM2unK5dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین زمان مصرف ویتامین‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/696902" target="_blank">📅 14:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696901">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
معتقدم واردات خودرو باید در حد یک یا دو در هزار باشد؛ آن‌هم برای اینکه ببینیم چه ابتکاراتی در دنیای صنعت خودرو انجام دهیم.
🔹
خودروهایی داریم که با خودروهای خارجی قابلیت رقابت دارند مانند تیبا. البته از نظر قیمتی قابلیت رقابت دارند، اما از نظر فنی پیشرفت نکرده چون توجیه اقتصادی پیدا نکرده است.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696901" target="_blank">📅 14:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696900">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bovxcBvnX7mQ9S6ylNzRU1ikQmIT_wXbl_D1-qTDs3_GloH1IswayoqfSZoEgCA_JXiZYNVVgVgg7byU7Oonhb8rb5Vh78UA_u9-qf1_VF0kDRSR_GCOuFv2sd9u9ChC3piRVA_ljzFVnHRXsdWkf6E95xaP27ysb_qTTCPorcyTznubfB160Z49YXPoGU_iLErH36qyiFkvVO6dZM4uNLxBijuluNyp8SFiBQ9qtFZ_Su6u471AoLPytLw1HesWI_bFQkmkZ0wh7mvipfIWJTdbjiquG7YZ-5v_Hj4VoRsyvLXpcZpwtRoaqh5TVj9mGrM1d3m6q_bzNd5w0TWJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ماریا کورینا ماچادو(عضو اپوزیسیون ونزوئلا که پارسال جائزه نوبل بهش اهدا شد) به من گفت که در طول تاریخ جایزه نوبل صلح، هیچ‌کس به اندازه‌ی من شایستگی دریافت این جایزه را ندارد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696900" target="_blank">📅 14:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696899">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
طبق تصاویر منتشر شده، طی حمله یمن به فرودگاه بین‌المللی ریاض، دست‌کم ۳ هواپیما آسیب دیده‌اند
🔹
یک فروند، به طور کامل منهدم شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/696899" target="_blank">📅 14:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696898">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
۳ عدد ۳ رقمی ناخوشایند اقتصاد ایران
🔹
با وجود ثبات نسبی تورم نقطه‌به‌نقطه در چهار ماه اخیر در محدوده ۹۰ درصد، فشار تورمی بر سبد مصرفی خانوارها همچنان سنگین است.
🔹
تورم خوراکی‌ها برای هشتمین ماه متوالی از ۱۰۰ درصد عبور کرده و پنج ماه پیاپی بالاتر از ۱۲۰ درصد مانده است.
🔹
تورم کالاها نیز ششمین ماه متوالی بالای ۱۰۰ درصد و چهارمین ماه متوالی بالای ۱۲۰ درصد را ثبت کرده است.
🔹
نقطه اوج هم، تورم ۱۴۸ درصدی کالاهای بادوام در شهریورماه است؛ رقمی که این گروه را در صدر تورم کالاها و خدمات قرار داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/696898" target="_blank">📅 14:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696897">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIvaoPhpXW68UERlJGsqY1vMnhTIUHWgFJuwMkjO0LI_7ZUCVFVVh3NA2OQTlH68nMePkyVk7pdShWgPmmy57SO1XcD1rAqQgLHa4j4UH0xC38WhbrXTs_B3Z-YH24Asjds2aB9bKYPJ9jR-fBteQHloh-an7PSF_oNwxkoGwjwwCPFuWPPsDEEG41tT58t1Sotrx2nm2SpPqZvbBMpl5pNLmGjt-PRwTwDOcZRU6Che3vdXwCYj4DHqcZB7Ga1xts1Hn71zVG0KHnLyJtopAkrNOjOJPq1ZH5cHlJAoaSOi4E9qBCTamBMT1YNYGLmdwijsQjfb46jjZiLOLhLjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/696897" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696896">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlMbWX9TZvAPSN3JppbGpsh-mdpK1-4Xu0e0kMCE7gElG1Rt5n_fW9c09bUykDQBex-93XidPFCn8uVDd88RABJZ4GcMqGJfngKx0Jf42JIRgN3E8ruVeyBFWkx6aMlsQybX1Gn_b_BWd5gWxawxB_8tx0h5pu_tIJruuNuTQ0mWdCwRnLkGhGQxAy0cvm0hjHSAcXKU6dcml_t5-DDNxay9fXXl6NqSqd6qYyfp-h450bTn_C7oeUosd4pBlSaqAuiBEe8OFvV_9M7Z6l-vcYdrK5X6JPHo44rXTVpq13wrC6Qo90ydgdBiBlZ4_WwBNmIKguBkJzTU9vGxvTMtZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
واکنش بیرانوند به مدیرعامل تراکتور؛ دفاع از اعتبارم را از مسیر قانون پیگیری می‌کنم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696896" target="_blank">📅 14:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696895">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
امام جمعه تهران: پرچم داران فتنه زن، مردگی، بدبختی، ترامپ جنین خوار و نتانیاهوی پلید بودند
🔹
همین ترامپ قمارباز عضو جزیره اپستین و جنین خوار و کودک کش و دوست پلیدش نتانیاهوی پلید در جریان فتنه، پرچم به دست گرفته بودند و به زبان فارسی در آن فتنه پیام و شعار می دادند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696895" target="_blank">📅 14:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696894">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کم‌خوابی احتمال درگیری کارمندان با مدیران را افزایش می‌دهد
🔹
پژوهشی با مشارکت دانشگاه جانز هاپکینز نشان می‌دهد مشکلات خواب می‌تواند توانایی کارکنان در کنترل واکنش‌های خصمانه و جلوگیری از تعارض با مدیران را کاهش دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696894" target="_blank">📅 14:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696893">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a5da29f8.mp4?token=ODazQBiOAudg9RglGbzIO_0pKS8b3H0Ne0TWySpKYuv2vUresKacNdpNgocO1zVL4hbT76n7SxSeePnDT3sezGcDiP3VLNUbfQGGss7919gXLetFEtg-MOztmh1liB9hUEj8KuKdJ4EWmpeAuovVl5gADTNmR4nM2uLTMCnry4-EJFpv4L88_Drval3Ozk1jWzC6r2-3zs0qcD3_qiKTyTNmMmRTC9hCO_3vjePTxFaXWpeNihb1H3GchIDBOZ7_hwfsD3bQO4kTxCSkqtk0UzjSBGhcmmkIFAD7hK3zD_3jNB2xnifmqw6jESGNMk_fGjhXdWzhpwKezufsDdCLrrpUE63_plP0bVlcMm1ef5e62p_WW4tTclmqwGBcCngdkpqMbbNFUTw7VtDl6he2Vc7cplgZ1aISHrCtB8ALO1wnOPysN45yhOg8l3gPLK8f0bbZeq5QGGaspb4i-xXgLsb_R0dzeKyWhOlPpAaORLGkFYqSSP5lT79NpGjgDN3BeNZDOeEFqSwTF0nutVSk-ddLFTCmLwIN1V3iMFkxovXNRyrLqNbPWgUpbPpIIv8huJECjcZ4vCiz_R8KAhknpI5WmbUTBlzkiYKZ6jxoW2UKA4eFYIS2qmLzOk0FykU3Wanv3iNpyoPHxmxenM_WNS7K6mCrwz-Txcf8CegTflM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a5da29f8.mp4?token=ODazQBiOAudg9RglGbzIO_0pKS8b3H0Ne0TWySpKYuv2vUresKacNdpNgocO1zVL4hbT76n7SxSeePnDT3sezGcDiP3VLNUbfQGGss7919gXLetFEtg-MOztmh1liB9hUEj8KuKdJ4EWmpeAuovVl5gADTNmR4nM2uLTMCnry4-EJFpv4L88_Drval3Ozk1jWzC6r2-3zs0qcD3_qiKTyTNmMmRTC9hCO_3vjePTxFaXWpeNihb1H3GchIDBOZ7_hwfsD3bQO4kTxCSkqtk0UzjSBGhcmmkIFAD7hK3zD_3jNB2xnifmqw6jESGNMk_fGjhXdWzhpwKezufsDdCLrrpUE63_plP0bVlcMm1ef5e62p_WW4tTclmqwGBcCngdkpqMbbNFUTw7VtDl6he2Vc7cplgZ1aISHrCtB8ALO1wnOPysN45yhOg8l3gPLK8f0bbZeq5QGGaspb4i-xXgLsb_R0dzeKyWhOlPpAaORLGkFYqSSP5lT79NpGjgDN3BeNZDOeEFqSwTF0nutVSk-ddLFTCmLwIN1V3iMFkxovXNRyrLqNbPWgUpbPpIIv8huJECjcZ4vCiz_R8KAhknpI5WmbUTBlzkiYKZ6jxoW2UKA4eFYIS2qmLzOk0FykU3Wanv3iNpyoPHxmxenM_WNS7K6mCrwz-Txcf8CegTflM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت مصطفی میرسلیم از پشت‌پرده اختلافات رهبر شهید و میرحسین موسوی/ اختلافاتی که از اقتصاد آغاز شد و به سیاست رسید
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
با میرحسین موسوی رابطه‌ام خیلی صمیمانه نبود.
🔹
در شورای مرکزی حزب، دوستان مرا به عنوان نامزد نخست‌وزیری معرفی کردند. یکی از مخالفان میرحسین موسوی بود و دوستان ایشان هم بعد در مجلس مخالفت کردند.
🔹
مهندس موسوی معتقد بود کارهای اقتصادی باید در اختیار دولت باشد و ارایه امور اقتصادی کشور را کامل در دست گرفت.
🔹
اعتقاد مرحوم خامنه‌ای هم این بود که مردم نباید کنار گذاشته شوند. میرحسین موسوی کسانی را که به این موضوع اعتقاد نداشتند از دولت کنار گذاشت مانند آقای عسگر اولادی.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/696893" target="_blank">📅 14:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696891">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
سخنگوی سازمان غذا و دارو، از ورود محموله‌ جدید واکسن آنفلوانزای فرانسوی و روسی به کشور خبر داد
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/696891" target="_blank">📅 13:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696890">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c986b92f4.mp4?token=oApGeZalm_neZkKdUJKlMhYektkVY14Y8BP7kSqjdmAsYEY5E56eH-4kH0JD7ekbbb56lEb24-WFqezr6uCAKsZ3Dw4D_kMW57REO8N1F22ySP8O9Rvs2EYp6G9Az8RcLt8XhbUu6niu5MQuZUrW35kjlNYkOjrW98zpeGqQyfLbxHzOWfLRiE3U2O92pWmWthJaAjK80CK4BkZIsxh6JtgNx969-Vj5CuclOBj7S9cPxIYsDqHsrCsHMtx97QP3rJYEZ0APu_MrCZ0Dv_e6VP9co_AcEcCItLz-aFTFZ4OSA1b7_NoFb7CK03XPjXEBccse1LbuEMF0ycV8UGWumoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c986b92f4.mp4?token=oApGeZalm_neZkKdUJKlMhYektkVY14Y8BP7kSqjdmAsYEY5E56eH-4kH0JD7ekbbb56lEb24-WFqezr6uCAKsZ3Dw4D_kMW57REO8N1F22ySP8O9Rvs2EYp6G9Az8RcLt8XhbUu6niu5MQuZUrW35kjlNYkOjrW98zpeGqQyfLbxHzOWfLRiE3U2O92pWmWthJaAjK80CK4BkZIsxh6JtgNx969-Vj5CuclOBj7S9cPxIYsDqHsrCsHMtx97QP3rJYEZ0APu_MrCZ0Dv_e6VP9co_AcEcCItLz-aFTFZ4OSA1b7_NoFb7CK03XPjXEBccse1LbuEMF0ycV8UGWumoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برگ بو؛ ادویه‌ای خوش‌عطر با خواصی فراتر از طعم‌دهندگی
🤩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/696890" target="_blank">📅 13:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696889">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6IyJuQMyc0bhrXA7rksKgMcM999uZcLEZVaFzieRSV9RW131fmAQgCn6PE8BQ0WgoaAONU6b650xOsBG1q0ODI5NDvC1OmJyU-vZv1dcJRJp1GbsaB6cELhsBilhd_nmEtT9uaMdqoy6W9fS8LLPtllToQzigNoNVwfpCeXIPR4Xd9KwEtgTo1cHuknxw6BEbXybSvgqJlJg4f66dWQqc7BsudD55aiE-GyZE11tnvbC2qnbh_-1T7qMEmzv9zvoS6R3QlDFiiiePTkdNhU84EHGtmzvqEH82qs2sNsF_5FDdjpTFoCpNV_pJ51zpAtd4pPRFUboE_hvpR5bM5YOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از پایتخت تا ساحل نیلگون خلیج فارس؛ عملیات گسترده بهسازی شریان جاده‌ای تهران - بندرعباس
🔹
کریدور تهران - بندر امام(ره) یکی از شریان‌های مهم جاده‌ای کشور است که عملیات بهسازی و ارتقاء ایمنی در پهنه ۳۵۶ کیلومتر در مقاطع مختلفی از آن، هم‌اکنون با پیشرفت بیش از ۷۰ درصدی در حال اجرا است.
🔹
سازمان راهداری و حمل‌ونقل جاده‌ای در راستای اجرای سیاست‌های کلان خود به‌منظور ارتقاء ایمنی، کاهش تصادفات و تسهیل تردد کاربران جاده‌ای و ناوگان سنگین، اجرای پروژه‌های مستمر بهسازی، لکه‌گیری، روکش آسفالت و ایمن‌سازی را در طول این کریدور راهبردی با جدیت در دستور کار قرار داده تا ترددی روان و ایمن در این شریان حیاتی را بیش از پیش تأمین کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/696889" target="_blank">📅 13:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
هشدار نفتی بزرگ؛ قیمت هر بشکه نفت ممکن است به ۲۰۰ دلار برسد!
اویل‌پرس:
🔹
راسل هاردی، مدیر عامل شرکت ویتول، هشدار داده که اختلال در انتقال نفت از تنگه هرمز و کمبود نفتکش‌ها می‌تواند بازار جهانی انرژی را با شوکی بی‌سابقه روبه‌رو کند.
🔹
به گفته هاردی که یکی از بزرگترین تاجران نفت است، اگر انتقال نفت میان کشتی‌ها در دریای عمان متوقف شود، سناریوی نفت ۲۰۰ دلاری جدی خواهد شد. هشداری که بار دیگر نگاه‌ها را به تنگه هرمز و آینده قیمت انرژی جهان دوخته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696888" target="_blank">📅 13:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
پزشکیان در نشست سران کشورهای مشترک‌المنافع: منافع مشترک ما، نه در رقابت میان مسیرها بلکه در اتصال مسیرهاست/ امروز بیش از هر زمان دیگری نیازمند چندجانبه‌گرایی واقعی در منطقه هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696887" target="_blank">📅 13:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696886">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM76xmNvDjvda3oDjb93vM_zldC2MTuzUj7VgQhwZa_2YvaWUqdwoex5ZbJL_np9IBNiSw_7eOKr8A9BwmT7zPkeMxB0cb-Z1jTl0i4Lh2VCIGybzqK7MGNaWZiEt3e_TVGkCzP6sOZQZQqFZoiTfPBARptk5SwcbxyPOPCWvqEtaWXgGqKO5r_BNKKnwwKLJZN6Bzk0JLzVSu1t0jYeCRzfWAZh-84g2lNjw7iSMvGK6rSl-DOlGsZ-n34sEw2RmPPENKOKLmcD25hJo45WiTCB_rWi9FBuWOrHrqRVFpCeBJ1m_5eJjsCnqb3hKbNPI0ezit3ZnD9hVlJslVeF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این مرخصی‌ها حق قانونی شماست
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/696886" target="_blank">📅 13:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696885">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyQQ_iMfV02YaF4_0rZHREguGohx3IiOiKzXTor-cP00sBsggKfwmd2KVYeInAi4xQcArkK2PH7syjAi7nA58X0jcY_033pg9P_qMVbHuz0STZt_E2QzSnfORwS_Z5LDySwA8NavvLVupwDHu_whlqwe-NqgAkmbvaXO1kimCfFUpsM5QLoxDixJ7emdhRVjgdm4pjO9uqN0Ej_icfDvmu7ksatBAyyPa45x8oP_QyiSfJbxx0QXc1ZkLNdptxm8hsf3bDEwKkg_WBSFIz17JuopTpQlTvX9FZ1Do5jofMsPvq4IT6n1PthuqGpjm6woaN4w6lO31tJscPFWGh5I_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساختمانی در ایتالیا در ۵ طبقه با ۱۵۰ درخت که حس زندگی در خانه‌ای روی درخت را زنده می‌کند
😍
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/696885" target="_blank">📅 13:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696884">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سفارت‌‌های آمریکا در اردن و امارات نسبت به احتمال تشدید سریع تنش‌ها و لغو پروازها هشدار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/696884" target="_blank">📅 13:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696883">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
پیش‌بینی‌های داغ از آینده بازار طلا
🔹
جی‌پی مورگان قیمت هر اونس طلا را در سال ۲۰۲۷ حدود ۶٬۳۰۰ دلار پیش‌بینی کرده است.
🔹
گلدمن ساکس محدوده ۵٬۴۰۰ تا ۵٬۶۰۰ دلار، یو‌بی‌اس ۳٬۸۵۰ تا ۵٬۲۰۰ دلار و مورگان استنلی ۵٬۰۰۰ دلار را برآورد کرده‌اند.
🔹
همچنین، متالز فوکِس رقم ۵٬۳۳۰ دلار و کنفرانس انجمن بازار شمش لندن (LBMA) میانگی۵٬۱۱۰ دلار را مطرح کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/696883" target="_blank">📅 13:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff041c3bcb.mp4?token=VdMultZtNoLItJ3QphdhtOMQUAnME3gpJB01LDpQikVsIn5USShBB8Z7JIXzYxeWYkzVGLBSgCFwlK4mt0rneNTjkfSBWxYSQ6TNnFVa-jYydVnNu2pFKma9XG8X39Jadn46Nos-_vPpfo1gaJQeSTatg93aSPPFyKrWnDHMQ0-56B2sljCVkpAQ5820oKrJskrh90RIjRlDQsfvtkzo5sWd5ZjcyXq7Q4yxdzMsRvO5pNSCs6VV2FLiFarbEdDsadBAHtKO5N3px38yEZR-d7tG6H9dep-Zp5DDppE4k5WX5j2ofUBIZ2HjfHYB7oW8kEu9LCgfgz5ainMOkjDr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff041c3bcb.mp4?token=VdMultZtNoLItJ3QphdhtOMQUAnME3gpJB01LDpQikVsIn5USShBB8Z7JIXzYxeWYkzVGLBSgCFwlK4mt0rneNTjkfSBWxYSQ6TNnFVa-jYydVnNu2pFKma9XG8X39Jadn46Nos-_vPpfo1gaJQeSTatg93aSPPFyKrWnDHMQ0-56B2sljCVkpAQ5820oKrJskrh90RIjRlDQsfvtkzo5sWd5ZjcyXq7Q4yxdzMsRvO5pNSCs6VV2FLiFarbEdDsadBAHtKO5N3px38yEZR-d7tG6H9dep-Zp5DDppE4k5WX5j2ofUBIZ2HjfHYB7oW8kEu9LCgfgz5ainMOkjDr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی «توزیع ارز» جای «تولید ارز» را گرفت
رفع محدودیت‌های بازگشت ارز؛ بازکردن گره‌هایی که خودمان زدیم!
🔹
با آقای احمدرضا فرشچیان، رئیس کمیسیون واردات اتاق بازرگانی ایران،
سیاست‌های ارزی کشور در سال‌های گذشته و آثار آن بر تجارت را بررسی کردیم.
تماشای نسخه کامل برنامه در آپارات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/696882" target="_blank">📅 13:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696879">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2124c18e8.mp4?token=LV12hz3YTT1O4WTV7VBbuz081OMnpnKr5mgkUedjdbcPHj0xsH1fKdUm9CFnvrEpaPliENDAe30YY76pHHdezHrKM5xBPoawvwVGlh0fMaLAAFZPG3xW5lHFmpvYg6ozLq-a8GRTxlBsqmCmns1_RWCUnE-04IsYHaFKDAAsaGDryvjFgP5fugeLicwqfU7uuhdyL3FNsotGtUcIjop7u5FjvdFpZsYysFGhyqiCSKepN9X7SB0hL7txa-_6Tc8S-s7MJ92Aw8uP97uDaEFDfFtFWumJvHMfFM0nUEP31wUHHqIbsQX2WVdJE4L8xFU2g2vxulRxKetwZkIkjUpUnjzvZQ7wPLwsGk8eAVmcPJ-Z1rb_wRuXCrRWF0LAiSE7t8EoZIm-WHZ_Na0ZazRaVDfA4CXTiGTU5NHXdAMFsmHHmNm3BUgFOFzb6nXH6Kex8naFp7DnNuXWPqgs_sCbbcPaw_EEEMzax8vvt6SbOHzfDRWqwA4HAACA7Z8UUbiyob_k5rbISkefBSo1Rmn4m-vSiFZRVfK9tWj8h2J8-iYsqXD48Yx1cARrRop9-pnC-W3Qvd_b6-tlKITKes1jw1I8Y8B-vPUtsoCdDbtupWNoddlww0IPllV8hwwdFQRQyem0NVoaYUbQCEExDPB3GP_OPc3G1duWqUegI7EKjWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2124c18e8.mp4?token=LV12hz3YTT1O4WTV7VBbuz081OMnpnKr5mgkUedjdbcPHj0xsH1fKdUm9CFnvrEpaPliENDAe30YY76pHHdezHrKM5xBPoawvwVGlh0fMaLAAFZPG3xW5lHFmpvYg6ozLq-a8GRTxlBsqmCmns1_RWCUnE-04IsYHaFKDAAsaGDryvjFgP5fugeLicwqfU7uuhdyL3FNsotGtUcIjop7u5FjvdFpZsYysFGhyqiCSKepN9X7SB0hL7txa-_6Tc8S-s7MJ92Aw8uP97uDaEFDfFtFWumJvHMfFM0nUEP31wUHHqIbsQX2WVdJE4L8xFU2g2vxulRxKetwZkIkjUpUnjzvZQ7wPLwsGk8eAVmcPJ-Z1rb_wRuXCrRWF0LAiSE7t8EoZIm-WHZ_Na0ZazRaVDfA4CXTiGTU5NHXdAMFsmHHmNm3BUgFOFzb6nXH6Kex8naFp7DnNuXWPqgs_sCbbcPaw_EEEMzax8vvt6SbOHzfDRWqwA4HAACA7Z8UUbiyob_k5rbISkefBSo1Rmn4m-vSiFZRVfK9tWj8h2J8-iYsqXD48Yx1cARrRop9-pnC-W3Qvd_b6-tlKITKes1jw1I8Y8B-vPUtsoCdDbtupWNoddlww0IPllV8hwwdFQRQyem0NVoaYUbQCEExDPB3GP_OPc3G1duWqUegI7EKjWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدهای نوشته شده پشت کامیون‌ها نشانه چیست و چه معنایی دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696879" target="_blank">📅 13:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696878">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f315cb4b.mp4?token=rrOhjiiVlZDgqY1kPYUtRVFnRF8bIrI_Ws-P7xYnULXLYsUngpvvk9lk3GXbbpO1O1wWQOcCpLfjAtdaAh0aHJ7yzbp11ZfqLJ028sNdzb9hmBRfaI0GKdG6dk5lWCp41hveDuDj8zg5m7fyk1-9DgS3GVgbcMTF9nJsPjP7lmPrCaVK3OqAdf2Jhgankd8gcH5O6um6WoYMEsaAGyCfDUNBB9hnI5zbqMmU8ykFKXcqLjY7xFI_WlBNbfyM5q_5-OF8YpAVXlLNsXVAspHgjUlWDFl2mzYSVNOy08VrJ4db0mEZSRmRMF3Y7eF9KsjWrqAThB2vUEL_GB2jrGnjkzIb1AIrGBCRCXc_lA2GgKQjlk2-DEVx_BZrHDnRqbVPdbv0bdEMxJ1YSz-hZaZ2oTOqLYceQRcXZ5oi5j_94ohDdCayZ03D0nE7Dex1hU7BrjWfU-S9SostuXAxpEds5Rl2gtsYRDUBOs_pb1fqVewROFCMwUs0XNVb2mVXmEZ0GM5Mn7VUG4gqHyQ3DUwIJpzI4wMNpVxdy2el_3h1rV7oMNU7ohaBVq6oqP5qcgiSV0JvMIGZGNz_w6CviYLWSqqyyFmOn7HHKmkczoJzLQkwTXnizDQRjmtGQW1JKpZhVHZ_0W6V_vvK5-zkJOLoySgwEZSFv3s9m002y88TMXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f315cb4b.mp4?token=rrOhjiiVlZDgqY1kPYUtRVFnRF8bIrI_Ws-P7xYnULXLYsUngpvvk9lk3GXbbpO1O1wWQOcCpLfjAtdaAh0aHJ7yzbp11ZfqLJ028sNdzb9hmBRfaI0GKdG6dk5lWCp41hveDuDj8zg5m7fyk1-9DgS3GVgbcMTF9nJsPjP7lmPrCaVK3OqAdf2Jhgankd8gcH5O6um6WoYMEsaAGyCfDUNBB9hnI5zbqMmU8ykFKXcqLjY7xFI_WlBNbfyM5q_5-OF8YpAVXlLNsXVAspHgjUlWDFl2mzYSVNOy08VrJ4db0mEZSRmRMF3Y7eF9KsjWrqAThB2vUEL_GB2jrGnjkzIb1AIrGBCRCXc_lA2GgKQjlk2-DEVx_BZrHDnRqbVPdbv0bdEMxJ1YSz-hZaZ2oTOqLYceQRcXZ5oi5j_94ohDdCayZ03D0nE7Dex1hU7BrjWfU-S9SostuXAxpEds5Rl2gtsYRDUBOs_pb1fqVewROFCMwUs0XNVb2mVXmEZ0GM5Mn7VUG4gqHyQ3DUwIJpzI4wMNpVxdy2el_3h1rV7oMNU7ohaBVq6oqP5qcgiSV0JvMIGZGNz_w6CviYLWSqqyyFmOn7HHKmkczoJzLQkwTXnizDQRjmtGQW1JKpZhVHZ_0W6V_vvK5-zkJOLoySgwEZSFv3s9m002y88TMXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: شأن من در حدی بود که به عنوان نامزد نخست‌وزیری مطرح بودم!
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
دوران وزارت کشور آقای ناطق نوری بود که از دفتر آقای خامنه‌ای که آن زمان رییس‌جمهور بودند با من تماس گرفته شد و با پیشنهاد پذیرش مسئولیت سرپرستی نهاد ریاست‌جمهوری مواجه شدم.
🔹
با آقای خامنه‌ای ملاقاتی داشتم و گفتند برخی از دفتر من راضی نیستند و می‌خواهم در اینجا تحولاتی ایجاد شود. ایشان به خاطر من برای اولین بار نهاد ریاست‌جمهوری را تشکیل داد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/696878" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696877">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
نشت عفونت ناشناخته از آزمایشگاه طاعون روسیه/ ۲۰۰ نفر قرنطینه شدند
🔹
یک کارمند ۲۸ ساله آزمایشگاه ضدطاعون روسیه پس از شکستن تصادفی لوله آزمایش حاوی نمونه زیستی، به ذات‌الریه ناشناخته مبتلا شده و جان باخته است. حدود ۲۰۰ نفر قرنطینه شده‌اند و احتمال طاعون ریوی…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/696877" target="_blank">📅 13:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696876">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پاکستان: خبر مشارکت جنگنده‌های پاکستانی در حمله به یمن جعلی و ساختگی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/696876" target="_blank">📅 13:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696875">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سفارت‌‌های آمریکا در اردن و امارات نسبت به احتمال تشدید سریع تنش‌ها و لغو پروازها هشدار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/696875" target="_blank">📅 13:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696874">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#ساخت‌ایران
🇮🇷
۱۷‌ مهر
بمناسبت‌ هجدهمین‌ سالگرد‌
افتتاح‌ بـــرج‌ میـــلاد‌ تـــهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/696874" target="_blank">📅 13:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696870">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1eAYD0T8a4NhVEZTwEusxEYI-SqEOf_NKPEg38okMbHeV2-u5tcJWM1M-ZNKnNcAscS-mdTiuV3mnsvX7wo8Kjad0r263gA2Kx5sU2hHP9QOWaxrovT4NUJsr1wRgZvbDpbFog0V0PLB5pudk63rUpYonjv4745lu_-N0-WsTRIaOMv_fUGQ9X3-9rvAlGRzRHoNu_94664VVIVFOrPgx5p3qrtMFfYEbq2eWYE4DA-nq1acQ6DHSKTdvV2MH9PXeJocSYfvZMN89R3zFV0aqvZhSskfUTXXQ19UY1dSLLZQgeRNhF65jSptR9ZYB4Nryy3mJM9MoqcROYiTXh_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLRtSxSRsgJ_a-BFJPQqEERGF_83H-MNHulDztPcrWIty2bUQLyjFYm535gKdx8Gn-P4Wt-Q6nDbeKA78MsHlvtjC_Utva-YYq2_1p3zBAGkxUdBkfua61j8Cl7rVaeEqBTpc5t8yznUr23XhAoLLV8XBXH5RAyy_LqNB6tqe1fMI9nodZ-qlxcZRb27oONbwt7-9vI--um1vYbgXAyyHr6qH5xZJ_zFUGnHPwujOPmyKpIUxW-n7xxklMDJnjxcdxQ0TpG6otr3S8FsYItaouhWX27vbQi4HTfeD6i8YJ_KSr1zwLH3tgPh8-9iiK_XLuoKkIRL5XfEgU52I_Hn7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUh79DAxdgoAsA06pFK_wm9ih-mme5RX_JC4f31hSgIQaMDCMeKNWG10yUTR_35RO5-PrcsJNlPLBxP_gw3cTDhY2YUC_0eLkHKVtNVwfm_-tNn08TDjKSlrv3ZM5rw3oBTqTVS4g6oVgmmJvU4MMoIG4BywHBOg52AU6YJVaSLkndFZ3zTFRzbfutT-iBtfz7ZzEg619s2EiTiQLUwSyqMbcfaaqCZ_WCLYVv8prvCej4RFUxhdOWYK2xTMFKaQztiPC3PVC2RLvrYyw0Gq4PcQCtwtybJEV4ggd1XpzNXSagCoLyyOC-dqw_P9FAsCjAJWepBj6IukrMlo5AYQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqEulvXVUrhq69EKiwW0J7c1Ut3PWYAHdPTY8mms9nf_ei9CC5d79STjMTieAUOF8FJGiKHtcXGKgkYkoHbeIgOBWWUm5FS06XlhHIhetMdtPgzSsSyyM20VgL1UlnACPiXp3VjqRCmeh-fD7I7tu80bp-yzzMYs7PyViiJY8a3m9QgQbd-QuWg8tbVx6c-9O7Bsm4xAdPdCjoms341ree11ky6B6Py-F9r-YhaLDl2_52M_vbqMgEJWxMgiElUX9p5Wu_smxPpaFAJTXtN1tEsT0YjSptsOFyTvGXbNYmjSbIeN6TyjqpYxR-YV3iivWdHEMUHusN07_9vBi7Pqnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تویوتا FJ کروزر جدید؛ انگار یک ماشین کارتونی از دنیای انیمیشن‌ها وارد خیابان شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696870" target="_blank">📅 12:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696868">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86d19c713.mp4?token=VUHAGJNL-m_UmFIQ87dnhITeqdUiJFJsv-i__RDC0AevmorC0Ylm98ZL60BJ-8kilXzGQzxdT2KTNU8o_uRDSLLCF8SgkoVYJvOnw2_NVKhAEDBINWUMhOgNqH9lsJeku6jwBMm47-udiI-_S9ebOA1y9Swflfdz35RjGN-LbI6ArPWnWYNrF4hPJ0ydnx7MxSkVIjNOZqjZpM56Rug0LGG0rlsjVsVC_x6fdnTy11GgYiHBW6v0iIGaKIK9FzRLHXPLiTx3W95LV8onnQEin9Ur009J4Q1XTMJwj5sDFT8Km4o2NOwtZZYmgF-DqsV7c6C5ZCBL962lC_KARs9WwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86d19c713.mp4?token=VUHAGJNL-m_UmFIQ87dnhITeqdUiJFJsv-i__RDC0AevmorC0Ylm98ZL60BJ-8kilXzGQzxdT2KTNU8o_uRDSLLCF8SgkoVYJvOnw2_NVKhAEDBINWUMhOgNqH9lsJeku6jwBMm47-udiI-_S9ebOA1y9Swflfdz35RjGN-LbI6ArPWnWYNrF4hPJ0ydnx7MxSkVIjNOZqjZpM56Rug0LGG0rlsjVsVC_x6fdnTy11GgYiHBW6v0iIGaKIK9FzRLHXPLiTx3W95LV8onnQEin9Ur009J4Q1XTMJwj5sDFT8Km4o2NOwtZZYmgF-DqsV7c6C5ZCBL962lC_KARs9WwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حریق گسترده و تلخ در مجتمع تفریحی تجاری «الیت سنتر» تنکابن
🔹
مجتمع تفریحی و تجاری «الیت سنتر» واقع در ترنجلا، تنکابن و در مجاورت جنگل گلستان، طعمه حریق شد و متأسفانه در آتش سوخت. این حادثه با اتصالی برق در یکی از یخچال‌های بخش هایپرمارکت آغاز شد
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/696868" target="_blank">📅 12:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696867">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ecf63feb.mp4?token=OD-NrOeeBnWiGgcP0PzBDUdk6dkw6oKbHsMNT3XtOG7U8IeBpcJ0K1EM1SYrHx_bFQ1OzPXK2hoSp6oypMGzN0a2cvuqlstrKysmgtTG5tbEFE4lWo3sjXARscmLyoAQm3gVENJEjCZgrqVPEnRj3brUE8xE1KDrN8t21z11NEn05odNKsVtI7Ntzbqg35RGzzM7encUep545gqr-Aj1n81ZX4OgzIZTAvBSp3MBxrNqnh4FUQbJu6_Z63iXx4NluvqOgBjGoHJ5K0oAoppl5LpWkLPRm1guzPYxmgbwuqf65sSeG6E3cSzVrSpU3BgkXDHEC-ScYI_ER5bdW6O6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ecf63feb.mp4?token=OD-NrOeeBnWiGgcP0PzBDUdk6dkw6oKbHsMNT3XtOG7U8IeBpcJ0K1EM1SYrHx_bFQ1OzPXK2hoSp6oypMGzN0a2cvuqlstrKysmgtTG5tbEFE4lWo3sjXARscmLyoAQm3gVENJEjCZgrqVPEnRj3brUE8xE1KDrN8t21z11NEn05odNKsVtI7Ntzbqg35RGzzM7encUep545gqr-Aj1n81ZX4OgzIZTAvBSp3MBxrNqnh4FUQbJu6_Z63iXx4NluvqOgBjGoHJ5K0oAoppl5LpWkLPRm1guzPYxmgbwuqf65sSeG6E3cSzVrSpU3BgkXDHEC-ScYI_ER5bdW6O6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ منوچهر متکی به اراجیف نماینده آلمان در نشست اتحادیه بین‌المجالس جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696867" target="_blank">📅 12:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696866">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
یک منبع نظامی آمریکایی به الحدث: پیشنهاداتی به ترامپ ارائه شده است مبنی بر اینکه به توانمندی‌های نظامی ایران در امتداد سواحل، در عمق ۵۰ تا ۸۰ کیلومتر، حمله شود
🔹
این اقدام، آسیب جدی به توانایی ایران در تولید انبوه موشک‌ها و پهپادها یا پرتاب آن‌ها وارد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/696866" target="_blank">📅 12:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696865">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/830f231c18.mp4?token=dQsqtHnHAPvxLQXwU8iykqR1JLE-v9lj_l4E9f2SSj0YfN96-oulCDEGfKpg40ZkgaspdJw-A9jj60q3jyv-DQAeNkH1h4u6xD4IYjs6eC4xScT4lVbML2r9SB8qQVt6_Rejy4QudnCjhUV5lqqBbyXIzGulVNGvLvi1VjPWiSpvUBTsR7NJuQsKVckILdtWBZzj6-PiWuNB_o6Tr0X1FilhOZBdI4KMUA5eXtHRFZo76dl1KePASaR1jZAH5BLvJYOu8aiTT-Ba345adS0qSeb5Fx2jdZIybdhKTly29n_J3Kr-vfyh-PtM1V1o74K3EXZf5XPazPF5bD4wpM_7bmKr2xj5Y0WlYTOwSb4dT0YaQUT-vF_DSH_St0pqd6ZuBf77Wmf8Qyj15zu8ISh5OykSw1IF82DbJSh9uvaLopzu5TuOjZbpxfa1XApiDm7FybSGYWG0hyZUGGtNndnLpcwymrUdjRfZtVGIiBMWcRh-NaKIdKC-SMjEApMPfU_Gn-f-EmrGUhRZMM38WFYCMdJLAhY7Irq9A7YuygXatd9L_4uIUh770rCuNJz_-RaYG2e7k_IvJtA_n3YuXqODKWEJRh61OcnBjz9WuGFy_W6RVJ-y9WC20e99GivdMUgfexUevh1ZxnUcqquJFws_tYOqrkvKHXMvvqOtp6c7N5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/830f231c18.mp4?token=dQsqtHnHAPvxLQXwU8iykqR1JLE-v9lj_l4E9f2SSj0YfN96-oulCDEGfKpg40ZkgaspdJw-A9jj60q3jyv-DQAeNkH1h4u6xD4IYjs6eC4xScT4lVbML2r9SB8qQVt6_Rejy4QudnCjhUV5lqqBbyXIzGulVNGvLvi1VjPWiSpvUBTsR7NJuQsKVckILdtWBZzj6-PiWuNB_o6Tr0X1FilhOZBdI4KMUA5eXtHRFZo76dl1KePASaR1jZAH5BLvJYOu8aiTT-Ba345adS0qSeb5Fx2jdZIybdhKTly29n_J3Kr-vfyh-PtM1V1o74K3EXZf5XPazPF5bD4wpM_7bmKr2xj5Y0WlYTOwSb4dT0YaQUT-vF_DSH_St0pqd6ZuBf77Wmf8Qyj15zu8ISh5OykSw1IF82DbJSh9uvaLopzu5TuOjZbpxfa1XApiDm7FybSGYWG0hyZUGGtNndnLpcwymrUdjRfZtVGIiBMWcRh-NaKIdKC-SMjEApMPfU_Gn-f-EmrGUhRZMM38WFYCMdJLAhY7Irq9A7YuygXatd9L_4uIUh770rCuNJz_-RaYG2e7k_IvJtA_n3YuXqODKWEJRh61OcnBjz9WuGFy_W6RVJ-y9WC20e99GivdMUgfexUevh1ZxnUcqquJFws_tYOqrkvKHXMvvqOtp6c7N5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار جبههٔ مقاومت در غزه: عملیات ۷ اکتبر واکنشی به یک قرن کشتار، اشغالگری و نادیده‌گرفتن حقوق فلسطینیان بود/ نسل جوان فلسطین پرچم مبارزه را تنها زمانی زمین می‌گذارد که آن بر فراز قدس برافراشته باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696865" target="_blank">📅 12:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696864">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جنون آنی یک داماد، چهار قربانی گرفت!
🔹
وقتی خشم و جنون آنی باعث می‌شه که چهار نفر از اعضای یک خانواده در آتش بسوزن!
🔹
روایت همسایه‌ها از به آتش کشیدن خانه مادرزن توسط داماد را ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/696864" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696863">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پزشکیان در نشست سران کشورهای مشترک‌المنافع: منافع مشترک ما، نه در رقابت میان مسیرها بلکه در اتصال مسیرهاست/ امروز بیش از هر زمان دیگری نیازمند چندجانبه‌گرایی واقعی در منطقه هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696863" target="_blank">📅 12:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696862">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU5xYyF8-ICWttmCiNZ4KHQW-CKbYsQdnaZ5XeBUqpDllDA2HtOX70CIMvBi-EBMkgGRn4YGgKsqoMhL_7yd2WKKAV_4DYSe-fwn6qtoEmVNj9hQ6O2rr6wch6kqF82A-b4pJyjBn9j6i0s4kSJeakkR4QssXixHoSDbskbTIHLdHBIhzvIK_Zo2WA-2smz973JpDl3DllGLgIAtL53dPQNND5IyRATJ4XMtf92jrHqxzpINQxjkWBklSMfW0OLa5Mp5Da5obWRnrxWJONG21CO1XWOTe4N_TJ66BFtfdESAIMuQA14DCgOE8pwfCpZSGitZYnLiTBLsncrK75BF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ بیماری که همیشه باهم اشتباه گرفته میشن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696862" target="_blank">📅 12:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696861">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bdb68dc1.mp4?token=I14-Y_RUN2R8RCHE-ILHQIpYIJx0OGDNJu6ZmGg6GGvSM_fbAkIV4TFoLBMnjOeZPV6PjbTgFW7b37MMhXhaElZn4Kkl1pnAV1w6mg4OavAD9my67PN9t1YErOmzt3Sr3c-Itl5FB9tBDRTCZtI-YX1ekjTe8uRBuL6OP53-UA4UnXVh7KGbVVdGpOdLyOR-ZKbrabUDXibjiXva4woXV7zmTaxGWSTGXxfoiulyuxpqqE9oQcjP92ykaCTIy-Oc9ypAYtsUHynhufSHONFPGVZePfijs46DJZJNqh4oHj7K-ZhbTAie048zWftYBb1rM0xE4xqE-NP6QSoNBlwm2au3ejuV2EMJgtTFcJGWbIwzeXWkFcW0HNOvsi7HMotUBU08LKhSiq8OGg7DDpaKGFXuE0zEZs-F79iwf8mHX74ScFUKvYfzH-WVoeVBQuwsXaOwYsj19nbUPWFjFrha7JAeerCg6lWiNFmg1BYPTR4U5nNMObWAjjpuPmlN1shkd8bcJu-deKmCoYQcs71ZuK9hjVtvLRW-z1333ZG4PL7g9uS0rIHtbGnhdC2l6LSv-i-mDtMIGtJJnkTqdbG8p86PnZWMAUn2YijydbW0tZPBj-LR8LucTEm5iYcJ2208Nw0kLKtoNpAZK2fRIRoZvWxAn24Yv7OFXxlXouplLKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bdb68dc1.mp4?token=I14-Y_RUN2R8RCHE-ILHQIpYIJx0OGDNJu6ZmGg6GGvSM_fbAkIV4TFoLBMnjOeZPV6PjbTgFW7b37MMhXhaElZn4Kkl1pnAV1w6mg4OavAD9my67PN9t1YErOmzt3Sr3c-Itl5FB9tBDRTCZtI-YX1ekjTe8uRBuL6OP53-UA4UnXVh7KGbVVdGpOdLyOR-ZKbrabUDXibjiXva4woXV7zmTaxGWSTGXxfoiulyuxpqqE9oQcjP92ykaCTIy-Oc9ypAYtsUHynhufSHONFPGVZePfijs46DJZJNqh4oHj7K-ZhbTAie048zWftYBb1rM0xE4xqE-NP6QSoNBlwm2au3ejuV2EMJgtTFcJGWbIwzeXWkFcW0HNOvsi7HMotUBU08LKhSiq8OGg7DDpaKGFXuE0zEZs-F79iwf8mHX74ScFUKvYfzH-WVoeVBQuwsXaOwYsj19nbUPWFjFrha7JAeerCg6lWiNFmg1BYPTR4U5nNMObWAjjpuPmlN1shkd8bcJu-deKmCoYQcs71ZuK9hjVtvLRW-z1333ZG4PL7g9uS0rIHtbGnhdC2l6LSv-i-mDtMIGtJJnkTqdbG8p86PnZWMAUn2YijydbW0tZPBj-LR8LucTEm5iYcJ2208Nw0kLKtoNpAZK2fRIRoZvWxAn24Yv7OFXxlXouplLKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عربستان برای جبران شکست‌های خود، به دروغ‌های رسانه‌ای رو آورد
سلطان سدح، خبرنگار جبههٔ مقاومت در یمن:
🔹
عربستان برای جبران شکست‌های خود در برابر انصارالله، به‌دنبال رسیدن به پیروزی در رسانه‌هاست.
🔹
العربیه و الجزیره به‌طور گسترده دروغ‌های عربستان را پوشش می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/696861" target="_blank">📅 12:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696860">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f9cfef3f.mp4?token=YvhebsZYXgoqLtNy6r0ZL0eTA3js1AgCQ1unFsaQpB80YP4m-692MzFKMC8e0ApQ7V1GQ3NigA1kqNsImMj6f9AkIsAFKpOk_py30dgzy_A19kAt46UpY3lLRcqhPsN1BpXU8Fe-GIwvtYJ0Jh4APEDO9IvCEvjETAuFPaqu9OmuupnEDolLBNdkidu5oPw2xz0nxE5dRPG7nAnGoRELLyAYFgRIIaWRQ39lEC8pa2NPHTA_o_NmNt6kjD8FWVuF7AlakxsGwXzkJIMb1QE8BA-BNUyaXa_jFrl_gybLHT0A490wq7Zga9CG-sDocaaPczZ1SqgbWSInQcqdP5_G8T0WchxMa7Jxum4hAQH7L0nW1GTHOGArgU1hiq0lBIN1gW7DfSXkjtLpqLZGhR8gMkpi8_V-PPhrTJ4GL890Cec0G3F8KvPlxp_6SiFcn-OKampYmkw_nxc5CKPNz4dXctDTb07IlP0VHBbmhI9c4xUKOVavx-jJe5XWmX-XNghOe881Lj8K0GPn7rrU92bxOI4f5Rnci5wU8bkrekyl86YoV98gdUFx87aa6aC98wxYnboC5kxvI3q4Yu0c-ADXXeD7A7IaHqtCgXSiPQjzK9Je27V8ZiBTm6f8OtY12mZwNIy0dm6RhQwNcn6STrvKb-mJrEskgGoEIdDT6DNFFlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f9cfef3f.mp4?token=YvhebsZYXgoqLtNy6r0ZL0eTA3js1AgCQ1unFsaQpB80YP4m-692MzFKMC8e0ApQ7V1GQ3NigA1kqNsImMj6f9AkIsAFKpOk_py30dgzy_A19kAt46UpY3lLRcqhPsN1BpXU8Fe-GIwvtYJ0Jh4APEDO9IvCEvjETAuFPaqu9OmuupnEDolLBNdkidu5oPw2xz0nxE5dRPG7nAnGoRELLyAYFgRIIaWRQ39lEC8pa2NPHTA_o_NmNt6kjD8FWVuF7AlakxsGwXzkJIMb1QE8BA-BNUyaXa_jFrl_gybLHT0A490wq7Zga9CG-sDocaaPczZ1SqgbWSInQcqdP5_G8T0WchxMa7Jxum4hAQH7L0nW1GTHOGArgU1hiq0lBIN1gW7DfSXkjtLpqLZGhR8gMkpi8_V-PPhrTJ4GL890Cec0G3F8KvPlxp_6SiFcn-OKampYmkw_nxc5CKPNz4dXctDTb07IlP0VHBbmhI9c4xUKOVavx-jJe5XWmX-XNghOe881Lj8K0GPn7rrU92bxOI4f5Rnci5wU8bkrekyl86YoV98gdUFx87aa6aC98wxYnboC5kxvI3q4Yu0c-ADXXeD7A7IaHqtCgXSiPQjzK9Je27V8ZiBTm6f8OtY12mZwNIy0dm6RhQwNcn6STrvKb-mJrEskgGoEIdDT6DNFFlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن زنگنه، نماینده مجلس خبر از واگذاری بیشتر از ۱۱۰ هکتار از خاکِ ایران به افغانستان برای سرمایه گذاری افغانستانی‌ها داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696860" target="_blank">📅 12:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696859">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
در جمهوری آذربایجان به معلمان محجبه یک هفته فرصت دادند که یا مکشفه شوند یا استعفا دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/696859" target="_blank">📅 12:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696858">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
معاون نیروی دریایی سپاه: شناورهای متخلف در تنگه هرمز هر شب تنبیه می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/696858" target="_blank">📅 12:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696857">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b91258e3.mp4?token=XHdXHc4YIu2OWzThGsXTsHRr4P-a93sFvtXU5u0VCVvHseeqW9FhND7BLnQG19D1LITRAfqLVHPWCbj60vqO9vVC2rac_fgEx7qMqji4rJixTqP6nzXMSm7cixZLZH7eD_kMR41Q_3rQaGSaGUE_QaYVx4Mxq9Q0MKTK7nsRWHo-xCaBIV6u3qts8d4PJvN8BuHaSiQyxhiPdo00dqz_8XZk-dhWdPE-ej46cSSdU9qfsObcXjl_DkZzlhbG8VUYq4yL1hbGr8QeaZY5ICEOGUbI9STFhGdeObVCbI_Hgwbv2n_0_7T135huKC-Foe6Z20RVTSPn63vF6AR7Jhz-6otjb6l84Y4pb20WSDUHuE546UGXdlLaBUsToRGtW7jAlfMVmz7nQvhnSvuqRk59MNrMBb8bLxATmDwOocl3gT820JpWqXBrnvTLV6oFQgCj8DCun9GWDXiSltF-7W0xEWGlPx__Gdfkr_yBun1TuSch24HexKNoniumkfQTseHEucFMwyLzT3mV58djqzV8Te61izJFkbUaKNPUybFBJ-2KJLgVCg70HN4941RUnNq1MsUOl5MariYH6ymf4FxEg2eL31qF2wmsBXF7_ydvkz8-AqVETcOqLyloyXGoDoaJw1THezRmrCy0BYRZ-D8KcE2Qhqvhk_4NL52LOKSbxBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b91258e3.mp4?token=XHdXHc4YIu2OWzThGsXTsHRr4P-a93sFvtXU5u0VCVvHseeqW9FhND7BLnQG19D1LITRAfqLVHPWCbj60vqO9vVC2rac_fgEx7qMqji4rJixTqP6nzXMSm7cixZLZH7eD_kMR41Q_3rQaGSaGUE_QaYVx4Mxq9Q0MKTK7nsRWHo-xCaBIV6u3qts8d4PJvN8BuHaSiQyxhiPdo00dqz_8XZk-dhWdPE-ej46cSSdU9qfsObcXjl_DkZzlhbG8VUYq4yL1hbGr8QeaZY5ICEOGUbI9STFhGdeObVCbI_Hgwbv2n_0_7T135huKC-Foe6Z20RVTSPn63vF6AR7Jhz-6otjb6l84Y4pb20WSDUHuE546UGXdlLaBUsToRGtW7jAlfMVmz7nQvhnSvuqRk59MNrMBb8bLxATmDwOocl3gT820JpWqXBrnvTLV6oFQgCj8DCun9GWDXiSltF-7W0xEWGlPx__Gdfkr_yBun1TuSch24HexKNoniumkfQTseHEucFMwyLzT3mV58djqzV8Te61izJFkbUaKNPUybFBJ-2KJLgVCg70HN4941RUnNq1MsUOl5MariYH6ymf4FxEg2eL31qF2wmsBXF7_ydvkz8-AqVETcOqLyloyXGoDoaJw1THezRmrCy0BYRZ-D8KcE2Qhqvhk_4NL52LOKSbxBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه کامل شهید لاریجانی در مورد تهدید ترامپ به لودادن افرادی که بهش پیام دادن و پاسخ کوبنده شهید لاریجانی به ترامپ
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/696857" target="_blank">📅 12:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696856">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52fcda1e41.mp4?token=Uv14XSlhRU_sfKrjjQoFzYQxRrYECJ1uTi-8jx1Rojz_rW74aVjpIVqgPjT7J8-s0qDJ0JOH-7LaTuP4Vkef4phxFq8IN1R-83SHZAj5ikjELsf4l3Q2GiuvdZ3OB8m3HyAxsxhzLhF8p8zMMwiE1OOP_aSdWi9I_djQu98FWcvZY-40KpMjv3ikC-TkuBRh3evqo0zEIW1WzliBbcGMcNLJCLiaGyDXl_gqC7_JfOwQ8eFgEygrrwrk3ZAT_NlIQpdUewFiQUEvG5caW6Jb67fauULpXtQWHRHhscLhe0vMxel-gNllTUKdWwc15e1s95zD3jt5bNqlu5hvrIUcFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52fcda1e41.mp4?token=Uv14XSlhRU_sfKrjjQoFzYQxRrYECJ1uTi-8jx1Rojz_rW74aVjpIVqgPjT7J8-s0qDJ0JOH-7LaTuP4Vkef4phxFq8IN1R-83SHZAj5ikjELsf4l3Q2GiuvdZ3OB8m3HyAxsxhzLhF8p8zMMwiE1OOP_aSdWi9I_djQu98FWcvZY-40KpMjv3ikC-TkuBRh3evqo0zEIW1WzliBbcGMcNLJCLiaGyDXl_gqC7_JfOwQ8eFgEygrrwrk3ZAT_NlIQpdUewFiQUEvG5caW6Jb67fauULpXtQWHRHhscLhe0vMxel-gNllTUKdWwc15e1s95zD3jt5bNqlu5hvrIUcFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری پزشک قلابی که با سرم بیهوشی وارد منازل می‌شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/696856" target="_blank">📅 12:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696855">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262369a4b2.mp4?token=uiyPTdAzqoX35tHJsz0EfEmjHNe99-tw2xi2if1hLYNGosUc6lf-yJ36dC-bdCPcwCu7SxjJpfgjw74CZC0yly2xeBse9vmYO60ANHLsJe16LwzbjTuuWO-pocTxdb32Rsx_Hk7k9jaq7s1ej5kn09lD5ws_Kz9WSPQaJGvviYc3Wu9SCXGKRmbDdYNiuGwRNJTSMbSrHZMemXYfv6Zy8qSUIKfFomEmIQShjSq4rWzloCDquh7kRt-cLqqCUnlamy4IeIQMy84P1SDQspLGxUDq0Ski39ZWzzR2WHKq9Cvuby8h0HMVV1t57phvJCVgW321Ryi_X3dHYJboxBT8WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262369a4b2.mp4?token=uiyPTdAzqoX35tHJsz0EfEmjHNe99-tw2xi2if1hLYNGosUc6lf-yJ36dC-bdCPcwCu7SxjJpfgjw74CZC0yly2xeBse9vmYO60ANHLsJe16LwzbjTuuWO-pocTxdb32Rsx_Hk7k9jaq7s1ej5kn09lD5ws_Kz9WSPQaJGvviYc3Wu9SCXGKRmbDdYNiuGwRNJTSMbSrHZMemXYfv6Zy8qSUIKfFomEmIQShjSq4rWzloCDquh7kRt-cLqqCUnlamy4IeIQMy84P1SDQspLGxUDq0Ski39ZWzzR2WHKq9Cvuby8h0HMVV1t57phvJCVgW321Ryi_X3dHYJboxBT8WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه شستشوی ظروف مسی که شاید بسیاری از ما، از آن بی‌اطلاع باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/696855" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696854">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TzSSyJbcT5eMtvhWHDgAsT2ZUSrNgYAbzD8xyfbNkEajTBVMuvnNreWxi48QJCnt6eJwgd0uuTjhEZyYP0B4YHa05HclAwC3QcpEeK9-rLPHr3JCiuGwYY9Dd242tXfl5biarznjHlGU9xKMA-dd9rYUqRoXcuQh9KM-Vvi0b9al33UOkIbj0vzVdOYt_o4ztbkQZj-UCTZN-S0CbLRZC8ros2AhAwDfI-rdiuL546Cc4pa3f1KVlOpyFKQnLRGQMpax72zSTQ05QkmfckUxkt1Uc_Bfq0jpOBreAA_1BZFCA03ko4PgUYKSm_Jia1UunsDVhmb2PH94B1QyQpIAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بالاترین هشدار امنیتی در کره جنوبی صادر شده است
🔹
دوربین‌های امنیتی بخش زایمان زنان در مراکز درمانی توسط یک سری افراد هک شده و درحال انتشار و فروش فیلم زایمان‌ها در سایت‌های مستهجن هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/696854" target="_blank">📅 12:05 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
