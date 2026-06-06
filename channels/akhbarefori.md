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
<img src="https://cdn4.telesco.pe/file/pAOfAhPescjWXlVXVusE6LBGN2pif_OUhruW9FKiLYXjNTaVKpID9h37MRICjH2KPklEiNUpKMgFc38Zf9A9X8i48RNToYqCxQECocyMNtsDUWI0s_nhu_4_YTwZWnULe0AXi3AR_aJDc8Q6ts-5LZrpFjRVLBPa7eDZd1uqMzcbBTNaBFKsgIx7A2JeajF8Nxzl5qTKp_Hw2CzoTYW4d9_OPyC1oa62umhGx5ksOtTBVW2U4BbY9IK8y9OCL1eMpnYTwOQeAvQSJdZ8z-syYn5lcw1BKWEeOUxpSXMwK0yQ_ayxYp1zIghsNv0BkuRsQtw1TUJ3hsu7SWLYz7aAcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 17:54:52</div>
<hr>

<div class="tg-post" id="msg-656631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXU8gFbluDQwNJUbri3lkLI6bVS9V3Xbb2afvLH80P0YgIJsWjAnTLkNydS6f_bHnfbNVK8biJ_2hozZpiYh5gKLL6CpN2ZlskY-5b8cPlct2XCDi7X-LE0oyvgiYYBRoMLr9Zi_DNsvzaJh3-ABtCTnbeKYx-Cue5dz0WsKjU5D9GtPkR-wDCwbmI_gvyvfgmdjSSuwpn6F_p_R6q8Svv0eo1pJee3sf7Rve-pLxfhZCU6KOR0xcvCZXBvb-GPF7lx9MSfxGUUEwWe8oggj8CqKzXj0_ETA033PMRVKkZXU-wAKVo8ZwZS2GQbGkWgTwM-1VsJm-47ipeobDDbSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی: حمله ایران پایگاه آمریکایی «علی السالم» در کویت را هدف قرار داد   رسانه‌های اسرائیلی:
🔹
در این حمله یک ساختمان محل نگهداری هواپیما و تعدادی از پهپادهای مستقر در این پایگاه هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/akhbarefori/656631" target="_blank">📅 17:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d271feecd.mp4?token=OlaslAuzU1g5Fa0iK5watudaWDoXM77QIA4T7-6zBJAE7sesvyGlV4Xb5UR9Amt2_4h6OIlAPawHuGifbH5twCRIYDrpgzpiDGZgdNHgu-fT4X34QUe5vC-oaPveFpKOt3SA38RyDQeFChjMe7Td-UHxY1pYj2t-VQ0RK3MWnq-FtiAEIB8aTZlH5RxfYJorQd68Zj7JULCNlW8ErreoSWNYFnCBZdsjXwAPVQpqN-hkeHZYHn4E-VH_LhuoH6oJE4I1MsoHKIpMaJYdjrSaFht04b5ff5PBDjIAQgAOetwdZvPIbdnViHzIv7nYfOcOmcHagJWhlfqokzdDO-QORKJlZoDMgXZX0k_IDBRNjCc82jBCJ0qmTUov4uEym7_4EinsLG4sedYHs8boszMxlivR-jH8-6hAzB256VaUoVvq-0IZ0Ji5V5P-Z1PY2sYXhprsxQ1rMkxeDOinhnIKvAvzn-Ut_1cXYszaOh6Noa1LZfzPuUyWKL7UmBlqZn_o8bMbFVLgNB-OGT13zNZOypNjiSq7p99NRrjQzvIcKrzQgndxiBqOwGirFz1hC1iIoGVKYwmWIOBP6iFKdmjQxdlN1zniAsYXEBE-uezIFU9T-VTzA1sG3MGQYTGQj5Q36CumhauDYB7c_Dk6TRuD5yEEKMNb60DUUUW71rhqsqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d271feecd.mp4?token=OlaslAuzU1g5Fa0iK5watudaWDoXM77QIA4T7-6zBJAE7sesvyGlV4Xb5UR9Amt2_4h6OIlAPawHuGifbH5twCRIYDrpgzpiDGZgdNHgu-fT4X34QUe5vC-oaPveFpKOt3SA38RyDQeFChjMe7Td-UHxY1pYj2t-VQ0RK3MWnq-FtiAEIB8aTZlH5RxfYJorQd68Zj7JULCNlW8ErreoSWNYFnCBZdsjXwAPVQpqN-hkeHZYHn4E-VH_LhuoH6oJE4I1MsoHKIpMaJYdjrSaFht04b5ff5PBDjIAQgAOetwdZvPIbdnViHzIv7nYfOcOmcHagJWhlfqokzdDO-QORKJlZoDMgXZX0k_IDBRNjCc82jBCJ0qmTUov4uEym7_4EinsLG4sedYHs8boszMxlivR-jH8-6hAzB256VaUoVvq-0IZ0Ji5V5P-Z1PY2sYXhprsxQ1rMkxeDOinhnIKvAvzn-Ut_1cXYszaOh6Noa1LZfzPuUyWKL7UmBlqZn_o8bMbFVLgNB-OGT13zNZOypNjiSq7p99NRrjQzvIcKrzQgndxiBqOwGirFz1hC1iIoGVKYwmWIOBP6iFKdmjQxdlN1zniAsYXEBE-uezIFU9T-VTzA1sG3MGQYTGQj5Q36CumhauDYB7c_Dk6TRuD5yEEKMNb60DUUUW71rhqsqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت محسن رضایی از آخرین دیدارش با امام خمینی (ره) و جمله مهم ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/akhbarefori/656630" target="_blank">📅 17:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656629">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsLZlGa6W4AAlxm-70vshQcWdU8fvkCCXR24GdBOMmotWnXU2lj8fzmnxzNliSQRUe24_kPEcVfy8b9N7I1oyrgjXpkrrDotuX1O54g-MjJ3AjtcLonVra2_yMqm6wxetxwk6BOIstnvOEfe127N3-UkQ5f0RYi_dxwoT39pHKBfsm7ZnwkA4uvtsAUXYwt77QFutiDkUUccItbLfXJYrRzgoPCsV90jxlFK0XrK_kxhlGubGRzwKRlHcB5NkK_RYetXxlc2bZZOjQr03sNRCbHAD4nFqxEHvxHrAKhik33_mg_6KjDLwZNUd6qTNAzpScPx_BuiA_2wO1eKVQROSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاهی فقط یک رنگ خوب، حالتو بهتر می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/656629" target="_blank">📅 17:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656628">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
احتمال سفر دوباره ترامپ به چین
مدیر اجرایی دبیرخانه اپک:
🔹
ترامپ ممکن است برای شرکت در اجلاس همکاری اقتصادی کشورهای آسیا-اقیانوسیه (اپک) در ماه نوامبر، به چین سفر کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/akhbarefori/656628" target="_blank">📅 17:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656627">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ممنوعیت دریافت وجه اجباری در مدارس دولتی
وزیر آموزش و پرورش:
🔹
دریافت هرگونه وجه به‌عنوان شرط ثبت‌نام دانش‌آموزان غیرمجاز است و ثبت‌نام نباید با فشار مالی بر خانواده‌ها همراه باشد. کمک‌های مردمی کاملاً داوطلبانه است و هیچ‌گونه اجبار در پرداخت آن‌ها وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/656627" target="_blank">📅 17:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656626">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تروریست‌های ضد ایرانی از کردستان عراق اخراج می‌شوند
شبکه خبری العربیه به نقل از یک مقام عراقی:
🔹
دولت بغداد قصد دارد با هماهنگی مسئولان کردستان عراق، تروریست‌های تجزیه‌طلب ضد ایران را به صورت کامل اخراج کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/656626" target="_blank">📅 17:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656625">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f566b3db.mp4?token=PMuTuvUc_lW-_mYfDgAnETfwH62o8_5YcUVZSz5aUhnf_nJ5gcjtGrHhAfxl0HBqvWzmGTcbqRAjBrYC-CSvy-MJuHCNWArkcxnf6V3Mtp-FdvghCqQrkHuJNgcgWdVW4WNG4pyHUbkqbjUU99zB5Vv9NxElYZl5Tq49dbJgS7FyXqoK9BJYzBvCp5p5Eik5ZhaegVBOGMvXq1n9BRL8RnoBZBNBmTcdV7BM50_KHhHugRDWY96AyKngX1GM2yebqHurxjW-mamRT_PNgbWGzociJb3RPdyGmsKLQnYuJqWAfF3JOwnj1tTwytM3iLJn62niybtDbR9XhB_okH5oVV8NaGJM8tAwZpGvkOapiTUcQmRZv1a8YhejXgEbUweaCnhjHdmG-JXstZOczPLY8gFx4XUC91-mk4XzznrpiuXxcTndQDiJCqA6dchVIXQ1KTLkX5UJmzopd8XCO9xQh2EtEGCz0OJfRL3_nCnod0S5FkPyklKM4HLikmCHxmVeWcA0B06LVIKOMmnjQ-cqHuXtHNfcgwXOL4bErebvQ0cJIJgImrOFVu8BzIjFDPNpPaZJPgOZfE8iSXuqXVtZm9xFuKq0F08G5tZEmfoC0uh1eIuDv2gM95XDmFprtv-AWIc9GZhjeg-iwsAKCn2rX7J1QnapFIE209Y8F93FdRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f566b3db.mp4?token=PMuTuvUc_lW-_mYfDgAnETfwH62o8_5YcUVZSz5aUhnf_nJ5gcjtGrHhAfxl0HBqvWzmGTcbqRAjBrYC-CSvy-MJuHCNWArkcxnf6V3Mtp-FdvghCqQrkHuJNgcgWdVW4WNG4pyHUbkqbjUU99zB5Vv9NxElYZl5Tq49dbJgS7FyXqoK9BJYzBvCp5p5Eik5ZhaegVBOGMvXq1n9BRL8RnoBZBNBmTcdV7BM50_KHhHugRDWY96AyKngX1GM2yebqHurxjW-mamRT_PNgbWGzociJb3RPdyGmsKLQnYuJqWAfF3JOwnj1tTwytM3iLJn62niybtDbR9XhB_okH5oVV8NaGJM8tAwZpGvkOapiTUcQmRZv1a8YhejXgEbUweaCnhjHdmG-JXstZOczPLY8gFx4XUC91-mk4XzznrpiuXxcTndQDiJCqA6dchVIXQ1KTLkX5UJmzopd8XCO9xQh2EtEGCz0OJfRL3_nCnod0S5FkPyklKM4HLikmCHxmVeWcA0B06LVIKOMmnjQ-cqHuXtHNfcgwXOL4bErebvQ0cJIJgImrOFVu8BzIjFDPNpPaZJPgOZfE8iSXuqXVtZm9xFuKq0F08G5tZEmfoC0uh1eIuDv2gM95XDmFprtv-AWIc9GZhjeg-iwsAKCn2rX7J1QnapFIE209Y8F93FdRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی ترند اینستاگرام برای تیم ملی فوتبال در جام جهانی
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/656625" target="_blank">📅 17:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656623">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWao0njeMy0Wal9HtHqV-HCUZLi-c3-6RwhnWHE6-zTSs3a8pgsmr41aHNuVux8CR0x884_-7p0s9z4-Mos7R1c8ki98iTSSG24OC2EShoXss-JHl5R8EphqDnV8yp0AN5hggyYBtbqPCMvTmCDHKpYIwXxvO9Bz5oyyVniNnSQ4tINYpIvVTWs8-Zm5jNPCeinhKCstLvfj62M6_TpwsI1MdjUCy4NnOrTCFsaI2_JLj6Loqwac3S9BBYT-0PKrfcq4wHNBLe8tPAzDeGnyVcFQTnoEd46eFIKcwAlrvtfTNrQvZoe5X7MXjpChmm34CVe-INEksSspFY6vIXvxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ایران برای صلح پول می‌خواهد/ ترامپ سختش می‌آید!
وال‌استریت‌ژورنال:
🔹
یکی از دلایل اصلی گیر افتادن مذاکره ایران و آمریکا، این است که تهران می‌خواهد به پول نقد سرد و فیزیکی دسترسی سریع داشته باشد و از نظر سیاسی برای ترامپ موافقت با این موضوع خطرناک است.
🔹
آزادسازی دارایی‌های ایران از سوی ترامپ، با انتقادهایی روبه‌رو شده و با حملات گذشته او به اوباما درباره پرداخت پول به تهران مقایسه می‌شود؛ ترامپ پیش‌تر وعده داده بود به‌جای توافق هسته‌ای، «توافقی بهتر» با ایران منعقد کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/656623" target="_blank">📅 17:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656621">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjNNXb2Fs5uERygoZxntjKh8g9HaykLp2yfP_O2kiwN8gplzzJRMfOF0rvcKFZgOcC9l2x2ZkUwRBOo6Ig6kJ9HaccwG3SoKL7KeLwyE_1IRLDUOfMhzZnXP3qZkH8e6vye_GbT0MgkJ4ORLrBNHu-sLvBzKhRWosSUuXvBpoc8VGrN3sfpLNturOf0jvKlvf_zDb6ZW70cthjgoSXKNhx6pIvisnMuNLKwSV8WOe5VQytG4mJhcUJ6_A7VNQaMLD-hAM_r-y8QyptdVwfQ_A_v6h_yg4Rj4uc0AdnpbNkCRXjZQ55KIPSC86fdwGY64PlulQFFgYkFRILE7g7JNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوان‌ترین و مسن‌ترین بازیکن‌های حاضر در جام جهانی حدود ۲۶ سال باهم اختلاف دارند
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/656621" target="_blank">📅 16:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656620">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تمدید خودکار گواهینامه‌ها متوقف شد
رئیس پلیس راهور تهران بزرگ:
🔹
در دوره جنگ، برخی خدمات از جمله تمدید گواهینامه‌ها با تسهیلات ویژه همراه بود و مقرر شد اعتبار گواهینامه‌های مشمول، به‌صورت خودکار تمدید شود، اما اکنون روند ارائه این خدمات به حالت عادی بازگشته است./ مهر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/656620" target="_blank">📅 16:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656619">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd6e0fc384.mp4?token=UKvGB8foXlVusYFjyC8f0TJBWlYr5pVDflC4i4_Sqm8JUm31Ty_yqLiPx8G_O0KlQJ8egatS1HMCXxPTyH838yTkYm6MyAr3TTT4JKuqx77MRqF90mOaoHYaJJ8yvlNIV4n6iSiajpWGLjBbLZV5AuDyjfFN2Pt639HZrQ8bWD1LoOKUJ-r42q9lDADLOVMgHA9Fyp8tQYqnntJY--PdhSwIvVJtDyNbK41k-LRliq3gbOKbBl0kLmWaRnPf3S37RMWpAQKVe7SZqemOqRIzeKJF-mjb7Uqzfqxd-VKenzd4ppUyD8_mttNmcB9EZyq7UeYm_QqkvESJU2mJDm-CQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd6e0fc384.mp4?token=UKvGB8foXlVusYFjyC8f0TJBWlYr5pVDflC4i4_Sqm8JUm31Ty_yqLiPx8G_O0KlQJ8egatS1HMCXxPTyH838yTkYm6MyAr3TTT4JKuqx77MRqF90mOaoHYaJJ8yvlNIV4n6iSiajpWGLjBbLZV5AuDyjfFN2Pt639HZrQ8bWD1LoOKUJ-r42q9lDADLOVMgHA9Fyp8tQYqnntJY--PdhSwIvVJtDyNbK41k-LRliq3gbOKbBl0kLmWaRnPf3S37RMWpAQKVe7SZqemOqRIzeKJF-mjb7Uqzfqxd-VKenzd4ppUyD8_mttNmcB9EZyq7UeYm_QqkvESJU2mJDm-CQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: اعتبار ۲ میلیون تومانی کارت امید مادر به حساب مادران واریز شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/656619" target="_blank">📅 16:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656618">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5531e602d2.mp4?token=D2Etk0RRx8luecclsMUbxs2v8PJLXRiDgbihY3AHC_dofW8-wuBrNoEs23-o-cjx8a1GpQuXa14RCOKkn7YcTw9_-xCs7jzzBI-K3XZCa-iQV7I_hnMKuHSNUAaU_3d6L1K0m2AFn7QBcWH_L7MgNA-nSzqw-CxMlwaua-nzsShi7k-ZmaMzojiF47lizhRIyYBxZZK7dDNf_D9cPQBMvJEdHLXsTGTBeIx5erLxVOiP-PROtTvdS4CdEtEUAJlYFOpcpUYLUzJuzm1fnZH-6qFX-FTwOUZWtFK27sVYlW5toRrhQ9qyVHIpNx2zJnvH0fpuSSjvI0szTCK4IIAJGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5531e602d2.mp4?token=D2Etk0RRx8luecclsMUbxs2v8PJLXRiDgbihY3AHC_dofW8-wuBrNoEs23-o-cjx8a1GpQuXa14RCOKkn7YcTw9_-xCs7jzzBI-K3XZCa-iQV7I_hnMKuHSNUAaU_3d6L1K0m2AFn7QBcWH_L7MgNA-nSzqw-CxMlwaua-nzsShi7k-ZmaMzojiF47lizhRIyYBxZZK7dDNf_D9cPQBMvJEdHLXsTGTBeIx5erLxVOiP-PROtTvdS4CdEtEUAJlYFOpcpUYLUzJuzm1fnZH-6qFX-FTwOUZWtFK27sVYlW5toRrhQ9qyVHIpNx2zJnvH0fpuSSjvI0szTCK4IIAJGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: اعتبار ۲ میلیون تومانی کارت امید مادر به حساب مادران واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/656618" target="_blank">📅 16:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656617">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
منبع آگاه: وزیر کشور پاکستان امروز به تهران سفر می‌کند/ ایرنا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/656617" target="_blank">📅 16:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuLNvK3yDvlYat22MOBZcUCP8L3qcroebLBbbzJDI2Li65bRDzq1wyJbiZffXQJ19tzdzddbroaAfx4nbojkSx48eIAB4jWZoZvPerqHhihGX-iVmjLhRan9PjRw-btV19DFXlcq5f_IP8Yr6IySvIiQO6bcEPKbATANOz_cohfmcgXGebTsD3nk8JPxu7Uviz2qqIEwbr3jv6pRG01WXAJ-EKfMNN4DhUjEN1uFdK-CxWftowRIbQSuU04vGwirezNv_2ricjG9S4TN54QmMZP06Oup9dYK6IYVC78dEcngSyH4SVMWaZmZ3CFKO3fuQPEcfQuwi9R7WmcoZc63tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFblXjtdKOBb1d4jbt4OZnsJb5r7IKJGrgH8e8cMaCIa1JrnFOnEvwhbX5HPkoVsM0lBVCcpwMNUbnQ-NvEuizOj--ECFLigz4OEuzog46lf5mT0RjoNGZP-XCL9d7aqDCtxv7rg6o-yR1_nieq2vRwcNMZOTlmNfvKSk4E7ByUqKf75SR3DhMzdl7MhIU8CVsI0Iwz1kWgDTsMXb2u2N7r6dkWuS3P_VuICSqF7ZAOz9Squih0WTBUXRumA0Th0cC4TwouKkog-_IvvdsAZUrfMoBsNcDvG37hsn758HoRwG_orswXuXB2WKx2MqaWFzNTerXHKyiXpmSTfmdXW_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از اعضای تیم ملی فوتبال ایران پیش از عزیمت به مکزیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/656615" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مایکروسافت در واکنش به افشای استفاده ارتش رژیم صهیونیستی از فناوری‌هایش برای جاسوسی از فلسطینیان، خدمات نظامی خود را محدود کرد
🔹
بنابر اعلام گاردین، این شرکت دسترسی ارتش اسرائیل به برخی سرویس‌های ابری و هوش مصنوعی را به‌دلیل تخلف از قوانین متوقف نمود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/656614" target="_blank">📅 16:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تکلیف ۵ بازیکن خط خورده برای سفر به مکزیک مشخص شد
🔹
کاروان تیم ملی فوتبال ایران امروز اردوی خود در آنتالیا را به پایان رسانده و ملی‌پوشان تا ساعاتی دیگر با اندکی تاخیر راهی تیخوانا مکزیک می‌شوند.
🔹
بر این اساس محمد خلیفه، هادی حبیبی‌نژاد و امیرحسین محمودی سه بازیکنی هستند که با وجود خروج از فهرست نهایی، در کنار تیم ملی باقی مانده و راهی مکزیک می‌شوند. در مقابل، امید نورافکن و کسری طاهری از جمع ملی‌پوشان جدا شده و به ایران باز خواهند گشت.
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/656613" target="_blank">📅 16:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvaUK2PVpmaKSim0TUmY1MNSOc_GfIdOuNOBp6HvDUjx-ADCsbz39ViDcrbn4muDO-F89fKMxTvxzlEW9sMkwW-4SjiTXLYY2gSy7JybkxBl9GKM4ql7ItCy2T69-rx1RfO0XzqYrp1FjItWsrqdSN3AMnySOusanin33bgdSCrgNAbwMFNSIueVQiiGN7CWxGa9merVPnfopytXR6UPM3xWpO4D2heXavu4HHIhGC4N0bNb_qN4lILM94xayj5G6zR3Tt0NTEkDH3KLp2-0tRxvn0vIdC8ZemuuC_DNPOdVjnvrB1ig_sDRWaMJDVxnyaPioq-wxYrjMkHq1w8R-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه جمهوری اسلامی ایران در خصوص نقض مستمر آتش‌بس توسط آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/656612" target="_blank">📅 16:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656611">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b44d587.mp4?token=S9qnS4kwiPtKLEMW0NRh5wVAJ0R2wTSO1aHKITPZavdxJ6EIXn8Gr4b0AK2YQ6Z75hoRxrhKXU3t-loBLU93sYz8y6ZPhi4LprPe7yaR9CEgNg4PtedwP8-8JuRekQ8HUotQ7bG9prN_tXS4kpbznyYuMrKgLVW8n5eJ9aSVgGe8Im1-ow2n9e23o_1EQ1H6hjrnLzakqdSwhreI7_ImN2MgbHedSnFQDdZkIiN19jrA2i7OwneL6rYfOcwvwt-Jd2LMRyjTxvfM7Wra61P_rTeILmosDILmLNIOI2sn6S1kOX2nnKNtbuOeaYOBq2UdS9Qwg7MLNYmaGmlZ5Tv2uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b44d587.mp4?token=S9qnS4kwiPtKLEMW0NRh5wVAJ0R2wTSO1aHKITPZavdxJ6EIXn8Gr4b0AK2YQ6Z75hoRxrhKXU3t-loBLU93sYz8y6ZPhi4LprPe7yaR9CEgNg4PtedwP8-8JuRekQ8HUotQ7bG9prN_tXS4kpbznyYuMrKgLVW8n5eJ9aSVgGe8Im1-ow2n9e23o_1EQ1H6hjrnLzakqdSwhreI7_ImN2MgbHedSnFQDdZkIiN19jrA2i7OwneL6rYfOcwvwt-Jd2LMRyjTxvfM7Wra61P_rTeILmosDILmLNIOI2sn6S1kOX2nnKNtbuOeaYOBq2UdS9Qwg7MLNYmaGmlZ5Tv2uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گستاخی سفیر آمریکا: واشنگتن هر طوری بخواهد در لبنان تصمیم‌گیری می‌کند!
سفیر آمریکا در لبنان:
🔹
مذاکراتی که در واشنگتن برگزار شد، بسیار مهم بود، هر طرفی حق دارد تصمیمات خود را بر اساس منافع و رویکرد سیاسی خود در پیش بگیرد.
🔹
ما در لبنان هر طوری که بخواهیم تصمیم می‌گیریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/656611" target="_blank">📅 16:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656610">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9jdXV67MRtIHD3HoyQAtXf8tOYWoKBwuHx2UjL8_gNUCvMwiAtlXnAgj2g7cSWNdZZma3t1ht_jR5h8WIAzSApnnEFroIjF4jNK_TUQIRfntbRxCFLlrjdPCUyyb_wV_5KuXieM4l0gqJUnBQA4LLS3E0pfUpmK_zgeWkCZXbmYZ2PjWMR00jiXijVV7-Q0MJvoLktR8mag0-DzPT1GDAeckj5eUI8iUC0aeCTqSVVrPLIvcIYUojtknt8P2bMEtMIjv8Iz4WGHx4gduyMCJbrpynhgB_JO4ZYLyi2QnirzmvlYRXLYx2-JKOJALCOuUrS5K8FPdrTroYlgK70Pug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه‌های برگزاری جام‌جهانی در ادوار مختلف
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/656610" target="_blank">📅 16:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656609">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3c84cedc.mp4?token=PQgV6C5LpMlOxJerByxztbNiGBDN4pAGEyGb5EGDUUHLN_bOcBCYSjtnDSQV0iJsdVjU2BpYENFCiwKchrCaxi8EuRHKQZgV86ikSvoiTfMpNu8ScOpQoW11ajq7vegZ18C1n3RpXNNmy2AA6xgNZWkLj-TU8oPPKe1SyjVLrkNGQFl_y4XmRnU8JlFON-qakDYHWTW7eLErCNyHg0vRKRe1GdV_e6e-JGiK9x3uDABRwNLxrjdrA2KesVufBOiSOWskwhwGk_OeDE7dn5JNb79eNffkUCzeOjZs5DD2Hd0FPeKj8xLl-W2y1aANbZDKKEfNkqv001SApZMkVUhVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3c84cedc.mp4?token=PQgV6C5LpMlOxJerByxztbNiGBDN4pAGEyGb5EGDUUHLN_bOcBCYSjtnDSQV0iJsdVjU2BpYENFCiwKchrCaxi8EuRHKQZgV86ikSvoiTfMpNu8ScOpQoW11ajq7vegZ18C1n3RpXNNmy2AA6xgNZWkLj-TU8oPPKe1SyjVLrkNGQFl_y4XmRnU8JlFON-qakDYHWTW7eLErCNyHg0vRKRe1GdV_e6e-JGiK9x3uDABRwNLxrjdrA2KesVufBOiSOWskwhwGk_OeDE7dn5JNb79eNffkUCzeOjZs5DD2Hd0FPeKj8xLl-W2y1aANbZDKKEfNkqv001SApZMkVUhVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاراگوئه‌ای‌ها به این شکل تیم ملیشون رو برای جام جهانی بدرقه کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/656609" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656608">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130a36096c.mp4?token=kiYnE6L-vTG5KskQUybq-LHSgyCXn78yrI5UGjOTynVg__mfzux01oTObhJ_4Ar-cBwkmzgq-nqiL6l4801izzhkRhAxw9v-pmZQ6IkY95-gqDAnjY-lPFwr3cNKVowtFIPz_o1V0xU54u7nTOAV2h7btNUH-9pBTji8ljvFvAuXqKI6Y0R8vPi9HEmpU4E7q3GioVIaoq9zdMfmcaLth0IBoUwzByZqY5klKWauDOGEk7qf_1e1wG8oz0cIBz6-49_t4KBb4_5n1C7cvmG3TVxcOMm-zOacZsK4q7Ccl2dbPjB6d4YjpnCP-Al7X9c8pOFIDkiKtCx4A_wDYitwgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130a36096c.mp4?token=kiYnE6L-vTG5KskQUybq-LHSgyCXn78yrI5UGjOTynVg__mfzux01oTObhJ_4Ar-cBwkmzgq-nqiL6l4801izzhkRhAxw9v-pmZQ6IkY95-gqDAnjY-lPFwr3cNKVowtFIPz_o1V0xU54u7nTOAV2h7btNUH-9pBTji8ljvFvAuXqKI6Y0R8vPi9HEmpU4E7q3GioVIaoq9zdMfmcaLth0IBoUwzByZqY5klKWauDOGEk7qf_1e1wG8oz0cIBz6-49_t4KBb4_5n1C7cvmG3TVxcOMm-zOacZsK4q7Ccl2dbPjB6d4YjpnCP-Al7X9c8pOFIDkiKtCx4A_wDYitwgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترند در ترید یعنی چی؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/656608" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
خودروسازان موظف به اعلام تعداد عرضه شدند/ قرعه‌کشی پابرجاست!
🔹
شورای رقابت با اصلاح دستورالعمل بازار خودرو سواری، خودروسازان را مکلف کرد اطلاعات مربوط به مشخصات خودرو، تعداد عرضه و مهلت ثبت‌نام را در تمامی طرح‌های فروش و پیش‌فروش خود منتشر کنند و در صورت بیشتر بودن تقاضا از عرضه، روش ثبت نام خودرو را از طریق قرعه‌کشی انجام دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/656607" target="_blank">📅 15:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بارونه بارونه بارونه</div>
  <div class="tg-doc-extra">کربلایی محمد فصولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
بارونه بارونه
#شور
🎙
کربلایی‌
#محمد_فصولی
#ولادت_امام_موسی_کاظم
(ع)
مرجع رسمی مداحی
👇
👇
@gharar_madahi</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/656606" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656603">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMmHdvnUl_aa1zEzz70X8A-55-SExETvC39sb8idTtnpATl9soTNPOjnJKKnSyeSsOLPOesqZu0m3gYBiaH1_tYuUQBYc7oxln8rAz_B9J7o87zAi71tMHEfwPfOG-WMNJo0vhqbqO57Z67zK1uUNmEr_UZ1CK8yCEUFXCgHJjzxMRmKUwb4i5UPa78EI3G172pjUPmn7EPfyCuPjrvz6s5oWF2HVYl5ymUpNAwjzXAhss-u8o5K9IJKJgOfpalWcaY7vMl3nV5idEZU3gl5d5ROMDB0YqKItcy8g2CvT776DRHFTxwZ9eLaC4aYtV-cLaTdeSp1W3Rv8Y0CFhwAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9G6NxJtEu_jxnSk0-XvTzYL_i_RQvvGfw3Me36OpwOD_cC3-Pf8V_xbkegnw8O312NVW-8JTaUqb5snjH7Q_7RdrlYum6bU39jER1HXtTRSGI5ItG5cWEyVwG51Hz1eur4PR3CdJG90CO9l5N3TAO-fP0FHFANcBKOmRcP5F7PzlVTXCJg465pSscgvn2Z7xCHcdNiYNz1MY9jZqefXMLhwCHc9E_LIXPeiUQnNjquuNzw0Rq893Gf4gmoK0d_YtOTOgmFAv32o0ephqex5XM4pre_bVFR8SxPJ0pYjvds9TwbU0vdqhyGu_QYUo62MI0iFQAdcyGAOQO_CgLaydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-vCxY77WFwNcO3KYUv4P_-TyreJRSO2UPZGekhVSIl08y8fMV0c2LpvIpWwodTEbDYoWO_cjskR8N0nhaFDEouoZZD1ti7loOPPoBN3MWEgwUwJcc5ruTcBFp0aDcdkbdQCP4o8rg6U8eMJNin_35rErNTABK6AiGQ02O5orToWdDukBqK7SW5kXWKkvGTI_MU0j-sVBCfnu5zRpnnuENXP2nLtOOV8jrUDUn1kPz5N14du3xIb7_Kb0VBp3gD22cqNzvsdUZXei1qK_sLMpESlHaYT4ZBzZPw_rKIkG19GoY3xHLqHqfiC-515Tt6pUHMECUgKFZwRb3a98Fig2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری عجیب از کاخ سفید؛ آماده سازی کاخ سفید برای برگزاری مسابقات UFC
🔹
قرار است کاخ سفید روز ۲۴ خرداد میزبان شش مسابقه UFC در قالب برنامه «آزادی ۲۵٠» باشد؛ رویدادی که همزمان با تولد ۸۰ سالگی ترامپ برگزار می‌شود و برای آن سکویی بزرگ در محوطه کاخ سفید ساخته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/656603" target="_blank">📅 15:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656602">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906cfb11a.mp4?token=Z9ljtvz_5F0CIz2JPjIMTazfLWKiQQ2mNBIIf1gCGVQVs3ES0_Wo1qZbk-wRlk6Sxc-2YuT_C8XEHM-PbHKOSaB0UvBUk_xZyQ2EZ9eUK2fjJXctnM2kSHkvSFyrpqHiyJh1t_cEmuCYQPwU4X2qVEMK-cYUN8Kk7NxNF0p5145MYf8ZdRBSE7yg32E5igCjwiIrhxQ9ib0b4TV9hsuRco_8HzgrFS6wseTgz6FebA95AQVU0QygzwD9vsUBoeZNI_tXlJi3775XMdnWIEDC_mpLuRNeCZHqa2YpUUZ41u-_ufBUVRk65Kw7GdSiJ0uJN0jHoEAEZaFrcf1YuDwZj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906cfb11a.mp4?token=Z9ljtvz_5F0CIz2JPjIMTazfLWKiQQ2mNBIIf1gCGVQVs3ES0_Wo1qZbk-wRlk6Sxc-2YuT_C8XEHM-PbHKOSaB0UvBUk_xZyQ2EZ9eUK2fjJXctnM2kSHkvSFyrpqHiyJh1t_cEmuCYQPwU4X2qVEMK-cYUN8Kk7NxNF0p5145MYf8ZdRBSE7yg32E5igCjwiIrhxQ9ib0b4TV9hsuRco_8HzgrFS6wseTgz6FebA95AQVU0QygzwD9vsUBoeZNI_tXlJi3775XMdnWIEDC_mpLuRNeCZHqa2YpUUZ41u-_ufBUVRk65Kw7GdSiJ0uJN0jHoEAEZaFrcf1YuDwZj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهران روی پوست تخم‌مرغ!
🔹
اعداد و ارقام این ویدئو می‌گوید تهران دارد منفجر می‌شود و باید فکری به حال آن کرد!
🔹
۲۶ نهاد متولی تصمیم‌گیری برای حریم تهران هستند اما عملا هیچ‌کدام تمرکز کنترل بحران را ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/656602" target="_blank">📅 15:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2rjYIvZr0QDBRLnRHAuyyY-RUSF3QW7BQso-0k_szjDq1DGSaeOQ4geXW-gMav7Il1bOBQl0HGVineyVy3-iJg3d74u-tSDG_gA7EFO-GBu3s8eBYnJpA1vUcE1fdTg45XeIzZoxGVLGWaG7IaPA62lizq3DmVjQ7elDZkwVF60rLhZ-kyIuepHlniiBhW6wqsDZEQjurWMAEbtkRjFnYT4xmIOKPyoDKA8tdOPF28iQSgWvzTbAl0wnOihdC3WyCfwlN7vkpS6f5aWOTJFqfvs4mcNEEPJ8OCMF_rnjBNrdY329Wwaz0x57PUsC0uDb_yWjt-GBe1gHpd0wyKHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای بلغارستان بر گردن نخودی
🔹
محمد نخودی در فینال ۸۶ کیلوگرم رقابت‌های رنکینگ اتحادیه جهانی کشتی در مغولستان، با عدم حضور حریف بلغارستانی (قهرمان المپیک) به مدال طلا رسید.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/656601" target="_blank">📅 15:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShtEVAIB5VwS2RTZ_DyovpScMO9rWMAshQHQJqrE_IvJ5mC40PRqFfIxXs2J-GZGL6Hvt4XEWfq2Y4NMIESrqhE03k6V5VOqF7KQWQDbZNI3r2BHXqGGsNVm3YkOPLouTU3EpfQSp7tzMVsZzY_su5crRiU1RAW2IUu-IRmogby2BaEPDO9DTfN58_skAQZkWyXWwlokOsmXeMu0Be3075lVtd6wqFepzCgY8eB6Ib1KPVtfCmR0N3czqJVAt94QUVZL_IkEHxXVocSvqOsP4CYk9CfKfwGFKzLUxpGnYtfpbBbkoY_zFnfXpBbp_XI2MbS_LGEBWR30xHQ-wcLCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرحسین قیاسی: سکوتم در جنگ اشتباه بود!
🔹
حتى در صورت سكوت هم معلومه كه من مقابل كسى هستم كه بدخواه كشورمه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/656600" target="_blank">📅 15:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
وزارت خارجه قطر: بر ضرورت دور نگه داشتن منطقه از پیامدهای حملات بی‌دلیل تأکید می‌کنیم و بر کاهش تنش برای بازگرداندن امنیت و ثبات تأکید داریم./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/656599" target="_blank">📅 15:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656598">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9yQz9I6IQ6wtbq3w3RNTAi2GbR1AfHbT3PFEnGf81g6JgOFvBs9o4Y6Tj6lICus64t_9uYHXytAIblJxvc1qY3gkH_2EPLrBPWm3yLgTpOAs3ZgOPRzZTb9jkTZQg5HSr_ZePakgtn4tWYiyhldaJoaa2jZedNsjsCGN66Oof9dfyOp4u-zzOLFGjkjhXjsA-eTqU8BHe3io01rBTJWUvtSrmtGwnegosOfQt0kaaoosny4YulwkMh57c0uEKem1MPaAyAtsKoaEONPSbrkJ-GST3yGTcYZw8_3uLd77Ih2YJLYLW3aDphVaj_1i1vPZIhymKkP_IhWhxx3DXQcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به جای طلا، مس بخرید!
🔹
کریس واتلینگ، مدیر یک مؤسسه تحقیقاتی مستقر در لندن، با بیان اینکه دوران «ابرچرخه صنعتی» فرا رسیده است، اعلام کرد: اکنون زمان ترجیح کالاهای صنعتی مانند مس بر کالاهای پولی مانند طلاست.
🔹
نیاز شدید به توسعه مراکز داده (دیتاسنترها) برای پردازش مدل‌های پیشرفته هوش مصنوعی، تقاضای فلزات صنعتی به ویژه مس و آلومینیوم را به سطحی بی‌سابقه می‌رساند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/656598" target="_blank">📅 15:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khr8zi-kfvpEXhi8pIKlYHLLB6zhvhVpsi2USL46zCJYlre0YwrIsE1YV_tJHK7gFR5rjFV7gH6fn_F5Tfnlb_IeGE-JdqRvmQvxM6KKdsZo3Q__dJ66x6Qnbp-Y2R3_DhqxUyCpspu4BLfvhiUtIKjILLv1vGtVLSdzUU4j4skA7u1UAEPNgOlvo3BNsR-J519EZM0365xXUG5U8PwvWVTVqS0Zkg2QdAci0v16ijzQhoM9zB_C-DTl78a1O7a4Ltgh6oYPijw2rilcrpFdPCOBDCAJ6jpELJEWerOnbEJxdi-X9YwVpNPmWLAMCSMDTojPbU1zfYnkSf-s7w3f0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست عراقی‌ها در جام جهانی؛ مجوز برای پوشیدن لباس مشکی عاشورایی
🔹
فدراسیون فوتبال عراق به دلیل همزمانی بازی این تیم با سنگال در جام جهانی با شب شهادت امام حسین، از فیفا درخواست کرد مجوز پوشیدن پیراهن مشکی (لباس سوم این تیم) را برای این مسابقه صادر کند.
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/656597" target="_blank">📅 14:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش قیمت بنزین تکذیب شد
🔹
چندی پیش شایعاتی حاکی از افزایش قیمت بنزین منتشر شده بود که اسماعیل حسینی، سخنگوی کمیسیون انرژی در
#گفتگو
با خبرفوری بیان کرد: طبق آخرین گزارش به کمیسیون انرژی، افزایش قیمت در دستور کار نیست./خبرفوری
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/656595" target="_blank">📅 14:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656594">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای العربیه: درمورد میزان و زمان آزادی اموال بلوکه شده اختلاف وجود دارد/ عراقچی و ویتکاف در حال تبادل پیام هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/656594" target="_blank">📅 14:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656593">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گوشه هایی از مهمونی کیلومتری غدیر تهران که امسال رنگ و و بوی «بیعت» داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/656593" target="_blank">📅 14:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656592">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1wmU7qsg16ILABlPEr7NIpV5Z-1M3R0H8qQywq8WqTlOIDStORaVdjUmjhaYMRVmFVtUiAFgJbySPkKCB3nE8VqbdXGE_gR5tYhmxHxko8ry2E4P9ApbC6u9O3zfy_j-C-qK-tsPxucJvHjjIgjytfjgHei90RkINjhF5EO13VSHMCsGJQUW1Fsik7KIkvatfCk4pvp5wwZVl2rbjl-RF_Yc0ly1zUit_Bt1YzX0z7tYvyOru6CwlxpXlCqzuNluMaBzIGzRhD0WQ474jk_6shTNgpqSBso2bwQgsiDLgrUPnATwME3hURtqMdlxW3cds-Cxqw76N0zUrtts8ICxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ هوش مصنوعی که دارند آینده را تسخیر می‌کنند
🔹
OpenAI همه‌فن‌حریف دنیای AI؛ از مکالمه و تحلیل تا ساخت ویدیوهای خیره‌کننده.
🔹
Gemini پژوهشگری که می‌تواند ساعت‌ها تحقیق را در چند دقیقه جمع‌بندی کند.
🔹
Claude وقتی پای منطق، استدلال و مسائل پیچیده وسط باشد،…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/656592" target="_blank">📅 14:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656591">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
فقط ضروری‌ها ویزا گرفتند
🔹
وزارت امور خارجه آمریکا مدعی شد که «برای افراد ضروری» از جمله بازیکنان و کادر پشتیانی تیم ملی فوتبال ایران ویزای این کشور صادر شده است. #جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656591" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656590">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است.
/ انتخاب
🔹
سفیر پاکستان:
اسلام‌آباد آماده ارائه پیشنهاد برای مذاکرات ایران و آمریکا است.
🔹
سفیر چین در تهران: همه طرف ها باید به حقوق مشروع ایران در تنگه هرمز احترام بگذارند.
🔹
استانداری هرمزگان از احتمال شنیدن صدای انفجار در بندرعباس به‌مدت ۴ روز خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/656590" target="_blank">📅 14:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656589">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da218c54b4.mp4?token=SD4em33LhFbhQvWHCFlmQ9WoWvRbmdnip5aLt8PhRf0oI_z_rb6O08JAUqZax7RbEtAQenaQOFoLKaG9WOHSNUumPlK2iRytdNS0RdYLzQIFPfOvrHy8066ufJvH14mAWqA93jgoUk9SF9vc1rDKvcgbQYuQTYEvw4jWSpgH4b4oqPxCNorutL0pod1JGYNHkwTl1sNHZhtJSvhtNpY9Qga7DJkny20t9xJkxCzdse0zmsDHQnbDzbR_Q_JL2qLSPogWWuW4GE7wrlTXkPgBzM1uKrLFIddmK3fthRmEN8pIS-bxeutEJ3o4gObh5-Pc-_ke9RMU2DCmVbXcTlG9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da218c54b4.mp4?token=SD4em33LhFbhQvWHCFlmQ9WoWvRbmdnip5aLt8PhRf0oI_z_rb6O08JAUqZax7RbEtAQenaQOFoLKaG9WOHSNUumPlK2iRytdNS0RdYLzQIFPfOvrHy8066ufJvH14mAWqA93jgoUk9SF9vc1rDKvcgbQYuQTYEvw4jWSpgH4b4oqPxCNorutL0pod1JGYNHkwTl1sNHZhtJSvhtNpY9Qga7DJkny20t9xJkxCzdse0zmsDHQnbDzbR_Q_JL2qLSPogWWuW4GE7wrlTXkPgBzM1uKrLFIddmK3fthRmEN8pIS-bxeutEJ3o4gObh5-Pc-_ke9RMU2DCmVbXcTlG9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آخرالزمانی یک آتشفشان در هاوایی
🔹
طبق اعلام وزارت کشور آمریکا، فعالیت این آتشفشان در ایالت هاوایی همچنان ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/656589" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656588">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055f3b54ae.mp4?token=Qu6Ruc-mhxF_2TDPQa2dqGwUt6KOap3oNyLPpfBYtlj_FEtLRFuCEdfSRj7f3ithH2PS0zjIaSbIe3HpTqKdidvvXiPUi1GWgVF-jX-fKLPgyz8Dk5MT2DZn8DCmUhccUAKDfaXRXdgbJO51zUMlLCrBaUY9UCvNyuao997Y4x5xImC1Rx7Nut_jBKOAalDLukXiV8EO93IKagcZ1OE6YvDEZr0JvDfpQ8I_6xdogOC72TeDoyzqAigfU4ie6hVvf6k1KJ4hOyrKrbGrx95K1yxy97jnLfMjdaQNB_O8NK9-tQ0FG4Wq1M5nGftAl27g4pjmmse5eLqzoxdYBP3MCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055f3b54ae.mp4?token=Qu6Ruc-mhxF_2TDPQa2dqGwUt6KOap3oNyLPpfBYtlj_FEtLRFuCEdfSRj7f3ithH2PS0zjIaSbIe3HpTqKdidvvXiPUi1GWgVF-jX-fKLPgyz8Dk5MT2DZn8DCmUhccUAKDfaXRXdgbJO51zUMlLCrBaUY9UCvNyuao997Y4x5xImC1Rx7Nut_jBKOAalDLukXiV8EO93IKagcZ1OE6YvDEZr0JvDfpQ8I_6xdogOC72TeDoyzqAigfU4ie6hVvf6k1KJ4hOyrKrbGrx95K1yxy97jnLfMjdaQNB_O8NK9-tQ0FG4Wq1M5nGftAl27g4pjmmse5eLqzoxdYBP3MCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ننگ بر آنکه خواسته شمر به ما کمک کند #ایران_من
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/656588" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656587">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
افزایش ۲۱ درصدی کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد ‌
🔹
بر اساس این ابلاغیه، نرخ‌های جدید شامل تمامی مسیر‌ها و ناوگان مسافری اعم از اتوبوس، میدل‌باس، مینی‌بوس، ون و سواری کرایه خواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/656587" target="_blank">📅 13:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656586">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
حمله پهپادی و موشکی به بحرین
🔹
منابع خبری امروز (شنبه) از وقوع انفجارهایی در بحرین خبر دادند.
🔹
وزارت دفاع بحرین اعلام کرد این کشور هدف حمله سه موشک و چندین پهپاد قرار گرفته است.
🔹
تاکنون جزئیات بیشتری درباره ماهیت این حمله، منشأ آن و خسارات یا تلفات احتمالی منتشر نشده است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656586" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656585">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تیزر قسمت هشتم از فصل چهارم
🔹
در این قسمت روایت ۲ تجربه نزدیک به مرگ سرکار خانم فاطمه سجادی که به خاطر مسائلی در زندگی از دنیا دل بریده و در شبی که ماه کامل می شود روح از بدن جدا شده و به آسمان بیکران رفته و تجربیاتی را از عالم غیر ماده را درک می کند را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: فاطمه سجادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/656585" target="_blank">📅 13:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656583">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_fa5nLg9eTlh1yy2Y1YSqU39B61XWyd2mE8Qlk_63JEVxotxSv217PfZhNslZm9N2r1xZBbzG2X-AefPXHkgFCS_wNYEH5yYDQ6VjCL4zrVwTEZyWpt87VAp56OsMITfEEto2TBbqiUDEnBnl4OWcq230CdueMPzkCNMithHAG40RxKv3OWvqcZOiBr0m3wPBDKn_rxvt8diToEK8YsGKjqijh0G-Ily_jfhvavGZSRrAI7l6Y32FZHThIH_lCawUwU8nRPB046QkBuO0sAVhlQfc2snvTPAZgtl7hQAH1ue-e7zfYG2ruXzb3oMm6bHhZeX1ILJxtEjIl7bcTdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نصف حقابه ایران از طالبان نقد شد
🔹
۴۱۷ میلیون مترمکعب آب از افغانستان به چاه‌نیمه‌های ایران رسیده که کمتر از نصف حقابه سالانه است. طبق معاهده هیرمند (۱۳۵۳)، در سال‌های نرمال باید ۸۵۰ میلیون مترمکعب آب تحویل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/656583" target="_blank">📅 13:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJpZRQ7c0XPzc7tFYtHA2Tn9g_ri4usS6dX1ySrDau49suLd6Jk6HzlwV_MHSd2Ng0YLVS0eX3OIOf4C-ABNjFwP0dSyLXJp5hf0ZWD3Cef7ZOs8xLHRl9zaTHFqH6yF22rlZLIlMRQ_t1NP-8bXcmEazEOfLv6BsAmg3coJEuGe5xbkpxQumsjB50QQCJ-0tQjJ47Arl_ESyGXBYoMhD6bRV8bC89nXz1EbV6HFbhazctZiQBRosCU2D0e4DpKHPeOfuipHdReJt-sueXjqlzkjQcQ5scFid63Z5sDTbt12IrK2Z_9v2LXGRFIGg9qCHDiapPtXQXFB_IWydjsq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
بانک اقتصادنوین در جمع سالم‌ترین بانک‌های کشور
🔸
بررسی شاخص بین‌المللی CAMELS، معتبرترین مدل سنجش سلامت و پایداری بانک‌ها، نشان می‌دهد بانک اقتصادنوین موفق شده رتبه سوم بانک‌های بورسی کشور را از منظر سلامت مالی کسب کند.
🔸
این موفقیت بیانگر عملکرد فوق‌العاده بانک در حوزه مدیریت سرمایه، کنترل ریسک و تقویت ثبات مالی است.
🔸
همچنین نسبت کفایت سرمایه بانک اقتصادنوین به ۱۰.۵۵ درصد رسیده؛ رقمی بالاتر از حداقل استاندارد ۸ درصدی بانک مرکزی.
🔸
قرار گرفتن اقتصادنوین در میان سه بانک برتر کشور بر اساس شاخص CAMELS، نشان‌دهنده پیشروی این بانک در مسیر استانداردهای نوین بانکداری و تقویت اعتماد سپرده‌گذاران، سهامداران و فعالان بازار سرمایه است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/656582" target="_blank">📅 13:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پرونده اختلاس ۳۰۰۰ میلیاردی به کجا رسید؟
معاون قوه قضائیه:
🔹
تمام مبالغ و جرائم پرونده به خزانه دولت بازگشته، چند حکم اعدام و زندان‌های طولانی صادر شده و همه متهمان به جز محمود خاوری که فرار کرده، دستگیر و مجازات شده‌اند./ باشگاه خبرنگاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/656581" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آخرین وضعیت ۲ دختر سنندجی که در توالت حبس شده بودند
سلمان حسینی، رییس اورژانس اجتماعی کشور در
#گفتگو
با خبر فوری:
🔹
همکاران ما در سنندج به محض اطلاع از این قضیه از طریق همکاران محترم‌مان در فراجا مداخلات تخصصی لازم را انجام دادند. درحال حاضر خواهر بزرگتر بابت انجام کارهای درمانی در بیمارستان است و خواهر کوچکتر در یکی از مراکز بهزیستی است.
🔹
در خصوص واگذاری این دو کودک به مادر خود، بعد از بررسی‌های مددکاری و روانشناختی این روند طی می‌شود و بر اساس قوانین مربوطه اقدام لازم صورت می‌گیرد. درحال حاضر روند واگذاری سرپرستی این دو کودک به مادر خود مشخص نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/656580" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656578">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c900f1da4e.mp4?token=LDFTfNw7q5sVxrNbWvNMM_TU89OH3w2iup22YZiRbURjqXGll6juZvjXcOO-aZCtk3kZjGjw8raoz4rZBNwqbdpG1RXKESkFt0GtnWB2LlwSJAyp0wG8CT45WhSQTbSZt33Ve81keFAS4oIXscR5a-j3WuoptrjS61LzTtygga8GX_IFpIhxEeGwimPCY79DeMpOgxnB7CkDd1blX1dztLvDJpoEhLbjSHDOD7krFF1Nrwe8FheDLqtIRv9zFcrsTPFeLsoZRzDKhECD7QlLeCmN_6m2MhJfcMTD6g7nR5U1CUu70MOJf5N9OO6EYsRayRhgkHwph705P49xl5TLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c900f1da4e.mp4?token=LDFTfNw7q5sVxrNbWvNMM_TU89OH3w2iup22YZiRbURjqXGll6juZvjXcOO-aZCtk3kZjGjw8raoz4rZBNwqbdpG1RXKESkFt0GtnWB2LlwSJAyp0wG8CT45WhSQTbSZt33Ve81keFAS4oIXscR5a-j3WuoptrjS61LzTtygga8GX_IFpIhxEeGwimPCY79DeMpOgxnB7CkDd1blX1dztLvDJpoEhLbjSHDOD7krFF1Nrwe8FheDLqtIRv9zFcrsTPFeLsoZRzDKhECD7QlLeCmN_6m2MhJfcMTD6g7nR5U1CUu70MOJf5N9OO6EYsRayRhgkHwph705P49xl5TLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لازانیا با سس بشامل
🔹
لازانیا یک غذای خوشمزه و دل‌چسب است که با لایه‌های نرم و سس بشامل خامه‌ای، همراه با مواد گوشتی و قارچ، تجربه‌ای لذیذ را برای شما به ارمغان می‌آورد.
🔹
این دستور می‌تواند دل هر کسی را به دست بیاورد و عاشق لازانیا شود!
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/656578" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656576">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
مرغ تازه؛ کیلویی ۳۵۰ هزار تومان
🔹
قیمت مرغ تازه در میادین و بازارهای میوه و تره بار، بسته‌بندی کیسه‌ای( پوشش کیسه نایلونی) کیلویی ۳۵۰ هزار تومان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/656576" target="_blank">📅 12:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656575">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
جزئیاتی از عدم صدور روادید آمریکا  ‌
🔹
تیم ملی فوتبال امروز  اردوی خود را در کشور مکزیک برپا می‌کند. نفراتی چون مهدی محمدنبی مدیر تیم، هدایت ممبینی دبیرکل فدراسیون فوتبال، مهدی خراطی مدیر اجرایی تیم ملی، محسن معتمدکیا مدیر رسانه‌ای تیم ملی، سیامک قلیچ‌خانی…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/656575" target="_blank">📅 12:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d02ANTVTQhulN7Z2-ZJsgfDIHdQ9bdS2SQ9t2TWSnmV4NdtUF0HsgTNKhQ_EJANxMqnSfxCDDCDAJoC6RgswaombiUPYZzKPoVPQ7d3GQn52Ote0gVg_HMndYIvXOHmYZQ4o7m2b64u-ZXxB9G_FTl-BGkHkdB3FsBcaiugxFvytPX1d39EGAyZq0BYj6vYKuM4rhh4DJlwONz_hfY7LAMKGOK4q3YHNi8HJBqowaTGT9-bJwUL5ahIRb4rTBB3w1Zp2C_iXaIu4n44VHxqhM1ErXAw0E4zBeVXeH1OjCktnDc6QW8nu-901svV3q-o2cBpKKfrfIpbjc5XfhoiGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWE9UBw7pf2wXBSi6WC1Ra_zGTSfd5whsuMxjUqnIb_3Nj4fiYcATsjWAnjJ6B4_dauLr6-Iy_-4BOimk5H_hAAuBslhHNOQLQgyLamr0HqivhWu7cJfOXrlpkKpeu4tjxDAtcW46S8FyXeP-gqXbkxevw8WG4_UVWjXJsJDqntt5QOyAQugzAEjJRpaeTB2AvqgQRddyIgSgbsVMqLRKGgTEzyAsdqVEixTrByx_SfyRPgzBKkRVQ3j9pZEVL88REPluSUi8p2NJH5PEHxPzah3m3uqtcr8Zrmy-7rucMepKXRL8KX1pU9cKk-Qe8GvW48TeoTyt3Qb9RwDjTx2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSip88rGOfLB6gGkBKQoqYP2zI_aWqO9pGhG5BujL__yptHeCZYM2H2DcvtZn2j-DbzQ1AikO55QfTUMxVObpYZaqzbIedbNUpIZWuoWASwTpqx7RVBcCoJRMo7Qmh1U_pgFIADpwkcO_wC_S1-aHqfb_qk39mEkrTRfstSlaIKzL8T4BonT5njJher3oWsZqY1AacDfch8CSuHOeyvV1eejJHXzYjckta1q0cTITLNsLrldNbeY6iRN7UBvEyMc-5RK6XFREJ_K6tpgAUUfeRToqFZJXMdI-gdpxfy_08I3j36A_gpLyxdCO7ZJVYCaPqZKdV_QeWOAVnCwRmzcrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pb6dbXJ1LRfJN2uoZIuhECzIsyi8W7jaEBUplv0tjMRimxq0e3m5GehuHz95gIiT9ogo-ODyychBFvyltwU_1LNTEftkP1PSPRMqYw8HqE6RNgZYDYOD98zHk2eeCZknIW0F2slJacLoTwBrmg6sAUij4vrCMHcQ_ZtewtIbsESyNmQ_bBO7I8rYkm_HREQTcNynmSu-wOGTVxj33_4b_YXkSEEzyqFgjj2oE5vlYVsIRvCihI5RAyDL9mNcI_UlTVY6t35W9EaPT7HiOA_IovxVuxKKD0ardoSxWvYagef9tDZf5fyPZa5DzRGMXYHv-teDuJnec13iFaQcnKWUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMx1agkVi7HBHNem6J-wijh364qMKF6GXhwb0Da-2AhI4I1rTc4EsYUIDP9rS80wveqUC_8QXi2ykdQGo6xLT3AwlbbBYbNxjdqK973_y1hf9FwXIP1X7SmV_3b6ItPtyHyUlKqScbVxPrKRRd7rEiMPTEJ4uG5MqA0gFkQh1tJZBXlK7IZBSnpRivFiPBxdll2kEIxHuRJW-Mqss6xK3JSJ705MVe3bDXNgnNipYZJTgi_15POChzipaZYer353eKRgpigfFHTy2IczBF-z02D9OHyqvhCrcidau_cKeukayx3FeHTswEx5USM0fXLY9lmOxAy14qA_Th5zaHHzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Izush-WdesCrA9O4t4ous2j2xVopR1qVCKaR0ph5P54aplbca_4YYdDyCPStdalMQhxU-nIgrOJtLdlkutq5jIT-fQtcy6bLSI9szs1oKTIi90UPKTHvywmxEEf_x7jvJOE0Jh9UVbO_V6_3tI7S9i1zJBqVA_LkKKQw3hEEfUERweRolIsVxcR-f9CvJIhzmCdb-diQxnMzieQ76icYdvsw8r5WGnNPb3KiKjBrRfowTIuvGTz1s_YPE3XK0yhQ9aVSMRZQoF9_AkxHBhrJLLhWOU4_P1n7g-MGgJmi7iLdgftNbfX3E3gLdOZFOV2aj6gbhY-NkTmbq4czNW91CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0idAplGzm_5ggMwqG0CbDM_UUGVloJL9R48P-iCRAQYuj9rquxrmatOp_KC2MMDGxt9Grz4SCyxpO3x9KZX4Dtk_pz9MAa8q3JyH3qm0AFCI67MjhYiMw3pjEwBLjHcjAL9IT2wenC5veJA1wAlz0jgEDM605H2oq1eNuYlnFYh0h-KMSAskd2CFsw1lgmcfYNXXK42rJD7HuiaE2Ae16pzeJTdp6HGfN4pObU-J_l1s48vvzna71hrONpep14pEHJoWXge5a1BGw8h9Q9pFGllt6VHKbbTO2RtJ7H_-KNOfAXgMAPgAIqlMQ_GBQZBvx80QVBlCVLl-bzeZMckxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مردمی «ایران سبز»
🔹
به مناسبت روز محیط زیست، مخاطبان خبرفوری با ارسال تصاویر اقدامات محیط‌زیستی خود، از کاشت نهال و پاکسازی طبیعت گرفته تا تفکیک زباله و صرفه‌جویی در مصرف منابع، در این حرکت مردمی همراه شدند.
#ایران_سبز
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/656568" target="_blank">📅 12:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM3-J4kjSjzStNCIQg1EmrLaoUnR8kgpNtuqVSibW7jPKUBuuE5Azwr6jVV6Zv9I-j7SNNSxuAAsskWd5ZUM3ASI6zHKzgYYedx0QkioIpE-sFWb7iuAhNYUVG8rYkrFNURriJDGYYnZhPfKsMPj_g0FGpqP-Ky7ZXzduG2PJrmklyYMyGKWaj8wgir7IZsK5CZClWXJMi4AWR9U5CPmkuqETeIEgroLzJcnJ2ky4QrzrobT99wPjAd6pZhNus4OdDomn7RAxQgxSfe1Ey2Q39BZ0t9wf__JZXUEYWrqiGShy7yHgOX_kdD3KAZ1jMtm3R3RwEMqlvmK8klnJ0XcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ فرزندآوری در افغانستان ۳ برابر ایران است!
🔹
داده‌های چشم‌انداز جمعیت جهان سازمان ملل نشان می‌دهد که ایران با ۱.۶۷ و آمریکا با ۱.۶۲ تولد به ازای هر زن تقریبا نرخ باروری مشابهی دارند. طبق این داده‌ها وضعیت چین، روسیه، آلمان و فرانسه بغرنج‌تر از ایران است.
🔹
در بین کشورهای همسایه ایران نرخ باروری در افغانستان ۴.۶۶، در عراق ۳.۱۷ و در پاکستان ۳.۵۰ است که برای ایران یک تهدید به شمار می‌رود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/656567" target="_blank">📅 12:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25e75fea.mp4?token=r8wGr7KgB6-o36F8BDSWMxATkEeeHlVRGU0dbsSrzzuvfx_ZKkmG7xOyhqdnUYKVF5gXJGAAVEzw-Lbhe1z2lBp0o_MiNNNzUAlRMO2u2PvR_zaFsdsZPj1ADWJ5FjaqgnDRO60FgA5EJnSuEBoSEg2xK0_yf6WG3OWldQCKtRKKR9t4UFMiMO-hz4QK7FydMhWNRt9686elf412D10yPitcwoJmZAKfBtHgoTkss7kBltghUi2Dx5PzdWqAbEz4fvU8YbcUMMLpVdXeBYszJlWOpl66Xp4h1QA5H7QxahiBIFLwJaouK9G6fww146SLKzi3f2KJR9JnTJNjcv8UzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25e75fea.mp4?token=r8wGr7KgB6-o36F8BDSWMxATkEeeHlVRGU0dbsSrzzuvfx_ZKkmG7xOyhqdnUYKVF5gXJGAAVEzw-Lbhe1z2lBp0o_MiNNNzUAlRMO2u2PvR_zaFsdsZPj1ADWJ5FjaqgnDRO60FgA5EJnSuEBoSEg2xK0_yf6WG3OWldQCKtRKKR9t4UFMiMO-hz4QK7FydMhWNRt9686elf412D10yPitcwoJmZAKfBtHgoTkss7kBltghUi2Dx5PzdWqAbEz4fvU8YbcUMMLpVdXeBYszJlWOpl66Xp4h1QA5H7QxahiBIFLwJaouK9G6fww146SLKzi3f2KJR9JnTJNjcv8UzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو جنجالی نظامی صهیونیست از کودکان بازداشت‌شده فلسطینی
🔹
انتشار ویدئویی توسط یک نظامی رژیم صهیونیستی که در آن گروهی از کودکان فلسطینی بازداشت‌شده با دست‌بند و چشم‌بند دیده می‌شوند، موجی از واکنش‌ها و انتقادها را در پی داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/656566" target="_blank">📅 12:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
منبع آگاه: وزیر کشور پاکستان امروز به تهران سفر می‌کند
/ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/656565" target="_blank">📅 12:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ آستان قدس برای تخریب آثار ملی و تاریخی مجوز گرفته!
احسان عظیمی راد، نماینده مردم مشهد در مجلس در
#گفتگو
با خبرفوری:
🔹
مدیر کل میراث فرهنگی خراسان رضوی عنوان کرد که آستان قدس از دیوان عدالت اداری مجوز گرفته و فضای انتهای خیابان نخ‌ریسی را که جزو آثار ملی و تاریخی ما بوده را از ثبت خارج کرده است و بدون مجوز شهرداری آنجا سه تا چهار مغازه تجاری ایجاد کرده اند.
🔹
این موضوع اگر بخواهد در سطح شهر مشهد یا کشور باب شود عملا آثار تاریخی،فرهنگی و ملی ما یک به یک از بین می رود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/656564" target="_blank">📅 12:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXH0zOA1--zrqJPpZv_rDDicKGrEifX12A7XnpICAJvE2aMipCgbfgFZz2VUI5vq7s1nkeamG_N_nz33IKSCm0FANCV2qvtPvVVs-X88Heq6VjlAmZs1zhRoQ09fkPbrBP_klj_AFsa-vr1YsSMYfMS7eMJVh92_0ghV3aqfc8J66rIcrufmd3v65dkYWQgyX92DbR4orKj1XLBx3ug6fe-F9v5kHcLze2Kbj2sRJFK8A_RL0i4FgiXGl5NEz3nGGLT4wIb9JJfLM7YdPbiRV8DU0CdzRop8sFoiSUNAoDoRWM-H1h9HOIu9jfHC7xJ5j54P_XrmS22Zvc255HBPgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام وزیرخارجه خطاب به رئیس جمهور لبنان: لبنان را از دست دشمن واقعی خود نجات دهید   وزیر خارجه:
🔹
بر اساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی ها را آواره کرده و کشور او را روزانه بمباران می کند.
🔹
اگر لبنان…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656563" target="_blank">📅 12:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw_uJts8jW4Wk6B2OUgcYQ8Vf0fSJVj6tCNxbwA0lcRKIhTx5fQgbbuZmxFq-ikIwDKJ1PDUArLTq_2U1KCg3pDID0WkqdFJgEETIYFtbgCsysFKE18JjJml_seUNrXmE4qBtExBIj2rnLxhdZ2CxLnUobgPd66UPRJLNEVQkbCllHpwlLsBIzHBb4vlp40RkqMe89ubf5RnqgP82EZ-oHppI6NS0Jj9oBbrjK-Mhw4XwEGBAYZE_B6qADokNWz3Eo31Tbf91OvN-h_vawLp5RX44GAaMqzWKR84hu8u9xqRZsTziq65Ki33I1Y3f1062_EnxfhTcC6suOKjW_oFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه‌های جلوگیری از بازنشر اطلاعات غلط #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/656562" target="_blank">📅 12:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb1072b44.mp4?token=TXTDV4VI3L3IhSy-vJtLxZQPf7zPTbPg489vIbfa-i299zf4Hbm-84fGcjDsfjbgEkV7-IYmYl7Xf-5EOijvaj4NsQEW_ac8TyQ_Q5Q6INdki_Y4-pHOQxui9hyTsZhQYWF2ZGdovx3gp1bSjAha476q3JQHqbGn4IsV3SmwKz54uIjXXvGlGKZa41UOubkv9WBjooN9PG7T4jo4Z689MVTB1kvJY5uuruK5irhj1KTD1pxdxtpWWcxYyLqkvdovQWQGJe-_w6oeES7OW3QX4-8riDVXeImBaHZuYPB5ZrqAW7PrkC56i4fSuPkE9B44umN6IisOOFHwfijhwGKanQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb1072b44.mp4?token=TXTDV4VI3L3IhSy-vJtLxZQPf7zPTbPg489vIbfa-i299zf4Hbm-84fGcjDsfjbgEkV7-IYmYl7Xf-5EOijvaj4NsQEW_ac8TyQ_Q5Q6INdki_Y4-pHOQxui9hyTsZhQYWF2ZGdovx3gp1bSjAha476q3JQHqbGn4IsV3SmwKz54uIjXXvGlGKZa41UOubkv9WBjooN9PG7T4jo4Z689MVTB1kvJY5uuruK5irhj1KTD1pxdxtpWWcxYyLqkvdovQWQGJe-_w6oeES7OW3QX4-8riDVXeImBaHZuYPB5ZrqAW7PrkC56i4fSuPkE9B44umN6IisOOFHwfijhwGKanQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین فروشگاه دیجیتال همراه اول در تهران افتتاح شد
🔹
همراه اول از نخستین فروشگاه دیجیتال خود در تهران رونمایی کرد، مرکزی که برای نخستین بار امکان دریافت بخشی از خدمات اپراتوری را به‌صورت ۲۴ ساعته و هفت روز هفته فراهم می‌کند.
🔹
این مرکز که در محدوده ونک راه‌اندازی شده، با بهره‌گیری از کیوسک‌های هوشمند خدمات مشترکان، مراجعه حضوری را سریع‌تر و ساده‌تر کرده است. توسعه این مراکز بخشی از برنامه حرکت به سمت خدمات هوشمند، منعطف و مشتری‌محور است؛ مسیری که می‌تواند شکل دریافت خدمات اپراتوری را برای مشترکان تغییر دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/656561" target="_blank">📅 11:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcoVn51G5pIsHQZtqushZZLyJcumRpj_AhsV3fkFum_vTUsTaB1acQYj23vNKUFeKoxZsTUEWOdRdtfZjQvMX9f-03wPkkmjnohvLroeenL-hNxBFhlmY3naLnsORsniOpIkXTLrO9pDYvGsXcwXZnyCXjP93gvzUbI60f6b5S0nGiK1gttcqFX-lvRSJ3sjxsdlNvNk6YO8Il52L6GIKdkZmetfyoXoDOrMMf-miK09-QEJbq25hytrqzjZCzXeWPlw5pnMFDp3ZR37kY303t6CVUrtl5KG7rmNGHZaCWy9e9lxCFVA7jQzsPTgEBF_OdD_oVLFF6d0G_S3gpZc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدف طاهریان به ایران بازگشت
‌
🔹
صدف طاهریان، بازیگر سابق سینما و تلویزیون که سال‌ها پیش از ایران مهاجرت کرده بود، با انتشار یک استوری در فضای مجازی از بازگشت خود به کشور خبر داد.
‌
🔹
او تمامی پست‌های صفحه اینستاگرام خود را آرشیو و از دسترس خارج کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/656559" target="_blank">📅 11:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62d3deebb1.mp4?token=QNgmk9KKv2Miov8vysbwED_rSxlrzxGV88cmNkHqZBv_Kshrj12FPvS8KbJ51sqyN8Jyth-CAWWKpf9VW1mWDcoFNZbY8OpE385mS3M4Mq6PWY0uN1d0WX_pDCxH_vDPOSFgOx3t67_rPy760OQSi7s1dRB80T2jULN-UheK9CsFA3m2xYpGtZ5okBFtUm_3vgzpX4sTKCS33DJ3URpg12W68FeNMbDhEl0K1p-Wcw5jxduOeiWmhgWSoKhiq5kMJ1N1UDoTSWhz90myx3yxZo9NaChanvAiIVhBBD9dFo3UN0SMkS7MF62lcvUvUw7BGe82hstPm2JzrsziU0xLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62d3deebb1.mp4?token=QNgmk9KKv2Miov8vysbwED_rSxlrzxGV88cmNkHqZBv_Kshrj12FPvS8KbJ51sqyN8Jyth-CAWWKpf9VW1mWDcoFNZbY8OpE385mS3M4Mq6PWY0uN1d0WX_pDCxH_vDPOSFgOx3t67_rPy760OQSi7s1dRB80T2jULN-UheK9CsFA3m2xYpGtZ5okBFtUm_3vgzpX4sTKCS33DJ3URpg12W68FeNMbDhEl0K1p-Wcw5jxduOeiWmhgWSoKhiq5kMJ1N1UDoTSWhz90myx3yxZo9NaChanvAiIVhBBD9dFo3UN0SMkS7MF62lcvUvUw7BGe82hstPm2JzrsziU0xLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرباز اسرائیلی: با حشیش ترس از مرگ در جنگ را فراموش می‌کنم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656558" target="_blank">📅 11:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3ad089cb.mp4?token=r9m6-mQlWtKgf1i73AXSaTkSuKsB0X_eQ9UP0Gc1zqwuP0QJwo4UzMvJ7vq0hIpR3UjQJuageM38Naeh3R6Ueexfd0GMUUU3FeP_UbSeTAHMiireNyzXJe82iKmVeprSY2nFo16WGA_KKtu-hg_gNP9h-W8M2aBBW_7AY4SlWTu68m8bauxwISKO8SBT1mhehN8VukiiKdgaaklv_GIjrDo9MTrHFAdyKuIEmzKMGDHMOQ2av7gZlU50BPXSF9JHfT69u5eBBP2FH1y6gf3yLrDpyNYcTkIh9u9yMoH1Mx0BjsyqXN-p_1WtnQjAMhXonK3lz9mPsK7jnZRJvmYd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3ad089cb.mp4?token=r9m6-mQlWtKgf1i73AXSaTkSuKsB0X_eQ9UP0Gc1zqwuP0QJwo4UzMvJ7vq0hIpR3UjQJuageM38Naeh3R6Ueexfd0GMUUU3FeP_UbSeTAHMiireNyzXJe82iKmVeprSY2nFo16WGA_KKtu-hg_gNP9h-W8M2aBBW_7AY4SlWTu68m8bauxwISKO8SBT1mhehN8VukiiKdgaaklv_GIjrDo9MTrHFAdyKuIEmzKMGDHMOQ2av7gZlU50BPXSF9JHfT69u5eBBP2FH1y6gf3yLrDpyNYcTkIh9u9yMoH1Mx0BjsyqXN-p_1WtnQjAMhXonK3lz9mPsK7jnZRJvmYd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تست نمایش پهپادی در استادیوم آزتکا برای دیدار افتتاحیه جام جهانی ۲٠۲۶ که قرار است بین مکزیک و آفریقای جنوبی برگزار شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/656557" target="_blank">📅 11:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e22e3e9e36.mp4?token=Rkkut4CmOWFLYtw7sOyO0n5k9K6mO0LAXURXqihbh7YspRZTPAk-GUHmgEO99VOfzuDsDKZ3kC7g75nUVM3hJyUkwoNNcHDfNH0LjMYBMt8ncyQiheFsuHru6LQxtkwnE4a518v6fT0oZQE6FxjVJDW7K5F_LS_pl0ezUfS9hMIdgBXZmHhEabU1a6NebCyYbFoEA43snvkLobEQlKCsxpNCizSlxhxqrw6ff_FTHXGNOT3YPjdZBkYIekW-n9n9Pcx5sqZQdMAPcSQdFJtdUD38WL_7xt-HfZqYf53UV-7ZWDgKy7WPOFWDfjQqaJGqxYD_5EcKY5xl5JfOaq4oRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e22e3e9e36.mp4?token=Rkkut4CmOWFLYtw7sOyO0n5k9K6mO0LAXURXqihbh7YspRZTPAk-GUHmgEO99VOfzuDsDKZ3kC7g75nUVM3hJyUkwoNNcHDfNH0LjMYBMt8ncyQiheFsuHru6LQxtkwnE4a518v6fT0oZQE6FxjVJDW7K5F_LS_pl0ezUfS9hMIdgBXZmHhEabU1a6NebCyYbFoEA43snvkLobEQlKCsxpNCizSlxhxqrw6ff_FTHXGNOT3YPjdZBkYIekW-n9n9Pcx5sqZQdMAPcSQdFJtdUD38WL_7xt-HfZqYf53UV-7ZWDgKy7WPOFWDfjQqaJGqxYD_5EcKY5xl5JfOaq4oRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی از هدف قرار گرفتن دو پایگاه هوایی آمریکا در کویت به نام‌های علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/656555" target="_blank">📅 11:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
جزئیات وام مسکن برای خانواده‌های دارای فرزند یا بدون فرزند
بانک مرکزی:
🔹
مبلغ قابل پرداخت تسهیلات به متقاضیان برای خانواده‌هایی که از سال ۱۳۹۹ به بعد صاحب دو فرزند شده یا می‌شوند، به هر خانواده به میزان ۴۰۰ میلیون تومان.
🔹
خانواده‌هایی که از سال ۱۳۹۹ به بعد صاحب یک فرزند شده یا می‌شوند ۳۳۰ میلیون تومان.
🔹
خانواده‌های دو نفره (زوج و زوجه) که تاریخ عقدشان از سال ۱۳۹۹ به بعد است ۲۱۰ میلیون تومان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/656554" target="_blank">📅 10:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-O5_mPBbaSV5mYri5fmx4YpzAyux4l0-cUDiuOEPHBL2Z728PkGtAI1tdZ5k4guFdkeQBzor3lE-pOYVfuI0BasxC7zq2ILZq0OYd0p1k3xhpWvGygyq5w0V535DXMDJ1_CzsKf5_y1j4ZhZhcl4NeFXvPZl0wy1fyCX42O_wMjaA6vWBQfXfsadla59VYB19oTM2Cqss1fvpH3B9PzhoAyv8RsDBEdNIN8NKK2ppic9Nnk8Go1F3wVsyAiF9vpz7AoSJ9XcE4ZeGt-wtjZU2-5NBDUYQMRJkYEYRKipsx4L5i86r5nxWbWKdLPGf150P1g1EPEEdXtNYYmp6djLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسوایی جدید در آمریکا؛ بازداشت ۸ ساعته مهاجم تیم ملی عراق در فرودگاه شیکاگو
🔹
ایمن حسین، مهاجم تیم ملی عراق، پس از ورود به فرودگاه آمریکا حدود ۸ ساعت در بازداشت موقت قرار گرفت و پس از بررسی‌های لازم اجازه خروج پیدا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/656553" target="_blank">📅 10:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
درگیری مرزی در زابل؛ ۶ تروریست به هلاکت رسیدند
فرمانده مرزبانی:
🔹
یک تیم تروریستی که قصد نفوذ و حمله به مقرهای مرزبانی در هنگ مرزی زابل را داشت، با مرزبانان درگیر شد.
🔹
در این درگیری سنگین، ۶ عضو گروهک کشته شدند و ۲ قبضه کلت کمری به همراه مهمات از محل کشف و ضبط شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
@akhbar_sob</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/656552" target="_blank">📅 10:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln43OpHMZiU73JDteOW8OKRK1JSd5F5mjNWf1TGNYVesp3xDrUQgLnlCCvCSnvnHT3d2RlKjRjGRyZW5ETs9UTDKcyGwRRBSUjVVnULrr8wd0p-EcS99aBufSRCq30fJ-Fpeg_FwtfDYrm2dYnBrytI-d6Na2hoxBFnaNtfyIPWREq1BdWqJLhc4TB6Hc-QpPpd4OPxU2NUoidgY3g5ZUHjsauYQXjzKAYu1TjwR6s-ORxJED0MmFXxA4Gd04OUIF2wXtAc8ylLgy8ny6QRqRKeagW8mSDM7SzqbdU1jVHTWJMv0ntIw4EzKvurTUYsj1ha35eImW-yU-rW_kNJF8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۲۱ درصدی کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد ‌
🔹
بر اساس این ابلاغیه، نرخ‌های جدید شامل تمامی مسیر‌ها و ناوگان مسافری اعم از اتوبوس، میدل‌باس، مینی‌بوس، ون و سواری کرایه خواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656551" target="_blank">📅 10:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844fd8ea2e.mp4?token=M2-FWl-4WyPTmnspDZG5EvDQm2bD-l-Q5OVcx0lrOX0i4RGTvlx-qsKm3TLwcwQeh3VLwObXymHZH1S9BAMiCioWWG1i1pKn-kOgicE20sDdA1z9Y2SD-tjEDc3oXwcFFiNaU8nEWe_EwVsIBHJlMTPrvwa8SrJFGqhLm400ZKs3vynfZVptzSZo7uCX0K2K2bdzqUsp1fX4HcZoCPpYXhPirO9kFIdO3Nw7uMCRWnCORU3YGv1DRygtZvMoAWYEOygzb7eC9LEo5mgq6A8IAVMeVtwPWFjtnoqyha6zExxiZKTxUrok-pvuf_CQKARy0z9UL9bkrLD6r4cPbhVKxIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844fd8ea2e.mp4?token=M2-FWl-4WyPTmnspDZG5EvDQm2bD-l-Q5OVcx0lrOX0i4RGTvlx-qsKm3TLwcwQeh3VLwObXymHZH1S9BAMiCioWWG1i1pKn-kOgicE20sDdA1z9Y2SD-tjEDc3oXwcFFiNaU8nEWe_EwVsIBHJlMTPrvwa8SrJFGqhLm400ZKs3vynfZVptzSZo7uCX0K2K2bdzqUsp1fX4HcZoCPpYXhPirO9kFIdO3Nw7uMCRWnCORU3YGv1DRygtZvMoAWYEOygzb7eC9LEo5mgq6A8IAVMeVtwPWFjtnoqyha6zExxiZKTxUrok-pvuf_CQKARy0z9UL9bkrLD6r4cPbhVKxIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سنتکام: اهدافی را در سیریک و قشم بمباران کردیم
🔹
فرماندهی مرکزی ارتش تروریستی آمریکا در غرب آسیا مدعی شد که به اهدافی در جزایر گوروک (سیریک) و قشم حمله کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/656550" target="_blank">📅 10:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656548">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
قاسم الاعرجی: ادعای پرداخت هزینه از سوی عراق برای عبور از تنگه هرمز صحت ندارد
قاسم الاعرجی، مشاور امنیت ملی عراق:
🔹
ایران پیش‌تر اعلام کرده است که عراق از اقدامات مربوط به عبور از تنگه هرمز مستثنا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656548" target="_blank">📅 10:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656547">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0Q6-YZWJLptnzvME9mDlxtWtB2ds_dP2B1CyRm1QqHeczxbJBbw6j63E6cnMb-gz8GGUxD5L3P8UUq49LpGls0JXp_HvmPhKGknyMpABuhCLct1zT8YT5ocpeGCASFnSdqIm-CwVEvnuSWsfEupkWKNm0GxlP1MFr02GuXI2qRMJjJrBqJUioYg2hLjCltVu1Ru5oT78K8zJ1__1y3T5eUzLkS_-wlaEzPKq0wL5ucVZ7royI9QMQfgiQ9B4-1Hgeof8L8zkhLIOVpCWWENKLuMaGkOXOOhLtyNQ1b_gkQSVSls8l4zk98YcfpSoZKtGc_8ChvO7jKjSEkA0oGIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابرت پیپ: ایران ویتنام ترامپ است
استاد دانشگاه شیکاگو و از تحلیلگران شناخته‌شده مسائل جنگ و امنیت:
🔹
ایران خواستار پیش‌پرداخت ۲۴ میلیارد دلاری است و بر تنگه هرمز تسلط دارد؛ آمریکا یا باید این مطالبات را بپذیرد یا تنش را تشدید کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/656547" target="_blank">📅 10:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656546">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_tZLuVAn3OaoRI6r9e99PamN0bhOsDyV1nUJUmKwZJa-qYXy0GGNKPJGaZrU16CbpLWlbnVKWilIbEoTaTridDuMhlKP7PWUb23gcl7HyOE2kynx-WNPvdw4_G8ZojjMobO8Qa8TTV6zZT7QqWdWUz7sremc_EahkBikcMo0iZ4jbEbwqVJjvURwhqV-_hfTu1UOnVSQN_PNCNspys26I3zGH_hDXeID19e3DL6r3zIWUpakP29pOzyl4jy5vhh3ODImmkD8y0oHYskAARIh7MlorYaUqM793tRlNIHmpNIdt4ZSUXfub6Gz3yvQ_Hy3LDklLPzdSuDbLvjDsh2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر رئیس سنتکام به بحرین، قطر، کویت و اردن
‌
🔹
در حالی که پاسخ ایران به نقض آتش‌بس توسط آمریکا ادامه دارد، «برد کوپر» رئیس سنتکام با مقامات بحرین، قطر، کویت و اردن دیدار کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/656546" target="_blank">📅 10:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656545">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59c822300.mp4?token=aSbwnH06stMS59_8DQPSA_wFgrcZpXDHwHblQ-NJbav5JNosPKv_f-A8QVNiCP9l11SgfEN1Z0KAM3sjTAsMyLgilL_BooBr4VAEyTBodQKbOa3ofCPJ_sjFKtWHAAp1Ylrdnuc7R6QQ4a7z22DHxlvGpsr53m6sHhQOJhgV1eThpBg9hKGjHHPwSpCMlft2vHO7YGii6jsvkhZawJXqkQZuL15b9MT2tImH5vL7gwIxxDovmKVk64dfNrOoIZgnbsKjZlch8G0fh4nsIWgDDo3xEobpPUgBb3KpXlbhaJ6zaUVU1KIFewMEbebFPI4FQrqY70Bw9lLfDcZ-8kNHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59c822300.mp4?token=aSbwnH06stMS59_8DQPSA_wFgrcZpXDHwHblQ-NJbav5JNosPKv_f-A8QVNiCP9l11SgfEN1Z0KAM3sjTAsMyLgilL_BooBr4VAEyTBodQKbOa3ofCPJ_sjFKtWHAAp1Ylrdnuc7R6QQ4a7z22DHxlvGpsr53m6sHhQOJhgV1eThpBg9hKGjHHPwSpCMlft2vHO7YGii6jsvkhZawJXqkQZuL15b9MT2tImH5vL7gwIxxDovmKVk64dfNrOoIZgnbsKjZlch8G0fh4nsIWgDDo3xEobpPUgBb3KpXlbhaJ6zaUVU1KIFewMEbebFPI4FQrqY70Bw9lLfDcZ-8kNHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دخالت والدین در دعوای بچه‌ها چطور باید باشه؟
👩🏻‍⚖️
#سلامت_روان
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/656545" target="_blank">📅 10:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHI4wiqBWwR6EiGP9-sXHvXl9eE4tbVaHP6PZzRxXsEUJ_iZ0IblnW4xxeDwwTObyfO3YfIoG4PMtc9YpkogGi96ZzCXmBvsBLaAS5pw8s6bgrsKp7AIZeoFB8V-G4zfkoAysbgVEHseTwMmOe3Z2REky6DKzFoKFeykCwCiovkTqCwmF4e56iFhwv_RPbPUkEpe3p7EN995iUh8KUbH-MqwgPXTtzFNqkJwrVXUiFfjsgrG0BbShvEgR6RRW4p_JFtEWufZ3I-Tkmml2APk3PupaV98JrydClBL-NPiufqJPEC1x43rerrRi4khfqpOGJ5O-231xGQ26b2qiJZOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir
نوشهر
📍
۱۰۰۰ متر زمین
۳۰۰ متر بنا
تعداد خواب ۴
ویلاباغ مشجر و سرسبز
فول فرنیش وسایل برند
چشم انداز ابدی جنگل
سند تکبرگ و مجوز ساخت
دسترسی عالی تا مراکز تفریحی
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/656544" target="_blank">📅 10:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656542">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr63TPJ2W5j4U-uneu42KgpvJp3P2MWbYguYo55n2Qe2zKwS5TlKjPzxHQWgL1sL39_HIzBgEpQQliy1PpWe14Y18w4KhFy6LcehXJSjAx1rC4VZvCKiniOfAliX9HBz0Tb8JzcobR16mlk53MueCmw3t0yOlmlzwWkJENfgnAApP--bRFln2IRRVe7wy93m66Lw1zIqggbHdoqNY4l09z83sy6BsJAOoeuJL5P-cd1iWZF983t8lO1q7CFzoKIr-chDIEw4Eau3o9C_uyppRSk_NtewljnC9KYOQu-U6I864oB9cibIM1wTj5vJTpBlWfICWabjGVl-XL3n-tGaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی، مشاور رهبر انقلاب در امور بین‌الملل: معماری جدید هندسه قدرت برپایه تضعیف مقاومت قهرمان شکل نخواهد گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/656542" target="_blank">📅 09:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656541">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4853bdc25.mp4?token=bXXuZM2PO260yeWqCGqT545jKqJM71dL9DBVpFi1H1fM79Xog8erU7y6VBpXzUnpL1g9rnCnDSXUk7UqMxWpoLgmT7Z-lVHBPyBOTdxRU3ya0m-TirfG5HD8tc_4aKLzqAY69sqzvwDQQ_jgA-Ui83KuRMkquTRjUSqoMtbV9yUjqvbh9K6nVuZLF2_Xr-X3S9V-J-LVefjJxMmYu5NllnQpM8O83GVdqeohKTIXHVbHURGsFkBX2yzcCAcZx2WngQjaePq31ix2-zuldcpv3D0X_tvuqaNYiLUf23EtLg_P9HxEwE22lPL0XloSev74atv29pmtmOhb6MvjA0UksQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4853bdc25.mp4?token=bXXuZM2PO260yeWqCGqT545jKqJM71dL9DBVpFi1H1fM79Xog8erU7y6VBpXzUnpL1g9rnCnDSXUk7UqMxWpoLgmT7Z-lVHBPyBOTdxRU3ya0m-TirfG5HD8tc_4aKLzqAY69sqzvwDQQ_jgA-Ui83KuRMkquTRjUSqoMtbV9yUjqvbh9K6nVuZLF2_Xr-X3S9V-J-LVefjJxMmYu5NllnQpM8O83GVdqeohKTIXHVbHURGsFkBX2yzcCAcZx2WngQjaePq31ix2-zuldcpv3D0X_tvuqaNYiLUf23EtLg_P9HxEwE22lPL0XloSev74atv29pmtmOhb6MvjA0UksQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر کمتردیده شده از لحظه آماده سازی و پرتاب موشک‌های ایرانی به سمت سرزمین‌های اشغالی در روز اول جنگ ۱۲ روزه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/656541" target="_blank">📅 09:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656540">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ویدیوی زیبای نایکی در آستانه جام جهانی با حضور فوق ستاره‌های دنیای فوتبال
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/656540" target="_blank">📅 09:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656538">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
آموزش ‌و پروش: امتحانات نهایی پایه‌های ۱۱ و ۱۲ احتمالاً از ۱۳ تیر برگزار می‌شود و اجرای آن منوط به تأیید مراجع ذی‌صلاح است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/656538" target="_blank">📅 09:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656534">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IoyZqweEq1QaFt3yZ7wSr3XtdXxZF2QSCjypW7NXC_HVj-Jb5GaS6AmJBdHWZhbvBAmutYztk3V8BEAXyjVoS5QlK1fuRmmNbbZzzd2ee1K_HkJhlSFmxVTKSfauBupV3kZNfWvYeSjDUJYvkA0F1x_y8WW1-efMdnNdsSJVmNIzBiNs93aH9uhQU3Him5WXLLW0RHmr5QHxHpJSuml1pQnrVVLguPYBC_TFlMxqangu8Ue7ZudbF9BfYzoCP2xHayl8jcB-Gba2H7988l61odzQPXlEXt3ZrV0nO_3AheFbrqtUUB7-LXQFBxbu3IJQaDP4D1FBL7CKhyYqiGMOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS6HYhK4CFjZjFjVakVpM_0rKsH5LXAfStdan5bDH882TQElAgslLh3Ib8ETIkj6U42QBUK5NRpPNpgrt1EW6fw3TvchMGqxsfLCzMdvBEKjF-DaytSnFzyM7lb6eJ4a50A0IH3hFeoVsxEZVoJcDTZCQ_2M23JMZY9r2umhylgwRVApjDvQHWGC-ceLCbHg2bUhldUwu5yMp-drtdQ_QkNltRciRdb84i60TcJsuzXdyWaKwqGTMrMhcd3GaAkOLpao-fOR-T16PPukKyXkpju9eYUnOyg_7E_dEAVRU2Ll9hGo4GDtz5Qwa5dNE9gnVm3GHasZe_uEWXBRwYriEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sH5itBds6CTF6PhMe2XZL2WFm-MEnHks5RdIfdwt2bQlNIn5RzxoQLKPryYbJ4fpfELr38XlAxXl2015uTPTQfTndE2S_h6MzswJeFDPyB6ZkTGeVMpJRRKWR0jVCAnDIcWJCyTzgl22ZtveTQdAKX1EyY3VksE15l6csNYoZQBliJu9XDqePDgIjYQwSkXLP8pRpSSmdi_KTZ9uvU5sYki6gpRn5n8QLKcXnfAOnApo6odTVcWdqZkB330RyjRcfQvo-RBo4uSRmmYqiMPfQqJH3YD7B0bdhSbJFcG_-K3S9VpSX6wT7-4HRZ76tjN1fUxRwPXayyKH7LEtI6TKOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اقامت لاکچری خانواده نیمار در آمریکا برای جام جهانی!
🔹
برونا بیانکاردی، همسر نیمار، برای دوران جام جهانی یک عمارت لوکس در اورلاندو با اجاره ماهانه ۱۲۰ هزار دلار اجاره کرده است. این خانه ۱۳ اتاق خواب، ۱۵ حمام، ۲ استخر، ۳ سالن ورزشی و ۲ سالن سینما دارد و میزبان خانواده او در طول مسابقات خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/656534" target="_blank">📅 09:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656532">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ویزای تاج و بیش از ۱۲ نفر از کادر رد شد
🔹
بیش از ۱۲ نفر از اعضای کادر پشتیبانی (از جمله مربیان، آنالیزورها، پزشکان و فیزیوتراپ‌ها) و همچنین مقامات فدراسیون فوتبال ایران که قرار بود تیم را همراهی کنند، ویزایشان رد شده‌ است./ ایسنا  #جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/656532" target="_blank">📅 09:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656531">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای سنتکام: اهدافی را در سیریک و قشم بمباران کردیم
🔹
فرماندهی مرکزی ارتش تروریستی آمریکا در غرب آسیا مدعی شد که به اهدافی در جزایر گوروک (سیریک) و قشم حمله کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/656531" target="_blank">📅 08:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656530">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc5589b7c.mp4?token=cTy0Dt90f1MqK8Y15kZ9cDZ7_MMDLfpK-UXU4I7kOpA2iN9xSZDMcDq6kZXb5iEKvGprRjO2bEESZQSJ-KoDiHu49963MHyMsK5td4u_yOwFz3NS_QJ6gcMh5vrRfuGRTuNjOkR0CZpHP0xXION4XSHRXWGV5yW6aIy1zMdtzfPt6ukjdrZ_YJOVBsd_bp7aw0O_9HUKGERhNUTk2xqBarm7Fjns2S3pY_qZ_smYGLD19n88gHQKyn-atNXr3M8FcFQ3PKquRyOEzmJH7O6NINrTcKZtdM40loX6TPjt0hvf3iNLKs2l6JVtoYYGn9M_O5gJTbNuM_CDr_u1gGzE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc5589b7c.mp4?token=cTy0Dt90f1MqK8Y15kZ9cDZ7_MMDLfpK-UXU4I7kOpA2iN9xSZDMcDq6kZXb5iEKvGprRjO2bEESZQSJ-KoDiHu49963MHyMsK5td4u_yOwFz3NS_QJ6gcMh5vrRfuGRTuNjOkR0CZpHP0xXION4XSHRXWGV5yW6aIy1zMdtzfPt6ukjdrZ_YJOVBsd_bp7aw0O_9HUKGERhNUTk2xqBarm7Fjns2S3pY_qZ_smYGLD19n88gHQKyn-atNXr3M8FcFQ3PKquRyOEzmJH7O6NINrTcKZtdM40loX6TPjt0hvf3iNLKs2l6JVtoYYGn9M_O5gJTbNuM_CDr_u1gGzE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تایم لپس بی‌نظیر مقارنه سایه دماوند و ماه
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/656530" target="_blank">📅 08:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656529">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
هزینه سنگین شکست‌های پهپادی
،
میلیاردها دلار در آسمان ایران دود شد
رسانه The War Zone:
🔹
نیروی هوایی آمریکا پس از از دست دادن شمار زیادی از پهپادهای MQ-9 در ایران و یمن، برای جبران خسارت‌ها به دنبال خرید تمام موجودی باقی‌مانده این پهپادهاست.
🔹
ارزش پهپادهای سرنگون‌شده حدود یک میلیارد دلار برآورد شده و این ناکامی‌ها حتی بحث بازگشت پهپادهای قدیمی‌تر به چرخه عملیاتی را مطرح کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656529" target="_blank">📅 08:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656519">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYczFDe9id-IfiykO69lqcwFJfPBGxccxW9O0YbdRaD8feXOTe9U6It7sZYYpvSvHmpGE3z_jIGTsGC42tdWe_VscZASsLAebKtnBdHiwdSdvH54KcwYaZk5MHues_PxSKVTT3A8pEASVAJWbRQPlhMa8DrQS5KDZZwS9tZpHWQGlvFSNINX9mJhIm1NoM40pLmxy8dYgO9BJx2LuFk5R_rWAk4r9VjMrQrJmQ3UZgGGJkUOE5IqiXnFIflGLCnxFIaDUr_9_t6bdOkTma_APMoJrqnLB6TzUTCzGXbAV4E7eUlSqozeUcQu2yRTl1_mYL92_3VPZ_Kche4F7-uB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAyMFiwMv5p6Zh7gYcx210Fv0dCV7bXK9pcjGd7WTBIL01C_JgR6eaFEco0ZVmFcOPUayCJgjT_YdoSCwMfsWQrbuECBH7yOf0NRPEeuKK73pdYxSM1x0zwMMctR6Sr0hj9-vM9srt6ze5PPVFdhFQ2EXRRWuAv_Lbq4URirOwpvOUylqRBRKhG3R3-AubGqtbSn5_wN2u_qmkf4RJfJiwDYYa2maTLqF6SZivftf_9oOSsURpm6wlynBXE-86ia3cRryQgAVS7ZTXGdUwjUJujna2E3CW76zRFoqAeo1nC3Qpsyj_h1MGoG5LI6Vz3RIrxDzq3wCQZOUhf4V57rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPbKnuiS2tFox3fHn_X1TitXlqj6FcU8zAPuXV4-l2fd8gkogubP1XM_lP4lWlMJEP6EdOuEgmko63GkVQn79GBXx3viUwHCOL7XvU8VchZKUgEo4YvcrWUArPl67h78NktDUays8y-qg6BT-nzzxZW6exo2_XELQGmH8O4FbDIUEuSKaJ6h94i6GI_uFGKM7hgeB9FO5YatKf6jeExwpGWNPVF35fo7buc8vJZCAOCkWNFSsW9eQSajZioX8JXeSooPo_21rQYgWRngQWuBrDjMWwdz1WWBZAqWI1RD06VttUman14-BkpUKMerv1tOWx5S6KvQBGYUa_PQylayTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeXCMWDiX3_fLu9O1kOYOyoxaJlkgUuXXd-QrJWKgKCq4lhSKLfUiPoFS-UCNqQzc47eWWXy1LnOA2hYZUdyGSqTEJS3tj9TtpgbL6AL6NhSXvMVkPKdbbM-v-EOe2r2XcPWY4HjZB9ZYRnpl66W4IJW0G0ibYy85eH3135TR4_D4Z-CPQhlA0jsloAuSEY2nYWiC_q44xVJbabZLHBd0O867ckp1gOvFS2a3tBJrgTKNIIN4i3zh0aHCtJZ_MfssbuxUrYchke2YxzO0U0oLc8hzx5SoO7CQUQmB8BQfMXHHz2YgTmgjx1FWCw6Ih0G5LCcjnFAXdaEeNP1LpVMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFj5taHyTwyod18uLs2zDFQf1lS39vta92xwDmK6PCilZChghkuQDZ_WAtu1BA0mJHgfKFtLUtdL4r5sfU4Ar3BvASKm92tNoGGKCIekeq_oFDZn2x48AUXbsXGdJLRqkd4T4gOnSWd5a7jYyFdHajo2_oF01aU7f6fSXkafiHo9539c7wdIsHeCb-nX3PF09X-BiU9HQnBCQ8OHs-bqbcVT3ALCmdRWD0YkJIZG1OyATzYw0mFojQ_grQ1aWfh6OTGFXcvp9tf_Ks_kumf2QcR2YmFTZ32wKyJZwAci6UbzWGWdsmxnKwnNG7sBnsFPKk5F0xHIDxi8TbJXK0FLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEaISgXevrYvwpKAl7U2sW82whGGoNJKkD4ZrJamVZb6munC7TNBt74tIrNDVy83p4X8jrEzWutunFHvZg1dALBBO5Sn6e2_kDWfEZUV3gaZvyReJiS4Jn7Bmv__wDgxX9HH7SjnlMl4_H40NQRh6XwExKO-h7UtmD6SRvTsAO9KhnReKWU1HrqEj72im1s4XRQStiUS7Au-CzgWYRy_6kNmE6V9GiuJHeIc0soN2M12-aCw-dE7j-kknvIt_6i2iFiuWkx-0L8QiR41Pz9178K0sNW4RHWVK8oblHgPGupzmI26ur4rGguPDlDa0K4G8XZs6nA9jEFScetMtJxysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA2QqrKHS1Y-guD_lQChjbjouFhSNRWv0RXo8RJg2GHn2AAQ2c9ZVEwWE9TFJUmQkKwgGqV5U1hXdlYpmqvPKHWBr_7XaACHG0piK8nnzEvFjWWnMhMoivRWBFKX3dNerGtgPTsJyCGql-xU3-8bq6ri2V-XEye6QimvBzqAb9sX5TVvGxTssFlOIs-uWoloA2obS2fXDZP98F3wcV6XcMxtAWOp3uysGzR0vzYoETETm_k_xgmJSjkQf2kJkeP6A-0qlms_hisxtUISuiSAzDSHu-KdSX9qr-Vtx5nXTDLjv0LcMAndxHy1d1n0wM8yQqpZeNeTi4Zq-MMfAOZrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2YcHPtCbY6Pk8K8FWWeM-szqP7Fo4ZszouQT-kizRqqY6XI63eTRikRWVMMNV1F2EF_CXddxz7ml1JdRGK52mdI9Lh1l2Ber2BnO46MH2_Risx_Jte9YYPdCu2URSA-F50qcAcTKLXA6PXM2QMn8ztYWFs5EtWlFXgr_tb2iw0g1et8urX3Bs5L-jOiE_2RrcgJ_LU_G8tsK66uSm8wM_bBRI41G0lsc5CAulbl-axqRTnivGNTLeKBEfEdQgeNXtQ5ks7M9vE5D0oTNHhWTg7s8O23Yam5TSsP-aIGgSs7kvVAIvxil2tAb-WJmdN-UfUF0HVri2nuiBsArQhQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNSMJdV5-NUajf3yHKfYEEDcVLDvvkZYZHc0Mj7Xar627Jxv4_02vLzH_9539ZnLZw4JmlWlrIXEHbsK8eycWqQe_XcF2r8MMVE5zwA27BuOCfvOIvi0vB-sxVk--nbGb-IfI3ArNdNuPrzZsVKhG2LEaScO5BgHitnQaRbGeatlYzB7AWf5gVGdDauQTUwSMt4RM-w7MA-gCs82JvFr0PxCtEw6Qx4oP86FUi_1LZcFh534aMz5jrnSuuEFJKlUpphZbWZAw12yUNggkee3M5mwOZoUR9cn0DK4fOqafb5cbQIVKwG8lp7hjoORJmS_sV1uSY1QW1BxZynPXpmpiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itMW38D6rrfYOyEHzKnKha3Ei-dDfs2mYzZ6rpu3rSfolUWyd5UffIxewa7-G0q2kBkHB8o6SJUJ89ZhZ5BHs6bbo1_GMImqsCbft_4ekPnf80N6kn1mhO99TT6dLm0bxEjvS7wn2VBfyksNnHuWLnWxDPGz1DMQRQqgRD10j_XBPnLCkcBQO93ceks_qoF58xLQJSIDggaa2s2UexJAoLifh_R6ne2OKqazeExrJv2y2v1a9mvm_Fh2wIXPc9Y4t0ewfSoSgTjsBuEs8aLeJHIyZkdyWOBUoyDpXgh3wy-pKBS-cZ_-dGa9cV2yVgyJtOp-AtHZ4oFwIE0nAyoWBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جشنواره آدم‌ برفی
🔹
جشنواره سالانه آدم‌برفی، پنج‌شنبه ۱۵ خرداد۱۴۰۵ در ایستگاه ۷ پیست بین‌المللی اسکی توچال تهران برگزار شد.
♦️
عکاس: بهنام توفیقی
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/656519" target="_blank">📅 08:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75414e6eb6.mp4?token=UtkJyNTMbUEzZBvPpIMeYoBSQ-RBVO1HuA2PRjRpXYBEs_iH9LT_myOBU0wGoJevCaLAe3E_om6fl0eYJgKEzMSSCXi3KIOK4CURpCNNqHAJi-tlwtKMtOmqtr2oTYc7kdT-Gif3autzXyWyx_7sAMjyBjV1Kso0GcaDPkZpHjfnmKpJyss8-FbMBP5vBh33zDDP78xOz4jWM5NqaIC8kEa0jgGfMWaqv3yEe6Xg2shTZwpsfIGZNR1Jah0_FhJc_-BfuxwfwbquPTIOKGpOsMMhII8wf1WB3o_tGt2MhzedjSF-zjzK4ZCT1tQp4TGPKbGsgbxZ3UPRXIolAttnBjP7Llx-KfzmQtufUbShVj00vXwH04oBOkBAWPo6BbxD2R6plDDrVrdsg7M8QLAq6sTUhF9JFeVkvBlHP5xNtBpzsTS22wW9FQb8iHme0FyTee723SCx7zWt1Me0FLEKfwOcX2xuD0OmBc1OcW4eNYfKE9kKu0kKlHF07kQV0_Jjw53VGegNkmLUBSzcvF7foBnKV5kUtqGvOlgYqKcl3N7VE1a3u9vxh-c6wRzvx6z_sUx4j3k6Pl4GhKs_ZvPgqxmDgk_2XY--ITCFvyJOVv-hYs_0E9lLbWQ8JmfDTqWqmB4e7UhPuJwC2s2yiO0kqFgdeBPhkjGEhelhrSZd_Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75414e6eb6.mp4?token=UtkJyNTMbUEzZBvPpIMeYoBSQ-RBVO1HuA2PRjRpXYBEs_iH9LT_myOBU0wGoJevCaLAe3E_om6fl0eYJgKEzMSSCXi3KIOK4CURpCNNqHAJi-tlwtKMtOmqtr2oTYc7kdT-Gif3autzXyWyx_7sAMjyBjV1Kso0GcaDPkZpHjfnmKpJyss8-FbMBP5vBh33zDDP78xOz4jWM5NqaIC8kEa0jgGfMWaqv3yEe6Xg2shTZwpsfIGZNR1Jah0_FhJc_-BfuxwfwbquPTIOKGpOsMMhII8wf1WB3o_tGt2MhzedjSF-zjzK4ZCT1tQp4TGPKbGsgbxZ3UPRXIolAttnBjP7Llx-KfzmQtufUbShVj00vXwH04oBOkBAWPo6BbxD2R6plDDrVrdsg7M8QLAq6sTUhF9JFeVkvBlHP5xNtBpzsTS22wW9FQb8iHme0FyTee723SCx7zWt1Me0FLEKfwOcX2xuD0OmBc1OcW4eNYfKE9kKu0kKlHF07kQV0_Jjw53VGegNkmLUBSzcvF7foBnKV5kUtqGvOlgYqKcl3N7VE1a3u9vxh-c6wRzvx6z_sUx4j3k6Pl4GhKs_ZvPgqxmDgk_2XY--ITCFvyJOVv-hYs_0E9lLbWQ8JmfDTqWqmB4e7UhPuJwC2s2yiO0kqFgdeBPhkjGEhelhrSZd_Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت اسکوات با کش ‌
🔹
تعداد ست و تکرار: ۴ ست با ۱۰ یا ۱۵ تکرار ‌#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/656516" target="_blank">📅 08:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656513">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای عجیب تلویزیون الجزیره: ۱۵ نفر از اعضای تیم ملی ایران ویزا نگرفتند!
🔹
هر چند هنوز مشخص نیست که این افراد شامل کدام اعضای تیم ملی هستند اما این خبر در حالی منتشر شده که شنیده می‌شود ویزای همه بازیکنان تیم ملی صادر شده است.
🔹
برخی رسانه‌ها مدعی شدند، آمریکا…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/656513" target="_blank">📅 08:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656511">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9a05f5b0.mp4?token=BidfNeoRMs5JcEWrPeFzha2PrPIfbTUxbO-wDZDXu_wLzN1xcDE9NgfzH_JRhgU-gOL0Gt19RHYvaiHo1HQNJDW5Hmu6s3okxL3NoAVkQ6SFAfnpCidPRmwo4Trj7hPySq_EUrCH368ON1xmrjuBpd8v7bnJ_fsC8YFzH-_mdyN-pQuYN747zLBQXqmHnLuIAbAV9ew9u1iEXIG1tqUbKeRKIQYfjBMD0MTtvrsPEtff-7Op3UXZPaaw9OXgu527Fk7YDgffFo4iBri21tKEFWTx0464HaYDIfv_-ZRC_Fx2H3vCou-WEK3YXlCHEiBErgcHakwXPOFNZasWhzabWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9a05f5b0.mp4?token=BidfNeoRMs5JcEWrPeFzha2PrPIfbTUxbO-wDZDXu_wLzN1xcDE9NgfzH_JRhgU-gOL0Gt19RHYvaiHo1HQNJDW5Hmu6s3okxL3NoAVkQ6SFAfnpCidPRmwo4Trj7hPySq_EUrCH368ON1xmrjuBpd8v7bnJ_fsC8YFzH-_mdyN-pQuYN747zLBQXqmHnLuIAbAV9ew9u1iEXIG1tqUbKeRKIQYfjBMD0MTtvrsPEtff-7Op3UXZPaaw9OXgu527Fk7YDgffFo4iBri21tKEFWTx0464HaYDIfv_-ZRC_Fx2H3vCou-WEK3YXlCHEiBErgcHakwXPOFNZasWhzabWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🔹
ویزای برخی اعضای کادر فنی و اجرایی تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن خودداری کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/656511" target="_blank">📅 07:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656507">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای سنتکام: اهدافی را در سیریک و قشم بمباران کردیم
🔹
فرماندهی مرکزی ارتش تروریستی آمریکا در غرب آسیا مدعی شد که به اهدافی در جزایر گوروک (سیریک) و قشم حمله کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656507" target="_blank">📅 07:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656505">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b87e64f79.mp4?token=u1zSUYYSTMMWuaNGI6PfyPsuMi5_MZwZNQ7xjJ0j3-4-JOYSFLAstmF2tP8r8jE4XKhwyPWOXZqWlUvaV8SqWkVbEZn-vqTTFjeNC7A5D71xy2Wq6DPU1E1GFc8vBeW4n989xYLd7kehF_f7ZEwuoXTrw6p0HnEkmG6MNgqQaxlI_bODZUa5t2w4RoRXHolnStYmJ7LmWu07R0uaK6W5QEfoQ5vwPRxnHUkgQ_BIYGwJW1P6HyIKV-1WwL0Cr38yR4Xc7aCCv83RND0zXZxKrqEdUTqrFcCquAfTZxsGY7biXs9JcxTpTaZned80hPHbqnxvQ0hbsFEeEmTAxvSj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b87e64f79.mp4?token=u1zSUYYSTMMWuaNGI6PfyPsuMi5_MZwZNQ7xjJ0j3-4-JOYSFLAstmF2tP8r8jE4XKhwyPWOXZqWlUvaV8SqWkVbEZn-vqTTFjeNC7A5D71xy2Wq6DPU1E1GFc8vBeW4n989xYLd7kehF_f7ZEwuoXTrw6p0HnEkmG6MNgqQaxlI_bODZUa5t2w4RoRXHolnStYmJ7LmWu07R0uaK6W5QEfoQ5vwPRxnHUkgQ_BIYGwJW1P6HyIKV-1WwL0Cr38yR4Xc7aCCv83RND0zXZxKrqEdUTqrFcCquAfTZxsGY7biXs9JcxTpTaZned80hPHbqnxvQ0hbsFEeEmTAxvSj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوهای منتشر شده از فعالیت سامانه‌های دفاع هوایی بحرین و کویت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/656505" target="_blank">📅 07:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656504">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
دو پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی از هدف قرار گرفتن دو پایگاه هوایی آمریکا در کویت به نام‌های علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/656504" target="_blank">📅 07:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656503">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ متوهم: تصمیم‌گیری نهایی در خصوص پرونده ایران ممکن است از طریق یک توافق مکتوب و یا از طریق مسیری دشوارتر صورت گیرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/656503" target="_blank">📅 07:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656501">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEROSZ9l-uiWp9nKcIugrGOx45KhGZlFuRJyJgmltsP3mYIiX8Ct3QjJMbEh7Rkef67slTalXtlyRXBgtlYIni5LVV4P7355Ut24USe2zBLJ2oFtdIjd8aapLdHJLppzdTh3lUufYciXB_92mJp-yXM9luHBw3xpOq6mjkCii1RZmCXA8FbEind0wWOK1PUbDflfh9unVVqtpZ1IYXVYn_iw-Kuh_b7YFRjSSdNLuyDOMjdx5SFPnBCBDN3lJ6d2oVkiuy8BhBc3b4l622CfpEa6XR9ZABIPNkNiojxi2HQr9Ny9vvPf3ZQqTG5CmwsE1XTMrjPWhslJczBN-0_SdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام وزیرخارجه خطاب به رئیس جمهور لبنان: لبنان را از دست دشمن واقعی خود نجات دهید
وزیر خارجه:
🔹
بر اساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی ها را آواره کرده و کشور او را روزانه بمباران می کند.
🔹
اگر لبنان برای ایران ابزار چانه زنی بود، ما مدت ها پیش به توافق رسیده بودیم.
🔹
لبنان را از دست دشمن واقعی خود نجات دهید، آقای رئیس جمهور!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/656501" target="_blank">📅 07:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656500">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">حسنک وزیر</div>
  <div class="tg-doc-extra">پادکست کافئین | قسمت بیست نهم</div>
</div>
<a href="https://t.me/akhbarefori/656500" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
حسنکِ وزیر
🔹
بشنوید از داستانِ مردی که طوری پای چوبه‌ی دار رفت که گویی بر تختِ پادشاهی نشسته است؛ درسی تاریخی برای «باوقار باختن».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656500" target="_blank">📅 07:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656499">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3118ae458.mp4?token=QGssc3uLEybFvU9rXUFI0MvV2z8DeZ9EoACQTTaMwzJFbtpfhZZ7B1gAvDGxW5wz8IJtDnWoBpe_grCe20dLtZlvOeXCjX2duPkqELpkN87SyidoWwasogUn715HAZ_uewwlMSZIraTLm_NfGIsSCkeaVvtWEsXAv1YPKYJ1ZTCYVdJQvO6zZVDnJOjDQL8579RoXPUpwmq7UKoUTU5ANH-7EhYBEU--9KT2EwGZzS82kXkIgtTC__qxEuJYOI8XKNmGvUWlUQ8n__MzZtR8POz5sNx2C6TD1qAYfAcTZppVuYxpRqou0Ug6nf_eeKCB-T_H0QPRsyBLJqaTbwGUpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3118ae458.mp4?token=QGssc3uLEybFvU9rXUFI0MvV2z8DeZ9EoACQTTaMwzJFbtpfhZZ7B1gAvDGxW5wz8IJtDnWoBpe_grCe20dLtZlvOeXCjX2duPkqELpkN87SyidoWwasogUn715HAZ_uewwlMSZIraTLm_NfGIsSCkeaVvtWEsXAv1YPKYJ1ZTCYVdJQvO6zZVDnJOjDQL8579RoXPUpwmq7UKoUTU5ANH-7EhYBEU--9KT2EwGZzS82kXkIgtTC__qxEuJYOI8XKNmGvUWlUQ8n__MzZtR8POz5sNx2C6TD1qAYfAcTZppVuYxpRqou0Ug6nf_eeKCB-T_H0QPRsyBLJqaTbwGUpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسنکِ وزیر؛ و تراژدیِ «حفظ وقار در مسلخ سیاست»
#پادکست_کافئین
| قسمت بیست‌و‌هشتم
☕️
🔹
هیچ‌کس به ما نمی‌گوید وقتی شکست قطعی است، «چگونه باید باخت؟»
🔹
در این اپیزود به سراغ مقتدرترین وزیر امپراتوری غزنوی رفتیم. مردی که وقتی فهمید راه نجاتی از چوبه‌ دار نیست، به جای التماس کردن به آدم‌های کوتوله، با فاخرترین لباسش به استقبال مرگ رفت تا به تاریخ ثابت کند: در زمانِ سقوط، «اصالت و پرستیژِ خروج» تنها داراییِ یک انسان است.
برای بیداری، یک شات غلیظ از تاریخ ایران کافیه!
از اینجا ببینید و بشنوید
👇
https://youtu.be/wGPuPBpm5AY?si=Ln3xUuAdgTaF5EDZ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/656499" target="_blank">📅 07:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656498">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDIqCdRV3TmOXqQCDXfvhEv6xoUMP3APK2uHxDZtOX6l_N5WvcVZ02RZUJOasg6eLV1ia2ju7qnhHG2SGZJXrDJULmDedZhpZO8JVmZVIzp8IwdmkPBK1tMuNWUc9-qDi7xp0kzbJjg8xQE223Jw5w5qDCclfnNTyZRDhmsWCW16Dq7kWwvxViWC9UXZLuOQ5dyQvNtcsIATJzEfFyxeCoTkP2mjaJ3fhmBqNHBaEA4BrOm1RGLnoYxLfwjkQ7xCupcN8EsAkNpXfO96aUCCCAQqLJ5hHpFQwn8diO-yI8tKNf_XR7zoagmKmyL-LlxxRUCAwUry-JJvhmagh2nSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۶ خرداد ماه
۱۹ ذی‌الحجه ‌۱۴۴۷
۶ ژوئن ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/656498" target="_blank">📅 07:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656497">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سنتکام: ایران ۷ موشک به سمت کویت و بحرین شلیک کرد
🔹
فرماندهی تروریستی آمریکا «سنتکام» حمله موشکی ایران به پایگاه‌های آمریکا در کویت و بحرین را تائید کرد.
🔹
سنتکام تائید کرد که ایران ۷ موشک به سمت اهدافی در کویت و بحرین شلیک کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/656497" target="_blank">📅 05:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656496">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
دو پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی از هدف قرار گرفتن دو پایگاه هوایی آمریکا در کویت به نام‌های علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین در پاسخ به تجاوز ارتش کودک‌کش آمریکا خبر داد.
متن بیانیه سپاه به این شرح است:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔹
ساعت ۱:۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون توجه به اخطارهای مکرر نیروی دریایی سپاه، قصد خروج غیر قانونی از تنگه هرمز را داشتند که پس از اخطار، یکی از نفتکش ها مورد هدف واقع شده و متوقف شد و دیگر شناورها متخلف به عقب برگشتند.
🔹
به دنبال این واقعه ساعت ۲:۳۰ بامداد، پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک مورد اصابت دو پرتابه قرار دادند. در پاسخ به تجاوز ارتش کودک کش آمریکا بلافاصله دو پایگاه هوایی آمریکا در کویت به نامهای علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک های بالستیک نیروی هوافضای سپاه واقع شدند.
🔹
به دشمن متجاوز و کودک‌کش اخطار می‌کنیم در صورت تکرار این شرارت‌ها به پاسخ محدود اکتفا نخواهد شد. مسئول عواقب بسته شدن کامل تنگه هرمز به روی خروج نفت و گاز شما خواهید بود.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/656496" target="_blank">📅 05:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656491">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQrt6vSCeImYiJRSJuUQTMn1TsIqdrL4jYpG8bYIsQXkT7fmY7b1XA9_Mr7tcnzlRykeoX1T1-2aeQVLXKffsAarFUyA8ghaedy9hd2RAh14k8n9Hx2MgEU6PH8Z_dqNZJeBweEUTS5wkIKvAkvJZVy_t9E7uDp3uMPnvw9WtWRP47-hLqrXuWs57bC_UxDXen4gSQEpmze0s8wsPMAbIrtOMfj87JmO6sdi-7kqczS82hc3-_kaSMMp_lwdms5DBICD-lnFU_up64A85eRtEFUCOu9mUMB0_xVLO5E9zOs7xvkXZFHWNimSSxpbVFc3gNJZ-zW6CigP0oAc-arURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/656491" target="_blank">📅 00:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh6eGA-DShhbwgIz9uJkb93GEWAHKqX-uQEDJLxBYrTuMraD8t1ZFVOzp0deraL735ZnZGhNfOsrxLN3MLRnO0kXhkka78pQbTp3eUy0auKyDHHdvQPFvU983xH5XdCN60TLVdlLD7-kdZBSUeg7trcrIx_dk44KPjiT3Z9K0CHEdCojxCMMZY4mEJcTuFUnYMYyVIF-jisB4j2v3rzXrVtnjlxOxx6Tpmj97WVDsWgReGz0KRll-iIo9AkM6_-Y-foAZRGp6n1js9H2-8arKPQgwN2Xl0_3aKOAhfiKgU6M6xV-JVilMW0Bb0vZlDOcgiO53v3sftkBWpicla06NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سنتکام به شلیک اخطار ارتش به سمت ناوشکن‌های متجاوز آمریکا  ادعای ستاد فرماندهی مرکزی ارتش تروریستی آمریکا:
🔹
شلیک‌های اخطار از سوی ایران برای هشدار به کشتی‌های آمریکایی در دریای عمان و عقب راندن آنها نادرست است.
🔹
لازم به ذکر است پس از شلیک های اخطارِ…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/656489" target="_blank">📅 23:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0LUvut5j_E6LfyM0Xj-Amkphn24VthyGtHvvHrnWmHSKI-Ljyl4noPPZp9InMgHiDywAKSKVMyT_cf6ZyYIoIoAaQxCviCtkgQ_g2qYCB2Yks6skKuNqfxJWl-aeRQCuMMMg-kvqfXmoJN_nOjxsL4YbegFWMWnPGSF4s-AWV3rn_OAlgo58uSd57HppY5mrc4Zxarfp3hn9ZazTYL1sWDEnsK50d4vWZb1M7HH_5GN82ScAVRAfdLkCnMUqt-6isAPI97W5ROUi4kTDqckgoTyJjSxlewWcWEaBrb_CGuP5JnZk4mTr9o_1-QsfEjPqXwBIgkkgbneAQEIbEg0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ زرد: در حال بررسی ارسال سلاح به تایوان هستیم
رئیس‌جمهور آمریکا:
🔹
در حال بررسی امکان ارسال بسته تسلیحاتی  ۱۴ میلیارد دلاری به تایوان هستیم.
🔹
هنوز درباره ارسال کردن یا نکردن این بسته تسلیحاتی به تایوان تصمیم نگرفته‌ایم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/656488" target="_blank">📅 23:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd3_iDBNONAkZDbx4pVU5YKPqK88P3IDevmeUbQNMHi6KNuKmMDCGaNjgLTaCK7NK4kflnEOL9ealk81rUzHqmSuJNpm6nnsmw0C6aJqAZxxl-3cwXcw5-IA6foxQig-t_LG5e0mMsCMZwa8x0PopZ5YRUYoy5WPNCSdoDqZ2oX4IF4-A5x3uX8_UjZS-xgz9YhkkB8MT46cHfY3EGnt0_fuLYJ3QG-wEVnTP5vw5j2KdT3bFmCkzxrj5Km8zW1xes4WRIjih-so6T9v3a-qOkcojzaDf_0P0zAwIhJFWKPTbH45lFUgDe0gW4hxK1YtS_EDna-i2nWDTweWCtNdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری تماشایی از قله دالانپر ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/656487" target="_blank">📅 23:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656486">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a55273f8b.mp4?token=atPgiaEHnWhP0WA825jAQEWZRWSLxyXqwDNBTElIHxv9fTtZJDgE3Mna3MLdkcyU4XEkNU69sa5t_QdRGaIwg0qzDR9sDabUg-U6zPvI3f-x6HFeO-KiDPVDNXZ2ftgERvtKQUiLnTAojVx1o75LLA1IeqHIUmEQhoqLEz1cI0iK2M0Idf3zUIe0XJo6xkWDp0gq0lN3Dr02G_kPCH7gDwst5GsILWjRvnxFv5Ass5alqSkhWmrV3GRbFXMs37ZuaML6z4lNFLkBjo8VOtPtBDAFN3GePpjCp4iotclNsrvalWL2updIqFZXU39SutfKXzILT1R6VU_6RRsknT59toWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a55273f8b.mp4?token=atPgiaEHnWhP0WA825jAQEWZRWSLxyXqwDNBTElIHxv9fTtZJDgE3Mna3MLdkcyU4XEkNU69sa5t_QdRGaIwg0qzDR9sDabUg-U6zPvI3f-x6HFeO-KiDPVDNXZ2ftgERvtKQUiLnTAojVx1o75LLA1IeqHIUmEQhoqLEz1cI0iK2M0Idf3zUIe0XJo6xkWDp0gq0lN3Dr02G_kPCH7gDwst5GsILWjRvnxFv5Ass5alqSkhWmrV3GRbFXMs37ZuaML6z4lNFLkBjo8VOtPtBDAFN3GePpjCp4iotclNsrvalWL2updIqFZXU39SutfKXzILT1R6VU_6RRsknT59toWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید یک نماینده مجلس به ترور مقامات اسرائیلی
متفکر آزاد، عضو هیئت رئیسه مجلس در شبکه افق:
🔹
اسرائیل بداند که مسیر ترور یک طرفه نیست/ همین امروز در خیابان‌های اسرائیل اتفاقی افتاده است که معادلات را عوض کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/656486" target="_blank">📅 23:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔹
خبرهای داغ امروز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
گزارش لحظه به لحظه از اخبار جنگ و مذاکره ایران و آمریکا | از شلیک موشک هشدار ایرانی تا توقیف نفتکش از سوی آمریکا
👇
khabarfoori.com/fa/tiny/news-3220568
🔹
ترامپ: به‌زودی جنگ نهم راه خواهد افتاد!
👇
khabarfoori.com/fa/tiny/news-3220567
🔹
رئیس جدید موساد کیست؟ | همه‌چیز درباره مردی که می‌خواهد نظام سیاسی ایران را تغییر دهد
👇
khabarfoori.com/fa/tiny/news-3220645
🔹
ماجرای آرم «ساواک» روی سینه طرفداران سلطنت؛ چماق به دستان وارد می شوند | رضا پهلوی «موسولینی» می‌شود
👇
khabarfoori.com/fa/tiny/news-3220679
🔹
پیش‌بینی یک نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر حمله کرده و ایران را تبدیل به غزه دوم خواهند کرد!
👇
khabarfoori.com/fa/tiny/news-3220707
🔹
ویدئوهای جذاب ما را در آپارات خبرفوری تماشا کنید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/656485" target="_blank">📅 23:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656484">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
صدای انفجار در کردستان عراق
🔹
خبرنگار المیادین گزارش داد صدای انفجار در حومه سلیمانیه در کردستان عراق شنیده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/656484" target="_blank">📅 23:40 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
