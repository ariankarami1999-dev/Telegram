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
<img src="https://cdn4.telesco.pe/file/ZwU5FRkFVVi4W3--nE4ASkrpBRCLK1i59lx9CxsYfdtCr-wEH1ajyW8R6tRxn3j7qiWBjhmBN_w5WmtFmQRyD6rqh3G6ct4JO-RdmKp842Bbr3bBGGNkTwJu5I-QxL--vbdy9qrMrf-288F6hxFf1sslkJICoQHHai72qGQWRDLdlADFtmkmxeTVcqKh2-7W8yQv_qSAUC9vJk3G5BwizMsNbMW9t2q6SHvJzTHKXSNYItYorUc7Aczh5yyeqUPDbDM66P-VGgV_G6ZItsdXWqBrKC4v0KvXKBmVJdMiWRf2f0wvVgP52lyqsjkvRtg0HgA5IhnVmkq0Ryj55sMrrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 60.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 19:09:59</div>
<hr>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hlKyrFAYSZTRMdoOHh4Dkf3wtTjgKKpLwPURpKIYNMC0JPEGwH4afqDOa1sevFYTVB7VTqgZ1E9cjleG7wTAFaRPEvKkmSp6vMvaLKsreRznwuckG1t9OeMo4Yp4vxnoZ6KP08GH1AHSqqIlti0J7yxH1porPc-6CVyFLce5es4tUoO-_sAmFLeidFxWl3h13eTLWLM4H6rFPT3NMWDdEYe6WIC84eWrTtWTCgiR7syjwmzlqmKthbOZiWYToc-KBGVsg9YKlWHZMVSUB32aKRz9jWt2sntQ-7p2CHAU4wLHUyTf0vOjpLXBOPsOQJjq8KIHJwOqnyoscwqGuupklA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hlKyrFAYSZTRMdoOHh4Dkf3wtTjgKKpLwPURpKIYNMC0JPEGwH4afqDOa1sevFYTVB7VTqgZ1E9cjleG7wTAFaRPEvKkmSp6vMvaLKsreRznwuckG1t9OeMo4Yp4vxnoZ6KP08GH1AHSqqIlti0J7yxH1porPc-6CVyFLce5es4tUoO-_sAmFLeidFxWl3h13eTLWLM4H6rFPT3NMWDdEYe6WIC84eWrTtWTCgiR7syjwmzlqmKthbOZiWYToc-KBGVsg9YKlWHZMVSUB32aKRz9jWt2sntQ-7p2CHAU4wLHUyTf0vOjpLXBOPsOQJjq8KIHJwOqnyoscwqGuupklA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=IxRJGqLc_vQw6e7S-LPtjkqaLcmbpNSWVsXEfbZfjVOEQ-VB90EhkfUzOl1dwGG6dyLYJ55465VeaoiJ_KZgvGCn-Str1Y8JZzFhNUVfOwRBSiTl9qBpzau-RMqBwbqowxu9Ey8WY2kGUT0MGuMWgFo6HJTQ2Y2dvZ6iFe7VeShkfPXGlaGvBkuC31hDH9HFIdQUSKuNXZGVM2LmMxihnCI49S_pBt0OlCT_1ze2SybmE5-UokWeid4oepcta-591R0GnKqBPm2cRmaa2anYiT2JrrtoCUyAcTqy_NEDmqJAVuaIR0lqdiBevP6W6ku56Eh2RoF3b6ZDJnOnOWuuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=IxRJGqLc_vQw6e7S-LPtjkqaLcmbpNSWVsXEfbZfjVOEQ-VB90EhkfUzOl1dwGG6dyLYJ55465VeaoiJ_KZgvGCn-Str1Y8JZzFhNUVfOwRBSiTl9qBpzau-RMqBwbqowxu9Ey8WY2kGUT0MGuMWgFo6HJTQ2Y2dvZ6iFe7VeShkfPXGlaGvBkuC31hDH9HFIdQUSKuNXZGVM2LmMxihnCI49S_pBt0OlCT_1ze2SybmE5-UokWeid4oepcta-591R0GnKqBPm2cRmaa2anYiT2JrrtoCUyAcTqy_NEDmqJAVuaIR0lqdiBevP6W6ku56Eh2RoF3b6ZDJnOnOWuuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=drD1s5F1Pt3cpfOM_EaEM3l5ZCSOEULga4uuK2AWhf-AlrL5uF5S5cRtQEqumnM-OFXYQ5p1l29sPGG-3ktelA0aK06By1wPAuF3HH6okkncxYqGp_2Cn-QN_4jcBvH-HvBHgZ2uwcmS3V-pnXxzU2C0aU4aKwVM_2TLw0BplWtzZNAMbqGxiQQJSNHdRp0SFqNRkzup_WmBuJScSl81g4F0rn5n5nHA5R7VmrOvWV5roDSV-0ZNgZZ7c6E-jm0QgX-rr4-9ktHpwkY-iGiVyfYZucSoRpx2794cJ1Dz389wly5piiil9iDr25z4zMFflyOHccGqXsQbmVJ1Fw3Hlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=drD1s5F1Pt3cpfOM_EaEM3l5ZCSOEULga4uuK2AWhf-AlrL5uF5S5cRtQEqumnM-OFXYQ5p1l29sPGG-3ktelA0aK06By1wPAuF3HH6okkncxYqGp_2Cn-QN_4jcBvH-HvBHgZ2uwcmS3V-pnXxzU2C0aU4aKwVM_2TLw0BplWtzZNAMbqGxiQQJSNHdRp0SFqNRkzup_WmBuJScSl81g4F0rn5n5nHA5R7VmrOvWV5roDSV-0ZNgZZ7c6E-jm0QgX-rr4-9ktHpwkY-iGiVyfYZucSoRpx2794cJ1Dz389wly5piiil9iDr25z4zMFflyOHccGqXsQbmVJ1Fw3Hlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=LL_fa4Y8F85QurXQKBZ713Z_fzdKXXihwN_39OGJinohzhYsNt1iVWzVWJLSvYAzVzYVLBwFuhobSYjUjJMNa-5DVn8-u3xfCpneZ1ilm09qepQ0_2PtxK2nIL6bcS5YChQWZqK66UpTa6z6ZCC1sNazjkyBMFvs4jddWPqQUo9Ge4DHkTjuZR6F_MdS1lDJ6nRQehcKIQ9kDVk8XDKfueZpLmlYhSIa-ZcTDGiY9OX0Va4BCh6YYk05OmQ-0FeEtB2bYrpgTW-D2dZ1BWjUfXr4KM2h9hw1dA17SJbi21DyMR62dsw9vpEisisxHuAlM3dceyhd4RETReqHnH1L6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=LL_fa4Y8F85QurXQKBZ713Z_fzdKXXihwN_39OGJinohzhYsNt1iVWzVWJLSvYAzVzYVLBwFuhobSYjUjJMNa-5DVn8-u3xfCpneZ1ilm09qepQ0_2PtxK2nIL6bcS5YChQWZqK66UpTa6z6ZCC1sNazjkyBMFvs4jddWPqQUo9Ge4DHkTjuZR6F_MdS1lDJ6nRQehcKIQ9kDVk8XDKfueZpLmlYhSIa-ZcTDGiY9OX0Va4BCh6YYk05OmQ-0FeEtB2bYrpgTW-D2dZ1BWjUfXr4KM2h9hw1dA17SJbi21DyMR62dsw9vpEisisxHuAlM3dceyhd4RETReqHnH1L6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyFQgGlz8HAw9eu44AC_Qq50Q0uDcOoGNVSjSz-KsH0gm-c2e7ftlKIs6sodfhqv8F0z6PkK3Lmyi1Mn7uu3iaQp9tImrITccN2O1ladJDRKYLLT6yG91YlCuVwrhSODgXgCEDIn5scbXH15bYZb6ouix5XWzJYHdY5sIktY9xHDaFUgB45dCWioWHxx2BNkNtEmoqz0YBKO6BLL9SBQvYEvQXtVNHamCTDIAcpNqh840j18UagAxccU-YnqtLkavAGMh-7mxniUYjGQbDHfB9x9daMORHpchVOud4Fl-0G9Q1orEvfXLe64T_WDEZ4lIRVTAlM4u5g773OPI_3g_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKnhIUVuqDA_mDbCGoyrTig3YFn4A600EBLWLTvHywe9kqq-qUoXkqh_CC9HE85IO9mEcbSi1tHqKDSBHlJJfCPQcBxSEJHq_1M-L_xRJSKadnINslztPNh_QgGTkvgAlY9xyTvejMQRP7lkOcbby2sHoWrbg7bgP1_OJrh1Q4dKg4RyZMrn6MqRGuNRmKCerPkYn7606tmoqfnwCSmPpwAF2og9GShE0fYFQgBBgXDcKQGH7S7VSzy9jITVlAchZX9guusSCXcr5D6eEyOVMxqm07Bc3hXlKdozQ3nc62f8hpNxNQNg6l95Pv4M5BbljfMXjYpD4VHl2fFMoX1Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afOzIKfdS0N5C9Dny499HE5a9pi6qVHMFFqre8-nUq9ht7aGoASBfC-vJs0cfAFjCnxUAUTqMZXQl4FTJ14OFnOkt6NbeDad27SgI6JqgJYCi0NDgEq3kLbxzKaGSVaaFMABOFC2VzWynsleXWUQK2w-qaHHNeC06ZobidwVZspOZY6daahRnMoohhZ8IKBopv75GKn6bLzRpGSAvSVt68HblCYZn9-UBo4aD5J8Fkhi7RGpyp3HR7Gd6WeBxqynZ0IWpuQu9CCrHIE2j4o4AfQfsk32oGbNy5jiz6lIfcodVMsVvuZKh6mnlplfvscnlvsfXSAnVrrg5Imn8aGFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D93imfMbyCpfv1cRED8DpRFvgVyLnOdJdRVqED0mTnJWqdB7yaKf6Nmru-jsUIRcCub3Gv3m3v7hS7HX8dLjwjWno_myjxdiCYMcHHkym9wY6Onb3AZDJ-HS3lDz6z2P2vgp0BgYKcPSBF3M0COQqWrZ5E7xNz7Gk7u-N9UMxznQVzE1JC5tEArkcTcYGeSD18OowlsC99BbI-upHjCGvGfKkwsBJ_Qg1rQThhQLlJAs30tA9ue55dCcUMiJ-pDeqHivabTCCZbjT3kYrMjd4iYmAk1gslhho7KsQxyqtf9roB-w710ReC8D5IF3xBoxtPMrFsHRJ-ossPAEVKCiBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRukd7fKxB4Eixlben6BHJT07f0bd_Oe8Yy2FkAMKGBywbyBwofBb_ztMiYv4InrDx1UKm4weJzm0jHGyzk2Wj8PkgM-KKnrCPceOOzb_yIFJYa87fK0JlcoUgAxRd5erY72rbDPGmFo8SrQGH0EQ1zt7YY9k4gvfhoWO8PhYdZM47RWVpY6Y8o2WmD72FF3-n05KYpqckRQswYNI9Ix4DVD_yraZbhWgqIzXwMLxQtA7EO7m06yzfQJyL6wAIIDKx2-Tck32Z929HT7zkaijIof0paPc8N-IxDcK5cx6hp8Qgkq4bC_yX865XWVaixXguh3wKSPLAZ_KB55dGu7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rG7BeCGTLxqSFu8SSNtloXV8wgL3NR6Ti9IafUcSlf4ob3YzXeVhbZgdK2DBzn5XrJKSRHFdlCkSfzj6WLk-udVrpKN9I8gMEkNGzlE6B6-tfZOCXMzi3l9skh8fMK4OIY8p5nO4jXqJ6tQEPUfuIZgHMp4aUYcLMlXbIzxzF_pd0lZ-TDpoCsSuYw-DDlTS_A0TLnAshNMRgTJm8yz9k351UZXfhKt0OkLUVsburq4W0b5zsgyh2p9DIhx3TQ-F9AG_gYQlFuVfSFC08ZOkN5FufU1nK4UFjCMJ4F_7QjOnYQoTzk-N6gU0MIjgELlEbKRSo2SaysNuSeNOsNYDHF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rG7BeCGTLxqSFu8SSNtloXV8wgL3NR6Ti9IafUcSlf4ob3YzXeVhbZgdK2DBzn5XrJKSRHFdlCkSfzj6WLk-udVrpKN9I8gMEkNGzlE6B6-tfZOCXMzi3l9skh8fMK4OIY8p5nO4jXqJ6tQEPUfuIZgHMp4aUYcLMlXbIzxzF_pd0lZ-TDpoCsSuYw-DDlTS_A0TLnAshNMRgTJm8yz9k351UZXfhKt0OkLUVsburq4W0b5zsgyh2p9DIhx3TQ-F9AG_gYQlFuVfSFC08ZOkN5FufU1nK4UFjCMJ4F_7QjOnYQoTzk-N6gU0MIjgELlEbKRSo2SaysNuSeNOsNYDHF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=ORjIfJFkvYTn3rk1Hs0jVrtibWLdE1z7g1QfY2J04rKdL6b-Rmxc2gHFui-kZLH0yoWoEywfR51DXxtp28AbnUJZKjA_w8ep0oS4a1i_4-34MZsc0RV_-FHu7zj3Q0FjEzfjbYgRx-r-eRGOqsiQg4eIf3wM9anUz9vp9nRYDGAWeL1n8IjhLtDttoHgMmTaUw99eVkiwLpXmnywpUjpAc1rtlZT6RtZtJyBa2cNYkMqhjMeiKGL5GMXU2XSOdR87a44PHO3gHlzNDIZoZrfOCIgw4eMOLT5LQhKNQ7vYhDqGctWlehnF3RfXM3VH5ZhAeD35CDlrHP0O0BRXI7VrnmS9gFlYOJ4_sNQly1u5YGtC_YcRvTbTlnRlH6iXEdR6D-oDTytYK_dxQQhDeMU821amjEf5xTzdbgUBRaKXO9Fl6KPraLqKLaVeX0CIeGBZfi_vnCOQu0Zq5zxhTloGC34nF3FQ5ywFRyxWdbgnbZkQt7wPGoSB97e4tY9XyV4aN-AN6T44znXasJ_4-PUrqgb18EONscpEeZikWwZWl33bduTdMblak8WBqzXi903f4e3-0fLzTojSD0nJP50J6SnBZvu99jGc6R8QLWK8ISZxwaK3E04b6sCZrFJNCF-Vus3YGiN3KwzGl5PtYG7CesxlbWPh7Nkw2h9I7s9GqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=ORjIfJFkvYTn3rk1Hs0jVrtibWLdE1z7g1QfY2J04rKdL6b-Rmxc2gHFui-kZLH0yoWoEywfR51DXxtp28AbnUJZKjA_w8ep0oS4a1i_4-34MZsc0RV_-FHu7zj3Q0FjEzfjbYgRx-r-eRGOqsiQg4eIf3wM9anUz9vp9nRYDGAWeL1n8IjhLtDttoHgMmTaUw99eVkiwLpXmnywpUjpAc1rtlZT6RtZtJyBa2cNYkMqhjMeiKGL5GMXU2XSOdR87a44PHO3gHlzNDIZoZrfOCIgw4eMOLT5LQhKNQ7vYhDqGctWlehnF3RfXM3VH5ZhAeD35CDlrHP0O0BRXI7VrnmS9gFlYOJ4_sNQly1u5YGtC_YcRvTbTlnRlH6iXEdR6D-oDTytYK_dxQQhDeMU821amjEf5xTzdbgUBRaKXO9Fl6KPraLqKLaVeX0CIeGBZfi_vnCOQu0Zq5zxhTloGC34nF3FQ5ywFRyxWdbgnbZkQt7wPGoSB97e4tY9XyV4aN-AN6T44znXasJ_4-PUrqgb18EONscpEeZikWwZWl33bduTdMblak8WBqzXi903f4e3-0fLzTojSD0nJP50J6SnBZvu99jGc6R8QLWK8ISZxwaK3E04b6sCZrFJNCF-Vus3YGiN3KwzGl5PtYG7CesxlbWPh7Nkw2h9I7s9GqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9yNl5eHJfiT644Y-Qakno5K6sKBT6Njo8YZdx3fTcBJLexurVMbodtpUk0xdV2T0Kec24OYtGZRv0Q71VnjUklLEqZRfPBkF82JjMRKzrjIxGL6hc9CtEKg4qnnf-sD9zBAaqJzsI-IxMSQ6_rJ4r-SO-IiAVaBDWmtrAsl1PzoPVAedMPwcjIrcbjhdhHexe4mFkGnogl5y6M4v7mZ5DoP0UbGi3zsrOjfAJGtBWs2v2V1VPJBlEQbnSdKj9xdyagkV5HhKzxiUTk_RZvHOkaUig24--1ulqlIX2oHDWALw3gVEfepf7gMPVuoZKbgG8FBCbmkrGrIzgpi_9sirA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caN42ObWUGX__wQwyMdzy-7YLo2UNKBvpylsPLgG3swayPZ5iDiuJWqUlMk_FBJktiYRS7vgew1hW_P8f1Xq7M6C45gLoUqlwScPLColclwd1nVtDn389Bh13D_QtWYlNjXBUmGe1V8s68P3yXtBUhfWdqMeRuKbRqOSOe2CmPdMVpXidDbond7Bmxd1-VO5KQEhrypRvGiBgg04DJ9ihNQrVtUFtmkNOIqh6Jy3Z9AjFrdDn_6bAeXiql7VtOZIdAVvQYGNBSc5UCWIzlqczhdER8ThPf70fs4Yz3ULCtrhEpOfEfehJ52tM8QzU0qpmZBID-u4mE6o7nDOkoMfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkFf-1RSat3Aos1sIv5gvthy7A4IB42aMLnzb53vCRY8N5KhrGO1JpGa8jx7RFoKK2-wFp8Ket5mV_EV0S5nmEL9g2gvv4yyCjkiXGWEDo_4Op_c0MOSiqbHaqtzzRIiB7CD6yDltsq4bXD-p3GgGWQtUtLarP7vr-X1sQGZ4XsNd5kvs8cLzbNMWanz4nAd7I9QplW4tnKLPzcvT0yVvQV_WKuLJg9BJK8Q5QQ83sOQMsTwZFCnAj6b5J-926QzoBhYCLoXMRmqTsf9pxRPgS-1FYLKzpUV_3Zdw3kZBV26PXe5LwNUsh5MCPDTy5EFWKCkBNBcfyNduTHvZo7epQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxYyRc35VTHztp5AR6zYloymOBMLIOo1hFDvmwaolZL_8IWektL8tECSSltXnpiGVbhsdWZr6OrMFf3MesDzx4fvcD1U2ZPSjmnfL3C7AFtIfHrfZmWXW8VKXeAcud1gjsewB3QYO7yhw4LoKHgHBcTxHEP1LgTb2xz8ucDwW3zfNGj1dDuya9K6kzeUv_4pLXeTwCoZlenZvn129OkX1WCDLhzZX5wQp5xSXX5hmG05mkQFgmGhSGYODdros1yKVyYzQUyLcn_PbK4_2eA4PMR-LSgTdCHKVU5Mjc89AE1fCtQfS7MPlqiFyqHfilUuqNyebdzZBGt3UGY7_bNXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5acMzyhOtFNeKQq7sLE94xYt6VNmjyoisix-uGH4-PAC8XbLmMQWBnDKaeqfZGvxo4IEQ-S8sYl0D5f96U0EM9Pdqk7Cki__45PUUbxOLl3MMP1LbNo_ezY3722N9ESifGKGzbERaUJ7Nm1EWxrdr6Zkdp6aT78H-AhgjjlbqGGyqEEyifYXOHZw_c5wTZfKhK3Y0gzrfbn9u9bBWTC-aNCuPqZtzpNw0LZ8VeEjvobjIjs1dXyJsAjCjh1z9nXxVGwev427JIlthlmVJI0nY2NY3pj9rYKlIB42I4wEQCupHRYJcB7ic9kk1HsksgN6SihXUatODqzKJ-9t2gz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoA0Sgys2pLZVCSCfFfNtpAf1_4VB5-lgK3TywzAsyENgMTnNZnZ4rFaPQbeVU7GwAp87MVy8oKPwdChAhuYmM82pWN8VgnbYI9D1JqyXhauniozG54vmj6aLnAa6zLZ4fpSF7b647a9z-mgB-N1BUgqn5IfP3pwth3hVIekPsoqcsVDa79ULhAEjD4MQc445lqAW-Y-O0oALZThI8BCl3m_P5Zu0KSWqG0Yu_kwS3S3X16JLWUAqC7r68LLEUWDQ2Py3amORqsbQpjsZ1MMV5db5zIoN8MPnOywhg1RZwFRg5-g5cmPp8osmhPCYKChRtxtVOisrN_TLoalSqcU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBg01SdjYgdeY3M0LMIuthT5GRXdJ9bGg5zYaylOcgX1-8-C8vOhaKkDr8yzJ_hBDHSeX6n6xaOI4VMern3_pwfOfrPigUc6TVIeb8xfcLV00fn6L9SF2LzwNwHJmz96TFkHTTb7pVr8Ip1ZktMbX9Ux4yxDv_Mkb50IkrKxeZBCCUNDxpmSE1IzFSRDSGWpFXnUcDkrnxmQp3gSVxgoXu8JsJntofHfb_b-yPRGqNjgsznToz601RzqdKfmrIg7IGG_EsqSWqXWQGt8n0ij2P3RZG8FKvezfTS5TLvYhv65m9rou5twkS3_bPFOBdDcQNoq2gA9fSYIgaFNlyf-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoeGg0EvpYNbtcLRudKcoCwBjgkRpqMbNykmAx29L7jdHKAGhbsAmsVbGyXxmAvRhca9i0F9ghmNsmmZ5OfITBEkK4_2kjeD5-PSmkrJU0lBthk0JsStYze3xKBplt9vYYk5HNcXudx1ATSFITggbsJWAWJqy2MqI3ldTdc1ekOI26gc1Oa-wbjVeZiluCLyg_qiHj3ts8sud9vBzrMc6g2pHzf9-sBQjk_NUUhllUOwHdT74xvMvQSiVmBGXOkJA7K1Nr243lAwSvHXZV2lO09WYFPpfD58VO2dufBiaWT2GpHVRtu7breRFFa-W8lJrHf9WP9ioRIeIK7j9zIcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkPl1gGcpzXqRdLQQHCAGM9r-274NbI_lG8SYTwildTC7xDVrY9A_9hGZg_5XrwXBTY-Hp7vytSlK-BPka--5WO0SwkXKjJeTkD_6nabTFBKJy5Ud76dcVV1nlweGLNdeKTERCSZhX0FVKZKeTn3M7x9fT0hmwwYtGFdZGTWbywF_RhQLh4_LTCBdP_zFl6RZDFyJoC6JOQvqqIW23YPPvWyBb_AGSJQNltesMeT4ZyTDDtj3ZO7AZchZvmNLyGgVzopmtoPXalJYXAYu8rXildoah_4jQv6j66gmjxrTDp6GItZCDd5RZxXkWmKf8RynTTj2OGJNSpeuZlsvanZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=LBGNBL-jMbW66wtX3kAUNKnL06hE4uoFnJ05gAAVjHJKD7ZKHObZzpcfCSFq6iAcgD-Esp4jeDeweCXE7vx16tVZr81r8leX1bHLDMnlW5s9hTZFUdPGoLLdSFyFaLQNLCW_9RVLXsLS-ftvlS6wuiL6TfXGKA9BkN5svSYiKCCmFEyetniAEFh7e8l1E1xCM59ecdeD_086-CnYPqrowp2_fxmYhl7CKF1b5UquJz-PD110FMoCFe-sldTxQCyYq2lk-e6enBPSFZdL0nU3zE1qphMYp1dTz8VfmeD0rIcCVId1R3iiIzZ0eaWOK99EQRrT8hcFmy1i2mNA9GJnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=LBGNBL-jMbW66wtX3kAUNKnL06hE4uoFnJ05gAAVjHJKD7ZKHObZzpcfCSFq6iAcgD-Esp4jeDeweCXE7vx16tVZr81r8leX1bHLDMnlW5s9hTZFUdPGoLLdSFyFaLQNLCW_9RVLXsLS-ftvlS6wuiL6TfXGKA9BkN5svSYiKCCmFEyetniAEFh7e8l1E1xCM59ecdeD_086-CnYPqrowp2_fxmYhl7CKF1b5UquJz-PD110FMoCFe-sldTxQCyYq2lk-e6enBPSFZdL0nU3zE1qphMYp1dTz8VfmeD0rIcCVId1R3iiIzZ0eaWOK99EQRrT8hcFmy1i2mNA9GJnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIQI7GJpr6s_Id20vcPQliGjrXlfZHpqFOxRuzw-mbXT5C67LBq4TTWIHVZTIeOhnhH_jXLhXR7fVv9YRcUSvtsw7naWjF3lJC6yPQMgBkG_NpbJX-uDA948eP2AeT7Wdmwu-KvnIJ-MZarqJlN8e-3HDg1R3C5lNvKjAmtSwjgclRTZGz0HY4nOHq6Cb_h98Q5PEgbWxn_EGQvv3YRbRjIXJlH6wPJtpivE2NBMYUqPN0ruYDbX4r-tTkebpN9EGMTCH-Y4GMWy8KR_vVNHlglxs5O6mpyK8yWoErzNBu-0Ol2D92V7YzdMYNzyBr7D328ekRt2rtOwP1Dbd3HlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nU6EBj5f_2SGDpVnBZBApRcOU9dw4Z_I31mCbd8RS4yU7zqRduRLPtQipN1yr_N3AUUIZEd0pzAgbsHzuJqpJf-tBXoSlRc9F3N5kmbibZEC_V6dL4YBoOHehxL9fab6s_47NZFiTf3vbEyyVRpxKVZGlploeLukLMfSLjDFMs6LyAi_xIfPP0lDgoBQFE35yJ73MZNiYRugJm9SGKim-Wjpv4Xk_nPg4vU6lzwOS1jNivphfctSZxiaUZyusTaxWZ5k1hUCVZPaj5lGF2Jf8noJDp9nynwVRJXTBhaAbMQ-4nbE1qVSISljeY7UcT_NT9nZBBypyG9_-mSle4Rw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTeGDHNrGTZLdudG64j4hZFKslzpwW1oFn8eMNRtNHejwwvgkHa01QP_hGA8mtJGE_CrmitEKYuNdHZ_ElyXeXkSdQD2UZZg3ZJuVCfEu35qGHEqrkQ2LcpLdfeZokWOOqjjQtb5JbzMX-0AwbTt5iuQge3YUHzKmoaVlALj9KKey7_DmH_MuHHQ2T9Jp-q7JEfbk7I_5kRLuDe7Tr-O28QgptvKmV3Zi3gmlLbvaBScDigdC7G5CljvaqarbaKkTCMT5bD3iYOoeWd2flzL0Iiw-oyALAK6RCbeZqXfwhhn1WC9VxJtdCPa4IRlvKjfjNbbW-u3u_g4k_rA4k2CUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3ZN3n36Xa5qppl2qffzZdw4ttZhpdPno8FCIAABS35aZkhoMZyNoOBOCD10ra7DPvbJXM3Vdd-c8Aqn0ZcMe_X96fDxsG9XELAjtaMrviuugQtTW02kh1BLjhkg9LM2CTop_LIddYgGAHqVm9UxgvmQKD4QsKTu_S8c2PCsi-m_0ogJ5u7RrCOMdQe2agxj8qBcnldgOuy6_OC4Cfe8L7mNoT5AdP5E2NU-oc5pUPO1W23kBxrw-tSEOFuFZepx0CidQZuu3-P6GkGTOCy1C5McLb7n0zalmzGbGURrTvR3J4LtxuX_61gS_gFPolJz5AFFeK8iw_O15T6wGtMs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
ترامپ در آستانه سفر به چین: نیازی به کمک چین در خصوص ایران نداریم.
🔺
یا ایران مسیر درست را انتخاب می‌کند یا ما کار را به پایان خواهیم رساند.
🔺
‏من به یک چیز فکر می‌کنم: ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
🔺
با فوران نفت در بازارهای جهانی مواجه خواهیم شد.
🔺
همه زندانیان سیاسی ونزوئلا را آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOmXVed2lkcM1SytBemcS15_XoK686uDU5Zj9MYHwK8WgU1-3L1cR9immDX2Gs3XCemt7xxY92cwwHlaKl5Zqg_M-kwXsVx3IgL367_9RzNt63Zl0ncMAvxP3Ov4486LPAahSXuPsHgWR9nUXp8MMJdr-7xKryxZcP3Nl_z4thRkZQtukA4I3dAxWfnkr5ZeMRJJcLg7vrjk0OJPooSsmQ3AL3XQ7TeR5KTUYVAMu8JEx2Vmaqm5pFhMd4zYlM5dJC6N0D0Sx5bQYpyeUmXo2uRHRjzG6oWU6aKnKE6Xkm97vV7W63vxF7zlmfeHh2qAN97O3UmHrudPJsPkfaDyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nm_btwSbszDuWp_Pe2FKQcf0K5oYsE09ElhJDUl1j9vMjkpfR7t1ekEoU3KedRhZi9eNO9sZzbTh5ACRDAiFKQIZh21AIT-aKk-NDEZ2cBtqMB_uDZQpLyilj7uBeEP6S_ZRyxf205pzFGVDUNVEA9rGExVDixUsyhZmnfzHDjhfYzzySys3KvYW5uxr7Nm3YU9JuqmEorY9tzidZSZZwNhQASFg5EHDUQxRtfBMY0boyI4VHjpuVWxTIyhHyuqCSYTAUavs8efT8mmmzNpeWzwUZE7PQW5PB-RgwEAU2CCUliUCM0SM3ztsDHHpsc_fr1JIYO9TKzZ9CprcvW2qrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای
رسماً جمهوری اسلامی  را متهم کرده که گروهی
از نیروهای ۳ پ  را با قایق ماهیگری
برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری
یک نظامی  کویتی زخمی شده است.
کویت که امروز سفیر جمهوری اسلامی
را نیز احظار کرده گفته که ۴ تن از عناصر وابسته به ۳ پ را دستگیر کرده.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOO5d-helVjNp1bKX5t4VOkTqHvq2WbhamE3rHQBYJl4cwm9jy5UdUcXP_43KldXuezNN_qnlpN3EjXAOnO_URNJ175IOZigNxT_RxSS1-ZhVdoNSad0z5W-jBq9Xur8NESgjhivafoxSliKAWm_ks55Hxu4-UkrhmPGWzZrkRYyn9JcnAzsZIx-vBZ7agzopMpiusnBHgxwtJRK0-cuXi6c4tRTYYFBioxm1AEbIKGVyfuXxY7jJJFKAKKxkPmSBryHUEv_FqT7mRTji1PURXYYLhfHV0g-0sCgqWmDUecUfFEK5v0Ygzr0eqJZt9D5wNOC_ArwrTUK75LLGhZvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuWz-NqeQHjGKr2bABolBmm04pq2wNAzJXwGRP_Eoq2cqrR7TqI4qOcMyzMIBNpndb1k2NbO6mvDHJhVmidRy3Tus1BeVnuF9Bk5DFJtjt5vgYQ6lej5t4PNeX7ptZn4-GXIv8ogppmWwRo6TnFZeCFVKD2PXF2cbeg1K31HtMT11D2B_Fe8S1suioKmTmL5GxeptUcwsePR8SnbpbcpzKdxakBkSIWODtUOhqes6J-yzIkRqHmQtcL2Wv3WMSFE-mpMVt4JfR_MjjO6toleOKPkrLQXArhyCLsj9gxl3a-oycoJSx7pEptc7RarWe76Lcn7Qv-Ii6EQ4rbpShdcqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=DsHHvRNo97XQpFOqjz2G2wuja-UASnXIi4Et8chWOnUC6H20muC4WzZyBUWtJMOs_idKgtjdBEWrE7caPFO5zmwkA77WBVRTDMDL-WMMaKnUR7Okp7fRttsc5LxJon_GQzx0NSH9qYZfzqN25cWHFgaIcwIZkXski2rqiJPdDuSJBr69snIxOGmlFNPkrgE5KDmbTSyQloPleZoy2iysxP-F7bOBkjxOqy3gYEmjPobH_hPUZsT--gKaiANFRnylaztY41EMb0bC-fmOBa_aKXA0WZ-OAFjbdjam288znbY3lunY7jlW71HW2jN4ektC7M4N3rsNRMrbKEFJod2Itg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=DsHHvRNo97XQpFOqjz2G2wuja-UASnXIi4Et8chWOnUC6H20muC4WzZyBUWtJMOs_idKgtjdBEWrE7caPFO5zmwkA77WBVRTDMDL-WMMaKnUR7Okp7fRttsc5LxJon_GQzx0NSH9qYZfzqN25cWHFgaIcwIZkXski2rqiJPdDuSJBr69snIxOGmlFNPkrgE5KDmbTSyQloPleZoy2iysxP-F7bOBkjxOqy3gYEmjPobH_hPUZsT--gKaiANFRnylaztY41EMb0bC-fmOBa_aKXA0WZ-OAFjbdjam288znbY3lunY7jlW71HW2jN4ektC7M4N3rsNRMrbKEFJod2Itg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ech8g-OXJPaM9vNqVBHJO8hUvr09YRoYPD_LQbfOfapxg3CU084VJU8X4jNnJTcG_nLQ4BWgN9nrY7GGCVXeMUONqDvJ3hP1ircO9hJoYSORsnDLUOSFcOU6o9h98UbYkw-g82McxMpT_OQCHKfajiPLCcwlPJAgm-_6l2Ju4We4HUkQFM3juh2SrhwUdTe-RvGjsfcXQkGNw6OmWdnJ3Vh9srXOvTzoKiZCnoF92bn7GrtKQME2EFLuZBFjjuuukjDFpVKuKOiXsnaHwWHdRUF0OWBVqOHHYOK1-6Pr7kET4H-BPxdLTkQxawrUrJhnOzkVDGGmQxU7M7CIx40elQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIVWItkZxEeDO4X3RScB-8W69B_buVVGKDSordJQxtNvJBwtaELAL96epjGH_9c5_z73eK_np4Mhb1vrP7Gwa6vhVMV0far4u2Los0eudm4GOLVAlbC0LRsri8e1gXAyQs1UA0E19Em-gebBVV3IizckUs98OGSbDvQ3F3526jePlmswXYlFikJfc_KGenGepxZi2cBuoGkMmsajxzWruqY9JjmZF3itP_sGG1dmX4qZv5SpLluHdBFvnsp2AhrShYoPjCdHjtTx58oVYGR7hcQ69e6nIhFaAvQCGEt-yLx_IJ5WngBiSPyw42S1OszcnY1pbGUnhY_31Hvrx5zXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYVQbZNA38Rdcr_7VVSbLTrHXX480NUpLQfWf08E1bfaBiHHiq4Yex2l8FcQuRvP-zCcGEzw5FmwxaqVtpJxfs7KKz7ejwTo04YJg8y3wBMMy2h1IhdPQHo4iqiNt6ehSgqp3bfFfZV2MYcygSg1DShWelBpzopRli-pm0C78GpQH2i-6JHVq8zER3WrDwI4jguaVDG2DnlD9FPToRdN0apuoUT0NWG5w4Z_bki8n9X8zKIoUyeBeeLfHo4_3B4wqUB80WBwfX7L_Dl_Aak1rUm-4HaX0KX8sOmPECbawJXPIocxz4hjP32aUXgM4aHpGXjlh76Q0ctXeZ7leocVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v663VLAY789Ya3Qj_KJr6W60rFvvH_9kYMT-gP4D_PuW2Q5O-e-c203-rfwn9cN64E3uzG-wrkm5StVnRFCXRA9TevgDVse99Qgb90v0gpohqkrRZUNFR1SXoydQpRmGkLhTR9KDtbS4xNgCMW0gYuFZJnBV-yyvLNittG1_o7Bpe7oPsus6PtNwuUSGsW9MkUIJV4OglwdHRHmqHC4F4wFpWGJjsPLn0pCpUiGInEbja3ArCmgVAXbcetfZa4lQXhtrGVJxVVtdVngDOkyGzdAouRlEp3jtGF2kWYC-Q221I4bkWClQVbJ5nSwaWKyXlnnwSWP5JffbB_IPX-82ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FObrYCMY5EqyHclTJk7n8obHk7HkSG2TpafRPTAk5qsw44rH32mdlJ1QnattUQ-FGVZOGzHLw-M6vhCdqR4ixqQrKkV4WhGRc1zLlRk5CTueOO4RtlC4pE5Oq9fxXSKZbyToK2w8g-hgWf--sPkk0qbVm6Bdys162_RTL06kxP5syeU5Ncn8F2lW7W4Yl8JN-HYhup8hdK-aG3t-J0R-EXyiZjw956nNlga9hF8r4QBo0tD4ko1s7_9QP8or-LFmipPLY0NQlX3PoukW-mSlIgs6mxiEg0Wcy46KBTdZKM2cReD-xK1BrNbAkq84C5n5SkqFGUuVYZGACL7SFiNIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
روزنامه «گاردین» در گزارشی از ارتباط اسحاق قالیباف، پسر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با یک مرکز پژوهشی در دانشگاه ملبورن و سرمایه‌گذاری او در حوزه املاک در استرالیا خبر می‌دهد.
🔸
آن‌طور که در این گزارش آمده، او از طریق «اجاره دادن دست‌کم یک ملک در این کشور کسب درآمد می‌کرده است».
🔸
گاردین نوشته اسحاق قالیباف چند سال در ملبورن زندگی و تحصیل کرده و طی این مدت با بازار سرمایه‌گذاری املاک و نیز دانشگاه ملبورن ارتباط داشته است.
🔸
این روزنامه نوشته که اسحاق قالیباف، ۳۸ ساله، همچنین موفق شده بود اقامت بلندمدت استرالیا را دریافت کند؛ این در حالی است که کانادا دو بار درخواست ویزای او را رد کرده بود.
🔸
در این گزارش این پرسش مطرح شده که علیرغم اینکه قالیباف، از فرماندهان سابق سپاه پاسداران و رئیس سابق پلیس ایران بوده و به نقش خود در سرکوب و کتک‌زدن دانشجویان معترض افتخار کرده، فرزند او چطور توانسته از املاک در استرالیا درآمد دریافت کند و در این کشور اقامت موقت بگیرد.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQeLBw-hAifaTB8eqBXb4QurP9rTzVFukWIbg_USQEVAq8y3pACx9ZRY6_E_dp0pNbOZFJmAedEhUtBl1RuCx8ZpfzRqPMFM6ELUEQJLWayr3XMimUIK-xhPMARkwSt5SGqNpdb1sZoPaVOrnV8cTgJBkfBrN9Q-o3MtQZq-4nHk2A3Vge-KF_E4bXLEfJ6NetXNjzPGkRuxPDWitAXG4_IPx1HiBCh34LFe-glshsKaKbM_LujGCh0xkO68hDrgeC3Hd8-TyTggNRu_7AYTCZdvBY1Jh4_bm7c5uTREDuOi9O1ymHHrQlC6Dy-TMPUr5ObaHDUEbJy-Am3e86QTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/holiTdA2MnRXMP9_8oM32tRrFvJKuq64EhYudaJoN4poPQNvuN-kgJwwOIS7_sbzC-lXcnYSf-VucgrC3f7zzGtdiRBPFcp8zcipa2ceUlHoZOuyCmL7FndfZ952w8T1Ez5oxsEWstmoVH9tSsYwaiMs9yVPw9nOJ3Mh_LR_6JbLGVI0ideX4DByIViqrRtt8owL8qrzBERU0S7VCY0uA2p6P2ldtbVzBojS5eEQ1EdZdcBKm2KK4ElkkP9Ln77m_iyhu62pwKLdoKJhAdRAOht8S4WOR5_ysBLNa7SD90JGdyKw7ArUdJevCZt-ZAkFeRiOlCm-adnFDy6i80r3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi6UPuVYGaoCBU0fDX_OeLUVvEFITkEi3dmt0GRZi5kaMYRDd-FGbuTUt8vf4lqMrbNIZQbWLFl8oT7OBcPR0Vc8gNRZ6EwEERH-EvSUH8hJWAsId_cCkUbLOb2VJPK5ajr6FkH85eiMNCbTrT4FWOOR3lLjcj8xddLhiYP6u0FWKN24m7HAFm6RKH4IkLG2rzrOyvvJPMWDFedoQ1Fmo89L_p8ayoHbGxMtU-nr_Mqhj1cAsv_d2vJWhU2pgWOCDyfDmaUrV_btZaPqpGL4LMGzMOt-yYq6LAq6ppCyLI4SRrjJDQj71gwuGzU_oSsdYBx8zQi4KCQV4SjpethjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
دونالد ترامپ در تروث سوشال:
«
ایران ۴۷ سال است که با ایالات متحده و بقیه جهان بازی می‌کند؛ فقط وقت‌کشی، وقت‌کشی، وقت‌کشی!
و در نهایت وقتی به “گنج” رسید که باراک حسین اوباما رئیس‌جمهور شد.
او نه تنها با آنها خوب بود، بلکه فوق‌العاده با آنها رفتار کرد؛ عملاً به سمت ایران رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار پول، و همچنین ۱.۷ میلیارد دلار پول نقد سبز، با هواپیما به تهران فرستاده شد و مثل هدیه‌ای آماده تقدیم آنها شد. تمام بانک‌های واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند!
آن‌قدر پول زیاد بود که وقتی رسید، اراذل و اوباش ایرانی اصلاً نمی‌دانستند با آن چه کار کنند. آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید.
این پول‌ها داخل چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها باورشان نمی‌شد چنین شانسی آورده‌اند. آنها بالاخره بزرگ‌ترین ساده‌لوح ممکن را پیدا کردند؛ در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی.
او برای رهبری کشور ما یک فاجعه بود، البته نه به بدی جو خواب‌آلود بایدن!
ایرانی‌ها ۴۷ سال است که ما را معطل نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً هم ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند، و به کشوری که حالا دوباره عظمتش را به دست آورده می‌خندیدند.
اما دیگر نخواهند خندید!
»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYitJpgolcqdvYLKOTfVrDWWBZJWqvlS5CX4JeRW8uT04WiEs5gGxa5AHF1DabHqZWFO7wA6DGn-AybF0mFXQl5zbfXp8yRrCXoyABUG6qUC6Ba4f-SSUrqp2PmYQNvaUZIg7iInQ4yX3mthYJizJ-_uIOvxl1yiDOCfzM6KKKFbqxkPHfCsvH7abEBgrJhBdzFkLKMWBFpliZIuCFkP2RQfdCm2PtVHYe5Y3kfk6qunDjed-nPfMWT10cs-OXPYZrebYl1pt2mWaougo0gnzWwj7fWhM2WjauzxS-HnjCAFmw7H4QUVyYwSaMuoD-QvQymuB7HjUvzYccgSkH88fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه چرا کمونیست‌های ایتالیایی نخست وزیر ایتالیا  - الدو مورو - رو در می ۱۹۷۹ کشتن!
چون گفته بود : «باید قدرت رو با چپ‌ها تقسیم کرد!  اونها هم ایتالیایی هستند! نباید مانع شد که وارد دولت بشن!  دولت ائتلافی ایجاد کنیم اونها هم باشن!»  کشتنش!
کمونیست‌های افراطی کشتنش و
گفتن : برنامه داشت تا ما کمونیست‌ها
رو از مسیر اصلی که مبارزه بی‌امان
با لیبرالیسم و سرمایه‌‌‌‌‌‌داری است منحرف کنه و ما رو به فساد بکشونه! در حالی که وظیفه  ما «انقلاب کمونیستی» است !
و نه سازش و شراکت با سرمایه‌دارها!
و‌ همین چپ‌های افراطی (در ایتالیا، آلمان و فرانسه)  که به خاطر مبارزه با سرمایه‌ داری به کشور خودشون رحم نمیکردن و دست به بمب گذاری و قتل و.. میزدن، بزرگ‌ترین حامیان فلسطین شدند (چون اسرائیل طرف آمریکا بود)
چپ‌های افراطی آلمان حتی می‌رفتند اردوگاه‌های فلسطینی
کار با اسلحه و مبارزه رو یاد بگیرن!
کاری که چپ‌های ایرانی هم انجام می‌دادند!
خلاصه ریشه این داستان‌ها و… خیلی طولانیه!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=KAkp3pM_4_23sBYGfogrhpOfZn9mO6iQTErS8LIgylXBPKy6l10mil4rkOCAAq8r74vISErPIfMxOt5zbRhjbki_UflwtbUFDmDmjhqUWc9Om58erivBoP5Ou3TgUyUb1iYnQq7tbyhVOmIjx2BY1tz2OIl9nin1PLroH231UlYL2DnQkego-vk2OVHOig5gvoNn6yd8IpxVFwqc2blffkMqdZs1I8-dseri9mDIQsrHthlXr4yBDc8JTiEw3hqZn6wg1igD_L2J_jNFRio1vzM_zYfrw89ZP2DLvn4xbwgguVRUMbKr6stSBO8BgcePOl46ErcgMM09p9PqYiqzMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=KAkp3pM_4_23sBYGfogrhpOfZn9mO6iQTErS8LIgylXBPKy6l10mil4rkOCAAq8r74vISErPIfMxOt5zbRhjbki_UflwtbUFDmDmjhqUWc9Om58erivBoP5Ou3TgUyUb1iYnQq7tbyhVOmIjx2BY1tz2OIl9nin1PLroH231UlYL2DnQkego-vk2OVHOig5gvoNn6yd8IpxVFwqc2blffkMqdZs1I8-dseri9mDIQsrHthlXr4yBDc8JTiEw3hqZn6wg1igD_L2J_jNFRio1vzM_zYfrw89ZP2DLvn4xbwgguVRUMbKr6stSBO8BgcePOl46ErcgMM09p9PqYiqzMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به مارکو روبیو در وزارت خارجه ایتالیا
سند و شجره نامه خانوادگی‌اش اهدا شد.
خانواده مادری او ایتالیایی است
(از منطقه پیه‌مونته - تورین)
و خانواده پدری او از اسپانیاست (سویل)
او کوبایی است.
در این مراسم گفت : از طریق یک اپلیکیشن ایتالیایی تمرین میکردم. همه رو متوجه میشم! (به خاطر اینکه زبان‌ خودش اسپانیایی است، متوجه میشه
و نه فقط ا‌پلیکیشن و تمرین ایتالیایی)
هر چی وزیر خارجه (ایتالیا ) میگه متوجه میشم.
اصلا نیازی به هدفون و ترجمه نیست.
دفعه بعد که اومدم ایتالیا، سعی میکنم که بتونم
به ایتالیایی هم پاسخ بدم و صحبت کنم.
باید اپلیکیشن زبانم رو هم تمدید کنم.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4898" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfZFVvpoheHLvsnb8KVPk61RH438SBjB18AvUFj7LD8AVa0F8tdeY5G1xQf5vzoN8JBnGNMPpMJvGCc5y60VNKEbTlQEoCocujSn3MYx7_GEfZOu5oEnnRo50irF1NNgxU5NbVeN1DFAFDqeRfNSnSgurdrkDTowZJiUAy3U8ToLOk9pB46hY5odUy1seMu3dis74T_JYmDRatNV-JDqZKYWi8XrOp8LV5rXpV5EJ6YPUTRpP_Et7d3bzIPLEEWwNEeCwi8qLg1rIgaQgTVDYlRwmKPmZ3Vu543rd2PkV4HRo1XNX1mTdIBZ7Bv0-rm2hF_NoWgWQtsAwe9ZAkIHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIFW2Hno570pq8LRExtFT5_x3ndjFWgTot0P81i6ED6Z_opMbKL5iX9cCQ-AE5fUTafe31pRWAt7cX2U6SGS77uwjncE2A40slj1j-k_SyhzdzM1TtXni0s3rjsMVIoyqciYSCOu6Wh148UnMTvcZL_hIY5KSZdWizZoxhg6-zupy0BJTy3JfeR1YyKsTL-xSwfknpLGPALdYbAC6B0i8wOCCp53McJVToktaykzRzmJiMOOBPeVw9keN7XCJeVohgAhUTry8jODdH-wa5BzJ343phKsrlbZpjldgz8A-9mYzf6sloXzkMrxdFlxpk6XHAOawE18UuAJq1BLHMlTcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=sCuuyqFcCvJ7ygWau5N468zW4_KRIlI1bwAZrrqQ4t_nImKxnMtnRiDZEfxZFaMb4A389s_yPoIZgoEppnW4d_L_a6c1uU7PZNHVX_2litZKbr7ssmDCgWD1757agUc2cZAIVMLt9EMGSRSotXl-NVpII72jTgJlZEoqPzUQxreEOLc9541o9-iVQdK6t8e1kpDpIDJVz43xshStP9u9M2xkaBkY6R14E1HdrsJ51Z2JgR22OuRTtsmSDYRaHGEkB_8MP15Wxge_TqXNloDAF1SxYG83nxUP6f7LEu4ILsxnDtsb-kf2lDKxYMVWCtT9PHCkPwNfJOPv75RBQDKs_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=sCuuyqFcCvJ7ygWau5N468zW4_KRIlI1bwAZrrqQ4t_nImKxnMtnRiDZEfxZFaMb4A389s_yPoIZgoEppnW4d_L_a6c1uU7PZNHVX_2litZKbr7ssmDCgWD1757agUc2cZAIVMLt9EMGSRSotXl-NVpII72jTgJlZEoqPzUQxreEOLc9541o9-iVQdK6t8e1kpDpIDJVz43xshStP9u9M2xkaBkY6R14E1HdrsJ51Z2JgR22OuRTtsmSDYRaHGEkB_8MP15Wxge_TqXNloDAF1SxYG83nxUP6f7LEu4ILsxnDtsb-kf2lDKxYMVWCtT9PHCkPwNfJOPv75RBQDKs_zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
‏ترامپ: «ما هر سه رده رهبری در ایران را از بین برده‌ایم.
ما ممکن است دو هفته دیگر به اقدام نظامی علیه ایران ادامه دهیم و به هر یک از اهداف تعیین شده حمله کنیم.
ما اهداف خاصی داریم که قصد داشتیم در ایران به آنها دست یابیم و ممکن است تاکنون حدود ۷۰٪ از آنها را محقق کرده باشیم.»
‏ترامپ درباره اورانیوم غنی‌شده در ایران گفت: ما بالاخره به آن دست پیدا می‌کنیم، ما آنجا را تحت نظارت داریم. همه‌چیز تحت نظر است. اگر کسی به آن محل نزدیک شود، خبردار می‌شویم و نابودش می‌کنیم</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4893" target="_blank">📅 18:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWu2UsXtePTa8JXxP6VsfvBZLpsEqkZbnQ9YXDdh2xp3_GGjfUGLkdGbz5g49wD_L8XNTYpdFTQHntIDXXeBvjYua20okkM5p1DkT724557Ziv464zAE6Cv47z-1aCCdiCYKcjhHXYSawN7fVwM252dhsvScc41RRJBYG5LHGY8xH9DaQTrfckmgA9jFuOgFa46zXLQuG0hgLmzTLUeq0e4LtzIfD7LLqwlTpnBKPFRz2beXtNtrwKjQpyNE1OquHbAxslIA7eui1Ly6N1QuNQLb98jeFiBdS1x1GqVWknDHhjuOWn5l08amcUJi0JpoomAlmqpN1wVh484cmj7iNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATa-tuviaDjJ3oEnJMVTA48E_1-XTQYNwVC5XelZ86Pp7ubgFlngT6Lw-LrmpmnIdld1wIWf3949XRhN6V80SwTJ4fwQlk1U9uAjE0rCI9V4CuQ3Z45Q87-CTzbjxYZMShQW21-kDzo5ZqpMN-2XmX9Ji7QZ_m5JAc3vfDMyDdQ3cFG_O3oXlenKIVKAKel2jkciDcoyDaw5LW16CGHv0oWrrypCxf9MyPb_Gf8Ov9D2Jf3CB2qRoVTh5Aqm6I86tPdOkV1xneyLBf6EqC49oMfkKmZfVt6WpCMuSFpEYrrQT8u4IXAd4IdU7eF6IsgD9sPjvbfYGd5M9VHPOQrwMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰ سال پیش در ۱۹۳۶و در آستانه برگزاری بازی‌های المپیک برلین در آلمان نازی دستورهای خاصی صادر شد.
مثلا گفتن که دامن زنان در این مدت
می‌تونه ۵ سانتیمتر کوتاه‌تر باشه،
گفتن یهود ستیزی باید کاملا متوقف بشه
که وقتی خارجی‌ها و خبرنگارها میان،
بهشون بگیم این حرف‌ها، فقط تبلیغات
دروغین خارجی علیه آلمانه و واقعیت نداره.
یا مثلا دستور دادن، بخش زیادی از نظامی‌ها و پلیس،
با لباس مردم عادی توی خیابون باشن تا جو پلیسی و نظامی به نظر نیاد و عادی باشه و نشون بدیم آلمان نازی اصلا با تبلیغاتی که بیرون آلمان میگن واقعیت نداره.
حالا توی جمهوری اسلامی این چند روز
زنان بی‌حجاب رو ویترین کردن! و طوری وانمود میکنن انگار ما اینها و سوابق شون و دستهای خو‌نین‌شون
رو نمی‌شناسیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry7Jw3lzc1ktCDzmvtsRGV5M3rNt-Uu16XnzgBszprBWsI3Qwjj8ejCc1dYQrfVxdIJPzGQ3bF1b-M0YtFrjdJr1RjHc7XYyqqfeV8CevFZ90yBFPr-foExNiEo4kk_Y9vRx95m7ilwzQHGxG4ZlATvtXWmSp1A3NE4T_8gyAABKVgTsXhfYIgijHhuJQAg19i1bW1dFT9xEvyZHUCoukGpco-oefbV2AzMo1TvdbEVGMQhbnqe-M1MMexz86t47Y7WfCuTk9iNYRnFLTfnpM-spnHSvt0U2xi-FPb4QMhS4G-2mblf4jE5u3AO6OXP640euh4YQxzbEICkFvWB3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXGw8dEU8SiwCeLtHZKgRdYdSI3BOFaHYnuV3AlPHbf4bm6qGIuWAyHVm_h1G-JEKAowikQyuwCCvbr8C1RGZPSIPIQnAdcdW1hV5p35K4TWOLqOWbp8spLTiuv8R_yCGIJIE5sLnMYYzwKyG_Nx-_exB44TLfpexPYNY-HGlhKmcHvjxgQFGJZWYjIKCDWj6_EnQS3CvJJpebtDSf-5mpcJDo7EHXA79V6LGlEFBDtyW-EwYJ_nmbID5FAeWcVUKMVjS1PuJctaclnJQd7QZumsWJjjI_kfArorzvq8HdfcoGcIp4rxUf843x6GA4UA_Hgb8gsIB4lpk5T7tB2UBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsfyuzRRQT0RfCK9_7VR6RrubmqIycIzRdeGF050FwPH5e306F19sogD00RjJPMYsYhk5AWyhuTW--jlf9WSAF07Rniy8MnnC0n9COqzH_4k7l4l1ZCixxqyR9UBE4wLT9ZcPD0RRaukk8DJVMe6_Uo_MwvmhyNic-lAOPskCKwAvBioxDAJXoWUo_bOGQuqrO2uLRA4UWpVg-i0sd9y0Nng4sNfSi1-NZXmzNNDOkMOPmRPM8GTKHmQrbvq2E7m6JuZn-vOXeS1DQyO6ypPJjNhd3RWLql_VTNDfD4TgZJa_H0EQ7Ny6VjU4uemnTauM10xSxV5oVE6DX8J39fF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ‌دست به اخراج گروهی از شیعیان پاکستانی مقیم امارات زده که برای جمهوری اسلامی تبلیغ میکنن.
🔺
امارات چند سال پیش یک وام ۳.۵ میلیارد دلاری
هم به پاکستان داده بود، که چون پاکستان
آه در بساط نداشت، هی تمدید می‌کرد،
که بعد از خودشیرینی‌های پاکستان برای جوش دادن معامله بین جمهوری اسلامی و ترامپ، امارات بهش گفت سریعا این بدهی‌ات رو پرداخت کن!
که یک شوک عظیم روی اقتصاد پاکستان ایجاد کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/4880" target="_blank">📅 12:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUKlWj6nzMUThkSEl_ZuciIOOe-DeqaiU8a9ssB7cGhhcmXyuSVdq1p_jDGbiAGPwrJHsC8BMPn4EB2hYDH3rvsSNs7bzmodxXCsI6_bKMe2ZNNKcWQ2BwL0IEIcKseQadb8QucVP3YKb0jnDHXnFHzgNRiDPe8zy-5vYZbIrRTPu6PL8CJ9CLKl03QJNZZS-SO76dG2Joqim76GLv8OyQztck5naq1emIHBLhgpCyPN60iozahn0XNfsaAZWt7mVkIOYBZueAytGPzSXlvGS5-jED8suKy_E-_xtTRF5xQEbXfKkVhMTxh4wOjA35NBk-9ZhlZjkkq4-PZcjPb4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت «مبعوث» شده :))
این هندونه رو  این چند هفته حاکمان
جمهوری اسلامی زیر بغل عمله‌هاشون میگذارن!
که منظورشون چیه؟ مبعوث/ برگزیده شده برای مبارزه با آمریکا و اسرائیل!
«قوم برگزیده» لقب معروف و شاخص قوم یهوده! برگزیدگی هم از سوی خدا بوده!
اینو فقط تورات میگه؟
نه! قرآن هم اشاره داره بهش:
سوره بقره، آیه ۴۷:
يَا بَنِي إِسْرَائِيلَ اذْكُرُوا نِعْمَتِيَ الَّتِي أَنْعَمْتُ عَلَيْكُمْ  وَأَنِّي فَضَّلْتُكُمْ عَلَى الْعَالَمِينَ
«ای بنی‌اسرائیل، نعمت مرا که به شما عطا کردم به یاد آورید، و اینکه شما را بر جهانیان برتری دادم.»  بخش بزرگی از کینه مسلمانان به یهودیان از  شدت «حسادت» میاد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/4878" target="_blank">📅 18:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiTUO0BqAk5N2ptUWBF4IMAgH2AAFS1KWysGPgt_LO8AqM9OscK9o5Ejd-4utY8dVqhqISQaexpDE4NtARPKQ9IA4Q3G9DKfO6LOt28NfLTZ6C75xC7ltXwruA1qd6OmsLcEKSstQDjmoXT9o8LnunNg1yKlsO3hkIdBFzbTWby4UNCRASk--ocMEM8XFA3DFZBIGoCA9kwcBmXvhNfaB3_GjQ3WIH1LjCtiJOitDrajiBGGjo8_XmQNdPAigumdDAGS2WSkMXB1N2LAj1B3I88nd5lbiz9pgZu5Da21d3TSt12ojT1vrcndNLM-ngpVcNa7WDaeSAbLCvAYEBn2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط واسه اینکه
روزنه‌ای متفاوت داشته باشید :
در قرآن بیش از ۴۰ بار واژه «اسرائیل» ذکر شده! اما یکبار هم اسم فلسطین نیومده! حتی به روایت صریح قرآن (یعنی
آیه ۲۱ سوره مائده
)
موسی که به‌ دستور خدا رفته بود قوم بنی‌اسرائیل رو از مصر خارج کرده بود و آورده بود تا «سرزمین وعده داده شده» (فلسطین) رو بهشون بده، میگه : « ای قوم من! وارد سرزمین مقدسی شوید که خدا برای شما مقرر کرده است، و به عقب بازنگردید، که زیانکار خواهید شد.» !
يَا قَوْمِ ادْخُلُوا الْأَرْضَ الْمُقَدَّسَةَ الَّتِي كَتَبَ اللَّهُ لَكُمْ وَلَا تَرْتَدُّوا عَلَىٰ أَدْبَارِكُمْ فَتَنقَلِبُوا خَاسِرِينَ
بله! پیامبر خدا، موسی، به روایت صریح قرآن ، به قوم یهود گفته وارد این سرزمین «
مقرر شده
» «
از سوی خدا
» شوید
و خارج هم نشوید
!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1KPDtYdzNTzKxsLeIBQaivMsWwToz_JEUkNWMICzP5GY-x93muz0YSy2Msr66aW9VyUxlGxXsSNRPpmIbOpm5GmronPN4PA788OlC0OHmXTUzyQoE5XPISshf2T4hoCbvESrR0Kavs5vRGi0LpnahQUjhfB3duXTifFgD229mPhbRgIf8RolqbuukzLgWW3MzFnsR8JY9aoi-0Jdu8q_sTJSEN5-9KSiWGARmkR-nZHui4d3FoirPB6wb_rzTRVNiCBk3D4ziOfpt_SmS1KNf_gRW9L8G3uGuDgHtfSgL7ToSjwKokld48p42hfHbneKhCZ9WZqM9md_dB4bGW7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSxxZ4nz-rjfZBWsmrDeC3gb3O66hnzDwJFmlWS7erIfznJnHMVl02nPyjOOlvOefDrF65xXc-2bnYsEWtaWZMx6N7efvEMZx4aKDIdrLIaKhCP-P3_CMbQtV4D-Q5AwgvrmTCRniwtdtrhza--FIaSmm9obK9lQk2PImHfi4PCMAg3T_MA6mnvl53DfiVs5pCgSq03oPlHYJDvcnZ4A5kR1AeQsdEjlyo0IkFNZVAgbL9ivmqVOXcBdIaVfKiAjSgAVVXgoFmQFfIiu6ZhBuw3h8Y-qCAHjmn_dd2x46_dkcSAiEcEV4DjWVqZn9J67t5nqKxiDL-NOxjuuGKHk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0n9eWfVv9ui1_xsLUt38UNOOlbfg2F_pG9ezXW1xLeaPPJxUFb8hETR-x6dfJcAFXt3TY5-NyxPkXC6k1MxTTyvzpSbTxx1RUEXnT1lRyOBcb1nf5W2USHWCSitfxY-qm9zp4Eb3rfWyz90AwbGqCGMTRQjBWDSc70GEPC-Y3sJ2iKzhjUTnH6OjdlS8_vPg-FC4Bgk7UkF0YvhFEAVVWDD4vQbtzH_IW3CviNoLeJ1Izlk6bdI6H0aK4-RqQdD8rn3iwat9kAl4Dx9a2DkWWezLsJ4laIu8fVxgoBE79qokWTG-nSo-nKCzIq61KBBsV_1WSByoU4yRm2nPDzvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD6W4vgeT9SFnWXHcwHdqYiE371j4C4XfYnlqKs0icfxB6Ugcr2JVNIX1xWPheQRj-fSXxGmCuX0KEmeCvYcm015P6sCschcH1MSfBbTgivwzKhOAvf8XyjRQnt7jB9XNe82RAwzrISh1_tSkarxDo8AHKSToX-nGCXB7mrkpRfuF-3nEgylxX8ZB1iN-foNm6h_28fsU5dHeNNmIg1K5GtEMiaJ42jq4tGMCHIhOJyvSoMJswBMpaTS7ce79006QMpByIbxdUqAKjVkpAYkk1z6EUva8Sm_9GNo6o7A6RgUvljLQJRWiYtjVEL_SGaNJofF_O83BlvEWhVm2_1HLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjCmhDTtKbIw4fxyBPk6rkk9N4njd5CMo0QeASQpAFmoL1MqATZhSxgiO--gFHJJkI02lWAi5dfdFT7IbWIEHQ-1zDzXRR0Cne8j6McfvYn4oCPtn-mpsiC_zzztRs5BI0GF0RggRbA8dcsj4T6Ngx-AMXq3jiD1Ycc6c-05owmz060cPtPhlfyMlaNRf8rc-TAqdu8JWxq3CBHhNYhvFIav8XoLpVYnY6mcKgoGtN19WmGgKxt13L1aMT8-Yhl4ZtdLO1lioyJobz3ZatLX73OObDhJpFvsnUrrrMOqGC5QCKQSYK6aj_TP8-bjoSdb4PtIDTJaUiCgtsV2j4z3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAK-Sbn1yZmfoPHt-pPNJCxM0jIlTWZmZOtOLGfnTygyjG6i9_pjZQgppgQ46oQCQ5u9OmKXJJKpC4ld7IjcnKoiLqcV0ZVBNQYeUUQpKGa-KwjN4Rps4SUQY_-0PMHS-65r-wNC7BD8ZZ9KRaY-S_dYdvAQ8oO5ELuJnPCwGIIh7wSpx33kRi5xGAZp5PL5AN2J5RRhXuKxyScir-pzrrsO-pa7xwKHHk05BPCKKfApDBmox28rdRgJXZi2I-z87pCSRQ2LTYZYLmHa07h0IkI-t1tZlTlzH1wED5y0pPNr1vGuxXr4gXf_5arpbSqtNgXFor0NkjniQIIw-sub9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=AttWbZulUT7Nzrc09RkU7sLT-vW1cE_chgTV2uE4ZTz9ey-OL_79VGCZSTXoq-kckgOGXrrBPFG2FPmaxP1oFqOaGeUrXo9ZVa6klzIw1tJQPFaP2lGO6qyqgWHMOuKEQjQr5pvDHZB_8g3T2NwzI2iWE4QlxCoEMra-0vBu3EEbqNoRKvl5BlTGNxkJUTXeKnCWaY4-7vkchYaUj7rhB3bAEssGYG6_GT83SfcTs2BWn92PgAgGdxTCFRgPuWskK336IirrAl7zYWBLOXfjpKCDg9mwUHlnNadGjZyxQ6oVz5wS2TSQewaWsj5XLqBSTCVjymLeepPmg6RA9o5SIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=AttWbZulUT7Nzrc09RkU7sLT-vW1cE_chgTV2uE4ZTz9ey-OL_79VGCZSTXoq-kckgOGXrrBPFG2FPmaxP1oFqOaGeUrXo9ZVa6klzIw1tJQPFaP2lGO6qyqgWHMOuKEQjQr5pvDHZB_8g3T2NwzI2iWE4QlxCoEMra-0vBu3EEbqNoRKvl5BlTGNxkJUTXeKnCWaY4-7vkchYaUj7rhB3bAEssGYG6_GT83SfcTs2BWn92PgAgGdxTCFRgPuWskK336IirrAl7zYWBLOXfjpKCDg9mwUHlnNadGjZyxQ6oVz5wS2TSQewaWsj5XLqBSTCVjymLeepPmg6RA9o5SIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،
یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت
از امارات در این کشور مستقر کرد
(همراه با خلبانان مصری).
رئیس جمهور مصر گفت :
«هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر قرار می‌دهد.
ما از امنیت و ثبات امارات حمایت می‌کنیم و تجاوزات ایران را رد می‌کنیم.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4866" target="_blank">📅 12:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEFt99QH7_NLF1yBQfoCie7yaP7V4UQS9h53mHg248CE7IU2DwhdNhv1QhZ6i51ouP38pE2pcFXyVs2LWZYFbWdcymN3N9JaadHP_3ChhgzL0auXjZRQ3Hld5TED8u_5pzZfSgi_zb21fTjHoefBwWr4vKslPYOk6E5MBW1ryXRog8p6ozn_A13EbaQgS5gyTGsLCuhg-CcTiHvh__4gwODd01PnN-1mZhjVpAkqLSNANWKkCU5ILoBhpOPg0gdeGQembk9LtggWcTOu6y19Qr7Sy7sAUM6_sYMLucfxABrW6xVnMsSarA36fUFAZyONFuZc9VzqFVSI0xxZ78LjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GN80wwdpz8WWT2SHD2DvH0l1moM8s97wKnNvFMwM7j1T1EjQuPIb-iEWYK5VwRi9Ew7Lxl2cxlaBNrlZimu05aXEvTV3Vk_stsoqmrB0nIs8HQDO-4wbeHmFPC6J5F9mFqvckrVmhbFFDkdBB6FSnkVucdAsfZwQQShheHIkxmjSheyzgemYQSsTr7qUQD0NhfoT3-XZSJHFDGDEej5PyCwggK9JM2yBWiWYXMijXIol-WzaSRx4XrTAP1STsgCdI59c0VrCyBj1-T-nJ2fo5viWjNzN6Z_lOb3HHMamxm7kxAewuZq34yfsyjpPmExt8kB8EUxvmSWao1FliammvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkZsR4zab6bvebz12Uz-JUzZcDHPmD_FuU1Rtn2lIRBdkAR8YDnkrV5_igNQxuhZ8pzfo3exYNXxHy1NnevY8ruVXP8b65Nw-XNfwPRxaOChWy7oT6u64F6QgZt5LPmvyGg0e30qDOOZ0E_AtVm0Wz6k_o6-leoLGcvGFkZFqLCHdPGbktU8Uhs_Ad4BvkSNeL6CctO6z7PxalS3SxNoVN6E5IkBUzc6io8DqL6yuJYRM0kGHAvMB56ronzubV3cqM5qxqz_Q2w45ml4e1Bj4r9JAsurbDNYnxoQ9xpdUAwUAjU1e9k74jgxR_wrrR8ta-smFK0s9wmyOm3OlP1Upg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujDuvRn1C3viCJYQZ4vrB9Xn5RVxh5ikx8RsbyRz999bWuaSXiQ3qkNXSTPXSUEHsBWD2UDDrgKLgA4tsTriWQ6iak04MN8DRsK6Z9CP6xl5q7YqNq06zM94nZZBB0StbGgsjdXV1u2hjuqANJfbdysX4UIHcWsw2Xmt5XLfxNu0R_qxbHnOgapMuZWYGID5ZxRJpp3ezbXTQYMrJ0EAE5cOK40he-iPparQAR-1xZCRpGnAJU-PfFPMLPKHcCFlX5E2Ntc3SvbVhwGKTFi_TB1pTC4bvSCshEvM4c5BU65GuVCD5KOm5aznzmyLydojB2Ag_Yx4gYpaS3EblardbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwhKA77MhGBGYOIh2uv0ob40O-YQCwVT53XUQcJ7rerGK58aWyD6E6-1k1KbnVm3Cxh-jj4watTDoxOWHhBz96Qg6AJD0qbPEyxED-tC6_Zw9z55ZgSglK5XAZw5q9P9sjeJRXdmKVUGiOFxZBhjfGzOLiJOJYvYz1Xhn8X3TZ5oJO2FF-vruQ_URmkrLKJ0dLQZFi_Y3ZPLRisgsOlBAcAP3yGzVNlHK3d3-VRwkb5LuSWCCA9cmFgzTfDjRzHgrsOWbdcdY6AIPP3aCEwPMf7DdUonVq3nfqjrOlVTqSwOtY11fxlMoJw4AIHrnJEMLhwS6NimK364ifnsfpI-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOQRqKgBaQ4CexJPoew2dCBCsO2vdTgPiRZ1KNzkmqww_vcRObOsYC2dB-GxOH8B6pWQjKGrOSJIOR6IRu-RSiScAsZ21DX7lYT7viyaVW9PuHsrPB4kJV0rQ8C5n4N6GRd8lecrfWcx609F-2xP9qdJRTUh3xn8RW8mfK0fZsMdpgKXgTIA3Dluqnw9sa2-ElfBSYH1gYaqJrGk3fXrnU8bT4JKotcSqyVaXE_UJW6_T71_N9X4rhQkhtRwN2axzpL80113FMM8ea367wvi5hdRF3kQiCvi-EelHHrwbo3crWahPvZae6e7TBqsp1U36XQiNWGmu8P6V46jy_zhFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XADueX0Nu-DPaEgLfoNFcgwhlWYu1xYTuCVzx5JCErCH5aLqNDEbHP78AaQlCnSD3vKfLaTai7k0pGOIUvXwhUEC1AU2X3COqSG930WV6IzLdAka49mqlYVMvMTWyCAyqWD-x4rzro7GRh0BYpoOs0UCAE-lYDaUkB6orfgAiBgSVrP8dOSWW8F2MrDfvTwICEAsfLb32pZCdm1-qLbWrZB610BOkkhKNJ5xbSNQZ753eNr251QttjhR4tET3eDHMivLp-wtkqHRzF-_sGR3Vno_2IBZyayW10TjpGy0Lrz7s6lj4GLG2hsgSDOndqBkW9uoaUFmKacHn053Taz_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
🔺
سه ناوشکن آمریکایی درجه یک جهان همین الان با موفقیت زیاد از تنگه هرمز عبور کردند در حالی که زیر آتش بودند. به این سه ناوشکن هیچ آسیبی نرسید،
🔺
اما به مهاجمان ایرانی خسارت عظیمی وارد شد.آنها به طور کامل همراه با قایق‌های کوچک متعدد که برای جایگزینی نیروی دریایی کاملاً سرکوب شده‌شان استفاده می‌شوند، نابود شدند.
🔺
این قایق‌ها به سرعت و به طور مؤثر به ته دریا رفتند. به ناوشکن‌های ما موشک شلیک شد که به راحتی سرنگون شدند. همچنین پهپادهایی آمدند که در هوا سوختند. آنها به زیبایی در اقیانوس سقوط کردند، مثل پروانه‌ای که به قبرش فرود می‌آید!
🔺
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند،
اما ایران کشور عادی نیست. آنها توسط دیوانگان اداره می‌شوند و اگر فرصتی برای استفاده از سلاح هسته‌ای داشتند، بدون تردید این کار را می‌کردند اما هرگز چنین فرصتی نخواهند داشت و همانطور که امروز دوباره آنها را شکست دادیم، در آینده بسیار سخت‌تر و بی‌رحمانه‌تر شکستشان خواهیم داد اگر سریعاً توافق خود را امضا نکنند
!
🔺
سه ناوشکن ما با خدمه‌های شگفت‌انگیزشان اکنون به محاصره دریایی ما می‌پیوندند که واقعاً «دیوار فولادی» است.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4859" target="_blank">📅 09:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_b8RGEbEMGg4dm-YSKUHylGA5SWjusdfbOF6A2nRMEnuymwm8Ku9XiYvdG9-Tz20SWx0m_doxUcGHfZgt5TYeEgiixF8j9B4XIlrn7nVxz5EKhPDg7OWvQTAWIUFmS8Kwm2q_UWA3Z0SgNKTX8C6AJU2zQi6GST1cBJ5kME4PLZCgq6fB75Zh8zmafazpACNDI56SbCJoMHoO5PjINoQdslZ1foCsjqAuR4dA_e7ojrEZUuNQo_cwcpM85dyb3o_q877Rvo0O62zH8M4UbGMg3rBMG55LwTxzZioBcq3QK-JjQnvTJe96ViWJpLTKaIrG0GJ9gPDp2HF4z962_Zzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4857">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tejjHbru2PVjV2kY2IHZ0hkYgmTZkuzKq3DFmMkAz4B2WTj8SE1w_8lIE9fkAT66HJ_NKMrkdU1yS_NkDSni6Qyk47RxMwtNwnIhk40X-_cssAvHXaent_aJiYT2mXSV1FvzqMC4AZNJoGVUrBT4TWXmbqTLLPib7nNIRKnvVOh1WJIqzprPgn-W3RrIfs9Oq9vxJHGR_43JNroCn0VI3GaY_HPfKQ8iZN2LR4y-yHysU0kIcBXE1UgmvqDCYYYZttNpt8Ah5Ajz2VDEAPwJMWlQ1xaqHn1otZPdEsAl_tkFUBLJkj1ko0v4lPScVQbwvX1uTQa_fVLtscFQljzHog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه سنتکام : سه ناوشکن آمریکایی در حال عبور از تنگه هرمز به سمت دریای عمان بودند که جمهوری اسلامی به آنها با موشک و پهپاد و قایق‌های تندرو حمله کرد و آنها نیز به حمله پاسخ دادند.
سنتکام در پیام خود افزوده که به محل پرتاب موشک‌ها و پهپادها و همچنین به مراکز فرماندهی و کنترل و مراکز اطلاعاتی، شناسایی حمله کرده است.
بیانیه تاکید می‌کند هیچ کدام یک از ناوهای آمریکایی مورد آسیب واقع نشده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4857" target="_blank">📅 01:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
تداوم درگیری های نظامی
🔺
گزارش‌هایی از حمله به بوشهر
🔺
گزارش‌هایی از فعال شدن پدافند در شیراز
🚨
حمله آمریکا به میناب</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4856" target="_blank">📅 00:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKtMEecHRmgudl5Vn4FUHgRws37etV7YEE824IVyu7p-d0Nd_HmXpEVM9EIekpE2K_09UzdBn9Q-p5bc6Bu9_FaBiEGrsI6_uUcqgQF8HuVGJcuwiXLHpR8CKeIF_Wqo2ptMquRu13RN3MfVB-K6Hl1wTMcp6zgHfQYU6FL_etbweIeLddcLZ20noPIqWa9qLyH7CDTkpguorU3seXiORY8RUYEdbXs0ldowWxeSzRVfgYefhQBhMCoLon0I5b_o6028FlgsNdpjx_EDVvTjUpof1dtPuglkvR0lTZFtqloo_08RcyaFjPOJd2ibZbs3xai-AdtlKuhvRsjDdg0rhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: با تلاش شهدا قیمت نفت رو بردیم بالا و به یک دستاورد راهبردی رسیدیم،
ولی با یک خبر باراک راوید در آکسیوس [ که خبر توافق بین آمریکا و جمهوری اسلامی رو زده بود] قیمت نفت اومد زیر ۱۰۰ دلار</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4855" target="_blank">📅 00:49 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
‏سخنگوی قرارگاه خاتم‌الانبیا:
‏ارتش آمریکا با نقض آتش بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند
‏همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.
نیروهای مسلح جمهوری اسلامی نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4854" target="_blank">📅 00:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی  به نقل از منبع مطلع نظامی: «
حملات نیروی دریایی ایران به ناوشکن‌های آمریکایی در دریای عمان ادامه دارد.
ماجراهای امشب از تعرض ارتش آمریکا به یک نفتکش ایرانی آغاز شد و پس از آن شناورهای نظامی آمریکا هدف حملات موشکی و پهپادی نیروی دریایی قرار گرفتند.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4853" target="_blank">📅 00:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
تسنیم: «۳ ناوشکن آمریکایی
در نزدیکی تنگه هرمز هدف حمله نیروی دریایی جمهوری اسلامی قرار گرفت»
🚨
خبرهایی از شنیده شدن صدای انفجار در ابوظبی و‌ دوبی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4852" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
