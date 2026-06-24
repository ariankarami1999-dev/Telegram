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
<img src="https://cdn4.telesco.pe/file/UGrTOBhuWzgOww0wXNEREE5BjVRiLPYFKvrvgDLUziz46mHJSGeuuPqkaGPQ_oKyab-gueii-mR-MpVg9nudsQyMrhY2ccggKL1HVOUmt6we3D6ZKsym2BO4B-Oa8FBcTHNLxNM3vU-YX9r77PYHLJ_RUwd3x4Ee8o6rjJISRJay-zYpBjOfUkF8nJrti_78iHuSH3y6zaGf1xy6kfTYRhqrgcayfChYNJlCt2PgooL6PMl2yyxC0Ks-6SL4WZvPe8X1vMii7IB8FdBAbjiuJrXkgTCoN3YyeAfHvqiCwI1Yc-FFi9zgR2Pcvn7Q-uaunI5pVhWoa0xXVAvqxJZu_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-CMETcUc6r3II7t4-ot8tUzi7rgzXrmB5n_IBtuOJi7h_gmadMcLHlPTxgBgb825hnhkGL1gqKBJdSY8m9MSR3bZwNQPbYUXSra5B17mlc3A2DO5_WxmQO6lukzYfK4yxIICB4GIZO3sikuyD1vIuO93_5Ik-kHl3pkOD14jqNyvjEMJIQdH0pw_FEdu7bmOuF5kYoSPaN2iFUp8OvFdaP86bEXN7Xj2gQQppxAhRTxtXJNahBHbQ8Rp0ozC3ClRbLhmNe8eNEKM4kZFjOWBZNPjSVUq1deOGeyWXq4v1t64Ft2ofTCh6ANPNZxTKEbcaIkzEDpbRFbnaw4-e2ktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=uaYyv8daaW-2OgmvzFIGpqMIDH_00-NHrDSTQKY2Fppf17qLRsy2c6LIMRh3XjQF0Owr3fkNGd1_Elg3CECjf03RS2rsyZDzFVOTFT3qW257LyolwldN1CVQLaNGEYLXnArSa4An2Ii6NGSTUXesjGFWqqN_NNO62GIdE6XwmbfKtSXgv5IeRQCYAr85Tbw4-ssA7ECrKufQwY5BUznEcy_vojx8r29O64NEN1uPA_xDRmuw-InNmb0rUDoz2xVlPy0g0bJjGLhVyhlIcXZkFitwZYIxWkN6nDMgstRzrtKaWQibj0rdlq_nyiItX2wC1GZWllU_Vy4y5ais39dN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=uaYyv8daaW-2OgmvzFIGpqMIDH_00-NHrDSTQKY2Fppf17qLRsy2c6LIMRh3XjQF0Owr3fkNGd1_Elg3CECjf03RS2rsyZDzFVOTFT3qW257LyolwldN1CVQLaNGEYLXnArSa4An2Ii6NGSTUXesjGFWqqN_NNO62GIdE6XwmbfKtSXgv5IeRQCYAr85Tbw4-ssA7ECrKufQwY5BUznEcy_vojx8r29O64NEN1uPA_xDRmuw-InNmb0rUDoz2xVlPy0g0bJjGLhVyhlIcXZkFitwZYIxWkN6nDMgstRzrtKaWQibj0rdlq_nyiItX2wC1GZWllU_Vy4y5ais39dN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-cqyRh_cCZkHhGS97QlBz2tGbpbRBqyJ8glo0FWImVX8Q4F91UZL5prrRymYW4VvzT6Kly_dDPfvg3ilax0KEo6xsPly5LNkIULqpLddIyZmFcSGP-lhx0wqjzkoyz81aeCYdjoXF7h7ZFJZ7eWZhRDqN7--QRWx08FuuGQj6QDHPXXziFcsFm2XQ9h3rwLc0dVnAHVjrzJdBHaH6TKtXyf5_f5B6JPw3HQcEy3UzdVgF46q3iN7UrCgkFgsP3uAOPrsB2QQcFITU8j_INMUBtLPMOYFwBa-D3N9NtJIBgjVWragIDIxzKLi_SGp8OAnf__ZD90DO1Da1ZPmq3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r65_cUMVECRh1d_kX9m8b7VQ0FZmDfcKjK5LsxSJDbvxHVp5xnYLKbeowLxfnN1TP8Im_mqoLpJkqLYkiQVBqM3GLdgd4iJJ-NJDgn0ZsSdo2fsakhBlvVnfI862S-zi1kWLoGe-xCe0YhQLYdCoes_jWGYN8dvH3lV3PhVnD2d3-vmdFEVO1Qjg8eGhBmeew8YDn2JCZ2m88iTbZLu2zI87dlLKDFjSdfoB-B00V3poqMiinoXrZ9ej_lJaaMkHyCNpihs3nT_PfmFbiyHpxISRFAdpcxHFXmAdXp0ULkmpgwd_kG1eNBm2gu3ADaJW0KDnI9h3O4PyiZLz8k4Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBZn9xG00ukVt-Zwp-SzpyrLM5t6WksgFugTcqmyzQXHQ9-1r-WjXLXhV3V9fcnRnYjLHY2RT7l4gW3SRTePhzDz9XudcS9L4csiBN3D6taPQvYXpTcYXVHh-f_hyzWunEDkBwIX7ZoQ9ooSFnueERu0Eu9-foE7oZ2_PvNGB43MavM80WV8GoBDqfWNK0ljZSrwF8K1kD0USDwVKH8pSMLnAjN-WNEwj3alHWfbf09-3kqYbfE-JpAu8JsDA_YC_j-Z4F8Fs5eszZkoO8HIuLMnF2tqgCN3R_J93U-YuOUuSCbyKUECz3u5CIN7g10jBP9OUE_ymbTPgnb9ZxaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZeYh9RPtt8JT0oV05Krm6lQKse0sDn_VbsiLgusg5UJq7DLfgfvaO5DDXBQlVhPXjlMKV1zwjh8f9sqoKU28GzsB43QIYDpxpTJ0e0g-KrtHHhGS4692cNY6hU0e4x2iwC2T8MP9Bc8nb4mtxanQfjCtlht9UuMqRv_ynJipik5D4GgMNpaoQP_Ctq3ZFL4DpjdQJXZKYEfWK81xvCSye8Fer2WIZME9s9zGIwVPkT0Y0zjQFfxA5IloeqiV33Wi0Crvmt31e3H3ROTSHrl8HBryESJBwAU6jJfnYAAmNkR0jIQUB4C3TzKXOW-UabBhSWAIMjUBi-s25V_fnufYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K6Zf2KpWDsTScUGf8J1m-heHOOKfO1AScVLqlmZ0qO99qhhHiXAUpbAYIlusTbwhAnVccgpmXxyCzCR3hCF4DHlTFAY9qjewju3Wvtl5qELMXXIyFBVXGbFV05qxU8U53lIyBgii5CzYZzgIR7i11aSs4Bh-mfSKQrQNzhrMtZ802eYlmt1vd_HoSlkRbF-CxXWhgH9kdtqn2kOlefSehGHENf2sqDCfgX21sYRjbdxE5W5M2n8FcdH_laMnz7aZX8NibCE4x8OOruS5zyFVEuX06bO1GBtCRzpT4b918Gy09wWH7VYVVo4pcfKnAUXVnkG7eTdm2s6HDmCTojLAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K6Zf2KpWDsTScUGf8J1m-heHOOKfO1AScVLqlmZ0qO99qhhHiXAUpbAYIlusTbwhAnVccgpmXxyCzCR3hCF4DHlTFAY9qjewju3Wvtl5qELMXXIyFBVXGbFV05qxU8U53lIyBgii5CzYZzgIR7i11aSs4Bh-mfSKQrQNzhrMtZ802eYlmt1vd_HoSlkRbF-CxXWhgH9kdtqn2kOlefSehGHENf2sqDCfgX21sYRjbdxE5W5M2n8FcdH_laMnz7aZX8NibCE4x8OOruS5zyFVEuX06bO1GBtCRzpT4b918Gy09wWH7VYVVo4pcfKnAUXVnkG7eTdm2s6HDmCTojLAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IZyW1Tjmq5ZJQP3eHdCmajmYLVTOGlEvzYdRScYT5GYQaPep67WOuDeaDqQV7OxcGij2haTRCSeYTLFBCvLA9Bwn61cDersfXkLRmBSkwr1aSkDZk2j5a_EZAWiLvNCq7eOxe2BaiXnQKj3oFY-FT7TjukTWeb1iHbUAsPXKdQcW9C7GoOXP2n70xxdhRmNsYN7UI0on7YfQVOVEidP1KmvgsJliRbNgaLj9kZe-C9M7pKn52I7a1VgMZm_ueRg2SGQX8WqGHmCU2gwxedghNK9-YOohNyAsfa1mL6t2UuffPviS-nXtBMcZKydwASRnQrvQYuyyO-Kf8zQgvsQqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IZyW1Tjmq5ZJQP3eHdCmajmYLVTOGlEvzYdRScYT5GYQaPep67WOuDeaDqQV7OxcGij2haTRCSeYTLFBCvLA9Bwn61cDersfXkLRmBSkwr1aSkDZk2j5a_EZAWiLvNCq7eOxe2BaiXnQKj3oFY-FT7TjukTWeb1iHbUAsPXKdQcW9C7GoOXP2n70xxdhRmNsYN7UI0on7YfQVOVEidP1KmvgsJliRbNgaLj9kZe-C9M7pKn52I7a1VgMZm_ueRg2SGQX8WqGHmCU2gwxedghNK9-YOohNyAsfa1mL6t2UuffPviS-nXtBMcZKydwASRnQrvQYuyyO-Kf8zQgvsQqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qilT7QhQH0IGjENi4vacYXBqoOXnYQ2PIuaHoe7YiKwc6Ba6Ks7zRDtUry711RhKLC7YZ6vBH4LGflPc4_matxq04rUj4DxtHL-MbzwkmCHPXR02ynfPhZ5uAQSqsP5_2PgZAFp96bfDMNm94tQNH_ikF3v1AQlESguyROGIs3rPv2C9maTYWr-hRGrgQxAfn45G-wLXhWmG5HId5garApkIpkUXee7nvRJ4Wk_IjdeYFJZdV56-TzPTYx5ZzvlSEhWRmRTG_UlYGx7KcLnuGJdkaVjvQ6nnLFkgXt3yjfhqc9V5imgQLzxCGsKsiKIc-eUdiAgVwE8y-EmWfAz1Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ2wUG7gL046DpBrEnG2QeC0XR-vsL1GcArIrq3CLQg1FiUI3qIr2z7cEBk_G0oSmLFfbrSccVI3HAmJ5UvVdJKpCbTAJCj_cJ64FO--J0N6JqebPyVbm41l0mNchfVZK4KG1Zu-RJmqOnO95rJQ-_FgCbeZgGDxzDumRGy9S9AIiPn2tgNEwcATuVU-QlVmIM3O3ITgekLsL4n7FgGxaH8x3Kfat1XAL1ROf8U48d4SduCZiLrNAtd9HjsV-kZL5urabAPAGmOcyXa1F5paudTxG_Y4sHUCe_YDRljd7s0bXaaqnvMX2IxsaLqUBVQZDpVYLid7RgV2CM5lN58lUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MeHBUOFpTW7gwMJ9QdUVAniMl7J7C7WfW_4VFdnoTufr_IY1aQyJkTbu67VKEuil0u9bsT3xX0oZHZpu6JCtjNYw8BD1k3rc4M1ANo0I9-HawmWqm7vKdo2on4-3F0KeFLkR7Q0ETBeupjsApooXyVZ1F1D_D63D5Gjp-KZwVU-BT2gpV45RpDW_eSR96HYv89BnluNm-UsJnHFi4cAhZ63N6Usc363wbVxXFeBnlHxv3PkjOUTJV6yeNZgvyWOJHbGA_0KIY56JaYzDjFDoHtikq1k4xbgvUoSWnHJ9CidYMjwu2yvoRBSorIDo15hlk05tCCuwcqYH_WH795sjJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbwijVVRQx60PHQLkrxWAccK00KtLdljr-b7Z_S2lNhsi-Fuy62MFhxCWi1mzfQkD_Lam8NqSlDjAq8dAkE0YgcNpHp23n4ByRu-13NMgZV8H22ZJyiJ9EDvfh_BgkJyGBx-V-XK-eC8rVZLJkja8iNngz-355xZnitrLePe_TtACtsgu3XvuPgMjWBQ47Mub5hEROsuOAFb4PMN4TdeWle4mvTrLU3AI_-Z1XZBcffJA4927pQvcDkoGQVRfUcOyD3cE_7ZhnLyALu7o1cd1lQugDHa-s83yOjb70GANqDf8fxjs3jTXRe1CsyvQQ9OEOEIAgrUg-l3JBb4_NAHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvb52JXVkfbOeAkossopVFT6MqPHAVmxOn1hHPtjhNdCywpe-YKLSYjOycTUWQFIZARmWNOoUN3CbcZBYnhtx8lbsMvv-_IfzYRIXJCF3lFpBgZ_K6_CqZvfUkHPQopBtplYu_MfnlWMedCW-7igBBN18snONnLWJQKZUaR0i6Ka2cOsSF-7hxHUdtsjNkQI3mavS64hD8wCpGM3z9oQHlyzOPgxPuuRc3yDQrTJwtLLKpd5Qx_zrzy4qMofN_UV366xSZ8Kmy6jui41le0wfYQSEXKJKsn2z49_-ob-KakY8twpvozlm55o3Z0aDm_ZhkyamP0PPEciaLMGpjGf8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fycvhhf_9qUIySTpbG4PdmjdYb6mwjIYbP07s6JliO3ov7IBid_INsjTo-SIiwrRffHcydkPzFjBLP3FDJl-UjTuHTkpbmtu-V8ZUBxEQvxsI_L6j7yOf-YO4U_ZYjhrfpK9Zz5hbMj5hGTgds6gjFxsUL4o6RTHovspRn9alWroHIzn14VJo4hfpBTW0P_IRhAuXvEi5vNcYciT4tqpUZuq7Gm_qTEOerQaFzkUrZ7HYgzq1_1yZSkfEOVA9uDKDpP7fy8vc7OBvwh_w5pIWyUvyx3H3fpE3lPFD-QC3wbRmEifVHRbKeQw1ZFV8Ez31b5P8E8e-Gl9dXqRLWETlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Er0TbnMEioiGdIH__42Z-zLQtU2ljX5ljFQTvV_0C_3SieuTPJoUOmRQ4U6iOxJQK8_A7WNfkxwk_3ubKOp0MP-ZVD9Wdh8wGDfMcc_ZYqSlEpd8aolM--aOynKW1w9p2isVtk1itMNF2CHBccRx60x2BTa_sHQM5cvRBXcylZCmuvBA3KnW8MQvzjU9G810NExQjivjnDHgwhmNMWBR05ReaD1jbqc4RE89EYdG0S9npe3Kxt15-SmEe_sJuT0cxbSZAz047UytFhTdDg66Tu7OgrLZq93Vwffv4BaASFWJ6se-_vbPYTLm2FlOxZBPjdYmV42OYrELNM-e0mp6sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl_C8y93k7nKeoxjvpLCE5XVvvMb3I1hgJgL1fRNAU3FBKcQRb-Xzsaev-pi0lly5Ntn-IXE7bBxKOpQnuoLcEz5lixKekd9zzDBNSUgC470xH6kW0wD8HiUbJXwDj1KAruvBYiWCqnZUvkR6qFZjhoqY79OQJh8sGkrPc-UKcmIvFmOpZtlc4bjq8DV9c51E2jWRKTEis2z5421KZfl-YZ83Lr83elUB_1k-5Ra0DLW25WH5ju-LAYRGrtmCoRlrxjkE9N_HSWRNZoQytiJd7NzQAi3HW6CpCNs0PeU1sEeRyxm8wGN0jM0I6AK0eVNZb36vNlQu2CJgg4izPCxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG0G48EYGsey2YvCNKPCQlBPkODctOR3Yho71no9J_8XEQtoBwgvksUb90PRuBxqB7uerdFiX6bD5YLqbs7JbZCu-4k4QyhPIxm5nrjq2LC4Of5Vb5zCDtnP6enp0AInTxBuAfwKNWPWpVgCtHsCNrs6EqxKShDHUgukDyWLepCe0ejrVDn13MgK8uhRLy8i_hJ-_LInQWT9v5Wnpynff5hzQ46_beguiVN5lHUK_rf6FP_85DDRe80brrEnTv4ryb5QWKSxb2x6reQDoAPfPLmixBe_WINSYTwLByfUGoZbKC82ClQqSNgVkD6euTHFc_HKfbWSlbvYjtgG_8cJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smkSXvUyGdxHiB6GvDM04il708XcnuglI5gvlsYJGw5y0cbGWVp22lLI4aR5uVMgiv0sBqUAoeOUfKxetyfrQl--MtLUBygU-vbZLL9yJz7-41iGaDSz86EDnfCqf9dLRjxM2MvbPIhxWj5HyIsljGg8Y41YeLkcRSTo2qd9s8QqzdmdCgBh2NeU7JIzCV3BHNOfSeikYOUP5yNEZIWbTVfqwVrTx3c8kDhYrVeV85syyef4ZNyGqv2D5fGQwn6OteD7oMNLOjc3OI4nS0d6S8jFmXV4fOIEgZo7-s00v1k9jDLQiDFJ2DAm8dzcI3jTAIN_fTDmemho2OOMHNfAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNzgADKy2qMc9ajM6RZuffODXli2XzKE52wDOKofgCCg4r0-8M3ZuAKj450AB2MdF2yUDgevTVfIn2tvumGWpn0ro408y5Q16rcobeKB_I1ibt90wezsj8Vgjf9xWyK3quptvozCvTMFbjZyoUA9DL7MzivOjycyKp_ZFAI9VwgTrp7f_1Ta2s_h3xgp9PdWaCFzcZqMpCM7B69odHPF7GvzPBtHxVk8BOMLWYSlShVbt6Q8vdG0DtP8MUTfm1O2EV0QfZsH7am7v0QAILUzNZok94fWgCQbpYS7RDHEUPUASN_xowmcJZ-5Hdo555OKETNRQrXsJg3A-iT_AORfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBI0XN1kiCadqgkfxNar93RyB5RVy6ZYpAV9g-pohmPqm03Ci0_uYvtc-xIX6DejKkJTd2ltRczyTZ917U_r6XfQohNrlZmH9wTqGdkMGCTeBUK95SPhn_KFb3d-TKOjBDzkA8V5JgZqZiIPmJQMN4I4WpvatlFNBHwuO-DuJNWIUtyIsawyNuLvwbC0ort0Y6B0_sAjxfApEyjDc-HxIF4p2-jnXYqCpi73HSnmEJx0TZedwzxW2-VNvLvIjzwOy_2IBtGGp7qIyKje7A0kHAs0LkWb7NBluMBXOTohiFSz_WGOuI5sMxFWRx3-Zmn39OohwKIQ3qQi00ImbPiytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X66VvQEJtt2pp8YdGiUg2pvHtmboTR7PkEt3PzFH-PzhBablvdB9VYXnidyYe_SlyHfURQO_Zjrl3AKLGt8Z_s-PSi2iJa9yiqt26LHcbBNxA4x42iO8OojfJPFnTPJ-PF-uJDcHZPAMnSrmStFkQjme_1H3RNpXVIp4yedIzqcyhFwoYfKm-KoyHP40UTJsgtbw1c5S647cyS-KDStk2tF_P0Rc5L2V2Uqk7azfF0AKun7wqejOIgR7VNBV5Yl0XZFSoXaRYAwY53QvYu0VUdcZaHgEjnRjO4KW1Z3OnRhgFa6Mrfr165-VA7LjGj6DMIwMy6ZPZtJ1-7CrfnxvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhUA4ligMyXDMEFDdck_8DkvhHLffNZ_R_W69jJxzp5wqMzBiCYkFV5LX5Fe3-BP7PL9P_OVUXMnvJi-cdLQMRw4rKsHfjt2Sodg_PKp6w90xvqHrMYJb3vQwwpZ83eK76oo8uv4lQFzg1CLWA2QVGO4qfRtrnoWBWS2eodMFIvLLFxhzMDIyMHQDjur2zi1yCcC9z6ObEePP4JldPXWljjBQiDy4TEhx1sFEkSLBjV88tDhsyB69PjqMYUI-qMDcNXXqbnMhsPcmMj_TqHfeLt46sBTUwWadCr0qpUEJNavW9ZbYD3L0mkL0f4rkn6H3JrkPBBY3pW4OOdoMV-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEv45dverOqbpiDyumNmF-QIHn1MjUIkfnEopjQDd3Bk-SqEcabvTOW3qoNAe0-JiyLYefwkdZaJIIFxctibj-tZPNavj2CASXZqUO5LiDcig3Bj-JYl15WIjxbVz18z0dMGvYQge60VS4O2_LAjOSptWvuqBpi2N5wLiR9TwuHvZGtpYEhFvOFj_0WUpX_o_jJywXirl_QCQLNgswss6se0b7hpWpZUyYdA1ir56_4o-LcjY2qEBETkHXyeRq1Zh5p5f7PB0ehpnD-UpoHFVqbK3su1az2PzSHrZBPwp10Gck4WmtiiBI6U3SVwJgieCSRs-F_BGUgJ_2qhgajzmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=mmOTMmWF9EahrMfYdPKqHyNr-Yz_MUbM6MjZ9wm03znbP2LwjxPOORd5AeiOajuWx24CBZUQ6C5uvKSrwZmzotp1ladjgMXKuQ0oPGqNcsF63HZPTxf0dpFdI_srF7339tH8bkkKyLl1Y_CS0eh3X71vFLbNgg5-Mipk1UXudgdQ9X2Mw59TGrWI6Fn7-1yT7HRaBRfSv2p1xd3i4Z63w6e8KeMWAd4mCs39HHbwPuAdneMN1T2Ae160swUHrfZz7vq0r8RJSo-idKLLiDQETMtsziKayUjrOTCAHRHs1EOeNKArHvrHo27N3w15vYgKWc9uzDwsGb1BO7io0sUWnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=mmOTMmWF9EahrMfYdPKqHyNr-Yz_MUbM6MjZ9wm03znbP2LwjxPOORd5AeiOajuWx24CBZUQ6C5uvKSrwZmzotp1ladjgMXKuQ0oPGqNcsF63HZPTxf0dpFdI_srF7339tH8bkkKyLl1Y_CS0eh3X71vFLbNgg5-Mipk1UXudgdQ9X2Mw59TGrWI6Fn7-1yT7HRaBRfSv2p1xd3i4Z63w6e8KeMWAd4mCs39HHbwPuAdneMN1T2Ae160swUHrfZz7vq0r8RJSo-idKLLiDQETMtsziKayUjrOTCAHRHs1EOeNKArHvrHo27N3w15vYgKWc9uzDwsGb1BO7io0sUWnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B__sMKYu8i26VPpZ6qbohPUSqh__ARhIydnnT1ECCT2e0hECnivNI6V9nwy3YiaKCuMKk143Lb3whFJ6EOVkZ0yuXK9TOaX6pOuc2BJWffGqPUWo8j1p505Lf17m98ekdc-WFKltOVVSov2k2vZ1B08jL4Je1h2yXLaP8R6N_1ZL2uyYJOUiOJpaE_POtod0kflxDpMP9qZhk_uGBtZxPSRRrXhVuhFO4wsXK5-_4YhIeELZLl_MGlhbYIhXmgb-ojsfpzD6kq4BVh-alMCuJ8LAS8TbVZjADuIS0IRD7xfcGt1vUG0uE9ovVjtEMzExVs5Am9SUJRW_0NM9nNedug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=fGqJL_wdqzjsTsBu63RYhVzO-zLlo-zvlRXcUzoy7ClqAZhUpKkDVry9-NJwFykrxdz9jxwP4K8BGSR09dlkmvzDCQeGes8TtdAzwhFBE42s7ccuFix5V92W1Ygkh78-VELKfu0wJTz3n3jr_S0J1LBvpZ2TEwq44uLQERsCVW_6FM9P0EH9n96AcA4HFx2GTFwqL-hR5biHgmumnRwJdasPPA3GzS5Bq8uJs2w-Hhvvtu_spWQK5UoBiTX-QVFxWKGfaNH-uTGNba0QiiwKBkRFTmQZGEDJzFeL_As904PnFityyIVNAa3-78Ro0wjApWkxrrSeouW-uTQ7cpLJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=fGqJL_wdqzjsTsBu63RYhVzO-zLlo-zvlRXcUzoy7ClqAZhUpKkDVry9-NJwFykrxdz9jxwP4K8BGSR09dlkmvzDCQeGes8TtdAzwhFBE42s7ccuFix5V92W1Ygkh78-VELKfu0wJTz3n3jr_S0J1LBvpZ2TEwq44uLQERsCVW_6FM9P0EH9n96AcA4HFx2GTFwqL-hR5biHgmumnRwJdasPPA3GzS5Bq8uJs2w-Hhvvtu_spWQK5UoBiTX-QVFxWKGfaNH-uTGNba0QiiwKBkRFTmQZGEDJzFeL_As904PnFityyIVNAa3-78Ro0wjApWkxrrSeouW-uTQ7cpLJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=vISX17ofvPqksw7MfDpQs7IjDxr_ibIw4sGzp0k5Ezq030eDN6yXXAcHijA6EFYX05S6zGCQ2LPpuPGvYG93IfauaDFzum08UBNiNPAnZlHJ6kAcERxXyM6s5MQJKouvuRa0RF_smpWVwI1gVpqrdaNKfTSi2TeL3mrbjy8MtBfhnS13XusJlIcUmC7EW4MHFcY_dqOFmqhzDolNKsVnRzTo6TiIiJ64P2l9A5qcHrhJCuurJ3A82VHhLErJeiLBGOhYOhZCPzASLZY8dQNkauK4lQzcRXRALFw0gpThfU2eUSVroAJwikslyVYn1ZdNv_HOpaRv7ZF_zc0knCZNDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=vISX17ofvPqksw7MfDpQs7IjDxr_ibIw4sGzp0k5Ezq030eDN6yXXAcHijA6EFYX05S6zGCQ2LPpuPGvYG93IfauaDFzum08UBNiNPAnZlHJ6kAcERxXyM6s5MQJKouvuRa0RF_smpWVwI1gVpqrdaNKfTSi2TeL3mrbjy8MtBfhnS13XusJlIcUmC7EW4MHFcY_dqOFmqhzDolNKsVnRzTo6TiIiJ64P2l9A5qcHrhJCuurJ3A82VHhLErJeiLBGOhYOhZCPzASLZY8dQNkauK4lQzcRXRALFw0gpThfU2eUSVroAJwikslyVYn1ZdNv_HOpaRv7ZF_zc0knCZNDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwnKrHGW-kCprLGvBRiuBBSKeMH50lfWFyq0kGgC-264AJaG30FIBevMWl7EXeR7gVlMvY3YMIL_Nj0mSISSXGDvpIL4U-D3p2umwnzvaKmpQTfS3cALxmOxhept5rJhDq6UW5exTkLf4BmzM0DZo6Zv11sx8bQWk234TesYK2S_BJGI8w4_-CvpOrXJWkx0hWx5igFxRAkMzuNieQQoMfpxT6-bvjcJQOZgcxppP9QuS4BfIlJrsgL1rbZ2U0IJdT675M-BJzI5-OZz_2oQjES7-e_iEOOkHkMsnvybiNdAnB5XHtKHAR60Vj03szgWFUHWsqHJr28YuyJ4-6OPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=qYrEC04uE2mSfoL-OsL0Gr3PcxJRymIBtE9BmWoLddtxe3fojkTvJEHYCwIr6idxEWR_zmV4SV8Tyk9upWJriwRkWxzGMWzAc0E2uh8rvB-hX4fW27ECTuOoSQ89ANWoCYI0cy3EZw6m5oBkixmt_DYwSq0D4JwuVGNJAsCfI3KcVDpFtHlp4E-RJpUq3yyNkgvODNWTgJ0Mgz41HGlzise_L1CBsVY_cW0crJ8c7JdGD_i_Y0n0i87rbgGvlJJo3mj4sL4irrEVWSSSHeT90FueBGQ8u1A1Qq3gp3uOC-j3_2CX2V8LgCb02rJLf8MF-wf0CywaHZ9zA1anT4FMKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=qYrEC04uE2mSfoL-OsL0Gr3PcxJRymIBtE9BmWoLddtxe3fojkTvJEHYCwIr6idxEWR_zmV4SV8Tyk9upWJriwRkWxzGMWzAc0E2uh8rvB-hX4fW27ECTuOoSQ89ANWoCYI0cy3EZw6m5oBkixmt_DYwSq0D4JwuVGNJAsCfI3KcVDpFtHlp4E-RJpUq3yyNkgvODNWTgJ0Mgz41HGlzise_L1CBsVY_cW0crJ8c7JdGD_i_Y0n0i87rbgGvlJJo3mj4sL4irrEVWSSSHeT90FueBGQ8u1A1Qq3gp3uOC-j3_2CX2V8LgCb02rJLf8MF-wf0CywaHZ9zA1anT4FMKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct5xAm11SIKG3j8RKRXZa9dxDMsiHj7op6fQg_2HmYpK8U2rz1y5XEaHCBX_E6Hm7_olArqMZWPH_KWeTW5Yd-Y8pjy7-FVqvQv9RwIBzS80VtsprtnF6vG60OahbkiqCRPBjSI27l1UmXFQvGW4n9041QfKyfAgiTTGJhO_2nhSXHMgE1IwmUF8ysLxitIQ_zGAmcziykfD0r-iTluo6rrhVFbSpk0Sc2OOI9bLbmKD6pqUqrewo0fM-ZPbcNnZQ7_-S_6fmawNS6PFlRTJ1Pua10fKYoFceAXKd2uWcufga9GmtD4DiHMyNHtfTvKrCV9dbU2TLa9ZkwwIpIrE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VK69JynOd_xGIzgWJQwYOsOwtGHOV4vcuBCiD1wwX0YkU5yUM7I_N4jZY7n_xKDbyTtLdcW1lEvifhnYxA79e-akfxPlQ_JBoI7RRZeDbHeCZBFEv1rhDmK-E6YGw30qKu0NYTxR_FjurEQwAGOyMTJZ4VUGO2xTvxCNAyxNotwCr1j9ETcxy5UFGPUKmzesZ_HuYuX88zZc3YvyogO_dtNLkx8l94c3k_rDLfvH2Q4uja3mw0jhWm2hqjioprxj0z_TujkWYoaIAVOGhFohbOdS_Kuq2HZujvaTqMFibkwNVOoKdxnG1hQyV3HMOfZzKsqQLP_HqqinSGDCkfk8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQPuQtfUGIhDrNG4lQjPcl0gqogdRcsyVoYRf1aFChNcvYRfqrGgzOxy5HxxA_f2e-I0yue4Bxv24uQnuWHKm8NbtvBiJvq0t9nESqRA8TqhmB8hl7zRrBNO8Auki1kUvLcOIlZzInfPXv_Uqtcs7M0QFfj0CihXT8nUSe6YXB6GXRcboZzGfpXq2_35Nhgl3Dgo37cnb9uf4M5uDYIA2pe-6YqTapM1ERRsmZFQqbZ31gWz9p3GjDrnvhfFW0hXOscnp8VriGKLY4KYe_pjfqA38-nFbbKIxp-n-cnHCX-mHhvUi86ow3gUp0on_Wir1ExJ2nX6AKYqKs3gtw0NFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1ZSTKuUBBVVjjwTC9g9USp3Z1TGHgvYijUW6Dh1TNNaJ3WMKrDDfwrHP7POnq9KlhUcNKw_0gmkjs8ZOr9PiCUCI3L67JKjXhjFFT5K6HjgRxHDE-TJLNE2EKhL_lN3F3WdzipiN1x-sjoF1rSImyUghEfnp-pFLu36R48i_5Y43babbJGg_lroQIVumUk4zJQrowT2iGzVIOCyCzFcwUm_ZwD2X3IhJHt5nROG6JpnJrqEs0auYvesu8pVXx13DNZyzLqwVJIzMjT9mb10vQYxt1L_W22UYfL_ZCzvugqiLLxw3nEpNnwMkyW62ucYihIdaqZT0FBSXuZ4hq2XJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=JQBDpIzE0j6gu3rdjx32t40nVzldBF8qVVDuC27VQoMKuVcf8LlNY3mGPxpqJzc70qdf58H3Sc_bbaKBtcMARLJ0xIVmWu05WjjTJagpsiHUY9K4Y94PEDeCpWzKLcuE_mE_PtLuqj0vYirfxcQtGWv9g9nH25RGiIBJDMb_2ffuEJ5BikW_9fHRhFjhtFFcbVm1gITZ7ASdUuH3S62CA24FqYn3c3esIwkiHvaN-rKQgiqP7UIVpdaHsKdJFBV5WR2j3MjQk0kHKs2mk0ysmc2YSlNxWOOPJ4WF-ChtVvythSg87YyJ2OaI2Z-qQi2ykXVyGPSo4DrM4JRy4VbG4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=JQBDpIzE0j6gu3rdjx32t40nVzldBF8qVVDuC27VQoMKuVcf8LlNY3mGPxpqJzc70qdf58H3Sc_bbaKBtcMARLJ0xIVmWu05WjjTJagpsiHUY9K4Y94PEDeCpWzKLcuE_mE_PtLuqj0vYirfxcQtGWv9g9nH25RGiIBJDMb_2ffuEJ5BikW_9fHRhFjhtFFcbVm1gITZ7ASdUuH3S62CA24FqYn3c3esIwkiHvaN-rKQgiqP7UIVpdaHsKdJFBV5WR2j3MjQk0kHKs2mk0ysmc2YSlNxWOOPJ4WF-ChtVvythSg87YyJ2OaI2Z-qQi2ykXVyGPSo4DrM4JRy4VbG4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=M-ldL-4jOGFuvh4O9pl1UYUadAJK-YF54hD_uIWpKAe9ZPE-90tIJJqgx2tu3ZIX9ZgIf0JgTwJEo6jtGYGiAl0s02noYvUfI5_q4wPDbnS7TPB7ozX5LdN8-j5vgAV-36CBDZGPWbVtfebBSXrdvnCuX3MP7qrPZoz9wbf2mIEBfdoa3Gl909tmpddehvEfYVsODgVcOT6usyzBZ0z7knC-kFyqKpdOXajKDiau-uyRvuY4x0e8sfDsNyMGE75gSh6fx8dDADfhmLhj3GRjYJMeIncpKEL8YIe0wF0-9XzAExFET_I92MR7FeIVivVh4e3qP0OlWuESdgcDy5FHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=M-ldL-4jOGFuvh4O9pl1UYUadAJK-YF54hD_uIWpKAe9ZPE-90tIJJqgx2tu3ZIX9ZgIf0JgTwJEo6jtGYGiAl0s02noYvUfI5_q4wPDbnS7TPB7ozX5LdN8-j5vgAV-36CBDZGPWbVtfebBSXrdvnCuX3MP7qrPZoz9wbf2mIEBfdoa3Gl909tmpddehvEfYVsODgVcOT6usyzBZ0z7knC-kFyqKpdOXajKDiau-uyRvuY4x0e8sfDsNyMGE75gSh6fx8dDADfhmLhj3GRjYJMeIncpKEL8YIe0wF0-9XzAExFET_I92MR7FeIVivVh4e3qP0OlWuESdgcDy5FHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=T3uHwx4GbjdEV9iBvZWPsihVPn2lcrFF_8kdhdiXJ57G0nzde_DFUXHRCj2_CINYkcZxYMUCuhH9pgGSC5uH1T7wvvd7rjQ_NSOCiZEFaIN9_eW4sS451DdlSDxsHIYPR8s8P4B3dYONvG-WX_7bihIgj3s4Rmi-1xQiue7zUxm74gKaA5bpdd9tQ48V220jyQe3XWa-9oPdvf3OvLC3vxQz0002p-wcFELenNGs15Y-_YF1Cp1XYBelhKRqkQDy9jTTYn5EkfCM3_PlZeLEcbHPTUAlsV0dLVILWs5VT-xKfChChLPGVQDF1p8Yg5XNBMQEJdMy6aW70p53CaMdQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=T3uHwx4GbjdEV9iBvZWPsihVPn2lcrFF_8kdhdiXJ57G0nzde_DFUXHRCj2_CINYkcZxYMUCuhH9pgGSC5uH1T7wvvd7rjQ_NSOCiZEFaIN9_eW4sS451DdlSDxsHIYPR8s8P4B3dYONvG-WX_7bihIgj3s4Rmi-1xQiue7zUxm74gKaA5bpdd9tQ48V220jyQe3XWa-9oPdvf3OvLC3vxQz0002p-wcFELenNGs15Y-_YF1Cp1XYBelhKRqkQDy9jTTYn5EkfCM3_PlZeLEcbHPTUAlsV0dLVILWs5VT-xKfChChLPGVQDF1p8Yg5XNBMQEJdMy6aW70p53CaMdQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=uIiPVaDKh5ab__7ABXNe7yVkXGJe5YENtw-3Zvpr940TT7lF1ZRs4BMGVKm0ohLzUO2dMaf_HL9CMbaWAB-wIsQyvVqHdMCqFVuAr1h4kv6i2Sr8SgFEdaXDwA-1j0879iDrr3RO0JMZTdEaTKNo2eIGl60tvbUAIBOuvZ-Vv3rxMwQD5LuGnsPuy_KtWI43zhaP0KYNbQR2AlNiqHnY0e8GR5A9c7kjL-RaA0FyBk6BOGdqIRmRxLRe080sAmCocdELujmHcakU4mc3M_n6zS4miXVzeEUiq4aJHPzpUsU-sLoJ-P4e8VKLXITOMzU5S7t_W5kLayMHbRLV-Rr4WF51s2dSatkQm_OtALkRtQ6BAzlpO4-xdA6JHN6Y-nO-01VV7JH-5al_LSpbHUQSoRIjUI7HIc4pnGDkpZtMXZUQnHge5WKT7MXYn8S7XMrs7CuKNBepHdq6T8_LnwCMmF9uvqQpQBx0HE8jPlmuLKlVWq2HcEf_xo-p63MYNkLunoSDnDjoAgQ5Ne_p4au5Jo7jB9ctKS_o6nzmHP3xRA9NyebslktIxoYzBLrKxSEw196yvvTv0y-nzExhpL33-QYmvzezLg6prk4yqcjw4u2NWhcnWVnmMHrKWIRxCmT5DqqUdT2qR7a8-w3XZiIdHEiJQ-EkCudOau86ngNMgrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=uIiPVaDKh5ab__7ABXNe7yVkXGJe5YENtw-3Zvpr940TT7lF1ZRs4BMGVKm0ohLzUO2dMaf_HL9CMbaWAB-wIsQyvVqHdMCqFVuAr1h4kv6i2Sr8SgFEdaXDwA-1j0879iDrr3RO0JMZTdEaTKNo2eIGl60tvbUAIBOuvZ-Vv3rxMwQD5LuGnsPuy_KtWI43zhaP0KYNbQR2AlNiqHnY0e8GR5A9c7kjL-RaA0FyBk6BOGdqIRmRxLRe080sAmCocdELujmHcakU4mc3M_n6zS4miXVzeEUiq4aJHPzpUsU-sLoJ-P4e8VKLXITOMzU5S7t_W5kLayMHbRLV-Rr4WF51s2dSatkQm_OtALkRtQ6BAzlpO4-xdA6JHN6Y-nO-01VV7JH-5al_LSpbHUQSoRIjUI7HIc4pnGDkpZtMXZUQnHge5WKT7MXYn8S7XMrs7CuKNBepHdq6T8_LnwCMmF9uvqQpQBx0HE8jPlmuLKlVWq2HcEf_xo-p63MYNkLunoSDnDjoAgQ5Ne_p4au5Jo7jB9ctKS_o6nzmHP3xRA9NyebslktIxoYzBLrKxSEw196yvvTv0y-nzExhpL33-QYmvzezLg6prk4yqcjw4u2NWhcnWVnmMHrKWIRxCmT5DqqUdT2qR7a8-w3XZiIdHEiJQ-EkCudOau86ngNMgrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BgIk0UXx4omjpeMRDWYxmvEt8hPAI0GF55XpsRJpovigfq2Tkw-fqgoVeES5pS77Qr8E8B5AL0_9rX2BlZdRfVRpJmj32k9MGceqNtHZA2kdr0YIWGfZuPWYPvQ7_mb4vDvTcVBosSW8pRTKj-YVozZP5FN8K_vWoiEFZIEjSABd1Thet4ByG6lZNK2C-19o5vqnajNGATp2o73lPt8Z308ogh3Ozde31lOprKD98eZcc3r-rvcI7DpULYFKbdXn-osPn3L0NYvqtS4arSOK5uGhaKLlJfigq7UpEAGiQoRhmR4gCg00g3zLlXqRQV18SCyx_K_ZtEzc9V-Sw-7RKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=BgIk0UXx4omjpeMRDWYxmvEt8hPAI0GF55XpsRJpovigfq2Tkw-fqgoVeES5pS77Qr8E8B5AL0_9rX2BlZdRfVRpJmj32k9MGceqNtHZA2kdr0YIWGfZuPWYPvQ7_mb4vDvTcVBosSW8pRTKj-YVozZP5FN8K_vWoiEFZIEjSABd1Thet4ByG6lZNK2C-19o5vqnajNGATp2o73lPt8Z308ogh3Ozde31lOprKD98eZcc3r-rvcI7DpULYFKbdXn-osPn3L0NYvqtS4arSOK5uGhaKLlJfigq7UpEAGiQoRhmR4gCg00g3zLlXqRQV18SCyx_K_ZtEzc9V-Sw-7RKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=byEO-Yo-4eNEr7psBlFf3QA-wBJbExkuhvOveBHI1TXu44aqaj7_SGuFMwRDhWn3YNRJSCw4mk0EEHfE0H7CHvak-TCkyXj9sPAzWUmpzTl3rylwOR2bRa13rSCskB6J8HZaL5KqXSiDJ1FVWcIYfdN2hGmMxeR83sCub0mY0afyUCPXrIItGelE7bMsMF1S3Tpj4v81sj8fXHg3-x2FOGPnc7PJPSviomkpxXlIrR1OdPXq9QWeOV2EaAF8tKDdO1XOfUwOKwLOgWFQkQMR3t5KNu7PVKruOsSJ56W0tEa6o644jSQANmmT9sRyOArUlHaofVdABeGI7sz6bb27Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=byEO-Yo-4eNEr7psBlFf3QA-wBJbExkuhvOveBHI1TXu44aqaj7_SGuFMwRDhWn3YNRJSCw4mk0EEHfE0H7CHvak-TCkyXj9sPAzWUmpzTl3rylwOR2bRa13rSCskB6J8HZaL5KqXSiDJ1FVWcIYfdN2hGmMxeR83sCub0mY0afyUCPXrIItGelE7bMsMF1S3Tpj4v81sj8fXHg3-x2FOGPnc7PJPSviomkpxXlIrR1OdPXq9QWeOV2EaAF8tKDdO1XOfUwOKwLOgWFQkQMR3t5KNu7PVKruOsSJ56W0tEa6o644jSQANmmT9sRyOArUlHaofVdABeGI7sz6bb27Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbqCmPsh54LXQFLUvMcx7Xem0BDCCBlyVETE6h4xp5LfEPzL5HcvDWtCHgi-H1JPhULCBu9AHxklS_nQ1E_0ZFp0Z9GhkrxU8WGX5UM4l0Mt5qFnkfatLS6LJ90WtmGj4c_1EWzkvbZt49fsuc0PbUh2yt5Al5ajfb8y8w0rnlD8wJs-Y1IHxjQ5tNY9oSaE0S9nTYP5S5Sw8AsglrqID7z5gIAd9GBLpNuBwTxZJUmhVg5ntUWJveXMo5sTglcd8r2boqOwAh4ynHeeqhKaDtYQ1-ZIhyRN0k25mERpZBObErJvyniir2-dsrak29Q_3Bj15GgCEblx0ynWgQFL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=hxakVXOwgAm6JvoGF9nWlYC6benmNoUWT4G3Od_qTnmjfRqrNY5Ybim823vao4OYqNz0P5OqTqv-Zn7UaNiwucRQYJn6ZNUk7F398OJMOvsj1oVxj0Nua6-QenaO22JJbtJnv-7g_y9VUOn3yeocZgmb65RlloV-JbFeyw-9Ap65wd3ZrPxCQV2GN18BIxanWuJ1KF_HaThK6RuOddKyszUtCR-aMRmGUQyKD8Tu8e1Onj5FwWJe5MaQQ8z8g98ApHovg1x5-DUkyXIWLlkXRAembVXKQtWHFzyrwmVc96kYkeLWy0FYeuZwsUxyqPBRaZlWWvCVOJnc7kKf_rErrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=hxakVXOwgAm6JvoGF9nWlYC6benmNoUWT4G3Od_qTnmjfRqrNY5Ybim823vao4OYqNz0P5OqTqv-Zn7UaNiwucRQYJn6ZNUk7F398OJMOvsj1oVxj0Nua6-QenaO22JJbtJnv-7g_y9VUOn3yeocZgmb65RlloV-JbFeyw-9Ap65wd3ZrPxCQV2GN18BIxanWuJ1KF_HaThK6RuOddKyszUtCR-aMRmGUQyKD8Tu8e1Onj5FwWJe5MaQQ8z8g98ApHovg1x5-DUkyXIWLlkXRAembVXKQtWHFzyrwmVc96kYkeLWy0FYeuZwsUxyqPBRaZlWWvCVOJnc7kKf_rErrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYI6F0Ez6007iHHkPB_nowVM86Nd7-FdEI12nXF5Asv8P_32o10vyLf5T4dRpDZCzK4-wTImHknsD9tCYHNJemJvZJOkS1DrHAIdD0IAwNL6bxymY8UTZKUDEG9FOIdrAVa6LURvFXreutIerSIp8n3MK6pdeZt455jxc8KdxkoFSkkANWM5JeqH17lh8n2p82Qwpf5DScoaeY-ByLSCwkJXXV_ngDbqihCKTcbDEQpLJv8oXyDdVeeCEtC7HPbFVvGgdFEvDFXZEDPWzF4ZYNWVy4wAQBR642Hs_8b-rhH2AsLgrkDUTCLZ07YD95lgQCg-tdZf9Z5DolElqG2cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGeuGadMg2zIUDq59LBuX8nukXTEUzKBleur7mNdu6r2ZkPYMRs2xlVQqnaySyeTT0Y3OL6O2EGkRcxge297pW_mZCqfqK5hUNhG50cpFeoZO-CVcX88hDyGWCVzoER2jUgOZifepP2erkts5VOBoW4ue3SvTIPhMcRtdTESr-zK96BQmvrMrlpo8Ai0SgkKxEwAWaWxxFsxMj-i14eM4QyQIuNYbti5KXTsnd0QMOzI5rDskF51bNVy_armM2VNMJimUgKOPav-PxdKxbtWplolMC1cCc6ZA3WfxuGgkEm6mdkcq8gd2_fmxuybG3oOpYcD8lMGCF9LzSxPwx4SEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=bsF7fgq-1QzGnx72_Dsjy6l_gA_MNlSbbqaGYcaCc7oQShXtop0_Td3VxhMggiVtD3JTILVQFU3PU9AKGwCCjlIoTmlDr30SLjjqudPegOma-hs9KpdIaI7ULXOtI5X578AHoKMpmG9KIR8uMp7747sR1FA2j1AhhZhIzz21XWeWlpTsPX9xDIXwbR8qbjuVBrMRZkfQC8gfmxHh3CRgOSw7VVQ7F5HqpV4vkA-h6NPEGvxpllQoOX2zXR1Y64HvGraB4Z2-DHastiy7WryX9Y6JhtoL8YE9PdiC_Eo-hccq6z2UrBV7caLECU09pXUU1Gc0p3eU0oNDpfbYlyMMLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=bsF7fgq-1QzGnx72_Dsjy6l_gA_MNlSbbqaGYcaCc7oQShXtop0_Td3VxhMggiVtD3JTILVQFU3PU9AKGwCCjlIoTmlDr30SLjjqudPegOma-hs9KpdIaI7ULXOtI5X578AHoKMpmG9KIR8uMp7747sR1FA2j1AhhZhIzz21XWeWlpTsPX9xDIXwbR8qbjuVBrMRZkfQC8gfmxHh3CRgOSw7VVQ7F5HqpV4vkA-h6NPEGvxpllQoOX2zXR1Y64HvGraB4Z2-DHastiy7WryX9Y6JhtoL8YE9PdiC_Eo-hccq6z2UrBV7caLECU09pXUU1Gc0p3eU0oNDpfbYlyMMLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=ZjOfjC24BxXKAqIPT0H7Jnbm69fCOUMYsb-QWPCSlnNYx-8h6kru-e93-H_KlJep-gqcPFcCAmuDR4ksNS2EM4CBqL0XguSddIPA3uWbmMUC6yJRU9JKau6uQ7ZcXyi-9DNxFbwzshaBzoYTfCTrtX6RgXd4WlPQYe77fvxtH0-mbDrGW-RvKdB2zZGF1zlEscOReqZk9OZyXWxYoLtcTC6SW_MEjPGSts5pwsVT2hD2YP5ZcEecXMCWx1M8DSIfbsHkfM0EK8tGyuf3IbcbH2wari3-wZ2vYJrfasrdQalvIFjXVJ_r0h4x8UutfyphmEF2XzjOEbZAkQJ8diGiVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=ZjOfjC24BxXKAqIPT0H7Jnbm69fCOUMYsb-QWPCSlnNYx-8h6kru-e93-H_KlJep-gqcPFcCAmuDR4ksNS2EM4CBqL0XguSddIPA3uWbmMUC6yJRU9JKau6uQ7ZcXyi-9DNxFbwzshaBzoYTfCTrtX6RgXd4WlPQYe77fvxtH0-mbDrGW-RvKdB2zZGF1zlEscOReqZk9OZyXWxYoLtcTC6SW_MEjPGSts5pwsVT2hD2YP5ZcEecXMCWx1M8DSIfbsHkfM0EK8tGyuf3IbcbH2wari3-wZ2vYJrfasrdQalvIFjXVJ_r0h4x8UutfyphmEF2XzjOEbZAkQJ8diGiVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=pVAZZtFyqi8eDmKdUNVwlGhetP5DyvTIy86u43VW72VEm5hh-Fk48D5stkfqeGW6tSwSUBUTH-aC7goWS0HvxnVIKPbEcMXNAdsslCG36qhvWZHEOFe6_HUSiTvXzu0odxcabIyy9nwt3erV9vXPjpzlxrk7M9SQQCwrvr0do3wkhYDrJ9wfTsfkqhVfdcPfzmvljcAfbAyu0604UyHxxxnPKX0fYIXoVp24rj-9PJ4Fa_aoZf_JCtN_-Nb7W0r8KlMnSiwTSW-wdN5NlfaHzVSOT_k98VlBw2Jh7Omkz5T2GrRdGTvnVCCW3Craaj6axAA5YMXtvC6vlfhUR0F4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=pVAZZtFyqi8eDmKdUNVwlGhetP5DyvTIy86u43VW72VEm5hh-Fk48D5stkfqeGW6tSwSUBUTH-aC7goWS0HvxnVIKPbEcMXNAdsslCG36qhvWZHEOFe6_HUSiTvXzu0odxcabIyy9nwt3erV9vXPjpzlxrk7M9SQQCwrvr0do3wkhYDrJ9wfTsfkqhVfdcPfzmvljcAfbAyu0604UyHxxxnPKX0fYIXoVp24rj-9PJ4Fa_aoZf_JCtN_-Nb7W0r8KlMnSiwTSW-wdN5NlfaHzVSOT_k98VlBw2Jh7Omkz5T2GrRdGTvnVCCW3Craaj6axAA5YMXtvC6vlfhUR0F4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDJ3iiEKZ43d2iP8BQv8Ql4uUEl0ZtyVVe9Z_Y6-GrutaxLabzOD8tXFUVw2Z0Hjfi1KEhHlYLpZ6GYqC_SLm-DRP61_vOaTg67FxCPrt_cuNgwUFtQgpB0dsx87CAV7y81WWG1KzEm0POuXZsF75IBRTE66Oj5axQCaVHWuzdW428N_AeJJIkl4FWXHFEFS-9ri0ff1y-wuQj_1hNGI2ERYmiYK1fe-6o5qdFBQdw5qI0QXsP4TONK_ocKRStfLKcOMNRf_zCr6nHz8uW4skqxTBNj29PkEiKlCct54zvWFMGx8fJKHcS461ksCb9ZjM4DpakZvA52pmxFxx2LrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=QHkb6KSWt2LEWalFs243ywy2AWeaswjz86ryPBJTCksSs1bhmqK2RVdlZFlKoiZ_3GGvd4eTsF2_lvis0QpDTG90A_Zof1Tyo9BICd0J4YEDFgEpr0sDRoH5NgvpxjFIyUGlcl28rGiMNP4a80dsaGkEh_8WJw1U4kz_nRkSL9HkqlurYbe2fAUly7rUdP0Qc2TP4BYljbkxC36dV-ATtcRcoOdOzr4GiRzDmKF6SrVDYeU2025LFRL6E7byOjXI6gMCe-Q6AtDeKE3XgO5vDncWDHI-DxKsQZXI4im_vKhh778BWr2OwAItNzkvkNePHmok-gKKwcp8QV4AVs80Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=QHkb6KSWt2LEWalFs243ywy2AWeaswjz86ryPBJTCksSs1bhmqK2RVdlZFlKoiZ_3GGvd4eTsF2_lvis0QpDTG90A_Zof1Tyo9BICd0J4YEDFgEpr0sDRoH5NgvpxjFIyUGlcl28rGiMNP4a80dsaGkEh_8WJw1U4kz_nRkSL9HkqlurYbe2fAUly7rUdP0Qc2TP4BYljbkxC36dV-ATtcRcoOdOzr4GiRzDmKF6SrVDYeU2025LFRL6E7byOjXI6gMCe-Q6AtDeKE3XgO5vDncWDHI-DxKsQZXI4im_vKhh778BWr2OwAItNzkvkNePHmok-gKKwcp8QV4AVs80Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=oEjkv689UFMoOD7mDETiJKLRrqlE8Jqk30Fr2mltxLM2hm9YRywQg_q80DH3fjVmtykr17Ry-XV1hcNJq-C55T-wUoqB-zpEbRfZOzAHcI2jtvCP-2SesB0BiNe1vET597jPNm8zwKirWy9KR0bfyp9OCGclbp_zXaCQOwIoHFFJmix1gkJzxIMwbmPB_7GLl9-yPa-7A97SdQh2opSfCAU8WgYgl5QQ-eeitmwFn_BjIhQZ2DAkj1mLlcK6NLGbbR0hsSdMF6-0KKDh-wr8c2-xrUYKmIDnsBkhR64E0lGyHtvMF4WbvXKPEeBur92ayKQaTnED8NDEG6QQQ-rRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=oEjkv689UFMoOD7mDETiJKLRrqlE8Jqk30Fr2mltxLM2hm9YRywQg_q80DH3fjVmtykr17Ry-XV1hcNJq-C55T-wUoqB-zpEbRfZOzAHcI2jtvCP-2SesB0BiNe1vET597jPNm8zwKirWy9KR0bfyp9OCGclbp_zXaCQOwIoHFFJmix1gkJzxIMwbmPB_7GLl9-yPa-7A97SdQh2opSfCAU8WgYgl5QQ-eeitmwFn_BjIhQZ2DAkj1mLlcK6NLGbbR0hsSdMF6-0KKDh-wr8c2-xrUYKmIDnsBkhR64E0lGyHtvMF4WbvXKPEeBur92ayKQaTnED8NDEG6QQQ-rRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=b3BLWAqMBRiXppkFk4zDXgwr3RmaNz-c1EbHAdX45bIdIU1iIn2vgli3hAERbouusOwBL-U1FfXF82EVCMDKoPV5rkWagI1XQrX7V1jWYnnbOj3Ibi67DJWs6sjP_iTxhjELYEqn7DbEWQxPdP7ZwbDhgtPHtAQ5alJ3L6KKcaWG0Il_PkjZhLlFJUAMegI0a7KuUWskI3IRNI7hm9BI0zgze4bNa-d7DtxGZM-7PY4ItbjmFiCA-1ui9vApSLABuW11mWk7GrWYTAZwt12ycGICnW9PXnUEj9wWfd7mBCv9x4UFtZVe0QaILR5iSkmZkljXulc9DRmkqHPn1gPvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=b3BLWAqMBRiXppkFk4zDXgwr3RmaNz-c1EbHAdX45bIdIU1iIn2vgli3hAERbouusOwBL-U1FfXF82EVCMDKoPV5rkWagI1XQrX7V1jWYnnbOj3Ibi67DJWs6sjP_iTxhjELYEqn7DbEWQxPdP7ZwbDhgtPHtAQ5alJ3L6KKcaWG0Il_PkjZhLlFJUAMegI0a7KuUWskI3IRNI7hm9BI0zgze4bNa-d7DtxGZM-7PY4ItbjmFiCA-1ui9vApSLABuW11mWk7GrWYTAZwt12ycGICnW9PXnUEj9wWfd7mBCv9x4UFtZVe0QaILR5iSkmZkljXulc9DRmkqHPn1gPvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0Njs23q2q6A_bt3fZvhofkq6Mo-eAh07xbJwpVIFGyfdM3iHU1R8L2wvnO_SCP6Q4VlO67sOPjXTnIHiE1BV9eVBx1UYNXgWcdbLoQE8r1e-sntFXDvJxYmXTMUMpIZbB9wd3dbnzGSG-gjQcckMS0ilajLhvGQLrdrjKAPfjkC3QH0_kX1QC2z07sOpxdmeg7Mbd7ytQ57mj1yKWrFZioMYVRgrAU3Hf9zkoleDun4GoA4tg396dH8D8jOBwd-_7KE2Ht2-zmlzgHPCRcUJWLcbB5Q284WEcJKtN9pQvDgHFjOR3PNEKLwgz4S2Co0EX6aiT3r8x7XbkNY133ARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=vkgLKXaLm9XdVEz8xuPEhFHUl4S2plmK6H7Er707Rao2jEXtA9bW1u57bEcPxiC9fu7MpgyuJwgLRc922qVs1B1uJ0VUzLN9m8JQ_tAXjZjKAEn-cgsqrsVpDXA_MW2jjACb480MlP570MhkISPPk2DDzMFn1Ky__Ieuy4wCFQrk0zMNjBZlMKd_80OyTiZMQebmmNF7_qomySyYe77xPmZ74Ku9hzyhL1H66tkrUIy0wEsBcZXxn2wVpsgg31RCPkOMjE60JMeNu8memzXd54qAe99Yt9vYTJwHlB2Em3KVzsoSwcG6tjaTu-xBHCNHJK01M_pC1yqzBOBZPXsZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=vkgLKXaLm9XdVEz8xuPEhFHUl4S2plmK6H7Er707Rao2jEXtA9bW1u57bEcPxiC9fu7MpgyuJwgLRc922qVs1B1uJ0VUzLN9m8JQ_tAXjZjKAEn-cgsqrsVpDXA_MW2jjACb480MlP570MhkISPPk2DDzMFn1Ky__Ieuy4wCFQrk0zMNjBZlMKd_80OyTiZMQebmmNF7_qomySyYe77xPmZ74Ku9hzyhL1H66tkrUIy0wEsBcZXxn2wVpsgg31RCPkOMjE60JMeNu8memzXd54qAe99Yt9vYTJwHlB2Em3KVzsoSwcG6tjaTu-xBHCNHJK01M_pC1yqzBOBZPXsZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4_Pe_c_aoM8AlxQeuzYzSmQZ60cSzMzslfwHiqmPsGKYIJ5b5BX1_UUa8uyyRzOXQgTsvTBARSWttpgv3chXydPR295ch1U59-QN9jXI-cnprKj07ys1tA5W1buBoa-S7QTTfmnUow_IDRFrrhtuMJ2xkt04yoCIH5rI4v2cECcN52idSva4GK8qW00_frHfa0kWiKokEzUZ7hyKT-rsRqwGe-oyA_glljJbFjOUCOc-ypNSKVCuuVCqI-goOxfkMpgvtgZNpQnih-Acr9mV5HzB-9aSbDDOGwynhgHyk2gTTmn5Qimd9PWeM_Mue1PIzDDwt5-mKRlZXzkML6r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=eb0AYHz_NX7Jr9BWiXG2bgW_JOaFx8R81ubzhbaZrRQhGguW3JRE2aF0U1nhH4ikcHUhhzFLp9koTrsXb1cZSRf08FXfNa5UtvlKGGy-hdXk0KUZkDs4DLwMnJZPg7s5KKrK2uSc5CDdo37FzlZua0y910axqBey_IhHfSUvs-wkCzFucOX-PlFkcSOHwD0Q3q3GNh_HnKaSBe-JLhoAO8mOjzeCWsvap1k1973uGhi0-pJUdrNu_QrqtSmqeknWSZqiz-axGOcUi_TCnlLRHaw5Hau1ntEbryVuPyxDCCTd6F3XgldLR32mLL9jtg2tUWiwMp3ESeT69CuIEH6zKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=eb0AYHz_NX7Jr9BWiXG2bgW_JOaFx8R81ubzhbaZrRQhGguW3JRE2aF0U1nhH4ikcHUhhzFLp9koTrsXb1cZSRf08FXfNa5UtvlKGGy-hdXk0KUZkDs4DLwMnJZPg7s5KKrK2uSc5CDdo37FzlZua0y910axqBey_IhHfSUvs-wkCzFucOX-PlFkcSOHwD0Q3q3GNh_HnKaSBe-JLhoAO8mOjzeCWsvap1k1973uGhi0-pJUdrNu_QrqtSmqeknWSZqiz-axGOcUi_TCnlLRHaw5Hau1ntEbryVuPyxDCCTd6F3XgldLR32mLL9jtg2tUWiwMp3ESeT69CuIEH6zKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vydW70gu7kGl8UBYLTMLyd19ic7wTsd_mmZIBWS_YAvgIJ23qWQVO_9Jtrcp9I9jeHEP8Ci3cFlSASUxr_IPZIuOpaX6z4N11QnKBKJWmPKibZ0WLo4pfFxJRZdcjJAwonSoKSWdPtgXCcnNeuj4_8cvzXMNpmL1gJ6jFoFCttabWXGO6rma_poiyJIViUPsCr1mde18N1jTViUUD3ycnwh3qarSQKHO3AMIvh-PlOQ7o-kf6rlYFfbwZ5_8JNVPS6nz35sHEexcT9Gz0KtgT4665kpZeLpARCMpyToQNtxgufXT8dN7zuSSyY3yEpspCAAWkOYgBJfOULxZ7Z2kvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=T3kNccb1F_UyzZTueKqF6zXAaCjUeDClrFeGqHlnR3mofysc0l3bi0rnafKWZ9rk8BMtQu-5aWv46aGOBKQTbR0a8TX13xzJteMART62POLweigU4tu6XXPGCyW3068V2oFXoM4Or7Pak3C8N4ghrPCv5HsLT2Z8Jw976HfIytO2Lc7Aky8WF3Xgvg9C5E49omF7Xleu0Q8-oYWWS-4ICsNTLo48UZ7XOTGeO0fGMgwJ5ZR_d3CbDwc-dMFhje-uv-ffqj8Juaihe_U8rO6D78hD-JAncbCVQGWMaT-N-i0hI1t7IwlJ141fVXcWQ1bl6b9Sn_c2snqpen9t1E_vbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=T3kNccb1F_UyzZTueKqF6zXAaCjUeDClrFeGqHlnR3mofysc0l3bi0rnafKWZ9rk8BMtQu-5aWv46aGOBKQTbR0a8TX13xzJteMART62POLweigU4tu6XXPGCyW3068V2oFXoM4Or7Pak3C8N4ghrPCv5HsLT2Z8Jw976HfIytO2Lc7Aky8WF3Xgvg9C5E49omF7Xleu0Q8-oYWWS-4ICsNTLo48UZ7XOTGeO0fGMgwJ5ZR_d3CbDwc-dMFhje-uv-ffqj8Juaihe_U8rO6D78hD-JAncbCVQGWMaT-N-i0hI1t7IwlJ141fVXcWQ1bl6b9Sn_c2snqpen9t1E_vbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRK7ftY_67nr6KoqnJbglb-bRrKSlI_v1GFRfnm9r1cMtfs2gYd-WxjEr7v29xsSZgNqpytPnYnvNcFEdnG0D_AwwRcHBIt8hrUd28-eJ9kECWt9F4juHQzzEXjZIFBPgnuywUuuW-IEqvGHKDRAblxaVLmvGO4C0k_7Cee7W_vM-c_Ho4NfOBRD0rUHa_s8uirge162Z93-3-1ai-miy6hLdineM_ZI3Icwd7aXESav3dpoKW2oMCuWNM0uxU3wUv4DL67BtX_STD1rGk8wNoyN00vHODS6Bw22ez0ivrc7EvAudksa4ju-Olbeo0-8IQSD93glGxTnWC4GkD499A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGd2vhh8m3V-ToS2IXq_5mVWFHejknlAZwbUxZlBWZ1Z3SRNbGJVUE_XcXenXTx0uQdtRFE6SvZwSE9gb2Wy_vf2yKy6WrQyMXGn455E8v92p-jn8BtxAp2It_HDHukpXouabGUbncS0feRWm-4z5YTsGded7rq4durnw8SUpyKDxa9sERJshCeJbySkfSK0TZqomKb5s3fh2bfitBvttKU_0S1QKzZ7Zm7MR1nKK3w6KoAVD6mAENLJqaDG3NgWAdkcFMRdDKosL5d73XSJ8rfH-BCumTA-UsHPwScxJtoBo0NsZGfqptRR3r59VkvG-RQSB76ZgMlAiqLNnh8f4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=mWIBkTEmKVlKpJWUeBEM9A90m16SshfGXBAAOytglP_NIRCZnZ_tfEsmorbKbctLuPh_hKmdZ4rcx0Kde8oDoTV9JubkIetv-ux4yaIecBwHtjaQ77VS2o1KieiVjDj_xkxhulkzgH2ynXjR6_0mWk2DBKhpXDjU9CbvsXiyeQIxCo9j3t3KJ-2jCz93gvKEoMXKy8RbzDGJNuUzbvzojrxnP4LDe8vx28Aa6-ZATydS6XEQv1Z4PNxNpHqW66vcocKjOG9Ellkadh8tcPo44Bpz7JqNBgIiuU7YBYqayjfz1ea79FdwHXfHipqgLkPbn3TnNXVSnHVot4BnCeuY2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=mWIBkTEmKVlKpJWUeBEM9A90m16SshfGXBAAOytglP_NIRCZnZ_tfEsmorbKbctLuPh_hKmdZ4rcx0Kde8oDoTV9JubkIetv-ux4yaIecBwHtjaQ77VS2o1KieiVjDj_xkxhulkzgH2ynXjR6_0mWk2DBKhpXDjU9CbvsXiyeQIxCo9j3t3KJ-2jCz93gvKEoMXKy8RbzDGJNuUzbvzojrxnP4LDe8vx28Aa6-ZATydS6XEQv1Z4PNxNpHqW66vcocKjOG9Ellkadh8tcPo44Bpz7JqNBgIiuU7YBYqayjfz1ea79FdwHXfHipqgLkPbn3TnNXVSnHVot4BnCeuY2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOwb8uflAwAkYrO7HiAFNYxsuUIEab_Sznu_2KJQTNk2i1nCXiJfOYGaVfNAiMza4TuDLvElun4kpsFK97VQDmcJsC9nL8URXwEucTT9GPwVacxyUPh6Y1ctC8zgVP6fB16zg0zY8jPTE4-vG4d0BN_GBLWYcL5HadBDSjfAVQ8T4j2YY1gT7isftgmKP2VLpQFGyzL3tF-69ZXQ2t7uSrXm9QlmEgb6nRsaKkXgfqNvU9rvzCd59WmLU3v3GJb8y-XWB4eCPwpFBbGRqKCF_mwSqLvC_mozFh0FGbLGJtiwd21mEp5lbGwb_35Kpqwvwu0db28cjjMnNgZ-TObTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVbpgwTa1Gz6UJFE40dh6X2rUkQ12IJybyhYam0oI8Zccv73OQT-GVDpHHm92BdHdro_lAbVRL2UqiOHDpqF8vPCEvBXRVUF6Uqv651cWrRSYzq9Wr2TzmdJqUI11lI6d1QHR4rIpGUS51SdVn-8-Yd5ysVZY8Wb0kprOB9RFWyc_8zawYqK8t481tVlNf-u0t1fJLXx5lO94-RyXNkEGMed8ZQTcmlzunT92gwYrjnyn30JGElVgte4TFoXWvfV2lUA3dXzLlHiBV_Gd2JmUSwPbJE0dcOMQav6k8Qwg12wm8D4fpQR-ebbPwi6w5tV7VUzd6W3Pk3wlHBdz_QQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPdYTU5q46Yf2FK0NTeK7kLVoF4MKKgugTcvyEbOZL28CvWo0unpzrCHz1PFyyzLPNlS8AvSqHrsUWeR58nzZgmO0Go8Yhm2TknluiU3d400LgiYpyWtgupP-7bpfYGexlF5CBUqWFmniz1or-0ktrL-HEso-phUGnZJE8dRaiEvod14JLHwirP5rR8K93Rs0YmNyTyR1NdKyD464owNa8NWV7YiNL_KHpsx68hx5KXvMtkaQlGnfWfsQH8bUIIfi9T-fmBz6UYVRaFR6m5rLiPOel687sQmgZrRlNsXXcDyAwglMQ5m41dAYm0rUQZJrg7Ide4LuQ0ARcU7Uv15rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWk7DJHgp1If4c-AT6pxle0z-_RjQIDHAhQLThHfGJZqm-2ZJaj0d0ZdboEyjSX5dg4s3uAZOkX4qR5nzTMIK9cayxMAtB8dg01MzCB5vwuwsJWJj-qaUifHQJ3HHHKmoUzuz3k2vdG6ukJl6nh0ToJdIe5fH3R_FsNHTP3dMY0e1pRKl0upTrY0uVpBJ5W5ZfTRSgULW8py-vMv55fJ7nRXU-12EWidkjzUw-6bpT90EtCSRFODmar8CWSJYEVCwUmEd2cLwmiy2nx5YAI9AnlAbeCMBAcF5PROlJQhrInGsendIGARl4nVs4LZF8VOmtxsFeCnDM0xM2u67WdURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_A4piOe5HFjV4XwUmOb7fkwOblZXVbejwYGveQ1v0GdPrk15ZAv57WmeuGaNkkGt3jattt2hEsEVukDRpJyNK1niKT-K6R8EoTrXcLonoCyzx2hATAs-g_QS8cxy80hRnugmz-_9306FZ_EFPRuOg7_rn6L-HYI1c5ouuzP7jc3lDeNhmMtbofCqD_ShGIHIFFDNWflwdybBb4fCA9yOzwSNOaDnqg5HBKyjWfIwMYNWYEGLq8zJWZiTiQ4DDihiMV7l1ert6gaaCagXvCGt46qQlT-Rnh71E3ccCifSSVapgmh6rEtqDRQrTi5c_WzgaIafKatdp9yju9seUegoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=aFuW7GEDpGgU--LHGZcoYHp9bO5YOPcBlqVyILewiF0o5UqEPbKLaMjXFQFM0iqGDZp6BqivA15EWrp-lF8ybDcIgzmI7hN2Db_nwa-YNoSSU3g0tblS2Sik1bcxnBpa0sZUdskjJ2Shyy2w4cGrFPl7cjEZbuoa7GCeQh50FFsuUfKvTMuOyFlF9KAk3Qxxhg0oH8mEwKDk_PEBxvBS5X27tHlUO-Z_9AH31yt2XkVoThNKp2SeWf9_mkg-1Yk3nNDl7JKBcLaMwvsolLMVfqZqHTHIxmxxTYjEgwREr2pXJ7Dw0FFN5j8-3WmsAXCptbhPV8Imdl9jXCOikZxt-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=aFuW7GEDpGgU--LHGZcoYHp9bO5YOPcBlqVyILewiF0o5UqEPbKLaMjXFQFM0iqGDZp6BqivA15EWrp-lF8ybDcIgzmI7hN2Db_nwa-YNoSSU3g0tblS2Sik1bcxnBpa0sZUdskjJ2Shyy2w4cGrFPl7cjEZbuoa7GCeQh50FFsuUfKvTMuOyFlF9KAk3Qxxhg0oH8mEwKDk_PEBxvBS5X27tHlUO-Z_9AH31yt2XkVoThNKp2SeWf9_mkg-1Yk3nNDl7JKBcLaMwvsolLMVfqZqHTHIxmxxTYjEgwREr2pXJ7Dw0FFN5j8-3WmsAXCptbhPV8Imdl9jXCOikZxt-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=qPY7XO1mxjIC3a6GTxqWh7q0V3_nYtBVsQPFNYyCHwsmjdg4t8kSGe6WCWisvnH2WJFZhAXATgtO9ptIYB3mz9g_Z-sHQTTlD_j9vaLWyUo5ePgrWE7gjhScAsRpZRxKT9JrU9o44T0F7jI1mujPHv3qpZ8_ZdjpybdEikKILoUbjJC5GEvAoHjsqBHFjfr0hYQHzV2YFClPMkUH3Wdloqrgn2_Vd2wcmQXXRatPk1y0ejgp7Uk8JjzfH7xnu5U5FiirKC7M0Em24OxrzJAYyk_yPXOZweyX4QmVBxy-DsZHm-hB6_CH1RWwNKSdZ1lyLU2OAVACFAtsZbdGbcKt5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=qPY7XO1mxjIC3a6GTxqWh7q0V3_nYtBVsQPFNYyCHwsmjdg4t8kSGe6WCWisvnH2WJFZhAXATgtO9ptIYB3mz9g_Z-sHQTTlD_j9vaLWyUo5ePgrWE7gjhScAsRpZRxKT9JrU9o44T0F7jI1mujPHv3qpZ8_ZdjpybdEikKILoUbjJC5GEvAoHjsqBHFjfr0hYQHzV2YFClPMkUH3Wdloqrgn2_Vd2wcmQXXRatPk1y0ejgp7Uk8JjzfH7xnu5U5FiirKC7M0Em24OxrzJAYyk_yPXOZweyX4QmVBxy-DsZHm-hB6_CH1RWwNKSdZ1lyLU2OAVACFAtsZbdGbcKt5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=mNzMsyYz1Cgr7Yc5P-lbrrXAE5GBidcIXOyBqDzL--7uaXK_sL6Ce4GMn92xK4Q3p9Edq0-0SYZYpJRd1tqp2xiZtj5NDMCTaQanr_1yXayOrQq9f3VB1h5Z8FLqa94rg9QZgNb8rGEoYR2qUcMYx7FckSgmc3PBQF02ixEqf4zXziGYE-bXSlwXtj4aGkz_Mb1PeaDy51TWNwBjql6Vi3fj3uyQQEy2bxhIHmEi_nQVfp7wGk0KHG0O5dka3EjMJoOHQ_0EVNAn7zTJPtQD4EIf4RHuaKNKkFAnayjIJPaMs8rxUGFEzQsGpoGXfT8Yk23bSL-O9R9jp0eubS_I_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=mNzMsyYz1Cgr7Yc5P-lbrrXAE5GBidcIXOyBqDzL--7uaXK_sL6Ce4GMn92xK4Q3p9Edq0-0SYZYpJRd1tqp2xiZtj5NDMCTaQanr_1yXayOrQq9f3VB1h5Z8FLqa94rg9QZgNb8rGEoYR2qUcMYx7FckSgmc3PBQF02ixEqf4zXziGYE-bXSlwXtj4aGkz_Mb1PeaDy51TWNwBjql6Vi3fj3uyQQEy2bxhIHmEi_nQVfp7wGk0KHG0O5dka3EjMJoOHQ_0EVNAn7zTJPtQD4EIf4RHuaKNKkFAnayjIJPaMs8rxUGFEzQsGpoGXfT8Yk23bSL-O9R9jp0eubS_I_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=TPBU05SAijV27WHWnfsly-aqiEw5i0fCjfXXgVQy4U-UCHVbd7Z6WyOKH2VTmU6XbUfQOAWQ9_BYBPWr_zOVJhwbuDr3qjf8WSd8yvGE5nz3AofVKGJ7qOMVKRu1EwiY2baR19uQUPOa5q7I6mxDC0w6nINRwnA17vgUF0iYyyRQHQwuYITa1D72PQPZbFmZ8dDbtGk4Hlip0RdrFyUKiEQbMekdH5ewlgyjGL6LD5IYdI0utmjw7DLTr6AYy11Oup9BtXkqsUcP66xnqa3ATvDFpqFEZKrJEVGDDR7kt-L3TQieisZjR_6NqIzPVWsMNpmVXi_TOZxSHCHh8AteeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=TPBU05SAijV27WHWnfsly-aqiEw5i0fCjfXXgVQy4U-UCHVbd7Z6WyOKH2VTmU6XbUfQOAWQ9_BYBPWr_zOVJhwbuDr3qjf8WSd8yvGE5nz3AofVKGJ7qOMVKRu1EwiY2baR19uQUPOa5q7I6mxDC0w6nINRwnA17vgUF0iYyyRQHQwuYITa1D72PQPZbFmZ8dDbtGk4Hlip0RdrFyUKiEQbMekdH5ewlgyjGL6LD5IYdI0utmjw7DLTr6AYy11Oup9BtXkqsUcP66xnqa3ATvDFpqFEZKrJEVGDDR7kt-L3TQieisZjR_6NqIzPVWsMNpmVXi_TOZxSHCHh8AteeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcaBCeaCWysvo1tGxrwZMYQh6I8zQc8jgmcUSIDKfWT0pyE3V8SyTC4n-8ylXikT_DWwt9RUQwK6PEAiyUPImwDtUCm7sOWIhMMJAqwZ48lsQmwPxstuhFBDHjguVCIKfSYWoFc7n-3ayY0vfOwUYIhcxdpdhRpwRWxNPfcapB__zzqCdBc-ibidmqf_k2jUCzSFfx3TXhJ_9dmY_IILY7vWPp_0S3cMm3p8ae4P0NGGBlA4tcLzV5DloosQHYOaw0nlKE3kSefc2MzFSM4TS-41yqACfidUHDmTbnuChKmZjKDRW9WJj6XMpHVEqdo9lEzIupTG8PtNO92t67oJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyxxGGJH0LTnBpYrtE7xfDkHxDSmP8E_HFgJYJV8f8zpXI8yJcm_dL8210xPPGMCK6FDHJa2zAbz9WjyhcUeKuQHnIpQnmUu9Ethz3R29W1ZfKNFqFrlucFS_aTX6TS-tT9ekf30khoqX9Uf8dRIcLUst1nJedCOFQoaVg6pMIs5cpttI4-D6kudYRK2tk361qF2LyFW3s7DqjXNXzv6WeeKdAPjwvtoUkB-02TaZ4IinXl8e1dU5WDCCd70Jo8gLUxprifQB3RQeHilzLsmvo-Dba8endP74ex6RWN5_k16rK2Cf4rlRyRPitnxnbg08GyYyZHclqh-ac2nCjuYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=aO3eLk_mWM8fAEL47pqoKwZofyCAK87u9QjBHQn9h250Ng_qyMTjPF54QGNKgQre2Fht4AsoaUulJIaYwW2uSVA45AJuzvR7AoLDIfVT_WBYQlvoF_AyQ47WXEIUj17-ifmcjI9tYCpo4zO9fUMVeKOnQwFtgt9e8mbXEr1amsfPt7-shzla8RMBx4J2hv2YZX6vjX7Bm2m8wDnGReTS2VoS23Yb7d37OVxMJFZnSS51ZjPlsSNqGNptPYLpc0HUcUgBmg3YhWX_xBXzXY3293FqS-xp0qyx3aLTJWcS0-1ZnoJocfbpdvcZypx7jVlnXatkXkbMM6osSrS1hPx3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=aO3eLk_mWM8fAEL47pqoKwZofyCAK87u9QjBHQn9h250Ng_qyMTjPF54QGNKgQre2Fht4AsoaUulJIaYwW2uSVA45AJuzvR7AoLDIfVT_WBYQlvoF_AyQ47WXEIUj17-ifmcjI9tYCpo4zO9fUMVeKOnQwFtgt9e8mbXEr1amsfPt7-shzla8RMBx4J2hv2YZX6vjX7Bm2m8wDnGReTS2VoS23Yb7d37OVxMJFZnSS51ZjPlsSNqGNptPYLpc0HUcUgBmg3YhWX_xBXzXY3293FqS-xp0qyx3aLTJWcS0-1ZnoJocfbpdvcZypx7jVlnXatkXkbMM6osSrS1hPx3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaiE86inScsVf7p6EvgelVsqfHaS1qGsQW9mSmosTFplm_x-CBfSIYlKklzIIGoNCt0BAgDREgq2Av5ZxrivXi573ZNL9nPFSmw54JobMpioGEa3E7tK912pp9GcRXRtRA2gSMNNyPceb9tSTBb6BLf823ZdkXH17xwhpgI2gjWs3hG8YktTktk5z91li41Ji2Sfw2Fz44s5zKE_ZT6zXFNbyM416jVbrnopmrqWhKa9824wS6pYNqIjNxXS-RCqD7KlNjEHrH9IHLEO-6cbJ3tn5RHtKNbTnMV8mx_qRtoCsvBTnarlx5U03uDYtOtB15lIqIHEApC0-kfnoRPz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=O4qYGMpbT_ERXZlM2YFu0mIJFxSlE07MBm4UC4HUx70kLtjERLVXnSjbHhufjNMGZLP9pp31hn78mckjAYVWGUDj0PP2HGA5ODzEI8CHMiBJN0UNrq2t-CVtuBnBO5YsZ6_YjeOSdxuJK0TmZnDX2D9AWffd3FFEPrXhgL0T7qI2Rekr6cCVHHudbtQNQz2bH2_5SQr-zjAn0oEDym7RmFAJhqIBP9nNXqO2ZBl8DpZqnp5DqY5jEg9JZyuka1CGRFUHAZAVlvgNgx6fY3Vfxkc-ki533tKACuiT6b03GghXr3zaIsw2X7PZnEq2v1bWiFbn0sxrt6efz-B05yX7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=O4qYGMpbT_ERXZlM2YFu0mIJFxSlE07MBm4UC4HUx70kLtjERLVXnSjbHhufjNMGZLP9pp31hn78mckjAYVWGUDj0PP2HGA5ODzEI8CHMiBJN0UNrq2t-CVtuBnBO5YsZ6_YjeOSdxuJK0TmZnDX2D9AWffd3FFEPrXhgL0T7qI2Rekr6cCVHHudbtQNQz2bH2_5SQr-zjAn0oEDym7RmFAJhqIBP9nNXqO2ZBl8DpZqnp5DqY5jEg9JZyuka1CGRFUHAZAVlvgNgx6fY3Vfxkc-ki533tKACuiT6b03GghXr3zaIsw2X7PZnEq2v1bWiFbn0sxrt6efz-B05yX7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGYOkHr-BMVAKJSrt_VqPnffGSbvEnszBQ7N_gEWcSKugHP-ml5iURZuCg2aNDqhFUfDdrLwQPJ1Czm0JnOufEBJYqfI7pkAEb7i6P0vLsnE6wUzCxEC1kIdrW-6Nl6tsDh7fVrFVvcrqG0TgdOAcA8iOKbJoh8eyaaOm8c6k0mBrZTozbnna8u9TyHiO2yJAk3KBl2l3gh75uT6AK9gZZWeeesqUeJaAvzrP8cTrn9mU2_Z4yHF6rpGMW4jF3T2BDlxoJV1VL7nwqMPTTsmvQhwQgXlWzybpC0_fNwOqlI0pqrXa7rCKTuWZEvuUu8qVdV0G139ib3WW8IhPqI2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDYqEdNWRmkTmY2mITPWrcoJDKR0u-HaR9jwWroZKHeF98sIuh7-3MLicFehgSwt6cTHQ6pVUNKSE3bV6HBgVRjT0SJe4Nt7ZHXvCaP_bAMys-jkzO2_3m7Uo3TzFoZTBxy2tO8sTrK3uxW5I3k701rAzshne2QRnQ_RieYkbV0TtzH0_Oy5yDQ_DkmPZiGAoz0Km8P96A6g9OtlUAKHb3eDfQmDF1BNJd5FEeFVReDs6tal1R-m8kl5z07C0vP1jWqFrM_KPBXfuqXMEMcUlyWrMb2fI2bofLSMtfk5WEay7y12QYIhQRj8aS7x1BDmB9XoMYSvIEOXRn27_m9kcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=lnJ5j5PbDNctkHZf7O0jm1xDHKcy4RAPJKgptm68mITg7Q2Xff5-Cg2NPfGD906F9rwQCU1VDuD9q-lcIGKdWG2CQLYJT6d7eYYdfFxXaj4jOk02jPQIf0tfuXB67kDRgdXkDALZF7BNhY2ZCGhudkenOXNR-wUfR93YMMLUm15hHknFQErbm5A8fS0vbnHS-t5-x_m7EKsewBguDlVr90PHSLF7kObSbNNai2gcWnO4EbX9lHfqYSnjMf2LiPkkTumEBId3koq3eQaRnA_Fpxbu-eDlTpMgSig_gSy-5qMSXHRnB4GARccZcDNKjMCAVTsfqZZZAsZVAhrCDwKisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=lnJ5j5PbDNctkHZf7O0jm1xDHKcy4RAPJKgptm68mITg7Q2Xff5-Cg2NPfGD906F9rwQCU1VDuD9q-lcIGKdWG2CQLYJT6d7eYYdfFxXaj4jOk02jPQIf0tfuXB67kDRgdXkDALZF7BNhY2ZCGhudkenOXNR-wUfR93YMMLUm15hHknFQErbm5A8fS0vbnHS-t5-x_m7EKsewBguDlVr90PHSLF7kObSbNNai2gcWnO4EbX9lHfqYSnjMf2LiPkkTumEBId3koq3eQaRnA_Fpxbu-eDlTpMgSig_gSy-5qMSXHRnB4GARccZcDNKjMCAVTsfqZZZAsZVAhrCDwKisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=Olq6XG5oMlHqu2IKQFl18yfiwvH2zTOA8vqRf57vn7LvdvbP_jTSWT2mOmMgo5fC0yoRueVpnKxtA3OO3SuGMUnOGqlVOIq8quBxvOooR0mKhbqN5D3Yn438MS0zRS8ALh-bIZIN8oZ8dC63KBacYf7sHs5Stiw_Q5w1cTfCTIM8mVmivG7b_tWBJLQxVIBsF0X--LAlmOij5WbjMt0m7O0E6eSihcgtz31NHdMT42OghYCA3BaYG1HNtC_gRp_qg8il0FTVvToJorUM1lDfp2KW3s7CYYU6Buf2lEi4J8B2S3f3sUmPUKvQShmHrUXEHhNIUTIdEfMNL502W7Uszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=Olq6XG5oMlHqu2IKQFl18yfiwvH2zTOA8vqRf57vn7LvdvbP_jTSWT2mOmMgo5fC0yoRueVpnKxtA3OO3SuGMUnOGqlVOIq8quBxvOooR0mKhbqN5D3Yn438MS0zRS8ALh-bIZIN8oZ8dC63KBacYf7sHs5Stiw_Q5w1cTfCTIM8mVmivG7b_tWBJLQxVIBsF0X--LAlmOij5WbjMt0m7O0E6eSihcgtz31NHdMT42OghYCA3BaYG1HNtC_gRp_qg8il0FTVvToJorUM1lDfp2KW3s7CYYU6Buf2lEi4J8B2S3f3sUmPUKvQShmHrUXEHhNIUTIdEfMNL502W7Uszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEwXGuspPrDmqZ3paDgroBG7OH3ZaRzKJjVlyOGIhVIKZt-GIIZ5n7HhY940LZIarj8xVqK0ZRI1iDiiQw0f5HRE-3yInVfo-b3ZCCPNzrVN7xa5L4KCrMs7cE-G3xBLXWg8Mp9eGxJ-ElJWOCEd7TVCVwk29lZEnDhS5mMmr-3di2JY3zpijyzqOhstb6QE1no0JNVO2s2_tX4UrYqTq5agnayF4b3gGhLMQPDKzQXLqn-BxKVDb2HlhBVm6F6eGFEKXYqpdj5XAOylh0eHdmVQ3CxeXEklkaaLt7n5zjrSIJx0pf-t6aunrMXl9hzZRcZCZEVTFTWxn9SrRQyFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEn4oZ5haW-WeFs0dIYWJTniNGenoDf_kVakMOWyTXNJIdW9dGYEWRcQ9A1e4xtaZ6zDieQcWGmJiqSmr-zKVik-j99qc0D_EUBVVNhs8_b9ZvhTsO4Q_sQaeAMjHICE1oNrGOF07nx0Wa-nEvxwsE6zrbJlGVkj8H-OLDw4AGXrb-jGSsJ3l1APzuQY58S6WNNKLubfdloTlJBX6vSVJKv7MXRQqqHsNMLCkT0VTr4wm0DItF9hvW4L7KEb1BPE5cy4uVyEV3PE0nG4Ih_TujyeoShiztboBXrFlJt2EpwhYKc5h0WZHsh5tMeupx3j7NYSbn1wtJAVVcABDeyrHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8KzFnNnxZQcBpLN1-MRP3YrN5Vwi3oWwF1YfsXMmENtvGREEKdND2w8jGKwts3kMmVSePskSnUQJy5FS8dTHK886AN3rv5FrMXTo-ZCgtUcAJHxf3U1pyq_fEeM251ZJxKjUcKL-JPx2PV4D-As7SGLQ6yH4o_gC4ZCMeaw2KH69bJWoHbzc76MwE7l2SvFi6b6q6hOaXr2RD1kww_zcrsKR6F7lIU1RTyl5bIB0CQbZ5x0PzpORK2eW5G_UCVQaqFBOYy_mVQ8BEYOxQCB0haWxi-D9rQePKS4PAoeyGyXT5n7ityuQIwjpcGVlT5IWa2iD6pw18hU_Gwi4CRIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=GZd9DuOiK9kQmowAn4FXkk67XZKoP6KaYN1zbZHV16z9zz0UX0YkVWYwz5l7dro7GJVcATsjpEssI8eNeSqh3joOyE4K0UWKVrsv65vblCYHuZP0vbhbR_t3DXT2bGGIhlEXnwN31vHPxE00VdaaIVNMOnD3q-5x0phSLcRLnlHLqHkQCNzRgPoamHqyyIssFhfG9bjzJu-5aWCtM3yFol2SiqOwYENb0HhuRTj1ELW6I_iJkqk629aRFbwDiGy9nfQjnom2yEBmxEWIuNlJxUYnMlTmN5-sbXYaIdoxf4M0SDUnElP3NozJ0_aW5spnhwJKHiSTa7nAyywV1I02dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=GZd9DuOiK9kQmowAn4FXkk67XZKoP6KaYN1zbZHV16z9zz0UX0YkVWYwz5l7dro7GJVcATsjpEssI8eNeSqh3joOyE4K0UWKVrsv65vblCYHuZP0vbhbR_t3DXT2bGGIhlEXnwN31vHPxE00VdaaIVNMOnD3q-5x0phSLcRLnlHLqHkQCNzRgPoamHqyyIssFhfG9bjzJu-5aWCtM3yFol2SiqOwYENb0HhuRTj1ELW6I_iJkqk629aRFbwDiGy9nfQjnom2yEBmxEWIuNlJxUYnMlTmN5-sbXYaIdoxf4M0SDUnElP3NozJ0_aW5spnhwJKHiSTa7nAyywV1I02dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqDF3BmM_Zxv4n9yi5iEK-XSOKUqUGkf_115JvZpfuddL37CLXSvbgGSANwsr6tOSxDdzCq6YNYls_GXnQs-vWUWqX7fc-3dMzi0E2zP1fdZWd1RKsOOcsxbiewJkcju-qlnFe_5N1KjRnxxLiE0TY-klELETqeaQcPxBR7gLBg9bsHkWaUnbzN1Fu51CKpbOQy-E_Jou8wjAjyOToQ9lDnK6ey07cjvYBNC8u8A3tanKJyxC-KBJd4GnJQjihunimEvq6HJjn4Q_dA38mvbe6mHDEXbBKzUdvT3aSCeDcxlWM9kV6TSqVyxt_Otk7DKgupLO7hJyvgD3uaAlyuCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
