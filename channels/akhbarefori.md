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
<img src="https://cdn4.telesco.pe/file/edHwB3Tg161wjMCQG7ePdnsXc2Z6NyfSrKNlpYg-SzjP0Cgot7dwF4Yij4Tv6P-9fLaXrVgRhVLvqTOWS2V2oOv0uVHRPMF-jT2c_o2zPhhYg3gfAANjNfTdwiIOdBTCSr5QWfK3TAyYUIRkhSgg9aCCnVrXhIIuvBc8BM_0lYxxW1BXs1RUucr7bJCJve7aqktPaveTkNY3lFBWTiQE_U08iZ0R5UzF_MbOpKPLNLmL1uolgpNECjbEKB5wznPDf5sXJoVh-qdWWLYNJTeuMHqzKlxevTdUXYHGBo7Z4bS6BX7_kLjFmtsrJ2OOUXdURgNyVuC1uQlNVyJAGrf4wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-670519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در امارات
🔹
منابع خبری از شنیده شدن صدای انفجار در امارات خبر دادند. وزارت دفاع امارات با صدور بیانیه‌ای فوری اعلام کرد که در یکی از انبارهای نظامی زاید آتش‌سوزی رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/670519" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
منابع یمنی: عربستان همزمان با نزدیک‌شدن هواپیمای ایرانی، به فرودگاه صنعا حمله کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/670518" target="_blank">📅 15:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca8bcaccc.mp4?token=rwA1xNgn-8cjCDeRN8OrCmvfusC9RS_oF9RmLUdhuIxGp6u8QhebUTT0JhEOIoOF5R7J9Rgdd4_0tVRYcpxGrhLz5xlR1zBRBjq4GhuESVpS0l91b3CT7BkhklClrm-iILv3rS31J1B3r_QWjTYvEN9tHUP6g4JzXBiZFjLWCiUyDJmBR2i62A9VClHcqazY4_H3xilHAMhbBJUxkHdDeBGgSjxf-KvFd5TyUJsw0fbW7f77fOUDlE8QGl3cutrd2-zlZ4lNM0GTEOKrwaULHIwayk6l2Wj9k1KL5rxSaQkwqsxgGWcCBRfKeA-EeoFB908kmXMbI8PYZAoe8rObXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca8bcaccc.mp4?token=rwA1xNgn-8cjCDeRN8OrCmvfusC9RS_oF9RmLUdhuIxGp6u8QhebUTT0JhEOIoOF5R7J9Rgdd4_0tVRYcpxGrhLz5xlR1zBRBjq4GhuESVpS0l91b3CT7BkhklClrm-iILv3rS31J1B3r_QWjTYvEN9tHUP6g4JzXBiZFjLWCiUyDJmBR2i62A9VClHcqazY4_H3xilHAMhbBJUxkHdDeBGgSjxf-KvFd5TyUJsw0fbW7f77fOUDlE8QGl3cutrd2-zlZ4lNM0GTEOKrwaULHIwayk6l2Wj9k1KL5rxSaQkwqsxgGWcCBRfKeA-EeoFB908kmXMbI8PYZAoe8rObXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سمفونی «مظلومِ مقتدر»؛ روایت رنج و فداکاری
🔹
هر پیروزی، حاصل صبر و فداکاری مردمانی است که برای حقیقت، از عزیزترین داشته‌های خود گذشته‌اند.
🔹
موومان چهارم «سوئیت سمفونی مظلومِ مقتدر» با عنوان «خون دل»، عمیق‌ترین لایه‌های احساسی این روایت را با آواز بازگو می‌کند؛ روایتی از رنج، استقامت، ایثار و هزینه‌هایی که برای حفظ عزت و سربلندی این سرزمین پرداخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/670517" target="_blank">📅 14:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSjdYNQ1n2NuVLiAYHvPbZs6zJ_iddIR_1Mo3XSQamf6GirHCcpX8iVbuHEcPbjBP0F0IIM7Ds9qPa0PXyw7ZW_HXyzZIpaa9NN62_Q4W76KbDHUD0BReW7qnVvXSEANNEU5M2H4CRR6aDauis-fsHH6Na_AcfxxRamGf2eeLobX539wUJOr2XINvoRUqlYIAfSsq-7d0gfiTDlcD2aO8A3W9-26-zGKhFJ9XtHVQPoSHUKiFfEXvec-zYVxWw-N-3xLdTa7fAdYKR7XbK9coztU2_lCliT8x6eedrMtJvOpXIdeo109VHYyh_kHMpNZIvg2ybtlCjffKFEtfylhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میچ مک کانل (Mitch McConnell) سناتور جمهوری‌خواه تندرو و ضدایرانی هم که یکماه است ایست قلبی کرده و در بیمارستان بستری شده و هیچ اطلاع دقیقی در مورد وضعیت او در دسترس نیست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/670516" target="_blank">📅 14:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57059b301.mp4?token=RV7vvVVqQbsxe0Cp7OY6g2yn2OQCP4vwcgtxMXgE4EeFE1u58F8Zdkno6GK3ifb8sIG_6it8SzWgl0zCWPplIRnEQ8PTrWZoRAKkW4crR3yHHIr6O8dUW9vCwduMdz2szj_52KHL-c_Apm-4JQTdzirCMJvI1flLw5Oyzj1_xHyapV0SDZewZvqcF7AYKI3Q8stUkEJe_CDPIMlmGolwiBQCmvZArX6tqg4s_Pr2nw3lx0c1invLI3w_QGxRfuCXKku-JoEuS76XI6bEqaKtPmR3zsayFFEU33uk2Kky3NaEUC4u6MZoAOVjhJ1skpNf2H9Vll5waTTfHEjaxtXoMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57059b301.mp4?token=RV7vvVVqQbsxe0Cp7OY6g2yn2OQCP4vwcgtxMXgE4EeFE1u58F8Zdkno6GK3ifb8sIG_6it8SzWgl0zCWPplIRnEQ8PTrWZoRAKkW4crR3yHHIr6O8dUW9vCwduMdz2szj_52KHL-c_Apm-4JQTdzirCMJvI1flLw5Oyzj1_xHyapV0SDZewZvqcF7AYKI3Q8stUkEJe_CDPIMlmGolwiBQCmvZArX6tqg4s_Pr2nw3lx0c1invLI3w_QGxRfuCXKku-JoEuS76XI6bEqaKtPmR3zsayFFEU33uk2Kky3NaEUC4u6MZoAOVjhJ1skpNf2H9Vll5waTTfHEjaxtXoMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم حملات گستردهٔ اوکراین به نفتکش‌های روسیه در دریای آزوف
فرمانده نیروهای پهپادی اوکراین:
🔹
دیشب ۱۵ شناور روسی از جمله ۷ نفتکش را در دریای آزوف هدف قرار دادیم که تعداد شناورهای منهدم‌شدهٔ روس در ۸ روز گذشته را به ۱۰۵ رساند.
🔹
طبق گزارش‌ها اوکراین در هفته‌های گذشته دست‌کم ۴۰ نفتکش روسی را در دریای آزوف هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/670515" target="_blank">📅 14:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFEmPzkCB9GDuv76NbRp04cVKcXnj-3YATwIdSpSKklGUZjCWWhuYQyX8t8rPqFm7CtlYwPnzo9IUfZCjSXtoeIDONeh5qKEor5Khlno3O3UpsTEfEdz1UYsOK6DW2bZ7b5lBwV7L0jCfhSEF7xkOouiWaB0EzTRF9QKp1MhDAZjDkdnj266MFjmtGLS6dSuZDW92R-Bz2TD29N7Gb6TthU9BbAdKvHSmbR-qHqNLvuFNcItxHil1wSUlpRAr9NvwGiglE1O3j5pi9PZJgC89nR6FkL5pWbd2ol_M3JBYpvcgBgCL9ALrN4GGVs0l6Isa7XmSh1HH2ZfnNqA7ubX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/670514" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/670513" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670512">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/670512" target="_blank">📅 14:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670511">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3OXq-7iRgYicHRq61yhNV12Lz67G8IwWxJhU2lIegwOZZWrOkUv4AjbXNKJb73vubwyqnFkZ9z5b0GSc792n934j8B-olBw2ACbk-eFcq7Egpzcc90EWydOpI1tWyZWPNmXiCDXdd8k2r93PihMJTbj5HFvELTqJrHz9_ij_CP9Gm0m1PEoxJep1pp1noRxm1sF_M7SdYOWY-CUFzgkv4-9P-J1Ox6iQ8nanUAA4uKFTK46ZK2v3dDVrnqHazEEEtaKv4pcRrH3-EXaTqY8JOJ6oT_q2CEYEQH3-ckY9hqV-Vo5kDITLuZn-UbXWlA2y8I6W58NLsiyP9fx8GuiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین بازدهی بازارهای مالی در سال‌ جاری
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/670511" target="_blank">📅 14:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670510">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f53e24f4a.mp4?token=rSqCdusksGXF_kg0u-QQJ_QuY9Pw6pPUWPlpsKxG8NIdyquE9_I-I23WinyiCMISAT3xCdYfjgo6gpXD8Xq8YuvGFEfggF1lNYIqA5H6awVioWRXEMk2t0IRaZ5P6bvjkqiq8ZayrnC8ioVEkaRRNUf95vpzV-BGgxmZa3fVoJBQNRPMHg-q9I9kmnsxdqjnEFojYuAAGgIEFqJGjERCnr_eYQ36H7-B4Qw-INCox7X7AEDf4Kd2GaX8xXbq2DnqvB8VXvHdrWpv8pe12pP3CMty341OJCaISPCQnmsnMEYqrAsFR81U2kgKP2-Xgz93fKsTRW2IJGlnfVCLyKDZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f53e24f4a.mp4?token=rSqCdusksGXF_kg0u-QQJ_QuY9Pw6pPUWPlpsKxG8NIdyquE9_I-I23WinyiCMISAT3xCdYfjgo6gpXD8Xq8YuvGFEfggF1lNYIqA5H6awVioWRXEMk2t0IRaZ5P6bvjkqiq8ZayrnC8ioVEkaRRNUf95vpzV-BGgxmZa3fVoJBQNRPMHg-q9I9kmnsxdqjnEFojYuAAGgIEFqJGjERCnr_eYQ36H7-B4Qw-INCox7X7AEDf4Kd2GaX8xXbq2DnqvB8VXvHdrWpv8pe12pP3CMty341OJCaISPCQnmsnMEYqrAsFR81U2kgKP2-Xgz93fKsTRW2IJGlnfVCLyKDZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگۀ هرمز در پی نقض یادداشت تفاهم توسط ارتش آمریکا، همچنان بسته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/670510" target="_blank">📅 14:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ایتالیا: نمی‌فهمیم چرا نخست‌وزیر ما از ایران تهدید شده!
خبرگزاری آنسا ایتالیا:
🔹
تاجانی، وزیر امور خارجه ایتالیا، پس از آنکه چهره نخست وزیر در فهرست سیاه یک روزنامه ایرانی قرار گرفت، گفت: تهدیدهای ایران علیه نخست وزیر جورجیا ملونی غیرقابل قبول است و ایتالیا علیه تهران نمی‌جنگد و نخواهد جنگید.
🔹
این تهدید «غیرقابل قبول» است.
ایتالیا علیه ایران نمی‌جنگد، به همین دلیل است که ما دلیل این حمله علیه ایتالیا را نمی‌فهمیم.
«این یک حمله باورنکردنی است.» /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/670509" target="_blank">📅 14:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
استانداری خوزستان: در پی تهاجم هوایی آمریکا به نقاطی در ابادان تاکنون دو شهید و سه مجروح گزارش شده است
/مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/670508" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
برق ادارات پرمصرف این هفته قطع می‌شود
🔹
حدود یک‌سوم جمعیت ایران تا ۳ دهه آینده پیر می‌شود
🔹
تهران و مسکو به نهایی‌سازی قرارداد تجارت گاز نزدیک شدند
🔹
کرملین: کشورهای حامی اوکراین، جنگ‌طلب هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/670507" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
کلیه اختلالات بانک ملی رفع شد
بانک ملی :
🔹
به اطلاع شهروندان میرساند کلیه خدمات بانکی و مالی بانک ملی ایران شامل همراه بانک، اینترنت بانک ، تسهیلات و ..... بعد از مدت ها از ساعتی قبل فعال شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/670506" target="_blank">📅 14:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اصابت پرتابه‌های دشمن آمریکایی به آبادان
«حیاتی» معاون امنیتی و انتظامی استانداری خوزستان:
🔹
ساعت ۱۳ و ۴۵ دقیقه امروز دوشنبه ۲۲ تیرماه شهرستان آبادان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
تاکنون مجروحیت یک نفر در اثر این حمله گزارش شده است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/670505" target="_blank">📅 14:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k08tjoHbcl3h_-Kpz9Y7K3A2YLHmtUx04kovuf0Mar5MJ-MaZJYICArJNfok5uMIilc1zKNLMfD0Hm5HClFy6D--WEiXYVZPBE40_K9pDMvHZMDs55kF7pD7IJagLa2UXBNYm40OK2pUzO8l2o7AEzHcCW3BCrFTJ-4a5shHCG4R8Hu9no7RBl_Iny0M2OIqC50raGWEgjsc6m09X9RF7QBfOtVz-8ww0Jnzeb6EBfxwP0N7Kq5PclgrJduepbviQ2mhJ7UyNDtqY2SHi9PKla8Tv2qfNpRj1_vWKIxb9uMqJkkSGs_ABELCxybEVLcgvJIo0boI-JO4yjJgdql3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما او را به خاکِ ایران سِپردیم؛ ولی یادمان باشد که او
خاکِ ایران
را به ما سپرد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/670504" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c4d6e586.mp4?token=ewPunu8yJYrfel_3FrUhKB0E-s2lBI8eFaYTWZ8XLJRRMfXWFoUNiVBfE0TvVrSel-yLAoXQSuN7HvSn2EVcqA2ptFy2_qT6eXGfhwSutHAr5yqEgfTim0DMEcJCAtqhH4f653kaapcPPY-nANBlv0KfGrOVknz1xE46fCJ2t3hY-e83mG_52_i7W1QAQiodbwkA0aODa9OIgwsXsCDq1TxU0fs22O5-jkLkQAKg_FPQTquVmr0mdKSwyBGhmyTgRM9fAP9q8yV-Eu8lD51IWRQGxdTG2OVYOBcvSjbezDxWx2zoS-MdfsTO8AyO-Sg0TltD7yUvvsAnb_s4a7jhmazq0w2pJ8x-E9-xb2bV0vUsOwMcUmOcx4NAi_FnOqbQDjJfAK6y-AXqqlncbNm1TZiNuupiH74qJ-v28TddcT0wcazkmjZNYr-hkFag5P3FF1I9BGZAVr12F7wCVULV0OjUBHj63jWBdb-Dmxd96thM6dE92skAnz8J0ry1rQ_xEF2XmLq95Vlxdd-HiJ-WgtXF2Bh0C3DZL6I8MjtSrG63XrECjZCVK7VQn4kYq8aVMfDNOTfqJJj8OrbJzdxp6MugeLR5xoVB1v8in6rZAcpwQ-ooJ-QpfG3dP7KwSShEZJOppigdsU_CQi5_LxCvQ1IqJhjS9389CfXCdGzR6wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c4d6e586.mp4?token=ewPunu8yJYrfel_3FrUhKB0E-s2lBI8eFaYTWZ8XLJRRMfXWFoUNiVBfE0TvVrSel-yLAoXQSuN7HvSn2EVcqA2ptFy2_qT6eXGfhwSutHAr5yqEgfTim0DMEcJCAtqhH4f653kaapcPPY-nANBlv0KfGrOVknz1xE46fCJ2t3hY-e83mG_52_i7W1QAQiodbwkA0aODa9OIgwsXsCDq1TxU0fs22O5-jkLkQAKg_FPQTquVmr0mdKSwyBGhmyTgRM9fAP9q8yV-Eu8lD51IWRQGxdTG2OVYOBcvSjbezDxWx2zoS-MdfsTO8AyO-Sg0TltD7yUvvsAnb_s4a7jhmazq0w2pJ8x-E9-xb2bV0vUsOwMcUmOcx4NAi_FnOqbQDjJfAK6y-AXqqlncbNm1TZiNuupiH74qJ-v28TddcT0wcazkmjZNYr-hkFag5P3FF1I9BGZAVr12F7wCVULV0OjUBHj63jWBdb-Dmxd96thM6dE92skAnz8J0ry1rQ_xEF2XmLq95Vlxdd-HiJ-WgtXF2Bh0C3DZL6I8MjtSrG63XrECjZCVK7VQn4kYq8aVMfDNOTfqJJj8OrbJzdxp6MugeLR5xoVB1v8in6rZAcpwQ-ooJ-QpfG3dP7KwSShEZJOppigdsU_CQi5_LxCvQ1IqJhjS9389CfXCdGzR6wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جهان‌بخش پس از بازگشت از جام‌جهانی، نانوا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/670503" target="_blank">📅 14:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
عراقچی: گفتگوها درباره تنگه هرمز در سطوح سیاسی و فنی ادامه خواهد یافت
🔹
در سفر کوتاهی که به مسقط داشتم با وزیر خارجه عمان دیدار کردم
🔹
به همراه هیئت‌های حقوقی و فنی، درباره هماهنگی دو کشور ساحلی تنگه هرمز برای مدیریت این تنگه و تردد کشتیرانی به گفتگو پرداختیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/670502" target="_blank">📅 14:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
محکومیت ۱۲۰۰ میلیاردی سرشبکهٔ‌ اصلی قاچاق سوخت در میناب
رئیس‌کل دادگستری هرمزگان:
🔹
حکم محکومیت افشین بادپروا، یکی از سرشبکه‌های اصلی قاچاق سوخت در بندر کلاهی میناب، صادر و به پرداخت بیش از ۱۲۰۰ میلیارد تومان جزای نقدی محکوم شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/670501" target="_blank">📅 13:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710326a1fd.mp4?token=KXusA792UnewLAJDD1T8BgZIBzyYHMr4HpQ253FAcxi2BSfyz1xLXR1C7huwouyn8Ka8kau0G69R7K7p2xqc5LqDFXIpsGhqvUz9dvus09pW5OeAiv0L1CaLd7LxJ_v9hFXWWaTA30Cai1vk0aAJN4LUydvIlG4HAiCt6Zml2CTLd4owgZn6CtQAn5tyS43q3Y1ftWclHAPADUcV3IxiEOI7lBoiwCRvcJf7H7n2NFRYgQ53geXRsJxwHvWFyuvsNHOsG662IgGgB0fAF16T-l_Q8JNOkrnGLP1nya9RAbd8LV1swj7ld40D7sqgIgzuU6SrIj-bCDVZ_6Xkj63uyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710326a1fd.mp4?token=KXusA792UnewLAJDD1T8BgZIBzyYHMr4HpQ253FAcxi2BSfyz1xLXR1C7huwouyn8Ka8kau0G69R7K7p2xqc5LqDFXIpsGhqvUz9dvus09pW5OeAiv0L1CaLd7LxJ_v9hFXWWaTA30Cai1vk0aAJN4LUydvIlG4HAiCt6Zml2CTLd4owgZn6CtQAn5tyS43q3Y1ftWclHAPADUcV3IxiEOI7lBoiwCRvcJf7H7n2NFRYgQ53geXRsJxwHvWFyuvsNHOsG662IgGgB0fAF16T-l_Q8JNOkrnGLP1nya9RAbd8LV1swj7ld40D7sqgIgzuU6SrIj-bCDVZ_6Xkj63uyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک های قدر، عماد، خیبرشکن و ذوالفقار در پاسخ به تجاوز ارتش تروریستی و کودک کش آمریکا در سحرگاه و صبح امروز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/670500" target="_blank">📅 13:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0259577f.mp4?token=cDhEjMwakKNhMH-hRmB90t9ZZUZoDX6z9MC0dqRzqGvcx1sxsS37luBh8VlW_kFC--AuQhFO53TpqHiwb_R6YuoAYv6vPyvm98PFBXIPSxNvqbDi9iZpk9s_uj-_fdS3iYagU2Pnk8JLunKghGZz5GXoOp7mUUUsgEwztPbiMX7dgQ9CcilvNI390Y6yAQg7RHPMsCrvdM2DuB8H_-GCrF0TS3Oe-jebhxnSkzWxfSmAqA3xbblvSNWjXHwzp72zSEAaUbzLdgx5nbIAtcSZutGeDmE3-ghipZnNZq_Sv428B15C__xMSTtK3Z_AzS6Wr2I5ziJxn2mNI4keXcR7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0259577f.mp4?token=cDhEjMwakKNhMH-hRmB90t9ZZUZoDX6z9MC0dqRzqGvcx1sxsS37luBh8VlW_kFC--AuQhFO53TpqHiwb_R6YuoAYv6vPyvm98PFBXIPSxNvqbDi9iZpk9s_uj-_fdS3iYagU2Pnk8JLunKghGZz5GXoOp7mUUUsgEwztPbiMX7dgQ9CcilvNI390Y6yAQg7RHPMsCrvdM2DuB8H_-GCrF0TS3Oe-jebhxnSkzWxfSmAqA3xbblvSNWjXHwzp72zSEAaUbzLdgx5nbIAtcSZutGeDmE3-ghipZnNZq_Sv428B15C__xMSTtK3Z_AzS6Wr2I5ziJxn2mNI4keXcR7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش آسون و خلاقانه سرخ کردن سیب‌زمینی، مهمونات رو شگفت‌زده کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/670499" target="_blank">📅 13:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRbvwugMO_u5RYEEGAyWDGMVfYF8IKFd9cwDl0Unxp-fObMFGhgk9mB97w10bqGWC3WEtyikyrez2iiJaGlw1TVHGT50dzvEg_atF78wjEclefmIpjOhShqjJJHhI82EE4VHvY6ttiHHMx8FBMySU4cmJw2c8gIP-PucGYbKmmOU_Q7d1ult3ifQjFm-jav1zzAvNxj1y-jvel6wylVavCNf_Ti-DQ3DeCQ7A3mav888ecXi10YyOnV9eW5MTaA7ysS3ZzIhXnTf5AmrKd65Y0rUFDMws9Q5qeAGCWTyDjAbAFT4I4kmdic7rCBXNpV9nAkGIMUEyW7JXgYJIc61uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران فاتحه دبی و دوحه را خواند!
🔹
تازه‌ترین گزارش شاخص جهانی زیست‌پذیری اکونومیست از افت قابل‌توجه جایگاه شهرهای خاورمیانه، به‌ویژه حاشیه خلیج فارس پس از جنگ با ایران خبر می‌دهد.
🔹
در رتبه‌بندی ۱۷۳ شهر جهان بر اساس شاخص‌هایی چون امنیت، سلامت، آموزش، فرهنگ و زیرساخت، دوحه با سقوط ۷ پله‌ای به رتبه ۱۰۸ رسید.
دبی و ابوظبی نیز هر کدام چهار پله تنزل کردند و به‌ترتیب در جایگاه‌های ۷۹ و ۷۶ قرار گرفتند. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/670498" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ارز اربعین از بازار آزاد گران‌تر است!
🔹
با کاهش قیمت دینار در بازار آزاد به ۱۱۰ هزار تومان، نرخ ارز اربعین به نزدیکی ۱۲۹ هزار تومان رسیده است./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/670497" target="_blank">📅 13:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ژاپن به‌دنبال ایجاد سازمان اطلاعاتی متمرکز با الگوبرداری از غرب
🔹
ژاپن برای نخستین بار از پایان جنگ جهانی دوم، با کمک متحدان غربی در حال ایجاد یک سازمان اطلاعاتی متمرکز است؛ نهادی که گفته می‌شود با هدف مقابله با تهدیدهای فزاینده به‌ویژه از سوی چین و روسیه تأسیس می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/670496" target="_blank">📅 13:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnpTKCH_ayeabqMroPJoQGjPhT-dbtITXPe-toPNfR-QjoZzRROAPHHDIKFruduHIeG0l6ErGMBF8ItKS7U9h-N6vTyATnTmzQeWApIyAAZ4DfcaxkMfA5BWRmKQ06TFB-nKGaHTpKIABBB3zMQW5ecw4ODMOIthyJW6VUEulxtThLKA-J4stxrm331U04-HnqVW3Wyyc7epNp4AIA9VEVsr77HFkGCEirs4IkcPT3-ddl7kF5RhXqEc2yolBhjFelxDKQ9ixI7J8m0M2T3PLVJ-ae9otz6dNv_bVvVtKYGZbxzmScdDGQK9_6G9AqLUdzO2MEaj-VmN4J9pK4-iQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۲ تیر ۱۴۰۵؛ ساعت ۱۳:۱۰
🔹
قیمت دلار امروز در واکنش به درگیری‌های نظامی ایران و آمریکا در تنگه هرمز و انسداد مجدد آن توسط ایران، آرایش صعودی گرفت و در آستانه ورود به کریدور ۱۸۰ هزار تومانی قرار گرفت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670495" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
چین خواستار عبور آزاد و ایمن از تنگه هرمز شد
آناتولی:
🔹
چین در بحبوحه حملات نظامی مجدد بین ایالات متحده و ایران، درخواست خود برای عبور «آزاد» و «ایمن» از تنگه هرمز را تکرار کرد.
🔹
لین جیان، سخنگوی وزارت امور خارجه چین گفت: «تنگه هرمز تنگه‌ای برای دریانوردی بین‌المللی است. از سرگیری عبور آزاد و ایمن در این تنگه در اسرع وقت به نفع همه طرف‌ها است.» /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/670494" target="_blank">📅 13:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
خیلی ساده و بدون هزینه از این دمپایی روفرشی‌های ترند بساز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/670493" target="_blank">📅 13:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670491">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
دارو ۵۴ درصد گران شد
🔹
با اعمال موج جدید افزایش قیمت دارو از نیمه فروردین، میانگین نرخ داروهای تولید داخل ۵۴ درصد رشد کرد.
🔹
در این میان، اسپری‌های دارویی با جهش ۱۶۳ درصدی و ویال‌های تزریقی با افزایش ۱۲۷ درصدی، بیشترین رشد قیمت را ثبت کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/670491" target="_blank">📅 13:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670490">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv_smMJB0AMyqWVXCkIO56WjZ52woMCsFrZObiopj8Qx5AGYgpdWtSt2pqjtLPej9Zi5VM1MMFIGB3AlXCYn8jLfEEtc5hisZcQuJCuJynkVF7iUnAvmJ8En0tie7FAjJzPdf8O6jAHxCBxV7cZZY8Ch8WU6_FR9Le0BXzEYW1HaIRamwtkne5_we_KeN7bWRiXTmEmWC6zPnwsio3Z3_bk_GOAVNS0q80JCqOUQQNldboSOHLGZwu5vAnIddhV69_A-L-87SDiWxTveLRU-QS0LiGwr4Rtxj4EmYgAI_xTXA01P72tqYdIOKb38FKM7eWJi3sCOdOGbjXpzGOUymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر منتشر نشده از شهید محمد ضیف
🔹
عزالدین قسام، شاخه نظامی حماس در دومین سالروز شهادت محمد ضیف، تصویری از او را منتشر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/670490" target="_blank">📅 13:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670489">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
گمرک بازرگان مجاز به ترخیص خودرو شد
🔹
براساس ابلاغیه گمرکی، گمرک بازرگان به فهرست گمرکات تخصصی مجاز به ترخیص خودرو اضافه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/670489" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670488">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b4de78a1.mp4?token=vRzYs_1qQMSAWKaOvqwWa8u4qOiMdVk3OpwACjcqI8f3cgWRAvKKE6c8VQhQHFjjV7ImwGC04HTE71PtCRhvT8EqStOTjkqz7sIxVMC3LCpO3N15_cFlSnZnpg7NxgTN2wbDDDiueRm7Cb2UUbnv8k0gTQ6WEsYm2rbP8aEiJfuOKe0iETwuSSzwQ1XS2hTF6au_6sMx7txWqpWqPYEnQD-ffI3aAO10XO99AFwggStE-pT9-GeTipT3RMMNycdx9xnyhkkwAGBQeStuw4gMXpWDDAkO9n78Fw58FU44jfkY-jpay8Ls-e0mTiZVoHK6_vnd95-OR5LiWl-ijyqoWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b4de78a1.mp4?token=vRzYs_1qQMSAWKaOvqwWa8u4qOiMdVk3OpwACjcqI8f3cgWRAvKKE6c8VQhQHFjjV7ImwGC04HTE71PtCRhvT8EqStOTjkqz7sIxVMC3LCpO3N15_cFlSnZnpg7NxgTN2wbDDDiueRm7Cb2UUbnv8k0gTQ6WEsYm2rbP8aEiJfuOKe0iETwuSSzwQ1XS2hTF6au_6sMx7txWqpWqPYEnQD-ffI3aAO10XO99AFwggStE-pT9-GeTipT3RMMNycdx9xnyhkkwAGBQeStuw4gMXpWDDAkO9n78Fw58FU44jfkY-jpay8Ls-e0mTiZVoHK6_vnd95-OR5LiWl-ijyqoWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات شبانه اوکراین به زیرساخت انرژی روسیه
🔹
در ادامه اصرار اوکراین به زدن زیرساخت انرژی روسیه، تأسیسات نفتی در مناطق استاوروپول و کراسنودار هدف یورش پهپادی قرار گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/670488" target="_blank">📅 13:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای انفجارهایی در حوالی بندرعباس و قشم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/670487" target="_blank">📅 12:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای چین: تردد آزاد و ایمن از تنگه هرمز به نفع تمامی طرف‌هاست
.
🔹
پیش‌ثبت‌نام دانش‌آموزان پایه هفتم به صورت غیرحضوری از طریق سامانه «
مای‌مدیو
» است.
🔹
گرما، جان ۱۰‌هزار اروپایی را گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/670486" target="_blank">📅 12:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
مصاحبه اختصاصی خبرگزاری وایس آمریکا با فرزند شهید تنگسیری و دلایل بستن تنگه هرمز و حمله به کشتی ها در تنگه هرمز از زبان ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/670485" target="_blank">📅 12:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670483">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFHyIzq_SU1iO12Is6FSsWn3t_th5Wt1yEI_ZVB5W3XQR6uIAO2wtqbdoeeQRTYh2SofECwU46uQyiXFcM1KF_P-xF1QmB357BMP5BsuPXqG7636h7xZgddk_et2igxz0PyaNhhHW2rhR6dBXAvvHRG0D6hwgDAoxvxu86XzdegWpHo8DEEnTwreXfPbe2XWHYHVJ_J-TGZIkrF4gZFbK952Doq6UapVXipd8IfqSo-NBtfk1fNlojRbM0MYm7fvZeyjutekkGoT_kf-KPCGpfJHI3jXvzi41DJMCDSfuYc4IM322zAmExUc6XekK4kl2Wr-B3FdMnusax8Mm-qaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkHMAtmPxj-Q7-J5b4CKNTW3FeUICH7Shl8igrlrPVi3842lsIUPUT_1mh0rKC_PCfTiC9lFqlzdX2pyCSzRxpQ3p0nYdLzBX9f6gii0UBqcOK65SjSIlBGKAuMh6vh1FQ6E-4hOTIavo6eLU6bpTqr7Hx1ma8rH-BZICWDzJxZ6Xfcc4gs5OgR5FsaXFFJAMG4MNsWLtK7V1hbZtD0ITm6krLzOtIJUDM6Q20CYOaCoTHU3w-p-_CRQlbF11K2EM1h4kG4bkhZPIBYWLUgFGhZgaa81On5z3irYrsjOsM2qiFwpdOTNnn8GJY553gQOECOf2g5bVZbHO_d52cpKNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آتش سوزی در جزیره خارگ رخ نداده است
تانکر ترکرز:
🔹
گزارش‌های آتش‌سوزی یا حمله به جزیره خارگ تأیید نشد؛ تصاویر ماهواره‌ای نشان می‌دهد افزایش حرارت ناشی از مشعل‌سوزی برنامه‌ریزی‌شده تاسیسات نفتی است که از ژانویه ۲۰۲۶ تغییری نکرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/670483" target="_blank">📅 12:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670482">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
محسنی اژه‌ای: اگر کسی در حاکمیت کار مردم را لنگ گذاشت قابل بخشش نیست
🔹
باید زمینه‌های فساد را از بین ببریم و اعمال فسادزا را خنثی کنیم؛ از ما توقع می‌رود مطالب را درست برای مردم تبیین کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/670482" target="_blank">📅 12:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670481">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf18d1a26.mp4?token=J6skzmq_lB8fAmkdNAnOgkVOZuWIL3itVMzaxSxHsZbLzgB3sGlpP9i4mPWUQbmFv3NZFxWf_XQgbnPr6Pv_VawfytGAS-ipch58u4HXQD1T404zCwDSEjbyllfl2gAQySCIZNPs1KjlMpLrb_Q-muflxcHbtgIs5s5u0ryf3RoKSerme0u9rdvZProm4ElK3iaRpl3vAt8gMhIqRRZ5tyjK-eFT6zhOrAhSjkQiPCk9Gy01jtZ72Rgb9NtYDnEM23aLJmHPJSJ9AAPWFPXPYY3M2axrLbYqk3xO20pVxz5X8QjFQzBchKBm0pnYs4j5jNBsOPJHZV0ZV0YAxAM_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf18d1a26.mp4?token=J6skzmq_lB8fAmkdNAnOgkVOZuWIL3itVMzaxSxHsZbLzgB3sGlpP9i4mPWUQbmFv3NZFxWf_XQgbnPr6Pv_VawfytGAS-ipch58u4HXQD1T404zCwDSEjbyllfl2gAQySCIZNPs1KjlMpLrb_Q-muflxcHbtgIs5s5u0ryf3RoKSerme0u9rdvZProm4ElK3iaRpl3vAt8gMhIqRRZ5tyjK-eFT6zhOrAhSjkQiPCk9Gy01jtZ72Rgb9NtYDnEM23aLJmHPJSJ9AAPWFPXPYY3M2axrLbYqk3xO20pVxz5X8QjFQzBchKBm0pnYs4j5jNBsOPJHZV0ZV0YAxAM_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مسیر پیاده‌روی اربعین از بصره تا کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/670481" target="_blank">📅 12:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670480">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbVFu8l9Jriq8g6zR0IA0ytCNSK-Wmhe_joPAjr72ApctTprHuJQcbQGLyaSJ6aYDnqSg0otXSlo0uYjQHzk8WF_F4_NOYsfiNYcr88ZGQk-Co6RYez9R6B0iy7HGxc07aMI6Z7GjXOTfJm72m8_FrZCm6sk-BRYRWO7SQSw6EFigbfIt9lAa2AbgDCppUyUQIkvAMZTCdetQYtHgs4HRuX_xWONEjlNb1cjBgJAGBTzFF9au2ExkDzEVOeP8Ns0wCDIPigMkGn33jxJKYftH2HrbaAfeHiHQ3O2_CsMWYa4t4ObyHTy06O2WM-rAwh-b7ohIdAUz9AQwCJCtMi12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش بورس به زیر ۵ میلیون
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۸۹ هزار واحدی به ۴ میلیون و ۹۶۷ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/670480" target="_blank">📅 12:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670479">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
جزئیات از حمله ارتش تروریستی آمریکا به تاسیسات آبی خوزستان
🔹
مدیرعامل سازمان آب و برق خوزستان از حمله بامداد دوشنبه ۲۲ تیرماه به ایستگاه پمپاژ زهکش RMD در محور ماهشهر–هندیجان خبر داد. در این حمله، «شاکر محیسنی» به شهادت رسید و یکی دیگر از کارکنان مجروح شد.
🔹
این ایستگاه نقش حیاتی در مدیریت زه‌آب اراضی کشاورزی منطقه دارد./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/670479" target="_blank">📅 12:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670478">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5RqR4vsBh9PoFd76zEZiRkD59sBiB1aeEUq3aGQURTcLQFy59jgN7W8aATgAiY9hg2lEqYLW-fLRNklBbLsar9De0TfCOESrVcg0k00yOd5Vi9yVsTJNFzO_X5Up9lgRkYx3vKyO0G_zIrpjLUHoCV1kYl5OoIXEUSQ0G6laErkqQFQDCrIyPfk1iNQtAJtQgn7wwFvam8vmDi8dndz1FeqQKj0H8u0p6-y_1fF6kpowD2DkNbJKbXRP2OC_EeADgOSRXU-q1oxVpkA2AUP40_pYEG2_iI3Qt779CCpz475tGiODfDxcpGao-oIL9AyYQp81R-C8MGS4c434YjESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت بحرین دو نوجوان را به جرم شرکت در عزای حسینی مجرم شناخت و زندانی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/670478" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670477">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33e67c24d.mp4?token=b3xHVnJHNP5laLsCKKkpvzxPegD5asQ-uFPKoxnjd8HiRH2DJWLR44vqsbIo3ZX4Y7BIbBk3qtnEd5o0piP1vRRZ8Qsya6Q3tqfOXQQtFjz3g3NpWl7qVIlCsXQj3yA9csuKeIEnND_7lYtgzbqRt9t1WoUgSxDnMC2o87Te5WvR1hsCWOEW4mZf5meS9PpbxZ2reGYEcSJjE1CvLVmj2VNLMQENUTNRCCf8KqmugWDXZS26dWfYInS519HPKOc4hPS-9laqcud7wwfnVybjGCtdeYbS_1mxTzpxDhggmLDrziCUANncpbPE3ZpRnNMqUf97whMz1cQSdZjGEGL8yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33e67c24d.mp4?token=b3xHVnJHNP5laLsCKKkpvzxPegD5asQ-uFPKoxnjd8HiRH2DJWLR44vqsbIo3ZX4Y7BIbBk3qtnEd5o0piP1vRRZ8Qsya6Q3tqfOXQQtFjz3g3NpWl7qVIlCsXQj3yA9csuKeIEnND_7lYtgzbqRt9t1WoUgSxDnMC2o87Te5WvR1hsCWOEW4mZf5meS9PpbxZ2reGYEcSJjE1CvLVmj2VNLMQENUTNRCCf8KqmugWDXZS26dWfYInS519HPKOc4hPS-9laqcud7wwfnVybjGCtdeYbS_1mxTzpxDhggmLDrziCUANncpbPE3ZpRnNMqUf97whMz1cQSdZjGEGL8yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جورج گالاوی، سیاستمدار مطرح انگلیسی: لیندسی گراهام مسئول ریخته شدن خون میلیون‌ها نفر است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/670477" target="_blank">📅 12:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670476">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKYy73x7kQO4xuD9Ogt0UzK1BjltTQWxxrxWUzn1kb4UHyGI0h4oApvOWnq-0jCTHmxHPtbt52PxnBwsQ0LjUeS-zwe1I2oDDiG4RF5sqkt0cwuxnfF5JamjiUYzaoZQ2Z60DyOuZpZR1IOLM69uscERdFYbbQst4D9HOWcbRUB1vcGKD27My0VrJXTR6mCgmHHX7IpcLvvQUFrxcbRDjQgheQ1NTG07c0_owocOcELeUCNBz-9k368hjRLnV03h3gnmtN4lRQapHrNzRctUo3gAA-47o9hZYamtQcHSlFENYGIArVmWHJ3sMDM_yf0yfVbPD-tDFvsym2nN16_eaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سم نیل، ستارهٔ پارک ژوراسیک، درگذشت
🔹
سم نیل، بازیگر سرشناس نیوزیلندی که با نقش‌آفرینی در فیلم‌های ماندگاری چون «پارک ژوراسیک»، «پیانو» و ده‌ها اثر سینمایی و تلویزیونی به یکی از چهره‌های محبوب هالیوود تبدیل شد، در ۷۸ سالگی درگذشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/670476" target="_blank">📅 12:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670475">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حمله دشمن به منطقه‌ای در محدوده شهرستان نایین‌
معاون امنیتی انتظامی استاندار اصفهان:
🔹
در دقایق اولیه بامداد امروز دوشنبه ۲۲ تیر، حمله دشمن آمریکایی به منطقه‌ای در محدوده شهرستان نایین، یک شهید و هفت مجروح در پی داشت.
🔹
مجروحان به‌صورت سرپایی مداوا و اوضاع تحت کنترل است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/670475" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670473">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QghoFsjUwxpfJApow3DikuaJpAh08sE4IaW_1MAWMxpZaHBslytJrXZ-j8sqY2QlvOjSfHaswrN_BSl4rKexesnekcKTf4GAKSSkwK3ryuGxkJCjGR6dSM6E-o7YcDZ4GiHki_s9XFpaDPywQ5pv5gG2MJTuPh984O-EVxhC1_AWK16a-Vovb1WUSTFiSGqCXPw_uf02h0w6PZIPUvo-7a6JceNj_8BVKcqh6WyPjDgaIDnt1GRxTlVQfZ-eVbmqhpwRxjS6Ll4so-Q9BIlWZqImpnR1HvI2AoGrHewEVGacRe_AomcOIPsnCreBH14SG1ZwyuQRE1tZ0gvinrEJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران کدام نقاط کلیدی آمریکا را زیر ضرب برد؟
🔹
در پی نقض بندهای تفاهم‌نامه، ایران مجموعه‌ای از اهرم‌های اقتصادی و نظامی خود -از انسداد تنگه هرمز تا هدف قرار دادن مواضع زیرساختی، لجستیکی و کنترل دریایی آمریکا در منطقه - را فعال کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/670473" target="_blank">📅 12:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670472">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بقایی: سفر لاوروف به تهران در حال برنامه‌ریزی است
.
🔹
توزیع کارت آزمون ارشد آغاز شد.
🔹
علی‌اف: روابط میان آذربایجان و روسیه عادی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/670472" target="_blank">📅 11:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670471">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3914cfc6.mp4?token=ekZ82yKXSNAYh5J9k2K3V85EeoHA4CMu50SXq8EY36mLeC6egO1PCdxVD9apTXJt9nn7oV1pgpO5LTY3iH5KT6bKM8EHIKzv1B6D3FsAoeQtsXbfLjy97RXtx6aUGXmy3_iLU8e2-3WU1VNhK-ThTiW7DspMI9vSqdBLGLJ03ZNqPeY0pkr426XEMB46QFooru6xxssiPgArqcaF4ZXewXa_iqRNKv5iLtnDcw1hXoq5gvL4YWLLTokJWS-FuhWrsX9fuGDymCcG1621QA7CmnGk_XVSDEbvTlbrYeX720O9q4frQ9OYhBURRiPCic040VhtMqfZoF6kAbAO-OtiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3914cfc6.mp4?token=ekZ82yKXSNAYh5J9k2K3V85EeoHA4CMu50SXq8EY36mLeC6egO1PCdxVD9apTXJt9nn7oV1pgpO5LTY3iH5KT6bKM8EHIKzv1B6D3FsAoeQtsXbfLjy97RXtx6aUGXmy3_iLU8e2-3WU1VNhK-ThTiW7DspMI9vSqdBLGLJ03ZNqPeY0pkr426XEMB46QFooru6xxssiPgArqcaF4ZXewXa_iqRNKv5iLtnDcw1hXoq5gvL4YWLLTokJWS-FuhWrsX9fuGDymCcG1621QA7CmnGk_XVSDEbvTlbrYeX720O9q4frQ9OYhBURRiPCic040VhtMqfZoF6kAbAO-OtiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما در فرایند دیپلماسی دست‌بسته نیستیم و استفاده‌هایمان را از این زمان کرده‌ایم و خواهیم کرد
🔹
می‌دانستیم که آمریکا پیمان‌شکن است و با علم به این موضوع و با چشمان باز از ابزار دیپلماسی استفاده کردیم.
🔹
مردم ایران تجربه تلخی از پیمان شکنی آمریکا دارند و برای ما دیپلماسی یک ابزار است و مردم ایران حامی تصمیم گیرانشان هستند؛ شیوه و کیفیت مذاکرات دیدگاه طبیعتا متفاوت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/670471" target="_blank">📅 11:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670470">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f188a0d7db.mp4?token=qGKulgnFLHL1tzRI386G762SObRWlrf5BJNHqulf5onGmyM6tPtMPhUfJr22S2p7Y7-CEqfF_mKt9sKBImh9_0CvxXhavyoP_6f--aJsLn7q3omTyCWEMG7_q3UrkJkLIg-nbfYygQMMl069MDZRcHeb41pDr6BShzmdGeH9kRzJdBCl4GyahZdsSPU_HXyGfNQ30U5ETrH9oNxfIFVE0pnkxGdjwLiTFZd3hA7IuyxJ1Re9FqLjmOC2B6iBO9_3TCWK160yzoMWDbgbwpzgP19WpliYIzKnMGuLB5N3oanYX1pqM8CWEvKfyeB_VUiesrp-d2QKtti_1e-YL7_jwSkPiJFL1O1K4tkWSTyM4atxmkE_3kS9XL5bHwwBbKxlptZk2k53ESmesQ62R8uwSzZcQ9WmBrhRPL98WNwMM8hsZpLhnaE5T5NStQB42aZEqWElV9Ds-uGnaBxlnGGtX5wb_X6QDCwXOP-aoYGs_SqL0WnFmjE13X_9prQPtoSlBotxuat5R8Yi5g70HEsj-UM9k0JIPWBf3dD42UuuO-7ld2Jsru-cRX-m1m3gD2U4wSirl27iyGGVi3G2rdQidVNr1THRbT2_a_O-qAT5E1PXcNp6_mGWuu_A5q2IMptWRZ8UICPh9GxxMQ1Xpv6PeAJktsQgIFOxubRukIK1jbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f188a0d7db.mp4?token=qGKulgnFLHL1tzRI386G762SObRWlrf5BJNHqulf5onGmyM6tPtMPhUfJr22S2p7Y7-CEqfF_mKt9sKBImh9_0CvxXhavyoP_6f--aJsLn7q3omTyCWEMG7_q3UrkJkLIg-nbfYygQMMl069MDZRcHeb41pDr6BShzmdGeH9kRzJdBCl4GyahZdsSPU_HXyGfNQ30U5ETrH9oNxfIFVE0pnkxGdjwLiTFZd3hA7IuyxJ1Re9FqLjmOC2B6iBO9_3TCWK160yzoMWDbgbwpzgP19WpliYIzKnMGuLB5N3oanYX1pqM8CWEvKfyeB_VUiesrp-d2QKtti_1e-YL7_jwSkPiJFL1O1K4tkWSTyM4atxmkE_3kS9XL5bHwwBbKxlptZk2k53ESmesQ62R8uwSzZcQ9WmBrhRPL98WNwMM8hsZpLhnaE5T5NStQB42aZEqWElV9Ds-uGnaBxlnGGtX5wb_X6QDCwXOP-aoYGs_SqL0WnFmjE13X_9prQPtoSlBotxuat5R8Yi5g70HEsj-UM9k0JIPWBf3dD42UuuO-7ld2Jsru-cRX-m1m3gD2U4wSirl27iyGGVi3G2rdQidVNr1THRbT2_a_O-qAT5E1PXcNp6_mGWuu_A5q2IMptWRZ8UICPh9GxxMQ1Xpv6PeAJktsQgIFOxubRukIK1jbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف‌های بی پرده یک روحانی: بسیاری در لباس روحانیت زندگی یک نسلی را نابود کردند و وجهه دین را نیز خراب کردند
/ تلویزیون اینترنتی مدار
این گفت‌وگو را در آپارات ببینید
👇
▫️
https://aparat.com/v/qypc186
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/670470" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670467">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecf0c49d7.mp4?token=IUdogZg9PKns1okdzWktQpijpuOwgtA79-wxtDuz5GXK5hkUCf4Lz8aV3z9-UzuXlITFHwyA8Re4qVuxYg2cO9o-fGcVvmldxhGginUw_FMhBSAU_1iuMZYhfnv5IwvJKgCEh06RkQN-ikkB0vtUCRSrhLubnOJ6wpmSFN9P6OaxP3JUEXsrgqFr2roPXkael-hDRSuZRShb1o0N1u8uOjs0ofk6-aVN2iKWkqXfhBphrZ1TAl0T726eyd_Pc2Y1x5e40J19e8sVHOSnqayUBnh9hiaDpp2fcW7hI0qyZZHzefqCcuEDQH5_N2ta3M62GdQ2QJ6ZoTQ_nVehbN-eFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecf0c49d7.mp4?token=IUdogZg9PKns1okdzWktQpijpuOwgtA79-wxtDuz5GXK5hkUCf4Lz8aV3z9-UzuXlITFHwyA8Re4qVuxYg2cO9o-fGcVvmldxhGginUw_FMhBSAU_1iuMZYhfnv5IwvJKgCEh06RkQN-ikkB0vtUCRSrhLubnOJ6wpmSFN9P6OaxP3JUEXsrgqFr2roPXkael-hDRSuZRShb1o0N1u8uOjs0ofk6-aVN2iKWkqXfhBphrZ1TAl0T726eyd_Pc2Y1x5e40J19e8sVHOSnqayUBnh9hiaDpp2fcW7hI0qyZZHzefqCcuEDQH5_N2ta3M62GdQ2QJ6ZoTQ_nVehbN-eFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب بقایی به اظهارات وزیر امور خارجه فرانسه درباره ایران
🔹
وزیر امور خارجه فرانسه دوست دارند هر از چندگاهی صبحتش در نشست سخنگویی انجام شود.
🔹
فرانسوی ها باید یاد بگیرند درباره مسائلی که به آنها مربوط نمی شود انتظار نقش آفرینی نداشته باشند.
🔹
اروپایی‌ها نباید رویکرد مهدکودکی خودشان را به دیگران تسری بدهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/670467" target="_blank">📅 11:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670466">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e81135af.mp4?token=BDOqjrpI9pkVzRaMKYBcvwBohoOoVCSayRmsfvw8Kh5ggRUG2hvdiuXjnWhaa_w4jiisufILdFdEfefiWeH1Ygm96eOxDG4s82jdj6sOB7uWaL0vbdLEsgEvGX3Wd5Tbh8-6F8ZzJzmpFuyEIaZAClHzDFNjRq0sNCAxL1z8TyGxDnHiHuzOayhA3tgJJZ2aiRcaTxy-YyoVN5gwOjDqMYEgzZi3eAwnnuMHlVU3YbXAdHpuu_evmnVGFVmoWnrtCtjRa_kczf2XwVyib-ABxFZdlyedyY6gFsTxe7bm6AEZDzjThFonCV-voNv1zoF07QTxx02aQEeoqvVmt7tD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e81135af.mp4?token=BDOqjrpI9pkVzRaMKYBcvwBohoOoVCSayRmsfvw8Kh5ggRUG2hvdiuXjnWhaa_w4jiisufILdFdEfefiWeH1Ygm96eOxDG4s82jdj6sOB7uWaL0vbdLEsgEvGX3Wd5Tbh8-6F8ZzJzmpFuyEIaZAClHzDFNjRq0sNCAxL1z8TyGxDnHiHuzOayhA3tgJJZ2aiRcaTxy-YyoVN5gwOjDqMYEgzZi3eAwnnuMHlVU3YbXAdHpuu_evmnVGFVmoWnrtCtjRa_kczf2XwVyib-ABxFZdlyedyY6gFsTxe7bm6AEZDzjThFonCV-voNv1zoF07QTxx02aQEeoqvVmt7tD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امورخارجه به ادعای ترامپ درباره درخواست ایران برای مذاکرات؛ طرف آمریکایی صادق نیست و یک بازی روانی است
بقایی:
🔹
ایران با میانجی‌ها در تماس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670466" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670465">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
نیوزویک: ایران ترور ترامپ را برون‌سپاری می‌کند!
ادعای نیوزویک:
🔹
تلاش‌های ایران برای ترور در خاک ایالات متحده معمولاً شامل برون‌سپاری واسطه‌ها می‌شود.
🔹
تهران به جای استفاده از عوامل آموزش‌دیده خود برای حمله، از منابع خارجی استفاده می‌کند و واسطه‌هایی را برای استخدام شبکه‌های جنایی محلی یا افراد مسلح اجیر شده می‌فرستد که امکان انکار را فراهم می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/670465" target="_blank">📅 11:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670461">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9610fe89.mp4?token=Os-taGKIvTf-NJDwcbniHge1989TB4WpN8dqHDcdTyzqaHg-7KreZYwJ1VrhNN851UIUSGPP0HH-z3GwGpl0lwG0rPWdKBaluh3jYFhJrxvrCHAc4dkdxDrc5CFQT8Wz1pVE-mDsXons4aY6hopMAKcDd-5XS6D17A8kQYiAFAMZ4bf9L8WA8-oYRG8YqQV_FeKsGXAHcOTUWWVOBHfz0amkdV9oTlHM1hHd4rI5PA3A64wTglghMnd0Qnh_X8sgfSNsCEy0BdxuTuHYsBGdnuIwcZLWeXfGUs1zFW7pnupni2UI163Asg0GrZs6jjn6gsck939A3c8YUEYsye_sFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9610fe89.mp4?token=Os-taGKIvTf-NJDwcbniHge1989TB4WpN8dqHDcdTyzqaHg-7KreZYwJ1VrhNN851UIUSGPP0HH-z3GwGpl0lwG0rPWdKBaluh3jYFhJrxvrCHAc4dkdxDrc5CFQT8Wz1pVE-mDsXons4aY6hopMAKcDd-5XS6D17A8kQYiAFAMZ4bf9L8WA8-oYRG8YqQV_FeKsGXAHcOTUWWVOBHfz0amkdV9oTlHM1hHd4rI5PA3A64wTglghMnd0Qnh_X8sgfSNsCEy0BdxuTuHYsBGdnuIwcZLWeXfGUs1zFW7pnupni2UI163Asg0GrZs6jjn6gsck939A3c8YUEYsye_sFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◼️
بدرقه یار
◾️
پیام‌های صوتی مخاطبان خبرفوری در پویش «بدرقه یار»، آخرین جمله به رهبر شهید؛ بازتابی از ارادت، دلتنگی و وفاداری مردمی است که حرف دل خود را با رهبر شهید در میان گذاشته‌اند.
◾️
این صداها، بخشی از بدرقه ماندگار ملتی است که در سوگ، همدل و در وفاداری، هم‌پیمان مانده‌اند.
◾️
کانال رسمی سوگواره «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/670461" target="_blank">📅 11:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670460">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39700be49e.mp4?token=CtHOqgbjBEc73qRoQJ7psqb3cSDDcBzXTf8v2OOUR_X_Pn3ab7qOp6UERAfhqYLeiRyy1SSAFr7ZCc7X7jaVCRDu3N_59w0KWmYtNK_HWcc59eIrnjW9QX413pkUq7o42owC3y0W9CCT-RBpgBOBmOrS0Kxy6N4MgnfYL9JLPvRatyMG_WXbU3RgA_oggWMyBeUS_sWQs4Z2j_6OCLsFWNtz3rSnW9R55kaKFKeKqyQ2amFbnxHuZwQ3PCkT2o-D425rDTYNfoG_LC13avDmmGCN-3kbvsj2edNZYidOasm1M5CKbfT4V2jOKasyKp4f8m0sABjuk0lCUesU66vUbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39700be49e.mp4?token=CtHOqgbjBEc73qRoQJ7psqb3cSDDcBzXTf8v2OOUR_X_Pn3ab7qOp6UERAfhqYLeiRyy1SSAFr7ZCc7X7jaVCRDu3N_59w0KWmYtNK_HWcc59eIrnjW9QX413pkUq7o42owC3y0W9CCT-RBpgBOBmOrS0Kxy6N4MgnfYL9JLPvRatyMG_WXbU3RgA_oggWMyBeUS_sWQs4Z2j_6OCLsFWNtz3rSnW9R55kaKFKeKqyQ2amFbnxHuZwQ3PCkT2o-D425rDTYNfoG_LC13avDmmGCN-3kbvsj2edNZYidOasm1M5CKbfT4V2jOKasyKp4f8m0sABjuk0lCUesU66vUbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ منفی سخنگوی وزارت امورخارجه به ادعای گروسی مبنی اجازه ایران به آژانس برای دسترسی به تاسیسات هسته‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/670460" target="_blank">📅 11:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670457">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152f9f93c8.mp4?token=YU0D_8yNe_5ZK4M0L7mDyYIyLoR0Etk1G2EDf5Jst3lP0yFOW74q5f2hC1FH7TtrbTDlovWFxCzsPT6ROl3ouKfP74Sy-rT3CQbgsCOPZmyJBEuvGyEMT-LNQ8RhJzJKUtHBLeOlsGyujO1jV1AVHopDiy6W-tG97TASYTZmTGpEmoStQaMmij2zR_o5cD8s8Bf1E9ulVyX-MLCBO8SEwJYT4P07bElZSZbDte-iomwUGqYdcgkAMQSOAlBREmAtMx7QpjcXgvcTrrMJxmDiRn3E0qmc8_S2AXFjwtKCu2JNWiJ_mf0ztVEHFCg0M36YmSC_eqdWgc1CsblvFDm9nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152f9f93c8.mp4?token=YU0D_8yNe_5ZK4M0L7mDyYIyLoR0Etk1G2EDf5Jst3lP0yFOW74q5f2hC1FH7TtrbTDlovWFxCzsPT6ROl3ouKfP74Sy-rT3CQbgsCOPZmyJBEuvGyEMT-LNQ8RhJzJKUtHBLeOlsGyujO1jV1AVHopDiy6W-tG97TASYTZmTGpEmoStQaMmij2zR_o5cD8s8Bf1E9ulVyX-MLCBO8SEwJYT4P07bElZSZbDte-iomwUGqYdcgkAMQSOAlBREmAtMx7QpjcXgvcTrrMJxmDiRn3E0qmc8_S2AXFjwtKCu2JNWiJ_mf0ztVEHFCg0M36YmSC_eqdWgc1CsblvFDm9nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ایران دولت فعلی افغانستان را به رسمیت شناخته است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/670457" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670456">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4368a18b89.mp4?token=BSRBfx7CM5V3EJnYhSexkShUq--h6zacgORQzw4-xErKEIvGBh0R4DxRJSnvfF-HtShrzrntAFMKR1R1siQR0-fZTipeyBsHZWu1LjQdTlHlFnRiKEPI8M4FRvdDo29CXvCN2aleB4PvBqIp-ujF8EeFfv62VrXp2w1zPnyAkaWlXzlgpEE_uHtQC7qfg7_dxAa5AZDyePIgw_4eh8Omr1j4RilSjus0_l2XygXPETYSK9WGvG7gkGCsCvTLLG2fcwHC08AquttXZg0dvgtHldOU6va4EseYuyKHZiLfVUpZTbDG1LWsWpjcpTIwZWikk5a7mdV7KFMdzGFNR0MRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4368a18b89.mp4?token=BSRBfx7CM5V3EJnYhSexkShUq--h6zacgORQzw4-xErKEIvGBh0R4DxRJSnvfF-HtShrzrntAFMKR1R1siQR0-fZTipeyBsHZWu1LjQdTlHlFnRiKEPI8M4FRvdDo29CXvCN2aleB4PvBqIp-ujF8EeFfv62VrXp2w1zPnyAkaWlXzlgpEE_uHtQC7qfg7_dxAa5AZDyePIgw_4eh8Omr1j4RilSjus0_l2XygXPETYSK9WGvG7gkGCsCvTLLG2fcwHC08AquttXZg0dvgtHldOU6va4EseYuyKHZiLfVUpZTbDG1LWsWpjcpTIwZWikk5a7mdV7KFMdzGFNR0MRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: به هیچکدام از کشورهای منطقه حمله نکرده‌ایم
بقایی:
🔹
کشورهای منطقه از وضعیت ۴ ماه گذشته که به‌دلیل حضور آمریکا به چالش کشیده شده، درس بگیرند!
🔹
مقایسهٔ ایران و رژیم صهیونیستی توسط وزیر خارجهٔ ترکیه حیرت‌آور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/670456" target="_blank">📅 11:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670454">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8effe0eb.mp4?token=OrDkf7mgW3_gNjC1qKGZAOy-ArjRLF9ekaCgJ7HkB0nrVCchJi0T1pNqcBAULFSlmQa5c6mH727dMwYix2yolWaHqHKA1uBRdQmJ9NzODkUaiEvzVP4tBeyrWZ1YpJ2jjItKlcfInESidpm5pwAq3U0sylOj5R5CaJG6NBSOS83SH-V_MSjodPNuqUpTF6rDgmRb2DXIuLkDQHQcKZ6AWQtJ-VQGiktrqp2tzvZSUXCYlnlW11sPvVwad4CrDkad5-ULI_fSbZ-xmZgKMFYo8TIFeJM-5abKUHdL8zhVIqZ5T6sGl3l3z5muZzlkW0V6uKeiEg0F7PJOthF2ayXHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8effe0eb.mp4?token=OrDkf7mgW3_gNjC1qKGZAOy-ArjRLF9ekaCgJ7HkB0nrVCchJi0T1pNqcBAULFSlmQa5c6mH727dMwYix2yolWaHqHKA1uBRdQmJ9NzODkUaiEvzVP4tBeyrWZ1YpJ2jjItKlcfInESidpm5pwAq3U0sylOj5R5CaJG6NBSOS83SH-V_MSjodPNuqUpTF6rDgmRb2DXIuLkDQHQcKZ6AWQtJ-VQGiktrqp2tzvZSUXCYlnlW11sPvVwad4CrDkad5-ULI_fSbZ-xmZgKMFYo8TIFeJM-5abKUHdL8zhVIqZ5T6sGl3l3z5muZzlkW0V6uKeiEg0F7PJOthF2ayXHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: آمریکایی‌ها از روز اول تقلب کردند
سخنگوی وزارت امور خارجه:
🔹
آمریکا با تحریک کشورهای منطقه سعی کردند مسیر امن تنگه هرمز را دور بزنند و بند ۵ یادداشت تفاهم را نقض کردند و امنیت کشتیرانی را در منطقه به خطر انداختند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/670454" target="_blank">📅 11:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670450">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb5b272db.mp4?token=q8uXDOoW5SSYOne_ENVuGldz-UldNLYGe0qpr2_n7UQaYorNtrDLP8KM223wPKA2qcNqHVgRGYAnjISKbwoe4pDhFAzbiZVHRSHQ85I7FXzAha6ZFevA3ykZqV38B3vYA3K9QrDY-9Y7YkhU1J26YGP1SDmS1D2pithtXLGb4BvZLZVyZ4ZNccwNyI_biZEqYu_764_Ya2CKzt-UFPmQrM8xcTUNeQ3a6-qpIg-12VK3YARy8ut0-sq0D3QbdRr9PU4k9qhzb1YHopprvxD0v-7ZKJdXTLvRQG7CdSNBGt0ZXGlcMffH8azsh3qr4tyYzuLyBsm-MRySoq1EOngNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb5b272db.mp4?token=q8uXDOoW5SSYOne_ENVuGldz-UldNLYGe0qpr2_n7UQaYorNtrDLP8KM223wPKA2qcNqHVgRGYAnjISKbwoe4pDhFAzbiZVHRSHQ85I7FXzAha6ZFevA3ykZqV38B3vYA3K9QrDY-9Y7YkhU1J26YGP1SDmS1D2pithtXLGb4BvZLZVyZ4ZNccwNyI_biZEqYu_764_Ya2CKzt-UFPmQrM8xcTUNeQ3a6-qpIg-12VK3YARy8ut0-sq0D3QbdRr9PU4k9qhzb1YHopprvxD0v-7ZKJdXTLvRQG7CdSNBGt0ZXGlcMffH8azsh3qr4tyYzuLyBsm-MRySoq1EOngNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آینده تفاهم صلح اسلام آباد چه خواهد شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/670450" target="_blank">📅 11:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b85f616b.mp4?token=K9LzYxgz9hCJnOG41iqgdSz1Oy4Pol75nPrLQxbbLh9BwpN9K5L8s0pNXRcYBCWpnhVLXwAHMMNluOQ-52ibU0N1liKfCoaAtaez0LZMWDfwK2Cik3VG8t213slX6gWM-Gw-SrqOX_j7MZrlMV1MetrzhxGSWXNBCR6drEIX5I5is8AtZkBgR2phTJrCO9ua9-w76y_mdRsSY6Q9vbcj_ewHlAME3iclCGU7jKKmiz0m3I3JpEq4nfJL-7pxlLiFftCzJDGx-WihYUx8iYsvUWpv5NkZJAHwnwHmd5x0gSuakob77jzNPinlq8OlNpc2f2C-SXgn6tmYVk2csl-NQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b85f616b.mp4?token=K9LzYxgz9hCJnOG41iqgdSz1Oy4Pol75nPrLQxbbLh9BwpN9K5L8s0pNXRcYBCWpnhVLXwAHMMNluOQ-52ibU0N1liKfCoaAtaez0LZMWDfwK2Cik3VG8t213slX6gWM-Gw-SrqOX_j7MZrlMV1MetrzhxGSWXNBCR6drEIX5I5is8AtZkBgR2phTJrCO9ua9-w76y_mdRsSY6Q9vbcj_ewHlAME3iclCGU7jKKmiz0m3I3JpEq4nfJL-7pxlLiFftCzJDGx-WihYUx8iYsvUWpv5NkZJAHwnwHmd5x0gSuakob77jzNPinlq8OlNpc2f2C-SXgn6tmYVk2csl-NQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: بی‌تردید تفاهم‌نامه وارد مرحلهٔ بحران شده
سخنگوی وزارت خارجه:
🔹
آمریکایی‌ها در پیمان‌شکنی این‌قدر کم‌صبر بودند که حتی اجازه ندادند بازهٔ یک‌ماههٔ تعهدات ایران دربارهٔ تنگهٔ هرمز تمام شود.
🔹
ما در مسقط صرفاً دربارهٔ تنگهٔ هرمز با عمان مشورت کردیم و اصلاً قرار نبود موضوع دیگری مطرح شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/670449" target="_blank">📅 10:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866026ebb3.mp4?token=sLbDCaFQ8RMjnA8WTzwOM2twj69AHMzBmlAQkhcunqQwL9O-xPM6bPvUkQb2gsMZOLeBN1xXfxoVicPQkO3_lauAdOJOxx3qsvzASAJchSZB9ZTwekIi6U6Mw1glxlUqFj8PaK2ug6uQgek98f-YZqu8MGmYtO0Pt3ShFlEwbERljLswS_e7MKecL65y7_Amz67OTzHMwMOcA7-cvxzTg8-JeJdFXoYsE6khpAUu1GIKfM_JFygPch-6voQ2VehydgrSidZhvfvjBnFuN2QOy5Z0REBSj77poDoJ_qKQYbQoWpECZuiDfk5E4rhdfMAXHIRLo7NGDHoJq9oJhze9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866026ebb3.mp4?token=sLbDCaFQ8RMjnA8WTzwOM2twj69AHMzBmlAQkhcunqQwL9O-xPM6bPvUkQb2gsMZOLeBN1xXfxoVicPQkO3_lauAdOJOxx3qsvzASAJchSZB9ZTwekIi6U6Mw1glxlUqFj8PaK2ug6uQgek98f-YZqu8MGmYtO0Pt3ShFlEwbERljLswS_e7MKecL65y7_Amz67OTzHMwMOcA7-cvxzTg8-JeJdFXoYsE6khpAUu1GIKfM_JFygPch-6voQ2VehydgrSidZhvfvjBnFuN2QOy5Z0REBSj77poDoJ_qKQYbQoWpECZuiDfk5E4rhdfMAXHIRLo7NGDHoJq9oJhze9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: خون‌خواهی رهبر شهید ایران یک مطالبه است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/670448" target="_blank">📅 10:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d0736354.mp4?token=TBzh1jSdaGpTHK0mEE0pnvfyLh-ET63eoVT1WL8vFdrqWujHz72GJwOfNB0gvRi3IspKAPPjV6dWjzdHxIk0ynJOEb3FAmE54AOAiwgESAaCkcP55H2RufVJtkHyG5OvHlEZEge6NQlgaixfQ3yFxEhKEeZbsWqVPlGqCG-jGbaVeFVqs6RSyHlJFc8atngZglEb9epiMFUamgen6_6Aud3gPfUxjHb7UzgFnoPgSNUHrpnELIj3edckRQ8M5LIjIoXJ6fpcV975eLt_gTY-uE1w_cCBWp8YNsb4oDpVO7-u3LuDC81XaN2n7TqYaL25g3Xu_uvtbuNDoQVS5wycLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d0736354.mp4?token=TBzh1jSdaGpTHK0mEE0pnvfyLh-ET63eoVT1WL8vFdrqWujHz72GJwOfNB0gvRi3IspKAPPjV6dWjzdHxIk0ynJOEb3FAmE54AOAiwgESAaCkcP55H2RufVJtkHyG5OvHlEZEge6NQlgaixfQ3yFxEhKEeZbsWqVPlGqCG-jGbaVeFVqs6RSyHlJFc8atngZglEb9epiMFUamgen6_6Aud3gPfUxjHb7UzgFnoPgSNUHrpnELIj3edckRQ8M5LIjIoXJ6fpcV975eLt_gTY-uE1w_cCBWp8YNsb4oDpVO7-u3LuDC81XaN2n7TqYaL25g3Xu_uvtbuNDoQVS5wycLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت رژیم صهیونیستی پس از به درک واصل شدن لیندسی گراهام
باید بسیار نگران بود، ایران از اجرای سیاست «چشم در برابر چشم» سخن می‌گوید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/670444" target="_blank">📅 10:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670441">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b64e8341f.mp4?token=Qe-8GRj0dJpoP-m2FLQ2rXPyLTDiRK_BlCm21xKU3v-oB_8urnJbUZZ7m4luYAdaCNsHaqh5Wp3hdSO_uRIMOAPzTIJCOBm6vvH8rL-BFWctmyTauxNDTcuFFEt1Y5U_p4z12Mh58U9-3JGpFWkXlJpgX4BMG16XHLsEkzZZP2B-lQxiit9F1JfwmwqShHW2RBQZc4ITyrWgdT6G6BAcunEgfeBJo6l_OBeplQI-LtA8PmT1R2wBK0cMSlrlXC7P2nPoJ70-As1FCCWrekS0RuofCCynOK2-f6O1TfztoV3mQ7UY56bFNuMZVPsr_o49UUVPPmTL5wTdoMH5G1AcHrAFFtRQ5OFq_DZwkt0XAzRffOxK_lzEFXRsfekf0hKpg7u3Miecr3TRS5KCyxdkvdhRDAVtdx8gh5ew5TDFFJnUf0PZQg-ybg1ZaZdY0IDbkp41b3AmJtbVUnP3bnf1BSkaFpErdqLSoHof2BaEA3dMFUSJx-v8tvjzjkZo3_59YVrsss-W7HnHi2o0fH-JLkxvKufQslnZJqwQuo7Xfn9Vo4fl6Lf2ZvE0C78SOeo6ypjN5GhLmCpQ74Avm6_5hSgij57h5VSfKAL0jDJZjwPRmXe-NiW2bqXq8EKzIP88pI0_KlyeK9cbmg5iGOygF-3Lh5DmuDRXa0QaoRj1x30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b64e8341f.mp4?token=Qe-8GRj0dJpoP-m2FLQ2rXPyLTDiRK_BlCm21xKU3v-oB_8urnJbUZZ7m4luYAdaCNsHaqh5Wp3hdSO_uRIMOAPzTIJCOBm6vvH8rL-BFWctmyTauxNDTcuFFEt1Y5U_p4z12Mh58U9-3JGpFWkXlJpgX4BMG16XHLsEkzZZP2B-lQxiit9F1JfwmwqShHW2RBQZc4ITyrWgdT6G6BAcunEgfeBJo6l_OBeplQI-LtA8PmT1R2wBK0cMSlrlXC7P2nPoJ70-As1FCCWrekS0RuofCCynOK2-f6O1TfztoV3mQ7UY56bFNuMZVPsr_o49UUVPPmTL5wTdoMH5G1AcHrAFFtRQ5OFq_DZwkt0XAzRffOxK_lzEFXRsfekf0hKpg7u3Miecr3TRS5KCyxdkvdhRDAVtdx8gh5ew5TDFFJnUf0PZQg-ybg1ZaZdY0IDbkp41b3AmJtbVUnP3bnf1BSkaFpErdqLSoHof2BaEA3dMFUSJx-v8tvjzjkZo3_59YVrsss-W7HnHi2o0fH-JLkxvKufQslnZJqwQuo7Xfn9Vo4fl6Lf2ZvE0C78SOeo6ypjN5GhLmCpQ74Avm6_5hSgij57h5VSfKAL0jDJZjwPRmXe-NiW2bqXq8EKzIP88pI0_KlyeK9cbmg5iGOygF-3Lh5DmuDRXa0QaoRj1x30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرغ رو به این روش درست کن
😁
مواد لازم:
🔹
ران مرغ: ۴عدد
🔹
رب گوجه: ۲قاشق غذاخوری
🔹
فلفل دلمه ای: ۱عدد
🔹
پیاز: ۱ عدد
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/670441" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670436">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYvXyhQSO4inE2duA1Xf_hyzXQXlBhPJNgLknXWV9s1P-WyL-H-VGUyZH4PL0b1dyNx22hW0Tblin5aLjpQsh5v1U2cAs3rzvcm6wZmz0Fvp461-8mZ9KUPz5-RXo-Rp-pmga7WcpsTrtatJFKeqgPh4rxw2LQl4tsteDMxEbQL8la7-KcGchVT-Hy2y4NnKpEQC7RoPW6B4UU_g7euCOA6e_Xwdx-K6HpdjFDOp-AC3y-L8wxgc2Qb8nTwMx3MZdBds8c5ZOrCvIOuszS1rLmmWBYNPV-UAAzXOx4VWBDwLCuDj7TifBREBKu7gW7f56eYixfAxyBhtQ2PsvtSE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوه‌های رنگی در مسیر زنجان_ میانه معروف به آلاداغلار
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/670436" target="_blank">📅 09:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c55e4a6.mp4?token=PQJ0NDHW2rsEsa4KkwtNEaeJhDuOeiK_Pes8kcW3QKYHfSW79Tc-hBW6vxAJRZBC4e3oRy469kCuxwL1WWUsUV-CWw7CaFx00j-GSzQAW28YjTwQViTWJRfdEQEceUZsSov3EE0Emznc_67VR7lVVefhwk10NJSomnO-L9D9cHwvQEaZtOte5d5tPGNjT3r_OUgngILc-RzdV-3TjIkAtA1JvnhjZa5dhyS8qytdVytX7wU5sXepbTfVZGrlJ-6T3TAl3xLKvEZ-KeSC1SOnEZkBd_1xO04fwk6sWEtKOp2R0n6wsxwO86oSnkw29orI4LAkbs9tZsVKdhi0iOIgHB_peVoUtKj2aFvoaXrv4kl5M9AUrS-WY8Jmi1Nm74PxyEk7-YHRe-CzpjjvW5o1Mtz1HrVW0L1AuQDqbOY3OZsJLi-TPe1ASagWXlhKKjKD-OB-qCL7nYSnWdTndrLmYUx007r-48D6oLxxfsP2WXQCwsx5o2FAzghyl8UE4_n_kj9JM8gdgEmAW4uisJc9VdY2MdirgqzKooAQbxD1OdskuAxrUwYXZd5cMs6fwYrQCmDbr7xeXGy58C7q7hqh6FWvLwLdq74Io8D9166VCVNNJCOHhV17wKZs5oCISXpYZc8BnVVVBzWyAFik89oovKScrakCT0yb_fPiXlMEKoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c55e4a6.mp4?token=PQJ0NDHW2rsEsa4KkwtNEaeJhDuOeiK_Pes8kcW3QKYHfSW79Tc-hBW6vxAJRZBC4e3oRy469kCuxwL1WWUsUV-CWw7CaFx00j-GSzQAW28YjTwQViTWJRfdEQEceUZsSov3EE0Emznc_67VR7lVVefhwk10NJSomnO-L9D9cHwvQEaZtOte5d5tPGNjT3r_OUgngILc-RzdV-3TjIkAtA1JvnhjZa5dhyS8qytdVytX7wU5sXepbTfVZGrlJ-6T3TAl3xLKvEZ-KeSC1SOnEZkBd_1xO04fwk6sWEtKOp2R0n6wsxwO86oSnkw29orI4LAkbs9tZsVKdhi0iOIgHB_peVoUtKj2aFvoaXrv4kl5M9AUrS-WY8Jmi1Nm74PxyEk7-YHRe-CzpjjvW5o1Mtz1HrVW0L1AuQDqbOY3OZsJLi-TPe1ASagWXlhKKjKD-OB-qCL7nYSnWdTndrLmYUx007r-48D6oLxxfsP2WXQCwsx5o2FAzghyl8UE4_n_kj9JM8gdgEmAW4uisJc9VdY2MdirgqzKooAQbxD1OdskuAxrUwYXZd5cMs6fwYrQCmDbr7xeXGy58C7q7hqh6FWvLwLdq74Io8D9166VCVNNJCOHhV17wKZs5oCISXpYZc8BnVVVBzWyAFik89oovKScrakCT0yb_fPiXlMEKoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز خاموشی‌های برنامه‌ریزی شده در کشور/ نیروگاه‌ها و شبکه برق با حداکثر ظرفیت در حال فعالیت هستند
مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:
🔹
این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/670434" target="_blank">📅 09:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670428">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ7WrVruh94rHH-XBaGCo4VSlju2zDkXJYeT4ggsKAi8i8vv1dl82jpv93_ZpWHbfj_VWst_YQm4XQ0BkcUySf06fywIqTBnW0zdii7luSQYvpJAT3qxbBS4yqejUN9boEHA0a4cpVnyOO2Hbl2qMg_d33bT8Ebm4hQRXK4rv5r9eW3tW7Scf0muU4GdaPRc5lvtM7vFAjPCX6O7T0u1Bw4phK_cJbAO6Ha-qHJbcr3gXurGm6vYXVhcCJOdL_4fxmGpTX6841IkX12etAC_0LOaqYlyKxWXRBWiTML1jgqGXFD5B3m03giXbq0GaHwdpbKEWBrJsldQVRIZBJ9Y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقال سهمیهٔ سوخت به کارت بانکی کلید خورد
🔹
براساس مصوبهٔ جدید هیئت وزیران، وزارت نفت و بانک مرکزی و وزارت ارتباطات مکلف شده‌اند که زیرساخت‌های لازم برای انتقال سهمیهٔ سوخت از کارت هوشمند سوخت به کارت بانکی را ایجاد و بهره‌برداری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/670428" target="_blank">📅 09:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670426">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff0dfaeeb.mp4?token=V6H39I0CLS8YKDPSDHb7BP6yCc2GCX6csGmf_5UIgmo9-I-klh5BYrJRtqx9EXeeLh8H0U5hxKMBzwfsPMNVdnAM3Vn35vS22TMzd3e9xALX5rE3XtyGzGmxvjHhQUqzLZV7G8amiGRrkH6MoarPFjK9EI_QwCHXl9t-37P1gh2_O5rCFZEI5yOZ9wUrW38YVbO1by_3_TZGbPAX3OT-9PigMn61O62anWiHSYdNeMue4DAVqnt03tzjUViV9wQZoBisfWYgraq2C7lQ74a1wRwmPhMcGHH4Jm-iXVlJhc5NYHIErFUTXQ2Q06_20M7FgrotflwhCSswIQMB23nh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff0dfaeeb.mp4?token=V6H39I0CLS8YKDPSDHb7BP6yCc2GCX6csGmf_5UIgmo9-I-klh5BYrJRtqx9EXeeLh8H0U5hxKMBzwfsPMNVdnAM3Vn35vS22TMzd3e9xALX5rE3XtyGzGmxvjHhQUqzLZV7G8amiGRrkH6MoarPFjK9EI_QwCHXl9t-37P1gh2_O5rCFZEI5yOZ9wUrW38YVbO1by_3_TZGbPAX3OT-9PigMn61O62anWiHSYdNeMue4DAVqnt03tzjUViV9wQZoBisfWYgraq2C7lQ74a1wRwmPhMcGHH4Jm-iXVlJhc5NYHIErFUTXQ2Q06_20M7FgrotflwhCSswIQMB23nh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرگردانی خودروها در سیل ویرانگر شمال شرقی چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/670426" target="_blank">📅 09:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
♦️
سپاه: تاسیسات و زیرساخت‌های ارتش متجاوز آمریکا در بحرین، رادار دوربرد هوایی FPS و رادار کشف شناوری در پادشاهی عمان منهدم شدند
روابط عمومی سپاه:
🔹
تنها راه باز شدن تنگۀ هرمز برای تردد شناورها، پایان یافتن مداخلات ارتش متجاوز آمریکا در این تنگه و احترام به حاکمیت کشورها بر آب‌های ساحلی خودشان است.
🔹
ادامۀ این مداخلات حوادث بزرگ‌تری را در حوزۀ نفت و گاز جهان به‌دنبال خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/670424" target="_blank">📅 08:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbrMKxc4sZt77BZ7VpfxCU786b26aDHod0h8UQjTUoswx72D33Q4iBUsuVM_UWY8MNvZ-JZZh1HinxLZv_wvCr8QfuyZD-dy5f2MGs6TuK2sYqsQNy4B9y8tp9mpMeCrssEWi_Yko_GCELNj2YI-YvEkvjw086kxS_jX86RTyF_HwunvQBA1x3-t-zcpUwCnJNj0PajB99nUZhDMTUUU7ez7WYJbkR4qMotlUsAp9fvLS66sL9GydAgZQgUMrPrUkOQ9UIRMe_4YSGbNNms_7M6ZW73NRRkUoTLEveRhGLIeYwYRx-wpgQxi70kvASvLYakxOH5eVAWicFazl17kNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucui_BrfF19ziKP_EqEhveq1quIIZlc8cZX97xmXINrSneb0LD_Ar95YW0ig_QYzONMni0_34YQsLrsO1bV-8Aopn2Q5ak1YIOqgznuIxZ25A9VEMPDljr-oulKtx95yhjg6sjnxM0YeY405IjPbzBW0Iqype3geOE-P5jfkHrtMj6F8i7tZk4UbqxKyRYhakrD-sES_6w_PNiZkrgDgh_RB7j-NiJuIcRQqtIZohHAlGR949mZ3nrqVGRd_NHI8qf-SdpB3WV3UbKuy-LPNtCFKNP6P_ZnP4sSWlVeKggPxkvfjzK8Y3tlsSe0OLZvkW3My-z8hEziN9eJ3f8ULEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7ok2aRAmkCh_fPJ4Ni4EVY7m6qI3_I4rDSJIVFqJAcIKQ-vD0-FHfSE3E7dGIc5PFzfcgfdxdfgPmBllq2ts_hWdbE9BGuYt3dlD3lQuZAVeWhf8d4n9DFvCgDRN9KxmflXeM89isz39FcTUfZGDggBA1K9dUrtB4IyAQHJzU83HRyfEH37IRGHp5ZE2p8FB1dh6bOuQfo5pUW8ciqFA0RuKzhqbFvef8c_Jp1DChShI8MnKjI-2f-6WTEnxGVCWv6Ytj60g7r4RqD47-bYzrQ8rl8uE89p5dRd8SlfEE44nMWI0RNKmYDQXi3m8E1QX8kyC60hNgdrXTOnQ8Yspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwdUkprefC81zm5bEhIAtGkYtWYWNafwmByp1rbeToaDaQfLy5j1HHqFbe7ujNej38JpN5OtDjiLhGF_NfKyYjAVZuhGQEdkUVY4lPySKafXq3Ws1fImhqfQzkazWhSXs16qRGivNldv7kALCbD-7zSgggdHe3ktcerXSPKmkkJ5vEhlDWeIhhh7pKxzcEcbIPtJZIUc0hNV4DLU7lMAln4z0U9R_prKXA5UAEWaq1Af6t66M4zwtUQKa87IGb2ImpCLjlVbXhVk-YwfzQFUbxs4TzZALFwZ-bIieMO9FCvX805YtfwbmgArCTvGEsc09VyZCAT2QOsqlWCriydQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjCXlN9qH_5ldGA7JwDGzxSBBi-0-hqsrwbdF3l4FxryWFcm2bwHG_pWkKvUAWoe8qPR-LXCyNSnBCCvkAPwoRa1kr8Z00FqSl1DwBbUuFnZHEyUhwSPGAmTB6hXF9dGuhqnp17dRemQC4K_esb_mX-9GmLwoUcqmrZJH5rnOvx2x--_9vtpSDtSCeoTIbCj1cXmrMFwCITqzAeCapucaSjCMjxi4ZF2GNdtkjapL125RC52NkWLNgD8yPcT1dlCdBI4vu2RSCl4AUNnLqWmdrzVw6wNwXmHCVVNr8hFa001k8jaejk40I4T-Ge1TTEnMz8PC0tTIjiuB6F1q9SfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0ngLBh-7u3ujxq3MNSAaI9xnqLwO4eKoAKWyt5U7LnY4nHnb0R1TK4hKtHkDcZ_5K5qr7FpEXsW8sXvI4ldPI5VBkO9vqi5O3eGyZvLC7WbYv47holPO8gWzADl6MMLPlABh30eDyL3WJYhuT20kdkLUgME_Q9ILAmgA0Czv2d19wtrYS2PGv7JHzOIag6k3unw7FDDW8I0G-9nxGfWmR4_XDDFPI9r5m4FY3cgh6h1WKTqkyDGHtimhYoemvhrGyPcuaXI1b2C3KIqMWIbWkjqCrYmTE28F_geVf2esc46djjQxx9OZPzwKV5QFqj5FMuOe-yLsAffXUdsnqc2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khaAqP229j0wNsB-OnDjQxFi8YBEsBMOtbk6r1n15AmMa_ZJDmBIMAejjVW4GkZ9z-y815TXBqfAhOyYRzpXhZZxaRZZh859Cb2tI4t94B4J_58TtlO6HgNhroUk9IANW8U8HTD-sm9ET2yxJ3YJiYxajUBgg5_nEY6sDFFQFFiKiHKoVIYy__R-9h7EQjQ8wDAvRCIXrpL4CEL59_mTvQ-NuvPe5UH_brX3ApeLYl0wfFgXsfoRGODkCaL6nXtr5yjhpk5amejtc_xKV3bt9MVx0faJD0bY-aPMkto2u1zORxkjHX6kc6zw7T4YXWNRl6k_2ARtqitrbqGaXXu9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s120GK3KjmeQvJVt2og7hVqyUL-v1IBlH8T2C7wH8rkooffBri7AMnovJvs7DqcYgJlTZ0C133YUFM4JkuRAa674rt3zPQAtmpqVL5-vavkipRH2qsrkFyfOis9un1yEmk7B99Bdsy5ZqKUiiD6lz0Akf2bsNPDBmcXumLWkIVlsaU9O2EPCKwQwOCXciEcvZROy8LnM5rOn-Y7z6orQVNQKJumHBWVJoCK3N-rYbIbaEDSL32AvPKHpQ1uTxCtFH_x3lpxbusnxolsjQ4HV2KbptzQlfKB_pf03y0oRIfi4Mcllbh9tbx2T6U66H0awLM1FtDHpjcabCeiL0d0dVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7gOFvKocDulgcWaQzFipkEl0-cqv1C6Db_b4mN878OCCjUp_W9woFBKwrTjNCmo-88P0AATwW21sUGFFztRvXRJlprfhiwlaPuEXWHEOU0i-UU9x2pAJ6irB81IKjEVo6fwjCsc9TxJx6o7B5cmhZLcvqwTAwLcBbmnzZmsM84dUQHfrNC0FpJusc0HxjwswNqew0AAmP8HJrIckC1mYjs1rEy4CX6nXwOnkgwK8yDp_ucKSxeF0baUmynak7z8dLgHH9_WRRp-_7EiJoTxBNAnXSJu8Ai9bfwBKKC8Dqma-r1gGB2SZ6JYUDJwKwaM0Fhd3-0JHZBPf0jnTA74xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
سوگواره رسانه‌ای «بدرقه یار»
▪️
از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور را به دبیرخانه سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر و مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبرفوری ارسال کند.
▪️
به آثار برگزیده هر بخش، ضمن اهدای یادبود
#بدرقه_یار
، جوایز ارزنده‌ای نیز تعلق خواهد گرفت.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق شناسه
@Badraghe_yar
در تمامی پیام‌رسان‌ها ارسال کنید.
برای اطلاع از جزئیات بیشتر، کانال رسمی سوگواره را در تمامی پیام‌رسان‌ها دنبال کنید.
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/670413" target="_blank">📅 08:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/369f15ca68.mp4?token=sMyh8WEcrP8xs5JlNn_XkRmvrfGbsF5icp_nUUBy6zf5nPNunbwNv--L_t4HxYIO8G72qTfC7p6oNd6jP78TByh4EDFD2RUJ1yUyHm9Q7K-O88oS-xgY3fwMM3_M8-LbR76kH3u1jb17y3fE_PA8rOE7vDbEXjU9ooiXk64936Gc5Z9fVPCvL5WvrnskbVk-j-qPHGTAbV1ZJUOZmqqtZdJJmcxJTiATvAPd6GaGeNkOruir1DnXct9wxjqBCyP2qdpB_knDEJ-aZOAbGrTB_CopVOJ_nC49m009zDqNdG4w0gXWcrPf74fuW7nfxmB08JRJKJ5vhJXbeTlVy75v0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/369f15ca68.mp4?token=sMyh8WEcrP8xs5JlNn_XkRmvrfGbsF5icp_nUUBy6zf5nPNunbwNv--L_t4HxYIO8G72qTfC7p6oNd6jP78TByh4EDFD2RUJ1yUyHm9Q7K-O88oS-xgY3fwMM3_M8-LbR76kH3u1jb17y3fE_PA8rOE7vDbEXjU9ooiXk64936Gc5Z9fVPCvL5WvrnskbVk-j-qPHGTAbV1ZJUOZmqqtZdJJmcxJTiATvAPd6GaGeNkOruir1DnXct9wxjqBCyP2qdpB_knDEJ-aZOAbGrTB_CopVOJ_nC49m009zDqNdG4w0gXWcrPf74fuW7nfxmB08JRJKJ5vhJXbeTlVy75v0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینات مفید برای تقویت زانو
🦵
🔹
زانو همیشه مقصر نیست؛ گاهی فقط اولین جاییه که دردش رو احساس می‌کنی. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/670409" target="_blank">📅 08:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سپاه: پایگاه موشک‌های زمین به زمین ارتش کودک‌کش آمریکا در کویت به دست رزمندگان نیروی زمینی سپاه منهدم شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔹
به استحضار ملت شریف ایران می‌رسانیم؛
در چهارمین مرحله از عملیات مقابله به مثل، رزمندگان نیروی زمینی قهرمان سپاه، پایگاه موشک‌های زمین به زمین ارتش کودک‌کش آمریکا در کویت را هدف قرار دادند و دو سکوی موشکی "های مارس" و زاغه‌های مملو از موشک را به آتش کشیده و به طور کامل منهدم کردند.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/670408" target="_blank">📅 07:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هرمز؛ جایی که باید برای ایران ایستاد
🔹
بی‌تردید هیچ انسان خردمندی دل در گرو جنگ ندارد. جنگ، هر اندازه هم که در ظاهر با پیروزی همراه باشد، در عمق خود زخم‌هایی بر جای می‌گذارد که سال‌ها بر پیکر ملت‌ها باقی می‌ماند.
🔹
از همین رو، صلح همواره مطلوب‌ترین مسیر برای ملت‌هاست. صلحی پایدار و محترمانه، نه صلحی که بر پایه فشار، تحمیل و توافقات یک‌طرفه شکل گیرد.
🔹
حالا سوال اینجاست؛ وقتی آمریکا به تعهدات خود پایبند نیست و خواهان توافقی نابرابر است، آیا باید از حقوق و منافع ملی خود چشم‌پوشی کنیم؟
🔹
واقعیت آن است که یکی از اهداف راهبردی آمریکا، کاهش اهمیت ژئوپلیتیکی تنگه هرمز برای ایران است. تنگه‌ای که نه‌تنها یک گذرگاه دریایی، بلکه بخشی از هویت راهبردی و قدرت ملی ایران به شمار می‌رود.
🔹
تنگه هرمز امروز یکی از مهم‌ترین ابزارهای قدرت‌نمایی ژئوپلیتیکی ایران در منطقه است. اگر این جایگاه تضعیف شود، مسیر فشار بر ایران و محدود کردن توان چانه‌زنی کشور هموارتر خواهد شد.
🔹
از این رو، دفاع از جایگاه راهبردی تنگه هرمز صرفاً یک مسئله نظامی نیست، بلکه دفاع از امنیت، استقلال، عزت ملی و آینده ایران است.
🔹
ما مردمی هستیم که تاریخ‌مان با مقاومت، غیرت و پاسداری از سرزمین گره خورده است.
🔹
حفظ تنگه هرمز، حفظ بخشی از اقتدار ایران است، اقتداری که باید با عقلانیت، تدبیر و وحدت ملی از آن صیانت شود.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/670407" target="_blank">📅 07:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOPdDKUYqjWVYUk_WPgqBQ4ZceaH3l2QKu3Yx4r4rOXaB_SVdZ6ElC0beS2rf8eU77oqrSubbge94BMMlukNu2eGVOwM2jQBCdgP67EJtXNDxh0YDmjKdY6I4OR-eqW4qgf5qVUYsUmHJqidBefcaDRwg4iqYc_FFIVW5YXi3WIllqC15kSYADN-KwcwfaFRfLzMcsJKWpB64AwIgX1aBT6Xio59dHv3c126lWnqARzEiDs5i8EHN1vaKT51oHMxCvexOoclO6LbyLQddLp1ZuMHTAx4eLh5NCEcCMYuR4is8d-ShL8eX2Z_79ZXKIOh10eeDm4whhfHaJQiSH2lyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رفتار آمریکا در برابر ایران چطور تغییر می‌کند؟
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/670406" target="_blank">📅 07:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670404">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
توزیع کارت آزمون کارشناسی ارشد ۱۴۰۵ از امروز آغاز شد
🔹
داوطلبان در صورت مشاهده مغایرت در کارت ورود به جلسه خود می توانند از امروز تا ۲۶ تیر از طریق درگاه اطلاع‌رسانی سازمان سنجش ویرایش کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/670404" target="_blank">📅 07:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIIZMoeG-RqQTONPy8ZyC1htiJA3KmbVnPEF9SVm9108u_aCcmgKcbovn1PIdeSezwBfhTV9mLYVe9kPmenAmUXcrboHuCH5JGqEhBInY19Lkh2e486vXIDyu0MTQ8dH3LeTQdpO_WpoEYtICi36ZvTWysLoPv9C5WwqJHveegeRzgddwhz8y1etk1x-80KSTY_SLPEy7ArZv7lSZdYRiBBGW4dVWRA7Gw32T6_krZyCHT0rk5nERDLC16C-GcbUsDkmrDNHtS3diBjKmKxlnGZfnJUVDFh0WkEAFLLnYxG1qKwUBPiGKBD25Mtjqb1NbWGc9X7OfYGiZk606Uxfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۲ تیر ماه
۲۸ محرم ‌‌۱۴۴۸
۱۳ جولای ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/670403" target="_blank">📅 07:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670398">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524db81262.mp4?token=LQvkLulY4KQPklUU8tYmaveYMXM-JxkkqBv6v9t1FQsFrQ77KCdiJeXDJ9GVYuaYh0TNVYVJoZCnghGaPUaFBsXzhcwMlUom4lFKNlnP3gxN4mxw6P7kjOleldckmwVTG0Joa0cyxBR6iajnX2FM2NySsZFY0VYVdB3_sw8MwXDbYiLf47QQwo8HaKOu8H53dtwG8JM6hk6ykjGXH-6JDeft1Zi1hlbZVZxMeZHNzaU_pLQhlJrBaIxmYGWAUx5wUElh5cMo2LP-ac6BCiKil1k1ZKtd3RhPhguisL7RUkehmeaJn_81xTSTVtuupUCAMdo1wqGdZjVawGnFgtmtWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524db81262.mp4?token=LQvkLulY4KQPklUU8tYmaveYMXM-JxkkqBv6v9t1FQsFrQ77KCdiJeXDJ9GVYuaYh0TNVYVJoZCnghGaPUaFBsXzhcwMlUom4lFKNlnP3gxN4mxw6P7kjOleldckmwVTG0Joa0cyxBR6iajnX2FM2NySsZFY0VYVdB3_sw8MwXDbYiLf47QQwo8HaKOu8H53dtwG8JM6hk6ykjGXH-6JDeft1Zi1hlbZVZxMeZHNzaU_pLQhlJrBaIxmYGWAUx5wUElh5cMo2LP-ac6BCiKil1k1ZKtd3RhPhguisL7RUkehmeaJn_81xTSTVtuupUCAMdo1wqGdZjVawGnFgtmtWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایۀ خبرنگار آمریکایی به وداع با سناتور جنگ‌طلب فقط با یک گل!
🔹
یک خبرنگار آمریکایی در مقایسه مراسم باشکوه تشییع پیکر مطهر رهبر شهید با مرگ سناتور جنگ‌طلب آمریکایی، با انتشار فیلمی از خانۀ او نوشت: آمریکا ۳۵۰ میلیون نفر جمعیت دارد، اما تنها چیزی که نصیب این فرد شد یک دسته گل کوچک مقابل خانه‌اش بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/670398" target="_blank">📅 07:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670397">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای سنتکام: حملات جدید به ایران تکمیل شد
ادعای سنتکام یکشنبه شب به وقت محلی برابر با صبح دوشنبه به وقت تهران: نیروهای
🔹
آمریکایی با استفاده از مهمات دقیق، ده‌ها هدف را در چندین نقطه هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های بین‌المللی در حال عبور از تنگه هرمز را کاهش دهند.
🔹
در این حملات، سامانه‌های پدافند هوایی، سایت‌های راداری ساحلی، توانایی‌های موشکی و پهپادی و همچنین شناورهای کوچک نظامی ایران با استفاده از جنگنده‌های آمریکایی، شناورهای نیروی دریایی، پهپادهای یک‌طرفه هوایی هدف قرار گرفتند.
🔹
نیروهای آمریکایی برای نخستین بار از شناورهای بدون سرنشین یک‌طرفه دریایی استفاده کردند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/670397" target="_blank">📅 07:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
روایت متفاوت جواد موگویی از تشییع رهبر شهید انقلاب در عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/670394" target="_blank">📅 06:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS در کویت به‌طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند هوایی پاتریوت در پایگاه آمریکایی در علی السالم کویت و همچنین یک سامانۀ راداری راهبردی FPS در پایگاه احمد الجابر را به‌طور کامل منهدم کردند.
🔹
تنگه هرمز سرزمین ماست و اجازه نخواهیم داد یک ارتش یاغی و کودک‌کش از آن سوی دنیا به دخالت‌های غیرقانونی خود در آن ادامه دهد.
🔹
عملیات مقابله به‌مثل فرزندان غیور شما ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/670389" target="_blank">📅 06:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
برخی منابع از وقوع انفجارها در پایگاه هوایی «موفق السلطی» در اردن گزارش می‌دهند
/ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/670388" target="_blank">📅 04:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670387">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
یک شهید و چهار مجروح در پی حمله دشمن به ماهشهر
🔹
ولی‌الله حیاتی، معاون امنیتی و انتظامی استاندار خوزستان گفت: در پی تهاجم بامداد دوشنبه دشمن آمریکایی و اصابت یک پرتابه به ایستگاه پمپاژ آب کشاورزی در شهرستان ماهشهر، یک نفر به شهادت رسید و چهار نفر دیگر مجروح شدند.
🔹
فردی که در این حمله شهید شده نگهبان این مجموعه بوده است.
🔹
وضعیت مجروحان توسط دستگاه‌های امدادی و درمانی در حال پیگیری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/akhbarefori/670387" target="_blank">📅 04:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20bcbbefa0.mp4?token=qDtBWOm1Q1-se3DvHYtOVEqbpwqNuaq1voSSsBa1ty0kC_94XapWgErOOD9SQZenAYOCBReYeD-ZYWUMxKrkMdA_xJ_wd0sloXdTuQu5s0k1hMjOtmqt6VK1AIVRh3rit6-9NFvDLxKsoYuo9bkWz7Bj__gRX4THfbA89r__jXVLkBbMLrjb3-rrjAg1gN4WCajEIwQsg7kWfpahQBNvm0wT3_BnQ5BEYrMZ2hMkWbDj1TRy1nm3mAqXrV5RSARbBYJHNhIOSX1IpZ27SQ2jXOrgdtFlyJLdGuWLXt_mc2O8Uh6NNyx77QzOtzfIjEL2kqh9kBMYEtHs04sCOAj9fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20bcbbefa0.mp4?token=qDtBWOm1Q1-se3DvHYtOVEqbpwqNuaq1voSSsBa1ty0kC_94XapWgErOOD9SQZenAYOCBReYeD-ZYWUMxKrkMdA_xJ_wd0sloXdTuQu5s0k1hMjOtmqt6VK1AIVRh3rit6-9NFvDLxKsoYuo9bkWz7Bj__gRX4THfbA89r__jXVLkBbMLrjb3-rrjAg1gN4WCajEIwQsg7kWfpahQBNvm0wT3_BnQ5BEYrMZ2hMkWbDj1TRy1nm3mAqXrV5RSARbBYJHNhIOSX1IpZ27SQ2jXOrgdtFlyJLdGuWLXt_mc2O8Uh6NNyx77QzOtzfIjEL2kqh9kBMYEtHs04sCOAj9fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امشب، یک پهپاد اوکراینی به یک انبار نفت در شهر میخایلوفسک روسیه حمله کرد...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/670384" target="_blank">📅 03:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3018e7f48d.mp4?token=PwhcQLGCzCvP5-7x8d6wy5bwUzwBCxldq-uYDL6VwSqtEzggw7rGzpoAJ9JA1zOdQWjq3xHF8UgMHNWzzbu2yenf2Vv7nBQB1IaNEfxyRNT3XC--9VIwisYSRDP2nAnZqzhI0vt68wPCz9tUiYyDBlWoStk-LD3gjYcQXgheVikSaWqyre0NpbFPdGxe7-tTm14Jrc4jOsthin1tsWlR-6rVSKntaE_-qXio8Ykanto3-0ntAqRx0HMTIJTq_mZjqAIfof03JB5jj5kzmSCW4XYAlNfCIWsL-uFi3Ae-mL_6THmkwNHJQm73fTvIW1dQkaC8yxrVmMMKwlPMmqbLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3018e7f48d.mp4?token=PwhcQLGCzCvP5-7x8d6wy5bwUzwBCxldq-uYDL6VwSqtEzggw7rGzpoAJ9JA1zOdQWjq3xHF8UgMHNWzzbu2yenf2Vv7nBQB1IaNEfxyRNT3XC--9VIwisYSRDP2nAnZqzhI0vt68wPCz9tUiYyDBlWoStk-LD3gjYcQXgheVikSaWqyre0NpbFPdGxe7-tTm14Jrc4jOsthin1tsWlR-6rVSKntaE_-qXio8Ykanto3-0ntAqRx0HMTIJTq_mZjqAIfof03JB5jj5kzmSCW4XYAlNfCIWsL-uFi3Ae-mL_6THmkwNHJQm73fTvIW1dQkaC8yxrVmMMKwlPMmqbLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارالذکر در نیمه‌شب‌های حرم امام رضا(ع)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/670383" target="_blank">📅 03:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670382">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpQgXO9juC0oeQUG4J4HVMeYdAh1-665K-rUcfW2Yf5-QB3SpabaMvlsLi0lYd_yeTyrUUfgXcD81oF0mJy_ENP1BIgNi58dJpG6h4P7Kwsp4PMAKtBTYqiP6iCFyBa3xN4-tZg-1r8RYutj1MASVHXLnqD3WdZWhp3If1pMdRILut1DZfPKRP2O8MMI78SMe8ldgKUJxINwkCaSpdcnJa17hQT_lTL6yHh1ZmRb_Ex0ZYfsf-ZSKswMFWS6QegM5I-d7-8RC0iX5OAYbs2PP2HCGzytjO0ZaQTweciaONr_EJk4R1YJWcWrUush6Lhf-hSn87QS3JkEmli5SbSuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهرهایی که مورد حمله آمریکا قرار گرفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/670382" target="_blank">📅 02:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: یک مقام آمریکایی گفت انتظار می‌رود موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در شامگاه یکشنبه انجام شود؛ حملاتی که از نظر گستردگی بیشتر از حملات اوایل همان روز خواهد بود./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/akhbarefori/670378" target="_blank">📅 02:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670376">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
نقاطی در آبادان و اطراف شادگان مورد اصابت پرتابۀ دشمن قرار گرفت
معاون استانداری خوزستان:
🔹
در ساعت ۲ و ۲۰ دقیقه بامداد امروز نقاطی در شهرستان‌های آبادان و شادگان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/670376" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670375">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
معاون استاندار خوزستان هرگونه اصابت به فرودگاه اهواز را رد کرد
حیاتی:
🔹
دو نطقه مورد اصابت اطراف محدوده شهر بوده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/akhbarefori/670375" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670374">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
چهار نقطه در امیدیه و ماهشهر مورد تهاجم هوایی دشمنان آمریکایی قرار گرفت  حیاتی معاون استاندار خوزستان:
🔹
در ساعت یک و ۴۵ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه ۴ نقطه در شهرستان های امیدیه و ماهشهر مورد اصایت پرتابه های دشمن قرار گرفت.
🔹
دستگاه های مربوطه در…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/akhbarefori/670374" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670373">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
برخی منابع خبری مدعی شدند، برخی از موشک‌های آمریکایی از کویت به سمت ایران شلیک شدند
🔹
طبق این گزارشها، موشک‌های آمریکایی از کویت شلیک می‌شوند، وارد حریم هوایی عراق می‌شوند و به سمت ایران حرکت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/670373" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670371">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
چهار نقطه در امیدیه و ماهشهر مورد تهاجم هوایی دشمنان آمریکایی قرار گرفت
حیاتی معاون استاندار خوزستان:
🔹
در ساعت یک و ۴۵ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه ۴ نقطه در شهرستان های امیدیه و ماهشهر مورد اصایت پرتابه های دشمن قرار گرفت.
🔹
دستگاه های مربوطه در حال ارزیابی خسارات احتمالی هستند که گزارش های تکمیلی متعاقبا اعلام خواهد شد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/akhbarefori/670371" target="_blank">📅 02:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670370">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
معاون امنیتی و انتظامی استاندار خوزستان: در ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه دو نقطه در اطراف اهواز مورد تهاجم پرتابه های دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/670370" target="_blank">📅 02:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670369">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
مهر: معاون استاندار مرکزی حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/670369" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
معاون امنیتی و انتظامی استاندار خوزستان: در ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه دو نقطه در اطراف اهواز مورد تهاجم پرتابه های دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/670368" target="_blank">📅 01:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
فاجعه در بانکوک؛ ۲۷ کشته در آتش‌سوزی یک رستوران
🔹
شعله‌های آتش نیمه‌شب، یک رستوران شلوغ در بانکوک را به صحنه‌ای از وحشت تبدیل کرد. در حالی که مردم برای نجات جان خود فرار می‌کردند، آمار قربانیان لحظه‌به‌لحظه افزایش یافت و علت این حادثه همچنان در هاله‌ای از ابهام قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/670367" target="_blank">📅 01:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
مهر: ساعت ۱:۳۰ بامداد امروز دوشنبه صدای دو انفجار شدید در اهواز و ماهشهر به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/670366" target="_blank">📅 01:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
حمله دوباره آمریکا به دکل مخابرات اطراف روستای طاهرویی سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/670365" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCRrqA5XMyexG-7G4AEK4J4gJ3yNasWXkGIKNS18HODwrCiylegrb4BtPfmEoR_BcW28IAEO4qHJ84P7ywn_LP2qVZCp7JlASUWIQonxoWHalyNv8Ez1UNgZll-Pddfged4ZBbd1ROVZd5aLE5JQuws__EU43o-RklrvGnjAjXJxYrIp1BlcJMMeriisaawavVvD8Tv0izhxE8pR1-CMOWvY6u70nDRa2IhYmcwP-vDRq-rXt_frot9HMv_Qk6hmmI9ayJa1HfMSS8QSfvFbYmrcAKA0FHbFlY0leNcUt8oNgl7pPxYPkEI60gs4E0LbZgTnRvZviU_27T1-bEv03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz4X81mvX7gNB43Y0zJ_eUUEO0cxfAkHxFjMBU35IZIjPy-UCJ_Sicbo3mSiJ7kYcou4tsjh5oPMjc3cW8cdKYkvxqLwNfpxa7FbyqYcC4h7E_xZnfhNoLtBmCS4uI_9MAyPGnhVIYacPzbrxrAgVZ6VR4QP8_EqjAQW4xtpt3V0mZKhYBgRCg--UG0GgRaIyDT9GstBB6y57N-f8M2FjISn0KyTEwyd0_pvOoFXQpR3wXx2CWvGR_9ZwQ8LcGYM661IVdVp9xPH_GhJbB0eKRtMscEfdOM5jxyFGT63QoX-jR33LsTunSREHTwmEaXM7Q-DVWGQZQuHQSQZPotoJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصویری
کم‌تر دیده‌شده از لحظه ورود پیکر رهبر شهید انقلاب به کنار ضریح مطهر حرم مطهر سیدالشهدا علیه‌السلام در کربلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/670363" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670362">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-3wxMDooGvLRi12ZLIkCGz5zuvwGMkHtN2bVuzLYUQdGK5vI_1hAEcJqqqYf86HgaCSqizPJ-ktxke1oQO7pGZe6FdTz21jucT4L-M-bPLrnTT2mUlAhMC3gTLNjqlcUR-LpDXQZFg1UfmxOZsiofPsm4xj5iavRm3Tl_iAxwd7qXMulgE7YCUX09HdpisYdKJTSrU19cJlt7u-LeUUKkdECDcjBPe16tQ9-btBJ6bzNsjmDySoPoHdaTUwxJy5L67hUMqz7GJATRbbpcStMWENXyRPFRd2awVZNuxAP4Z7qZrUhS1F7DO0uKt6c9YguhDNcj_AXwRh3ZbEcUMcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله اراکی: ریختن خون ترامپ و نتانیاهو و شرکای آن‌ها «واجب» است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/670362" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
سخنگوی فرماندهی مرکزی ایالات متحده در گفتگو با سی ان ان مدعی شده که سپاه پاسداران انقلاب اسلامی ایران به تازگی به سوی شناورهای در حال عبور از تنگه هرمز آتش گشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/670360" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670358">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
پرس‌تی‌وی: صدای انفجار در کنگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/akhbarefori/670358" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670357">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
مهر: گزارش‌های اولیه از شنیده‌شدن صداهای انفجار در جنوب شرق کشور؛ جزئیات رسمی در انتظار اعلام مراجع مسئول
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/akhbarefori/670357" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670356">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
صدای ۶ انفجار در اطراف روستای طاهرویی سیریک (هرمزگان ) /باشگاه خبرنگاران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/akhbarefori/670356" target="_blank">📅 01:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670355">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رسانه‌های پاکستانی از چند انفجار در چابهار نوشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/670355" target="_blank">📅 01:15 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
