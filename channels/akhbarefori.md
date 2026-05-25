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
<img src="https://cdn4.telesco.pe/file/PJw9hkxK_oTU-YohH67SUMYd7y6VaqZqaijXf5hO1KbKVPMnOeUbPPaFcvz0lKF8Vq9SAIQxJd3a8VjAyBi95faCcwVmTvVhe-oa43jjGAutPA8nSmsmUZTVoXbDXJ_Hd93aRJsMDBNxO1be_FMGVmurilMr4JYkHPCcijkNDEiZ4IvBVVJry949_Og_ay7ep-rutdtGhB56aurCqFYahifU3bWeb7T8Lhuj3SYLR09iIFDDCWTiTCDiMqI_CwKpQhRkDnz7QsdtZz18SXmVp0TZpo9RM0zuU7IdbncxCrIT94f5gvCG95gyYaxYYblEeALDoQ8H-eewyAoJQ3N5ow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.87M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 15:03:20</div>
<hr>

<div class="tg-post" id="msg-653998">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/218662fffa.mp4?token=Lf0ljrH9elFm0EjY22RmKaVxvQPu7e6CXp88-gvCRcgcTJZa4zrlpRFAQXtf1pDN1Eue-I0L4tDvu_8hJyi5FliW3OfZNPXO9QQ49JHwfzlTDOC6twZrD4MtYlIqqkHTvzAlPlNMPfBprB63soDYPNzPLYVGJCr0dk0t044Vp41DPEDBdR1-j8v2D--0noEcZrLnFmACHcFShyUFkYPgC9Ip5zEaCrOxlpb--fw98e8hRJn7YL_xBB883QMCI36gF7VYIZxrOsMTF82rgI9K29elwbrXHg5SseAUbfovBY7vKp96jiiA9Qxra4IqQAWAnLr6CxRQdSdsNo7CzpIYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/218662fffa.mp4?token=Lf0ljrH9elFm0EjY22RmKaVxvQPu7e6CXp88-gvCRcgcTJZa4zrlpRFAQXtf1pDN1Eue-I0L4tDvu_8hJyi5FliW3OfZNPXO9QQ49JHwfzlTDOC6twZrD4MtYlIqqkHTvzAlPlNMPfBprB63soDYPNzPLYVGJCr0dk0t044Vp41DPEDBdR1-j8v2D--0noEcZrLnFmACHcFShyUFkYPgC9Ip5zEaCrOxlpb--fw98e8hRJn7YL_xBB883QMCI36gF7VYIZxrOsMTF82rgI9K29elwbrXHg5SseAUbfovBY7vKp96jiiA9Qxra4IqQAWAnLr6CxRQdSdsNo7CzpIYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرندی: قرار شد قطری‌ها پول‌های بلوکه‌شدۀ ایران را پرداخت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/akhbarefori/653998" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653997">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjArKdMXVEiGXlXFWL5UmE1nSGLK7i0yqoO3i7NNRqmfuN_-Ozff31qkYoUyn_DghQszWN27pwvRPMfJXFMT6jdDUWwZwUdrPNlTyxrhMCTJbd5NwmEG7nokWEy6Us17g2tdqIGt30D0u7e8sWAs3HItM0quWh4zLIVL8KS9qEzMtnEKyyozPrexbvdTD6gOC0nUOBFZwzSkghDGwWGfp-Q9bn-71vk-sr0aCGgbp5YSk5vNnENaj08_Ut164sezlJ7GiMounRITMFudvUKwikNOJrLN_95dGbD7GPlk668fDrNBDVCW7fsLQGQolNy4XMnEPerZT56wu0aabObcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تداوم ششمین سال خشکسالی پیاپی در ایران؛ بارش‌ها در ۱۲ استان نرمال نیست
🔹
معاون شرکت مدیریت منابع آب ایران: اگر چه در سال جاری متوسط بارندگی به ۲۲۹ میلی‌متر رسید‌ و ۶۳ درصد نسبت به سال گذشته افزایش داشت‌، اما نباید دچار خطای شناختی شویم.
🔹
همچنان در ششمین سال خشکسالی پیاپی قرار داریم و ۱۲ استان کشور که ۴۰ میلیون نفر از جمعیت ایران را در خود جای داده‌اند، همچنان در وضعیت بارش زیر نرمال هستند.
🔹
نامتوازن بودن بارش‌ها و زمان نامناسب ریزش‌های جوی مدیریت منابع آب را با چالش جدی مواجه کرده است. ‌
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/akhbarefori/653997" target="_blank">📅 14:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653996">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969b451344.mov?token=Mkzt717L1APeJUJ15CQNO4T_kgi7B4Wb_uAsCzmkQzU0Bg1gb_1snUmtfUA9D1PuopXlOfEUH3Q52XbCdKutKF53B6cWiZAZwhp99jgrNa_t0uQFC2y5OQ9lXOz7JZH9oK5ksRFPp7P--qU4oAjGGn7Fl4iMv1aa-YI-_s21mWhJjLqlcYOIefYVU2S_mmcYxiXjqKPU52IotME1fjJh3hy2f1nri9FWYq-OdoOXxGMHI05P5JSKoPyQTzJH4hxC9bIz6RpPCxgJZxKIiSl6cOfMP7-Kn_j6hj-gBuBKWseELYgtflWklRjvDuLOj7YUlVMOfyBTS8RaKtUq4i4f1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969b451344.mov?token=Mkzt717L1APeJUJ15CQNO4T_kgi7B4Wb_uAsCzmkQzU0Bg1gb_1snUmtfUA9D1PuopXlOfEUH3Q52XbCdKutKF53B6cWiZAZwhp99jgrNa_t0uQFC2y5OQ9lXOz7JZH9oK5ksRFPp7P--qU4oAjGGn7Fl4iMv1aa-YI-_s21mWhJjLqlcYOIefYVU2S_mmcYxiXjqKPU52IotME1fjJh3hy2f1nri9FWYq-OdoOXxGMHI05P5JSKoPyQTzJH4hxC9bIz6RpPCxgJZxKIiSl6cOfMP7-Kn_j6hj-gBuBKWseELYgtflWklRjvDuLOj7YUlVMOfyBTS8RaKtUq4i4f1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز متناسب‌سازی حقوق بازنشستگان روستایی از تابستان امسال
🔹
مدیرعامل صندوق بیمه اجتماعی کشاورزان، روستاییان و عشایر: در صورت تأمین اعتبار از سوی سازمان برنامه و بودجه، مجموع مستمری مستمری‌بگیران این صندوق در سال ۱۴۰۵ حدود ۵۵ درصد افزایش می‌یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/akhbarefori/653996" target="_blank">📅 14:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653995">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ-y7CD3JIriiQtDidW05YYor7w3vqCc3odC2Mg54o6BOBt0je2t_Fox2j3lP7-MGVEsS99Tgn7rfjV1Pegj0vD_t5PcpVmZ0Gqn-TgMHrodvhDd9aSULR55nFulHZB8yYetNUHKeUrKlL9kLO1uuAH4uCTDqjy5oZnKDBso6EBf-ZdoPuwgxUGUY26VSSrp0ZVwCVDzBjDrbunsFmUBOCyn0wg35l8AoL11D-7mp62L7-ZhIAGnva9z_Zpq7C4Q6hJW8J3OuTlY46-uR0WDr1FabwyknuQwYZSR5yw1t54uLGlkew-MGzq-xClkoS7Hc4gl1ZRwrJkZ_BgcN50OCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بن‌‌گویر: اسرائیل باید به جنگ تمام‌عیار در لبنان بازگردد
🔹
وزیر امنیت داخلی اسرائیل «ایتامار بن گویر» با حمله تند به نخست‌وزیر اسرائیل «بنیامین نتانیاهو» خواستار بازگشت اسرائیل به جنگ تمام‌عیار در لبنان شد.
🔹
بن گویر گفت: ما نباید واقعیت پهپادهای انتحاری را عادی‌سازی کنیم.
🔹
زمان آن فرا رسیده است که نخست‌وزیر بر میز رئیس‌جمهور آمریکا بکوبد و به او اطلاع دهد که ما در حال بازگشت به جنگ در لبنان هستیم.
🔹
ما باید برق را در لبنان قطع کنیم، زهرانی را تصرف کنیم و به جنگ با شدت بالا بازگردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/akhbarefori/653995" target="_blank">📅 14:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5b3e85d2.mp4?token=OpRwFIY59FT8AZkL-dsyaR6XUuMr5MI031DGn8ZzvChUpG3dVseKkQ5UvCX8Ei-m6uVsL0MlCgwBbyrYEwgKIHeKjiikmFAPr5L3E52S4Ovgb9cXV3IYGPPFRKT5KE78o9b5hnRMpjCjCjw-qBiPCqRwlgpOYT6bsT8H1xIUwjc2Zo48rnU1fs00FvW5STr9dxRyabQnczOVyRWE8XJMvtNsVFQMDSOi4oCy5AaCaVS--pO1H522XK4ju00R6cFyTqLEWqwlCs3dQj9UBzMUpIvXfvHa19HEJuB_skwgGBApp1KDSGgijRCMAKodJCTtMfa1OxC4BUJ6hdwT60krSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5b3e85d2.mp4?token=OpRwFIY59FT8AZkL-dsyaR6XUuMr5MI031DGn8ZzvChUpG3dVseKkQ5UvCX8Ei-m6uVsL0MlCgwBbyrYEwgKIHeKjiikmFAPr5L3E52S4Ovgb9cXV3IYGPPFRKT5KE78o9b5hnRMpjCjCjw-qBiPCqRwlgpOYT6bsT8H1xIUwjc2Zo48rnU1fs00FvW5STr9dxRyabQnczOVyRWE8XJMvtNsVFQMDSOi4oCy5AaCaVS--pO1H522XK4ju00R6cFyTqLEWqwlCs3dQj9UBzMUpIvXfvHa19HEJuB_skwgGBApp1KDSGgijRCMAKodJCTtMfa1OxC4BUJ6hdwT60krSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع بی‌سابقه در قلب اروپا: ۳ هزار حامی محور مقاومت سیاست‌های آمریکا و اسرائیل را محکوم کردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/akhbarefori/653994" target="_blank">📅 14:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653993">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY_3v9xBiT4GaWQSO_FW1BS1wAyQVSbMieJqsIHlIvDFdsf7W_Sr9m45MGqylDP922-bN_MXJWLjWSOpxa6T5D6bcNOjHzEOMVlH0V909P5KtcMP6OR_zBOOF4W06WeEwVOApQKef-l_nBGR5aZwOaf0yj05PuC5C6lrMY2R7IvrVwM8gOoMYA4nsHNiaFv6UEORFQN2QXgHJkTnBj4Hy2RarXwEgvOvPzLqXzeOvAWrmeO19n_n561-ARBVcm3vbsZENPF0liJsIcF9X_sfyoAPR_GGQkI_oMthv38gJGbUnj47OXBLJAtGh31QqAxAQp1JodZPVtQh9-pxv-0tHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکید سران چین و پاکستان بر لزوم برقراری صلح در غرب آسیا
🔹
رئیس جمهور چین و نخست‌وزیر پاکستان در جریان دیدار در پکن، بر لزوم تلاش میانجی‌ها برای پایان درگیری ایران و آمریکا تاکید کردند.
🔹
«شی جینپینگ» در دیدار با «شهباز شریف» گفت: «ما برای نقش پاکستان در میانجی‌گری صلح در خاورمیانه ارزش قائل هستیم».
🔹
شبکه «المیادین» گزارش داد: «هر دو طرف باید ارتباط و هماهنگی نزدیک خود را حفظ کنند و با یکجانبه‌گرایی مخالفت نمایند».
🔹
نخست وزیر پاکستان نیز در این دیدار، از حمایت‌های چین از تلاش‌های میانجی‌گرانه اسلام‌آباد در مذاکرات آمریکا و ایران ابراز قدردانی کرد.
🔹
شریف در این‌باره اظهار داشت: «پیشنهاد چهار ماده‌ای رئیس جمهور چین درمورد خاورمیانه، چارچوب راهنما برای دستیابی به صلح محسوب می‌شود».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/653993" target="_blank">📅 14:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653992">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McIS7Q5LCNQjEyFIcsNzhctM5bfOpnBqR2NGycy1lPcwZY4-r9_eqEPy5X0QvYsnHdPcIfSGJRUVFrKmdM5mzuc51EsHQCbI7a8Z67c2z9IY7pdT2LYsglQgUY4FImllAyi1zRAWpvJE5dDRR5cxX_aajfwCbRthvl2Es2RvJTeCdli_swCAf4BCEvT8xv0e0pTS-yGkZOOB_iG5nhnS8-Pej-VP3k-ovte67-eDJwbEpzznPM_h5YZBXF2WVjVTEGcqbLgqP1UhIJkmrvo_ypBOfIUVQpipT8nbs2C4FERzxp8Eix6n1cR4a5l85Md1vxw_bBOZa23jv54nswDDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع پاکستانی: توافق موقت آمریکا و ایران، قریب‌الوقوع است
🔹
منابع پاکستانی گفتند که آمریکا و ایران می‌توانند طی همین هفته، «یک پیمان موقت برای پایان دادن به جنگ امضا کنند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/akhbarefori/653992" target="_blank">📅 13:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653991">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2dQVHy3ENAlR-KFpi7zyIVqOPU0omMrSoGSRPB14pfCxP9WiZwBKgwXQ-4X64DZzKhHKkGNa_XtHy0_ube8JhAAqMQ6lRDWTtfOhEtIwzMCln0ImNOyKSuCDF_wsuwl7kppF7CN6tra-fps2HR92eRgs5HwLCmsGPfaP-52ttE88d_uZd8VDlfEb2n_WRQQnKo6caF70IG_P3yQaf527pShoyWQ9e_I2SQSoPzAech5NUkExY25WLwKfeawIWbNNpqyysZRACvBhSfJ_d1ZXHckTpamhlr5Pu7pnRi09DM8GRNG3p32Fhyzc2LUYAq6gDRIi3Hnuz-65JgqSx7hHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتکش عراقی با شکستن محاصره دریایی آمریکا عازم چین شد
🔹
یک نفتکش غول پیکر عراقی ضمن عبور هماهنگ شده از تنگه هرمز و شکستن محاصره دریایی آمریکا عازم چین شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/akhbarefori/653991" target="_blank">📅 13:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653990">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bubiBdjoYbQAwePIqV6JmxWvOxJzI0VAC12DvN9JhENo6ZFwcVsz5pKX3WE79Z4ZO9mqWd1fOKg3QTvwFj3_fpY2yvw5rdDIRIBx61QKlY6HosEY3ghC4s8dONpPD-4Wr3OYRhk-aDfvi5sSrpwd3Y8Shw16J8kJNWstQZGWCTc9STn8YZH6qie10com7PzJuvvOWhEUTg0Wdc7jiaWNkj0LpDr1pp9tGxO_7OzNBn8iPjVV11QWTj-OIuWG91whrus06GrVRgqZUecXVTBb-4TQf1BupHl4a8X0xcs561j6C5z8Blpfed1NkTwZ_jpkZ3NKAHcd_MJzMyazAmLARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهدید مقامات اسرائیلی به جنایت جنگی در برابر پهپادهای حزب‌الله
🔹
در حالی که ارتش اسرائیل برای مقابله با ریزپرنده‌های انتحاری حزب‌الله ناتوان مانده، مقامات این رژیم گزینه جنایت جنگی را پیش کشیده‌اند.
🔹
بزالل اسموتریچ، وزیر دارایی رژیم صهیونیستی امروز در نشست کابینه که با موضع بررسی معضل پهپادهای انتخاری حزب‌الله تشکیل شده بود، پیشنهاد داد که «به ازای هر پهپاد انفجاری، ده ساختمان در بیروت باید ویران شود».
🔹
او همچنین گفته است که «این هفته بودجه‌ای حدود دو میلیارد شِکِل (حدود ۷۰۰ میلیون دلار) برای راه‌حل‌های تکنولوژیکی برای تهدید پهپادها تصویب کرده‌ام. از جمله موارد دیگر، این پول به نهادهای غیرنظامی اجازه می‌دهد تا راه‌حل‌ها و ایده‌های نوآورانه‌ای ارائه دهند.»
🔹
ایال زمیر رئیس ستاد ارتش اشغالگر نیز در این نشست پیشنهاد داده است که در پاسخ به حملات ریزپرنده‌های حزب‌الله، بیروت بمباران شود.
🔹
اما ایتامار بن گویر، وزیر معلوم‌الحال امنیت داخلی اسرائیل نیز در این نشست، پیشنهاد بمباران زیرساخت‌های برق لبنان را مطرح کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/akhbarefori/653990" target="_blank">📅 13:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653988">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رادیو ارتش اسرائیل: از زمان آخرین «آتش‌بس» در لبنان، ۱۱ افسر و نظامی «اسرائیلی» کشته شده‌اند که ۷ نفر از آنها بر اثر اصابت پهپادهای انفجاری بوده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/akhbarefori/653988" target="_blank">📅 13:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653986">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c8fb333c.mp4?token=DihA0wlslizxapGpSJ_GuCOSJQNStXFCqtJAyFMhrNPL2PItqigN_mtS2IW56w8apGMsg8vllehH90q8OBTpSUoC09knviRg0LvlRaNG0daYLAYoPS427krI6SDn1K8IqjCU0UU1xiZV7ryAyUUejzjAsY13c5D-ALzDGoxkC3oyaeQUFWaKr_pAvH66jmAloJ0yEROcdxhprVCyTgaON0cQmn86R_9v-vTMheEbVtzQcjos0EXCSfJEDJuqeKLkpAniyl2WPPaOtzElYc-64i-8BiADOMNn6dcas5rT4Qv1lPzTJLmbY5M7uWYJLx96oeDioq2M-sEumbrYy2geMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c8fb333c.mp4?token=DihA0wlslizxapGpSJ_GuCOSJQNStXFCqtJAyFMhrNPL2PItqigN_mtS2IW56w8apGMsg8vllehH90q8OBTpSUoC09knviRg0LvlRaNG0daYLAYoPS427krI6SDn1K8IqjCU0UU1xiZV7ryAyUUejzjAsY13c5D-ALzDGoxkC3oyaeQUFWaKr_pAvH66jmAloJ0yEROcdxhprVCyTgaON0cQmn86R_9v-vTMheEbVtzQcjos0EXCSfJEDJuqeKLkpAniyl2WPPaOtzElYc-64i-8BiADOMNn6dcas5rT4Qv1lPzTJLmbY5M7uWYJLx96oeDioq2M-sEumbrYy2geMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون امور زنان رئیس‌جمهور: اگر خانم سرپرست خانواده هستید و ضامنِ وام ندارید، دولت شما را ضمانت می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/653986" target="_blank">📅 13:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653985">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVX3KvYGwy9436ltCsgRWFzVD3hkQU2GO11iGhciSDriuf2TOAUs-36uA3QJiT_mj9K1zEFbwlod3MrOlncSjf6yOhIWDifpI2f-EzUvMJ76sBJbOWTJcWvs7UHE0-CawiTElCLnI-Vuxcnckgs85o1Y_0yOMFUuUnTtlX4XTd-J2A6YfrMsBx8nqVxnuDQbdy2EH3RgjzIUfwoaFJTxb7LFz-J0C32DelnXWFEwyTaUMwuPnAirgAP1k_Vdqlg-rM5s73-65RFe4Kb7_WTQTM-vgXfTVq5jI069jL3aQfnriit3uQfXcPwowGpndZYcx7Ea9FbswXQTJADL_VMFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهار شرط اتحادیه اروپا برای آغاز مأموریت تنگه هرمز
🔹
روزنامه ایتالیایی «ریپابلیکا» امروز گزارش داد که طرح اتحادیه اروپا برای مأموریت دریایی جهت بازگشایی تنگه هرمز آماده است ولی فقط در صورت تأمین چهار شرط، آن را اجرایی می‌کنند.
🔹
این روزنامه نوشت که با فرض برقراری آتش‌بس دائمی بین ایران و آمریکا، شروط مذکور برای اجرای مأموریت دریایی اتحادیه اروپا بدین شرح است:
🔹
«اول. پایتخت‌های اروپایی در آینده باید درمورد رضایت رسمی آمریکا از حضور نیروهای اتحادیه اروپا در تنگه هرمز با یکدیگر دیدار کنند.
🔹
دوم. رضایت ایران برای حضور یک ناوگان خارجی در سواحل خود. کانال‌های ارتباطی بین کشورهای اروپایی و تهران هم‌اکنون برقرار شده است.
🔹
سوم. حمایت سیاسی از این ماموریت دریایی توسط سازمان ملل متحد.
🔹
چهارم. اخذ مجوزهای لازم در پارلمان‌های کشورهای مشارکت‌کننده، مشخصاً در ایتالیا و آلمان».
🔹
این در حالی است که جمهوری اسلامی ایران صراحتاً هشدار داده هیچ کشتی نظامی خارجی اجازه عبور از تنگه هرمز را ندارد و در صورت هرگونه تلاشی در این زمینه، شناورهای مذکور هدف قرار خواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/akhbarefori/653985" target="_blank">📅 12:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653984">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qur8LRpv8HDquRF5Nex4z1aWkiTSA7sAVRCEURCcaUV0RuYUqnZ_rAKCq7CKfk6UbYlulVlwm57eaxzOX4uYGUtAKVPQIyZzPt1DGY-9EhOTE51sRDis4xHdAG4ygwMWP5-xjBDYp6HH46M6PYtETQvgt-pzRqDVZRF3hfCoAZIlKbFnMZcBteguAa8VMk10bVhyZa_HoUJEDrbsPMBU9TKPTzrvitYpz3TGv0Gh2F7EJqrqmsp_N2KylfsTBEGhcLjyxkfC-9uvqZTEPlFYrwxik1UvFkinbMRZrF0JmdTrEzwPyIgejWCpNaGov6GXLfKUYU_3DtXhkewmBizlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رژیم صهیونیستی، سناتورهای جنگ‌طلب آمریکا و گروه های تجزیه طلب و تروریستی دنبال تخریب توافقند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/653984" target="_blank">📅 12:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653983">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تصویب مصوبات جدید در خصوص وضعیت اینترنت
🔹
در چهارمین جلسه ستاد ویژه ساماندهی فضای مجازی، مصوبات مهمی در خصوص وضعیت اینترنت کشور مصوب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/653983" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653982">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP8pt2eDOnG9WeLaOwv3kwlE0MHkPh7Fm-JCC4-9Yi-SBOFo7BUuUBzAAwgEjAqxgmEsqDLLVLtJiiDQBLMfVqGTTJPk71AH_MEUcl5hRFOgQlobcRwJ04dXDhnIhBXJO202RxfmXLaRoTbTai5bXBz8oOVXFg3axYNZFkn_pfTcHM4PyRvSz8ASJKTTnfN5nVKVJoclJylLKlC1cg5VidhIxZYEK7nhS_RCwEokovlwynwv1XdfrEgGIBAyoEBS-OtzciKDG6a-HDHGhAKGeWXIoZ2iSwUFTtPiIYv2m1JB6x1uTQ7V1AiUHQ2tjtb-5Ka8lTY9nXGLzrFT0PnM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خنثی‌سازی بمب سنگر شکن ۱۰۰۰ پوندی در چگنی
🔹
سپاه لرستان: بمب سنگر شکن ۱۰۰۰ پوندی از سری mk در ستاد فرماندهی انتظامی شهرستان چگنی توسط متخصصان و مجاهدان گمنام یگان کشف و خنثی‌سازی سپاه استان لرستان صبح چهارم خردادماه خنثی‌سازی شد.
🔹
به سبب عمل‌نکردن این بمب در مجاورت یک بیمارستان و یک مرکز درمانی، فعالیت این مراکز در روزهای گذاشته با اختلال مواجه شده بود که با این اقدام ارزشمند رزمندگان یگان کشف و خنثی‌سازی سپاه حضرت ابوالفضل علیه‌السلام، فعالیت این مراکز به حالت عادی خود بازخواهم گشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/653982" target="_blank">📅 12:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249b96e72b.mp4?token=RIxmt7D6Su7_l8DhGv7qKdwJjS1LOOk5fgJtjpIPMChcq2s49pVyrNWFNBfWfBkYaCxI_rDNPQRnNCK84SFvSlpHrKvUy-MOeXYW9uaW1UyASzlxp1emLejtdIGaBxmt6xIWbeGOpJbnjHBfCcITvveUWbcdqHlQz_t5eHrBJQ29uoGZxkfysI2WNhB2DjVUzYbrLKLyWfPCcEnG4kMFP1HklqUcwgsoiTNwIGbJCiCVNiXY1XRpE46qPaAnsRS0kFJ5jZInHLXJ2KWCLgVtVETyp-yZSAFaU_qTbvyRJNDi-I-P2xzuVNmA14uaG01Lwiu_ul7qOp1uMIQvSXpHkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249b96e72b.mp4?token=RIxmt7D6Su7_l8DhGv7qKdwJjS1LOOk5fgJtjpIPMChcq2s49pVyrNWFNBfWfBkYaCxI_rDNPQRnNCK84SFvSlpHrKvUy-MOeXYW9uaW1UyASzlxp1emLejtdIGaBxmt6xIWbeGOpJbnjHBfCcITvveUWbcdqHlQz_t5eHrBJQ29uoGZxkfysI2WNhB2DjVUzYbrLKLyWfPCcEnG4kMFP1HklqUcwgsoiTNwIGbJCiCVNiXY1XRpE46qPaAnsRS0kFJ5jZInHLXJ2KWCLgVtVETyp-yZSAFaU_qTbvyRJNDi-I-P2xzuVNmA14uaG01Lwiu_ul7qOp1uMIQvSXpHkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت اعضای ناوگان صمود از ۴ روز جهنمی در اسرائیل
🔹
پس از اینکه دهها نفر از سرنشینان ناوگان صمود از کشورهای آلمان، ایتالیا و فرانسه از شکنجه و آزار جنسی خود توسط نظامیان اسرائیلی پرده برداشتند، اکنون سرنشینان استرالیایی این ناوگان نیز روایت‌های مشابهی بیان کرده‌اند.
🔹
برگزارکنندگان «ناوگان جهانی صمود» اعلام کردند برخی از بازداشت‌شدگان پس از آزادی به دلیل شدت آسیب‌ها و جراحات به بیمارستان منتقل شده‌اند.
🔹
«جولیت لامونت» فعال استرالیایی و مستندساز، در گفت‌وگو گفت: «این فقط آغاز چهار روز جهنم مطلق بود. من به چشمان بی‌رحم‌ترین انسان‌های دنیا نگاه کردم و هیچ چیزی در چشمانشان ندیدم. باید جلوی این افراد گرفته شود.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/653981" target="_blank">📅 12:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRvD7QREXksB7hXYOsCAqG4odU1PpCQ0GCBVm30uv7S-94DSPqVPdC0ZlFKF5bhuofdQJqtYI9LUu8WpTZyMUg99rlOqXlMKc7x5aVMJXisJ0OL4cfs252P6BLBjMW4ZzeisFobNnxO2b2SrDiBth-DFL0qj-VSiaIBC5y8GWvEzw6E9zkyXWIqGLMvpPd_2Gpjd0fQ33Qctv4oPM6LTiR7eZ-NAjc1Z16qOQZZ5OioY76cyMmnU_WDCAg9AYN3Ww-kZZP2l25AU8EpVyOJL5B0H8T5qr9hiTZwc0xfXlIVnpJPXYx6nc_X9i_zgttdzDo9b30lfl1S_zTFWcO9A9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: ایران زیر بار زور نمی‌روند/ اگر توافق می‌خواهند مذاکره کنند، اگر بنزین ۶ دلاری می‌خواهند بایستند و بلوف بزنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/akhbarefori/653980" target="_blank">📅 12:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653979">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تشکیل جلسه ستاد ویژه ساماندهی و راهبری فضای مجازی کشور
🔹
چهارمین جلسه ستاد ویژه ساماندهی فضای مجازی به ریاست معاون اول رئیس‌جمهور و با حضور اعضای ستاد برگزار شد.
🔹
در این جلسه مصوبات مهمی در خصوص وضعیت اینترنت کشور تصویب شد که پس از تایید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ می‌شود.
🔹
اخبار تکمیلی به‌زودی اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/akhbarefori/653979" target="_blank">📅 12:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653978">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4jluRSQfrP7MMHV8W_mjJ7GvUILp90soyqbRrgT5V1f7R-Z_CVg8gx2I5YPGDE1FBlD7-mqE80AsYR_DOhq8rfN-glE9T7XUbUg1mKSk5N7OgZncAD0NHoZbMfmuyNi26Em6nHQSq3FR_3CQU-qMXG-IrWj8fLc4sjn9J1nKtdY1SkEOIy6iSUb4-veaMqFlPW3UeglHeaslkaEZOJn6L1C5g0iRlKQWMF-eU3O_qhTEzEeEpeKsu4uzVfL-iI1WLRYAYX7icIYyFD1ErICeUBV7Heum0LC9oAmlQIUx7l9yj6F1xd1v2W5TVkm62QiEGOlA8XcdOSLMdTp8SGe6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقابله با رانت و قاچاق مطالبۀ رئیس‌جمهور از اتاق بازرگانی
🔹
پزشکیان در نشست با اعضای اتاق بازرگانی، مسائل و موانع موجود در حوزه‌های ارزی، انرژی، تولید و تجارت را مورد ارزیابی قرار داد و دستورات فوری و لازم را برای تسهیل فعالیت‌های اقتصادی و رفع مشکلات موجود به دستگاه‌های ذی‌ربط ابلاغ کرد.
🔹
رئیس‌جمهور: دولت خود را موظف به پشتیبانی از تولیدکنندگان، صادرکنندگان و کارآفرینان می‌داند و در مقابل، انتظار دارد تمامی فرآیندها با شفافیت کامل انجام شود و زمینه‌های رانت، فساد و سوءاستفاده از بین برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/653978" target="_blank">📅 12:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رئیس پارک فناوری اطلاعات و ارتباطات: دسترسی به اینترنت بین‌الملل تا هفته آینده محتمل است
🔹
مصطفی مافی، رئیس پارک فناوری اطلاعات و ارتباطات: اگرچه با هماهنگی نهادهای امنیتی بسیاری از شرکت‌های فناوری با دریافت ip ویژه حمایت شدند، اما به نظر می‌رسد محدودیت های دسترسی و اتصال به اینترنت بین‌المللی تا هفته آینده رفع شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/akhbarefori/653977" target="_blank">📅 12:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86d693271.mp4?token=gk2thl5j6us3aV0jVXpCafQBYuJISDHV6eD8wO8DKTrxIElR0jOKmOpeiqWgaHm6geDGr5YcVew88DaEdbNqY2E8PGCYwn1ZGs9BVuBiGtK_9zbQN-8EXe0LZ3OHqvW_45pe6Kqy9UieWoQKao3SmTogCByS5QBO1j6V4X2XtdJqPl682GbGIATiZnbZq1BtMTnMACO6gaueGlB0achetJq6Yc51nuA5zA9DDmhPLsLLdpTJ_fyk_WAyPnh-Z-7CCULTd8OWJHTUllu4ON9D21LIeQquXWUEfsbAkVaSqbiqDeJmwlY5KHO0eUOMzO7FWNW0-miV_ZPVe7SpKJfExA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86d693271.mp4?token=gk2thl5j6us3aV0jVXpCafQBYuJISDHV6eD8wO8DKTrxIElR0jOKmOpeiqWgaHm6geDGr5YcVew88DaEdbNqY2E8PGCYwn1ZGs9BVuBiGtK_9zbQN-8EXe0LZ3OHqvW_45pe6Kqy9UieWoQKao3SmTogCByS5QBO1j6V4X2XtdJqPl682GbGIATiZnbZq1BtMTnMACO6gaueGlB0achetJq6Yc51nuA5zA9DDmhPLsLLdpTJ_fyk_WAyPnh-Z-7CCULTd8OWJHTUllu4ON9D21LIeQquXWUEfsbAkVaSqbiqDeJmwlY5KHO0eUOMzO7FWNW0-miV_ZPVe7SpKJfExA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین شعارهای ضدصهیونیستی در برلین؛ ۳ هزار معترض به حمایت از ایران، لبنان و فلسطین برخاستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/akhbarefori/653976" target="_blank">📅 12:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f516eaef.mp4?token=oS0jNhyb2J42OcqAYhfQ9JY4HpFA9hgocxKj1mLVBggargNsLan62LTVXYqtOzdVaW0ZVLLY-zR_MchD2ZLedO3YKCDsPkh9CgiEFyxmK3V9K-8w1TjETm8cHF44A5A5TqaDyqRTxSW-03Uk7pCiklGA2UdLXc9GMYgKVvJLH-Wp7Z_ux90pJje_lpEhSLDjDL1qim5PA0OAUGCuHm0wHWQRN1cYFwyF81ksFDhhnTaklRKJXhZuAZisw7YZgdAxktHy2T2tmyPLT0hoZE5hvoy3QSM7KKmLwyaOOYsPqHWA9tpAbNpEQPRfdtOK6I_OHx_AhL_oc8cJgKQe3hIHZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f516eaef.mp4?token=oS0jNhyb2J42OcqAYhfQ9JY4HpFA9hgocxKj1mLVBggargNsLan62LTVXYqtOzdVaW0ZVLLY-zR_MchD2ZLedO3YKCDsPkh9CgiEFyxmK3V9K-8w1TjETm8cHF44A5A5TqaDyqRTxSW-03Uk7pCiklGA2UdLXc9GMYgKVvJLH-Wp7Z_ux90pJje_lpEhSLDjDL1qim5PA0OAUGCuHm0wHWQRN1cYFwyF81ksFDhhnTaklRKJXhZuAZisw7YZgdAxktHy2T2tmyPLT0hoZE5hvoy3QSM7KKmLwyaOOYsPqHWA9tpAbNpEQPRfdtOK6I_OHx_AhL_oc8cJgKQe3hIHZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: حتما بخشی از پول‌های ما خرج موشک و پهپاد می‌شود/ اگر چنین نمی‌کردیم دشمنان ما می‌توانستند به مطامع‌شان برسند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/akhbarefori/653975" target="_blank">📅 12:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiKZhnD1CeHeTmXdd4bcD0TbgTHcFXAiURQ1-yfUUvsXxqHEpcPYrUvwK4lEIRY9sl8Ji_nph1vqEdqyOWMaYXcG85Bbbe2Mte_Whhs8b-ToURDHnu9uhJ2IOJ-4j4PWw9otgKihOSJ7SN1bsbUvnlxx6n1P1vaijVBNv7QnoLs1THbV7Ec4W0nC3rGq2voud5u3pCDJKoEid_4scXxfdTxHp-juryRRy7UaXVPs16KDbssvAQmRpKuZLOVOm8j_b1jjrKkCPVHh44b7mYgsRUF0Kf_9tO3k7gFrMbIGnnuwfBF8Bv728djLIh2Fr2AgjLTh_z1glX39jPhNVPO9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک مرکزی: برای کنترل رشد نقدینگی سپرده قانونی بانک‌ها یک و نیم واحد درصد افزایش می‌یابد
🔹
همزمان، بانک مرکزی حمایت هدفمند از تولید و تامین مالی بخش‌های اولویت‌دار اقتصاد را دنبال می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/akhbarefori/653974" target="_blank">📅 11:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653973">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فرمانده قرارگاه خاتم: سامانه‌های جدید پدافندی به کار می‌گیریم
🔹
دشمن بار‌ها مدعی شد که بخش نظامی ما را در حوزه‌های دریایی، هوایی و موشکی نابود کرده‌است؛ ولی همواره ما در صحنهٔ جنگ نشان دادیم که همهٔ ظرفیت‌های ما باقی مانده است. ما تا آخر با دشمنان مبارزه و شکست را بر آن‌ها تحمیل خواهیم کرد.
🔹
روند ارتقاء تجهیزات ما به لحاظ تطبیق با شرایط روز، مرتباً درحال پیشرفت بوده و این موضوع در میدان مشهود است.
🔹
پدافند هوایی ایران در جنگ تحمیلی سوم به‌مراتب بهتر از گذشته عمل کرد؛ ان‌شاءالله سامانه‌های جدیدی را به‌کار خواهیم گرفت تا بیش از پیش با حملات هوایی دشمن مقابله کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/653973" target="_blank">📅 11:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653972">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhkfXLMPNNKd4sdnSYT931M5gB-UScmsq1cjeQ-Coks5NyupDP4yLqzaLEO6fg1lBSfNa6C4rT6Xw_bU9EeFroV5YrHmhMmtm_PpPMEJMU5bWArGMYpC16aen6pz-1mMaA3MZVT4fMh0w2-ZPq8zBt4P9AyL6P_L1a6oApXkgjlvmfXT1QkwSjfcxhGPK-ZzaDY8EtFSV6Xh69bPJfqLAExDr7J8atcPXFfedMPVg6ALqbZtEQHkU5ecoDfAT0YRNGiesG0FfEOjt0lvYin5km_SVjxXkNdaX-l2dhXIM4HZLXTpapHVNksWN7Ma7YtGe_sWCrD2BHh1Z-bKgYjBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا دبه کرد؟ روبیو: اسرائیل حق دفاع دارد
🔹
در حالی که به گفته مقامات ایرانی، آتش‌بس در تمامی جبهه‌های جنگ به ویژه لبنان در تفاهم‌نامه بین ایران و آمریکا مطرح شده است، وزیر خارجه آمریکا در جدیدترین اظهارات خود گفت که اسرائیل حق دارد از هرگونه حمله توسط حزب‌الله جلوگیری کند.
🔹
مارکو روبیو در پاسخ به این سؤال که آیا اسرائیل طبق توافق، به لبنان حمله نخواهد کرد، گفت: «اسرائیل همیشه حق دارد از خود دفاع کند. هر کشوری (رژیم) در جهان این حق را دارد.»
🔹
وی ادامه داد که «اگر حزب‌الله قصد داشته باشد به سمت آنها موشک پرتاب کند، اسرائیل کاملاً حق دارد که به آن حمله پاسخ دهد یا از وقوع آن جلوگیری کند.» به نظر می‌رسد که روبیو با این اظهارات، این موقعیت را برای اسرائیلی‌ها فراهم کرد تا به بهانه حمله پیشگیرانه، حتی در صورت امضای توافق آمریکا و ایران، همچنان حملات خود به حزب‌الله و مردم لبنان را ادامه دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/653972" target="_blank">📅 11:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653971">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a012e51993.mp4?token=rjsdEf4q0SmpX1UQbdVVfnxB-9lRNvvhzDGbk445_T8gUmW6fYLqvxc7LWpu_kh0yfHtrEzxj5NkniihEG0UqNWMfPh8THQvB7DP6i_1Rr_u-RYbKY412HLjwj6L9KL1qh13oGf5qtMz7KwoMUlEPul0NzJd-0FGDpE4nPdznzRczygvP6EZZVfQ1PBGQoaeiQhKle0RjtgoSRbSgYPQkA6G3ekD5qjRNtOxAj2JsYEFXMfI8jO5A8tXk4QdDY3RmeX04WrVDMVuN-m5aeaRSwlrAkNES64Xpoy9gU_HJz8PZ0kqGKXrMHlkN3oEGCRKwzijKIfJvTvd8UzkAWldOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a012e51993.mp4?token=rjsdEf4q0SmpX1UQbdVVfnxB-9lRNvvhzDGbk445_T8gUmW6fYLqvxc7LWpu_kh0yfHtrEzxj5NkniihEG0UqNWMfPh8THQvB7DP6i_1Rr_u-RYbKY412HLjwj6L9KL1qh13oGf5qtMz7KwoMUlEPul0NzJd-0FGDpE4nPdznzRczygvP6EZZVfQ1PBGQoaeiQhKle0RjtgoSRbSgYPQkA6G3ekD5qjRNtOxAj2JsYEFXMfI8jO5A8tXk4QdDY3RmeX04WrVDMVuN-m5aeaRSwlrAkNES64Xpoy9gU_HJz8PZ0kqGKXrMHlkN3oEGCRKwzijKIfJvTvd8UzkAWldOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: قطعا بخشی از پول‌هایمان را خرج موشک و پهپاد می کنیم که اگر این کار را نمی کردیم، دشمنان می توانستند به اهداف شان برسند/ پل ها و نیروگاه های ایرانی خار چشم آمریکایی شده است
🔹
سخنگوی وزارت خارجه در پاسخ سنگ های میناب از شنیدن سخنان وقاحت آمیز مقامات آمریکایی، کهیر می زند.
🔹
بعد از ۷۳ سال اقدامات علیه توسعه ایران، باز دم از دلسوزی برای مردم ایران می زنند.
🔹
آمریکایی‌ها در ۴۰ روز تجاوز نظامی به ایران، فقط زنان و مردان و کودکان ایرانی را هدف قرار ندادند، بلکه به تاسیسات زیربنایی ایران حمله کردند.
🔹
آیا صنعت فولاد و داروسازی ایران با پولی غیر از پول مردم ایران ساخته شده بود؟
🔹
لفاظی‌های آمریکایی ها، برای فرار از جنایات چند ماه اخیرشان هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/akhbarefori/653971" target="_blank">📅 11:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653970">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIqdQr7tVa6DP1RmhOfdnp6MMDniQC18B7sVC34i3_e7eMgLYmc5H5osgdVIo6btAxgXFrqCTAbBK-h7qoAfmI0BPSAJAl78kiYXHQ0UNfRjvX9ZJKARZQMHBsWxkABjRMnJGEMOAa3QcR0U6w4oK3TG1dLDdhtjOPSG02dD0CHcZCjZat9u8lvSvCUiN0BlTa8w7IUli9ChtOnfcdWRxQKOIUQrl9u_tWuIPDEg5aZ9vVITyqgGiZ3jzdQJInk5mgLneCsGaIk50raI1KJL23eKYho4BuwThEGWMx5SDiOttqov1vXvwuZOWMG8AQCY6hlVvvzo-z-xouEOX9ZCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده قرارگاه خاتم: سامانه‌های جدید پدافندی به کار می‌گیریم
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا در واکنش به ادعاهای آمریکا درباره توان نیروهای مسلح ایران، گفت: روند ارتقاء تجهیزات ما به لحاظ تطبیق با شرایط روز، مرتباً در حال پیشرفت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/653970" target="_blank">📅 11:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: بسیاری از کشورها در تماس‌های دوجانبه با ما، به شدت از وضعیتی که ناشی از اقدام آمریکا و رژیم صهیونیستی است، ابراز نارضایتی می‌کنند و از اینکه یک ساز و کار مطمئن و پیش‌بینی‌پذیر برای مدیریت تردد در دریانوردی تنگه هرمز ایجاد شود، استقبال می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/653969" target="_blank">📅 11:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
موضوع توقف جنگ در همه‌ی جبهه‌ها در پیش‌نویس اولیه توافق احتمالی لحاظ شده
🔹
سخنگوی وزارت امور خارجه در پاسخ به پرسشی درباره لحاظ شدن موضوع توقف جنگ در همه جبهه‌ها از جمله لبنان در پیش نویس توافق اولیه با آمریکا، آن را تایید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/653968" target="_blank">📅 10:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
نگاهی به آرای کاندیداهای ریاست مجلس در انتخابات میاندوره‌ای
🔹
نمایندگان در نشست علنی امروز (دوشنبه، ۴ خرداد ماه) مجلس شورای اسلامی، با ۲۳۵ رای از ۲۷۱ آرای ماخوذه، محمدباقر قالیباف را به عنوان رئیس مجلس در سومین سال دوره دوازدهم مجلس شورای اسلامی انتخاب کردند.
🔹
لازم به ذکر است که آرای محمدتقی نقد علی و عثمان سالاری برای تصدی جایگاه ریاست به ترتیب ۲۹ و ۷ رای بود و آرای سفید ۵ رأی، تعداد کارت های توزیع شده ۲۷۶ برگه بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/653967" target="_blank">📅 10:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بقایی: هر اقدام خصمانه ای با واکنش ایران مواجه خواهد شد
🔹
سخنگوی وزارت امور خارجه: اروپا نمی تواند یکسویه علیه ایران اقدام کند و طرف مقابل دست روی دست گذارد.
🔹
اگر اتحادیه اروپا موضع مسئولانه ای اتخاذ می کرد شاید بسیار مشکلات جامعه جهانی روی نمی داد.
🔹
در موضوع تنگه هرمز اگر اتحادیه اروپا به اعمال قانون و منشور ملل متحد پایند می بود شاید وضع کنونی ایجاد نمی شد و باید آمریکا و رژیم صهیونیستی را محکوم می کردند.
🔹
تنگه هرمز تا قبل از تجاوز به ایران باز بود و به علت تجاوز به ایران، وضع کنونی ایجاد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/akhbarefori/653966" target="_blank">📅 10:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG9SxUSW_ITBKxVniRcZ6PpgY74lrZPUlJ3kX3bYtCurm8URoYEslSby-PJDosIFFeNyj_aLN9I5CqtU0nF3ybH-UCLz3nqW5DunjNWI_KQ02HRR5s9_a6G5LH2HoQMPyZFAhbWROrlz-qE_IQdq0jIixvIx60kIkOZAKYi9--fyFaJR7bXBXT3ieZcqNRbATl3B1yKIe38hrKwrtZQMNWcgUIBbc1UWomiAGRp1pVRJbE-xHMlu9vqIGkJAvzn-nU8VyDLrUbhEoYGDgrLV-T1vuaOOY8Kxhl8XHe-moIntGoAp5XYs5dGH4vKtebl8rSYxZ6q_839XE2snNwYVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی: هیئت مذاکره کننده ایران، بخشی از حاکمیت است
🔹
سخنگوی وزارت امور خارجه در پاسخ به این که تضمین متعهد ماندن آمریکا به تفاهم احتمالی در مذاکرات چیست: تضمین ، قدرت ماست و درسی که ملت ایران به متجاوزان داد
🔹
این که تمهید هیئت ما چیست باید گفت تمهید ملت ایران است.
🔹
هیئت مذاکره کننده ایران، بخشی از حاکمیت است.
🔹
تمرکز مذاکرات بر خاتمه جنگ است و در این مرحله درباره جزئیات هسته ای بحثی نداریم.
🔹
تهدیدها و کاریکتاتور کشیدن بخشی از سیاست ورزی در آنطرف دنیاست ، ما در میدان عمل، فارغ از تصورهای طرف مقابل عمل می کنیم.
🔹
سخنگوی دستگاه سیاست خارجی در پاسخ به این پرسش که چرا وزیر امور خارجه و رئیس جمهور به تهدیدهای ترامپ پاسخ نمی دهند: ما کارهای خیلی مهم تری داریم اگر بخواهیم فقط پاسخ دهیم به توئیت ها و عکس و تصویرهای طرف مقابل به کارهای مهمتر نمی رسیم ما متمرکز هستیم بر پیشبرد و طراحی برای صیانت از منافع ملی.
🔹
ما سبک خودمان را داریم و قرار نیست که به سبک طرف مقابل عمل کنیم هر جا لازم باشد به سبک و سیاق خودمون به عنوان ایران متمدن عمل می کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/akhbarefori/653965" target="_blank">📅 10:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By0p_N9jzitPrP3FtQ_j0ylVKxmv3kAWUmFiBvei0-TSd8rZWayfjbrzsJ1jrCoQlAfithmM93YuJv16qaNbmIuvttFaUomVxnYB2bkILhmZBhZZc--JrWnHofirvwm-phSmoLur-uMbqrrd-etQQoXk4ihlT4_FnopiLuBMu97Bqnx4IdGWCLnGhqrBNLeIPw3XHV68yQ7qGcWHMx9DMVfJ-0p0FdsOomQlboQ298YVMC9aMZtKqOpCT5va-FKchLiwDJaACfWB5CrMQNjZ2foYsMfqobEWvjgw-66uGQyPw7WrSI3GZIMDgvwBmtr2cZiyuBins1EuNf_BGqSqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر عاصم منیر به چین
🔹
تلویزیون پاکستان امروز گزارش داد که عاصم منیر، فرمانده ارتش این کشور و میانجی مذاکرات بین ایران و آمریکا به همراه شهباز شریف، نخست‌وزیر پاکستان، برای دیدار و گفت‌وگو با مقامات چین به پکن سفر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/653964" target="_blank">📅 10:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E25LQ5aaV4sQeQM_1tcZ5CQbhIgFW2Q_W0cf7fHIdf2MHMFQoh7ewR7YcFk7KF3y0vFrfiCRcRbTf-HsyI1CxmjZw1daApPJl7zULRgtO2VqyPuuQuTfzDpIGfFYLwWCN_SthyZn9XNO-MnjoCJ6Aa8rhuXzjCT1tdEnQFnBEBJUzMih1lUTNG4GWmNyYio1RxxINTc8laTc14dEv3yJlNoByyQd9jl0G91HH01RCK9WwgJY1VyknSy74qS-yBv8sVtkSlisFjdCxgfxbBhhLGUFZKAwZVuwjLl6Su3zd--4wPOsu8TEQlznOO1nS5V0xdrO-U1MPneI5nWElwOlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه عبری: استراتژی نتانیاهو در برابر ایران فروپاشید
🔹
روزنامه عبری «هاآرتص» گزارش داد: سخن گفتن از «دستاوردهای نبرد»، برای گمراه کردن مردم است؛ استراتژی نتانیاهو در برابر ایران فروپاشیده است.
🔹
از سوی دیگر، روزنامه عبری «معاریو» نوشت: حزب‌الله به دوران تحمیل معادلات بازگشته و نگرانی، محافل ارتش اسرائیل را فرا گرفته است.
🔹
همزمان، کانال ۱۲ رژیم صهیونیستی تصریح کرد: طی هفته‌های گذشته، نظامیان ارتش اسرائیل گفته‌اند که به دلیل آسان بودن هدف قرار گرفتن آنها توسط حزب‌الله، احساس «اردک در میدان تیر» به آنها دست داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/653963" target="_blank">📅 10:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قالیباف رئیس مجلس شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/653962" target="_blank">📅 10:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5275bdcf0.mp4?token=C2ViB7Tj-R3OuhE_7x7fKAQ32_cP-yQuo52vO8qRH8jiYTPnOUyi14EozHKiX_FeJiGP-eC-Mx2WGw_v9hd5oJkXv1AIkjmr6sz_aPOvg4mU_AcgPwYrnIRfXfdtkb-HoREYxi0yGjE8zmv8CTkfBVUPtOnNYDyHX2M59DUhUPSSEHgWirO8Ipk8Pf1lVH0R6JutWFUZyTOxu85ATnAOUmjTWWjyMwoINu8l663Hh1gwJsAqE8F97mJ1-N3mxFSbr5XdwyiyoXcJ57JUoLCsmrMipbDfBM3OJXLLR0sFaNjTrwtomUw8X52FWjSoR-rXC6x9CeXCC_3tJ_TcGseZEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5275bdcf0.mp4?token=C2ViB7Tj-R3OuhE_7x7fKAQ32_cP-yQuo52vO8qRH8jiYTPnOUyi14EozHKiX_FeJiGP-eC-Mx2WGw_v9hd5oJkXv1AIkjmr6sz_aPOvg4mU_AcgPwYrnIRfXfdtkb-HoREYxi0yGjE8zmv8CTkfBVUPtOnNYDyHX2M59DUhUPSSEHgWirO8Ipk8Pf1lVH0R6JutWFUZyTOxu85ATnAOUmjTWWjyMwoINu8l663Hh1gwJsAqE8F97mJ1-N3mxFSbr5XdwyiyoXcJ57JUoLCsmrMipbDfBM3OJXLLR0sFaNjTrwtomUw8X52FWjSoR-rXC6x9CeXCC_3tJ_TcGseZEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا به دنبال باز کردن تنگه هرمز به هر قیمتی
🔹
سید محمد مرندی، تحلیلگر سیاسی: آمریکایی‌ها نیاز دارند تنگه هرمز به هر شکلی که شده باز شود. می‌دانند با نیروی دریایی یا هوایی نمی‌توانند این کار را انجام دهند. چند هفته پیش عملیاتی برای باز کردن تنگه آغاز کردند، اما پس از چند ساعت ادعا کردند که به درخواست پاکستانی‌ها فعلاً متوقف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/akhbarefori/653961" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtXzF-iG8yuuj78LAoYJktl17fI_q1peemJXNH3BIrNTolY4kfN4-zFOMBJNBdrDF-Fh-x3jcBqTKBI1EJsNgHp4bYn5C2f3fgMVnaGoDOM-K7ONpMA97MttVN-61Bz3wqmZD6MRSTG77EdmVMt6mZgiyPq8JyodazHww2x1wNI88lSEMS5JuNr15_yv7COThHE-PAbLRz0GQE-7loSHbz4g077ObQzA6Hmim9lSK8rEXv9W2SpIYfXGlvGIAhwPbGPk8mlCNNuC-OfLm3-oZI4Il2jsIf8XhogScIJLDXqPoXrX9ly9wfAtSfBzhFiTF8dWSEE7yjzoCmyCp95jFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا منتظر بنزین ۶ دلاری باشد
🔹
سخنگوی کمیسیون امنیت ملی مجلس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/akhbarefori/653960" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
از قبض برق تا قبض روح/ مشترکان پرمصرف منتظر صورت‌حساب‌های سنگین باشند
🔹
مدیرعامل شرکت توانیر در پاسخ به سوال: یکی از برنامه‌های راهبردی شرکت توانیر، رعایت عدالت در توزیع یارانه برق است. برقی که در شبکه سراسری توزیع می‌شود از یارانه‌های دولتی برخوردار است و طبیعتاً اگر مشترکی بیش از سهم خود برداشت کند، هم در حق دیگران اجحاف کرده و هم در تامین پایدار برق برای شبکه ایجاد مشکل می‌کند.
🔹
اله‌داد در خصوص گروه‌های هدف برای اعمال محدودیت‌ها: تمرکز ما بر مشترکانی است که بیش از ۲.۵ برابر الگو، مصرف دارند. اگرچه این گروه تنها ۲ درصد از کل مشترکان را تشکیل می‌دهند، اما بیش از ۱۰ درصد از برق شبکه را مصرف می‌کنند.
🔹
هم‌اکنون بیش از ۸۰ درصد این مشترکان به کنتورهای هوشمند مجهز شده‌اند و در صورت افزایش مصرف بیش از الگوی تعیین شده، برق آن‌ها محدود یا قطع خواهد شد. مشترکان پرمصرف باید منتظر صورت‌حساب‌های سنگین نیز باشند؛ چرا که قبض برق این دسته از مشترکان ممکن است در برخی موارد به «قبض روح» تبدیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/653959" target="_blank">📅 10:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
وزارت امور خارجه چین: جنگ ایران هرگز نباید اتفاق می‌افتاد و نیازی به ادامه آن نیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/akhbarefori/653958" target="_blank">📅 10:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKse0ItxA2DVP_6pw9U0wjZBkyKq_ez63X-gtqSsF-jxUsa95xB4vMaXpkkvofc2Tjo_lruOEZcg7txFQ0S7pnyna7q6ZPEyVXQPyFh8VsijVSZBFVQH0kF9b99WlVB7B8X_l4GzPtf8i7LbuUZnIYXzRnPnirk7AjXxffzkfOnPzck-vmEaYDBpOz3AAnIQC9cE5bN7EXXk-_WNVneem_8RRHn1_MyB43sLEVPqI9CitUURKu_qK623sLJJMAYeX0ECH6JCI9Sf8JiIRa6vKsN6VGbHU3ETshC7WJEfnHtfnVE5FmtUCjbPcHmyBpEzuxBqbu-06TqhpVQGy2sN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان وال استریت ژورنال به جاه طلبی رژیم صهیونیستی در غزه
🔹
روزنامه وال استریت ژورنال فاش کرد که رژیم صهیونیستی با نقض مداوم آتش‌بس در غزه، کنترل بخش های بزرگتری از نوار غزه را در اختیار خود گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/653957" target="_blank">📅 10:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8NsJdgCUULE2InnpeIRzClnQQp63f7sxRemufN1sXpW7JSckyxBQ3X44ASsFIVf0wLa3_P93TYARUob3sisioNNYza5Z6eJQyWd2GKUsu6wkviWMEygNe14IfxxwGkzPjUAd-6dO_SqChIi-L-FebP6mPg4F1x8PJY8ISysF3BnsIEYkJkFwXhvmLlRSSL7hZRt7NfXCzHgeJFlyrVp35eHj2SRmaCN1nJG_2dVKV2IFWzdzMYSnIAZ5Mpen17yLDetyXSYuEinCPBwRP586u-59S369j_THCfodBdYrE0eZIXBLiICSfkQnYjfeM4-2Vo0qrh4es7HmkEJo6Wu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مناسک حج آغاز شد
🔹
همزمان با فرارسیدن یوم‌الترویه (روز آماده شدن برای آغاز مناسک حج)، فرآیند انتقال زائران حج به عرفات از ساعاتی قبل کلید خورد و مناسک حج تمتع امسال وارد فاز عملیاتی شد.
🔹
۷ هزار زائر اهل سنت کشورمان با اتوبوس‌ها از هتل‌های محل اسکان خود خارج شدند و حدود ۲۳ هزار زائر دیگر هم امروز به مشاعر مقدسه منتقل می‌شوند تا از فردا خود را برای دعای عرفه در صحرای عرفات آماده کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/akhbarefori/653956" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDT9O94aRDmpKxTmLPRfSNP_J-lhgFyLpTyA0icIU6K-2rdW0Hao5pX6_qDPAIVjEOWF_wDXF-Y2mCroLIEAip22K9s8G6WxyfOHBrkAAaIiZl0UqhXaub4Ajt9TQlbvIxFXPR7Ef0GSUKnxIvswi11W9k--sxigmZoDaXKQbww33Ppc6LzbvKiF2LNboTfAdOh-26ImxvFEI7RTPpZbr3fi5CkDON29HknC5F8YJYnDJN-0mvB-0Z61lkuFfcFYxlEhL169dBYxS4_aDTggnBqm2zCDSSVNvlgl3kgaxaV5sS49TivbfXoxnJ_vM6bOh7MFcLGrWZtYMRlE6j6j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: مقاومت امروز همچون خرداد سال ۶۱ و ۷۹ زمینه‌ساز آزادی قدس شریف است
🔹
فرمانده نیروی قدس سپاه: حماسهٔ ۳ خرداد ۶۱ زمینه‌ساز حماسهٔ پرافتخار ۴ خرداد ۷۹ برای حزب‌الله قهرمان بود که رژیم صهیونیستی را از جنوب لبنان اخراج کرد. ارتش رژیم فراری شد درحالی‌که ‌بیسیم‌هایشان روشن و همهٔ امکاناتشان در سنگرها جا مانده بود. مقاومت امروز فلسطین عزیز و لبنان قهرمان هم باعث آزادی قدس شریف خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/akhbarefori/653955" target="_blank">📅 09:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رژیم صهیونیستی هشدار تخلیه ساکنان ۱۰ روستا و شهرک در جنوب لبنان را داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/akhbarefori/653954" target="_blank">📅 09:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMZIOb2zt_EPtVzmOHRp47t-pXF0vUwrWXLo6ZOATTp2JBt73s4reMgPCGyKO5cL0NASndpQhS34pcnNjZU4HDDkczNJwP6A4syYVSW8CZRZcJjvPxRJrlV3dIF-xqicVbCGnrq_a0K1RXUhYIlU59rbQv97mxYe5DJI2A1_ODJF27qNaoqynGWDrBdhySPjlv_yN4Tw71dbQZxHN131CZncBnPS2n6wYOjW2wCIADMt-Xm6O0UoTblup-dVVK9HNyDVHDavnMieqj-g_SK5LX-dVjbcLN0lOfdFNs--JGRnM7lZk1AkTbhALKSO1RgAmWrqtt6XDG56K_lwEj_FnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود پلاستیک ممنوع
🔹
برای کاهش آلودگی و حفاظت از محیط‌زیست، باید ورود پلاستیک‌های یک‌بار مصرف را به خانه‌های خود محدود کنیم  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/akhbarefori/653953" target="_blank">📅 09:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
دادستان تهران: بیش از ۵ میلیارد یورو ارز با پیگیری قضایی وصول شد
🔹
دادستان تهران از وصول بیش از ۵ میلیارد یورو ارز به کشور از صادرکنندگانی که نسبت به رفع تعهدات ارزی خود در موعد مقرر اقدام نکرده بودند، خبر داد و گفت: بیش از ۲۰ میلیارد یورو نیز تعیین تکلیف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/akhbarefori/653952" target="_blank">📅 09:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg1GrvOyz4UGv7ZErrqCaFFV7E8txUA9qe0eYAGePXBF5tbPQo_Td8UvHikIbbJzejZi-aCYe6OHvtRXK3sQgpjOfTUKh2InUHU3Jo0wdqg7rZ3Dnjc8tQl8nAcPzXDwghiv94yQQ0-m8SMcVogyxVr-77lgIF6L8XiqpJLYku7gLpvtZrdyZkC5pUpz6EbafLNWTVLFVnogY2ssqBXvM-bus6yLV8qflAHJFH2ATBfj5N7pRK2k2fCxPE0q_c8opbM7Vd1-6EGfEIXDltfhpaGY3J85M72plFW7kvMA6-aShK8xvAqV8fJEXXwoLRKxrpgPjKwF0DQ15kWcFkGsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRfz1GyF4FoZEp-7Ae-bpo_9WfkylGTph8UiDvRmtug1UXhCDER12m8AVQNnDT9BC-5nbhPgIleebDqCvwyufVBrS0QdPtrgoKdziPpwVrA-CBEVdVhnr8UbbrZwieP0C3Vczo3n2owhA4ZajDnlJrSVQwqL2YXQJXybEPMWoGDikMkwpaMieRs-EnijncvvoTBnMlrY3ioHoylyp4olZ8dBnQIYsMKKDHbjFnk0V4i2BWiaoBb8G59k7S9aEVIcoJ_kjXh3BMhGYifar0cq22elcccpdf-c0tLh9YaBEPiTil5_g0lOL_bh-DV9q-EESVXZYIceNHcUboX8-qK-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZNTLeSEWn5MIYhB5HkOGoCKK7FftEBruE_jPUS85tPvtiZX9EijwktttPPhQXjm9v4y-zWYDFIaKJKD9kJNqH2yQ8MQz5jTTG-QfhzA4CYe_Y9a40DGG2Rl7dzjarv2cTrI5WDUK0dkkvSWEoJtNVlja1CWHamfngROZue--id34kY5fT2oEsYvFSBCMPfGv5Q2BVFNAZnwzCjyaM-tC--ElHYAKIanPqUCwZ7j6iOzAm-G1C_a0iU1Ppi3AnwQ-F5ORWuAtcyPc6-2NxVaweMY7AEdrbz0hsv0r1P4ESef6ipwbf9IXH4GBIVNvyUwfA16lWpSPWkwwfqKUqCz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETcyCx1Q0WgJNhoK8wye7vIgXr9TRlw84zFhaq-UueSN0TwcCWz2tkcNa4oRB6-ezfWrl8YzJTwjJGqwPEDZ_V3pjU5niLuPctTEgsZtPuP97f9t_Jjn0-JxazRUsXXVT0eAbMt84BA4nfUcP7FV1WKZwb7vHOVSpt3Zlhcn3fk_vieWG7_pH9AlqkC99kNzkJE59c3LgKzvhueILI5_pBt1ojLO1k1oGVgCjoHtesMRVqnQ-AcrFZ3eRwpVQ9WCJBdxONeMHl8yQjIyn1XMJmKUUkXvMyIyq6todZsslU6cFSQGGoIYIDqBcGN9QHylHVYQxe6Id-7wFVKpU5Ce9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gngDuSqmnw0sxXbGJkNJ0jg5FA4eCx5krxcMQcfLGmZlNsMxPu9Lq-S2uatkzPRCI-AC8itrSvQMMIqYscmvsYCJMHfR1QBjsQBCx7Qxsu2p1GwHBYPTpRgJ1PTKoiyfcXNaOSBAgaSLSHZGCAxByKP5xsbH4nqUH0zgHEz1kVVjCO9NIKzrm8-Wwh_YdRll9tk402PyEv0S8ClRzwIjCTolP3MVSYkS-3ACZPscCxCgTIKk6HxYB7ZUSQEKFHb4WmgviVK_oGFrXAUNtolE76NQRyAa3iAERtXa7jgEhICxcxMgE75p_BVEnyxH7-qFlytWGzcLsulpJCIh_8hUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PNmQrO4R9gfkWFOg7fB2cU-9ZsUysm-244W6MeOl6jDj3HVLKASFOJU3un4NHoxclm2d8av471s2-R1paw20A82zgBWSJqbLUaTJa7Q0lONgy8BQzwuN_hNoYbiDq5coLJ5JceF-nLeiyJemAhT8qnpQ3E0nUHMQx15ttFqDyCh8REbQgG3TSHTr7O6l36RIjm5PaLGQq59vmSwIdAauvlbQ-ZQKdC11hkC6xr7IY0vFQiIzE5z41LI62NlNNnK-9MRP0AAbiwixal3bMRZaonb-J48oxWPj1_xx75dn0IT1ybBBCuixKET4OAQ26D8NvtLLqE2BEP962g5zvvzqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekgCJsBMljAYM-MfelpSP7ZRmsKRmVo5KZT2uKdGpMxe5gbeyMmr5t_0XU_44njEk6ISihJ22bhXFCWeLBuuRUMqlS80LZZesWg2_ZCm8uYqIDKKZJjqaEgVqDSF7XUHftwWpuy6LoZewKCo1TE-ZH1s_7pS-GtwtBmvsmsd1MU4oiwoe5yhcz5nuoY1wP2YfY_T8bL00G28AMCQ7vVLUh_Ol3codOW6VClk-hH-1r-lD3shlVal-QWI1SVEJZbPF98MrBwr0-uDYPtyAOqL42dhL3nXBc1sFjWIqncWSJ5KMFCVPpvQhe8EGbF-1xB7qM735IksHrH3pp7Eb8V6yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از آثار تجاوز آمریکایی صهیونیستی به واحد های صنعتی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/akhbarefori/653945" target="_blank">📅 08:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653944">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b82ad759b.mp4?token=kU8qT7plBsAeZFdj8ngkAna2Zcmqbkl8G_vVPeewkkYlFXGICxN406E1GfXNecAKTzsFSV-ExnNNjkinENUF1nzLVph8jWFPbunEzTiCePEUwnmiHZ7lJvv8LNe-VPHtrgcxIh3QJ7wALHKTMtWrrfAj0ntYuU_jislJ_lsDUpOUIvRIHWvIr6RtlholDRum7nHH-WcR1LE3xgdspSy4Hw5Hso17PLJbPL16qF8Hf6voH3tw6n7-0FSl8r3U53wBmuOfeh2lF4Q6D3DpH4OSI394I39sPLD5YspKgRnLf2k8JMe57cwcnx0b0YTuFKropGMP48ueWiJFLWOb_nwWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b82ad759b.mp4?token=kU8qT7plBsAeZFdj8ngkAna2Zcmqbkl8G_vVPeewkkYlFXGICxN406E1GfXNecAKTzsFSV-ExnNNjkinENUF1nzLVph8jWFPbunEzTiCePEUwnmiHZ7lJvv8LNe-VPHtrgcxIh3QJ7wALHKTMtWrrfAj0ntYuU_jislJ_lsDUpOUIvRIHWvIr6RtlholDRum7nHH-WcR1LE3xgdspSy4Hw5Hso17PLJbPL16qF8Hf6voH3tw6n7-0FSl8r3U53wBmuOfeh2lF4Q6D3DpH4OSI394I39sPLD5YspKgRnLf2k8JMe57cwcnx0b0YTuFKropGMP48ueWiJFLWOb_nwWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ قابل توجه تحلیلگر بی‌بی‌سی به مجری این شبکه که قصد داشت مقصر جنگ را ایران نشان دهد: نمی‌توان انکار کرد که هر دو جنگ اخیر را آمریکا و اسرائیل شروع کردند و آنها بودند که به ایران حمله کردند، گروه‌هایی مثل پهلوی و طرفدارانش هم از این جنگ حمایت کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/akhbarefori/653944" target="_blank">📅 08:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653943">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKyZcwLf-sgKZpXtK14FKRUp9LMalADuFl0BLb3h7m4_8dT9W67wx73bx6t3yMYJWDyfmVFHcLNqHyy3LuHKGhYOk3P-5qDBK_60YD8Qu6pcMgFX4w9F_N3_s1M7mtrLxqBBLlVBw8fOdgB2tb0QNpVlgc85GwwkG-V_o7L6aD1SymVkD3mZ-MPk96h0EVcRMk61V1CJDRflkt-10-HNyKBewQ3X-BcSOMKj_GX6N8c3GXyzJ9gJQgKx9n3MaQdPp-Zku-vPSq7sXt052z3_ZSwAHrCHCz6BthVfGrvcOpqw8bCNgFYVqJETXICDYhzOHYv_5cjBpF-w2mX3W9f-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه: ترامپ به ایران ۷ روز فرصت داده تا توافق را نهایی کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/653943" target="_blank">📅 08:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653942">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw5m0VeWCLN5J9VKh88vIZ6tLRbAqYY-BoaQjYhQIFYxcycjmlFvVqsJGA3tLfdjd4YQKDbw2FEdTGN-ka8NW6h_dErknYqbT1KoEfbLD03yeLqRtELotTLG82f4-yXq-BgWr4s7x_MZtHZ5JoOzD_p3E3hDplv8mp1A7yFPC0eOmONRYLSx4lyBYIQf8Gu9L9TItdpRevAxo7hf33bUN0VXTYlzZ83UiOwPdbTDwuu6VG2IUVhbmlaR6gUzCtPOeSs-s2RY-ccW75xDqdx0VhhZTrAeU3EHFsjY_QkRABX9E5tbzGKkq3jjy9cgrAJ2sGIJxTdt1oEIb-LG_vRisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ رئیس کمیسیون امنیت ملی به تهدید اتمی ترامپ: قابلی نداشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/akhbarefori/653942" target="_blank">📅 08:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653941">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2a076d66.mp4?token=vjc9q8SHkp7fwcBArjafmlaL6bFZxnK6QEFJ_GRA23xIda2t8r-rPTvj7KmG45YZYpiLGytvtm17N9nXFwr4uQH7ByaX2oXJoOJ7k3yqV7U6NvtrzQ47QEGrexJY1E-6cmCg3qYpJ0tk34yrTjKWJyynv2CAWT2AoFd8cw4l69vEL0aNJpiylUmTGHyEA2dsR-lVaTXPeb41ECQv5SCQngf2L1tTZ15eh_NjLySAZ202HJSkp8A_xxFxSAoj2OvUu1AP3uXLfxWtjHKO87MPlPTs7oILCgD_bQVkMLxgFzULcolKGCAQI0iuGCAzAsU_TtpSw1x2_OOy8MQlEZMWpm96Utq1kPT8fV1_1FXSlrJnzrJ_d2GQzMSwnJkCAvCgPhSYBzh_5nyT5wuOz4RcAe0J6a97e-jA19TZqcM_qEkXpgPAocmVqcNw8_ZXzaRIO86gJ-NC2XAbDmrzIW5WV73SMB5-zFUFlGyaZmQTNQGHLHCa069_-WwqkZq6M59xqJW53CLDw7vYeaO0j_qC2bULKKhDpxFNs7F_pycqn6LFF8FEYDUQvZ9Gw6M7p7ZEnjYc8wPGy1olT55WbhVoUNelPoOhqtu8vPaJIRLTfv1DvFMSKl-bitrYa4ieI9tHne6jsF2lb9r59EkJRiAhferMlMPd8dwD4NHpp8p8L3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2a076d66.mp4?token=vjc9q8SHkp7fwcBArjafmlaL6bFZxnK6QEFJ_GRA23xIda2t8r-rPTvj7KmG45YZYpiLGytvtm17N9nXFwr4uQH7ByaX2oXJoOJ7k3yqV7U6NvtrzQ47QEGrexJY1E-6cmCg3qYpJ0tk34yrTjKWJyynv2CAWT2AoFd8cw4l69vEL0aNJpiylUmTGHyEA2dsR-lVaTXPeb41ECQv5SCQngf2L1tTZ15eh_NjLySAZ202HJSkp8A_xxFxSAoj2OvUu1AP3uXLfxWtjHKO87MPlPTs7oILCgD_bQVkMLxgFzULcolKGCAQI0iuGCAzAsU_TtpSw1x2_OOy8MQlEZMWpm96Utq1kPT8fV1_1FXSlrJnzrJ_d2GQzMSwnJkCAvCgPhSYBzh_5nyT5wuOz4RcAe0J6a97e-jA19TZqcM_qEkXpgPAocmVqcNw8_ZXzaRIO86gJ-NC2XAbDmrzIW5WV73SMB5-zFUFlGyaZmQTNQGHLHCa069_-WwqkZq6M59xqJW53CLDw7vYeaO0j_qC2bULKKhDpxFNs7F_pycqn6LFF8FEYDUQvZ9Gw6M7p7ZEnjYc8wPGy1olT55WbhVoUNelPoOhqtu8vPaJIRLTfv1DvFMSKl-bitrYa4ieI9tHne6jsF2lb9r59EkJRiAhferMlMPd8dwD4NHpp8p8L3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر محمد مصدق، معمارِ استقلال نفت
#پادکست_کافئین
| قسمت بیست‌و‌پنجم
☕️
در این اپیزود به سراغِ مردی رفتیم که میز بازیِ یکی از بزرگترین امپراتوری‌های تاریخ را به هم ریخت. پیرمردی با اراده‌ای پولادین که در برابرِ انحصارِ مطلقِ بریتانیا ایستاد و غولِ استعمار را در دادگاهِ بین‌المللی لاهه زمین‌گیر کرد.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=CNnq-Y7JNjOTm0Z_
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/akhbarefori/653941" target="_blank">📅 07:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653940">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست پنجم | پادکست کافئین</div>
  <div class="tg-doc-extra">دکتر مصدق</div>
</div>
<a href="https://t.me/akhbarefori/653940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
دکتر محمد مصدق
🗓
وقتی تصمیم می‌گیریم مستقل باشیم و حقمان را از یک سیستمِ انحصارگر پس بگیریم، چگونه باید برای فشارهای ناجوانمردانه آماده شویم و چرا در این مسیر، بزرگترین خطر نه از جانبِ رقیبِ بیرونی، بلکه از سوی «موریانه‌های درونِ تیم» است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/653940" target="_blank">📅 07:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653939">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggFpQ8otwjVeLLw5ULryxvQ-vrOF02EmntEjUe2KclaDyPUrUksuWw0hgapZbIVCtytBHM70O_42Lf9Lc_ipJvn5-8ZFEBs9YLfB9laJZVSQ78pvRFbu7LKx-hcv88mj6TSxOTNWCDQgzhLJSoRmGEgCo3A4FfX_tf-yl4wowFSQxmdzlzi2wTVmcldxjxIztm9luiJwQBZxO2_7vkTSlEmznfTliLl2d1FvNmr8c2A0rDUJaq7C3ijkj3OHLeaFlmQDu5zJ5HMCKojsGPOpPoVTzGfgahFyKGl_yZcOTo3Ir4ud-Y5KJvB-mWhig3h34XCv9JDRf35ZbXA1tRo5Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام آمریکایی: نهایی شدن توافق با ایران چند روز طول می‌کشد
🔹
در پی انتشار برخی گزارش‌ها در رسانه‌ها مبنی بر حصول توافق بین ایران و آمریکا، گزارش کرد که نهایی شدن یادداشت تفاهم میان ایالات متحده و ایران ممکن است چند روز دیگر به طول بیانجامد.
🔹
او دلیل این امر را فرایند طولانی کسب تأییدیه ایران برای متن توافق عنوان کرد.
🔹
بر اساس گزارش، انتظار می‌رود پس از حصول توافق نهایی همه طرف‌ها، مراسم امضای حضوری میان مقامات آمریکایی و ایرانی برگزار شود و بلافاصله پس از آن، احتمالاً دور جدیدی از مذاکرات بر سر مرحله بعدی توافق آغاز شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/akhbarefori/653939" target="_blank">📅 07:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سدهای کشور تنها ۶۷ درصد آب دارند
🔹
میزان پرشدگی سدهای مهم کشور ۶۶ درصد است اما پنج سد لار، دوستی، پانزده خرداد، بارزو و ساوه کمتر از ۱۰ درصد آب دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/akhbarefori/653938" target="_blank">📅 07:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653937">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN4BYlLdssdp0jyZa0jzFSPrUnj6_BR93OMZ9Y53chv1kxqlEHJgxvEoSExceKiGFNOgWu4y0QIY8e5SO32hjRogNb03i5Z0N2sS2r7uo8hLJxXZW5ZpfT52ebZLLX5EWhYuAg7EKvhQtYN_POJ-BdzDxgc--0FX3Msx7cHgaKmh9QC76YpAmHWdJ0lj-j7XppXkoDqdi-SFtPZZJBjXUkX3rN-NRPnza-mf5PrIVCpk_vrgYLmwS7UPBgi4_Vf6v3Zcxyw592ETMAFzSxJnvu0vj_-YAXHVaOB8_MtOYrE-urYnOI86ydYBtKgPYerptueg67U63mULVQKj8sk9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۴ خرداد ماه
۸ ذی‌الحجه ‌‌۱۴۴۷
۲۵ می ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/653937" target="_blank">📅 07:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653936">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcpPZ-rzr7DPKGe5_J7-C2onbA_0JSCP2eJnihxM4qFGcHseqUBpAS4LntVgHODodKhgEXno5JbFEgd8QuqEjie_tYkFvCmvOl78O7FP4TUZTDE4e4f9UlQva5UXEAGHCbxfXpiUi8EeGBVcqu3US-TxvDWLWJVqTsZwE-ECUJNUAqX1HMIpf3SuoQXiSq-9zJ7O_voJVVahG8s73iGEbXSNQJhuT4Aznc5fo-xN1SoDFQg_hd_mJQEwuGKrrgHupL4-yR49BxcBCyJGeYsldZ4iW7EQWUjfvhUemuSaNPFaOGsW2nD_KnvhfM7tFGBAWd0UGllMFLOaOFwadjOhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان ثبت‌نام‌های مشکوک در قرعه‌کشی خودرو، با ورود دادستانی
🔹
پس از تکرار گلایه‌های مردمی مبنی بر اختلال‌های مکرر و تکمیل‌ظرفیت برق‌آسای سامانۀ ثبت‌نام خودرو، دادستانی تهرام ضمن صدور دستور قضایی برای رفع این مشکلات، خودروسازان را مکلف به برقراری عدالت در عرضه و بازگشت به سازوکار قرعه‌کشی در صورت تداوم شرایط نابرابر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/653936" target="_blank">📅 06:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653935">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
فاکس‌نیوز مدعی «پیشرفت ۹۵ درصدی تفاهم اولیه بین ایران و آمریکا» شد
🔹
شبکه آمریکایی فاکس‌نیوز مدعی شد که تفاهم اولیه درباره حدود ۹۵ درصد مفاد یک توافق‌نامه حاصل شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/akhbarefori/653935" target="_blank">📅 05:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653934">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سردار نقدی: عملیات براندازی به عملیات تحکیم نظام تبدیل شد
🔹
مشاور عالی فرمانده کل سپاه پاسداران با بیان اینکه ملت ایران بزرگ‌ترین پیروزی‌ها را به دست آوردند گفت: با وجود تغییر مداوم راهبرد و تمرکز بر ترورها، دشمن در دستیابی به اهداف خود ناکام ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653934" target="_blank">📅 04:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653933">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
خشم شهرک‌نشینان شمال فلسطین اشغالی از رها شدن در برابر حزب‌الله
🔹
ساکنان و مسئولان محلی در شهرک «کریات شمونه» و دیگر مناطق شمال فلسطین اشغالی با ابراز خشم از عملکرد ارتش رژیم و کابیته نتانیاهو، اعلام کردند فرماندهان صهیونیست در جبهه شمال، نیروهای خود را در برابر حزب‌الله «رها کرده‌اند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653933" target="_blank">📅 04:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653931">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riRY3FxvNsNzcMlsJv_9UveZ5Vjsu8-me7brKA7pSXLK8MdWLLIOgyj5KJahchQ4hf9bx0YzqZC6NGNbNwQQE0HJyKQ0ZU97IFsSlk7OzyVmNlg15RJqVCPCXqOF8Q3Hxjp4itWK-fVCBJDYZL8-yUTUfNrpvBvT36s978CBBjbqPhLaHt81iA9jqPR5O3isjKJixDKyNJ_QzhifPrbRTMw3DDRujEYz-EpOzqHhE1f6UxNhMJ5_BOV3flA36N-u6wLJSbiquzA27wJxlK4CnLbyO-yNI_S8YHBnYgcuX-gxFiSZBJm2gbeOISQMoblyNQDdVAJ7CW1yqnaoHA5n6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: شوک عرضه ناشی از جنگ ایران، تولید در آسیا را برهم زده است
🔹
کمبود نفتا، یک ماده مشتق شده از نفت، که مستقیما ناشی از محاصره نظامی تنگه هرمز است، زنجیره‌های تامین در شرق آسیا را به شدت مختل کرده است.
🔹
ژاپن و کره جنوبی که به شدت به واردات نفتا از کشورهای حاشیه خلیج فارس (به ویژه قطر و کویت) وابسته هستند، حالا با قطع کامل صادرات از این منطقه روبرو شده‌اند.
🔹
بیش از ۸۰ درصد از خطوط سنتی تامین نفتای ژاپن به یکباره مسدود شده است. شرکت‌های بزرگ مواد غذایی مانند کالبی (تولیدکننده تنقلات) و کاگومه (تولیدکننده سس گوجه‌ فرنگی) مجبور شده‌اند طرح بسته‌ بندی محصولات خود را تغییر دهند و برای صرفه‌‌جویی در جوهر، رنگ‌ها را حذف کنند که نتیجه آن بسته‌ بندی‌هایی با طرح‌های محو و کم‌رنگ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/653931" target="_blank">📅 02:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653930">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10f1b43b4.mp4?token=uuVHimZtEVLXhstlv0mHE1416UnR0fgqn53ODh-LN3Y_U-oXwtXFsk-hg_gMArm5qoKP6afX6Z70NfXKquCC-MDJ-rfxAopxchniQVs22i5abNen-8aqm_bDOCD6XkaSz9FopkAUOy8OB_hf5uokCgxd589RktDVk94QHG9pgegbJHWhpqiUXR3T-QSJRqPUy3ctSBgO7P7cz0IxqaXj1KMVj8H0Q5TaJu189pb79j-bu23R_XmX9RPXM3Wudjw0yMHNF_YNXBUHcXjQw2mRDgqJ2HRd8269DlDCxGK28R6dTuvNwy4ksmJpbyKvUf3dDL9_D9Kq1SitDIwr3-0x-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10f1b43b4.mp4?token=uuVHimZtEVLXhstlv0mHE1416UnR0fgqn53ODh-LN3Y_U-oXwtXFsk-hg_gMArm5qoKP6afX6Z70NfXKquCC-MDJ-rfxAopxchniQVs22i5abNen-8aqm_bDOCD6XkaSz9FopkAUOy8OB_hf5uokCgxd589RktDVk94QHG9pgegbJHWhpqiUXR3T-QSJRqPUy3ctSBgO7P7cz0IxqaXj1KMVj8H0Q5TaJu189pb79j-bu23R_XmX9RPXM3Wudjw0yMHNF_YNXBUHcXjQw2mRDgqJ2HRd8269DlDCxGK28R6dTuvNwy4ksmJpbyKvUf3dDL9_D9Kq1SitDIwr3-0x-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت دکتر کلاینمن، پزشک آمریکایی و عضو ائتلاف پزشکان علیه نسل‌کشی از رفتار وحشیانه رژیم صهیونیستی با اسرای ناوگان صمود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/653930" target="_blank">📅 00:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653929">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c25a3cd81.mp4?token=doxA5ZQWCsA0Jl1EMALiSkiuczKd_xwTPVZ2zfmo-ZJBhgLcl7OcUhpEvHQdL45neIhu299icJMJHmkjZEIEzv52cX5gT2B3CuaG09C4ntV1X0cmkGiXx_leh3pTkGZwsvsYnN1XxxDRZG3WmjCSOXDTnV9nYumR9Qasdh37g1fNRV5xbgaj4b1P-yYlPNhqenHiij7xIBDTGzwxjIsdn0xmJ8_u0eV2Wso5mCQHVywo0meTT_lmy_b6sKj977CZc-jSnKsD6Ch-ns-mwsIiDe3sBEIWl00uwA58KN3qxESivmzk9oIS5cheihSY1Nmp1Cg2TVj981EU4VAy_Uq6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c25a3cd81.mp4?token=doxA5ZQWCsA0Jl1EMALiSkiuczKd_xwTPVZ2zfmo-ZJBhgLcl7OcUhpEvHQdL45neIhu299icJMJHmkjZEIEzv52cX5gT2B3CuaG09C4ntV1X0cmkGiXx_leh3pTkGZwsvsYnN1XxxDRZG3WmjCSOXDTnV9nYumR9Qasdh37g1fNRV5xbgaj4b1P-yYlPNhqenHiij7xIBDTGzwxjIsdn0xmJ8_u0eV2Wso5mCQHVywo0meTT_lmy_b6sKj977CZc-jSnKsD6Ch-ns-mwsIiDe3sBEIWl00uwA58KN3qxESivmzk9oIS5cheihSY1Nmp1Cg2TVj981EU4VAy_Uq6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، تحلیلگر مسائل راهبردی: تا پول بلوکه‌شدهٔ ایران آزاد نشود، هیچ تفاهم اولیه‌ای با آمریکا در کار نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/653929" target="_blank">📅 00:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653928">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
پست جنگ طلبانه ترامپ در فضای مجازی
🔹
رئیس‌جمهور تروریست آمریکا در ادامه مواضع ضد و نقیض خود، بار دیگر پستی جنگ‌طلبانه در فضای مجازی منتشر کرد؛ در این پست، تصویر بمب در زیر هواپیما به چشم می‌خورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/653928" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653927">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob3e99Ix6edlTt2-zpozgQRpRWfRBojZ2FGcLVFlU6UUPl96w0y3i8qLr9l_SfsTW-9-H2szP-Y-uKojhsWihIQlFS4cbvlPOFjRMaskqDiYf9MZY4im_yiBKftN6puGMP4sGFtK0x-KR68Cuoy25amCbwOaPFhmvjJGmwlRzjfyyYfw23fdUwmHE5j1h2DWOVO-aXBNtItVTXLGdtSd7vNtLXqf1QEXYhoo_xZY8djN7cWLNJpX3PdYu5fHQrwaQOW3xSuq_V3keMRJyulcLnr-sG7OX_m-n4n5eXmANayjJlmv9xzOnHFOs4vai62jcX2UqTWRqpjMV6SMRIfhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی: ایران کنترل تنگه هرمز را حفظ خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/653927" target="_blank">📅 00:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653926">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
آمریکا با انتقال اموال بلوکه شده ایران در قطر مخالفت کرد
🔹
«سید رضا صدر الحسینی»، تحلیلگر مسائل سیاسی در گفت‌وگو با شبکه المیادین: آمریکایی‌ها روز یکشنبه مانعی در برابر انتقال ۱۲ میلیارد از اموال بلوکه شده ایران در قطر از طریق مسکو به ایران ایجاد کردند.
🔹
آمریکایی‌ها تعهد خود را امروز نقض کردند و شرط گذاشتند که این اموال با پیشرفت مذاکرات با ایران منتقل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/653926" target="_blank">📅 00:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653925">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: سلاح در دست ما می‌ماند؛ ایران از جنگ سربلند خارج می‌شود
🔹
۴ متهم پرونده شهادت آرمان علی‌وردی به اعدام محکوم شدند
🔹
بازتاب روزانه جنگ علیه ایران در رسانه‌های جهان
🔹
موحدی‌آزاد: در تمام دنیا مجازات جاسوسی در شرایط جنگی سنگین است
🔹
رضایی: امروز ارتش آمریکا در مواجهه با ایران به بن‌بست رسیده است
🔹
عبور ۳۳ فروند کشتی طی شبانه روز گذشته با مجوز نیروی دریایی سپاه
🔹
ابهام در مسیر توافق؛ روایت‌سازی واشنگتن و واقعیت مذاکرات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/653925" target="_blank">📅 23:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653924">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
۲۸ عملیات حزب‌الله از بامداد امروز علیه صهیونیست‌ها
🔹
حزب‌الله طی ۲۸ عملیات خود از بامداد امروز تا به الان از هدف گرفتن محل تجمع نظامیان صهیونیست و مراکز تازه‌تأسیس فرماندهی در مناطق جنوبی لبنان و نیز مقابله با جنگنده و پهپادهای اسرائیلی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/653924" target="_blank">📅 23:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653923">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b9d939e3.mp4?token=E3mJPRhKL3XzmZYcvLEFWIhEBk1r_tVfWLon83jwYNgEddIjXpPm6hV-e9GV6JOUotzPKMWg7yg6js-jtkSNHvoBzb48TkrVJvjZdiq_ZeylArlT05cs7W0FfBs8vzpxdGIDPkbb3bUvi__sy-VA-K3PPrmH49NJkbvmMuBIF1KH_6ZdvQV8sItd5cqka4YL1kxQxxeeXKARvoexgR0eyHaBL0Eo789a94O8_0oqRU73EjPw5oD2E2vlrj90F7t4fXJ_F6WV7Qf4_YHWJmI2qqGo_shaU7J-F68Z8Qn0NdL5D5BXNjw2nz5PN_l_lgKKoR-QAXUmZIya_jRrss6eIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b9d939e3.mp4?token=E3mJPRhKL3XzmZYcvLEFWIhEBk1r_tVfWLon83jwYNgEddIjXpPm6hV-e9GV6JOUotzPKMWg7yg6js-jtkSNHvoBzb48TkrVJvjZdiq_ZeylArlT05cs7W0FfBs8vzpxdGIDPkbb3bUvi__sy-VA-K3PPrmH49NJkbvmMuBIF1KH_6ZdvQV8sItd5cqka4YL1kxQxxeeXKARvoexgR0eyHaBL0Eo789a94O8_0oqRU73EjPw5oD2E2vlrj90F7t4fXJ_F6WV7Qf4_YHWJmI2qqGo_shaU7J-F68Z8Qn0NdL5D5BXNjw2nz5PN_l_lgKKoR-QAXUmZIya_jRrss6eIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت شکست آمریکا مقابله‌ی مردم با تمام توان بود
🔹
سردار نقدی: همه نیروهای مردمی با هر سلاحی که در دست داشتند به هوابردهای آمریکایی شلیک می‌کردند. ژنرال آمریکایی در گزارشش گفته است «ما از همه طرف محاصره شده بودیم و هرکس با کوچک‌ترین سلاحی به ما شلیک می‌کرد.»
🔹
علت شکست آمریکا این بود که مردم با تمام توان مقابله کردند و ذهنیت غلطی که می‌گفت «ایرانی‌ها منتظر نجات از سوی آمریکا هستند» برای همیشه از بین رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/653923" target="_blank">📅 23:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353232745a.mp4?token=hc2bn7PJngdOK8SsNMtkZwsrvS1yDu9rvQFNz5QYmaEOhPHclTK8U5BHbws0RTYVpo1zvwbrlx241e2LrflU7S6w4EiclwvGISwZ30rueVt3JiC7vbfJfTq9VmdXpe9dIczE06kLkf89VC17B123BUwELTodAm28bYwNijE370sibzPavc8v7lHB2tZY5shL2NmMlC7VITShDi8uME7b-hU-POMjMuFfWMT_jWvcv3P6iTPtZrSsCOGjc0kwa51z5s5yJvp2K_M8dWek0ydEZXVdbjsMOSKHv5uCnuL5zv9d5bjU1hVVUSmkj3BM9y9U2AvSmJWHZhpJs4Vsl7IJyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353232745a.mp4?token=hc2bn7PJngdOK8SsNMtkZwsrvS1yDu9rvQFNz5QYmaEOhPHclTK8U5BHbws0RTYVpo1zvwbrlx241e2LrflU7S6w4EiclwvGISwZ30rueVt3JiC7vbfJfTq9VmdXpe9dIczE06kLkf89VC17B123BUwELTodAm28bYwNijE370sibzPavc8v7lHB2tZY5shL2NmMlC7VITShDi8uME7b-hU-POMjMuFfWMT_jWvcv3P6iTPtZrSsCOGjc0kwa51z5s5yJvp2K_M8dWek0ydEZXVdbjsMOSKHv5uCnuL5zv9d5bjU1hVVUSmkj3BM9y9U2AvSmJWHZhpJs4Vsl7IJyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: دشمن ۲۱۰۰ پرتابه و ۳۰۰ موشک زمین‌به‌زمین به جزیرهٔ بوموسی شلیک کرد اما رزمندگان ما بدون هیچ ضعفی ایستادگی کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653922" target="_blank">📅 23:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653921">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c1b495ff7.mp4?token=qkzbhp8fluP9seq7BWYzFsKUg5YYlSf2jZOcA087Fqzv2maWlGRxCHilUsDUYqVt73LHNSUz5jOOUvFQ_yjNVRdgUIDRiSAwopbVhon3GLkKvEo9RgHR9kBhrxNSCrGl6T91AAtMXD163DHjLqY5WGu8vHnLT-RqaPsSP_DAkowMFN9-9NM-fEGSgjBFnHqoELT_utoeDMZC6wOz5AdfFzRTbWdKtp_ojaEe0tOtVvDPuUy8qwGb2yTHO1o62-BPNZUkQ7fhjOMsaivdo2ZCrbpzYiI7_jhhEi1SBDlznp0J8qMOmpsBWpf376J_oItUIf3I74dYhX5Y_Sy8PYm4Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c1b495ff7.mp4?token=qkzbhp8fluP9seq7BWYzFsKUg5YYlSf2jZOcA087Fqzv2maWlGRxCHilUsDUYqVt73LHNSUz5jOOUvFQ_yjNVRdgUIDRiSAwopbVhon3GLkKvEo9RgHR9kBhrxNSCrGl6T91AAtMXD163DHjLqY5WGu8vHnLT-RqaPsSP_DAkowMFN9-9NM-fEGSgjBFnHqoELT_utoeDMZC6wOz5AdfFzRTbWdKtp_ojaEe0tOtVvDPuUy8qwGb2yTHO1o62-BPNZUkQ7fhjOMsaivdo2ZCrbpzYiI7_jhhEi1SBDlznp0J8qMOmpsBWpf376J_oItUIf3I74dYhX5Y_Sy8PYm4Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: ۲ هزار و ۱۰۰ پرتابه روی جزیره بوموسی ریختند و نزدیک به ۳۰۰ موشک زمین‌به‌زمین به این جزیره زدند، افراد داخل ناوهای آمریکایی تحت فشار روانی از حملات موشکی بودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653921" target="_blank">📅 23:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653920">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEuGoMgfzz5DELiHiWKAP5G9jQEhzf5xR53Spe_jU2gru5S2C4kpn4sw-ge2IC9PJVAzmj6e-r3gqsyUAEIaxpVI7TgE0GgSqbYjkJf6fRi-Lo_g3cyW6Uvkgf2U8otJ0CWUZA9aGunAfpjIxOl26XNurbA6DX38TuRjtSVtgm2Bo54G4BkU1j0peRPpnNBwdjKLIlh8_DepLWsDTA-GRrNlQrxBs3DvVKimdUDg3g_b395kjoYKfQji4wiYrstJ2OMXC_rHKiyh6eWpFc-uc6S-Lzb8A57e1BaJLyYlFQH8s7Ip_YAh-MI_m6DhJyGSSoSMEPmMUlkzV-HK--KDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیلی دور خیلی نزدیک
🔹
از شب گذشته زمزمه‌های رسانه‌ای درباره توافق ایران و آمریکا بر سر یک تفاهم‌نامه با میانجیگری چند کشور به گوش می‌رسد. اعلام محتاطانه ترامپ این گمانه‌زنی را قوت بخشید از دیشب رسانه‌های غربی و داخلی طیف گسترده‌ای از تحلیل‌ها را منتشر کرده‌اند؛ برخی آن را گامی موفق در مسیر دیپلماسی ارزیابی می‌کنند و برخی یا نقد به آن آن را فاقد تضمین‌های لازم می‌دانند. جزئیات تفاهم‌نامه هنوز به طور رسمی اعلام نشده‌است. در این فضای پیچیده آنچه روشن است، ایستادگی مردم پشت وطن و حمایت از تصمیمات مسئولان مربوطه است؛ مردمی که همواره پشتوانه محکمی برای نظام در برابر تحولات منطقه‌ای و بین‌المللی بوده‌اند.
🔹
هفتصدوپنجاه‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653920" target="_blank">📅 23:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653919">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj5oxPWnMVJsy1NCg7UH1LodIT2fxjssyyv7898UG_4_TakhiL4_sy4CYdpw65f69bx9SfJyYhuL-kVMjpDNOx1PATEyYPwh7dgfzV5lJ0limUU42QpGEqBqyaSclvsll2qDZbgP8I_onfbOuTz0GSsVsMDw20VIX6w39dlLP5RbUVKhVd38ksJ3bc-8nH_-xVhc4isqsyQDui5mHDLrcP1QDsy-twpS_4Y-jktilzzrqOZdy8aKYF75S45ZUU8YX5HP0bJSSbRufp8mW0OsSMdP2JV1ZNcLlIi30WXsVdnKU9GS_QgbNMBQsvzMWJC8xSdFUICP9zn9QlCsb4QxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پترائوس: آمریکا در مقابل ایران در وضعیت دشواری قرار دارد
🔹
فرمانده پیشین سنتکام: فکر می‌کنم ما در موقعیت دشواری هستیم.
🔹
مقامات ایران می‌دانند که رئیس‌جمهور آمریکا با انتخابات میان‌دوره‌ای روبرو است.
🔹
تشدید بیشتر تنش از سوی آمریکا، موجب خواهد شد زیرساخت‌های حیاتی در کشورهای خلیج فارس که قبلا در طول جنگ آسیب دیده‌اند، بیشتر آسیب ببینند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/akhbarefori/653919" target="_blank">📅 23:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653918">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm5Z3M6gIcxkyCNhfO92LC3dpbnOOLlVYrhjccjiD09QgSc5t1gvnM1xkoueJCQ7mUdv5aHujkn-USazt7Eo7V82akutVX1Nyoc43V38AvQBnybYmGbWnWIL9Y49phQuS5q4gQG9H5nvlA8GjMqZVd1H36AgjW5zKH_2RSDvupt44KDG8vuQHSSnEu2gKGKw4XHIuxjh1tSJhAirTo0Xid5bvSeSENSPPliornSwUQzL0QsIQjLyi14Epcnup6cA31BjcS7sBHMR720dZw-qTh-46-8iqUqfMoV6fqoLPLatuG3zHOlkYx7D0EjniNMReZPAN9xECjcpoXzvUcNC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضایی: اداره تنگه هرمز به وضعیت قبل از جنگ بازنمی‌گردد
🔹
سخنگوی کمیسیون امنیت ملی مجلس با تاکید بر اینکه اداره تنگه هرمز به وضعیت قبل از جنگ باز نخواهد گشت، تصریح کرد که این تنگه تحت مدیریت ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/akhbarefori/653918" target="_blank">📅 23:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653917">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4b4de4f2.mp4?token=nSsZk3WW71CmAY8erPCjM1kW_5LYaadCOttdAH9ZPccwAirZUJ2p9Uo7fFtNRQLPn_JeuB1fDlf3utJYYT9gWqm2LKT9PUkrIqzv011w3jQqnrol-aZot_WrWr0cY2EAImCkaf8GHoIZmawL_CCSMKvM5Uwf1w1d2Mc74c4Y-bfvcqzNrXXjcyUEcn-2ypHIRjDGBudjJ9iWoeTLVREB66zNcracqFQuzGNqam2eoUBTbATTit7c0zfVcYmfXPkeriMUQaI8rKUQg2TQqDlGVTrQMAOwQw8gN0oUXZMT4gCjIqzZyo64goK1SrFhBjA0ziO5kGIpDrm_uAYDDAduv1MvMHA1IrbUYXrJRzGT3dCQfMwbZ7z8mpfoLdRhDECUU_yiU-KMoHAw8urIfFszCrltpt8O9WA4ho7K9h026bvXZl7jBUb4-rAvbQH_tVQmfA8USqHL27gseOJNRzeJzeA5fmlBYPyrQRgF49C-hZ3iT6Ia-uR0IWYMLODu3WEnVLVAYXho6_kAGf4AEtA7x5WZi_J0VFlPSswt4ZXvoiiBfupJkYw4GrDQrNTcdQjjQRW3JLAv9p85uu9jemEPC1sabKFwHwE2ttBZlriJJXu_kaS54BLfAj-RIp3AL0FuHZfCR--PG6BX2OsUIX4mT4UG1Rdxuq4o1mNziCQ9DCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4b4de4f2.mp4?token=nSsZk3WW71CmAY8erPCjM1kW_5LYaadCOttdAH9ZPccwAirZUJ2p9Uo7fFtNRQLPn_JeuB1fDlf3utJYYT9gWqm2LKT9PUkrIqzv011w3jQqnrol-aZot_WrWr0cY2EAImCkaf8GHoIZmawL_CCSMKvM5Uwf1w1d2Mc74c4Y-bfvcqzNrXXjcyUEcn-2ypHIRjDGBudjJ9iWoeTLVREB66zNcracqFQuzGNqam2eoUBTbATTit7c0zfVcYmfXPkeriMUQaI8rKUQg2TQqDlGVTrQMAOwQw8gN0oUXZMT4gCjIqzZyo64goK1SrFhBjA0ziO5kGIpDrm_uAYDDAduv1MvMHA1IrbUYXrJRzGT3dCQfMwbZ7z8mpfoLdRhDECUU_yiU-KMoHAw8urIfFszCrltpt8O9WA4ho7K9h026bvXZl7jBUb4-rAvbQH_tVQmfA8USqHL27gseOJNRzeJzeA5fmlBYPyrQRgF49C-hZ3iT6Ia-uR0IWYMLODu3WEnVLVAYXho6_kAGf4AEtA7x5WZi_J0VFlPSswt4ZXvoiiBfupJkYw4GrDQrNTcdQjjQRW3JLAv9p85uu9jemEPC1sabKFwHwE2ttBZlriJJXu_kaS54BLfAj-RIp3AL0FuHZfCR--PG6BX2OsUIX4mT4UG1Rdxuq4o1mNziCQ9DCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: نمی‌توانیم از خون رهبر شهید انقلاب بگذریم/ حتما انتقام خون رهبر انقلاب را می‌گیریم و نمی‌توانیم در خصوص این موضوع حساب و کتاب کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/653917" target="_blank">📅 23:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653916">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بودجه کالابرگ برای همه مردم ۹۶۰ هزار میلیارد تومان اعلام شد
نادرقلی ابراهیمی، عضو کمیسیون محیط زیست مجلس در
#گفتگو
با خبرفوری:
🔹
در قانون برنامه و بودجه ۱۴۰۵ حدود ۹۶۰ همت برای کالابرگ پیش‌بینی کردیم. باتوجه به تغییرات قیمتی باید رقم کالابرگ تغییر پیدا کند.
🔹
در بحث کالابرگ با یازده قلم کالای اساسی نیاز کیلو کالری روزانه هر فرد به میزان ۲۱۰۰ کالری تامین می‌شود، اما متاسفانه حتی آب آشامیدنی و نوشابه را هم در کالابرگ آورده‌اند.
🔹
در سند امنیت غذایی یازده قلم برای کالابرگ شامل تخم مرغ، برنج، شیر، گوشت قرمز، گوشت سفید و ...است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/653916" target="_blank">📅 23:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653915">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTR4AQAbM5PZZMfxO3-CU_MCbsU1AIZ1r8SeSdfBeSGG8o_uXX24iyt-aKMKsy3PXQdQgkABSI91mXyRx33NXMR8XKKWqxXFFBLWhH2F67oPw-h7qgzaed-_lEOKp-usRJ2R7jE8-f_DSB4rQ0Tp2hFTuvxz4dNQ-v94YKwRZBAIyCP1GuzH21MqMnxiPwDX32Jc0JLPlnOb3dR_ERrc91MsmTvSFjP3oXNsPC0ipDkl8KffrgnWGNuKrqrYe88T7d60iQCl2q1pG4oyOMYVTpCUayDEtLNUqSy3r7n6myS6NIEt7txr84FQheV0QO7yHEQhgNhJusjFBUrkFf6BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوشحالی پسر ترامپ از توافق با ایران/ ترامپ جونیور: منتقدان تا حمله زمینی راضی نمی‌شوند
دونالد ترامپ جونیور با انتشار پستی در ایکس، از توافق هسته‌ای پدرش با ایران دفاع کرد و نوشت:
🔹
«این یک پیروزی بزرگ برای آمریکاست. ما باید افرادی را نادیده بگیریم که تا زمانی که یک حمله زمینی به ایران نشود، راضی نخواهند شد. پدرم قول داد ایران را از داشتن سلاح هسته‌ای باز دارد و این دقیقاً همان چیزی است که او به دست میآورد!!!»/خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/akhbarefori/653915" target="_blank">📅 23:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653914">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a88e17fd9.mp4?token=knG0gqTnkv7GJirp9G28mPQRtvVT9NCI5eh7rUPJiX_XXRHRxX6ZhY3BakUOJcyPxhRP5jKewHpZhFpsQxuZ3-Pkz0sX9XCNASjz_PEinWj228ElLBaSmC8DDwj9SPZFVnDGBkRkq0521f2twd0aKi8gdJcCb1FkUcycCZ0ipsXVCT4IoHwOSba_Xcmwu0CuteqhryOhEwrNsQfTtWnjQmb7CMY4bYrzVJy-ZlZtSc0q-8eTYohvL9lki1BQajWsFTHV4dXsTzI4Aezqq1oRSn4Q_oPXGT3-xukvAnYvfp56fS6Kotp8bevmpnHk-hrAlaYl1S0mei7f9rVLrp_EEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a88e17fd9.mp4?token=knG0gqTnkv7GJirp9G28mPQRtvVT9NCI5eh7rUPJiX_XXRHRxX6ZhY3BakUOJcyPxhRP5jKewHpZhFpsQxuZ3-Pkz0sX9XCNASjz_PEinWj228ElLBaSmC8DDwj9SPZFVnDGBkRkq0521f2twd0aKi8gdJcCb1FkUcycCZ0ipsXVCT4IoHwOSba_Xcmwu0CuteqhryOhEwrNsQfTtWnjQmb7CMY4bYrzVJy-ZlZtSc0q-8eTYohvL9lki1BQajWsFTHV4dXsTzI4Aezqq1oRSn4Q_oPXGT3-xukvAnYvfp56fS6Kotp8bevmpnHk-hrAlaYl1S0mei7f9rVLrp_EEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: ترامپ نمی‌داند خارک اصلا نفت ندارد و مرکز پمپاژ نفت به کشتی‌هاست
🔹
تمام پایگاه‌های نظامی در خارک را بمباران کردند و بطور دائمی بالای سر خارک جنگنده پرواز می‌کرد.
🔹
از ۲۸ اسفند تا ۳ فروردین بر روی راهبرد نفت بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/653914" target="_blank">📅 23:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653913">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3869eef77.mp4?token=Rvtp6XlHKGbXotZ9e_v_c5zKngfWkG4vOrDyRqHL6IstpIy8P_H9m7BahSiZgIGm6-v3fDsrXqD_JZaO8MCmRl7eRx9MKdj0mmIIsZ__REfW60trtB_8SGZbSw7Adkw8GpCmJIsn6J7YeiJv17u-O7yuODCpuxvmFLf_DUNBZV-_PpJGCqhi4zPQIT2rFUrdtfHuB3Cxnsou8LNiORXVLujHf3MZsF2cRrvML6SVkouXT_bJYlbEI7j_yPcF7B5iwsi7Xe3jB3iMFEbzTt96xjfMFv8SiuKzD2Ly19CscQintlmaKpeazjdZNvHABm-rPGCC0coq8gHZYwhnLEQWrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3869eef77.mp4?token=Rvtp6XlHKGbXotZ9e_v_c5zKngfWkG4vOrDyRqHL6IstpIy8P_H9m7BahSiZgIGm6-v3fDsrXqD_JZaO8MCmRl7eRx9MKdj0mmIIsZ__REfW60trtB_8SGZbSw7Adkw8GpCmJIsn6J7YeiJv17u-O7yuODCpuxvmFLf_DUNBZV-_PpJGCqhi4zPQIT2rFUrdtfHuB3Cxnsou8LNiORXVLujHf3MZsF2cRrvML6SVkouXT_bJYlbEI7j_yPcF7B5iwsi7Xe3jB3iMFEbzTt96xjfMFv8SiuKzD2Ly19CscQintlmaKpeazjdZNvHABm-rPGCC0coq8gHZYwhnLEQWrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: از ۲۵ اسفند تا اواخر سال بر روی بحث ترورها تمرکز کردند که شکست خوردند
🔹
در ترورهای هوایی کم‌تجربه بودیم.
🔹
نتوانستند برخی از شخصیت‌های مهم را ترور کنند. مثلا اقدام کردند برای ترور فرمانده سپاه اما شکست خوردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/akhbarefori/653913" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653912">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
دفاع رئیس مجلس نمایندگان آمریکا از توافق ترامپ با ایران
🔹
جانسون، رئیس مجلس نمایندگان آمریکا از حزب جمهوری‌خواه، با ترامپ گفتگو کرده و او را «مصمم مانند روز اول» توصیف کرد. او قول داد که دولت مسئله هسته‌ای را حل کرده و تنگه را بازگشایی خواهد کرد و پیش‌بینی کرد این اقدام باعث تثبیت بازارهای جهانی و کاهش قیمت بنزین در داخل شود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/akhbarefori/653912" target="_blank">📅 22:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653911">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bf900486.mp4?token=GZ1c46LUXHe6uLGbAsn2P1qxGeTmdNhFdH5dQHJ30mIKcQK1ay5yx-DUuB7qaJhApiMyWejCK8mcLxaCuudN1F92NofvLILQHccvkqJOgL3HafatdLeheoiOAvg8N6ZnC-sZqTG6UZ10QR5E82NYcjdpOwZDWBRCxp_R10E_psecE1F_15LOIVdcAAkerlagnRTlYfbogmHyMIhE4JcGep_8yq4g8mlM7vgz7-aX9XgTdsLuhQ9Yw4qZFjhZx_rwV7YQ4Mrdfim594tQLAyWWY3oGkHGV6rvSXaZbg2uJqWOy0DolzYIYbCfQLcFcuul240gPRUUZSuqcIqiVgA09DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bf900486.mp4?token=GZ1c46LUXHe6uLGbAsn2P1qxGeTmdNhFdH5dQHJ30mIKcQK1ay5yx-DUuB7qaJhApiMyWejCK8mcLxaCuudN1F92NofvLILQHccvkqJOgL3HafatdLeheoiOAvg8N6ZnC-sZqTG6UZ10QR5E82NYcjdpOwZDWBRCxp_R10E_psecE1F_15LOIVdcAAkerlagnRTlYfbogmHyMIhE4JcGep_8yq4g8mlM7vgz7-aX9XgTdsLuhQ9Yw4qZFjhZx_rwV7YQ4Mrdfim594tQLAyWWY3oGkHGV6rvSXaZbg2uJqWOy0DolzYIYbCfQLcFcuul240gPRUUZSuqcIqiVgA09DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: از روز ۱۷ اسفند دشمن اقدام به بمباران سنگین نیروی دریایی ارتش و سپاه کرد
🔹
با پدافندهای غیرعامل نیروی دریایی پیش‌بینی شده خیلی از امکانات خود را نگه داشتند.
🔹
۴ ناو امریکایی دچار درگیری‌های داخلی شدند که به اسم آتش‌سوزی وضعیت آن را رد کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653911" target="_blank">📅 22:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653910">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDgnRIo8Hy23_noQvTmgFmbOg-sektAR5avk0K0QRLC-uPyGipkjINA05yMMGB6_kD8Zu6OxvRoY5ydpGJtXpFlqmXVt6f3mmM-hZxaUjr3gUCHt-S58QoQtU6t8ZsUNQ-zAckSbPYCViguMr4jZFDsC6ZJQfRgu-gapaQuxKIIBePvycWx229BRo7UVntGKnTDg3VmKyU5fTWYE_5gss7srNEq-vKHc3BWtokPG7-pTrKInzLcfJ5PzBR5uFEtkXHs_GxrHWlW930l7l6Br_IuV5OeFDKD59SI_97DFoaAaQ-oQ13HL7LI2V4zLPUsk8_JBEipKjlgWxbi5cW0V9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا جنگ افروزترین کشور ۵۰ سال اخیر
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/akhbarefori/653910" target="_blank">📅 22:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653909">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">روايت جانسوز پدر زينب، دانش آموز مينابى:
" اين لباس هاى سوخته تنها باقيمونده از زينب منه"
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/653909" target="_blank">📅 22:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653908">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnJIn_HVYB6mAhScr5UD783XVO6GYq8S3_Ng-53coGJju51UoNhaN-EzxDcZL5sELpL948rt2VJXixkJIofnDOEF7-LEhTO9Niz69l6gpiSOi-e8w42oI9LbiI9peWjLm8IGrbucOou3rlZK1bKtdLK_xRcDMaNxgMZ2QwxDJhYlkAMqG4KMEZY2XlzjE9lN2JwntHD5txwMKAKOGwmS8rSUlTPmryq1QJ8mZJvhbpMZ9IQUs2NyBTd83Zp9tpbvdSaccT30_RKbP07SCjX1xgdxyACUx-kKl6w2ZAVwnxgUcZdZc1vjOxfMroNdM3Ce-i9V_5llbp_YN0Wtxn5_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیل: ترامپ با فشار فزاینده‌ای مواجه است که به هر شکل ممکن تنگه هرمز باز شود
🔹
ترامپ در جبهه‌های متعدد با فشار فزاینده‌ای برای اقدام جهت بازگشایی تنگه هرمز، مواجه است، زیرا مردم آمریکا با بالاترین قیمت بنزین در نزدیک به چهار سال گذشته روبه‌رو هستند.
🔹
نظرسنجی‌ها به وضوح بد هستند. قیمت‌های انرژی این هفته افزایش یافته است. واکنش نامطلوب بازار سهام و اوراق قرضه به وضعیت موجود هم شروع شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/akhbarefori/653908" target="_blank">📅 22:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653900">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1MDIQ5t9CMGBU7BeIzkkpDnHLRQDKkczckgDiHbX6LUXPnXgNrldxeyIK_nsHoH4oVRR3ctdMRfZhMT5d2bZY5WpZTfbThWjc4BvYK0uQ1hvUkPDG7PiGv57b3gUdzGl1ZAuGinxpRIGUlmNiPvbB9RMjv4_Xs7WxLFaUtG1PrclUhFvpcuAI38a9P2JUwvgjeGH1my86REFjO88CDlhsuUf3plYbTTlF48EleIjdYpa_n0TyJHpyL6FT0vEwAJe1SC1y7CykROsiHMkLYC69V-i4IiLqO6E-p2N1mEDJz26YLfp9ZqrtsktejurYUFB-amBiB9kKnNaWrxeLS89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XM2GSXbQCldwRFG3YULovktZ8NY9mhs1Vb8WJKPjXnKla_No7E4ADGhq5FtxGNMI8AHEYfcakuTeL-PnFF4Vqp-v78opaSHsKKNugQhOb1yMad6aHPIfvS76HaHzP7N5wOGV8rf6fIN8lqdmzyR5OLSKi5caNE__PxNopSwfKfO2T1hwZq2sPG1HyHTmW4SM1JTnKSkdtVyybx29_Kl9ILHAOEsCLQeUFVkYJ6vLAXE8TILpAqwVk0eqdbHM6eOk8LgMzZrH2y03L8g6PbFS5E4d1r5btf2rp-4TNsi9FIIqZWZ6JxSEsGdtjAAZg5GxQ6zGE009YmdGKj5zX8Jbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRDLgVJKQ__OJMtGeoHjK1OJsjW2deans3wtX7ptxdg3htZWxMPv310Wnp5W7DCk7ZVrPMSzDDOY6-faLBMCFZxJzqD8LpD0i2EmzlAZZg6KmEFsjVFBxFomnQDOVHsAT7R-Ox0EOx0NkDxuYJEcFxOkvwORaVdiDTx18BY0WeKUH3k2fL1kJScq8uIojSQLljpq0vzvHP4fSC6K_yUyZLFoZ0dUrrtqm22dNTqrEuk4iH9CJ3-T11vZzrdmf-Byhi0wk5iOVBFgeZTdj36SlO9pXRqfMeyxfVW7W-64f7Og6uHMInDAkBgwMMX1QRjvkNxOT3GorGFMA5QSQNiF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkLBhmEolDY5zDdxpn2186lr1PD5jPUkRnpr3ECjb3n_f0MimHU-YB3tCLF8AHQP4wWv8rMC6GRSfxOT3dYX8itXHT9df6_0nLQj5W48Fp1MYBsfGkj-DWytSZnGho2zMun3FmB0LmM4YBERcD8JPemwJ0mjPldhuZStxfiSwc6YVdK-1xde_XIXrzetAMbV38Pb3fTX85i_Noje-uqqk7-laebYnyblAayz12rah-9ArRTmC6pLUiblvPNPRwllaKJBg3wTGyxRFJ42HjuP3OBXW_xVDSlghMvcuYxNt9NDr6qx_qTpdd4SBZRux-B9OrVfCTTzwP8lJleXxAu1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwkO14wGMlcH8IdDPVO1EWou_gxWONCgR3ywfw_dX_W9IWw4Y2Vo9Cluob5Hq2C070QyQtZ8e-NFp3B9dBWQqvW_ZMH9W7VFKbUWGxt-_lFy4f509WIR5z7CPX-dVXh8W1X9uqU_XpOHg7mW7GsrysMu75U7r5KY-hqf1tNTGXmnUlEsJ94vKoEHNui4MoapVadDerVpjLULI3YRYrGzxwA6flm61JUQ632DZOdiv29WwnutWAFkZFYA49os7tYQOyRuqRVlFR-i3Hgxorob2zDjCMf_4JnQTvIDtUaFE1X4F16gTvhuaKMT4sxqkklQ_c5_nV2QHfPW4O_AhiR9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kItW6ab2SohMmedw2--q0XMulUskzuLusv3Qna0EyZj_2SH7bfGC4nnhmfvH6ZrOk1_Fe9nZczlXFlOP_A53-q4fE6wTpCyWRtZJYy6wO5jSkE2sf9qqQZwj7woolN_4Y_FXkw71OvMgLNzgsE9CqgsNZ1oXxjNZddLosou80NqOt_8qvCNsJ-5d-e1g02G5HiNpBSUbMOlMqY-9AX453S3dAp0Tcx-1vNQWa_YnMyhx3IIYdOF5FN_ANtD-y0Na_Ru810uAknH7KK6vKaVtlFkvtNg6ZjI_CSsD2FgxbgMDuTfgIDT8abC-B4z430ep6Vlj_yP7NWScax5-iRE7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBTCbV8zo9v-2qZIfXhE0q9WAHCyQaT4yZlXlWkhz0xlFdporVHWNi6m41eATwfxKhBbmnDahr5sp98CkiNRrV70XJ9rje30zgXHsgbwf-_Sh8ssb0CRwkrwrQ-F3cj0GO6QAExYqIsT1is9tsHGnWGHbaGOivuTHq8nZKOmDNFv4NjKECJAWZ7oerpROO2f9W8rFRpvH30ZSAXW1Cyhl_JXsC43vDyqeJXbzd7Ilb_bXwqweG9Heq5JCJppb8I7YJ9N6K-aX8edKkSqlqgG4uU6NWh8KTzjxoXUNKaKCvSmnm-91x6sHg3bXTDPxGT1aRfIX4BaFgqmHd9pNAzRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oY_91s3ALaA_Sg5Z9Yar5Iqp08W9qXd3soNDz8plIb6tuTDnplf8s_HuuKirM-BkaAPNMbUV7DR5AYuN575vELVMXpmrHlKPeGw9AJCWVnxFUyP3ZFDiNrri1pGnck01L1bdsuagENWQIFqj8uVhXXbbc-88cMdCZC3iyYTOcnk0b-Y6p9_W9quQlllPn202LxEUw1maEbPpoW-L2N0eeCgBEZj8OcEb9fwKoMMhCsWFjfrZmXdOqTswK7IeHcRilNvWu-MTjhJOnuhq6vMRzd9iC6XKPCbrByKPPB1MMx4VJN-RWiWw7yvDXzdxroFTaKc8vsfjf6-CQUsiQSgboA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت سهم‌های کوچکِ ماندگار
💫
✨
این روزها،
#همدلی
فقط یک واژه نیست؛
حضور مردمی‌ست که کنار
#هیات_قرار
ایستاده‌اند تا هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی، قدمی برای حمایت از خانواده‌های ایرانی و خانواده‌های حائز صلاحیت بردارند.
همدلی شما، ادامه‌دهنده این راه خیر است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/akhbarefori/653900" target="_blank">📅 22:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653899">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu39Xq_atCNK93SNrCmfcin2L-nzoCnU6jITH23f4NNhYwxF8uPkeWf37Igje3-xfWLrsL_NOViVDm-AEBVDyMUgFl6rGjNHHoZR4-v_tS4xOiYJzmL0JDwiVTDmgDiQrSNXr0TOIz5XRywoCexkON1k54aP3W3qNMmvBb9stTeY_tqHYzvw-wtG57juizcMGTCHLd8x01WwPnvSBJSMSS-rJl_yZV-yq7cEUbsXVgcC7NiGUdWElRbepHLNGcmEiSVo8lMKIzSsgsUmOyKCnZG9x3iC2PY-lUyRm1F4O1W0Mgy5zs-K-djQGXaY2N82DNNWrn8FI0O7Oe3AofXTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: اگر توافقی شود، دقیقاً برعکس برجام خواهد بود
🔹
دونالد ترامپ با انتشار پیامی در تروث‌سوشال بار دیگر به توافق هسته‌ای پیشین ایران و آمریکا، برجام، حمله کرد و مدعی شد که اگر مذاکرات کنونی نتیجه دهد، توافقی «دقیقاً برعکس» برجام به‌دست خواهد آمد.
🔹
وی با انتقاد از رئیس‌جمهور اسبق آمریکا ادعا کرد: «اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد.»
🔹
این در حالی است که آژانس بین‌المللی انرژی اتمی و حتی نهاد‌های اطلاعاتی آمریکا تأکید کرده‌اند که ایران در تلاش برای تولید سلاح هسته‌ای نبوده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/653899" target="_blank">📅 22:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653898">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a41c67cb6.mp4?token=p1yQL7phinI3VrEriuAVdzQQ5i3mveb7Ymf_YWW0i6pWy1d6e8WlYBqJojF6QuInUIdCgT0tP7pc9Tej3HWjvgb6kz-_FPSMupjwd5289htoAgfHmwRO7-CCIZEVnDgt8osE7p2tjEYxxV8eORP4yeD4b8lQa8V-KI3JFaOGruQ1_JtjDzeY01bsaw5eDtiQnzSXcLSyYEyPblSwLBtjy5Q9samW59Ukv9pQBCLwtQr_XgG2Tf7Cfslq6h-HbhXpL6DdZ5lsesjUb6r_pKasIaJVRPgEy6xUOS25J16bFfRJvu0rXTyX5yNpJg3eLrPcTLEG9n15Cc19BLVQi0BHLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a41c67cb6.mp4?token=p1yQL7phinI3VrEriuAVdzQQ5i3mveb7Ymf_YWW0i6pWy1d6e8WlYBqJojF6QuInUIdCgT0tP7pc9Tej3HWjvgb6kz-_FPSMupjwd5289htoAgfHmwRO7-CCIZEVnDgt8osE7p2tjEYxxV8eORP4yeD4b8lQa8V-KI3JFaOGruQ1_JtjDzeY01bsaw5eDtiQnzSXcLSyYEyPblSwLBtjy5Q9samW59Ukv9pQBCLwtQr_XgG2Tf7Cfslq6h-HbhXpL6DdZ5lsesjUb6r_pKasIaJVRPgEy6xUOS25J16bFfRJvu0rXTyX5yNpJg3eLrPcTLEG9n15Cc19BLVQi0BHLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: ۲۸۲ نقطه حساس دشمن منهدم شده است و روزانه یک آمبولانس هوایی ۴۰ تخته‌ از امارات و یک ۱۰ تخته از کویت هر روز در کل دوران جنگ مجروحان بدحال را منتقل می‌کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/653898" target="_blank">📅 22:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653897">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMhUR7Jg2g0l2J-QZwkiPYXnxWetJDAjw2Fv4LAtPCWQh9Iw7LvkA_O8REGu0cTDcRtlxTqRYuidNh4xaWiR00cO-0JMYYRJCezMu8fpTzmj_FQYSxCaxfjcdzEJeuOJG4LhtTC8KtKcTdBAjzAecTG9GkKMHfCTO83M6i0Moi3QfRoj3J9MazAWOYJt7jHMewAa88lwNDCaHaC0jIC2jXA7spi29ZoswhVxDTYr7yzM_PasY6uSdUOT6E8Fx38ftlswAU89YatOBIKeY8dQ3rPLr2NNTZ_1opmfBjt2ZY5ZrMiYvm2P8P0AHiMgmEcBQNLJ4-AZJAvI27tWMRIHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان کل کشور: در تمام دنیا مجازات جاسوسی به‌ویژه در شرایط جنگی سنگین است
🔹
آمریکا، اسرائیل و هم‌پیمانانشان با تشدید دشمنی‌های خود زمینه‌ساز رخ دادن جنگ تحمیلی دوم، کودتای دی ماه سال گذشته و جنگ تحمیلی سوم شدند.
🔹
این ایرانی اسلامی است که به پشتوانه مردم، سربلند و با اقتدار در برابر تمامی این حملات، جانانه مقاومت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/653897" target="_blank">📅 22:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653896">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 56</div>
</div>
<a href="https://t.me/akhbarefori/653896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وششم
رائفی‌پور:
🔹
0:11:25 رسالت حضرت علی(ع) چه بود؟
🔹
0:30:00 چگونگی مسموم کردن حضرت محمد(ص)
🔹
0:43:20 دستور الهی در اطاعت نزدیکان پیامبر از حضرت علی(ع)
🔹
0:59:20 منتخب شدن هارون و فرزندانش توسط خداوند
🔹
1:04:40 دروغ کلید تمام گناهان است
🔹
1:18:00 عظمت و صبر حضرت علی (ع)
🔹
1:20:40 اهمیت انتخاب اسامی فرزندان
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/653896" target="_blank">📅 22:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653895">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
معرفی قهرمانان کشتی فرنگی توسط حسن رنگرز سرمربی تیم ملی و حمایت‌های مردم/
تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/akhbarefori/653895" target="_blank">📅 22:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653894">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تلخ‌ترین اتفاق این‌ روزهای موسیقی ایران
🔹
در روزها و ماه‌هایی که تب و تاب خبرهای جنگی بر همه چیز سایه افکنده بود، موسیقی ایران تلخ و شیرین‌های ماندگاری را تجربه کرد.
🔹
برای شما کدام‌شان ماندگار بود؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/653894" target="_blank">📅 22:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653893">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCxSDl4vEDy3E_QgEei4Xg0ycydkA7HLqRqseVJhTvMyfKKmRHN-pjtoFCa9Md8wCyAEwdsttL3w19K9hUEOJppacsRs3bsgVx9-CvsxTV30s8MdeboR0qCCIpwmd3YIaWWO8HHE2yVCLdy6ewrxoV-60EQ3qHCp-ufGAoQme0vho_oQiKtNscEN5244-FDoCS5PpUSL1JwNj2XmVakDKvILqrUNo4GdbWPVODviSMTN3zMdegfSDzlucKO8IMetxVxqcRJ_4AM6IZsf7M2mUx_fcy2vSVuShtYaIwCKwP5MkpbuvquK7_JLvaDApg7CfbAwJj0cZacXhGYP0Z01sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
تهران را «با هم می‌سازیم»
سخنگوی شهرداری تهران با اشاره به آغاز پروژه بازسازی منازل آسیب‌دیده تهران توسط شهرداری و افزایش درخواست‌های مردمی برای مشارکت در این پروژه از رونمایی سامانه «با هم می‌سازیم» خبر داد.
مردم می‌توانند از طریق مراجعه به آدرس
BAHAMTEHRAN.IR
یا ارسال عدد ۱ به سرشماره ۳۰۰۰۱۱۴۱۱۱ در فرآیند بازسازی تهران کمک کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/akhbarefori/653893" target="_blank">📅 22:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653892">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
«خفه شو بچه»؛ جنگ لفظی سناتور کروز با مشاور ترامپ بر سر توافق ایران
نیوزمکس:
🔹
ماجرا از آنجا آغاز شد که کروز توافق احتمالی با ایران را «اشتباهی فاجعه‌بار» خواند و هشدار داد تهران نباید میلیاردها دلار تسهیلات تحریمی دریافت کند و همزمان راه غنی‌سازی را داشته باشد.
🔹
الکس بروزویتز، مشاور ترامپ، در پاسخ نوشت: «هیچکس از تو نپرسیده داداش.» کروز بلافاصله واکنش نشان داد: «خفه شو بچه. بزرگترها حرف می‌زنند. من داداش تو نیستم.»/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653892" target="_blank">📅 21:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653891">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93edb5d38.mp4?token=FL2yCo1x7Oto0oSpB4-sj7iljt9af-qamjIQhUdlICGZO337AYgfMDlg57JWv9msds4h2YtX4EjBcdXG_vdTfxDnRGSQWJzWS0n7l1NpsDwNUVw7sPGjErJEm5qGgNWxlbN6oenoQCKp2bKcf7Yn8E6idnw8nu7bSfKAI-xZkdB6Rqa0WanWaI5CElMp0HXoy2m7iPKfgKP2llt7IEZC-MdCVg1iHZABIzx6lrek2Ga8DP7dozdkMjRKW3JW46A7TAdJzwLHYHLOm0v5H6BYSwIxSXkiistj_vv7Ff3ACE7x2B0nBla8Xteokk64wS8sgAkMLakGzY7L4IRkywIU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93edb5d38.mp4?token=FL2yCo1x7Oto0oSpB4-sj7iljt9af-qamjIQhUdlICGZO337AYgfMDlg57JWv9msds4h2YtX4EjBcdXG_vdTfxDnRGSQWJzWS0n7l1NpsDwNUVw7sPGjErJEm5qGgNWxlbN6oenoQCKp2bKcf7Yn8E6idnw8nu7bSfKAI-xZkdB6Rqa0WanWaI5CElMp0HXoy2m7iPKfgKP2llt7IEZC-MdCVg1iHZABIzx6lrek2Ga8DP7dozdkMjRKW3JW46A7TAdJzwLHYHLOm0v5H6BYSwIxSXkiistj_vv7Ff3ACE7x2B0nBla8Xteokk64wS8sgAkMLakGzY7L4IRkywIU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر عابدینی، معاون سیاسی رسانه ملی: در یکی از سرخط‌های خبری در خبر ۲۰:۳۰ و ۲۱ به موضوع صرفه‌جویی می‌پردازیم، چراکه کشور در حال جنگ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653891" target="_blank">📅 21:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653889">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
الجزیره: ۲ چالش در مذاکرات ایران و آمریکا وجود دارد
🔹
اولین اختلاف دربارۀ لبنان است؛ آمریکا خواستار آن است که نوشته شود اسرائیل می‌تواند «درصورت وجود تهدید» اقدام کند، اما ایرانی‌ها این متن را رد کرده‌اند.
🔹
درباره دارایی‌های مسدود شده، ایران خواستار آن است که در چارچوب همین تفاهم‌نامه، دارایی‌ها آزاد شوند اما آمریکا اصرار دارد که این اتفاق در یک توافق نهایی رخ دهد.
🔹
انتشار روایت رسانه‌های خارجی به منظور اطلاع مخاطبان است و به معنای تایید ادعای آنها نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653889" target="_blank">📅 21:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653888">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
طلا گران می‌شود یا ارزان؟
کشتی آرای، عضو کمیسیون تخصصی طلا و جواهر اتاق اصناف در
#گفتگو
با خبرفوری:
🔹
بازار جهانی طلا در روزهای شنبه و یکشنبه تعطیل بوده و قیمت جهانی طلا تغییری نداشته است. در بازار داخلی قیمت سکه حدود ۸ میلیون‌ تومان و طلای ۱۸ عیار حدود ۱ میلیون‌ تومان با کاهش همراه بود که به علت کاهش قیمت‌ ارز می‌باشد.
🔹
قیمت‌ ارز با توجه به نشانه‌های صلح و روند مثبت مذاکرات، مقداری واکنش مثبت نشان داده که باعث شده قیمت ارز با کاهش همراه باشد. باتوجه به کاهش قیمت ارز، تقاضا نیز با کاهش همراه بوده.
🔹
روند بازار بستگی به مذاکرات دارد اما غیرقابل پیش‌بینی است. طبیعتا اگر روند به طرف صلح باشد، بازار هم واکنش مثبت دارد.
🔹
باید در نظر گرفت در ماه پیش‌رو، هم حجاج می‌آیند و هم قبل از محرم است و خیلی از خانواده‌ها مراسم دارند و بازار طلا رونق دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653888" target="_blank">📅 21:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653887">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4db43f7f.mp4?token=Iwmt9w5qSUqT3xwwKkQ7KOIjgKkhG8FNimvyz6dOqCesZPFMO8FCXH1-UVyN8gBLKNiNEmWBnhFD0sq3PPna6YH37AQ_l2CHnICNhf3M-0uWBgTCqm5P-OY48voyFkIXMUqYIfWmzY7Amf1IGPfRsUrxIjjEpkJv9V7vZXhJA8c-3KafRKk40HaVAeaGFB-4GxQhtp_3L6NvzALBpiVYYZkrLBMGIFW-I4UoIMAy6My5X6QzKScHt7eE4VijXcnskNrOKQeh5_LoBuqZmSsA5mNRYnAXzAFPz_wzKFoDYMQB5L8KpAlQx_hG4K5RFRsxgEsDBGn6Z-8eqiQyTbYjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4db43f7f.mp4?token=Iwmt9w5qSUqT3xwwKkQ7KOIjgKkhG8FNimvyz6dOqCesZPFMO8FCXH1-UVyN8gBLKNiNEmWBnhFD0sq3PPna6YH37AQ_l2CHnICNhf3M-0uWBgTCqm5P-OY48voyFkIXMUqYIfWmzY7Amf1IGPfRsUrxIjjEpkJv9V7vZXhJA8c-3KafRKk40HaVAeaGFB-4GxQhtp_3L6NvzALBpiVYYZkrLBMGIFW-I4UoIMAy6My5X6QzKScHt7eE4VijXcnskNrOKQeh5_LoBuqZmSsA5mNRYnAXzAFPz_wzKFoDYMQB5L8KpAlQx_hG4K5RFRsxgEsDBGn6Z-8eqiQyTbYjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعدام، عاقبت خائنان به وطن است
🔹
مجتبی کیان، که با لودادن محل ساخت قطعات لانچر موشک‌ها به دشمن صهیونیستی خوش‌خدمتی می‌کرد، به سزای اعمالش رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/akhbarefori/653887" target="_blank">📅 21:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653886">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7722c4f35.mp4?token=vHMdLd6Q3FtW8rHUapOPeAALNO7YwkKaV6n6JmfxDXd1GPzwVgroDQ2_CGtFaKZ05l8qchG90glRDfqd4cFsoZJ4ln6Fz3diUIVSMNiFBmUTC9MvebKwotqndu_ewAxsoG7mFfBWgjViaqHXBm3xccQj5DHMrclSsiXAM4ZJ2V9CM9rJN5qmpRSFDI611O4BD_-ErGYaMYO0G0CHAYMCaWGpAYjkXE6A7IVTUwUbQxemj_qnQKSYwpNfz5NLNglOdGjHyvRnFWbCcyROpy6b5npqz0cEdlJ6lKISicEwdpfpTl1koG6h5Md2Of00PXxw37kDtETAmi3ySzlDfc85Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7722c4f35.mp4?token=vHMdLd6Q3FtW8rHUapOPeAALNO7YwkKaV6n6JmfxDXd1GPzwVgroDQ2_CGtFaKZ05l8qchG90glRDfqd4cFsoZJ4ln6Fz3diUIVSMNiFBmUTC9MvebKwotqndu_ewAxsoG7mFfBWgjViaqHXBm3xccQj5DHMrclSsiXAM4ZJ2V9CM9rJN5qmpRSFDI611O4BD_-ErGYaMYO0G0CHAYMCaWGpAYjkXE6A7IVTUwUbQxemj_qnQKSYwpNfz5NLNglOdGjHyvRnFWbCcyROpy6b5npqz0cEdlJ6lKISicEwdpfpTl1koG6h5Md2Of00PXxw37kDtETAmi3ySzlDfc85Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتظامی: یک عده فکر می‌کردند آمریکا به هر کشوری فوت کند آن کشور نابود می‌شود اما ما هیمنهٔ آمریکا را شکستیم
🔹
معاون وزیر فرهنگ: اسرائیل دولت نیست یک گروه تروریستی است؛ این‌ها از اول فقط ترور انجام می‌داده‌اند و به‌همین‌دلیل سیستم ترور قوی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/akhbarefori/653886" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653885">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
۳ حادثه امنیتی دشوار برای نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری گزارش دادند که طی امروز یکشنبه ۳ حادثه امنیتی دشوار برای نظامیان صهیونیست در جنوب لبنان رخ داده و این امر به خانواده‌هایشان نیز اطلاع داده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/akhbarefori/653885" target="_blank">📅 20:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653884">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
لهستان: از ادامه مسدود بودن تنگه  هرمز رنج میکشیم
🔹
وزیر امور خارجه لهستان: بسیاری از کشورها از بسته شدن تنگه هرمز رنج برده‌اند. امیدوارم  تنگه هرمز باز شود و ما خواستار آزادی دریانوردی برای کشتی‌های حامل سوخت در این تنگه هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/akhbarefori/653884" target="_blank">📅 20:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653883">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2261645d3.mp4?token=I89-50B2pqM4aAaMRJF2Zzl2ezxyVDS2Jg-HyJ3K2AwidZ5AGrtZM-f6s_fdlw0jCXvMht7dVZNzccLuJtwvaq4ctcBYTWJgaaamNCnF49D5ynoEkphsKEYh8eQ7751ZXw-WYwwUN3LcbyLppvg177nmvUSMWcWy6GT_bItT43jZjE8CkLut9HdOruosIjkd9gJuHH8NXA8jT7k4m1stwxVkSRvonEdO7chJGJztiTPrPvAbEJjKcIaiJFgg1gs5RoJD3MwAhYUmw2etKFvQ-i_3wxy-8AIei4_Rta6vfL77eFzUOaqYUE8Qcdxx89sG7EEfdzkhThk_avke5yIlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2261645d3.mp4?token=I89-50B2pqM4aAaMRJF2Zzl2ezxyVDS2Jg-HyJ3K2AwidZ5AGrtZM-f6s_fdlw0jCXvMht7dVZNzccLuJtwvaq4ctcBYTWJgaaamNCnF49D5ynoEkphsKEYh8eQ7751ZXw-WYwwUN3LcbyLppvg177nmvUSMWcWy6GT_bItT43jZjE8CkLut9HdOruosIjkd9gJuHH8NXA8jT7k4m1stwxVkSRvonEdO7chJGJztiTPrPvAbEJjKcIaiJFgg1gs5RoJD3MwAhYUmw2etKFvQ-i_3wxy-8AIei4_Rta6vfL77eFzUOaqYUE8Qcdxx89sG7EEfdzkhThk_avke5yIlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل غیرعادی سکونت یک سوم جمعیت تهران!
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/653883" target="_blank">📅 20:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653882">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
‏مصادیق جنایات جنگی آمریکا و اسرائیل در حملات هوایی به ⁧ایران⁩ در جنگ تحمیلی سوم به روایت تصویر / فقط در ۴۰ روز!
🔹
‏از کشتار دانشمندان، زنان و کودکان تا حمله به مدارس و مراکز آموزشی، ساختمان‌های مسکونی، دانشگاه‌ها، آمبولانس‌ها و مراکز امدادی هلال‌احمر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/653882" target="_blank">📅 20:24 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
