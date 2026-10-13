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
<img src="https://cdn4.telesco.pe/file/IdrBVNgS2lgGwepqQYJQzi1rm7ssfTVDJ4zabDbc5MdCo5GysBWeosTjxEROEW4hXG63qHr5dwoggbqyuueZjOdcinI_x0WCOzd0XSBMGAs8rAyoEqtWZHCm4L2Gq017_K3I2xb_muxw5td5A_wUJuah5mifVxFipx000qjL77h6BXyX52-DzhqyXhKcXNShaeEmeA5nt4jFB5kyi_EjjV7sOXiRiY-qrp-oNy1Khas7CeJIs1euZgXevgWVP7TvVdstNNHNo-4RThr1zkeI-8Gtui0S7yAd85-jd7bNr7H4iC2e8atGFe9Rhm0x6pVu38kg_71ckJnUdSC-ZLPBXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-73241">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26766391a1.mp4?token=dff96swu5RsaYDhLBXUy-8Mdq2drZuOtyixI7NgH8XzUW8nSVHf9sySOiPvMmFehH-Rm2-QWdcou_U-Qg_xeswDujtkU-hlxHiMayq_WYhgnbxL3hj8hjxZ7Hvr-fN2FXgQJB5N6S5KJnKwK7yvZ38GiCI81D3lcOu7Jl4LY_ZosrnJMwtTnVIm2TqE7hUJy_4S8aLOe43ITbm8eieSfd3OwNf_45pdg_ax4HOIcmyfntac4CFKkoz7UHO9fVCddGQ_fl3XwQPdgXQXAer9y35_137ysc6KAKBMtxih-QEoLiB1Ffr61Y9KqQt7Dfjd35BUF9yr392hO4TSMUm9KPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26766391a1.mp4?token=dff96swu5RsaYDhLBXUy-8Mdq2drZuOtyixI7NgH8XzUW8nSVHf9sySOiPvMmFehH-Rm2-QWdcou_U-Qg_xeswDujtkU-hlxHiMayq_WYhgnbxL3hj8hjxZ7Hvr-fN2FXgQJB5N6S5KJnKwK7yvZ38GiCI81D3lcOu7Jl4LY_ZosrnJMwtTnVIm2TqE7hUJy_4S8aLOe43ITbm8eieSfd3OwNf_45pdg_ax4HOIcmyfntac4CFKkoz7UHO9fVCddGQ_fl3XwQPdgXQXAer9y35_137ysc6KAKBMtxih-QEoLiB1Ffr61Y9KqQt7Dfjd35BUF9yr392hO4TSMUm9KPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عرازشه در مقابل منزل حسن روحانی و شعار بر علیه او:
@News_Hut</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/news_hut/73241" target="_blank">📅 22:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73240">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=oAb709mQ6FBug0iSUQqNZqPlOuMDiflJnIEmFpW7mlPQgl6nKeX5dQE84QdpcQOBTxTm6tOvLWH1P5S3SDk33PuRGz16oGrPe2j1FeumwTZez0RNjweKWpswEEQJaore5J2UP5gzkB92WNNrv9hAikxINWPANtPaZrjGuV5ixOiApU8oy_Qv9A7pCagEgWqk4caWX2js2V1iXSB-zvEU2e8KIf2lQy6FZ6zUK570pRhlKjq5YPXnY6MdP4VLPMeQONpELiFFHqErqfEmTH_6_3Hu8Nn70OLEx5803lLjewreDUfPdCYuon5mJejZtJIjw3cI41sM-xR7SqPI40Lsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6568459aaf.mp4?token=oAb709mQ6FBug0iSUQqNZqPlOuMDiflJnIEmFpW7mlPQgl6nKeX5dQE84QdpcQOBTxTm6tOvLWH1P5S3SDk33PuRGz16oGrPe2j1FeumwTZez0RNjweKWpswEEQJaore5J2UP5gzkB92WNNrv9hAikxINWPANtPaZrjGuV5ixOiApU8oy_Qv9A7pCagEgWqk4caWX2js2V1iXSB-zvEU2e8KIf2lQy6FZ6zUK570pRhlKjq5YPXnY6MdP4VLPMeQONpELiFFHqErqfEmTH_6_3Hu8Nn70OLEx5803lLjewreDUfPdCYuon5mJejZtJIjw3cI41sM-xR7SqPI40Lsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرویس بهداشتی یه مدرسه پسرونه در تهران!!
@News_Hut</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/news_hut/73240" target="_blank">📅 21:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73239">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbTTAj7biiKOyBVZpQlNm0UyL2YZ0d1anTUtaRsiTWhbHaIrp4xhw9cwhOH2L74uKR4O52ArqEGQb5JqWxtsnm7kSfjDUtnN9_ryL1NmllRIce-4nh8xsduQl9qxtLsUmIgwK0CbHscBG2Zd2538nmJg9aVPs_ch_FdNcrJr_WlAvZd8QEiwS1z_N2ZM_QzvKUZNa5tE-c_Xh6nZQFviEYU-RX9wex07PLjVAGtKxp-3HjWWsgMOH3qpZfQK0fnYc8W6xgt9qQ_ZYcWoeRubeEZLvy0QWG-71fDaXGeQdmAScRcKix4fKrQLes1vsMPL4GXroNk_J-ULgkOV1DfP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، طی دو هفته گذشته گفتگوهای متعددی با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره آغاز یک عملیات نظامی مشترک جدید علیه ایران داشته است؛ عملیاتی که احتمالاً پیش از انتخابات ۲۷ اکتبر اسرائیل و انتخابات میان‌دوره‌ای ۳ نوامبر آمریکا انجام خواهد شد.
نتانیاهو با ابراز نگرانی نسبت به تلاش‌های ایران برای ازسرگیری فعالیت‌ها در تمامی بخش‌های برنامه هسته‌ای خود، این تحولات را توجیه‌کننده‌ی انجام حملات مجدد علیه تأسیسات نظامی و هسته‌ای ایران دانست.
یک مقام آمریکایی اظهار داشت که ترامپ به نتانیاهو گفته است «اقدام کند و آماده شود»، اما تعهد قطعی نداده است؛ در همین حال، مقام دیگری گفت که موضع رئیس‌جمهور همچنان در حال تغییر است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/73239" target="_blank">📅 20:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73238">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حوثی‌ها (انصارالله) اعلام کردند که عربستان سعودی طی ۲۴ ساعت گذشته ۱۰۴ حمله هوایی و موشکی علیه صنعا و استان‌های ذمار، تعز، عمران، لحج، الجوف، مأرب، صعده و الحدیده انجام داده که منجر به تلفات غیرنظامی شده است.
این حملات توسط جنگنده‌های اف-۱۵ و تایفون که از پایگاه‌های هوایی «خمیس مشیط» و «طائف» برخاسته بودند، و همچنین با شلیک موشک از «نجران» صورت گرفت؛ امری که مجموع حملات ادعایی ائتلاف به رهبری عربستان را به ۲۲۸۱ مورد می‌رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/73238" target="_blank">📅 20:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PPPG7Y70tMK9xIvVhnI1j_Dprc_Aqa6yzKUnOi-Ax8a0zIjvkj_LVA7B_z_TizwG4d3HJT6gVodIAEFZhNKQt6gbcoifS60eyTFS7V4AqqaHB-C76rvqmWOK-t860aenqjtJazy-jFU0fSokOXP7UNv0X7qpDJUJp0sgnr88zGsDyJ-YrLnU6q2X6gN3VTBU-71TDgsiyl48ZKlKNjmPqonEfRMd5tlR4XoZcVIjPxXbGaUmLAx-U-4TIbI-bJdIBtZ0R_CGBWeBzWzHRGeA-J1-6Obo4WNgGAiyCN8nNkwgeCa8UFymM0rmYvpZDIkNoNYXLgrFPKN6JPEy6798TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ترامپ در تروث سوشال:
«حوثی‌ها رفتار خیلی بدی دارن. فکر می‌کردم یه سال پیش، وقتی حسابی بمبارونشون کردیم و به درخواست خودشون حملات رو متوقف کردیم، درسشون رو گرفته باشن.
اونا مدت زیادی سکوت کرده بودن، اما حالا دوباره ظاهر شدن؛ احتمالاً به دستور ایران که یه کشور در حال فروپاشیه، نیروی دریایی نداره، نیروی هوایی نداره، بدترین اقتصاد دنیا رو داره و تورمش به ۳۰۱ درصد رسیده.
اونا به شکل خیلی بدی به عربستان سعودی حمله می‌کنن و عمداً سعی دارن قیمت نفت رو بالا ببرن؛ احتمالاً هم قبل از انتخابات آمریکا. این اصلاً قابل‌قبول نیست!
یکی باید بهشون توضیح بده که من دیگه نامزد انتخابات نیستم؛
من قبلاً با اختلافی بسیار زیاد پیروز شدم!
اما بعد از انتخابات دوباره وارد ماجرا می‌شم و این اتفاق رو هیچ‌وقت فراموش نمی‌کنم!»
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/73237" target="_blank">📅 19:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=GADSdIwg-9koaTcDPiuiR4h49yYD5tKNaDSNhZPpdCNBtfJPY1nOS0gB3ulvlYNwQPCgJOZblXcsjaCdMxvhyKt3UFoRp9plCGX5ElMkNqiqZFJS82pCcDiQ7NPJFeSUS7ZHXS4MI03Ykl5lWMqktWeeuE6M2FKyiPOc7APdMx9rZBA8ABJrgsbOD_OhLx-lnkU_A6fVPtdSExNljRhwA-0XB_rLW7b1cFaxuqWr6arqZ4maaeWFTRRInPC2VzQbKBDYujkP32bXfcBzo_EWxJx1g75Gy4FasClXC2zrQA1RNAdxq78xnMiNzCpSY9M6UvgrM1wMxUlfE0Q8SIzAyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0e101b64.mp4?token=GADSdIwg-9koaTcDPiuiR4h49yYD5tKNaDSNhZPpdCNBtfJPY1nOS0gB3ulvlYNwQPCgJOZblXcsjaCdMxvhyKt3UFoRp9plCGX5ElMkNqiqZFJS82pCcDiQ7NPJFeSUS7ZHXS4MI03Ykl5lWMqktWeeuE6M2FKyiPOc7APdMx9rZBA8ABJrgsbOD_OhLx-lnkU_A6fVPtdSExNljRhwA-0XB_rLW7b1cFaxuqWr6arqZ4maaeWFTRRInPC2VzQbKBDYujkP32bXfcBzo_EWxJx1g75Gy4FasClXC2zrQA1RNAdxq78xnMiNzCpSY9M6UvgrM1wMxUlfE0Q8SIzAyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خبرنگاری رو که همیشه درباره وضعیت ایران سؤال می‌پرسه، مسخره کرد:
ترامپ:
«ایران؟ باز هم ایران؟ همیشه ایران!»
«ایران یه کشور شکست‌خورده‌ست. هیچ اقتصادی نداره، تورمش ۳۰۰ درصده، پولی نداره و حقوق نیروهاش رو هم نمی‌ده؛ نه به نیروهاش، نه به هیچ‌کس دیگه‌ای پول نمی‌ده.
خیلی زود درباره ایران تصمیم می‌گیریم.
ما تنگه هرمز رو کنترل می‌کنیم و نفت زیادی هم از این تنگه خارج می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/73236" target="_blank">📅 19:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=f1BJpx750HC_hQH1EnRb0-mMXtdX3mhHv0tsCl4CkONIh3Pc_jv5exAGqe-FX2XrWVxFdywXJmjqgmOebJwN8c2YeOGes_d--lrjuX_PYMZDb9C_-0Y6wx1gkCPDomRjeCJ6vB7RK1NPEEW4ZWe6pPAq-L6_LQzLai3fNmVFfORj30xxseZBZbO71fvNCLZf2ji13lS60olR0XGMWUGA5jIxHnx8TMq1K8lXvzhuXerxhKkSRo-wXIGNLN-_vYHMGdv1uesTOUgUi7E3XgK3GkoSaMBxVGKIOjJVmM3O2bOFMdpOEdE3UN4YwErlsmfc6w-ZVIivOj45JtNUlmB9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2628e9cb18.mp4?token=f1BJpx750HC_hQH1EnRb0-mMXtdX3mhHv0tsCl4CkONIh3Pc_jv5exAGqe-FX2XrWVxFdywXJmjqgmOebJwN8c2YeOGes_d--lrjuX_PYMZDb9C_-0Y6wx1gkCPDomRjeCJ6vB7RK1NPEEW4ZWe6pPAq-L6_LQzLai3fNmVFfORj30xxseZBZbO71fvNCLZf2ji13lS60olR0XGMWUGA5jIxHnx8TMq1K8lXvzhuXerxhKkSRo-wXIGNLN-_vYHMGdv1uesTOUgUi7E3XgK3GkoSaMBxVGKIOjJVmM3O2bOFMdpOEdE3UN4YwErlsmfc6w-ZVIivOj45JtNUlmB9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا از ترکیه می‌خواید که در واکنش به اقدامات یمن ملحق بشه؟
ترامپ: «ممکنه این کار رو بکنم. اردوغان دوست خیلی خوب منه و احترام زیادی براش قائلم.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/73235" target="_blank">📅 19:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=Rzh1I5Iyk3frrd5c2_C9evY98CyBBBdv9vyzDliFrSwKy27zhXmGFqCgAuYk_qrPebGzuzHAuRFE82AoO8hgzPmuIkkkG-dB45KtkvHfI3r1u8gD6FhPxmaGe2K5oe1iC_u7mw71JGZAl_R9iXURnSiNPZ0S59X7_7xfFLe7Bc95Mq45vOZ-r__4sOiEyaBe4cmcBNN8nuvSZLLdFL-Rb_YdW4BnzvZNMB0iPGyK90ZFYPO0WG4Tltko9wmV1J3Msh6bVwZUb7ol6TMV3g2FQhQr-2sfVXyWy1OlS4u2yhCVa4X9NOPh9oiQM5WF_C9LVl5ETcmkKIbWLoZRAfc2VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fdc0493f.mp4?token=Rzh1I5Iyk3frrd5c2_C9evY98CyBBBdv9vyzDliFrSwKy27zhXmGFqCgAuYk_qrPebGzuzHAuRFE82AoO8hgzPmuIkkkG-dB45KtkvHfI3r1u8gD6FhPxmaGe2K5oe1iC_u7mw71JGZAl_R9iXURnSiNPZ0S59X7_7xfFLe7Bc95Mq45vOZ-r__4sOiEyaBe4cmcBNN8nuvSZLLdFL-Rb_YdW4BnzvZNMB0iPGyK90ZFYPO0WG4Tltko9wmV1J3Msh6bVwZUb7ol6TMV3g2FQhQr-2sfVXyWy1OlS4u2yhCVa4X9NOPh9oiQM5WF_C9LVl5ETcmkKIbWLoZRAfc2VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سؤال که آیا حوثی‌ها رو هدف حمله قرار می‌ده:
ترامپ: «اونا خیلی بد رفتار می‌کنن. اگه بهتون بگم تصمیمم رو گرفتم، اون‌وقت... حوثی‌ها واقعاً خیلی بد رفتار کردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/73234" target="_blank">📅 19:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=RCHAkwL7oOf1onzazwyUCMzyiZmwkFPlCYrc6-zyt4AsAAHLjGsYbRnsIBCJ28Ax5mPz8URCm3azkM-aG_IEB8ZckO_-0EkYVARpT81G7PE_UpfoiponWC0ySJltCxJaR4kJ1EdnLI5AeMYPZmr28SzMmcFKkWyJACY-qVUVMNoHLQ5fYdA5xfRzTLxoDwTkV_7tZgobvZtFshvlH5ih1vgCHthrgjhlph3nSceZjk9vBoxa8x2AjffOx3JLjI3Y5LH3okepCz2eur_UGqb5YgHqYmpkaE-Fs3PAXex9LCW1eV2yxk4q0g8tIyjosX1J4MTnAG7RjoC8Ki3Yhtl3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae90f7f46.mp4?token=RCHAkwL7oOf1onzazwyUCMzyiZmwkFPlCYrc6-zyt4AsAAHLjGsYbRnsIBCJ28Ax5mPz8URCm3azkM-aG_IEB8ZckO_-0EkYVARpT81G7PE_UpfoiponWC0ySJltCxJaR4kJ1EdnLI5AeMYPZmr28SzMmcFKkWyJACY-qVUVMNoHLQ5fYdA5xfRzTLxoDwTkV_7tZgobvZtFshvlH5ih1vgCHthrgjhlph3nSceZjk9vBoxa8x2AjffOx3JLjI3Y5LH3okepCz2eur_UGqb5YgHqYmpkaE-Fs3PAXex9LCW1eV2yxk4q0g8tIyjosX1J4MTnAG7RjoC8Ki3Yhtl3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی، خبرنگار فاکس‌نیوز: «اشتراک‌گذاری اطلاعات و داده‌های اطلاعاتی با اوکراین رو متوقف کردیم؟»
ترامپ: «نه، متوقف نکردیم. ما بهشون کمک می‌کنیم و واقعاً داریم کمک می‌کنیم که به یه نتیجه نهایی برسن. پیتر، ما می‌خوایم جنگ تموم بشه. داریم بهشون کمک می‌کنیم و اطلاعات هم در اختیارشون می‌ذاریم. می‌خوایم جنگ تموم بشه؛ برای همین با اوکراین و روسیه همکاری می‌کنیم تا به این جنگ پایان بدیم.»
این جنگ بی‌فایده‌ست و باید تموم بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/73233" target="_blank">📅 19:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=gnVuFo14Ryz573u2Edc5LS2h8hsiNko63Ngtc1LuqgNh2fa1ujb6LjxKfa7kTj_10qpOUB-fWmwfME6lANCwf_mZFnqbHZvRQNiQh74Nq_eCNdZUNfDK_F0DotEfJi0yF8d2q9g5eIxflzwLYONMQ3cM8uBc85Y0WHobFERdRGjTFFME-4-9l251QFvUjfhFFPWehji9AS-18wYpP2U0awknOULFyNbmq1Q4L6mv21bEuZnorTgViehzQPo51S5-Wov4yOCrnff0DGWZM8I6nf8R16OpR8vSIssjCid0JuERbKIKwFP6_AHS72AXy8zESUhP6DeM0zsEItlvLqcbpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3fc7b7be7c.mp4?token=gnVuFo14Ryz573u2Edc5LS2h8hsiNko63Ngtc1LuqgNh2fa1ujb6LjxKfa7kTj_10qpOUB-fWmwfME6lANCwf_mZFnqbHZvRQNiQh74Nq_eCNdZUNfDK_F0DotEfJi0yF8d2q9g5eIxflzwLYONMQ3cM8uBc85Y0WHobFERdRGjTFFME-4-9l251QFvUjfhFFPWehji9AS-18wYpP2U0awknOULFyNbmq1Q4L6mv21bEuZnorTgViehzQPo51S5-Wov4yOCrnff0DGWZM8I6nf8R16OpR8vSIssjCid0JuERbKIKwFP6_AHS72AXy8zESUhP6DeM0zsEItlvLqcbpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی حملات هوایی نیروی هوایی سلطنتی عربستان سعودی، مخازن سوخت در بندر الحدیده یمن (تحت کنترل انصارالله) دچار آتش‌سوزی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/73232" target="_blank">📅 18:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73230">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=j4uXEhD5y4_86sUkqqa_uTrcXe60E7alMvpMn2rc4Pr4b-IjMxQqgjAKdAN-rHv-QDrbx6MxaqdqPLYxxqMjfVa1M8ZweSAHVqmMf-hZ91Xg4zrFmGP7vMQYK53C3E4sV3gwffVgn1zxL-kn9bleXVEwP-BYgAl3OjDsXvYi1sJjVmVnQGCfd4zChu_A9lZkXTPjZOsecoxtiNIVKwzMGoSl3Iv9j7hk0RskSANriEoxZ666_OdIH_IyC2VTGBBr1FQcv2Kvvso4x4wCH2-vDkhkmn9D1Z8nbJNAS2Dd9FutSk4huAvFyybEFCMGePvZSsZlH7A7KrF_LlnqBUNIqWZalMOjfhbMwtK1fZgmZFZi79xssv6Mwtx8VYQZtPPnLQCYwPa08ykHmALNr23NYyydJ3b_WHJeyj_ey1vIBAIRSenB0RkaVbYRRUmj31vaFByDkEM8iXz8ORVBy4yMSHzYnqj1K1YIp3mECwIQBYpIJ8yLhOIaWn3Xt0i7uy0-zgIm-51cc4dH06sx7qQnt1BfMCt5FnocC0_ZGWV5GvYWfFFojRpFWsGsng218tXYZhpgt3f1UQvdiwkxMTRrUwAuE7C1nxakoP1_F5hWvYHf-Ech_jAtHUtT8y497rP-mVPw26w3gPJe0twexbug89xzNdepwbf6BFKBxrY44S4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3237ca4f82.mp4?token=j4uXEhD5y4_86sUkqqa_uTrcXe60E7alMvpMn2rc4Pr4b-IjMxQqgjAKdAN-rHv-QDrbx6MxaqdqPLYxxqMjfVa1M8ZweSAHVqmMf-hZ91Xg4zrFmGP7vMQYK53C3E4sV3gwffVgn1zxL-kn9bleXVEwP-BYgAl3OjDsXvYi1sJjVmVnQGCfd4zChu_A9lZkXTPjZOsecoxtiNIVKwzMGoSl3Iv9j7hk0RskSANriEoxZ666_OdIH_IyC2VTGBBr1FQcv2Kvvso4x4wCH2-vDkhkmn9D1Z8nbJNAS2Dd9FutSk4huAvFyybEFCMGePvZSsZlH7A7KrF_LlnqBUNIqWZalMOjfhbMwtK1fZgmZFZi79xssv6Mwtx8VYQZtPPnLQCYwPa08ykHmALNr23NYyydJ3b_WHJeyj_ey1vIBAIRSenB0RkaVbYRRUmj31vaFByDkEM8iXz8ORVBy4yMSHzYnqj1K1YIp3mECwIQBYpIJ8yLhOIaWn3Xt0i7uy0-zgIm-51cc4dH06sx7qQnt1BfMCt5FnocC0_ZGWV5GvYWfFFojRpFWsGsng218tXYZhpgt3f1UQvdiwkxMTRrUwAuE7C1nxakoP1_F5hWvYHf-Ech_jAtHUtT8y497rP-mVPw26w3gPJe0twexbug89xzNdepwbf6BFKBxrY44S4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ارتش جمهوری اسلامی تصاویری از یه نفتکش در حال سوختن تو شرق تنگه هرمز منتشر کرد و از اعزام نیروهای جدید به دریای عرب، دریای عمان و شرق تنگه هرمز برای رصد رفت‌وآمد کشتی‌ها خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/73230" target="_blank">📅 18:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73229">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=m9Et5YNhy1tqQ0t1E_rGI5vW8AeDABO6sXSOKa332MJxy5EpsMCTWCOly89ippI5BXPoCmunYhVStqeT6uJTbvelR8HrqOujbhGVJJdmAZdhmbm-9hjOowzlc7vc_9WyLwXgEYynVFunSINNSNsECEdm6YiosXluE97JHJqqTF0mcGeeVHPqyGlz0UAFurmKiYckAJx5qZKkzI4WkuiMvg-n9wCeOSWcxv0UqbtKX5BFqas05YypwFTiUg5_WFuCZb7ywT8Dv54UiR4eprxFDAxNvJL2JJj8bO0aPfxQROM0Ff_hUoUhPvEgq_Tq10uXmyxUAMnqUO5k0q21Zouzpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7853c789a5.mp4?token=m9Et5YNhy1tqQ0t1E_rGI5vW8AeDABO6sXSOKa332MJxy5EpsMCTWCOly89ippI5BXPoCmunYhVStqeT6uJTbvelR8HrqOujbhGVJJdmAZdhmbm-9hjOowzlc7vc_9WyLwXgEYynVFunSINNSNsECEdm6YiosXluE97JHJqqTF0mcGeeVHPqyGlz0UAFurmKiYckAJx5qZKkzI4WkuiMvg-n9wCeOSWcxv0UqbtKX5BFqas05YypwFTiUg5_WFuCZb7ywT8Dv54UiR4eprxFDAxNvJL2JJj8bO0aPfxQROM0Ff_hUoUhPvEgq_Tq10uXmyxUAMnqUO5k0q21Zouzpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۸۰ تن میوه به علت بسته بودن تنگه هرمز رو دریا خراب شده و داره دور ریخته میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/73229" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73228">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/73228" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73227">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/patPdm-b9qTYQL6oaA276jkPlZ1XdWVexxGiGWnBRXsasEp4XSlMgpmsa_PSThkoB78GIS0-NJdlO3cwgspiLSAw5m3aEuUhj7Bv36BBcIik5iI3rULyPdV8nQ2Sq5XYrFlSZt-es_UaalZUU6cnZN13nnWsvcO3LeFpclRh5EfF7TShFAfrc6o1SUDUNKTuJJU56GVYnivs_jlYy2SXJFsJhCEPriq-4VsNmX6GN5z8VYToaTyx0Z0Fenp2vyvGiF3z75IgqtgSIswx4mjPTxcDmPbgWpOWH2spb-hWQ73wVOXRXvTK34FoNcVYTKfD38CoFz8192EXQayIlrLKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منچستر یونایتد
🆚
اتلتیکو مادرید
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم
در ۵ رویارویی اخیر :
منچستر یونایتد : ۱ برد، ۲ تساوی، ۲ شکست و ۷ گل زده
اتلتیکو مادرید : ۴ برد، ۱ شکست و ۱۲ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/73227" target="_blank">📅 18:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73226">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به صنعا، پایتخت یمن تحت کنترل انصارالله.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/73226" target="_blank">📅 17:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73225">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=DVrHIqvezRJ3GRlmrEA64p8i0bAJ-2gczGhElGLSgEQYrW-yRu81YCNcJg32bmt32-w8nBGLq9r3gN4yYg1PtQBKWz9AVUMdvb2Su-Nt5oXVmAj2zaiS6hxSuGBtVz00i2IMxnKkB5MCKg2qaDO3gwCWxbJHVmhIclyGkfKCUwHSDNnHUbeVGU8fhL-vp-ZOynl-arfcErytODLpSJyt2ej2GvMd9ghjUjj0ulITgcm00RSemV6YYfjRqAri3kToBI0pu-dBpi21jc92mpv7NePLQHe5J-clSuya0ltEHXSP9n49ewHT8aXTkAUyppD-m1_MTrGFor7R3_XMDbcWjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f155f86ad3.mp4?token=DVrHIqvezRJ3GRlmrEA64p8i0bAJ-2gczGhElGLSgEQYrW-yRu81YCNcJg32bmt32-w8nBGLq9r3gN4yYg1PtQBKWz9AVUMdvb2Su-Nt5oXVmAj2zaiS6hxSuGBtVz00i2IMxnKkB5MCKg2qaDO3gwCWxbJHVmhIclyGkfKCUwHSDNnHUbeVGU8fhL-vp-ZOynl-arfcErytODLpSJyt2ej2GvMd9ghjUjj0ulITgcm00RSemV6YYfjRqAri3kToBI0pu-dBpi21jc92mpv7NePLQHe5J-clSuya0ltEHXSP9n49ewHT8aXTkAUyppD-m1_MTrGFor7R3_XMDbcWjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه شهروندان ایران کرجی‌ان، فقط خودشون خبر ندارن؛ چون بالاخره هر کسی یه فامیل کرجی داره.
آغوش کرج به روی همه بازه، ما هم آماده‌ایم از همه مهمون‌نوازی کنیم.
از پارک‌های زیبا و اماکن دیدنی تا رستوران‌های خوب، همه‌چی مهیاست؛ فقط مونده بیاین کرج.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/73225" target="_blank">📅 17:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73224">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#فوری؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/73224" target="_blank">📅 16:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73223">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حوثی‌های یمن بار دیگر به همه کارکنان تأسیسات نفتی و فرودگاه‌های عربستان سعودی هشدار دادند که محل را ترک کنند و این نشان می‌دهد که حملات بیشتری در پیش است.
حوثی‌ها به همه «کارشناسان، مهندسان و کارگران در تمام تأسیسات نفتی عربستان سعودی» هشدار دادند که مناطقی را که نشان دهنده اهداف هستند، «چه قبلاً مورد حمله قرار گرفته باشند و چه نه»، ترک کنند تا از به خطر انداختن جان خود جلوگیری کنند.
آنها همچنین هشدارها را به خطوط هوایی، فرودگاه‌ها، مسافران و کارکنانی که قبلاً به عنوان مناطق هدف تعیین شده بودند، مجدداً تمدید کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/73223" target="_blank">📅 16:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73222">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4GnX9Wk3un1iw0JM4SZTJkd12WDCHxjnZMK2ppgGgK18pv6js7rxwDoQ71lPhaD4dCxPbdWcsB74EJwyUaxUEq1XtErcpN0Gdqt2u0V8gEA9O96DKv0R8uthpixesBxAyroq3iAQ0oc33Leo__Le-Y21h18PtU_8OdtOpIp14SXhw92qSxouBMg3uF5pID3HKjCwZd6tZlNB4KZWuf6MjUrC4-v-NeprN_7z_mPZmmIF44BWqvHT_BY_iUuErXzDeD0dZGJ-qrj_wfNkyB-73EPfwliYlztoP2bsVz74l8uCnZYkQ_hTMU4mej3D3n4WmCdK9D5BXsMM7fYdU6L1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛ائتلاف به رهبری عربستان سعودی دستور تخلیه ایستگاه مرکزی «الصباحه» متعلق به شرکت نفت یمن در صنعا را صادر کرده است؛ تأسیساتی که تحت کنترل حوثی‌ها (انصارالله) قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/73222" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73221">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/73221" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73220">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tpKltLThb6iqP_HfyiOF21GGgHISap6XFrW8eIV6t_n07Xgs7e1X8Y893ZkXbqJPjPEW9to2mnqRJdf3MuLkDfm9WHWq83ZuwwVLaVYvxw2qlSKIj30RGidYgaiOOMecBnl-hpnnd9w0tfGf7mUEnfyTxNthqT8ZhjA0tiIB_TSLKnPQTf-ZAkgi_vkHmZvGUEuKe54t9vNiD-1CkEJsuA0m90asfXRm0nQBSPHFK4Mg8QzYPV9rSQwnYK8DRBwr3iPNcnk-MKxiLKHLWuHvx_Bz9pO367Oa9BvjHW_VLlxy-5fShNq7F8IuJS4Zb7HKyTxAwouJSVSferl3-H8nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/73220" target="_blank">📅 16:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73219">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HZST9ylQ0sevEn_OEenivMJUpVfhQUvRCrvkCzp-0WGvZbZvILDpSeWnc6sDT-3ceYK6bJbZ3-6RQTnmsD-hNNxpNhQB_xEMR5kwwsFLrOz8y3kvSnlPcX8ASEUKfN3xmfSZFnuW7063sIYkMcz1Jtkg8glo9K4ify1UwAWt8aJAiqYO4EhNvgrHRjakwdZcP-h7yc2BAH_LpuO95IKrM6rYc-QeiWrkYZ5n5oV0jtYug44-yYkp7FCy0OPIWU2D3r85NabxywGWI6Iegy-SxFmAPLe8hxfubJKy-FmC4xZqUqzQyf_JjIzjYKqWU5ntuvrmRtZhjvjy44LQMWUKyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش وال‌استریت ژورنال به نقل از منابع مطلع، ایران به کشورهای منطقه هشدار داده که در صورت آغاز دوباره جنگ، ممکنه نیروهای مسلحش حمله زمینی به کشورهای همسایه انجام بدن.
ایران همچنین به مقام‌های عرب هشدار داده که ممکنه تأسیسات نفتی عربستان رو هدف قرار بده؛ در کنار حملات ادامه‌دار انصارالله به تأسیسات نفتی سعودی.
به گفته این منابع، ایران قصد داره در صورت شروع دوباره جنگ، حملاتش به نیروهای آمریکایی رو هم افزایش بده؛ از جمله تلاش برای غرق کردن ناوهای آمریکا در غرب آسیا و کشتن ملوانان حاضر در اون‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/73219" target="_blank">📅 16:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=NY2VqHa_Gbsc-LR24s7VZ8HHGg39uHeVMyObZ6PTeaeAXgNIPSq96F6ddod9dod-l45YO4HcpCmFi_8H7cLH88ctHW87NDXQiMU312kjAwvB7drK0O8w9mFEPJGJfCHTiMm6quh_dBRHHGyURjhy-UQ7372rgOMm0uw5Pw9yQjOsUsWEf3eOepwmboG8BqNePdOnMi8Nxh-ayWEq6oe0JzcBst9-1lzHhx3QSa9tfYRh81TOFjo46tk-494BLGn8yUkfeKIFhzX1SXCzJ_nNUASW9BNTRBaOhtfkwJszEwgUummjxTafuy7Qq673fZGMrTmRk2BzEv3opq8zQD42GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f037a6e61d.mp4?token=NY2VqHa_Gbsc-LR24s7VZ8HHGg39uHeVMyObZ6PTeaeAXgNIPSq96F6ddod9dod-l45YO4HcpCmFi_8H7cLH88ctHW87NDXQiMU312kjAwvB7drK0O8w9mFEPJGJfCHTiMm6quh_dBRHHGyURjhy-UQ7372rgOMm0uw5Pw9yQjOsUsWEf3eOepwmboG8BqNePdOnMi8Nxh-ayWEq6oe0JzcBst9-1lzHhx3QSa9tfYRh81TOFjo46tk-494BLGn8yUkfeKIFhzX1SXCzJ_nNUASW9BNTRBaOhtfkwJszEwgUummjxTafuy7Qq673fZGMrTmRk2BzEv3opq8zQD42GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌ها در ارتفاعات چاه‌احمد تفتان، با گذشت بیش از ۷ ساعت، همچنان ادامه دارد.
به گزارش حال‌وش، در حمله افراد مسلح به ستون موتورسواران لشکر فاطمیون، بیش از ۲۰ نفر کشته یا زخمی شده‌اند.
پس از این حمله، بیش از ۴۰ خودروی نظامی و پهپادهای شناسایی و رزمی به منطقه اعزام شده‌اند و نیروهای نظامی همچنان با خمپاره و پهپاد ارتفاعات را هدف قرار می‌دهند.
این در حالی است که رسانه‌های حکومتی پیش‌تر از پایان درگیری و کشته شدن تنها سه فرد مسلح خبر داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/73218" target="_blank">📅 15:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی:
به‌زودی به غیرنظامیان هشدار خواهیم داد تا مکانی را در صنعا تخلیه کنند؛ این اقدام به منظور انجام یک عملیات ویژه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/73217" target="_blank">📅 15:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73214">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhWh05TbNh9Vk-yPxv3UqomHrutfqAKUBfL2LHsRxTIo_awsewltfImZriOKhSPzfQWAwzjqDSTlWrYuILZqDPNAmJRZcQaMzBQzt3n0Uh-VAdElWKw2l_NzS8KHvhXhK88xqxp8VWxJ8cxyCzpzB8eiZ9mJixMfAGvOLBsSbPKUljRxwpsEPJkMpnbLmmhDRMot5rhDojKIAu-T7zJPSBKElv_YV5GvRRd1-cMYPYzlaWgad7hVwascm0l4nGUe6zhmAySJpB0J0qml736DayW_C29VwXFmSWS_O4RcZXTWaXnRO7PL1_72IsyMGs7BLD4jJH4fOprUsVstsql8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2qO47-SZK7gofB-YZiwoBZaBQUdRnd_xTJqNF8tEKefGre8ibwcGvKCoYXN6pWSErRnYKJHIAxJuvEpnRWBdE3sk8yiNmTitnT25UutiQ1LAH3Qbu5jKK0wHANHr1LI2toaqZwOcehkek4qWJUupjWmxHOen0zx1MZ0dkyTUCcwZsVOg2Ny-uEvwGcsSk33_9wV7XeziEQLNoVu9Ed9VS_n60J6h188SUXwmCOetoHZsIc3MgBSXSLI-55maQHGbMSkYbMSsLTC5ifOxzLipNIbQMkrUv_7suyx17efNftDT6pY4R7ILBdU_3iMldGjFnu8V8ZjVIE-yAFFaXeBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYwyo9gRqKHOsSTHaF51X10RSiAXuWH9tegkh4TV0OJ7vrmu0k8h_LnsXy3XJee4p6mExF5eS7CV0eugd6b7SNRc12KBqrOeMK_mkpr2X_sRsHa59v8mBj4Gf-AwAisgwMHPkbBmwLCzcufZAVuEzJpUU2lDWEFAHGd3QWEOuT6jTzVQFe7lt9LbqRiqAV4zsrAufVet4JcPCdey1QrohvMJ1sCr24YhouPG3YnDn1_MHzSZhQgp2P5uy1qV6Q9X9776CfLW7LGhaMVkuB9I3u_r0nYBF7ELrydShTa5d77wYRCpyOWNpu1iIW7WmpbBlYmFiHqnUU2NdEDTNLesvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدیث ستاری، مدل ۲۵ ساله ایرانی و دانشجوی دندان‌پزشکی در امارات، در مسابقات بین‌المللی زیبایی «میس گلوبال ۲۰۲۶» موفق شد دو عنوان «ملکه زیبایی خاورمیانه» و «برگزیده مردم» رو به دست بیاره.
+لباس ملی حدیث در این مسابقات با الهام از سیمرغ، پرنده افسانه‌ای ادبیات فارسی، و نمادهایی از حکومت‌های ایران باستان طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/73214" target="_blank">📅 15:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73213">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=nTAr7SUl0VF58knIgjtNqD03k6IBwq3IvRXxdMKSUVweBKt5rwfXiF9UoMqJuBQoMlMY6r_TEmFn1ao_7TEVMgmZyuHOLqPS9ZCQ-hfVB54EqINbYdbSvqS-JGfLM7FfoJyk5zOjnEwPtURljKr6G-E40Yj0kTaDAnw9dAhD8xmACl3CJVQTXzaUa1lNKpIYF6eZNnZh4o4Za4UXkqNsFOhCkgwRAwKaYlbymQLqvhcBpPtIQCTnC3LwaycbongW_e-jpE6i1-zhMeUjzsCx6kxNEKbj12NOt1G_Shu160eUQR4-f7wHEKqoYD-RMpOzSSYzhGIr2GqINzmX5eNhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90850a02ad.mp4?token=nTAr7SUl0VF58knIgjtNqD03k6IBwq3IvRXxdMKSUVweBKt5rwfXiF9UoMqJuBQoMlMY6r_TEmFn1ao_7TEVMgmZyuHOLqPS9ZCQ-hfVB54EqINbYdbSvqS-JGfLM7FfoJyk5zOjnEwPtURljKr6G-E40Yj0kTaDAnw9dAhD8xmACl3CJVQTXzaUa1lNKpIYF6eZNnZh4o4Za4UXkqNsFOhCkgwRAwKaYlbymQLqvhcBpPtIQCTnC3LwaycbongW_e-jpE6i1-zhMeUjzsCx6kxNEKbj12NOt1G_Shu160eUQR4-f7wHEKqoYD-RMpOzSSYzhGIr2GqINzmX5eNhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/73213" target="_blank">📅 14:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73212">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs26GIBfcX5RQ7btjYtUzGtgAmk11946OFVkGbiygoQbyHUhF_qvbrKz3QuTLWsng2cNazqgUOsJiAJhcIhiJsxCivblszyI75VWwz8DPOPDQwJMIaBbNNprOc167bBbTqCHzrX1VlxPWRHCO5DxW2NWIOxoeYepcopw1-1JOcmXwtX4ydzOuREA8RkTZVCZ7wku9_j54SDan6GvuLJMjSdbC1YfeRzzlOqnA6tqyOl2NvWqGXyHTVm8No87w1slkymqNdoBLHzUOsHPpiDnkxmM1TJO-A9OBV4Sv3PZOv6in7VRNixAE-bjgZNbpoTfGDWmiUs08o-JgJrzWLluCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش روزنامه «هاآرتص»، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از طریق میانجی‌گری ایالات متحده به دنبال جلب موافقت عربستان سعودی برای مشارکت اسرائیل در عملیات نظامی علیه حوثی‌های یمن (انصارالله) است.
نتانیاهو این پیشنهاد را فرصتی برای تقویت روابط با ریاض و پیشبرد توافق احتمالی عادی‌سازی روابط می‌داند.
با این حال، محمد بن سلمان، ولیعهد عربستان، به دلیل نگرانی از واکنش منفی افکار عمومی در داخل پادشاهی، با مشارکت اسرائیل مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73212" target="_blank">📅 14:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=XVU8Kkh2t9JVDie0RQFrxiEF8vlYaXqDCciU9jRhYuBJ24IXB9TgH3IijEiTd5yTRcBIS1YqKNiVdjC7aWrzNu-sOuZtW-bZmp5Tu6WQQb-vDGio2NUyeF9Vl8cBwZdLoXh0CRKTOr8IC7A654Ex8bc9W3Mz8v0Ps_xYlMlBHWcgNU6QVIvouuj6KMzHDXPVD3rXeVxjhkGylJWmsr1QMMiyzf8ECMWKeyhS4ckRqdkvOxcS26hJfcPRmkbDizIhf3xBb5-3dI4UQouznZHA50L0aaiKntzB8HTfzCJk26Z24uqWZq5GqmMKtqVxumRXLfvVuNEH-pflOWi9q-fX9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876aa9210f.mp4?token=XVU8Kkh2t9JVDie0RQFrxiEF8vlYaXqDCciU9jRhYuBJ24IXB9TgH3IijEiTd5yTRcBIS1YqKNiVdjC7aWrzNu-sOuZtW-bZmp5Tu6WQQb-vDGio2NUyeF9Vl8cBwZdLoXh0CRKTOr8IC7A654Ex8bc9W3Mz8v0Ps_xYlMlBHWcgNU6QVIvouuj6KMzHDXPVD3rXeVxjhkGylJWmsr1QMMiyzf8ECMWKeyhS4ckRqdkvOxcS26hJfcPRmkbDizIhf3xBb5-3dI4UQouznZHA50L0aaiKntzB8HTfzCJk26Z24uqWZq5GqmMKtqVxumRXLfvVuNEH-pflOWi9q-fX9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت آب و فاضلاب استان تهران: قیمت آبی که به مشترکین ارائه می‌شود ۱۱ هزار تومان است درصورتی که قیمت تمام شده آن ۸۸ هزار تومان است؛ فاصله وحشتناک است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/73211" target="_blank">📅 14:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=OaPgcYsq4NY0bNn62wTAkBq6ooiydug6Z9QslIYTUs_7Jj6FXuNg9JyTDLCIjQWMbq5INir1GOakniwSaY6r8FjbrIqq1WHylLud8pcDALkXkQRvi1E8P0saZ0CHSpIi6t4uqvptuaK793fGL-8f7e942L1qvAuYGPIjjOk4ai7MKy0TEi-LFuXDjdPOwjkj5fZUu8aJa0g7gpaJnuQE04gIFzmmojkhhyYZnzaI9a52OLFWG-ZNq7RqL1uEjDl-s7pgT-xpG9M3ey4v1vs2T1GaLjJ3ZX1W4xHCqWcRa9E_mXekClTopG81kdfiWzeto1M1ZsX62LqOqu42mtligw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54425bdea.mp4?token=OaPgcYsq4NY0bNn62wTAkBq6ooiydug6Z9QslIYTUs_7Jj6FXuNg9JyTDLCIjQWMbq5INir1GOakniwSaY6r8FjbrIqq1WHylLud8pcDALkXkQRvi1E8P0saZ0CHSpIi6t4uqvptuaK793fGL-8f7e942L1qvAuYGPIjjOk4ai7MKy0TEi-LFuXDjdPOwjkj5fZUu8aJa0g7gpaJnuQE04gIFzmmojkhhyYZnzaI9a52OLFWG-ZNq7RqL1uEjDl-s7pgT-xpG9M3ey4v1vs2T1GaLjJ3ZX1W4xHCqWcRa9E_mXekClTopG81kdfiWzeto1M1ZsX62LqOqu42mtligw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو :
کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که رژیم جمهوری اسلامی باید سرنگون شوند، آنها ما را خفه می‌کنند.
ما مطمئن خواهیم شد که آنها(رژیم جمهوری اسلامی) سرنگون شوند. آنها سرنگون خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73210" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=afg_hvOr4ZST9m6IQqz7b7-_0ms49zHmkyeXMMO3ZvFyHjFwDbGWD_SXbyYtSSMFYg9iNsqzTzQRNHjKy1uCmqJAUXzgIobWEQCAWZz4oN-79sIwHPPD6K-7VpFSak9sXZJTASKRB81HOWDxSIx253wspd_NXaaEVijcl4sWOp-RQRgFZuKFT13MpjtQbOL6CUDHca_E_LNpUgfEz642wpWhwd8rXM4F8ZEFgGSvoNMqgwDyvpJxklGXtTEFo1YtNK4MQkZ9d_6WnvNcMNQDdyAVT5FkyyHFMUN-yvjvYwP1MEyzXEmL4bwR7citoCFw8WjZCzxwp5WykeOI00brdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6a75e3c2.mp4?token=afg_hvOr4ZST9m6IQqz7b7-_0ms49zHmkyeXMMO3ZvFyHjFwDbGWD_SXbyYtSSMFYg9iNsqzTzQRNHjKy1uCmqJAUXzgIobWEQCAWZz4oN-79sIwHPPD6K-7VpFSak9sXZJTASKRB81HOWDxSIx253wspd_NXaaEVijcl4sWOp-RQRgFZuKFT13MpjtQbOL6CUDHca_E_LNpUgfEz642wpWhwd8rXM4F8ZEFgGSvoNMqgwDyvpJxklGXtTEFo1YtNK4MQkZ9d_6WnvNcMNQDdyAVT5FkyyHFMUN-yvjvYwP1MEyzXEmL4bwR7citoCFw8WjZCzxwp5WykeOI00brdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جالبه بدونید این ویدیو که خیلی وایرال شده یه بداهه از خواننده و طرفدارشه و بیت شعرش از قبل مشخص نبوده:
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73209" target="_blank">📅 13:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=up-Y6mumYn56DzkBmvgENqutSXF0zKS2ytXbpBlBAohLlXU3gzcxIAWiNuV7J4gxU5zx9qy3EsmHAqWn9Z-jnd7OIkuSVrHwRS40h9VBG7f4vONj5ztStltDjU2DBwJGRIGlEt6B1VgRRLBqXcHwvlUY6ifWxWWpXvRWu-cHKJvoghwPNA7v7rY8OzMPAzogXAJkv-G8TtSCCqfNjnFO8BVCVXUdES5sPo25QvxI3mXRtgaQsXQXTH4mWmBETGCHf0AO_r1qSvVqwk21JQB5ras5T_Pf0JGZuCZitgu63aOZ4MJbN89t79rBpjYbg96hcBct6XyXZuHzv18A_vwK2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96bc792f3.mp4?token=up-Y6mumYn56DzkBmvgENqutSXF0zKS2ytXbpBlBAohLlXU3gzcxIAWiNuV7J4gxU5zx9qy3EsmHAqWn9Z-jnd7OIkuSVrHwRS40h9VBG7f4vONj5ztStltDjU2DBwJGRIGlEt6B1VgRRLBqXcHwvlUY6ifWxWWpXvRWu-cHKJvoghwPNA7v7rY8OzMPAzogXAJkv-G8TtSCCqfNjnFO8BVCVXUdES5sPo25QvxI3mXRtgaQsXQXTH4mWmBETGCHf0AO_r1qSvVqwk21JQB5ras5T_Pf0JGZuCZitgu63aOZ4MJbN89t79rBpjYbg96hcBct6XyXZuHzv18A_vwK2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال‌وش:درگیری در منطقه تفتان-سیستان بلوچستان بین نیروهای نظامی جمهوری اسلامی و گروه های مسلح ناشناس:
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73208" target="_blank">📅 12:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcbUQCF6JWVygh78rPscMP3be4jNhlIv5HxA2G9kgj1SF71yfoHVa9XMz6iq178QCAguSQDswvxM8M7jtvIp-i9ddjcTT8mmf81mlxwq_PNYnEFQudBC6nILETFMAv0EWg6DqrcOlZanwXSkSb8wxqd07KSZGbNrNZ7XZYqlrEFWp9Tr1b-BBAO6-3n7jMYOeC4YVdRaAgvRg8t7lhfDwn0ey1L26lPeRItthILSZuxmvzAjDQDgoUn5oB0GY2GmrZU0bGlTbJD74d4C1v11VqBx4P7WPc6kWlturoWfBwyNmo5n9CwWlTjdTxHGX0NUe6A7OxrbB9ja4dp6gWgOVjqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98721d1ae5.mp4?token=KpslO5CYWeGnspCMC5MIsZwfS0S_a16YBJuHoahfIy0TC_g7SLe8d1YkggqA__8XWvm68Z5rbrhLQ_PY6D64r2QT9n8Q2feqfP38znMgyQDAWil2AN2ioOfhg9BM3TlPYIO3t5sEwRPbjPn0EHuy77dn49Erq6JkBdUX42Mw9UAsmRvnd219gqyukwPubl0WyyTsk2MS2Z7ADTO7PIE1OgDH8Nqp54GQ7KGvXGkkxGrStyF1-WF3PJ4qszuKQhlu4SRIoEBlOJiGsgDQ0_DLqFZQlbzDvcSEHIbmFGmx6qS2ZjceuHrmLsqM6bo_v0asT96QQBKPUyirqHuDezRPcbUQCF6JWVygh78rPscMP3be4jNhlIv5HxA2G9kgj1SF71yfoHVa9XMz6iq178QCAguSQDswvxM8M7jtvIp-i9ddjcTT8mmf81mlxwq_PNYnEFQudBC6nILETFMAv0EWg6DqrcOlZanwXSkSb8wxqd07KSZGbNrNZ7XZYqlrEFWp9Tr1b-BBAO6-3n7jMYOeC4YVdRaAgvRg8t7lhfDwn0ey1L26lPeRItthILSZuxmvzAjDQDgoUn5oB0GY2GmrZU0bGlTbJD74d4C1v11VqBx4P7WPc6kWlturoWfBwyNmo5n9CwWlTjdTxHGX0NUe6A7OxrbB9ja4dp6gWgOVjqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرازشه شب گذشته،  در میدان انقلاب تهران علیه مسی شعار دادند  !!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73207" target="_blank">📅 12:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be338c559.mp4?token=qbBcOcq7HhQgQ7eUh4R7NCeP5iVm6g0glyj1Lz-jEtfzfIxD-Arq-6kDF9VK0bhSWG3drOpPdutza2FRawZFBFnwW61NUfi7MB5yLdUnpsKq--95-IY1gogXECjD7imlFmPuwd01lPuTTclHoE991TQrUjoOvFAuIexyMy9sSV0AzIuyNqnZ0gKsOWuVg1TaJADXxbS5H0jpbXUCNwJvy2Reh8MNBqfJG2R4VjI15RPDq1J7dgIFf5aVnSrSIWMyl30SinnMOR_uTqz1HZ7ENHMfHyEOqHn3k55EBLrXLsT0tLo34KcMZk0A97jluicxXSDqAB-1uEGq5eEA2ZaNuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be338c559.mp4?token=qbBcOcq7HhQgQ7eUh4R7NCeP5iVm6g0glyj1Lz-jEtfzfIxD-Arq-6kDF9VK0bhSWG3drOpPdutza2FRawZFBFnwW61NUfi7MB5yLdUnpsKq--95-IY1gogXECjD7imlFmPuwd01lPuTTclHoE991TQrUjoOvFAuIexyMy9sSV0AzIuyNqnZ0gKsOWuVg1TaJADXxbS5H0jpbXUCNwJvy2Reh8MNBqfJG2R4VjI15RPDq1J7dgIFf5aVnSrSIWMyl30SinnMOR_uTqz1HZ7ENHMfHyEOqHn3k55EBLrXLsT0tLo34KcMZk0A97jluicxXSDqAB-1uEGq5eEA2ZaNuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عده‌ای از اراذل و اوباش سرکوبگر سپاهی و بسیجی با لباس شخصی و پرچم فلسطین و به بهانه حمایت از دانش‌آموزان فرانسوی در برابر سفارت این کشور در تهران تجمع کرده‌اند و علیه دولت فرانسه شعار می‌دهند:
«مکرون حیا کن، دانش‌آموز رو رها کن!»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73206" target="_blank">📅 11:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73205" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73205" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boFu_eAujI2-FqsT0JxHrKNquqgUbTjYReJiXrqScMGPUKoTr2RdTkHsX4PNrQ1kbUsR6Esli2ljvhNAIsowBpMeeaSlpuJpDWedldxSBWxLkjt4CId8K0YeCRi6jdRNj7XlThtUzB3G9Yrdm1KHQHpQM-NkXqt66CA1C4zzkFMPFV6nM9p4asf2NhWpQPCfBUT3Wg_hj6QqDcLdVO7oF4P2JcqS2qyHy441KpIUOP5DtHzfXZFheU58nNdaMclzqjh_iL0E6zMiAjHkvHQintgE27Q_1tsSG_HNy1eCInHn9XQqc9LW6m3gBS0Z3q8xr8UAcVkl0DJp9gSY-oL2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بارسلونا
🆚
گالاتاسرای،
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
🦖
گزینه پیشنهادی:
بالای ۲۸.۵ شوت در مجموع بازی (Over 28.5 Total Shots)
با
ضریب 1.64
📉
با توجه به سبک هجومی دو تیم، تمایل به خلق موقعیت و آمار شوت‌های مسابقات اخیر، انتظار داریم دیدار گالاتاسرای و بارسلونا شاهد موقعیت‌های گل‌زنی متعددی باشد.
📉
بررسی ۵ بازی اخیر هر تیم نشان می‌دهد که مجموع شوت‌های مسابقات آن‌ها به‌طور میانگین نزدیک به ۳۰ شوت بوده است. به همین دلیل، خط ۲۸.۵ شوت می‌تواند گزینه‌ای قابل بررسی برای این دیدار باشد.
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73204" target="_blank">📅 11:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پرونده کنکور ۱۴۰۵ بسته شد /نتایج نهایی اواخر آبان اعلام می‌شود
با اتمام مهلت انتخاب رشته داوطلبان، پرونده کنکور ۱۴۰۵ بسته شد و نتایج نهایی اواخر آبان اعلام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/73203" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_wyPfx7-aQE-Bf4dKZGyEn1Qz0UdB9DDageaz9B_urTc4LFA88forQizT8CQO7L0PURt1GYLe_W3B3f5jvJiHUcAkRJMvF1Po1ZAvjjnUtkboMLnD30xCP0w-fdgvRRiO1eATEI2VLd4TW_t50v8IfIHvAywvsA_lMpjwveiWDdJQSsCAp0_VCOHlPiSOA2irJFCuStxDgNdPyTBQwP3zhdZGdqr8zMGsT4RgL82NEQEiwTzKWRF5fZbbFKZ0JF42POUrbLKktMRbburWteYq_ZTcIEI2W6gRx9rlWcJLoj67raq0U1R6i9FbVqwenbTy4OYLxJURpTK2NI8ONmZdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31f93a352.mp4?token=P1UnLQmxfoOJsoW3nIPX6zykOcg7B64a5sGqysgkjE5ushDpu1XOCC0Pzm6r264_J6Mqvt6-0rh5tAkQ7XwlHULiQcZSjs1Mo7HYevVQzgSKsV4xxUpqd2TO48xn18oaUGPAUQu8Lp53It2Ihw5UolaWPxlT10uJVNTvSjmu4mfqXhT9V2UM6DZBojOPjsT7VlVnT-42LAneFRG4925ffGvwV_JsRTgQ5Xlia_hw08TUD3mwDKMzcEMP6UzIgOjnNYQpkxlbpWvwNgnfrdyhnmqCrke2qm45zvvy-qwyijAEi-W0TQh5VVDYZl2HjFCStdy3kjiJvG3F3Ba4DUlc_wyPfx7-aQE-Bf4dKZGyEn1Qz0UdB9DDageaz9B_urTc4LFA88forQizT8CQO7L0PURt1GYLe_W3B3f5jvJiHUcAkRJMvF1Po1ZAvjjnUtkboMLnD30xCP0w-fdgvRRiO1eATEI2VLd4TW_t50v8IfIHvAywvsA_lMpjwveiWDdJQSsCAp0_VCOHlPiSOA2irJFCuStxDgNdPyTBQwP3zhdZGdqr8zMGsT4RgL82NEQEiwTzKWRF5fZbbFKZ0JF42POUrbLKktMRbburWteYq_ZTcIEI2W6gRx9rlWcJLoj67raq0U1R6i9FbVqwenbTy4OYLxJURpTK2NI8ONmZdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«شاید در برخورد با رهبران ایران زیاده‌روی کردیم، چون دیگه نمی‌دونیم دقیقاً با چه کسانی طرفیم!
راستش رو بخواید، به‌سختی می‌تونیم بفهمیم باید با چه کسی مذاکره کنیم. فکر می‌کنم زیادی جلو رفتیم.
می‌تونستیم همون سطح یک متوقف بشیم؛ رفتن به سطح دو و حتی دو و نیم، احتمالاً دیگه زیاده‌روی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73202" target="_blank">📅 10:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=EWJS0RyQEj5wzQ5FODIB_fWb0EgbvTj1obXe9B5RXYRJJ8HoemCuvTZzKQyJMnyYYnCz68VP0jKO1i2W-FtS7fNaG00p67Cm42CgmAhLThDoyuG8UXiOF3xTNfldqtS-reYn1j90DADQWaSiDgzW_xR3k0GfjuSXMaB8VfCSepSCBN58BRlMXmh6RHB5lwcsKVWPuGHJm34It6urvP2Cfnd5eSPwfziSvQZWWiHhmXEAy7iRUUT5r8HaujDcvbeJfJdVf3HoPkr2rxUxe22HnlqP-2Mb5M7_feQWiCuoLYKvlhFa7aGwvDYyzNEOSyyQVZzzL29yXtwnt_6LG6oKOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec03fa2f2.mp4?token=EWJS0RyQEj5wzQ5FODIB_fWb0EgbvTj1obXe9B5RXYRJJ8HoemCuvTZzKQyJMnyYYnCz68VP0jKO1i2W-FtS7fNaG00p67Cm42CgmAhLThDoyuG8UXiOF3xTNfldqtS-reYn1j90DADQWaSiDgzW_xR3k0GfjuSXMaB8VfCSepSCBN58BRlMXmh6RHB5lwcsKVWPuGHJm34It6urvP2Cfnd5eSPwfziSvQZWWiHhmXEAy7iRUUT5r8HaujDcvbeJfJdVf3HoPkr2rxUxe22HnlqP-2Mb5M7_feQWiCuoLYKvlhFa7aGwvDYyzNEOSyyQVZzzL29yXtwnt_6LG6oKOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند شب پیش در تجمعات شبانه تبریز، یه دختر توی ۲۰ ثانیه کلاشینکف رو باز و دوباره سرهم کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73201" target="_blank">📅 10:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دونالد ترامپ:
«شعاری که از همه بیشتر دوست دارم، «همجنس‌گراها برای فلسطین»ه!
می‌دونید اگه تو اونجا همجنس‌گرا باشید، باهاتون چی کار می‌کنن؟ از بالای یه ساختمون پرتتون می‌کنن پایین.
شما رو می‌برن بالای بلندترین ساختمونی که دارن؛ البته ساختمون‌هاشون خیلی هم بلند نیست، ولی لازم هم نیست بلند باشه. از بالاش پرتتون می‌کنن پایین. با این حال، من مدام می‌بینم که می‌گن «همجنس‌گراها برای فلسطین»!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73200" target="_blank">📅 10:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73197">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CK0mCHpkcpeu4IAg7wTm5px0fPxfYxIiOUg5P4Qab431EiE6X8Lw1c-_LlRtswWIccoBQG32HFufs46JijKVL8xOwCHSzp9zm5u4NWWlzsnMN99BOwJRpQOtztvZGv5ZEj6wrq4JrMnu9OmeG03JsWhz-IblEHhJTRUkwg0lKIlLm4YchbwMJZv8WdTk4Obfs5aTDffkbLJa7YZMatzqyp8Wx9aYsx47b7GoeJgZFqCp4eGz5od6kPypgEEe7xYBalIk5jd6Ex0CFW6Ptbq5-1rRX9KxB37JtjqdpVxXLQxeZQhwQ2_kBbitXDj5dbyRd-E8_qOoGg-2X-oadtvVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JxAo1G2_b3vBTF00xDOlV3vdo_tAhSrLLvgEYcRJxOY5_hV2-w3rs_TtCpH9xL-b-MjdfEo3WJXFGN7KhJxhMP9Py4A434Dof7ZxAnx_7aHY0mN4YK4HDP11FuNWyqw6QBZU_4V5-9n6d0P0hzC3HZBcPS8yu9cFX2Kl4QJdJmvW8YqEUnC6ke7TdlS8M1UQGZ1nHdpsUJOqkE3Mf_XGkMyC-gVIy2LAX_bTX-ZsE7ojH0D9SeNt1zFKYT31JRqbeo5YNxlPGO1o5Lf7CBDiF9YMP_4-92XMNv11Yw6dHUV79t8So0gEXt4k97U_T_Uda6uDggdt_I8rNPv1pfdTPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/352c619970.mp4?token=G7j5vagj_dhWhb2zArOE71KdLsZeSgClzq3FVJGB-JhiEzeTJcj0aJBZauPY4WU6b2F0cJzzJBM8gTT3XkLc2Uh_RDjioxs6t9EiMOeDVpFBC2VKiV1Y46H2X2A_92GR1jU68J2qEET3XEzObQab6O80vzMWO9jqDly_orZfcwkw1xkiDC-x2lIS6Q54QZU0pFzWeXEsqzc9ZI_3UHgwVRsAQTI6-jhv3CD9NgVTlrs_Bwqr67gdNO5HDK8UqkOoowV9Z6TxyYnb3aAblggAmzvBQ9P5FJU3TWaKPa3E3lbbkHJFxvyKlujIF7QNrxhtn7Zy2UyQYQdgT8jf09l49g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/352c619970.mp4?token=G7j5vagj_dhWhb2zArOE71KdLsZeSgClzq3FVJGB-JhiEzeTJcj0aJBZauPY4WU6b2F0cJzzJBM8gTT3XkLc2Uh_RDjioxs6t9EiMOeDVpFBC2VKiV1Y46H2X2A_92GR1jU68J2qEET3XEzObQab6O80vzMWO9jqDly_orZfcwkw1xkiDC-x2lIS6Q54QZU0pFzWeXEsqzc9ZI_3UHgwVRsAQTI6-jhv3CD9NgVTlrs_Bwqr67gdNO5HDK8UqkOoowV9Z6TxyYnb3aAblggAmzvBQ9P5FJU3TWaKPa3E3lbbkHJFxvyKlujIF7QNrxhtn7Zy2UyQYQdgT8jf09l49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر دانش آموز ۱۶ ساله از اندامش فیلم گذاشته و حالا کامنت دخترا زیر پستش:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73197" target="_blank">📅 09:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73196">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=fRRiqpbZUFWnSo_vzSPeJoAuNRQo3XzslFkI0TxfygOeSDNBPYKeJt2BjdC_LWnM_2gsWwxz2opiEHziPshVYNuZ25cePNpJGl-oCCQYY56sf5F5-IkL9XvY0lN1C6Uryr58l9GqNKpTPMPQxI7LOFHfnVleUGzgMYqWUlb5KWNx49NkicA7dCVv2Jlb9DRSFfQgROgPAxWra4rxyzrxGOYJLtJBm4nTpcD7ZE5T3qsnfJQXgtTQTSTE_JyQONlag3TImNnfLtWgZ50EbDxXkmZA1gLhGLBSPvKQSJW4Z_or70Woe_x_dRdzz8cOGSG3YAzR0WsJVkO-1y3QZZxndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a7342c7.mp4?token=fRRiqpbZUFWnSo_vzSPeJoAuNRQo3XzslFkI0TxfygOeSDNBPYKeJt2BjdC_LWnM_2gsWwxz2opiEHziPshVYNuZ25cePNpJGl-oCCQYY56sf5F5-IkL9XvY0lN1C6Uryr58l9GqNKpTPMPQxI7LOFHfnVleUGzgMYqWUlb5KWNx49NkicA7dCVv2Jlb9DRSFfQgROgPAxWra4rxyzrxGOYJLtJBm4nTpcD7ZE5T3qsnfJQXgtTQTSTE_JyQONlag3TImNnfLtWgZ50EbDxXkmZA1gLhGLBSPvKQSJW4Z_or70Woe_x_dRdzz8cOGSG3YAzR0WsJVkO-1y3QZZxndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از ساختمان پلیس دیپلماتیک در میدان فردوسی پس از اصابت موشک در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73196" target="_blank">📅 09:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73195">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73195" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73194">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/news_hut/73194" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73193">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: انتخابات میان‌دوره‌ای آمریکا تأثیری بر سیاست من در قبال ایران نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73193" target="_blank">📅 01:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73192">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=eVc6keTcClFH1Y1X2kBfPt6o4nNLOBAI50CXSOekww9Ly-uAUvoYfv0jDcSlPF9vMTF-cRzJoCgus47RBE8ffSESERY2sFjqUGwwZcasEGohvXLp3AII3uvPEGFcXRtMWhmxkUoH9v11W-1aoSLtKgbo5HEMz4aCF-OLYnhnals577rCKqhYOmpfnFtXg_C7t8oEFsEt7Aeqc3H0gsTJYgWZF8hYOI4EH0TC1q1J1FPgJZPo8TWdpKH6HKk_5bof7bPfJrfiGQWlrtGt2zGxOA0BnDTLfz5duHY-sA_FmfhQaqOLxzBhZwKGZiRM1kWrY82sgiJ7IzzLzyiwFnxzLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=eVc6keTcClFH1Y1X2kBfPt6o4nNLOBAI50CXSOekww9Ly-uAUvoYfv0jDcSlPF9vMTF-cRzJoCgus47RBE8ffSESERY2sFjqUGwwZcasEGohvXLp3AII3uvPEGFcXRtMWhmxkUoH9v11W-1aoSLtKgbo5HEMz4aCF-OLYnhnals577rCKqhYOmpfnFtXg_C7t8oEFsEt7Aeqc3H0gsTJYgWZF8hYOI4EH0TC1q1J1FPgJZPo8TWdpKH6HKk_5bof7bPfJrfiGQWlrtGt2zGxOA0BnDTLfz5duHY-sA_FmfhQaqOLxzBhZwKGZiRM1kWrY82sgiJ7IzzLzyiwFnxzLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: بعد از اینکه متحدان ناتو ایران رو به طرح حمله تروریستی به پایگاه هوایی فرفورد بریتانیا مرتبط دونستن، آیا قراره اقدامی علیه ایران انجام بدید؟
ترامپ: «باید ببینیم چی می‌شه. اقدامات زیادی در جریانه. وقتی می‌گید اقدام علیه ایران، (باید در نظر داشت که)اونا دیگه نیروی دریایی و نیروی هوایی ندارن. تورمشون هم الان به ۳۰۱ درصد رسیده.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73192" target="_blank">📅 01:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73186">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DTjx64I53ZNfVWWRV0Scz0CjAvLrJWgB8gMidX1A9RnoF-pkyuzwRqJ5WCsEMl1zXUoXHb6g7J9uFf7y0mcwxioquTEKHcE5_4klELxV5BGithk_tg0wclPNHDmz-uykWZMWcW90RgJXOkJDUeuSZRd_3G_OXnp3TOEyCFv5Mr2Laq1JZhXLydREHH0mGBiE7pf-dOkF791JhISwOaDKio4K6E9299cIf8937fvdKdQtsA2qWTmJSdOwL6kJQLlfFWo7luk-2Z8sCW8u0u82vZ5OryZ1Vq4fDO9UhssnXXaAVTOUeOd8sEKlBojT7wxaEm4IRuugsWJl8-FzdEZz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LwAx4Xxonmz5-7yUUNDJISADFxTMsoemWYVxOGEbt2Qa2CQynHg0JMRIUdytTtNTrH4wyTdKC2J6pot_3_uzmigLr42H_F5stg5hVX43Id4tehdcADojgFuJI6FQGKepVwh0j2guTEZnFYCle6lGY5EhQnplyCONm9TeiyARJYZQrO-9W54h5cPRq_ms7DwcLHPDA43hn0CRV2VNBzMuK5MAZC4NsDXt4XBy94U1NtTl8KbiezD8C2f1hVYvYl0gOAKuzKj8kow0ut349iqX1ym9dbWS-U7TaTQxCxv4WEhtU_xjgYL9bwDLslyn04t8yTk_MVaLka_YHhaBcBp9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YTsZpEfgWoqNygcR4L5s827M0Jog32mHQXbCKrZdmaZqq-vcukZx35_gxA9sfhLjewaXZkJKrmwRTcenO8SEp4aK_m9ipMnHGc50rdf0Oa0z-kkSm6dve2dbmKoqcrULevMZqkKHius6pP2bTLE1YItAEi7CP4s83uqFTy1MCH1rhI-7oKkEnWIX3oPpliIRX1LpU73PJcjYvr0Oqzp7JDXPpphdZgCmjSqkN9bZzv2iao6o9vcBYp94VC2mGoNFLodFNfecxXXvE-SdDuQZVM1u1QFzCrzp6NJ5hLRyrktP8nYOVAUAqPt1uIHkWWER59K79nNvPZB0lWZY_EvpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n4xcRyYY4kVSh9Co3UpqDmrg5YQKVmTUTTIpfirHgSRrh4wIimUgmFMdX2vL5Sbm1Ult70Libqw8CGa9V9uhVCbRDpLIqVwhawOl49UY0-Ej59Wk4fPOL_LzHGFnpgjrtnyIvfQYCbgfOf5pgAjvgr531cp13IfssYIzZQ2jmqG7T2NE_-WjBfPIKk7eCiy-PziAC0yh4EL5U-3_RWYZt_5E3BftxRkFD40KlVsS8kIkBHPKb6b-tzIF0gWhibLdNjdG3AixsgPBsf_oE2OT2d1hFku8wfg5eDDHgmaEARYL8nM6U5kym2J8f1tF5--gjBNooANokOQ7V67WlPmflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ben0rVuT5Ulv30sPKzJ5Qy8KvvBbGetRAtIU-jJtqweitBEGsIKI8JzOm0pFut9lyHA-RfY2kI7Rt9z4PZA2_dkCXLDJTH4owiIz8PG2GkQrRO-giQLbSkwD9xX-tWQgGLGrw6B0JDdFq5YQeh74NVrjnBLk016yfuE6ZM7zTQqR0r58oVJfQo4kEwEGPKyOPTn29cHdmbmXYuxavYCn_zWmdlEJ2AYM8j2oxXtZI1AAsWZn-DyaXQwnc1w7ZcjND1PbbIYqFMt-Z2dCp0eKRcxn907lmOTknaEaYSsoU7lUzgCn_TnKHgXsCj-PzkRS52mHjycwK3BAt5ghaTQC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UeDi-iHRhLt_wKKvYUfNRlkH8ep_gjpEIhWNXzB76yNK8N-3HELOW-kmYsaSqsHMF0wIuwJAhgYdf1HepAKPL3hPPjldCFarHoRIEZWafgWaGZU74AT3zEqdUHabiK-91Hx6obHHLwGF6rXJV-Jjv_08mxb5cY-KYv18pBFPNsI5lMT9FF5WhVRNLjzrqBZuLbM379cYoKTyiWIGyEw25wRD6IWPqtwW88Asza0CZoccrq8z4SVTLgC-CD-Kfi2n-SuFwkq8DtwXjQXbMU_YMRrfNbEArItvJcB21d7L9YDVr_4vHoUyHGO0bOgOHPYw1SN8w_2F_3WSJZXnsyyc-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ۲۴ساعت گذشته سپاه پاسداران به پنج کشتی در تنگه هرمز و یک کشتی در ساحل عمان حمله کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73186" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f60941af.mp4?token=kFxFxn2eU2HfrnWNGxnanzE73jFPgeJ9E87Cpj75niH8GxtXAkdzZb0NIE-VIruXLmsTd50Gps8RVBlvcKG0yOIuhFz_R86BAr2qVZy-wQc3tSxSsLGETKTf6hy3Gk62aAl0vXVJJ2iF1hvGleKZCtm60N7kZ2B_-hFsEX_2FyJnbBkmG7QjsiaNzyDMwN1epFvdwMPDX42SP1HQ9Zf4SykXw9tAYvxZeJllzIlIcsQ1RhaoKkh3c7lPYkseQaJnErI9hMaNZ2QvhFf8jdW5_IF_MnkHgkmoAqbEEMps6ldmedUgU8nZ5l7b_D_jEdiZbmC4IK-_LAyGGs5vxsPY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f60941af.mp4?token=kFxFxn2eU2HfrnWNGxnanzE73jFPgeJ9E87Cpj75niH8GxtXAkdzZb0NIE-VIruXLmsTd50Gps8RVBlvcKG0yOIuhFz_R86BAr2qVZy-wQc3tSxSsLGETKTf6hy3Gk62aAl0vXVJJ2iF1hvGleKZCtm60N7kZ2B_-hFsEX_2FyJnbBkmG7QjsiaNzyDMwN1epFvdwMPDX42SP1HQ9Zf4SykXw9tAYvxZeJllzIlIcsQ1RhaoKkh3c7lPYkseQaJnErI9hMaNZ2QvhFf8jdW5_IF_MnkHgkmoAqbEEMps6ldmedUgU8nZ5l7b_D_jEdiZbmC4IK-_LAyGGs5vxsPY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: انتظار دارید جمهوری‌خواه‌ها مجلس نمایندگان رو ببرن؟
ترامپ: «ما عملکرد خوبی خواهیم داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73185" target="_blank">📅 00:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=eoSVzqBssenEdo1LmNKAKy6bBpSmo2PgIysbUadvW5b3-Jr99FPtYgIEMihvwciDSbDmwsagQlF4JbthIPUoUwXqHarzW8eSnJxi1tEPxWgtRAMAUzuH8up6d9Jz6HNZcVsQBRepOyJxdnqZMKQXa0TZDV6eWP2SsfcMGRItnJg37jLLoXbTErR8PkqbGZLYOi_AyeQPVfD4vF0qgNM15emUnuh49ZZuKETEnlq98GAN4bKZEz9Cs1XpRTYaCKfSNUjtiW6xUGc6MtEW8P-Xe3RmHoYP3PcTrAXhAMAKqSMJlf_9y_gXnpxowX43KbZVwUD_h6xX2slV1ihCFgmc-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=eoSVzqBssenEdo1LmNKAKy6bBpSmo2PgIysbUadvW5b3-Jr99FPtYgIEMihvwciDSbDmwsagQlF4JbthIPUoUwXqHarzW8eSnJxi1tEPxWgtRAMAUzuH8up6d9Jz6HNZcVsQBRepOyJxdnqZMKQXa0TZDV6eWP2SsfcMGRItnJg37jLLoXbTErR8PkqbGZLYOi_AyeQPVfD4vF0qgNM15emUnuh49ZZuKETEnlq98GAN4bKZEz9Cs1XpRTYaCKfSNUjtiW6xUGc6MtEW8P-Xe3RmHoYP3PcTrAXhAMAKqSMJlf_9y_gXnpxowX43KbZVwUD_h6xX2slV1ihCFgmc-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید روسیه و اوکراین با آتش‌بس موافقت کردن، اما هر دو طرف می‌گن چنین توافقی نکردن.
ترامپ: «موافقت کردن. می‌دونید چرا؟ چون من گفتم: شما موافقت می‌کنید! دلیلش هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73184" target="_blank">📅 00:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73183">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=VE1oWOeUaAiLf3H8qQ8HYcM-Mqy0NGoANfawt7DCzBGnr2piJ-buhE-bEY-tQHMGoJRgGzfZjID0O-ykT6CHTyfRb53LnACS0o6w4UrtJAwqeJFNEyogLJetjdyxSe6tEf8Uor6Bzti_a37g3hvPi_MjCCd5T17_HIIXUOAJ-bY_tu-xDe_IqVe8fYnt4reRDQwBUK8F6x4l07iUbzrItxhxzS_YFPFBUO9gGAVr5u8x3QLBhy4PWuzDaMxGHRkzjTnT1CHYUlq01Ye31rwmhmlOcX-00owXmK5QnBBsoy9WuIUZJIlHJBrz4qxb6zp6MFH8Muo8U5qkvDj7oCADdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=VE1oWOeUaAiLf3H8qQ8HYcM-Mqy0NGoANfawt7DCzBGnr2piJ-buhE-bEY-tQHMGoJRgGzfZjID0O-ykT6CHTyfRb53LnACS0o6w4UrtJAwqeJFNEyogLJetjdyxSe6tEf8Uor6Bzti_a37g3hvPi_MjCCd5T17_HIIXUOAJ-bY_tu-xDe_IqVe8fYnt4reRDQwBUK8F6x4l07iUbzrItxhxzS_YFPFBUO9gGAVr5u8x3QLBhy4PWuzDaMxGHRkzjTnT1CHYUlq01Ye31rwmhmlOcX-00owXmK5QnBBsoy9WuIUZJIlHJBrz4qxb6zp6MFH8Muo8U5qkvDj7oCADdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: روسیه همین حالا آتش‌بس رو نقض کرده و دیشب به اوکراین حمله کرده.
ترامپ: «در این مورد مطمئن نیستم. بررسی می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73183" target="_blank">📅 00:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mK_0D0VfvR5cMRA3gtSAtWTHL2lP1Gso4g7fmKmlLEaDk2J6BkVWN5hTnHAANKU3LbBdEt0BOBCueHzSDi0YVj51LuA-NfngWWa2w2djhx2FVvyxgn4fD3Gtj1PTFLSzLijfAb5IMYw8WyacOSZaGyj7FqZYiYRhOCAz_9OnD7dbrvp5UkCQZ4JB0iQtYpTdyM9RF4nd022G5-iI-tlmevuCT10Ow4-PrFIX1MZuOFr5eT47WD_gtDMPABIV1x-0dWZgp3eagYD8j7euUOHIr5bCT6r4gQ0-d2fEyQiSBRPh1pPYAREDeFkacRmxHfOl4E8NGR54Urmk7KlbxycWxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آر. جی. میته، بازیگر آمریکایی که به خاطر ایفای نقش «والتر وایت جونیور» در سریال محبوب «بریکینگ بد» شناخته می‌شد، متأسفانه در سن ۳۴ سالگی بر اثر خودکشی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73182" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a66098169.mp4?token=IwUZeLdxewvrFNorK_z3eUzm51-X9ZtO89hQGSsvU8gi5G4qIVczyXHj6bHsMWPtuyvCU08gUiBd1UIYVTgjJVVSxAOSRmfYvk5bzLZ5P-OA6dBJodJRmNyijHLQfRn2siQILxkXoVhFnZYk7w-HlFtVm-EZ4c_Kpd-vbgybxC9mI5bSZJMg1sTV1JWq_sBrHqa-NSzXQ1vIvqGm9uFOBT0UZeRFXUCh5BrQhD1UtzikLIC7kuanQEokbXEiUnNbkjicWCGKSVrFBLhheezkw2D1WObNVJtVZExCNd3BOl6jUVmsy_qiQsfnG-DGKjIe_zZxoioXGR_pBGgGoGdcPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a66098169.mp4?token=IwUZeLdxewvrFNorK_z3eUzm51-X9ZtO89hQGSsvU8gi5G4qIVczyXHj6bHsMWPtuyvCU08gUiBd1UIYVTgjJVVSxAOSRmfYvk5bzLZ5P-OA6dBJodJRmNyijHLQfRn2siQILxkXoVhFnZYk7w-HlFtVm-EZ4c_Kpd-vbgybxC9mI5bSZJMg1sTV1JWq_sBrHqa-NSzXQ1vIvqGm9uFOBT0UZeRFXUCh5BrQhD1UtzikLIC7kuanQEokbXEiUnNbkjicWCGKSVrFBLhheezkw2D1WObNVJtVZExCNd3BOl6jUVmsy_qiQsfnG-DGKjIe_zZxoioXGR_pBGgGoGdcPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالملکی؛ وزیر کار دولت رئیسی و عضو هیئت علمی اقتصاد دانشگاه امام صادق:اگه گرانی رو در نظر نگیریم، هیچ مشکل اقتصادی توی کشور نداریم.
+اگه ۴۷ تیم دیگه رو درنظر نگیریم تیم جمهوری اسلامی تو جام جهانی قهرمان شده
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73181" target="_blank">📅 00:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بریتانیا دو تبعه ایرانی به نام‌های «روح‌الله بازقندی» و «شهرام علی‌رضا تمرزاده جاکی» را به اتهام دست داشتن در فعالیت‌های اطلاعاتی ایران و توطئه‌هایی با هدف قرار دادن افراد یا دارایی‌ها در بریتانیا و سایر کشورها، تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73180" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXm6MRVOhFA14GsdxNQGVCUgKgJGGZjLM9KLZZdQRK3KKtPAJ_ag6GPUovZ4pbvUEUqedFPryYLwj2k8srwCgRwd3FOScS3WRrnC2wXZBh-U_XBA8ig6LAKYWoXk_BfGSS1QSDeuEokU-iYImLWbEtJWtPWrSmSh5VrQIVh-X8PtIo-ErHZIMqT-3GABWfJAPTXQJos0bS2mc9Xl6m_sOE3CbS_sG0fIUlDpIwGfVFfz3eIUHfV5VqhiF7UoOHEr6vzP4X1mPTdk9HUlEH4iOySo3kDB6_JcJwOqSS-27tXV5FDG0UtjVDHKaW_ySkzcXWsk69awGTVIkuGMdqG8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو امروز لایو گذاشته بود و خیلی جدی داشت در مورد انتخابات اسرائیل حرف میزد که یه ایرانی این کامنت شاهکار رو گذاشت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/73179" target="_blank">📅 22:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73178">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=u63AcIVDKywQRMgDxH7LskiyNgURlBPPkv8B5Xo3bTTspEU6Y4NXwLCxA_IsL35lmpvBW9cKFrOkTnv9sxX5zXReR6VOw489YIYHyjHLPrDdfAchWGNUKZNxmG8a5hQ0iZd6XRk4k15WOs00cHGfrayguRq6-lWAj8XPNRbM98LdmflHBq9S2Eh4TS2RTwPM5AJIEG5oFdjfIElWuBSINgC_Sgt9DQYTaSj9OP38turu9KVk59ZeXfxMpFbt3GcO5AGaE_u7endwqPEnlPhnbe8RSx-3_xwxbQ88hJENDiW20sreJ6gJwcoVR47_x8dMQe3Ng0sOIYt3SM4MgdvIFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=u63AcIVDKywQRMgDxH7LskiyNgURlBPPkv8B5Xo3bTTspEU6Y4NXwLCxA_IsL35lmpvBW9cKFrOkTnv9sxX5zXReR6VOw489YIYHyjHLPrDdfAchWGNUKZNxmG8a5hQ0iZd6XRk4k15WOs00cHGfrayguRq6-lWAj8XPNRbM98LdmflHBq9S2Eh4TS2RTwPM5AJIEG5oFdjfIElWuBSINgC_Sgt9DQYTaSj9OP38turu9KVk59ZeXfxMpFbt3GcO5AGaE_u7endwqPEnlPhnbe8RSx-3_xwxbQ88hJENDiW20sreJ6gJwcoVR47_x8dMQe3Ng0sOIYt3SM4MgdvIFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض به تاخیر افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73178" target="_blank">📅 22:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6Bxw_IHG1XYJdTP7Ze-QBKYjhMLezdj71R85sBQoNf9fc5gelrFSyJiJrsz6_fx-JSjgnNxPoVb87vmLF5kLAr9FMHC7YUcmtmmmUdYM6nstZiexhgp1vFA8BdXadDvHF3KBpZYOKlfelIBvmMIzgabLdG-OpTtazn-Jj6WnxheZOfhwQrYXMeUcGMzrNcGf0pwHFNPnbzzWfzzPtbk4CgagPyXbiGzzjWycmR_PQQCeliodzrb4c7bzGD9AOT4GL_xGms8f5tNY51_XaVi1-DckFl1Db9BP1xuJmyuL6PS8ZBZ61_wA58lP8atUdzYzfoIU43abXb4aDxMXx0LYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که یک نفت‌کشِ حمل فرآورده‌های نفتی، هنگام عبور به سمت خارج از تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73176" target="_blank">📅 22:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=acmKjeEZPIK789oz7Ambuw77mTpLzdsp2EeYv6c3rxSMBQnFxd-eDiHARgbPI7Qn6LH_HdVu6KXukh7JCYJlRsVZNAX9amzJTDK17VM7noWho_XIYa05BZaLqruTNCDUMt3I8TA9ID8373O3JrInJTSMwlFTQC8ah0w9Mc3YHjsT8JHkXQKrHS9bV8KmUwjycKNL4hSEzZfFdqZ59UwKaRUC4z1yf-PIYR873qK2CzUTA5cz4i2Qx-Lr5_7kssxA2MSvozrvIVDgWuZusH45MqfJPLuD5FxmmTkAkFZ2Qnf5WBL49rgAYGpAl_LaCL86KbYer9gI8WbFQs9OdPQ6RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=acmKjeEZPIK789oz7Ambuw77mTpLzdsp2EeYv6c3rxSMBQnFxd-eDiHARgbPI7Qn6LH_HdVu6KXukh7JCYJlRsVZNAX9amzJTDK17VM7noWho_XIYa05BZaLqruTNCDUMt3I8TA9ID8373O3JrInJTSMwlFTQC8ah0w9Mc3YHjsT8JHkXQKrHS9bV8KmUwjycKNL4hSEzZfFdqZ59UwKaRUC4z1yf-PIYR873qK2CzUTA5cz4i2Qx-Lr5_7kssxA2MSvozrvIVDgWuZusH45MqfJPLuD5FxmmTkAkFZ2Qnf5WBL49rgAYGpAl_LaCL86KbYer9gI8WbFQs9OdPQ6RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از یه مدرسه پسرونه!
معلم اون جلو وایساده داره درس میده، دانش آموزا دور هم جمع شدن و کله‌پاچه میزنن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73175" target="_blank">📅 20:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aek3nq_yZizaI49kAKQs5YXvzfYS-SpA4atNZk-nWIanNCO9qPohBnsqv5IokKQQoc6rexgZGvB0-NQrkLOLIf-wZ3OIHL4P_0cREwn5Nj5lB073-bf4_Uur6eCP87JgQobVmfK1NuySdtqpLx2vDY8O1oYW0lpi4XrYVogL4Nwt8t7eZQPWex9U3oAXViEAjfkI-7WglHuybwX8q_J_JpV5GLcyKHH_keudlui3SkccyAyWzSxAgWQyAvVZw5fVDj_Y51fpxiuCOU72pqUHP3vxYOZvnn_8qtxNRobGysff4ir2Ou0DIKbL8BoM9Ach6Na3SWXqXI_vTrjUWYZsPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار تصویری، اعلام کرد ۱۵۹ کشتی ایرانی در دوران ریاست‌جمهوری او نابود شده‌اند؛ همچنین مقایسه کرد که در دوران رؤسای جمهور قبلی این کشتی ها روی آب بودن ولی الان کف دریان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73174" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=CAmHn43P6xMFMcuefIi7nWewY-e8zboNCoXVfnQo2dWJHXUm90s84r4GaFeCtgwgg10NLUuqZO1VQf3-ZD77yGbZ_z3zi6So7OYLJoUc09yxw6jh4IYJDhYRIz_F_Spw5FG_dJJVFvDy8Z-03GS2ld6QTBRYyFDJf2GZaRkBDwb0dJ7EXJu9OLxgdD5BdbhRp_JyAQCJnV0i1TZDcmDwBIXZ-IR1s31VqDnumpsaTXbkQZL97y8cIs-5WSRd8ZzUaCj9ObR0HhHGjna1c2Bc3XzyhABIUtNPzyyetzdBTMUTv6LJ8uhfZMJuryvAN4SRFbV85BrvUp4902xi8cfS_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=CAmHn43P6xMFMcuefIi7nWewY-e8zboNCoXVfnQo2dWJHXUm90s84r4GaFeCtgwgg10NLUuqZO1VQf3-ZD77yGbZ_z3zi6So7OYLJoUc09yxw6jh4IYJDhYRIz_F_Spw5FG_dJJVFvDy8Z-03GS2ld6QTBRYyFDJf2GZaRkBDwb0dJ7EXJu9OLxgdD5BdbhRp_JyAQCJnV0i1TZDcmDwBIXZ-IR1s31VqDnumpsaTXbkQZL97y8cIs-5WSRd8ZzUaCj9ObR0HhHGjna1c2Bc3XzyhABIUtNPzyyetzdBTMUTv6LJ8uhfZMJuryvAN4SRFbV85BrvUp4902xi8cfS_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سرباز روس تو خط مقدم، سربازای اوکراینی رو که از پله‌ها بالا می‌اومدن، با نیروهای خودی اشتباه گرفت!
وقتی اوکراینی‌ها به سمتش تیراندازی کردن، تازه متوجه اشتباهش شد و درگیری از فاصله نزدیک بینشون شروع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73173" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8047543035.mp4?token=XAowXH9RZb-q000HArFq-5pc-TM5RMasywZnoVcutuq5Qv5AX-u1np2X-uLZ4dApI6akgLOtHgRabMrrTXCNFB2iINK8TwBSXFpMJC7YSEHAajs9nET7n5kBVk43yeQxF561b0BViawtoiT74Zl8_1j2MbBYyhYC2LXJf3n5vpxVGgnS8tnqlaVkQQJHt9pgzrmYDhzWAKq3vZaQ1eaGa7L6GiMOrTR46Qj3wQINGhq5vOQ0ENGr7b8Wiv0_tE-5Uuqns5O7uZ1R9o7Z3yalZxvh_pH5-nO0LAIvoQU7cBtVhZF7ywEAhlIQpwjEG9mGYS5t4MeJ0fC2Fh2-_wrQpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8047543035.mp4?token=XAowXH9RZb-q000HArFq-5pc-TM5RMasywZnoVcutuq5Qv5AX-u1np2X-uLZ4dApI6akgLOtHgRabMrrTXCNFB2iINK8TwBSXFpMJC7YSEHAajs9nET7n5kBVk43yeQxF561b0BViawtoiT74Zl8_1j2MbBYyhYC2LXJf3n5vpxVGgnS8tnqlaVkQQJHt9pgzrmYDhzWAKq3vZaQ1eaGa7L6GiMOrTR46Qj3wQINGhq5vOQ0ENGr7b8Wiv0_tE-5Uuqns5O7uZ1R9o7Z3yalZxvh_pH5-nO0LAIvoQU7cBtVhZF7ywEAhlIQpwjEG9mGYS5t4MeJ0fC2Fh2-_wrQpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش علیرضا خمسه به کلیپ معروفش توی فضای مجازی(خلوت کنید آقای خمسس...) :
منم مثل همه شما یه آدم معمولیم. صبحا میرم پارک پیاده‌روی، بعدش میرم نون میگیریم و ...
بخدا من بادیگارد ندارم چرا به من فحش میدین؟
چرا به اون جلوییم که اون جمله رو داشت میگفت فحش نمیدین؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73172" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73171" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4gk7eFc7CzrMnWzuXH_EXrVZIw3n-trp9WAQVmW2YGHOYSVrcbwj_tPdnAbtx3ES83J_8Seouo9FxXOiP93o3nDZ2n5DwPouaPWs7TEf4q9_dtBxI6dgf6i_yLw_i7oU414erxscA5pRp2HcdpRMfMITtELKiuP_fCG4zjabRgOBM5Tkw4-JvGEBV9BiZ-AWHTFMna601L5sS8F-zhG4nJgxKVRBhmLFSFFoJpcqdWrrUG3woISyh349vFUKTbuD06AoPBdQEFeMennoVP674JRKFd6AT1hH_unEqxhilPpehJIRpAPUp8S50Ccq_Y73VnHaXfAgKqlnIoAn25M4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز استقلال
🆚
الغرافه رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
استقلال: ۲ برد، ۳ تساوی و ۶ گل زده
الغرافه: ۱ برد، ۱ تساوی، ۳ شکست و ۶ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73170" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#مهم
؛
اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید می‌تواند تأیید کند که حادثه پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
من می‌توانم ارزیابی خود را مبنی بر اینکه این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریباً به‌طور قطع توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است، تأیید کنم.
ما این تهدیدات را در خاک خود تحمل نخواهیم کرد. ما با استفاده از تمام اختیارات قانونی خود برای هدف قرار دادن شبکه‌های جنایتکار مورد استفاده ایران و همچنین منابع مالی آن‌ها، با این اقدامات به‌شدت مقابله خواهیم کرد.
ما تحریم‌های بیشتری را برای محدود کردن توانایی ایران و سپاه پاسداران در آسیب رساندن به خودمان اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73169" target="_blank">📅 18:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50742ac121.mp4?token=p0kje9968JKRrH5ghu624o6hScQXXMl7DM8Kut_tcJrWgs0_Zr3kNOlO7Bs_wruWkVoh7_WjBc_QNVfyCHjdBumJfL2MogAQuY85_ZlV0yuQt0ZRHazp9n5IUGmtNeRTiKCw0fMYQ1arkDbM_8Kv7_jz-FUp_m5HnUP-un6H62h1Cx6kOJoE-j_WUHO8XqN7xO1DPcEfRHxr0DA5fojggosymsrCRLaSvZKbeqlA5JigxM5x_n8lHdhhgeJ7HL8mRMFR2MB9rzJVvIs4aK3iOZA0ZZ9PMqFc12uAPem_0guznyVDXA2_oJdR5VEmFE-5tj61DWy70HtYqKm39uLYZh3zuj0JW_2jey0czGs_ttYFg2sQdIRCJUYVLJqqBil1-rZxZCr8h3seZAfvmkXuSB1nkrSXYL_R_RrMJpnBkw7tPbUQoS0ZVddugzzfOIoCvZHatfj9HmhDWTNjVh68M-Xfr7CfL9ea_ij9re8lEKuFT-Z3WVCdzTAGUgRg85UfWWj5oj1pU2UGDsRP4jkIiPM0NUVYK7yfN3U2ARIFqYSVEGk56p1il8_pLAWDkPDAnENY6CCTHIAQwAsRzMKfy6sQOtsRdtH3zUZ83TTuvJb69X4REt8sAzCRgkNMAVBG8j0lyMxvYInDaUe7CLeGcNVmwm3HYSXB9huFFYqChQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50742ac121.mp4?token=p0kje9968JKRrH5ghu624o6hScQXXMl7DM8Kut_tcJrWgs0_Zr3kNOlO7Bs_wruWkVoh7_WjBc_QNVfyCHjdBumJfL2MogAQuY85_ZlV0yuQt0ZRHazp9n5IUGmtNeRTiKCw0fMYQ1arkDbM_8Kv7_jz-FUp_m5HnUP-un6H62h1Cx6kOJoE-j_WUHO8XqN7xO1DPcEfRHxr0DA5fojggosymsrCRLaSvZKbeqlA5JigxM5x_n8lHdhhgeJ7HL8mRMFR2MB9rzJVvIs4aK3iOZA0ZZ9PMqFc12uAPem_0guznyVDXA2_oJdR5VEmFE-5tj61DWy70HtYqKm39uLYZh3zuj0JW_2jey0czGs_ttYFg2sQdIRCJUYVLJqqBil1-rZxZCr8h3seZAfvmkXuSB1nkrSXYL_R_RrMJpnBkw7tPbUQoS0ZVddugzzfOIoCvZHatfj9HmhDWTNjVh68M-Xfr7CfL9ea_ij9re8lEKuFT-Z3WVCdzTAGUgRg85UfWWj5oj1pU2UGDsRP4jkIiPM0NUVYK7yfN3U2ARIFqYSVEGk56p1il8_pLAWDkPDAnENY6CCTHIAQwAsRzMKfy6sQOtsRdtH3zUZ83TTuvJb69X4REt8sAzCRgkNMAVBG8j0lyMxvYInDaUe7CLeGcNVmwm3HYSXB9huFFYqChQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ اندی برنهام نخست‌وزیر بریتانیا می‌گوید می‌تواند تأیید کند که حادثه تروریستی در پایگاه نیروی هوایی سلطنتی «فیرفورد» «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73168" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=jtI9hFa_IE5_TUaq5lLXDJiWl9bv5KfGPU8wVlqwQ7dqszDTB64SEAAZ_S-9oPMZH2SQ0EhqP88FL8VGsLbLae0vjuZ_-zHTylJ2XpzsMKFRVgarTiGjDIw2xJ9MTQ3eXXHYUR6e5ffUkooXqpENWIGGaJ2I2ep1FalI9HrGJwM5B9zyqHdN7mYeTN7VOkClzrE7pxEHP2ikbnJGHfMPy_gqWfO4j2sDK6gBwGkWPYvakuT90jQZxAboKLiVQ0HUvO7kF8lgYu9xRsWGlSe23alRPKmRglev1gZd2Crs0lUXn5o19pJ9KC_Chfm6NrpErHjpVYPVDszCaJYBIKDHAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=jtI9hFa_IE5_TUaq5lLXDJiWl9bv5KfGPU8wVlqwQ7dqszDTB64SEAAZ_S-9oPMZH2SQ0EhqP88FL8VGsLbLae0vjuZ_-zHTylJ2XpzsMKFRVgarTiGjDIw2xJ9MTQ3eXXHYUR6e5ffUkooXqpENWIGGaJ2I2ep1FalI9HrGJwM5B9zyqHdN7mYeTN7VOkClzrE7pxEHP2ikbnJGHfMPy_gqWfO4j2sDK6gBwGkWPYvakuT90jQZxAboKLiVQ0HUvO7kF8lgYu9xRsWGlSe23alRPKmRglev1gZd2Crs0lUXn5o19pJ9KC_Chfm6NrpErHjpVYPVDszCaJYBIKDHAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که طی دو روز گذشته به سومین سوپر نفتکش در تنگه هرمز حمله کرده و موجب آتش‌سوزی آن شده است.
سپاه پاسداران اعلام کرد که این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه، سامانه ناوبری خود را غیرفعال کرده و به هشدارهای مکرر بی‌توجهی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73167" target="_blank">📅 18:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73164">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hk-kL3snbjsyrQN-C_Jrk_bwpbBkBmsoGNGCLxEt130ttofSC1fguFrF6O97UZXKuaLqqlNFlsaHX-hgGa9IojNkiKs5HGW0FIaNswJhLwlBvpDIFUlqAZjae2CziVXjYyENs2-BcLVyXv_mrRUQFnj1H5FDyvXU1OgOcORuPrR7A95KOioKIwlHMpK2FfK6vvCuuKWGmi90C8fNrF68KtuUyx4gAARCfqOlpq6AgmpdkhRTpzqHpwr-uyMYFCOCagNMqfYnXnXOedPq-LiDyzS4vGhcQ-tYq9zXd2yJIACLcQJwPcC-0lbZYOn-9nF-lOp5k8Hon19b4FNYMMLDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBQpObfWSxhHUSduZPq951goo-tfSoWSg6eMgBAp3JDsAOt8vqoZUU1_jsRB0eUq2jO-iikAXfV-WtA-3ZIkLyORL95qI_YTdDy-QEuwpz0YXs9eNOs2LZQw_hb64tvroMovSia86Ldsn7Sa60nZmSlgQKEv51oXOs6foS9mPtG6V3hlHlxhb5hE9lNeRal1GRkTM_cKtD9w1Cz2mVAyvUoDashuOwbFWb_T-wKQ-Ta54roRLbI_PNhqCiGYMu9eISd-4gSp6jvqjRFSZB4LQFH7y58iWJcjzYF5CD4_S9KPiRuKhiZ1-saztvdw5Xo1GKu2fqSoa5a5otyX_dsqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-ZkgwaCsRtbPNHgyppulLawl-naNhVTjfA6TyE-1Qg5q7_S6WpzwIqI7uuKilUakRsIsp07aEOpyiT7rYpzxh-XvcmdbPBlwYtKCdF82prBBMbo679wmsseaH5Fd3cXDjjeFh1vm1zERGn12WXJ5T92sv4HUfrAPobUkS9okpLouXF5FFDd4QhZxo-tgADGWiOdQZR0P-0mzWPVxsOFVTGO8rJw_zvpjnHK1ncmWzz8P5QUuCoDqDSjYS7ssRItNnSrRoT9XOeQYhpFY0u6na34oig-KbAr53XGlPV86tMR195eJYr5Nmf3U33pBhUn0GDCoJwjJ4aIKq_7fPCm7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آزمایش موشکی سپاه در یزد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73164" target="_blank">📅 17:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=KeOn0L9sdznMtCTZ-A08MTGFREUBNEPBeTFXwVcx2yWK5oI_sWyQptfApdrZsPQuMjXfleXgfccevAp-pVgutyq1vWXalS7_-nQRfKNNRowQQWiyuzZIsEFC34mb40AZ6ZirSnVz2W593GD0s68mZVZtUlOYMAw7KXOkYLESfiqikxrlIFdHDWFDw-Z1Y1MlNO6lNq9VueCw6gw5GJBr-7GTn0rcs_mwJlcQQ4267VudfRfZXWnkWC7ImsLe-7Kj6Pr21nxy8PqE4ELBALVUrPz-8lrZUQVQuFi118sRAWsm09sTI8H8Bu5b4iBVOewMwZjPdwgw-lM3dBImQzWdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=KeOn0L9sdznMtCTZ-A08MTGFREUBNEPBeTFXwVcx2yWK5oI_sWyQptfApdrZsPQuMjXfleXgfccevAp-pVgutyq1vWXalS7_-nQRfKNNRowQQWiyuzZIsEFC34mb40AZ6ZirSnVz2W593GD0s68mZVZtUlOYMAw7KXOkYLESfiqikxrlIFdHDWFDw-Z1Y1MlNO6lNq9VueCw6gw5GJBr-7GTn0rcs_mwJlcQQ4267VudfRfZXWnkWC7ImsLe-7Kj6Pr21nxy8PqE4ELBALVUrPz-8lrZUQVQuFi118sRAWsm09sTI8H8Bu5b4iBVOewMwZjPdwgw-lM3dBImQzWdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین اصابت و انفجار ها روز ۹ اسفند در پایگاه سوم نیروی دریایی ارتش، کنارک
؛
در این ویدیو ، یکی از پرسنل که به ناچار و طی غافلگیری به اطراف پایگاه همراه با هم رزمان خود پناه برده بود، می‌گوید ،"جایی نداریم ،فعلا همین جا بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73163" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73162" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KhBv6lzKaeLNR5tB1FewtmKKXF4pD3M5y3Bjr30xkZ5iYzCc68WlZBVFh4mj1aUKZ1uJzO9qnTnGMBaT4X66JR1aPWIWO8eFfvrwp5Kc8XEJ8DupdTM-Rq4-FKf7dTrntetjkz02N4VDIY2ve91Gb5N6UHqu0PsUjPtb2J0fwiZxXgM3URwnhOSY9qhgqg1Zzdoyf6R9ckPIskkXZZHhPhFEJo0ebV7yw196JlGR2Kl4py6d_NXroW_4lP-JeQTXg_0BoXtxfRC8f4W-XXXETK8E-odkUYBqJur6JZuTCewMX_kgH3Wq32Bgh3EzqiWy3srBJCJ8zLq5GhF5r02fqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73161" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتش اسرائیل در پی وقوع حادثه‌ای در شمال این کشور که منجر به مجروح شدن گروهی از کوه‌پیمایان (که گفته می‌شود معلم و دانش‌آموز هستند) شده، وضعیت «حادثه با شمار بالای تلفات» اعلام کرد.
این حادثه احتمالاً ناشی از برخورد با مهمات عمل‌نکرده بوده است.
گزارش‌ها حاکی از حدود ۲۰ مجروح است که وضعیت برخی از آن‌ها وخیم بوده و یک نفر نیز نیازمند عملیات احیاست.
ارتش در حال انتقال مجروحان با بالگرد است.
نتانیاهو حضور خود در برنامه تلویزیونی «The Patriots» را لغو کرده و در حال عزیمت به محل حادثه است.
فردی که در وضعیت وخیمی به سر می‌برد، اکنون جان باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73160" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=AzKnxpwMzwKsCks9D5yWdPOS1lgioFG06ZawlzXvqx6mIKYcb4fHCLQuHpE3S3SYT6yMLlf8Qfm1_XY6atw2vzicK3XCuR2Whk4cZ7OD0mDTMkppdgFgCufcKgBDjzbxbpPP1HeaXHNwk0YuVLRCRmZtEW5ip1QogJF4tZq5BDozOWfDlZTnLDM3yDdxFv8XqVwLta1LP842wU4brpjSNOMeuFYcHoWnM0obzdKeo4HFYaJ6tcbb6-J5gHI1hHGmGPhQPAcyzTgEYrxO8eq_LocESvxblnKLWVKVH4mVpHZJGETZOOok0h32ueXI0u4mEm_xkXipRtUY-TWtUC79eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=AzKnxpwMzwKsCks9D5yWdPOS1lgioFG06ZawlzXvqx6mIKYcb4fHCLQuHpE3S3SYT6yMLlf8Qfm1_XY6atw2vzicK3XCuR2Whk4cZ7OD0mDTMkppdgFgCufcKgBDjzbxbpPP1HeaXHNwk0YuVLRCRmZtEW5ip1QogJF4tZq5BDozOWfDlZTnLDM3yDdxFv8XqVwLta1LP842wU4brpjSNOMeuFYcHoWnM0obzdKeo4HFYaJ6tcbb6-J5gHI1hHGmGPhQPAcyzTgEYrxO8eq_LocESvxblnKLWVKVH4mVpHZJGETZOOok0h32ueXI0u4mEm_xkXipRtUY-TWtUC79eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو ماه پس از سیل ویرانگر پیشین، نپال بار دیگر گرفتار سیلاب‌های شدید شده است. این حادثه خسارات سنگینی به مناطق سیل‌زده وارد کرده و بار دیگر زندگی ساکنان این کشور را تحت تأثیر قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73159" target="_blank">📅 16:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=OA-1NiCTOS0gj_Q9SRVUiUxD4j6UBcobTiIeD0LjuNFJDUpZJCOhwwjZjPZboVE9xGyL9zvqieMI7qBY4ZqC5jXkjvqBrZqeRoD5XGrRCmMB5-Lg9WfnMCZ0sq-GckGULD-MjXeyt5x7CVxgRV92TcaERs_WO5yl0WEUPqO5Z2YQ05HY0f9bQFUEMrCHVNwgBWgItkvx_Er1gCLdnV7lnrb8qQgD_13p4kXRriS9TeOie_RT-j2t6aLZz1MCM4Cr_UT3PBl-tyi1Y5C_KQIsRezkFralLFzWLWGcVVIs4NeW9F3aqF0MhrEO0_quoXDlYvAlgPXQNDfbnAOkJcNNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=OA-1NiCTOS0gj_Q9SRVUiUxD4j6UBcobTiIeD0LjuNFJDUpZJCOhwwjZjPZboVE9xGyL9zvqieMI7qBY4ZqC5jXkjvqBrZqeRoD5XGrRCmMB5-Lg9WfnMCZ0sq-GckGULD-MjXeyt5x7CVxgRV92TcaERs_WO5yl0WEUPqO5Z2YQ05HY0f9bQFUEMrCHVNwgBWgItkvx_Er1gCLdnV7lnrb8qQgD_13p4kXRriS9TeOie_RT-j2t6aLZz1MCM4Cr_UT3PBl-tyi1Y5C_KQIsRezkFralLFzWLWGcVVIs4NeW9F3aqF0MhrEO0_quoXDlYvAlgPXQNDfbnAOkJcNNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی عجیب که از اعتراضات فرانسه وایرال شده؛
مردم تو یه میدونِ بزرگ با جمعیتی زیاد جمع شدن و درحال شعار دادن هستن که تاچشم کار میکنه پرچم فلسطین دست گرفتن و حتی یه پرچم فرانسه هم دیده نمیشه :
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73158" target="_blank">📅 16:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73155">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=nXqBPPz-BN0Hy68M47rVn3mMpSLGqrzagmPjXiYZddm4fPOJR6c4I4rvZjGO9McUu2ujNt-1GvBqRzRfoh1bFHjZn3PxSKKFURK6cGOrOi4f8ZGU_E0Z-_zQ7hnY2e1Im9lq4loAuzant8XKGY_xJ08w6I_E7ubcbi4ja_e7Wyn7c7ds53FcNABfAQEUI6VyeNnaDpcnVFaj9ShxlvYoNZyba1_x0TuV3RvpYcQZJ8S82ibcBK1oapvWJuuq4NB5Xt4KIzMnN4nfU4ehpszgognlOd42h6dZxi1mfWLqqmVW0gtY2481dO0IC__zffarC9cxWsQHRGI0v9OjahDb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=nXqBPPz-BN0Hy68M47rVn3mMpSLGqrzagmPjXiYZddm4fPOJR6c4I4rvZjGO9McUu2ujNt-1GvBqRzRfoh1bFHjZn3PxSKKFURK6cGOrOi4f8ZGU_E0Z-_zQ7hnY2e1Im9lq4loAuzant8XKGY_xJ08w6I_E7ubcbi4ja_e7Wyn7c7ds53FcNABfAQEUI6VyeNnaDpcnVFaj9ShxlvYoNZyba1_x0TuV3RvpYcQZJ8S82ibcBK1oapvWJuuq4NB5Xt4KIzMnN4nfU4ehpszgognlOd42h6dZxi1mfWLqqmVW0gtY2481dO0IC__zffarC9cxWsQHRGI0v9OjahDb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو بریتانیا، یه مرد جوون وارد محوطه ببرها تو پارک حیات وحش یورک‌شایر میشه و اونجا یکی از ببرها به نام آلتای بهش حمله می‌کنه و نهایتا میکُشتش!
مسئولین حیات وحش اعلام کردن که خوشبختانه ببر سالمه و داریم بررسی می‌کنیم بفهمیم اون کسخل چرا رفته داخل...
یه ویدئو از قبل ورود این مرحوم اومده که داره به یه زوج بریتانیایی میگه "
من میرم بین ببرها، ازم عکس بگیرید!
"
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73155" target="_blank">📅 15:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73154">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e5000591.mp4?token=NGDKfyXZ7Vc-X0YZhV7sRH9Hkppseq5t_gpcFJ8Cb4rHZakxwCvLTaVFmWdC9PosK96jBisId8mSzkvGfuMYFFBwSlZDpSsIfsBmLVa2PAAp614RWgTdk0aIPB4ZQHErlhFQ63MMTnvZ4ZDkwEoMNk6zNh23xl0PZPXdGxvoix0dyxODuxFsWgZITVN2ypQB9B22s4tCB26z6ASnfPMzAxvPC9MCDlanuUtbHd7yy40jXvOKFI1gjIpG6Ho3X34KpIt9cwVc1Q_xbGZ2UbH030UTo952TLrBxNwfEyZStREje_4-aQevIqcRTmWPeDJLWSg9VsjzPuVeo_iRgL9dPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e5000591.mp4?token=NGDKfyXZ7Vc-X0YZhV7sRH9Hkppseq5t_gpcFJ8Cb4rHZakxwCvLTaVFmWdC9PosK96jBisId8mSzkvGfuMYFFBwSlZDpSsIfsBmLVa2PAAp614RWgTdk0aIPB4ZQHErlhFQ63MMTnvZ4ZDkwEoMNk6zNh23xl0PZPXdGxvoix0dyxODuxFsWgZITVN2ypQB9B22s4tCB26z6ASnfPMzAxvPC9MCDlanuUtbHd7yy40jXvOKFI1gjIpG6Ho3X34KpIt9cwVc1Q_xbGZ2UbH030UTo952TLrBxNwfEyZStREje_4-aQevIqcRTmWPeDJLWSg9VsjzPuVeo_iRgL9dPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با نیسان از اصفهان راه افتاده و رسیده به پلیس‌راه سیستان‌ و بلوچستان؛ اونجا مأمورا بهش می‌گن می‌خوای کجا بری؟ می‌گه ایرانشهر.
مأمورا بهش می‌گن مسیر خطرناکه و توی جاده احتمال کمین گروهک ها وجود داره؛ بهتره صبر کنی چند نفر دیگه بیان تا باهم حرکت کنید، یا بین دو تا کامیون راه بیفتی تا همراهی‌ات کنن و به ایرانشهر برسی!
+
گنده‌گوز منطقه حتی نمی‌تونه امنیت جاده‌های داخل کشور رو تأمین کنه
!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73154" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73153">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWbuFeUuUz0DpCB9b7qREpDQXSSFn8ZmDBTKwFKw39tfvStPqpJpAaksCGaGfZWCfyAMkps04PV1hlMfWpkSmyMSmCp_H_YO5rcDUBcvPBEMX1uev1IvZmrJQytLauIFTiz7OT4IShPWqweyJ6_BcQuAorrE6E_vTI92DyubtfuiYBsYG-z2Dvy7qPZhX8N6RgwH90lBklCviHfHaTIiZlh70esIgzvbyIPTfRLI-O4ZIpgwChTcuEcSM445mHSzU0wRBW7hIrn0yLfNwT3iZdMiPsshDZo7jTABMzVboH9383spr4wFbfbcvJWlgJQ8XDEHJ9AbuX8hrZR5JkNswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر به هوش مصنوعی گفته هر چی میگم، در جوابش بگو جمهوری اسلامی.
بعد ازش پرسیده بهترین حکومت تاریخ ایران چیه؟ اونم همچین جواب شاهکاری داده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73153" target="_blank">📅 14:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73152">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=vLcw7xxtHDb3Vz9o694Y1mO0kh0PCMSLKGn8UL3MiLsOqc6Bgfni4vjLikc-ezeqVTU7Uw20hW2Mu5YzH3G2GdqGPVL95rqhBxBONv1i23RQeqE-6nU-2zLuruyu9s4IM7K1lK5QpyTFPmPhimhCfYSayaifugsOd_J0L1YifQc1jTRu623srXHFG2cePTFjpQzjPMu3jpFT8iHO41GuNV18B1cqC_yLrK68VDE12Q6lCzmveelA1stVfeN1GW0XHC1s8T7CeRgbVDa221g9RU568bDVRCVuMEzSfaUdjdQMm2vCAVTRCRw_2cRkcvX5S_SDoqvn6chc46acR2PeGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=vLcw7xxtHDb3Vz9o694Y1mO0kh0PCMSLKGn8UL3MiLsOqc6Bgfni4vjLikc-ezeqVTU7Uw20hW2Mu5YzH3G2GdqGPVL95rqhBxBONv1i23RQeqE-6nU-2zLuruyu9s4IM7K1lK5QpyTFPmPhimhCfYSayaifugsOd_J0L1YifQc1jTRu623srXHFG2cePTFjpQzjPMu3jpFT8iHO41GuNV18B1cqC_yLrK68VDE12Q6lCzmveelA1stVfeN1GW0XHC1s8T7CeRgbVDa221g9RU568bDVRCVuMEzSfaUdjdQMm2vCAVTRCRw_2cRkcvX5S_SDoqvn6chc46acR2PeGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دوربین مدار بسته از لحظه وقوع سیل‌ ویران‌گر در شهرستان گرمی اردبیل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73152" target="_blank">📅 14:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73151">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=neAQgcjAuNavUY4GRtnJV9E8457dL_A7hnrp8_AhbnDi1p8Rpre2MDzgOSFdib37pMkYR6hNw2zfHLFy-YJLUQM53CWO8e7pHDwosw0BE2jFVEl-kWZnbvZ4NWrbFK9g8fXukbYBDdAhAz0vfHdC_RpRwSBYr_Fj8xcUUSdqj_EEn4oeo9CTwVL_8eb5sXl53yJaowddyNDDSWOoPug0esYIgGB1S-NpEcwYn2ldbkwofZKP50jiQbkenMJEvHk93lVALiMjYMB6fN1QAj87Ytrj2NhJU3FbQm9-MraEyvE87dv0tbDMRnSrI4H_B4iY100rX90M3f-f2_yZxFRCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=neAQgcjAuNavUY4GRtnJV9E8457dL_A7hnrp8_AhbnDi1p8Rpre2MDzgOSFdib37pMkYR6hNw2zfHLFy-YJLUQM53CWO8e7pHDwosw0BE2jFVEl-kWZnbvZ4NWrbFK9g8fXukbYBDdAhAz0vfHdC_RpRwSBYr_Fj8xcUUSdqj_EEn4oeo9CTwVL_8eb5sXl53yJaowddyNDDSWOoPug0esYIgGB1S-NpEcwYn2ldbkwofZKP50jiQbkenMJEvHk93lVALiMjYMB6fN1QAj87Ytrj2NhJU3FbQm9-MraEyvE87dv0tbDMRnSrI4H_B4iY100rX90M3f-f2_yZxFRCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش یک روس، برای سرنگون کردن پهپاد انتحاری اوکراینی با استفاده از یک نصف آجر:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73151" target="_blank">📅 13:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73150">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=nsVf9HBwuEf4eLjSfRIHzdWQkSsBLUdDXUK-lzK_B91RUT85hR7ra5t6SQh0_8cWOt6bStAXVFOpf5oGnim0txMr3ERp39SYSrBdlo83BMTkVi-f0BjhoiKL5uPE-syo1WQQTeyuPL-ESaXf6u5D-7yRXUvfUuq7RGcFuCSrVmQ4QbzAnSel7o1JNiyO2e8BisHzdIK3Q1kvcX3aEtdNu9MO657ASvXeNdFFn7wslndc4la_JbT-N8HlkPheKfzDheFQao6f8aLwcTnFY3yTKs2s378u9C24AArv2nimy4c78lv_Y5oEe-m-D_hU0hEZfKQWIeXcILfCK7FjtE_Gog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=nsVf9HBwuEf4eLjSfRIHzdWQkSsBLUdDXUK-lzK_B91RUT85hR7ra5t6SQh0_8cWOt6bStAXVFOpf5oGnim0txMr3ERp39SYSrBdlo83BMTkVi-f0BjhoiKL5uPE-syo1WQQTeyuPL-ESaXf6u5D-7yRXUvfUuq7RGcFuCSrVmQ4QbzAnSel7o1JNiyO2e8BisHzdIK3Q1kvcX3aEtdNu9MO657ASvXeNdFFn7wslndc4la_JbT-N8HlkPheKfzDheFQao6f8aLwcTnFY3yTKs2s378u9C24AArv2nimy4c78lv_Y5oEe-m-D_hU0hEZfKQWIeXcILfCK7FjtE_Gog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی:
«بلافاصله بعد از پست ترامپ در تروث سوشال، روسیه حمله‌ای هدفمند به یک نیروگاه در خارکیف انجام داد.
معلومه که پوتین تروث سوشال نمی‌خونه!»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73150" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73149">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=g5kmoH4GHt8nuwbakjqvgHRtzgET5rbG1dk9YwVWgl0xnGW0IY3kl0ZDpix6wGhSGi6nnNp5RjgS2B8FPkbtsJn15-PDjgDDYgHo4ta6CqJINJqG2p92JY0KCyWr3rIhh026B94-z00O1d0LDfKTw8RqWyWg5MQpYSB8L_9a0lcxGqHqfET-xpxXZ_NWUH-KXh4YfXJA1_kd-sKdKekGA5dPwF2rHfQ9U659ZJZa6eGZrgy7jbEMl7vDKPpLr7k0fcf3iUadDVocDcC0JkvfHa6GFwIuYb2pUSa1w8uh1pvhjQuVpoESlU40O60gJPfamyGaKgqOPXU6AnWC21iSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=g5kmoH4GHt8nuwbakjqvgHRtzgET5rbG1dk9YwVWgl0xnGW0IY3kl0ZDpix6wGhSGi6nnNp5RjgS2B8FPkbtsJn15-PDjgDDYgHo4ta6CqJINJqG2p92JY0KCyWr3rIhh026B94-z00O1d0LDfKTw8RqWyWg5MQpYSB8L_9a0lcxGqHqfET-xpxXZ_NWUH-KXh4YfXJA1_kd-sKdKekGA5dPwF2rHfQ9U659ZJZa6eGZrgy7jbEMl7vDKPpLr7k0fcf3iUadDVocDcC0JkvfHa6GFwIuYb2pUSa1w8uh1pvhjQuVpoESlU40O60gJPfamyGaKgqOPXU6AnWC21iSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بیکارِ کنجکاو رفته بازی Resident Evil 4 رو روی نوکیا N95 دکمه‌ای پیاده کرده و همه رو به تعجب وا‌داشته :
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73149" target="_blank">📅 12:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73148">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=jDL83c6zetxpnCs5if4tfXud6Enle-91_JSiNc-G2XeleUUOckDBC3AIzq4JPhjpFxqx4RweDx3O6F7bCTGZk9nlXleJ0Y5ipvufKZKYM6QWPMxnwjMqv3id4-8Gbx4ya55BMVNN3m4NEhRhzFVllQsMfDAQo2GSuRdnI63Z3wV00PI2Z_h3sMAO6xWpg-t8Q1JOoSDiIbLcLxbOULTpPM3te8YYk9K4r81pWAFdmDzEFc1GlucTHUPuHyB-Jf-PAP284VPg1ztIcSdvccT__uJrGvPRIup1b2evZTPMzXGjhytjmjRFSzfQOmTkt8OAp7CGRRvXRVW2CeY8-lIOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=jDL83c6zetxpnCs5if4tfXud6Enle-91_JSiNc-G2XeleUUOckDBC3AIzq4JPhjpFxqx4RweDx3O6F7bCTGZk9nlXleJ0Y5ipvufKZKYM6QWPMxnwjMqv3id4-8Gbx4ya55BMVNN3m4NEhRhzFVllQsMfDAQo2GSuRdnI63Z3wV00PI2Z_h3sMAO6xWpg-t8Q1JOoSDiIbLcLxbOULTpPM3te8YYk9K4r81pWAFdmDzEFc1GlucTHUPuHyB-Jf-PAP284VPg1ztIcSdvccT__uJrGvPRIup1b2evZTPMzXGjhytjmjRFSzfQOmTkt8OAp7CGRRvXRVW2CeY8-lIOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیسکو مذهبی هم آنلاک شد و توی تجمعات شبانه یه رپر آوردن و حامیان حکومت دورهم میخونن و میرقصن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73148" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73147">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73147" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73147" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73146">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhgN7MO2TUzLEXIwglKeL4O63FoTJGFiHcyY6MoSuEZhIYYq5yCVkntMfKVj6qxzksEzpdiyIH25DtQ-rynH4G9BSi-qck7Nx9BZHKB3hh4HCd6oXkUL2bj-27NhIoGvRbIdvUyhOykHMSwn3OSqIP8W1uXC71K6rIQpJIsxBMrEb7ldbq3ddBce6oXu2QYJ6dc_bRubRzOcuZsulTCTBVLI23PvPWWJDRhHGGtYuDW0-ku6yW8wNRFtKcWSE7ZhG8RBj3jz3fafdXD2FsP_nIVBvAf-s74cINQKWfq4U7SGNbB9E0JfmxuR4QpRg9r7xi_D9eafRmp55eKMfrOvmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
کاونتری
سویا
🆚
لوانته
ونزیا
🆚
آتالانتا
اودینزه
🆚
تورینو
نفتچی فرغانه
🆚
النصر
استقلال
🆚
الغرافه
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
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73146" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73145">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=FNDVG582WgiXvDZu-o6GR25Fq8mpzE5TTqZ-IbYCK4-JxLYAIbQlF5kU2aJd4SyHu6thhDOfBp98oN5R6JINto6qgtbc0fGMMmT54KF-akzOkjQcONRhXdLrfRDq5m9Sqso3bCnH6ayNkL4q_Xcnpukv-_UN0eL4bibeirGbqP2a7nb1G770WWHzlGXV2jnV8qyfa38jjOZUf9mpg-ryPrSQkA3oj2dgmZOQ3B0CTjOVPBxZD2-2E950j4OTe2kzhOqEQ73AsqNKtoW0JbP1DWhIp6qYuqxEvHhedcQyVq87U_QV4oZ_F7dNBO_klKn8Td9eEPifgkICx-6Tw3KhmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=FNDVG582WgiXvDZu-o6GR25Fq8mpzE5TTqZ-IbYCK4-JxLYAIbQlF5kU2aJd4SyHu6thhDOfBp98oN5R6JINto6qgtbc0fGMMmT54KF-akzOkjQcONRhXdLrfRDq5m9Sqso3bCnH6ayNkL4q_Xcnpukv-_UN0eL4bibeirGbqP2a7nb1G770WWHzlGXV2jnV8qyfa38jjOZUf9mpg-ryPrSQkA3oj2dgmZOQ3B0CTjOVPBxZD2-2E950j4OTe2kzhOqEQ73AsqNKtoW0JbP1DWhIp6qYuqxEvHhedcQyVq87U_QV4oZ_F7dNBO_klKn8Td9eEPifgkICx-6Tw3KhmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف رائفی پور به باز بودن تنگه هرمز برای همه بجز جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73145" target="_blank">📅 11:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73143">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=t9Tpo6CuJ4HuuM-OEqdsJRgf9PArPb_R8zfbV0mzxuWnOeV6rPLEk0r9ef52PtEmSHqbOccM2H8lQd5MX6yPD3X2l6VDiJs8kU6klwsE5VM-K0uuY6ud4v26uY21QbntHdWsQlpZycaCR5CkikVv5TtkqpkjPV7-s5K2fzGTBwbZSOEZjkUUPulnKLxX0YPTLZx_FCHEGSK1NtqhT_-cZNVhxxXOKqAvPqRQ6qHFngWYm4S9Wsy-Zj8weazgQGD-yAPLHsHp3FVWV5xkQ5lYMdzCOj0TLvfImlKnWNyuc9SN_450SXP6deh9iRUHt-EPmKlVpM4vxYigk1PQV1sRLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=t9Tpo6CuJ4HuuM-OEqdsJRgf9PArPb_R8zfbV0mzxuWnOeV6rPLEk0r9ef52PtEmSHqbOccM2H8lQd5MX6yPD3X2l6VDiJs8kU6klwsE5VM-K0uuY6ud4v26uY21QbntHdWsQlpZycaCR5CkikVv5TtkqpkjPV7-s5K2fzGTBwbZSOEZjkUUPulnKLxX0YPTLZx_FCHEGSK1NtqhT_-cZNVhxxXOKqAvPqRQ6qHFngWYm4S9Wsy-Zj8weazgQGD-yAPLHsHp3FVWV5xkQ5lYMdzCOj0TLvfImlKnWNyuc9SN_450SXP6deh9iRUHt-EPmKlVpM4vxYigk1PQV1sRLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی، مجری صداوسیما که سال ۹۸ گفته بود «مملکت مال حزب‌اللهی‌هاست، هرکی نمی‌خواد بذاره بره»، طبق گفته محمدرضا باهنر از ایران مهاجرت کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73143" target="_blank">📅 10:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73142">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=G6t0Q54NoHI9kEiFnQa9kGFSxeBe0yrBCcdZXMALJgXU9Rgi_TO6Sl8bHtgy84C-dlTCnYrLkpFxV_dClif2uzpC1Kx2pOmChFgKrMBk-4UN51WFzvH4jf1r-h4xX_fcTS0Z_9jrwkcMI_Pg8MdblPUHXVQ7RW-1E7UONK9uPa32G107iPMiSICP4NNMoPoObqOFefb_5rRJKWWmJRt5RFBDuYwy9x4H3QB24198Dyb22KRoTiZoxfZ6rlWevzCooHtWhHhT3_cR1C-FB5b1ymzxix7c9_KDAbPQQYviMDsVmViuNRSkIXN4VWSSq_q_T2H_dx-Qa_8lVTUkD14kEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=G6t0Q54NoHI9kEiFnQa9kGFSxeBe0yrBCcdZXMALJgXU9Rgi_TO6Sl8bHtgy84C-dlTCnYrLkpFxV_dClif2uzpC1Kx2pOmChFgKrMBk-4UN51WFzvH4jf1r-h4xX_fcTS0Z_9jrwkcMI_Pg8MdblPUHXVQ7RW-1E7UONK9uPa32G107iPMiSICP4NNMoPoObqOFefb_5rRJKWWmJRt5RFBDuYwy9x4H3QB24198Dyb22KRoTiZoxfZ6rlWevzCooHtWhHhT3_cR1C-FB5b1ymzxix7c9_KDAbPQQYviMDsVmViuNRSkIXN4VWSSq_q_T2H_dx-Qa_8lVTUkD14kEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای این خانم در مورد کادوی روز دختر و گل‌های چند صد میلیونی که این روزا بلاگرا به پارتنرشون کادو میدن، حسابی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73142" target="_blank">📅 10:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73141">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479627e865.mp4?token=E4R3_1A-93zCbxiS6705qyveeIfSp8RB01cUy1Iru0pIclE5LNOmoJrsj5UQ2MRL6YfSYXw_NZMCiuu0Xk9Nn9uI_WAA_w__0w_6VxqFuF3ykeA2PwiBX3oDjSPY4HrGJ4HsNrRPjROCOkSkQnwm2_IHb5skSMknECkedrx5DkHkI2024qEYDQD7qWU5E_LJTRs01tgSjHpUYT06VEklECIYd0TDXxak3gv_CSqTQtpVctN8yp2vHMnp8gxR_El4ZLo8fvctS7UdNCKWB3vPaXj8mCjroJ7JMqQwq-DWEB4KlX9dtznZAUPRBTyg3gIrT28-LxNx0RCtx36DdZ6CAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479627e865.mp4?token=E4R3_1A-93zCbxiS6705qyveeIfSp8RB01cUy1Iru0pIclE5LNOmoJrsj5UQ2MRL6YfSYXw_NZMCiuu0Xk9Nn9uI_WAA_w__0w_6VxqFuF3ykeA2PwiBX3oDjSPY4HrGJ4HsNrRPjROCOkSkQnwm2_IHb5skSMknECkedrx5DkHkI2024qEYDQD7qWU5E_LJTRs01tgSjHpUYT06VEklECIYd0TDXxak3gv_CSqTQtpVctN8yp2vHMnp8gxR_El4ZLo8fvctS7UdNCKWB3vPaXj8mCjroJ7JMqQwq-DWEB4KlX9dtznZAUPRBTyg3gIrT28-LxNx0RCtx36DdZ6CAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه یک صداوسیما:دانش آموزان معترض فرانسوی، می‌تونن بیان تو مدارس ایران که همگی فول امکانات هستن، تحصیل کنن.
شما هیچ معلمی ندارید، پلیس هم داره دستگیرتون می‌کنه.
ما اینجا کلی معلم اضافه و کلاس خالی داریم.
اینجا ما آرامش داریم و همه چیز عالیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73141" target="_blank">📅 09:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73140">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=dPbej3Bf2k64HAVYk1sE8fSnSuA5H77ea649u7bprTbv2Mdt6IVx0HTe6wB8UOdTf3-diaPW8ViubrI41Bn_IH1-TNFi-G5jjnkwhsm3yi3iqdLAhMso_Ii8p3vqCYKH58gxFEhPyG84Z4_DpnXGwJZX6a2e2uYUom-R1WYE7iR44JU1jBMO4hL5TpEoTFfGfPgsZLuyzLsqU1FcSV9XhAVHzOBsZkg23uTCfObFoVznM7FSZ-u5lbcTMaWieg9SfBDCIOSSk56p4E0L_oI64KhLjf61ICYrpXou7nqlx802DR7k3BbZtKkkepH7u2CaJOtgW1vbiVI1YjMkyJHscA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=dPbej3Bf2k64HAVYk1sE8fSnSuA5H77ea649u7bprTbv2Mdt6IVx0HTe6wB8UOdTf3-diaPW8ViubrI41Bn_IH1-TNFi-G5jjnkwhsm3yi3iqdLAhMso_Ii8p3vqCYKH58gxFEhPyG84Z4_DpnXGwJZX6a2e2uYUom-R1WYE7iR44JU1jBMO4hL5TpEoTFfGfPgsZLuyzLsqU1FcSV9XhAVHzOBsZkg23uTCfObFoVznM7FSZ-u5lbcTMaWieg9SfBDCIOSSk56p4E0L_oI64KhLjf61ICYrpXou7nqlx802DR7k3BbZtKkkepH7u2CaJOtgW1vbiVI1YjMkyJHscA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که روبیو درباره خشایارشا صحبت کرده و باعث شده عده زیادی از طرفدارای حکومت عصبی بشن، یادی کنیم از مصاحبه قدیمی خامنه‌ای درباره خشایار‌شا که دوباره وایرال شده؛ جایی که می‌گه خشایارشا با بیش از یک میلیون سرباز به یونان حمله کرد، شکست خورد و هیچ منفعت ملی‌ای برای ایران نداشت!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73140" target="_blank">📅 09:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73139">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73139" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73139" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnan9dW71dhktlYq40uf-3RNcaATX97T_NWV6TRscQFTbldUMwloOjJFcH67ZmTDoUzVfsXQm5_Lmyuyl-vK3YYkcJaD9L49l3HKa6vFfD2Cfi6nQwh-JQ7I7ETTBCvwU53vo5MgMQDkPlbO45VFNH9_0RekvgCW3crRHxg-qd8qXZLlnQecYJL7tulxINbF4HIkAcPl7J7079U9cUMALb_PRq3yOv3Tx5PyrN7QzcYfRXb9R_z15DiWH_zXlHe0is2YJ4xKp-5TluYhDztMWxeSqkSaognR8FHoSz2XTXhfgdgzW_12p46p8ujMRoR0zXuGPvbYcq8OEc17G_uDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
[
قوانین رو در سایت مطالعه کنید
]
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/73138" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ens0nTScLm4jFfX4X8lDRmmoottMFsGf0TuaXAIelSjdH7gdlMsQnmwmB_isOfKZ_xne9AnzASMkp3wQ0VeORQdKfZtKNgcLQbyq4xBamFtWEkhNDNuX_L-h0Png8Ev2uM0WSkfw9Udm3AqZ-nF3TN2q7Hh5DOzNWvZRg3Xmcfkl4_1EU_MBhUdMfmjRdQgbUB2-XoYteaiyyat5kcTyruFX8dQYrfTwV3oygVSFgwIydjcOZCyXv0jSozxTBLtvaIqTvrVg_kHW1QunjLb6_Wkes18XAGp6EFYkZ17CHX2woLY8Hds9mLbgzgrb1_yrGhg0Ws8WLrFgoCQObI2ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
«آمریکا با بعضی از شروط هفت‌گانه ایران موافقت کرده، اما از نظر ما پاسخ آمریکا کافی نیست.
دیپلماسی ایران تغییر کرده و دیگه اوضاع به شرایط قبل برنمی‌گرده.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73137" target="_blank">📅 01:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73136">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ویدئوی لحظه اصابت موشک حوثی‌ها به فرودگاه ریاض
تصاویر دوربین‌های مداربسته، لحظه اصابت موشک بالستیک حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض، در روز گذشته رو نشون می‌ده.
بر اساس این گزارش، دست‌کم ۱۳ نفر کشته و بیش از ۳۰۰ نفر زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/73136" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73135">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=rehgSg_pjlQA9vx7frPmFXhckSG-YUE7dQF9iKwh4k3bw2U_Lm4pIr09Gef07oDkm7nBYYjmDIgaYa2Nrp_w6hf9rjaZDOAOA846tYNAOSOQjsfCWHUfm4RwUVA5271WyXyXo_U71eJwU9dIUgRn9QTzuywpNlMWMRtqc9qBd22L-7crVHMM9WpTSS6cDDWDEcJW5GMLw-6r84gRNaqN9uOOSS5XgEwohuK7N3oir-BMSV22SswGy6dFNh7q0jcfYdkK3NARVSnrSv7YhNG4VMBhH4CYSGSHOdFZMZNCYmi9ybuy-mc2MOiqBxYqfR6dfu0zdGCt2JOILBvH7dANxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=rehgSg_pjlQA9vx7frPmFXhckSG-YUE7dQF9iKwh4k3bw2U_Lm4pIr09Gef07oDkm7nBYYjmDIgaYa2Nrp_w6hf9rjaZDOAOA846tYNAOSOQjsfCWHUfm4RwUVA5271WyXyXo_U71eJwU9dIUgRn9QTzuywpNlMWMRtqc9qBd22L-7crVHMM9WpTSS6cDDWDEcJW5GMLw-6r84gRNaqN9uOOSS5XgEwohuK7N3oir-BMSV22SswGy6dFNh7q0jcfYdkK3NARVSnrSv7YhNG4VMBhH4CYSGSHOdFZMZNCYmi9ybuy-mc2MOiqBxYqfR6dfu0zdGCt2JOILBvH7dANxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مدارس پسرونه، اسپایدرمن تبدیل به اسپایدرعن شد :
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/73135" target="_blank">📅 23:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73134">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=IY0naii2kXchE0EkV_Hoh4zvSZd6Kl_0wsiPi6FWpaXrB15xWdemoeq48DWSKgzMEfp-BmY6mymuqGaZpiYuUHPqcif5NlKlOgTUqzBxA48pV476ByusTCZzUB-2jU7fVEInPp1YTb3VP_QjtKPdwI8Se744GTa0fhvnQBa2Ip93QHq04wCqpTljkeJwuqAqvAWCMbwmzKNccNygt3zimGX7-hnff4PgwP2ulnG8orXzbrsNMAlGIYC1PgQt4rQ1fATy8NZXX_i7NuixDxq_eR7roRrFLS4w-TejcYLO5IhUThuqbzAZBGIgqfonCAUSnBCww9KTSJS5nW6caIrXCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=IY0naii2kXchE0EkV_Hoh4zvSZd6Kl_0wsiPi6FWpaXrB15xWdemoeq48DWSKgzMEfp-BmY6mymuqGaZpiYuUHPqcif5NlKlOgTUqzBxA48pV476ByusTCZzUB-2jU7fVEInPp1YTb3VP_QjtKPdwI8Se744GTa0fhvnQBa2Ip93QHq04wCqpTljkeJwuqAqvAWCMbwmzKNccNygt3zimGX7-hnff4PgwP2ulnG8orXzbrsNMAlGIYC1PgQt4rQ1fATy8NZXX_i7NuixDxq_eR7roRrFLS4w-TejcYLO5IhUThuqbzAZBGIgqfonCAUSnBCww9KTSJS5nW6caIrXCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اگر لازم باشد برق اتاق‌های دولت را خاموش می‌کنیم اما نمی‌گذاریم چرخ کارخانه و تولید متوقف شود. مردم همکاری کنند فشار دشمنان شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/73134" target="_blank">📅 23:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73133">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=VdRrEfiW0fPB1dnb26VpPT3I8gmnl9hWTkXTGpQmJV8J_vXjoqCNU3XRA-GSET4sBSCX4Vqg8U2xOv9P_Bs9Tr19RMz5w3NAAVNDdks-Ay60X_jHMHeUEPvVb7vFiP3Vq-bySvwqk_fG5chUc7PurSEkI4yOJYOINJFBFCJT-e4O5k_tee86hCa982csID-Opugd6TGYE3rv7elIwgCjJ07P7YQU6XdFYhGZ5jdUnzA1lyYES9XdAZx1D_PawYNXLrKYsxv_MWwHxThLCJBV_V8YOoIZyxdoJLA6ESRG5na-FpaVSu3UGl37cjjYwKcnNGAGmLzbJXmxGyZ34nr5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=VdRrEfiW0fPB1dnb26VpPT3I8gmnl9hWTkXTGpQmJV8J_vXjoqCNU3XRA-GSET4sBSCX4Vqg8U2xOv9P_Bs9Tr19RMz5w3NAAVNDdks-Ay60X_jHMHeUEPvVb7vFiP3Vq-bySvwqk_fG5chUc7PurSEkI4yOJYOINJFBFCJT-e4O5k_tee86hCa982csID-Opugd6TGYE3rv7elIwgCjJ07P7YQU6XdFYhGZ5jdUnzA1lyYES9XdAZx1D_PawYNXLrKYsxv_MWwHxThLCJBV_V8YOoIZyxdoJLA6ESRG5na-FpaVSu3UGl37cjjYwKcnNGAGmLzbJXmxGyZ34nr5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ مربوط به پشت‌صحنه یه تئاتره؛ جایی که همه با هم دست می‌دن و همدیگه رو بغل می‌کنن.
+ عرزشی‌ها هم از این صحنه به خشم اومدن و می‌گن باید این بساط جمع بشه؛ حالا هم افتادن به جون عوامل تئاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/73133" target="_blank">📅 22:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=IWQbhtXrVrlXVswd7IxiF98A4rMFZ69UOPJ6W8GXMrL5hoiKayzwOtInf_hf9V4xFjqhxzC5ORDzKnewiLq9_BLvTLG4mNeqIn6OIxCGrFHY4gDh76jhXjD8y4aTv1owycr-u7ZQMdgHkGjgEymeQTN-VU6TF85tnVaRiRCxj4Iyvo8qNjDgpVaaYBHOPv2H-az-geus6gx89_6hVUZP70gKGm61QOBztl-U7OTfk4tYs7pQ4hpAbf_lVjMVzgVfiHOHRdXJpqHqkBF0yxiUsCjqnGG4IXjhqqigiWV90bSeAjrPcnaEhsGtbqmIK616rl-yE4IiPxUftobcmGe2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=IWQbhtXrVrlXVswd7IxiF98A4rMFZ69UOPJ6W8GXMrL5hoiKayzwOtInf_hf9V4xFjqhxzC5ORDzKnewiLq9_BLvTLG4mNeqIn6OIxCGrFHY4gDh76jhXjD8y4aTv1owycr-u7ZQMdgHkGjgEymeQTN-VU6TF85tnVaRiRCxj4Iyvo8qNjDgpVaaYBHOPv2H-az-geus6gx89_6hVUZP70gKGm61QOBztl-U7OTfk4tYs7pQ4hpAbf_lVjMVzgVfiHOHRdXJpqHqkBF0yxiUsCjqnGG4IXjhqqigiWV90bSeAjrPcnaEhsGtbqmIK616rl-yE4IiPxUftobcmGe2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه مدعی شد سومین نفتکش از دیروز تاکنون در جنوب تنگه هرمز با مین دریایی برخورد کرده و دچار انفجار و آتش‌سوزی شده است.
سپاه هشدار داد با کشتی‌هایی که سامانه‌های ناوبری و شناسایی خود را خاموش کنند، به‌شدت برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73132" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=hBpTwxGuVkM-Kl9rPo7r76dmhjQ_9jsir2AZmsafzVftVCrdBD7poqn4sJ7GP-x8v-o93z0QEoWNqTlZo6aGOZjXPAACBl8wX3_hOeaQmS-yazHyHF2PKsAqftZo-tUQMQJSiHVlqSB_K3zMhWzdChjzlv7ipS66iBOH0lK0MbT8JB3RzjvnNy1pEQ2B0hYXET8F4ToflrZJML4gGofhFfEtCrZqtD5NQgyzM3lRyGoIRdRjvdIB4sGkHACKhLlwu3PlmntLfCSvF1Bb0dT2g_BFtT5zGR8j8ULBFkzMsLCV2U_XULdTFehYkq2qyXFdXFJj2n7fjOEqSKhC5-Kx_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=hBpTwxGuVkM-Kl9rPo7r76dmhjQ_9jsir2AZmsafzVftVCrdBD7poqn4sJ7GP-x8v-o93z0QEoWNqTlZo6aGOZjXPAACBl8wX3_hOeaQmS-yazHyHF2PKsAqftZo-tUQMQJSiHVlqSB_K3zMhWzdChjzlv7ipS66iBOH0lK0MbT8JB3RzjvnNy1pEQ2B0hYXET8F4ToflrZJML4gGofhFfEtCrZqtD5NQgyzM3lRyGoIRdRjvdIB4sGkHACKhLlwu3PlmntLfCSvF1Bb0dT2g_BFtT5zGR8j8ULBFkzMsLCV2U_XULdTFehYkq2qyXFdXFJj2n7fjOEqSKhC5-Kx_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از جشنی که یه خونواده، برای اولین پریود دخترشون گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73131" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=psr0EWSM75Wt8AVLOX7PcWjVu6jyLgAp-0TPeQ9Hu2La9WMK9o2rZdFCzS63rELENgFRX-KjEioy6LU-r6daa6SDbLrLURSpbzgO7lCotfjm6EUu3Pme4JLX-vVGf1zj7zmwnU7G4Wv-OECVL9FTwYTdaJruRhYMhcWBTxkfUyx0ZtTmvR_iUmePstcVgBFHuJranIBOkmWOcekzIGHbIFoRajv2P96_oXyU_mjwpIPrwosCfUurYBFuGgNL7zaOzHcc_yhub_zs9Uy4IQd_Kw62zCa6Es_4rgLJH15hO7ZmsddjHdVqs1ix4iKMK5MvVTEiaT91rEiuLDbSJYtR8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=psr0EWSM75Wt8AVLOX7PcWjVu6jyLgAp-0TPeQ9Hu2La9WMK9o2rZdFCzS63rELENgFRX-KjEioy6LU-r6daa6SDbLrLURSpbzgO7lCotfjm6EUu3Pme4JLX-vVGf1zj7zmwnU7G4Wv-OECVL9FTwYTdaJruRhYMhcWBTxkfUyx0ZtTmvR_iUmePstcVgBFHuJranIBOkmWOcekzIGHbIFoRajv2P96_oXyU_mjwpIPrwosCfUurYBFuGgNL7zaOzHcc_yhub_zs9Uy4IQd_Kw62zCa6Es_4rgLJH15hO7ZmsddjHdVqs1ix4iKMK5MvVTEiaT91rEiuLDbSJYtR8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافعمان را یا با دیپلماسی می‌گیریم یا با نبرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73130" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73126">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=ZLCfAs3oohZ-z2RzP_EtLQGspmntbZgsnHSd_Tohesb16whg1KKW_JOzJGwqy34HPSmVC2CaynhnfKb5B04CZh43FE5DyfS-YSsjqx0nlE-KBKxjFquJ1BB34QZ7IOCmqcQ8mJV-nzEa7RiutRdQ1aIelV1DWX3wKUv3J6dzHvHadDUgCjDGyP7F7shCqrE97fsN3mmbE0qyvLgyta9-MfpsuWiprWZq2_UMQ6K6NbqkGQ6NNxynxrEdLgLhhogM5N0H2reb27y4SYhNrxq9GEKwqinU3QBR6SKwRuVTKNm8Agv-i8S5DsgLIadBlhRjrIRX3Xj6qm0MyO9sYB2Y-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=ZLCfAs3oohZ-z2RzP_EtLQGspmntbZgsnHSd_Tohesb16whg1KKW_JOzJGwqy34HPSmVC2CaynhnfKb5B04CZh43FE5DyfS-YSsjqx0nlE-KBKxjFquJ1BB34QZ7IOCmqcQ8mJV-nzEa7RiutRdQ1aIelV1DWX3wKUv3J6dzHvHadDUgCjDGyP7F7shCqrE97fsN3mmbE0qyvLgyta9-MfpsuWiprWZq2_UMQ6K6NbqkGQ6NNxynxrEdLgLhhogM5N0H2reb27y4SYhNrxq9GEKwqinU3QBR6SKwRuVTKNm8Agv-i8S5DsgLIadBlhRjrIRX3Xj6qm0MyO9sYB2Y-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی امروز گسترده‌ترین رزمایش نظامی خود از ۲۸ فوریه تاکنون را با مشارکت سپاه و نیروی هوایی ارتش برگزار کرد. تصاویر منتشرشده، پرتاب پهپادهای انتحاری شاهد-۱۳۶ و موشک‌های بالستیک و پرواز جنگنده‌ها بر فراز تهران و شهرهای دیگر را نشان می‌دهد؛ تحرکاتی که می‌تواند نشانه آمادگی ایران برای دور تازه‌ای از درگیری باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73126" target="_blank">📅 20:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73125">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محسن رضایی:
«اگه جنگ دوباره شروع بشه، خیلی از کابل‌ها، دیتاسنترها، مراکز هوش مصنوعی و زیرساخت‌های دیگه تو منطقه نابود می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73125" target="_blank">📅 19:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73124">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js_ZJSJFT5-lKmlN2f6DNmafcitX4V1IO70sb4kQ0Uaz3Qnvj7RiRqIi7aE6fHOBo3_cAfT3GGr1GEgQohTbbBuICLDigZg8a_1AWtkGfHj_nV32fDRPjgfAO1AtScmZdNh36_zUL8gPQxIepqy4wqS3eXD5fDBl-nPvYT5fAT1rrGK_jsdnkyUFHnyLLrQjehzmqjnYbMvEe9EnbFLU7cH5RMA31pa47oi1jIOlTNdMuANV1xirjLreVkmL7ayviEtSByBK4FiAANpHu8apNEG378PyjWqBgYfla97wasuCg2DRYxGcsAy8CvuOIGBpWUGsE2_9t1ZxnQ7Jqlc-MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
«ترامپ به قاچاق روی آورده و با استخدام تعدادی مجرم که در آب‌های ساحلی عمان فعالیت می‌کنن، این کار رو پیش می‌بره.
اون هر روز ادعا می‌کنه تنگه هرمز بازه؛ اما من در پاسخ می‌گم شما مشغول قاچاق هستید، در حالی که تنگه هرمز تحت کنترل ایرانه و ما مدیریت اون رو در دست داریم.
طی چند ماه گذشته، هر شب پنج شناور مورد استفاده قاچاقچی‌ها رو در تنگه هرمز هدف قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73124" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73123">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20290170.mp4?token=kJu13JfzdFIXllpVlVOlj9w_7UgHttHHgbqPvj3-M0prH-sxazG4au1cNX2gb44ep_yTyg6B4HajgzAXbbRpzfBk_iq5x_mW0WjwMQgrRTiXEZRDCJhea1kx-nNFItu2L0rKIw_oTI-pUVQqVSVou_U2JknMt6ipAtlHVeF4g8PTo9GfhlzJEwiA1NfHadE3etxeo4OdMhx0FGhB9q46_bUMUCKXLXKB1PgcIDO8M-z9Rtz5ua6hzbl5MH4gjwCvsFTURa8RrgXhcvMhAUWyCbbAcPTY7yG676MzIGWeQCVmqQssNU9jkquBUWgIvNJdfvwTSciTqHTptAQBlU_P0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20290170.mp4?token=kJu13JfzdFIXllpVlVOlj9w_7UgHttHHgbqPvj3-M0prH-sxazG4au1cNX2gb44ep_yTyg6B4HajgzAXbbRpzfBk_iq5x_mW0WjwMQgrRTiXEZRDCJhea1kx-nNFItu2L0rKIw_oTI-pUVQqVSVou_U2JknMt6ipAtlHVeF4g8PTo9GfhlzJEwiA1NfHadE3etxeo4OdMhx0FGhB9q46_bUMUCKXLXKB1PgcIDO8M-z9Rtz5ua6hzbl5MH4gjwCvsFTURa8RrgXhcvMhAUWyCbbAcPTY7yG676MzIGWeQCVmqQssNU9jkquBUWgIvNJdfvwTSciTqHTptAQBlU_P0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات رسانه‌های عربی حوثی ها مجددا به فرودگاه ریاض حمله کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73123" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
