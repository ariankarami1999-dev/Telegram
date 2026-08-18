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
<img src="https://cdn4.telesco.pe/file/bQDxknggJqln7zRwrkQSKk1uGBfiA2rIKrTZWOe1eFWTBigNziZnRqw7ZO_T61ePnJrW4UlSFqK92vRpWVymlxMD6dwDVfqy7f7HacuXy7WWMmyV9oLSPPh2qwig5tBhs8q5iiqlKU519Nk_XeFyfqh1Ob3nSfuxm6wnlhEIofvIRrGSfA17Bvmx75KRCqRWsjJ-NH8pxGyt3Asid-ZoPTkjUiaydi5TqbGE43X-IW6-RYU9L5EuSDRQP8C0ueAgUoiujOkFsbgOuDoOAPjS1inJLGxV38lrP-5Bn3EkufFRn8m5Otub_txSFWjPTICr7ugaObfqVY1yQWfyhfxlbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 23:43:10</div>
<hr>

<div class="tg-post" id="msg-20001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e373b297.mp4?token=SZ2PDftWp2HxRM4r-70eVGkWVaKuX_u_ivL2B7B6kEyGJDbV6OJN2aCncoyg5B-GxQuzeM4EOwgJpdv1umseOPV4CSR7UecI-3fPkW-OLcPeio6UKHym38DBiFanVWnq7HlJUhGKS3pBp8e33PRqS9HDlaY_xJ_mlru4wqOaz1yFnnHLrJclfbPV3ovvuVawRlmgtaCClkijDlcDdfntYzf9uE_j8mA2OemFCtbSMTsLvTHDVg-WJQV0biaCK8mAcME_5G29uZt7eeOQE2EfqSVcuBA9LB_vJTI8JDeatan7kyk3Cpy_00EzM9xsLPhDzQiPUA1XSVFAsa7z5u2qcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e373b297.mp4?token=SZ2PDftWp2HxRM4r-70eVGkWVaKuX_u_ivL2B7B6kEyGJDbV6OJN2aCncoyg5B-GxQuzeM4EOwgJpdv1umseOPV4CSR7UecI-3fPkW-OLcPeio6UKHym38DBiFanVWnq7HlJUhGKS3pBp8e33PRqS9HDlaY_xJ_mlru4wqOaz1yFnnHLrJclfbPV3ovvuVawRlmgtaCClkijDlcDdfntYzf9uE_j8mA2OemFCtbSMTsLvTHDVg-WJQV0biaCK8mAcME_5G29uZt7eeOQE2EfqSVcuBA9LB_vJTI8JDeatan7kyk3Cpy_00EzM9xsLPhDzQiPUA1XSVFAsa7z5u2qcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پروفسور خوش چشم:
باید برویم آب های فلوریدا را مین گذاری کنیم ...</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/20001" target="_blank">📅 22:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تاکر کارلسون می گوید که اعتقاد ندارد که انسان‌ها بمب اتمی را ساخته‌اند.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/20000" target="_blank">📅 21:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تاکر کارلسون می گوید که اعتقاد ندارد که انسان‌ها بمب اتمی را ساخته‌اند.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/19999" target="_blank">📅 21:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujspRTDpdLJ7GAxBkGXuaXlWWUXFAJTqFAA_hsQapAfJr1X0Hdb8h_f-eFTk4FblleJyVoAdrV-OuIB4cgiC92fyjNS7m-YIXRpTBWSnLhcQDIq_7zoQrGNYpj4WOZLH-wFSl0Vhgu4GiKBV25cwtKOUiTYAJrrqcNgkHlY8A-kxLx-OQ13gr2aVy-Pl4MXkw4-afB-JtqBnPoU_vrDobVzbVszvJjKldBr8VHExS7zdkDv_BetYMB3V4yhJSmfaS9naPgehYgZoDrXikx_qc-k6MPDSKCfWhcoii7LBgrMIjdQGJQbRRxjIWAawY8rPIthsOd59Jth584JPh9bZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر کوتاه بود و دردناک!
تادالافیل ۷۰۶ درصد افزایش نرخ گرفت
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/19998" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یکی رهگیری شده و دیگری در آب افتاده!</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/19997" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزارت دفاع امارات در پلتفرم ایکس اعلام کرد  : وزارت دفاع امارات دو موشک بالستیک پرتاب‌شده از ایران را شناسایی کرده است.</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/19996" target="_blank">📅 20:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت دفاع امارات در پلتفرم ایکس اعلام کرد
: وزارت دفاع امارات دو موشک بالستیک پرتاب‌شده از ایران را شناسایی کرده است.</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/19995" target="_blank">📅 20:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً بالایی قرار دارد و افت قیمت طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/19994" target="_blank">📅 18:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گویا حمله به امارات کار انصارالله (حوثی ها) است.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/19993" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/19992" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات در بندر جبل علی امارات</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/19991" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53cb17e6f7.mp4?token=JLJm8YnC_pL8ieq8Vgj4Uccft_ZdlKMMJZRvsKRzrYpetBq6VmjpRhlre9gnaWg9ztIkt0joo9-zv635Z6FqO6yL1RjN6eIM1DSvMEv-t7d5lEkgofOnQ36DCzoVeQS1Q3EoRcYwYEFkVv9sWL-W68hMq0zGlWq4u9p-NugLeH5EUG3UImIn8Nxs8hwb61zwX7wyIEi_sQcapOtcX-CYfOlFtuFQJwRxKfOi24_zNRF-h6i1bm3IDaCLMfyRVpfDRV9BBkWSpWmCeKADBAEz76LPvm6bBqNCqGSY84QfFt0UxeUKXHJQiFPUcbSJBOWVVoRjZmAsC8Lm8QIIl1Q1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53cb17e6f7.mp4?token=JLJm8YnC_pL8ieq8Vgj4Uccft_ZdlKMMJZRvsKRzrYpetBq6VmjpRhlre9gnaWg9ztIkt0joo9-zv635Z6FqO6yL1RjN6eIM1DSvMEv-t7d5lEkgofOnQ36DCzoVeQS1Q3EoRcYwYEFkVv9sWL-W68hMq0zGlWq4u9p-NugLeH5EUG3UImIn8Nxs8hwb61zwX7wyIEi_sQcapOtcX-CYfOlFtuFQJwRxKfOi24_zNRF-h6i1bm3IDaCLMfyRVpfDRV9BBkWSpWmCeKADBAEz76LPvm6bBqNCqGSY84QfFt0UxeUKXHJQiFPUcbSJBOWVVoRjZmAsC8Lm8QIIl1Q1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:   هیچ مذاکره ای با جمهوری اسلامی ایران در جریان نیست و برنامه ریزی نشده.   محاصره دریایی با تمام شدت و اثر باقی هست.   تنگه هرمز باز و در حال عمل است. تمام مین های دریایی هم حذف و یا خنثی شده اند.   از توجه شما به این موضوع سپاسگزارم، دانلد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19990" target="_blank">📅 18:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">طنز تاریخ در این است که پیمان دفاع مشترکی که عربها با ترک‌ها بسته اند دقیقا ۱۱۰ سال پس از جنگی روی داده که میان خودشان در قالب شورش «شریف حسین» ضد عثمانی ها درگرفت و اتفاقا نخستین شهری که عربها آزاد کردند همین «مکه» بود که نامش اکنون شده لقب پیمان دفاعی اخیر!…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/19989" target="_blank">📅 18:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/19988" target="_blank">📅 18:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">— عربستان حملات اسرائیل به فرودگاه ابوظهور در ادلب سوریه را محکوم کرد.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/19987" target="_blank">📅 18:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اسرائیل فرودگاه ابوالظهور در ادلب را با ۴ حمله بمباران کرد.   طبق گزارش‌ها، نیروهای ترکیه در این فرودگاه مستقر هستند.</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/19986" target="_blank">📅 18:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ:
هیچ مذاکره ای با جمهوری اسلامی ایران در جریان نیست و برنامه ریزی نشده.
محاصره دریایی با تمام شدت و اثر باقی هست.
تنگه هرمز باز و در حال عمل است. تمام مین های دریایی هم حذف و یا خنثی شده اند.
از توجه شما به این موضوع سپاسگزارم، دانلد جی. ترامپ</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/19985" target="_blank">📅 18:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دولت تایوان به هر شهروند این کشور مبلغ ۳۱۴ دلار به عنوان «سود تقسیمی هوش مصنوعی» پرداخت می کند که ناشی از جهش اقتصادی این کشور به دلیل رشد تقاضا برای محصولات مرتبط با صنعت هوش مصنوعی است.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19984" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کشتی یونانی در هرمز هدف قرار گرفت
کشتی فله‌بر «Minoan Dignity» متعلق به یونان، هنگام عبور از تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و موتورخانه آن آسیب دید.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19983" target="_blank">📅 13:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مادرقحبه ها این چه وضع اینترنت است؟!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19982" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">با پایان مدت تعیین شده برای نهایی سازی توافقنامه اسلام آباد، اسراییل حملات سنگین خود به جنوب لبنان را از سر گرفت</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19981" target="_blank">📅 13:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اسرائیل فرودگاه ابوالظهور در ادلب را با ۴ حمله بمباران کرد.
طبق گزارش‌ها، نیروهای ترکیه در این فرودگاه مستقر هستند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19980" target="_blank">📅 07:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اگر تن ندارید لااقل آماده باشید!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19979" target="_blank">📅 00:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خب رفتیم برای موج C از ۲ و چند صباحی دیگر فرصتی برای خرید تن و دلار و نفت</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19978" target="_blank">📅 00:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o59cz5B0UMJuPxO9jHH2zNKbVImdpcMG6KcYeOP48hVKLXLpDcOg_TU1n8MTedZLB7Vw5-sKMVJHjER17Qub8-7K35icmGj3WRFUPZ886t6Bom7fayvunaB-IkW1Z0hOITtv0riICVf8R9tvfhNkoYzE_V3f0CNQJIB6Cd3SQB54Z4X2oWDr3B83k6ywM-2OeBYhbKAJn1IaX3h9ED1MjluJIIIdkkJIoFaBPV5bjGzeTy3ZRHmWauwf4E3zPTfHZWdEdw7HDf0E_PuacomCUu36FbZgKlTPRVrBZDU9sFABGZpE9gP81tOBZoq4z_dmCwDNKGtzphW0GUajfh1D8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19977" target="_blank">📅 00:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">محسن رضایی :
تا حالا زیادی صبر کرده ایم ، لازم شود از NPT خارج میشویم و خودتان میدانید این یعنی چه!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19976" target="_blank">📅 00:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx0NoAO-2X3eJsnFn59eEcoOn6Ep-vhqrwbZ7FfJA_sH3eHCf-QhVm_vwmUfIJWvJ007Tivg1V9QOtc5B46jVx24j8oLI1E2Lp9QAR6_1n0C0kNFU5TWVJwwrlx7cxnBv1X1I9Aca0VUQG9XinReeSwx09zxmTfkpG4G1yYpGUB91PX2-Put42nQqSTnItsxaBeN6cPgr4uXi4MaKd31dnyEYKFInfUjdY5lwdi1NkuQT0aRATBFJoaY9x-yOgQzaImH5y2rSZXZQKw22Bx9HRcSXwzNBd_newrVV8IVnyit2NByE3BNmj2fwQ7c8rDjvz-EBrc5BdUdjhl8yBXekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19975" target="_blank">📅 00:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جرد کوشنر درباره ایران:
در حال حاضر،  ترامپ بر فشار اقتصادی متمرکز شده است.
اگر ایران مایل به پایان دادن به توافقی است که آنها با ما در مورد آن صحبت می کردند تا از توانایی خود در ساخت سلاح هسته ای چشم پوشی کند، واضح است که او مایل است توافقی را انجام دهد که می تواند برای مردم ایران عالی باشد، اما در حال حاضر آنها هیچ علاقه ای به انجام کاری که برای ما منطقی است نشان نمی دهند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19974" target="_blank">📅 23:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxcp5n9_nTh_a_A3668nrYJTtCX5iwKGC37HXMzZ7CndBKhFWN-txgDqoC0tSigYS1lMmMNQRCIGCG_SDvKga7YMCLv6qnzZENhpZKD8-jiIkwH_TQxycGVSmyQYmmV-9Id6N1jAEfP8_d0xL9XY_IIXbxn-wLu83o_z_d-Hw_RVTqkaGfzD45YDd_TXLRjgFz88xAua4au7q2iIvdZqOFpDPiQtJeBbt2cWo9lrpmqwSnUAGEi2rWu9vXwFYw3HPqjP_6o_loE6v_XdH4Snfc4SQdT3qWyA1PnngNt6bVMhqgM1bByHnhxqGmkoByEFOyZfrflHuDPoGI4epFjJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19973" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:   توافق با ایران را لغو خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19972" target="_blank">📅 22:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ در مورد ایران:
آن‌ها می‌خواهند توافقی انجام دهند، اما قصد ندارند آن نوع از توافقی را انجام دهند که من احساس می‌کنم ضروری است.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19971" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19970" target="_blank">📅 21:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:
توافق با ایران را لغو خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19969" target="_blank">📅 21:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گویا سپاه رفته کشتی اماراتی را از دهن آمریکایی ها کشیده بیرون و آورده قشم!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19968" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ می‌گوید ایالات متحده تنها از «بادام زمینی» (استعاره از بخش کوچکی) از انبار سلاح‌های خود استفاده کرده است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19967" target="_blank">📅 20:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQv0iJu6AKkHEUUIP1Ru5MGZ9WvePO_VXeIkBKjEbGbVSLP_Js_vcOi0yRFFZHbvCRjVFtMXp-0JeOQhMe1ra1sA6YYWkvJJMye9sIyyW_5dG8LDO5R8Cn9jlVUw9_QmJ1NCaOpoVwRl1nUHpflh6kuEhlE6pfhDaycfN70M3yCEIWz_vR_Ug-jJzlUZ1EOOB4C5QiMTU9KLTNGnFB9kz0il18lMb9myWng6jhyQMuFAE1jZ4yovkxO_yrbQuT9qa8RpUlQRpPUtZlHL__vNH0N6-GhsW-yK5Ak90PNQ92onAfov2-AYLonj7H7lYAd7BLplhTkF0qurpYZjB1nRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم:  داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.  نفتکش امارات در نزدیکی قشم متوقف شده است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19966" target="_blank">📅 20:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تسنیم:
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
نفتکش امارات در نزدیکی قشم متوقف شده است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19965" target="_blank">📅 20:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک مقام ارشد ایرانی به خبرگزاری رویترز گفت که تهران از یک سیاست دفاعی به یک سیاست «کاملاً تهاجمی» روی می‌آورد و به ایالات متحده «چند هفته» فرصت می‌دهد تا توافق صلح را اجرا کند.
«تمام نهادهای ایرانی آماده‌اند تا در صورت شکست دیپلماسی، تنش‌ها را در تنگه هرمز و در سراسر منطقه افزایش دهند. ایران به طور نامحدود منتظر نخواهد ماند تا ایالات متحده به محاصره دریایی ادامه دهد.»</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19964" target="_blank">📅 18:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یحیی سریع طی بیانیه‌ای اعلام کرد که انصارالله یک کشتی نظامی متعلق به سعودی را در دریای سرخ، در حوالی سواحل مخا همراه چهار شناور نظامی همراهی کننده آن، با استفاده از موشک بالستیک مورد هدف قرار دادند.   به گفته یحیی سریع اصابت موشک‌ها دقیق بوده و این عملیات…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19963" target="_blank">📅 15:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یحیی سریع طی بیانیه‌ای اعلام کرد که انصارالله یک کشتی نظامی متعلق به سعودی را در دریای سرخ، در حوالی سواحل مخا همراه چهار شناور نظامی همراهی کننده آن، با استفاده از موشک بالستیک مورد هدف قرار دادند.
به گفته یحیی سریع اصابت موشک‌ها دقیق بوده و این عملیات منجر به سوختن کامل کشتی و غرق شدن تعدادی از شناورها و سوختن بقیه شد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19962" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19961" target="_blank">📅 15:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPtt2tg64gQbi43EDFQGYa46TBUUZmwFogi-M-Goen-pXHKxyCbwCnuHIw_27VUKNfs-NYLk1MakbV1kkuV4-T_kFSV_cpJ76YX6z9i0O7eFdk6RJm5Jvct2TspFGKeoVC6CFLVkrM1ZaNBfHM8vXGBnvC-ntyLqQqAAStSu6gzc9fYQHL5DTnmAz7HpFFI9lw0QE6ltm-VOVQ89k94lVhCnP6UT_KF4gZnQDBBrGW1tN97EsgaOT-aHkMIca9LIq3E3i_2fB0Fr8_GHTb2ttaALWLRAP4wpXAnfOmPpjSkEsmjNfCY8IvrEtemGglD5SnkYM7Sy1tHbOmqL2TQ-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ترامپ: اگر عمان سر راه قرار بگیرد، آن‌جا را شدیدا بمباران می‌کنیم.  او هشدار داد که عمان نباید در تلاش‌های ایالات متحده در مورد تنگه هرمز دخالت کند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19960" target="_blank">📅 15:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔹
ترامپ: اگر عمان سر راه قرار بگیرد، آن‌جا را شدیدا بمباران می‌کنیم.
او هشدار داد که عمان نباید در تلاش‌های ایالات متحده در مورد تنگه هرمز دخالت کند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19959" target="_blank">📅 15:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ به فاکس نیوز:  ایران باید پرچم سفید تسلیم را بالا ببرد. آنها پوکربازهای خوبی هستند، اما دارند می‌میرند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19958" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ درباره ایران:
ما یک کانال پشت پرده با سپاه پاسداران  ایران داریم. ما مستقیماً با مقامات سپاه صحبت می‌کنیم.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19957" target="_blank">📅 14:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ایران باید پرچم سفید تسلیم را بالا ببرد.
آنها پوکربازهای خوبی هستند، اما دارند می‌میرند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19956" target="_blank">📅 14:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ایالات متحده و ایران بر تمدید آتش‌بس ۶۰ روزه توافق کردند
— العربیه</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19955" target="_blank">📅 14:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">درباره اینکه چرا ایران مداوماً مواضع تجزیه طلبان را در کردستان عراق می زند، یک دلیلش این است که توان ترابری نیروی هوایی ارتش و سپاه در جریان جنگ 40-روزه بشدت آسیب دیده و در صورت ورود زمینی نیروهای شبه نظامی تجزیه طلب، کار پشتیبانی هوایی و لجستیکی بسیار دشوار خواهدبود.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19954" target="_blank">📅 14:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">لطفا یکی به نوید ممدزاده بگه
وقتی روی مواد هست
گوشی دست نگیره
مرسی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19953" target="_blank">📅 13:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19952">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A92r69tmUsNFl3TdlzeODYVNpu73CRNd1aPyo7AZkfmOHT78J0wiHZANDd4PKeU5Hy745rGtrDbbJHs5Wr086TazdWBkR4i-8F2DF3-4kZsQMW5YJQjFI1UTSM7SHcGA4OOGBevjq-DyAo761VRBfHc3dHzutsV0XLOFpArmYNmNCkQ9oeBeIJ9WL4ZFYWx4agTjPSggI_SJQl4PyOBkTUVUVKL9Q9oWLzI1orbDxgAS6t5ox5ANTkejdAOXkXBpiN7DelcTt8lFkPcTN5TikZIuw72HOaF6IBjJWshq5QtpvH6i2WkUx5NmwyCMNITsZh_ag0KpNRoPZ67Jvif3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً بالایی قرار دارد و افت قیمت طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19952" target="_blank">📅 12:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19951">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU-8OI_0Ly3BGc6w-7omoxwZ4sdzLPkX08CIGeuR9-l3ASR909f-gYKlzlfpZ3kuDI3QqM_oIIcTIqeIod5iWlX5UZuVJnT4AelsUQeztoZXn2ZI-Hf1RQ65eoKkBXO4CqaFwY_f2iqpZ0hbo-xAKlasukAGJ7E27rFbUrRS_3dpE6j6NnsAu6g-CnLuygmcsA_DabG4PYY26bb085bt5SbQMyp5cD67wQnJc21IN_jF_8ty6no9IjDECPt-v2JPGc5Nexgm5fBLSslTU_uK6AOU8TvyQ6Bv-T-7LP9znT80ypJm5SSzsL4sBMSSV2AYpFon-d_CoCzrCXOfyhSawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19951" target="_blank">📅 01:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC9X9E9wYHCBhuRLsjbDE0SkSVlfc2yMu98dLO-IJs6PhOD7b-b6xcf5DsVVxygvWlLl5vSQsdYOgg6lt6Gxxyoy59fA5nLkc7BCNCEtdnmxD67AAzwsESSFPwnbIyLTSQZSJGMZ39ojtIuLf1KTdp8X2yiPgxN6G-NfmFhEdr63PXjJpym7eTaFq5W0scFikQQKZLWjSfnjdAblqNNPnLqI7mNHW__SHxJk200HoWpxs4V-IpS2d-KaLmJrupr75C5Hn5Q3UvEzP-oWYWTgc1hHz7KVgcBH6ppPDqyG7lUWxNGoitRAxdPvj0u1ivxjv4KqyNPK97nZBa0HM6xFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ادامه برخوردهای نظامی میان ایران و اسرائیل بسیار محتمل است؟</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/19950" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19949" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">چرا ادامه برخوردهای نظامی میان ایران و اسرائیل بسیار محتمل است؟</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19949" target="_blank">📅 20:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا به پایان رسیدن مهلت 60-روزه در فردا، لزوماً جنگ از سر گرفته می شود؟!</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/19948" target="_blank">📅 18:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بر اساس گزارش واشنگتن پست، کشورهای حاشیه خلیج فارس در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکا از این مناطق هستند، زیرا اعتماد خود را به طور کامل نسبت به استراتژی جنگی دونالد ترامپ علیه ایران از دست داده‌اند.</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/19947" target="_blank">📅 15:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بر اساس گزارش واشنگتن پست، کشورهای حاشیه خلیج فارس در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکا از این مناطق هستند، زیرا اعتماد خود را به طور کامل نسبت به استراتژی جنگی دونالد ترامپ علیه ایران از دست داده‌اند.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/19946" target="_blank">📅 15:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">از فردا با حجم کاری کمتر فعالیت کانال از سر گرفته می شود.
سعی میکنم شاخص GRI دستکم بروزرسانی و ارائه بشود.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/19945" target="_blank">📅 02:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مدتی نخواهم بود...</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/SBoxxx/19944" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAFZkE4ks8R4FCC9izJPVhhkwM5heFAIdMVZTfrrd6kGrRFAyOEeuSZ2anR7alGgzmhOClQFBv-E7LWSSW8q1RJ1hZw656cl4qGHifGxSepeXgh-XIxiXcDMPw_7azt08huRH_MBXs3WYsWx1wvPES2OQccWAyvhY-RKAGFD-azAkrmomM-saDaa-OA-Fe7_SoJspf7TBWGnfrgWLzBDLwANS5Ir_GjMoCKrTbcW3LWPE0I8K40cJAiecZOpAVVqEOIjjt9vzUvYxsTFaanmtyTNFGmFczFaNEH02U-lKg3ypCrPU82RXDt8YpF7dIKfvZUUI5B89t4kvhJ-Rf0oRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه به دنبال تایید ایالات متحده برای ارسال ذخیره‌ای بزرگ از سلاح‌های ساخت آمریکا به اوکراین است!
این بسته شامل موشک های اتکمز و ۴۷,۰۰۰ گلوله توپ خوشه ای است که به گفته منابع، ارزشی حدود ۲۵۶ میلیون دلار دارند.
واشنگتن آماده تایید این انتقال است، اما سازمان دیده‌بان حقوق بشر از کنگره می‌خواهد که جلوی آن را بگیرد و به خطراتی که سلاح‌های حاوی بمب‌های خوشه‌ای برای غیرنظامیان ایجاد می‌کنند، اشاره کرده است.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/SBoxxx/19943" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چقدر خوشحالم جای پاکستانی ها نیستم؛
فردای امضای پیمان دفاعی با عربستان، یمنی ها یک کشتی سعودی را زدند که در اثر آن چند پاکستانی کشته شدند!
الان هم سه روز است میگویند ایران و آمریکا دارند سازش می‌کنند اما ولی خب</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/SBoxxx/19942" target="_blank">📅 14:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:   فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.   ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/SBoxxx/19941" target="_blank">📅 14:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آذربایجان در پی دریافت کمک‌های ایالات متحده در زمینه فناوری‌های پیشرفته برای پاکسازی مین‌های زمینی است.
دهه‌ها درگیری این کشور را به شدت با مین‌ها و مهمات منفجر نشده آلوده کرده است.
باکو امیدوار است که روابط نزدیک‌تر با ایالات متحده بتواند تلاش‌های نقشه‌برداری و خنثی‌سازی مین‌ها را تسریع کرده و بازسازی پس از جنگ را پشتیبانی کند.
منبع: آکسیوس</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/SBoxxx/19940" target="_blank">📅 14:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.
ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/SBoxxx/19939" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/SBoxxx/19938" target="_blank">📅 10:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حالا باید ببینیم ائتلاف «مکه» پاسخ می‌دهد یا صرفا برای دوشیدن گاو شیرده حجاز و نجد تشکیل شده.</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/SBoxxx/19937" target="_blank">📅 10:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/SBoxxx/19936" target="_blank">📅 08:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:  به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.  وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19935" target="_blank">📅 07:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxUeLk6ZqB_hZHIWym9JxIipzvvPxrJn5kGTgndUp6r37gMgiqVdRl9GBeI4cO76tdVzWkmKMr3SQuXlCyIzWpLa6WV1x_FeON1HTNys7zkk_zjwpoPmT5kTnB7h44Fey6iQ7CMlDuBWOSSyy9IPUunKcbDqO2HbRvg3gDnzwXVqPfycWk2SyQY4Y-XvcHG8IZH-g6bpDd6IoA3vdVg3HphObC2MmyO08ECe06w_Xh7FSJSbhXFKeKffX_9Yu6RxOxgV4Wu-4YnpnYQcHxNLGbJcYAzGnI2bwJpilO3AAqM-eAi9OKn8snDI5EYwkXkWUuW0X9iJ7SBU1P7BFuRBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:
به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.
وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق خطوط لوله و تأسیسات صادراتی تازه ارتقا یافته از منطقه خارج می‌شود، ترکیب شود، مجموع جریان‌های نفتی در حال حاضر به طور میانگین حدود ۱۵ میلیون بشکه در روز است.
فقط در روز یکشنبه، بیش از ۲۰ میلیون بشکه از منطقه خلیج عربی خارج شد که این رقم بالاتر از میانگین پیش از درگیری است.</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SBoxxx/19934" target="_blank">📅 07:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کوشش ژاپن در تقویت توان دفاعی  ژاپن با تأکید وزیر دفاع خود، شینجیرو کویزومی، بر لزوم تقویت و تحول توان نظامی این کشور با «حسی بی‌سابقه از فوریت و بحران» اصرار می‌ورزد. گزارش سالانه سفید دفاعی ژاپن، منتشرشده در ۴ اوت ۲۰۲۶، بار دیگر بر تهدیدات فزاینده چین، کره…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SBoxxx/19933" target="_blank">📅 06:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SBoxxx/19932" target="_blank">📅 02:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19931" target="_blank">📅 02:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.  @PressTV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/19930" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=ApekSCr_KkJ32zS-myFXSgvO1ub9eSERMbdp2qXpZElOE0Y0i0W-slxTd30AZKc98Bslq3tb-FphHWJlAodaJF5b5pZ4l8kpq2KiGT8cq10HaOoMwIsimdnDqH3xTsUtgfLq0FbTia4NDudHNvQI_9smZxQ23WkKkHorAS2ryALdtzm0NdBPVsmaQN2EF-_Ptx3xZepu5BcPZJTZvXcFgcmL-1o78tk-yHF1gOW1UFVOX9bRWJThKy0LN9AKlJVB-uo-0TuT9DEYOtoEi7yhXXwPZN0pZOCkAx55tGB6v4yR41HOucZ_WiqZ7dfzYMAR_YQ8_2FRN0cM5T3dTLh6Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=ApekSCr_KkJ32zS-myFXSgvO1ub9eSERMbdp2qXpZElOE0Y0i0W-slxTd30AZKc98Bslq3tb-FphHWJlAodaJF5b5pZ4l8kpq2KiGT8cq10HaOoMwIsimdnDqH3xTsUtgfLq0FbTia4NDudHNvQI_9smZxQ23WkKkHorAS2ryALdtzm0NdBPVsmaQN2EF-_Ptx3xZepu5BcPZJTZvXcFgcmL-1o78tk-yHF1gOW1UFVOX9bRWJThKy0LN9AKlJVB-uo-0TuT9DEYOtoEi7yhXXwPZN0pZOCkAx55tGB6v4yR41HOucZ_WiqZ7dfzYMAR_YQ8_2FRN0cM5T3dTLh6Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.
@PressTV</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/19929" target="_blank">📅 02:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP31hPbm4gSncsBAHnQE6WaNMfpFHRtFvgzqRoaQISKG6Hgp6FXmXxGjSUFA-md-QrtTd3vglcSmG-EbLVW4pOzNDw5O5P7IQa6Wrjp2toLkedwY9E-WeoBBheM8M5-QpZHBWitK33DKkXGaGF7vqq8tsKARZ7jt7rGzKTF0fbQib3UKhxU5rJBXkdLxvcojh7qqPCZRIyTTVq-5HCOWr5UToIe6q-CIA7vFLTkixRfziJDS7Xy85o9oZfwq3f3y2YjvQQkljr9Y1sed8dSxJz1zjoWI4_cYTTRY_wYDENEXC31LpKBLQ553-ZdWlIB3OsNIzysZpNQgNrjKyew5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19928" target="_blank">📅 02:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/19927" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این ترکیب و چینش سیاسی و نظامی خبر از جنگی شدید می دهد.  تًن ماهی یادتان نرود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19926" target="_blank">📅 23:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اساساً به حمایت خاصی نرسید که برای خرید اقدام بشود.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19925" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGBxKdvFWA6XEZbexYLRUPsEtaCKXIOiQ0I6XroHFR1iguoFSBKAqBXjMoqofcUJ-SFyfkE3QnsFrNosDUWrO9L20C-ZvwxEWMxmsWDKxorAFY67BmV9os4BO18reRoAZ1G50ERXI2t-Oev2ZyKkh2-zodBLYifs_qi3OKUlNd2TzgDqlI1GN6OFCz_9x77-n3l7N9fBzoLDiCV5DRDiYL6n4w9RtDSl4TCKvxLH1rsFjzXrFvraZmA7EDFPRFde-QYScDQc6EeAx3WjkOFmm08kDsVzZH-4Nub63gxmRuY0ls59Rd34jpb3ZK_GK4DM5Q7BNhaDPoKB68P-n2iwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19924" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر   ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/19923" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گریدم به اسلام آباد و توافق ش. نفت را دریابید.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19922" target="_blank">📅 20:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران:  پیام ایران روشن است: تنگه هرمز تا زمانی که آمریکا جنگ و محاصره را پایان ندهد، دارایی‌های مسدود شده ایران را آزاد نکند و به آتش‌بس در کل منطقه، از جمله لبنان و غزه، موافقت نکند، باز نخواهد شد.  تا زمانی که تمام…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19921" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">محسن رضایی:   تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19920" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این خواهرمیانه درست بشو نیست؛ ببینید کی گفتم.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19919" target="_blank">📅 20:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3df015c88.mp4?token=kvKweRvHFJQ8gqq_KOhGxuF4LYb8QcJxXksacONAulo2eW7pDe8x3IhpbRWSJNN_Ur2xkqaT4wNJtEiapoYTtJfuO-1Sosl8tr7Y4gxAAFxIli4iJgo0xgpLao1X5_rpsUo-HUs_imXPbQUs9XEj8Pzx1wxL1SWLWuLk6BDepEyR75LcPQiz6CO7i1yBIh8cdwnFxQa9JIU4Nzldfi1L2VxCQ6Q2DiqLBFXYI_qKTl9-ltLKl3OetptDjha0zSqFgxoxc_4exUbpDs3wowMQoJNVkqWNnHfNOpSYHwcAGL8cdvZBz4-eHu4VawMLV4a7WyUE6uRKieR_Mx-_zyfXrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3df015c88.mp4?token=kvKweRvHFJQ8gqq_KOhGxuF4LYb8QcJxXksacONAulo2eW7pDe8x3IhpbRWSJNN_Ur2xkqaT4wNJtEiapoYTtJfuO-1Sosl8tr7Y4gxAAFxIli4iJgo0xgpLao1X5_rpsUo-HUs_imXPbQUs9XEj8Pzx1wxL1SWLWuLk6BDepEyR75LcPQiz6CO7i1yBIh8cdwnFxQa9JIU4Nzldfi1L2VxCQ6Q2DiqLBFXYI_qKTl9-ltLKl3OetptDjha0zSqFgxoxc_4exUbpDs3wowMQoJNVkqWNnHfNOpSYHwcAGL8cdvZBz4-eHu4VawMLV4a7WyUE6uRKieR_Mx-_zyfXrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی بچه های تیم New Castle !  همه هم پنج سانت و ده سانت و …</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19918" target="_blank">📅 20:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19917" target="_blank">📅 20:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ:   ایرانی‌ها با ما بازی می‌کنند، در اتاق‌های جلسات موافقت می‌کنند و در رسانه‌ها رد می‌کنند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19916" target="_blank">📅 18:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19915" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFVuu5KSo_2FzYxWDV40-eauLUl_ZP-vgSanWlPHA0rRAB2ThAmsZuW-BEK80is7fkfP6OPyXBLdN6exSxFvMXbVH0KBPfDiSeelk4_Wmqd7236O5HojT8dImN25-PPPskYTdqtikcK2O-tEvP-36on6TqA3m2d-l2IU_8JA_vFnLCYmvqNawcJxMo_grj_XbTrHg63FOuR4THKJpLsdbYrjny1mrhCtsJI9FW8yBzK_XYcGC58LNe9WmxY4Gdi1iiTdlZujHEpBMCqizOYwlsQl0OGuw1QgzVg6raw0ppuwuR16DtQVftLY-JIgqwtuNfd4kGtAGzZgE9bUanzH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط کم‌سابقه قتل در آمریکا
داده‌های جدید مربوط به نیمه نخست سال ۲۰۲۶ تصویری کم‌سابقه از وضعیت امنیت شهری آمریکا ارائه می‌کنند. بر اساس داده‌های Major Cities Chiefs Association که در نمودار نیز منعکس شده، در شماری از شهرهای بزرگ آمریکا میزان قتل به‌شدت کاهش یافته است.
این کاهش‌ها صرفاً محدود به چند شهر نیست. تحلیل داده‌های MCCA نشان می‌دهد که قتل در مجموعه شهرهای بزرگ آمریکا در نیمه نخست ۲۰۲۶ نسبت به مدت مشابه سال قبل حدود ۱۷.۲ درصد کاهش یافته است؛ بنابراین با یک روند گسترده‌تر در سراسر کشور مواجه هستیم، نه صرفاً یک اتفاق محلی.
یکی از عواملی که می‌توان در این تحول مورد توجه قرار داد، تغییر شدید سیاست مهاجرتی دولت آمریکا تحت رهبری دونالد ترامپ است. دولت ترامپ از آغاز دوره دوم ریاست‌جمهوری خود سیاستی بسیار سختگیرانه‌تر در قبال ورود غیرقانونی، بازداشت و اخراج مهاجران غیرقانونی اتخاذ کرده است. بر اساس آمار ارائه‌شده از سوی کاخ سفید، دولت در کنار کاهش شدید عبورهای غیرقانونی از مرز جنوبی، تعداد اخراج‌ها و بازداشت‌های مهاجرتی را نیز افزایش داده است.
از منظر سیاسی، دولت ترامپ این سیاست را مستقیماً بخشی از برنامه بازگرداندن امنیت عمومی معرفی می‌کند. افزایش فعالیت ICE، تمرکز بر افراد دارای سابقه کیفری، مقابله با شبکه‌های تبهکاری و کارتل‌ها و کاهش شدید ورود غیرقانونی، همگی می‌توانند از دیدگاه دولت نوعی افزایش بازدارندگی ایجاد کنند. داده‌های موجود نیز نشان می‌دهد اجرای سیاست‌های مهاجرتی در دوره ترامپ به‌طور محسوسی تشدید شده است؛ برای مثال، یک تحلیل مبتنی بر داده‌های ICE نشان می‌دهد تعداد بازداشت‌های ICE در مقطعی از سال ۲۰۲۶ نسبت به نیمه دوم دوره بایدن چند برابر شده است.
با این حال، نباید از نمودار فوق یک رابطه علّی قطعی میان سیاست مهاجرتی ترامپ و کاهش قتل استخراج کرد. روند کاهش جرم پیش از آغاز دولت دوم ترامپ نیز شروع شده بود و خود آکسیوس نیز تأکید می‌کند که کاهش جرم در دوره پایانی دولت بایدن آغاز شده و سپس در دوره ترامپ ادامه یافته است. علاوه بر این، عوامل متعددی مانند افزایش یا بهبود عملکرد پلیس، تغییر الگوهای باندهای جنایتکار، وضعیت اقتصادی، کاهش خشونت پساکرونا و سیاست‌های محلی می‌توانند در این روند نقش داشته باشند.
با این وجود، از منظر سیاسی می‌توان استدلال کرد که سیاست «مرزهای بسته‌تر، اخراج سریع‌تر و برخورد سخت‌تر با مجرمان» یکی از مؤلفه‌های محیط امنیتی جدید آمریکا است. کاهش ۶۰ درصدی یا بیشتر قتل در چندین حوزه قضایی، همراه با افت ۱۷.۲ درصدی در شهرهای بزرگ، نشان می‌دهد که آمریکا در حال تجربه یک چرخش مهم در شاخص‌های خشونت شهری است. بنابراین، حتی اگر هنوز برای نسبت‌دادن این تحول به یک سیاست مشخص زود باشد، دولت ترامپ اکنون می‌تواند این آمار را به‌عنوان شواهدی از موفقیت رویکرد امنیت از طریق اعمال قانون و کنترل مهاجرت در برابر منتقدان خود مطرح کند.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19914" target="_blank">📅 18:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:
ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19913" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19912" target="_blank">📅 16:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">محسن رضایی:
تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19911" target="_blank">📅 16:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19910" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.
او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19909" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک نفت کش که قصد داشته محاصره دریایی آمریکایی را بشکند هدف آتش نیروهای آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19908" target="_blank">📅 16:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر
ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در جریان حملات آمریکا و اسرائیل، به‌ویژه عملیات هدف‌گیری فرماندهان ارشد، ناشی شده باشد. مهم‌ترین تحول در این روند، تلاش برای ادغام ستاد کل نیروهای مسلح و ستاد مرکزی خاتم‌الانبیا است. ستاد کل مسئول سیاست‌گذاری و راهبرد نظامی و خاتم‌الانبیا مسئول فرماندهی عملیات مشترک در زمان جنگ است. جدایی این دو نهاد از سال ۲۰۱۶ یکی از منابع بالقوه موازی‌کاری در ساختار فرماندهی محسوب می‌شد و اکنون ادغام آنها می‌تواند با هدف ایجاد یک زنجیره فرماندهی کوتاه‌تر و منسجم‌تر انجام شود.
منطق این ادغام، صرفاً اداری نیست. ساختار جدید می‌تواند هماهنگی میان ارتش و سپاه را افزایش داده، کاغذبازی و بوروکراسی نهادی را کاهش دهد و سرعت تصمیم‌گیری در شرایط جنگی را بالا ببرد. اهمیت این مسئله پس از حملات «سر بریدن» بیشتر شده است؛ حملاتی که با حذف فرماندهان ارشد، توانایی ایران برای هماهنگی عملیات تلافی‌جویانه را مختل کردند. بنابراین، ایرلت ظاهراً در حال حرکت از مدلی است که در آن بخشی از ظرفیت فرماندهی به افراد و نهادهای متعدد وابسته است، به سوی ساختاری که بتواند حتی پس از حذف بخشی از رأس فرماندهی نیز به فعالیت خود ادامه دهد.
انتصابات جدید نیز همین جهت‌گیری را تقویت می‌کنند. علی عبداللهی علی‌آبادی در رأس ستاد کل قرار گرفته و هم‌زمان نقش او در خاتم‌الانبیا، وی را در مرکز ساختار فرماندهی مشترک قرار می‌دهد. سوابق او در سپاه، فرماندهی انتظامی، وزارت کشور و ساختار ستاد کل، ترکیبی از تجربه نظامی و امنیت داخلی را فراهم می‌کند. در کنار او، کیومرث حیدری، با سابقه فرماندهی نیروی زمینی ارتش و فعالیت در خاتم‌الانبیا، به لایه بالای ستاد کل اضافه شده است.
در سپاه نیز تثبیت احمد وحیدی در مقام فرمانده و انتصاب مصطفی ایزدی به‌عنوان معاون فرمانده، نشان‌دهنده بازسازی سریع زنجیره فرماندهی پس از ترور محمد پاک‌پور است. انتخاب ایزدی، که اخیراً مسئول حوزه سایبری و تهدیدات نوظهور خاتم‌الانبیا بوده، می‌تواند بیانگر اهمیت فزاینده جنگ مدرن، حوزه سایبری و تهدیدات نوظهور در معماری دفاعی جدید ایران باشد. انتصاب حسین طائب به فرماندهی بسیج نیز نشان می‌دهد که بازآرایی نظامی با لایه امنیت داخلی و بسیج اجتماعی پیوند خورده است.
در سطح امنیت ملی نیز تغییر دبیر شورای عالی امنیت ملی و جابه‌جایی مشاوران ارشد، بخشی از همین روند تمرکز قدرت و هماهنگ‌سازی ساختار تصمیم‌گیری است. در مجموع، تصویر ارائه‌شده در انتصابات اخیر حاکی از آن است که ایران پس از تجربه آسیب‌پذیری فرماندهی در جنگ‌های اخیر، در حال ایجاد ساختاری متمرکزتر، یکپارچه‌تر و کمتر وابسته به یک فرد یا نهاد منفرد است؛ ساختاری که هدف آن افزایش سرعت واکنش، هماهنگی ارتش و سپاه و حفظ تداوم فرماندهی در صورت تکرار حملات علیه رأس هرم نظامی است.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19907" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ws8eZ6SiawoLpcu22-vex1Rb96t1zTP33dz1K6NfY65W7CxBreoke-Srx4ECWW5Ye_tj9iZyQvxpKcIZr7FTYcIqULeu1wHNQyqJ-6mAYq703G7edFwYbTU4eAv6CeWXJ3_GgVxs586KVSpbJ3IakO7O-3BHaQGkmfgChDG8yl3-xJcUw87AUojHQXsOGCUy-BG1J8ndDhJTNHD-7YJi1DCEsAwYLUlW5Ixq97Dv6KxX3lWdixSKLvFpxvIXZ1tWNLT0-L_P-hBCu0R0zk-EE8j7HMCbUHud81nOlUjQlaSkSGF2e-Vg8IWk-pNOmns8ELaCvIHsezD6rEuvhDPLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه درگیری های میان انصارالله و نیروهای دولت رسمی یمن</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19906" target="_blank">📅 15:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=QON5AfndF-1Ra0Gzhj1i5f1dagXDoA-2PQwCPW82WWLI4uJRrNqiQbP1Jsp5Ia1F4A1i3PwJWc3TZkTgGiR7HMdCH4ldRkGlyDCI9CoUT2EdTJ2lKzJaLqH-DApdFRqw23-IkPh0ngo92UnTbIKmcOX-W58wg_6634RR53m5gODbGNB4KlmQZLVCH2S_lFD_qGwk3SZ_H7z7YnOybylCxmUvMAgLTwWqOJj_f2TCjDLZCcbhqtpGJrFwLBHkMlIGRs63u5ZKvWKxHHnscIP9tdhDbSUgd1Wnf3K9rOTHf_xsZED4wafHYsmQX_sZ25gdYW5psYOKB_Fc1q-K2476sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=QON5AfndF-1Ra0Gzhj1i5f1dagXDoA-2PQwCPW82WWLI4uJRrNqiQbP1Jsp5Ia1F4A1i3PwJWc3TZkTgGiR7HMdCH4ldRkGlyDCI9CoUT2EdTJ2lKzJaLqH-DApdFRqw23-IkPh0ngo92UnTbIKmcOX-W58wg_6634RR53m5gODbGNB4KlmQZLVCH2S_lFD_qGwk3SZ_H7z7YnOybylCxmUvMAgLTwWqOJj_f2TCjDLZCcbhqtpGJrFwLBHkMlIGRs63u5ZKvWKxHHnscIP9tdhDbSUgd1Wnf3K9rOTHf_xsZED4wafHYsmQX_sZ25gdYW5psYOKB_Fc1q-K2476sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  برای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید بگریند. تمام لبنان باید بسوزد!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19905" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/19904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 23</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19904" target="_blank">📅 14:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صد رحمت به جنگ (تحلیل ژئواکونومیک محاصره دریایی)  مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، طی گفتگو با خبرآنلاین با تاکید بر ضرورت فوری پایان یافتن محاصره دریایی بنادر جنوبی ایران توسط سنتکام، گفته است: این محاصره باید پایان یابد؛ با مذاکره، خواهش، تهدید…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19903" target="_blank">📅 14:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19902" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
