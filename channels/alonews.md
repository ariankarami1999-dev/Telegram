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
<img src="https://cdn4.telesco.pe/file/DMbufwhNWVs3kY7FiJwsPL0X2BHS37_PSpRVEIegdQ4-vah5PTwd60Jo7BJUM3kOUUvZWwzEWfsehRi1krhM2UhcbM7YAvVuJPLNaXoiBA36D6J_GzTFJVkyKkxNpK-ECQnvBRMAxU9MbesR4Y6SjMUBebwVj7ADjPL12um68FQ3u0p6bpO3dcCfddelBo-MHKn_fea__-HMTgvbR5mTbauUwb3lgulNlcrFRxOehSqQdVshzhTI3gRlyvyYv079jyPZxdeYvw4nPI0EAdgEt9DMhv14Fq0iL1uMaan-xytx3QW56RiQxyi5cjJN3I5PsNge08GR41_1PksoyvtJ9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 990K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 00:51:44</div>
<hr>

<div class="tg-post" id="msg-139501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ظاهراً مسیرهای اینترنت بین‌الملل زیرساخت دوباره تغییر کرده و به‌جای عبور از آذربایجان و Delta Telecom، حالا در برخی مسیرها نام PCCW Global و رنج IPهای دیگر دیده می‌شود.
🔴
متأسفانه این تغییر هم بهبود خاصی نداشته؛ مثلاً پینگ کلودفلر روی 5G ایرانسل که قبلاً حدود ۸۰ تا ۹۰ میلی‌ثانیه بود، حالا به ۱۴۰ تا ۱۶۰ رسیده است. به نظر می‌رسد NAT شدن اینترنت هم کم‌کم به یک رویه عادی تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/139501" target="_blank">📅 00:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رکنا: آمار ثبت‌احوال نشون میده تعداد تولدها در ایران طی سال 1404 با 892,000 متولد، به کمترین سطح در 66 سال گذشته رسیده.
🔴
گرانی، تورم، هزینه بالای مسکن و کاهش تمایل جوانان به فرزندآوری از مهم‌ترین دلایل اونه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/139500" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9bc38bda3.mp4?token=LWRDGlvfrceHoGKX9FLMGd4C3w28jcPSAkXWUCFrtX1ywnbmlmAhUm19qlO4HwYNaPXBUi3XwvydpIXRWF8lZeYOkoV1LF8kM_dEyflf04Va5F_qB8pjhGvzHxAG_0a2ZTeqJK7Kmdt8jpMY4UjLK_RVmdp-pU7Q2M5KJRuqKBrFA1urZrULDh19BIN0yUbTyujlKjFkwKQtBligG224kC1KovGTT2YnR9CJYFevxpN7pkxKvWyhiymzD2_9yH-MEJaJuiVl_I0_Kfcu4-IUdM1vxfyFhyXllJTSLbridKxmIReTQRPp5UkJJcjYo_PrdVhu4pwl3nonmxgC2U2bWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9bc38bda3.mp4?token=LWRDGlvfrceHoGKX9FLMGd4C3w28jcPSAkXWUCFrtX1ywnbmlmAhUm19qlO4HwYNaPXBUi3XwvydpIXRWF8lZeYOkoV1LF8kM_dEyflf04Va5F_qB8pjhGvzHxAG_0a2ZTeqJK7Kmdt8jpMY4UjLK_RVmdp-pU7Q2M5KJRuqKBrFA1urZrULDh19BIN0yUbTyujlKjFkwKQtBligG224kC1KovGTT2YnR9CJYFevxpN7pkxKvWyhiymzD2_9yH-MEJaJuiVl_I0_Kfcu4-IUdM1vxfyFhyXllJTSLbridKxmIReTQRPp5UkJJcjYo_PrdVhu4pwl3nonmxgC2U2bWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاتز: همه چیز در جنوب لبنان نابود شده است!
🔴
وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:
ما ۲۴ روستای لبنانی را ویران کردیم. ما هر خانه را تخریب کردیم.
🔴
آنها برنخواهند گشت. آیا می‌دانید چرا؟ چون جایی برای بازگشت ندارند. همه چیز نابود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/139499" target="_blank">📅 00:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
طبق گزارشات، اینترنت ایران امشب خیلی ضعیف بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/139498" target="_blank">📅 00:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
توی تهران یه دختر و پسر جوون رو دستگیر کردن!  حالا چرا؟ هر روز میرفتن توی پارک و دختره کیک، سس و... میمالیده روی پاش و پسره لیس میزده و میخورده. بعدش فیلمشو ضبط میکردن و به فوت فتیش‌ها میفروختن. آدمای توی پارکم لوشون دادن و دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/139497" target="_blank">📅 00:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbVnEZuptAkQhDHJnKB275Vh3iDrG-AN9CorhyY9oAHuNK5qjnioBggxejuIAca1mdquJHCrJcZ1q_NqQi90VavbqofwtMBg2Nl2bu3jgsox_eXuZBAf6YuYrj5hPnPdFjwU-2LjpOaBq_WjVmMDseF_p0hD87TJpw4TMnXg4qilsChjPq2uiHeC7ZQWuw04a8Q19Of7XASsB8EWvE-V5EbrpaPCQ97_uai3Iedc67uzB5GVfeZ38wFVU4E3huF_ls_HbKFBawzjwyrPNv8MLzQzqq_lUaUHkTGeQkG4DPcOuSqnYTys8u5CiVFKyNltb7q0MYeJcYSq68PTrw7Evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی تهران یه دختر و پسر جوون رو دستگیر کردن!
حالا چرا؟ هر روز میرفتن توی پارک و دختره کیک، سس و... میمالیده روی پاش و پسره لیس میزده و میخورده.
بعدش فیلمشو ضبط میکردن و به فوت فتیش‌ها میفروختن. آدمای توی پارکم لوشون دادن و دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/139496" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi2XtKeo5Zk19XL-ICZROwHoAL2Q1I8-vK89-15QAIMYs6z1ufRKL_coAeR1dkabGp3MlCRwkutoGw09BlgoeJ_QnWeAxK5O5AqaJqgRY99njV-yHhE8MBBR44nmJczJyxZ16lTmscMiCB80oHEwANGdCMQU8RLETzCVquU0jjJPZ_UTEDlBU61gmcnjDMPQRq0SvuC3kC661NUJYZ7uHYaom5NbSA4lm2vLLJujUyNv_BAQmBZyD6WKDtc3IW9tHf9P4_7fabzS239MqSgMMZm7LMu10rqgifgdTsxiZ3U4Ti193iqaolOwaFQtGJ9zdT1HMfOHiV0X4ctY9ARvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید: به ترامپ اعتماد کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/139495" target="_blank">📅 00:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HxY-xMmLqvoRCQaC231b-KT8lS9aBqNSvUypR64aWw6Bp-nR35le7psu6tDA83ql_XTvaxPj_BCeNG7mHH82vVrl2_YKolBQKsNo1OVBafoESLa2cM4Kcnm-SuriMUyye-ao-eVOmnDDZ-fk0m6rfxFpmjtZ6nF2-K1T-m6zKnRYFFfhjx9AEMupbcc-eiZrf40txma74yHsKlN5Z68_HcyEWQfhU4hqM80OwWF3ooZIlhpOl7_qryrY92Uyh8SgW89ndA_nBrilvurPaqQbw6SjBx3vA6Wvvk5kTT99AG7b0srruyfVaaX5igFhUTuSFupKJPsCTsPl50c9O5WWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aAdUe0JDQNgV3XmD6UCwybFq581vU-qdGoM6VX0gLM7cQxd0Get87I6H2ptCcegSSM8rnYds0chT0djbSTaEC1gJVTxMnRDw1299_FeO6Sphu_A0X8F6fpnSPG1hQNveHx67qR2st3QnT5zyhs7xrghNwxnTtdBVvkE5vb4PD0eb5JGFXTdJkgFvYTEcMfkPFrw_82KPcOzMgJob7t9p9Sdajq4nY2F5cadD8dATqtmg75dYdXpw4Pibk37abWKsa_f6qatNmnZOvw_AKC3iGKUjzBboHfaTpxPUS501vd-QEWCMamNf1xHvn0CIUwkW2tH8WLen_OjWlLiOTpW7ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ایسنا: یک هفته پس از حمله اوکراین به یک کشتی ایران، پیکر ملوان کشته شده در این حادثه به همراه هشت عضو بازمانده از خدمه و مالک کشتی، به ایران بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/139493" target="_blank">📅 00:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
👈
تصویر تازه منتشر شده از لحظه انفجار پلیس امنیت فردوسی تهران در روزهای اول جنگ ۴۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/139492" target="_blank">📅 00:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
👈
تصویر تازه منتشر شده از لحظه انفجار پلیس امنیت فردوسی تهران در روزهای اول جنگ ۴۰ روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139491" target="_blank">📅 00:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_IIR3ueLzTP5IceQXd-wpeZjRQts_E4aTOhpSWWwZml5qLFzeqidxR4Oxty0H9bzcyNqOV9cJ2BedfIcT3QMHEl3TCnryl5fbrPPOBTPXCmYkcG_-Q8n_lX7e64vETgO1TGg3Jironi2voput_k1zpT3GAgudWRb8Ku36Ymt7oOKD-AONSzu8ECjNwedx8a7Botvu7PckTKEm9iIPcQghWOpmLSvlEvNK3mmRcPi6mhhB_wLMaY9_z-S-Y_JpINHaeAPMqNMXEn_KiYoG9Xs83epB5zRCTQ_He5zPCir2wyQlttaujGIoUn97fecGVOd0_XI6swnzWGgePaopAGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2Xp-H3ZuvjiPGKjG6ZGYRRTYZx-wBNqUOxDgm3FjxU2TqtbuiYiIQ-sbDBI8NXFQn2_B5yznfyJ2iq5frqOlocIYOPFzBRWKry_1mJ3HzFAUxpDrtaFGQ29W1YZeALP-J6j2ZBxsjGDuNJ1P__twaDGO0Su0gGcMG1JlAyZZGCkjrR7mRIuYJZILgRJkRE-jib5qAJHiY70tm3elJBcqQbnISPQJwCNfqcjEp3rj7RZAmr4800bVshsSdimSVTlRo4adqLHE2eTBhMUVe_tj3Yqrb5bSeXnwxvf-KH29RIyozgPRT3JgYEetyO3JZtB88dPiGBu_tjUTd0u_0lMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZE5oABdNbCmyQrB-s_JDQXDliD8pUH78AvqdIwYWlMGRBaKmooF68_FBk43FpEZINHO3Z8_NyTdWa6JM9KL30z-e_lvEbyOc2qaZe0YW_liwdCCIzxtkq3CWcM52iyulFmG-TDbs88IFVqBo8TnlVYHqisi26Wi7vzm50T5_wD4jvTjMYJZcXMRdKOhD9wkTfWWKmC_XsA_DrYDJOhYzg99viRifhLV3ORAZjBtuHoCUKPYOaGrwyhkHSHh0Pw_bONYS_H0-nb13HnEkqrF5jm-jW2UM5u0Moy8IIH0Y2kU3KtlKeer9XQK2eMZfG-Up9YxL4SFgkUuftCdKZzvpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c16e67daf.mp4?token=F8YPyUGCpt8oefg_6GbKYPkiatN0LLnKCQqUquR4TFEG64ivq7mu6nzV9tVIu-RS3_HfQk1Ffn_sA_aLv4qYgCH9DfEXmKJu7FIU5RicbiuWjVEE55FT8SHr3fxptJ1GfKCTuJSzrcMNaoPgn3s_xjU0eU806ko7aO-0gHGQAKZ2iX4v2fFpDRLjWL1f8_YZkCM6SV8-1k_3-ipjvj3KKyOTb5rzD17tTlB9H2nPYZHkatDUo82ULBIXi51lTajfXnTE_HCX3VUv2_hf030Io4deKBRopfCasbHW5QaAxFD8JuRmUybKI_plN1q6BHDkJJy2zzoKOFv_NDdprbhosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c16e67daf.mp4?token=F8YPyUGCpt8oefg_6GbKYPkiatN0LLnKCQqUquR4TFEG64ivq7mu6nzV9tVIu-RS3_HfQk1Ffn_sA_aLv4qYgCH9DfEXmKJu7FIU5RicbiuWjVEE55FT8SHr3fxptJ1GfKCTuJSzrcMNaoPgn3s_xjU0eU806ko7aO-0gHGQAKZ2iX4v2fFpDRLjWL1f8_YZkCM6SV8-1k_3-ipjvj3KKyOTb5rzD17tTlB9H2nPYZHkatDUo82ULBIXi51lTajfXnTE_HCX3VUv2_hf030Io4deKBRopfCasbHW5QaAxFD8JuRmUybKI_plN1q6BHDkJJy2zzoKOFv_NDdprbhosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در منطقه المانصوری و مجدل زون در جنوب لبنان عملیات تخریب گسترده‌ای را انجام می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/139487" target="_blank">📅 00:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMRa87WZ1QfEr5zxrKcqOxtM3ZPNFZnJF0ig2gzEDmp30c35GFxD-Jp3T9yDBelkdCBR9XV1c4sC6OXImTOl_R2YDKNPgRsdU4yiZAQX-bvtBmu4oA5hjArFQOOO2OVLoEIk_R-DsUUGVldrqgFYr4tlRljM5hVyT-H2w2CpxOJJy59Rntl1OSXT284NXQysbyNZuZ2a1lUUXr82dQCg357qECSb6ZM9yI58ARvbsnCI2Jxz1Ny2tgmOG-Ihh85Up0GYmgwEhCpytMNRy-Ud0ZZaqAwfKxnquFhSam-p6USc9sx7G5NrJT9eZe1ubFvC8xU5JMHrVPKDi4gc3-ftug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی زاده:
آخر سر آمریکا اعلام شکست میکنه و میزاره میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/139486" target="_blank">📅 00:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB4sKNO0gyq7-vo1pB-1xxXZ7dOIxk5qMATyuOK2QuzSeJDZlOixWNpeO1xrzivCHig4KffdedtvYtyrTucgBEGnQFNz8UAwAWqjl7xBU7KMHTi5OW4EB0su6NUE80deWiWF1QI5zchfVZV-0oojr3PHt5h0_v6OdJiomCoz_QmCVVwq7JLJryXTTLlNerQYTt_s34H88ghcBzwdUOK2R7jU_hkWvMcj2vlesCHVImdHPlLp0ked7gtFcEE-Jqr74b_6jfMUHQWSwmRCXG0Bx-s7UzrHkUcz6iRZah_4Wpeya-jEc9n0TRwQYbDE2he1aLGaHH64BB-zApzRUX_OVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: آخرین نبرد رو بازم‌ ما پیروز میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/139485" target="_blank">📅 00:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8549b9f30e.mp4?token=od3xpVlbQdKm0-F5aTtsCrazKAQbU7r4G8MqgcILl_x3FJUOqKZWNCHHjOhdIUCIeyGABpvWV1OONf-Eh3t2_VAa_0nnnMLNrlKzWbmsTxVe1O2oJexu8iuvDsYagVU95T4LjlooiKRM1LlqNks16GzJHdVZLe9kMZhukk-YWPJCUCHAfxkqm5sIZNVT9AqY_tdM0Z9rRwjxeM-yd-Jk23c3lHDdRJaftkCacq0v2EPA3BtpulUHxECm2jibgIkW12RpSsQs6bcsWr7G6xpfuMoPiG4Df1jtAOwrKMk-wYeRgDEDnHWMvtBX2NfkEEk9mj6JBdMfyC-zZKTDIKByuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8549b9f30e.mp4?token=od3xpVlbQdKm0-F5aTtsCrazKAQbU7r4G8MqgcILl_x3FJUOqKZWNCHHjOhdIUCIeyGABpvWV1OONf-Eh3t2_VAa_0nnnMLNrlKzWbmsTxVe1O2oJexu8iuvDsYagVU95T4LjlooiKRM1LlqNks16GzJHdVZLe9kMZhukk-YWPJCUCHAfxkqm5sIZNVT9AqY_tdM0Z9rRwjxeM-yd-Jk23c3lHDdRJaftkCacq0v2EPA3BtpulUHxECm2jibgIkW12RpSsQs6bcsWr7G6xpfuMoPiG4Df1jtAOwrKMk-wYeRgDEDnHWMvtBX2NfkEEk9mj6JBdMfyC-zZKTDIKByuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه اسم انواع رابطه ها رو بلد نیستید؛ این پست میتونه بهتون کمک کنه.
وان نایت؛ رابطه ای که فقط یک شبه.
اوپن ریلیشنشیپ؛ رابطه ای که هر دو نفر با رضایت هم بهم خیانت میکنن.
بنفیت؛ باهم دوستن و رابطه جـنسی هم دارن ولی تعهدی ندارن.
لانگ دیستانس؛ رابطه ای که دو نفر توی دو شهر یا کشور مختلفن.
سیچوئیشنشیپ؛ یعنی هم تو رابطن هم تو رابطه نیستن؛ یه روز هستن یه روز نیستن. خیلی وابستگی وجود نداره.
هلسی ریلیشنشیپ؛ رابطه عاطفی سالم که همه چی توش جدیه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/139484" target="_blank">📅 00:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfzgyYJqbLtmOyzf4AdZ3kPOiTcPnvuuZpRzs0f1bsa5HByzhO37Pa9JrTCJsionvjUxKrawRKk3hTj0SvQfTLKbPljR0fyzr_0vUkF231ZJ1ucGssGtA6J0Ndvy9Nb6xBGgkkqjKLRofANtUzCYqJou4YJKnImXZq9Fnyzd3X40DCRjLmsbx84_p4qF2F5AHzycKsnWwmJEBV6APfVbWX8KwKIHaz02dx1St9pFLVsijWu5NeQnoBqYgi7AuZs11p98Vyih5RaJmFaI2jWscgCto7Alq76F-hBxPZ2p5Jt98L20DiGRxmv2eGov-7VuVNJcsZKIga9T7TfQb_kO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رد پیشنهاد بی‌سابقه‌ 1.5 میلیارد یورویی به‌خاطر خانواده؛ وقتی مسی ثروت افسانه‌ای عربستان را ندید گرفت!
اظهارات تازه‌ و شگفت‌انگیز آنمار الحائلی، رئیس باشگاه الاتحاد عربستان، از یکی از بزرگ‌ترین پیشنهادات مالی تاریخ ورزش پرده برداشت؛ پیشنهادی که لیونل مسی بدون حتی یک لحظه تردید آن را رد کرد.
📌
رئیس باشگاه الاتحاد درباره روند مذاکره با فوق‌ستاره آرژانتینی گفت: ما پیشنهادی خفن و تاریخی به ارزش 1.5 میلیارد یورو به مسی ارائه دادیم، اما او این رقم باورنکردنی را رد کرد؛ چرا که خانواده‌اش ترجیح می‌دادند در میامی زندگی کنند. چیزی که ما را عمیقاً شگفت‌زده کرد این بود که او حتی یک ثانیه هم تردید نکرد. او می‌توانست تلاش کند خانواده‌اش را برای آمدن به عربستان قانع کند، اما بدون معطلی، آرامش و خواسته خانواده‌اش را به پول ترجیح داد. ما کاملاً به این تصمیم احترام می‌گذاریم، چرا که خانواده همیشه از هر مبلغ پولی در دنیا مهم‌تر است.
این تصمیم مسی نشان داد که خانواده برای او از هرچیزی مهم تر است
@AloSport</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/139483" target="_blank">📅 00:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb15c4e0e5.mp4?token=d2F1G2qscjvx8S_bmQkO0b2v0fe7imtNFf1u0b_JdHxrJAlBba_zmV7XMF_FuzbPzy5M-stgahsSYpdnN34KAmdpaFs_RRLxq2-DQve11zmhDAqagO6xwrRr5x3v2un3zvJ3M0kM8f_H5CujHlf1ZaovFkeu5qHdU9m_EadP4nZNYBWUTcn08uiJu7OoU-Ru4wFerZL44YstuTPpN-mwjeEKw2YVYpq9WKu0IkcUTUvVVI1WejBZedUrt9I2ZH8J1-6T5CIiiPXIFAwAw7IU_rhVX4aCxVR6rnoYmA5h-zb-O_5C4bDdnk32wlzlsRagbRtfotA71WqJy3HHmiklJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb15c4e0e5.mp4?token=d2F1G2qscjvx8S_bmQkO0b2v0fe7imtNFf1u0b_JdHxrJAlBba_zmV7XMF_FuzbPzy5M-stgahsSYpdnN34KAmdpaFs_RRLxq2-DQve11zmhDAqagO6xwrRr5x3v2un3zvJ3M0kM8f_H5CujHlf1ZaovFkeu5qHdU9m_EadP4nZNYBWUTcn08uiJu7OoU-Ru4wFerZL44YstuTPpN-mwjeEKw2YVYpq9WKu0IkcUTUvVVI1WejBZedUrt9I2ZH8J1-6T5CIiiPXIFAwAw7IU_rhVX4aCxVR6rnoYmA5h-zb-O_5C4bDdnk32wlzlsRagbRtfotA71WqJy3HHmiklJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیلا فرخی (همسرِ بیژن مرتضوی) مجری یه برنامه به نام TV10 شده و مجید واشقانی رو دعوت کرده؛
حالا بنظرتون چی جوری طرف رو معرفی کرده؟
🔴
"امروز میزبان یه هنرمند و تحلیل‌گر سیاسی هستیم که تقریبا تو همه جمع‌های خانوادگی، مردم دارن دربارش حرف میزنن!"
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/139482" target="_blank">📅 00:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ecf46d77.mp4?token=NrVagkRUUPykdRWu5Ek4wFJSJKc2A0Ra8c0nvhVynV0KCkdy2AXo0sw0dGxhSkmNpbyiXDM1wxKkD9crZWV1jC92VsjFZ3_D8_UtOmITJZKvlZsNPD_-FNYrzjmvRtdCNOT0WCkhTPwtC0oppyOIcH_BXNnMc0bFj4WYEeXE-SQ7Li3NtqBkBFyjV4-daul0vosvWcR3blqjWRAiimjGC5VwZVhvcqf_XtPTc3CWVWUjXvLdsXuhyX9DNdAuwNOspt0xAx52OUt9y4cdkO6erbnZemQIMm9qQaxkh5n_zWAJBW8kIEJFHL3NuHJnvurF-ocxkD_LesgU0AQWzJ9DoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ecf46d77.mp4?token=NrVagkRUUPykdRWu5Ek4wFJSJKc2A0Ra8c0nvhVynV0KCkdy2AXo0sw0dGxhSkmNpbyiXDM1wxKkD9crZWV1jC92VsjFZ3_D8_UtOmITJZKvlZsNPD_-FNYrzjmvRtdCNOT0WCkhTPwtC0oppyOIcH_BXNnMc0bFj4WYEeXE-SQ7Li3NtqBkBFyjV4-daul0vosvWcR3blqjWRAiimjGC5VwZVhvcqf_XtPTc3CWVWUjXvLdsXuhyX9DNdAuwNOspt0xAx52OUt9y4cdkO6erbnZemQIMm9qQaxkh5n_zWAJBW8kIEJFHL3NuHJnvurF-ocxkD_LesgU0AQWzJ9DoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خمینی خودش سواد نداشت و مخالف سواد بود بعد طرفداراش میگن محمدرضا شاه بی سواده
🤔
یه مشت حرام زاده مفت خور که هیچ چیزی از وطن پرستی نمیفهمن و فقط از امت‌گرایی اسلامی میگن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/139481" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdBgsz4SDxTQvU1XwNUkRde01voHvEghUfraZqmI871UqQ4K27fOE99w0KihC6KAjb6CqRaxlZrVnr_uCqAoF3Hud4e-ojSh4zuKz7b4mqYj5X_xxQeShPdKrq1MII8KB-y52Digxjaru6Dv-VqKLA1RHi0Dxklc0yGxGHpD_THe4AsncT3jCDtyTdmA6gNia5wgrq8-av5CXAkmhKom-_WIrHDrwiGiyp08u_Oju_xJKNj4eVo_pFYso53ahIpb8H2KB1f1_-gWvw72gC84Qhg-8czEWbsgYlvTB70X88AzDikZTtlRkvqTH73IzIjmA15sMnKRLJUFA5OgYEiu4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی بازهم به عاصم منیر زنگ زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/139480" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش همچنان در آماده باش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139479" target="_blank">📅 23:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚠️
امشب
پشت پرده
جنگ ایران و اسرائیل
فاش
میشه
ادعای ترامپ و نقش قطر، عربستان، ترکیه و پاکستان در آستانه بازگشایی بازار....
دیدن کامل خبر....
🔴
🔴
مجبورم لینک سریع پاک کنم حتما
کانال
داشته باشید</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/139478" target="_blank">📅 23:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEaEYDy-Xc4RDW3M1VSRu3rdDVEVrlNW3wfswW_Wzc0RKfIRWeRwo_aJhJ8HJSQQIG9goC1Ux3SjUM5u4MVynq3sBnP6Ay8XSaDmxjs-hxtNHKgQ3GcwdOWbowiUskjxPumIsYwP_DRxF0qqD2csYebxeDy6sz5xxeZ1iWUmCVS9uIYnPu8lo_q6mOrLBpB686puFq4RbrhQ8II2p6Z7JikFDPSnuZCb0mMONc9aIZjqaxjm6LLC3Z8GiZ-Z5-yIbT9HM9s3S9PwOXSh73DaCn7txK1CD1Ci_0BbSSMoPZxINbnNMofWQ6II4hP7WSfbbTiqMiLn-Rw6gI9tbt_qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
5 فروند هواپیمای آمریکایی تانکر سوخت، در حال پرواز بر فراز خاورمیانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/139477" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
منابع عبری: قرار بود اسرائیل در حمله آمریکا به ایران مشارکت داشته باشد اما قطر برای ادامه مذاکرات، زمان خواست، عربستان درباره جنگ هشدار داد و پاکستان و ترکیه فشار آوردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/139475" target="_blank">📅 23:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزارت کشور مراکش : تو جریان تلاش جمعی برای عبور به سمت سئوتا
🔴
۱۰ نفر غرق شد‌ و یک نفر هم بعد از سقوط از صخره جان باخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/139474" target="_blank">📅 23:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
هواشناسی: پائیز قراره کلی بارون بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/139473" target="_blank">📅 23:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd3485532.mp4?token=Hx7n9aZZnEiRx8SPo6IlfVdpiI5DfpKKg92z5v4fjU2zywoKmAqkN-se61jelhjLfNS7LWBoPGbIwrJJuKoqLoXwQiRmkO9OR03zy79BJ4I3yw7TlIVjy-2JFUAGzwVp0vvRMNMi5tyKW59d2Jha5uHIY_diKAzTAmT_RnLoBKnAnnkCl6W9JgRVJM8DYKqW3ot2ZWsoyAQVVKxRPGVFc8K1Lsk4nnYR9iuvOg5qSw6AZUb66pskeb8uqb6M3FVltxmoL32eb3szu7LF8CUlPtOZjq_DU5XEH5fQww5jV8tY22Lb3HIwsOixqmG0uw6c23MVgecm86urBFK3tSZEDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd3485532.mp4?token=Hx7n9aZZnEiRx8SPo6IlfVdpiI5DfpKKg92z5v4fjU2zywoKmAqkN-se61jelhjLfNS7LWBoPGbIwrJJuKoqLoXwQiRmkO9OR03zy79BJ4I3yw7TlIVjy-2JFUAGzwVp0vvRMNMi5tyKW59d2Jha5uHIY_diKAzTAmT_RnLoBKnAnnkCl6W9JgRVJM8DYKqW3ot2ZWsoyAQVVKxRPGVFc8K1Lsk4nnYR9iuvOg5qSw6AZUb66pskeb8uqb6M3FVltxmoL32eb3szu7LF8CUlPtOZjq_DU5XEH5fQww5jV8tY22Lb3HIwsOixqmG0uw6c23MVgecm86urBFK3tSZEDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو کربلا موکب "خدمة ام البنین" به زائرا آیفون ۱۷، آیپد و طلای صلواتی داد!
🔴
منبع پولاش هم مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/139472" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
واشنگتن‌پست:
همزمان با ادعای ترامپ درباره پیشرفت در توافق پایان جنگ، ایران و اسرائیل همچنان در حالت آماده‌باش هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/139471" target="_blank">📅 23:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUXhKCZ43Dkq0vxY6YFHi7ACNIWwl_aDmL2Cb9WO_z91RpmHJ75m1snc-Q1u0VPx9b96ITGHq2H46vq4xf1zWTDQiPCcZ0UueXWLObpyeTH7VRvVg56ZU73uvblibXM3VVSBPtJDlH-d46js5X7jb6-WhJHIdIy0Pagkq-L5VXbog2pzghA7WydcRgoBjCcog0i-Y2DcljRhV0y94RN_YprBc2gOg2NUGxJou-hooLof-YFaMrW0x-_tCuYm8Y_POFAcLlHGBCPOMXm6e8IHIYjjaEjY-Tr7n8nXEXPhymyMraQDVXZeUc34tD5bORm98zG0fhE8urrsHPDOZ6MHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناتوانی سپاه در بستن تنگه هرمز بر اساس امار جدید تانکرترکز
🔴
از ۲۱ روز گذشته تاکنون که سپاه انسداد کامل تنگه هرمز را اعلام کرده روزانه بطور میانگین ۷.۵ میلیون بشکه نفت غیرایرانی از تنگه هرمز صادر شده است. در ۲۴ ساعت گذشته نیز ۱۳ میلیون بشکه ظرفیت نفتکش وارد خلیج فارس شده است تا شاهد استمرار این جریان باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/139470" target="_blank">📅 23:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
👈
والا نیوز:
قرار بود اسرائیل در حمله آمریکا به ایران مشارکت داشته باشد اما قطر برای ادامه مذاکرات، زمان خواست، عربستان درباره جنگ هشدار داد و پاکستان و ترکیه فشار آوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/139469" target="_blank">📅 22:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK4nRAOwdO-V38lROv0OjDkgfDGph9XqfZSki9WRWmJunZQINljdAf5AHEbUNOqqleRejfRhMKR6w_EM5gG9rmpJNLjCABx95DmIjwND_H9Qn5BEQJ19tb069AS3mK_dQuctIU_ZStvvzI3sY1LYKE6NYoSU5afj5-zFL8NnNi_9S9LuZXec3TRHydCkcV-nrVAXDYsZu81EzFDlWp5TaG19s50i4w68anz3nV_FkxdO32XyrWCeomvJ-WV0vaq0LWGSQNhpTYsrK0kCjryzaWWzNSuuH_VdLfdrWMV9rH1-3DuOrqwBYQCrwe_IXQQUEBoYP_s6fu49J0ypHLy4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش ها خط فقر در تهران برای یک خانواده ۴ نفره به ۹۰ میلیون تومن رسیده.
یعنی اگه یک خانواده ۴ نفره در تهران مجموع درآمدشون کمتر از ۹۰ میلیون تومن باشه؛ فقیرن.
🔴
حقوق وزارت کار چقدره؟! ۱۷ میلیون تومن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/139468" target="_blank">📅 22:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7b7518965c.mp4?token=vGo05dyBbF5frqP2CvGWD9axRwxKDIjAdnBoazskaDhzX3e3mHl5VY1ZCLX9rLWTjigAmkM421hUUrUyUDhQeEuwNudHNY9m9dZaKLQfNo1v2jfhhq682oCXrNeWJzJfhgkyiguy36liD64BQoB_F1RXqR6kthygNbiH7S6gC92IC3KzVimDwx66nm5tG4OX-e8x91ADVazQHdrbWwKLDtTVzZ_B-nEEkPP7xbWGbaaDLNEIMBUnEHoXSvmD_ZiCsRlMkJf02CZY336IyrUXaBNDd_rcppt1tRNuqHIFLwtW8_POUj-az2QbsApK_NbfBYv4qXJrSsj3IfQqYQIy8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7b7518965c.mp4?token=vGo05dyBbF5frqP2CvGWD9axRwxKDIjAdnBoazskaDhzX3e3mHl5VY1ZCLX9rLWTjigAmkM421hUUrUyUDhQeEuwNudHNY9m9dZaKLQfNo1v2jfhhq682oCXrNeWJzJfhgkyiguy36liD64BQoB_F1RXqR6kthygNbiH7S6gC92IC3KzVimDwx66nm5tG4OX-e8x91ADVazQHdrbWwKLDtTVzZ_B-nEEkPP7xbWGbaaDLNEIMBUnEHoXSvmD_ZiCsRlMkJf02CZY336IyrUXaBNDd_rcppt1tRNuqHIFLwtW8_POUj-az2QbsApK_NbfBYv4qXJrSsj3IfQqYQIy8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از طرف صدا و سیما اومده بودن از چند تا کرمانی بابت حفاظت از تنگه هرمز تشکر کنن؛ که بساط سیخ و سنگ راه انداخته بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139467" target="_blank">📅 22:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaA65339QOhBmqDZIidsXYhUMyJLGQSWryW8JKpp9kg2VW8Y9kAIKOGYc2q8d6VrGcLKgDj1BEi_A3_EsaL0NC-kv0jCqZbuUFZ0v0k8F7QCcn74kmS8M1qeoCUkw-XI3G4N9kmGg8psVN4jAkLy43vUj4Ln22i1nUBjqoyYVbjJ-g9AUmzFau5QVGLMSr-2co5Huj-4Bt03vdKQqBpPM3tT3n-a-CMrK63dcC3kCYDZWJJCFiiAX2uxg35t74bIH2cfuHb1kh9mPBZViACRMyIINwZp7Q9_IaCzmkvCg3FC9IxPUMRn5SyqB4MGswqzWsPQ02fX5kjU1YoPvGHA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل:
ایران مستقیماً ادعاهای دونالد ترامپ مبنی بر دستیابی به یک توافق مهم را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/139466" target="_blank">📅 22:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139465">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فارس:
روسیه 11 تن غذای مفتی برامون فرستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/139465" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dfa1b7126.mp4?token=guWccb8cSrlRUbXooIgMd4m4UUlceH9wN-CrrOs_c_pNlCz3PyboYJMFA7uIB4wB82MWkwX6wJ7Mnv5eej_tHrtzQKhAEgwflHe1vaHCip7GbUhVKh-s1LyAUM_EepQJGUwJCSf7LQKd3Gp3PhtNL8PaKJDVxLhgqst6mnDUmQDXMcfG4yXG9qdgEh5d0x7Q0DlH2ec5JVfV4RxgiECjC-cDtlqPLU8IkyTE7YO7yzkTL8rcAbwVEgBwG746fIsDdsTUKZa1aV5JgrW4jcYtpavev3DWSs7hSc_54Y3Qe9klFDbfGnllxUElcBgm-1BW4Kf1Oju4x36DZyOMelr8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dfa1b7126.mp4?token=guWccb8cSrlRUbXooIgMd4m4UUlceH9wN-CrrOs_c_pNlCz3PyboYJMFA7uIB4wB82MWkwX6wJ7Mnv5eej_tHrtzQKhAEgwflHe1vaHCip7GbUhVKh-s1LyAUM_EepQJGUwJCSf7LQKd3Gp3PhtNL8PaKJDVxLhgqst6mnDUmQDXMcfG4yXG9qdgEh5d0x7Q0DlH2ec5JVfV4RxgiECjC-cDtlqPLU8IkyTE7YO7yzkTL8rcAbwVEgBwG746fIsDdsTUKZa1aV5JgrW4jcYtpavev3DWSs7hSc_54Y3Qe9klFDbfGnllxUElcBgm-1BW4Kf1Oju4x36DZyOMelr8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاق باورنکردنی در ایران
‼️
🔴
یک دزد، یک دزد دیگر را با لباس پلیس به خانه مادر یک دزد می‌فرستد تا ساعت ۸ میلیاردی را بدزدد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/139464" target="_blank">📅 22:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139463">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی دولت:
تغییری در قیمت بنزین ایجاد نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/139463" target="_blank">📅 22:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=mPDVURkMj9rv1zGopZaBepQTCAb3_Ft9-CGKCKPTpPUBtakWJzyvT3HkSOFq6tJbg3TVfktA5HNaR0xJVYOwmqfJ-NRpZ3Jznv-5086q7aJynhzN4M3KbyxMmyC51k0zCCihpEWyVBzonwrQWn-zSl5u-TBAmLIvRfisTDAru3y3fA7pJ98OYrw7qt4PW5yxS7JGzA4BKH7bnQ3NTwtteD51s-x-j2E54oHc69XfT1VpmwN_e6qNlzSPH2DDdW5Ur9jT_COvZw8bkKkRPI1UaaUoqXvlFngk060JAZdd3-JENveXCaAhLRagmLguajU7zYt-FGTB31dfcLc2PtpriA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=mPDVURkMj9rv1zGopZaBepQTCAb3_Ft9-CGKCKPTpPUBtakWJzyvT3HkSOFq6tJbg3TVfktA5HNaR0xJVYOwmqfJ-NRpZ3Jznv-5086q7aJynhzN4M3KbyxMmyC51k0zCCihpEWyVBzonwrQWn-zSl5u-TBAmLIvRfisTDAru3y3fA7pJ98OYrw7qt4PW5yxS7JGzA4BKH7bnQ3NTwtteD51s-x-j2E54oHc69XfT1VpmwN_e6qNlzSPH2DDdW5Ur9jT_COvZw8bkKkRPI1UaaUoqXvlFngk060JAZdd3-JENveXCaAhLRagmLguajU7zYt-FGTB31dfcLc2PtpriA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت:
تا تهش پای این حکومت وایسادیم. بازم بیاین بیرون دوباره بهتون رحم نمیکنیم و با گلوله میکشیمتون؛ چون داریم دستور خدا رو انجام میدیم. پاینده باد جمهوری اسلامی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/139462" target="_blank">📅 22:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIi6thGVLwx2Fb-n75I-Y34vzVJB7JwwxuqfC2-8RaAQztpoV7hDuTCI1N1MXBsZkdX8Xsx0Ie_7NtJ1JKoXeWqJDw-fInCQ0opbd6NwjLcfl3Y46aPTIKTs3xPvbIgNhQN9gFAp2lNrSHBj8VQKSy2A9pujHHtdNYCj-j9Bjk9M-lGoinRgTMEK8VGSs-ij_9jKljjFE_j8P7kUqx1VbwtD4QCcEkrFxT1_7Sfhy3QZBC4umEjAzQhTlh6QcsvX6H3pA4um7_1m3CpmejgdzhYdJLfNg62xi8vz7WYNfD3JLf3z53j5pb-FGWqogVVy0Sho-G5UvhaFtgOMK2aoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیر کل فرودگاه های اصفهان از برقراری پرواز های مستقیم بین اصفهان و استانبول از ۱۷ مرداد خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139461" target="_blank">📅 22:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4Ij41z_yGeveEFMNOcUEB9IHijGhbssheQx2Tip0AbHSmZ3wdOxoxwrv7TNtta_ta5iguP1Huzfqya7GCfFeBQnI2x1APn5yi6FmoY0_ly0Z8YGQs0Ir-dbFt_nSFNU7HbH58Gea0fvC6QH2G1j9r5trkMEKO0oMQ_vKO4kNi7N-8raXHInTCOuBbpGhTWrdc9vvvotEBcMjCSDSVuZEHiHt8LJq40DSQwO5O9a3-cc1-uYRl-Z_A0a5uZ-zGxhLaW9DdkxSM6q3FWUgjhMDdV8xnhXE0KVwhb5x-5ePCWmJ9-slWiRa4Ij5XQMxLhV3DekhSMq_JfdIlkorU-dlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی شریفی زارچی:
وضعیت روزانه‌ی ایران توسط عاصم منیر و بدر البوسعیدی و محمد بن‌سلمان تعیین می‌شود؛ بعد می‌گویند خامنه‌ای برای ایران استقلال آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139460" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNau7HlgxtfXnWMKrnoHr-TwnwKDKXHXlCBWcPAwJlfNnjOjUynoXz5SeaZGkTSHbMJF7Lea3VMOfSDWFK9m4sficuVnRJsRjwTxS6H8Kh5hscjUzQPCyPfDCZYOPCVwwPj4Ur8Hl-ZekUAY-BQCYvU2KHITwdiEsuQMDg_aBTvQYFxWRP9t8g8OOGm0cWiauoEO6Bm4deytLEST5H37JvJEBfGMM7eqRq2BUG5NwCpZ4da8ax0AjyELgegCWgzOwEWK-Rtf2XupcAV5e4iaVtnRKvnrYeLASFvq-L-Lo3xoIicP7lkF2w8BwWgnxVhLURb2UiSlpEDcFl5Zm07GKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: باید بکوشیم دشمن را وادار کنیم به آنچه در تفاهم‌نامه امضا کرده پایبند بماند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139459" target="_blank">📅 22:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139458">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
یک مقام امنیتی اسرائیل به کانال ۱۱ تلویزیون این کشور گفت
: واشنگتن برای دومین بار در یک هفته ما را از حمله‌ای قریب‌الوقوع که می‌تواند خاورمیانه را به لرزه درآورد، مطلع کرد، اما در آخرین لحظه و بدون هیچ توضیحی آن را لغو کرد و این به آمادگی عملیاتی اسرائیل آسیب می‌رساند و آن را تحلیل می‌برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139458" target="_blank">📅 22:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دولت سوریه با موافقت سفارت بحرین در دمشق، از ورود زائران شیعه بحرین برای ورود به کشور سوریه جلوگیری کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/139457" target="_blank">📅 21:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از منابع آگاه: اسرائیل تلاش کرده از فرماندهی مرکزی ارتش آمریکا (سنتکام) اطلاعاتی درباره حمله احتمالی آمریکا به دست آورد، اما پاسخی دریافت نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/139456" target="_blank">📅 21:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
الحدث: گفتگوی وزرای خارجه عربستان، اردن و قطر درباره تلاش‌ها برای یکپارچه‌سازی مواضع با هدف کاهش تنش
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/139455" target="_blank">📅 21:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از مقامات امنیتی این کشور: ترامپ ما را در وضعیت ابهام و سردرگمی کامل رها کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139454" target="_blank">📅 21:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
شبکه «کان» عبری: تصمیم ترامپ برای لغو عملیات گسترده علیه ایران، آمادگی عملیاتی اسرائیل را تضعیف و برنامه‌ریزی نظامی را زیر سوال برده است.
🔴
این دومین بار در یک هفته است که آمریکا حمله‌ای برنامه‌ریزی شده علیه ایران را در آخرین لحظه و بدون توضیح لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/139453" target="_blank">📅 21:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1ATC4IEERWaqtOvOnxge9IkQQG7li4dtJC7dWD7T0bRC1jRvB8QQUVrKdLzfxiGPxionCvs4InzFTfA8OFLlBBXw4C3zxqdymM1ryFPjsrfxT3GSIMSupzHtiLaSNr6Rd0MrO9ug3iWTn2d9cJUdFl5Ai5Vy386R9OQ7DpeispBiVUHMwhJI49gMLk719d7ZlumdIGIoJzjQwRaT_Ci4QXNffp0u7u8_JQqYqJsg_c7kwvwI-ta7SNma2JWkUgj9YhXbu2Fu_07B561QSOHrrlJce3GD7HgWwr9ZZSmmxrH_IpwVJ7NFL9Uc3buAoBp2yk-5VbIznDKe3DmVZpRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت بلاکس: اینترنت تو واشنگتن آمریکا ضعیف شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139452" target="_blank">📅 21:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_DIb_jZCf5IPkdGr9_2xMGkHBKgM2eKiNx7JwORraovMKGjtuDAIKwqQIZGnxexJby5iLMW_bHlkSoUXJxK13XLOMoKVYXvf61ZIovscUH2EZZVLcGHsBQNXHppAuRqUhruH-GjtIulnVrg48wJVIrgZFtXQYs89HPcR8WkqZlsnTPaukjHpeUKmke8jvNgmGSTWlGSekAj38DsD-77l4q9quAuiW8LTK576wr3GdYJZMbLiOs2rkv1rex259W2Yo-ePd81z2F4J-bWCY0eKfPjCpkvSWd4_XiCNiRvZOKWNDhexsR4YOwy7VQEqBLZ2M2EhRMOBn-8W8koXgtV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : عکسی از خود را که در آن لباس الوییس پرسل را پوشیده بود، در شبکه اجتماعی "تروث سوشال" منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139451" target="_blank">📅 21:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پزشکیان: اجازه ندهید جریان‌های تفرقه‌افکن فضای عمومی کشور را تحت تأثیر قرار دهند
🔴
هرچه انسجام ملی تقویت شود، مسیر پیشرفت هموارتر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/139450" target="_blank">📅 21:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd230</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139448" target="_blank">📅 21:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=Kg8W48OlZEbfJ3HnefPjyG1YXFIb_v-pSJWedT5HsAoRv-1tMkdV0BkPXw0ypia-J7Jp79ya6zoIpyiMw8LpV5nhxi9LkbNtJ5-d0LUAA1XKlcggQc4TfE0tUcpctELhwRGFqDWrb0Qe7kc5bv04ijcbsuTdbZOt-MIuvezf1Uw_X0w_jFI2oImJ0zGi-Q_cy64Mjy2YZYx2dr6GIl5FiF8mNjqwCW25DOLnv0vxSYqW-4el5k9SAh75sqUm3mCqKeTNq0OJ5tDyxNkQm47NddTOeEnLGvbiTW-qB5o392jEHllnxiD6Q6uc8KeSWpUUVB2UZYZWuTwODU6R8j8oKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=Kg8W48OlZEbfJ3HnefPjyG1YXFIb_v-pSJWedT5HsAoRv-1tMkdV0BkPXw0ypia-J7Jp79ya6zoIpyiMw8LpV5nhxi9LkbNtJ5-d0LUAA1XKlcggQc4TfE0tUcpctELhwRGFqDWrb0Qe7kc5bv04ijcbsuTdbZOt-MIuvezf1Uw_X0w_jFI2oImJ0zGi-Q_cy64Mjy2YZYx2dr6GIl5FiF8mNjqwCW25DOLnv0vxSYqW-4el5k9SAh75sqUm3mCqKeTNq0OJ5tDyxNkQm47NddTOeEnLGvbiTW-qB5o392jEHllnxiD6Q6uc8KeSWpUUVB2UZYZWuTwODU6R8j8oKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
باز نشر
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139447" target="_blank">📅 20:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec22906e5.mp4?token=HFaPJdNOGbaQq8IJLOZcKPz92S29F-1TbibSYTq4E_wDZ2JpE7UZRXoqRvkBEGxhvpn4evguCqo5bIgil4rR-qZYYv0lGSw7IwpjYvgwNkqjSmSmzEwAPg5Yu7rgl85_OcHokXoK6_czV4oJLQoyxni9n8savOQpUE6dhlMEv2Wwks7-VUbpAJ4BwFOZiqGvmn-54EH8IyU95H852u93_RKDjSnNHTcd3MfR3grn-Ge_-jgui1WEaJP_yY8dBXQ2zbR1uZIAnY17K2oflCJv3It04bcatnG2S3m9Cn7jmznxswHrPFcWSvoWvoP1BHeqD8qUpVhyG6XDXUiIjYrDJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec22906e5.mp4?token=HFaPJdNOGbaQq8IJLOZcKPz92S29F-1TbibSYTq4E_wDZ2JpE7UZRXoqRvkBEGxhvpn4evguCqo5bIgil4rR-qZYYv0lGSw7IwpjYvgwNkqjSmSmzEwAPg5Yu7rgl85_OcHokXoK6_czV4oJLQoyxni9n8savOQpUE6dhlMEv2Wwks7-VUbpAJ4BwFOZiqGvmn-54EH8IyU95H852u93_RKDjSnNHTcd3MfR3grn-Ge_-jgui1WEaJP_yY8dBXQ2zbR1uZIAnY17K2oflCJv3It04bcatnG2S3m9Cn7jmznxswHrPFcWSvoWvoP1BHeqD8qUpVhyG6XDXUiIjYrDJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی :
بریتانیا، بلغارستان و اوکراین
به ما پیام دادن، و گفتن وارد هیچ درگیری‌ای علیه ایران نمی‌شند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139446" target="_blank">📅 20:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از منابع آگاه: اسرائیل تلاش کرده از فرماندهی مرکزی ارتش آمریکا (سنتکام) اطلاعاتی درباره حمله احتمالی آمریکا به دست آورد، اما پاسخی دریافت نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139445" target="_blank">📅 20:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139443">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iydsoiq2El0eNbSf7eFg40kVXgbQKUQ9ohk56rekBcYL-Vy3foto_pmZojPDAYp9rwKJnRleht0x7cGHgf8zXN3nei81RHBHA8nDpCTA4cYRgva68EpRv-8e5tlkZdTvsfeAv4K7POlRTdrrq0WhQrAw_pJus-NoBnm8HQEXOWUWj2llgVXIjE_FRUUaHupmkolzIQ1rdl3-pCgKcgj1YOPg23POpQ0NPnliPd85hIKmJkZZkoUGiW8Wcp7V4W2M_a-0yLV3VE5c8HxN-W4mtIdqX6TYQBN9GqZHypdEZkjxosbtWvKTMTRPArVTlqD4LXRfTTK9w1WrBYdK9m5b2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxy6gVHgRYjdl0tCqlJ8-MEd3iJyhoHwYXuJTNpdfIXIOFnE8ecJsECGjaveBu-iFHULeENRio7Oua4E2iyA8Mi8ea7H3MnZFaWE94_zZNp45kxIP38wjA7K7iLvQlqCoIBozh2Ef2jLtRY-Gcx_YYtVxFYdGC7vxBuFCSmmg7nCHvBYMmbTPSATRn7Ofeh1FDFxLl0668InyMTEzVRQCwUbkENygxIy6B-8yncr2VUEKlLfmEhdNYO0vS8OthaZov3_FyGktc6IADwuc3hQR4_se1rm2jIDqq29sbpfzafX0CWNyIp5Vud_ilAGQXBzEX8jIc1P-44DBR_GXqCqSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ناو هواپیمابر آبراهام لینکلن کجاست؟
🔴
تصاویر ماهواره ای سنتینل-2 از دیروز نشان می دهد که یو اس اس آبراهام لینکلن در مجاورت خلیج عمان، تقریباً 200 کیلومتری چابهار، ایران فعالیت می کند و هیچ کشتی اسکورتی در نزدیکی آن قابل مشاهده نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/139443" target="_blank">📅 20:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139442">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ تو هر دو رقابت قهرمانی باشگاه گلف خودش تو بدمنستر نیوجرسی، قهرمان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139442" target="_blank">📅 20:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139441">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مدیریت آینده تنگه هرمز با ایران و مشورت عمان انجام می‌شود
🔴
بر اساس بند پنجم یادداشت تفاهم پایان جنگ، مدیریت آینده تنگه هرمز باید توسط ایران و با مشورت عمان و گفت‌وگو با کشورهای منطقه انجام می‌شد.
🔴
در ۲۲ یا ۲۳ روز نخست اجرای تفاهم، مسیر شمالی تنگه کاملاً امن بود و کشتی‌ها در آن تردد می‌کردند
🔴
پیش از پایان مهلت ۳۰روزه پیش‌بینی‌شده برای بازگشت ترافیک دریایی به شرایط پیش از جنگ، «مرتکب تجاوز علیه ایران» شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139441" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت خارجه : در حال حاضر با عمان درباره مسیری برای عبور در تنگه هرمز گفتگو می‌کنیم که نه مسیر شمالی باشد و نه مسیر جنوبی.
🔴
واشنگتن اجازه نداد حرکت کشتی‌ها در هرمز طی مدت مقرر از سر گرفته شود و پیش از پایان آن، به ما حمله کرد
🔴
مکالمات آقای عراقچی با مسئولان پاکستان و ترکیه هشدار و تهدید آمریکایی‌ها به پاسخ متقابل درصورت اقدام علیه ایران بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139440" target="_blank">📅 20:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: همۀ دوستان و همسایگان باید بدانند که تبعات هرگونه حملۀ آمریکا به زیرساخت‌های ایران، دامن همه را خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139439" target="_blank">📅 20:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
عراقچی: مذاکرات ایران و عمان در مسیر نهایی شدن قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139438" target="_blank">📅 20:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139437">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552a5e4a47.mp4?token=gibq9JVfhy6cZJ9U_dEXy_SIU9U6j0Kt8S-S0jjXFOwkjHhMGzKKln2JIkoVUFUQ7A8rzqBV_rSjzOMclUMgIADKJ7INS-uj44qBk17oc-vCOu7aNhUNo11KH9D-N4eDffhrunLnSERtATEuXnvHuJblkizvNhHpiAREBqbjaI-YYyFYF0YKoh14gwiOx8WvBsTYxYAYiXJ_bkfk473KtKRBCx9k7mmB5neYSX_0vuJWlyWtBr6ijwLGMmZ8ymSAuzlhs4FamX5nALZp9BcfIVHaywZ10FIrc0rGX7Y03oRRxdBzq92xIzvDnG8OctpN1qOKxBpq-BXK51miU4H3pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552a5e4a47.mp4?token=gibq9JVfhy6cZJ9U_dEXy_SIU9U6j0Kt8S-S0jjXFOwkjHhMGzKKln2JIkoVUFUQ7A8rzqBV_rSjzOMclUMgIADKJ7INS-uj44qBk17oc-vCOu7aNhUNo11KH9D-N4eDffhrunLnSERtATEuXnvHuJblkizvNhHpiAREBqbjaI-YYyFYF0YKoh14gwiOx8WvBsTYxYAYiXJ_bkfk473KtKRBCx9k7mmB5neYSX_0vuJWlyWtBr6ijwLGMmZ8ymSAuzlhs4FamX5nALZp9BcfIVHaywZ10FIrc0rGX7Y03oRRxdBzq92xIzvDnG8OctpN1qOKxBpq-BXK51miU4H3pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی: امروز صبح در روسیه، به یک پالایشگاه نفت، یک پایگاه هوایی نظامی، یه مخزن ذخیره نفت و مکانی که برای ذخیره، آماده‌سازی و پرتاب پهپادهای تهاجمی استفاده میشد، حملات سنگینی رو انجام دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139437" target="_blank">📅 20:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139436">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش در تنگه هرمز مورد اصابت موشک یا پهپاد قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139436" target="_blank">📅 19:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139435">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت دفاع ایتالیا اعلام کرد یک نیروی نظامی مشترک اروپایی یک نفتکش ناوگان سایه روسیه را رهگیری و متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139435" target="_blank">📅 19:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139434">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
جروزالم پست: امریکن ایرلاینز پروازهای نیویورک به اسرائیل را تا مارس ۲۰۲۷ لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139434" target="_blank">📅 19:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139433">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
حمله انتحاری در شمال پاکستان ۷ کشته برجا گذاشت
‏
🔴
پلیس پاکستان: در جریان حمله‌ای انتحاری در حاشیه تظاهراتی در شمال این کشور، دست‌کم ۷ نفر کشته شدند.
‏
🔴
تاکنون جزئیات بیشتری درباره هویت عامل انتحاری یا شمار مجروحان منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139433" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139432">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ اگر فورا پیشرفتی در مذاکرات و توافق نبینه، میتونه هر لحظه عملیات علیه ایران رو آغاز کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/139432" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139431">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دیپلمات ارشد ایرانی به وال استریت ژورنال:
ایران در حال بررسی حملات موشکی پیش‌دستانه به پایگاه های آمریکاست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139431" target="_blank">📅 19:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139430">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سنتکام: از زمان ازسرگیری محاصره بنادر ایران، مسیر حرکت 35 کشتی تغییر داده شده و 2 کشتی نیز از ادامه فعالیت بازمانده‌ اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/139430" target="_blank">📅 19:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139429">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
کانال i24 عبری:
اختلاف و ناامیدی کشورهای خلیج فارس از ترامپ، دلیل لغو حمله شبانه به ایران
🔴
تحولات اخیر، اختلافات فزاینده بین کشورهای خلیج فارس و دولت آمریکا را در مورد نحوه برخورد با تنش‌ها با ایران آشکار کرد، در حالی که احساس ناامیدی از مواضع ترامپ در بین کشورهای منطقه در حال افزایش است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139429" target="_blank">📅 18:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139428">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کانال 12 اسرائیل:
مقامات اسرائیلی خودشونم از پست تروث سوشال ترامپ متوجه لغو عملیات شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/139428" target="_blank">📅 18:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139427">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
احمدرضا رادان، فرمانده کل نیروی انتظامی:
من یه مشکلی برام پیش اومد که گفتم نمیتونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139427" target="_blank">📅 18:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139425">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مقامات جمهوری اسلامی به روزنامه "وال استریت ژورنال"
:
"ما در حال بررسی گزینه حمله هستیم، اگر دیپلماسی شکست بخورد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139425" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139424">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال استریت ژورنال:
رئیس جمهور ترامپ، حمله برنامه‌ریزی شده به ایران را لغو کرد، پس از آنکه نمایندگان مذاکره‌کننده ایرانی (عراقچی) به پیشنهاد جدیدی از سوی قطر مبنی بر باز شدن تنگه هرمز پاسخ مثبت دادند. مشخص نیست که آیا توافق نهایی بر سر این پیشنهاد حاصل خواهد شد یا خیر.
🔴
در پشت پرده: کشورهای حاشیه خلیج فارس از فقدان یک سیاست روشن از سوی ایالات متحده ناراضی هستند. همه کشورهای حاشیه خلیج فارس دیدگاه یکسانی ندارند، و امارات متحده عربی از آمریکا خواسته است که رویکرد سخت‌گیرانه‌تری را در قبال تهران اتخاذ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139424" target="_blank">📅 18:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139423">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
👈
وزارت خارجه آمریکا بار دیگر به شهروندان خود در سراسر خاورمیانه هشدار داد و از آنها خواست احتیاط بیشتری به خرج دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139423" target="_blank">📅 18:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139422">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf749ff64.mp4?token=YAEkYD9iI0P5y8XJRLvdy55VgtmEADkMJXScxLg4mmAcJ_B8X3RvkaXQQVWkdkcnfefZDozSDyjq9gkaiPO_sTz0sEfvBuEOO0QYXdJrjm-hBp2bnzehDEuhXKe60jj5BMLN9xWYc8FIRoIr6CBHqeqprdxatewjU5qEKfxFKNbV-SF1qbbZFtsyD8mcByumYmz2YeOX8sMjFawsnnRa7HgK5lthspOf_874Xa0Wf56NUUgiaEpd_LAw0AlkewpfPeD39mMN5kED0qGle1hDeJXhlHAt_4bF-X3UQNJdXXUn6w0ESyM6yWAi2Id8lrQZWxniey3HHlEN0sRUN2hjMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf749ff64.mp4?token=YAEkYD9iI0P5y8XJRLvdy55VgtmEADkMJXScxLg4mmAcJ_B8X3RvkaXQQVWkdkcnfefZDozSDyjq9gkaiPO_sTz0sEfvBuEOO0QYXdJrjm-hBp2bnzehDEuhXKe60jj5BMLN9xWYc8FIRoIr6CBHqeqprdxatewjU5qEKfxFKNbV-SF1qbbZFtsyD8mcByumYmz2YeOX8sMjFawsnnRa7HgK5lthspOf_874Xa0Wf56NUUgiaEpd_LAw0AlkewpfPeD39mMN5kED0qGle1hDeJXhlHAt_4bF-X3UQNJdXXUn6w0ESyM6yWAi2Id8lrQZWxniey3HHlEN0sRUN2hjMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: هدف هیچوقت تغییر حکومت ایران نبوده، هدف فقط این بوده که ایران سلاح هسته‌ای نداشته باشه. اصلا میشه یکی رو بدون دیگری به دست آورد؟
🔴
مارکو روبیو، وزیر خارجه آمریکا: حکومت ایران باید تغییر کنه، شاید نه به معنی تغییر رژیم، اما رفتار این حکومت باید عوض بشه.
🔴
اونا میخوان انقلابشون رو به کشورهای دیگه صادر کنن و این باید متوقف بشه. تنها راهش هم اینه که هزینه این کار رو انقدر براشون بالا ببریم که دیگه نتونن ادامه‌اش‌ بدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139422" target="_blank">📅 18:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139421">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اکسیوس: در حزب جمهوری‌خواه، جناح قابل‌توجهی استدلال می‌کنند که نباید رهبری حزب پس از ترامپ به ونس سپرده شود
🔴
بسیاری ترجیح می‌دهند روبیو نامزد آینده حزب باشد
🔴
یکی از بزرگ‌ترین حامیان مالی حزب جمهوری‌خواه، گفته در انتخابات از روبیو به جای ونس حمایت خواهد کرد
🔴
ترامپ توانست حزب جمهوری‌خواه دوران بوش را شکست دهد و آن را دگرگون کند؛ ونس باید ثابت کند که او نیز توانایی انجام چنین تحولی را دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139421" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139420">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256951396a.mp4?token=LWv4_oEAhbdNiOmt_jIF3bXRqwC5SpdjhjfDYAA7u5laFsqwYpl3u4hDdtnct1hl7bLn0xhMLZrVeGHulSvcwjUALce2GK3GXHNDKhmxyYs6b7eYTGpnmXM_DiYwqs93gScvMKSbl_PYNg-rvYzgkgbwBWhJtWjkxfv89j_zNf6rHW1uUJMz1GXB3ExhbxDjLFBe3cQ__HvFt2f2P9Vq1sPd1KP1kmYQ3eQuLCPLTEhc_YdMMGPYLvrYc0gBBm0U-zBnnmU1GM2cD6RRBgVX-vuhLZ8kAkZx8IMbORnx6qobfFKIWH2bfBjYGuh4XkeJKMyEcxyFBZ54VyC_PrWVSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256951396a.mp4?token=LWv4_oEAhbdNiOmt_jIF3bXRqwC5SpdjhjfDYAA7u5laFsqwYpl3u4hDdtnct1hl7bLn0xhMLZrVeGHulSvcwjUALce2GK3GXHNDKhmxyYs6b7eYTGpnmXM_DiYwqs93gScvMKSbl_PYNg-rvYzgkgbwBWhJtWjkxfv89j_zNf6rHW1uUJMz1GXB3ExhbxDjLFBe3cQ__HvFt2f2P9Vq1sPd1KP1kmYQ3eQuLCPLTEhc_YdMMGPYLvrYc0gBBm0U-zBnnmU1GM2cD6RRBgVX-vuhLZ8kAkZx8IMbORnx6qobfFKIWH2bfBjYGuh4XkeJKMyEcxyFBZ54VyC_PrWVSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو تا هلیکوپتر اطفای حریق موقع مهار آتیش‌سوزی تو یونان سقوط کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139420" target="_blank">📅 17:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139419">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEuJ1a-6b7Usk6jSPKaTKMfaAQk5TKoBsVkk2bm5noPN-fs9qVvs3ZLSgsRWez-EeS_Vh0aGY3MH9lycJxN18e4wzQ78fauXdf2YT1xaWOQqvrAi9cmMQD3nyA7x7nK-JArdwnu3P1TeIGID2jYwURQu4OBJaI4lMFoxd0lzHTeWDWRmFsThZA68XQfJaiigqslbYrTLwNLrSoQ0tmqpeURgB6XI-HNVnQ7vE7bvD0U7wFjLSQtRKHbL7GGDokHWJar75N_f0y0JvqM47qqnsx7m3eTs-Xw_wSC9UXvhicacdRECU3Eq34iGtco9E8zwcssvXqmMi5zjGgSnpYA-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار بی‌بی‌سی: راهبرد ایران در مقابل تهدید آمریکا نابودی متقابل اعراب است و چه بسا که اسرائیل از نابودی متقابل دو طرف سود ببرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/139419" target="_blank">📅 17:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139418">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سپاه: توطئه خلع سلاح حماس با شکست راهبردی مواجه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/139418" target="_blank">📅 17:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139416">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPRso5woSVyPE7wUqjXRy_CoVMiT0HwulBGqWUgJya0my7dOYQCuUZIucVURehqXzn4fzoF1t17DM2JoER26ByeppjPn_sdUQDh4dgqt9wGBon9yBp_CKAkPgWQJlnkX3pnJf8Ap4BTkwNILIT6rSeecYk-xWPQVPH8KZ_2q4L7og-Ey1812RKcmU7nN8tNY5e2yS6BcBMAGph6fF_DrhTBOBFweHU0Ny94-aYnp0_88IEM9YRmMyG3VfQDPL2s2l0XGBtyDKUirr6wQ6WHLw4LhxdipYCPmd33vV-wGoCo6pz5_-XnuVM490PU58ZTwaDuLfCgiYGiSu3wHUU3o6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTxN4tYsHV97ZiCkVQnhBtHy32-YR64BciHin9IreIeNw1MEDNNnkc-moUjPeh_R4o02flcz6vXKNALBT8X6y_ojK8TzHLNpQckwTCPZwuFY2v7zoql6dR8AEGw9MFayMji_F4c9zCx83-WHClJq53bU5Z__zie2l_vLjz39aLXIyI4VP_GtjzvvgrNohIGw-cGk-STbR9RaPnGmmEczObBgard-Qfo7fBChGss_ER-Q7UXj8myY7ix5ySZ_giy59n5n94v0o2y48heKqjzCCugP-qFVsaorhv52q-tS2jCcvV3c_VBR9HfAD2AmI4QFOEBVWAtLLAxApycpVyWm-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در حمله ارتش اسرائیل به یک خودرو در غزه 2 تن کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/139416" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139415">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=IydkuAkv4KSyxSFh_Qlu1JwuRiq-xAR6k3ozV5eWvITQMQDoLl9DNfKybibZkN-jlQokGGg5DgDUBkETpEVrN2jKnjLwvySRaTSR5n1iR94k0I_BP1pVWjWnP3aRQUZbpprdirK3uX-RgcQ9SI2VHytsboKdHs_yyrQNJlnJphScZ1ihepvMwDbLK2UDsWj0SxE4Wy8GeNwNbFQqACVYonwhmXu9cFN14uvK0tXGByvFuzS3mGi97sxrZyKosvXlOzDnxf_B4nDYH8spnnNrZDEQMyZjudMbDzyb4d4sSNtdagkPUgvgj4XdRyEsWeDwZQfWMPkNiQ8QZ8nnBBXO_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=IydkuAkv4KSyxSFh_Qlu1JwuRiq-xAR6k3ozV5eWvITQMQDoLl9DNfKybibZkN-jlQokGGg5DgDUBkETpEVrN2jKnjLwvySRaTSR5n1iR94k0I_BP1pVWjWnP3aRQUZbpprdirK3uX-RgcQ9SI2VHytsboKdHs_yyrQNJlnJphScZ1ihepvMwDbLK2UDsWj0SxE4Wy8GeNwNbFQqACVYonwhmXu9cFN14uvK0tXGByvFuzS3mGi97sxrZyKosvXlOzDnxf_B4nDYH8spnnNrZDEQMyZjudMbDzyb4d4sSNtdagkPUgvgj4XdRyEsWeDwZQfWMPkNiQ8QZ8nnBBXO_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای پی‌در‌پی در پایگاه التاجی به دلیل آتش‌سوزی در انبار مهمات ارتش عراق رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139415" target="_blank">📅 17:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139414">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk9G0fo94I8jIcXy7zQMI6desiDGouIGRjk4MkBhL5XvknElLFjzpc9UvsqxPNBbWjLhJ936qwr1mJT1fdmOYmH6tFQiPa_MlMVhIeHsA-6h6JA2R0U_kUcqodS-hDg5JnxnLWlsMqG8QwebOs4WJfvx2MiQGXCmMhFYWLFJHwgt174oGCRSq6O6DrUsez6I0jw1Tc_kqF2ctMqQ80jV1gXv0V6UfXve0PdJY8p9Dlq7B26_Wz6fBEnwUIn3TypVscheICym23MFIc6OfxHxyBnOabX3sMsC8gRLFkR1SFhvfq7JMU5P2Crep8UYJ1FI45nIl7pIwdjvPFp--JFzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همسر حسین رمضانی، ماموری که در ۱۸ دی تو میدون علیخانی اصفهان به قتل رسید : یکی از اعدامیا موقع اعدام گفت آب میخوام و بهش آب دادن و این اعصابمو خورد کرد،واسه چی به آدمی که اینقدر بی رحم بوده آب دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139414" target="_blank">📅 17:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139412">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr5SG_C1V67rrMv28endwvuZ18elr2eUCE0rS44G3BPEYsZ3hT569mOZl3MvoinnbeQONRM-5oh1PqdOVdr4QehXr8dv6rQOnkMjzzisVXaUnAXo3vBJGm3I-yQ0ZdchZRrQ5wqIjDn1qFChqB0rCLGHSGLy3IBa3wMV5GZs8m19Qnoz0JWwBKjznsMo6DInxl7C1q2IaHLje0DjhYL1dAyGEJnivVXrPtJ_84HAWXzYvm7M3FJfNzwl1PPNs_kOl0u1mhQjtWQeKz1ZnhAI1EKiuOD_Xl1Die_VEcCOKNjGk-0eu1RGDhpSSLf5kOYovyfe6c1o15Y6HyvzRt2hNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUP43WZ9GfzyDROHIptdKqPpIWcJhbvzaX53ZbH1dFuTcmlqMJYO4F6D6iuep7uQGIad5Bi1zEhTC71KsRHseNwm4lKOSAIgTwb-ON_GPbICgDlInrZPvGF-k5zMWzNwiW3RZTF9JKWBZwieVvMRGKZE821LJdn_CSIn7OXE94BE1Be62TbhYLWNKH3IAgsgGUYEViejEjkyRA4wBXZ0oefHnchs_-Ydlhfrd7iOtkLhS-Gv4kH0qRKZs90Fr0F6526DircEZH_shpZyWVnxcl6NnJIDs14982Q7TSuG5Db2lJnRl2odQh8ucZacknfqVF2rubDkiCt2G3ljtsIbtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای تانکر KC-135 متعلق به نیروی هوایی ایالات متحده که در تاریخ ۱۳ مارس ۲۰۲۶ در یک سانحه هوایی در آسمان عراق به شدت آسیب دید، صبح امروز پس از انجام حدود ۴.۵ ماه تعمیرات در فرودگاه بن گوریون، از اسرائیل به سمت ایالات متحده عزیمت کرد.
🔴
این سانحه زمانی رخ داد که دو فروند هواپیمای KC-135 در حال سوخت‌رسانی به هواپیماهای جنگنده بودند که به سمت عملیات‌هایی در ایران در حرکت بودند. یک فروند از هواپیماها سقوط کرد و هر شش سرنشین آمریکایی آن کشته شدند، در حالی که فروند دیگر با وجود از دست دادن بخشی از دم خود، موفق به فرود اضطراری در اسرائیل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/139412" target="_blank">📅 17:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139411">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی دولت: تغییری در قیمت بنزین ایجاد نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/139411" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139410">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سی‌ان‌ان‌: ترامپ با وجود ملاقات با نتانیاهو، او را در موضوع ایران و غزه ناکام گذاشت
🔴
نخست‌وزیر اسرائیل به شدت خواهان آن است که آمریکا جنگ علیه ایران را با جدیت از سر بگیرد
🔴
تل‌آویو معتقد است که واشنگتن برای دستیابی به یک پیروزی عجله دارد و بیش از حد آماده مصالحه با حماس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139410" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139409">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En9FQkvTtIP8m6YXntWjiEAhV3nn8cnEMD5NFht47BPpIEqTm1rWpoO0zZ-_4NKY61EqmskK2AlqT8JU_IDJrBvd4EvE1EfClmHBmDrBgf5eMiE97wIVg976UlCZJ0Cxu4cCb98H5Aqc0C9RVSbdQGwwVOqbilhPAlTlw-mQcKRW8tro7a4HaNJSGY4RRBmAiwj6u5WpRGQPFYQlB-3nw8VcMRm8QF8gu21joV29rckB3AmzXgEQaP_fEAREVgjPgN1LztMX1ncUhw8wHPzA4mLoUM4fK5e2ga8IWElW5J4Tzih08-uoHAAtePT3mxOtarMke_CKA-wQKSNDBjs8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
🔴
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139409" target="_blank">📅 16:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139408">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTpPeBN-5cDf4rOh75mAxZxyUAw-9hEgc6Ek4pSix5SEB9zZH42zCIOo4y9pjkmq4zB3Curo7AIS4kEtZfq4tdpjgAIiU24EFhjFH9CujBhsOVGEA6rEGgkU51Uc7ewWOHezWmmCQIT1ITwf8eRA5a3dV0ToUOzZF15b0b5zBXo7jJfNYh4qpPBngRoQWXnESeoBtUpS1wDpKvdExW0aO9EbTrfhar7VitYJSnOVfbUleqrN_fIpE6Mo4hfqbELBq9Hs1qX7bAdODyYw46adf6DHOeKtOMLTuV1NGAtPnQKOyoTeVUGqIHgWhaY4YEDhWqnQx3B_UX38wOwZHyk4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایتالیا به طور موقت، کنترل‌های مرزی را برای مسافرانی که از طریق هوا و دریا از اسپانیا وارد می‌شوند، مجدداً اعمال کرده است. این اقدام در پی بحران مهاجرتی اخیر در سئوتا انجام شده و قرار است به مدت یک ماه ادامه داشته باشد.
🔴
ماتئو پیانتدوزی، وزیر کشور، گفت که این کنترل‌ها با هدف نظارت بر تردد شهروندان غیرعضو اتحادیه اروپا در منطقه شنگن و جلوگیری از مهاجرت ثانویه به ایتالیا انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139408" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139407">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
قوه قضاییه: اموال سردار آزمون همچنان توقیفه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139407" target="_blank">📅 16:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139406">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBF2_9dJyoLrw-Wnoa_S3MJo9JvO7DZEeGwAI4to8CbRLcwKYjCqFap8nBWgmCqWk0W1UpzHnfPaE7Vme7370MLxpxKu4Q4mY-KWcCiprd4CwAuCiu46vWNxFqhItIZRlPGV-ExHe3zzGNQevKWTv_MaPkXskk-72ebOhf83FQYJA3fV0maTypNOPPhH6DA-Lo6QJCOHeR0ekW4eUfxOrT-WtpCVv48tXxNj3cnVWaTM_AIKJ2IIcFp2Lh_W5_L9KGAGCppKhS7axDs63gIcLFL7VRaMfh9L_auKG1e3IPL554ZgQMno9uK5aGOQpf1c8FMDE4grL1RVJiEz7iwoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین: جنگ آمریکا علیه ایران از کنترل خارج شده است
🔴
دونالد ترامپ به جای یک جنگ سریع که هدف آن سرنگونی حکومت ایران بود، یک درگیری منطقه‌ای را آغاز کرده است که خطر اختلال شدید در تامین انرژی و قیمت‌ها را به همراه دارد و باعث رکود جهانی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139406" target="_blank">📅 16:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139405">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی: در بخش برق خانگی، طبق وعده وزیر و معاونان ایشان، از اول مهرماه جاری به شرط تداوم شرایط فعلی، هیچ‌گونه قطعی برقی برای بخش خانگی نخواهیم داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139405" target="_blank">📅 16:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139404">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رویترز گزارش داد دولت ژاپن به‌زودی اعلام خواهد کرد که توکیو و واشنگتن به‌صورت مشترک برای حمایت از ارزش ین در بازار ارز اقدام کرده‌اند
🔴
این اقدام مشترک با هدف تقویت پول ملی ژاپن و کاهش نوسانات بازار ارز انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139404" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139403">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آناتولی به نقل از منابع پاکستانی: قطر و پاکستان نسبت به اینکه مذاکرات میان ایران و آمریکا «به زودی» از سر گرفته شود، به صورت محتاطانه خوش‌بین و امیدوار هستند
🔴
میانجی‌ها انتظار دارند تا پایان هفته جاری، نشانه‌های مثبتی درباره شروع دوباره مذاکرات ظاهر شود
🔴
واشنگتن و تهران از طریق میانجی‌ها در حال تبادل پیام هستند تا برای پایان دادن به درگیری‌ها به مدت دو هفته و آغاز مجدد گفت‌وگوها، به تفاهم برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139403" target="_blank">📅 16:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139402">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4CqJT_3UQnwYTg5xOZC1PjabciYkF7ZHzcNjB3Lq9Cgbjf-cgygbXPJqdE_-kCSCzHSHxub4LWW_Yh5WE2P54y9y9eMps6RML7YUspU5DSfVmWc6FBxwtn4xRGkQpGB-bWHgueJUPQcr4EgCU3N8ghZeJK6Eh1yqPrsrGrBYOHXhPhAbMiTfm7GvpUmwtcxRyZ1-bbDakjEcxDMmhi8Mozm8QSqTGXD0ucXp8tOkSjNrE4dHfaIxJRkPqc1UFT0YiENoGRIpoIx3Tp-b2HAEOzAWEAyLj2l7bw1aaIydfVGUldm1wbCfQQ5wrSAShiF_79ec-2GxkqKGWni_YPydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید نیویورک پست: انقلاب در ایران ممکن است «هر لحظه» رخ دهد؛ رهبران اعتراضات در تلاش برای مسلح شدن هستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139402" target="_blank">📅 16:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
برق ۱۰۴۷ اداره و بانک پرمصرف در خراسان رضوی قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139401" target="_blank">📅 16:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139400">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8KEiCzExkRZgzBXxeZDdrrhRlBsqVikBmssVBKb8QkX5GM9xCqlHdTQXJLUc_ddsGroB6uW4YxxkATPKEF2ryfFvPo4wbXcMiH9dewxSqKaONxx4QooRFvP3v7VLfomvePvNKsVB61LhPFUFZbgQtzMzVBMTXGlDpOThe-yv5K9fzapehD7h87oV8UopaVd9yoJMrRdg4avmt_BPhthm1tzzkgsJJopjEfsM61Cda-RVoCDCxKSMNU6XyrycrPt9uVAZKCfxoH4DuFAY3T35KdNowlEDWeVVG6vm1moZ5HA2HjwtfiFbihGFigynihIN-47lnMwjvLe7Tcst7KYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: یک گروه رو به رشد از جمهوری‌خواهان سنتی که پیش از ترامپ فعال بودند، معاون رئیس‌جمهور، جی.دی. وانس، را به عنوان جانشین احتمالی ترامپ مورد انتقاد قرار داده‌اند و استدلال می‌کنند که او بیش از حد جاه‌طلب، کم‌تجربه و بیش از حد همسو با تاکر کارلسون است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139400" target="_blank">📅 16:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139399">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c11034b26.mp4?token=MSCRJ8geJEjrYUKo6T-gQOwPXVub_r0pR65X3zdDxe7iKrY6noSqbGu4kkwHdN9orOIgE39CMNAMYvK3oDSWIszklx2NpioCNaxG6N8zzc72HVexoe64F9Qrw8bw4jIFJ7OKmWsp8VbHhZxR5WVVZNc_RdgplxiVhA-25uM_LeGLznV1ApQ03vDUP7pLhf9ER20fjVSr5svkIMTmJKN083FsmtvW3aZRTKueUu28QlBsDNQ7zGNabwFYe3JvXCF3d4altEWFWbwhLBlnBo0dawSEQvHZSZLR45XploP-ECrTSeTi_tIHn0mgrpJxnqntuW0fu-IHK5qZbGQ0uwPFCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c11034b26.mp4?token=MSCRJ8geJEjrYUKo6T-gQOwPXVub_r0pR65X3zdDxe7iKrY6noSqbGu4kkwHdN9orOIgE39CMNAMYvK3oDSWIszklx2NpioCNaxG6N8zzc72HVexoe64F9Qrw8bw4jIFJ7OKmWsp8VbHhZxR5WVVZNc_RdgplxiVhA-25uM_LeGLznV1ApQ03vDUP7pLhf9ER20fjVSr5svkIMTmJKN083FsmtvW3aZRTKueUu28QlBsDNQ7zGNabwFYe3JvXCF3d4altEWFWbwhLBlnBo0dawSEQvHZSZLR45XploP-ECrTSeTi_tIHn0mgrpJxnqntuW0fu-IHK5qZbGQ0uwPFCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بوسه‌ امام جمعه‌ طبس به چادر داور مسابقات والیبال کارگری
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139399" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139396">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0RbhlqHKvdkktPycKXJMgV0uIH-mvUg_2FwBp6a3lOpfH_FY3Mg-FqZVOj_ciC1vTC3csmSy31yaEIbfn7LSdP8E81WK4jQU0QlcY0uP4aQ46idztdF5kTt5mg_ejL4uMl-A7sT5_twjw0jvM_qnMlEt5Yd0AOnazw6PREoWYlueTkILO5FovNm-r97x8cJMRRsTbKhHwI17ggWGnKEdfZIrm_pNgjqojcetWun7o1nawzWg3qIBBf-i9nta3diSJ5uq11yv2Edbh-dzMmy8N1Ha-fkCvUOsR4VE_ucnk_aqe6ZmzoB4V9duhxA-eLWeqIgivqFTzRhnyBv1u-y1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOpvOjhO_FkMHLHF73jn5IrgUqzRdpmNC8__k-B7vhtaGSi-JdINSENA3DeRtOu8t_wSkDCJ1BxWiIgp4A0KSIWqRlr4Lv4QFeuKgzzGjuJ6QhBdnt4h9mbFvLheUZhOpybCza9ezr9jTeG6joMG-CR-Rzbtf5y4ttyD3nxXLYnacxtc5VT_DWyxrjJQY1DeMfQY0MwdFp0KDpb3xKchiHX1vmCbm8bfO-Mz01AZSdhu3bu4EArerPfMQRVDY-6WnypfSrv-tftbQgwYUksHAlVliaBOib7eHnCgNhAauXtf87v3C-bKczDhfwceBYbuGJ1JvgW2zI6P5dUbG6-c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsPvLlVj9Mw6GOVUnx_8WnknJU5OaSGck_wX1UmVy2K0jRtD5yJ8Vqaf5Y6iTATApPhzHvv7vZeEzmE0YsthysOk81vE5QVfbwKaT6CEaHqxXrhub-bbF9B3MdNSnOUbIujZw8LdOFFxh8g0ggKh8XpDJdw7DrQGeYZXtL7Fjk8JeaoFHmSs2mgbpzirE4apEjGuSUS4boi4ZUfQanENgq4EmFOYrWGpq5pTkrcWeyajSHXB_NTgmzPuHcH0FHEEI6J-4gvhAnH4CfEAQq2Qk-CxXLvjvnQWmSmuVYgGuOAzAqqJAT7UH-5jHi0vLUsLo5BED6q7jf3yaezQiYex0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک کشتی جنگی نازی که در طول جنگ جهانی دوم غرق شده بود، در رودخانه دانوب، در شهر پراهووی، صربستان، و در پی کاهش سطح آب ناشی از موج گرمای بی‌سابقه در اروپا، دوباره سر برآورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139396" target="_blank">📅 16:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c72ef2d60.mp4?token=I7S3OlnaDm3l5v8C2DF55T9mR8pvvdT9z8fLVQgAUAOblkoFvVCZJu0tAJyXrvfvw8IXVBqYl1Gj00Oyh_3D1wkhrpXedvMsUj_kJZYFZ1bxIn5OTxkZW7Yx8zg3HnTWEW0TeKvTRNQ06dyz0WGs4VPhqJRxctPrC3X-w5MfGeCOzAxaLUW15ogLah4M-Q-AGiPgAa2mJdNLIvcrBuoEQ3jZW3y1tHbXTGjnsUt4zhBkV-g8XbpYQ4J7N4vvj98iB6omiCoUmIw_gEB3t8wGYSR-qSX652qejx-WlvF1IY5gYZAZbXU6pTUc_FNVtqBzB4lpsAzbk3r0iLxv2s6v30TQtMgh2QUv507HR2FK3os40rrqHrotjVMP9e2cOSlRXaGje7ux-dC_4KuSF03i4bRIlaJ1fsN4Oh4n4S19LbIY6WsKPclJpMfPsJjsxyyOie20dhL99Oue6WKqrXsvOMJRrZJ_Doec-msq1L4yjvFFI0IrZ_qkfWQmGRf2GAXpD8aQPzZ5Y_prZWPzwA0Z9tTLhe79V31-_bUA_QESQtJ7o5bmHnJdSaMvL8sX1SRk0SZyhgJN31Nji6czeWTdveC3r3MEh1ISydoummltNNwWAwMFvJwIwAC05e2VS1dETLaIkg5d7wu9k2hwn5Vc8GpbNe9tuKGeCWuP7ofMdnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c72ef2d60.mp4?token=I7S3OlnaDm3l5v8C2DF55T9mR8pvvdT9z8fLVQgAUAOblkoFvVCZJu0tAJyXrvfvw8IXVBqYl1Gj00Oyh_3D1wkhrpXedvMsUj_kJZYFZ1bxIn5OTxkZW7Yx8zg3HnTWEW0TeKvTRNQ06dyz0WGs4VPhqJRxctPrC3X-w5MfGeCOzAxaLUW15ogLah4M-Q-AGiPgAa2mJdNLIvcrBuoEQ3jZW3y1tHbXTGjnsUt4zhBkV-g8XbpYQ4J7N4vvj98iB6omiCoUmIw_gEB3t8wGYSR-qSX652qejx-WlvF1IY5gYZAZbXU6pTUc_FNVtqBzB4lpsAzbk3r0iLxv2s6v30TQtMgh2QUv507HR2FK3os40rrqHrotjVMP9e2cOSlRXaGje7ux-dC_4KuSF03i4bRIlaJ1fsN4Oh4n4S19LbIY6WsKPclJpMfPsJjsxyyOie20dhL99Oue6WKqrXsvOMJRrZJ_Doec-msq1L4yjvFFI0IrZ_qkfWQmGRf2GAXpD8aQPzZ5Y_prZWPzwA0Z9tTLhe79V31-_bUA_QESQtJ7o5bmHnJdSaMvL8sX1SRk0SZyhgJN31Nji6czeWTdveC3r3MEh1ISydoummltNNwWAwMFvJwIwAC05e2VS1dETLaIkg5d7wu9k2hwn5Vc8GpbNe9tuKGeCWuP7ofMdnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک کشتی مسافربری با ۲۷۱ سرنشین، روز یکشنبه ۱۱ مرداد ماه، در دریای جاوه دچار آتش‌سوزی شد و عملیات امداد برای تخلیه مسافران و خدمه این شناور در حال انجام است
🔴
به گزارش خبرگزاری فرانسه، این کشتی از شهر سورابایا، دومین شهر بزرگ اندونزی در استان جاوه شرقی، به مقصد استان سولاوسی جنوبی در حرکت بود که دچار آتش‌سوزی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139395" target="_blank">📅 16:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc8c6cc96.mp4?token=fOOw-cJMuKMEklXJqZnsk40BdDCEQuaq6Kozh5ip7Xj239NKLKzqESuC1wMK3PBquHPXOZeFfnsV3qYeSB4hSdzQA2YYoKHXzCw-PVd5IS_nH8g61pob7Jai3bhaMyMnQJi4iv-FE5-MSX_wEhXVgvIgjgvgNkL_D8LyiCsTDREkuxwQw699qogvrZvFLS3FyLlHVmGyvsSUVTrUPAZezSDtWvDRI1h0dApCAu4YfLa6v3_LI4s00mpagQgxl9lTuDySji6FKcWnOBAMR8-IO_y614z_qSLt_t1YK0cSquQxVnmtqNR2OWl1V3nBXKkbjvZfDyC2nNY4YB5bGcR7RCsTzKn0THGpg6O6lr9JkH6XWcJWIjYB3u04zs_freT6jn9Wx8nctQMJLDJ3eZvVnnT3mqT6qENpnJWRdzpXJX7iSMxTS3rZuOhcOdfB9AtdgCecPZ2AGhT6WtyGN761QXiY-YabiG4TpeHbhGx5rlFiZ5ExdXJ_ot_qbLWO3snHyuB38BRCO3kBBD7sqLbuiOLNQ3eIBWs3RFTi-Pl2id7efJUUyRrxgwKgsZwgqhy-RuBWaWu_iqqU5CKBL8eLtOD9i7Pc_z8k9pEseps-gl34-5SobU9feqYuqABSCS-mks0_-9v6JIkk2dttqSfR1cVo3QJHw-IQfQ3IhtuTM0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc8c6cc96.mp4?token=fOOw-cJMuKMEklXJqZnsk40BdDCEQuaq6Kozh5ip7Xj239NKLKzqESuC1wMK3PBquHPXOZeFfnsV3qYeSB4hSdzQA2YYoKHXzCw-PVd5IS_nH8g61pob7Jai3bhaMyMnQJi4iv-FE5-MSX_wEhXVgvIgjgvgNkL_D8LyiCsTDREkuxwQw699qogvrZvFLS3FyLlHVmGyvsSUVTrUPAZezSDtWvDRI1h0dApCAu4YfLa6v3_LI4s00mpagQgxl9lTuDySji6FKcWnOBAMR8-IO_y614z_qSLt_t1YK0cSquQxVnmtqNR2OWl1V3nBXKkbjvZfDyC2nNY4YB5bGcR7RCsTzKn0THGpg6O6lr9JkH6XWcJWIjYB3u04zs_freT6jn9Wx8nctQMJLDJ3eZvVnnT3mqT6qENpnJWRdzpXJX7iSMxTS3rZuOhcOdfB9AtdgCecPZ2AGhT6WtyGN761QXiY-YabiG4TpeHbhGx5rlFiZ5ExdXJ_ot_qbLWO3snHyuB38BRCO3kBBD7sqLbuiOLNQ3eIBWs3RFTi-Pl2id7efJUUyRrxgwKgsZwgqhy-RuBWaWu_iqqU5CKBL8eLtOD9i7Pc_z8k9pEseps-gl34-5SobU9feqYuqABSCS-mks0_-9v6JIkk2dttqSfR1cVo3QJHw-IQfQ3IhtuTM0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آی ۲۴ نیوز عبری
🔴
بنی گانتز، عضو کنست : اسرائیلی‌ها باید بدونن که کارزار علیه ایران کوتاه‌مدت نیست
🔴
این یک نبرد طولانیه و ممکنه سال‌ها ادامه داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139394" target="_blank">📅 16:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نشریه اکونومیست گزارش داد چین اندکی پس از دیدار دونالد ترامپ و شی جین‌پینگ در سال ۲۰۲۵، ارزیابی و آزمودن واکنش متحدان آمریکا را آغاز کرد.
🔴
این گزارش می‌افزاید پکن از آن زمان تاکنون به‌طور مستمر دامنه فعالیت‌ها و اقدامات خود را افزایش داده و فشار بر متحدان واشنگتن را تشدید کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/139393" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139392">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkvcLtMNKdF005yBHcTvKOeWUhgbEgj_VCW-dT7yJKb1hE4HIAzbKIVGjp63PUg4MCaHVQjD9ebRcBWQVwEp1VnL6ExjjdnWvroDlZKSZIAbaU6ls3e2cQppL6U4Gjml8CTcX3DKvQ6LMKRvjeDDA0PzipKSbS6xiq4UxOcYHDpopL8GlmVJbk51eHHHfo3da8KNYNWWvhzhSi3ooulVdPu8OSAdPFGtu-CNp4U4lqTGuH6OXuBIY6oEEmV0rwdGjcc31bheUr25o51C66Tt4hqOuw6oSuBCupyAc191u32yPcHWK8eFoB5cLGwHNlU0dt30_jfts9YFBkRPZNz5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چرخه مودی ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139392" target="_blank">📅 15:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139391">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق گفته است که توافق شده است تا یک دفتر برای نمایندگی ناتو در بغداد تاسیس شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139391" target="_blank">📅 15:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139390">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ادارات خوزستان دورکار شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139390" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
