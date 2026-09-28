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
<img src="https://cdn4.telesco.pe/file/LxLGU3_Qfon5Z0btmDbTYLDm1CaXXLiNwU4BCrQ3EWPJgBbf2_M0RKSINAoKabXP_m1bYkXdaK9d7f9XGLAXYSeIPYcXfTL7QyF9JZcqDw_wuU8D5sCCfd2grUBgrRsGM9KzdBIaPOZc34FpSfThquZRx9ePRaqA6oY-Omi7F0f45pPNDVpZNmwoTjWz6SJfoSflxG6inVZnuiLBoGSpr88YSh7FuEHKa64e2SJajcLgn1fGI4GpLk6TXeKOruxt-QcZAdkgxLweI5u8bnBMrYRHLzMjn9bPIR9LRLppxz_EYDC2KU3VVrqceWJGYPzjeMd3c_JufbuVnOfOnfTaQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-149837">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVc22hNlSs8jq-c0_vMxydkHZt33sfaMbgkEDJjOOEUVSNfM5v4_OfiLDC2e_JPK54ic9mCB-VSVtQPVr0NsPcYHLvdg0kZZyxCzz4hCh57D4s891McKqzzsswyB6pMuc8u4F0wUoAR5-jQqrWrLIGQqc4hpUMnqCZrLWjrxzaiP9ktxLBYjQFD-o4aBTSCL4D7FwQHlYWkiOybl0YlxzldCSbnJUNxGlwuSr4z8ZT3Avp34JZPrzw8HnhpfaqeyW0gs_DhK1XLjcgj0yFxqd-P6WWOveEITNuh2wwHELLsYA3a1ndHvfjaNdQ4kURd2OiWUwCqS3o5czK-y6Esl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رکورد تاریخی نقدینگی در جهان
🔴
حجم پول ۴ غول اقتصادی دنیا از ۱۰۳ تریلیون دلار گذشت.
🔴
تزریق پیوسته پول در ۱۰ ماه اخیر یعنی تقویت سوخت طلا و بازارهای مالی، همراه با هشدار روشن تورم جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/149837" target="_blank">📅 12:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149836">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlvDje39HpuzUt738_x7y1vHrOPg-vdjzjexxxfNxtMqNNZPfykAwqHdYN-3bC2buvpF_yDM-bTOwdHccpdvEFxlH6DIs8wX-f_b9pDoNqlZCiEXea3U3V_p3pZeXZBHohwr_fCbRvdBsw3blCc9clPZXzQsSRTULSKhP7rcWwf2128a1iTmOavOS9Hvi7cKcQxg1rswdfsk7Zbt2kcgP5g3K0t85jALBqMron7kgZM7tpkgSq1b0yW6-cXe_CO8Ziq5u4KMxe1DNPvaTh9hGJahyPj-EnHHnD1HcrWF0IU3hKfQ79JxyO6ddWeRz6KmXs5mRFc1nCjXxqB8T2jwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای حوثی در جبهه "الأغبرة" در منطقه "المضاربة" واقع در استان لحج، پیشروی می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/149836" target="_blank">📅 12:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149835">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
هشدار جدی به خریداران نقره و مس در اپلیکیشن‌ها !  بزودی اداره مالیات به سراغ شما می‌آید...
💠
قانون‌گذار فقط معاملات انواع شمش طلا و انواع حواله‌‌های كاغذی يا الكترونیکی دارای پشتوانه ۱۰۰ درصد طلا را معاف از مالیات ارزش افزوده دانسته است
💠
ضمنا این پلتفرم‌ها…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/149835" target="_blank">📅 12:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149834">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d9df52eb.mp4?token=AiOzffkz4zBbyS3UjldWBKu3JfMLFZhWTNLa0Qb22w0YRQt007OMC36Ux1Ks26LEShjxNM5hsDzh-oF2uhO6Svb3ePBHA63GaWx58MPk3T5nE26p3ojaGPFliJmNSUbzDMHOSaxULvsMQcz20EKe2nuwBua08zH1OhKUcY_SOczv8OBiCpTxIkUuszx4pdYOdYr1Wkx09yxnU1KpjIHAt5D1exuPZ5NO-a--zyBbVoKHG6AhHj_O8-I5k6Ku6enEr_daO264asoaIznZsGxSqEeoYoeAHGSA9D8BDAr51ua2u3oIynu5PVR-PHWow6HFjbY5DAQ_Y5AVUMtmuRpyww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d9df52eb.mp4?token=AiOzffkz4zBbyS3UjldWBKu3JfMLFZhWTNLa0Qb22w0YRQt007OMC36Ux1Ks26LEShjxNM5hsDzh-oF2uhO6Svb3ePBHA63GaWx58MPk3T5nE26p3ojaGPFliJmNSUbzDMHOSaxULvsMQcz20EKe2nuwBua08zH1OhKUcY_SOczv8OBiCpTxIkUuszx4pdYOdYr1Wkx09yxnU1KpjIHAt5D1exuPZ5NO-a--zyBbVoKHG6AhHj_O8-I5k6Ku6enEr_daO264asoaIznZsGxSqEeoYoeAHGSA9D8BDAr51ua2u3oIynu5PVR-PHWow6HFjbY5DAQ_Y5AVUMtmuRpyww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا: «ما در اطلاعات و ارزیابی‌های اطلاعاتی می‌بینیم که روسیه در حال برنامه‌ریزی برای اقدامات خرابکارانه بیشتر و حتی حمله به دموکراسی‌های ما است؛ اقداماتی با هدف ایجاد شکاف در جوامع ما و ترساندن مردم و دولت‌ها برای جلوگیری از ادامه کمک به اوکراین.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/149834" target="_blank">📅 12:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149832">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vh9a_yiisdzJxGIRZIMtFPL-PBqT0x6m8tsgxr7FtZmDfx-HjEfX8sXVGwyBir0Yzq4iqg9RkQLtIJ7R_9PCDnxSzN3MgnZe4-5knh8ujXmg_t8U1QlcK11i-eMEixdLnYhDQp0nUKnE6spVwR3DvpmGCXyRn51oGUpNxR1PYDoWuZybV2GQarJwMu3kXcamuIDwbV3gdfKQt2saeSZaDAM5PCFLfDTVdbrlzhsNPw-X-Hb34r0JANCQZatz-OJ488UOlWzDejHu3LSfrj_nueOYjCSFbMkPGz4fa5DsMvNP7M9toPnLI1AbTGNTf72S_SkPrNHjZ2z2GOY1txPdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckRNa_WC8dNolJ1T0lcxKVTbbVO-DPCRv_GC1Gst53Q1ci2O8-Q3MmEyRD2CipxblmmfEkdWgsqi2k_tGJjTgu3ZNk2p7Sryr612gVgPjToqXICwQx279sumUlvNnrTKfIS1PQmDK1iAcM-GJL_5nm_A-zwzhbAhBOoLHc-utiX_VDQUPpY1S2WDsad9bPZFBNVQAeRlxZV8i_d5EjKUSWcp4ENAENNisUk4GfsnRW4Ir2B8-kHslPTZjPqEsEy3KGY-fIwKqFLjuU-m_vypyNzHTm1abD0OIzjlvKZtNsMnyoOsYD4DXLeT_ZPR-pslkubS5ZsNjumqtxrvRw7xMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از زوطر شرقیه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/149832" target="_blank">📅 12:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149831">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b4864699.mp4?token=s-GAsOM0OEXHnm4r3yS1rE1uHG7RvB-QR6dbTSRrZ5ZisDUamKD4zLjJSfOsZ7uG7WoV6k7RjwJYcgk0KMgC-GZ_ELGNJTuh6G5RfG2Rq8xXQHHcj4qxrjtOCnZ1KdNBtf8PvrZQ1jGvc4NPTbZmUgNlkVnY4xG6BGR1Rew6EmxkDU-qLIHAFPLKdCpgwcGzj_8hKm_3Oxj4CjmQZkquUkOt3I_LjsE1QuZCJ2iJ9YKMUpB54W0dl-a9sEsF-HLuAZKWKmrZVltE67SafA_v48qQu7jvNaAmeTcyWjYBjj4kPGqjUTCl4lJAH8hUj5-XBxE_-mU0TtRs7fIecyBXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b4864699.mp4?token=s-GAsOM0OEXHnm4r3yS1rE1uHG7RvB-QR6dbTSRrZ5ZisDUamKD4zLjJSfOsZ7uG7WoV6k7RjwJYcgk0KMgC-GZ_ELGNJTuh6G5RfG2Rq8xXQHHcj4qxrjtOCnZ1KdNBtf8PvrZQ1jGvc4NPTbZmUgNlkVnY4xG6BGR1Rew6EmxkDU-qLIHAFPLKdCpgwcGzj_8hKm_3Oxj4CjmQZkquUkOt3I_LjsE1QuZCJ2iJ9YKMUpB54W0dl-a9sEsF-HLuAZKWKmrZVltE67SafA_v48qQu7jvNaAmeTcyWjYBjj4kPGqjUTCl4lJAH8hUj5-XBxE_-mU0TtRs7fIecyBXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین:
«ما قرار نیست در دنیایی زندگی کنیم که برای انجام تجارت به شیوه‌ای که می‌خواهیم، مجبور باشیم برای جلب رضایت چین سر فرود بیاوریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/149831" target="_blank">📅 12:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149830">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">طلای 30میلیونی
‼️
با توجه به خارج شدن قیمت از مثلث  عملا اماده پرواز شده و با توجه به قیمت دلار داره به سمت بالا حرکت میکنه  فقط تنها دلیل حرکت اهسته طلای ایران، ریزش انس جهانیه وگرنه قیمتش باید با سرعت بیشتری حرکت کنه   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/149830" target="_blank">📅 11:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8M2lZicoCHNy8rXMHV9sSD2T5Gk4vcL42vwGHNSPenhUfNQBaLLdOQvvIhMc6uMTVTEr0NUChX0fuNj9kd-ulC5fQrY7-O0Ixg9XrtOi2eCEIkaU2Qqo6knxBY6woNMjpyvDpGlaSdfVlw8ovYrQiTvdFvDmH5swVQMjSXtVsvOa-VcwdsFt1_z6QMAvjK37EguWOQ1tyqGkQ2OQuCsl6_8-caQJ1Ngt6SnHS5Ic69j2m63a9v0SIGTP1Q53-KL7lH6_OIXI-U4mzTBix4LVOlYNWnN9QtDG6D4rgkP55x65sXiA-JbVvjBTCc9huuyJw43-6hmW7VjvsfZ7Il2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ مدیرعامل خبرگزاری قوه قضاییه به رسایی: وقتی قانون سراغشان می‌رود؛ می‌شود مصداق بارز بی‌عدالتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/149829" target="_blank">📅 11:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149828">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از مقامات:
دیدار ۴ ساعته نتانیاهو و بن‌زاید در سفر یک روزه نخست‌وزیر اسرائیل به امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/149828" target="_blank">📅 11:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149827">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر دفاع انگلیس: احتمال دست داشتن ایران در حادثه دستگیری پنج نفر [با مواد منفجره] در نزدیکی پایگاه آمریکایی فیرفورد؟ هرگونه گمانه‌زنی در این مورد بسیار نابخردانه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149827" target="_blank">📅 11:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149826">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
واشنگتن: به‌زودی ساخت سفارتخانه دائمی آمریکا در قدس آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/149826" target="_blank">📅 11:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149825">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na1TyskbXotyMRVnDyW6Y_Tlh2mb-yjXFhiIrYEiIhCBzMbAudc0s29REb9qU_KcXXEZ-WRilskZrtk8KySa8fyE87kaUMZTtvKMxfcXFkFPu-ZF2NhmcvdjS8t1LIoyyl0GGBTgnGNnKxFDuL5SUCrg4Nlsj8MZ0A1FiyZOg3Ofhff4Koz8fzd4OwpKQ97YLtE_RqCvQ_gNBmSrqk3_dEZRVKTiw2gpnOoxXX9XsFAOzWOsSuG97t19ah2D849Y-CpYKQ3Jlzz2YkDgk77cXno-fWeypXwshVFjBVG-gcNFBbkL1B3CWsUbOzYVtJUPkeWbxOs-GoXBLfeZUnEMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی اونس طلا ۱۵۰ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149825" target="_blank">📅 11:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149824">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b519bfb392.mp4?token=YRZ3pdSC6C-HnYPB5Z94b3PJIKJ3oIEqym0P31hz1hJH0Ny9-vynIsIeqvp1nWkMoPs5mWN9S-yy3OoOWlxUyEYlRD_ldkhHM1dZJAZxBJ-WE3Plt9GbOAl8iNsJQYTVSTgaSJJkZvQYeL97DOIfKsZfZO0K-uPCgrhcaoGwC49QcLvZJgCjPzwzNujJZfeLSq7UP3jlxPmdzY5H0iTjoHcJhdAKBv_ArkHXWMbUyfZy0ZlhVtucAuVoCMZdKMbV0pvGRa9MD8yyTHvIijFL5-ZOX6i3q1ZDUXvc0YuSIeIGQ_LH882fbrA5SK0G3LVEljKa7OXzZP5SPFdWqwBH-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b519bfb392.mp4?token=YRZ3pdSC6C-HnYPB5Z94b3PJIKJ3oIEqym0P31hz1hJH0Ny9-vynIsIeqvp1nWkMoPs5mWN9S-yy3OoOWlxUyEYlRD_ldkhHM1dZJAZxBJ-WE3Plt9GbOAl8iNsJQYTVSTgaSJJkZvQYeL97DOIfKsZfZO0K-uPCgrhcaoGwC49QcLvZJgCjPzwzNujJZfeLSq7UP3jlxPmdzY5H0iTjoHcJhdAKBv_ArkHXWMbUyfZy0ZlhVtucAuVoCMZdKMbV0pvGRa9MD8yyTHvIijFL5-ZOX6i3q1ZDUXvc0YuSIeIGQ_LH882fbrA5SK0G3LVEljKa7OXzZP5SPFdWqwBH-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین: «ترامپ همچنان می‌گوید: «ما به کشورهای دیگر در سراسر جهان تسلیحات می‌فروشیم.»
🔴
او حتی در مقطعی از شی جین‌پینگ پرسید که آیا مایل است مقداری از این تسلیحات را خریداری کند؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/149824" target="_blank">📅 11:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149823">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647255f9b3.mp4?token=Ybmpbunk1JVAS5L0i3ELUSab8KXr6YmZfn3Flu80YMZvcJlj0kYkMDIXDNpM51wpQgLgO3NgsK4fVZKLAX-Dni3xlW1eQ-3rDIHT5E8I-STa-DvJGG93XXJFQzjWYgP2Uz5BErgQOcIrf-fzmcBJ4eXVo1s-42Vi-wz5OcHbueoH3gzzEK43UJQF7a1ZkJLP4sL7Pdgp6EbE0ICedKfSajcXiDt_kPBS-r53o4FkEO7mPbRpQJooiiM7Z03nFG6RTLGN-CQu6FU3mTVRGaMDKttxJE2XCE3G4AcbPaV0vy2cp1Y8iLxNY3V7dQwq-ZZVauyDfgGDuJ0YHcHyQz2avg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647255f9b3.mp4?token=Ybmpbunk1JVAS5L0i3ELUSab8KXr6YmZfn3Flu80YMZvcJlj0kYkMDIXDNpM51wpQgLgO3NgsK4fVZKLAX-Dni3xlW1eQ-3rDIHT5E8I-STa-DvJGG93XXJFQzjWYgP2Uz5BErgQOcIrf-fzmcBJ4eXVo1s-42Vi-wz5OcHbueoH3gzzEK43UJQF7a1ZkJLP4sL7Pdgp6EbE0ICedKfSajcXiDt_kPBS-r53o4FkEO7mPbRpQJooiiM7Z03nFG6RTLGN-CQu6FU3mTVRGaMDKttxJE2XCE3G4AcbPaV0vy2cp1Y8iLxNY3V7dQwq-ZZVauyDfgGDuJ0YHcHyQz2avg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین:
«دونالد ترامپ، رئیس‌جمهور آمریکا، در موضوع تایوان به‌اندازه‌ای که من تاکنون از هر رئیس‌جمهوری دیده‌ام، موضعی قوی دارد.
🔴
ترامپ تاکنون ۵۰ درصد بیشتر از هر رئیس‌جمهور دیگری از سال ۱۹۷۹ به تایوان تسلیحات فروخته است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/149823" target="_blank">📅 11:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149822">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwvFVBFkbbYfJIFIMFSONJUHs9uS2IP_xUxXwFhkFAW9cTg_ESjUfBzoePvO6WKecluU6WXPVnvSNYZlqzx3cgzwXWw2mFiB8urFGpCTuuaiq2iWU_peqTXFeYH7jXNwO0ONflv-kRkyQVSQF4-bGtArZHhfCAzqVADxTK5gXXzC_Ub19jhD4Rg8bMT_uf0ouG3yKYSMBT_kcVnp6lYybujoYErprlHJxzwdI-rp1Gv1vJ9ECMkRw_JdIlQu8cYMCaZcAogaRFBY7RtruknvpYagvu80pBSyGujJU9RFlaQyqPVq0U2OBVE5AXNfiXl_ksbG8tgzmS6qYEbMl2V-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی وارد ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149822" target="_blank">📅 11:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149821">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f86249bb.mp4?token=WrfgLqx4NGVRqvwSmqELNDH_RBCDN-G1bAy3IY2bb_-KEaBYloWLDA7V9NQqAq-53Clvkp5jTQ3-YDZ57x_KUvkjoKMFP7eAmjVqli-KzTv53Eagh_n1seMB5QBGrFINash_FeMZ3rEpVIFKS_DX6NK9kPF0dpImpAAnwuZVt3v0nISGtHFbDoN5qhRlIAsITzGlgkC7eZfK50-ifTKDPlyO30z8Dv20fnS8a5qjGLZAKaA07qSCVng6qmnquEtyKLPqDG2LArT-GeXNCEMEo9BghVRQNaVZeBQMhsQ2n8Lit5jx4FtXqjktUkwz8XVt87vMepwnHJINEZbHYTfIVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f86249bb.mp4?token=WrfgLqx4NGVRqvwSmqELNDH_RBCDN-G1bAy3IY2bb_-KEaBYloWLDA7V9NQqAq-53Clvkp5jTQ3-YDZ57x_KUvkjoKMFP7eAmjVqli-KzTv53Eagh_n1seMB5QBGrFINash_FeMZ3rEpVIFKS_DX6NK9kPF0dpImpAAnwuZVt3v0nISGtHFbDoN5qhRlIAsITzGlgkC7eZfK50-ifTKDPlyO30z8Dv20fnS8a5qjGLZAKaA07qSCVng6qmnquEtyKLPqDG2LArT-GeXNCEMEo9BghVRQNaVZeBQMhsQ2n8Lit5jx4FtXqjktUkwz8XVt87vMepwnHJINEZbHYTfIVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین: «دونالد ترامپ به‌صراحت اعلام کرده است که هرگونه کمک چین به ایران — چه در قالب اطلاعات، قطعات یا تجهیزات نظامی مستقیم — کاملاً غیرقابل‌قبول خواهد بود.
🔴
شی جین‌پینگ به او اطمینان داده است که تغییراتی در این زمینه انجام شده و موضوع در حال بررسی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149821" target="_blank">📅 11:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149820">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eea1b3b65.mp4?token=YyUhdkriRy-SwBZgpAScABJ1vJhvPvImGQX6CldogrUz-i7vWB5bz2fhvbYAKa6rGQIaRXC1t0Fq-K98F1Omoi1ihDMOw0i15NTLd4nNEfETWx5oFXJ2T3zlF0IKuq_XcJXSmGnvxqO9YfmF3q5RQs8zxHCgwV2Cst9zIPDwaqTwbEZmdAJBa-qMFB0mwSNFNbDXNBViUctQrqDzIgBHVZfU0Z4hzBTOp5FUA2-Rd189fjyTn3dvup2bYEk0iL1uZoenHh2YEAmOIb7ee-noMGK5buKQhU9uL7zj2ySUt0FEEikm5qGFdz8fzxwED32IhadosjMrojURWy84bVkxBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eea1b3b65.mp4?token=YyUhdkriRy-SwBZgpAScABJ1vJhvPvImGQX6CldogrUz-i7vWB5bz2fhvbYAKa6rGQIaRXC1t0Fq-K98F1Omoi1ihDMOw0i15NTLd4nNEfETWx5oFXJ2T3zlF0IKuq_XcJXSmGnvxqO9YfmF3q5RQs8zxHCgwV2Cst9zIPDwaqTwbEZmdAJBa-qMFB0mwSNFNbDXNBViUctQrqDzIgBHVZfU0Z4hzBTOp5FUA2-Rd189fjyTn3dvup2bYEk0iL1uZoenHh2YEAmOIb7ee-noMGK5buKQhU9uL7zj2ySUt0FEEikm5qGFdz8fzxwED32IhadosjMrojURWy84bVkxBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پردو، سفیر آمریکا در چین:
«شی جین‌پینگ در ماه مه موافقت کرد و اینجا نیز بر آن تأکید کرد که چین از دستیابی ایران به سلاح هسته‌ای حمایت نمی‌کند. این موضوع بسیار مهم است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/149820" target="_blank">📅 11:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149819">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر دفاع بریتانیا:سریعاً و بدون بررسی دقیق، ایران را متهم کردن به دست داشتن در حادثه امنیتی داخل پایگاه هوایی ویرفورد، کار عاقلانه‌ای نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149819" target="_blank">📅 11:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149818">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی جلوی دلار رو بگیره
‼️
تتر از ۲۴۲تومن هم عبور کرد</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/149818" target="_blank">📅 11:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149817">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqutPUH69mEWf11L5r2qE3CaubmPOBlw284xBHCyz3JlpYzipBBKq7UD9B2vqSfD1bEnH0tjePnRELbZ3qs43mhb2qpwijsZbzzmhobLKnYNalz_U9jTH6rlCL8lWcYqjHJmO_f7kET2xyxdJnTpIXiC7VdOB304hUJrBXkqfzL_K9N-RyakWOcqSQo_sUW8niHF-Yu7Cev-V42kD8dENK1k-Dmsgkv_MisIARvgbbdX4Vm2IKPrp5HMxLfRfrAWkcZN-bqjCDzqbi3NgtUXwVZN1FmvWbXBJ2QwZ_-3KxO-9Fn5dHaO8vvBQKfakKh4vSuUobc3Zc0jZRyt7xHGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی: فرصت آخرو به آمریکا دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/149817" target="_blank">📅 11:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149816">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2niQLvOQvTjpUmZ7wzkt-b1KjbGNLz3vS0RcnuMzbIHSOQ4DQjgMKZe5Zr8K9imDcaVLkSNRGehUtGAatP1KQ3EXIZMmZ-VEr9JexZyFeHuVyPP2dkHhAeLaR3NncZl_-LNVoDifMcQOPy2-Zm6H_dsPRbx5QgvTPcSBo8fpLcNu_Gj2GS0yiXFLQ6YlkDlSHs3XfoOO6X84gl9nvR8iGPJdedRFjrV17XF7KY4ny5_EiYCx4hP__PX_uu5hFyb8qGPJyrHpLOwqwUuR12lu8sGz2eAKks5TQu5QYfoFvGKOVoNch0lTT97pAk1xAMcJTI8hSlCm5u4RQKWL3XVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران در زیمبابوه: تنگه ترامپ باز است، اما تنگه هرمز نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/149816" target="_blank">📅 11:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149815">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بانک مرکزی: صدور چک رمزدار از فردا (سه‌شنبه، هفتم مهرماه) در شبکه بانکی ممنوع می‌شود. بانک‌ها از این تاریخ موظفند برای مشتریان خود به جای چک رمزدار، چک تضمین‌شده صادر کنند
‏
🔴
تبادل و واگذاری چک‌های رمزدار موجود تا ابتدای دی ‌ماه ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/149815" target="_blank">📅 10:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149814">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
الشرق الاوسط به نقل از منبع دولتی عراق: آمریکا به عراق درباره نقض تحریم هوایی اعمال شده علیه ایران، هشدار جدی و مستقیم داده
🔴
واشنگتن گفته ممکن است اقدامات تنبیهی آن، هر نهاد یا فرودگاهی که پرواز‌های ایران را تسهیل می‌کند را هم شامل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149814" target="_blank">📅 10:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149813">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بوی جنگ به مشام میرسه! ایران شاید پیش دستی کنه.....  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149813" target="_blank">📅 10:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رویترز: صادرات نفت خاورمیانه با بالا رفتن تعداد محموله‌های صادراتی عربستان، دوباره افزایش یافت
🔴
صادرات نفت در مهر ماه به ۱۲.۸ میلیون بشکه در روز افزایش یافته؛ با این حال، این رقم همچنان بسیار پایین‌تر از ۱۸.۸ میلیون بشکه در روزهای پیش از آغاز جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149812" target="_blank">📅 10:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTDqsF6Ll0Oy9VjAVKrRln5X3rIpyZ8A67HtPW52iY3h_qO0N1Db4YMQnG3RNmJD4n-u1Wz8Z7lqJIezvroPruzfHu1DWk8sogLqFYDQhtsed6UM68wfPp5vn6HN3VUYlbUfxb9rQuxcyTyFWHqm1Jb-K0ewJ7JXoEE6ULyU70qh_lzZVLiRzE_PpQf0Y3WHicJXZnxUrQHPlaPpZJGKsh3IaFdAd6dCwrZwkHPO2YOyLTbMhnSZMvPVkCUG47LFoEuG4Nf9maUgWIahzWQ5lhNxVpPrpgshqF2pxTmhE7y0lvxwFwB-tKDa12P0c-c3se90EBJv2y3UD0ItUs8_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر ۲۴۰ هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149811" target="_blank">📅 10:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دونالد ترامپ: «به‌جز نفت که قیمت آن از دوران دولت بایدن پایین‌تر است، همه‌چیز در حال کاهش است و دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم، چون آنها به‌طور کامل از بین رفته‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149810" target="_blank">📅 10:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a7312bfe.mp4?token=JuyruXYd_CUVyFWPgAFAXNvpUz2HA-_wiLmDkRkoo_wpfdTUAvg5Db8xNXdRxU0dAqz_S80fiuurWIAdnyD0ZqQFoIlIKTTx87SkM6cfALONI1MGZVk43Njb9mk9jC6SXQk46APjG13G0LFSvrWDZTQ8mRPjyYjsceqnI4B1Ml8cs8NgIG8nJCHGjgnrCOSkBZ5wMO3AbNtkY4DdmXQxeeUBDNIC8QJLJ98KjXghWX4mitKIzEVwzczL8UNdW9wQHM-WvFg1ssX3EAr66R5mbXOdNGKQuSNMrEL6NfkijFubk_7UeoZ4g6yARXylhCtxLXgnLCTExD64rfNsfYQ7MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a7312bfe.mp4?token=JuyruXYd_CUVyFWPgAFAXNvpUz2HA-_wiLmDkRkoo_wpfdTUAvg5Db8xNXdRxU0dAqz_S80fiuurWIAdnyD0ZqQFoIlIKTTx87SkM6cfALONI1MGZVk43Njb9mk9jC6SXQk46APjG13G0LFSvrWDZTQ8mRPjyYjsceqnI4B1Ml8cs8NgIG8nJCHGjgnrCOSkBZ5wMO3AbNtkY4DdmXQxeeUBDNIC8QJLJ98KjXghWX4mitKIzEVwzczL8UNdW9wQHM-WvFg1ssX3EAr66R5mbXOdNGKQuSNMrEL6NfkijFubk_7UeoZ4g6yARXylhCtxLXgnLCTExD64rfNsfYQ7MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره حادثه پایگاه RAF Fairford: «ما همه‌چیز را درباره آنها می‌دانیم و خیلی زود درباره این موضوع خواهید شنید. گرفتیم‌شان!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/149809" target="_blank">📅 10:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a96eb2ec.mp4?token=C1Wsf9JDJi2pLytW69OS1E7le1H3XegHaW7y2MMsQnEIKXZjtQc-H___9EeNnFxncjOYG0Mc_QrFb0cG2nDBIOWrwhNYsKvZhbFXCRpBjqlN9MP2kEusXBeLmQKgz2kgjIgXGeeI8S0qiiIH2LMakFTG1KGe2EDoD-rLdv5H1weykLuM4ezt77G9OZ8_Bea9Fg24itPy9THTwT0vi4Wa_yIElzxjJ7H4xan2H7fmNm7m4AnNYFsxCDmf4Y0Oi1YZlZbNwpIAVEwIOvC-xb50GoWKTn-P_DXgoxkKplZrrcKYK2PQRzkgNpUXuqpaSzhyyLnlqRimoecJA9RU6eKvOwIWNGx7v5Lj_sjrcng0x4Y9WwifV3SrTJOBtQPCUohdA8ZxYyrAyLKD6pw-wTP_OVtxagCAbCkzAQUV_hyngDVJgzcP5cv-vWd-Mu15Vs67XVNjI6rJpb5ESgnhmyFsNFJGPQccm0WPrdtf2-mPj-8Wgpdw8KXxh5_RB0-b8GAOvTiDCI7EZ2yl0l0uijU_3ezNdhHakscsIAnBwHkD7PW4q49pSW58h_KrLbNtY9oGVnb-taprIb7hJATRsCWRYkrnnk-Yx-Dw0NEcwzYP_mUxToLi34XJCybgbUvU5IhTzpjDuPKBOSM4KT8X0qdfXiBxJBuqORT8usOwdia8thw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a96eb2ec.mp4?token=C1Wsf9JDJi2pLytW69OS1E7le1H3XegHaW7y2MMsQnEIKXZjtQc-H___9EeNnFxncjOYG0Mc_QrFb0cG2nDBIOWrwhNYsKvZhbFXCRpBjqlN9MP2kEusXBeLmQKgz2kgjIgXGeeI8S0qiiIH2LMakFTG1KGe2EDoD-rLdv5H1weykLuM4ezt77G9OZ8_Bea9Fg24itPy9THTwT0vi4Wa_yIElzxjJ7H4xan2H7fmNm7m4AnNYFsxCDmf4Y0Oi1YZlZbNwpIAVEwIOvC-xb50GoWKTn-P_DXgoxkKplZrrcKYK2PQRzkgNpUXuqpaSzhyyLnlqRimoecJA9RU6eKvOwIWNGx7v5Lj_sjrcng0x4Y9WwifV3SrTJOBtQPCUohdA8ZxYyrAyLKD6pw-wTP_OVtxagCAbCkzAQUV_hyngDVJgzcP5cv-vWd-Mu15Vs67XVNjI6rJpb5ESgnhmyFsNFJGPQccm0WPrdtf2-mPj-8Wgpdw8KXxh5_RB0-b8GAOvTiDCI7EZ2yl0l0uijU_3ezNdhHakscsIAnBwHkD7PW4q49pSW58h_KrLbNtY9oGVnb-taprIb7hJATRsCWRYkrnnk-Yx-Dw0NEcwzYP_mUxToLi34XJCybgbUvU5IhTzpjDuPKBOSM4KT8X0qdfXiBxJBuqORT8usOwdia8thw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ:«کشور ما در حال پیروزی است
🔴
دیدار بسیار خوبی با رئیس‌جمهور شی جین‌پینگ داشتیم که مدت زیادی طول کشید؛ در واقع اگر حساب کنید، حدود
دو روز
ادامه داشت.
🔴
ما پیشرفت چشمگیری داشتیم. سه روز گذشته واقعاً فوق‌العاده بوده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/149808" target="_blank">📅 10:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149807">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6Mzjp673DM_z8fR1PN7pKzziASsm6KP-r9qpzatyU-M6U7gKz11a8UWm8uvNNcRQ0gjiR32cZt-HSe_4feQExDD5iU7FMc4mEhCUwOc2z44YjtFaWPbBa4SHG1TxmMM5xQoxnppDfAJrGBh5AT2J5fjL_HSX2wpmJf0fbX0XqRl_vYmcJCLF2JLGqSEUUN_-2ICSbalVGG4VSzYqRNvFrHWbNOB0ine0t7kJdDVoW0z5B5bJ-VjUBPTTlbyYLStKp1p5jmIzVxFJ9m4-KKkNFNSj1KrnNM2Kwr4znRaIuS8YZeJGFLJQaW1L2Q0z7N63sNA3vUIxHc7oEoCqSPDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور محسن رضایی: چرا به امارات حمله نمی کنید ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149807" target="_blank">📅 10:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149806">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oksnWnFncMHbQSxbJvD6LVncIwMTK6pOIjadyyrNNQZxE4CfASLBs4MYiPlvXu25frKwWFktXvYOF3OhOTFhPjVVDp-jVSPpXEuWgqj2RhgfMd4L3Ny7zD0A4htTVA5gO_rAso4jCrCTA9AElr2JtD5eJGpVOZ3G3B2K7J4PlV8rdqX-Mv1eIHVlgAEv7hl7-H7JlW11IHN7mVrwtEeqgR8DTrmCtXjye1vboSMTElgkiie1eIYLtOzEVAuX7epSF4StS4oU6DIIwZUsdVGSuHpvSbEDGbT15QfOTA8IjxagqbkwKLoE2NH993Tayuo3P8oI2xcpzu_aiGz1_f2AdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی نیروی هوایی اسرائیل منطقه وادی زبقین در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149806" target="_blank">📅 09:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149805">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کانال 13 اسرائیل: مقامات ارشد اسرائیلی که از جزئیات سفر نتانیاهو به امارات متحده عربی اطلاع دارند گفتند که این دیدار با رئیس‌جمهور امارات حدود شش ساعت به طول انجامید و تمرکز اصلی آن بر روی جنگ آتی با ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149805" target="_blank">📅 09:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149804">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfFrgipbJvKbcu-bwwpi61ei5rj8gYa3HM-aOJH_h3Qkxi5JF_fLZDaDJbMBEABMDLIoPiSloLe9o9XSzr7gqFkkOVciyglefnsPN6_RifnPD0RiIp3-R0a2FoumVCIa_uQd4r9I8YWAHoagrg5T1ZZp93d-Z1mxyt9Dl-c9a0sFquZQppwVQ7G13SN-9y13-8FqHpG4k9LUlYt1q7QtWrsLBMegDrXmj8AlZ_yTCwC08Xl0kTEs-rkmV3FF3VJB0JVyw0gfumg7d0a6RAZshVok-8AXJSmxofBmUdsnG7itcfnkJqPA_9IWPMGZuWkJbqqoLWbM5lyVBinYzecvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۷ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/149804" target="_blank">📅 09:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149803">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از مقام‌های آمریکایی گزارش داد: ۸ تن از تفنگداران دریایی ما دو هفتۀ پیش در حملۀ موشکی ایران به کشتی آن‌ها در تنگۀ هرمز زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/149803" target="_blank">📅 09:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر خارجه مصر: مشکل اصلی در بحران ایران، «نبود اعتماد» است
🔴
راه‌حل، پایبندی به تفاهم‌نامه [اسلام‌آباد] است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/149801" target="_blank">📅 09:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش: قرار نیست مدارس مجازی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149800" target="_blank">📅 09:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f1f8d6ad1.mp4?token=aMtyo-pk90hiFhPil1WDhn0DlmderQFHq-C5qaM8rfVOUOcRmlhB8-u61V9im4Dz9ZFd6UdsVUlLLM5ZuhUufz-DLuO7uKEoVhPPDwpe62iL1IRSlti7Y7_z1EZzW2TSeb0qFMb0ix2CKzbJPvfbF31r0jb2fE4zMcl376O2DdmjwymieG2TYy5wfXSOb731BaMo5HLAaMj-EgYoUqnePtmq_gyto5TMJWKHZmSM34WcurJYxnCHwgo8_yCQBlYTcPwuucfiERQ76vOoiHcQShmNpPhirwnaGkN9BrzEDnhkUda8SDI_HHp2-LxDKYx50kOIYAJJwD0iWeKARWvvbi5EVopQrDjiT2xSd8lmCKX_kmSd1ytw_Yi1Jb_a3BhD0axUJc8Wpilzx9ZdxDxUdxnujQh933ibkMnazO6slw8YNw1hHVQISgXPnQc79SxlovwdoQk3RQP9HuiqcZ97fCn3RAStcobe-ZESqTwtDmBZFArehCZ8Pw4nKAiXTgPSbusCbViFFsptQKeM6Wct9AAz7TlgJiGZNwQL9_o5CNzs1CZxZZX0_ZMSlAMkoQIwGw24MkMrqcwB-DqdQPQu-xTMRNP96zZRAtaoiIpZ-t0PAwdwJentBaNZpYxX7kPGDE1N_F6-pJakgh4mcijduxb98eC-Xv19iX2EF8B8URY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f1f8d6ad1.mp4?token=aMtyo-pk90hiFhPil1WDhn0DlmderQFHq-C5qaM8rfVOUOcRmlhB8-u61V9im4Dz9ZFd6UdsVUlLLM5ZuhUufz-DLuO7uKEoVhPPDwpe62iL1IRSlti7Y7_z1EZzW2TSeb0qFMb0ix2CKzbJPvfbF31r0jb2fE4zMcl376O2DdmjwymieG2TYy5wfXSOb731BaMo5HLAaMj-EgYoUqnePtmq_gyto5TMJWKHZmSM34WcurJYxnCHwgo8_yCQBlYTcPwuucfiERQ76vOoiHcQShmNpPhirwnaGkN9BrzEDnhkUda8SDI_HHp2-LxDKYx50kOIYAJJwD0iWeKARWvvbi5EVopQrDjiT2xSd8lmCKX_kmSd1ytw_Yi1Jb_a3BhD0axUJc8Wpilzx9ZdxDxUdxnujQh933ibkMnazO6slw8YNw1hHVQISgXPnQc79SxlovwdoQk3RQP9HuiqcZ97fCn3RAStcobe-ZESqTwtDmBZFArehCZ8Pw4nKAiXTgPSbusCbViFFsptQKeM6Wct9AAz7TlgJiGZNwQL9_o5CNzs1CZxZZX0_ZMSlAMkoQIwGw24MkMrqcwB-DqdQPQu-xTMRNP96zZRAtaoiIpZ-t0PAwdwJentBaNZpYxX7kPGDE1N_F6-pJakgh4mcijduxb98eC-Xv19iX2EF8B8URY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : دیگر نیازی نیست نگران سلاح‌های هسته‌ای ایران باشیم، چون آن‌ها نابود شده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149799" target="_blank">📅 09:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
👈
به گزارش خبرگزاری دولتی عربستان، وزیر امور خارجه عربستان برای دیدار با همتای آمریکایی خود وارد واشنگتن شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149798" target="_blank">📅 09:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149797">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoEzrNpZILfjuRKy2iJ25-rJ9xJ_HKPeH8VSwqD3OnOl6mEHWVeyHZEbnfEEMfbrfc7DAlVoX_OuI_NrDEIZbsjblb8XQOf2Hz99NOBJziLuscnCRCgWFPPsgxo9TaPVaoe3SHaUbEGPylJAercLVMmirkN7wsZ_LXgjpZEAC8DiKVd4uXdglQMb78X5QyE2o9rzb2FHHHFd9KTDQHgk-R9nFiJJCJTEKMgEiQNwnokm9ov3HzMK_6ymofXyFkCX-BzUAtb2efZDNp7u_JGY2hGxqW_CHMDbIqjJu2vDHVVP2TS1H4-OAWGEzOtb4VdTZix-zfHvZOhWMQxiuJEE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهران نفس تازه کرد
🔴
شاخص کیفیت هوای پایتخت امروز روی عدد ۸۹ و در وضعیت قابل قبول قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149797" target="_blank">📅 08:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149796">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نخست‌وزیر عراق: نیرو‌های آمریکایی به طور کامل از عراق خارج شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149796" target="_blank">📅 08:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149795">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وال استریت ژورنال: واسطه‌ها می‌گویند ایران از زمان رد طرح آتش‌بس خود از سوی ترامپ، هیچ‌گونه امتیازی نداده
🔴
تهران اطمینان دارد که می‌تواند در برابر محاصره طولانی مدت آمریکا یا ازسرگیری جنگ، مقاومت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149795" target="_blank">📅 08:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149794">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHhbkk1Gn_aMaW0pGcOIlZqiEr9XF7odKJ0MYO8wJfBIH_9y3tXB8u3c1qUvpEDq9Jm2S3uoGT0_9hPJkEE2pdU5zPPrK3np_Zq0xH8jzjFhbX5qtABGo1QoWmud3CIxp7pCbFHrg4WsPXArtUJ3BvaFqw2T_nvSj7E5O9if8DjYj5qLj5BZXeqj1vXTo9LIqTbbN4A6zbuyX_b1XGkr6ZGRmYRZCwpEky12l2db9EaiPeUucB8RSVqiCE41NNJ4L8TivE9tp7_gEpdhsNmU2LqWIT2PDPZVVCThoJ2LEWNMuNROLWVo6QaSS31Upc-fsHBcvSe8yMJ0v3HyF7inVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی نفت در نخستین ساعات هفته از ۱۰۶ دلار برای هر بشکه فراتر رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149794" target="_blank">📅 08:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149793">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در شمال اردن
🔴
منابع خبری گزارش دادند که یک انفجار مهیب ساعاتی پیش شمال اردن را به لرزه درآورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/149793" target="_blank">📅 08:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149792">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445b783ab0.mp4?token=fnj74MJnvQzWDBxePz-tZOaXb1mjpbvGzcldYdpws829M-lZKk4JBH9yoFcZqeJMEl_hUwDNl6RJrI9OtcxylI151aR3KPnt-fFjmbRaIEjbicKk8wGszmQIiC1m7chZRddjcE-br9MUjlB0TEAGrjNgxy1jhW3wIFdz2Zq0trzRXpEvtxDFjLcU9bIfuBkWIgwa6-rVVCgRWZFyHV5i82oNtSUNnjTP8bkKrpQH0Pye7nZXC1yuK9-_AeimV7sujx1KcafYlOmHJC3GxIypMNCvtFzizOZXmaC7EmpFiskwpIEyPMU8O6uFr98PPhu2QKNbmrbuQv8xkuP6EqCF8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445b783ab0.mp4?token=fnj74MJnvQzWDBxePz-tZOaXb1mjpbvGzcldYdpws829M-lZKk4JBH9yoFcZqeJMEl_hUwDNl6RJrI9OtcxylI151aR3KPnt-fFjmbRaIEjbicKk8wGszmQIiC1m7chZRddjcE-br9MUjlB0TEAGrjNgxy1jhW3wIFdz2Zq0trzRXpEvtxDFjLcU9bIfuBkWIgwa6-rVVCgRWZFyHV5i82oNtSUNnjTP8bkKrpQH0Pye7nZXC1yuK9-_AeimV7sujx1KcafYlOmHJC3GxIypMNCvtFzizOZXmaC7EmpFiskwpIEyPMU8O6uFr98PPhu2QKNbmrbuQv8xkuP6EqCF8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ناو هواپیمابر «تئودور روزولت» برای مأموریتی ۷ماهه عازم خاورمیانه می‌شود!
🔴
دریاسالار داریل کادل، رئیس عملیات نیروی دریایی آمریکا، اعلام کرد ناو هواپیمابر اتمی USS Theodore Roosevelt (CVN-71) در حال ترک سن‌دیگو برای اعزام به منطقه سنتکام است.
🔴
این ناو به همراه گروه رزمی و بال هوایی یازدهم ناوگان، برای یک مأموریت طولانی‌مدت عازم منطقه خواهد شد که مدت آن دست‌کم حدود ۷ ماه برآورد شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/149792" target="_blank">📅 08:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149791">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkcVQ6EA32mfNEApbQOsYEvxz5XOAnzKudafGzBxImXrpxryNmt9GOs4sGXXlkdcVzVOo_-n70vOpdL80YKqxRcOgnQu-2kqoZ4rbFoAt-loNLiWLoSGI0SUAL3UKVwrxaE90J9VNbsdbJf-XTRW5aIqVNBZoq6TBYux_vW1JrCXiUTXBLfxsrMkTl6R2kUtaDq4i5YnswfMO33ApvVUFLW9pLzGXkFmw8Iaqi2ITpxdnKvUDzYrkLpfdu7qps2UiqSv9NW7vcfLYh5RobiSNrXtu03xtj3r0FrJL5Y2QuDBorUq4CjsWBK--T50YfIf4h28W2Hjesj49-lYSZxYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان هواشناسی:
بالاخره موج سنگین بارندگی از آفریقا در حال حرکت به سمت ایرانه و حداقل 15 روز بی وقفه تو تمام نقاط ایران باران و برف شدید بیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149791" target="_blank">📅 08:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149790">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95325b2b7e.mp4?token=I7crCFJT0fj7-27DJQgxyYagWpPOWNf363Aa7AkAIbWYxdjthMz2sjM13-1hBBL4sVlVxGoRjFR0Vnnaj-XXnpWYPhLgXt2jrpV_x3_C4BQYhVu4EfAe_pAdKKg_lPSJG0F1GVJNH2KO7T0MJsmTWfAXRowwlqKPlVCtmjVccVNV_zeRpVQQ3rMlbGIgQZvAyqh-Qj3w_u_kBqb7x8cKsoCPfXJK06sGWpdFuQSRcLfaXRyu-sbivSNu659VpS5CIHxWhkcSDXP8UnVMT4u4xtU1yXGsDki0WuJJmEzuQ2kX1Sj_dJtzSeovR7craugdb086TQtcDzGdFzpNwV40fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95325b2b7e.mp4?token=I7crCFJT0fj7-27DJQgxyYagWpPOWNf363Aa7AkAIbWYxdjthMz2sjM13-1hBBL4sVlVxGoRjFR0Vnnaj-XXnpWYPhLgXt2jrpV_x3_C4BQYhVu4EfAe_pAdKKg_lPSJG0F1GVJNH2KO7T0MJsmTWfAXRowwlqKPlVCtmjVccVNV_zeRpVQQ3rMlbGIgQZvAyqh-Qj3w_u_kBqb7x8cKsoCPfXJK06sGWpdFuQSRcLfaXRyu-sbivSNu659VpS5CIHxWhkcSDXP8UnVMT4u4xtU1yXGsDki0WuJJmEzuQ2kX1Sj_dJtzSeovR7craugdb086TQtcDzGdFzpNwV40fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب تو صیدون خوزستان دو طایفه درگیر شدن برای انتقام یه جوان ۲۰ ساله که به دست رفیق صمیمیش کشته شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/149790" target="_blank">📅 07:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149789">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPAYONET | VPN |</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_UAKLgtdzmXqTkfkGRs-UjvAJMWxils2arTDlG2YTYUjMEjfIA32SXNlEu6pZSqy3Aq3mvhrdsPReYAdn6F5-U1ejcoPnmlMpn17_RQ91PwZ4vrsGGqt26hOuQuJ-d5GMexpGm2zlH75ReElD-HK6B0-YNK-fNQyeYW-HDS6xqsntDUX1WnZWSvP7fy8r63sjdX3Jls0RXlsGlCRWPVynq7YPCgzyOeQxeS9BB0aZgpCIukFef2q0lk8BgQCsO7gdAFDFPeUwyT7yHnFRuaFBtCLHDAifq1ezrID7qMzelHVXu7x7CFRVbXcELXcCe6hLizoWekqraYMJ8IkbhreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
☄️
مناسب شرایط جنگی و اختلالات
💬
پشتیبانی تا آخرین لحظه اشتراک
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
👾
نامحدود تک کاربره  | 79 تومان
💵
👾
نامحدود دو کاربره  | 99 تومان
💵
👾
نامحدود سه کاربره  | 119 تومان
💵
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
خرید و تست رایگان از ربات
⬇️
BOT
🤖
@Payonetvpn_bot
ID
✅
@payonet_supp
❤️
CHANNEL
🫡
@payonetvpn
🔺</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/149789" target="_blank">📅 01:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149787">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPcVQzCdMYEYom4p4-JzcIMZsnWHSMa_UKU58mdCKBL8jd8Cz0v-Didv9YDGSqV7VZen6-Wc_gNx6ZsG5qGFiFsRiXT99UK71GHb3d80T_X0aiGY57vbffofmuIDEF58ooUX-vmOtmQwqDa73eIAi5PmsSIAgf6zqaqcfHVdABCkmTCuECtoLFvLIg5MSOFKznWKCpNa8S2SpRJ_clDZX6jYk9ne3KR9kZBF2tXEhVM852as6krLB-LSKeza-uaOCLwWJHZTFuzRIpYZShdVwJMUhnwuQkaRUF5kPWNmTu67CpoXQthE-G3VVAD2OcCIATXLLUvsF5chGwHlWYFAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلاهی که ترامپ توی مصاحبه استفاده کرده همون کلاهیه که اول جنگ سرش گذاشته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/149787" target="_blank">📅 01:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149786">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گزارشات ارسال انبوهی از رهگیرهای پاتریوت به خاورمیانه در هفته اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/149786" target="_blank">📅 01:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149785">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYcfVEo_j8XpwuTmR30AGi1RIFezfSGRDT-c-lTCfXwoNKgW2JTxE7MsLgLd-QW8foYut25qD1vDWLTYjQk_zfRKkDyGhW5NfGyuUzcB-smX63xrdWtqd5T-BUmaB1SyzP9lExw7RgEUvgts67ziZv03Xey5Hbql4-lGE-wXvLgNihV71iLnFcIV5A_UjMEo4Dgkf-Yp8iU7ai-z0g8vTo9UxjcC2ThWmU9xC7lzJbP7e4z0CmMutoM4SFKhGXEZbM1ydkKo_DxCFX4syzCYlstgfBehFyKrcdbuZyHIKqiqwPIyKK5QyiNUy0KfONaIHgnVr32ntr0JmFsR9s7NZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فصل جدید فرار از زندان رسید
🔴
نیو سیزن: فرار از اوین
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/149785" target="_blank">📅 01:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149784">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ:ما ایران رو بزودی شکست میدیم و فعلا این کار رو با فشار اقتصادی داریم پیش میبریم چون از نظر نظامی قبلا پیروز شدیم؛ اما این به این معنی نیست که عملیات نظامی رو کنار گذاشتیم و اگه لازم باشه بمباران رو مجددا آغاز میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/149784" target="_blank">📅 01:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149783">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری/آکسیوس: تحرکات حاکی از اقدام نظامی قریب الوقوع علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/149783" target="_blank">📅 00:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149782">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gioUC1xu1V1b6-2lSrJUw-1Bmbyf9zJ2YCj4FGnuALHxrgsSE38O6O2jyorSCiYBiVs3_e5SDX0Pk08NjJHcAt-YQTGhDLZ00CONdqYgCayCTvQumF9CavPa1zFN9TiDKpsJMH2XxfWrfsephVUHTm7L0uYMr7KGRvmBgTmunit9QwefMUudaJ1I1EVe0X2P1xJSY8gui_FVI3dMZWFttVUHeav626gQU_jNxflkHjSODr2kTAhVKq1ZHX_hhM5wVoRrusLPsyylZD0M08T4BC-bDbMDgJ85US9Wk9oUa-AvNUmpaIhH19UHjAsddAY9xjsc0C7eioBBhQDFa3O-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سر سلامتی همه حبسی‌ها
❤️
🔴
ایشالا نبویان و ثابتی و .... هم میرن پیشش  که یه بند رو تشکیل بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/149782" target="_blank">📅 00:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149781">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3k3_kXVQxGXNQ3VbvvvAZFKmFff9R8dGIeJk2Uj3ab2_lA-q4fsE0dQtQId_hZev1S0cTSjrPkBOq7ruLL0Wn4rU5S0cjjM9KMxIfcfyozS5RI8f5XA8azFa-3PmKMGDZ_GLZJamqRtvNc7C_HmI8CI-hS7yPW0OyeAqWOL34X38XL6DypceWZmxHSY_HlWWr-5ue_o4E3lkVmJLy21uDB_3xNmTgbzhREdmzJquvDxWan_4Nj7ak9ElSDzelBNSl7pQ8JUlQ4oHxeQgY9Xp6IfrKniYWt2-58ve4tijbbkVdvU7H3UC78ZRn7c0X_ErjnBW_yzwBZ4m0B8-FuDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: دو ستاره برای سردار محسن رضایی کمه، باید ۵ستاره بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/149781" target="_blank">📅 00:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149780">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نتانیاهو الان تو امارات هست اگه میخواهید بزنید بسم الله اگه نه، لطفا دگ شعار الکی ندید تشکر
🔴
فاصلش الان ۱۰۰کیلومتر هم نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/149780" target="_blank">📅 00:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149779">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نتانیاهو الان تو امارات هست اگه میخواهید بزنید بسم الله اگه نه، لطفا دگ شعار الکی ندید تشکر
🔴
فاصلش الان ۱۰۰کیلومتر هم نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/149779" target="_blank">📅 00:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149778">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
فارس: حالا که اینجوریه! مذاکره نمیکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/149778" target="_blank">📅 00:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149777">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a46df7be.mp4?token=GcDjzAZCmROazXpNh0R49jYOnCFMZ6LIY-D32s-dD22UG8dOrhGFVs-kUW7yfBu758P8fjkSunC8HJb8fkDlm7eGWa3LGdL_LnezVNR5dp_eKJo6x7XUxH7WV7aoTviofh3nbem0SuiAaGGD5LTiSm4wYfoFMXsb31ulvXs5USKXiYv3RcOktKWVxeE-11m0A_MfMClCyJozohzVsispWu-h2rroF5GUPQylXrDs3Js7GzMoPICn5pTJra--6C-JxW0KixMsOdiSw2ldyPkGHHRHkEnhqZpzgFUvgdxU0PntJ646KfeVL-aV3pZ9AvYSWS6OiRYjbr61l1Y6p1bkTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a46df7be.mp4?token=GcDjzAZCmROazXpNh0R49jYOnCFMZ6LIY-D32s-dD22UG8dOrhGFVs-kUW7yfBu758P8fjkSunC8HJb8fkDlm7eGWa3LGdL_LnezVNR5dp_eKJo6x7XUxH7WV7aoTviofh3nbem0SuiAaGGD5LTiSm4wYfoFMXsb31ulvXs5USKXiYv3RcOktKWVxeE-11m0A_MfMClCyJozohzVsispWu-h2rroF5GUPQylXrDs3Js7GzMoPICn5pTJra--6C-JxW0KixMsOdiSw2ldyPkGHHRHkEnhqZpzgFUvgdxU0PntJ646KfeVL-aV3pZ9AvYSWS6OiRYjbr61l1Y6p1bkTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیش ۴ بار بمباران شد
‼️
🔴
وسط برنامه زنده علی اوجی
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/149777" target="_blank">📅 00:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149776">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/149776" target="_blank">📅 00:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149775">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_Igye58G6Qai9QfCi1CfYsPxNa5PTIwrz3_O65T4iO65XQqgxV5KD6RlIARNMBdbIgO829q9S0jJuRhrLBsGV4a04-w7iL_I3RaWmMsj41w_D5yf-kZSuuZ7PwTVwKMpR1zUErIX3Uv0_cVfS8WQrloaYNT8ZbkwymIIxHB-XRdSP4VFGd6YwW97tlzctq1NEP3JJDzpCQCVn6o-FxTMBNfTdLG8nAnhnuNHFpVnWQNwG2SszZcUJsOVSjosqThygdrH-RzaZl17HiM0ROzlHW4dhg88-AMc766Mn0H4CfgYWcjVYPOEnTypVDmH0wjI6kN7p5YzvH6oG_vfdnKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت تتر در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/149775" target="_blank">📅 00:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149774">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ایران سریع‌تر از جهان پیر می‌شود؛ رشد ۳.۷ برابری سالمندان تا سال ۲۰۶۰
🔴
بررسی داده‌های آماری نشان می‌دهد در حالی که سهم سالمندان جهان تا سال ۲۰۶۰ تقریباً دو برابر می‌شود، جمعیت سالمندان ایران با سرعتی به‌مراتب بیشتر حدود ۳.۷ برابر رشد خواهد کرد و به ۲۷ درصد کل جمعیت کشور می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/149774" target="_blank">📅 00:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149773">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac306d37b.mp4?token=QFL_H31zs3Tb7C-5717ZZ9tHLl7oIFbGkoR7401Z-VZ1nuvoruZax6tLEC74HLT7M1XmAEH-VPNYxhQa-jxnYjI7LgIJNX0JyClbxYPY8EUD91q2lzCmL5JDeciYfxOvX_dz-kyxu_4QozoGCswiK94bDyf5zGCY9VGoEkmMEeo7jLF4bsUyDlynPZQ9V_i8tN2f--aAm83zJ-TSH39_qIVDN_T4f2ywp2zI5bTtNcooXpgqEcJ4ZmSWuzyFPmYIrTBKBGlr0croPdH_YHlkwphED8aoECckePutK4XJriARWNL21JjOmOn4J83HBJKXgLgMFT9EqzbKdIcUbN0MOXni5Fo_G3Vwh7nJrqA4E1jkW10nCLdVk2JAcERrh93AxbyQ4lJSBdTmkLORV3D8BT6N_3qMevE9lXpAvbU-WVcVGZ3z0GRPZ4uZyTLPFxeXPVnpvoiJfKTnBqDrrW3HMp9PFGpN9_9S_xWDAEargbdjfoj1b0oROMqdX_O3yYyx_xu7_z6r7xs2wO22R2lO9fy1W-kUW-8AMs7a8KagltRZe1_AOkloMW5BsS9GPUl91GC1IyrGWwAatKM3wXfacJ7sBMs3COn-P7PPRsvV-axmTwNek9uTIxL4_AJJgm1NWsqDtgzM1WwCekVyEstr50wrOw5G4N5up3QN-nIGwEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac306d37b.mp4?token=QFL_H31zs3Tb7C-5717ZZ9tHLl7oIFbGkoR7401Z-VZ1nuvoruZax6tLEC74HLT7M1XmAEH-VPNYxhQa-jxnYjI7LgIJNX0JyClbxYPY8EUD91q2lzCmL5JDeciYfxOvX_dz-kyxu_4QozoGCswiK94bDyf5zGCY9VGoEkmMEeo7jLF4bsUyDlynPZQ9V_i8tN2f--aAm83zJ-TSH39_qIVDN_T4f2ywp2zI5bTtNcooXpgqEcJ4ZmSWuzyFPmYIrTBKBGlr0croPdH_YHlkwphED8aoECckePutK4XJriARWNL21JjOmOn4J83HBJKXgLgMFT9EqzbKdIcUbN0MOXni5Fo_G3Vwh7nJrqA4E1jkW10nCLdVk2JAcERrh93AxbyQ4lJSBdTmkLORV3D8BT6N_3qMevE9lXpAvbU-WVcVGZ3z0GRPZ4uZyTLPFxeXPVnpvoiJfKTnBqDrrW3HMp9PFGpN9_9S_xWDAEargbdjfoj1b0oROMqdX_O3yYyx_xu7_z6r7xs2wO22R2lO9fy1W-kUW-8AMs7a8KagltRZe1_AOkloMW5BsS9GPUl91GC1IyrGWwAatKM3wXfacJ7sBMs3COn-P7PPRsvV-axmTwNek9uTIxL4_AJJgm1NWsqDtgzM1WwCekVyEstr50wrOw5G4N5up3QN-nIGwEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سرعت تورم برخی مواد غذایی
!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/149773" target="_blank">📅 23:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149772">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAKN8MbB5q7mfjb88OfuIebNy7ewFFgHrqKay1DKqZRYlIDfiL3Mfeb3Y4LakJYulwzd-7b0FAdbYAMVCDSuDu8NQ2HBmc0uqFRG0BPTKc_HHC8MJyj-Hrq-kBtjKrDjPl4l1CQ9i7BQBe06huXnrsc5eK6bLBM_W4X3vVaervye_RRTUI_as9oCmhUDby51X1sqnRv6Lsa6jh-lKEC-A1CcYjKI_v96gN9WazMmC0HjIniwOT3vGjoMU5iR-ZT-zsQbaR5pOiRvpfYTBdrnggXDcw-MhD_rVbA-CUloX4y3CA_Q7W30hB-ZMitMteQlmLfLMG2niLHgGF1Ik-iPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بار دیگر نام تنگه هرمز را به "تنگه ترامپ" تغییر می‌دهد و قطر و بحرین را از روی نقشه حذف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/149772" target="_blank">📅 23:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149771">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bz6jodpb9F9hny5SbTr6wfWUJgqveb-PRDVNpsO6wSmVOR6Q8KnHg8q0PeyNyt-i5qVP4GP765f2OLAn4yhwjWhFrs1YcswhRM2ROVUnc31ihCYssdlJsW7VhYNTPDfWnut9QA8MYMnPaJXzGzkNM6zOuO9XScMNS2p40ExgNkL0JOkT9Um7qVslQ_0BnDlRtWpQUCcx9RWrhMTFVAFKCvxoYzNiWe5jZiyWMXyOxhkRW7D7N_p56Kce5F-_SXpfnIV4gAa_XPObo9pGwXCNJklsdtb6x9r5WHoyAeOBRlPLYdIhziLFEXkbP_3OAveFCi5S90V8sm_ekEQyZ6FPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ از طریق شبکه اجتماعی Truth Social
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/149771" target="_blank">📅 23:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149770">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گزارش صدای انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/149770" target="_blank">📅 23:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149769">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tDjuzJGqyj7DFcYNHeZuF59lPssG6cyDAfnW2R_TCN-uemuNimgW_FI-6EtgCWm3WVQo2a--PJZsyzE4ZuBpEGen4YZm6QbACsREKP84i1LF3SknDj-dAIbBfLWYRaey9O8limhyhSX0ZK5ieZ23ZSJRxdk9uuSivQzz4OAeDlP61dJ1yfn3zoiKe-4-TjVu5rULR1bgQ_UyUF9Q-0ibyBIsd3ZTPdBGqe7izaVOkG1TSWcV7oWdVgfxbKellOyyif9ZFQOM-VFtqGtGeMi-V2hneBwSN4BaeptSXX9V1NKK8WysVMwxStvkoe3xUaRhUsLUoT9on0USnMDVj_Pwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در تجمعات شبانه ترامپ و نتانیاهو، خودتون و زن بچه‌تون رو میکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/149769" target="_blank">📅 23:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149768">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ایرنا: هیچ برنامه‌ای برای مذاکره با آمریکا در دستور کار این هیات قرار ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/149768" target="_blank">📅 23:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149767">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عارف،معاون پزشکیان: نباید برق و گاز صنایع قطع شود
🔴
برای عبور از زمستان به همراهی مردم نیاز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/149767" target="_blank">📅 23:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149766">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_zMnhnqoyDvLOuNIPM0eBamhhMlK8ompj0K-jNsG4OPfYlfQs9CX6O5asT-n4C2VeC4-Py4FJ8RaP6OxZNWXI3Xkm2zHPZfu9B3TX3ztZaSSpRgMTCk8znW09J0CFo7R6eaXr_wzC3ih4PMg0iHyrZNsdUoHLylEzYTfsl32OM7lxNAyJSwnFOfI7Ojsg9QVEwK6XC_mz7ZIkexOuyo0zoksL2ZBnXAvooeHp2Y7u6TlwZ4tZnzBVrgJZiVaNhP9rDpiPPw61AO_udxtv8SrG6rO-GFGfGwnWoFQEV7wsRKRxstDTeGcgumwy_JtLC8kODxXoWvBShljtn3AGy0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
۶ فروند هواپیمای سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/149766" target="_blank">📅 22:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149765">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
میدل ایست نیوز به نقل از یک منبع آگاه نزدیک به دولت عراق: ممنوعیت ورود پروازهای ایرانی به فرودگاه بین‌المللی نجف قرار است طی ۲۴ ساعت آینده لغو شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/149765" target="_blank">📅 22:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149764">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT-uTUhNxl6rYyoVQsvBaPGBLjLuRSNbmqvlQh5Fp69wfe4iKAUhaUaMBFE62x6LrJlbjJPj6VoKi3UyasSIr6QOAjdQoAP9QwqVeBKn6O1YpKoDLOB-GyBnw2TqFNtmUC5KeD4gKkqrFQWUfrZGvSXIAxDkQa1tCqHpaI5hgCZgISwbgsEa9CdXqHEq8OFyGiaYRu-PpVwVj4rl1rJHrZVX_QJHJveeMPsalX0lWVGKojyNAlzyra2zVbev-rDb-q67_EUGylJXC1L_ULIEuk9VlodshbklHXwRE_VoKakyrWM3Cqy8uJHrlgEO4esejNea8m2eKfWMwBUMmZ9iDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: در حق من ظلم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/149764" target="_blank">📅 22:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149763">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
…</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/149763" target="_blank">📅 22:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149762">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
خوش چشم: یک جنگ دیگه در راهه و آمریکا قراره شکست بزرگی رو توش متحمل بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/149762" target="_blank">📅 22:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149761">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
کانال ۱۴ عبری: نتانیاهو امروز برای دیدار با محمد بن زاید به امارات سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/149761" target="_blank">📅 22:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149760">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=j0UeHi0bnHVk33XR6Wk2lWSnw2khomlUToLNoJ0gdPTGfQs5JqFHLPOOvecKmQpsyHz0j0eCECXqH_r2G3zTC51z9zZm8zq3iOM6S8Adc2-WUHPgjmQ_B0hODzuKL4Odbq6zlohu2IRZbx_9wT8SCcJtKdQCF7rtf48kH2lRsSdJrDj7zAdiz7g9BHWXDJFkORaba8CMaDFpWWBxjI4GkTOPLPXftByCXHu-FWa2UVf8nXhR7G246cBf4KgW8BMMAo53yf8PDJPui9pYrpQTC5rAS-lBwO-MweZvkm4y_6SJ3sKXofz48Abhr6xbMCK7LjggNKmkU7zaR-AM4qgWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=j0UeHi0bnHVk33XR6Wk2lWSnw2khomlUToLNoJ0gdPTGfQs5JqFHLPOOvecKmQpsyHz0j0eCECXqH_r2G3zTC51z9zZm8zq3iOM6S8Adc2-WUHPgjmQ_B0hODzuKL4Odbq6zlohu2IRZbx_9wT8SCcJtKdQCF7rtf48kH2lRsSdJrDj7zAdiz7g9BHWXDJFkORaba8CMaDFpWWBxjI4GkTOPLPXftByCXHu-FWa2UVf8nXhR7G246cBf4KgW8BMMAo53yf8PDJPui9pYrpQTC5rAS-lBwO-MweZvkm4y_6SJ3sKXofz48Abhr6xbMCK7LjggNKmkU7zaR-AM4qgWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی وایرال شده از لحظه تصادف
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/149760" target="_blank">📅 22:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149759">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e1f47427.mp4?token=Ad8x4Ro5tHtR_sFI6Lp92CIXsp6ia-mNBA-rTTk_Dc4241OAVkdauxb7MtJrZFmXSPRq7b8BsYWw-8_R07Ykr_F-zbHjxVOYnxWswD7IvaGVYEGbn5JbBDs76cS72--L-99ECdE6Z5hPCLXyD06vzOq6j4LWBpx-xu8ZYk-JFoctCwOsMPLAApcdh0wIwejUpTTSFOCGqQeaqnMrBwd3mqGCq0cOyRzsO1zRVr6DVYLvtfzxefgx7viN3mjdQMn0_yhVVx2pDk66F70H7q7Z2gFpjJdk8hqg3KM6zm2pS_zZxwGdlmNkTmWqzhfuZ_5ZLCIowv_uZUZwsvkj3wXI9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e1f47427.mp4?token=Ad8x4Ro5tHtR_sFI6Lp92CIXsp6ia-mNBA-rTTk_Dc4241OAVkdauxb7MtJrZFmXSPRq7b8BsYWw-8_R07Ykr_F-zbHjxVOYnxWswD7IvaGVYEGbn5JbBDs76cS72--L-99ECdE6Z5hPCLXyD06vzOq6j4LWBpx-xu8ZYk-JFoctCwOsMPLAApcdh0wIwejUpTTSFOCGqQeaqnMrBwd3mqGCq0cOyRzsO1zRVr6DVYLvtfzxefgx7viN3mjdQMn0_yhVVx2pDk66F70H7q7Z2gFpjJdk8hqg3KM6zm2pS_zZxwGdlmNkTmWqzhfuZ_5ZLCIowv_uZUZwsvkj3wXI9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: ژاپن چون انتقام نگرفت باخت و الان برده آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/149759" target="_blank">📅 21:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149758">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:   به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید.  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/149758" target="_blank">📅 21:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_9302DtsxDQHEFnqB4u8iYFakTvcA7mEXzICFOFMbyfc1rhMTyffpeM2UiJc1kJ5Q8YvmxcV2WPWmxdXm3xjTeXgB9huGjzuHF8k8Zk7S0F-2A1XdPkoAV8msUZdc2iRYJr_9fYZlobW0DqDW4JscJZEzgi7sBBGLN6DtqZfH5jLVioyKbA4Qhsj4ys1KlRcKMMeC0vPWK-T60VQJ0wgfmib-2jbyH98J23icQlo0Ozfym0l5Bw0K9Q6ZwNebGKuzOMhU4jJjcJI8PE5QGOwKL2G4CH3npRvHKBr8ZnktBTb-45I-_44IHOL0xTFQ4HTM31wgen5sqPMDH-WVL1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری وایرال شده از مدرسه رفتن یکی از کودک ها که کیف نداره و به جاش پلاستیک انداخته رو دوشش
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/149757" target="_blank">📅 21:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
اسرائیل از دیپلمات‌های هلندی که در رام‌الله فعالیت می‌کنند، خواسته است تا ظرف هفت روز، مدارک دیپلماتیک صادر شده توسط اسرائیل را تحویل دهند.
🔴
این اقدام پس از آن صورت می‌گیرد که هلند ممنوعیت واردات و فروش محصولات حاصل از سکونتگاه‌های اسرائیل در کرانه باختری، قدس شرقی و بلندی‌های جولان را اعمال کرد.
🔴
بر اساس این تصمیم، دیپلمات‌ها پس از اتمام مهلت تعیین‌شده، از امتیازات و مصونیت‌هایی که توسط اسرائیل اعطا شده بود، محروم خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/149756" target="_blank">📅 21:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بدر البوسعیدی» وزیر امور خارجه عمان : گفتگو مطمئن‌ترین مسیر برای دستیابی به صلح پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/149755" target="_blank">📅 21:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل: مذاکرات پیشرفت چشمگیری نداشته و میانجی‌گران از مواضع طرف ایرانی ناامید شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/149754" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149753">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) تصاویری از بقایای یک پهپاد "کاریال" ساخت ترکیه را منتشر کرد که توسط عربستان سعودی مورد استفاده قرار می‌گرفت و امروز صبح در آسمان استان حجه سرنگون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/149753" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149752">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح دولت تحت حمایت عربستان در یمن: در عملیات جدید نیروهای ما علیه مواضع حوثی‌ها در مرکز یمن، چهار کارشناس ارشد ایرانی متخصص در راه‌اندازی و پرتاب پهپاد و موشک در مرکز یمن ترور شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/149752" target="_blank">📅 21:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پزشکیان: بار‌ها می‌گوییم گفت‌و‌گو می‌کنیم، تا نگویند ایران حاضر به گفت‌و‌گو نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/149751" target="_blank">📅 21:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
تلگراف: پلیس ضدتروریسم بریتانیا در حال بررسی این موضوع است که آیا تهران پشت طرح بمب‌گذاری علیه پایگاه هوایی مورد استفاده آمریکا در جنگ ایران بوده یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/149750" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5MR2mrMgccog0RhRYnBgRo2_6czp0JW9zO0oat0qRfE0E0cmGsoStj1Bz9bGh_6C9mO2F4TH3Sd9vVqrTM6NnNIONbWMp2Ww875PvTX5p8CZyf-u27y0XzyD_S_7mVPLybSF5WuZ5coQGEam5JgdI6k_r7xq9dg1SSju1nATfdVKUBXhfBS-e_mu_GiahYFMkXTmYAQzcxHLD7Q-j5cWLpK3AhmZVAzsHscAoDe46_iQb1p92ZGEenWikIvPMA0LM1igYTKIveUC0zrS9X7CYnFiaiV5t77doMot1Lso21nPYHYH_Xw7sFRqBnuBgMYfvNiQr3FFtgfDxKnBs9clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان قبل زدن زنگِ آغاز سال تحصیلی؛ یه استخاره باز کرد که انگار نتیجه خیلی جالب نبود و سَر تکون داد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/149749" target="_blank">📅 20:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149748">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be3641b4.mp4?token=GzUYWxlGcsTj03ZRbHlC57rVYZnRAdlVD9rCJN5PcepQt3Dhp0INcoeDUxrHnSmOJlwrzqwGJxA5Q228Rjwx3uvZ7Jy9ksjoomWce_topL_ayS7t7MUnehUWykxCyMzgI_JFYN68JemMUMtQsiiMzH2r1DlzczL1MYdmKHTmsaYtjMhMt3hZDI8YDIKe2VNH5X9Z2Ilz-dvMpYHg_ZnG9edz8lAUyDE03AYyQp0fCTBBZ6zTzHeu9JMU1rNNqrvP0rPIS1PhMudBZXwD3iHdIcNMsjBSa9GixNuQdZO0LKRFiC4wI-isWoL_Zee0ht1R4QPnvEgciq-cWRBLK8FCpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be3641b4.mp4?token=GzUYWxlGcsTj03ZRbHlC57rVYZnRAdlVD9rCJN5PcepQt3Dhp0INcoeDUxrHnSmOJlwrzqwGJxA5Q228Rjwx3uvZ7Jy9ksjoomWce_topL_ayS7t7MUnehUWykxCyMzgI_JFYN68JemMUMtQsiiMzH2r1DlzczL1MYdmKHTmsaYtjMhMt3hZDI8YDIKe2VNH5X9Z2Ilz-dvMpYHg_ZnG9edz8lAUyDE03AYyQp0fCTBBZ6zTzHeu9JMU1rNNqrvP0rPIS1PhMudBZXwD3iHdIcNMsjBSa9GixNuQdZO0LKRFiC4wI-isWoL_Zee0ht1R4QPnvEgciq-cWRBLK8FCpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیل گیتس: هوش مصنوعی از انسان باهوش‌تر است
‏
🔴
هوش مصنوعی فقط یک فناوری جدید نیست. این واقعاً یک رویداد تکاملی است.
‏
🔴
ما یک گونه هوشمند خلق کرده‌ایم که در بسیاری از جنبه‌ها، همین حالا از ما باهوش‌تر است و در چند سال آینده، با سطحی که به‌صورت نمایی بهبود می‌یابد، به‌طرز دیوانه‌واری از ما باهوش‌تر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/149748" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149747">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq4SbwuXaVi590Jx7uDzZ_2F6_KL5KaQeP8O2LzdkTwZlhkVhwI12okOWTDKW-N428PMswMEJlgdR_SFUeVG8NoSh36HLe2ipfK3GM5TdyOtD7qNh8BKiZUpJrwVJTNMya11FZ-6ra-dOh-Iad9sZ7bkrMxJNke6on86YX5phtOyiNtzqiiifdutpfkX8Q5FT0RN9Ey_y5zse7GLxL5c78qQiTWTw3qnhBAD-HwO5XSb7V2rteQrvN-v16JY07_5eTz4mAmrqIuFlrOUSgczkIKrn6pAH3uk30ixAuMJ7z2tPLT7CmLWs6jpNGNxkhG3muKqT5LjbvQJB6oNyS7-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف بنگاهِ فریب‌کاریِ آمریکا می‌گوید ایران کنترلی بر تنگه هرمز ندارد، اما بازار یک اضافه‌بهای (پرمیوم) سنگین روی نفت کشیده است: ۳۵ دلار بالاتر از قبل از تهاجم، و ۵۰ دلار بر اساس قیمت‌های نفت فیزیکی.
🔴
پس یا بازار احمق است که نفت را با این قیمت‌های بالاتر می‌خرد، یا دستگاه روایت‌شویی آمریکا دارد سیاه‌بازی می‌کند.
🔴
برای کسانی که حرف آمریکا را باور دارند، یک دستگاه چاپ دلار رایگان در تنگه هرمز گذاشته‌اند؛ بفرمایید بروید بردارید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/149747" target="_blank">📅 20:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149746">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
تریتا پارسی: مداخله دیپلماتیک با رویکرد سنتی چین همخوانی ندارد؛ اما اگر دور سوم و ویرانگرتری از جنگ آمریکا و ایران رخ دهد، شرایط ممکن است تغییر کند.
🔴
اگر شوک‌های اقتصادی جنگ به سطحی برسد که چین دیگر نتواند خود را از پیامدهای آن مصون نگه دارد، پکن ممکن است برای مداخله انگیزه پیدا کند؛ آن هم به شکلی که واشنگتن ترجیح می‌دهد از آن اجتناب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149746" target="_blank">📅 20:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149745">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
هم اکنون گزارش های اولیه از وقوع انفجار های متوالی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/149745" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149744">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1bc066b31.mp4?token=JhxPeFdFe2NC2CIaMg8RpSQU_6txiwWbMImztvcPvg0zokte_n5RMDX4mYmBeEmjR31SkAKaQs-ncj0UMVxr6fcDnD-3LWAjlSlPbMDR-mWEmxNEgbV1JAFGe_K-msi_b7TWZlJFVRuAkHko6fQm1TwHFXzpwGoYmiQ7jRmV7ABR0S9UXLqPqLnH-oOLzhBTw0Nqtsr5CItk4f2NMFEJVQ3-DF6ClHK0_ScukC0QrYaiStvhNZMpuRrgYkC4ZyDyZIsNzUvmfWTbKKCBZ5cquaHY2Ac08XjdVndvtpLnlTUpjjDDj8mC5z2_cbREOFUAYrnux_Y3H-et2qGv57akhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1bc066b31.mp4?token=JhxPeFdFe2NC2CIaMg8RpSQU_6txiwWbMImztvcPvg0zokte_n5RMDX4mYmBeEmjR31SkAKaQs-ncj0UMVxr6fcDnD-3LWAjlSlPbMDR-mWEmxNEgbV1JAFGe_K-msi_b7TWZlJFVRuAkHko6fQm1TwHFXzpwGoYmiQ7jRmV7ABR0S9UXLqPqLnH-oOLzhBTw0Nqtsr5CItk4f2NMFEJVQ3-DF6ClHK0_ScukC0QrYaiStvhNZMpuRrgYkC4ZyDyZIsNzUvmfWTbKKCBZ5cquaHY2Ac08XjdVndvtpLnlTUpjjDDj8mC5z2_cbREOFUAYrnux_Y3H-et2qGv57akhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور جلیلی در زمان بایدن و با دلار ۶۰ هزارتومانی: آمریکا ابزار جدیدی برای تحریم ایران ندارد و تحریم به سقفش رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/149744" target="_blank">📅 20:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149743">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه سی‌بی‌اس:
ما با درخواست ایران برای لغو تحریم‌هایی که پس از ماه ژوئن اعمال شده‌اند، مخالفت کردیم.
🔴
ما می‌خواهیم تعهدات مرتبط با هسته‌ای در پیشنهاد ایران گنجانده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/149743" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149742">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
فعالیت‌های قابل توجه هواپیماهای سنگین نیروی هوایی ایالات متحده در استان اربیل، کردستان عراق. به نظر می‌رسد عقب‌نشینی نیروهای آمریکایی در حال انجام است؛ مهلت تعیین‌شده برای عقب‌نشینی، یعنی ۳۰ سپتامبر، تنها سه روز دیگر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/149742" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149741">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI2_vIrtb6R941QV-U93bcXecdIihNPOSTet6X-Ziv_UNJ8HtKul_DAm-XL6t2ubagK3M4YAEHzDgzogOnWoR7EXm7iyWOJzMLxqLkzS_UKEvoN6JU9ZPnSN-AtC73gbmub8OGYqBf69dX-QCADQDO8jw_-DI2ebVGJG9-nyr-akhBE0uqXO3CbISZJP6HvpISVzgUxAdBus2V1kfGkPOyZFJyqIJUFtTQIw_0ifNBRescHk3xIOgsMJiGY0kgA3tQwOq0iIwtZIlQJv29FgdCoQAUGA_8eJrEFMJYfEwhYwV25gPg0xM_HNe9FmPq4y9bl6YaqMF0Xde6JhFNp4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو بلوبانک‌ بیش از ۱۰ میلیارد تومن پول تو حسابتون داشته‌باشید، از این کارتای VIP از جنس استیل بهتون میده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/149741" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149740">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/149740" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149739">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سید عباس عراقچی:"جنگ راه حل نیست. این موضوعی است که باید از طریق مذاکره حل شود، و ما در گذشته این کار را انجام داده‌ایم. ما اورانیوم را تا غلظت 60 درصد برای اهداف صلح‌آمیز غنی کرده‌ایم، و این در چارچوب تعهدات ما در پیمان منع گسترش سلاح‌های هسته‌ای (NPT) قرار دارد. ما هیچ‌گاه پیمان NPT را نقض نکرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/149739" target="_blank">📅 19:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149738">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59c715ba.mp4?token=qH8XXFEy91pbNZ6O72kN2Ct_3qoFdmvLsNu2EXMm8jh8mp_NhxUNzOr5mw0giWFFiSdrFkzgh3kZobDxDHpP66Tuf8__-nTCnPb7-BblFq1-DlYABH31JC1Ix7S3BIvoZLdcNib16kiTPQzY-F8r_txMLRUZTAwMFfZhgD9FsLoGumagPFmLd7BsSAYeI2lDPErBC7Tg4heLtj6IHO0J3HgFMB9em5kUQLA8tYA2PiTkBk5PHpCNabLHQn-Yb_VQHXf75dcnKEyEKqJ7DN1CbxPW3jGcY5h0z9-DgZohF7QkSemC8ocFVz6G26npzRilB2rsJey9iqfxEXxabE7hkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59c715ba.mp4?token=qH8XXFEy91pbNZ6O72kN2Ct_3qoFdmvLsNu2EXMm8jh8mp_NhxUNzOr5mw0giWFFiSdrFkzgh3kZobDxDHpP66Tuf8__-nTCnPb7-BblFq1-DlYABH31JC1Ix7S3BIvoZLdcNib16kiTPQzY-F8r_txMLRUZTAwMFfZhgD9FsLoGumagPFmLd7BsSAYeI2lDPErBC7Tg4heLtj6IHO0J3HgFMB9em5kUQLA8tYA2PiTkBk5PHpCNabLHQn-Yb_VQHXf75dcnKEyEKqJ7DN1CbxPW3jGcY5h0z9-DgZohF7QkSemC8ocFVz6G26npzRilB2rsJey9iqfxEXxabE7hkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه NBC: «رئیس‌جمهور ایران این هفته گفت که ایران، نقل قول، هرگز به دنبال سلاح‌های هسته‌ای نبوده است، اما ایران اورانیوم را تا غلظت ۶۰ درصد غنی کرده است. این میزان ۲۰ برابر بیشتر از غلظت اورانیوم غنی‌شده‌ای است که برای تولید برق مورد نیاز است. چرا ایران به ذخیره اورانیوم غنی‌شده با غلظت ۶۰ درصد نیاز دارد؟»
🔴
عراقچی:"خب، این سوالی است که ما در طول مذاکراتی که با ایالات متحده داشتیم، به آن پاسخ داده‌ایم. اول از همه، غنی‌سازی تا ۶۰ درصد غیرقانونی نیست. این کار همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد. ما این کار را برای اهداف خاصی، از جمله اهداف پزشکی، انجام داده‌ایم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/149738" target="_blank">📅 19:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149737">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9056ac4f3.mp4?token=Sms6zHDwgBtXNqcMrkGthEccZvCbPu6cWPj8-0mWlD9hTTwq4Uc32r7zkDDqyOZkN13tJ6inJl_HESWWjKYYbBjs9g_jY2LfpiQhc024LqFI0mTL63lFmvXREPm34l8IphdAAjmqRpbJ9FgHs3vxYHCTWTFJOdRYfhSa9T5UCfPw96LsNQOcH61fTvYzv2CXU0GAy5Svpr_LDD0VvbOYI1orUONOVYs22QYBJRwtNvlbqb4bT2Vhvl-Yzvwz7YNScA9anoWwqHR6j0H3gwMZcpbU5KFS5QV_kILxfDLH3Cc6icDTDISm5k8z7E7RCvgiLIZYluyu2CZ9bhMHWw9Vow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9056ac4f3.mp4?token=Sms6zHDwgBtXNqcMrkGthEccZvCbPu6cWPj8-0mWlD9hTTwq4Uc32r7zkDDqyOZkN13tJ6inJl_HESWWjKYYbBjs9g_jY2LfpiQhc024LqFI0mTL63lFmvXREPm34l8IphdAAjmqRpbJ9FgHs3vxYHCTWTFJOdRYfhSa9T5UCfPw96LsNQOcH61fTvYzv2CXU0GAy5Svpr_LDD0VvbOYI1orUONOVYs22QYBJRwtNvlbqb4bT2Vhvl-Yzvwz7YNScA9anoWwqHR6j0H3gwMZcpbU5KFS5QV_kILxfDLH3Cc6icDTDISm5k8z7E7RCvgiLIZYluyu2CZ9bhMHWw9Vow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: "آیا به پرزیدنت ترامپ، اعتماد دارید؟"
🔴
سید عباس
:
خب، ما به خودمان اعتماد داریم. ما برای دیپلماسی آماده هستیم. و در عین حال، برای جنگ نیز آماده‌ایم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/149737" target="_blank">📅 19:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149736">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b1c0d3e2.mp4?token=ktLPuhKKHyRkcvbbf85EZR9M1Xw334EbxY5DbzYnsDX0i_p2-kslbvpEil-r6bl_iMUpSZScFCXZ5RQRo2Bga6UGw55mir8OcwFLqYq8O07CQ9z70MaI9Z19WwJml-hvnGSFFx_UVXXhb3hVb6FQ5EJqSxd-oP6a2Fu49QZCc8Nw8LRHZFFHq24BAyifVeRJfjR30PNx_p3Da3k8YgjPQ84FQwQ0-YxqjBuffhBoYtGXHyquODI2Z_rfcyr5eZ8NLmW8tumvVXga8cA0PveBNL3rPJAuyF_zCssaNJdlMl7I0_AJrW3VZ8DEl4WHJd-bghld427lNZq8LsGqKP2BcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b1c0d3e2.mp4?token=ktLPuhKKHyRkcvbbf85EZR9M1Xw334EbxY5DbzYnsDX0i_p2-kslbvpEil-r6bl_iMUpSZScFCXZ5RQRo2Bga6UGw55mir8OcwFLqYq8O07CQ9z70MaI9Z19WwJml-hvnGSFFx_UVXXhb3hVb6FQ5EJqSxd-oP6a2Fu49QZCc8Nw8LRHZFFHq24BAyifVeRJfjR30PNx_p3Da3k8YgjPQ84FQwQ0-YxqjBuffhBoYtGXHyquODI2Z_rfcyr5eZ8NLmW8tumvVXga8cA0PveBNL3rPJAuyF_zCssaNJdlMl7I0_AJrW3VZ8DEl4WHJd-bghld427lNZq8LsGqKP2BcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: آیا این درست است که ترامپ در حال آماده شدن برای از سرگیری حملات نظامی پس از انتخابات میان دوره ای است؟
🔴
سفیر ایالات متحده در سازمان ملل:  چیزی که می‌توانم بگویم این است که رئیس جمهور همه گزینه‌ها را برای اطمینان از ایمن بودن جهان از تهدید سلطه ایران از طریق سلاح‌های هسته‌ای، باز نگه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/149736" target="_blank">📅 19:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149735">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3SBPKPI_B93QNhuNn8n3L0mSPQIQTGnuIMtJyKu_UfUq92W-fis84WJkUiJvuFo1Yb3ufvJjq11H_AjHAzIFmnAYDG-m1wrFzxXkIDDb3ySqcubSRkyaRFVGTNEiyFsqFjAiwkvElGIPMbSP9IDgTt1WB78N_1qlgg6jJDvaKIyghI3hGe96jGVowIUBYexKQ2xP16fJZCMB4-sz-Vs_yVYX9QSZKHjzaO_cQrGFJhyDrHYs-pJsT1GwdGxOGnTk4e0e4qGWe-gJR0YXpeLX8W_VxC-MfaU77pEp28iWWuwJPekY8L3EDJR6AfrWMU1n2NZ1KHmTUdlrICzqfa8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : دیوان عالی ایالات متحده آمریکا هرگز اجازه نمی‌دهد که میزوری یک پیروزی انتخاباتی داشته باشد. آن‌ها به‌طور مداوم، تاکنون سه بار، رأی قضاتی را که به تصمیمات صحیح رسیده بودند، نقض کرده‌اند.
🔴
از فرماندار و از همه مردم بزرگ میزوری که به‌شدت برای عدالت و امنیت انتخابات می‌جنگند، سپاسگزارم. روحیه و عشق فوق‌العاده‌ای به کشور ما.
🔴
من میزوری را به‌طور بزرگ، هر سه بار، بردم و نمی‌توانم بیشتر از این به انجام این کار افتخار کنم. جای فوق‌العاده‌ای — همه شما را دوست دارم!
🔴
پرزیدنت دونالد جی‌. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149735" target="_blank">📅 19:24 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
