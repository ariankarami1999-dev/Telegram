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
<img src="https://cdn4.telesco.pe/file/M1FT8c7QyAppcfNGFAocN76S4whyyv0zNJNkUqbnCB8EDfv_lTkjnybNV7U87FsLeEHzMLqev9P7gd3mUxL-NXox7mHQNvZbv6_4uKcSv5BWeRYoRmeB-ZdUmqgBBS50bOfj1Nldj_RMu-dn61AgwFqGXJVIKnjiLXjXfoYvZQtkHVsBIMuH8PX8Uko8slLtqa-kvhrhcvZ9o9OYBwY6gV2j1W9zDQdIKQ_a3e_MmB_kZmCPnMdZS-qZZssxXIavVBHUM5RgCQJfLUgS0pYOMIYtmZZ7F6OY578STl-l_-o-M7prEerRbXq5bL7xTkd_UXZuMWYW-WUD7QLUzVDVBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 02:39:36</div>
<hr>

<div class="tg-post" id="msg-668761">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7o6dLSqbK5V9V_ypx1s0l1lt6Z42_uKNLKC_0d071OjP0Hcq9zZNF1aXZnm0t2VQEdDsN1VbkWTQf7fbbE5zdNf9s7C2bvMFK9XgNfNDvmDozBzgy05iLV3tXZT5XNX0oxbAJU6H2dwK3Ni225JYLspWGi7UC07ufF0NfCzgRlGC3aps302zMxT00VECOOJ8Ms6XHmrObCxZKI8vLC3usp7zv5sk7dp0KJ7mrD95h8FEsKVdo4JMMzTlEdhA89T88eYKH3viIQP2V7QB82771po9ipEYiU0VPzH5DR57PcmHDGmxITkcoqqFskq5ZYYSBRUfYw1YFfg7NeZi6g5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری هوایی از جمعیت عزاداران در مراسم تشییع پیکر آقای شهید ایران در کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/668761" target="_blank">📅 02:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668759">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTrW8xgGJZXmlZ-M_DbFLVsrD02OkwH0DMgnxq4P8yplnHoivxkUH5aOAtzWRgghiWZ9y0xSaU6kqjrnQq93nha8O8WxFN5nUCr2228MmJ2J7OFcBjcr8iV3OlZG-bs1houqZd5VwaNhYrASxnEdF_ykz1tfuQ_KTZtTb6hX92f1gQbD8XcxLpK577NWnK114UQlizWVNXMFMNhLTd65gFuaeuEDqGfbcHkSvL3Q_jEXGhAU9XrAhI-rIo5ZUZPXGiCgbLLBsEz2EwHnHGGpCSmrKu94x8UxP44yCt4d6yohK-Da_tb6cQF0uOnSOGgRLTthc2GDAI7Nx5dXQUtWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما ترامپ را خواهیم کشت
...
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/668759" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668758">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb3e36225.mp4?token=csFQTuZ01eheCxaCunDoHl4VQflNjwVs5E1kKMaUsw_RsT84iUimXfMly_hUF-OAy_36J7GsH17F6RGWKXIsD8k7H8DNEuPqJV3ZnW1odaWxMtICJq6j8ESf3f3-E1f5yyx1pZ6gFWS__2KrU-MVNssj53l6CyZeJhXphO8_eeymv4kq7s9NGX2QP_fJMWfrDdlL0450WNI9xqJwSu5x4ID8XqZSXaWXXEUE7ufY2YpZwvn2LTHWBZTKXnsC0nTh3fJfkFy-W3Xt_tdpjxWr_BUDH922w1KeoDXnsRT5Q2zPpt0GXQXFMX1z0X1kKAongWVBTcdaesWYxg96M0yo-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb3e36225.mp4?token=csFQTuZ01eheCxaCunDoHl4VQflNjwVs5E1kKMaUsw_RsT84iUimXfMly_hUF-OAy_36J7GsH17F6RGWKXIsD8k7H8DNEuPqJV3ZnW1odaWxMtICJq6j8ESf3f3-E1f5yyx1pZ6gFWS__2KrU-MVNssj53l6CyZeJhXphO8_eeymv4kq7s9NGX2QP_fJMWfrDdlL0450WNI9xqJwSu5x4ID8XqZSXaWXXEUE7ufY2YpZwvn2LTHWBZTKXnsC0nTh3fJfkFy-W3Xt_tdpjxWr_BUDH922w1KeoDXnsRT5Q2zPpt0GXQXFMX1z0X1kKAongWVBTcdaesWYxg96M0yo-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای مردم عزادار در جوار پیکر مطهر رهبر شهید انقلاب در نزدیکی بین‌الحرمین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/668758" target="_blank">📅 02:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668757">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حال‌وهوای مردم عزادار در جوار پیکر مطهر رهبر شهید انقلاب در نزدیکی بین‌الحرمین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/668757" target="_blank">📅 02:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668756">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای شیطان زرد درباره ایران: ما همین الان ضربه بسیار سختی به آن‌ها زدیم
🔹
می‌گویم که نسبت ضربه ما ۲۰ به ۱ بود.
هر بار که آن‌ها به ما ضربه بزنند، ما ۲۰ برابر به آن‌ها ضربه خواهیم زد
🔹
وقتی آن‌ها حمله کنند، ما با شدت بسیار بیشتری پاسخ خواهیم داد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668756" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668753">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubfk4hFIQCpjjvD7kPg60BP6qV2_8lL2TNXnnIPNShAIxrk4XBJmVec1-MEV-BoehGZ0RbcmiKt5GJDOmPalhHMpq2HiTYm3EpE-NQy34gxmr4bp90gq_PUGrXXFl6LAMIIz43hGLWY3Vee7K_u0yBEpy3EpMxaBk59NTRFnaR6CVD2pcqVysVrDrphyNPQcShd4XW3fEDCfZeTwByw3YY5oetyclQtI7yT8aFsFCL4N2QsK1T5tnxXvXl2Z6C7gSKJMXW6TtuVLRhnKzeWkowrw1nR3Hj7ym07iWmTNT_zCQZzS4DdYpdTMDSpkQvyi9Ux9nHkF-_F1UuVitB4oVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uW7RUFgaphgSDyUwly8NO4pX4lSksDMuk6Yve-rrDWSkOVII-_ova2V27ZYz6jd4I1NCRXkhdEn20CGWyQI0NDlUbb8Kn2sXW0KNXVNhqljW0avpiTJ9HlfhuskLZYTA6JToicctxmR8ktRocClv-qx8mawEzKAtCT2Fu7MwRSvAQUMKp4WXuL4zhR0_yjPfMOIaRBFAIlYp8Xe9UP6k3ytf6QGnUwzFHGfK4z3p_SE5xpCuWTbVGPF22IKPJkZfqoUy3svDHjTGxiZieW0_PkVz5VcYEHpfiMupDs7wmL5h8LG1xa8dCuz35k38rKvOEG14wdPfwof8piXI9crCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4QzUsHS6yCI2SSxQyWy_3jPhG6iDLrGzRmhSUILCeXofGDIwkSUtcsHhiVLArLBNZPVphz54u5CHhGlwc5s_MeBOZPIH47lbujizcev8YEHym41a_4WjEwQ-2GGGqJtW0lPnORCOhIBof2XLhknbmHKm5Vxl9yAvSJ3JUGoOM_e4LMCEntjg7xlLP--vdLY0OoGHoPJZyjkZUOPPEOeFKtW7Z3H2P3Ck1tCt7o-J92zWZgq8OgT18xZmVc1Bk-FPX-g2pmGM1w9y4NkukhACjMyrJLL16vaN0T0H5jjsXuphSZylwD-a2stid7rzISWq5JCE0XFtAcVQfNJrosNKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انبوه زائران در بین‌الحرمین در انتظار رسیدن پیکر
رهبر
آزادی خواهان جهان
انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668753" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668752">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
نگرانی اسرائیل از انتقام‌گیری ایران از تجاوز آمریکا
🔹
رسانه‌های صهیونیستی هشدار دادند که احتمال دارد ایران و حزب‌الله در عملیاتی مشترک، به سمت فلسطین اشغالی موشک پرتاب کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668752" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668751">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65366aac01.mp4?token=CP1TnVO5xvOugxH5Ph71gCphMDPyBxF6Yy087ApeuQ8exxXH0k1nrrMB0avo6zKZqR-p1-f62zRsQt3BNIfwPSPwfozu3lpQYFM_SHtF62Oui9DalY4WTsKEYlkjIq3g2vB6E1JiP3gViGL9MW6XXVMsVQ21nT3WtMn05KHaCBWhEBly7FDOMkn6SUt-QjmBUFiJvbuZ76c3_aK8L0U6BzmM7HBI34BHoZveeXb_nBfBgnyFHq1oxPcyM2dzUisOUFAQqd7OGj2y4IFhjEt2P67VIdXGoXgdevg3FaP-RwAiQ7W831K5ipSI59IGLBJ6RcdU2ugQ3KjnFG5-XK9yQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65366aac01.mp4?token=CP1TnVO5xvOugxH5Ph71gCphMDPyBxF6Yy087ApeuQ8exxXH0k1nrrMB0avo6zKZqR-p1-f62zRsQt3BNIfwPSPwfozu3lpQYFM_SHtF62Oui9DalY4WTsKEYlkjIq3g2vB6E1JiP3gViGL9MW6XXVMsVQ21nT3WtMn05KHaCBWhEBly7FDOMkn6SUt-QjmBUFiJvbuZ76c3_aK8L0U6BzmM7HBI34BHoZveeXb_nBfBgnyFHq1oxPcyM2dzUisOUFAQqd7OGj2y4IFhjEt2P67VIdXGoXgdevg3FaP-RwAiQ7W831K5ipSI59IGLBJ6RcdU2ugQ3KjnFG5-XK9yQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@modaberanschools_bot
📩
یا عدد
۴۴
را به سامانه پیامکی
09982003159
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668751" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668750">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2bcb646e.mp4?token=WZsQwwbRP3VrtIbuJd9_4j6ciSgBH8GGwwQlMcgg44kPcgGZpW6T3cpaXaTJKmDhMD1xIjMOqGLorYk62wuRtsX5PwRGth2cNpsCwoZxAZqc9aJa_ABLihB6271xOLsik72v0R0VKJVfsWZ8XgYFNzOjd-6ZFXelaUoOtYjEJPL9q9ihMFnZkZaqpqpnR_4lMCAylAmUZaE7Dhx7vtEKAESMK74N-_euY0cBWK9Fb450IRDLp2gwMr5w1v2ERTh30DCdThperC8pQGrCArhQY34_fmHIv_QTUC5128zXebCbCFQJ90o-lwx963ahFahSXIW2Q7bQlZottIG61D8xAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2bcb646e.mp4?token=WZsQwwbRP3VrtIbuJd9_4j6ciSgBH8GGwwQlMcgg44kPcgGZpW6T3cpaXaTJKmDhMD1xIjMOqGLorYk62wuRtsX5PwRGth2cNpsCwoZxAZqc9aJa_ABLihB6271xOLsik72v0R0VKJVfsWZ8XgYFNzOjd-6ZFXelaUoOtYjEJPL9q9ihMFnZkZaqpqpnR_4lMCAylAmUZaE7Dhx7vtEKAESMK74N-_euY0cBWK9Fb450IRDLp2gwMr5w1v2ERTh30DCdThperC8pQGrCArhQY34_fmHIv_QTUC5128zXebCbCFQJ90o-lwx963ahFahSXIW2Q7bQlZottIG61D8xAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان امام‌رضا(ع) مشهد، ساعت‌ها پیش از آغاز مراسم تشییع پیکر رهبر آزادی خواهان جهان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668750" target="_blank">📅 01:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668749">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
حمله آمریکا به برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار  مدیرعامل سازمان منطقه آزاد چابهار:
🔹
در جریان حمله ساعتی پیش آمریکا به چابهار، برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار هدف قرار گرفت و آسیب دید. در این حملات یکی از انبارهای منطقه…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668749" target="_blank">📅 01:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668748">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d748eb74f9.mp4?token=rpQVNegCCFpV9C6oC7ZLlF_uRnE5LYfhQfB7YJf7UkHNbftVzTr-g6OfKwJt-aYrwrpW_UqV-yXmbALXwoGIBQfZ78Mocz1AAmyX_LJlWkV74A74HqzgWni7mKWHHUdCLxgEvw-AGLH6CrgTTAmzXrnhxjXa5PSiq5cyzb5ERj1BYHrKz-3PDk2_fgegIEAOxt6VCoorcov_BgBRfm4u9e-pdYUSCc6_eA_cZOfC8lFoiiS3glo-v_QRJX9Re5oECfqU7DsoAjdTtTBEwzAdMpAawqABNwz2LMXeTSNIveu-vp7D-QAM61TDl_Or0bVy7auI5PxNzCAkuCZEx4nobw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d748eb74f9.mp4?token=rpQVNegCCFpV9C6oC7ZLlF_uRnE5LYfhQfB7YJf7UkHNbftVzTr-g6OfKwJt-aYrwrpW_UqV-yXmbALXwoGIBQfZ78Mocz1AAmyX_LJlWkV74A74HqzgWni7mKWHHUdCLxgEvw-AGLH6CrgTTAmzXrnhxjXa5PSiq5cyzb5ERj1BYHrKz-3PDk2_fgegIEAOxt6VCoorcov_BgBRfm4u9e-pdYUSCc6_eA_cZOfC8lFoiiS3glo-v_QRJX9Re5oECfqU7DsoAjdTtTBEwzAdMpAawqABNwz2LMXeTSNIveu-vp7D-QAM61TDl_Or0bVy7auI5PxNzCAkuCZEx4nobw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع نمادین آقای شهید ایران در بحرین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668748" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668747">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4481c2c676.mp4?token=vXtUo_fAilhvTs-1OCeR18cNsQGAj5jrOG4qTqc9IHA_l_QajJVqIOSyNC8cU-QEeS3-8xfaNsU6on0aTvb1cFcNAGJ-pizj8xn5Jf9ZlcEw5AGtjfDUVHLklRb7JNKhws93DH2GfqU2SZaXQyqTcFi67UfzuZqO1flquh1z8Mm9mZTngkp0EkF33ztK1NVVschEbn8uAJGCTc46kLqVPGfe7-a4y857PLH4HaiLUI8hKM1fGwnuPCvmJClBKW2ogCoStkKodkZEs30mGVP0M8LrOyeo3AwvJYS8itQd-ZTotjH39P7BFppYH4yXEL1V_nJFMCdTognbN4Hbmmxb_kxak-TEivY6r1GH7CLNdDfg1Os0gux9DFwVH7Q9_iXCa1fntcCEeUPbZIkMmn8AXVvGzFNZOStBBSSxImhhb8TtrT2IaFSn4aQt2WPd8SQ1sLos1ctpbvbq0DLCgBHXX1W8fF0C7rurZsoJHII33ODBPLA0HntNst1g5nSf7LEudal_mZeEGg3Z8AX4_-CKjw5oe1L9T3OpNLdvhsAC2RCOQr2sClPfx5Sx_Rh7lIIJJfh1W3c_VsLu2Ljn0LDO55QRFrENoH8veQ4cKkwoxX2hAkNY3ceB-xROhHxSaBZzLVN2eTlM2uA-L1hp16UtNIygb_khEycyjVZhSi1GFvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4481c2c676.mp4?token=vXtUo_fAilhvTs-1OCeR18cNsQGAj5jrOG4qTqc9IHA_l_QajJVqIOSyNC8cU-QEeS3-8xfaNsU6on0aTvb1cFcNAGJ-pizj8xn5Jf9ZlcEw5AGtjfDUVHLklRb7JNKhws93DH2GfqU2SZaXQyqTcFi67UfzuZqO1flquh1z8Mm9mZTngkp0EkF33ztK1NVVschEbn8uAJGCTc46kLqVPGfe7-a4y857PLH4HaiLUI8hKM1fGwnuPCvmJClBKW2ogCoStkKodkZEs30mGVP0M8LrOyeo3AwvJYS8itQd-ZTotjH39P7BFppYH4yXEL1V_nJFMCdTognbN4Hbmmxb_kxak-TEivY6r1GH7CLNdDfg1Os0gux9DFwVH7Q9_iXCa1fntcCEeUPbZIkMmn8AXVvGzFNZOStBBSSxImhhb8TtrT2IaFSn4aQt2WPd8SQ1sLos1ctpbvbq0DLCgBHXX1W8fF0C7rurZsoJHII33ODBPLA0HntNst1g5nSf7LEudal_mZeEGg3Z8AX4_-CKjw5oe1L9T3OpNLdvhsAC2RCOQr2sClPfx5Sx_Rh7lIIJJfh1W3c_VsLu2Ljn0LDO55QRFrENoH8veQ4cKkwoxX2hAkNY3ceB-xROhHxSaBZzLVN2eTlM2uA-L1hp16UtNIygb_khEycyjVZhSi1GFvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین قاب مشترک از پیکر رهبر آزادی خواهان جهان با گنبد حرم مطهر حضرت ابالفضل العباس علیه‌السلام در کربلا هم اکنون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668747" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668746">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOXh2Rb4kZE7q5RiFhfGkG3bYA_95SNYPZzf4uj_AFPL6RVv7YV3GZRED2MX8C-QKdjZxFR4H_-roX1EPiwbYPY8TuHfgrgYwHSG5ikgfWLBjH0V22qTT5nY4qf32F3p0i6rOTwjjSj3rv0jBWzKHHnNamKuf6SQkEUQuN3jCqWsHu-w3cr4NlEksfLcYMAbSj_hp5c9ZOHLHE1fw0Pl3pxfK5hE2nnyvJd0oVOJjFBW_MZyzIZ_X7gPNAxVleLWLENPeV0OfX8N0K15qfMIT_8lMF5kfAJmMglHM0LQkEA3GyWlwyFjlMoSAZLqF2N0q-toKJ-WvJVYQbvQ-joICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره مزايده در سامانه ستاد:5005095004000004
موضوع مزايده: بهره برداري تعدادي از بازارهاي ميوه و تره بار سطح شهر مشهد مقدس مطابق ليست هاي مندرج در اسناد مزايده به اشخاص حقيقي و حقوقي واجد شرايط به صورت اجاره .
مدت و مبلغ بهره برداري: به شرح اسناد مزايده
جهت اطلاعات تكميلي به سامانه تداركات الكترونيكي دولت ( ستاد ) به نشاني
www.setadiran.ir
و همچنين جهت اطلاع در روزنامه رسمي به نشاني
www.rrk.ir
مراجعه نمائيد.
#مزایده
#مزایده_عمومی
#مزایده_شهرداری
#سامانه_ستاد
#سرمایه_گذاری_مشهد
#فروشگاه_شهرما
#شهرداری_مشهد
#بازار_میوه_و_تره_بار
#سازمان_ساماندهی_مشاغل_شهری
#واگذاری_فروشگاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668746" target="_blank">📅 01:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668745">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSAZop9eBdFBbgMiB9ntW0_UzI3y8eV6Elu2MU4czPbBIWTAhxRikFuFIsEEhhgcGRs-WWtKSo8g_kf3dxyoxBLCZkYfmyFPxg2R1xOAp8VIMDwyNuKqq7bXIqy37rpLHrSqO45_DaoRO37queaSqbmfCVDTkAavp2jfri47UmQhCgSU3Gc1v4074HbnQ8DEYeOK_VbQ0MK4kukQuaJgXQFjU3TKZSGZmixIrdKfeeJ_Slv7bI75rffmVp2mWU-Tf5LLA0cKfTXS2x8_GHXHd4L2FpC8nTW7My9k-xWnYNbTf5u5yY8h5YBkW3VB9zedSd-LN9sbd7_Oa7nOR84ZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود بر ملت و دولت نجیب عراق؛ شما معنای واقعی برادری را به جهان نشان دادید. صمیمانه از شما تشکر می‌کنیم.
تحيةً للشعب العراقي الأصيل وحكومته الكريمة؛ لقد أثبتم للعالم المعنى الحقيقي للأخوّة. نتقدّم إليكم بخالص الشكر والامتنان
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668745" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668744">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
پایداری برق در اکثر نقاط شهر چابهار
روابط عمومی شرکت برق چابهار در اطلاعیه ای:
🔹
سه خط برق در شهر چابهار که براثر موج انفجار قطع شده بود، دقایقی قبل دو مورد از این سه خط برق دار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/668744" target="_blank">📅 01:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668743">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d112d822.mp4?token=qwkkvxyuOk3IWEvJsgEhJb7oy2gghowbXNMijVbGZvoen-HySxGq3NM-v4EwbWgBZPDMhYvnCLszWEHo_COl8t09JvNjydcefmbKYCCylG8KiVY7LNbXPSzoXqmcJ1ke3pIQm4S0KnhAHx0oZDrjQk1ShdFnoNfH39va-3JjLxGR9e4-jIbump8w-CR6IRcT94km4fvNcblIEhqlQrpPNElI6QG5CeitoF6lQT8--9USy2pxwrEACWhoQlLfsIwvOgANvc2pnbCl7VqBxvyE3Wn9u6FHgD7CBxeXfZk2BJSukcNo2mlBBF391wpJyAVn9xJxK4uLPd-4Ihi2AJ7celA9DmqwAbkqww5kIb95jnMG9Vscpchg74CzgKdRgPUdE9EYOI4O7rNTliid5qq17ThTPQpGtO8UnWrdZZs9a5hh54fUo5hQjBGkekv2sLPjGdD2JYFI9DSrB6RK4yOMR_kb0Yb1KFzRY9At0YLlzh_Auh8CbzYKQzygH-pQAshd3GhNpCezY6_QRrFVOR3igc-7ZJ1buMbjHIBur4EoIumrrcF7FycmTlzhroNLK6DwPqnwkVEnfCjUZuITrk12TPY384PzWYUBkm0cf1M97FvQ214mDmIMB8Xv59s3NVNiAVb62yXVcV2m7jsyPOdiZBAlA4xSuttSURySRJ8CftY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d112d822.mp4?token=qwkkvxyuOk3IWEvJsgEhJb7oy2gghowbXNMijVbGZvoen-HySxGq3NM-v4EwbWgBZPDMhYvnCLszWEHo_COl8t09JvNjydcefmbKYCCylG8KiVY7LNbXPSzoXqmcJ1ke3pIQm4S0KnhAHx0oZDrjQk1ShdFnoNfH39va-3JjLxGR9e4-jIbump8w-CR6IRcT94km4fvNcblIEhqlQrpPNElI6QG5CeitoF6lQT8--9USy2pxwrEACWhoQlLfsIwvOgANvc2pnbCl7VqBxvyE3Wn9u6FHgD7CBxeXfZk2BJSukcNo2mlBBF391wpJyAVn9xJxK4uLPd-4Ihi2AJ7celA9DmqwAbkqww5kIb95jnMG9Vscpchg74CzgKdRgPUdE9EYOI4O7rNTliid5qq17ThTPQpGtO8UnWrdZZs9a5hh54fUo5hQjBGkekv2sLPjGdD2JYFI9DSrB6RK4yOMR_kb0Yb1KFzRY9At0YLlzh_Auh8CbzYKQzygH-pQAshd3GhNpCezY6_QRrFVOR3igc-7ZJ1buMbjHIBur4EoIumrrcF7FycmTlzhroNLK6DwPqnwkVEnfCjUZuITrk12TPY384PzWYUBkm0cf1M97FvQ214mDmIMB8Xv59s3NVNiAVb62yXVcV2m7jsyPOdiZBAlA4xSuttSURySRJ8CftY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری بی‌نظیر از مهمان نوازی مردم عراق از پیکر رهبر آزادی‌خواهان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/668743" target="_blank">📅 01:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668742">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حمله آمریکا به برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار
مدیرعامل سازمان منطقه آزاد چابهار:
🔹
در جریان حمله ساعتی پیش آمریکا به چابهار، برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار هدف قرار گرفت و آسیب دید. در این حملات یکی از انبارهای منطقه آزاد چابهار نیز هدف قرار گرفته است. در حال حاضر خدمات‌رسانی و اجرای عملیات تخلیه خودروهای موجود در انبارها تداوم دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/668742" target="_blank">📅 01:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668741">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
صدای چند انفجار در ایرانشهر شنیده شد
🔹
دقایقی قبل، صدای چند انفجار در شمال شرق شهر ایرانشهر شنیده شد. هنوز ماهیت این صداها مشخص نیست./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/668741" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668740">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
یک مقام آمریکایی به سی‌ان‌ان گفته است که آتش‌بس با ایران «دست‌کم به‌طور موقت متوقف شده» است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/668740" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668737">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDWj6FpsiyNdOUi6Y_ultSwudZzBlSpmQqLxbmXFXUE-RGK56NBhc2Qzh-T-o9YCK-jllVviKxdL0PGzT2E73_3nlyBJIeLpM9B518Q9xuFOJU0OUgBsBd8nboY61LiYxEaa89a0MZiZ2mqCeOEV9u9F9Rg_nZ8GZ5v7bFTKZWZ_J8xbktVP32cHxg2Ymfzozg6QYpCx2KiqY2B32kiGRURoZ2l1ZC-DT63gKpuRaW_0fcEDTqNA6bbEy-OggwWwc2-Hmv0ZjxPKq2bs_14pzZkI7BmQ28yb09WefNYd-dv2d2MyNtt4tDkeYzNawP0Pk3Rir6ioMZw7kwdlxwo6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQNIK4WFB7uQMnZ0uEYbqImpFOS--X1vA22HJ4by0G2TpUHYKxO2wgT677t7n7jiItLOz_hdcTxqPGD3CYK14p3orqpN20NU560WleKZGGaoRfCHIsYEcYjPLzGn-UgHnYVKjGdnKjp5F18U1YRuwvXyIlxiDlBNDoqs3qkrfxlF9PYvXDnQ-7x-YGqZNdTV5AlubcWa-npyDbixmB0vZBvhAaSrzFn26OkbapLEMftquOuyU6hyNiQS9bqMxY2rsPKOhXTxjOeqsvFV4hbCewz_kz0pRW6oLWGLvchkBSaSE7n4chQWFle5nhDqcai5LIP7A9uzmL3J38icFcbbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDbqa06x_0-RBuYmJ84JIha0sVKOvg3-8sDilkZdnCtEAxxMFisCJxEVxDXAgr-qwPxo47J34DbrdhJp4g2Xr7R_ml8um2xKzv6YpckoqyIrSJGjL43cR1n4sGtiAYG5o5oJ4xjf1Fa-8awqilwpXQ0udtbHlka_lYSMjVwIY7AXwWvgpN3WSHuXpvuLE104WUPa5n9m0NOpLHtAJ42IcFgB0nKwimIqizzGn5XWLaWhxjCpZ-eITso2_WnLkEnvWW9kTJMsP7pNMg0zY2J7t8wUpAJt0FOtaA20iP7zAq-LvPNRJS6j70e6lZobRDl0OsWYwubZKa52xsOBvZtk-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از پیکر رهبر آزادی‌خواهان جهان در شارع العباس کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668737" target="_blank">📅 01:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668736">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شبکه العربیه، در گزارشی ادعا کرد بحرین امشب در حملات به ایران شرکت داشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668736" target="_blank">📅 01:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668735">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxVWVJR3BfvU4EgWTuk-EL-chgn6_lDgDzqjH2LLFVZDEoXrfYE24juUu0Uw6dIgjl3igpMuHxnz1Q1LtyDb5WGCGNAzQKqWj9ZX9hwRTW4SGhZaMeduIPVZHNX9c0ey0tyPIAmZetnBv99mNPzfeDs0L27dsANww6-AqxfRnKu7eVTfHTdWJhE2EPw8Iac5bjFk0kluyAAiz1XoNxmCGvM5TMP868b8yKmDUcKx2_Fc3MUFE1u0G25sd4pMHyTs9sOzbzMjr_lVDyM2UD1E-S1S1S1C1TNkORmnjFx1yxEw-mf40aR69BGiM_53fEABG2dDDzrKm_TLA1YUrSPdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید خوک هار: این به تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، حملات خیلی بدتر خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668735" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668734">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک مقام آمریکایی: ممکن است به سمت حملات تهاجمی علیه ایران حرکت کنیم
🔹
نیروی دریایی ما در حملات امشب علیه ایران مشارکت داشته است. ممکن است در زمان دیگری حملات بیشتری علیه ایران انجام دهیم./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668734" target="_blank">📅 01:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668733">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ایرنا: بنا بر شواهد میدانی هیچ اصابتی در زاهدان وجود نداشته و اخبار منتشره در فضای مجازی کذب می‌باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668733" target="_blank">📅 01:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668732">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/afdd27149d.mp4?token=mIDHXbgVEzJXgWWGYuEOEQuq9alBajg2BjsT_4Z8aSLRMXKDL5HJ6iByupsKBgaJ3050Y_yNaKhXpf5054ATuO49Imdhjstpr8GwDmB7YccSFUfMdMSjTTmQnnyQVHGZupBVIX62mBMJlhNCLqt3Gyl1YBGlnmfxqvMJuRcWG7nmkuN-Z6Nf9EECbCYIxBeV7RDSbJ4dn0NU2je6WRvIZOyfPNnAiSxbG9yKMhEMq6RKyHIPjuwiRqx-UVDGK9VMoj3LToeGLWHDyYPipci0fAzHynSpp-ym4at4JkqRFNGhuZRqbZ-kytbGO87EZ3PGoXwkW_qqR_w0EZShLXCbbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/afdd27149d.mp4?token=mIDHXbgVEzJXgWWGYuEOEQuq9alBajg2BjsT_4Z8aSLRMXKDL5HJ6iByupsKBgaJ3050Y_yNaKhXpf5054ATuO49Imdhjstpr8GwDmB7YccSFUfMdMSjTTmQnnyQVHGZupBVIX62mBMJlhNCLqt3Gyl1YBGlnmfxqvMJuRcWG7nmkuN-Z6Nf9EECbCYIxBeV7RDSbJ4dn0NU2je6WRvIZOyfPNnAiSxbG9yKMhEMq6RKyHIPjuwiRqx-UVDGK9VMoj3LToeGLWHDyYPipci0fAzHynSpp-ym4at4JkqRFNGhuZRqbZ-kytbGO87EZ3PGoXwkW_qqR_w0EZShLXCbbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«شارع العباس» غرق در استقبال از پیکر امام شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668732" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668731">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شبکه سی‌ان‌ان در گزارشی درباره نیروی دریایی آمریکا نوشت: ما حداقل ۱۹ کشتی جنگی در نزدیکی ایران داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/668731" target="_blank">📅 01:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
مهر: اصابت ۴ پرتابه به بوموسی و سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/668727" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668726">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlNDKIx2Lzv_XHIv--S9ysuFqTKKQB2ivjgFYDLDJMyAjPv8w0V0nkqF8XpPzy9LB9Cyk5ta6uWFuBT3rkSmKxPPZA95SzAAuiMi_0I_0dTerPnK7yTl8FrcwaRMH-u5xtKFBE6UthdJOcGRENqy3GyywyF9KBHhaPb2e2KjEu-FCTejKAqPoFwyfsVtBaBQiAqNiHFDgLI4oQVLD9Wc3SZ-tCDXy2y5l_hrt2zS9Zavl2FPUszol_vUeMrrcSQMqHchrUpTboT9pwDJ07X956P7b0YVGydYGYkWIiEd_YVdDAXn_RN5JYf2yiaUH8HlORXJSKA2uOwB3V3GjS64KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره مزايده در سامانه ستاد:5005095004000006
موضوع مزايده: بهره برداري از پنج دستگاه كيوسك هوشمند شهري در سطح شهر مشهد مقدس مطابق نشاني هاي مندرج در اسناد مزايده به اشخاص حقيقي و حقوقي واجد شرايط به صورت اجاره .
مدت و مبلغ بهره برداري: به شرح اسناد مزايده
جهت اطلاعات تكميلي به سامانه تداركات الكترونيكي دولت ( ستاد ) به نشاني
www.setadiran.ir
و همچنين جهت اطلاع در روزنامه رسمي به نشاني
www.rrk.ir
مراجعه نمائيد.
#مزایده
#مزایده_عمومی
#کیوسک_شهری_هوشمند
#سامانه_ستاد
#سرمایه_گذاری_مشهد
#شهرداری_مشهد
#سازمان_ساماندهی_مشاغل_شهری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/668726" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668725">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9793440cc1.mp4?token=aBTSi5MgFHUbL0oC-lM6FeLTWDlQuff6DDulsQHue3NNiFDIZvODxCjAEWVrS5vAXcAWk9gm5ITbWkVBb03CsNv4090JsK3k3THdmmU-aBmLdpvP8g8tlJn1R4JYZzoo8ZjzEi9rqudfinnTFnIhz416nK--NM9k_N02FrIOoj6LKwUUeJRYqsyY3wQLwLy_H7VDiwQy7faodRla85G34sF1wF9_voNqnIFm6MIM0SCzyG0I__hyvaxDGLJjJ1f-zkH1hNEc_fyD3lfHDbOmbF4-5qbCnmkKwTotp-bNBzRspIR_7hHi08EnP6c7R6pqF61Wr1qxegoQaa1fqGzaPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9793440cc1.mp4?token=aBTSi5MgFHUbL0oC-lM6FeLTWDlQuff6DDulsQHue3NNiFDIZvODxCjAEWVrS5vAXcAWk9gm5ITbWkVBb03CsNv4090JsK3k3THdmmU-aBmLdpvP8g8tlJn1R4JYZzoo8ZjzEi9rqudfinnTFnIhz416nK--NM9k_N02FrIOoj6LKwUUeJRYqsyY3wQLwLy_H7VDiwQy7faodRla85G34sF1wF9_voNqnIFm6MIM0SCzyG0I__hyvaxDGLJjJ1f-zkH1hNEc_fyD3lfHDbOmbF4-5qbCnmkKwTotp-bNBzRspIR_7hHi08EnP6c7R6pqF61Wr1qxegoQaa1fqGzaPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل جمعیت عراقی‌ها در تشییع رهبر شهید انقلاب در شهر کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668725" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668724">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuAxPJlWSWderWx1r9ECFFPoIjXVq7uH685R7lRTsp13juiSYCJz_Bxr24197fY8rVIN-A8fagAes4TXrInFo_ZvvN2qC0ixea0V2yq_zhI868gtK7Ar8xpO5SuPsv4B856bjmWfkMsMJlPUHu17QFqfLLO9NjsXX2XOBpru7aFDAolrAvxlHJ9nW5O2TL50-Qs_3QYyMwivteUGIqoU539rUKLYjIG-189bzS7XPLATTgPDG1cQ1ssddn5OyqwYReLJeQTGc_Uo0fjXOZZUAv2z1IFKQJ-usGfxvDbrkn9S5ZHxazbTXnxTO5AyafMgynK_T5SvnY8n0OYcCwNI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: دشمن به شدت تنبیه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/668724" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اصابت ۲ پرتابه به پایگاهی نظامی در جنوب شهر بوشهر
معاون سیاسی و امنیتی استاندار بوشهر:
🔹
دقایقی پیش پایگاهی نظامی در جنوب شهر بوشهر مورد اصابت ۲ پرتابه دشمن آمریکایی قرار گرفت. تاکنون گزارشی از تلفات انسانی ناشی از اصابت این ۲ پرتابه دریافت نشده است‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/668723" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668722">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
مهر: اصابت ۴ پرتابه به بوموسی و سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/668722" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668721">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
مهر: یک پهپاد متخاصم دشمن در جنوب کشور توسط سامانه پدافندی کشور رهگیری و منهدم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/668721" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668720">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
🔹
چغادک در حملات روز گذشته ارتش تروریست رژیم آمریکا نیز هدف قرار گرفته بود./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/668720" target="_blank">📅 00:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668719">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
منبع آگاه نظامی: لحظاتی قبل؛ اصابت دو پرتابه دشمن آمریکایی-صهیونی در شهر بوشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/668719" target="_blank">📅 00:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668718">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90accfc73.mp4?token=N68nQnK2bRKygF5RV1-SptWRM0qikagqhKJVeHJCIoTt6QdeeHkLowXY5eTqV2yy_fjVM8DQI5qGZU6KZJKIukAsommMQSE8QWyN8gj2r5Ik1PjCLjZigysa9AbGSxFR6wQfUBFBibzStsVlQmb0xje0eBiu5YvnRW-H3QoXorY1QbkCowzdPEuNz2cmMCXhgZn5Mg7VX-mpNUJQzxm-ld8ksmH-FasuFO8tiZclXOQPxPrdq7ZgFzRuXcH7gMY93MdbBpxxs_Cq7NsFfQUWu1YlP66R3T1_NEpZ7-oREBpB6ZP9C3-3ngf7RydJ5Ln9_9nlYIkkErErT2A2N9lWWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90accfc73.mp4?token=N68nQnK2bRKygF5RV1-SptWRM0qikagqhKJVeHJCIoTt6QdeeHkLowXY5eTqV2yy_fjVM8DQI5qGZU6KZJKIukAsommMQSE8QWyN8gj2r5Ik1PjCLjZigysa9AbGSxFR6wQfUBFBibzStsVlQmb0xje0eBiu5YvnRW-H3QoXorY1QbkCowzdPEuNz2cmMCXhgZn5Mg7VX-mpNUJQzxm-ld8ksmH-FasuFO8tiZclXOQPxPrdq7ZgFzRuXcH7gMY93MdbBpxxs_Cq7NsFfQUWu1YlP66R3T1_NEpZ7-oREBpB6ZP9C3-3ngf7RydJ5Ln9_9nlYIkkErErT2A2N9lWWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب، با استقبال مردم عراق وارد شارع‌العباس(ع) شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/668718" target="_blank">📅 00:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668717">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXzHz2Wlme8KohniVOHQDhXLlTaIU4RzgbHz46DFSfL2faSuaOfC66KxSis8Evdg8XczfJkveObL2Ejzuk4qAHxGuFHu0Eqe_3Dkq6LS6V-VKlU8EgmF9YODreTXjIFvjLsgKLaUG9Sl4C9zv0q4aYPvm77PCwlcBfF2THTo2M0BtJN5a4N9wcjx33AdBgTM7YGx1AzomJ1SkcmpQWCkAObR--G6XNFWPkj3VEu2PyOJkh94tOMkUqWayAqt-dULrQZhX7cpO-ZEexuQgOGXNABHFQtW0i2E8bHkBOZL2vwcTTqzHuTT7HJDiP6lpqHJ-SOUIprhjRkFktL7KWjbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنبه حداکثر دمای تهران و کرج به ۴۲ درجه میرسد، بالاترین دمای امسال تا الان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/668717" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
یک مقام آمریکایی به رسانه‌های آمریکا ادعا کرده است که حملات جاری ایالات متحده علیه ایران، احتمالاً از حملاتی که روز سه‌شنبه انجام شد، گسترده‌تر خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/668716" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تجاوز مجدد جنگنده‌های ارتش تروریستی آمریکا به مناطقی در بوشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668715" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تکذیب شایعه حمله به جزیره لاوان/ تأسیسات نفتی در وضعیت عادی هستند
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668714" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تاکنون انفجار در خارگ نداشتیم
🔹
خبرهای منتشر شده در مورد صدای انفجار در خارگ صحت ندارد و تاکنون انفجار در خارگ نداشتیم/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/668713" target="_blank">📅 00:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
آکسیوس: آمریکا امشب حداقل ۱۵۰ هدف را بمباران کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/668712" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
فعالیت جت‌های جنگنده خودی بر فراز اصفهان
🔹
دقایقی قبل صدای جت‌های جنگنده بر فراز اصفهان شنیده شد که بررسی‌ها نشان می‌دهد جنگنده متعلق به نیروهای مسلح ایران است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/668711" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668706">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
برق بخشی از چابهار قطع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668706" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668705">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GloQY8txDsLh28oXmeL7YG_zbK-fYJ9EEV03WtQ7g5azLyVjZh2MllDEypQlWElxmdOAmsAo3W784tWTEcU6736RAmCpknLbItqz69SliRI_LuWaN04DgAG4I6kC6A3GFTfx2MKz9Oi1AreFd0VsRVw4naz2uxoXjeEJH3ILO92KZNBk-lMQ16VSc02ROzDEiMhwJpnYt8b9w_rU6ZV2bCDxIRTXgkTnddzyMzcEdosD9QaOVXlXJdGvReYPJ3Fei-pIlLib0r9qK24MyVRhzfXf2w6MAGIGL3zZdcrTkWobDHMdiFbK3cAsZ5hIeCgsj1BNyD8YLYaHCvqZjf9tQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آگهي مزايده عمومي»
شماره مزايده در سامانه ستاد:5005095004000005
موضوع مزايده: بهره برداري تعدادي از فروشگاه هاي ارزاق عمومي شهرما در سطح شهر مشهد مقدس مطابق ليست هاي مندرج در اسناد مزايده به اشخاص حقيقي و حقوقي واجد شرايط به صورت اجاره
مدت و مبلغ بهره برداري: به شرح اسناد مزايده
جهت اطلاعات تكميلي به سامانه تداركات الكترونيكي دولت ( ستاد ) به نشاني
www.setadiran.ir
و همچنين جهت اطلاع در روزنامه رسمي به نشاني
www.rrk.ir
مراجعه نمائيد.
#مزایده
#مزایده_عمومی
#فروشگاه_شهرما
#شهرداری_مشهد
#سازمان_ساماندهی_مشاغل_شهری
#واگذاری_فروشگاه
#ارزاق_عمومی_مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668705" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668704">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
هم اکنون؛ شنیده شدن صدای چند انفجار در جاسک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/668704" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668703">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
برق بخشی از چابهار قطع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/668703" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668702">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
صداوسیما: شنیده شدن صدای ۲ انفجار در بوموسی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/668702" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668701">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7b02a9986.mp4?token=jSG98uhXIxMwHkDcX6MOXoLQ8u_ZpOLIbEUIulet0s-loeS9z1GqMRpLsG_p2UbkzqQsLNwz4sqJJjqG4rGw6ADYGSG-ARApgWjGM8YGzbOaCTp1Yc_aAk-5yHoXGo-rKeCdCJLvJaAfPU4-X4HSrgrhS3ouY4NLav4BxE7Btz7O4v-12yFWClNxNPSu-RsSr3lWGtEDRFjGnD3D1mefAaOw3lqt5-RIhH10Guz2W_rmdGKkKuXS_F9U7DmApsmULZIIOvMzW4LgdqXOYAG-Q40hBR3icyVRmOvU7GOQttT0N72K-U5GHOaJaYPCWbQKSyVMEDGsi2l7xKArJ2-DIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7b02a9986.mp4?token=jSG98uhXIxMwHkDcX6MOXoLQ8u_ZpOLIbEUIulet0s-loeS9z1GqMRpLsG_p2UbkzqQsLNwz4sqJJjqG4rGw6ADYGSG-ARApgWjGM8YGzbOaCTp1Yc_aAk-5yHoXGo-rKeCdCJLvJaAfPU4-X4HSrgrhS3ouY4NLav4BxE7Btz7O4v-12yFWClNxNPSu-RsSr3lWGtEDRFjGnD3D1mefAaOw3lqt5-RIhH10Guz2W_rmdGKkKuXS_F9U7DmApsmULZIIOvMzW4LgdqXOYAG-Q40hBR3icyVRmOvU7GOQttT0N72K-U5GHOaJaYPCWbQKSyVMEDGsi2l7xKArJ2-DIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای ورودی باب‌القبلۀ حرم سیدالشهدا(ع) و مردمی که در انتظار رهبر شهید انقلاب هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/668701" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668700">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
برق بخشی از چابهار قطع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/668700" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668699">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مهر: تا کنون بالای ۲۰ انفجار در بندر چابهار ثبت شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/668699" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668698">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تسنیم: براساس برخی اخبار غیررسمی، پایگاه امام علی ندسا در چابهار توسط جنگنده‌های آمریکایی مورد هدف قرار گرفته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/668698" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668697">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
یک مقام مطلع در استان بوشهر: تجاوز امشب ارتش تروریستی آمریکا به بوشهر آسیبی را متوجه نیروگاه هسته ای نکرده است. جای نگرانی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668697" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668696">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
شنیده شدن صدای سه انفجار در محدوده روستای طاهرویی سیریک
/صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668696" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668694">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ayf8KbjVElq6uQHZWxn-APhZISLBT6ocIC79JTZEXwYth4Ey-Nt_lJkWuXgAknYUhQyGjyOCn03zk1_CWkRTWkakF8ZVdDwBQcW3ZpdHl8JNEgngTMilfp3xviZRwUH36tqatwmP7-YT3Zc2SfM7ATQocoeT5Ps-HmsLo8GmJl-njeOYK-sWFnamdAcGycm_Tv5aVY9ev3UY8WAK3A6DqQ4eGqrKeP-NvVJdHBVjoB673m6kxWVNEgCflGFD_Rg4RqpvZvVO_18tcXnT4Q6g7czHaezN4qWHOgkoB7OghAVhDphNN4-hOzjXSaZmcBiAiaOc9-C1AyfsomF9ul8lXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B39ZXw56DAvx5G_XHXRZIFITkdUI-b_zMiSbImmfzbfOfYbHkQ_vr8BUvOOI9v3MCxVx4uELPVvI0F6Gks_CYWIeNSiK8dNyvIFLOAzJVc9CzB20Jix008D8jTiDFQy93SLd_jG2W6QMmyu4O2nf247x3qdquWpXkYc9LQi4qYZ0rp74wCrROYspNZ4ZTkIjQ9mC5f52YWnatlhyII6uIPOn5mACb1viV0lr12H6zKpu9fA-0kD0Mn2xoGIhtw2IRa94XMNw0r24MKaNWqTYN8uXTM3P4ax93zmJ5tLvlZAzEZrMjIjWbqTuFesO3m75z4vtVBJzrSa44hOvlw2geA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر منتسب به پایگاه امام علی چابهار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/668694" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس: آمریکایی ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668693" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668692">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عربستان سعودی، انتقال وجه به امارات را مسدود کرد؛ تنش‌ها رو به افزایش است
بانک‌های عربستان سعودی به دلایلی نامشخص، انتقال وجوه به حساب‌های مستقر در امارات را مسدود کرده‌اند که این امر، نگرانی‌های گسترده‌ای را در میان شرکت‌ها در پی افزایش تنش‌های ژئوپلیتیکی بین ریاض و ابوظبی ایجاد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668692" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668691">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آکسیوس به نقل از مقام آمریکایی از حملات ارتش آمریکا به اهداف نظامی‌ ایران در جنوب کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/668691" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
یک منبع نظامی: پاسخ نیروهای مسلح جمهوری اسلامی ایران به تجاوز امشب ارتش تروریستی آمریکا پشیمان کننده خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/668690" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
رویترز: قیمت نفت خام برنت با ۵.۲ درصد افزایش، به ۷۸.۰۲ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/668689" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668688">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
مهر: تا کنون بالای ۲۰ انفجار در بندر چابهار ثبت شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/668688" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668687">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
صدای انفجار در بخش هایی از استان بوشهر شنیده شده است
🔹
هنوز اطلاع دقیقی از جزئیات و ماهیت صدا موجود نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/668687" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668686">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF9-KtdqsVXZWO_gPge7hCwAM-9DMeuFr8RqMwASVSwWU64sfebV5n86IpubTETRxwh10LN893YOYuEythOOEVIkcayy21FKDHkXxV_PpPFPm_YU2pBp3L_ctU_KR_cCVv12upkGf57zA7NkwJ2I0xlXR4w3ripXN-zThtz2doUbNhjNbKCpbnOezTh4726WwE0FY_z4r2db60ZwEzuCH8ram3rP-okkvdgE0r1rs7VVkGUp94eZufAtIqftC8WC1kedK8v0prvYzpB-WtcNhijP0kRhyKMIUQfY480QEGrudwzx40bRqDBe3cUvpb4edtT8JA5nyo_m6hMYTGAUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا بعضی‌ها با نصف توانایی شما، ۱۰ برابر بیشتر درآمد دارند؟
‌
نه چون باهوش‌ترند...
😑
نه چون شانس بیشتری داشته‌اند...
🙄
‌
بلکه چون یک چیز را زودتر از بقیه فهمیده‌اند.
افزایش 10 برابری فروش آنلاین شاپ
👇
https://t.me/+Xot5PGy2C04wMzA0
https://t.me/+Xot5PGy2C04wMzA0
https://t.me/+Xot5PGy2C04wMzA0</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/668686" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668685">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sclUzO9r2G2nSyUy_dIsk7ZKt7IUpymGhUa9XxOwtKpiJaq1TzTmOmBHCo_fNfUHsS16Dee9lqIHovRZ8QNRmZrT1W4Tih_aFRGJwVVqjCx75rnhvXjFr4EhqWYpwJxVBfB3QnhT2dMERIUABvUuXo1l5DQAIFXI2rorjOA3JQLT1QHhsmj7gXup_8qQisxtMpdqEez5lyaFMHkd1KNzU1U8hlKeUJqQPj1PU2IVLlJWqmWZHxeTWnPpJpp4mzPHGSGAtMfDCajT_HBtXUEdJksl-2xEf27BWiKA5lB6yr6vtzQ0HBzMYaZGSROEjakeOh7H_1y5w422m1UWTj5L2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی سردار قاآنی از ملت شریف و غیور عراق در پی تشییع باشکوه رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/668685" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-a0b8zdJodSMG0Q8kublSH53cQeZjz44OwSAENlkvO1jxMhVGfIW5dZ8_FhkbNK8VjZlQd0y4zRxaETVJLEjceO-d4A2Hk3mSYfuSRSCoMuwxHjVBaoRZl3cFQJuidn82KdYtn97cXzZ54H7sZrXjTH5I_R89_Skp-AXqMEgv1ybE9282KL2IO2mXp4wTGCE-zALbtqtmsRcxeq6tSNVUeZp_LYgTv8hEwm6rzHtAMcc2EsoMzM6xjMjyuPF7uhuBcUcRNz1PXOItyZ65xim84PKE9g9flstdnVJxMYIURvnj3aEbQrVAAFvHwdq_MnnZVY8remB27mWquDGetEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668684" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668683">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای مجدد انفجار در بندرعباس
🔹
شدت شنیده شدن صدا در ناحیه غربی شهر بندرعباس بیشتر بوده است.
🔹
همزمان پدافند شهر بندرعباس نیز برای مقابله با اهداف متخاصم فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/668683" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668682">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
صدای انفجار در بخش هایی از استان بوشهر شنیده شده است
🔹
هنوز اطلاع دقیقی از جزئیات و ماهیت صدا موجود نیست./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/668682" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668681">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
شنیده ‌شدن صدای پرواز هواپیماهای جنگی بر فراز جزیره کیش/
ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/668681" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668680">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: شنیده شدن صدای ۸ انفجار در بندر عباس و فعال شدن پدافند هوایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/668680" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668679">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
منابع محلی از شنیده شدن صدای چند انفجار در بوشهر و هم زمان درگیری آتش‌بارهای پدافند هوایی با اهداف متخاصم خبر داده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/668679" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668678">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
مهر: طبق اعلام استانداری هرمزگان هیچ برخورد یا اصابتی در شهرستان بندرعباس، شهرستان قشم و شهرستان سیریک صورت نگرفته است و پیگیری‌ها برای کسب اطلاعات بیشتر ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/668678" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668677">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
گزارش‌ها از چندین انفجار شدید در کنارک و چابهار خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/668677" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668676">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ارتش آمریکا رسما از حمله به اهداف نظامی ایران در تنگه هرمز خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/668676" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668675">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfwIk5SYWwdaJWfidbJUXe2f-M2KkhDXcU2VZ1Qv9MKXK-GBuzJJMt4_H2bQvhugA3NEdjzzYICkVYKFlz7BpkCBjxgqo3VLzjVfMCsosq1C2NNltaJFgQPMqzvse4Xb--JzxxETQ2l0vIZZCCoOWMgIfMHamzkjnft1XTENzZZIPp6aE2RNC43CM821bDfq8DP3atr6mabwV3qzw7-9g9NTDdIYzyC7zC1D70AnyPsv6AdWtAK-0_URMmAlS4glhWnHceqf-tctDmMiymuzbcGdV7Aj931aOuG8if2btdChlXmsrYt95w7jIdhjGThrGA8_2oF-OlA6vM1xS2h3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش آمریکا رسما از حمله به اهداف نظامی ایران در تنگه هرمز خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/668675" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668674">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آکسیوس به نقل از مقام آمریکایی از حملات ارتش آمریکا به اهداف نظامی‌ ایران در جنوب کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/668674" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668673">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
گزارش‌ها از چندین انفجار شدید در کنارک و چابهار خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/668673" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668672">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfdfe604d.mp4?token=jOjvLL0EKDL0wFTsK1N0h8aNOEU_OcBgQhpZRkBXBh7H4a-D9fho_Rulv-LhtUCS3LRAPdhiu8o_p2pxS4sNaTVu_31NboTXns_M2nBUVKdXqRS0S_N2APeZ0IbJ6Ml5CAuZb_d65am3kEkiEfV0T6cfVaXL1HMUnGERlG-KLdWUGguQjFo3vORWV54PRkZZV6jUl3_RLhwJfayGhmO-ybG36I6EGL6XQ6GC6gknfbFiuLBMKGEglg4P7Cw1cdQK4N82AviqAzHpHGh_ki5ymhwSWsUfKKE9jqOeyG8ILN4qoO4UTPRp06BJNVB2hjWZb0DISWjUE75KuwS07du8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfdfe604d.mp4?token=jOjvLL0EKDL0wFTsK1N0h8aNOEU_OcBgQhpZRkBXBh7H4a-D9fho_Rulv-LhtUCS3LRAPdhiu8o_p2pxS4sNaTVu_31NboTXns_M2nBUVKdXqRS0S_N2APeZ0IbJ6Ml5CAuZb_d65am3kEkiEfV0T6cfVaXL1HMUnGERlG-KLdWUGguQjFo3vORWV54PRkZZV6jUl3_RLhwJfayGhmO-ybG36I6EGL6XQ6GC6gknfbFiuLBMKGEglg4P7Cw1cdQK4N82AviqAzHpHGh_ki5ymhwSWsUfKKE9jqOeyG8ILN4qoO4UTPRp06BJNVB2hjWZb0DISWjUE75KuwS07du8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهر، قامت بست به احترام رهبر شهید/ چهار قاب، چهار نشانه از عشق و وفاداری...
🔹
معاونت خدمات شهری با آماده‌سازی و نصب چهار المان گل‌آرایی‌ شده از تصویر رهبر شهید، جلوه‌ای از احترام و دلدادگی مردم مشهد را در چهار نقطه شهر به نمایش گذاشتند.
🔹
این المان‌ها، تنها یک سازه شهری نیستند؛ روایتگر عهدی هستند که در حافظه این شهر ماندگار خواهد ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/668672" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668671">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
الحدث به نقل از یک رسانه اسرائیلی: واشنگتن از قبل به تل‌آویو اطلاع داده بود که امشب حملات شدیدی علیه ایران انجام خواهد داد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/668671" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668670" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668669">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
آغاز دور جدید جنگ های ایران و آمریکا/ تفاهم اسلام آباد مرد؛ منتظر «جنگ بزرگ» باشیم؟
👇
khabarfoori.com/fa/tiny/news-3228841
🔹
اولین تصویر از محل احتمالی دفن رهبر انقلاب
👇
khabarfoori.com/fa/tiny/news-3228872
🔹
موج گسترده شلیک موشک از نقاط مختلف ایران
👇
khabarfoori.com/fa/tiny/news-3228652
🔹
احمدی نژاد دستور رهبر شهید را اجرا نکرد
👇
khabarfoori.com/fa/tiny/news-3228861
🔹
تهدید حذف فیزیکی معاون رئیس جمهور توسط گروهی ناشناس
👇
khabarfoori.com/fa/tiny/news-3228696
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668669" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668668">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در جنوب کشور
🔹
حوالی ساعت ۱۱:۱۵ صدای چند انفجار در بندرعباس و سیریک به گوش رسیده است
🔹
همچنین صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است. اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/668668" target="_blank">📅 23:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668667">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تغییر ساعت مراسم تشییع رهبر شهید در مشهد
ستاد استقبال و تشییع رهبر شهید در مشهد:
🔹
با توجه به استقبال کم‌نظیر و باشکوه مردم عراق از پیکر مطهر امام مجاهد شهید، زمان ورود پیکرهای مطهر به مشهد مقدس با تأخیر همراه شده و از همین رو مراسم در ساعت ۱۴:۰۰ برگزار خواهد شد.
🔹
مراسم استقبال و تشییع رهبر شهید انقلاب و خانواده شهیدشان روز پنجشنبه ۱۸ تیرماه از خیابان امام رضا به سمت حرم مطهر رضوی برگزار خواهد شد.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/668667" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668666">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ونس: قرار نیست دقیقا به شما بگویم امشب چه اتفاقی خواهد افتاد، اما ترامپ خیلی روشن به آنها گفته است که تنگه هرمز باز خواهد ماند؛ اگر آنها تلاش کنند آن را ببندند، با پاسخ ارتش آمریکا روبه‌رو خواهند شد
/ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/668666" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668665">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در هر جای دنیا باشند از آنها سلب خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/668665" target="_blank">📅 23:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668664">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
برخی منابع از شنیده شدن صدای ٣ انفجار در استان هرمزگان خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/668664" target="_blank">📅 23:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668663">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سلیمی: ملت آماده گرفتن انتقام سخت از عاملان جنایت به شهادت رساندن رهبری هستند
علیرضا سلیمی، نماینده مجلس:
🔹
مراسم تشییع رهبر شهید، پیام‌های متعددی برای جهانیان داشت و اولین پیام، عزم راسخ ملت برای انتقام و قصاص است و هیچ تفکیکی بین این دو وجود ندارد و ملت با شعارهای یا زهرا(س) و لبیک یا خامنه‌ای آماده گرفتن انتقام سخت از عاملان این جنایت هستند.
🔹
دومین پیام تجدید پیمان با شهید و ادامه مسیر عزتی بود که ایشان ترسیم کردند، مردم با خون و اشک خود پیمان بستند که آرمان‌های رهبر شهید هرگز به حاشیه رانده نشود.
🔹
این حضور عظیم به دشمنان داخلی و خارجی فهماند که ملت ایران منسجم، متحد و یکپارچه است و هیچ کس نمی‌تواند در صفوف آن خللی ایجاد کند.
🔹
دشمن هرگز نمی‌تواند در چنین مراسمی خللی ایجاد کند، مردم با هوشیاری و اتحاد خود، اجازه هیچ گونه سوءاستفاده به دشمنان نخواهند داد.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/668663" target="_blank">📅 23:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668662">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/668662" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668659">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرعباس
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/668659" target="_blank">📅 23:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
در روزهای حماسه و حضور، آتش‌نشانان مشهد بار دیگر معنای «خدمت بی‌وقفه» را به نمایش گذاشتند
🔹
همگام با خیل عظیم زائران و دلدادگان رهبر شهید ایران، نیروهای سازمان آتش‌نشانی و خدمات ایمنی شهرداری مشهد با اجرای عملیات گسترده خنک‌سازی و مه‌پاشی در مسیرهای تشییع، گامی مؤثر در تأمین آسایش، سلامت و ایمنی حاضران برداشتند.
🔹
این حضور مسئولانه، جلوه‌ای از آمادگی، تعهد و روحیه ایثار آتش‌نشانانی است که در همه صحنه‌ها، بی‌ادعا در کنار مردم ایستاده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/668657" target="_blank">📅 23:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
غریب آبادی: نیروهای آمریکایی کشتی‌ها را مجبور به استفاده از مسیر عمانی می‌کردند/ ایجاد مسیر کشتی‌رانی در جنوب تنگه هرمز، با فشار آمریکا بر عمان انجام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/668656" target="_blank">📅 23:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668654">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شیخ نعیم قاسم: تشییع پیکر شهید آیت الله خامنه‌ای، قیامی الهی و حرکتی انقلابی است
دبیرکل حزب الله لبنان:
🔹
برگزاری مراسم تشییع شهید آیت الله خامنه‌ای به عنوان یک حرکت انقلابی و خیزشی برای تحقق آرمان‌های الهی و مسیر حق شناخته می‌شود. شهادت رهبر مستضعفان و همراهان ایشان، ضایعه‌ای سنگین برای امت اسلامی و تمامی پیروان این جریان فکری به شمار می‌رود.
🔹
این واقعه به عنوان نمادی از عزت و افتخار، مسیر آینده امت اسلامی را برای نسل‌های بعدی روشن نگاه می‌دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/668654" target="_blank">📅 23:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668653">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5cVxr8ESBdipRJhmg5Sr07IXfZBYSCmMHRqSGkVAV_Bd3oAUJ05qoKiIRjX0pJy9gKjdzJcA2SCLtI06cTLb9OcgGrHgU3hsxP0Lyun0ZwOaruAEU15t6B-iEzLQ4Kmf61OoLks6aGgsCe68x58ZgoOTr0u585Z9RlqElWlVbSSmkknyhBZXv3bUtMTNl3BIoperAr8ZazjRaPF4Apv3WrABxyEsDeLpRWgNdEGpeuGU_g1ip50N48qLOmM9GUowNmW5eDUjwGGmjgXLzOlmAC7R5a1Y-ohi8vNQUD0WyPw6K3PZ3YPLYAy55iiHW7pDzL85_eqO-MpImsQijlgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/668653" target="_blank">📅 23:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668652">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebab569f72.mp4?token=D3bQ-xF_1V3JDcfhnm4iffOkUK8c_5WkiIlWbZs9QWS2jX4tOE5U-yzh8uOV4hgsOgnMOIo35yFyCouvS22jGldYoLVw1zC2HsK1ZYXBc83XwMZAPoK_h-tWe1HVCscmcAYvTttwZgDp86ZPE3u60L7NEcp5T6RkczEcH2fVzBg1J97yJWC77XQQPR5xdIviRjYyU9segsIiCSvRu3_rjrPYojxVN27Wg9-qPHuLxJVScrS3ckobivK7vGpF90YxzN1uI-YAlVjk2W4XIUKY4Rzbn72PMBSLRRXZa5y1fiSf39vpiZ4OfAcn_q6Fw8KEyEhODdIkwemMcEXfgW7jdDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebab569f72.mp4?token=D3bQ-xF_1V3JDcfhnm4iffOkUK8c_5WkiIlWbZs9QWS2jX4tOE5U-yzh8uOV4hgsOgnMOIo35yFyCouvS22jGldYoLVw1zC2HsK1ZYXBc83XwMZAPoK_h-tWe1HVCscmcAYvTttwZgDp86ZPE3u60L7NEcp5T6RkczEcH2fVzBg1J97yJWC77XQQPR5xdIviRjYyU9segsIiCSvRu3_rjrPYojxVN27Wg9-qPHuLxJVScrS3ckobivK7vGpF90YxzN1uI-YAlVjk2W4XIUKY4Rzbn72PMBSLRRXZa5y1fiSf39vpiZ4OfAcn_q6Fw8KEyEhODdIkwemMcEXfgW7jdDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین وضعیت تشییع پیکر رهبر شهید در عراق: هنوز پیکر رهبر شهید به بین‌الحرمین نرسیده است. گمان می‌رود با این روند، استقبال و تشییع پیکر تا نیمه‌شب ادامه داشته باشد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668652" target="_blank">📅 22:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668651">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75948b9387.mp4?token=t4jzAnwhRiJtd5_akClJQcE9dktSNq6-5SW4FlQXU9JtreWH1XnRvBRhmVzN104BPJ-VtpHUwu_u-0vl1cJoifU_FGYcWREEM2g0s2Aucac5CP-d9hR4NlX0i63rgPpawx4LxLoJ4o8PzYlYEg44wQWXtD45oiXrjwIt63KXJSBynb2UmM4YGi9YK8un7Nea-g73CAau9eQey54VjoGIQNDc7Ffc-bxd4J4e7O4eP1GIwO7Pw1dCg1agRrSpIy5WphA5XfhWgGQnDxax-L_x0HdodbKmpLlmzhZi7c6ZGqI4nGfy12KhQpB0NtPZzhpB-0vwuOmnqLMoqfxXbbhmWRZKHUTLOZRrPus5_GGsskWBDSWxOHiyEXcRDhOo-psRuTtPcK3p5eeJKP3SaPs0Kb02GwIa4FhwZR1aXouASKq5qNSc-hHCCRvDb0LMA37wPLF_x_6xs2O59wwb7b7yqvsob9X2pnD940NU7DF_VMBGjLPkzxMAmemgPP7Bj6zGjUbbJ9kS79esgcY4kweaRHLcNq2ac3FaARvAp9HmI__szJOPZWA3iwySuR5Glr-xieTZNM1pEX4kYXO6LpMKHIlMK6MMnIjEF_SlreMJwE9P49VLB0MqbHXRBBu23SbIW5jrxyjvRHPjyq2GfP0MexYbQhUDJZ9muwNMAAmSDsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75948b9387.mp4?token=t4jzAnwhRiJtd5_akClJQcE9dktSNq6-5SW4FlQXU9JtreWH1XnRvBRhmVzN104BPJ-VtpHUwu_u-0vl1cJoifU_FGYcWREEM2g0s2Aucac5CP-d9hR4NlX0i63rgPpawx4LxLoJ4o8PzYlYEg44wQWXtD45oiXrjwIt63KXJSBynb2UmM4YGi9YK8un7Nea-g73CAau9eQey54VjoGIQNDc7Ffc-bxd4J4e7O4eP1GIwO7Pw1dCg1agRrSpIy5WphA5XfhWgGQnDxax-L_x0HdodbKmpLlmzhZi7c6ZGqI4nGfy12KhQpB0NtPZzhpB-0vwuOmnqLMoqfxXbbhmWRZKHUTLOZRrPus5_GGsskWBDSWxOHiyEXcRDhOo-psRuTtPcK3p5eeJKP3SaPs0Kb02GwIa4FhwZR1aXouASKq5qNSc-hHCCRvDb0LMA37wPLF_x_6xs2O59wwb7b7yqvsob9X2pnD940NU7DF_VMBGjLPkzxMAmemgPP7Bj6zGjUbbJ9kS79esgcY4kweaRHLcNq2ac3FaARvAp9HmI__szJOPZWA3iwySuR5Glr-xieTZNM1pEX4kYXO6LpMKHIlMK6MMnIjEF_SlreMJwE9P49VLB0MqbHXRBBu23SbIW5jrxyjvRHPjyq2GfP0MexYbQhUDJZ9muwNMAAmSDsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهالی کربلا پیکر مطهر رهبر شهید انقلاب را گلباران کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668651" target="_blank">📅 22:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668650">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xcw3osE3m1AIdDmLp6YoTdu9P_WEsFjEqaENqrA1DGqvG-O1zCtsgdEbWju-gs2My11cFrUebYM0Ve8sajsxKbggbI_m-fTjup4_6E1C4oeUiqUyEyl9vujBEgPC24W_SihjccsChS-eo3GqyHa0waoEdlZD7mA7TiSlWN3uQfRvxZsCItp1mRkn40dyL7GeLVmUZQ1HVvBiaczLK5O6OghJSfqbIAyTD4inADEJA7t1aCit5a-z11vyHqS5pLOC2C7uC7RXVy8Lf_5ypv2AYhFABzGUgFhLMGu3jrYAa86Lfu9qfBXZXmgj_trxccjQz5tLkgAVVHmDAyoPX3lPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی عراقچی از عراق برای میزبانی باشکوه مراسم تشییع امام شهید
وزیر امور خارجه:
🔹
صمیمانه‌ترین مراتب قدردانی خود را از کشور برادر عراق؛ دولت، ملت و مراجع عالی‌قدر، به‌پاس میزبانی شایسته و برگزاری آیین باشکوه و باصلابت بدرقه و تشییع امام شهیدمان، با مشارکت گسترده و پرشور مردم، ابراز می‌داریم.
🔹
پیوندهای ایران و عراق، فراتر از مرزهای جغرافیایی و همسایگی، ریشه در تاریخی مشترک، ارزش‌هایی ماندگار و سرنوشتی واحد دارد. از سخاوت و اصالت عراق، برای این همراهی و وفاداری ارزشمند، سپاسگزاریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668650" target="_blank">📅 22:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYbZYYVJmd9fTRgB4EgBLXgUnZnXcDKhOqUkJ8BAJZ69LMZg6Lx0-2LjrNwY6z019VBIt15YFLOFjunWpW0DAZfdXqTZyevevwaskNFyESxiOQIX9LZPwMcPUSKe-rXzRF55vbNqnFJ3BaElQofqmTKlBkEtg1kfvYTiWF8wLoLCYg2_9l_C0chvp1KlPgLcqBTjoO9aw0TcXbICoRqedI9kQd6SgTIyAySsXmlDvyEPydN8no2XlShBtmNLMJT8xC_vOgC9qDjrE171l08rOnDAKkKaj82t10l7nRLfV3FC7Xk9avLBLWTyC6E29t9vcJwXhUzALbtKrU1e56-zZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ با «سیستم توالت اختصاصی» به ترکیه رفت | مدفوع ترامپ به واشنگتن بازگردانده می‌شود!
🔹
هم‌زمان با برگزاری اجلاس سران ناتو در آنکارا، تدابیر امنیتی بی‌سابقه‌ای برای سفر دونالد ترامپ، رئیس‌جمهور آمریکا، در نظر گرفته شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3228571</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668649" target="_blank">📅 22:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deb3c4331d.mp4?token=s528raGTrj5PhBKYTe8BXAFvi7PAON7VZYxfJJHGdgCAmYbo-koGy01jsaKc-Uj8CsAkW_TGYGqG3vfGM2GX7Hmhi2Q32koezRUfU9ET8iNyuuKhLg0WIeVVUWfbWFGqwbbgCVioh5yMInvOtF2ZFDc_-2smJS-g8tx7G_7pEKGnj75nIUo7p35tl0GaDUDqY1rQIsCCoHwbvZ2ZrEr2dSj7ZGRpkOyAIfR0mXiixg3xVookBHK4XwSkkTAQ88piSfQSUhqqTw4F7nrn_D3VMsw_XB1q5hSDRuvuAZt-gMzw-HC2GfJYMyt-Ym0e1tBGeH_mUyXYh3iOVnaMav-egEa7hZULorFVDsztGp3VdxvEhmQsllKfhHqlJrrcpo_3sSCD3UmxJvCTukG9M32RixPP9p8KZyy7TmRh7YGMHKOS0aya5ZV2C8Pq-XLevF23EMrdWwPTFT7UzBgdcmS9zE_uIfz2yYj843Q2zpROY9gYC-V3TvTXjz7PvxhD_9DJgqxpxa6eC1qoymW2DktStO4jyMrDRNnoaV-Pg85fhs61lnMU3-33kkcGvqPt6qmdWnSs5ta8VXGc6uuAByobo7tH6jr81RWWeAcDES5EwVO_Oh-X3ml0WcCV6r22qD9YX3kAGJrPX49OAIxzulC4ZvI7Ytyf2VK0jWahzK9sNws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deb3c4331d.mp4?token=s528raGTrj5PhBKYTe8BXAFvi7PAON7VZYxfJJHGdgCAmYbo-koGy01jsaKc-Uj8CsAkW_TGYGqG3vfGM2GX7Hmhi2Q32koezRUfU9ET8iNyuuKhLg0WIeVVUWfbWFGqwbbgCVioh5yMInvOtF2ZFDc_-2smJS-g8tx7G_7pEKGnj75nIUo7p35tl0GaDUDqY1rQIsCCoHwbvZ2ZrEr2dSj7ZGRpkOyAIfR0mXiixg3xVookBHK4XwSkkTAQ88piSfQSUhqqTw4F7nrn_D3VMsw_XB1q5hSDRuvuAZt-gMzw-HC2GfJYMyt-Ym0e1tBGeH_mUyXYh3iOVnaMav-egEa7hZULorFVDsztGp3VdxvEhmQsllKfhHqlJrrcpo_3sSCD3UmxJvCTukG9M32RixPP9p8KZyy7TmRh7YGMHKOS0aya5ZV2C8Pq-XLevF23EMrdWwPTFT7UzBgdcmS9zE_uIfz2yYj843Q2zpROY9gYC-V3TvTXjz7PvxhD_9DJgqxpxa6eC1qoymW2DktStO4jyMrDRNnoaV-Pg85fhs61lnMU3-33kkcGvqPt6qmdWnSs5ta8VXGc6uuAByobo7tH6jr81RWWeAcDES5EwVO_Oh-X3ml0WcCV6r22qD9YX3kAGJrPX49OAIxzulC4ZvI7Ytyf2VK0jWahzK9sNws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرزوی سه ماه پیش از شهادت رهبر شهید انقلاب اسلامی که اکنون برآورده شد...
گلپایگانی، رئیس دفتر رهبر شهید انقلاب اسلامی:
🔹
برای افتتاح صحن مطهر حضرت زهرا سلام‌الله‌علیها در نجف، دعوت کرده بودند رفتم؛ برگشتم، گفتم: «آقا! من آنجا از امام حسین علیه‌السلام تقاضا کردم، استدعا کردم، التماس کردم که جنابعالی را این توفیق نصیبتان بشود و بیایید به پابوس جدتان امام حسین(ع).»
🔹
حضرت فرمود: «ان‌شاءالله خدا دعای تو را مستجاب بکند.» آرزویشان این بود...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668648" target="_blank">📅 22:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668647">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4066b49a.mp4?token=pfSWkWsQaTx7POFC9C3gXjJhOaIZWNG-Ph13TaBsR3Zz9l0-r2kGqi-B6pSXVy3drnEYTKOc7Hy42dw7GschioDdhux_4pMeFuvQiJHHxK7DWdncYqn3Wv_e8zWNrWJzfieS1JEo0bHPCwzkMvpVOc7CTVeCQtrapogEoPAMXa42ILMyCygotFHYjIZ6RSjEmlpehHK9jLD1C4J6tzPHhlYMPffTCHgtnAFFj6stiG0kpMjT-o5OdBz0Bm0EhO2LCkrjViWpwvc4hCWsC7p7m7naKxs3RO4Ib-8F6VVY6pPJKIzRbh8tvBtq6kjfH2MA-P1jHYAgxUta7HCaSA0lYywD9u6ovtU4kAJGq8bRfhdmqCHWZzQPTKXj3bblKbLvONzNcZx-hHTqlVN_EjgHJRcrhRbVlNeLRI9szq3yCHLFuXHVmw2C8iKeGFHpZtSfp-RrAseVAQ7rqUEsqPHqyvmcDaetb-JBSpeNiJeP5bqngA2jaX2pJoxCUM7Av_AuojXtfizXaEmQhwGf62CemjN1MDTL0T11TtoSAZiLGH_q36WIrGX8BftJS9QcX66AN5nD698xP1DUAUOcTmZ20bDd6Ir3EPdyHq72wmpsYw6DzYNK5bg88eU95ufiyDGzvdsif7frILj0mKlqkhY5j6VX_Y2SViYPNi0VCl5LUCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4066b49a.mp4?token=pfSWkWsQaTx7POFC9C3gXjJhOaIZWNG-Ph13TaBsR3Zz9l0-r2kGqi-B6pSXVy3drnEYTKOc7Hy42dw7GschioDdhux_4pMeFuvQiJHHxK7DWdncYqn3Wv_e8zWNrWJzfieS1JEo0bHPCwzkMvpVOc7CTVeCQtrapogEoPAMXa42ILMyCygotFHYjIZ6RSjEmlpehHK9jLD1C4J6tzPHhlYMPffTCHgtnAFFj6stiG0kpMjT-o5OdBz0Bm0EhO2LCkrjViWpwvc4hCWsC7p7m7naKxs3RO4Ib-8F6VVY6pPJKIzRbh8tvBtq6kjfH2MA-P1jHYAgxUta7HCaSA0lYywD9u6ovtU4kAJGq8bRfhdmqCHWZzQPTKXj3bblKbLvONzNcZx-hHTqlVN_EjgHJRcrhRbVlNeLRI9szq3yCHLFuXHVmw2C8iKeGFHpZtSfp-RrAseVAQ7rqUEsqPHqyvmcDaetb-JBSpeNiJeP5bqngA2jaX2pJoxCUM7Av_AuojXtfizXaEmQhwGf62CemjN1MDTL0T11TtoSAZiLGH_q36WIrGX8BftJS9QcX66AN5nD698xP1DUAUOcTmZ20bDd6Ir3EPdyHq72wmpsYw6DzYNK5bg88eU95ufiyDGzvdsif7frILj0mKlqkhY5j6VX_Y2SViYPNi0VCl5LUCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از مراسم حزب‌الله برای رهبر آزادی‌خواهان جهان انقلاب در ضاحیه بیروت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668647" target="_blank">📅 22:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668646">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEqTLgl8PIlWZosGEaLh5YJDr_Uju1PHNg13aXxc29Ipyk6xNdTkdzPF0ma-MSN429CGz60nYe1tRxTCM01N3aLt75RtApzQRXxapt98C73aSeFoAl0kw84IgY4xv-OwtTdCLb3VJVxc35RaOE-KKJ-m2it_BAqflHN6OWPKdHPhJ9-1PWprz52-NkDbrXG2t_m1y4Wz5BWc4KcbjKzsbZFfs5IGxRGYbQ816VnAr85RK_fpOPdvtkF-7rLV2qx_Bfx8weQWPqrE02o2HecZTAOjZlPvnhzpth-TnsWl6jvrhpKmOquCIeqC0TqOZ5-qou3N-QPf7Kv_KqnI7Aev1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی: در دفاع از امنیت ملت بزرگ ایران خط قرمزی نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/668646" target="_blank">📅 22:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668645">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA_ldXul1fWanxgDlHy3SpRFtCSKHKSyK7sFFMatj_FTRlNHbmI7DyAV8xn4awmSK5jmT4IjuXuIj9xUzObaTY0HiRqcVkFaIcTY4OQ0dB94lr1Vaqx3FJk8MCjIEKuWZpEFPObhzk8ZSdLIV46iff-5amgFdFSsUUKLDZool-NW91tsKrzje15znmKfn3cbXzMyQ8u9bkZw67Pt5nz2yZxNQqCoVBkQYTpFjKdb0a6iOZzL0KE516uT_nAsZLMiPEV8nc2eRbme4fWIpwNaoSSfQ0zJW1EKL-aeKN-U5jks5gtPfEjFDCoVtfy6LRMl9_8sLgA-MBkXQ3aI67dMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهد کابوس همیشگی تو هستیم
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/668645" target="_blank">📅 22:40 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
