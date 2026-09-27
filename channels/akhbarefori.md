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
<img src="https://cdn4.telesco.pe/file/JKgikmVwZj_ooOa_vGgHKZPqgerJri3mvV_uW79Ynyxu-LQ8UCU-Fx8vc6PktmO4UWPN1L05YWGBf3jXd-LuuIIFmiiGcq30sg6PkpOjBstc5z4msYrSQNuzzNkiawTlfApv3FGTOVNy8Z4vRLfaPJtYJL7X8tb8sIzye9fEHIJoECtfM0VZ46k9IJOZMcYNZp-RWdpnOZUPq_XBq_90X142rKrjDhD-QMVF-eq5jC71OfM8zSPJKUxJ9kEP9k7CtCSd2OlP3w9Bb7G4enNi2oU6Q-Nkne2t0oa0HJFnBM5WWF71EhOQ8-6DXwRpQjspUGbgVj9A9u4VpsewakrPYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-693341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvOyhSlzL15oQ085E4Ok50x660IH0q2Ig5IA6vHhPiQXz-xQjFbNE_Ebh9Kd5adTLcTHPrgenAS96H7nMyh_p3NyILa3vmXjtLFNeneS_x4rrRhWulkIlJWLsUPVVfoyzWZA1-YU1T0RNS9BLTuJlhGk3a5-y01LBNEd0ocoh6C-y13bh9cPP8-xg9Iw-T6SXDtRk8yN0z6U5IuBmYuflWs8xbtVhx7qvxQVbREzSX8Id_4-In-IbVjSUZPw74PtVgxZeWO58Ff3apBPNPFdmm3mAvHkSband7tjCj8v1H1mnwIhKB_nrBpn6k73ndIFqwhdk0DBg0pnjdnp4pNiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرهنگ دوم مجید بهرامی در زنجان، ترور شد و به شهادت رسید
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/693341" target="_blank">📅 10:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gC2luvrUaD6UQafdJGDMm0X5NK7EZhLn99u3fVwjceOkFH8PzW0jLj13Xiwh1qKEANqT11PfqSJNi2KZpnCZWVd8ItEtFbeRNCYEfXFFL1gg3WvYi1-Epxd9faiJlzmNjxYxaS8zBD5jok_rvuZsS7ewmZ0pMlyrmJq5BmwAQLzxcfw2STuoXWBJIg-mk5b0uhf9esYhVaRjnYj6TAF4PCOvOoYK4XwpHJOwRQ2CukW1PZ5cDsIoLye9xhX-7W7AV5OdJg3IzUJkWwoaOt1wQpPDOyy-XONGNqAsg-u89gdJU8AQO8DUOwPzgfu15pLcmtUxOk12cJrzW58wiueWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل دسترسی ایرانی‌ها به ایمیل را محدود کرد؟
🔹
گزارش‌های متعدد کاربران ایرانی نشان می‌دهد روند ساخت حساب جدید گوگل و دریافت کد تأیید برای شماره‌های ایرانی با مشکل جدی روبه‌رو شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/693340" target="_blank">📅 10:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
حشمت‌الله فلاحت‌پیشه، نمایندهٔ پیشین مجلس به یک سال حبس تعلیقی و ۵۰ میلیون جزای نقدی و صادق زیباکلام به یک سال حبس تعزیری و ۲ سال منع فعالیت رسانه‌ای محکوم شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/693338" target="_blank">📅 10:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZBdmsFad1ddFA7IVYlrMiftld8JceGq--pN8T6HFuYeuRfUXI5VnaySHSKkWUD9ZpCpcYo0XDD5-sLYonD63IypWxh_jBL7w6D1QE_4vKTqJU4DB5Yh89ZidlBwMnZZj9DTPXSbKkBF4GXUpe0HOFEVp6TqmqLFG39GMw8QexO4GTWkOqUPzB2A7gPN0pqtthWK1i5OrZzLmSUySYVvC0na160lX-swhE6kiA4eLuT2cwVvO_C-2Km0Extn-D-SvCpoGDEZdUOrL8FGo_2nqAUKUCRqI4SPOoT38OGnok_gS1hSCHG4fr1KiDhgCHgYnEsSaeh8mBfrzkkawSFdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: پنتاگون با تأیید ۳۷ مورد جدید، مجموع مجروحان نظامی آمریکا در جنگ علیه ایران را به ۸۶۱ تن رساند. در لیست جدید، نام ۲۹ ملوان و ۸ تفنگدار دریایی ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/693336" target="_blank">📅 10:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: جنگ علیه ایران باعث شده در آستانه انتخابات میان‌ دوره‌ای، جمهوری‌خواهان در محاسبات خود درباره ترامپ بازنگری کنند
🔹
نامزدها در برخی ایالت‌ها شروع به حذف نام ترامپ از وب‌سایت‌های انتخاباتی خود کرده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/693335" target="_blank">📅 10:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fc5bf247.mp4?token=IeGMjcHvGKxHseDQmZrwwmg1rugZdhRus8FjsjJaYiG41x5IKPFl_qSWkNOkHm5De9Fw3_07f1K30-sRKg6kSCWsipuQQfne89rOKu8YTkmp7MJG7WeG_c1entHWiUl4gzlpdRupS1BXhlUZVOJh1cFSnqOkJF0N8Dz8BLJU2cq8p2mNdxB1xN7aq6oHADc2NVaF0tgp4M2k25ZxTg1DK0wuWZm9q4PVxOUVJxYm8XCDw12-8Oraihki8Y8V8W1SZ8AV3ibPQNT7tyaAynNAgOCu-zuSuppY5hBySlLq_QeM8hqRg1-2afDqUUL_Uf1BMYh9kc00XBMcY1tOnU5o5QXVaD6J_bAVcD4TDvCFoOoPk-N8zB7v997C90EdH6SxLmLXtBCMAYOPriIqACSuOwDnQM1TiW4pt64XOoGr5Qm3QWhTphy7zLIpTHeHConI6cy-_mI5xUnn-22iYVQUun8gqTioX11REZHK67PsFkN6Nk7VDe0dcauTygkz_47T84Wust8rvaoGFok5VbKzFK481LHrNp_n2KT_9RZ45kx3qICg-Pc83sYk878wglOZQheWaLKWSH5EiGxFDSZr-uViTKvX05jqc687CjWYln9spSC5hVvDN0LyIyL8BhJOw8y_G0FMoAJ_uxJnFprfMXa17x49tcfgm9zIw4JTugE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fc5bf247.mp4?token=IeGMjcHvGKxHseDQmZrwwmg1rugZdhRus8FjsjJaYiG41x5IKPFl_qSWkNOkHm5De9Fw3_07f1K30-sRKg6kSCWsipuQQfne89rOKu8YTkmp7MJG7WeG_c1entHWiUl4gzlpdRupS1BXhlUZVOJh1cFSnqOkJF0N8Dz8BLJU2cq8p2mNdxB1xN7aq6oHADc2NVaF0tgp4M2k25ZxTg1DK0wuWZm9q4PVxOUVJxYm8XCDw12-8Oraihki8Y8V8W1SZ8AV3ibPQNT7tyaAynNAgOCu-zuSuppY5hBySlLq_QeM8hqRg1-2afDqUUL_Uf1BMYh9kc00XBMcY1tOnU5o5QXVaD6J_bAVcD4TDvCFoOoPk-N8zB7v997C90EdH6SxLmLXtBCMAYOPriIqACSuOwDnQM1TiW4pt64XOoGr5Qm3QWhTphy7zLIpTHeHConI6cy-_mI5xUnn-22iYVQUun8gqTioX11REZHK67PsFkN6Nk7VDe0dcauTygkz_47T84Wust8rvaoGFok5VbKzFK481LHrNp_n2KT_9RZ45kx3qICg-Pc83sYk878wglOZQheWaLKWSH5EiGxFDSZr-uViTKvX05jqc687CjWYln9spSC5hVvDN0LyIyL8BhJOw8y_G0FMoAJ_uxJnFprfMXa17x49tcfgm9zIw4JTugE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مایونز سالم و خونگی با چند ماده ساده؛ پرپروتئین و سرشار از چربی‌های مفید
😋
🍽
🔹
مواد لازم برای یه شیشه کوچیک مایونز سالم پروتئینی: تخم مرغ اب پز ۳ عدد آب ۸۰ میل یا یک چهارم لیوان سرکه ترجیحا سرکه سیب ۲ ق غ روغن زیتون فرابکر ۵۰ میل حدودا یک پنجم لیوان نمک نصف…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/693334" target="_blank">📅 10:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693333">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/693333" target="_blank">📅 10:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6629a320.mp4?token=YEJlprs8o2wpkyvhtvdWLBXwdYFENaXJkNtY4YCznwMQ2FkKmRKVLPA_y0zkyuFN7CaSdtuYhQ78o_2SZ1yoARD2Px1YOIZplbmb2_k3xeKEYEdxmlCbF6lyJNL8VO6snMiRdCbmWw7i0lg9WUR6FmNZjTjcPC8wB9j0VLe3K9jrEnQ9tbILQbH_15LoUnycNouFQm-0VAEZ2Lr1m0IZne9J2DCourHUBRULX_ZFnC6rXTLG1mLskizyem448nDIVBUFwBFhBzmLs__ZsJDDzhZP41onRW0UIYlIdi6mU2wOsukJuPZfHbAiK_YnInSCqYL4b8AC9JozYZKUh6_-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6629a320.mp4?token=YEJlprs8o2wpkyvhtvdWLBXwdYFENaXJkNtY4YCznwMQ2FkKmRKVLPA_y0zkyuFN7CaSdtuYhQ78o_2SZ1yoARD2Px1YOIZplbmb2_k3xeKEYEdxmlCbF6lyJNL8VO6snMiRdCbmWw7i0lg9WUR6FmNZjTjcPC8wB9j0VLe3K9jrEnQ9tbILQbH_15LoUnycNouFQm-0VAEZ2Lr1m0IZne9J2DCourHUBRULX_ZFnC6rXTLG1mLskizyem448nDIVBUFwBFhBzmLs__ZsJDDzhZP41onRW0UIYlIdi6mU2wOsukJuPZfHbAiK_YnInSCqYL4b8AC9JozYZKUh6_-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صاحب یکی از آشناترین صداهای طبیعت را ببینید؛ جیرجیرکی کوچک با صدایی بزرگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/693332" target="_blank">📅 10:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3124a279ab.mp4?token=b8G3-e_vT6LUf7OdDJQiiMy7Tr9KXCHd4lRUnXobhR2PH5OVeKUgD6PaAqTmCbfw2tt-mgSB_2CYdsLlD-G5PSmDVDQYGPCFyvAha8Mp8xZYYW-zG83FnP8M8rAECf69D6LwTfGiy9LtRUzV19cHRAtSiaAbpBhegA9x78lCm5V2aSngerM-HV_I2nF9Y37kLUPFBRoLMQP5uSTrI0NEc0SF27pbDtRIIzLJuupTIXHJr66w-heACXn1-QDID6uZXg2jfbjSEvz8K7HlZJGK6dlUqb2kj1Q6wKXc1T8QSj32dlluARVKySvYd5My2ArzduETZ0ja5I0D4aX0Ukzvvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3124a279ab.mp4?token=b8G3-e_vT6LUf7OdDJQiiMy7Tr9KXCHd4lRUnXobhR2PH5OVeKUgD6PaAqTmCbfw2tt-mgSB_2CYdsLlD-G5PSmDVDQYGPCFyvAha8Mp8xZYYW-zG83FnP8M8rAECf69D6LwTfGiy9LtRUzV19cHRAtSiaAbpBhegA9x78lCm5V2aSngerM-HV_I2nF9Y37kLUPFBRoLMQP5uSTrI0NEc0SF27pbDtRIIzLJuupTIXHJr66w-heACXn1-QDID6uZXg2jfbjSEvz8K7HlZJGK6dlUqb2kj1Q6wKXc1T8QSj32dlluARVKySvYd5My2ArzduETZ0ja5I0D4aX0Ukzvvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار بود فرد دیگری آن روز در اتاق عملیات باشد
🔹
روایت فرزند شهید نصرالله از روز ترور، به مناسبت دومین سالگرد شهادت دبیر کل حزب الله لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/693331" target="_blank">📅 09:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91ef1e8ef.mp4?token=et12vdxA8Sh2DIQ4GiNB0gHKyhmM_xq11-RIkVgVjqQsXQTDSWlXDCNfeytOe5Xt2lsRLAhWsI5QBqXt4WLlBMx1gzPxokdPyfldjfV89KtA8sNs5oWfS0ubVk8o0mpkGnNZaZWV8cuXVmSCic5oV_tPns0yLGallYio5KtGmcz-tw5wsTTGiYZlNIrh3DmdGe15i9vbEQIA-2vyo4PuaMBrvlQxQYcNNGp7UlqzvM0xvHhIHFfAVUeVFIRWzd0X5kdlsjpD1nKvm7d7RB-Ky47sDHyZHQ8BcP4HBwIMHPYcgTh-_YNebkuNmMYnDE3-vlPqunWLYpGCcxg_HI6pfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91ef1e8ef.mp4?token=et12vdxA8Sh2DIQ4GiNB0gHKyhmM_xq11-RIkVgVjqQsXQTDSWlXDCNfeytOe5Xt2lsRLAhWsI5QBqXt4WLlBMx1gzPxokdPyfldjfV89KtA8sNs5oWfS0ubVk8o0mpkGnNZaZWV8cuXVmSCic5oV_tPns0yLGallYio5KtGmcz-tw5wsTTGiYZlNIrh3DmdGe15i9vbEQIA-2vyo4PuaMBrvlQxQYcNNGp7UlqzvM0xvHhIHFfAVUeVFIRWzd0X5kdlsjpD1nKvm7d7RB-Ky47sDHyZHQ8BcP4HBwIMHPYcgTh-_YNebkuNmMYnDE3-vlPqunWLYpGCcxg_HI6pfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باران شدید خیابان‌های ایتالیا را به رودخانه تبدیل کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/693328" target="_blank">📅 09:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c67f1e8bc5.mp4?token=OXVnJiVC3EFLz8ub8llQXd2-RVqlqS_jEVW6o_Q3pnb9zzwEtEKS451JcYUJpbZwZdPbhk8FHZ07DBymWWE7VvtR1g6w-qsl7P0pQn_9rUVxvRmsTtobbR5ScBTsMagyE34TuJQz34s771wUcYAKVQzAqojaeXgm3fK0p-D90xT6o1H2krbLn_K4qjq6Ptxx6PLx96_mfQonaoAdfXRJ6wcpMmJX2YV7ZCSJQa_WVm_QnQb-aOTAJ5-jjv2qVg93luKcX71oRTS_748kgf2udbVWrF76Ltt0fZmC5BsqSC6Af_wE8Ch4Sex_ZCnn3457zT3H22ApivDUxBEcRUF_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c67f1e8bc5.mp4?token=OXVnJiVC3EFLz8ub8llQXd2-RVqlqS_jEVW6o_Q3pnb9zzwEtEKS451JcYUJpbZwZdPbhk8FHZ07DBymWWE7VvtR1g6w-qsl7P0pQn_9rUVxvRmsTtobbR5ScBTsMagyE34TuJQz34s771wUcYAKVQzAqojaeXgm3fK0p-D90xT6o1H2krbLn_K4qjq6Ptxx6PLx96_mfQonaoAdfXRJ6wcpMmJX2YV7ZCSJQa_WVm_QnQb-aOTAJ5-jjv2qVg93luKcX71oRTS_748kgf2udbVWrF76Ltt0fZmC5BsqSC6Af_wE8Ch4Sex_ZCnn3457zT3H22ApivDUxBEcRUF_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو سال پیش؛ حمله مرگبار به ضاحیه و شهادت سیدحسن نصرالله
🔹
دو سال پیش در چنین روزی، سیدحسن نصرالله به همراه چندین فرمانده ارشد حزب‌الله و سپاه پاسداران در حمله نیروهوایی اسرائیل با ۸۳ بمب سنگرشکن ۲ هزار پوندی به مقر فرماندهی زیرزمینی حزب‌الله در زیر یک شهرک ضاحیه بیروت، ترور و به شهادت رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/693327" target="_blank">📅 09:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: آمریکا برای قطع ارتباط هوایی و بانکی کشورها با ایران، فشار می‌آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/693326" target="_blank">📅 09:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061905b87d.mp4?token=AFbwFEjJPSilrbUfY2eFiUwz30CQ6qCV8VRKzTZCxg0LMpMYMVWMttuTuR46gDei-KdmYM6j6Umx1N-er5fyMK-n7AK_6N3AK_ha6RIaOWAprEZigctjuvpPnSSTKPNyXVltaitgDAWRgtYIpSUTKjSN4cdQmaKsEs7JItvBgW8NOnrapstbxsec8qgXuZHKGRoHX2kctYm2UKWQ2u63AxDOcUpemJtIv415gdAh0Fvr8vNi0Ml72k2BTzuItk6cL6eAknHEB0LEZL00j2gMBs4oeosga1I7BwLKnn7mlWnR8ErLq65qctZwxQW4SaZvI89fMJZGkl3yWHAt6n3VbAaACyI75jzDqGl901eEmLUzdFeVbV1-jg9y9aTqtFpPVzjLrn74TDW-cWQudR98gjFQ9AvyRwWStpTroO-j3uVJDvGMKNGhPpc6EUYT19i8cgSR4r4qYEhogJMu8Ow3L1ZPOjl-cZ5xl0b8q5xOtIMfFM1s1EuGrq0cCBfqjkkWbnZjn666X144-2ToqOabCp16j2RpcfcAEGSOqprsb5orgqAuoiyxGxskinLfVGptgDmowtD3--LIPdota4ySWKaSpkAaxShbFDBUJYCeKWJSkt-lzoMqjNNgvoFyuaiP9ZfUPrfbRej8CcJZJICOtURDvMhCYhRYgTG1KNkJoVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061905b87d.mp4?token=AFbwFEjJPSilrbUfY2eFiUwz30CQ6qCV8VRKzTZCxg0LMpMYMVWMttuTuR46gDei-KdmYM6j6Umx1N-er5fyMK-n7AK_6N3AK_ha6RIaOWAprEZigctjuvpPnSSTKPNyXVltaitgDAWRgtYIpSUTKjSN4cdQmaKsEs7JItvBgW8NOnrapstbxsec8qgXuZHKGRoHX2kctYm2UKWQ2u63AxDOcUpemJtIv415gdAh0Fvr8vNi0Ml72k2BTzuItk6cL6eAknHEB0LEZL00j2gMBs4oeosga1I7BwLKnn7mlWnR8ErLq65qctZwxQW4SaZvI89fMJZGkl3yWHAt6n3VbAaACyI75jzDqGl901eEmLUzdFeVbV1-jg9y9aTqtFpPVzjLrn74TDW-cWQudR98gjFQ9AvyRwWStpTroO-j3uVJDvGMKNGhPpc6EUYT19i8cgSR4r4qYEhogJMu8Ow3L1ZPOjl-cZ5xl0b8q5xOtIMfFM1s1EuGrq0cCBfqjkkWbnZjn666X144-2ToqOabCp16j2RpcfcAEGSOqprsb5orgqAuoiyxGxskinLfVGptgDmowtD3--LIPdota4ySWKaSpkAaxShbFDBUJYCeKWJSkt-lzoMqjNNgvoFyuaiP9ZfUPrfbRej8CcJZJICOtURDvMhCYhRYgTG1KNkJoVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا ایران است
🇮🇷
🔹
این تصاویر بخشی از زیباترین مکان‌های دیدنی ایران است
😍
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/693325" target="_blank">📅 09:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693323">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182adcc130.mp4?token=nVIsPnycY61KZMHf9_6uMX9mPALjXTSoJYppqJWnB-bEMCYixYXM8uLkXvwu3MynWgFombRFdPfbgP0DZuhNtBb6Cv9BEYGIfKLJnlVCeZyI1B7NZYSocbEJz826y2dJ0IkhY3y_AL2jprRPncZYOs167ldDOzjItq1did-f6U11AzCTk_h14V_MkoHTuQYkjri3bR68c7IFCKnE9fvS3DK_-wQwmRQVYI57BzcpsVrLTAqzOfW15LFlT9-eKVcKpnIlnaTCvMZtDlzLEBF8ETNT41uOZIrxlhS_zrdYnbX35vwNX0BG2_1JuHWp6C3rEkUo8BzMyl1j3pPbWABx4VySt6mbwT1NPlaBpFBjfkUDLuTtJlc2i_SM44kWEH3UzsaNpG2v36hQLvh4OzKWAxcWsCfZlw0r45AzCwDYjb_coWxiaoz6UkImvkNxkZEAF5eU9Tu2b42lzq_FBRirfaEt13KOZhxU_0nZvKssb5l0BtWM3Y88Or3wSntHlkr4TwIaXh5qSNTQj19HsvR26pWf9PSVCnR8lrc5-Grm7MEaEOZAa-xwSnYApImKP2puN5btDJNbEVl9t487E8bhABSqGyG06mJIaxn0tOkOTeaREolUayrBPZ_iKXD_Kku5CrFQPeinF4WKcg27FAuKTsFgliMruI4HZPPLwGJH1nY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182adcc130.mp4?token=nVIsPnycY61KZMHf9_6uMX9mPALjXTSoJYppqJWnB-bEMCYixYXM8uLkXvwu3MynWgFombRFdPfbgP0DZuhNtBb6Cv9BEYGIfKLJnlVCeZyI1B7NZYSocbEJz826y2dJ0IkhY3y_AL2jprRPncZYOs167ldDOzjItq1did-f6U11AzCTk_h14V_MkoHTuQYkjri3bR68c7IFCKnE9fvS3DK_-wQwmRQVYI57BzcpsVrLTAqzOfW15LFlT9-eKVcKpnIlnaTCvMZtDlzLEBF8ETNT41uOZIrxlhS_zrdYnbX35vwNX0BG2_1JuHWp6C3rEkUo8BzMyl1j3pPbWABx4VySt6mbwT1NPlaBpFBjfkUDLuTtJlc2i_SM44kWEH3UzsaNpG2v36hQLvh4OzKWAxcWsCfZlw0r45AzCwDYjb_coWxiaoz6UkImvkNxkZEAF5eU9Tu2b42lzq_FBRirfaEt13KOZhxU_0nZvKssb5l0BtWM3Y88Or3wSntHlkr4TwIaXh5qSNTQj19HsvR26pWf9PSVCnR8lrc5-Grm7MEaEOZAa-xwSnYApImKP2puN5btDJNbEVl9t487E8bhABSqGyG06mJIaxn0tOkOTeaREolUayrBPZ_iKXD_Kku5CrFQPeinF4WKcg27FAuKTsFgliMruI4HZPPLwGJH1nY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه واردات کالا به کشور در شرایط جنگی سرعت گرفت؟
🔹
محمدحسین مصباح، فعال اقتصادی: سیاست‌های پیشین ارزی در کشور، تجار را برای واردات کالا زمین‌گیر کرده بود.
🔹
اما بانک مرکزی با ورود به‌موقع و اصلاح یک رویه غلط، گره کور تجارت را باز کرد و دغدغه دسترسی به کالا در شرایط جنگ و محاصره برطرف نمود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/693323" target="_blank">📅 09:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693322">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50fbe3f8e.mp4?token=rZ-WqUvwjEWZV1BCsDKz1C4mTKlxAtWejtNCDo_9SDLpfy799UpZ2tAS9oWLlRGRo99JG1hR7z8_5m0U992m_NQmuqqlkaaJfHfq8w4fBad8MQNdDgHF6RMCsSBt6IlYjUrvixcwUsG9nM2E2C-Hlx8Ky9mHJh5222wjVFBQRxvZTRdjWWNhq0y1448eh8iLl4X6ELItKUsZjCYX_T7xkgl6i4zuwHweTOF6mMO9f_PBin3jvNfXBq1df_dA6AJYvEQzg96hADgu10om8VmozdiMShVDaKURLq4sWJgCMZveQkj5ns25xOeRsBVkB3WCSH7LHAP9ug4f-JWEe1WsRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50fbe3f8e.mp4?token=rZ-WqUvwjEWZV1BCsDKz1C4mTKlxAtWejtNCDo_9SDLpfy799UpZ2tAS9oWLlRGRo99JG1hR7z8_5m0U992m_NQmuqqlkaaJfHfq8w4fBad8MQNdDgHF6RMCsSBt6IlYjUrvixcwUsG9nM2E2C-Hlx8Ky9mHJh5222wjVFBQRxvZTRdjWWNhq0y1448eh8iLl4X6ELItKUsZjCYX_T7xkgl6i4zuwHweTOF6mMO9f_PBin3jvNfXBq1df_dA6AJYvEQzg96hADgu10om8VmozdiMShVDaKURLq4sWJgCMZveQkj5ns25xOeRsBVkB3WCSH7LHAP9ug4f-JWEe1WsRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترمز ماشین برید؟
قبل از هر کاری این روش توقف اضطراری خودرو را یاد بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/693322" target="_blank">📅 09:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693321">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwrjwbZw9R90wPIFwFlz7t0EaKIn3QfaXxihgKqGW5F6fRpiSxNtHF1jyhgOtwHB2p0AydkpwjGpz3xZLOYNhD1ChL3uVPCHtuH2dz0wa-2szkUOKfeY8Brpr1W9pmYos30C8VsdGxaPRPpOpu_RjvUvsqdmMIPOc9Tj3u8erpqiftYyQUvtXuT91DsoN-F4rm7iohrWcBQiazYRp4agn926ge1nAZ-wUy22WfWVcJtseQr0nDuHycct6U2Tvxw9mpGVQcVgXvIQa8NQCT1LpX0tpjKfpUz2Ll_Os4Erh_9t2VR6ePGKr_I4ogmcgx_ZR3kgGIigXgSxr-YCPjCs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه خبرگزاری روسی راشاتودی درباره میزان حضور مخاطبان در سخنرانی پزشکیان و نتانیاهو
🔹
سالن سخنرانی پزشکیان مملو از جمعیت بود؛ در حالی که سالن محل سخنرانی نتانیاهو به‌زحمت نیمی از ظرفیت خود را پر کرده بود. سوال مهم:
واقعاً چه کسی منزوی شده است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/693321" target="_blank">📅 09:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693320">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه هفتم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه هفتم؛ ولایت پروردگار
🔹
تکرار و تدبر در نام‌های پروردگار باید در عمیق‌ترین لایه‌های خیال و سلول‌های بدن تثبیت شود تا فرد حس استواری و قدرت الهی را با تمام وجود احساس کند.
🔹
اتصال به نام «الْوَلِيّ» مانند یک قطب‌نما عمل کرده و به صورت شهودی، دوستی با اهل حق و دوری از اهل باطل را در دل انسان نمایان می‌کند.
🔹
پذیرش ولایت «اللَّه»، انسان را هم‌زمان به بندگی حق و رهایی از تمام قید و بندهای باطل و تاریک می‌رساند.
🔹
تکرار و اتصال به نام «الْوَلِيّ»، حصاری نفوذناپذیر در برابر انرژی‌های تاریک، کدهای ابلیسی و افکار منفی ایجاد می‌کند.
🔹
انسان شبیه به کسی یا چیزی می‌شود که به آن دل می‌بندد؛ بنابراین، انتخاب‌های او در دوستی و الگوپذیری، تأثیر عمیقی بر زندگی او دارند.
🔹
دوستی حق، فقر، رنج و بیماری را از وجود انسان‌ها و سرزمین‌ها پاک کرده و برکت، عشق و فراوانیِ الهی را جایگزین آن‌ها می‌کند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/693320" target="_blank">📅 09:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693319">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d4b39765.mp4?token=RAgD4lQaL_uHJB_GL9K9pFb4Ss0p9RzBeusQ5qnwfSaym0MK1P-v21qxqYKPm5c-mlHFUjCZF024iy82s5WSXXy34FtigB6F3OAsthNz3MPBcVSb1DuvBg9p3meCjGjLWlcNgHUJPU7LnR5x-SI7AL3Ttu1qtVszX4W2Qe6x94IKBbI_9_OxTDwXB_pCsgRG3okNHfGUdF3dyWG06ZbiZNwMMnoWT9EZv34GUbHCTR7G5Q4KGqBbzGaqTtoOthitQFmSiON4DNPciipGz9cj3U_GamnOin2fXyy3qhABWaycsc3QPNeVZAPY7tIEwrdRyjH4PxlenSjC1RIgyVZM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d4b39765.mp4?token=RAgD4lQaL_uHJB_GL9K9pFb4Ss0p9RzBeusQ5qnwfSaym0MK1P-v21qxqYKPm5c-mlHFUjCZF024iy82s5WSXXy34FtigB6F3OAsthNz3MPBcVSb1DuvBg9p3meCjGjLWlcNgHUJPU7LnR5x-SI7AL3Ttu1qtVszX4W2Qe6x94IKBbI_9_OxTDwXB_pCsgRG3okNHfGUdF3dyWG06ZbiZNwMMnoWT9EZv34GUbHCTR7G5Q4KGqBbzGaqTtoOthitQFmSiON4DNPciipGz9cj3U_GamnOin2fXyy3qhABWaycsc3QPNeVZAPY7tIEwrdRyjH4PxlenSjC1RIgyVZM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: از امروز برای شمال کشور بارش برف و باران و برای گلستان و شمال‌شرق سمنان هشدار نارنجی سیلاب صادر شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/693319" target="_blank">📅 08:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693318">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862b79e23.mp4?token=W4ytMm-55U4OTZRusksZ6FuHSuo6CRpFApN6xIn5_-29fEiGCGylKk0pLS0-z3LDAZxMrpJJI2yEeYKc3f_LZEDeihPmFKVBBn50PSMCxMm3CG3oYLChaea0FbEUkNFXDn3s7_hHHzXN5QZoukYibNbcdPTxjOENhaiPC6gQqRdoSf4ppkd04bRSm52e-aOKtFYWcVy9N6hGVVul46HEgNmppHz-ZJ728uBQfYIyyI3eNRtxqye4RgNVVibIwHFkhFKBBw61pwOWoZZebI9OwAmoa4c2WvwceHQ3eb3QyV4l48xYYThDFolpoLbm04MzWNxGpbrrL5yG1J3bULL5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862b79e23.mp4?token=W4ytMm-55U4OTZRusksZ6FuHSuo6CRpFApN6xIn5_-29fEiGCGylKk0pLS0-z3LDAZxMrpJJI2yEeYKc3f_LZEDeihPmFKVBBn50PSMCxMm3CG3oYLChaea0FbEUkNFXDn3s7_hHHzXN5QZoukYibNbcdPTxjOENhaiPC6gQqRdoSf4ppkd04bRSm52e-aOKtFYWcVy9N6hGVVul46HEgNmppHz-ZJ728uBQfYIyyI3eNRtxqye4RgNVVibIwHFkhFKBBw61pwOWoZZebI9OwAmoa4c2WvwceHQ3eb3QyV4l48xYYThDFolpoLbm04MzWNxGpbrrL5yG1J3bULL5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نبرد انسان و حیوانات در ماراتن ۱۰۰ کیلومتری؛ این‌بار برنده یوزپلنگ نیست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693318" target="_blank">📅 08:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693317">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
خبرنگار اسرائیلی: حملات دیشب سپاه پاسداران به کشتی‌ها در تنگه هرمز گسترده و کم‌سابقه بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/693317" target="_blank">📅 08:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: تیم‌هایی به نقاط مختلف جهان اعزام شده‌اند تا از کشورها بخواهند علیه ایران اقدام کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693315" target="_blank">📅 08:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949dc40c1e.mp4?token=REfuuVLwqdNa1tbjDEQIadUpUp5vHhd39dQ5jTwaeZ85E4EJ9DSojN12j9KL6HH4h6qHvfGRmKqx7huYWzukINDt4caJjR_pbgXQHWci2K59WDsVwqKfXOLdlkeJ3vLb0yNH4hgG_-WGR0ucLVZNmJLwU2gPWc90qkTAYe28o4nWeqWD2pAnwnnScOmcMEEBpt1IqIy5w6mxII-zwcKbmUQ3oDK0b8t4SweiHiUJHEZe9iybFQjxybMx3qjIayTAjApBkSt0MHiVyj45uO8DsINdYO65i7sDPmzVVS8sNwwGU248VyrfWTsrdFfqLbdjAT-Buth9qilwrrNIv7qWviCvz_dthDNhza20v77m8QPxCIfAi7TRDjz4jAl3zFdLZoTyrJyo4o0rh0m8rSQjjBgUMbopzZ4Gv8ljNPrhMgFSo266Wx3ii-zifK33Ew48u7sFcXG14Cz0hFm9_7NaRZW2q8TcCxJijelAF9JoT122qp830ghBERabwL_8UGJDRb6RhWGEoS-rCKgMro3SeDkivdpuer7agT0E_ic-4xkptxhJq_iBr7qIVvPMGOCxSVu8T55h-MlnqNrqibo7JHenWJZ0skU7xocH6kEl2TIdbf9htrrn3giAtJbFhFXr5EMi14Fw9YOGxYvrPi_kE2CFRVNiSTBqKwvbqRFeKZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949dc40c1e.mp4?token=REfuuVLwqdNa1tbjDEQIadUpUp5vHhd39dQ5jTwaeZ85E4EJ9DSojN12j9KL6HH4h6qHvfGRmKqx7huYWzukINDt4caJjR_pbgXQHWci2K59WDsVwqKfXOLdlkeJ3vLb0yNH4hgG_-WGR0ucLVZNmJLwU2gPWc90qkTAYe28o4nWeqWD2pAnwnnScOmcMEEBpt1IqIy5w6mxII-zwcKbmUQ3oDK0b8t4SweiHiUJHEZe9iybFQjxybMx3qjIayTAjApBkSt0MHiVyj45uO8DsINdYO65i7sDPmzVVS8sNwwGU248VyrfWTsrdFfqLbdjAT-Buth9qilwrrNIv7qWviCvz_dthDNhza20v77m8QPxCIfAi7TRDjz4jAl3zFdLZoTyrJyo4o0rh0m8rSQjjBgUMbopzZ4Gv8ljNPrhMgFSo266Wx3ii-zifK33Ew48u7sFcXG14Cz0hFm9_7NaRZW2q8TcCxJijelAF9JoT122qp830ghBERabwL_8UGJDRb6RhWGEoS-rCKgMro3SeDkivdpuer7agT0E_ic-4xkptxhJq_iBr7qIVvPMGOCxSVu8T55h-MlnqNrqibo7JHenWJZ0skU7xocH6kEl2TIdbf9htrrn3giAtJbFhFXr5EMi14Fw9YOGxYvrPi_kE2CFRVNiSTBqKwvbqRFeKZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: آقای الشرع، یهودیان از زمان موسی در بلندی‌های جولان حضور داشته‌اند؛ می‌توانید در کتاب مقدس بخوانید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693314" target="_blank">📅 08:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38043922b9.mp4?token=JaIk9I4La_MNET0l-1O9Q6Q1fnLf5t7D0oSo4wy99zOxpXwR6A-oMwhxC-M6Xs1knfFxulAF2C1QjAmAR1OgsieQAtteNRIPkcI59YnHBtCjZVyt52xYS3nm0JORdkF9_fEGnfRyT9crqX5nVN7NkrHxAOmKAgCL2Waj37O7NFdmhbECzEVaYGeMZFiWsCw5KXz_2rSMqfo3vZgc_wkSKD_i-tX2E0iePyep1yFxe2g3Boew-XZn4uxJaLGfvT7WDZ7AHc31NI-CXgNHLQSTqDFGhwJ7Rp5h6dRVBTQm3utdaPn61mQNmqe9FvipxUlKy7eEm5-jnoxnon3UW7wCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38043922b9.mp4?token=JaIk9I4La_MNET0l-1O9Q6Q1fnLf5t7D0oSo4wy99zOxpXwR6A-oMwhxC-M6Xs1knfFxulAF2C1QjAmAR1OgsieQAtteNRIPkcI59YnHBtCjZVyt52xYS3nm0JORdkF9_fEGnfRyT9crqX5nVN7NkrHxAOmKAgCL2Waj37O7NFdmhbECzEVaYGeMZFiWsCw5KXz_2rSMqfo3vZgc_wkSKD_i-tX2E0iePyep1yFxe2g3Boew-XZn4uxJaLGfvT7WDZ7AHc31NI-CXgNHLQSTqDFGhwJ7Rp5h6dRVBTQm3utdaPn61mQNmqe9FvipxUlKy7eEm5-jnoxnon3UW7wCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماهنگ جدید محمود کریمی به زبان انگلیسی منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/693313" target="_blank">📅 08:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پکن: روسای جمهور آمریکا و چین توافق کردند که «هیچ کشور یا نهادی نباید بابت تردد در آبراه‌های بین‌المللی، عوارض دریافت کند»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693312" target="_blank">📅 08:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7JpiPZrz4EHeG5i04wL3tU2W9cqOqRzgLWCurgAv3gLA_XB-eCMBkEudai10Iyg2dUnnm3JmI4AaEt6oeSI74v1sOtVU1P6UdgqV7Y93Ct-RKer-XqdexSzaQh5x32agzMOKX17UVeR6C4tH12phulJp8qaveRdDAH6ljPbNwLT5LtASzPjRYWmIzudVbTRqCweYsE2u6iFuhAB-uglkMjm0DwHtd3e1XbOaHnyvNr7UrOjqXESrnlsvJSO1Xs8FIZj24JOg3stuv7IqTbmTuLYY-oLeqarwu6dXw1ROfIboI1UYSUNgozAoXFlpuYk1p1tP9-ajBWLRfS6CmhgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgDjD1HWwmgAKbT7iEV7Vc97PkYe_T5MT_URR4S2jDHJe25lc5Lba-iFcRo2RjiFTrdOnYWSHj36z-rF7AjRp6rf9eJMIzfP_aXly3KZo6sdNo_hUCNNZ0ooA2_Ja0se8-Y8H9qmEwiyfdc5ruO3bWQhd1kEdLLkPiGRX4sRHlteug92ohmQRmGD3GDhPicneiwv8JjzXx6g6QUDJBBBIrfwWowwk3ScX3duF0s7IMCOGmMiK34IZF3KjMAHMe4MYL5LTYfpIylAJbikCXMMfSPfTH-m_PejRHVBZHkWxGSDbvaZXo-u383V-z4-IF2bvNy8H4Vdqd0Jv7dJe2zDug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار نهاد مدیریت آبراه خلیج‌فارس به مالکان کشتی درخصوص تردد از مسیرهای نامعتبر
🔹
در راستای این هشدار ایمیل عذرخواهی مالکان کشتی‌ها بخاطر عبور غیرمجاز کشتی از تنگه هرمز دریافت شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/693310" target="_blank">📅 08:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693309">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d88a96cd.mp4?token=XLurf3QGzYwJUQuo9KMl8XG-3_L2kaM3Rmkk3koWMBrt4VdOtzrTgfLS3LDX3qUr71ieyJyx0uABIyNBaK_Mmzsk4qJDAkTv5fb8B4ka-RGQtNKLYhVK2BpsQhUoUvwvhbTvi_VqY3BlhMzfaVJC7POrLPz6TYNjCuWs23bCHxhMBFnufqYlOrpBfq76tPkQiESHOPIcocrNpyUhcsCzKfgUBYy-I2tI-iGVzrB_LeTGh95B5MJxeNMkM9NJxM58TvzOhJRfooI7MH-2zUOmgX6mUfGZEIS8luyVc95B23fyYmoEbVzzapaO6kpfli0eVWvuc0D-HdMNZy-vfJOqE7ucZwGg0MWhYFuoLAAiLLLoza_y35ghMTb3fOWvg6iqVBqCl7KM-BUPTws4CB-djlTf58suTF0mlgQhEnpoMjRCRKADJLl90Qq4-zewflmQOnM0tfwr8JNzzYw__-eLE3FfqT-zOVjf3uDSrQ5mY-ttMihNY5BRLdxZ4mB7IFHT8TTmvqI6vFO0IPjNVAhPT7IM2oQwikwCnlx46hJ8oDv9cFrZLK0OqBq9vlehQPYce3oP_Vx1hVB_lgdxSxw5YfYwy_D54ECbR-HfGl_fh6-Gq3ipbmP6NJ8-_eGt17GGxaXIb5d8-afakHjko1Y96y_tR8a_beK_Ii1MQYsM6rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d88a96cd.mp4?token=XLurf3QGzYwJUQuo9KMl8XG-3_L2kaM3Rmkk3koWMBrt4VdOtzrTgfLS3LDX3qUr71ieyJyx0uABIyNBaK_Mmzsk4qJDAkTv5fb8B4ka-RGQtNKLYhVK2BpsQhUoUvwvhbTvi_VqY3BlhMzfaVJC7POrLPz6TYNjCuWs23bCHxhMBFnufqYlOrpBfq76tPkQiESHOPIcocrNpyUhcsCzKfgUBYy-I2tI-iGVzrB_LeTGh95B5MJxeNMkM9NJxM58TvzOhJRfooI7MH-2zUOmgX6mUfGZEIS8luyVc95B23fyYmoEbVzzapaO6kpfli0eVWvuc0D-HdMNZy-vfJOqE7ucZwGg0MWhYFuoLAAiLLLoza_y35ghMTb3fOWvg6iqVBqCl7KM-BUPTws4CB-djlTf58suTF0mlgQhEnpoMjRCRKADJLl90Qq4-zewflmQOnM0tfwr8JNzzYw__-eLE3FfqT-zOVjf3uDSrQ5mY-ttMihNY5BRLdxZ4mB7IFHT8TTmvqI6vFO0IPjNVAhPT7IM2oQwikwCnlx46hJ8oDv9cFrZLK0OqBq9vlehQPYce3oP_Vx1hVB_lgdxSxw5YfYwy_D54ECbR-HfGl_fh6-Gq3ipbmP6NJ8-_eGt17GGxaXIb5d8-afakHjko1Y96y_tR8a_beK_Ii1MQYsM6rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از نخستین لحظات جست‌‌و‌جو تا رسیدن به پیکر مطهر شهید سید حسن نصرالله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693309" target="_blank">📅 08:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693306">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
ترامپ: من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/693306" target="_blank">📅 08:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQO1MRMBBScvyQjTGNoPpMVWFPDC_wNZM4484kxPIjG3XytF6RQ_LW5quWxenw_gJMK4Gh1kdrOVaD9YdKQyr6yR_ckGX6Kti_vAJUO3owyhKOFig577d3turkMOOz-ZhF2PC9U7WhKb2kXntKv72SX0P3zECkTsVanCnAQTsHXfbmhbWNO5JKulEm4VRU98KW-59Hd5VydUE-iO5Nq_V0k4TMXbETeAKusSTCkAWzhJbKblNYLQuGxG8hKmYepehpBcwNo3i0BQaDbsWgC-cr0P_0HuIaMRJm-heWcAqfb3iKpVTNsBM3qn83MYlFnca8-tZIoiXCi67K9m371D2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۵ مهر ماه
۱۵ ربیع‌الثانی ۱۴۴۸
۲۷ سپتامبر ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/693304" target="_blank">📅 07:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6e6adadb.mp4?token=XprQxRPJkCcCTIQ1XB1_-jRtQICL762-q9nRf-uOXYTzY6daaI-mWbehGPQ9Hfv7TWhcYdD_1LzPEKBwYvlA6wr8s0Mwo4HyRwLublwDqL_8cQDdeF3-te0HKTU6QHh2O_Sr-Abu_nUTk_VMcklJeHc63nwYbJQbJU7vRM3C4uya3wvhR8BM6toTQxMvXYHrSrzLcBjp5GXmNUb7Unpgo11I8p2xLBt5k8jUyn4Xg_NkXUDnPhAeatnpx85B63OgLsW7FPgvDc_PmZUlTD_qNBZwc788WsfG1RqqylsdzX4uqtsTEmf8ayXUJmeEeDOgQIvyGLPxrs3wQ3zCGrYc3zgAK8wvuRDMsuW9gPKsxV9-tOYF3NxAXcx9z0UT0OGPo0vVjo8Fa2h4MRDjQco6f92l8dmtgDIfO9Zk3B8QBTWH5C3XsCVjns2uekl7wOk_FDxMHakB0nyFLZqWnArwJe-1lckm68qWILSqgIl2Q4KOgg_mrtMiL6byAhlvExArPq_fzlP8t9wcAVZvrLzLxGTDh2YwNp5xeQ2j4CX-LvhL8qRjDfp9lZsEt3dJ7otZZTBmcBMZPY_Ucf5WIh0YBYC7WcLuwzkazxqolyReOZ4-qRkAIxeb6esHL9mQL3F_RdpGZ5WVECErIJr_rO4l5Isw7Pmk2LvA1UPk5XDcIHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6e6adadb.mp4?token=XprQxRPJkCcCTIQ1XB1_-jRtQICL762-q9nRf-uOXYTzY6daaI-mWbehGPQ9Hfv7TWhcYdD_1LzPEKBwYvlA6wr8s0Mwo4HyRwLublwDqL_8cQDdeF3-te0HKTU6QHh2O_Sr-Abu_nUTk_VMcklJeHc63nwYbJQbJU7vRM3C4uya3wvhR8BM6toTQxMvXYHrSrzLcBjp5GXmNUb7Unpgo11I8p2xLBt5k8jUyn4Xg_NkXUDnPhAeatnpx85B63OgLsW7FPgvDc_PmZUlTD_qNBZwc788WsfG1RqqylsdzX4uqtsTEmf8ayXUJmeEeDOgQIvyGLPxrs3wQ3zCGrYc3zgAK8wvuRDMsuW9gPKsxV9-tOYF3NxAXcx9z0UT0OGPo0vVjo8Fa2h4MRDjQco6f92l8dmtgDIfO9Zk3B8QBTWH5C3XsCVjns2uekl7wOk_FDxMHakB0nyFLZqWnArwJe-1lckm68qWILSqgIl2Q4KOgg_mrtMiL6byAhlvExArPq_fzlP8t9wcAVZvrLzLxGTDh2YwNp5xeQ2j4CX-LvhL8qRjDfp9lZsEt3dJ7otZZTBmcBMZPY_Ucf5WIh0YBYC7WcLuwzkazxqolyReOZ4-qRkAIxeb6esHL9mQL3F_RdpGZ5WVECErIJr_rO4l5Isw7Pmk2LvA1UPk5XDcIHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مضیف الکریم
نزدیک ترین رستوران بزرگ به
حرم امام رضا علیه السلام
غذای با کیفیت، قیمت مناسب، پذیرایی بی آلایش
⏰
هر روز هفته
ناهار از ۱۲.۳۰
شام از  ۱۹.۳۰
تا اتمام غذا
روزانه و درهر وعده فقط یک مدل غذا سرو می شود
جهت دریافت لیست غذاها و تاریخ سرو آنها پیج مضیف را دنبال کنید
📌
قیمت تمامی غذاها با برنج درجه یک ایرانی،
۳۸۵ (سیصد و هشتاد و پنج) هزار تومان + ۱۰ درصد مالیات بر ارزش افزوده
•
📌
مضیف هیچ ارتباطی با آستان قدس و مهمانسرا ندارد.
📍
آدرس:
حرم مطهر، ابتدای خیابان شیرازی، مجتمع جهان نما
ورودی پارکینگ مجتمع: از شیرازی ۹
•(اطلاعات بیشتر رو از طریق پیج اینستاگرام پیگیری بفرمایید)
https://www.instagram.com/mudhif_alkarim?stkn=N3gwam9rN3BkOGtw</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/693303" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd7b5d2cb.mp4?token=aEuqky0QJrHbDT9ZuVwq-vwuhuGKqEPjP1XE5T_zxYmaNhxIwZw4fGpbQCjxloh1MRbB6bGoXixu7f96R9GprmZQGuBbw6t4MyX9h4MnnmpuNZ7n3WjrqNKEA315rWvFGbt7Z1taVFMdkvH4JjdCEKGihW7f46hQOhvniyg7uei5mh8HvHu3b4IrhmYCreex0RnVTHr8Rfo_OnxuzKm31WZJXrsjRedWTICWHzjHB4BCyeESy3w157DoZOXl9NCwhB0oGnfVXYbU0G1sMcBeW-68SOlWXHhx9de9iVFcN6xW25r559V-wA4jP6P4AiQhu__RoKnyKvXmR9PSP6OJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd7b5d2cb.mp4?token=aEuqky0QJrHbDT9ZuVwq-vwuhuGKqEPjP1XE5T_zxYmaNhxIwZw4fGpbQCjxloh1MRbB6bGoXixu7f96R9GprmZQGuBbw6t4MyX9h4MnnmpuNZ7n3WjrqNKEA315rWvFGbt7Z1taVFMdkvH4JjdCEKGihW7f46hQOhvniyg7uei5mh8HvHu3b4IrhmYCreex0RnVTHr8Rfo_OnxuzKm31WZJXrsjRedWTICWHzjHB4BCyeESy3w157DoZOXl9NCwhB0oGnfVXYbU0G1sMcBeW-68SOlWXHhx9de9iVFcN6xW25r559V-wA4jP6P4AiQhu__RoKnyKvXmR9PSP6OJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
چسب همه‌کاره پلی‌اورتان آرازیم؛ مناسب روزهای بارونی!
برای آب‌بندی و درزگیری قسمت‌های مختلف مثل:
🔹
درز پنجره و درب
🔹
ترک و شکاف‌های ساختمانی
🔹
درزهای بین سطوح
🔹
جلوگیری از نفوذ آب و رطوبت
💪
چسبندگی بالا و مقاوم در برابر رطوبت
🎨
رنگ: خاکستری
🔴
قیمت 1,798,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
قبل از شروع بارندگی، درزهای باز رو جدی بگیر!
😉
خرید تلفنی
👇
https://memarket24.ir/product/fast/63720/180124/</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/693302" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBUd53iPH9HMbtKaSKe1PrnNwiKBZnFfrmiCIgXdMn5jFJveIlgNgt3lwvLgRWBEO9xfDHlh043KtTwZDuhIBKhcrCc5QLo3v2DisM2JBYHnLHRMtDB_9U8Gzf1bufKKJwfosL-iNy5Z6cJ2Xml6SO1wCrzWwmteTClOuIVNWRCyD2-vCN0SZfC4sCTXuw-WAJuLX6ECAS_4ck3t_HpDtRcV5VxDiw0fl176wv2y1usLNU7KTsOal6xBESkUDyGijObO1-VIFZ4dNkfhuO4zhbox45ykexcaEoJSN-bfeYGIYaWdz6USHqZ9Jc0gyizjLW91cccYXTt4gYrXO2zx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگشتر نقره میخوای ولی از قیمت های زیاد نمیتونی بخری؟؟؟
💎
کانال زیر انواع
#محصولات_نقره
رو با پایین ترین قیمت میفروشه
👇
😳
https://t.me/khalijjgallery
https://t.me/khalijjgallery
❌
تخفیف ویژه برای خرید اولی ها
❌</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/693301" target="_blank">📅 00:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxEMgz1VgSE_K6Yct5BLBRGqE3BR7Rm_1o2Itrdydd0d7N4JnEiBzo2yl8QlCt-mv4028iTB5uaXzOM5fL4z9637Dae2L4DSqLb9yPY5X0_Yj_tibOtjM0qhWdQHgGp3rGzEn1FBwwqtuGipjtGzk3zIzd5g9pKrKvFG3aW6HDH9q76UGhlTPXNkMHuTykC3ciCnccizqpJGZmKxtxqHF0A6TZ_alvXP0fC_A83iufx9Fn504Ij2YvI9U42gmBrOcVOLUO6CvzhBU4kE_GN234wT-193pFWTmHqGRcHIKKMUOhApWzT125KqwNMgNQfQUOJ5koSBhvyxfLsSMeJ5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از ماه کامل امشب
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/693300" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c245685da2.mp4?token=n80AibVqDIZoeP1VISGAsR5E0q42csRc4o9tmij-Bj5Ndg4t0vks0rAd_Br8uJiOsn67gkxcxpkgxwAArc5IP3p0KJ9FAKp1rTLJhKBnS5IFsI2_8U-eAfhAmJsx1h7AAKf4RLrKPOZfxgs7SeUZC4qbk9RDQiCCUocZEaqEsKCapEd5VUFSbx1S6Ft_8JeM7prGRA3iqCIDmDAV_9Eb7KCaP6UDFfMkjS4JzLQzz3GQyz-qpqMZPO3BNlXM-LPLFa31z25Te2fCs0cdxTA0pi_nQGKK_VLPaZSfm9Yh0BmwSWknPNhr7Ib-j8AYx1owG3hUbUiKRLuL5Ggf6wjhLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c245685da2.mp4?token=n80AibVqDIZoeP1VISGAsR5E0q42csRc4o9tmij-Bj5Ndg4t0vks0rAd_Br8uJiOsn67gkxcxpkgxwAArc5IP3p0KJ9FAKp1rTLJhKBnS5IFsI2_8U-eAfhAmJsx1h7AAKf4RLrKPOZfxgs7SeUZC4qbk9RDQiCCUocZEaqEsKCapEd5VUFSbx1S6Ft_8JeM7prGRA3iqCIDmDAV_9Eb7KCaP6UDFfMkjS4JzLQzz3GQyz-qpqMZPO3BNlXM-LPLFa31z25Te2fCs0cdxTA0pi_nQGKK_VLPaZSfm9Yh0BmwSWknPNhr7Ib-j8AYx1owG3hUbUiKRLuL5Ggf6wjhLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو جالب از وضعیت دو مدرسه دولتی و غیرانتفاعی در کنار یک دیگر، استان مازندران
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/693299" target="_blank">📅 00:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع عربی: شلیک سه موشک کروز ضدکشتی ایران به سمت تنگه هرمز/ هم‌میهن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/693298" target="_blank">📅 00:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc30cdd6c.mp4?token=YkHWD5dsetD9EGEoZWB43fGbPW9ONX-OrtrEO2TTX0OmOoG0WosCtkBePT7YP4mo18c6O42beNzzpy4NgSZIhkOQrTWnZZcLwGm9hfJzA4mcLhPt8uVZXYTqtoBqLDCbE5uzMVN7am6zUSPjUd3l3VsgE2oDZyohhkqbCDSSw9I1Ug-jwb3SROwU2fGJT82ODm2LxS0MAT_MXH7-jsSuMOf_-yGWs6u5vUwaopwg2A9tauvoGz2YfgQWN06Gr7XvNJCEIz7Pq-BBgpJbHHL4eV4qOjC_dEodLqAvY9Li2mb8Rkwv0hkhGeoxVnIH_ULmIElYlxXOPzbVUiyuOFOpaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc30cdd6c.mp4?token=YkHWD5dsetD9EGEoZWB43fGbPW9ONX-OrtrEO2TTX0OmOoG0WosCtkBePT7YP4mo18c6O42beNzzpy4NgSZIhkOQrTWnZZcLwGm9hfJzA4mcLhPt8uVZXYTqtoBqLDCbE5uzMVN7am6zUSPjUd3l3VsgE2oDZyohhkqbCDSSw9I1Ug-jwb3SROwU2fGJT82ODm2LxS0MAT_MXH7-jsSuMOf_-yGWs6u5vUwaopwg2A9tauvoGz2YfgQWN06Gr7XvNJCEIz7Pq-BBgpJbHHL4eV4qOjC_dEodLqAvY9Li2mb8Rkwv0hkhGeoxVnIH_ULmIElYlxXOPzbVUiyuOFOpaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به نظر شما چرا تریلی ها یک چرخ معلق دارن!؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/693297" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693296">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
درگیری شدید در مرز افغانستان و پاکستان
🔹
گزارش‌ها از آغاز درگیری‌ شدید میان نیروهای طالبان و پاکستانی در خطوط مرزی منطقه خارلاشی در ولسوالی دنده پاتان، حکایت دارد.
🔹
بر اساس این گزارش‌ها، دو طرف در این درگیری‌ها از سلاح‌های سنگین استفاده می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/693296" target="_blank">📅 00:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔹
از خبرهای جذاب امروز و امشب جانمانید
🔹
🔹
مذاکرات نیویورک چطور شکست خورد؟
👇
khabarfoori.com/fa/tiny/news-3248085
🔹
ترامپ پیشنهاد ایران را رد کرد؛ جنگ شروع می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3247922
🔹
موج عظیم ورود غیرقانونی افغانستانی ها به ایران | ویدئوی عبور مهاجران از مناطق خطرناک
👇
khabarfoori.com/fa/tiny/news-3247956
🔹
بازسازی جنگ سوم ایران و اسرائیل و آمریکا | سه روز نخست جنگ چه اتفاقاتی خواهد افتاد؟
👇
khabarfoori.com/fa/tiny/news-3247830
🔹
اقتصاد زیر فشار؛ آیا یک شوک بی‌سابقه در راه است؟ | این محاصره تا پایان سال دو دهک دیگر را به فقرا اضافه می‌کند!
👇
khabarfoori.com/fa/tiny/news-3247997
🔹
برای خبرهای بیشتر، کافیست کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/693295" target="_blank">📅 00:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693294">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb3JAagYZ-HlSPN6Nq3x7nEp1Tca8C1I2XCOCcMM9B8Im86xcZxnhkjlQgLSRBRXjyGDfG-MirTXJKvTL3sEXdRoMIiwKHFPBZifaWQt4fyX-9-ecVVr7F27RAq2_K7IOByCYgcy8rltHf_GruZ01JsiIaRRQgY2MCcn1Vyc5ejCsRStHZGsM9II6L1HaEQXIBj6rvSuD-V4LmKjUSc7OnYoZn7aqJmf0KWmqTWury6WwYx3ndgacpCqczGNVl1QUEWR_lcWmdG9o8UsUWhQn5Fr_sbDrFRhqVzPYHtzcLK8QTRFFv6SubZ1WR32PFgYuRCIMfNqZMTtCTcvPdVGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/693294" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693293">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWNlxoHoq9u_q8pbXNmFTSDfrIn4wPaoxMXvOgzsBMZNZ7N8I05RhU9mwQP_iNAD9GP8hZ76vTfsgFQ1S3bElnmPukacpIP91LxO48-znNnqyhUKSKxiheB2l5rFzzvQbwPYsJI0HAWlfth_OiSjLWfTPI8lz8DI7pY4pmw4ZR8vBsSDGyuLdifaBeKE2iLogBJ2urZB5UUAU2l8A6zUH1D9YaLpL7eZ8TeHYwTzZ603ksW_3GrSNjiOn2HZfih3lOvdrfgPC7SriDI2_ytJLkPM7WgrDuRN0tTlAopo0Yx1b5chKatbfK0zbsXZJKCCFK8ehyW-tGptymXwWBYT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صالحی: فصل جدیدی در روابط فرهنگی ایران و روسیه شکل می‌گیرد
🔹
وزیر فرهنگ و ارشاد اسلامی در دیدار با وزیر فرهنگ روسیه در سن‌پترزبورگ، بر توسعه همکاری‌های فرهنگی و هنری میان دو کشور تأکید کرد و گفت: با برنامه‌ریزی انجام‌شده، اتفاقات بزرگی در ارتباطات دو ملت بر پایه فرهنگ و هنر رقم خواهد خورد.
🔹
سیدعباس صالحی همچنین اقتصاد فرهنگ و هنر، تولیدات مشترک، برگزاری رویدادهای فرهنگی و تقویت همکاری‌های آموزشی و علمی را از محورهای مهم همکاری ایران و روسیه دانست.
🔹
او با اشاره به ظرفیت موسیقی سنتی و نواحی دو کشور، آن را فرصتی برای تقویت مناسبات فرهنگی ایران و روسیه عنوان کرد و امضای موافقت‌نامه تولیدات مشترک سینمایی را گامی مهم در توسعه این همکاری‌ها دانست.
🔹
این دیدار در حاشیه سومین کمیته فرهنگی ایران و روسیه در سن‌پترزبورگ برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/693293" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203520b431.mp4?token=f9E-t_gFJUSn9gG13FCej6ZSC38vmYGewilE9Z6HZ_Fj2W2DnHSMPqdcORKc4_sgUz5QgmbvNrk2sCJygTQwmtJ_kSZ9lv_iMwS9kcCxuWcEqrmKzHj599nFhYMuua1vhrp72NEW7DFtRHqVc8w8l68nQN7CGlVeqmw5odnWv0v_iH4rynuG0VaPRwTgjUSEoKek0RrbT8-OSDvN_QyuNkoSmX6HL80TREIDeLNtDSVsyRw6JyPVTq4rB3XmyrruWyOv72ApVUdpdZIIOGThO6l9DduM4ihbir0j3Wj61ArDU6P8NeJNVgT2Bgv5ZNnD2vGbvgMFI_4E2d-8BkUMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203520b431.mp4?token=f9E-t_gFJUSn9gG13FCej6ZSC38vmYGewilE9Z6HZ_Fj2W2DnHSMPqdcORKc4_sgUz5QgmbvNrk2sCJygTQwmtJ_kSZ9lv_iMwS9kcCxuWcEqrmKzHj599nFhYMuua1vhrp72NEW7DFtRHqVc8w8l68nQN7CGlVeqmw5odnWv0v_iH4rynuG0VaPRwTgjUSEoKek0RrbT8-OSDvN_QyuNkoSmX6HL80TREIDeLNtDSVsyRw6JyPVTq4rB3XmyrruWyOv72ApVUdpdZIIOGThO6l9DduM4ihbir0j3Wj61ArDU6P8NeJNVgT2Bgv5ZNnD2vGbvgMFI_4E2d-8BkUMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین نتانیاهو به سران کشورها: اگر بزدل‌های دیگری در سالن باقی مانده‌اند، همین حالا خارج شوند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/693292" target="_blank">📅 23:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026e426b.mp4?token=advj7Sd-hBSo-P5nWlprWFgaf50RmbhmNDtdZlkmPD5yFxbAXSwpM7nwk-EBfs-w6vvH5IrjDwBH8uy6U5_Y7d9cgUbgavU98jiDPSuB09Yq3-eOwvUaMnZb_bBYDGx9aJpCXsrbamhX0dAEfIkoXweEiB4ksSg0KW8Y-pYItzx48kE8ZIcaZPsJSR8ReAWs79VJJ_G0n02DA9yVYEslj-nfLpn8aTNGwWq02bxCSpFMqmeFMmB1EVDKPBRs-a1oiIwRcpbSme_rRfkb9SCRF_WEYm7tzoswqmA6zUH8fvvJNCjRY9PgkxwrwerUfJ_IxtMxz6mz-LxXXzU94V-Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026e426b.mp4?token=advj7Sd-hBSo-P5nWlprWFgaf50RmbhmNDtdZlkmPD5yFxbAXSwpM7nwk-EBfs-w6vvH5IrjDwBH8uy6U5_Y7d9cgUbgavU98jiDPSuB09Yq3-eOwvUaMnZb_bBYDGx9aJpCXsrbamhX0dAEfIkoXweEiB4ksSg0KW8Y-pYItzx48kE8ZIcaZPsJSR8ReAWs79VJJ_G0n02DA9yVYEslj-nfLpn8aTNGwWq02bxCSpFMqmeFMmB1EVDKPBRs-a1oiIwRcpbSme_rRfkb9SCRF_WEYm7tzoswqmA6zUH8fvvJNCjRY9PgkxwrwerUfJ_IxtMxz6mz-LxXXzU94V-Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز سال تحصیلی در بعضی مدارس اینجوری بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/693291" target="_blank">📅 23:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWT-beOrb2BSJDRlJMUr_K5joBNu39eLHnKtJaYYipX_mYokC1e3bzvHyC6uSYxWKE1b2iQGTthEmJmYial9WlK_X6Dlvn4jZnkpTIjSA0J5JNsrEjosQ8DZYzDsQ16LcpTuM-QQnl_Ja90XZ4AC2LtgOdaVRnySbnMuxlY79xHtjHjDFbSYFW2fck4HVzHMb_X19jxxwoES-08Q89K27kGzxJwtarrgua8_hZDLguNZDqDXctC4miOh7G8MFOtlj7pdJUOZHdiyhVNTX7D1GR49-WB4ALoATr8KYsBy5D28WDaViFJMgHaiCXIzj_2V5jI2WiVKEoPNktfqgaLtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«چاو مبارک»؛ نخستین پول کاغذی ایران
💴
🔹
حدود ۷۲۵ سال پیش، «گیخاتوخان» حاکم مغول ایران فرمان انتشار پول کاغذی با نام «چاو مبارک» را صادر کرد. این اسکناس در «چاوخانه» تبریز تولید شد، اما به‌دلیل بی‌اعتمادی مردم و استقبال‌نشدن از آن، مدت کوتاهی بعد انتشارش متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/693290" target="_blank">📅 23:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d270ec2f.mp4?token=je01wXdotIGv6xkhEquFQnfcP19VaD4IgTXaoNwY1WaZXrH23KzYB88CXHtDKbZkHyE8MKsqjrQb5kQnxT-5ww1aoTl3VnU0C89bc95JLTicUJWCx2-YuyEqyUEsd_N9ie5a1WCFTInIIJCjXGP_YymZP2vY9bAtl2EjBr2-VVMZ7CWi1PDuqPumdsfwX0-32qX1dAFS6rDaxDslpgp0PpWsoC-JaQYK7RP8y-rEaYoMUZd3_kF8oTrlwD4_WE3IB9wQ5xn_BX0xJtjeFFKn8DXJWwu4FiIxZZE5zSjWakZoonAeLIrzeEul11Yg0yyWKKzZOd3XHyrIvMyUIFhRjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d270ec2f.mp4?token=je01wXdotIGv6xkhEquFQnfcP19VaD4IgTXaoNwY1WaZXrH23KzYB88CXHtDKbZkHyE8MKsqjrQb5kQnxT-5ww1aoTl3VnU0C89bc95JLTicUJWCx2-YuyEqyUEsd_N9ie5a1WCFTInIIJCjXGP_YymZP2vY9bAtl2EjBr2-VVMZ7CWi1PDuqPumdsfwX0-32qX1dAFS6rDaxDslpgp0PpWsoC-JaQYK7RP8y-rEaYoMUZd3_kF8oTrlwD4_WE3IB9wQ5xn_BX0xJtjeFFKn8DXJWwu4FiIxZZE5zSjWakZoonAeLIrzeEul11Yg0yyWKKzZOd3XHyrIvMyUIFhRjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داماد حسن روحانی: جلوی خانه کسی که به بنیان‌گذار جمهوری اسلامی لقب امام داد، قائم‌مقام جنگ بود، دو نشان فتح و نصر گرفت، ۱۶ سال دبیر شورای عالی امنیت ملی بود و دو بار با رأی مردم و تنفیذ رهبری رئیس‌جمهور شد عربده می‌کشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/693289" target="_blank">📅 23:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20257d6f8e.mp4?token=fynG-f4E0XUMYOxDcZMod6eacqm09893NgstdM982vzfkpaj4qjJQPVNHDvxmEGH-lX3MpcqsQm-XQBj62rGARD1h9w8otn-r1twGH-EP5bqodc_HMKCyKmAzKwKcAkETE4MzNGgqWJ-RWLk0k_U6s7_ljvtd3y_YqbS56meelADGF9CrZbO9VZTUmTD66djiebe2cL_fHEj1ckaVXXYTawxz2csGT-3TabMBQWLTJlovRRC-CxMrO7v4GMXiIB5WDHDHA2xDDBJIDx2yB81HnrRwpDWJKexpqImSUlKwNWrDC5q0SyNLNate9lzQ5Y662Zuky72wxFhCGVjCyPLpYfiafVHYCNSRJakUjlqKQMg3iYoffLryL4tYIFi_KKZ4HAdSl1arspzkH4rfL7qXttjemKFYi7Ujm_ujv9wxIu7N1dIIGaQYflyOwPBZureOSlrzokyghnhkcAN3UsByjKIAIY-4LLu58bYQ5qRqPyRGs3vrf_NRnJ1B0BZOqc_BtAVFHjwcZR_HE5WY8UfSGg5d-W1vZfDOOqgihWENqrTbVlyvoFmKJJmHiMUySWA3DBBoC0VXhEkGwTuA7oT5GKBZE9T30PYm20vJJE72ftlhBK3Na0XUowlZGC0hsbsrh04fdp6ojnd_9bz4cuKvy-ruRN2VYXN3O7A7CXCY1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20257d6f8e.mp4?token=fynG-f4E0XUMYOxDcZMod6eacqm09893NgstdM982vzfkpaj4qjJQPVNHDvxmEGH-lX3MpcqsQm-XQBj62rGARD1h9w8otn-r1twGH-EP5bqodc_HMKCyKmAzKwKcAkETE4MzNGgqWJ-RWLk0k_U6s7_ljvtd3y_YqbS56meelADGF9CrZbO9VZTUmTD66djiebe2cL_fHEj1ckaVXXYTawxz2csGT-3TabMBQWLTJlovRRC-CxMrO7v4GMXiIB5WDHDHA2xDDBJIDx2yB81HnrRwpDWJKexpqImSUlKwNWrDC5q0SyNLNate9lzQ5Y662Zuky72wxFhCGVjCyPLpYfiafVHYCNSRJakUjlqKQMg3iYoffLryL4tYIFi_KKZ4HAdSl1arspzkH4rfL7qXttjemKFYi7Ujm_ujv9wxIu7N1dIIGaQYflyOwPBZureOSlrzokyghnhkcAN3UsByjKIAIY-4LLu58bYQ5qRqPyRGs3vrf_NRnJ1B0BZOqc_BtAVFHjwcZR_HE5WY8UfSGg5d-W1vZfDOOqgihWENqrTbVlyvoFmKJJmHiMUySWA3DBBoC0VXhEkGwTuA7oT5GKBZE9T30PYm20vJJE72ftlhBK3Na0XUowlZGC0hsbsrh04fdp6ojnd_9bz4cuKvy-ruRN2VYXN3O7A7CXCY1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس مسائل منطقه در شبکه سه: اگر امروز در مقابل محاصره هوایی اقدامی انجام ندهیم، قدم بعدی دشمن محاصره زمینی است/ می‌توانیم بین پروازهای غرب و شرق جهان دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/693287" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سخنگوی ارشد نیروهای مسلح: از ترامپ و نتانیاهو و دیگر قاتلان امام شهیدمان نخواهیم گذشت؛ این موضوع دیر و زود دارد اما سوخت‌‌وسوز ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/693286" target="_blank">📅 23:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8Bj-t-HnScK4DicPB5E4sWvMba1H9q5FdWjXnxxe-p3u01N4cgFVDbSBnVjP3aK9Og1sHqW87wEnNgMYpK2fqRAUqKJOuQ7rIfbo8n7d5PFcosN1oV8V-IqVbWt1fISMqUFNRA1KAwfO-xKBt-ieINuek8jvLQZRCvWeR2hwTYDDg1j_PBdgM3nTl2knwK1uoX4MxV_5gXs2bF02x4m6mSscjKIQhvq6cX-ATssV1sYv8ZjFpdRhGCpelSN0UN8E7oXXBF3__eYlP102XyVTRtnapbuDUIQ2y2wEqftYjI1WZMSgfPpdI_4OahBRdwepl9DAbluF8hk5G9WJaeF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrzKUs7MKJ6wEwnOdhP6iMtwUfOhJIptNPwVDmbE0SOoGI4Q-svKCgmSsIcrd8IQrBWEMk7ewH01jFrtbz_2zE6YoJs4zMsZAJmyttReWclp1tIvTQnmWM8qzan9cp_Jo9wSnYZDZvQmD3meszqBRUYq2n4PMGHiG8S3NUkzzPrhZCq3OIRRMMoL0o2qhKGn8lcqSmF9bcYklPI8Ocs2ZNBdQ0wHRrSo3VsiPd0azi3K3da9nUf3koIpsw6iX4QNEe6PkxkhIU5TDWq1zhxfkTizEKYSOMFU5gHiuYo5wfsoTiZF-cCYBdRPmQHkpX2f_gcJvHLpHJlyZwe2l2Xe9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRQBBn4StQ5weNELVIxbQKDsVjVL_8gHiJXLM-uimwod89eg8QfL_wKh5X5CI1oPVaYFYCt1ZbpdXtv9e9yg6tqG_FFmnzklfr_vD_50wY20LWUXF1Z1ltU_l3vwR5aLwIxp5yUUEzqWH2rMGfIXkQ-2VTtBZA3ktSQuOseRsb9HmU_gUL_Bep5ZWj1s8lA7An8t8BlBLoME2ip4pKnvcOlX7fTOWUuj-3nTiMUk4lNZ9Rm0TJjMLYN2Hr8tKdMTSD6wq8bKwzWcm8DNOAHNHO8rIV3YXpHxESmoObV_QtyQGkFIchPzj1jN9zreBJlxgMXetHTrcBWiyPTbq4HySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPDO897mdJqr1r2I98jdb3mT3ZW1EQEq4ezYu7H34CRk3f6LWCrR5bAGLDDsZrSnxYMnGPhMaT2ibZ0x0TYWj-Rg5w8QVW1se2nyzuv7pNdkZ7e8su9ledAbnp1406bAqpEDBQyGcg72CODiwue2YSy73V6NPl-nMhNuubXinf9Hn07jrQYZ0o2fWaom9Z41lplMJ8fgCBrF4A5KKRW8fT4wtZC9RBrWtTHi-l5UwNny4EGSovRBq3p_Widm6r7gE8li3qM4TkIob_mUj4VVjN8bPkJtp1pR-XkqRoMYQNnSU1ND-flD6qA9DLB_9VPA-gxVqC6Rq2pvsYbM-X-qMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-aLxRNzViX0jC54HPzvTNHnaiC6k05f7pTT-VzXLvlTC0UQDCDgUE4XIXjZ7af9I2gmx76iXEOncQC07JaFtKlU_m1Z910_CLz-z8pJEnNX1eoHDw8gjvOijxm6ZyALWMJtWAUjRKQezhj7dNQKKPUdRURKJUXwuAaYG2FeZ-xkCX1-hxAjbgBnyhe_DRhbvygbggPedUU8WKF8KsDZ2U08Yo2vKRzj-OYHJSPVkvXabgA2oiCfiw1m_qA-3ow9PCV2FNtrCNGJh26yQRdhR14LNCGYiTyfkIAdaL-yV587ZFvJjpAqfx424LqcHDcgax8y_3GpCzct9_YEMBVZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzLC6EZT8dhJQEo5af93Zha30PF8RItoTxW1lnfSoCQoRmt8SVdr47L922YYCRCM-4p7nobIMG3ivYzZBqIy0i_kfTlYT0ewMo85zp-5UZpyXgo6lXkYbtDgZAd3aFA_xyeX-x7QWsC9QQB7giNEHWfJ76Jom61AAMsDzqe-CRLw-bi6BgMv-FWAdMNt26DFwoT6wJwvPn0RvaS0q-mu9vxsBYhR6jtaItLBrhJ10ihxDRCIV6PkvAoiEe75fIoSxQTJo1MD9kWc-Ax40JtWAAKCiQOQHd-aFrSMOyIArEKdM7EQE2kd3TgDFpIwYJqzUXkzMCJ9Obw9xJWBVrIrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQaL0YSnUfL7jBZZgAJ3Jploc1PSYpF7H2pzZ8RwlT6lWgj7_HfV9r_h34YT5sxXLGUoo1B5KsJynkpT4zVfKDV1kvDQq_8x-h4mQ8Jby8fcH6Q3UkJYU6QAX7Fk6ysDOe7mqQah4WW1eCvsat6MBgOQy3ytAZaxYwcUbnv96UkcxyiQIe5Q3RDqXNZ1ntznwplxasLlecsFZRQAdiMPau7KPzC-8ziybM7nQ3-Gwyl-HL7TuZd08rwhLmmAnrgElICwApm4U1zU8ehV_O5hbMdGYOV8kYPSdO1At9UdGEOXFnmfmB7vxeX7RrnY8B2PMWa6hM26ifhRmFfm6BhkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW7csjOY4ywSdEO5-KDGtMWSRbwMFDkAP9__TNWLMX4oreMSjQBFgs5InUUtW5Tj2y0KtmuLLdOcvPkyn7VxDvmXHVpSo9qc8M9zbZLFkJMI3WUCxVoJMawjUzIbeUEXy4baPH9f7-3x6lP2c4IZIbfXoqBadyyShyV6kbz38nDcwXfBTbXlxboK1VEBk99ph8RFe2DuUGkRNIzm7349sb-aNHy98bWXoaZpHHW4X3TvnNshknLdrcx4TimQJGd0uPAS42a1FFoTHPXggbce9uDap6RTVHWKn-82jYDZdTOXheclqe4reUIetPy-IuripbJX_f4y0QOo7zAzMZphtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YT77lV-24GBEsHSXyKvu6iy_vjsm3RZF3TB9wutRX3tuJMgVDpn5IQUiT3TmYlPxW5fbaf_70H2ccJ0C16dlx8xBRY9GIpKmIoN7qNFjJR91LVjq1dMQD132bEXf79WgjfXtqpOcvdYtcCB5tOlhZ-JwJPW5RBwfilgr2QWxxBD0WSE4kW1PelIDzpCQDOKrJrH2srw13txnz-seYkHXG-n8lQVSc50QE4-RlxNBfdh2Q8NhUpMDXq-2cTeylW1h6tqGmEa6JdQQafn-5mXpXfBaV7WG-JJWI5QgfWDZYlrRTfmJc2ekEDDtCDxm_MbILl7FpkeqxES590frTvzVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bF1HntQB2oqEubK2OhErDOX6LA0ODRFs1HERIAnDM0fXY1mAS3p2ngi6lz_JcDtIcd4F2QtWhCWKYfDBCd4hSb7XD9eLVSDww-cD4d7s2b1LTvgwVVC0g8Hs8QgzUOHgu55EzucJo2_Qgs_USXBSaT7AAqSBPmA7H2R7TcZcUqOQWZpho_Oa8Fu9zA_4wF7z_W_MNTpNUyL2KFgnZuvP7f0s4zTeE2V50L9Bc6caJOy0Ms-JF8bQPMiDA7fvDHjpHSI1n5G14jetFw3RXufag_Rv2D5mxaqOnmgKd0beF2wUYMxrWME5y7PN_39WP4RR1rgX3yHsDGe2CHCqL8ofcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۰
تصویر جذاب از ۱۴ سال کاوش مریخ‌نورد ناسا
در سیاره سرخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/693276" target="_blank">📅 23:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693275">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4c438769.mp4?token=Vxc6nE6wtXidRuiseqrbqQH6U_-9hhrDmkzEhVM2NlVqs_KoZ9UiEtUtuMJnRhgRPjcFehyyynXfvTCP1AQ6WsyZtFhlskWU7K9OkTQz1PuaYUyX15WGlPx1Oqs-UvDIXoIASNMCqmUWbbViPQzhvEUcuj6ODkN2WcLZlgFqNjQA9RkbMCdATqZVa3SShc2X4N3vgqtRR9-waX3KVcBDB0uXQ6u_P1_22o1aarbUvLqUkErH3qjxxRdvd8r7hQz086VP3AZChcDo18c9VBbiFKzZ_a37J10FaMzTSvx3-Qa9XqvYwQykMdrqgTnTtfc8R7EVpN2AvwQp7CYVB_QW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4c438769.mp4?token=Vxc6nE6wtXidRuiseqrbqQH6U_-9hhrDmkzEhVM2NlVqs_KoZ9UiEtUtuMJnRhgRPjcFehyyynXfvTCP1AQ6WsyZtFhlskWU7K9OkTQz1PuaYUyX15WGlPx1Oqs-UvDIXoIASNMCqmUWbbViPQzhvEUcuj6ODkN2WcLZlgFqNjQA9RkbMCdATqZVa3SShc2X4N3vgqtRR9-waX3KVcBDB0uXQ6u_P1_22o1aarbUvLqUkErH3qjxxRdvd8r7hQz086VP3AZChcDo18c9VBbiFKzZ_a37J10FaMzTSvx3-Qa9XqvYwQykMdrqgTnTtfc8R7EVpN2AvwQp7CYVB_QW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس نظامی: تمام کشتی ها را میزنیم؛ به جز شرکت ادنوک امارات!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/693275" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693273">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
علی‌رغم ترک صندلی‌های سازمان ملل توسط سران کشورهای جهان به صورت گسترده، نماینده شیخک‌نشین امارات در سالن باقی‌ماند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/693273" target="_blank">📅 23:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693272">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5ad2cef4.mp4?token=oD9u200ZwOMZ8k-aXMPj6_xbzd6zWPYp8HAVKRkBmK7agURAjEbSdMBZIsfrhGJXK5pTZ-jRBg8K--EjJTMtooJXonKoArDXxcf1VwYvBg04d6PNFvKqICs8pbv-LmBbjCFknxxacQq-mfOcCA-h9HRuYtx4ZiTmFJzkjI2NfbNaNFDFSkW0fDU-OMupelyumUsDDgVv2GZuC8KlCq4ha4VqRYaO9sygJh4HGYQw3xrXU_PGHHfgHSn01YRNgL4qxaxktPEG0AW1FFYHb5hTZ3kYFFkegUtXwNeWI12ra-lS6ElB04Kb_Rd8GVwc-losZqnKVF3Gs0Txl1kzIlKrA42Z82B9DYvCT_EI-R8RO0RtPMooHvY4Aqd3t-xHgS9a0xymweKGyngU2hzvq8dxvvAtZ_o_PIc9BGomm2yG-dtvmzqR6xqaoIYG0YWK-ZvHlYLyZT2wmLbLm5UbvzI2PcOVMg7XQdJu8rSuFcpyFq-wMNDll7BCwNeQIKvF_xIk3ANdSLzlBP1qieXppeZECFvVkcO1DakTh2r6ZPVLKtqxwfh0v5r6GYMx2BWZxOAO6t3YvBLJwfgSoRY1xdDyYcA2kufKPEQzKRBpivxJXBbIkWbkd-Hbzua4ZwbyhQbNudVUwd4poLGtaPBi1v4zrniqawgY-xAsOtzbPhKUl3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5ad2cef4.mp4?token=oD9u200ZwOMZ8k-aXMPj6_xbzd6zWPYp8HAVKRkBmK7agURAjEbSdMBZIsfrhGJXK5pTZ-jRBg8K--EjJTMtooJXonKoArDXxcf1VwYvBg04d6PNFvKqICs8pbv-LmBbjCFknxxacQq-mfOcCA-h9HRuYtx4ZiTmFJzkjI2NfbNaNFDFSkW0fDU-OMupelyumUsDDgVv2GZuC8KlCq4ha4VqRYaO9sygJh4HGYQw3xrXU_PGHHfgHSn01YRNgL4qxaxktPEG0AW1FFYHb5hTZ3kYFFkegUtXwNeWI12ra-lS6ElB04Kb_Rd8GVwc-losZqnKVF3Gs0Txl1kzIlKrA42Z82B9DYvCT_EI-R8RO0RtPMooHvY4Aqd3t-xHgS9a0xymweKGyngU2hzvq8dxvvAtZ_o_PIc9BGomm2yG-dtvmzqR6xqaoIYG0YWK-ZvHlYLyZT2wmLbLm5UbvzI2PcOVMg7XQdJu8rSuFcpyFq-wMNDll7BCwNeQIKvF_xIk3ANdSLzlBP1qieXppeZECFvVkcO1DakTh2r6ZPVLKtqxwfh0v5r6GYMx2BWZxOAO6t3YvBLJwfgSoRY1xdDyYcA2kufKPEQzKRBpivxJXBbIkWbkd-Hbzua4ZwbyhQbNudVUwd4poLGtaPBi1v4zrniqawgY-xAsOtzbPhKUl3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه در بازار سرخ‌رنگ بورس هم سود کنیم؟/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/693272" target="_blank">📅 23:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693271">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه ششم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693271" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
🔹
جلسه‌ ششم:
تفسیر دعای ندبه
🔹
دلیل تأکید بر خواندن دعاهایی با سند معتبر، این است که معصومین «نحوه حرف زدن با خدا» را به ما می‌آموزند و استفاده از این الگوها باعث اصلاح شیوه‌ی تفکر و باز شدن دروازه‌های استجابت می‌شود.
🔹
امروزه نباید به دنبال نوگرایی‌های شخصی در اندیشه دینی باشیم؛ فهمِ عمیقِ اصلِ دین کافی است.
🔹
حمد خداوند باعث می‌شود ذکر از سطح «زبان» عبور کرده، به «قلب» نفوذ کند و نور باطنی خود را نشان دهد.
🔹
وقتی انسان از درون با خدا وصل شود، دیگر نوسانات بیرونی زندگی او را افسرده نمی‌کند.
🔹
«پذیرشِ آگاهانه و سپاسگزارانه» نسبت به قضای الهی در دنیا، تنها راهِ عبور از فتنه‌های آخرالزمانی و تبدیل شدن به ابزاری در دست اولیای الهی است.
🔹
در آخرالزمان، پیچیدگی فتنه‌ها به قدری است که عقل به تنهایی پاسخگو نیست و باید زیر پرچم اولیای الهی باشیم تا به عنوان «ابزار» در دست آن‌ها قرار گیریم.
🔹
اسباب خدا شدن، حالتی است که فرد ناخواسته منشأ خیر می‌شود و با یک حرف یا نگاه، گره از کار کسی می‌گشاید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/693271" target="_blank">📅 23:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693270">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxdB-0oKbmGwETLqxQ_E2KRghEH0amFcc2iLS5H8b-VsyL2NlIBkrL9seo4i0drvrMXWDEJSIzpKuBXO2MnlVHhMIXYZx_iHDM3kb-FbAFp3Otdgj9kokFEhuC1do8uKNrI-mR0ix6u4HZZL5HAfOT8xDpwKSsixyHAFTP4lqYnZQKPh3WiPdaF18mVtcWKhvKzvizni5BZJDP-qYB9etEwSvifI03ZlOB55rRBy_nsqIbl_cn8OqvFo9L4wQN6HcHtLHk6xiZm1KeGGJOQ_XJa0Fkep5E11OFhMfFPOBrCBRbiuKQdB1zJc0Ds6oEpIryzZMOGzs9DhQS3avBO0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید بیمه بدنه، بیمه بازار داره!
ماشین‌مون فقط یه وسیله برای رفت‌و‌آمد نیست؛ یه
سرمایه‌ست
که با کلی زحمت به دست اومده...
برای همین،
بیمه بدنه
برای من یه انتخاب نیست، یه
ضرورته
که خیالم رو بابتش راحت کنم.
اما برای خریدش کجا برم؟
✅
راستش برای خریدش رفتم سراغ
بازارِش
!
چون می‌خواستم جایی باشه که بهم
راهنمایی
کنه و امکان خرید با
اقساط طولانی مدت
داشته باشه
👈
برای مقایسه و خرید بیمه بدنه وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/693270" target="_blank">📅 23:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693269">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cede7dbb3e.mp4?token=EqlopLluHHZzzUE0M9URFv24icFtIY2tQlEiGjnp179ajQM-4T5L7Sl_bL57ICQ_wR5bkz_IVHsaeyU92-yTjmsw-9BiFtEMgNP9wzwjbWkV_OfRK_wo4itKLsjRoc2htHfLnlAEj30vxCg67s_KCqKcMPqgeX8JPQWf4-jsOCYlfryBafFzaJit2Mqlb4RjseC1Fp9JE_beJyCahTbpBrShjqrcIjxYcgFGPKkvSzHngf9ZxChBXsObftokqzBqyW11EDrZmnPsiMETgmpJ675Oz0XGJT74Y5WwFxPDpPQJ9gCywGx3jN4lqxUw9kzwm6S9jsW0PxXgBrlIdWRpcGK9l6XJLB3JfHtwcXwUs1b4n_6Lk5jh1EIEX5bZuEL3oSSr7TqHJ7an7nfkH-YQWjCc0y0jpv-ksRrSsaOmh1r0XytDCYC3YEy0DCX_v6MNBgLfOkIOj3vN9eEisv3d_qM4nLuB1kwfFug5TteTCyEWLfEt4KVPgBvb1gjp_vOYBnrMoL8lgMcfZP50UBLeqw9mVXUvaaf_4cUteOt9RLaFY_QSlyZLeA0x3YA4m_p3aq68NudzGUzgr4jFzlYuShl8-w5kPFmDT50n3Ujk_LfM__xig3_mV5UCJQetxF4O_z-fWbhG_3uOsNREGGTFzhSJfQTHCRlK4a6dOrkPOcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cede7dbb3e.mp4?token=EqlopLluHHZzzUE0M9URFv24icFtIY2tQlEiGjnp179ajQM-4T5L7Sl_bL57ICQ_wR5bkz_IVHsaeyU92-yTjmsw-9BiFtEMgNP9wzwjbWkV_OfRK_wo4itKLsjRoc2htHfLnlAEj30vxCg67s_KCqKcMPqgeX8JPQWf4-jsOCYlfryBafFzaJit2Mqlb4RjseC1Fp9JE_beJyCahTbpBrShjqrcIjxYcgFGPKkvSzHngf9ZxChBXsObftokqzBqyW11EDrZmnPsiMETgmpJ675Oz0XGJT74Y5WwFxPDpPQJ9gCywGx3jN4lqxUw9kzwm6S9jsW0PxXgBrlIdWRpcGK9l6XJLB3JfHtwcXwUs1b4n_6Lk5jh1EIEX5bZuEL3oSSr7TqHJ7an7nfkH-YQWjCc0y0jpv-ksRrSsaOmh1r0XytDCYC3YEy0DCX_v6MNBgLfOkIOj3vN9eEisv3d_qM4nLuB1kwfFug5TteTCyEWLfEt4KVPgBvb1gjp_vOYBnrMoL8lgMcfZP50UBLeqw9mVXUvaaf_4cUteOt9RLaFY_QSlyZLeA0x3YA4m_p3aq68NudzGUzgr4jFzlYuShl8-w5kPFmDT50n3Ujk_LfM__xig3_mV5UCJQetxF4O_z-fWbhG_3uOsNREGGTFzhSJfQTHCRlK4a6dOrkPOcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✂️
ماشین اصلاح GYT-999
✅
صفرزن و خط‌زن | تیغه استیل
🔋
شارژ Type-C |  تا ۴ ساعت استفاده
📊
نمایشگر شارژ + ۴ شانه اصلاح
🔥
فقط ۱,۳۹۸,۰۰۰ تومان
💰
قیمت قبلی:
۱,۶۹۸,۰۰۰
✅
پرداخت درب منزل | ضمانت تعویض ۳ روزه
✅
امکان پرداخت قسطی با ترب پی
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/693269" target="_blank">📅 23:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1e64dfd8.mp4?token=Ypy7ycSku3juRXZHzk5_PAnBweATX-b7ZmpDS7UWXcVprpuVgzgIfkP9rrBINmNmrzbmlXhwPVILhY4OYzXptW-dTH1qcN3n8UcZvdTX_TKOZoJ4y3hY9dzRNmoHrMhviA8wksHzPcd7WjczEj0crLlaIBghJrc-3WTXKXu3R0fSiM8jckQbCsl-YmcX9Kn0d1OX-i6OvfJjSi-BqwTTOiRYopcvDgxm2Hv_wz5eYewYdrINB3eG7mdIbcXIZq3jh3mAQubIiAcn2YxlCtosBgK_MSrN2c5NrcddCyLiu1H11FQQLll_8T9u1vTj67SxUWYUY45okfrEjyk9skZkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1e64dfd8.mp4?token=Ypy7ycSku3juRXZHzk5_PAnBweATX-b7ZmpDS7UWXcVprpuVgzgIfkP9rrBINmNmrzbmlXhwPVILhY4OYzXptW-dTH1qcN3n8UcZvdTX_TKOZoJ4y3hY9dzRNmoHrMhviA8wksHzPcd7WjczEj0crLlaIBghJrc-3WTXKXu3R0fSiM8jckQbCsl-YmcX9Kn0d1OX-i6OvfJjSi-BqwTTOiRYopcvDgxm2Hv_wz5eYewYdrINB3eG7mdIbcXIZq3jh3mAQubIiAcn2YxlCtosBgK_MSrN2c5NrcddCyLiu1H11FQQLll_8T9u1vTj67SxUWYUY45okfrEjyk9skZkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: ۲ بار با رهبر انقلاب دیدار کردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/693268" target="_blank">📅 22:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پزشکیان: برنامه بعدی آمریکا ایجاد اختلاف بین مسئولان است  رئیس‌جمهور در گفت‌وگو با شبکه الجزیره:
🔹
هیچ وقت وحدت در کشور و بین مسئولان و نیروهای مسلح مانند الان نبوده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/693267" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
پزشکیان: ما و یمن در حمله به خط‌لولۀ عربستان دخالت نداشتیم
🔹
احتمال این‌که اسرائیل این کار را انجام داده باشد تا اختلافات را شعله‌ور کند دور از انتظار نیست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/693266" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab28f65d1b.mp4?token=daZzj9BmOritgfyylXH4uha8TasUKNA5YD9X7OOE1T3gqDj2TwzaoU7WSX_DWjkjTsVeKgUkndGiNbvb1KPCL6qlzdCZ2Bvbctw9JsXJeY32Q5TW8BuaO8U6_Bb7Oev8d_-yGVkhTa2rFHZnsw_lbkc-zshG243GH0u-8mtsWBrSz9eEC-d1kLEE26qaNYnJNOj-FoOktZEl3OfY7deZ13lFz8cq_797by2-lAOIz9MuRMC9Slg6_Y8fPn75P7Aae2eDt3VZTFZH8EyJSBAfI8OftrrWj0Kxr4riP4pLzJblw4AwljNeHS1S7DWT7c-0knHfA0MFssTWrqSACKW05g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab28f65d1b.mp4?token=daZzj9BmOritgfyylXH4uha8TasUKNA5YD9X7OOE1T3gqDj2TwzaoU7WSX_DWjkjTsVeKgUkndGiNbvb1KPCL6qlzdCZ2Bvbctw9JsXJeY32Q5TW8BuaO8U6_Bb7Oev8d_-yGVkhTa2rFHZnsw_lbkc-zshG243GH0u-8mtsWBrSz9eEC-d1kLEE26qaNYnJNOj-FoOktZEl3OfY7deZ13lFz8cq_797by2-lAOIz9MuRMC9Slg6_Y8fPn75P7Aae2eDt3VZTFZH8EyJSBAfI8OftrrWj0Kxr4riP4pLzJblw4AwljNeHS1S7DWT7c-0knHfA0MFssTWrqSACKW05g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا باید از Projects در ChatGPT استفاده کنیم؟
🤖
🔹
به‌جای ساختن چت‌های جدا برای هر موضوع، می‌توان با قابلیت Projects فایل‌ها، چت‌های مرتبط و دستورالعمل‌های هر پروژه را در یک فضای مشترک نگه داشت تا برای کارهای طولانی‌مدت نیازی به توضیح دوباره زمینه کار نباشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/693265" target="_blank">📅 22:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بسیار کاربردی؛ ۱۲ ماه سال به انگلیسی
🔹
۱۱ دی (۳۱ روز): January
🔹
از ۱۲ بهمن (۲۸ روز): February
🔹
از ۱۰ اسفند (۳۱ روز): March
🔹
از ۱۲ فروردین(۳۰ روز): April
🔹
از ۱۱ اردیبهشت (۳۱ روز): May
🔹
از ۱۱ خرداد(۳۰ روز): June
🔹
از ۱۰ تیر (۳۱ روز): July
🔹
از ۱۰ مرداد (۳۱ روز): Augest
🔹
از ۱۰ شهریور (۳۰ روز): September
🔹
از ۹ مهر (۳۱ روز): October
🔹
از ۱۰ آبان (۳۰ روز): November
🔹
از ۱۰ آذر (۳۱ روز): December
#زبان_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/693264" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693263">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413608cbc5.mp4?token=Bo4mF-Gcrhc5uJDPcnBcFB_W4_AU2ZDoMKcD3qDCMnG2kYpKqfxlr9NfJnqx_RRcrozHpfTZ-VdSGoMdH9eq52m15T-RCFsO1Sg6jLNnHOsJT384jC9BXa6saqhmub9PY-KSR7vYQh98diLDWqIE98qc_nNzxS8RxURyWDDTOoczyxeI88iX1Papom-lPUmSl5hCCaNgsgS-Mz9QRu-3LJwGVJXD2r-FB0yvcl14Wq2h9AXvBxTbTfLT9I-OsxUVP8r9lgkxLJR-WZEr_e7Km37r9aPUw8c6t2R5Co8aAxABwsoNdzjj7ExYlR90kPGTwdPemLC2TtzVqgMlMnijSiamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413608cbc5.mp4?token=Bo4mF-Gcrhc5uJDPcnBcFB_W4_AU2ZDoMKcD3qDCMnG2kYpKqfxlr9NfJnqx_RRcrozHpfTZ-VdSGoMdH9eq52m15T-RCFsO1Sg6jLNnHOsJT384jC9BXa6saqhmub9PY-KSR7vYQh98diLDWqIE98qc_nNzxS8RxURyWDDTOoczyxeI88iX1Papom-lPUmSl5hCCaNgsgS-Mz9QRu-3LJwGVJXD2r-FB0yvcl14Wq2h9AXvBxTbTfLT9I-OsxUVP8r9lgkxLJR-WZEr_e7Km37r9aPUw8c6t2R5Co8aAxABwsoNdzjj7ExYlR90kPGTwdPemLC2TtzVqgMlMnijSiamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا طلاق؟
🔹
سراغ شما آمدیم تا از شما بپرسیم، مهم‌ترین عاملی که باعث طلاق می‌شود، چه می‌تواند باشد. هر کدام نظر خاص خود را داشتید؛ اما واقعا مهم‌ترین عامل طلاق چیست؟
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/693263" target="_blank">📅 22:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc810592c.mp4?token=omTbhJtL555KFEc1tfnbk7zhwt2pyaa6TCVtCdWsVCmbI6mZ2fhhoop2fHR4ovUvjC2HNuNJsB7rPWDM-tL21DMFuI0r1FRvYu2oBPO_Mn8-itKy0-o2IOiPlRwm1GXfXPRaLrNzrJwrFgSCVFK1WeJdmU1cl2u54DcLob0ZNtnJvNpcWCg9CF_TPMfau-OXtSehc4dTh-y9tJ6OOTeljNBoNxfCd5eBodXxWISt1OcaiC2bUFNvakvPtOCY865GMkZ-JARGfn43KTQ6ES-23pHXCjfUhLi-GDttiE5yDnVbQ8lNoxlSOKPFVUqhrYznwnJR-3wnJuBU1CUQtPLs_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc810592c.mp4?token=omTbhJtL555KFEc1tfnbk7zhwt2pyaa6TCVtCdWsVCmbI6mZ2fhhoop2fHR4ovUvjC2HNuNJsB7rPWDM-tL21DMFuI0r1FRvYu2oBPO_Mn8-itKy0-o2IOiPlRwm1GXfXPRaLrNzrJwrFgSCVFK1WeJdmU1cl2u54DcLob0ZNtnJvNpcWCg9CF_TPMfau-OXtSehc4dTh-y9tJ6OOTeljNBoNxfCd5eBodXxWISt1OcaiC2bUFNvakvPtOCY865GMkZ-JARGfn43KTQ6ES-23pHXCjfUhLi-GDttiE5yDnVbQ8lNoxlSOKPFVUqhrYznwnJR-3wnJuBU1CUQtPLs_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قیمت بنزین و گازوییل در استرالیا رکورد زده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/693262" target="_blank">📅 22:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ: امیدوارم روسیه و اوکراین قبل زمستان به توافق برسند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/693261" target="_blank">📅 22:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39ccd2db8.mp4?token=BpV4FuRezcF_jF5eQIxTLMmX_x7dZG8i_YGhz5u7x75Juiyu_qHsvb-rCteS5eQd8aYymUinzZrPCOfNJdmIrk8O7VmnmL-RQHFBZjaSMjXqWOZIcIpwKhJcR8AHAoLLvOq54brMVd8bZn47cONtNi1I7tH-a1LK-hvklehhwz0Fx_oQbq-w79qHpDSlnkCUVdECI2SDd0NjZyeJUo093279zwfKo1lsbTKqN0FfJYRyhLD6x4FFNZxPcxyz4RHvdjqQDlFA3qfTLcnpMRorSKuyHGFwaYqtX54jGIsf6sWUptaQ45877PnycCoxQqXbyg5QkwG-laijYLpXrade3Yj49Q2PaLGwiM0cPzOosfv8nlWuwPop-MKSSjgCUth-4N9O0XIf_RJjDnJiOlADNRfnrjen9eYGvuWQlQlWxkbCJ9UH4voeeMO0pJsToAEIdPmmFqLTBHltq1DiwIa_Py9cHQJmkc42Kk-CQxfqh4o13nHtiZ4FoCC34rqPjBfXj4RQp9LmaJzzHvibW6q3yvTVQqPzasdLoU5_IrD38DbzazqZRUjQb6cCXo3BIp-rAjw8nCScRhHa1oBgV2Q1ZVmaRimWKQYGScND5fFdXAQHmKLTPDlB7qSTKIB-YlbFitSHnBfP6CUKUyYydV9StX0C2eBmtMmo4XpmxiaL93c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39ccd2db8.mp4?token=BpV4FuRezcF_jF5eQIxTLMmX_x7dZG8i_YGhz5u7x75Juiyu_qHsvb-rCteS5eQd8aYymUinzZrPCOfNJdmIrk8O7VmnmL-RQHFBZjaSMjXqWOZIcIpwKhJcR8AHAoLLvOq54brMVd8bZn47cONtNi1I7tH-a1LK-hvklehhwz0Fx_oQbq-w79qHpDSlnkCUVdECI2SDd0NjZyeJUo093279zwfKo1lsbTKqN0FfJYRyhLD6x4FFNZxPcxyz4RHvdjqQDlFA3qfTLcnpMRorSKuyHGFwaYqtX54jGIsf6sWUptaQ45877PnycCoxQqXbyg5QkwG-laijYLpXrade3Yj49Q2PaLGwiM0cPzOosfv8nlWuwPop-MKSSjgCUth-4N9O0XIf_RJjDnJiOlADNRfnrjen9eYGvuWQlQlWxkbCJ9UH4voeeMO0pJsToAEIdPmmFqLTBHltq1DiwIa_Py9cHQJmkc42Kk-CQxfqh4o13nHtiZ4FoCC34rqPjBfXj4RQp9LmaJzzHvibW6q3yvTVQqPzasdLoU5_IrD38DbzazqZRUjQb6cCXo3BIp-rAjw8nCScRhHa1oBgV2Q1ZVmaRimWKQYGScND5fFdXAQHmKLTPDlB7qSTKIB-YlbFitSHnBfP6CUKUyYydV9StX0C2eBmtMmo4XpmxiaL93c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این فیلم آمریکایی، ۱۸ سال پیش مقابل دوربین رفت و روی پرده اکران شد
🔹
در این فیلم به وضوح از اهمیت تنگه هرمز و لزوم کنترل آن توسط آمریکا (از دید دولتمردان آمریکا) صحبت می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/693260" target="_blank">📅 22:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693258">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da4e0877ee.mp4?token=ABIdRJf0PeSeLvTrm7pOKx0FuLy6D9XEyicBfhvzhqpbJTYfIC85eufPIMHzGyAU2HvB6wjDDLK0XWqsKYv5MxKILCxSsLBFCJYKHZx04wTtjXnIg8JriyVuOL89lMKwL6f5mzbfygr4VGnPhOEJgm-bzuzMPb2NIlibcPA7VYSB9Oej8-EFK4Q9jsGTPhwF_jhPlqm_lFroVvRB7DjHrb1Su3ugrD5PHAhm4M73JOr_WvzlB6t7P5y3G_tlXRDrcG9xrix8MYi48HQsQA7fAFb9RaeF7z5qvA-JCcZvIJcoXILTtm49tD4S45dHlGMdUDSUkTCBg0r4edbZMJbNSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da4e0877ee.mp4?token=ABIdRJf0PeSeLvTrm7pOKx0FuLy6D9XEyicBfhvzhqpbJTYfIC85eufPIMHzGyAU2HvB6wjDDLK0XWqsKYv5MxKILCxSsLBFCJYKHZx04wTtjXnIg8JriyVuOL89lMKwL6f5mzbfygr4VGnPhOEJgm-bzuzMPb2NIlibcPA7VYSB9Oej8-EFK4Q9jsGTPhwF_jhPlqm_lFroVvRB7DjHrb1Su3ugrD5PHAhm4M73JOr_WvzlB6t7P5y3G_tlXRDrcG9xrix8MYi48HQsQA7fAFb9RaeF7z5qvA-JCcZvIJcoXILTtm49tD4S45dHlGMdUDSUkTCBg0r4edbZMJbNSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشریۀ اکونومیست: آمریکا از خاورمیانه خارج می‌شود و ایران ابرقدرت مطلق منطقه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/693258" target="_blank">📅 22:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693257">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدپارتمان آموزش های مجازی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9ZiBwHyHgidBy_HA6n3tBb4aP7HrF26Udqpp395R0bFojYW53YnwwJaJw16QMG8-RBz30Ph4I6JznTfNpt5Tqv6bImZe0DAwAz_N7ZU_KySIdXo1i6SCZkuLIbHUUr-DCDAoIiTpznBdYDMtr4o6Txciv4aQnAno0PLQPP-JASdma8W6HADnAelUEP8I0kxl0WroTbM4YBMdgucvSQDiBvcY9Ow5JKYASJg3rU6Lpt2qocSjWgotbf_YTE3z8x3JE-mzgHr6HvV7ceoAMnpy-p-H8aqgjfqEcJshRKp80EeIyr-ThZQtgSM0BgoNXASVk9X76A04yB22OgTW00Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
فرصت جدید ثبت‌نام ICDL آنلاین!
💻
یادگیری کاربردی
🎥
دسترسی به ویدئوهای کلاس
👨‍🏫
رفع اشکال با استاد
📜
مدرک معتبر مجتمع فنی تهران (قابل ترجمه رسمی و ارسال پستی)
📅
شروع قطعی:
۵ مهر ۱۴۰۵
⏰
روزهای فرد| ۱۷ تا ۲۱
🚨
ظرفیت محدود!
📞
02634127 داخلی ۱۲۰
📱
09032648676
🔗
ثبت‌نام آنلاین:
https://B2n.ir/kj1017
مشاوره و ارتباط تلگرامی:
@siam_lms
کانال دوره های مجازی:
https://t.me/siamlms</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/693257" target="_blank">📅 22:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693256">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c55df22d.mp4?token=SmX7M_vpvcwJ40qK7tWL-hhXpU1svgjySTzJzTq0Yn7jOSwVq2RaWIJEgWu5QbDv4HSb4t-C2H3vd955OhDBL5KEPn0IYczCdqVL8vJpLqW83gDSV0gwmsLCxiWBF9kPsbUUrDNHpCG58Hwqoe4dCVQA7blnHSKxcfkZ5hmi1TkuYI4XhUcwckdP1Id0SRDS5FA4GBsQ8gE3VR6VOdbCZhKYjtDIHop1_xCkODE9r42HQfLFOWEDTS3m-AyKc_iG7pw7kCLYAd5rwYmq6n-sWJDk5pJob5r3ewogGzprv2_G6LncMH_1fxgtyIrzgLi-e77GMF3aLxoVHiHZ23CScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c55df22d.mp4?token=SmX7M_vpvcwJ40qK7tWL-hhXpU1svgjySTzJzTq0Yn7jOSwVq2RaWIJEgWu5QbDv4HSb4t-C2H3vd955OhDBL5KEPn0IYczCdqVL8vJpLqW83gDSV0gwmsLCxiWBF9kPsbUUrDNHpCG58Hwqoe4dCVQA7blnHSKxcfkZ5hmi1TkuYI4XhUcwckdP1Id0SRDS5FA4GBsQ8gE3VR6VOdbCZhKYjtDIHop1_xCkODE9r42HQfLFOWEDTS3m-AyKc_iG7pw7kCLYAd5rwYmq6n-sWJDk5pJob5r3ewogGzprv2_G6LncMH_1fxgtyIrzgLi-e77GMF3aLxoVHiHZ23CScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای یک رسانه ترک: عربستان خط لوله نفت شرق به غرب خود را دوباره عملیاتی کرد/ احتمال ازسرگیری صادرات از بندر ینبع نیز وجود دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/693256" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693255">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
پزشکیان: دیدار با ترامپ چه مشکلی را حل می‌کند؟  رئیس‌جمهور در گفت‌وگو با شبکه الجزیره:
🔹
وقتی آمریکا به آنچه نوشتیم عمل نمی‌کند، دیدار با ترامپ چه مشکلی را حل می‌کند؟
🔹
نمی‌دانیم بر اساس کدام قانون با آمریکا حرف بزنیم که به آن عمل کنند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/693255" target="_blank">📅 22:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693254">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/693254" target="_blank">📅 22:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693253">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8de0a4b3.mp4?token=km-1dPs-LXUIH2Gmo47IbcK2uCCT5efNc82UbpKF7g5WVIu4IObZcf9_eh-x_nCAWKhOHhAIAJYZcBbT1a0ugN9AOzPtu5BPuhgcg8WO2Z9hIdSnEJYzQ8mu3J8LNlcejzHPwxu9Gb3MJ0VtbYg2hnLQjso-xD-f0q-Igd2Hx1f2I35297IQC89JAQzeFs8ruNLCkCxGPA4iB--Bsg0Og5cl-o2LmPs3HAFfcE44ma3zdJywzUzvi9sI01Z7R_JgEYujA0dxwPCncaYGiFiq-Q8HdHY6V-hMAkTlcF0a0Cur5d0dz2LlQmPev3iEA2m9ZxjJrmUl7LcGEA5B7RnBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8de0a4b3.mp4?token=km-1dPs-LXUIH2Gmo47IbcK2uCCT5efNc82UbpKF7g5WVIu4IObZcf9_eh-x_nCAWKhOHhAIAJYZcBbT1a0ugN9AOzPtu5BPuhgcg8WO2Z9hIdSnEJYzQ8mu3J8LNlcejzHPwxu9Gb3MJ0VtbYg2hnLQjso-xD-f0q-Igd2Hx1f2I35297IQC89JAQzeFs8ruNLCkCxGPA4iB--Bsg0Og5cl-o2LmPs3HAFfcE44ma3zdJywzUzvi9sI01Z7R_JgEYujA0dxwPCncaYGiFiq-Q8HdHY6V-hMAkTlcF0a0Cur5d0dz2LlQmPev3iEA2m9ZxjJrmUl7LcGEA5B7RnBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نتانیاهو نتوانسته غزه را وادار به تسلیم کند، حالا می‌خواهد حکومت ایران را تغییر دهد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/693253" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693252">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
پزشکیان: تروریست آمریکا و اسرائیل است و ما قربانی تروریست هستیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/693252" target="_blank">📅 22:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693251">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با شبکه الجزیره: ما اعتمادی به مذاکره با آمریکا نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/693251" target="_blank">📅 22:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693250">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac92dad0c2.mp4?token=iw_4k8GeZMn696q3HkMWANnif78xcdhGkK8xztnM8HuFFOD_8Aqrj-dvK0D-5Zq-Sa8KtkxVIaRh6CTAOO05NQDw3Ivz0tEdKe1_EnRuOjsTOQrB4hKDwBKtAdT9ob2Tebbs4wWib2ISgKdVjDt65OW6lHhdLqEKeIVzBVdpGjKpyVMHFis29ToY93KcfLOFgZu6u_5aMaIKyQNrxYrAa_NKVP-f1JBybuUgv7hN41cOPc1iVtxfIMNgPyzyUgX8Ri5DICkgsl8Vwed69UtVaNsM8V5WxAdTOGsj2CXAPMQdRI4b74ZGLL8mHmkBVceGu0owGjW149SM1iwgQVJJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac92dad0c2.mp4?token=iw_4k8GeZMn696q3HkMWANnif78xcdhGkK8xztnM8HuFFOD_8Aqrj-dvK0D-5Zq-Sa8KtkxVIaRh6CTAOO05NQDw3Ivz0tEdKe1_EnRuOjsTOQrB4hKDwBKtAdT9ob2Tebbs4wWib2ISgKdVjDt65OW6lHhdLqEKeIVzBVdpGjKpyVMHFis29ToY93KcfLOFgZu6u_5aMaIKyQNrxYrAa_NKVP-f1JBybuUgv7hN41cOPc1iVtxfIMNgPyzyUgX8Ri5DICkgsl8Vwed69UtVaNsM8V5WxAdTOGsj2CXAPMQdRI4b74ZGLL8mHmkBVceGu0owGjW149SM1iwgQVJJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با شبکه الجزیره: ما اعتمادی به مذاکره با آمریکا نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/693250" target="_blank">📅 22:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693249">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
پزشکیان وارد تهران شد
🔹
رئیس‌جمهور پس از پایان سفر به نیویورک و شرکت و سخنرانی در هشتاد و یکمین مجمع عمومی سازمان ملل متحد، وارد تهران شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/693249" target="_blank">📅 21:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693248">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581bd5215c.mp4?token=CuA31kqaBseKXlLhiptMFVw8pqQNyIqVGG8FKInS0avgLg15AjdaSH5gQuzbxTVWucSg1JfI1h9gSDfvsO9-s91G9P-FHB3I9eFHJLnnF0LHj_bM1LJlH54yEjMGv4pu2hp14Owum0-CVOyiiaTLGRa6OHgORiWQYEfD7nytyVrBCTbUR7ESIJkOOmRnWzu81s3FmRIFRLYyKgUAN9pj7BYbVtWaoF_0ZmYlvPH00VXHCKHjEQt2M1Lx9H-49jREfJQasaguJ-7pfDJ2uDhWyF4J_YVv9eM3jjkxkURggcNrEfvLgWQ8A1KRM-02Llv_HvSJZImqjoD6Bdms46gKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581bd5215c.mp4?token=CuA31kqaBseKXlLhiptMFVw8pqQNyIqVGG8FKInS0avgLg15AjdaSH5gQuzbxTVWucSg1JfI1h9gSDfvsO9-s91G9P-FHB3I9eFHJLnnF0LHj_bM1LJlH54yEjMGv4pu2hp14Owum0-CVOyiiaTLGRa6OHgORiWQYEfD7nytyVrBCTbUR7ESIJkOOmRnWzu81s3FmRIFRLYyKgUAN9pj7BYbVtWaoF_0ZmYlvPH00VXHCKHjEQt2M1Lx9H-49jREfJQasaguJ-7pfDJ2uDhWyF4J_YVv9eM3jjkxkURggcNrEfvLgWQ8A1KRM-02Llv_HvSJZImqjoD6Bdms46gKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تورها وارد فضای عجیب و غریبی شدن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/693248" target="_blank">📅 21:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693247">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
نگهداری طلای پلتفرم‌های طلا در بانک به معنای خالی‌فروشی نیست
🔹
رئیس اتحادیه کسب‌وکارهای مجازی با اشاره به حواشی اخیر بازار طلای آنلاین گفت: صرف اینکه طلای یک سکو در کارگاه یا بانک نگهداری می‌شود، به‌معنای خالی‌فروشی نیست.
🔹
الفت‌نسب تأکید کرد که در بازاری که معاملات آن لحظه‌ای انجام می‌شود، نظارت هم باید لحظه‌ای باشد؛ یعنی موجودی طلا، تعهدات و معاملات سکوها به‌صورت هم‌زمان قابل تطبیق باشد.
🔹
او راه‌اندازی کامل سامانه نظارتی طلای آنلاین را یکی از مطالبات جدی این حوزه دانست؛ سامانه‌ای که به گفته او می‌تواند ابهامات را پیش از تبدیل‌شدن به نگرانی عمومی شناسایی کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/693247" target="_blank">📅 21:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
فوت موجر یا مستأجر قرارداد اجاره را باطل می‌کند؟
وکیل دادگستری:
🔹
در حالت کلی با فوت موجر و مستأجر قرارداد منحل نمی‌شود و به وراث منتقل می‌شود، مگر اینکه در قرارداد، مباشرت مستأجر جهت استفاده از مورد اجاره شرط شده باشد یا مدت اجاره تا زمان عمر موجر یا مستأجر تعیین گردیده و یا موجر فقط تا زمان حیات خود، مالک منافع ملک استیجاری بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/693246" target="_blank">📅 21:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7NJIjc0yzRP16J7KkuOfsaST7XHvb8FE5qWZF6zj1Ktf4rmfdacBF5n1SebioSAH4v5uQcf5bZ6BAcEjlKnkPxq3Xi0IMXw_ZUxgNTySn_gr0LMFP7TFMYrFZv5iefs0jkyND1aX_48MuwlHW0wWWBuxi7vqNfgOcEvekvjcRhzetXBqsqbr9Ko5P98esclQbdArymMYmZFC1CAEElwON-4swLQDC_Nx9xw1YHpkda3ppWVhMHFAHZK_U_c3WhWYFP2Wy8h4vv8Z5JRhwnWkK7z7Go_aqkYVGZiro2W38tU2ej12umF43wQAUBDgcGhqJtxNj39gM7mniVbCwVIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شناسایی پیکر شهید پس از ۴۰ سال
🔹
پیکر شهید «علی‌اکبر گندمی» از رزمندگان ارتش که سال ۱۳۶۵ در عملیات کربلای ۶ در منطقه سومار به شهادت رسیده بود، پس از ۴۰ سال در جریان تفحص شهدا کشف و شناسایی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/693245" target="_blank">📅 21:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bO4bIdkp4vLLGMGcLUBuFYWc5VwiFd6akxUXznDI3pyWr5GEeD8BwEfyZKnR-WLDDR5XbvKHqTY-uYlB36MDWIVpuS50jDOJNLvBKqRPrmbVx5dHE66j0gLu7bqry5YYz_4BaMyVFFBWiE9mqkMqDvISbyrO8V3iajr-l5EkufmnftlKRnT8gmnd9amh4DzYjXRZmlsOsxV749mqjSNNyiAwX18-TDrUFp4wIOIDCQXOqIh3X-GmEdeI3GsHTkmdyUZ2MK6qBsxWD6Mos_ugz9r1wCdsM4Sohij4SH5ZEuS1GuZlQHvFFCbH6cNDo6DIzFm7a6JFiT93nkzcCyPWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیر خاکستر
🔹
مذاکرات غیرمستقیم ایران و آمریکا با فعال‌شدن دوباره میانجی‌ها وارد مرحله تازه‌ای شده است. ایران پیشنهاد هفت‌روزه‌ای برای بازگشایی تنگه هرمز و ازسرگیری مذاکرات ارائه کرده و پزشکیان و عراقچی تأکید کرده‌اند که اجرای این طرح به پذیرش شروط ایران از سوی آمریکا بستگی دارد. هم‌زمان، گزارش‌هایی از ادامه رایزنی‌های مثبت میان دو طرف و نیز مخالفت ترامپ با پیشنهاد ایران منتشر شده است. رئیس‌جمهور آمریکا اعلام کرد که پیشنهاد ارائه شده توسط ایران را که به موجب آن، تنگه هرمز ظرف مدت هفت روز باز می‌شد، رد کرده است. با این حال، بی‌اعتمادی عمیق و اختلاف بر سر شروط توافق همچنان پابرجاست و اگرچه تحرکات دیپلماتیک به کاهش موقت سطح تنش منجر شده اما تداوم فشارها و تهدیدهای نظامی، احتمال بازگشت درگیری‌ها را همچنان منتفی نکرده است.
🔹
هشتصدوهفتادمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/693244" target="_blank">📅 21:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59247c96c0.mp4?token=ETHo85toPUys0yBgWT85JRYd0XfektwWe0FGSuU_6lLyn-VyS8WSDdCSVOmEGsXdD6e8xBhjXqqE3tQL5slRDxKCTskOQyFD1BR1NhCYvLbmT9IYuu-hr8eCyqsDiEofr40uKhWRs4k_jI7LaGuKHGlhz-PFnnprR14kFnuXS070hTgZqHJwSuf8-0HPcPZeQ4iTX5R7bg7iVZdRnYHZhIA7NXWYMyI9JsKUk6nHb7NHDNajfAd7W8iVc3GjW3Xl5uqngTTutKFU-UXiGW4SirhMWEG7ovU8IXrYyJvZ1RFevVKQpGe64MS7djSpxHBgfV3Wb9kZCEOUAR8hLc8wZ2qvXUy0jWE4cOKWQrS40orO-DDqJUkrSxcTH4wWPFYsKuVbi2bcX1vbZGkj78jrDdpj9ISFV0GXNruQf8sMv4auRKZ1Qu4BOszVdnztliBjAx0TlSW5wdWzYBp6NA-XFYgY0RrtsPbQfoLnQEU3OlPbxH-Eu3ahyYmtvz-WKosLUmKkaYX_vfP4o2ZMJg-o8soimSlF8CBJl_KvdgNHU7pYikDSsQI_0G4u2QH3re6AqT7op5vXzkbkv96oNAJZtJJc7V9BLYtln_fXnLGLBYumqiQOMqSS4XGvH-7kdfBlJG5cDBCGAcBoTkjEdIVRQIwyBSVhSqdWcCSqYMlqeQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59247c96c0.mp4?token=ETHo85toPUys0yBgWT85JRYd0XfektwWe0FGSuU_6lLyn-VyS8WSDdCSVOmEGsXdD6e8xBhjXqqE3tQL5slRDxKCTskOQyFD1BR1NhCYvLbmT9IYuu-hr8eCyqsDiEofr40uKhWRs4k_jI7LaGuKHGlhz-PFnnprR14kFnuXS070hTgZqHJwSuf8-0HPcPZeQ4iTX5R7bg7iVZdRnYHZhIA7NXWYMyI9JsKUk6nHb7NHDNajfAd7W8iVc3GjW3Xl5uqngTTutKFU-UXiGW4SirhMWEG7ovU8IXrYyJvZ1RFevVKQpGe64MS7djSpxHBgfV3Wb9kZCEOUAR8hLc8wZ2qvXUy0jWE4cOKWQrS40orO-DDqJUkrSxcTH4wWPFYsKuVbi2bcX1vbZGkj78jrDdpj9ISFV0GXNruQf8sMv4auRKZ1Qu4BOszVdnztliBjAx0TlSW5wdWzYBp6NA-XFYgY0RrtsPbQfoLnQEU3OlPbxH-Eu3ahyYmtvz-WKosLUmKkaYX_vfP4o2ZMJg-o8soimSlF8CBJl_KvdgNHU7pYikDSsQI_0G4u2QH3re6AqT7op5vXzkbkv96oNAJZtJJc7V9BLYtln_fXnLGLBYumqiQOMqSS4XGvH-7kdfBlJG5cDBCGAcBoTkjEdIVRQIwyBSVhSqdWcCSqYMlqeQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نگاهی نزدیک به طراحی متفاوت خودروی برقی عربستانی CEER EXOBOT
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/693243" target="_blank">📅 21:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e764cc31.mp4?token=DL3FEbZ1mxaPQ-et3gwgZVcsXP8cn6MIHFzrUXjTiTnuzmKDAAcxccVqRa2w51jv3YuNiqIYjvv6PTCmxXF6lL480fnpyUrNUDiWqxu9c8KAX_2AYsIlJxQJ6YeA0i4L7BKValv0iHa9jXlPEZvVUGHXCKzF4Stgj8v0bNf3s1Uz-W_FA7D18nWthEgxqQndt9KzkOqKzNW3RCtElCWbowaz18V7gBm2D4naNqx_uU_zJfd3tLS7IkLXNhz_TGBnCcDyn0iPHyfvXeNrDzCIMhGlYldZtq0KqEOSAK4puIbVcKSybfOdvlvlhH0xBRYeiVcm6yVPaAprrh44X4a9vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e764cc31.mp4?token=DL3FEbZ1mxaPQ-et3gwgZVcsXP8cn6MIHFzrUXjTiTnuzmKDAAcxccVqRa2w51jv3YuNiqIYjvv6PTCmxXF6lL480fnpyUrNUDiWqxu9c8KAX_2AYsIlJxQJ6YeA0i4L7BKValv0iHa9jXlPEZvVUGHXCKzF4Stgj8v0bNf3s1Uz-W_FA7D18nWthEgxqQndt9KzkOqKzNW3RCtElCWbowaz18V7gBm2D4naNqx_uU_zJfd3tLS7IkLXNhz_TGBnCcDyn0iPHyfvXeNrDzCIMhGlYldZtq0KqEOSAK4puIbVcKSybfOdvlvlhH0xBRYeiVcm6yVPaAprrh44X4a9vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خالی‌فروشی آنلاین طلا چیه؟
🔹
بعضی پلتفرم‌ها بدون اینکه به اندازه طلایی که به مشتری می‌فروشن، طلای فیزیکی داشته باشن، معامله انجام می‌دن؛ به این می‌گن «خالی‌فروشی».
🔹
طبق دستورالعمل جدید، پلتفرم‌ها باید طلا رو قبل از فروش به خزانه تحویل بدن و موجودی‌شون در «سامانه ناظر» ثبت بشه.
🔹
با توجه به تشکیل ۵۰۸ پرونده کلاهبرداری در سه سال گذشته، بهتره قبل از خرید، مجوز، کارمزد، محل نگهداری طلا و شرایط تحویل فیزیکی پلتفرم رو بررسی کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/693242" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
ترامپ: من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/693241" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2755b599d8.mp4?token=tmKn3s17WqWHd9U8HyEcFL7fbaUUJ9hZYdLElyuMCfq6a_5wSQuTdSluahnrQuLS_BWTPUohQcYH8Enj1d90QvqlJN2TWTxjbG2wkACOwFsVQngY6_51HaMHhHfVMNNSv1FStk7vkJVJI9x_RqI5tDSDgxB-BY26HPxqvzCg3ODXx6VbcblIz65pZlhrdae926CJZMx7ofbd_DjR64ZN8JMNR7MfkAdoPwyCm1AOSN-c9qW-CPZP6c_wFOxvru_WAGbiw8cqvffCKyyv818sOqpPj9_cwMfGE7AxvN_SO86Wj5DPc2gyM4pMW39GaQbVHUlV-5afMjavqf6kmaD_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2755b599d8.mp4?token=tmKn3s17WqWHd9U8HyEcFL7fbaUUJ9hZYdLElyuMCfq6a_5wSQuTdSluahnrQuLS_BWTPUohQcYH8Enj1d90QvqlJN2TWTxjbG2wkACOwFsVQngY6_51HaMHhHfVMNNSv1FStk7vkJVJI9x_RqI5tDSDgxB-BY26HPxqvzCg3ODXx6VbcblIz65pZlhrdae926CJZMx7ofbd_DjR64ZN8JMNR7MfkAdoPwyCm1AOSN-c9qW-CPZP6c_wFOxvru_WAGbiw8cqvffCKyyv818sOqpPj9_cwMfGE7AxvN_SO86Wj5DPc2gyM4pMW39GaQbVHUlV-5afMjavqf6kmaD_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت جنجالی ترامپ پس از دست دادن با زلنسکی
🔹
حرکت دست ترامپ پس از دست دادن با زلنسکی در فضای مجازی با عنوان «دست شاخدار» پربازدید شده است؛ برخی کاربران خرافاتی این حرکت را نمادی برای دور کردن بدیمنی می‌دانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/693240" target="_blank">📅 21:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693238">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
،
شنود
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/693238" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693236">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رئیس‌جمهور در مصاحبه با شبکه CBS آمریکا: ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد/ ما نمی‌خواهیم بجنگیم اما اگر بزنند، دفاع می‌کنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/693236" target="_blank">📅 21:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693235">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2ab6808bd.mp4?token=vOH6HwX9y8SM3GvMOBZEd2qvty2YxVPmSctP72V41N9ZZjFfT3M4QP11BldyjgFxjbLMONP3AdhTYw146nf6LTA6e446IKpG7b1eeYFlZd5kjRPHZ51pfKP9kMOHMH7ED9NLpnZxqaii77gFZEe9oym226voWBt37d87ZZ4DGg79uNX_kXYyEiIsY6138h-5bM73uW-Zl55x4Oeey9MDmRV_Bdzltp9nPhNa6oH__pgX4VFuUv0-7hb2Erl22PySZg6k-be3JvzLYepJ7AIFV0nyIun39AyK-T5Iu7z94vs4VdcT_uRIBxAYRiyAW48xCfBCsIqzkqzFide8x0yefjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2ab6808bd.mp4?token=vOH6HwX9y8SM3GvMOBZEd2qvty2YxVPmSctP72V41N9ZZjFfT3M4QP11BldyjgFxjbLMONP3AdhTYw146nf6LTA6e446IKpG7b1eeYFlZd5kjRPHZ51pfKP9kMOHMH7ED9NLpnZxqaii77gFZEe9oym226voWBt37d87ZZ4DGg79uNX_kXYyEiIsY6138h-5bM73uW-Zl55x4Oeey9MDmRV_Bdzltp9nPhNa6oH__pgX4VFuUv0-7hb2Erl22PySZg6k-be3JvzLYepJ7AIFV0nyIun39AyK-T5Iu7z94vs4VdcT_uRIBxAYRiyAW48xCfBCsIqzkqzFide8x0yefjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت ۱۳ همتی بانک تجارت از جوانان با اعطای تسهیلات ازدواج و فرزندآوری
🔹
بانک تجارت با پرداخت ۵۱ هزار و ۵۷۷ فقره تسهیلات ازدواج و فرزندآوری شامل ۳۳ هزار و ۳۷۶ فقره تسهیلات ازدواج و ۱۸ هزار و ۲۰۱ فقره تسهیلات فرزندآوری جمعا بالغ بر ۱۳ همت، حضوری موثر در حمایت از جوانان و خانواده‌های ایرانی داشته است.
🔹
این بانک با بهره‌گیری از زیرساخت‌های دیجیتال و سامانه باجت، فرایند ثبت‌نام و پیگیری تسهیلات ازدواج و فرزندآوری را به‌صورت غیرحضوری فراهم کرده است تا متقاضیان بتوانند آسان‌تر از خدمات مربوط استفاده کنند.
📱
tejaratbankofficial
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/693235" target="_blank">📅 21:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693234">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
آجرلو، عضو رسانه‌ای تیم مذاکره کننده: با تفاهم اسلام‌آباد ۸۰ میلیون بشکه نفت فروختیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/693234" target="_blank">📅 21:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
واردات سامسونگ و ال‌جی آزاد شد  سازمان توسعه تجارت ایران در نامه‌ای به گمرک:
🔹
با توجه به تصمیمات کارگروه ساماندهی مبادلات مرزی، واردات لوازم خانگی از مبدأ کره جنوبی دیگر با هیچ محدودیتی مواجه نیست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/693233" target="_blank">📅 20:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fa0a337d.mp4?token=DQoZA6UJ8jRSGQpdxkhvxCWuiyJ9-9x8ahhHd-iCgnoT8S_xCyz3-y7XYiEfaznf7y0i7KqW030duLTPeFQQpgvHEKeSCJxA1WzBPO0wvGDTeSPs_ie5PwOYtTVa0TpD6tbvZ9TyprC2arbzd5XZUD6DuTv3gmTD1bQC11czVKXuMXtDQZ3Kq-dUViHtdilbax1Awt5WhdjTbtPiItf6W91QxtQ94Qr-_EvqTAkJQkZtdW6gIOmpmEfe40enDkUcf4W3zfp4VAlJAMtIhlyXm0ZACrvHCd4KEcFjEA8ukfH-S35eVlVFmZud-7rIpSUH9sgIRPKmnOGiX3FIWHt3OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fa0a337d.mp4?token=DQoZA6UJ8jRSGQpdxkhvxCWuiyJ9-9x8ahhHd-iCgnoT8S_xCyz3-y7XYiEfaznf7y0i7KqW030duLTPeFQQpgvHEKeSCJxA1WzBPO0wvGDTeSPs_ie5PwOYtTVa0TpD6tbvZ9TyprC2arbzd5XZUD6DuTv3gmTD1bQC11czVKXuMXtDQZ3Kq-dUViHtdilbax1Awt5WhdjTbtPiItf6W91QxtQ94Qr-_EvqTAkJQkZtdW6gIOmpmEfe40enDkUcf4W3zfp4VAlJAMtIhlyXm0ZACrvHCd4KEcFjEA8ukfH-S35eVlVFmZud-7rIpSUH9sgIRPKmnOGiX3FIWHt3OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یعنی این جنگ رو ما خواهیم‌ بُرد!
🔹
جملات طوفانی شهید آیت الله خامنه‌ای خطاب به مجری آمریکایی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/693232" target="_blank">📅 20:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693231">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
مهران مدیری دوباره راهی اتاق عمل شد
🔹
مهران مدیری برای دومین بار طی دو ماه گذشته تحت عمل جراحی دیسک کمر قرار گرفت و ادامه تولید آثارش فعلاً متوقف شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/693231" target="_blank">📅 20:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693229">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3053de3fdc.mp4?token=MQu6EzxyBPvgC-0zZYPx_t1rf4T1rEMlOvsDT2PO98SwAhuW6NUHcpi_PFnJpsh8-noMvIHTOpRsQYW1psU3SMqXgYxpfDaQYKRlgF-iMbSw9MO1ZXpcpgHaiWoJYOnOAcwFPfdd5HDLvp1KN8OoFJnzCTdzTkJbntTkJgN6U94g3qJczgiZJl8a_XjUqhM6ZYAVWh1AwYwm42LjgykAgEy6iDpU8UcPcetdnQBXc0JTLvb2xW5FXA7y12BiU6PI7dOnVAHeFEkbCxPoebtvDE9xZUOc11njQQ4eCDxN54khdE-XQR5sFX9rvmWwRHkt6pBRkafr7MLzE9NbFV0jGBlgpKbOGaI4OIY16jRTlrP6fmQByaPN_x0GFE77_jlilvP_cERdXd4QoitfEJlSwSQCyPV443vdNcvayi39Bv7Sr6S3GOd5x8uR6IhYS8AbuE8E4L6JW0oqa1AyzFNZe4Rz_T-1pceTE1N5yXfkUanftKZWnXHktHG0mWOtocThgliC830oJz0LUc5171FH2DqwrpCrv7HibY9V9URX9mxhZ2x-W6SaRuDTQ6kC1WhOhw_OUCtxXMX_U3c0UVkLJm6yDIWOoVzaJwUz4cAyd-RMoVc-RYJyu1oSizYhJer1AQYKDSGYxR9sNxmDB3ddBu6XQdSQI3y8IBD6dla4B6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3053de3fdc.mp4?token=MQu6EzxyBPvgC-0zZYPx_t1rf4T1rEMlOvsDT2PO98SwAhuW6NUHcpi_PFnJpsh8-noMvIHTOpRsQYW1psU3SMqXgYxpfDaQYKRlgF-iMbSw9MO1ZXpcpgHaiWoJYOnOAcwFPfdd5HDLvp1KN8OoFJnzCTdzTkJbntTkJgN6U94g3qJczgiZJl8a_XjUqhM6ZYAVWh1AwYwm42LjgykAgEy6iDpU8UcPcetdnQBXc0JTLvb2xW5FXA7y12BiU6PI7dOnVAHeFEkbCxPoebtvDE9xZUOc11njQQ4eCDxN54khdE-XQR5sFX9rvmWwRHkt6pBRkafr7MLzE9NbFV0jGBlgpKbOGaI4OIY16jRTlrP6fmQByaPN_x0GFE77_jlilvP_cERdXd4QoitfEJlSwSQCyPV443vdNcvayi39Bv7Sr6S3GOd5x8uR6IhYS8AbuE8E4L6JW0oqa1AyzFNZe4Rz_T-1pceTE1N5yXfkUanftKZWnXHktHG0mWOtocThgliC830oJz0LUc5171FH2DqwrpCrv7HibY9V9URX9mxhZ2x-W6SaRuDTQ6kC1WhOhw_OUCtxXMX_U3c0UVkLJm6yDIWOoVzaJwUz4cAyd-RMoVc-RYJyu1oSizYhJer1AQYKDSGYxR9sNxmDB3ddBu6XQdSQI3y8IBD6dla4B6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن کیایی و پوریا رحیمی سام در سانس‌های ویژه «قبض روح» روی صحنه می‌روند
🔹
بلیت سانس‌های ویژه از طریق فیدیبوآرت در دسترس است.
لینک تهیه بلیت
👇
https://fidb.ir/t8x
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/693229" target="_blank">📅 20:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693227">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادامه پیشروی یمن به سمت باب المندب
سخنگوی نیروهای مسلح یمن:
🔹
نیروهای یمنی در کمتر از دو هفته با پیشروی در جنوب و مناطق ساحلی، به مناطق مشرف به تنگه باب‌المندب رسیده‌اند و در واکنش به افزایش حملات هوایی عربستان، با حملات موشکی و پهپادی به عمق خاک این کشور پاسخ داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/693227" target="_blank">📅 20:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693226">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6693eaba7.mp4?token=EUMTPevU_VG0fPCl1r63F0Btb57Ke2T5kZKyJnigKWEsqCHXyxhJcYLR6Pl7K7dAm8icyQ1Mk5j7k8qAdPFGwCVyJn18QRbwwC-lLUCkKIXctSDHaMM8EWmE6PdgBLIIXMvvdQPyVCEFDNl_etsmlI6-z1IzJBDUY7GWsE8-aaPqYCNQh6rPGU7WWc3E_bMVgct5j4hXpS2IcLldGxs9Wh3-MjdfNf2SPMrvYRhidNv3zCR2T496Wgmxcrrn2q1KlyAuyFZLGw1R44aQSEDT0uHRVf95dPfupF2l4oOIiRV4kUa47drG3hXSpnjp8nSl_i8h5UEi9PHOWqYHnNTqnU3jyfC2tsy7JuNOTWTPjdBXoeEMmdk5AqpMY0ehJckQZnKxoM3X08AKGGFCMyqaASFsM4UH7FZHkV-rhDosAK6FfNX9Oz5ra4YC29_WgiUklX8yyBpnOC__k4sVlfrXy714FQZHx6mTO6U1wfvLcNPcjDTE4wg8qxqtknNA6bWPC8LHXUJBbG4nGjXrEtnH3xsHmG8NjwljgwemTTMpKM601U2fkLYvnFEx6KkHVzoq3yCfmLKT9kFseyW22Rbr05EsQ6TR5XaO8wjePaBKayjpnu8mnzE948K0Q7SSPiJoVErvoW8fneQr4LP26r7Q4g7v3FIGPotVJUT_DhR1dxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6693eaba7.mp4?token=EUMTPevU_VG0fPCl1r63F0Btb57Ke2T5kZKyJnigKWEsqCHXyxhJcYLR6Pl7K7dAm8icyQ1Mk5j7k8qAdPFGwCVyJn18QRbwwC-lLUCkKIXctSDHaMM8EWmE6PdgBLIIXMvvdQPyVCEFDNl_etsmlI6-z1IzJBDUY7GWsE8-aaPqYCNQh6rPGU7WWc3E_bMVgct5j4hXpS2IcLldGxs9Wh3-MjdfNf2SPMrvYRhidNv3zCR2T496Wgmxcrrn2q1KlyAuyFZLGw1R44aQSEDT0uHRVf95dPfupF2l4oOIiRV4kUa47drG3hXSpnjp8nSl_i8h5UEi9PHOWqYHnNTqnU3jyfC2tsy7JuNOTWTPjdBXoeEMmdk5AqpMY0ehJckQZnKxoM3X08AKGGFCMyqaASFsM4UH7FZHkV-rhDosAK6FfNX9Oz5ra4YC29_WgiUklX8yyBpnOC__k4sVlfrXy714FQZHx6mTO6U1wfvLcNPcjDTE4wg8qxqtknNA6bWPC8LHXUJBbG4nGjXrEtnH3xsHmG8NjwljgwemTTMpKM601U2fkLYvnFEx6KkHVzoq3yCfmLKT9kFseyW22Rbr05EsQ6TR5XaO8wjePaBKayjpnu8mnzE948K0Q7SSPiJoVErvoW8fneQr4LP26r7Q4g7v3FIGPotVJUT_DhR1dxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی ربیعی، دستیار رئیس جمهور در امور اجتماعی: بخش بزرگی از مردم می‌گویند هیچ راهی برای اعتراض ندارند / باید سازوکاری ایجاد کنیم که مردم بتوانند اعتراض کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/693226" target="_blank">📅 20:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693225">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
صالحی: چین میزبان نشست سه‌جانبه ایران و آمریکا شود
🔹
علی‌اکبر صالحی، وزیر خارجه پیشین ایران، پیشنهاد کرد چین با میانجی‌گری و تضمین اجرای توافق احتمالی، میزبان نشست سه‌جانبه ایران، آمریکا و چین باشد.
🔹
او تأکید کرد با وجود از دست رفتن برخی فرصت‌های دیپلماتیک، کانال‌های ارتباطی همچنان از طریق قطر و پاکستان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/693225" target="_blank">📅 20:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhsLHparwxx_cIt4XCh8X5Jx6G2zCIUi4-DvpUB9pUdOGXnyPMl6HSsg_u6YPKlC0YQ-QH4nwbrWCoAxf63ImaZglWp5beiYjVNEY1GKrQkj9eLmpmdCKkNRF7rINCRVUa_gUNcFW28dePturWrL0xH74hWwqcKVNPNsXqz0jWOV-TfPUs8ymrFM4P7vxSbd5lzM4Djlgd1LoNsxYYenlc-rKMey5SZ513EulpGNz0FC7OyuqJ4mE72ukSJ9neoJRV8BNdY-qP9t8O0ttEQQDl12MSRanjd_fskvTAuRs4WCUfXw9QDKbRR4hXASZuf0u0jteelKR7FJtY614vpuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میلی: ۹۶۵ کیلوگرم طلای کاربران موجود است؛ تسویه و تحویل ادامه دارد
🔹
میلی در بیانیه‌ای درباره تأخیر در بخشی از تسویه‌ها، ضمن عذرخواهی از کاربران اعلام کرد معادل ۹۶۵ کیلوگرم طلای مربوط به تعهدات آنان به‌صورت فیزیکی در خزانه‌های امن و بانکی نگهداری می‌شود.
🔹
به گفته میلی، محدودیت دسترسی به بخشی از این طلا، از جمله در بانک کارگشایی، روند برخی تسویه‌ها را کند کرده است.
🔹
این شرکت همچنین از انجام بیش از ۷ هزار میلیارد تومان تسویه ریالی و تحویل فیزیکی بیش از ۳۶ کیلوگرم طلا در ۳۰ روز گذشته خبر داد و اعلام کرد پیگیری‌ها برای رفع محدودیت و انجام کامل تعهدات ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/693223" target="_blank">📅 20:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">19-1 Ane Manaee (1404-02-06)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/693222" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه نوزدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
توصیف منافقان و بیماردلان با ظاهر مؤمنانه و ایمان مستودع، در سوره مبارکه محمد [01:46]
🔹
چهره غلط‌‌انداز حق و باطل در فتنه‌های آخرالزمان؛ خطر سقوط برخی مؤمنان و فرصت عروج برخی کافران! [07:50]
🔹
وقوف به عجز و کاستی خویش، اولین و بزرگ‌ترین گام است در مسیر خود سازی و اصلاح نفس [17:45]
🔹
موضع‌گیری جریان‌های مختلف با فرمایشات رهبری در لباس تبعیّت از حق؛ مصداق "زُیِّنَ له سوءُ عمله" [22:08]
🔹
مَثَل فتنه‌های بزرگ و ایمان‌های ظاهری، مَثَل چوب است و لجن های ته حوض! و تکانه‌هایی‌ که باطن ما را بیرون می‌ریزند [26:50]
🔹
امتحان ولایت پذیری، سیلی خوردن از ولیّ خدا و ماندن پای اوست! نه صرفا ناسزا شنیدن از دشمن [31:13]
🔹
دایره امتحانات اهل حق؛ از شیرین بودن طعن و آزار فسّاق! تا شنیدنی بودن اذّیت مؤمنان! [34:43]
🔹
آیت‌الله مصباح و مخالفت با هر نوع مصلحت‌سنجی، بی هیچ رودربایستی! مردی که «از خدا کوتاه نمی‌آمد.» [37:56]
🔹
دین؛ ابزاریست برای توجیه نفس، یا تدیّنی برای تبعیت از حق؟! [42:30]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/693222" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
محکومیت ترور رهبر شهید انقلاب از سوی لاوروف
🔹
وزیرخارجه روسیه در سخنرانی در مجمع عمومی سازمان ملل در نیویورک ترور رهبر عالی‌قدر و نمایندگان دولت ایران را نمایش غیرقابل‌قبول از دیکتاتوری و زور خواند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/693221" target="_blank">📅 19:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bdbcc32d.mp4?token=TMGmIEzl4krRWzjr6cjQhbZ8InSyApQisLye792RkE8RDdcDUUCGPvC_2F_lWzO-JzSIOsivAVMsczW2blaXvBVdUgp0mMTclOsxcepL31gIxwmd74vKsQL32EVowf6gr0CwhRrfaVMgrqxtEdAiZ_Td1rQUP6m-I6Z9HVuIqsDFCL5Hb3roVzUgFqRocOT1R1grgz18Lo1hC8jv19_vffUiPt1rQFi7mOX2zu4PlSPc9YQmdMt4kLiW-tcUpXdqiMuyQVMRKfDxli_MV_O2iQ1SOh1YbJUNwxuKOS4PcgCvC8in9ceNvln9ZrplJhYcA8CXCJY_NlJ7SBA1vVHztA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bdbcc32d.mp4?token=TMGmIEzl4krRWzjr6cjQhbZ8InSyApQisLye792RkE8RDdcDUUCGPvC_2F_lWzO-JzSIOsivAVMsczW2blaXvBVdUgp0mMTclOsxcepL31gIxwmd74vKsQL32EVowf6gr0CwhRrfaVMgrqxtEdAiZ_Td1rQUP6m-I6Z9HVuIqsDFCL5Hb3roVzUgFqRocOT1R1grgz18Lo1hC8jv19_vffUiPt1rQFi7mOX2zu4PlSPc9YQmdMt4kLiW-tcUpXdqiMuyQVMRKfDxli_MV_O2iQ1SOh1YbJUNwxuKOS4PcgCvC8in9ceNvln9ZrplJhYcA8CXCJY_NlJ7SBA1vVHztA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از دانشگاه آزاد تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/693220" target="_blank">📅 19:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e51551b9b.mp4?token=m7BPyGm-EHLCWUecdmg6_7sDBkV6zi5Vc5HwpmQNESuTeCoVblLb6SG4-bjZArTU3dSV215Nw3vU9w-7OzYqGYFwtf40g_W8vHwZl6cFhEDRmrWnY5laWA5h-cjD8MnQAwSkvBB7jm_rF8bI0z3vKn6Q7-yxg64vVUyqdZcS1VvtX-Eq1gRq0utv4QDIkJ8hSzBuYT5Pw_P0M5J0OIrg-8K8laA8V2BulXxb1bw1wixRl2lwMN6idfvAH1O-A9LwcBWY8Ho7kKIp03syYqVsIFdLwh7vnybjUklAuHndo9AuFCgH5tiXfqQPYXQ7fxeaKqoG_da-jdFWSVL7WmUqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e51551b9b.mp4?token=m7BPyGm-EHLCWUecdmg6_7sDBkV6zi5Vc5HwpmQNESuTeCoVblLb6SG4-bjZArTU3dSV215Nw3vU9w-7OzYqGYFwtf40g_W8vHwZl6cFhEDRmrWnY5laWA5h-cjD8MnQAwSkvBB7jm_rF8bI0z3vKn6Q7-yxg64vVUyqdZcS1VvtX-Eq1gRq0utv4QDIkJ8hSzBuYT5Pw_P0M5J0OIrg-8K8laA8V2BulXxb1bw1wixRl2lwMN6idfvAH1O-A9LwcBWY8Ho7kKIp03syYqVsIFdLwh7vnybjUklAuHndo9AuFCgH5tiXfqQPYXQ7fxeaKqoG_da-jdFWSVL7WmUqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محکومیت ترور رهبر شهید انقلاب از سوی لاوروف
🔹
وزیرخارجه روسیه در سخنرانی در مجمع عمومی سازمان ملل در نیویورک ترور رهبر عالی‌قدر و نمایندگان دولت ایران را نمایش غیرقابل‌قبول از دیکتاتوری و زور خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/693219" target="_blank">📅 19:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693217">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3137cf5f.mp4?token=XhLWEpw0t2tUk-66YtOMej-rE5XlePMIO1OXYeJzUs3X64JA4zBFhklYcS2xgR0Y3otBkbg3pLzywgI5dVntrALVhzyPwtnomT947eNHzDe5lzoyKH8R9B8m5uiNZNdBWAwTNR96XG6hB1-9bPV5k5k4YPMUXV5GNrw2x7mQBAbtkR8AaYKKrSg22hTPqRQFAwdL6HT4AKAZa4bH5Y_CYlAjvn2q97ALOSX61sFiijn3S3SCwmBJjm6ILOkdEFTDr6-tMen9-ypLYyeDY00ojr5gLsuoov5vl-Cte4IoXii0QSged8YVqB-GfjH-Bz-hCo3qB2zuD_nNS333b76K8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3137cf5f.mp4?token=XhLWEpw0t2tUk-66YtOMej-rE5XlePMIO1OXYeJzUs3X64JA4zBFhklYcS2xgR0Y3otBkbg3pLzywgI5dVntrALVhzyPwtnomT947eNHzDe5lzoyKH8R9B8m5uiNZNdBWAwTNR96XG6hB1-9bPV5k5k4YPMUXV5GNrw2x7mQBAbtkR8AaYKKrSg22hTPqRQFAwdL6HT4AKAZa4bH5Y_CYlAjvn2q97ALOSX61sFiijn3S3SCwmBJjm6ILOkdEFTDr6-tMen9-ypLYyeDY00ojr5gLsuoov5vl-Cte4IoXii0QSged8YVqB-GfjH-Bz-hCo3qB2zuD_nNS333b76K8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده تعلیق پروازهای ایران به نجف   یک منبع عراقی:
🔹
نخست‌وزیر عراق دستور تعلیق پروازهای ایرانی را به وزارت حمل‌ونقل این کشور داده تا این تصمیم به فرودگاه نجف ابلاغ شود؛ با این حال، تصمیم‌گیری درباره پروازهای فرودگاهی در اختیار سازمان هواپیمایی و وزارت…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/693217" target="_blank">📅 19:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693216">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سی‌بی‌اس به نقل از یک منبع آگاه مدعی شد: مذاکرات آمریکا و ایران با وجود رد پیشنهاد توسط ترامپ، هفته آینده برگزار می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/693216" target="_blank">📅 19:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693215">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21de8c005.mp4?token=jKJmlUkVjS4GBzWr902Kbf7W_wR_IdYzCMn-J7-0k5uLHL-ms8jmVlDJQ2sX27_GeNuimYIXYOxj8K_-3DWt05ie1NANbzDRqfNtn9_jZlJdPk1Dm9uEeb3umAAVFwFP7Uy7euXb7B8HPfzwaVMzCQWktGiPA4OIk-oLnSi_FSYJkAEU-GBwmDPbfLTw67KORO94k0rjs4aA_NF_xgag6B1ed_d1Kn12bLppZB099sqSmXc6bjQJQ_1eM8UWMadoud8eY49p_XQB61eHCBauVVTZ-_subKslqK1W6kYBv0UtWG2EY5y0sxoKymL7VQnAHsg10Hq237lS12-KSVwqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21de8c005.mp4?token=jKJmlUkVjS4GBzWr902Kbf7W_wR_IdYzCMn-J7-0k5uLHL-ms8jmVlDJQ2sX27_GeNuimYIXYOxj8K_-3DWt05ie1NANbzDRqfNtn9_jZlJdPk1Dm9uEeb3umAAVFwFP7Uy7euXb7B8HPfzwaVMzCQWktGiPA4OIk-oLnSi_FSYJkAEU-GBwmDPbfLTw67KORO94k0rjs4aA_NF_xgag6B1ed_d1Kn12bLppZB099sqSmXc6bjQJQ_1eM8UWMadoud8eY49p_XQB61eHCBauVVTZ-_subKslqK1W6kYBv0UtWG2EY5y0sxoKymL7VQnAHsg10Hq237lS12-KSVwqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات پلیس انسان‌نما به خیابان‌های چین آمد؛ گشت‌زنی T800 در کنار افسران مسلح
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/693215" target="_blank">📅 19:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693214">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsEYoA24CFCscHkUA56ry1kDF-Bqb0nOgknm3hEA4foxKCgxekeBp7AumdWcy4OfmFgI2zji_TfingeFQREHmNPrQl_zXZGZQ8DOopwKXqF-Ear0bkRDIcNvDBNXitXKmoABlqs_8BgRzdF9SD1O0LdwDxB_2-67wb15TNP0o1cOROonUjC7ChEZe_p0OtHRp03DOuAVEvHpyyMWJrULdkezEgvIoCz0SR0NvQvpJ6I14ztCoZW7MvbNQ_e8IwI-mJDunAqjo0tYFSQdSmSUfv08dStg3HbecQ3V5Fqw4iq5tV-ZTCOdr3-xCV0M815IWV-TYwK-IEYkxL5lcdvMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممکن است اسرائیل جنگ جدیدی به راه بیندازد
مرندی، کارشناس مسائل بین‌الملل:
🔹
به نظر می‌رسد ترامپ تحت فشارنتانیاهو و متحدانش برای تشدید تنش، پیشنهاد ایران را که مبتنی بر تفاهم‌نامه اسلام‌آبادبود، رد کرده است.
🔹
اگر نتانیاهو تصور کند که درانتخابات شکست خواهد خورد، ممکن است برای به تعویق انداختن رأی‌گیری یا ایجاد فضای«همبستگی ملی در شرایط بحرانی» (پدیده «حمایت از پرچم»)، به دنبال جنگ باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/693214" target="_blank">📅 19:14 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
