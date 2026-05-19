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
<img src="https://cdn4.telesco.pe/file/f3VMPlIyDI8GrdF3Rvwk9HGa5EhoFl6HI6QF07wJIC3kj3Af7oHmQDFma6-5L6wXA_a_8FlRSzoARvgz7SVcKJXMFWwQUUUEbvh5cSyLfZW8QVJeRxKMcMEVd0oBxbmOu7zIir0GzofuXfmZdm46B3QHWmOiJV7ZyXOMTp9VYOAmJg6MkH4eqFcm0Q3XqliHbM_FGx0y2OlnlIKSYAV2-L1K3viuWesKc8rB5jKXjz-e4RfbslVlznrjhoeV3doxXJwH-BjX4EbKZH7oPtrbQdS4M-LtDgLar8ysQnvEOZfcoT0rLsrkzrEwRjBGeit8vld_rweloPr488nO6DQbiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 20:16:10</div>
<hr>

<div class="tg-post" id="msg-436693">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCO-Vsu6n7y4VVYpeQ5DX8oCGXM8eCuUP43JiFiwDPGIHmoHWLh1uymMXR8GLLGh00rYzLLg1NKe8BziMxlHHiepSmtZqPm60Jkyiig3egkBnMGlQa6DrOa230RU65YO2Vr1aUjrMGYcwYB0C11mEG1AfpdgCHxjHB7QtVNhzMzNPcvawd5PMm_9W3hUWWpqe30Y5uXlWE3-G2ZeWwo1jj7ILCTPD_ZgD_vsYTiA5Gl9I_0NFVA2Chn5QLrkCFmhejUR0YYJA6vful3zhR34sKEnReoSU412oCfPyL3E7-JpzOwmHUgpJm-xc7KV2R1BGM0b2umqYvO-Gwc7cUsE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزاداری مسلمیه ۳ شب در شهرری برپا می‌شود
🔹
معاون آستان حضرت عبدالعظیم(ع): مراسم ایام مسلمیه و شهادت امام باقر(ع) در روزهای ۲، ۳ و ۴ خرداد برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 654 · <a href="https://t.me/farsna/436693" target="_blank">📅 20:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436692">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d7386ddfe.mp4?token=ptey8GInZIMeXTYTU_m1CqGm-M6BSiwjAOGP3yj93fP9UCuaNaO5W4LPsFAwCeGQqp9bfsORisuIxnLkwHgs2Q9sY97xVqLg-Z8pxzbcnl-zuuLWCl_eqEdHD377DGx5R0sfVtqWPFtEmC6qaZOOA330X4EU_d8lQj_OPosTSMSSczhCCJiZXeIaw1oa6wZq_jHIiF6gqWyEnLroyhTQwWxGLe5LWcARrqoFMNGlf88CZwzPSZlep8IXuHkGd56Z8YThA_kWAqFMjGqZXcAfTHC53XNZYLPtjPOeO0dzgHS5AcELEY5M5AZ57NxCZ9NUE-t_yYPfAaP4CURJ1wGP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d7386ddfe.mp4?token=ptey8GInZIMeXTYTU_m1CqGm-M6BSiwjAOGP3yj93fP9UCuaNaO5W4LPsFAwCeGQqp9bfsORisuIxnLkwHgs2Q9sY97xVqLg-Z8pxzbcnl-zuuLWCl_eqEdHD377DGx5R0sfVtqWPFtEmC6qaZOOA330X4EU_d8lQj_OPosTSMSSczhCCJiZXeIaw1oa6wZq_jHIiF6gqWyEnLroyhTQwWxGLe5LWcARrqoFMNGlf88CZwzPSZlep8IXuHkGd56Z8YThA_kWAqFMjGqZXcAfTHC53XNZYLPtjPOeO0dzgHS5AcELEY5M5AZ57NxCZ9NUE-t_yYPfAaP4CURJ1wGP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی فیفا به پهلوی در جام جهانی
🔹
نشریۀ اتلتیک از منبعی در فیفا اعلام کرد که این نهاد قصد دارد آوردن پرچم‌های دارای شیر و خورشید را در ورزشگاه‌های جام جهانی ممنوع کند.
🔹
در جام جهانی قطر هم برخی از هواداران پهلوی پرچم‌هایی به ورزشگاه‌ها آورده بودند که از…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/436692" target="_blank">📅 20:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436691">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‌
🔴
هدف‌گرفتن گنبد آهنین و پایگاه رژیم صهیونی توسط حزب‌الله  حزب‌الله: یک سکوی گنبد آهنی در شهرک مرگلیوت و یک پایگاه تازه‌تاسیس رژیم صهیونی در شهر مارون‌الراس را با پهپادهای انتحاری هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/farsna/436691" target="_blank">📅 19:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436690">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqu4DAOkAAWTOogaNxb248fk9bsZeCktQht5pOrUHXnnEuiVJA-qf7Of3K7m6BO0V1qBtTP-IVHJsVBNygLPGsEV7CuSuhAIlVzO3Q-sCnRtzdFiyUFQMlveQSnj5gUiJ8233X2zOQlac2Syw2zPRH0IyRqHoMuFiIWdBuWW9bJQ8AvUUZA9RDnJwon2CwVZHd75_ta0B1DHNurXxyTeUl6402El8esh1uj0wRhUsB2DqOhgP2HqT4nv_3O3rgn4k-wgrVes1mUR_tN204ZalAzitPdM5aO8BgNzejsEftTBovgSADSlBkuc_sWl7KNqiE3TMYC0lhmvVwF4tqTlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولد ۱۰ نوزاد خارجی در رویان
🔹
پژوشگاه رویان: از ابتدای سال، ۱۰ نوزاد زوجین نابارور خارجی که از استرالیا، انگلیس، عراق، افغانستان و پاکستان برای درمان به ایران سفر کرده‌اند، به دنیا آمدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/436690" target="_blank">📅 19:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436689">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
واکنش وزیر کشاورزی به بازار سیاه گندم
🔹
روال همیشگی نشان‌داده که کشاورزان مایل هستند گندم و محصولاتشان را به وزارت کشاورزی تحویل بدهند. @Farsna - Link</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/farsna/436689" target="_blank">📅 19:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436688">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ce9cf249.mp4?token=Y56DvHOPZs7Ws5liVMQPLdcu6jPFW8nJ8occuOeW_9EMuPwM1_VKCime0lPDNTqxEgjVPBu5n2kwo-DAXtUt8PBERT9DkAuZYISdyw8ZmiwzvOQNtjuUHWyQicqFAXpVpR50aql6t6HPqy2fbXyBFRhogHgQ7QXgudpKGo34x6-n1fmGG2Mr7bqkREVb60GomD5lueiuNAVax4J9wBn3jieXwmt98ig1PxxYfzohtZxzmX1AarLwIjUI1DumBcaTK3UcQyhiAh8sIwk6Cmdc6MYffB3NWKeJP-v2Hr2-1ucCFRoPh7oed814FtZeZISk9_sgRWdhlsNxTXCTalzZGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ce9cf249.mp4?token=Y56DvHOPZs7Ws5liVMQPLdcu6jPFW8nJ8occuOeW_9EMuPwM1_VKCime0lPDNTqxEgjVPBu5n2kwo-DAXtUt8PBERT9DkAuZYISdyw8ZmiwzvOQNtjuUHWyQicqFAXpVpR50aql6t6HPqy2fbXyBFRhogHgQ7QXgudpKGo34x6-n1fmGG2Mr7bqkREVb60GomD5lueiuNAVax4J9wBn3jieXwmt98ig1PxxYfzohtZxzmX1AarLwIjUI1DumBcaTK3UcQyhiAh8sIwk6Cmdc6MYffB3NWKeJP-v2Hr2-1ucCFRoPh7oed814FtZeZISk9_sgRWdhlsNxTXCTalzZGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام یک تانک مرکاوای اسرائیل با موشک‌ هدایت‌شوندهٔ مجاهدان حزب‌الله در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/436688" target="_blank">📅 19:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436687">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGzKBh9KbTVlJdU1YkikF1bn7-QKQCr09dRIen_D7MmQlp_RL4Wx_1_nWm8YeFceV0hl7nBvX9ehcbrzEOTTuUw70yaF4zFuzLtWV59u1Q7kZGgkvCCVNWvduw6rUGpZrrC9CJp-tI4vKqPjNUUxunefVXf5zfHrnON_4WM81XTbIamzqEpYgTMsg-368_i8o75eqRaktJIEwmBuHR-imObHMs16HBozIVPZ9c8zXLV0tITI-MdNXXA80Zuw1SCrMscmwzEXXz6Jd570WkxYeUhY7yr63w-hvQX1gQCEa7y6oHr6kWeIfrsCdi6sBH15RcUh88yYKzY7_hysaFC83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات چای مجاز شد
🔹
صادرات چای به‌صورت مجاز مشروط از سوی دفتر مقررات صادرات سازمان توسعهٔ تجارت به گمرک ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/farsna/436687" target="_blank">📅 19:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436686">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
بیعت عشایر بختیاری با رهبر انقلاب در خیابان کشوردوست
@Farsna
_
Link</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/farsna/436686" target="_blank">📅 19:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436685">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b981437517.mp4?token=Tnor5xP2RIWkd9I11ql7WhUul1Wh84t_mYKQdP3LhmIcDI7mw_wjTpzMbMaHgZ-xgPi3T3as8bO1k0XyiCixq0mpZ_mYlojhaxNaYC2DRJ1z-wj1VM8M3CpZB7WLtqBFryUcjc3TN_5ivGK4pEuDN3Kg1dEKhasUe5tPGO3qlySC2yi2RbEQ7hc5kmInAQKnXNhgXDI7R5A72LeX_P-QTiJjWBP9GFwGJVZbETkD2oycV2mVsImOALZ5-jyOpfrcgvaimtmddaacGyDGYUnAH9El6uU2uNuZ3VBzH2hsGJf8VORZCGeewxjwAbND8QSSkmRGVbB9GMWk5ibGa-Qd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b981437517.mp4?token=Tnor5xP2RIWkd9I11ql7WhUul1Wh84t_mYKQdP3LhmIcDI7mw_wjTpzMbMaHgZ-xgPi3T3as8bO1k0XyiCixq0mpZ_mYlojhaxNaYC2DRJ1z-wj1VM8M3CpZB7WLtqBFryUcjc3TN_5ivGK4pEuDN3Kg1dEKhasUe5tPGO3qlySC2yi2RbEQ7hc5kmInAQKnXNhgXDI7R5A72LeX_P-QTiJjWBP9GFwGJVZbETkD2oycV2mVsImOALZ5-jyOpfrcgvaimtmddaacGyDGYUnAH9El6uU2uNuZ3VBzH2hsGJf8VORZCGeewxjwAbND8QSSkmRGVbB9GMWk5ibGa-Qd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز تمرینات بدنی شاگردان قلعه‌نویی
@Sportfars</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/436685" target="_blank">📅 19:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436684">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6077f0e9.mp4?token=gwuyW5vNbZTJL9FMSNcdHXm4IMNv5zv0AEwYNGDYDS5V0f6x6Ap4OBV6jBoaCVdqTaYORSOEQOlpUFZ2h0T-yWYbOlO6LRVqPElps9LJ3nqnuJ8bpZftMqvkFefwQBX6uFRLV7po10xPPuWGMxOIFSqtuKxnzfZH46yzZ6UycLU0IACmxTktwcqnuqEjiCkcXUXPveCmoc2OLxw7_lOHX5HfAsXj-Kf5w6a_ZI_v0ewXj3BE0t0DpVadUrep9gXwEAgjTXT7w-WOumgOxARO5cFkTulNIEM2ZleZfa17crSAovjWQjIAaiyUk3dlynUdQaeLYnZOydls-2yITx-AwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6077f0e9.mp4?token=gwuyW5vNbZTJL9FMSNcdHXm4IMNv5zv0AEwYNGDYDS5V0f6x6Ap4OBV6jBoaCVdqTaYORSOEQOlpUFZ2h0T-yWYbOlO6LRVqPElps9LJ3nqnuJ8bpZftMqvkFefwQBX6uFRLV7po10xPPuWGMxOIFSqtuKxnzfZH46yzZ6UycLU0IACmxTktwcqnuqEjiCkcXUXPveCmoc2OLxw7_lOHX5HfAsXj-Kf5w6a_ZI_v0ewXj3BE0t0DpVadUrep9gXwEAgjTXT7w-WOumgOxARO5cFkTulNIEM2ZleZfa17crSAovjWQjIAaiyUk3dlynUdQaeLYnZOydls-2yITx-AwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین وارد پکن شد
🔹
رئیس‌جمهور روسیه فردا با همتای چینی دیدار می‌کند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/436684" target="_blank">📅 19:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436683">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7Hx-lbABA-BpucTWJg6YlGwLH_KBoah_M4FpHrjyWR77hQ-KptAzyrpVKbe31spm-0mogPwO8Yjxpi7lzBYTxpbaRVLDhyh3ePmMHVna6yxiDS5ZRtSljotxUGb5keOYlWGCFUzm8nPLyNTUJDUNqJNN1uGWlZe6yHz0OfaI1H9EXcPCi3km7vAWZZReJ2SCKdOl74-mT7RwlJEaQU7ltx5hYMAvGmokOPYLV1g-rqLyzNUWA4NeTPfOIdpQWFRazuY4Xms8g-y_gNR-yG95oKiX0Jz4AGep9JkM9S9KOOGMXcIm2Nb0iTK-QMlVD_haLtl09RDwkVm_u2NZ4YvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ رهبر انقلاب اسلامی به نامهٔ جمعی از فعالان مردمی حوزهٔ جمعیت
بسم‌الله الرّحمن الرّحیم
با سلام و تشکر از ابراز محبت و مسئولیت‌شناسی فعالان دلسوز حوزه‌ی جمعیت؛
🔹
از جمله دستاوردهای ذی‌قیمت دفاع مقدس سوم و نعمت عظیم بعثت بی‌نظیر ملت که بر همگان آشکار شده، برآمدن ایران در مُستَوای قدرتی بزرگ و تأثیرگذار است. بی‌شک استمرار این وضع و وصول به درجه‌ی مطلوب‌تری از آن، نسبت مستقیمی با مسئله‌ی جمعیت می‌یابد. به مسئله‌ی لزوم افزایش جمعیت، گاه از منظر لزوم جبران کاستی‌های ناشی از بعضی سیاستهای گذشته نگریسته میشود؛ ولی افزون بر آن، با پیگیری مجدّانه‌ی سیاست صحیح و حتمی افزایش جمعیت، ملت بزرگ ایران قادر خواهد بود، در آینده نقش‌آفرینی‌های بزرگ و جهش‌هایی راهبردی را تجربه کرده، قدمهای بلندی را در جهت خلق تمدن نوین ایران اسلامی بردارد. از این رو، تلاش روزافزون فعالان مردمی حوزه‌ی جمعیت و ترویج فرهنگ فرزندآوری میتواند تأثیر قابل توجهی در جهت تأمین این
#آینده‌_روشن
داشته باشد.
🔹
از سویی دیگر، این امر یکی از مهمترین دغدغه‌های رهبر عظیم‌الشأن شهیدمان اعلی‌الله مقامه‌الشریف بوده است که در بسیاری از جلسات، مراودات، و دیدارهای عمومی و اختصاصی بر آن تأکید داشتند و همچنان از مهمترین مسائل راهبردی نظام قلمداد میشود. امید است تلاشهای خالصانه‌ی شما عزیزان در پناه دعای خیر سرورمان عجل‌الله تعالی فرجه‌الشریف به نتایج پرباری منتهی شود ان‌شاءالله.
سیدمجتبی حسینی خامنه‌ای
۲۹/اردیبهشت/۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/436683" target="_blank">📅 19:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436682">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
روایت جانسوز شناسایی یکی از شهدای میناب توسط مادرش
@Farsna</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/farsna/436682" target="_blank">📅 19:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436681">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f86e9a08c.mp4?token=bzU74wad5_0jlBTCmpusbDYBpr9LnrS5_EoHxZu373vS5U2vtBgjOoxVECATK8mviZtwVk2fp2LKfA8ubzv128JZasSfH-lpReDGq1n7bENCBqaSIgp9hZXKeXL8iBj_zowA7zVpx9spC4KVjqasdryOGjgrno3Ui2YxBMDqBgEAJAo9L2lhSJycr7QoGmDusP7FDI5o5qPJn4yebWddGoQENEzt_czcWZ6E_g2rjIsvvI3kfKfoSvAH0d1HSDrddB0qUH5X24mccUG5zZUiR7zBBd1A6RlXge61lC7KhHpwVR5_iSI0FWHc61Q1iaeH-jNrE91fGm0DL_SvXEdfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f86e9a08c.mp4?token=bzU74wad5_0jlBTCmpusbDYBpr9LnrS5_EoHxZu373vS5U2vtBgjOoxVECATK8mviZtwVk2fp2LKfA8ubzv128JZasSfH-lpReDGq1n7bENCBqaSIgp9hZXKeXL8iBj_zowA7zVpx9spC4KVjqasdryOGjgrno3Ui2YxBMDqBgEAJAo9L2lhSJycr7QoGmDusP7FDI5o5qPJn4yebWddGoQENEzt_czcWZ6E_g2rjIsvvI3kfKfoSvAH0d1HSDrddB0qUH5X24mccUG5zZUiR7zBBd1A6RlXge61lC7KhHpwVR5_iSI0FWHc61Q1iaeH-jNrE91fGm0DL_SvXEdfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این مکالمهٔ تلفنی رئیس‌جمهور شهید ماندگار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/436681" target="_blank">📅 19:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436679">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b241ac6151.mp4?token=SwvSdJ2CYIzl8JYLMR-LlgoR9P6g7m0-XwKiSLARQYYiudBPr7MRHusamNA5NNGj3QR5ruegC8HpJ9LcPU7_WuxPoMXBk2Bp9nX2qv141-mW6RFBStT9kKPrE0mNVRELv8ZDygOT5mbqyfo6hvcR_4VeInK7Vhmcughm0KBdOsPlvH5RU0iJLzrYg-seIiQvNRuPUiEPCockrvIZ0iSh7c0fmVKWJWdmTEhDUr99-PmlrenN0i5Z6OT7wG5fAG6blibAIY9Ym5i-4iE3W0fgxK6pBdEQIe2H5N6qfOnl2wT8zM5yxgtc1QhYdJMAPcwyPZxNphSX8zGL1jjv0n-07A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b241ac6151.mp4?token=SwvSdJ2CYIzl8JYLMR-LlgoR9P6g7m0-XwKiSLARQYYiudBPr7MRHusamNA5NNGj3QR5ruegC8HpJ9LcPU7_WuxPoMXBk2Bp9nX2qv141-mW6RFBStT9kKPrE0mNVRELv8ZDygOT5mbqyfo6hvcR_4VeInK7Vhmcughm0KBdOsPlvH5RU0iJLzrYg-seIiQvNRuPUiEPCockrvIZ0iSh7c0fmVKWJWdmTEhDUr99-PmlrenN0i5Z6OT7wG5fAG6blibAIY9Ym5i-4iE3W0fgxK6pBdEQIe2H5N6qfOnl2wT8zM5yxgtc1QhYdJMAPcwyPZxNphSX8zGL1jjv0n-07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام ۴ هسته تروریست‌های تکفیری در جنوب‌شرق ایران
🔹
وزارت اطلاعات: سربازان گمنام امام زمان(عج) در سیستان‌وبلوچستان موفق شدند ۱۹ تروریست عضو ۴ هسته تروریست‌های تکفیری را که تحت هدایت مستقیم دشمن آمریکایی-صهیونی بودند را پیش از انجام هرگونه اقدام شناسایی…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/436679" target="_blank">📅 18:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436678">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAgNOxvJz19DsD77hE_C2uEpaMqne-kBsmSeKjrzYwlZIBLCgwcZGQ6jLEmtSwUVlMmNAIbV9XLmxv5OejqDR9q6X9jYjVGxf1MGKo62F5cPnt_DGqrcfQ3uR3K_InFtXBrX-LG9cgR1Ixrw5GY_cxdv7EyCDp75qJ_tHmxGCvvKxmryJVX69ORAu7fYx2surMH39Kv05hLeV8Zaieu54MobRghYx7ZMU3aohUXFqdafIXEHO8KeHrQiIjDVqIAfzZtZ1i1Vwul426yCGCkc0Q4dwKO33Pm_zAhLY8wx-2RC1233O_TeKoMJvxE0GduDm8rqcZ3PQCG6oQ8y-4nDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۹ هزار مگاواتی تولید برق ایران
🔹
وزیر نیرو: امسال حدود ۹ هزار مگاوات به ظرفیت تولید برق اضافه شده که این میزان تقریباً معادل ظرفیت برق کشور عراق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/farsna/436678" target="_blank">📅 18:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436675">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db686a4019.mp4?token=BMSFLKvKUxRicSA_Hj54lyZKvsxeuONt_o0qECdVfwxMJXqAbivjoYkEpZrxFJUtSmUkQYfcgrEIXWOp2kP-IwlZhhQnreHgXxzBVjCxYcEYfWYdoyAcZ1-Nir8T_sO5iqXr5zrX3xzw13Zg1DGoVRWGTH6XYGSFmYEgZ0SfMNSdbhG1tMYVfcKXruDbEf6YFg-LyOQ8t4zxxxkvgpB15ExxUlNnEUzL0IoneA-wPny8K1BvyIKx27nANgBaQlqTC_4OkPHwwAPNS9swcPYGkqT3jxtk2GWmfe6gZIL3gVNLChrhvVX9zKpRBUSV28W4pfPMqRlKiJY-hPUA9VJ2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db686a4019.mp4?token=BMSFLKvKUxRicSA_Hj54lyZKvsxeuONt_o0qECdVfwxMJXqAbivjoYkEpZrxFJUtSmUkQYfcgrEIXWOp2kP-IwlZhhQnreHgXxzBVjCxYcEYfWYdoyAcZ1-Nir8T_sO5iqXr5zrX3xzw13Zg1DGoVRWGTH6XYGSFmYEgZ0SfMNSdbhG1tMYVfcKXruDbEf6YFg-LyOQ8t4zxxxkvgpB15ExxUlNnEUzL0IoneA-wPny8K1BvyIKx27nANgBaQlqTC_4OkPHwwAPNS9swcPYGkqT3jxtk2GWmfe6gZIL3gVNLChrhvVX9zKpRBUSV28W4pfPMqRlKiJY-hPUA9VJ2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: همه می‌گویند [جنگ با ایران] محبوبیت ندارد، اما به‌نظر من محبوب است
🔹
وقت ندارم موضوع را به مردم توضیح دهم چون درگیر اجرای آن هستم؛ اما وقتی درک کنند که هدف، جلوگیری از نابودی سریع لس‌آنجلس و شهرهای بزرگ با سلاح هسته‌ای است، همراه می‌شوند.
🔹
در هر صورت، چه محبوب باشد و چه نباشد باید انجامش دهم؛ چون اجازه نمی‌دهم در دورهٔ من دنیا نابود شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/436675" target="_blank">📅 18:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsqWoqdlvBUmshhbyONuxJB3yKksDYr7A-Ee4aU3X_UAL1Y1h4v9VZDO7z0YHmMZxgmhtH-53IjX6kRznlBU3NAasPZZuqsTYouOcf8eW5TkoAhvSflXJ-ZbumMNk2M4kfxJga6au8HLrXEdZ08zFPG6ANIL8lq-K2w800vhmbblkOSU3Eu3vKmjGZA21CQ0cwKUD5wgkyEqI_2e95CtVIRxYEUzuNB5_D05wZw7wgHPQbMRKxrAt3NEczwKAFnxAKzOQED_cUZALZkbusdO8eYkxG_Z9v_wwiZhDFajORUo9sJl70UKOzlWJd35aN4d5mky9N3ghl3mwoXE5WUnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ترانزیتی ایران و عراق با توسعهٔ بندر فاو
🔹
دبیرکل اتاق مشترک ایران و عراق: براساس دستور فعال‌سازی جریان ترانزیت کالا میان ۲ کشور از تمام گمرکات عراق گمرک‌های این کشور موظف شده‌اند رویهٔ ترانزیت کالا با ایران را فعال کنند و این اقدام در چارچوب اجرای کنوانسیون بین‌المللی تیر (TIR) انجام شده است.
🔹
با مصوبهٔ جدید عراق این ظرفیت توسعه یافته و اکنون تمام مرزهای مشترک ۲ کشور که مجموعاً ۷ مرز است برای ترانزیت کالا در نظر گرفته شده است.
🔹
فعال شدن این مسیر می‌تواند فرصتی برای شرکت‌های حمل‌ونقل بین‌المللی ایرانی و عراقی باشد و حتی امکان ترانزیت کالا از بنادر عراق به سمت کشورهای حوزه CIS و آسیای میانه را فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/436674" target="_blank">📅 18:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8PDw3z1Wkdel0HeE3f5F4aVfugqyymk-rpo81HowtaCPnKHx2xjlDcfoyleQ-aCTmw_uaZUYbAPcpPIVLwlgelqp8SgHjRZW9MxbSJDqrUZbcrAzXBQXRSA739qojAi2L_EfrZF_Hl_yViLxB2TytPrlfME-lDvtu56VLWc_m8-eD2erXNYI4ETpR8cu6Op0cZOzZj8h615t52shLO0LHDesFoFGXqx0Kvd0Jk2wpG67saZml9xXCFPRiRPBYe4ilE63q9oN7nPznHsHcpWrPRlGZZvR6CK-ILH8J45uSfNgbccOYEiRezDjmWx7e9pROuJ6bZjhaYl-zvJARvsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریتیش‌ایرویز هم لغو پروازهایش به تل آویو را تمدید کرد
🔹
شرکت هواپیمایی بریتیش‌ایرویز بار دیگر توقف پروازهای خود به مقصد اسرائیل را حداقل تا اول اوت (۱۰ مرداد) تمدید کرد؛ علت این تصمیم «نگرانی‌های امنیتی» ناشی از ادامهٔ جنگ و بی‌ثباتی در منطقه اعلام شده است.
🔸
پیش از این چندین شرکت‌ از جمله امریکن‌ایرلاینز، لوفت‌هانزا، دلتاایرلاینز، ایرفرانس، کی‌ال‌ام و ایرایندیا پروازهای خود به تل‌آویو را تعلیق کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farsna/436673" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌نکرده در اسلامشهر
🔹
فرماندار اسلامشهر: اجرای عملیات تخصصی خنثی‌سازی و انهدام تعدادی از تسلیحات عمل‌نکرده در روز چهارشنبه ۳۰ اردیبهشت‌ماه از ساعت ۷ الی ۱۰ صبح انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/436672" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db634b8a2d.mp4?token=Z1L3YubFiTLfmnCscCbQ3tfAgCVTycjVsgInjtJ_hUn8mWjeMIP__P6gAnAt3OqCICtpPZWN8pFtW-tJiM-YXgeDlklLakz0G8HDNIfqgqxwj050mdgXIMTdFFgSR6iJlnQVMDyZPqk0y8aW7zKcXyqZ6xlRKCIjag3Gxds-vFQwvkeUWP4_A1dg4EA-1KCsbNSSSMLr0MflEfjs2WNFFTkKAZaoRF288JShjsvDxDO1X94g80VVanBrnvwUzn3AGit7W_IMnzYP25SoOEQRxA5m6t5ev3JdNV6MJJxioC02G09JoAmTVmKUfX9pv53L3KVstyKQAFwI1B2uBFdGYQyBQwzYT743Y1P46a8stLghYRTZEDbKRvFpBs224hzXgnV0KKUZN0Ru_3Sif4Ns0QXMCK9-pYBoN1JHS3kPa2-AcLHRCrZBBCT8q3bL39NxPwJdnDZ2KIEhYn7Z8dmFDFv_01dzIWjC7CfQQdU6JyDp_VNrLcSpIn89AwpmWbJbP52ODAL9GBwnlvxTYR_JVi8sJakoNur4ZfHRUB86Fy1wfK91e7wXvKPo3YGc1EPqT7Rc7mbiw5P-lbSiJzYpDE7yhtxi44Yz8S4m5rnfe8tRw5hPc4C9LfO4PBkZgvawvM7NzBkGBurg2IDUeuVFJAhnuRGJ9Z0k2eK07RE-MUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db634b8a2d.mp4?token=Z1L3YubFiTLfmnCscCbQ3tfAgCVTycjVsgInjtJ_hUn8mWjeMIP__P6gAnAt3OqCICtpPZWN8pFtW-tJiM-YXgeDlklLakz0G8HDNIfqgqxwj050mdgXIMTdFFgSR6iJlnQVMDyZPqk0y8aW7zKcXyqZ6xlRKCIjag3Gxds-vFQwvkeUWP4_A1dg4EA-1KCsbNSSSMLr0MflEfjs2WNFFTkKAZaoRF288JShjsvDxDO1X94g80VVanBrnvwUzn3AGit7W_IMnzYP25SoOEQRxA5m6t5ev3JdNV6MJJxioC02G09JoAmTVmKUfX9pv53L3KVstyKQAFwI1B2uBFdGYQyBQwzYT743Y1P46a8stLghYRTZEDbKRvFpBs224hzXgnV0KKUZN0Ru_3Sif4Ns0QXMCK9-pYBoN1JHS3kPa2-AcLHRCrZBBCT8q3bL39NxPwJdnDZ2KIEhYn7Z8dmFDFv_01dzIWjC7CfQQdU6JyDp_VNrLcSpIn89AwpmWbJbP52ODAL9GBwnlvxTYR_JVi8sJakoNur4ZfHRUB86Fy1wfK91e7wXvKPo3YGc1EPqT7Rc7mbiw5P-lbSiJzYpDE7yhtxi44Yz8S4m5rnfe8tRw5hPc4C9LfO4PBkZgvawvM7NzBkGBurg2IDUeuVFJAhnuRGJ9Z0k2eK07RE-MUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود بازیکنان تیم‌ملی به کمپ تمرین
@Sportfars</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/436671" target="_blank">📅 18:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک خودروی نظامی ارتش اسرائیل در  «مسکاف عام» هدف اصابت قطعی قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farsna/436670" target="_blank">📅 18:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مقام نظامی آمریکایی: جنگ، ایرانی‌ها را مقاوم‌تر و تاب‌آورتر کرده است
🔹
نیویورک‌تایمز به‌‌نقل از یک مقام نظامی آمریکایی نوشت: اگرچه ۵ هفته بمباران سنگین ممکن است باعث شهادت چندین تن از رهبران و فرماندهان ایرانی شده باشد، اما این جنگ حریفی سرسخت‌تر و تاب‌آورتر برجای گذاشته است.
🔹
ایرانی‌ها بسیاری از تسلیحات باقی‌ماندهٔ خود را بازآرایی کرده‌اند و این باور در آن‌ها تقویت شده که می‌توانند با مسدودکردن موثر تنگهٔ هرمز، حمله به [منافع آمریکا] در کشورهای خلیج فارس یا تهدید هواپیماهای آمریکایی، به‌طور موفقیت‌آمیزی در برابر آمریکا مقاومت کنند.»
@Farsna</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/farsna/436669" target="_blank">📅 18:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuEcCkFf4Td7V5gRN0YtjsL6ObZo9yQ7UJ3DwdhH33lkgppyAXy9lq5gdDxmppQNBAfy2FV9r31kSMzqGdpeGcb5ks5CzbffHnPMh6MT96Sr0efOguv-Pffhrb_3xwEIexB6NFkKSWcb4PG3yQIECaUUxNXxqY2gE-6K7SLqWR0thD8HU4TTWGBCBFUVMQp_QB2TxewnufKsl_bdIQENIibe016GgoDX-3aLLbOdhY-zw7sqOQwvxeg42bHQecJ782xmH2838LoQ6qJPf3P6RTs008TfzDgCCqxkDkYzp0TW3hTDUJNNYcukFi1H6m_VXHjLmwyY2uv2BEqCm5_2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsNTKtNyeyPCmW9hlIw4GAhh2_SpjF2xD3RUCPVnrEGtUEUmlJJwpTUhLY8Wuh9unKrrdtnqWUOcV0O-xYH6yklbOVdRpGyy2MxnuvscmW6SYfJnezVTrqzYjM0ObppSnbuCWxpTg-LU6lAcN1CLQObr0719e901ztlVQTTUjDBJAYQWL6B4MoAHgEYQHJSQ56EM6hV_XZ_jljoeO-mxD97aGSzKUMFYUI4aXhqs-XpLBZoHvye5Ev6-yQpwgBWXY4GM5KfNMBdxZVcKKM2oECZRJqShVNg1SrIyN-71Yn5K6ChoXCPb_hqhS7J4mcTTkR1c097b4EXv07aPiLbcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-nAoxW-yhAlEiz5MrNHqm4Cbjo4ipGFXV6vezIh3zjP_WZWHrv5L8APqJBad1e5NgF4IuPqkNuCkftiR6LW9LDJE2IHNW4dHOubbjvFw9pyggbg3XI6HIIgP90mRIgAinwiZ_eQerRGaN9LGMeJEw1U4hqBq2rSnUVNf5u1-mUIuFA3Sp5B67ooMdoie0BfX6Sa-Q4frU_rbJeQq6ytAygeE92Mj42wvUpRIqcaEm2OBuqzbCGT8PbI0Xl6jTtgX2JL7KSoqhJdKfukxkab9o9JNNVxGRERdw6RPwFlHAcZaIn2unXVWrpaEhD4mwc_QxhQZLKXB9oDPAplhdVLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3E2voU6SylFlVXsVCEue8SPfFqxxhevOnhN4hUnjiADL8s6RL8T65e87ec-bHGS8ecBRL69cdKF43R3ewEeBLGVt0YGSCp1AX-VLsgz_xtzkpTgRPK-HNmerk7mqKpwHZjLi32rWVncqS94c01tPzqi0wqrcZZBGUEceQuD__NJ8s0Y_kDXum9-oBgZmsIT7AoIZV_LNCy8-o_RrtthFW-mSXvtCvwRpRT0zozEC3ojtbSH26_ijZrvSXD9v4rj_Z7gM9NuS9CDVhx65MzsMM1qAOCbpbDCKFHHbhjU2OguyKyeGwXgXuFhnqh9uU5r8hRjVUhGCuh325U-1Jm2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1BAdLNe_OrfLU6JXZjirzmg-1kymiMQKIFPuilBWFzZAnmWo9U4OmY5_8PNyoCOP7RrLAucrvrw4xsw5g02eOmstHU_HetlFWB9vqrVRegCXUFE5g36TtsRcjlRcdY_O8S4QYPTtE5FTSuN6RLfMQkxNBW2EEdxZlBhEh_kD5dED2xN5u5zbezg3rcUxcnmdjFWxM6bF1TxDEVnrRebBGIgs1lwU6KWitgWaKfIrw1hRh-r7AhsJVlwGjv2WMtHNRNR0xiG0zkHrERQuXakNwQiLkLxzyzSGsQu7_FbQbkXWjrLbeI6hII52Bdui-yxYiml-YO1vG2ejLREX1YotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjhcPeiRV_N80ofDIMnTZ59kcOPBsKi8arOBBELA7YnabL4XclzLjaM7QBa3POCVKpZVx5Kz0wsqTQ84mzHWdCBH_WgbeBsxHHdE_YHZkxViC1V1Pmn28swPKGmOnQxxtDWgS6RcZ2SoM-myiIJp9pneFWpoPu6EZTIxDehUMNLvdvqrRAI6vCtpFQfR4P7xVLGGNNVcMpwSgc7f0zQZ1h0UAqLaiPoPucHB6Imzbpb4zr6tBzM380OQ51pR1dU7be6Zsgz0O4Wkr0CeA_rUwavqXPjIAuqoy6hrJFPMyUVZlmzPKGRH1-KGRAasgBg2XaU4f5_XzQN6nFWP2dtKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAHgJWNkkXLf3QihDxDBSdzuRKC4CKxSUz9LuvmQfFFxd1kddADvckpEL-jPQ-oCGEOo6Fc-0eI1LpNtAzj0HV9wHXAG44D9MKgIXse8-Uj8-__A_5u9LWQoKtdQreas1YWUo1hrYu-YXHYxu6d37923R-2CGBhUgrcbXut-PjqpA9bmXTc9IGytO_QlGnYY8chaE8KVk1LBmO8ALuIUi4_mKN2k50-ftUJ1k3tpR28iIp1AyyyiR9Dmn6ZPdQ8efXw_WWns-RSTEJ8TmlLetDyjCCZTeNcBwTHKgDbvjWVwhfXqlCHq38iSZNbsJLxK-7Pd0Une9r8WHCmagtu6eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خرمشهر در محاصرهٔ گرد‌وخاک
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/436661" target="_blank">📅 18:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436659">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
حزب‌الله: تجمعی از خودروها و سربازان ارتش دشمن اسرائیلی در شهر «رشاف» با حمله موشکی هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/436659" target="_blank">📅 18:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436658">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جدال بانک مرکزی و تولیدکنندگان بر سر پرداخت وام جنگی
🔹
پیگیری‌های خبرنگار فارس نشان می‌دهد از ۱۸۰۰ همت تسهیلات در گردش پرداخت شده به بنگاه‌ها از ابتدای دی تا ۱۰ اردیبهشت، ۹۰۰ همت آن جدید بوده است.
🔹
رئیس بانک مرکزی می‌گوید که «این رقم بالاتر از هدف‌گذاری تعیین‌شده در شرایط جنگی بود.»
🔹
به‌تازگی رئیس اتاق بازرگانی گفته است که از ۷۰۰ همتی که قرار بود به بنگاه‌های اقتصادی کمک شود، «هیچ مبلغی پرداخت نشده» و ما هیچ گزارشی از استان‌ها در خصوص پرداخت این وام نداریم.
🔹
افزایش نیاز بنگاه‌ها به سرمایه در گردش بعد از افزایش بی‌سابقه نرخ ارز در دی ماه و حذف ارز ترجیحی اتفاق افتاد. اما تسهیلات بانکی همواره به بنگاه‌هایی تخصیص پیدا می‌کند که ارتباطات ویژه‌تری با بانک‌ها دارند.
🔹
کارشناسان می‌گویند برای کاهش انحراف در تسهیلات و دسترسی عادلانه به وام بانک مرکزی با انتشار ریز اطلاعات تسهیلات، «نظارت عمومی» را فعال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/436658" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccf5a176a.mp4?token=uNKg6tr5mMlsN54ESapmFR0_9ARSmUNqvma01zzplmyH6RZ2-UrYIo67d6nK6UiCeyMkWkoUjkillkKTUf1BIE1VwNCe8gae7Agn5Mx7_x05pEsfvKa85VpmxUnX1bjgqKKkPB8KuGm2wuMAM6SdtkrGZU3SM-HyvdLR4VmNkqahueBm58yZ9M_iJrYk-LMmpXRGJ85YixfKm5bFINL9aced9Ad0uJtfJTDmnJfmZGIsbwEj4bd16a61N9zFat2h0MRvzS6JxzX5oRNiRI_KWu-mwzB_Tdzosnfp_ef6LR6hW-G1ReP3c3hNm8yo88mYRImp4J462lnZViZZR18S1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccf5a176a.mp4?token=uNKg6tr5mMlsN54ESapmFR0_9ARSmUNqvma01zzplmyH6RZ2-UrYIo67d6nK6UiCeyMkWkoUjkillkKTUf1BIE1VwNCe8gae7Agn5Mx7_x05pEsfvKa85VpmxUnX1bjgqKKkPB8KuGm2wuMAM6SdtkrGZU3SM-HyvdLR4VmNkqahueBm58yZ9M_iJrYk-LMmpXRGJ85YixfKm5bFINL9aced9Ad0uJtfJTDmnJfmZGIsbwEj4bd16a61N9zFat2h0MRvzS6JxzX5oRNiRI_KWu-mwzB_Tdzosnfp_ef6LR6hW-G1ReP3c3hNm8yo88mYRImp4J462lnZViZZR18S1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هُمای: خاکِ وطن که رفت چه خاکی به سر کنم؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/436657" target="_blank">📅 18:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
شبی که تکّه‌ای از قلب ما در ورزقان گم شد
@Farsna</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/farsna/436656" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کشف نیم‌تن مواد مخدر توسط پلیس بم
🔹
فرمانده انتظامی کرمان: ۴۷۴ کیلوگرم تریاک که در یک دستگاه تریلی جاسازی شده بود، در مسیر بم-کرمان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/farsna/436655" target="_blank">📅 18:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436653">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-39.pdf</div>
  <div class="tg-doc-extra">8.3 MB</div>
</div>
<a href="https://t.me/farsna/436653" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-38.pdf</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farsna/436653" target="_blank">📅 18:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
وزارت دفاع امارات: امروز یک پهپاد ناشناس به محوطهٔ داخلی نیروگاه هسته‌ای «براکه» در منطقه «الظفره» اصابت کرد.
🔹
تحقیقات برای شناسایی منشأ این حملات در جریان است. @Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/436652" target="_blank">📅 17:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
انهدام سکوی گنبد آهنین با پهپاد FPV حزب‌الله
🔹
حزب‌الله در ادامه ضربات مستمر و جنگ فرسایشی خود علیه نظامیان صهیونیست در جنوب لبنان، از انهدام یک‌ سکوی سامانه گنبد آهنین این رژیم خبر داد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/436651" target="_blank">📅 17:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVZPq2IX0DChQSZymcO2m2_ply_i5vqaaEvlCWn5ect7g5x5cLNEXpXcOPQMLzxsVCv4Ge9vt3o-8enrlwyDoe1PM-tKYH3_QusLTkEldcwqXvSlJxWTU9a7_exx0KoixS2xALJSBy4QZ7f0Ci5VjV-azfIA-aZGNJDmJXcqJKJq3joZwbSq4qfyJkb4967jGDxRwfips8x0TxPdwVOxV5sCGWb6alMhQPwWn3VM5OJqziWx61F_GDm8k-O-ZJ9U5poK1JWYtePExZdRW5osoPaHIIeb7wCvbnYrLwDA4UOrMPiimyBm3rSfPMSH1G3NgjnxseOLkRp6MwK3DVli8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: ایران یکپارچه و قاطعانه آمادهٔ مقابله با هرگونه تجاوز نظامی است
.
@Farsna</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/436650" target="_blank">📅 17:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063d55c2bd.mp4?token=jf1kXzLVQuGZPtYkGedO6MitegKvf61Hdx92w1vGY9eJdt1EdP4QpqHRqi2uecVdkRolUzGiZ4B9P9KRxg1zjb1iCwGShsnyw_qQCKMUls-O4yOA_RN9W5OybZajdVDx-W7U-8PlJI_FSh6PLokSl0uQTzi7_9neNHoVkeuP3q_9_AhRCae6E_Fn1bP90W3pTpnQ-BTExoOa-GE_psTwtachtjz92AQJRkzkmeoXTHmYhiPAYF7pBdoisLeYQ3q3xrUnikT7C16Uhu53iESNsHgwyAv14pUkCmFL8bF9f3stkvQrjTzZXbWWxAr_s_TN7pkTvt8a80QnKEfOwqlkpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063d55c2bd.mp4?token=jf1kXzLVQuGZPtYkGedO6MitegKvf61Hdx92w1vGY9eJdt1EdP4QpqHRqi2uecVdkRolUzGiZ4B9P9KRxg1zjb1iCwGShsnyw_qQCKMUls-O4yOA_RN9W5OybZajdVDx-W7U-8PlJI_FSh6PLokSl0uQTzi7_9neNHoVkeuP3q_9_AhRCae6E_Fn1bP90W3pTpnQ-BTExoOa-GE_psTwtachtjz92AQJRkzkmeoXTHmYhiPAYF7pBdoisLeYQ3q3xrUnikT7C16Uhu53iESNsHgwyAv14pUkCmFL8bF9f3stkvQrjTzZXbWWxAr_s_TN7pkTvt8a80QnKEfOwqlkpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/436649" target="_blank">📅 17:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
ادعای امارات: طی ۴۸ ساعت گذشته با ۶ پهپاد که قصد داشتند مناطق مسکونی و حیاتی را هدف قرار دهند، مقابله کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/436647" target="_blank">📅 17:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436645">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/farsna/436645" target="_blank">📅 17:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436644">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیویورک‌تایمز: ایرانی‌ها الگوهای پروازی جنگنده‌های آمریکایی را مطالعه کرده‌اند
🔹
نیویورک‌تایمز به‌نقل از یک مقام نظامی آمریکایی نوشت: «فرماندهان ایرانی، الگوهای پروازی جنگنده‌ها و بمب‌افکن‌های آمریکایی را مطالعه کرده‌اند.
🔹
سرنگونی یک فروند جنگنده F-15E در ماه گذشته و آتش پدافند زمینی که به یک فروند F-35 اصابت کرد، نشان داد که تاکتیک‌های پروازی آمریکا بیش از حد قابل‌پیش‌بینی شده است؛ به گونه‌ای که به ایران اجازه داده با کارآمدی بیشتری در برابر آن‌ها دفاع کند.»
@Farsna</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/436644" target="_blank">📅 17:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436643">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e98f32ddb.mp4?token=ffALAa3MeoCi0OzUBNiT0FyyAExSIi20whb9j0U1SKeKIXYVagqpCmbyHRMw8EvhJcRDW97y4KoULQNp9Cya3vOj9y8UA5pk8elHOVcuhV-FQgjlrKawKN_gTahXKlAsnmJAoWMjEHg_cnTqmKBuabkhAl2YDUqMqpdUiwPO-rMHpOmqhqzERQqtbwoFSZX_xqVxgIbMIAen93o8iy4iEVDjdJELgTyXL0yEqa4cNi_SC9lnncn9kW77Q5GJRbzHwHV8laoYBpS46KmsP6TDrLb8-yL-ac7yx1vsUei2_7DoRBi0f0gPDoJmsA6jDF3rdV4dESoQSMXCNNFYiEKrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e98f32ddb.mp4?token=ffALAa3MeoCi0OzUBNiT0FyyAExSIi20whb9j0U1SKeKIXYVagqpCmbyHRMw8EvhJcRDW97y4KoULQNp9Cya3vOj9y8UA5pk8elHOVcuhV-FQgjlrKawKN_gTahXKlAsnmJAoWMjEHg_cnTqmKBuabkhAl2YDUqMqpdUiwPO-rMHpOmqhqzERQqtbwoFSZX_xqVxgIbMIAen93o8iy4iEVDjdJELgTyXL0yEqa4cNi_SC9lnncn9kW77Q5GJRbzHwHV8laoYBpS46KmsP6TDrLb8-yL-ac7yx1vsUei2_7DoRBi0f0gPDoJmsA6jDF3rdV4dESoQSMXCNNFYiEKrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان متفاوت عروس‌ و دامادها در تهران  @Farsna</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/436643" target="_blank">📅 17:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436642">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okwzwVMjxe7rbuozNctqTuOTKtlmpIRsHxHiv5Jvg6Jp-bV0AlzfLMLZ2qLtYlZc_B0cSk2kczcYph3i3_vHDmKEa_HnxicVQsw-p71XqzlamsPsKlk6WjJCt7GvGDmBSKgKMwt6_jKpi6RslVf8yrlbBo25yiU4KEPKSI_kGYCGs77RF07vrl9SskMI4zFT9pZxrkxBrm5mOguoK1ua5-K-Dq-9le98QDblY5lRfTj4_5jVagSX9dELMhuLVS21Wgembgp3vl3Xnu1NXfcVFbioRsETvpiRZtvdGbWV5hAhX5DeAzEEFuCm-hpRdk20O0_1gHan-uem93FXViI7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پزشکیان! صداقت خوب است اما برای درمان، نسخه لازم است
🔹
رئیس‌جمهور در گردهمایی روز روابط‌عمومی، مشکلات دولت را بی‌پرده پشت تریبون اعلام کرد؛ «نفت فروش نمی‌رود، اقتصاد افتضاح است و کوهی از بدهی روی دست دولت سنگینی می‌کند».
🔹
این صداقت را باید قدر دانست. روراستی با مردم غنیمتی است که می‌تواند پل اعتماد را بازسازی کند؛ اما اگر این صداقت به نقشهٔ راه ختم نشود، به‌جای روشنگری، بن‌بست می‌سازد.
🔹
مردم وقتی می‌شنوند «اقتصاد اقتضاح است» اما بلافاصله نمی‌شنوند که «دولت برای برون‌رفت از بحران برنامه دارد»، ذهن‌شان نه با واقعیت، که با ناامیدی پر می‌شود. فرماندهی که فقط زخم‌های میدان را گزارش کند و راه فتح را نگوید، جنگ را از پیش باخته است.
🔹
خطر دیگر خلأ روایت است. وقتی دولت راهکار داخلی ارائه نمی‌دهد، تنها نسخه‌ای که از بلندگوهای بیرونی پخش می‌شود «مذاکره» است؛ مذاکره‌ای که بهایش تحویل اورانیوم و ازکف‌دادن تنگهٔ هرمز است.
🔹
این درحالی ا‌ست که برای خارج‌شدن از این وضعیت راهکار عملیاتی کم نیست و دست‌کم ۶ مسیر فوری پیش‌روی دولت است:
🔹
مشارکت واقعی مردم
🔹
شفافیت حداکثری
🔹
شوک به بدنه‌ٔ دلالی
🔹
برنامهٔ فوری تهاتر
🔹
جهش دیپلماسی اقتصادی همسایگی
🔹
بازتعریف مسیرهای خنثی‌سازی تحریم
🔗
جزئیات راهکارهای خارج‌شدن از وضعیت فعلی را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/436642" target="_blank">📅 17:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
صحنه‌هایی از هدف قراردادن یک تانک مرکاوا توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/436640" target="_blank">📅 16:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvzYPEcIf_c3tVhTjcxso9BGoVu6ozka22xGo6tWyemCR4pUknGuveT5Y_JhvuciKEMkCiclHtgambwAT3xeRzPovGB3WJlenpW5aB5m5j7pZleHhZaCij5oanjE0dW0oQhG_ChJUj0PkZ4LcqPRt1xzKhjJ-gKNh6E4DRbXOGAeyPmYpHrYvRK_K2IcwmLHa9X6XN3Zoi0vVOXfttqG9Q6pu8p3Dwvx_YvB9Lapa06B8PXNWxnejeHD60cPpoT1qis_lXl9lDcakBX6lhHf-u6BY51aTNPmmG7jI01kwvSwQtMPNiCuc409JG76cA1u0J7q3qhyfuAoubvoiH9NDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نیویورک‌تایمز: برخی مقامات آمریکایی می‌گویند شاید حرف‌های ترامپ در مورد حمله‌نکردن به ایران، فریب باشد
🔹
نیویورک‌تایمز نوشت: «برخی از مقامات آمریکایی هشدار دادند که اظهارات علنی ترامپ در مورد حمله‌نکردن به ایران با درخواست قطر، عربستان و امارات می‌تواند…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/436639" target="_blank">📅 16:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCwqKtmTyhl4rq3q6K3X7nYvre_9TTlpcFGHlWgkgVnU1kkwHdn7Lfg9gU9M3Q7CS37YafMDLPVLFopCAk4t967fuQwPgcvVGlF0UNJ-evaurCmbJjlRGI_J5HYK3vwl_1X3vKCNfvR0OJNtYDZrsr7aV71jmONMpO688CDYPXmGoi0KxPS6KiSZxzgisMyUk5TUq2Jx7CwS6-vfW5LMMUXhDZ2ATE3c9AnMzXfBaHFCAw3W24Y-3_-H0vHX1uPMOvSDV_P-ZePUMuNNHQeoB3nxwSvDAqqHnOLbnw25hPIVi6TCq6tg-H_69UleVSEMX0KhiFAxlLkRe_lCu6BtzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پزشکیان با زاکانی
🔹
رئیس‌جمهور در دیدار با شهردار تهران، آخرین وضعیت عملکرد شهرداری در مدیریت شرایط جنگی، خدمات‌رسانی شهری، بازسازی مناطق آسیب‌دیده و ساماندهی اسکان خانواده‌های متأثر از حملات اخیر را بررسی کردند.
🔹
همچنین بر ضرورت طراحی سازوکارهای یکپارچه میان مدیریت شهری، نهادهای اجتماعی و دستگاه‌های اجرایی برای ارتقای حکمرانی محلی، تسهیل خدمات‌رسانی به شهروندان و افزایش سرعت واکنش در شرایط بحران تأکید شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/436638" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0586d97c1.mp4?token=tAzW5WtEiQKnWx_hsEBycopiz0i2dqXFYtpU_KJIuyxCGjUz4PmQ1-sctq_i-7FOC6oemTvv39FPv1mC5usb9j0_Ec1JDMB1zK7iCWsMLGsg5PpgKPzTJhX5-8GLhVTfphvENjHZFzxsuL8jTpBbHiFX00SRh0fQbxFRonUzP-yELd6qLKX7R1ZUm8rKByyF2Z1s3j3VRfsE1-yhCRXhX1ldHty0VNVJybXk8BnwslZ3cJ6yuaWnEj9WoIgMIjt4KwuF0PoCYz92Umf1iAvf-B96JpknWTpbcRHXSmStnrk6Cuo0d6Jgfqwos62J_HrjSmXOkdH-YV6MysIOkJmxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0586d97c1.mp4?token=tAzW5WtEiQKnWx_hsEBycopiz0i2dqXFYtpU_KJIuyxCGjUz4PmQ1-sctq_i-7FOC6oemTvv39FPv1mC5usb9j0_Ec1JDMB1zK7iCWsMLGsg5PpgKPzTJhX5-8GLhVTfphvENjHZFzxsuL8jTpBbHiFX00SRh0fQbxFRonUzP-yELd6qLKX7R1ZUm8rKByyF2Z1s3j3VRfsE1-yhCRXhX1ldHty0VNVJybXk8BnwslZ3cJ6yuaWnEj9WoIgMIjt4KwuF0PoCYz92Umf1iAvf-B96JpknWTpbcRHXSmStnrk6Cuo0d6Jgfqwos62J_HrjSmXOkdH-YV6MysIOkJmxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آذری جهرمی: اینکه خیال کنند با مداخلهٔ نظامی می توانند تنگه را باز کنند خیالی باطل است
.
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/436637" target="_blank">📅 16:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5b66a691.mp4?token=nX-6GGHUEYyOBAnMHDDF51Fm2UYVLJKibzsbmzkcfhchDY6PMdcvh-sBHeZd6fPrI5mno6XIE_4Jr1ZFDB4hOQfTZwEpfy89EVftIOCDNby060Ul6Aiv-_7lf85-vLxfPSor_TpIOTtjahV3I9V6KdprfP5uEGczSKVuSmhgVfH9xU-Ha-4ECe7ue1WLx1egarPM9tmQGPeV9wvCnB8XLcS3RVDUKGFvBmXfbXPTOGgLxAGKKJbTXczfEkcCrFg-yLjRNaAXJ2flgbNQdF2Ux8cFy7gx983UUXSFmgVQI0BcftuwH_5jVO0hM_XT_0khUonRR6W4qObwNgNXMdPTOqyG2Be4i8THQpJI0wtR4MOitPzAk6hWKzJ9uOga0r-4MHFGkSBOlW9Y_MzZmqboMJr7jSirCG5hqEwHQbr2RzAe9nMcvSVIwAx8FNEGLq-M4wT0WRevQ5-EHhaIA6JTUZAKKOgmET6ROSMtr0_wspBTaQEg66y4vDMbv17DFsS4k2PLhsDMdAeryI0CrMSfA1hRwfpuZvd18zCtx3lFep39KqnAQGOw-UhiYlO6tINl01_4izPL97cWJeXWv0N3ABTEfpd-hQOxLdCB5D7u8aHLqKDrRpvthPYlDyGlowcW8iboXCMNZE-xb0bn78SnSle8Gg8eoXQueqnHtacjnAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5b66a691.mp4?token=nX-6GGHUEYyOBAnMHDDF51Fm2UYVLJKibzsbmzkcfhchDY6PMdcvh-sBHeZd6fPrI5mno6XIE_4Jr1ZFDB4hOQfTZwEpfy89EVftIOCDNby060Ul6Aiv-_7lf85-vLxfPSor_TpIOTtjahV3I9V6KdprfP5uEGczSKVuSmhgVfH9xU-Ha-4ECe7ue1WLx1egarPM9tmQGPeV9wvCnB8XLcS3RVDUKGFvBmXfbXPTOGgLxAGKKJbTXczfEkcCrFg-yLjRNaAXJ2flgbNQdF2Ux8cFy7gx983UUXSFmgVQI0BcftuwH_5jVO0hM_XT_0khUonRR6W4qObwNgNXMdPTOqyG2Be4i8THQpJI0wtR4MOitPzAk6hWKzJ9uOga0r-4MHFGkSBOlW9Y_MzZmqboMJr7jSirCG5hqEwHQbr2RzAe9nMcvSVIwAx8FNEGLq-M4wT0WRevQ5-EHhaIA6JTUZAKKOgmET6ROSMtr0_wspBTaQEg66y4vDMbv17DFsS4k2PLhsDMdAeryI0CrMSfA1hRwfpuZvd18zCtx3lFep39KqnAQGOw-UhiYlO6tINl01_4izPL97cWJeXWv0N3ABTEfpd-hQOxLdCB5D7u8aHLqKDrRpvthPYlDyGlowcW8iboXCMNZE-xb0bn78SnSle8Gg8eoXQueqnHtacjnAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ازدواج
۱۱۰
زوج‌ جان‌فدا در میدان امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/436636" target="_blank">📅 16:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF3C2x2tJ5okabFcsUDor3tMGe9BROMAqukrRBoF9D5HMHsrFebmzc5RzJ1s7RTZIjH86rYxuOObLy9hcqd9eYhdo8dVAgI60zgF09sXLRh9fVYGOCusWHoPRI_JVc2ad1M1S4GZMWLL_3Vm0QHwewtqu6a6q5wymN55zDDAkrBBbRI7erUtlCPyFZZWl1Ij7BKlXtcHcT5nArkOBeddX6tIaRPFCjWPtDAbInIBnJWagKsdJNSbOYf5xrs-tCsvanDeYHe6BCm660YfC1zJbRX1X5NiiQLqwa_iUuhOCbHsCfNdFxV8BJ8FVekwZQwJfwyAARq1wivsBmYVzHfcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین نیروگاه خورشیدی تهران در آستانهٔ بهره برداری
🔹
بزرگ‌ترین نیروگاه خورشیدی تهران با ظرفیت ۶۳ مگاوات در مجاورت شهرک صنعتی شمس‌آباد در آستانهٔ بهره‌برداری قرار گرفت.
🔹
این نیروگاه در زمینی حدود ۹۷ هکتاری احداث شده و شامل ۲۱ واحد ۳ مگاواتی است و پیش‌بینی می‌شود بخش قابل‌توجهی از برق شهرک صنعتی شمس‌آباد را تأمین کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436635" target="_blank">📅 16:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
نیویورک‌تایمز: آمریکا نتوانسته شهرهای موشکی ایران را منهدم کند
🔹
نیویورک‌تایمز به‌نقل از یک مقام نظامی آمریکایی نوشت: «بسیاری از موشک‌های بالستیک ایران از غارهای عمیق زیرزمینی و دیگر تاسیسات حفرشده در دل کوه‌های گرانیتی مستقر شده‌اند که انهدام آن‌ها برای هواپیماهای تهاجمی آمریکایی دشوار است.
🔹
در نتیجه، آمریکا عمدتا ورودی‌های این سایت‌ها را بمباران کرد تا با ریزش کوه آن‌ها را دفن کند، اما خود سایت‌ها منهدم نشدند. ایران اکنون تعداد قابل توجهی از آن سایت‌ها را بازگشایی و پاکسازی کرده است.»
@Farsna</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/436634" target="_blank">📅 16:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YouZXB41L6h8a8fK54VZgv2BSKihUYc7TvSVuB6CrZPA3AqtZp3kZP16iZRacaRlcp7WE6jsBlYY8PUekwyu1MQCNn4HOISymCZIHwFlDWdyTNGTfuukpn7hwarMbBSb4U5gaJm43hYa6BwykfPNZ0e_rLC_5rsOQU2gbhg233cYX7zO0YDRTC6F5UNAHtN-LgZO1rxwEyy7tt3ArppR4oFIJVA0UbeT-8nhd1bwT2YV1xsShgL3Pv6C65lwJ5tCe1KfxLRZAgZ8HdurYFxFyhIQITMFwQ8xsOs6t9MhPt3gFUW4kunbQccfgvAa6JMjIMO8gEb7iNex3JTsKO4pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زمین‌لرزۀ ۴.۶ ریشتری در عمق ۸ کیلومتری زمین، حوالی نورآبادِ لرستان را لرزاند.
@Farrsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/436633" target="_blank">📅 16:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO0LFKvcTzpT7BkoJhjANYbh1aOSaQtvRQNBSqS4z-WoBDBq39jqDUbAzR5jMmc_LztMxAzwrl3xYHT9y4G7pk3njkyhsIqzMcN9CFGdzfbjiOjU3bHzz3BN67ODoCOH5eDe9nbGBuFe0fzwPtIy_nuoGOtTkWWSdFCBN0NG6HPRBKTWTIM1Gelua-18yZ2p8R8kOpELAXvwhB5c4NTEVETU_cAhxAV2w-t0R_GopeHXWox_ue6J-SQi3pC6jBUF42iyfw03etn7244ywn_kDv5QaYbGcW8jPBci4_u7hweBL3ciGiSWDg0CwexJZE4YmgEh2X5uVSaU1Fc1dsE5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتکار ۱۴۰۰ تنی مرغ منجمد در شیراز
🔹
تعزیرات حکومتی فارس: در بازرسی از یک کشتارگاه در شیراز، ۱۴۰۰ تن مرغ کشف شد که از ابتدای جنگ تحمیلی در ۹ سردخانه احتکار شده بود.
🔸
یک محمولهٔ مرغ منجمد ۹۰۰ تنی دیگر نیز روز گذشته در شیراز کشف شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436632" target="_blank">📅 15:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
حزب‌الله: تجمعی از خودروها و سربازان ارتش دشمن اسرائیلی در شهر «رشاف» با حمله موشکی هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/436631" target="_blank">📅 15:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436625">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jz09N2eXNmimwOzzxS-O2qLDys3fNOx2ERxtDjE62dtxNFnDn3nz4_kBaYRQzMMcOsSlDhHA5culj4lA_XlegJzVel-I0-Qrk4uBPEYVCQMcPd8nlLciV-xAE4tH8cEB2RaxJ91oN45lNFY26hq9NB48nNyh0VZTqNrgl5ygdMVwttXh7vgYh0e9WIe-0PfwLc-XrZQ-wNDso6b-WToiofo4AhNit7fgqutMyDDzmsuJLFkGAZJM4lLES6mMh-kipv6xgbQazuVj4Ng9A95GOSGnaUEzqVqhelUhvZ33vZWxg3DDfO8wqSOFP8AST-U-ITe-lUq9jxgQRE7DIsC-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvXcbyXO5jru04HXtV-_gmhullz-fbz4J6qysYgc5ryl_46DH4Qr-A2es-BOY2C1YWvdu_5BEPSXN6YG9HJSGAheusH5dI07Ko24DifQ1-CzIQCXjh5qI7uvyC-PHwx7u75QboGpdgpIFMGyUJ-BPjgWrL66udMyTM8xpkkI0A80P-HgFhkvEPj4bGwKkEqBxIUOPQXAv0qtH6xvROaSIl6AL54a_iiu6SkFcBRWbEftZLGe0bvC5QgGPcOygMIkKwIr64khMOKD7rHl2lw9iR6A_3iLbLdNcHcTrO-y3XSol67Zuc7sz5_4fV7nrfZtj_wtuAe_qyPrjfBq5EMPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUS-voQ3etZwvYlOK77dfDHWJb_IXnfQ0Ac3a8xoRXoaQDD85ePK9UWi6bwQLJa8V9092ppEN8zxL7iVa4VTQ89JoPbodDGc-1hPF9KJxKjABtn7oll9th4FURAy1-aEjSnG-AV_R8lBYBAaRbl9AX8GznlW3hzliM8NtK-GlvSy7ETpIm8UxOZaDVBCcpo-uXkr7dxmBIxpRlvniqxvkNi2SN554F5_jjxNvmUfewQbRbLxtiyN0CTiJAhWSfHHX2r9JUX3kD5ae31a73PsxxmE3MDCNq3v0zFaIOKN09NkUmLJlWz2yGTaeV6qeBUdZT51in6DTJAeIjnwpyqNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1epNCKUY1ir7ruFWghgZpjg44uhk8sGABvR41MqjEMz_hwTLyLbJLDR5VG56dBbLs2pzzdq84onZevs2fYorZGu-gGp6Zno6NRqnw0pzgShTaVBwYmPFkjKRTr9_wUI8ZhDcYEShkhzaLn52IfGLKHOAokocz24iSTifcDRIfMfoflkuBk77yS5YCLEl9F0JAfS6Aqc1mXT4sz1SbzmoUzkJKfjvRMlB8oAUs9Rgfkwbmyk8cfcX2EU6gBo46G5PIGBOqjqGHPaT_1NWUfZR48b9idJPsyIGBi7v_ivLCWARuHcaADBJBU1xfWrTk2myIqME_g18qVplnwNaSZWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6BFmxlAPSf7XNtf2ezW5r_FKW5adgYiPhdXAWAG1xZEBBoRqSSitwzgMCizy3sIOHLOp74ckdJuKiAa4m0rRN-_XqwThyrBw_Tr0FHRAD6GemaSrbut4NZJPcWWah4vkYftQzdVqiP1u5VlvcD-riMstQnsHQktTgzV6yaAmSVulEvJgQCM7GNJiFCCf1U_XeaACOWyV8SvAn5Y6Th3M1vAecoBq4qDmDNxidK12TS-6CgREuViph6pQrsRYRjFSl6gStqtJz2Y39meLL6bCkXFNNCp63WjD8LF21TrysMGX1BKxI_49O3G-vsdlbeWUhxGRdYVYILYqhWDy3l2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUtH1wII4zBik6yH9C1HtKiPVBQNsunURnku2vKVXgtL16Mr-5s46uCr-N9jUu0w4aXLHLC9m-tHUzR12wqT4dkJ0FOiGNe8T3T6c0N3qx1w13ExxHp53PRjUKlv2aUnPYNKhpZFpgovky5wzI4AUOB88g1kfPtxo51OKZHCKTxq_KgqEQXoaTK6czCkFyZQ-9Sl4DyGtHCW5xhJ38jJy86A3M0n5kf3N1dtFCWx21hKLPHASPj4EGNie3_YBbCToAP5FWAhAQ-R_nqo0tMgc9Mq-_yuq3XEae4V0CPcmQz9NMshpb_ly3A2joRIB0bDHQj_ZWf_NBHdd7PZHsay0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تمرین بدنسازی تیم ملی در آنتالیا ترکیه
@Sportfars</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/436625" target="_blank">📅 15:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی: در ایام جنگ روزانه ۱۰۰ حملۀ سایبری به کشور می‌شد
🔹
در جریان جنگ رمضان روزانه بیش از ۱۰۰ حمله حرفه‌ای به زیرساخت‌های کشور از جمله حوزه‌های بانکی و انرژی انجام شد که با تلاش متخصصان امنیت سایبری، بخش عمدۀ آن‌ها با موفقیت دفع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/436624" target="_blank">📅 15:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAuCJ6lJb9j5mFOMJGMQRzo7Sk3YJQ7rrG9kmMGjlFZB_7M89bBTOdxuHQDpyMX1PFe3nxJdktFzcZ5-85t2jQC5fOwsofqOwR6mf6YtJ8b7YryFze5pIsfpU_fDoOgNMp6E_gikrhoygZH2KcEVPiiJTo2rEOU45oQHzp5BnT8urG8fj-OH_6jJ8_Sex_8s9OFN-ALZdz2lMIRCUX8uePTSGZbsG129qDpKNVQA36TLiBxHPZfmUFi25Ya4XLhZas6QBf7hWKh6S4Afj16acDDZoNVGoRE3YQafeLSxnsu2RwX6kZ_80zB-NKuYlg7YMrhw7i139Tp3Ws2y0dbL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقدم‌فر: مدیریت جهادی شهید رئیسی ادعای ناکارآمدی دین در مدیریت را ابطال کرد
🔹
مشاور فرمانده کل سپاه: تحولات دو سال گذشته، به‌ویژه جنایات رژیم صهیونیستی و آمریکا در غزه و همچنین فساد اخلاقی و ساختاری رهبران غربی همچون ترامپ و ماجرای جزیره اپستین، ماهیت پست…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/436623" target="_blank">📅 15:36 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp6UYwoNoEB8dlGv2A0UdKxtgD3F9sF35eYFfmpbF5qWQdtDphisOYxrO9a8q71vR02pM-bpEd8IQQtGr5wSMitEUNc-Kn9unkgR98sgQzS02KOnx5_0Z50FFRZe0yoPK8ZUa1-kaZNBpyZbPsUkXhOc2oiA_QZiZtX0m-I3rJASYj6wrG4R2EshH9wbsTFs3IQFGiHDOP8XW1F7ltbWarViFbmUZFA4R1xINpchoZP6f9g8h_KjKW2wiDGWihFJ3Men8po51mdHRX7jsljaNFF8Us7uvXgqAP53YOqoEgR3nyF1uUobCV96WdtAjIbDY5Oi_b5CwRHwhb8wi9rtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیلی فیفا به پهلوی در جام جهانی
🔹
نشریۀ اتلتیک از منبعی در فیفا اعلام کرد که این نهاد قصد دارد آوردن پرچم‌های دارای شیر و خورشید را در ورزشگاه‌های جام جهانی ممنوع کند.
🔹
در جام جهانی قطر هم برخی از هواداران پهلوی پرچم‌هایی به ورزشگاه‌ها آورده بودند که از سوی ماموران جمع‌آوری شد ولی این‌بار اصلا اجازه ورود به ورزشگاه‌های آمریکا را نخواهد داشت.
🔹
طبق قانون فیفا هواداران حق توهین، سیاسی‌کاری، بی‌احترامی به پرچم و فرهنگ کشورها در ورزشگاه‌های جام جهانی را ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/436622" target="_blank">📅 15:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
منابع خبری از انفجار یک خودروی بمب‌گذاری‌شده در پایتخت سوریه خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/436621" target="_blank">📅 15:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrKbY6YyNYoWKQtGNZYL8zVyKdSjG3MsxP3lspLElDwVZt0ItC7SYpVdfKO9aJsRbSEI8hNQOlBQNBa1MGN1G27vSbuOjk31Od98Q9Slv6vshT5f50KoM56bQkAiTfSiHtRXOdI7zeTePmBo-SRTT0NhxY3xRdjQUlSnDiffyWVLEq6guLdTekYZqVsl8d6Hq6EmAuwDXPbKq65uY_0k8eBKg-I0UfY7FFO0q5O82cgsnixXPGbPltI2BPNLzYYrzA02syMSazQpYtK00zepYn4GmqM9PJWkCnwQh6kZAChJh_bxOXMsaWn4_aTOaTM8QivP_1Z2db_JDqZAMZpy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی شورای شهر تهران: از فردا مترو و بی‌آرتی در تهران رایگان نیست تا زمانی که تعیین‌تکلیف طرح پیشنهادشده به شورا مشخص شود.  @Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/436620" target="_blank">📅 15:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌ نیویورک‌تایمز: برخی مقامات آمریکایی می‌گویند شاید حرف‌های ترامپ در مورد حمله‌نکردن به ایران، فریب باشد
🔹
نیویورک‌تایمز نوشت: «برخی از مقامات آمریکایی هشدار دادند که اظهارات علنی ترامپ در مورد حمله‌نکردن به ایران با درخواست قطر، عربستان و امارات می‌تواند…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436619" target="_blank">📅 15:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMBN0hqKgozrmX8ejhVpFBrUBavSDl1QO4Yh3k3SoG0lTNCBCqR6IG6vN1Q9cHDBQB8mPJhggd_hRSQOK9udJ2UBOci2sCTSmiCDUHCn1gP2J9nPZzJyTgecnsDzlkAa9kHWAJAI-QllAnxZdSNaBMQBiQljK0Mzj7RMwuOgJ50xmGK3BQzQW6SIJKjEmhbZOLSBjT4CdTKM4LccNrdV05ci_R03gRt9tkvTAFR8FbzgOkViQ-JE-SVN6KfINHvGIZZBLE-26uRmwzmZ5YV9If4tRIUd10VoWYO_iC36-JCA3cFJQAZ-1H6D4QOweOljt2wEQgAeSq2nBXWfLE1dAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشترکان پرمصرف برق در تهران محدود می‌شوند
🔹
شرکت برق تهران بزرگ: مشترکان بسیار پرمصرف برق از ابتدای خردادماه با اعمال محدودیت در مصرف برق از طریق سامانه‌های هوشمند و پایش‌های میدانی مواجه خواهند شد.
🔹
ادارات نیز در صورت عدم رعایت ابلاغیه هیئت وزیران با قطع برق مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/436618" target="_blank">📅 14:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📷
زوج‌های جان‌فدا
🔹
همزمان با سالگرد ازدواج حضرت علی(ع) و حضرت فاطمه(س) مراسم جشن ازدواج ۵۰۰ زوج‌ جان‌فدا عصر دوشنبه در میادین اصلی شهر تهران برپا شد.
🔹
از این تعداد، آیین ازدواج ۱۱۰ زوج در میدان امام حسین (ع) برگزار شد.  عکس: صادق نیک‌گستر @farsimages</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/436617" target="_blank">📅 14:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">توقیف اموال ۵۲ نفر از خائنین به کشور در زنجان
🔹
با دستور مقام قضایی، اموال ۵۲ نفر از افراد مرتبط با شبکه‌های همکار با دشمن در زنجان شامل دارایی‌های بانکی، منقول و غیرمنقول به نفع مردم توقیف شد.
🔹
از این اموال ۳۳ مورد در شهر زنجان، ۱۵ مورد ابهر، ۳ مورد خرمدره ، یک مورد در تهران و خدابنده شامل وجوه نقد بانکی و ارزی، اموال منقول و غیرمنقول و طلاجات می‌شود که با دستور قضایی توقیف شده و بررسی دقیق‌تر ادامه دارد.
🔹
از این متهمان تعداد ۷ نفر در بازداشت و تعداد دیگری نیز درحال‌حاضر در خارج از کشور به‌سر می‌برند.
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436616" target="_blank">📅 14:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدای انفجار در قشم مربوط به خنثی‌سازی مهمات عمل‌نکرده دشمن بود
🔹
معاون سیاسی استاندار هرمزگان: صدای انفجارهای شنیده شده ظهر امروز در جزیره قشم، ناشی از عملیات خنثی‌سازی مهمات عمل‌نکرده متعلق به دشمن بوده است؛ ممکن است طی ساعات آینده نیز  عملیات انهدام مهمات عمل نکرده ادامه داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/436615" target="_blank">📅 14:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436614">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c918f9837c.mp4?token=tJo0nMZK9yiext3jbPbIKTF-SXxCK67bkoaJ_xWMkjfZmgT-y-kA1a7EKKcHNpfvCuofn6gWbmbX-zdKukQ63AkfzIS_fzmnqdKYuuvUzCPvy5uEr4IRko6CyAZ0VP8ka-zNblIs9cRtEu_P1rwF4UcOIQsgrcGX5SlDv3cJisNHaRmpOLDUzvXH_pFWpfVa73yj6IqkXC2FHsv0wknZ2My92q10anvSdtqWQYq6u4N_csS7CG96tlqaLwXf7pbPmYia8rSHxEizIw3sTXzCh89SYwuBbFyEf2RTmEo-m4jED6R1j3btOjGI0mNth_ob9db-5MLbdtzg7e6rRmmZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c918f9837c.mp4?token=tJo0nMZK9yiext3jbPbIKTF-SXxCK67bkoaJ_xWMkjfZmgT-y-kA1a7EKKcHNpfvCuofn6gWbmbX-zdKukQ63AkfzIS_fzmnqdKYuuvUzCPvy5uEr4IRko6CyAZ0VP8ka-zNblIs9cRtEu_P1rwF4UcOIQsgrcGX5SlDv3cJisNHaRmpOLDUzvXH_pFWpfVa73yj6IqkXC2FHsv0wknZ2My92q10anvSdtqWQYq6u4N_csS7CG96tlqaLwXf7pbPmYia8rSHxEizIw3sTXzCh89SYwuBbFyEf2RTmEo-m4jED6R1j3btOjGI0mNth_ob9db-5MLbdtzg7e6rRmmZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عارف: این ذهنیت مردم که «کارمند ما را سر کار می‌گذارد و کار ما را انجام نمی‌دهد» باید حل شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/436614" target="_blank">📅 14:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436613">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ نیویورک‌تایمز: ترامپ ابتدا ایران را تهدید و سپس عقب‌نشینی می‌کند
🔹
نیویورک‌تایمز نوشت: «ترامپ بارها تهدید به راه‌اندازی حملات جدید کرده، اما در آخرین لحظات از واردکردن دوبارهٔ آمریکا به یک جنگ گران‌قیمت و نامحبوب عقب‌نشینی کرده است.
🔹
زمانی‌که ترامپ در…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/436613" target="_blank">📅 14:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae2b25b77.mp4?token=N8NdF7zyB5XKxIeMaj7JFW5ZzAIv6SEGgvdmuh439qg0I3ni3WzY2cGkVUHymum5hXVWd_BTMAQpZXDow-ix0Uo14uaefhfdAZbkJBL6-O14e8g-TnYfjmKGpik2W1qk6gP1_Rf2eK46EQxrXr48l1qF2W0Dxfz87cPVCtsNCq0k5QUn8adHU65Yw7DR8hSgiLV3S5cDgxc-_rwbgbUo05_SrsJfCkz93c8D0vZAEZcLnHEKXECDYg2KTYIC5_mj4T47uaSJ0rGMUusyvGwxgLajqftugxCybsmvZINxRI03J2-P6Ms4lO5auIJ5fxU1nK73W_sefbFCIF9594-C8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae2b25b77.mp4?token=N8NdF7zyB5XKxIeMaj7JFW5ZzAIv6SEGgvdmuh439qg0I3ni3WzY2cGkVUHymum5hXVWd_BTMAQpZXDow-ix0Uo14uaefhfdAZbkJBL6-O14e8g-TnYfjmKGpik2W1qk6gP1_Rf2eK46EQxrXr48l1qF2W0Dxfz87cPVCtsNCq0k5QUn8adHU65Yw7DR8hSgiLV3S5cDgxc-_rwbgbUo05_SrsJfCkz93c8D0vZAEZcLnHEKXECDYg2KTYIC5_mj4T47uaSJ0rGMUusyvGwxgLajqftugxCybsmvZINxRI03J2-P6Ms4lO5auIJ5fxU1nK73W_sefbFCIF9594-C8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی حزب‌الله به یک بولدوزر رژیم صهیونیستی  @Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/436612" target="_blank">📅 14:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
آرون مکلین، تحلیلگر آمریکایی: ترامپ در یک چرخهٔ باطل قرار گرفته است
🔹
ترامپ اساساً پشت‌سرهم تهدید کرده که اگر ایران تنگه هرمز را باز نکند و از دیدگاه او در مذاکرات منطقی رفتار نکند، اتفاقات وحشتناکی رخ خواهد داد اما اکنون چند هفته از آن روند می‌گذرد و به…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/436611" target="_blank">📅 14:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKtreC3R3IsWI96RusdUhFjCgXWUxyN6AxF5vEsFWFzBCCTtd6aBy0n5mWJNH5KZF_au34Tvk8JwGmAP8gXgIAfinBwGJKlbpJ1BwukphXRN986wFnmPkvrkkecu7f1LNLH2_YZzLb9BJwYydnIOiKsDhbzA_savojHYtXFSXnxeSHTliGLiEqYzSDgLwH2lWs5MD07Q0EjzTSU6GSqlVYDJNTQyuLNNPJdAujMUVLaRrdVTHJeEzIqP5bbi3pFrX-W3XzhwM1Md7ZEnur51NI4SDg2Qb3HeJ6THKMrQmC34ej3VTs8960x3sCWfO5DmprSooi8PuwuR1drtLwLvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TedO2IRSXdAKysk4l7oBmZ0mMbWddjglLXgTGaNgz4SQQriuLMtt6nmaeyl-V2wE5VkGiGv9wj9VXMvtoYd0ORs82TNQ9XX7t82uFBbzFhZRXQDHol7o4KQyWuFU57Xvg-ti_l_UoD_bROnBAzWRmRwJ3SpebTqxX9SxWCP40uOgSKB9YMFWZ_bMDjj-VyId972pl_tGwSp2cFwW7PsZLl6A1hYX49MXgYLReQfhTRtSacr-pTHQLllMSWmYrGbaFEb4q68C7cNX8L6gSNepHd3TMoM9zAcyOjIdeEQ7uiFWPHk-cgV2Vpm4MRjSTEIw6-EhWgqmfXjfWhc4L344Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_P6Qd3YKf-7vnoCgxJtaW-zsl3pUoGwjJQ8oDui6kUVA9GnSaRJtzY5-01tpx7RyG_8l7dU2DJngDqnc7sApJmU6c0uwUPOxG-CMQAEVq9ygrKJInQsYrkPfSgCGp5081gZB6NIXRGf1Fn_7eYcAJPcqZSIfB5UnPjOZ23EQiuBgPrO_93XI8f_6Fm9ZkUWRp9TvsZr1atMTnFUIw5JMD6cCPXQNXGtz7n0sIe6fzjdJH21k4JipVOzvqbKqZDTyP3zIOuLsm3zphZ-7V8wbQN2N7Bszs0KA_4Zxm8qRG6IjnnbspzlCU1dCRv98b0VP1YjdpdXIFX3DTSBgEdk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpJlgAnVYYzXGTH5WuOhGPd8r1KX03YqMmxZ5nYaxzj9_tZG1hLlqHTP17nBHH4hp2j8jdzLV_Gi1MiF2tNSFQgtfCZ3jGljIVYtGXAUrA4soEDCLQxg8hQCdI4t7LsZwBmCieceZJDHDj3uz73poIUpXhi52EKyZVG6jgk_0ZFFla7UFEvAvu0ew1vYeGgNYb0rQSOEH0ysSMooNXqvKGPD2NJIauEwLCi4x5dswsYSyXPm3AoeI13ZaTTa7Nm6U1UjIemniPLFDLV9rYkw-YUn-coFu6jmMMph4T-KHpQ9hdOf1uA5TiiRUoxFSQIedchZQuajdexEKBzHJ4CywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcZ0uI1GEpetboQP1lw_xSMoadSMW2u7xROPC5Y84lq0b2_ZYgoOrXcLsgJxE4qr4Es1uDCHvvaCTshgJpBLCZeFxrAbLB4FVQsfefP0q9lWZMvpMHmWsz6Zjtzv_w2YC2BDMyGNzyrvibWi2LjLZZghi5OnWsimYI_UJVJNlIg9oT8Z4xtub3YTech4o20csRjP_648HYJmk1OnquEmbCTXU0aPTEbm64PS9jQ3P8Js1PQzdV6UG-wETuWHoKdw-MUFTHzYJn0e1tHfr3LWV3FwUpWCxbxgE7pm9gK_ApUk6TqO7IIQ4Yq51HSKy1vO57wEZhFJ7f69SH3yVXVL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QasULYP2Nv6I5H2bz2Kfff3oDt-o0SyAzb1PiQoQKcXzOm0UAuakoDOuBmVYH-njedVYIfX68uWyRFX_gl4f-vD5ry6SFJ8oCrMXEZzL5S25xnJtuQyyZo_fQTdLgh0z2BFkLJgsZVnVEnhxes2ukNxmj8RQbjco1v9m8FELxIEUpSHHATcFoW_zYYnZra_CqxbrYL-c2YH-Lzs3AntoB557BoGSSmTyIEaB7GWPmlWz5Ae4sbe1Z91L3WdVGY1HZqN6WEIgY1VfUri7plQ6w-lujEWDW71j6DuAV0pBdMf4Ko-HxBPXLlHJRROVLXPxLhEaHVB7QJrPqujwoohOcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم
گردهمایی
روز ملی بومگردی‌های ایران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/436604" target="_blank">📅 14:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سخنگوی ارتش: دشمنان دوباره حماقت کنند، جبهه‌های جدیدی باز می‌کنیم
🔹
ایران محاصره‌پذیر و قابل شکست نیست. اگر دشمن حماقت کند و مجدداً در دام صهیونیست‌ها گرفتار شود و دست به تجاوزی دیگر به ایران عزیز ما بزند، با ابزارها و شیوه‌های جدید جبهه‌های جدیدی را علیه آنها خواهیم گشود.
🔹
با توجه به اشراف نیرو‌های مسلح به تنگۀ هرمز و غیرقابل بازگشت‌بودن وضعیت تنگه به گذشته، تنها راه دشمن احترام به ملت ایران و رعایت حقوق حَقۀ ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/436603" target="_blank">📅 13:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436602">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-RDKZ8WFy49aFHksox9rtX-Bw6_z7LmY7U5bFNcz-7MduVajLwsdxyuXNCyt90fJw42wYglb2dJM1aK0vQEZCPp2cIKE_JNGMbygRe5-q8EsYWX-iyrlpn8FwL2UZpXQ-k7VIs3K1V37TsAcRGXNUmtQ_7asEIpVRJaU9ppW0O4rIeH-zmpDfQcpuD27UgwlQlq5k4FwpqrfEBIjlPkvOP0HSNwr5-lXyvHPqXgItj0vAm0y8qlMlEQ73PIhjqMKWowZBZs6jfLDyuzKnbltkgqex_Dj7otKKM72alxteOSVcpCSVOY3odJnJTr-geLIPfQgl-EZ3C5-1iOYlcOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اقتدار امروز ایران ریشه در روحیهٔ مقاومت مردم دارد
🔹
پیام رئیس‌جمهور در آیین گرامیداشت شهدای صنعت پتروشیمی: در روزهای دشوار جنگ تحمیلی رمضان، تلاشگران صنعت نفت و پتروشیمی در خط مقدم جهاد اقتصادی از استقلال و اقتدار ایران اسلامی دفاع کردند.
🔹
دشمنان پس از ناکامی در اهداف شوم خود، زیرساخت‌های اقتصادی کشور را هدف قرار دادند؛ اما فرزندان غیور ایران اجازه ندادند چرخهٔ اقتصاد ملی متوقف شود.
🔹
شهدای این صنعت ثابت کردند جهاد، تنها در میدان نبرد معنا نمی‌یابد؛ بلکه ایستادگی در سنگر تولید نیز جلوه‌ای روشن از جهاد مقدس است.
🔹
اقتدار امروز ایران اسلامی ریشه در فرهنگ ایثار، خودباوری و روحیهٔ مقاومت مردمی دارد.
🔹
عبور موفق کشور از شرایط موجود، متکی‌بر انسجام ملی و اعتماد به توان متخصصان و کارگران متعهد ایرانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/436602" target="_blank">📅 13:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17b16a4f1.mp4?token=NYemzB3bOSmV15_PfGmKrfLZHMbrBJxe7pdAtLGBDec4g_Nggnmumgpkc3bsj2OC0b4DI0O6wtIdRLQ6EkvCA_vV5J-a_H4ZBlKD3MFEq-sq_n1KkSNpG94OBeTQBY_TLO5gf9jcggaBj9ByegB_AkTgjFLVXPs1N0QLIKr8e6SYgF-CguRUX9rF77Mewms4U_fUB5y68WEag8eCNRvlPvnLTl9WUNV_-GungAhJ0aVJ_XFk6HN3XINxoRSXEGYcRV1-VhgUp2Dt_I33AgFD0-aHIDSCaSjjc9r85HvaRTLv2oUgg7DB6uOrKEYfOBNJ52ANneK9GRPvV6UwmkI3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17b16a4f1.mp4?token=NYemzB3bOSmV15_PfGmKrfLZHMbrBJxe7pdAtLGBDec4g_Nggnmumgpkc3bsj2OC0b4DI0O6wtIdRLQ6EkvCA_vV5J-a_H4ZBlKD3MFEq-sq_n1KkSNpG94OBeTQBY_TLO5gf9jcggaBj9ByegB_AkTgjFLVXPs1N0QLIKr8e6SYgF-CguRUX9rF77Mewms4U_fUB5y68WEag8eCNRvlPvnLTl9WUNV_-GungAhJ0aVJ_XFk6HN3XINxoRSXEGYcRV1-VhgUp2Dt_I33AgFD0-aHIDSCaSjjc9r85HvaRTLv2oUgg7DB6uOrKEYfOBNJ52ANneK9GRPvV6UwmkI3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ فوریت طرح رایگان‌شدن مترو و بی‌آرتی تهران برای برخی اقشار تصویب شد
🔹
در جلسهٔ امروز شورای شهر تهران طرح رایگان‌شدن مترو و اتوبوس تندرو برای اقشار ویژه بررسی شد که در نهایت یک فوریت این طرح به تصویب رسید.
🔹
براساس این تصمیم، جزئیات اجرایی، نحوهٔ تأمین منابع…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/436601" target="_blank">📅 13:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKPSz9oGZKbHPEADalwIfubQJ9witUyMxvMKtEZCmxOccHJ6a8gbMpVKGDhQ6otOBSZ48iUMHxnOEYBET8vRqHpuEVKs3Tpb1fMhrGqb5RZB2sCIG4jlxxDbX5cInMqkvUqqV4Z2GF1Bm4wtRpcYGLDyv8tqlU2epPRNbK5KGop2_n2cmTxIDlGBo5zS9KgO6QFTc-qw0i-LRK71G6RGnqiKN-V3q0wocj0hjPZpPCiI357hfK6NDJd_L9SIWlQjRXWcIN7ezMYopf-HVZJH0uJzH_0nxcd6rII1M3tXe9L6lYpFjPwFzhGUMTPvRx5CM6oZa63K_B899yuXpIcMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنگ آغاز معاملات در بورس زده شد
🔹
۲۸ درصد نمادهای بورسی در محدودۀ مثبت در حال معامله هستند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/436600" target="_blank">📅 13:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436599">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fc065a9.mp4?token=vFQHF7P9QxFnRqziB1OLcvL76fCdLMvw_4Yfr2UTxqQyAp3IHk9s-2bM9wYRntBq7z6V-duihW7Zob9XsjrfwKG9Pgslolgpy-A4edUrJHb1A2MN3XE8OZcMyjjx8TMCGtU3uehg0Sq7cl9PvI2rK6eE2c2LKk0emPrwyMUwD6mxVDEcS8vsV9_pjbYKQlfVRA9Ql3lhIQWm87VBRQ-1h9DkxKi8UI1bF2nz8JAu5ICBZsHMSixIVOM-vyTdoeP_MTO0YCy1l3u72lVNRUtBqZosLFROnfnTAXzMUl-GRARBvx-JjzsDvgg0oe3aat4wEAer6IY8SPbLmh0ndhKJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fc065a9.mp4?token=vFQHF7P9QxFnRqziB1OLcvL76fCdLMvw_4Yfr2UTxqQyAp3IHk9s-2bM9wYRntBq7z6V-duihW7Zob9XsjrfwKG9Pgslolgpy-A4edUrJHb1A2MN3XE8OZcMyjjx8TMCGtU3uehg0Sq7cl9PvI2rK6eE2c2LKk0emPrwyMUwD6mxVDEcS8vsV9_pjbYKQlfVRA9Ql3lhIQWm87VBRQ-1h9DkxKi8UI1bF2nz8JAu5ICBZsHMSixIVOM-vyTdoeP_MTO0YCy1l3u72lVNRUtBqZosLFROnfnTAXzMUl-GRARBvx-JjzsDvgg0oe3aat4wEAer6IY8SPbLmh0ndhKJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی رهبر شهید مسابقۀ تلویزیونی را می‌بیند و اشکالش را به داور می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436599" target="_blank">📅 13:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436598">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwmab3bx-qLeC-gSXxvUkwNB9fS87AqvtyynR18xCIq9shCizasY3__2QVx41Qi9eVr7Ika-JxfsbYohLLNdf7RH9wJjJWAJXnkdigi6aa0tjFsTl9qV8bay3uLbXB8pBsExqH9k0GjUElPSfFtcgWcPM6jvGissaueqir0LrPyCMTSwby0N6bcNGjDp1QAG9YiYggjI3-qMC4F0dTFGDaMvOF3owUXWuz-3xwspTYCQt3ppP2UqcpsugEcY5FE4kw0sG4GON9-2zrKcUlY3NPl93BmBRGH2YxiR8AM-6VfnKE3xEtDuuFdh7AwZFhStl4jYNIsAb0ahvr5DqiAS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش زارعی: خودم را سرباز رهبر انقلاب در عرصه فرهنگ و هنر می‌دانم
🔹
کوروش زارعی در گفت‌وگو با فارس: من همیشه معتقد بودم که هنرمند باید فرزند زمان خودش باشد و نسبت به مسائل پیرامون واکنش نشان دهد.
🔹
پیش از آنکه رهبر معظم انقلاب موضوع بعثت هنرمندان را مطرح کنند، کار بر روی پروژه‌های هنری در حوزه موسیقی و تئاتر را آغاز کردم.
🔹
من همیشه خودم را فرزند حضرت آقا و سرباز ایشان در عرصه فرهنگ و هنر می‌دانستم؛ از همان روزی که ایشان به عنوان رهبری جدید منصوب شدند، اعلام کردم که در رکاب پدر عزیز و بزرگوارشان و در رکاب خودشان و سرباز ایشان در عرصه فرهنگ و هنر هستیم.
@farsnart
_
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/436598" target="_blank">📅 12:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436597">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ed86f8ba.mp4?token=n1ArWsrab_O78BZOGRNXE6Ta5a9ZDlmaTlfFTt0fDJ7jI0-HqbwfBE-V3mGqpX8kcmBChKCXOCuXGe-HXc8lWFgqS4yRtxICCYQzNlnPXFqjvF6-yy2T09QKx8Ti0hZsN7e0FGZN-XSVn5fm6WcyPEGuEef0XFBoTBpR9unzoOXtspxoXvI112OZADRLcWNdl4PF-EgMzKvV-ookX7SwU-bZFSR5myPgA-fZ17bX0dVXXuzQY3osdm75zliE7M5kjROFjS5ZQTWep2MG-9LPIzBDXLOAEMCMCzoal7IRJJ-e87wKpdDlvh07qXzmxQLIakvIJCsFUuLskow62KFRQCiL8BVU0ypCZ8xC8h3MHYRnEPAwOPcm0ixGDjc65W_Lr_tyOOZUlkjktJnTPxIOI9zSfdvcFxMfqcEOlkg-tEkMq_CN9wuxYGDmyzIg1auq-Py-OHE0Q0l0pxmd6vkvqOkZffgbRgTkBQBcCIKe3nQ966aYO0Vzr__1b85gh47UDmDTA87CXtDRR-z4ij0t4qLOOIo_ehU3_EMi1ahzZehYKQY0iWf9hwanjqCUzbJxjGMRpPjUcWnhMZ8layc7edzphdmT99j196dyqBdQwyjaIruxk0wE1rZKWTvVGRmYiDuAQR9o3qn4_WbEfuSEAWmdWaZ_m0xHpwoR4hVhLZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ed86f8ba.mp4?token=n1ArWsrab_O78BZOGRNXE6Ta5a9ZDlmaTlfFTt0fDJ7jI0-HqbwfBE-V3mGqpX8kcmBChKCXOCuXGe-HXc8lWFgqS4yRtxICCYQzNlnPXFqjvF6-yy2T09QKx8Ti0hZsN7e0FGZN-XSVn5fm6WcyPEGuEef0XFBoTBpR9unzoOXtspxoXvI112OZADRLcWNdl4PF-EgMzKvV-ookX7SwU-bZFSR5myPgA-fZ17bX0dVXXuzQY3osdm75zliE7M5kjROFjS5ZQTWep2MG-9LPIzBDXLOAEMCMCzoal7IRJJ-e87wKpdDlvh07qXzmxQLIakvIJCsFUuLskow62KFRQCiL8BVU0ypCZ8xC8h3MHYRnEPAwOPcm0ixGDjc65W_Lr_tyOOZUlkjktJnTPxIOI9zSfdvcFxMfqcEOlkg-tEkMq_CN9wuxYGDmyzIg1auq-Py-OHE0Q0l0pxmd6vkvqOkZffgbRgTkBQBcCIKe3nQ966aYO0Vzr__1b85gh47UDmDTA87CXtDRR-z4ij0t4qLOOIo_ehU3_EMi1ahzZehYKQY0iWf9hwanjqCUzbJxjGMRpPjUcWnhMZ8layc7edzphdmT99j196dyqBdQwyjaIruxk0wE1rZKWTvVGRmYiDuAQR9o3qn4_WbEfuSEAWmdWaZ_m0xHpwoR4hVhLZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: ترامپ در حال نابودکردن خانواده‌های آمریکایی است
🔹
کریس مورفی با حضور در پمپ‌بنزین‌های آمریکا از عملکرد ترامپ در به‌راه‌انداختن جنگ ایران انتقاد کرد و گفت: این هزینه‌ها در حال نابودکردن خانواده‌های آمریکایی است. قیمت بنزین به ۵ تا ۶ دلار در هر گالن رسیده و این اعداد همچنان در حال بالارفتن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/436597" target="_blank">📅 12:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436596">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl1_v4kobjWJAwyqazWB2KU22Z79N3-lP5NXTWMa9K6QWGK-QTt01EnZ4rbwayi1bGRzutCCXh8bp7dK0gnTdZGlyNHdBjKEA3ZOstExbDp-13eo3pX_vDhqHwpc0dZUllQ-zFLCLh6cLPPaTjdR1Jgrsq7SoGx7_g5r194dRL2Zn9G6VXmOhKMVkD5DNbP2IlO9tP1g3aEq_R7qoCjhCRXYi_EHI_9AvGOJPK9HrXmmpMY8epXj5vGt9RqgsuU5AsguzGGMKxuimAYovzQ94dbf4xO1awEBcaIwKWGF4oleaFK7akxNAeKtJD2N20vtEfgbr4BkbChrDckD9xnX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت رزمندهٔ بروجنی در مأموریت خنثی‌سازی بمب‌های عمل‌نکرده
🔹
شهید حمید خانی پاسدار بازنشستهٔ بروجن، در مأموریت خنثی‌سازی بمب‌های عمل‌نکردهٔ دشمن صهیونیستی-آمریکایی در تهران به درجهٔ رفیع شهادت نائل شد.
🔹
مراسم وداع با پیکر مطهر شهید امروز از ساعت ۲۰ تا ۲۰:۳۰ در شهر نقنه و پس از آن ساعت ۲۱ شب مراسم شب وداع در روضةالشهدای بروجن برپا خواهد شد.
🔹
مراسم تشییع و خاکسپاری این شهید عزیز نیز فردا ساعت ۱۶:۳۰ از حسینیهٔ ثارالله سپاه بروجن به‌سمت روضةالشهدا برگزار می‌شود.
🔹
همچنین مراسم ترحیم شهید خانی فردا شب هم‌زمان با آیین بزرگداشت سالگرد شهادت آیت‌الله سیدابراهیم رئیسی در بروجن برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/436596" target="_blank">📅 12:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436595">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بازگشایی مرز ایران-آذربایجان برای واردات خودرو
🔹
براساس جدیدترین تصمیم هیئت وزیران، گمرک منطقهٔ آزاد اردبیل-بیله‌سوار در شمال‌غرب کشور به جمع گمرکات مجاز ترخیص خودرو اضافه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/436595" target="_blank">📅 12:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436594">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463189fa48.mp4?token=DKKiGsRwuju5iaSQySMzehe8Yo6KhPM6cNOJskc6eeRDcE2vADOZpxW_56pJtGf0OEg2m5f5k-0WbkjtxPKABpPyBySYBJv8bNeF8ccjtRQEzPZwukPIGrXVqqcEVnXHkFNBVUeQQQvI6O8WR4q-_Ydv69gRLOg_Aq7Gv1lfEh6TyMyNPHveUtc7Ce6GjsZ-_YC58rBkXNLrnOJlfFRGGU2rU_EOFD1JYxE0hBf3uOBl256hfdqXdimvEDVZ9OSz478QlbpiLPdSx7uBzDbTGTQx1k71gE3zzQSBqGP3_7KbwtEyP7E-whT8S8dAvhGG4ykxNTA2IfSFx3v20yLqlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463189fa48.mp4?token=DKKiGsRwuju5iaSQySMzehe8Yo6KhPM6cNOJskc6eeRDcE2vADOZpxW_56pJtGf0OEg2m5f5k-0WbkjtxPKABpPyBySYBJv8bNeF8ccjtRQEzPZwukPIGrXVqqcEVnXHkFNBVUeQQQvI6O8WR4q-_Ydv69gRLOg_Aq7Gv1lfEh6TyMyNPHveUtc7Ce6GjsZ-_YC58rBkXNLrnOJlfFRGGU2rU_EOFD1JYxE0hBf3uOBl256hfdqXdimvEDVZ9OSz478QlbpiLPdSx7uBzDbTGTQx1k71gE3zzQSBqGP3_7KbwtEyP7E-whT8S8dAvhGG4ykxNTA2IfSFx3v20yLqlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام ۴ هسته تروریست‌های تکفیری در جنوب‌شرق ایران
🔹
وزارت اطلاعات: سربازان گمنام امام زمان(عج) در سیستان‌وبلوچستان موفق شدند ۱۹ تروریست عضو ۴ هسته تروریست‌های تکفیری را که تحت هدایت مستقیم دشمن آمریکایی-صهیونی بودند را پیش از انجام هرگونه اقدام شناسایی و بازداشت کنند.
🔹
از محل اختفای مزدوران یک دوشکا، ۲ آرپی‌جی ۷ به‌همراه ۷ موشک مربوطه، یک سلاح آمریکایی‌ ام۴، ۵ کلاشینکوف، ۶ کلت کمری، ۲ دوربین نظامی و حجم زیادی مهمات کشف شد.
🔹
بیشتر مزدوران بازداشت‌شده از اتباع بیگانه بودند که پس از جذب و عضویت در گروهک‌های تروریستی تکفیری و گذراندن آموزش‌های نظامی، وارد کشور شده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/436594" target="_blank">📅 12:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436593">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSATHZMEiMAfdnWqYn1ABg9Mk_pAsqa_K18Mf8nV7syJgzfwW8YVM75aZBdVls83Nd4aiqgUE4m5ClAtjz9IhRW3TGuR35mYuxxOpW9cFqMYGtzn4bbUQ5y5MYJBlmAYIUf47-Y3cLdG4si1BSd-tZKlR3Et0jwKUdenKEXndUXBjpeZK6o4JnppIuCFYJyJ2hbnq1n85Rl5Q0Vx8unp22qeKfiVpUfdvwmcjp0CmSvwt5s-RibYfJiN4Tm6QoW8m_m73gkAh7Ch7qH6Ab41X_VyStktqlNMO6Oha4-49-L33uwmV4ty3-JMS5x8w3rjqPSQRvMYG0yXgvv-3oHCwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ قیمت تخم‌مرغ کاهشی شد
🔹
رئیس سازمان جهاد کشاورزی آذربایجان‌غربی: واردات تخم‌مرغ شروع شده و امروز ۳۰۰۰ کارتن از ترکیه وارد کشور شد.
🔹
در روزهای گذشته قیمت تخم‌مرغ به شانه‌ای ۶۰۰ هزار رسیده بود و الان در محدودۀ ۵۰۰ هزار تومان و حتی پایین‌تر است.
🔹
هرچه به…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/436593" target="_blank">📅 12:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436592">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiO_k9tuyWWpcadfICnCAF2emKWWMxXq1Cyiyt9nw8XUDGiffMklDtEFQ_uQ9g6apUl1SRl7_x7-1YIWGHnzMuPJVf-lSIRcQCAmXj6XE6Ud53SZUZDuccbSveFlRgSV_i98b5GIsZdtCyVV8uJGwzJh2tuawX6Y21n2qRISnZgHRwxDWlGAGk-gT40gbZEMIzHIG1ldq09e8I-XfXdNV0FqqdBWtSnMXiaUhBWCk71abT04Nil2ioM8BnU5ojrbZGsW4jccQ24jtxi2gf-jGRkYzMn94XG9DgDqGZaG43kTufOTOMN5GyJ1LgodMGoLL1tk2gfeiQD9GdKNoeiVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از ۱۰۰ روایت ناگفته از دولت شهید رئیسی
🔹
آیین رونمایی از کتاب «خسته نیستم» به‌قلم مهدی مجاهد که روایتگر ۳ سال دوران ریاست‌جمهوری شهید سیدابراهیم رئیسی است، فردا ساعت ۱۶ در باغ کتاب تهران برگزار می‌شود.
🔹
این کتاب شامل ۱۰۰ روایت مستند از تصمیم‌گیری‌ها، سفرها و لحظات کمتر دیده‌شدهٔ دولت سیزدهم است و بخش‌هایی از زندگی شخصی و سبک مدیریتی شهید رئیسی را به‌تصویر می‌کشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/436592" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436591">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌ مترو و اتوبوس در تهران همچنان رایگان می‌ماند
🔹
صادقی، عضو شورای‌شهر تهران: تا زمان طی‌شدن مراحل بررسی و تصویب نهایی، روند رایگان‌بودن استفاده از مترو و اتوبوس همانند گذشته ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/436591" target="_blank">📅 11:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436590">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBz6ak5uYsRxT5E8nxoRZOqxdBtkriI1fdFWQTjIuV8EzVUrMJEAVjOmMikAW_cPlhaZzNemThj7L3T-_Hv9t6AvzWAHKWLXu6Hjt_hjt8Cz6iLkCCFM5CievP4lMdEc47otyGXJHsH4flWvJS0p3WoYNnKgQwC8lZnSkTB1uGmkz5OgYcZgn6Q33f7MVy9te09s2jXJwMeuOk0wW0ivhQ7vLhvp0AiSnNoGCadgTUPpv4tJJhcR9oROHfM9Kw19Yx5tiLhG7aAzifT7POllWAvMYlgmq3ITBqe0TkZpNAW1EEj4Hhtw7kN2RYH_R_juYRg2PSAVEZURig8zCWWW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه جنگ برای آمریکا از ۸۵ میلیارد هم عبور کرد
🔹
دونالد ترامپ بر خلاف ادعاهای انتخاباتی خود، نه تنها وضع مردم آمریکا را بهتر نکرده بلکه با به راه انداختن جنگ ایران، بیش از ۸۵ میلیارد دلار از محل مالیات این مردم را نیز صرف یک «جنگ انتخابی» کرده است.
🔹
سایت «Iran War Cost Tracker» پس از ۸۰ روز، هزینه جنگ ایران و حضور گسترده تجهیزات و نیروهای آمریکایی در منطقه را  بالغ بر ۸۵ میلیارد و ۳۹۶ میلیون دلار برآورد کرده است.
🔸
این در حالی است که پیش‌تر جوئل هرست، یکی از مسئولان مالی پنتاگون در ۲۲ اردیبهشت، هزینه این جنگ را حدود ۲۹ میلیارد دلار تخمین زده بود. به اذعان سی‌ان‌ان، وزارت جنگ آمریکا از بیم انتقادات، رقم دقیق این هزینه‌ها را اعلام نمی‌کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/436590" target="_blank">📅 11:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436589">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK-X9SqeuDuf0Zg-IT0Wj9c9S6rw0iHJs2BasiOYUPBB0PNoE12ut-l5dXbTQkdAXCdKm6XMoPKoGrU2Bc3uBakyNVVkdJklhqdKtbQp3mgic1DXqaRuHdWcwCxD4-nvdgjuiTeZqc_dBhVG8qy3PKtuCtcyDhb5uc_J-9h2x7j9Rnf91ARJ8ERWdR49f1OVYjRXAqdsmEoXUPhfcRkVBfO4xNlZY7_TbwTOeQlve-8skGAaavZHxhN8o6_H2Hs7MJ5GQtfpjWByPO2umgIMraJxaQKACJf7NGRXmh8iYpm3AJGRzSAt5W-7aZW1IafL1ZJc6MHi7VY7_idAKgiOKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلیمی: انتخابات هیئت‌رئیسۀ مجلس هفتۀ آینده برگزار می‌شود
🔹
عضو هیئت‌رئیسۀ مجلس: به‌هیچ وجه انتخابات به تعویق نخواهد افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/436589" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436588">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3OfHerqUlNZZASkHCNpH8zKwj3np5_MFDMUT8aMVftgUWHj-Mn2cSJFYkhCBgotwBcwnaE-mg5saiNeqHfl4QZ89dtb_rijgOh9cElSt7JbNNOzSfJ1cs3trcnArin0hICMFuBlP5Xn-YWdkrivOk8TkkZwNxUI_ybNG7Xt1TvMyvzB54kR-i5ZIgR4ieW1CvD6zcFs48eR7kcDcfiav8Vm05eeaa9TvhkvmbgQ2grQHozxG5d0n431K9GE8wGHEkK8HfIfM_ckukrAh837wBMotLHQScQhaKUm7Xj6p1MG7sH3TpcqVzoivzKfsq1lpIVOSDBEz6u2PfXPUQdPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقدم‌فر: مدیریت جهادی شهید رئیسی ادعای ناکارآمدی دین در مدیریت را ابطال کرد
🔹
مشاور فرمانده کل سپاه: تحولات دو سال گذشته، به‌ویژه جنایات رژیم صهیونیستی و آمریکا در غزه و همچنین فساد اخلاقی و ساختاری رهبران غربی همچون ترامپ و ماجرای جزیره اپستین، ماهیت پست حقیقی و ناکارآمدی مدل‌های حکمرانی سکولار را برملا کرد و نشان داد که این الگوها شایستگی سرمشق بودن را ندارند.
🔹
در مقابل، الگوی حکمرانی دینی بر دو پایۀ «سلامت شخصیتی کارگزار» و «مدل خدامحور» استوار است به‌گونه‌ای که مدیریت جهادی شهید رئیسی ادعای ناکارآمدی دین در مدیریت را ابطال کرد.
🔹
شهید رئیسی با وجود عمر کوتاه دولت خود، توانست با کارنامۀ اجرایی موفق و سلامت اخلاقی، این الگو را تثبیت کند؛ به‌طوری که امروز مدیریت ایشان به‌عنوان شاخص و مدلی عینی از حاکمیت اسلامی شناخته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/436588" target="_blank">📅 11:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436587">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سکوت مؤسسات بین‌المللی دریانوردی دربارۀ انفجارهای تنگۀ باب‌المندب
🔹
منابع خبری از وقوع انفجارهای مهیب شب گذشته در تنگۀ استراتژیک باب‌المندب خبر می‌دهند که به مدت دو ساعت تردد تمامی شناورها در دو سوی این آب‌راه حیاتی را به‌طور کامل متوقف کرد.
🔹
به گفتۀ این منابع، منشأ این انفجارها هنوز به‌طور دقیق مشخص نیست و این ابهام، نگرانی‌های جدی را در محافل دریانوردی و امنیتی ایجاد کرده. آنچه بر پیچیدگی ماجرا افزوده، سکوت معنادار و تأمل‌برانگیز مؤسسات بیمۀ بین‌المللی و نهادهای مسئول اطلاع‌رسانی امنیت دریانوردی است.
🔹
کارشناسان ارشد حوزۀ دریانوردی این سکوت گسترده را بی‌سابقه و خلاف تعهدات حرفه‌ای این نهادها ارزیابی می‌کنند. به باور آنان، سکوتی که زیر سوال رفتن تعهد مؤسسات در حفظ امنیت دریانوردی و مخدوش شدن اعتبار جهانی آنان را در پی داشته، ناشی از دو عامل اصلی است:
🔹
۱. فشار مستقیم دولت آمریکا به این مؤسسات به منظور جلوگیری از بازتاب خبری منفی که می‌تواند منجر به جهش قیمت نفت در بازارهای جهانی شود.
🔹
۲. ناتوانی ارتش آمریکا در تأمین و برقراری امنیت در این آبراه حساس.
🔹
این تحولات در حالی رخ می‌دهد که تنگۀ باب‌المندب به‌عنوان یکی از گلوگاه‌های حیاتی انتقال انرژی، همواره زیر ذره‌بین امنیت بین‌المللی بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/436587" target="_blank">📅 10:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67eeb2d82d.mp4?token=I4m7lqOvc0H7L3zRTp-aDkrybY3Wq1iDHJ_EI70nau3-K0HsUK1JJaLEVzAaDBW2JqZpZpaEhH3ARtiZp5qFzqGVDXrerOMD1SEGSyT7p9kzjVpwBTLHMH-wxFU8NBlBxpXp6qx7d4C-_A7KsNbLZCVXWhFJoxXQEztVAFjp9P_mgi08TYdef5cEr0VPYDQTtS0Nq_RqPMxgBAeMCWHephoRbPSHwADinqEXf4pMt2taGxJ7o9ab45EmysCXvWGTOaQRh94RKMaecq36C_AwHOd6M34ApGrMkBnKk4bW7nTA-dnZQHsyNDTl3e5Wipz3iVkFNit2K8H6MUT0W2AC7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67eeb2d82d.mp4?token=I4m7lqOvc0H7L3zRTp-aDkrybY3Wq1iDHJ_EI70nau3-K0HsUK1JJaLEVzAaDBW2JqZpZpaEhH3ARtiZp5qFzqGVDXrerOMD1SEGSyT7p9kzjVpwBTLHMH-wxFU8NBlBxpXp6qx7d4C-_A7KsNbLZCVXWhFJoxXQEztVAFjp9P_mgi08TYdef5cEr0VPYDQTtS0Nq_RqPMxgBAeMCWHephoRbPSHwADinqEXf4pMt2taGxJ7o9ab45EmysCXvWGTOaQRh94RKMaecq36C_AwHOd6M34ApGrMkBnKk4bW7nTA-dnZQHsyNDTl3e5Wipz3iVkFNit2K8H6MUT0W2AC7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدمت ارگ کریمخان‌زند برای آمریکا زیادی سنگین است!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/436586" target="_blank">📅 10:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دستگیری ۲ عنصر نفوذی در تهران در پوشش خبرنگار
🔹
فرماندهی انتظامی تهران: ماموران پلیس اطلاعات فاتب موفق به شناسایی و دستگیری ۲ عنصر نفوذی شدند که در غرب و شمال تهران فعالیت می‌کردند و خود را در پوشش خبرنگار معرفی می‌کردند.
🔹
این افراد با سوءاستفاده از پوشش رسانه‌ای، اقدام به جمع‌آوری و ارسال اطلاعات طبقه‌بندی‌شده مرتبط با مراکز حیاتی و حساس نظامی و اطلاعاتی کشور به شبکه‌های معاند نظام می‌کردند.
🔹
تحقیقات اولیه نشان می‌دهد کانال ارتباطی امن این شبکه با اتاق عملیات خارج از کشور، از طریق اینترنت ماهواره‌ای و با بهره‌گیری از تجهیزات استارلینک برقرار بوده است. دستگاه گیرنده استارلینک این شبکه نیز در جریان عملیات کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/436585" target="_blank">📅 10:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtL9rPLPl_FozwPh1b7AUEZ4-DJuhA9fPgEDuUJl65w1DF4W3kSLmQwkm3cuVtoT2ETPmpI5cTM0Jwrr541lJadTfzTwYt3QNivDmcKTcb6a6MNoSS0VmRUS8zKjQgrHYDpOi4Sk-wF71yJA4V2d8PmqjUhx2wK4C7Y9mGFClCqrLqKQCksyhSdwldKg9avrBME9wQh5NKbZxaI3y3D8vzwsnhEB8OtkIu2oyAnBWne9vZh5ziT8BuQO0UJuqfoS__tD8hlE7F5pvL2y3ssSDZDLrDg5KPbhs5RIKSHeeMzeU-aG51kWOykCaAkU7exNzhQu3AsNYK1Nx2sp5-IHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تولیت آستان قدس رضوی: قوه‌‌قضائیه باید با قاطعیت وارد میدان شود و علاوه بر برخورد، نام محتکران و اخلالگران را علنی اعلام کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/436584" target="_blank">📅 09:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcca367ade.mp4?token=Z6zwInjcoKeDc9IOzDtCL3YY1-hqacnw22if14XbPGYQJQ208MPk0M5x37YlVOocsP9umbfu18ICXdAuHPOgAbLi1phm8tqhQax9kFn2PipDq3Vh2TS9uIW0YrvqdhYk-qVVGv_qcAsNY1IpkT3hmJIm-zPEqONipz8P9sH3xPDoV2dBuQIevqgZ7z7aVqvr8LdbsvOLW58BemRBJo-ZAdKLiUyTGQpnvz3Kw_HCJQ0fn2Lx__Gg3J-0BsE0VjftUX3cywBPCQGljuLb4KtPIOstYAgEnQpvBbIgsfWl_0k7wS8T8vqBD9jJMASpjoICTVSKnYy5DNgIVmceNzTyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcca367ade.mp4?token=Z6zwInjcoKeDc9IOzDtCL3YY1-hqacnw22if14XbPGYQJQ208MPk0M5x37YlVOocsP9umbfu18ICXdAuHPOgAbLi1phm8tqhQax9kFn2PipDq3Vh2TS9uIW0YrvqdhYk-qVVGv_qcAsNY1IpkT3hmJIm-zPEqONipz8P9sH3xPDoV2dBuQIevqgZ7z7aVqvr8LdbsvOLW58BemRBJo-ZAdKLiUyTGQpnvz3Kw_HCJQ0fn2Lx__Gg3J-0BsE0VjftUX3cywBPCQGljuLb4KtPIOstYAgEnQpvBbIgsfWl_0k7wS8T8vqBD9jJMASpjoICTVSKnYy5DNgIVmceNzTyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مهدی رسولی از «بزن که خوب میزنی
»
@Farsna</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/436583" target="_blank">📅 09:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436576">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nr2BnBRE69bT4njNLjXNY-RUWv9URBBgi7QWFVmIlBuMx6i4e4HjhbP9PpsbxcEjcc7XJbe3LD5rpDf8OtAuEDR4fcKoJRt6wHSRaf4davIQrTzgLupIVrYwvKz8VOmSpWkZsm5D6TXbIfcRgpSneG_nmmPl2K5KsOzWpSetFxuzxcm9CUZKTKBMZqfPanZf87E11v1CDPzTKEOFNPUM5xI-Tx_5dP5w3x-LVfQW-22bgWoQ4i_8-FczrS2OA81mQc-y3B9VkGyJ8NDViH2SDVkflQ7XR1EbExRNd7pDhH86Dv-BLEwKdz2iAAL-lXkSujrhKuv53fJfs4mM6ivI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-3DadDNHmDUVT5VXoQhQNI6xgoa8tWwj_SNGF45sdWH0gYJxpTURm3bX702qJXG_uaPDCRqSawvO0Wy5_dK-8Oeekcd_thHfl0DDXJaBP3vwbT5pTri9Uix-ECXadCNZnEZI4jN06Bt_kZibzOx2Goww6eWSfAUmACVOvNjwvrAbvyvu1y864FpIrZnK1KXLtUehX5t_DfVaneRcrDlys0JUpqjqFpleh5SzcJtbl8hQyDgUDTeRdu2mFlXmj-gl9MOXM2T4BK6Gy-rh0porHBlouv0-SE7hQDYLVLRXP-YakFEFs4n0daBN4ZBMaPItAkzU0XxFU7lgw9ePGtNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCvdE65_dRTL4NN-d6MnqyAXDMRbWPcujV_YB1uXBdq8b6-Va66Glp16h0iarBx0EoNitu1Tx8d7KLiCbZlDdBU6bvHlFP5suscd2VWvAc1DzT0kmeux6HbLMag1ebb1AN1u57RWqU-TFa2D3oAr6wkQnXvP2kmAUtHV9Ag18kDVxJjf3_7hYPM_fhnmVdPXOE8I3SYnwejnr1dyaM7Vuu0E-LEpGyzGYRY_dWoQ8JtiGymr5sP_ProAl35O7ZizzfPxghvaktcSMRbHTpgLrt8M1q5xqG2mZuDIY6z315jsdqpNmYECeVNWXuwdj-Cx1vFHFZkTYWzvSubLG07mpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6dyDserFdO4WbTLp32ZFAhUcWNGOFwoK37HLqbVwy_TZ-fWIyvFo6iZIQkSnVS5EHyvoUkI1xAra-lO7IEiIzClVMPLknknZfTuWpvtPB9jruP7v_lgzVHppgLI1EvKLDwEhK7iVu6qXho9uYAYhARtBxa-h3pi17pzK6hnmyxQEUMy2_4w__VNXgk3Jz4po0wP4OQBiVsOxPzNeuTs5byW0u9yvAy4RUtjGWRFbM4fG4wKihER6FHMm9_SZIDddtgqh_fU4XIaqcPVC3_sPx1koe9wOJbhxeT7H7TD9t5-AfBrs_4rCSpUJLfGFSOlJh99_mD5VPGtFGe-Z7Wkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSS7WqcSnEE_LJHLO2S_JFvm44dmjuABZde3Z_XKJ-5TZ6XuL1WuXaiSZUsCFFbKug68Tva0I9HX0OoX4yBFY4cWsfgVBG5i39wFmsgZc90EE_o_DUsISTPx_UkNAPms8aJanEl-H4Wz5EKLMWUSbfuATLZhmPEzNfm1Uft1X5NhmPFSu34dGqnc5-hywrQK8mu6Kv4zpkK5c4Fjtt2lft2IQDRPOJq55FHFwsFa4hqlnfgIth2vOhgGqU7HOBq7boD0MvxZ96S0iJe9MLphpDanw62csuh_MHN8rGe-Cmq4_tll8zgBlPGBuOQWFJPl-0YQUJMI7hsh9txydl7prA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4e0aJcNj0OAd7iCBheX7gbIMgPSaJS7gWYD1kx1Ymp-JWdu1mxnSi6hINfYRRsXnU2y9WsPrp2-44czZSabYjJ5U6QbBoYoHJjSLWVoY1EWi-P3PgVhwgWurQH52UUe61NgrJ40tLu3SVnJzAYgOKADpdl3Zjiu_VuZR2eqcss-799N4E2Cix6-0GeblG7sZ3CF7zBfl2Goi_xidDWyrd6WOepU0q6cr3-Xxxscm1sahuKe3Tn-SDYOYMdUDfYTbEnP-ohiZzREKFtrBYvtS3yrzrDGqsfr6QTfkHBKAdD-5mqsV7ovRputQYh3UTtan1QBJKzUS1-Pg9TDGav8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j48DnKrx5A1ro4OZMXAvCfj8_4wVBcjZQjVsiQbAN_4_2GRuESHNxmYdYcurgJ6NC98l670UXLjy6E6PmsTKvhl2kNT073HxGR66cF5ouFed5XrAu-Jo8IDvYUq_45puxNNrjiMw9f_mMwnCDMBTFns3I-s7lxq402FgYBpf8zNRxkzwbNUazoryTQ-tn928cCwhPV6L2VUOH1j186LPp6WIIHe3hz2TtNrlbn6F0Za7fumg92bBziSxR7NPHXAF5IU30iNEGtH8rPaXSq1yZETwIwAIWSq1Rfy--_AB5fOnCo-VDC_eClTpwVl3wdd31xMh06tK9fMvAp_ACNQqEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنوارۀ هلهلۀ فرشته‌ها در قم
🔹
هم‌زمان با سالروز پیوند آسمانی حضرت زهرا (س) و حضرت علی (ع) هجدهمین جشنوارۀ هلهلۀ فرشته‌ها با حضور اقشار مختلف مردم در جوار امام‌زاده موسی مبرقع برگزار شد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/436576" target="_blank">📅 09:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436575">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfaRwRpxI8z_FGiVHkexiPnkVkbmvCxvmfUVJg0fRo-j_xkhQ8cn7vk_28U8Qs9xozSQJB59C1h2VVslWlhLdG7Dc0b7WsHKChF4WHvxFU4LPRV6jFBYfi_P31DgXvU4_pr9nI-64kJbm3e_-badqAJKhfA4QDbT9iTeziwbDYpSgrz8sWlyi1LEdQ7dcoHLk9HxGfgkWCQl0Rv4T0SUyy7-MIy-B30CFGXyS__oxtrY8KGqrAFji4Wb1LCFmT3SXMp7ASDl4VSJ4UzZnxk3vPYyFafPXuSPi0_u3n1_4UdF-I5EG7Fz4ZNbcWdv6Z6jon1Z2H7gpBDqlEYj_D8C1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ۴۲ نماد بورسی فردا بسته خواهند ماند
🔹
معاون سازمان بورس: شرکت‌هایی که در جنگ آسیب دیده‌اند فردا نمادشان بسته خواهد بود.
🔹
در مجموع، حدود ۴۲ نماد اصلی بازار فردا بسته خواهند ماند که چیزی حدود ۳۵ تا ۳۶ درصد ارزش بازار را شامل می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/436575" target="_blank">📅 09:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436574">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dab78b3b3d.mp4?token=QiMfCC888WAkZh8g6fs9HapnSwrtZAyFAibmPZ12Xzb8LU60hyVvj9Wj8399kC25s5G5it1YQbEuKYkW4wY3MnAChwW6haUiso3XdGoQE1G6rw_OouPeLrAK0hbYx1d5-eu56HFsgk1DdIZRm1_yP-ahxp4yDegQnwZwZhl6zO5LeYvc4GAHY0mKadfwkt8SY-ZBHnkUFO9cHGNV0p2NXdm_I79Of2z1FjAitVyygVt8qnTXjAvyA5F2HOxkatJUJ8gk8-PvikwHakGbrS_1Qw7mVPGNw8g8KO6uq43-O8ucZgHcuLpI1uijjlGnBMud0z2YOa_LbgrvHXaS785zXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dab78b3b3d.mp4?token=QiMfCC888WAkZh8g6fs9HapnSwrtZAyFAibmPZ12Xzb8LU60hyVvj9Wj8399kC25s5G5it1YQbEuKYkW4wY3MnAChwW6haUiso3XdGoQE1G6rw_OouPeLrAK0hbYx1d5-eu56HFsgk1DdIZRm1_yP-ahxp4yDegQnwZwZhl6zO5LeYvc4GAHY0mKadfwkt8SY-ZBHnkUFO9cHGNV0p2NXdm_I79Of2z1FjAitVyygVt8qnTXjAvyA5F2HOxkatJUJ8gk8-PvikwHakGbrS_1Qw7mVPGNw8g8KO6uq43-O8ucZgHcuLpI1uijjlGnBMud0z2YOa_LbgrvHXaS785zXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این لباس‌ها برای چه کسانی است؟
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/436574" target="_blank">📅 08:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436567">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3IyF1oWZKufC2FQFwNZyEiPCTs1859QCgzjSkbDlBRfYlW1XGOCSABTc3DE9Epux-SeLX3fc47e3LMxa7to1I_PDt7YOrwDh7ePZDqZGq6YCjhK06nmrL0EDpETA1eDhIigACAIyimFQKAUo2Hf5j7q_s1j3ljKepE2ZLmgRrzrXCUTwP76SCLV5QlUMZKIj2jd3GiqfsepSgq0Rjda7D07JCQvJjs4gBw5FOegog9DMYOjzQcNK_ZRYhLGhkYzDjDCk-7EB_QhC9pscc-_sMfcqnh287NbVKNSk0NPxOq0P2QJVUCLHy9R9LLvMbQypg9wAqRs3YYJFkHzQ0ZB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDLphgTUMAYEb3STVYXzd18YHjRB-svAxM_XKN2_sjTNP3ymOT0rHJjVTE8CRvTx_VRskW8zOEM5qpLKECTxZox508MmTwjZiwIZ5-XCyxyw_2QPyClU4eo_o0hOo_zh59YlMeWU6CLIHjCGkDOxpuVM4N7DGiUdeVYA4qWWxzwL7lStTDU3JJBq4TbVVa4b8HDYJJ7GFNt531ht3Cef0W1RAasc6mR8eYnCAEJXhpM_cdPmHLamMYGhfEmmd48CeY7YpXMSLLgYRAeoWkYTOHr7X_VC5qh43c3aLbckaZm9oPg05aTRVi3aYA9JT4LO8SWPRG2J3ftEdAT2AdznbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slMZDUJIEagcJwuFWwzqHyUkoeIKNDYW2r41DY8cqg89-EG1Z9ynQXxtCogtgwcM5XX0bOoVzOqSCNtkez10zCabaTK8vrlanffJp0cQk0zhW27NuMIZWG5un_CtovfyLp8RjFgDVj_6UxGWbbvXWd5viKVCQ7d-swy25FJKN0-M4cYh4zOWDox5P8i2xjI6QiolGCf3W-IfWkBuBsHsoWcJAVGZ_yCPx3sNxCgGUgES9_4_RvMq3d9Q2EJYBnyiB5gu60uNQBO4SrzHYaJ3TWnoz5HPq2ivEwA7CEOdrGjv5vWHRKdLkx3LGg1UFRzsdTNJuCt1elOkNQ1PMN9n7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzi7PE9DwwYKIKUkchjWC_C3xQOxE8DtHPoSzoLGyW44Dlhl-FEwPXov2qBavq5RrMVXTdA4ehQdl7mTlc8WVQOofcK75XFHTAH6qlU3Q6nl6safQwV56sUTujqvi0u19_o5hdUC47atN2Xa3X9xstxC9lEqCwT1ivbjJReJ3ZkSLBOrS9G-aBbmt6ioRf3IMo0Mj_YQyZSc7RXGzKpWfOfN_HQdXEPkR5ZuYjqLCUoQP3gBg2D1WTfLRK4lSuvhwJXVbWiHEhajkyLVsba7eeRlOYl9OeEbtCprWLj6W3c3nqdZ5hvtYazdvWK5hVqTUlgZbWGby9ZNtw7z0hObIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CK6g4QGGw3W2pMMeLajAFcFeHnL3kLEI3tXRJQ0XLreVtlIY4i-Dr1Ss1gkAvNcvRsuknc-lMxb4ebB0PciojCFsr0cdUe1m99n1xOeNNInytSouaHnHb6bbPl39hhSUCSU6qeagyfLDZL3gnzDTQFzTRLj9Jz_tXKZrEHb6uAn_YjfnlprI590Z6TpucFILudUF4b_wS-0H_zhQzyIGEkPqlucmQuOFy_3r7QMPyHaZKh2iWbX9rV97F0ycl-vUyxGhKq8SklCV6JX-zXj_UaUWQ7_-kLi5WkxgSf8Ci1uzSgtabDEVLpzdUJzeDydmkiHxci-df2UrB2hWFouHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-nyR2eZSYa8swMeej1hEppXJV4KMp9QTmr2k9KkGRmGjKNuwdwF7Pz3sVa-sL0Pz8SWF7vAEZ-Crb9O3-I3WWkk1MizbiKE3zLGWFtSB8hJdJzgtGwPvaHGlDMxNHHYVVyyn0pSzCxZblm6uyAe1s0evgTjQ0lBOwZQAhyutiHzHe-KCsEVcvIDzknEawrhNe5pQr0MHHNoTc2rMtMapzxDvp2-4YSf937Jqhv5OGpv1NcnVimkbfeB701y0zoFW-tfmz-TFDa817ygFWxjEKzW7_2VOTFxl4l-FpGpPol7muwiV32HDA4oUsxzV5tbfNwsY46P7xVf7XeAMd2c5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGgO3x8tZdaXjO1DLOL_LyC-ZQa6BSfOYxGei_T6kGaY5HErZ4sSqCBZUX3dRJOkVO8UFixMT1AybKe92FVXk6CWgT1ftwanZgxgjx7XDaAAzjjNlkqR_X49NsuUkpSQOS4OQmfatY8OTfzOb1at4o7KPCJo0HHYM-5WTR_IX1DHb17-QcrcSQc_SN0Hmm4dJ8CNKcG6a54rA4vZmcc28wjvxtjWxKRVNpEp3ifjKj7VGGp4RZNZZ2aHv9BpfkGXcvYvNW0L8k5tEEf0s_RXhTlgDHOiz3irAtwMcIhulJQ5H3Xm-SYM-qWlYhAMZiL9TLpMIglrXlaU1HQ3itMLLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زوج‌های جان‌فدا
🔹
همزمان با سالگرد ازدواج حضرت علی(ع) و حضرت فاطمه(س) مراسم جشن ازدواج ۵۰۰ زوج‌ جان‌فدا عصر دوشنبه در میادین اصلی شهر تهران برپا شد.
🔹
از این تعداد، آیین ازدواج ۱۱۰ زوج در میدان امام حسین (ع) برگزار شد.
عکس:
صادق نیک‌گستر
@farsimages</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/436567" target="_blank">📅 08:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436566">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42603926e.mp4?token=YZFmmNMbgkFi1EkZan8YI6mpQkstW1x-qTqbrAb5lIfXEW1FuOjalqPSb05QSSloANrjVqZvZdlE1Ffk2O-hyqq1Vukiymh2jxzGCd5h7-gp6CC-JkNQHgmBAasx8Lpf_OZ6xFQuhFJXCVKL5uy4MGQwtCtBfAM5MJ7rbdV021KoX80QBuDV-Jww9jEZFYZ1BJ141qw1mItcyBNLguGoXLv_BYx1p0LW1aNwuK8I8wTOFLFTqPvXzz_6jpwAqUBytLMPwMh-zQo54eAjaX3ItfEMGnXdEIRUHmYD4ICodSqXEsQULBzgigsqLHAYqr1JkRZitagbssuoat1jRIZhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42603926e.mp4?token=YZFmmNMbgkFi1EkZan8YI6mpQkstW1x-qTqbrAb5lIfXEW1FuOjalqPSb05QSSloANrjVqZvZdlE1Ffk2O-hyqq1Vukiymh2jxzGCd5h7-gp6CC-JkNQHgmBAasx8Lpf_OZ6xFQuhFJXCVKL5uy4MGQwtCtBfAM5MJ7rbdV021KoX80QBuDV-Jww9jEZFYZ1BJ141qw1mItcyBNLguGoXLv_BYx1p0LW1aNwuK8I8wTOFLFTqPvXzz_6jpwAqUBytLMPwMh-zQo54eAjaX3ItfEMGnXdEIRUHmYD4ICodSqXEsQULBzgigsqLHAYqr1JkRZitagbssuoat1jRIZhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واحدهای صنعتی راکد که با پیگیری‌های رئیس‌جمهور شهید احیا شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436566" target="_blank">📅 08:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436565">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYgWuPoB1HIKV_L8gsh1as_EAxTbEdimaBqGjtKiefBsv5kBi_CBV_exh2bF_yjx91_MrLelt1UqDjQwHMS8W0gsYn76FceTLdTrNNcid_hixbv7hd_WIJcc7D4j_1nEQ_RaNLDLCxDG2QYrhMbbLqMTZjVZEWblA8RHkguKmGf_M6ie-5SL1D5KjULuO0fto2nd_aMPHJYwkz4LGnD5IRgAZoAYgYCFdgbcJAoO6jnYS5Lpso7NGGcBhL2PJTH8TFlthz1focP1VPChrlJW5LiddkqN1775ce3b1_uU_DxVPH5mcwLjmQ1s5JeAgQ2slNOpxT63z8Xox3FQ43iopQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عشایر کشوردوست
🔹
بیعت اقوام و عشایر ایران زمین با فرماندهٔ معظم کل قوا در سالروز بیعت تاریخی اقوام و عشایر کشور با بنیانگذار نظام مقدس جمهوری اسلامی ایران.
🔸
سه‌شنبه ۲۹ اردیبهشت، ساعت ۱۸
🔸
تهران، خیابان جمهوری، خیابان کشور دوست
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/436565" target="_blank">📅 08:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6406a66fd.mp4?token=XVhJk65FzZhHpne60fRaAgftPtvEUMn492tWs8urTVvW1yX90AbJueTG3rQJKyWpgqPsqbDnlITlACNNzpKFC3iN6DisFJlShSw6pFl9Xt9McbYuPDSN3J8l-pZxyAJBqqwWwyk5XEo5nTrfBel8Svy642T3GAQuOwf853feT4sVuW9YRSsW3g-W1U_gvVH95BnR0b5a04fsN48FG-uwav9YNKblJ2FpCuOXjunXHkDuZXBlHgwlNKfYkEYgpahuoxqZWKv1POnEtFqYYvVrM8fqCxvzQhXFGkJfy21Up6Sf3GBY_my3m5Kaixce2_WAE3uFhuXVl2TjeA5W5iUyCoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6406a66fd.mp4?token=XVhJk65FzZhHpne60fRaAgftPtvEUMn492tWs8urTVvW1yX90AbJueTG3rQJKyWpgqPsqbDnlITlACNNzpKFC3iN6DisFJlShSw6pFl9Xt9McbYuPDSN3J8l-pZxyAJBqqwWwyk5XEo5nTrfBel8Svy642T3GAQuOwf853feT4sVuW9YRSsW3g-W1U_gvVH95BnR0b5a04fsN48FG-uwav9YNKblJ2FpCuOXjunXHkDuZXBlHgwlNKfYkEYgpahuoxqZWKv1POnEtFqYYvVrM8fqCxvzQhXFGkJfy21Up6Sf3GBY_my3m5Kaixce2_WAE3uFhuXVl2TjeA5W5iUyCoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلجی: رهبر شهید انقلاب با بیش از ۱۰۰ ویژگی، شهید رئیسی را توصیف کردند
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/436564" target="_blank">📅 08:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPG45huRMzrYtnJ0T2RHyPH4XtgyF5xc6nHnA76HQfNwD2WoA-OliEQIR23BKHc1tpPAx5RNsj2D_vbk7e1t8hVQr7ZuvxuoTQaMiSs77PtZhyFreN5r5m9eFCYB1WZXXixTt2u0wkCU-kch5VC0chrvBTKGtguSywtCp5edXiCalWTfvWDQ5P9ZWEtrjVBKxdVWH6OHPxcpXCDXut2ZJ_J_LZ5nwLBOpKx9xJmTihY_OOX6C_FK9GTAZzHYuVmrV23iFDXrg11UbsNWrGfw-xnDXbpalmFnqu-8lmGWGNoF6XzC3TpdkVrZbSguFgK9kkKMmBV9z1X0RWIspq894A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنبد طلایی آمریکا؛ ۷۸۰۰ ماهواره برای رهگیری تنها ۱۰ موشک
🔹
مطالعه‌ای از دفتر بودجۀ کنگرۀ آمریکا نشان می‌دهد، آمریکا برای رهگیری یک حملۀ محدود شامل ۱۰ موشک به‌طور همزمان، به استقرار سامانه‌ای متشکل از ۷۸۰۰ ماهواره با هزینه‌ای بالغ بر ۷۴۳ میلیارد دلار در طول ۲۰ سال نیاز خواهد داشت.
🔹
این ماهواره‌ها بخشی از لایه فضایی سامانۀ پدافند هوایی پیشنهادی «گنبد طلایی» را تشکیل می‌دهند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/436563" target="_blank">📅 08:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIfFahm1x0joMUcQY_Difv7Sj7G_ra6s9kFxaRpGACnqJa2BBlsOPwFmf0iI_j9RlCs_tMLKW4K6qIIM4wiOCzBhEH1SZi6NO-KfOdgTIiHOHwzgbX6-O4uj7kMwwSSa8stUdtOvnj4j1Qby0FkyyKhcfpKgh0BVk-UbFkP1iwlTxlEUyBGUolPYIjj6NobcnN_La5SGFIFSfRbU6uNgHJN4Mdmy29J_5NowPWFEB1vMJCN8UXxZqcMZweePfSkPPUOiuJxO0KTPoX_kI0hC3q2TE9iDTwF9gBl2NcE60xEgWmOMO9uQ_XAdi636QwOny2a2Fc6XBU3EOzfFVmjbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنفس قابل‌ قبول هوا در پایتخت
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین کیفیت هوای پایتخت هم‌اکنون با عدد ۸۰ در شرایط «قابل‌ قبول» قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/436562" target="_blank">📅 08:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K48NFQn96hMyF4Xhw_o3r049VOsStWX6NqQRfm3dmx3maAAGs_SzTkr-w6DjFcZQo1DuZGbB_nPEAhwD9_appdMMg3JNEJB8kXYFcwuLus2Jcyt2Po6pAxPkmdrRZvxjpYTtgaSJ2gKBxWgYHYnOl8x8mdQRy_Qkmn53dcCPHRsGlDJVtHyCPb4fUwrnXxw2I3yA4kOOYgX6uxhJ8n6M4227GnDIoJV4VA5s9vBtFHSuvOcfXKgdfVhEUmk1ecdqymZiFDmoE5jBtUhCrJyOABlDWf5w6f2jZGXOVD5H_Y1sSk3_NN5_i_ipk_UNm0dR_yi2mUEKDlnQb7TWUR64Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت پدافندی ایران، ترامپ را وادار به عقب‌نشینی کرد
🔹
روزنامۀ آمریکایی نیویورک‌تایمز گزارش کرد، پنتاگون هشدار داده که ایران با بازسازی پدافند هوایی خود به توانایی «ردگیری عملیات هوایی» آمریکا دست یافته و ترامپ را واداشت موج تازۀ حملات علیه تهران را متوقف کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/436561" target="_blank">📅 07:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77cdee184.mp4?token=uNEerdjlzEq0BIChCXXVBhRyaQx0Dfn9myMggm-I3n5p6Jz-VjggdmfykjFE9t02GHpZKn1kM-OM1ypNdVJ3UqgeZjkOl_HiOt7oYjipgYe1pdmgtlQD2cjmuQsrTJkME9UbFRshDNaMawteuRSi49kOfN4DicWLsXb77BBFGa6eAaeP06KHn523vtGrnhMm9KD52H_A2ceaIGYs8oVnK66GoFfpxTahBMKoaz1VYugMJOFkkk11cl73hz-rTngbzBgiiNIDtkkrzzCpqAGnWl8Rr9jMkVokvHYK3C_Q3QX8TjPm8-aNCxZR4IIBg7hy-Gc3j3C98EzMXNQY9kJ5PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77cdee184.mp4?token=uNEerdjlzEq0BIChCXXVBhRyaQx0Dfn9myMggm-I3n5p6Jz-VjggdmfykjFE9t02GHpZKn1kM-OM1ypNdVJ3UqgeZjkOl_HiOt7oYjipgYe1pdmgtlQD2cjmuQsrTJkME9UbFRshDNaMawteuRSi49kOfN4DicWLsXb77BBFGa6eAaeP06KHn523vtGrnhMm9KD52H_A2ceaIGYs8oVnK66GoFfpxTahBMKoaz1VYugMJOFkkk11cl73hz-rTngbzBgiiNIDtkkrzzCpqAGnWl8Rr9jMkVokvHYK3C_Q3QX8TjPm8-aNCxZR4IIBg7hy-Gc3j3C98EzMXNQY9kJ5PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گله قوچ اوریال در پارک ملی سالوک خراسان‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/436560" target="_blank">📅 07:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXUCnLi5gQvO_ypAoMjjUTrWcSE4gEzu796rhHQHNQ7uZbf52vZPEgcE3uukIjD_2t-BGHyolcvELgx3BbD2REbPdKr0t_i-BwjpRo4kLXmpLWwk0p-6HopkgyU-oV8LgUoDlTB30-WMjfS_Z4whavzhxyM3TwGEOG1Ukngxxzs6MjUqPOnyzI0dUX2JRFgVkHlAH6NqES7ckMDqEszuAgv8bU4xDmjw0iXvxDpxRgRE8hDANNZ9j-PvnWvDsUoqGX15pUNlL4KfGZhV8JTlDm84f8gAB8s-y_dKxkYmrUPc08SZNEu3SExj077c7vAXkegQLdTQWpUE_eoogEy4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFi_CntixHK93HSDPVfF26kpNyqFUjhrUbsRnnCTe252uR82Jy-o7R-ckVcXcCzAdo3GwhkYjpgg_opTPxaqjXmKKnXqA8XKL4HwgYPwqJHtFecCGdXeLMEKm-oFtnr9V29a4piusnDQv9NEwOFLM5RaEqp5Y1fIMYFTCURfKGqg51lyzjtlD6RO96RqY6l6ATF4W6XfMRLGvjmevuXFjFbaleI7LrekMHWqZ8EZo5k-jchE5frTbkcZJq9pL_hQj3Az-aQQ7YZIE7gIvElGS7GmOWkRaO0zQ-QdgsmLX7Va41DZX_vc3zN2BNuf42QyGfm3Uav17n1S_SzeCVmjbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6dcieadCtvKUVGagtMOZp24areI9sKOypXOQJORKkYLiX-fEPA-uxBk0cmttSJh0-sVmtaf9LSm7g3n1Ul0rdrXsVIkSALQ2e6JFH_KRIcu2rKufsWey58D37O0vXA62xAnsfnYh-cxKrZY6DYqBWabA7uRtQYwBvmA-CWcl7qL0VS7RDM-BQFUpR-PLxTnPJm66fJePEWWCIqQop5X8czRROXF4HzYx4bJzV8wH9NKSmMRQep3nO180WnMTFGB6xhAdhcoMBR542PJukDSaNXJKz1PgcMF0mRCN6NJZCPlPShaF5kYTgShwSS4Unk2C6axqeSIJPGksvYQ3rQ6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cH6lS5rkw5dWlHhc6BSPHRL2sU20gnxLwIHl95lOXpHYrVb-rt9tcolR0VdfY4Am8zIOFdaaGAtqv8owNwevVIAk9YQKPhuiC93dFCxfCAO8z0RUz3KmgVBK9ilhcTPgK-nERU4QdBQ2FfGe9XBtpE1yzHXDlbqIon6Qptvz7RWynYTw3jx-1OhgdOnIbTaDxu1MizcrtD0ZLCSk0Z4reHLDd0XgpA73B4Ud2WMOX5sOzhV3Uon2jnI6crYRaj1ZSDtxebiLrzhLPxpQDAIaCtlrIz7zkukXzHK8jHHocPlJwSEK17YR7fw-QCwSjqMHmF2o6kR7NavUUcPWljEoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EeuGU2wneBRy42-aYWZYsUG7E-gR-xco3eCJE5pY0ajODDeNxRfrDn__FQaSlP5PnLugPLPgG_q0u5VPbNCLTW0NO0diquDTzeAHXUCBhrmDO2mkun97O2ZfEKoswGU-1g8mi3sFOCyGz6WcuG55NHEPT50SfJBNk03GOhEncnuF7lSpXXOycGqA1rKA7eTeykgwGlcnr334QXD6NZFHiulg23ihOTuVeMlOYY-_bWQFALBKTl8asdrMuMqQbzAsoyu_9-YGTjsncqMbfkBiBFcMdenMryIHaT2GxqLqIZni0VRfw-Rmm7tlHPefORCVs-FqVpYq7UBRHg9yBf64Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUM9EbA3QITjjDtLwqJf-m-iVY03N5ZxjcdMSHLE6BbBhGal53DD2Eg94YrMYjSztk8DfB1Zeb-SodQTdXdYN_FYmd57A8Qr75S_G4BJKFaMw5cLrS3fW7qp5e7hrg8Mmx69ijCoCSKe4KAcb-tenVfkpjQGg8L0vpgy-XY_XwsdOhIkwHcL9kAPHy0C1LKxKj_y2jkvcMSj0VjSfWXBM87nQ5Lg7Qb2PrATPN2Z4TB3qBrMmeq22aWyji0mWZ4JLEBZyMU361XCPvTphsQO5FisAqXI4EuTSfhDsMn48ncmscdgccV9MTuDQ4M2RVhp-Z5jtQ41BEXAvri_ACry3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC7n4-AbPxAI3EQmR8CZ_0My7alpb742Ge3QSBLWmK8ihz1u-WZek6kVfJiEgqNr_Fq3QFiurGcskbHhmOe40nu_D7FAP00DynUzHFJXTa3KauRr25k-9VsUrGJLhBw8pgnxaVuTRVsriBzcNYU-OpTe2JjJjazVluZ-QTvpZNZtd5JL3m_xfi1N8YNeP5-3-ItagC7zLl66od14lZLSVGOiqOA265A6i872V3XI9Rw8WTJv5nnD8A85N5rWFB0lCyFh_tafydel0ASv3n3kkpt5oIal78Cdvay8k2ZIRq-YgGSTc-fte3zkW35FpgzoOQAw3cdmoPjtnuVUgmpTHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بیعت بختیاری‌ها با رهبر انقلاب در رواق کشوردوست
🔹
دوهزار نفر از عشایر غیور بختیاری‌ برای بیعت با رهبر انقلاب، برنو به دست در رواق کشوردوست تجمع کردند و شعار «دایه دایه وقت جنگ» سر دادند.
عکاس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/436553" target="_blank">📅 07:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRRVZg82BFvQ4LESHNKKu38_6puH9XblVJunWAb3xv_b5wMTFE_cvnScTBPRJqIoXBzXCX5uAXtcYrYi7CypIS9TqERZ0bvIhJYPa6pyw9WPli_fAVMUzyMVSxB04StCgndoloq5RmsWJkavCrnzDz6puq3uSmDEI7dyDPMwIVhFUeUP4vJOhLXtsHr7nsfHjbDMFC3bRjgh403L6POw4VwwhVGdF06OmKA84NT6a3WIQOJTti9gLaYPf_X5_VGajPoJohZiPZqAgthly8MNG5Yoh3ajbnKcbR48WCeX9iItShxaC09BTJ-z4bUOegdCbWXcLtkjF83qNRi2IK2hYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط ثبت‌نام کلاس اولی‌ها در مدارس
🔹
وزیر آموزش‌وپرورش اعلام کرد، «هیچ دانش‌آموزی بدون سنجش سلامت وارد کلاس اول نمی‌شود» و این تنها شرط برای ورود به پایۀ اول دبستان است.
🔹
در سال تحصیلی جدید، نوآموزان متولد دوم مهر ۱۳۹۸ تا اول مهر ۱۳۹۹ می‌توانند در پایۀ اول دبستان ثبت‌نام کنند و
هیچ الزامی به ارائۀ گواهی پیش‌دبستان برای نام‌نویسی وجود ندارد.
🔹
نوبت‌گیری سنجش نوآموزان نیز تا پایان اردیبهشت از طریق
سامانۀ «سیرت۲»
انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/436552" target="_blank">📅 07:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436545">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cV-htBxLnJNn5VRQwFJXxBLG6bm5nPXskT4wXbD_lvgp3yYVti6ZHyJYezAfpjQeCcDzmyydXXEHtYvQsklzgW7njPSc394Lrn7RjCFoTnfnn1_SIGu4wb31sjcJw6Y9GcDiv6ak4faLDYG4NLWnu-7wOFa8Q-QYKY3DLCxNlF1g3goat3thcxYpAfBU2esRC9MgYBRwTMVBM8Br57Uf-v5D6SwfYxwCn6VtE3rbaScpbvjq9oYSSR1z154AArjg_OBfv7zHJFbYHFulgrJZNMzszY1mlfonyujnq2EnYUSKWvOKYjoFmXQP3sYTIMuuCkuQ1XI9ZHvShzCNUrdaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhXnQqST7dbJ4a83u6lLAcOLE_TafwNKS1580JDzbbrbQ85goG3lpRnWYJ2sqgQb9WRbiV05CF56p9y344w9oPM50T99vGjuG3r9OrAYha8MQM68cMUmI7F7jJB6HmlkIPRXmdugHwqarCaxyrMknopZGYLmfpmFtIu7mdpsUr8sMk3-SD_W7GUhZGIoldTqt_aYeXI_oK_69xFwMKj-LSY9yflhKIRBgszOGZv0-7R4XkP6jWZiAroT051DZcv3gtHeS8HpBKV7VGh4xseDIR2c8Qapqifrc4i1evddRtN_amo2lXNB0MDUGdk5NB68d4lydwcRjGjDU8oV4ZF76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pECgPSQn7pKZChvYUgzW7TQ124MWsX5EoiBTJBKJPvCbJSeUTRQ30sy4-SiQmUumYFzPzPGkOyVLwVxxwMqcy0wJiCYbGEHZi-QtGsRgPHLXDpzurGC5udTSrLWPEI6NW5tr6DuZDd69zsuKhogTlBUniQJec2ixvLuY6PRAwzN8SQ_rWUdokz9-PZl75gF5X-EC44XQxiRga6KGjrJsLBrUUpjceNS7PlM8-zk8qoojEjuU1BMagmJh-YuQenil1RR5kS8w2IeH637ANH9JyCd_R03c1pTxKzYOghGcJShluYCU4Elaor7jnDMHQli0qdxpt-h2CLdbPrmzarhXhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksn3bzGVwf6anGrU9btUzibLL1LjvcKZEJX07_tbiO7niyoBxkFRd98soy4_cN70xfTym-rBekbFXY89pvHLKnyqjq6KUfBK5-Pqgsm_8UugXkNW0uUO4RwNmc5wtkcI69QQhw-wNaBmE0HYzIDXq0bgX7KjO_7hJQxPwa_CUGtxIcy8eRjROmB_19f2azsPL58oxC-kFOzO9OO6Fk2gkZPxxcv7vjMnLM-9gKgT7Ug5s7QROsZTZE8J1sM1VYl47qyTNTxNJo0BiPkVytUYcKGzNRmiylHU13COPeQ22lJkZxu83Y1BY55xvN9o6KTmNO3CnrHRlB8YavB9CgNS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMYMSKGsBlTG51M3JCnTdRBmmoP5LGaZeL-xhnqoPsf_eC48ZiXXOsj5pqkk3Du7qOVtWhgwzmvxoVTUh02PVpvLu7BDS0wkZ-sSDgTr-gpipdiCa9FNCeNe8U_rgBaVEtKTTkuFLi-a1HVyo1vxXix1MXCKohveEZvDs5CwCkOOUKNHheSaMUzs-4OrLsVRTS_t9zmMHVJPf5qSwslAIsjicIwHWpMSXxubPfjnNejfpCrVPH_zH7tHMcqonyXEuUFJl8CWU6AKFIRYKIbkxCP0WnyhIJr1JjxxOObL8B0GeqDuUirJ0SK_oSTdxV0ml_hwcGNCmrA55yVZXSk67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXi7A0u0ORuNtJXz4rQaZsrh8C5YtlFj0VI_fJSSHWlsf38-kpou2yqQzCVT8WVQzVtGZogT2w3nTuBsClDVgZte-T0RnfIJyMOKFMBlTxDxfRdc__zILSTTOFxyWbubTcJxtEbxemSGVcjA7Kbn7cgI2G_zBoIRHUiwtJNYuP2BwWtfSjOXDUiju677DSkoDdvfZbclf0TOsmy1jglq4KpymL5GNWYqw5puMcuJXX8o10AwzkR0q0BiCvPNNTN9Abxa0vP0FjDdC7HnLWd_gqmtcyMZff38t2dvbZdr-lYveXki8SRGUYMPioUMpHxJGELjksoEu7w0E832LPLuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olQ26UGpN1tCfFd1UXcj1vHUL14qddpGfvCegBibRTSBTZVl_z470sf7WNvr-AZGxKeXUK3w-F-6ULDimfNoZXpR0Nldyr6peZmWXCiN7VFlLATCurYowjTWwBiGhB1_wOyX3r7Icc8Q_iRFMkGQLoGpuIWY25Z6xBfgyh5e9_4Hl_OW9GflvEM69qxuM-kYg63M0Ylq6npekYPpXcnTFD41WJMhCdAuD16UMzpQK3f3iJ1h7QdR712d5Yx5vMyfFoKDCayRYoFM_ZcjBF3ny-bxZrJIgf_3MN2BBqEig01NKaNLJtHrASZm75rXWMs-4SN7LykeQlUIqKVzJF1Y5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عروس‌ودامادهای جان‌فدای سمنانی هم مراسم عقدشان را در میدانِ خیابان گرفتند
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/436545" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436544">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy3vCaQkISy6GiBoXb1H2pqjEp_zwR6_F_0U9f_6M-T00gUjnYBwjuVxW2dY4QrDaiHI6ayX13ouC7i1n_QnaM-ItjFG_mpgNPjfe583HOxDxPJ1uT-GR5ASRY62ypYqewd4t2dqkGzKOs0uoviAhK40HCy3A2GBD5Bj-s2rsePgPFBoxM6liw3brbT2iBVU9arEpDzQgV3NO4kQgwkVeNKpYJ1x3bXrZLRaU0UrTLh4oJlBT-7mDeWRKTSFzR8xH7aJPtZeUJTnB00lyHCnR1vxPVWGRYA6qBHZgXBNAMMRXxaGhd_5NqQrTDQSqm-NuKT0OxY1IN0DclBZaLDmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر دست اسرائیل را از دریای سرخ کوتاه کرد
🔹
طرح اسرائیل برای تسلط بر دریای سرخ با کریدور زمینی مصر نقش بر آب شد. مصر با همکاری اریتره، مسیر لجستیکی از مدیترانه به شرق آفریقا ایجاد کرد و نفوذ تل‌آویو در منطقه را شکست.
🔹
این پروژه که بنادر اسکندریه و سوئز را از طریق خاک سودان به بنادر اریتره متصل می‌سازد، عملاً حلقۀ محاصرۀ اقتصادی و لجستیکی اسرائیل در شرق آفریقا را تکمیل کرده و طرح‌های تل‌آویو برای تسلط بر کریدورهای تجاری دریای سرخ را برای همیشه خنثی می‌کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/436544" target="_blank">📅 05:54 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
