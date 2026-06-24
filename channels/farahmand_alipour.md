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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 20:55:17</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-cqyRh_cCZkHhGS97QlBz2tGbpbRBqyJ8glo0FWImVX8Q4F91UZL5prrRymYW4VvzT6Kly_dDPfvg3ilax0KEo6xsPly5LNkIULqpLddIyZmFcSGP-lhx0wqjzkoyz81aeCYdjoXF7h7ZFJZ7eWZhRDqN7--QRWx08FuuGQj6QDHPXXziFcsFm2XQ9h3rwLc0dVnAHVjrzJdBHaH6TKtXyf5_f5B6JPw3HQcEy3UzdVgF46q3iN7UrCgkFgsP3uAOPrsB2QQcFITU8j_INMUBtLPMOYFwBa-D3N9NtJIBgjVWragIDIxzKLi_SGp8OAnf__ZD90DO1Da1ZPmq3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBZn9xG00ukVt-Zwp-SzpyrLM5t6WksgFugTcqmyzQXHQ9-1r-WjXLXhV3V9fcnRnYjLHY2RT7l4gW3SRTePhzDz9XudcS9L4csiBN3D6taPQvYXpTcYXVHh-f_hyzWunEDkBwIX7ZoQ9ooSFnueERu0Eu9-foE7oZ2_PvNGB43MavM80WV8GoBDqfWNK0ljZSrwF8K1kD0USDwVKH8pSMLnAjN-WNEwj3alHWfbf09-3kqYbfE-JpAu8JsDA_YC_j-Z4F8Fs5eszZkoO8HIuLMnF2tqgCN3R_J93U-YuOUuSCbyKUECz3u5CIN7g10jBP9OUE_ymbTPgnb9ZxaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlnDV4DAQd3YiFu5RxwSarHQtL8R1vcVP8SxsmWW5GPwgWzhSPkzJEgYOv9E9L6FIXEPk4kpf8-mIJHbj4Kib3crAL6Dgf7Aod6DQJUzhztDDS_bQRMgqntHpL3oqINjquVf1xCyR9gNDBZBViu7KmI7SpLGck1TEFm_EiF1IR_TtNIVMfzncvBbis9aAEiiujqRnypl3fId9zXOyq2OUYwW7T0P9FcoE9I0skl5n4k-M3qFXk6cRES4RtaNydYUjpH2WAxjuzM-PFyFuzR4DEf7EccLUHkq_ghmIumEjZ_5TXMsXZbmT6B5KlDmdR9KnkDxfKoDF39dhkVTapmMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCKB7WGjbhXuaOBPtnACG118IvVSeDBXAolDpRjZh427Xw0VbrxjTVU7eGVbMQiTLyFVM5outkQuH6dTntn67oFAzsk04uLA0MeTKZxoGgsskz4C722yOC2m-5FTmugGYXtLIK7rCRj1e5wtKqPdMkSGPXvi3v8R-WoMMK9ttiS4QUJf7jrwQUQgbL1ODqaVesDPvyxC23i5EMkK3s3r8OS7cB96Uf4mxq8gNJ8FWeaL9EqZRrTvWTUdQ-HZFFj4_xJLtOalNQOyw_sY43WN_6Y_K1HeImGUgY3V9hCaLDOpDHvUufrj8BonpLKtKWNgxZ9hroQW5Vkh16JhuMG5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJchDAatLgzzocraEr4GhmTqFR1hzHq-tqvZEgqysL_l-ryKkdvmGCbQ_jjvYg6rLGbJ-w551rF3z92Pd4LEP6J5J2fvWFM_zb0yobf74FEJpFFLQDeFcJPDHuPpAMl6ahhY4seR5UyJAVn8T-aQyBK9SEQlv7LX3_QXVr4yxcg-1MnuFSfQkl183j2np7VzSeSLUreY41RDdAblYtYaU8nYZfwOjoVRgoSRwn10rFvRwWLwCkYcyHK7zRangiBTdMpDN9SoF2wVSIL01O4-ahp2Ok9UBviEGf78L-DZ8wzcrcAT0qKvDCP3bY920yhb3xUKcEP9XdLt68BzCREB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTzYhuv3qCnFrAYrohfnRmrkI_GuhyYv5wAo8yFRjWIXeslPEhJ8VRphPoRViGXAnmMPMMP33bGL8xf2MSBfV5l1o7Ri1xPn1774_WNqyYj9Y4r9INam41eoxUksuLt-xa9pxX1dfz8GX9aMPMbQcTgOCRAovsumrKjHNwjLKeqAll6llSoQFN7yGipOEPRAfquxu99HzXGasSd_UB2CHwrmhBMhZq0LquMAtMwrpfvJcuoOy-JAyherBPmPCFB-ochAGaFxKfHKuAs6be-ICGZRvt6PhpmlgigxcP3n1WIFZWh5zQDv2NpM0QuyaAj4zlkcKyTKd0QKIyCovJNvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqqjVy40McybRWo99TVR7ExDiS7iiPIpVhzO1pzRqpPgrKe-ofiZtx3Sig7wAgjOK96jnVIcYuBQ6BOHENT17znKb4rv2Ilyvc2GoU57OOJa-yfaHTXbgWYCgrdZFIimIzMwJwjzG33fHK21e6otuUajkaEdKdTgzHiZ-R0GlLVTdPY0MrJq7Odtbqw4PjnIf4KFP_BxPKVMX1P_dENU5ktLjZaT6c0Gicr6cEGTsV9BqNnrDM-ZWjm3BvDTUs_ONwmis7BOOSYYPpQBAHKbo_lEjjs8BbZve_rn9Ts8ou8w207RLrJWjvhKask2LbnjW7fLDst4JaeYgh6cx6NKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_R_YRsyMrs12jxk8kITv7wj-7ODSZu2wMhxuF-PsPdHbH_6I80z_VzIU5F0DMnQzeVkHKksYkcM9nH2mOLGNOSZl8sz8yFCs1tT5Mqb6wHLUGZtfgSXfTMbWGxQonFOUJshL_omTbDLK5Ox5UouH5UpaRufwVE2R0yxnt52EJmaLeEtyRPJrXWOTRFLHdA6O02M06Mt367iZW1_mtkyXlgTEtoKyckcqhOrjBbtHw3FzCu_OCxvzulzqm--ix7XBWbTabozdAgmEz_f-IPKvkqT6hAepdgSDtXtW7N9e-Gdk7wk1FE_G9xP4QZ355Cxko3RGtbL0QgFX1gAbmUEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3-9tYrYMqULmIeCLZWEgmtQNT2HmdFzf0JUi8u2dw2EA496DBsus1VKjH9EyFDqJwzr1Hr-27gA37uEqI7YB-KaL2AXvvpcY1wp69XkbwDb7urhqgRRHvseyFzx9v4RItmp3nHREoa8gA4XSAHgWMnig__8OeDT_c-I1ArRFcb2U8n-5cXPsGAheixAyLqaWeonuVVreFzNuI_G1DpQ7MjKPOya9ITeA-g5TjquljvCwfFgI8LJzl9rxzsUISl9sBbp47or4Ev4yEPvPJmfjQwwheb1qsIuear-qhUAVHFewctBzrN_DjrwGSV6id-9hzCsN9EqBLSb9AtiCUnc1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfgJzCWDq66HFgaqdh9OVwNeHwqgVQt4pBIdM7ljrHrUSzORKyyPNT7Bt-6PsOhEtsr_61r0cSYyW6NorNavO-oBOpe-h6ZMrHSVnu6I0Yn79C1RJqWY7hl7gQpwbA1qtfKRS7nn4lDJibO2pt_gj3UqfdXf_Sqp1HZEASIwA7LhF6p9LIDRbQY4XFBo5DPhxQoWitaLyOYcxAiZ8Jxg5AZit_nuKQsMabL68h9NN1fpVWotcTt-mD8zPFvO-uGbOCmll4PY99SbMOrseLjqLF4vJ67a8TQ8Fze5ntX9WV1RcrzpftY7IghgA0-U5MyDsmEq8zL8MV2unh4H_LPuDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObgEMBSQ3SY4C4wB4M39-2SHE8J8-AgzHNHMxlcL1KsRsoJe7wWLH9Sii-PXtF25tkZsjG5JuOm8AEhEC0YebhAW-9iHkXyXi8QDzMgock6RoXiYqBTNlKgY2MyF5kAUfj6eUt-DnADYLELHb3KsUaFCYztouVkQns9-l3wO7uOKfL_5FF99vlme02krJQEUL-6BJMqJGp9VM83lwNOHIYkn-J-z7O6JPWIgqPVpcso9ej8vGhPGIpOWKwHvGs01idrlyCnrw3QzoUY2L_2qpXT0f2FFvXyP7ZYho_1Lhi0P0ftERgtx8Y8r1cEbsL61WuUejRy42t_N9mJwwjP_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgy60DIFS2hyVX7AV4Q0rpf7FP0VQp-ZuqvII0FrcbGWmtyuGJ-0_XVubvsaERcjfztLQQ_czcUhb-zlSyfTE5YfwvUUiIILA_LfBhSIXspFGz8E2pgd609L7lSBD0Rilu44d6Q9ITumw4nuYMVmxEedxvtZV0v47iiqLwWt1boUgwcKd43kme-W6LNt_mXG_h2g8TiyZ98bpnT7oo5_zdru02V1XwSPGIyQmYAAvL7LJEqqN0epPiyagfFKhBAc0SQ2wcfYfqAKZcRSazedhJTGhivnVyPoo3Zw35mGo3hlps8HCn3PnG0VlbuLdMzT41_ExNCmF3QLo397CEhCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af40xEAHym6-WluiaF8-N84s0P6RpOWHW5_LL6JJMfuesQ5cha6ONoIAX0ZseDHFykXB2_KcIVsXEdkdy737kihgxYdLUDZhzGdCfyi__ncB8TZche-VSYO9OS5pErcof7w1-GyBqly3AzgsH9YL2gmsdLb5nvPbm4_GDLWwVNY1I920c8bpd8cdZq0_elOZc6mEcbXCfjgbqO3h99dQKR_jzLl8jv8Sft4YsprDkBWYPxRVxrAJmbEcJQk-FkmRi1QmYeMlm66WFUHt89Ipy_MGXG1v7o-6DGG6sNmueSl4s8dVENDDzUu1TluWuEkjk_omPHl_9s-vb1MJnnOyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbbMCHOt6qyCK9rAvhXkL79ekEuXXxXHTEjY6_kqdAwY2vGf_AlWHlCfkCy0GioxeHWJZwqeFat9WNP9vELVpiC3QdwS86SE95YioeAxrPqoq94rfP_BVTNaQC3XeAPuR0SaMAitE0qg434_5T--vFcoR8dArS7MQa7td13OuDs-xB8gBCT-ccuwS_0tPWQ2l5FVQd6zdACX9fcWQ4PFICOH4_dKjSc8FBpBdcCU95djeORsYD7rP9lJgwRGWvrRg2CXeRYcjoqJoL2f3Z81_GlsZLy99sgpnyqHvD5JwXxULuJOJGdCHqC2B3-jZ9pX8o_V0zRPkFXBGW3-CbWdAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQEEMmfedZH2k_n7UoKLKeqT2eTBLh4GYRQkYRL-cQqY0p_ChD4TTFj71R9cUoZr7i6hJSQrGH1OSNC5agAwlGpGaHyhAcJ8CoCSaHMUwe9ipjfvn_CYpNN48DO76rb45Y68Jqsza0KQS7fPih_tYsX08hmW41Xkk6c-n6mOI6BbGaOuT3KOglq4FLxDVGQWQwogkP1iB86X_t5XXygvh1IkKvw8MjtvQ224Lxiwid2UnuZgN3LcQME0mS-bAE7IO8UVcQjU77rmDZl2HrqvTmhlhUSU2KBmxR04Git4dF1wNUHl-ZDuk41PyPa9ytBsSYabyGEuKf6Ko_JshU1PvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbtzPkS9Sqx7f-W9yUQHZWcFxr8luZ7Y2yMMTJor0Mo3SLzxBXLg-sDran_XEB9SWAxTKbfJmGbE5FnZLrT4DHZyVKXt3nbalBx5WNkxSs6u5G1flI5nOZgAetONHZFcDCzHTEy4jQPUCh1b2CI-zqfTanVRVtFyGISeLGLc8pNszrNrtYxDC2y8_qOhcbxRBW7cHWwpA-TnucbXOpicsjQp-pFwjbDavbCj6emKU_baj-7wSXaua_Z31y5E4StqOcr1u0zsNkOw7P93LBoGg4OEAhh-es3sXEX1wdXhRXd2M_KVCouXXW-SSpmtCByfV1mOsIOokVXZtyJbZcfBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg9F7ugYaxiGd4VaKJe1KqV2l6Di8Ru2lhInp5mXFmksHdlyBWKgB1zQ6nGYIkTNKrh8WAOcR4h6jexbzcf_70BVgYgPxslrIO1t9esuKFXhxiBeyQ25KHsHZtPW0OIWHzidvWA27t61HQJPbURgyC_SxStusfImgy-qf9kXpK1kJn4GH_pQ3YrOb6vehkfp5VmJs1gT-4zoGZRq5_24jXQJe4xT7HbtL4oFUlztU1d35Mp5ZQHU1D8Dk7fa27qMgoEAMW0x1CNANahQLhU0GWcskmzCrScqN7ZkW74nJpS3igEH-6ZvJu9fqtY83_XCCX53Lva5bH8igN2i5lBKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=kUDWEneBTdNic-FYw0Lp1YutcUfdyNLAxSClGBho93PQJOPoHOMrtzwVfCkf2_fOwfBauMVXHZaJonZaNsp8DJHkZe34d07QojDWcnb-VS_9q4isl3wI5sTySjXbeDEE4pzAzQxOKX0FirjVoAyX_Gil-kj8D6GWqG6xQ_v_7sqlLi9XySbsgcshCaBWKDOBN1LknRc9hBAXk8OTx9DNcMA791ubcUH_eSbQGaR2OT39uQHcIAKWTY2KQkVIUNrAe5X0u4mTnyq5gUWF7fuZc9vyukIL2X_5tjSYrbRLg-r__xA3xv-r6Zs46kcIWD-C4jSy8KGG4Eh5m0mGs-sr-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=kUDWEneBTdNic-FYw0Lp1YutcUfdyNLAxSClGBho93PQJOPoHOMrtzwVfCkf2_fOwfBauMVXHZaJonZaNsp8DJHkZe34d07QojDWcnb-VS_9q4isl3wI5sTySjXbeDEE4pzAzQxOKX0FirjVoAyX_Gil-kj8D6GWqG6xQ_v_7sqlLi9XySbsgcshCaBWKDOBN1LknRc9hBAXk8OTx9DNcMA791ubcUH_eSbQGaR2OT39uQHcIAKWTY2KQkVIUNrAe5X0u4mTnyq5gUWF7fuZc9vyukIL2X_5tjSYrbRLg-r__xA3xv-r6Zs46kcIWD-C4jSy8KGG4Eh5m0mGs-sr-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNlfBCAfyPTfRhkWEhrzhRL-sSMfdatNQDQZ0hetgiohmBpenG65LgXlqpxfrRx3cAuvDwJdkYbTVCTh9lt2cGrLgemPAy0yc3kSr79dCqk94l1yxZ2ccEVeZ6-X4CeUCheu31K8ys0BDJ9yiowYpu_--Lqk_ycY9OQfiDUVy4oE_BpjYZVRwzW_Ql2aT_Uy8dscKKpsy7d0Bdm5qTap8K6j5sELyVUhVMzoPMmL3fxrYyR2s0msEZJEDzTbzx4Zjrbx-MXSGroYW8FhozQVXoMqAynqG-6hBtIg1EZP5VY_wc80j7UoCUhkY1NaNvfKQQfcr7Wg6niImRSY1U3vXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=EbEB01L5pVHLGtTe1gDk_r99_VREN2H-DWSz3c3yunLaMbKYEWJBWMRnz2JxH9VOp5-V1e-iMbN7hwknzLsXbK6BZgnJ80f7Xw4HiMaunzupKia4RCGdRPE_1MWCzip2S2lCPx2QjGuTH5G_wcCoMogOkD5TVfPzpsUuGW3-ZouVssgZa5IInKsA1Bz75GiSW87qho3LViyr_btq-Ja9JwZC9OBl0fWOdZOTyLNWn3WGzzqNhvFWz0mEosHzvTmBeCG-w-JdkRUNGmUFq573G7BvCjPH6fW4Ki9ERkHFvaVEbMCz2WjWQxQ3wVnTfAl4LwWxH2LqHPahGkvnmIqFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=EbEB01L5pVHLGtTe1gDk_r99_VREN2H-DWSz3c3yunLaMbKYEWJBWMRnz2JxH9VOp5-V1e-iMbN7hwknzLsXbK6BZgnJ80f7Xw4HiMaunzupKia4RCGdRPE_1MWCzip2S2lCPx2QjGuTH5G_wcCoMogOkD5TVfPzpsUuGW3-ZouVssgZa5IInKsA1Bz75GiSW87qho3LViyr_btq-Ja9JwZC9OBl0fWOdZOTyLNWn3WGzzqNhvFWz0mEosHzvTmBeCG-w-JdkRUNGmUFq573G7BvCjPH6fW4Ki9ERkHFvaVEbMCz2WjWQxQ3wVnTfAl4LwWxH2LqHPahGkvnmIqFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=eCnosj-lwfyoceQ_xlXsZPQs_rLAsS24htW7DqKXeTuNNowYExzSfrvXMf8bK2iSC0lp4LMvh0bPmzmDoNvMyonWw_qyxV3FVTwatveCWGEKbC_n1OsTP10ZpoOtl4UvIRJ8_9KAv31i9ajfGJYarA12OWs6Yhwblz-nU1UuZI3Eu41UvyzbA2qfMFoI81Xbd8_SxNtRBax11GHU2-4MoZoNJNgp04WLStsG-T5gTtMDzE35PSdcbng6myGw5pcqU-a5kiAedMmFPwHKxirZfkKXtVntxko8IcPyMKJvsyhHI2kgWMAgyQ4Wdjc7uYCOJZ0RoLeZS0u5pz64EelG8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=eCnosj-lwfyoceQ_xlXsZPQs_rLAsS24htW7DqKXeTuNNowYExzSfrvXMf8bK2iSC0lp4LMvh0bPmzmDoNvMyonWw_qyxV3FVTwatveCWGEKbC_n1OsTP10ZpoOtl4UvIRJ8_9KAv31i9ajfGJYarA12OWs6Yhwblz-nU1UuZI3Eu41UvyzbA2qfMFoI81Xbd8_SxNtRBax11GHU2-4MoZoNJNgp04WLStsG-T5gTtMDzE35PSdcbng6myGw5pcqU-a5kiAedMmFPwHKxirZfkKXtVntxko8IcPyMKJvsyhHI2kgWMAgyQ4Wdjc7uYCOJZ0RoLeZS0u5pz64EelG8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BARNSAQz8LQZ5Yg8q47Wc7-MWRt1ASehUij9rSueEaUYBkj8Ab_a7eeDn-wM1NEt_GFtBYdwkDtKYYrtPh6eNYbT0gWQM_JFESvxSXNXbShZlQCs7dHuZRBUpyFVu4pwEoKoupMB0uAR8TfK5OA1KJbYvgKS6SDpEM4bXRsvrK5utH_CVJKrY70S6_OmddoZ7J30tL9n80jZXakJPCuntMlwgG2_d9OJMNJTUjsOyiQXKcvnFmQ0mX_BkIVXWsxOcfsX5xypoo7-SEwzpyu4p_EJAg4E5uaWX38brLZQi-eM35Hc-RxoOPPEQeqsrtm4ffrNXctkdt4ozHzEHReRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=VxUug67FZQjyUbdcIWKlBSAlsvzbVKaGJ5GYrqDVrFvreUM55Co8SkXhxSxDVTl7M6GDzZg8etb5QgXxuNAjtYc01N2SWQTSmyc9cjfhtMmLxeWNCpKxST8OUx94dfweg1BJTD696sx3CdYVRuogqRiaG98Ut-GgnzvPfYqYdGFidqsHwvJDN9ddQ1ku6pZcVg6ziKKWpaIlRQYg1eMTruRG2-mDR_2hu0bqDIeNLsdnCwKhZd-Smi-phou_YcdWM5w8sb3E_u3e7_qT6s25qO-6ooZl5IKJvQ6W6QdfmLHul2Au5ipKjwVMvursTb7rWiO6G3FTZYFgofO2MYOYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=VxUug67FZQjyUbdcIWKlBSAlsvzbVKaGJ5GYrqDVrFvreUM55Co8SkXhxSxDVTl7M6GDzZg8etb5QgXxuNAjtYc01N2SWQTSmyc9cjfhtMmLxeWNCpKxST8OUx94dfweg1BJTD696sx3CdYVRuogqRiaG98Ut-GgnzvPfYqYdGFidqsHwvJDN9ddQ1ku6pZcVg6ziKKWpaIlRQYg1eMTruRG2-mDR_2hu0bqDIeNLsdnCwKhZd-Smi-phou_YcdWM5w8sb3E_u3e7_qT6s25qO-6ooZl5IKJvQ6W6QdfmLHul2Au5ipKjwVMvursTb7rWiO6G3FTZYFgofO2MYOYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1vsbe-xsq3ykTPjvuy4s3W8n3tzesOd006ucd3alkbwfa_zStfO3AHW2_cfj0SlyCM1YV4c_7iMpRdsZg4dqd6l56M3vHI8L85jvvG12FQXy2PFa2-QAXt3fWzIwr5zxz5ULLl8cHkbeXpRrXglbgndW4QeHWPaXjYSI-dDlhh2IzsKl0vWD3nB9jAHrd4QN6nxkzl2wQRh99UHeHkiKDejE_KSCXYj_3MltkTPfUxeYpn19cTTxDVNFMFoUymOf8IDkQswiuIIHfoDv57VsmBnC03vwFOuQHSqYmONlMxt8NVOR-Fq8k2pxlFCmmSFkwklcgEF_wyrR_Zq8P597w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViVdwmfSaj6CeHC3JowSKsLH6yTihfgnxOKv9fbqKwJRchNVM5oR0ITS2KXqgPqU_gNcyqiEAwqzUO0cW1zxrET-IQDQdE9D8yqSiCF9VSDM3Fx34UX-sqSgag1pt1QU8I61Q9kzVUlJkolBZp9wEQWpokUIBxHP3bKKEWue0mrkVU6k6S1vhDWYZ0YLKtmAiE3PFJo-TBieBn1MxwAHgs_fsAcF4flFWzwU1vl_7MA-0L4qJVmyIFX2jRcwjOMZWfTSm81xGMkWUrMrhMzof6id8E0LKU_6hWZUzIQCypnmw_W7X-y5smbc9h_dkk2u2Gi1crceB_DlzGM_zCL9ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teqv46im1-lv7nmjXNXYjhznmL8HYEHBI6b7All4zdR6w1-mQ0jIEVZFynS60ru1wGQiWIaFjv3taK35pWqgx6Y0R5en57-PozD8WMgD0ByRjUq6OocUCqWXAG0viqJpxU8eH5MKibjx1-4f7she_H06aoRuLCrM12D3ZUMTuZz7zmejsys1EZ5aoO2Kx2iXNgaSrcPWB7d_iwEe2Jbr62RasMaN7wKaptsVkp6z-VyvTj2vF23j7_raSrqXAtqr-wnhLq5m9ALsXwxtJCjJOQcJbdR1TovnJGTs7WkQDJkz2MRDcDemt5mA8gYJKXn4Ttnq5ylFeRE8fb0lxvmlDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyMRDP1IeOHC_89XBXSrrqZPIjiVMyCEiZFFSoHO2cFPkMygB1F4_KdHL1Nxy8fzbNVgTB-j0PihLfyS25S4O0ML4v7DxHJn-ET_1oz1hXD7saGKyPEsjRN7J-uuDBO3d5LnkuQxiaSuArpfLAbBlI4thXAJu-4oXOLrjoaVLdn-_yDVAA1AqenaR8pkW9zV199_aw8m5P3zy1jlR0bf0vX7Wd1_T3TfxtJNhXWAthzzvJ2Kg9Bz2WTaPescc8aWf5OArHtnnxh4-w_2L3pBFiGvadRLmkxmHmCcMxWxK1WSJCRDW2k0DzkEN9YvrATPnhrrNqAruIkEcYL_TRQGvg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=J_dWH0pvEgSFK0K0brZBGXOJSrF-VBfqxm6cybDKSGMWD3n8Dsw8tB8RQyriQ3Gfm4Mk1Uen_sHGwjWiA1EfHxNxCGbJm2pFTp4rwKBWf71u5Rj3WTksbqg5vyDNSEffdXmaMoga7SX3iTaPKIgJ0o6PkSXxQksz9DqP2cfKtmu8e4JzE1bJatWdbYduQoi8Hkoydd5rM3qclxI4b4KYC2hVbXKZGGfqS3mJB2Sqfios9hSYhRP_Pf4NZXRjUSa3XI-ibBZDjf-_UkykwIeQalsh6kMv2YSSf-PcwpMsP_zDsXQLlqwdQET5lBQYpE7Fs19V-divf0tD1ZhY0ghgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=J_dWH0pvEgSFK0K0brZBGXOJSrF-VBfqxm6cybDKSGMWD3n8Dsw8tB8RQyriQ3Gfm4Mk1Uen_sHGwjWiA1EfHxNxCGbJm2pFTp4rwKBWf71u5Rj3WTksbqg5vyDNSEffdXmaMoga7SX3iTaPKIgJ0o6PkSXxQksz9DqP2cfKtmu8e4JzE1bJatWdbYduQoi8Hkoydd5rM3qclxI4b4KYC2hVbXKZGGfqS3mJB2Sqfios9hSYhRP_Pf4NZXRjUSa3XI-ibBZDjf-_UkykwIeQalsh6kMv2YSSf-PcwpMsP_zDsXQLlqwdQET5lBQYpE7Fs19V-divf0tD1ZhY0ghgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=uBkpP5nKMkOaG59rDxjhO3AyGsOJE_DQkP1eW1ho_M7AKWQ8vRUvynXbBNu4nQiU3Cyw3BRXrpIMsCgNAjjSz9R4QwrAWHoFGd2tVxCk3EqPUJixaZkqIHCv753lS3DZJEkCvfrdqsmVZm34xosi52LiumSaWxhbY6pfShB7XAupZkdwQaXjgpNW8MwS4Z2fz4DTo2N2gNa1uERWmGzjyJNEgErPL6TGMOxe_01qhzG9Op1ggKOZvO6kNURJh6CG9lRdfdBiQ-Qsk7f6QHemCWWaE_aEbXHJ-ZbpYN3mFeKlAFK9xk1_IxxwbkS1Ydx2ioh_ZLdTM9UCPfbFhhPd6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=uBkpP5nKMkOaG59rDxjhO3AyGsOJE_DQkP1eW1ho_M7AKWQ8vRUvynXbBNu4nQiU3Cyw3BRXrpIMsCgNAjjSz9R4QwrAWHoFGd2tVxCk3EqPUJixaZkqIHCv753lS3DZJEkCvfrdqsmVZm34xosi52LiumSaWxhbY6pfShB7XAupZkdwQaXjgpNW8MwS4Z2fz4DTo2N2gNa1uERWmGzjyJNEgErPL6TGMOxe_01qhzG9Op1ggKOZvO6kNURJh6CG9lRdfdBiQ-Qsk7f6QHemCWWaE_aEbXHJ-ZbpYN3mFeKlAFK9xk1_IxxwbkS1Ydx2ioh_ZLdTM9UCPfbFhhPd6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=fLCsFThldx6lvJMFM-rdcwVpfglHbfrQqVzijqWywM6etG91FDtvYqVMPwaECCBjw0vv_jm8sR0TmflyiNiLiJ5u49OWx5H4QR5EFnUWSANomCsMObPlSsh2Nx0OmLFbt6mAONhLMeZ9q46XeWxkZkLRM9KWJ6BNuYCswuMQQn42kwaajz3TakYjPEwIk5iewMOM7DKyQcFa97jsmZZAriZb87B4uni22Ppmhtin8eC9zDyJNxOgLAl3veOryTKLnbnqB3G_WMlD8eXI4z9jhw4fvYEuGP33I41iAfkSYLgDrjW3kk-5exvPhsvLAk28-FywgHUTqik7zHtXAz9eLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=fLCsFThldx6lvJMFM-rdcwVpfglHbfrQqVzijqWywM6etG91FDtvYqVMPwaECCBjw0vv_jm8sR0TmflyiNiLiJ5u49OWx5H4QR5EFnUWSANomCsMObPlSsh2Nx0OmLFbt6mAONhLMeZ9q46XeWxkZkLRM9KWJ6BNuYCswuMQQn42kwaajz3TakYjPEwIk5iewMOM7DKyQcFa97jsmZZAriZb87B4uni22Ppmhtin8eC9zDyJNxOgLAl3veOryTKLnbnqB3G_WMlD8eXI4z9jhw4fvYEuGP33I41iAfkSYLgDrjW3kk-5exvPhsvLAk28-FywgHUTqik7zHtXAz9eLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=uf8DBVRtmLirrP6K5y0h6GH-x0gFLbj23NAkR7K30LXI0jTqKmNzFzTOHd3MU5zLRYPqb7vAPUuWUw8mX_dWhYioaAiby7nUetUFkOdADVtiy0tjN0MXrwcoYokDg60cc-FRqT6hV3UmC9UOT1nRW23sUE0JT55ZHotjJSRFyEjoG0l4AKS_3K8hSvk8z-9vUEFcYVjGm3-ubrjMNAmUQrJRGtYncdlSpCShpjYf8shHyAFfZjkhbcbPubuMNWdPH9b28ZdDYLLzRUiPuL0VwmUo9nzXhXExJnwFOXpYf5OUG5vtXM99DD-hrG8iNahGIMglfsOqLWM0yBG2vuvrSjUViiqPuBk2R73u_CGT5OEVm1tr1oa7FZ5lkFIGLWG0Ve8uRNj9NfkEFfg8-YmLoEwSdj0PklfQoMiLM096H-CcgbaN2ulLkmt8EadIjF1rDRUCw5s0NEurxKgF-jvAFE_tTInM-oGPir3o-sRd17nZWFhxbRY3_CPjfXj0u0-Mk1PCFse-Kj6XspDenWdS5UCkJ3ByjNXmQWESCb1FCepzhvQchkO59jXWz4ucFbHHt3k6s6NmEZ-qXC-vJlVwEUPmrwSCRLSGusnfJ_l9x8YcPgi2R8hv0JhA-kY11FbdueEAn9quhNBoxiXETHRwy7bkWRWfUz3T0TYxokfwM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=uf8DBVRtmLirrP6K5y0h6GH-x0gFLbj23NAkR7K30LXI0jTqKmNzFzTOHd3MU5zLRYPqb7vAPUuWUw8mX_dWhYioaAiby7nUetUFkOdADVtiy0tjN0MXrwcoYokDg60cc-FRqT6hV3UmC9UOT1nRW23sUE0JT55ZHotjJSRFyEjoG0l4AKS_3K8hSvk8z-9vUEFcYVjGm3-ubrjMNAmUQrJRGtYncdlSpCShpjYf8shHyAFfZjkhbcbPubuMNWdPH9b28ZdDYLLzRUiPuL0VwmUo9nzXhXExJnwFOXpYf5OUG5vtXM99DD-hrG8iNahGIMglfsOqLWM0yBG2vuvrSjUViiqPuBk2R73u_CGT5OEVm1tr1oa7FZ5lkFIGLWG0Ve8uRNj9NfkEFfg8-YmLoEwSdj0PklfQoMiLM096H-CcgbaN2ulLkmt8EadIjF1rDRUCw5s0NEurxKgF-jvAFE_tTInM-oGPir3o-sRd17nZWFhxbRY3_CPjfXj0u0-Mk1PCFse-Kj6XspDenWdS5UCkJ3ByjNXmQWESCb1FCepzhvQchkO59jXWz4ucFbHHt3k6s6NmEZ-qXC-vJlVwEUPmrwSCRLSGusnfJ_l9x8YcPgi2R8hv0JhA-kY11FbdueEAn9quhNBoxiXETHRwy7bkWRWfUz3T0TYxokfwM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=JT9bKaT-xvB5vz5mRYBOIJXTXXCLJ8htMnQiR5ySchnOTJ0SPVr9MmBtT9tkjiKsfcezJ-WBqvoZDUIByrQOiAwKZr3Tx1McKPvthXUaSc1FHPtFtRIOGKpqJOy_jUv2FTWomYYu3nduUuf9vef4UzNTDJUQA_E-pE4uKiXIMxqIjMnkAREjfyLkUtcQwKmisproX4NKDP_QPZIJF9seOWmk8FTB3BiQW81-c42oT1RhbgrT1Kxdtp9mqqSbjgUAB3jZ-d3BTR-VQ9iRZFccJpGrGV7uPKtJmycm5U5KJE_ujOKeKFaKU6Dm1sQLE-O0_tWvzgbdcf3e0GlNF4VxaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=JT9bKaT-xvB5vz5mRYBOIJXTXXCLJ8htMnQiR5ySchnOTJ0SPVr9MmBtT9tkjiKsfcezJ-WBqvoZDUIByrQOiAwKZr3Tx1McKPvthXUaSc1FHPtFtRIOGKpqJOy_jUv2FTWomYYu3nduUuf9vef4UzNTDJUQA_E-pE4uKiXIMxqIjMnkAREjfyLkUtcQwKmisproX4NKDP_QPZIJF9seOWmk8FTB3BiQW81-c42oT1RhbgrT1Kxdtp9mqqSbjgUAB3jZ-d3BTR-VQ9iRZFccJpGrGV7uPKtJmycm5U5KJE_ujOKeKFaKU6Dm1sQLE-O0_tWvzgbdcf3e0GlNF4VxaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=IV5tCz6La11uYqtdfuKnPeiz3lNOIfVE0uejgOj3vrvY5WJYAG3kVC2vizoq0c5IspryTeudhm-Cm3do9Tbr-eGNS7wlfJCe5S-PJM17CN2p_JNakC4-Wkyx4NM9aPH_arLv1KrFLKqrOdecGnmDco4SkPShT5WO4CD75ApBmW5UfZq-3xgj5Ly3Q3b_dyjl5DNxk5tnl5USKd33DllqVbjBLWjLY1_yZGaKhGqv-7WXbTi1gQipKgdLPd5aUuIBV_xAONziZ2fqoHLcorxNLYan44xYd2kLPJr8xYo_76i9rXDpGycQXkLJf3x_5Ufg6YD_6tGYFboMURm7Cpt6Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=IV5tCz6La11uYqtdfuKnPeiz3lNOIfVE0uejgOj3vrvY5WJYAG3kVC2vizoq0c5IspryTeudhm-Cm3do9Tbr-eGNS7wlfJCe5S-PJM17CN2p_JNakC4-Wkyx4NM9aPH_arLv1KrFLKqrOdecGnmDco4SkPShT5WO4CD75ApBmW5UfZq-3xgj5Ly3Q3b_dyjl5DNxk5tnl5USKd33DllqVbjBLWjLY1_yZGaKhGqv-7WXbTi1gQipKgdLPd5aUuIBV_xAONziZ2fqoHLcorxNLYan44xYd2kLPJr8xYo_76i9rXDpGycQXkLJf3x_5Ufg6YD_6tGYFboMURm7Cpt6Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Twvh3_ksq90zoG_yG8LZhqjhjuGds5pnIJBSykyGzgSb4dAMy-mWzTrvlszH9aIb0ggk6nHJWK2R-QM1h5o1ehWtlq-rGEKtZmejxCoCvB_OhVRx4Enahz7bXPsb65QxbsLO5SwB3SU7EO50FnPRUa5dG4ewv__HhS7VV3ciWp5upR1UUrQ3z5jeD_bspDOpit_L9HeiSl6NMC1pV-Gc9li770BD-CEVwgV25RmVcF1sVtjdpaluDAYJSiEu40vzsLMtE1Q4ulvfL402-Q4YrH5ae_OZ16VpJ2PM_OlsBjNlOCpIIRka7Liad2-r-prKQPSidAYEg5Zs13W0k5qV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=TKFxHj6BmWIleKK2kucFxpQqSoJWKNlgQdlk70EFWDNgbt6bFmiIcXb6bgcPar3YloA4aIFgsnUuahEVqE6GrmnO7i2f6QwplqgAR0qdOZeqdLuu_IeWXg4gtUwZ3x1adfSQVrvRLpNEDf-K9VzUf-puvZXXCRwlCu9lmT7xDL9ooOWFj2enAUB5rintDVK6YPumUH6CowUliPgDiNjNThIFWnfuA46hEdRlz0LLJilYzLTYe3W7_Lfo0HfHXUWaFKNBkbdGEoXbFg0SyDQkzytj2-v673p2P2EqEdw18uqK5JVgNkycpp1vng7XtV36nJuIKLSFJWqCIGLs8eZGcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=TKFxHj6BmWIleKK2kucFxpQqSoJWKNlgQdlk70EFWDNgbt6bFmiIcXb6bgcPar3YloA4aIFgsnUuahEVqE6GrmnO7i2f6QwplqgAR0qdOZeqdLuu_IeWXg4gtUwZ3x1adfSQVrvRLpNEDf-K9VzUf-puvZXXCRwlCu9lmT7xDL9ooOWFj2enAUB5rintDVK6YPumUH6CowUliPgDiNjNThIFWnfuA46hEdRlz0LLJilYzLTYe3W7_Lfo0HfHXUWaFKNBkbdGEoXbFg0SyDQkzytj2-v673p2P2EqEdw18uqK5JVgNkycpp1vng7XtV36nJuIKLSFJWqCIGLs8eZGcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g67FdcWJUg7L3wWGVILirOksCg1oeWO6OA7vb1QMkTL6UiROIAzP_HIkmZPJmRNN9AL9Cq3E4UQELqtZOuSBeDF5MNaBZED4QxBhURdXIIjkEaTLd_sscYCOsJnXHIZYqXIISvHNkONXuQ9T5FeFXO7lb_wCSwB2xaUSCTbOHfIakNeeB7uGGXwYIBkUVswe_4qFQBQz7Swqk_4iuL9gRSV9pKEJ2SYyFWvKJnq9BgV-teVw6jVpZtafXuFqwRbHwpKmyXqg_N9Qd9KkM5gWVbAVhonHDnQTr5LeU-NrKcEhdSfa63OHJk5TY5xFb1LRKmk6t7Y6ZKo6JcKs-v9NFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPRdD3NMdnDJc71ELID0hSvVpmcGU1pJcHPz9gkvV7z_PClBh-CufpHXG2yWUazcTU4dQkH1BQ2flAAEsyDNRYjFbrMG7YhRfhuO_2deC7W0lhd_6CvRS_7AFFsRFpiR4K4wy5_rRHGvphYcl3oBFhY4VniArWNxA3ngWnKhT3Mv1XJUKpORMpBNfkFCWANil6qWizXmHiVgxe5cVWgWOCB580v-LD0XNCXSulqubcqknJDrwwvBs8Y71vQlEFvIhYKExf0iKmsCIrVSao0s8aiQ3xDkOJsxa11L5N_3L8Ce8sPHhmis7Wlhg8x-cYyN7YF018y7cCaMPbjYkBDJ2g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=vKE3qkJXTS0ySIMTy_vORnkwd50519Cwdk0-yDsHjQmImw1MvIALdY8zUBqOb6A_dhYREsrsJbyPrMS6oupniNrkr6cm_QOuW206uWWB8U783Cs8xFaFoRQQ_2GnonQzZe1yaU2ydDy8AUqPLRv16G7ffcjc63qziKAyMFc91TWeL0IBa689pw0jBy_oSxP61ihwpcCu6urUGOkFjE9LmrWcXQzy5ZnvyymcjdRWJu6uxvSGlR4Knzghjd1aFIvAT2Ts9v3bem6D6wn_ScSuZOMdvpHsN3I1maKow_LvPr9IZntQCPxxGlSYCcMkj6iUFOyQpvCHE4N62NwjU1ArmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=vKE3qkJXTS0ySIMTy_vORnkwd50519Cwdk0-yDsHjQmImw1MvIALdY8zUBqOb6A_dhYREsrsJbyPrMS6oupniNrkr6cm_QOuW206uWWB8U783Cs8xFaFoRQQ_2GnonQzZe1yaU2ydDy8AUqPLRv16G7ffcjc63qziKAyMFc91TWeL0IBa689pw0jBy_oSxP61ihwpcCu6urUGOkFjE9LmrWcXQzy5ZnvyymcjdRWJu6uxvSGlR4Knzghjd1aFIvAT2Ts9v3bem6D6wn_ScSuZOMdvpHsN3I1maKow_LvPr9IZntQCPxxGlSYCcMkj6iUFOyQpvCHE4N62NwjU1ArmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=vZnmsiau42ZYJDOJ0MLOYyqigJQaGDnmQszgj1nzigWwxqC1sXO1ml0wQOASde5dhb2mA-omu2eUhzZNVLHou3n70ElYbkBLIJWqDymDMdvudDk-_TOi_j45NsUS2NMAYgDgiRMYC8xp2T8_RqW1MpSTkYkIr7jcZifxsrzVVBUu_JGdOZrDtDOlvO4zdnjnfFN_JyQKxuh-QqBrhhkRQo7aphtO-5AWXCsMFP8zE9iKUPfxolU3BDsXZXZ2fJO6KdB0yc_e3kXO3P9QVkBvcmf93nnKBV8AXHtW16vTrn6Wr3_f7bcQceUi0RISChs497EYlL4oDfqv4AfasJM9MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=vZnmsiau42ZYJDOJ0MLOYyqigJQaGDnmQszgj1nzigWwxqC1sXO1ml0wQOASde5dhb2mA-omu2eUhzZNVLHou3n70ElYbkBLIJWqDymDMdvudDk-_TOi_j45NsUS2NMAYgDgiRMYC8xp2T8_RqW1MpSTkYkIr7jcZifxsrzVVBUu_JGdOZrDtDOlvO4zdnjnfFN_JyQKxuh-QqBrhhkRQo7aphtO-5AWXCsMFP8zE9iKUPfxolU3BDsXZXZ2fJO6KdB0yc_e3kXO3P9QVkBvcmf93nnKBV8AXHtW16vTrn6Wr3_f7bcQceUi0RISChs497EYlL4oDfqv4AfasJM9MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=KQH7fuodST9Ei236-XD5lzrqENzLB8pEDHvAECmdUaYnyboWxdlNY3Zbm5qgsc0UoH28sAPN7WMDU9M7yJ7XJfauNICYjTswYPAG8W1I9OQ6IiBJxIddqvEFadSOe1uyUuJHJnYYoWzYOabYJFDNXLQl_czdQCtODpSzjr2iFiB3tAZdLj87tSrs6YwFd9PwVlfQAln5UzJkIJTZHlLkjIePNWemy2r20KT5BLdV-15NqAlon9peUcnhajGDYZC3-Cjde8GMxmfoWmtatKLtSWtXRP8zPKYu6h7US52jQZb8kuOB2AE6-AxCRJzs52vUct7reh73MEGbXSoKT13sJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=KQH7fuodST9Ei236-XD5lzrqENzLB8pEDHvAECmdUaYnyboWxdlNY3Zbm5qgsc0UoH28sAPN7WMDU9M7yJ7XJfauNICYjTswYPAG8W1I9OQ6IiBJxIddqvEFadSOe1uyUuJHJnYYoWzYOabYJFDNXLQl_czdQCtODpSzjr2iFiB3tAZdLj87tSrs6YwFd9PwVlfQAln5UzJkIJTZHlLkjIePNWemy2r20KT5BLdV-15NqAlon9peUcnhajGDYZC3-Cjde8GMxmfoWmtatKLtSWtXRP8zPKYu6h7US52jQZb8kuOB2AE6-AxCRJzs52vUct7reh73MEGbXSoKT13sJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHmoF75WFVgoPHRWJkRktvpBmVQVA8ls2zMp3VaWG9uVOde1cWru4XfulNlInBiFJiV36rgpZR45H3Phc76RIt1GbwTCsMsfgKQTLQrB1_hfSlYsf84UzUGCODYYy3KUgsnNIYRFW6bx_YGJZZoQ2eBNvskVxyIdkUdqvqKeo0lCFPkwB1GdqN6NnumMnNSu7aib6jxbBmsj3dbiEIWRxZI-jgd7lg8NUFglu1LPN3Trym7pYPLEqISVtJL1ffzynjqZ18-CYfnGlF2jKoLxBHZRHOThSDlw8zWsycRQbmu4i98Z7zpzcZKVswfNm-4pKUnDcG_JDbpHvEDU0imAkw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=XJxPdGfeeWqHtNMg1reNwUPA6v4Ku1ljI9_u1G04Ur1ERU3ivliTPTiY1WLz9IK9rg3qiMwQjWjpOfEw6mTtnPaPifr8wP5gZn_09Q4OF36HD3Z4k-hCfjW6AlFyi5IJfH6sXP8yUPhTm4SgsKr9eKo-GAuU2t51AfdcnocW6WCMytnZOhhhbODxebJiPsxdNFSGu_-hYbyNRRR3Gngoj8AHt3Gl3U7dx1PW3fpomxWOinHuCS3CcuUytMaX7D7l9SP50BoAMj_KtgZiZbWMQGKRW08BzbWzBg9IKWQmo7OlbKOvOmXn80DJVRRabaDe5hJIPJVK3fQ--8MhKaixqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=XJxPdGfeeWqHtNMg1reNwUPA6v4Ku1ljI9_u1G04Ur1ERU3ivliTPTiY1WLz9IK9rg3qiMwQjWjpOfEw6mTtnPaPifr8wP5gZn_09Q4OF36HD3Z4k-hCfjW6AlFyi5IJfH6sXP8yUPhTm4SgsKr9eKo-GAuU2t51AfdcnocW6WCMytnZOhhhbODxebJiPsxdNFSGu_-hYbyNRRR3Gngoj8AHt3Gl3U7dx1PW3fpomxWOinHuCS3CcuUytMaX7D7l9SP50BoAMj_KtgZiZbWMQGKRW08BzbWzBg9IKWQmo7OlbKOvOmXn80DJVRRabaDe5hJIPJVK3fQ--8MhKaixqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=N79Fm0fI0YsYErdnIDrd-QQHQuwsSmRMm7OeYVU54dSKKBQobrHhKVPwN93fLM6VXPYJn-2cZmFdi-OLflSQMF5ZW0U9cqYTnhc5VUaj4vLfJLlCnNBraiG2LF3VRUu9eyrjmhGVWuV7mXpxJyV_X1R9OKQNFbk9RDZNmw7saLaWtfsGLg2mdwe_OivN4RIETe__lJfIdSFwu-ogSkGeWcpaGtxevSyKhn0LKvOA93IgfFL49IkHze19UPx-T3-Mo8oCLgqEzJxUKmNC95Lbq7p8lU1DzbDnJKtgVntqZSZL2CVj9NEMuZqXAvY2r9_LmT38Qxr23nuwW5kvXUkZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=N79Fm0fI0YsYErdnIDrd-QQHQuwsSmRMm7OeYVU54dSKKBQobrHhKVPwN93fLM6VXPYJn-2cZmFdi-OLflSQMF5ZW0U9cqYTnhc5VUaj4vLfJLlCnNBraiG2LF3VRUu9eyrjmhGVWuV7mXpxJyV_X1R9OKQNFbk9RDZNmw7saLaWtfsGLg2mdwe_OivN4RIETe__lJfIdSFwu-ogSkGeWcpaGtxevSyKhn0LKvOA93IgfFL49IkHze19UPx-T3-Mo8oCLgqEzJxUKmNC95Lbq7p8lU1DzbDnJKtgVntqZSZL2CVj9NEMuZqXAvY2r9_LmT38Qxr23nuwW5kvXUkZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=HUNBpHGWSAR87iSZyzp3qckostjkJQAECIA_63Y1TL6M7g9k8J8m3-CeJDcAfMe893T84eP4U2WhptUKGIFVz2_etzVxqFhxTqB5fnx8iLiw-55vKpM-CnU8abl0Zr6iMgfDGis0JtGLRlfTXkLKBrxDKVATdyyxAgZjxAKyARTcQEcP_V2pqhPmEdxluVR6DzZ3eAbC0UP3GBG_79J057kAO9fGYmc0g95bTK_r1It979CdBwHDa1vjJykmbjgmQA8-cDNS36JEaTCneIm1w3qlp-BarIj4x-_ncSqrDd-33pbdrLtMkOUIhq0Bofz_aDeC1czaX3pt_fsPZxXeNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=HUNBpHGWSAR87iSZyzp3qckostjkJQAECIA_63Y1TL6M7g9k8J8m3-CeJDcAfMe893T84eP4U2WhptUKGIFVz2_etzVxqFhxTqB5fnx8iLiw-55vKpM-CnU8abl0Zr6iMgfDGis0JtGLRlfTXkLKBrxDKVATdyyxAgZjxAKyARTcQEcP_V2pqhPmEdxluVR6DzZ3eAbC0UP3GBG_79J057kAO9fGYmc0g95bTK_r1It979CdBwHDa1vjJykmbjgmQA8-cDNS36JEaTCneIm1w3qlp-BarIj4x-_ncSqrDd-33pbdrLtMkOUIhq0Bofz_aDeC1czaX3pt_fsPZxXeNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOIlR61gGFoVvjEwIR6twy1bbkUzNhE0-Rb-c5yy1CSp94PYAFeYPsUCE9XTa07TkGKxV-JwU2IMPRDHtXXWCdvaFeK298cVgSePtX7FbAkaajzXqbfQ0399Dk8IOXSwiIIPXKuufO7kSvWTDBubNPamA221-yQkUYWh4mhSpJeX4ClSzK7N_PqJypqgESArWoxRvJJnglQ18QcsNC-PyfpeMe4wy08BCM-yrP66pu5SzIFSSzQv-_RN5gyuoC-G109XxG3TARG53X_XX4Wlqptgs1BMUXiDtBFjzveihE3LZMgAs4Oqw9QfC6vnrX7bsTtnX8BKLSE4rUukfeCSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=IVOGb6FPhqBkAE9Y3GX1ss_BBxahwStd9ru4MqXL5i7oe2c4-gDmLm8QsZWTjX04K6dfqjX1Zw5xzVso4-DTlwuBiffvIW_Fu6ngH5x9t6mrps-NCCgXXtVc_qRMGPrc41UAda7C5t0OxSGbauXCZPrSNdCjCutPnLvIrPr9oKmGYlTttJBmTJ_TQxiO55ZYxwM5cO9trGc82IRhlzeZcCCjB9ZGfsmXMOBvI28vhJa4F_twHxXdZvr2Ch_qnlngu64FlElRa0hvjVouGtVJMrTvNco8Ki1dHlp4reHafDfXwaLOStRd33zvIkuK6RBPep822uLc804DPu3Y2r5cog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=IVOGb6FPhqBkAE9Y3GX1ss_BBxahwStd9ru4MqXL5i7oe2c4-gDmLm8QsZWTjX04K6dfqjX1Zw5xzVso4-DTlwuBiffvIW_Fu6ngH5x9t6mrps-NCCgXXtVc_qRMGPrc41UAda7C5t0OxSGbauXCZPrSNdCjCutPnLvIrPr9oKmGYlTttJBmTJ_TQxiO55ZYxwM5cO9trGc82IRhlzeZcCCjB9ZGfsmXMOBvI28vhJa4F_twHxXdZvr2Ch_qnlngu64FlElRa0hvjVouGtVJMrTvNco8Ki1dHlp4reHafDfXwaLOStRd33zvIkuK6RBPep822uLc804DPu3Y2r5cog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwAF62KYUwhThbI50BU4CZawM0x4lkjQ7ML10tt0fdO7bRoNCeLqTWbGR25zVucbm6F8dpHot4lDUnj9OzQDDs82pHsdiD0VuQ-JAesUjXDSLQ3eKsTeo7rN_VyLR75CJuGeB2Tb7lE5QOcpg7b8-x-9YmWaBGm9kWG7FrbsHWtlu7miXoJD2SfjWGwA3YYVtLzeDOV8OvKn0CYVJ0K--ejduWD8W1Um-3iYCkIyAvKHZAVKa7urHpOgV3HKRcHSrTmZuirRHRtl8h4yYUzMsLUJLS60Bi85UVpnWPviACgKpLPxBkW1YmcmvUnHWqPnvgUOQnXqr1yvDN8mwtVoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=p_5ND4fTDdvr-vzxsx2mnYFDFy1XQzXWqO7EBvx5zuU_KcoWOZDWsjBQlBdO3RDNOEKl2tP3pG8MIlyqmf2FJKXJzUVq-8LZzsbkJOFiZleZZzuLYokSlkvDhmqmnfr_zofzeiE3BSQIuUJBMucjcwwzPTFGP5wyBKYA9BMbZKa_hQyqxMc65iUOeeFnU8p2hrY2SDCtXKNSJ0QBdqsu7mTa9Sjoo91mzOf_8j8POcYrRum9gFm3ak0f180gb-ORLbpBNEB489DIPK88iphKTh9YzGOpzVDO8Zk8Z9XMQqpJ7NmXHJ2Se8FigvCYp_2e1gej0UKHVSSEPAeVESmhWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=p_5ND4fTDdvr-vzxsx2mnYFDFy1XQzXWqO7EBvx5zuU_KcoWOZDWsjBQlBdO3RDNOEKl2tP3pG8MIlyqmf2FJKXJzUVq-8LZzsbkJOFiZleZZzuLYokSlkvDhmqmnfr_zofzeiE3BSQIuUJBMucjcwwzPTFGP5wyBKYA9BMbZKa_hQyqxMc65iUOeeFnU8p2hrY2SDCtXKNSJ0QBdqsu7mTa9Sjoo91mzOf_8j8POcYrRum9gFm3ak0f180gb-ORLbpBNEB489DIPK88iphKTh9YzGOpzVDO8Zk8Z9XMQqpJ7NmXHJ2Se8FigvCYp_2e1gej0UKHVSSEPAeVESmhWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtVYfTJHMquBq_4fpmR5L3fXXbS34YaiMrzNyhYDRMMOByoe3cr54ma1Pfh_fWsvtkcb1Bm9rDL76PWBUKv4fDyVsWTwXF9GfQinTJrrZ7yH1XQRyiewc1p69SJr0_A2TIIVCOrWLug8_Irw7IZyzWUW3qDg32b6HWz_uOq-t2JFpWc4Y3yAyPhD6qfNPyIXBuGz64ID7m6SS_JV-12gAU0Q8u0aZSIwgFmyH0OyiRKhgIB01GgJasXx8r-xRAUoV8Lt3KP-oi56XBWT_O55kN986BkASMVmSlqpZ6ydn_Mc5SbudVEs3Tz0uBETksOcDCpUA04_vJWtxmNheTI_rQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=S_vwOJ7iejoiBulNYc7l_BqsSHtSpAmCyk1MZH2vi_cA1K_eFcKppOZmMmyyS_EXe8rKEAl2wZETA4z_t8_TgLaXQbhnKnogZ61Kkrfz1UgYQwtGQ8ZO_nY1XzDlrhYNgB7ibf1TjRadEETRcvPD3Ug4kKgeDZB_0Fnsku4bxoD2zibdnWijlfEpf_oTAVXf234arJrs4ufljKNQyGPcAMDxKTWXmuGHWukq1AdQ7SuR1FkB3gXHDU3D637KFXrMcfHxwiMh-3DjBss5uCicfNVG3JmsQMWVvoUTBe_6CIQJSDt3NbplLa-Y5h7t3oeptenPHW4WwtVAHljn2mOTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=S_vwOJ7iejoiBulNYc7l_BqsSHtSpAmCyk1MZH2vi_cA1K_eFcKppOZmMmyyS_EXe8rKEAl2wZETA4z_t8_TgLaXQbhnKnogZ61Kkrfz1UgYQwtGQ8ZO_nY1XzDlrhYNgB7ibf1TjRadEETRcvPD3Ug4kKgeDZB_0Fnsku4bxoD2zibdnWijlfEpf_oTAVXf234arJrs4ufljKNQyGPcAMDxKTWXmuGHWukq1AdQ7SuR1FkB3gXHDU3D637KFXrMcfHxwiMh-3DjBss5uCicfNVG3JmsQMWVvoUTBe_6CIQJSDt3NbplLa-Y5h7t3oeptenPHW4WwtVAHljn2mOTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrZS9mwhpIpmn8OOS_mM7ps8X2T5IxRWLsLZyUT6eFbjJMqixsoRur0QzfJ8AGcGJfaTWFfHhOEuMSpLMLLdW6ZLs8UqEnCi91ltpgCoHbWbG2zFX9PYhuKlfNJGHB9Ag5Zh5zlYevCSY_Mtw5zkKGc8vx-Y7QHjddgF2fCOLCU_rPuqYI7MlvZG49e1qU61-50QjKeBCDZeS-HiYguCEc2DUCyN0Ape46oSF4pfrQzUVom6iWE_2T79lBW2yjmbFND-saQr5pq4nen0mr8WMLcqy2G0sGPSxfiPB_mZIPVP3ydyXyZhRaBqEZnT5mSX92ioxCuh_mcHbGMvTP-qPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDVTTWE2atq9rCX0PmAi3ADu6Krdie1LtiC9lQ7ElTAEz70_ILduvCQfcYUgF2OPGYvNvAwE4yA2xrT4qgqX49XJPazn58mB8JPqF2wmR4dvB58EBCZNzXrKgpIBrTzj_PK4WrMQaAtfJ5fOuB-k40ii2rxpqOZIalsSeHy0Bqldl5Z3jEOUlWeV2Ve7KZxi384aqYSYFuvFXOUNF-OPOCD-Ml4N5x481h6tRHB2QT_GASPWJpBtgXpfViIJDKqtNS1aGbzrgmtekPNKAMZrXJDSerdR9vtCRNVImXuSknQ-Ln-40Kh5zcKzXPSArPMDr5PjudMOE2FB4Qmq2YfLPg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=VlybAXHfVUX4pZJL32IXXYrtfgcEeGcFf3L7BqIwXg08Q5uQOB0nABMQQHrA3Nb9lbddNVlLs4ArpAj15GNIzsPg4G4PGMtH7EBhPoqEARx5e9a1yYhrRTr5CERK9XjA5XkTrljlj5wLfYJ09R1sZtehq7IStILRrGvGMtaJgozYmrvB4ZY1dNbOdHzeloxdQE9tJ1iBVvw2edf-5t4ovIugtPHyzxVtJ0ays32Y9z9QOYlxSQy4ihkN8aCsNpMbuq0Pspq4qFZAQgCkXIJA9O94JacM2Vn6mKwOFeEHSsNMYpMJRPJHp1uXn2FaO58xZX1sOHCr6y7sVSj6b3RH0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=VlybAXHfVUX4pZJL32IXXYrtfgcEeGcFf3L7BqIwXg08Q5uQOB0nABMQQHrA3Nb9lbddNVlLs4ArpAj15GNIzsPg4G4PGMtH7EBhPoqEARx5e9a1yYhrRTr5CERK9XjA5XkTrljlj5wLfYJ09R1sZtehq7IStILRrGvGMtaJgozYmrvB4ZY1dNbOdHzeloxdQE9tJ1iBVvw2edf-5t4ovIugtPHyzxVtJ0ays32Y9z9QOYlxSQy4ihkN8aCsNpMbuq0Pspq4qFZAQgCkXIJA9O94JacM2Vn6mKwOFeEHSsNMYpMJRPJHp1uXn2FaO58xZX1sOHCr6y7sVSj6b3RH0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KePEvMhzcHpbAIGK-RW2TG3Nr0C1oNSeLtIgZZ3_cAIs3EapMmDufBH6niPJC1X_P2KfH_2QSUYm_uOxTWitjlgWYvosT9zeWF98fb9lxbrgcFzvpL5Z_8NOG5ApMRJa9K9Fz1wru0fdNC1zVHQQMV4K6iucsn5mfnLqzY1PP_gyakYtqNPz-vb3UJcahJECHwT4cES2j8NFjiQtWTd3rja08_AWp9ZVZIpuvtgvHYHZrY-4Qn-J0zIdBzm2-MR5LxQN9udMCtOste3WAfrlD-Es0vyTIN3dHkFPqMHOMFywF2btS-C5czZwDdEAGGuXjUF8I2AiilfxAvEYotgjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJcsJiIMXRV3d61UItCapneoIFVcsPPehYOzCvyFb29oxLkOlMYrNZDkiE6x2Z-joksINVGnHEQwr7wW6Yn_Yx6rAyH2ohBMEHnXRLibVYgY5B1Lekb5Is1sesO9Kg-DA8WXQ8cIWaTJw5YoJMp_hEkQOpGWY6Njfk3Ez2JjnTc3ZVR87_DscDY7_kd4W5O5y7ny3libpBOT4PDOKg0vFFGHJ6zVZxQYMVH00kxtdYh9EzUKvctxZ5cN28P4yVg-OqGETarP8EMb0i0B5-l8eBb5yE2wpME9exy5dA_Oyg6XhY1csesdf4umTnfpdYQRMmOeOXPP42j8xdkQ4zbWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB4QwntEah4XLlRs5UjaThgAr25uVe-noaDG44F6OSrGvLGcNr8XM6PWORJgN8EkY67p8Bdz3sAZRX5awJosOpeLJzezzBA8ixhESAnZ61zJYj3SoU4iP2YK1WNgF03HZftD61FNr_uk4JGeNZZG-g-MCfABldK7JYnaahaYcQA1oaYJped2kAKAq1RbQR5Cz4VOoWIkvlIXBp6VbTbFtixzAf0ynbFvA0K0gOQLzAPyEbawtQJJ2XkbPgfTrUBd5m8Z8QUSqxzDaGGeaz2IgKP1hyxL9nGSBG0kUFx5QvNYZ1WjZmABJyLqSMNlqBhaPd5Hzp_-cOY_cuWQYEKdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiKNHtnzMzuVh-fS7EukGgOXMYu8nyPdAJ0HrX3dsuOegbPWEAPF6an2VMBCVdd_F1ZuJlHpL9gyRrIDZmmjPnZr54qrNv2F-6zBgEiprlAQywZjVodG7yI1wECIT9kNrcTlR5fnUbE3UGPvaXAxFxuF6zH5nkDx1aThgwU_jysq8C6GtNhrOfMOAeMeYjbTinJgWRb5sDpygKx2K57RhX6LszHsAvsTOOgHovkviUpjHYnGARI73IxsXCH4t10PPM4OhDxCdP0motjVruRcB-h1575KchUre4u2mbATN_Pg5p9phCs5lbyhoJHk_7EmowIVdRzGmVtAfuy-kKkJrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjlJKT3LwHJjhzVcMNic3sKj6PrBpS3UwG2kQNKf-z_atXAO09iuOc_cs4jwRBE1niSkEukVqGAzcxCmj4XUq_YsZ3FXfYKREthYB-Gi365z2s3w3vlQgWQyUF7giSJ8-fTx_aG_ZnPHWyX5f12EEPxkBbDJdrDRyjqlzlawkVhOlyI6gOLUdKfZs19bfII1pqyAxHuUtQV81GJlRujplp7pt8ljRtNv0cBeUUYKC_OvkrlquukdYkAoqN8nptdgV-FQzs3Uy5IpTHCESWKv-bQVj5I8daPYVmKpZ4FwcCxrojBWJenCjrlzn4gXf6AlQ83MxvgmAGk6lZTxUb6abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=n9dIU1hae8o2UBj4ehgXMhtVZ_mM4x83zFoGjO4rcnVq0RP6QK19P188vYIBIxqAd4LbDwJ0jd3363hEQggUiZ4kOUi4hyMZE9xp95oZlKSsxQw4f5-DeNc7_-JduexOV-uzKeNJNC7iYHAbgy3HVdQ4tYhnxdD2tlw2y80PPie-TIlbn9IIR5oXd1YCv2Z6a_8xjRv2RycHUJq29G3lAlJL1xoaykJXLvI7qyGz6ek_u-gtAuvFXy-5nDgn05x_UrmyexoHaJA1Y14v6Gi0FGvJhhA1r8TrSNMauBx6-N6YCNOSIPhGggYoMmHBqb-iuaxibVDlCZktNFLSbQ_94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=n9dIU1hae8o2UBj4ehgXMhtVZ_mM4x83zFoGjO4rcnVq0RP6QK19P188vYIBIxqAd4LbDwJ0jd3363hEQggUiZ4kOUi4hyMZE9xp95oZlKSsxQw4f5-DeNc7_-JduexOV-uzKeNJNC7iYHAbgy3HVdQ4tYhnxdD2tlw2y80PPie-TIlbn9IIR5oXd1YCv2Z6a_8xjRv2RycHUJq29G3lAlJL1xoaykJXLvI7qyGz6ek_u-gtAuvFXy-5nDgn05x_UrmyexoHaJA1Y14v6Gi0FGvJhhA1r8TrSNMauBx6-N6YCNOSIPhGggYoMmHBqb-iuaxibVDlCZktNFLSbQ_94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=dGKwEXE-ZwzA5Aw-gB1Vq9kD5KK3eqEaKdpUnG_zRdr4QU04CKwt2FuSYW22EkFTCEmLRrj6zc6sclkR0zKPm0fNG2W6c7x_JA1e5LGVO8-VqpXnk3sj040QdmZejBb1ggIAsY3X9n9CzA_SumqBoi7DbQG-h0tPyREv_CLGB2PP6c1HySuLWSsMFUCkiVK-pO6ArpcY0w8DmuWdTsVSVqu9kbLepELUNl-ail6RYzdkJG053Z9L_LwQGZVDE2bKW95o3hqnS1KTXh8KeItCYAagqXgL4gkp-jsXd_dh3oBjqLeoTJYnec-Eo7a42ZrXDyrBpkgNgfFsU7KhaGnxzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=dGKwEXE-ZwzA5Aw-gB1Vq9kD5KK3eqEaKdpUnG_zRdr4QU04CKwt2FuSYW22EkFTCEmLRrj6zc6sclkR0zKPm0fNG2W6c7x_JA1e5LGVO8-VqpXnk3sj040QdmZejBb1ggIAsY3X9n9CzA_SumqBoi7DbQG-h0tPyREv_CLGB2PP6c1HySuLWSsMFUCkiVK-pO6ArpcY0w8DmuWdTsVSVqu9kbLepELUNl-ail6RYzdkJG053Z9L_LwQGZVDE2bKW95o3hqnS1KTXh8KeItCYAagqXgL4gkp-jsXd_dh3oBjqLeoTJYnec-Eo7a42ZrXDyrBpkgNgfFsU7KhaGnxzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=SGh16oTaj0W2OZtVaDGWIHmhbECiJgooQ-AauKiQWHDvOmP_opKcALTNLylrfhHG3eFJ8EJ7Q_PbE5go-iVH_f8P45ujO9d6o15T558PwZ8XnVOAirH8ydUBwNj6x5p8O0n5DFNl2GNJae6W67lRfpQHkz0eE_PfoQfdp5JviloB13M_pEnOnZF-zY4GHidnQMjsmaAUQHTjNBx2MD3t181DlGWBM60v_Lku3C3Gs-hwxkwmq4UhevAC83R3PAmEWxHVTdQPoJnF5VpxFfrYm02OsId2PavPAPFVD1MC3TYawEzNruj1xyYR_ArjzJ2DWOFBmBuwlvUMIr6ytaUgiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=SGh16oTaj0W2OZtVaDGWIHmhbECiJgooQ-AauKiQWHDvOmP_opKcALTNLylrfhHG3eFJ8EJ7Q_PbE5go-iVH_f8P45ujO9d6o15T558PwZ8XnVOAirH8ydUBwNj6x5p8O0n5DFNl2GNJae6W67lRfpQHkz0eE_PfoQfdp5JviloB13M_pEnOnZF-zY4GHidnQMjsmaAUQHTjNBx2MD3t181DlGWBM60v_Lku3C3Gs-hwxkwmq4UhevAC83R3PAmEWxHVTdQPoJnF5VpxFfrYm02OsId2PavPAPFVD1MC3TYawEzNruj1xyYR_ArjzJ2DWOFBmBuwlvUMIr6ytaUgiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=VUZJaF9DUfj9llVGDLQd5q8HCBeYFoG90m4-H6bkWmNO5X9j4y1A1_BUzquxMD5v02RabEdszfHea-5yh0B7-gnDwJmerUlN0dXJVoYv5c3pvz5NjH0YzDzGzvJ5FJf48gj_Tee8rqZxDxyiaDdIuXevbL7XUH67J8fU1XGVOKncXTAM8AAkXm4Tu1b_frj4KV3tE4_M8cSwjKiVYbKj8HDTaIj49LlJJb6vw4JHEZobZeVzXcAAT9DQvxt13vsT9UVl4YZCLpoSiHPSZjGufcngFo1iIx-XIdygg7ko9FNrx0J-Sh8yiXWQVpctNyJCo3HSCrmdupRMcRON06zmRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=VUZJaF9DUfj9llVGDLQd5q8HCBeYFoG90m4-H6bkWmNO5X9j4y1A1_BUzquxMD5v02RabEdszfHea-5yh0B7-gnDwJmerUlN0dXJVoYv5c3pvz5NjH0YzDzGzvJ5FJf48gj_Tee8rqZxDxyiaDdIuXevbL7XUH67J8fU1XGVOKncXTAM8AAkXm4Tu1b_frj4KV3tE4_M8cSwjKiVYbKj8HDTaIj49LlJJb6vw4JHEZobZeVzXcAAT9DQvxt13vsT9UVl4YZCLpoSiHPSZjGufcngFo1iIx-XIdygg7ko9FNrx0J-Sh8yiXWQVpctNyJCo3HSCrmdupRMcRON06zmRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmtMBttjFOfLoXxgFAhmI770Ylqh5QqR2GxL-shL5uXBUaB0LKCq2uRfb_fZwtcicxyAt5nZWdeShPtH72yjmDzfE551o6M56FVsfkLEAt5oRAmNCKF9wXu9TtGRIoTB9ltjmQ4G0uYlNey1dZYkb7W0qPUzLhRVEOKGnIQpmwcv81Fu5sgIT512tZ2kQTsB5JRHUhTnxGvs3fwEXW3F3JP0Q8M7XFpBroFWp8OVgYjWR5zz2U3UEY8Dx2mTUqT-1r3yzGk7I_D1a9AUanQMXjfplS9fEdTf0IH4jEfFDHikMh_kbB0InNaCPr6lz8QbhfOtl-k4BL2qvelkD_w0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkrJsLxWQPYPi9Wxz5yhLA52q-Vfy_FoXdkwgspTO9dZPXAkuyNVyVKG6NQS5fSjSvfyQx8b3O3U9ZYXF4iKxm7uDs_6A90mwETszrOea70E8AEu7wz6R61AVzmX7Yztu_mm6aYkqFBjCf63h15WdMhGz0XxuJHo-SVTA0TCy2earwLps4qqt_bH-vqNK0llvg8E6DMC1IANwQLbuwpNIAnDRRbDmhxbnDduJDSijRP6CF5Ioldgq6XP3rHjfGcOjW7lhPyzeOXoeF6BALbTHJh2M3OSD-sNU3G2zaalIy0WBacLR0WAVm2ZpyDx6-eFOf4XHTgPpiRG62JlhkFEiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=X0TWIpS0oay_g0m7MhVX-d2KBORYOl2kzal1huBitax3nuNbZLjJdMu4UFWFGjNTusAOkOIxLxFWd-5zAsEFV2xBXPYA06rCwI-kKydzsgYWC-j0tu18EXLFvECkZi1ZKbjnxDWAkHB9O7AnCKWJUOcAL-9N4bFnrz6KSObTTLgZfsjp8gtXLDSB9U-4oqP0jgdfzRULLYlv-snDMt0Vn7TFYZwX7sF2DpU-rCQT1fSXetedyccxWDF5Ok1TZvt8ee6rH8XIggim85mUgKDb4_r-qn48J2be3Nv7-falIho49qdJFltEJz3wNwrBxj0s7rBrW5A8_zA1jzUocQc9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=X0TWIpS0oay_g0m7MhVX-d2KBORYOl2kzal1huBitax3nuNbZLjJdMu4UFWFGjNTusAOkOIxLxFWd-5zAsEFV2xBXPYA06rCwI-kKydzsgYWC-j0tu18EXLFvECkZi1ZKbjnxDWAkHB9O7AnCKWJUOcAL-9N4bFnrz6KSObTTLgZfsjp8gtXLDSB9U-4oqP0jgdfzRULLYlv-snDMt0Vn7TFYZwX7sF2DpU-rCQT1fSXetedyccxWDF5Ok1TZvt8ee6rH8XIggim85mUgKDb4_r-qn48J2be3Nv7-falIho49qdJFltEJz3wNwrBxj0s7rBrW5A8_zA1jzUocQc9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZxgNVBInl8MdSPdIa0iypcKFA_aw9VYZebkf5bOmfjT5KRXDVxbnnh4BWWukv2yMIRcCa1m76DzxCNDdxILTAE8wY4USguusu-8N88ECfb9xXYV0SgvB04FrN16pDH7enGKiEiJZ4yRZ5LppxXmB0qhx-qSaVuvnza7zcluDh7ZDK2pNu5Dq1-DYxDS3eulBNFQ4ltrHrtlu6bC_j_6WjY5q2UZPJSSMqg2sIiwYNRFYzRI7fY9KoZwL9Pl_bfMDl50oELoJisymGc-u_rQhScwk_FVKtr4PjAOBHJLvPrXjxRuPnPoHIc8vHhbMIxl1d9RHqqQAjBxD3Sg6v_Zcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=I7uWBJcf345uK7NR8k1rE3NFunNgoio8dp2jRR7nC89BUUokpVQvTkpUjqEDPXWGHlvZd5pjEgf0ESbPtSjzoWj_QWzleXQXuekbWqGbu6CqSLfmjqO7VJ30VWfROnLMhVrarwEu0IFgPN5apo8fnhspEkEKO9xD8R44LdaEKThGcaSj2GXGprGyeOerzjNMqaCtl1IiXJmPBIYna7ZG9G2M7cRR5nAbONnJQCJchmXvT6_vm9Bb0J2cSDmIaCEQYRoUxZzH2j9tpGCaxbMDrpL9BPWoUr-3cTvfpUd7wy3Vxfo0Odf0PTkeUgf7Y09S9cw5P_g9zsgUN-Licbm_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=I7uWBJcf345uK7NR8k1rE3NFunNgoio8dp2jRR7nC89BUUokpVQvTkpUjqEDPXWGHlvZd5pjEgf0ESbPtSjzoWj_QWzleXQXuekbWqGbu6CqSLfmjqO7VJ30VWfROnLMhVrarwEu0IFgPN5apo8fnhspEkEKO9xD8R44LdaEKThGcaSj2GXGprGyeOerzjNMqaCtl1IiXJmPBIYna7ZG9G2M7cRR5nAbONnJQCJchmXvT6_vm9Bb0J2cSDmIaCEQYRoUxZzH2j9tpGCaxbMDrpL9BPWoUr-3cTvfpUd7wy3Vxfo0Odf0PTkeUgf7Y09S9cw5P_g9zsgUN-Licbm_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcqj_CBfZR_D2B_Sgke8GURu4gu_gFzB_TIGggUHEjHGPNYIbcFEarXn6sRTGTOsaxONbfLT3W7MFYItrHJk7PiJIVZZIg09Z_VaroIe5SkzdLqPVQYb5QH_n-x9x-VMN5Bi-dOQ3avfjypkF3ylb2HrMnZQwbfx47wR6Rpos2hXGTQ0lPvUxnUeA7Frte2gvylryykJtU-k2VX7ASBm3dOdXHOmg_W17qKgUlca3ntG2H4F8OBCCbTkpdtnAudfRcalpE2IdvHTcexhOuQwzEAQyfkVPSg9YkhdOhmhE8tucCNjkV-D0SfdlwD6ac5tSeRmzqsxQSag-TqVgF5oeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs-rFUW9L_lHEJKP2oHZXrFUnDQr_lB7MyUNfiLk1H7-0GLPoWo6dNdWtlmHAwdFpAg5F-ox-gLRAPXvS_fd0D0BQ-cq5SDm8Q8oQVWfQQoPUzRIrTvM-xv88ZjwvjZ9NQf_fOPchRUMTzYyqHNobcqoPX0qqVceC2gAGm-vnICDKeG_MJsX17KBu6AseyBPSuArlcrSFhYIeOfjMS9d4xFo4wo6w2WfuWD_gmd9bfo4QBx0LPzWxhkpNGvdvaX2Oi_usTg7M7TYLQZeA71Sp5VPKjMpMrqRwcIf2rnVjIf3znPaGDYdOwy1L5Wlej6ih17OsvOJoki3tzA0278UZA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=GvrsC4-6Zt84_6FLFRH3L_OBQ2GNKB6mtVx7R_1y2FDuVE1Ny-0p4T_rMV4ICgJTnHO1mHQO1j9BvKka9VERr88gBfWGVJW6UtvA2DQEreTyeA0n4nwb8IuFXBKNWrGLyUq9bY6PyoEZbRsaeLsYoBC7ik3ZyOJLvWsHFoCOzVlCTdjDQE81mrZh0jCCgNPu269TlgP7y9gbfQR-qHk_ISs8HZkQd0ZuWyQxTOeZwk55HyGP072JI7SYr-mZAf3Qjjhf2YKaDV9KOcuUGOOckiVTir-KiFmXqaRe_7x8WWIdbsnFd_eGyuYqnMKqQ07Qe4-Wi2R8JXOyP9fQ3Mj62g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=GvrsC4-6Zt84_6FLFRH3L_OBQ2GNKB6mtVx7R_1y2FDuVE1Ny-0p4T_rMV4ICgJTnHO1mHQO1j9BvKka9VERr88gBfWGVJW6UtvA2DQEreTyeA0n4nwb8IuFXBKNWrGLyUq9bY6PyoEZbRsaeLsYoBC7ik3ZyOJLvWsHFoCOzVlCTdjDQE81mrZh0jCCgNPu269TlgP7y9gbfQR-qHk_ISs8HZkQd0ZuWyQxTOeZwk55HyGP072JI7SYr-mZAf3Qjjhf2YKaDV9KOcuUGOOckiVTir-KiFmXqaRe_7x8WWIdbsnFd_eGyuYqnMKqQ07Qe4-Wi2R8JXOyP9fQ3Mj62g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=qWq6O6YOZZ4lf03wrGyYMx3k6cbM4xf8AAielpk1uiBl0SqVpwWGU2E3C8mtPB8wVKbnOX_1iZcuY9xO-XCOB0AQBEDExONiIyr9lrlS90NPegHQsSN_0r2UD46Dny_pAckz9T7sgq1q_w6b6pMnH54acJXEZqXodkb70yXVykxMPVtwQ-OPug5jvUSafXc6DsCrxMIrN9ikT1YT2CHLflQPcS56rBbdkTHAPmENI2HzR23-ZReTZrs6kMckYVKH2kMjPLtFcSRHONHBwkiMgjVxHdIvmnRodLDxm_GLvRfDH9hK2RntZhMxPN_EKBsS8Qv4jzEJXNSa4CosCOQJlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=qWq6O6YOZZ4lf03wrGyYMx3k6cbM4xf8AAielpk1uiBl0SqVpwWGU2E3C8mtPB8wVKbnOX_1iZcuY9xO-XCOB0AQBEDExONiIyr9lrlS90NPegHQsSN_0r2UD46Dny_pAckz9T7sgq1q_w6b6pMnH54acJXEZqXodkb70yXVykxMPVtwQ-OPug5jvUSafXc6DsCrxMIrN9ikT1YT2CHLflQPcS56rBbdkTHAPmENI2HzR23-ZReTZrs6kMckYVKH2kMjPLtFcSRHONHBwkiMgjVxHdIvmnRodLDxm_GLvRfDH9hK2RntZhMxPN_EKBsS8Qv4jzEJXNSa4CosCOQJlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgRgUQbe7ah6gaB6_GS4vCYca0pJm00plntqzkuEZaTrVEuSRQfu9j88kWloHERam7WKsi-Kn4jEci0tK_ocozB817qPSukwWFQPmE5oyDhwapkjYng0oNDbbt0M2UJCR6bXipQgDpGQc8dColoIFJ_Hw4rx-owcpcrIu2pjlNUdfm89m9HQs7YIfbj7Q3wT9e7zXyJRzIpAMxCmFkUG26L-Q6X_A1PWcERMqFCifXxD18Uhm6GTl9hqhWpfuV2JtjwaVmpv2u1yEwtEoYOrsEtQjFy89emvAPjsQM7EEZ3Tp9GogVikTN1nZaI5OU6AVv35Y1HTVvheh_HcI8pIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krGOn5f4k8L970-EkoXU7c6ENomQA7o_I-je4Aphdiabt0rXgxQEYEbE7whnkskQiycJW8_sIyHowTKxmy1T3b-eTY1zAlISfGIC_BVoOXQT1ZtyF3Yn2uoJWRrF_h4UlIo02XI3x4vfni5Vu-HQoWtP3dodh3mJ8_obvwzCqLbjihqwwBNosQYuq1nwS5RPXoKQ6yCoZktg-jmajVVleUVXc8ZkFGLI98O66Q_DLiGGzo37WRpwjaQ5UOyPp3ME277MnuGibQ5XykB3SuL8obcPwNoPtTtc5cynRvbPtja3eO7E49hwb5CNnExQ7SUuN5HA9g1lyl6mp_USUKejQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1LHqTnYJQHTBHxtqEZUJ5hQPFA--oEGKavMb7FfQIKZM5XxCpGh8XiGHTWHpRu55UPZQF2074Q0EYHRX6fZt08eyHlkZR0J-z06zhb7YGa_NFQ1hEdVrYkXGs5vsLg4yBypX7Z-TFkVARsR3jK7QVXAYJFKhWPhfK8aZNboFsJuJORs7PFH7wluleNy0YqTQyb3_47nxdsEn_ReP_WDhJwrNb0CxVYQ81I7kiC5SbmZNIwMEJFAlD3TAEzmPKW2g3hZQMNn75xhrjn0sVKZHs9ss4VuAOzU0OpQ55BrdUSTD5J6anKWRF-I98y-aVjbZdOzOg6d_9hcZTwA6CRe_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=Vw9ZB3OAtr73EjwW_WLpPHLeOuBG6I70ZePl7ymwvOREVqKtC0nYe5bdPmkvYCjQXiFgJiLUPnKncVu4JV-ykOFGFkpJM89NVF5oigzYTyTX34XK8PLj5dCL1_biSVqWla2HufBAbHioZVnGqrof2Tv_lQ0vXvZQjHepMQQWcMpYkc9mgCJvRhOI8RkAOHX9pCcg7xa2ntY6bshrTNY8tvSLq0t6sYqHC10SlE9GBTxnRd5zYm0gKpaU3kcCm2ZLW6WVm0upSiIYp_PEOOj_HtFyRRfII6BIeV5qF9e7pzCUIsYz9dQD2Uv6Vib2FiCDZlNWqF5vadMvKJcC_6WHRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=Vw9ZB3OAtr73EjwW_WLpPHLeOuBG6I70ZePl7ymwvOREVqKtC0nYe5bdPmkvYCjQXiFgJiLUPnKncVu4JV-ykOFGFkpJM89NVF5oigzYTyTX34XK8PLj5dCL1_biSVqWla2HufBAbHioZVnGqrof2Tv_lQ0vXvZQjHepMQQWcMpYkc9mgCJvRhOI8RkAOHX9pCcg7xa2ntY6bshrTNY8tvSLq0t6sYqHC10SlE9GBTxnRd5zYm0gKpaU3kcCm2ZLW6WVm0upSiIYp_PEOOj_HtFyRRfII6BIeV5qF9e7pzCUIsYz9dQD2Uv6Vib2FiCDZlNWqF5vadMvKJcC_6WHRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP21IjL2sVxklgEccAQGvXNCsu_fWD9OWMoo0T1fmfZdERnFZVPXGVKEuKn7xzVsweoCsKjEZ1V2yOf0lMzcoF_GH_-4Ey1VYaN4-wBn6RGdlAtTtx9EiM6SJYLfObIT-3CPwxkRkT22B8522W2vbiGq9_9KC9c6NfjG9VQwcVHEinBJqRMCh2ZPxQrtVzUgWbNq3_GeQz2HCg1XcF0VDPE1JjMHeGe5kCQ_bxpG7ZxNLfABrCzOnrdTBdoHS5VjV8Ezf0MzHQqRNNpB0ksWLqM69mxRGNs5sHJKFZIcn6UH4z23UT5jANbRp6-b94my_AL0QGWdsLRoBD8opRlphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
