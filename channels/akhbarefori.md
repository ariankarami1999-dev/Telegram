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
<img src="https://cdn4.telesco.pe/file/k4VVmg45X3Jzwu-adEyTDaLinrk8qJ-UNy_lRVRjCfxmDLx5m2gsSwUQ8cP1b5GMcCfyfxRKkxlv7EszxZZAuSNG6GOEg99Qo35Njj9kUo-CASJyyfpF3mYUzV3qo_rwEBKoiy3GuGrE3C-Fvd4MRubMDW4kgocucUtmCjeG4oj2CjTdp_GrlmsXUvboUi0JZxCUnlYtFRAqDDQR8uhFp43fQvG-746o0WKHXyrQYY6pT3qwnXYjRPhRafDbgOGY6RAYJDJKyBVuLShmIQrJ0BhEbvFZZpVwRev5KbGQRKdxa_TO4anj4WAclGlNKhsIjH6VJviE1cH2xmx4r2OpXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-694582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNRA0DqsUMuMSeD5H_f9qp0Im9y1rrKBMdtRXodzvNM_QPkx-PpR2omYwE_wbGEIY9oSXECDOvvuryEX2fbnyASOzXAki-zOL7U-lkiYRGXo47cjBCwaqEn-ilKPS8vXiOc761owlNODin47Gg4l00en82heTGJVb8P5ZcuvuBchMEOQL3L6LDhvPEmRxEAcwfCcFdYFQPvMQUgJn7mYIC3jl6HiDVK6ngdDKl0UkChEijQkt_ARz7h0-jbvaSFbLe_Xz6yGAWRREWodPfkVt6JkedKsta4wxPFhPM4MQCXStqb6ts9awSVRo9j-ff3HF7SKzU16Mi0znEPQ83dB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش مجمع وزیران ادوار طی نامه‌ای به رئیس جمهور به رئیس جمهور از عملکرد دوساله مدیریت گروه صنایع پتروشیمی خلیج‌فارس
/
هلدینگ خلیج فارس با عبور موفق از تنگنای دوران تحریم و جنگ وارد دوره «جهش سودآوری و توسعه» شده است
🔹
این هلدینگ «دوره رشد و تثبیت» را پشت سر گذاشته و دوره «جهش سودآوری و توسعه» را شروع کرده است و اکنون از نظر اندازه، سودآوری و ظرفیت سرمایه‌گذاری وارد مرحله و موقعیت متفاوت از نظر خلق ارزش افزوده بیشتر شده است.
🔹
سود خالص ۱۸۷.۵ همت سال گذشته نسبت به سال قبلتر ۶۷.۴ درصد رشد داشته و تولیدات آن به میزان ۲ میلیون تن نسبت به سال قبلتر افزایش یافته است، در صورت تداوم وضع موجود، این میزان در بازه زمانی منتهی به خرداد ۱۴۰۶ به ۲۲۰ همت می‌رسد.
🔹
در مقطع حساس دو جنگ تحمیلی و محاصره دریایی، علیرغم تمام سختی‌ها، روند تجارت و صادرات هلدینگ خلیج فارس به‌صورت شبانه‌روزی ادامه داشته و در بازه زمانی دوساله اخیر، قریب به ۱۰ میلیارددلار ارز حاصل از صادرات محصولات شرکت‌های تابعه هلدینگ، با استفاده از سامانه نظام مالی-بانکی فروخته شده و به کشور بازگشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/694582" target="_blank">📅 17:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORiPF2T9GZOBIiJJwkpWtHyEQu60xxgyTNnFDfLOTto6_f0kLxFB_pNdYRB1sHFUXKNPniSUZH2fcdcWz50DV1gHkLcmveZPThM72vxlYBRiF3Rr_71xvf8tUj8SAaTauhX9MG3UmCO8rkHAOsQY1I31SmPrBvKiqDDDfwoDRtTRMjdXFQbguceSKNu22NXBJA7u4AH1gM2ShtbSR0fNIkjRIunaqVO7o6loaWy_5o4yJs1164h9G7Gm_on6o3MJgwa9naCljjj2BTLbHWGdMOwT4QSpvqNDmUj3iHKkJpYu78R5mci4lyVNP1gpeZHcmfA_wnZy-28ySwVP_mvr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مناره‌ معروف ژئوپارک دره شیرِز؛ کوهدشت لرستان
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/694581" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سفیر ایران در گرجستان احضار شد
پایگاه خبری سیویل گرجستان:
🔹
وزارت خارجه گرجستان، سیدعلی موجانی، سفیر ایران را به‌دلیل اظهاراتش درباره ملکه کتِوان و «تفاوت روایت‌های تاریخی» احضار کرد.
🔹
گرجستان می‌گوید اظهارات سفیر در شبکه‌های اجتماعی از حدود فعالیت دیپلماتیک فراتر رفته و بر افکار عمومی تأثیر منفی گذاشته است.
🔹
ملکه کتِوان چهره مقدس گرجستان است که ادعا شده در قرن هفدهم، به دست ایرانیان شکنجه شد و جان باخت. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/694580" target="_blank">📅 17:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/414c940d77.mp4?token=PhMbJ3rewwDUoBXm47Bs-g_ZKfeMBx-ZJK-U2T9w6zK1bpOJpq9IqZPNT0WCzvAGKff0xaYIaJWXBL8N1dX-weTtI8Yi2z-aOPMdVQla9j2UxS-HXgV__wn6bEeig1MayR5Fdyuf1XqOSWUvr3wIawAOTQHhKo8RABuCI6DcUWgKOGILlg71DRNW7KNjHtYWo5ta1F4A0_bOlGrNskjIQLMt42KeeeetRwNsztk8p5Tijs_wKNT3zNyFuNtnQJeXCe7PGv_sHdSUlWHYQmVJNWDPBjbb6UNe5dCd0OPO-rzK8ZUKopUN0siIzSTDU0cirnWd9JsUPHk4aLRvpteI2ItJjf8Q-J87rCVRaSYZSGVlClsRQ1GrWb0O2FD1DWtJzm314yNOhgf3N9iXtDkIKxnJHGmaciT3jmmuxFtfxutabpzZyr47GFvC7K6-vMMAsMcspL09gXMNsLj3hqNw1PfdA_ako-4ybsFPtPhbsNJZCgNh7t4Kwk5MgVcfKE3IUwFEXofTYCWuQGZoJU_x3SQDta5-dS23NAcohg-BghfZulUkTkM7i-vyqwmhfYCXg6fH7-eMaej2vczgVC9OG7Pm52FqDblOFg4JN4LGY6le-Td6156QzBM6x5376ZKJwERkfBI1pYsiscX8n6k1FtxqvH1838_pg5gvC3jLv_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/414c940d77.mp4?token=PhMbJ3rewwDUoBXm47Bs-g_ZKfeMBx-ZJK-U2T9w6zK1bpOJpq9IqZPNT0WCzvAGKff0xaYIaJWXBL8N1dX-weTtI8Yi2z-aOPMdVQla9j2UxS-HXgV__wn6bEeig1MayR5Fdyuf1XqOSWUvr3wIawAOTQHhKo8RABuCI6DcUWgKOGILlg71DRNW7KNjHtYWo5ta1F4A0_bOlGrNskjIQLMt42KeeeetRwNsztk8p5Tijs_wKNT3zNyFuNtnQJeXCe7PGv_sHdSUlWHYQmVJNWDPBjbb6UNe5dCd0OPO-rzK8ZUKopUN0siIzSTDU0cirnWd9JsUPHk4aLRvpteI2ItJjf8Q-J87rCVRaSYZSGVlClsRQ1GrWb0O2FD1DWtJzm314yNOhgf3N9iXtDkIKxnJHGmaciT3jmmuxFtfxutabpzZyr47GFvC7K6-vMMAsMcspL09gXMNsLj3hqNw1PfdA_ako-4ybsFPtPhbsNJZCgNh7t4Kwk5MgVcfKE3IUwFEXofTYCWuQGZoJU_x3SQDta5-dS23NAcohg-BghfZulUkTkM7i-vyqwmhfYCXg6fH7-eMaej2vczgVC9OG7Pm52FqDblOFg4JN4LGY6le-Td6156QzBM6x5376ZKJwERkfBI1pYsiscX8n6k1FtxqvH1838_pg5gvC3jLv_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه آتش‌گرفتن یک هواپیمای مسافربری و تخلیه فوری مسافران آن‌ در آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/694579" target="_blank">📅 16:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
وزارت خارجه پاکستان: تحریم‌های اعمال‌شده علیه ایران یکجانبه هستند و از سوی شورای امنیت صادر نشده‌اند؛ بنابراین به تجارت خود با تهران ادامه خواهیم داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/akhbarefori/694578" target="_blank">📅 16:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0571b8208b.mp4?token=f_-Z-OD1kxQlsbZZCFCblmmFEaWaEEARp18gezxyGhQeZknNLedPFmGSiOqq8tg3Gc0GsJdIK1tPW0tphedKOoVzUF9bh80htoH2owuY2yWHKlin5NXfL2_7l9LMINlserVqAQNV_7vXHwZxuqQ8bX6DMTyVASsmcyenJBsVLqzhyA0re30ekfRZwm7JW7icSg6zd5VkwJWHeXxkcLIudljxerSyhU-Tb0KHm2kre3WjbBjhbHjWuXJRICxzz5URo1QZimntkaUC9RZhlm8Fn3PBFqmgN1PJyeO3zpWBOWdE_s7-0WZu_t1EweB6llW_RXkKToL_BgltWspA3QAUsAzfA0FizVXi5WK8zey-pbnvfgzVIU94ShA4e001ToOrAkAXwVPxIPj8XRI2cPJYZhaY7QNbMdoRCGjcaZWe_j0eaPt-yLReeoQa6XNDTiFcIOTJiEXuMfph17CUbuRB4Wf9lmcpxSnP1RFqr_VUoOgdr3xpXgAe0Er5_OtxlKbKikJyGognGJlZsQMASSKlz4dMm6Gbbsoilxxn9PGu1oPZHpSBF2WWJFGBCHkuoFbAC0DjDswLTiPCdrn-Nr9crSrtC-DQxA74lbY9mFJ3AnClw20oh8Uep7yunN80aVSAEGQa8Y6uMvZFZ9vbR_pKMikwUBtcSouYj03cIEnaJkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0571b8208b.mp4?token=f_-Z-OD1kxQlsbZZCFCblmmFEaWaEEARp18gezxyGhQeZknNLedPFmGSiOqq8tg3Gc0GsJdIK1tPW0tphedKOoVzUF9bh80htoH2owuY2yWHKlin5NXfL2_7l9LMINlserVqAQNV_7vXHwZxuqQ8bX6DMTyVASsmcyenJBsVLqzhyA0re30ekfRZwm7JW7icSg6zd5VkwJWHeXxkcLIudljxerSyhU-Tb0KHm2kre3WjbBjhbHjWuXJRICxzz5URo1QZimntkaUC9RZhlm8Fn3PBFqmgN1PJyeO3zpWBOWdE_s7-0WZu_t1EweB6llW_RXkKToL_BgltWspA3QAUsAzfA0FizVXi5WK8zey-pbnvfgzVIU94ShA4e001ToOrAkAXwVPxIPj8XRI2cPJYZhaY7QNbMdoRCGjcaZWe_j0eaPt-yLReeoQa6XNDTiFcIOTJiEXuMfph17CUbuRB4Wf9lmcpxSnP1RFqr_VUoOgdr3xpXgAe0Er5_OtxlKbKikJyGognGJlZsQMASSKlz4dMm6Gbbsoilxxn9PGu1oPZHpSBF2WWJFGBCHkuoFbAC0DjDswLTiPCdrn-Nr9crSrtC-DQxA74lbY9mFJ3AnClw20oh8Uep7yunN80aVSAEGQa8Y6uMvZFZ9vbR_pKMikwUBtcSouYj03cIEnaJkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهنام ابوالقاسم‌پور با حضور هیات ایرانی در منزل شهید حزب‌الله: قهرمان‌های واقعی اینجا هستند؛با وجود حضور در خط مرزی، خانواده شهید خانه و منطقه خود را ترک نکرده‌اند/ من به‌عنوان یک ورزشکار، شهید محمد را که هیچ‌وقت اینجا را خالی نکرد، الگوی خودم قرار می‌دهم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/694577" target="_blank">📅 16:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
آغاز خروج اضطراری اسرائیلی‌ها از امارات
🔹
روزنامه «یدیعوت آحارونوت» از آغاز انتقال حدود ۱۰ هزار اسرائیلی از امارات به سرزمین‌های اشغالی از روز جمعه خبر داد؛ مسافران تنها مجاز به حمل کیف‌دستی هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/694576" target="_blank">📅 16:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21dadef9e3.mp4?token=EAXUzzrzEtR8n1e1fzO0IHFXO6O9J2VlX4aiIwTjvBay3JznPGc_4N48kOFcbUrnQkTbit6azVc9bzGQTpT8OiE-tQmQZwuf1w8zNHptH1lcPi9IOm2yTaqf4fhnQN-vrAG9BySTT-tN_NA23Ei6WXt14dO_3Hf58elqULNovUyxkaqd50BFJuL4LnSALl07uTnz57CnnpcgILAxxv5qY72WmwpJRhABHnrxPojXUiroMPEYoesQj0WAjoHc47bZeZk0d8crScRpmLuegeCM6ZxRjrwGLWSCdZShNyzoAW-M00x_OWugL6PeFNZrGEy2VmxPwgt7iwtpire9pZ678w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21dadef9e3.mp4?token=EAXUzzrzEtR8n1e1fzO0IHFXO6O9J2VlX4aiIwTjvBay3JznPGc_4N48kOFcbUrnQkTbit6azVc9bzGQTpT8OiE-tQmQZwuf1w8zNHptH1lcPi9IOm2yTaqf4fhnQN-vrAG9BySTT-tN_NA23Ei6WXt14dO_3Hf58elqULNovUyxkaqd50BFJuL4LnSALl07uTnz57CnnpcgILAxxv5qY72WmwpJRhABHnrxPojXUiroMPEYoesQj0WAjoHc47bZeZk0d8crScRpmLuegeCM6ZxRjrwGLWSCdZShNyzoAW-M00x_OWugL6PeFNZrGEy2VmxPwgt7iwtpire9pZ678w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهم‌ترین راز رشد گیاهان از زبان خودشان
🪴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/694575" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خبرنگار نشریه‌تایم: درباره ایران، آیا قرار است پس از انتخابات میان‌دوره‌ای بمباران‌ها را تشدید کنید؟ گزارش‌هایی در این باره منتشر شده است
🔹
ادعای ترامپ: ممکن است. ما سلاح‌های زیادی داریم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/694574" target="_blank">📅 16:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV_Wh0Epbxv1rd4TeNgTyChfbb23zHJobjUV_5Q6k0zCW9_1rBi3XmcZQH8tOlbOKyQhFeO72z8o4dmmVlheA-kEMht1HnoloXSPB4fDh0W9xBofIYtVgcgd8632oAH1jQxJ3wb4ZOeSXhXi26vBjc3EAtTg8FUrOpu19WF8CODuIaz7DcO4jUhHWnU3LXHPo59J_whmoJR5ViaU5f9RwwYBwmC_YT4nexybDS5w8xhazaJyLbu49iPrVV5FUeiGJvyyH2jVxkZUn2jk73mFb7ly0OFVjBZzWpjAkY8NqSHhjvxg_ldQNHGvEr9xbJkDLhpG79wPgy5e5QwamW8z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصرف اینترنت اینستاگرام رو کمتر کنید
🔹
برای اینکار نیاز به فعال‌سازی Data Saver هست:
Settings > Data usage and media quality > Data Saver
🔹
با فعال کردن آن، اینستاگرام فرایند دریافت محتوا را بهینه‌تر خواهد کرد تا مصرف کمتر شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/694572" target="_blank">📅 16:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حاج حسین یکتا در منزل شهید حزب الله همراه با هیات ایرانی: در جنوبی‌ترین نقطه لبنان و خط تماس با دشمن، مهمان خانواده شهدا و رزمندگان هستیم/ اینجا همه یک سؤال دارند؛ «حال مردم ایران خوبه؟» پیداست که یک امت و یک ید واحده هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/694571" target="_blank">📅 16:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOFGxVpRdWYauraV3mJ4zMPHujwCqDxxHBeOTZy5Y3iNMWJh2Ejp8pqxNc-SXEOUgzfKI23dmCkd73FxIDzVINyHpZ4GBlasikPkFOuAbxCNFmXrir8QMecDPlIpnHbHMKaP_TMYaI9BtO3s4pbcxEnNTIrHblInDPBF2bTavnyUUnROGvul6D7uBbOww9pVvq4dUYfMJkLmDRouIUM2XhwEqup2_v9Vq-hzfxt3ulFST2fpF0lH3l-t-VfzBdcqacJdoI1gnplVGM2AbzOclFeTqFMXidzXz1zTjRYMh8dybC5bsYoIA3aI49Rw8n_mo9YIEhO895fcyUdOPXZ4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین واکنش نخست‌وزیر عراق به پایان حضور آمریکا در این کشور: از این پس تصمیمات امنیتی و نظامی کاملاً در انحصار نهادهای دولتی است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/694570" target="_blank">📅 16:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای‌نتانیاهو جنایتکار: ما می‌دانیم که خلبان مهاجم، تحت "فرآیند آموزش و تلقین افراطی اسلامی" قرار گرفته بود #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/694569" target="_blank">📅 16:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4ef28a16.mp4?token=PPNTGjxD4x8zVtSXwj-n5ANA5eVdakfyPS00mchLcFtrO-xQITTfGDuvHcIrRxg1NJiHp0hy6Lcg6XG57Ujxm7jR_qCukz5fPasfVpoSCX7hsJeCJDel7OqrSTfYb4VWAVRvAxY4XoMOguF1gx1eXPpTLpb8Y_JKdVv9wRqQK2l7oflnRbotZX9MCd6yZkC-0gz5kNtjmwxHuvgQXqWZzgQ2Chg5yzRlatXg91sQRgal5WhEqnpi6su7QMwAaSsw4fgsBkqPSFHRGg-E7waW5PvHJz3_0eRO7vfLDgwCTkvSectw2imw1x9AuEpVa4qvlr5II8UOVfWRZRPW3KsFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4ef28a16.mp4?token=PPNTGjxD4x8zVtSXwj-n5ANA5eVdakfyPS00mchLcFtrO-xQITTfGDuvHcIrRxg1NJiHp0hy6Lcg6XG57Ujxm7jR_qCukz5fPasfVpoSCX7hsJeCJDel7OqrSTfYb4VWAVRvAxY4XoMOguF1gx1eXPpTLpb8Y_JKdVv9wRqQK2l7oflnRbotZX9MCd6yZkC-0gz5kNtjmwxHuvgQXqWZzgQ2Chg5yzRlatXg91sQRgal5WhEqnpi6su7QMwAaSsw4fgsBkqPSFHRGg-E7waW5PvHJz3_0eRO7vfLDgwCTkvSectw2imw1x9AuEpVa4qvlr5II8UOVfWRZRPW3KsFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو جانی: ما می‌توانیم ظرف چند روز مشخص کنیم که آیا کمک خلبان ارتباطی با ایران داشته است یا خیر/ الجزیره  #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/694568" target="_blank">📅 16:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cd932658.mp4?token=uvwnfysO7WUKZt7PzjxTZDJNtPwBe2vvCaK0HLEurKfZ-BdW9MDNuHFrl2iBKTl3SB4gHYtqHhtIDHMwxYKs8uMxXFiYlE77tSry2XKgHBjUzDIZ0w0_VSCBl_3Ob-q9CFfm0W1JOgtS-BHH_QaTZo81Dw-jMkD4PuQvtAQhqVOlE4dYhWRXXvU5sQfLwA6CYS2foS6E96uPLeTl3N3WTcmOjCH0A1kWxIr9np_TDTXtc1AfvoW7VP2LEyAc2UdRG2E6SJrOlTyVDjjytvuJ4AGRCcna_rmB46L9hx3qwvNzHfRZq8KzNgkHhXD9y7XXGnIR2fbxYXA-0w0iaxe6QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cd932658.mp4?token=uvwnfysO7WUKZt7PzjxTZDJNtPwBe2vvCaK0HLEurKfZ-BdW9MDNuHFrl2iBKTl3SB4gHYtqHhtIDHMwxYKs8uMxXFiYlE77tSry2XKgHBjUzDIZ0w0_VSCBl_3Ob-q9CFfm0W1JOgtS-BHH_QaTZo81Dw-jMkD4PuQvtAQhqVOlE4dYhWRXXvU5sQfLwA6CYS2foS6E96uPLeTl3N3WTcmOjCH0A1kWxIr9np_TDTXtc1AfvoW7VP2LEyAc2UdRG2E6SJrOlTyVDjjytvuJ4AGRCcna_rmB46L9hx3qwvNzHfRZq8KzNgkHhXD9y7XXGnIR2fbxYXA-0w0iaxe6QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر فکر می‌کنی دیر شروع کردی و به هیچ دستاوردی تو زندگی‌ات نرسیدی، این ویدئو رو ببین! #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/694567" target="_blank">📅 16:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d731a499.mp4?token=XxHiXdD0nu-95swkg5Wgn_2_pDsQVC0_bGWZ0WYWJRMnToejFqQwHT3ORX6QFHP_NIn8B9AbFcReWE9geyxIy5zB1ubTKtXsN4kJHg-jRlgp5ttGN9dDQvUjO-CYw0z1syiijiPYTH9GiNcxjAtb2yeDZt2QZOW5DJC-F2KMLkLDx9s4l52-fF5RAac_jQYX-hpQHOlhlnv0un1uvaIDY2M907NnD6ntvxUM48JHJ2Q8Y6wqBzsPURF5B6jooPXyXJiD8E4qmO6Vgbaz1YLmAf6Ycqc1JHES45lz1SA6H-RwlBO0gtl7cBcsAF4bVc869bhBxRQeCrJizzpqOQjqITPmhU6HssclnlXQa_sb1TV9EIPBW7HhEpJY-nIHmMuyzydkYLQdS4PSCUslx4iHqo0G3r-3_XPSZDzOBcb-uGSTTgL_0djBsOFxvy1sPCkE1sNqZD1_ODt-rQOGpWfvC2z8h78gbu-t9MyS-C6gWqezr-TyhZ9YahjdSazbZM--d28UVSdGyMKVFWOzZOxStitA9ozGrHbVsqwyyTy7gp5e-2VVHD0z_evyJ6OZBE9sANLGHDUIiaH8zD2oYQniijSgJRNdgt3u3zyrizKgZKag7Pa9LthwQ6bSkOYNf7IgRpirld3F0DNxmZdMY9Qa9ubuA4nl1PrCvbVd9ppbUZc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d731a499.mp4?token=XxHiXdD0nu-95swkg5Wgn_2_pDsQVC0_bGWZ0WYWJRMnToejFqQwHT3ORX6QFHP_NIn8B9AbFcReWE9geyxIy5zB1ubTKtXsN4kJHg-jRlgp5ttGN9dDQvUjO-CYw0z1syiijiPYTH9GiNcxjAtb2yeDZt2QZOW5DJC-F2KMLkLDx9s4l52-fF5RAac_jQYX-hpQHOlhlnv0un1uvaIDY2M907NnD6ntvxUM48JHJ2Q8Y6wqBzsPURF5B6jooPXyXJiD8E4qmO6Vgbaz1YLmAf6Ycqc1JHES45lz1SA6H-RwlBO0gtl7cBcsAF4bVc869bhBxRQeCrJizzpqOQjqITPmhU6HssclnlXQa_sb1TV9EIPBW7HhEpJY-nIHmMuyzydkYLQdS4PSCUslx4iHqo0G3r-3_XPSZDzOBcb-uGSTTgL_0djBsOFxvy1sPCkE1sNqZD1_ODt-rQOGpWfvC2z8h78gbu-t9MyS-C6gWqezr-TyhZ9YahjdSazbZM--d28UVSdGyMKVFWOzZOxStitA9ozGrHbVsqwyyTy7gp5e-2VVHD0z_evyJ6OZBE9sANLGHDUIiaH8zD2oYQniijSgJRNdgt3u3zyrizKgZKag7Pa9LthwQ6bSkOYNf7IgRpirld3F0DNxmZdMY9Qa9ubuA4nl1PrCvbVd9ppbUZc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهنام ابوالقاسم‌پور در لبنان: به‌عنوان نماینده ورزشکاران به دیدار خانواده‌های شهدا رفتیم و انگشتر متبرک آیت‌الله سید مجتبی خامنه‌ای را به آن‌ها تقدیم کردیم / تازه از نزدیک فهمیدم مردم لبنان با چه شرایطی زندگی می‌کنند و چقدر نسبت به ایرانی‌ها محبت دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/694566" target="_blank">📅 16:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای نتانیاهو جانی: ما می‌توانیم ظرف چند روز مشخص کنیم که آیا کمک خلبان ارتباطی با ایران داشته است یا خیر/ الجزیره  #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/694565" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اطلاعات میلیون‌ها نظامی آمریکا هک شد
پنتاگون:
🔹
اطلاعات شخصی حدود ۲.۸ میلیون نیروی نظامی فعلی و نزدیک به ۳۰۰ هزار فرد فوت‌شده آمریکایی در یک حمله سایبری به سامانه اطلاعاتی پنتاگون به سرقت رفت و هویت مهاجمان همچنان مشخص نیست!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/694564" target="_blank">📅 16:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe71894de.mp4?token=N5KLExrAFFkdcsDoG99yOZfmGwns_Z6s3g86LSkacotSfh095fq-RbWd8lMq5q41hKXsYw-Qu4RC9XtvK8GMit79nkdumwQZZIGyuxf_NAnNacVpq50R9aLHHsunCSHEqgqBqn65xs26hWNL-ki7JwXXhsv_bt5tO7rtMsTlhBPoLvV9_Z0FANXaAVxwKjYbkSxM5iM4xAOuLMvA3tOnoM4dN6jMGDOYcP8W-oo1F_MBl66iHgfy4Y_6p8cUQV8Xxhg-FZDy7IbK0ijnJaND2uayv8UWi_YhYZrt4Dv_PzpBGQDOpVxI4OFrVa5DLtqyioFW15cGzRUdhtQBqcLVag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe71894de.mp4?token=N5KLExrAFFkdcsDoG99yOZfmGwns_Z6s3g86LSkacotSfh095fq-RbWd8lMq5q41hKXsYw-Qu4RC9XtvK8GMit79nkdumwQZZIGyuxf_NAnNacVpq50R9aLHHsunCSHEqgqBqn65xs26hWNL-ki7JwXXhsv_bt5tO7rtMsTlhBPoLvV9_Z0FANXaAVxwKjYbkSxM5iM4xAOuLMvA3tOnoM4dN6jMGDOYcP8W-oo1F_MBl66iHgfy4Y_6p8cUQV8Xxhg-FZDy7IbK0ijnJaND2uayv8UWi_YhYZrt4Dv_PzpBGQDOpVxI4OFrVa5DLtqyioFW15cGzRUdhtQBqcLVag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج از نشست به یاد ماکان و هم‌بازی‌هایش؛ وقتی قاتل هزاران کودک در سازمان ملل سخنرانی کرد
🔹
ویدئویی پربازدید که پرس‌تی‌وی از نشست سازمان‌ملل منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/694563" target="_blank">📅 15:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای نتانیاهو: خلبان هندی ناجی جان ۱۷۴ اسرائیلی در پرواز فلای دبی بود #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/694562" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe40db7c0.mp4?token=MI7axdmIhlAS-3bC-2k5nxdtEEUbnMYpN3d8Fqw0nj46WRy7PcS4rC6E_g2xcGSN8KUXjizT08r4w0cbsKIr7mrlKYt033G-Ct9JMWk2PXXqbiMTLjJc40YbhEAkIkw1R3e1FjqqPKFuXbAyjZTg6dZfV2e7I12VWPA26IHfopLJiNsGzlAE7aAVE_2brSjiC43Pgch71s0G3euwZu8YAmpvjFsJB2DL92YUV3rgsOAzV2o24RUe5Rse-zYkC6w_kujHWCEj7nymC6jY7Kylq-YvfNNMj6wyiwW7qYwN4mOKKhx8Ur91YsBMzYY4vu0WheCZYgnzCo4WnAJ31mmUyLSn2nx2votCI8IWdFdizyi1ICVgDBJkL2sUq56dk7R5oB3GC3_aA08COD3zsbgW26jPJNwhX0VkZwAGoz6-t1kZ_OBwVtj8ACFUoNqEU_gnuZGXyOmePMWsfRWxZFb1OLug2JQjCMMYuIuA0D1V36EUGWL5tYoXvo2VyrMXLl5Eo5HuIWW74wPtg-nLQ73VpM7kjMFs3Nhg3EfFPsrsGa-ZVyOcakVXdvucRriV18vgyfq1kGyZkVhGn7qL84wehqS1D35HLpuPdgpYRudqb6qCnnNAsltu5FmT_-c9JuQziwtmXJN_QkMNw7uCGCcAiMMwS_tO96ylxwUGm-FJgUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe40db7c0.mp4?token=MI7axdmIhlAS-3bC-2k5nxdtEEUbnMYpN3d8Fqw0nj46WRy7PcS4rC6E_g2xcGSN8KUXjizT08r4w0cbsKIr7mrlKYt033G-Ct9JMWk2PXXqbiMTLjJc40YbhEAkIkw1R3e1FjqqPKFuXbAyjZTg6dZfV2e7I12VWPA26IHfopLJiNsGzlAE7aAVE_2brSjiC43Pgch71s0G3euwZu8YAmpvjFsJB2DL92YUV3rgsOAzV2o24RUe5Rse-zYkC6w_kujHWCEj7nymC6jY7Kylq-YvfNNMj6wyiwW7qYwN4mOKKhx8Ur91YsBMzYY4vu0WheCZYgnzCo4WnAJ31mmUyLSn2nx2votCI8IWdFdizyi1ICVgDBJkL2sUq56dk7R5oB3GC3_aA08COD3zsbgW26jPJNwhX0VkZwAGoz6-t1kZ_OBwVtj8ACFUoNqEU_gnuZGXyOmePMWsfRWxZFb1OLug2JQjCMMYuIuA0D1V36EUGWL5tYoXvo2VyrMXLl5Eo5HuIWW74wPtg-nLQ73VpM7kjMFs3Nhg3EfFPsrsGa-ZVyOcakVXdvucRriV18vgyfq1kGyZkVhGn7qL84wehqS1D35HLpuPdgpYRudqb6qCnnNAsltu5FmT_-c9JuQziwtmXJN_QkMNw7uCGCcAiMMwS_tO96ylxwUGm-FJgUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژیلا صادقی در مزار گلزار شهدا لبنان: آنچه در جنت‌الزهرا دیده می‌شود تداعی‌کننده اتحاد و غیرت است؛ در ورودی این گلزار مشغول نصب تصویر رهبر معظم انقلاب هستند / امیدواریم جشن پیروزی جبهه مقاومت را در کنار مردم لبنان برگزار کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/694561" target="_blank">📅 15:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1761a9ad21.mp4?token=C1cyEIP330pClF3RRJtF7Bh7VW8soPlc3jmYIBAb2PGHnXo0G6fr0esPod_nllWATnK7uaulrxVPJrDuJdr5zk_ruCUwm9V49pfOmRTpL_6k7Xi7BHpF9jl9y9ed28p85aX80Zrecjk7TLG-cE5zs-1nd6940VaNAk0e1xapnF4o692_wOSTZuBSHDD2Q7NpBL2K47HVsWiK8seWl8Yz43S9at-5QSWbnEv2dBoflaskllZJ410OGe-rndbyT6JmJCCHvb7w-F0_DtzfnQyIG4ivHYXgrvtDDl3IYb7vTYIuAWRJbqrI7BrRp7AOBexQXtVkRKV5coBHWFBxi9Xu5Zk3MSOYGaN9ik80pSvUwjh8OcA1VBRPEh3CYaleYmQj8yKY4mw_UArHZXYBC0KEGZvsIxMfgShmvqnwEj0km1rMIaoouQMZGl16xwfBn7AoJEog2Q7jJQfCoKQS30TH-8weNnlH0fFdzuJRcWXvOMDgsy6oa50dxSTJIfGfjgnK24qfzFFTZpNQ8VW1JtoochSstiqNfHwachE34m8zVhjdamwkUmNAxBUc1OPjQ68frOQY0r5Ie2wZHjKDiAmaTLsAJ-obSAqT7gO80nMzhnhpgjhd5n7jyhGwZWFIqZtr9RdWpAqR90FQvtLeDs-SUl1S3ZQF5CdXRWziIJjIWAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1761a9ad21.mp4?token=C1cyEIP330pClF3RRJtF7Bh7VW8soPlc3jmYIBAb2PGHnXo0G6fr0esPod_nllWATnK7uaulrxVPJrDuJdr5zk_ruCUwm9V49pfOmRTpL_6k7Xi7BHpF9jl9y9ed28p85aX80Zrecjk7TLG-cE5zs-1nd6940VaNAk0e1xapnF4o692_wOSTZuBSHDD2Q7NpBL2K47HVsWiK8seWl8Yz43S9at-5QSWbnEv2dBoflaskllZJ410OGe-rndbyT6JmJCCHvb7w-F0_DtzfnQyIG4ivHYXgrvtDDl3IYb7vTYIuAWRJbqrI7BrRp7AOBexQXtVkRKV5coBHWFBxi9Xu5Zk3MSOYGaN9ik80pSvUwjh8OcA1VBRPEh3CYaleYmQj8yKY4mw_UArHZXYBC0KEGZvsIxMfgShmvqnwEj0km1rMIaoouQMZGl16xwfBn7AoJEog2Q7jJQfCoKQS30TH-8weNnlH0fFdzuJRcWXvOMDgsy6oa50dxSTJIfGfjgnK24qfzFFTZpNQ8VW1JtoochSstiqNfHwachE34m8zVhjdamwkUmNAxBUc1OPjQ68frOQY0r5Ie2wZHjKDiAmaTLsAJ-obSAqT7gO80nMzhnhpgjhd5n7jyhGwZWFIqZtr9RdWpAqR90FQvtLeDs-SUl1S3ZQF5CdXRWziIJjIWAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی سیلاب اخیر گرگان، این موش هم برای نجات جانش دست به هر کاری زد!
🐀
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/694560" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR6xpKOUHdg9wTOQEtuhSdH2yJiugSFi35o_NgXHSewubBlPdkznhVZhKcg2XmB_Pmuaxc1IXcLS7nSzVTv9Q9Ha7t-RVBSBA8IG6VjrLZ0NPfsbg3zSpwivu-C1X6ClApmMoYAP83lnr0IY3l2r9PJrUbk9WlpUerXIpunroEqqpAKUY6hlx1i96IQwF4PnV05qZeBtIfwYlpiijnFlib31ygAmYpf7USZ5adNOoQ8K9kA4trDWa_cvhCdsU9y-ZBcSKcsoyVj-9_lpHRI_51BrxK7IjBQ1RVb7ecQSQrtaDeXNwoIQkWkje_MOFfqrNKQP7X40gXFW243lKSADQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاخیردوباره در حذف مدارس سنگی و کانکسی
🔹
قرار بر جمع کردن مدارس سنگی و کانکسی بود؛ اما وعده‌ها یکی‌یکی به موعد بعدی منتقل شدند. از «جمع‌آوری» در سال ۱۴۰۳ تا «نبودن مدرسه سنگی و کانکسی» در سال ۱۴۰۴، اما حالا وعده به «تعیین تکلیف تا مهر ۱۴۰۶» رسیده است.
#اینفوگرافی
#وعده‌های_نافرجام
@Fori_Graphi</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/694559" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3cb7d903.mp4?token=kWpKvFGIXoSSh24SlOjvlmXXIc1h-ASCfAJ2K1C-a-wa4Er66q3P729f8OZUh8ck9wEOoA8v6B26Ob_kTvdJR-VjlGqshuzV-0Ukvgwn_-kPWOGZ0GJBwbzsYt6KgOGS6jAS7GLVAIYeDgEPH2lwa46HQN0Cupv5guki831CGvULRlTIfzfC72BBoiA3-jF-nOk5qIb6ERmpj1JfAMRNXZRrU8fXtZq6QrW0bJ1wG7co5ocpG7giQrjq1V_r-4dSF2n5GKaEBxTLh-fg3ZAcQoxM1Or_JNDcRUkJnEVhyFL4U7JDW8IjV5D22lgc72u3sDj8BJdDSnj8aXuzlFezDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3cb7d903.mp4?token=kWpKvFGIXoSSh24SlOjvlmXXIc1h-ASCfAJ2K1C-a-wa4Er66q3P729f8OZUh8ck9wEOoA8v6B26Ob_kTvdJR-VjlGqshuzV-0Ukvgwn_-kPWOGZ0GJBwbzsYt6KgOGS6jAS7GLVAIYeDgEPH2lwa46HQN0Cupv5guki831CGvULRlTIfzfC72BBoiA3-jF-nOk5qIb6ERmpj1JfAMRNXZRrU8fXtZq6QrW0bJ1wG7co5ocpG7giQrjq1V_r-4dSF2n5GKaEBxTLh-fg3ZAcQoxM1Or_JNDcRUkJnEVhyFL4U7JDW8IjV5D22lgc72u3sDj8BJdDSnj8aXuzlFezDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر یارقلی در برنامه نزدیکتر:گاهی برای حال خوب بیشتر از هر درمانی به آدم هایی نیاز داریم که دوستشان داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/694558" target="_blank">📅 15:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
خبرنگار مجله‌تایمز: نظرسنجی‌های شما هرگز به این سطح پایین نرسیده بودند!  ترامپ:
🔹
اینها اعداد جعلی هستند. من امروز می‌توانم هر کسی که در انتخابات شرکت کند را با اختلاف ۲۰ امتیاز شکست دهم. افرادی که نظرسنجی‌ها را انجام می‌دهند، فاسد هستند. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694557" target="_blank">📅 15:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198e221736.mp4?token=BEfDiM5mfjCr7-VT3BLclbrizf5eI--sLLydJsl_T5F_rqR81UpOSmKaan9-bftrTVgVG8ufmtAL8UTnL8MoOLxWAva65dr9qV1DbhlRSH719K4curAEjKGvuUH_kLq0SxORt0yfOcL6i0md3dIU4h3PAGVH0OpqmZAbSACm76EH-wmgKGODaiHLPPB2V4iEBfx74g94PiWO0fWGA-Ioe-aHSAf3-ggjrCbMs5iC-GVQKQ9UQAcZXDWmkBwoTBX4yznp7tGJ5ew6ut-XNUMkf7ts1ncnVfn86H9DA6LO2v-fJeo1-2de4jYmd2uu-8EkCW2UlCwt9W3vymlFyM_-vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198e221736.mp4?token=BEfDiM5mfjCr7-VT3BLclbrizf5eI--sLLydJsl_T5F_rqR81UpOSmKaan9-bftrTVgVG8ufmtAL8UTnL8MoOLxWAva65dr9qV1DbhlRSH719K4curAEjKGvuUH_kLq0SxORt0yfOcL6i0md3dIU4h3PAGVH0OpqmZAbSACm76EH-wmgKGODaiHLPPB2V4iEBfx74g94PiWO0fWGA-Ioe-aHSAf3-ggjrCbMs5iC-GVQKQ9UQAcZXDWmkBwoTBX4yznp7tGJ5ew6ut-XNUMkf7ts1ncnVfn86H9DA6LO2v-fJeo1-2de4jYmd2uu-8EkCW2UlCwt9W3vymlFyM_-vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعقیب‌‌گریز و دستگیری سارق متواری توسط‌ ماموران پلیس‌آگاهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694556" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
نظرسنجی جدید درباره ترامپ؛ جمهوری‌خواهان وحشت‌زده شدند  وال‌استریت‌ژورنال:
🔹
در آستانه انتخابات میان‌دوره‌ای آمریکا، محبوبیت دونالد ترامپ به پایین‌ترین سطح ثبت‌شده برای یک رئیس‌جمهور پیش از انتخابات میان‌دوره‌ا از سال ۱۹۹۰ رسیده است.
🔹
بر اساس نظرسنجی جدید،…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/694555" target="_blank">📅 15:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEqRxe7ChEjMuBl6UySynea7RtpiVyA19xv8CBU5lW2Y4V6U-pBG23iSJEAqeuXXbjI2bK_8vlIBg-aP-4J3GThkWvLU2AZReZ2xlHidpLnxOlbK6c4lXnO_1ePO61Y22MyBzcB5ejg-jUSuiBHfVTHVV3fZGDWDnXSOD8j1pJt4j4HgTLXL0tqFgkhANYNQ9mM-NkKEj7KdWnCoCiH-RAhJOqdGL1P5JgwsKB2U3sFESDwjA2hhm-C6A_RgpkD0UpuEq_bmB29Ok66BmFHlmtUPAjkN3BC33Hf7gv_8_oEJLfn5_7GGEJXZbw-CrSb7S1077S6xkETgdESz48Ed7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چند ثانیه یک نوزاد در غرب آسیا متولد می‌شود؟
🔹
بررسی نرخ تولد در کشورهای غرب آسیا نشان می‌دهد فاصله زمانی تولد نوزادان در این منطقه تفاوت چشمگیری دارد؛ از چند ثانیه یک تولد در کشورهای پرجمعیت تا چند دقیقه در کشورهای کم‌جمعیت‌تر.
🔹
بر اساس برآوردهای جمعیتی، در کشورهایی مانند ایران، ترکیه، مصر و عراق به دلیل جمعیت بالاتر، تعداد تولدهای سالانه بیشتر است؛ در حالی که کشورهای کوچک حاشیه خلیج فارس فاصله بیشتری بین تولدها دارند.
🔹
این تفاوت‌ها تحت‌تأثیر عواملی مانند جمعیت کل، نرخ باروری، ساختار سنی جامعه و سیاست‌های جمعیتی قرار دارد و تصویر متفاوتی از روند رشد جمعیت در غرب آسیا ارائه می‌دهد.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/694554" target="_blank">📅 15:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694553">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ترامپ متوهم برای چندمین‌بار در طی روزهای اخیر: دیشب بیشترین مقدار نفت را از تنگه‌هرمز عبور دادیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/694553" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694552">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6368419f.mp4?token=PPFcJFibCGcjzBAuEZVwto3RtoDMPs-fO0tB93XYbXGAHwkTWFUZjr3IZnP8epRplMRL45U3N1lJmmtmLg8tsL_ejtyd5NqhsVE58SYw0hzskQ6iRcLq8Uf8B1Hr1ve0w7EIGL06FAHqbNDo1anqJylxTazAh_rGQsRDUkdj_pAWxsLd5UOrWIJEMuNy_vWthFbN9LwMNNszforH3dd0jbMkTbelqIM6_giDosEglSqkcv3rNQ3hJG_YwzRe65CGqarPVGOMsz5SAYwEDVv7eufAcfeMWUO5gEOjJp4XXLCvDiib-nwc2KUqXiy-SIGAFLGXvsYyYo8Wr7rwZZMZhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6368419f.mp4?token=PPFcJFibCGcjzBAuEZVwto3RtoDMPs-fO0tB93XYbXGAHwkTWFUZjr3IZnP8epRplMRL45U3N1lJmmtmLg8tsL_ejtyd5NqhsVE58SYw0hzskQ6iRcLq8Uf8B1Hr1ve0w7EIGL06FAHqbNDo1anqJylxTazAh_rGQsRDUkdj_pAWxsLd5UOrWIJEMuNy_vWthFbN9LwMNNszforH3dd0jbMkTbelqIM6_giDosEglSqkcv3rNQ3hJG_YwzRe65CGqarPVGOMsz5SAYwEDVv7eufAcfeMWUO5gEOjJp4XXLCvDiib-nwc2KUqXiy-SIGAFLGXvsYyYo8Wr7rwZZMZhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت جواد قارایی از لحظه هدف قرار گرفتن و نجات خلبانان ایرانی در لواسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694552" target="_blank">📅 15:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694549">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V54RNd6U-YvYnO-hunRq8L5Xm2jPVyJjy7tKRXGFiRMgw1I1xP6-INQgWg7iGgRUcfSnpzo0R7ySDwdNiY1Qs7Htb3tCje2y9Luu7g7g1fKSskOwJMhEfm-W6GFudbeXA707q59Ms4xIunM5FhHzLBHiFVujZWSOCZuXAQympl-VVeVejWe6HF2UzIv-Xz50ju3D6npY_OKcXSxiJjY5MHmYWev7eUfOVJM5gGaGB68yn8DTLjSxpE5_gDDczXnzCjBOMQQhp4LjMo1xwBLbTfzrN6XGC_kXKkF0isxwrsvqMdvaqKB3D_QlE0lI_zTJgoxlo6itv87LNN7cRYRqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzTG2nzh_eOBe4v5Sia-_6dtBgwcohDRvzVJgeH9TJnSM6QujQtwWRMum-5QbPOA7E71ZMta0a2ifFT8Cty1o2NpvluYJ8FDCS-ZMQZWkPrvczLU2eTWgJc2D66qxphf5-2g4JbkEEB12BguPZvVlPrNPvhIab3oKM1xXglp3Kes4AX3LepCuv8xHSvFIsTxbLaVKtO4QugKy20e1miGDTa3rptAPIe12hefOKMlix4KvUvFoWI6u4lqME8k5cx3yOi4PgMeb2IcRbNGY4GBd8PKPY4VjT1B1ylHueZ6bULhsn5CVWflbBDnMOdBEWe6_NUD3Zvu2BvYn6bP5iJmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSGrH6Gp-s0TEVd41sbdzHZ_pP0aczROYhyKuV45syG0g7I8ERSZZeWPX_DgUvcCWQHVSCcFzz5PHJyRbiHlDsK7oJYbVn7F6be9guIj1B3_SXNy8tSjqzPrrFMdNqn50BGbfKS2jbv5lldnAyMHG406nuNlYyEqXI2U0ES2bUVNPmQfKtDNqBDB6yZZfmNr5r33iKqMekK7-vU2XTcV4GzmEsX-RNFempHkC2Yf7Oadxp3cCLN7Aa_sC5k7dCnFg4PblTfT59CX0rZu1v3SMsLH89JL3Q_CSvpi1l3gITdUBd28UN0Ip1lCzHg4l5WwJ1FxZ97zT13p8xPOf9ZjmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت یامین‌پور از اهدای انگشتر متبرک رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای به خانواده شهید حسین هاشم: دیشب را به زیارت خانواده‌های شهدا گذراندیم.‌ الماس‌های درخشان در خانه‌های کوچک در کوچه پس کوچه‌های ضاحیه...
اینجا خانه‌ی شهید حسین هاشم است‌. سه فرزندش در سکوت آمدند و دل ما را آتش زدند.
این شهید به‌خاطر اینکه در ویدئوی وصیتش مکان و کیفیت شهادتش را توضیح داده، در بین شهدای اخیر مشهور است.
با خود چفیه و انگشتر متبرک رهبر عزیز انقلاب آیت‌الله سیدمجتبی خامنه‌ای را آورده‌ایم. هربار نام امام سید مجتبی را می‌آوریم صلوات می‌فرستند. همسر شهید یک کلمه هم حرف نزد، چفیه را روی صورتش گرفت و اشک ریخت
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/694549" target="_blank">📅 15:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694548">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b30665a573.mp4?token=CLczbQgu8c3J0uLmiLazB68Le6qsIBGvKeVDWWzTZqc6Wo-gZixqai1D9_solanjOTQCrXlo8UwsH9cPdcUK0nFkPQop7CxL1SQF4qDXBrpQFcfZmQ2iLnQWtiZRv8wlNlNjgZ37XHUL8MQOvY-a0JAPcD2RLACO-ujibW2WN3ajnueGQ6XWSPxgs5gBjZS4sojmCwVrivZnkHylDOo-ucdP3VryPaDUU_XyYQnO-yvmAdZb5vYdtmP4e5e_oAO5sA0g6hdSl9f5wmx9yNKcdG7lgmzVIgu2IG0tr427OTSeTs9N5NwcX3av97qCWoNtW2oYpBS-nH4bFyGARojQq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b30665a573.mp4?token=CLczbQgu8c3J0uLmiLazB68Le6qsIBGvKeVDWWzTZqc6Wo-gZixqai1D9_solanjOTQCrXlo8UwsH9cPdcUK0nFkPQop7CxL1SQF4qDXBrpQFcfZmQ2iLnQWtiZRv8wlNlNjgZ37XHUL8MQOvY-a0JAPcD2RLACO-ujibW2WN3ajnueGQ6XWSPxgs5gBjZS4sojmCwVrivZnkHylDOo-ucdP3VryPaDUU_XyYQnO-yvmAdZb5vYdtmP4e5e_oAO5sA0g6hdSl9f5wmx9yNKcdG7lgmzVIgu2IG0tr427OTSeTs9N5NwcX3av97qCWoNtW2oYpBS-nH4bFyGARojQq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خنجر از پشت امارات به امنیت منطقه/ ابوظبی چگونه بازوی اجرایی نتانیاهو شد؟
علیرضا سهرابی‌پور، تحلیلگر و کارشناس مسائل منطقه غرب آسیا:
🔹
نتانیاهو موفق شده برخی حکام عرب از جمله امارات، عربستان، بحرین و اردن را همراه کند تا ایران را تهدید اول منطقه جا بیندازند؛ امارات امروز رسماً در نقش بازوی اصلی رژیم صهیونیستی در منطقه بازی می‌کند!/ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/LCIixYhGzCs
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/694548" target="_blank">📅 15:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ترامپ مجدداً «ملت ایران» را تهدید به نابودی کرد
🔹
خبرنگار مجله‌تایمز: هفته گذشته گفتید ممکن است ایران را نابود کنید
🔹
ادعای ترامپ: بله، من این کار را می‌کنم؛ این امکان‌پذیر است؛ آرامش با نابودی ایران به‌دست می‌آید
🔹
خبرنگار: چگونه رئیس جمهور صلح می تواند خواهان…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/694547" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694546">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای ترامپ درباره شرایط ایران: پیشنهادی که سال گذشته رد کردم، امروز هم آن را نمی‌پذیرم  ترامپ به نشریه تایم:
🔹
ایرانی‌ها پیشنهادی درباره باز کردن تنگه هرمز ارائه کرده‌اند. من برخی از جنبه‌های آن را دیدم، اما نه همه، و به سادگی این پیشنهاد کافی نیست. #Devil…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/694546" target="_blank">📅 15:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694545">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150f73299a.mp4?token=YAH7snJD98iOXIlQNfpoId4mwfpvwDLZofqFfPhKOeHERbqImxQvhSz-qNsfMOb-jsN54kNy0GGQonhhlnKoJRROlNmaCLoeRuW8MGZG2Q-uZV5Yr0xa0ZIwP5_DLtQ6GMgZiCJ9DrKwzm0rHtlZT8KPeuXULWfnQeh0q_cv3UVUv514x9HXycHN65fnGTlmtLXsiOwH99Zox9tUj5G5SfmJnS50RFhFN87flsU-QvUDUH_VFshSfFretbxcDD5-_P0c6jZgBLxMh0GMYopdc2Lov0WON0pJqBY_QHnC7BGYUCqKOYuFQbGm5rUk3cN1Xw-rveh6IxvK2b-BzihY7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150f73299a.mp4?token=YAH7snJD98iOXIlQNfpoId4mwfpvwDLZofqFfPhKOeHERbqImxQvhSz-qNsfMOb-jsN54kNy0GGQonhhlnKoJRROlNmaCLoeRuW8MGZG2Q-uZV5Yr0xa0ZIwP5_DLtQ6GMgZiCJ9DrKwzm0rHtlZT8KPeuXULWfnQeh0q_cv3UVUv514x9HXycHN65fnGTlmtLXsiOwH99Zox9tUj5G5SfmJnS50RFhFN87flsU-QvUDUH_VFshSfFretbxcDD5-_P0c6jZgBLxMh0GMYopdc2Lov0WON0pJqBY_QHnC7BGYUCqKOYuFQbGm5rUk3cN1Xw-rveh6IxvK2b-BzihY7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورتون می‌شه اگر گوش‌هامون نبود نمی‌تونستیم تعادل‌موم رو حفظ کنیم و روی دو پا راه بریم؟ #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/694545" target="_blank">📅 15:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694544">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5t8Tq0nHAxRXXqDIdJ4Q5Bjez6g6erq07znqGLubNg9S-7GgSm25t_JEuMusdnvqoI_g-nNvB6E1xA2hhxahBIHmEG0NyEQCCe87IdmZQ3suXcnIkpl2bYAkpvU7q5RoujwVvqNMYFv39ve_WddCw6WMpQtViHzeoi0_xCK79sOvrwlGNrOhLeXiaFDmqy6LBYJ7jwW9qW7qY0uAR6E5dA2mSf2-wSD4vNKIh-uGbuFKbo1gsWbx0mSNm4zbo5rX94ivpEgQ5xeKpLLwfc0aoUQ2Vm4GI5RV2aHJ-gZJRpkjDH1Prsuj7K2W1pIl4Vzf8OtDlhyU1sfg3IK1l92bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری راحله امینیان از خانواده شهید حسن نصرالله پس از هدیه رهبر انقلاب/تلفیقی از اشک و لبخند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/694544" target="_blank">📅 15:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694543">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ترامپ دیوانه: من بالاترین ضریب هوشی را دارم. من بالاترین را دارم. من عالی هستم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/694543" target="_blank">📅 15:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694542">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ترامپ دیوانه: من بالاترین ضریب هوشی را دارم. من بالاترین را دارم. من عالی هستم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/694542" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694541">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b17db74fa.mp4?token=BPIqQsmRylTMdOEdH6_XwUB8OSNSGrF9PSAnN917iwX5DpUmdMAU-CkHtjH0kZf6ZAlbBE8OdH9x02lvv-nCskRfQZUrU_QD2eSFooEkMe4ZROcbefT-Yf-JNonT9GNDO8KfOTZaAjxzYatu_as2am_gHcSkQrwJmx2jcVCr8vyPDc8sZnQcpSE1wJ2qEDBH1vfroO1ipdz_h7Qvpwq9oB4NG2mCFNXnXSGDE3ZaoSvIlfW3VPsuCnx2ABu85tdwgP8hvy17yghAnnH19Q-GlcELmCU4pfuq6GTFAv5f_0cV3pM3f90SVgj5YrmljmtkHNcuWLXIWIzxvDno_k7odg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b17db74fa.mp4?token=BPIqQsmRylTMdOEdH6_XwUB8OSNSGrF9PSAnN917iwX5DpUmdMAU-CkHtjH0kZf6ZAlbBE8OdH9x02lvv-nCskRfQZUrU_QD2eSFooEkMe4ZROcbefT-Yf-JNonT9GNDO8KfOTZaAjxzYatu_as2am_gHcSkQrwJmx2jcVCr8vyPDc8sZnQcpSE1wJ2qEDBH1vfroO1ipdz_h7Qvpwq9oB4NG2mCFNXnXSGDE3ZaoSvIlfW3VPsuCnx2ABu85tdwgP8hvy17yghAnnH19Q-GlcELmCU4pfuq6GTFAv5f_0cV3pM3f90SVgj5YrmljmtkHNcuWLXIWIzxvDno_k7odg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط مرگبار بالگرد پزشکی در کالیفرنیا
🔹
سقوط یک بالگرد در کالیفرنیای آمریکا به کشته‌شدن ۲ نفر، انتقال ۲ نفر دیگر به بیمارستان و مفقودشدن یک نفر انجامید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/694541" target="_blank">📅 15:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619042ce0f.mp4?token=Q1q69Vp9PzA6CTRijUMKa9VY7mYyO1mhOZWv8S5kPk59l6fLsKYR7-9lpzq2ajTjjKLdjE63aTymFyIpbhQq_nWltU4-OAx-HM6GHnA7agj1LZtwM83UiL9CLOrLgq7pPFo2fdKQRNMX0BJakILgZTLgcqda78VvIyMGzMsMSuity2Vf-kGm3Qu-htMUFnf4fEvRszIomBShWVCsEuv_B_wM7dE1pQI2RbtrbMZ8pir6Yy20SFH3uacFVNyMW1dEiv4SEfq1q3GVpUFltgqmGNvKX5QcZbgWWhQzhHvhQtB0oveTeepiY_iQsGm8uwpTgED8JnJegHhOHfWQ91_hPYBzEutl4EtaJRefghIg_r0lfPENUBIPwsBtI1q90V6fY4dbjpyjpKoFOAZx131XquWWhHEUlgrJXYqQZtC4l4JoVIn7tph_95zjAPiNWgxtzY2nHOlT8yiv1LQPdr88SnU2QF5ooiK8ZLQbEmr4F3yKWrczzGcJ1mQLCRJSw1AKyRQROLNNgLcIGrpfHWrp8fgB9KzKzpRoqdUk4DWsSiQbWGFvTVmLRmqvRId0XihV-SKUiZw6yojWHGOpqTPr-1Cu3csFeO2RhKkhaSe_kC0fDp4KUTAo9-eaY3VAqonyUjDPqfqhwjuDafk16bJ9E-d6Sb1aOAGZIoiyifCsrck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619042ce0f.mp4?token=Q1q69Vp9PzA6CTRijUMKa9VY7mYyO1mhOZWv8S5kPk59l6fLsKYR7-9lpzq2ajTjjKLdjE63aTymFyIpbhQq_nWltU4-OAx-HM6GHnA7agj1LZtwM83UiL9CLOrLgq7pPFo2fdKQRNMX0BJakILgZTLgcqda78VvIyMGzMsMSuity2Vf-kGm3Qu-htMUFnf4fEvRszIomBShWVCsEuv_B_wM7dE1pQI2RbtrbMZ8pir6Yy20SFH3uacFVNyMW1dEiv4SEfq1q3GVpUFltgqmGNvKX5QcZbgWWhQzhHvhQtB0oveTeepiY_iQsGm8uwpTgED8JnJegHhOHfWQ91_hPYBzEutl4EtaJRefghIg_r0lfPENUBIPwsBtI1q90V6fY4dbjpyjpKoFOAZx131XquWWhHEUlgrJXYqQZtC4l4JoVIn7tph_95zjAPiNWgxtzY2nHOlT8yiv1LQPdr88SnU2QF5ooiK8ZLQbEmr4F3yKWrczzGcJ1mQLCRJSw1AKyRQROLNNgLcIGrpfHWrp8fgB9KzKzpRoqdUk4DWsSiQbWGFvTVmLRmqvRId0XihV-SKUiZw6yojWHGOpqTPr-1Cu3csFeO2RhKkhaSe_kC0fDp4KUTAo9-eaY3VAqonyUjDPqfqhwjuDafk16bJ9E-d6Sb1aOAGZIoiyifCsrck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژیلا صادقی در لبنان: مردم بیروت عاشق وطن، مقام معظم رهبری و سید حسن نصرالله هستند و اجازه زورگویی به باورها و سرزمینشان را نمی‌دهند / مقاومت ادامه دارد چون هنوز شهید می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/694540" target="_blank">📅 15:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694537">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181ece1d6d.mp4?token=lfJXsRmkfcafydic0J4YWaFbGkXavJ2HkwdPYtCfRxo4QusZIoa-m0PotpYj1XFGYkkci7eOW-2_D3v7-FLjLNVdrTlWXAt7kRCrx5ONYPOWj4Ow1ip1R8CM3slymepfxJ8Aijpp1J-2ywCdwzgrRHdKWvHXMVnBAC7UDDZVI1dXY24Kkul_cgQJKW6uBCAOw2aGIpVSB5kdnqrxW-HltBHBksDjMp6af1HCeHzAHFiAEgNjiMVA3gaRn0SCYKJn8RUiC5808wZOdO94qG5MF9prLYF13de58Em6VWOIqcoc9nCD1QAFSAII0D_Q1rTBm_qnHzA3fovrDbe-WPgKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181ece1d6d.mp4?token=lfJXsRmkfcafydic0J4YWaFbGkXavJ2HkwdPYtCfRxo4QusZIoa-m0PotpYj1XFGYkkci7eOW-2_D3v7-FLjLNVdrTlWXAt7kRCrx5ONYPOWj4Ow1ip1R8CM3slymepfxJ8Aijpp1J-2ywCdwzgrRHdKWvHXMVnBAC7UDDZVI1dXY24Kkul_cgQJKW6uBCAOw2aGIpVSB5kdnqrxW-HltBHBksDjMp6af1HCeHzAHFiAEgNjiMVA3gaRn0SCYKJn8RUiC5808wZOdO94qG5MF9prLYF13de58Em6VWOIqcoc9nCD1QAFSAII0D_Q1rTBm_qnHzA3fovrDbe-WPgKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری عجیب از نوع پوشش در هفته مد پاریس؛ استایل‌هایی متفاوت و غیرمتعارف که نگاه‌ها را به خود جلب کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/694537" target="_blank">📅 14:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8XzCVnKkZM-gaFc2n4CWyVSvgbSeZqnxMzOQOBYt9XvWCqBoxl2C5x1V7lYETjw9K0eD9QgwtZ8QYhLfq3BOcUosw4BNc0tgbD5BIGIKI9ShUCd0XTyugQtaJKjhXTzKLIN-7npdT--UuDdpe6bnGpDfGw6vBeBY31aVeFs92OKekMTvgVNGSJ-GF1UP1g94Ed_3Kz63C4NE2BCK50BWOuE8Qdj8jxzcpsJUy2XMhlHIWj8P705oUzXUyzx7hJrLrsXd_7jU3BC1Hgu0Nh0bsixWrybMmD2GAOV6-AvGZ1rhaIvPhGrSVx_oqOcB8vIhgParEaYn0oZY3LiBh0_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXyMcKEKS1HeTsog2bOWZc9IbTM6FR39Z8y2q2XJJDkwKgYQa3HjNoUgmTBu1ZBmHxZOOu5ysMuPmqPlqiYDrf6-GRHBXhsRPnmu53RzOHTq-GwB2VNmkJMU3ZBPzAkhETLlc_UkbFN0ZAVhMJ866PxCdVyDFEn5M3BAikl1KsYtqbUiJ_83hDowdUx0lIJhWKlUSY25uGsUmLfFObqHusdr2RVzddwr3WlJFOXBl6loxPMDczybcEVSdRIWLuOoW_I-kMioTzSBA_DMCEw4fSRi3sWykjW-dyE1NveaKdnatJ2alje0cMzb4BR8pHqCABkR3cwdWEmNpD-zNuhgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XL-fVltFYMiy4AxfbtoSPhLd4nfgUD9Odw7EH2TdEFhbYXVS5VpYAjkjG3bbGXNyrO8ZTrmSOKq-hNEcwiuQfyyEww99B1Yvb0RavC970OB1CwTX1O50tja6Unuahz6ny-rfaQgtqYC5RV5C8ofZDGW9RV6yRg0pVLTCzZyWLC35sNuhach-AL0CaN9Y6rW34zojSrDr9mNpjbU7u0iVcxnofqijHJcaRXNEiykw-0rRd3gtiyKxscj5N6g3lY_ufad7f2cABdR_tzEkttQ-BfU1u7A31SLILfUv0BxbbOiHJ8gBPl6whzrf_TqQDGcjQ90uKbtKwa2h10xI5qMaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgOocg36Wdo2nK5bcfn29Y2LAJvdL_gBqQClcGYELMIHLbpWKIMpQd3qjnvE3HQQ_e_wMO0A7ICObLxwKI4vFu5BwBAPp2_BSOqNiteRAp_Xi1xqopgAjE4Q0Ycq0KBTwE2r7c7ZZPWPNBBEY3aCDxHZFoA8CXMtl2sdzn5rqGIe_reejHbs-Q64epfKSJ1OozASBn8wahYVAGlTVpz1eAmhYyZwiDrtKfoIvj93Pf_B7mR2U11i2ovnW5pnfBKa7vvpIEYY0E5shv73Zaf-bq8ufrC4ywA9GyNUdwBBp5KLvinQW3mO-ju0lebgl1O1j6siyG_Y8pQ0RzlkxVBV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqeMY7LxbyH9865ejA6F3F0ZJeMFT8uDC8zAvSXa6IvhueLl-t0wNpITYI2M3sVntcT9z-LAjwkegvegILgKecM4ksg2uueDJ4CxD8uMU6wa3ukMFRkZ53GiZ6muIxdbKwIu6BcXolJ1nHnDocykBGfhxgBeJIumO_sCiGgx0pp3jQObgTHffvH1gkAoqrlUTRzhsBcAtXESlt7mVk-8xshjCkv6cQvIr1lIqv2xcb8gUH6AFoCq8byI79EFv8xBCynf2sbrv09tLxBhIOW3zl9diIFQIBg8QrxxFaODB-3T-qt7ssye5REjHqjThlJbmV0Wtu0YGnlgpFfGyo_J2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴
راه انتقال پول، پایا و سانتا چه فرقی دارند؟
🔹
پایا، ساتنا، کارت‌به‌کارت و پل؛ هرکدام برای یک نوع انتقال وجه کاربرد دارند، اما  کدام روش سریع‌تر است؟ سقف انتقال هرکدام چقدر است؟
@Fori_Graphi</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/694532" target="_blank">📅 14:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694528">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohgM2ycEIBk5y9qQUnnT9mPD_1iP_eDXftQMFGYlfNENvjXtGVSlf_yC6s_eg3ifpIB8UXKQ4cPt8aSiXA9v3X5nl5XPE7RkN9SAhVYRymkagCgoMIdO16b2GNmcw7tFZhpE9bnndAgEoOVdTFqDUz4GG89Ap8dJBqR3LwwRthAEjdxJfwjZOu8bTqM5kF9tNsbv5WNdyavXpbzotXSI8XUHWVIGxPXZ0DJMJbwP_aV7HFIZmNzSafcOUJZnEnBimqQy1ltW2dTNh9UqmMiGwNqbGc14uELVV4GLYlt6hGDsPoDWMX80yx4rWnJ-qK1EoDo1dRAmT2g-p_iHVhQt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lgljOKciVkr30Dac7UxS2isIUV7X0ygEPdYA_Kglor_fOSzEVQLTUliww6MEzJOE7SYnSFOEb2ZAPEm2xK_pHaUFLQy_4ql5fmyc3lU3bccGBEdVyJo8KcubW4xx3OF0HgF2AX_ZJJVlAV2I8NnBnmrXoL0ewAPzvig1k1Mv_IFkUMhcF3zH66bRjORjolm0z1RCml4pdVKWzsPII3hrc8fHJhfGQ-RiAtHAryShyFYX9UsNR0Cip0qZg3e60cZ1_nuAmhBDdVN6n-ST1jgrkLXVXy_885PbFVQwJVT_LDGpwhQsMj4OQ8uCDOjAf6n7KiYJ3AX_FwWV6rt-7fWkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lE9iNncGS_FdaVoNS7H9CvOebNlw5P0nfe8JYwXszp0hUmClIxn--UqUy1dRFOxLC0yc4Kn2_HRH42MYcmsLI9FLJ_fe-PVzGgqe08YxNPVYoiR5kpUhpXpAdryoC-oYcq5UAd3Tz_UaYZdn5qoaj6EApg0QrxOHTrgE3XrWmYZ-VMPuVCDkf-1zpTJr58r2PvXwQR1azQA4fqGaludUqsIqBVT2zGXka0fW3UF3gd-gHIBwegZ7szlro_IUYleNAjxKvViDGx40oDVsua23b1EvWpTL0URpxVn8AMq5WzMOWF3ftrz9gHBW0GDe2E5PfKZmxb9LLK8e0dQ5qOTqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmL5AwuZb_87TxZGNufKCT8zF9j7nPGMldJer20xNI8vD89xYL7mSiUDXdeWVFe6LNdaCNh2kJos7JRAT94iwOU5Rxp3ZgFGFQhfmKzU2ARLA_kcnzvPSTWECXclnBoqhFRZh92ibGDb2EMFDQ98kAujYb8YYfJ2tFRUhb8c7jSpUG5dLSSgM2oubuJ_bTkE3_Tqh8jRCkN_QdO53Ol5mEaPORZg8ikI-CbAePHKcjef4I3BWrpJ718wOnKInx8c5EPv5g5rZx1L3BeF9KGcHQkgRfpJSBln80RutqUkB3RZyg1fcuVCmvmTSXvpty-z2-3Oig780dDMrPhiYOs5ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست بوراک آشپز ترکیه‌ای از خودش کنار امیرمحمد شهریار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/694528" target="_blank">📅 14:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سردار بلالی، مشاور فرمانده نیروی هوافضای سپاه: توانمندی اصابت موشک بالستیک دوربرد به اهداف متحرک در چند روز گذشته محقق شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/694527" target="_blank">📅 14:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694526">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f16328c3c.mp4?token=JvXl4bSK8xHoJoU9UHRILm9Z3lC71MiwTc3tKLhdsya3aOA3clpOV0ppjpcUKqevgv8yfYdG-x1Wj5TM7cVQD1MtBLmK79VkQBf6L-9W3S0ttBFlB0U3K6u6b0p-zKpdHXtZEmVhtlpGTtu4PjRAZuYb5m9nX_2nyywWVhPkl8t72nASq2her0naiwJXQPJX-bGxTSahWkuXy-CDU9Y8tl4EiPVrGaXAh0n1l-K01gKsT1cnG2tu9Yp1Hqu6DWBqaEs8LS1ClJrZA8xDpzbpk_Vu3D4VP7dNTqTeKR3qcX9FfhiZBW8jqbI26fzk8zs1VyksdsNRnfgl4lenQsrSxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f16328c3c.mp4?token=JvXl4bSK8xHoJoU9UHRILm9Z3lC71MiwTc3tKLhdsya3aOA3clpOV0ppjpcUKqevgv8yfYdG-x1Wj5TM7cVQD1MtBLmK79VkQBf6L-9W3S0ttBFlB0U3K6u6b0p-zKpdHXtZEmVhtlpGTtu4PjRAZuYb5m9nX_2nyywWVhPkl8t72nASq2her0naiwJXQPJX-bGxTSahWkuXy-CDU9Y8tl4EiPVrGaXAh0n1l-K01gKsT1cnG2tu9Yp1Hqu6DWBqaEs8LS1ClJrZA8xDpzbpk_Vu3D4VP7dNTqTeKR3qcX9FfhiZBW8jqbI26fzk8zs1VyksdsNRnfgl4lenQsrSxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با آغاز فصل گردوی تازه، این راهکار ساده را ببینید برای جلوگیری از سیاه‌شدن پوست دست هنگام پوست‌گیری گردو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/694526" target="_blank">📅 14:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ4qD14pMX0F5QDLo72LGGDmqncABYu0vXFebuUkHwo301gtUq8M8gpVxjZ9B6zhAg4cxqCvwrpvWzsqsoTXnyWjaHs2B_siYcys9RpiS2RoJqiLdx4EpC1nTQpwUBer-2SNwSChRierC73rmJZdVN0wkFn_zHFS0FnpXSe8s5PmgcKFDa1RV_Y4RsEJgbXekooxW44kxitjWIW6CMfwUbivhmB-hKsuIDuZJv8_15VuYldyIFfCt32oPPNQp1CGsOXiJsoSbNrKpBU1zn2-N2EtL1wzI6SvPbsfQVlT5rWvDualdiKLj_QWVLXNX9w6cNPYcvCHIVUr9D-OmGf-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گام
بزرگ
بانک
ملی
ایران
برای
خروج
از
بنگاه‌داری؛
«
شفادارو
»
۲۵
مهرماه
در
بورس
عرضه
می‌شود
🔹
بانک ملی ایران در ادامه برنامه خود برای خروج از بنگاه‌داری و واگذاری بنگاه‌های تحت مدیریت، ۹۰.۵ درصد از سهام شرکت سرمایه‌گذاری شفادارو را ۲۵ مهرماه در بورس اوراق بهادار تهران عرضه می‌کند.
🔹
بر اساس برنامه عرضه، شرکت مدیریت طرح و توسعه آینده پویا اصالتاً
یک میلیارد و ۹۹۶ میلیون و ۲۴۵ هزار و ۳۳۹ سهم، معادل ۷۳.۶۰۸ درصد از کل سهام شرکت سرمایه‌گذاری شفادارو،
و همچنین به وکالت از شرکت سرمایه‌گذاری گروه توسعه ملی،
۴۵۸ میلیون و ۹۰۷ هزار و ۴۸۵ سهم، معادل ۱۶.۹۲۱ درصد
از سهام این شرکت را عرضه خواهد کرد./
شرح کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/694525" target="_blank">📅 14:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e7375a868.mp4?token=Q2s_-0SWPY3-56ELe5CwG5ZlMtFeCzCsaFdbWavwkduMeOvkUH6Xm4PF-uxhCOvQnQP9sXjazhySv0_24TIOlbxQwACouHtU0SQO2r8R0W9g70ULh8MVb6watSBDH-mAfHafBfCtZ_qU06844S5dSozDqZOnLKyBJHnHn2eRtema6zqmSj6oGfZP6UGvoYfKJk3b44Gi2XbiqINfNT17ZxdQv-ayb70lX2jfOVmWQ2xjBtfBmkx-4y7FxazVm3hLryrPR-nwFCDzvoc29VR_TRZIYjQ6RRiJ4oqICrHRTn5o2jGPRwmQDteg2FxYLZOKuls4OT40OnsAHZ2v49nQ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e7375a868.mp4?token=Q2s_-0SWPY3-56ELe5CwG5ZlMtFeCzCsaFdbWavwkduMeOvkUH6Xm4PF-uxhCOvQnQP9sXjazhySv0_24TIOlbxQwACouHtU0SQO2r8R0W9g70ULh8MVb6watSBDH-mAfHafBfCtZ_qU06844S5dSozDqZOnLKyBJHnHn2eRtema6zqmSj6oGfZP6UGvoYfKJk3b44Gi2XbiqINfNT17ZxdQv-ayb70lX2jfOVmWQ2xjBtfBmkx-4y7FxazVm3hLryrPR-nwFCDzvoc29VR_TRZIYjQ6RRiJ4oqICrHRTn5o2jGPRwmQDteg2FxYLZOKuls4OT40OnsAHZ2v49nQ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید از محل اختفای تروریست‌ها در زاهدان  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/694524" target="_blank">📅 14:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3eb5810e9.mp4?token=Pw8q-XBsfOGCZav9sktEBHGHBDDKx_xAp_a5_o7uyNyJhqq1qqkbm7la2_O7NBH_UsI74ifMBWtv5Mwju5wVQFHX9esfSVYESX2oOyJnGGZv2c7ZC7Y60XI-55mstEhmoFILa42xm9QgWxWaRxBGZJ6tgP0z0JD3FNtKDDXMHaFMnhTLQ5PlVUelLm7j89sIXtFjMHcEmBXP_LlhGKnMD6fSDwbDoeQkmA7cu2fB8e1PeprZHcGP13yNawkdYAXHvHHR6uPXETDvUQvul2vAxr5aRUI7MsxA1_-AGvCEGbcWUt6DzOH31kmJM_3_sc9c5kNOG6CAD4I9d4N6kMqWxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3eb5810e9.mp4?token=Pw8q-XBsfOGCZav9sktEBHGHBDDKx_xAp_a5_o7uyNyJhqq1qqkbm7la2_O7NBH_UsI74ifMBWtv5Mwju5wVQFHX9esfSVYESX2oOyJnGGZv2c7ZC7Y60XI-55mstEhmoFILa42xm9QgWxWaRxBGZJ6tgP0z0JD3FNtKDDXMHaFMnhTLQ5PlVUelLm7j89sIXtFjMHcEmBXP_LlhGKnMD6fSDwbDoeQkmA7cu2fB8e1PeprZHcGP13yNawkdYAXHvHHR6uPXETDvUQvul2vAxr5aRUI7MsxA1_-AGvCEGbcWUt6DzOH31kmJM_3_sc9c5kNOG6CAD4I9d4N6kMqWxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان دریادار، امیر سیاری از زوج پهپادساز: وقتی آقا شهید شد، همسرش لباس شوهرش را پوشید و به تولید پهپاد ادامه داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/694523" target="_blank">📅 14:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تصاویری از پیشروی نیروهای یمنی در جنوب تعز
🔹
نیروهای مسلح یمن در جبهه‌های جنوبی تعز پیشروی کرده و نیروهای وابسته به عربستان از این مناطق گریخته‌اند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/694522" target="_blank">📅 14:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
میلیتری‌تایمز: نیروی دریایی آمریکا تایید کرد در بازه زمانی ۲۰۲۵ تا ۲۰۲۶، هشت ملوان در پایگاه هوایی تینکر در اوکلاهماسیتی خودکشی کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/694521" target="_blank">📅 14:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694520">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed9d34d24.mp4?token=ZV2mrSuKP4fpTX9ASCjfU0ZKbIMTqwN4LNzkWHYNPgsKE4k7c3LhyvveJIVlS402Njqol2jtCJUWFN72AmDK6P2inxhLmEWzhQeIY0bN1yfc9j4PzRkPQdpkE1cR8NrHqUnB6RbFFYNXmojFKx-KgWDE16F-mlm_kfh8USX-p2He76ETW9FxCK1D1xFVYMTWn3F0EWojz_Cn-j65R1mQpdBliwD9Qv2s6gDY4InGk8-D7ShCXumTgX1st7tBv7cjfFdJ4_Ws3YytbE1nmmQXzC9DzBq5u12HlrLR0OBStk_7wvY1jsdbz0VNeeb4aSGF01wY3k-iPbv3WRvY_IAE84lXvzuA5oqBombwDt4Wrx3S-t7_2UAAh5R2UEyMMIE3XzXv133w6asFoarAW51I0NbESBLMyZiBfInumaJ_EbP-ncg_TPchu_AcK9-PKIxNY0JLOkz2zGKVwNDlJ053OIvfwXAzQvX8sU-BzbZ6P_v4DkrG8Tdq-el5wDfR70f-NtbuUxhxBS3fq8TVq3jIqUOKauEdwzeJRZ6fEhVky3jr0dytXDjaP2w-eJxHBRvc2WsRSMeZykT8ntvPDHX0G03bGRHAkji2M-sR6QURj8yqdBKlDlPN_4REm1Ao5_kHn2JsfwWKmszsgBT6T0V9aUWaRRJwVRRFUu0pmxFm84I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed9d34d24.mp4?token=ZV2mrSuKP4fpTX9ASCjfU0ZKbIMTqwN4LNzkWHYNPgsKE4k7c3LhyvveJIVlS402Njqol2jtCJUWFN72AmDK6P2inxhLmEWzhQeIY0bN1yfc9j4PzRkPQdpkE1cR8NrHqUnB6RbFFYNXmojFKx-KgWDE16F-mlm_kfh8USX-p2He76ETW9FxCK1D1xFVYMTWn3F0EWojz_Cn-j65R1mQpdBliwD9Qv2s6gDY4InGk8-D7ShCXumTgX1st7tBv7cjfFdJ4_Ws3YytbE1nmmQXzC9DzBq5u12HlrLR0OBStk_7wvY1jsdbz0VNeeb4aSGF01wY3k-iPbv3WRvY_IAE84lXvzuA5oqBombwDt4Wrx3S-t7_2UAAh5R2UEyMMIE3XzXv133w6asFoarAW51I0NbESBLMyZiBfInumaJ_EbP-ncg_TPchu_AcK9-PKIxNY0JLOkz2zGKVwNDlJ053OIvfwXAzQvX8sU-BzbZ6P_v4DkrG8Tdq-el5wDfR70f-NtbuUxhxBS3fq8TVq3jIqUOKauEdwzeJRZ6fEhVky3jr0dytXDjaP2w-eJxHBRvc2WsRSMeZykT8ntvPDHX0G03bGRHAkji2M-sR6QURj8yqdBKlDlPN_4REm1Ao5_kHn2JsfwWKmszsgBT6T0V9aUWaRRJwVRRFUu0pmxFm84I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهدای چفیه متبرک رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای به رزمندگان مجاهد حزب‌الله لبنان در خط مقدم نبرد با ارتش رژیم صهیونیستی در کنار رودخانه لیطانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/694520" target="_blank">📅 14:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694519">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
بدرالسادات عراقچی، خواهر سیدعباس عراقچی وزیر امور خارجه، دار فانی را وداع گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/694519" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694513">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHEUZX-thYu-3tSQ5lDizmFX_3UpdNNX5OYC12YUMBOXreLIM96FXTzI3LAMeZU-cs6xdoDlmlr_xQNC5Y_DNxYx2pcU1jytCybanmRywBLKid6J9urkDBOeiZoUtlbIGkNGcre8Eb0yst8NHgAmdBR2lWQ6y1j0pt-CdyOaF79Z43Ew9ULZdC6nsLTjFAx4ZVBvDXQwPzkNjpTemMnXWeNhMfHItXknaZiMb_aF_iFITjaIjbTdjnA7y31ONhxhUvx1DsHSnlGwvB5IPYJMpfe3rT1fwGcGbelrBAd116olJxGnnQF13gJlO8SeH6ogq_Dts2t3_ldLBKU174JrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NQss3oGU_dgxxFL1ncOUq0Z4POKLa2OMXAuO7V59w4qz-fg46CenBvDGSW4dyyRVRbFhENptpEbJMrvfvsb3bBbWQlq-Ew1N3lTscBpqIHVum0CaUiPTbQPuX6KAF8tCgZ1-ehk4yxuYX_h52d1_8-nZfIqC0JuyT7USYsJL8z7rbIJ961U4CGaQUNrIOwAQeSy0zzqskMxjDjMHRFTiFAnvgVVMssUhN7CLwW3svEoMvwLbEMLCS0-prvZGrVjWUnSFThxQK3pXp0Ig-q8S29941Uq3Xhjdud3a1Vy0LBgk4qbJrimIHAAaVA7sm7T2sOhabjOaaNnNYKPj2MqUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjs--EmIwHEQ-c5AWQUwJD81ijkCaQ4q9N_FTW8v35CYNC74PPfyteLxzkD53-I7w1G0nctMgHBw_wDysezkWOsTB_NE7k9j1xkm_c-1dKBLs65tUOlWrORPGdHLI1bDtuuUqPXjU15db6kJLfm5p0cJ-Tt51zUI7Z42tvrOK_f9vtsOITkyBCeWsVF58G4wKDF0t-EaUxowko9mjr0VcNgkvi9RVrhu2CFKwFAMs6G5Em7liv0wHnozSls27nYqS-PFk96s1M991RLa-seUsR0_qKVVmnE5gBN6zGWMoZyaekrNvWHxJ3BY51t2OsThD2xyzqxIdecohCawp1XfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bG3Xv0KrHS0Pb7HgOTGvFUB_nfGvQaJ0J6wXL4-sTlPoJVYQ9XnHVsvnlhPvvi6464eFSBuY7g238V4RZIdLqx0NV6-LAtvpF3mzMAsLh-NcmE4hbG8iYDZuJ2B8TkS0cvU1mUk1GCCMb-F5OB5n9J6vuFHmxuq-QdV3OhbAoZ_6mdtddGxGGkqWmLGNBWmOYJtzpRs9hTPmASXgvmgT1QdC3rWAt1YoQ1TORRahrAeP0nuxqGX9waNOT5BnT4qPXWNNXwH_ijTx8P46kKFck78vvW4DF0Qp6mbXNpLxGNLv3XkZGwp-tofMHpzWjLG1kU0DRavGcaIYJjnxR5dNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3O5MdUgtbKKk-kr7gFI6wEbczkAvutaj9ACzin5qErha0gZTVilPvQLrVx0W0VrQwXKmWOlPYqoC5GXFLe0gcw9HHQwCpX3TX6ue3D9rUNRBbJ3TaS9Se-YP2tnOxa57MW9o0YoiKw5w1y7m94fKwG0OwQJf3iVROoXttwGcSbu45tcvdF0r-eSep3Y7oq0xKb4lrmnoEopDMoXEplaIYUUg6RX2nbWX27QUw1q41bkuYSbMnno5pZujP8exEEaoIJaHGpe0vWmf__rnYd8RGKOqwRizZ46l5OMymExDjOLF5Vq81SFvmn4AKA2v0iojCed1rCUpMnyIqD02TRkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKtFzvrDXy2jm7STLLYnWu3ZWylK_DYm0aRp1pVOGr9K5NuAUwYd5PaKoI0NA5WHjzqh76W9CqF1HyYlK-34WemX7NIMqDfmwZy1XKbEJWlZv7mjzrwCzzdnLtbRWQQiIRrXhRfjRJF_WtAK2hzVGwkSdCmtiKNzKnFbcTjvyAXpVBfasxT3opI3HxopDUQzab4dXJDxIDxmsaKiv91fWiCvUuIS3epzVuqq_YPoKRKI8LMSVU9F0Zcx0AHg2Oing_iCVrhgab97VlIjXGb-Uo3VZyOFWO1en8ojzFdIrqSIQDtHDGmDOjZCl6GkCU5yn2I4tvjXc11uSh6hlYXXhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر مدل دامنی رو چه‌طور تو فصل پاییز و زمستون، استایل کنیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/694513" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694512">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1736666e7d.mp4?token=isyYY9U-D4Qcyc4T9uEkklrwkSRerXqTYPNefbUxodWdT4lLPpM_oCeJSYPLOGvtwm6OwGuCQe4Unx8x6jnrNddW1K15sy_rL66-Ea-hfbjaEog0ClAAg5JJq4UvcIjtD-x6zWSgyuC-uTWD_d0BxtL6dhs_b_8xjj6Dp6g7TVa8fi0KyEiWlFhq1O2GJ7tJE0s4aT8XrHgRy9iUZOYTC_AOmm94kbEwsig_Z7gnKjZgrfR8_bEFv1yBvwitXcrAXPb6fQWSuFeAe9zcNUKq39n4K3jpW6kRfqwkutQ24zvS_gczGrsMHtP0nyaMqzuXADNFjO5MblEksxDB_XuBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1736666e7d.mp4?token=isyYY9U-D4Qcyc4T9uEkklrwkSRerXqTYPNefbUxodWdT4lLPpM_oCeJSYPLOGvtwm6OwGuCQe4Unx8x6jnrNddW1K15sy_rL66-Ea-hfbjaEog0ClAAg5JJq4UvcIjtD-x6zWSgyuC-uTWD_d0BxtL6dhs_b_8xjj6Dp6g7TVa8fi0KyEiWlFhq1O2GJ7tJE0s4aT8XrHgRy9iUZOYTC_AOmm94kbEwsig_Z7gnKjZgrfR8_bEFv1yBvwitXcrAXPb6fQWSuFeAe9zcNUKq39n4K3jpW6kRfqwkutQ24zvS_gczGrsMHtP0nyaMqzuXADNFjO5MblEksxDB_XuBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ ترفند کاربردی word که باید بلد باشی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/694512" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694511">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1cce8e6.mp4?token=VvMy461iaSf1fBaseB6XYOIhhwph1vrJraTa0w--SSa4CPfG2JjUszpsdTKOtOWGgWrNLUK_3JR-mgdTnCjSVQeSzU6fibMB1HCkFKd6GiQstVCPmD5WCoosxTE9KuofSe1BkpsfO9j_hWvYSCN_2YwP9g2eIRhsQlp0s77fZ_OgvjF8-_x1AGlmzX2bz7s04rJzcXenrWL25zKcPczAGj80XxR81BpizqIrZ9kXhyyp7saX4cxDiHG6NvcnhTsZYxFMZTmj0e0KFvNUXNPMjGKb1YmDwLahDx_LOJWWT-1H004MMCnb5tSXbO7-mx8wDH5C940O7DstUT7rPR3xQjtMlhINTK_lj5GIZr56wr_I75K3KjbiOoH5yWzKCTA870cFubVlN6n_NmscztgeTzCoiiuuh8RiDxqqIrDGdnd23TYTxJsNlvH8eDUXfWybZJnwrzasvXKowYy93KrQPFeGuDFiaFbY9Pu6yxwo6PDJZgbC86MZshgYD8cbq5do_ZJGg7SvmJ3fjxbW1dwwd_ZqSxagvf8AsUPc8CSVkSElPAP41fq3B3JGphALlNmTt856eW-t-RG33qmPa4l9SqZEx8Yq3oqrzl0fVGZ-e_lWevL0gwvOxEnKpUB_3NhKVpK3folIveOurYMeBhI50MSmdzn8cqAi46_lvxW1I0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1cce8e6.mp4?token=VvMy461iaSf1fBaseB6XYOIhhwph1vrJraTa0w--SSa4CPfG2JjUszpsdTKOtOWGgWrNLUK_3JR-mgdTnCjSVQeSzU6fibMB1HCkFKd6GiQstVCPmD5WCoosxTE9KuofSe1BkpsfO9j_hWvYSCN_2YwP9g2eIRhsQlp0s77fZ_OgvjF8-_x1AGlmzX2bz7s04rJzcXenrWL25zKcPczAGj80XxR81BpizqIrZ9kXhyyp7saX4cxDiHG6NvcnhTsZYxFMZTmj0e0KFvNUXNPMjGKb1YmDwLahDx_LOJWWT-1H004MMCnb5tSXbO7-mx8wDH5C940O7DstUT7rPR3xQjtMlhINTK_lj5GIZr56wr_I75K3KjbiOoH5yWzKCTA870cFubVlN6n_NmscztgeTzCoiiuuh8RiDxqqIrDGdnd23TYTxJsNlvH8eDUXfWybZJnwrzasvXKowYy93KrQPFeGuDFiaFbY9Pu6yxwo6PDJZgbC86MZshgYD8cbq5do_ZJGg7SvmJ3fjxbW1dwwd_ZqSxagvf8AsUPc8CSVkSElPAP41fq3B3JGphALlNmTt856eW-t-RG33qmPa4l9SqZEx8Yq3oqrzl0fVGZ-e_lWevL0gwvOxEnKpUB_3NhKVpK3folIveOurYMeBhI50MSmdzn8cqAi46_lvxW1I0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای مسلح یمن گسترده‌ترین عملیات خود پس از نبرد ساحل غربی را علیه مواضع نیروهای مزدور در تعز آغاز کردند؛ پیشروی رزمندگان انصارالله و آزادسازی چندین منطقه حیاتی و مهم ادامه دارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/694511" target="_blank">📅 13:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWgNsaYAoswkblYJNatxJM4GO6plWFB6L3tvc3dOkYIi95WC9LyXpmg7TjS36RtmgtJOeuBo2LycFhQ_QtHn20OcYkNTyVBjNU8Q25oKc0xNxvmb63xvJjt7mgNinmle0zSPOcVghk-H3PXwHt957RGi8UGu68tFlDB9pCgkGSLZeqbm2FSpPgX55rmptZEq1tQgY6NmNl5BF1yq-njeqlDAQ6lys_6h23a0aqMm1TGC5A2zU4m5rzZ3OzNNDrty-SsJnPMcBkQQ98fsO9XzT0Ypb_L8lm3rFLWv1SgmMSOYRUhnJNE4ns6vj-QVhuuq8PWqDiq32r3iRIgo-QVRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منظور ترامپ از "اتفاقاتی که به زودی در ایران رخ می‌دهند" چیست؟/ نقشه آمریکا برای آشوب جدید؟
🔹
یک خبرگزاری با انتشار بخشی از سخنرانی ترامپ، تأکید کرد که او «تلویحاً از برنامه‌ریزی برای آشوب در ایران» سخن گفته است. بسیاری از کارشناسان معتقدند هدف اصلی ترامپ از فشارهای اقتصادی، «شعله‌ور کردن اغتشاشات تروریستی، مسلح کردن گروه‌های تجزیه‌طلب و در عین حال حملات نظامی» است تا زمینه آشوب در ایران را فراهم کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3249189</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/694509" target="_blank">📅 13:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufDl_aJMlm6jy2orEveI7kiV0hTPOvmpqQlTbJklUn65JNMgTF6Z6uiEh3aLd12gC-7FzSUw0Wm8QfXhyxZbJXuAwVNOxjd_jY-vzgnlYqIj00WSsyp4vUFpuGRbwEYfdGtqSAvzNcBvCexVG7Jnw3VrOnCFaky0RzjlSzF2VzSK11YEfc5pYOk9eh2RXaCyjYiGxWUmHsMD_MWUpj2CWJNiSEsVJf2UI_zFV1ZdInBODLt3s4_CnnQyGYv4Wc_jk2cXdhNJxeIXARaGB4dLWum4Pn9pOTDe3cPIMPrEGxnf44TIJpiZq-6WtJNjPvmv7NwfxL6HpQSttPRVQm6_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این آمپولا به چه دردی میخوره
💉
🔹
مصرف این آمپول‌ها باید با تجویز و نظر پزشک انجام شود و از مصرف خودسرانه آن خودداری کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/694508" target="_blank">📅 13:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694498">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMC90TxT8PMWi0wHb4T_q8tHLUN62XEfCsnxwuLdlcqx_OAcCSF8cEQE0zt02Fqs91QZ_xxNesb9oSvYL_dlHzd-r2xNV9fiBo9Z46D7OoqRCaR2c4Cbu502EmkC0O7fMbnwN_5niha3lYXBWqPik7DYBRvGJ7b6gai4_nJW8uOiJ83cciw10FmeRleYuF95TiguwIRRVpRcXc8HBqbYTOny_NwylL9vyYpNAhbzGXlfIWjA2PXsAtZHatxhxH7H5eD_GllzwUvvvs8plnpyTTUFD2pB_MZDcrF8s0uZx2NZC2cCe_7D3hBI_hTfACsRK5zRp7VGUvLr36fyZgjiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKI85r532NBJ5t1-wB2ZOKUeUQGFBNQlONNLoCv-YnAocfJYdPpkcZgQWY9zzM8y9lguJQWhQReIKbjU7DqtCyVobO2OoWB2L1QhINHSctSrcWTipMa-7DHpOKkye8uFXG2XVH98g4LeaZMlCgrN6OMLTlMhOFt-2v-xwZsL_IerlmSzVUQAclWgCvkNlV2N7KenOv1DtH_zDpOa6DUGTaJ4BCNYgarS7NLBczaUhfcx63gkJG6L4jPcte63oLBnNV4wCDiQv7GjLv32JzDK008bgxgmVAd_Oz-8UDnOmTtf35Dw0NF36bIh4GZj0A4Rl0W8_hqK6ZFkit39_lYecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZ9ZznZx9_jo9MTXq2ARZUdNTSPP8U9bTK5Tvhfi6_7CIBZSKP5JcQG8LrQc-rvTPG-UOy97D3YKjYXEXUw6EUBv1md_rOqlUSXJ_4x5vrZTb7YaUUSxbZjyXecEHLeU7Fakj9WxuSitRD-n289RGuQpuOVD0MdKJXv-BJuZwSZFWvSGbWk_t2TFEh9V3T7_M6PC1UoSbPjoAncA0jEfMS5APbKg8TSExneC20UTPXG8ynCWSgkAEOHF8PSEJyJbT1UnOy-hCb8ApNjzH7Up2855SpyIEWoh_t5fZgrajacKLwJngtVPZ_3TTDWCQ72Tm1lskLeshWLQSWm7aVEs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuOSeB6fX-GNWvQ7RKUfpPZHdpC-jb4sHmJS9ciqi3TCgnvFLDkc_I1TEvS0ciVbEGWYOELl9cHbNp6RHqgoAwwKvDCXeKCrV3SPoMhJOw7WywmBt6H7VfA95usald3EhaOjA5AM-BjVNapJCkcTRqN8XS3gJ-SYtRLygf5urP4T_nKlcAlayszfpxd_btcvJKALgMuzX4E9TuUJXaQX6rgqrSwsqCN7TKGvGZPo7E_3jGsVi8IqqAXsHKLeD_EWaRKJ8s3mPsXn4U8icWcxfaVm4s25qkIbYEr5FzfO4pbB_qajs5JU423gEfXsocc9solxN7F6hSEb1G0bC22RCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEOoGSUl97M3mrt914nbZQE-xddi8Fh9m8OR5SAwkOJ5sqYM8l88BI-ze5QggW3Z90AP-tlaks1Uu27Lfin-7qVTcxGPDikkDSl4tmdACKxC792Ubf9x1lEERVA1wNMJrItRHb7az7tllcdCC_M36bi-Lu2IltgM_ukalNz7eT5WvV6HQO3L5mT_FXcuh82THtOad8fjTBVvkr1tuoUvk3RXsenzLt-sCec65p1FkvsM-n-kNbfHUl9grP5PzPHHBNZMV5iyGFpS2fed2ilUQNPYMkZq28ATGIA97QMCkzJX3nckuThKM95cbTh46s1X2D_PfoDRbVtEVFTfxKZFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LinC_ziuKXZiDukj34pgyObE0KjRqdn1tLgu8DJ5xsVzYwN1PsPes6WIut8oQUvPq5BProMbbSke6Dk87x5H95SfjFOMj6dk0xbPY4su9tuu8RfYbnJmXkXYZVJvxOf3cQlcFNhlF8WDa0UnVP8hHMlPDA86xVzhKZMezllpWsnVFSMdKUiPhm2gOk7oNxbxXs-s5I7k27p_UyBeDg2TV8uhxkVrKdGbOfJdZDGwA5unzRUR92CAvSc425j6s00g8xnR_hq7iRkvRd4n_q347HVysiWU99cVEtmI2VQAjkbRfEC4N2BPtKTbevZm2ccD5G84qDgqYBIcDrO_lJ5_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBZxwpS3P6_MFovkHbvLDZHfn3uKuq7KxWZ7E480plQcfGSUMfSz0JUEMQF8F1gRHZj_VayTKjYBABGR6XutyQhl3jsHL5XtQdLYWrsCOm2Jjn_dmBR_5tYdKcTkjH6DNlDWxQ4OCUr0daeyawKhlbzAYP51YxB_OkpNqaDJimW-krXMpaYgtMw-6cuzKewSZQAwv0D9ZK3VKJEgt5kbLvEERFHoko37znfITgSJuA6189Vm9lexpgZGXMaa8WpUkoTgIiM1ssLwXIbEkkerSOVch5Yx5E40iIon0ZB5V-djWHk9OiXEZgxCIgQk95by6Y57omNaXBfaR1foplUPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxLcohKPIwkK9FeAqnrYuroRbrSmm3b66Pt_N68SCEZj6YZjqgkWIDz9L5ksNdvB9pO0nO4P7f0aTBZokq63YRkfFJnDdr5Xw0TJEkIVj6sHnkS_5yEL0tohYBssGLKjTAJ_OKwQHXmJ5khe8SGCzFF9KVXVqg-HPwQfYrh1AdunzEtRtcNil-LuBHdgTR2CFNzmb9hmPKW-K-WJgOZwI26vsc6qjixAL1zGQRVW9XnhbCIakF2qpTA-IkP1Rh41X3yEb52sCqqucmfSQfhLbl9OtpA1d8AFyYHbn_R0aqoGGyu9h948bgw_N2g_0nI5djazRqQJDyQMTVtSeqsg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWhXqC4MRim_Y5ioMcaxmvOB2ZpaAobH9NbNUcMiuL2BfHvk2EuBR38dHSNUMKPV9qTW4yvlkZ-invgNsDVVPAT0BAO7h8aETcXP-n93QgmT14KXsITNg97YoaepIBj71b0qlIKluQhc3as0OJToAKXIRvVPtsX_CM00MR0I1FyiC32wfEUhYG6-wkvdUD05II8ZtT7hifGXyPfVUWnbZZcjokXdFGBczgK4wsQqO3j3W1bp_82u_ffrFcWdMJptC6QU5kuYSBzt3hC9u_qXwcsXeRdzOkzqjZAORTqqkjB0k8bq_zBb_Oz7arEUQ3lGuQ3owdg591MgchdPHYBLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxPskrltOVHyDoBOPXqZyvuI-PdR6UgLNVFsvlST8m2XalppM6lSNhPySg-lApIxyPV-mAqEmIZBO9Cnk1306LoyDFx6de9c7FbYKRVDQnfn2LYZiUIc6fsVzcp2HO38fuu31Svsjm28_qSPCWlEhb2_IIzvleobkVKDAjJZ1Ahu6LyTXYDhEnh0jKEGIKGrqSLN-ETzBHV45bpOWGmhN29soSOzgHMJpUksVj5GbK2OvOtmq6xoQUFfXj1HUpd6Z1D0gDAhuugEyppM-RgJXiFz5_jUeko_LQ1j3CYOzunbbz5tsgtoNRlxhjUt3iBwRMpyherhzHQM69_J_ZPAoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏋‍♀
استقبال بانک صادرات ایران از قهرمانان وزنه‌برداری
🔹
قهرمانان تیم ملی وزنه‌برداری در بازگشت از مسابقات آسیایی ناگویا ژاپن، مورد استقبال مدیران ارشد بانک صادرات ایران قرار گرفتند.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#وزنه_برداری
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/694498" target="_blank">📅 13:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e9d1b4ee.mp4?token=VEma2BuvSkknT_kLLW-qGSvU-c9LTCzNpPtD62q1ZxtJq0I_hMA-X5dHRS_z5cs1Z9rQyGzzcjUBkp5cPkneopTA-ccGNztoRAWa_hPrnIS3ZnZtotNhG_SCt1FqEnxBNviiqXzf21i0CCptikCPq04nd5_arYxAzJYLqJu8cZR7l0Yu1SVh4IKh12crurVkzN5riojNyA1yBuGNHpdIsbqRowS1IzSZUDWdVAs92C7xOsErI2eNw5kCIEf93PNtn9eXuEPBUS-2V4ur_qcPXo43_wsAxHddjuY6oqFofbD_kcOtnq9zFJmxOjSqrvvwvcAnZO64WWbrtSdcyVCqxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e9d1b4ee.mp4?token=VEma2BuvSkknT_kLLW-qGSvU-c9LTCzNpPtD62q1ZxtJq0I_hMA-X5dHRS_z5cs1Z9rQyGzzcjUBkp5cPkneopTA-ccGNztoRAWa_hPrnIS3ZnZtotNhG_SCt1FqEnxBNviiqXzf21i0CCptikCPq04nd5_arYxAzJYLqJu8cZR7l0Yu1SVh4IKh12crurVkzN5riojNyA1yBuGNHpdIsbqRowS1IzSZUDWdVAs92C7xOsErI2eNw5kCIEf93PNtn9eXuEPBUS-2V4ur_qcPXo43_wsAxHddjuY6oqFofbD_kcOtnq9zFJmxOjSqrvvwvcAnZO64WWbrtSdcyVCqxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقطه صفر شروع رانندگی
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/694496" target="_blank">📅 13:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TibaszGWmX9s1Hb5L1ly54vdSM-N3hFpGMnUEiFlUlyxyhWRvtb0j3vfqdBa28vcK-3YmGhl5i7EEw2pdoq5l4TDq6Vs02bnxEOqByKYHJR0CHg59IB_Ojt4PAYYFKKD_2UR4jJiNRtkFD6w0E8OMBhHndk10eSgGNsDT8cZFcsNgFUxe2aOGM_SiCqLAlAncHmsIsgGXVU4WIjH9jy0l9_SgElFEv8wwYNCtcetMNnonPGpnNZjjWg6dwVvxc7RZ8zTTLiZuWf_tDEewqphGfcdb1SSSsT2I9oZ4X9a3BvQPZ7gxW5n94F3gPFUJFhz6qZeKxRklh6Pfe1qeek_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت تتر از سایت نوبیتکس حذف شد
🔹
تتر حوالی ۲۵۷ هزار تومن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/694495" target="_blank">📅 12:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694493">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c802c030.mp4?token=qlffrOl0NiNblORKXxalmpvWejZOPH6yX-KJAaD7Hilm_LgObcSzVHtaFz-fa2UbBZsSD9YgvIEbD4B695wjr9n3HGPLRJyeScR4OSCVWSZvQk1_gSZEB1tST8VSOZKkU8Rm2HmneGzVEcaEvDU4Ww0wZUlsndd8kP_7tZn4ICjZk8XwZhNw7UL0K3ysH8iRw8VsVsBEPBz1KntzwSRbub8_8bbEYzeH9LN3GXtUvGhoWHK-NHUiGhngXSFMkNlY5dDrcR28RiKJ9TJn29nCa7iKlOxN5bJfMHSzbcyxEQPQPx7n_co7_hxkUKM0T2y7k0PBF7r2FpWbyYtSt63IOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c802c030.mp4?token=qlffrOl0NiNblORKXxalmpvWejZOPH6yX-KJAaD7Hilm_LgObcSzVHtaFz-fa2UbBZsSD9YgvIEbD4B695wjr9n3HGPLRJyeScR4OSCVWSZvQk1_gSZEB1tST8VSOZKkU8Rm2HmneGzVEcaEvDU4Ww0wZUlsndd8kP_7tZn4ICjZk8XwZhNw7UL0K3ysH8iRw8VsVsBEPBz1KntzwSRbub8_8bbEYzeH9LN3GXtUvGhoWHK-NHUiGhngXSFMkNlY5dDrcR28RiKJ9TJn29nCa7iKlOxN5bJfMHSzbcyxEQPQPx7n_co7_hxkUKM0T2y7k0PBF7r2FpWbyYtSt63IOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشنواره تخفیف‌های برج میلاد بمناسبت سالگرد افتتاح برج میلاد و هفته کودک
🎊
۵۰درصد تخفیف بلیط بازدید
🎊
🔸
بازدید کامل ۲۱۵هزار تومان
🔸
بازدید ۳ طبقه ۱۵۰ هزار تومان
🔸
بازدید سکوی دید باز ۹۰ هزار تومان
🗯️
کودکان زیر ۱۲ سال رایگان
🎡
شهربازی ۵۰درصد
🗓️
۹ تا ۱۷ مهر
🕐
۹ الی ۱۱ شب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/694493" target="_blank">📅 12:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694492">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
صحبت های شنیدنی حاج حسین یکتا در خط مقدم و  نقطه صفر نبرد با رژیم صهیونیستی هنگام وضو گرفتن در رود لیتانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/694492" target="_blank">📅 12:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694491">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRql1yr48eX41ZhTfvmvoUMCeSh-WCaN7eNbzmjfzQZnN5-T_VKFt--3DM1esiKK2AtKbezOjL4RQgoEPtkYHX8yjf6wgmMikAZxeRDEDX8rmHCOetLyaMk-AtWj2ZeepsfOqMa_N_0pCqeCLjY5cFmHuZ8Qb569vR7dXHdM_Y5m246zR5PaYvqZjBTj2SQwzndnqSysrNNq0mjF-mPuaY4gel6drGKbCFu2ZvrNrM_XnVF8LCzVglgX36_vBOee6uxDdn-OD6_xsx8oHbG4GpdaXsEPQeyfBeG488Gwytr7gL0cMYJ2Jzy2QMatJW0MZ35_vxgjOccwUgwTK1iVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۹ مهرماه | ساعت ۱۱:۳۰
🔹
دلار در محدوده ۲۵۴ هزار و ۷۰۰ تومان و تتر در ۲۵۵ هزار و ۳۸۲ تومان قرار دارند؛ فاصله اندک این دو نرخ نشان‌دهنده همگرایی بازار ارز است.
🔹
طلای ۱۸ عیار ۲۵ میلیون و ۳۴۶ هزار تومان و ربع سکه ۷۳ میلیون تومان قیمت خورده‌اند؛ همزمان انس طلای جهانی در محدوده ۴۱۶۳ دلار معامله می‌شود./تیتر تجارت
@titretejarat</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/694491" target="_blank">📅 12:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ترامپ امسال هم باید خواب نوبل را ببیند
الجزیره:
🔹
با وجود تمایل ترامپ برای دریافت نوبل صلح، برخی تحلیلگران به‌دلیل جنگ آمریکا و ایران، شانس او را محل تردید می‌دانند.
🔹
پاپ لئو، ICC، ICJ و فرانچسکا آلبانیزه از گزینه‌های مطرح‌شده هستند. برنده ۹ اکتبر اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/694490" target="_blank">📅 12:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694489">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f648393f.mp4?token=e5A2C7H4Gb91RZ61qBvoHIg5m9eyows95UUEwluyTOuAPNTHB5NYydpgYHOQ_SfO3ofTsemferWNVgcrk5LPSX0lE9HXXW1mbLPjx7Rvy3eL7puuLYccEiV-nj1zXPjT7rlQWVOUbA-uizYtja0czLS1WFKKEzankEjV67aKRqTnwY5UrQFhTzGmOJQnZ7dDWXXmfc528TToaNtaCZmdcWFPiESKG0faa6ah161cl-EFr-KOmvjlw9OMP32ZEFy6Owh1yrJcbWhYnxwZUooXq7i14Wl2hdeiZ86OYN_9jsFctF88ZLySUx36sPHLet2o6VRaQu1DkXk0rd2jRpD5Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f648393f.mp4?token=e5A2C7H4Gb91RZ61qBvoHIg5m9eyows95UUEwluyTOuAPNTHB5NYydpgYHOQ_SfO3ofTsemferWNVgcrk5LPSX0lE9HXXW1mbLPjx7Rvy3eL7puuLYccEiV-nj1zXPjT7rlQWVOUbA-uizYtja0czLS1WFKKEzankEjV67aKRqTnwY5UrQFhTzGmOJQnZ7dDWXXmfc528TToaNtaCZmdcWFPiESKG0faa6ah161cl-EFr-KOmvjlw9OMP32ZEFy6Owh1yrJcbWhYnxwZUooXq7i14Wl2hdeiZ86OYN_9jsFctF88ZLySUx36sPHLet2o6VRaQu1DkXk0rd2jRpD5Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید از محل اختفای تروریست‌ها در زاهدان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/694489" target="_blank">📅 12:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694488">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8ADOTKsPGtU34cq2euH3Z1NKYXfccbfkyw8zs1__lyb1OFO18zxT6CtCPA8BN_KQsyC--u3SkDRKqCWaCDwc8Z0HfcU8B1SlFxSrSHXhRg5sm1wZhlCD7W1YWGnu3tAP6MjXeVLxT2moZYJbLy3etzsYJL3JVOQvv_gjdz5LnEpNRfczRlLMJkAOeUIZbZCNvukFw7bFz4XDMsGLsOI-t-bTUjHKGLw7_Ko13YyFLVoWCpKR6Dz4sAJJekVlxo3mDiqoXtRcV3beFvpXGTQUyZhErko_uEMgnU18Oj2ebORaf2TG3WAkvp4ktshyqBaBe8lC-9sptcuv_1hHezFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند سبک برای طراحی پوستر با هوش مصنوعی
🎨
🔥
با اضافه‌کردن نام سبک‌های بصری به پرامپت، می‌توان ظاهر و حال‌وهوای پوستر را تغییر داد؛ از جمله:
• Skeuomorphism: شبیه‌سازی ظاهر اشیای واقعی
• Neumorphism: نرم، برجسته و سایه‌محور
• Glassmorphism: شیشه‌ای و شفاف
• Claymorphism: نرم و سه‌بعدی
• Minimalism: ساده و خلوت
• Maximalism: شلوغ و پرجزئیات
• Brutalism: خام و خشن
• Liquid Glass: شیشه‌ای و سیال
🔹
مثلاً می‌توانید در پرامپت بنویسید:
Create a poster in a Glassmorphism style.
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/694488" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694487">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2dn-JrAtkq4srNroIberQGMgB3NcjvdoKHDQ3PZ_3JbqlDxSzGAJWRh5HUI78yf3DHKm8IyTjvY-gwKqdqwkiW55K3RyaO6MRF6CNor2Mmy2ZnRGV0FDPY3F4fxX42ebOezjXPj6-JVO4On-tTrn5hc5BtMVnf1gV_10eaSxj0c_tH8H2pSk2Q7CmrIAo0-XcN68IavScNPm6OquqwRkQe4A5NTYTduCZayLG08KNfw0xgsatNfN22tO83a6OEEsnvf3WtCQ82038Aim1xe9za1if7-rxJuC_zTnyx2d2Nbcr2wiHiGqnwJIYAXBOvzgnioedOdEkiwkBTR4iE2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع بسته های حمایتی لوازم مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز پنجشنبه ۹ مهر ماه تا اتمام موجودی
امکان دریافت نقدی و اقساطی
هموطنان گرامی می‌توانند با مراجعه به سامانه رسمی ایرانکو اقلام مصرفی حمایتی خود را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694487" target="_blank">📅 12:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694486">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بازی ایران و گینه‌بیسائو لغو شد
🔹
دیدار تدارکاتی ایران و گینه‌بیسائو که قرار بود ۱۴ مهر برگزار شود، به‌دلیل محدودیت‌های منطقه‌ای و تحریم‌ها لغو شد.
🔹
گینه‌بیسائو برای سفر به تهران با پرواز چارتر اعلام آمادگی کرده بود، اما نبود پرواز شرکت‌های هواپیمایی خارجی مانع برگزاری این دیدار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694486" target="_blank">📅 12:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694485">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWw21LjmQHTEdsqbrE-yyzXwbQXLJTUAU8BtdvR2YJoSCsIvALfJSAIlsy7U1lnBm8hoCSLVSRH4IkUvax8_HccMecNnbLzUIUxUZfoSQkHJoFO7LsT_acx9tUckPbIIyn8qX37WbwO9O9lYmYj4jCmGvVi3SUno-CYL0NttmGbbdNFbbo3smqzgrFybSHFjrKF92ZO6Ou7j_KN94J5dH-Ve_EAXemORV5h4poAz1Fa0xlNyxBfafrmGEVa0dOc4DLpjvpBKxRWinWmrasS50ehidh2lwRWVxCzYj0Q5DzBzDIUGc2UYsnhoO3VxT8mfXfjpdALJdzpiUSslg4kkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ صدای شهر
🔹
اگر در محله یا محیط زندگی خود با مشکلات شهری، کاستی‌های خدمات عمومی یا نقص در زیرساخت‌ها مواجه هستید، صدای خود را به گوش مسئولان برسانید.
🔹
با ضبط یک ویدئو، مشکل را برای ما توضیح دهید. لطفاً در ابتدای ویدئو حتماً بگویید:
«این ویدئو را برای خبرفوری تهیه می‌کنم.»
🔸
ویدئوی خود را به همراه نام شهر و یک متن کوتاه در ارتباط با مشکل به آیدی زیر ارسال کنید
👇
#صدای_شهر
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/694485" target="_blank">📅 12:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3350de5f75.mp4?token=hNZk_lgFHA5knUeItI7dC0ZGkXQ0RIAMFA7NkYzmxq5Va8xyIVYuyekCqYG4RTFIdv4YhsYhp8Bk62NzTZdW2BMwtFTxVuTW0p1p9NO_GR0NVcVzLAsEPRIDGkrdvoYhpwHAQ31AvizZ6TBOdeTnZZfzQOYHNHhaXxuMN0jZ8SFChJSu4-zAYTI1fCQaYFIH2ob8xWgjiQf0RcNlU_gFVfMa7Y6STyzA86YRAnJEZNMXuWXIQL8-B8keBRGOGLYrtegpUKwQJTTyu0WggiuswdHKDvAsqz8ogdNgX4MXbR7C4qHNDRv0DI3tjHB5-FLFvIhRNuTFDC3d5B0SKkY15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3350de5f75.mp4?token=hNZk_lgFHA5knUeItI7dC0ZGkXQ0RIAMFA7NkYzmxq5Va8xyIVYuyekCqYG4RTFIdv4YhsYhp8Bk62NzTZdW2BMwtFTxVuTW0p1p9NO_GR0NVcVzLAsEPRIDGkrdvoYhpwHAQ31AvizZ6TBOdeTnZZfzQOYHNHhaXxuMN0jZ8SFChJSu4-zAYTI1fCQaYFIH2ob8xWgjiQf0RcNlU_gFVfMa7Y6STyzA86YRAnJEZNMXuWXIQL8-B8keBRGOGLYrtegpUKwQJTTyu0WggiuswdHKDvAsqz8ogdNgX4MXbR7C4qHNDRv0DI3tjHB5-FLFvIhRNuTFDC3d5B0SKkY15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا به حال شده که فکر کنید چرا مطلبی رو که بارها مطالعه کردین به خاطر نمیارین؟
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/694483" target="_blank">📅 12:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4rAGZRvoTEpZw2-WiEhLswkymZh-TkfBiJtDQF6saJ-a8dbXCi6IwkRXZOLaLl0tOMbduHczEOIVr5uyko10dN41jqz_m1gHu2TItX-K7Ziw87YO46qBZuL-s66M1jcfgRAPuMI5x1bcyi9-qRxpIKCpj9n1BLGQoQ3NU_-yCPrScv4BwS-QyxIpyIpo3xcKMIGtwcPw1PClwbABcEMrjIOUjsVLiHAVVJm1Slz38SCIY7sDcG197gJ6JcecBtEEuXSnMj0iPXBRh_YrR6lvJeqHMoKBC5CRkqt5mzZtBzQ-HdT8xJMkZhl7DjyEFGcGmN-FA5Lj4S2uzeyGZyWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع قهوه که بد نیست هنگام رفتن به کافه بشناسید و بدانید چه چیزی سفارش می‌دهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/694482" target="_blank">📅 12:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694481">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uw3qteULrr9bsqCVzSiDPQxJ7cz7rqI1Wua1ve4hH45psZlqCIZlhMFmPkMNrr0XYqwd9xp5_z9veoyEJ-YdIsKQVrTStHcSFI_M2ehXRrZQYNi8RZ8NrkHAogtg0FngFSxu-wRD85OlnfWwy3Z7xqC5ENdwyx_0RE4Kgr87uUQuBoFa0cQmxzy7hk_DaiU-OxYIsmNkrKLYKkJlk0nsHCnYhrR2UoOERjlVl2n3aeQwOtw82RU37ak6mZEQdXYleD47HAys0W-RuutSiFlh4NQAuwsqmt7WxGGYE_zBW-UGHh30nN_yHoCFxtV2gsjTr5_YaZPV0fNe4XKZgpoXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694481" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694480">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تصویری رویایی از قله زیبای دماوند
🇮🇷
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/694480" target="_blank">📅 11:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2923ddbe3.mp4?token=aHWxtqZI7WHOWPs0-yprwuJs9pfh7RUle7J2rADdhnSTefqeUd9aBkAMph8iEfh-7nrMWuUoz6p3TTrKBuED7h5S0oGDMYQ1dZj7etug_BaL9-Bb2YM6IReRha7eW30b9ixNd93B0tavE3j8AEq-dspAPl7EOqGlPwaBsbV1YufIbY0Lfft4HTu9oUIGzC22iBKOaCRVulUKqA-T_CfG_dOIQomc9rWipLie-nfpyuClfhu8c__A0np_nRLoRZeSH3-ZkvqV8Kf3PndDmQfMD2_cj6MGdIKAf8o59YGxcSQ9VO6zUvpUN3Ur_cG7K4FzxbvG62basLWtsc6jndyboA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2923ddbe3.mp4?token=aHWxtqZI7WHOWPs0-yprwuJs9pfh7RUle7J2rADdhnSTefqeUd9aBkAMph8iEfh-7nrMWuUoz6p3TTrKBuED7h5S0oGDMYQ1dZj7etug_BaL9-Bb2YM6IReRha7eW30b9ixNd93B0tavE3j8AEq-dspAPl7EOqGlPwaBsbV1YufIbY0Lfft4HTu9oUIGzC22iBKOaCRVulUKqA-T_CfG_dOIQomc9rWipLie-nfpyuClfhu8c__A0np_nRLoRZeSH3-ZkvqV8Kf3PndDmQfMD2_cj6MGdIKAf8o59YGxcSQ9VO6zUvpUN3Ur_cG7K4FzxbvG62basLWtsc6jndyboA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان تلخ فوت ۴ عضو یک خانواده بر اثر سهل انگاری در مصرف قارچ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/694479" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694478">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZNHwRqXyAwUdVHXqJ11OGSjGjvi-oo8jTZMyqm5yscBXtMxE8_hrVsyOTKOWSVDDt8_j68YK6ms16cP3eL9SbOhEZRCafMZNomfDdzipqrvECv9bifTH3rJWvUF3RJ6G3w5etYp07YM7wd5IUfbdqOEi_AcLloIo0JbTRNCFrBwH91idO8ZbkriGyMyn-FOKBTi7SRe2B71Rmt6zQlZdDUdTOI99j_zQtex-6gMz4AjIjT4XKjAG91DkFA4rIFVUp9blzKf0THIZdxN11QyOMWposUSufv2FYW_jp19IzsvkeFTEhJ6ZRniaqd1CB6WVwFb5mYZtavUdbj2Xs_ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وام‌ها آب رفتند!
🔹
از ابتدای سال ۱۳۹۷ تاکنون، سطح تسهیلات‌دهی بانک‌ها ۱۳.۳ برابر شده، اما قیمت‌ها ۲۱.۹ برابر افزایش یافته‌اند.
🔹
حالا در حالی که سطح تسهیلات‌دهی ۵۰ درصد رشد کرده و تورم از مرز ۸۸ درصد عبور کرده است.
🔹
این میزان نشان‌دهنده شکاف ۳۸ واحد درصدی میان رشد تسهیلات و تورم است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/694478" target="_blank">📅 11:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694477">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
رویترز: آمریکا از فرانسه و آلمان خواسته است مقادیری از ذخایر اضطراری دیزل خود را آزاد کنند؛ در غیر این صورت، ممکن است با تحریم آمریکا مواجه شوند
🔹
آمریکا از اتحادیه اروپا می‌خواهد طی شش ماه آینده، ۱۲۰ میلیون بشکه دیزل را وارد بازار کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/694477" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694476">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXJZbyoKmomIDPoHshVLLsM_Y-RZcy_9CczRVPGARW0bYV2Z-vNo9btY4GPMB5MSyWm4rhhe8rPwEaAul5W9wZos4cOUvw2JeV0V-6RjxrNkmtNZX9jUsK2MZ85uko-amPFZ9z4L22Iyf9W8hd96RiFtFamZy_oZAo9siEG5bKcoUmRFKH7OCnnueHgU7evBF2RDTljzbPjuZ_92OijFWchKg6wCMm-WOcoFzU19-uB7AXSK5PthiKAGtAWslTlOQiAaU1FAOqgRDgqSFcSDrckdMVv22RrUpOCfkj8J_PHFvKB-Klh_AqQkzEm3Z9H66M6YTz3UBy7QN3ptdXk6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف نمادین بازی کونیااسپور و فلسطین در دقیقه ۸۹:۵۹
🇵🇸
🔹
دیدار دوستانه کونیااسپور و تیم ملی فلسطین در حالی با نتیجه ۲-۲ دنبال می‌شد که در دقیقه ۸۹:۵۹ به‌صورت نمادین متوقف شد.
🔹
در ورزشگاه اعلام شد: «ادامه این مسابقه تا زمانی که فلسطین آزاد شود، به تعویق افتاده است.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/694476" target="_blank">📅 11:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694475">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQNW_JCweWrTSHlPa7mfxp4n9KXd0j75YIdJXdnn2c3s-w_pzepSccm-RczkXf0T64Ql0IXOoFo_m9ZsPO8I-BhlmEcoSWz1Bg8tGDrux2PyzwXtzTODniKG3f6NSsD0-0jkmd7PaKXGMmLeTg7D85mFUH5w_KWPAGJup7p1WuGD3oFcIWeEpsZ9iIaobgLtyCc9YQS0pb9b4xCV1QUC8igJPT4HhqezpqO3IJoJPD3W_OOcNKCz4kWdcjg54UwA_d0b0ZgOAwC3t52ecnh9_MEmT8BUvU02RNHps0fu7TzfwrhK9rKEEyVDt7XSyhRpH9xzlsui2Fe_jxF-OP6Vww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک‌سوم جمعیت جهان زیر سایه آلودگی شدید
🔹
یک‌سوم جمعیت جهان در سال جاری در معرض سطوح به‌شدت بالای آلودگی اوزون قرار گرفته‌اند.
🔹
موج‌های گرما و آتش‌سوزی جنگل‌ها در کنار انتشار گازهای گلخانه‌ای انسانی، از عوامل تشدید آلودگی اوزون است.
@amarfact</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/694475" target="_blank">📅 11:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694474">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نیروهای مسلح یمن گسترده‌ترین عملیات خود پس از نبرد ساحل غربی را علیه مواضع نیروهای مزدور در تعز آغاز کردند؛ پیشروی رزمندگان انصارالله و آزادسازی چندین منطقه حیاتی و مهم ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/694474" target="_blank">📅 11:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
چین قید صادرات بنزین را زد
🔹
چین صادرات فرآورده‌های نفتی به خارج از هنگ‌کنگ و ماکائو را تا اطلاع ثانوی متوقف کرده و پتروچاینا نیز بیشتر محموله‌های بنزین و سوخت جت برنامه‌ریزی‌شده برای اکتبر را لغو کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/694473" target="_blank">📅 11:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a31716373.mp4?token=s9kMpRYYW7FNu2qm4bMaJCX6JIpp3kv-FB4nTFTsM9G-wnED5K1P6fWmq_bi2W6dgaFxYV6zr3IzNLqzp6OqlyQ2ZQHC0fUXd-GqOa12iaPd5mZQW7hZm7tJyM84veRHZXg-MMLy9k4F6HlQQQ0vPddsjbjGLW_UvoswVGo3Vp-XpmyPuNVTqUOzpQ7CG-lJg3-2XBieq_4zqUVyzWTskk5vqcWmnVw_6olne5Xs6R8y7HFx3mmaF7zXpQPUBs1qPfjoz8dPY0z_TMRw3O-eNMZUc465rKkv2ev0jt-OYor6pF0isINBFdsx2us6alZc3OCqtbE38MPYOr8Pg0HRng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a31716373.mp4?token=s9kMpRYYW7FNu2qm4bMaJCX6JIpp3kv-FB4nTFTsM9G-wnED5K1P6fWmq_bi2W6dgaFxYV6zr3IzNLqzp6OqlyQ2ZQHC0fUXd-GqOa12iaPd5mZQW7hZm7tJyM84veRHZXg-MMLy9k4F6HlQQQ0vPddsjbjGLW_UvoswVGo3Vp-XpmyPuNVTqUOzpQ7CG-lJg3-2XBieq_4zqUVyzWTskk5vqcWmnVw_6olne5Xs6R8y7HFx3mmaF7zXpQPUBs1qPfjoz8dPY0z_TMRw3O-eNMZUc465rKkv2ev0jt-OYor6pF0isINBFdsx2us6alZc3OCqtbE38MPYOr8Pg0HRng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدقولی ۱۰ هزار دلاری خواننده لس‌آنجلسی به قهرمان ایران!
🔹
فرامرز آصف برای کسی که رکوردش را بشکند، ۱۰ هزار دلار جایزه تعیین کرد؛ اما سال‌ها بعد وقتی علیرضا حبیبی رکورد او را شکست، اتفاقی عجیب افتاد.
🔹
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/pNG2hI6dFXQ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/694472" target="_blank">📅 11:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694471">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFgRS9-qNWoMC1_WQwMIkQSmXo5XBloMjgx7GQN_td1ZFm_JYTNE8JZiRu2K-5bN2WIXdtOJ2OriiW08ao77ffDAUCxDdIytrN_5HoakupaC1JL5sLseSDfIDy6KLlQES0vszzxkTs3h_2bb5Zfqpm05KpYO8v3LlvIPRK6G6druRiZzrkqSrD38W8lZj2r0688YGyK0FVT-_rVmeBiElRdJF5mfRvGkvKqOh1WOGBob6I95-89KuPiH-UVEqeVrXPKZgalRl9SdIDUrM8yGscx6Hz_m-XqEiTLnbfangagLWktIweHVhYCnfgYl0UvahC5fFEiw2iTCw1t8JvSjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نتانیاهو: فکر می‌کنم هنوز خیلی زود است که بگوییم آیا ایران در این ماجرا [هواپیمای فلای‌دبی] بوده است یا خیر
🔹
ما نشانه‌هایی داشته‌ایم مبنی بر اینکه ایران، به ویژه از طریق نیروهای نیابتی خود، قصد افزایش حملات تروریستی علیه اسرائیل و شهروندان اسرائیلی…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/694471" target="_blank">📅 11:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
کدام کشورها به هواپیماهای ایرانی اجازه پرواز می‌دهند؟
الجزیره:
🔹
چین تحریم‌های هوایی ایران را رد کرده و آنها را «غیرقانونی و یکجانبه» توصیف کرد، در حالی که همچنان پروازهایی به فرودگاه‌های خود دریافت می‌کند.
🔹
پروازها به روسیه و پاکستان نیز ادامه دارد؛ در ترکیه، ماهان ایر پروازهای خود را به حالت تعلیق درآورد، اما ایران ایر همچنان پروازهای خود را به استانبول انجام می‌دهد.
🔹
امارات اما  تمام پروازهای ایران به و از خاک خود را به حالت تعلیق درآورده و کویت از ابتدای جنگ ورود هواپیماهای ایرانی به این کشور را ممنوع کرده است.
🔹
در همین حال، خطوط هوایی عراق روز دوشنبه پروازهای بین نجف و فرودگاه‌های ایران را از سر گرفت./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/694469" target="_blank">📅 10:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGsh_8Eb_YyIGqIS4cjkfZ0skI-3ZUHrg6WNExaC8tMXEQKapiDDKvOrH7b3rf4oGrd7MSqG6_Lk9wwoqzpfjNygn9qQ1ZpK0DgAe--lKkFgV0uyCOiFhxZj6mdun0aV8VAAv8hZeakGcr2JMHB-gkLVN5so6lhz6FP1s1UsIteCw1c__ktCadqE3Z52jGtpWdjVPa0QHAsw6RfR1eiphvbXeSUsNX-be4a9yauK9CKEZ8gDrBYrQwcgORQ_GU943buYNJ4iye1RPx3oryrvOWSWQ30kC_mX0FFHCBP_K7eLd0S6Pq1WeIG1gifzajQK0QTQAECEME0rPhW-rwlYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمود دولت‌آبادی در میان گمانه‌زنی‌های نوبل ادبیات ۲۰۲۶
🔹
نام محمود دولت‌آبادی، نویسنده ایرانی و خالق «کلیدر» و «جای خالی سلوچ»، در فهرست گمانه‌زنی‌های مربوط به برنده نوبل ادبیات ۲۰۲۶ دیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/694468" target="_blank">📅 10:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chf_mKJTHRDAtZCfNTPNcdbA8gkgXOxQOpRGxge84DvW0j-su7eSM2eQRoah8ehiVhrBkhC9ChheRACvUCwhpzLbk6YPtQzFPmSMywvFcpCmLzKjpAzrTCViMDimiFvaTIRHB22LBrxK_ygmJLpahAvarwWLkTzIY5osrJKUVSjU5HxgTo74HNJ1AvpLI43gS_YBLQKQZhs0_ZDCX5x6UmmPRWZviuuXvtCQxSHBPXcg8oWSI91f7LZaeFnh5toWUGhv9jf33jvd6AWM2x-NmUvBew8AouZzMxGufIEsBr7aJhHNWytcpn6Hn1t4QrUd1QaSPttd3ykNmrS9zpSL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جمعه این هفته غرب و شمال‌غرب کشور در انتظار توفان خواهد بود
🔹
سرعت باد به ۵۰ الی ۸۰ کیلومتر برساعت خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/694467" target="_blank">📅 10:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694466">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تکذیب خبر قطعی‌شدن افزایش پایه حقوق کارگران
فاطمه محمدیان، رئیس کانون عالی انجمن‌های صنفی کارگران ایران در
#گفتگو
با خبرفوری:
🔹
خبر منتشرشده درباره قطعی‌شدن افزایش پایه حقوق کارگران صحت ندارد.
🔹
هنوز هیچ تصمیم نهایی یا مصوبه قطعی درباره رقم و نحوه افزایش پایه حقوق اتخاذ نشده و مذاکرات ترمیم مزد همچنان ادامه دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/694466" target="_blank">📅 10:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694465">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frfvK9Cf-XyKy47R4QP9J5AAqbo2TwIGzNaQVNhrHI9NlPp40JMwgHGS8TrZxZnsBKcx2ZLiAmB-hk20xCE-d0mCwSBAzqUJkqfVcPZ9lgncdraZ9u_JzTqsLsuOpV4uDXWQ5odkWqdMIeMc_uDMdoaGTx47ExTLKz4LKcioThGmOowGds0ZUHZrWFm9dAALvSarSj5ejta0Z3j8Nj2us2uh3zEPJGiCI69mSTk5HG48lLNR0-5j52QrUy5hY9N0QvQq0e5lThNh0GaLCUqn-gxH3OSl2CRv0FDwBKbBnOV_TBrgykyPZDRK6wq669gtEX_UyjtmhZHLf51fz93CMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۶۵ دلیل برای نوشیدن چای!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/694465" target="_blank">📅 10:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694463">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b06e6b29d.mp4?token=bWXfho9uBoQtw2Fc2IqmyN69Afm83CNS90R7YC5Hu9qY9barbK4wO9kNAVKhW_-ZRlCzvzJ-6O9w7kTm4G3_Kpz3CGslzWUB2xNwBr_skQOaFNY7XA9tzI4uI-34H2d-2NKIprVCysYFEXmhtdM3mgqysxbfkNlLaDZjJ8O-Mr48t0ieYr2zTaI2Nl003a8GwoiwrPTyfUJhLfhrDzrb4-BjEo1Tb3grziuhAH8md6yxvDntSVQsH0SDhefdEoHV0XY5eWREWwCx8Ip85fja_SOBom1OzCAkdG3KXX7m-MKlZw3DpPyN0aFyBAgYCfoIagkhW7BTqw1LKfV54jFw1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b06e6b29d.mp4?token=bWXfho9uBoQtw2Fc2IqmyN69Afm83CNS90R7YC5Hu9qY9barbK4wO9kNAVKhW_-ZRlCzvzJ-6O9w7kTm4G3_Kpz3CGslzWUB2xNwBr_skQOaFNY7XA9tzI4uI-34H2d-2NKIprVCysYFEXmhtdM3mgqysxbfkNlLaDZjJ8O-Mr48t0ieYr2zTaI2Nl003a8GwoiwrPTyfUJhLfhrDzrb4-BjEo1Tb3grziuhAH8md6yxvDntSVQsH0SDhefdEoHV0XY5eWREWwCx8Ip85fja_SOBom1OzCAkdG3KXX7m-MKlZw3DpPyN0aFyBAgYCfoIagkhW7BTqw1LKfV54jFw1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرارگاه قدس نیروی زمینی سپاه: ۶ نفر از اعضای گروهک تروریستی تکفیری به هلاکت رسیدند و تعدادی هم بسته‌های انفجاری از آنها کشف شد  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/694463" target="_blank">📅 10:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694462">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaxNmMMeFmCuiV3m5zRxiO-z5LNzeNott9DUf6NtViBniC3fHamCR-Q7odum91WSdfWAjRhEvnruu9k_BmW4BspFwtTLZ46CEC-yfPvKl6x00aa2DuLnHQuSS9bc4MuFJPis8aKSpNQReq04SFIGdFeI9bX-tEf_SYwezI7l00KSxToSsQHGwfi3Ep9R4R7Bv5bXrEbJIwmYO4E-RS9xaquHCQ423s1ZP6AvgY7FH6BQaSzdaB8Pi-ggIdnABvDNB8sd01IqnbEs77CkzO0oTno-2yJ6go9IfVhxOfghtVPDfSE8q0WIHVoeb2zrrZ83q1Ryu0E7nfHP02-ywKcQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسمان امارات در اختیار چند هواپیمای نظامی ارتش آمریکا!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/694462" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694460">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
عملیات نیروهای امنیتی علیه عناصر یک گروه تروریستی در زاهدان
🔹
نیروهای امنیتی پس از شناسایی محل اختفای این تیم تروریستی در منطقه منزلاب زاهدان، عملیات پاکسازی منطقه و محل استقرار آنها را آغاز کرده‌اند.
🔹
این عملیات با هدف پاکسازی کامل محل و مقابله با عناصر…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/694460" target="_blank">📅 10:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694459">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
مادر همسر رهبر انقلاب اسلامی: زمان تدفین رهبر شهید، آیت الله سید مجتبی خامنه ای رهبر انقلاب اسلامی در حرم مطهر رضوی حضور داشتند و اکنون رهبر انقلاب در صحت و سلامت هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/694459" target="_blank">📅 10:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694458">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc9966af.mp4?token=RoKmnZiW98LTEPu6QdiEvhatHSlenpOjrEoGiup7vF8WVAcGSCRkCJeHs7xB3PATV3bow6eVVRmCwZQ1AGhBIuDeqJhDbzSGEgjqfwwdZQKSrh1mOAHVgEaTNcfSKlK0eur_BtknXcEjdX5_Lev77ZBarQkpjEzZMHwh3K5j2Yf_MYdX45koMRkx5DHUOId26Uq4uAV9feM2n2LucJzs2qC7KBY68BwDQV4nJ3f2WkXf-1LStEFjBLhBGoSoyznqD698rXnkUd7HEgWGvXEAn5aJfDaoTa1KABqUsaN6aTrNP4l0MBjV1gH2qdL3lrhFuB0_BtY7QqthS7jMPQAVa4CTyvbHzy_1cde6wQ1SqApQ7_M2pjFfByUr19sE0dCE-cEMzN8CgXgDGbF5WPjFCQLyeaxkrvN5mY9p-CDMhv2qiXpEKOtytRS_4LmfhhvVRDelkaZsdVCLjD-ragq-xBvd2UL2Wwbp7MNH6rZzQBd7oGacEpZoD4XC8eq_aBhta2MLNCPVeu0STwbn-RuMkJJDObLATqI2qd7Asr_LN82jXCDDuOCXWmHZuppjkvk5VwJANdZgM_S37jRGMf2H4qpB8ilq5C2m9wLt1mX0ZOPXtu_idPCoyzkFI3_SYPx_4G8oYlsn1brvVZCuy1_bbwxzrXkKEqLMbAyLQeGvLjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc9966af.mp4?token=RoKmnZiW98LTEPu6QdiEvhatHSlenpOjrEoGiup7vF8WVAcGSCRkCJeHs7xB3PATV3bow6eVVRmCwZQ1AGhBIuDeqJhDbzSGEgjqfwwdZQKSrh1mOAHVgEaTNcfSKlK0eur_BtknXcEjdX5_Lev77ZBarQkpjEzZMHwh3K5j2Yf_MYdX45koMRkx5DHUOId26Uq4uAV9feM2n2LucJzs2qC7KBY68BwDQV4nJ3f2WkXf-1LStEFjBLhBGoSoyznqD698rXnkUd7HEgWGvXEAn5aJfDaoTa1KABqUsaN6aTrNP4l0MBjV1gH2qdL3lrhFuB0_BtY7QqthS7jMPQAVa4CTyvbHzy_1cde6wQ1SqApQ7_M2pjFfByUr19sE0dCE-cEMzN8CgXgDGbF5WPjFCQLyeaxkrvN5mY9p-CDMhv2qiXpEKOtytRS_4LmfhhvVRDelkaZsdVCLjD-ragq-xBvd2UL2Wwbp7MNH6rZzQBd7oGacEpZoD4XC8eq_aBhta2MLNCPVeu0STwbn-RuMkJJDObLATqI2qd7Asr_LN82jXCDDuOCXWmHZuppjkvk5VwJANdZgM_S37jRGMf2H4qpB8ilq5C2m9wLt1mX0ZOPXtu_idPCoyzkFI3_SYPx_4G8oYlsn1brvVZCuy1_bbwxzrXkKEqLMbAyLQeGvLjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخت این کیک لقمه‌های خوش بافت و‌ خوشمزه کلا ۱۰‌‌ دقیقه زمان می‌بره  مواد لازم:
🔹
تخم‌مرغ: ۳ عدد
🔹
شکر: یک پیمانه
🔹
وانیل: نصف ق چ
🔹
روغن: نصف پیمانه
🔹
آرد: ۲ پیمانه
🔹
بکینگ پودر: ۱ ق چ
🔹
شیر: نصف پیمانه #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/694458" target="_blank">📅 10:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694457">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750e7f7160.mp4?token=oEG9Yoni34Ry5yWKiWGjP3WUHnOHLFr1ErgSbfN4qZyaW4vqORT4QkibTxd9ZqZnz1iamIkpRUchpt-yZIw9ab85pWa6aZK5GKRiqCcToMrrUb8u9A3nnKlrlryslP-FO6ESQe8VtRdOYWw9fLFAqlaFsjPur90bUq7gnu9pwb4IVC7zMIuDAcCtELbQ51nOHDknAyLKdX9MYkvzAdZNySsFWTtr8H2S_FJdlUcntkiJd_Lku1VYRL2oe08Vshki4-AvaVX3p4XcZA5Vtjpmsbfs45Y7fSQqWk6Oc5SG6hCPapLIj3_skKBkoZSEWfkFf0UEGXkFmtxDbtE6P3Hr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750e7f7160.mp4?token=oEG9Yoni34Ry5yWKiWGjP3WUHnOHLFr1ErgSbfN4qZyaW4vqORT4QkibTxd9ZqZnz1iamIkpRUchpt-yZIw9ab85pWa6aZK5GKRiqCcToMrrUb8u9A3nnKlrlryslP-FO6ESQe8VtRdOYWw9fLFAqlaFsjPur90bUq7gnu9pwb4IVC7zMIuDAcCtELbQ51nOHDknAyLKdX9MYkvzAdZNySsFWTtr8H2S_FJdlUcntkiJd_Lku1VYRL2oe08Vshki4-AvaVX3p4XcZA5Vtjpmsbfs45Y7fSQqWk6Oc5SG6hCPapLIj3_skKBkoZSEWfkFf0UEGXkFmtxDbtE6P3Hr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تپش قلب خارج از بدن برای انجام پیوند
🫀
🔹
یک سیستم پرفیوژن، قلب را گرم نگه می‌دارد و با رساندن خون اکسیژن‌دار، آن را تا زمان انجام پیوند در شرایط مناسب حفظ می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/694457" target="_blank">📅 09:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694456">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
عملیات نیروهای امنیتی علیه عناصر یک گروه تروریستی در زاهدان
🔹
نیروهای امنیتی پس از شناسایی محل اختفای این تیم تروریستی در منطقه منزلاب زاهدان، عملیات پاکسازی منطقه و محل استقرار آنها را آغاز کرده‌اند.
🔹
این عملیات با هدف پاکسازی کامل محل و مقابله با عناصر تروریستی ادامه دارد و جزئیات بیشتر درباره روند عملیات پس از دریافت اطلاعات و تایید مراجع مسئول اطلاع‌رسانی خواهد شد./‌ تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/694456" target="_blank">📅 09:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694455">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/694455" target="_blank">📅 09:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694454">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2165832117.mp4?token=mg0SyIGDaK_7T9NNtnZx9N7jyl5AOXgLPY_NuiyyAM6tctLnD_eX2nZ6RgBQzYLxlgEluapQlWltXOE1ao6x2Sy1wQdc-fdsV8GeZ0VyYVA5YxfEARRak92GLiTre1D0nqhI9fZI15roswCPKVkdlFiJ21sS1nqH9IAVC0zZdUF6zTjMqhqTkfOKagCRc_fBltjswcMS6IzjX-1oy0Yt8mGufFLgh5R-ahBjsB1O4Gg2Y6NDfKF2zudp_l3MheQUvtpj7HyH5Yi2bBIomvGxzf6yCTWj5W70vvviC7TieVgOOJLuc-mJN_TNtQQe9RJwwHz0NOyOwm2Tsi3RzetAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2165832117.mp4?token=mg0SyIGDaK_7T9NNtnZx9N7jyl5AOXgLPY_NuiyyAM6tctLnD_eX2nZ6RgBQzYLxlgEluapQlWltXOE1ao6x2Sy1wQdc-fdsV8GeZ0VyYVA5YxfEARRak92GLiTre1D0nqhI9fZI15roswCPKVkdlFiJ21sS1nqH9IAVC0zZdUF6zTjMqhqTkfOKagCRc_fBltjswcMS6IzjX-1oy0Yt8mGufFLgh5R-ahBjsB1O4Gg2Y6NDfKF2zudp_l3MheQUvtpj7HyH5Yi2bBIomvGxzf6yCTWj5W70vvviC7TieVgOOJLuc-mJN_TNtQQe9RJwwHz0NOyOwm2Tsi3RzetAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلای‌دبی پروازها به اراضی اشغالی را تعلیق کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/694454" target="_blank">📅 09:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694453">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه یازدهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694453" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه یازدهم؛ لذت وصال حق
🔹
دنیا یک صحنه نمایش است و انسان باید در سخت‌ترین شرایط، آنچنان نقش خود را به راستی و درستی بازی کند که مورد تمجید و تحسین فرشتگان الهی قرار گیرد.
🔹
صحنه نبرد همانطور که می‌تواند یک صحنه هولناک باشد، می‌تواند صحنه هیبت پروردگار باشد و باعث افزایش باور و ایمان انسان شود.
🔹
پشت دروازه‌های دعا، امکانات الهی بسیار زیادی وجود دارد که منتظر طلب و اشتیاق انسان‌هاست تا انرژی‌های الهی بر سرزمین‌ها جاری شود و یقین قلبی انسان‌ها افزایش یابد.
🔹
نام «اَلْمُحیی»پروردگار انسان دل‌مرده را زنده می‌کند و به انسان ناامید نیروی حیات می‌بخشد.
🔹
نام «اَلْمُمیتْ» پروردگار، نتیجه اعمال و افکار انسان را مشخص کرده و عادات و وابستگی‌های او را می‌ستاند.
🔹
انسان باید در نام‌های المحیی و الممیت خداوند، تجربه تولد و مرگ را به لذت وصال حضرت حق تبدیل کند و طعم خوش آزادگی را بچشد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/694453" target="_blank">📅 09:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694452">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر TV</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyto74IMdLycAmepyIb_Smrb-R9JuaauA5zdQ5FCHkfahP4a5H29HGaaDN9dYC5_dU4Ul3RDpoQADqyn734ygy6H9InqFU1WOI0ka6kvamxDJJiix2Q_QgbvBBylpijM-mXjulvW-u9P9rKNWf1kD-K7FXVztlKXLLJRpRUKX2NBcDv2NC0ZFDnMo9r5JDNN_rIxPOS9d0EWOK4G_DLSIs1kxt-eCb2UVI76vrCcY2_yatGcAtREB8ilqkUDnkIP2XvJ4eup9Q_y7I6ybO8tC8WysFedqcWTGQc9dw3eWr6BDaF9NrlNRcXOXvJPXI5RP11wzAzaBiVeyvOIwtPiaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#اینفو_تیتر
|تورم نقطه به نقطه مواد غذایی در شهریور ماه
۱۴۰۵
@Tv_titr</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/694452" target="_blank">📅 09:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694450">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27132a7cae.mp4?token=VY8DyhVhuGdyz9-dJKQSktl8y_xsBwFp_OvkESbTVVixrmlx34_8Edx5sA-8CwhDNC5iwxzJKCwEN_ykJM3ZfgLu8DQN4CxkWcDCfAN6jSl-nrmh4D8c_26_CKC8_6YupiEr4AweXGq777SYLjuoGjspcOeagFG7YOxVLqcRDJNQMb9hY_3uY9UA-5QsXDJvNnfej9ir3pfJj-Drk6WbfEJM4ougESi832vdtThxl0yBhW6Y9R602z0Sze0OaSB34eEQPooAf-ldGV3eM5Z32ikVyGtAlPSZvW5rCOl9bXJ2MO-YqdiOqoLnTr66VKT5e1Q3JcWimkSGAyoMblnnrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27132a7cae.mp4?token=VY8DyhVhuGdyz9-dJKQSktl8y_xsBwFp_OvkESbTVVixrmlx34_8Edx5sA-8CwhDNC5iwxzJKCwEN_ykJM3ZfgLu8DQN4CxkWcDCfAN6jSl-nrmh4D8c_26_CKC8_6YupiEr4AweXGq777SYLjuoGjspcOeagFG7YOxVLqcRDJNQMb9hY_3uY9UA-5QsXDJvNnfej9ir3pfJj-Drk6WbfEJM4ougESi832vdtThxl0yBhW6Y9R602z0Sze0OaSB34eEQPooAf-ldGV3eM5Z32ikVyGtAlPSZvW5rCOl9bXJ2MO-YqdiOqoLnTr66VKT5e1Q3JcWimkSGAyoMblnnrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: امروز دستور دادم عقیدتی سیاسی در ارتش آمریکا تشکیل شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/694450" target="_blank">📅 09:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694449">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
آخرین مکالمه ناو دنا پیش از حمله آمریکا به‌دست آمد
🔹
مکالمات لحظات آخر ناو دنا به دست آمده است؛ در این مکالمات، ناو اعلام می‌کند «ناو نظامی نیستیم، اصلاً مسلح نیستیم و برای امر آموزشی آمده‌ایم» و طرف سریلانکایی نیز این موضوع را تأیید می‌کند.
🔹
بر اساس قوانین حقوق بین‌الملل، حتی در صورت هدف قرار گرفتن ناو، باید به نیروهای حاضر کمک می‌شد؛ اما نه‌تنها کمکی صورت نگرفته، بلکه حمله دوم نیز انجام شده و اجازه کمک‌رسانی داده نشده است.
🔹
رئیس‌جمهور تروریست آمریکا دربارۀ جنایت حمله به این ناو آموزشی گفته بود ما برای «تفریح» آن‌را هدف قرار دادیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/694449" target="_blank">📅 09:09 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
