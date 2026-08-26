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
<img src="https://cdn4.telesco.pe/file/TmjqJV9Vm65Fbi0qiDGJyqcQ7-p2v6ntmxbg_ICOybzlmVdjrS_IkB7cUo-l7KGc1kifEZjT8QHzjWhsffoof6e1R24m8M6IrQFW0_CwDe5R-ZQBCU9H4BeNh55Upd43kCShBFMbgCmBZHuQpNxve4hx7ST9yzh8rZCjihySMSA0jWTsing9Og8H-145I8EZ5ikmluXfDIlBQBFh841Ubuy7mboGAbogm0MIZBCgqGNNTjw-vfgLvIlj5ijOOvFOb1YAlm4GGuWH2_qYcJJDqxta5XsdlX4mKVk41LGtiwXGRZy9jsLBOHWNCQBtGCt0iYzu_Nc_lKrcm_JdeJmqKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 16:02:31</div>
<hr>

<div class="tg-post" id="msg-684481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f28dcbef.mp4?token=W28-iiV3P8pRgfxghtLkeVHzzfTa5yMl7oeHYX8aYLRtDa8QYO94-v-3oXXE-Id32PZQCeDIk4MMck6pEUeQK46eZwOzyTdPuTyecs6fNH-Dpx7SdISPW-bkd4eHj0U8OE0ak4QGHHwZhC5Lmpr9GkZ7in6aMjO2_dI9DhREajl26zWvk1lxHA7yQihdijWgGVFF39f2PBc4pxI2yOuKjZitSFmbmGPJ6-aQIuOnLQChXsPaoJTBLbMXBwH5W6K1iwVFfO9VHgXGUUIBhUj52M4GlSnWBnXgcTBZbgVLVycJTVO2Vloqq9iuxPiA9Xp9wmPrIYYRHkoYXQqKoKHn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f28dcbef.mp4?token=W28-iiV3P8pRgfxghtLkeVHzzfTa5yMl7oeHYX8aYLRtDa8QYO94-v-3oXXE-Id32PZQCeDIk4MMck6pEUeQK46eZwOzyTdPuTyecs6fNH-Dpx7SdISPW-bkd4eHj0U8OE0ak4QGHHwZhC5Lmpr9GkZ7in6aMjO2_dI9DhREajl26zWvk1lxHA7yQihdijWgGVFF39f2PBc4pxI2yOuKjZitSFmbmGPJ6-aQIuOnLQChXsPaoJTBLbMXBwH5W6K1iwVFfO9VHgXGUUIBhUj52M4GlSnWBnXgcTBZbgVLVycJTVO2Vloqq9iuxPiA9Xp9wmPrIYYRHkoYXQqKoKHn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سواد مالی و مدیریت پول مادران در خانواده از چیزی که فکرشم می‌کنید مهم‌تره #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39 · <a href="https://t.me/akhbarefori/684481" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379bc087d9.mp4?token=rsKOIDIWhUKxUSFFnkuQXMUx_KoCN0MpGQ5YD1wnZbNmBVvWOrnowDGMhwHXonBIqMpjGUFS41HzmAr2zEE5K8sike5py-TCFxgMDEpRSye677JUjrlPu79hqbXnkNVwCWenp85_qxzRXhWQSLlDsRiFf-_hStGR5FGpILVGyBxWCXnJ_ZdhZrGMrpTwx0Q0NcBIoMyGNtHkmJPNeHRkEKXVsoBpr0twTIqMROQdWxHiqH8-TlHMPGHp5Jy2mqzRdQ5g8YRPx9brpa1SFpB1h_64lq9f-HGpmvcFP5sb97fx3EV8GwUerVTgm-ejTEBtD8ieVEuKnGGtBU7bmHpycA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379bc087d9.mp4?token=rsKOIDIWhUKxUSFFnkuQXMUx_KoCN0MpGQ5YD1wnZbNmBVvWOrnowDGMhwHXonBIqMpjGUFS41HzmAr2zEE5K8sike5py-TCFxgMDEpRSye677JUjrlPu79hqbXnkNVwCWenp85_qxzRXhWQSLlDsRiFf-_hStGR5FGpILVGyBxWCXnJ_ZdhZrGMrpTwx0Q0NcBIoMyGNtHkmJPNeHRkEKXVsoBpr0twTIqMROQdWxHiqH8-TlHMPGHp5Jy2mqzRdQ5g8YRPx9brpa1SFpB1h_64lq9f-HGpmvcFP5sb97fx3EV8GwUerVTgm-ejTEBtD8ieVEuKnGGtBU7bmHpycA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی
نتانیاهو جنایتکار درمورد ایران: به ترامپ گفتم اسرائیل با توافق خوب مشکلی ندارد؛ ولی توافق با این وحشی‌ها ممکن نیست
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/akhbarefori/684480" target="_blank">📅 15:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90808e7a06.mp4?token=XC8ABTl9DrUa03AyBtZTtL0ViqoA-6dZOHNqwr_BoOlJ1nGacJU8m_7itTtwAyKlDlb1IuNQtUqJcguWe_-QjD0OUY_vXQeuKcqvWACd0n8AwWkppXC7jvMprkNvhoFMz3armuBTs1rznRo4BUZfYagQvl0MVJiomzIEVcuePRhbhGk-GEyIuZJH7AXqiCjsdFEEeBS-jxvETiek0Xwu2qmXXphynnp7Wv6mmTMtpbrfqcYvmtY7GTrP6rRFNlREjbpIjGbFSJ2bUjDthJYIKJT0qEDFioxtkgUff4s6yHrkaMno8Jt7anKmAqkVESgLq69KTBYjFNCJHaB_hlSbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90808e7a06.mp4?token=XC8ABTl9DrUa03AyBtZTtL0ViqoA-6dZOHNqwr_BoOlJ1nGacJU8m_7itTtwAyKlDlb1IuNQtUqJcguWe_-QjD0OUY_vXQeuKcqvWACd0n8AwWkppXC7jvMprkNvhoFMz3armuBTs1rznRo4BUZfYagQvl0MVJiomzIEVcuePRhbhGk-GEyIuZJH7AXqiCjsdFEEeBS-jxvETiek0Xwu2qmXXphynnp7Wv6mmTMtpbrfqcYvmtY7GTrP6rRFNlREjbpIjGbFSJ2bUjDthJYIKJT0qEDFioxtkgUff4s6yHrkaMno8Jt7anKmAqkVESgLq69KTBYjFNCJHaB_hlSbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: پیگیر بازگشت ایرانیان خارج از کشور هستم؛ معین هم یکی از شهروندان ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/akhbarefori/684479" target="_blank">📅 15:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
از ملاقات با نوزاد در زندان تا بازگشت به دنیای سیاه؛ داستان باند ۳ نفره سرقت موتورسیکلت
🔹
داستان این باند ۳ نفره فقط یک گزارش سرقت ساده نیست؛ این یک تراژدی واقعی است. یکی از اعضای اصلی این باند، در حالی که در اولین دوره بازداشتش، شاهد تولد فرزندش در میان دیوارهای زندان بود، تصور می‌کرد همه چیز تمام شده است. اما بازگشت او به دنیای سیاه سرقت موتورسیکلت همراه با دو برادر، نشان می‌دهد که چرخه جرم چقدر بی‌رحم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/akhbarefori/684477" target="_blank">📅 15:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نخست وزیر قطر به تهران سفر می کند
🔹
شیخ "محمد بن عبدالرحمن آل ثانی" نخست وزیر وزیر خارجه قطر قرار است به زودی به تهران سفر کند. این سفر احتمالا فردا پنجشنبه و در چارچوب میانجیگری میان ایران و آمریکا صورت می گیرد.
🔹
در چند روز اخیر هم فرمانده ارتش پاکستان و وزیر خارجه عمان نیز در همین چارچوب به تهران سفر داشتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/684476" target="_blank">📅 15:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00dee499cc.mp4?token=eNlbSe0Q9XPoGBzE_G12a0yNwXgm4B5zfv7phh_dCBqsSxP8mkVqRUlTMYYPdB_dESZ_I7IqrF3R0rGGSQyzNrTlsDKmdmiyilrbHlL5OcGI5DxCzy2WYjK6AXuTk5V-GcNxsBPLSTO6N_k5AA6Isv1x2tgueQSJpOPpiCa3HdmAyrWL7at0oskFOcQRtbvKSsvTgcweLW2agP3ru5QKNdH3BqifXctLVoBSLqMPlG8dIUFGr1MfIHzOf2ShG2oxcq0o2UoKlCk2Cufb2X1oaaMWeVIjvdfB1gUMr38d1d3EydxnGfmwkmANyJpJd-6zLoCyptQJJiUeiGrSVegDdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00dee499cc.mp4?token=eNlbSe0Q9XPoGBzE_G12a0yNwXgm4B5zfv7phh_dCBqsSxP8mkVqRUlTMYYPdB_dESZ_I7IqrF3R0rGGSQyzNrTlsDKmdmiyilrbHlL5OcGI5DxCzy2WYjK6AXuTk5V-GcNxsBPLSTO6N_k5AA6Isv1x2tgueQSJpOPpiCa3HdmAyrWL7at0oskFOcQRtbvKSsvTgcweLW2agP3ru5QKNdH3BqifXctLVoBSLqMPlG8dIUFGr1MfIHzOf2ShG2oxcq0o2UoKlCk2Cufb2X1oaaMWeVIjvdfB1gUMr38d1d3EydxnGfmwkmANyJpJd-6zLoCyptQJJiUeiGrSVegDdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید نیروگاه های برق‌آبی(تولید برق از آب پشت سد) چطور کار می‌کند این ویدیو را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/684475" target="_blank">📅 15:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
جزئیات تحریم‌های جدید دانشگاهی علیه ایران
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) با انتشار سندی:
🔹
واشنگتن فعالیت‌های ورزشی و تبادلات دانشگاهی با ایران را به‌طور نامحدود متوقف کرده است.
🔹
این تصمیم سرنوشت آزمون‌هایی مانند تافل و GRE در ایران را با ابهام مواجه کرده است./ شفقنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/684474" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آخرین وضعیت تنگه هرمز از زبان سخنگوی سپاه پاسداران؛ اگر آمریکا شرایط ما را نپذیرد، تنگه هرمز به‌هیچ عنوان باز نخواهد شد
سخنگوی سپاه پاسداران:
🔹
تنگه هرمز در اختیار ماست و هیچ شناور نظامی دشمن داخل خلیج‌فارس حضور ندارد؛ تمام شناورهای جنگی دشمن دست‌کم ۴۰۰ کیلومتر از تنگه هرمز فاصله گرفته‌اند و از نظر نظامی و سرزمینی، هیچ شناوری بدون اجازه و مدیریت ایران قادر به عبور از این آبراه نیست.
🔹
آبراهی که در نزدیکی عمان قرار دارد نیز به‌طور کامل تحت کنترل ماست.
🔹
تنگه هرمز متعلق به ایران و کشور عمان است که مقابل ما قرار دارد. ما حدود یک ماه پیش با عمان وارد مذاکره شده‌ایم و به نتایجی رسیده‌ایم که مورد قبول دو طرف قرار گرفته است.
🔹
در این مذاکرات درباره میزان سهم هر یک از دو کشور از آب‌های تنگه و سهم ایران و عمان از درآمدهای آن توافق‌هایی صورت گرفته است؛ آمریکا در این مسیر کارشکنی می‌کند و همین مسئله موجب شده است روند کار به تأخیر بیفتد.
🔹
اگر آمریکا کارشکنی را کنار بگذارد و به تفاهم‌نامه بازگردد، می‌توانیم در چارچوب تفاهم انجام‌شده، تنگه هرمز را باز کنیم، بنابراین شرایط ما باید از سوی آمریکا پذیرفته شود؛اگر آمریکا شرایط ما را نپذیرد، تنگه هرمز به‌هیچ عنوان باز نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/684473" target="_blank">📅 15:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW5bdiev8Ty8FsL5YYR2Pvqj3TAPa2nsP7Y0K39QzVjnkNUSkRnGr4AMQTcmccuKZZXBvLZnSJTpWBC3Ta48guxW-Zxwr_EOKr4xCFnDhwvB4AV_EVDIlcB-e3UOdmM9soKYcyyG2-xoAV5IyoEu45FtwYDcoWT7ImvfTaV7jIkfV9UsnPmBrVg9EB91suehbpjnPaBe_zqJ9Vj7j5sD0m3h_WpnRwEQx4YMe9TUcoxYIMAcBhR6Yh9bIiZ2cXYrJ0Ou-Zr73K5gZWZXL99i24gw-DauYX0f_KJbHrh6DgGtxjPufVpqx5JCUHT614h2TnHgfiTArNAPl68iHpZfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد فروش در تاریخ شرکت پتروشیمی امیرکبیر شکسته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/684472" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1432aaa5a8.mp4?token=BMr7H0irIuvBZc06Ltf0-vldXzdpDoBnLQ76rEL8jWM6VRDXMgBBQOkWmaOdTLPgyOaSNTH3GJxxrtvrabAY-Lw4JqyfVBDLbT2lCZrkEaO-s7oM-ujWVRiNwXhHnYISYaJ2m3cp9CcAB_hZQaxjiXeMflr1Xvj6fdLXuVYjIQMIVI_Ifwf33gOmfEiBSeWv5z5D1OrPfywgv3FTtaKAzd19DZ6fKuNK3ZG7spoEezUU1R4LJH1q2NqNWrYYMS9mAj0AStxPrWwUTbjssm0Cc4SYkJr1qoc0GZueL1BPkRj3wNWXEEO2fk2ja_-PK5E2I-6VSS2cTkMcJmsiGa2m8XMuoZR1ur30JunYEuwmkDkXM2UkMDRZsosSpUErvwyFVb1hzT4_tCIUh402BX7m3NnfrBPeBQ8fqQl5zNmO6Oy45VxqzVvLUC-KQrLQu40puC8mvg12XO7s6r-MdrZpcEgcmTSot4dF04ysLNcHIrpI_nYAE7_8z05VIbOaVabb3l7jL-IZNRFKsb93ocUw9sd4aHZNsIY65obGAKl33p8Yu9l0NO9Y-Ypp0OVDVvD4UZ0hlufQTvyco8vZbXeaBDsbpsxrRNvo-VjoUh3z2HSCjyndjVS65EVplhDc_2DAXVsIo3HAUR4SM-25E1SfEk0Fb8tKISUtUYlVL3TUcsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1432aaa5a8.mp4?token=BMr7H0irIuvBZc06Ltf0-vldXzdpDoBnLQ76rEL8jWM6VRDXMgBBQOkWmaOdTLPgyOaSNTH3GJxxrtvrabAY-Lw4JqyfVBDLbT2lCZrkEaO-s7oM-ujWVRiNwXhHnYISYaJ2m3cp9CcAB_hZQaxjiXeMflr1Xvj6fdLXuVYjIQMIVI_Ifwf33gOmfEiBSeWv5z5D1OrPfywgv3FTtaKAzd19DZ6fKuNK3ZG7spoEezUU1R4LJH1q2NqNWrYYMS9mAj0AStxPrWwUTbjssm0Cc4SYkJr1qoc0GZueL1BPkRj3wNWXEEO2fk2ja_-PK5E2I-6VSS2cTkMcJmsiGa2m8XMuoZR1ur30JunYEuwmkDkXM2UkMDRZsosSpUErvwyFVb1hzT4_tCIUh402BX7m3NnfrBPeBQ8fqQl5zNmO6Oy45VxqzVvLUC-KQrLQu40puC8mvg12XO7s6r-MdrZpcEgcmTSot4dF04ysLNcHIrpI_nYAE7_8z05VIbOaVabb3l7jL-IZNRFKsb93ocUw9sd4aHZNsIY65obGAKl33p8Yu9l0NO9Y-Ypp0OVDVvD4UZ0hlufQTvyco8vZbXeaBDsbpsxrRNvo-VjoUh3z2HSCjyndjVS65EVplhDc_2DAXVsIo3HAUR4SM-25E1SfEk0Fb8tKISUtUYlVL3TUcsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معماری ایرانی یکی از بهترین نمونه‌های معماری در جهان که از دل اقلیم، جغرافیا و نیازهای محیطی شکل گرفته
#حواست_هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/684471" target="_blank">📅 15:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684470">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d563470688.mp4?token=LRWvjPLx3DJzSIf1vX-lGY7TNeHPpZq0zhr5frUvQUxrWpq6A8lOZdn9A6j8U-2ZxgHK9AbowvJYm1TpF_GtwW_tcvVQS5m6vbxtdX328kq1xCo-cWoNu-kseHvJ61oiSKFKWvFH3q7rXVcyQ7maQuQoRbhbd8iYgN2OZytdgm8SJhpp0OuJqpP56Kf83nXHGX_7t_1fwok5uJEr9Sog-QcgLk9SOegghCv0o06PlS419nftEOTpRXJwSXygR_oI-95n0Prblh0hQiWytGzBMUwaLXwWE4gM_ZoZn6ucq66xl2dpjrtpDU06bZceRmHnpWzyqN7cKbFOnt4-eP-YPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d563470688.mp4?token=LRWvjPLx3DJzSIf1vX-lGY7TNeHPpZq0zhr5frUvQUxrWpq6A8lOZdn9A6j8U-2ZxgHK9AbowvJYm1TpF_GtwW_tcvVQS5m6vbxtdX328kq1xCo-cWoNu-kseHvJ61oiSKFKWvFH3q7rXVcyQ7maQuQoRbhbd8iYgN2OZytdgm8SJhpp0OuJqpP56Kf83nXHGX_7t_1fwok5uJEr9Sog-QcgLk9SOegghCv0o06PlS419nftEOTpRXJwSXygR_oI-95n0Prblh0hQiWytGzBMUwaLXwWE4gM_ZoZn6ucq66xl2dpjrtpDU06bZceRmHnpWzyqN7cKbFOnt4-eP-YPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان اداری و استخدامی كشور: حقوق نیروهای شرکتی، قراردادی و رسمی از این ماه مستقیم پرداخت می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/684470" target="_blank">📅 15:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684469">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd0097cd7.mp4?token=kKHxkuWRSumSloLAq3FyJ78mOPoBzL30XO9PxiF60EyuMkqubrVuW35WqXswZedYt3PWmJ01EcMs0GR4fZ6z2saFawAqCdOCDilWOpdmZwLt7fgevHHENG6LEpLZz9d09KJ-d_egGg1hmAOF3ZSs3J_p2pre16l8esrR_c-VW_SzxlHSq0nGsLwO7cbgTvcKikINVMXZlUsARIOVOpwqDiwazARNbBDdULS5ujGoK398M8js4qFKKs5A9jSFuIz4wvVUxEWK4A0Yl7ffGrDccSq-zbWREUjYkG1P0J4m97aVttbcpESIirRZNTLDr0LosrSWoHwTSJqnvt43UWpniQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd0097cd7.mp4?token=kKHxkuWRSumSloLAq3FyJ78mOPoBzL30XO9PxiF60EyuMkqubrVuW35WqXswZedYt3PWmJ01EcMs0GR4fZ6z2saFawAqCdOCDilWOpdmZwLt7fgevHHENG6LEpLZz9d09KJ-d_egGg1hmAOF3ZSs3J_p2pre16l8esrR_c-VW_SzxlHSq0nGsLwO7cbgTvcKikINVMXZlUsARIOVOpwqDiwazARNbBDdULS5ujGoK398M8js4qFKKs5A9jSFuIz4wvVUxEWK4A0Yl7ffGrDccSq-zbWREUjYkG1P0J4m97aVttbcpESIirRZNTLDr0LosrSWoHwTSJqnvt43UWpniQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وطن در دل آدمی باید باشد
🇮🇷
🤍
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/684469" target="_blank">📅 14:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684468">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d33b77b6e.mp4?token=a9aqOCv3zb4R4XqS6qtDGLnPOC49_BNBqGoaNOgaufFMR3IlzgdTp5XB5QXdiKV5JxbN9r48PGAfNJR4QfYnF81tjeSU262e0rKytsQ_g3PXNNlWHotvNAL9qvQwS_5nRSgHzZMhWYzQIfbZh4U1m9o8hN-a_SQ2WUVf0A2DCN7KLBKhHNSGhE7mouweYsa16KK6gITNBZOB1S_9K2SMdExe1lAFBK-OTr7293PMr95U0lw4u838ByR7CzCtzdfX4OMbIMgzP409FPHfjCJ3PUiNJkIDwFKqsMWF-FEu17RL7qdv2g5pUmLbH0wUcinmI23koK-YDlKeF9mhm25yww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d33b77b6e.mp4?token=a9aqOCv3zb4R4XqS6qtDGLnPOC49_BNBqGoaNOgaufFMR3IlzgdTp5XB5QXdiKV5JxbN9r48PGAfNJR4QfYnF81tjeSU262e0rKytsQ_g3PXNNlWHotvNAL9qvQwS_5nRSgHzZMhWYzQIfbZh4U1m9o8hN-a_SQ2WUVf0A2DCN7KLBKhHNSGhE7mouweYsa16KK6gITNBZOB1S_9K2SMdExe1lAFBK-OTr7293PMr95U0lw4u838ByR7CzCtzdfX4OMbIMgzP409FPHfjCJ3PUiNJkIDwFKqsMWF-FEu17RL7qdv2g5pUmLbH0wUcinmI23koK-YDlKeF9mhm25yww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی ماندارین؛ یکی از رنگارنگ‌ترین ماهی‌های جهان
🐠
🔹
ماهی ماندارین یا «اژدهای ماندارین» ماهی کوچکی از آب‌های شور اقیانوس آرام است که با رنگ‌های درخشان آبی، نارنجی و سبز و طرح‌های مارپیچی شناخته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/684468" target="_blank">📅 14:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684467">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37e4708f1.mp4?token=LVzuNKemeB-zYa3xAYXJ9JCipP_Zjp1RNyejaeIlr5P72IrqIGaSHxHfK0pWrvQvcSzEFEsqARbSdnfNlvN1AKQBlGhmMlRpZjul5FgaAPNp0IvMIRySvj7x3queWnZKU6Y5VrPaToVpCRGZDN7YEYhtVWhKH6cv-6PWu4r1_20TBYpBsWDJGXUHevJHUYMh_CVI2Aqal1qbk62VMPxAj7KcPhmfYfPg_Bj-iUl7ZcgiTxO321RY7jMzX398PQjlgE_wPOl17hrUvO6ceSMTrZQtvjTNFqLiI1Z-FxFp7DVenoTmjqej9ianNCwpZRpZ30SgLMVpnPXsyVHRusALqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37e4708f1.mp4?token=LVzuNKemeB-zYa3xAYXJ9JCipP_Zjp1RNyejaeIlr5P72IrqIGaSHxHfK0pWrvQvcSzEFEsqARbSdnfNlvN1AKQBlGhmMlRpZjul5FgaAPNp0IvMIRySvj7x3queWnZKU6Y5VrPaToVpCRGZDN7YEYhtVWhKH6cv-6PWu4r1_20TBYpBsWDJGXUHevJHUYMh_CVI2Aqal1qbk62VMPxAj7KcPhmfYfPg_Bj-iUl7ZcgiTxO321RY7jMzX398PQjlgE_wPOl17hrUvO6ceSMTrZQtvjTNFqLiI1Z-FxFp7DVenoTmjqej9ianNCwpZRpZ30SgLMVpnPXsyVHRusALqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: جنگ همیشه راه‌حل عبور از مشکلات نیست
🔹
مشکلات امروز ناشی از اعمال فشارهای غیرانسانی وحشیانه‌ای بر ایران است؛ مردم نشان دادند اگر لازم باشد، می‌جنگند و کوتاه نمی‌آیند.
🔹
گره‌ای که می‌توان با دست باز کرد را نباید با دندان باز کرد.
🔹
در همه تحلیل‌های…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/684467" target="_blank">📅 14:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684466">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای تانکر ترکرز: در خلیج عمان دست‌کم ۱۵ مجموعه عملیات انتقال کشتی‌به‌کشتی (STS) در حال انجام است
🔹
ما ۲۵ میلیون بشکه نفت خام را شمارش کرده‌ایم؛ به‌علاوه مقداری محصولات پالایش‌شده نفتی.
🔹
این نفت تقریباً از تمام کشورهای منطقه، به‌جز ایران، منشأ گرفته است.
🔹
اکنون پنج مجموعه دیگر نیز پیدا کرده‌ایم و یکی از آن‌ها مشخصاً مربوط به گاز مایع نفتی (LPG) ایران بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/684466" target="_blank">📅 14:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684465">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d668cb3f77.mp4?token=fWRdcPqSXLFi4aeEGp6R5JaJkljV9iMAqEPHCj9LZOUcqSSk5NjYsqpjDbvIl71WVZMKOTLLak317MUgzCpzmirSr8BY4ijk-dFQN_iHhtcwfSa7tfKMyiC60yeIU1yeyjd8cutvig4PitjhitDnYDAkh_P4kBRo4WCvMMqKyPdSLfeInTM2yA4jVN3Y2kTAkdVMpg4HaPSxCwUrm484XAxPSgABxWQi5p1JlCC5GtnoN04kG7JaSXKaHEZXVpcpzaCIQ2R5pXGlMyTcTlmbxZ6BtSXw4uE0Snw-KLr7M_pH-SWyDH94qhsXkToagOfN7OdAdb-V0M_I1OE4sSoSXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d668cb3f77.mp4?token=fWRdcPqSXLFi4aeEGp6R5JaJkljV9iMAqEPHCj9LZOUcqSSk5NjYsqpjDbvIl71WVZMKOTLLak317MUgzCpzmirSr8BY4ijk-dFQN_iHhtcwfSa7tfKMyiC60yeIU1yeyjd8cutvig4PitjhitDnYDAkh_P4kBRo4WCvMMqKyPdSLfeInTM2yA4jVN3Y2kTAkdVMpg4HaPSxCwUrm484XAxPSgABxWQi5p1JlCC5GtnoN04kG7JaSXKaHEZXVpcpzaCIQ2R5pXGlMyTcTlmbxZ6BtSXw4uE0Snw-KLr7M_pH-SWyDH94qhsXkToagOfN7OdAdb-V0M_I1OE4sSoSXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا حمام هتل‌ها همیشه تمیز می‌ماند؟
🛁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/684465" target="_blank">📅 14:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684464">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
قیمت دلار با کارت ملی مشخص شد
🔹
نرخ پایهٔ دلار برای خرید با کارت ملی امروز ۱۹۵ هزار تومان اعلام شد؛ دلار در بازار آزاد نیز ۱۹۸ هزار و ۵۰۰ تومان معامله می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/684464" target="_blank">📅 14:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684463">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf9e2aeb.mp4?token=hDorX9ILw8kczvWUswqDMY6fhryZdlAiPVVfJt072Ammw4VQ7A4t7kCM44wRaym5aJvrWy8xFCTUmP9-a1zhfFpptkZiDvagH0r9yCO3EneL5petTO2gGJM9ko1d3_qQVkTPWN64L4X2TCmTI00z98rHeqe39WtXL75ezpu9riWhkWC-cYMT6X51iOQTW6tBPtttqMuSPm0JBXS_dHhzCBDKMi6ThftAdx81p1_RCDqRFf-ZeFwu-AsSpwmCLE-di4-DTRkMTN5vIL_teAnAVLesScc6TuP2LUZS8wDx9Z6ID2sfbRSQXBf6N6TOJJ3jaiqbQEu6tXjWnQBWLOISQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf9e2aeb.mp4?token=hDorX9ILw8kczvWUswqDMY6fhryZdlAiPVVfJt072Ammw4VQ7A4t7kCM44wRaym5aJvrWy8xFCTUmP9-a1zhfFpptkZiDvagH0r9yCO3EneL5petTO2gGJM9ko1d3_qQVkTPWN64L4X2TCmTI00z98rHeqe39WtXL75ezpu9riWhkWC-cYMT6X51iOQTW6tBPtttqMuSPm0JBXS_dHhzCBDKMi6ThftAdx81p1_RCDqRFf-ZeFwu-AsSpwmCLE-di4-DTRkMTN5vIL_teAnAVLesScc6TuP2LUZS8wDx9Z6ID2sfbRSQXBf6N6TOJJ3jaiqbQEu6tXjWnQBWLOISQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسکن استیجاری برای جوانان
۳۰۰۰ واحد در تهران و خراسان رضوی به جوانان تعلق می گیرد.
آخرین مهلت ثبت نام امروز می باشد.
@Titretejarat</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/684463" target="_blank">📅 14:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684462">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSh2fUvoyYkpzLk4SNp0b4go8o6rm_s7Q5xroIb-V9BlUq2uMUxNB2_2GyuIX8mqrEqCdfxs2Pha_ttHg1MClJ7pUHXzfAnshw9yMbMaRKMatH2mn4ILZ3EvOK_ELER0oHjfPn3dbwajC8LV-vpiVXuNzQ8ysj9ukYN8st3DG2_KfIhmcyEyRklntmfiqWYBJZtjqtzNvH0-18s6XBzH8v3oo1gnMPZOGl2EBkAcQ1KbbAmg5t8Lv4_hKB8I5C0R5ZqkxUsTP_psmC3DbKCAEUpzrpQxeeMREFf8n3uxXD0ARpKiFkkSsQ08gVH7p71ecSqYWr1kB0mTZxy1h0Jafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیاین خودمون بنگل و دستبندهای رنگی‌رنگی درست کنیم تا استایلمون شیک‌تر بشه #استایل_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/684462" target="_blank">📅 14:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmoI3Y9WF3vjkWw1wWbOQHXBPGz5hItAruxrZ0Ok2ft8g7K0O9ctLHSbYil8GzUfWAIfAL2Avd9zpQ1EUVfbhmr1Eymd8ca5W8x6FvEIsCiyNZJChUdpB0lpwgtrNAMAkAcwnW2DY9nDYuNOh_P5zs6BmslRA-w6O5baXx7ll76uL7hQTXUkuTFGZf14_RFFjm_iVvr6TQ7RqusKQNU2ifALtVNR2Ip9rcFc_eTKXX6A-QQMZUHaExM5cziJSL--blLrUbcS2HId_t82lCdbJv-V_hz88nLVuIP8dGLGCLrBLnJZlFAB-vaGWg7GPP5J2tlytmTodfJMUTcVcgIs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هر شب، 1 میلیارد تومان جایزه نقدی!
🎉
شب‌های میلیاردی اسنوا شروع شد
🎉
—— 5 جایزه 200 میلیونی برای 5 نفر ——
با خرید از اسنوا، علاوه بر دریافت هدیه و تخفیف حین خرید، در هر یک از شب‌های جشنواره، شانس برنده شدن ۲۰۰ میلیون تومان جایزه را خواهید داشت.
💰
⏳
فرصت خرید، فقط تا پایان شهریور
❗️
🔥
شرایط شرکت در قرعه‌کشی و جزئیات جشنواره رو همین حالا ببینید:
👇
👇
👇
https://s.shdk.net/snowa-telegram</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/684461" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684460">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره مالی اتاق تهران همراه بنگاه‌ها در دوران بحران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مالی، به بنگاه‌های اقتصادی کمک می‌کند با بهره‌گیری از روش‌های متنوع تأمین منابع، استفاده از ظرفیت‌های حمایتی و تصمیم‌گیری مالی هوشمندانه، تاب‌آوری خود را افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/684460" target="_blank">📅 14:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شرکت ملی پخش فرآورده‌های نفتی:۱۲ میلیون لیتر بنزین بیشتر در راه است
.
🔹
فرمانده پدافند هوایی ارتش: توانمندی‌های خود را در عمل نشان خواهیم داد.
🔹
رویترز: صادرات LNG قطر ٩٨ درصد کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/684458" target="_blank">📅 13:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سخنگوی ارتش: قطر از سرنوشت خلبانان سوخو اظهار بی‌اطلاعی کرده است
سخنگوی ارتش:
🔹
پیگیری‌ها از طریق وزارت خارجه، ریاست‌جمهوری و دولت و ارتش قطر انجام شده، اما طرف قطری تاکنون از سرنوشت خلبانان اظهار بی‌اطلاعی کرده است.
🔹
وی خواستار پیگیری جدی‌تر و ارائه پاسخ روشن و مستند از سوی قطر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/684457" target="_blank">📅 13:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پزشکیان: جنگ همیشه راه‌حل عبور از مشکلات نیست
🔹
مشکلات امروز ناشی از اعمال فشارهای غیرانسانی وحشیانه‌ای بر ایران است؛ مردم نشان دادند اگر لازم باشد، می‌جنگند و کوتاه نمی‌آیند.
🔹
گره‌ای که می‌توان با دست باز کرد را نباید با دندان باز کرد.
🔹
در همه تحلیل‌های جهانی، ایران پیروز این میدان شناخته شده است؛ اما گاهی خودمان روایتی می‌سازیم که گویا شکست خورده‌ایم.
🔹
می‌توان با تدبیر و اندیشه از این مسیر عبور کرد و به سوی عزت و سربلندی رفت؛ کسانی که از تفاهم‌نامه دفاع کردند، به فکر عزت و سربلندی کشور هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/684456" target="_blank">📅 13:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30952a8d65.mp4?token=s6tkxQNyZNHAVxAYHrCtrgI150e8ZatViJLuNvPZOrdaVPZkP7JFZLDOhWpYB00oih3GwO4QNeB_VBv3COPM3HydaiCo4KaabpItoo57s6rG7zmLTdsZHEoDtht5GFUaJ4nIRW_EcNnDiGJLnnnhkNqFH-Z-1aPu5eXgGKOW6v6lw098YWOvi_NA4ajLAkBPj1xaaIZ7uBdaGtKcrdfi007X6RZ2j-F5xRceo95dZiIsTgEr5-Mhgxy5y-4v4YgvYCvpJY-hLecBTx9u1K4-S88tnqNvaewRLclZAxCO3FqcSi0ONlbhI8OLooLOUUXR6BiZONkbDn7NfNvPs6X-2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30952a8d65.mp4?token=s6tkxQNyZNHAVxAYHrCtrgI150e8ZatViJLuNvPZOrdaVPZkP7JFZLDOhWpYB00oih3GwO4QNeB_VBv3COPM3HydaiCo4KaabpItoo57s6rG7zmLTdsZHEoDtht5GFUaJ4nIRW_EcNnDiGJLnnnhkNqFH-Z-1aPu5eXgGKOW6v6lw098YWOvi_NA4ajLAkBPj1xaaIZ7uBdaGtKcrdfi007X6RZ2j-F5xRceo95dZiIsTgEr5-Mhgxy5y-4v4YgvYCvpJY-hLecBTx9u1K4-S88tnqNvaewRLclZAxCO3FqcSi0ONlbhI8OLooLOUUXR6BiZONkbDn7NfNvPs6X-2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ویرانگر در نپال؛ ۸ کشته تاکنون و مفقود شدن ده‌ها گردشگر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/684455" target="_blank">📅 13:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGvt5mIxRyq7FB7XDSB0aomoajnTmiQyESXectcqO-pnW5wcwN-A6op7hehDLFXbOA2AKug0YySN1ksuuQqIp-EC7miQDKb0Ws626UH_SxmytmcNJZUAAIbWv8Ww9hlYAhzWsqCDAbqlbK7E1fSFupvH42aQqKWHZ_DXnM40fNBL9sJihNjrbNSKQ4XoqIAGIJAMcdpa6Gf0vQpA5V__3Rywg2SLne0kOa0RHaxzes7iRgZ8ueK52_yFjVE1uOjOWMyfKoFc7ePvyJALAmsrK2n7IMZsIgd3rfMsVbDDdQVbQojtJbFF8pd3jSdvlAo5WN0SZ9WCpjbch92uLrfk7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیپلماسی جاسوس‌ها؛ رمزگشایی از سفر رئیس سیا به مسکو | یا توافق نزدیک است یا اوضاع خیلی وخیم!
🔹
سفر غیرمنتظره جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا، به مسکو بار دیگر یکی از قدیمی‌ترین ابزارهای دیپلماسی میان واشنگتن و مسکو را فعال کرده است؛ کانالی که در دوره‌های اوج تنش سیاسی، گاهی از مسیرهای رسمی دیپلماتیک مؤثرتر بوده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3240619</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/684454" target="_blank">📅 13:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454460bfe4.mp4?token=BK4B5TcuXcbnqIwVTnnKaysXzZpRozum0D0AVjz4tg0kdTzX0sQfSHjOBFfmjFZM8Ih_EOaxbPEWttOgWyKgVuhOHlR0bgcRqgz9ZoOswaiQlxcMjzR6gQ8Ntclco0peAnDhIQ2yZn3-DEr8NcH-EjR5nF2e8G7s2Q9xon5fMzb03tkhWzMNTYN44_4aj8pfQJdTTOQNxQYV2FRmtplgEuvb_RHk6paj-ZjeYc1lCp-x681s0TAC8pFLwexjINa4S4JEY3-k7pNUnXvnGyx7AtEemJfHyi3FJNUHWCHGn3DE1auxV4dDu1C6gNORqaoc64Oc6FSr6qbYlOPgC-jhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454460bfe4.mp4?token=BK4B5TcuXcbnqIwVTnnKaysXzZpRozum0D0AVjz4tg0kdTzX0sQfSHjOBFfmjFZM8Ih_EOaxbPEWttOgWyKgVuhOHlR0bgcRqgz9ZoOswaiQlxcMjzR6gQ8Ntclco0peAnDhIQ2yZn3-DEr8NcH-EjR5nF2e8G7s2Q9xon5fMzb03tkhWzMNTYN44_4aj8pfQJdTTOQNxQYV2FRmtplgEuvb_RHk6paj-ZjeYc1lCp-x681s0TAC8pFLwexjINa4S4JEY3-k7pNUnXvnGyx7AtEemJfHyi3FJNUHWCHGn3DE1auxV4dDu1C6gNORqaoc64Oc6FSr6qbYlOPgC-jhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی‌کنم
🔹
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/684453" target="_blank">📅 13:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eded00e64f.mp4?token=ASTpQ6B6WBRrhgwbSrzQ-cUMv4AaXKMI5o4zGTrr_FsblGeePv_IRE0Lb9kyTXRJvdRWXui55_FE1pG-cnOCwRzn1EdViGq1irAfaBi4LWWUupJxXtdxNbDWYN7oc0nkdWTii4ypuGSHLnueqq4-YUB_MlTFz5hK7i-filINH_h4UN6scYSp5YeDAEFNyATIp7vrICsvwZ1G7qdKubFb2fo8wYwxz0P1RzielsmG1HDMXhK6gZ9bto9uAX0SlZNJE5uCA1smfmL0zzRMDPgDLGMCF04o46i3PDHipnBAXqIkbnlE4KoE7huegVuCvQED_3sVVll0Pf7KVyubDHcZAIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eded00e64f.mp4?token=ASTpQ6B6WBRrhgwbSrzQ-cUMv4AaXKMI5o4zGTrr_FsblGeePv_IRE0Lb9kyTXRJvdRWXui55_FE1pG-cnOCwRzn1EdViGq1irAfaBi4LWWUupJxXtdxNbDWYN7oc0nkdWTii4ypuGSHLnueqq4-YUB_MlTFz5hK7i-filINH_h4UN6scYSp5YeDAEFNyATIp7vrICsvwZ1G7qdKubFb2fo8wYwxz0P1RzielsmG1HDMXhK6gZ9bto9uAX0SlZNJE5uCA1smfmL0zzRMDPgDLGMCF04o46i3PDHipnBAXqIkbnlE4KoE7huegVuCvQED_3sVVll0Pf7KVyubDHcZAIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خرد کردن حرفه‌ای پیاز در چند ثانیه
🧅
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/684452" target="_blank">📅 13:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_PZ4D1jBWXzO6y62WU-uPrukEZQdvxm2vs76WBJ6kXjkxwqUchGiU30FEfbc6J-iW5eMbtkLcrQgQVf79_0QpRDiqwqf8U30hYR9dg6xUfcdxc-pzZFfocGI6_A7OCRHOp7NGwTvpHvgd6Pg8eOj3hwNu_6mmXxvG76RWzQyi8_1xRKgpzukgatY6JFglQ6i-f0dytd3ZvMETe_1e-urfGEeTXt_VaRH9bOk4fuqZXtTPJHN2SgqOdj7JZuAzq7jgT2Ziai2dAmzDhvcoN6ZfYOWGey1MFGH_b2-jmWDY-gHBTMRrXeByx_ZCQJLaWDa_BQhg4kQU7ylOYRgAxBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صمت: فولاد خوزستان یکی از قطب های اقتصادی کشور است/ سرعت بازسازی در این شرکت قابل تحسین بود
🔹
سیدمحمد اتابک روز دوشنبه در حاشیه بازدید از خطوط تولید و روند بازسازی خط تولید فولاد خوزستان پس از حمله دشمن آمریکایی-صهیونی، با گرامیداشت یاد و خاطره شهدای…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/684451" target="_blank">📅 13:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzrClpJ05Dps-0E4ux9sd2efNFDOfdwdxrds-Y39iiy3qkgNCN1gZ88Ljve4-Tmu6BLSQFOYl8qbPknKH2MTAscdHVnTQ9wRP4YXNI3Vq7C9oSTbRLOIspvYCCDBX1yJJw1o3GthzvaVwGGODSMbuTSOxhugW1zIK1KrTpoW100sqRiroKrzjzm7EGYxy6S4Y9Q1Awev-9gZ42zdxaZsnL9wQLx4_H8Y5rIMBvlRnY4aqv_ef4HtFODSPnD0EZJwd7ZX-JEh91UtqycuLvlaWfogzJdEQ_BRU0PjHMOANgLv4s5fXU-rD0ZA1EDT6HMM_z35ohhM2Ew0oQnf1vZWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هادی چوپان، پس از غیرفعال شدن ویزای طلایی امارات و از دست دادن مصاحبه سفارت آمریکا، از حضور در مستر المپیا ۲۰۲۶ انصراف داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/684450" target="_blank">📅 13:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a24138b85.mp4?token=g5qCHe0UjMaA8Ng8gHY90v83xBfjCzMc5bB6oQMUVzmJyhPDreIRnq80tPshsRiVkrl9UR4hAvlypsqbFI3y_s-rPE30vXrY09t9yiMOWfgh8EZ2u3ry-7OdRcQuyWbFzlPSKAnIareG-tMnlu8ZL_00eJl2PK3e5AzsRyU1ubym8kMXsTCZfgFIctvLB4NQGi0U1kFnbR2m125Q6IhNJqXNXSUQIZZO9PiMu_XggxkkQK543iAxh9DCXkdl2anvMUMoWWu1yRYj_VxrxHnt_BZOOozyC2oXhhqYFtAluXR7quA5gRqaNgG6Bvj1pAJ3AhbRV3Z1RgbJn3EX3KlMAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a24138b85.mp4?token=g5qCHe0UjMaA8Ng8gHY90v83xBfjCzMc5bB6oQMUVzmJyhPDreIRnq80tPshsRiVkrl9UR4hAvlypsqbFI3y_s-rPE30vXrY09t9yiMOWfgh8EZ2u3ry-7OdRcQuyWbFzlPSKAnIareG-tMnlu8ZL_00eJl2PK3e5AzsRyU1ubym8kMXsTCZfgFIctvLB4NQGi0U1kFnbR2m125Q6IhNJqXNXSUQIZZO9PiMu_XggxkkQK543iAxh9DCXkdl2anvMUMoWWu1yRYj_VxrxHnt_BZOOozyC2oXhhqYFtAluXR7quA5gRqaNgG6Bvj1pAJ3AhbRV3Z1RgbJn3EX3KlMAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه‌قضائیه:‌ نگوییم نمی‌شود؛ بگوییم می‌شود
🔹
اگر مردم فقط حرف و لفظ از ما بشنوند خوب نیست؛ باید کارهایی که مشکل است و نمی‌شود را انجام داد تا مردم متوجه بشوند ما همت داریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/684449" target="_blank">📅 13:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684447">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a0d51ad3.mp4?token=DeJAxkyal-QZdaL7yHeadE8nAH6n6kjluN5F6YJ3vttUsMqa4mWSoD5xEVqaJswMKcsq1CxgA4OTK9GiS6WnqlZ8a_hM0VpHGy70-Zdw4R4ucp1WFoVQbhV7-ph5zk6Un6jPMATOROWI7pBMvMeKmZ3gjnXrafcig_Y9DTMJ6ju063p9lxOc2wloQS4nCoq73iYf4vNzZ1v_qrphbK7aO2QcbDDcUsHBYV7KXBIy1i67-wC81kVDOW6xcmf7tJ3HZKIwaNOcP1bFyBNO6TcU1amDCx2ciybkgseYZY7ZJ4mK6DoNpc7x1dO6oNftNvid72BvHJMugw7cBJJtrTAmuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a0d51ad3.mp4?token=DeJAxkyal-QZdaL7yHeadE8nAH6n6kjluN5F6YJ3vttUsMqa4mWSoD5xEVqaJswMKcsq1CxgA4OTK9GiS6WnqlZ8a_hM0VpHGy70-Zdw4R4ucp1WFoVQbhV7-ph5zk6Un6jPMATOROWI7pBMvMeKmZ3gjnXrafcig_Y9DTMJ6ju063p9lxOc2wloQS4nCoq73iYf4vNzZ1v_qrphbK7aO2QcbDDcUsHBYV7KXBIy1i67-wC81kVDOW6xcmf7tJ3HZKIwaNOcP1bFyBNO6TcU1amDCx2ciybkgseYZY7ZJ4mK6DoNpc7x1dO6oNftNvid72BvHJMugw7cBJJtrTAmuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدان مغناطیسی MRI؛ ده‌ها هزار برابر قوی‌تر از زمین
🔹
میدان مغناطیسی دستگاه MRI می‌تواند حدود ۶۰ هزار برابر میدان مغناطیسی زمین باشد؛ قدرتی چشمگیر که حاصل پیشرفت علم و فناوری پزشکی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/684447" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684446">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
مذاکرات برای حقابه هیرمند ادامه دارد
سخنگوی صنعت آب:
🔹
طبق معاهده، در سال‌های نرمال باید ۸۲۰ میلیون مترمکعب آب وارد ایران شود، اما امسال حدود ۴۶۱ میلیون مترمکعب آب وارد کشور شده است.
🔹
وی افزود مذاکرات با طرف افغانستانی ادامه دارد و با دریافت قول‌های مثبت، امید می‌رود مفاد معاهده اجرا و حقابه ایران تأمین شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/684446" target="_blank">📅 12:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684445">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzaXVKmtq__5JuSgXv19wn7Nf6NplMewJPtjB6LnEm5KnrCtg3vXwIjThAN0LsyiuYlP22pXI_tG0qoEAxqK23gHUed65AdiCzfdJyRp47JAqeX9DLO9GJp5mY1goXTXPhVq_dv6ine8FwOTJXIHZgXWMj9piH0-g129ma26YD6c28cKbE9d1AJLWZ49CMWtXuP4s7X3RWHOkiQElBUdcH1jkdVf_HspMSCV9rnmHyFYJtzzdEl3WKpolRAM8LEOTzmTBT7NU1mq_JWuq9KpJEcRB7cpZkQfxImx317LIvkay4iZ3Y1JK-A-6SJuMlojeTN7uAvbwRu-bqP6nobuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۴ شهریور ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
دلار آزاد امروز با افت حدود هزار تومان، از مرز ۲۰۰ هزار تومان عقب نشست.
🔹
هم‌زمان، هر گرم طلای ۱۸ عیار در بازار تهران کمتر از ۲۱ میلیون و ۴۰۰ هزار تومان معامله شد و سکه بهار آزادی نیز حوالی ۲۰۶ میلیون تومان قرار گرفت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/684445" target="_blank">📅 12:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684444">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZz_6HOrgMltLLILfD2CWf4x2lZck8KDeXaUP2FsGEGZJE_opDWzIVwb-khtsjUmE1NOeTvi0dYl3JpP0jPcq4wjOG3SiG-856rWVpRsmgoyZuKnMxMkvLGneCWA6bwGNqcTNOJsY4dj9jwkSb8GPg9utNJdyXepuWZ1-_tKsERAwq8GEEDz7oybqpdxbdGAc4wuOlSkPy7D0AhMtKg38WhoxJL4H8_sJuO1uY4-nGDuS9xvv_pP1n7cq7OsxhMqk2XAU5Nk2rpZcmX4fvetCnqDpirP8sCkf1EQvmsJAqnGkvtMVcgmzydZgi_QWF-o9_yl1Fl3E9ZVyZo5w3HTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد بیش از ۱۶۲ هزار واحدی شاخص کل بورس
🔹
در جریان معاملات امروز شاخص کل بورس با رشد ۱۶۲ هزار و ۶۹۷ واحدی در سطح ۶ میلیون و ۳۸۶ هزار واحدی قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/684444" target="_blank">📅 12:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684443">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQIs7bqfyeqrEJCzPn2-UtW_g3jChFuYIQjHaOHaeO_KJ9R3qnYsiO3m0THVt8VN14mFwjIpr25KqNx9175JJLYVTl6lwf9uIcP9GuJJGdw2bHbiOj5bSyovFBT_O_ygBAHH2bgoVyYGt9TIEMIDXCpIKd1lUyIyO90Oq17VVM1w7gsVP_3sxAL0zLHa-IRBycL-EJN3-_RkXxvbbr8tAR42Fsi1Zlwv9N7IBSeb3lzG-UYyvVqt7uNyQwoCcqjlpWx6crID1CvGZDPXRpDjGpcJ2Na2pg10SyLZ3bTYgTPAKyo6MlPi9lpIi-BOkX-AEbATKVQ23YRfBwiAhVxI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/684443" target="_blank">📅 12:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: نقش ایران و عراق در ایجاد نظم منطقه ای تعیین کننده است.
🔹
ادعای نتانیاهو: دستیابی به توافق دیپلماتیک با ایران غیرممکن است.
🔹
انجمن داروسازان: بدهی ۷۷ همتی بیمه‌ ریشهٔ کمبودهای دارویی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/684441" target="_blank">📅 12:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684440">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU9CQ_i4-Md9ffod4FpCcm4hitvQ_8KZC8R52FsDwcsAgX4zDQIJLxna_ig4vNKOS0EAKantgAMYHG_Od7q05hDcVljsBwSrTYBnuqog2D3DNGoq5dsA0dOxvKuO9Pi_RQUakbb1JgVG6aQmSvJVHFqi7FeYZa73T_NFbAireJnouhNQbuqzUx3W1zkDpNZxLURBgU_ErjMbbNoy9--J45uW38oAjd7H-OHhW32bWaUJcdHzyhoFxcWdYvDkAIItG8JVh3BCsKLDGNWnA3vARq8_gAZJG1B_hft5_XQhQHX27Tbpleigxwi-G5-w-boS0HEo50jSiQEn_IBEhg-lwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین نیروگاه بادی کشور وارد فرابورس ایران شد
🔹
آیین عرضه اولیه سهام شرکت «تولید نیروی برق سبز منجیل» به‌عنوان نخستین نیروگاه تجدیدپذیر در فرابورس، با حضور جمعی از مدیران ارشد دولت، بازار سرمایه، بانک سپه و گروه سرمایه‌گذاری امید برگزار شد.
🔹
دکتر تقوی‌نژاد، دبیر هیئت دولت: توسعه انرژی های پایدار اولویت هوشمندانه دولت است و همراهی بازار سرمایه، کشور را به سمت استفاده حداکثری از انرژی های پاک هدایت می کند.
🔹
مدیرعامل بانک سپه، دکتر ابراهیمی: ورود منجیل، جهشی قابل‌توجه در ارزش بازار فرابورس ایران رقم زد.
🔹
دکتر سید بابک ابراهیمی، مدیرعامل گروه مدیریت سرمایه‌گذاری امید: علت نگاه ویژه به این عرضه، موضوع ناترازی انرژی موجود در کشور است که رفع آن از اهداف مهم و اولویت‌های اصلی دولت، بانک سپه و گروه مدیریت سرمایه‌گذاری امید به‌شمار می‌رود.
🔹
یاسر سلطانی، مدیرعامل گروه سرمایه‌گذاری انرژی امید تابان هور، این عرضه را نقطه‌عطفی برای انرژی‌های سبز دانست و گفت: منجیل بخش قابل‌توجهی از ظرفیت بادی کشور و ستون اصلی سبد نیروگاه‌های بادی گروه بانک سپه بوده و عرضه آن در بورس، نشان‌دهنده بلوغ صنعت تجدیدپذیر در کشور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/684440" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684438">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/684438" target="_blank">📅 12:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684435">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a402c7d897.mp4?token=hZhXoTbDvEf9FjFE6O_k2MnkOcLTo12Rwdx4fevapTOawgsRT_nRPNCeURlUL_PjHgEUYeQfLCAn2BL5VGqYpyz4DvKmZvzQPgrzeUkpabyu1upbfu4TBXkyghovaPcWT64isVpQ4KA5Oj4odJ8zgEpGKzwoa6sH8YMf15IhIi_ZdtBjNTAndeNoudhd9on6C7PfVENvKa7SQprjtJMi3NX2nTYG97vKAXyk0YV0h5xiGwNEXGQtVAdM6aVRjcCIKJZyQCXe2iWEpEP69XUwvOlldRciQlvMK9alkZix3SL2hsoMq1YLfKklkz2dXZ1-pUIJKVGW70Z0Y_7jCBA-hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a402c7d897.mp4?token=hZhXoTbDvEf9FjFE6O_k2MnkOcLTo12Rwdx4fevapTOawgsRT_nRPNCeURlUL_PjHgEUYeQfLCAn2BL5VGqYpyz4DvKmZvzQPgrzeUkpabyu1upbfu4TBXkyghovaPcWT64isVpQ4KA5Oj4odJ8zgEpGKzwoa6sH8YMf15IhIi_ZdtBjNTAndeNoudhd9on6C7PfVENvKa7SQprjtJMi3NX2nTYG97vKAXyk0YV0h5xiGwNEXGQtVAdM6aVRjcCIKJZyQCXe2iWEpEP69XUwvOlldRciQlvMK9alkZix3SL2hsoMq1YLfKklkz2dXZ1-pUIJKVGW70Z0Y_7jCBA-hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع طوفان شدید امارات
🔹
طبق اعلام مرکز ملی هواشناسی امارات، سرعت باد در برخی مناطق به ۶۰ تا ۷۰ کیلومتر در ساعت رسید، در حالی که میزان بارندگی ظرف چند ساعت از میانگین ماهانه معمول فراتر رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/684435" target="_blank">📅 12:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684434">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riHlS7boKjhjRRF8rTWeondpfBUkVIgTQdXnGnvcX89TvtCtG_vQcgSPz96H-xxGfJWisQQs8_y5MHBCGdRX3EWkOKxLJj4FT84JNSmPJ3oA9ipJW0eNN8Mhl6syU7csysG6LPBJ-tP6gqnb6J66leqVMsOVoklyYMS7M6UjZdtG-NJALo6rJPvsvCwLMRX-eDV_2ssj6Apqp6f8xiWBP-ue7Fii27mml-KqUG0xVQtxMuc9optBmoA_S2qG-t6_fHseabm91yZcyjCE2TtA-lj9K_oGczLjKBHJcrHhZM0UGBq_2ZlZi2JVZecxx_HWm9VpnKzjR4zDCiAYRq9tKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترانزیت ریلی ایران از مرز افغانستان به ۱.۵ میلیون تن می‌رسد!
🔸
حجم ترانزیت ریلی ایران و افغانستان از ۱۵ هزار تُن در سال به حدود ۱۳۰ هزار تُن در ماه افزایش یافته است.
🔸
پیش‌بینی می‌شود تا پایان سال این میزان به ۱ میلیون و ۵۰۰ هزار تن افزایش یابد.
@amarfact</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/684434" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684433">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38579b3344.mp4?token=ts7LlV0-PEKlh4u3XJ4vqKhSHX8o8FaItXyDHJ32EU39s9FHmgMRhIeozkiQpUESl2anClYI74tKFickcDDGVFCVbvqthn4aJ1Y626IjSohwQ9SZSLLxb-cqKnRkUvvxe2NmHTE0J4smZ85hlyENAJY6XKlcWrw0baXt-wyjYkiur7R7fS8khWLfVl--_Vx0zF3bvJwQuKkNDUzdzNvXrLaKhy5ADLvillMMxjAlgaOiTmh--kbNdb0lwoXasNNngANJTD0yC5vrZ41WNw0_OhM7JZIEpH5m6MzDkER2e_PRu2QyVRtGM9ReI7tIm_9NsIsnnoDi2PA_l52SP1IAww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38579b3344.mp4?token=ts7LlV0-PEKlh4u3XJ4vqKhSHX8o8FaItXyDHJ32EU39s9FHmgMRhIeozkiQpUESl2anClYI74tKFickcDDGVFCVbvqthn4aJ1Y626IjSohwQ9SZSLLxb-cqKnRkUvvxe2NmHTE0J4smZ85hlyENAJY6XKlcWrw0baXt-wyjYkiur7R7fS8khWLfVl--_Vx0zF3bvJwQuKkNDUzdzNvXrLaKhy5ADLvillMMxjAlgaOiTmh--kbNdb0lwoXasNNngANJTD0yC5vrZ41WNw0_OhM7JZIEpH5m6MzDkER2e_PRu2QyVRtGM9ReI7tIm_9NsIsnnoDi2PA_l52SP1IAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: تا آخر شهریور هیچگونه تغییری در بنزین ۱۵٠٠ و ۳٠٠٠ تومانی نخواهیم داشت
مهاجرانی:
🔹
تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/684433" target="_blank">📅 12:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684429">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_ibrhJPYbMbaGa4Ta3BFde2489vzIFTirIkBtp-PIHeAp7D78XFfD0buQNmW_YsbznZZhdVQ7KZ-GGNTsQSJn7RVKoOA34nB_DqiiN0owGLvU7aPLFO3NmqxXO1SzEGH_whXDblFiP8Qnp0m5WQQV3FCkppJ6BaEwQ0NuRKmE4EQRzm4S6eynODKAxKQbm2rpE9yPcVGxtELz8j5OmKAcYn6w1i67sULBeqA-751gNv4e3hExuLNVDtOLF11WfFWEOHiqQKPU2f0xyxW619m2rWSbKqbB4D8pYe7r79eU6ZyvhzN2ZEoUpJ2nd9TO5sHNkhSXPlkq0eLsslDfIgQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9NpjtUGZQX3q9EG7LarXAN_u9wRq0K19ytmZynhOJbgrFhp8t0Jb59WTYj_R0jsxOrPhRb6gZft66OEUIyiUVo4v2R435Pp0JP_vp28odoH0kpxhMeStnsyO73rEpeWkI-WBFD4seXLeYB3wOUnhwS1lAfy9PogMGdbP4zvJKrQm-ljbWWOwTYKJTT6-4h99TwC5jvMplD7D31xG5dcQfcvdVmx4Rq8qViPmu93eNhY_KDSAYKeHh4U7rlLnk0DsYDCcWHi17nRsRzzz7ATt4_tNd6z4gAWNORBMtvZiGyneO1r8hD1LO_gBvxsIiN6HFsj9QZc_ePYRcl5TJxrzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6LHRDsl7zc-WDhUdKGNKUS6LSXYj1FA9Dze7JMwxo8mLgp92VLYS1-MkMwXCa1i1VH4tgC1wAtHCJ4M2NEbpczirw_uEKYgC7GsA8pfDPg-_B9VU9T5t_hyYbdj2CULlCA_FCIyRZJ-8ZLPfZE3jT0q5pXLRVRHkyRLnNp0GzxcTaRRugiHWnBIbnMW5dS7eZnoDQbVouzI7hfCAzg7vpAoOjmuH8zhrtFW4T51b2XkJBI5AOglZYEm2_vrokPZaMumzYEVvlOtjBY072A6Oa5x53TyVonLM3yueKH6iQW6KHqnDkJvQ6yVKkvdqEa00-FvHt5eqP201_vO5ws9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRZmx_f5NvdnT_ejRp-Rd_HEElxK3d-6xzP2YYkRVlQB-k_b7dZf-pVcezcaUfx3hSCkO_rNytSPKgl0WXsxaArZz8y5SSqco00TU78OBoVjSl6rDN_sDiC4Avjezu4M54Z1xALZfypfq42yJDEqXVWe4UmzBaEOFq_KHICBCmQfb9-LmsBtl0nJQ4o67Sll4CV_yzBbidzvhgldhv3roo96zkuAQM6_jbTLiZNFkNRPwepZZJP8nPTqIP8bt7z5evpJDKAQZ980bqceBBFA4oXwyEV2SFffuXNpwkzBwKfAt1Z1Oq59tNPRuxKA1yirT426i0lnXxR7DnuNpgZNwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ازدواج خوب به معنای دستیابی به همه آرزوهای‌مان نیست!  #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/684429" target="_blank">📅 12:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684428">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دقایقی قبل زمین لرزه‌ای به بزرگی ۴ ریشتر نوار مرزی کردستان را لرزاند.
🔹
سپاه: احتمال شنیده شدن صدای انفجار کنترل شده در شهرستان پاکدشت
🔹
انگلیس رسما به تحریم‌های تازه آمریکا علیه ایران پیوست.
🔹
سی‌ان‌ان: چین حاضر نیست ابزار راهبرد فشار آمریکا علیه ایران شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/684428" target="_blank">📅 11:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684427">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ac8d7041.mp4?token=nFAkOS5IgHfRH6cb7BjCRArIUIbYmBCueoomCTO0G7hmkbNaYLTpEGnzB87bhWrX0_-fGg-yFc2-TaAWzYnXyJT1aYkFNIa6lnnAxhAieLB4Fi706p8n3VMexA5bC9heuDQgcsxGU2lbItGO2LURHvZVXVbhrU4acApqZ9LhRwNu-eaAXEPgiKFfO91k5605jdfub3RLoncLIx7_Oq4u08C6AHBDMw_zw7Htj3q4WyO-hJ9nlXMFxbYGri3GJFECLWw0bm9ASHEplolCqd-cdtU3Z4DOpviaHwjqrdEYqUslI-O1X4f-EPbPPEs_62KKf32j-EAfdGf6bE2TEgYurw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ac8d7041.mp4?token=nFAkOS5IgHfRH6cb7BjCRArIUIbYmBCueoomCTO0G7hmkbNaYLTpEGnzB87bhWrX0_-fGg-yFc2-TaAWzYnXyJT1aYkFNIa6lnnAxhAieLB4Fi706p8n3VMexA5bC9heuDQgcsxGU2lbItGO2LURHvZVXVbhrU4acApqZ9LhRwNu-eaAXEPgiKFfO91k5605jdfub3RLoncLIx7_Oq4u08C6AHBDMw_zw7Htj3q4WyO-hJ9nlXMFxbYGri3GJFECLWw0bm9ASHEplolCqd-cdtU3Z4DOpviaHwjqrdEYqUslI-O1X4f-EPbPPEs_62KKf32j-EAfdGf6bE2TEgYurw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لپ‌تاپ جدید لنوو با قابلیت باز شدن و بسته شدن خودکار
🔹
این دستگاه مفهومی به یک نمایشگر موتوردار مجهز شده که با کمک هوش مصنوعی می‌تونه به صورت خودکار باز بشه، بچرخه، زاویه خودش رو تغییر بده و جابه‌جا بشه؛ آن هم بر اساس دستورات و حرکات کاربر.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/684427" target="_blank">📅 11:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684426">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/677455779a.mp4?token=CW1tmQmCLSAJCdNP1Qqb4xY1GTF2Bm46QjzxdI51PjtdiGsf0TjYAs6VuLwa58w04ohIJXjtzMgYjwZXsfhTFoS_70SHFzASkAFbqUSK0wU1CBdQgf6O7UE1TGMeU4wi4DMriw6H0MTWAGSvDwIzLbf85fYIRJjXmO57Ivjgi01poqYjKshrlj1Tl6N1JvFbpKxWYZwJso-tb0IPBqaCjhb5hAWy-v_AoT8EMi3UVw2uSC9Jh82dck5yVxij29jpSlGGgaxMxk-t0Xjj_ESeUiLLC4DgWNTpjVvi6ayb8ewhaT8ICKC8H7IPhIQbJcZU-0mdNvzsiTVL4jHlwUVQuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/677455779a.mp4?token=CW1tmQmCLSAJCdNP1Qqb4xY1GTF2Bm46QjzxdI51PjtdiGsf0TjYAs6VuLwa58w04ohIJXjtzMgYjwZXsfhTFoS_70SHFzASkAFbqUSK0wU1CBdQgf6O7UE1TGMeU4wi4DMriw6H0MTWAGSvDwIzLbf85fYIRJjXmO57Ivjgi01poqYjKshrlj1Tl6N1JvFbpKxWYZwJso-tb0IPBqaCjhb5hAWy-v_AoT8EMi3UVw2uSC9Jh82dck5yVxij29jpSlGGgaxMxk-t0Xjj_ESeUiLLC4DgWNTpjVvi6ayb8ewhaT8ICKC8H7IPhIQbJcZU-0mdNvzsiTVL4jHlwUVQuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
انعکاس پشتکار و انگیزه شما در مشاغل خانگی؛ قصه‌های شنیدنی از تلاش، چالش‌ها و دستاوردهای شیرین شغلی.
🔸
اگر کسب‌وکارتان را از صفر شروع کرده‌اید، روایت شما می‌تواند الهام‌بخش دیگران باشد. نام، شهر، نحوه شروع و نتیجه کارتان را در یک صوت ۳۰ ثانیه‌ای، به‌همراه عکس کسب‌وکار برای ما ارسال کنید
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/684426" target="_blank">📅 11:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684425">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d83fca7700.mp4?token=h3RiaXCoQmdwNQz33DyzoAthv1PiL0e8eycNX04vBRU5HZ6F8pkbvfyjeh4Xj5zEjKiQkDfZbEKcQiJf1cOXntdrm7P8llCFzCjxqFEoSed4FOlYvtUauC-wo-GW4ej2erf2_39CVUz-E0XjHV7TRa2-fQy3iklFyLjSbZ6YAUAz2BZUS8tRyY8mP3ygyEvDxOczwLUyZPzvgEkXoHbsCXOqxnzwIKjXy8gTHhVXLtUfKUqsRPdBGlB7cUdIOX7Z257UPWOfe0exy9glucUNk_8ydkQRXFkPeOzdXZylmNnTrkfBrASpjl-HIpamjvMaYnjDZr5lUk8ug57yb4x5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d83fca7700.mp4?token=h3RiaXCoQmdwNQz33DyzoAthv1PiL0e8eycNX04vBRU5HZ6F8pkbvfyjeh4Xj5zEjKiQkDfZbEKcQiJf1cOXntdrm7P8llCFzCjxqFEoSed4FOlYvtUauC-wo-GW4ej2erf2_39CVUz-E0XjHV7TRa2-fQy3iklFyLjSbZ6YAUAz2BZUS8tRyY8mP3ygyEvDxOczwLUyZPzvgEkXoHbsCXOqxnzwIKjXy8gTHhVXLtUfKUqsRPdBGlB7cUdIOX7Z257UPWOfe0exy9glucUNk_8ydkQRXFkPeOzdXZylmNnTrkfBrASpjl-HIpamjvMaYnjDZr5lUk8ug57yb4x5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی دیده‌نشده از حضور رهبر شهید انقلاب در منزل مرحوم آیت‌الله‌ صافی گلپایگانی
رهبر شهید انقلاب در پاسخ به دعای آیت‌الله صافی:
🔹
یکی از چیزهایی که ما خدا را شکر می‌کنیم این است که اخیار و صلحاء زمان به ما دعا می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/684425" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684424">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
دلار به ۱۹۹ هزارتومان بازگشت
🔹
دلار روز گذشته با افزایش شدید مواجه شد و حتی از ۲۰۵ هزارتومان هم عبور کرد اما امروز به ۱۹۹ هزار و ۵۰۰ تومان کاهش یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/684424" target="_blank">📅 11:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684423">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
بارش کشور در محدوده نرمال؛ تهران و مشهد همچنان درگیر تنش آبی
سخنگوی صنعت آب:
🔹
از نظر شاخص بارش کشوری، ایران در شرایط نرمال قرار دارد، اما به دلیل ماهیت محلی منابع آب، برخی مناطق از جمله تهران، مشهد، کرج، اراک و ساوه همچنان با تنش آبی مواجه‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/684423" target="_blank">📅 11:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684422">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c6077a4d2.mp4?token=Flfk41GT5FYBw0OPBn6Hv8pcLzSsgQJJ_-0NfPgtG08aUewTuZkqhNQBd-kmyBuju0zc1tO_nfnluI75nqThj1KGej3kwmjAEieiqR1fY-H22QAPj4M9-3UVwaQbpdMQW9B0TR89q07bE0aKFcBwKzMN4-fFUkAGT8zf1Z8RgwDTnKCYRBEOKfr-XcrAJYscvHll5J5hzyQG6gCx9OmSXsnCPHZlevlPdc82Mvs-Xo_pLRwJGiyV1xhwP327Pxxnu81qPXQkt9mckmcRYL2Pw7LhK9FZKQHftqZFNI7sjNJPkcECesa7CXR2KZ6MYNPvt5QCgnaxV3WQqfLZBOrUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c6077a4d2.mp4?token=Flfk41GT5FYBw0OPBn6Hv8pcLzSsgQJJ_-0NfPgtG08aUewTuZkqhNQBd-kmyBuju0zc1tO_nfnluI75nqThj1KGej3kwmjAEieiqR1fY-H22QAPj4M9-3UVwaQbpdMQW9B0TR89q07bE0aKFcBwKzMN4-fFUkAGT8zf1Z8RgwDTnKCYRBEOKfr-XcrAJYscvHll5J5hzyQG6gCx9OmSXsnCPHZlevlPdc82Mvs-Xo_pLRwJGiyV1xhwP327Pxxnu81qPXQkt9mckmcRYL2Pw7LhK9FZKQHftqZFNI7sjNJPkcECesa7CXR2KZ6MYNPvt5QCgnaxV3WQqfLZBOrUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه یک فیل از طریق خرطوم خود آب می‌نوشد؟
🐘
💧
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/684422" target="_blank">📅 11:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684421">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
انتخابات شوراها ۲۴ مهر برگزار می‌شود؟
رئیس هیأت نظارت بر انتخابات شوراها:
🔹
تاریخ پیشنهادی ۲۴ مهر ماه برای برگزاری انتخابات به شورای عالی امنیت ملی اعلام شده و همچنان منتظر تأیید شعام هستیم.
🔹
زمان اعلام نظر نهایی درباره تاریخ برگزاری انتخابات هنوز مشخص نیست./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/684421" target="_blank">📅 11:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684420">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa78a2f28.mp4?token=UWjUHNvAuSh358dVlHokkDELLEiTi2TA-HlqDJlVO7z0XGUyQKX7Akgkke4sKnVNngSIop2i9LLzjUk35us5Czm51BHwAksBim0T2rVm-q276eBPO60N7tMCju7KWyTdPyVMgcmDlc0yrII-JZds_DvCxhXOq8iL4ILJGvJCOosru0UeIUuok8Qfy-8WPCQBzIR7-kqzEuszpceqnibbl55dtq6nXoGaaZyEZzMMbEgTWjNXFJ8no1GP7wv5FoKejU7IUiilSFi2l4yEGXigYizLUq9MinpaKFk1GVmUoY1rgGCt1cVQiMfr7D5kp_j9kCqqbgfVZ6x4nkiEAo_rWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa78a2f28.mp4?token=UWjUHNvAuSh358dVlHokkDELLEiTi2TA-HlqDJlVO7z0XGUyQKX7Akgkke4sKnVNngSIop2i9LLzjUk35us5Czm51BHwAksBim0T2rVm-q276eBPO60N7tMCju7KWyTdPyVMgcmDlc0yrII-JZds_DvCxhXOq8iL4ILJGvJCOosru0UeIUuok8Qfy-8WPCQBzIR7-kqzEuszpceqnibbl55dtq6nXoGaaZyEZzMMbEgTWjNXFJ8no1GP7wv5FoKejU7IUiilSFi2l4yEGXigYizLUq9MinpaKFk1GVmUoY1rgGCt1cVQiMfr7D5kp_j9kCqqbgfVZ6x4nkiEAo_rWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌های جنگلیِ اسپانیا به مناطق مسکونی نزدیک می‌شود
🔹
مقامات اسپانیا اعلام کردند به دنبال گسترش آتش‌سوزی‌های جنگلی در نزدیکی «بارسلون»، به ساکنان حومه این شهر دستور تخلیه داده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/684420" target="_blank">📅 11:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684418">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRlRyKbkZnWal-xMMG2jMBkDbfcSJOY7KxqUfbtwjbbm79M0jnzJPe_dRr7RnDt2UutIIRBtNRsbBabMFl3FlzKNh7Vbl-Zkk4TJPlfaxeqS2ut3A2R194e0mLAoRGICZMRhPweobNXMTqgSih-TxJ3YJ3NchMwoBg_DPI7C4M_O45XgIH8rHEcUvhrrjeIyBOD4YvrWAVXQCy72gQn8TJpwUr6RZvbkZDZdmyjEjv88Gj6SXYuqjdNP05cmU1SrrfK5XauAkQKkmeauoC1ppQfn7CR1ENHfiWsAnO9djHc_SGm31d8RevwdGv8yWwlDkl0qKcs20ViqVKBMh-w-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واردات لندکروز و مدل‌های LX لکسوس برای ایرانیان مقیم خارج مجاز شد
🔹
واردات خودروهای تویوتا لندکروز هیبرید، لکسوس LX۶۰۰، لکسوس LX۷۰۰ هیبرید و لکسوس LX۷۰۰ بنزینی صرفاً از طریق ایرانیان مقیم خارج از کشور و بر مبنای تبصره (۱) ماده (۲) آیین‌نامه اجرایی بند «ر» تبصره (۱) ماده واحده قانون بودجه سال ۱۴۰۴ کل کشور قابل انجام خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684418" target="_blank">📅 10:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684417">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
زمانبندی فعالیت‌های آموزشی نیمسال اول سال تحصیلی ۱۴۰۶-۱۴۰۵ دانشگاه‌ها
🔹
شروع کلاسها از ۲۸ شهریور تا ۴ مهر است و پایان آن بین ۱۵ تا ۳۰ دی خواهد بود.
🔹
امتحانات پایان ترم از ۱۹ تا ۲۸ دی شروع می شود و تا اوایل یا اواسط بهمن ادامه دارد.
🔹
سال تحصیلی جدید حضوری است و کلاس ها مطابق برنامه آموزشی برگزار خواهند شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684417" target="_blank">📅 10:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fc419b68.mp4?token=rVyoDk-yCZhprmajMrLJkhrh7CsXpawwsrln6zj5AX5cTF2GmfEKVImPySvBXnT93h6bn5pDoi4eOYr15igKfjMOHf_Yvs1r5TvD-CLehAwkgIwjXDJn7ka4SGVYCmQw1LnQdMy78kXUZrL5WnEsSHnds8X8M_Knxfeg2kNvxyopRoNunLQ3vghdU2MXSMRNqXVgDWJ3UuYUdBLeAsD1Mmk4cKvbe0qE5xWabhk2OSjJ1fQPMBj5EPdoUw0FBRQy-ueRThoHSX3h-ugdaI-O-jPRve4ddt-xO1zGUG65OLeGeyZa1Sg2N_rNFJbm46S6CiIwwHjrBmf0naY6TQaWKUFum_XSzQbMOX8-3XR72BEWPsWKV0i1X4iK1FcKaptWvHIrlTcoqRQXyJ0KFGHW1cGF3m36BdJU3FGFgBnM-NDVWNzEArq5HmpPLiBTSRv3x3nxrnDUPVCTOHafLiItGUre1gOW2lLjpwA4j02Eg7nFHRch5qoHt-5RYqyd7EmIsRNmiB0-UWJ8UtGz4WNLW10_uH2jqajopqv49slgIs0IfjLkMxI0v0uOJVymeIPFWjT1Q3YVQtaedLTJKznh_TquvWUkczI5B94UPpuddxbYBC3slZ7425u0E6afr8sWkpWtTsgdxEBT9Bjyeqitd2M7Vo_Vp3L4N0ji2gKUJo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fc419b68.mp4?token=rVyoDk-yCZhprmajMrLJkhrh7CsXpawwsrln6zj5AX5cTF2GmfEKVImPySvBXnT93h6bn5pDoi4eOYr15igKfjMOHf_Yvs1r5TvD-CLehAwkgIwjXDJn7ka4SGVYCmQw1LnQdMy78kXUZrL5WnEsSHnds8X8M_Knxfeg2kNvxyopRoNunLQ3vghdU2MXSMRNqXVgDWJ3UuYUdBLeAsD1Mmk4cKvbe0qE5xWabhk2OSjJ1fQPMBj5EPdoUw0FBRQy-ueRThoHSX3h-ugdaI-O-jPRve4ddt-xO1zGUG65OLeGeyZa1Sg2N_rNFJbm46S6CiIwwHjrBmf0naY6TQaWKUFum_XSzQbMOX8-3XR72BEWPsWKV0i1X4iK1FcKaptWvHIrlTcoqRQXyJ0KFGHW1cGF3m36BdJU3FGFgBnM-NDVWNzEArq5HmpPLiBTSRv3x3nxrnDUPVCTOHafLiItGUre1gOW2lLjpwA4j02Eg7nFHRch5qoHt-5RYqyd7EmIsRNmiB0-UWJ8UtGz4WNLW10_uH2jqajopqv49slgIs0IfjLkMxI0v0uOJVymeIPFWjT1Q3YVQtaedLTJKznh_TquvWUkczI5B94UPpuddxbYBC3slZ7425u0E6afr8sWkpWtTsgdxEBT9Bjyeqitd2M7Vo_Vp3L4N0ji2gKUJo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر الهامی: پدافند هوایی در آمادگی صددرصدی برای دفاع از آسمان ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/684416" target="_blank">📅 10:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCLPIZpiyzk5LEmuD_Z4Hx748Tq4WE8ON3L4PJCG-M-vZkreLEOe19TUBoVnBn7Po-KTSOyeB7HDWAc1TaRGHABp9E9jNGdVfJqum65Ad6mvuGYObO_ImNgTeTD9TifaYsNpeIeEWczSDlxeF4rHCTuUEtN_hwD1R8UADLEVL3OwvyQyqsiYZXRNewm0VsejpVVE4aQtAS366gpaxwQ4bml4_tx5QU_Zi137wYk-2E7dT4ZS5MYcZDw2FinA5KKUy-2tn_bwWxnpIO2OR6vi9SJ-EUDgMrbXA2PVMYJekDI0x3xgYM2ZFKlfwgAc3sSKlj6VmyYQcA_vFrM-vAG11w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: قدرت آمریکا در برابر ایران شکست خورد/فشار اقتصادی هم بعید است موفق شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/684415" target="_blank">📅 10:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff3fa3920.mp4?token=CjFn-ZiVjjl1qB_wsHQj1Fc4DNAdsFN9OP0mgMBQrxit-jo-mmoSLI9yfpizPFNkIiewsLnZppj664TT1_41Ys3q0vNtzvM98CEeAX4VzNQpsMgUTuFBnr7l3ZDauGepORQg0_e2zZHD6fzUl-SrxM9ylcG4E35DVa2jLAe0S9d1g-MG1TVHv2Sz_IZUCa7zwbEV14sEEv9INtVSpvEB9387teP09Qn985rquva1zP8Y8gLiST6zHVMlw3t9NLf69LaGGTkOiQMZ-Qwda9u1HBVXNtHQv2ZwaNzfeRKh-OySzKXUPLyFX9S5t7SQehjloSLr9Nbfzn790z191G32LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff3fa3920.mp4?token=CjFn-ZiVjjl1qB_wsHQj1Fc4DNAdsFN9OP0mgMBQrxit-jo-mmoSLI9yfpizPFNkIiewsLnZppj664TT1_41Ys3q0vNtzvM98CEeAX4VzNQpsMgUTuFBnr7l3ZDauGepORQg0_e2zZHD6fzUl-SrxM9ylcG4E35DVa2jLAe0S9d1g-MG1TVHv2Sz_IZUCa7zwbEV14sEEv9INtVSpvEB9387teP09Qn985rquva1zP8Y8gLiST6zHVMlw3t9NLf69LaGGTkOiQMZ-Qwda9u1HBVXNtHQv2ZwaNzfeRKh-OySzKXUPLyFX9S5t7SQehjloSLr9Nbfzn790z191G32LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرت زدن راننده تراموا در سانفرانسیسکو و برخورد با تراموای دیگر
🔹
راننده یک تراموا در سانفرانسیسکو هنگام حرکت به خواب رفت و به تراموای دیگری برخورد کرد. خوشبختانه این حادثه تلفات جانی نداشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/684414" target="_blank">📅 10:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuyf6H28r585yKhuTEimyx2QpwJ3sEUst0RmJyzbX1BXg6rbQqquAfZYgCg3Z8QWSRavLQD5ZypIV_kYaL6J-wzyAdq_v-6797pgixoVDi9dXYRjWuOnnEJLCse9lGv1fwOib-nQ4xuSzmCNYm9DsICkOIMLCNpCLJiF-5RlFqvYN8wkJuJY43-1tMRC09LkD-DVrN1yYHFN6twh2JuouqPSgOD0tHGFgU6RnPbpvcxWBpZcVUO-wcziMHzEKe6MIsrExuJL8GYRDsqYI0ncXCWk7mtVevmFLvSHctRcDI6VaWCMliACzGLt3JF4JzoIKwmvCkw2lmQ8S_AW-AC7mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ جدید مالیات و عوارض ارزش افزوده محصولات دخانی وارداتی اعلام شد
🔹
بر این اساس، نرخ مالیات و عوارض ارزش افزوده در سال ۱۴۰۵ برای سیگار، توتون، پیپ و تنباکوی وارداتی ۹۰ درصد تعیین شده است همچنین نرخ مالیات و عوارض ارزش افزوده توتون خام وارداتی ۱۰ درصد و توتون فرآوری‌شده وارداتی ۳۵ درصد اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/684413" target="_blank">📅 10:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e896b023.mp4?token=TnqTPWelkrQAevAL-hkaX-yNSLngLb7wE5GnuAas6pSr3ctS8aih8osbQGLmo4E5jqxl3ExnDGXfc0g0nfXKIOz9ogTDRNY_qB83QG2Phrn1C1iLHpqfeqrlm5Ex1kBwSOFUKvkBLb53bS-QfIeJOZuOC9MM2Y-cUMZVUEeb__yXl38YA8hXvC-OE51sa7Fp8Z81yjUOV4uQm7ZdmFBLMsjqNa84JVRkuEbdc0QFsPJlZqTDVkOmFzHgdGqdSw_AR9cMGMg7qhkoexgmrw5hhjx5fZ32YKod8pCB0C3hEz98zsLdXyWE3D-ewnPPDeX2L1uOG0d8aft50wS5v-RNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e896b023.mp4?token=TnqTPWelkrQAevAL-hkaX-yNSLngLb7wE5GnuAas6pSr3ctS8aih8osbQGLmo4E5jqxl3ExnDGXfc0g0nfXKIOz9ogTDRNY_qB83QG2Phrn1C1iLHpqfeqrlm5Ex1kBwSOFUKvkBLb53bS-QfIeJOZuOC9MM2Y-cUMZVUEeb__yXl38YA8hXvC-OE51sa7Fp8Z81yjUOV4uQm7ZdmFBLMsjqNa84JVRkuEbdc0QFsPJlZqTDVkOmFzHgdGqdSw_AR9cMGMg7qhkoexgmrw5hhjx5fZ32YKod8pCB0C3hEz98zsLdXyWE3D-ewnPPDeX2L1uOG0d8aft50wS5v-RNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترشی کلم؛ یک ایده کوچک برای یک شروع بزرگ
🔹
در کمپین #چرخ_زندگی تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه کم، امکان شروع دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار سراغ یک ایده ساده و کاربردی رفتیم؛ تهیه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/684412" target="_blank">📅 10:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNrLiBsfuRgdf10sFWwqJs3jDOmXLUVff0L5bttZwx1PJrgwE4_bTo3GYo1EFekOuQaE9DVceNl7gQv64dGA1uZUUpRLc8MbqDkgfiNaWSmYymvRXHxqK6UhASj8yM3zTNPrCtUxwK_6HRFVl9vzBA8K_HIcnF4o1V3RH5c-fCu1qOrGNJNLk1UMioX0AddJ-txMvXZV3zJLxArG_HqwdKo7uLy5USx568GFGfY0CY16a2V4ErhA2GQtH2HctNElTsu8RqbCq0PKIDbR9uJfaIj85NmYMOcbg1OjmGAPdhKRrCOYdn7FVflOg6J3RLIlFhQ6wjio-n1aAQYpl7i1Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/684411" target="_blank">📅 10:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igWwhLmuk3Otq-yUuL9epwLzFKRGGFd9hc9z7r9komXKK-0ZdMu3S0TAt6vGsNq3OTjSvGFjA4TftfrDe3eGQYKsEvaNnHmh-a7bz493sGXRHpb7INNQ87mSLL-8RiHzVJKAalZ9T2wxBa5wzXGvgPv5OhmUuW6dHGHRiT3QvtLp7RqWmuPaQhDnC6PK2ljL2YkOhQo254AvIS8a_i85rhiu99Ae38igofLwSpV4xqBzsCGDBSa4jMrgYt1TMZ_rJ3qrrKNhXeTK1Ur3DqBbFhyelsMAuxi2Mn7A2zhoDA0q2WHf6rOaR2eklDWCfncDwgBTN_6BjnJf4OUXGvFR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا از شیر کیهانی!
🔹
عکس روز ناسا که «تلسکوپ فضایی جیمز وب» آن را ثبت کرده است، «سحابی سر شیر» را به نمایش می‌گذارد.
🔹
سحابی سر شیر، بقایای یک ستاره خورشیدمانند است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/684410" target="_blank">📅 10:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSeCpDwJCgXzc4gzyQv5uQ6BQuJLMG1LqOZwsx6VEge99EbD-toVGyi0GnRDKnqdtOGz2tBfWkmUF-OJXv1rFIGVqgCQLllTash7bHAG5WDt6Hw2qJYecJFRFFGil5sEUDWv6NAtOzCZwmkZyPfwHfYpbupAMH3-QTGJV1eAFATKm04eL-t5NT6TCo1y9b-qE7DS_QGN5ZUIXdYmSYkTJUSFH-NStBx-OF9L1AhzKSRuPKpEdE9t0O8N61hBz2UCG5Fyrqoqrot4q0igZEidD0tkhfJLuffcWcUXyGIafyJEGAeE2EGx09Jq4BDHA4XRr1Rw9MCH4AFm6SOe7qEp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار چین به آمریکا به‌خاطر تحریم ایران: تلافی می‌کنیم
نشریه انگلیسی فایننشال تایمز:
🔹
چین به آمریکا هشدار داد که ممکن است به دلیل تحریم‌های ایران تلافی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/684409" target="_blank">📅 10:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684408">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
کالابرگ خانوارهای باقیمانده از طرح یارانه غیرنقدی فردا شارژ می‌شود
🔹
فردا پنجشنبه ۵ شهریور ۱۴۰۵ کالابرگ خانوارهای درآمدی با رقم انتهای کد ملی ۷، ۸ و ۹ شارژ می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/684408" target="_blank">📅 10:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده نیروی پدافند هوایی ارتش: سامانه‌ها و تجهیزاتی را که در جنگ ۴۰ روزه امتحان خوبی پس دادند، تکثیر می‌کنیم.
🔹
فرمانده پایگاه دریابانی میناب از توقیف ۲ فروند شناور حامل سوخت قاچاق در این شهرستان خبر داد.
🔹
رئیس سازمان اداری و استخدامی: تبدیل وضعیت نیروهای شرکتی هنوز به قانون تبدیل نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/684407" target="_blank">📅 10:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684406">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13241e502d.mp4?token=H95JkFAlbB_LgfTind_VM_YTbEBrKm2aIjyZ7DvxgM4Ax46_YavDFPXjjXGcErbkMl0rKyUjNAUfd4xLqB4lze4g400GdOR43TJGFm6-dSLS_Xs88B6YzDoMdkwLgKn-vAgcdwo9AIhGscXygLeCs8yGIoBngEPRE0V8-KgNKRv6Q5UbWoVJ-Pxt-MER8ZXQH4RqdZap0hyWkKtN1bwN250oKxEO_gq3R4AR3-BfxyoRRmljwXIZ5TTxhgcpuuKXgi1vPJ1SS5hYwIAsjgpruZdvC4DYBIVMk_kpTcoNjxnzGHSri3VYgIezIxAIqn2tjM4PgAro3ih2XgWmLIJYPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13241e502d.mp4?token=H95JkFAlbB_LgfTind_VM_YTbEBrKm2aIjyZ7DvxgM4Ax46_YavDFPXjjXGcErbkMl0rKyUjNAUfd4xLqB4lze4g400GdOR43TJGFm6-dSLS_Xs88B6YzDoMdkwLgKn-vAgcdwo9AIhGscXygLeCs8yGIoBngEPRE0V8-KgNKRv6Q5UbWoVJ-Pxt-MER8ZXQH4RqdZap0hyWkKtN1bwN250oKxEO_gq3R4AR3-BfxyoRRmljwXIZ5TTxhgcpuuKXgi1vPJ1SS5hYwIAsjgpruZdvC4DYBIVMk_kpTcoNjxnzGHSri3VYgIezIxAIqn2tjM4PgAro3ih2XgWmLIJYPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باور می‌کنی فقط با جوشوندن شیر بتونی همچین دسر خوشمزه‌ای درست کنی؟
🍮
مواد لازم:
🔹
شیر
🔹
نشاسته‌ذرت
🔹
شکر
🔹
زرده‌تخم‌مرغ #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/684406" target="_blank">📅 10:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvDH2HOxzPFsTytYVOuEI49O1CJ2K-udpmDJRq202ISC0SOdXaZCCUPeQS2yjUUI5pn-Wyn_-2D1FFQ9hkDc5ZffhFWYUiVxtDhE1XROb7MuNrrDUXYOSOcDV8Icnl3pfHNDyLAx0x_Ctk9zuVFjxhzMCPGqXzNgk5XKEGWxZQH2yrl3EQbvwnIxGPRi5M5EbVobF7cG-DXby4lDUBkxAPAwmCNtJo2oEyRla5c-dG80JkC5RyB3kj1-uQnhe_hxCN2N_0MuIQgQ6HQDPzZlYq0jTkJxuIHN07ob-iYzV295maqQ1BYra83hQG12bWFs4Tl-8ouZ06QARDxf9zrQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام با قابلیت جدید First Draft ویدیوهای ریلز را خودکار کوتاه می‌کند
🔹
اینستاگرام ویژگی جدیدی به نام First Draft معرفی کرده است که با کوتاه‌کردن خودکار بخش‌های ساکت و مکث‌های موجود در ویدیوها، فرایند ویرایش Reels را ساده‌تر می‌کند. این قابلیت چند کلیپ را تحلیل می‌کند و یک نسخه اولیه از ویدیوی نهایی می‌سازد تا کاربر بتواند آن را ویرایش یا منتشر کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/684405" target="_blank">📅 09:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684404">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9083107f6.mp4?token=EKlZ_N3kZruNjL1-NrDTUUUWYPx29rfGCKwYzXyWq3URg3QSO9juaTIzeP0u4G5IriTNF2S0CS9TaIvg2g9IzlJMc6jvndzdvUyB7G7VNx8S39LE9eDH6d4Iu1aMOmV51mMYSApPBVI4Ampm8s1rOUnOGG55iwLipYrl3nxG8RQFLzxtB8AR7fabyO8sRJlgnfiHWhwrDj086AQX3kNREbP9S4VJpc40wLfT6cjaL78ET5xwhQJQ2mAPFvZzELyBok4fAv1hH6e8_tn49sF9mWmLD5suaqXnV2OA0hnbNpChcohGRCkBXX7enwhylG0ZkOR5ENUB0salxbJ6geuJdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9083107f6.mp4?token=EKlZ_N3kZruNjL1-NrDTUUUWYPx29rfGCKwYzXyWq3URg3QSO9juaTIzeP0u4G5IriTNF2S0CS9TaIvg2g9IzlJMc6jvndzdvUyB7G7VNx8S39LE9eDH6d4Iu1aMOmV51mMYSApPBVI4Ampm8s1rOUnOGG55iwLipYrl3nxG8RQFLzxtB8AR7fabyO8sRJlgnfiHWhwrDj086AQX3kNREbP9S4VJpc40wLfT6cjaL78ET5xwhQJQ2mAPFvZzELyBok4fAv1hH6e8_tn49sF9mWmLD5suaqXnV2OA0hnbNpChcohGRCkBXX7enwhylG0ZkOR5ENUB0salxbJ6geuJdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کلکسیون فوق‌العاده از ساعت‌های Jacob & Co
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/684404" target="_blank">📅 09:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
جهش بلند ۱۵۴ هزار واحدی بورس
🔹
شاخص کل بورس تهران ۱۵۴ هزار واحد رشد کرد و با فتح قله ۶ میلیون و ۳۷۸ هزار واحد، انتظارات فعالان بازار سهام برای ورود به کانال ۶.۴ میلیون واحد را بالا برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/684403" target="_blank">📅 09:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اکسیوس مدعی شد: ویتکاف و کوشنر برای پیگیری پرونده ایران به «سنتکام» می‌روند
اکسیوس:
🔹
انتظار می‌رود استیو ویتکاف و جرد کوشنر، نمایندگان کاخ سفید که هدایت مذاکرات با ایران را بر عهده داشتند، امروز چهارشنبه از فرماندهی مرکزی آمریکا (سنتکام) بازدید کنند تا درباره وضعیت میدانی منطقه توجیه شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/684402" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5RpGO2T0Ec1XY-gzUkte_lD7HqpDrNpRPOaTFPeAenibGEWaM-DC-vx2SPdLoPHiPSQ2_kF-5_UpfprxxXJCHNVDG9W2BUY4oEuuZx0kYhyOQ_fIFZhzsrlcrXQl4-XFOI9K5FFiM-I4RU8kShtsTN9KthDNXNxVpDsZp748wtAw0QvUmRUg1i_MlDXRi1nJbPoipqjVP9ykT3OSg61AC9nWXK8a9RuGqot0ZuPsNRHKImEzefUqdeFekIQ2NrgWleu8AcP25f59f3W_0AKS76QvY3snpeygb59OCfmPdDpOPgRw2y37rCwU9V83KdhEdz3LKXV8cYeTQ_OY7UpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی، ترامپ را به نفع بردن از جنگ علیه ایران متهم کرد
سناتور دموکرات آمریکایی:
🔹
ترامپ کاخ سفید را به یک کازینوی پول در ازای بازی تبدیل کرده است‌
🔹
ترامپ از زمان بازگشت به کاخ سفید میلیاردها دلار به جیب زده است.
🔹
واضح است که ما رئیس جمهوری داریم که از جنگ غیرقانونی که در کنار نتانیاهو آغازگرش بوده، نفع می‌برد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/684401" target="_blank">📅 09:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684400">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی دولت: انتشار اطلاعات میزان فقیر بودن مردم ایران نیاز به مجوز شورای عالی امنیت ملی دارد
.
🔹
آغاز ثبت‌نام دکتری بدون آزمون دانشگاه آزاد از امروز
🔹
رویترز به نقل از داده‌های کپلر: طی روز گذشته تنها ۵ کشتی از تنگه هرمز عبور کردند.
🔹
حمله ارتش تروریستی آمریکا به یک قایق در کارائیب و کشته شدن ۴ نفر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/684400" target="_blank">📅 09:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684399">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25b806c1fc.mp4?token=YXWn8xmWPhHkJZlUWfA64AN7-XtoEv-5v7oKbTKMWKQT5NX22CF-NfnhVcf09xQHIjtGGVjEcEBPmQeDxALW2ejLLzHX6Sv-as2uqAxucM_8I6vom4YtAMHCu6ghT9JdejwaXPdiznXGS96Vzq45ZRBoE_801iHCh5FAYYVjFWwbAFRJss2-Vxt_WgswF0-oSEY8GqS5Gn6XghODEskYx4KQKUnctb_8z6-3nIVKuKdGMlfLC-C2R8z287dYK-Bd3_YkNPAhJTSPHIp3TLeq4qwreejD6bBdOSTKc9CuMCp03zI-e_V0IwlyNLB-Ep28ovCKm_eVXskk-OotXv2gKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25b806c1fc.mp4?token=YXWn8xmWPhHkJZlUWfA64AN7-XtoEv-5v7oKbTKMWKQT5NX22CF-NfnhVcf09xQHIjtGGVjEcEBPmQeDxALW2ejLLzHX6Sv-as2uqAxucM_8I6vom4YtAMHCu6ghT9JdejwaXPdiznXGS96Vzq45ZRBoE_801iHCh5FAYYVjFWwbAFRJss2-Vxt_WgswF0-oSEY8GqS5Gn6XghODEskYx4KQKUnctb_8z6-3nIVKuKdGMlfLC-C2R8z287dYK-Bd3_YkNPAhJTSPHIp3TLeq4qwreejD6bBdOSTKc9CuMCp03zI-e_V0IwlyNLB-Ep28ovCKm_eVXskk-OotXv2gKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملهٔ پهپادی اوکراین به یک پالایشگاه روسیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/684399" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684398">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa7gSnQV2Hs949-Cs7lOflTUVCrhg1Ur4jO7VZKIKXY1a5bEzAm1wTBxnxOYTVgd-BmwW1c62JWrkdL2a5ke9FheE3Hdbmu85bha0D7JHyWVdziCJoE-w5_appK4M1SSH9alnwQ7vdfwydf8HoqrIVMuVQtbvCKIyZtYua0YKQRareIUGxuiCGXbL-zUVm84LiIzsA6AiiOCULisRWUmp6czaOLvGuSxKFPyoyQn8BFaa7IOwQ3FIx_Uwk8ZLW0hDcEsBJfJ6t1IFzlCvqlCrTM6mICYO6ZV3MLLzZlwmKQvkSrlSx8fFqO0IjB1nhLWpmXVxrg7i7r4ytTFiMLqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت: ۸۶ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/684398" target="_blank">📅 08:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684395">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bec075ebb.mp4?token=H0ZIy1vNazJzZg1yFr9nTZSDt__vKRnq9a4gQaRcE4pFS-UM45gK9izpFwCrncvsdt1GKHng_JtQeNdzZliSs_E5rfWHOX9npYZkVMX9T6fGcK5NIoRJ87E7PVQzIjHwYYuyRCS3iJJZBfYbLOIft6-hvWXcnfAgCRKloYVaEP6vGW1vKgDefPf3OpjwU0nY5AFvJO_glDdqzIax5VaUPQQCwDQ-p21PVnvreyPeHUnqjND4NMrsEJoHwN6empJOEGdebFyd-qBmhdBNNZYvrFIa7eCf9aeXXQtwLNBLD8o6U9hlvhAafLHxgQmkOJqE0_i4kof2TSyrz8ZaEyXBrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bec075ebb.mp4?token=H0ZIy1vNazJzZg1yFr9nTZSDt__vKRnq9a4gQaRcE4pFS-UM45gK9izpFwCrncvsdt1GKHng_JtQeNdzZliSs_E5rfWHOX9npYZkVMX9T6fGcK5NIoRJ87E7PVQzIjHwYYuyRCS3iJJZBfYbLOIft6-hvWXcnfAgCRKloYVaEP6vGW1vKgDefPf3OpjwU0nY5AFvJO_glDdqzIax5VaUPQQCwDQ-p21PVnvreyPeHUnqjND4NMrsEJoHwN6empJOEGdebFyd-qBmhdBNNZYvrFIa7eCf9aeXXQtwLNBLD8o6U9hlvhAafLHxgQmkOJqE0_i4kof2TSyrz8ZaEyXBrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به حرف‌های مفصل زانو گوش کنید و آنها را جدی بگیرید ....
🦵
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/684395" target="_blank">📅 08:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
«مافیای سرقت مسلحانه کشور» پای چوبه دار؛ برادران نجفی اعدام شدند
🔹
حمید و سعید نجفی، اعضای خشن و اصلی باند سرقت مسلحانه که با ارتکاب بیش از ۲٠٠ فقره سرقت مسلحانه، تیراندازی به مأموران، فراری دادن همدستان و تهدید شاکیان در استان‌های تهران، البرز، مازندران، قم و اصفهان اقدام به ایجاد رعب و وحشت می‌کردند، پس از طی مراحل قانونی رسیدگی قضایی و تأیید حکم اعدام در دیوان عالی کشور، به دار مجازات آویخته شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684394" target="_blank">📅 08:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684392">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34728cc8dc.mp4?token=jxNc1BDo841NBtwR8hn-oRV_BX2xZLh-viVo8zlS85oxyE97GB3IxviWCM5A2Vlnaf11Zm8DD35LINhevtMKAPdNtUfpQTR0Th3donKStYXYaxXumPibKqmJMugSiwC7cmLsQOrsvTwwRjN7Tdu3clUl0MeHdZ1AQygZOTu3-8BG9GcsjThGSSvuBugRIq6FzkZA7luBbYj22AeAUpbgU3meXhg11o1aFqbfm3F3GTFdKtijBqqY2wZKK9y9DnqJpWROhaia-iqpxGY2jg75r-ch3xfCjPJaX3MTm2EEiFRFb2XY9YAOxW-dpNa4sqzYkjPfhQvbKsxz7fqZ64rG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34728cc8dc.mp4?token=jxNc1BDo841NBtwR8hn-oRV_BX2xZLh-viVo8zlS85oxyE97GB3IxviWCM5A2Vlnaf11Zm8DD35LINhevtMKAPdNtUfpQTR0Th3donKStYXYaxXumPibKqmJMugSiwC7cmLsQOrsvTwwRjN7Tdu3clUl0MeHdZ1AQygZOTu3-8BG9GcsjThGSSvuBugRIq6FzkZA7luBbYj22AeAUpbgU3meXhg11o1aFqbfm3F3GTFdKtijBqqY2wZKK9y9DnqJpWROhaia-iqpxGY2jg75r-ch3xfCjPJaX3MTm2EEiFRFb2XY9YAOxW-dpNa4sqzYkjPfhQvbKsxz7fqZ64rG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طراحی موتور موشک با هوش مصنوعی؛ از ایده تا آزمایش در ۱۴ روز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/684392" target="_blank">📅 08:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684391">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47eb2b4939.mp4?token=Hgw07H3WQ9W40AKQqcFZGNLi9NBKBxV9HVVeigNdkNNfsenHos8_z99JdLjSZOeOB3_-4LMjT9Y5OUzNQCG8YtavLSsGfCmycXmVu6nczhRVo8xZfjpyAeCX4_4Z7tucMbS8PCsN4inCcOorjegGPsHyuqMSBMg8kBnLVZ7U5xVprv57Ylq4ffM8S6mayUnKmo1N28ZqxOsvLrLmdOcWkvlsu2-7NUU-e8ZGWUCi8_ss2vuzI2ITmcXPXDgI4b1UTYDfU6Q_mi1zV0nmygAtpsA8PZbE-TJD2kdJDQ9EURnvKqpptAJ3zK7gftEo5xRCHzMXDRX7_JA1AFSY_KeZyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47eb2b4939.mp4?token=Hgw07H3WQ9W40AKQqcFZGNLi9NBKBxV9HVVeigNdkNNfsenHos8_z99JdLjSZOeOB3_-4LMjT9Y5OUzNQCG8YtavLSsGfCmycXmVu6nczhRVo8xZfjpyAeCX4_4Z7tucMbS8PCsN4inCcOorjegGPsHyuqMSBMg8kBnLVZ7U5xVprv57Ylq4ffM8S6mayUnKmo1N28ZqxOsvLrLmdOcWkvlsu2-7NUU-e8ZGWUCi8_ss2vuzI2ITmcXPXDgI4b1UTYDfU6Q_mi1zV0nmygAtpsA8PZbE-TJD2kdJDQ9EURnvKqpptAJ3zK7gftEo5xRCHzMXDRX7_JA1AFSY_KeZyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این حرکات انجام بده تا درد مچ پا برای همیشه رفع بشه! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/684391" target="_blank">📅 08:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کارشناس مسائل آمریکا خطاب به تحلیلگر ضد ایرانی: پکن زیر بار جنون واشنگتن نمی‌رود
ابراهیم الفریحات:
🔹
مسئله برای چین اقتصادی نیست، بلکه سیاسی است| اینکه به چین گفته شود با چه کسی تعامل داشته باشد یا نداشته باشد، نوعی دیوانگی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/684388" target="_blank">📅 07:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3J-yetV14jNNrDvjLNOuyN0HM1f-6FBQq6uz-V7KpiGa10fkoz_CV9jNBi5qSLyK5i5gzHisjLsMAtN_zmxa_fBHh25RKquJ65UBcuPJpcuJJTjKyrc9xDePYibXC8NdANiGhEDiWbXolR_ZvrjEvIApXiySeENA4fWoLP28LTYEqGU_OXQwrQVpcwOZDMb7X_FQMwbP-R3t1lMWH7njk7T38GNiVjiiLhKh0eLhZ_zUMDNcAzyH19Wrv-Xn5JKHWpdiwOyu-eCeeXbyd4rZ_ANQLnTXZhtH18rLc8yHRjB2nSZxs3PE0ZPdGH4Fy2fMXJhYdACJwZOYv1hTxrfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۴ شهریور ماه
۱۳ ربیع‌الأول ۱۴۴۸
۲۶ آگوست ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/684384" target="_blank">📅 07:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای خبرگزاری ریانووستی:‌ واشنگتن و تهران بر سر آتش‌بس توافق کرده‌اند؛ منابعی در ایران و پاکستان این موضوع را اعلام کردند
🔹
این آتش‌بس شامل آزادی کشتیرانی در تنگه هرمز خواهد بود، انتظار می‌رود اعلام رسمی آتش‌بس طی روزهای آینده انجام شود.
🔹
پس از آن نیز مذاکرات و یک دور نشست‌های فنی برگزار خواهد شد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/684383" target="_blank">📅 02:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684382">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1roYXvlfG0JlAhbt0pgS3sPxUjPamzfSlmHg32OdofoQeMgU7nlrm6pUNhq-fByBzW9lW8_qtS4KIRhfxwtEJgBffU--Xc1ZbHOmHKLsvaoZg3NpmxdLH1-uTN3iueibJaulaP9hGRHj6_GTnSHCyPsLVyL45x344VNjXtEeq_XM4h0y_ZChIVQEe5Q7DfHjz98YLFELs-tuZOl6Ak4-iMSm0ys4_0kXlfoNeJdvW744rHRqTxf_enyI2a-LNkdJ0l_69WsClzUVF1QwZ-1ygEzeZ6_Y0R9PiHhsEtwFhcGHvEpKgaMgWuMsTP5OGgy3ZeHIUCn2m0Z1-coy30lKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
گوشی نوکیا 105 | دکمه‌ای، ساده و بادوام
اگر دنبال یه گوشی دوم، سبک و جمع‌وجور هستی، نوکیا 105 انتخاب خوبیه
👌
🔹
دو سیم‌کارت
🔹
منوی فارسی
🔹
باتری ۸۰۰ میلی‌آمپری قابل تعویض
🔹
چراغ‌قوه و رادیو FM
🔹
صفحه‌نمایش رنگی ۱.۷۷ اینچی
🔹
ریجستر شده و آماده استفاده
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔴
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
🚚
پرداخت درب منزل
✅
ضمانت تعویض ۳ روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63518/180124/</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/684382" target="_blank">📅 01:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684381">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b8388dc3.mp4?token=RcWyBFsEEechDNFBpn5cEDwz4bDL6b3En92WLf8B_stOrSPqkCvKO8Ep3isvC8zuvQwZHPbLCxaxtN_7R8w58sUgUHaAe3tn0iCJ_bgqaxECARTWVIkOdGRdFaLlFG6KPC6XT97AM79JkdkUOYJozeE_jzfr4MHfQ6we9EpNNiqcFYaUEowk-SpuvXmt7fQNsTRdbwRA40cmS6kNV2Ijeb7b3ntlouSCr8vJNTQPlI4acJ92326zLwiedS9HjAbYJ4zpPhkzZ8Ri00Asi4Zg6PLRHidAEpMNf6r3O4IdIaNGAI2u1LAKdZFbP1jw3T0KcqO5-CZmcLUXGBk2y2SVsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b8388dc3.mp4?token=RcWyBFsEEechDNFBpn5cEDwz4bDL6b3En92WLf8B_stOrSPqkCvKO8Ep3isvC8zuvQwZHPbLCxaxtN_7R8w58sUgUHaAe3tn0iCJ_bgqaxECARTWVIkOdGRdFaLlFG6KPC6XT97AM79JkdkUOYJozeE_jzfr4MHfQ6we9EpNNiqcFYaUEowk-SpuvXmt7fQNsTRdbwRA40cmS6kNV2Ijeb7b3ntlouSCr8vJNTQPlI4acJ92326zLwiedS9HjAbYJ4zpPhkzZ8Ri00Asi4Zg6PLRHidAEpMNf6r3O4IdIaNGAI2u1LAKdZFbP1jw3T0KcqO5-CZmcLUXGBk2y2SVsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاقاتی که بعد از خوردن تخم مرغ در بدن شما می‌افتد
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/684381" target="_blank">📅 01:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684380">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_Il33ICllM99-qJg7K0i-BiK_qEkV_XVkYZL0FGMoAMf457z7oN1reoTtakdUkfPta3Jb_xTKASegUXWkhJZ1gFVtJsFsK8HSidHWY6g62a6IwiorQiDKvLmVlSOaME3A4luyDSCDIPvTYNyJP98nBuSFKf8At8nUYtT2_IDYmxzuCU6Fenh9xihWokH_m_YgUYb8g3tOF07i5-SkJ7LXnBVpEu9qZIPUFBfwcWv4asUrnnDpQm6F4Vu0jxv7otLGt9hjOiGicSpQkrCX_7Jt1IlRVFphSFX1pNK5rJKHFOeg5G_xzMVqJq00u9iB4WF23BDHmjf9ZzFxBxmoJoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه هم حمله به نفتکش‌ها را کلید زد
🔹
روسیه اعلام کرد که سه کشتی باری حامل تدارکات برای ارتش اوکراین و یک نفتکش را در بندر پیودنی در دریای سیاه هدف را قرار داده‌ است.
🔹
همچنین روسیه به یک کشتی باری دیگر در بندر مجاور اودسا، و همچنین زیرساخت‌های بندری در پیودنی و اودسا و تأسیسات ذخیره‌سازی سوخت در بندر چورنومورسک نیز حمله کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/684380" target="_blank">📅 01:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684379">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5458e415.mp4?token=qgv1JAS5bm7e-QDxvJSNzsyvgOBnot80A4q3rZxWySwwmwmDzcq4LCSktz16cNdZDt1X6vC3Fl68POSwq8jeRk_njVuPZWMW4viBTZWbO4HzKy5k6jQjf3t9YXLW5Ffr6b4HhUzlhXJWDyhzky5kJz8Hn4TwvGRkT8iRteOdsL2aHBGnk8dRoq8yjnw2U3CZbkFVn-15nhusWSGnwmMsspMS0I7bfebN1SRLrgKtnp8dJpsI72-FBeY0c7TNrWYyqO88rdxJnbyCBtOtWn-hcV66QEqcBHbaIdlDrGv8rnXRL782-GeTzhtYMJoBXX-xfLCC_2mU78Tr7b8KS1iS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5458e415.mp4?token=qgv1JAS5bm7e-QDxvJSNzsyvgOBnot80A4q3rZxWySwwmwmDzcq4LCSktz16cNdZDt1X6vC3Fl68POSwq8jeRk_njVuPZWMW4viBTZWbO4HzKy5k6jQjf3t9YXLW5Ffr6b4HhUzlhXJWDyhzky5kJz8Hn4TwvGRkT8iRteOdsL2aHBGnk8dRoq8yjnw2U3CZbkFVn-15nhusWSGnwmMsspMS0I7bfebN1SRLrgKtnp8dJpsI72-FBeY0c7TNrWYyqO88rdxJnbyCBtOtWn-hcV66QEqcBHbaIdlDrGv8rnXRL782-GeTzhtYMJoBXX-xfLCC_2mU78Tr7b8KS1iS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار درباره گوش‌پاک‌کن‌های پنبه‌ای؛ عادتی روزمره که ممکن است به گوش آسیب برساند
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/684379" target="_blank">📅 01:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEUA_T6NtXcBzWnMDhawqkHTACi19vmCTqk_JG3fUcGbtOGPgRTXFSDVKj5Y9T7DJhNWquPhF--Fe2lTCYpQOGx4Cajd2vrLy78IoDhwu1X9u595S4xUacOpYwsPBfSqBLMj1vjpB_sfH1llYI4KnvIHW2-Bg9vpr0MRT0BkK3ImbJJ9WRmri933CZKpI6FLrLqZlLFkK9GTT-H7m-m5bskY-wU4CJwNpITEJ7kW55oHxbzwX7Msqidt7vp_-TzFBUzCOL61S9XN1SX8E2Elkd1dvaY8XYilZAjfEGRT4yVPHnr3mc0fedGwTLfYlbrxb3XO9tQwJBddxGv8uWxaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تد لیو، نماینده مجلس نمایندگان آمریکا: قیمت بنزین بالا رفته، قیمت مواد غذایی بالا رفته، هزینه خدمات آب و برق بالا رفته؛ ترامپ روی چه چیزی تمرکز کرده؟ تغییر نام دریاچه انتاریو به دریاچه آمریکا
🔹
ماه نوامبر (انتخابات میان‌دوره‌ای) در راه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/684377" target="_blank">📅 01:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684374">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69982cd01.mp4?token=pjGBG5cEB_94v7S0bvERgTkSt_nQpH1KykSSe3opahPDih2qKfsQ4Mu7hSKIw7_tT93GnNIkt-2R3N1C4M1JYPnKqayjejZf2yYHFTZljzn_sVWwDVfYECRen__qIoP4BzLBk-1RogDLv5GxVz0ej_rfzcCLbRQmAQCdKFyPSprBCW66v7qaMudAsYAb_MVp0Zd6CfGM-iXSUEXfrLdeZJvHJd3lUv7pUNEBVmGsJXtIyLUR6pTu6eM2SxARlMVP1Dk2v_S66vJ-08JEjyoGOAs2AxM5F-J-4Y0uGzsgxKC20M2pFojQcWqVeOyt7WOPVzRqh0wtaQDy6zl2TJoU7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69982cd01.mp4?token=pjGBG5cEB_94v7S0bvERgTkSt_nQpH1KykSSe3opahPDih2qKfsQ4Mu7hSKIw7_tT93GnNIkt-2R3N1C4M1JYPnKqayjejZf2yYHFTZljzn_sVWwDVfYECRen__qIoP4BzLBk-1RogDLv5GxVz0ej_rfzcCLbRQmAQCdKFyPSprBCW66v7qaMudAsYAb_MVp0Zd6CfGM-iXSUEXfrLdeZJvHJd3lUv7pUNEBVmGsJXtIyLUR6pTu6eM2SxARlMVP1Dk2v_S66vJ-08JEjyoGOAs2AxM5F-J-4Y0uGzsgxKC20M2pFojQcWqVeOyt7WOPVzRqh0wtaQDy6zl2TJoU7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساختن این جک خلاقانه خیلی پرکاربرد و راحته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/684374" target="_blank">📅 00:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
قائم‌پناه: تفاهم‌نامه اسلام‌آباد پابرجاست؛ توافق آرا بین اعضای شعام به قوت قبل باقیست‌
معاون اجرایی رئیس‌جمهور درباره حل شدن مسئله جنگ، تفاهم‌نامه اسلام آباد و اتفاق رای بین اعضای شعام:
🔹
در تلاش هستیم از طریق دیپلماسی و از طرق مختلف بتوانیم آمریکا را وادار کنیم که به تفاهمنامه برگردد و عهدی که بسته را اجرا کند.
🔹
امیدواریم بتوانیم آرامش را به عرصه اقتصادی کشور برگردانیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/684373" target="_blank">📅 00:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBQGr4lAqEtaBcdobXwKdsrNVjpIGBccq-ZFi64FGqr1fpNCkAqztibFH8tdfmuHtOym1ep4PW8d6439AGspva01wk7dhNozz93SaeQDiEfLXig2sv0KD3MSFWNjRp_ZjkBCydA9O-0efi8k6HfMD9Hj30TzX6QQAETu_iQ0Yc2MzIZDQTRCsei8HqMt_rHvjxr2GoRKptWDHcwuAwe6hLofg3P8zL_K-8A536Cu_j4ZjhvYSTnBlQR3G3VPTA5uG25lQ19zT36M_Vib-GTHqPhoOMlt9TF7iU0hf5BMa2s9KFQqyPW6XGpGEixhPPQGCiRX0z9jKJ6fF_iXzVEUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نویسنده سابق گاردین: مصاحبه درباره حکم سنگسار سکینه آشتیانی ساختگی بود
🔹
سعید کمالی دهقان، نویسنده گزارش جنجالی گاردین در سال ۲۰۱۰ درباره سکینه محمدی آشتیانی و ادعای حکم سنگسار او، اعتراف کرد مصاحبه با آشتیانی هرگز انجام نشده و متن آن را خودش ساخته است.…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/684372" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a1909c4.mp4?token=Gu3E_qs-5-FmnSIC74c9d1FpY8ZCq--5XfQsjjES2c_zEUo3zIcoFK6eDqAKs5lfxREoe5B-_xBbgMmmjAM0j125VfdTuoVw9mlS6vPssBpJw8zHL-z-wmp5X-xfOcgaou3nUuPaSq994kBbTtMaVbTK3MS-4vXAze_g38Efz7L9UPC131OEMgQHJrAeByyDo0tiH_lBrZYzhji5fPvFLYPFEHy5w_bo9ts5kU56IchzLg5GaYDMzqUUz3BQhhIpYDXs0c1QuyAlIXuc-Hbu43v7NBK6huD2MR4IzFx5YKtFcapmK-gNP9r-kwwym26ds3lbH5prVac9YjDBDz0Esg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a1909c4.mp4?token=Gu3E_qs-5-FmnSIC74c9d1FpY8ZCq--5XfQsjjES2c_zEUo3zIcoFK6eDqAKs5lfxREoe5B-_xBbgMmmjAM0j125VfdTuoVw9mlS6vPssBpJw8zHL-z-wmp5X-xfOcgaou3nUuPaSq994kBbTtMaVbTK3MS-4vXAze_g38Efz7L9UPC131OEMgQHJrAeByyDo0tiH_lBrZYzhji5fPvFLYPFEHy5w_bo9ts5kU56IchzLg5GaYDMzqUUz3BQhhIpYDXs0c1QuyAlIXuc-Hbu43v7NBK6huD2MR4IzFx5YKtFcapmK-gNP9r-kwwym26ds3lbH5prVac9YjDBDz0Esg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد جالب درون کپسول آتش نشانی وقتی آن را فشار می دهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/684371" target="_blank">📅 00:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684367">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73796fbb7f.mp4?token=O6aXa_oHFDyq90J61aeelZaYsQrKHF4kIAvJWiFD3dUuXHKYrFf2tNyDdA5Fx74J5Nz7P8Pk42assWfzivM4d6W5qRi-lDUdGHT8nqzATbSL-MSGPnRphsCS7ntXwH7omVmHZDf8AtcpzncHhfBpywmLyW-TqeojOnICPk6hsI58EUYyK-yOyIOqNn49wes4qIT-5ZgF7zUOzVw13guhJmSCFgbhGJwgj_v9kfSypAlphCgzC26CWZXZhJrV4D3Ynycs0dvMVURu8VXNds40Zovk3yBhJYZIuRoPCtyPCn7CQM61gE5DlI7HIE6YdD2MyqMRphhB2UGUv3GY4vD5hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73796fbb7f.mp4?token=O6aXa_oHFDyq90J61aeelZaYsQrKHF4kIAvJWiFD3dUuXHKYrFf2tNyDdA5Fx74J5Nz7P8Pk42assWfzivM4d6W5qRi-lDUdGHT8nqzATbSL-MSGPnRphsCS7ntXwH7omVmHZDf8AtcpzncHhfBpywmLyW-TqeojOnICPk6hsI58EUYyK-yOyIOqNn49wes4qIT-5ZgF7zUOzVw13guhJmSCFgbhGJwgj_v9kfSypAlphCgzC26CWZXZhJrV4D3Ynycs0dvMVURu8VXNds40Zovk3yBhJYZIuRoPCtyPCn7CQM61gE5DlI7HIE6YdD2MyqMRphhB2UGUv3GY4vD5hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه عجیب عملکرد مکانیزم دسته صندلی اتوبوس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684367" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684366">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUSZ06hoBpQBJ89ce9g0AtmzfR-Mo-v7TK-R3mkCJRzPo6ChrswlbMdwIDnZZlnscwao9XsKIpfZNPlCtkgL7Ogr_aaidv3Yjxbe0SDMgySy0796FXgkMJA-kSwNsoC-KHF4GpHayewaTKjnqFj_XOsVaT_mcng3qafJ9YhL2iyBZjtd2zeoSs5jKdin2iwYmgKqpJogcfYacg23T_mmGSdELt5GaGtMCLNrpC_Xcmn4Xn_2H07ieuAWty9DsxMRzD-2MM-q_sP0RJaxZgq8h3rIfcp3fIzv-UV7JhECzAopLzSV91oC5yPaRbnFK1R_EE7fiK-1nsofqCNh0zTcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بیش از ۱۱۰۰ اارز دیجیتال
📈
۴۰۰ ارز اهرم‌دار تا اهرم ۱۵۰
🎁
هر هفته تا ۳۰۰ تتر جایزه برای انجام معاملهٔ اهرم‌دار
فقط در صرافی رمزارز کبرین
👇🏻
👇🏻
👇🏻
ورود و ثبت‌نام</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/684366" target="_blank">📅 00:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684365">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI-raUfzqG8xjSkuQD80ZVLGtE0MQDUMn8xa4ppSYS4Sfpw4Hl0_IV-_LYLd14hZad4HdglpG3ZYbl52JR3OUU3nYWu91bnkrtC2ipMMaQE1C33FLdsUNMFSCfZVhzysOwgA28mVEvcCXpuJPY8CDhUsI_BPW2hsL7rc-huwNHT7fULQ7NBgmBJows-_9G-4ak5f8lv98_d7OGqpbQWtDbUsJX4iF7dUOPho4oBZ6XfQWpaFm4Vys9AmXT0pDSkcvfM--pX26raRXKJyM2QP1G16pJ-lXe_wmmskN-kF79cylUPID44QjYbWtYOSIvFyPDHJJsJVzozuWfEhm_x9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/684365" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684363">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTu45Q5mvH74qHoFue2dn2purOJtIarvXhZf41o4Ov6wvf-I0w8kEBDDprZDziDaAEFAasXz3UcijIZ9IibHQc4BBgkVd2Pk1hbt_67fnDo3oA2ou-xaPFbtGL_3QUt9EQcbFXMa1emxEvloCb-FWduCWK4sZo_kV3cRiTMMcHo-1tEvg2iL83-V8Rz6C2AkXTLjha3pU6bHn6bsK6cBM1QN5_DyEIZ_PylxiAv2_cHXO6q4NmVOGRsBEyhJeMV7gmjAUX7BbSwaIWWJMxi9Z8cCVRXNHhpQnG97A3GX6W2_JQTP79vSjeCIb_EkrxVVg0lCuHKTpX4RdWjNJXC-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس یادگاریِ زنده‌‏‌یاد اکبر عبدی، زنده‌یاد خسرو شکیبایی، مجید مظفری و علیرضا مجلل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/684363" target="_blank">📅 23:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684361">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e1877ded.mp4?token=k3WbXvmMQ_2-pPE8PNGG4hPjjS8Jet4XVvi6OVApQcMvFRaVGZnb1UovCrxYQhz69xkOKP6EkDDS-VeZhmsKit1pCCUD2sktZYi1IDmwYY60Rcy2iAojkvLjkFpriQWXI2QlfX7lyqAhQQzAsELe9WtpX88xSa1ooh_FiQIe9dFy6V8ZC3bg3b6b0YvFitKrZZUvg9ylwCbW1HOaEwYcYkI2AI2Z2uE53HJvU862dlo_gF2jtyRgKb8UiHEWHgw2eIKQGOa0Auh2_irNoN9W7PMRMuXGKM6-AgwdpuXlcMfD7QHnvJ19bxeBdbDcniVnZx42oOtrkbgKKQVJnEdqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e1877ded.mp4?token=k3WbXvmMQ_2-pPE8PNGG4hPjjS8Jet4XVvi6OVApQcMvFRaVGZnb1UovCrxYQhz69xkOKP6EkDDS-VeZhmsKit1pCCUD2sktZYi1IDmwYY60Rcy2iAojkvLjkFpriQWXI2QlfX7lyqAhQQzAsELe9WtpX88xSa1ooh_FiQIe9dFy6V8ZC3bg3b6b0YvFitKrZZUvg9ylwCbW1HOaEwYcYkI2AI2Z2uE53HJvU862dlo_gF2jtyRgKb8UiHEWHgw2eIKQGOa0Auh2_irNoN9W7PMRMuXGKM6-AgwdpuXlcMfD7QHnvJ19bxeBdbDcniVnZx42oOtrkbgKKQVJnEdqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: شناورهای مین‌روب آمریکا اگر وارد منطقه شوند اهداف بسیار خوبی برای ما هستند
🔹
دلیل عدم انتشار متن توافقات امروز ایران و عمان و انتشار یک بیانیه مطبوعاتی این است که ما هنوز تعهدی نداریم و این موضوع زود است
🔹
به عاصم منیر گفتیم به آمریکا بی‌اعتمادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/684361" target="_blank">📅 23:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684359">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b79635eec.mp4?token=d80FE-ftQRMKV2G_ldD-LECNadRMPyP4f9ZHsmBxJHE-L6WWPYaJB4AuJJYI2kYDAtT3dRmu9mOIEaRy5RjGlXBIb_WBvsKZLkgJjZRw575zTBEnJdXU9dgEeUUfdM-do6206vbDy72Lrh1XzIjp0-VParPrKnIYohnStfJDuqme3p-YIKeKPYl6hzSMmazZU-d6WLs0JwKCqxmbp03_7XtksglV1jpR-xaIUhOjhZ-cq-IcA4vqpHEyQJSYQjeSd0khbEYonvphA4PV3ihLQ97ilKiM_wLnhEoUJ6-eoDrVzbf6hZ3B-Q4XpLQB_6ZVRhUB5Kg8KWCB2jsRqpN9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b79635eec.mp4?token=d80FE-ftQRMKV2G_ldD-LECNadRMPyP4f9ZHsmBxJHE-L6WWPYaJB4AuJJYI2kYDAtT3dRmu9mOIEaRy5RjGlXBIb_WBvsKZLkgJjZRw575zTBEnJdXU9dgEeUUfdM-do6206vbDy72Lrh1XzIjp0-VParPrKnIYohnStfJDuqme3p-YIKeKPYl6hzSMmazZU-d6WLs0JwKCqxmbp03_7XtksglV1jpR-xaIUhOjhZ-cq-IcA4vqpHEyQJSYQjeSd0khbEYonvphA4PV3ihLQ97ilKiM_wLnhEoUJ6-eoDrVzbf6hZ3B-Q4XpLQB_6ZVRhUB5Kg8KWCB2jsRqpN9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: پاسخ جدید ما به تحریم‌های دشمن هدف‌ گرفتن منافع اقتصادی آن‌هاست
🔹
نباید مثل سابق با تحریم‌های دشمن برخورد کنیم.
🔹
بر خلاف ادعای مقامات آمریکایی تنگه هرمز بدون ترتیبات ایرانی باز نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/684359" target="_blank">📅 23:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684357">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVua2Os863m8DAiO3uNXmz0IHz5yzdl_yWDVJ7wxKFTln2qe4ZylhY1kaSeWdgJYUQWK9sOrj7aikJkKa_fLo5fVbtmp9txppcYQbOiRhCUXIp0hX7fybNld0-o_4e4fzY_N4m6mwLwIPDXrkGQXEVKfoxnl_ViZ7SxEBlUVuYWFHz8St5WdCuvvS1-AZFD82t-aTeWtr-zJDGGbOY5qtlZ16EI9fqIpHkEZrCTn1ygV-hqaFHrFq-6-9SmPIK-eh6azGvmgwage4n5pxSE1RU3TtWVGAVqi-ikZukh96Ynle49WLTpxV9P6BqAxFWJO4WBAM1kArDDJM-cYWYqGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وکیل و فعال رسانه‌ای سیاسی آمریکایی: وزیر خزانه‌داری آمریکا گفته است که وقت آن رسیده جهان بین آمریکا و ایران یکی را انتخاب کند
🔹
این اعترافی قابل‌ توجه به آسیبی است که ترامپ به جایگاه آمریکا در جهان وارد کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/684357" target="_blank">📅 23:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684355">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
غریب‌آبادی: چرا باید همیشه ما منتظر بمانیم آمریکا حمله کند؟ ما می‌توانیم دست به اقدام پیش‌دستانه بزنیم
🔹
مذاکرات ایران و عمان برای اداره آینده تنگه هرمز ادامه خواهد یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/684355" target="_blank">📅 23:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684354">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHP4KgZrD22KsemwvqbAcbU7hRA1NTmwGpTfdYbG2ZwUpKgA_dEJ2XLuVO9L0Z4narfrYcxWTULRNCwumhPamwYralLz97zXO4ImQe7F7drAfVbNzNQklUuLdJgcHRZCjJVDSmFO2SH-_5cnB1YSOkJktvvPADR3Vt7sNOGuQB_Jnc6G3k39_AfoSPe3QdMMfQgdZ95UoCmdFj3NUEhZkw_96bkHOaZ9D6gvOEtw5Fuf_Jy_SZL0tLm4N4sa7EiPSa_nY18Dh7SK6mLC4EPR5HkzhKxwMCo3ose0zP0crm-mXs1aCBDG-pA4eNraOfS782ZRMlNsFvTDrspuq0zQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارآفرین و فعال سلامت آمریکایی: لطفاً به مدت ۹۰ روز آینده هیچ گوشت چرخ‌کرده‌ای نخرید
🔹
در آمریکا ادعاهایی مبنی بر واردات گوشت فاسد از آرژانتین توسط ترامپ مطرح شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/684354" target="_blank">📅 23:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684351">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRswyb76WdXokDlDO8lYgsMJvC4oB2K-9a3WDTiVQGk3jCR7uGqFGPq77ZOOqNwTtf7NUM1Z50puIuh97OJppqujKxEy4zVR-1VksFVvIReuXjYaNI9Aatt2DbirFBOlqNhXsjQMDkROyxHlrm7Jn1iEGfnV3Smw_uN0Lq3cVAEkd3IFBpbjWicZyFxlsa4sEe6pnL7rIJhQpOhbXg0dgUGd5CRaSkDHfaGNuIEHmDEluJUmGpQMNeV2GZ6I8sP5FeKTdtAq3CT_13Mq61rfaiOQR2svjldLzvniO_SzRnskoV76hgMPbhbRzTGd86zPochi9Ar2ZeucHOIASsr1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صمت: فولاد خوزستان یکی از قطب های اقتصادی کشور است/ سرعت بازسازی در این شرکت قابل تحسین بود
🔹
سیدمحمد اتابک روز دوشنبه در حاشیه بازدید از خطوط تولید و روند بازسازی خط تولید فولاد خوزستان پس از حمله دشمن آمریکایی-صهیونی، با گرامیداشت یاد و خاطره شهدای دولت اظهار کرد: فولاد خوزستان از قطب‌های مهم اقتصادی کشور به شمار می‌رود و فعالیت این مجموعه تأثیر مستقیمی بر اقتصاد ملی دارد.
🔹
وی با اشاره به بازگشت سریع کوره‌های آسیب‌دیده فولاد خوزستان به چرخه تولید، از تلاش کارکنان این مجموعه تقدیر کرد و افزود: راه‌اندازی کوره‌هایی که در جریان حملات آسیب دیده بودند، اقدامی درخور توجه و قابل تحسین است و نشان می‌دهد نیروی انسانی صنعت فولاد در شرایط سخت نیز برای حفظ تولید پای کار است.
👇
👇
akharinkhabar.ir/local/10984144/</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/684351" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684350">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb1146038.mp4?token=m1WI6xcGkqn8LE52X4MQAKVjSnPNDnbvX5tmAZyMzATqNGUFzeXNeBLjml3Tvj9TONbPHCSFQP4HYrZTIypbvHzHtwFrUg9jROzUU8m42H98CcQxD9F108Z6pLcsDphDLVvoYLJZ4-FL4XgvfTNEb1RWPwZ0f0ISA2tagfH37x1sIbVW7qlfg50AIEnfGPrrCex1CEBBatqIAhT82xXUHRvE22z8AxqWhtzLchrsVZoQpMrDvxfhszmztR9180hSsEEzfi66niaTns0c-AsON_EGrYwv9rPLRHgaao2NspEKozmYPb2e6h5FlQ4tUx2RyxSwXKIS1c0vzFNk8EyJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb1146038.mp4?token=m1WI6xcGkqn8LE52X4MQAKVjSnPNDnbvX5tmAZyMzATqNGUFzeXNeBLjml3Tvj9TONbPHCSFQP4HYrZTIypbvHzHtwFrUg9jROzUU8m42H98CcQxD9F108Z6pLcsDphDLVvoYLJZ4-FL4XgvfTNEb1RWPwZ0f0ISA2tagfH37x1sIbVW7qlfg50AIEnfGPrrCex1CEBBatqIAhT82xXUHRvE22z8AxqWhtzLchrsVZoQpMrDvxfhszmztR9180hSsEEzfi66niaTns0c-AsON_EGrYwv9rPLRHgaao2NspEKozmYPb2e6h5FlQ4tUx2RyxSwXKIS1c0vzFNk8EyJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‌غریب‌‌آبادی: بازگشایی تنگه هرمز تنها در ازای پایان جنگ در همۀ جبهه‌ها، رفع محاصره و تعیین‌تکلیف وضعیت یمن رخ می‌دهد
🔹
هیچ کس جز ایران از مکان مین‌ها در تنگه هرمز اطلاع ندارد و موضوع مین‌زدایی که مطرح می‌شود، ادعایی بیش نیست و اگر این ادعا صحت دارد چرا شناوری از تنگه هرمز عبور نمی‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/684350" target="_blank">📅 23:32 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
