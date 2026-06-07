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
<img src="https://cdn4.telesco.pe/file/P188c6ks6rkT5Ja_bHCdfIzk3UpLqLIGVsUlnHYVGSqbJpdaqLK2ViVZhAgHNWnNP7lc02s5ZJUU03ZhWAtqbVfdHMxsOL5rbkgW5qfeMq8LRdjowyQujaLKv7yYqJjVD53W5usaGfRVY_Qt4b9YzBrL7czuarcJzqGWLRFTezGQbmy5LDFDiuVGrmFYkxmZJcJqycj93_8Af2NLJFeyfYOfR9cUwk6beWXI9qNiD-UwlTP_jLuwltRBa2tuc3RW9tyzBtoM6QJzNMnQSafdjW44Veh1PNSZtMx1o_v742gd54m-OGWSwonjsZVRRQO0pEQ3ti_GU1SMbHCVZj19BQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 12:03:12</div>
<hr>

<div class="tg-post" id="msg-656782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69564d38f.mp4?token=T18PzCI_0_Jy8GlJKcgM-48nolIxYSpHzjMTEhRxYsOCtBr7dTq_HNioxA6ViFuUMyoiibV95RSGVublGO_30CYjYq9TG5MHzQCfQuuEvysNq5QBbKROpdeSoDCaO-SKOgjCRKFWe2QLCMk0Lo3F-Ba-SmKOrRXOtj3Njo5noXNCBWkWElD9Nfn7XY9Mp5YcAU4vmLidBnwinm_NheaCKHfYTIk0VlHHXzunW3OM7PJe8N8cl3EowKsg-mxo4U6cUTIlPQM56mqK-VFlmiWFIz65pChvZ_brGIUFbqmyCqzi7tlVk8IZxYUEjtnQ-9fw2wBUhIRPtdnXW6MOFZXk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69564d38f.mp4?token=T18PzCI_0_Jy8GlJKcgM-48nolIxYSpHzjMTEhRxYsOCtBr7dTq_HNioxA6ViFuUMyoiibV95RSGVublGO_30CYjYq9TG5MHzQCfQuuEvysNq5QBbKROpdeSoDCaO-SKOgjCRKFWe2QLCMk0Lo3F-Ba-SmKOrRXOtj3Njo5noXNCBWkWElD9Nfn7XY9Mp5YcAU4vmLidBnwinm_NheaCKHfYTIk0VlHHXzunW3OM7PJe8N8cl3EowKsg-mxo4U6cUTIlPQM56mqK-VFlmiWFIz65pChvZ_brGIUFbqmyCqzi7tlVk8IZxYUEjtnQ-9fw2wBUhIRPtdnXW6MOFZXk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در شرق دمشق
🔹
آتش‌سوزی بزرگی «بازار الهال» در شرق دمشق، پایتخت سوریه را فرا گرفت.
🔹
به گزارش رسانه ها علت وقوع حادثه در دست بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/akhbarefori/656782" target="_blank">📅 11:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656781">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF1Xwk0WrmMqzPxHCjR0TubB3LfPHyBI8fokfHLPhKNvIAljUUMqaDPx1PV--2YQFgfOL39W842xyQnjriM3AgyAYONrFTX63y_KlhZsAEO0zzZOlBw3TDbAJ6qJFdeJ2HdkCNrHq2VoQ_YJFYi7fMEVPYB93llSthGwCLOC4FdFFYCfhwNV-sdTM28wB-aBsTl9qEmAHeiy3EymwllCTyCSMfwHBu5KgjTrX6W0W_xA7QBOyX3zjaS16bI-YBK0vWDLxSkUWjC27BkC1CIcgGIrz5QkXplCIRNEYCUjnueBrYPCf8oXgRKlO296Pj3rfeK_nkjr_LeYQ7D78Vemcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور پاکستان با عراقچی دیدار کرد
🔹
محسن نقوی، وزیر کشور پاکستان امروز یکشنبه با سید عباس عراقچی، وزیر امور خارجه ایران دیدار و رایزنی کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/akhbarefori/656781" target="_blank">📅 11:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656780">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
آغاز عرضه گواهی اسقاط خودرو از ۱۷ خرداد
🔹
عرضه گواهی اسقاط خودرو با نرخ جدید از ۱۷ خرداد آغاز می‌شود و نحوه اعمال آن برای خودروسازان مشخص شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/akhbarefori/656780" target="_blank">📅 11:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656779">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKSVmL72poh9xVavKIAHLfYK9aF8IgqxHc7yVS1OK4tNzOy3dwnUYqok1AybGLnEYlBWqZKvRh2MBfFcZpQV3TDWvNX3dewUVp-PF9ge80aMI5xCuKbzdV64mMiPLBNOJM4L6AvijNMi64Pls0iZaUyhiDfaP_iy62LoLXxiwnvP2HnwurtrwzoiFneDk-Z9nSL6J8Ci2Ze2RomAizaGdvjbKkgS6catmhpoo9UFEJUZhhwwV8gL_5c7OmHn8Zxf7mOGxdX_csP8oX9e3WP9X_LvB5tyU8127S7RjCZaXRr6CmXqqxYpR5dopQZoyOo-ibd_DfGZmaTDJxZJljd6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور پاکستان با عراقچی دیدار کرد
🔹
محسن نقوی، وزیر کشور پاکستان امروز یکشنبه با سید عباس عراقچی، وزیر امور خارجه ایران دیدار و رایزنی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/akhbarefori/656779" target="_blank">📅 11:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656778">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
جزئیات ویزای تیم ملی برای بازی‌های جام جهانی در آمریکا
🔹
برخلاف برخی ادعاها درباره «ویزای ساعتی» تیم ملی، پیگیری‌ها نشان می‌دهد اعضای تیم یک روز پیش از مسابقات وارد آمریکا می‌شوند و پس از پایان بازی به مقصد تیخوانا در مکزیک بازمی‌گردند.
🔹
پیش‌تر سفیر ایران در مکزیک گفته بود تیم ملی باید در روز مسابقه وارد آمریکا شده و بلافاصله پس از بازی این کشور را ترک کند.
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/akhbarefori/656778" target="_blank">📅 11:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
معاون رئیس جمهور: تا تراز اكولوژيك درياچه ارومیه هنوز ٣ متر باقی مانده!
شینا انصاری، معاون رییس جمهور و رییس سازمان حفاظت محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
سطح تراز درياچه ارومیه ١٢٧١/١٠ متر بوده كه نسبت به ابتدای سال آبی یعنی اول مهر ۱۴۰۴، ۱۶۰ سانتی متر و نسبت به سال گذشته در اين تاريخ ۸۰ سانتی متر افزايش تراز داشته است.
🔹
مساحت پهنه آبی درياچه نیز تا تاریخ سوم خرداد، ٣١٠٠ كيلومتر مربع  می باشد كه نسبت به سال گذشته در اين موقع حدود ٢٦٠٠كيلومتر مربع افزايش سطح داشته است.
به لحاظ شوری نیز در حال حاضر غلظت نمک حدود ۱۶۰ گرم بر لیتر است که نسبت به سال گذشته حدود ۵۰ درصد کاهش داشته است.
🔹
با وجود افزایش قابل توجه ورودی آب به دریاچه در حاضر تا تراز اكولوژيك درياچه هنوز ٣ متر باقی مانده است. از این‌رو شرايط درياچه اروميه هنوز به پايداري مورد نیاز نرسیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/656777" target="_blank">📅 11:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ9DOqZs7zHEaahbIfoveWavp71hW2nSE3QS-9u_GwazTsHK4QoEuGB-s4UIaOj2Ywjy_bLrDWuYoPTEJeEVb34leoQud9jAo1_LHy7QIlg_ZD7oEYHMIkHMKI9oLc0UdCYmFxlJz0D-dV6qTstjsAmkINalodZ2pMwukwoKxr6XxAeg4ygjnst20hflcPySEfkRvacBPVgDbKBNPKEDi_DV90WDdfPOCkPomn_62_Z0i75yFZXOAbn8HMmCxdrz1Pk2jhwhCc0_PwB_QA1OIvxg8KNmXqNT2qUOmWXKzcygQ5Vd1ONQhFFMBRw_gGgj_CHPBqIfCfgJEsLNlPdorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمام فینال‌های جام‌جهانی در طول تاریخ با پنج قهرمانی برزیل
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/656775" target="_blank">📅 11:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e851e12eea.mp4?token=VhTBHcJZhK99-FBB15qkrOzjODfpV8aqtsVtxf_suJ6XweTD5SPSRyn5oqH2YtagM5g4SeoJc_KThHnlICiAy4X3z2kDidwdvm5q7CJKAf1AQN-QGsGsjmQwEZiwpotmVGW0r4IKUOJQZpfhYCBQO8TOugzUaykacRMOs3nUbMDVlVWbr0RuvNVR1QE5eSBmYai9D3jQBSGMTB3XoygMSWYFVcvYKn83tzyWIwDYCKx8lIGw3neEOwuEvW9sYNoViASgCr-hz0D3GsSI8oeRF_FEpXxlweTsNBAxIVM5tOpRxK6i7ee2iXVZHNX61Hp9V4Xbzc_QTfciFz9emfpBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e851e12eea.mp4?token=VhTBHcJZhK99-FBB15qkrOzjODfpV8aqtsVtxf_suJ6XweTD5SPSRyn5oqH2YtagM5g4SeoJc_KThHnlICiAy4X3z2kDidwdvm5q7CJKAf1AQN-QGsGsjmQwEZiwpotmVGW0r4IKUOJQZpfhYCBQO8TOugzUaykacRMOs3nUbMDVlVWbr0RuvNVR1QE5eSBmYai9D3jQBSGMTB3XoygMSWYFVcvYKn83tzyWIwDYCKx8lIGw3neEOwuEvW9sYNoViASgCr-hz0D3GsSI8oeRF_FEpXxlweTsNBAxIVM5tOpRxK6i7ee2iXVZHNX61Hp9V4Xbzc_QTfciFz9emfpBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه دیدنی فرو ریختن یخچال طبیعی در گرینلند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/656774" target="_blank">📅 11:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656773">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGMCw1B4CPO4NBQScy558t1JdqRPReMYiU_VTrux33eUloGhv45_9ySGv_j4RcAnk3H1pgExUxhuM3k49ryFdstXOjrMindPA7wfdw7fOuS63spzCgmkMNttWlIJR6N_tUYX0yVVK5X3xL1AJ3fhn2OlOzO7yotZWsuBSpqfisxbvIq_7964GNIXtSw2pplAsy3jaWOvoLVf4kaYlK86QWYjcPjEG8UiqTGNUNQqpQdFxpPZ-g4Balvkx4cFMvDtKqRJkjaYRLyCU-h9qj-06myyS7shIEJ8_FvvkpZ43o-W7u1d5tfLo6Yi9aRofvb_1hvf7TtTyzgYycr5OFoDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir
نوشهر
📍
۶۵۰ متر زمین
۷۰۰ متر بنا
تعداد خواب ۴
مهندسی ساز متریال عالی
فول فرنیش استخردار
شهرک ویلایی تکمیل
سند تکبرگ و مجوز ساخت
محوطه سازی حرفه ای و زیبا
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/656773" target="_blank">📅 11:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aisadZ6Mfgla89aQo8GWtKoZKias1lILeI5369Qk7JhSeJJpkAzb-lBlI8z-v-K_INitZ61VM3EU3C1r9KNrOa4otEXIUsoJTcoByV80ZfZreKv7sLGfg_3emElQJqfbRwpuqpyNAAAN0GG7l8IQ5KdfuiCSd-HnowVn18IQ0dhbAUgKNWOtYcSX4qradnr9BcpVTYdeYoLHOtbKCy5aXBpTjGcEwN10BC8hn5JFd7mQ13I9-bRqMOPEMd8_1Ep5YpzVPHN32XIAPy7ZsSZegE2SYUI7e-6m9PZbRZhA99ZHpoeN9hCGZPypnO2T8Um0YSYFF898krsnYEzyt_WWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: تا عقب‌نشینی خفت بار اسرائیل نبرد ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/akhbarefori/656772" target="_blank">📅 11:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656770">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b5b35804.mp4?token=j4cUAuauWqhpX4URlnIawEF5GTIuqXYjB7tevSp4oBjZVkE9Bt4-wmqnywmm7ZvXfkh_0r5aa9q7EUKE8ze_FPE-05pCZLIhOpQxsqogrwZkGuqUIP8oNHKXsHwbbevUlWhhE56_t9bJMkXnPzt4iV9r4i3zMuQQm0xlNmwO4qwxsnNHNeAj1IWxa-8qFRR_L-8muIsLXWfVMc4dreWgXrRPPOdxHrWFTQ1OQR36cUmqw2k0KxHJXJHNFQtpx0hEJrvNb-1Rn4u7bWXE9279rpNV30ZyUXdcAuYM6jNhgPKNANU7_Oi9R1myW2sfY8FkAfE5f005LRUbnoJtk4goWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b5b35804.mp4?token=j4cUAuauWqhpX4URlnIawEF5GTIuqXYjB7tevSp4oBjZVkE9Bt4-wmqnywmm7ZvXfkh_0r5aa9q7EUKE8ze_FPE-05pCZLIhOpQxsqogrwZkGuqUIP8oNHKXsHwbbevUlWhhE56_t9bJMkXnPzt4iV9r4i3zMuQQm0xlNmwO4qwxsnNHNeAj1IWxa-8qFRR_L-8muIsLXWfVMc4dreWgXrRPPOdxHrWFTQ1OQR36cUmqw2k0KxHJXJHNFQtpx0hEJrvNb-1Rn4u7bWXE9279rpNV30ZyUXdcAuYM6jNhgPKNANU7_Oi9R1myW2sfY8FkAfE5f005LRUbnoJtk4goWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی به چادرهای آوارگان در شرق غزه
🔹
تصاویری از حمله پهپادی یک «کوادکوپتر» رژیم صهیونیستی به چادرهای آوارگان و شهروندان فلسطینی در محله «الزیتون» در شرق شهر غزه منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/656770" target="_blank">📅 11:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656768">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2138dffc55.mp4?token=e-rvPZm0djVM5f4nEb0y8WYKSWm0Y869QsvEYKAw-zJ7-h13cYwG1sD-gKYZadbnp-m-p76Gg3CNKSLuPiB8bX6PMLhPNUXxwU_tfEpA1Ob1NdC57K0xQnNj7kQ08Z6E-v93ffwpBOpwCcSoP9kvoMstonVs5h-w6HS1Z6nxzivW9mjCV0bNac6uiBY2qwr7IV-ZjF7GZwylb2Tq3XKbr4MfuP1XEfcWKLLaMukt6V3J0zsEmQz6Hrr3TDFLu-iMw5EdEoaRkzlDjFXurdrcdi0D0hgjOXT766ZLR_jczrKFL1_Rhy42eud7AdYHVSHn24iG0vWM_J7oDvXHBhrhLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2138dffc55.mp4?token=e-rvPZm0djVM5f4nEb0y8WYKSWm0Y869QsvEYKAw-zJ7-h13cYwG1sD-gKYZadbnp-m-p76Gg3CNKSLuPiB8bX6PMLhPNUXxwU_tfEpA1Ob1NdC57K0xQnNj7kQ08Z6E-v93ffwpBOpwCcSoP9kvoMstonVs5h-w6HS1Z6nxzivW9mjCV0bNac6uiBY2qwr7IV-ZjF7GZwylb2Tq3XKbr4MfuP1XEfcWKLLaMukt6V3J0zsEmQz6Hrr3TDFLu-iMw5EdEoaRkzlDjFXurdrcdi0D0hgjOXT766ZLR_jczrKFL1_Rhy42eud7AdYHVSHn24iG0vWM_J7oDvXHBhrhLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک‌ پست: پنتاگون به‌اشتباه با موشک ۵۰۰ هزار دلاری یک بادکنک پیشاهنگی را هدف گرفت
نیویورک پست:
🔹
دولت آمریکا در جریان ماجرای پرنده‌های ناشناس(UFU)، یک موشک
۵۰۰ هزار دلاری
را برای سرنگونی بالونی شلیک کرد که بعدها مشخص شد متعلق به
سازمان پیشاهنگی
بوده و ارتباطی با پرندگان ناشناس نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/656768" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656767">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aba2cc55d4.mp4?token=snFUWeZsdZzOxzZ19LnZd8in21r3IwvXNmnylbu-lozhQgzRGOSmntcOesbgW8sbs08VlfuZbhUIsYpMLqKO53Shz-aivR6jxxUlMnyIlCJPLlG-vZgBYhUaBXAN0LhUflS1vRn8DpPSpgBfSuiaPOv5LxotA6TVy1F85WaAFXBslyM3zdBnsnWL_3gcDKK7s4gHGvSJYPbwKi9286oi6J1Z8udsA0FYOxZc-7GA4vDh9NWCd63us5IZh97QSBHGuvGHLsIIWeaJnn77e5c6va-8Iz-4Hl7ARGjet6us9ieRqUgmyWPpYXuuP6NJBWv2Vb2KabVjFZjeu1WuJl_0oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aba2cc55d4.mp4?token=snFUWeZsdZzOxzZ19LnZd8in21r3IwvXNmnylbu-lozhQgzRGOSmntcOesbgW8sbs08VlfuZbhUIsYpMLqKO53Shz-aivR6jxxUlMnyIlCJPLlG-vZgBYhUaBXAN0LhUflS1vRn8DpPSpgBfSuiaPOv5LxotA6TVy1F85WaAFXBslyM3zdBnsnWL_3gcDKK7s4gHGvSJYPbwKi9286oi6J1Z8udsA0FYOxZc-7GA4vDh9NWCd63us5IZh97QSBHGuvGHLsIIWeaJnn77e5c6va-8Iz-4Hl7ARGjet6us9ieRqUgmyWPpYXuuP6NJBWv2Vb2KabVjFZjeu1WuJl_0oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما را به محرم برسانید فقط
🔹
شستشو و غبارروبی گنبد حرم حضرت اباالفضل (ع) در آستانه محرم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/656767" target="_blank">📅 10:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656766">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4292617c2.mp4?token=IhzytgxXuRy7htdt1jq42mLzkPaK-gNdOFetas6fCGwy1q5MlOKn_CDinxexh2Fez6p8XFEVFY7jbbE2MuGXRv2igAUl02g-bReozFS_agixwbFijDOGTzmj2ixVsQTUjS9l_GNG0dVaWxFtGH_-gISu1teAhVZwJAVlPecTOlXjBICx_d1WH9IOUjCczAbLWpbAw3qO-jYWTN3IVzDJxh07pezus2wWPXwZ0AHdYPVJONoLT_XYKQfq_gOw8Sbsrbd0iiAbp05ggNLIr2UHtr1i-qvTIdgahNIMVLx0u1_V4uyfY7Ui8IujWxuBLgfCE6rtx8Qu0a5wCYRv5bubDjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4292617c2.mp4?token=IhzytgxXuRy7htdt1jq42mLzkPaK-gNdOFetas6fCGwy1q5MlOKn_CDinxexh2Fez6p8XFEVFY7jbbE2MuGXRv2igAUl02g-bReozFS_agixwbFijDOGTzmj2ixVsQTUjS9l_GNG0dVaWxFtGH_-gISu1teAhVZwJAVlPecTOlXjBICx_d1WH9IOUjCczAbLWpbAw3qO-jYWTN3IVzDJxh07pezus2wWPXwZ0AHdYPVJONoLT_XYKQfq_gOw8Sbsrbd0iiAbp05ggNLIr2UHtr1i-qvTIdgahNIMVLx0u1_V4uyfY7Ui8IujWxuBLgfCE6rtx8Qu0a5wCYRv5bubDjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حکم کشتن ترامپ و نتانياهو صادر شد
آیت‌الله جوادی آملی:
🔹
امروز ریختن خون ترامپ و صهیونیست‌ها خواستهٔ امام‌زمان(عج) است
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/656766" target="_blank">📅 10:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
بقائی: کودکان نخستین قربانیان جنگ هستند
سخنگوی وزارت امور خارجه:
🔹
برخی از آن‌ها بر اثر گلوله، بمب و موشک جان می‌بازند و برخی دیگر تا پایان عمر با زخم‌های جسمی و روحی زندگی می‌کنند.
🔹
میناب، نمونه‌ای از «جنایات آمریکا و اسرائیل» علیه مردم ایران است و در همان روز در منطقه لامرد استان فارس نیز از موشک خوشه‌ای استفاده شد که با انفجار، شمار زیادی ترکش کشنده را در منطقه پراکنده می‌کند.
🔹
صلح و امنیت بدیهی نیست و نتیجه هزینه‌ها و رنج‌هایی است که نسل‌های پیشین برای دستیابی به آن پرداخته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/656765" target="_blank">📅 10:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7301e98b8.mp4?token=f5MRdgfMUVhWEK7VNugRsa-P5UdjYXbAkV4Hj3CMEp6wI7ApF6kiQ-VMG3WUbuhJvJ8aeODJfVc48Xig5dyrDcT6emPEU2lk1ebZCtRs8Rk5kgGb_Co1EtrzhgaS_W1vzIzr5t_Ter-YCSDrdJQPnNGTt40IwMpEulhNnJRJEHQ1wLtLFAIl64DatdMRIUEyr7mqdkLcM0CGZ4r69dWU4wSMRW1SQQx__dsvSedTM66ZNp1XCQ5YjuHKBi_Qe5nSzRPjzup3NZa5g8m1sLMuP-F80JlyBX5KHHEGT1RiF_G3Ug9LISzdFRn8_y4noOoZ9I75Co7QT0QeM05yjBzu7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7301e98b8.mp4?token=f5MRdgfMUVhWEK7VNugRsa-P5UdjYXbAkV4Hj3CMEp6wI7ApF6kiQ-VMG3WUbuhJvJ8aeODJfVc48Xig5dyrDcT6emPEU2lk1ebZCtRs8Rk5kgGb_Co1EtrzhgaS_W1vzIzr5t_Ter-YCSDrdJQPnNGTt40IwMpEulhNnJRJEHQ1wLtLFAIl64DatdMRIUEyr7mqdkLcM0CGZ4r69dWU4wSMRW1SQQx__dsvSedTM66ZNp1XCQ5YjuHKBi_Qe5nSzRPjzup3NZa5g8m1sLMuP-F80JlyBX5KHHEGT1RiF_G3Ug9LISzdFRn8_y4noOoZ9I75Co7QT0QeM05yjBzu7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین خیمۀ عزای محرم در کربلا برافراشته شد
🔹
درحالی که تنها ۱۰ روز تا محرم باقی مانده، این خیمه با نظم و تزیینات ویژه برپا شده و کربلا را در آستانه عزایی باشکوه قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/656762" target="_blank">📅 10:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
معاون وزیر نیرو: هیچ برنامه‌ای تا امروز برای اعمال خاموشی‌ها نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/656760" target="_blank">📅 10:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P36hX8MHCCmbWfLK2dbROOrfEzMVOVtFV23hZLPaQLbvTCmdCnET6ZNftEvPG2cXirEKYWyppKAsjofH6vdo3RcEuSY2cXzA7p3Qe7QSbinAnxHFmDRj_kZiRcFkcKHQaCvLx64BdscF3TvDyypKon_Q3kTPftusry9_4MiWSjtvhdwjhXc2-HNAeMcTzh9OYmbKWbRSU8GWIJRYnBsHYyUlfJrH9w7Zuf8m_NLL0JottVVccU9_YxyG0UonCfUglwSQ8bE5t2IFxj28LhO-vlaEk6w92CjEZNDiaQRm2jiiUo3ZhGQPAHeuMpVrm7MgtuvYbN_b3zsgY_A7dUlYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز یک شروع پرانرژی؛ فقط یک لیوان آب ولرم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/656759" target="_blank">📅 10:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpl7w-jUisGydnDxXBkeusu1lmfHbc2UtnmQ8WyT-OwHmFGG2uvvlaF3K6JUVubP1Q9SnDgNuzoOm8V1Ovc9ynEQuvIfqB4gl3ufm5Dzm_Dxi7MWJtbHIS2yMrYd-Sj7klTAZZ1zIuectRIP0w-A8JMwQ1EtHbn9-s4K37rYPwBUvot2APIVuQeKrtUzM6jhMbiCW7aAjnfuyffJDMmL5sNaqEZkGOI0s9tEFaupFiEOkK8ZQdaVnnxCCy7wAhaGEZknl5ydyg6sDNKrKYryUc6LXCY08IQWVvEX-LAQ1gl5DU1hFxR9Dxhtr34RA_PTOVCIoGLNrhMTggPeUyxYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس تهران در یک ساعت از آغاز معاملات امروز ۸۶ هزار واحد مثبت شد و به ۴ میلیون و  ۴۷۸ هزار واحد صعود کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/656758" target="_blank">📅 10:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
آغاز مسیر تیم ملی ایران از سانتیاگو به تیخوانا
🔹
تیم ملی فوتبال ایران پس از توقفی ۲.۵ ساعته در اسپانیا، سفر خود را به مقصد تیخوانای مکزیک از سر گرفت و پس از سفری طولانی وارد محل استقرار خود خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/656757" target="_blank">📅 10:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9518161dc9.mp4?token=MolouWFvjeRGZNnf-0dT7RGn-tAORP4yfnDqbkw9w0ImqcqxFvdJ654ozg6_CSI7AK8_CbnJvWmsQIvcJaWOtt4XsGlSzJMQYW2T9CWhNvOjHiszSISRxqt9P4Au-YWHjyjp7rC_l-tRIFovPbKHjYx3KHnO1u8_zFk76aKBJ6DeR2nKqt4iTFO8ZzPVeloZCim027KBRi7c9GiR7a0OrPLKneAVg-2A3USxLj6GnPCJ2nIUU1-MtEEUxs9_LopuLLy0gw4_7J7cn1Dw3bC6mSvH4TM6w8_1J3atVa3AyGnRD7c5o7tTLJ1-rZJgqbY9Ngrn0S1vjoCH_crqbI6X8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9518161dc9.mp4?token=MolouWFvjeRGZNnf-0dT7RGn-tAORP4yfnDqbkw9w0ImqcqxFvdJ654ozg6_CSI7AK8_CbnJvWmsQIvcJaWOtt4XsGlSzJMQYW2T9CWhNvOjHiszSISRxqt9P4Au-YWHjyjp7rC_l-tRIFovPbKHjYx3KHnO1u8_zFk76aKBJ6DeR2nKqt4iTFO8ZzPVeloZCim027KBRi7c9GiR7a0OrPLKneAVg-2A3USxLj6GnPCJ2nIUU1-MtEEUxs9_LopuLLy0gw4_7J7cn1Dw3bC6mSvH4TM6w8_1J3atVa3AyGnRD7c5o7tTLJ1-rZJgqbY9Ngrn0S1vjoCH_crqbI6X8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار هالیوودی با خودروی پلیس؛ متهم دستبندش را باز کرد و پشت فرمان نشست!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/656756" target="_blank">📅 10:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_KudCFnwLsPIB-uhBbDpNObHiJ5tlvRYKs-9_ffw_D08OhW9at55gBL7fB7RnVRWsgRxQKIEpapI2Z5YYyOPqfN5e2emrTF3qVj_5Vd2dCy3eaXd9Fer66Q6wNhGIGIFOffg1nC0zvfv4lsLt1w7fr31s0XfKIJSA36jGl5am6DrgC7QJirt5vMsEY9fDzVwUYqKYOCdana0riEDAf6m5Ju3qQmElv1tPm6vVKUDczbPfDfpouxWaEuU10XcVERgAcbglD47RnEwqNf5ds264iIC6ByZSdLhgfNK6eNFZjZewa551tZ-AFw4I-xbra_87Znc27L8mUCHCMsEtdHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/656755" target="_blank">📅 09:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656752">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLcA-udFINUsrkqw9CsPcBYFxg46Unt5ItIRxF4pcJ3wdmR5XbjfAdDqLZAx0NwNimH7LZkdjGOpMfjl3LWWZeU2m7befFjpn_G7SL-mi-debsXMs3jJHHkMaokXVSMOaXMxIAA_mudGzOZtMJUkz10dr4GowxwB-3SmCEopm5v1lrbB-j9cFnWXJfpj8euKRp1vljLYm1NUENdjHbx3Fj24E4ueUnfUIGGJ2KMvhMxlUHaPPNyFHXfRg56eESryPUHua-dCEsc6yX1QPVHCONY16ye7hkYsGPqOcm7-a5M43x-IhCpUKXbETfJQh0HlF-BvBBppq33fIbJ1J3Sm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRRXcWvmQjCsN8evsIp8_M_YvA2kO3Y7OzxhCUMplXW5rzhUUetGokA64NeRH6WKvUOk8YlRi-ujL0mGKLF_zDu4a3l7gYJs8MOFfa92OSBDXrTkceJlSqVLJMztdJbZE5xeCdFwzZQKiQvXvVcsY-Em2B4Cw0A-p2HdSMDzlkenYAZz-Yv75rWQZWEwyEmW1bwTof7iUs3C4pTRJ8Ouu5mbxd-3roY1-bmXwqRs74k76y_6n_lrx7YDRvh-GHuBGJsuor25gZfniwJ4GcZ2ktr_cuWpg7p_VGkinsVkcEhq3eU0PMX7ea2X6Ro8YI-AtYKyXHNhYLnGhpBp3EdRsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgJMXxMGAmorLFxVCwKitR9mda-Ik6ntmH3scDQ12d03Qkfh-fL2Emw4ypag3HmTUzn1hmdKQxcHBauZckeGCt3f0z_V11VPuQldihqLj5JQV-c650zspXJGeLdhfrCFO9ITak_vhiGaNIDnjjWKZwvmc2Irob59StVtrMZoCfnl19SflmwfLqbcs7q-4JUetlxNcrBSt2iECJwmdcOG0ac35gM7d1PTCDHCW4wGsEXccw4Vq_MVm9DhXVtNs9zA_V82PouYAsOsTcenxdjNdv7ZrqC0J34iQhBSn0pl_QZYO4t12ncr9iKAAKRgJ7ylXVbG0fiho0qwxz6rf-NQww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصادف مرگبار پژو پارس در محور کرمان–بم
جانشین پلیس راه راهور فراجا:
🔹
یک دستگاه پژو پارس در بزرگراه کرمان–بم به دلیل سرعت غیرمجاز از مسیر خارج شد و با تیر برق برخورد کرد. شدت برخورد به حدی بود که راننده و تنها سرنشین خودرو در صحنه حادثه جان خود را از دست دادند.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656752" target="_blank">📅 09:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e0e5bb6b.mp4?token=H-bTI3yvJMjUVWjy4522O4boDKnKXQ1cVES3YZ91FzSWMQyl22VQck_DhtDJTTRPHBmtA953fySjnJAEL7wcUAKVBvILNPWuiPeul2GoX_ifC7bgvBseuGZb-qK0RVmXFzOOVL-wCRiXP_BtcVMJituiVmNrTVq06GSfA4rQf3pXYbKSWPgs0yrVkVkXqa8fTVeVAt_RGMh4k8tZeUYhjRtmYJ6xZb04H_7Y0GlsHZdUOJyLK0KALF0jkuekUJ1BIYUMyUbVIo1q7AMWxd19sDrdoPATQFzdDCs8MMImq5W6yQd4WC4dI80ymxL_niHkmD3BT8ayqqKsy19t_u4RBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e0e5bb6b.mp4?token=H-bTI3yvJMjUVWjy4522O4boDKnKXQ1cVES3YZ91FzSWMQyl22VQck_DhtDJTTRPHBmtA953fySjnJAEL7wcUAKVBvILNPWuiPeul2GoX_ifC7bgvBseuGZb-qK0RVmXFzOOVL-wCRiXP_BtcVMJituiVmNrTVq06GSfA4rQf3pXYbKSWPgs0yrVkVkXqa8fTVeVAt_RGMh4k8tZeUYhjRtmYJ6xZb04H_7Y0GlsHZdUOJyLK0KALF0jkuekUJ1BIYUMyUbVIo1q7AMWxd19sDrdoPATQFzdDCs8MMImq5W6yQd4WC4dI80ymxL_niHkmD3BT8ayqqKsy19t_u4RBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران فعال‌ترین آتشفشان ژاپن
🔹
آتشفشان «ساکوراجیما» دوباره در حال فوران است و شهر «کاگوشیما»ی ژاپن را در خاکستر آتشفشانی فرو برده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/656751" target="_blank">📅 09:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656750">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSc8aQ-RFXOrD1xXCoUzYWO4KNljvV1HfIq4fzlGmFpD8QzMQuC4uLeb272lro6nXhVF8-kiQN171sR65dGjkwH1BZYA38vVj60updwDnF1IsdygdKToGB1Qv3vqq6qqDBZH0rBrYAD2UI_cUVkYqQSs2YJiDuhB6Z1YAWa697vElLhMpcRLeGnPCy8BdPjyXCdp0kbG33xFkkBfCIvfItahU6pNXBDEsv7zY94E69QLebkYgwfql8Dh0oL1uoPuDcP-MKNuDDtdnTg_Ah5FfOcdbanyTkOGxFSzKf_b_ZNL7EMJmqxsvc-Auusrmb9qK-YWeduGFUCPopSUsuLy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیک‌تاک با اولویت دادن به ویدیوهای احساس‌برانگیز به جای روایت های رسمی باعث شده ۶۴ درصد جوانان آمریکا تحت تاثیر آن مخالف جنگ با ایران باشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/656750" target="_blank">📅 09:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656749">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c78TekoP0wXd3QUcoU5eH4r_nhYVtUr2ZERW6Eh9JGjhOVo7YaNe-o_AodaqWTuWiY-LSP-gL1DK_B8uWlPJyPfM3J87puTLYRiE7DsqBy7sNGNPbXP-316Sc6wCMY9AzB1yqNoaTyVU3Jk-CTujuv1uhlq4mZHMIsK80daU0LNeTU5xKg58VL27bHxdJdmMXstca_IxIbf-_cpAAJJ3AxXwKgUahtU71yxUcD5edmjSUnzYGJV5yHhJFnivbdeWUM7DaDqm8aqS-V0qmU7WgQZT4roRPgoP-fPSBYrpm9Wv62peb5vvkZ1dVhPfpoL6SODI-TyEBnaCumsWUpLQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس روز ناسا
🔹
عکس روز ناسا مقارنه سیاره‌های مشتری و زهره را در سال ۲۰۱۲ با پس‌زمینه‌ای از غروب خورشید به نمایش می‌گذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/656749" target="_blank">📅 09:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656748">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
روزنامه صهیونیستی معاریو: مسئولان ارشد اسرائیلی از اینکه ترامپ در آخرین لحظه حمله اسرائیل به بیروت را متوقف کرد، ابراز ناامیدی می‌کنند؛ آنها معتقد هستند این اقدام باعث تقویت روحیه حزب‌الله شده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/656748" target="_blank">📅 09:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656747">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MsU0ogIKONTKi3A6uVWEefnwbxTBtoIOnhbUgW5Vx53CM6pWOE4D-pidNHvjlY9itckKAHqvo80l9Kpk0Y8w5qD4c5KcN1jx9KkHKFV2-oOZMo-RfyZ7IwTFr4ZDv74BuLzO7YD7gRmB0Om8U5t9r-zryGwjucFj0BuBvdNMTd-ANqQAZtyZfhsOOW0MtA_B7h_3FnqeVrmQvcbFLb4ANUIRJWFLNY4NTbwnZLcYvSjf7cvuccYdGUKJoL4F1UKwvo5-CMTL_-uGjchJLfOav1uf9YtQFPR-lvl8-StgywIua8DMmY9ihyB6m4LSU1lZuVcePt7aN6bSLTZXQNvUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایالات متحده از آماتورترین میزبانان در تاریخ تورنمنت
سفارت ایران در سیرالئون:
🔹
کاملاً شرم‌آور است که فیفا جام جهانی را به کشوری سپرد که حتی قادر به رعایت ابتدایی‌ترین تعهدات میزبانی نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/656747" target="_blank">📅 09:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656746">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
جمیله علم الهدی: رهبر شهید انقلاب پس از پیروزی آقای رئیسی در انتخابات صریحا به من گفتند در امور اجرایی دولت دخالت نکن
‌
همسر سیدابراهیم رئیسی:
🔹
رهبر انقلاب در نخستین دیدار پس از پیروزی شهید رئیسی در انتخابات، صراحتاً از من خواستند که در امور اجرایی و مدیریتی دولت دخالت نکنم و من همواره خود را ملزم به اجرای این توصیه می‌دانستم و از ورود به انتصابات و تصمیمات اجرایی پرهیز می‌کردم/ خراسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/656746" target="_blank">📅 09:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656745">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94f9cb3895.mp4?token=L0uOixEfCDQwF0OUVLcV4jZpEP2XZ1Jz6kuaXBxS6z0kMlQo-gjOlGX--x1-jGkwoNn3v9474XKHETT5pRfhDi-lXaPwVj3Cfvt0FoMxWHO49KqD9VfoFtQdKR7O7vRMn6rX-JGq1iJfULxjtfiaDdJ95WTjvNjs_pE2cVDGDEEosA6Lb1rTAi18uwsAbNsjMINl8q-g0aFG2IG6tS8MeqGsMofOtzpIXow3EhRM4Qjud5mDuaRvCCA2FO0xsRhl9iglV53BOHRRN0kOUVMps3ahPEROnm9NluX9GW0HRV3roxWPK3pcmHBvcabR_-53o2h7IqF8zLeKjmyETg-gRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94f9cb3895.mp4?token=L0uOixEfCDQwF0OUVLcV4jZpEP2XZ1Jz6kuaXBxS6z0kMlQo-gjOlGX--x1-jGkwoNn3v9474XKHETT5pRfhDi-lXaPwVj3Cfvt0FoMxWHO49KqD9VfoFtQdKR7O7vRMn6rX-JGq1iJfULxjtfiaDdJ95WTjvNjs_pE2cVDGDEEosA6Lb1rTAi18uwsAbNsjMINl8q-g0aFG2IG6tS8MeqGsMofOtzpIXow3EhRM4Qjud5mDuaRvCCA2FO0xsRhl9iglV53BOHRRN0kOUVMps3ahPEROnm9NluX9GW0HRV3roxWPK3pcmHBvcabR_-53o2h7IqF8zLeKjmyETg-gRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوضاع لس‌آنجلس، یکی از شهرهای میزبان جام‌جهانی فوتبال
‌
🔹
علیرغم جمع آوری بی‌خانمان‌ها از شهرهای میزبان جام جهانی باز هم خیابان‌ها شاهد حضور افراد بی خانمان هستند
#جام_جهانی_۲۰۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/656745" target="_blank">📅 09:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656744">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
کالابرگ از ۱۶ خرداد وارد فاز تخفیف می‌شود ‌
🔹
خانوارها می‌توانند با ۱۰ درصد تخفیف لبنیات خرید کنند و احتمال افزایش تخفیف روغن و تخم‌مرغ نیز در دست بررسی است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/656744" target="_blank">📅 09:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سفیر ایران در مکزیک: تیم ملی باید در روز مسابقه وارد آمریکا شود و همان روز خارج شود
🔹
امتحانات دانشگاه علمی کاربردی غیرحضوری است
🔹
تایوان: کشتی‌هایی را برای واکنش به عملیات چین مستقر کردیم
🔹
بغداد: هماهنگی‌ها برای دور کردن گروه‌های ضد انقلاب ایران از عراق ادامه دارد
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/656743" target="_blank">📅 09:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656742">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
منابع خبری عراق از شنیده شدن صدای انفجار در استان اربیل در شمال عراق خبر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/656742" target="_blank">📅 08:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/656741" target="_blank">📅 08:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656740">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
امتحانات دانشگاه جامع علمی کاربردی غیرحضوری شد
‌
🔹
امتحانات نظری دانشگاه جامع علمی‌کاربردی (۶ تا ۲۱ تیر) آنلاین برگزار می‌شود،  امتحانات عملی ترکیبی از حضوری و مجازی خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/656740" target="_blank">📅 08:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656739">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSTu9OHXhXb3CgukL6e9XXXcFIic1B8DB6ZMh00eQp41oz7Kt9tX49c-owaI2_uT3sharjxUK0NLr2vF3eo4Se_08h-_XyrmknfX_ntFYwR9hXJbhKSD6jYP4SW9zikDsDqxI1u2zhEb1S_jPDdZZ8KFh8_kgRvWZlyTJsLbBp2lq61w3vh9_z2XfYlsuxq-Ng-q-EnY4Vye-X90cmxOQWqCIYEsncvkEVPhNJ3IlpojzNolF5sdHXcsIsa6O1lHaYUtl9E31qqLktDLamKQbul3R-ZmfU9iLRHUTokhOAqGbYnjd6s83-Ocos9rlneRIeR1MM27YPFPuX2IVE4EnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از سردار سیدمجید موسوی فرماندۀ نیروی هوافضای سپاه، همراه با شهیدان سیدحسن نصرالله، محمدرضا زاهدی و محمود باقری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/656739" target="_blank">📅 08:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656738">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3f0e505d.mp4?token=KdLoEP3SmzLe1-kybBuW4IJzjOHbcz9tZgIDVy2zIblWlxLVH11JpfpbqRK7xuLEg5TKjhA-vphZk8rojYmBh9BRFMeCj6eYTtMoI0XK7fyUL3Ncj6VW7N12kFDK_8Z8jN5Pr1j048d4QU9smaXJvGXjOBJMuAZ5TYqY1hSkSNQaLwn4aDIS6FsKaVYCtqKbH4662xsx6Qb_YKdvOhznuoH_WA3pVBKRPymNeujNJ0Nlc5HmfBq1MmfdRL9JkEgNWkFjBwShlVUmIU0rejh61jrDRIYpEoJBUVN3QrGWF-_dYnJiza6i9dk-qre_Svh0-14Rjsw5InPE91dAzPo7ll_4SaINKCwYuyVUHJ9BmxZgSunpdELE9q9-kDfStVBp42hvlubxPL9V1Q4qAmBSa8BNXZ8ZRCbpp6jc9CJqQsDzlWtIVVOguhXqPM0c-z2uh5FeIwDsPNAuy5EP2yYiEolbCpXr40uKVMYo2RzHNS9TSO3q6JM7JXlb6V5KNKWHpXrv0RJWMRHNef7kTMtRkC34sp4AkpXQYRDYvnXD8g-qOUqFmbakt44-4uZWz5BxMAY0mTG1AJzGYQRnRNcjbQEOnpnY2cGV4pu1b6aaU2EmAZ0exFNUHUUdyanfPuYbwStwt93zbkQ6x45UHERu3vKbr0iTaBTO9spBszK2fhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3f0e505d.mp4?token=KdLoEP3SmzLe1-kybBuW4IJzjOHbcz9tZgIDVy2zIblWlxLVH11JpfpbqRK7xuLEg5TKjhA-vphZk8rojYmBh9BRFMeCj6eYTtMoI0XK7fyUL3Ncj6VW7N12kFDK_8Z8jN5Pr1j048d4QU9smaXJvGXjOBJMuAZ5TYqY1hSkSNQaLwn4aDIS6FsKaVYCtqKbH4662xsx6Qb_YKdvOhznuoH_WA3pVBKRPymNeujNJ0Nlc5HmfBq1MmfdRL9JkEgNWkFjBwShlVUmIU0rejh61jrDRIYpEoJBUVN3QrGWF-_dYnJiza6i9dk-qre_Svh0-14Rjsw5InPE91dAzPo7ll_4SaINKCwYuyVUHJ9BmxZgSunpdELE9q9-kDfStVBp42hvlubxPL9V1Q4qAmBSa8BNXZ8ZRCbpp6jc9CJqQsDzlWtIVVOguhXqPM0c-z2uh5FeIwDsPNAuy5EP2yYiEolbCpXr40uKVMYo2RzHNS9TSO3q6JM7JXlb6V5KNKWHpXrv0RJWMRHNef7kTMtRkC34sp4AkpXQYRDYvnXD8g-qOUqFmbakt44-4uZWz5BxMAY0mTG1AJzGYQRnRNcjbQEOnpnY2cGV4pu1b6aaU2EmAZ0exFNUHUUdyanfPuYbwStwt93zbkQ6x45UHERu3vKbr0iTaBTO9spBszK2fhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران چه بلایی بر سر آمریکا نازل کرد؟
‌
اعتراف شان‌بل، سرلشگر نیروی هوایی انگلیس:
🔹
ایران اهداف آمریکا را یکی پس از دیگری درهم کوبید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/656738" target="_blank">📅 08:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovoFF97MULu1p-na0C-GXheUVsUgirq_7UPa2eQdu1TLOzObEvcbP_YlvTF6aQ8vbqvWi5W76d1dWCWIx-Xb_PIZsDnBYjCvejM6p1yUlr3j5qfWS5TnZOU0Zu7klxaK7JQhekHTnY4_IhJvkqIM11APSJG552wEuysA319elYEZKpCm9cpHutqXTIGpFPG5uKUGRCeFxBknBKiERi_GwUau-u2rlODd6kDx1Ajroy4C3ptinvqK5rLZmR7LIJrQX3oqQ7r-v9ndxss9rrPiI-3a5U3zyjHFRosWhtEhLxe-GfZrDB5fCAbgSRkYU2D0xijfeU1AfF42SJMztqhafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امریکا در فکر بالاکشیدن اموال ایران برای بازسازی کشورهای عربی
🔹
آمریکا در حال بررسی راه‌هایی برای انتقال دارایی‌های ایران به متحدان خود در کشورهای عربی خلیج فارس است تا به تأمین مالی؛ بازسازی و تعمیرات ناشی از حملات ایران کمک کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/656737" target="_blank">📅 08:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf320a24b.mp4?token=Eldyrgf0NEVsBsyklYODaSNE-dMGu8kbxdqVp2N9KWLBFHMCSCY2ZBbhxBa4UXhLP0hnrfgBxQpyqF5QWzHX0fN7ADKRR9DRsTTGlmnIjoBM4NnFxJy9PJxix7Z8W4tX7GApv2ifuUkuVoxQJqN0i16n6fq_6OgDNx3S3XprMFUkTidTXVBENlwJmHe_Tzxki_UeebanV9WtERXKtMDnY_ZF5b6621sJn6OGQFl1zV5NiAGW7J_ckrWv3fiZ0gOGAT0UYnodCI_ZUspZNLoJTjEgGb1Hlyf5GlqLqVQfpUWGKaHgYuS8tX22QV5OsixqqWCOjl2CC4fMeAF-FQZgIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf320a24b.mp4?token=Eldyrgf0NEVsBsyklYODaSNE-dMGu8kbxdqVp2N9KWLBFHMCSCY2ZBbhxBa4UXhLP0hnrfgBxQpyqF5QWzHX0fN7ADKRR9DRsTTGlmnIjoBM4NnFxJy9PJxix7Z8W4tX7GApv2ifuUkuVoxQJqN0i16n6fq_6OgDNx3S3XprMFUkTidTXVBENlwJmHe_Tzxki_UeebanV9WtERXKtMDnY_ZF5b6621sJn6OGQFl1zV5NiAGW7J_ckrWv3fiZ0gOGAT0UYnodCI_ZUspZNLoJTjEgGb1Hlyf5GlqLqVQfpUWGKaHgYuS8tX22QV5OsixqqWCOjl2CC4fMeAF-FQZgIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک حرکت عالی برای تنظیم لگن و ساختن عضلاتی که پاسچر رو اصلاح میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656736" target="_blank">📅 08:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d89eaf78.mp4?token=tsa_obDRCHKXiRhW3NANGiCbKeJIb_Niz_XJ3hn5Wzc-Mh7p2WrBLSqktPPXUsP4LZjRPiSLcpMDdu7YhRBpfne_V4UgTnE8b4qj35-JmjnvDzU4cq02xJH0_Mqo8xmZpIrfm7eMMgmpZSn5RgIH-xELH6he3HV1O9ImpYg45-c8-n7axDNt7nxTyMV21Bpq3yd_2g_IZvOUOJfSXpS9q2DE-UnTuWQzABjoSyFXsiPgm2si3sF5nyWY39OzPcfE0-fUyz3DJnnnPbgpYQzg2Ilg-5ih_T_UXaezqYhwzadvgWHcvsmBxbzpl0TKt1-BCCIYzgJBkC4NnWv653-Q0mHBJUCWiHpKhW-uFIIyDssbvcU8T3-nGlJithVhSrQ-VXNfHF9z35utxD6sj1omtxdBJUS1s_1QFe7CxFqszrjMGxS4BAwtjRaK8Q87PBEBSW3E3IMSSBaySKoCZkLEuGr9wHaeGyckwSLeJeu_ZkoxlBBQji0SA56fyEFs32q2Lvm8t9_M0D_jfyqbH1qlPTTAsbAKvmXqlQt2CW4fEqb6HGu02tP9AEBvnoqNtKQoFocjxrC6oHYpbQBXJCO1GcfwQRP7lMoYk2-GTr9AqRyJFoPoDlQ74bkTASdOJFXPhWRlv1_qxPD56Jpld8ZNa2WoUz3p7j6E2L6ZTVIDUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d89eaf78.mp4?token=tsa_obDRCHKXiRhW3NANGiCbKeJIb_Niz_XJ3hn5Wzc-Mh7p2WrBLSqktPPXUsP4LZjRPiSLcpMDdu7YhRBpfne_V4UgTnE8b4qj35-JmjnvDzU4cq02xJH0_Mqo8xmZpIrfm7eMMgmpZSn5RgIH-xELH6he3HV1O9ImpYg45-c8-n7axDNt7nxTyMV21Bpq3yd_2g_IZvOUOJfSXpS9q2DE-UnTuWQzABjoSyFXsiPgm2si3sF5nyWY39OzPcfE0-fUyz3DJnnnPbgpYQzg2Ilg-5ih_T_UXaezqYhwzadvgWHcvsmBxbzpl0TKt1-BCCIYzgJBkC4NnWv653-Q0mHBJUCWiHpKhW-uFIIyDssbvcU8T3-nGlJithVhSrQ-VXNfHF9z35utxD6sj1omtxdBJUS1s_1QFe7CxFqszrjMGxS4BAwtjRaK8Q87PBEBSW3E3IMSSBaySKoCZkLEuGr9wHaeGyckwSLeJeu_ZkoxlBBQji0SA56fyEFs32q2Lvm8t9_M0D_jfyqbH1qlPTTAsbAKvmXqlQt2CW4fEqb6HGu02tP9AEBvnoqNtKQoFocjxrC6oHYpbQBXJCO1GcfwQRP7lMoYk2-GTr9AqRyJFoPoDlQ74bkTASdOJFXPhWRlv1_qxPD56Jpld8ZNa2WoUz3p7j6E2L6ZTVIDUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت فلامینگوها به دریاچۀ ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/656735" target="_blank">📅 08:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
خبرنگار الجزیره مدعی شد پیش‌نویس تفاهم ایران و آمریکا در تهران در حال بررسی است و در صورت تأیید، احتمال تحولات مهم تا اواسط هفته وجود دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/656734" target="_blank">📅 07:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fbb7113a.mp4?token=nwhYoEFjuCWurrz_7TAe0HiIjYwg-sMK4C9fhKqqBMhF7n1QCCvv2L1eW1yH8YHoRMhBQJWT8nSucPok1s-nAPgJyBXRPGNYh2EzO8XIYRA9pLMGHFPLxGACGHC5FxraQGzaytdS2IM7QSBBuAbyJZqpQqCaY-IsQOEdtLqdeJ-rLNAfW3O9L0uEg4sMCjGPeGcb5xoVCNiCyM1puLYHULQ0g8Q0kWEhXuCi-Ppw1vntzF-gtmHv1KrfC3jzBF9lrO0kcbl0ZFcGQC_Jo-Pdc4AuuB4FVYvdtll3nzVanLxUmf9ESonzS8Puc3_0iqPleRZ-1gUTpsOToa8GK4fS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fbb7113a.mp4?token=nwhYoEFjuCWurrz_7TAe0HiIjYwg-sMK4C9fhKqqBMhF7n1QCCvv2L1eW1yH8YHoRMhBQJWT8nSucPok1s-nAPgJyBXRPGNYh2EzO8XIYRA9pLMGHFPLxGACGHC5FxraQGzaytdS2IM7QSBBuAbyJZqpQqCaY-IsQOEdtLqdeJ-rLNAfW3O9L0uEg4sMCjGPeGcb5xoVCNiCyM1puLYHULQ0g8Q0kWEhXuCi-Ppw1vntzF-gtmHv1KrfC3jzBF9lrO0kcbl0ZFcGQC_Jo-Pdc4AuuB4FVYvdtll3nzVanLxUmf9ESonzS8Puc3_0iqPleRZ-1gUTpsOToa8GK4fS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلبانی علیه داماد ترامپ؛ معترضین البانیایی: پروژه لوکس کوشنر را متوقف کنید
🔹
در ادامه اعتراضات مردمی در آلبانی علیه «جارد کوشنر» داماد ترامپ که در حال ساخت استراحتگاه مجلل در خاک این کشور اروپایی است، مردم دست به تظاهرات زدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656733" target="_blank">📅 07:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2O6KgwMSGavpArWcb_RuoKgtgVhdjjrmBHeFguEY4bdwwwHGYIfbcOWIjfsEnu8fEGwRwv5f7lAVGJfpKvax4Sjzw2hNpgUR6ijNyrPccHNWLwottAqmxoUipHffFpD4Yrtzr-1UGdWUbcY5Ft9vVdotlWFtayiBdPgSE0mGh-Wqf8HNBjylF0yhqkIGBzWU3fo67C10pCgHccO4arGaRCym7mc-lK-voJrSQLRFTJN6sj4b04EpBlw2kyyni1b5C7w-T59yPl7W-ssP8OllonupedVzvgGSbgCZ2KHuiZSFke6eKVaL9qm4wqIzpMZaFIXxT8aXtvPhTcgpdQfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز مسیر تیم ملی ایران از سانتیاگو به تیخوانا
🔹
تیم ملی فوتبال ایران پس از توقفی ۲.۵ ساعته در اسپانیا، سفر خود را به مقصد تیخوانای مکزیک از سر گرفت و پس از سفری طولانی وارد محل استقرار خود خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656732" target="_blank">📅 07:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کره شمالی: برنامه هسته‌ای ما مطلقاً غیرقابل مذاکره است
🔹
وزیر خارجه عراق: تداوم جنگ با ایران، عراق را دچار بحران اقتصادی می‌کند.
🔹
مقر فرماندهی ارتش اسرائیل هدف حزب الله قرار گرفت
🔹
نخست وزیر جدید عراق از سفر قریب الوقوع خود به آمریکا خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/656731" target="_blank">📅 07:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای سنتکام درباره پهپادهای مهاجم ایرانی در تنگه هرمز
‌
🔹
سنتکام مدعی شد نیروهای آمریکایی دو پهپاد انتحاری ایرانی را که به گفته این نهاد تردد دریایی در تنگه هرمز را تهدید می‌کردند، سرنگون کرده‌اند.
🔹
ایران تاکنون واکنشی به این ادعا نشان نداده و آن را تأیید نکرده است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656730" target="_blank">📅 07:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
وزیر خارجه عراق: یک فاجعه اقتصادی ممکن است رخ دهد؛ اگر جنگ علیه ایران تا پایان سال ادامه یابد، با مشکل پرداخت حقوق مواجه می‌شویم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656729" target="_blank">📅 07:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca89026fe0.mp4?token=sZg0b-rbvJRVg98oVcBu45o0TbZycUt-9Bv4SnbU_a1qZsmzCAPZWI7wfO9fPiK8TDA8xT0iYaPRXscZU1hXnTGrhPq1-SvlUI61cleYkvreGSpWrJfwCNH_HbexpGBjOjJF9JHY_58ENVoOiI78mG60FdIuLFrjV75QUWb8zhnwf9uQm5rGqLIUA_Gskd6DuUrBKCu4nPsB-tnnMbR0ijYoX0zHGx4ECjrn571wXZtVqVnZNShexFdD_jbpnBZ49jUa_GeIrA7lsv1ggbADlWvVtjldrc2Tx-IuvSvjw1eGBUZyTmIerniAIgUv46XzDG5qo0Ac4V8uBdyvzcSq_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca89026fe0.mp4?token=sZg0b-rbvJRVg98oVcBu45o0TbZycUt-9Bv4SnbU_a1qZsmzCAPZWI7wfO9fPiK8TDA8xT0iYaPRXscZU1hXnTGrhPq1-SvlUI61cleYkvreGSpWrJfwCNH_HbexpGBjOjJF9JHY_58ENVoOiI78mG60FdIuLFrjV75QUWb8zhnwf9uQm5rGqLIUA_Gskd6DuUrBKCu4nPsB-tnnMbR0ijYoX0zHGx4ECjrn571wXZtVqVnZNShexFdD_jbpnBZ49jUa_GeIrA7lsv1ggbADlWvVtjldrc2Tx-IuvSvjw1eGBUZyTmIerniAIgUv46XzDG5qo0Ac4V8uBdyvzcSq_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در یکی از بنادر اکوادور
🔹
به دلیل آتش‌سوزی گسترده در یکی از بنادر اکوادور، چند قایق و شناور روی آب دچار حریق شده‌ و ستون‌های عظیم دود سیاه آسمان منطقه را پوشانده است. هنوز جزئیاتی درباره علت انفجارها یا تلفات احتمالی منتشر نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/656728" target="_blank">📅 07:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت سی‌ام - پادکست کافئین</div>
  <div class="tg-doc-extra">کوروش کبیر</div>
</div>
<a href="https://t.me/akhbarefori/656727" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
کوروش بزرگ (پایانِ فصل اول)
🔹
مدیرِ سازمان شما از کدام مکتب فکری استفاده می‌کند؟ «مکتب آشوری» که بر پایه رعب، وحشت و یکسان‌سازی است، یا «دکترین کوروش» که بر پایه اتحاد در عینِ تفاوت‌هاست؟ در قسمت آخر از فصل اول، بزرگترین کلاس درسِ تاریخ را برای مدیریتِ منابع انسانی، ادغام رقبا و جنگ روانی مرور کرده‌ایم. برنده‌ها نیازی به شمشیر ندارند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/656727" target="_blank">📅 07:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6e5ccfc4.mp4?token=Z1Dym0g2fDum1-ynj5h-UNcysG6cgAuTg3yAHTWD96OtoBys6c3z8NidOvAcqWOozuPLpCOE1wGm_ZcCgNZILomheSeelvvwGDDjUGN9e6LD---Ce7c12tZSMLSVGBLCj3p9uAu5a63fVybak0NaptVuXSVoD4b437J6m7RdEbHQQjxrL8BpicNbO3uYMdigvN2Fr_axCAh7XUOufh_GlvxJ3K9skxASF7pPKPBVli3-ieuLLS7eX0NhWbrRvr3oPhN_Or6f7yaWVHNdZp0uqYQAVb3o_dACeiE1I5-1G2X-pVXEkDV-xQNiTM4ja2KMw4DR8EzUX5I69_XKU8Ek6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6e5ccfc4.mp4?token=Z1Dym0g2fDum1-ynj5h-UNcysG6cgAuTg3yAHTWD96OtoBys6c3z8NidOvAcqWOozuPLpCOE1wGm_ZcCgNZILomheSeelvvwGDDjUGN9e6LD---Ce7c12tZSMLSVGBLCj3p9uAu5a63fVybak0NaptVuXSVoD4b437J6m7RdEbHQQjxrL8BpicNbO3uYMdigvN2Fr_axCAh7XUOufh_GlvxJ3K9skxASF7pPKPBVli3-ieuLLS7eX0NhWbrRvr3oPhN_Or6f7yaWVHNdZp0uqYQAVb3o_dACeiE1I5-1G2X-pVXEkDV-xQNiTM4ja2KMw4DR8EzUX5I69_XKU8Ek6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوروش بزرگ؛ استراتژیِ «فتحِ بدون شمشیر» (قسمت پایانی فصل اول)
#پادکست_کافئین
| قسمت سی‌ام
☕️
🔹
در ایستگاه پایانی فصل اول، افسانه‌های کلیشه‌ای را کنار گذاشتیم و به سراغ نبوغِ کوروش در «توسعه سازمانی» و «قدرت نرم» رفتیم. پادشاهی که به جای شکستن استخوان‌های دشمنان، مغزها و قلب‌هایشان را هک کرد و به تاریخ نشان داد: «برای اینکه رهبرِ همه باشی، نباید همه را شبیهِ خودت کنی!»
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/uot54a9
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/656726" target="_blank">📅 07:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idMf4L4lu4BbSo526NNYZm01XvA0UOx2pk9hb1EUtCaRJM_e5Fwht8SkuwkKgumL0Nq_yCfEn9b_CnJ3VkE_5BsOMDMrd5znP4KrUB-6-z74dPwg0_kWi0IgHfXRHVCBPxmnlWcEzXreZXRWhLypVcktjfnrPyAb896e9O7S_GaI2yAlQIbn-H2BgtNU8NZfQOy-WgDizkOgSXhitpvNt4yrjzPHkQzUFIa-Q5FHaH5vwynreNUQqfawIfWRsHyXYZd9FNj2W69ILUUl6vfCA1u0Dte_80h2voqNR8veg1UD6Wx2Tj-5fVOLydpH4aHgnFIgcQ4QxVBzmMTHLeWuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۷ خرداد ماه
۲۱ ذی‌الحجه ۱۴۴۷
۷ ژوئن ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/656725" target="_blank">📅 07:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from-Salar-via@chToolsBot</strong></div>
<div class="tg-text">تست هوش زبانی امشب
🎯
🚀
معنی اصطلاح Hail Mary به نظرتون چی میشه؟
🧑‍🚀
روی جواب درست کلیک کنید
👇
👇</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/656724" target="_blank">📅 00:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwnsQJFcMeEBE5LAm-_FsqKRSzXR7wz8ipZ5x-31ag9Jv9J5SZVxXEqxaipJanL6cDsAMCJwD0vc4W81wkZn1C6_WlkPC9yGfS3FugtW2JkYkxetT93HxXZ7K346Ecczt1FX7UAOdgYnajcdbvO1uF0HjdDUtuQnYMfvKkT95SxEu9HWQ9HhW-_VKniqUlqa2wO45g7-ScdwRyxUVjKllueiVtfxMEXEdFEQGnuRee0BG4Gj0Db1XiyuRgOltejEVePmo7UR6VkWRl3vba987ouQmo7bvsfAPMaJZIvLNBZGc1hy5iTbKyxzvaMaMYKlo1qNJ2VC82kcNla37YXMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/656722" target="_blank">📅 00:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1Fj-ZujftFSzudirOcazjtAfkEF-eUy6lupRnHhqqKFyG4rWKng6inZeYblrvBO13vTEsV18z8MXv4E0M-b_qrGTSblxu_KydlSNcHCquhk3oHB29Qt_9_o07fNMt_wO9KS1fyqNzhXcCrEw3zRFk0k8VM1TuWuz7Qz77sFqxojMw5N1uqyxVaemRtWkVg412-LbzZP5a7j8KhpDOcVRJszWRynRDmBhp4aTY5R0ugjhe7fKICyx7kY1oAMJ3Y6W-9WXUiNyFpTvREPaXVonwfwZ1zHK1lq8geHHGPDXV7--0MQvqLI52GNHebh7BbAswWIpms8dSLdG32oXWUgPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انقلاب در انرژی پاک؛ برگ مصنوعی CO₂ را به سوخت مایع تبدیل کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/656721" target="_blank">📅 23:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر تکان‌دهنده معاون رئیس‌جمهور؛ آلودگی هوا جان ۵۹ هزار نفر را گرفت
شینا انصاری، معاون رییس‌جمهور و رییس سازمان حفاظت محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
مطابق با آخرین گزارش‌های وزارت بهداشت و مراجع ذی‌صلاح در سال ۱۴۰۳،  بررسی‌های اپیدمیولوژیک روی ذرات معلق کمتر از ۲.۵ میکرون (PM2.5) نشان‌دهنده ابعاد نگران‌کننده این پدیده (آلودگی هوا) بر سلامت عمومی است.
🔹
تلفات کل کشور در سال ۱۴۰۳، تعداد کل موارد مرگ ناشی از تمامی علل منتسب به ذرات معلق PM2.5 در افراد بالای ۳۰ سال، ۵۸,۹۷۵ نفر برآورد شده است. تلفات تهران از این میان، ۸,۸۵۵ مورد از مرگ‌ومیرها مستقیماً به آلودگی هوای پایتخت اختصاص دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/656720" target="_blank">📅 23:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656712">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1hpJFczElYXqz5HNhDlDz_X7v9KHZr0doa4wfdIBlfucmA9JtX_K6R8716z7RQwLREqg-gAfR-mQttNrXXx46kpiyIENHN-2BL4YMqRsLDFD4JeTaqhve7CA2tQrso1hJ0aZOH2x0Kb5O8bY4VqQOYqvkMBIpE2JDcqSHSfZZzFeY8tl6WTeJOs8v55EEoesLeTfnDBU3Bk3v811r56aNMc7pRPKNt2LmvpXjx3FEAZeWNCSCj5kZ-FXcvwdstGPqqH8MN3CLViuq7bbXS8Lje-Vw0Iw7xV0IR0sVc4pMPQATUOxm_0L0VJKWJ3_SK7X7ojc0aj3GTFEObxAr1_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOO0txudDsGVaKleDsFYwlElhNSO3btjJdNnSrwSMlhci0lZaBtuHqO9nQ1M0aCF7EvkmgCEDUYEs9paLcHTHU5G-mBIUTs_mb7E13O5G6iVr_6kAXb30AmJQ51FqDNCg7rmOecPeYNH5JcJ_HQchdyIJeu8oUBZ0m_wDsaitIXVNQhsaUKIFvhadoqKfIPAG-lE2OfIwyHJZmXB_Z8WoB9YxTaaLvqHE2ZL9na9eShaHParPHbdxU2zwSwuuCqZzSBPrgY71Gt47aV6lqEevBdrfukF_Lr4IwT6lbL3W4k1IMPHeuTorYciwyqSFHQ0_hTI2bW2uSQudX9y_qu4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIRrSV686i8SgqtJhwZxCRoVTYQUd5JTZRaYl1vEtXlOb4GV2JsuzNYk0FBC7aZAgBYzBTNb_Y011RsfMXj8o3zRfJ9wpvIcpUoUuK8y1XSLsmh4gchsTxJ1S69E0sLJ_0Tai3z62ocsi2Ph3SaS0BBmSmBb3yIv0OhEt9p_CNMTBvcTyMut_ZuvOhoPaxjmB3Vt95UzOeM1SPh_qskNwAOuIcbuo_woASfe6r1Z9e1MMeKdcKAf-bbtJ4OFBq5ZKtpvhqDaFi8SRcV4JuIfjID8txLp0zSCKyl_FskdczqGTQvCKVteFi3t7v_7bEihfmRPpeg-6gTs7EXb_SSHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofTUaRNmTp_fAMqidVH-8od2gK2PrQNVTKjnM_-mmHjy0o5FIhXm39bL4_6Nf8f3ddhLnwfNJrFYySxpQHm0S1trwGzTdhLL4KnD25SeVKqzvFij2ALyiO7HMSYhYlaOrJ6dCbFojvHwQlnQOhP8tlkl_s3-9Z9mJ4bv28-wSn2EIzPv2wALAfSuGv9_rBlPv_0AwSopMFrArtibBOOjdMvKZQui-5FXgKxDYZv9WHtQnTF6HeTs3koMoZ6dX_r_iETFFEwW2tKn9MbWOXZyvHg0tW09nuyveER_AUpB6EKe0xZIrzdVvOkYTItAaAdBts9xOnjvAFMbdCNdOpDWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feuom3g_sHIYf7KMhC9hSC1S8JvTX-epb-BT2cW9M25YjzKTuh3MF5Mo-b2rme5fTrTx_2w_01ORYYi2mpl7vyW03zVVyGnVZb6Is5VfZYYw9u5GtrOcIdbbcBWb7q5OT_vQ9DqyubeHvEM9JhVEm3JSErxJUPN_CQ9NFIehLxWcr4WI5_n4I1GTFiKv4oQqmi3i4UGEgI9UU_oGZVgdAbXWGytKBQ9rXTRxvDjLZ3q6QY7kdwgtVfQAACShsQ0CyfwssdMAOvprMPKeNbDGoiLpSFFHB6Wy6t5Sa9xCIv98gFSMoBrxiZrxlV4PR4j62xjltjsRmamLJUszy4bPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6Rzeij8eYPyW-Nl2WXVhXJ5LbyVW0iOIjZppDP5YYcK07JuB594GyvzvnRqso_zfhNxB7ofXHtH7whQkkSAYdUvbODu0S5Sqr1gt63v77te5X1Xsy6dnZAwnF9pbWLml83lpj4uCttJE2mxWKQXyUD4VfVN7RT6whYEDNxi7tUPE4RTlvsd34LE7ObzLLbO6pSgDaglkeSjjnyUFJSObOSYl0Nk4Gq8yuINQSAHfSa48T3qQhcTnIni8oAmrUwS_u5KD8VO4XyVSS7gt3zQFrUNdff3gulvK91yPraJWcjQDmCGBwTns6rVQWl4WFILIz3seBPFPxgVR-WvpAbcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVc0zaEa36lhPHmWBLKz1k2ZLyofy97b-4APXnQBdn-uCaia4FbJbuPTdSVtMt0xweqT-JuovjKNLXUHXm-H1HZy1480XW01eFfDgkmTlVhboOOJHEQHSXINUi_9N8FpcLXavv_MkannJo9M30CaIBCIE2g6isskpqH00diq0TZrnE0vXK08636g3lSrY_0UOu4XQRdM5fFvWfkgFpUMhl-uXVC6x6OBAlS4GP0fe18TCUaCMqqVKEcjQ0BQlsaVXjBFV8pqyjsgODl4gZgfoo4maXJCVnYePAeIIA6yok6qX5xoL6isplpYtGrc0I8ssVqwKlvg8s0unPATvwWXWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
به یاد ۱۶۸ دانش‌آموز شهید میناب، یادواره شهدای میناب در هامبورگ
🔹
برای دنبال کردن اخبار و گزارش‌های بیشتر، کلیک کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/656712" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656706">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EysLYX0cKCpoCjjS6xK6fQ4YOvUHuFNrV1Tc5XC7ReWWkBPUpewk5aP7T1KQ5aSeL3ANByuobkMYqWzxa17ZZS65R2zO52Gv1kP8Yilc-CTaIuUDjcNgy828ZFaQQZ58t_E-IioIeEaIwXBsOdr_gzhtS_ZkxHdOORPpRqqhAA0UTdYqeHUGyK7W7ma2sY50CFlFYYe-GMf0S4UqfAaX_ty2vnDdgXzTzyPoxASymn-YDXRMOwBaIlSJtUeokVa6l4waEBAmGiZTvOZp_mrPZZMCTfs9oW3cHZo78BeaKCoYppfWiX-naBROHLceXP_vf50Gil130dnzCjmxnxyo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLZtsLt1p6dv9oxtdQphUoLEY_zQxhOZmXgASlSY2uJzRFhslV-8hs_j3LQNehKNoUC7feeAHL59ZXbjIefGrP7-p3SKwK8AMWNOWDkJk6va8rLnMtSNVrxeGVJ2cKWXXZbrIK0r1gbkzBIrqUA-iHhf7zUJZyMky-Jm6Lui1BQLazVjNB-5EL1bCUmtYlJ3XaTx_BYeM2T17no1hZUxD--NC8yg-xsaAMOhrVWZP7pXYRnj3G5dwzTX8YQZ8luJz83MRbJ5X_F3hg0SPCjugyYf5tZHFPakpNij8Wrg2NkIboi74klHQOfYY5EfDSWvKXAqxPjp45ia1lbJ8iLjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkH4aCqHXPH7X9zib98LsHWT5L3araotlSRe8D3ddIg4lnhSdyTfPiADJFCF7dhcB6dKDhjicFRti49uLYlUdGmGyZZOXoDpzeO9T4u5rlJyxduWCJbQ-RQCJugFZbViPCONtWXwpAJCeWagHxwV2WQ8CBGucggZVecaPqxltEs1O7J0EbpceVWsnLMvEOCyDZbg3CpRpJOF56LsmbPbyYlOJI5Bsfo5Nt5jspY5_0_4HZkXmwGhBSgZlAh3zeYviXuZQV8PS1b3jhKaooj9TPzsltElw-E5_KuJI2XImRjnKFgK7ulL0aimi7OMc-SAQWZVev6qhmNT1wR_fs4rDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvy7skO7RwkfewHPlT8fIxIhAedPmT4JcXKQxihpIueARKUOr5ke6ISAqVTXkVZq8FlG-z22US7laB0TLIFmSyCfKOcKnfDLJH30C_BxVjPw_IhBehI72NNvxqedyrfpD4lDQQAStNU-meKWHQMel_RXUB68v-vb2kgHFG8Q6V5drOc92sNzs05szaau7ebJHHbvx5xC8JGs4tPvW_K7SgqBct9ETQy3r3q58fyHXSDeEOaoMJu_kJWjV-0aQclsTXnjyvQn-T_YYMtx4nhwQNDWYWFn12Sb3LACpKP20rkzya8XLWo9b5XlBugh-1IeSJzgoP_sz3iDojlZeFumZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDhFfsCHtVYKIWbuZhz2YNb_95VxipGQhTaeuS9bFTFx4M-nNj0Cd4QkwOHSiNEJFYD7HDzf5XjaY1WE3L0bejd8GPJ2eGs03nGI_tL83IMZYcvhe60K3wYfOn3xIlDp-68gBp5RusAR0hgmMT4pL9-b8IaIWIoYW63rBwkUo34UXoa2zmQKXGElu1EzsHUoLAr08vLIEja8HaDQwk2QALtLSIhedhPReC7QeRdFfYTzIpUFKUyrAXfPRCloFbzjCkRhcrd56Th7syHGtCCeit3VtidCAQ8RHnYtlGh5KcYanST3PnqRxMz2cYKcvA4daHhr0B3dxwFxe-dRuMlNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wr0qddcujTu7P2kktSLxS6YrjRka-h7VTG00bXdvA40fN971W8AA_jtV4XeFR4HgArxbEB22Wj23tysyr66gZxj4rYrg6PyKJtizHWp3mDxtf6l8jroe-UHpqBESQKaYhN9ArcVpfR8GTI9HU066J0x1RstOdjXrPWvVwUdVe9JAoARFI3c8KgY32mq98tMUsFT_zvNWnAXC4jMVHQ49IX_ACSTG1PYrh0FIQFSs5g89jaGOlv6JWly27iE1yLuMQJcndH3GOIfPsOTYggwXYa3_kQgIgfbAwTWfQB59fJLF0DcORGr4ph48YV-n2bZJnvbxpRyXzN2oDGgamvPyGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترسناک‌ترین سلاح‌های قرن/ یکی جلوی هوش مصنوعی را بگیرد!
🔹
وقتی هوش مصنوعی فرمان جنگ را به دست می‌گیرد، الگوریتم‌ها افراد را پیدا می‌کنند، خانه‌ها را ردیابی می‌کنند، اهداف را انتخاب می‌کنند و بدون دخالت انسان حمله می‌کنند.
🔹
۵ نمونه واقعی از هوش مصنوعی‌های جنگی که همین حالا در میدان نبرد استفاده می‌شوند را در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/656706" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656705">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
محمدجواد لاریجانی، کارشناس ارشد مسائل بین‌الملل: پاکستانی‌ها الان میانجی‌گری نمی‌کنند
🔹
نخست‌وزیر پاکستان، آدم خوبی است، اما لازم نیست ما و آمریکایی‌ها را مقابل هم قرار دهد تا مذاکره کنیم، باید میانجی‌گری بلد باشد.
🔹
اگر ما بخواهیم خودمان با آمریکا صحبت می‌کنیم…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656705" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656704">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای منابع خبری: معاون موساد به دلیل شکست پروژه علیه ایران برکنار شد
🔹
باراک راوید، خبرنگار صهیونیست به نقل از منابع مطلع اعلام کرد که رومن گوفمن، رئیس جدید موسادمعاون خود را برکنار کرده است.
🔹
دو منبع آگاه گفتند که معاون رئیس موساد یک سال پیش بودجه‌ای معادل یک میلیارد شِکِل (واحد پول رژیم اسرائیل) دریافت کرد و گروهی شامل صدها نفر برای پروژه سرنگونی نظام ایران را تشکیل داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/656704" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656703">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
ویدئوی منتشر شده از حمله دیشب آمریکا به قشم و سیریک
👇
khabarfoori.com/fa/tiny/news-3220813
🔹
ایران و آمریکا در آستانه جنگ سوم؛ دیشب در تنگه هرمز چه گذشت؟
👇
khabarfoori.com/fa/tiny/news-3220762
🔹
گزارش لحظه به لحظه از مذاکرات ایران و آمریکا؛ نامه مهمی که میانجی برای آیت‌الله خامنه ای فرستاد
👇
khabarfoori.com/fa/tiny/news-3220753
🔹
جنجالی‌ترین پرونده تیم ملی فوتبال قبل از جام جهانی؛ فهرست محرمانه ویزا نگرفته‌های آمریکا لو رفت
👇
khabarfoori.com/fa/tiny/news-3220848
🔹
پشت‌ پرده اولتیماتوم جدید ترامپ درباره پایان مذاکرات | پس از ۶۰ روز جنگ می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3220986
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/656703" target="_blank">📅 23:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656702">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhdJ-r-LUwhbXAiCtFEFnW7y6OSREGibLcVPyF9TUdx2O0_izFbqBV5DAS1s4yJ9z8VTTp3Dc7UhuwIG0qQgVMNaD-8vSmeDLQ3eiBJYNXhhkcllEw0-WEoMzAHJusowUhhON5jBi0NhpYz6tUsxs8YA_n3ghIowSytZ3TArYCApL0PV0KVAi_SG4Jc9-y4-O0FyW9PwdbCS-NIz8FhbvnkHt5ttx1S3EszmREsqxsBU8vdcUAfv1t94X0vEkVER5BToi8tTte04C1-0gOEgAXKwz86cw9Mpq_e1mT7JpLH-9Fq69c-6RYp03ZmKeRBbG7e9Sylw4ZRF1M-f0lev9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فقط ۱۶ درصد آمریکایی‌ها فکر می‌کنند در جنگ با ایران پیروز شده‌اند
الجزیره:
🔹
۱۰۰ روز پس از جنگ علیه ایران، ترامپ در جلب حمایت آمریکا شکست خورد. یک نظرسنجی دانشگاه مریلند در مورد مسائل بحرانی روز پنجشنبه نشان داد که تنها ۱۶ درصد از رأی‌دهندگان آمریکایی فکر می‌کنند که آمریکا در جنگ پیروز شده یا در حال پیروزی است. عدم محبوبیت این جنگ ممکن است به جمهوری‌خواهان در انتخابات آسیب برساند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/656702" target="_blank">📅 23:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656701">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
دارایی واقعی فیروزه چیست؟‌
🔹
خرید نماد
#وفیروزه
:  چهارشنبه، ۲۰ خرداد ماه
رامین ربیعی، مدیرعامل گروه مالی فیروزه (سهامی عام)، در آیین معارفه‌ی عرضه‌ی اولیه‌ی سهام این گروه، خطاب به سهامداران و سرمایه‌گذاران گفت: «دارایی واقعی فیروزه، تیمی ۵۰۰ نفره است؛ تیمی که هم از نظر حرفه‌ای، هم از نظر اخلاقی و هم از نظر تلاش و دانش، در سطح بالایی قرار دارد.
ما کارخانه نیستیم. برای رشد، به ماشین‌آلات نیاز نداریم؛ به انسان‌های درجه‌یک نیاز داریم تا فیروزه و ایران عزیز را بسازند.
شما با سهامدار شدن، در دانش و توان این افراد شریک می‌شوید.»
🎁
خرید نماد
#وفیروزه
با
آمادگی ۱۵۰٪ در کارگزاری فیروزه
💎
گروه مالی فیروزه
سرمایه‌گذاری، برای همه مردم ایران
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/656701" target="_blank">📅 23:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656700">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961752bfc3.mp4?token=fWymlzcHwRg-is46LirlrHJVupdXOfMZH5D63d4I2UdUbttwC-EJVVHgU-OsjUXjt_ceDETge1b2gCHbVQjYa0k5lozGYG9HosBAnV62Ybp3nIFBPWPN2Aejq0tiINPrVt3G7YAokIoSB7KxXn-rthtvlV9ORQE0LNg587g82xs88RjChSFysdZV8yIt-FkvQdehDRA3MoaBfdKJZx1KQbDZ9QX0VkZc2wiLr84hzhrRKCTqo52IWYpVPUio9Dwu0DHwMUiBnvweb-2IB3Up5KVfydWyl-6IPGlBhUmiTicnF9GzRhG05NYTnZQUrIOuoTeTgEkH1AY4c7n0cB660w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961752bfc3.mp4?token=fWymlzcHwRg-is46LirlrHJVupdXOfMZH5D63d4I2UdUbttwC-EJVVHgU-OsjUXjt_ceDETge1b2gCHbVQjYa0k5lozGYG9HosBAnV62Ybp3nIFBPWPN2Aejq0tiINPrVt3G7YAokIoSB7KxXn-rthtvlV9ORQE0LNg587g82xs88RjChSFysdZV8yIt-FkvQdehDRA3MoaBfdKJZx1KQbDZ9QX0VkZc2wiLr84hzhrRKCTqo52IWYpVPUio9Dwu0DHwMUiBnvweb-2IB3Up5KVfydWyl-6IPGlBhUmiTicnF9GzRhG05NYTnZQUrIOuoTeTgEkH1AY4c7n0cB660w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش شدید امشب شهر سیرکان جنوب سراوان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656700" target="_blank">📅 23:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_q8YLYI-aj2WKvzxhsnb02KBbULs-6qFvdKfMir0yhyki1NIM5T25EpLzZb6ocrHEDpPWMOANllQgMogDRtn-9I-IHJNRx9w605YlO61csE2LzS8DmR5_0VdwRfvv33n76EMA46W9tics0y55qZOxhmY3I9lPP36fvSols6RpCIRgk7_M0bIYdWhHvoL3nVKEry9ZSXOvwnibGwUYDYAzJWfduTwYzbymh16gCncMrXedvxs7eFrQhlQ9uwTQ2SWRChvXA5cNxmTIYydTEv31k9EZKil34gSdmNHNzAVXghpV_iTkNCJjdC7wy-0jWha51S1BREbcKnrvGienOfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آزادی قسمت همه
🔹
با رونمایی از نخستین پلاک اختصاصی خودرو در منطقه آزاد سرخس، گامی مهم برای شکستن انحصار خودرو برداشته شد. بر اساس طرح جدید، امکان استفاده از خودروهای خارجی در این منطقه با عوارض صفر فراهم شده و تردد آنها در استان با مجوز شورای تامین امکانپذیر است. در شرایطی که بازار خودرو در دست دو تولیدکننده محدود است، اجرای چنین سازوکاری در مناطق آزاد میتواند به رقابتی شدن قیمت‌ها، کاهش انحصار و بهبود شرایط برای مردم منجر شود.
🔹
هفتصدوشصت‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/656699" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656698">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIWV45YlPxeo-dsXozc-tZMxW7JP8oKKLrdhgLQnMY31jZlwBHOmo7YJdDLgJAe4Y1_kvZbmkb7JD0rBhX3GnQI6-_fNjoSnXZbgUp2nq2KOmeM2M-uNFrkKU9H6041qm2upk2bV4Iwm4KSYurlMGiZOix6dEDGqeFKCIdaIltkh6qCgqR9nW2qW5av8z7deUwrbsgiLkJlZeOmbWGGlN8wMEgoIQ9S4utiJ0No57nHMX-GaliO0RUsA9tCkfTlB6P0BvIIJLeLVXPOG67RSwyAH5AoewU2VGIc1X5j7lNjRsyejT8nxkEHiHW6mxgie1zfIQqICHNhcAoU4R86cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عاقبت بسته ماندن تنگه هرمز؛ شاید غذا هم گران شود!
🔹
هرگونه تنش یا اختلال در تنگه هرمز می‌تواند قیمت نفت را جهش دهد و در ادامه، از مسیر افزایش هزینه تولید، حمل‌ونقل و کودهای شیمیایی، فشار را به بازار جهانی غذا منتقل کند.
🔹
بررسی روندهای جهانی نشان می‌دهد هرگاه بازار نفت دچار شوک شود، با یک فاصله زمانی کوتاه، شاخص قیمت جهانی مواد غذایی نیز صعودی می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/656698" target="_blank">📅 23:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
فرمانده صهیونیست: جنوب لبنان باید اشغال شود
🔹
فرمانده جبهه شمالی ارتش رژیم صهیونیستی خط بطلانی بر مذاکرات لبنان و رژیم صهیونیستی کشید و خواستار اشغال جنوب این کشور شد.
‌
🔹
او گفته که خلع سلاح حزب‌الله بدون کنترل و اشغال جنوب لبنان امکان‌پذیر نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/656697" target="_blank">📅 23:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDl4u4jGul-yoEYHXv-CBWdJN4Nc3CZ0glg3-MakD7huiYT1DcubW6jeFvRtr3FXxLZlL2iMvm1ZKwRHzBe9pYwmh3oA3ZRUyVWBqUIfPigpEJ_EnfbBc4rVY3-DdNZY7htE7zVWQNezXntNsr63NSdMLWKdATg_cnpzLUkDCcmBkeJzl3AO_cQz2KO0H9uGHNIfPSTKL6PfmRigIdblLydnjAEFoWTqLSS70JTVDZAtuqVoBHvrIip_sN4YHGjxd2NVV5M1rmRlVXvwftKllrKO5LNuapUvtEnbHmrAVs8UgIMquk9GpoaI3aAQUiScIn7FQ4SKpI-dsUNANP_fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیکزاد: بیش از پیش آماده جنگ هستیم/ دست بر ماشه به هر اقدامی که لازم باشد، پاسخ می‌دهیم
علی نیکزاد، نایب رئیس مجلس در
#گفتگو
با خبرفوری:
🔹
آمادگی کشور برای پاسخ به هر اقدامی در بالاترین سطح قرار دارد؛ ما دست بر ماشه آماده پاسخ هستیم و این یک ادعای صرف نیست. استراتژی ما با رویکرد آفندی و پدافندی تدوین شده تا دشمن از صبر ما سوءبرداشت نکند.
🔹
درباره احتمال حمله پیش‌دستانه نیز باید گفت زمان و نحوه واکنش، تنها در ساعت صفر و ثانیه طلایی تعیین می‌شود و هرگونه پیش‌بینی پیش از آن خطاست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/656696" target="_blank">📅 23:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
لاریجانی، کارشناس ارشد مسائل سیاسی: مردم خیالشان جمع باشد که ایران برنامه هسته‌ای خودش را به هیچ وجه از دست نمی‌دهد
🔹
برای گرفتن پول خودمان از آمریکا التماس نخواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/656695" target="_blank">📅 22:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
لاریجانی، کارشناس ارشد مسائل سیاسی: مردم خیالشان جمع باشد که ایران برنامه هسته‌ای خودش را به هیچ وجه از دست نمی‌دهد
🔹
برای گرفتن پول خودمان از آمریکا التماس نخواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/656694" target="_blank">📅 22:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDcmj4DoVzM79vasmkRq5XjUeJuPviD5DV6TQXe-UScPHbps7bynehP1Gl-wQ8RdVHzgJM5shBF4gNzw1hXsAlp3EY9cMfoly9auA9wgPrMJTOQpO40bj--U6X76Xykahh28J3btEF8FwhvEd210e1Mf0c8x-XsD8nOrJ8CpSVjWtJerp8zTZ8ZqG9e4l1-0VVw5nm3uzZwPYtm6NZM0pz_P3JyWs37djNBEkrVdlSVgCLtreVkfYKMuXt8pHeN9uUYatkNR0N8aA9qbAFcNMFM6EL4K6cYx9XmcXQnBB8ViN56u18qe5Lj_5t9NIffrZLmtdiGEW0wa3OCN7yeWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رفتار جالب ایرانی‌ها در بازار طلا در زمان جنگ
🔹
طبق گزارش منتشر شده از پلتفرم میلی ۸۲ درصد دارایی خود را حفظ کردند. این یعنی رفتار غالب کاربران، فروش هیجانی نبوده و به دنبال حفظ سرمایه طلای خود بودند
🔹
حجم خرید و فروش تقریباً متعادل بوده؛ ۶۹۵ کیلوگرم خرید در مقابل ۶۵۱ کیلوگرم فروش. خبری از خرید و فروش هیجانی نبوده
🔹
طبق گزارش بزرگترین پلتفرم فروش طلای آنلاین؛ بیشترین تمایل به خرید در ۱۹ اسفند ثبت شده؛ روزی که حجم خرید ۲.۷ برابر فروش بوده است. به بیان دیگر، بخشی از کاربران اوج بحران را فرصت خرید دیده‌اند.
🔹
در این بازه قیمت طلا از ۲۰ میلیون و ۳۱۶ هزار تومان به ۱۶ میلیون و ۷۴۴ هزار تومان رسید؛ نوسانی بیش از ۱۷ درصد در کمتر از سه هفته.
🔹
در حالی که ۱۳۴۶ کیلوگرم طلا در بستر میلی معامله شد، تنها حدود ۹ کیلوگرم طلای فیزیکی تحویل کاربران شد؛ الباقی کاربران ترجیح دادند طلای خود را در پلتفرم‌ها نگه دارند.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/656693" target="_blank">📅 22:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سفیر چین در تهران: جنگ آمریکا و اسرائیل علیه ایران هرگز نباید رخ می‌داد
‌
🔹
هیچ ضرورتی برای ادامه این جنگ وجود ندارد.
🔹
همکاری‌های تجاری عادی ایران و چین تحت تاثیر موضوعات خارجی نیست.
🔹
به هر طرفی که «چین واحد» را به چالش بکشد، محکم واکنش نشان می‌دهیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/656692" target="_blank">📅 22:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e31b59b5.mp4?token=WHfF3A_Xq6xZVFGfEJLihCRws2g8KWbqyTHXczFxW8Zho6eTTsZVd6B8yuUY5jDBS86eJBi6n_-hSJSCr0rd5KwdN5hORATpBstJJxOuFGOhCMFpNyycygBMO4cIzyK-ykR07FaLUDBsOSiaiBPRhS7ILH3uugfK-QjUdij6qvByLFEtSw4Ajy4fm0MaPoHo9tM-nGlM-kDW-kUalpprHZi-zgi6iEIrSXRTFPMhaYAKPY6iIE0Jcr5AnP7jbuXjAQMNGZEuWTBiz-aFBY-6MloUPeAUVg96dbcEqiES4-EsslvGmBUqf6p7AC26Mk0j_mK6AsXq7rD3MHm3gq3RJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e31b59b5.mp4?token=WHfF3A_Xq6xZVFGfEJLihCRws2g8KWbqyTHXczFxW8Zho6eTTsZVd6B8yuUY5jDBS86eJBi6n_-hSJSCr0rd5KwdN5hORATpBstJJxOuFGOhCMFpNyycygBMO4cIzyK-ykR07FaLUDBsOSiaiBPRhS7ILH3uugfK-QjUdij6qvByLFEtSw4Ajy4fm0MaPoHo9tM-nGlM-kDW-kUalpprHZi-zgi6iEIrSXRTFPMhaYAKPY6iIE0Jcr5AnP7jbuXjAQMNGZEuWTBiz-aFBY-6MloUPeAUVg96dbcEqiES4-EsslvGmBUqf6p7AC26Mk0j_mK6AsXq7rD3MHm3gq3RJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری فیزیکی در بازی دوستانه پرتغال و شیلی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/656691" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاسب بخار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slS-8q9JH0qQCVCGH39-WempiB4mZdrz8N2UnAXrLjaOrgwgNaz6Z4tDyhrFI-IENdur4TB4pMMHoTrKZUFr1zRJNJasg10w0RlKAPILm_4i8eOxxp5HTYpYJSh3kpxjy-uC2y_wfQ7IfGqw2lM4Ejga1SnmQH4hiXO16l0jbUol0d3ActIix4IYmcSj5TVriCvukkbOJWTX7v6DdMQB6n6DThIQ4D67N1bSmCJr1xRp4mS-b2hHZji-A6GX_9k6-z2XDakoegpQSIb3ut7nvzbu3097-nwkkCOtYsxGu0Fal18Jt7-kL-hSUbnprYdOMpozllz-FtsZg3TVSTzDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رمزگشایی از خودروهای ناقص سایپا ؛ تولید هیچ به جای خودرو
🔸
بازدید رئیس سازمان بازرسی از پارکینگ‌های سایپا فاش کرد که برخلاف ادعاهای مدیریتی، نقص خودروها محدود به چند قطعه خاص نیست. لیست‌های طولانیِ کسری بر روی شیشه‌ها، نشان‌دهنده فروپاشی زنجیره تأمین و بحران عمیق مالی است؛ فاجعه‌ای که فراتر از نقص فنی، ناشی از سوءمدیریت ساختاری است که سرمایه ملی را به گروگان گرفته است.
🔸
بازدید اخیر رئیس سازمان بازرسی کل کشور، ذبیح‌الله خدائیان از پارکینگ‌های مملو از خودروهای ناقص شرکت سایپا، فراتر از یک نظارت اداری، پرده از واقعیتی تلخ برداشت که مدیران جاده مخصوص سال‌هاست در پشت واژه‌هایی نظیر تحریم و بدعهدی قطعه‌سازان پنهان کرده‌اند.
🔸
واقعیت این است که بحران خودروهای ناقص در سایپا، دیگر یک مسئله فنی یا قطعاتی نیست؛ بلکه یک بن‌بست مدیریتی و اقتصادی است.
🔸
آنچه در سایپا می‌گذرد، تلاقی نگران‌کننده
فقدان نقدینگی و زوال نظارت است که دود آن مستقیماً به چشم مصرف‌کننده نهایی می‌رود.
🆔
@asbe_bokhar</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656690" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک هشدار پنهان برای صنایع ایران
🔹
شبیه‌سازی‌های پیچیده نشان می‌دهد که احتمال ورود ایران به وضعیت ناترازی شدید برق در سال ۱۴۰۵ به وضعیت نگران‌کننده‌ای رسیده است.
🔹
این ویدئو را تا پایان ببینید تا بفهمید چرا احتمال ناترازی، بزرگ‌ترین هشدار برای صنایع ایران است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/656689" target="_blank">📅 22:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وزیر کشور پاکستان وارد تهران شد ‌
🔹
وی قرار است در این سفر با مقامات ایران از جمله عراقچی، وزیر خارجه دیدار و رایزنی کند/تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/656688" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9CALhGnxGQ1mHLd94ckl7WCWlIGVYLzD3P-MZIlFyiH2xELP8wgOa6vc46ZaiiOjCz3vSrOyiaeWKpQMvcAChkcN6HWLMQVjI5A4cIMBnKJpeAriL3J9HlDYeciOjMAgqk1yGriRBZ1FgUtizklSIUNZ0sgyauHFrYpv_vlGLsW3lDkLepAClQ4eIpo4icR0bDfv4zO8fs1gGhDewAWnMfMdoxATMOZIN_iF5Elhjgb8WSGw_BlzeKm0v3F1ZQdQ84vU7nAvj5kijunM9FyqfbZhY-Tj8FoL-3HSZ4leUThTC5Xb8S4ZajnviNzKreX8wRFJk6GHsQwQizTAk5Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن پالیسی: استراتژی «مرد دیوانه» ترامپ [از سوی ایران] پاتک خورده است
‌
🔹
از آغاز دور دوم ریاست‌جمهوری ترامپ، بسیاری از ناظران تأکید کرده‌اند که او با اقدامات یا تهديدات دیوانه‌وارش احتمالاً از نظریه مرد دیوانه به عنوان ابزاری برای ترساندن دشمنان و تسلیم آنها استفاده می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/656687" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h73AT2gKFzY56OLdV_Bm7jYgDRYBnE0hE7OnfLSbh8kxAyylLi5FCN7TFPp22fPREU5A17NIf_6MuQw8fHtje1jO24QlL5y0nP87ySMGFnlpNX0eVhiSHs0PtzllB56a1PPIFBLb_RPYpahKwZCIzkRQFbFlkacPTOjRgbdikw3HuOYUzZYI1jEHLsXma3PkGi5gtuoFvMJjmgRgFU_FyveNZrZPiEJewkJWtL5F4KKUcH--kNtE4IW9tfW6fInD34hnDloo71GxRa-lq8YafrahPuZK2c5I3-xQjJbSfMI-2-sraAazl408W36hDVoZ7CLBl4HP28WrEjRGI8oUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌ پرده اولتیماتوم جدید ترامپ درباره پایان مذاکرات/ پس از ۶۰ روز جنگ می شود؟
🔹
اگر ترامپ می خواهد بعد از پایان دوره اولتیماتوم، مهلت مذاکره را تمدید کند، پس اصلا چرا اولتیماتوم ۶۰ روزه تعیین کرده است. شاید علت این مساله این باشد که ترامپ می خواهد ژست عجول بودن بگیرد و از طریق تعیین دوره های زمانی محدود و اولتیماتوم های مختلف، جلوی تعلیق و طولانی شدن مذاکرات را بگیرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3220986</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/656686" target="_blank">📅 22:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656685">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
احمد خاتمی: آیت‌الله سید مجتبی خامنه‌ای در جنگ رمضان از ناحیه پا آسیب شدید دید به‌طوری که احتمال قطع پا مطرح بود، اما با تلاش کادر درمان اکنون در سلامت به سر می‌برند/ انتخاب
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3220989</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/656685" target="_blank">📅 22:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDMdcPVbqat0bBbgJB0v9TdUcyy06CoHXug7F02Thj4x7jp3zm2dE55HsmClWfMih9YQf7lrho0SSYusDhwhOtuHhk9UBKUjg2STxmlV113QSqNH-dvg8wk1i8CBh5pJBe2pLx-EWFUc_9ssE-n8TJIlhr7I-Gz5LTRba3uZT8DR9x70dOuEqSsK5RfRrEt19S4rPVtgYLpDuXgaWlAySreBW34wxPjlvzD_L8-Bj6x6o8R-fU2o5tLddI78GyOT5c_3CBr_25Y1Q08VCqpciAPF2_xvmSz3pGX4hQXIRUVdFsWkCg7dS_qbPwRj7zTKLCAHSSiwQt1cmMMzZdTMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
قابل توجه مالباختگان موبایل‌های سرقتی در سراسر ایران
چنانچه شما یا اطرافیانتان جزو مالباختگان گوشی‌های سرقتی هستید،
فقط ظرف ۴۸ ساعت آینده فرصت دارید اطلاعات خود را در
سامانه کشوری همیاب۲۴
ثبت نمایید.
⏳
بیش از ۵۰۰۰ گوشی سرقتی ولی بدون صاحب در همیاب۲۴ شناسایی شده‌اند
؛ شاید یکی از این گوشی‌ها مال شما باشد!
📱
🔍
برای شروع ردیابی، از لینک زیر بدون فیلترشکن اقدام کنید
👇🏻
https://hamyab24.ir/l/aix
https://hamyab24.ir/l/aix</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/656684" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Dphf0eFSKqYLmIMRhyZdiX9GpX_nxkImt6MVt6Nd0lYI7Uc8EplgX0y2y4twE50_59P6eVdnzxFFKhNhWIJwU6UIvo-mkLQvrHaaL_IGOG8sEaMV9Mp0-BTjQ4TOC4DHDAd5C2z_WZ9MqUC1eV63HaxhjhbKmdoBWkAEtqfs3Gs3WVBffaXrh4LYtdy934cg8dq-fndAtJjkYkho_q9csky-ixTuwTWsWgZMa8j4nSN2IEBeemczIRJJPvyMs1ZQ4nklDY_PyDCE-A4djoNrtlJCXLMDScC1mTp4WQaOA1j-B6dL_HUK1XLA2QK9g_Nrw_mtDTSVMJmXiP5ybYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: کتابخانه باراک حسین اوباما، در ۱۰ سال، زمانی که به طور کامل رشد کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/656683" target="_blank">📅 21:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
در شبی که ماه کامل شد؛ روح از بدن جدا شد و به آسمان بیکران رفت
🔹
00:14:30  روح وقتی تعالی پیدا کند توان خلق کردن می یابد
🔹
00:30:30 دل بریدن از دنیا
🔹
00:34:00 احساس سنگینی عالم ماده
🔹
00:43:50 پخش شدن ذرات وجود در عظمتی باور نکردنی
🔹
00:48:10 تمام عشق هستی در یک نگاه خلاصه شد
🔹
00:52:30 درک عمیقی از حقارت و کوچکی‌ام در عالم هستی
🔹
00:57:29 شادی و شعف وصف ناپذیری بعد از تجربه
🔹
قسمت هشتم (مهتاب شبی)، فصل چهارم
🔹
#تجربه‌گر
: فاطمه سجادی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/656682" target="_blank">📅 21:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
صدای انفجار در خارگ مربوط به خنثی سازی مهمات است
‌
🔹
لحظاتی پیش صدای انفجار در جزیره خارگ شنیده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/656681" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
بازداشت عکاس تیم ملی عراق در فرودگاه آمریکا
‌
🔹
«طلال صلاح»، عکاس رسمی تیم ملی عراق که برای پوشش مسابقات این تیم در جام جهانی ۲۰۲۶ به آمریکا سفر کرده بود، از ورود به این کشور منع شده و حدود ۱۲ ساعت است که در بازداشت موقت فرودگاهی به سر می‌برد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/656680" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سناتور آمریکایی: ایران با ۷۰ درصد ذخایر موشکی دست برتر را در مذاکرات دارد
کریس مورفی، سناتور آمریکایی:
🔹
به رئیس‌جمهور آمریکا دو نکته هشدار داده شده که ایران در صورت حمله نظامی، تنگه هرمز را می‌بندد و اقتصاد جهانی را مختل می‌کند.
🔹
هیچ کارزار هوایی قادر به نابودی کامل برنامه هسته‌ای، موشک‌ها و پهپادهای ایران نیست. ایران بر این باور است که قوی‌ترین ضربه ما را تحمل کرده و دوام آورده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/656679" target="_blank">📅 21:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4B8hIICIyb_UNYG42evHCO2fciCqpgfeSYU1jc6OcorHBHmP-9_tGV7YnZWMuzprpoDUsE4cMrcCro_vqZsYXbDTkE9fQlzESTmIEtr-1gwUYeqfM4z7_xywm_DRceqlJimcCh_UmwmBd-jdMXh2rCwXf6Zw1z6uTAhM_5iHlXdWAsGP7ojUJZJ2dRZpfeEd-GH6vJDm5nKYVqY1P6baM71pN4WyITxXS7dpV4PO2lP9UHwh2wkvHXYdwDN_z_il5jdF3dCQV_OfOHx9CmUShvW3P2fWyETJKKCd_gTXLequWAHKXh2JPvI-t5r3ATCm3NG89Ggk1181Ykg0PgXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از وزیر کشور پاکستان در تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/656678" target="_blank">📅 21:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
رئیس سازمان انرژی اتمی: نیروگاه اتمی بوشهر برای سومین سال پیاپی در حوزه بهره‌وری و ایمنی در جمع ۱۰ نیروگاه برتر جهان جای گرفته است
‌
🔹
این نیروگاه تاکنون معادل ۵ برابر هزینه ساخت خود را جبران کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/656677" target="_blank">📅 21:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
قیمت مسکن افت پیدا می‌کند؟
🔹
بر اساس گزارش‌ها، بازار مسکن تهران از آغاز تنش‌های اخیر در منطقه، پیشتاز بازدهی در میان بازارهای دارایی بوده و میانگین قیمت هر متر مربع به حدود ۱۲۰۰ دلار رسیده است.
🔹
مسکن در سال ۱۳۸۷ با تخلیه حباب قیمتی افتی حدود ۲۵ درصد داشت. در سال ۱۳۹۲ هم‌زمان با آغاز مسیر مذاکرات هسته‌ای کاهش ۷ درصدی قیمت داشت.
🔹
کارشناسان معتقدند در صورت تحولات سیاسی مثبت، وقوع کاهش قیمت در این بازار کاملاً نامحتمل نیست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/656676" target="_blank">📅 20:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
عارف: هیچ اختلافی درباره متن و پیشنهادات مذاکره میان مسئولان کشور وجود ندارد
‌
🔹
جمهوری اسلامی ایران یک راهبرد مشخص در مذاکرات داشته و همه مسئولان با هماهنگی کامل آن را دنبال کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/656675" target="_blank">📅 20:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzzzQTFCMql7x-ldRRPYf4mQKU2z-OJNIH-trD3NS4cN2VkQ_KQemiW-HC3XJdq244A2y1_O-sdNAwpEzYNNJ0wZslv1SPz5a_lmJ21CKTiRt9_FspdSdyYRMjHOmN7izhmcGZxCtaz2yBjM8EMTwALYXdQJVO9SUdJbgTVtkSbpa8snYZhFWiWUzfQmKT29X-xOh22Xwbc4csqApsZo0beaie2E58eyuyWOtvRZb5r1QyM5CS6hjnsIp92h4qIGV8uhyQ6UnKe-jXD5ZmThk4nMPRXEfBSlt0ElBcJYIt2a8lYhyEkupIhmRdaAS2VHGOjOPBhADZKo4d53ZZ-nyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هک گروهک تروریستی پژاک توسط حنظله
گروه هکری حنظله:
🔹
در یک عملیات سایبری پیچیده و طولانی‌مدت، کل زیرساخت‌های ارتباطی گروه تروریستی پژاک هک شد و تمام مکاتبات، ایمیل‌ها و اسناد امن اکنون در اختیار ماست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/656674" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEhG0w7AvO4hYsFCS8zdZn9mbohGdLkAag62QfS-uGImV-cIEZL0B7kcLEDzHMWXFYqW_SKHa8ReilS1wnFifD0G8BQY9oWSPTPAj8xdi51AXU7Lv_7SigGAQ5490BDnKZmWlIA9KIO8jubydHL32RgUKk43C_r7_OgccmbjVgUQlyUPPUv7oRhE1UkRZhQmEjjOSxH9ngeXJL1wyPXoyVmK2DLRhJt-P8ccE2PJzf8D4xdcKTEaAAE-23Nfn4rmHgQJWjMS7TRk3ZShpRo5B4kv5acte7hq62yRNe4fZaO6PC05m8wGImzyulWEUTE5egji3JqyPuXkASFsZybB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند قابلیت مخفی تلگرام
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/656673" target="_blank">📅 20:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
هوش مصنوعی برای اولین بار واکسن جهانی کرونا ساخت
‌
🔹
پژوهشگران دانشگاه کمبریج و شرکت دی‌آی‌او‌سین‌وکس موفق شده‌اند نخستین واکسن «جهانی» کرونا را در فاز نخست آزمایش انسانی با موفقیت آزمایش کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/656672" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
وزیر کشور پاکستان وارد تهران شد
‌
🔹
وی قرار است در این سفر با مقامات ایران از جمله عراقچی، وزیر خارجه دیدار و رایزنی کند/تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/656671" target="_blank">📅 20:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So160a0Zzynv5-SqHc8EZGjYWkg794LwNraUgrqT2KaehMA9-bLDsqHs3AvtIQryIc5wPrza6KxDpZ59q0B4ocym5WcTYFIVvhK4arAa2feuzqs19VmWxTrAF-XmnIE_27NR9f0R0hLxCSwhZ0lctc4gd1aQ4qU1c4JZ0JyGj0589oMfjuuAQNA_TIB3pep3bI72zMiq6dc3et3Wd8yGC37CK-XMQEp4c0ikBd_A68B0NMDlpC-lnqPB7QMXskk4aGnalFTtR8IYsi9MsVb19V9cxXf1v19H78XcmWKJzh7AJiJUK0OW3Bj1_7YZqXKlxqUfgCN7uslt9MZPTEgRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی مستقل شد؛ ۸۰٪ کدهای Claude توسط خودش نوشته می‌شود
گاردین:
🔹
آنتروپیک خواستار یک توقف موقت جهانی در توسعه هوش مصنوعی پیشرفته شده و هشدار داده مدل Claude به سمت «بهبود بازگشتی» حرکت می‌کند؛ روندی که می‌تواند خطر از دست رفتن کنترل انسان را افزایش دهد.
🔹
همزمان گزارش شده بیش از ۸۰٪ کدهای جدید شرکت تا مه ۲۰۲۶ توسط Claude نوشته می‌شود و آنتروپیک برای عرضه اولیه سهام با ارزشی احتمالی نزدیک به یک تریلیون دلار اقدام کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/656670" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNNJlHDnou3hUV2ZmjV32XvOmitywWr0ro72D_B02ue4oCsaxS7oeToEMWqe7DVmLvY3W0P7Xsx-usuD6KAMTwnyqKCbqDzYhyG_7fSsepwVvFnLEym2W1DUtvCj2QsiCKmMmFwYBAHudgNW7gE1MM3iWICVLsn7UBX5yH44ktyGtfaSi5c2PNWFaXWztE9ukMbwHYT4SGQBbruEzwggu13-LN_0tOy9CY57BUWNc1VEMh3MYVaDMDmguUkKwRRdbI_Q9eqLfZTZqssjgTjm89MCtdwTFNpyPFG_GLleHMQ3Nbo2nrjchqY-HfVcVj2M-og4t3cb0dHVFPsAc6WH5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5rZ0UPVRz4hPmFE6DpRYJ-Jd8RsmCmaRSc_V6QT4KonIr1GxTjkaIkvKStxPJe5_Dh2Hk-1nzxJ8NYkWQQyIeQ8Hp10y98RSRBwSzuqBUwiOBho4N55eG9GkipYJvA1FL5rK3yXRZiy2aYg4BP4IDUJs5q6mrC7-HXd82ykidVi8B-Ihkb-YtJ8tN0KgfJvgXLjzu0QzScALdYIkRJAeQKNU_5sn7LC-R8H50M8r--s79mcJ2BeagRdCPL6BcXo1iOk4OyZfmxnUQHqa-MHNHfNJw41nXHxGBkD9FoNj9VzpHRMYClcUtmcZi0OK06KXqcOsb3Nby7yU6FGmpHQHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: بی‌کتابی
🖋
نویسنده: محمدرضا شرفی خبوشان
🔹
بی‌کتابی، داستان میرزایعقوب آنتیک‌فروش و دلباخته کتاب‌های خطی را در دوران مظفرالدین شاه قاجار با نثری دلنشین و خاص روایت می‌کند. کتابی عمیق و تامل‌برانگیز که سند جان‌سوزِ تاریخی است با زبانی ادبی.
🔹
اگر دلتان می‌خواهد تاریخ را از میان ناله‌های یک دلال کتاب عاشق بشنوید، کتاب «بی‌کتابی» را ورق بزنید.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/656668" target="_blank">📅 20:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk8Hdbtq487hzHcOc64fqRVf1TYh69sc9-hKbBKmpx80QUlbceJEuz1swqNdonIClEnVeFlErK6sGDSC1izHyc5nL7r6PEZ3_l_LLlPpMHuBNYu8OnmiTkSKnTZJ9cAl0RiZBGug-4mSqVNLPaKYZQITJgucxdOuOwXT03tqTT3Og8t6P4oH92WlE1rOaHoZeL0Qin34AxIy61Gu1R5Su1q976LemMfs2zzZ9BYeN77nsF27kPYFur_q-8cSA49UjCnWDR9YZwCtxTC81Anr9olovRDhVk1iewyV9J87M2M6aS_LN8C-s1DrMW2NonIOE1L-XvEe0UpXgGkhcpTZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی فوتبال ایران برای حضور در جام جهانی ۲۰۲۶ عازم مکزیک شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/656667" target="_blank">📅 19:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMbyu0GddF4uhGRIVPMBbvkhQX1ETWIRe5XVZ4m9eRyD5KgII8QHETBbZZDs_OmR3T7GBrfU1MSyXQrE_qpf307oQhn6gkdVyWvyLmfBKLyWNZlQBw7t5mKJUH2y0utgy-ZlFLhENnXbRbxZPfHJJsr4ntdFB6y4ikOO4vvpfbpPWlMrDXOcDQ9M_Nf3Wwu9_LqtOyiWpe6Cyq0VSg9_Hhbupd2UTY_4FBl59NIwckF4Kgp0QG_oErctuapWfrO1U8Y02y_F1BMNCwK04hbXBQQ1LfkSf0a-8IWNFQ6y7dZpafSs_MO2IberHLz60t9uqyDpzWjTifFfDoPU-afTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/656666" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDzelEFrlFJdWYG2-YTOhgYY4ybrzqKmHFvl9qwkVxz-mqL4PJVVGodvfZhyjBIsoANapIufCgw8um_1PztS-zrE1YjqLiu4VxdwADJ3G5Qt2VcmkrZOYq9Q8p6wqZYFrjDvAJyZESWx4qls2VAXZYMilMYzjn3MPkPNKSfsCq9pylvj5qHjCi3uCzZDXXDTr5_V_DUefnawJMLfbFrOJ0jbt1qUl-3h9DaN214sAKY1N9-99KuPRnVOVLmQ1ROVo4ZWdE956W68hmvkPgv5Vlun1Ox5LarwQENnURm1RSocwmrKElD5LOgYN-gpO1mcP_bnZ8dfVjtkcNm6fpg7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا واقعا عموی دونالد ترامپ یک «ابرقهرمان» بود؟ | جان ترامپ کیست و چه کرد؟
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا، بارها عموی خود جان ترامپ را که در سال ۱۹۸۵ درگذشت، «مردی بزرگ، درخشان و نابغه» و حتی «ابرقهرمان» توصیف کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3220885</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/656665" target="_blank">📅 19:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: گزینه‌های غیرمستقیم ترامپ برای کاهش فشار بر ایران
🔹
ترامپ ممکن است به مسیر‌های غیرمستقیم، مانند برداشتن محدودیت‌های دارایی‌های ایران در قطر، عمان و عراق یا اعطای معافیت‌های تحریمی برای فروش نفت ایران به چین، روی آورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/656664" target="_blank">📅 19:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
معاون تحقیقات و فناوری وزارت بهداشت: قطعی اینترنت در سال گذشته باعث از دست رفتن ۵۶۰۰ مقاله علمی و سقوط یک پله‌ای جایگاه علمی ایران شد
🔹
اگر این مقالات در زمان مقرر منتشر می‌شد، ایران از نظر تعداد مقالات علمی حدود ۳ هزار مقاله از عربستان سعودی جلوتر بود. ما سال گذشته به دلیل قطعی اینترنت، یک رتبه علمی را از دست دادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/656663" target="_blank">📅 19:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656653">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiWhcGZsPp1588XcV_ptoIewZE0MjQWJUYQsBVcT-z1kmnqHQtESGsjTwF85Kbn4r-CWppFpz1I6oVzHiILIsmlyOEW43S3wZPZzrwtIGRYoiMh0OXvNS4S-IkMtzecsVc9J3T_xUOdjx_DaNrxzdWmLuioTzXiLbBEWAHIBH0CeMiBWWPZcwC4xk6ursc_a7XWAyOwVGx-6GVmFnncG2YH8yN3fl5eEiaYLMzO9PhI4qP1-QpfiFdUjqi1bOFj0L58wQxyW9-88LsZvtL8iRbUZVq_cDyHE4V1HGbg5zoX3yDmA1qV8J6NYUKcaV6VyOpbUyQDxde6mFD79YBTZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IikpEHxfeDhn0ma_Z3vAEhm3Snbpe5dCHXxWdPfYTvawVfOaTQ-CXxTQfWQV0NC3UIWYrxAyqxC86w1A5iBnXoTt1jMvUP8-9RfuBnBkBPYNrqYa5T-J5VWWtA95GotSdMzmLnUsAr-4sm5CAr10jXfMX_niFwhz8q1TgNF6eQgkzRwFTrBCm4jB_u1EnTQ5bVrBJ_F6jcsgdZJFlHCfg4N8mHeBOwBnyoW43chd9sVfVeV6AJlIvWSvu6-Mat2B8cMSLIM8oe-SjKdVn72cgUbwr4wkaZ6UEnMZ_auYTRaFnUm0KRyHZie26paBNXH1HcVN6JhOMtZarJimniFhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtTiNvaiKJd8Znoyy7cB8vmxZ2ZnAknEHGYDV1CM5M8ymUj4gd3xO-jhONcqSs5XYsmZ2zTN3dyqBXBWZ5AeXhO9EfCNOT0a-HH99kb6mrFXYundrifd7VhK8OUgh1qZiaaxTWpXUfvpIqc-VURJvDrgUtJWlVJR8ywkuDGk7XtzUQy4GO-loorPKdU_i8nmHbUMCctn0NcFTi3IILhgqkbxGWo_6jRgvo-tdVnAjWII7uRvPZJg7fKZdesCxwSDOUttcleocq6qdcgI8m1sZqROBY4psSC0YDezkQyJKI2010uGmMCPxclqdu6X2BRme1C47IPGQV8eApxkVWkDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klj60bF07BuxsMsEndnkGIoZlUZ-EL927aXS4gNXurTCy4ZS0vU9u-f9Fty1eDb9zjWtD97rO0b7EnuvmeVMp1jO_vkz8QldrQXaT0l52rpiAGKaUDLTmvLlZIgVTBd6BFgUIcOSgqBTLEj8Hc1I9kIwOsjh5qJ1Dp1jSNsOFVIcFhmS6meeIV3aD5mHqehLD5bVKl3EmIeAuaEeMR9ybuwgS6cgbsty_96dnozxTWIHTOGfVE5gu_TLxCzSI7ZDokKBwTApgH089wwiv2OasIZeGR1BmkoD-sT43yuevo7yOQKJ9xqG7_ELXi9OotVCrcvoJZR58_mNFSB7Zm5cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpS6qsE6rgMS9ZmKg-0BvZZMlmXOsAGOXpVBTMEOnpdTCfqoIdaINF6TlbjQG8ruTxUsMc10K95avjZol8nj_CiwSAOpz6YvfWhUrF56okDvxfKZ6Z-FT57sBvRKlLB0cy-BeAcEhF-k4znkt82lB1CbeCjii1qzhHTQG-2OVtFXSt9FsRKGltKqflcXyWWgTMD5xBetMLhubddPbWCY4XaI3fxOaNLO-2H5mlmy-IvHBIYcnbWJkYZk2mvnofwPwfRZUS3G5S9M87egQNldL5Iwv2XFM5mhmAbFIq-3i_pkHFXMuxyJ-tgQ8c_BD318Zew1SZKFE9Spg8BBf6Xjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxy8tMF71O-yoUNeyXCKy1ePtnwdFqHuIeZAYx7wSd1crmRYX_7FaOsw3DEEXChLqXE3RtclEBTouqH6tkmSzi2iLVZW160b0fttGj0vKeZetp7cTWSMwyia34rKVE8wIo_EUf-7QGN3AJNs5Q3eiL4voPQEz0W4O7MUSTPGjBETP6tkVbJiTLV4ozT0D5uUHtgc5cXtNStUBDoNy3z5zSLJhgAq15266E3THAnAOBT9VA9RmAq-9iAPq7oTqZjUsLkJPgCbiLivRu6E1wmzL94WfQS5xRcSi5KA42UxktbfZ4fGKuTu10eUqIsB458qpXrqK86nLyMNs0oU0UL38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVEkxzXukiczjbE6W07mZiANA8Tf7_czbL6qd3k2xgkyY8H1UT_AiHmVhwFFYz2I0EDgnZWNjq9juwsp9BHuby8x4Xj763jawd9mjZmsj2vWctOfzJPtGIC8XrK7BtxkpqwYY7waubmdDzTEcsmd4UHG9GCF17wnvsbNZ3rZD3zQncrtBvRKULMys2YrTHM3AE310AwgTahKK0md6-OXdOiY7RN_y-4MEPLdJnxqKKfdyK6dAAJPKJI6jKPY-qq0N5wM8988zkdbn6ocCEXu06LVQ8GScQBRbLJbnXn0drJcBA_3lFaEH2x76c_qUu5kfWIUinKaPzNunrGo_cfOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPqbbzpWRy2j2Kl7-zQ5-kuB9hJHJdzZbyW1SSpNZpD0IC3nu24-KZr4GPFLcyOGA_FTqNtO5Mj4UA4uhOqOfWVJCz7ryRDxqgVVCdOUh1nuWM1LommvZAEwPoQRw51nw3EzqV7SkQQZnxHKC9qt3nP3KH-8BsqCrns77W9BNb9GoHGzanqQrAvzDnTNsjzlj2at-RlXO_-Xj2xtcbPZ_hGRc34AncgaxNYyHxHq43RBswMHYBkBJHcvUNXeOF0C2FLcbCM9XahfqF1UVMuvX8-iQVVIoVIwjYLtgfN-BCjpSxZrEgUU_1tr9BHkkQv2qPZEc7MflfPtdVmPNjGktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XF62iGE1z5iu2GZ5RIsWCxpPe--1lTH3zG2mbt8BrdCrFKJ6yUcJPOt2_8aZOBFczCfJcUydgEC4UEIoB0eALEl5_XbQPcilKGleWA-BoXVp1nRNqXADbGKwyqyUJ1XD0v980TSAYOT5Rk0MaxS1MnqxllUWBbdv4N9CKxOuJ1LnHCvieXpMNNwp07lw8I8ouebb4BgD-kzdgC3NtKqmnokHhxfOhazxAwcmR-9e_vjLL9Yn11lB5kbt2CU-XyD0XiUctCDulxvJGeundmDPwTHibdla61V7c3xWh73JPt1xGjlNQ_jQ6cdsgvDCj59NmPB1P_p7VLq-Lfoq3lK47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNk75s9XcwW3fHkMQimgEXrI4Nnu6XFZEWhlAq2Hvu-vzeoIEtlJ9NBYhf8X6knZBUnUEz4HiOvYhc5hGFhm0L_As1uosI9nmIYiAw1KXmq818tZfyZLYWv55N5J3APerf3hPU990MFtb10Te6quU1SLPGJaVJknzC9k1i2OwsFNnrBrLBdIPzwRK_uhVOdjtNPM14xfK4-omaGHN0m5z5rUVYxEthfcK3mxJRAhWNqXB-mbZELl_NwoLqMgOEWlneFLyPOafIAJlGuJrxWqY0IcUE1lAXV9vurh408bm3VgcozxTRX1NyTMGU0YZYnk4Gh1Cxf23k5qxUTLDNSuag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مهمونی کیلومتری غدیر در زاهدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/656653" target="_blank">📅 19:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656652">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed997974f.mp4?token=KJ4AQ-PUf-b7K26K-rCkotQI3_qHkBd_tGvg9PF3OFRIItjQ6XveAYiX7X7sJd32CbCdModkntHH2qrRnhmTEg4iStLWTMU9gT1XdkriZ3VIXEDiI5YOWQizZ90jUiPaVlZzG_ap7mg8klf0Y7F0h_E10sjVU3a3qvMkSaL65UzbNJBmcM5j0y6P4ZGh5IjoZ0yYrC1qmee4ymI0V4CvFTixlI8jH8TiHAa5xN5fmqxKBV2-4qR7PLFzwWKKSYTKdYnpI61VgiscFHrlFRpfMe8JDgY7BFVMFwdmI2NeQmUW4MQ-gmmq9LzNQ8XqPR05FyMD1i9dTdhcLVJkiqEDWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed997974f.mp4?token=KJ4AQ-PUf-b7K26K-rCkotQI3_qHkBd_tGvg9PF3OFRIItjQ6XveAYiX7X7sJd32CbCdModkntHH2qrRnhmTEg4iStLWTMU9gT1XdkriZ3VIXEDiI5YOWQizZ90jUiPaVlZzG_ap7mg8klf0Y7F0h_E10sjVU3a3qvMkSaL65UzbNJBmcM5j0y6P4ZGh5IjoZ0yYrC1qmee4ymI0V4CvFTixlI8jH8TiHAa5xN5fmqxKBV2-4qR7PLFzwWKKSYTKdYnpI61VgiscFHrlFRpfMe8JDgY7BFVMFwdmI2NeQmUW4MQ-gmmq9LzNQ8XqPR05FyMD1i9dTdhcLVJkiqEDWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمار حیرت‌انگیز مصرف سرم در ایران
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/656652" target="_blank">📅 19:27 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
