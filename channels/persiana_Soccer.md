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
<img src="https://cdn4.telesco.pe/file/pMrgRbT3mgH68o5QK7N0rlCkGX5a4mxeDZgpZSTs5zhOn-cUoLRMrvPpUd9tNWuu6r_LgEF7J0yYGPo_8LZb7jbn9RztzGPE9P3LCFPzVzgHkIwxbxe3Dv5xlnHjT1p0gGWcoSPO-MaFd1KH4FqeM6j9usksFrIAKCn56KIBdMQTJAhJ-ddmfH78cBlrbjJSsbNVPBTZIo3UhRk5GUol17a9uI-NTX3-Ooi9UOZf2MZPPAeDm-4eyEJi-KVEhtOfrF2VoKqvvFsWgtW5grP26lwakyuRO5QD3D4Yi3HV_VOL4kYA2qWsdq_AbV5CPoPlsXSlaJ1MpvpI7rhj1pUsNQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 508K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-29818">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3gZbnWyDOvmF2hW86_9cw3Zbs4ztmafpYnQwPUfKSauOWk50Q6_yh_rjPAfqGeSaJq3cGpjvOjp0UAMGBiVjx1X53fbskpNdpXtbTorTD3pwd7jP0s7-9grvMiimQGlwHdl2U21JAWWjm1SPLUDBT-5_G-4fIRF-OQKdB83f-b0wq3166POdlp3nCZNJju8CEpr6AlnxPVb4haqSa8fvpHrp0jQlhVcJOLF6FhaqT1HnnRlkLWbBoJj0rD5AtUTVsOzl2s7rjrUImLLaaai31uUuKnkrkoPUMopVy7qiZDPcvTiSpY8BFG3_xwsjYE0wFRRRiSfLHx5AnM2JFAb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/persiana_Soccer/29818" target="_blank">📅 19:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29817">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmFIWl8Q27AlHsjJmSPy2KSN-R-4CpFA8sM5PtZD6gGd1xRUN_t98LIS_wctd67mw96VCHEYS9_nDKCttsSSeZgmt2-sTpXxEgky3avE-RhHbAcw5WpgZAQ47-6fMxzh8H4e8ETX9173QQXE59RQ7blaETqwX_VX8qu1D0MvKk10eVA-1mb5C6AzwywOJYyQ_km6_P_xlP9SdBhue2aArgXWV38610T9I8giW8JCT0jJ2iErJ0ctYvIaClmUbKHfIyrS0v_onPgR0b6-0fH_5OPM4blGm3IlLwmYGVodFEodGOXPBxK44TPBOWnmjPmihjvb1MSCphS5qoqIx2AE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/29817" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29816">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf-egeZeABpSkupE6yRcV0ZiIwJZEssD4ovQxPEW1_0Oj0J2TNUHw_vHhHcbHPkBbG-DlUs85SpwZ2zpr4QtlugDRd7Cg8_vJqO5FeY8D4HyhTCXjCK-7rjSgnict9jInVC9Bw7modJyvCMx5svlMXtRYlQrsUmIvEoCjIGOScciUYmrUEC7sZF0iX2ab3sXfZ1CQQhjRvpwYI1UPlUhC_oS8_zyIWByWvJ9UqS72xFnKHZha6kNA88N-47OXYc_n7GZ0PAcv8_Awzfn9Q9AgG17KquUa6qZdDJYiZ_3FE0xSlKni_e3US3RkezdFWvKmQq8avtefnF5Nf8_b8s6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/29816" target="_blank">📅 18:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29815">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Nn8IB3Uj1FoghQFPJlLhNiqaBoAuWjKKBL4k_EcheMywyAGMRH6GuBLxfoAX9776-MaZyY8nlT8ZN2MdSLv0m6JE0FRN0onUC2R5UCQ6amYbigxuuiYfbaeQ3pqOZwitf25n629Oth8K5S-WLkyXOxHr7MFfI2HsofZWJ_rv7dcYdCFxnaZxSKdAAB8yZj2kcMhJwqciOb1PymlKcWOXsxcBAZXjuVmgmXbIHlcQqxr0XBy7O0L4zOm9_A2h0arCxEKBKLWA1kn9UQanyAkehYV0mXOsBFrP1TKxm7QLSKQId054P8yC5754zyf1k29rAxx0IOOieUlAihwGo5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/29815" target="_blank">📅 17:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29814">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlMzHRvFCmKN-HaQcw52B5JXFUBheHk77rhCYxnoDJusxp3HU7ol-q67CiHkI36CBgc7FZMdcXLt-mXX1JCojy6mw9FcieicBXSHsedMwpepGutYQK--tns3FbpUl6x3yRsdChCUBV0UxNfEfcnKfdP4QS7EoHoMe6EhUnnDa6DOcjnY_obkatvEKZ8FIe2RSeCN7wVfrKBWg2F4kbc4wyQWYjKoIHP9s8S73yCEyYYtncQZNzj8fcss_0OgW-A-0WnFAWFyqd80CYAaLT_4EUBZeSfqW4IijuXjTO6ZJe0eNOXkUipcTs6H1lT36yfWIdxaSBVt75MA25EsEwt4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/29814" target="_blank">📅 17:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29813">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okyr2B6VBTDObiVBxbI9sbf57YVWJJGeYTCj1KqcYXTnJc0Vay9vZPggXVxv8EVLqZJ5gh6x4Aj7dKVsnm3xdRp7sjPjMzoSmNwSe-EF17fQUjDZ_Xfx_L92v7vNXUtTCSTRD46pX6vOuhx0JbMAV27RV8zX3kidpUzdJP4HlXPrLk1Zxdi4bxKDVMaGWOI7ByYAVj7pXhkre2ifWneY9FD2CyZLRzwAD6SLA4FZh1ZTXNtDcUxceygUgOWjl39lme88xh9GLKs4CpyNh8lF5RYyOxfmZFjChPeMKVkLdY5HOwKL2fVcU6EINrlt5d4Mrptm_sUhvHt5zAQiBQh5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمپین تبلیغاتی جدید سیدنی سوئینی برای پلتفرم Novig هیت زیادی ازسمت ورزشکارهای زن گرفته اونا میگن این کارهای بانو ورزش زنان رو جنسیتی میکنه و اینجور به نظر میاد که تنها استفاده زنا از ورزش این حرکتای سکسیه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/29813" target="_blank">📅 17:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29812">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seJ1i3ny2Js3u_fplyMlYjeprclWUNX_UkW9OlN22W-y1Jf97brhEuhWoh779awhXrrxaGPQYvbgfHUxt8vdqr1Idv6NLGOOZcvXvi2oMMvaMDIP-ziRImPp3i_NDkjZVQbeHMnXjsgrpLHA-GD404ys4uAfXwKCTcxoB6h-RJ48IueyJSW490Dv_gvU0Cgo2KMszjl4duhwgzyX2ynnhwvCQ4qw2sw_RklY0JQzRbjDHHBL_DOB7tiHUiy93HbRX4-xFIzM-7VC1g8tgjdwY3GWY3Fddvoo7c65bMVfM88XprNj-2-zN40FZ6R_xKlDnXG8pf1gMnlI5LvjCBD5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای تیم امید ایران در مرحله گروهی بازی‌های آسیایی ناگویا 2026؛ فردا اولین بازیمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29812" target="_blank">📅 17:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29811">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMJHlE5T2rgbvcPIHvCX5BRDgH3eCcnv7gRBY74_A9lAl52uvuZ-54JDIXdNKTIH1NNciivqpxh9SxBJ-C2a7I_J0Sko66VMwDmo1XGTbQEvPmtVMK-UjwEK1vGra7T8OxvxGJ-u_Iv8g-VZ0jxartqMbfKVYrwIJSTAjWpBry2sQkFzo5QMeDpe3AOBYQ7DbGlUam046sSUM0yWjwztNo2pw9r1ZsPaekJYIMpOyPwFtbjYlwFxMiKOYqBtpH0diyPXruALhg5JS-C1aAF9bPmzKG-kLVneQvOG80XxS7Py799RxwDM1wlFVOznjpZNv-KYbuOM3gJGaG_MxO9q2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ویدیویی‌زیبابه‌بهانه خداحافظی مانوئل نویر 40 ساله از بازی‌های ملی. نویر گفته دو سال دیگه کلا از دنیای مستطیل سبز برای همیشه خداحافظی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/29811" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29810">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQFxB-RwN4sqe7BRpyYp_QXsk4M-uCwbWmQO8nhD0FDvBPsXX53E5Sju2k5FCxQiZtwSOUWOj-3gEynnCGBwNldjQ4RDiMsoyIUHnG0iiz5qINYHcuq1u0SySv_nblbqY2_rHm0XA-NZb-phog9X3pbUTebeXDvD4WRpT6ZYmmzVVRUj1DMaFKJ3zS8eX66Mj5DGxe7moZDoJyIQG_zTcs6CDFt4dHgUKGaAUXI1fD42i0VZJaEkIpVbPJojxrLTc1MLaWTv-wP_51xJ6UmttOauv1KDBfAqpzJrzG5fOq6onoNojG3w568ojvvTOY633UBzV2lBVJ39rv98RKHqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/29810" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29809">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJJfE-C0qsRKaH9CpqyiSJ2eykZRV76-rfL4Qc028DgUdNfGVhHMrzg_cxDOJyhmiRjo4zKqBpivnWP6CgI9gfklpsemusFnIHRzOHc6tUoSMhQv--Q0UdCUOfPG9S5EYykdWVO0FylGQASEAZs2Yk2GcTSZXUBzOPSd-j_idUmJduXpyoo2TjvAmTwVWBlOqSJC96Cr2fqpYRAf3Q8y9jzH-92MRc_4JBJ1MRVaThVqAXYSIUSVU1drDH7ZtY3ZINN8bNVMVVBeEsh6BSvamHjYZQxgh2RhdPHNgrtDpE7s0yg1jTL5Vuu2AVC3Fs9I0_KsiK2VOZnJgjEWg4HfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/29809" target="_blank">📅 16:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29808">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX083ow9_l104AtkGbDGO4R2yJrW_HUKgI9qMhbjI5_CWFFJ9IAHefxBoYvHmODh0VV6FqO0GH3YdK2ewnzbJfGbtshl5RdiFk7XigSoRSbq6N1JYi1BxKKCSnkOi3E7oMJ5_IFuVKZFOooHAPlGffwQJSDIlic5RARCpn00KJhSK5GbmgBuupip3NxDDm6TEg5yVZY7_m0mxepdqtvHxtRmrREEZiUpW7dOBHzUWHIgPrSyE7SdJ3KNTuDyyNSx9RlQHyHxeypW7_UP_zJ-GPFFBNgSIfD3R07kxZEnt9_hKQ4zCX8lRGAgmRqNfWIo3SLDqy5NcB4RVbf4wJsMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ در قرارداد شهاب زاهدی با باشگاه جوهور دارالتعظیم بند فسخ 150 هزار دلاری گنجانده شده است. هر باشگاه لیگ برتری که شهاب زاهدی رو برای نیم فصل بخواهند باید 150 هزار به باشگاه مالزیایی پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/29808" target="_blank">📅 15:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29807">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrUDIQUyXDRK3yVLrW73iIp0zjA_BAWQ1BFeCkRft2_viZHhf7Y4h1wm2YyMvWyM-GuUsRCMujZgbBaZZihTVDFi8OBI4ugGTHDc9kI7eHqDZR9AkjuGO7V_ogSngPP_RJMjAFnKI0pic6gCLa3qv4jA1gJiyl3s9tLL8ADKLA4Zl29Yl4BDMvzpkgTPCRai_wudYg9tdc-Ny0liylt9By5jTQTjH__JF0KhyuB6dwOXqhO97QX8hcJ_pwQ-FVJKwerskNREqm1TX9-R3QoZ1-cEPgvxbtcsXgUqyNFY2-u9xsCbdlQRm_TXWQ9Z5hlfPspyNMhvC6-gRAzvNzPM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابل‌توجه‌مفت خورایی که با گذشت حدود چهار سال هنوز نتونستن‌آزادی روبازسازی‌کنند؛ ورزشگاهی که دیشب‌استقلال دربصره‌عراق از السد میزبانی کرد ۶۵ هزارگنجایش‌داشت و ساخته‌شرکت‌های آمریکایی بین‌سال‌های۲۰۰۹ تا ۲۰۱۳ بوده. هزینه‌ساخت مجموعه به همراه استادیوم ۵۵۰ میلیون دلار گزارش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29807" target="_blank">📅 15:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29806">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAZUuudk51XK-HZlQRPedNCk6zRDZItPQlAHrvIj02C9uv_eGG9lwb8ide3o1hijov556zIYQ4wIrnFw77M6BldG48tBBklEMRru1LDBAeVa2psFGQPehmY9IxGMzqT-68v7w0EFmx-utn6rEH9yh0PuRQhi4fkvF3LYtEGrjwvuwJDy9LhpvZ4lgFbQPJfiq0K87aby09eiIVpCi7jwePO7j-9hq0_Rr4qhFlKMPrW40VXmC3S4fOWN7kOREXDOXAiBGJu8Njclk-cAcaZv6pQ9OywklAvYMgIUaCqXwQbL1icT6YQPlEiUQalli-QqFpAjHQG9f6yrCxfJwZ2Aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29806" target="_blank">📅 14:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29805">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdv7NG0fsc_QnztDr4SZkqPO9vW7cjBdFDYdN5T5-z5U_4C5oYQDAcwkJ8qbtyXto4EfVaqdKyqCj3beLB-WartrHygEryO2f8Yo-m7F8qcrnYCg7U4MiKAiNNhqfH2WKlNVHOlBprb4PhoHc2-F9JRwodtbJocqCYVx3HY_ciPj9bJ20U2w0loif32h7REl3eOGBt5a6pWrHdfwIbN6w2ux7iY4Xi9o4wLlykWazE9P8ZuKX7lMMZHeHK6q64WYha0xFiQL7VWu5XZt_tOy2fo2OBqt9g7DKn-GtuebQ63AfJQKpNFMQKDwR7tlkPPt8hcos6h553nqvUT-cB1MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امیرنوری‌بازیگرسینماچندروزپیش در مصاحبه‌‌ای گفته بود که خیلی پولدارم از هفت سالگی فیلم بازی کردم و اولین خونه ام رو تو پانزده سالگی خریدم.
‼️
خلاصه‌کلی از اتفاقات مثبت زندگیش گفت. بنده خدا فکر کنم چشم‌ خورد دیشب‌ تصادف شدید کرده الان بستریه. زندگی‌خودتون رو رسانه ای نکنید لطفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29805" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29804">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-Yd84dbHesu2I6mzpFGOzq8w_f_VKC_h1QuX9GOMsOLOVoqt5nemaElvhDO22Psjb3f05cmsmJwKKE9dAjyauQIg8timxbF4NX9DfhSFSVYGmGvN8oedlV64EuTcJ01ZsG8RVZY5fSU_0yrFq36YgmDnsTJfxKN_TTuf_VNO1LmBLfWuOnU0fAi6dbwayonUa6k9ZSV_A63UDVvCk_QX4pRcK10cQgBrZLf8tFINNFwPBadt_gBiEMeQA6Ss5K3kLwYnb7voQZoPMUKkY9w7mH42mPEJzzRsMWaSvhPb9BxXmX4I-Lffm_Tl9SkgfMSfR_Ym7CqxEFgBMwx4y-8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سسک‌فابرگاس سرمربی‌جوان‌وموفق کومو در گفتگو با گاتزتا گفته در وهله اول اولویت فابرگاس موفقیت کومو دراین‌ فصله اما اگه درپایان فصل رئال مادرید به او پیشنهاد بدهد باعث افتخار ماست که با باشگاه رئال مادرید کار کنیم و سسک به اونجا برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29804" target="_blank">📅 13:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29803">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ1XqGhADuWfz7MwRMUPjwUBnlurCIKW4NjmJoypq8VVVijUcMASSVDR6MYk0-RQHvezKOmuoXv_7ddFToRoh9mrVwKvXEH6-N4k0nLGFCUcdK7gnN-3mNUlyeeJ4w8DhOHHl-WK0v0TBHV5CS-6ZVfQnKj358R_WHJmXCEz4Ty_NH6R7J5l5Me5riWpTUKXS7B7RovCgLRBx5pxTAJiTuE68W4J1q0gYba3HTVmsNHV9Ed8RncL81vXJOBijjZJWat-2uuKHckF91pgH1pT-uCQWs_Hy6te8AlF2POiRdfVETIUicvdoTfxcwLbCkgXU_MMArkBJg0-YMeXPav7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29803" target="_blank">📅 13:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29802">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TALA5qbb-8uPfnBNkPk2K-yUSIhhbpzoTDXYbSNZxWdazlrl1OH78GGVrOI4M0NPOdrmwk6JxPnsx37r6Vy5CRx7QRE6LOcz8WEjImEFBNXWImqyeJ3qeKH7iMZSoWZbW1PxAWpnGl-0h5iz4HoiPGxV8in29flMmv4ZrhZcvlI262DNcMuQ54uWI0tG_UCD6Db_1qAFIQXnOrobqSV9t3iMMPs3SBYbEFCrvivStKzxvQwjnDGUN4k5csSHgPNpJ9O21YbFdrh9Y6nZOX_hAGMRIntWr_VhKB4kfklAfIRTPfcrNOdbcpwPm-gr8YVhRyugCQkewvJqg74o_QcaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دراتفاقی‌جالب‌وبی‌نظیر؛
در هفته چهارم رقابت های لیگ جزیره؛ لیدز یونایتد تنها تیم میزبان بود که موفق به کسب سه امتیاز شیرین مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29802" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29801">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOhqP8Qs8F6yyAfRYnwD-YPTajypokUoVWVatCjAgvmOVhfIomNWlvAM1c_kWegM_c4BTbzsDS0rQXQHoKJglBmkBwzy6ICj_VGLmQac2PiaAGLG5JTMXnOfJljJzR8xl2-xhcBfMvBhJhvd9Uu1a5uwIrJkh9a_ia3el9nYTQQi0BSKrSKsCuQigN0LJa3ogHdq47Xsgttjwu-L5egGFY4pe5xY3yRuWriMvnP5JaydNbT1fsdwEAObbtB_JkpgUshNYZfqLkaks2oafBuV96m9qop47p3DVBmfIzAI9-wfzJZzHqEUbdoTTsGvNjnJqsYUoia3c4UL-RvmWoBiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29801" target="_blank">📅 13:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29800">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMH5IVhTzHGuAqreYxQWbS3sFvzbRUODjydhGfA4qFtZgZmz4Z5jOxpysxhdr7g7jy2Kj2WYWERw6zNf6ZBAoGHDq8NoWT5bSLQQ8_FzzOyNVnybQaCvtYRetEPW_I7d2rHaRDWFi8_pPt46UWdU_GZaQLDcBPqzWHd0QF0Gt4rvafnJ6DWiwG-OiPFU7IAHL4ThPHL6MdzWcr8w-bKo_U8ty7dGqpcGTkH08aP3b9AVKnnhdn96v7WgQwzA-c5BWevdmnIsL6YhSwo4GxOYEV5lZdbPqXltP2qLsNZ13te59RlCU9MS1eFAKDMD_1EMT6YU5xMCacz98X16_k5uEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های علی قلی‌زاده امشب به محسن خلیلی گفته درنیم فصل با پرداخت 700 هزار دلار به لخ‌پوزنان میتونه موافقت مدیریت این باشگاه رو برای صادر کردن رضایت‌نامه علی قلی زاده بگیرد. خلیلی قراره با حدادی و بانک شهر در میان بگذارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29800" target="_blank">📅 12:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29799">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5gIcugYddcxhqc1oe45nuz7-fDKObA1S6H-9dNvhq8TPH_Gzr_1zpYfyQRDq0X_UkRYcLJK05wcLrbfSmJpQOKPW1jSu7McHqNd9fEBWW0YiAj0VPAkSKcGtWyg2vhddTDxwQsnKhxX9UQXoxGaDeDorti5awKpDn0GO3Zig54E11MiMHtJjJgDcxWlF8SigLc_ekMy_PuegLcuFJr5JJPfHQUmNDtgQJ7l-Qs8IYJ3nO6ZPPJusBPJ0bWPsKh31ixrJJ_tls9nJXWBjoUXMFvkt0hxKhvhFh8gL0b_wBlt6wSW_uNO5-NxF28aU6_l6zs4nOanOBAtG1V-l5dVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درخواست‌عجیب‌وغریب علیرضا بیرانوند از سازمان نظام‌وظیفه: مریض هستم یه ماه سربازی ام رو بندازین عقب که بتونم برای تراکتور بازی کنم!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29799" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29798">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O18BqiBz4P4EuFj0S-lgssmghXM3JQXDG_EiCzfwZxv6RK3D9bQFn-3ykKHFvtLaIRGM5wQlFkucbFRUenKv_do2Cey_7sLDCR2KR4tsJmYW29kyw1Pr4PJihpinn3YgL5y_d9m9w9WJDE8iy0xLjKEKdAFPSJO_qtvsKzhUpOimAFM28M_XAD2IunMs1Fc1N8rQtKS7whGyHbAOUsgbyFO0Smek4ExMPTprQ0ycLF6zU6dk89Eph1BsvbSzgtYyQFm57LowOsbHPNSfVVzRXB8UT1I1F4Mmvc00f2f0fm7Rsk9pPJvcgkL2vm0dz61LS2wtYZ8q71BkLg9_Yua7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29798" target="_blank">📅 12:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29796">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vE5P8hWoGMM6pdQLiv8ntdhqsNyDpCxn5tD_ocIJjbBWZdO-977H9iUxNaFj-_wtaDQ3f0cs6fMMjEuslzCDs6KdS31uGd8r7YeQHv-tcLuAY96Jzr_qKJepiEIfuMtmj6jOx3UvLQXNbdN_NVTueV1Ju5eCBXROIL1PJHyaut1juQFaYYg29cpWUYP93-L8QeDjCe6jteLejO-NOmOtx87COqDHfIDT67EjLAEua_fdrDK4MkZ-CgEXDocMhKYhcWbG02bGtNvY0K6gS8rgUktaYJe_zQvMEzLtNpTWNFRRsiGaeKa4P4QB9CDQtzqi8d0ZB35DaVgGOhge81XjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQesQrGQU88TTfns74rO_bunfUFQvUS1d6o23JnuHNx7vZWvbe8sJH5mCFxUs2WWg7eB1ObW0dxHj2-JOs93HYJOsdNAV3ZRASAQoGSStSYo9rXypFFU2NouVl2gvaPoI6VhDt9172Gx5s13EaAO_FfKC2zeEZFdMnaMA8p4ANkSTvtUOhZUQJHyhNOhoCOLDlQjzvZQA8l4Oa9wd0oUZh1FSMCa6UQCbEJ8PvIJaepZ_Ew3x2JYxggoZ-q8QBxqhxU-ygy3DOSlqi3zwZsD_dcs9NdcsSm12LHZyTxVhM7mlkP8A3hh5zBu2WhP5eCm3wopyCPnTCd65Xp02pOXCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
تمام قهرمانان رقابت‌ های لیگ قهرمانان آسیا از ابتدا تاکنون؛ الهلال‌پرافتخارترین تیم قاره کهن. نکته جالب این که تیم الاهلی تا همین دو سال پیش هیچ افتخاری نداشت اما درست هزینه کرد و عین باقلوا دوتا قهرمانی شیرین در این مسابقات بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29796" target="_blank">📅 11:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29795">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPYWIzRZ0Qhckvu4yC9C6Ib3Yj87MjQ7jb4NoDC4Hjr7yw97a2fOoZg65y9N6lA580epZ414VFjue8zpEx4jI3zSQBTJlYSXuEQ4K9Wo6wAOs6UKnX5GH80yNRXrqUyJD_eAnmCUicDvK4_XHr7uvDjYPPt2ENKsX9Bz6biVwg_J0PdJPfckcsIQYFr5OYq-mi-5ggSrTd2sVyQDTazUhdfWoPepg4eNLrg_5_uk5P0dzTYvCLgTaSFHXogFZaGm9HKhH41KoVjy-0q5wrH2JoVfrxnCCPGPYBSh28nB_8H7dOsZz5Isyrf3wY78L5n4bhVWXw1rJtb_hXwRfoQtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابیو آبرئو تا پایان نیمه اول بازی امروز بیجینگ گوان درسوپرلیگ‌چین؛ موفق به به ثبت سه گل شده که‌یکی‌ش داور بازی مردود اعلام کرد. نمره آبرئو در این بازی تا پایان نیمه اول 9.1 ثبت شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29795" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29794">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to9iD7gAK0t08Y1ZOSbvUUamWCLnxrPJUWzGGfUFb4ah4Esi_frhzkC8WUgvQ2alo5vwgnIssvEVoX3UZLCJm7kUHQFUJC5zPvrC8tB33TK_RzlaCJz5J75HSUsFlxca-NEyXEdjt9xTWLOMbvf_xR75o2_fE2Z_x2J9Zmv4V336Lz7ckIs3HzYOtzrdhJa7wktWtgTfUZ9fIuowDXtau8Tog3IOpPgq9q3Gdyw13JuLjQ57eQMa5IwQE2bn1olbEehIgD90uaJoWWKqhfVuCNy3fqdWIo__hREvCaRUiSZ1toJFFxua4j-BSsIsY2xwQFmnT7xum-MBzRTgWvlobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29794" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29793">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy-zOMB9SYABT9uqIhGjm8gjr2J68Zxsyg5UswF52wl4gmKHZCIN9o6dWXAWQibCCzDFdEbsnHx-m3UNe3jDUCfaLyzVdqBbUla_JQ7G9pwCK5Yc5GURYnrEBTe8AUe6-9Zk7Ut24MVWdBFvN0wk8TWiB8ey0A5OUHsi0N6IIrDPcOBjASmWmHhU6zU0-LispxydJWxFnRCHJwFMO8WYY2cTA5nUIVrWwCQH0ZgFW8TymM0nPEVlxOvUCVbL5LPBIEVrrgP2v9DAQ34aAUqg3PKanvwtizF9laCQul_qcoNgCGRb8_GZ1EVta0Fbn0W5vU0qz-Kq72r_oQ3ozc1bkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29793" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29792">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29792" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29790">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPLHQDHcs3plerZfi71pbg8pMFBZyHQ2ZdWIu8MWWt-O14ZSdTayQzFqC9tkf4tG1YpEcxLpD24ySocnsBxYAohwLnrLpJBEChK3QCB3QDZ3psjNJnJPu_Z-bMtWDJM3e9Kl9DgTnkZfZcdDP-i5rBjlOML0yH5o9ll9aDESKT1qSqlfy3-rcoBJd56Ks1nazO2I2nD-sOr-JQMT3HmpK0-V9BYlEoJIOyd7UijQy9qsVztbUYtrajMwf3OPC2gcX1WAIY9vqr7r0YXwX0Qs1t7YYQ0IdU7sDbYtycVykBnYGAHrqLy2dJy1saf3O-ek4QyXYR_tU_d8O6Kj4xtOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29790" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29789">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3JS1FSa1KPlh0K2wMh1iY2gzteVX7rs6SYZOMOz8PTgCQOvBqDK6mcQ_GxjRZNmKDPvTFS7GjC0nBo-JrTVMl-l8sUmy-k43nu7I_LLvCdBIf8gxCMmuJNF69mED4YXv8XydWNhMochXi-QZgHlC6ucx0Q2-gmGiVMguYNMImxDSeNGA3w0pshcXR122lQhEskhMqP2ss_Ho8zzT_vh78GXcErnaEnh4tc2CyCTJE0vwEe8RxNZmZqDM-ZjUD7E2hMZNFOcJrm2U9LgupPzYqnclXq275FazOj-A9_d9sS1wTZ2RD0kvZyjdpbMBLrSJ1KZmy5cp16gy_hK9TduVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌کادرپزشکی‌تیم استقلال؛ مصدومیت یاسر آسانی جزئی بوده و او مشکلی‌برای همراهی‌آبی‌ها در بازی روز دوشنبه مقابل السد قطر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29789" target="_blank">📅 10:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29788">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntASYxpl_OA0YxDmKtKOZ1GhuS58uXzd6lwldS7n8IJGk9UYezNsW2u29dxGqNBW-0228OcLM9FZrYwiLp-34hdTz-8W1IRt2s75zu5EeBBd4G9mIze5pyldjGXdA0FXMmD-qa7hliTQQazk5vUkq0yVfa3KcYM4-Tul5a1r9vF1gB4mtlHW5hPBOKSiA_vY3aW0zbJdfDjFbO_1bv6vuglxSlJg47_n4fE04H8kg1C0xeNNs0oJRH-vO1RdB8dgc6L-wDP4oTEeRj8gnOx-bYILJipl1VzRM7u9h42U4VDdUFYksUzupRc-FFuEJpDt-bat0XjbTfT1XLFwtPWURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودیگو گومز ستاره پرتغالی ولورهمپتون در کنار دوس‌دخترش؛ پارتنرش‌به‌حدی گومز رو دوست داره که تموم بازی‌ها برای حمایت از استادیوم میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29788" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29787">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=LgqO-nE12SIpyLRE0Py-y7nRHzGuXFXHayaNVRnwX1IX7X2MSUbNZG0NpYf-y-0p7rR2y0D2kZm5y5kWPNc5Cd2JAZyf-L1Ii34o1zYirSUckWMRhQOpOh1QXM9kFhVjpa1qyfLjPsl34aK2P0ETXgxO3-d3FlpRYEZO5MVa_5DTNQaDbqhjNH6yk-VSkJTbY0UqV5i_ZFgX1Z7OvYleJQR5BNQHbxAjDi-AeKkQuzG-zs7AAbp1_qNT9dLIhsjGKsf1lrLdS6SDlr3Rq4ZIHVWsA39YevnxxEeC4MvKdUHB26MULtbaUWZYD0c_5hNpQV2-BJl4BCtRd4ak_8hhgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=LgqO-nE12SIpyLRE0Py-y7nRHzGuXFXHayaNVRnwX1IX7X2MSUbNZG0NpYf-y-0p7rR2y0D2kZm5y5kWPNc5Cd2JAZyf-L1Ii34o1zYirSUckWMRhQOpOh1QXM9kFhVjpa1qyfLjPsl34aK2P0ETXgxO3-d3FlpRYEZO5MVa_5DTNQaDbqhjNH6yk-VSkJTbY0UqV5i_ZFgX1Z7OvYleJQR5BNQHbxAjDi-AeKkQuzG-zs7AAbp1_qNT9dLIhsjGKsf1lrLdS6SDlr3Rq4ZIHVWsA39YevnxxEeC4MvKdUHB26MULtbaUWZYD0c_5hNpQV2-BJl4BCtRd4ak_8hhgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29787" target="_blank">📅 10:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29786">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB4nTy8pQrI4ENPSP_RHsyGZlrP82oYvTiTT4TvTN_iLNJG7Fo0QWefWEOFRT-0yNrIG4oPcNQKRrTHqkrcW1xtrw9deiEOekOB6uH9-F9NeX4EkpGypSI9odnZXQ61z6BTyHcDBjeCnj8UG50q3L6WfMXU9kjaW-1OPFHr-9KbkVIiw-T65LC_jDj9rM5oq7Wlf-o4tG4u4L7eS6I_zoSOnXDuoEB4990SqAJUP-oEepCt329rsaHJ1kwuHu5beLhzxG22-IWqm_SxIjmL0k24anO60UWFtZUNNdTM2oZlMtZZYv_RfE-ILPWQ49Gqv50CU7aUqHJ7nwho8keVmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/persiana_Soccer/29786" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29784">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGxGgYbbtHbUoxqZp4w2LJWk9qstNZvhyPmqMPdvC9FFe-Cx0yEk7XoJz1pm1q_8_KcGD47hZ807eEssYTth7gDzWrT-X7wO3QgPiLTA5dRJ7WFLXTicZWFp3LYzrwDWpZOfpWcArA8XgJ85WJiqjpLytVRm1JZL2rv7UIuU3gwRKBLXj7yjBET6k0zxRntUyi4epfAaaSjD8ZAaQLB79MXJhwcaLehUb9l0tClcHjf3cjoLUTBjOdUCWriJYBzKOlyKFNjNaK1QTF6YimxerNGLgHBDMiOhDactBfUPzvV8sCfEJbps2Xd7ugY326pu0voaQ8Fh5VMVY1ztVqzXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/persiana_Soccer/29784" target="_blank">📅 01:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29783">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFXkCo8rF-56tR1HGJDK-OjliLgCrwLuPXaQUbIBho_GATbPqFQX1FpH4BBIGiVrOmKRMxT8u7-5cnuyWZbmgK0ofdkmMpKUKTNVDELHJAlOYJKdzdlTj62gB0QWyMjNscCNlDtOdmz6g2ofuOVxb8GzJn5O71FUwiyNB3mQ-cuRaRn8LS1oXKNCVqJs3H3xyUDLkZ6WIHcr5g7GQIzyWs9A93zCyyixyqpVi-1uhwIvWBnBBxOvVfDnqGJiwsqE4mZZ5CGCCgOQf_TR_ZgkMorpctDVzFm1CESlB2thRT15z3xwPFo_I5IPPcyq63L_xUNc7dsbJDMypXdqhMDWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/29783" target="_blank">📅 01:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29782">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPmHYryae5YPJAjhAkfc9bXrffQB2-e3dDZwVW1go-suGRVCRElMsSjXgH_F41qH2mrGSDnxqaU5_Mwo6qX6CIpHSERZlMt9aWU3Hxowu4kMitKQNmQq9j252LlsLCDtFKxQIFq14SubeuSp_URKnFdy5t6BWCUp9WrTDuW4UIj6njhYB9BwBy9ZxnOObDbprq0yvO9Z7d8ANwQpdn5bVPPRXiQrg5z4owm66Snhzhk69E6E-efAiZFPI8U079oqS5lg2nl2iZcpcNYP1VKDMWbVzybJVUNRdoFJdCjBCstxk0LnSmtdm3x4Fa6cDvLMqS-kjw18jfvjQkqsBTSp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ تقابل‌لیورپولیها با شاگردان دی‌زربی در کارابائوکاپ و مصاف رئال مادرید با الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/29782" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29781">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGtzqSgNRucyCyJCTGgYyBmm5GNRAb46cU6oW7t0updO-6V_PkmKp7AxEWW4TM_RH-IYenNqHLaYvgCaQOdYxSGuA97qYqalMF3gOpVwyR0Z5rmOCriQnJvCy4y8d9AmvKKuTJLltKuTjWTmtzgrW84tWIol2htt9_qluG32G1qKXeEgKktfeVgm0JtA96J7PW3Do-6_tbBHIZCMr29ZUA-5j-0rXGXHYRnG4IsnwNjCpMKUuV2t5a3rI6u6eWdJI9D4Top0MtefVU7YHSvTfTXWfaIQmM3bvxy1-vMgWioFp2mO2UtZ2TOPULqNAYSBEs9fIKuc_TwuJT9SPzuGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرد شاهکار استقلال برابر قهرمان قطر تاصدرنشینی‌یاران دیبالا در سری‌آ ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/29781" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCD8Gja4WEKuJqOfoU0eZ1zit-mzIqJgBkaIwsCERTKv2-HcTHj433xAI7XueS9sh4c-FyIrgxgP4m4dcxcIn6aiP3QLazKWujvd1J3BJxaQBhhlls9Hkk6MA_7NeS0GezYwpKIBqtxh0xK7U1oDVKyY0bRAzhrkzE4531vvtRSkdoJVlNgR07URThBGftPIQQ3qDyd7Ao-ComfZLcKd0v1E5NkR7M9hn23T25zcPff-x9eGKUI6GMWtaxgDKlq6OigxPcGZ3KH1yjujPAavDv3_HyLwjkZKklIjxRPprrbKdRvwNBRQ7U6ywQrIjtsXdMS16ANJGwmFALseS8H5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیربرنامه‌های علی قلی زاده که رفاقت نزدیکی که با محسن خلیلی داره با توجه به چراغ سبز علی قلی زاده به پیوستن به پرسپولیس قصد داره این بازیکن رو در نیم فصل به پرسپولیس بیاره و صحبت‌های اولیه شروع شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/persiana_Soccer/29779" target="_blank">📅 01:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw9VGvKYg8-rjN78X5z77ufrySCF5XHH8yjfS3saGqrGEiOkQm1p_Dk5srpbTU7RD7h1_PigI0hWM6fbYTV4pNlwSmh7yvPjSuXJTH8qFiHnsGvB9YXyxyUckEX8CRuXOrRS8vfOmRp_sXVZtJ5dSsc3lhspzQevPoz7ikyg4uW4V__IaeTznki58Hf90UwirZ7Lw1P2ZrZmKqwVl49h3qaNDgFvPYL-cec--YvKi3GEx8mCfKYjVY-E1j67Ig9hNGEqp9YScfYZqUnMzuZKhvaVXvqsL5m7tPBoNoddcqSSMHVjTx0DjWOnayazstlSCXWNt92TGlscAfkZ4Q8d3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/persiana_Soccer/29778" target="_blank">📅 01:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRm7k_Ja4zp-GrxcT932aUnNIv6a9tadAVktqiWw8zGHLSRPCm1qU3nqiRbkJDnZK7-C1XQ_91uvVnkwTVwWfUWOvMx948MPvf3CO1HgXoisx5gAisC3d2Cb9LxrkUIILviPS3mnVqT-fJQaasFhyoF3EljkzgKPPisQ6gCnAzdGCuiCKZOMnrqNWNgQnIWj_grACLj6_Srb1iRM3C0y8SYuSmN4dUK5f0d68b8gSHqZsQYuyArqWVPr8ShO2YmGtaTPTB91UqpuzX4cICAxaOqIyi2HUV5Te73letxW6eSk7avrZ4-NRC2Jc1Q9hONrWDJ8EViwUF9SWZpq2vF-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/persiana_Soccer/29777" target="_blank">📅 00:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGt6zNjh9q19f7XI1_oJbBRGiQ3r6OJSoT4pgIo8kQjAOMDWeVKWcnbQOoKB7ShvGrpXTiAiPgN_7bzjpp5AyoRfy9OCfQYccg4oeWeHi2KCKCxsaySr-v8_a_-My2d_MIPNVHjkTQGtzyAUFIpF6645pOwwceTxAcHhel1nvi36qpIz8Dcag5tHdPP_96uRO8NTExMqw2Z5_ilVzk69ATZ42BTxhDfrH_4-806JA7vt6lnC6_KoAIF0IWUsBXMlHSGOVXi58J8z7wCqE41ZVJ_63t6UTsheXA76HucEL0AJFq9B3KRwEwWVj4JOhwellD-6UkovnjcIjc5myXzGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال‌ میخواد درروزهای آتی با پرداخت 800هزاردلار به‌فابیو کاریله پرونده او ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/29776" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgygiC0XvXeRpo-gEO63e3qA9d1ihGZeXbaMI2Rw9-98QjFHUdqPeyhhzAxzs-G5gcyNgxEdqviTi2g7QqRhd_brJheZZtAgUWpBy84tvn59MiVkaa2wiSVN9Meq7_pg330sDKksURU6OrEfLQ4Jmx_XpMMzqUenBw_4aMzkOG8PZnxdG01o9bQuJobLW0F88Kg0BQcw8UUqhRC2fEy-lioyTf9h-jBxpuYOhh6BJRGXrOcHVvsc06sraVPhDiha7wYYvEP7BFW4cbG2F3pb6XX6ac1bz3OZHKMplEgV6CIByraRayUg_HRisnIwgoJKRI2gZ9ReqJCz4LMR2AKzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم سری‌آ؛ آاس رم گاسپرینی با دو گل سه‌امتیازارزشمند رو از تورینوگرفت‌و با چهار پیروزی پیاپی درصدرجدول ایستاد. شاگردان سسک فابرگاس هم دو بر یک ازسد پارماگذشت و با10 امتیاز در رتبه دوم جدول رده بندی سری‌آ ایتالیا قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/29775" target="_blank">📅 00:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29774">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti7834UbECJMTCCwM61PdRkG_e1sj7MCqFIJmSAI0dmsu31Qc57l9_y-ob_U_ElaWYTcaanNB2OJ8Bp_ChGH-ZBHf-5-tQPp2iSbX-Rq2DUg2MBiZpdZycKie3eLhTlNvixYXaMi-eJZEZOgk92ft9Td0vXjPBQCreOz4tsodv6OSpgZSmVn3fpBs6zOUVNGxq5xKcux24CAZJtTOJvPqti57GKu6WvLKf6a5E-fBauzMqVVhwknKVcucjszZRC7Z2QQBO2aiaKgtpTzOSVfViUJ_QuSuF7vo-pGU-RTtnQif9AF63ACqYlxN1nbFy1FY5htud-gnUxvWuwyyA6doQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/29774" target="_blank">📅 00:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29773">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcQFIk_clIJXB5rVELwfqGLFvRc_hFlA6i0eQgUBuW_zsu9c8e-Lf7ezp7f5cu1pXJqAAA4FDkGBXenE5lDPomS2Jjh3x2Qx1PMjleba9p3eu4Jvgx8ny2bxNWURRuW3TrlpcQdeiaBRtBfEEXWFjknbc3tFGUk4U6lPlUu5V6medDcULORBpHk5DcJgME8QNSzvlVXjFxkrixkkt9YKi4rwC4j_N6XMYxiG54dOh0SmKOlzz1K9kS3eff5_I9VRcJhZwC2SmV4MYGtKug8LhnHNc1Bab2a4lUKx_SxjLKFQT71zUkNEwJmnFxn_Jp2ZGn_NCeZf8gA22uIhVoZ3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/29773" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29772">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSHJel-IkUTW2MCxENaiCEn9GK7zyPfM8LFAR7jluydSr-XnBrxQnz4J8IqH8Loah8jxqWFeXy-Z2AYFtfDUN3AwGIQqeF-lDzLpThgYXTVx1stFEsx_omivW9TlePN58erPHDgZdC33BuYj7UXNkkJ9tC4GI148-dNK0RC7DAs4KoG11rg9-Yb2fU0o68MrQRjy61bvQSYPjALC7BK0F_Ui31OUN4KZyjhXgD04j9dt9dTCxeAhBHiUZ6bYuXqj0oNIvhViugzT8CQzl1lmL6SXg4YdgME_9jaDugZTd1T61CGfdq_gCaADNTROucgvnPy-2LZxvfMAq8xqwCMdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/29772" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29771">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvV0eICDHNzMke1wXIvzdEX0FnJyUNMXGtKARh4RBRqqPacX3ilMmq5aqyOJa7raqnNDj-T_nTNju7MQIwkMfghYryrhtehdmABzzhZV8xmiUiCCIJJdXF8iJUtseaBF4JSjOkdcgJ-AEjbma7HOmE8V5QwLnOxdKV47gH8ZuBX6bWe_ebvpCmUuCvwuOc2oSHnolHRhAYqWIK6xV5Pw9YXJ7O2VQa2P7Q0yMY8KTVDe0vYYL2fSwmzJnLTk_wjwDhXYkJ_IFdNDk9TNrcgSQo-RPnCyftsujxjrD7vXXsskfXsZDnoDpzMMYfeg03utn6oAqEg6uq85RlmRNujzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/29771" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29770">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=Bh1K4sn_B8f1y5y3BIB59SOtKF5geGWlADsXMle8VCibhSrpFt_9dfqwIRNWvzPvMqjNGXJ6TcXUdJffdt8CiVBm5kwhnbT9DhwBjlm0hb-skI-LYq-3V46s2EkmyR8Jvpxv57oP5odmvGJCjbpEhnmXaizWl1tPFs7hW9aaDIEhAqA3Yl3LNejlOkz1U8xLCMM-dZo9ngvXtIougrPJghqKUytT2OMYcJMi2cDkJbNhDfXRQvG54WHagW5wqHKhfT2JQ6dHwVNooxdQzMO-8y_03i2xd5HABEttcje2DHYiMIAR8yIQtZehNfHSJys_-reW23umAcXTn56X0qkRUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=Bh1K4sn_B8f1y5y3BIB59SOtKF5geGWlADsXMle8VCibhSrpFt_9dfqwIRNWvzPvMqjNGXJ6TcXUdJffdt8CiVBm5kwhnbT9DhwBjlm0hb-skI-LYq-3V46s2EkmyR8Jvpxv57oP5odmvGJCjbpEhnmXaizWl1tPFs7hW9aaDIEhAqA3Yl3LNejlOkz1U8xLCMM-dZo9ngvXtIougrPJghqKUytT2OMYcJMi2cDkJbNhDfXRQvG54WHagW5wqHKhfT2JQ6dHwVNooxdQzMO-8y_03i2xd5HABEttcje2DHYiMIAR8yIQtZehNfHSJys_-reW23umAcXTn56X0qkRUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/29770" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29769">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7c5VAQ13LAHvg-KqeSnHZ8N6MUHe8CciGK0XfZVIBR8mtCmo7O6ILrzBLBGpJ7MhlSINkymLgfaBR9OIOjfWhQWDqmR6LFTjX6PkU-WjRX4-L25Jc78qqB42XTd-9RUla0zCsqiWnkNvt_pndMyRJzqqM98cdgT04wAEy4zUD_E6dXbOx05tBCKdP7dhJeArjmJVM8Z7YKJ_i_Zd3QFYYcbTvIQ37nEDNtes4PPSpl9kgEl8ofF_aGAWM3Nm1n0YUi4ayU8HytzaP40_p0VbRrSPxt9ITmDdI7XCMlhLplZahLzvNp1dyNFzirT65o3t0I9Wx0CuXPNM5Vzq4Uixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
اظهارات‌ جالب لامین یامال ستاره بارسلونا درباره توپ طلا: "فکر می‌کنم امسال من لیاقتش رو داشته باشم، بخاطر چیزهایی که بردم. چون از نظر من، من و امباپه دو تا از بهترین‌های دنیا هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29769" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29768">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=G_lSX7bBpVUoMLSF2Tk09gJW69M21ux5VG4tR0HSKujM68D4MkIIfEVU0moIdX842kwL0WvcMYPaTuisJ8mR0KLQU1cTHt99jfrgH-yLeZ1ZK_oAIMtfzQsCdwXn8gRcKr-rZ754roPmSEZL03X_xDMi7hRlorwBYe-jznNBvsVY1wSTnWkAgb0C1Btrfk25BIbCVyanWK4_k-YxkOJSYt5y8ya763dtOJEUPl_YJXHcAf4GWTlOoe1UjijyOqlyZP5w0DUtQIlhvygDgsb9rqE_eAtcAvK8tjCKCNEL1EJLvw5Nblfhl14g0XcDaku1taTA5RI6I6nqYyk49_t74Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=G_lSX7bBpVUoMLSF2Tk09gJW69M21ux5VG4tR0HSKujM68D4MkIIfEVU0moIdX842kwL0WvcMYPaTuisJ8mR0KLQU1cTHt99jfrgH-yLeZ1ZK_oAIMtfzQsCdwXn8gRcKr-rZ754roPmSEZL03X_xDMi7hRlorwBYe-jznNBvsVY1wSTnWkAgb0C1Btrfk25BIbCVyanWK4_k-YxkOJSYt5y8ya763dtOJEUPl_YJXHcAf4GWTlOoe1UjijyOqlyZP5w0DUtQIlhvygDgsb9rqE_eAtcAvK8tjCKCNEL1EJLvw5Nblfhl14g0XcDaku1taTA5RI6I6nqYyk49_t74Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
روی‌سماجت‌کاپیتان‌‌آبی‌ها؛گل‌دوم استقلال به السد توسط سحر خیزان روی پاس آسانی دقیقه 47
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29768" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29767">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=eIy4KVAXjTxkG2vn9YzynjbpWq4AZtvU6Eq7efC1kgKCivGdtHwHcN7agoLEWPz0qHb-1KaZuFbrKEj2uXATNqD-QaqoBiV8cETa9fcVv8pc5ctASRuncD6ueGUBrMjD-36_P2sR2Vb_kjKsZlYdOsqaB7wVInWDAO8hBimZ0UaaNZGr8uTY6eAhKpM8SC2vleuYmTvowmbz80DDyWAuEzejDone5FAMnNjfVpL2ASk_u1eWxcR2V_Cxukocjy4GVT-L6OLPAX_sTGwVWhk5vOa1VOtAVSLt7CTdlaQB3lR8rxVmt-J6-zfdbfIGH-XRv9WLX023D7UxZCgs5ItUOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=eIy4KVAXjTxkG2vn9YzynjbpWq4AZtvU6Eq7efC1kgKCivGdtHwHcN7agoLEWPz0qHb-1KaZuFbrKEj2uXATNqD-QaqoBiV8cETa9fcVv8pc5ctASRuncD6ueGUBrMjD-36_P2sR2Vb_kjKsZlYdOsqaB7wVInWDAO8hBimZ0UaaNZGr8uTY6eAhKpM8SC2vleuYmTvowmbz80DDyWAuEzejDone5FAMnNjfVpL2ASk_u1eWxcR2V_Cxukocjy4GVT-L6OLPAX_sTGwVWhk5vOa1VOtAVSLt7CTdlaQB3lR8rxVmt-J6-zfdbfIGH-XRv9WLX023D7UxZCgs5ItUOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29767" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29766">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OokZChzbJW-iuJvuRPkNQTAuXWp_A66uhJ6-P_6OshtNXRyxtk3aSDG0p_sLUfMmLHtznHjgXpfwpAgT4lobuVaPmR0NagHONnHsXsTczyYWsG2dJO5EFUNUvu6Fj8_XWZhpSF5disyT0zcOVFsG1kPa2EJoRGgcgyreJkuAXCSgfmdtSBG9ArAGGDYvSCss3Moh8ZM9CwJg1gxYO6ZVfp65VkL04EBiA6JMLeqEqbLWu69HmuuJ73OOiuCa67pVdumbCZWw94KWcauZsEeqTJVRMPbYgI7vkDYD0y0ee78OUfF4MPsge22YJCd3CxfrqEICn087x9U0pntucyJKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/29766" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29765">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0Ql0D2JDowfkbFunnwfxSFRKeKjUpmXabWjSr9JQlK4NpeLJS8YM99z7V0kSR4nu0LZERn3xoDRb8so5eTY6GDAwMD9k94FNMConN2ImZPsSYMRNlcHmbOVGms6Mayd-IJ6k9RzGgeIpEklGAsaxVfgkZkX8S3Jy_2u7QHSw_-jh9IUd2HYFQ505sJUUrokDprq1AOeujdYtXxxNMJ18bvvdWTics91rQbSZ13nI9oZupdBm3s7IEvEZIucpuf-CU2cx99xwpkZRe7HGhOR9WztG4vn3xO-u8sh8dLFK2Ua6l26jTJzwbaP4BlgLGiVnSqMbZ7N9z9ydhsQMx8tAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/29765" target="_blank">📅 22:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29764">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=ZA_939onLZSG_6oqujx-q9GGsh7c5O2kRfhsqOqCbjGOGWx2MYVF8JQkJa8yjlkfteBA_DrhetBNyCl6DfKWg2gMQ3C6YZYIKm2Obz_OEZUAy_id8rJQEfcKUkNlZuztMcFqOQUxN_odL3QnQ7pcMVh0ZeX1lJXXyQzYsuPkbI9pDMNKqQzXo4nOKjn7nV_SMy9z3dci-ubp320xMbp_G4DbddfjJd7wJAEFzleaC0G3cNgU9iPxKdn9mrsF3tCc37dhmrCGgbmaV1dzKsdq8I1HhpXJE_G9_8T0aGmUGqE7sn_tgS4tbLRiV1YF-x4snMDC67BRMANCtIB--VG1rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=ZA_939onLZSG_6oqujx-q9GGsh7c5O2kRfhsqOqCbjGOGWx2MYVF8JQkJa8yjlkfteBA_DrhetBNyCl6DfKWg2gMQ3C6YZYIKm2Obz_OEZUAy_id8rJQEfcKUkNlZuztMcFqOQUxN_odL3QnQ7pcMVh0ZeX1lJXXyQzYsuPkbI9pDMNKqQzXo4nOKjn7nV_SMy9z3dci-ubp320xMbp_G4DbddfjJd7wJAEFzleaC0G3cNgU9iPxKdn9mrsF3tCc37dhmrCGgbmaV1dzKsdq8I1HhpXJE_G9_8T0aGmUGqE7sn_tgS4tbLRiV1YF-x4snMDC67BRMANCtIB--VG1rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم السد قطر در هفته اول لیگ نخبگان اسیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29764" target="_blank">📅 21:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29763">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orVFUl-78EvjI5MVxSNp65jXvfMqidaABv7hRaUpUWHzzzzxCmobzv3ulDzaSrFevPiHo01i_QUEr72Apvwx_uE5mo0rGu5aBISHpAHttSweEVm9vNgRNfKjIOiL3BJbXhAo5rLEPHdXZnEbUj6Oadr5WbB29dPZtkY1hudn2EHN8Bzpy8YZYEZI1I7pgn0RNVyNKthE8bjiuc8IVl9j4rL09U_1ZgWZeDUASRJwfbPK7KKx1uPAtaXBNsKyPftRT6vJf5cOVjUngP1f8tHY5rT3N78KdDrfw74DkHSA1b67546hMd9BBDohtU_UIeFMtTo1GgthFuF1priN-kdAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل اول شباب الاهلی به تراکتور توسط یوری سزار در دقیقه 22 روی پاس زیرکانه سردار آزمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29763" target="_blank">📅 21:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29762">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=fN_jP8D6p2zRq-MCw1Ws7ykqOJfMG6ZCre9ZtlbQwv-JUR6u6gLpqKJ3U6vs0lyFjXKKOct0LzDOQdXMUdrMJ_yY6_kTLZZDgNkgag1zph-I7GtLcC9_Lxsm22W_QGXOIcBb5X046w8uQBc7Ec3tDpJJ-V7-J1JjKLhXFQ80N7TTfbS6yrSEqm5NruaHTeVhZQBbedRcsYS7xkhbVvhII-mU7hG4uY_eJClnvreoPLrm9MS6Or5mgXgrbuQU6fblp_UKhIzammVl1shnbZzciSh-f_XRmQL1SaBcGQc0ICrAhETokHjkBDY-xINZIRUw0pVvPqqMV7SFo04uMUglzUnneCYcAREqjtXfMeJXIUDK5kB2WnUMiotLS1gycoMgMK5BPy8gHy2csAhd434dIm0pL4zT4SVhPPaqtcJGoIQ4W0goAbsfr6UoO-m83zdQ91eNKm2Xl8ukuagh7d7cQqkc1Bwcq_EQ39aMM63R3WhPVqW8jDOEa-euFglsEo-RmYRcN3VIgk_0Y_oJNffTpJ1dGP3ihc1udYSxFzbd9WcOIn6JOIR5DE2vBoeoNrB-2gxFAZflchF97d7vHtaEKly3jQWaqj7urrbdCFrmHXT6aCuYXc0h0dOYTHzV5hlqDXz-VtBrRpndjc4b7zDbq8fScLk-t5OZnDdpRNxR9OU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=fN_jP8D6p2zRq-MCw1Ws7ykqOJfMG6ZCre9ZtlbQwv-JUR6u6gLpqKJ3U6vs0lyFjXKKOct0LzDOQdXMUdrMJ_yY6_kTLZZDgNkgag1zph-I7GtLcC9_Lxsm22W_QGXOIcBb5X046w8uQBc7Ec3tDpJJ-V7-J1JjKLhXFQ80N7TTfbS6yrSEqm5NruaHTeVhZQBbedRcsYS7xkhbVvhII-mU7hG4uY_eJClnvreoPLrm9MS6Or5mgXgrbuQU6fblp_UKhIzammVl1shnbZzciSh-f_XRmQL1SaBcGQc0ICrAhETokHjkBDY-xINZIRUw0pVvPqqMV7SFo04uMUglzUnneCYcAREqjtXfMeJXIUDK5kB2WnUMiotLS1gycoMgMK5BPy8gHy2csAhd434dIm0pL4zT4SVhPPaqtcJGoIQ4W0goAbsfr6UoO-m83zdQ91eNKm2Xl8ukuagh7d7cQqkc1Bwcq_EQ39aMM63R3WhPVqW8jDOEa-euFglsEo-RmYRcN3VIgk_0Y_oJNffTpJ1dGP3ihc1udYSxFzbd9WcOIn6JOIR5DE2vBoeoNrB-2gxFAZflchF97d7vHtaEKly3jQWaqj7urrbdCFrmHXT6aCuYXc0h0dOYTHzV5hlqDXz-VtBrRpndjc4b7zDbq8fScLk-t5OZnDdpRNxR9OU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه دورتموند با انتشار سوپرگل دیدنی و فوق العاده فیلکس کلو اِنمکا در بازی این هفته با پادربورن مدعی شده باید جایزه پوشکاش 2026 به او برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29762" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29761">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlaGhOG_1l_x3HPHjHei7LCebLR78Ds9pfNcXKU2AHiIA_bLkLCVqX2apFf3v15P2M2J3bqbjqdJaxn9Xh-dvhCW4LMrMZijKEBealVXGHiq2AZQX_fV6nX8_SW0LkwNYzEWkzbUh8UuUuLGyBd1QswtdILVCLBgZG34IhjVh6vgjZKf7yHN5cEug_MKSZ-NGA2Ybo-biWIywQvsov6Tt4IJMHHHoYpuXhviw-B50cU2wmA9VwoqoSIICojXqGuu45vsLsPdgpl16aQZogzjUyQZWb6egFii9kOaX4UNd2CXnSgHlBbf9eY94pqrJFzMPVNWa5JImFDGbKYmhBUweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29761" target="_blank">📅 20:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29760">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wieup3JuJtWU3Ozc1B4CIOJxtA8WlSHurDIk7Ka_FXULa8YfVOrO4_eDNSEjzv6dY14sZyVIuTIjl_XCu5EakIKozBs3YfLdBPhCJR1jUgxliwCqmRQ1uSfzQ8UXB4fw4oyhVPZLHaAN7nt86TuXad54fjIkkU211fzmM3thgiTKHXDgEYeU0eb6gj24kbksM1eaVXvTuuTKl20yAePL3Js2KjcY-5ZjMOJ4xS3dFAUDU-CtMx6BQFFsabo5iUGH9-tEzzckPlGefsYNXpkw4vXRg-n766aY4Qw3OPZaX3MFB2u64Cw9LPajlP88qVKeFHv-X6ZjfgittR5o_OtytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29760" target="_blank">📅 20:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29759">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dohTJFUO53jtz4vDax8_dlca6rIVZ3odWw6asBvW5i3w9oI4moXcM2s7xFfeXkARrEFtOSlUCNkK8O8v0jp1LCRSZlzCPsx1jWOFqxNBTLxWLyNbMsr2NroKd9DNX-wxC0CJx4OsU8aaaBxfO4zK-mPDYCsngRNta9ejNDBwIbBZkO2VFhG_W2eufdX4eXKI9LF0kvppviAqqLJDYXiKIoxLAaFwkDd8Aj7DtU6VgsBVjUbHhEu8JEVNGsHpZPdHAvPqB8JB0ik1lV7XB5s0lasfLw6PehAg-R3c-oUhP4GqGvBPDZ6TiZwHcjZ-H5FDKSxAA-ydMLp2VR6-gh0hCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل السد قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29759" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29758">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioZB8Cs6_KwoHK5JKtExMo6bg_VpCVfO9uJRWo3-FGUXfbmUkGuVkcl0NJU0ETq6aOyq1CS7epf4bBCdvQJcwHdKWmPlSkIYbUxojURhOa0iL7Y-lPFwgdAh7dBt6ul469rdfZ0rS7qCw90VsBoJQka60oZ3YhHPwWTg3EsaMlblU5zZ60h6HlgzPiAb7u5ngA7e2gWR_5DSM2ZGMWrJcnrGt4jU_XskNexqh1vJB6gnadIG0lepn74v5jZvkwyLQgIO3GNUOhjTFrtfWcMnyfSD1raUiAPMtFmqcQ5nDVHGujG6FvFkklyXTJcxSCeSVs4VE2hiKuWN33KvSQQmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سوال خبرنگار از بلینگهام:
هنوز هم گواهینامه رانندگی نداری‌نه؟ جود بلینگهام: نه ولی به کسی نگی ها. من هنوز راننده‌شخصی میگیرم، الانم کسیو ندارم باید ببینم همیلتون بعد فرمول یک چیکارست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29758" target="_blank">📅 20:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29757">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=ImEaIsUtrdaZvir_HPNPUriDybAiNVURN1R8mdq-lAuHd_Tl0qAHbXIduyvL_XnxEBSQb09idr5l3C0wHQxXl78FMKOvR6PirvoM04UPNMo1aEbYfZlWvVpL3hjo2GLNzxMZch7F4QLz5sZtyaIhmgTVcATio1wmUr0xy87BGVQ37Df3s36TW8PrculXH3PA2MvUzYLpujEFvp6-u-TwIKwLLizdoCD-IKwlyDw6jiErdPEIUGonqXN5Dqf13THQnkTCtyp3-hciTUFo4WMjhXxppkOL-gj8CsaE9rLMkzrYWhthbStxwcW8_0q3bQlOddUQc1TzfsSYBgs4oTO86A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=ImEaIsUtrdaZvir_HPNPUriDybAiNVURN1R8mdq-lAuHd_Tl0qAHbXIduyvL_XnxEBSQb09idr5l3C0wHQxXl78FMKOvR6PirvoM04UPNMo1aEbYfZlWvVpL3hjo2GLNzxMZch7F4QLz5sZtyaIhmgTVcATio1wmUr0xy87BGVQ37Df3s36TW8PrculXH3PA2MvUzYLpujEFvp6-u-TwIKwLLizdoCD-IKwlyDw6jiErdPEIUGonqXN5Dqf13THQnkTCtyp3-hciTUFo4WMjhXxppkOL-gj8CsaE9rLMkzrYWhthbStxwcW8_0q3bQlOddUQc1TzfsSYBgs4oTO86A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ضربه‌سرمحکم‌سردار آزمون‌در دقیقه 7 مسابقه که وارد دروازه تراکتورشد اماآفساید بدرستی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29757" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29756">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90deefc883.mp4?token=Xr7AoPwXCiHKXGeik8JexCVy34g9asQACa25rInPPVlwccLZJSV_El69Va5FriiYETzanD3gg-QtoUVvvEiCFbnvleYqi0a85xGWznWtLdC036JYgI5znWWGC9hfxHhtaG-pyNtV-emLlgWMrEjNC8_ydoCEtp6TekmtO1ivxPK_ECh4JLjbT5XO6micIwEhu151B9UG6PrevEddxui3j3HREEYz1Xk_7qmCaJxcK2YBbpN_zsAqJXxZjq1Zi4OA1okFUjkXqYaPIqPKwErdxZMGFGPm_dZGkKEnmcyswquVvgui4qH4Rldw4o-uHmSWf2izfJzUBKOyozSa8HXN0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90deefc883.mp4?token=Xr7AoPwXCiHKXGeik8JexCVy34g9asQACa25rInPPVlwccLZJSV_El69Va5FriiYETzanD3gg-QtoUVvvEiCFbnvleYqi0a85xGWznWtLdC036JYgI5znWWGC9hfxHhtaG-pyNtV-emLlgWMrEjNC8_ydoCEtp6TekmtO1ivxPK_ECh4JLjbT5XO6micIwEhu151B9UG6PrevEddxui3j3HREEYz1Xk_7qmCaJxcK2YBbpN_zsAqJXxZjq1Zi4OA1okFUjkXqYaPIqPKwErdxZMGFGPm_dZGkKEnmcyswquVvgui4qH4Rldw4o-uHmSWf2izfJzUBKOyozSa8HXN0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ایشون خبرنگار باشگاه شباب‌الاهلی هستن که پیش از مسابقه امروز با سردار مصاحبه کرده و بهش گفته مطمئن هستم امشب دو گل به تراکتور میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29756" target="_blank">📅 19:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29755">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4XMXwb88B1DXfECcXE8Dj3r9T9fNZYg4dUMvTx0gEyjWNth9UGOZDW-lGg6yglJDqyGQw74lERHJYKnDG8-F8VJeGPcyL9S0mdYzVEFVZ0b6Pk1-nnIBHSlob5t60mnhfjJStn3G4yNoQ0GgNjoAxdUFhG_bNTIg7YdyRqr9j7ruhCRVsSdJzGq4aQmcxnYo6WE394Y-QuLT3G2XqFQ8EWXaNFrInw39rRfKsJa19972BCM8o3oEeFgK5RAi7NN2AGjbyVhaIAhHsXXKvoLYjCAC9hrM40zAjBqo7QAgBjYTWTm3TFl9SQisT3cW78Wj-o4gitc0KeMUJWuWYBYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29755" target="_blank">📅 19:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29754">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8E8EQaFR6JchRP0gWsLrgtUB84ogq3abyp4-nnyM1Y288KvGcWy18PSEgiVkjUckgX_sXhLiAuN3V3-kSfWI5216jSMCnfMUROFS5g-XqpK8ymQo7Ifd351zidwVO0wPutnlIxSSWvfmgOg5SPMuYT9uVK2h9dzMCekxCfZPaAgX-Ls0-HToRJ0I9DmLuCWktNjIMtwbcSCP_wbhnsKFGjL0aQDuhiRyyd1xrfHWc-JQjGO__u3m-MLew6Rax9ycVcyGUKRU2AMX_C4l50C3mt6E0Ms0OyPftHhtnRoLwwOkumVUxEExAkrUbtOEEke3ac8GQNvgLNcPImI0jsgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فلیپ کوتینیو فوق‌ستاره‌برزیلی سابق لیورپول و بارسا با عقد قراردادی دو ساله به سانتوس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29754" target="_blank">📅 19:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29753">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKbOyBkDcWh3uVypbPyH0d-N6_iZnF8Fyke6V94AV3dcMWOwW4TtER2Dosju1vSNazkbGhVfch8vRZBcdEMHihATHIZcc7G-V_tK8oDdzf7hSYyefKHi6CxYlht29kJG2jlDbAGxsi9m4hnVBY7BbXlFj0jaWeqbZBcZ9ZJ9ZIwBppLkvGcihGkF_vWY_tACugtfRMmfXvwX1rqDJ4CdpjNshhzCk5AZYSP5Fht3iu9_6F3fOrUdAk_ZCnVBYEMFqzKe_TawX1JXjyAKNChxmg0riRjzChzJNwsLVzl7j00E0TkbkM2Yl9GnhMjUPwlXSiFjVAHv7Bh7M4QjmSHjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛
مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29753" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29752">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjRILOh8ZaPbyQXqsKL_2SWr3TSrxsD3SAE2CwAzFh8mU6hsPOhbfNxNbv3JRk8V4_JedaPZ-fy34U7Gh5U6GV_A4kAPDawTcbtMSJgvafCsUc9m8WnphqnnC708o_bHdfYXeq31kZph33aRtQ5FlLtTGCs3Of0ui-jJT6Bn1T-xDZ3Iy5lkMQPVsxcOPmRpEKi7FkP_cfuaRiptPF9zgCGC0WDUCJHOASEb1lVt_4XNP9O8NCgKtL84-cwmoEisX8qLtDZNFTuIDyK6AaEIiz-DuzACUvoICQlSAlSqVI82CvAhb_cTt-jPfstZ58oYLKGA1-Vid2H3vTss2KoZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29752" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29751">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgL6x8qUV2mV0wn2ir75POmfYMm5Ckxk7wja02-kEtEshB2cwcPr2L-WfkTEjPznf16BJwEvEugzLkjWsm7PtFS-hPdsKl59tQ694s91C05xzFdd9HkiaKZzds7JyBN4YWZnhEL5GVsx7ng41KDIN2eO30BL-EwUuzyu6O8zipJm-CtGGFFBbgpA6TdR3xyYgntaXDRfWyTC0lW8omASDsrs4pF_Jk3_hCiw_hH6mgyBOKCc3QN4xIPknhQW2s9CQX9k7ooCgjddA6n6WvMNy8m2N-HDEDrDQj7fPbph6_y3XAzUXteDqbzZ4ghC2_YvyjFgC_QxcNSgR4nIdM095Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤝
دوستان خود را به پین باهیس دعوت کنید و
🤩
🤩
🤩
واریزی دوست دعوت شده پاداش بکیرید
🤩
برای دعوت دوستان خود در پین باهیس بعد از واریزی دوست دعوت شده به پشتیبانی وصل شوید و همزمان با دوست دعوت شده و برای  واریزی شخص دعوت شده پاداش  بکیرید
🤩
برای آزاد سازی فری بت دریافتی میباست یک بار فری بت را با ضریب 2 به بالا کردش دربیاورید و سود حاصل از فری بت را برداشت نمایید
💬
برای اطلاعات بیشتر با پشتیبانی زنده سایت در ارتباط باشید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g23
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29751" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29750">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU6NINKWkxbfWE9tw2ilq9c3buKMXO2qqCizXRVYFlNKwabzefPZqgO-9koPuefJ6prami0FNA3-KXCz-3sKpbStnq_9NkOCyfPYBlzInGMMtFANo3cAKmgB9-faMY5-MPDl86Jwv0nlf5lbInFisv7sWf0WSBa1QuU9nd6ZlVcUTSEF5BQwnf7TNWGJM6S5eM6zmY63jbwysGD3P-OROk_9cu6JqkZvJljQCOKO0TFHIBc6DRuqYusVHRU234oPd6IpzVbVGv1CeoaEWTJau-nsHYMdexfI3UxeseYWWKy85yPN4UtyYqt5xnix53maXeNB3NLX6oFZ7dtKOJYVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29750" target="_blank">📅 18:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29748">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXKLhFDiXFMq-Tt1dRRGq7isC1pmiRo3b9xj-PCYQB_8IsGvouCGcGmSYDcB4KHOxYqz8YGWd6j6DjGL9lKUSMm5QC7wuApEGlRIi204sjjSAZCb9h-07ehymr62FV1-Hw-ghTNwIrD1EwRauLMBeSD6AXf7reN0B37evpn5XuFYhierptrQJ_DwJwGZ04aCNRS6CyKLGHSbysUxHXS1N7lXaI98WQRmIjBZLFsl8jCA4WC_0rzDjr302E3vz_ESjzKCRLT7MKPxk_4aRJx02R_XofLXxNckxWyRSYgXY10r0mly_62E-RWQDTG0Qr9Aym9wu17jXq8IOE_84C3DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fogxMifWwfjasZ2QfWtbzZKHM3xrDUcLI-o4o1FfbsszzZJtYnBgo5WvhPkOS-IVkbM70iLQusP_385jyjhwJhQsvEPbTXZR-UIcrYQ5ntALWkaXFLBeKdt6LkvLP-x9ukXvHkwcEa4kyHSG1T36ukdmsHdV9G08UtWFLmP-2Ks_w5eNfpnQ-bcj1hhm57PUxkyqmZ7zX4jP0apW3QOvcLpGKYkdplDkMqXW9r_r-s_UMrDkrs38NbzDkJUF7OCUWi34J88X27LN9ZWC69_Bp-e3BS7_xxlxEN-2UeHsLEN2wxSZRQDaKTi2E4G-81i0Tev-VDAE4b--u387T_mCqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا
؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29748" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29747">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VILNyaUgHKTKekii9rwVCc3PPAwZvt_g7YqTYQWtKQG0rXKWeZ9WnYau2FMnK9ok42UYMju91MVfx-W22tVLTg1bEMOezmZs-mhkxQnQosun2fz3zIGyinQ3vuqBDfJ18cxocFcn0fDj6_d-DtRJDHRopRrJGHt28rAPP4ysA9hE7UB3faN3YHpISi6dFFaxkw9bFlkNqlJ-bsJ3E_m1yEnqAgv5b7-pE2N_enkliUWX3zmg44VbDWd1MjmaZt1UvxIO1a65M_zGMYXiG8Pz3SoncUnEpHO-gwcLLI4ISXscfKbho4m8d_31A9hPLfING6JCP4Z3-4Zyo1uPPwFJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از زمانیکه
؛نامزد ویکتور بونیفیس قبل از مراسم عروسی‌وقتی‌‌فهمیدبازیکن تمام اموالش را به نام مادرش‌زده سریعا تصمیم به جدایی از بازیکن گرفت. دختره این امید رو داشت که بعداز ازدواج و باطلاق از او ۵۰ درصد از دارایی او رو صاحب شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29747" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29745">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae707100.mp4?token=LM54Ey2n1LH4Jzk9vtP5cSBKRcDsx2SaHf74GcS8x3NEL-zhNGUS-Sw_lP0ZR1It_4oNClpfe5O8xSIMezmtZBHs6GxjNz5yt1crYPrXyk8jXYN50jodDNpaKAzYdjvQJ6wXuJzjWyKzsXeNxVey-rX-vhWV9efUi7Cwu4LDq69vYnZKTZmTQvtSx_Zg_pDOUiudZtQipUDXD6IYGQVeOdyPEP_plX7AKffpSyOAQP93x01ULVo6Ajgk-mQ7Q6zxPIfCw7afIUXPAyJVWmzDoOC-dfAzKhGjMg9AD254DAorN0xKPfq9LmJobh8cvjtAoivzyuHDa4fwqgAdiggVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae707100.mp4?token=LM54Ey2n1LH4Jzk9vtP5cSBKRcDsx2SaHf74GcS8x3NEL-zhNGUS-Sw_lP0ZR1It_4oNClpfe5O8xSIMezmtZBHs6GxjNz5yt1crYPrXyk8jXYN50jodDNpaKAzYdjvQJ6wXuJzjWyKzsXeNxVey-rX-vhWV9efUi7Cwu4LDq69vYnZKTZmTQvtSx_Zg_pDOUiudZtQipUDXD6IYGQVeOdyPEP_plX7AKffpSyOAQP93x01ULVo6Ajgk-mQ7Q6zxPIfCw7afIUXPAyJVWmzDoOC-dfAzKhGjMg9AD254DAorN0xKPfq9LmJobh8cvjtAoivzyuHDa4fwqgAdiggVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله‌ تند و عجیب یک‌آخوند روی آنتن زنده صدا و سیمای‌ جمهوری‌ اسلامی خطاب به لاله مرزبان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29745" target="_blank">📅 17:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29744">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P13hVfJ_yL8Fc5RmGCVC1b11cWDKq0hVx26HcsEdwttfRB4QWi6CNyWAmHW7wY5EQ_38JqTrH6MZ0fY2uDL5sLL2FJLmBE4gVIcmeLW50fU8PU8vagKmpZ3mpLZSsbrEWK4t68o737OV7TUBM_2DaYYIlkg1To2TADiQR3Dn1_DpKuY_WMxse3kQdbGbNj0wgcgEJL4omr6chzaIn6uLqsno0F-8tdRzHECUbgQO7IMkqqyJ2jBZnR-IO2D5ZTkz0ZglGGti_HXEMDC5F8pfdnZzemwF-UiDepazJn_QiLgNXXQmySR_-NcfC361MKTdSImxnYGwMHbQwlFNZn7TTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29744" target="_blank">📅 17:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29742">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VViyqkVPRyiaI0iabvygeJLSgW5lSkXtO--az2kAbgYvIVL0CeXwZkhobPKq2zS8fKflpEukBvEIstvC9YeusZ1BqdKLr34dx1ZfZRwMrMHKdJaEeJvWrWMDIUkTTjThpHxh7w9AiiCggO61gSfNS3MgI99Zuz3lMPSWOZr01EHvgp7sa8MJNHhzjJgzO8VwXB2GqjitZuzqlA4qko0TtmNA2Mvo-Vv8C9Lo_4vJ0LKEg-k2ids1m-YI6wRbQouZ9xfGjZotiQlYcu-3ASPdH3isHcP0kLyWU_ub4PDqAx2m6-EExveePrStfqq-RL1NMzTJVcnjTEssTelwLZapeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگارباشگاه فنرباغچه هستن که معتقده کارتال باید درفنرباغچه‌بمونه و باید به او فرصت داد. باشگاه اون‌فردیکه بطری زده بود تو سر کارتال شناسایی کرد و از حضور در استادیوم در فصل جاری محروم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29742" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29741">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9hw8mNRcTX0VI1qrK2VrtK3RVAqveL66_6gpO1gE9h2KkMzIDE50psDN48gKrCgoW6e0O4vxW-kGnLpstrrFiND_QUg9FxQe7Vh1wIa651UkJ92IXYifZSKIRO5GKpJ75wntVltVqgAtoUxs_WWwh8ugmukktNCcxgseGtgn2Kx2we7OkyYO6aQdJPbA8dakER6ZM4B5fprGmhSIFSydC35UgLIJC8vvJ8hOZeRKHhiVfXGSBProLScn84Hdj5hg3A4SowsJJw0xB2dRr0Mokp0bWwdvSaQSmwwXyNrV5C-VQVLgwPaUz_3ycUAoBdewB3vLw35k2vArwRpNOrRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29741" target="_blank">📅 16:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29740">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3lFlztOu67Rvivx8n2Li7og94jDR2lrYTNq5ghwk7rumPlhtdzIxJk0zU4Up74_3VwMO9WE0SNyzbyaPbnoafOPgB7U2URzVBRD3coBngWbveNcpk8PoGE0llgL8WPZOtCEGGxclYizf9hlX_PXo1Pukd6yMypbx0AR1TCEJg2cITNlaQxGufjAv3JJXikToQfRio_-IQ1tnIRtMPetc5GNZSDeiXZ0hO2jP31VDBC0D5RY1ISDXQjXLvcWIfj97QG575EQsZ515sHgxZOLlv6-Cvwux2lGnePZBuyC78hCeIeJbWboWEWQSlXgKQqXgVEfZqXQOJIyhcc82aeYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29740" target="_blank">📅 16:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29739">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBNexY7qKhhRGAT7yOH_MQCdpQKcS_D8TEmuZ0ABq1wGMUzAG1SAUEOsIM0rhEQvSR_cfesrgETVYr56rC4P1xk5GJmrb_CLaGsXjKfBYIuUK_Dh9R1nuOpNGXai1eIuYe1Pzov-nUvYCPUaDZoCCixUH4dQmFKwdLwZumSg-biO9Ea67D8vbxSDVqg7pqZoGzNvjDma2ISPk5VlxV1xF7rFD1h-oENP7dZPcvCKpt2DQN5v824wTHqklWLJ6j6Si5sRsQLPa2KsqZEb4EGA9_WeDoWU5Itpk7isSQUqLpkduU6dQLSOSXzLT50cFlfdUEPGJyC-NO_XVQ1q-qXf4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29739" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29738">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3bU7B75cZtSAVDUf94sLRkJfNfuCjkgQ2hJKDDldzn7LQ6jeU5cdHwv8xaC3N48mV5BMSEAJCK2uupMBXn4cC-bgNCPQdsfFbe_rC_yrLbAATcQywBiAx7XBL2nbt1bsRFrd_Yf-GdziyWQ1mfnfVHNO7DyFcdCz-9ucypmpOg4b_epnqyOMcxE5KLiOXjVSxMiSZiL0bjpJdAbjzs65A62yTgr5GXQ-pzONBKXHcuOAzO8W26NoDRl8HT9HkC6V7ErTJQopt8wt2AwP-ylDUL5_ivOCJ-UtU75YE4xE8JACXMXyoQwRvJwwqtD0YEidf86r58gi1qPRlL95AlMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردلامین‌یامال و رافینیادیاز باعملکرد کیلیان امباپه و وینیسوس جونیور در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29738" target="_blank">📅 15:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29737">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=QwSOcMmGdxo1V9UtPEV-n0EIk2EBhtryOYq7OIfqG0OG2Ki2CZxcFKQ0YreqSDV4OIcna1ywEs2-86FKwDrR8t61BhCXNLYx2nuU3s81LhV8llA_8H-OujJyH86zUr1VozgpWxsGQtGytmPDf2naY884b-K9xVQox0TVHq1r7EsDqTcDyOIDGVrEaqATnQbl5ttUEcMO1c4NglGVi8N78x9FSPisYF8HuN2dwH5K9CrgwvkplxQp40JF4OYgfnpXBsgoBaIQPIYfkZG_rM9dKK1nL-t_0wWhkfFPwMBrxomc9gXn3_VQgid4anTKaon-896RuZcU3pgsOn2BvyeC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=QwSOcMmGdxo1V9UtPEV-n0EIk2EBhtryOYq7OIfqG0OG2Ki2CZxcFKQ0YreqSDV4OIcna1ywEs2-86FKwDrR8t61BhCXNLYx2nuU3s81LhV8llA_8H-OujJyH86zUr1VozgpWxsGQtGytmPDf2naY884b-K9xVQox0TVHq1r7EsDqTcDyOIDGVrEaqATnQbl5ttUEcMO1c4NglGVi8N78x9FSPisYF8HuN2dwH5K9CrgwvkplxQp40JF4OYgfnpXBsgoBaIQPIYfkZG_rM9dKK1nL-t_0wWhkfFPwMBrxomc9gXn3_VQgid4anTKaon-896RuZcU3pgsOn2BvyeC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛ تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29737" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29736">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmJzihVEN7S2yEwUvGEPN8lWnF4wN6H_CT4CJ1O-g_IOl8C6VJb1NRnd4Q-r6ZT0xR9jppQgs-36eR2AH_BRSgJEdCjkrckdhHEthJzknm5SsEcfV6Q8mQ4ALWLkmcZNV1LM3DrOXw0UxmHoJNdwmbMnShRa55ZszPcum8hZE5xPwI3nJRvuOJHL0RQO26cqZ0pN8QqNOooa0ExWY_akXF0QD6JV_VX131vQ-QTgMTIcZPiixNSRzxVDcZqcgA_ecGuj-A8S63V3P91E0hlIo5wIOqHhdzcgfXXc6vyaAUjSn01zWgEGN5dAbW1w8dBfm2gDjYWr7U-OfacbF3TmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان نیم فصل و قهرمانان فصل لیگ برتر خلیج‌فارس در 10 دوره گذشته این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29736" target="_blank">📅 14:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29735">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otltkhE3CcV54ftiHcrSm3U3xpYsRL2xlLUROECUhHz2RHjxpKFQcoLX1K2KwPh4w862tkgzmnLCkaEXvuDNQRnQ8gRw3iScD3PRjt6ZwEBJ03FEM2zVlbprY75v05YRPsjR-k9FF2nQPmHJgx-pOlbGrLSOcxsdp_AZcUUno7mY-wf6iXM-10jMQ_R2dO52ejlD6slZfCLsMgfb1teAmDsSTI0HI_9pSRz9GYEDoB4YLMaSx95g6gkxYtpg2lZb44idWujYxE_wgW7He5kXNiuaXutmBQuS_M292BvR1q8jwLdLUu39rJbcPavXjaNG5UpTpC-6bfSO0Tskh-lXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29735" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29734">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=FkdbEPPsl9IRqMDot8lxb4-uvg8S5mkA7LuVyPZ-8tC_E6G-PmaqflBfHDnAanbjDRT4IEcHj07ySG50e1XKJZjdW6LiswGLXXi25vApsjrNJ4qcJkaxZ4s0liZ2Q1P61M4L5Mr0LqRdwbki12TtdUgaOWxT4u4MCapTP0aunAEgeJSNXbOb1V9v7V3aYlzhohutau9JrHPu5wg3j8w7zXM8XGI45RZQHyxDmaf0q7kHMwLV-m_xxYPthBrTSJX_Y-zTB3fVHz_nx5O8I403qGIS_pxDlWxOpmtXJKL_heBjgVF1zxBixvKJlm14pLqEDBJycrHRy7gKkDaARvbZWnxBySV4LgZwxYfG76KRnShZ65hLNr5zk2eceFCS0B2UK6Lte879QMzz_U9DVKy3v2R7E4UTntAy468q521snoYlHxPiKEgfX1-kuqjwIbM3Waufd-B7S0nSFNh_KmtYcM74tt6yX2H6lrMfi05EYmAamcLsKSghVqg7ScsVrc_CET_9Snuol1tIWtCbr38361CMswg6kq-WLvIv28ktD04H9UsTRbCn3rbotJWN-AXgS5MMYAK-z5q2WFnm9e8YnPPmexd49VXBi4RV55UuLLphEaFjluS8Cig978CYtGbFdvhzW-p8PJI77rKZlc8ieKRGkpEflps2y9gUTsmd-TE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=FkdbEPPsl9IRqMDot8lxb4-uvg8S5mkA7LuVyPZ-8tC_E6G-PmaqflBfHDnAanbjDRT4IEcHj07ySG50e1XKJZjdW6LiswGLXXi25vApsjrNJ4qcJkaxZ4s0liZ2Q1P61M4L5Mr0LqRdwbki12TtdUgaOWxT4u4MCapTP0aunAEgeJSNXbOb1V9v7V3aYlzhohutau9JrHPu5wg3j8w7zXM8XGI45RZQHyxDmaf0q7kHMwLV-m_xxYPthBrTSJX_Y-zTB3fVHz_nx5O8I403qGIS_pxDlWxOpmtXJKL_heBjgVF1zxBixvKJlm14pLqEDBJycrHRy7gKkDaARvbZWnxBySV4LgZwxYfG76KRnShZ65hLNr5zk2eceFCS0B2UK6Lte879QMzz_U9DVKy3v2R7E4UTntAy468q521snoYlHxPiKEgfX1-kuqjwIbM3Waufd-B7S0nSFNh_KmtYcM74tt6yX2H6lrMfi05EYmAamcLsKSghVqg7ScsVrc_CET_9Snuol1tIWtCbr38361CMswg6kq-WLvIv28ktD04H9UsTRbCn3rbotJWN-AXgS5MMYAK-z5q2WFnm9e8YnPPmexd49VXBi4RV55UuLLphEaFjluS8Cig978CYtGbFdvhzW-p8PJI77rKZlc8ieKRGkpEflps2y9gUTsmd-TE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایوان تونی مهاجم انگلیسی الاهلی عربستان:
من‌ عاشق این هستم که موقع پنالتی زدن دروازه‌بان حریف رو تحقیر کنم برای همینه اکثرا چیپ میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29734" target="_blank">📅 13:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29733">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnNMoReRyhkBb6LSAsubPge7GFPNylJLDrmHLHKyFtBoOh4AOKmpfk1ixoS4AQ_CzjLp9pxrUIjPoImsZish_OqG9y06ulGmO3aURMzZUq754h5Dt11v6y4NMnki1WtaXfvYHNUBQo_in6jvQ6RHQSWolV2ipTUCAflfZsfV64DtnKaonzcwSFSd_JECBG4SYaU8asrr0QEQvGqS0aV-Dmux15ioAo5F0jK-fpsUYWDK6ypTADhKX-Y41ZwWupZ-aSRhOR5g_A64J_g48sA6jjITHwUFvYqxaWtO_I1TYdjslLETsKPjhs-bTXc9XWXzuMuhIGM23mLdWkaiWqiCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خوزه مورینیو خطاب به‌خبرنگاران در نشست خبری پیش‌از دیدار فرداشب با الچه: در فاصله 3 روز من باید 6  بار بیام جلوی شما بشینم، خدایی خودتون خسته‌نشدین؟ اصلا سوالی مونده ازم بپرسین؟ واقعا خسته‌کننده‌ست. بلند شیم همگی بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29733" target="_blank">📅 13:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29732">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX_iNzAIjaBW-80YweZ9Oyz7k91B1eo6i-KVagrxNOHu9cz8i88vCoYuydNg1gq0UHYiesrLMm_BDsCPA3pF7tTiYFqJkFON7faP6MYzbsQ6-5xaytOuNjukD0ChyNMICnFBLLPQJ8W1pekgyER6XLvUPxSzvSBip54Fg0kcMc2obnF5QTrR6L6nHyab51XSTc8hq3Lzbka7Z8UvoLEfjbyqWhZZEn0EuaW1kBcKS1ihu8UFlKD7q_LjU2dZL0gVgv7Y-JQQ0zZNIp4TI8-lJNBUrPkv4IXWyRU_M7KDkXjbyzFNEB4ylrKQ5LCO_XdM_GLmEj4b6s2NRklHra4KjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیره‌کننده رافینیا و لامین یامال زیر نظر هانسی فلیک دربارسا؛ یادتون باشه قبل اومدن فلیک سران‌بارساداشتن‌رافینیا رو میفروختن‌که فلیک اومد و با رفتن رافینیا مخالفت‌کرد و گفت احیاش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29732" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29731">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=Cr7ibn5TpGQ7766cz82IAv3juU5a_7NCh7y7kH5YJ-oQ-aHS0ooo4O36vWRNZh9buekYJoTRTXLbMUb7nNwoAJDKWBNuHcGpH4rwhUqqgis-qvDheY-GSnrJ8Y4cBB-MD0KQYOFmEsvqpVZ6ONJpsrIdghgfHpwmddbwl1MLJGXK267zrzcyBfKbThy1MwjLlz96WzrinvLBvjrRkcobhPhGmIhI_xXytuZmNXGRmMLIABKG4qNYUMWl3p6bEWj3dRDj-PqgF1dtsEz9FTealBUuGG5_qRupL9hy8qUGtIDRK_H1SRnRCwgrBKJPdfKtjNU8x5Yl7kyjVEsyS9nl7IUZPSlPx-z6y-1Yy5k8KRA-o4nCMKIViqYN0shsRi0abix9EgZ73bLooZJAI16Awg5PuRkTbVuB7S5zt6vBRJuBYwqu6iuPXzigZQc3PnGS0j6gFVrdCZMje-SIYetktU4jKa3Ic3dPIGxcO5yRthSsRueBtT6MmtDTC53zkzCGB_2s1ee3Lti721pRLC-lpAqPbct0rVs2H3_vx5e0sKqTtY4PTmbrDiN10O7_HmGS3K4dgu5KIFM4xB_CfyeSi5hI1owi2tA8G8MI950xqFrbIlA1yRyzY5-W-3g6g85mPIX5Z1s84IT-JN6LCk-JShJ9q_tSaeKD951lkJOuW34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=Cr7ibn5TpGQ7766cz82IAv3juU5a_7NCh7y7kH5YJ-oQ-aHS0ooo4O36vWRNZh9buekYJoTRTXLbMUb7nNwoAJDKWBNuHcGpH4rwhUqqgis-qvDheY-GSnrJ8Y4cBB-MD0KQYOFmEsvqpVZ6ONJpsrIdghgfHpwmddbwl1MLJGXK267zrzcyBfKbThy1MwjLlz96WzrinvLBvjrRkcobhPhGmIhI_xXytuZmNXGRmMLIABKG4qNYUMWl3p6bEWj3dRDj-PqgF1dtsEz9FTealBUuGG5_qRupL9hy8qUGtIDRK_H1SRnRCwgrBKJPdfKtjNU8x5Yl7kyjVEsyS9nl7IUZPSlPx-z6y-1Yy5k8KRA-o4nCMKIViqYN0shsRi0abix9EgZ73bLooZJAI16Awg5PuRkTbVuB7S5zt6vBRJuBYwqu6iuPXzigZQc3PnGS0j6gFVrdCZMje-SIYetktU4jKa3Ic3dPIGxcO5yRthSsRueBtT6MmtDTC53zkzCGB_2s1ee3Lti721pRLC-lpAqPbct0rVs2H3_vx5e0sKqTtY4PTmbrDiN10O7_HmGS3K4dgu5KIFM4xB_CfyeSi5hI1owi2tA8G8MI950xqFrbIlA1yRyzY5-W-3g6g85mPIX5Z1s84IT-JN6LCk-JShJ9q_tSaeKD951lkJOuW34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ بااعلام‌مدیرعامل‌فجرسپاسی؛ علیرضا بیرانوند دروازه‌‌بان‌تراکتور درنیم‌فصل‌با عقد قراردادی تاپایان‌خدمت‌سربازی به این‌تیم خواهد پیوست. بدین ترتیب بیرو تا نیم‌فصل بدون تیم خواهندماند و راهی لیگ آزادگان نخواهدشد. بااین‌شرایط باید ببینیم بیرو درجام ملت…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29731" target="_blank">📅 12:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29730">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGrL-psAkzMZ2wlWRXtqIpYLXC_irby0vg3TRsutku5d_j615dZ8OupFbzenTwFFHK0Ep45WG9Oyh2nOvODUJw8lrQ3FTH5_xgDOfal1nX5JetwKSQax_ZRoV0v7-3445V-DLajvdvXIJp5WNgu_bCpgDhxYiqR1k9yI-05ASSj48GLhadRqKqJAikRwgX_H3qgj8fu79icxZ-1aWtDVUCbLO0Jj_jkBcR1WBpmAjKymklWPyovycRuCXM533P-kDHQwWP1haWlPS9FsuL1ff5ZHbc0vfZ3-3J4qx6Hcv-Snss72euLBJ6GACUjUzd4iBZwV9cVOCLtyiSV5wJ1iEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده یاسر آسانی ستاره آلبانیایی استقلال در لیگ‌قهرمانان آسیا: 10 مسابقه، 9 گل زده، 1 پاس گل، کسب میانگین نمره 9.1 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29730" target="_blank">📅 12:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29729">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=udhGZ78VROAsvAoRMaDqlHhB8Trezhqnf4gEtdOX9z_srSVs_GMTm0HWwI3sp8vmO99LjbntVBlirYXtOKrrbOWMMWydYrd_SVI8Yktj9YTAg-GtDItL04cX6n9rGbLlLIjrj1C_9KAe1srRk62ImXpJlISrCxZL6vXZWIqqud87_TppdOlXVc7WlimAqdNy6x-qUV6vRoNdqB3C9HmCawNuKRb4Aqu7cS2xyxnhzeQQmKYCnWTz18pdu7BzPRhk4G9AZQ_P4oVxNxJyFrbDNFQ-OWU0IwFhCMyTahEmIRidJGtgSAKh_q8n51ZyKDPvd_mzt42Y1n2xZHcXq7Khow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=udhGZ78VROAsvAoRMaDqlHhB8Trezhqnf4gEtdOX9z_srSVs_GMTm0HWwI3sp8vmO99LjbntVBlirYXtOKrrbOWMMWydYrd_SVI8Yktj9YTAg-GtDItL04cX6n9rGbLlLIjrj1C_9KAe1srRk62ImXpJlISrCxZL6vXZWIqqud87_TppdOlXVc7WlimAqdNy6x-qUV6vRoNdqB3C9HmCawNuKRb4Aqu7cS2xyxnhzeQQmKYCnWTz18pdu7BzPRhk4G9AZQ_P4oVxNxJyFrbDNFQ-OWU0IwFhCMyTahEmIRidJGtgSAKh_q8n51ZyKDPvd_mzt42Y1n2xZHcXq7Khow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛
تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29729" target="_blank">📅 12:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29728">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHldIq181s0eEdl21k4byuqFkX4yFeITjpbtcqMayjLqlX5TUzCNi6PHfScIFZ6V87cSMWtYZAT5g-4ng3hAp2PbH5QR7iHMiB7Qx6SnlKpGYmf2ebCTupUCdT2kRmWrazKZXo6xrtT36Aevc7H2Nxct_b0r8sM35AHN1Cy-HJpgc8r5gOba9SogXDO_NdmJ98OZJt77EJXv9-nfIF5ZmeJZ52jeOl2sOkKhnjTvUVPFNHcrXn_Ve9sYCjzYnKeJFgoI_GCvao7hpw8q8h9hhdN34GOPdfs67IqzbKHZpv6OLRi5Cb9OH2-T8Wdtg6UqtlvXpAuo-i3NHVzPNcrXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29728" target="_blank">📅 11:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29727">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_Ujz4oA7UklMuoZKfysvj2YVz2DY_6nB5FLeMmTIZ-Ku-5r4fZmsnfwACBrfjpPMrnSFt2D9Mouao6Af2uMKOlNzwDAu061dJN9xT8JsnDruQWuVrhPLWmWmpVyw6tK4NfKSn2fZbMbasoJQJyGuH3KBSOEbeI2r_5czme2y2wHVBDdUioLw8OHkeFQ0NcWNmGUgm5qzYD60tKQ8JUjRxuTbtDujaql3JDP4OGBuRcdu8GCGXxvi9B6brLls7lq-f4h5v0Z3zgx7517rVlDG172f8-u3nAjWhDzmCEvFtMRoDZWtOUzVxfQ02Jw5AIcr9xDp8GV311YgucdooXJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29727" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29726">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=p-N9M9jr0t4-i6dWAsHq9rYOlQ-qb5N9ywKLUPNxy0zvh187UjzXRQhCs-BjJIe1DnsjvQozYat8cTIc40diCrcRaxBaAlyjtLro8CFzx81UaEw_6fU7pbqZ1uSh3DQxV_Aco9hvK8KR5JTq06cVGwQGHiWKiLsePh143Smgw2ju9TaFPwOuKZOgN6Rxlru3pozqOJ1OneI70T7pAx62yNLNxOu5CSQkHHLkJa3TKXddikjyKva4PwfCgszSgj2mYIQ7URH_JRnkqD_wY2AseZAk79JSElfE2JSaB9CZkrZyQ2Zd_T6SqOTP4zQXBXScfsHF56ksKrF4HTiAXkgkqL5W2CZy2vIiau-nf87myPdGVhmherm2yBYqTVUH_fEwNmfKtm94a5ABxtukHgPYGH1HQ7BK-_ZjdOsDcaNlUG4nmmu_SeIPDhdsFxEuGcalfoGogI0nYhBoWqiB8d_E6sWxh0DCFrYV3OiIslFUXJfxv1C33fg7hVAylBiq1uYb3CMQmvhQmuaYyCrnosOkODrVeE-DD2oVYULiW_HRi7RHVWp_MMRzYIxROebUDnIAb7BsNZN_DWcGdYNSh6KKpqnKpAc1PH-cdzEmAx942kVqit-cTVT5vmJBYoArUZj5KKFFQ5aP--T8Ivej_Wxbiqt8XRscU0lHhfiSUHT_x4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=p-N9M9jr0t4-i6dWAsHq9rYOlQ-qb5N9ywKLUPNxy0zvh187UjzXRQhCs-BjJIe1DnsjvQozYat8cTIc40diCrcRaxBaAlyjtLro8CFzx81UaEw_6fU7pbqZ1uSh3DQxV_Aco9hvK8KR5JTq06cVGwQGHiWKiLsePh143Smgw2ju9TaFPwOuKZOgN6Rxlru3pozqOJ1OneI70T7pAx62yNLNxOu5CSQkHHLkJa3TKXddikjyKva4PwfCgszSgj2mYIQ7URH_JRnkqD_wY2AseZAk79JSElfE2JSaB9CZkrZyQ2Zd_T6SqOTP4zQXBXScfsHF56ksKrF4HTiAXkgkqL5W2CZy2vIiau-nf87myPdGVhmherm2yBYqTVUH_fEwNmfKtm94a5ABxtukHgPYGH1HQ7BK-_ZjdOsDcaNlUG4nmmu_SeIPDhdsFxEuGcalfoGogI0nYhBoWqiB8d_E6sWxh0DCFrYV3OiIslFUXJfxv1C33fg7hVAylBiq1uYb3CMQmvhQmuaYyCrnosOkODrVeE-DD2oVYULiW_HRi7RHVWp_MMRzYIxROebUDnIAb7BsNZN_DWcGdYNSh6KKpqnKpAc1PH-cdzEmAx942kVqit-cTVT5vmJBYoArUZj5KKFFQ5aP--T8Ivej_Wxbiqt8XRscU0lHhfiSUHT_x4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29726" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29724">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6rAWJSgwoWxepdO8n-6o9hpayEyywe0YOSaRBqfgAlsmD5paZV7RDmbv4dJj-lsZmgWoyfHCM-jZgyfh8EHSwYHiQMETsEU7kj_RTtLUd0-KhcvcLVCoEhZwvCxoUoCMqNtVyospPPC2c9c9xo0iTTLg9is1fIEfR9FV7W0h8DnLnJhRPl-4u_FbSj_sJkj5vlSs7_FKLYMD7VOrHqwRttYpOIKvEJxGulv0Vv3hH8544qn4ai7o0jA_ktV4BxfpvCr5vbgUNPyEbewtQjIFPmR54nudVCPeu2b-rRVX6MtOfXb3kq4P9t5vBT07DgRnH_ZCjTmUg4Ll66fKwb_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29724" target="_blank">📅 11:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=YElCin7oMLAf8cRVRYSjCLss7Zv_dVQO9fCZGUxdQkkjBQ8s2i3MnnEpNQQnoBL7LO01pz0ev1RciuoXLlNDJk7A6LIBmXN_wVDJDNnWzx9PLGLPY8Mkk1txT8kCvT_I75lxp0PoCDSclcb_nsCQWNt4M4MmZFXlzahWRKs53OlM1OxyD29x4TeR_7OSNp4uo41qQjS5vWWlP80UVURh2nWI5o2IAcqYjKdt0byib6mlqdA_Gl-DZ4DjiaqdVlrQyKc3pYHFzR6yYdIPIzYxRCybv5Tq3BgnoicJKqqaJQ4qbSgIdSbhrG30S61GAX3bBJgawpexgP0ZD0ne4KB7AzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=YElCin7oMLAf8cRVRYSjCLss7Zv_dVQO9fCZGUxdQkkjBQ8s2i3MnnEpNQQnoBL7LO01pz0ev1RciuoXLlNDJk7A6LIBmXN_wVDJDNnWzx9PLGLPY8Mkk1txT8kCvT_I75lxp0PoCDSclcb_nsCQWNt4M4MmZFXlzahWRKs53OlM1OxyD29x4TeR_7OSNp4uo41qQjS5vWWlP80UVURh2nWI5o2IAcqYjKdt0byib6mlqdA_Gl-DZ4DjiaqdVlrQyKc3pYHFzR6yYdIPIzYxRCybv5Tq3BgnoicJKqqaJQ4qbSgIdSbhrG30S61GAX3bBJgawpexgP0ZD0ne4KB7AzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کل‌کل‌های وحید هاشمیان سرمربی سابق تیم پرسپولیس با پیمان حدادی مدیر عاملی این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29723" target="_blank">📅 10:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWAb4HfbUgpeBT3zTGYWQ1WQ7O0t631wGfsZZMvQHIO2Uviq3wSrRww_kEO0hevhHdvJxntX8rJvNdMyowWacMcop3KtsntvCpuzLUsdkIkWwN7jx9dSUu2GyTiqAkZt9MXAeOBVCP1uv0lQpflrpC_le5W-y3MQVXmOKYjddiMc3_69aKz9Jz0YOHf_7PyZ7v9Lr2Q4Hq7-x_2UGlXuJIHvfvNAv0l0ARyTaXbDL9GbJs0z9h_KgtwXrdxrJOlhsYkGxXquIlNcGbf7DMv2222YjmOEEMxk4wi0vwwDGsvHhmVhLknt78c2f0fbuFwuq0oLKIk7LaQ7U0QiRcV3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند دفترچه خدمت سربازی را ارسال کرد. دروازه بان تراکتور از اول آبان‌ماه ۱۴۰۵ دوران خدمت سربازی خود را به‌صورت رسمی آغاز خواهد کرد و به مدت ۱۸ ماه در یکی از تیم‌های نظامی خدمت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29722" target="_blank">📅 10:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29721">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyWye1_h88yAVZD0JEsXzTkw6Pi6K2hBz5s7zy0H4I9yexHsi-36RO046yNqG5jAgHYW9YCY_P-EdraRJJEeolOv3pazxE642e6mTbUuHIm2pENhuuBP_76RERcJitkuKImT2M-O16dGU6gwfzLlHCp4fvVve-k39JW6gdtlPPV25T9ihGCoLI1smMT3YZVDIfV-xkhgT8MWF0_x7Td9uAzEKl5TChIJAju1n9S3rOxj5KnG2ohXHtJLBT632IFbQDcS4qlrJCoHrekfwN3yoK8fHhQ1zC3bXc8kYaO4ibtXbqnQMxYGsohw-4VyJwywMAFwkcUhacA0oGsULj22CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کمک‌ داور رقابت‌های این‌ فصل‌ سری‌آ هستن که در بازی اخیر فروزینونه
🆚
فیورنتینا حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29721" target="_blank">📅 10:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29720">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kdbj01iTejlU3qGhpbf6JZGM0RnhBXVS8xr-zpNZSD0hE6R-2GC8uR62iBN-D2iNNNWAq0XxmI7RQ24GMVCo9ksxDsojoyNtIaFhbX_Z5lx9jkWkFY7z_sgUBqF_mXGgWK1Hsc_RVMvpKgt1xC95lHfK1CTDAbKLClYP1rhEEo2NPG-44kQmT5Na2-QQwVdLzz6p3bfhdl5zd_wYH1YyDuRL2naUYkm_dpJgJds_qgHGvt5ZsFPg6XHq7ENLM1-EETsMaBT9ifk6vBEQghBMqT231VTZxcVOy7Fru66QsQ0hOH537znBhtpIU8uQLUN2qTBDEHuJb0a0QvZfUAQkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29720" target="_blank">📅 10:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29719">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiLgEDx5xecMnr1M79b3t6bTcH3CwuhjWgd5dOAuEXiLeaeDPKjGVPX0UbTdTW716fDif1U3lI8QJAgG9X0RQbDVfKSW0xDCbMAxL0RfhJME7BWO4C4Pp_cF2RTtdeUqJI6Vx7WE-Y3N4FjbxpVM8AMbN6QaJ1xqZWgxJwgHGTdr7fsWrd8_xnc6eMolkJ3tQmW6XrbDk8uCv-oDmOmJpVccUbFW4ydTdNfNmWCFrBfgvVTiW4T2IZybHzv8q56usiSh16EVvvwRPQuk_xhVQA4fIHHlJ3XqLkFQs_TzOeOo0RsIsTL8-sWOoQ-ost8JaOzVJNSsHm-hhpavA_lM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌لالیگا درپایان‌دیدارهای‌هفته‌پنجم؛ عملکرد خیره کننده بارسلونا هانسی فلیک درفصل جدید: پنج مسابقه، پنج پیروزی، 27 گل زده. 5 گل خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29719" target="_blank">📅 09:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29718">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYzYnl5FIeLDgZ1AcKdIe7j5LpnrTBiJ14Gk5WhcCKlGlfA56nyXBmaFOb7TYkBgrWMpjp4M0zMAQbEzJWMkgVevr_yqGyaFeRmSVqTRS101kDLM-CMVs4J1x-9gSCTgFGW7GmP2kDM7KDTIF77j38JMcir3xWHrYA0U8fmtAI1lIxK7D68w3q8LHKCIGTx_JuxaFrTlIbI2tVhsrvdISdx8FoQ8WPzQcAiKFaq7IqTiqlUPZWtzrCRinzS63tZC_01VpbUWMihma56Fio1C3WRqt2EH5Jvr6ZmDSs496Xl1wxAIAYagqKo4bINZRbmyIxpfBWItRmhVLeqGTeCkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
۱۰ سال‌از شبی که قلب پرسپولیس ایستاد، گذشت؛ واکنش امید عالیشاه به سال‌روز فوت هادی نوروزی کاپیتان‌ابدی‌ سرخ‌ها: از آن روز تاکنون هربار دقیقه ۲۴ نامت از سکوها بلند می‌شود، انگار دوباره برمی‌گردی به زمین، به قلب‌ها، به جان هوادار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/29718" target="_blank">📅 01:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX3vwUPQF1FDulTph6iljnxw1kcmPqQWfE-41z4XO1BYTbCvPd3zjxAbgh5aVFccONBC-NjhxmSA-AIoXaCsbgrs3ts2QV6aqD6hLnawqbWlq8bFL8tpC3JIB_983WAX23-V8B7HiUQPclGdAyJBi8TXRRoL1zVT4OUkkbCA1vcT_5BX7fBM-pPU7l0AbqIk0BEJeay0T25q0sFFoXo6fXGsHtsXCTTEgMFL-Rt4zgu_SsuCKlVnxPtzHy5Rje7az6EYYK33vJel0xHZFNXjA1PjSoskNECXf3TWGoX5UJihoqiIXufvJyJaITFRzlvQC-xy_3dky2Q-Qm6_ZZpn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ا ازآغاز فصل جدید رقابت های لیگ‌نخبگان‌آسیا با جدال مجدد یاران آزمون برابر تراکتور تا تقابل استقلال
🆚
السد قطر در عراق!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29716" target="_blank">📅 01:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNfmNp2fGTBX8XvUDnbt2RNPrtFwkurKcMKn6pzHp6YHa0XVaq2xtgmzUQkTFT-cDBJ2sJJ2a2n0V3pzkfS5sXLw34r325DSGY31qw9JodXblCFxCx4AAvXDIWKX0ghBPvfjsjljNtK4TVuQNBfd_DPPiiBSH1KJxWYt3F-Jvqhnj6LcGbC1oy3ZJ5gFefbJsb_BtjyF3i_414zYkie6F35i-uCFjIlXn4ReL9kKPTBA9HyXGQVWXiHs2fnF-2MrpkRtw-o8k9et1_GVM0K8pgxzW3DoL8FOUvDyOPvPqeU8xw19j3xJ-vNjG7_rCFvb-5I7sC5OACgyM-q9rfQe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌سخت و پر حرف و حدیث سیتیزن‌ها در دربی شهر منچستر تا پیروزی بارسلونا در ادامه درخشش‌ های یامال و رافینیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29715" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQVrS1IMkMKRXIOiEpQ4RkdrUAvqty8QphUUXG5RXLEZhXbVbxUB_oBjDSOc5oufUG-rugiRqUaozfasdfRqcSiiF9mV3g_nNZ1GDB-xr4aEa2WQYPRFAFMj6Z_w7TpRhsRxuN9FlYY0Uelj4DaIzuGFzdu6Kdvcp6Mshr7OvrYP93d5vgukn2crSxn1CiPE0G3KPf9xRirBerCOT3aKLidzp3dovBnfhn86XmgRklirgk9OctVAYHSOukFp30ebMIOTEb5Zfc8VVR0ibikH6lH58lK3cKY749VEkDBVAdeNUA1i8jdudE4JcORQIXR5DTxyjWIIdG1bq49iK0xmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل تقابل‌های استقلال
🆚
السد در رقابت های آسیایی به‌مناسبت‌بازی‌فرداشب دو تیم در ACL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29714" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8k3ZU202ogqsEmczuooXL8OhmiKc37ZRlgTAz9GcN1yIRxu9j_wT48Cf8T8xTk2otwythtZI8kIZoCxhnsju7eNTAjquckNypvAPNPOWawQ3D5N1XxuYty80un4uCg-zkEdTmGBxzbRkghLNv1ZbqSkin21wb8pg0HYfQAsWtVP9SGqQqswtfbgkS7sRuXpC9gG6EXJGt5RCcq5IZZ463XYhwyk-Hw7Uv7JHbEpIqmxWe79fXFf3I4TwRCdcLPxbjHu9RFOUloXa9UsgBYwO7bAenii_enfg7KKTQzDE6J4_Apauxe-zxghE6hEjlWwscl5r-Y8lBImANp76mTsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام مدیرسامانه هوشمند سوخت؛ خودروهای صفر "نو" بالای یه‌میلیاردتومان فقط میتونن از بنزین 10 هزارتومانی‌استفاده‌کنند و سهمیه بنزین 1500 و 3000 تومانی براشون حذف شده. حالا سوال اینجا ماشین صفر زیر یک تومن چی مونده اصلا؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29713" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFFuw7wo3KHf-e0mlgFNpS15joWEi-5bCrwBijz3Wtw4ZIXgPUsXMZE11bPDOefvtPUs_OoKOk10vLcPSn13YTKFSj-OuerzxF2RcASwftXnfGY-2NcM_3yN5tJxZw_qYtfmh2GhH32OJa3g_t0WN2n-DiPqgY3Au_u0igPblR1PykAxWsaJSX5hXalUaxXgQtIGtIcbsW1zyieOkUrGEeSFwXRKgLTNxiDyVO9QRrzeEJL5YxcLhQE0h2h4wRmpw0lpuynbq61MaqjnrO9QdKNzIKgyAtNPRdY2nwn-G8berb2_DsC7A51BVi8BQ1ZzcyQXRySTUoUgPaZzeJuGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29710" target="_blank">📅 00:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCbwiiBeA50JZJ79wNwDGprx95xrLm80slm80HVrpjhs3FvTDx7dBirATL4qtKd0BIsSRhKL00rH3RChmYrDbn3cA6jiv-I24jdlwisiliUSb8M0z1xrypNWEEy7SVnW9i2-qgHvXhLR7o3yNtj_hxHKsTuAzVyTK6NCwO5Ge4LodnhfmMAePpg2Xh71rhd-m65lc5lHkM93NvWzbktBfiz37tSy1Pzesv2dUC3D3N67kYSUull3ztT8hq4qhCmfl9l9fPt4F5cPf2xGuyZdimYCcDrBQgyzkwDAEFtm1TGMvnKdzz3O0TrSOtwKzuCC2J-NvUWrh5pL0ZdYjJsCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29709" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJi8HnslNUN_g9DI7cEhM1z6ecwvvhbtMDCplvNYEW03X4YDRP0_fnH4dZ4rsaT4iWroq7S1hqVxha8Bk3fR_U8qdXQPobBxZXWB94AWmQFU_8h0Lj0Iuaaj9XV4eTr01VxSMYOUnkwk8AH11E4tlUzWuvJ22IGXTZ8HagttMW8kGL0vKKd1pnBq1K2F4S6QmQY6TFY5jS-j5hlSuZYqxtTSJxK-RWSg0VGtFW9guhJzNpGEWb0fhBmV8m1pb014MjvT96WXqKy5xKfG_AguzkENI6zKRAYfH14XhRRUQtXDp06d9hrTpFuO3tQkmJIGEIU12Gn9OtrFk7X_vw31LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29708" target="_blank">📅 00:07 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
