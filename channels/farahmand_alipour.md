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
<img src="https://cdn4.telesco.pe/file/NoHYwl4mcvUU9MJsSJNHkrH2LI8d05XSK4-wB-dhXZ4mVIW14svOjrlsV2xvvzQHFZbVi4dnQ0lOUdpVMe5OsHVtjRhKFJpi2Qt8B1fhNHu-sa4vxb51g9MOGXdMJeDBVbbO-ONyFi5IjLg7ecEB-bhXtKsptGB0xJ7rJKI3WCTAP4SRv8fJasxL3imHwUCr5Z2AeYt-DU7pAunI9paoKDMj_IY9_hYrl2xyonCBtlf9u-z5upMFwJpfMcoArrzDOGm4Wl9SwP-F8VUHahDBDD1siiCDnraU-UV_gkZsaIkFHVtnpCXRlOL5YvBxbVwTvPJqG4qFDmN1eow7l-8MJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 60.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 22:58:53</div>
<hr>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=HBd2p9VFgDu_3V4V4CQapncWDbf9IHmQn8uZluF87qqlmiu8R7Ui4nfhwHdjUO9lFeONZuxUAAgva_4soOgZ4pO6D-YSBDZxE3P_x6YBlkfqZeYXeb0SJ_Q8Lsa1quQyS_78mcogw44fpBGp8MXbufiP-gC6eYkl19vqtp7vkO1ovmCAGatBQju2y_uYCnrC2Es8lcV2dwPO1wKG3pNei938DflFPL6n_o8lS8zNQcZa4NqJYTi-VDkuPArIEN4MUSrYtP4Ob9EbwFXchwCjLP-X_Bldvfr5J6LncGc_N1hX2myxa8x1OZhVSJmkfwuTvWUXtIBTOlI_zlE6qaUd3miPsZ3V6LnyIEDbgi383fD9dgZ843ju3KibIDywRURIcvJR9Z0EelT8msQxW5eutm5PjRkJ71nibx2sPSixAjOrWztJWT9rI0QeQuWbIiHNL3LWFUl2ucBfADXbUR7CmSHyfL0cdzuV-RPhlovvkyfGVGGw6LHW_4ezewIr5QUYhWcfkESegGHIAG83dZRYVRLVcac7raGpIoSWznAZKS46dI-nNXGlIL0J5tjlb84DrScDlj9F2TjgH1lwugGbwTQqapb-Yg9pUYaeCEPj_igMX7KuihGpiWfYlbmJVyWh11NexPovwA5Ve2PTNCB2EKTofq-Htx70XYwe_-mg53U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=HBd2p9VFgDu_3V4V4CQapncWDbf9IHmQn8uZluF87qqlmiu8R7Ui4nfhwHdjUO9lFeONZuxUAAgva_4soOgZ4pO6D-YSBDZxE3P_x6YBlkfqZeYXeb0SJ_Q8Lsa1quQyS_78mcogw44fpBGp8MXbufiP-gC6eYkl19vqtp7vkO1ovmCAGatBQju2y_uYCnrC2Es8lcV2dwPO1wKG3pNei938DflFPL6n_o8lS8zNQcZa4NqJYTi-VDkuPArIEN4MUSrYtP4Ob9EbwFXchwCjLP-X_Bldvfr5J6LncGc_N1hX2myxa8x1OZhVSJmkfwuTvWUXtIBTOlI_zlE6qaUd3miPsZ3V6LnyIEDbgi383fD9dgZ843ju3KibIDywRURIcvJR9Z0EelT8msQxW5eutm5PjRkJ71nibx2sPSixAjOrWztJWT9rI0QeQuWbIiHNL3LWFUl2ucBfADXbUR7CmSHyfL0cdzuV-RPhlovvkyfGVGGw6LHW_4ezewIr5QUYhWcfkESegGHIAG83dZRYVRLVcac7raGpIoSWznAZKS46dI-nNXGlIL0J5tjlb84DrScDlj9F2TjgH1lwugGbwTQqapb-Yg9pUYaeCEPj_igMX7KuihGpiWfYlbmJVyWh11NexPovwA5Ve2PTNCB2EKTofq-Htx70XYwe_-mg53U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hlKyrFAYSZTRMdoOHh4Dkf3wtTjgKKpLwPURpKIYNMC0JPEGwH4afqDOa1sevFYTVB7VTqgZ1E9cjleG7wTAFaRPEvKkmSp6vMvaLKsreRznwuckG1t9OeMo4Yp4vxnoZ6KP08GH1AHSqqIlti0J7yxH1porPc-6CVyFLce5es4tUoO-_sAmFLeidFxWl3h13eTLWLM4H6rFPT3NMWDdEYe6WIC84eWrTtWTCgiR7syjwmzlqmKthbOZiWYToc-KBGVsg9YKlWHZMVSUB32aKRz9jWt2sntQ-7p2CHAU4wLHUyTf0vOjpLXBOPsOQJjq8KIHJwOqnyoscwqGuupklA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=hlKyrFAYSZTRMdoOHh4Dkf3wtTjgKKpLwPURpKIYNMC0JPEGwH4afqDOa1sevFYTVB7VTqgZ1E9cjleG7wTAFaRPEvKkmSp6vMvaLKsreRznwuckG1t9OeMo4Yp4vxnoZ6KP08GH1AHSqqIlti0J7yxH1porPc-6CVyFLce5es4tUoO-_sAmFLeidFxWl3h13eTLWLM4H6rFPT3NMWDdEYe6WIC84eWrTtWTCgiR7syjwmzlqmKthbOZiWYToc-KBGVsg9YKlWHZMVSUB32aKRz9jWt2sntQ-7p2CHAU4wLHUyTf0vOjpLXBOPsOQJjq8KIHJwOqnyoscwqGuupklA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=IxRJGqLc_vQw6e7S-LPtjkqaLcmbpNSWVsXEfbZfjVOEQ-VB90EhkfUzOl1dwGG6dyLYJ55465VeaoiJ_KZgvGCn-Str1Y8JZzFhNUVfOwRBSiTl9qBpzau-RMqBwbqowxu9Ey8WY2kGUT0MGuMWgFo6HJTQ2Y2dvZ6iFe7VeShkfPXGlaGvBkuC31hDH9HFIdQUSKuNXZGVM2LmMxihnCI49S_pBt0OlCT_1ze2SybmE5-UokWeid4oepcta-591R0GnKqBPm2cRmaa2anYiT2JrrtoCUyAcTqy_NEDmqJAVuaIR0lqdiBevP6W6ku56Eh2RoF3b6ZDJnOnOWuuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=IxRJGqLc_vQw6e7S-LPtjkqaLcmbpNSWVsXEfbZfjVOEQ-VB90EhkfUzOl1dwGG6dyLYJ55465VeaoiJ_KZgvGCn-Str1Y8JZzFhNUVfOwRBSiTl9qBpzau-RMqBwbqowxu9Ey8WY2kGUT0MGuMWgFo6HJTQ2Y2dvZ6iFe7VeShkfPXGlaGvBkuC31hDH9HFIdQUSKuNXZGVM2LmMxihnCI49S_pBt0OlCT_1ze2SybmE5-UokWeid4oepcta-591R0GnKqBPm2cRmaa2anYiT2JrrtoCUyAcTqy_NEDmqJAVuaIR0lqdiBevP6W6ku56Eh2RoF3b6ZDJnOnOWuuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=LL_fa4Y8F85QurXQKBZ713Z_fzdKXXihwN_39OGJinohzhYsNt1iVWzVWJLSvYAzVzYVLBwFuhobSYjUjJMNa-5DVn8-u3xfCpneZ1ilm09qepQ0_2PtxK2nIL6bcS5YChQWZqK66UpTa6z6ZCC1sNazjkyBMFvs4jddWPqQUo9Ge4DHkTjuZR6F_MdS1lDJ6nRQehcKIQ9kDVk8XDKfueZpLmlYhSIa-ZcTDGiY9OX0Va4BCh6YYk05OmQ-0FeEtB2bYrpgTW-D2dZ1BWjUfXr4KM2h9hw1dA17SJbi21DyMR62dsw9vpEisisxHuAlM3dceyhd4RETReqHnH1L6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=LL_fa4Y8F85QurXQKBZ713Z_fzdKXXihwN_39OGJinohzhYsNt1iVWzVWJLSvYAzVzYVLBwFuhobSYjUjJMNa-5DVn8-u3xfCpneZ1ilm09qepQ0_2PtxK2nIL6bcS5YChQWZqK66UpTa6z6ZCC1sNazjkyBMFvs4jddWPqQUo9Ge4DHkTjuZR6F_MdS1lDJ6nRQehcKIQ9kDVk8XDKfueZpLmlYhSIa-ZcTDGiY9OX0Va4BCh6YYk05OmQ-0FeEtB2bYrpgTW-D2dZ1BWjUfXr4KM2h9hw1dA17SJbi21DyMR62dsw9vpEisisxHuAlM3dceyhd4RETReqHnH1L6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooXPqvI1q8taXawnq1FN12dPEqhZLLLOH9FdAjS2xz6YfW1_72kw3Bmovod5L7KuwOrYv1pcK-jlY1NWC6-5KEhcwsvf5RJG9Llsk3Trkpg5z9X_u1uaEBmhFUcfo_qKjSNff4TwDiE_ljzgxlz1EAI2IB38wkBmIm8R3QFqsvhwCf58Wft2k9g8hXTXSqTymsQvwO3z0eOk6-i8axkcMcG0nadoNFF4SAfxi3nY9LvBpSxtZzdZ5aHVNwoIEkaKs2e7L9uWwtD9jgqg185fQcBi64msUvdXLwtuJgxSHg_M92R9OO9gF_ibn2wkLqZ6giqoGLgUvjS8-wPYgkvcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKnhIUVuqDA_mDbCGoyrTig3YFn4A600EBLWLTvHywe9kqq-qUoXkqh_CC9HE85IO9mEcbSi1tHqKDSBHlJJfCPQcBxSEJHq_1M-L_xRJSKadnINslztPNh_QgGTkvgAlY9xyTvejMQRP7lkOcbby2sHoWrbg7bgP1_OJrh1Q4dKg4RyZMrn6MqRGuNRmKCerPkYn7606tmoqfnwCSmPpwAF2og9GShE0fYFQgBBgXDcKQGH7S7VSzy9jITVlAchZX9guusSCXcr5D6eEyOVMxqm07Bc3hXlKdozQ3nc62f8hpNxNQNg6l95Pv4M5BbljfMXjYpD4VHl2fFMoX1Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afOzIKfdS0N5C9Dny499HE5a9pi6qVHMFFqre8-nUq9ht7aGoASBfC-vJs0cfAFjCnxUAUTqMZXQl4FTJ14OFnOkt6NbeDad27SgI6JqgJYCi0NDgEq3kLbxzKaGSVaaFMABOFC2VzWynsleXWUQK2w-qaHHNeC06ZobidwVZspOZY6daahRnMoohhZ8IKBopv75GKn6bLzRpGSAvSVt68HblCYZn9-UBo4aD5J8Fkhi7RGpyp3HR7Gd6WeBxqynZ0IWpuQu9CCrHIE2j4o4AfQfsk32oGbNy5jiz6lIfcodVMsVvuZKh6mnlplfvscnlvsfXSAnVrrg5Imn8aGFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRukd7fKxB4Eixlben6BHJT07f0bd_Oe8Yy2FkAMKGBywbyBwofBb_ztMiYv4InrDx1UKm4weJzm0jHGyzk2Wj8PkgM-KKnrCPceOOzb_yIFJYa87fK0JlcoUgAxRd5erY72rbDPGmFo8SrQGH0EQ1zt7YY9k4gvfhoWO8PhYdZM47RWVpY6Y8o2WmD72FF3-n05KYpqckRQswYNI9Ix4DVD_yraZbhWgqIzXwMLxQtA7EO7m06yzfQJyL6wAIIDKx2-Tck32Z929HT7zkaijIof0paPc8N-IxDcK5cx6hp8Qgkq4bC_yX865XWVaixXguh3wKSPLAZ_KB55dGu7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9yNl5eHJfiT644Y-Qakno5K6sKBT6Njo8YZdx3fTcBJLexurVMbodtpUk0xdV2T0Kec24OYtGZRv0Q71VnjUklLEqZRfPBkF82JjMRKzrjIxGL6hc9CtEKg4qnnf-sD9zBAaqJzsI-IxMSQ6_rJ4r-SO-IiAVaBDWmtrAsl1PzoPVAedMPwcjIrcbjhdhHexe4mFkGnogl5y6M4v7mZ5DoP0UbGi3zsrOjfAJGtBWs2v2V1VPJBlEQbnSdKj9xdyagkV5HhKzxiUTk_RZvHOkaUig24--1ulqlIX2oHDWALw3gVEfepf7gMPVuoZKbgG8FBCbmkrGrIzgpi_9sirA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_fzUZSVCuS9WUQw_SipkkLTpKeJYE-AMlv87PhiHBFKDJhePIP-J938d9bqSCkcPrNVv_KSn-AAyE8m-K9dqMNpzt8vP_jN0IwJSiT0FnqqYl1ocBm-DA6rBR6kqHFunp2m3G79yJfr9WEORd2fhH_J-1tKnynVrzlNUyenDHZvcylJmS2OXC-_rnjAEnly3of_DQKRArVri6zstATi8rONxLuMM60OHIVdv-a-vLF0NlouuA0fvxjEARb_Yw19P3TZlsKzyZHdk8KrqLwakRZiWiKWqfvDctUen1rilbmgJ3hNloTLZT9wi2gfOxiQN65Z-tPRJWlOmHBXMBXF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGGsJI8pGgotNR2SEhqfbKWxswd0fjTAMNrQ8G7KkAkyUSqu0EyusoJsE4i_SxnYzwU8rBSu0ye-VSmIQr9S430HxrfnRDyCzT4dF2VN0lj0MBN9DO6vhTzLmH_U7yA7eo6gvIuvQqOlyMDzTI9GJ3a7WSKmSWLljpem4krNbPR4_oM2pT6aasNcV6h1M9eKOSQOJcnwOnRepagoJBumO19IOfLGSol2IKqPbL5TZA7UKt_Uo4BMmBSvuQxPr113-jgmJt_8IW6k4Ly7piUfDmOEVNfEHmgtvVFUQO43GYWIB4iMQsa3-3CFtMJGeRAPuUOmBhFhh1HyxvrXhTRH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3gijX2EHPOLcNAb48Z07FqKZd-JEIzxmHEnBXQEzOxtAe19xEVpzW9tlfxaZSD_iqh6It3EWDxPrr5aSHyDRUisjIZp3Q2I6wc39NhxMkbh31RToCDup3_iSrN2Iek2-FkrhYKdtDETo-lfSke3FvJjcpM8OO--A9dSXHrt5LRp21Y_HGNHeG2WGQO50_7vXGFiOUrm6b1ngEjEE_FvK730S5-wsgbXpiNECcDwbA9eUluD3ovzP_rfjncg_IEswft5Cx5sN-ZQL88bFiP8O94VbrtFGy7Hu2VsvqepO9yr0VwPOYX6i6bqaTcxgat9_HrlwV8ZemAiQ4Dc5B5o-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_aWMaITcdUlpVzRctFV4mnJ_zpnc-zd9B9fzIaJ5W53-jWQWxMdDOHRQMraNYwSecSPXEmP3wQxSo0ookhfVxHIOTrJHrzLFMeBloAd_hgZom8lisZY_gZzckaYzxBa7jnAVSThph3HzwK43DcttMLKZGYkx04dEql2Z3oQXXUpe_qjol3mCd4rbvgvREuIgPbgTn8Uzki8OSa6O4SSJxJdb_ZniWUaB7gqZIuZfbElLJdHVNV8U8SnzinwH_3d4_Gf6zD-PrteM8hdsDSU_9aEJq6tNpymtqS8--I45pWWRNpI55emk7S2FtDUyh9mnTiMAvdUaUPBWBzRwKhhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOKYUwcjXlb5bTZgjYAv0vtjlZt_k0yakpJ2ESKOFy887FYaxJl7kDWbtwlgl12P7xMSKLdDcBEcKoTttiHhgiE0sain2wG__8Zik9MzRvH0RGcdL4wtVanRTWeACVYS9-wRwBV8rES4BTiTmDRo70uVPg-RbGO-AR6kXqHKq7nz7VNeIQilFPOrt7kdcbDilClf7s_ZebqipFXMik41W4cT8y26etCjQNR4YKvMsTfkX0MdMsXmMyh6LKZ3O6YtYux7x5ZvzNWnJoIfmk1pQ0FDYzwzBoxfuMMjAp_B1oK5GiCAKAKKioWW9gKoYh86A3Bc5dJRJYbwvmoa63N5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfs7GGHhbOgCSl3bb7BZ5SG5hbusuU6lMIPigdTN1mzPA9uvPAMBfR2rjPYp7-rxGJ4CF0598C3rXZ8LyqrrDSEDhtOdQlEvjISy_a2Ys6rPCntNNWTHGoLckxO6wcGrhuIb84Xp1ULhPpXGUzV3l-ulTnQCvjXhViswzXMQ_Wh1k2tCoLMdpULpRHGtd5qYuhvI8o5m5RjKCYKo-tmmx3EUIONRBlXaml_n1Va7DxDSXDGaoxM2mYUvhzxCz5obP3aD_JvuoD9aAtINBAh_jJcebZlD4UWQ3DpWTQz12fkCS5ogas9HfvxFrETkDR19tzA4g3i3M5WIKaHU0T7WBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN1LKNiprNgQLYjXlmhZPj5Eqzc9jtsjoDc3NZhCfrOc1FCGYY4Xgq_yU9jK1UE41ojofElyF4XMMkZk-yGA4yNFu4Ezw23b5hHtS08GkLEfjAljhpgHKGFpthM7d8OLWE4tEitQGqZ9L9cHEpS-1AJTj-bj4PmyJK9NucBRF5dDsX6_60wqYn84oM4C1umwySvW-hPZ6ae1OsQdW-eEnvALNBpoHP-51EFy7Z2is7P9zAA-a_QsFMp__41sY-e2V89q_IGz04xI82cFObx9f76owYP8Fijp1zPr0nftSNCaFO8yTIVLtk7UxQgE85jHmOuJqj5RTr4bIOEY_7AL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHQHs5moHni3Umqd-GYdV0ZNzzFTQvd-ZoIeormro2h-DU4DRanBdl9w3avFhMN5UKYoGLmWu0M4kqEIID3qkdPFoipBaBiiaFW5OXhsSi_oARzPDrFJSyvc3J_dSa9bAElZXM09hh5xQGcketpXqb7i4IpwoGnirICDUVWkS8MReI7-ZNFf0HC92Q3nBJFOWqpytAGw3sz2__a0oQW3Fik9-Qg5ONZER7bOKVsozXFvN5XqMABSFfNLGGA_sOE2GgtKKsrE3B88XTNEHA0YLfboafvfoUkTu5PWblLFatCZfJf-kF67NWtxTg__f_zWC5ZUzR98ut3P9nPfBoghpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=rfiKAwX23qUmAvqrCLW8wsmOFswXqs5_3CAktfY75ufm96xa80YySJXHfIi7oV3s5Zj0n369F45CacjZ4fE3ZfHyqKmkWZq3R1j0MqXXHs8fNbSen8_vR3G-eXwiv2X_K5SH5MurXQN5vdW7BOoEjly0TdzK0mLmsP_PJpFa3_HELcLH1OOi2dU3D-JKyZiTcxmEZNWrLoBnaFNYSmEkO_YFFQeaTocHT8n7z6RWLf2b36XTymOS1W82kOcKULPA4o8kf9_DmcJHXM-xpADDkLuvfUYPuyLeEnlkz_U5CiFoVj8pwyPDFuNSySEAR1Mofy2uGFKKNWCRYHm0Jpt1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=rfiKAwX23qUmAvqrCLW8wsmOFswXqs5_3CAktfY75ufm96xa80YySJXHfIi7oV3s5Zj0n369F45CacjZ4fE3ZfHyqKmkWZq3R1j0MqXXHs8fNbSen8_vR3G-eXwiv2X_K5SH5MurXQN5vdW7BOoEjly0TdzK0mLmsP_PJpFa3_HELcLH1OOi2dU3D-JKyZiTcxmEZNWrLoBnaFNYSmEkO_YFFQeaTocHT8n7z6RWLf2b36XTymOS1W82kOcKULPA4o8kf9_DmcJHXM-xpADDkLuvfUYPuyLeEnlkz_U5CiFoVj8pwyPDFuNSySEAR1Mofy2uGFKKNWCRYHm0Jpt1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I3-VT43WVupV3a9St6TmX8bS0obf-FLvIQtZVDThz6nCl8v2ICW63YVMaGHAVT_KgK9FZWF8nTZK-v0Anzc1ETPc_trNlVOiohkuXmlz5nlNhih5kZeTGFJRVFiwLKGNQgshF5t8iwKCOqxzjcFUZC6lU7Xx6OMRIQkeDyZMjL3rKiVnRVc_FTlF5N5zwHyzkivMH4ki6GizJjj0FmhPDtAS9yNK6VB1ftb7_l6Km-XPtHh43byyZY8K5CnOHQstRe31KdjMl2R3DAdlv30yTr26zJ6bPjq5djX55-ntntbSjwjnemrTzDG1ZaoKFBRwV337hFISGbkC3zp3jft8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLntFrru7YW-4Q2JMQQTOLwKdZTk_1imfEoGdfw5DPSydgP3QvFM3qHHVK9zoTzllNXwlnMj6thM7Yqx52yY6Li9pnp22_-a35jA06JT3-b7dZ3tUayIfXPZvzDeJywQ9X6cJzucGSZNj7_HJgzQzCQypZjMccGr5D5YABEaGNctZWC9loRnovqttMle_I1-WOH5Bc5Yu0_yqkkx2POSjpT76teCK1HGQ_dchnKfLpGS5ymQx90XhXkGwIaaHD5ijaXzHwgCFRrDZG-GPmShd50u1gh6HBV8LXvin0oESJoxZMeIVcfA9kmd0_pdIJ3Se6d2ke9s88xeB3Ru3x4FrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFT6TCpZ2GfHyEFuKsPFDIfFkeL7pCBywySUW1HEpXMZz8s1frWhySxGSu9_tPF9RRN3v0aGZjppAMkNkg5L8l1K5yN69440uTZEttO0ev7u0BqDZrcRzL_bPqRNYc7IzvMDK5PUJf2kqJRnlKJV-g3n1YJCDhHFO9D9szytf7JW6ynFNHH1IvCBvhEwyy3rItb2KIrpch1qM41r11HlFgBwaHrGO63x_dkvXvaQCuEMwX2UP87sY5xTvqYYla6GSc9TkTFPGY3ggUjFRA11XGUuAvKN8v7V0A08aj_aUrih5AHDpPG0wkuIEBgEYJLcTJKTkbZETDwgu_q2ShBGhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sf0QmweMZ5k_DpOO6H8Nn9UpzNRRt2bPk0WtKbW21No0_wC3Ph3mW7MUSCpBLo59ktbEBoS7t-r_brIrG5sJk0VMcWSthagUDusfuRwK5uyfFKdGhUkfUAtz5GS27q93WR0m_JL8RJxqKjR3EPH2l-hiZGcPa3zKWaHyyYrUoIgbmynpl70f7644utakj1NIkBUr6rWIVoWsLa5R0_yqNBU8MFm5a6haz6ZCjQpQiLKCL4cmwHutPSyi02Lvi11pSvhTV5wo_WuCen7mAExqCjdQ5E2UEtrYG8ksmVBQtGbvMbQOzb31SnCGJn1nEk1iDnYhYYWzJvhYjCziV2SaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tti016lMbBqf79N-Rbufgi3IHafrMHyUfuzruLTJdWognQ5vfg_1QbyeuL9e_Gz-tywYOvWs5kMHtg1ikg6BbhKIQ5phcapa9cuEcNeBknH-kkWnctysMNrB7qXO2s965uy2frFXy-JWOvPalA6nVkRBMTQuaAI19f9eZBUCb_kRUdp1Ya664rwzf5ZK5hUIVRB1mKiWtq5Zj6qoPL3UybT837fq-4xQuxft8ZDcGt7DVdDgX3YrRERbmvL0tLdFuaZnOnyTCl8SHgx2YINXg1wd-WhOoSwsa6TdXGuVMxIkv_y3emyla5hhVsCBGhSAUJdV4HWrGKdwaijLS_AMaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZceEVAdABuBPQp4PLagXDUUs2-S03b2hcrwV5FTWo8cjh1AySAa2AH6dpYef4W5Ht-X3kYJQ7n9FGCNWRWdH4sds0ZLIsqjObOYFa5ykiJtBNYivVKVaYG2KpEP5FKmlV2hS8zrSvRSef4Yb_PFXg9FbdsaORk_v2Sih9p_dVpQlN0exuhrVsiPZByVJ3zYsC1Qp_UnTxw5Y-XC_2hRqSpLHpmxVRZnicX-yjtpZ_tiyOvfrBrtzCoRn7gD7Umz9l9Aa5WUB5Uz3Z0XZ7RSpjKj-9ksWEaWMx8VwuDGrKiCAXLDNVgBGxeMbmRSg1IymdFBc0e0iq0tyQLIy9rvHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmjNWch9VkjlWhrtP9yeqQpgns3TDHhIGwO8lwP9oA9-y6YkslkYZ7U6PXdekFHEBJyCH6MlLM2Z7Uy6YgG6BuZ9eX4Q1i_KsDfm-bm8tkRjOH7Lzm6-8lDJ_CrfLzVNqTjmGvzv3TGeaZ5XItPVoZNTKhS9-67WYmVOt2MY98nfNzV0-Svwj07Mjr-sEUYPzpF9uXjuI99uGEX657tDEZX0HMpmfcsgPX8h-iPdZD35de6_TrBSXk7LYkowB6hiZS_2aCfAFq7nXlHNSSCYKww3XXqo0QeL7BMg2SQF7COqrI17yh1Ud7teL073iIZiu5BbvmdzqrFFSCs1mjWogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiwwqojbyry_g6zIy30FGDiV2PJB2dw0F2TxdbWfyMC4ngFAa4WURJRgKcrSIGDO1P1NM0Iygq7UWJZSnkYkR-d2X6U_q00HhNMDhwBrr_DhkV6WrwX4aYTzWQK9_4nSTdA-KRyb8zZitXagJRrFHXKCwj6vI-8bp2B8twKlaFKQbckjaFE0m1v7l05Y0PCz1S2Z0ZLEn-tYHBDn1MtATGiCuio12u_Dzigg66cve31aDhe5RXp8dH6o5rLNQpMWRYkiMjTUGNTmCLDkfg9_DD9sAwWhY8nZW0DkLaPd4xwgYNZSrg9ArSWzC4drYXe8QJvuTkjfp9NQR2iLChU9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=IoCzNYVuUhfOfXRTWAuGKyKZr1RlR6wSCiShRdX86l-OCBs1TvDOdjgO47ircc7Tmu9emuEX8nId0hMuz4lFiltG8xgB50yrD48ymn4XhcSnFwBLTI-u-NM3eyjGt7lRskLE2tA7ztyW5v4l2aCVDBAgQkQgrWlRk9eiUF_D5-003KEovh1k4Z9qe0SO8tPqZ6f034q3LiHSk3caGGo38WtuQJ-fwHqApDHWZK7J4vLMIrdQcbiTqe-bz0M2C_ccKWkj30LrL2YHZI5ke5T_4B8s05eApxms7RqzyzahSpfP3Ro6IoK4x1lGVf88pzda0QON4WZKA1mq6Aud2RKo2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=IoCzNYVuUhfOfXRTWAuGKyKZr1RlR6wSCiShRdX86l-OCBs1TvDOdjgO47ircc7Tmu9emuEX8nId0hMuz4lFiltG8xgB50yrD48ymn4XhcSnFwBLTI-u-NM3eyjGt7lRskLE2tA7ztyW5v4l2aCVDBAgQkQgrWlRk9eiUF_D5-003KEovh1k4Z9qe0SO8tPqZ6f034q3LiHSk3caGGo38WtuQJ-fwHqApDHWZK7J4vLMIrdQcbiTqe-bz0M2C_ccKWkj30LrL2YHZI5ke5T_4B8s05eApxms7RqzyzahSpfP3Ro6IoK4x1lGVf88pzda0QON4WZKA1mq6Aud2RKo2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNHqnH9ye06ZHRxODTL00AVIV1oseCNhfF4Uj2dSWyAUR8xo2tU-kpF8TPQfseJ5LhhCy4mpvhTRBIekDP84a1VjdUgSIzYrEPeu2FVtZ7-aHb7SiSWDuOeQ8An3fNwQBGEHQDuFuv54gO_lODAJI1H5Lbo9g_MLXU01SDnMxdraa5xOtb65k1YQu6rbTWCrJqkO0NIqLZBF0KRElKDXF993sjrXLa3PbekP4Nw9DihlZgAZprRXZc5c8oK8T8CrpgokjCkXZm1pKNacvCHjEKUnKvm5rnRU-yqttKBfl6HV0SB-il3wPydEiEl_KIrA1cDvfsLEsRO9My5UmBUzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqAYVf8WsFROjYPpTEysZbC_u82iQsLg_pdU4rpBeXJYKivG_ebic-9aAnfohePukVmuR0a_XiqJAcIYkxCDw_4fdFuCPcBcNVMokFTS4x_18G1Vo_-oT5dV08zOYgKivqoPzMF6bt_Qk-iMLOQT400uZWdQXlfDVcYLfiXUWHPqTWgoaLtKbLF6oVxwUTHVo4y8gxOf4VDZCmMR1RyL_lGSiszEug6C9gAyYmr7a3JQQWm4vL64o7mD_HHouLU2HYgQ0FABJtd9N4m-KYbdSCLOb080REGGrIy3r93xT3tg_d-y0Ks4w15EbmZY_tNMg5kJoCEv8RtFcO93eJ83gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9L31iaZCemz0rjwHqpHbEqbK3Rbm4SHcKr8cswK7zKFQxsA3R2DMp_MfjwZAhk3RBYuyIhTZEN14H5TmiUTL9xMp75TOfIQULadJrQs1F84Fooijo8QSMOfqR0F_TRxKoQXumh46eosSM5NczwiaeHNpr9bi6l9WKuiMG-VHUxqOqOmv1JWu0vHtJ4hqE0yZPl-Jr9EDszgPVGLMKfQsVOQVDS9_xhOHVIYDncX0evlQC1F6zh3ZUeL9ky3Mznfj5xZ5Rf5iXmue7y7s0DyyfD78AUx0z-zXbmajoBJ_DwrCrd7TefYe3Fk0lxXTBjEj8zpvAaZ11QadVlIqzUOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlrH0PZR7Cl1u_FenqJrtCsnc9I7BbSoAt5KqSdvkdZZKsFkBNWMXyeDpz14j9xkw3vDBnMCs2YKZNRR6kWj5tq-mlI8eugpUppZMvrC6C7CyEaavW0feqULvaOU6sVEDtq8qbigj1ZrR2wZRdttv8QRTT_3kDZZrDfuDqPo4g2IDpJSeG8ThIlTVjBFKZ3kbTakaGgBdGG9WSN4mk7SWwJFjtTzts4ZWiZeFTkegVpvD64ycJ6Aet1PZheyrlkfvjZHWFKnQcQvKe3fuYeo4-CjX0kyaV26AuEW8y1JraSvia-PZVG3efKUk2N4wqAq_i-mNqcB0nR-MUaE4kIG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD_-V2T6keVlVEA5mysYO4huoG6uv4MhjbhdBGsedBFw115mxXSO4QXNmZPU5QvhX93etwd17Fookhfvo-DHV6nANZ836Hn8_m98YZmtHFz8zZPlWQZ3kf7JERWtxzVtaLfP5sS5b35fG5BeWZ9rkWD_omxVwhGFUe_haE3zFb6pmv1ycwuflxnjTySWqeBDeP0hVTsRP8fDFwsrdS64AGOwdCbovysvssqpPS7rcCLI_wibffalNKdnLpyih1KE21ZqOZnpfjfJ0g-8-1F3ECKgVPmkciE1bKatlLO32vneura6ofPU2dg9FWC_5j0L9w-iyO1zXDljKm2Ps2PYHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTA0wL3Q-0JLK8Loc-1C_BkKhHX-DscXeP_AGb5Jj0nxiZziUE6P5gtZoGKYFrjvhTkrKE5NyX897Hki0-8N0WffzOH-p0mTbV829Y8fhOqXydIAk4x38GSO8dELX8kKkbO-9i8_8ZjR0Ldcu01w-9goZLtxvSuXRctXuDDBFHfrzBBntGbaGTA9_XN7fodbUX1EcYgxfHLEFX209mYhlNw7W-PJVqyAADB4ZE8JChvBxaL76i1SPpImKxnk3n3xTklej32GzRT5YIrhhsE5_iQTRVcSXIa6sZ4koiZXgblux1AbUH0NqBLslHfOa9040BrSOLYUgGN0qPgROysmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJO3anQ9PDiZgBc5xJiDuXKovISAa9GA10JjzBhWfzBXWwi9yhpWDvmmzcjN1yyb3DQqPEBDo7i2oHFDkxcHn_VV4EBUQSHfH7Sd-aMX3JmfWLJ5Pjl3QjReK9xMzKARshoc70xCEgPOFhMpjvKg_4cHkxH6QEcToVuEiBTq9RlU0mM57whti2w_FpNnRR-PSzcMqXaZN9DthyF5tnSEhTmI8xdbKUXDCqVeSJ_J4x__mvXDY2DeVHgt51mqZCOYe6XpDAWWr8ORMCacW3_Y8zEPmQ_oH3v5CDj5XazAyEojvMSVt5-Gns0N7cLIAFj5VsO2vWUgFVSirwfT6nW7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmxrvjMXxN_sv6XzwZOqbN6HnusMgF6V9KPvWBYN7o3IKjE2soOTqVefy9iJCoxVm5vcQBo5QzDzeUAAIQyFMAV-_ZqpVJqfnIYYR7UdWDjlD48GimQ3at1REETLUjo9ocASWMribnGmpilxO4ye7MdTGeQUMA9DQ2LMJrY-7DtgXehSNrsG_91XCE_xID-iiWgN7wKG59HhxCYMX_u1YfFKqedhFo93BR87A2OBg4LjNpbruuVsIRzzEchIpxYAG9FWrVtvMZ7lVUd4MVbw-oI2bw4E6OwgRjfq3iDHtLdHN8y_oxHQNQeHCNlsuqwN0sAWISB_S_4Ee2afuE-kZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmoNTQWU3ubTr9mdcQFMDCbaIHYOMPFKwET7ZP6RFUKdE-SiHXpIg75kLc0Bh7_DCRHX4IwT1eRwuDhxiVJsxYXRU_CMfLInp-smdPbHwlPykF3v9WkCv4pLT3DZftBj-cRJM-rBa1NKnyP1pdGMK_TtxKvprX852nnnLAnOx-uYz7dDMJjupS3wwJLUdoJ5ylPWL-7j_yKOlZPrNkUFW0ua5F382kxnqcPP38oSzl4ps0_B1NviEo7wDctVYGnQkBS0c2_W1gohONV_iQh6C39dv0VVwrsSkyrhDF3K1wQFonlp-JoTUUan-2qBYGrlcNmhRV-2pn2HjwTVXS-RwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=q78-hQ1oZOrCkK9yDY8gTmvNhMq7Vq6GJVC0Aapz02_xOjUy24FhOK6T7TxsL-nQ1hv9rcAgmsnwZ4uBe8jaNUf91wq8GbTEd1CwbxrB30jTaxbc2VdPkTKzLtDpeVC517w6AaBbK87RMaHAoq-g89BadRfMGF61-ZMahcBshKcvdkCSfV9BndlI12QiqxB3smmvxlJPmVEgBkV_wfsLwe-FRq_hh5a6570yE3t4MN3_C5Ky7fLF1xQf-wcLtrCgUaOydureC78M_CnGRIEtui6arexc_488BuHzfwhKOpj_IQbongd0jYxnd9JXfBbCrtjoefwxZM2JlWmFT06nUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=q78-hQ1oZOrCkK9yDY8gTmvNhMq7Vq6GJVC0Aapz02_xOjUy24FhOK6T7TxsL-nQ1hv9rcAgmsnwZ4uBe8jaNUf91wq8GbTEd1CwbxrB30jTaxbc2VdPkTKzLtDpeVC517w6AaBbK87RMaHAoq-g89BadRfMGF61-ZMahcBshKcvdkCSfV9BndlI12QiqxB3smmvxlJPmVEgBkV_wfsLwe-FRq_hh5a6570yE3t4MN3_C5Ky7fLF1xQf-wcLtrCgUaOydureC78M_CnGRIEtui6arexc_488BuHzfwhKOpj_IQbongd0jYxnd9JXfBbCrtjoefwxZM2JlWmFT06nUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcsVbkmJlH2AC7QeGgwGDz-eRBns10301aiGGqhL-SRSRnJVnZkOltqqTC6zioD17CPCd_cbMfg_RmSjbu_2QTj-nw6kJdnAhwW6TDVxOOhdLpI_4-IN9XrzDT8MlVXkO_0eSP7JZuUelzDzn1FqIqcMhhG2au9ujJlQzSyP-cfcc4PvtnprpLYyIMqVQnJkWOciyUV5qDtUO12UBwU4jKzTGGy5mn3SAWMyAvILOsk9t7_z8MM87PuctASRCYkUN3rjsIG-Ll6cWjicJ_aOGErPE35hny2oC_S_FQnlYNFcKFFuseUpd9adxfodLwu5W999nMT3aphZjlQVnik3CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcdqw1aA_wK3xqBCjpiRjDJYPdSGup-Zdyjm7l7tyMaLn2PA7PMv5VG1Vi2p_4kn8JMnSAzrH85pGPp6q0SOCE8E3S1PwqsvDdQNcbzbSMiEzFIcRgIa8w6KMwJ5G_3tYrUG2JQq6SqG9U2Gde5CQTtPTSRkD2bCuU2L6_B0mH7VSVLkF6BbZR-SWdVofCWrJS1pvcEd18YAxu0sG_rPyrdkh-EZHa4ch_jisl0hmF_hkG-SlBb-Iwpfh7p0WbZoR-LvxLJHsUO1B_4Gfrf_A39otH45LWmjdWO7ZQF7u_uxkXzuObrbBWdrDrMdicGX_WI_SFUThf4ZiPy1u5qbvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=cf6MO8LqQgsgjf4IX9iu2P5QIMPIALHRfZXHJIgEaonFriroJ-856CN1zpryEM8VVS9w58h0eFmXvUUj0rUqwK8kahMQ5BvOxoz38LuKX79I-YpQ1qzD3aMLHie_fXh5cFob20-KbxsRziTrX3Id9BhiUmhIhg2En7ngab_MY1JE-EZUtdvaMC7Nd69dDgDKe6zUycIQfQgw6DYTtfX_Z0BJB_d_Co8i8APQl-CBZ-12BooD3xrSogQjNocF7u8GsJwRf8ps988Jnj1vjc-1xtFP4A1LsRAtQMZSkPqt3PfxxNAWprs6Lgdxhp-KxPhT_fNpQhSBBnBtUAvOyuiunzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=cf6MO8LqQgsgjf4IX9iu2P5QIMPIALHRfZXHJIgEaonFriroJ-856CN1zpryEM8VVS9w58h0eFmXvUUj0rUqwK8kahMQ5BvOxoz38LuKX79I-YpQ1qzD3aMLHie_fXh5cFob20-KbxsRziTrX3Id9BhiUmhIhg2En7ngab_MY1JE-EZUtdvaMC7Nd69dDgDKe6zUycIQfQgw6DYTtfX_Z0BJB_d_Co8i8APQl-CBZ-12BooD3xrSogQjNocF7u8GsJwRf8ps988Jnj1vjc-1xtFP4A1LsRAtQMZSkPqt3PfxxNAWprs6Lgdxhp-KxPhT_fNpQhSBBnBtUAvOyuiunzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRkKpGq5Vfr56kbRHB1U4UJAr597XokHHdcXRbxlEBjsBoom7Pyh7Ukl4nHsahvnL6t2sM-yWf69vxOjTKCc_wLPnm3-7M37DDu6iDvAJui_XeoOm7cJiZWqpemgqR4ADzxHq_Bo8QwjTP6w_lAKFaVp5Vy7Qi3P6G0Qe6spnI1FHZJjdVGErz4pPwYsercVdEpA-yM9OO8OmTc9sQaQKibKXwA967KA0WY6FrU1i4xJqFKYCERjajfWLNEsXfsdUYj4ChUTt7SdvQYSaKL4q1qVgUfmY_CxjjUAjZch-RHw2mCsfjbSCT-veuzi6Uaj7kbt8w3ZeEWgoi39H9HSUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH5uII_FhnYpTTe6_ZQuO0JLvwWTvcZq85EiDYKSInkivXCW_3Q-EuCdHJv8YZu5VvyGlWxRqRnISiuwZiToOPiWYCXmTd3lNRDaadeFO8sfQtuhT76bgSM7scJcjSq0TfL5rBp6LdQ0ljpzN8ivPeRTeyCW-VCp5X2cYNMIthfU0zmCEmNl3HMPjGeZC6M_N_f9kCKe53-GDDhUURA2EsoKu0ish0YlSq-ZOCY0fRWcD-8hA8hs642gixc2EX5nxOjcgiuFka1WDEOeo2yZizCBSIDbNzMVVTlq2LaOLmA2KZvUE8GcbXq_JioNOf4nflh9gw1vdq0l281IhqSP1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWQQ26ZXfFD4Id7vyz2CpUgUQoHsebcavp3fM34lLP3hCFW3Cgk4SP15HLSVK51YGsfi3aQdV9zjttsWiR0me3jHb-5INQ1_prvou0cVV0PWpmqJX4tGu5-bdQdy6V55nnW3DbbAdKeGeszj7aC4fmSFKUDamk9Dz1hJiRmJlw2cwVN7E_2OTLhczAML-z1Q6CarqpQJWGWPIytHJeS_qHBGKBAu94FgmRXH89eOwo5jwcDfw6nfhk6m6WzgaCTFt1PMLvASE-q8hgLpV3T0d8epa9DmbKyOAMts_zSXmYulB_oTzHqw6rdRnBx6AU4tiMTWgRKrO_i8-IRYQ9hrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF_ub188lxMWG2H-_54iVQv6tYKK4wU4G511YaRT6tnCJJvtAT4YgexIYxriI-28q8iH89gwA_j9FYvkaoZhAcozlGq3ItoBc1bqQI0SdfGbh24cVu-uTqRIsuDqtLaHlh_smjtu9hcGTIuIbzjsVbwWEv7SG6QY5mutSaGmNazVJt4GRLXTNlJec7j1Cd7YHXvXMbpGWe7sgLCMvJT0fATJaSbx1YXy29qklf85zGSMr-PxuBhTmm-RMiLoG3AODMHc_VsPRYMumTb_YVeGGw_Cyti7GGSmSz0vovy_8W1rYshL4Yjj_QnCPNLaPDDvt6ZDxwwxgKm3sM-rPXyRSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXWIf9U1uG7pHhivAk24P6KGJW8pH3jGwHSKU_AYBMMS-edRb824rmbcBMNGSmKkkieTTBS4w3Ko1GijSYeAz81hxPaRYOwiEXEtb6WhJ7h3O8JOarwQNapkMPYZ9CO93pwi_4ME8FQbYmBoB8rFXNYHy2YzyvV70szUW3dE3ffN0J1fDx0utMu9IRqjcFz81CZhmfGC5_t6a4qXK9Csa-fS-uCK_WMGGfHmWzp0a_1jf2GraTsodGYgUA06gEBtySw1dxK9huCs2zH1VGtqrCzWWXjuf1WrImTCg_wbPWLzp2WuYxozuJc95NyU4BswhEbLSljMN4sa6OHGDy5Xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ‌دست به اخراج گروهی از شیعیان پاکستانی مقیم امارات زده که برای جمهوری اسلامی تبلیغ میکنن.
🔺
امارات چند سال پیش یک وام ۳.۵ میلیارد دلاری
هم به پاکستان داده بود، که چون پاکستان
آه در بساط نداشت، هی تمدید می‌کرد،
که بعد از خودشیرینی‌های پاکستان برای جوش دادن معامله بین جمهوری اسلامی و ترامپ، امارات بهش گفت سریعا این بدهی‌ات رو پرداخت کن!
که یک شوک عظیم روی اقتصاد پاکستان ایجاد کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/4880" target="_blank">📅 12:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guN87_e4kExi_fuDj1jPOrkXSQJT0GfvRMU_EGGDh7U6OQOtrJ6-TQuaFF3p053Bk08Osx-VvV2DauuBN6mA2qmlvdVggqums4DmIj4WflwMcMCFSFuyxmS2k9pDft93QPZpj8rZnnhGRQ92YxzUmQA655-mtHvfP8-Ms8P8SXkOtndxLFRcT1RZxRotwNuqE15c0aVAY4CaK2GmvnEdyeN2KzmBjEK8rO2J5SscjvH1x2QUWjOAJQ4RPtVWwixopzC2kTb24aB1YIkot8woLj37GlxY98_eo23RpNMzPJf-rr-RW1SzkHmKiP8BVK6E8G4Pr4K24PqABXfYxVAdRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu848Z_PxCDR07bkchm5vsX1KNRI-kri1wtQVCw_JVPJP3x6QUn3lKtPOWc1kwcY-n22mByESBxljv6cFODMKcohQlTSa5nfQxJQH4hT2z3CBg_Z_tUp_dgZL6WdGvWrhbGbJzSHo1bQQ8PisvjFgq4nTL5nWlMWIjGQWRl67lecqDH5xoiI54NoFa4u0fe53HXQmpf6QJk6uAMHT6KfjOOCCxybEhoGDvzZiiv2acJuJj7c7tP8RCrCTNl_eW5PpsmugbnV6dYxHlAELn0wXx70nskHi_nFpa6On9bDSO_i3nNAxkQyaiWFUeTL2Hco0X1mHBAVtxEo7JQQ63_s5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9kcRsAG8_v1fFyaOoNOXspx_t2eKSJCPsdskWKfl3COWdncG_ibxQ40spZ3mFwdBFGf1mr-a6zE3vYygzo-0iRaa45CFA6mUNvoSoYhYdnvswhyj4p-1fx391ZcoefA3m1wjb9zNC5c6XayUCltq_fv52uo81DYQPty0Kyz2mnlunTv0AEEmDUkrhUxiEQlbYisLLLPUaUBaFHQ4pVm-7pmWDpZgYqEsHEjy7ajzMhEVQhjyru3mzlt26h6b72X8NyazZEK-skAs9drq57jLoHlaCFsAMov-hwTeDRkGhKAIUFQk8SHFuzo9qVm414diPYeLA7fOvq5FtE1EjuTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAHhx0O_W1Eg7WhJDb9dyfcP98cfjdZ3-iSKbwz_hUjyrvJffdy_XujWLFDbvT80CKBHvT8tpq7DBbMYMt4aSyLU7NfOKk6lXE10VmcZzFYD1kR3NmkApRP-lE9vgI3CfbPVB5luY9eiRwaAsDRkX7x_6rwdIYJkBUIhe1K5y9kMkiLbNkwHA40PhLRYWx5HVD5CVQjvYtz8I4f1dxesnggOqFckbsT2_LOU5cEhg5x0Cg58l14R5B1zvypcqXZXOzRe1ozB0XkGMAN_G1B1uJVALwAvwyRMPyj38oWx8CyaY3dDKm6OyFWA7ycBNaNdCw8Gnj72nbCgU3HwagPBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRCDIuvb8EWcj2eT5iv6NY3wM9UShlmy1gSn44cq1xoM09RhCwXxvBJwc1-qJTmvLDXIZcMgPkLBdiCDxcjBr-Lat7zXk2NZ1Qk8-cOKUwLZNOBcGZuER6JkEuCb9st4Hrwek07cxcS-EaOREg17X_3eLCEY0m5wQmBe48m-BPBkzuD6d1ldcrSjLzm2AuZLrCRQDvTkxNpvhbRoMqx9-CCpi2QzpCt_zGRQgHoeNjDtJpVMtByDAETuJbM_8x-9rmWRBCWSE0WEofV4JubTG9mS6y_glBd2RcWl1pspvVBFUS7L8E9RCrHJ0jBugjY0X6JGnXJwSs7H5nLiLXaUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdLnT2y3Kt-37Q-9zp3YshryUoeUrAh0OWiEucTUvepKn2vD96LAqrNvOsBfU0ZZDD9NT0TJNF_WXf0CvAiVw6l35lD9L2hT19ge-EgCgtwSPS6RTCLiIqnmj1M-43lKoOk1yXFaLiuPXkfAs81YRuD9fglG0pq5lV7B-0gi-TIJRtSNBN6CqqG5E2o-RPpQ1qmV64twH0TgnLArmUs9_XOqfPdicPZfY6wCn9ldvu0CzXu8SUnfcfPH58dC5WyQ9OdsGE2Bt1P-5x3JowyqrcLyJiWp3xf5OY8BgZfFhH4YWVXTjMJUOe71FKQejwSKlybODxVtF8TgeKP6mZf63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhTbrAss2eW-troF2_B4SXT6RHEOoOuPBPxY9rgv2ke_SoLg_UHtUPuYORra87zdI0wEk6H1EuXT0bRAILX_RDg8RHJS8fPmcj5vsUqbixk6eg3fD5QJNznNptBcrVTfVG0j4Vkzpt0NMzlorqMNvwAPM1zTW2fC3NTi0IVElDUQxjNGZJu2HjMWjpqRTwfn5XvKi97ps_ovCfKQXEvE_DRyLC0QLPBv1iEwZsPIX8MTVEG_VojCLYGimGYx_v9d4_5zHeDK6GdfPKB7ZZqEqjLNH4oWg_s3XGi_il3d4xB0OJbNsZQBz1yJ5JGkTGnKo8eod54YPEwYRIb3awBTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKu0i0klWG36lu9aDjinReJ-XIxOtcQMhGJ3L3tFwA1q0nHFdyhMDuRQHUi34R0iluVXPm6RV0TlI5ZaHyGtRUJWbVfa2Gp556TjTFNd9K2KE1SFnpJm_yl_0YmTuQx4jTtkAiOEmKCcr3ymmJNgCfvLyj3rnLcS4oRygBupzclATxWtno9I6cMwE1vEehrJU1mktUw3pTb4AO-t-M-FfLL2VEM6AfpUeB3_XhV20POKMR7xdi5Ho-bd6c0Xta3dyg1EesMVM6dkdoPUZvDIwpYJQHw57Pr6wJJMFX8wWVuIvQ1snbpn3vnMSrUgUr45sW0ep_JSWNVdeB2uF5i1Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=Gr2TrAtC5RCo96uYaz36ynfVdYgKrRitbJ1-sDywzINaTHIk00q14FFAScLEG8o_ivfOD0I7czloTy6_MgBX89X6AySI-XwhSRPC02CWZWGgOy5_mH6IuRiClWtmfPuu6c-ZXwYPsDYXvrQt1Rdg3lDDwChJbDaQaaEqDhKwUHEDUkqrP9BqMN1Ne6eUtA8BOHW-BI3NQCIPZqHN893NnQZPBmle_Zkkd3hRe0Vo0DgHvF2jNGOewG1Jf_yIbU0XfRGEGP_8krr4F9Iz2cEVeNmsLNu4kw5lzswlF4qkSvBlliilW3iiNdduP0j5EtDL70yleh_fD5zGl3hxLVF9vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=Gr2TrAtC5RCo96uYaz36ynfVdYgKrRitbJ1-sDywzINaTHIk00q14FFAScLEG8o_ivfOD0I7czloTy6_MgBX89X6AySI-XwhSRPC02CWZWGgOy5_mH6IuRiClWtmfPuu6c-ZXwYPsDYXvrQt1Rdg3lDDwChJbDaQaaEqDhKwUHEDUkqrP9BqMN1Ne6eUtA8BOHW-BI3NQCIPZqHN893NnQZPBmle_Zkkd3hRe0Vo0DgHvF2jNGOewG1Jf_yIbU0XfRGEGP_8krr4F9Iz2cEVeNmsLNu4kw5lzswlF4qkSvBlliilW3iiNdduP0j5EtDL70yleh_fD5zGl3hxLVF9vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4866" target="_blank">📅 12:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZ22m1WtBIldpOMNw6afCaJKOW-Y308XH2Txb8436bVK9hJ-MLtnx8TgcHChJDZlZ1y1WBRXXVZkCfEgXFfMp9u8WcUY-6YvAhHLDyCwA91v2n6eiVmp-jDtzDWb-v1S1ZAHEW5wbpTVN5mBDVska59fzAffYqPmPwnYPmLgU5CMZ0oB2ft_w9iHfw4eeDcs95IXf8NI7cZ5o2xH0cpC_-EUFU9hdyEwbZnzIioVu6JA6DKUtlE6KU5NVGmR2_UuHnMptZ0-eOqTqtEaiMzi8M2q1pTIfXX_h5F1DcPznA67OL-K6nGMHV1w5SC_DBUqHhdDrj9xJjEoKAnUElZfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfcK4OCpwSBmY5bwmh9gMtLZl-bPDmecSoXaOrhwH5fGPhkIPWYp4ud-LgI5wGo0ksJjctPp-DCzCYaoTZ8u0uW0w_ej10xI9o5AH849yFKsQzMgfzYm1VOF878Z1klQLjSd3-j0YDdnwVVddZnBF1fWAs--zE2a8nSTX3aIGU8IuJboVaPw7qA9zZKT2lwvfTMgbPCOBz4i1qIC0753KSqycqrRBUZPHJX76Phhh9LA88vklD5Liu68EMEgqeWWY2nAEZhRktY1gXhC36EtZU_JnzzqysFVcO22IZiQyMJSq_9irUBUBgW7uJl7XVs2FHQ7ZLjp5TvxBsL8gt9C3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpwCN87p3OFo82hrQz5W6R59ugCR_aPoLyGzWmYdk-bZ2oL02bBEqUs4jf2CXX_0VuuVbZsEXtzBkD5rAYgnZvtygobfpaUeUDxa4yuinCn0lQm1KMI5kWoz52af45hTsq_faToXypzeyqwc_ILywiCxpvk-JHGgWwcN36Ed2OYosV-1FQqJy7Upy14IovTokA-pYCNaIaXWKu461sftEY3cprwfRHry20lx9HL9uh96_xkSLUuY4ihR1HDFCf202oB0weWFFnYx0-VuhseiiQ2KeqJUMiPQhonHGSFjhNa0ajpIqJZlio3SOG4YT67XPOTOnfpHptp4y_jMOOICeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vg1KgO1Tr67dh-Xkyg0joTUPw-wJCBn0w8Dr-IQxk3vqOJqj_ZF1NpQRsv9Q9vK_nHpev861w9TVAZ64Wq_P4UAMfZ89X5YPPLeRLCabBZsmvZClyYYsGX-vGNKGU5ISg_Tg7lluqSFnzXqDFm8OJWUqfMd9hSCbrtiu577QXXn9uWRPLk0rMzhchdJLHNF79iWXU8oe6Vv2oDgo5tHSHaYX4EPoJGFePxtOhF0exXa-LqQVJu5oJOMin41paqQvIziWs749JnLsDl_9V9QcTROSCYqPHiNbHAXc7PRJ91M5Ym33z_CAgt4AajXyt74EACSVaXhkO9xyCYJOwtzTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhOJ5lSZpy77BYgfA8lJN7g6dlw8zPziKr3WIajB9qmPD72ZOacqNkrnLiUlv14OAHYVUGwBkgKmJIY6aYgs_n4oSe7Ofac7fzk6b-_X4ODQsyYhZmwSwHpwTAQtSElMsFdF30wyMlcWp3EPM1Pui8T2Of6-bj6608HHN4O-W0rbjzKI0-HuRxhsghyjBXiGRbz2ceKW_xRz0wx6t6WDHCdyZ87-dPzbN7KaaO142IXTU8lVzFBjZeaoYvHHmr840Cft6P15Y60lYxwkde8kQvKD70PxvZtcQyWdmpd4lyG_GkjGeeBfAGraiCGqCk6CDmBbTN8vfh_wb3t1sUTaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnTIp1zEpozdM3FAqrbE8WYiXsbE6l4Hov3yJQX8sEY_lM96FiQFesEKWQ9bPatmTff-x4vxJkuNuMpBmIOlkgj3R4ceHhuiKDupWPI4wAXLAiB9bSCIWT1yKYHcLgYIGS0MCJFGQHemYQua7gcOaHmhjMEtPAva2T_47Y6uIiF-zTPT8JbGkHHmr5XMSyE5u7Wn3b24HB1XAa0XipMTG1EEKcadu4bv0VzQ1U94o9ubVttX9imY1LAT_WclAA3rth6JNNdtgeRWGYjOWm61KkpBgkiako7HCNfVoxlS4EXHUqIidvoys9ZIj1dOQ2K2XusThaEzTQJVPyHJJ9Isng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucw3Bqfav_JtOxj4kW7vlyo10TGm9VDoZXDbjxlNzapz0QAMg68dzUiuj_3UWqLIY_TtowKsVQPpDSWrc4jgjq2gN1sT1rqrpW4wGPnLLdvqR56DN0TM_oEXHAaxfTO-0isPHb8nhUsMdQIQ0oXOJBGJbTmDRRhp27crYoRjzhLRn1W1O1iH3EfUJcPpm5oXUkfqiY8CyVUvKchTlzn_qDGnAFlPbhmfgb6a2getTTqQRmzJyo44V8h_G0ZZdaUZhcRXLIEVh7PRoP9HRu3nnOhfVfQlhsulRbniAIj7hfJrGEmEQRK9qAhi_VtmiLJSmy3YAY_4ybPNtQs2YLUeEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoYhiiG-nYjX7RF9GWUMPVK7V62UsF9nm5B3UCZJ_57A6RL8HdAztCaWn7qfRNeqOOnP4c2ZC99utyAtnXHs9FmrCInPk9K2qxRkJAa3XzduIqaoIpU6uAiEBkwxmPHtox79-czOMAZDKVAMXQrXUz_FNCjpuEMUuK3gFqNdm3ePg-OHWJLG0D0FvAjcUBQshR4xbxwG5QNXNMxzsJmaQfiMe1B4IxEOFyM-GcSW4Lc_e2Iqc-ezGNK5aB3fwUEL9zLQtT3f3xhRPll7dB-0R1XH8FKJCatVBI5Kjkuplr5C3l9mwXYKnLtnCIFxc06e_cvUzhkw5Dg2CuXGmcX_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4857">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b31Gwjqqi--xuqtOf7XhMYilvpQtEy94_vfvg7AYws3jI7859EQKbyunPFjF-U8B3N4wYjVt1fkccHUPn1z11OrNsiRd8dcUkgNlcLLox8IelJXYCbNUt0gZgMajR6qt8qwgAqJUo2gM56U_cVgkDOyd1gFc3HeHYBhGcfXFM2wkGKi7Cix3u2NQdfbvxQcgsW1H0TBZ1NhTVZyUOvxrwYbRNJWF0qwpuurg2wotymFyGsKeqscDHU6vQwi76HL5ak6-I_ikSm4TEqj4AKXbUfev7aB_TkwyGut5_UH7PU1LQTrQMpuH6h1czQ3oEZ9LjowSojTK_y0OZ_DaPG1VwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه سنتکام : سه ناوشکن آمریکایی در حال عبور از تنگه هرمز به سمت دریای عمان بودند که جمهوری اسلامی به آنها با موشک و پهپاد و قایق‌های تندرو حمله کرد و آنها نیز به حمله پاسخ دادند.
سنتکام در پیام خود افزوده که به محل پرتاب موشک‌ها و پهپادها و همچنین به مراکز فرماندهی و کنترل و مراکز اطلاعاتی، شناسایی حمله کرده است.
بیانیه تاکید می‌کند هیچ کدام یک از ناوهای آمریکایی مورد آسیب واقع نشده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4857" target="_blank">📅 01:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
تداوم درگیری های نظامی
🔺
گزارش‌هایی از حمله به بوشهر
🔺
گزارش‌هایی از فعال شدن پدافند در شیراز
🚨
حمله آمریکا به میناب</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4856" target="_blank">📅 00:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai4Jhja4L2ChHTGUVZnK7MfaJb2aTINv--7RL12uN54S93g9JDtVTU4MJYRZ8VgSbBz5aQf5mxEcuNf5IAiND5jc2Lb52Vwl3hmmLUvDArxOlqjLIyBCemQORWgAYIbgdkr49H3fM-8TEHlTJ31uZed7HiOFLro19LGCIgV1PVV0BuGf43RNSd9apjnG9GgjJXB2EU-XD19VT2_FmR4QZzDVPdKVt-VcIvJPbLdxvI9znKHWeJ1NQPg0jU5VvZenJDbsDyO-lM1LC5QV7FyYmaeVUL86ElyUtLYBsh5ECiwsgjIhcalTuQ2LZT_tXRMqMNN7mcCjk3ysl7leaVXKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: با تلاش شهدا قیمت نفت رو بردیم بالا و به یک دستاورد راهبردی رسیدیم،
ولی با یک خبر باراک راوید در آکسیوس [ که خبر توافق بین آمریکا و جمهوری اسلامی رو زده بود] قیمت نفت اومد زیر ۱۰۰ دلار</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4855" target="_blank">📅 00:49 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
‏سخنگوی قرارگاه خاتم‌الانبیا:
‏ارتش آمریکا با نقض آتش بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند
‏همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.
نیروهای مسلح جمهوری اسلامی نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4854" target="_blank">📅 00:37 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
